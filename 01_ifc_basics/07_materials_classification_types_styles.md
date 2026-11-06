# Materials, classification, types, colours/styles and layers

## In plain words

An IFC model describes things (a wall, a beam, a window), and four separate mechanisms say *what they are made of, what kind they are, how they are coded and how they look*. **Materials** say what the thing is made of (a single material, or layers/profiles/parts). **Types** say "this wall is an instance of wall type EXT-300", so many walls share one definition. **Classification** attaches an outside code (Uniclass, OmniClass, Uniformat, КСИ, GB/T 51269, ETIM...) to an element, type or material. **Styles and layers** (colour, transparency, CAD-like layers) only control how geometry is drawn. They carry no engineering meaning, and people confuse them with materials all the time. Most "my IFC lost the material / the colour / the classification" tickets come from mixing up these four mechanisms or from exporter settings.

Last researched: 2026-11-06

> Research notes. The buildingSMART HTML documentation (`standards.buildingsmart.org`, `ifc43-docs...`) returned HTTP 403 to the fetch tool, so entity facts below were read from the official buildingSMART *IFC4.3.x-development* GitHub repository (the source Markdown of the same documentation) [1]-[17]. The web-search budget ran out part-way. National classification systems (КСИ, GB/T 51269, NL-SfB, CoClass, CCI) are therefore covered more thinly, and unverified items are marked. Entity names are IFC4/IFC4.3 unless stated. "IFC2x3" differences are noted where known.

---

## 1. Materials

### 1.1 The material family (what to know)

| Entity | Role | Typical user |
|---|---|---|
| `IfcMaterial` | One named material. Attributes `Name`, `Description` and `Category` (the last two are new in IFC4) [6] | Concrete C30/37, Steel S355 |
| `IfcMaterialLayer` | One layer: `Material`, `LayerThickness`, `IsVentilated`, `Name`, `Description`, `Category`, `Priority` [7] | A 12.5 mm gypsum board layer |
| `IfcMaterialLayerSet` | Ordered list of layers (`MaterialLayers`, `LayerSetName`) | A wall build-up "EXT-300" |
| `IfcMaterialLayerSetUsage` | Places a layer set relative to the element's axis or plane (occurrences only) [1] | A wall occurrence |
| `IfcMaterialProfile` / `IfcMaterialProfileSet` | Materials plus cross-section profiles (IFC4+) | Steel beam IPE300, composite section |
| `IfcMaterialProfileSetUsage` | Places a profile set relative to the member axis via `CardinalPoint` [4] | A beam or column occurrence |
| `IfcMaterialConstituent` / `IfcMaterialConstituentSet` | Parts identified only by a keyword in `Name` (IFC4+) [2] | Window: "Lining" + "Glazing" |
| `IfcMaterialList` | Old unordered list. Deprecated from IFC4, use a constituent set instead [3] | Legacy IFC2x3 files |
| `IfcRelAssociatesMaterial` | The link: `RelatedObjects` to `RelatingMaterial` [3] | All of the above |

