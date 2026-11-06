# Domain overviews: MEP, structural, infrastructure (IFC 4.3), 4D/5D, FM/COBie

## In plain words

IFC is not one "building model" but a family of domain slices that share one core. The same file can hold ducts and pipes (MEP), beams and rebar (structural), a road centreline with stations (infrastructure, new in IFC 4.3), a construction schedule (4D), a cost plan (5D) and the handover data a facility manager needs (FM, COBie). Each domain uses its own entities and its own way of expressing relationships. That is why a model can look perfect in a viewer and still return nothing when you ask "which pipes belong to system X?" or "what is the cost of this wall?". For a tester, the practical rule is: for every domain, know (a) which entities carry the data, (b) which relationship entity connects them, and (c) which exporters (Revit, Tekla, Archicad, IfcOpenShell/Bonsai) actually write that data.

Last researched: 2026-11-06

> Research limits (read first): the official buildingSMART specification hosts (standards.buildingsmart.org, ifc43-docs.standards.buildingsmart.org, www.buildingsmart.org) returned HTTP 403 to the page fetcher, and the web-search quota ran out partway through. Statements about the specification therefore rest on search-result excerpts of official pages, on buildingSMART forum threads, NIBS pages, the OSArch wiki and vendor help, plus my own background knowledge. Items from background knowledge that I could not re-check are marked "(unverified)". Searches in German, Chinese and Japanese for national infrastructure topics could not be run (see Gaps).

---

## 1. Shared concepts you need in every domain

| Concept | What it means | IFC mechanism |
|---|---|---|
| Type vs occurrence | A product type (catalogue item) and its placed instances | `IfcXxxType` + `IfcRelDefinesByType`; occurrence `IfcXxx` |
| Spatial structure | Project > Site > Building > Storey > Space; in 4.3 also Facility / FacilityPart | `IfcRelAggregates`, `IfcRelContainedInSpatialStructure` |
| Grouping (systems, zones) | Non-spatial or functional groups | `IfcGroup` subtypes (`IfcSystem`, `IfcZone`) + `IfcRelAssignsToGroup` |
| Properties | Named values in property sets, quantities in `Qto_*` | `IfcPropertySet` / `IfcElementQuantity` via `IfcRelDefinesByProperties` |
| Process / control | Tasks, schedules, cost items | `IfcProcess`, `IfcControl` subtypes + `IfcRelAssignsTo*` |

Versions in the wild: IFC2x3 (still very common in Russia/CIS and in many national requirements), IFC4 (Reference View / Design Transfer View in Revit 2022+ (unverified exact start)), IFC 4.3 (ISO 16739-1:2024, see section 4). IFC 4.3 was approved by ISO in January 2024 [9][11] and published as ISO 16739-1:2024 [10]; the buildingSMART development repository calls the formal release "4.3.2.0" and says it is CC BY-ND licensed [14]. Nordic BIM notes that, at the time of its page (undated), no software was certified for IFC 4.3 and that building deliverables should still be specified as IFC 4 or 2x3 [13]. Certification status changes; check the buildingSMART software list before asserting it.

