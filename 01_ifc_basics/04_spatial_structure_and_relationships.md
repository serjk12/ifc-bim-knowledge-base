# Spatial structure and relationships (IfcRel*) explained

## In plain words

An IFC file is a graph of objects (walls, doors, rooms, storeys) tied together by **relationship objects** whose names start with `IfcRel`. Nothing "sits inside" anything by itself: a door is "on level 2" only because a separate `IfcRelContainedInSpatialStructure` object points from storey "Level 2" to that door. The project tree you see in a viewer (Project > Site > Building > Storey > Space > elements) is built from just two relationships: **aggregation** (`IfcRelAggregates`, builds the skeleton) and **containment** (`IfcRelContainedInSpatialStructure`, hangs elements on the skeleton). Everything else (types, properties, materials, groups, openings, space boundaries) is yet another `IfcRel*` object. For an MCP tester this matters because almost every "find / list / count / move" request becomes "walk these relationships forwards or backwards", and most wrong answers come from walking the wrong one.

Last researched: 2026-11-06 (fact-checked 2026-11-06, see `_meta/qa/qa-basics-1.md`)

---

## 1. The spatial hierarchy and decomposition

### 1.1 The skeleton

IFC separates the **spatial structure** (a strict tree) from **spatial zones** (free-form overlays).

| Level | Entity | Notes |
|---|---|---|
| Root | `IfcProject` | Exactly one per exchange context (global rule `IfcSingleProjectInstance`); it cannot itself be decomposed [1] |
| Site | `IfcSite` | Optional in IFC4/4.3: the project can aggregate an `IfcBuilding` directly, or even an `IfcSpatialZone` as a stub for non-building projects [1] |
| Facility | `IfcBuilding` (IFC4.3 also `IfcBridge`, `IfcRoad`, `IfcRailway`, `IfcMarineFacility`, all under `IfcFacility`) | `CompositionType`: COMPLEX (building complex), ELEMENT (a building), PARTIAL (a building section) [2] |
| Storey | `IfcBuildingStorey` | Sits at the "facility part" level of the 4.3 spatial composition (the 4.3 docs say "`IfcFacilityPart`, or more specifically `IfcBuildingStorey` or `IfcSpace`" when listing allowed targets). **QA correction:** an earlier draft said it is a subtype of `IfcFacilityPart` in IFC4.3; that EXPRESS supertype could not be confirmed (IFC2x3, IFC4 and the IFC4.2 pages show `IfcSpatialStructureElement`; the official 4.3 HTML returned 403). `CompositionType` COMPLEX / ELEMENT / PARTIAL allows split-level houses [3] |
| Space | `IfcSpace` | A room/area/volume; may be aggregated under a storey or under another space (COMPLEX space group > ELEMENT space > PARTIAL space) [4] |

The hierarchy is joined by **`IfcRelAggregates`** (RelatingObject = parent/whole, RelatedObjects = children/parts). The rule for composition types: a COMPLEX parent holds ELEMENT children, an ELEMENT parent holds PARTIAL children [2][3]. Example: `IfcBuilding.IsDecomposedBy` returns `IfcBuilding` or `IfcBuildingStorey` children [2].

Spatial elements normally have **no geometry of their own** (an `IfcBuildingStorey` is mostly an elevation + placement anchor); they rely on the elements they contain. A body representation may be added when needed (this is how `IfcSpace` gets its volume) [5].

### 1.2 Two kinds of "decomposition"