The `RelatingMaterial` of an `IfcRelAssociatesMaterial` can be a layer set, layer set usage, profile set, profile set usage, constituent set, a single `IfcMaterial` (where the element's material use definition allows it), or the deprecated list [3]. It can be attached to element occurrences (`IfcElement` subtypes) or to element types (`IfcElementType`) [3].

### 1.2 Which structure for which element

| Element kind | Expected material structure | Source |
|---|---|---|
| Walls, slabs, roofs, coverings (layered, constant thickness) | `IfcMaterialLayerSet` on the type or occurrence, `IfcMaterialLayerSetUsage` on the occurrence | [3] |
| Beams, columns, members (extruded profiles) | `IfcMaterialProfileSet` and `IfcMaterialProfileSetUsage` | [3] |
| Doors, windows, distribution elements (parts) | `IfcMaterialConstituentSet` with keywords defined per element subtype | [3], [2] |
| Anything simple | One `IfcMaterial` | [3] |

### 1.3 Layer set usage in detail [1]

- `ForLayerSet`: the layer set.
- `LayerSetDirection`: the axis along which the layers stack. For `IfcWall` it is AXIS2 (the local y axis), for `IfcSlab` and `IfcPlate` it is AXIS3 (z).
- `DirectionSense`: POSITIVE or NEGATIVE, meaning whether layers build toward the positive or negative side of the direction, starting from the base line (MlsBase).
- `OffsetFromReferenceLine`: signed offset of that base line from the element's reference line or plane. Its sign does not change the stacking direction, and `DirectionSense` does not move the base.
- `ReferenceExtent`: new in IFC4. Only needed when `IfcMaterialLayerWithOffsets` is used.
- Thickness and offset are measured perpendicular to the layers. For a non-perpendicular (sloped) extrusion the total layer thickness can differ from the extrusion depth.
- Rule of thumb for QA: `sum(LayerThickness)` should equal the wall thickness in the body geometry (the spec's cavity-wall example says TotalThickness must equal wall thickness) [1].
- A layer set usage must never be associated with a *type*, only with occurrences. The same holds for a profile set usage [3].

### 1.4 Layer details worth testing [7]

- `LayerThickness` is `IfcNonNegativeLengthMeasure` since IFC4, so a **zero-thickness layer** (membrane, vapour barrier) is valid and may not appear in the geometry.
- `IsVentilated`: TRUE = air gap exchanging air with outside, UNKNOWN = air gap without exchange (or unknown), FALSE = solid layer (default). An air gap is modelled as a layer with `Material` empty, but an empty `Material` alone does *not* mean air gap.
- `Category` keywords in the standard: LoadBearing, Insulation, Inner finish, Outer finish.
- `Priority` (0 to 100) says which layer wins at joints and corners.

### 1.5 Profile cardinal points [5]

`CardinalPoint` is an integer. 1-9 refer to the profile's bounding box (1 bottom-left, 2 bottom-centre, 3 bottom-right, 4-6 mid-depth left/centre/right, 7-9 top left/centre/right). 10 = geometric centroid, 11-14 = bottom/left/right/top in line with the centroid, 15 = shear centre, 16-19 = same four in line with the shear centre, 20 = lowest point inside a pipe or channel. This is how a "beam top-of-steel aligned with level" is encoded.

### 1.6 Type vs occurrence material

If both an occurrence and its type have an associated material, **the occurrence wins** [3]. If only the type has it, tools should treat the occurrence as inheriting it (IfcOpenShell: `ifcopenshell.util.element.get_material(element, should_inherit=True)`, from background knowledge, not verified this session).

### 1.7 Material properties and appearance

- Engineering properties (density, strength, thermal) hang off the material via `IfcMaterialProperties` subtypes or via property sets (`Pset_MaterialCommon`, `Pset_MaterialConcrete`, ... names from background knowledge, unverified). The spec page for `IfcMaterial` only says properties are defined through subtypes of `IfcMaterialProperties` [6].
- Appearance of a material comes from `IfcMaterialDefinitionRepresentation` > `IfcStyledRepresentation` > `IfcStyledItem` (with *no* `Item`) > `IfcSurfaceStyle` [6], [31]. See section 2.
- A material can be classified (e.g. a Uniclass `Pr_` product code): `IfcRelAssociatesClassification` can relate objects and types [17], and per the forum thread many tools let users classify elements and spaces but not materials or wall layers [21].
- Materials must not be assigned to openings or virtual elements (formal rule `NoVoidElement`) [3].

### 1.8 Revit specifics (practical)

- Revit materials live in the Material Browser (tabs Identity, Graphics, Appearance, Physical, Thermal). Compound wall/floor/roof layers are Revit "structure" layers, each assigned a Revit material. On IFC export, the layers normally come out as an `IfcMaterialLayerSet` + usage, and each Revit material becomes an `IfcMaterial` named after the Revit material. A column or beam family typically exports one `IfcMaterial` (or a profile set). This is background knowledge and was not re-verified in this session.
- The Revit IFC exporter is the open-source project `Autodesk/revit-ifc`. Issues about export behaviour are tracked on GitHub, for example [23].
- Revit's built-in classification-ish parameters are **Assembly Code** (drawn from the hierarchical Uniformat list, file `UniformatClassifications.txt`, configurable in *Manage > Project Settings > Assembly Code*), **Keynote** and **OmniClass Number/Title** [20], [21].

---

## 2. Styles, colours and presentation layers

These affect **display only**. They are not materials.

| Entity | What it does | Source |
|---|---|---|
| `IfcStyledItem` | Binds a style to one geometry item (`Item`) *or*, when referenced from `IfcMaterialDefinitionRepresentation`, to a material (then `Item` must be absent). Attributes `Item`, `Styles`, `Name` | [31] |
| `IfcSurfaceStyle` | Surface appearance: `Side` (POSITIVE/NEGATIVE/BOTH) and `Styles`. Often called a "material definition" in rendering apps | [8] |
| `IfcSurfaceStyleShading` | `SurfaceColour` and `Transparency` | [30] |
| `IfcSurfaceStyleRendering` | Extends shading: `DiffuseColour`, `SpecularColour`, `SpecularHighlight`, `ReflectanceMethod` (PHONG, PHYSICAL, FLAT); transmission/reflection colour attributes deprecated in IFC4.3 | [9] |
| `IfcPresentationLayerAssignment` / `IfcPresentationLayerWithStyle` | CAD-like named layer holding shape representations or items; the "WithStyle" subtype adds on/frozen/blocked flags and layer styles | [10] |

Facts that trip people up:

- **Transparency is inverted vs. alpha**: 0.0 = opaque (default), 1.0 = fully transparent [30]. An LLM or a viewer-writer that treats it as "alpha" will make glass opaque.
- `IfcSurfaceStyle` can be attached (a) to geometry items through `IfcStyledItem` (per-element colour) or (b) to the material (colour by material). If both exist, which one a viewer shows is viewer-dependent. The spec page for `IfcStyledItem` defines no priority rules [31] (unverified in practice).
- `IfcStyledItem.Styles` should contain `IfcPresentationStyle` objects from IFC4 on. `IfcPresentationStyleAssignment` is deprecated [31].
- Presentation layers: `AssignedItems` can be a whole representation or single items, and an item's own assignment overrides the representation's. The spec says layer use should be limited to simple grouping and display [10]. They are *not* a classification, a storey or a discipline split (that is `IfcBuildingStorey`, `IfcSystem`, `IfcGroup`).
- Colours in the file are RGB intensities. The exact 0..1 range was not confirmed in the page text fetched here (the standard type is `IfcNormalisedRatioMeasure` from background knowledge, unverified).
- Revit-side: whether Revit writes `IfcSurfaceStyle` from the material's *Graphics > Shading colour* or *Appearance asset* colour is behaviour-specific and not verified here (unverified). Typical complaint: "everything is grey or white in the viewer" is usually the exporter writing no style, or a viewer ignoring it.

---

## 3. Types (IfcTypeObject)

### 3.1 The model

- `IfcTypeObject` (concrete subtypes: `IfcWallType`, `IfcDoorType`, `IfcBeamType`...) holds information shared by all occurrences. "Type" and "style" are used interchangeably [13].
- Link: `IfcRelDefinesByType` with `RelatingType` (the type) and `RelatedObjects` (the occurrences) [11]. One type to many occurrences, and each occurrence has at most one type. The inverse on the type is `Types` (named `ObjectTypeOf` before IFC4) [13].
- `IfcTypeObject.HasPropertySets` carries the shared property sets. Property set names must be unique within a type. A type must have a `Name` [13].
- Properties: an occurrence's effective properties are the union of the type's and its own. **On a name clash the occurrence value wins** (spec example: type says `ExtendToStructure` TRUE, one wall overrides to FALSE) [11], [13].
- A type can be unattached to any occurrence (e.g. library content) and can point to a catalogue via `IfcRelAssociatesLibrary` [13].
- `ApplicableOccurrence` (optional) names allowed occurrences, e.g. `IfcMember/BRACE` [13].
- `IfcTypeObject` itself should not be instantiated from IFC4 on [13].
- Type-level material/classification: both `IfcRelAssociatesMaterial` and `IfcRelAssociatesClassification` accept types [3], [17].

### 3.2 ObjectType vs PredefinedType (USERDEFINED)

- Most types and occurrences have an enum `PredefinedType` (e.g. for walls values like STANDARD, PARTITIONING, SHEAR, RETAININGWALL... from background knowledge, unverified for 4.3 exact list), always including `USERDEFINED` and `NOTDEFINED`.
- **Occurrence side:** `IfcObject.ObjectType` is "a very lightweight classifier". When `PredefinedType = USERDEFINED`, `ObjectType` stores the custom label [14].
- **Type side:** the inherited `ElementType` attribute plays that role. The formal rule `CorrectPredefinedType` says `ElementType` shall be provided if `PredefinedType` is USERDEFINED [12].
- On many occurrences `ObjectType` is also filled by exporters with the family/type name even when `PredefinedType` is not USERDEFINED. Do not assume non-empty `ObjectType` means USERDEFINED.
- Forum advice on mapping local concepts: choose the closest IFC class, refine with `PredefinedType`, then USERDEFINED + custom `ObjectType`, then add the local classification via `IfcClassificationReference`; not all software supports the last two steps [21].

### 3.3 Revit mapping (background, unverified here)

A Revit **family** + **type** (family symbol) maps to IFC *type* when the exporter creates `IfcRelDefinesByType`; Revit instances become occurrences. Per-category IFC class and predefined type can be overridden with the `IfcExportAs` (type/instance) parameter and mapping table; IFC type name typically equals the Revit type name. Mismatches between "family name:type name" in `Name` vs `ObjectType` generate many test cases.

---

## 4. Classification

### 4.1 The three entities

| Entity | Key attributes | Meaning | Source |
|---|---|---|---|
| `IfcClassification` | `Source`, `Edition`, `EditionDate`, `Name`, `Description`, `Specification` (URI/URL), `ReferenceTokens` | The classification *system* (e.g. Uniclass 2015, edition, publisher) | [15] |
| `IfcClassificationReference` | `Identification` (the code), `Name` (title), `Location` (URI), `ReferencedSource`, `Description`, `Sort` | One *item* in the system, e.g. code `Ss_25_10_30` | [16] |
| `IfcRelAssociatesClassification` | `RelatedObjects`, `RelatingClassification` | Assigns system or item to occurrences or types | [17] |

Version notes:

- IFC2x3 `ItemReference` was renamed `Identification` in IFC4 [16]. In IFC2x3 the system had no `Specification`/`Description`/`ReferenceTokens`; `Edition` became optional and `EditionDate` became an ISO 8601 `IfcDate` string in IFC4 [15]. `Specification` is the IFC4.3 URI attribute, while IFC4 used `Location` [22].
- `ReferencedSource` can point to an `IfcClassification` ("lightweight", flat) or to a parent `IfcClassificationReference` (full hierarchy) [16].
- `ReferenceTokens` mark facet boundaries, e.g. DIN 277-2 key "2.1" uses "." and OmniClass Table 13 key "13-15 11 34 11" uses "-" and " " [15].
- One relationship can carry many objects, and an object can be linked to several systems through separate relationships (the page does not state this explicitly [17], but IFC practice and the forum thread confirm multiple assignments [21]).
- The relating classification may be the system itself (object "is governed by" the system, no item) or an item [17].

Minimal illustrative STEP fragment (illustrative, not from a real file):

```
#10=IFCCLASSIFICATION('NBS','2023-04','2023-04-01','Uniclass 2015',$,'https://uniclass.thenbs.com',$);
#11=IFCCLASSIFICATIONREFERENCE($,'Ss_25_10_30','Rainscreen cladding systems',#10,$,$);
#12=IFCRELASSOCIATESCLASSIFICATION('2xYz...',#5,$,$,(#100),#11);
```
(The exact Uniclass code and title above are an example of the *shape* only, unverified.)

### 4.2 Systems you will meet

| System | Origin / scope | Code shape (example, shape only) | IFC notes |
|---|---|---|---|
| **Uniclass 2015** | NBS (UK), 12 tables: Ac, Co, En, SL, EF, Ss, Pr, TE, FI, PM, Ro, Zz. Ss = Systems, Pr = Products, EF = Elements/functions, SL = Spaces/locations [18]. Tables updated several times a year; e.g. Jan 2022 update listed Ss v1.25, Pr v1.25 [18] | `Pr_20_93_52`, `Ss_25_10_30`, `EF_25_10` | Has bSDD dictionary `identifier.buildingsmart.org/uri/nbs/uniclass2015-1` [38]. Mandated/expected in UK BIM Framework workflows (ISO 19650 info requirements, unverified detail) |
| **OmniClass** | CSI/CSC (North America), 15 hierarchical tables. Table 11 Construction Entities by Function, 21 Elements (UniFormat-based), 22 Work Results (MasterFormat-based), 23 Products (EPIC-based) [19]. Table 13 = Spaces by function (key in [15]) | `23-17 11 11`, `13-15 11 34 11` [15] | Revit families often ship with "OmniClass Number/Title" parameters [21], [36] |
| **Uniformat** | Elemental classification (ASTM E1557 / CSI-Construction Canada; levels A Substructure, B Shell, C Interiors, D Services, E Equipment & Furnishings, F Special Construction, G Sitework, from background, unverified) | `B2010`, `C1010` | Revit's **Assembly Code** list is Uniformat-based (R.S. Means hierarchy) [20]. Revit IFC export writes Assembly Code as an `IfcClassificationReference` under `IfcClassification` "Uniformat" (issue #543: reference holds code e.g. 22.21, system is "Uniformat (1998)") [23] |
| **MasterFormat** | CSI/CSC spec sections; 2018 edition uses 50 divisions 00-49 (background, unverified); basis for OmniClass Table 22 [19] | `04 21 13` (brick masonry) | Used for specifications/cost, often as a custom parameter |
| **CCI** (Construction Classification International) | CCIC collaboration, based on EN ISO 12006-2 classes; adopted/planned in several European countries (Czech BIM strategy, Lithuanian NSIK under development) [29] | (not verified) | Compared with Uniclass 2015 in a 2022 *Buildings* study [29] |
| **NL-SfB** | Dutch SfB variant, element-based (e.g. 2-digit element codes such as 21 outer walls, 22 inner walls, 23 floors, 27 roofs - from memory, unverified) | `21.1`, `(21)` (unverified) | Often used with the Dutch "BIM basis ILS". No official source fetched, mark unverified |
| **CoClass** | Svensk Byggtjänst (Sweden), Swedish application and extension of ISO 12006-2:2015, successor to BSAB 96, covers whole life cycle; licensed in tiers incl. API [28] | e.g. 2-3 letter prefixes (shape unverified) | No IFC mapping page found in this session |
| **КСИ (Russian Construction Information Classifier, Классификатор строительной информации)** | Order of Minstroy Russia No. 430/пр of 06.08.2020 approved structure and composition; 21 tables, 30,000+ elements; part of GISOGD; mandatory only where building a information model is mandatory under the Town Planning Code; synchronised with Moscow's МССК codes [25], [26] | (code shape unverified) | An update was announced 13 Jan 2021 (21 tables, 700+ changes) [25]. One search snippet linked IFC base classes to GOST R 10.0.02-2019, but the number "ГОСТ Р 10.0.03" from the task prompt was *not* confirmed (unverified) [26] |
| **GB/T 51269-2017** (建筑信息模型分类和编码标准) | China national standard "Standard for classification and coding of building information model", issued 2017-10-25, effective 2018-05-01, MOHURD announcement No. 1715 [27]. Describes OmniClass-like multi-table coding by ISO 12006-2 concepts (unverified); local BIM component standards (e.g. a Guangxi one) require compliance with it [27] | (not verified) | No official mapping table to OmniClass or an IFC implementation guide was found in this session [27] |
| **ETIM** | Product classification for technical trades (electrical, HVAC, sanitary). ETIM 9.0 and 10.0 published in bSDD; 10.0 links 97 groups and 491 product classes (of 5,799) to IFC 4.3 [24], [39]. ETIM Modelling Classes preview in bSDD since March 2025 [24] | class `EC000xxx`, feature `EF000xxx` (from background, unverified) | IFC is coarser: one IFC lamp class vs 34 ETIM lamp types [24] |

### 4.3 buildingSMART Data Dictionary (bSDD)

- bSDD is an online service hosting classes, properties, allowed values, units, translations; reachable by API (production at `api.bsdd.buildingsmart.org` per search snippet) and referenced from IFC and IDS [22], [38].
- **Mapping rule** (official docs [22]):

| bSDD | IFC4 / IFC4.3 | IFC2x3 | IDS 1.0 |
|---|---|---|---|
| Dictionary name | `IfcClassification.Name` | Name | `classification.system` |
| Dictionary URI | `Specification` (4.3), `Location` (IFC4) | not available | `classification.uri` |
| Dictionary version | `Edition` | Edition | via URI |
| Organisation code | `Source` | Source | via URI |
| Release date | `EditionDate` | EditionDate | via URI |
| Class name | `IfcClassificationReference.Name` | Name | via URI |
| Class code | `Identification` | `ItemReference` | `classification.value` |
| Class URI | `Location` | Location | `classification.uri` |

- Class URI pattern: `http://identifier.buildingsmart.org/uri/<OrganizationCode>/<DictionaryCode>/<DictionaryVersion>/class/<ClassCode>` [22].
- Practical upshot for tests: an IDS can demand "the element must carry a classification from system X with value Y or URI Z" and the check is done on `IfcClassification`/`IfcClassificationReference` [22].

### 4.4 Real-world classification issues

- Revit has no native classification concept. People use Assembly Code, Keynote or shared parameters; the exporter can be set to map a chosen parameter to an `IfcClassificationReference` [21]. Revit's *IFC Export > Classification Settings* dialog takes source/edition information (per Autodesk help, via search snippet), and a community answer says the top field may name any Revit parameter and the bottom field overrides the classification name written (BB/SfB example) [34]. Treat these as unverified UI details. Exact field names vary by exporter version.
- Exporter version change: from revit-ifc 2022.5.1.0 the `IfcRelAssociatesClassification` *name* became "Uniformat <code>" rather than "Uniformat Classification". Some viewers (an older Solibri build, BIMcollab Zoom) then showed one tree per code. The maintainer said this was by design because the relationship name is not the classification name [23]. Lesson: do not read the classification from the relationship's `Name`.
- Many viewers show property sets but not classification references, so users duplicate codes into custom Psets [21].
- Solibri reads classification references for filtering but does not write its own back into IFC [21].
- Idea-board report: the IFC exporter defines only one classification system, and a later thread says several can be added (behaviour depends on exporter version, unverified) [34].

---

## 5. Documents

Documents (specifications, datasheets, drawings, URLs) are linked, not embedded:

- `IfcDocumentReference` (`Location` = URL string, `Identification`, `Name`, `Description`, `ReferencedDocument`) points to a document or position inside it. `Name` should be given only if no `IfcDocumentInformation` is attached [32].
- `IfcDocumentInformation` carries the metadata (title, version, etc.; attributes not read in this session).
- `IfcRelAssociatesDocument` assigns a document reference or information to objects or object types (`RelatedObjects`, `RelatingDocument`) [33].
- Library/catalogue links for types use `IfcRelAssociatesLibrary` [13].

---

## 6. How these pieces fit (cheat sheet)

```
IfcWall (occurrence)
  |- IfcRelDefinesByType ---> IfcWallType (name, PredefinedType, ElementType if USERDEFINED)
  |                              |- HasPropertySets (Pset_WallCommon ...)
  |                              |- IfcRelAssociatesMaterial ---> IfcMaterialLayerSet (shared)
  |                              `- IfcRelAssociatesClassification ---> IfcClassificationReference
  |- IfcRelAssociatesMaterial ---> IfcMaterialLayerSetUsage ---> IfcMaterialLayerSet ---> layers ---> IfcMaterial
  |- IfcRelAssociatesClassification ---> IfcClassificationReference ---> IfcClassification (Uniclass 2015)
  |- IfcRelAssociatesDocument ---> IfcDocumentReference
  `- Representation ---> geometry items <--- IfcStyledItem ---> IfcSurfaceStyle (colour)
                                 `-- IfcPresentationLayerAssignment (layer name)
IfcMaterial <--- IfcMaterialDefinitionRepresentation ---> IfcStyledRepresentation ---> IfcStyledItem (no Item) ---> IfcSurfaceStyle
```

---

## 7. Test ideas for an IFC/Revit MCP server

(These are suggestions derived from the facts above. Python function names are background knowledge, unverified.)

| Scenario | What a good tool should do |
|---|---|
| "What is wall W-101 made of?" | Return layer list in order with thicknesses and materials; state if from the type or occurrence; report sum thickness; mention usage direction |
| "List all walls whose type has no material" | Walk `IfcRelDefinesByType` and `IfcRelAssociatesMaterial` on both type and occurrence |
| "Change the insulation layer to 120 mm" | Edit `LayerThickness` in the shared layer set (affects *all* walls of that type), warn about side effects, and note geometry may not update |
| "Give every beam a Uniclass code" | Create/reuse one `IfcClassification`, create references, one relationship, avoid duplicates |
| "Which elements have no classification?" | Check occurrence *and* type (inherit) for `IfcRelAssociatesClassification` |
| "Make the glass blue and 70% transparent" | Set `SurfaceColour` and `Transparency = 0.7` (not 0.3), via style on material or item |
| "Export colours by material" | Explain material-style vs item-style |
| "Rename type, then check the instances" | Occurrence properties override type properties |

---

## Typical questions people ask about this

Real questions are linked (paraphrased); the rest are marked illustrative.

1. How does IFC work with existing classification systems such as OmniClass and Uniformat, and how should they be attached? Real thread: [21] (buildingSMART forum).
2. After a Revit IFC export update, why does my viewer show a separate classification tree for every Uniformat code instead of one tree? Real: [23].
3. How do I change which classification (e.g. BB/SfB instead of Uniformat) Revit writes in the IFC? Real (Autodesk Community, search result): [34].
4. Can Revit export more than one classification system into the same IFC? Real (Autodesk Ideas / Community, search result): [34].
5. How do I get my Revit OmniClass Number / Assembly Code into an IfcClassificationReference? Real: [36] (buildingSMART knowledge base entry on Revit 2020; page not fetched, search snippet only).
6. Does the occurrence or the type win when both have a different material? (illustrative) Answer: occurrence [3].
7. Why does my wall layer set have a layer with zero thickness and is that valid? (illustrative) Yes since IFC4 [7].
8. How do I find the real thickness of an IFC wall: from geometry or from the layer set? (illustrative)
9. My beam is shifted by half its depth in another tool: is that the CardinalPoint? (illustrative) Check profile set usage cardinal point [4], [5].
10. What is the difference between `ObjectType` and `PredefinedType`, and when must I fill `ElementType`? (illustrative) [12], [14].
11. All objects are grey in my viewer: is the colour missing from the IFC or ignored by the viewer? (illustrative)
12. Is `Transparency = 0.3` mostly opaque or mostly clear? (illustrative) 0 is opaque [30].
13. What is an `IfcPresentationLayerAssignment` and does it correspond to a Revit workset/level/category? (illustrative) No; it is a CAD-style layer [10].
14. Can I put a Uniclass code on a material or a single wall layer? (illustrative) Materials can be classified in the schema [6] but tool support is thin [21].
15. What should be in `IfcClassification.Source`, `Edition`, `Specification` when using bSDD? (illustrative) See mapping table [22].
16. How do I check in an IDS that every door has a classification from a given bSDD dictionary? (illustrative) [22].
17. How do I model a cavity wall with an air gap so that it survives export? (illustrative) `IsVentilated`, material empty [7].
18. Which classification does my country use: Uniclass, CCI, NL-SfB, CoClass, КСИ, GB/T 51269? (illustrative) See table 4.2.
19. Do I have to use КСИ in Russia, and for which projects? (illustrative) Only where an information model is mandatory under the Town Planning Code, per the cited summary [26].
20. Can I link a PDF datasheet to a type so that every instance inherits it? (illustrative) `IfcRelAssociatesDocument` on the type [33].
21. How do I tell whether a property comes from the type or from the instance? (illustrative) [11], [13].
22. Why does `ItemReference` appear in IFC2x3 files and `Identification` in IFC4? (illustrative) Renamed in IFC4 [16].
23. Our IFC has material names like "Concrete, Cast-in-Place gray": how do I map them to a standard material list? (illustrative)
24. If I change a layer's thickness on a type, do all walls of that type update their geometry? (illustrative) No automatic geometry change in the file; the layer set is shared [1], [3].
25. What is the difference between `IfcMaterialLayerSetUsage` and `IfcMaterialLayerSet` and when does a missing usage break import? (illustrative)

## Common pitfalls and misconceptions

- **Colour is not material.** Colour comes from `IfcSurfaceStyle` via `IfcStyledItem`; a material may carry a style but many exporters attach styles to the geometry [31], [6].
- **Transparency is inverted** relative to alpha [30].
- **Layer set vs usage**: the usage belongs to occurrences only, never to types [3]. Layer sets can be on types.
- **Do not confuse presentation layers** with levels, worksets, disciplines or classification [10].
- **Type name vs ObjectType**: USERDEFINED requires `ElementType` on types [12], `ObjectType` on occurrences [14].
- **Occurrence overrides type**, for both properties and materials [3], [11].
- **Read classification codes from `IfcClassificationReference.Identification`** (IFC2x3: `ItemReference`) and the system from `ReferencedSource`; do not parse relationship names [23], [16].
- **bSDD fields differ between IFC2x3 and IFC4+** (`Location` vs `Specification`) [22].
- **Material list is deprecated**; old IFC2x3 files still use it [3].
- **Classification is optional and viewer-dependent**; do not claim "no classification" just because a viewer does not display it [21].
- **Unverified claims** in this file include: national code shapes (NL-SfB, CoClass, КСИ, GB/T), exact Revit UI paths for classification export, Revit's colour export rules, PredefinedType lists.

## Gaps

- buildingSMART HTML documentation pages returned HTTP 403; used the official GitHub source docs instead. Pages for `IfcMaterialLayerSet`, `IfcMaterialProfileSet`, `IfcDocumentInformation`, `IfcPresentationLayerWithStyle` attributes and the IfcWall page (404) were not read.
- Autodesk Revit help page for IFC export options not retrieved (page-not-found). Autodesk Community thread on classification returned 403.
- Web search budget was exhausted before NL-SfB, GB/T 51269 structure, KSI table structure, CCI table structure and Revit material-colour export could be searched. No suspicious or pirated sites were encountered.
- No Python IfcOpenShell docs were fetched; function names are from background knowledge.

## Sources

Official buildingSMART IFC4.3.x-development source docs (GitHub raw Markdown):
- [1] https://raw.githubusercontent.com/buildingSMART/IFC4.3.x-development/master/docs/schemas/resource/IfcMaterialResource/Entities/IfcMaterialLayerSetUsage.md
- [2] https://raw.githubusercontent.com/buildingSMART/IFC4.3.x-development/master/docs/schemas/resource/IfcMaterialResource/Entities/IfcMaterialConstituentSet.md
- [3] https://raw.githubusercontent.com/buildingSMART/IFC4.3.x-development/master/docs/schemas/core/IfcProductExtension/Entities/IfcRelAssociatesMaterial.md
- [4] https://raw.githubusercontent.com/buildingSMART/IFC4.3.x-development/master/docs/schemas/resource/IfcMaterialResource/Entities/IfcMaterialProfileSetUsage.md
- [5] https://raw.githubusercontent.com/buildingSMART/IFC4.3.x-development/master/docs/schemas/resource/IfcMaterialResource/Types/IfcCardinalPointReference.md
- [6] https://raw.githubusercontent.com/buildingSMART/IFC4.3.x-development/master/docs/schemas/resource/IfcMaterialResource/Entities/IfcMaterial.md
- [7] https://raw.githubusercontent.com/buildingSMART/IFC4.3.x-development/master/docs/schemas/resource/IfcMaterialResource/Entities/IfcMaterialLayer.md
- [8] https://raw.githubusercontent.com/buildingSMART/IFC4.3.x-development/master/docs/schemas/resource/IfcPresentationAppearanceResource/Entities/IfcSurfaceStyle.md
- [9] https://raw.githubusercontent.com/buildingSMART/IFC4.3.x-development/master/docs/schemas/resource/IfcPresentationAppearanceResource/Entities/IfcSurfaceStyleRendering.md
- [10] https://raw.githubusercontent.com/buildingSMART/IFC4.3.x-development/master/docs/schemas/resource/IfcPresentationOrganizationResource/Entities/IfcPresentationLayerAssignment.md
- [11] https://raw.githubusercontent.com/buildingSMART/IFC4.3.x-development/master/docs/schemas/core/IfcKernel/Entities/IfcRelDefinesByType.md
- [12] https://raw.githubusercontent.com/buildingSMART/IFC4.3.x-development/master/docs/schemas/shared/IfcSharedBldgElements/Entities/IfcWallType.md
- [13] https://raw.githubusercontent.com/buildingSMART/IFC4.3.x-development/master/docs/schemas/core/IfcKernel/Entities/IfcTypeObject.md
- [14] https://raw.githubusercontent.com/buildingSMART/IFC4.3.x-development/master/docs/schemas/core/IfcKernel/Entities/IfcObject.md
- [15] https://raw.githubusercontent.com/buildingSMART/IFC4.3.x-development/master/docs/schemas/resource/IfcExternalReferenceResource/Entities/IfcClassification.md
- [16] https://raw.githubusercontent.com/buildingSMART/IFC4.3.x-development/master/docs/schemas/resource/IfcExternalReferenceResource/Entities/IfcClassificationReference.md
- [17] https://raw.githubusercontent.com/buildingSMART/IFC4.3.x-development/master/docs/schemas/core/IfcKernel/Entities/IfcRelAssociatesClassification.md
- [30] https://raw.githubusercontent.com/buildingSMART/IFC4.3.x-development/master/docs/schemas/resource/IfcPresentationAppearanceResource/Entities/IfcSurfaceStyleShading.md
- [31] https://raw.githubusercontent.com/buildingSMART/IFC4.3.x-development/master/docs/schemas/resource/IfcPresentationAppearanceResource/Entities/IfcStyledItem.md
- [32] https://raw.githubusercontent.com/buildingSMART/IFC4.3.x-development/master/docs/schemas/resource/IfcExternalReferenceResource/Entities/IfcDocumentReference.md
- [33] https://raw.githubusercontent.com/buildingSMART/IFC4.3.x-development/master/docs/schemas/core/IfcKernel/Entities/IfcRelAssociatesDocument.md
- [22] https://raw.githubusercontent.com/buildingSMART/bSDD/master/Documentation/bSDD-IFC%20documentation.md (HTML view: https://github.com/buildingSMART/bSDD/blob/master/Documentation/bSDD-IFC%20documentation.md)
- [38] https://technical.buildingsmart.org/services/bsdd/referencing-bsdd-in-ids-and-ifc/ (search result, not fetched); https://technical.buildingsmart.org/services/bsdd/data-structure/ (search result, not fetched)
- Search-result pages for the same spec entities (HTML, not fetchable): https://standards.buildingsmart.org/IFC/RELEASE/IFC4_3/HTML/lexical/IfcMaterialLayerSetUsage.htm , https://standards.buildingsmart.org/IFC/RELEASE/IFC4_3/HTML/lexical/IfcRelAssociatesMaterial.htm

Classification systems and tools:
- [18] https://www.thenbs.com/knowledge/uniclass-tables-explained ; https://www.thenbs.com/knowledge/uniclass-2015-january-2022-update
- [19] https://www.csiresources.org/standards/omniclass/standards-omniclass-about
- [20] https://help.autodesk.com/cloudhelp/2018/ENU/Revit-Model/files/GUID-5900EA95-9702-4054-A849-C0A70EABB2D1.htm (Revit Uniformat Assembly Code, search snippet)
- [21] https://forums.buildingsmart.org/t/how-does-ifc-work-with-existing-classification-systems-such-as-omniclass-uniformat-etc/804
- [23] https://github.com/Autodesk/revit-ifc/issues/543
- [24] https://www.etim-international.com/etim-10-0-now-available-in-the-buildingsmart-data-dictionary/
- [39] https://www.buildingsmart.org/etim-9-0-is-now-published-in-the-bsdd/
- [25] https://www.akm.ru/press/minstroy_rossii_obnovil_klassifikator_stroitelnoy_informatsii/ (КСИ update, 13 Jan 2021)
- [26] https://pravo.ppt.ru/prikaz/rosstandart/n-618-st-185754 and https://www.normacs.info/articles/921 (search results used only for the Order 430/pr and GOST R 10.0.02-2019 mentions; contents not fetched)
- [27] https://www.chinesestandard.net/PDF/English_MS.aspx/GBT51269-2017 (search result, GB/T 51269-2017 basic data)
- [28] https://byggtjanstcms.byggtjanst.se/contentassets/d56221107b144d7496f2a9795882f851/coclass-blad-20201124.pdf and https://vpp.sbuf.se/Public/Documents/ProjectDocuments/56b8fb0a-f12e-45b0-ab49-30521fa4b649/FinalReport/SBUF%2013172%20Slutdokumentation-CoClass-v1.2.pdf (search results, CoClass summary)
- [29] https://structurae.net/en/literature/journal-article/comparative-study-of-construction-information-classification-systems-cci-versus-uniclass-2015 ; https://architektur-informatik.scix.net/pdfs/w78-2023-paper_33.pdf (search results, CCI)
- [34] https://forums.autodesk.com/t5/revit-architecture-forum/change-classification-type-in-ifc/td-p/8579247 and https://forums.autodesk.com/t5/revit-ideas/support-for-mulitible-classifications-built-in-to-the-product/idi-p/7028958 (search results, community)
- [36] https://user.buildingsmart.org/knowledge-base/how-to-deal-with-ifcclassification-using-revit-2020/ (search result; page returned 403)
