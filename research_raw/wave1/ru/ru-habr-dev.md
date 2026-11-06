# Habr / VC / GitHub (RU): разработка под IFC (парсинг, IfcOpenShell, xBIM, web-ifc, Revit API)
Cell: ru-habr-dev · Languages: Russian · Collected: 2026-11-06 · Records: 34 real / 16 synthetic · Communities covered: habr.com, forum.dwg.ru, cyberforum.ru (snippet only), github.com (RU READMEs and issues)

## Top themes (ranked by frequency)
- Pre-checking Revit models against IDS before submission to Moscow AGR (architectural-urban approval) via the "Строим просто" service.
- Revit IFC class assignment: category-to-class table unreliable; IfcExportAs / "Экспорт в IFC" parameters; value -1 to exclude.
- Post-processing exported IFC (fix classes, remove stair stringers, duplicates, wrong MSSK codes) with a change log.
- Property type errors (IfcArea/IfcLabel instead of IfcReal), numeric format (comma), UDPS mapping of Russian parameters.
- Zone/room (IfcSpace) geometry defects and area mismatches (ТЭП, RUS_Area vs geometry).
- Duplicate elements invisible in 3D; comparing versions by GlobalId; edit journals.
- Browser viewers and editors on web-ifc / IFC.js / That Open (performance, version pinning, project abandonment).
- Python extraction with IfcOpenShell/ifctester (quantities in ~40 lines, batch IDS checks, Excel export).
- Batch export of many .rvt to IFC (Revit Server, worksets, memory).
- Strategy debates: IFC vs USD/glTF, parametric geometry lost on export, IfcBuildingElementProxy as a "crutch".
- Older forum pain: Revit opens IFC badly, Tekla/Sapfir to Revit exchange.
- Emerging: Revit MCP servers and AI assistants with IFC tools.

## What people want
- Not wait two hours for an export only to learn a parameter is empty: validate inside Revit.
- A file that passes the IDS validator strictly, not merely "opens".
- Automate repetitive IFC cleanup and share edits with colleagues as a reproducible journal.
- Read, count and export IFC data (quantities, psets) without proprietary APIs.
- Lightweight offline/in-browser viewers, no data leaving the machine (NDA).
- Batch IFC export with per-model settings; control over IFC class of every Revit element.
- Move models between tools (Archicad to Revit, Tekla to Revit) without losing geometry/data.

## How people write here
- Habr: long first-person engineering retrospectives; BIM managers writing with colleagues; structured headings, numbers (1500 vs 200 clashes, 577 values, 0.78 mm). Titles are hooks: "Два часа выгрузки ради пустого параметра".
- Mixed Cyrillic/Latin: IfcExportAs, RUS_Area, UDPS, GlobalId inside Russian sentences; Revit UI terms in Russian ("Экспорт в IFC", "общие параметры").
- Slang/jargon: ЦИМ (digital information model), АГР (architectural-urban concept approval), МССК (classifier of construction resources), "зона", "склейка" (model merge), "ифс" (spoken IFC), "Навис" (Navisworks), "ревит", "прокси".
- Emotional tone: weary pragmatism ("коварная вещь"), humour ("перестали бояться валидатора"), rarely hostile except in comment sections on opinion pieces.
- Forum.dwg.ru questions are short and lowercase with minimal context: "Как корректно открыть IFC".
- Fragments: "категории Revit не определяют IFC-класс"; "файл открывается не значит валиден"; "объёмы: 17 кликов или 40 строк".
- Comments on Habr were not retrievable by the fetch tool; opinions there are from article text and one comments page.

## Local ecosystem
- Moscow: order ДГП-Р-1/26/64-16-6/26 (from 2 April 2026) requires IFC with attribute sets for AGR; checking via "Строим просто" with IDS packs.
- St. Petersburg state expertise (СПб ГАУ ЦГЭ) publishes an IDS example; Sverdlovsk region BIM standard cited for IDS properties.
- МССК classifier for rooms/elements; Russian parameter prefixes RUS_*.
- Tools: IDS Core (browser editor/validator), AGR.Checker (Revit plugin), ifc_checker and BatchIfcExporter (https://github.com/i-savelev), nanoCAD СПДС/mcad, Sapfir-3D, BIMIT, Bonsai (BlenderBIM), BIM Vision, Solibri, Navisworks.
- Open source: https://github.com/IfcOpenShell/IfcOpenShell, https://github.com/xBimTeam/XbimEssentials, https://github.com/ThatOpen, https://github.com/Autodesk/revit-ifc.
- Educators/authors: Habr BIM authors (data-first open-source advocates, IDS educators).
- International standards: buildingSMART IDS 1.0, bSDD, ISO 16739.

## Notable sources
- https://habr.com/ru/articles/1089018/ - pre-check IFC inside Revit for AGR
- https://habr.com/ru/articles/1094224/ - IDS Core browser post-processing
- https://habr.com/ru/articles/1100956/ - post-processing part 2 (areas, duplicates)
- https://habr.com/ru/articles/1098340/ - AGR.Checker details, UDPS
- https://habr.com/ru/articles/1087472/ - AGR.Checker changes
- https://habr.com/ru/articles/883016/ - IDS checking with ifcopenshell
- https://habr.com/ru/articles/908192/ - IDS limitations
- https://habr.com/ru/articles/882890/ - IFC associations by text editing
- https://habr.com/ru/articles/1063062/ - parametric geometry in IFC4
- https://habr.com/ru/articles/846382/ - building a BIM viewer, lessons
- https://habr.com/ru/articles/759230/ - IFC.js viewer tutorial
- https://habr.com/ru/articles/868186/ - data-centric BIM opinion
- https://habr.com/ru/articles/860936/ - IFC vs USD opinion
- https://habr.com/ru/articles/590819/comments/ - debate in comments
- https://habr.com/ru/articles/460719/ - IFC introduction
- https://habr.com/ru/articles/784224/ - IDS (snippet)
- https://habr.com/ru/articles/1054266/ - BIMIT analysis (snippet)
- https://github.com/i-savelev/BatchIfcExporter
- https://github.com/roosslan/ifc_exporter_revit_addin
- https://github.com/Davud77/bp-revit-tools
- https://github.com/Autodesk/revit-ifc/issues/777
- https://github.com/LuDattilo/RevitCortex
- https://forum.dwg.ru/showthread.php?t=154396
- https://forum.dwg.ru/showthread.php?t=146029
- https://forum.dwg.ru/showthread.php?t=160240

## Gaps
- Habr comment text was not returned by the fetch tool (only counts), so reader questions are underrepresented; cyberforum.ru returned HTTP 403.
- GitHub issue search in Russian returned nothing relevant; vc.ru surfaced only generic BIM explainers (not fetched).
- Several Habr dates show no year; 2026 inferred from content. No suspicious sites encountered. Most "real" records are author-stated problems from articles rather than Q&A threads; tosters/StackOverflow were not accessible.
