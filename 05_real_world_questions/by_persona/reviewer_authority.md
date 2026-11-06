# Reviewer / authority: who they are and what they do with IFC

**Last built: 2026-11-06 · Persona code:** `reviewer_authority` · **Data behind this page:** 85 records (41 real, 44 synthetic; `python tools/kb.py stats --persona reviewer_authority`). Languages: en 32, zh 15, es 8, ru 8, de 6, ja 5, it 4, ko 3, fr 2, no 2. Most real records are **official portals, notices and guidelines** (what the authority publishes), not questions typed by reviewers. Reviewers are not vocal online; the synthetic prompts fill the gap by imitating what a reviewer would ask an assistant.

## In plain words

A reviewer is someone who checks a design on behalf of the public: a building-permit officer in a city, a state expertise body (Russia's *expertiza*, Moscow's AGR), a fire or accessibility office, a planning department, or a public client's technical office. They receive a model together with the drawings and ask: **Does this comply with the rules? Is the data complete? Is it in the format we accept?** If not, they write a list of remarks and send the file back.

Think of a customs officer: a package arrives with a declaration; the officer checks that the declaration is filled in, the contents match, and nothing forbidden is inside. What changes with BIM is that parts of the check can be run by software: are there rooms with an area and a use, how wide is each door, which storey is each space on, is the model georeferenced, is the file under the size limit.

