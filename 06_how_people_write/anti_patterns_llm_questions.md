# Anti-patterns: how LLM-invented questions look (and how to rewrite them)

**Purpose:** when a language model is asked to "write realistic test requests for an IFC/Revit assistant", it tends to produce a recognisable, over-tidy style. This file lists the tell-tale signs, shows 64 side-by-side rewrites (23 Russian, 23 English, 18 in other languages) and gives rules a generator can apply.
**Read first:** [style_guide.md](style_guide.md) (what real people do, with numbers and sources).
**Reference docs:** [multilingual glossary](../08_glossary/glossary_multilingual.md), [abbreviations](../08_glossary/abbreviations.md), [IFC in real projects](../01_ifc_basics/00_ifc_in_real_projects.md).

> **How to read the pairs.**
> - The **"LLM-style"** column is an *illustrative caricature* written for this document: what a polite, thorough model typically produces when asked for a test prompt. It is not a logged output of any particular model.
> - The **"Human-style"** column is either (a) a **synthetic** KB prompt quoted exactly, with its id (for example `ru-clash-s007`), or (b) a **new synthetic** rewrite written for this file, modelled on the real records and cell reports named in the last column. Neither is a quote of a real person unless the last column says "real".
> - Where the human-style line is a real README prompt or real forum text, the source URL is given.
> - Ids may repeat across files (41 do); the cell name inside the id and the URL are what to trust.

---

## 1. The anti-pattern catalogue

| Code | Name | Tell-tale signs | Why it is unreal (evidence in this KB) | Fix |
|---|---|---|---|---|
| **AP1** | Over-polite wrapper | "Could you please", "Would you be so kind", "Здравствуйте! Не могли бы вы", "I would appreciate", "Thank you in advance" | Real "polite" tag: 4% of 2,256 records. Typed-to-AI synthetic prompts: please/could-you in 7% (EN), 1% (RU), 0% (ZH). Politeness is a forum habit, not a chat-with-tool habit. | Drop it. At most "pls" or "плиз" or "bitte" |
| **AP2** | Complete, self-contained spec | Every parameter named: class, property set, units, tolerance, grouping, format, scope | Real posts omit schema/version/units about half the time; typed requests rely on "this model" | Keep the *one* anchor that matters; delete the rest |
| **AP3** | Textbook vocabulary | "IfcBuildingElementProxy elements", "Reference View MVD", "georeferencing", "property set" always spelled out | People say proxy/проксики, ifc/ифс, ревит, "the base point", "family", "mapping". Slang and loose words are the norm. | Swap in the person's word; keep the technical token the task depends on |
| **AP4** | Perfect structure | Numbered lists, bold headings, "Context / Task / Constraints / Output format" | GitHub templates exist, but typed prompts are one line; only 2% of notes mention numbered lists | Collapse to one clause chain |
| **AP5** | "Comprehensive overview" | "comprehensive analysis", "detailed report", "thorough review", "complete overview of all aspects" | Real asks are narrow: "which walls dont have FireRating" | Replace with one checkable question |
| **AP6** | Balanced symmetry | Three equal criteria, "advantages and disadvantages of each", pros/cons | Real requests are lopsided: a precise 20% plus a vague 80% | Make one part detailed, the others thin or absent |
| **AP7** | No mess at all | Perfect spelling, perfect case, consistent units, no ellipsis | Slips are small but frequent (see style guide section 8) | Add at most one slip, away from the key token |
| **AP8** | Invented backstory or over-clean context | A named project ("Skyline Tower, 25 floors"), the full version stack ("Revit 2024.2, exporter 24.2.0, IFC4 RV") | Context is partial and lopsided; software with version numbers appears in 29% of records | One context item or the motive ("эксперты не принимают прокси") |
| **AP9** | Unrealistic or exam-style task | "Explain what IfcRelAggregates is", "optimise my structural design", "calculate the carbon footprint" with no data in the model | Real people ask for a list, a check, a fix, a tool; or a concrete "why does X happen" | Convert to the question a working person would ask about their file |
| **AP10** | Theatrical or missing emotion | "URGENT!!!", "my career depends on it", or no motive at all | Real urgency = deadline, person waiting, repeated failure. "!!!" in about 1% of titles | Use a because-clause |
| **AP11** | Single clean intent | One question, no side-check, no follow-up | Piggy-backed checks and numbered sub-questions are common | Occasionally add a second clause |
| **AP12** | Translationese or bureaucratic register | RU "Не могли бы вы любезно оказать содействие", ZH "您好，麻烦您", JA keigo ("いただけますでしょうか"), FR "Pourriez-vous avoir l'amabilité" | Chat prompts in these languages are short and plain | Use the language's colloquial imperative |
| **AP13** | Answer-shaped or lecture request | The question already contains the explanation, or asks for a lecture | Real questions state a symptom and wait for a cause | State the symptom, not the theory |
| **AP14** | Closing boilerplate | "Let me know if you need more information", "Thanks!", signature | Closers occur on forums after a solution, not in a prompt | End on the request |
| **AP15** | Template repetition across a batch | Same opener, same length, same structure in 20 prompts | Real corpora have a long tail: title-only, one-liners, logs | Vary form deliberately (section 4) |
| **AP16** | Round, tidy numbers | "tolerance 10 mm, 100 elements, 50%" everywhere | Real numbers are specific: "212 doors", "0.78 mm", "480 MB", "1500 vs 200" | Use measured-looking numbers, or none |
| **AP17** | Persona costume | "As a BIM coordinator, I need to..." | Role is implied by vocabulary and by the because-clause | Let the vocabulary signal the role |
| **AP18** | Wrong direction of vocabulary | The model never uses Revit words for IFC objects; never confuses "export" with "convert" | Real asks apply Revit vocabulary to IFC ("family", "category", "open or link") | Allow the loose term, test whether the assistant resolves it |
| **AP19** | Vague in the useless way | "Check my model", "improve this file" with no object or anchor | Real vagueness still names an observable ("half my walls came out grey") | Add the observable, not the theory |

