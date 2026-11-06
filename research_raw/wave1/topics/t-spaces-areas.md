# Spaces, rooms, areas, zones in IFC (IfcSpace export, room boundaries, area calculations, space boundaries for energy)
Cell: t-spaces-areas · Languages: English (real sources); synthetic prompts in en, de, ru, zh, es, pt, fr, ja, ko, it · Collected: 2026-11-06 · Records: 37 real / 18 synthetic · Communities covered: GitHub (Autodesk/revit-ifc, IfcOpenShell), forums.buildingsmart.org, community.osarch.org, qiita.com (one hit)

Note: the WebSearch budget was exhausted before any search ran, so everything below comes from direct fetches (GitHub CLI, Discourse search JSON, OSArch search pages) and is English-heavy.

## Top themes (ranked by frequency)
- Revit IfcSpace quantities wrong or missing: Net/Gross floor area identical or absent in Qto_SpaceBaseQuantities, varying by Revit/exporter version.
- Room/space geometry regressions after exporter updates (displaced rooms, ignored top/bottom bounding objects).
- 2nd level space boundaries (IfcRelSpaceBoundary2ndLevel) displaced, invalid virtual boundaries, missing for curtain walls, for energy (BEM) use.
- Rooms vs Areas vs Masses exported as IfcSpace (offsets, wrong units, LongName missing).
- IfcSpace PredefinedType / IfcSpaceType control (NOTDEFINED, 1:1 types), including national delivery rules (Chile).
- Link/open IFC in Revit: IfcSpace not turning into Rooms/Spaces, generic-model clutter.
- Custom psets for room data (area to custom pset blocked, German parameter names, map.txt overrides).
- Zones: IfcZone vs IfcSpatialZone, one space in several zones, unstable IfcZone IDs per export.
- Boundary placement for energy models: inside face vs centreline, gross vs net volumes, national methods.
- Authoring spaces in Bonsai/BlenderBIM: generate from walls, chimneys, fillets, roofs, boundary generation.
- Space-to-element relations: doors to rooms, containment of MEP in spaces, adjacency via boundaries.
- Spaces around stairs and slab-to-slab definition of IfcSpace volume.
- Verbose HVAC property sets on IfcSpace (Pset_SpaceThermalDesign etc.).

## What people want (the goals behind the questions)
- Trustworthy room areas and volumes in IFC that match the Revit schedule (Net vs Gross, per level totals).
- Rooms exported reliably with correct position, predefined type, long name and custom client psets.
- Space boundaries usable for energy simulation without manual cleanup.
- FM/CAFM handover: zone membership, door-to-room connectivity, room numbers.
- Linking an architect's IFC into MEP models so spaces become Rooms/Spaces.
- A way to override or extend standard Qto sets (vendor says immutable, use custom psets).
- Fast, automatic space generation in open-source authoring tools.

## How people write here
- GitHub issues: template headings (Problem Description, Revit Version, IFC for Revit Addon Version), screenshots instead of data, often one line ("Areas are exported as IfcSpace with offset").
- Prefix "PR:" in titles of Revit-IFC bug reports (problem report), "ENH:" enhancement, "INQ:" inquiry.
- Regression framing: "broken in 25.4.3", "introduced in latest 25.4.4 release".
- Typos in classes are common: "Qto_SpaceBaesQuantities".
- Non-native English with German parameter names in the text: "Tiefe x Hoehe", "German-language RVT".
- Polite closers ("Thanx in advance"), NDA caveats ("not allowed to share the model").
- Forum posts (buildingSMART) are longer, conceptual, option lists, cite entity names (IfcRelConnectsWithRealizingElements).
- Jargon: "room bounding", "2nd level boundaries", "BEM", "core center", "RVArch", "CV2", "proxy", "Qto".
- Illustrative fragments: "wall core center", "why are net and gross identical", "+1 same problem in 2022", "tried ExportAs to IfcSpace".

