# GitHub: Autodesk/revit-ifc exporter issues
Cell: en-gh-revit-ifc · Languages: English · Collected: 2026-11-06 · Records: 59 real / 16 synthetic · Communities covered: GitHub Autodesk/revit-ifc issues (bug reports "PR:", inquiries "INQ:", enhancements "ENH:"), 2018-2026

## Top themes (ranked by frequency)
- Property sets: user-defined pset txt files, Revit parameters not exported, type vs instance params, "(Type)" suffix, Revit 2027 new Manage Property dialog
- Regressions between exporter builds (25.4.x, 26.4.x, 27.x): geometry, joins, curtain walls, rooms
- Spaces/rooms: displaced IfcSpace, wrong height or elevation, areas as IfcSpace, room-bounding relationships
- Coordinates and georeferencing: IfcMapConversion/ProjectedCRS, IFC2x3 psets, survey vs project base point, Z offsets, true vs grid north
- Link IFC / Open IFC problems: double Z offset, hangs, stray points, IfcSpace not becoming Room
- IFC class mapping: IfcBuildingElementProxy fallbacks, IfcExportAs, fascias/sweeps, per-model DataStorage mapping
- Crashes and unrecoverable errors, large models, Design Automation
- Export performance and slow property export
- GlobalId stability: duplicates across files, phase changes, UniqueId coupling, linked-file federation
- IFC4 / IFC4x3 specifics: Reference View header, AdvancedBrep, quantity sets, predefined type enums
- MEP: system vs real material, grey colours, flow units
- Rebar and steel connections: rounding, text-prefixed values, API-built containers
- Colours/materials and view-based export requests
- Type generation: duplicate IfcTypes per Revit type

## What people want (the goals behind the questions)
- Predictable, documented mapping of Revit parameters and categories to IFC classes and psets
- Stable GUIDs so external databases and revisions survive re-export
- Correct placement/georeferencing so models federate with other disciplines
- Exports that do not regress between add-in versions, and clear error reports instead of silent loss
- Faster exports and partial-failure tolerance
- IFC4/4.3 features (quantities, reference view) equal to IFC2x3 reliability
- Round-tripping: IFC links that become usable Revit elements (rooms, spaces)

## How people write here
- Register: technical and terse; structured templates (Problem Description, Revit Version, Add-in Version, Windows Version).
- Length: from one line to long reproductions with version comparison tables.
- Jargon: "Pset", "proxy", "DTV" (Design Transfer View), "RV" (Reference View), "CV2" (Coordination View 2.0), "UDPS", "Link IFC" vs "Open IFC", "base point", "survey point".
- Fragments: "Floors not exporting"; "Fast export"; "Thanks already!"; "Hello IFC gurus"; "unacceptable in a production environment"; "22.4.2 ok, 23.2.3 not ok".
- Version strings are central: add-in 25.4.40.17, Revit 2027.3, REVIT-xxxxx Jira ids reposted by bot.
- Context given: screenshots, test rvt links (file transfer), IFC snippets with entity numbers; often missing: sample file or exact settings, prompting maintainer "we need the file".
- Tone: mostly neutral/frustrated about regressions; politeness markers; code-switching in non-native phrasing (decimal commas, "Hallo all").

## Local ecosystem
- Autodesk revit-ifc repo and wiki: https://github.com/Autodesk/revit-ifc , https://github.com/Autodesk/revit-ifc/wiki/Revit-IfcExporter-parameter-expression
- Revit Public Roadmap (Trello): https://trello.com/b/ldRXK9Gw/revit-public-roadmap
- buildingSMART standards: IFC2x3 CV2.0, IFC4 RV/DTV, IFC4.3 (ISO 16739); bSI forums https://forums.buildingsmart.org/
- Viewers/checkers named: Solibri, BIMcollab ZOOM, BIM Vision, xBIM Xplorer, Trimble Connect, Navisworks
- Open source: IfcOpenShell / BlenderBIM (ifcpatch recipes), OSArch wiki on Revit geolocation https://wiki.osarch.org/index.php?title=Revit_geolocation
- Other tools: Dynamo, Tekla, ArchiCAD, 12D, simpleBIM

## Notable sources
- https://github.com/Autodesk/revit-ifc/issues/1015 beam spacing unit bug
- https://github.com/Autodesk/revit-ifc/issues/752 psets per predefined type
- https://github.com/Autodesk/revit-ifc/issues/960 Category as user pset
- https://github.com/Autodesk/revit-ifc/issues/984 Revit 2027 property dialog
- https://github.com/Autodesk/revit-ifc/issues/582 missing type params
- https://github.com/Autodesk/revit-ifc/issues/676 auto-generated proxy types
- https://github.com/Autodesk/revit-ifc/issues/759 floors not exporting
- https://github.com/Autodesk/revit-ifc/issues/481 proxy override
- https://github.com/Autodesk/revit-ifc/issues/924 room geometry shifted
- https://github.com/Autodesk/revit-ifc/issues/907 rooms wrong elevation
- https://github.com/Autodesk/revit-ifc/issues/990 Link IFC Z coordinate
- https://github.com/Autodesk/revit-ifc/issues/462 IFC2x3 georeferencing
- https://github.com/Autodesk/revit-ifc/issues/177 doubled georeferencing
- https://github.com/Autodesk/revit-ifc/issues/321 true north on import
- https://github.com/Autodesk/revit-ifc/issues/378 GlobalIds not unique
- https://github.com/Autodesk/revit-ifc/issues/480 IfcAdvancedBrep
- https://github.com/Autodesk/revit-ifc/issues/492 slow export
- https://github.com/Autodesk/revit-ifc/issues/577 system material
- https://github.com/Autodesk/revit-ifc/issues/1013 Reference View header
- https://github.com/Autodesk/revit-ifc/issues/992 curtain wall crash
- https://github.com/Autodesk/revit-ifc/issues/768 IFC4x3 quantities
- https://github.com/Autodesk/revit-ifc/issues/880 linked files in one IFC
- https://github.com/Autodesk/revit-ifc/issues/14 rebar rounding

## Gaps
- Only issues of this one repo; no Discussions, PR threads or forums read. Closed issues only sampled. Comments read partially (first two). Poster identities deliberately omitted. Maintainer replies in 2026 appear bot-assisted. No suspicious sites encountered; attachment links (file transfer, OneDrive) not opened.
