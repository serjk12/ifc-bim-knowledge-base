# Architects: IFC questions (exporting for consultants, receiving consultant IFCs, permits)
Cell: p-architect · Languages: en, ru, zh, es, de, fr, ja, ko, it (pt only synthetic) · Collected: 2026-11-06 · Records: 48 real / 19 synthetic · Communities covered: Autodesk Community (Revit), Graphisoft Community (Archicad), OSArch, buildingSMART Forums, dwg.ru, GitHub Autodesk/revit-ifc, CSDN, note.com (JP), official permit portals (CORENET X SG, Geneva, Shanghai, Dubai Municipality), Korean academic papers

Note on evidence: Autodesk and Graphisoft community pages returned HTTP 403 to fetch, so those records are "snippet" (search-result text), not full-thread reads. Paraphrases stay close to titles and snippet text.

## Top themes (ranked by frequency)
- Archicad <-> Revit IFC round trip: architect on Archicad, consultants on Revit; elements arrive as generic models, proxies, breps or lose data.
- Class mapping on export: structural framing, columns, beams, ceilings (IfcCovering) landing in the wrong class or IfcBuildingElementProxy.
- "Which translator / export settings should I use for the structural or MEP engineer" (Revit Structure translator, MEP translator, IfcExportAs, mapping table).
- Missing or shifted elements after export/link (linked models not exported, view range, phase filter, columns displaced, floating location lines).
- Coordinates, base point, storey elevations and levels tied to 0,0,0 instead of survey point; "model lands far away".
- Permit and authority submissions: IFC-SG/CORENET X (Singapore), Geneva deposit standard, Japan BIM drawing review (PDF + IFC), Shanghai EDM vs IFC, Dubai DM template, Korea Seumteo.
- Receiving consultant IFC and updating it (relinking a new version, GUID stability, comparing versions).
- Export crashes, hangs and slow exports (Archicad exchange plugin for Revit 2024, 50% crash, slow property export).
- Analytical vs physical model: whether analytical elements go through IFC to ETABS/Lira/STARK.
- Properties and quantities: psets, base quantities wrong, fire ratings, room numbers/areas required for submission.
- Opening/door/window handling (voids, door footprints, IfcOpeningElement sizing).
- Native vs IFC expectation: "IFC is for coordination/reference, not handover of an editable model".
- File size and performance when linking large Tekla/MEP IFCs into Revit.
- Open-source authoring (BlenderBIM/Bonsai, FreeCAD, FME, IfcOpenShell) feeding Revit/Archicad.

## What people want (the goals behind the questions)
- Hand a consultant a model they can open and use without remodelling; know the one right export setting.
- Avoid proxies/generic models so the engineer gets real structural categories.
- A pre-flight check before sending or uploading to an authority: classes, levels, coordinates, rooms, psets.
- Receive a consultant IFC that lands in the right place, at the right levels, and can be re-linked on update.
- Know exactly what an authority wants (version, standard, validator, viewer) and how to satisfy it from Revit or Archicad.
- Repeatable one-click IFC output (layer sets, saved views, export setups).
- An honest answer on what IFC cannot do (round-trip editing, analytical model, phasing).

## How people write here
- English forums: short symptom-first titles ("X not exporting", "IFC import problem - ceilings, walls"); version in title ("Archicad 25", "Revit 2024"); little or no BEP/context; often no IFC schema stated.
- Typical post 2-6 sentences; replies ask for translator, versions, mapping table, screenshot, file.
- Vocabulary: "consultants", "the structural guys", "MEP guys", "proxy", "generic model", "DirectShape", "translator", "linking vs opening", "mapping table", "BREP", "extrusion".
- Russian (dwg.ru): informal, lowercase, no greeting, "ифс", "ревит", "конструкторы", "экспертиза", jokes/emoticons; regulation talk cites ПП 87, СП 333.
- Chinese blogs: checklist style, "没有东西", "链接模型", "导出映射"; practitioners write tutorials rather than questions.
- Japanese: note.com business-blog style, 〇/△/－ marks, "確認申請", "意匠・構造・設備", "原点", "豆粒問題", "誓約書".
- Spanish: students, error strings kept in English ("Could not find ENDSEC").
- German/French: formal; English product terms mixed in ("Bauteile ... als Revit-Elemente", "BET", "maquette", "Starter Kit", "BIM Checker").
- Illustrative fragments: "my consultants work in Revit", "fundamentally flawed", "elements not exporting", "only axes arrive", "豆粒問題", "tengo un problema al momento de importar".
- Tone: mostly frustrated-neutral; urgent when a deadline (permit, issue date) is implied; closers rare, no thanks in titles.

## Local ecosystem
- Singapore: BCA CORENET X, IFC-SG, IFC4 Reference View, IFC+SG Validator add-ons for Archicad/Revit — https://info.corenet.gov.sg/ifc-sg/model-setup-and-coordination
- Geneva (CH): Norme IFC de depot, Starter Kit (bimetat.ge.ch), BIM Checker; Revit and Archicad guides — https://www.ge.ch/utiliser-bim-building-information-modeling/je-prepare-maquette-bim-autorisation-construire
- Japan: MLIT "BIM図面審査" from April 2026, ArchSync cloud, input/output standard (入出力基準), plan for BIM data review ~2029 — https://note.com/arent3d/n/nc9cf79adcb17
- Shanghai: BIM smart review modelling manual (EDM files, IFC for structural load review) — https://zjw.sh.gov.cn/cmsres/4a/4a7bc95634cd4852b2399e57e9c692dd/a646541bab5ad86dc1684d1126e21e29.pdf
- Dubai Municipality DM BIM submission (openBIM IFC, Revit template) — https://dxmdigitaldocs.github.io/site/docs/dm-bim-submission/frequently-asked-technical-questions
- Korea: Seumteo (세움터), KBim Assess-Lite, open-BIM permit research — https://koreascience.kr/article/JAKO201608450940594.pdf
- Russia: ПП 87, СП 333.1325800.2017, dwg.ru community — https://forum.dwg.ru/showthread.php?t=153428
- Germany: digital Bauantrag portals (BundID, Bauportal.NRW, Bavaria Digitaler Bauantrag) — no IFC requirement found.
- Software: Archicad (Graphisoft) with Revit Structure/MEP translators and Revit add-in (Improved IFC Import); Revit IFC exporter (open source, Autodesk/revit-ifc); Solibri, BIMcollab, Navisworks; Tekla, ETABS, Lira, STARK ES, CYPE; J tool for Revit IFC (JP).
- Open source: BlenderBIM/Bonsai, IfcOpenShell, FreeCAD BIM, FME, OSArch community — https://community.osarch.org

