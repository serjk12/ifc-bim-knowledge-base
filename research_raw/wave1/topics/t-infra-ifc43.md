# IFC 4.3 infrastructure: alignment, roads, rail, bridges, tunnels
Cell: t-infra-ifc43 · Languages: English only in practice (planned ru/zh/es/pt/de/fr/ja/ko/it not reachable, see Gaps); synthetic prompts are written in en/ru/zh/de/es/pt/fr/ja/ko/it · Collected: 2026-11-06 · Records: 36 real / 18 synthetic · Communities covered: forums.buildingsmart.org (Discourse), GitHub issues (IfcOpenShell/Bonsai, ThatOpen web-ifc)

Note: the WebSearch budget was exhausted before the first search ran. All real records come from direct page fetches, the buildingSMART forum's own search.json endpoint and `gh` issue search. 22 are read pages, 14 are title-only snippets.

## Top themes (ranked by frequency)
- Stationing/chainage vs DistanceAlong, IfcReferent STATION, Pset_Stationing, removal of StartDistAlong
- Alignment geometry implementation (IfcGradientCurve, IfcSegmentedReferenceCurve, clothoids, cant) in viewers and libraries
- Viewers and libraries failing to show alignments or sectioned solids/surfaces (web-ifc, Bonsai, Civil 3D)
- IfcLinearPlacement and IfcAxis2PlacementLinear: placing signals, piers, rail parts along an alignment
- Spec/documentation inconsistencies and missing examples (Axis attribute, cross-section orientation, Alignment Based view status)
- Sample files and validation for bridges, rail and roads (ifcinfra.de, IFC-Rail samples, bSI validation service)
- Schema version confusion: 4.1 and 4.2 withdrawn, 4.3 vs ADD2 identifiers, Unsupported schema errors
- Class mapping: getting from BuildingElementProxy to IfcRoad/IfcBridge/IfcRailway/IfcCourse
- Spatial structure of facilities (IfcFacility, IfcFacilityPart, IfcBridgePart, IfcRailwayPart)
- Authoring alignments from code or CSV (ifcopenshell.api.alignment, cogo, transition curves)
- National data into IFC (German DB GIS/GNEDIT, Spanish rail classification, US station/offset)
- Geotechnics (IfcBorehole) and terrain as add-ons to infra models

## What people want (the goals behind the questions)
- Exchange a road/rail corridor between design tools without losing alignment, stationing, cross sections
- Position equipment (signals, sleepers, piers) by station and offset along an alignment
- Know which view/MVD to implement (Alignment Based view) and find test files that pass validation
- Read or generate alignment geometry programmatically (python, web)
- Quantities from sweeps and courses (volumes of pavement layers, tunnel solids)
- Convert legacy or national formats into IFC 4.3 and get correct classes instead of proxies

## How people write here
- Developer-heavy audience: precise entity names (IfcAlignmentHorizontalSegment, IfcReferent), spec section numbers, pasted tracebacks; little emotion except "it's not clear why it is not working".
- Short bug reports with no versions ("Unable to assign ifc railway part"), maintainers then ask for file and version.
- Civil jargon: station, chainage, "15+00", cant, superelevation, clothoid, spiral, PI, P.C./P.T./P.V.C., kilo-point.
- Misspellings seen: "convertig", "doesnt", "IFCRoad", "alignement", "BBIM".
- Openers rare; closers like "Thanks in advance"; polite academic framing from students ("could discuss for 30 minutes").
- Fragments: "station 15+00 landed 1500 ft", "painful BuildingElementProxy", "exports are shot in the dark".
- Synthetic prompts mimic lowercase, mixed English terms ("пикетаж", "Trassierung", "線形") and missing context.

