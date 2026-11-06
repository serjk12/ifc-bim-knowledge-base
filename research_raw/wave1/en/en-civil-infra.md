# Infrastructure: Civil 3D, InfraWorks, OpenRoads/OpenRail, 12d: IFC 4.3 alignment, roads, rail, bridges
Cell: en-civil-infra · Languages: English · Collected: 2026-11-06 · Records: 33 real / 15 synthetic · Communities covered: GitHub issue trackers only (IfcOpenShell/Bonsai, That Open web-ifc, xBIM). Autodesk and Bentley forums were NOT reached (see Gaps).

IMPORTANT LIMITATION: the WebSearch budget for the run was exhausted before my first search, so no forum search was possible. Only about 15 fetch/gh calls were made, below the 25-search target. All real records come from GitHub issues, not from forums.autodesk.com or communities.bentley.com. Of the 33 real records, 29 were read at page level (issue body plus first comments) and 4 are snippets (title only).

## Top themes (ranked by frequency)
- IfcAlignment geometry not displayed or not implemented in viewers and libraries (IfcGradientCurve, segmented reference curve, cant)
- IfcLinearPlacement support: elements land at the origin, and no easy Python API to get the placement matrix
- Schema identifier problems: IFC4X3 vs IFC4X3_ADD2, case sensitivity, "Unsupported schema" in builds
- Swept and sectioned solids and surfaces for roads and bridges (IfcSectionedSolidHorizontal, IfcSectionedSurface, IfcFixedReferenceSweptAreaSolid, IfcOpenCrossProfileDef)
- Everything arrives as IfcBuildingElementProxy; users want IfcRoad, IfcPavement, IfcCourse and IfcBridge classes
- Spatial structure for facilities (IfcFacility, IfcRoad, IfcRailway, IfcBridge parts) and tool UI restrictions
- Georeferencing and far-away coordinates from 12d and Civil 3D, double offset in federation (Forma)
- Rail samples (bSI Rail room) used as test data, plus railway parts
- Terrain (TIN) and earthworks booleans
- Alignment authoring APIs (stationing referents, PC/PT/PVC, cogo)
- Missing 4.3 support in .NET libraries (xBIM)
- Clearance volumes and clash detection from alignments
- Viewer disagreement (ODA, RDF, DESITE, BIMcollab, Blender)

## What people want (the goals behind the questions)
- Get roads, rails and bridges out of "proxy" into correct IFC4.3 classes.
- See the alignment and the elements placed along it in any viewer.
- Author alignments and sections programmatically (Python, C#, JS) and in Blender-based tools.
- Convert infrastructure IFC to glTF, OBJ or DAE reliably.
- Hand over to a CDE (Forma) without coordinate shifts.
- Quantities for terrain and earthworks.
- Clearance and clash checks driven by alignment geometry.

## How people write here
- Register: developer-style bug reports, either template-driven ("Bug Description", "System Info") or free text; code and traceback pasted, files attached.
- Length: short title plus 2 to 10 lines; maintainers answer at length.
- Jargon: alignment/allignment (frequent misspelling), cant, superelevation, stringline, clothoid, station/chainage, directrix, "proxy", "ADD2", "4.3.x", "BBIM" for BlenderBIM, "ifc4x3" in lowercase.
- Code-switching: none; but STEP lines and Python mixed into prose.
- Openers/closers: often none; students are polite ("Hi guys", "Thanks in advance").
- Context given: library version and OS in templates; the source tool (Desite, 12d, PGSuper) is often named; the IFC schema usually has to be inferred.
- Tone: confused or mildly frustrated, e.g. "it's not clear to me why it is not working".
- Fragments: "shows signal at origin"; "painful BuildingElementProxy"; "Can not display Alignments"; "assigns as space, not things".

## Local ecosystem
- buildingSMART Infrastructure room / IFC 4.3 (ISO 16739-1:2024): https://www.buildingsmart.org/standards/rooms/infrastructure/ (403 on fetch)
- IFC4.3 documentation: https://standards.buildingsmart.org/IFC/DEV/IFC4_3/HTML/lexical/IfcAlignment.html
- IFC Rail sample files: https://github.com/bSI-RailwayRoom/IFC-Rail-Sample-Files (7 folders: alignment with cant, linear placement, swept solids, spatial structure, and more)
- buildingSMART IFC4.3.x sample models and Sample-Test-Files (Infra-Rail.ifc), referenced in issues
- Open source: IfcOpenShell / Bonsai https://github.com/IfcOpenShell/IfcOpenShell ; That Open web-ifc https://github.com/ThatOpen/engine_web-ifc ; xBIM https://github.com/xBimTeam/XbimEssentials
- Software named by users: Civil 3D, 12d, OpenRoads (named in synthetic only), Desite MD Pro, BIMcollab, PGSuper, Autodesk Forma, ODA and RDF viewers.

## Notable sources
- https://github.com/IfcOpenShell/IfcOpenShell/issues/3464 IfcRoad creation
- https://github.com/IfcOpenShell/IfcOpenShell/issues/4921 IFC4 to IFC4.3 upgrade for IfcRoad
- https://github.com/IfcOpenShell/IfcOpenShell/issues/5049 linear placement of signal
- https://github.com/IfcOpenShell/IfcOpenShell/issues/6886 Unsupported schema IFC4X3
- https://github.com/IfcOpenShell/IfcOpenShell/issues/3098 IfcGradientCurve not implemented
- https://github.com/IfcOpenShell/IfcOpenShell/issues/4933 alignment authoring proposal
- https://github.com/IfcOpenShell/IfcOpenShell/issues/6888 railway parts
- https://github.com/IfcOpenShell/IfcOpenShell/issues/5502 swept solid along gradient curve
- https://github.com/IfcOpenShell/IfcOpenShell/issues/4565 viaduct not rendering
- https://github.com/IfcOpenShell/IfcOpenShell/issues/8116 sectioned surface with cant
- https://github.com/IfcOpenShell/IfcOpenShell/issues/7456 facility spatial decomposition
- https://github.com/IfcOpenShell/IfcOpenShell/issues/7621 stringlines
- https://github.com/IfcOpenShell/IfcOpenShell/issues/9121 referents
- https://github.com/IfcOpenShell/IfcOpenShell/issues/9445 12d IFC in Forma
- https://github.com/IfcOpenShell/IfcOpenShell/issues/5471 clearance volume clash
- https://github.com/IfcOpenShell/IfcOpenShell/issues/6254 infra authoring API RFC
- https://github.com/IfcOpenShell/IfcOpenShell/issues/6386 skewed bridge girders
- https://github.com/IfcOpenShell/IfcOpenShell/issues/10076 TIN terrain voids
- https://github.com/ThatOpen/engine_web-ifc/issues/926 and /878 alignment not read or displayed
- https://github.com/xBimTeam/XbimEssentials/issues/93 Civil 3D plugin with xBIM

## Gaps
- WebSearch quota was exhausted before any search ran; no Autodesk forum, Bentley community, buildingSMART forum, Reddit, YouTube or blog content was gathered. Direct fetch of forums.autodesk.com returned 403 and buildingsmart.org rooms page returned 403.
- No OpenRoads/OpenRail, InfraWorks or Civil 3D end-user threads were read, so those user voices (less code-oriented, more "how do I export") are underrepresented; recommend re-running this cell with search access.
- Tool-call count was well below the 30 to 45 target (about 15 calls plus 3 failed searches).
- Four real records are title-only snippets. Synthetic prompts are inspired by GitHub developer voices and may be more technical than typical Civil 3D users.
- No suspicious sites encountered.
