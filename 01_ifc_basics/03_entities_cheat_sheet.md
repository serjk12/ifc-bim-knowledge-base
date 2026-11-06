# IFC entities cheat sheet: the ~150 classes people actually meet

**Last researched: 2026-11-06** (fact-checked 2026-11-06, see `_meta/qa/qa-basics-1.md`; enumeration lists marked "QA" were re-read on the buildingSMART IFC4.3.x-development GitHub markdown, which can differ slightly from the final published HTML)

## In plain words

An IFC file is a list of typed objects. The type is the "entity" (class) name: `IfcWall`, `IfcDoor`, `IfcSpace`, `IfcPipeSegment`. Almost every question a BIM person asks a model ("how many doors on level 2?", "why did my floors become proxies?", "which walls are external?") is really a question about which entity an element has, which parent class it inherits from, which `PredefinedType` it carries, and where it sits in the spatial tree. This sheet lists the ~150 entities you meet in practice, their plain meaning, what Revit/Archicad usually produce them from, how IFC2x3, IFC4 and IFC4.3 differ, and typical `PredefinedType` values. It also lists the classic traps: `IfcBuildingElementProxy` everywhere, `IfcWall` vs `IfcWallStandardCase`, the 4.3 rename `IfcBuildingElement` -> `IfcBuiltElement`.

Conventions: `Ifc...` = entity; `...Type` = type object (the "family type" side); `PT` = PredefinedType enum. "(unverified)" = from general schema knowledge, not re-checked on a primary page during this research. [n] = source number in the Sources section.

---

## 1. Versions in one minute

| Name | Schema ID in file header | Status / note |
|---|---|---|
| IFC2x3 TC1 (2.3.0.1) | `IFC2X3` | Still the most common exchange version in practice (Revit "Coordination View 2.0", Archicad default translators) [8a][9]. Released 2007 (TC1) [1]. |
| IFC4 (4.0.0.0) / ADD2 TC1 (4.0.2.1) | `IFC4` | Adds type/occurrence symmetry (e.g. `IfcDoorType`), PredefinedType on most classes, `IfcMapConversion`, tessellated geometry. Revit "IFC4 Reference View / Design Transfer View". |
| IFC4.1, IFC4.2 | n/a | Intermediate non-final releases (alignment, then bridge/`IfcFacility`); folded into 4.3 [1]. |
| IFC4.3 (4.3.0.0 ... 4.3.2.0 = ADD2) | `IFC4X3_ADD2` (4.3.2.0) [4] | Published as **ISO 16739-1:2024** (ISO stage date 2024-03-22; buildingSMART announced ISO approval 4 Jan 2024 and publication 2 Apr 2024) [3]. Adds roads, rail, ports/waterways, geotechnics, earthworks; renames `IfcBuildingElement` -> `IfcBuiltElement` [1][5]. buildingSMART names 4.3.2.0 as the latest official version; a later revision (update vs new Part 2) was being considered, status as of Nov 2026 not confirmed (unverified) [3]. |

IFC4.3 numbers from the official release notes (the notes label them "IFC4.3 RC1", i.e. the first release candidate; QA re-read them): 62 new occurrence entities, 294 new predefined types, 40 modified items (mostly description changes), 24 deprecated entities [1]. Per domain: shared infrastructure 24 entities / 68 predefined types, railways 22 / 121, roads 7 / 39, ports and waterways 9 / 66. Final-release totals may differ.

---

## 2. Inheritance tree (the spine)

```
IfcRoot                      GlobalId, OwnerHistory, Name, Description
 |- IfcObjectDefinition
 |   |- IfcObject
 |   |   |- IfcProduct                 has Placement + Representation (geometry)
 |   |   |   |- IfcElement             physical things
 |   |   |   |   |- IfcBuildingElement  (IFC2x3, IFC4)  ==> renamed IfcBuiltElement in IFC4.3 [1][5]
 |   |   |   |   |    IfcWall, IfcSlab, IfcBeam, IfcColumn, IfcDoor, IfcWindow, IfcRoof,
 |   |   |   |   |    IfcStair, IfcRamp, IfcRailing, IfcCovering, IfcCurtainWall, IfcPlate, IfcMember,
 |   |   |   |   |    IfcFooting, IfcPile, IfcBuildingElementProxy ...
 |   |   |   |   |- IfcDistributionElement  (MEP)  -> IfcDistributionFlowElement -> IfcFlowSegment/Fitting/Terminal...
 |   |   |   |   |- IfcElementAssembly, IfcElementComponent (fasteners, reinforcement)
 |   |   |   |   |- IfcFurnishingElement -> IfcFurniture, IfcSystemFurnitureElement
 |   |   |   |   |- IfcFeatureElement -> IfcOpeningElement, IfcProjectionElement, IfcVoidingFeature (4.3), IfcSurfaceFeature (4.3)
 |   |   |   |   |- IfcGeographicElement (IFC4+), IfcTransportElement, IfcVirtualElement
 |   |   |   |- IfcSpatialElement (IFC4; IfcSpatialStructureElement in 2x3)
 |   |   |   |   |- IfcSpatialStructureElement -> IfcSite, IfcBuilding, IfcBuildingStorey, IfcSpace
 |   |   |   |   |- IfcFacility (4.3) -> IfcBuilding, IfcBridge, IfcRoad, IfcRailway, IfcMarineFacility [6]
 |   |   |   |   |- IfcSpatialZone, IfcExternalSpatialElement (IFC4)
 |   |   |   |- IfcPositioningElement -> IfcGrid, IfcLinearPositioningElement -> IfcAlignment, IfcReferent
 |   |   |   |- IfcAnnotation, IfcPort (-> IfcDistributionPort), IfcStructuralItem (analysis members)
 |   |   |- IfcProcess  -> IfcTask, IfcProcedure, IfcEvent
 |   |   |- IfcResource -> IfcLaborResource, IfcConstructionEquipmentResource ...
 |   |   |- IfcControl  -> IfcWorkPlan, IfcWorkSchedule, IfcCostSchedule, IfcCostItem(*), IfcPermit
 |   |   |- IfcActor    -> IfcOccupant ;  IfcGroup -> IfcSystem -> IfcDistributionSystem, IfcZone, IfcBuiltSystem
 |   |- IfcContext  -> IfcProject, IfcProjectLibrary           (IFC4+; project was an IfcObject in 2x3)
 |   |- IfcTypeObject -> IfcTypeProduct -> IfcElementType -> IfcWallType, IfcDoorType ...
 |- IfcRelationship  -> IfcRelAggregates, IfcRelContainedInSpatialStructure, IfcRelDefinesByType ...
 |- IfcPropertyDefinition -> IfcPropertySetDefinition -> IfcPropertySet, IfcElementQuantity
```
(*) `IfcCostItem` is under `IfcControl` in IFC4; `IfcCostSchedule` too (unverified for exact 2x3 placement.)

Key rule: **everything "physical" with a shape is an `IfcProduct`; everything with a name and GUID is an `IfcRoot`**. Types (`IfcTypeObject`) are NOT products: no placement, only shared properties and optionally `RepresentationMaps`.

In IFC4.3 `IfcBuiltElement` is **not abstract**: it can be instantiated directly for a built element that no subtype covers, and the docs advise this instead of using `IfcBuildingElementProxy` for arbitrary elements [5]. IFC4.3 docs also say `IfcBuildingElementProxy` should no longer be used as a spatial placeholder or provision; use `IfcVirtualElement` instead [5b].

---

## 3. The big table

Legend for the "Source" column: **R** = Revit, **A** = Archicad, other tools in words. Mapping is the usual default; every exporter lets users override it (see section 4).

### 3.1 Architecture / building elements

