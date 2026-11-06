# Infrastructure (IFC 4.3), site and terrain, GIS and digital twins, energy analysis

Topics covered (vocabulary tags): `infrastructure_ifc43`, `site_terrain`, `gis_citygml_digital_twin`, `energy_bem_gbxml`.
Evidence base: 212 distinct real records (135 + 16 + 58 + 12, minus overlaps) and up to 78 synthetic prompts in `research_raw/wave1`, read in full for this page. Last compiled: 2026-11-06.

## In plain words

Most IFC files describe a **building**. IFC 4.3 (the edition published as ISO 16739-1:2024) added the vocabulary for things that are not buildings: **roads, railways, bridges, ports**, and the thing that holds them together, the **alignment**, which is the centre-line of a road or track described by horizontal curves, a height profile and (for rail) cant. Objects can then be placed "at station 1+250, 2 m left of the centre-line" instead of with X/Y/Z. Tunnels are not a finished domain in 4.3 (planned for a later update). See [domain overview, section 4](../../01_ifc_basics/08_domains_mep_structural_infra_4d5d_fm.md) and [IFC versions](../../01_ifc_basics/01_what_is_ifc_and_versions.md).

Around that sits the question "where on Earth is this?". A building model lives in a local coordinate system near zero; GIS and web-globe tools (QGIS, ArcGIS, Cesium) need to know the map coordinate system, the shift, the rotation to north and the unit. IFC stores that in `IfcMapConversion` and `IfcProjectedCRS` (IFC4 and later) or, in older files, in rough latitude/longitude on `IfcSite`. Most "my model landed in the ocean" complaints are a unit, scale or missing-CRS problem. See [geometry, placement, coordinates, units](../../01_ifc_basics/06_geometry_placement_coordinates_units.md). The **terrain** (site) is usually a triangulated surface, and its quantities (cut and fill) are fragile. **Digital twin** questions are really about how to connect sensors, asset tags and city-model formats (CityGML, 3D Tiles) to IFC without bloating it. **Energy analysis** is a different world: the usual handoff is gbXML or an energy model, not IFC; the IFC-side tool is space boundaries, which are optional and easy to get wrong. See [abbreviations (gbXML, CityGML)](../../08_glossary/abbreviations.md).

One-sentence summary for a tester with no BIM background: **these tasks fail on tiny, checkable facts in the file header and the coordinate settings (schema name, units, CRS, which entities exist); a good assistant checks those facts first, reports exactly what is present or absent, and never invents a coordinate system, a station or a U-value.**

How to read this page: "real" rows are *paraphrases written by the research pass* of questions seen at the linked source, not verbatim quotes; non-English rows keep the original language with an English gloss. "Synthetic" prompts are written for testing and never presented as real.

Coverage caveats (design your tests around them):
- Infrastructure and GIS real evidence is overwhelmingly English (buildingSMART forum, IfcOpenShell/web-ifc GitHub, OSArch, Cesium community). Real non-English items exist in Norwegian, Dutch, Chinese, Japanese, Spanish, Italian, German and one Russian item; they are mostly guideline pages and blog posts, not user questions.
- **Energy is thin.** Only 12 real records, all English and all about space boundaries, thermal material data or layer data. No real gbXML, EnergyPlus-model or Revit Energy Analysis question was found in the KB. Anything beyond space boundaries in the energy part below comes from the reference docs or is marked as a test design choice.
- **Site/terrain is thin.** 16 real records, mostly English issue-tracker items.

---

## Problem map

Roughly ranked by number of real records (several records can point at one thread).

| # | Problem | How users describe it | Frequency signal | Root cause | Typical fix |
|---|---|---|---|---|---|
| 1 | Alignment is in the file but tool or viewer shows nothing | "Can not display Alignments", "alignment not shown", "IfcGradientCurve not implemented", "Civil 3D alignment export errors" | ~40 records, ~32 threads; en, zh | Alignment is nested layouts (horizontal/vertical/cant) plus a curve representation; viewers and libraries implement only part; some exports carry no representation | Check schema, entities and representations; use a library build that implements the curves; update the viewer |
| 2 | Wrong location: model lands "in the ocean", wrong scale, drifts | "Revit IFC4 lands in the ocean in Cesium", "gpkg in the ocean in QGIS", "coordinates changed after BlenderGIS" | ~32 records, ~30 threads; en, nl, ja, zh | Missing/ignored `IfcMapConversion`+`IfcProjectedCRS`; mm vs m with missing Scale; tools reading `IfcSite` lat/long instead; offset baked into placements | Read the real fields, fix unit/Scale, set CRS, tell the tiler which CRS to use |
| 3 | IFC 4.3 file does not open / schema error | "SchemaError: Unsupported schema: IFC4X3", "file with IFC4X3_ADD2 header fails to link in Revit 2024" | ~19-24 records, ~14 threads; en | Identifier must be `IFC4X3_ADD2` (case-sensitive) and the build must include it; Revit 2024 link bug; older viewers | Right package/build; temporary header edit; update software |
| 4 | Everything arrives as `IfcBuildingElementProxy`; wrong facility/part hierarchy | "road model: all proxies", "IfcBridge or IfcRoad for the wearing course?", "railway part turns into IfcSpace" | ~19 records, ~13 threads; en, de | Exporter has no mapping to 4.3 classes; Revit 4.3 export files elements under Building; authoring tools hard-code building hierarchy | Use the 4.3 extension/mapping file; upgrade then reassign classes; follow a bridge hierarchy convention |
| 5 | IFC to CityGML / 3D Tiles / GIS conversion | "broken faces in CityGML", "0 files loaded", "convert IFC to 3D Tiles", "CityJSON into IFC" | ~12 records, ~10 threads; en, de, es, ja, zh | Lossy by nature (LoD, envelope only); converter libraries lack IFC4 support; georeference missing | Use FME/ion/ifc2gis or envelope extraction; define LoD; verify CRS first |
| 6 | Sectioned solids, sweeps, cant render wrongly | "IfcSectionedSolidHorizontal ignores orientation", "twist due to cant not considered" | ~10 records, ~9 threads; en | Complex placements (`IfcAxis2PlacementLinear`) and open-ended surfaces implemented differently by engines | Update engine; compare in a second viewer; avoid concluding the model is wrong |
| 7 | Energy handoff: space boundaries missing or shifted | "boundaries only four walls", "2nd-level geometry displaced from IfcSpace", "centre line or inside face?" | 12 records, 12 threads; en | Space boundaries are optional (Revit default None); phase/room-bounding settings; level-1/2 semantics; exporter bugs | Enable boundaries, align the Energy Settings phase, test one model manually, follow the customer's rule |
| 8 | Stationing (chainage) vs DistanceAlong; linear placement | "my station 15+00 landed at 1500 ft", "signal sits at origin" | ~10 records, ~8 threads; en | `DistanceAlong` is purely geometric; station is semantic (`IfcReferent` + `Pset_Stationing`); importers may not apply linear placement | Add start-station offset; use referents; check importer support |
| 9 | Digital twin: sensors, asset IDs, properties in web viewers | "where to store sensor data", "500 projects, one query", "Korean property not searchable in Cesium" | ~8 records, ~8 threads; en | IFC is a file, not a time-series store; property keys combine pset and property name; encoding of non-ASCII text | Keep IDs in a pset, link external data; database/GIS hybrid; check string encoding |
| 10 | Terrain and earthworks | "slab to IfcSite fails after editing points", "sharp triangles break spot elevation", "void on TIN gives extra faces", "no quantities for earthworks" | 16 site + ~4 quantity records; en, 1 ru synthetic | Terrain is an open triangulated surface; booleans differ per kernel; auto-Qto not implemented for earthworks | Clean the TIN, use manual `Qto_Earthworks*`, state method |
| 11 | National requirements and IDS for infrastructure | "which MMI code per milestone", "BIM Basis Infra ILS", "VA detail model guidelines", "check export against client's IDS" | ~12 records; no, nl, ru, en | Requirements live in national guides and IDS files, not in IFC | Ask for the requirement document; check against IDS; never guess |
| 12 | Version expectations: tunnels, downgrades, sample files | "does 4.3 have tunnels?", "how to downgrade 4.3 to IFC4?", "where are test bridges?" | ~10 records; en, no, es, it, ja | 4.3 has no complete tunnel domain; no official downgrade mapping; sample files scattered | Say what is absent; offer closest supertype/proxy; point to official samples |

---

## Problems in depth

### 1. The alignment is in the file but the tool shows nothing

