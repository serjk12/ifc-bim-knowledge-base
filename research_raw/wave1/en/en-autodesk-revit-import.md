# Autodesk Community: opening and linking IFC in Revit
Cell: en-autodesk-revit-import · Languages: English · Collected: 2026-11-06 · Records: 50 real / 15 synthetic · Communities covered: GitHub Autodesk/revit-ifc issue tracker only (the Autodesk Community forum itself could not be reached)

IMPORTANT CAVEAT: the WebSearch budget was exhausted before any search ran (0 searches succeeded), and forums.autodesk.com returned HTTP 403 to fetches. All real records therefore come from the Autodesk/revit-ifc GitHub tracker (via gh CLI), where users, often Autodesk Community regulars, report Link/Open IFC problems. 25 records were read in full (evidence "page"), 25 are title-only ("snippet"). The 25+ searches/fetches target was not met.

## Top themes (ranked by frequency)
- Wrong location / origin / Z offset when linking (large coordinates, base point vs internal origin, survey point)
- Project north vs true north rotation on Link IFC, and .ifc.rvt differences
- Link IFC vs Open IFC: separate code paths, in-place/DirectShape vs reference results
- Import class mapping: proxies, loosely typed MEP (IfcFlowSegment), "Not Imported", mapping tables hard to manage
- Missing or wrongly placed geometry (roofs, windows outside wall face, doors, openings, triangulated sets, unsupported profiles)
- Links hanging or failing (Link IFC fail, IFC4X3 header, IFC4 not opening with Open)
- Archicad / Vectorworks / BlenderBIM / Tekla IFCs behaving differently in Revit (door swings, assemblies)
- Properties: Psets to shared parameters, new GUIDs on every relink, shared parameter file deleted
- IfcSpace to Room/Space, IfcOpeningElement as separate generic models
- Editable native elements wanted (walls, sweeps) instead of imported symbols
- API automation of Link IFC and import templates
- Regressions between Revit versions (2020 to 2021, 2023 to 2024, 2024 to 2025-27)

## What people want
- Place the linked IFC at project base point / survey point with correct rotation, repeatably
- Convert IFC into native, editable Revit elements with right categories
- Keep properties and stable shared parameters across model updates
- Predictable class mapping on import without per-session manual setup
- Reliable linking of consultant IFCs (MEP, Archicad, Vectorworks) matching what Solibri/BIM Vision show
- Bulk/scripted linking, validation of files before linking

## How people write here
- GitHub issues use a template: "PR:" (problem report), "ENH:", "INQ:" prefixes; version listed as "Revit 2025.4.x", add-in "25.4.40".
- Titles are terse and often blunt: "Link IFC fail", "Geometry not importing".
- Comparison style: "fine in Revit 2023/2024, broken in 2025-2027"; "opens in BIM Vision/Solibri but not Revit".
- Jargon: "Link IFC", "Open IFC", "ifc.rvt", "DirectShape", "in-place family", "PBP", "survey point", "project north vs true north", "mapping table".
- Developers write precise, code-referencing questions; coordinators write screenshot-driven, slightly frustrated posts; non-native speakers use friendly openers ("thank you for possibility to ask").
- Fragments: "Link IFC only hangs", "opens fine in other viewers", "6 objects close to the zero point", "broken since 2015".
- They usually omit the IFC schema version but give Revit version, often attach screenshots or a zip.

## Local ecosystem
- Autodesk revit-ifc open-source add-in: https://github.com/Autodesk/revit-ifc (LGPL, Link IFC / Export, Jira ids REVIT-xxxxxx cited by maintainers)
- Revit Ideas thread on import by project base point (referenced in issue 320, not fetchable): https://forums.autodesk.com/t5/revit-ideas/ifc-import-using-project-base-point-not-revit-origin/idi-p/6975115
- Viewers/checkers mentioned: BIM Vision, Solibri, BIMcollab Zoom, Trimble Connect, Navisworks, BIM360, simpleBIM
- Other authoring tools: Archicad, Vectorworks, Tekla, AECOsim, BlenderBIM/IfcOpenShell, 12D
- buildingSMART IFC Validation Service (issue 947)
- Bond Bryan guidance on Revit-Archicad exchange (cited in issue 358): https://bimblog.bondbryan.co.uk/guidance-notes-for-autodesk-revit-users-exchanging-models-with-graphisoft-archicad/

## Notable sources
- https://github.com/Autodesk/revit-ifc/issues/990 Link IFC Z coordinate doubled (2025-27)
- https://github.com/Autodesk/revit-ifc/issues/951 Link IFC hangs on single chair
- https://github.com/Autodesk/revit-ifc/issues/223 Link vs Open official explanation
- https://github.com/Autodesk/revit-ifc/issues/320 Import at project base point, solved in 2026
- https://github.com/Autodesk/revit-ifc/issues/566 Shared coordinates IFC to Revit
- https://github.com/Autodesk/revit-ifc/issues/658 DirectShape validation errors in linked MEP IFC
- https://github.com/Autodesk/revit-ifc/issues/442 2020 vs 2021 location difference
- https://github.com/Autodesk/revit-ifc/issues/712 Large coordinates 2023 vs 2024
- https://github.com/Autodesk/revit-ifc/issues/773 Vectorworks IFC linking in 24.2
- https://github.com/Autodesk/revit-ifc/issues/358 Archicad door swings
- https://github.com/Autodesk/revit-ifc/issues/778 How IFC maps to Revit elements
- https://github.com/Autodesk/revit-ifc/issues/798 Import class mapping tables
- https://github.com/Autodesk/revit-ifc/issues/380 Link IFC via API
- https://github.com/Autodesk/revit-ifc/issues/408 Relinking and shared parameter GUIDs
- https://github.com/Autodesk/revit-ifc/issues/522 Project north vs true north
- https://github.com/Autodesk/revit-ifc/issues/710 .ifc.rvt rotation difference
- https://github.com/Autodesk/revit-ifc/issues/729 Wall with window reimports as Imported Symbol
- https://github.com/Autodesk/revit-ifc/issues/928 IFC4X3_ADD2 header fails in Revit 2024
- https://github.com/Autodesk/revit-ifc/issues/909 Re-import duplicates grids
- https://github.com/Autodesk/revit-ifc/issues/568 BIM360/Navisworks import
- https://github.com/Autodesk/revit-ifc/issues/1019 Windows outside wall face
- https://github.com/Autodesk/revit-ifc/issues/15 IfcSpace to Room/Space

## Gaps
- WebSearch limit reached before any query ran; no web-wide discovery was done.
- forums.autodesk.com and Revit Ideas returned 403, so no genuine Autodesk Community forum posts were read; only the tracker was covered. Queries such as "convert IFC to Revit families", "ifc.RVT", "DirectShape editable" were not searched on the forum. source_type for all real records is github_issue, not forum.
- 25 real records are title-only (evidence "snippet") with limited answer detail.
- No suspicious sites encountered; none skipped.
- Re-run this cell with search budget restored to obtain forum threads and Revit Ideas posts.
