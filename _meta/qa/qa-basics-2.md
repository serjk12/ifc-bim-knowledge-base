# QA log: basics-2 (01_ifc_basics 05-08 and 03_software)

Date of pass: 2026-11-06. Scope: `01_ifc_basics/05_*` to `08_*`, `03_software/authoring_tools_ifc.md`, `03_software/viewers_checkers_cde_converters.md`, `03_software/revit/ifc_export_reference.md`, `03_software/revit/ifc_import_link_reference.md`.

Method and limits (read first):

- Only web pages were read (WebFetch); nothing was downloaded, installed or executed. Page text was treated as data.
- WebSearch was available for the first few queries only; its per-session budget (200, shared) was then exhausted, so later checks used direct fetches of primary pages.
- The official buildingSMART spec hosts (`standards.buildingsmart.org`, `ifc43-docs.standards.buildingsmart.org`, which 301-redirects to the `IFC/DEV/IFC4_3` build), `iso.org`, `buildingsmart.org`, Autodesk support articles and the GitHub REST API for single issues returned HTTP 403. Workarounds that worked: (a) the buildingSMART GitHub documentation sources (`raw.githubusercontent.com/buildingSMART/IFC4.3.x-development/...`), (b) the buildingSMART documentation mirror for the **IFC 4.4.0.0 working draft** at `bsi-infraroom.github.io/IFC-Documentation-Tunnel/4_4_0_0/...` (used for all Pset/Qto lists; it is a draft, so 4.3.2.0 may differ slightly), (c) the GitHub releases API for the list endpoint, (d) Autodesk help hosts `up1.autodesk.com` and `help.autodesk.com`, (e) vendor sites.
- No pirated, crack, keygen or suspicious sites were encountered or linked. No online converter sites were visited.
- No personal data of posters was added.

## 1. Corrections made (errors found and fixed in place)