Two facts shape everything this persona does, both from the records. First, **in many systems the model is not the legal document**: Hong Kong's Buildings Department treats the submitted BIM model as supplementary and drawings prevail ([zh-tw-hk-r002](https://www.bd.gov.hk/tc/resources/online-tools/building-information-modelling/index.html)); Japan's 2026 BIM drawing review does not review the IFC, and the 2029 data review is planned to use it but not to be fully automated, for reasons of accountability ([ja-japan-r016](https://note.com/kensesu_ai/n/nee08ddde31f1)). Second, **the rules are local**: a model that passes in Shenzhen's SZ-IFC tool or Singapore's CORENET X checker is not guaranteed to pass elsewhere.

## Daily IFC tasks

| # | Task | What it looks like in practice | Evidence |
|---|---|---|---|
| 1 | Intake check | Right schema and view? File under the size limit? Georeferenced? Uploaded in the right folder/stage? | synthetic `en-fs-s016` "permit portal rejects ifc over 200mb, mine is 480"; `en-fmor-s013`; [zh-tw-hk-r007](https://dbadgp.gov.taipei/DownFiles/Login/%E4%BD%BF%E7%85%A7%E7%AB%A3%E5%B7%A5%E6%A8%A1%E5%9E%8B%E4%B8%8A%E7%B9%B3%E6%93%8D%E4%BD%9C%E6%89%8B%E5%86%8A.pdf) (upload IFC, then trigger model conversion) |
| 2 | Data completeness | Every space has name, use, area, storey; every wall/door has fire rating; classification codes present; no proxies. | `permitting_code_checking` 38; synthetic `ja-japan-s002`, `de-permit-s012`, `en-mea-s001` |
| 3 | Rule checks | Door clear width, stair rise/going, corridor width, ceiling height, fire compartment area, accessibility, lighting/ventilation ratios. | synthetic `en-aimcp-s002`, `no-norway-s014`, `fr-permit-s014`, `ko-permit-s011`; [ja-japan-r017](https://note.com/ken_newslab/n/n9d7072936346) lists roughly ten initial items |
| 4 | Cross-check against drawings and tables | Areas and heights in the model vs the numbers on the area table. | synthetic `zh-lightweight-review-s007` |
| 5 | Write the remarks | A list the applicant can act on, optionally as BCF or CSV. | [en-aimcp-r029](https://github.com/zeussilver/bim-ifc-mcp) (`export_issues`, CSV or BCF 2.1) |
| 6 | Compare resubmissions | What changed since version 1? | synthetic `ru-tim-expertiza-s008` |
| 7 | Run at scale | Many submissions, same ruleset; reports per file. | [ru-autodesk-telegram-r037](https://minstroyrf.gov.ru/press/pervyy-proekt-polnostyu-sproektirovannyy-na-osnove-bim-tekhnologiy-proshel-gosekspertizu/) (two stages: geometry, IFC classes, attributes, clashes; then automated code checks) |

## Goals

- **A fast first pass**: pass / fail / unknown per rule, with counts and a list of offending elements, so human time goes to the hard cases.
- **No guessing.** The bim-ifc-mcp README states the design rule as "model proposes, code executes", returns UNKNOWN instead of guesses and never lets the model estimate numbers ([en-aimcp-r029](https://github.com/zeussilver/bim-ifc-mcp)). A reviewer wants exactly that behaviour.
- **Reproducible and explainable** results, because a rejection must be justified to the applicant.
- **Standard, machine-readable requirements** (IDS) published by the authority; Mosoblexpertiza (Moscow region) has published new BIM requirements in IDS format ([ru-autodesk-telegram-r025](https://t.me/s/ifc_ru)).
- **Early self-checks for submitters** so bad files do not arrive ([zh-lightweight-review-r002](https://zhuanlan.zhihu.com/p/633827596), an in-Revit self-check before Shenzhen filing, and the unofficial CORENET X pre-checker [en-sg-corenetx-r011](https://github.com/OrvenBentleySystems/sg-ifc-microstation-eap)).
- **Accountability stays human**: tools support the reviewer, they do not approve ([ja-japan-r016](https://note.com/kensesu_ai/n/nee08ddde31f1)).

## Pains (ranked)

_Quoted phrases in the last column are illustrative: some paraphrase real records, others are taken from the synthetic prompts further down. Only the tables of real records are evidence of what people actually wrote._

Ranked by the topic counts (national_requirements 39, permitting_code_checking 38, validation_checking 16, ids_requirements 14) and by what the records describe.

| Rank | Pain | Signal | Typical shape |
|---|---|---|---|
| 1 | **The submitted model lacks the data the rule needs** | `validate_check` 38 | Missing property sets, spaces without use or area, generic proxies, stairs without a width ([en-permit-r001](https://github.com/buildingSMART/IFC4.x-development/issues/976) proposes adding stair width to the schema) |
| 2 | **Local profiles and formats differ** | `national_requirements` 39 | Shanghai uses EDM data for architecture and MEP review and IFC for structural load review; Shenzhen has SZ-IFC; Nanjing wants a lightweight 宁建模 file; Hubei H-IFC; Singapore IFC+SG; Moscow's classifier and IDS packages |
| 3 | **Checkers that silently pass** | GitHub issues on IDS | IDS Classification and PartOf facets implemented as stubs so rules that use them pass without being checked ([en-gh-thatopen-r039](https://github.com/ThatOpen/engine_components/issues/830)); optional / prohibited cardinality inverted ([en-gh-thatopen-r040](https://github.com/ThatOpen/engine_components/issues/821)) |
| 4 | **Files too heavy to open or upload** | `file_size_performance` | "the file they sent is 900mb and my viewer freezes"; "permit portal rejects ifc over 200mb" (synthetic) |
| 5 | **Rules that cannot be automated as written** | IDS limits | Geometric and conditional rules need more than property checks; "UNKNOWN" is often the honest result |
| 6 | **Exporter behaviour that breaks compliance** | Revit issues | IfcSpace PredefinedType exported as NOTDEFINED although mandatory for Chilean public projects ([en-spaces-r015](https://github.com/Autodesk/revit-ifc/issues/247)) |
| 7 | **Unclear status of the model vs the drawings** | policy | "drawings prevail", "IFC not reviewed" |

## Vocabulary they use (and what they do not know)

### Words and phrases you will see

| Phrase (language) | Plain meaning |
|---|---|
| submission / resubmission / remarks, 提交 / 报建 / 报批, 確認申請 / BIM図面審査, Bauantrag, licencia de obras, alvará, государственная экспертиза / АГР | The permit or approval process in each country. |
| compliance, code check, rule set, ruleset, 規範 / 审查要点, TEK17 (no), CTE (es), PMR (fr) | The rules the model is tested against. |
| clear width, means of escape / egress, evacuation route, 疏散门, 避難経路 | The numbers reviewers care about. |
| fire compartment, fire rating, EI30-EI120, 耐火時間, огнестойкость | Fire-safety data. |
| IFC+SG, COP 3.1 / COP 4, SZ-IFC, H-IFC, EDM, 宁建模, IDS | Local checker profiles and the open IDS standard. |
| IFC0000101, IFC0000104 (CORENET X error codes) | Checker error codes people quote in their question. |
| pass / fail / UNKNOWN, PASS/FAIL/UNKNOWN | Allowed outcomes for a machine check. |
| BCF, CSV, report | Output forms for remarks. |

### What they typically do not know, or get wrong

- **IFC stores what the authoring tool wrote, not what the rule needs.** A door's "width" may be an overall size, not the clear opening, and a stair may have no width property at all. A good assistant says which attribute it read and when the data does not exist.
- **How a model "passes" in a checker but still violates the rule** (formal pattern correct, content wrong; see [nl-dutch-r002](https://github.com/OpenAEC-Foundation/OpenAEC-BIM-validator/issues/22)).
- **Differences between IFC versions** in how occurrences map to types (for example [en-fmor-r025](https://github.com/buildingSMART/IDS-Audit-tool/issues/56): IFC2x3 type/occurrence mapping gives wrong results in an IDS audit; [en-val-r031](https://github.com/buildingSMART/IDS-Audit-tool/issues/61): the audit passes attributes that should not be allowed).
- **How much the authority's own tool can see.** They ask the assistant whether a file will "pass"; the honest answer is "these checks pass, these cannot be evaluated".

Read next: [Regulations, permits, contracts](../by_topic/regulations_permits_contracts.md), [validation / IDS](../by_topic/validation_ids_model_checking.md), the national files ([Russia](../../02_standards_regulations/national/russia.md), [China](../../02_standards_regulations/national/china_mainland.md), [Singapore](../../02_standards_regulations/national/singapore.md), [Japan/Korea](../../02_standards_regulations/national/japan_korea.md), [Spain/Portugal/Italy](../../02_standards_regulations/national/spain_portugal_italy.md), [DACH](../../02_standards_regulations/national/germany_austria_switzerland.md), [Latin America](../../02_standards_regulations/national/latin_america.md)), [buildingSMART standards](../../02_standards_regulations/buildingsmart_standards.md), [properties and psets](../../01_ifc_basics/05_properties_quantities_psets.md).

## Real questions (41, linked)

Paraphrases of what the linked page says or what its reader wants to know, in the original language where the researcher wrote one. Language mix in this list: Russian 4, English 12, other languages 25. **Most rows are official pages, not questions typed by reviewers**; the English gloss states the content. Where a source page is not in English but the stored paraphrase is, the Lang column still shows the page language.

### A. China, Hong Kong and Taipei: model-assisted permit review

Local notices and manuals from planning, construction-drawing review and building departments. They define who must submit a model, in which format, at which stage. The "question" column is what a submitter (or reviewer) wants to know from the page.

| # | Lang | Their words (paraphrase, original language) | English gloss / context | Source (record id, type, year) |
|---|---|---|---|---|
| 1 | zh | 哪些项目要同步提交BIM模型做规划报批 | Guangzhou trial of BIM electronic planning approval: submit BIM model with planning technical review for gov projects over 20,000 m2, prefab, key zones, from 2020-10-01. | [zh-lightweight-review-r019](https://www.gz.gov.cn/xw/tzgg/content/post_6469259.html) regulation, 2020 |
| 2 | zh | 施工图审查要同时上传二维图纸和BIM模型吗 | Guangzhou trial of BIM-assisted construction drawing review: upload 2D drawings and BIM model together; owner confirms consistency. | [zh-lightweight-review-r020](https://zfcj.gz.gov.cn/gkmlpt/content/6/6434/post_6434530.html) regulation, 2020 |
| 3 | zh | 自主可控BIM，审图后模型汇入CIM平台，图模对位不合格传不上去 | Guangzhou 2025 white paper on autonomous and controllable BIM: models flow into the CIM platform after review; drawing-model alignment check since 2023. | [zh-lightweight-review-r023](https://zfcj.gz.gov.cn/attachment/7/7943/7943479/10589336.pdf) official_doc, 2025 |
| 4 | zh | 南京BIM规划报建要交原生模型和宁建模轻量化文件吗 | Nanjing BIM planning submission: from 2021-03-01 in pilot zones, projects submit native BIM plus lightweight 宁建模 file after QC; free aided-design software. | [zh-lightweight-review-r024](http://ghj.nanjing.gov.cn/njsgtzyj/202103/t20210301_2834720.html) official_doc, 2021 |
| 5 | zh | 上海审查用EDM还是IFC | Shanghai BIM smart-review modeling manual: EDM data file for architecture/MEP review, IFC for structural load review. | [zh-lightweight-review-r026](https://zjw.sh.gov.cn/cmsres/4a/4a7bc95634cd4852b2399e57e9c692dd/a646541bab5ad86dc1684d1126e21e29.pdf) regulation, 2023 |
| 6 | zh | 深圳哪些项目要用SZ-IFC报建，几个阶段提交 | Shenzhen SJG114-2022 SZ-IFC: projects over 10M yuan and 1,000 m2 must apply BIM from 2023; models submitted at planning, construction permit, completion. | [zh-lightweight-review-r027](https://zjj.sz.gov.cn/attachment/0/678/678888/7768421.pdf) regulation, 2023 |
| 7 | zh | 湖北H-IFC数据规范是什么 | Hubei province BIM cloud platform (June 2026) with H-IFC localized data specification across planning to archiving. | [zh-lightweight-review-r030](https://www.ctdsb.net/c1676_202606/2785613.html) social, 2026 |
| 8 | zh | 上海试行BIM智能辅助审查，设计单位要导出什么格式 | Shanghai from 2024-02-01 trials BIM-assisted review (EDM format; IFC to be explored) | [zh-zhihu-r024](https://zhuanlan.zhihu.com/p/676069996) regulation, 2024 |
| 9 | zh | 屋宇署：呈交的建築信息模型屬補充資料僅供參考，圖則與模型不一致以圖則為準；提供Revit/ArchiCAD外掛核查樓面面積、衞生設備、消防 | HK Buildings Department: submitted BIM models are supplementary only; drawings prevail; plug-ins check GFA, sanitary, fire safety; Revit IFC export text file provided. | [zh-tw-hk-r002](https://www.bd.gov.hk/tc/resources/online-tools/building-information-modelling/index.html) official_doc, 2025 |
| 10 | zh | 屋宇署第二輪持份者諮詢活動頁面（無繁中版本） | BD 2nd-round stakeholder engagement on BIM roadmap (Chinese page redirects to English). | [zh-tw-hk-r004](https://www.careyourbuilding.bd.gov.hk/ors/tc/event/307.html) official_doc, 2023 |
| 11 | zh | 使照竣工模型上繳：在系統BIM模型頁選擇上傳IFC檔，上傳完成後啟動模型轉檔 | Taipei building administration manual: upload as-built (use permit) BIM model as IFC then trigger model conversion. | [zh-tw-hk-r007](https://dbadgp.gov.taipei/DownFiles/Login/使照竣工模型上繳操作手冊.pdf) official_doc, 2023 |

### B. Japan, Singapore, Russia: IFC in an official check

Japan separates a 2026 drawing review from a planned 2029 data review. Singapore's CORENET X uses IFC+SG. a Moscow-region expert body publishes requirements as IDS files, and state expertise describes a two-stage check.

| # | Lang | Their words (paraphrase, original language) | English gloss / context | Source (record id, type, year) |
|---|---|---|---|---|
| 12 | ja | BIM図面審査では確認申請書+BIM書き出しPDF+同時書き出しIFC+誓約書を提出。IFCは審査対象外。AIはどこまで入る？ | BIM drawing review (Apr 2026) vs BIM data review (spring 2029): what is submitted and how IFC is used | [ja-japan-r016](https://note.com/kensesu_ai/n/nee08ddde31f1) blog, 2026 |
| 13 | ja | 国交省の基本構想では採光・換気、容積率、建蔽率、斜線など約10項目から。構造・省エネは検討中 | MLIT 2029 BIM data review: view review vs digital review, initial ~10 review items | [ja-japan-r017](https://note.com/ken_newslab/n/n9d7072936346) blog, 2026 |
| 14 | en | pre-check ifc+sg against COP 3.1 or COP 4 before submitting, select failing elements, export bcf | Unofficial pre-flight checker against CORENET X Code of Practice editions COP 3.1 and COP 4, exporting BCF. | [en-sg-corenetx-r011](https://github.com/OrvenBentleySystems/sg-ifc-microstation-eap) blog, 2026 |
| 15 | ru | формат IFC 2x3 и выше для обмена моделями | SP 333 recommends exchanging digital models in IFC 2x3 or higher and requires elements to be classified and uniquely identified | [ru-autodesk-telegram-r036](http://docs.cntd.ru/document/556793897) regulation, 2017 |
| 16 | ru | входные проверки: геометрия, классы IFC, атрибуты, коллизии | First fully BIM-designed project passed state expertise; two-stage check: geometry, IFC classes, attributes, clashes, then automated code checks | [ru-autodesk-telegram-r037](https://minstroyrf.gov.ru/press/pervyy-proekt-polnostyu-sproektirovannyy-na-osnove-bim-tekhnologiy-proshel-gosekspertizu/) regulation, 2021 |
| 17 | ru | требования к выгрузке элементов в IFC, соответствие классов IFC категориям | Collection of Moscow TIM requirements includes classification of CIM elements and rules for exporting elements to IFC with class mapping appendices | [ru-autodesk-telegram-r038](https://digest.wizardsoft.ru/wp-content/uploads/media/doc/2025/MKE-OD-24-178Chast3.pdf) regulation, 2025 |
| 18 | ru | новые BIM-требования в формате IDS | Mosoblexpertiza published new BIM requirements in IDS format for roads, utilities and buildings | [ru-autodesk-telegram-r025](https://t.me/s/ifc_ru) social, 2026 |

### C. Europe, Latin America, Korea: public bodies and procurement rules



| # | Lang | Their words (paraphrase, original language) | English gloss / context | Source (record id, type, year) |
|---|---|---|---|---|
| 19 | it | da quando e obbligatorio il BIM negli appalti e sopra che soglia? serve per forza l'IFC? | When is BIM mandatory in Italian public procurement (over 2 million euro, from 1 Jan 2025) and which open format is required? | [it-italy-r004](https://biblus.acca.it/nuovo-codice-appalti-il-bim-e-obbligatorio/) regulation, 2026 |
| 20 | it | cosa dicono le linee guida MIT 2026 su ACDat, ruoli e formato IFC? il modello prevale sul 2D? | What do the 2026 MIT guidelines on digital information management (GID) require: roles, ACDat, formats, model prevailing over 2D? | [it-italy-r010](https://biblus.acca.it/linee-guida-bim-2026-per-le-stazioni-appaltanti/) regulation, 2026 |
| 21 | it | nei raggruppamenti il requisito BIM lo deve avere il singolo o il gruppo? | BIM requirements in RTI: individual professional or working group? | [it-italy-r020](https://biblus.acca.it/notizie/requisiti-bim-negli-rti-conta-il-professionista-o-il-gruppo-di-lavoro/) blog, 2026 |
| 22 | es | presentación del MEF sobre aplicación obligatoria de BIM en inversión pública, Guía Nacional BIM y NTP-ISO 19650 | MEF training deck: Peru national BIM guide, NTP-ISO 19650, mandatory application under DS 203-2024-EF | [es-latam-r015](https://www.mef.gob.pe/contenidos/inv_publica/docs/capacitaciones/2026/20260317.pdf) official_doc, 2026 |
| 23 | es | documento de política del MEF para la adopción progresiva de BIM | Plan BIM Peru policy document led by the MEF for progressive BIM adoption in public investment | [es-latam-r016](https://www.mef.gob.pe/planbimperu/docs/planBIMpE.pdf) regulation, 2021 |
| 24 | es | official report on the draft plan | Junta Consultiva de Contratación Pública report 22/2023 on the draft Plan BIM. | [es-spain-r026](https://www.hacienda.gob.es/DGPatrimonio/Junta%20Consultiva/informes/informes2023/2023-23-MTMAU-BIM.pdf) regulation, 2023 |
| 25 | en | English summary of Spain's Plan BIM | EU public buyers document on Spain's Plan BIM; a search snippet says models should be delivered as IFC per UNE-EN ISO 16739 or equivalent. | [es-spain-r027](https://public-buyers-community.ec.europa.eu/system/files/2024-05/AIDA%20240322_GabSUB_DGGROWPPUnit_PlanBIM_en_v1_0.pdf) official_doc, 2024 |
| 26 | de | Official explanation of CDE states WIP/Shared/Published/Archive and openBIM. | BIM Deutschland explains the CDE per ISO 19650 and says an open CDE must manage IFC, BCF, COBie. | [de-dach-r024](https://www.bimdeutschland.de/bim-wissen/standards-normen-richtlinien/common-data-environment) official_doc, 2025 |
| 27 | de | MVD defines which data an IFC must contain for an exchange use case. | Explains MVDs (Coordination View, Design Transfer View, Reference View, QTO View) and that AIA/BAP must name them. | [de-dach-r025](https://www.bimdeutschland.de/bim-wissen/standards-normen-richtlinien/model-view-definitions) official_doc, 2025 |
| 28 | de | Federal AIA and BAP templates for Hochbau, Strasse, Schiene plus IFC data-exchange guide. | Download list of Muster-AIA, Muster-BAP and BIM4INFRA2020 Teil 9 Datenaustausch mit IFC. | [de-dach-r026](https://www.bimdeutschland.de/bim-wissen/downloads) official_doc, 2025 |
| 29 | ko | 국토부 건축 BIM 적용가이드 내용 | MOLIT architectural BIM application guide (2010) hosted by bSK | [ko-korea-r003](https://www.buildingsmart.or.kr/Data/Main/BIM%20Guide_MLTL_Korea_2010.pdf) regulation, 2010 |
| 30 | no | hvilke komiteer i Standard Norge styrer BIM-standarder og klassifisering? | Which Norwegian standardisation committees govern BIM and classification? | [no-norway-r008](https://www.buildingsmart.no/standarder/standardiseringsarbeid.html) official_doc, 2026 |
| 31 | es | Looking for international counterparts developing land models based on IFC, CityGML or similar; what is the status of the site/landscape/urban planning initiative? Aim: discussion at the chapter conference. | buildingSMART Spain chapter looks for international groups working on land models via IFC/CityGML and the status of IFC for Site, Landscape and Urban Planning. | [es-bsi-gis-r011](https://forums.buildingsmart.org/t/rfi-urban-and-land-management-think-tank-room-group/4754) forum, 2023 |

### D. Checking technology and its defects (reviewer-side tooling)

What happens when the checker itself is wrong, silent or too cautious: these are the cases that matter most for judging an AI checker.

| # | Lang | Their words (paraphrase, original language) | English gloss / context | Source (record id, type, year) |
|---|---|---|---|---|
| 32 | en | model_summary, check_door_widths(min 850), run_rules, export_issues | Design rule 'model proposes, code executes': room areas, door widths, fire doors checked deterministically, UNKNOWN instead of guesses, exported as CSV or BCF 2.1. | [en-aimcp-r029](https://github.com/zeussilver/bim-ifc-mcp) official_doc, 2026 |
| 33 | en | check that all IfcDoor have Fire Rating in a given pset with allowed values | Model validation workflow: translate sports facility code into Solibri rules and IDS checks. | [en-blogs-linkedin-r029](https://bimcorner.com/model-validation-as-a-key-step-in-the-bim-workflow/) blog, 2024 |
| 34 | en | IDSClassification and IDSPartOf bodies are commented out; against buildingSMART test cases all 27/33 select nothing so failing cases pass | IDS Classification and PartOf facets are stubs, so specs using them pass without checking | [en-gh-thatopen-r039](https://github.com/ThatOpen/engine_components/issues/830) github_issue, 2026 |
| 35 | en | cardinality optional/prohibited does not follow IDS: prohibited inverts each match, optional forces pass, no matching pset pushes fail | Optional and prohibited property requirements give inverted results in IDS checks | [en-gh-thatopen-r040](https://github.com/ThatOpen/engine_components/issues/821) github_issue, 2026 |
| 36 | en | While working through accessibility code I see IfcStair has no direct width property; suggest Width/StairWidth in Pset_StairCommon to support rule-based compliance checks. | Propose adding a stair width property to IfcStair/IfcStairFlight so accessibility and fire code checks can be automated. | [en-permit-r001](https://github.com/buildingSMART/IFC4.x-development/issues/976) github_issue, 2025 |
| 37 | en | What are the expectations for Qto_ quantity properties (title only) | What are the expectations for Qto_ quantity properties | [en-fmor-r034](https://forums.buildingsmart.org/t/qto-properties-expectations/6298) forum, 2025 |
| 38 | en | the definition of flexible pavement was wrongly redefined with text invented by someone without consulting the original definition | Pavement predefined type definitions were wrongly redefined in the IFC4.3.2 / ISO text versus the original PIARC-based road definitions. | [en-civil-infra-r026](https://github.com/IfcOpenShell/IfcOpenShell/issues/7447) github_issue, 2025 |
| 39 | en | Revit auto-generates hundreds of IfcBuildingElementProxyType (maybe curtain wall reveals) that cannot be edited so clients see proxies without data. |  | [en-gh-revit-ifc-r011](https://github.com/Autodesk/revit-ifc/issues/676) github_issue, 2023 |
| 40 | en | IfcExportAs=IfcSpace.EXTERNAL becomes NOTDEFINED; mandatory in Chilean public deliveries; manual text edit workaround | IfcExportAs IfcSpace.EXTERNAL shows NOTDEFINED in Solibri/BIMcollab; PredefinedType required for public projects in Chile. | [en-spaces-r015](https://github.com/Autodesk/revit-ifc/issues/247) github_issue, 2020 |
| 41 | en | Revit exports similar walls inconsistently as IfcWall or IfcWallStandardCase; layer data missing for thermal analysis; questions how interoperability can claim success. |  | [p-student-r015](https://forums.buildingsmart.org/t/difference-between-expectations-and-reality-of-ifc-standards/1040) forum, 2019 |

## Ready test prompts (47, synthetic)

**All prompts below are SYNTHETIC.** Ids that start `new-reviewer-` were written for this page, each inspired by the record named in its tag; all others come from the research files. Rule prompts name the threshold in the prompt; the assistant must not apply a rule from memory that the user did not state, unless it names the source.

### 1. Is the required data there?

Mandatory classes, properties, spaces with use and area, classification, proxies. These are the checks a reviewer runs first.

| # / id | Lang | Prompt (SYNTHETIC) | Meaning (EN) | Difficulty | A good answer should |
|---|---|---|---|---|---|
| S1 `en-blogs-linkedin-s005` | en | do all IfcDoor have FireRating in Pset_DoorCommon, values EI30-EI120 only? list the failing ones | IDS style check on fire rating | medium, file | Query doors, check property and allowed values, list failures with GlobalId/Name. |
| S2 `en-gh-revit-ifc-s016` | en | check every IfcDoor has Pset_DoorCommon with FireRating filled, list those without | Pset completeness | easy, file | Iterate IfcDoor, check property presence/value, output failing list. |
| S3 `es-latam-s011` | es | revisa que todos los muros tengan FireRating y material asignado, dime los que no | Check fire rating and materials on walls | easy, file | Check Pset_WallCommon.FireRating and material associations for IfcWall, list offending elements. |
| S4 `de-permit-s012` | de | Bauantrag IFC: haben alle Räume NetFloorArea und Nutzungsart? Liste die ohne bitte | Check permit data on rooms | medium, file | List IfcSpace missing area or usage and report. |
| S5 `en-mea-s001` | en | need to submit this to the municipality tomorrow. can u check every wall, slab and door has a classification code + fire rating + level name filled? list whatever is missing | Check a model before submission to a Gulf municipality: every element needs a classification and a few mandatory properties. | medium, file | Iterate walls, slabs, doors; check classification references, Pset FireRating, and containing storey; return a grouped list of missing items with GlobalIds and counts; do not invent authority-specific rules. |
| S6 `zh-tw-hk-s004` | zh | 查一下牆、門、窗有沒有填防火時效、材料欄位，缺的列出來 | Check required parameters present | medium, file | Check Pset_*Common FireRating etc. on walls/doors/windows, report elements missing values. |
| S7 `ja-japan-s002` | ja | 確認申請用に出したIFCの全IfcSpaceについて、部屋名・用途・床面積が入ってるか確認して。抜けてる部屋は一覧で | For BIM drawing review check each IfcSpace has a name, usage and floor area | medium, file | List IfcSpace, check Name/LongName, usage property and Qto_SpaceBaseQuantities NetFloorArea, report missing ones with GlobalId and storey. |
| S8 `en-gh-xbim-others-s012` | en | does every storey have elevation and at least 1 IfcSpace? list the ones without | Check each storey has elevation and spaces assigned | easy, file | Verify BuildingStorey Elevation present and contains IfcSpace; report exceptions. |
| S9 `en-us-canada-infra-s017` | en | GSA wants space ids, dept, and areas. do the IfcSpaces have those? list ones missing | Per GSA guide, check spaces for area and department data | medium, file | Check IfcSpace for names, department data, Qto areas; list missing. |
| S10 `en-spaces-s007` | en | every IfcSpace needs a PredefinedType per the client spec, which ones are NOTDEFINED | Check required PredefinedType on spaces | easy, file | List spaces with NOTDEFINED/missing PredefinedType, explain 2x3 limits. |
| S11 `en-fmor-s007` | en | how many IfcBuildingElementProxy are in here and what are they supposed to be | Count proxies in the model and show where they are | easy, file | Count proxies, group by Name/ObjectType and storey, suggest likely proper classes. |
| S12 `en-fmor-s014` | de | pruef mal ob alle Raeume ne Nutzung haben und einem Geschoss zugeordnet sind | Check all spaces have a use designation and are assigned to a storey | medium, file | Check IfcSpace for use/occupancy property and containment in IfcBuildingStorey, list violations. |
| S13 `en-permit-s002` | en | which IfcStair / IfcStairFlight have no width anywhere? psets, quantities, doesnt matter. i need to check min stair width for egress | Find stairs lacking width data | medium, file | List stairs, search Pset/Qto/attributes for width, fall back to geometry-derived width, report stairs with no data. |

### 2. Rule thresholds: widths, heights, stairs, areas, fire

Rule checks need numbers AND a statement of which attribute was read. "UNKNOWN" must be an allowed outcome.

| # / id | Lang | Prompt (SYNTHETIC) | Meaning (EN) | Difficulty | A good answer should |
|---|---|---|---|---|---|
| S14 `en-aimcp-s002` | en | check every door in the model for clear width >= 850mm, give me a list of failures with storey and GUID, dont guess if the data is missing | Check all doors for min clear width 850 and list failures | medium, file | Run door width check, return PASS/FAIL/UNKNOWN with GlobalId, storey; mark missing widths UNKNOWN. |
| S15 `en-fmor-s004` | en | check all doors on the escape route, clear width ok? flag anything under 900 | Check that every door on escape routes has min clear width | hard, file | Find IfcDoor with OverallWidth or clear-width property under 900 mm, state which property was used, flag missing values, list by storey. |
| S16 `no-norway-s014` | no | sjekk dørbredder i rømningsveier mot TEK17, hvilke dører er under 90 cm | Check door widths and escape routes for TEK17 | hard, file | Filter doors on escape routes, read OverallWidth/clear width, list those below threshold with caveats on what is not modelled. |
| S17 `zh-permit-s008` | zh | 帮我审一下这个ifc模型，疏散门宽度有没有小于0.9米的，列出楼层和编号 | Check evacuation door widths | medium, file | Find IfcDoor on evacuation routes, read width, list those below 0.9 m with storey and tag. |
| S18 `fr-permit-s014` | fr | vérifie l'accessibilité PMR : portes < 90 cm et couloirs < 1,40 m dans la maquette, liste avec niveau | Check accessibility of doors and corridors | hard, file | Measure doors and corridor spaces, list those under thresholds with storey. |
| S19 `ko-permit-s011` | ko | 건축허가용 IFC인데 계단 챌판 높이랑 디딤판 폭 기준 안 맞는 계단 찾아줘 | Check stair tread and riser dimensions | hard, file | Read stair geometry or properties, compare riser and tread against supplied limits, list failures. |
| S20 `ja-permit-s010` | ja | 確認申請用のIFCです。居室の天井高が2.1m未満の部屋と面積を一覧にしてください | Check ceiling height for building confirmation | medium, file | List IfcSpace with height and area, filter by 2.1 m, tabulate. |
| S21 `zh-lightweight-review-s016` | zh | 楼梯净宽和走道宽度查一下，哪些小于规范要求 | Check stair widths and corridor widths against code. | hard, file | Extract stairs and corridor spaces dimensions, compare to a stated threshold, flag with GlobalId; ask which code clause. |
| S22 `en-permit-s004` | en | all IfcSpace on level 2 with area, and is any fire compartment over 1000 m2? name the spaces | Check room areas and fire-compartment area against a limit | hard, file | Read IfcSpace areas from Qto or geometry, group by zone/compartment, compare to threshold, list offenders. |
| S23 `zh-lightweight-review-s007` | zh | 核一下建筑面积和层高跟图纸报的数对不对，差多少 | Check building area and floor height against drawing figures. | hard, file | Compute slab/space areas and storey heights from the model, compare to given values, report deviations and uncertainties. |
| S24 `ja-japan-s015` | ja | 防火区画に関係する壁と床の耐火時間が入っているか、IsExternalと一緒に確認して | Check fire-compartment related properties on walls and slabs for permit review | medium, file | Collect IfcWall/IfcSlab, read FireRating and IsExternal from Pset common, report missing or inconsistent. |
| S25 `es-spain-s013` | es | revisa si los espacios tienen superficie y uso asignado para el CTE | Check basic CTE-related data | medium, file | List IfcSpace with area and usage, flag missing. |
| S26 `new-reviewer-n01` (new, inspired by en-aimcp-s002) | ru | найди двери на путях эвакуации уже 0,9 м. если ширины в свойствах нет - так и пиши, не додумывай | Find evacuation-route doors narrower than 0.9 m; say so if width is not in the data | hard, file | Identify doors on escape routes (via spaces/properties; say if routes are not modelled); read width from the right attribute/property; list below threshold with level and GlobalId; mark unknowns separately. |
| S27 `new-reviewer-n02` (new, inspired by zh-lightweight-review-s007) | ru | сравни площади помещений в модели с таблицей ТЭП из пояснительной записки (csv прикреплю), расхождение больше 1% - в замечания | Compare room areas in the model with a TEP table, flag deviation over 1 percent | hard, file | Sum IfcSpace areas by room number/storey, join with the csv by room number, compute deviation, list rows above 1 percent and rows that do not match; state area source. |

### 3. Against a client or authority specification (IDS, EIR, national package)



| # / id | Lang | Prompt (SYNTHETIC) | Meaning (EN) | Difficulty | A good answer should |
|---|---|---|---|---|---|
| S28 `de-dach-s011` | de | prüf die IFC gegen unsere IDS vom Auftraggeber und gib mir die Fehler nach Bauteilen | Check against an IDS file. | medium, file | Run IDS validation, group failures by requirement and entity, provide GUID lists. |
| S29 `ru-autodesk-telegram-s012` | ru | проверь модель по этому IDS ЦГЭ и дай сводку нарушений по классам, самые частые сверху | Check model against provided IDS and summarise failures by class | medium, file | Run IDS validation, aggregate failed specifications by IFC class and requirement, list top failures with sample GlobalIds. |
| S30 `ru-renga-nanocad-s012` | ru | проверьте пожалуйста, у элементов проставлен классификатор по требованиям к информационной модели, какие без кода | Check classification codes per Russian requirements on elements | hard, file | Read IfcClassificationReference on elements, list those without a code, group by IFC class, state the assumed classification system. |
| S31 `ru-permit-s006` | ru | проверь ifc на соответствие требованиям к ТИМ для госэкспертизы: есть ли классы, уровни, обязательные свойства, что не заполнено | Check the model against expertise requirements for IFC submission | hard, file | Check classes, storeys and required properties; report gaps; state that the exact national requirement list must be supplied. |
| S32 `es-latam-s002` | es | revisa si el modelo cumple la MIDE de planbim, qué entidades no traen sus propiedades requeridas | Check the model against the Planbim MIDE required properties | hard, file | Load the required entity/property list, check each entity for the required Pset properties, report missing ones per entity with counts. |
| S33 `fr-francophone-s008` | fr | contrôle la maquette par rapport au cahier des charges BIM : propriétés obligatoires par classe, résume les écarts | Check the model against required properties from the BIM execution plan | hard, file | Apply listed requirements per class, output pass/fail counts and non-conforming elements. |
| S34 `it-italy-s007` | it | verifica se il modello rispetta il capitolato informativo: classificazione, materiali, FireRating su tutti i muri | Check model vs capitolato informativo requirements | hard, file | Check required properties/classification across classes and report non-conformances. |
| S35 `ko-korea-s015` | ko | IDS 파일 기준으로 이 모델 검증하고 실패한 객체 알려줘 | IDS check | hard, file | Run IDS validation and list failing elements per specification. |
| S36 `en-us-canada-infra-s006` | en | check this bridge ifc against our dot delivery reqs - every girder needs material, pay item no., and a predefined type. list failures by GlobalId | Check bridge IFC against delivery requirements | medium, file | Validate required properties per element class (IDS-style), return failing GlobalIds with reasons. |
| S37 `en-civil-infra-s009` | en | can you check each rail asset has the required pset from our EIR before I submit | Check every rail asset has the EIR property sets before submission | hard, file | Read the requirement list; check psets/properties per class; output missing items per element. |

### 4. Schema, georeference, size limits, resubmission diff, reporting



| # / id | Lang | Prompt (SYNTHETIC) | Meaning (EN) | Difficulty | A good answer should |
|---|---|---|---|---|---|
| S38 `en-autodesk-revit-import-s009` | en | opens in revit fine but bsi validator complains, can you check the schema errors in this file | Validate schema compliance | medium, file | Run schema validation, summarize error classes and offending entity ids. |
| S39 `en-beginner-qa-s015` | en | is this file even valid ifc? my viewer complains | Is this a valid IFC | medium, file | Parse and validate schema conformance, list errors, state IFC version. |
| S40 `en-fmor-s013` | en | does the model have proper georef and is it in meters? authority needs it | Check model has georeferencing and units correct for submission | medium, file | Inspect IfcProjectedCRS, IfcMapConversion, unit assignment, report values and missing items. |
| S41 `en-infra-s005` | en | check spatial structure: are IfcBridge / IfcRoad / IfcRailway properly aggregated under the site or facility? | Check that facilities (IfcRoad, IfcBridge, IfcRailway) are aggregated properly under IfcSite. | medium, file | Walk IfcRelAggregates from IfcProject, flag orphan facilities and illegal nesting. |
| S42 `es-infra-s011` | es | puedes validar este IFC de carretera contra el esquema 4.3 y decirme los errores principales | Check the IFC against the buildingSMART validation rules for an infrastructure model. | medium, file | Run schema and basic rule checks, summarise errors by type, mention bSI validation service. |
| S43 `ru-tim-expertiza-s008` | ru | сравни версию 1 и версию 2 модели, что добавилось, удалилось, поменялось по GUID | Compare two submitted model versions | hard, file | Diff by GlobalId: added, removed, changed attributes/properties; summarize by class. |
| S44 `en-fmor-s018` | en | the file they sent is 900mb and my viewer freezes, anything to make it reviewable? | Submitted IFC too heavy to open for review | medium, no file | Suggest checking geometry density, splitting by discipline, IFCZIP, filtering; offer summary without full load. |
| S45 `en-fs-s016` | en | our permit portal rejects ifc over 200mb, mine is 480. whats the safest way to shrink without losing the data they check? | Portal upload limit of 200MB | medium, no file | Suggest reducing geometry detail, removing non-required psets, ifcZIP, splitting; keep required classification and property data and verify afterwards. |
| S46 `new-reviewer-n03` (new, inspired by en-aimcp-r029) | ru | оформи замечания по итогам проверки списком для заявителя: что не прошло, где (этаж, GlobalId), какое требование нарушено | Format the findings as a list for the applicant | medium, file | Produce a structured list of failures: requirement id, storey, element name and GlobalId, short explanation; offer CSV or BCF; no verdict about approval. |
| S47 `new-reviewer-n04` (new, inspired by en-aimcp-r029) | en | give me those failing doors as a BCF, one topic per storey, with the requirement text in the description | Export findings as BCF grouped per storey | hard, file | Create BCF topics (one per storey) with viewpoints/GlobalIds and the requirement text; confirm count and file name; do not invent camera positions that cannot be computed. |

## How to role-play this persona in tests

**Voice.** Formal-ish and directive; bureaucratic wording in real pages, short imperative in chat: "check every door in the model for clear width >= 850mm, give me a list of failures with storey and GUID, dont guess if the data is missing"; Russian: "проверь модель по этому IDS ... дай сводку нарушений по классам, самые частые сверху"; Japanese: "確認申請用に出したIFCの全IfcSpaceについて、部屋名・用途・床面積が入ってるか確認して"; Chinese: "疏散门宽度有没有小于0.9米的，列出楼层和编号"; German: "Bauantrag IFC: haben alle Räume NetFloorArea und Nutzungsart? Liste die ohne bitte".

**Typical context.** A submitted IFC (often IFC4, sometimes IFC2x3, sometimes 4.3 for infrastructure), a rule set (national code, IDS, portal checklist), sometimes an area table from the drawings. The reviewer usually cannot see the authoring tool and does not know the exporter settings.

**Knowledge level.** High on codes, low on IFC internals. Knows "storey", "space", "fire rating", "classification code"; does not know `IfcRelContainedInSpatialStructure` or property-set inheritance. Wants results traceable to elements and rules.

**Typical follow-ups.**
- "now only the ones on the escape routes"
- "list those unknown separately from those that failed"
- "export as BCF / CSV for the applicant"
- "compare with the previous submission, what did they fix?"
- "which of these failures are the exporter's fault vs the designer's?" (the assistant cannot know; it can show which classes/properties are absent)
- "is it approved?" (must be refused politely: a reviewer decides)

**Traps worth including.** Thresholds in different units (mm vs m; feet); "clear width" vs overall width; doors without a width property; rooms without storey; IFC2x3 vs IFC4 property placement; an IDS with unsupported facets (Classification or PartOf in some tools) that silently passes; portal size limits that make "just upload it" impossible; a request for a rule from the assistant's memory ("what is the minimum corridor width?") where the right answer is to ask for the applicable code or cite a source.

**How to judge the answer.**
1. Pass / fail / unknown reported separately, with counts and identifiers (storey, GlobalId, name).
2. States which attribute or property was read for each rule, and when a needed value is absent says "unknown" rather than estimating (the design rule of [bim-ifc-mcp](https://github.com/zeussilver/bim-ifc-mcp)).
3. Never says the project is approved, compliant with law, or "will pass the authority"; only what the file shows.
4. Does not apply national thresholds from memory unless cited.
5. Output is suitable to send: structured, no chatty text, optional BCF/CSV.
6. For tool defects (silent passes), a good assistant tells the user which facets or rule types it could not evaluate.

**Related personas.** [BIM coordinator](bim_coordinator.md) (the submitter's side), [BIM manager](bim_manager.md), [Architect](architect.md), [Owner / client](owner_client.md).