## Local ecosystem
- buildingSMART International Infrastructure Room, IFC 4.3 docs: https://ifc43-docs.standards.buildingsmart.org/
- Sample models: https://github.com/buildingSMART/IFC4.3.x-sample-models , IFC-Rail samples https://github.com/bSI-RailwayRoom/IFC-Rail-Sample-Files
- Germany: IFC-Infra by planen-bauen 4.0 (BMVI): https://ifcinfra.de/ (alignment, bridge, tunnel, rail, road, ports)
- Spain: buildingSMART Spain events, SCF railway classification, ACCA Bridge-for-MINnD model
- US: TPF-5(372) unit test suite for bridges; station/offset practice
- Korea: buildingSMART Korea site (no infra content found): http://www.buildingsmart.or.kr
- Open source: IfcOpenShell/Bonsai https://github.com/IfcOpenShell/IfcOpenShell , web-ifc/That Open https://github.com/ThatOpen/engine_web-ifc , RickBrice IFC alignment geometry implementation guide (GitHub)
- Software mentioned: Civil 3D, ProVI, Desite MD Pro, 12d, ODA Open IFC Viewer, Revit (as web-ifc test input)

## Notable sources
- https://forums.buildingsmart.org/t/understanding-ifc-alignment-and-rail-beginners-guide/4117
- https://forums.buildingsmart.org/t/ifc-4x1-file-containing-alignment-is-not-opening-in-civil-3d/3830
- https://forums.buildingsmart.org/t/startdistalong-in-ifcalignmenthorizontal-4-3-rc2/5118
- https://forums.buildingsmart.org/t/new-alignment-and-need-for-stations-and-offsets/3330
- https://forums.buildingsmart.org/t/how-is-it-possible-to-import-german-rail-ver-esn-or-gnedit-in-ifc/2835
- https://forums.buildingsmart.org/t/alignment-based-reference-view/6414
- https://forums.buildingsmart.org/t/orientation-of-cross-sections-in-ifcsectionedsolidhorizontal-defined-by-ifcaxis2placementlinear/4696
- https://forums.buildingsmart.org/t/new-ifc-4x2-3-bridge-file-examples/5218
- https://forums.buildingsmart.org/t/ifcalignment-axis-documentation-is-not-consistent-with-express-file-or-unit-tests/3695
- https://forums.buildingsmart.org/t/exchange-road-network-with-ifc/1545
- https://github.com/IfcOpenShell/IfcOpenShell/issues/3464
- https://github.com/IfcOpenShell/IfcOpenShell/issues/4933
- https://github.com/IfcOpenShell/IfcOpenShell/issues/6254
- https://github.com/IfcOpenShell/IfcOpenShell/issues/7621
- https://github.com/IfcOpenShell/IfcOpenShell/issues/8116
- https://github.com/IfcOpenShell/IfcOpenShell/issues/4921
- https://github.com/IfcOpenShell/IfcOpenShell/issues/6888
- https://github.com/IfcOpenShell/IfcOpenShell/issues/5049
- https://github.com/IfcOpenShell/IfcOpenShell/issues/3098
- https://github.com/IfcOpenShell/IfcOpenShell/issues/6886
- https://github.com/IfcOpenShell/IfcOpenShell/issues/7456
- https://github.com/ThatOpen/engine_web-ifc/issues/878
- https://github.com/ThatOpen/engine_web-ifc/issues/926
- https://ifcinfra.de/

## Gaps
- The WebSearch quota was used up before any search ran, so no native-language community (dwg.ru, csdn, cnblogs, zhihu, cad.de, qiita, Spanish/Portuguese forums, reddit, stackoverflow, Autodesk forums) could be searched. All real records are English; ru/zh/de/es/pt/fr/ja/ko/it content exists only as synthetic prompts.
- Qiita tag page, cnblogs search and Autodesk forum search returned no usable content (404/403/no list); OSArch search was empty (site migrating).
- buildingSMART forum search.json was rate-limited (429) partway; GitHub API rate-limited later, so buildingSMART/IFC4.3.x-development and sample-models issues were not read.
- 14 real records are title-only snippets (evidence "snippet").
- No suspicious or pirated sites were encountered.
