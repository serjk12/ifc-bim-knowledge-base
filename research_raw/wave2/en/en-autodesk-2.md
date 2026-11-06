# Autodesk Community 2024-2026: newest Revit (2025-2027) IFC questions, IFC4.3, new property mapping
Cell: en-autodesk-2 · Languages: English · Collected: 2026-11-06 · Records: 48 real / 17 synthetic · Communities covered: forums.autodesk.com (Revit Architecture/MEP/Structure/Ideas, via search snippets), Autodesk/revit-ifc GitHub issues and releases, help.autodesk.com Revit 2027 What's New

## Top themes (ranked by frequency)
- User-defined property sets / parameter mapping: values not exported, type vs instance, empty values dropped, TXT file quirks (IFCElement vs IFCRoot, encoding, unit mismatch).
- Revit 2027 new Manage Property Sets / Property Mapping GUI: incomplete parameter lists, no project parameters, IfcProject missing, unclear Property Type.
- Export failures and crashes on Revit 2025/2026: network or cloud (ACC/Forma, Desktop Connector) write errors, duplicate exporter add-ins, "unrecoverable error".
- Link IFC / Open IFC problems: slow, hangs, crashes, empty bound groups, wrong Z/level elevation, positioning options missing.
- Coordinates and georeferencing: Project Base Point vs Survey Point, IfcSite elevation, double-offset levels.
- IFC4.3 / IFC4x3 export: errors on door families, space boundaries broken, wrong ViewDefinition header, quantity sets lacking, ADD2 schema not linkable in Revit 2024.
- Class mapping: everything becomes IfcBuildingElementProxy, IfcExportAs parameter vs mapping table, predefined types lost for beams/columns.
- Regressions between exporter builds (wall joins, room geometry shifted, curtain walls, openings, door/window placement).
- Rooms/spaces and quantities: IfcSpace areas missing, 3D-view vs plan-view export, space boundaries.
- Structural/MEP specifics: steel connections without psets, IfcFlowSegment vs duct/pipe segment, flexible ducts inflating file size.
- GUID stability across exports and linked models.
- Validation wishes: IDS inside Revit, exporting empty properties for later checking.

