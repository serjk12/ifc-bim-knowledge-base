# Structural and MEP engineers: IFC needs and questions
Cell: p-engineers · Languages: English only in practice (native-language searches in ru/zh/es/pt/de/fr/ja/ko/it were NOT possible, see Gaps) · Collected: 2026-11-06 · Records: 33 real / 17 synthetic · Communities covered: forums.buildingsmart.org, GitHub issues (Autodesk/revit-ifc, IfcOpenShell, ThatOpen/engine_web-ifc), community.osarch.org

## Top themes (ranked by frequency)
- MEP unit and scale errors on export (flow in m3/s vs m3/h vs L/s vs ft3/s; airflow values wrong scale).
- Systems: IfcSystem grouping, psets on systems, system material replacing real material, grey or uncoloured MEP elements.
- Structural analysis model (IfcStructuralAnalysisModel, curve members, point connections) exported but not visible in viewers or imported by anyone.
- Sharing analysis results/loads via IFC (STAAD, ETABS, Robot, RFEM, SAP2000) and no viewer or receiving software support.
- Classification choices for MEP parts (fitting types such as CONNECTOR vs TRANSITION, ports, IfcRelNests).
- Rebar: groups, cover/spacing, lap lengths, fabricated vs installed shapes, IFC4.3 reinforcement.
- Which MVD/view to use (Reference View, Coordination View 2.0, Structural Analysis View) and certification status.
- Multi-discipline federation: separate IFC per discipline, duplicated spatial structure, who is master.
- Clash detection between MEP and structure; reproducible clash points.
- Authoring MEP/structure in open tools (Bonsai): routing, fittings, loads, solvers.
- Viewer and parser robustness on big MEP files (web-ifc crashes, missing pipe geometry).
- Eurocode/national checks on analysis models.

## What people want (the goals behind the questions)
- Trustworthy values: correct units, true materials, properties surviving export so downstream calculation and coordination work.
- A usable structural analysis exchange: model plus loads plus results, viewable by clients without the analysis package.
- Clear rules on which IFC entity or enum to use for a physical part, and which export view to pick.
- Discipline models (struct, MEP) that load and federate with the architect model without duplicated storeys or missing geometry.
- Quantities (rebar weights, concrete volumes, duct lengths by system) and clash lists straight from the IFC.
- Open-source authoring and checking tools for engineering (loads, solver, code checks).

## How people write here
- Register: technical, concise, forum or issue-tracker style; many name exact entities (IfcRelNests, AppliedCondition) and software versions. GitHub issues often auto-templated with tracebacks.
- Typical length: 2-8 sentences for questions; MEP issues often a single line ("Revit cannot export properties of an IfcSystem").
- Jargon: MVD, CV2.0, Reference View, psets, "analysis axes", "rigid link", "system material", "ports".
- Non-native English is common: "I want to know that it is possible to put geometrical data..." ; typos in titles ("Load Strucutral ifc"); run-on feature requests.
- Little context given: often no Revit or IFC version stated; users attach files or screenshots instead.
- Tone: mostly neutral/curious; frustration when units or materials are semantically wrong ("a pipe is made of copper, not hot water supply"); urgency where a live project is affected.
- Short fragments: "whats the root cause of grey MEP-components", "Flow Units export not correct".

## Local ecosystem
- buildingSMART International: IFC4 Add2 structural analysis domain docs, IFC4.3 (https://standards.buildingsmart.org/IFC/RELEASE/IFC4_3/HTML/), Implementation Database, MVD certification (Revit IFC4 RV1.2 MEP finished April 2022).
- Open source: Autodesk revit-ifc exporter (https://github.com/Autodesk/revit-ifc), IfcOpenShell/Bonsai (https://github.com/IfcOpenShell/IfcOpenShell), ThatOpen web-ifc (https://github.com/ThatOpen/engine_web-ifc), Code_Aster, PyNite, FreeCAD, Ifc2CA, GeometryGym.
- Commercial tools named: ETABS, STAAD, ISM, RFEM, SAP2000, SCIA, Tekla, Robot, MagiCAD, Bausoft CAD (German), Solibri, Navisworks.
- Standards: Eurocodes and National Annexes, Spain CTE (OSArch thread).
- Communities: https://forums.buildingsmart.org, https://community.osarch.org

## Notable sources
- https://forums.buildingsmart.org/t/ifc-structural-analysis-view/1267 - ETABS export with no geometry
- https://forums.buildingsmart.org/t/ifcstructuralanalysisdomain/832 - STAAD results via IFC
- https://forums.buildingsmart.org/t/supported-data-type-volumetricflowrate-m-h/4189 - flow units MEP
- https://forums.buildingsmart.org/t/ifc-files-that-reference-one-another/1804 - federation
- https://forums.buildingsmart.org/t/rigid-link-representation-in-structural-analysis-model/1364
- https://forums.buildingsmart.org/t/user-defined-point-connection-between-structural-elements-structural-analysis-domain/2633
- https://forums.buildingsmart.org/t/best-ifc-classification-for-a-reducing-coupling/5963
- https://forums.buildingsmart.org/t/field-bent-rebar/5870
- https://forums.buildingsmart.org/t/there-is-a-need-for-a-reinforcing-bar-group/5688
- https://forums.buildingsmart.org/t/reinforcingbar-lap-lengths/6430
- https://github.com/Autodesk/revit-ifc/issues/579 - grey MEP components
- https://github.com/Autodesk/revit-ifc/issues/577 - system material
- https://github.com/Autodesk/revit-ifc/issues/523 - IfcSystem psets
- https://github.com/Autodesk/revit-ifc/issues/444 - flow units
- https://github.com/Autodesk/revit-ifc/issues/237 - airflow scaling
- https://github.com/Autodesk/revit-ifc/issues/357 - IFC4 MEP certification
- https://github.com/Autodesk/revit-ifc/issues/162 - ports
- https://github.com/IfcOpenShell/IfcOpenShell/issues/6138 - clash points
- https://github.com/IfcOpenShell/IfcOpenShell/issues/9866 - structural analysis in Bonsai
- https://github.com/ThatOpen/engine_web-ifc/issues/948 - structural analytical items
- https://github.com/ThatOpen/engine_web-ifc/issues/1999 - large MEP crash
- https://community.osarch.org/discussion/3699/structural-analysis-in-bonsai-what-im-working-on

## Gaps
- The WebSearch budget for the session was exhausted before any search ran, so zero web searches were done; all material came from direct fetches (buildingSMART forum search endpoint, GitHub CLI, specific pages). Search-engine breadth is missing.
- No native-language content (ru, zh, es, pt, de, fr, ja, ko, it) was reached: dwg.ru and Habr search pages returned nothing usable, Qiita API rate-limited or irrelevant, cnblogs search 404. Non-English synthetic prompts are therefore based on general knowledge, not observed phrasing. Needs a follow-up pass.
- forums.autodesk.com returned 403; reddit, Graphisoft, Stack Overflow, zhihu, csdn not attempted.
- Several buildingSMART records (snippet evidence) show only titles or reply fragments, not the opening post.
- No suspicious or piracy sites were encountered.