| | Aggregation | Containment |
|---|---|---|
| Relationship | `IfcRelAggregates` | `IfcRelContainedInSpatialStructure` |
| Meaning | whole/part: parts only make sense as part of the whole (storey is part of building; roof slabs+rafters are part of a roof; a curtain wall assembly is part of ...) | "is located in": an independent element is placed in a spatial container |
| Cardinality | a part has exactly one whole (tree) | an element is contained in 0 or 1 spatial structure element [5][6] |
| Applies to | all `IfcObjectDefinition` subtypes (spaces, elements, types) [7] | `IfcProduct` (elements, spaces' contents, annotations); NOT other spatial elements (rule WR31) [6] |
| Dependency | whole depends on parts and vice versa; deleting the whole implies deleting parts [7] | element exists independently of the room/storey |
| Inverse attrs | `IsDecomposedBy` (on whole), `Decomposes` (on part) | `ContainsElements` (on container), `ContainedInStructure` (on element) |

Rule of thumb for testers: **"Spatial elements are aggregated; physical things are contained."** Putting an `IfcBuildingStorey` into `IfcRelContainedInSpatialStructure` is a schema violation (WR31: "must not be used to include other spatial structure elements. The spatial hierarchy is defined with IfcRelAggregates") [6].

Aggregation is also used for **non-spatial** assemblies: e.g. a stair (`IfcStair`) aggregating `IfcStairFlight` + `IfcSlab` landing; a roof aggregating slabs/beams; an `IfcElementAssembly` aggregating members. Only the *top* assembly is contained in a storey; the parts are reached through `IsDecomposedBy` (this is why naive "list everything on level 2" queries that read only `ContainsElements` miss the stair flights; see Pitfalls).

### 1.3 Spatial structure vs spatial zones

`IfcSpatialElement` has two subtypes: `IfcSpatialStructureElement` (hierarchical: site, building, storey, space) and `IfcSpatialZone` (non-hierarchical, potentially overlapping, e.g. thermal / lighting / fire-compartment / usable-area zones, can have own placement and shape) [5][8]. Its inverse attributes are `ContainsElements`, `ReferencesElements`, `ServicedBySystems`, and (IFC4.3) `IsInterferedByElements` / `InterferesElements` [5].

---

## 2. How an element gets onto a storey

### 2.1 Normal case

One `IfcRelContainedInSpatialStructure` per container: `RelatingStructure` = the storey (an `IfcSpatialElement`), `RelatedElements` = a set of `IfcProduct`s (many walls, doors, slabs in one relationship object) [6]. The file therefore usually has *one containment relationship per storey/space*, listing hundreds of elements.

Which level an element type belongs to "depends on the project and can vary by region"; IFC only insists on at most one container [6]. An element can be in a storey (typical), directly in a space (furniture, terminals, equipment), in the building (a roof, or something spanning all storeys), or in the site (external works).

### 2.2 Multi-storey elements: contain once, reference elsewhere

An element can be contained in only one container, so a column, curtain wall, stair, lift shaft or multi-storey space spanning levels 0-3 needs a convention:

- **Contained** in exactly one storey, normally the one where it starts (ground-level storey). The standard text: a multi-storey element is contained by its base storey and "referenced" by every other storey it passes through; example: a lift shaft contained by the basement and referenced by all storeys it passes through [6][9]. For spaces: "Multi storey spaces shall be spatially contained by only a single building storey" [3].
- **Referenced** by the other storeys through **`IfcRelReferencedInSpatialStructure`** (non-hierarchical, 0..n referencing containers; new in IFC2x3). The standard's own illustration: a curtain wall contained in the ground floor and referenced by the first and second floors [10][5].
- Allowed targets for referencing (QA-verified wording of the 4.3 dev docs): `IfcSite`; `IfcFacility` or its subtypes (`IfcBridge`, `IfcBuilding`, `IfcMarineFacility`, `IfcRailway`, `IfcRoad`); `IfcFacilityPart`, "or more specifically `IfcBuildingStorey` or `IfcSpace`"; and `IfcSpatialZone`. The same page says the relationship must not be used to include other spatial structure elements into a spatial structure element (hierarchy is `IfcRelAggregates`), with the exception that an `IfcSpace` can be referenced by an `IfcSpatialZone` [10]. The page's own example: a curtain wall "might span through several stories ... can be contained within the ground floor" and referenced by the other storeys it spans.

This is why a correct "everything on level 2" query must union **contained** and **referenced** elements (IfcOpenShell: `get_container` + `get_referenced_structures` / `get_structure_referenced_elements`) [11]. In practice, many exporters (including Revit; see below) do *not* write `IfcRelReferencedInSpatialStructure` for multi-level elements at all; they either split the element per level or assign it to one level only (unverified for every exporter; check each file).

### 2.3 Alternative: split at each storey

Real models avoid the multi-storey problem by splitting: one wall instance per storey. Revit's IFC option **"Split Walls, Columns, Ducts by Level"** (General tab; label as in the Revit 2024 help - the open-source exporter 26.4.1 help page words it "Split walls and columns by Level", so the label varies by version) cuts multi-level walls, columns and ducts at each level that is a building story. Elements based on a non-storey level are put on the next lower building story, with an offset [12].

### 2.4 Revit levels -> IfcBuildingStorey (quirks)

Facts from Autodesk's help and the community (QA re-read the Revit 2024 help on 2026-11-06):

1. **Only levels with the "Building Story" property checked become `IfcBuildingStorey`.** The help says "Revit only exports levels for which the Building Story parameter is enabled" (in the description of *Split Walls, Columns, Ducts by Level*, General tab). If no level is marked, Revit exports all levels used as base levels for walls, columns and ducts (community) [12][13][14].
2. **Elements on an unflagged level are re-assigned to the next lower exported storey** ("using the next lower building story as the base level, with an appropriate offset" - Revit 2024 help, QA-verified); "if none, to the next one above" comes from a community source only (unverified) [12][14]. So a wall can silently land on a storey with a different name than its Revit level.
3. **Which parameter picks the level** (community wiki, not official Autodesk): Base Level for columns, Base Constraint for walls, Level for floors, Reference Level for beams, Schedule Level for face-based families (must be set manually) [13]. The Autodesk ducts article says the duct's reference level should be the bottom level for splitting to work [15 - unverified, page returned 403 to the fetcher; summary came from search snippet].
4. **Override:** a shared/instance parameter **`IfcSpatialContainer`** with a level name, `IfcBuilding` or `IfcSite` forces the container; a level name is only valid if that level has Building Story enabled. Setting `IfcBuilding`/`IfcSite` takes the element out of every storey [13][14] (community sources; verify in the exporter version you test).
5. **Storey name and elevation:** name defaults to Identity Data name (often long); override via `IfcName` / `IfcLongName` parameters. Elevation comes from the level's Constraints Elevation, which the OSArch wiki calls "fundamentally broken in Revit" with respect to buildingSMART's intended meaning ("verify elevations in the output") (QA-verified wording) [13]. In IFC4.3 `IfcBuildingStorey.Elevation` is deprecated in favour of `Pset_BuildingStoreyCommon` (`ElevationOfSSLRelative`, `ElevationOfFFLRelative`); `IfcBuilding.ElevationOfRefHeight` is also deprecated [2][3].
6. **Only one `IfcSite` and one `IfcBuilding`** are produced; nested/multiple buildings are not supported by the Revit exporter [13] (community wiki). Revit's extra reference levels (finish floor, ceiling) have no IFC equivalent; elevations can only be recorded as values, not constraints [16].
7. **Rooms/Spaces:** both export as `IfcSpace`, Areas are lost; with "Export only elements visible in view" you must also tick the "Export rooms in 3D views" option (both on the Additional Content tab; the help says that with the option on, all rooms inside the section box of the selected 3D view are exported, or all rooms if there is no active section box) or no `IfcSpace` appears [12][13]. `IfcSpace` is contained/aggregated under the storey of its Revit level.
8. **Space boundaries** option: None / 1st level / 2nd level (2nd level splits boundaries by the spaces on the opposite side and considers material) [12].
9. Release notes of the open-source exporter mention fixes like "MEP insulation assigned to the wrong level" and assemblies being shifted/mirrored, i.e. level assignment bugs still occur between versions [17].

Other tools (Archicad, Tekla, Allplan): each maps its own "story/floor" concept to `IfcBuildingStorey` (Archicad stories; details not researched here: unverified).

---

## 3. Catalog of IfcRel* relationships

Structure: IFC4 (and 4.3) has `IfcRelationship` as the root, split into `IfcRelDecomposes`, `IfcRelAssigns`, `IfcRelAssociates`, `IfcRelDefines`, `IfcRelConnects`, `IfcRelDeclares` [18]. Relationships are "objectified": they are objects with their own GlobalId, and typically have a `Relating*` (one) side and `Related*` (many) side.

| Relationship | Plain meaning | Relating side -> Related side | Typical use / note |
|---|---|---|---|
| **IfcRelAggregates** | Whole/part (unordered) | RelatingObject -> RelatedObjects | Project>Site>Building>Storey>Space; roof>slabs; stair>flights; `IfcElementAssembly`. NoSelfReference rule [7] |
| **IfcRelNests** | Whole/part with an **order** (list) | RelatingObject -> RelatedObjects (list) | Tasks in a schedule, cost items, `IfcDistributionPort`s on a device, alignment layouts [19] |
| **IfcRelContainedInSpatialStructure** | Element is located in one spatial container | RelatingStructure (`IfcSpatialElement`) -> RelatedElements (`IfcProduct`) | "Door is in Level 2". 0..1 per element ("Any element can only be assigned once to a certain level of the spatial structure", QA-verified) [6] |
| **IfcRelReferencedInSpatialStructure** | Element is also referenced by other containers | RelatingStructure -> RelatedElements | Multi-storey elements; spatial zones referencing spaces; systems linked to spaces. 0..n [10] |
| **IfcRelServicesBuildings** | A system serves buildings/storeys/spaces/zones | RelatingSystem -> RelatedBuildings | **Deprecated in IFC4.3.0.0, use IfcRelReferencedInSpatialStructure** (QA-verified: "IFC4.3.0.0 DEPRECATION Use IfcRelReferencedInSpatialStructure instead") [20] |
| **IfcRelDefinesByProperties** | Attach property/quantity set(s) to occurrences | RelatingPropertyDefinition -> RelatedObjects (N:N) | Pset_WallCommon etc.; not for `IfcTypeObject` (type psets are in `HasPropertySets` directly) [21] |
| **IfcRelDefinesByType** | Occurrence is an instance of a type | RelatingType -> RelatedObjects (1:N) | Wall type "Generic 200mm" -> 80 walls; occurrence values override type values of the same property name [22] |
| **IfcRelDefinesByObject** | Occurrence is a declined version of another object | (in IFC4+ list) | Rare; not researched in detail (unverified) [18] |
| **IfcRelDefinesByTemplate** | Pset instance follows a property-set template | (in IFC4+ list) | Rare for testers [18] |
| **IfcRelAssociatesMaterial** | Material / layer set / profile set for elements or types | RelatingMaterial -> RelatedObjects | Wall layers; material usually on the type (IfcOpenShell `get_material` resolves occurrence then type) [11] |
| **IfcRelAssociatesClassification** | Classification reference (Uniclass, OmniClass, CCI, ...) | RelatingClassification -> RelatedObjects | Item in an external system; can also reference the system itself [23] |
| **IfcRelAssociatesDocument** | Document information/reference | RelatingDocument -> RelatedObjects | Datasheets, specs [24] |
| **IfcRelAssociatesLibrary** | Link to library reference | | Listed in schema; not researched (unverified) [18] |
| **IfcRelVoidsElement** | An opening cuts a void in an element (Boolean subtraction) | RelatingBuildingElement -> RelatedOpeningElement (1:1) | Wall -> `IfcOpeningElement` [25] |
| **IfcRelFillsElement** | An element fills an opening | RelatingOpeningElement -> RelatedBuildingElement (1:1) | Opening -> door/window [26] |
| **IfcRelConnectsPathElements** | Two path-based elements (walls) meet at ends/along path | RelatingElement / RelatedElement + RelatingConnectionType / RelatedConnectionType | ATSTART, ATEND, ATPATH, NOTDEFINED; L-shape: both ATSTART/ATEND combos; T-shape: ATPATH on one wall, ATSTART or ATEND on the other. Subtype of `IfcRelConnectsElements` (optional connection geometry) [27][28] |
| **IfcRelSpaceBoundary** (+ `1stLevel`/`2ndLevel` subtypes) | A space is bounded by an element (physical) or virtual divider | RelatingSpace, RelatedBuildingElement, ConnectionGeometry, PhysicalOrVirtualBoundary, InternalOrExternalBoundary | Energy analysis, room finishes. Virtual boundaries reference an `IfcVirtualElement` (or opening). 1st level = from inside the space only; 2nd level 2a = space on the other side, 2b = building element on the other side [29] |
| **IfcRelCoversSpaces / IfcRelCoversBldgElements** | Coverings (floor finish, tile, insulation) attached to spaces/elements | | Mentioned for spaces [4]; coverings are usually the way finishes are modelled |
| **IfcRelAssignsToGroup** | Objects are members of a group (and thus of systems/zones) | RelatingGroup -> RelatedObjects | Not hierarchical; groups can contain groups; object can be in 0..n groups [30] |
| **IfcRelAssignsToControl** | A control (cost item, constraint, performance history) applies to objects | RelatingControl -> RelatedObjects | E.g. performance history on a service element [31] |
| **IfcRelAssignsToProcess / ToResource / ToProduct / ToActor** | Object is input/output of a task; resource assigned; product-to-product; actor (person/org) responsible | | Listed in schema; 4D/5D use; details not researched (unverified) [18] |
| **IfcRelDeclares** | Project declares library objects / types / non-spatial structures | IfcContext -> definitions | Types, libraries, work plans belong to the project via this [1] |

Naming trap: **`IfcRelAssociates*` and `IfcRelDefines*` are not hierarchy**. They never change where something is in the tree.

---

## 4. Zones, systems and groups

Hierarchy: `IfcGroup` > `IfcSystem` > (`IfcZone`, `IfcDistributionSystem`, `IfcBuildingSystem`, `IfcStructuralAnalysisModel`). Members are assigned with **`IfcRelAssignsToGroup`** [30]. Because grouping is non-hierarchical, one object may belong to several groups.

| Concept | What it is | Geometry | Membership relation | Notes |
|---|---|---|---|---|
| `IfcGroup` | Arbitrary collection of objects or types | none | `IfcRelAssignsToGroup` (inverse `IsGroupedBy`) | Used e.g. for "fire compartment" sets of walls, or user selections [30] |
| `IfcSystem` / `IfcDistributionSystem` | Functional system (HVAC, drainage, power) | none | `IfcRelAssignsToGroup`; serves spaces via `IfcRelServicesBuildings` (deprecated in 4.3) or `IfcRelReferencedInSpatialStructure` [20] | Revit exports groups as `IfcSystem` types (exporter 25.4.3.0 notes) [32] |
| `IfcZone` | Grouping of `IfcSpace` (and other zones) | none: "a mere grouping" | `IfcRelAssignsToGroup`; per IFC4.3 docs only `IfcSpace`, `IfcZone`, `IfcSpatialZone` as members | Subtype of `IfcSystem` since IFC4 (was `IfcGroup`). Not part of the spatial tree, not hierarchical, a space may be in several zones [33][34] |
| `IfcSpatialZone` | Spatial zone with its own placement and shape (thermal, lighting, usable area, fire compartment...) | optional | Spaces/elements linked **by `IfcRelReferencedInSpatialStructure`** | New in IFC4; support in viewers/authoring tools is uneven (community discussions mention Archicad and Bonsai gaps) [8][34][35] |

Revit behavior (community wiki): HVAC Zones export as `IfcZone`; rooms can also be grouped into zones via a `ZoneName` parameter, but such "virtual" zones do not keep GlobalIds between exports and conflicting zone properties collapse to one set [13]. Exporter 25.2.0.5 notes "Better treatment of IfcSpatialZones and zones in general" [32].

Quirk: if one space has a different room number in each of two zones, IFC has no native place for that; community answers suggest zone-specific property sets or per-zone number properties as the pragmatic workaround [36].

**Fire compartment** is not a dedicated IFC entity. Typical choices: `IfcZone` of spaces (with `Pset_ZoneCommon`-style properties; exact Pset content unverified), `IfcSpatialZone`, or `IfcGroup` of walls/doors with a name like "FC-02". Which one a model uses must be discovered from the file.

---

## 5. Inverse navigation (reading the graph backwards)

IFC stores the link in the *relationship*, not in the element. To go from an element "up", you read **inverse attributes** (EXPRESS `INVERSE`; in IfcOpenShell they appear as normal attributes):

| From | Inverse attribute | Gives you |
|---|---|---|
| Element | `ContainedInStructure` | `IfcRelContainedInSpatialStructure` -> `.RelatingStructure` = storey/space |
| Element | `ReferencedInStructures` | `IfcRelReferencedInSpatialStructure` list |
| Element / spatial | `Decomposes` | `IfcRelAggregates` -> `.RelatingObject` (parent) |
| Element / spatial | `IsDecomposedBy` | children (`RelatedObjects`) |
| Spatial element | `ContainsElements` | contained elements via `.RelatedElements` |
| Spatial element | `ReferencesElements` | referenced elements |
| Spatial element | `BoundedBy` (IfcSpace) | `IfcRelSpaceBoundary` list |
| Element | `IsDefinedBy` | `IfcRelDefinesByProperties` and `IfcRelDefinesByType` (IFC4 also `IsTypedBy`) |
| Element | `HasAssociations` | material/classification/document relationships |
| Element | `HasOpenings` | `IfcRelVoidsElement` -> `.RelatedOpeningElement` |
| Opening | `HasFillings` | `IfcRelFillsElement` -> `.RelatedBuildingElement` (door/window) |
| Element | `HasAssignments` / `IsGroupedBy` (group side) | group memberships |
| Wall | `ConnectedTo` / `ConnectedFrom` | `IfcRelConnectsPathElements` |

(Attribute names `ContainsElements`, `ReferencesElements`, `ServicedBySystems`, `Decomposes`, `IsDecomposedBy`, `BoundedBy`, `ContainedInStructure`, `ReferencedInStructures`, `HasOpenings`, `HasFillings`, `IsNestedBy`, `IsGroupedBy` are confirmed by the standard pages or IfcOpenShell helper code [2][4][5][11]; `HasAssociations`, `IsDefinedBy`, `ConnectedTo/From`, `HasAssignments` follow the usual IFC4 inverse names but were not individually re-verified here (unverified).)

IfcOpenShell utilities (`ifcopenshell.util.element`) show the standard walks [11]:
- `get_container(element, should_get_direct=False, ifc_class=None)`: spatial container; by default walks up aggregates/parents until it finds one
- `get_decomposition(element, is_recursive=True)`: all sub-elements incl. subspaces, contained elements, aggregate parts, openings, fillings, nested parts, surface features (IFC4.3)
- `get_parts`, `get_aggregate`: aggregation down/up
- `get_referenced_structures(element)` and `get_structure_referenced_elements(structure)`: the `IfcRelReferencedInSpatialStructure` pair, "typically for multistorey elements"
- `get_grouped_by(element)`: group members

IfcOpenShell **selector syntax** [37]: `IfcWall, type=WT01, location="Level 3"`; `location=Foo` matches elements contained directly *or indirectly* (bubbles up through spaces and aggregates) in a spatial element named Foo; `parent=Foo` also any depth; for the immediate parent only use `query:"parent.Name"="My Site"`. `group`, `system`, `zone` exist as getter keys (no dedicated filters documented).

---

## 6. How typical queries walk the graph

Assume an IFC4 model, storey names "Level 1", "Level 2".

1. **All doors on level 2**
   - Find `IfcBuildingStorey` with Name "Level 2" (watch for LongName vs Name, duplicates, different `Name` from Revit level name).
   - Take `ContainsElements` -> all `RelatedElements` that are `IfcDoor`.
   - Also include doors contained in **spaces** that are aggregated under that storey (some exporters contain doors in `IfcSpace` rather than storey: use `get_decomposition` recursive, or `location="Level 2"` in selector).
   - Also add doors found through `ReferencesElements` of the storey (rare), and check doors inside **aggregates** (curtain wall doors, prefab assemblies).
   - Doors are usually in the storey of their *host wall*, found via `IfcRelFillsElement` -> opening -> `IfcRelVoidsElement` -> wall -> storey. Use this chain to answer "which doors are in wall X" or to reconcile when doors have no containment.
   - Doors can be `IfcDoor` with `PredefinedType`; check `IfcDoorStandardCase` in 2x3-style files (IfcOpenShell class filter includes subclasses [37]).

2. **All elements in a room**
   - `IfcSpace.ContainsElements` gives furniture/equipment explicitly contained in the space [4].
   - Walls "in" a room are **not** contained in it; they bound it: `IfcSpace.BoundedBy` (`IfcRelSpaceBoundary`) -> `RelatedBuildingElement`. Exists only if the exporter wrote space boundaries (Revit: setting "Space boundaries" must not be "None") [12].
   - If neither exists, only geometry (point-in-volume / bounding-box overlap) can answer; that is a computation, not a graph walk.

3. **All walls in a fire compartment**
   - If the compartment is an `IfcZone`: zone -> `IsGroupedBy`/`IfcRelAssignsToGroup.RelatedObjects` = spaces -> `BoundedBy` -> walls (needs boundaries).
   - If an `IfcGroup` of walls: group members directly.
   - If a property like `Pset_WallCommon.FireRating` or a custom `FireCompartment` property: filter elements by property, no relationship walk. Always ask which convention the file follows.

4. **All walls of wall type X on level 2** - `IfcRelDefinesByType` (type -> occurrences) intersected with storey containment.

5. **Which storey is element E on?** `E.ContainedInStructure[0].RelatingStructure`; if empty, walk `Decomposes` to the parent assembly and repeat; also check `ReferencedInStructures`. IfcOpenShell `get_container` does the climb [11].

6. **Which spaces are in zone Z / which zones is space S in?** Via `IfcRelAssignsToGroup` (inverse `HasAssignments` on the space, `IsGroupedBy` on the zone) [30][34].

7. **What does system S serve?** `ServicedBySystems` inverse on spaces (IFC4); in IFC4.3 expect `IfcRelReferencedInSpatialStructure` instead of the deprecated `IfcRelServicesBuildings` [20].

8. **Openings and windows** - wall `HasOpenings` -> opening `HasFillings` -> window [25][26].

---

## 7. Notes for testing MCP servers (IFC/Revit)

Useful test angles (what the MCP tool should do, and what a correct answer looks like):

- **Counting per storey**: expected total of elements across storeys = elements with a container + those with none; a few elements will legitimately have no container (e.g. only referenced, or aggregated parts). A tool that reports "0 elements in Level 2" for a model whose elements are in spaces is probably reading only direct containment.
- **Moving an element to another storey** must remove the element from the old `IfcRelContainedInSpatialStructure.RelatedElements` (rule: at most one container) and, ideally, change its placement; a tool that adds a second containment produces an invalid file. Deleting the last element of a relationship should delete or leave valid the relationship object (empty `RelatedElements` is invalid because the set needs at least one member; unverified for IFC4.3 cardinalities).
- **Creating a storey** requires `IfcRelAggregates` from the building, not containment.
- **Revit side**: after changing a level's "Building Story" flag, re-export and compare container names; test an element placed on an unflagged level (expect silent reassignment to the lower storey) [12][14].
- **GlobalId stability**: relationship objects have GlobalIds too; Revit virtual zones do not keep them [13].

---

## Typical questions people ask about this

1. Why does my IFC viewer show elements under "Level 1" when they are on Level 2 in Revit? (Level not flagged "Building Story" -> reassigned to next lower storey) [12][14]
2. How do I list all doors on a given level? (illustrative)
3. What is the difference between `IfcRelAggregates` and `IfcRelContainedInSpatialStructure`? [6][7]
4. Can an element be contained in two storeys? (No; use reference for the other storeys.) [6][10]
5. How should a multi-storey column / curtain wall / stair be modelled? [9][10]
6. How do I get the storey of any element when it is inside an assembly? (illustrative; `get_container` climbs aggregates) [11]
7. Why is `IfcZone` not shown in the spatial tree? [33]
8. How do I group rooms into a zone in IFC (IfcZone vs IfcSpatialZone vs IfcSystem)? [34][35]
9. A room belongs to two zones but has a different number in each: how to model it? [36]
10. How do I recreate Revit's four reference levels per storey in IFC? [16]
11. Why are my IfcSpace entities missing from a Revit IFC export? (view-export setting + rooms in 3D views option) [12][13]
12. How do I select all walls on "Level 3" of type WT01 using IfcOpenShell? (`IfcWall, type=WT01, location="Level 3"`) [37]
13. Does `location=` match elements inside rooms on that level, or only direct children? (any depth; use `parent.Name` for direct) [37]
14. How can I override which storey Revit assigns an element to? (`IfcSpatialContainer` parameter) [13][14]
15. Which walls bound a room? (space boundaries, enable in export) [12][29]
16. Why do windows not appear as children of walls? (They are linked through opening + `IfcRelFillsElement`, not aggregation or containment.) [25][26]
17. What is `IfcRelServicesBuildings` and why is it deprecated? [20]
18. How do I find all fire-rated walls in a fire compartment? (illustrative; depends on convention)
19. Why does the number of elements in the storey differ from the count in Revit? (illustrative; aggregates, split walls, unflagged levels)
20. Does IFC support nested buildings/multiple buildings on a Revit export? (Revit exporter: one site, one building) [13]
21. What does `CompositionType` COMPLEX/ELEMENT/PARTIAL mean for a storey or building? [2][3]
22. Can the project contain elements outside any storey? (Yes: building/site containment, `IfcSpatialContainer` override) [14]

Real-question sources: [33][35][36] (buildingSMART forum and OSArch threads), [16] (OSArch). Items marked illustrative are invented.

---

## Common pitfalls and misconceptions

- **"Containment = hierarchy of the model tree."** The tree is aggregation + containment together. Reading only one relationship loses nodes.
- **Reading only direct containment** misses: elements contained in spaces, parts of aggregates (stair flights, curtain wall panels), and referenced multi-storey elements.
- **Assuming referenced == contained.** `IfcRelReferencedInSpatialStructure` does not make the element "belong" to the storey; a count of elements per storey should not double count them, unless the question asks "which elements touch the storey".
- **Walls bound rooms; they are not in rooms.** Room-to-wall requires space boundaries, which Revit exports only if enabled [12].
- **Revit "Building Story" silent re-assignment** of elements on unflagged levels [12][14].
- **Storey elevation is not trustworthy** from Revit exports (community wiki says so) and the `Elevation` attribute is deprecated in IFC4.3; use placement and `Pset_BuildingStoreyCommon` [3][13].
- **`IfcZone` has no geometry; `IfcSpatialZone` may.** Not interchangeable; tool support differs [8][35].
- **Type vs occurrence**: a property may live on the type (via `IfcRelDefinesByType`) and be overridden on the occurrence by the same property name; a query reading only occurrence psets misses type psets [22].
- **Type psets use `HasPropertySets`, not `IfcRelDefinesByProperties`** [21].
- **Name vs LongName vs Revit name**: storey/space names differ between Name, LongName and Revit's Number/Name (spaces' Name defaults to the Revit Number, LongName to the Revit Name) [13].
- **IFC2x3 vs IFC4 vs IFC4.3 differences**: `IfcSpatialElement` (4), `IfcRelServicesBuildings` deprecated (4.3), `IfcFacility` (4.3) / `IfcFacilityPart` (introduced in IFC4.2 per the release notes, extended in 4.3), `IfcRelContainedInSpatialStructure.RelatingStructure` type changed `IfcSpatialStructureElement` -> `IfcSpatialElement` in IFC4 [6]. Always check the file's `FILE_SCHEMA`.
- **Empty or multiple containment relationships** per storey are legal (a storey may have several relationship objects); do not assume one.

