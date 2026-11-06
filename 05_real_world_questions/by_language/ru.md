# Russian (ru): how people ask about IFC, BIM and Revit

Primary language of this knowledge base. Language code `ru`. Everything in this file is grounded in `research_raw/wave1/` (104 real records, 149 synthetic records, all `lang = ru`) and in the reference docs listed in "Local ecosystem". Russian is shown in the original; English glosses follow.

**How to read this file (30 seconds).**
- *Real* = a thread, article, post, video title or regulation text that was actually seen, with its URL. The Russian text is a **paraphrase** kept in the asker's register, not a verbatim quote (only titles of 20 words or fewer are verbatim).
- *Synthetic* = a test prompt written by us. Never present it as a quote from a person.
- "ЦИМ" (digital information model) and "ТИМ" (information modelling technologies) are the Russian words for what English speakers call "BIM model" and "BIM". "Экспертиза" is the official design review a project must pass before construction.

**Honest limits of the data.**
- 104 real records come from about 74 distinct URLs. Several records share one thread (for example dwg.ru thread 146029 gives four records, thread 154396 gives four), so the number of independent voices is smaller than the number of rows.
- Only about 40 of the 104 are genuine questions in a forum thread. The rest are *problems stated in an article* (Habr, vendor blog), Telegram posts, video titles, or regulation text. The "Форма" column in section 5 says which is which.
- Time skew: 28 records are from 2026 (the Moscow АГР wave), 14 from 2025, and the rest are spread over 2009-2024. Older dwg.ru threads (2011-2021) show how ordinary engineers write; the 2025-2026 material shows the current regulatory pain.
- Three of the six Russian research cells (`ru-tim-expertiza`, `ru-dwg-revit`, `ru-renga-nanocad`) found **zero real posts** because search was blocked in that run. Their 44 synthetic prompts are hypotheses; this file reuses only the ones that other evidence supports. Real Renga and nanoCAD voices are thin (see section 3).
- Several dwg.ru pages were fetched with broken encoding (cp1251), so those paraphrases are reconstructions of the gist, not close readings. Where the answer is unknown it is left empty.

---

## 1. Where people ask

| Place | What happens there | Evidence in data | Access notes |
|---|---|---|---|
| **forum.dwg.ru** (Revit, Tekla, ArchiCAD, Allplan, Renga sub-forums) | Classic Russian CAD forum. One question per thread, short, usually no greeting. Threads get revived years later by newcomers with the same problem (the Tekla-to-Revit thread was active 2018, 2023 and 2024). Replies are terse; "помогло" closes the thread. | 38 real records, 2009-2026, most 2011-2021. | Public. Fetch tool returned garbled cp1251 text on many pages. Attachments (files, screenshots) carry much of the context and are not visible. |
| **Habr (habr.com/ru)** | Long first-person engineering write-ups by BIM managers, plugin authors and open-source advocates. Titles are hooks ("Два часа выгрузки ради пустого параметра"). Numbers in text (1500 vs 200 clashes, 20.63 m2 gap). Almost all about checking and fixing IFC for the Moscow АГР procedure (2026). | 32 real records (mostly 2025-2026), plus a few 2019-2024 tutorials. | Public. Reader comments could not be fetched (only counts), so reader questions are under-represented; one comments page was read. |
| **Telegram channels** | Short announcements, links, essays and opinion: "Всё про IFC" (t.me/ifc_ru), RevitHelper, BIMLIB, "Просто о BIM", "Академия BIM", "BIM Solutions". Channel posts are reference material and news, not Q&A. | 10 real records. | Public web preview (`t.me/s/...`) shows only posts and often without dates (years in these records are estimates). Closed chats and discussion groups are **not covered**; tgstat returned 403. |
| **Vendor and trade media** | Renga blog and manual, sapr.ru articles (nanoCAD СПДС with IFC from Revit), dwg.ru blogs, MasterDigitalTwin PDF instruction for Revit export. Written as how-to answers to an implied question. | 8 real records. | Public. |
| **GitHub (Russian READMEs and issues)** | Small tools: BatchIfcExporter, ifc_exporter_revit_addin, bp-revit-tools (MCP + Archicad-to-Revit), RevitCortex (MCP). READMEs state a task in plain Russian. | 8 real records. | Public. Few real issues in Russian; most Russian-speaking developers file issues in English (see `gh-enc-r017`). |
| **YouTube** | Course lectures and lessons: IFC export, absolute coordinates, project base point and survey point. | 4 real records (titles only). | Titles only; no comments read. |
| **Not covered** | VK groups, closed Telegram chats, cyberforum.ru (HTTP 403), RU sections of forums.autodesk.com (search showed almost nothing), vc.ru. | none | Treat as unknown. Renga runs communities in VK, Telegram, Max, RuTube and Zen ([community doc](../../04_open_source/community_projects_and_enthusiasts.md)); they were not read. |

Who asks (real records): BIM coordinators 23, developers/programmers 22, structural engineers 21, architects 14, BIM managers 12, students 5, reviewers from authorities 4, researchers 2. Estimators, MEP engineers and facility managers are absent from the real data (they appear only in synthetic prompts), so Russian-speaking estimator or MEP voices are a **gap**. Real tone: neutral 31, curious 22, frustrated 22, confused 17, skeptical 10. IFC version where stated: IFC4 43, IFC2x3 25, unknown/unspecified/not applicable 36. IFC 4.3 appears only once, in a synthetic prompt.

---

## 2. Top themes (ranked)

Ranking uses the topic tags of the 104 real records plus the cell reports. Counts are the number of real records carrying the tag (a record can have several).

| # | Theme | Real tags | What it looks like |
|---|---|---|---|
| 1 | **Revit-to-IFC export for expertise and Moscow АГР** (permitting, validation, IDS, class mapping) | export_revit 18, validation_checking 15, permitting_code_checking 9, ids_requirements 11 | "ошибки видно только после загрузки в Строим просто"; a two-hour export to learn that one parameter is empty; since 2 April 2026 an IFC conforming to IDS is required for the Moscow АГР procedure (per Habr). |
| 2 | **IFC class mapping and proxies** (`IfcExportAs`, shared parameters, stair stringers, ramps) | class_mapping 9 | "категория Revit не определяет класс IFC"; stringers still exported when set to "Нет"; a Wall-category family turned out to be a sliding gate. |
| 3 | **IFC into Revit loses data** (only grids, "dead geometry", yellow glass, missing properties) | import_into_revit 12 | "в Ревите видны только оси из Tekla"; "элементы приходят телами, а не объектами". |
| 4 | **Other software to Revit and back** (Tekla, SAPFIR-3D, ArchiCAD, Allplan, Bocad, Advance Steel, Plant 3D, SolidWorks) | export_other_tools 12, export_tekla 7, import_other_tools 6 | Tekla/Sapfir/ArchiCAD IFC opens badly in Revit; AutoCAD has no native IFC import. |
| 5 | **Which IFC version and view** (2x3 CV2.0 or IFC4 RV) | versions_mvd 10 | "для экспертизы какой ифс выгружать?"; MasterDigitalTwin guide: version and MVD are critical. |
| 6 | **Machine-readable requirements and checking** (IDS, ifctester, IDS Core, AGR.Checker, BIM Inspector) | ids_requirements 11 | Regional expertise bodies publish IDS (СПб ЦГЭ example, Мособлэкспертиза for roads, utilities and buildings); critique that IDS cannot express geometry or conditional logic. |
| 7 | **Properties and data types** (`RUS_*` parameters, IfcReal vs IfcLabel, UDPS mapping, comma as decimal separator) | psets_properties 10 | Validator rejects an area stored as IfcArea; global find-and-replace in a text editor breaks `Pset_*`. |
| 8 | **Rooms, zones, ТЭП areas** | spaces_rooms_areas 4 (11 synthetic) | Zones with imperfect contours compute in Revit but do not export as solids; sum of zone areas differs from the ТЭП XML by about 20 m2; duplicates invisible in 3D. |
| 9 | **Viewing and checking a received IFC** (free viewers xBIM, BIMvision, KIT; Navisworks) | viewers_opening 12 | "как корректно открыть IFC"; first diagnostic step is "open it in a free viewer". |
| 10 | **Structural handoff** (SCAD, Lira, STARK ES, Robot) | structural_analytical 5 | IFC carries the physical model; the analytical model is lost ("молоток и кирпич"). |
| 11 | **Developers: post-processing, scripting, viewers** (IfcOpenShell, web-ifc, xBIM, Revit API, batch export) | programming_* 14, revit_api_automation 7 | "объёмы: 17 кликов или 40 строк"; pin the web-ifc version because the That Open project changed. |
| 12 | **Coordinates, base points** | coordinates_georef 3 (10 synthetic) | Video titles about project base point, survey point, internal origin; "модель улетела". |
| 13 | **Cyrillic and encoding** | encoding_text 2 (7 synthetic) | Tekla refuses an IFC whose header holds a Cyrillic path; SolidWorks writes raw Cyrillic next to `\X2\` escapes. |
| 14 | **Strategy and opinion** (Renga maturity, IFC vs USD, data-first BIM, "работа в стол") | request_opinion 9 | Skeptical tone toward both software and regulation. |
| 15 | **AI and MCP** | ai_llm_mcp 2 real | Russian READMEs for Revit/Archicad MCP tools; "plain words" interface (see `rauto-r032`, `habr-r026`, `habr-r034`). |

What people want (shared goal): pass expertise or АГР on the first attempt, avoid long exports that fail late, get elements into the right IFC class with the required properties, hand a model to subcontractors or analysts without losing data, and view IFC for free without a Revit licence.

---

## 3. Local ecosystem

Short and linked. Facts marked *(unverified)* come from the repo's national doc or reports and could not be confirmed against official texts; do not use them as test oracles. Details: [Russia national doc](../../02_standards_regulations/national/russia.md).

**Regulation and who asks for what**
- Terms: ТИМ (technologies), ЦИМ (the model), "информационная модель объекта капитального строительства". The state pushes ТИМ through government decrees, the Town Planning Code (Градостроительный кодекс, article 48 mentions the information model), standards (СП, ГОСТ Р) and expertise bodies. IFC is the main open format for models submitted to state expertise (Russian Wikipedia, secondary source).
- Standards named in the data: **СП 333.1325800** (rules for forming the information model; the 2017 text recommends IFC 2x3 or higher and requires classified, uniquely identified elements, `tg-r036`), СП 328, **ГОСТ Р 21.101-2020** (design documentation, in force 2021-01-01), **ГОСТ Р 10.0.02-2019 / ИСО 16739-1:2018** (national adoption of IFC, in force 2019-09-01; see [glossary](../../08_glossary/glossary_multilingual.md)). The national doc also writes "10.0.03-2019" *(unverified; the glossary number 10.0.02 is the better-sourced one)*.
- Government decrees 331 and 1431: dates and scope *(unverified)*. Safe wording for tests: "decree-based obligation for budget-funded projects from about 2022, with exceptions; private projects only when the contract requires it".
- **Moscow АГР** (architectural and urban concept approval): from 2 April 2026 an IFC conforming to IDS is required, with the site exported as `IfcSite`; checked through the "Строим просто" service (Habr and business-press snippets; the order number quoted on Habr is ДГП-Р-1/26/64-16-6/26). See [IFC in real projects](../../01_ifc_basics/00_ifc_in_real_projects.md).
- **Expertise bodies**: Главгосэкспертиза (federal), Мосгосэкспертиза (Moscow; collection МКЭ ОД 24-178 with class-mapping appendices, `tg-r038`), СПб ГАУ ЦГЭ (publishes an IDS example, `habr-r014`), Мособлэкспертиза (IDS for roads, utilities, buildings, `tg-r025`). A regional TIM standard with an IFC export instruction exists for the Sverdlovsk region (`tg-r021`).
- **Classifiers**: **КСИ** (Классификатор строительной информации, on ФГИС ЦС; Minstroy order 430/пр of 2020-08-06 per the [classification doc](../../01_ifc_basics/07_materials_classification_types_styles.md)) and Moscow's **МССК**. Expect "код КСИ" / "код МССК" on elements and rooms. Whether codes go in `IfcClassificationReference` or a custom property is not settled in the data; one Telegram critique proposes `IfcClassificationReference` instead of hard-coded codes (`tg-r023`).

**Software (what Russian users actually name)**
- Foreign: Revit (dominant in the data), ArchiCAD, Tekla, Allplan, Navisworks, Solibri, AutoCAD, Plant 3D, SCAD-family analysis tools. Since 2022 vendor sales and support limits explain questions about moving models to domestic tools *(unverified specifics)*.
- Domestic: **Renga** (Renga Software, ASCON and 1C; IFC2x3 and IFC4, property mapping JSON in the `IFCMap` folder, IFC4 advised for merging, clashes and expertise), **nanoCAD BIM / СПДС** (Нанософт), **Model Studio CS** (CSoft), **Pilot-BIM / PilotICE** (ASCON, CDE), **SAPFIR-3D**, **Vitro-CAD** (views IFC, RVT, NWD), **Credo**, **BIM42** (online Revit-to-IFC converter), free viewer BIMvision (Poland). See [authoring tools](../../03_software/authoring_tools_ifc.md) and [viewers, checkers, CDEs](../../03_software/viewers_checkers_cde_converters.md).
- Revit-specific mechanics that appear in Russian posts: `IfcExportAs` shared parameter (value `-1` excludes an element, per Habr), user-defined property sets (UDPS), shared-parameter file (ФОП), export version and MVD choice. See [Revit IFC export](../../03_software/revit/ifc_export_reference.md) and [import and link](../../03_software/revit/ifc_import_link_reference.md).

**Enthusiasts and tools**
- Habr authors and plugin builders: AGR.Checker (Revit plugin checking against IDS before export), BIM Inspector (PIK), IDS Core (browser editor and validator), `i-savelev/BatchIfcExporter` and `ifc_checker` on GitHub, `roosslan/ifc_exporter_revit_addin`. Telegram: "Всё про IFC", BIMLIB, Академия BIM.
- Open source used in Russian posts: IfcOpenShell and ifctester, Bonsai (BlenderBIM), web-ifc and That Open, xBIM, `Autodesk/revit-ifc`. See [open-source libraries](../../04_open_source/libraries_and_toolkits.md).
- MCP and AI with Russian text: `streletskiy/archi-helper` (Archicad, README in Russian), `Davud77/bp-revit-tools` (MCP bridge plus Archicad-to-Revit via IFC), `LuDattilo/RevitCortex`. See [MCP servers](../../04_open_source/mcp_servers_and_ai_tools.md) and the [import/interoperability topic file](../by_topic/import_and_interoperability.md).

---

## 4. How people write

### 4.1 Register, length, structure
- **dwg.ru style (forum).** Title is a noun phrase naming the software pair or the symptom: "Экспорт из Tekla в Revit", "Как корректно открыть IFC", "Импорт IFC файлов в Revit 2022", "САПФИР-3D 2020 R2. Как правильно экспортировать модель в IFC?". Body: 1-4 sentences, no greeting, often lowercase, version and export settings missing, "файл приложил" instead of describing it. Customer pressure is the only context offered: "заказчик требует IFC". Closer: "помогло", "спасибо".
- **Habr style.** Long first-person retrospective with headings and numbers, mixed Latin/Cyrillic, humour ("перестали бояться валидатора"), weary pragmatism ("коварная вещь").
- **Telegram style.** Post = a link plus one or two lines of commentary; essay tone in analytical channels; hashtags such as `#IFC`; titles prefixed with channel name in this dataset.
- **Prompts to an AI assistant** (not directly observed in real data; inferred from the synthetic prompts and the forum register): imperative verbs, 8-25 words, no greeting, no file name, relies on "the loaded model". Median synthetic prompt: 14 words, longest 24. Treat this as a *bias* of the generator: real users also write a long paragraph with context, and some write formally ("Здравствуйте, подскажите, пожалуйста...").
- **Formal register** appears in regulation-adjacent writing: "в соответствии с требованиями", "прошу проверить", full words instead of abbreviations, plural "мы" for a team ("как нам проверять проект").

