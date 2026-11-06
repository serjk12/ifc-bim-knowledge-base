# Contractors, site teams and estimators/QS using IFC (quantities, 4D, field viewing)
Cell: p-contractor-estimator · Languages: English only in practice (native-language searches could not be run) · Collected: 2026-11-06 · Records: 22 real / 18 synthetic · Communities covered: GitHub (IfcOpenShell/Bonsai issues), community.osarch.org

## Top themes (ranked by frequency)
- Wrong or inconsistent QTO values (areas, volumes) compared with other tools such as Solibri or Blender
- Gross vs net quantities, openings baked into meshes vs modelled voids
- Cost schedules / BoQ from IFC (5D): rates, rounding, totals, parent-child sums
- Assigning model elements to cost items via queries/selectors instead of manual selection
- CSV round-trip of BoQ and work schedules (import crashes, optional columns)
- 4D animation of tasks (construct, demolish, move) and what IFC can express
- Comparing with commercial 4D tools (Synchro, Fuzor, P6 import)
- Weight/steel quantities from profiles (MassPerLength) at low LOD
- Heavy files and viewing on site (not covered by found sources, see Gaps)
- Version comparison between design revisions for re-pricing (synthetic only)

## What people want (the goals behind the questions)
- Trustworthy numbers to price from, and to know which quantity (net/gross) they are looking at
- A repeatable BoQ/cost schedule linked to the model that survives file reloads and revisions
- Schedule-linked visualisation (4D) that matches what Synchro/Fuzor show
- Fewer manual steps when linking elements to cost items or tasks
- Ability to record actual and unplanned costs alongside model-driven quantities

## How people write here
- Register: terse bug-report or forum style; screenshots and attached sample IFC carry the context.
- Openers: "Hi all", "please find attached"; closers: "by the way, thanks", "please advise".
- Jargon: BoQ, QTO, takeoff, 4D, 5D, cost item, formwork, LOD200, rate, work schedule, P6.
- Context given: software version, element class, screenshot; often omitted: IFC schema version and export settings.
- Fragments: "4D simulation im export to glb ... not working"; "gross side area = net side area"; "total in the BoQ is one too many".
- Tone mostly neutral to confused; practical estimator reasoning (e.g. file size vs accuracy).

## Local ecosystem
- Open source: IfcOpenShell / Bonsai (cost, 4D, QTO modules) https://github.com/IfcOpenShell/IfcOpenShell
- OSArch community https://community.osarch.org
- Commercial tools mentioned: Solibri, Synchro, Fuzor, Primavera P6, Navisworks
- Native-language ecosystems (dwg.ru, CSDN, cad.de, Qiita etc.) not researched, see Gaps.

## Notable sources
- https://github.com/IfcOpenShell/IfcOpenShell/issues/9235 - gross vs net side area against Solibri
- https://github.com/IfcOpenShell/IfcOpenShell/issues/5349 - QTO difference window mesh
- https://github.com/IfcOpenShell/IfcOpenShell/issues/6401 - cost calculation discrepancy
- https://github.com/IfcOpenShell/IfcOpenShell/issues/6344 - MassPerLength weight
- https://github.com/IfcOpenShell/IfcOpenShell/issues/2050 - synced animated timelines vs Fuzor/Synchro
- https://github.com/IfcOpenShell/IfcOpenShell/issues/2413 - 4D animation bug
- https://github.com/IfcOpenShell/IfcOpenShell/issues/3738 - 4D in GLB
- https://github.com/IfcOpenShell/IfcOpenShell/issues/5155 - product resource wrong quantity
- https://github.com/IfcOpenShell/IfcOpenShell/issues/5390 - query filter for cost item quantities
- https://github.com/IfcOpenShell/IfcOpenShell/issues/6616 - regex in cost schedule property
- https://github.com/IfcOpenShell/IfcOpenShell/issues/7354 - sum of total costs in parent items
- https://github.com/IfcOpenShell/IfcOpenShell/issues/8580 - work schedule CSV import crash
- https://community.osarch.org/discussion/2887/dynamic-csv-to-cost-schedule-now-available - CSV cost schedule discussion
- https://community.osarch.org/discussion/1131/ifcopenshell-python-ifctask-predefinedtype-construction-demolition-move - MOVE task in 4D

## Gaps
- The web search budget for the session was exhausted before any WebSearch could run, so no searches were possible for forums.autodesk.com, buildingSMART forums, Graphisoft, Stack Overflow, Reddit, or any non-English community (Russian, Chinese, Spanish, Portuguese, German, French, Japanese, Korean, Italian). Only GitHub (gh) and two OSArch pages were reachable; GitHub API rate limit then blocked searches in web-ifc, xbim and revit-ifc.
- Real records are therefore English-only and mostly IfcOpenShell/Bonsai-centred (open-source users), which over-represents that community; Revit/Navisworks/Synchro/Trimble field users are underrepresented.
- 7 real records are title-only (evidence "snippet"); well under the 25-record minimum and fewer than the 20 tool calls requested.
- Synthetic records in ru/de/es/pt/zh/fr/ja/ko/it are modelled from knowledge, not from observed native-language posts; their phrasing should be treated as unverified.
- No suspicious sites encountered.
