# Contractor and site team: who they are and what they do with IFC

> Persona tag in the data: `contractor_site`. Evidence base: `kb.py stats --persona contractor_site` gives only 40 records (17 real, 23 synthetic) from `research_raw/wave1`. **This is the thinnest persona in the knowledge base.** To reach a usable size, this page adds clearly labelled "adjacent" real questions from neighbouring personas (estimator, structural, BIM coordinator) that a site team would plausibly ask, and a few new synthetic prompts. Last compiled 2026-11-06.
> Sibling pages: [estimator / QS](estimator_qs.md), [structural engineer](structural_engineer.md), [MEP engineer](mep_engineer.md), [student / beginner](student_beginner.md). Topic overview: [quantities, cost, schedule](../by_topic/quantities_cost_schedule.md), [file size, viewing, conversion](../by_topic/file_size_viewing_conversion.md).

## In plain words

A main contractor, subcontractor, site engineer, foreman, planner or construction manager is the person who has to **build** what the designers drew. They rarely author IFC. They **receive** it (from the architect or coordinator) and want to do concrete things with it:

- look at the model on a phone, tablet or a modest laptop without a heavy design program;
- get quantities for a pour, an order or a work package;
- link model elements to the construction schedule (**4D**: the model animated against time) or to costs (**5D**);
- check what changed since the last revision;
- prepare setting-out points, prefabrication lists, as-built updates and handover information.

They think in **levels, zones, work packages, trades and dates**, not in IFC classes. They do not care that the element is `IfcSlab`; they care that it is "Level 3 slab, pour 2". The most common frustration is not "the export is broken" but "I cannot even open this file on site" (`ja-japan-r013`, `en-s005`).

Evidence caveat: the 17 real records tagged to this persona are mostly open-source 4D / schedule issues (IfcOpenShell / Bonsai) and a handful of single items from Japan, Italy, Norway and Latin America. There is no real Russian, German, French or Korean contractor material in the data; the Russian and other non-English prompts below are synthetic or new synthetic. A site-team voice from a real forum (Russian "прораб", German "Bauleiter", Portuguese "mestre de obras") is **not observed**; role-play it from the patterns below, and mark it as such in test reports.

## Daily IFC tasks

| Task | What it looks like in practice | Typical tools | Example ids |
|---|---|---|---|
| View the model on site | Open a heavy architect IFC on a tablet or low-end PC; ask for "just structure and level 2". | Free viewers, Trimble Access / field apps, web viewers | `ja-japan-r013`, `en-s005`, `es-latam-r019`, `en-mea-s009` |
| Quantities per level for a pour or order | Concrete m3 by level, rebar by pier, count of doors by type. | Spreadsheet, QTO tools | `en-gh-ifcopenshell-s009`, `it-italy-s017`, `ko-korea-s006`, `fr-francophone-s009`, `en-us-canada-infra-s007` |
| Link elements to the schedule (4D) | Build a work schedule, link columns / slabs / beams to tasks, find elements with no task. | Bonsai, Synchro, Fuzor, Navisworks, Primavera P6 | `en-gh-ifcos-r009`, `en-osarch-r011`, `en-s003`, `pt-s010`, `ko-s014`, `en-s017` |
| Group elements into work packages | By level and type, structure only. | Scripts, QTO tools | `es-latam-s015`, `ja-data-s014` |
| Check what changed between revisions | Which elements are new / moved / deleted, and which of those are already in the 4D plan. | Compare tools | `pt-guid-s010` |
| Clash-check above the ceiling | Duct vs beam clearance before installation, exported as BCF. | Navisworks, Solibri, BIMcollab | `ja-japan-s008` |
| Handover information | What to deliver (COBie or IFC with properties?) so the client can run the building. | COBie sheets, IFC | `en-uk-anz-india-s013`, `zh-revit-export-r011` |
| Procurement / prefab tracking | Mark elements as procured, fabricated; read manufacturer data. | IFC properties, spreadsheets | `no-norway-s015`, `no-norway-r012`, `nl-dutch-r023` |

## Goals

- **Open and navigate the model without a licence and without waiting** (`ja-japan-r013`, `en-gh-thatopen-r049`, `es-latam-r019`).
- **Quantities they can pay or order against**, with a clear statement of what is included (`en-gh-ifcopenshell-s009`, `en-us-canada-infra-s007`, `mx-mcl-s017`).
- **A schedule-linked model** that matches what commercial 4D tools show, so planners can trust the animation (`en-gh-ifcos-r009`, `en-gh-ifcos-r010`, `en-osarch-r011`).
- **Fewer manual clicks to link model and schedule / cost** (`en-s003`, `pt-s010`, `ko-s014`; cf. `en-gh-ifcos-r017` in the estimator list).
- **A stated information requirement they can actually meet** in the tender: what to deliver, in what format, with what properties (`it-italy-r018`, `no-norway-r009`, `en-uk-anz-india-s013`).
- **Reuse the designers' IFC for fabrication and procurement** without redrawing (`no-norway-s015`, `en-blogs-linkedin-r030`).

