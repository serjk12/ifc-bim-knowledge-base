# IFC / BIM Knowledge Base — как люди на самом деле работают с IFC и Revit

**Русский** | [English](#english)

> **Статус.** Волна 1 исследования завершена и разобрана в документы. **Волна 2** (больше языков и стран) ещё добавляется: новые файлы будут появляться в `research_raw/wave2/`, а сводные документы и выгрузки будут обновляться.
> Новичку в BIM: сразу открывайте [00_START_HERE_RU.md](00_START_HERE_RU.md). Нужна карта всех файлов: [INDEX.md](INDEX.md).

---

## Зачем это

Эта база знаний нужна, чтобы **тестировать MCP-серверы и AI-ассистентов, которые работают с форматом IFC (Industry Foundation Classes), с Revit и вообще с openBIM**.

Главная проблема тестировщика без опыта в BIM: языковая модель, которую попросили «придумай вопросы для IFC-ассистента», выдаёт гладкие учебные формулировки. Живые люди пишут иначе: «ифс на 1.5 гига, вьюер у экспертизы виснет», «IFC exported from Revit has no psets, wtf», «Revit导出IFC后构件丢失». База собрана так, чтобы модель могла:

1. **писать запросы, которые звучат как настоящие** (жаргон, опечатки, сжатость, тон, язык);
2. **попадать в реальные боли**: что у людей ломается чаще всего и почему;
3. **оценивать ответы ассистента**: есть ли знание о версиях IFC, о ловушках экспорта, о том, чего в файле быть не может.

## Для кого

| Кто вы | Что вам здесь нужно |
|---|---|
| Тестировщик IFC/Revit MCP-серверов (без опыта BIM) | [00_START_HERE_RU.md](00_START_HERE_RU.md), затем [07_mcp_testing/](07_mcp_testing/what_ifc_mcp_servers_do.md) |
| Автор промптов / сценариев тестов | банки запросов, матрица вариаций, готовый промпт-генератор в [07_mcp_testing/](07_mcp_testing/llm_generation_prompt.md) |
| Разработчик MCP-сервера | боли пользователей, ловушки, каталог существующих серверов: [05_real_world_questions/](05_real_world_questions/pain_points_top100.md), [04_open_source/mcp_servers_and_ai_tools.md](04_open_source/mcp_servers_and_ai_tools.md) |
| BIM-специалист, который проверяет качество базы | справочники в `01`–`04`, источники в [09_sources/](09_sources/sources_index.md) |

## Что внутри

| Папка | Содержимое |
|---|---|
| [`01_ifc_basics/`](01_ifc_basics/01_what_is_ifc_and_versions.md) | IFC простыми словами: версии, устройство файла, классы, связи, свойства, геометрия и координаты, материалы, MEP/конструкции/инфраструктура (9 документов) |
| [`02_standards_regulations/`](02_standards_regulations/buildingsmart_standards.md) | стандарты buildingSMART (IFC, IDS, BCF, bSDD, MVD), ISO/CEN, EIR/BEP, **12 национальных обзоров** (Россия, Китай, Сингапур, Великобритания и Ирландия, DACH, Франция, Бенилюкс, Скандинавия и Балтия, Испания/Португалия/Италия, Япония и Корея, Латинская Америка, США и Канада) |
| [`03_software/`](03_software/authoring_tools_ifc.md) | Revit (экспорт и импорт/линк IFC), Archicad, Tekla, Allplan, Renga и др.; вьюеры, чекеры, CDE, конвертеры |
| [`04_open_source/`](04_open_source/mcp_servers_and_ai_tools.md) | IfcOpenShell, xBIM, web-ifc и др.; **каталог MCP-серверов для IFC/Revit**; исследования LLM + BIM; тестовые IFC-файлы; сообщества |
| [`05_real_world_questions/`](05_real_world_questions/pain_points_top100.md) | реальные вопросы: **топ-100 болей**, по 17 темам, 13 языковым группам, 14 ролям |
| [`06_how_people_write/`](06_how_people_write/style_guide.md) | как люди формулируют: стиль, жаргон, написания названий, антипаттерны «машинных» вопросов |
| [`07_mcp_testing/`](07_mcp_testing/what_ifc_mcp_servers_do.md) | таксономия намерений, 156 сценариев, ловушки, рубрика оценки, **готовый промпт-генератор**, банки запросов (RU/EN/14 языков), тесты MCP, управляющих Revit |
| [`08_glossary/`](08_glossary/glossary_multilingual.md) | многоязычный глоссарий и расшифровка сокращений |
| [`09_sources/`](09_sources/sources_index.md) | индекс источников и каталог сообществ |
| [`exports/`](exports/) | машиночитаемые выгрузки: `real_questions.*` и `synthetic_prompts.*` (JSONL и CSV) |
| [`research_raw/`](research_raw/) | «сырьё»: отчёты и записи исследовательских ячеек (волна 1, позже волна 2) |
| [`_meta/`](_meta/SPEC.md) | схема записей, отчёт о покрытии, методология |
| [`tools/kb.py`](tools/kb.py) | утилита: статистика, фильтры и постраничное чтение записей |

Полный список файлов с описаниями: [INDEX.md](INDEX.md).

## Как использовать с LLM

| Сценарий | Что делать |
|---|---|
| **Чат-LLM** (Claude, ChatGPT, Gemini в браузере) | Загрузите в чат один файл `exports/kb_compact.md` (компактная версия всей базы; собирается в конце сборки, если файла ещё нет в вашей копии, возьмите вместо него [07_mcp_testing/llm_generation_prompt.md](07_mcp_testing/llm_generation_prompt.md) и [06_how_people_write/style_guide.md](06_how_people_write/style_guide.md)). Затем вставьте промпт из [07_mcp_testing/llm_generation_prompt.md](07_mcp_testing/llm_generation_prompt.md). |
| **Агент** (Claude Code, Cursor и т.п.) | Дайте агенту весь репозиторий (или папку, скачанную ZIP-ом). Скажите: «прочитай `00_START_HERE_EN.md` и `07_mcp_testing/llm_generation_prompt.md`, затем сгенерируй 30 запросов для такого-то MCP». Агент сам откроет нужные документы и сможет искать записи через `tools/kb.py`. |
| **Таблица** (Excel, Google Sheets) | Откройте `exports/real_questions.csv` и `exports/synthetic_prompts.csv`. Фильтруйте по `lang`, `persona`, `intent`, `topics`. Это удобно, чтобы вручную выбрать «образцы голоса». |

## Быстрый старт в 5 шагов

1. Прочитайте [00_START_HERE_RU.md](00_START_HERE_RU.md) (15 минут): что такое IFC, 15 главных терминов, топ-10 болей.
2. Откройте [07_mcp_testing/what_ifc_mcp_servers_do.md](07_mcp_testing/what_ifc_mcp_servers_do.md): что вообще умеют MCP-серверы для IFC/Revit и какие запросы честно задавать.
3. Выберите, на чём тренироваться: [файлы для тестов](04_open_source/sample_ifc_files.md) (IFC-модели).
4. Сгенерируйте запросы: вставьте промпт из [07_mcp_testing/llm_generation_prompt.md](07_mcp_testing/llm_generation_prompt.md) в LLM; для разнообразия бросайте «кубики» из [variation_matrix.md](07_mcp_testing/variation_matrix.md) или берите готовые запросы из банков ([RU](07_mcp_testing/prompt_bank_ru.md), [EN](07_mcp_testing/prompt_bank_en.md), [14 языков](07_mcp_testing/prompt_bank_multilingual.md)).
5. Оцените ответы по [evaluation_rubric.md](07_mcp_testing/evaluation_rubric.md) и проверьте ловушки из [edge_cases_and_traps.md](07_mcp_testing/edge_cases_and_traps.md).

## Покрытие (после волны 1)

Источник цифр: [_meta/coverage_report.md](_meta/coverage_report.md) и подсчёт по `research_raw/wave1/`.

| Показатель | Значение |
|---|---|
| Записей всего | **3 592** (реальные вопросы: **2 304**, синтетические запросы: **1 288**) |
| Файлов-ячеек исследования | 78 (ошибок разбора: 0) |
| Языков (коды) | 20 кодов; больше всего: en 2 452, zh 304, ru 260, ja 107, es 102, de 78, it 72, ko 50, fr 48, nl 35, pt 30 (+ pt-BR 15), no 30; единичные: tr, sk, vi, cs, da, ar, el |
| Страны и регионы | 12 национальных обзоров регламентов в `02_standards_regulations/national/` (см. таблицу выше) и 13 языковых документов в `05_real_world_questions/by_language/` |
| Уникальных ссылок-источников | 1 887 (на 105 сайтах; больше всего GitHub, buildingSMART Forums, OSArch, Autodesk Forums, Dynamo Forum, dwg.ru, Zhihu, Habr, CSDN) |
| Темы | 56 тем; самые частые: export_revit 470, psets_properties 401, geometry_quality 296, class_mapping 289, coordinates_georef 272 |
| Роли | 16 ролей; больше всего bim_coordinator 950, developer_programmer 825, architect 380, bim_manager 356 |

Важно: данные неравномерны. Английский доминирует; португальский почти целиком синтетический; языки «other» (арабский, греческий и др.) представлены единичными записями. Подробности: [05_real_world_questions/by_language/other.md](05_real_world_questions/by_language/other.md). Именно это должна выровнять волна 2.

## Методология в одном абзаце

Параллельные исследовательские ячейки (по языкам, источникам, ролям и темам) искали реальные обсуждения: форумы, GitHub issues, блоги, Q&A, официальную документацию. Для каждого найденного обращения записывался **пересказ** (на языке оригинала, без копирования текста), роль, намерение, темы, версия IFC, тон и ссылка. Отдельно создавались **синтетические запросы**, явно помеченные как `synthetic`, с ожидаемым поведением ассистента. Справочные документы (`01`–`04`, `08`) написаны с опорой на официальные источники, непроверенное помечено. Итоговые документы (`05`–`07`) построены на подсчётах по записям. Подробно: [_meta/METHODOLOGY.md](_meta/METHODOLOGY.md) (файл пишется в конце сборки).

## Оговорка

Материалы сообществ **пересказаны со ссылкой на источник**, это не цитаты; права на оригиналы принадлежат авторам. Синтетические запросы придуманы и не являются реальными высказываниями. Нормативные требования, версии программ и возможности MCP-серверов меняются: **критичные факты проверяйте по официальным источникам** (buildingSMART, ISO, документация вендоров, README проектов). Возможности MCP-серверов описаны по их документации (README): авторы документов эти серверы не устанавливали и не запускали, поэтому всё это заявленные, а не проверенные возможности.

## Как скачать

Зелёная кнопка **Code → Download ZIP** вверху страницы репозитория. Либо `git clone`.

---

<a id="english"></a>

# IFC / BIM Knowledge Base — how people really work with IFC and Revit

[Русский](#ifc--bim-knowledge-base--как-люди-на-самом-деле-работают-с-ifc-и-revit) | **English**

> **Status.** Research wave 1 is finished and written up. **Wave 2** (more languages and countries) is still being added: new files will appear under `research_raw/wave2/`, and the summary documents and exports will be refreshed.
> New to BIM? Open [00_START_HERE_EN.md](00_START_HERE_EN.md) first. Need a map of every file: [INDEX.md](INDEX.md).

## Why this exists

This knowledge base is for **testing MCP servers and AI assistants that work with IFC (Industry Foundation Classes), Revit and openBIM**.

The problem for a tester with no BIM background: if you ask a language model to "invent questions for an IFC assistant", you get smooth textbook sentences. Real people write differently: "ифс на 1.5 гига, вьюер у экспертизы виснет" (the IFC is 1.5 GB and the expert-review viewer hangs), "IFC exported from Revit has no psets, wtf", "Revit导出IFC后构件丢失" (elements went missing after exporting IFC from Revit). The base is built so that a model can:

1. **write requests that sound human** (jargon, typos, brevity, tone, language);
2. **hit real pain points**: what breaks most often for people and why;
3. **judge the assistant's answers**: does it know about IFC versions, export traps, and what cannot be in a file.

## Who it is for

| You are | You need |
|---|---|
| A tester of IFC/Revit MCP servers (no BIM background) | [00_START_HERE_EN.md](00_START_HERE_EN.md), then [07_mcp_testing/](07_mcp_testing/what_ifc_mcp_servers_do.md) |
| A prompt or test-scenario author | prompt banks, variation matrix and the ready generation prompt in [07_mcp_testing/](07_mcp_testing/llm_generation_prompt.md) |
| An MCP server developer | user pain points, traps, a catalog of existing servers: [05_real_world_questions/](05_real_world_questions/pain_points_top100.md), [04_open_source/mcp_servers_and_ai_tools.md](04_open_source/mcp_servers_and_ai_tools.md) |
| A BIM specialist reviewing the base | reference docs in `01`-`04`, sources in [09_sources/](09_sources/sources_index.md) |

## What is inside

| Folder | Contents |
|---|---|
| [`01_ifc_basics/`](01_ifc_basics/01_what_is_ifc_and_versions.md) | IFC in plain words: versions, file anatomy, classes, relationships, properties, geometry and coordinates, materials, MEP/structural/infrastructure (9 documents) |
| [`02_standards_regulations/`](02_standards_regulations/buildingsmart_standards.md) | buildingSMART standards (IFC, IDS, BCF, bSDD, MVD), ISO/CEN, EIR/BEP, **12 national overviews** (Russia, China, Singapore, UK & Ireland, DACH, France, Benelux, Nordics & Baltics, Spain/Portugal/Italy, Japan & Korea, Latin America, USA & Canada) |
| [`03_software/`](03_software/authoring_tools_ifc.md) | Revit (IFC export and import/link), Archicad, Tekla, Allplan, Renga and others; viewers, checkers, CDE, converters |
| [`04_open_source/`](04_open_source/mcp_servers_and_ai_tools.md) | IfcOpenShell, xBIM, web-ifc and more; **a catalog of MCP servers for IFC/Revit**; LLM + BIM research; sample IFC files; communities |
| [`05_real_world_questions/`](05_real_world_questions/pain_points_top100.md) | real questions: the **top 100 pain points**, by 17 topics, 13 language groups, 14 personas |
| [`06_how_people_write/`](06_how_people_write/style_guide.md) | how people phrase things: style, jargon, spellings of product names, anti-patterns of machine-made questions |
| [`07_mcp_testing/`](07_mcp_testing/what_ifc_mcp_servers_do.md) | intent taxonomy, 156 scenarios, traps, evaluation rubric, **ready generation prompt**, prompt banks (RU/EN/14 languages), testing MCPs that drive Revit |
| [`08_glossary/`](08_glossary/glossary_multilingual.md) | multilingual glossary and abbreviations |
| [`09_sources/`](09_sources/sources_index.md) | sources index and communities directory |
| [`exports/`](exports/) | machine-readable exports: `real_questions.*` and `synthetic_prompts.*` (JSONL and CSV) |
| [`research_raw/`](research_raw/) | raw material: reports and records of the research cells (wave 1, wave 2 later) |
| [`_meta/`](_meta/SPEC.md) | record schema, coverage report, methodology |
| [`tools/kb.py`](tools/kb.py) | helper: statistics, filters and paged reading of records |

Full file list with descriptions: [INDEX.md](INDEX.md).

## How to use it with an LLM

| Scenario | What to do |
|---|---|
| **Chat LLM** (Claude, ChatGPT, Gemini in a browser) | Upload one file, `exports/kb_compact.md` (a compact version of the whole base; it is built at the end of assembly, so if it is not in your copy yet use [07_mcp_testing/llm_generation_prompt.md](07_mcp_testing/llm_generation_prompt.md) and [06_how_people_write/style_guide.md](06_how_people_write/style_guide.md) instead). Then paste a prompt from [07_mcp_testing/llm_generation_prompt.md](07_mcp_testing/llm_generation_prompt.md). |
| **Agent** (Claude Code, Cursor, etc.) | Give the agent the whole repository (or the unzipped download). Say: "read `00_START_HERE_EN.md` and `07_mcp_testing/llm_generation_prompt.md`, then generate 30 requests for this MCP server". The agent opens the documents it needs and can search records with `tools/kb.py`. |
| **Spreadsheet** (Excel, Google Sheets) | Open `exports/real_questions.csv` and `exports/synthetic_prompts.csv`. Filter by `lang`, `persona`, `intent`, `topics`. Good for hand-picking "voice samples". |

## Quick start in 5 steps

1. Read [00_START_HERE_EN.md](00_START_HERE_EN.md) (15 minutes): what IFC is, 15 key terms, the top 10 pain points.
2. Open [07_mcp_testing/what_ifc_mcp_servers_do.md](07_mcp_testing/what_ifc_mcp_servers_do.md): what IFC/Revit MCP servers can do and which requests are fair to send.
3. Get some model files to test with: [sample IFC files](04_open_source/sample_ifc_files.md).
4. Generate requests: paste a prompt from [07_mcp_testing/llm_generation_prompt.md](07_mcp_testing/llm_generation_prompt.md) into an LLM; for variety roll the "dice" in [variation_matrix.md](07_mcp_testing/variation_matrix.md), or take ready requests from the banks ([RU](07_mcp_testing/prompt_bank_ru.md), [EN](07_mcp_testing/prompt_bank_en.md), [14 languages](07_mcp_testing/prompt_bank_multilingual.md)).
5. Score the answers with [evaluation_rubric.md](07_mcp_testing/evaluation_rubric.md) and try the traps in [edge_cases_and_traps.md](07_mcp_testing/edge_cases_and_traps.md).

## Coverage (after wave 1)

Figures come from [_meta/coverage_report.md](_meta/coverage_report.md) and a count over `research_raw/wave1/`.

| Measure | Value |
|---|---|
| Records | **3,592** (real questions: **2,304**, synthetic prompts: **1,288**) |
| Research cell files | 78 (parse errors: 0) |
| Languages (codes) | 20 codes; largest: en 2,452, zh 304, ru 260, ja 107, es 102, de 78, it 72, ko 50, fr 48, nl 35, pt 30 (+ pt-BR 15), no 30; singletons: tr, sk, vi, cs, da, ar, el |
| Countries and regions | 12 national regulation overviews in `02_standards_regulations/national/` (see the table above) and 13 language documents in `05_real_world_questions/by_language/` |
| Distinct source links | 1,887 (on 105 sites; most: GitHub, buildingSMART Forums, OSArch, Autodesk Forums, Dynamo Forum, dwg.ru, Zhihu, Habr, CSDN) |
| Topics | 56 topic tags; most frequent: export_revit 470, psets_properties 401, geometry_quality 296, class_mapping 289, coordinates_georef 272 |
| Personas | 16 personas; largest: bim_coordinator 950, developer_programmer 825, architect 380, bim_manager 356 |

Note that the data is uneven. English dominates; Portuguese is almost entirely synthetic; the "other" languages (Arabic, Greek and so on) have single records. See [05_real_world_questions/by_language/other.md](05_real_world_questions/by_language/other.md). Wave 2 is meant to even this out.

## Methodology in one paragraph

Parallel research cells (by language, source, persona and topic) searched for real discussions: forums, GitHub issues, blogs, Q&A sites, official documentation. For each real item they recorded a **paraphrase** (in the original language, not copied text), persona, intent, topics, IFC version, tone and a link. Separately they wrote **synthetic prompts**, clearly labelled `synthetic`, with the expected assistant behaviour. The reference documents (`01`-`04`, `08`) rest on official sources, with unverified statements flagged. The synthesis documents (`05`-`07`) are built from counts over the records. Details: [_meta/METHODOLOGY.md](_meta/METHODOLOGY.md) (written at the end of assembly).

## Disclaimer

Community content is **paraphrased with a link to its source**, it is not quoted; rights to the originals belong to their authors. Synthetic prompts are invented and are not real quotes. Regulations, software versions and MCP server capabilities change: **verify critical facts against official sources** (buildingSMART, ISO, vendor documentation, project READMEs). MCP server capabilities are described from their documentation (READMEs): the authors of these documents did not install or run those servers, so treat them as claimed, not verified, capabilities.

## How to download

Green button **Code → Download ZIP** at the top of the repository page, or `git clone`.
