# Reddit 2: r/Construction, r/MEPEngineering, r/blender (Bonsai), r/FreeCAD, r/gis, r/AskEngineers
Cell: en-reddit-2 · Languages: English · Collected: 2026-11-06 · Records: 27 real / 17 synthetic · Communities covered: NONE of the assigned subreddits directly (see Gaps); substitute coverage from GitHub issue trackers of IfcOpenShell/Bonsai and FreeCAD, which are the same user bases as r/blender (Bonsai) and r/FreeCAD.

IMPORTANT: the WebSearch budget for the turn was exhausted before any Reddit query ran (every call returned "budget used up"). Reddit cannot be fetched. No Reddit record exists in this file. The 27 "real" records are GitHub issues found with the gh CLI (4 read in full, 23 title-only), labelled source_type github_issue. Treat the Reddit cell as NOT done and re-run when search budget is available.

## Top themes (ranked by frequency)
- IFC export from FreeCAD/Blender loses or corrupts content (openings, spatial structure, hidden objects, linked objects)
- File opens in one viewer but not another (Bonsai vs BIMcollab ZOOM vs BIMvision vs xBIM)
- Georeferencing / projected coordinates (IfcMapConversion, EPSG, far-from-origin precision, BCF and drawings from georeferenced models)
- Property sets: custom Psets not saving, filtering by pset value, missing units on pset fields
- Quantities / QTO accuracy (volume precision, layered coverings)
- Units confusion (feet vs mm in clash results, SI vs project units in profile properties)
- IFC patching/linking/extracting with IfcPatch recipes
- Spatial structure problems (missing site/building/storey, several buildings)
- IFC4X3 / infrastructure (boreholes, schema-version attribute errors)
- Version regressions between FreeCAD and bundled IfcOpenShell

## What people want (the goals behind the questions)
- Models that round-trip to IFC without silent data loss.
- Predictable viewer behaviour across tools; explanation when one viewer shows less.
- Correct placement in GIS/real-world coordinates.
- Reliable quantities for takeoff and cost.
- Clear unit handling and property templates.
- Scripted, batch edits of IFC (patch, extract, link) without breaking georeferencing.

## How people write here (GitHub-issue register, not Reddit)
- Terse, lowercase symptoms, often no greeting: "file did not open in BonsaiBIM".
- Compare tools by name: "I could take a look at it using BC ZOOM though".
- Mixed jargon: Pset, QTO, IfcOpeningElement, "strict IFC mode", "proxy".
- Context given via automatic version dump (OS, Blender, Bonsai/FreeCAD version); IFC schema often omitted.
- Tone: neutral to frustrated; precision-minded reporters add numeric tables (volume error percentages).
- Feature requests phrased as "no unit shown, unclear which units to enter".

## Local ecosystem
- buildingSMART / IFC standards: https://www.buildingsmart.org
- IfcOpenShell and Bonsai (open source): https://github.com/IfcOpenShell/IfcOpenShell
- FreeCAD BIM workbench: https://github.com/FreeCAD/FreeCAD
- Viewers named by users: BIMcollab ZOOM, BIMvision, xBIM Xplorer
- GIS tools mentioned: BlenderGIS, QGIS (no pages opened)
- IfcPatch, ifcclash, ifc5d (IfcOpenShell tools)

## Notable sources
- https://github.com/IfcOpenShell/IfcOpenShell/issues/7945 viewer disagreement, MEP file (read)
- https://github.com/IfcOpenShell/IfcOpenShell/issues/8026 missing walls vs other viewers (read)
- https://github.com/IfcOpenShell/IfcOpenShell/issues/9770 precision of volume far from origin (read)
- https://github.com/IfcOpenShell/IfcOpenShell/issues/10074 pset unit confusion (read)
- https://github.com/FreeCAD/FreeCAD/issues/30614 wall hole not exported (read)
- https://github.com/IfcOpenShell/IfcOpenShell/issues/8205 drawings/BCF from georeferenced model
- https://github.com/IfcOpenShell/IfcOpenShell/issues/7178 clash location in mm for feet project
- https://github.com/IfcOpenShell/IfcOpenShell/issues/1428 BlenderBIM + BlenderGIS georeferencing
- https://github.com/IfcOpenShell/IfcOpenShell/issues/8199 extract elements breaks georeferencing
- https://github.com/IfcOpenShell/IfcOpenShell/issues/9808 QTO vertical coverings
- https://github.com/IfcOpenShell/IfcOpenShell/issues/8091 boreholes in Bonsai
- https://github.com/FreeCAD/FreeCAD/issues/21399 spatial structure with multiple buildings
- https://github.com/FreeCAD/FreeCAD/issues/16293 exclude invisible objects from export
- https://github.com/FreeCAD/FreeCAD/issues/32743 duplicate pset property names on import
- https://github.com/FreeCAD/FreeCAD/issues/33854 importer vs bundled IfcOpenShell

## Gaps
- Reddit research not done: WebSearch budget exhausted (200 calls per turn shared across agents) before the first query; reddit.com is not fetchable. No r/Construction, r/MEPEngineering, r/blender, r/FreeCAD, r/gis or r/AskEngineers content was seen. Do not cite this file as Reddit evidence.
- 23 of 27 real records are title-only (evidence "snippet"); paraphrases and answers for them are minimal.
- Real-user colloquial phrasing from Reddit (slang, openers, emotional tone) is missing; synthetic prompts are modeled on GitHub-issue style, not Reddit style.
- No suspicious sites encountered. Nothing downloaded.
- Follow-up: re-run this cell after raising CLAUDE_CODE_MAX_WEB_SEARCHES_PER_SESSION.