## Pains (ranked)

Ranking is editorial and based on a small sample (17 core real records plus the adjacent ones); treat it as a hypothesis.

| Rank | Pain | What the user says (paraphrase) | Evidence ids |
|---|---|---|---|
| 1 | **Files are too heavy to open on site.** | "to just look at the IFC I need gigabytes of software; site staff have no environment" / "a 2 GB industrial IFC loads very slowly" / "architect sent 480 MB, the site tablet chokes" | `ja-japan-r013`, `en-gh-thatopen-r049`, `en-s005`, `en-mea-s009` |
| 2 | **4D animation does not behave.** Tasks show up wrongly, objects appear and vanish instead of moving; only an interactive HTML gantt instead of a synced timeline. | "two walls, three tasks (construct, move, demolish): schedule shows but the animation misbehaves" / "where do I put the displacement for a MOVE task?" | `en-gh-ifcos-r009`, `en-gh-ifcos-r010`, `en-osarch-r011`, `en-gh-ifcos-r018`, `en-gh-ifcos-r019` |
| 3 | **Schedule and cost CSV import/export breaks.** | "work schedule CSV import fails, CSV lacks Relationships column" | `en-gh-ifcos-r016`, `en-gh-ifcopenshell-r044`, `en-data-r014` |
| 4 | **Nobody told them what to deliver.** Information requirements arrive as a tender clause nobody explains; or none exists. | "do I have to submit the information management offer in the tender or am I excluded?" / "contractor needs IFC for cost estimation but we have no BEP" / "where do I find the client's digital delivery requirements?" | `it-italy-r018`, `no-norway-r009`, `en-blogs-linkedin-r030`, `en-uk-anz-india-s013` |
| 5 | **Colours and presentation do not survive export** (so the site model looks nothing like the design). | "colors from view filters are not exported" | `en-autodesk-revit-export-r041` |
| 6 | **Concepts of the model are opaque.** | "I use a parent/child analogy: only the children carry geometry?" (aggregates vs nests) | `en-bsforum-r006`, `en-gh-ifcos-r020` |
| 7 | **Updates overwrite site data.** Re-export from Revit loses cost and schedule data added to the earlier IFC. | "how can a Revit model be re-exported and updated without losing cost and schedule data?" | `en-osarch-r011`, `en-roundtrip-r006` |
| 8 | **Subcontractor models are heavy or inconsistent.** | "subcontractors share a cached .ifc.rvt, rotation differs between Link IFC and the cached file" | `en-roundtrip-r006`, `ja-japan-r014` |
| 9 | **Field data and AI.** | "click a component and AI suggests tags from properties and past defects" | `ja-data-r035` |

## Vocabulary they use (and what they do not know)

| They say | Meaning for them | What they usually do not know / confuse |
|---|---|---|
| 4D / 5D, lookahead, AWP / IWP, work package, Gantt, Primavera P6, Synchro, Fuzor | Model + time / model + cost; planning vocabulary | That in IFC a *task* is an object linked to elements and that "move" or "demolish" are task types, not geometry (`en-osarch-r011`). |
| BoQ, QTO, takeoff, tender, 积算 / 積算, DPGF, computo, pour sheet | Quantities for pricing or ordering | Gross vs net (openings), which quantity set the number came from, what a missing quantity means. |
| level / storey / pavimento / этаж / 層 / piso / 층 | The floor, used as the grouping axis | That "level" is a separate object and some elements are not attached to any (`en-s003`). |
| COGO, setting out, replanteo, CRS | Field survey points and layers | That IFC may carry presentation layers but field apps do not all read them (`es-latam-r019`). |
| "IsProcured", "Milestone" (Norwegian NS 8360 properties) | Procurement flags | That these are ordinary properties and the model may not have them (`no-norway-s015`). |
| COBie, AIM, handover, 竣工 | What to give the client at the end | Whether COBie or IFC with properties is expected (`en-uk-anz-india-s013`, `zh-lightweight-review-r025`). |
| "oGI" (Italian information management offer), "BEP", "EIR" | Tender documents | That they define which properties and which file format are required (`it-italy-r018`). Background: [requirements in contracts](../../02_standards_regulations/requirements_in_contracts_eir_bep.md). |

Plain-language bridge: a site manager sees the building as "areas of work by floor and trade". IFC offers exactly that: elements, which floor they are on, which type they are, and (if someone added it) a task and a date. When these links are missing, the 4D animation is empty and the quantity list is wrong, not because the contractor did anything wrong but because no one entered the links. Background: [domains overview, 4D/5D section](../../01_ifc_basics/08_domains_mep_structural_infra_4d5d_fm.md), [properties and quantities](../../01_ifc_basics/05_properties_quantities_psets.md), [open-source libraries](../../04_open_source/libraries_and_toolkits.md), [viewers and checkers](../../03_software/viewers_checkers_cde_converters.md), [glossary](../../08_glossary/glossary_multilingual.md).