| Entity | Plain meaning | Typical source | IFC2x3 vs IFC4 vs IFC4.3 | PredefinedType examples |
|---|---|---|---|---|
| `IfcWall` | any wall | R: Walls; A: Wall tool | In 2x3 has no PT; IFC4 adds PT. 4.3: still the main wall class | `PARTITIONING, SOLIDWALL, SHEAR, PARAPET, PLUMBINGWALL, MOVABLE, RETAININGWALL, WAVEWALL, ELEMENTEDWALL, USERDEFINED, NOTDEFINED` (13 values in 4.3 incl. deprecated `STANDARD`, `POLYGONAL`) [7] |
| `IfcWallStandardCase` | wall with constant thickness, vertical extrusion, material layer set usage | R (IFC2x3 Coordination View), A (straight walls) | **Deprecated / discouraged for new export** - search summaries of the IFC4.3 and IFC4 ADD2 TC1 pages say so [2][2b], but QA found **no deprecation note** in the IFC4.3.x-development markdown of the entity (it only says "New entity in IFC2x" and that the material layer set usage "has to be given (enforced by where rule)") [26], so the exact version that deprecated it is **unverified**. The enumeration values `STANDARD` and `POLYGONAL` of `IfcWallTypeEnum` are marked deprecated (in IFC4) [7]. Some national working groups want StandardCase kept because `IfcMaterialLayerSet` is not fully usable on `IfcWall` [10]. Revit IFC4 Reference View exports `IfcWall`, 2x3 CV2.0 exports StandardCase [8a] | none (PT `STANDARD` on `IfcWall` stands for it) |
| `IfcWallElementedCase` | stud-framed wall with parts | rarely seen | Marked "Deprecated" in the IFC4 ADD2 TC1 documentation (seen on a buildingSMART forum thread, QA); community: use `IfcWall` + `ELEMENTEDWALL` [11] | - |
| `IfcSlab` | floor slab, roof slab, base slab, landing | R: Floors (and Roofs in some setups); A: Slab; A: Roof is exported as `IfcSlab` + `ROOF` in old translators [9] | PT added in IFC4; 4.3 adds infrastructure uses | `FLOOR, ROOF, LANDING, BASESLAB, APPROACH_SLAB, PAVING, WEARING, SIDEWALK, TRACKSLAB, USERDEFINED, NOTDEFINED` [12] |
| `IfcRoof` | roof as a container of slabs/members | R: Roofs (category-level), A: Roof (modern translators, unverified) | IFC2x3: no PT; IFC4: PT | `FLAT_ROOF, SHED_ROOF, GABLE_ROOF, HIP_ROOF, HIPPED_GABLE_ROOF, GAMBREL_ROOF, MANSARD_ROOF, BARREL_ROOF, RAINBOW_ROOF, BUTTERFLY_ROOF, PAVILION_ROOF, DOME_ROOF, FREEFORM` [13] |
| `IfcCovering` | thin finish layer: ceiling, floor finish, cladding, insulation | R: Ceilings; also Duct/Pipe Insulation (`INSULATION`), Duct Lining (`WRAPPING`) [14] | 2x3 has PT too (CEILING, FLOORING, CLADDING, ROOFING, INSULATION, MEMBRANE...) | `CEILING, FLOORING, CLADDING, ROOFING, MOLDING, SKIRTINGBOARD, INSULATION, MEMBRANE, SLEEVING, TOPPING, WRAPPING, COPING` [15] |
| `IfcDoor` | door | R: Doors; A: Door | 2x3: `IfcDoorStyle` carries type info and `IfcDoor` has no PT; IFC4: `IfcDoorType` (replaces style); 4.3: types extended | `DOOR, GATE, TRAPDOOR, BOOM_BARRIER, TURNSTILE, USERDEFINED, NOTDEFINED` (4.3 list, QA-verified) [16]; IFC4 had fewer values (unverified) |
| `IfcWindow` | window | R: Windows; A: Window | same pattern: `IfcWindowStyle` (2x3) -> `IfcWindowType` | `WINDOW, SKYLIGHT, LIGHTDOME, USERDEFINED, NOTDEFINED` (4.3, QA-verified) |
| `IfcCurtainWall` | curtain wall assembly | R: Curtain Walls / Curtain Systems; A: Curtain Wall | IFC4 expects the panels (`IfcPlate` `CURTAIN_PANEL`/`IfcWindow`/`IfcDoor`) and mullions (`IfcMember` `MULLION`) aggregated via `IfcRelAggregates` | `NOTDEFINED` mostly |
| `IfcPlate` | thin flat element (curtain panel, sheet, plate) | R/A curtain wall panels; steel plates (Tekla) | 2x3 had PT-less; IFC4 added PT | `CURTAIN_PANEL, SHEET, FLANGE_PLATE, WEB_PLATE, STIFFENER_PLATE, GUSSET_PLATE, COVER_PLATE, SPLICE_PLATE, BASE_PLATE, USERDEFINED, NOTDEFINED` (4.3, QA-verified) |
| `IfcMember` | linear non-load-bearing or structural bar: mullion, brace, rafter, stud, purlin | R: Structural Framework (braces), curtain mullions | IFC4 PT; 4.3 adds cables/arches | `BRACE, CHORD, COLLAR, MEMBER, MULLION, PLATE, POST, PURLIN, RAFTER, STRINGER, STRUT, STUD, STIFFENING_RIB, ARCH_SEGMENT, SUSPENSION_CABLE, SUSPENDER, STAY_CABLE, STRUCTURALCABLE, TIEBAR` [17] |
| `IfcBeam` | horizontal load-bearing member | R: Structural Framing (beam); A: Beam | IFC4 PT | `BEAM, JOIST, HOLLOWCORE, LINTEL, SPANDREL, T_BEAM, GIRDER_SEGMENT, DIAPHRAGM, PIERCAP, HATSTONE, CORNICE, EDGEBEAM, USERDEFINED, NOTDEFINED` (4.3, QA-verified; the last six bridge-oriented values are 4.3 additions) |
| `IfcColumn` | vertical load-bearing member | R: Structural Columns, Columns; A: Column | IFC4 PT | `COLUMN, PILASTER, PIERSTEM, PIERSTEM_SEGMENT, STANDCOLUMN, USERDEFINED, NOTDEFINED` (4.3, QA-verified) |
| `IfcStair` / `IfcStairFlight` | stair assembly / one flight | R: Stairs (Revit often needs overrides; Revit 'Stairs' category not mapped by default in the OSArch rule list [14]); A: Stair | IFC4 `IfcStair` can aggregate `IfcStairFlight` + landing `IfcSlab` | `STRAIGHT_RUN_STAIR, TWO_STRAIGHT_RUN_STAIR, QUARTER_WINDING_STAIR, QUARTER_TURN_STAIR, HALF_WINDING_STAIR, HALF_TURN_STAIR, TWO_QUARTER_WINDING_STAIR, TWO_QUARTER_TURN_STAIR, THREE_QUARTER_WINDING_STAIR, THREE_QUARTER_TURN_STAIR, SPIRAL_STAIR, DOUBLE_RETURN_STAIR, CURVED_RUN_STAIR, TWO_CURVED_RUN_STAIR, LADDER, USERDEFINED, NOTDEFINED` (4.3, QA-verified; `LADDER` is in the 4.3 list) |
| `IfcRamp` / `IfcRampFlight` | ramp | R: Ramps [14]; A: Slab/Stair tool variants | same | `STRAIGHT_RUN_RAMP, TWO_STRAIGHT_RUN_RAMP, QUARTER_TURN_RAMP, TWO_QUARTER_TURN_RAMP, HALF_TURN_RAMP, SPIRAL_RAMP, USERDEFINED, NOTDEFINED` (4.3, QA-verified) |
| `IfcRailing` | railing, guardrail, handrail | R: Railings [14]; A: Railing | IFC4 PT | `HANDRAIL, GUARDRAIL, BALUSTRADE, FENCE, USERDEFINED, NOTDEFINED` (4.3, QA-verified) |
| `IfcFooting` | footing / foundation element | R: Structural Foundations; Wall Foundation | 4.3 PT list: | `FOOTING_BEAM, PAD_FOOTING, PILE_CAP, STRIP_FOOTING` (+`CAISSON_FOUNDATION`, deprecated since IFC4x2) [18] |
| `IfcPile` | pile | R: via override | IFC4 PT | `BORED, DRIVEN, JETGROUTING, COHESION, FRICTION, SUPPORT, USERDEFINED, NOTDEFINED` (4.3, QA-verified) |
| `IfcShadingDevice` | louvres, awnings | R: override (Generic Model) | IFC4+ | `JALOUSIE, SHUTTER, AWNING, USERDEFINED, NOTDEFINED` (4.3, QA-verified) |
| `IfcChimney` | chimney | rare | IFC4 | `NOTDEFINED` |
| `IfcBearing` | bridge bearing | civil tools | IFC4.2/4.3 era [6] | `ELASTOMERIC, POT, ...` (unverified) |
| `IfcFurniture` / `IfcFurnishingElement` | movable furniture / equipment | R: Furniture, Casework, Specialty Equipment (override); A: Object | 2x3: `IfcFurnishingElement` generic; IFC4 adds `IfcFurniture`, `IfcSystemFurnitureElement`; Revit's older list shows `IfcFurnishingElement`, `IfcFurnitureType`, `IfcSystemFurnitureElementType` [14b] | `CHAIR, TABLE, DESK, BED, FILECABINET, SHELF, SOFA, TECHNICALCABINET, ...` (unverified) |
| `IfcBuildingElementProxy` | "generic built thing", no semantic meaning | R: Generic Models (default), anything not mapped, in-place families, invalid IFC class names [19][20]; A: Morph (unverified) | exists in all versions; in 4.3 not deprecated but discouraged as spatial placeholder; use `IfcBuiltElement` directly for arbitrary built elements [5][5b]. The release-notes page lists it in a deprecation bullet list [1], but the entity page itself does not mark it deprecated [5b]. (Conflict: treat as "discouraged, not removed".) | `COMPLEX, ELEMENT, PARTIAL, PROVISIONFORVOID, PROVISIONFORSPACE, USERDEFINED, NOTDEFINED` (IFC4 values, unverified in 4.3) |
| `IfcBuiltElement` | 4.3 name of the old `IfcBuildingElement`; non-abstract | any | **New name in 4.3** [1][5]; `IfcBuildingElement` in 2x3/IFC4 | - |
| `IfcElementAssembly` | named assembly of elements (truss, rebar cage, stair + railing set) | R: Assemblies / Groups; Tekla assemblies | exists in all | `GIRDER, TRUSS, BRACED_FRAME, ...` (unverified) |
| `IfcBuildingElementPart` | sub-part of a layered element (e.g. a layer of a wall) | A: "split composite into parts" (IFC4 RV option [9b]); R: option | IFC4+ | `INSULATION, PRECASTPANEL, APRON, ARMOURUNIT, SAFETYCAGE, USERDEFINED, NOTDEFINED` (4.3, QA-verified) |
| `IfcVirtualElement` | invisible boundary element/space separator | rare | all; 4.3 says to use it instead of proxy for spatial placeholders [5b] | - |
| `IfcGeographicElement` | terrain, trees, vegetation | R: Topography (override), Planting | IFC4 (new); `IfcSite` terrain in 2x3 | `TERRAIN, VEGETATION, ...` (unverified) |
| `IfcTransportElement` | elevator, escalator, moving walkway | R: override of Generic Models (see report of escalators dropping out of export when class stayed proxy [20]) | all | `ELEVATOR, ESCALATOR, MOVINGWALKWAY` |

