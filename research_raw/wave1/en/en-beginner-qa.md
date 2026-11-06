# Beginner questions: what is IFC, how to open it, IFC vs DWG/RVT
Cell: en-beginner-qa · Languages: English · Collected: 2026-11-06 · Records: 16 real / 16 synthetic · Communities covered: GitHub issue trackers only (Autodesk/revit-ifc, IfcOpenShell). INCOMPLETE: the web search budget ran out before any search ran.

## Top themes (ranked by frequency, from the thin sample)
- Open IFC vs Link IFC in Revit: different results, in-place families, lost data.
- IFC will not open or load in a viewer (BIMvision, Bonsai, Blender, Xbim Xplorer).
- Importing IFC into Revit: geometry errors, unsupported representations, wrong Z or placement.
- Whether Pset values and Revit parameters survive a round trip.
- Converting IFC to other formats (SVG plans, OBJ, GLB).
- Editing IFC after export, for example type-shared property sets.
- Slow loading or hangs on large files.
- IfcSpace not becoming Rooms or Spaces.
- Not covered (no data): IFC vs DWG/RVT concept questions, "what is IFC", free viewer recommendations. The synthetic records are based on prior knowledge, not on collected posts.

## What people want (the goals behind the questions)
- Use someone else's IFC inside Revit with usable, editable, correctly placed elements.
- See a file at all without owning Revit.
- Keep properties and parameters through exchange.
- Get 2D or other formats out of an IFC.
- Know why a file fails and which tool is at fault.

## How people write here
Observed only in GitHub issues, so the register is biased toward developers and power users.
- Short title-only problem statements: "Link IFC fail", "Can't import IfcTriangulatedFaceSet".
- Polite closers: "thanks in advance", "appreciate some official feedback".
- Pasted code and lists of which viewers succeeded or failed.
- Beginner phrasing is only seen in the drag-and-drop converter question.
- Software versions are given in the title: "Revit 2019 and 2020".
- The issue tracker's "PR:" prefix marks a problem report.
- Real beginner chat phrasing (Quora, Reddit, YouTube titles) was NOT collected.

## Local ecosystem
- buildingSMART International, IFC standard: https://technical.buildingsmart.org/standards/ifc/ (page blocked, 403; not read)
- Autodesk revit-ifc, the open-source IFC add-in for Revit: https://github.com/Autodesk/revit-ifc
- IfcOpenShell and Bonsai (formerly BlenderBIM): https://github.com/IfcOpenShell/IfcOpenShell
- web-ifc and That Open Engine: https://github.com/ThatOpen/engine_web-ifc
- xeokit SDK: https://github.com/xeokit/xeokit-sdk
- IfcPlusPlus: https://github.com/ifcquery/ifcplusplus
- Viewers named in issues: BIMvision, BC ZOOM, Xbim Xplorer, ODA Open IFC Viewer.

## Notable sources
- https://github.com/Autodesk/revit-ifc/issues/223 (Open vs Link, read)
- https://github.com/Autodesk/revit-ifc/issues/15 (IfcSpace to Room, read)
- https://github.com/Autodesk/revit-ifc/issues/152 (parameter import, read)
- https://github.com/Autodesk/revit-ifc/issues/131
- https://github.com/Autodesk/revit-ifc/issues/587
- https://github.com/Autodesk/revit-ifc/issues/951
- https://github.com/Autodesk/revit-ifc/issues/990
- https://github.com/Autodesk/revit-ifc/issues/138
- https://github.com/IfcOpenShell/IfcOpenShell/issues/585 (read)
- https://github.com/IfcOpenShell/IfcOpenShell/issues/1516 (read)
- https://github.com/IfcOpenShell/IfcOpenShell/issues/3957 (read)
- https://github.com/IfcOpenShell/IfcOpenShell/issues/7945 (read)
- https://github.com/IfcOpenShell/IfcOpenShell/issues/6433
- https://github.com/IfcOpenShell/IfcOpenShell/issues/2499
- https://github.com/IfcOpenShell/IfcOpenShell/issues/3922
- https://github.com/IfcOpenShell/IfcOpenShell/issues/9055

## Gaps
- WebSearch failed with "web search budget is used up (limit: 200 per turn, shared by every agent)". Zero searches ran. The target of 25+ searches was not met.
- Quora, YouTube, Reddit, Autodesk forums and other Q&A sites were never searched. The Autodesk forum fetch returned 403, the OSArch fetch returned 404 and the buildingSMART fetch returned 403.
- The cell asks for 30-60 real records. Only 16 were collected, and all are GitHub issues. 7 were read in full and 9 were seen as snippets. None are true beginner Q&A.
- The 16 synthetic records come from general knowledge of how beginners phrase requests, not from collected posts. Treat their style as unvalidated.
- To finish, rerun this cell after raising CLAUDE_CODE_MAX_WEB_SEARCHES_PER_SESSION.
- No suspicious sites were encountered.