## Real questions

The first 17 rows are the real records tagged `contractor_site` in the data (17). They are a small, open-source-heavy sample. Language mix of the whole first table: en 11, ja 2, es 1, it 1, no 1, zh 1. The "Question" column is the research pass's **paraphrase** of the source (not a verbatim quote).

| # | ID | Lang | Question (paraphrase, original language) | English gloss | Outcome in source | Source |
|---|---|---|---|---|---|---|
| 1 | `en-gh-thatopen-r049` | en | integrating fragments into a construction PM platform, 2 GB industrial IFC loads very slow, need IFC plus Primavera P6 schedule, AWP/IWP, lookahead | — | Maintainer pointed to the streaming import example in PR 311. | [GitHub #315](https://github.com/ThatOpen/engine_fragment/issues/315) |
| 2 | `ja-japan-r013` | ja | IFCを少し見るだけで数GBのソフトが必要。現場担当は開く環境がなく設計変更のたび重いアプリを起動 | Site staff cannot open IFC without multi-GB software; built a browser-only IFC viewer with clash check | web-ifc WASM parsing in browser, Octree raycast, AABB then BVH clash, chunked mesh building to avoid UI freeze. | [zenn.dev](https://zenn.dev/kazuyamaeda/articles/97933cdafce6d8) |
| 3 | `es-latam-r019` | es | archivos IFC para replanteo, COGO, capas desde presentation layer, no soportado en Android | Trimble Access Spanish help: IFC (.ifc, .ifczip) usable for stakeout and COGO, layers from presentation layers, not on Android | Surfaces and vertices selectable; attributes can be saved to design file. | [help.fieldsystems.trimble.com](https://help.fieldsystems.trimble.com/trimble-access/2021.20/es/Map-files-BIM-and-IFC.htm) |
| 4 | `it-italy-r018` | it | in gara serve per forza l'oGI? se non la presento vengo escluso? | Is the offerta di gestione informativa (oGI) mandatory in BIM tenders? (Consiglio di Stato 6834/2026) | Court ruling discussed; oGI role in CI-oGI-pGI chain. | [biblus.acca.it](https://biblus.acca.it/notizie/appalti-bim-lofferta-di-gestione-informativa-e-obbligatoria/) |
| 5 | `no-norway-r009` | no | hvor finner jeg Nye Veiers krav til digitale leveranser? | Supplier page of Nye Veier: tenders via Doffin and Artifik, delivery through total contractors; no BIM/IFC rules stated | Page covers EHF invoicing, Doffin/Artifik, ISO certifications and 30% climate weighting; BIM/IFC requirements must be found in the tender documents. | [nyeveier.no](https://www.nyeveier.no/for-leverandoerene/) |
| 6 | `en-gh-ifcos-r009` | en | P6 schedule imported, only an interactive Gantt HTML is produced; wants native synced animated timeline like Fuzor/Synchro | — | Live date already animates with the animation; the animated timeline feature does not exist yet. | [GitHub #2050](https://github.com/IfcOpenShell/IfcOpenShell/issues/2050) |
| 7 | `en-gh-ifcos-r010` | en | two IfcWall with same geometry, three IfcTask (construct, move, demolish); tasks show in the schedule but animation misbehaves | — | Not read in detail; see the related forum thread on MOVE tasks. | [GitHub #2413](https://github.com/IfcOpenShell/IfcOpenShell/issues/2413) |
| 8 | `en-osarch-r011` | en | construct and demolish tasks show objects appearing and vanishing; where do I put the displacement for a MOVE task? | — | MOVE needs both input and output products; duplicate the element at the new location and link old as process input and new as product output. | [community.osarch.org #1131](https://community.osarch.org/discussion/1131/ifcopenshell-python-ifctask-predefinedtype-construction-demolition-move) |
| 9 | `en-gh-ifcos-r016` | en | work schedule CSV import fails; CSV lacks Relationships column | — | Importer read every column unconditionally; should treat missing Relationships column as blank. | [GitHub #8580](https://github.com/IfcOpenShell/IfcOpenShell/issues/8580) |
| 10 | `en-gh-ifcos-r018` | en | colour-coded task types in 4D animation via custom ObjectType | — | Not read. | [GitHub #2748](https://github.com/IfcOpenShell/IfcOpenShell/issues/2748) |
| 11 | `en-gh-ifcos-r019` | en | hour granularity in generated Gantt chart | — | Not read. | [GitHub #2772](https://github.com/IfcOpenShell/IfcOpenShell/issues/2772) |
| 12 | `en-gh-ifcos-r020` | en | needs docs on work schedules and resource assignment | — | Not read. | [GitHub #2016](https://github.com/IfcOpenShell/IfcOpenShell/issues/2016) |
| 13 | `en-gh-ifcopenshell-r044` | en | CSV import errors with key error | — | Optional Relationships column wrongly assumed | [GitHub #8580](https://github.com/IfcOpenShell/IfcOpenShell/issues/8580) |
| 14 | `en-bsforum-r006` | en | general contractor uses a parent/child OOP analogy to understand IfcRelAggregates vs IfcRelNests and thinks only the children carry geometry with aggregation | — | IfcRelNests implies an ordered list of parts; aggregation is unordered composition; geometry is not the real differentiator. | [forums.buildingsmart.org](https://forums.buildingsmart.org/t/4272) |
| 15 | `en-autodesk-revit-export-r041` | en | Colors from view filters are not exported. | — | Idea open. | [forums.autodesk.com](https://forums.autodesk.com/t5/revit-ideas/ifc-export-element-color-export-as-per-visibility-graphics/idi-p/12995112) |
| 16 | `ja-data-r035` | ja | クリックした部材のプロパティからAIがタグを生成し、過去の不具合事例を検索して原因と対策を表示する。 | Demo where clicking an IFC element in a browser viewer fetches its properties, generates semantic tags with AI and matches them to a structured defect-report knowledge base for pre-construction review. | Properties to tags to RAG matching. | [qiita.com](https://qiita.com/dnp-hiraoka/items/aa1d12e5784485542583) |
| 17 | `zh-revit-export-r011` | zh | revit模型怎么导进广联达BIM5D，插件和IFC哪个好 | Revit plugin for exporting to Glodon BIM5D, richer than IFC. | Plugin reads Revit source data directly, more complete than IFC; supports floor merge, MEP and civil export. | [bbs.zhulong.com](https://bbs.zhulong.com/106010_group_3002227/detail33178172/) |

### Adjacent real questions (tagged to other personas)

These are real records tagged with other personas (estimator, structural engineer, BIM coordinator, developer) that a contractor or site team would plausibly ask. They are listed here so the page reaches a usable size; the persona tag in the data is different, and the id shows the source cell.

| # | ID | Lang | Question (paraphrase, original language) | English gloss | Outcome in source | Source |
|---|---|---|---|---|---|---|
| 18 | `en-blogs-linkedin-r030` | en | contractor needs IFC for cost estimation but we have no BEP or template | — | Set BEP/template, check classification (Ctrl+T), survey point, only mapped properties, graphic override QA, Publisher sets. | [bimcorner.com](https://bimcorner.com/exporting-ifc-from-archicad/) |
| 19 | `en-roundtrip-r006` | en | Inconsistent rotation between Link IFC and linking the cached .ifc.rvt; subcontractors share the .ifc.rvt; detailed Tekla IFCs cleaned by script. | — | Logged in Autodesk Jira; open. | [GitHub #710](https://github.com/Autodesk/revit-ifc/issues/710) |
| 20 | `no-norway-r012` | no | hvilke egenskaper krever NS 8360 i modellen, f.eks. Milestone og IsProcured? | NS 8360 concepts: LOD, custom property sets, process status codes, IsProcured, Milestone, DuplicateOwnedBy | NS 8360 defines process-information property sets and status codes used to mark object maturity and procurement. | [buildingsmart.no](https://www.buildingsmart.no/standarder/kort-forklart.html) |
| 21 | `nl-dutch-r023` | nl | Materiaalnamen verschillen: prefabbeton, gewapend beton, grindbeton, ihw, ihwg, tpg; computers kunnen dit niet betrouwbaar interpreteren | Material names vary (prefab concrete, grindbeton, ihw); computers cannot interpret; NAA.K.T. fixes order | Mnemonic NAam_Kenmerk_Toepassing. | [digigo.nu](https://www.digigo.nu/ilsen-en-richtlijnen/bim-basis-ils/praktijk/1-naa-k-t-eenduidige-materiaalbenaming) |
| 22 | `ru-dwg-other-r014` | ru | экспорт в ifc из Теклы 2017 для Field 3D не работает как надо, настройки не помогают | Tekla 2017 IFC export for Tekla Field 3D does not work as expected; changing settings does not help. | One export setting (surface geometry) fixed it. | [forum.dwg.ru](https://forum.dwg.ru/showthread.php?t=146367) |
| 23 | `zh-lightweight-review-r025` | zh | 竣工模型交付用什么格式，要在施工图模型基础上加变更信息吗 | Nanjing local standard for as-built (completion) BIM delivery; format preferably 宁建模. | Completion model builds on drawing-review model plus changes; delivered after BIM review and completion filing. | [amr.nanjing.gov.cn](https://amr.nanjing.gov.cn/ztzl/bzhzl/tzgg/202302/P020230216538033075572.pdf) |
| 24 | `ja-japan-r014` | ja | 協力会社の重いモデルや古いモデルを開かずに値だけ取り出したい。API/プラグイン経由は遅くAPSは組織整備が前提 | Extract values from heavy Revit models from subcontractors without opening them; ETL to columnar store | EAV + column-oriented storage in Parquet, analyze with DuckDB. | [zenn.dev](https://zenn.dev/tomosandego/articles/59e6cf8dfe60bc) |
| 25 | `en-eng-r008` | en | Precast girder stirrups project straight and are bent on site; wants both fabricator and final geometry conveyed. | — | Multiple representations per product allowed in schema but no way to label them; tool support lacking. | [forums.buildingsmart.org](https://forums.buildingsmart.org/t/field-bent-rebar/5870) |
| 26 | `en-qto-r004` | en | trying to get a budget for a small toilet building but some quantities in the IFC are not correct; asks what they are doing wrong | — | QTO is not live-updated: run the calculation explicitly (Shift-Q); aggregates were also missing. | [GitHub #4964](https://github.com/IfcOpenShell/IfcOpenShell/issues/4964) |
| 27 | `en-qto-r009` | en | spreadsheet-based BoQ is how tenders work; wants a simple CSV BoQ export preserving GlobalId/Tag/location links to IFC elements | — | Maintainer suggests Spreadsheet Import/Export; requester says it does not cover the need. | [GitHub #7762](https://github.com/IfcOpenShell/IfcOpenShell/issues/7762) |
| 28 | `en-qto-r022` | en | lightweight alternative to full estimating suites; asks what prevents real-project use and what CSV export should contain | — | Shows 2D PDF takeoff remains a parallel workflow to IFC QTO. | [community.osarch.org #3576](https://community.osarch.org/discussion/3576/plan-measure-open-source-pdf-takeoff-tool-looking-for-aec-feedback) |
| 29 | `en-data-r005` | en | Tender and cost work runs on spreadsheets; I need rows traceable to IFC elements, e.g. ventilators FAN-01..03 per room, and summarise equal elements by floor. | — | Use Spreadsheet Import/Export and group/sum by an aggregator property; link to cost items via code or GUID. | [GitHub #7762](https://github.com/IfcOpenShell/IfcOpenShell/issues/7762) |
| 30 | `en-osarch-r012` | en | how to keep a CSV BoQ linked to the IFC cost schedule, and let one cost item match differently named quantities across element types | — | Selectors work in Query and Spreadsheet but not Property; link persistence added via document reference; regex request filed on GitHub. | [community.osarch.org #2887](https://community.osarch.org/discussion/2887/dynamic-csv-to-cost-schedule-now-available) |
| 31 | `en-struct-r006` | en | wants rebar weight per concrete volume as custom Qto for cost schedule; rebar not modeled | — | Options: density on a 'rebar' material, Qto_ReinforcingElementBaseQuantities, Pset_ConcreteElementGeneral.ReinforcementVolumeRatio, script writing custom pset. | [community.osarch.org #2578](https://community.osarch.org/discussion/2578/how-to-create-a-custom-qto-calculation) |
| 32 | `en-gh-ifcos-r017` | en | assigning elements to cost item needs select, unit, click; wants query such as walls with concrete, saved in the quantity Formula | — | Implemented later with a query field in the Cost Items Quantities panel. | [GitHub #5390](https://github.com/IfcOpenShell/IfcOpenShell/issues/5390) |
| 33 | `en-gh-ifcos-r001` | en | IfcOpenShell QTO gives wrong area for an IfcWindow defined by an IfcWindowType with mesh geometry, Blender shows right value; attached test file | — | No answer in thread at time of reading. | [GitHub #5349](https://github.com/IfcOpenShell/IfcOpenShell/issues/5349) |
| 34 | `en-qto-r002` | en | after Perform Quantity Takeoff Bonsai reports Gross 9.81 = Net 9.81 whereas Solibri gives Gross 20.08; affects almost all walls | — | Gross short-circuits to Net when no IfcRelVoidsElement; maintainers ask for a semantics decision. | [GitHub #9235](https://github.com/IfcOpenShell/IfcOpenShell/issues/9235) |
| 35 | `ja-japan-r024` | ja | 図面から数量を拾うのが時間と精度の両立が難しい。モデル化されない部材の数量ルールは？ | BIM-based quantity takeoff: reading IFC from ArchiCAD for estimating; unmodeled members need rules | MLIT encourages IFC for takeoff; Maeda reads ArchiCAD IFC for exterior walls, columns, beams into estimating software. | [note.com](https://note.com/bold_cobra9180/n/n4f52d62f230f) |

## Ready test prompts

36 prompts for an MCP server or assistant connected to an IFC file. **All are synthetic**: the first 23 are the research pass's `contractor_site` synthetic prompts; the next five are borrowed from neighbouring personas because they fit a site team; rows whose id starts with `new-contractor-` were written for this page (no observed site-team phrasing exists in Russian, so these are extrapolations). Russian and English get the most rows.

| # | ID | Lang | Prompt (synthetic, as the user would type it) | File needed | Difficulty | What a good answer does |
|---|---|---|---|---|---|---|
| 1 | `en-beginner-qa-s007` | en | which doors have fire rating and what are they | yes | medium | Read Pset_DoorCommon.FireRating for IfcDoor, list by value and missing. |
| 2 | `en-civil-infra-s011` | en | terrain mesh in there? any earthworks cut/fill elements with volumes | yes | medium | Find terrain representations and IfcEarthworks*; report quantities if present or say they are absent. |
| 3 | `en-gh-ifcopenshell-s009` | en | total concrete volume per level, columns beams slabs separate | yes | medium | Aggregate NetVolume by class and storey for concrete material. |
| 4 | `en-graphisoft-s015` | en | how many doors and windows have openings in walls? some walls look solid | yes | hard | Check IfcRelVoidsElement and IfcRelFillsElement, report unmatched doors/windows. |
| 5 | `en-mea-s009` | en | this ifc is 900MB and my laptop dies. what is making it so big? can we strip out the furniture and landscaping | yes | medium | Report element counts and geometry weight by class, identify heavy classes, offer a reduced copy without selected classes. |
| 6 | `en-uk-anz-india-s013` | en | what do we actually need to hand over for asset info, COBie or IFC with psets? client's EIR just says 'AIM compatible' | no | easy | Explain AIM under ISO 19650-3, COBie as spreadsheet/IFC subset, suggest defining required properties explicitly, advise clarifying the EIR. |
| 7 | `en-us-canada-infra-s007` | en | pull rebar from the ifc - bar mark, size, length, count and total weight per pier. need it for the bid | yes | hard | Query IfcReinforcingBar elements, group by mark/diameter and containing pier, sum length and weight, flag missing quantities. |
| 8 | `es-latam-s015` | es | agrúpame los elementos por nivel y tipo para armar paquetes de obra, solo estructura *(EN: Group elements by storey and type for work packages)* | yes | medium | Group structural elements by storey and IFC class/type, export a table suited to scheduling. |
| 9 | `fr-francophone-s009` | fr | sors moi les volumes de béton par niveau pour le chiffrage, murs + dalles + poteaux *(EN: Extract concrete volumes per storey for the quote)* | yes | medium | Sum NetVolume for IfcWall/IfcSlab/IfcColumn with concrete material per storey; flag elements without volume. |
| 10 | `it-italy-s017` | it | volume solai per piano, mi servono per il computo oggi *(EN: Slab volumes per level)* | yes | medium | Sum slab volume per storey from Qto or computed geometry; note source. |
| 11 | `ja-japan-s008` | ja | 天井内のダクトと梁の干渉探して、BCFにして出して。クリアランス50mmで *(EN: Find clashes between ducts and beams in the ceiling zone and create BCF issues)* | yes | hard | Run clash with 50 mm tolerance between IfcDuctSegment and IfcBeam, produce BCF topics with viewpoints and GUIDs. |
| 12 | `ko-korea-s006` | ko | 층별 콘크리트 물량 m3로 정리해줘 슬래브 벽 기둥 따로 *(EN: Concrete volume per floor)* | yes | medium | Sum NetVolume/GrossVolume by storey and class, flag elements without quantities. |
| 13 | `no-norway-s015` | no | sett IsProcured = true på alle prefab betongelementer og lagre ny ifc *(EN: Add procurement status to selected elements)* | yes | medium | Select precast elements, add/modify property in a custom Pset, save a new file preserving original. |
| 14 | `pt-brazil-s010` | pt-BR | me mostra as propriedades do pilar P12: seção, fck e em qual pavimento tá *(EN: Show properties of the selected pillar: fck, section and storey)* | yes | easy | Find element by name, return psets, container storey. |
| 15 | `en-s003` | en | which elements on level 3 arent linked to any task in the work schedule? need the list before tomorrows 4D review | yes | medium | Query IfcTask assignments (IfcRelAssignsToProcess/Product), find level 3 products with none, return grouped list by class and name. |
| 16 | `en-s005` | en | architect sent a 480mb ifc, site tablet chokes on it. whats the quickest way to get just the structure + level 2 to view on site | no | easy | Suggest splitting/filtering by class and storey, removing unused geometry/psets, or converting to a lighter format; offer to export a subset if a file is loaded. |
| 17 | `pt-s010` | pt | quais elementos do pavimento 2 ainda nao tem atividade no cronograma? preciso pro 4D da obra *(EN: Link elements to the schedule and list which have no activity.)* | yes | medium | Find level 2 products with no task assignment, list by class. |
| 18 | `ko-s014` | ko | 공정표랑 연결 안 된 부재 층별로 뽑아줘. 4D 시뮬 돌리기 전에 확인해야돼 *(EN: Check which elements are not linked to the schedule.)* | yes | medium | List elements without task links per storey. |
| 19 | `en-s017` | en | make a work schedule with a task per level (foundation, L1..L5 structure), 5 days each, and link all columns slabs and beams on that level | yes | hard | Create IfcWorkSchedule and IfcTasks with durations, assign elements by storey and class, report counts. |
| 20 | `ja-data-s014` | ja | 大梁を階ごとに一覧にして、断面とスパンと材料も出して。施工前検討会で使いたい *(EN: List main beams by level with section and span for pre-construction review)* | yes | medium | List IfcBeam by level with profile, length/span and material, output table, state missing values. |
| 21 | `pt-guid-s010` | pt | o que mudou da revisao anterior pra essa? preciso saber quais elementos ja estao no cronograma 4D e foram alterados *(EN: Which elements changed since the last revision and are linked to the 4D schedule)* | yes | hard | Diff two revisions by GlobalId, intersect changed elements with those assigned to schedule tasks, and report them. |
| 22 | `mx-mcl-s017` | es | dame el volumen por material de todos los muros, por capa, para el presupuesto *(EN: Quantities by material layer)* | yes | medium | Aggregate layer thickness x area by material per wall; report totals. |
| 23 | `zh-revit-export-s006` | zh | 机电和土建ifc我要导BIM5D，先帮我按楼层统计下各类构件数量，看有没有楼层对不上的 *(EN: Count elements per storey before importing to BIM5D)* | yes | medium | Group elements by storey, report counts and areas/volumes from Qto, flag elements with no storey. |
| 24 | `en-blogs-linkedin-s012` | en | need this as ifc2x3 for the contractors site app, whats going to break | yes | hard | Explain conversion, warn about loss (alignment, classes, properties), run if supported and report differences. |
| 25 | `en-struct-s005` | en | tekla precast ifc w/ rebar kills my web viewer. can u make a lighter copy without IfcReinforcingBar? | yes | medium | Explain size cause, offer filtered copy removing IfcReinforcingBar/fasteners, report size reduction and what was removed. |
| 26 | `pt-viewconv-s008` | pt | exporta pra excel a lista de ambientes com area e nivel, to precisando pra planilha da obra *(EN: Export room list with areas to Excel)* | yes | easy | Query IfcSpace with area and storey, write xlsx. |
| 27 | `en-s001` | en | need concrete wall volume per level for the pour sheet. NetVolume from Qto_WallBaseQuantities, and list any walls that dont have it | yes | medium | Filter IfcWall by concrete material, group by storey, sum NetVolume, list walls lacking Qto_WallBaseQuantities or NetVolume, state which volume (net/gross) was used. |
| 28 | `en-tekla-s010` | en | put elements into storeys based on the Phase property, all in one site/building now | yes | hard | Create or reuse IfcBuildingStorey and reassign contained elements by property value; confirm before writing. |
| 29 | `new-contractor-s001` | ru | завтра заливаем плиту на 3 этаже. дай объём бетона по плитам 3-го этажа, раздельно по захваткам если они есть в модели, и скажи откуда цифры (Qto или с геометрии) *(EN: Tomorrow we pour the level 3 slab. Give the concrete volume of the level 3 slabs, split by pour sections if the model has them, and say where the numbers come from.)* | yes | medium | Filter slabs on level 3; report NetVolume from the quantity set where present and flag slabs without it; say honestly whether any pour-section grouping exists (zones, properties) instead of inventing one; state units (m3). *(new synthetic written for this page; inspired by en-s001, it-italy-s017)* |
| 30 | `new-contractor-s002` | ru | этот ифс весит 500 мб, на планшете на объекте не открывается. как быстро получить лёгкую копию только каркас и 2 этаж, чтобы потом смотреть свойства? *(EN: This IFC is 500 MB and does not open on the site tablet. How can I quickly get a light copy of just the frame and level 2 to view properties?)* | yes | hard | Offer a subset by level and class, keep GlobalIds and properties, save as a new file and report the new size; do not delete from the original; warn that dropped classes (furniture, MEP) are gone from the copy. *(new synthetic written for this page; inspired by en-s005, ja-japan-r013)* |
| 31 | `new-contractor-s003` | ru | какие элементы 2 этажа ещё не привязаны ни к одной задаче в графике? нужен список до планёрки *(EN: Which level 2 elements are not yet linked to any task in the schedule? I need the list before the planning meeting.)* | yes | medium | Check whether a work schedule exists at all; list level 2 elements without a task assignment, grouped by class; if there is no schedule say so instead of returning every element. *(new synthetic written for this page; inspired by en-s003, pt-s010, ko-s014)* |
| 32 | `new-contractor-s004` | ru | сколько у нас дверей и окон по типам и этажам? для заказа у поставщика, с размерами ширина-высота *(EN: How many doors and windows by type and level? For the supplier order, with width and height.)* | yes | easy | Count doors and windows by type and level, read width/height from type or instance properties and say which; flag items with missing dimensions. *(new synthetic written for this page; inspired by pt-qto-s014, fr-francophone-s009)* |
| 33 | `new-contractor-s005` | ru | что поменялось в ифс с прошлой недели? интересует только то, что уже в работе: колонны и плиты 1-2 этажей *(EN: What changed in the IFC since last week? I care only about what is already under construction: columns and slabs on levels 1-2.)* | yes | hard | Compare two files by GlobalId, restricted to the stated classes and levels; list added, removed, moved/resized; say that exporters may regenerate GUIDs and mark the uncertainty. *(new synthetic written for this page; inspired by pt-guid-s010, no-norway-s009)* |
| 34 | `new-contractor-s006` | ru | расставь всем сборным ж/б элементам IsProcured = true и сохрани как новый файл, оригинал не трогай *(EN: Set IsProcured = true on all precast concrete elements and save as a new file, do not touch the original.)* | yes | medium | Identify precast elements (state the rule used), confirm scope and count before writing, add the property in a clear property set, save under a new name, report how many elements changed. *(new synthetic written for this page; inspired by no-norway-s015, no-norway-r012)* |
| 35 | `new-contractor-s007` | en | foreman needs a list for tomorrow: all beams on level 4 with section size and length, grouped by size so I can order cuts | yes | medium | List beams on level 4 grouped by profile, with length per beam and totals; flag beams without profile or length; state units. *(new synthetic written for this page; inspired by ja-data-s014, ja-japan-s012)* |
| 36 | `new-contractor-s008` | en | client says deliver 'as-built IFC' - what do I need to update in the model after site changes, and what in the file would show it's as-built? | no | hard | Explain in plain words that IFC itself has no 'as-built' switch, discuss updating properties/status and revision data, and ask for the client's requirements document; do not invent a mandatory field. *(new synthetic written for this page; inspired by zh-lightweight-review-r025, en-uk-anz-india-s013)* |

## How to role-play this persona in tests

**Voice.** Direct, deadline-driven, impatient with software. Shorter than an engineer's message and more about *what I need to do tomorrow* than about the file. Phrases like "before the meeting", "for the pour sheet", "для заказа", "para o orçamento", "施工前検討会で使いたい" (`ja-data-s014`). Often speaks in lists of levels and trades. Abbreviations and no punctuation are normal ("lvl 3", "mm", "pls"). English example: *"architect sent a 480mb ifc, site tablet chokes on it. whats the quickest way to get just the structure + level 2 to view on site"* (`en-s005`); Portuguese: *"o que mudou da revisao anterior pra essa? preciso saber quais elementos ja estao no cronograma 4D"* (`pt-guid-s010`); Korean: *"공정표랑 연결 안 된 부재 층별로 뽑아줘"* (`ko-s014`).

**Typical context.** A model received from someone else (architect, structural engineer, subcontractor), not their own; a schedule in Primavera P6 / MS Project / Excel; a specific deadline (pour, order, planning meeting, tender). Rarely states IFC version or exporter. Often has no BIM software installed. `needs_file = true` for most prompts, but "what do I deliver?" questions need no file.

**Knowledge level.**
- Strong: construction sequence, trades, quantities for ordering, practical constraints on site.
- Medium: reading drawings and schedules; has used a free viewer.
- Weak: IFC concepts (class, property set, relationship), the idea that links to tasks must be created, the difference between the design model and a construction model, quantity sources (Qto vs geometry).
- Believes: "the model should already have everything; if the animation is empty, the file is broken."
- Low tolerance for technical explanations; wants an action and a number.

**What to test with this persona.**
- Honest absence: no work schedule in the file; elements without a level; empty quantity sets. The assistant must say so and not fabricate a schedule or volumes.
- Safe edit: writes only on explicit request, to a new file, with a count of what changed.
- Units and source of every quantity.
- Practical simplification: when the file is too heavy, offers a subset (levels, classes) rather than a lecture on IFC.
- Language: the same answer should come out in ru, pt, ko, ja, es, it when asked in those languages.

**Typical follow-ups.**
1. "А можно только 3 этаж?" / "only level 3 please"
2. "Put that in Excel / CSV so I can send to the supplier."
3. "Which of those are already in the schedule?"
4. "Why is this number different from the architect's?" (gross vs net)
5. "Can I open it on my phone?"
6. "What do I actually have to deliver?" (expects a request for the client's requirement document, not a guess)

**Quick judge checklist.**
- Does the answer tell the user *what is not in the file* (schedule, quantities, level links) in plain words?
- Is each number labelled with its unit and where it came from?
- Is any change written to a copy, never the original?
- Is the answer short enough for a person standing on a site?
- Does it avoid claiming a particular 4D tool's behaviour that it was not shown?
