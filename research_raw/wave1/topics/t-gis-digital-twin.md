# IFC + GIS (CityGML, Cesium, ArcGIS, QGIS) and digital twins/IoT/operations
Cell: t-gis-digital-twin · Languages: English (dominant), Japanese, a little German; ru/zh/es/pt/ko/it only as synthetic prompts · Collected: 2026-11-06 · Records: 39 real / 18 synthetic · Communities covered: community.cesium.com, forums.buildingsmart.org, community.osarch.org, GitHub issues, Qiita

## Top themes (ranked by frequency)
- Georeferencing: the model lands "in the ocean" or at the wrong scale in Cesium ion, QGIS or BlenderGIS (IfcSite vs IfcMapConversion vs IfcProjectedCRS, EPSG codes, mm vs m).
- Converting IFC to 3D Tiles or glTF for Cesium (Cesium ion Design Tiler, FME, mago-3d-tiler, Revit add-in); IFC4 and IFC2x3 support gaps.
- Keeping IFC properties and GlobalIds after tiling, and reading them in CesiumJS (getPropertyIds, pset names, EXT_structural_metadata).
- IFC to CityGML, CityJSON and GIS formats (GeoJSON, GeoPackage, shapefile); LoD choice; broken geometry; envelope extraction.
- Digital twin plus IoT: where sensor data belongs (IfcTimeSeries, Pset_SensorHistory, or linked external store); huge files from sensor history.
- Asset management and O&M at campus or agency scale: IFC to CMMS/GIS, unique equipment IDs, querying thousands of models.
- QGIS 3D and viewer limits (nothing below ground, GeoJSON ignoring georef).
- Encoding of non-English metadata (Korean) in web viewers.
- Urban and land IFC: IFC for Site/Landscape/Urban Planning, LandInfra, national topographic base to IFC.
- Choosing a free or open-source toolchain (Bonsai, FreeCAD, QGIS, Cesium) against vendor lock-in.
- Coordinate checking tools (TU Delft IfcGREF/ifcLocator, geo.buildingsmart.nl viewer).
- AI/MCP for geospatial (Cesium MCP servers call).

## What people want
- One reliable georeferencing recipe, so an IFC lands at the right place in Cesium, QGIS and ArcGIS without trial and error.
- Automated, batchable pipelines (CLI, API) from IFC or Revit to 3D Tiles and GIS formats, keeping GUIDs and psets.
- A sensor-data design for digital twins that does not bloat the IFC file.
- System-wide queries across many models, via GIS or database hybrids, for owners and operators.
- Open, cheap alternatives to proprietary BIM and GIS stacks.
- Clear answers on what the IFC schema (4.3, IfcMapConversion) supports for urban and infrastructure scale.

## How people write here
- Registers: GitHub and Cesium posts are structured bug reports with repro steps. OSArch and buildingSMART posts are short, conversational, often non-native English. Qiita posts are formal tutorial blogs.
- Typical length is 1-4 sentences with a tool chain named, often with numbers (EPSG codes, coordinates). Context is often missing: no IFC version, no export settings, no file.
- Jargon is mixed: "ocean" for a wrong location, "tiler", "ion", "Sandcastle", "tileset", "3DBAG", "LoD".
- Entity names are written in caps or as "IFCSITE". Titles can contain typos, e.g. "Ceisum JS White Screen".
- Fragments: "appears in the middle of the ocean"; "is it possible with this library?"; "Anyone with experience?"; "ungültige Daten auf Stammebene" (error quoted in German inside an English report); Japanese: "ArcGISで表示する".
- Tone is mostly neutral or curious. Frustration shows in georeferencing threads. Openers are rare; thanks come at the end.
- Non-English requests (ru, zh, es, pt, de, fr, ja, ko, it) appear here only as synthetic prompts. I found no real native-language GIS/IFC threads, so their phrasing is inferred.

