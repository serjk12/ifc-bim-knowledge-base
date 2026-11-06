# GitHub: xBIM, IFC++, BIMserver, GeometryGym, Speckle IFC issues
Cell: en-gh-xbim-others · Languages: English (some Russian/Japanese/Turkish text inside IFC samples) · Collected: 2026-11-06 · Records: 62 real / 18 synthetic · Communities covered: xBimTeam (XbimEssentials, XbimGeometry, XbimWebUI), ifcquery/ifcplusplus, opensourceBIM/BIMserver, GeometryGym/GeometryGymIFC, specklesystems (speckle-server IFC import, speckle-sharp)

## Top themes (ranked by frequency)
- Geometry that renders wrong or not at all in a given library (openings, booleans, rebar, Revit/Tekla/Archicad/Vectorworks exports)
- Performance and memory (large IFC, regressions between library versions, browser freeze on big wexbim)
- IFC4x3 support gaps (storeys, psets, colors/styles, writing 4x3)
- Property set and material/quantity retrieval from code (GetPropertySet, material paths, areas/volumes)
- Coordinates: global vs local placement, huge coordinates, rotated IfcSite, map conversion
- String encoding and invalid STEP content (\X2\, backslashes, line breaks, culture issues)
- Conversion requests: IFC2x3 to IFC4, IFC to SVG/DWG/floor plans/3D PDF/wexbim on Linux
- Validation against buildingSMART validator (schema-invalid attributes written by libraries)
- Embedding viewers (WebUI, WinForms/WPF, Unity, WASM) and per-element highlight/hide
- Authoring IFC from code (add opening, PolygonalFaceSet, Pset gaps, serialization bugs)
- Server-side use: BIMserver queries/revisions, Speckle self-hosted IFC import
- Spatial structure/storey tree reading
- Build and platform problems (Linux, Visual Studio, .NET versions)

