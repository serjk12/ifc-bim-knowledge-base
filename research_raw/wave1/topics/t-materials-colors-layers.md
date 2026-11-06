# Materials, colours, layers lost or wrong in IFC

Cell: t-materials-colors-layers · Languages: English (real sources); synthetic prompts in ru, zh, es, pt, de, fr, ja, ko, it · Collected: 2026-11-06 · Records: 35 real / 17 synthetic · Communities covered: Autodesk/revit-ifc GitHub, ThatOpen/web-ifc GitHub, IfcOpenShell GitHub, xBimTeam GitHub, FreeCAD GitHub, buildingSMART forums, OSArch community.

## Top themes (ranked by frequency)
- Colours lost or grey after Revit export (MEP, fittings, IFC4 vs IFC2x3): view filters and graphic overrides are not exported.
- Revit exports system material (e.g. SEWER) instead of the real material (PVC, copper).
- Layered walls/floors: layer sets reduced to constituent sets (IFC4 Reference View) or a single material; custom families output only one layer.
- Same colour shown differently in different viewers (Solibri, ArchiCAD, Revit, BIMcollab); transparency often ignored.
- Where colour actually lives: IfcMaterial is only a name; colour needs IfcSurfaceStyle via styled item; shape style beats material style.
- Type vs occurrence: material or style on the type not applied to occurrences in viewers.
- Developer pain: web-ifc, IfcOpenShell, Xbim not resolving styles (multiple styled items, definition representations, profile sets, append_asset).
- Request to colour by parameter/view/room scheme/rebar diameter in IFC.
- Presentation layers (IfcPresentationLayerAssignment): duplicate names, mapping from CAD layers, little viewer use.
- Duplicate or bloated material lists from other exporters (Allplan).
- Hatches/2D appearance of layers in Bonsai drawings.

## What people want (the goals behind the questions)
- Colours and materials surviving round-trips between authoring tools and viewers.
- Colour-coding by system, diameter, room or parameter for coordination, without custom hacks.
- Correct layer build-up (names, thickness) for quantities, U-values and drawings.
- Ways to audit a file: which elements lack material/style, where the loss happened (exporter, schema, viewer).
- Scripted fixes: assign styles, merge duplicate materials, normalise layer sets.

## How people write here
- GitHub issue titles are terse, prefixed (INQ:, ENH:, PR:, Bug:), sometimes lowercase with no punctuation ("whats the root cause of grey MEP-components in IFC").
- Mix of British/American spelling in one title ("colour/ color").
- Users give version info (Revit 2024.3, exporter 24.3.2, Windows 11) but often omit the IFC schema or MVD.
- Developers quote entity names exactly (IfcSurfaceStyleShading, IfcRelDefinesByType) and attach repro scripts.
- Forum posts by beginners are polite and long; experts reply with entity chains and ask "attach the IFC file".
- Tone: mildly frustrated, resigned ("Revit does not display colour nor transparency"); often ends with +1 on open issues.
- Native-language fragments were not obtainable in this run; synthetic prompts imitate brevity and slang (ru "ифс", "глянь", zh "帮我查下").

## Local ecosystem
- Autodesk revit-ifc exporter (Jira tickets REVIT-xxxx mirrored in issues): https://github.com/Autodesk/revit-ifc
- buildingSMART forums and MVDs (Reference View, Design Transfer View, implementer agreements): https://forums.buildingsmart.org
- IfcOpenShell / Bonsai (BlenderBIM): https://github.com/IfcOpenShell/IfcOpenShell
- That Open Company web-ifc and fragments: https://github.com/ThatOpen/engine_web-ifc
- Xbim Essentials: https://github.com/xBimTeam/XbimEssentials
- FreeCAD BIM: https://github.com/FreeCAD/FreeCAD
- OSArch community: https://community.osarch.org
- Viewers named by users: Solibri, BIMcollab Zoom, BIMvision, KITModelViewer, SimpleBIM, Allplan, ArchiCAD.

## Notable sources
- https://forums.buildingsmart.org/t/ifc-textures-and-colors-current-situation/2862 - inventory of colour/texture entities and support
- https://forums.buildingsmart.org/t/why-is-it-so-difficult-to-get-colors-to-show-up/2312 - viewer inconsistency, precedence rule
- https://forums.buildingsmart.org/t/where-and-how-will-my-colors-be-saved-in-ifc/1806 - Allplan colours lost
- https://forums.buildingsmart.org/t/how-can-i-control-the-ifc-pipes-colors-revit-to-archicad/2729 - pipe colours Revit to ArchiCAD
- https://forums.buildingsmart.org/t/why-are-material-layer-sets-excluded-from-ifc4-reference-view-mvd/3638 - RV and layer sets
- https://forums.buildingsmart.org/t/how-does-multiple-ifcpresentationlayerassignment-with-the-same-name-work/3126 - presentation layers
- https://forums.buildingsmart.org/t/ifc-materials/4861 - which material entity
- https://github.com/Autodesk/revit-ifc/issues/579 - grey MEP
- https://github.com/Autodesk/revit-ifc/issues/577 - system vs actual material
- https://github.com/Autodesk/revit-ifc/issues/731 - export view colours
- https://github.com/Autodesk/revit-ifc/issues/610 - layered material pset IFC4
- https://github.com/Autodesk/revit-ifc/issues/929 - multi-material family
- https://github.com/Autodesk/revit-ifc/issues/75 - colour by parameter
- https://github.com/Autodesk/revit-ifc/issues/92 - inconsistent colours
- https://github.com/ThatOpen/engine_web-ifc/issues/1793 - IFC4 loses colours
- https://github.com/ThatOpen/engine_web-ifc/issues/2235 - type material not applied
- https://github.com/IfcOpenShell/IfcOpenShell/issues/8662 - append_asset drops styles
- https://github.com/IfcOpenShell/IfcOpenShell/issues/10111 - multiple styled items
- https://github.com/xBimTeam/XbimEssentials/issues/543 - colouring AutoCAD items
- https://github.com/xBimTeam/XbimEssentials/issues/642 - retrieving materials and colours
- https://community.osarch.org/discussion/comment/30460 - layered walls in BlenderBIM

## Gaps
- WebSearch budget was exhausted at the start (all searches refused), so no keyword search of the web was possible. Sources came from site-internal search endpoints (buildingSMART Discourse search.json), the GitHub search API via fetch, and direct page fetches. gh CLI hit a rate limit.
- No native-language (ru, zh, es, pt, de, fr, ja, ko, it) real posts obtained: dwg.ru search returned garbled markup, cnblogs search 404, Autodesk and Graphisoft community searches returned 403, Stack Overflow and Stack Exchange API blocked, Qiita API returned irrelevant results. Non-English entries are therefore synthetic only.
- Not covered: forums.autodesk.com threads, community.graphisoft.com, Reddit, csdn/zhihu, YouTube/blogs.
- Several records are snippet-only (marked evidence "snippet"); years for some OSArch posts are estimated.
- No suspicious or pirated sites encountered.