## Local ecosystem
- buildingSMART forums, with the Site/Landscape/Urban Planning project and the BIM & GIS Integration group: https://forums.buildingsmart.org
- TU Delft GeoBIM tools (IfcGREF, ifcLocator, IFC envelope extractor), and geo.buildingsmart.nl (viewer that can save IfcMapConversion).
- OGC standards: CityGML, LandInfra, 3D Tiles; CityJSON; 3DBAG (Netherlands).
- Japan: PLATEAU 3D city models (MLIT), Qiita and Re:Earth communities. Netherlands: Rijksvastgoedbedrijf (government real estate agency) IFC standardisation.
- Open source: IfcOpenShell/Bonsai (https://github.com/IfcOpenShell/IfcOpenShell), BlenderGIS, QGIS, ThatOpen (web-ifc), mago-3d-tiler (https://github.com/Gaia3D/mago-3d-tiler), digital-twin-toolbox (https://github.com/geosolutions-it/digital-twin-toolbox), KITModelViewer (https://github.com/KIT-IAI/SDM_KITModelViewer).
- Commercial: Cesium ion Design Tiler and Revit add-in, FME, ifc2gis (CityGeometrix), ArcGIS, Bentley iTwin, Trimble.

## Notable sources
- https://community.cesium.com/t/ifc-properties-for-geo-referencing-in-cesium-ion/43003 - which IFC fields ion actually uses.
- https://community.cesium.com/t/right-way-to-georeferencing-file-on-cesium/47030 - Revit IFC4 lands in the ocean.
- https://community.cesium.com/t/revit-coordinates-to-cesium-ion-viewer-coordinates/37407 - aligning IFC and tile coordinates.
- https://community.cesium.com/t/cant-retrieve-ifc-properties-and-attributes/40009 - reading IFC props in CesiumJS.
- https://community.cesium.com/t/how-to-get-features-in-bim-model/14683 - FME IFC to 3D Tiles.
- https://community.cesium.com/t/citygml-has-no-color-after-uploading-to-cesium-ion/31018 - CityGML colour bug.
- https://community.cesium.com/t/how-can-i-convert-my-ifc-files-into-citygml-files-in-order-to-visualize-them-on-cesium-globe/13781
- https://community.cesium.com/t/ifc-metadata-not-shown-when-it-is-korean/44612 - Korean metadata.
- https://community.cesium.com/t/cesium-mcp-servers-for-ai-workflows-your-input-needed/44465 - MCP angle.
- https://forums.buildingsmart.org/t/ifc-to-gis/6115 - community state of IFC-to-GIS.
- https://forums.buildingsmart.org/t/ifcprojectedcrs-epsg-code-not-known/972
- https://forums.buildingsmart.org/t/the-future-of-ifc-for-urban-design-planning-development/3916
- https://forums.buildingsmart.org/t/rfi-urban-and-land-management-think-tank-room-group/4754
- https://community.osarch.org/discussion/comment/25984#Comment_25984 - IFC to QGIS GeoPackage.
- https://community.osarch.org/discussion/comment/27629#Comment_27629 - BlenderGIS moves IFC.
- https://community.osarch.org/discussion/comment/14415#Comment_14415 - IfcTimeSeries and sensors.
- https://community.osarch.org/discussion/comment/25545#Comment_25545 - IFC asset management at scale.
- https://community.osarch.org/discussion/1118/operation-and-maintenance-on-campus-site-with-ifc
- https://community.osarch.org/discussion/3136/georeferencing-mon-amour-first-steps
- https://github.com/IfcOpenShell/IfcOpenShell/issues/5279 - IFC to CityGML geometry.
- https://github.com/Gaia3D/mago-3d-tiler/issues/79 - IFC4 not loading in tiler.
- https://github.com/geosolutions-it/digital-twin-toolbox/issues/68
- https://qiita.com/tosseto/items/34a2a801b8eb299453d1 - CityGML (Japanese).
- https://qiita.com/masumur/items/8362a1ed91048e26ed2a - PLATEAU CityGML to ArcGIS.

## Gaps
- The WebSearch budget ran out before any search ran, so everything came from direct fetches of forum search pages, Discourse JSON, GitHub CLI and Qiita search. Coverage is therefore uneven.
- No real threads from dwg.ru, CSDN, cnblogs, Zhihu, Juejin, cad.de, Spanish/Portuguese forums or Korean communities. cnblogs and dwg.ru searches returned 404, CSDN and Juejin returned empty pages, and Stack Overflow, GIS StackExchange, Esri Community and Autodesk forums were blocked (403 or fetch refused). Reddit was not reachable without search.
- Native-language synthetic prompts (ru, zh, es, pt, de, fr, ko, it) are inferred from English threads, not observed, so treat their phrasing with caution.
- Some records rest on search-result snippets only (evidence "snippet"). Two buildingSMART URLs (cityjson-into-ifc, ifc-editor-authoring-georeferencing-tool) lack numeric topic IDs because that is the form I fetched.
- No suspicious or pirated sites were encountered or linked.
