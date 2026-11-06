# Cross-tool interoperability via IFC (Archicad<->Revit, Tekla<->Revit, Allplan<->Revit, Revit<->Civil 3D) and round-trip expectations
Cell: t-roundtrip-interop · Languages: English (real sources), Japanese (1 source); synthetic prompts in en, ru, zh, es, pt, de, fr, ja, ko, it · Collected: 2026-11-06 · Records: 32 real / 17 synthetic · Communities covered: Autodesk revit-ifc GitHub tracker, buildingSMART forums, OSArch community, Qiita

Note: the WebSearch budget was exhausted before any search ran, so discovery was done through GitHub issue search, forum-internal search pages (buildingSMART Discourse JSON, OSArch) and direct page fetches.

## Top themes (ranked by frequency)
- Open IFC vs Link IFC in Revit: two code paths, in-place families vs DirectShapes, which one to use.
- Coordinates and orientation: project north vs true north, shared coordinates, Z offset, Project Base Point on Link IFC.
- Regressions between Revit versions (2024 fine, 2025-2027 broken) for imported doors/windows and levels.
- Class mapping: IFC class to Revit category, generic models and proxies, hardcoded mappings, IfcSpace to Rooms/Spaces.
- Openings and door/window hosting from Archicad (curved walls, FootPrint 2D symbols).
- Loss of properties/parts/types on round trip (Parts, Name/Reference/Type, psets).
- Colors and materials lost between Allplan/Revit/Archicad.
- Storeys and spatial structure (equal-elevation levels, several IfcBuilding in Tekla).
- Steel and assemblies from Tekla/Advance Steel: duplicates, missing connections.
- IFC2x3 vs IFC4 choice as workaround or requirement (Allplan wants 2x3, upgrade for Archicad).
- Link failures/hangs and performance; sharing the cached .ifc.rvt.
- Parsing differences between tools (valid STEP syntax rejected by Archicad).

## What people want (the goals behind the questions)
- A real round trip: edit in Revit, send IFC to another tool, get back editable native elements with GUIDs and properties intact.
- Predictable mapping from IFC classes to native categories, with control over the mapping table.
- Models landing at the correct place, rotation and elevation without manual fixing.
- Rooms/spaces and storeys that survive across tools.
- Clear official guidance and roadmap from vendors on IFC import in Revit.
- A diagnostic ("what is lost?") before sending a file on: diffs by GlobalId, property comparison.

## How people write here
- GitHub issues use a template (Problem Description, Revit Version, IFC for Revit Addon Version, Windows Version); titles prefixed "PR:", "INQ:", "ENH:" (problem report, inquiry, enhancement).
- Titles are short factual statements; bodies list versions and attach zips: "works in Revit 2024, not 2025-2027".
- Forum posts are polite, longer, and give the tool chain: "Revit to ArchiCAD", "exported as IFC2x3".
- Emotional peaks are rare but explicit: "I am a bit desperate", "Please fix this! Our deliveries are IFC".
- Jargon: Open IFC / Link IFC, .ifc.rvt, DirectShape, in-place family, MVD, IfcExportAs, project north, true north, shared coordinates.
- Typical missing context: no schema version, no exporter version, no file attached; maintainers then ask for the IFC.
- Vendor-specific questions are redirected to vendor support by forum regulars.
- Synthetic prompts for other languages imitate lowercase chat with mixed English terms ("ифс", "ревит", English IFC class names).

## Local ecosystem
- buildingSMART International and forum: https://forums.buildingsmart.org
- Autodesk IFC exporter/importer open source: https://github.com/Autodesk/revit-ifc
- OSArch community (open source AEC, Bonsai/IfcOpenShell): https://community.osarch.org
- IfcOpenShell / BlenderBIM / Bonsai: https://ifcopenshell.org
- Geometry Gym (diff/merge, Rhino): https://geometrygym.com
- ACCA cloud IFC refactoring tool (mentioned in forum): https://www.acca.it
- Vendors: Graphisoft Archicad, Trimble Tekla Structures, Nemetschek Allplan, Autodesk Revit/Civil 3D/Advance Steel.
- Local-language communities (dwg.ru, cad.de, csdn, zhihu) could not be reached; see Gaps.

## Notable sources
- https://github.com/Autodesk/revit-ifc/issues/223 Open vs Link IFC with Tekla assemblies
- https://github.com/Autodesk/revit-ifc/issues/1019 Archicad windows outside wall in Revit 2025-2027
- https://github.com/Autodesk/revit-ifc/issues/1018 Archicad 2D symbols displace doors/windows
- https://github.com/Autodesk/revit-ifc/issues/522 Link IFC project north vs true north
- https://github.com/Autodesk/revit-ifc/issues/710 Link IFC vs .ifc.rvt rotation difference
- https://github.com/Autodesk/revit-ifc/issues/778 How IFC entities map to Revit on import
- https://github.com/Autodesk/revit-ifc/issues/803 Hardcoded import class mappings
- https://github.com/Autodesk/revit-ifc/issues/15 IfcSpace to Room/Space
- https://github.com/Autodesk/revit-ifc/issues/285 Equal-elevation levels vs Allplan
- https://github.com/Autodesk/revit-ifc/issues/282 Steel elements missing in export
- https://github.com/Autodesk/revit-ifc/issues/990 Z coordinate doubled on Link IFC
- https://github.com/Autodesk/revit-ifc/issues/951 Link IFC hangs on round trip
- https://github.com/Autodesk/revit-ifc/issues/658 Missing DirectShapes on link
- https://github.com/Autodesk/revit-ifc/issues/120 Parts properties in IFC
- https://forums.buildingsmart.org/t/how-can-i-control-the-ifc-pipes-colors-revit-to-archicad/2729
- https://forums.buildingsmart.org/t/where-and-how-will-my-colors-be-saved-in-ifc/1806
- https://forums.buildingsmart.org/t/strange-geometry-for-ifcopening/3869
- https://forums.buildingsmart.org/t/correct-use-of-ifc-name-and-reference-deprecated/6429
- https://forums.buildingsmart.org/t/convert-upgrade-ifc2x3-to-ifc4/5210
- https://forums.buildingsmart.org/t/revit-to-ifc-wall-is-dislocated/4575
- https://forums.buildingsmart.org/t/a-number-of-interesting-revit-ifc-parsing-errors/4605
- https://forums.buildingsmart.org/t/next-steps-for-ifc-support-in-revit/3580
- https://community.osarch.org/discussion/3754/opening-cuts-skipped-in-bonsai-studio-0-9
- https://qiita.com/kiyuka/items/00434f1b8e0b38c621fb

## Gaps
- The web search tool had no budget left at the start, so no general or native-language searches (Russian, Chinese, Spanish, Portuguese, German, French, Korean, Italian) could be run; non-English real records are limited to one Japanese Qiita article.
- Blocked or empty: forums.autodesk.com and community.graphisoft.com (403), stackoverflow.com (not fetchable), zhihu/csdn, dwg.ru and cad.de search pages (404), buildingSMART tag pages (404).
- A Chinese-language result list was incidentally retrieved through a search page (titles only, no usable URLs); it was not used for records. It pointed to topics such as lost steel elements, coordinate offsets and Archicad-to-Revit distortion, which informed the zh synthetic prompts.
- Revit<->Civil 3D and Tekla<->Revit forum threads were thin: Tekla appears mostly via GitHub issues; Civil 3D has no real records.
- No suspicious or pirated sites were encountered.