## What people want (the goals behind the questions)
- Get a clean, predictable coordination IFC out of Revit without a Dynamo/TXT detour: right class, right predefined type, right psets.
- Map their own shared/project parameters to standard Pset_* properties through a GUI, with data-type awareness.
- Round-trip: link or open an IFC (often their own export or a partner's) with correct position, levels and editable-enough content.
- Hit client or national requirements (IDS, German/Nordic-style property demands) without bloating the file with N/A values.
- Know which exporter build fixes which bug and whether to roll back, update the GitHub add-in, or wait for 2027.x.
- Stable GUIDs so change tracking works between issues.

## How people write here
- Register: mostly neutral and technical, slightly clipped; forum titles are noun phrases ("IFC Export location issue", "Unable to create IFC"); GitHub issues follow a bug template with Problem / Version / Add-in version.
- Length: forum posts short with little diagnostic data (often no file, no add-in version); GitHub reports are long, with screenshots and pasted TXT or header text.
- Jargon and shorthand: "IFC", "ifc4x3", "RVT", "PSet txt", "IfcExportAs", "Reference View", "Design Transfer View", "proxy", "bind link", "base point", "survey point", "Dynamo".
- Casing/emphasis: ALL-CAPS titles ("REVIT TO IFC EXPORTING AND MAPPING TASKS"), "ANY", "NOT EXPORTING", triple exclamation in crash titles.
- Version-first: people lead with the release ("Revit 2026:", "Revit 2025.4.4", "26.4.1") or compare versions ("worked in 2025, broken in 2026").
- Short fragments: "Revit 2026 won't export to IFC?"; "mapping parameters severely lacking"; "Link IFC fail".
- Context often omitted: IFC schema/MVD, exporter add-in version, shared coordinate settings; context often given: screenshots, error text quoted verbatim.
- Closers: many threads end with a workaround found by the poster (uninstall add-in, UTF-8, change IFCElement to IFCRoot) rather than a vendor answer.
- Tone: frustrated about regressions and crashes; polite and curious in GitHub inquiries ("I'm currently testing the new dialog").
- Code-switching: none in English threads, but local-language parameter names appear (Czech-style Volume/Area shared params).

## Local ecosystem
- Autodesk Community forums (Revit Architecture, MEP, Structure, Ideas, Forma): https://forums.autodesk.com/
- Autodesk open-source IFC exporter (revit-ifc) and its issue tracker/releases: https://github.com/Autodesk/revit-ifc, https://github.com/Autodesk/revit-ifc/releases
- Revit help and 2027 What's New: https://help.autodesk.com/cloudhelp/2027/ENU/Revit-WhatsNew/files/GUID-C057D715-1571-4D11-8F02-417F3B385577.htm
- Autodesk Forma / ACC (cloud collaboration, Desktop Connector).
- buildingSMART IFC4.3 (ISO 16739-1:2024), Reference View MVD, IDS (Information Delivery Specification); IFC4 Design Transfer View and IFC2x3 Coordination View 2.0.
- Third-party tools mentioned: Solibri, BIMcollab, BIM Vision, Navisworks, Dynamo, DiRoots, Archicad IFC Model Exchange add-in.
- Third-party blog coverage: https://bimcorner.com/?p=43755 (IFC exports from Revit), https://blog.bimsmith.com/Revit-2027-Key-Things-to-Know-About-the-Latest-Release-of-Autodesk-Revit, https://www.autodesk.com/blogs/aec/2026/06/16/whats-new-in-revit-2027-1/

## Notable sources
- https://forums.autodesk.com/t5/revit-architecture-forum/revit-2026-won-t-export-to-ifc/td-p/13807489 - 2026 export failure, duplicate exporter, network path.
- https://forums.autodesk.com/t5/revit-architecture-forum/ifc-export-from-rvt2026-and-linking-problem/td-p/14065386 - level elevations doubled after relink.
- https://forums.autodesk.com/t5/revit-architecture-forum/issues-exporting-ifc4x3-quot-unexpected-errors-occurred-while/td-p/13292361 - IFC4x3 door errors, fixed in 2026.
- https://forums.autodesk.com/t5/revit-architecture-forum/revit-ifc4x3-export-incorrect-space-boundaries/m-p/14048745 - IFC4x3 space boundaries.
- https://forums.autodesk.com/t5/revit-architecture-forum/issues-with-exporting-type-parameters-from-revit-to-ifc/td-p/14004505 - type parameters missing.
- https://forums.autodesk.com/t5/revit-architecture-forum/ifc-export-in-2027-mapping-parameters-severely-lacking/td-p/14229702 - 2027 mapping GUI complaints.
- https://forums.autodesk.com/t5/revit-ideas/gui-for-project-parameter-mapping-in-ifc-export-missing-in-revit/idi-p/14097939 - idea for full GUI.
- https://forums.autodesk.com/t5/revit-architecture-forum/revit-2026-ifc-link-binding-issue/td-p/13940725 - Bind Link empty group.
- https://forums.autodesk.com/t5/revit-mep-forum/ifc-link-takes-long-and-revit-crashes/td-p/13207354 - link performance.
- https://forums.autodesk.com/t5/revit-architecture-forum/problem-linking-ifc-in-revit-acc-desktop-connector-issue/td-p/14108889 - ACC/Forma linking.
- https://forums.autodesk.com/t5/revit-architecture-forum/missing-properties-when-exporting-ifc-from-revit-using-custom/td-p/13217311 - TXT mapping pitfalls.
- https://forums.autodesk.com/t5/revit-structure-forum/structural-connections-ifc-parameters/td-p/13252740 - connection psets unsupported.
- https://forums.autodesk.com/t5/revit-mep-forum/ifc-export-ducts-and-pipes/td-p/12370919 - duct/pipe classes by schema.
- https://github.com/Autodesk/revit-ifc/issues/984 - 2027 Manage Property dialog Q&A.
- https://github.com/Autodesk/revit-ifc/issues/971 - IfcProject missing in 2027 pset picker.
- https://github.com/Autodesk/revit-ifc/issues/960 - Category not exportable in user-defined pset.
- https://github.com/Autodesk/revit-ifc/issues/963 - empty-value export by design.
- https://github.com/Autodesk/revit-ifc/issues/1013 - IFC4x3 Reference View header bug.
- https://github.com/Autodesk/revit-ifc/issues/990 - Link IFC Z offset.
- https://github.com/Autodesk/revit-ifc/issues/1001 - wall joins regression 2026.
- https://github.com/Autodesk/revit-ifc/issues/952 - predefined types for beams/columns.
- https://github.com/Autodesk/revit-ifc/issues/906 - class/predefined-type forcing.
- https://github.com/Autodesk/revit-ifc/issues/902 - IDS auditing in Revit.
- https://github.com/Autodesk/revit-ifc/issues/981 - network-folder write check.
- https://github.com/Autodesk/revit-ifc/issues/924 - room geometry shift.
- https://github.com/Autodesk/revit-ifc/issues/1018 - Archicad 2D symbols and door/window placement.
- https://github.com/Autodesk/revit-ifc/releases - release notes per Revit version.
- https://help.autodesk.com/cloudhelp/2027/ENU/Revit-WhatsNew/files/GUID-C057D715-1571-4D11-8F02-417F3B385577.htm - official IFC Parameter Mapping.

## Gaps
- forums.autodesk.com returned HTTP 403 to every fetch, so all forum records are snippet-level (search result summaries); the original question text, tone and accepted answers are only partially known. Several forum records carry only a title-level paraphrase and an empty answer_summary.
- Forum years are estimated from thread id ranges and search snippets, not read from the pages.
- Autodesk help pages disagree on versions: search summaries said the new property-mapping GUI arrived in 2026.3, while the fetched What's New page lists it under Revit 2027; treated as 2027 here.
- Dynamo/API-side IFC questions, IFC import into editable families and Navisworks-specific IFC threads were thin in results.
- GitHub revit-ifc records are Autodesk-hosted but are a developer-leaning community, not the forum proper.
- No suspicious or pirated sites were encountered; none skipped. Posters' names and emails deliberately omitted.
