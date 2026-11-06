# Owner / client: who they are and what they do with IFC

**Last built: 2026-11-06 · Persona code:** `owner_client` · **Data behind this page:** 52 records (28 real, 24 synthetic; `python tools/kb.py stats --persona owner_client`). Languages: en 32, it 3, ko 3, zh 3, de 2, es 2, ja 2, no 2, fr 1, pt-BR 1, ru 1. **This is the thinnest persona in the base**: owners almost never post on BIM forums, so most "real" records are official pages and a few cross-posted voices. Treat the profile below as evidence-based where it cites a record and as informed inference where it does not (both are labelled).

## In plain words

The owner (or client, "employer", "appointing party", Bauherr, maître d'ouvrage, 発注者, заказчик) is the person or organization that orders and pays for the building: a developer, a ministry, a municipal road agency, a hospital trust, sometimes a homeowner. The owner does not model anything. The owner **buys a model along with the building** and wants to be sure it contains what the contract promised, so the building can later be operated and maintained without re-surveying everything.

Think of buying a house and receiving, with the keys, a binder that is supposed to list every boiler, window and fire door with serial numbers and warranty dates. The owner's questions are: *Is the binder complete? Can I check it myself without hiring a specialist? Can I send a clear "not accepted, fix these items" list back?*

IFC matters to owners because it is an open format: the contract can demand it, nobody is locked into one vendor, and a checker can read it. The tools owners hear about are **EIR** (the written requirements), **IDS** (the same requirements in a machine-checkable file), **COBie** (a spreadsheet for handover data), and national rulebooks that sometimes make BIM mandatory for public projects.

## Daily IFC tasks

(Which of these are observed and which inferred is marked in the last column.)

| # | Task | What it looks like in practice | Evidence |
|---|---|---|---|
| 1 | Write the requirements | An EIR (AIA, capitolato informativo, cahier des charges BIM, ТЗ) naming IFC version, view, properties, classification, naming; increasingly an IDS file. | Observed: [it-italy-r006](https://biblus.acca.it/capitolato-informativo-come-redigerlo-con-la-metodologia-bim/), [de-dach-r027](https://www.bimdeutschland.de/bim-deutschland/faq), [en-fmor-r005](https://community.osarch.org/discussion/2678/view-ids-xml-file-as-simplified-text-human-friendly-readable-ids) |
| 2 | Accept or reject a delivery | Run the checks, get a short pass/fail list, send it back to the contractor. | Observed in synthetic `en-fmor-s003`: "run our IDS on the contractor model and give me a short fail list I can send back, grouped by discipline" |
| 3 | Check headline numbers | Total floor area, number of storeys, doors per type, equipment counts, against the brief or the invoice. | Observed: `en-fmor-s009`, `en-us-canada-infra-s015` (synthetic) |
| 4 | Collect handover data for operations | COBie or an equipment/room list with manufacturer, serial, warranty. See [Facility manager](facility_manager.md). | Observed: [en-cobie-r021](https://community.osarch.org/discussion/3568/massing-ifc-native-platform-from-feasibility-through-turnover-built-on-ifcopenshell-that-open), [en-cobie-r024](https://community.osarch.org/discussion/comment/12333) |
| 5 | Run a portfolio | Query assets across hundreds of as-built models (e.g. bridges with a given bearing and age). | Observed: [en-cobie-r008](https://community.osarch.org/discussion/comment/25545) |
| 6 | Follow public-procurement rules | Check whether BIM and IFC are mandatory for a given tender size and country. | Observed: [it-italy-r004 (reviewer list)](https://biblus.acca.it/nuovo-codice-appalti-il-bim-e-obbligatorio/), [it-italy-r021](https://biblus.acca.it/notizie/c-e-l-obbligo-di-appalto-bim-anche-per-completare-un-opera-incompiuta/), [en-mea-r001](https://www.cidb.org.za/innovation/cidb-bim-adoption-strategy/) |
| 7 | Prepare for authority submission | Owner is the legal applicant in many systems; the model must pass the portal's checker. | Observed: [zh-tw-hk-r003](https://www.devb.gov.hk/filemanager/tc/content_2373/BIM-Book-content-cn.pdf), [ja-japan-r020](https://note.com/legal_tiger6680/n/n6781ba815061) |
| 8 | Decide on tools and lock-in | Which free or low-cost tools can read the deliverable; whether the vendor can hold the data hostage. | Observed: [en-osarch-gis-r017](https://community.osarch.org/discussion/3541/long-term-workflow-blk360-revit-fiverr-ifc4-freecad-bim-ai-assisted-remodeling-is-this-a) |

## Goals

- **Verify without becoming a specialist:** yes/no answers, counts, a list to forward ([en-aimcp-r030](https://github.com/ekkodale/IFC-MCP): the README imagines a glass cleaner asking for the largest window, painters asking for total wall area, an architect asking for counts of chimneys and ramps).
- **Requirements people can read:** a human-friendly view of an IDS instead of XML ([en-fmor-r005](https://community.osarch.org/discussion/2678/view-ids-xml-file-as-simplified-text-human-friendly-readable-ids)).
- **Replace Excel/PDF requirement lists** that make checking a manual job, with something that can be automated ([en-val-r030](https://zenn.dev/miyamiyaumya/articles/6714ef2c6e2c6c), Japanese).
- **Compliance with mandatory schemes** (national BIM mandates, portals) without surprises.
- **Operational data on day one:** equipment, rooms, systems, warranties in a form the FM system accepts.
- **Independence from one vendor** and low licence cost.

## Pains (ranked)

_Quoted phrases in the last column are illustrative: some paraphrase real records, others are taken from the synthetic prompts further down. Only the tables of real records are evidence of what people actually wrote._

Ranked by signal across the 52 records; owner evidence is thin, so the ordering is judgement based on the topic counts (national_requirements 15, cobie_fm_handover 14, contracts_bep_eir_loin 13, ids_requirements 9, permitting_code_checking 6).

| Rank | Pain | Signal | Typical shape |
|---|---|---|---|
| 1 | **No easy way to know whether the delivery is complete** | `validate_check` 8 + synthetic | "did they actually classify everything? how many elements have no classification"; "which equipment has no manufacturer or serial number? need it for handover friday" |
| 2 | **Rulebooks are many, local and changing** | `national_requirements` 15 | "is BIM mandatory for this tender? is IFC required?"; Singapore, Hong Kong (tentatively 2029), Japan (2029 data review), Italy, Peru, Spain, Korea |
| 3 | **Requirements are not machine-readable or not readable by humans** | `contracts_bep_eir_loin` 13, `ids_requirements` 9 | Excel/PDF requirement lists; IDS XML nobody can read; "how will ISO 7817-3 relate to IDS?" |
| 4 | **Handover data shape** | `cobie_fm_handover` 14 | "can IFC carry room areas, doors, windows and fire extinguishers for FM without geometry?"; "are manufacturers stored in a COBie-compliant way?" |
| 5 | **Portfolio-level queries across many files** | gis/asset records | "500+ projects a year", "thousands of project models" |
| 6 | **Heavy, over-detailed deliverables** | [en-fmor-r037](https://forums.buildingsmart.org/t/opinion-about-high-polygon-count-in-ifc/4699) | "opinion about high polygon count in IFC deliverables" |
| 7 | **Confusion between classification and IFC class** | [en-bsi-r032](https://forums.buildingsmart.org/t/how-does-ifc-work-with-existing-classification-systems-such-as-omniclass-uniformat-etc/804) | "model as IfcDoor, classify with OmniClass, or both?" |

## Vocabulary they use (and what they do not know)

### Words and phrases you will see

| Phrase (language) | Plain meaning |
|---|---|
| deliverable, handover, as-built, sign-off, "friday" | The thing to be accepted; the moment of transfer. |
| EIR / AIA (de) / capitolato informativo (it) / cahier des charges BIM (fr) / ТЗ заказчика (ru) / 発注者要求 (ja) / 발주처 지침 (ko) | The written list of what must be delivered. |
| FM, CAFM, CMMS, GMAO (fr), FDV (no), 運維 / 维持管理 (zh/ja) | The operations system that will receive the data. |
| "net m2", NGF, BTA/NTA (no), GFA, 面积 | Area measures the contract pays or is judged on. |
| "which equipment has no ... ?", "pass or fail per item" | The owner's native request form. |
| asset, asset register, "tag" | A piece of equipment with an identity. |
| mandatory / obligatory, "is IFC required?" | Compliance questions. |

### What they typically do not know, or get wrong

- **IFC class names.** They say "equipment", "doors", "rooms"; the assistant must translate to the right classes and mention uncertainty (equipment may be stored as generic proxies).
- **That "complete" is not a property of a file.** A file can pass an IDS and still be wrong in content; an IDS can check a code's pattern but not whether the code fits the element ([nl-dutch-r002](https://github.com/OpenAEC-Foundation/OpenAEC-BIM-validator/issues/22)).
- **The difference between EIR (client) and BEP (supplier).** Easy to confuse; the regulations topic page keeps them apart.
- **That the model may not be the legal reference.** Hong Kong's Buildings Department treats the submitted model as supplementary and drawings prevail ([zh-tw-hk-r002](https://www.bd.gov.hk/tc/resources/online-tools/building-information-modelling/index.html), per the record); Japan's 2026 drawing review treats the IFC as not subject to review ([ja-japan-r016](https://note.com/kensesu_ai/n/nee08ddde31f1)). Owners may assume otherwise.
- **That a spreadsheet export (COBie) is a derivative**, with its own conformity rules (see [Facility manager](facility_manager.md)).

Read next: [IFC in real projects](../../01_ifc_basics/00_ifc_in_real_projects.md), [EIR/BEP clauses with real examples](../../02_standards_regulations/requirements_in_contracts_eir_bep.md), [buildingSMART standards (IDS, bSDD, BCF)](../../02_standards_regulations/buildingsmart_standards.md), country files in [national/](../../02_standards_regulations/national/) (e.g. [Italy/Spain/Portugal](../../02_standards_regulations/national/spain_portugal_italy.md), [Japan/Korea](../../02_standards_regulations/national/japan_korea.md), [Singapore](../../02_standards_regulations/national/singapore.md)), topic pages [regulations, permits, contracts](../by_topic/regulations_permits_contracts.md), [classification, COBie, FM](../by_topic/classification_cobie_fm.md), [validation / IDS](../by_topic/validation_ids_model_checking.md).

## Real questions (36, linked)

Paraphrases of questions or pages seen at the linked sources, kept in the original language. Language mix in this list: Russian 3, English 18, other languages 15. Groups C and D are mostly pages, not questions; read the middle column as "what this reader wants to know". Where a source page is not in English but the stored paraphrase is, the Lang column still shows the page language. Honest limit: apart from group A, **no record is a verified post by an owner**.

### A. The few genuine owner-side voices

A state road agency, a homeowner, a general contractor building a portal for its clients, and a README that lists what non-experts want to ask. Everything else about this persona is inferred from official pages.

| # | Lang | Their words (paraphrase, original language) | English gloss / context | Source (record id, type, year) |
|---|---|---|---|---|
| 1 | en | how many windows, doors, chimneys, or ramps | Business case: glass cleaner asks largest window, workers ask walls above a height, painters ask total wall area, architect asks counts of chimneys and ramps. | [en-aimcp-r030](https://github.com/ekkodale/IFC-MCP) official_doc, 2025 |
| 2 | en | US state DOT with 500+ projects/year wants system-wide asset query (e.g., bridges with certain bearings and their age) from as-built IFC | How to keep IFC organized for asset management and query assets across hundreds of project models? | [en-cobie-r008](https://community.osarch.org/discussion/comment/25545) forum, 2025 |
| 3 | en | How do we manage IFC for asset management when data sits in thousands of project models? Which software do you use? | State DOT person asks how to run system-wide queries across thousands of project IFC models (e.g. bridges with bearings by manufacturer and age). | [en-osarch-gis-r020](https://community.osarch.org/discussion/comment/25545#Comment_25545) forum, 2025 |
| 4 | en | Is it a sound strategy to avoid vendor lock-in? Are imported Revit IFC elements editable in FreeCAD? Which import settings? | Homeowner plans a DIY digital twin: scan, Revit model from Fiverr, IFC4, FreeCAD, AI remodelling; asks if editable and sensible. | [en-osarch-gis-r017](https://community.osarch.org/discussion/3541/long-term-workflow-blk360-revit-fiverr-ifc4-freecad-bim-ai-assisted-remodeling-is-this-a) forum, 2025 |
| 5 | en | configurable GC portal incl. COBie closeout | Presented a platform covering RFIs, pay apps, scheduling and COBie closeout on IFC. | [en-cobie-r021](https://community.osarch.org/discussion/3568/massing-ifc-native-platform-from-feasibility-through-turnover-built-on-ifcopenshell-that-open) forum, 2026 |
| 6 | en | question about COBie-compliant storage of manufacturer data | Are nominated manufacturers and procurement data stored in a COBie-compliant way? | [en-cobie-r024](https://community.osarch.org/discussion/comment/12333) forum, 2022 |

### B. "What do I even demand, and how do I check it?"

Requirements, IDS, classification, and the awkward feeling that the file is too heavy to review.

| # | Lang | Their words (paraphrase, original language) | English gloss / context | Source (record id, type, year) |
|---|---|---|---|---|
| 7 | en | saw a demo showing IDS as readable text and asks how to get the same in Bonsai; no Python experience | How to view an IDS XML as simple human-readable text like in a conference demo | [en-fmor-r005](https://community.osarch.org/discussion/2678/view-ids-xml-file-as-simplified-text-human-friendly-readable-ids) forum, 2025 |
| 8 | en | General discussion of IDS as a way for clients to specify delivery requirements. (title/snippet only) | General discussion of IDS as a way for clients to specify delivery requirements. | [en-fmor-r010](https://community.osarch.org/discussion/647/ids-information-delivery-specification) forum, 2023 |
| 9 | en | Asks how to create IDS files with open-source tooling. (title/snippet only) | Asks how to create IDS files with open-source tooling. | [en-fmor-r018](https://community.osarch.org/discussion/2723/creation-ids-information-delivery-specification-with-open-source-tool) forum, 2025 |
| 10 | en | Clarification on actor assignment for owner/organisation roles (title only) | Clarification on actor assignment for owner/organisation roles | [en-fmor-r035](https://forums.buildingsmart.org/t/actor-assignment-clarifications-on-specification-and-usage/6305) forum, 2026 |
| 11 | en | how will the upcoming ISO 7817-3 level-of-information-need schema relate to IDS? |  | [en-bsforum-r023](https://forums.buildingsmart.org/t/5533) forum, 2024 |
| 12 | ja | IDS as client weapon to replace Excel/PDF requirements, auto-check IFC | What IDS can do for the client: automate checking of IFC against requirements, limits | [en-val-r030](https://zenn.dev/miyamiyaumya/articles/6714ef2c6e2c6c) blog, 2023 |
| 13 | it | devo scrivere il capitolato informativo per una gara, cosa metto su formati e livelli di dettaglio? | How to write a capitolato informativo (EIR) with open data formats and ISO 19650 CDE. | [it-italy-r006](https://biblus.acca.it/capitolato-informativo-come-redigerlo-con-la-metodologia-bim/) vendor_kb, 2026 |
| 14 | en | model as IfcDoor, classify with OmniClass, or both? will growing IFC entity vocabulary make OmniClass obsolete | Should assets be IFC elements, OmniClass-classified, or both? Will IFC entities make classifications obsolete? | [en-bsi-r032](https://forums.buildingsmart.org/t/how-does-ifc-work-with-existing-classification-systems-such-as-omniclass-uniformat-etc/804) forum, 2018 |
| 15 | en | Opinion about high polygon counts in IFC deliverables (title only) | Opinion about high polygon counts in IFC deliverables | [en-fmor-r037](https://forums.buildingsmart.org/t/opinion-about-high-polygon-count-in-ifc/4699) forum, 2026 |
| 16 | en | Autodesk asks users how Revit should better support IFC workflows. | Revit team survey on IFC support: do you need IFC workflows in Revit? | [en-roundtrip-r019](https://forums.buildingsmart.org/t/next-steps-for-ifc-support-in-revit/3580) forum, 2021 |

### C. National and public-client rulebooks an owner must obey or may adopt

These are official or semi-official pages, not questions. The "question" column says what the reader of the page wants to know, written the way a client would ask it.

| # | Lang | Their words (paraphrase, original language) | English gloss / context | Source (record id, type, year) |
|---|---|---|---|---|
| 17 | de | BIM-Portal requirements are recommendations; agree per project; REST API for AIA contents. | FAQ: are BIM-Portal requirements binding nationwide? Which formats do machine-readable AIA use (ifcXML)? | [de-dach-r027](https://www.bimdeutschland.de/bim-deutschland/faq) official_doc, 2025 |
| 18 | en | What does South Africa's national BIM strategy require, and does it name IFC or any standard? | South Africa's construction regulator publishes a 2025-2030 national BIM adoption strategy; 2026 phase is governance and standards, with no mention of IFC or openBIM. | [en-mea-r001](https://www.cidb.org.za/innovation/cidb-bim-adoption-strategy/) official_doc, 2026 |
| 19 | es | fichas por modelo con entidades IFC requeridas: arquitectura, volumétrico, sitio, MEP eléctrico | Chile's Planbim IFC entity sheets per model (architecture, volumetric, site, MEP electrical) | [es-latam-r011](https://planbim.cl/documentos/fichas-ifc/) official_doc, 2022 |
| 20 | es | documento BIM del Ministerio de Vivienda sobre licencias | MinVivienda Colombia BIM document series (e.g. licenses) published on the BIM portal | [es-latam-r020](https://bim.minvivienda.gov.co/sites/default/files/doc-bim-2022-09/10_licencias_.pdf) official_doc, 2022 |
| 21 | it | per completare un'opera incompiuta serve il BIM? | Is BIM mandatory to complete an unfinished work? | [it-italy-r021](https://biblus.acca.it/notizie/c-e-l-obbligo-di-appalto-bim-anche-per-completare-un-opera-incompiuta/) blog, 2025 |
| 22 | ja | 個人開発のBIMCraft(MCP/CLI操作可)は審査用IFCに使えるか。RVTは読み取りのみ、カーテンウォールや階段は未対応 | Can the free Rust BIM app BIMCraft handle the 2029 review IFC? Reads IFC2x3/IFC4, writes IFC4 | [ja-japan-r020](https://note.com/legal_tiger6680/n/n6781ba815061) blog, 2026 |
| 23 | ko | 조달청 시설사업 BIM 적용 기본지침서 | PPS (Public Procurement Service) facility project BIM application guideline v2.0 | [ko-korea-r004](https://www.buildingsmart.or.kr/Data/Main/시설사업%20BIM%20적용%20기본지침서%20v2.0-S.pdf) regulation, 2020 |
| 24 | no | hvilken MMI-kode skal objektene ha i modellen ved hver milepæl? | MMI-veilederen 2.0: model maturity index harmonised for building and infrastructure by Statsbygg, Nye Veier, Bane NOR, Statens vegvesen | [no-norway-r007](https://www.mmi-veilederen.no/) official_doc, 2026 |
| 25 | en | Portal describing IFC+SG onboarding checklist, data structure and mapping requirements, authoring guidance, glossary of identified components, readiness self-check and Model Checker; agencies BCA, LTA, NEA, NParks, PUB, SCDF, URA. | Official Singapore CORENET X portal: IFC+SG start guide, data structure and Excel mapping file, model checker, readiness self-check, seven regulatory agencies. | [en-permit-r002](https://info.corenet.gov.sg/general/corenet-x.aspx) official_doc, 2024 |
| 26 | zh | 广州开始BIM审图试点，要做什么 | Guangzhou MoHURD announcement: BIM drawing review trial. | [zh-lightweight-review-r022](https://zhuanlan.zhihu.com/p/157220418) blog, 2020 |
| 27 | zh | 竣工模型交付用什么格式，要在施工图模型基础上加变更信息吗 | Nanjing local standard for as-built (completion) BIM delivery; format preferably 宁建模. | [zh-lightweight-review-r025](https://amr.nanjing.gov.cn/ztzl/bzhzl/tzgg/202302/P020230216538033075572.pdf) regulation, 2023 |
| 28 | zh | 政府2023年12月公布全面採用BIM擬備及審批建築圖則路線圖，暫定2029年強制呈交 | HK roadmap for adopting BIM in building plan preparation and submission; mandatory BIM submission tentatively 2029. | [zh-tw-hk-r003](https://www.devb.gov.hk/filemanager/tc/content_2373/BIM-Book-content-cn.pdf) regulation, 2023 |

### D. Adjacent: tagged as other personas in the research, but it is the client's job

Client-side requirement writing and rule reading, labelled `bim_manager`, `bim_coordinator` or `reviewer_authority` in the raw files.

| # | Lang | Their words (paraphrase, original language) | English gloss / context | Source (record id, type, year) |
|---|---|---|---|---|
| 29 | en | one bridge exported three ways: 161 proxies, random GlobalIds, no quantities, national-grid mm coordinates making viewers jitter. How to tell a good file from a bad one? | Same bridge exported three ways gives three very different IFC files; which one will the client send back? | [en-blogs-linkedin-r001](https://bimcorner.com/same-bridge-three-ifc-files/) blog, 2026 |
| 30 | en | EIRs often name the property but not the Pset, e.g. UK BIM Framework template; IDS property facet needs both | UK BIM Framework EIR templates name the property (e.g. GrossFloorArea) but not the property set; IDS requires a Pset | [en-uk-anz-india-r013](https://github.com/buildingSMART/IDS/issues/189) github_issue, 2023 |
| 31 | no | hva er POFIN og kan vi bruke det til å stille krav til informasjonsleveranser? | What is POFIN and can I use it to set openBIM requirements in a contract? | [no-norway-r002](https://www.buildingsmart.no/pofin.html) official_doc, 2025 |
| 32 | es | tabla que asocia parámetro con atributo IFC, Pset y propiedad, requerido u opcional, exportación automática o 'a ingresar' | Planbim information matrix v3.0 maps each parameter to IFC attribute, Pset, property, required/optional, auto/manual export, COBie | [es-latam-r012](https://planbim.cl/documentos/mide/) official_doc, 2022 |
| 33 | it | cosa dicono le linee guida MIT 2026 su ACDat, ruoli e formato IFC? il modello prevale sul 2D? | What do the 2026 MIT guidelines on digital information management (GID) require: roles, ACDat, formats, model prevailing over 2D? | [it-italy-r010](https://biblus.acca.it/linee-guida-bim-2026-per-le-stazioni-appaltanti/) regulation, 2026 |
| 34 | ru | новые BIM-требования в формате IDS | Mosoblexpertiza published new BIM requirements in IDS format for roads, utilities and buildings | [ru-autodesk-telegram-r025](https://t.me/s/ifc_ru) social, 2026 |
| 35 | ru | формат IFC 2x3 и выше для обмена моделями | SP 333 recommends exchanging digital models in IFC 2x3 or higher and requires elements to be classified and uniquely identified | [ru-autodesk-telegram-r036](http://docs.cntd.ru/document/556793897) regulation, 2017 |
| 36 | ru | в проекте СП модель предъявляется в RVT и DWG, а IFC нет; элементы должны быть классифицированы | Draft national BIM standard recognizes RVT and DWG as model formats, not IFC? | [ru-dwg-other-r025](https://forum.dwg.ru/showthread.php?t=134394&page=33) forum, 2016 |

## Ready test prompts (36, synthetic)

**All prompts below are SYNTHETIC.** Ids that start `new-owner-` were written for this page (not in `research_raw/`), each inspired by the record named in its tag; the other ids come from the research files. They assume a loaded IFC unless "no file" is shown.

### 1. A quick picture of what I received

Owners ask in everyday words and rarely name an IFC class.

| # / id | Lang | Prompt (SYNTHETIC) | Meaning (EN) | Difficulty | A good answer should |
|---|---|---|---|---|---|
| S1 `en-beginner-qa-s002` | en | how many levels does this have and at what heights | List storeys with elevations | easy, file | List IfcBuildingStorey names and elevations in project units. |
| S2 `en-beginner-qa-s016` | en | does this file have real data like materials and costs or is it just a 3d shape | Does it contain data or just 3D | easy, file | Check for property sets, materials, classifications, cost items versus geometry-only elements. |
| S3 `en-gh-thatopen-s007` | en | file is like 1.3 GB, dont crash, just give me storeys, element counts per class and total size | Give a quick overview of a huge IFC file without loading all geometry | hard, file | Use streaming/line-based parsing, avoid geometry, return storeys and counts per IFC class. |
| S4 `it-italy-s013` | it | riassumimi il modello: discipline, n. elementi per classe, livelli, per il verbale di consegna | Summarize model for BIM obligation deliverable | medium, file | Produce model inventory by class, storey, discipline, schema version. |
| S5 `en-gis-s006` | en | for the city model I only need footprint area, total height and number of storeys of this building, can you pull that | Summarize footprint, height and storeys for a city model. | medium, file | Compute footprint from ground slab or base storey geometry, height from bounding box, count IfcBuildingStorey, state assumptions. |
| S6 `new-owner-n01` (new, inspired by en-beginner-qa-s016) | en | im not technical. is this model just a 3d picture or does it have real data in it, like what each wall is made of and what the doors are? | Does the model carry data or only shapes | easy, file | Summarize in plain words: counts of main element classes, how many have materials/property sets/classification, a few examples; say clearly what is and is not there; no jargon without a gloss. |
| S7 `new-owner-n09` (new, inspired by it-italy-s013) | ja | 発注者としてIFCを受け取りました。中身が空っぽでないか、階数・室数・設備の数だけざっくり教えてください | As the client, give a rough summary: number of storeys, rooms, equipment | easy, file | Report storey count with names, IfcSpace count, count of main equipment classes, schema version and authoring software; plain wording. |

### 2. Did they deliver what the contract says?

Pass/fail per requirement, a list that can be sent back. The assistant should not issue a legal verdict.

| # / id | Lang | Prompt (SYNTHETIC) | Meaning (EN) | Difficulty | A good answer should |
|---|---|---|---|---|---|
| S8 `en-mea-s013` | en | can you test this model against our EIR? we need manufacturer, model and warranty on all mechanical equipment. tell me pass or fail per item | Test a contractor model against the employer's information requirements. | hard, file | Check IfcFlowTerminal/IfcFlowController etc. for Manufacturer, ModelLabel, warranty properties, return pass/fail per element with summary; propose IDS if repeated. |
| S9 `en-fmor-s003` | en | run our IDS on the contractor model and give me a short fail list I can send back, grouped by discipline | Check the delivered model against our IDS and summarize failures for the contractor | medium, file | Validate model against provided IDS, summarize failed specs with counts and example GUIDs, group by discipline/class, concise report. |
| S10 `en-fmor-s006` | en | did they actually classify everything? how many elements have no classification | Are classification codes present on all elements per client requirement | easy, file | Count elements without IfcClassificationReference, break down by class, report system used, give coverage percent. |
| S11 `en-fmor-s015` | ru | глянь в модели у всего оборудования есть атрибуты по ТЗ заказчика? нужен список чего нет | Check whether equipment has all attributes required by the employer brief | medium, file | Check equipment elements for required attributes, report missing per class, produce list. |
| S12 `en-vm-s016` | en | EIR says IFC2x3 CV2.0. contractor sent this. compliant? just yes/no plus reasons | Is this deliverable compliant with the schema in the EIR | easy, file | Read schema and ViewDefinition, compare with EIR, answer with reasons. |
| S13 `ko-korea-s003` | ko | 발주처 BIM 지침 기준으로 층/공간/부재 분류 누락된 거 있나 체크해줘 | Check against Korean delivery requirements | hard, file | Check IfcBuildingStorey/IfcSpace presence and classification on elements; report gaps; state which guideline assumptions were used. |
| S14 `no-norway-s006` | no | har alle tekniske komponenter FDV-info og NS 3451-kode? vil ha liste over de som mangler | Do all technical equipment items have FDV data and a TFM/NS 3451 code? | medium, file | Check equipment for classification reference and maintenance properties, list gaps. |
| S15 `en-gh-xbim-others-s016` | en | before sending remove all psets except the ones in our EIR list, keep a backup | Strip properties not required by the EIR before sharing | hard, file | Create a filtered copy removing non-listed property sets, confirm counts, preserve original. |
| S16 `new-owner-n10` (new, inspired by en-vm-s016) | en | contract says IFC4 and the city wants georeferencing. is the file they sent actually IFC4, and is it georeferenced? yes/no and why | Schema and georeferencing check against the contract | medium, file | Read the header schema (IFC2X3/IFC4/IFC4X3) and view definition; check IfcMapConversion/IfcProjectedCRS and site lat/long; answer yes/no per item with evidence. |
| S17 `new-owner-n02` (new, inspired by en-fmor-s003) | ru | подрядчик сдал модель. есть там лифты и тех. помещения или это просто коробки? просто скажи да/нет и сколько | Do the lifts and plant rooms exist as real objects in the delivered model | medium, file | Search for IfcTransportElement (lifts) and spaces named or typed as plant/technical rooms; report counts and examples; say if lifts are modelled as proxies or generic shapes. |
| S18 `new-owner-n04` (new, inspired by zh-lightweight-review-r025) | zh | 甲方要求每个房间都要有面积和功能，帮我看看设计院交的模型有没有漏的 | Owner requires area and function on every room; check the designer's model | medium, file | List IfcSpace without area (net/gross) or without usage/long name; counts per storey; list of GlobalIds/names. |

### 3. Numbers against the brief or the invoice



| # / id | Lang | Prompt (SYNTHETIC) | Meaning (EN) | Difficulty | A good answer should |
|---|---|---|---|---|---|
| S19 `en-fmor-s009` | en | Could you give me total gross floor area per level so I can check it against the brief? | Floor area per storey for checking against the brief | medium, file | Sum IfcSlab/IfcSpace areas per storey using Qto, clarify GFA vs NFA, flag missing quantities. |
| S20 `en-us-canada-infra-s015` | en | list every piece of mechanical equipment by system with manufacturer, model, serial. what is blank | List equipment by system for FM import | medium, file | Collect equipment with system assignment and manufacturer pset values and list gaps. |
| S21 `en-fmor-s001` | en | which equipment in this model has no manufacturer or serial number? need it for handover friday | Which asset types lack manufacturer/model/serial for FM handover | medium, file | List IfcElement occurrences of equipment classes missing Pset_ManufacturerTypeInformation Manufacturer/ModelLabel and serial number; group by type and storey; output table. |
| S22 `en-fmor-s017` | fr | combien de portes et fenetres par type? cest pour le contrat de maintenance | Count doors and windows by type for the maintenance contract | easy, file | Count IfcDoor/IfcWindow by type, group by storey, output table. |
| S23 `en-model-checking-s015` | en | can u check door clear widths and corridor widths vs accessibility rules | Accessibility | hard, file | Compute door clear widths and corridor widths where possible, compare to a given threshold, note limits. |
| S24 `new-owner-n03` (new, inspired by en-fmor-s009) | de | Wie viele Wohneinheiten stecken im Modell, und passt das zu den 48 aus dem Vertrag? | Count dwelling units and compare with the contract's 48 | hard, file | Look for IfcZone/IfcSpace groupings or properties indicating dwelling units; state how the count was derived and its uncertainty; do not just output 48. |
| S25 `new-owner-n06` (new, inspired by en-us-canada-infra-s015) | en | the invoice says 12 air handling units were installed. how many are in the as-built model? | Cross-check an invoice quantity against the model | medium, file | Count IfcUnitaryEquipment / air terminal units / by predefined type or name; show the list with tags and locations; explain classification ambiguity (could be proxies). |
| S26 `new-owner-n07` (new, inspired by en-fmor-s009) | en | we pay per net m2. does the total net floor area in the model match the 4,820 m2 in the contract? just tell me the difference | Compare net floor area with a contract figure | medium, file | Sum net floor area from Qto_SpaceBaseQuantities or computed geometry of IfcSpace; state which source and which spaces were included; report the difference and caveats (gross vs net, external spaces). |
| S27 `new-owner-n05` (new, inspired by it-italy-s013) | es | el contratista dice que entregó todo en IFC. ¿me dices cuántos elementos hay por disciplina y si falta alguna? | Contractor says all is delivered; counts per discipline, any missing | medium, file | Summarize per-file or per-discipline element counts by class; flag expected disciplines with no or very few elements; avoid claiming completeness. |
| S28 `new-owner-n08` (new, inspired by en-fmor-s017) | fr | dans la maquette livrée, quels équipements n'ont pas de date de fin de garantie ? j'en ai besoin pour le contrat de maintenance | Equipment lacking a warranty end date, for the maintenance contract | medium, file | List equipment elements whose Pset_Warranty (or custom equivalent) has no end date; group by type and storey; say if the property is absent from the whole file. |
| S29 `new-owner-n11` (new, inspired by en-fmor-s003) | ru | у всех помещений в модели от проектировщика есть площадь и назначение? выдай список тех, у кого нет, скину ему на доработку | Rooms missing area or purpose; list to send back to the designer | easy, file | List IfcSpace without area (Qto or property) or without usage/name; counts per storey; GlobalId, number, name; offer to group by storey for forwarding. |
| S30 `new-owner-n12` (new, inspired by en-fmor-s009) | ru | сложи площади помещений по этажам и сравни с ТЭП из задания, там 12 450 м2 общая. расхождение больше 1% - пометь | Sum room areas per storey and compare with the brief's 12,450 m2 | hard, file | Sum areas per storey from IfcSpace (state source: Qto vs geometry), give total and per-storey table, compute the difference against 12,450 and flag above 1 percent; note gross/net ambiguity. |

### 4. Handover, FM and requirement-writing questions



| # / id | Lang | Prompt (SYNTHETIC) | Meaning (EN) | Difficulty | A good answer should |
|---|---|---|---|---|---|
| S31 `en-fmor-s011` | en | do we still need cobie or is ifc + ids enough for our FM system handover | Do we need COBie or just IFC with IDS for handover to FM | medium, no file | Explain COBie vs IFC property delivery with IDS, tradeoffs, suggest defining requirements and spreadsheet export for CAFM. |
| S32 `de-cobie-s010` | de | was muss ich in die AIA schreiben damit wir vom Bauherrn ne brauchbare IFC für den Betrieb kriegen? COBie oder was anderes | What should we require in the AIA for FM handover from IFC? | medium, file | Explain COBie vs FM-handover MVD, list asset attributes, suggest IDS-based requirements. |
| S33 `en-cobie-s004` | en | need a room list for the CAFM: space number, name, floor, net area, one row each | Room list with area and floor for CAFM import. | easy, file | Export IfcSpace with Number, Name, storey, NetFloorArea (Qto_SpaceBaseQuantities) as CSV/table; flag missing values. |
| S34 `ko-cobie-s015` | ko | 시설관리 시스템에 엑셀 올리면 오류 나는데 어느 행이 문제인지 찾아줘, 자산코드 중복인가? | CAFM import fails with the exported spreadsheet; find which rows break it. | medium, file | Check duplicates and blank mandatory fields in exported asset table; list offending rows. |
| S35 `en-fmor-s019` | en | are the same properties repeated in multiple psets on the walls? show them | Find duplicated properties across several psets | hard, file | Detect same property names in multiple psets per element, group results, report examples. |
| S36 `pt-brazil-s015` | pt-BR | abro o ifc no visualizador e tá tudo cinza, cadê as cores e materiais? | IFC opens without colors/materials in viewer | medium, no file | Check presence of IfcStyledItem/surface style in the model and report; explain viewer limits. |

## How to role-play this persona in tests

**Voice.** Plain business language, no IFC vocabulary. Short, impatient, often with a date ("handover friday", "tomorrow", "завтра") and a requested output form ("yes/no plus reasons", "a short fail list I can send back", "tell me pass or fail per item", "just tell me the difference"). Lower-case chat style in English ("im not technical", "did they actually classify everything?"); polite in German, Japanese and Korean; fragmentary in Russian ("подрядчик сдал модель. есть там ...").

**Typical context.** The owner has a model from a contractor or designer and a contract document. No authoring software. Maybe a free viewer. Does not know the IFC version unless the contract says it. Asks about counts, totals, "do they have", "is it". Uses the contract's words (lift, plant room, dwelling unit, net area).

**Knowledge level.** Low on BIM, high on contract and money. Has heard the words EIR, IDS, COBie, but cannot use them. Will accept a table; will not accept a stack trace or a class diagram. Expects the assistant to *decide* ("is this compliant?") even when it can only report evidence.

**Typical follow-ups.**
- "ok so is that bad?" / "can I send this list to the contractor as it is?"
- "who is responsible for fixing this?" (not answerable from the file; a good assistant says so)
- "group it by discipline / by floor / by contractor"
- "how many of them, in percent?"
- "can you make that an excel" / "in my language" (assistant should switch language)
- "do we still need COBie or is IFC plus IDS enough?" (a concept question with no file)

**Traps worth including.** A request to certify compliance or approval; a comparison against a contract figure that the file cannot reproduce exactly (net vs gross area); equipment stored as generic proxies; a requirement worded in contract language that maps to several properties; a question that is really about law or procurement ("do we need BIM for this tender?"), where the assistant must not invent a legal rule; mixing owner's currency or area units.

**How to judge the answer.**
1. Answers the business question first (yes/no/number), then the evidence, then the caveat.
2. Gives something forwardable: a short, grouped list with identifiers.
3. Never asserts legal compliance, contract acceptance or authority approval. It reports what the file contains.
4. Translates jargon on the way out; does not demand IFC knowledge.
5. States the data source of every number (which class, which property, which storeys).
6. For national-rule questions, cites the rule source or says it cannot confirm; never improvises a threshold.

**Related personas.** [BIM manager](bim_manager.md) (the person who answers the owner's requirements), [BIM coordinator](bim_coordinator.md), [Reviewer / authority](reviewer_authority.md) (checks for the public interest), [Facility manager](facility_manager.md) (the owner's operations team).