**What users say**
- en: "[Bug]: Can not display Alignments... the civil release has been around for some time, I suppose the library should at least read Alignments correctly." [web-ifc #878](https://github.com/ThatOpen/engine_web-ifc/issues/878)
- en: "Civil - can't read alignment: I tried 3 files with alignment but the property Civil inside fragmentgroup is empty." [web-ifc #926](https://github.com/ThatOpen/engine_web-ifc/issues/926)
- en: "Alignment error at Civil 3D exported IFC file: cannot destructure property x of undefined" (fixed by maintainers). [engine_fragment #158](https://github.com/ThatOpen/engine_fragment/issues/158)
- en: "[Error] IfcGradientCurve Not Implemented" when converting a rail alignment-with-cant sample. [IfcOpenShell #3098](https://github.com/IfcOpenShell/IfcOpenShell/issues/3098)
- en: "IFCALIGNMENT child elements not included in getSpatialStructure() result" (visible in BIMvision, absent in the library; fixed on main). [engine_components #743](https://github.com/ThatOpen/engine_components/issues/743)
- zh: 道路BIM必须先模型后剖面吗？——IFC标准打脸啦！(EN: must road BIM go model first, then sections? The IFC alignment standard says otherwise). [Zhihu](https://zhuanlan.zhihu.com/p/71839267)
- en (synthetic): "IFC4.3-filen fra Civil 3D viser ikke aksen i viewer, ligger den i filen?" (no).

**Why it happens.** An `IfcAlignment` holds nested layouts (horizontal, vertical, cant) built from segments (line, circular arc, clothoid; constant gradient, parabolic arc...), and the 3D curve is derived through `IfcGradientCurve` / segmented reference curves. Libraries have implemented these in stages (IfcOpenShell lists spirals, gradient curves, cant and sweeps as separate work items). Files from different exporters hit different bugs (a Revit-origin alignment loaded in one web-ifc version but not in the fragments loader, [web-ifc #864](https://github.com/ThatOpen/engine_web-ifc/issues/864)), and the withdrawn IFC 4.1 produced alignments some importers ignore: "IFC 4x1 file containing alignment is not opening in Civil 3D" was answered with "4.1 was withdrawn and never certified; ask the vendor for IFC4.3" ([bSI forum](https://forums.buildingsmart.org/t/ifc-4x1-file-containing-alignment-is-not-opening-in-civil-3d/3830)). In Civil 3D, IFC 4.3 export is delivered as an extension (command `IFCINFRAEXPORTSELECTED`, mapping files), and an older corridor export produced only TIN surfaces and 3D solids ([Dynamo forum](https://forum.dynamobim.com/t/exporting-ifc-from-civil-3d-with-dynamo/114735), [corridor thread](https://forum.dynamobim.com/t/export-corridor-to-ifc/59548)).

**What fixes it.** Confirm the file schema (`IFC4X3_ADD2`), confirm `IfcAlignment` exists with nested horizontal/vertical layouts and a representation, then try a library build that implements the curve types. For viewing, the Alignment-based Reference View is described in the 4.3 docs although its official MVD status was "pending" in the cited thread ([bSI forum](https://forums.buildingsmart.org/t/alignment-based-reference-view/6414)).

**What a good assistant should do.** Distinguish four answers: no `IfcAlignment` in the file; alignment present with layouts but no geometry representation; alignment present with representation but this tool cannot display it; alignment present and displayable. List per alignment: name, presence of horizontal and vertical layouts, segment counts, whether an `Axis` or `FootPrint` representation exists, referents with stations. Never fabricate a polyline from the surrounding meshes.
**Clarifying questions:** Which program exported it (Civil 3D, OpenRoads, Tekla, Bonsai)? Which IFC schema is in the header? Is the alignment needed for display, for stationing, or for placing objects?

### 2. Georeferencing: the model lands in the ocean

**What users say**
- en: "I export from Revit to IFC4, checked the coordinates in IfcSite, but the model appears in the middle of the ocean." [Cesium forum](https://community.cesium.com/t/right-way-to-georeferencing-file-on-cesium/47030)
- en: "Which properties in IFC does ion use to geo-reference? Uploaded three times with no EPSG, 4326, 2056; correct coordinates are in IFCSITE." (Answer: the tiler uses the UI CRS or `IFCPROJECTEDCRS`, not `IFCSITE`.) [Cesium forum](https://community.cesium.com/t/ifc-properties-for-geo-referencing-in-cesium-ion/43003)
- en: "Model georeferenced to EPSG:27700 in Bonsai lands in the ocean in QGIS after converting to GeoPackage." (Unit mismatch mm vs m and a web-ifc bug ignoring IfcMapConversion; both fixed in newer versions.) [OSArch](https://community.osarch.org/discussion/3037/ifc-to-qgis-geopackage)
- en: "Model origin 51.9026, 4.4539; after BlenderGIS map generation my XY moved; I cannot reconcile EPSG:28992, WGS84 and the calculated value." [OSArch](https://community.osarch.org/discussion/comment/27629#Comment_27629)
- nl: «GEO Coordinatiepunt en BIM nulpunt los gedefinieerd, maar samen beschrijven ze dezelfde transformatie als IfcMapConversion» (EN: the GEO coordination point and BIM origin together describe the same transformation as IfcMapConversion). [digiGO GeoBIM](https://github.com/nl-digigo/GeoBIM_Georefereren/issues/5)
- zh: BIM模型到3Dtiles转换后精确定位工作流及存在的问题 (EN: positioning after BIM to 3D Tiles needs origin lat/lon plus rotation, and the origin is not at the model centre). [CSDN](https://blog.csdn.net/liyan_gis/article/details/100132931)

**Why it happens.** `IfcMapConversion` converts local coordinates to map coordinates by scale, then rotation, then translation (Eastings, Northings, OrthogonalHeight), and `Scale` must be given when the project unit differs from the map unit (e.g. mm to m = 0.001). `IfcSite` latitude/longitude is only an approximate legacy mechanism and should not be used for georeferencing if a map conversion exists. Tools disagree on which one they read. Model-in-ocean checks and the LoGeoRef 10 to 50 grading are detailed in the [coordinates doc](../../01_ifc_basics/06_geometry_placement_coordinates_units.md); the Revit "Coordinate Base" options (Project Base Point, Survey Point, Shared Coordinates, Internal Origin) decide what the exporter writes.

**What fixes it.** Read `IfcMapConversion`, `IfcProjectedCRS` (Name should carry a single EPSG code), project length unit and Scale; compute where a known point should land; fix units or Scale; tell the tiler/viewer the CRS explicitly. A combined horizontal+vertical pair (e.g. UTM 32N plus EVRF2007) has no single EPSG entry; the forum answer is to put the combined pair in the name as CityGML does ([bSI forum](https://forums.buildingsmart.org/t/ifcprojectedcrs-epsg-code-not-known/972)).

**What a good assistant should do.** Report which of the three georeferencing mechanisms exist (IfcMapConversion + ProjectedCRS, IfcSite lat/long, nothing), the units, the bounding-box distance from origin, and a plausibility verdict ("eastings of 530268 with a mm project and scale 1 will be 1000x off"). Do not assume an EPSG code from a country name. If asked to place the model, ask for CRS, true north/rotation, elevation datum and base point before writing anything.
**Clarifying questions:** Which target tool (Cesium ion, QGIS, ArcGIS)? Which CRS and vertical datum are expected? Is the project in mm or m? Is there a survey point to check against?

### 3. IFC 4.3 file does not open: schema identifier and versions

**What users say**
- en: "ifcopenshell.SchemaError: Unsupported schema: IFC4X3... I try to open an IFC4x3 file." (Schema identifier must be `IFC4X3_ADD2`; compiled schemas differ by build.) [IfcOpenShell #6886](https://github.com/IfcOpenShell/IfcOpenShell/issues/6886)
- en: "schema_by_name IFC4x3 throws No schema named" (identifier is case-sensitive: `IFC4X3`; conda-forge build works). [IfcOpenShell #2382](https://github.com/IfcOpenShell/IfcOpenShell/issues/2382)
- en: "Link / Import IFC 4x3 Revit 2024: files with the official IFC4X3_ADD2 header error on link or import." [revit-ifc #928](https://github.com/Autodesk/revit-ifc/issues/928)
- en: "Unable to open IFC 4x3 add2" in a web viewer (support added in later releases). [web-ifc #1171](https://github.com/ThatOpen/engine_web-ifc/issues/1171)
- en: "Web IfcTester errors when loading a Bonsai-made IFC 4.3 ADD2 file though IDS testing works inside Bonsai." [OSArch](https://community.osarch.org/discussion/3308/solved-ifctester-ifc-4-3-add2-support-question)

**Why it happens.** There is more than one 4.3 identifier in circulation (`IFC4X3`, `IFC4X3_ADD2` and older development identifiers; ADD2 is the one the cited threads treat as current); software ships a fixed set of compiled schemas; Revit 2024's link code fails on the ADD2 header (changing the header to `IFC4X3` was reported to work; internal ticket open, per the [import reference](../../03_software/revit/ifc_import_link_reference.md)). IFC 4.1 and 4.2 are withdrawn editions and not interchangeable with 4.3.

**What a good assistant should do.** Read `FILE_SCHEMA` first and quote it. Say whether the problem is the file or the reader. Header editing is a temporary workaround and does not make a file conformant. Do not claim "invalid IFC" without running a validator.
**Clarifying questions:** What is the exact error text and software version? Which program wrote the file? May I make a copy with a patched header?

### 4. Proxies instead of roads, bridges, pavements; wrong hierarchy

**What users say**
- en: "How can I introduce IfcRoad and related classes instead of painful BuildingElementProxy to my IFC model? Upgrade gives a python error." [IfcOpenShell #4921](https://github.com/IfcOpenShell/IfcOpenShell/issues/4921)
- en: "Exporting bridge elements to IFC 4.3: IfcBridge or IfcRoad? Should wearing surface, kerbs, junction boxes go inside the IfcBridge?" (Answer: everything between approach slabs is bridge except the asphalt wearing course which is road pavement; kerbs, footpaths, drains, barriers are usually bridge.) [bSI forum](https://forums.buildingsmart.org/t/exporting-bridge-elements-to-ifc-4-3-ifcbridge-or-ifcroad/5811)
- en: "Revit IFC 4.3 export places elements under Building domain so infrastructure domains can't filter." (Revit 2025 added facility-type assignment.) [bSI forum](https://forums.buildingsmart.org/t/bsdd-buildingsmart-data-dictionary-and-classification-of-ifc-4x3-domain-mapping/4854)
- en: "openings in IfcSpatialElement: wants voids in an IfcBridgePart" (a bridge part is a spatial decomposition, not a physical element). [bSI forum](https://forums.buildingsmart.org/t/4425)
- en: "Unable to assign ifc railway part as it gets automatically updated to IfcSpace." [IfcOpenShell #6888](https://github.com/IfcOpenShell/IfcOpenShell/issues/6888)
- de: IFC Struktur – IfcProject, IfcSite, IfcFacility: Revit exports only one IfcSite and IfcBuilding; how to get multiple sites? [BIM me up](https://bim-me-up.com/ifc-struktur/)

**Why it happens.** Authoring tools map their categories to building classes by default; infrastructure classes (`IfcRoad`, `IfcPavement`, `IfcCourse`, `IfcKerb`, `IfcBridgePart`...) need an explicit mapping. Hierarchy conventions (nested bridge parts, US bridge proposals) are not yet uniform, and Bonsai's spatial panel was built for buildings.

**What a good assistant should do.** Count proxies by name/ObjectType and propose 4.3 classes **as proposals with reasons**; on a write request, show the mapping first, require confirmation, upgrade the schema if the file is IFC4, preserve GlobalIds, and report counts changed.
**Clarifying questions:** Is the target a specific convention (AASHTO-style bridge parts, a national guide)? Should name matching be used (it is a guess)? Is the file IFC4 or already 4.3?

### 5. IFC to CityGML, 3D Tiles and other GIS formats

**What users say**
- en: "How to convert geometry from ifc to citygml: when ifcopenshell.geom converts the geometry the CityGML shapes come out very broken. Do I need to load all ifc objects?" [IfcOpenShell #5279](https://github.com/IfcOpenShell/IfcOpenShell/issues/5279)
- en: "Tried converting AC20-FZK-Haus.ifc to 3D Tiles... 'Finished loading 0 files'" (the Assimp library used does not fully support IFC4). [mago-3d-tiler #79](https://github.com/Gaia3D/mago-3d-tiler/issues/79)
- en: "Cityjson into ifc: I work with CityJSON in the Netherlands and also 3D .shp files. How do I convert city models to IFC?" (no replies). [bSI forum](https://forums.buildingsmart.org/t/cityjson-into-ifc/)
- ja: _PLATEAU_のCityGMLをArcGISで表示する (EN: displaying PLATEAU CityGML in ArcGIS through a conversion workspace). [Qiita](https://qiita.com/masumur/items/8362a1ed91048e26ed2a)
- de: KITModelViewer: IFC export to GML works but reimport fails with "ungültige Daten auf Stammebene" (malformed header comment; maintainers confirmed). [KIT-IAI #13](https://github.com/KIT-IAI/SDM_KITModelViewer/issues/13)
- zh: 如何将Revit格式的BIM数据导入GIS平台？ (EN: how to import Revit BIM data into a GIS platform). [Zhihu](https://zhuanlan.zhihu.com/p/388012269)

**Why it happens.** IFC to CityGML is lossy by design (only the envelope and a chosen LoD survive; the reverse direction loses detail). Converters depend on libraries with partial IFC4 support, and without a correct CRS the result lands in the wrong place.

**What a good assistant should do.** State which parts survive (envelope, storey count as an attribute, selected psets) and which do not, ask for the LoD, and produce a *light copy* by filtering classes while keeping GlobalIds and pset names. Check georeferencing before conversion.
**Clarifying questions:** Which LoD (LoD1 block, LoD2 roof and walls)? Do you need properties carried over? Which CRS and target (Cesium ion, ArcGIS, CityGML)? Is a one-off acceptable or a repeatable pipeline needed?

### 6. Complex geometry: sectioned solids, sweeps, cant

**What users say**
- en: "IfcSectionedSolidHorizontal doesn't account for orientation of section... bridge with girder ends skewed at 45 degrees." [IfcOpenShell #6386](https://github.com/IfcOpenShell/IfcOpenShell/issues/6386)
- en: "IfcSectionedSurface isn't rendered correctly because of IfcAxis2PlacementLinear: twist due to cant is not considered." [IfcOpenShell #8116](https://github.com/IfcOpenShell/IfcOpenShell/issues/8116)
- en: "IFC to gltf of IfcFixedReferenceSweptAreaSolid with IfcGradientCurve directrix gives unexpected geometry, fine in DESITE or BIMcollab." [IfcOpenShell #5502](https://github.com/IfcOpenShell/IfcOpenShell/issues/5502)
- en: "IFC4X3: IfcSurfaceCurveSweptAreaSolid gets no geometry when StartParam/EndParam are written as IFCPARAMETERVALUE(...)" (fixed in the parser). [web-ifc #2247](https://github.com/ThatOpen/engine_web-ifc/issues/2247)
- en: "IfcSectionedSolidHorizontal caps added twice in 0.9.0: wrong volume, stray internal cap." [IfcOpenShell #9820](https://github.com/IfcOpenShell/IfcOpenShell/issues/9820)

**Why it happens.** These solids are defined along a curve with a sequence of cross-sections; the spec's frame rules are subtle, viewers disagree, and bugs appear as regressions between versions.

**What a good assistant should do.** Report which representation types the elements use (count of `IfcSectionedSolidHorizontal`, `IfcFixedReferenceSweptAreaSolid`...), say when a visual or volume problem is likely a kernel limitation, and recommend checking in a second viewer. Warn that volumes computed by a kernel with a known cap bug may be wrong.
**Clarifying questions:** Which viewer or converter shows the wrong geometry? Do other viewers display it correctly? Is the quantity from the file or recomputed?

### 7. Energy analysis handoff: space boundaries and thermal data

Evidence is thin (12 real records, all English). The facts below are what they say plus the reference docs.

**What users say**
- en: "Export IfcRelSpaceBoundary / Room boundaries: about 1000 models for thermal simulation; boundaries only the four walls." (Answer: set the Energy Settings phase to match walls and spaces; test manually before automation.) [Dynamo forum](https://forum.dynamobim.com/t/export-ifcrelspaceboundary-room-boundaries/91608)
- en: "2nd Level Space Boundary ConnectionGeometry displaced from corresponding IfcSpace: shifted several metres in XY, breaking BEM workflows." [revit-ifc #961](https://github.com/Autodesk/revit-ifc/issues/961)
- en: "Level1 boundary generation to the centre line or inside face? Told centreline needed for EnergyPlus/CIBSE but boundary areas then exceed true surface area." (Answer: depends on regulation.) [bSI forum](https://forums.buildingsmart.org/t/level1-boundary-generation-to-the-centre-line-or-inside-face/2724)
- en: "invalid Virtual boundary between 2 Walls of different thickness". [revit-ifc #243](https://github.com/Autodesk/revit-ifc/issues/243)
- en: "IfcMaterial Properties for IFC2x3: material thermal properties unsupported in viewers except FZK" (maintainer declined). [IfcOpenShell #2433](https://github.com/IfcOpenShell/IfcOpenShell/issues/2433)
- en: "Revit exports similar walls inconsistently as IfcWall or IfcWallStandardCase; layer data missing for thermal analysis." [bSI forum](https://forums.buildingsmart.org/t/difference-between-expectations-and-reality-of-ifc-standards/1040)

**Why it happens.** Space boundaries are optional in the Revit export (setting None / 1st level / 2nd level; default None, per the [export reference](../../03_software/revit/ifc_export_reference.md)); they depend on room-bounding flags and phases; first-level vs second-level semantics differ; thermal material properties are not a default part of exports. gbXML is a separate energy-analysis format and is not IFC (see [IFC versions and formats](../../01_ifc_basics/01_what_is_ifc_and_versions.md)).

**What a good assistant should do.** Check whether `IfcRelSpaceBoundary` (1st/2nd level) exists, count per space, flag spaces with none, check whether spaces are closed volumes; say plainly that gbXML export or U-values are outside what an IFC reader can produce unless material layers and thermal properties exist. Do not invent U-values.
**Clarifying questions:** Which energy tool is the target (EnergyPlus, IES, IDA, a regulator's method)? Centre-line or inside-face boundaries? Do you need an IFC for the analysis or a gbXML from the authoring tool?

### 8. Stations (chainage) versus DistanceAlong; linear placement

**What users say**
- en: "StartDistAlong in IfcAlignmentHorizontal 4.3 rc2: the attribute is missing in the final 4.3.2.0; need curvilinear abscissa, not Cartesian StartPoint." (Answer: use an `IfcReferent` of type STATION with `Pset_Stationing`.) [bSI forum](https://forums.buildingsmart.org/t/startdistalong-in-ifcalignmenthorizontal-4-3-rc2/5118)
- en: "New alignment and need for stations and offsets: IfcLinearPlacement with StartDistAlong=500 put an object at 1500 ft instead of station 15+00." (Answer: distance along is geometric; with a 5+00 start, station 15+00 is distance 1000.) [bSI forum](https://forums.buildingsmart.org/t/new-alignment-and-need-for-stations-and-offsets/3330)
- en: "IfcLinearPlacement of signal shows signal at origin." [IfcOpenShell #5049](https://github.com/IfcOpenShell/IfcOpenShell/issues/5049)
- en: "Grid and linear placement from Python: only local placement is implemented in util.placement." [IfcOpenShell #4556](https://github.com/IfcOpenShell/IfcOpenShell/issues/4556)
- en: "alignment: transition point referents (P.C., P.T., P.V.C.) are no longer created" (intentionally dropped; the spec is unclear). [IfcOpenShell #9121](https://github.com/IfcOpenShell/IfcOpenShell/issues/9121)

**What a good assistant should do.** Always separate *distance along the curve* from *station label*; read start station from referents or `Pset_Stationing` and say if absent; for each element with a linear placement report base curve, DistanceAlong and offsets, flagging when the importer in use cannot resolve them to XYZ. Mind the unit (feet vs metres).
**Clarifying questions:** What station does the alignment start at? Are stations in feet or metres? Do you want the station label or the raw distance?

### 9. Digital twins: sensors, asset IDs, searchable properties

**What users say**
- en: "ifcTimeSeries in blenderBim? Should sensor data be stored directly in the BIM model or should I just link data?" (No UI for IfcTimeSeries; one day of `Pset_SensorHistory` made a <100 MB file that crashed viewers.) [OSArch](https://community.osarch.org/discussion/comment/14415#Comment_14415)
- en: "Using IFC models for asset management: a US state DOT with 500+ projects/year wants a system-wide asset query." (Answer: file-based will not scale; database/GIS hybrid with psets mapped to tables.) [OSArch](https://community.osarch.org/discussion/comment/25545)
- en: "Operation and maintenance on campus/site with IFC: which IFC entity assigns a unique code to each piece of equipment?" [OSArch](https://community.osarch.org/discussion/1118/operation-and-maintenance-on-campus-site-with-ifc)
- en: "IFC metadata searchable in English but not in Korean" (Cesium ion; investigated). [Cesium forum](https://community.cesium.com/t/ifc-metadata-not-shown-when-it-is-korean/44612)
- en: "Can't retrieve IFC properties and attributes: scene.pick shows nothing; keys combine pset and property name." [Cesium forum](https://community.cesium.com/t/cant-retrieve-ifc-properties-and-attributes/40009)
- zh: 2025 广州市自主可控BIM应用与发展白皮书 (EN: Guangzhou white paper; models flow into the CIM platform after review and a drawing-model alignment check blocks noncompliant uploads). [Guangzhou gov](https://zfcj.gz.gov.cn/attachment/7/7943/7943479/10589336.pdf)

**What a good assistant should do.** Keep identifiers (tags, sensor IDs) in a property set and link time series externally; match a spreadsheet of IDs against `Tag` and every pset and report unmatched IDs; avoid putting thousands of readings into the file; for non-ASCII text, verify how strings are escaped before blaming the viewer.
**Clarifying questions:** Which system consumes the IDs (CMMS, Cesium, a database)? Which ID is authoritative? Is the data static (asset IDs) or streaming (sensor values)?

### 10. Terrain, site objects and earthworks

**What users say**
- en: "Revit Slab to IfcSite does not work with modified points." [revit-ifc #505](https://github.com/Autodesk/revit-ifc/issues/505)
- en: "IFCs with 'sharp' triangulated faces cannot have spot elevations or spot coordinates" (terrain TINs from 12d). [revit-ifc #511](https://github.com/Autodesk/revit-ifc/issues/511)
- en: "[geom] Void on open IfcTriangulatedFaceSet (TIN terrain) with IfcEarthworksCut: extra faces of the opening body." [IfcOpenShell #10076](https://github.com/IfcOpenShell/IfcOpenShell/issues/10076)
- en: "wants to use IfcEarthworks elements but automatic quantity take-off returns nothing" (use manual `Qto_EarthworksFillBaseQuantities`). [IfcOpenShell #6325](https://github.com/IfcOpenShell/IfcOpenShell/issues/6325)
- en: "Qto: UndisturbedVolume for IfcEarthworksCut returns the volume of the subtraction solid, not the excavated volume" (fixed). [IfcOpenShell #9376](https://github.com/IfcOpenShell/IfcOpenShell/issues/9376)
- en: "ifc-sg-site-object-repair: site coverage and site boundary came out as IfcSpace, IFC+SG wants IfcGeographicElement." [GitHub](https://github.com/noddlesskcho/ifc-sg-site-object-repair)
- en: "Show gradients steeper than 1:21" (title only). [Dynamo forum](https://forum.dynamobim.com/t/show-gradients-steeper-than-1-21/115245)

**Why it happens.** Terrain is an open triangulated surface (`Closed = .F.`); boolean subtraction on open surfaces behaves differently per kernel; elevation conventions changed between Revit versions ([revit-ifc #581](https://github.com/Autodesk/revit-ifc/issues/581)); quantity sets for earthworks are not automatic.

**What a good assistant should do.** Find terrain representations and `IfcEarthworks*` elements; report quantities only if present or computed, naming the method; say when a volume is unreliable because the surface is open. Never report "cut/fill" without a stated reference surface.
**Clarifying questions:** Which surface is existing ground and which is design? Do you want values from the file's Qto or recomputed? What slope convention (1:21 = about 4.8 percent)?

### 11. National requirements, IDS and guidelines for infrastructure

**What users say**
- no: «hvilken MMI-kode skal objektene ha i modellen ved hver milepæl?» (EN: which model maturity code should objects have at each milestone). [MMI-veilederen](https://www.mmi-veilederen.no/)
- no: «hvordan skal kummer, rør og rørdeler modelleres i IFC 4.3 for VA?» [buildingSMART Norge](https://www.buildingsmart.no/standarder/publikasjoner-og-veiledninger.html)
- nl: «Werkpakket B BIM Basis Infra Stedelijk Spoor: te beschrijven wat het probleem is» (EN: describe problem and goal for BIM Basis Infra, urban rail based on ILS). [digiGO NLCS #189](https://github.com/nl-digigo/NLCS/issues/189)
- ru: «Мособлэкспертиза в IDS: новые BIM-требования в формате IDS» (EN: Mosoblexpertiza published BIM requirements in IDS format for roads, utilities and buildings). [Telegram](https://t.me/s/ifc_ru)
- en: "Check the IFC export against a client's IDS... clients send one more and more often." [Open-Infra-Studio #65](https://github.com/OpenAEC-Foundation/Open-Infra-Studio/issues/65)
- en: "Enforcing required PredefinedType values when they are a mix of standard and user-defined." [IDS #447](https://github.com/buildingSMART/IDS/issues/447)

**What a good assistant should do.** Ask for the requirement document or IDS file; check class, attribute, property, classification, material and part-of facets; report per element what is missing; refuse to substitute its own rules. See [national: Nordics](../../02_standards_regulations/national/nordics_baltics.md), [Netherlands/Belgium](../../02_standards_regulations/national/netherlands_belgium_luxembourg.md), [Russia](../../02_standards_regulations/national/russia.md), [buildingSMART standards](../../02_standards_regulations/buildingsmart_standards.md).
**Clarifying questions:** Which requirement set applies (EIR, IDS, national guide, regulator)? At which milestone? Is the check pass/fail or an itemised list?

### 12. Version expectations: tunnels, downgrade, sample files

**What users say**
- en: "Guidelines for Ifc4x3 (add2) exports to Ifc2x3 (tc1) and Ifc4 (add2 tc1)? IfcConveyorSegment to IfcFlowSegment? IfcBridge parts to IfcSite? geotechnical classes dropped?" (No official downgrade mapping; use closest supertype or proxy.) [bSI forum](https://forums.buildingsmart.org/t/5133)
- en: "Looking for new IFC 4X2/3 bridge file examples to test our IFC reading tools." [bSI forum](https://forums.buildingsmart.org/t/new-ifc-4x2-3-bridge-file-examples/5218)
- no: «hvilke IFC-versjoner brukes i prosjekter nå, og hva er nytt i IFC4.3?» (answer: 4.3 adds bridges, roads, rail, waterways, harbours and coordinate transformation; tunnels expected in 4.4). [buildingSMART Norge](https://www.buildingsmart.no/standarder/kort-forklart.html)
- it: IFC 4.3 cosa cambia per strade e ferrovie? i software lo supportano? [Biblus](https://biblus.acca.it/ifc-4-3-approvato-come-standard-finale/)
- en: "INQ: Ifc4x3 official release: exporter supporting Quantity Sets" (Autodesk: 4.3 less stable than 2x3/IFC4 for now). [revit-ifc #768](https://github.com/Autodesk/revit-ifc/issues/768)

**What a good assistant should do.** Say that tunnel classes are not a complete part of IFC 4.3 (the synthetic prompt "list the IfcTunnel parts" is a trap), check what the file actually contains, and warn that downgrade has no official mapping so any class change is a choice to be confirmed.
**Clarifying questions:** Which schema does the receiver accept? May unsupported classes become proxies or the nearest supertype? Who keeps the original?

---

## Real questions

Paraphrases from the linked sources. "Persona" is the role inferred by the research pass.

| lang | Question (original-language paraphrase) | EN gloss | Persona | Source |
|---|---|---|---|---|
| en | Files with the official IFC4X3_ADD2 header error on link or import in Revit 2024; I traced it to the header schema name. | — | civil_infra_engineer | [revit-ifc #928](https://github.com/Autodesk/revit-ifc/issues/928) |
| en | I try to open an IFC4x3 file with ifcopenshell python but get that IFC4x3 is not supported. | — | developer_programmer | [IfcOpenShell #6886](https://github.com/IfcOpenShell/IfcOpenShell/issues/6886) |
| en | On the latest version we are unable to open IFC 4x3 add2 (zip attached). | — | civil_infra_engineer | [web-ifc #1171](https://github.com/ThatOpen/engine_web-ifc/issues/1171) |
| en | Highway alignment exported as IFC 4x1 imports into Civil 3D 2022 but nothing shows, even on zoom extents. | — | civil_infra_engineer | [bSI forum](https://forums.buildingsmart.org/t/ifc-4x1-file-containing-alignment-is-not-opening-in-civil-3d/3830) |
| en | Web IfcTester errors on a Bonsai-made IFC 4.3 ADD2 file though IDS testing works inside Bonsai; is ADD2 supported? | — | bim_coordinator | [OSArch](https://community.osarch.org/discussion/3308/solved-ifctester-ifc-4-3-add2-support-question) |
| en | Helping a thesis: how do I place railway elements along an alignment and read or create an IfcAlignment? | — | student_beginner | [bSI forum](https://forums.buildingsmart.org/t/understanding-ifc-alignment-and-rail-beginners-guide/4117) |
| en | Many IFC files with alignments fail to display; the model properties are empty arrays of curves. | — | developer_programmer | [web-ifc #878](https://github.com/ThatOpen/engine_web-ifc/issues/878) |
| en | I export IFC with alignment from Civil 3D 2026 and get "cannot destructure property x of undefined". | — | civil_infra_engineer | [engine_fragment #158](https://github.com/ThatOpen/engine_fragment/issues/158) |
| en | Not implemented IfcCurveSegment, failed to convert IfcGradientCurve in my test file. | — | developer_programmer | [IfcOpenShell #3098](https://github.com/IfcOpenShell/IfcOpenShell/issues/3098) |
| en | StartDistAlong (start chainage) is missing in final 4.3.2.0; I need curvilinear abscissa. | — | civil_infra_engineer | [bSI forum](https://forums.buildingsmart.org/t/startdistalong-in-ifcalignmenthorizontal-4-3-rc2/5118) |
| en | US road work uses station/offset; IfcLinearPlacement with StartDistAlong=500 put the object at 1500 ft instead of station 15+00. | — | civil_infra_engineer | [bSI forum](https://forums.buildingsmart.org/t/new-alignment-and-need-for-stations-and-offsets/3330) |
| en | A signal with IfcLinearPlacement shows at the origin; is the 4x4 matrix transposed? | — | developer_programmer | [IfcOpenShell #5049](https://github.com/IfcOpenShell/IfcOpenShell/issues/5049) |
| en | Alignment transition point referents (P.C., P.T., P.V.C.) are no longer created. | — | civil_infra_engineer | [IfcOpenShell #9121](https://github.com/IfcOpenShell/IfcOpenShell/issues/9121) |
| en | The cross-section twist due to cant is not considered when lofting an IfcSectionedSurface. | — | civil_infra_engineer | [IfcOpenShell #8116](https://github.com/IfcOpenShell/IfcOpenShell/issues/8116) |
| en | An example bridge with girder ends skewed at 45 degrees; IfcSectionedSolidHorizontal ignores the section orientation. | — | structural_engineer | [IfcOpenShell #6386](https://github.com/IfcOpenShell/IfcOpenShell/issues/6386) |
| en | IfcSurfaceCurveSweptAreaSolid gets no geometry when StartParam/EndParam use typed values. | — | developer_programmer | [web-ifc #2247](https://github.com/ThatOpen/engine_web-ifc/issues/2247) |
| en | Should wearing surface, kerbs and junction boxes go inside the IfcBridge or in a separate IfcRoad model? | — | civil_infra_engineer | [bSI forum](https://forums.buildingsmart.org/t/exporting-bridge-elements-to-ifc-4-3-ifcbridge-or-ifcroad/5811) |
| en | I want voids in an IfcBridgePart but IfcRelVoidsElement requires an IfcElement; should I use CSG? | — | civil_infra_engineer | [bSI forum](https://forums.buildingsmart.org/t/4425) |
| en | Which IFC classes for unitary precast culvert sections? | — | civil_infra_engineer | [bSI forum](https://forums.buildingsmart.org/t/6078) |
| en | Is there an example that generates an IfcRoad via IfcOpenShell, like the wall example, with two points and a straight line? | — | developer_programmer | [IfcOpenShell #3464](https://github.com/IfcOpenShell/IfcOpenShell/issues/3464) |
| en | How can I get IfcRoad and related classes instead of painful BuildingElementProxy? The upgrade gives a python error. | — | civil_infra_engineer | [IfcOpenShell #4921](https://github.com/IfcOpenShell/IfcOpenShell/issues/4921) |
| en | I include IfcRail and IfcRailPart but the entities appear as spaces, not things. | — | civil_infra_engineer | [IfcOpenShell #6888](https://github.com/IfcOpenShell/IfcOpenShell/issues/6888) |
| en | How to downgrade 4.3 classes: IfcConveyorSegment to IfcFlowSegment, bridge parts to IfcSite, tendon conduits to proxy? | — | developer_programmer | [bSI forum](https://forums.buildingsmart.org/t/5133) |
| en | Revit IFC 4.3 export places elements under Building so infrastructure domains can't filter. | — | civil_infra_engineer | [bSI forum](https://forums.buildingsmart.org/t/bsdd-buildingsmart-data-dictionary-and-classification-of-ifc-4x3-domain-mapping/4854) |
| en | Exporting many surfaces to IFC from Civil 3D with Dynamo. | — | civil_infra_engineer | [Dynamo forum](https://forum.dynamobim.com/t/exporting-ifc-from-civil-3d-with-dynamo/114735) |
| en | I want IfcEarthworks elements but automatic quantity take-off returns nothing; is IFC4x3 unsupported? | — | civil_infra_engineer | [IfcOpenShell #6325](https://github.com/IfcOpenShell/IfcOpenShell/issues/6325) |
| en | UndisturbedVolume for IfcEarthworksCut returns the subtraction solid, not the excavated volume. | — | civil_infra_engineer | [IfcOpenShell #9376](https://github.com/IfcOpenShell/IfcOpenShell/issues/9376) |
| en | I want a structural clearance for a road from its alignment (copy alignment 4x with offsets) and clash it against structures. | — | student_beginner | [IfcOpenShell #5471](https://github.com/IfcOpenShell/IfcOpenShell/issues/5471) |
| en | Where are IFC4.3 bridge samples to test our reader? I already tried ifcinfra.de. | — | developer_programmer | [bSI forum](https://forums.buildingsmart.org/t/new-ifc-4x2-3-bridge-file-examples/5218) |
| en | Is the Alignment-based Reference View published, and can I implement it before final sign-off? | — | developer_programmer | [bSI forum](https://forums.buildingsmart.org/t/alignment-based-reference-view/6414) |
| no | Hvilke IFC-versjoner brukes i prosjekter nå, og hva er nytt i IFC4.3? | Which IFC versions are used in Norwegian projects now, and what does 4.3 add? | student_beginner | [buildingSMART Norge](https://www.buildingsmart.no/standarder/kort-forklart.html) |
| no | Hvordan skal kummer, rør og rørdeler modelleres i IFC 4.3 for VA? | How should manholes, pipes and fittings be modelled in IFC 4.3 for water and wastewater? | civil_infra_engineer | [buildingSMART Norge](https://www.buildingsmart.no/standarder/publikasjoner-og-veiledninger.html) |
| no | Hvilken MMI-kode skal objektene ha i modellen ved hver milepæl? | Which maturity code should model objects have at each milestone? | owner_client | [MMI-veilederen](https://www.mmi-veilederen.no/) |
| no | Finnes det et fagmiljø for IFC i veg og bane? | Is there a professional community for IFC in road and rail? | civil_infra_engineer | [buildingSMART Norge](https://www.buildingsmart.no/fagnettverk/infradomene.html) |
| nl | Voor uitwisseling van 3D BIM-modellen is een classificatie nodig zoals NL-sfb; onderzoek hoe NLCS aligned kan worden met IFC 4.3, evt via bSDD. | Research how NLCS can align with IFC 4.3, possibly via bSDD. | developer_programmer | [digiGO NLCS #147](https://github.com/nl-digigo/NLCS/issues/147) |
| nl | Werkpakket B BIM Basis Infra Stedelijk Spoor: te beschrijven wat het probleem is en wat we willen bereiken. | Describe problem and goal for BIM Basis Infra / urban rail based on BIM basis ILS. | bim_manager | [digiGO NLCS #189](https://github.com/nl-digigo/NLCS/issues/189) |
| nl | GEO Coordinatiepunt en BIM nulpunt zijn los gedefinieerd, maar samen beschrijven ze dezelfde transformatie als IfcMapConversion. | The GEO coordination point and BIM origin together equal IfcMapConversion. | bim_manager | [digiGO GeoBIM #5](https://github.com/nl-digigo/GeoBIM_Georefereren/issues/5) |
| ru | новые BIM-требования в формате IDS (Мособлэкспертиза: дороги, коммуникации, здания) | Mosoblexpertiza published new BIM requirements in IDS format. | reviewer_authority | [Telegram](https://t.me/s/ifc_ru) |
| zh | 道路BIM必须先模型后剖面吗？——IFC标准打脸啦！ | Must road BIM go model first, then sections? The IFC alignment standard says otherwise. | civil_infra_engineer | [Zhihu](https://zhuanlan.zhihu.com/p/71839267) |
| zh | BIMSee免费IFC浏览器，支持大文件（IFC2x3、IFC4.x，含桥梁、铁路） | BIMSee free IFC browser, IFC2x3 and IFC4.x incl. 4.2 bridges and 4.3 rail. | developer_programmer | [Zhihu](https://zhuanlan.zhihu.com/p/602546350) |
| ja | 初のIFC勉強会に参加。IFC4.3で土木にも広がる。 | Attended the first IFC study session; IFC4.3 extends to civil engineering. | student_beginner | [Qiita](https://qiita.com/ktaroabobon/items/25349c7fa7bdb55c63b8) |
| es | Artículo de Planbim sobre IFC y sus actualizaciones IFC 4.3 e IFC 4.4. | Planbim article on IFC and its 4.3 and 4.4 updates. | bim_manager | [Planbim](https://planbim.cl/ifc-y-actualizaciones/) |
| it | IFC 4.3: cosa cambia per strade e ferrovie? i software lo supportano? | What changes for roads and railways, and do software tools support it? | civil_infra_engineer | [Biblus](https://biblus.acca.it/ifc-4-3-approvato-come-standard-finale/) |
| de | IFC Struktur: Revit exportiert nur ein IfcSite und IfcBuilding; wie bekomme ich mehrere Grundstücke/Gebäude und MEP-Systeme getrennt? | Revit exports only one IfcSite and IfcBuilding; how to fill project/site/building and separate systems. | bim_coordinator | [BIM me up](https://bim-me-up.com/ifc-struktur/) |
| en | I export from Revit to IFC4, checked the coordinates in IfcSite, but the model appears in the middle of the ocean in Cesium. | — | bim_coordinator | [Cesium forum](https://community.cesium.com/t/right-way-to-georeferencing-file-on-cesium/47030) |
| en | Which IFC properties does Cesium ion use to geo-reference? Correct coordinates are in IFCSITE. | — | bim_coordinator | [Cesium forum](https://community.cesium.com/t/ifc-properties-for-geo-referencing-in-cesium-ion/43003) |
| en | A model with EPSG:27700 coordinates set in Bonsai lands mid-ocean in QGIS after converting to GeoPackage. | — | bim_coordinator | [OSArch](https://community.osarch.org/discussion/comment/25984#Comment_25984) |
| en | Loading a 3D-BAG IFC with projected CRS and map conversion, I cannot place it in the correct CRS. | — | civil_infra_engineer | [engine_fragment #160](https://github.com/ThatOpen/engine_fragment/issues/160) |
| en | I need to extract source and target coordinate systems from IFC (IFCMAPCONVERSION, IFCPROJECTEDCRS) to translate coordinates. | — | student_beginner | [engine_components #223](https://github.com/ThatOpen/engine_components/issues/223) |
| en | IfcProjectedCRS Name is mandatory but UTM 32N plus EVRF2007 does not exist as one EPSG code. | — | developer_programmer | [bSI forum](https://forums.buildingsmart.org/t/ifcprojectedcrs-epsg-code-not-known/972) |
| en | IFC with coordinates around 1934745, 4252640 flickers in three.js; where do I put it on the CesiumJS globe? | — | developer_programmer | [web-ifc #91](https://github.com/ThatOpen/engine_web-ifc/issues/91) |
| en | When ifcopenshell.geom converts to CityGML the shapes come out broken; do I need to load all objects? | — | researcher_academic | [IfcOpenShell #5279](https://github.com/IfcOpenShell/IfcOpenShell/issues/5279) |
| en | Converting AC20-FZK-Haus.ifc to 3D Tiles with mago-3d-tiler loads 0 files. | — | developer_programmer | [mago-3d-tiler #79](https://github.com/Gaia3D/mago-3d-tiler/issues/79) |
| en | I work with CityJSON in the Netherlands; how do I convert city models to IFC? | — | civil_infra_engineer | [bSI forum](https://forums.buildingsmart.org/t/cityjson-into-ifc/) |
| en | Should sensor data be stored in the BIM model via TimeSeries or just linked? I want BIM as the digital twin database. | — | civil_infra_engineer | [OSArch](https://community.osarch.org/discussion/comment/14415#Comment_14415) |
| en | A US state DOT with 500+ projects a year wants a system-wide asset query from as-built IFC. | — | owner_client | [OSArch](https://community.osarch.org/discussion/comment/25545) |
| en | Which IFC entity assigns a unique code to each piece of equipment for O&M on a campus? | — | facility_manager | [OSArch](https://community.osarch.org/discussion/1118/operation-and-maintenance-on-campus-site-with-ifc) |
| en | IFC metadata is searchable in English but not when it is Korean (Cesium ion). | — | developer_programmer | [Cesium forum](https://community.cesium.com/t/ifc-metadata-not-shown-when-it-is-korean/44612) |
| en | QGIS 3D shows nothing below ground level unless the viewpoint is below ground. | — | architect | [OSArch](https://community.osarch.org/discussion/3406/qgis-3d-question) |
| zh | BIM没有地理坐标，需要原点经纬度加xyz旋转角度，原点又不在模型中心 | BIM has no geographic coordinates; origin lat/lon and rotation are needed and the origin is not at the model centre. | developer_programmer | [CSDN](https://blog.csdn.net/liyan_gis/article/details/100132931) |
| zh | GISBox实操指南：如何将IFC文件高效转换为3DTiles格式（设置零点坐标） | Vendor guide to IFC to 3D Tiles incl. zero-point coordinates and b3dm vs glb. | developer_programmer | [CSDN](https://blog.csdn.net/GISBox/article/details/149612800) |
| zh | 如何将Revit格式的BIM数据导入GIS平台？ | How to import Revit BIM data into a GIS platform? | developer_programmer | [Zhihu](https://zhuanlan.zhihu.com/p/388012269) |
| zh | 自主可控BIM，审图后模型汇入CIM平台，图模对位不合格传不上去 | Models flow to the CIM platform after review; non-compliant drawing-model alignment cannot be uploaded. | reviewer_authority | [Guangzhou gov](https://zfcj.gz.gov.cn/attachment/7/7943/7943479/10589336.pdf) |
| ja | PLATEAUのCityGMLをArcGISで表示できる形式に変換する手順 | How to convert PLATEAU CityGML so ArcGIS can display it. | architect | [Qiita](https://qiita.com/masumur/items/8362a1ed91048e26ed2a) |
| ja | CityGMLを都市シミュレーションのデータとして使う論文紹介、CesiumJSにも言及 | Overview of CityGML as urban-simulation data, CesiumJS, smart city. | researcher_academic | [Qiita](https://qiita.com/tosseto/items/34a2a801b8eb299453d1) |
| de | Export nach GML funktioniert, Reimport wirft „ungültige Daten auf Stammebene. Zeile 9, Position 1“ | IFC export to GML works in KITModelViewer but reimport fails with an XML error. | researcher_academic | [KIT-IAI #13](https://github.com/KIT-IAI/SDM_KITModelViewer/issues/13) |
| es | Looking for international groups developing land models via IFC or CityGML; status of IFC for Site, Landscape and Urban Planning. | buildingSMART Spain chapter RFI (record tagged es; the thread text itself is English). | reviewer_authority | [bSI forum](https://forums.buildingsmart.org/t/rfi-urban-and-land-management-think-tank-room-group/4754) |
| en | Revit Slab to IfcSite does not work when the slab points were modified. | — | bim_coordinator | [revit-ifc #505](https://github.com/Autodesk/revit-ifc/issues/505) |
| en | Terrain TINs from 12d with very obtuse triangles break the spot elevation tool in Revit. | — | civil_infra_engineer | [revit-ifc #511](https://github.com/Autodesk/revit-ifc/issues/511) |
| en | An IfcGeographicElement TERRAIN voided by IfcEarthworksCut gives extra faces of the opening body. | — | civil_infra_engineer | [IfcOpenShell #10076](https://github.com/IfcOpenShell/IfcOpenShell/issues/10076) |
| en | Site coverage and site boundary came out as IfcSpace but IFC+SG wants IfcGeographicElement. | — | architect | [GitHub](https://github.com/noddlesskcho/ifc-sg-site-object-repair) |
| en | Is my IFC georeferenced to SVY21 (EPSG 3414), and do I need a SITEBOUNDARY IfcGeographicElement? | — | bim_coordinator | [ifcgref-corenetx](https://github.com/chunyen93/ifcgref-corenetx) |
| en | IfcSite elevation differs between Revit 2022 and older versions, tied to the survey point. | — | bim_coordinator | [revit-ifc #581](https://github.com/Autodesk/revit-ifc/issues/581) |
| en | About 1000 models for thermal simulation; exported space boundaries only include the four walls. | — | developer_programmer | [Dynamo forum](https://forum.dynamobim.com/t/export-ifcrelspaceboundary-room-boundaries/91608) |
| en | 2nd-level space boundary geometry is displaced several metres from the IfcSpace, breaking BEM workflows. | — | mep_engineer | [revit-ifc #961](https://github.com/Autodesk/revit-ifc/issues/961) |
| en | Level 1 boundary to the centre line or inside face? I was told centreline for EnergyPlus/CIBSE but areas then exceed true surface area. | — | researcher_academic | [bSI forum](https://forums.buildingsmart.org/t/level1-boundary-generation-to-the-centre-line-or-inside-face/2724) |
| en | One space and its curtain wall (room bounding on) gets no space boundary, leaving a gap. | — | bim_coordinator | [revit-ifc #107](https://github.com/Autodesk/revit-ifc/issues/107) |
| en | Material thermal properties are not supported in viewers for IFC2x3. | — | researcher_academic | [IfcOpenShell #2433](https://github.com/IfcOpenShell/IfcOpenShell/issues/2433) |
| en | Revit exports similar walls as IfcWall or IfcWallStandardCase inconsistently and layer data is missing for thermal analysis. | — | reviewer_authority | [bSI forum](https://forums.buildingsmart.org/t/difference-between-expectations-and-reality-of-ifc-standards/1040) |
| en | A coordinator wants a free tool to author IFC, edit properties and georeferencing, and convert generic 3D to IFC. | — | architect | [bSI forum](https://forums.buildingsmart.org/t/ifc-editor-authoring-georeferencing-tool/) |

---

## Ready test prompts

All prompts below are **synthetic** (written for testing, never real quotes). "Base" names the synthetic record in `research_raw/wave1` it was derived from; "new" means written for this page to cover a gap or a trap. Several were reworded to sound less like a textbook. Difficulty: easy = one read-only lookup; medium = grouping, comparison, or one ambiguity; hard = multi-step, absent data, risk of invention, or a write.

| # | lang | Prompt | Type | Difficulty | Expected behavior |
|---|---|---|---|---|---|
| N01 | en | is there IfcAlignment in this file or just meshes | understand_concept | easy | Read the schema and list `IfcAlignment` / `IfcLinearPlacement` presence; if none, say so and do not infer an alignment from geometry. (base en-allplan-vw-bentley-s006) |
| N02 | en | my ifc wont open, SchemaError unsupported IFC4X3. what's the FILE_SCHEMA in this file and is it ok | validate_check | medium | Quote `FILE_SCHEMA`; compare to `IFC4X3_ADD2`; explain build/identifier issue; offer a patched copy only if asked. (base en-infra-s003) |
| N03 | en | list all alignments in the model w/ segment counts and total length pls | query_model_data | medium | Walk nested horizontal/vertical layouts; count segments; length from representation or last segment; mark unknown. (base en-infra-s001) |
| N04 | en | what's the starting chainage of the main alignment? I need station of every referent too, file says 4.3.2.0 | query_model_data | hard | Find STATION referents with `Pset_Stationing`; explain StartDistAlong no longer exists; report absence of stationing explicitly. (base en-infra-s002) |
| N05 | en | wait, is station same as DistanceAlong? my start station is 5+00 and everything lands in wrong place | understand_concept | medium | Explain geometric distance vs semantic station; show how to offset by start station; ask unit (ft/m). (base en-infra-s018) |
| N06 | ru | покажи все трассы (IfcAlignment) в модели и пикетаж начала и конца, ифс 4.3 из civila | query_model_data | medium | Alignments with start/end station from referents and length; say if Civil 3D omitted stationing. (base ru-infra-s008) |
| N07 | de | pruef mal ob im Schienenmodell die Gradiente und Trassierung sauber drin sind, inkl. Stationierung. IFC 4.3 | validate_check | hard | Check horizontal/vertical layout presence, segment continuity, cant, referents; report gaps, not a verdict without evidence. (base de-infra-s010) |
| N08 | en | which elements use IfcLinearPlacement and at what DistanceAlong on which alignment? signals mostly | query_model_data | medium | List users of linear placement with base curve, DistanceAlong and offsets; warn if the tool cannot resolve to XYZ. (base en-infra-s006) |
| N09 | en | sample the 3D alignment curve each 10m, x y z + station | convert_format | hard | Evaluate horizontal+vertical at 10 m steps, output a table, state which engine/segment types were supported and flag unsupported ones. (base en-civil-infra-s012) |
| N10 | en | road model from civil3d, everything is IfcBuildingElementProxy again. count them by ObjectType and tell me what they should be | query_model_data | medium | Group proxies by ObjectType/name; propose 4.3 classes as suggestions with reasons; no writes. (base en-us-canada-infra-s003) |
| N11 | en | reclass all proxies with asphalt in the name to IfcPavement FLEXIBLE pls | modify_model_data | hard | Check schema is 4.3, preview matches, ask confirmation, set class and PredefinedType from the valid enum, keep GlobalIds, report count. (base en-civil-infra-s008) |
| N12 | en | upgrade this ifc4 to 4.3 and move the bridge proxies to IfcBridge stuff, keep guids | convert_format | hard | Upgrade schema on a copy; reclassify per an agreed mapping; no official downgrade/upgrade mapping exists so list choices; report changes. (base en-us-canada-infra-s016) |
| N13 | en | show me the IfcBridge tree - which IfcBridgePart has the deck, kerbs, barriers. is the wearing course under the bridge or road? | query_model_data | hard | Print the facility/part decomposition with contained elements; report where the wearing surface sits and note common conventions without asserting a single rule. (base en-us-canada-infra-s001) |
| N14 | zh | 帮我看一下这个桥梁IFC4.3模型里有哪些IfcBridgePart，分别是上部结构还是下部结构，数量多少 | query_model_data | medium | List parts with PredefinedType and element counts. (base zh-infra-s009) |
| N15 | ko | 교량 IFC 4.3 모델에서 교각 목록이랑 선형 기준 거리(DistanceAlong) 뽑아줘 | query_model_data | medium | List piers with their linear-placement distance; state if placed with plain XYZ instead. (base ko-infra-s015) |
| N16 | fr | dans ce modele de tunnel IFC 4.3, liste les IfcTunnel et leurs parties avec la longueur | query_model_data | hard | Trap: there is no complete tunnel class set in 4.3. Say so, check what the file really has (proxies, generic civil elements), report lengths only if present. (base fr-infra-s013) |
| N17 | ja | 道路の線形をIFC4.3に変換して、平面線形の曲線要素(クロソイド含む)がちゃんと入ってるか確認して | convert_format | hard | Convert only if a tool exists; inspect horizontal segment types (line, circular arc, clothoid) and report what survived. (base ja-infra-s014) |
| N18 | no | ligger veimodellen i riktig koordinatsystem (EUREF89 NTM sone?) Hva er origo og rotasjon | query_model_data | medium | Read map conversion/CRS; report EPSG, eastings/northings, rotation; flag missing georeference; do not map "NTM zone" to a code by guess. (base no-norway-s005) |
| N19 | es | puedes validar este IFC de carretera contra el esquema 4.3 y decirme los errores principales | validate_check | medium | Run schema/rule validation, summarise errors by type, mention the buildingSMART validation service. (base es-infra-s011) |
| N20 | en | total concrete m3 for girders and piers in the bridge, by element type | extract_quantities | medium | Select girders/piers, read Qto volumes or compute, group by type and material, state the source. (base en-civil-infra-s007) |
| N21 | en | check each rail asset has the required pset from our EIR before I submit | validate_check | hard | Ask for the requirement list (IDS/EIR); do not invent required psets; output missing items per element. (base en-civil-infra-s009) |
| N22 | en | the alignment is in the file but my viewer shows nothing, can you make it draw as a line | troubleshoot_viewing | medium | Confirm the alignment and its representation exist, explain viewer support gaps, extract a polyline only from a real representation. (new, from web-ifc #878) |
| T01 | en | terrain mesh in there? any earthworks cut/fill elements with volumes | query_model_data | medium | Find terrain representations and `IfcEarthworks*`; quantities only if present; say absent if not. (base en-civil-infra-s011) |
| T02 | en | what are the cut and fill volumes in this model? earthworks elements | extract_quantities | hard | Read `Qto_EarthworksCut/FillBaseQuantities`; offer a geometry computation with named reference surfaces; mention open-surface pitfalls. (base en-qto-s017) |
| T03 | en | site coverage, planting area, site boundary - are they IfcSpace in here? should be proxy / geographic element | validate_check | medium | List IfcSpace matching those names, report the correct IFC-SG classes, offer conversion with relationship repair. (base en-sg-corenetx-s004) |
| T04 | en | highlight everything on the terrain steeper than 1:21 and tell me the area | query_model_data | hard | Ask which surface; compute slope per triangle from the TIN; state 1:21 is about 4.8 percent; flag if surface is open or in odd units. (new, from Dynamo title) |
| G01 | en | model opens far from origin in the viewer. what coordinate system is it using? is there an IfcMapConversion, what are eastings northings | query_model_data | medium | Report CRS, map conversion, site placement, bounding box; suggest fix. (base en-mea-s006) |
| G02 | en | my gpkg lands in the ocean, ifc is in mm, EPSG 27700, check scale on map conversion | troubleshoot_export | hard | Read Scale and project unit; compute expected coordinates; explain mm vs m. (base en-osarch-s012) |
| G03 | en | check georef on this ifc - is there IfcMapConversion + ProjectedCRS or only IfcSite lat/long? will cesium ion put it in the right place | validate_check | hard | Report which mechanisms exist, units, true north; note the tiler reads CRS/ProjectedCRS rather than IfcSite lat/long. (base en-gis-s001) |
| G04 | ru | модель в ифс улетела далеко от нуля и привязки к геодезии нет, глянь что в IfcSite и есть ли MapConversion, надо в qgis положить | validate_check | medium | Report extent from origin, MapConversion/ProjectedCRS presence, IfcSite coordinates; suggest setting CRS and offset. (base ru-gis-s010) |
| G05 | ru | в файле какие координаты у IfcSite и угол истинного севера, в МСК или локальные | query_model_data | medium | Read IfcSite lat/long/elevation, MapConversion, true north; state georeferenced or local; do not assert a regional MSK zone without evidence. (base ru-autodesk-telegram-s016) |
| G06 | es | revisa si el ifc trae el sistema de coordenadas (ETRS89 UTM 30N, EPSG 25830) bien puesto, que lo voy a cargar en el SIG | validate_check | medium | Compare ProjectedCRS name/EPSG to 25830, report mismatch. (base es-gis-s012) |
| G07 | ja | このIFC、平面直角座標系の設定入ってる？なければ座標系と原点のずれ確認して | validate_check | medium | Check for a Japan plane-rectangular CRS; report map conversion and offset. (base ja-gis-s016) |
| G08 | pt | como levo o ifc do revit pro qgis mantendo as coordenadas? tem que converter pra geopackage? | how_to | medium | Explain georeference settings in Revit export, converters, and a units/CRS check before loading. (base pt-gis-s013) |
| G09 | it | come georeferenzio un ifc cosi lo vedo in qgis al posto giusto? uso bonsai, EPSG 3003 | how_to | medium | Explain IfcProjectedCRS and IfcMapConversion in Bonsai, units, verification in QGIS. (base it-gis-s018) |
| G10 | zh | 要把这个ifc放到cesium上，模型有没有地理参考？IfcSite经纬度和IfcMapConversion有没有，没有的话给我原点和旋转怎么取 | query_model_data | hard | Report IfcSite lat/long/elevation, map conversion/CRS, true north; otherwise explain how the user must supply origin and rotation. (base zh-csdn-dev-s015) |
| G11 | de | kannst du aus dem Gebäude ne Außenhülle für CityGML LoD2 ableiten? nur Dach und Wände, Geschosse bitte als Attribut | convert_format | hard | Derive an envelope, classify roof/wall/ground, record storey count, list limitations and assumptions. (base de-gis-s014) |
| G12 | en | I have sensor ids like TS-0412 in a spreadsheet, find which elements in the model have that in Tag or any pset and give me their GlobalIds | query_model_data | medium | Search Tag and all psets; return GlobalId, class, storey and unmatched IDs. (base en-gis-s004) |
| G13 | zh | 帮我按楼层统计一下构件数量，导出成表，数字孪生平台要用，顺便看看有没有没挂楼层的构件 | query_model_data | medium | Group by storey; list elements with no storey; output a table. (base zh-gis-s011) |
| G14 | ko | 한글 속성값이 깨진 요소 찾아줘. 웹뷰어에서 검색이 안돼 | validate_check | medium | Detect encoding problems in non-ASCII strings; list elements; check escaping; do not assume the viewer is wrong. (base ko-gis-s017) |
| G15 | fr | sors moi la liste des locaux avec surface, niveau et nom pour la GMAO, et dis moi lesquels n'ont pas de surface | query_model_data | medium | List IfcSpace with area, storey, name; flag missing area. (base fr-gis-s015) |
| G16 | en | need a light version for the web viewer - strip furniture and mep, keep walls slabs roofs, keep GlobalIds and pset names | convert_format | medium | Filtered copy by class; preserve GlobalIds and psets; report counts and size before/after. (base en-gis-s009) |
| G17 | nl | in welk coördinatenstelsel staat dit model, RD (EPSG:28992) of lokaal? en klopt het hoogtedatum (NAP)? | validate_check | medium | Read projected CRS and vertical datum from the file; do not confirm RD/NAP without evidence. (new, from digiGO thread) |
| G18 | en | put this building at lat 52.37, lon 4.89 so it shows in cesium | modify_model_data | hard | Trap: lat/lon alone is not a georeference. Ask for CRS/EPSG, rotation to true north, elevation datum and base point; confirm before writing a map conversion. (new) |
| E01 | en | do we have IfcRelSpaceBoundary2ndLevel in this file? how many per space, any space with zero | validate_check | medium | Count boundaries per space and level; flag spaces with none. (base en-spaces-s003) |
| E02 | pt | preciso rodar simulacao energetica, verifica se os ambientes estao fechados e tem limite de espaco | validate_check | hard | Check closedness of IfcSpace volumes and presence of boundaries; say what cannot be verified from IFC alone. (base pt-spaces-s014) |
| E03 | en | can you export this to gbXML for EnergyPlus | convert_format | hard | Trap: gbXML is a different format and is not produced from IFC by a plain reader. Ask which tool is available (authoring tool/energy tool); offer a readiness check of spaces, boundaries and layers instead. (new) |
| E04 | en | space boundaries look shifted a few metres from the rooms, is the model wrong? | troubleshoot_export | hard | Compare boundary geometry with the IfcSpace bounding box; mention the known exporter issue before blaming the model. (new, from revit-ifc #961) |
| E05 | en | what are the U-values of the external walls? | extract_quantities | medium | Look for thermal properties/psets and layer thickness; if absent, say so; do not compute U-values from guesses. (new) |

---

## Edge cases and traps for MCP testing in this area

1. **Schema identifiers.** `IFC4X3`, `IFC4X3_ADD2` and older development identifiers are different strings; `IFC4x3` (lower case x) may fail. A good tool reads the header and quotes it; a bad one says "invalid IFC".
2. **Withdrawn versions.** IFC 4.1 and 4.2 files may contain alignments that behave differently from 4.3. Do not treat them as 4.3.
3. **Tunnels.** "List the IfcTunnel parts" in a 4.3 file is a trap: tunnel classes are not a finished 4.3 domain. The correct answer is "not present in this schema; here is what the file does contain".
4. **Alignment presence is layered.** Check four things separately: entity exists; layouts exist; a curve representation exists; the tool can display it. Never report a length from a mesh bounding box.
5. **Station vs distance along; feet vs metres.** The classic error is station 15+00 landing at 1500. Always state the start station and the unit.
6. **Map conversion units.** Eastings in map units; coordinates in project units; Scale connects them. Test a mm project with Scale missing.
7. **IfcSite lat/long is not a CRS.** Latitude/longitude on the site is approximate and secondary when a map conversion exists; True North should not be applied twice.
8. **EPSG ambiguity.** Horizontal-only vs compound codes; "EUREF89 NTM zone" or "МСК" does not identify one code; the assistant must read what the file says, not infer from the country.
9. **Float jitter far from origin.** Large coordinates break viewers (float32). Warn rather than shifting placements silently.
10. **Open terrain surfaces.** TINs are open; boolean cut/fill differs per kernel; extra faces or empty results are kernel artefacts, not necessarily a bad model.
11. **No automatic Qto for earthworks.** Absent quantities should be reported as absent or computed with a named method, not guessed.
12. **Name-based reclassification.** Mapping "asphalt" proxies to `IfcPavement` is a guess; require preview, confirmation, GlobalId preservation, and verification after reload.
13. **Downgrade 4.3 to IFC4/2x3.** No official mapping; every class change is a decision. Warn before doing it and keep the original.
14. **CityGML/3D Tiles loss.** Conversions drop properties and detail. The assistant must say what survives (envelope, selected attributes) and which LoD was assumed.
15. **Sensor values in IFC.** Embedding time series makes files huge and can crash viewers; the right design is IDs in a pset and external data.
16. **Non-ASCII text.** Korean/Japanese/accented properties need correct STEP escapes; viewer search failures may be encoding, not missing data.
17. **gbXML is not IFC.** A request to "export to gbXML" from an IFC reader is out of scope; expect an honest redirect and a readiness check.
18. **Space boundaries are optional.** In a Revit export they are off by default; zero boundaries often means a setting, not a broken model. First-level vs second-level and centre-line vs inside-face are methodological choices tied to the regulation.
19. **U-values from nowhere.** Never compute thermal transmittance without material layer thicknesses and conductivities in the file.
20. **Facility hierarchy rules.** Bridge parts are spatial decompositions; do not put openings in them; some authoring panels cannot nest facilities the way the schema allows. A "tree" request must report the actual relationships, not an idealised hierarchy.
21. **Multi-language terms.** пикетаж/ПК = station, трасса = alignment, Trassierung/Gradiente = horizontal/vertical alignment, 線形 = alignment, 平面直角座標系 = Japanese plane rectangular CRS, МСК = local (regional) coordinate system. The assistant should map them without a translation request but must not guess a code.
22. **Requirements without a document.** "Check against our EIR/IDS" with no document attached needs a clarifying question, not a made-up checklist.

---

## Related docs

- [IFC domain overview: MEP, structural, infrastructure (IFC 4.3), 4D/5D, FM](../../01_ifc_basics/08_domains_mep_structural_infra_4d5d_fm.md)
- [Geometry, placement, coordinates, georeferencing, units](../../01_ifc_basics/06_geometry_placement_coordinates_units.md)
- [What is IFC and versions (IFC4.3, gbXML, CityGML, LandXML)](../../01_ifc_basics/01_what_is_ifc_and_versions.md)
- [Spatial structure and relationships (space boundaries, facilities)](../../01_ifc_basics/04_spatial_structure_and_relationships.md)
- [Revit IFC export reference (coordinate base, space boundaries)](../../03_software/revit/ifc_export_reference.md) and [import/link reference](../../03_software/revit/ifc_import_link_reference.md)
- [Authoring tools (Civil 3D, Tekla, Bonsai)](../../03_software/authoring_tools_ifc.md) and [viewers, checkers, CDE, converters](../../03_software/viewers_checkers_cde_converters.md)
- [Libraries and toolkits (IfcOpenShell, web-ifc)](../../04_open_source/libraries_and_toolkits.md) and [sample IFC files](../../04_open_source/sample_ifc_files.md)
- [MCP servers and AI tools for IFC/Revit](../../04_open_source/mcp_servers_and_ai_tools.md)
- [buildingSMART standards (IFC, IDS, MVD)](../../02_standards_regulations/buildingsmart_standards.md); national pages: [Nordics](../../02_standards_regulations/national/nordics_baltics.md), [Netherlands/Belgium](../../02_standards_regulations/national/netherlands_belgium_luxembourg.md), [Japan/Korea](../../02_standards_regulations/national/japan_korea.md), [China](../../02_standards_regulations/national/china_mainland.md), [Singapore (IFC-SG)](../../02_standards_regulations/national/singapore.md), [Russia](../../02_standards_regulations/national/russia.md)
- [Glossary (multilingual)](../../08_glossary/glossary_multilingual.md) and [abbreviations](../../08_glossary/abbreviations.md)
- Companion page: [MEP, structural, rebar](mep_structural_rebar.md)