### 3.2 Openings and fills

| Entity | Plain meaning | Source | Notes |
|---|---|---|---|
| `IfcOpeningElement` | a void cut into a wall/slab | R/A exporters generate it for every hosted door/window/opening | linked by `IfcRelVoidsElement` to host; filled by `IfcRelFillsElement` to the door/window. PT `OPENING`, `RECESS` (IFC4, unverified). Not an "element you design", a derived subtraction. |
| `IfcRelVoidsElement` | wall HAS opening | - | the "opening -> host" link |
| `IfcRelFillsElement` | opening IS FILLED BY door/window | - | |
| `IfcVoidingFeature`, `IfcSurfaceFeature` (4.3) | typed voiding/surface features (groove, chamfer, mark) | Tekla-ish | new in 4.3 (present in the structural elements domain list [18b]) |
| `IfcProjectionElement` | a bump added to an element | rare | |

### 3.3 Spatial structure

| Entity | Plain meaning | Source | Notes |
|---|---|---|---|
| `IfcProject` | root of the file (units, contexts) | R: project; A: project | exactly one per file; `UnitsInContext` and `RepresentationContexts` live here |
| `IfcSite` | land plot | R: Site / project location; A: Site | `RefLatitude`, `RefLongitude`, `RefElevation`, `LandTitleNumber`. Revit exports `IfcSite` (`IfcSite` is also in Revit's mapping list [14b]) |
| `IfcBuilding` | one building | R: project info; A: building | 4.3: `IfcBuilding` is an `IfcFacility` [6] |
| `IfcBuildingStorey` | floor level | R: Levels; A: Stories | `Elevation` attribute; Revit levels are mapped by level; in IFC the building storey "contains" elements through `IfcRelContainedInSpatialStructure` |
| `IfcSpace` | room / zone volume | R: Rooms (and MEP Spaces if exported); A: Zones | PT `SPACE, PARKING, GFA, INTERNAL, EXTERNAL, BERTH` (BERTH new in 4.3) [21]. Bounded by walls via `IfcRelSpaceBoundary` (1st/2nd level exist in IFC4.3 listing [18c]) |
| `IfcSpatialZone` | non-physical zone not part of the storey tree (fire compartment, thermal zone) | rare | IFC4 |
| `IfcZone` | group of spaces (a *system*, not spatial element) | R: Zone; A: zone grouping | IFC2x3 and later; uses `IfcRelAssignsToGroup` |
| `IfcExternalSpatialElement` | outdoor space bounding region | rare | IFC4; no IFC2x3 counterpart, sometimes downgraded to `IfcSpace` [22] |
| `IfcFacility` | umbrella for building/bridge/road/rail/marine | - | IFC4.3; subtypes `IfcBridge`, `IfcRoad`, `IfcRailway`, `IfcMarineFacility`; aggregated under project/site/another facility [6] |
| `IfcFacilityPart` | sub-division of a facility (segment, junction, above/underground) | - | Introduced in IFC4.2 (release notes list it under the IFC4.2 spatial-structure basis); the 4.3 notes say `IfcBridgePart` is now covered by `IfcFacilityPart` through an EXPRESS SELECT (QA-checked) [1] |
| `IfcBuiltSystem` | system of built elements | rare | 4.3 rename of `IfcBuildingSystem` [1] |
| `IfcGrid` | grid lines (column grid) | R: Grids; A: Grid | positioning element, `IfcGridAxis` |
| `IfcAnnotation` | 2D/3D annotation geometry | R: text, dimensions; in Revit mapping list [14b] | |
| `IfcRelAggregates` | whole/part decomposition (project -> site -> building -> storey) | - | |
| `IfcRelContainedInSpatialStructure` | element sits in storey/building/site | - | the usual "which level is this wall on?" source |
| `IfcRelReferencedInSpatialStructure` | element is referenced but not contained | - | e.g. a curtain wall spanning several storeys |

Containment rule per the docs: default container for an element is `IfcBuildingStorey`; if it cannot be assigned to a storey, `IfcBuilding`; if it is outside a building, `IfcSite` [5b].

### 3.4 MEP (building services)

IFC hierarchy: `IfcDistributionElement` -> `IfcDistributionFlowElement` -> (`IfcFlowSegment` duct/pipe/cable run, `IfcFlowFitting` bend/tee, `IfcFlowTerminal` diffuser/outlet/fixture, `IfcFlowController` valve/damper/switch, `IfcFlowMovingDevice` pump/fan, `IfcFlowStorageDevice` tank, `IfcFlowTreatmentDevice` filter, `IfcEnergyConversionDevice` boiler/chiller/coil), plus `IfcDistributionControlElement` (sensor, actuator, controller, alarm). In IFC4 each has concrete subclasses; IFC2x3 mostly had generic occurrence classes plus detailed types (e.g. `IfcFlowSegment` typed by `IfcDuctSegmentType`) (unverified, consistent with the IFC4 "occurrence entities" change).

| Entity | Plain meaning | Source (Revit category) | PT examples |
|---|---|---|---|
| `IfcDuctSegment` | straight duct | Ducts | `RIGIDSEGMENT, FLEXIBLESEGMENT` [23] |
| `IfcDuctFitting` | duct elbow, tee, transition | Duct Fittings | `BEND, CONNECTOR, ENTRY, EXIT, JUNCTION, OBSTRUCTION, TRANSITION` (unverified) |
| `IfcPipeSegment` / `IfcPipeFitting` | pipe, pipe fitting | Pipes, Pipe Fittings | `RIGIDSEGMENT, FLEXIBLESEGMENT, CULVERT, GUTTER, SPOOL` (unverified) |
| `IfcCableCarrierSegment` / `Fitting` | cable tray, conduit | Cable Tray, Conduit | `CABLETRAYSEGMENT, CONDUITSEGMENT, ...` |
| `IfcCableSegment` | cable | rare | `CABLESEGMENT, CONDUCTORSEGMENT, ...` |
| `IfcAirTerminal` | diffuser, grille | Air Terminals | `DIFFUSER, GRILLE, LOUVRE, REGISTER` |
| `IfcSanitaryTerminal` | WC, sink, urinal | Plumbing Fixtures | `WASHHANDBASIN, WCSEAT, TOILETPAN, SHOWER, SINK, ...` |
| `IfcLightFixture` / `IfcLamp` | luminaire | Lighting Fixtures | `DIRECTIONSOURCE, POINTSOURCE, SECURITYLIGHTING` |
| `IfcElectricAppliance`, `IfcOutlet`, `IfcSwitchingDevice`, `IfcProtectiveDevice` | sockets, switches, breakers | Electrical Fixtures | `POWEROUTLET, TELEPHONEOUTLET, ...` |
| `IfcElectricDistributionBoard` (2x3, IFC4) -> `IfcDistributionBoard` (4.3) | electrical panel | Electrical Equipment | 4.3 deprecation noted in release notes [1] |
| `IfcValve`, `IfcDamper`, `IfcFlowMeter` | controllers | Pipe/Duct Accessories (override) | `ISOLATING, CHECK, ...` |
| `IfcPump`, `IfcFan`, `IfcCompressor` | moving devices | Mechanical Equipment (override) | `CIRCULATOR, ...`, `CENTRIFUGALAIRFOIL, ...` |
| `IfcBoiler`, `IfcChiller`, `IfcCoil`, `IfcUnitaryEquipment`, `IfcAirToAirHeatRecovery` | HVAC plant | Mechanical Equipment | many |
| `IfcTank`, `IfcFilter` | storage / treatment | Mechanical Equipment | |
| `IfcSensor`, `IfcActuator`, `IfcController`, `IfcAlarm` | controls | Communication/Data/Security devices (override) | |
| `IfcDistributionPort` | connection point on equipment, with flow direction | Revit connectors | `FlowDirection SOURCE/SINK/SOURCEANDSINK`; `SystemType` (supply air, return air...) ; linked with `IfcRelConnectsPorts` and `IfcRelConnectsPortToElement` (both in the 4.3 doc list [6b]) |
| `IfcDistributionSystem` | named system (Supply Air 1, Domestic Cold Water) | R: MEP systems | grouped through `IfcRelAssignsToGroup`; PT like `VENTILATION, DOMESTICCOLDWATER, SANITARY, ELECTRICAL, ...` (unverified) |

Practical Revit note: "Mechanical Equipment" cannot be split by the category table into pump vs. boiler vs. AHU; use `IfcExportAs` per family, otherwise you get proxies [20][14]. Sources for Revit MEP default mappings are not backed by a primary page here (unverified).

### 3.5 Structural

| Entity | Plain meaning | Source | Notes |
|---|---|---|---|
| `IfcBeam`, `IfcColumn`, `IfcMember`, `IfcPlate`, `IfcFooting`, `IfcPile`, `IfcSlab`, `IfcWall` | physical structural elements (see 3.1) | R: Structural Framing/Columns/Foundation; A; Tekla | Revit hard fallback: Structural Beam -> `IfcBeam`, Structural Brace -> `IfcMember`, Structural Footing -> `IfcFooting`, Structural Column -> `IfcColumn` [14] |
| `IfcReinforcingBar` | single rebar | R: Rebar [14]; Tekla; Allplan | PT `ANCHORING, EDGE, LIGATURE, MAIN, PUNCHING, RING, SHEAR, STUD, SPACEBAR, USERDEFINED, NOTDEFINED` (4.3, QA-verified); has `NominalDiameter`, `BarLength`, `SteelGrade` |
| `IfcReinforcingMesh` | welded wire mesh | R: Fabric Sheet (limited) | |
| `IfcReinforcingElement` / `IfcReinforcingBarType` / `IfcReinforcingMeshType` | rebar abstract/type | | present in the 4.3 structural elements domain [18] |
| `IfcTendon`, `IfcTendonAnchor`, `IfcTendonConduit` | prestress tendon, anchor, duct | precast / bridge tools | `IfcTendonConduit` present in 4.3 domain list [18] |
| `IfcDeepFoundation`, `IfcCaissonFoundation` | foundations (abstract / caisson) | | in the 4.3 list [18] |
| `IfcStructuralAnalysisModel` | container of analysis objects | R: Analytical model export (Structural Analysis View, limited); Robot, SAF | needs MVD "Structural Analysis View" (unverified) |
| `IfcStructuralCurveMember` / `IfcStructuralSurfaceMember` | analytical beam / slab | | `IfcStructuralItem` subtypes |
| `IfcStructuralPointConnection` / `IfcStructuralCurveConnection` | nodes / edge connections | | |
| `IfcStructuralLoadCase`, `IfcStructuralLoadGroup`, `IfcStructuralPointAction`, `IfcStructuralCurveAction`, `IfcStructuralSurfaceAction` | load cases and actions | | `IfcStructuralResultGroup` for results |
| `IfcBoundaryNodeCondition` | support condition | | |
| `IfcRelConnectsStructuralMember`, `IfcRelAssignsToProduct`, `IfcRelAssociates` | analytical <-> physical link | | |

### 3.6 Infrastructure (IFC4.3)

Release-notes counts: shared infrastructure 24 new entities, railways 22, roads 7, ports and waterways 9 [1].

| Entity | Plain meaning | Notes |
|---|---|---|
| `IfcAlignment` | centreline-like reference for roads/rail: horizontal + vertical (+ cant) layouts. The release notes discuss alignment as an IFC4.1 addition and an enhanced definition in 4.3 (the entity name itself is not listed in the notes) | Components `IfcAlignmentHorizontal`, `IfcAlignmentVertical`, `IfcAlignmentCant`, `IfcAlignmentSegment` [6c]; shape reps: `IfcCompositeCurve` (2D), `IfcGradientCurve` (3D without cant), `IfcSegmentedReferenceCurve` (3D with cant), polylines for survey data [6c]. Parent chain: `IfcLinearPositioningElement` -> `IfcPositioningElement` -> `IfcProduct` [6d] |
| `IfcReferent` | named station/chainage marker on an alignment (e.g. km 12+500) | positioning element [6d] |
| `IfcLinearPlacement` | "place this at distance X along alignment, offset Y" | placement kind alongside `IfcLocalPlacement` [6]; the release notes list linear placement as an IFC4.1 feature (ISO 19148-based) and the rail version `IfcLinearPlacementWithInclination` as new in 4.3 [1] |
| `IfcRoad` | road facility | new in 4.3 [1] |
| `IfcRailway` | railway facility | new in 4.3 [1] |
| `IfcBridge` | bridge facility | listed under the IFC4.2 release in the notes [1], part of 4.3 |
| `IfcMarineFacility` | port/waterway facility | new in 4.3 [1] |
| `IfcFacilityPart` | segment / junction / sub-structure of a facility | introduced in IFC4.2, extended in 4.3 where it covers `IfcBridgePart` [1] (the dev-docs `IfcFacilityPart` page names `IfcProduct` as supertype for placement and says it "provides for spatial breakdown of built facilities", QA) |
| `IfcPavement`, `IfcCourse` | pavement; layered course | `IfcCourseTypeEnum`: `ARMOUR, FILTER, BALLASTBED, CORE, PAVEMENT, PROTECTION` [24]; pavement is also expressed with `IfcSlab` PT `PAVING`, `WEARING` [12] |
| `IfcKerb` | kerb | new in 4.3 roads [1] |
| `IfcRail`, `IfcTrackElement` | rail, track elements | new in 4.3 railways [1] |
| `IfcSign`, `IfcSignal` | road sign, rail signal | new in 4.3 shared infrastructure [1] |
| `IfcEarthworksCut`, `IfcEarthworksFill`, `IfcEarthworksElement`, `IfcReinforcedSoil` | cut/fill volumes, reinforced soil | new in 4.3 [1] |
| `IfcGeotechnicalAssembly`, `IfcGeotechnicalElement`, `IfcGeotechnicalStratum`, `IfcGeomodel`, `IfcGeoslice`, `IfcBorehole`, `IfcSolidStratum`, `IfcVoidStratum`, `IfcWaterStratum` | geotechnical model, boreholes, soil strata | new in 4.3 [1] |
| `IfcImpactProtectionDevice` | crash barrier / impact attenuator | new in 4.3; absorbs `IfcVibrationIsolator`/`IfcVibrationDamper` [1] |
| `IfcMooringDevice`, `IfcNavigationElement`, `IfcConveyorSegment`, `IfcLiquidTerminal` | ports and waterways elements | new in 4.3 [1] |
| `IfcPlant` | vegetation/plant | new in 4.3 [1] |
| `IfcCivilElement` | generic civil element (IFC4.2) | deprecated in 4.3 per release notes [1] |
| `IfcSectionedSolidHorizontal`, `IfcSectionedSurface` | geometry swept along an alignment through cross-sections | `IfcSectionedSolidHorizontal` named for facility body geometry [6] (the release notes list it as a new IFC4.1 geometry representation, not a 4.3 one); `IfcSectionedSurface` new in 4.3 roads [1] |

### 3.7 Assemblies, groups, systems, types

| Entity | Plain meaning | Notes |
|---|---|---|
| `IfcRelAggregates` | whole/parts (assembly, stair -> flights, curtain wall -> panels) | |
| `IfcRelNests` | ordered nesting (ports on equipment) | |
| `IfcGroup`, `IfcSystem`, `IfcZone`, `IfcInventory` | arbitrary groups; system; zone; inventory | `IfcRelAssignsToGroup` |
| `IfcTypeObject`, `IfcTypeProduct`, `IfcElementType` and `IfcWallType`, `IfcDoorType`, `IfcWindowType`, `IfcSlabType`, `IfcBeamType`, `IfcColumnType`, `IfcPipeSegmentType` ... | the "family type" | Linked by `IfcRelDefinesByType`. In IFC4, PT should be on the type if a type is assigned (docs: occurrence PT "should be used only if no type object is assigned that provides its own PredefinedType") [5b] |
| `IfcRelDefinesByType` | occurrence -> type | In Revit: Family Type -> `IfcXxxType` |
| `IfcRelDefinesByProperties` | occurrence/type -> property set | |
| `IfcRelAssociatesMaterial` | element -> material or layer set | |
| `IfcRelAssociatesClassification` | element -> classification reference | |
| `IfcRelConnectsElements`, `IfcRelConnectsPathElements`, `IfcRelConnectsWithRealizingElements`, `IfcRelCoversBldgElements`, `IfcRelInterferesElements` | wall joins, connections, coverings, clashes | in the 4.3 lists [6b][25] |

### 3.8 Resources: properties, quantities, materials, classification

| Entity | Plain meaning | Notes |
|---|---|---|
| `IfcPropertySet` | named bag of properties (`Pset_WallCommon`, custom sets) | `Pset_` prefix = buildingSMART standard set; custom sets must not start with `Pset_` |
| `IfcPropertySingleValue` | name + value + unit | typed values: `IfcLabel`, `IfcBoolean`, `IfcReal`, `IfcLengthMeasure` ... |
| `IfcPropertyEnumeratedValue`, `IfcPropertyBoundedValue`, `IfcPropertyListValue`, `IfcPropertyTableValue`, `IfcComplexProperty` | other property kinds | |
| `IfcPropertySetTemplate` (IFC4) | defines a property set definition | used by bSDD/IDS tooling |
| `IfcElementQuantity` | quantity set (`Qto_WallBaseQuantities`, `BaseQuantities` in 2x3) | listed in the core docs [6] |
| `IfcQuantityLength`, `IfcQuantityArea`, `IfcQuantityVolume`, `IfcQuantityWeight`, `IfcQuantityCount`, `IfcQuantityTime` | quantity values | `NetVolume`, `GrossVolume`, `NetSideArea` ... |
| `IfcMaterial` | one material | `Name`, `Category` (IFC4) |
| `IfcMaterialLayerSet`, `IfcMaterialLayer`, `IfcMaterialLayerSetUsage` | layered build-up (walls, slabs) | Usage is mandatory for `IfcWallStandardCase` [26] |
| `IfcMaterialProfileSet`, `IfcMaterialProfile` | extruded profile materials (beams, columns), IFC4+ | |
| `IfcMaterialConstituentSet` (IFC4) | composition without layers; counterpart `IfcMaterialList` in 2x3 [22] | |
| `IfcClassification`, `IfcClassificationReference` | classification system and a code (Uniclass, OmniClass, CCI, Uniformat, national) | 2x3: `IfcClassification` + `IfcClassificationReference` also exist; IFC4 reshaped (unverified) |
| `IfcSurfaceStyle`, `IfcStyledItem`, `IfcPresentationLayerAssignment` | colours/materials appearance, CAD layers | |
| `IfcUnitAssignment`, `IfcSIUnit`, `IfcConversionBasedUnit` | units of the project | |
| `IfcMapConversion`, `IfcProjectedCRS` (IFC4) | georeferencing | |
| `IfcShapeRepresentation`, `IfcExtrudedAreaSolid`, `IfcFacetedBrep`, `IfcTriangulatedFaceSet` (IFC4), `IfcMappedItem`/`IfcRepresentationMap`, `IfcLocalPlacement`, `IfcAxis2Placement3D` | geometry vocabulary | extruded + mapped = lightweight; tessellation = what Revit/Archicad use for freeform |
| `IfcPerson`, `IfcOrganization`, `IfcApplication`, `IfcOwnerHistory` | authorship; `OwnerHistory` mandatory in 2x3, optional in IFC4 (unverified) | |

### 3.9 Process, cost and control

| Entity | Plain meaning | Notes |
|---|---|---|
| `IfcTask` | schedule activity (4D) | tied to products with `IfcRelAssignsToProduct`, ordered with `IfcRelSequence`, times in `IfcTaskTime` |
| `IfcProcedure`, `IfcEvent` | non-task processes; milestones/events | |
| `IfcWorkPlan`, `IfcWorkSchedule`, `IfcWorkCalendar` | schedule containers; PT of schedule `ACTUAL, BASELINE, PLANNED` (unverified) | `IfcWorkSchedule.Identifier` became `Identification` in ifcXML only [22] |
| `IfcCostSchedule`, `IfcCostItem`, `IfcCostValue` | cost plan, line item, amount (5D) | `IfcCostItem` links to products via `IfcRelAssignsToControl`; sums via `IfcRelAggregates` (unverified) |
| `IfcLaborResource`, `IfcConstructionEquipmentResource`, `IfcSubContractResource` | resources | |
| `IfcPermit`, `IfcActionRequest` | FM/control objects | (unverified) |
| `IfcActor`, `IfcOccupant`, `IfcActorRole` | people/organisation roles | |
| `IfcDocumentInformation`, `IfcDocumentReference`, `IfcRelAssociatesDocument` | attached docs | |
| `IfcApproval`, `IfcConstraint`, `IfcMetric` | approvals and constraints | |

---

## 4. How Revit and Archicad pick the class (what a tester must know)

**Revit** applies a decision order (community write-up, simplified) [14]:
1. Hard-coded category rules (e.g. Ceilings -> `IfcCovering`, Duct Insulation -> `IfcCovering.INSULATION`, Railings -> `IfcRailing`, Ramps -> `IfcRamp`, Rebar -> `IfcReinforcingBar`, Wall Sweep -> `IfcBuildingElementProxy`).
2. Family-level / instance-level shared parameters: `IfcExportAs` (class, or class.PT such as `IfcWall.PLUMBINGWALL`), `IfcExportType` (PT only; recommended replacement for deprecated `IfcType`; it wins over the dot notation).
3. Type-level `IfcExportAs[Type]`, `IfcType[Type]`, `IfcExportType[Type]`.
4. The category-to-class mapping table: File > Export > Options > IFC Options (Revit exposes category/subcategory -> IFC class and IFC PT; entering `NotExported` suppresses a category) [14][27].
5. Blank PT becomes `UNDEFINED`; structural categories fall back to fixed classes: beam -> `IfcBeam`, brace -> `IfcMember`, footing -> `IfcFooting`, column -> `IfcColumn` [14].

Known behaviours reported by users:
- Generic Models and invalid class names fall to `IfcBuildingElementProxy` [19][20].
- "Typos fail silently": no dropdown validation on `IfcExportAs`. An override on an instance auto-creates a type named `<Class>Type`, and the type class cannot be controlled [14].
- 2x3 Coordination View 2.0 exports walls as `IfcWallStandardCase`; IFC4 Reference View as `IfcWall`; `IfcExportAs` does not always override system families (reported) [8a].
- Autodesk's own "Supported IFC Classes" page for the mapping file lists 30 classes in IFC2x3 vocabulary (`IfcDoorStyle`, `IfcWindowStyle`, `IfcColumnType`, `IfcFurnitureType`, `IfcRailing`, `IfcSlab`, `IfcCovering`, `IfcCurtainWall`, `IfcFooting`, `IfcPile`, `IfcRamp`, `IfcRoof`, `IfcStair`, `IfcWall`, `IfcOpeningElement`, `IfcBuildingStorey`, `IfcSite`, `IfcAnnotation` ...). It is an LT help page; the full list differs by release [14b].
- The mapping table is stored in `exportlayers-ifc-IAI.txt` in ProgramData; deleting it and re-clicking "Standard" regenerates defaults [27][19].

**Archicad** [9][28]: each tool has a default IFC type; GDL objects use their subtype. You can map by Element Type (automatic) or by Classification (manual) in the translator ("Type Mapping for IFC Export"), with `IFC Type`, `IFC Type Product` and `Predefined Type`; choosing `USERDEFINED` lets you type a custom value. PTs not in the target schema (e.g. `MOLDING` in 2x3) are greyed out and not exported [28]. Older guide: Archicad Roof -> single `IfcSlab` with PT `ROOF`, Zone -> `IfcSpace`, and the IFC4 option "split complex elements into Building Element Parts" for Reference View compliance [9][9b]. Archicad 29 discussions about IFC4.3 implementation exist on the Graphisoft community [29].

**Bonsai/IfcOpenShell side:** OSArch recommends the Bonsai IFC class search to find class names [14].

---

## 5. Renamed, deprecated, replaced

| Change | Where | Source |
|---|---|---|
| `IfcBuildingElement` -> `IfcBuiltElement` (also `...Type`) | IFC4.3.0.0 | [1][5] |
| `IfcBuildingSystem` -> `IfcBuiltSystem` | 4.3 | [1] |
| `IfcElectricDistributionBoard` -> `IfcDistributionBoard` | 4.3 | [1] |
| `IfcBridgePart` -> covered by `IfcFacilityPart` (EXPRESS SELECT) | 4.3 notes (`IfcFacilityPart` itself dates from IFC4.2) | [1] |
| `IfcVibrationIsolator`, `IfcVibrationDamper` -> within `IfcImpactProtectionDevice` | 4.3 | [1] |
| `IfcCivilElement`, `IfcGeographicElementTypeEnum`, `IfcRelServicesBuildings` deprecated | 4.3 | [1] |
| `IfcWallStandardCase`, `IfcWallElementedCase` deprecated (StandardCase: per search summaries, exact version unverified, see 3.1); enum `STANDARD`, `POLYGONAL` deprecated (use `IfcWall` + PT) | IFC4 ADD2 TC1 and onward (ElementedCase: confirmed for the ADD2 TC1 docs; enums: marked "deprecated in IFC4") | [2][2b][7][11] |
| `IfcRelServicesBuildings` deprecated, use `IfcRelReferencedInSpatialStructure` | IFC4.3.0.0 ("IFC4.3.0.0 DEPRECATION", QA-verified) | [1] |
| `IfcDoorStyle`/`IfcWindowStyle` -> `IfcDoorType`/`IfcWindowType` | 2x3 -> IFC4 | (unverified) general schema knowledge; Revit's 2x3-style list still names the Styles [14b] |
| `IfcMaterialList` (2x3) vs `IfcMaterialConstituentSet` (IFC4) | 2x3 -> IFC4 | [22] |
| `IfcDateAndTime` (2x3) -> `IfcDateTime` (IFC4); `NumberOfRiser` -> `NumberOfRisers` on `IfcStairFlight` | 2x3 -> IFC4 | [22] |
| `IfcSpatialStructureElement` as top spatial class (2x3) -> `IfcSpatialElement` with `IfcSpatialStructureElement` below it (IFC4) | 2x3 -> IFC4 | (unverified from 4.3 doc list [6]) |
| `CAISSON_FOUNDATION` footing PT deprecated | IFC4x2 | [18] |
| `IfcBuildingElementProxy` discouraged as spatial placeholder | 4.3.0.0 | [5b] |

Where changes are documented: IFC4 Annex F change log, "IFC2x3 to IFC4 mappings" forum thread (an open discussion, not an authoritative table), IFC4.3 release notes [22][1].

---

## Typical questions people ask about this

Real threads (title seen in search results; threads not all opened; posters not named):
1. "Export IFC - IfcWall and IfcWallStandardCase" - why are some walls StandardCase and others plain IfcWall? (Autodesk Community) https://forums.autodesk.com/t5/revit-architecture-forum/export-ifc-ifcwall-and-ifcwallstandardcase/td-p/10700508
2. "Changing IFC class for system families" - how to make a Revit wall type export as another class. https://forums.autodesk.com/t5/revit-architecture-forum/changing-ifc-class-for-system-families/td-p/9338744
3. "Export IfcExportAs and change of ifc-classification does not work - why?" https://forums.autodesk.com/t5/revit-architecture-forum/export-ifcexportas-and-change-of-ifc-clasification-does-not-work/td-p/10035969
4. "PR: Floors not exporting" - floors/roofs landing in proxies via the open source exporter. https://github.com/Autodesk/revit-ifc/issues/759
5. "Objects missing when exported to IFC" - Generic Models mapped to proxy, escalators missing. https://forums.autodesk.com/t5/revit-architecture-forum/objects-missing-when-exported-to-ifc/td-p/7308264
6. "IfcWallElementedCase (Deprecated?)" - why deprecated, use `IfcWall` + `ELEMENTEDWALL`? https://forums.buildingsmart.org/t/ifcwallelementedcase-deprecated/2933
7. "List of changes between IFC versions?" - where is the IFC2x3 -> IFC4 -> IFC4.3 change list? https://forums.buildingsmart.org/t/list-of-changes-between-ifc-versions/4604
8. "IFC 4.3 schema implementation in Archicad 29" https://community.graphisoft.com/t5/Project-data-BIM/IFC-4-3-schema-implementation-in-Archicad-29/m-p/680785
9. "Classification of composite walls" (Graphisoft Community) https://community.graphisoft.com/t5/Project-data-BIM/Classification-of-composite-walls/td-p/276001
10. "Doors are being transformed into Objects in IFC" (Graphisoft Community) https://community.graphisoft.com/t5/Documentation/Doors-are-beign-transformed-into-Objects-in-IFC/td-p/330050
11. "Revit: Wall type is missing after IFC import" https://forums.autodesk.com/t5/revit-architecture-forum/revit-wall-type-is-missing-after-ifc-import/td-p/8443090

Illustrative (invented) requests for an MCP tester, with what a good answer should hit:
12. (illustrative) "List all `IfcBuildingElementProxy` in the model and tell me which Revit categories they came from." -> count + group by `ObjectType`/Revit category property; mention `IfcExportAs`.
13. (illustrative) "How many doors on level 3 and what is their fire rating?" -> `IfcDoor` + container `IfcBuildingStorey`; `Pset_DoorCommon.FireRating`.
14. (illustrative) "Is this wall `IfcWall` or `IfcWallStandardCase`, and does it matter?" -> IFC version; deprecation; material layer set usage.
15. (illustrative) "Change all generic-model pumps to `IfcPump`." -> in IFC: change class (IfcOpenShell `root.reassign_class`); in Revit: set `IfcExportAs` and re-export.
16. (illustrative) "Which entities does a stair consist of?" -> `IfcStair` aggregating `IfcStairFlight`, `IfcSlab` landing, `IfcRailing`.
17. (illustrative) "Are `IfcSpace` and `IfcZone` the same?" -> no: space is spatial; zone is a group.
18. (illustrative) "My IFC4.3 model has `IfcBuiltElement`; my old script filters `IfcBuildingElement`, why empty?" -> rename; `by_type` with subtype inheritance in the IFC4X3 schema.
19. (illustrative) "Why does `IfcWall` have no `LayerSetUsage` in the IFC4 export?" -> material association rules.
20. (illustrative) "What is `PredefinedType` and where do I set it in Revit?" -> `IfcExportType`/IFC Options mapping table.
21. (illustrative) "How do I get the road centreline from an IFC4.3 file?" -> `IfcAlignment` + `IfcAlignmentHorizontal` segments or its `Axis` representation.
22. (illustrative) "Do rooms export as `IfcSpace`? What about MEP spaces?" -> yes, with bounding settings; PT `INTERNAL/EXTERNAL`.
23. (illustrative) "Which entity holds the tasks of my 4D schedule?" -> `IfcTask` under `IfcWorkSchedule`, linked with `IfcRelAssignsToProduct`.
24. (illustrative) "Is `IfcBuildingElementProxy` deprecated in 4.3?" -> not deprecated on the entity page, discouraged for placeholders and arbitrary elements [5b]; the release notes list it among changed items [1].

---

## Common pitfalls and misconceptions

- **"IfcWallStandardCase is the right wall class."** It is reported as deprecated (IFC4 ADD2 TC1 / IFC4.3 docs per search summaries; exact version unverified, see 3.1); modern exporters write `IfcWall`; consumers must still read StandardCase [2][2b]. Some users depend on StandardCase because `IfcMaterialLayerSetUsage` handling [10].
- **"A proxy means the exporter failed."** Often just means the Revit category (Generic Models) or an invalid override was used [19][20]. Fix is an `IfcExportAs` value or mapping table change.
- **`IfcExportAs` typos** silently produce proxies [14].
- **Type vs. occurrence confusion**: `IfcDoor` (instance in the model) vs. `IfcDoorType` (family type); PT often lives on the type [5b].
- **Roof**: in older Archicad translators a roof is `IfcSlab.ROOF`, not `IfcRoof` [9].
- **`IfcSpace` vs `IfcZone` vs `IfcSpatialZone`** are different concepts.
- **`IfcSite` as terrain**: IFC2x3 had no `IfcGeographicElement`; terrain sometimes exported as `IfcSite` geometry or proxy.
- **IFC2x3 vs IFC4 classes**: many MEP occurrence classes only exist in IFC4+ (unverified); downgrading may fall back to generic `IfcFlowSegment`.
- **IFC4.3 names in IFC4 files**: `IfcBuiltElement` does not exist in the `IFC4` schema. Use the file header schema (`IFC4X3_ADD2`) to decide [4].
- **Deprecation lists differ by source**: the release-notes page, entity pages and forums disagree on some entities (`IfcBuildingElementProxy`, `IfcWallStandardCase`); treat "deprecated" as "do not newly produce, still read".
- **`IfcExportAs` does not touch hard-coded categories** (the OSArch decision list puts these first) [14].
- **Fabricated entity names from LLMs**: a model may answer `IfcRoomElement`, `IfcFloor`, `IfcPlumbingFixture` - none exist. Judge answers by actual schema names (`IfcSpace`, `IfcSlab`, `IfcSanitaryTerminal`).

---

## Gaps

- The official IFC4.3 HTML documentation (standards.buildingsmart.org, ifc43-docs mirror) returned HTTP 403/redirects to a 403 site for direct fetches; entity details were taken from the buildingSMART GitHub IFC4.3.x-development markdown (development branch, may differ from final ADD2 text) and from search summaries of the official pages.
- Enumerations flagged "(unverified)" (pipe segment/fitting, furniture, bearing, transport element, electrical and other MEP lists) come from schema knowledge, not re-fetched pages. In QA (2026-11-06) the following were re-read on the IFC4.3.x-development markdown and corrected or confirmed: Wall, Door, Window, Beam, Column, Stair, Ramp, Railing, Plate, Pile, Shading device, Building element part, Reinforcing bar, Duct fitting, Space. Paths for IfcPipeSegmentTypeEnum and IfcTransportElementTypeEnum returned 404 in the guessed locations.
- `IfcWallStandardCase`: the exact version that deprecated it could not be confirmed (see 3.1 row). The official IFC4.3 HTML (standards.buildingsmart.org) returned HTTP 403 again in QA.
- Revit MEP default category mappings and the current (2025/2026) Revit IFC4 mapping table were not found on a primary page.
- Several forum threads were seen as search results only (titles/URLs), not opened.
- No suspicious or pirated sites were encountered or linked. The web search quota ran out partway through, so IFC2x3->IFC4 MEP-class specifics were not searched.

---

## Sources

1. buildingSMART IFC Release Notes (GitHub mirror): https://github.com/buildingSMART/technical.buildingsmart.org/blob/main/IFC-Release-Notes.md
2. IFC4.3 docs, IfcWallStandardCase (deprecation seen via search summary): https://ifc43-docs.standards.buildingsmart.org/IFC/RELEASE/IFC4x3/HTML/lexical/IfcWallStandardCase.htm
2b. Technical mirror of IFC4 ADD2 pages (IfcWallStandardCase, wall enums): https://technical.buildingsmart.org/projects/2024tunnel/schema/ifcsharedbldgelements/lexical/ifcwallstandardcase.htm
3. ISO 16739-1:2024 record and buildingSMART news: https://www.iso.org/standard/84123.html ; https://www.buildingsmart.org/ifc-4-3-formally-approved-and-published-as-an-iso-standard/ ; https://www.buildingsmart.org/standards/bsi-standards/industry-foundation-classes/
4. IFC 4.3.2 (IFC4X3_ADD2) docs page: https://ifc43-docs.standards.buildingsmart.org/IFC/RELEASE/IFC4x3/HTML/lexical/IfcBuildingElementPart.htm
5. IfcBuiltElement (IFC4.3.x-development): https://github.com/buildingSMART/IFC4.3.x-development/blob/master/docs/schemas/core/IfcProductExtension/Entities/IfcBuiltElement.md
5b. IfcBuildingElementProxy: https://github.com/buildingSMART/IFC4.3.x-development/blob/master/docs/schemas/shared/IfcSharedBldgElements/Entities/IfcBuildingElementProxy.md
6. IfcFacility: https://github.com/buildingSMART/IFC4.3.x-development/blob/master/docs/schemas/core/IfcProductExtension/Entities/IfcFacility.md
6b. Core entity list: https://github.com/buildingSMART/IFC4.3.x-development/tree/master/docs/schemas/core/IfcProductExtension/Entities
6c. IfcAlignment: https://github.com/buildingSMART/IFC4.3.x-development/blob/master/docs/schemas/core/IfcProductExtension/Entities/IfcAlignment.md
6d. (same listing as 6b: IfcLinearPositioningElement, IfcReferent, IfcPositioningElement)
7. IfcWallTypeEnum: https://github.com/buildingSMART/IFC4.3.x-development/blob/master/docs/schemas/shared/IfcSharedBldgElements/Types/IfcWallTypeEnum.md
8a. https://forums.autodesk.com/t5/revit-architecture-forum/export-ifc-ifcwall-and-ifcwallstandardcase/td-p/10700508
9. Graphisoft IFC Reference Guide for ARCHICAD 20: https://gsdownloads.graphisoft.com/cdn/ftp/techsupport/documentation/IFC/IFC%20Reference%20Guide%20for%20ARCHICAD%2020.pdf
9b. Graphisoft geometry conversion for IFC export: https://help.graphisoft.com/AC/24/INT/_AC24_Help/115_IFC/115_IFC-37.htm
10. buildingSMART Forum, comment on IFC4.3 review category: https://forums.buildingsmart.org/t/about-the-ifc4-3-building-room-building-domain-review-category/3933
11. buildingSMART Forum, IfcWallElementedCase: https://forums.buildingsmart.org/t/ifcwallelementedcase-deprecated/2933
12. IfcSlabTypeEnum: https://github.com/buildingSMART/IFC4.3.x-development/blob/master/docs/schemas/shared/IfcSharedBldgElements/Types/IfcSlabTypeEnum.md
13. IfcRoofTypeEnum: https://github.com/buildingSMART/IFC4.3.x-development/blob/master/docs/schemas/shared/IfcSharedBldgElements/Types/IfcRoofTypeEnum.md
14. OSArch wiki, Revit and IFC classes (community): https://wiki.osarch.org/revit-setup-for-openbim-revit-and-ifc-classes/
14b. Autodesk, Supported IFC Classes (Revit LT 2025 help): https://help.autodesk.com/cloudhelp/2025/ENU/RevitLT-DocumentPresent/files/GUID-EE6C0CF8-7671-4DCC-B0C7-EEA7513C90A9.htm
15. IfcCoveringTypeEnum: https://github.com/buildingSMART/IFC4.3.x-development/blob/master/docs/schemas/shared/IfcSharedBldgElements/Types/IfcCoveringTypeEnum.md
16. IfcDoorTypeEnum: https://github.com/buildingSMART/IFC4.3.x-development/blob/master/docs/schemas/shared/IfcSharedBldgElements/Types/IfcDoorTypeEnum.md
17. IfcMemberTypeEnum: https://github.com/buildingSMART/IFC4.3.x-development/blob/master/docs/schemas/shared/IfcSharedBldgElements/Types/IfcMemberTypeEnum.md
18. IfcFootingTypeEnum and structural elements entity list: https://github.com/buildingSMART/IFC4.3.x-development/blob/master/docs/schemas/domain/IfcStructuralElementsDomain/Types/IfcFootingTypeEnum.md ; https://github.com/buildingSMART/IFC4.3.x-development/tree/master/docs/schemas/domain/IfcStructuralElementsDomain/Entities
18b. (same listing, IfcVoidingFeature, IfcSurfaceFeature)
18c. (core listing 6b: IfcRelSpaceBoundary1stLevel/2ndLevel)
19. Autodesk revit-ifc issue 759: https://github.com/Autodesk/revit-ifc/issues/759
20. Autodesk Community, objects missing when exported to IFC: https://forums.autodesk.com/t5/revit-architecture-forum/objects-missing-when-exported-to-ifc/td-p/7308264
21. IfcSpaceTypeEnum: https://github.com/buildingSMART/IFC4.3.x-development/blob/master/docs/schemas/core/IfcProductExtension/Types/IfcSpaceTypeEnum.md
22. buildingSMART Forum, IFC2x3 to IFC4 mappings: https://forums.buildingsmart.org/t/ifc2x3-to-ifc4-mappings/3093 ; List of changes: https://forums.buildingsmart.org/t/list-of-changes-between-ifc-versions/4604
23. IfcDuctSegmentTypeEnum: https://github.com/buildingSMART/IFC4.3.x-development/blob/master/docs/schemas/domain/IfcHvacDomain/Types/IfcDuctSegmentTypeEnum.md
24. IfcCourseTypeEnum: https://github.com/buildingSMART/IFC4.3.x-development/blob/master/docs/schemas/shared/IfcSharedInfrastructureElements/Types/IfcCourseTypeEnum.md
25. Shared building elements entity list: https://github.com/buildingSMART/IFC4.3.x-development/tree/master/docs/schemas/shared/IfcSharedBldgElements/Entities
26. IfcWallStandardCase (dev docs, conditions of use): https://github.com/buildingSMART/IFC4.3.x-development/blob/master/docs/schemas/shared/IfcSharedBldgElements/Entities/IfcWallStandardCase.md
27. BIM Corner, IFC export from Revit (community): https://bimcorner.com/exporting-ifc-from-revit-part-1-mapping/
28. Graphisoft, Type Mapping for IFC Export: https://help.graphisoft.com/AC/26/INT/_AC26_Help/121_IFC/121_IFC-35.htm
29. Graphisoft Community, IFC 4.3 in Archicad 29: https://community.graphisoft.com/t5/Project-data-BIM/IFC-4-3-schema-implementation-in-Archicad-29/m-p/680785
30. IFC4.3.x-development enumeration pages re-read in QA (raw GitHub markdown, e.g. https://github.com/buildingSMART/IFC4.3.x-development/blob/master/docs/schemas/shared/IfcSharedBldgElements/Types/IfcStairTypeEnum.md ; the same folder holds IfcBeamTypeEnum, IfcColumnTypeEnum, IfcRampTypeEnum, IfcRailingTypeEnum, IfcPlateTypeEnum, IfcShadingDeviceTypeEnum; IfcPileTypeEnum and IfcReinforcingBarTypeEnum are in docs/schemas/domain/IfcStructuralElementsDomain/Types; IfcBuildingElementPartTypeEnum in shared/IfcSharedComponentElements/Types; IfcDuctFittingTypeEnum in domain/IfcHvacDomain/Types)