## Notable sources
- https://forums.autodesk.com/t5/revit-architecture-forum/problems-with-imported-ifc-from-archicad/td-p/11509535 — Archicad IFC into Revit problems
- https://forums.autodesk.com/t5/revit-architecture-forum/ifc-import-problem-ceilings-walls/td-p/10593825 — ceilings/walls on import
- https://forums.autodesk.com/t5/revit-architecture-forum/ifc-from-archicad-imported-into-revit-phasing-inconsistencies/td-p/13129044 — phasing lost
- https://forums.autodesk.com/t5/revit-architecture-forum/ifc-exchange-revit-archicad/td-p/10357376 — IFC is not an intermediate format
- https://forums.autodesk.com/t5/revit-structure-forum/ifc-export-option-include-steel-elements-messing-up-columns-and/m-p/9163932 — steel elements shift
- https://forums.autodesk.com/t5/revit-structure-forum/is-there-a-final-answer-as-to-if-analytical-elements-can-be/m-p/9350321/highlight/true — analytical elements via IFC
- https://community.graphisoft.com/t5/Collaboration-with-other/Interoperability-issue-Share-model-with-consultants-working-in/td-p/341497 — sharing with Revit consultants
- https://community.graphisoft.com/t5/Collaboration-with-other/Revit-IFC-to-Archicad-is-fundamentally-flawed/m-p/589984/highlight/true — coordination not handover
- https://community.graphisoft.com/t5/Collaboration-with-other/IFC-Model-Exchange-with-Archicad-for-Revit-2024-error/m-p/622653 — plugin crash
- https://community.graphisoft.com/t5/Collaboration-with-other/Issues-with-exporting-Beams-from-Archicad-as-IFC-into-Revit/td-p/276679 — beams
- https://community.graphisoft.com/t5/Modellierung/IFC-Export-aus-ArchiCAD-f%C3%BCr-Revit-MEP/m-p/544905 — German MEP export
- https://www.bimpedia.eu/articles/15926-ifc-export-from-archicad-to-revit-structure/ — translator settings guide
- https://community.osarch.org/discussion/926/blenderbim-authoring-ifc-files-for-revit — types for Revit
- https://community.osarch.org/discussion/873/blenderbim-add-on-to-archicad-workflow — Blender to Archicad
- https://community.osarch.org/discussion/3541/long-term-workflow-blk360-revit-fiverr-ifc4-freecad-bim-ai-assisted-remodeling-is-this-a — Revit IFC4 in FreeCAD
- https://forums.buildingsmart.org/t/como-poder-exportar-un-modelo-3d-estructural-realizado-en-revit-a-etabs-por-medio-del-formato-ifc/2985 — Spanish ETABS
- https://forums.buildingsmart.org/t/ids-and-federated-ifc-file/5654 — IDS on federated IFC
- https://github.com/Autodesk/revit-ifc/issues/408 — relinking updated IFC
- https://github.com/Autodesk/revit-ifc/issues/492 — slow export
- https://forum.dwg.ru/showthread.php?t=160240 — IFC export error (ru)
- https://forum.dwg.ru/showthread.php?t=153428 — BIM regulation questions (ru)
- https://forum.dwg.ru/showthread.php?t=107461 — architect/structural collaboration (ru)
- https://note.com/arent3d/n/nc9cf79adcb17 — Japan BIM drawing review
- https://note.com/iu_bimstudio_n/n/nf41bb9e91025 — Archicad IFC output (JP)
- https://info.corenet.gov.sg/ifc-sg/model-setup-and-coordination — Singapore model quality
- https://www.ge.ch/utiliser-bim-building-information-modeling/je-prepare-maquette-bim-autorisation-construire — Geneva permit
- https://novedge.com/blogs/design-news/revit-tip-revit-ifc-export-configuration-and-quality-control — export QC tips

## Gaps
- Autodesk and Graphisoft community pages returned 403; no full thread text, answers are from search summaries only.
- Reddit not searchable (domain blocked); no reddit records.
- Portuguese, Korean and Italian practitioner threads were thin or absent (pt has synthetic only; ko/it real records are an academic paper and official docs); zhihu/csdn partly 521; Chinese records are blog snippets.
- Germany: no IFC-specific permit rule found; Norway ByggNett/Statsbygg not confirmed; OpenPermit and Dubai FAQ pages returned 404 on fetch (Dubai kept as snippet).
- Years for some snippet records are estimated from URL ids or search context; treat as approximate.
- Skipped: freelancer sales pages (comeup, Fiverr gigs), a doubtful blogspot article on IFC errors, a vendor announcement for a Revit-less converter (DDC) listed only as vendor claim.