---

## Gaps

- The official IFC4.3 documentation pages on standards.buildingsmart.org and ifc43-docs.standards.buildingsmart.org returned HTTP 403 / redirect to the 403 host to the fetcher; IFC facts were taken from the buildingSMART `IFC4.x-development` repository on GitHub (the source of the HTML docs) and from search-result summaries of the official pages. Wording may differ slightly from the published release.
- QA 2026-11-06 re-read on the IFC4.3.x-development GitHub markdown and confirmed: IfcRelContainedInSpatialStructure (at-most-one container, lift-shaft example, WR31-style rule wording; the dev page names the rule `AllowedRelatedElements`, the "WR31" numbering is from the earlier IFC4 text), IfcRelReferencedInSpatialStructure (allowed targets), IfcRelServicesBuildings (deprecation), IfcRelDefinesByProperties (type psets via `HasPropertySets`, `NoRelatedTypeObject`), IfcSpatialElement (subtypes, inverse attributes incl. `IsInterferedByElements` / `InterferesElements` new in IFC4x3), IfcBuilding (`ElevationOfRefHeight` deprecated), IfcBuildingStorey (`Elevation` deprecated in 4.3 in favour of `Pset_BuildingStoreyCommon` `ElevationOfSSLRelative` / `ElevationOfFFLRelative`). Not confirmed: the EXPRESS supertype of IfcBuildingStorey in 4.3, "new in IFC2x3" for IfcRelReferencedInSpatialStructure, IfcOpenShell function signatures (not re-read), the Autodesk duct-splitting article.
- No fetch was possible for: `IfcRelAssociatesMaterial`, `IfcRelAssignsToProcess/Resource/Product/Actor`, `IfcRelAssociatesLibrary`, `IfcRelDefinesByObject/Template`, `IfcRelConnectsPathElements` (GitHub path 404; facts via search snippet), `IfcZone` and `IfcSystem` pages on GitHub (404), Pset content such as `Pset_ZoneCommon` (not verified).
- The Autodesk "Revit IFC Manual 2.0" (PDF) could not be read as text; the Autodesk duct-splitting support article returned 403 (used only as search-snippet evidence).
- Search quota was exhausted before searching for national topics or Graphisoft/Tekla/Bentley storey mappings; Archicad, Tekla, Allplan behavior is therefore not covered. Graphisoft community page returned 403.
- No suspicious or piracy sites were encountered; a search result from a mirror domain (`dev.glassvision.dedyn.io`, mirrors of IfcOpenShell commits) was skipped and not linked.
- Real questions found (forum threads) are paraphrased, no usernames; community content is labelled as such. OSArch wiki and bim-me-up.com are community/vendor blogs, not official.