| # | File | Wrong text (first pass) | Corrected to | Evidence |
|---|---|---|---|---|
| 1 | 05 | `Infiltration` typed `IfcVolumeFlowRateMeasure` | `IfcVolumetricFlowRateMeasure` (door and window) | Pset_DoorCommon / Pset_WindowCommon, 4.4 draft mirror |
| 2 | 05 | `GlazingAreaFraction` typed `IfcRatioMeasure` | `IfcPositiveRatioMeasure` | same |
| 3 | 05 | `Pset_CoveringCommon` listed `TotalThickness` "from memory" | Removed; real set has 11 properties incl. `FlammabilityRating`, `FragilityRating`, `Finish` (IfcText), `Reference`, `Status` | Pset_CoveringCommon page |
| 4 | 05 | `Pset_RoofCommon`: `ProjectedArea`, `TotalArea` implied as properties | They appear only in the history note (IFC2x3); set has 7 properties (Reference, Status, AcousticRating, IsExternal, ThermalTransmittance, LoadBearing, FireRating); roof areas are in `Qto_RoofBaseQuantities` | Pset_RoofCommon + Qto_RoofBaseQuantities pages |
| 5 | 05 | `Pset_ColumnCommon` list missed `Roll` and `ThermalTransmittance` | Full 8-property list | Pset_ColumnCommon page |
| 6 | 05 | `Pset_BeamCommon`: "`Slope` presence unverified" | Verified: Reference, Status, Span, Slope, Roll, IsExternal, ThermalTransmittance, LoadBearing, FireRating (9). Residual: a search summary of the frozen 4.3.2 page listed 8 (no `Status`) | mirror vs search summary |
| 7 | 05 | `Qto_WallBaseQuantities`: `GrossFootprintArea` / `NetFootprintArea` | `GrossFootPrintArea` / `NetFootPrintArea` (capital P); `GrossWeight`/`NetWeight` confirmed in draft mirror | Qto_WallBaseQuantities page |
| 8 | 05 | `Pset_DoorCommon` / `Pset_WindowCommon` short, incomplete lists | Full lists (19 and 17 properties); note that windows have no `LoadBearing`/`SelfClosing`; `WaterTightnessRating`, `MechanicalLoadRating`, `WindLoadRating` added in IFC4 Add1 | the two pset pages |
| 9 | 05 | `Pset_BuildingStoreyCommon` lacked 4.4-draft extras | Added `Reference`, `LoadBearingCapacity`, `ElevationOfSSLRelative`, `ElevationOfFFLRelative` flagged "(4.4 draft mirror)", presence in frozen 4.3.2 unverified | pset page |
| 10 | 05 | Spec example for type/occurrence override: `ThermalTransmittance` described as occurrence-level and "added" | In the spec example the **type's** `ThermalTransmittance` (0.375) still applies to the wall | IfcRelDefinesByType source |
| 11 | 05 | Qto rows for Door, Slab, Space, Beam, Column, Covering, Roof "not retrieved" | Filled with verified quantity lists (Door 4, Slab 10, Space 13, Beam 9, Column 9, Covering 3, Roof 3); Storey confirmed (7) | 7 qset pages |
| 12 | 05 | User-defined Revit pset file: I/T flag and TAB rules "unverified" | Verified: tab-separated; flag not required from 2024.1; type properties not exported unless a type entity is named (since 24.1.0); class-name case sensitivity and the Boolean snag remain community-only | Autodesk Revit 2025 help; template header on GitHub |
| 13 | 05 | IFC versions in Revit export "(from memory, unverified)" | Replaced by verified list incl. IFC4.3 Reference View since add-on 26.4.1 | releases API |
| 14 | 06 | `IfcRigidOperation` "details not fetched" | Verified: new in IFC4X3_ADD1; offset only (`FirstCoordinate`, `SecondCoordinate`, `Height`), no conversion/distortion. `IfcMapConversionScaled` also new in IFC4X3_ADD1 (`FactorX/Y/Z`) | entity sources |
| 15 | 06 | `IfcPolygonalFaceSet` new in IFC4 ADD2 (only claimed) | Verified in the entity's version note | entity source |
| 16 | 06 | Revit Coordinate Base "names as seen across sources" | Verified four choices (Shared Coordinates default, Survey Point, Project Base Point, Internal Origin); True-North variants come from the exporter resource file | Autodesk IFC Exporter help 25.2 |
| 17 | 06 | "Keep content within about 16 km (10 miles)" stated as fact | Marked (unverified); only blog sources, no readable Autodesk page | (not resolvable) |
| 18 | 06 | `get_local_placement` "function name unverified" | Verified in `util/placement.py` (v0.8.0) | raw source |
| 19 | 07 | КСИ: "Order 430/pr of 06.08.2020 ... [26]" presented as sourced | Cited pages do **not** mention it; marked unverified. Verified instead: AKM news 13 Jan 2021 (21 tables updated, 700+ changes, no order number) and ГОСТ Р ИСО 12006-2-2017 (Rosstandart order 618-st of 30.06.2017, identical to ISO 12006-2:2015, effective 1 Oct 2017). Source [26] annotated accordingly | pravo.ppt.ru, normacs.info, akm.ru |
| 20 | 07 | Revit Assembly Code configuration "Manage > Project Settings > Assembly Code" | Help page truncates the path; path marked unverified; verified the usable path: Edit Type > Assembly Code > browse > "Choose Assembly Code" | Revit 2018 help |
| 21 | 07 | `ReflectanceMethod (PHONG, PHYSICAL, FLAT)` partial | Full enum: BLINN, FLAT, GLASS, MATT, METAL, MIRROR, PHONG, PLASTIC, STRAUSS, PHYSICAL, NOTDEFINED | IfcReflectanceMethodEnum source |
| 22 | 07 | Uniclass / OmniClass tables only partly listed | Full verified lists (12 Uniclass tables; 15 OmniClass tables with 21=UniFormat, 22=MasterFormat, 23=EPIC) | NBS, CSI |
| 23 | 08 | Port `FlowDirection` "SINKANDSOURCE" | Enum literal is `SOURCEANDSINK` (also NOTDEFINED); connected ports need same system type and opposite directions | IfcFlowDirectionEnum, IfcDistributionPort source |
| 24 | 08 | `IfcElectricDistributionBoard` "unverified rename" | Verified: deprecated in the 4.3 line (import allowed, do not export; supertype `IfcFlowController`); IfcDistributionBoard is the entity used in the cited thread | 4.4 draft mirror |
| 25 | 08 | Analytical-to-physical link `IfcRelAssignsToProduct` "unverified" | Verified in `IfcStructuralItem` source | entity source |
| 26 | 08 | "IfcWaterway-style parts" | No such entity believed to exist; flagged and rephrased (waterways via `IfcMarineFacility` + PredefinedType, enum values unverified) | IfcFacility source lists subtypes |
| 27 | 08 | Revit 4.3 export "unverified whether a 4.3 option exists" | Exists: IFC4.3 Reference View since 26.4.1 (2025-12-18), back-ported 2026-01-14 | releases API |
| 28 | 08 | NIBS "IfcRail, IfcRoad, IfcTunnel (IFC4.4)" noted as odd | Confirmed wording; since `IfcFacility` docs already list `IfcRoad` and `IfcRailway`, the NIBS "(IFC4.4)" label is imprecise | NIBS page, IfcFacility source |
| 29 | 08 | Revit "no native COBie IFC button" | Refined: exporter has the "IFC2x3 COBie 2.4 Design Deliverable View" setup and COBie tabs | exporter resource file (see ifc_export_reference) |
| 30 | 03 export ref | Release table years wrong for IFC.v26.4.1 (listed 2026), IFC_v26.4.0 (2026), IFC_v25.4.40 (2025), IFC_v24.3.40 (2024) | Correct: 2025-12-18, 2025-10-30, 2026-01-14, 2026-01-14. Added missing rows v25.4.4, v25.4.3, v26.1.0, v24.3.20 | GitHub releases API |
| 31 | 03 export ref | ISO numbers: "IFC2x3 TC1 and IFC4 (ADD2 TC1) are ISO 16739:2013 and ISO 16739-1:2018" | Rephrased: IFC2x3 ~ ISO/PAS 16739:2005, IFC4 = ISO 16739:2013, IFC4 ADD2 TC1 = ISO 16739-1:2018, 4.3.2.0 = ISO 16739-1:2024 (all from memory except 2024; marked unverified) | Wikipedia (2024 only) |
| 32 | 03 export ref | User-defined pset file data types short list | Template lists many more types alphabetically (Acceleration, AngularVelocity, Area, AreaDensity, Boolean, ... Length, Mass, Text, Volume); first-pass list marked incomplete | template header |
| 33 | 03 viewers | IfcConvert output formats incl. HDF5; no mention of default excludes | HDF5 removed; verified list OBJ, DAE, GLB, STP, IGS, XML, JSON (xeokit), RDB, SVG, TTL, IFC; default `--exclude=entities IfcOpeningElement IfcSpace` | IfcConvert usage page (0.9.0post1) |
| 34 | 03 authoring | Archicad: IFC2x3/IFC4 "(unverified)", path "(unverified)" | IFC2x3, IFC4, IFC4.3 import/export; File > Interoperability > IFC > IFC Translators; default import = "Import as IFC Properties"; Archicad 30 released 7 Oct 2026 | Graphisoft help AC29/AC27; Wikipedia |