### 4.2 Openers and closers
| Where | Typical opener | Typical closer |
|---|---|---|
| Forum | none; straight to the symptom: "не происходит экспорт модели", "получается фигня" | "помогло", "всё пучком", thread revived with "а у меня то же самое" |
| Habr | story hook, then numbers | link to repo, "будем рады замечаниям" style |
| Prompt to assistant (synthetic) | "глянь", "покажи", "проверь", "выведи", "найди", "сделай" | a deadline or a constraint: "срочно", "до экспорта надо", "если нет Qto, скажи прямо" |
| Formal | "Здравствуйте", "Подскажите, пожалуйста" | "Заранее спасибо" |

### 4.3 Jargon and slang
Evidence tag: **R** = seen in real records or reports; **S** = only in synthetic prompts (assumption, plausible but unverified); **R/S** both.

| Term | Meaning | Standard term | Evidence |
|---|---|---|---|
| ТИМ | technologies of information modelling (the practice) | BIM | R |
| ЦИМ | digital information model, the deliverable file or model | BIM model / information model | R |
| АГР | architectural and urban concept approval (Moscow procedure) | planning concept approval | R |
| МГЭ / Мосгосэкспертиза, ЦГЭ (СПб), Мособлэкспертиза, ГГЭ | expertise bodies | design review authority | R |
| экспертиза | state design review before construction | design review / permitting | R |
| Строим просто, "строимпросто" | Moscow service where IFC is uploaded and checked | authority upload/validation portal | R |
| ТЭП | technical and economic indicators (areas, volumes) | building performance indicators | R |
| КСИ, МССК | classifiers (national; Moscow) | classification system | R |
| ФОП | shared-parameter file | shared parameters (Revit) | R |
| UDPS | user-defined property sets file for IFC export | custom property set mapping | R |
| `RUS_*` (RUS_Area, RUS_Height) | prefix of Russian parameter names required by Moscow АГР | custom properties | R |
| ифс, ифц, IFC-файл | IFC (spoken forms; Latin "IFC" dominates the stored paraphrases) | IFC | R in reports, S in prompts |
| ревит, Ревит, "в Ревите", Текла / "из Теклы", Архикад, Сапфир, нанокад, Навис / нависворкс, Ренга, Лира, СКАД, Старк | Revit, Tekla, ArchiCAD, SAPFIR-3D, nanoCAD, Navisworks, Renga, Lira, SCAD, STARK ES (transliterated and declined by case) | product names | R |
| проксики, прокси, "проксей" | `IfcBuildingElementProxy` (generic fallback class) | proxy elements | R ("прокси", "проксики"); the genitive "проксей" is S |
| "тела", "обобщённые модели", "мёртвая геометрия" | geometry that imported as dumb solids or Revit Generic Models, no editable object | DirectShape / generic model | R |
| "только оси" | only grids visible after import | missing phase or surface geometry issue | R |
| косоуры, пандус, дубли | stair stringers, ramp, duplicate elements | IfcMember / IfcRamp / duplicates | R |
| "зона", "помещение" | space-like objects exported to `IfcSpace`; which Revit object is meant varies | IfcSpace | R |
| склейка | merging models into one | federated model | R |
| выгрузка / выгружать, "затащить", "загрузить" | export; bring into | export / import | R |
| экспортнуть, импортнуть | colloquial verbs with English roots | export, import | R |
| "улетает", "уехала", "улетела на километры" | model lands far from the origin | coordinate offset | S (strongly plausible) |
| кракозябры | garbled text | mojibake | S |
| бцф | BCF issue file | BCF | S |
| психеты | property sets | Pset | S |
| CV2, RV, "2х3", "четвёрка" | Coordination View 2.0, Reference View, IFC2x3, IFC4 | MVD names | R (MasterDigitalTwin guide, synthetic) |
| "работа в стол" | work that will never be used | idiom | R |
| ГИП | chief project engineer (decision maker in regional guidance) | lead designer | R |
| КР / АР / ИОС | structural / architectural / engineering systems sections | disciplines | R (Moscow requirements) |
| ВОР, экспликация, смета | bill of work volumes, room list, cost estimate | BoQ, room schedule, cost plan | S |

### 4.4 Misspellings and name variants
- IFC written as Latin `IFC` (most common in stored paraphrases: 121 occurrences), as "ифс/ифц" (transliteration of the spoken form), and in one real video title as **`IFС` with a Cyrillic С** (`tg-r032`). A tool that matches "IFC" literally can miss it.
- Product names: Revit / Ревит; Tekla / Текла; ArchiCAD, Archicad, ArchiCad, Архикад; SAPFIR / САПФИР / Сапфир; Navisworks / Навис / нависворкс; Renga / Ренга.
- Case endings on foreign names: "в Ревите", "из Теклы", "в нависе", "из Архикада". Do not expect the name in nominative.
- Mixed Latin and Cyrillic in identifiers: `RUS_Area` next to Russian parameter names; `IFCGrid`, `IFCExportAs` in capitals in older articles (`sapr.ru`), `IfcExportAs` in Habr.
- Year-and-service names: "Revit 2022", "САПФИР-3D 2020 R2", "Plant 3D 2025", "Tekla Structures 2020 SP4/SP5".

### 4.5 Code-switching with English
- Error text is quoted in English inside a Russian sentence: "System Error encountered during import" (`tg-r003`).
- Names of schema objects stay English: `IfcSpace`, `GlobalId`, `Pset_WallCommon`, `Qto_WallBaseQuantities`, `IfcMapConversion`.
- Revit UI terms are often Russian when quoted from the localized interface ("Экспорт в IFC", "общие параметры"), English when quoted from the API or exporter options ("IfcExportAs", "Surface geometry"). Russian Revit says **типоразмер** for family type, **стадия** for phase, **связь** for link.
- Verbs: "экспортнуть", "импортнуть", "пушить" are plausible; only the first two are evidenced.

### 4.6 Tone
Pressure and fatigue dominate: deadline words ("завтра сдача", "до экспорта надо", "в понедельник"), irritation at slow exports and late errors, and ironic distance from regulation ("работа в стол", "коварная вещь"). Beginners sound confused and apologetic ("признаётся что новичок"). Developers sound dry and technical. Hostility appears only in comment sections of opinion pieces.

### 4.7 Context given and omitted
| Usually given | Usually omitted |
|---|---|
| The two software products and direction (Tekla to Revit) | Revit and IFC version, export settings, MVD |
| The symptom in one phrase ("только оси", "пропали зоны") | Which authority's requirements apply (it is "known" to the asker) |
| Customer or expertise pressure | File size, element counts, units |
| Exact error text (English) | Exporting application when it is third-party |
| A number when it matters (20 m2 gap, 1500 vs 200 clashes) | That a file or IDS is attached or already loaded (the asker assumes it) |

---

## 5. Real questions

104 records, grouped by theme. "Форма" shows the kind of source and year. The Russian column is a paraphrase (bold = verbatim title when 20 words or fewer). EN gloss is the dataset's gloss. IDs are short forms of the record ids (`tg` = `ru-autodesk-telegram`, `dwg` = `ru-dwg-other`, `habr` = `ru-habr-dev`, `rauto` = `ru-revit-auto`, `gh-enc` = `en-gh-encoding`), so each row is traceable to `research_raw/wave1/`. Answers (what solved it) are not repeated here; they are in the `answer_summary` field of the JSONL records.

Reading tip: the "ветка форума" rows are the closest thing to a real question typed by a person. "статья/блог" rows state a problem inside an article; "пост Telegram", "видео" and "нормативный/пресс-текст" rows are announcements or titles and are useful for vocabulary and topics, not as prompts.

### R1. Госэкспертиза, АГР, требования заказчика и нормативка (ТИМ, IDS)