QA 2026-11-06 notes on this paragraph: (a) the Construction Management article is dated 5 Jan 2024 and says IFC 4.3 "received 100% approval" and ISO would publish it as the latest version of ISO 16739; it does not itself mention "4.3.2.0" or "ISO 16739-1:2024" (those come from the buildingSMART repository README and Wikipedia). (b) The GitHub README confirms: the formal 4.3.2.0 release is ISO-approved, published on buildingSMART's standards site and the ISO website, static releases are CC BY-ND 4.0; the `ifc4.3-main` branch is the development version with minor post-ISO fixes. (c) The Nordic BIM page [13] shows a date of "May 11, 2026" and still says that no software is currently certified for IFC 4.3 and advises specifying IFC 4 or IFC 2x3 for buildings; the page does not say when that statement was written. Vendors' own pages differ (Tekla's help lists certified MVDs only for IFC 2x3 and IFC 4; Wikipedia says BricsCAD BIM is "certified for IFC 4.3 import and export" citing a Bricsys page) - treat any "certified for 4.3" claim as vendor-stated until checked on buildingSMART's list.

---

## 2. MEP (HVAC, plumbing, electrical, fire protection)

### 2.1 Entity families

All MEP content sits under `IfcDistributionElement`. The practical split (names from the IFC4/4.3 schema; the family listing is from my background knowledge unless cited):

| Family | Purpose | Typical entities |
|---|---|---|
| `IfcFlowSegment` | Straight run of duct/pipe/cable ("a segment of a flow distribution system" [18]) | `IfcDuctSegment`, `IfcPipeSegment`, `IfcCableSegment`, `IfcCableCarrierSegment` |
| `IfcFlowFitting` | Changes direction/size/branches | `IfcDuctFitting`, `IfcPipeFitting`, `IfcCableFitting`, `IfcCableCarrierFitting`, `IfcJunctionBox` |
| `IfcFlowTerminal` | End points of a system | `IfcAirTerminal`, `IfcSanitaryTerminal`, `IfcLightFixture`/`IfcLamp`, `IfcOutlet`, `IfcFireSuppressionTerminal`, `IfcSpaceHeater`, `IfcWasteTerminal` |
| `IfcFlowController` | Regulates flow | `IfcValve`, `IfcDamper`, `IfcSwitchingDevice`, `IfcAirTerminalBox`, `IfcFlowMeter`, `IfcProtectiveDevice` |
| `IfcFlowMovingDevice` | Moves the medium | `IfcPump`, `IfcFan`, `IfcCompressor` |
| `IfcFlowStorageDevice` | Stores medium/energy | `IfcTank`, `IfcElectricFlowStorageDevice` |
| `IfcFlowTreatmentDevice` | Cleans/conditions | `IfcFilter`, `IfcInterceptor` |
| `IfcEnergyConversionDevice` | Converts energy | `IfcBoiler`, `IfcChiller`, `IfcCoil`, `IfcHeatExchanger`, `IfcUnitaryEquipment` |
| Distribution boards | In an IfcOpenShell thread an author models an `IfcDistributionBoard` together with `IfcLightFixture`, `IfcSwitchingDevice`, `IfcOutlet` [25]; in IFC4 the board entity was named `IfcElectricDistributionBoard`; QA-verified: that entity is marked **DEPRECATED** in the IFC 4.3 line ("may be imported, but shall not be exported by applications"; status changed to Deprecated for IFC4x3_RC1), a subtype of `IfcFlowController`; the replacement used in the IfcOpenShell thread is `IfcDistributionBoard` | |
| `IfcDistributionControlElement` | Sensors, actuators, controllers | `IfcSensor`, `IfcActuator`, `IfcController` |

The `PredefinedType` attribute (and `ObjectType` when it is `USERDEFINED`) narrows the meaning, e.g. a pipe segment can be `RIGIDSEGMENT` or `FLEXIBLESEGMENT` (unverified exact enum list). Russian-language practice: ОВиК = HVAC, ВК = water supply/sewage, ЭОМ = electrical; these map to different `IfcDistributionSystem.PredefinedType` values (e.g. `VENTILATION`, `DOMESTICCOLDWATER`, `ELECTRICAL`) (unverified enum names).

### 2.2 Ports and connectivity (the part that breaks most often)

- A port (`IfcDistributionPort`) is "a product's inlet or outlet for a substance"; its `FlowDirection` is SINK (inlet), SOURCE (outlet), SOURCEANDSINK (both), or NOTDEFINED [19] (QA fix: the enumeration value is spelled `SOURCEANDSINK`, as verified in `IfcFlowDirectionEnum`; the first pass wrote "SINKANDSOURCE", which is the wording used in the entity description text, not the enum literal). Two ports connect only if they share the same system type and have opposite directions (one SOURCE, one SINK) [19] (QA-verified).
- Port-to-port connection is `IfcRelConnectsPorts`; the MVD "Port Connectivity" template for the IFC4 Add2 Reference View describes this for ducts, pipes and air terminals [20].
- Port-to-element: in IFC2x3 `IfcRelConnectsPortToElement`; in IFC4 fixed ports are attached with `IfcRelNests` (works for types and occurrences), while `IfcRelConnectsPortToElement` is reserved for "dynamic" ports and applies only to occurrences [19][21]. Per a forum answer, Revit's IFC4 exporter writes `IfcRelNests` and cannot define dynamic connections, whereas for IFC2x3 it writes `IfcRelConnectsPortToElement` [21]. (Forum statement about exporter source code; verify per Revit version.)
- Flow direction logic in Bonsai: setting one port to source/sink sets the connected port to the opposite; direction describes how an element is used, not a physical property, and tees/wyes/manifolds have more than two ports [23].
- Real-world data point: a Revit 2025 IFC4 export contained about 1,474 `IfcDistributionPort` and 691 `IfcRelConnectsPorts`, i.e. connectivity was exported; the loss happened later, when a web converter dropped `IfcRelConnectsPorts` [24]. Lesson: when "connectivity is missing", check the IFC text first, then the importer.

### 2.3 Systems

- A system is an `IfcSystem` (for MEP, `IfcDistributionSystem`) that gathers members through `IfcRelAssignsToGroup`. Any product can be a member, including pipe segments [22].
- Known gap: a user reported pipe `IfcSystem` information present in Revit IFC2x3 exports but missing in IFC4 exports, with no confirmed fix in the thread [22]. Older Revit MEP versions exported systems inconsistently [30-forum, see Sources].
- Known gap: an IfcOpenShell user built an electrical model (board, switches, outlets, ports, electrical system) but Revit did not recognise circuits on import; maintainers recalled that Revit did not export circuits to IFC, so it may not import them either [25].
- Round-trip: Revit does not turn IFC pipes into native MEP Revit elements by default; a commercial plug-in (CYPE) advertises generating native piping/HVAC elements from IFC [see Sources, CYPE item].

### 2.4 Sizing and performance properties (where the numbers live)

Values live in three places, and a good test checks all of them (names below are from background knowledge, unverified):

1. Geometry: profile of the swept solid, e.g. `IfcRectangleProfileDef` (XDim/YDim) for rectangular ducts, `IfcCircleProfileDef` or hollow circle profiles for round ducts/pipes.
2. Quantities: `Qto_DuctSegmentBaseQuantities`, `Qto_PipeSegmentBaseQuantities` (Length, cross-section areas, surface areas). Revit writes these only if "Export base quantities" is ticked in the IFC export setup.
3. Property sets: `Pset_DuctSegmentTypeCommon`, `Pset_PipeSegmentTypeCommon`, port sets such as `Pset_DistributionPortTypeDuct` / `...Pipe` (ConnectionType, nominal diameter or width/height); equipment sets such as `Pset_FanTypeCommon`, `Pset_PumpTypeCommon`. Revit adds its own "Pset_Revit_*"/ custom sets when "Export Revit property sets" is on. Flow rate, pressure drop, velocity, insulation thickness are typically Revit parameters exported as custom properties, not guaranteed standard Psets.

### 2.5 Typical MEP checks an MCP server is asked to do

- Count and list `IfcPipeSegment` / `IfcDuctSegment` per system and per storey.
- Find unconnected ports (a port with no `IfcRelConnectsPorts`).
- Trace a path from a source port to terminals through connected ports.
- Sum duct length per system; report diameters present.
- Check that every distribution element belongs to some `IfcDistributionSystem`.
- Rename or reassign a system; add a missing `Pset` value (write operations must survive save + reload).

---

## 3. Structural: physical vs analytical, loads, rebar, precast, steel

### 3.1 Two different models

| | Physical (structural design / BIM) model | Analytical (structural analysis) model |
|---|---|---|
| Content | `IfcBeam`, `IfcColumn`, `IfcSlab`, `IfcWall`, `IfcFooting`, `IfcPile`, `IfcMember`, `IfcPlate` with solid geometry, materials, profiles | `IfcStructuralAnalysisModel` containing `IfcStructuralCurveMember` (1D), `IfcStructuralSurfaceMember` (2D), connections, supports, loads |
| Purpose | Coordination, drawings, quantities, fabrication | Finite-element / frame analysis |
| Geometry | 3D solids | Centrelines, mid-surfaces, points |
| Export from authoring tools | Everyday and reliable | Patchy |

The IFC 4.3 structural analysis domain lists `IfcStructuralAnalysisModel`, `IfcStructuralCurveMember`, `IfcStructuralCurveMemberVarying` and `IfcStructuralLoadCase` among its entities [26-schema, see Sources]. Typical supporting entities (unverified list): `IfcStructuralPointConnection` (nodes, supports), `IfcStructuralCurveConnection`, `IfcStructuralLoadGroup`, `IfcStructuralLoadCase`, `IfcStructuralResultGroup`, `IfcStructuralPointAction`/`...LinearAction`/`...PlanarAction` for loads. The analytical item links to the physical element with `IfcRelAssignsToProduct` (QA-verified: the `IfcStructuralItem` documentation states that building elements and their structural idealisations "can be expressed by instances of IfcRelAssignsToProduct"; `IfcRelConnectsStructuralActivity` is a different thing - it attaches an action/reaction to a member, connection or element).

State of tool support (all from forum/vendor pages, treat as snapshots):
- Revit's built-in IFC exporter: forum users report that analytical elements are not exported, or produce a near-empty file; one 2024-era thread repeats this; the Geometry Gym RevitIFC plug-in is cited as offering a "Structural Analysis" export option [26].
- Archicad: experimental "IFC Structural Analysis Model Import/Export" using the "Structural Analytical View" MVD (QA-verified on the Archicad 27 help: must be switched on under Options > Work Environment > More Options > Experimental Features; Graphisoft says it may change or be removed); import for IFC2x3 and IFC4, export only IFC2x3; exports 1D and 2D members with geometry, profiles and materials; the page does not describe supports or loads; imported members become columns/beams by orientation [27].
- Modelling rigid links: a buildingSMART forum thread discusses representing them as curve members with a rigid-link material and using `IfcStructuralCurveMemberVarying` to distinguish them [28].

### 3.2 Reinforcement

- Entities: `IfcReinforcingBar` (with `IfcReinforcingBarType`), `IfcReinforcingMesh`, `IfcTendon` and `IfcTendonAnchor`, grouped as `IfcReinforcingElement` (unverified exact hierarchy). Typical attributes: nominal diameter, steel grade, bar length, surface (`PLAIN`/`TEXTURED`), role (`MAIN`, `SHEAR`, `LIGATURE`...) (unverified).
- Rebar is hosted in a concrete element, usually by an assembly or by `IfcRelAggregates` / `IfcRelNests`; the geometry is a swept disk solid along a bar centreline, so the file size explodes with detailed rebar.
- Tekla maps reinforcement to `IfcReinforcingBar`; bars, wires, strands, meshes and tendons fall under the wider reinforcing-element category in its table [29]. Tekla supports IFC2x3, IFC4 and IFC 4.3 export, certified views are IFC2x3 and IFC4 [29-2026]. A precast view exists for IFC4 only (walls and slabs including reinforcement and embeds) [29].
- Pitfall: Revit-modelled rebar is exported to IFC only if the exporter option for rebar is enabled and the Revit category is mapped (unverified option name).

### 3.3 Precast and assemblies

- A cast unit is an `IfcElementAssembly` (Tekla: an assembly or cast unit maps to it; a sub-part maps to `IfcDiscreteAccessory`) [29]. Pour units also map to `IfcElementAssembly` in the 2021 table [29].
- Embeds, lifting anchors, dowels: `IfcDiscreteAccessory`, `IfcMechanicalFastener`, `IfcFastener` (the Graphisoft help lists tendon and mechanical fastener as mapping targets [30]).
- Secondary steel parts: by default not exported as `IfcDiscreteAccessory` in Tekla's IFC2x3 export unless the advanced option `XS_IFC2X3_EXPORT_SECONDARY_AS_DISCRETEACCESSORY` is TRUE [29].

### 3.4 Steel connections and fasteners

- Bolts, nuts, washers, welds: Tekla exports bolts with nuts and washers and welds as `IfcFastener` [29]; bolt groups are normally `IfcMechanicalFastener`, welds `IfcFastener` with a weld predefined type (unverified).
- Plates/gussets: `IfcPlate`; cleats/stiffeners: `IfcMember` or `IfcPlate`; steel beams use `IfcBeam` with `IfcIShapeProfileDef` and a profile name from the standard (e.g. IPE 300, HEA 200).
- Tekla lets you define which IFC entity each object becomes and add custom property sets for IFC export [29].
- Connection semantics for analysis (`IfcStructuralPointConnection`) are different from physical connection hardware; do not mix them.

### 3.5 Typical structural checks for an MCP server

- List all `IfcBeam`/`IfcColumn` with profile name, material, length.
- Sum concrete volume (`Qto_SlabBaseQuantities.NetVolume`) per storey; sum rebar mass per element.
- Find `IfcBuildingElementProxy` objects that should be columns/beams (misclassification).
- Check `LoadBearing` and `FireRating` flags in `Pset_BeamCommon`, `Pset_WallCommon` (unverified exact pset names).

---

## 4. Infrastructure in IFC 4.3

### 4.1 Status

- IFC 4.3 extends IFC to horizontal infrastructure: roads, railways, bridges, ports and waterways, and common elements [11][12][15].
- It was developed through the IFC-Rail and IFC-Infra projects; entity coverage was alignment, aggregated structures, earthworks, bridge structure, rail energy/signalling/track/telecom, drainage, maritime elements and "some geotechnics" [15][12].
- Announced as approved in January 2024 (article dated 5 January 2024, "100% approval") [11]; formally published by ISO as the 2024 edition of ISO 16739-1 [10]. In 2022 buildingSMART had already published it as a production standard [12].
- Buildings got only small changes; most changes concern infrastructure [13].

### 4.2 Tunnels status

- Tunnels were not in the initial IFC 4.3 content; entities were planned for IFC 4.4 [12][15]. The NIBS COBie V3 mapping page also marks tunnel entities as IFC4.4 [35].
- A buildingSMART forum reply (dated 24 March 2025, the only reply in the thread; QA-verified) said the work of the "IFC for Tunnel" project would go into an update of IFC 4.3.2.0 and might be called 4.4 "or something else" [16]. The IFC 4.3.x documentation of `IfcFacility` itself names `IfcTunnel` only as an example of a future facility type, while listing `IfcBuilding`, `IfcBridge`, `IfcRailway`, `IfcRoad` and `IfcMarineFacility` as the existing subtypes (QA-verified).
- A March 2026 buildingSMART Germany article (seen only as a search excerpt) reports that a Project Proposal for IFC 4.4 exists, with an ISO process to follow, and that IFC 4.4 is broader than just tunnels [17]. A buildingSMART statement (seen in search excerpts only) says 4.4 is meant to add to 4.3 without invalidating it.
- Practical answer for testers: "Does IFC 4.3 support tunnels?" Not as a complete domain (unverified for individual 4.3.x additions); tunnel-lining content is the 4.4/next-update topic. You can still model tunnel parts with generic classes (`IfcBuildingElementProxy`, `IfcCivilElement`, `IfcGeotechnicalElement` subtypes; unverified).

### 4.3 Alignment: horizontal, vertical, cant

- `IfcAlignment` is a `IfcLinearPositioningElement` and the layouts (`IfcAlignmentHorizontal`, `IfcAlignmentVertical`, `IfcAlignmentCant`) are `IfcLinearElement` subtypes; `IfcLinearElement` is an `IfcProduct` [6][3][4][5].
- An alignment can be described by a horizontal layout plus optionally a vertical layout and a cant layout, in several configurations [2].
- Horizontal: "a linear reference projected onto the horizontal x/y plane"; segments connect end-to-start [3][2].
- Vertical: a height profile along the horizontal alignment, points given as distance-along and height [5].
- Cant: a lateral inclination profile along the horizontal alignment; it carries a `RailHeadDistance` attribute and is used e.g. for structural gauge calculation [4].
- Segments (from background knowledge, unverified): horizontal segments are straight, circular arc, clothoid and related transitions, defined by start point, start direction, radii and length; vertical segments are constant gradient, circular arc, parabolic arc, defined by start distance, horizontal length, heights and gradients; cant segments are constant or linear/spiral transitions.
- Typical vocabulary: station / chainage (пикет, ПК; German Station/Stationierung), horizontal curve (план трассы, Lageplan/Trasse), longitudinal profile (продольный профиль, Gradiente/Höhenplan), superelevation or cant (вираж, Überhöhung / Querneigung), 線形 (Japanese: alignment).

### 4.4 Linear placement

- `IfcLinearPlacement` is an `IfcObjectPlacement` subtype alongside `IfcLocalPlacement` and `IfcGridPlacement` [see Sources, search excerpt].
- IFC4.1/4.2 form: `PlacementRelTo`/basis curve plus an `IfcDistanceExpression` carrying `DistanceAlong`, optional `OffsetLateral`, `OffsetVertical`, `OffsetLongitudinal` and `AlongHorizontal` (horizontal projection vs 3D distance) [7]. The IFC 4.3 form uses `IfcPointByDistanceExpression` (same distance/offset slots plus a basis curve) and an optional `CartesianPosition` (third-party implementation notes; the forms are not interchangeable) [8]. QA-verified against the IFC 4.3.x source: in 4.3 `IfcLinearPlacement` is a specialisation of `IfcObjectPlacement` whose `RelativePlacement` must be an `IfcAxis2PlacementLinear` ("placement that provides location and orientation confined to the context of a curve"; always 3D in nature), and `CartesianPosition` is an optional fallback for applications that cannot handle linear placement.
- In plain terms: place a bridge pier or a sign "at station 1+250, 2.5 m left of the centreline, 0.3 m above it" instead of giving X/Y/Z. If the alignment moves, the objects move.

### 4.5 Facilities and parts (road, rail, bridge, marine)

(Entity names from the schema, background knowledge, unverified in this session.)

- Facilities: `IfcFacility` with subtypes `IfcBridge`, `IfcRoad`, `IfcRailway`, `IfcMarineFacility`, plus `IfcBuilding`; parts: `IfcFacilityPart` with subtypes such as `IfcBridgePart`, `IfcRoadPart`, `IfcRailwayPart`, `IfcMarinePart`. Caution: the NIBS COBie V3 table lists "IfcRail, IfcRoad, IfcTunnel (IFC4.4)" in its Facility row [35] (QA-verified wording). Because the IFC 4.3.x `IfcFacility` documentation already lists `IfcRoad` and `IfcRailway` as existing subtypes (and `IfcTunnel` only as a future example), the "(IFC4.4)" label in the NIBS table is at best imprecise for road and rail; use the IFC 4.3 entity listing [1], not the NIBS label, to decide what exists in 4.3.
- Road elements: `IfcPavement`, `IfcCourse` (layers), `IfcKerb`; earthworks: `IfcEarthworksCut`, `IfcEarthworksFill`, `IfcReinforcedSoil`, `IfcEarthworksElement`; geotechnics: `IfcGeotechnicalStratum`, `IfcBorehole`, `IfcSolidStratum`.
- Rail: `IfcRail`, `IfcTrackElement`, `IfcRailway`, plus signalling, power and telecom devices (signal, mast, cable carrier, etc.).
- Bridges: `IfcBridge` with `IfcBridgePart` (SUPERSTRUCTURE, SUBSTRUCTURE, ABUTMENT, PIER, DECK...), elements such as `IfcDeepFoundation`, `IfcBearing`, `IfcBeam`, `IfcTendon`.
- Ports and waterways: `IfcMarineFacility` with `IfcMooringDevice`, `IfcNavigationElement` (unverified names). QA note: I do not believe there is an `IfcWaterway` entity in IFC 4.3 (the first pass wrote "IfcWaterway-style parts"); waterways are modelled as `IfcMarineFacility` with a `PredefinedType` (e.g. canal or navigational channel; enum values from memory, (unverified)).
- Most authoring tools do not yet write all of this. QA-verified on vendor pages (2026-11-06): the Archicad help (version 29 page) says Archicad handles IFC2x3, IFC4 and IFC4.3 for import and export [13]; Tekla's 2026 help says IFC export "supports the IFC 2X3, IFC 4, and IFC 4.3 schemas" but lists certified MVDs only for IFC 2x3 and IFC 4 [29-2026]; the open-source Revit IFC exporter has an "IFC4.3 Reference View" option (exchange requirements) added in add-on 26.4.1 (released 2025-12-18) and back-ported to 25.4.40 and 24.3.40 (2026-01-14), see `../03_software/revit/ifc_export_reference.md`. Whether any of this is buildingSMART-certified for 4.3 is a separate question (see section 1).

### 4.6 Tests that make sense for infrastructure

- Does the file declare `IFC4X3_ADD2` (or another 4X3 schema) in the header? Older libraries fail with "unknown entity IfcAlignment".
- List alignments with their layouts; count horizontal/vertical segments; compute alignment length.
- Resolve a linear placement to XYZ (requires a geometry engine that implements it; many viewers do not yet).
- Ask for stations of all elements placed along an alignment.

---

## 5. 4D: schedule linked to the model

### 5.1 Entities

- `IfcWorkPlan` groups work schedules (e.g. construction vs facility management); `IfcWorkSchedule` groups tasks toward a goal and can be labelled planned, actual or baseline (a duplicated copy used for comparison) [31]. The common chain is IfcWorkPlan -> IfcWorkSchedule -> IfcTask, although the specification does not clearly say whether a task belongs to a plan or a schedule [31, see Sources: OSArch thread].
- `IfcTask` is an identifiable unit of work; it can nest sub-tasks (a work breakdown structure), and the nesting (`IfcRelNests`) only affects display order, not logic [32][31].
- `IfcTaskTime` holds duration and dates. Attributes (background knowledge, unverified): `DurationType` (WORKTIME/ELAPSEDTIME), `ScheduleDuration`, `ScheduleStart`, `ScheduleFinish`, `EarlyStart/Finish`, `LateStart/Finish`, `FreeFloat`, `TotalFloat`, `IsCritical`, `StatusTime`, `ActualDuration`, `ActualStart`, `ActualFinish`, `RemainingTime`, `Completion`. Constraints can address a path such as `TaskTime.ScheduleStart` [32].
- Logic: `IfcRelSequence` links predecessor and successor tasks (`RelatingProcess`, `RelatedProcess`; types FINISH_START, START_START, FINISH_FINISH, START_FINISH, with an optional `IfcLagTime`) [32][31]. A lag may be an absolute duration or a ratio of the predecessor's duration [31].
- Calendars: `IfcWorkCalendar` defines working and non-working time; tasks inherit calendars from parent tasks [31].
- Resources: `IfcConstructionResource` items (crews, equipment, materials) connect to tasks [31].
- Linking to model elements: a task is related to the products it builds or installs. In IFC4 this is done with `IfcRelAssignsToProcess` for inputs (products consumed by the task) and `IfcRelAssignsToProduct` for outputs (unverified direction; the OSArch page does not name these relationships [31]).
- Authoring advice from the IfcOpenShell side: build schedules through the `sequence.*` API instead of creating `IfcTask`, `IfcWorkSchedule` or `IfcRelSequence` by hand (third-party guidance, see Sources).

### 5.2 Tools and reality

- Revit has no real 4D; the common workflow is Revit -> IFC or NWC -> a 4D tool (Navisworks TimeLiner, Synchro, etc.) where the schedule from MS Project / Primavera / Excel is imported and linked by selection sets, not by IFC. (Background knowledge, unverified.)
- Russian terms: ГПР / календарный график = work schedule; WBS = СДР; "связь предшественник-последователь" = predecessor/successor link; "4D-моделирование" = 4D simulation.
- IFC schedule data are mainly produced by open-source tools such as Bonsai (BlenderBIM) and IfcOpenShell scripts; many viewers do not display `IfcTask` at all.

### 5.3 4D checks for an MCP server

- List tasks with start/finish and duration; compute critical path from `IfcRelSequence`.
- Find elements with no task (unscheduled) and tasks with no elements.
- Shift a task and report which successors move (requires the tool to recalculate, IFC itself does not).
- Export a "who is built in week N" list.

---

## 6. 5D: cost

- `IfcCostSchedule` is "a collection of cost items, used for a specified purpose", e.g. a cost plan or a tender; it can carry approvals and actors (author, client, ...), holds one summary cost item that can be broken down into further items [33].
- `IfcCostItem` represents a cost line; it can nest other cost items into a hierarchy, carry classification references (phase code, CSI code, cost account), and hold standalone quantities of one measurement type [33].
- `IfcCostValue`: with no quantities it is the total cost; with quantities it is a unit cost multiplied by the summed quantities (e.g. 3 x 2 = 6). Cost categories (labour, material, transport, overhead) act as cost types; the special "*" category sums all nested items; the category filter sums only matching nested costs; values can be formulas [33].
- Linking physical elements to cost items: `IfcRelAssignsToControl`; this relationship also attaches the top-level cost item to the schedule [40]. In IFC4 the nested summing rule is: `AppliedValue` is the sum of nested costs of the same `CostType` [40, search excerpt].
- IfcOpenShell: first cost item must belong to a schedule; `cost.*` API (add schedule/item/value/quantity) is the documented route [see Sources, IfcOpenShell cost docs]. A Politecnico di Milano paper states that no BIM authoring software could write this entity, so the authors used IfcOpenShell to generate estimates [42].
- Practical reality: estimators usually take quantities from `Qto_*` (areas, volumes, lengths) or from Revit schedules, then price in Excel, Candy, iTWO, CostX, or a Russian cost package ("смета", ГЭСН/ФЕР norms - unverified details). The IFC cost chain is rarely produced by commercial authoring tools.
- Typical questions: "What is the total cost of walls on Level 2?" works only if the model has cost items linked via `IfcRelAssignsToControl`; otherwise the correct answer is "no cost data in this file; I can compute quantities".

---

## 7. FM and COBie

### 7.1 What COBie is

- COBie (Construction Operations Building information exchange) is an MVD of IFC for facility management data [38]. It is delivered as IFC, as a spreadsheet (SpreadsheetML/.xlsx/.csv) or as COBieLite XML; the spreadsheet is a readable snapshot, and IFC to spreadsheet is many-to-one, so the reverse is lossy [38][36].
- Source specs: NBIMS-US V3 section 4.2 and annexes (Annex A mappings, Annex B definitions); the original specification was an IFC2x3 MVD [38][39]. NIBS now publishes COBie V3 with mappings to IFC 4.3 and says the COBie3 MVD and IDS hold the formal definitions [35]. COBie 2.4 is the long-standing spreadsheet version.
- Authoritative commentators on a buildingSMART thread stress: COBie is a subset of IFC; a free IFC4 "responsibility matrix" mapping was not found; the output is only as good as the source IFC; owner history is often poorly implemented by authoring tools [36][37].

### 7.2 COBie sheets and IFC mapping

COBie V3 table from NIBS (IFC 4.3 unless noted) [35] (QA-verified: the NIBS "IFC Table A" lists exactly these V3 sheets: Instruction, Company, Facility, Level, SpaceType, Space, Zone, Type, Component, System, Resource, Job, Event, Package, Risk, Document, Attribute, Coordinate, PickList); the COBie 2.4 sheet names (Contact, Facility, Floor, Space, Zone, Type, Component, System, Assembly, Connection, Spare, Resource, Job, Impact, Document, Attribute, Coordinate, Issue, plus PickLists) are from background knowledge.

| COBie sheet | What it holds | IFC mapping |
|---|---|---|
| Contact (V3: Company) | People/organisations | `IfcOrganization` (and `IfcPerson`/actor) |
| Facility | The building/asset | `IfcProject`, `IfcSite`, `IfcFacility`, `IfcBuilding`, `IfcBridge`; IFC2x3: `IfcBuilding` |
| Floor (V3: Level) | Levels | `IfcFacilityPart`, `IfcBuildingStorey`; IFC2x3: `IfcBuildingStorey` |
| Space | Rooms | `IfcSpace`, `IfcExternalSpatialElement` |
| Zone | Groups of spaces (fire zone, HVAC zone) | `IfcZone` (members via `IfcRelAssignsToGroup`; members may be `IfcSpace`, `IfcZone`, `IfcSpatialZone`) |
| Type | Product models/catalogue items | `IfcElementType` subtypes (Table C of the NIBS document lists them) |
| Component | Individual assets | `IfcElement` subtypes (Table C) |
| System | Functional systems | `IfcSystem`, `IfcCircuit`, `IfcBuildingSystem`, `IfcStructuralSystem`, `IfcDistributionSystem` |
| Resource | Construction resources | `IfcConstructionEquipmentResourceType`, `IfcConstructionMaterialResourceType`, `IfcConstructionProductResourceType` |
| Job | Maintenance task templates | `IfcTaskType`; IFC2x3: `IfcTask` |
| Document | Manuals, drawings | `IfcDocumentInformation` |
| Attribute | Extra properties | `IfcPropertyValue` subtypes (i.e. property set contents) |
| Coordinate | Placement | `IfcLocalPlacement` |
| Others in V3 | Instruction, SpaceType, Event, Package, Risk, PickList | `IfcProject`/`IfcUnitAssignment`, `IfcSpaceType`, `IfcTask`, `IfcWorkPlan`, `Pset_Risk`, `IfcClassification` |
| Assembly, Connection, Spare, Impact, Issue | Not listed on the NIBS page I read | Not mapped there (unverified elsewhere) |

### 7.3 Assets, manufacturer data, warranty

Where typical COBie columns come from (property set names from background knowledge, unverified in this session):

- Type: category (from `IfcClassificationReference`, Uniclass/OmniClass), `AssetType` (Fixed/Movable), manufacturer, model number, warranty, replacement cost, expected life, nominal sizes. Sources: `Pset_ManufacturerTypeInformation` (Manufacturer, ModelLabel, ModelReference, ArticleNumber, ProductionYear), `Pset_Warranty` (WarrantyIdentifier, start/end dates, WarrantyPeriod, PointOfContact), `Pset_ServiceLife` (ServiceLifeDuration, MeanTimeBetweenFailure).
- Component: serial number, bar code, installation date, asset identifier, tag number, space. Sources: `Pset_ManufacturerOccurrence` (SerialNumber, BarCode, AcquisitionDate), occurrence-level `Name`/`Tag`, containment in an `IfcSpace` via `IfcRelContainedInSpatialStructure` or `IfcRelReferencedInSpatialStructure`.
- Zone and System membership: `IfcRelAssignsToGroup`.
- "Asset" in the FM sense is any component with a maintenance obligation; the COBie definition lists "maintainable asset classes" in Annex A [38].

### 7.4 Tools

- Bonsai (BlenderBIM) and BIMserver COBie plugins are named by the OSArch wiki as implementing the mapping correctly; Bonsai can write CSV/ODS [38]. A Python IFC-to-COBie converter was reported finished for all sheets in October 2019, alpha quality, CSV output with a log of missing data [36].
- Revit: no native "COBie spreadsheet" button, but the IFC exporter (open-source `Autodesk/revit-ifc`) ships a setup "IFC2x3 COBie 2.4 Design Deliverable View" with COBie company/project info tabs (QA-verified from the exporter resource file, see `../03_software/revit/ifc_export_reference.md`); typical flows add a COBie add-in or Excel mapping, or COBie parameters via shared parameters (product specifics unverified). The repository's `DefaultUserDefinedParameterSets.txt` also contains a commented `COBie_Specification` example set on `IfcElementType` (QA-verified). Bentley OpenBuildings has COBie spreadsheet population help [see Sources].
- Related modern approaches: IDS (Information Delivery Specification) and LOIN to state which data are required, and ISO 19650 asset information requirements (AIR).

---

## 8. Typical questions people ask about this

Real questions found (linked, paraphrased) and illustrative ones.

MEP
1. Why do I see IfcRelNests instead of IfcRelConnectsPortToElement for a space heater in a Revit 2020 IFC4 export, and how do I get dynamic port connections? (real) https://forums.buildingsmart.org/t/ifcrelconnectsporttoelement/2510
2. Why is IfcSystem information for pipes present in a Revit IFC2x3 export but missing in IFC4? (real) https://forums.buildingsmart.org/t/ifcsystem-information-related-to-pipes-ifc4-from-revit/3178
3. How do I model a basic residential electrical system (panel, switches, outlets, ports, system) with IfcOpenShell so Revit recognises the circuits? (real) https://www.github.com/IfcOpenShell/IfcOpenShell/discussions/4582
4. Port-to-port connectivity is lost when I convert a Revit IFC to a web format; is it the export or the converter? (real) https://github.com/ThatOpen/platform_services/issues/27
5. In Bonsai, how should flow direction behave for tees and manifolds with more than two ports? (real) https://community.osarch.org/discussion/comment/27745/
6. List all duct segments in system "Supply Air 1" and their total length. (illustrative)
7. Which pipes in the model are not connected to anything? (illustrative)
8. Add a "NominalDiameter" value to every IfcPipeSegment whose Name starts with "DN50". (illustrative)

Structural
9. Is there a final answer on whether Revit analytical elements can be exported to IFC? (real) https://forums.autodesk.com/t5/revit-structure-forum/is-there-a-final-answer-as-to-if-analytical-elements-can-be/m-p/9350321/highlight/true
10. How do I export a Revit structural analytical model to IFC? (real, API forum) https://forums.autodesk.com/t5/revit-api-forum/exportation-of-structural-analytical-model-to-ifc-file/td-p/12331957
11. How should rigid links be represented in an IFC structural analysis model? (real) https://forums.buildingsmart.org/t/rigid-link-representation-in-structural-analysis-model/1364
12. Concrete elements are missing from the Tekla IFC export, why? (real, Tekla support article title) https://support.tekla.com/article/concrete-elements-are-missing-from-the-exported-ifc-file
13. Give me total rebar mass per column and per level. (illustrative)
14. Which beams are IfcBuildingElementProxy instead of IfcBeam? (illustrative)

Infrastructure
15. Will tunnels be part of IFC 4.4, or of an update of 4.3.2.0? (real) https://forums.buildingsmart.org/t/ifc-for-tunnel/6031
16. Which software can already read IfcAlignment and IfcLinearPlacement correctly? (illustrative)
17. How many horizontal curves does alignment "Main Road" have, and what is the minimum radius? (illustrative)
18. Place a pier at station 1+250 on the alignment (linear placement). (illustrative)
19. Is IFC 4.3 certified in any software yet? (illustrative; see [13])

4D / 5D
20. How do I connect an IfcTask to the walls it builds, and show a 4D animation? (illustrative)
21. Which tasks are on the critical path in this IFC schedule? (illustrative)
22. What is the total cost of all slabs on level 3? (illustrative; correct behaviour depends on the cost chain, section 6)
23. Why does my 5D import in an estimating tool show zero cost? (illustrative)

FM / COBie
24. Is there a COBie responsibility matrix updated for IFC4? (real) https://forums.buildingsmart.org/t/cobie-and-ifc-mapping/1796
25. I need a document mapping IFC4 Add2 TC1 to COBie because my team thinks COBie needs new properties. (real) https://forums.buildingsmart.org/t/relation-ship-about-ifc-cobie/1478
26. Produce a COBie sheet of all components with serial number, manufacturer, space and warranty end date. (illustrative)
27. Which spaces are not assigned to any zone? (illustrative)

---

## 9. Common pitfalls and misconceptions

- "IFC4 means every relationship is IFC4 style." Revit exports `IfcRelNests` for ports in IFC4 but `IfcRelConnectsPortToElement` in IFC2x3; readers that only know one fail [21].
- "A system exists, so all its elements are in it." Systems are groups; elements may be absent or dropped by the exporter [22].
- "Missing connectivity is Revit's fault." Check the IFC text for `IfcRelConnectsPorts` before blaming the exporter; a viewer/converter can drop them [24].
- "Revit exports the analytical model to IFC." Not with the default exporter according to forum reports; use vendor/third-party plug-ins or analysis-tool formats [26].
- "Physical = analytical." They are different entity trees; a beam in one is not automatically linked to the other.
- "IFC 4.3 means my building files should switch." Nordic BIM advises specifying certified formats (IFC4/2x3) for buildings, since no 4.3 certification existed at the time of their page [13].
- "IFC 4.3 includes tunnels." Not as a full domain; tunnels are the 4.4 / future-update topic [12][16][17].
- "IfcLinearPlacement is the same in 4.1/4.2 and 4.3." The attribute structure differs; check the schema version in the header [7][8].
- "Task order = nesting order." `IfcRelNests` only affects display; logic is `IfcRelSequence` [32].
- "COBie spreadsheet can be converted back to IFC." Mapping is many-to-one; round-trip loses data [38][37].
- "COBie Facility is always IfcBuilding." In IFC 4.3 it can be `IfcFacility` and its subtypes; IFC2x3 uses `IfcBuilding` [35].
- "Cost data is in the IFC because the Revit schedule has prices." Revit schedules are not exported as `IfcCostSchedule`; the entity is rarely written by authoring tools [42].
- Wrong-direction flow: direction describes use, a pipe can carry flow both ways [23].

---

## Gaps

- The official buildingSMART specification pages (standards.buildingsmart.org, ifc43-docs.standards.buildingsmart.org, www.buildingsmart.org) could not be fetched (HTTP 403); I relied on search excerpts, forum threads, NIBS, OSArch, vendor help and background knowledge. Attribute lists for `IfcTaskTime`, alignment segments, structural entities, pset names and `IfcFacilityPart` subtypes are therefore marked unverified.
- The web-search quota was exhausted before searches in German (Trasse/Gradiente/Überhöhung; German national infrastructure BIM requirements), Chinese and Japanese (CIM/线形/道路 national standards), and Civil 3D / Revit-specific IFC 4.3 export capabilities. These remain open.
- Not verified: whether Revit exports `IfcStructuralAnalysisModel` in the latest releases; exact Revit export option names for rebar and base quantities. (QA 2026-11-06: resolved - the Revit IFC exporter does write IFC4.3 via the "IFC4.3 Reference View" option since add-on 26.4.1, 2025-12-18; resolved - Archicad and Tekla IFC 4.3 statements checked on vendor help pages.)
- QA 2026-11-06 still unverifiable: ISO catalogue page for ISO 16739-1:2024 and the buildingSMART approval page (HTTP 403); the buildingSMART Germany roadmap article (empty page); `IfcTaskTime` and `IfcRelConnectsStructuralElement` entity pages (404 on the mirrors tried); `IfcMarineFacility` enumeration; chapter-level claims about reinforcing-element hierarchy (the `IfcReinforcingBar` page confirms supertype `IfcElementComponent` and an `IfcReinforcingBarRoleEnum` role attribute only).
- The buildingSMART Germany roadmap article (Porto, March 2026) was seen only as a search excerpt; the fetch returned an empty page.
- Not reproduced because of suspicious or irrelevant nature: none skipped as malicious. Two aggregator pages (infralens.in listing ISO 16739-1:2024 as an "Indian Standard", and a skill-marketplace page for a COBie "skill") were not used as facts because they conflict with or are secondary to official sources.

---

## Sources

Official buildingSMART / NIBS (some seen only as search excerpts, see Gaps):

[1] IFC 4.3 Annex B entity listing: https://standards.buildingsmart.org/IFC/DEV/IFC4_3/HTML/annex-b1.html
[2] Alignment layouts (concepts): https://standards.buildingsmart.org/IFC/DEV/IFC4_3/HTML/concepts/Object_Composition/Nesting/Alignment_Layouts/content.html
[3] IfcAlignmentHorizontal: https://ifc43-docs.standards.buildingsmart.org/IFC/RELEASE/IFC4x3/HTML/lexical/IfcAlignmentHorizontal.htm
[4] IfcAlignmentCant: https://standards.buildingsmart.org/IFC/DEV/IFC4_3/HTML/lexical/IfcAlignmentCant.html
[5] IfcAlignmentVertical: https://standards.buildingsmart.org/IFC/RELEASE/IFC4_3/HTML/lexical/IfcAlignmentVertical.htm
[6] IfcLinearElement: https://ifc43-docs.standards.buildingsmart.org/IFC/RELEASE/IFC4x3/HTML/lexical/IfcLinearElement.htm
[7] IfcLinearPlacement (IFC4.2): https://standards.buildingsmart.org/IFC/DEV/IFC4_2/FINAL/HTML/schema/ifcgeometricconstraintresource/lexical/ifclinearplacement.htm
[8] Third-party IFC4X3 implementation notes (Rust crate, not official): https://docs.rs/ifc-alignment/0.3.2/src/ifc_alignment/placement/linear.rs.html
[9] IFC 4.3 approved as a final standard: https://www.buildingsmart.org/ifc-4-3-approved-as-a-final-standard/
[10] IFC 4.3 formally approved and published as an ISO standard: https://www.buildingsmart.org/?p=29521
[11] Construction Management, 5 Jan 2024: https://constructionmanagement.co.uk/digital-construction/ifc-4-3-for-infrastructure-approved-as-final-standard/
[12] Construction Management, 13 Jul 2022: https://constructionmanagement.co.uk/buildingsmart-international-publishes-ifc4-3-for-infrastructure/
[13] Nordic BIM, IFC 4.3: https://www.nordicbim.com/knowledge/en/ifc-4.3
[14] buildingSMART IFC4.3.x-development repository: https://github.com/buildingSMART/IFC4.3.x-development
[15] ACCA/BibLus, IFC 4.3 overview: https://biblus.accasoftware.com/en/ifc-4-3-the-new-ifc-standard-for-exchanging-openbim-models-of-infrastructural-works/
[16] Forum: IFC for Tunnel: https://forums.buildingsmart.org/t/ifc-for-tunnel/6031
[17] buildingSMART Germany, IFC roadmap after Porto (excerpt only): https://www.buildingsmart.de/buildingsmart/aktuelles/ifc-roadmap-nach-porto-version-44-kommt-ifc-5-wird-zu-ifc-x
[18] IfcFlowSegment (development docs, raw): https://raw.githubusercontent.com/buildingSMART/IFC4.3.x-development/master/docs/schemas/shared/IfcSharedBldgServiceElements/Entities/IfcFlowSegment.md
[19] IfcDistributionPort (IFC4): https://standards.buildingsmart.org/IFC/RELEASE/IFC4/FINAL/HTML/schema/ifcsharedbldgserviceelements/lexical/ifcdistributionport.htm
[20] MVD Port Connectivity (IFC4 Add2 RV1.2): https://standards.buildingsmart.org/MVD/RELEASE/IFC4/ADD2_TC1/RV1_2/HTML/schema/templates/port-connectivity.htm
[21] Forum: IfcRelConnectsPortToElement: https://forums.buildingsmart.org/t/ifcrelconnectsporttoelement/2510
[22] Forum: IfcSystem information related to pipes, IFC4 from Revit: https://forums.buildingsmart.org/t/ifcsystem-information-related-to-pipes-ifc4-from-revit/3178
[23] OSArch: Bonsai ports PR discussion: https://community.osarch.org/discussion/comment/27745/
[24] ThatOpen platform_services issue 27: https://github.com/ThatOpen/platform_services/issues/27
[25] IfcOpenShell discussion 4582 (MEP modeling): https://www.github.com/IfcOpenShell/IfcOpenShell/discussions/4582
[26] Autodesk forums on analytical-to-IFC: https://forums.autodesk.com/t5/revit-structure-forum/is-there-a-final-answer-as-to-if-analytical-elements-can-be/m-p/9350321/highlight/true ; https://forums.autodesk.com/t5/revit-api-forum/exportation-of-structural-analytical-model-to-ifc-file/td-p/12331957 ; IFC 4.3 structural analysis domain (dev build): https://standards.buildingsmart.org/IFC/DEV/IFC4_3/HTML/ifcstructuralanalysisdomain/content.html ; AUGI thread: https://forums.augi.com/archive/index.php/t-165346.html
[27] Graphisoft, IFC Structural Analysis Model import/export (experimental): https://help.graphisoft.com/AC/27/INT/_AC27_Help/090_StructuralAnalyticalModelTools/090_StructuralAnalyticalModelTools-62.htm
[28] Forum: rigid link representation: https://forums.buildingsmart.org/t/rigid-link-representation-in-structural-analysis-model/1364
[29] Tekla Structures IFC export (2026): https://support.tekla.com/doc/tekla-structures/2026/int_ifc_export ; property sets for IFC export (2020): https://support.tekla.com/doc/tekla-structures/2020/int_defining_property_sets_using_property_set_definitions ; missing concrete elements: https://support.tekla.com/article/concrete-elements-are-missing-from-the-exported-ifc-file
[30] Graphisoft community, IfcSystem mapping from Revit MEP (old): https://community.graphisoft.com/t5/Collaboration-with-other/IfcSystem-mapping-from-Revit-MEP/m-p/193468 ; Graphisoft help center mapping: https://helpcenter.graphisoft.com/de/user-guide/93090 ; CYPE plug-in (commercial): https://info.cype.com/en/subject/plugin-open-bim-revit-generating-native-revit-elements-from-an-ifc-file-of-piping-systems/
[31] OSArch wiki, IFC sequence concepts: https://wiki.osarch.org/ifc-industry-foundation-classes-ifc-concepts-ifc-sequence-concepts/ ; OSArch forum thread: https://community.osarch.org/discussion/comment/6498
[32] IfcTask (IFC 4.3.2.0): https://standards.buildingsmart.org/IFC/RELEASE/IFC4_3/HTML/lexical/IfcTask.htm ; Pset_WorkControlCommon: https://standards.buildingsmart.org/IFC/RELEASE/IFC4_3/HTML/lexical/Pset_WorkControlCommon.htm ; IfcOpenShell sequence guidance (third-party skill page): https://skills.sh/openaec-foundation/computational-design-day-delft-march-2026/ifcos-impl-sequence
[33] OSArch wiki, IFC cost concepts: https://wiki.osarch.org/ifc-industry-foundation-classes-ifc-concepts-ifc-cost-concepts/
[35] NIBS, COBie V3 mapping to IFC 4.3: https://nibs.org/nbims/v3/cobie/6-2/
[36] Forum: COBie and IFC mapping: https://forums.buildingsmart.org/t/cobie-and-ifc-mapping/1796
[37] Forum: Relation ship about IFC & COBie: https://forums.buildingsmart.org/t/relation-ship-about-ifc-cobie/1478
[38] OSArch wiki, COBie: https://wiki.osarch.org/construction-operations-building-information-exchange-cobie/
[39] NBIMS-US V3 COBie Annex A: https://www.nibs.org/files/pdfs/nbimsv3/NBIMS-US_V3_4.2_COBie_Annex_A.pdf
[40] IfcCostSchedule / IfcCostItem (IFC4 and IFC4.2 pages): https://standards.buildingsmart.org/IFC/RELEASE/IFC4/FINAL/HTML/schema/ifcsharedmgmtelements/lexical/ifccostschedule.htm ; https://nibs.org/files/docs/IFC4x2_Bridge/schema/ifcsharedmgmtelements/lexical/ifccostschedule.htm
[41] Bentley OpenBuildings Designer, populating COBie spreadsheet: https://DOCS.BENTLEY.COM/LiveContent/web/OpenBuildings Designer Help-v7/en/GUID-AC611F03-3D8A-4EF7-804B-ED0F6CDA3889.html
[42] Cost estimation paper (Politecnico di Milano) and ITcon 2024 cost-domain paper: https://re.public.polimi.it/retrieve/84b2e3ca-76b9-4b30-8a57-6e1c204a373b/EC32024_255.pdf ; https://www.itcon.org/papers/2024_58-ITcon-SI-Cassandro.pdf
[43] IfcOpenShell IfcCostItem class docs (seen as a search result only): https://ifcopenshell.github.io/docs/rst_files/class_ifc4_1_1_ifc_cost_item.html