## 2. Claims re-verified and left unchanged (confirmed)

- 05: `Pset_WallCommon` 11 properties and types; `Pset_SlabCommon`, `Pset_SpaceCommon` (no Category), `Pset_ManufacturerTypeInformation` core properties; `ProductionYear` is IfcLabel; `AssemblyPlace` new in IFC4; `Reference` deprecated since 4.3.0.0; `Qto_BuildingStoreyBaseQuantities`; `Qto_Door/WindowBaseQuantities`; override rule occurrence over type; `IfcPropertyBoundedValue` (inclusive bounds, `SetPointValue` IFC4, unit rule), `IfcPropertyTableValue` (unique defining values, linear default, 3+ columns via IfcTable), `IfcElementQuantity.MethodOfMeasurement` ('BaseQuantities', DIN277-2, 2.BV); Revit Property Sets option labels (25.2 help); `IsExternal` type-level removal in 25.2.0.5; type properties not exported since 24.1.0.
- 06: `IfcMapConversion` rotation by `atan2(XAxisOrdinate, XAxisAbscissa)` (text unchanged), EPSG examples 5555 / 9286 / 9306 names, `IfcUnitAssignment` WR01 and single monetary unit, `IfcGeometricRepresentationContext` (ContextType Model/Plan/NotDefined, Precision 1E-5..1E-8, TrueNorth default (0,1), informational when a coordinate operation exists), US survey foot value (math check 1200/3937 m).
- 07: `IfcCardinalPointReference` 1-20, `IfcMaterialLayer` (Category keywords, Priority 0-100, IsVentilated semantics, non-negative thickness), `IfcMaterialList` deprecated, GB/T 51269-2017 data (issued 2017-10-25, effective 2018-05-01, MOHURD Announcement 1715), ETIM 10.0 numbers (97 / 491 / 5,799; article 31 Jan 2025), Revit issue #543 (2022.5.1.0, by design).
- 08: IFC 4.3 approval news dated 5 Jan 2024 ("100% approval"); forum tunnel reply (24 Mar 2025); GitHub README (CC BY-ND 4.0 for static releases); Nordic BIM page (no software certified for 4.3; page shows "May 11, 2026"); `IfcDistributionPort` nesting via `IfcRelNests`, `IfcRelConnectsPortToElement` for dynamic ports; Archicad structural analysis import IFC2x3/IFC4, export IFC2x3 only, experimental feature; Tekla 2026: schemas 2x3/4/4.3, certified MVDs 2x3 and 4, ifcXML 2x3 only; NIBS COBie V3 sheet list.
- 03: Solibri legacy statement and tier names; Speckle Explore plan; xeokit AGPL-3.0; web-ifc MPL-2.0; IDS "over 250 test file pairs"; validate service four checks (bSDD disabled); FZKViewer 6.5.1 / 2023-01-31 no further development; Trimble Connect APIs and "legacy credentials in or before early 2026"; FreeCAD default `DefaultIfcExportVersion` = "IFC4"; Bonsai schema choice IFC2X3/IFC4/IFC4X3 and Ctrl+S saves only the .ifc; Renga Software is a joint venture of 1C and ASCON; Vectorworks first IFC4 Export Certification April 2019 (as worded on Wikipedia); BricsCAD "certified for IFC 4.3" (Wikipedia wording, with promotional-tone warning).

