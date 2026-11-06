# Opening/viewing IFC and converting formats (IFC <-> DWG, PDF, SKP, glTF, OBJ, FBX, Excel)
Cell: t-viewers-conversion · Languages: English only in practice (native-language search not possible, see Gaps); synthetic prompts in en, es, pt, de, fr, ru, zh, ja, ko, it · Collected: 2026-11-06 · Records: 34 real / 17 synthetic · Communities covered: GitHub issues (IfcOpenShell/Bonsai, Autodesk revit-ifc, ThatOpen web-ifc, FreeCAD, BIMserver), community.osarch.org, forums.buildingsmart.org

NOTE: the WebSearch budget was exhausted before the first search, so no web searches were run. All sources come from gh issue search and direct page fetches. 18 real records were read in full (evidence "page"), 16 are title/snippet only.

## Top themes (ranked by frequency)
- IFC to GLB/OBJ conversion via IfcConvert: lost colours/materials, huge files, hangs on complex geometry (booleans, many voids)
- Same IFC looks different in different viewers/apps (walls missing, openings wrong, Revit vs Bonsai vs Solibri vs BIM Vision)
- Slow loading / crashes on big files (>2 GiB, minutes to open) and comparison of viewer speed
- DWG/DXF in and out: layer translation by IFC class, DWG->IFC with no meaningful result
- SketchUp interop: SKP import/export, SketchUp-made IFC failing to load
- IFC to Excel / spreadsheets for quantities, BOQ, FM lists
- IFC to GIS (GeoPackage, GeoJSON): units and georeferencing errors
- Revit import problems (IfcTriangulatedFaceSet, windows off wall face, link vs open)
- Revit IFC export aborting, and standalone RVT to IFC converters
- Extracting/saving only a subset of an IFC to share a light model with clients
- Which free viewer to use (Open IFC Viewer, BIM Vision, Bonsai Viewer, xeokit/web-ifc based)
- Malformed IFC headers/encoding from third-party exporters breaking tools

## What people want (the goals behind the questions)
- Open any IFC without owning Revit or the authoring tool, see properties quickly
- Deliver IFC plus DWG/DXF with CAD-style layering
- Get lightweight GLB/OBJ/FBX for web, visualization and game engines with colours intact
- Pull property and quantity tables into Excel
- Trust that a model looks the same everywhere; know which app is wrong
- Slice models by discipline/selection for clients
- Move IFC into GIS at the correct location

## How people write here
- GitHub issues: formal template, pasted logs and version dumps; many bare titles with empty body ("Can't open an IFC file")
- Beginners: self-label ("I am a beginner"), describe symptoms by app comparison ("fine in Blender, broken in Revit")
- Developers: code snippets, version numbers, "regression after update"
- Terse lowercase, dropped articles, "export" used for any conversion ("export dwg to ifc4")
- Polite openers ("Hi Team") in bug reports; closers asking for help "Many thanks for your help"
- Fragments: "walls missing in Bonsai but show in other viewers"; "Conversion ifc to json doesn't work"; "Cannot export material to object format"
- Commonly omitted: IFC version, source authoring tool, file (private); often attached as .txt
- Tone: mostly neutral to frustrated; open-source maintainers answer with "not a bug, IFC is not a 3D mesh format"

## Local ecosystem
- buildingSMART forums: https://forums.buildingsmart.org
- IfcOpenShell / Bonsai (Blender), IfcConvert, ifc2gis: https://github.com/IfcOpenShell/IfcOpenShell
- Autodesk Revit IFC exporter/importer: https://github.com/Autodesk/revit-ifc
- That Open Company web-ifc: https://github.com/ThatOpen/engine_web-ifc
- xeokit: https://github.com/xeokit/xeokit-sdk ; BIMserver: https://github.com/opensourceBIM/BIMserver ; FreeCAD BIM: https://github.com/FreeCAD/FreeCAD
- Open IFC Viewer, BIM Vision (viewers named by users); ACCA IFC viewer; ODA File Converter (DWG<->DXF)
- ifc-to-excel repos: https://github.com/chuongmep/Ifc-to-excel ; https://github.com/datadrivenconstruction/cad2data-Revit-IFC-DWG
- OSArch community: https://community.osarch.org
- Government/regulation: none encountered in this cell (AMB Catalonia IFC-from-topography standard mentioned in buildingSMART thread)

## Notable sources
- https://github.com/IfcOpenShell/IfcOpenShell/issues/8009 DWG layer translation by IFC class
- https://github.com/IfcOpenShell/IfcOpenShell/issues/9481 native SKP import
- https://github.com/IfcOpenShell/IfcOpenShell/issues/6634 SketchUp IFC will not open
- https://github.com/IfcOpenShell/IfcOpenShell/issues/3124 DWG to IFC4
- https://github.com/IfcOpenShell/IfcOpenShell/issues/4247 IFC to GLB 12-hour hang
- https://github.com/IfcOpenShell/IfcOpenShell/issues/2824 GLB lost colours
- https://github.com/IfcOpenShell/IfcOpenShell/issues/5486 GLB size increase
- https://github.com/IfcOpenShell/IfcOpenShell/issues/8026 missing walls vs other viewers
- https://github.com/IfcOpenShell/IfcOpenShell/issues/5626 DWG-derived IFC to XML
- https://github.com/IfcOpenShell/IfcOpenShell/issues/4846 OBJ materials
- https://github.com/IfcOpenShell/IfcOpenShell/issues/2151 DXF to IFC
- https://github.com/IfcOpenShell/IfcOpenShell/issues/9055 viewer load-time comparison
- https://github.com/IfcOpenShell/IfcOpenShell/issues/6118 save selected elements
- https://github.com/IfcOpenShell/IfcOpenShell/issues/10119 >2 GiB IFC
- https://github.com/Autodesk/revit-ifc/issues/587 IfcTriangulatedFaceSet in Revit
- https://github.com/Autodesk/revit-ifc/issues/223 link vs open
- https://github.com/Autodesk/revit-ifc/issues/1021 export aborted
- https://community.osarch.org/discussion/3280/i-am-a-beginner-i-created-a-file-in-bonsai-but-it-doesnt-appear-correctly-in-3d-in-revit
- https://community.osarch.org/discussion/3037/ifc-to-qgis-geopackage
- https://community.osarch.org/discussion/3150/free-standalone-revit-to-ifc-ifc2x3-ifc4-ifc4-3-ifcxml-conversion-without-revit-and-autodesk
- https://forums.buildingsmart.org/t/ifc-to-gis/6115
- https://github.com/opensourceBIM/BIMserver/issues/1334

## Gaps
- WebSearch unavailable (budget exhausted before any call): no native-language (ru, zh, es, pt, de, fr, ja, ko, it) real records; synthetic non-English prompts are not backed by observed posts and phrasing there is my approximation.
- No Autodesk forums (403), Stack Overflow (blocked), reddit, Graphisoft, dwg.ru, csdn, zhihu, cad.de, Qiita/Zenn (article lists did not render).
- No real PDF, FBX or Excel-specific user threads beyond repo listings; GitHub search rate limit hit on xeokit.
- Heavy bias to open-source GitHub issues; commercial-tool users (Revit/Archicad/Navisworks) underrepresented.
- No suspicious sites encountered or skipped.