## Local ecosystem
- buildingSMART (IFC4.3, Qto_SpaceBaseQuantities, IfcSpace, IfcZone, IfcSpatialZone, IfcRelSpaceBoundary): https://forums.buildingsmart.org
- Autodesk IFC exporter for Revit (open source): https://github.com/Autodesk/revit-ifc
- IfcOpenShell and Bonsai/BlenderBIM: https://github.com/IfcOpenShell/IfcOpenShell , https://community.osarch.org
- Checkers: Solibri, BIMcollab Zoom (mentioned).
- Chile public delivery rule requiring IfcSpace PredefinedType (from issue 247).
- Belgian "Energy Level" method using gross volumes with outside-face envelope (forum 2724).
- EnergyPlus / CIBSE boundary conventions (forum 2724).
- Qiita (Japanese dev blog) example with IfcOpenShell: https://qiita.com/kiyuka/items/ef4b197fa28d3a96d068

## Notable sources
- https://github.com/Autodesk/revit-ifc/issues/742 Net vs Gross floor area identical
- https://github.com/Autodesk/revit-ifc/issues/529 NetFloorArea not exported Revit 2023
- https://github.com/Autodesk/revit-ifc/issues/751 FloorArea missing Revit 2022
- https://github.com/Autodesk/revit-ifc/issues/849 Base quantities IfcSpace IFC4x3
- https://github.com/Autodesk/revit-ifc/issues/865 Qto override question (German Revit)
- https://github.com/Autodesk/revit-ifc/issues/855 Room area to custom pset
- https://github.com/Autodesk/revit-ifc/issues/851 Areas as IfcSpace offset
- https://github.com/Autodesk/revit-ifc/issues/891 Room geometry export broken 25.4.3
- https://github.com/Autodesk/revit-ifc/issues/923 Horizontal displacement of rooms
- https://github.com/Autodesk/revit-ifc/issues/961 2nd level boundary displaced
- https://github.com/Autodesk/revit-ifc/issues/243 Invalid virtual boundary
- https://github.com/Autodesk/revit-ifc/issues/107 Space boundary not generated
- https://github.com/Autodesk/revit-ifc/issues/15 Link IFC IfcSpace to Room
- https://github.com/Autodesk/revit-ifc/issues/247 IfcSpace PredefinedType
- https://github.com/Autodesk/revit-ifc/issues/494 IfcSpaceType control
- https://github.com/Autodesk/revit-ifc/issues/671 Best class for Areas
- https://github.com/IfcOpenShell/IfcOpenShell/issues/6668 Space boundaries wrong in Bonsai
- https://github.com/IfcOpenShell/IfcOpenShell/issues/8570 ifc5d no IfcSpace quantities
- https://github.com/IfcOpenShell/IfcOpenShell/issues/10051 Generate Space from Cursor
- https://forums.buildingsmart.org/t/level1-boundary-generation-to-the-centre-line-or-inside-face/2724 BEM boundary placement
- https://forums.buildingsmart.org/t/space-data-depending-on-zone/4434 space in several zones
- https://forums.buildingsmart.org/t/relation-between-doors-to-rooms/3961 doors to rooms
- https://forums.buildingsmart.org/t/propertysets-of-ifcspace/3997 IfcSpace property sets critique
- https://forums.buildingsmart.org/t/ifcspace-and-ifcstair/1451 space around stairs
- https://community.osarch.org/discussion/comment/30080 IfcSpace and BlenderBim

## Gaps
- WebSearch was unavailable (budget exhausted), so no native-language community was actually searched; only English sources are real. All ru/zh/de/es/pt/fr/ja/ko/it content is synthetic except one Japanese Qiita snippet.
- Not accessible: forums.autodesk.com (403 on search), community.graphisoft.com (403), stackoverflow.com and api.stackexchange.com (blocked), dwg.ru, cnblogs.com, cad.de (404), juejin.cn (no results rendered), zhihu/csdn not tried.
- Reddit not queried. Several forum records are snippet-level only (evidence "snippet").
- No suspicious or pirated sites were encountered. A second pass with working search is needed for Russian, Chinese, Spanish, Portuguese, German, French, Korean and Italian sources.