| ID | Форма | Оригинал (заголовок / пересказ) | EN gloss | Персона | Источник |
|---|---|---|---|---|---|
| `tg-r001` | ветка форума, 2019 | **Экспертиза проекта, созданного в Revit**. с 01.07.2019 госэкспертиза требует BIM, как проверять проект в Revit или IFC, можно ли PDF и чертежи, как быть с 87 постановлением, методики нет | From 1 July 2019 state expertise reportedly requires BIM; how do we check a Revit project or IFC model, can PDF drawings be used instead? | bim_coordinator | [dwg.ru t=153428](https://forum.dwg.ru/showthread.php?t=153428) |
| `dwg-r017` | ветка форума, 2019 | **Экспертиза проекта, созданного в Revit**. нужно ли с 01.07.2019 переходить на ТИМ, можно ли работать в 2D и сдавать PDF | Since 01.07.2019 BIM is required?; can we keep 2D and PDF? Is IFC the format? | architect | [dwg.ru t=153428](https://forum.dwg.ru/showthread.php?t=153428) |
| `dwg-r025` | ветка форума, 2016 | **Обсуждение проекта СП информационное моделирование (стр.33)**. в проекте СП модель предъявляется в RVT и DWG, а IFC нет; элементы должны быть классифицированы | Draft national BIM standard recognizes RVT and DWG as model formats, not IFC? | bim_manager | [dwg.ru t=134394](https://forum.dwg.ru/showthread.php?t=134394&page=33) |
| `tg-r036` | нормативный/пресс-текст, 2017 | **СП 333.1325800.2017 Информационное моделирование в строительстве**. формат IFC 2x3 и выше для обмена моделями | SP 333 recommends exchanging digital models in IFC 2x3 or higher and requires elements to be classified and uniquely identified | reviewer_authority | [docs.cntd.ru](http://docs.cntd.ru/document/556793897) |
| `tg-r037` | нормативный/пресс-текст, 2021 | **Первый проект, полностью спроектированный на основе BIM-технологий, прошел госэкспертизу**. входные проверки: геометрия, классы IFC, атрибуты, коллизии | First fully BIM-designed project passed state expertise; two-stage check: geometry, IFC classes, attributes, clashes, then automated code checks | reviewer_authority | [minstroyrf.gov.ru](https://minstroyrf.gov.ru/press/pervyy-proekt-polnostyu-sproektirovannyy-na-osnove-bim-tekhnologiy-proshel-gosekspertizu/) |
| `tg-r038` | нормативный/пресс-текст, 2025 | **МКЭ ОД 24-178 (требования к ТИМ, части 2-4)**. требования к выгрузке элементов в IFC, соответствие классов IFC категориям | Collection of Moscow TIM requirements includes classification of CIM elements and rules for exporting elements to IFC with class mapping appendices | reviewer_authority | [digest.wizardsoft.ru](https://digest.wizardsoft.ru/wp-content/uploads/media/doc/2025/MKE-OD-24-178Chast3.pdf) |
| `tg-r021` | пост Telegram, 2025 | **RevitHelper: инструкция по экспорту ЦИМ из Revit в IFC**. коллеги из Минстроя Свердловской области написали инструкцию по экспорту ЦИМ из Autodesk Revit в IFC | Sverdlovsk region ministry wrote an instruction for exporting a CIM from Revit to IFC, to be part of the regional TIM standard | bim_manager | [t.me/revithelper_kmv](https://t.me/s/revithelper_kmv/146) |
| `tg-r025` | пост Telegram, 2026 | **Всё про IFC: Мособлэкспертиза в IDS**. новые BIM-требования в формате IDS | Mosoblexpertiza published new BIM requirements in IDS format for roads, utilities and buildings | reviewer_authority | [t.me/ifc_ru](https://t.me/s/ifc_ru) |
| `tg-r022` | пост Telegram, 2025 | **Всё про IFC: машиночитаемые требования**. перевести нормативку в OWL, SWRL, IDS сложно, без основы получится работа в стол | Turning human-readable regulations into machine-readable form (OWL, SWRL, IDS) is hard and may become 'work for the drawer' | researcher_academic | [t.me/ifc_ru](https://t.me/s/ifc_ru) |
| `tg-r023` | пост Telegram, 2026 | **Всё про IFC: критика методики цифровых требований**. семантический разрыв между сущностями требований и данными IFC, привязка к КСИ | Critique of a methodology for digital requirements: semantic gap with IFC data, per-software connectors, tied to the frequently changing KSI classifier | researcher_academic | [t.me/ifc_ru](https://t.me/s/ifc_ru) |
| `tg-r014` | статья/блог, 2025 | **Спецификация IDS в BIM: сценарии, ограничения, перспективы развития**. что такое IDS, где поддерживается, какие ограничения | What is IDS in BIM: scenarios, limits, tool support | bim_manager | [Habr 908192](https://habr.com/ru/articles/908192/) |
| `habr-r014` | статья/блог, 2025 | **Проверка IFC моделей по требованиям IDS**. как пакетно проверить кучу IFC по одному IDS и получить отчёт | How to check many IFC models against one IDS with ifcopenshell + ifctester and HTML reports | bim_manager | [Habr 883016](https://habr.com/ru/articles/883016/) |
| `habr-r015` | статья/блог, 2025 | **Спецификация IDS в BIM: сценарии, ограничения**. IDS не умеет геометрию и условную логику - что делать | IDS 1.0 cannot express geometry, spatial or conditional rules | bim_manager | [Habr 908192](https://habr.com/ru/articles/908192/) |
| `tg-r012` | статья/блог, 2025 | **Проверка IFC моделей по требованиям IDS**. как проверять IFC по IDS пакетно, с отчётами html и json | How to check IFC models against IDS requirements (example from SPb CGE) in batch with reports | developer_programmer | [Habr 883016](https://habr.com/ru/articles/883016/) |

### R2. Выгрузка ЦИМ для АГР: классы, параметры, зоны, ТЭП (Habr, 2026)

| ID | Форма | Оригинал (заголовок / пересказ) | EN gloss | Персона | Источник |
|---|---|---|---|---|---|
| `tg-r008` | статья/блог, 2026 | **Два часа выгрузки ради пустого параметра: проверяем ЦИМ для АГР внутри Revit**. тяжёлая модель выгружается 2 часа, ошибки видно только после загрузки в строимпросто, зоны пропадают, площади задваиваются | Heavy model exports IFC in 2 hours and errors only show after upload to the Moscow AGR checker; rooms vs zones, vanished zones, area overcounting | bim_coordinator | [Habr 1089018](https://habr.com/ru/articles/1089018/) |
| `tg-r009` | статья/блог, 2026 | **Как мы научили BIM Inspector проверять IFC-модели до выгрузки**. экспорт в IFC занимает от минут до часов, ошибки находим итерациями, у окон нет параметра RUS_Height | Since 2 April 2026 IFC conforming to IDS is required for MGE/AGR; every check needs a full slow export | bim_manager | [Habr 1057314](https://habr.com/ru/companies/pik_digital/articles/1057314/) |
| `tg-r010` | статья/блог, 2026 | **Постобработка IFC без Revit, часть 2: площади ТЭП, дубли и правки**. площади ТЭП в xml расходятся на 20 м2, дубли не найти, как править IFC без ревита и переслать правки | TEP areas differ ~20 m2 from AGR XML; duplicates hard to find; how to post-process IFC without Revit and share fixes without resending big files | bim_coordinator | [Habr 1100956](https://habr.com/ru/articles/1100956/) |
| `tg-r011` | статья/блог, 2026 | **AGR.Checker: как сэкономить время и нервы на проверке модели для АГР**. косоуры всё равно выгружаются при IfcExportAs нет, пандус уходит как IfcRampFlight, МССК коды помещениям вручную | Preparing a model for AGR: each element needs IFC class and attributes; stair stringers still export when set to No; ramp as IfcRampFlight needs another classifier code | bim_coordinator | [Habr 1098340](https://habr.com/ru/articles/1098340/) |
| `tg-r016` | статья/блог, 2026 | **Разработка и регистрация плагина под Revit: как АГР подтолкнул BIM-инженеров на разработку**. зачем писать плагин под АГР | How AGR requirements pushed BIM engineers into Revit plugin development and registration | developer_programmer | [Habr 1075736](https://habr.com/ru/articles/1075736/) |
| `habr-r001` | статья/блог, 2026 | **Два часа выгрузки ради пустого параметра**. таблица категория-класс врёт, в IFC класс берётся из параметров экспорта; в 2022 и старше только IfcExportAs | Revit category-to-IFC-class table is unreliable; export actually reads Export to IFC / IfcExportAs parameters | bim_coordinator | [Habr 1089018](https://habr.com/ru/articles/1089018/) |
| `habr-r002` | статья/блог, 2026 | **Два часа выгрузки ради пустого параметра (зоны)**. зоны с кривыми границами в Revit считаются, а в IFC не выгружаются как тело | Zones with imperfect boundaries compute area in Revit but fail IFC export (short segments, overlaps, self-intersections) | bim_coordinator | [Habr 1089018](https://habr.com/ru/articles/1089018/) |
| `habr-r003` | статья/блог, 2026 | **Два часа выгрузки ради пустого параметра (коллизии)**. Навис показывает 1500 коллизий, сервис 200 - почему разное число | Navisworks finds ~1500 clashes, the check service ~200 on the same model | bim_coordinator | [Habr 1089018](https://habr.com/ru/articles/1089018/) |
| `habr-r004` | статья/блог, 2026 | **Постобработка IFC в браузере с помощью IDS Core**. валидатор ругается, что площадь IfcArea а не IfcReal; глобальная замена в блокноте ломает Pset_* | Exporter writes areas/volumes as IfcArea or IfcLabel instead of IfcReal and the IDS validator rejects them | bim_coordinator | [Habr 1094224](https://habr.com/ru/articles/1094224/) |
| `habr-r007` | статья/блог, 2026 | **Постобработка IFC без Revit, часть 2: площади ТЭП**. площадь по геометрии зон не сходится с атрибутом и с XML АГР | Area of zones from geometry differs from RUS_Area attribute by 20.63 m2 vs AGR XML | bim_coordinator | [Habr 1100956](https://habr.com/ru/articles/1100956/) |
| `habr-r008` | статья/блог, 2026 | **Постобработка IFC без Revit, часть 2: дубли и правки**. как найти дубли в IFC которых не видно и переслать правки коллеге | Find and remove duplicate elements invisible in 3D; keep an edit journal keyed by GlobalId applicable to later exports | bim_coordinator | [Habr 1100956](https://habr.com/ru/articles/1100956/) |
| `habr-r009` | статья/блог, 2026 | **AGR.Checker: как сэкономить время и нервы**. стандартный параметр Экспорт в IFC ненадёжен: косоуры выгружаются при Нет; категория Стена - откатные ворота | Revit category does not determine IFC class; a Wall-category element turned out to be a sliding gate family | bim_coordinator | [Habr 1098340](https://habr.com/ru/articles/1098340/) |
| `habr-r010` | статья/блог, 2026 | **AGR.Checker (UDPS)**. как связать русские параметры Revit с именами свойств IFC | Map Revit parameters to IFC property names via User Defined Property Sets (e.g. ID участка -> LandID) | bim_coordinator | [Habr 1098340](https://habr.com/ru/articles/1098340/) |
| `habr-r011` | статья/блог, 2026 | **AGR.Checker: типичные ошибки**. числовой параметр не переносится, если не запятая; помещения не классифицируются по МССК | Numeric parameter in IFC needs a comma, otherwise value is not transferred; rooms not classified by MSSK | bim_coordinator | [Habr 1098340](https://habr.com/ru/articles/1098340/) |
| `habr-r012` | статья/блог, 2026 | **AGR.Checker: что нового**. косоуры лестниц и дубли кода МССК у пандусов - как чистить после экспорта | Post-export cleanup: remove stair stringers, fix MSSK codes copied from ramp to flights, remove IfcExportAs=-1 | bim_coordinator | [Habr 1087472](https://habr.com/ru/articles/1087472/) |
| `habr-r013` | статья/блог, 2026 | **AGR.Checker: что нового**. недокументированные опции IFC-экспортёра ведут себя по-разному, поэтому стандартное окно экспорта | Undocumented IFC exporter options behave differently between Revit versions | developer_programmer | [Habr 1087472](https://habr.com/ru/articles/1087472/) |

### R3. dwg.ru: IFC между программами (Revit, Tekla, Archicad, САПФИР, расчётные программы)

| ID | Форма | Оригинал (заголовок / пересказ) | EN gloss | Персона | Источник |
|---|---|---|---|---|---|
| `tg-r002` | ветка форума, 2019 | **Как корректно открыть IFC**. как открыть IFC в ревите корректно, выгружал экспортёром, импортированная модель кривая | How to open and work with IFC files in Revit; problems with a model exported by a third-party exporter | student_beginner | [dwg.ru t=154396](https://forum.dwg.ru/showthread.php?t=154396) |
| `dwg-r008` | ветка форума, 2019 | **Как корректно открыть IFC**. после экспорта в IFC из Ревита часть элементов и параметров потерялась, как проверить где проблема - в экспорте или в просмотрщике | Newcomer: Revit IFC export loses elements and parameters; how to check the exported data? | bim_coordinator | [dwg.ru t=154396](https://forum.dwg.ru/showthread.php?t=154396) |
| `habr-r028` | ветка форума, 2019 | **Как корректно открыть IFC**. Ревит не открывает IFC с 3D геометрией нормально, чем открыть | Revit cannot open IFC with 3D geometry properly; recommended xBIM viewer | structural_engineer | [dwg.ru t=154396](https://forum.dwg.ru/showthread.php?t=154396) |
| `tg-r003` | ветка форума, 2021 | **САПФИР-3D 2020 R2. Как правильно экспортировать модель в IFC?**. импортирую IFC из сапфира, выдаёт System Error encountered during import, как правильно экспортировать | IFC exported from SAPFIR gives 'System Error encountered during import' in Autodesk tools; how to export correctly? | structural_engineer | [dwg.ru t=160240](https://forum.dwg.ru/showthread.php?t=160240) |
| `dwg-r003` | ветка форума, 2021 | **САПФИР-3D 2020 R2. Как правильно экспортировать модель в IFC?**. IFC из Сапфира в автокад не импортируется, системная ошибка, в BimSight открывается нормально; как правильно экспортировать | IFC exported from SAPFIR opens in BIMsight but AutoCAD 2020 import fails with System Error; how to export/import correctly? | bim_coordinator | [dwg.ru t=160240](https://forum.dwg.ru/showthread.php?t=160240) |
| `habr-r030` | ветка форума, 2020 | **САПФИР-3D 2020 R2. Как правильно экспортировать модель в IFC?**. как правильно выгрузить в IFC из Сапфира | How to correctly export model to IFC from SAPFIR-3D 2020 R2 | architect | [dwg.ru t=160240](https://forum.dwg.ru/showthread.php?t=160240) |
| `tg-r004` | ветка форума, 2022 | **Импорт IFC файлов в Revit 2022**. при импорте IFC геометрия есть, но элементы не распознаются как объекты, пропадают параметры, нужно получить модель для чертежей | On IFC import geometry stays but elements are not real objects and properties are missing; which export settings or software to use? | bim_coordinator | [dwg.ru t=166052](https://forum.dwg.ru/showthread.php?t=166052) |
| `dwg-r009` | ветка форума, 2022 | **Импорт IFC файла в Revit 2022**. при импорте IFC архитектурных моделей из других программ элементы приходят как тела, а не как родные объекты Ревита, хочу их редактировать | Imported IFC elements come in as dumb solids instead of editable Revit objects; which import settings? | architect | [dwg.ru t=166052](https://forum.dwg.ru/showthread.php?t=166052) |
| `tg-r005` | ветка форума, 2018 | **Экспорт из Tekla в Revit**. как перекинуть модель из Теклы в Ревит, IFC не работает; позже свойства и геометрия теряются при импорте | Tekla IFC export did not work for moving a model into Revit; later revivals: lost properties and geometry, which IFC version? | structural_engineer | [dwg.ru t=146029](https://forum.dwg.ru/showthread.php?t=146029) |
| `dwg-r001` | ветка форума, 2018 | **Экспорт из Tekla в Revit**. через IFC конструкции из Теклы в Ревит не передаются нормально, при открытии в Ревите элементы теряются, подскажите как передать | Passing structures from Tekla to Revit via IFC loses elements on open in Revit; need another way. | structural_engineer | [dwg.ru t=146029](https://forum.dwg.ru/showthread.php?t=146029) |
| `dwg-r002` | ветка форума, 2018 | **Экспорт из Tekla в Revit (заказчик требует IFC)**. заказчик требует выдавать IFC и грузить в Ревит, стандартный экспорт с настройками по умолчанию даёт в Ревите только оси | Standard Tekla IFC export with default settings shows only grids in Revit while the customer demands IFC. | structural_engineer | [dwg.ru t=146029](https://forum.dwg.ru/showthread.php?t=146029) |
| `habr-r029` | ветка форума, 2018 | **Экспорт из Tekla в Revit**. в Ревите видны только оси из Tekla | Tekla to Revit IFC shows only axes; fixed by assigning a phase to the linked IFC | structural_engineer | [dwg.ru t=146029](https://forum.dwg.ru/showthread.php?t=146029) |
| `dwg-r013` | ветка форума, 2020 | **Почему не меняется материал и тонирование колонн в Revit 2020, экспортированных из Tekla?**. колонны из Теклы в Ревите: материал и тонирование не меняются; арматура и узлы не переносятся | Why can't I change material and shading of columns exported from Tekla in Revit 2020; rebar and connections not carried? | structural_engineer | [dwg.ru t=155997](https://forum.dwg.ru/showthread.php?t=155997) |
| `dwg-r014` | ветка форума, 2018 | **Tekla 2017. Экспорт в ifc для приложения Tekla Field 3D**. экспорт в ifc из Теклы 2017 для Field 3D не работает как надо, настройки не помогают | Tekla 2017 IFC export for Tekla Field 3D does not work as expected; changing settings does not help. | structural_engineer | [dwg.ru t=146367](https://forum.dwg.ru/showthread.php?t=146367) |
| `dwg-r018` | ветка форума, 2018 | **Вопросы по Tekla и Tekla BIMsight (стр.2)**. арматура неправильно отображается в BIMsight после экспорта, как передать свойства | Rebar shows wrongly in BIMsight after Tekla IFC export; how to export properties? | structural_engineer | [dwg.ru t=150272](https://forum.dwg.ru/showthread.php?t=150272&page=2) |
| `tg-r006` | ветка форума, 2016 | **Связка Revit-STARK ES. Не происходит экспорт модели**. не происходит экспорт модели из ревита в старк ес | Revit to STARK ES link: model export does not happen | structural_engineer | [dwg.ru t=133669](https://forum.dwg.ru/showthread.php?t=133669) |
| `dwg-r015` | ветка форума, 2016 | **Связка Revit-STARK ES. Не происходит экспорт модели**. не все элементы передаются из Ревита 2016 в Старк ЕС, IFC пробовала - результат плохой | Revit-to-STARK ES transfer drops elements; IFC tried, result unsatisfactory. | structural_engineer | [dwg.ru t=133669](https://forum.dwg.ru/showthread.php?t=133669) |
| `dwg-r029` | ветка форума, 2019 | **Как корректно открыть IFC**. при экспорте из Архикада в IFC и вставке в Ревит стёкла жёлтые и толщиной в метры, часть перегородок пропала | ArchiCAD IFC in Revit: glass yellow and meters thick, part of partitions/trusses missing; fix? | architect | [dwg.ru t=154396](https://forum.dwg.ru/showthread.php?t=154396) |
| `dwg-r023` | ветка форума, 2016 | **Как редактировать семейство в модели!?**. можно ли редактировать семейство из IFC в Ревите | Can an imported IFC be edited as a Revit family? | architect | [dwg.ru t=130296](https://forum.dwg.ru/showthread.php?t=130296&page=2) |
| `dwg-r010` | ветка форума, 2020 | **Ошибка импорта опорной модели IFC.**. Текла просит переименовать файл без спецсимволов, имя только латиница, не помогает | Tekla refuses to import an IFC asking to rename the file without special characters though the name is Latin; Cyrillic in header path suspected. | structural_engineer | [dwg.ru t=159943](https://forum.dwg.ru/showthread.php?t=159943) |
| `dwg-r011` | ветка форума, 2020 | **Вставить IFC в Autocad**. нужно открыть 3D модель IFC в автокаде, редактировать и проектировать по ней, у кого получилось | Need to open a 3D IFC model in AutoCAD, edit it and design on it; any workable method? | structural_engineer | [dwg.ru t=158006](https://forum.dwg.ru/showthread.php?t=158006) |
| `dwg-r007` | ветка форума, 2011 | **перевод модели из ifc (ArchiCAD) в r2s (Revit Structure) для препроцессора Forum-Scad**. есть проект в Архикаде 14, выгрузил в IFC, как перевести в r2s для Форум-Скад, есть ли конвертер | Have an ArchiCAD 14 model exported to IFC; how to convert to r2s for Forum-Scad? | structural_engineer | [dwg.ru t=76210](https://forum.dwg.ru/showthread.php?t=76210) |
| `dwg-r016` | ветка форума, 2013 | **Как пересести из ifc в dwg ?**. как перевести ifc в dwg и какими программами, работаю в Архикаде | How to convert IFC to DWG and with which programs? | architect | [dwg.ru t=96356](https://forum.dwg.ru/showthread.php?t=96356) |
| `dwg-r021` | ветка форума, 2011 | **Как из ArchiCad экспортнуть в DWG Solid?**. нужны тела DWG Solid а не сетки, цепочка Archicad-IFC2x3-AutoCAD Architecture | How to get Archicad geometry into AutoCAD as DWG solids rather than meshes? | architect | [dwg.ru t=75883](https://forum.dwg.ru/showthread.php?t=75883) |
| `dwg-r024` | ветка форума, 2012 | **Пересохранение файлов ArchiCAD**. как сохранить файл Архикада в IFC для открытия в младшей версии | How to resave ArchiCAD files to an older version via IFC? | architect | [dwg.ru t=75685](https://forum.dwg.ru/showthread.php?t=75685) |
| `dwg-r012` | ветка форума, 2021 | **Как из Advance Steel вывести модель в Archicad**. как обмениваются данными Advance Steel и Archicad, какая последовательность для правильной передачи модели | How to move a model from Advance Steel into Archicad, in what order? | structural_engineer | [dwg.ru t=163697](https://forum.dwg.ru/showthread.php?t=163697) |
| `dwg-r022` | ветка форума, 2020 | **Импорт 3D моделей из SolidWorks в Revit**. как лучше перенести 3D из Солида в Ревит, теряются ли параметры и материалы | Which format moves SolidWorks models into Revit; are parameters and materials kept? | architect | [dwg.ru t=159973](https://forum.dwg.ru/showthread.php?t=159973) |
| `dwg-r019` | ветка форума, 2017 | **Как импортировать стальной каркас из SCAD в Revit?**. как лучше передать конструктив из Ревита в СКАД, есть ли прямая связь, можно ли DWG/DXF | Best way to move a structural model from Revit to SCAD: direct link, DWG/DXF or IFC? | structural_engineer | [dwg.ru t=142967](https://forum.dwg.ru/showthread.php?t=142967) |
| `dwg-r020` | ветка форума, 2009 | **Создание или импорт расчетной схемы здания (СКАД, Лира, Мономах, Робот)**. как перенести модель из архитектурной программы в расчётную, какой формат лучше, через IFC можно? | Which format best moves an Archicad model into analysis software; IFC import to SCAD gives odd wall junctions. | structural_engineer | [dwg.ru t=33352](https://forum.dwg.ru/showthread.php?t=33352) |
| `dwg-r005` | ветка форума, 2015 | **Bocad-3D (и не только): передача данных в формате IFC**. умеет ли Bocad работать с IFC, можно ли импортировать/экспортировать модель в другие программы | Can Bocad-3D exchange IFC with other software; what works and what breaks (bolts, bracing)? | structural_engineer | [dwg.ru t=126080](https://forum.dwg.ru/showthread.php?t=126080) |
| `dwg-r030` | ветка форума, 2012 | **Передача 3D модели Заказчику**. чем проверить корректность IFC, атрибуты могут не дойти | How to validate IFC from Archicad; attributes may not survive in AutoCAD. | bim_manager | [dwg.ru t=34919](https://forum.dwg.ru/showthread.php?t=34919&page=3) |
| `tg-r007` | ветка форума, 2025 | **Получение IFC файла на основе проекта AutoCAD Plant 3d 2025**. как получить IFC из Plant 3D 2025, штатно часть элементов не выгружается | How to get an IFC from an AutoCAD Plant 3D 2025 project? | developer_programmer | [dwg.ru t=173570](https://forum.dwg.ru/showthread.php?t=173570) |
| `dwg-r004` | ветка форума, 2025 | **Получение IFC файла на основе проекта AutoCAD Plant 3d 2025**. нужно выгрузить 3D модель из Plant 3D в IFC; Codemill платный и с ручным маппингом, через Navisworks не экспортирует, в Ревите объекты не распознаются | How to get an IFC from a Plant 3D 2025 project without losing 3D objects and data? | developer_programmer | [dwg.ru t=173570](https://forum.dwg.ru/showthread.php?t=173570) |

### R4. Renga, nanoCAD, отечественное ПО и облачные СОД

| ID | Форма | Оригинал (заголовок / пересказ) | EN gloss | Персона | Источник |
|---|---|---|---|---|---|
| `tg-r017` | статья/блог, 2021 | **Как принять IFC**. часть свойств потерялась после импорта IFC, какие настройки экспорта выбрать, почему файл не читается | Why are properties missing after IFC import and which export settings to use from Renga (Reference View vs editable geometry)? | architect | [blog.rengabim.com](https://blog.rengabim.com/2021/08/ifc.html) |
| `tg-r018` | статья/блог, 2022 | **Больше 10 форматов экспорта/импорта в Renga. Какой из них выбрать?**. какой формат выбрать для экспертизы, коллизий, расчёта | Which of 10+ Renga export formats to choose; IFC4 for coordination, clashes, calculations or expertise | bim_manager | [rengabim.com](https://rengabim.com/stati/bol-she-10-formatov-eksporta-importa-v-renga-kakoj-iz-nih-vybrat/) |
| `tg-r019` | статья/блог, 2019 | **СПДС GraphiCS 2019 и nanoCAD СПДС 9.0. Работа с IFC из Revit**. ревит надо настроить заранее: оси в IFCGrid, IFCExportAs в ФОП, разбивка стен по уровням | How to export plans from Revit via IFC to nanoCAD SPDS: map grids to IfcGrid, IfcExportAs in shared params, split walls by levels | architect | [sapr.ru](https://sapr.ru/article/25825) |
| `dwg-r026` | справка вендора, 2024 | **Экспорт атрибутов объектов (справка Renga)**. как добавить свойство Renga в экспорт IFC | How does Renga decide which properties go to IFC? | bim_manager | [manual.rengabim.com](https://manual.rengabim.com/ehksport_atributov_obektov.html) |
| `dwg-r028` | статья/блог, 2022 | **Проходим госэкспертизу информационной модели правильно (Renga)**. при выгрузке в Navisworks SweptSolid отображается некорректно, нужна Tessellation | What geometry representation should Renga IFC use for Navisworks? | bim_coordinator | [rengabim.com](https://rengabim.com/stati/prohodim-gosekspertizu-informacionnoj-modeli-pravilno/) |
| `tg-r027` | пост Telegram, 2022 | **Просто о BIM: форматы в облачных СОД**. IFC-выгрузка сейчас в разработке, форматы нельзя называть собственными | Are PilotICE web formats proprietary? IFC export from CAD API is under development | bim_manager | [t.me/prostobim](https://t.me/s/prostobim?before=267) |
| `tg-r028` | пост Telegram, 2024 | **Академия BIM: вебинар Vitro-CAD 2024.1**. просмотр IFC, RVT, NWD моделей с серверной конвертацией | Vitro-CAD adds viewing of IFC, RVT, NWD with server-side conversion | bim_manager | [t.me/bimacad](https://t.me/s/bimacad?before=557) |
| `tg-r030` | пост Telegram, 2023 | **BIM Solutions: онлайн-конвертер Revit в IFC**. онлайн-инструмент преобразования Revit в IFC без лицензии | BIM42 built an online tool converting Revit files to IFC | bim_coordinator | [t.me/bimsk](https://t.me/s/bimsk?before=133) |

### R5. Мнения, выбор ПО, потери данных, споры

| ID | Форма | Оригинал (заголовок / пересказ) | EN gloss | Персона | Источник |
|---|---|---|---|---|---|
| `dwg-r006` | ветка форума, 2018 | **Renga для конструктора, реальная альтернатива ?**. стоит ли переходить на Renga вместо Ревита, как у неё с обменом через IFC | Is Renga usable for design instead of Revit/ArchiCAD, including IFC exchange? | architect | [dwg.ru t=149046](https://forum.dwg.ru/showthread.php?t=149046) |
| `dwg-r027` | статья/блог, 2018 | **Сравнение Revit, Tekla и Allplan для конструктора КЖ**. что выбрать конструктору КЖ: Revit, Tekla или Allplan | Compare Revit, Tekla, Allplan for reinforced concrete; which handles IFC links better? | structural_engineer | [dwg.ru](https://dwg.ru/b/utrfm/263) |
| `tg-r020` | статья/блог, 2020 | **sapr.ru: потери данных при конвертации в IFC**. при каждой конвертации в IFC и обратно теряются данные, элементы возвращаются мёртвой геометрией | With each IFC round trip data is lost; elements come back from IFC as non-editable dead geometry | bim_manager | [sapr.ru](https://sapr.ru/article/24777) |
| `habr-r018` | статья/блог, 2024 | **Мир после BIM**. объёмы в Ревите 17 кликов, в ifcopenshell 40 строк; IFC слишком сложный | Quantity takeoff is 17 clicks in Revit/Solibri vs ~40 lines in IfcOpenShell; flat formats beat IFC | developer_programmer | [Habr 868186](https://habr.com/ru/articles/868186/) |
| `habr-r019` | статья/блог, 2024 | **Эпоха перемен: IFC уходит в прошлое**. Autodesk бросит IFC ради USD? | Autodesk may abandon IFC for USD; Revit IFC depends on ODA SDK | developer_programmer | [Habr 860936](https://habr.com/ru/articles/860936/) |
| `habr-r020` | ветка форума, 2021 | **Open Source в строительстве. IFC и buildingSMART (комментарии)**. для редких объектов хватит Proxy - нет, это костыль, нужен ручной маппинг | Commenters argue IfcBuildingElementProxy is enough for rare classes; author calls it a crutch | developer_programmer | [Habr 590819 (комм.)](https://habr.com/ru/articles/590819/comments/) |

### R6. Обучение, инструкции, видеоуроки, каналы

| ID | Форма | Оригинал (заголовок / пересказ) | EN gloss | Персона | Источник |
|---|---|---|---|---|---|
| `tg-r015` | статья/блог, 2019 | **Industry Foundation Classes. Краткое введение**. что такое IFC вообще | Short introduction to Industry Foundation Classes | student_beginner | [Habr 460719](https://habr.com/ru/post/460719/) |
| `habr-r021` | статья/блог, 2019 | **Industry Foundation Classes. Краткое введение**. как устроен IFC файл, как руками написать минимальный | Short intro to IFC: STEP file structure, units, project/site/building/storey, write a file by hand | student_beginner | [Habr 460719](https://habr.com/ru/articles/460719/) |
| `tg-r026` | пост Telegram, 2026 | **Всё про IFC: курс по постобработке IFC**. курс для начинающих по правке IFC в Blender Bonsai | Beginner course on IFC post-processing in Blender + Bonsai: change schema and classes, batch-fill parameters, merge files | student_beginner | [t.me/ifc_ru](https://t.me/s/ifc_ru) |
| `tg-r031` | инструкция вендора, 2023 | **Инструкция по выгрузке IFC из Revit (MasterDigitalTwin)**. версия IFC и MVD критичны; связи выгружаются отдельным IFC; наборы параметров по умолчанию отключены | Russian PDF guide for IFC export from Revit: choose IFC2x3 CV2.0 or IFC4 RV, linked files exported separately, Revit parameter sets off by default | bim_coordinator | [iek-digital.ru](https://iek-digital.ru/upload/iblock/685/4jzi0mt4ob86xb78imiswfg6dngrrots/Instruktsiya-po-eksportu-IFC-dlya-REVIT.pdf) |
| `tg-r032` | видео, 2021 | **Лекция 8.4. Экспорт в IFС связь, IFC Viewers (Revit_#СВОИ)**. лекция про экспорт в IFC и просмотрщики | Lecture: exporting to IFC, links and IFC viewers (Revit course) | student_beginner | [YouTube](https://www.youtube.com/watch?v=VPlQf3fv908) |
| `tg-r033` | видео, 2020 | **[Урок Revit Structure] Экспорт в расчетные программы через IFC**. экспорт в расчётные программы через IFC | Revit Structure lesson: export to calculation programs via IFC | structural_engineer | [YouTube](https://www.youtube.com/watch?v=z1BcpIq3Tss) |
| `tg-r034` | видео, 2021 | **Revit. Как выставить модель в абсолютные координаты**. как выставить модель в абсолютные координаты | Revit: how to place the model in absolute coordinates | civil_infra_engineer | [YouTube](https://www.youtube.com/watch?v=r6_pYyH7Vgc) |
| `tg-r035` | видео, 2022 | **Все о точках в Revit. Базовая точка, точка съёмки и внутреннее начало**. базовая точка, точка съёмки, внутреннее начало | All about points in Revit: project base point, survey point, internal origin | bim_coordinator | [YouTube](https://www.youtube.com/watch?v=soPG0YMueqY) |

### R7. Разработчики: постобработка IFC, IfcOpenShell, web-ifc, xBIM, Revit API, ИИ/MCP

| ID | Форма | Оригинал (заголовок / пересказ) | EN gloss | Персона | Источник |
|---|---|---|---|---|---|
| `tg-r013` | статья/блог, 2026 | **Постобработка IFC в браузере с помощью IDS Core**. правка IFC в браузере и повторная проверка по IDS | Post-processing and fixing IFC in the browser with IDS Core so the validator stops being scary | developer_programmer | [Habr 1094224](https://habr.com/ru/articles/1094224/) |
| `tg-r029` | пост Telegram, 2026 | **BIMLIB: Постобработка IFC в браузере**. бонус к выходным, валидатор перестанет пугать | Weekend bonus: IFC post-processing in the browser with IDS Core (Habr link) | developer_programmer | [t.me/bimlib_pro](https://t.me/s/bimlib_pro) |
| `tg-r024` | пост Telegram, 2026 | **Всё про IFC: визуальный редактор IDS**. редактор доступен только через VPN, для больших спецификаций неудобен | Visual IDS editor reachable only via VPN and unwieldy for large real specifications | developer_programmer | [t.me/ifc_ru](https://t.me/s/ifc_ru) |
| `habr-r005` | статья/блог, 2026 | **Постобработка IFC в браузере с помощью IDS Core (удаление и смена класса)**. удалил элемент - файл открывается, но валидатор падает; смена класса требует смены типа | Deleting elements or changing class via web-ifc passes basic checks but breaks strict schema validation | developer_programmer | [Habr 1094224](https://habr.com/ru/articles/1094224/) |
| `habr-r006` | статья/блог, 2026 | **Постобработка IFC без Revit, часть 2**. после переписывания сущности web-ifc показывает старый класс | web-ifc keeps the original class of a rewritten entity so viewer and IDS show old class | developer_programmer | [Habr 1100956](https://habr.com/ru/articles/1100956/) |
| `habr-r016` | статья/блог, 2023 | **Создаём с нуля своё BIM-приложение для просмотра IFC в браузере**. как с нуля сделать просмотрщик IFC в браузере на IFC.js | Build a simple browser IFC viewer with IFC.js | developer_programmer | [Habr 759230](https://habr.com/ru/articles/759230/) |
| `habr-r017` | статья/блог, 2024 | **Как мы делали просмотрщик BIM-моделей**. Discord удалили, документация пропала; GLTF в разы больше IFC; остались на 1.5.1 | IFC.js project shut down, Discord deleted, docs vanished; GLTF bigger than IFC; settled on v1.5.1 | developer_programmer | [Habr 846382](https://habr.com/ru/articles/846382/) |
| `habr-r022` | статья/блог, 2025 | **IFC-Ассоциации или как подружить элементы и документы**. как привязать документ и согласование к стенам правкой текста IFC | Link walls to documents and approvals by adding IFCDOCUMENTINFORMATION/IFCRELASSOCIATESDOCUMENT in a text editor | developer_programmer | [Habr 882890](https://habr.com/ru/articles/882890/) |
| `habr-r023` | статья/блог, 2026 | **Параметрическая геометрия в IFC4**. параметрика теряется при экспорте из Revit/ArchiCAD, остаётся геометрия | Bonsai stores parametric recipe as JSON in BBIM_ psets; Revit/ArchiCAD lose recipe on IFC export | developer_programmer | [Habr 1063062](https://habr.com/ru/articles/1063062/) |
| `habr-r024` | GitHub, 2025 | **BatchIfcExporter**. выгрузить пачку rvt в IFC с разными настройками, экономя память | Batch export many .rvt to IFC with per-model Excel/JSON settings and workset exclusion | bim_coordinator | [GitHub i-savelev/BatchIfcExporter](https://github.com/i-savelev/BatchIfcExporter) |
| `habr-r025` | GitHub, 2025 | **ifc_exporter_revit_addin**. аддон экспорта IFC/NWC в Revit 2023 и 2026 | Revit add-in with IFC/NWC export button, builds for 2023 (.NET 4.8) and 2026 (.NET 8) | developer_programmer | [GitHub roosslan/ifc_exporter_revit_addin](https://github.com/roosslan/ifc_exporter_revit_addin) |
| `habr-r026` | GitHub, 2026 | **bp-revit-tools (BotPlus RT)**. перенести модель из Archicad в Revit через IFC и управлять Revit из ИИ-клиента | Plugin combining MCP bridge, Archicad-to-Revit transfer via IFC/Tapir and HVAC calcs | architect | [GitHub Davud77/bp-revit-tools](https://github.com/Davud77/bp-revit-tools) |
| `habr-r027` | GitHub, 2022 | **INQ: IFCopenshell - Revit (issue 777)**. IFC из ifcopenshell в Revit не становится семейством | IFC created via ifcopenshell opens in Revit as a wall but not a native family | architect | [GitHub Autodesk/revit-ifc](https://github.com/Autodesk/revit-ifc/issues/777) |
| `habr-r031` | ветка форума, 2024 | **Revit API. Как получить список глобальных параметров связи rvt**. API: глобальные параметры связанного rvt | How to get the list of global parameters of a linked rvt in Revit API | developer_programmer | [cyberforum.ru](https://www.cyberforum.ru/csharp-beginners/thread3129703.html) |
| `habr-r032` | GitHub, 2025 | **IFCViewer (xBIM)**. просмотрщик IFC на C# xBIM | C#/WPF IFC viewer with xBIM showing tree, properties | developer_programmer | [GitHub troyyu527/IFCViewer](https://github.com/troyyu527/IFCViewer) |
| `habr-r033` | GitHub, 2025 | **PDF-to-IFC**. PDF -> IFC на питоне, установка на Windows | PDF to IFC converter with Windows install notes | developer_programmer | [GitHub KashlakovNikita/PDF-to-IFC](https://github.com/KashlakovNikita/PDF-to-IFC) |
| `habr-r034` | GitHub, 2026 | **RevitCortex / Horizun MCP**. MCP для Revit: IFC export, IDS проверка | Multiple MCP servers connect Claude to Revit with IFC export/IDS tools | developer_programmer | [GitHub LuDattilo/RevitCortex](https://github.com/LuDattilo/RevitCortex) |

### R8. Прочее (кодировка, параметры семейств)

| ID | Форма | Оригинал (заголовок / пересказ) | EN gloss | Персона | Источник |
|---|---|---|---|---|---|
| `rauto-r032` | ветка форума, 2026 | можно ли настроить параметр семейства так, чтобы значения применялись автоматически при загрузке семейства | Is there a way to set family parameter values to apply automatically when the family is loaded | bim_coordinator | [dwg.ru t=175384](https://forum.dwg.ru/showthread.php?t=175384) |
| `gh-enc-r017` | GitHub, 2023 | **Swood Design (SolidWorks) - IFC read error**. IFCBUILDINGELEMENTPROXY name mixes \X2\ escapes with raw Cyrillic; Python exception on read | SolidWorks IFC has Cyrillic names written raw alongside \X2\ pieces, Python read fails. | structural_engineer | [GitHub IfcOpenShell/IfcOpenShell](https://github.com/IfcOpenShell/IfcOpenShell/issues/3182) |

---

## 6. Ready test prompts

All prompts below are **synthetic** (written by us, inspired by the real records and by the earlier synthetic cells; never quote them as human posts). They are curated: duplicates across cells were merged (the sentence "глянь сколько в модели проксей..." existed in six cells), wording was roughened or formalised to match a register, and several new prompts were added to cover gaps (formal register, boundary cases, confirm-before-write).

**Tag legend.** `intent` uses the KB vocabulary. Difficulty: easy / medium / hard. **F** = assumes an IFC model (or live Revit project) is already loaded; **-** = knowledge question, no file. Register: **TG** short chat/Telegram style, **FORUM** dwg.ru style, **FORMAL** polite/official, **LONG** paragraph with context, **STUD** student. "Based on" gives the synthetic record it was derived from (`s:` + short id, see section 5 for id prefixes) or `new`; `r:` marks a real record that inspired it.

**What a judge should check in every answer (global rules).**
1. Answers must come from the loaded file, not from guesses. If a required property set, quantity, classification or georeference is absent, say so plainly instead of inventing a value.
2. A checker cannot certify that Главгосэкспертиза, Мосгосэкспертиза or the Moscow АГР service will accept a model. It can report schema, view, classes, properties, classification and geometry facts.
3. Do not invent decree numbers, clause numbers, EPSG codes or КСИ/МССК codes. National facts marked *(unverified)* in [Russia national doc](../../02_standards_regulations/national/russia.md) must be hedged.
4. Cyrillic must survive: names and property values should be shown in readable Russian, not as `\X2\` escapes or mojibake.
5. Modification requests: write to a **new copy**, keep `GlobalId`, report counts, leave everything else untouched.
6. Never claim the user's wording is wrong. Interpret "ифс", "проксики", "зоны", "бцф" as IFC, proxy elements, spaces, BCF.

### P1. Readiness for expertise, АГР and customer requirements

| # | Prompt (RU) | Tags | Expected behavior (EN) | Based on |
|---|---|---|---|---|
| P-001 | завтра сдача в АГР, проверь что у всех окон заполнен RUS_Height и не пустой, выдай список без параметра | validate_check, easy, F, TG | Iterate `IfcWindow`; read `RUS_Height` in every property set; list GlobalId, name, storey of windows where it is missing or empty; do not claim АГР acceptance. | s:at-s002; r:tg-r009 |
| P-002 | надо сдавать на экспертизу в понедельник, проверь ифс что у всех стен и перекрытий заполнены обязательные свойства по требованиям заказчика, список пустых выгрузи | validate_check, medium, F, TG | Ask for or read the requirement list (ТЗ/IDS); without it, state that "обязательные свойства" are unknown and propose checking a stated list; then report empty values grouped by class and storey. | s:tim-s001 |
| P-003 | проверь модель по этому IDS от ЦГЭ и дай сводку нарушений по классам, самые частые сверху | validate_check, medium, F, TG | Run IDS validation (ifctester or equivalent); aggregate failures by specification and IFC class; give sample GlobalIds; note IDS 1.0 cannot express geometry or conditional rules. | s:at-s012; r:habr-r014 |
| P-004 | Проверьте ifc на соответствие требованиям к ТИМ для государственной экспертизы: классы, этажи, обязательные свойства. Что не заполнено? | validate_check, hard, F, FORMAL | Check class assignment, storey containment and properties; list gaps; state that the exact requirement list must be supplied and that acceptance cannot be certified. | s:permit-s006 |
| P-005 | ну и по итогам твоей проверки — экспертиза это точно пропустит? | request_opinion, medium, F, TG | Do not promise acceptance. Separate what was checked (schema, classes, properties, classification) from what depends on the authority's own validator and reviewers. | new (boundary) |
| P-006 | для экспертизы какой ифс выгружать, 2х3 или 4, и какой вид, CV2 или RV? | how_to, easy, -, TG | Answer depends on the authority and customer: СП 333 allows 2x3 and higher, Moscow АГР cases use IFC4 with IDS; explain CV2.0 vs Reference View briefly; ask which authority. No single universal answer. | s:at-s015, s:vm-s005 |
| P-007 | принимает ли экспертиза IFC4x3? | understand_concept, easy, -, TG | Say it is not confirmed in the KB; versions named in practice are 2x3 and 4; advise checking the requirements of the specific body. Do not invent acceptance rules. | new; r:dwg-r017 |
| P-008 | чем IFC отличается от XML-схемы ЦИМ для экспертизы? надо делать и то и другое? | understand_concept, easy, -, STUD | IFC is the geometric and semantic model; the XML is a structured description required in some procedures *(unverified in KB)*; advise verifying current official requirements; no invented schema names. | s:tim-s011 |
| P-009 | с какого года ТИМ обязателен для бюджетных объектов, и касается ли это частного заказчика? | understand_concept, medium, -, FORMAL | Hedged summary: decree-based obligation for budget-funded projects from about 2022 with exceptions; private projects only if the contract or financing requires it; recommend checking the official decree text; no invented decree numbers. | new; [russia.md](../../02_standards_regulations/national/russia.md) |
| P-010 | можно ли с 2019 года вообще сдавать на экспертизу PDF и 2D, или уже только модель? | comply_regulation, medium, -, FORUM | Explain that the 2019 forum threads were confused; state that current obligation depends on project funding and region; BIM is a process, IFC an exchange format; no firm legal claim without source. | r:dwg-r017, r:tg-r001 |
| P-011 | сверь ЦИМ с правилами Мосгосэкспертизы: соответствие классов IFC категориям и имена параметров. сначала скажи что ты можешь проверить сам | comply_regulation, hard, F, LONG | List what is checkable without the document (class vs Revit category in ObjectType, property names present); ask for the МКЭ ОД 24-178 mapping tables; do not invent the mapping. | r:tg-r038 |
| P-012 | проверь что все элементы привязаны к этажам, нет ли висящих вне IfcBuildingStorey | validate_check, easy, F, TG | Find products without containment in a storey (`IfcRelContainedInSpatialStructure`); list by class; separately mention elements aggregated through other relations. | s:tim-s004 |
| P-013 | АГР требует чтобы участок выгружался как IfcSite. проверь есть ли он и какие у него координаты | validate_check, medium, F, TG | Check presence of `IfcSite`, name, `RefLatitude/RefLongitude/RefElevation`, placement; report if absent; no assumption about МСК. | new; [real projects](../../01_ifc_basics/00_ifc_in_real_projects.md) |
| P-014 | У всех ли помещений в загруженном IFC есть код классификатора КСИ? Если нет, перечислите какие. | validate_check, medium, F, FORMAL | Look for `IfcClassificationReference` (system named КСИ) and a custom property; list spaces without a code; state which mechanism was found. | s:classbsdd-s007 |
| P-015 | у экспертов замечание: "модель не соответствует требованиям заказчика". Какие замечания по ифс я вообще могу получить и какие из них ты можешь проверить заранее? | understand_concept, medium, F, LONG | Give typical categories (elements without КСИ code, spaces missing area/name, wrong storey, mismatched coordinates, file size) marked as illustrative; check the ones testable on the file. | new; [russia.md](../../02_standards_regulations/national/russia.md) |
| P-016 | Привет. Заказчик прислал IDS на 40 требований, а у меня IFC из Revit. Прогони и скажи, какие требования вообще невыполнимы из-за того как у меня настроен экспорт, а не из-за пустых значений | validate_check, hard, F, LONG | Run IDS; separate failures caused by missing export mapping (property absent in all elements) from empty values; point to `IfcExportAs`, user-defined property sets. | new; r:habr-r003 |

### P2. Classification (КСИ, МССК)

| # | Prompt (RU) | Tags | Expected behavior (EN) | Based on |
|---|---|---|---|---|
| P-017 | покажи элементы у которых не проставлен код КСИ, сгруппируй по классу IFC | query_model_data, medium, F, TG | Group elements lacking a KSI code by IFC class with counts; state which representation was searched. | s:tim-s002 |
| P-018 | код классификатора из параметра ревита не попадает в ифс, в настройках экспорта указал, а в IfcClassificationReference пусто. почему | troubleshoot_export, medium, F, TG | Check whether any classification references exist; compare with the parameter name used; explain export options and the typical mismatch; do not claim the cause without evidence. | s:classbsdd-s008 |
| P-019 | проставь код МССК помещениям по названию, где неоднозначно не трогай, выведи список | modify_model_data, hard, F, TG | Apply a code only on exact name match from a supplied table; list ambiguous rooms untouched; new copy; refuse to invent codes if no table is given. | s:habr-s013; r:habr-r011 |
| P-020 | КСИ в ифс это IfcClassificationReference или просто свойство? как у меня сделано? | query_model_data, medium, F, FORUM | Inspect and report which form is used; note that the form required by an authority is not settled in the KB. | r:tg-r023 |
| P-021 | у пандусов и их маршей один и тот же код МССК, это ошибка? найди такие | validate_check, hard, F, TG | Find ramp and ramp-flight elements sharing a code; show pairs with class; explain that the data suggest codes copied from parent to children, flag as likely issue, do not assert a rule. | r:habr-r012 |
| P-022 | что такое КСИ и обязателен ли он на моём объекте? | understand_concept, easy, -, STUD | Plain explanation: national construction information classifier on ФГИС ЦС; used where an information model is mandatory; links to МССК in Moscow; hedge on obligation. | new; [classification doc](../../01_ifc_basics/07_materials_classification_types_styles.md) |

### P3. IFC classes, proxies, export mapping

| # | Prompt (RU) | Tags | Expected behavior (EN) | Based on |
|---|---|---|---|---|
| P-023 | глянь сколько в модели проксиков и из каких категорий ревита они пришли, надо понять что перемапить | query_model_data, medium, F, TG | Count `IfcBuildingElementProxy`; group by Revit category or ObjectType; propose `IfcExportAs` or mapping fixes; no changes. | s:proxy-s001, s:coord-s007, s:at-s001 |
| P-024 | почему после экспорта у меня всё стало IfcBuildingElementProxy?? препод сказал так не должно быть | troubleshoot_export, medium, F, STUD | Count proxies by source; explain class mapping at export, mapping file and `IfcExportAs`; teach, don't blame. | s:p-student-s010 |
| P-025 | косоуры лестниц опять в ифс хотя стоит не выгружать, найди их и скажи по какому классу ушли | validate_check, medium, F, TG | Find stringers by name/type; report IFC class and Revit category; suggest `-1` in `IfcExportAs` or post-processing deletion. | s:at-s008; r:habr-r012 |
| P-026 | перебей класс у всех IfcBuildingElementProxy с именем "Ограждение*" на IfcRailing и сохрани новую версию, оригинал не трогай | modify_model_data, medium, F, TG | Select by name pattern, change entity (and predefined type if applicable), keep GlobalId, write a copy, report count. | s:at-s009 |
| P-027 | все проксики с именем Колонна_* переведи в IfcColumn вместе с типом чтобы валидатор не ругался, остальное не трогай | modify_model_data, hard, F, TG | Change class and associated type consistently; validate schema afterwards; write a copy; list changed ids. | s:habr-s008, s:dwg-s007; r:habr-r005 |
| P-028 | в ревите стена-откатные ворота ушла в IFC как стена. как сделать чтобы класс брался из моего параметра IfcExportAs а не из категории | how_to, medium, -, FORUM | Explain that the exporter reads the export-as parameter and mapping, category is not authoritative; `-1` excludes; versions differ so verify in the user's Revit version. | r:habr-r009 |
| P-029 | у всех типов обобщённых моделей с "Колонна" в имени проставь IfcExportAs=IfcColumn, остальные не трогай | modify_model_data, medium, F, TG | Live Revit: list matching family types first, set the parameter only there, report changed list; ask confirmation before writing. | s:proxy-s011 |
| P-030 | арматура из Теклы пришла как IfcReinforcingBar или опять прокси? диаметры и общая длина по классам | query_model_data, medium, F, TG | Count `IfcReinforcingBar` vs proxies named rebar; list diameters; sum lengths; if absent explain known export limits. | s:struct-s006, s:dwg-s006 |
| P-031 | в ифс из ренги какие элементы вообще без свойств, ни одного pset | validate_check, easy, F, TG | List products with no `IfcRelDefinesByProperties`, grouped by class, with counts and examples. | s:renga-s001 |
| P-032 | таблицей: класс IFC, сколько штук, сколько из них без базовых количеств | query_model_data, medium, F, TG | Count elements per class; count lacking `IfcElementQuantity`; highlight classes where nearly all are missing. | s:qto-s010 |
| P-033 | в ифс окно экспортировалось как IfcWindow, а в типе стоит IfcDoorType. как так? | validate_check, hard, F, TG | Compare occurrence class with type class; list mismatches; explain possible cause (export-as set on type vs instance) without asserting. | new |

### P4. Properties and data types

| # | Prompt (RU) | Tags | Expected behavior (EN) | Based on |
|---|---|---|---|---|
| P-034 | выгрузил в ифс а мои общие параметры (Марка_ЕСКД, Огнестойкость) куда-то пропали. проверь есть ли они хоть в каких-то псетах у стен | validate_check, medium, F, TG | Search all property sets of `IfcWall` for those names, with spelling variants; report presence and pset, or absence; explain user-defined property set export. | s:revit-s002, s:psets-s014 |
| P-035 | найди все свойства RUS_* где значение лежит как IfcLabel или IfcArea а не IfcReal, список с GlobalId, ничего не меняй | validate_check, medium, F, TG | Scan property sets; filter by name prefix and nominal value type; report GlobalId, pset, property, current type; read-only. | s:habr-s001; r:habr-r004 |
| P-036 | исправь тип у RUS_Area и RUS_Volume на IfcReal, Pset_* не трогай, сохрани как новый файл | modify_model_data, medium, F, TG | Change only named properties, leave standard `Pset_*`; save a copy; validate; report count. | s:habr-s002 |
| P-037 | какие параметры ревита вообще дошли до ифс, покажи психеты у одной стены и скажи чего нет | query_model_data, easy, F, TG | Dump property and quantity sets of a sample wall; compare with an expected list if given; mention the "export Revit property sets" option. | s:at-s010 |
| P-038 | проверь у всех стен заполнены огнестойкость и марка, какие пустые списком. имена свойств могут быть и русские и английские | validate_check, medium, F, TG | Match property names tolerant of language and case (`FireRating`, "Предел огнестойкости"); list empty or missing; state the matching rules used. | s:renga-s004 |
| P-039 | по ТЗ площадь должна быть числом, а у меня часть значений текстом. проверь RUS_Area на тип и формат значения | validate_check, medium, F, FORMAL | Report value type per element and text values with comma or unit suffix; read-only; mention the comma-vs-dot trap seen in Habr posts. | r:habr-r011 |
| P-040 | добавь всем IfcDoor пропертю Огнестойкость из FireRating если там пусто, остальное не трогай | modify_model_data, medium, F, TG | Copy only where target is empty; write a copy; report count and skipped. | s:tim-s010, s:dwg-s012 |
| P-041 | добавь всем колоннам свойство "Класс бетона" = B30 в отдельный pset | modify_model_data, medium, F, TG | Create a custom pset on every `IfcColumn`, save to a new file, leave the original unchanged; confirm the property name is as typed. | s:renga-s011 |
| P-042 | какие типы окон без RUS_Height? надо знать в каком семействе поправить | query_model_data, medium, F, TG | Group windows lacking the property by type name and family; give counts. | r:tg-r009 |
| P-043 | как сделать чтобы русские параметры ревита уехали в IFC с английскими именами свойств? про UDPS слышал | how_to, medium, -, FORUM | Explain mapping through a user-defined property set file or shared parameters with the target names; example mapping; Revit-version caveat. | r:habr-r010 |
| P-044 | у каких стен из Renga не заполнен код классификатора в пропертях? список с GUID | query_model_data, medium, F, TG | Iterate walls; check psets and classification references; list GlobalIds missing a code. | s:dwg-s004 |

### P5. Rooms, zones, areas

| # | Prompt (RU) | Tags | Expected behavior (EN) | Based on |
|---|---|---|---|---|
| P-045 | сумма площадей по IfcSpace не бьётся с ТЭП. покажи по каждой зоне RUS_Area и реальную площадь по геометрии, где разница больше 0.5 м2 | query_model_data, hard, F, LONG | Compute floor area from geometry per space; compare with attribute; list deviations above threshold with names and levels; note spaces without solid geometry. | s:at-s003, s:habr-s004; r:habr-r007 |
| P-046 | глянь какие помещения из ревита не выгрузились в ифс, в модели вижу только 40 IfcSpace | validate_check, medium, F, TG | Count `IfcSpace`; compare with a supplied room list by number and name; mention unplaced or unenclosed rooms as typical reasons; do not assume the list. | s:spaces-s010 |
| P-047 | в ифс не выгрузились зоны, хотя в ревите площадь есть. проверь IfcSpace и скажи что не так | troubleshoot_export, hard, F, TG | Count spaces; check representation presence; explain boundary-contour problems (short segments, overlaps, self-intersections) as hypotheses from Habr, ask for the Revit side to confirm. | s:habr-s011; r:habr-r002 |
| P-048 | выведи таблицей все помещения: номер, назначение, площадь, этаж, для экспликации | extract_quantities, easy, F, TG | List `IfcSpace` with number, name/long name, net floor area, storey; flag missing fields. | s:permit-s007, s:renga-s015 |
| P-049 | посчитай суммарную площадь помещений по этажам, нужна таблица для экспликации | extract_quantities, easy, F, TG | Sum net and gross areas per storey; output a table; state which quantity was used. | s:spaces-s011 |
| P-050 | найди помещения с одинаковым номером или лежащие одно в другом, ну дубли | validate_check, medium, F, TG | Find duplicate numbers and overlapping solids; list pairs with GlobalIds; read-only. | r:habr-r008 |
| P-051 | в Revit сделай ведомость помещений по этажам с площадью и итогом по этажу, выгрузи в эксель, неразмещённые отметь | extract_quantities, medium, F, TG | Live Revit: create or compute a schedule grouped by level with totals; export xlsx or csv; note unplaced rooms. | s:rauto-s009 |

### P6. Coordinates, levels, units

| # | Prompt (RU) | Tags | Expected behavior (EN) | Based on |
|---|---|---|---|---|
| P-052 | АР и ОВ в ифс не совмещаются по координатам, вроде одна точка съёмки везде. глянь где у них смещение | coordinate_clash, hard, F, TG | Read `IfcSite` placement, `IfcMapConversion` and building placement in each file; compute the offset; explain base point vs survey point export option. | s:at-s006 |
| P-053 | ифс от архитекторов улетает на километры от нуля при связи в ревит. покажи site placement и в чём косяк | coordinate_clash, hard, F, TG | Report site placement, map conversion, bounding extents and distance from origin; suggest shared origin; no automatic move. | s:revit-s003, s:mul-coord-s007 |
| P-054 | какие координаты у IfcSite, угол истинного севера, это МСК или локальные? | query_model_data, medium, F, FORUM | Read site reference values, map conversion and true north; say whether the file is georeferenced or local; do not name a CRS if none is stated. | s:at-s016 |
| P-055 | чем базовая точка проекта отличается от точки съёмки и что из них попадает в ифс при экспорте | understand_concept, easy, -, STUD | Explain project base point, survey point, internal origin and the exporter's coordinate-base option in plain words. | s:mul-coord-s008; r:tg-r035 |
| P-056 | как привязать модель к МСК моего региона в IFC? | how_to, hard, -, FORUM | Describe `IfcProjectedCRS` plus `IfcMapConversion` and units; ask for the CRS definition; do not invent an EPSG code or parameters for a regional МСК. | new |
| P-057 | выведи этажи с отметками и сколько элементов на каждом, лишние уровни тоже покажи | query_model_data, easy, F, TG | List `IfcBuildingStorey` with elevations and contained counts; flag empty storeys and elements outside any storey. | s:at-s007, s:renga-s003, s:revit-s006 |
| P-058 | перенеси элементы с этажа +3.000 на +6.000 так чтобы они не уехали по высоте | modify_model_data, hard, F, TG | Reassign containment and recompute local placement so absolute position is preserved (or state clearly if moving is intended); write a copy; verify. | s:habr-s009; r:habr-r005 |
| P-059 | в нависе ифс улетел куда-то в сторону, координаты проверь, единицы ок? | troubleshoot_import, medium, F, TG | Check unit assignment, site placement and extents; mention large coordinates; suggest shift. | s:dwg-s014 |
| P-060 | покажи единицы длины, площади и объёма в файле. мне кажется там футы | validate_check, easy, F, TG | Read `IfcUnitAssignment`; report units and conversions; do not guess. | s:revit-s013 |

### P7. Quantities, schedules, cost

| # | Prompt (RU) | Tags | Expected behavior (EN) | Based on |
|---|---|---|---|---|
| P-061 | объём бетона по этажам, только монолит, ВОР в эксель. если в модели нет Qto скажи прямо | extract_quantities, medium, F, TG | Group volumes by storey from base quantities; filter by material if available; export; flag missing quantities; no invented numbers. | s:aimcp-s011, s:revit-s005 |
| P-062 | сделай ведомость объёмов по стенам: тип, площадь, объём, сумма по этажам. для сметы, срочно | extract_quantities, medium, F, TG | Group `IfcWall` by type and storey, sum area and volume from base quantities; output a table; flag missing. | s:s007 |
| P-063 | если Qto нет, посчитай по геометрии, но пометь что это расчёт, а не данные из файла | extract_quantities, hard, F, TG | Fall back to geometry-derived values; label provenance per row; mention tolerance and openings handling. | s:qto-s009, s:habr-s010 |
| P-064 | выгрузи колонны по этажам: тип, длина, объём, марка. csv ок. если объёма нет — отметь | extract_quantities, medium, F, TG | Group `IfcColumn` by storey; take column base quantities; mark missing volumes; output csv. | s:data-s008 |
| P-065 | сумма площадей стен по типам из Qto_WallBaseQuantities, таблицей | extract_quantities, easy, F, TG | Aggregate net side area by wall type; flag walls without the quantity set. | s:dwg-s011, s:at-s011 |
| P-066 | посчитай длину воздуховодов по системам, в ифс они в IfcSystem вроде | extract_quantities, medium, F, TG | Group `IfcDuctSegment` by system membership; sum lengths; note elements without a system. | s:eng-s009 |
| P-067 | можешь привязать мои элементы к расценкам ФГИС ЦС и посчитать смету? | find_tool, medium, F, FORMAL | State the boundary: quantities and classifier codes can be extracted and tabulated; prices are not in the model; do not invent unit costs. | new (boundary); r:tg-r023 |
| P-068 | Нужна ведомость объёмов по бетону для сметчика: тип конструкции, этаж, объём, единицы. Чего не хватает в модели, перечислите отдельно. | extract_quantities, hard, F, FORMAL | Compose table by structure type; state units; list gaps in a separate section. | new; s:tim-s007 |

### P8. Comparing versions, duplicates, change tracking

| # | Prompt (RU) | Tags | Expected behavior (EN) | Based on |
|---|---|---|---|---|
| P-069 | сравни две выгрузки ifc (v3 и v4) по GlobalId, что добавилось, удалилось, у каких поменялись свойства | compare_versions, medium, F, TG | Match by GlobalId; report added, removed, changed properties; summarise by class. | s:at-s005, s:habr-s006 |
| P-070 | сравни вчерашний и сегодняшний ифс, что удалили из АР. смотри по guid и по имени, а то guid опять поменялись | compare_versions, hard, F, TG | Match by GlobalId; fall back to class, name, tag for unmatched; flag GUID churn explicitly; list deleted items with level. | s:guid-s006 |
| P-071 | найди дубли стен и перекрытий, которые лежат один в один, bbox в пределах 5 мм, не удаляй, просто пары | validate_check, hard, F, TG | Compare bounding boxes per class with tolerance; list pairs with GlobalIds; flag which copy has fewer properties; no deletion. | s:at-s004, s:habr-s005; r:habr-r008 |
| P-072 | хочу вести журнал правок по GlobalId чтобы применять их к следующим выгрузкам из ревита. как это устроить? | how_to, hard, -, LONG | Describe a change log keyed by GlobalId (class change, property edit, delete) and re-application; warn that GlobalIds may change between exports. | r:habr-r008 |
| P-073 | эксперту ушла версия 1, потом версия 2. что изменилось, чтоб написать в сопроводительной | compare_versions, hard, F, FORMAL | Produce a structured change summary by class and storey; separate geometry and property changes. | s:tim-s008 |
| P-074 | сравни две выгрузки из Allplan: что добавилось, удалилось, поменялось | compare_versions, hard, F, TG | Diff by GlobalId; note if Allplan GUIDs are unstable. | s:dwg-s008 |

### P9. Clashes, MEP, openings

| # | Prompt (RU) | Tags | Expected behavior (EN) | Based on |
|---|---|---|---|---|
| P-075 | найди пересечения труб с балками и скинь в бцф | coordinate_clash, hard, F, TG | Compute geometric intersections `IfcPipeSegment` vs `IfcBeam`; list pairs; produce BCF-ready output or state the limitation. | s:renga-s014 |
| P-076 | прогони коллизии вентиляция vs балки, допуск 20мм, сгруппируй по этажам, без касаний | coordinate_clash, medium, F, TG | Clash with 20 mm tolerance; exclude touching; group per storey; counts. | s:clash-s007 |
| P-077 | бцф из нависа в ревит не наводится на элементы, пишет не найдено. ифс подгружен как link | troubleshoot_import, medium, -, FORUM | Explain BCF viewpoint IfcGuid vs Revit element identity, need for export with IFC GlobalId, linked-IFC limitation. | s:clash-s008 |
| P-078 | в Navisworks 1500 коллизий, в сервисе проверки 200. почему такая разница? | request_opinion, medium, -, LONG | Plausible reasons: grouping, class vs Revit category, tolerance, duplicates; ask for the settings of both; do not assert a single cause. | r:habr-r003 |
| P-079 | покажи воздуховоды и трубы которые не входят ни в одну систему, надо до сдачи | validate_check, medium, F, TG | Find segments and fittings lacking system assignment; list with level and id. | s:mep-s005, s:eng-s018 |
| P-080 | в ифс пропали проёмы под двери, стена сплошная. у каких стен нет IfcOpeningElement и какие двери висят без проёма | validate_check, medium, F, TG | List doors lacking fill relation to an opening; walls without void relations; group by level. | s:geom-s007, s:revit-s012 |
| P-081 | найди трубы и воздуховоды которые пересекают стены и перекрытия, а отверстия нет. список с отметками | coordinate_clash, hard, F, TG | Intersect MEP with walls and slabs, exclude existing openings, list with elevations. | s:openings-s010 |
| P-082 | при экспорте вентиляция пропала из навигатора, галка "только видимые" вроде стояла. что не так | troubleshoot_export, medium, -, FORUM | Explain how systems export as distribution systems and what visibility-only export changes; steps to check. | s:mep-s006 |
| P-083 | у труб есть имя системы и диаметр? выдай те, где нет | validate_check, medium, F, TG | Check system assignment and nominal diameter; list elements lacking them. | s:revit-s010 |

### P10. Import, export and exchange between programs (mostly no file)

| # | Prompt (RU) | Tags | Expected behavior (EN) | Based on |
|---|---|---|---|---|
| P-084 | Экспорт из Tekla в Revit. Заказчик требует IFC, стандартный экспорт даёт в Ревите только оси | troubleshoot_import, medium, -, FORUM | Suggest surface geometry export option, assigning a phase to the linked IFC, checking the file in a free viewer; ask IFC version. | r:dwg-r002, r:habr-r029 |
| P-085 | САПФИР-3D 2020 R2. Как правильно экспортировать модель в IFC? AutoCAD пишет System Error encountered during import | troubleshoot_import, medium, -, FORUM | Forum answers of that period say AutoCAD has no native IFC import (newer versions and vertical products may differ, so hedge); the file opens in Revit or Tekla; try the general-view export option; ask for log. | r:tg-r003 |
| P-086 | Как корректно открыть IFC в ревите? Экспортировал сторонним экспортёром, модель кривая. Файл не прикреплял | troubleshoot_import, easy, -, FORUM | Recommend verifying the file in a free viewer first; explain Open vs Link and import mapping; ask for software and IFC version. | r:tg-r002, r:dwg-r008 |
| P-087 | Импорт IFC в Revit 2022: геометрия есть, а элементы не объекты, параметров нет. Нужна модель для чертежей | troubleshoot_import, medium, -, FORUM | Explain that IFC import yields non-native elements unless linked or mapped; class mapping file; DirectShape; set expectations. | r:tg-r004, r:dwg-r009 |
| P-088 | как вставить IFC в Автокад чтобы редактировать? | convert_format, medium, -, FORUM | Forum answers say plain AutoCAD does not edit IFC (verify for the user's version); options: BricsCAD BIM, IfcConvert to DXF, other converters; trade-offs. | r:dwg-r011 |
| P-089 | из архикада ифс в ревит затащить чтоб были стены а не обобщённые модели? open или link? | how_to, medium, -, TG | Explain Open vs Link IFC, import class mapping, DirectShapes; translator preparation in Archicad. | s:roundtrip-s007 |
| P-090 | из ArchiCAD в Revit стёкла жёлтые и толщиной в метры, часть перегородок пропала. получается фигня | troubleshoot_import, medium, -, FORUM | Point to class mapping file and default import template; check units; edit IFC only as last resort. | r:dwg-r029 |
| P-091 | как лучше передать конструктив из Ревита в СКАД, прямая связь есть или через IFC? IFC пробовал, получается фигня | convert_format, medium, -, FORUM | IFC carries physical model, not an analytical one; vendor plugins and direct links are alternatives; place model at origin to avoid offsets. | r:dwg-r019, r:dwg-r015 |
| P-092 | как из ревита выгрузить расчётную схему в Robot или Лиру? нужны стержни и узлы а не тела | convert_format, hard, -, FORUM | Explain analytical model vs physical model, limits of IFC, alternatives; offer to inspect any exported IFC for structural members. | s:struct-s007 |
| P-093 | из робота выгрузил ифс, в ревит колонны пришли обобщёнными. как сделать колоннами | troubleshoot_import, medium, -, TG | Import mapping; check whether source classes are `IfcColumn` or proxy; link vs open. | s:eng-s010 |
| P-094 | Как получить IFC из Plant 3D 2025? Codemill платный, через Navisworks не выгружается | find_tool, hard, -, FORUM | No native export; Codemill plugin; custom exporter via .NET API and xBIM is an option; set expectations. | r:dwg-r004 |
| P-095 | нужен dwg из этого ифс, чтоб слои по классам, а то в автокаде одним куском | convert_format, hard, F, TG | Map classes to layers; DWG/DXF export route; state limitations. | s:viewconv-s011 |
| P-096 | Текла не открывает ифц, глянь заголовок. Там кириллица в пути? Какая версия экспортёра и схема | validate_check, easy, F, FORUM | Read `FILE_NAME`, `FILE_SCHEMA`, exporter; report non-ASCII characters in header. | s:dwg-s003; r:dwg-r010 |
| P-097 | ифс из ренги в ревит заходит какими-то глупыми телами, параметров нет. что не так | troubleshoot_import, medium, -, TG | Link vs open; class mapping; Renga export settings (Reference View vs editable geometry); IFC version. | s:renga-s007; r:tg-r017 |
| P-098 | какую версию ифс выбрать при экспорте из ренги, 2x3 или 4? координатор сидит в нависе | how_to, easy, -, TG | Compare 2x3 and 4 for Navisworks; mention that IFC4 is advised in Renga material for merge, clashes and expertise; confirm the Navisworks version. | s:renga-s013; r:tg-r018 |
| P-099 | навис не показывает ифс4 из ревита, 2x3 нормально открывается. че делать | troubleshoot_viewing, medium, -, TG | Older viewers: tessellation and advanced brep limits; try 2x3 CV2.0 or an updated tool; ask Navisworks version. | s:vm-s017, s:vm-s004 |
| P-100 | в модели ренги какое представление геометрии у колонн и стен, SweptSolid или Tessellation? для нависа надо | query_model_data, hard, F, TG | Report representation types per class with counts; advise Tessellation for Navisworks per vendor article. | s:dwg-s005; r:dwg-r028 |
| P-101 | какой транслятор в архикаде выбрать для передачи в ревит, и IFC2x3 или IFC4? | how_to, easy, -, TG | Explain translators and MVD, Revit support, with caveats. | s:dwg-s010 |
| P-102 | как сделать чтоб мои параметры семейства уехали в ифс? галка "экспорт параметров ревита" вроде стоит а пусто | how_to, easy, -, STUD | Explain export of Revit property sets, user-defined property set file, shared parameters; where to check. | s:revit-s008 |
| P-103 | ифс открывается в ревите минут 40 и потом файл 800 мб, что делать, связью лучше? | troubleshoot_import, medium, -, TG | Link vs open/import, cache, reduce source, set limits. | s:revit-s009 |
| P-104 | чем бесплатно открыть ifc, без регистрации и чтоб свойства смотреть можно было. по NDA в онлайн заливать нельзя | find_tool, easy, -, TG | Offline free viewers (xBIM-based, BIMvision, KIT); confirm properties panel; warn about uploading confidential models. | s:at-s014 |

### P11. Encoding and Cyrillic

| # | Prompt (RU) | Tags | Expected behavior (EN) | Based on |
|---|---|---|---|---|
| P-105 | в ифс названия типов как кракозябры, найди все где имя битое и скажи из какой категории | query_model_data, medium, F, TG | Scan names and properties for mojibake and escape artefacts; list entities with class and Revit category; hypothesise cause. | s:enc-s001, s:tim-s005 |
| P-106 | в модели имена вида РЎС‚РѕР№ка. вылечи, перекодируй обратно | modify_model_data, hard, F, TG | Detect cp1251/UTF-8 double decoding; convert back; before and after table; write a copy. | s:enc-s016 |
| P-107 | при экспорте из ревита русские названия семейств ломаются в другом софте. какие настройки смотреть | troubleshoot_export, medium, -, FORUM | Explain `\X2\` escaping and exporter differences; strictness of the receiving tool; test steps. | s:enc-s011 |
| P-108 | IFC из SolidWorks не читается в питоне, имена с кириллицей вперемешку с \X2\ | troubleshoot_code, hard, F, LONG | Raw non-ASCII characters are invalid in the STEP file; the exporter must escape; show a safe re-encoding approach. | r:gh-enc-r017 |

### P12. File size, performance, batch

| # | Prompt (RU) | Tags | Expected behavior (EN) | Based on |
|---|---|---|---|---|
| P-109 | ифс весит 900 мб, откуда столько? глянь по классам что тяжелее всего и что можно выкинуть не ломая модель | optimize_performance, medium, F, TG | Count entities by class and estimated size; repeated geometry without mapped items; heavy properties; safe removals listed. | s:fs-s006, s:renga-s016 |
| P-110 | ифс на 1.5 гига, вьюер у экспертизы виснет, чем облегчить не потеряв свойства | troubleshoot_viewing, medium, F, TG | Split by discipline, remove 2D and unused types, reduce detail while keeping property sets. | s:tim-s014 |
| P-111 | ревит экспорт в ifc висит уже 3 часа, 500 мб rvt, что отключить | troubleshoot_export, easy, -, TG | Export settings affecting speed: view-only export, split by level, 2D elements, linked files, base quantities. | s:fs-s007; r:tg-r008 |
| P-112 | ревит валится при экспорте в ифс, "неустранимая ошибка". что может ломать, помещения без границ, битые стены? | troubleshoot_export, hard, F, TG | Check unenclosed rooms, null geometry, bisect by categories; ask for log. | s:err-s005 |
| P-113 | пакетная выгрузка 20 rvt в ифс падает по памяти, как исключить рабочие наборы | troubleshoot_export, medium, -, LONG | Sequential export, per-model config, workset exclusion; mention batch tools seen in the data (BatchIfcExporter). | s:habr-s016; r:habr-r024 |
| P-114 | прогони все 6 ифс из папки на обязательные свойства и скинь одну сводную таблицу, сроки горят | automate_batch, hard, F, TG | Open each file; run the same requirement check; one consolidated table per file and class. | s:at-s017 |

### P13. Concepts, regulation, opinions (beginners and managers)

| # | Prompt (RU) | Tags | Expected behavior (EN) | Based on |
|---|---|---|---|---|
| P-115 | что такое IFC вообще, простыми словами? для курсовой | understand_concept, easy, -, STUD | Plain explanation, no jargon dump; offer a quick look at the loaded file if any. | r:tg-r015, r:habr-r021 |
| P-116 | препод сказал, что в ифс стены бывают IfcWall и IfcWallStandardCase. покажи у меня какие есть и в чём разница | query_model_data, medium, F, STUD | Count IfcWall vs IfcWallStandardCase, list examples; plain explanation: StandardCase is the typical IFC2x3 Coordination View output (constant-thickness walls), IFC4 exports use IfcWall, and the exact version that deprecated StandardCase is not settled in this KB. | new; s:p-student-s002 |
| P-117 | подрядчик просит ифс но не говорит какой. 2x3 или 4? какой вьюшкой выгружать | understand_concept, easy, -, TG | Recommend asking for the customer's requirements; default to 2x3 CV2.0 for compatibility, RV where supported. | s:vm-s005 |
| P-118 | ЦИМ и ТИМ, в чём разница? в ТЗ пишут и то и другое | understand_concept, easy, -, STUD | ТИМ = technologies and process; ЦИМ = the model; users say "ТИМ-модель" loosely. | new; [russia.md](../../02_standards_regulations/national/russia.md) |
| P-119 | СП 333 и СП 328 это про что вообще? | understand_concept, medium, -, FORMAL | Hedged overview: 333 rules of forming the model at lifecycle stages; 328 describes components *(title unverified)*; avoid clause numbers. | new |
| P-120 | IDS не умеет геометрию. как тогда проверять площади и коллизии? | request_opinion, medium, -, LONG | Explain IDS scope; geometry checks need other tools or scripts; mention Solibri rules, Dynamo, mvdXML as options named in the source. | r:habr-r015 |
| P-121 | стоит ли переходить с Ревита на Ренгу если нужна IFC выгрузка для экспертизы | request_opinion, medium, -, FORUM | Balanced: Renga IFC support and registry status vs older threads calling it immature; recommend a pilot export test; no promises. | r:dwg-r006, r:tg-r018 |
| P-122 | Autodesk бросит IFC ради USD? есть смысл вкладываться в инструменты под IFC? | request_opinion, medium, -, TG | Neutral, separates a contested opinion from facts; IFC remains in regulations; no speculation presented as fact. | r:habr-r019 |

### P14. Live Revit tasks (MCP to a running Revit) and safety

| # | Prompt (RU) | Tags | Expected behavior (EN) | Based on |
|---|---|---|---|---|
| P-123 | переименуй все виды этажей по шаблону ПЛ_{уровень}_{имя}, дубли имён не плодить | automate_batch, medium, F, TG | List plan views, build names, detect duplicates, rename in one transaction, report mapping. | s:rauto-s008 |
| P-124 | глянь у каких стен и перекрытий не заполнен параметр Марка, список с id, до экспорта надо | validate_check, easy, F, TG | Query walls and floors, blank "Марка", return grouped list with ids. | s:rauto-s010, s:aimcp-s010 |
| P-125 | покажи таблицу что поменяется если я проставлю IfcExportAs по имени типа, но пока ничего не пиши в модель | modify_model_data, medium, F, TG | Dry-run: produce a before/after table; write nothing; wait for explicit confirmation. | new (confirm-before-write) |
| P-126 | почисти модель, удали все неиспользуемые семейства и виды | modify_model_data, medium, F, TG | Treat as destructive: summarise what would be removed, ask for confirmation, advise a backup; do not run silently. | new (safety) |
| P-127 | перед экспортом прогони проверку по IDS прямо в ревите, какие параметры пустые, чтобы не ждать два часа выгрузки | validate_check, hard, F, LONG | Evaluate the mapped parameters against requirements without full export; report element, requirement, missing value; caveat that class assignment follows the exporter logic. | r:habr-r001, r:tg-r009 |
| P-128 | выгрузи IFC4 Reference View из текущей модели в папку на рабочем столе и скажи сколько заняло | convert_format, medium, F, TG | Run export with stated version and view; confirm path before writing; report duration and file size. | new |
| P-129 | клод пишет что не может подключиться к ревиту, плагин вроде стоит. что проверить | troubleshoot_code, easy, -, STUD | Verify plugin started and project open, port and client configuration, restart order; do not guess versions. | s:aimcp-s012 |
| P-130 | можно ли настроить параметр семейства так чтобы значения подставлялись автоматически при загрузке семейства | how_to, medium, -, FORUM | Explain family parameters with defaults and options; what is not possible without API; ask Revit version. | r:rauto-r032 |

**Coverage check.** 130 prompts. By register: TG 82, FORUM 21, LONG 10, STUD 9, FORMAL 8. By difficulty: easy 26, medium 73, hard 31. Needs a loaded model: 86; knowledge or how-to without a file: 44. Gaps to fix in a later wave: real MEP and estimator voices, Allplan and Pilot-BIM IFC questions, IFC 4.3 and infrastructure (Credo), and real Renga/nanoCAD posts.

---

## 7. Tips for generating authentic prompts in Russian

### Do
1. **Mix registers**: roughly 60% short chat/Telegram imperatives, 20% forum-style symptom descriptions, 10% polite or formal, 10% paragraphs with context. Real forum posts and the synthetic set both skew short; add a few long ones on purpose.
2. **Name the software the Russian way and decline it**: "в Ревите", "из Теклы", "в нависе", "из Архикада", "из Ренги", "Сапфир". Keep identifiers in Latin: `IfcExportAs`, `GlobalId`, `RUS_Area`, `IfcSpace`.
3. **Use the local vocabulary**: ЦИМ, ТИМ, экспертиза, АГР, "Строим просто", КСИ, МССК, ТЭП, ФОП, UDPS, СОД, ГИП, ТЗ заказчика. For "BEP/EIR/LOD" Russians say "требования заказчика к ТИМ" and "уровень проработки".
4. **Add a deadline or a customer**: "завтра сдача в АГР", "в понедельник экспертиза", "заказчик требует IFC". Pressure is the main emotional note in the real data.
5. **Leave context out**: no Revit year, no IFC schema, no export settings, no file name, unless the persona would know them. Let the assistant ask or inspect.
6. **Use imperatives and constraints typical of tasks**: "глянь", "покажи", "выведи", "найди", "выгрузи", "скинь" plus "ничего не меняй", "сохрани как новый файл", "если нет Qto, скажи прямо", "список с GlobalId".
7. **Quote English errors inside Russian sentences**: "System Error encountered during import".
8. **Include numbers**: 800 мб, 1.5 гига, 40 IfcSpace, разница 20 м2, 1500 против 200 коллизий, допуск 20 мм.
9. **Keep human mess**: missing punctuation, lowercase starts, "ифс/ифц", "проксики", "бцф", "кракозябры", "получается фигня", an occasional Cyrillic С in "IFС" (seen once in real data).
10. **Cover both worlds**: files from foreign tools (Revit, Tekla, ArchiCAD) and from Russian tools (Renga, nanoCAD, SAPFIR-3D), and both IFC2x3 (still common) and IFC4 (Moscow АГР cases).
11. **Include boundary tests**: "экспертиза это точно пропустит?", pricing from ФГИС ЦС, a regional МСК without a CRS definition, "удали всё неиспользуемое". Good answers hedge, ask or confirm.
12. **Say who is asking**: coordinator and BIM manager (most common), structural engineer (Tekla, SCAD, Lira), architect (Revit, ArchiCAD, Renga), developer (IfcOpenShell, web-ifc, xBIM), student, reviewer from an authority.

### Don't
1. Do not write "BIM Execution Plan", "LOD/LOI", "ISO 19650 CDE" in Western style for ordinary users; that is a manager or consultant voice at best.
2. Do not make every user polite or write machine-translated Russian ("не могли бы вы любезно..."); forum and chat users are blunt.
3. Do not call every file "IFC-файл"; vary "ифс", "IFC", "модель в IFC", "выгрузка".
4. Do not invent decree numbers, СП clause numbers, order numbers, КСИ/МССК codes or EPSG codes in prompts or in expected behaviour. Mark national facts that are *(unverified)* as such.
5. Do not assume ТИМ is mandatory for private projects, or that every expertise accepts IFC4x3.
6. Do not present synthetic prompts as real posts. Cite `source_url` only for real records.
7. Do not clean up fragments like "только оси", "теряются свойства", "пропали зоны"; they are the authentic form.
8. Do not give every persona perfect context (version, MVD, settings, file path); real posts almost never do.
9. Do not use English-only property names for a user who works with Russian parameters (`RUS_*`, "Марка", "Огнестойкость"); also test an English-named equivalent in the same file.
10. Do not forget that in Russian Revit "типоразмер", "стадия", "связь" are the UI words; do not translate them back to English in prompts.

### Persona to register map
| Persona | Typical register and topics |
|---|---|
| BIM-координатор | Chat imperatives, validation before submission, class mapping, IDS, coordinates, clash grouping; deadlines |
| BIM-менеджер | Slightly longer, version comparison, batch checks, requirements from customer |
| Архитектор (Revit, ArchiCAD, Renga) | Export settings, rooms and zones, link vs open, "почему так" |
| Конструктор (Tekla, SCAD, Lira) | Forum symptom titles, rebar, analytical model, steel connections lost |
| Разработчик | Tool names, code-level detail, English identifiers, reproducible steps, MCP |
| Студент | Plain "что такое", "для курсовой", apologetic or confused tone |
| Эксперт / рецензент | Formal, "проверьте на соответствие", asks for lists and reports; version comparison |
| Сметчик (synthetic only) | ВОР, смета, "в эксель", "если нет Qto скажи прямо" |

### Three rewrites (weak to authentic)
| Weak (translated textbook) | Authentic (chat) | Authentic (forum) |
|---|---|---|
| "Пожалуйста, проверьте, содержит ли IFC-файл все обязательные свойства согласно требованиям государственной экспертизы." | "завтра сдаём в АГР, глянь у всех окон RUS_Height есть? кто без - списком" | "Подготовка ЦИМ к АГР. Как проверить заполнение параметров до выгрузки? Экспорт идёт 2 часа" |
| "Не могли бы вы подсказать, как правильно экспортировать модель из Tekla в Revit?" | "из теклы в ревит только оси пришли, заказчик ифс требует, что крутить" | "Экспорт из Tekla в Revit. Стандартные настройки дают одни оси" |
| "Каково расхождение между площадями помещений в модели и показателями ТЭП?" | "площади по зонам не бьются с ТЭП, покажи где разница больше 0.5 м2" | "Расхождение площадей ТЭП и IFC. Зоны с кривыми контурами не выгружаются?" |

### Related files
- [Russia: ТИМ/BIM and IFC requirements](../../02_standards_regulations/national/russia.md)
- [Revit IFC export reference](../../03_software/revit/ifc_export_reference.md) and [import and link reference](../../03_software/revit/ifc_import_link_reference.md)
- [Glossary (10 languages)](../../08_glossary/glossary_multilingual.md) and [abbreviations (Russia section 5.1)](../../08_glossary/abbreviations.md)
- [IFC in real projects (IDS, АГР, expertise)](../../01_ifc_basics/00_ifc_in_real_projects.md)
- Topic files: [import and interoperability](../by_topic/import_and_interoperability.md), [validation and IDS](../by_topic/validation_ids_model_checking.md), [revit export and class mapping](../by_topic/revit_export_and_class_mapping.md), [materials, spaces, zones](../by_topic/materials_spaces_zones.md), [quantities and cost](../by_topic/quantities_cost_schedule.md)