## What people want (the goals behind the questions)
- Read an IFC reliably in their own app (C#, C++, Python, web) and get geometry, properties, materials, quantities.
- A model that looks the same in their viewer as in BIMvision/Solibri/others; they compare viewers constantly.
- Convert between schema versions and to drawing/2D/web formats.
- Produce valid IFC from code and pass the buildingSMART validator.
- Speed and stable memory on 200-300 MB models in servers and browsers.
- Self-hosted data platforms (BIMserver, Speckle) that accept IFC and expose queryable data, with control over which properties are shared.

## How people write here
- Register: GitHub issue-template style; developers, mostly formal and polite ("Hi Team", "Dear XBim Team", "Hello, team!", "Thanks!").
- Length: from title-only ("How to convert an IFC2x3 file to an IFC4 file?") to very long structured posts (Environment / Context / What we tried).
- Jargon: wexbim, IfcStore, Esent, ShapeInstances, WCS, CreateContext, Xplorer, carve, CSG eps, MVD, BaseQuantities, GUID, STEP/SPF, `\X2\` escapes.
- Context given: exact package versions, attached zipped IFC (often renamed .txt), screenshots comparing viewers ("BIMvision geometry vs xBim").
- Context omitted: no unit info, no export settings, often no schema stated; maintainers must ask "which version?".
- Non-native English: "I wants to display an IFC file", "Thankx", "Informatoin"; Russian/Japanese content appears inside sample files.
- Emotion: mostly neutral; frustration shows in regression reports and with performance; "mission impossible" resignation.
- Code-switching/tool talk: "regression", "repro", "NDA", "proxy".
- AI-assisted posts appear (ChatGPT code that does not match DLLs; very formatted bodies).
- Fragments: "Perhaps related to #550"; "renders correctly in v4/5 and other viewers"; "no greeting, just a STEP line".

## Local ecosystem
- xBIM Toolkit (open source .NET, buildingSMART-adjacent): https://github.com/xBimTeam ; docs https://docs.xbim.net ; XbimEssentials, XbimGeometry, XbimWebUI, XbimPropertySets, xbim Flex (commercial service for floor plans).
- IFC++ (C++ reader/writer, Carve CSG): https://github.com/ifcquery/ifcplusplus
- BIMserver (Java, opensourceBIM): https://github.com/opensourceBIM/BIMserver
- GeometryGym IFC library: https://github.com/GeometryGym/GeometryGymIFC
- Speckle: https://github.com/specklesystems (server issues, archived speckleifc importer, speckle-ifc-import)
- Related tools named by users: BIMvision, Solibri, Trimble Connect, FreeCAD, IfcOpenShell, OCCT, Tekla, Archicad, Vectorworks, Revit.
- Standards/resources cited: buildingSMART IFC4/IFC4x3 docs and validator https://validate.buildingsmart.org, string encoding guidance https://technical.buildingsmart.org/resources/ifcimplementationguidance/string-encoding/, OSArch wiki on IFC materials https://wiki.osarch.org/index.php?title=IFC_-_Industry_Foundation_Classes/IFC_materials

## Notable sources
- https://github.com/xBimTeam/XbimEssentials/issues/676 world vertices vs rotated IfcSite
- https://github.com/xBimTeam/XbimEssentials/issues/674 IsTypedBy regression
- https://github.com/xBimTeam/XbimEssentials/issues/666 IFC4x3 colors missing
- https://github.com/xBimTeam/XbimEssentials/issues/665 v6 export slowdown
- https://github.com/xBimTeam/XbimEssentials/issues/661 IFC4 TagList validation
- https://github.com/xBimTeam/XbimEssentials/issues/660 newline in \X2\ string
- https://github.com/xBimTeam/XbimEssentials/issues/642 materials and colors retrieval
- https://github.com/xBimTeam/XbimEssentials/issues/633 add opening to wall
- https://github.com/xBimTeam/XbimEssentials/issues/620 memory growth in server
- https://github.com/xBimTeam/XbimEssentials/issues/619 area and volume
- https://github.com/xBimTeam/XbimEssentials/issues/616 storeys in Revit IFC4x3
- https://github.com/xBimTeam/XbimEssentials/issues/614 IFC4x3 class tree and psets
- https://github.com/xBimTeam/XbimGeometry/issues/547 invisible geometry due to Plan context
- https://github.com/xBimTeam/XbimGeometry/issues/515 Revit geometry wrong in xBIM
- https://github.com/xBimTeam/XbimGeometry/issues/511 performance metrics
- https://github.com/xBimTeam/XbimWebUI/issues/490 large wexbim in browser
- https://github.com/xBimTeam/XbimWebUI/issues/438 Archicad IFC in web viewer
- https://github.com/ifcquery/ifcplusplus/issues/305 GUID first char regression
- https://github.com/ifcquery/ifcplusplus/issues/303 large coordinate precision
- https://github.com/ifcquery/ifcplusplus/issues/210 bad openings / CSG eps
- https://github.com/opensourceBIM/BIMserver/issues/1327 FM sensor updates discussion
- https://github.com/opensourceBIM/BIMserver/issues/1201 JSON API query vs loops
- https://github.com/specklesystems/speckle-server/issues/5773 IFC importer missing quantities
- https://github.com/specklesystems/speckle-server/issues/1168 IFC traversal in connectors
- https://github.com/specklesystems/speckle-sharp/issues/1778 MVD-like property filter
- https://github.com/GeometryGym/GeometryGymIFC/issues/109 local coordinate system extraction

## Gaps
- Only GitHub issue trackers were read (via gh CLI); no WebSearch/WebFetch was used, so no forum, blog or Q&A cross-checking.
- XbimXplorer and GeometryGym Revit/Rhino plugin repos are either private/unavailable by name; the GeometryGym org public repos hold few user issues (mostly library API bugs).
- Few non-developer personas (architects, coordinators) post here; synthetic records add those voices and are marked synthetic.
- Some synthetic `inspired_by` links point approximately (not exact issue match).
- Posters' identities intentionally omitted. No suspicious sites encountered.