## 3. Residual uncertainty (marked "(unverified)" or flagged in the files)

- Pset/Qto lists come from the IFC 4.4.0.0 draft mirror; the frozen 4.3.2.0 pages were unreachable. Specific doubtful points: `Pset_BeamCommon.Status` (8 vs 9 properties across two sources); `Pset_BuildingStoreyCommon` extras; `Qto_WallBaseQuantities` weights in 4.3.2; first release in which `GlobalTradeItemNumber` and the document references of `Pset_ManufacturerTypeInformation` appeared; documentation chapter numbers (6.1.4.x etc.) were not re-checked.
- 06: Revit "16 km / 10 miles" limit; `PointCloud` deprecation text; LoGeoRef literature (secondary); sub-context identifier list.
- 07: КСИ order number and date (430/pr, 06.08.2020), "21 tables, 30,000+ elements", GOST R 10.0.02-2019 / "10.0.03" references; NL-SfB, CoClass code shapes; Revit Assembly Code settings path; Uniformat level letters, MasterFormat 50 divisions (background knowledge).
- 08: `IfcMarineFacility` enumeration; `IfcTaskTime` attribute list and `IfcRelConnectsStructuralElement` (pages 404 on mirrors tried); full infrastructure entity listing (spec "Annex B" not reachable); ISO page for ISO 16739-1:2024 (403).
- 03: Allplan, Bentley, nanoCAD, BIMBase/Glodon/PKPM, GLOOBE, Edificius, SketchUp (help page 404), Rhino (404), Civil 3D "IFC 4.3 Extension" details remain unverified; IfcConvert options `--use-element-guids`, `--site-local-placement`, `--building-local-placement`; prices, plan tiers and vendor feature claims of BIMvision, Dalux, Catenda, Revizto, dRofus, BIMFACE, Simplebim, CAD Exchanger were not re-checked.
- Revit exporter/import: statuses of GitHub issues quoted in `ifc_import_link_reference.md` (#15, #223, #321, #522, #566, #710, #928, #951, #970, #990, #1019 and others) are as read in the first pass; the GitHub issue API returned HTTP 403 during this pass, so open/closed status may have changed. Revit menu paths (File > Export > IFC, Insert > Link IFC, Manage Links > IFC tab) remain without an Autodesk page confirming them.

## 4. Gaps

- Native-language verification (German, Chinese, Japanese, Russian official sources) could not be extended because the search quota was spent. Russian sources checked: akm.ru news (КСИ update), pravo.ppt.ru (Rosstandart 618-st), normacs.info; docs.cntd.ru was unreachable (connection refused).
- Skipped for safety or irrelevance: none flagged as suspicious. Aggregator pages already noted in the first pass (infralens.in listing ISO 16739-1:2024 as an "Indian Standard"; a skill-marketplace page about a COBie "skill") were not used as facts and remain unused.
- Suggested follow-ups when search access is available: confirm the КСИ order number and date on a Minstroy/ГИСОГД page; re-read the frozen IFC 4.3.2.0 pages for Pset_BeamCommon.Status and Pset_BuildingStoreyCommon; check the buildingSMART certification list for IFC 4.3 (BricsCAD, Archicad, Tekla, Revit); confirm Autodesk help paths for Link IFC / Open IFC.

## 5. Files changed

- `01_ifc_basics/05_properties_quantities_psets.md`
- `01_ifc_basics/06_geometry_placement_coordinates_units.md`
- `01_ifc_basics/07_materials_classification_types_styles.md`
- `01_ifc_basics/08_domains_mep_structural_infra_4d5d_fm.md`
- `03_software/authoring_tools_ifc.md`
- `03_software/viewers_checkers_cde_converters.md`
- `03_software/revit/ifc_export_reference.md`
- `03_software/revit/ifc_import_link_reference.md`
- `_meta/qa/qa-basics-2.md` (this log)
