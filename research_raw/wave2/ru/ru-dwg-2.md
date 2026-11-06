# dwg.ru 2: координаты, КСИ в IFC, ADSK-параметры, шаблоны ЦИМ, IFC для экспертизы
Cell: ru-dwg-2 · Languages: Russian · Collected: 2026-11-06 · Records: 28 real / 17 synthetic · Communities covered: forum.dwg.ru (Revit, BIM, Civil 3D, AutoCAD subforums), dwg.ru news/download catalog

Note: the page fetcher returned Cyrillic text partly garbled (encoding), so many real records are paraphrased from the readable parts plus search snippets, not verbatim quotes. 8 of the 28 real records are snippet-only.

## Top themes (ranked by frequency)
- IFC for state expertise (what to submit, 2019 start, then 1431/331 in 2021-22; IFC vs RVT/PDF/DWG)
- Coordinates: base point, survey point, shared coordinates, linking with Civil 3D/topo, MSK zero, X/Y swap
- IFC import problems in Revit (missing objects, wrong categories, phases, no geometry)
- IFC export loses data (properties, structure, schedules not exported)
- Exchange with other tools: Tekla, SAPFIR, STARK ES, Plant 3D, Renga, Model Studio CS, ArchiCAD
- ADSK template and ADSK_* shared parameters (schedules, formulas, shared parameter file, GUIDs)
- Classification: KSI (ksi.faufcc.ru), properties filled "by a classifier" for automatic checks
- Regulation debate: PP 1431, order 331, SP 328/331/333.1325800.2017, LOD 300/400
- Batch adding parameters to families (API, Dynamo)
- Choosing Revit vs Renga/Allplan; domestic software substitution
- IFC viewers/checkers (xBIM, BimVision, BimSight, IfcOpenShell, BlenderBIM, FreeCAD)
- Terrain/GPS placement (WGS84 vs projected CRS, Civil 3D, QGIS)

## What people want
- A clear answer on what format and content experts accept (IFC vs native model) and what gets checked.
- Models that land in the right place: matching coordinates between disciplines and survey (MSK).
- Properties and ADSK parameters surviving IFC export, plus classification codes in elements.
- Working exchange with domestic/structural/MEP tools without data loss.
- Ready scripts or automation for repetitive parameter work.
- Ways to verify an IFC (viewer, validator) before submission.

## How people write here
Register: informal, terse forum Russian, often lowercase, one to five sentences; newcomers add a self-intro and ask several questions at once. Long argumentative posts appear in regulation threads (sarcasm, jokes like "2019 vs 2119").
Jargon: "ифс" / "ифц" (IFC), "ревит" (Revit), "ЦИМ"/"ИМ" (information model), "КСИ" (classifier), "ФОП" (shared parameter file), "МСК" (local coordinate system), "общие параметры", "базовая точка / точка съемки", "семейство", "спецификация", "экспертиза", "шаблон ADSK / weandrevit".
Code-switching: error texts pasted in English; software names in Latin; links to English Autodesk forums.
Context: usually version given in title ("Revit 2022"), often no IFC version, screenshots attached, files rarely shared; many threads get no replies.
Fragments: "System Error encountered during import"; "как правильно экспортировать модель в IFC?"; "подскажите, кто сталкивался"; "в ифс теряется информация".
Typical responders (not named): terse experts give links to API/docs or one-line pointers.

## Local ecosystem
- Government: PP 1431 (15.09.2020), order 331 (05.03.2021), ФАУ «ФЦС» KSI classifier http://ksi.faufcc.ru/
- Standards: SP 328.1325800.2017, SP 331.1325800.2017, SP 333.1325800.2017
- Expertise bodies mentioned: Мосгосэкспертиза (pilot RVT+IFC+DWF), СПб ГАУ «Центр государственной экспертизы» (IFC accepted)
- Local software: Renga, Model Studio CS, nanoCAD, KOMPAS, SAPFIR-3D, STARK ES, BimVision, Allplan (foreign but used), ADSK/weandrevit templates
- Open-source/others: IfcOpenShell, BlenderBIM, FreeCAD, xBIM, ifc-checker, IfcValidator, Solibri (mentioned as paid addon)
- Educators/resources: vplate.ru (mentioned), ISICAD article (mentioned)

## Notable sources
- https://forum.dwg.ru/showthread.php?t=153428 expertise of Revit project (2019)
- https://forum.dwg.ru/showthread.php?p=1809655 same, page 2
- https://forum.dwg.ru/showthread.php?page=7&t=161332 BIM requirements 2022, IFC and KSI
- https://forum.dwg.ru/showthread.php?t=166431&page=25 latest BIM news, IFC as exchange format
- https://forum.dwg.ru/showthread.php?t=134394&page=33 draft SP discussion
- https://forum.dwg.ru/showthread.php?t=154396 how to open IFC correctly
- https://forum.dwg.ru/showthread.php?t=160240 SAPFIR IFC export
- https://forum.dwg.ru/showthread.php?t=166052 IFC import in Revit 2022
- https://forum.dwg.ru/showthread.php?t=146029 Tekla to Revit
- https://forum.dwg.ru/showthread.php?t=133669 Revit to STARK ES
- https://forum.dwg.ru/showthread.php?t=173570 IFC from Plant 3D 2025
- https://forum.dwg.ru/showthread.php?t=154884 Revit-Civil 3D coordinates
- https://forum.dwg.ru/showthread.php?t=157807 terrain by GPS in Revit 2021
- https://forum.dwg.ru/showthread.php?t=166064 pile coordinates in schedule
- https://forum.dwg.ru/showthread.php?t=157998&page=2 MSK zero in AutoCAD
- https://forum.dwg.ru/showthread.php?t=124794 MSK NSO in Civil 3D
- https://forum.dwg.ru/showthread.php?t=162520 ADSK template steel schedule
- https://forum.dwg.ru/showthread.php?t=129504 shared parameters and ADSK file
- https://forum.dwg.ru/showthread.php?t=144315 batch parameters
- https://forum.dwg.ru/showthread.php?t=169847 Revit to Model Studio/Renga
- https://dwg.ru/dnl/7769 Revit coordinates PDF
- https://dwg.ru/cat/news/4619 BIM competition checks

## Gaps
- Fetcher returned mojibake for most threads; verbatim Russian quotes were largely unavailable, so paraphrases dominate.
- Little direct content found on KSI mapping into Revit IFC, ADSK parameters inside IFC Psets, or "шаблон ЦИМ" specifically; dwg.ru search surfaced mostly 2015-2023 threads, few 2024-2026.
- Several threads have no replies (answers unknown). Snippet-only records have unknown years.
- No suspicious or pirated sites encountered; the dwg.ru download catalog entry was cited as a description only, nothing downloaded.
- Did not open ksi.faufcc.ru or official decrees (outside assigned domain).
