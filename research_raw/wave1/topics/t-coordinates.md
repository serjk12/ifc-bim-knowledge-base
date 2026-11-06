# Coordinates, georeferencing, shared coordinates, survey/base point, IfcMapConversion, models far from origin

Cell: t-coordinates · Languages: English (real sources); native-language prompts only as synthetic (ru, zh, es, pt, de, fr, ja, ko, it) · Collected: 2026-11-06 · Records: 41 real / 17 synthetic · Communities covered: GitHub (Autodesk/revit-ifc, IfcOpenShell, ThatOpen/engine_web-ifc), forums.buildingsmart.org, community.osarch.org

IMPORTANT LIMITATION: the WebSearch budget was exhausted before this cell started, so no native-language community (dwg.ru, csdn, cnblogs, zhihu, cad.de, qiita, foros) could be searched. All real records are English. The non-English synthetic prompts are NOT backed by real posts from those communities.

## Top themes (ranked by frequency)
- Revit IFC export/link puts the model far from origin or in the wrong place (Link IFC regressions, add-in version changes).
- Choosing the coordinate base: internal origin vs project base point vs survey point vs shared coordinates, and mixing options across models.
- True North / grid north rotation applied twice or ignored.
- Elevation/Z offsets from project elevation (rooms, IfcSite, upgraded models).
- IfcMapConversion written wrongly (projected coords in geometry plus a map conversion = double shift) or not read by most software.
- IfcProjectedCRS / EPSG entry problems in the Revit export GUI (code not persisted, wrong code).
- IFC2x3 has no map conversion: workarounds via psets (ePset_MapConversion) on IfcSite/IfcProject.
- Large coordinates: float precision loss in viewers and code (flicker, wrong volumes, web-ifc/three.js, Cesium).
- Georeferencing lost on IfcPatch extract/link/federate in Bonsai; drawings/BCF/clash positions off.
- Units mismatch (feet vs mm, metres) shifting georeferenced positions.
- Validation of georeferencing rules (HasCoordinateOperation, IfcSite lat/long vs MapConversion consistency).
- IFC to GIS (QGIS, Cesium, CityGML) coordinate handling.

## What people want
- One reliable setting so architect, structural and civil models line up on import without manual moving.
- To import IFC into Revit using the project base point as origin (asymmetry with export).
- To read, verify and set CRS/EPSG, eastings/northings, height and rotation in a file without a GIS specialist.
- Detect files with double-applied or missing georeferencing before federation.
- Keep georeferencing through patching/extraction/linking workflows.
- Numerically stable geometry/quantities for models at E 500000 / N 5000000.

## How people write here
- Register: GitHub bug reports are terse templates (Problem Description, Revit Version, Add-in Version); forum posts are longer, polite and spec-aware.
- Jargon: PBP, survey point, shared coordinates, internal origin, True North, "georef", EPSG, MGA, "BIM zero point".
- Misspellings: "Georeferening", "Georefrancing", "IFCsite", "EPSG-code".
- Venting: caps and sarcasm after regressions ("USE 21.2.1.0 if don't want to work additionally at the weekend").
- Context given: Revit version, add-in version, screenshots; omitted: the actual file, EPSG, units.
- Fragments: "I googled it, seen many videos"; "works well in Trimble, BIMvision"; "It is more like a question about correct behaviour".
- Synthetic native-language prompts imitate lowercase brevity ("ифс улетел на 3 км", "revit导出ifc位置不对") but are unverified.

## Local ecosystem
- buildingSMART International (IFC4/4.3 georeferencing rules): https://forums.buildingsmart.org
- Autodesk revit-ifc exporter (open source): https://github.com/Autodesk/revit-ifc
- IfcOpenShell / Bonsai (Blender): https://github.com/IfcOpenShell/IfcOpenShell
- That Open Company web-ifc: https://github.com/ThatOpen/engine_web-ifc
- OSArch community (openBIM enthusiasts): https://community.osarch.org
- QGIS, CesiumJS, Trimble Connect, BIMvision, Tekla mentioned as counterparts.
- National CRS examples seen: SWEREF 99 (Sweden), MGA/EPSG:28356 (Australia).

## Notable sources
- https://github.com/Autodesk/revit-ifc/issues/566 IFC to Revit with shared coordinates
- https://github.com/Autodesk/revit-ifc/issues/320 import using project base point
- https://github.com/Autodesk/revit-ifc/issues/301 double True North rotation
- https://github.com/Autodesk/revit-ifc/issues/424 add-in regression, far-away link
- https://github.com/Autodesk/revit-ifc/issues/804 large coordinates, openings displaced
- https://github.com/Autodesk/revit-ifc/issues/780 Z offset after upgrade
- https://github.com/Autodesk/revit-ifc/issues/907 rooms wrong elevation
- https://github.com/Autodesk/revit-ifc/issues/255 Projected CRS GUI how-to
- https://github.com/Autodesk/revit-ifc/issues/818 wrong EPSG in GUI
- https://github.com/IfcOpenShell/IfcOpenShell/issues/9770 precision far from origin
- https://github.com/IfcOpenShell/IfcOpenShell/issues/8199 extract elements loses georef
- https://github.com/IfcOpenShell/IfcOpenShell/issues/7016 linked georeferenced plan view
- https://github.com/IfcOpenShell/IfcOpenShell/issues/5055 edit_georeferencing keyword
- https://github.com/ThatOpen/engine_web-ifc/issues/91 Cesium + high coordinates
- https://github.com/ThatOpen/engine_web-ifc/issues/302 local vs global coordinates
- https://forums.buildingsmart.org/t/we-have-a-problem-with-ifcmapconversion/5695
- https://forums.buildingsmart.org/t/offset-stored-in-ifc-file-how-and-where/2848
- https://forums.buildingsmart.org/t/how-is-the-real-world-placement-stored-in-a-ifc-file/4976
- https://forums.buildingsmart.org/t/article-about-ifc-coordinate-reference-systems-and-revit/1418
- https://forums.buildingsmart.org/t/ifcsite-does-not-reference-the-epsg-code-for-wgs84-and-further-inconsistencies-with-georef/3499
- https://community.osarch.org/discussion/comment/29556/ IFC2x3 georef psets in Bonsai

## Gaps
- WebSearch budget exhausted: no searches done; discovery relied on gh issue search, and on the site search pages of OSArch and buildingSMART forums.
- No real posts from Autodesk Forums (403), Graphisoft, Reddit, Stack Overflow/GIS SE (fetch blocked), Qiita (empty results), dwg.ru (404), CSDN/Cnblogs/Zhihu, cad.de, Spanish/Portuguese/French/Korean/Italian communities.
- Many buildingSMART records are snippet-level only (title plus blurb); 3 revit-ifc and 1 IfcOpenShell records are title-only snippets.
- GitHub search API rate limit hit mid-way.
- No suspicious sites encountered.