---

## 2. Side-by-side pairs

Columns: **LLM-style** (caricature) | **Human-style** (synthetic; id when quoted from the KB) | **Fixes** | **Grounding**

### 2.1 Russian (RU-01 to RU-23)

| # | LLM-style | Human-style (synthetic) | Fixes | Grounding |
|---|---|---|---|---|
| RU-01 | «Здравствуйте! Не могли бы вы, пожалуйста, подсчитать количество элементов класса IfcBuildingElementProxy в загруженной IFC-модели и указать, из каких категорий Revit они были экспортированы? Заранее благодарю!» | «сколько в модели проксей и из каких категорий ревита они пришли» (new, after `ru-renga-nanocad-s002`)<br>*(how many proxies in the model and from which Revit categories)* | AP1 AP2 AP3 AP14 | `ru-renga-nanocad-s002`, `ru-tim-expertiza-s003`; Habr: ru-habr-dev-r009 ([link](https://habr.com/ru/articles/1098340/)) |
| RU-02 | «Прошу провести комплексный анализ качества IFC-модели, включая геометрию, свойства, классификацию и пространственную структуру, и подготовить подробный структурированный отчёт.» | «надо сдавать на экспертизу в понедельник, проверь ифс что у всех стен и перекрытий заполнены обязательные свойства по требованиям заказчика, список пустых выгрузи» (`ru-tim-expertiza-s001`)<br>*(due to expertise on Monday; check all walls and slabs have the required properties; export the empty ones)* | AP5 AP2 AP10 | real pressure: [dwg.ru](https://forum.dwg.ru/showthread.php?t=153428) |
| RU-03 | «Как BIM-координатор, мне необходимо выявить пространственные коллизии между воздуховодами системы вентиляции и несущими балками с допуском 20 мм и сгруппировать результаты по этажам.» | «прогони коллизии вентиляция vs балки, допуск 20мм, сгруппируй по этажам, без касаний» (`ru-clash-s007`)<br>*(run clashes ducts vs beams, 20 mm tolerance, group by floors, no touching)* | AP17 AP1 AP3 | t-clash-bcf cell |
| RU-04 | «Объясните, пожалуйста, подробно, что такое IfcBuildingElementProxy и по какой причине элементы Revit могут быть экспортированы в этот класс.» | «почему из ревита стены вышли проксями? IfcExportAs прописал, не помогло» (new)<br>*(why did walls come out as proxies? I set IfcExportAs, no help)* | AP9 AP13 AP3 | real: [Autodesk forum](https://forums.autodesk.com/t5/revit-structure-forum/ifcexportas-parameter-doesn-t-work/td-p/8219179); Habr "категории Revit не определяют IFC-класс" |
| RU-05 | «Пожалуйста, проверьте корректность геопривязки в приложенном файле IFC4 Reference View, экспортированном из Revit 2024 (версия экспортёра 24.2.0), с учётом Project Base Point, Survey Point и системы координат EPSG:3857.» | «ифс из аллплана улетел на 3 км от начала координат в ревите, глянь где у него смещение и какие координаты у IfcSite» (`mul-coord-s007`)<br>*(IFC from Allplan flew 3 km away from origin in Revit; find the offset and IfcSite coordinates)* | AP2 AP8 AP3 | t-coordinates cell |
| RU-06 | «Подготовьте, пожалуйста, ведомость объёмов бетона по этажам с разбивкой на плиты, стены и колонны в виде таблицы.» | «объём бетона по этажам, только монолит, ВОР в эксель. если в модели нет Qto - скажи прямо» (`ru-aimcp-s011`)<br>*(concrete volume per floor, cast-in-place only, bill of quantities to Excel; if there is no Qto, say so)* | AP6 AP1 AP3 | t-qto-cost cell |
| RU-07 | «Сравните, пожалуйста, две версии IFC-модели и предоставьте подробный отчёт обо всех обнаруженных различиях.» | «сравни вчерашний и сегодняшний ифс, что добавили удалили и что поменялось по GUID» (`ru-dwg-revit-s007`)<br>*(compare yesterday's and today's IFC: added, removed, changed by GUID)* | AP5 AP1 | t-guid-versioning cell |
| RU-08 | «Не могли бы вы определить все элементы, у которых отсутствует назначенный материал, и предоставить их перечень с указанием типов и уровней?» | «найди элементы без материала, а у стен покажи слои и толщины» (`ru-dwg-revit-s011`)<br>*(find elements without material, and for walls show layers and thickness)* | AP1 AP6 | t-materials-colors-layers cell |
| RU-09 | «После экспорта IFC из Revit в наименованиях элементов вместо кириллицы отображаются нечитаемые символы. Не могли бы вы помочь установить причину?» | «в ифс кракозябры вместо русских названий, найди где поломано» (`ru-renga-nanocad-s010`)<br>*(gibberish instead of Russian names; find where it is broken)* | AP1 AP3 | t-encoding cell |
| RU-10 | «Пожалуйста, измените класс всех элементов IfcBuildingElementProxy, имя которых начинается с "Колонна_", на IfcColumn, не изменяя остальные элементы модели.» | «все проксей с именем 'Колонна_*' переведи в IfcColumn, остальное не трогай» (`ru-dwg-revit-s004`; note the genuine grammar slip "все проксей")<br>*(all proxies named 'Колонна_*' to IfcColumn, leave the rest)* | AP7 AP1 | t-proxy-mapping cell |
| RU-11 | «Подскажите, пожалуйста, какие настройки экспорта IFC следует выбрать в Revit, чтобы модель успешно прошла государственную экспертизу?» | «как настроить экспорт из ревита в ifc чтобы прошло по требованиям экспертизы? какую версию и MVD ставить» (`ru-tim-expertiza-s006`)<br>*(how to set Revit IFC export to pass expertise; which version and MVD)* | AP1 AP4 | [Habr](https://habr.com/ru/articles/1089018/) |
| RU-12 | «Пожалуйста, предоставьте список всех этажей модели с высотными отметками.» | «какие этажи в ифс и отметки, есть ли элементы без привязки к этажу» (`ru-dwg-revit-s006`)<br>*(which storeys and elevations; any elements not tied to a storey?)* | AP11 AP1 | t-spaces-areas cell |
| RU-13 | «Как лучше передать модель из ArchiCAD в Revit: использовать импорт IFC или связь IFC? Опишите преимущества и недостатки каждого варианта.» | «как из архикада ифс в ревит затащить чтоб были стены а не обобщенные модели? open или link?» (`ru-roundtrip-s007`)<br>*(how to get ArchiCAD IFC into Revit as walls, not generic models; open or link?)* | AP6 AP3 AP18 | real: [revit-ifc #223](https://github.com/Autodesk/revit-ifc/issues/223) |
| RU-14 | «Пожалуйста, составьте таблицу помещений со следующими столбцами: номер, наименование, площадь, уровень.» | «таблицу помещений: номер, название, площадь, этаж» (`ru-renga-nanocad-s015`) | AP1 AP4 | t-spaces-areas cell |
| RU-15 | «СРОЧНО!!! Это критически важно!!! Мне необходимо ПРЯМО СЕЙЧАС проверить модель, иначе проект будет сорван!!!» | «прогони все 6 ифс из папки на наличие обязательных свойств и скинь одну сводную таблицу, сроки горят» (`ru-autodesk-telegram-s017`)<br>*(run all 6 IFCs in the folder for required properties, one summary table, deadline burning)* | AP10 AP19 | understated pressure; real: "заказчик требует IFC" ([dwg.ru](https://forum.dwg.ru/showthread.php?t=146029)) |
| RU-16 | «Что такое IDS и как он применяется для проверки IFC-моделей?» | «чем бесплатно открыть ifc, без регистрации и чтоб свойства смотреть можно было» (`ru-autodesk-telegram-s014`)<br>*(what opens IFC for free, no registration, with properties visible)* | AP9 AP13 | real: [Zhihu "recommend a viewer"](https://www.zhihu.com/question/583830829) |
| RU-17 | «Суммарная площадь помещений по IfcSpace отличается от значений ТЭП. Проведите детальный анализ причин расхождения.» | «сумма площадей по IfcSpace не бьётся с ТЭП, покажи по каждой зоне RUS_Area и реальную площадь по геометрии, где разница больше 0.5 м2» (`ru-autodesk-telegram-s003`)<br>*(sum of IfcSpace areas does not match; per zone show RUS_Area and geometric area where diff > 0.5 m2)* | AP5 AP16 | Habr: [ТЭП vs XML on 20 m2](https://habr.com/ru/articles/1100956/) |
| RU-18 | «Проверьте, пожалуйста, наличие дублирующихся элементов в модели.» | «найди дубли элементов - одинаковые стены стоящие друг в друге, по bbox в пределах 5 мм, не удаляй, просто список» (`ru-habr-dev-s005`)<br>*(find duplicates: identical walls inside each other, bbox within 5 mm; don't delete, just list)* | AP19 AP2 | Habr: bounding box 5 mm |
| RU-19 | «Я работаю над проектом жилого комплекса «Северная звезда» в Москве, 25 этажей, монолитный каркас. Мы используем Revit 2024 и IFC4. Возникла проблема с координатами в Navisworks.» | «в нависе ифц улетел куда-то в сторону, координаты проверь, единицы ок?» (`ru-dwg-other-s014`)<br>*(in Navis the IFC flew off somewhere; check coordinates, are units ok?)* | AP8 AP17 | t-coordinates cell |
| RU-20 | «Как включить пользовательские параметры Revit в экспорт IFC, чтобы они отображались в наборе свойств?» | «параметры RUS_* из ревита в ифс не едут. файл общих параметров подсунул, всё равно пусто» (new)<br>*(RUS_* parameters don't make it from Revit to IFC; I fed the shared-parameter file, still empty)* | AP3 AP13 AP7 | Habr UDPS ([link](https://habr.com/ru/articles/1098340/)); t-psets-params cell |
| RU-21 | «Не могли бы вы любезно оказать содействие в получении перечня оборудования с указанием производителя и серийного номера из представленной информационной модели?» | «перед сдачей эксплуатации проверь у всего оборудования есть серийник и дата монтажа? что пустое - списком» (`ru-cobie-s005`)<br>*(before handing over to operations, does all equipment have serial and install date? list empty ones)* | AP12 AP1 | t-cobie-fm cell |
| RU-22 | «Определите, пожалуйста, какие трубы в модели не связаны с инженерной системой, и представьте результат списком.» | «у труб в модели есть имя системы и диаметр? выдай список без них» (`ru-dwg-revit-s010`)<br>*(do the pipes have system name and diameter? list the ones without)* | AP1 AP6 | t-mep cell |
| RU-23 | «Подскажите, пожалуйста, какую версию формата IFC и какое представление модели предпочтительнее использовать при выгрузке из Revit для передачи подрядчику.» | «подрядчик просит ифс, но не говорит какой. 2x3 или 4? какой вьюшкой выгружать» (`ru-vm-s005`)<br>*(contractor asks for IFC without saying which; 2x3 or 4? which view to export)* | AP1 AP3 AP8 | t-versions-mvd cell ("IFC4 meaning RV or DTV") |

### 2.2 English (EN-01 to EN-23)

| # | LLM-style | Human-style (synthetic) | Fixes | Grounding |
|---|---|---|---|---|
| EN-01 | "Hello! Could you please provide a comprehensive overview of the IfcBuildingElementProxy elements in my IFC model, including their count, names and the Revit categories they originated from? Thank you in advance!" | "how many IfcBuildingElementProxy in this revit export and what categories did they come from" (`en-gh-ifcopenshell-s001`) | AP1 AP5 AP14 | t-proxy-mapping cell |
| EN-02 | "I need to verify that all IfcWall elements contain the FireRating property within the Pset_WallCommon property set. Please generate a detailed report of any non-compliant elements." | "which walls dont have FireRating in Pset_WallCommon? list names + guids" (`en-reddit-s004`) | AP5 AP7 | t-psets-params cell |
| EN-03 | "Could you please assist me in identifying clashes between the HVAC ducts and the structural beams, using a tolerance of 10 mm, and group the results by building level?" | "run clash between ducts and structural beams, hard clashes only, tolerance 10mm, group by level" (`en-reddit-s010`) | AP1 | t-clash-bcf cell |
| EN-04 | "I would like to understand the differences between Open IFC and Link IFC in Autodesk Revit, and the advantages and disadvantages of each approach." | "why does File>Open IFC give me in-place families with no ifc data but Link IFC gives different geometry and dupes the assemblies? which one is meant to be used" (new) | AP6 AP13 AP18 | real: [revit-ifc #223](https://github.com/Autodesk/revit-ifc/issues/223) |
| EN-05 | "As a BIM Manager, I am responsible for data quality. Please perform a thorough validation of the IFC model against ISO 19650 requirements." | "pls check all IfcWall have FireRating and LoadBearing before we send to the revit team" (`en-graphisoft-s013`) | AP17 AP5 AP9 | t-validation-ids cell |
| EN-06 | "Please provide a detailed Bill of Quantities organised by building storey, including wall area, slab area and door count." | "make a BoQ per storey: slabs m2, walls m2, doors count, as a table I can paste in excel" (`en-qto-s004`) | AP1 AP5 | t-qto-cost cell |
| EN-07 | "My IFC file, exported from Revit 2024 using the IFC4 Reference View MVD with exporter version 24.2.0, appears to be positioned incorrectly. Could you analyse the georeferencing?" | "linked ifc sits too high in revit, levels at double height, open ifc was fine" (`en-gh-revit-ifc-s015`) | AP8 AP2 | real: [revit-ifc #990](https://github.com/Autodesk/revit-ifc/issues/990) |
| EN-08 | "Could you kindly explain what an IfcRelAggregates relationship is and how it differs from IfcRelNests?" | "when do i use aggregates vs nests? im modelling an AC-DC power supply w/ rectifier, battery, controller as sub-parts" (new) | AP9 AP13 | real: [buildingSMART forum](https://forums.buildingsmart.org/t/5016) |
| EN-09 | "The model appears to be very large. Please analyse the potential causes and suggest optimisation strategies." | "architect sent a 480mb ifc, site tablet chokes on it. whats the quickest way to get just the structure + level 2 to view on site" (`en-s005`) | AP19 AP5 AP16 | t-file-size cell |
| EN-10 | "It would be greatly appreciated if you could check for duplicate GlobalIds within the model and present the results in a clear format." | "check for duplicate GlobalIds in this model, list class and name for each pair" (`en-guid-s003`) | AP1 AP14 | t-guid-versioning cell |
| EN-11 | "URGENT!!! I need this IMMEDIATELY!!! My deadline is in one hour and my career depends on it!!! Please check the equipment data." | "which equipment in this model has no manufacturer or serial number? need it for handover friday" (`en-fmor-s001`) | AP10 AP19 | t-cobie-fm cell |
| EN-12 | "Could you please convert my DWG drawing to an IFC4 file using IfcOpenShell?" | "how can i export dwg to ifc4 by ifcopenshell, my language is C++, is there an example for CAD to ifc4" (real, [IfcOpenShell #3124](https://github.com/IfcOpenShell/IfcOpenShell/issues/3124)) | AP18 AP7 | real; "export" used for "convert" |
| EN-13 | "I would like to know the start station, end station and total length of every alignment contained in the IFC 4.3 model." | "whats the start/end station and length of every alignment in this file" (`en-civil-infra-s003`) | AP1 AP7 | t-infra-ifc43 cell |
| EN-14 | "Please review the IfcSpace elements and verify whether the Gross Floor Area and Net Floor Area values differ from one another." | "gross and net floor area look identical on all my rooms, is that an export bug? check the model" (`en-spaces-s002`) | AP13 AP19 | real: [revit-ifc #529](https://github.com/Autodesk/revit-ifc/issues/529) |
| EN-15 | "Could you list the storeys with their elevations and highlight any discrepancies with the levels defined in the original Revit model?" | "list storeys w elevations, revit shows different levels" (`en-graphisoft-s010`) | AP1 AP2 | t-coordinates cell |
| EN-16 | "Can you confirm whether the IFC file conforms to the IFC4 Reference View Model View Definition requested by the client?" | "client says they asked for IFC4 reference view. is this actually RV or just ifc4?" (new, after `de-vm-s010`) | AP3 AP2 | t-versions-mvd: "users say IFC4 meaning RV or DTV interchangeably" |
| EN-17 | "I am a beginner and would like to learn about the IFC format. Could you provide a comprehensive step-by-step guide covering all aspects?" | "i've used revit for years, never touched ifc. where do i even start in bonsai, practising on a small timber house" (new; paraphrases the real post) | AP5 AP9 AP6 | real: [OSArch roadmap post](https://community.osarch.org/discussion/3765/roadmap-for-revit-migrator-to-bonsai-bim-absolute-beginner) |
| EN-18 | "Please reclassify all proxy elements whose names contain the word 'asphalt' as IfcPavement elements with PredefinedType FLEXIBLE." | "reclass all proxies with asphalt in the name to IfcPavement FLEXIBLE pls" (`en-civil-infra-s008`) | AP1 AP3 | t-infra-ifc43 cell |
| EN-19 | "The IfcExportAs parameter is not functioning for slab edges. Could you investigate the underlying cause?" | "slab edges still come out as proxy even tho i set IfcExportAs to IfcSlab" (new; paraphrases real) | AP13 AP7 | real: [Autodesk forum](https://forums.autodesk.com/t5/revit-structure-forum/ifcexportas-parameter-doesn-t-work/td-p/8219179) |
| EN-20 | "Please compare Revision B and Revision C of the IFC model and summarise all differences in detail." | "compare rev B and rev C ifc - what got added/deleted/moved. only care about structure" (`en-us-canada-infra-s008`) | AP5 AP6 | t-guid-versioning cell |
| EN-21 | "Please verify that all MEP elements are assigned to a distribution system." | "which pipes and fittings arent in any IfcSystem? need before coord meeting" (`en-eng-s002`) | AP1 AP2 AP10 | t-mep cell |
| EN-22 | "Can you check whether the colours in the IFC model have been exported correctly?" | "half my walls come out grey in the viewer, which ones have no IfcSurfaceStyle at all?" (`mx-mcl-s001`) | AP19 AP13 | t-materials-colors-layers cell |
| EN-23 | "Why is my IFC file not working in Revit? Please diagnose the problem." | "one chair family exports fine and opens in bimvision but Link IFC just hangs revit" (real, [revit-ifc #951](https://github.com/Autodesk/revit-ifc/issues/951)) | AP19 | real: vagueness replaced by an observable plus a cross-check in another viewer |

### 2.3 Other languages (XX-01 to XX-18)

The first line of each human-style cell is the line itself; the italic line is the English gloss. Evidence levels differ: ZH, JA, ES have some real basis (see the style guide, section 13); FR, PT, KO, AR have **none** in real data, so those human-style lines are plausible but unverified.

| # | Lang | LLM-style | Human-style (synthetic) | Fixes | Grounding |
|---|---|---|---|---|---|
| XX-01 | zh | 「您好！麻烦您帮我检查一下这个IFC模型中所有墙体是否都具备"防火等级"和"是否外墙"两个属性，并将不满足条件的构件整理成清单。非常感谢！」 | 「按ids检查下：所有IfcWall必须有FireRating和IsExternal，不满足的导个清单」 (`zh-zhihu-s009`)<br>*(check by IDS: every IfcWall needs FireRating and IsExternal; export a list of failures)* | AP1 AP12 AP14 | zh cells; IDS usage |
| XX-02 | zh | 「您好，我在使用Revit 2019导出IFC文件时，点击导出按钮后软件没有任何反应，请问可能是什么原因导致的？」 | 「revit2019导ifc点了没反应只出个schema文件，咋回事」 (`zh-zhihu-s012`)<br>*(revit2019 export ifc, nothing happens, only a schema file; what's up)* | AP1 AP12 AP7 | real: [Zhihu](https://www.zhihu.com/question/455661969) |
| XX-03 | es | «Buenos días. ¿Podría usted indicarme, por favor, cuáles son las plantas del modelo con sus respectivas cotas y el número de elementos asignados a cada una?» | «dime las plantas del modelo con su cota y cuantos elementos tiene cada una» (`es-spain-s006`; accent on "cuántos" dropped)<br>*(tell me the storeys with elevation and how many elements each has)* | AP1 AP12 AP7 | es-spain cell |
| XX-04 | es | «Por favor, cree cuatro muros de tres metros de altura que formen un rectángulo de cinco por cuatro metros.» | «Creá cuatro muros de 3 m de alto formando un rectángulo de 5 × 4 m» (**real README prompt**, [archicad-mcp](https://github.com/joacos/archicad-mcp)) | AP12 AP1 | voseo "Creá"; digits and units |
| XX-05 | pt-BR | «Olá! Poderia, por gentileza, informar quantos elementos foram exportados como IfcBuildingElementProxy e de quais categorias do Revit eles se originaram? Agradeço desde já.» | «cara olha o ifc e me fala quantos elementos viraram proxy e de qual categoria do revit, preciso mandar a compatibilização hoje» (`pt-brazil-s001`)<br>*(dude look at the ifc and tell me how many became proxy and from which Revit category; need to send the coordination today)* | AP1 AP10 AP3 | pt-brazil cell (unverified style) |
| XX-06 | de | «Könnten Sie bitte so freundlich sein zu überprüfen, ob sämtliche Wanddurchbrüche im IFC-Modell korrekt als IfcOpeningElement exportiert wurden?» | «Pruef mal ob alle Wanddurchbrueche als IfcOpeningElement exportiert sind, bei manchen Waenden fehlt die Aussparung fuer die Tuer» (`de-geom-s011`)<br>*(check whether all wall penetrations are exported as IfcOpeningElement; some walls miss the door recess)* | AP1 AP12 AP2 | de-dach cell; Durchbruch/Aussparung vocabulary |
| XX-07 | de | «Bitte erstellen Sie eine detaillierte Mengenermittlung der Außenwände je Geschoss für das Leistungsverzeichnis.» | «Wandflächen und Volumen je Geschoss als Liste fürs LV, nur Außenwände. werden Öffnungen abgezogen? bitte angeben» (`de-dach-s007`)<br>*(wall areas and volumes per storey as a list for the bill of quantities, exterior walls only; are openings deducted? state it)* | AP5 AP2 AP19 | LV = Leistungsverzeichnis |
| XX-08 | fr | «Pourriez-vous avoir l'amabilité de réaliser une détection de conflits entre les gaines de ventilation et les éléments de structure avec une tolérance de 2 cm, puis d'exporter les résultats au format BCF ?» | «fais un clash gaines vs structure, tolérance 2 cm, et sors les points en BCF» (`fr-francophone-s017`)<br>*(run a clash ducts vs structure, 2 cm tolerance, and output the points as BCF)* | AP1 AP12 | fr cell (no real posts) |
| XX-09 | fr | «Je souhaiterais obtenir la liste exhaustive des équipements présents dans le modèle, avec le nom du fabricant et la référence pour chacun.» | «fais moi la liste des équipements avec fabricant et référence pour le DOE / GMAO» (`fr-francophone-s011`)<br>*(make me the equipment list with manufacturer and reference for the as-built file / CMMS)* | AP5 AP12 AP17 | DOE and GMAO are everyday French handover terms |
| XX-10 | ja | 「お忙しいところ恐れ入りますが、IFCファイル内のIfcBuildingElementProxyの数を、元のRevitカテゴリ別に集計していただけますでしょうか。」 | 「このIFC、IfcBuildingElementProxyが何個あるか数えて、元のRevitカテゴリ別に集計して。マッピング直す対象知りたい」 (`ja-japan-s001`)<br>*(count the proxies in this IFC by original Revit category; I want to know what to fix in the mapping)* | AP1 AP12 AP10 | ja cells |
| XX-11 | ja | 「IFCファイルの面積とRevitの集計表の面積に差異が生じている原因について、詳細にご調査いただけますと幸いです。」 | 「IFCの面積がRevitの集計表と合わない。単位か境界の問題？部屋ごとに差を出して」 (`ja-japan-s010`)<br>*(IFC area doesn't match the Revit schedule; unit or boundary issue? show the difference per room)* | AP5 AP12 | t-spaces-areas cell |
| XX-12 | ko | 「안녕하세요. 바쁘신 와중에 죄송하지만, 프록시로 분류된 객체 중 이름에 '기둥'이 포함된 것을 IfcColumn으로 변경해 주시겠습니까?」 | 「proxy로 나온 것 중 이름에 '기둥' 들어간거 IfcColumn으로 바꿔줘」 (`ko-korea-s007`)<br>*(of those that came out as proxy, change the ones with 'column' in the name to IfcColumn)* | AP1 AP12 | **no real Korean user data**; style hypothesised |
| XX-13 | it | «Buongiorno, potrebbe gentilmente verificare quali porte non dispongono della proprietà FireRating all'interno del Pset_DoorCommon?» | «dimmi quali porte non hanno il FireRating nel Pset_DoorCommon» (`it-italy-s002`) | AP1 AP12 | it cell (article-derived register) |
| XX-14 | nl | «Zou u zo vriendelijk willen zijn om te controleren welke elementen in het model geen NL-SfB-code hebben?» | «welke elementen hebben geen NL-SfB code of niet 4 cijfers? lijst per IFC class graag» (`nl-dutch-s002`)<br>*(which elements lack an NL-SfB code or one that is not 4 digits? list per IFC class please)* | AP1 AP12 | real tone: [NLCS #238](https://github.com/nl-digigo/NLCS/issues/238) |
| XX-15 | no | «Kunne du vært så snill å kontrollere om alle tekniske komponenter har FDV-informasjon og NS 3451-kode, og lage en liste over de som mangler?» | «har alle tekniske komponenter FDV-info og NS 3451-kode? vil ha liste over de som mangler» (`no-norway-s006`)<br>*(do all technical components have FDV info and NS 3451 code? want a list of the missing)* | AP1 AP12 | no cell (inferred) |
| XX-16 | ar | «السلام عليكم، هل يمكنكم من فضلكم التحقق من سبب ظهور أسماء الغرف العربية على شكل علامات استفهام بعد تصدير ملف IFC؟» | «أسماء الغرف بالعربي تظهر علامات استفهام بعد تصدير IFC، شو المشكلة؟» (`enc-s005`)<br>*(room names in Arabic show question marks after IFC export, what's the problem?)* | AP1 AP12 | **single synthetic prompt, no real data**; colloquial "شو" is Levantine |
| XX-17 | tr | «Merhaba, IFC dosyasında Türkçe karakterlerin neden Unicode kaçış dizileri olarak kodlandığını açıklayabilir misiniz?» | «ifc dosyasında ğ ü ş harfleri neden \X2\ diye kodlanıyor? bozuk mu?» (`enc-s015`)<br>*(why are ğ ü ş encoded as \X2\ in the ifc? is it broken?)* | AP13 AP1 | real encoding class: `\X2\00C7...` ([IfcOpenShell #101](https://github.com/IfcOpenShell/IfcOpenShell/issues/101)) |
| XX-18 | sk | «Prosím, mohli by ste oddialiť pôdorys o 15 percent a zobraziť vzduchotechniku v perspektívnom pohľade na celú obrazovku?» | «Oddiaľ pôdorys o 15 percent. / Ukáž vzduchotechniku v perspektíve na celú obrazovku.» (**real**, [AIMviewer #65](https://github.com/Menezeris/AIMviewer/issues/65)) | AP1 AP4 | the only Slovak real example: two plain imperatives |

---

## 3. Rewriting rules

Apply in order. Each rule says what to do and gives a quick example.

| # | Rule | Example |
|---|---|---|
| **R1** | **Delete the wrapper:** greeting, "please/could you/would you", "thank you", sign-off, "let me know". | "Could you please list X? Thanks!" -> "list X" |
| **R2** | **Start with the verb or the symptom.** Put the background after, as a clause, or drop it. | "I have a model and want to know ..." -> "which walls ..." |
| **R3** | **Point at the model, don't describe it:** "this model", "эту модель", "这个ifc", "este ifc", "このIFC". | "the attached IFC4 file exported from Revit 2024" -> "this ifc" |
| **R4** | **Cut to one anchor.** Keep the single most specific item: a class, a pset name, a number with unit, a name pattern. Delete the other four. | "tolerance 10 mm, level 02, hard clashes only, by system, by discipline" -> "tolerance 10mm, group by level" |
| **R5** | **Add the human reason in one clause** when natural: a deadline, a person waiting, a failed earlier attempt. | "...need it before the coord meeting" / "заказчик требует" |
| **R6** | **Use the person's word for the thing:** proxy/проксики, ифс, ревит, "BoQ", "LV", "DOE", "family", "export". Keep class and property names exact where the task depends on them. | "IfcBuildingElementProxy" -> "proxy" (unless the exact class matters to the check) |
| **R7** | **Let the Revit/IFC vocabulary mix happen once,** if the persona is a non-expert (architect, owner, student): "family", "category", "open or link", "export" for convert. | "как из архикада ифс затащить чтоб были стены" |
| **R8** | **Use the language's colloquial register.** RU: ты-imperative, no "вы"; ZH: 咋回事/导个清单/查下; JA: plain imperative (...して); ES: "dime", "dame", voseo where regional; DE: "zeig mir", "prüf mal"; FR: "fais moi", tutoiement; KO: 해줘 (unverified); keep technical tokens in Latin script. | see section 2.3 |
| **R9** | **Replace round numbers with measured-looking ones** or drop them. | "100 elements" -> "212 doors"; "50 MB" -> "480mb" |
| **R10** | **Allow at most one slip** (dropped accent, lowercase product, "recieve", missing apostrophe), never in the key token; skip it in half the prompts. | "cuantos" (no accent), "dont" |
| **R11** | **Make the structure lopsided:** one detailed part, one thin part, or a piggy-backed check ("...and any elements without a storey?"). | RU-12 |
| **R12** | **Kill "comprehensive/detailed/thorough/complete".** Replace with the single question the report would answer. | "comprehensive validation" -> "which walls have no FireRating" |
| **R13** | **Turn lectures into symptoms:** "explain X" -> "why does Y happen on my file" or "what do I use for Z". | EN-04, EN-08, RU-04 |
| **R14** | **Understate emotion.** Replace shouting with "again", "still", "??", or a deadline. No bold, no capitals for emphasis. | EN-11, RU-15 |
| **R15** | **State the output format only if it is practical and short:** "csv ok", "list with guids", "таблицей", "as a table I can paste in excel". | EN-06 |
| **R16** | **Add an honest-answer or safety clause in about one prompt of eight:** "if there is no Qto, say so", "не удаляй, просто список", "don't change anything". | RU-06, RU-18 |
| **R17** | **Check the batch,** not just the prompt: vary openers, lengths, languages, personas (section 4). | |
| **R18** | **Re-read as the tester.** Could someone who can open the model verify the answer in a minute? If not, restore the missing anchor (section 5). | |

### 3.1 Worked rewrite, English (5 steps)

| Step | Text | Rule applied |
|---|---|---|
| 0. LLM draft | "Hello! As a BIM coordinator working on a hospital project, I would like to request a comprehensive analysis of the attached IFC4 Reference View model exported from Revit 2024. Could you please identify all elements that have been exported as IfcBuildingElementProxy, provide their names and original Revit categories, and present the results in a structured table? Thank you very much for your assistance." (52 words) | |
| 1 | "As a BIM coordinator ... I would like to request ... Could you please identify all elements that have been exported as IfcBuildingElementProxy, provide their names and original Revit categories, and present the results in a structured table?" | R1 (and drop the persona, AP17) |
| 2 | "identify all elements exported as IfcBuildingElementProxy, with names and original Revit categories, in a table" | R2, R3, R12 |
| 3 | "how many proxies in this model and what revit categories did they come from" | R4, R6 |
| 4 | "loads of proxies in this one again. how many, and what revit categories? need to fix export mapping" (adds a because-clause, British "loads of") | R5, R14 |
| 5 | Check: one anchor (proxy), no version, no greeting, 18 words, answerable by reading class counts. | R18 |

### 3.2 Worked rewrite, Russian (5 steps)

| Step | Text | Rule applied |
|---|---|---|
| 0. LLM draft | «Здравствуйте! Я BIM-менеджер, готовлю модель к государственной экспертизе. Не могли бы вы, пожалуйста, провести проверку IFC-файла на наличие обязательных свойств у стен и перекрытий и представить подробный отчёт о выявленных нарушениях? Заранее благодарю.» (36 слов) | |
| 1 | Убрать приветствие, «не могли бы вы, пожалуйста», «заранее благодарю» | R1 |
| 2 | «проверь IFC на наличие обязательных свойств у стен и перекрытий, дай отчёт о нарушениях» | R2, R12 |
| 3 | «проверь ифс: у стен и перекрытий заполнены обязательные свойства? пустые списком» | R6, R15 |
| 4 | «надо сдавать на экспертизу в понедельник, проверь ифс что у всех стен и перекрытий заполнены обязательные свойства, список пустых выгрузи» | R5, R8 (this is `ru-tim-expertiza-s001` in spirit) |
| 5 | Проверка: мотив есть (понедельник), якорь есть (стены и перекрытия, обязательные свойства), формат есть (список), тон без эмоций. | R18 |

---

## 4. Batch-level anti-patterns and targets

A batch of 20 invented prompts often fails as a set even when each prompt looks fine.

| Failure | Sign in a batch | Fix (recommended target, derived from the data in the style guide) |
|---|---|---|
| Same shape | 20 prompts all 25 to 35 words, all starting with a verb, all ending with a format | Spread: 5% title-only (2 to 8 words), 60% one line (6 to 25), 25% line + pasted detail, 10% forum-style paragraph |
| Same opener | "Please check ..." x 12 | Mix: verbs, questions ("how many ..."), symptom-first ("ifc улетел ..."), noun phrase ("таблицу помещений: ..."), because-clause first |
| Same polish | No typo anywhere in 20 prompts | About 1 in 4 or 5 carries one slip |
| Always full context | Every prompt names the software version | Version in about 1 of 5; schema in under 1 of 4 |
| Only experts | All coordinators and developers | Add owner/FM, estimator, student, architect; across all 3,525 records the persona tags are dominated by coordinators (949) and developers (825), so non-experts need a deliberate quota |
| Only English | Every language is a translation of the English batch | Write each language from its own habits (style guide section 13); keep 20 to 30 % of non-English prompts in the local slang |
| Every task is solvable | All tasks have a clean answer | Include tasks where the model lacks the data (no Qto, no material) and the right answer is "not there" |
| Uniform difficulty | Three equal bands | Do not force equal thirds; the existing synthetic prompts in this KB skew medium (53% medium, 27% hard, 20% easy) |
| Clean sequence | No follow-ups | About 1 in 10 is a follow-up that depends on a first answer |
| No honest tests | No request asks the assistant to admit a limit | About 1 in 8 includes "if not there, say so" or asks for something the model cannot know |

---

## 5. When *not* to roughen

Realism must not break testability.

- **Keep the task checkable.** The tester must be able to verify the answer in the model: keep the exact class or property name, the number, the name pattern.
- **Do not damage the key token.** A typo in `Pset_WallCommon`, `FireRating` or a threshold turns a test of the assistant into a test of luck.
- **Do not hide the object.** "Check my model" with nothing else is unrealistic and untestable (AP19). Real vagueness still names an observable.
- **Do not invent facts the model cannot hold.** "Is this compliant with the Moscow АГР procedure" needs the rule set; either name it ("по IDS ЦГЭ") or expect the assistant to ask.
- **Do not copy real private details.** Real records have no personal data; neither should invented prompts. Use generic names ("Колонна_*", "level 02").
- **Mark trap cases.** A prompt that depends on the assistant fixing a loose term ("family" for an IFC element) should be flagged in the test metadata, not left implicit.
- **Do not go overboard with slang.** The real corpus is mostly plain; slang concentrates in Russian, Chinese and Spanish chat-style titles. English prompts are mostly plain lowercase with a few abbreviations ("pls", "w", "mb").
- **Respect evidence gaps.** For Korean, French, Portuguese and Arabic there are no real user posts in this KB; keep prompts short and plain, avoid invented slang, and label them "unverified style" in test metadata.

---

## 6. Quick lint for a single prompt

Reject and rewrite if **any** of the following is true:

1. It begins with a greeting or "Could you / Would you / Can you please".
2. It ends with thanks or an offer of further help.
3. It contains the words comprehensive, thorough, detailed analysis, complete overview (or the same in the target language: "комплексный", "подробный", "详细", "包括所有方面", "包括的").
4. It names the persona ("As a ...").
5. It contains three or more parallel criteria of equal weight.
6. It states a full version stack (year + exporter + schema + MVD).
7. It uses a bulleted or numbered list in a one-line register.
8. It asks "what is X" with no link to a file or task.
9. It has more than 40 words and no pasted detail.
10. The tone is "!!!" or the all-caps urgent type.
11. It is grammatically perfect in a language where the genre is clipped chat (RU, ZH, ES, PT, JA, KO) and has no local slang or transliteration at all.

Then run the positive check: [style guide checklist](style_guide.md#14-checklist-does-this-sound-like-a-real-person).
