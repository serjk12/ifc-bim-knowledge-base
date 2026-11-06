# OSArch community: Bonsai (BlenderBIM) and IfcOpenShell users
Cell: en-osarch · Languages: English · Collected: 2026-11-06 · Records: 42 real / 17 synthetic · Communities covered: community.osarch.org (forum, General category), IfcOpenShell GitHub issues

## Top themes (ranked by frequency)
- Importing Revit-exported IFC into Bonsai: missing or skipped openings, flipped faces, missing annotation contexts, weak materials.
- Drawings from the model (plans, sections, SVG/PDF sheets): styles, CSS, hatches, dimension formatting, national standards (DIN), regeneration speed.
- Georeferencing and coordinates (IfcMapConversion, IFC2x3 ePsets, false origin, large coordinates, QGIS/GIS handoff).
- IfcConvert usage: OBJ/STEP export, scale and units, per-storey output, excluding glass, placement options.
- IDS and IfcTester: PredefinedType and attribute facets, web app versions, BCF output of failures.
- AI, LLM and MCP: IfcOpenShell MCP, Blender MCP, chat front ends, drawings by AI, rate limits.
- Voids, openings, windows and doors in Bonsai 0.9 (snapping, Refresh Geometry, void limit, crashes).
- Properties and psets: shared property entities from Revit, custom Bonsai psets, documentation gaps.
- Software installation and compatibility: Blender versions, macOS Apple Silicon, add-on conflicts, IfcConvert download.
- Batch and programmatic editing: moving placements, IfcPatch recipes, Python scripts.
- Geometry quality: tessellation, Brep faceting, triangle reduction, performance with large models.
- Layered walls and material layer sets.
- Versioning and round-trip with Revit while keeping cost or schedule data.
- Learning path for newcomers from Revit.

## What people want (the goals behind the questions)
- Use a fully free, IFC-native workflow and still get real construction drawings.
- Get Revit IFCs into Bonsai without broken openings, geometry or lost data.
- Automate: batch moves, per-storey exports, validation with IDS and BCF reports, AI agents that read and edit IFC.
- Get georeferencing and units right once and have it survive export to GIS and other tools.
- Understand whether odd behaviour is a bug, a limitation of IFC, or user error.
- Share national drawing and template standards (German DIN, LOIN).
- Keep downstream data (cost, schedule) linked when models are updated.

## How people write here
- Register: collegial, informal, polite; many threads end with thanks and "solved" self-answers. Posts are short unless a developer posts a design proposal.
- Context given: Blender and Bonsai version numbers almost always; IFC file often attached when asked; error text pasted verbatim.
- Context omitted: IFC schema version, source tool export settings, units.
- Jargon: Bonsai (formerly BlenderBIM, "BBIM"), "dailies" (nightly builds), "false origin", "pset", "ePset", "proxy", "void", "authoring tool", "native IFC".
- Common framing: "bug or intended?", "am I doing something wrong?", "is there a setting for...".
- Code-switching: occasional German or Italian terms in otherwise English posts.
- Newer posts openly mention AI assistance and Claude or MCP.
- Fragments: "hope it's not lost!"; "bug or misunderstanding of IDS?"; "Add Window tool doesn't attach to the wall"; "G'day all" as an opener.

## Local ecosystem
- buildingSMART standards: IFC (ISO 16739), IDS, BCF, bSDD, IFC4.3 (infrastructure), https://www.buildingsmart.org
- Bonsai / IfcOpenShell: https://ifcopenshell.org , https://github.com/IfcOpenShell/IfcOpenShell
- OSArch community and wiki: https://community.osarch.org , https://wiki.osarch.org , https://osarch.org
- Tools mentioned: IfcConvert, IfcPatch, IfcTester (ifctester.org), IfcClash, IfcCsv, IfcViewer/BonsaiViewer, ifcchat/ifcmcp, ifc2gis, ifcurl, Speckle, TopologicPy, FreeCAD, QGIS, Inkscape, Solibri, BIMvision.
- Standards touched: DIN 1356-1 (drawing conventions), EN 17412-1 (LOIN), OpenBIM Pledge.

## Notable sources
- https://community.osarch.org/discussion/3765/roadmap-for-revit-migrator-to-bonsai-bim-absolute-beginner
- https://community.osarch.org/discussion/3783/claude-bonsai-construction-drawings
- https://community.osarch.org/discussion/3782/native-ifc-as-the-source-a-reproducible-project-template-for-bonsai-and-two-questions
- https://community.osarch.org/discussion/3750/german-drawing-conventions-din-1356-1-for-bonsais-2d-output-a-reference-from-vocational-training
- https://community.osarch.org/discussion/3478/ifctester-not-properly-check-predefinedtype-requirements
- https://community.osarch.org/discussion/2781/ifcconvert-how-to-control-the-resulting-step-models-scale
- https://community.osarch.org/discussion/3308/solved-ifctester-ifc-4-3-add2-support-question
- https://community.osarch.org/discussion/3754/opening-cuts-skipped-in-bonsai-studio-0-9
- https://community.osarch.org/discussion/3685/bonsai-0-9-blender-5-2-2-new-void-system-improved-until-ist-was-broken
- https://community.osarch.org/discussion/3037/ifc-to-qgis-geopackage
- https://community.osarch.org/discussion/3043/canceled-revit-subscription-need-help-with-future-file-translations-to-ifc
- https://community.osarch.org/discussion/1753/bbim-two-door-types-with-connected-properties
- https://community.osarch.org/discussion/3514/rendering-png-snapshots-for-bcf-issues
- https://community.osarch.org/discussion/3548/batch-editing-object-placement-for-multiple-editable-ifc-elements
- https://community.osarch.org/discussion/2823/building-local-placement-in-bonsai
- https://community.osarch.org/discussion/3396/ai-chat-ifcopenshell-org-is-live
- https://community.osarch.org/discussion/3567/should-a-drawing-in-bonsai-be-a-live-view-rather-than-a-generated-file
- https://community.osarch.org/discussion/3071/blender-bonsai-edit-ifc-file
- https://community.osarch.org/discussion/261/layered-walls-in-blenderbim
- https://community.osarch.org/discussion/95/ifc-export-newbie-question
- https://github.com/IfcOpenShell/IfcOpenShell/issues/3115
- https://github.com/IfcOpenShell/IfcOpenShell/issues/6120
- https://github.com/IfcOpenShell/IfcOpenShell/issues/8205

## Gaps
- WebSearch was unavailable (the per-turn search budget was already used up), so discovery relied on fetching the forum home, listing pages and the forum's own search, plus the GitHub CLI.
- Several records from threads without a visible year were dated 2026 by inference; the forum UI shows only month and day.
- The OSArch wiki, Matrix/Discord chats, YouTube, Reddit and Hacker-news style mirrors were not covered.
- Records r034, r035 and r039, r041, r042 are snippet-level only (title or search snippet).
- Spanish-language category of the forum was not examined (outside this cell's English scope).
- No suspicious or pirated sites were encountered.