## Sources

[1] buildingSMART IFC4.x-development, IfcProject: https://github.com/buildingSMART/IFC4.x-development/blob/master/docs/schemas/core/IfcKernel/Entities/IfcProject.md
[2] buildingSMART IFC4.x-development, IfcBuilding: https://github.com/buildingSMART/IFC4.x-development/blob/master/docs/schemas/core/IfcProductExtension/Entities/IfcBuilding.md
[3] buildingSMART IFC4.x-development, IfcBuildingStorey: https://github.com/buildingSMART/IFC4.x-development/blob/master/docs/schemas/core/IfcProductExtension/Entities/IfcBuildingStorey.md (also official HTML: https://standards.buildingsmart.org/IFC/RELEASE/IFC4/FINAL/HTML/schema/ifcproductextension/lexical/ifcbuildingstorey.htm, seen in search results)
[4] buildingSMART IFC4.x-development, IfcSpace: https://github.com/buildingSMART/IFC4.x-development/blob/master/docs/schemas/core/IfcProductExtension/Entities/IfcSpace.md
[5] buildingSMART IFC4.x-development, IfcSpatialElement: https://github.com/buildingSMART/IFC4.x-development/blob/master/docs/schemas/core/IfcProductExtension/Entities/IfcSpatialElement.md
[6] buildingSMART IFC4.x-development, IfcRelContainedInSpatialStructure: https://github.com/buildingSMART/IFC4.x-development/blob/master/docs/schemas/core/IfcProductExtension/Entities/IfcRelContainedInSpatialStructure.md (official: https://standards.buildingsmart.org/IFC/DEV/IFC4_3/HTML/lexical/IfcRelContainedInSpatialStructure.html, seen in search results only)
[7] buildingSMART IFC4.x-development, IfcRelAggregates: https://github.com/buildingSMART/IFC4.x-development/blob/master/docs/schemas/core/IfcKernel/Entities/IfcRelAggregates.md
[8] buildingSMART IFC4.x-development, IfcSpatialZone: https://github.com/buildingSMART/IFC4.x-development/blob/master/docs/schemas/core/IfcProductExtension/Entities/IfcSpatialZone.md
[9] Search-result summary of IFC4.3 spatial composition/containment docs: https://standards.buildingsmart.org/IFC/DEV/IFC4_3/HTML/concepts/Object_Composition/Aggregation/Spatial_Composition/content.html and https://standards.buildingsmart.org/IFC/RELEASE/IFC4_3/HTML/concepts/Object_Connectivity/Spatial_Structure/Spatial_Containment/content.html (not fetched directly, 403)
[10] buildingSMART IFC4.x-development, IfcRelReferencedInSpatialStructure: https://github.com/buildingSMART/IFC4.x-development/blob/master/docs/schemas/core/IfcProductExtension/Entities/IfcRelReferencedInSpatialStructure.md
[11] IfcOpenShell `ifcopenshell.util.element` source (v0.8.0): https://raw.githubusercontent.com/IfcOpenShell/IfcOpenShell/v0.8.0/src/ifcopenshell-python/ifcopenshell/util/element.py
[12] Autodesk Revit 2024 Help, IFC Export Setup Options: https://help.autodesk.com/cloudhelp/2024/ENU/Revit-DocumentPresent/files/GUID-E029E3AD-1639-4446-A935-C9796BC34C95.htm
[13] OSArch wiki (community), Revit setup for OpenBIM / Revit IFC spatial hierarchy: https://wiki.osarch.org/revit-setup-for-openbim-revit-ifc-spatial-hierarchy/
[14] bim-me-up.com (vendor blog), IfcBuildingStorey: https://bim-me-up.com/en/ifcbuildingstorey/
[15] Autodesk support article on ducts not split by level (search snippet only; fetch 403): https://www.autodesk.com/support/technical/article/caas/sfdcarticles/sfdcarticles/Ducts-not-split-with-the-option-split-walls-columns-ducts-by-level-while-exporting-IFC-from-Revit.html
[16] OSArch forum (community), "[IFC] Revit levels in native IFC?": https://community.osarch.org/discussion/1605/
[17] Autodesk revit-ifc release notes v27.3.0.12: https://github.com/Autodesk/revit-ifc/releases/tag/IFC_v27.3.0.12
[18] buildingSMART IFC4.x-development, IfcKernel entities listing: https://github.com/buildingSMART/IFC4.x-development/tree/master/docs/schemas/core/IfcKernel/Entities
[19] buildingSMART IFC4.x-development, IfcRelNests: https://github.com/buildingSMART/IFC4.x-development/blob/master/docs/schemas/core/IfcKernel/Entities/IfcRelNests.md
[20] buildingSMART IFC4.x-development, IfcRelServicesBuildings: https://github.com/buildingSMART/IFC4.x-development/blob/master/docs/schemas/core/IfcProductExtension/Entities/IfcRelServicesBuildings.md
[21] buildingSMART IFC4.x-development, IfcRelDefinesByProperties: https://github.com/buildingSMART/IFC4.x-development/blob/master/docs/schemas/core/IfcKernel/Entities/IfcRelDefinesByProperties.md
[22] buildingSMART IFC4.x-development, IfcRelDefinesByType: https://github.com/buildingSMART/IFC4.x-development/blob/master/docs/schemas/core/IfcKernel/Entities/IfcRelDefinesByType.md
[23] buildingSMART IFC4.x-development, IfcRelAssociatesClassification: https://github.com/buildingSMART/IFC4.x-development/blob/master/docs/schemas/core/IfcKernel/Entities/IfcRelAssociatesClassification.md
[24] buildingSMART IFC4.x-development, IfcRelAssociatesDocument: https://github.com/buildingSMART/IFC4.x-development/blob/master/docs/schemas/core/IfcKernel/Entities/IfcRelAssociatesDocument.md
[25] buildingSMART IFC4.x-development, IfcRelVoidsElement: https://github.com/buildingSMART/IFC4.x-development/blob/master/docs/schemas/core/IfcProductExtension/Entities/IfcRelVoidsElement.md
[26] buildingSMART IFC4.x-development, IfcRelFillsElement: https://github.com/buildingSMART/IFC4.x-development/blob/master/docs/schemas/core/IfcProductExtension/Entities/IfcRelFillsElement.md
[27] buildingSMART IFC4.x-development, IfcRelConnectsElements: https://github.com/buildingSMART/IFC4.x-development/blob/master/docs/schemas/core/IfcProductExtension/Entities/IfcRelConnectsElements.md
[28] IfcConnectionTypeEnum / IfcRelConnectsPathElements (search-result summaries): https://standards.buildingsmart.org/IFC/DEV/IFC4_3/HTML/lexical/IfcConnectionTypeEnum.html and https://standards.buildingsmart.org/IFC/RELEASE/IFC2x3/TC1/HTML/ifcsharedbldgelements/lexical/ifcrelconnectspathelements.htm (not fetched directly)
[29] buildingSMART IFC4.x-development, IfcRelSpaceBoundary: https://github.com/buildingSMART/IFC4.x-development/blob/master/docs/schemas/core/IfcProductExtension/Entities/IfcRelSpaceBoundary.md
[30] buildingSMART IFC4.x-development, IfcRelAssignsToGroup: https://github.com/buildingSMART/IFC4.x-development/blob/master/docs/schemas/core/IfcKernel/Entities/IfcRelAssignsToGroup.md
[31] buildingSMART IFC4.x-development, IfcRelAssignsToControl: https://github.com/buildingSMART/IFC4.x-development/blob/master/docs/schemas/core/IfcKernel/Entities/IfcRelAssignsToControl.md
[32] Autodesk Revit IFC exporter help 25.4.40: https://up1.autodesk.com/2025/RVT/ADSKIFCExporterHelp_25_4_40.htm
[33] buildingSMART forum (community), "IfcZone & Model Tree": https://forums.buildingsmart.org/t/ifczone-model-tree/4762
[34] IfcZone docs (search-result summaries): https://standards.buildingsmart.org/IFC/DEV/IFC4_3/HTML/lexical/IfcZone.html and https://standards.buildingsmart.org/IFC/RELEASE/IFC4/FINAL/HTML/schema/ifcproductextension/lexical/ifczone.htm (not fetched directly)
[35] OSArch forum (community), "IfcSpatialZone, anyone?": https://community.osarch.org/discussion/comment/22224/
[36] buildingSMART forum (community), "Space data depending on zone": https://forums.buildingsmart.org/t/space-data-depending-on-zone/4434
[37] IfcOpenShell selector syntax (source docs): https://github.com/IfcOpenShell/IfcOpenShell/blob/v0.8.0/src/ifcopenshell-python/docs/ifcopenshell-python/selector_syntax.rst
