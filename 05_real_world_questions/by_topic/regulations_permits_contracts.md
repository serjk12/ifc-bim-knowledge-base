# National requirements, permits and code checking, contracts/EIR/BEP/LOIN

Vocabulary topics covered: `national_requirements`, `permitting_code_checking`, `contracts_bep_eir_loin`.
Built from the wave-1 research records (240 records carry at least one of these topics: 161 real, 79 synthetic; languages: en 75, zh 45, ru 26, es 20, ja 13, it 12, no 12, de 12, ko 8, nl 8, fr 5, pt 4). Last built: 2026-11-06.

## In plain words

When someone must hand over a building model to an authority or a client, they are told *what the model has to contain*. That "what" lives in three different places that people constantly mix up:

1. **The rules of a country, city or portal.** Examples: Singapore's CORENET X with its IFC+SG data structure, Shenzhen's SZ-IFC, Moscow's AGR submission (checked against an IDS file), Japan's BIM drawing review (since April 2026) with a planned IFC-based "data review", Hong Kong's roadmap, Italy's rule for public tenders above EUR 2 million. These rules are local, change often and are sometimes recommendations, not law.
2. **The contract documents.** The client writes an **EIR** (Exchange Information Requirements; German: AIA; Italian: *capitolato informativo*; Norwegian packages such as POFIN) and the supplier answers with a **BEP** (BIM Execution Plan; German: BAP). These fix the IFC version, the view (MVD), exchange rhythm, naming, coordinates, classification and who checks what.
3. **The technical wording of requirements.** IFC version and MVD, **LOIN** (level of information need, which replaces the vague "LOD": how much geometry, data and documents each object needs per phase), classification codes, and increasingly an **IDS** file (a machine-readable list of "every IfcWall must have FireRating").

An AI assistant connected to an IFC file can honestly answer "is the data there?" (classes, property sets, classification, storeys, areas, base point, schema). It cannot answer "will the authority approve?" and should never say so. The typical test request is therefore: *"I submit tomorrow, check my IFC for X and list what is missing"*. Real users write exactly like this, in many languages, usually under time pressure.

Background reading: [EIR/BEP clauses with real examples](../../02_standards_regulations/requirements_in_contracts_eir_bep.md), the country files in [national/](../../02_standards_regulations/national/) ([Russia](../../02_standards_regulations/national/russia.md), [China](../../02_standards_regulations/national/china_mainland.md), [Singapore](../../02_standards_regulations/national/singapore.md), [Japan/Korea](../../02_standards_regulations/national/japan_korea.md), [Spain/Portugal/Italy](../../02_standards_regulations/national/spain_portugal_italy.md), [Nordics](../../02_standards_regulations/national/nordics_baltics.md), [NL/BE/LU](../../02_standards_regulations/national/netherlands_belgium_luxembourg.md), [DACH](../../02_standards_regulations/national/germany_austria_switzerland.md), [UK/Ireland](../../02_standards_regulations/national/uk_ireland.md), [Latin America](../../02_standards_regulations/national/latin_america.md), [North America](../../02_standards_regulations/national/north_america.md), [France](../../02_standards_regulations/national/france_francophone.md)), [IFC in real projects](../../01_ifc_basics/00_ifc_in_real_projects.md), [IFC versions and views](../../01_ifc_basics/01_what_is_ifc_and_versions.md), [property sets](../../01_ifc_basics/05_properties_quantities_psets.md), [coordinates and units](../../01_ifc_basics/06_geometry_placement_coordinates_units.md), [Revit IFC export](../../03_software/revit/ifc_export_reference.md), [MCP server catalog](../../04_open_source/mcp_servers_and_ai_tools.md) and the [multilingual glossary](../../08_glossary/glossary_multilingual.md).

### Local words you will meet in the data

| Word | Plain meaning |
|---|---|
| EIR / AIA / capitolato informativo / cahier des charges BIM | The client's list of what information must be delivered |
| BEP / BAP / PEB / piano di gestione informativa | The supplier's plan answering the EIR (not the same as the client's requirement) |
| LOIN (ISO 7817) | Level of information need: geometry + data + documents per object and phase; replaces "LOD" |
| IDS | buildingSMART file that states checkable requirements (applicability + requirements) |
| MVD / view (Coordination View 2.0, Reference View) | A named subset of IFC to export for a purpose |
| IFC+SG, SGPsets | Singapore's extension of IFC for CORENET X submissions |
| SZ-IFC | Shenzhen's local IFC profile for permit filing (own converter plugin and checker) |
| АГР, ТЭП, ТИМ/ЦИМ, КСИ, МССК | Moscow architectural-urban approval, technical-economic indicators, information-modelling technology/model, national construction information classifier, Moscow's own classifier codes |
| BIM図面審査 / BIM data review | Japan: permit drawings produced from a BIM model (since 2026-04) / planned IFC-based automated review |
| CI, oGI, pGI (Italy) | The Italian tender chain: the client's information requirements (CI), the bidder's information-management offer (oGI) and the information-management plan (pGI) |
| POFIN, MMI, NS 8360 (Norway) | National requirement package, model maturity index, process property-set standard |
| NL-SfB, ILS | Dutch classification; Dutch information delivery specification (not the same as buildingSMART IDS) |

## Problem map

Ranked by number of matching records (real + synthetic). Records were hand-grouped; one record can appear in several problems, so the counts overlap and are a signal, not a statistic.

| # | Problem | How users describe it | Frequency signal | Root cause | Typical fix |
|---|---|---|---|---|---|
| 1 | "Will my IFC pass the authority's checker?" (completeness before submission) | “тяжёлая модель выгружается 2 часа, ошибки видно только после загрузки в строимпросто, зоны пропадают, площади…” (ru); “报建前能不能在Revit里先自检，不用每次导出IFC再检测” (zh); “pre-check ifc+sg against COP 3.1 or COP 4 before submitting, select failing elements, export bcf” (en) | 43 rec. (28 real, 15 synth.); zh 16, ru 12, en 9, ja 3 | Every portal has its own mandatory classes, property sets and rules; the official checker is run only after a slow export and upload | Pre-check in the authoring tool or on the IFC (IDS, mapping file), list gaps per class with GlobalId, fix in the source model, re-export; never claim approval |
| 2 | "Is BIM/IFC mandatory for me, since when, above what threshold?" | “da quando e obbligatorio il BIM negli appalti e sopra che soglia? serve per forza l'IFC?” (it); “нужно ли с 01.07.2019 переходить на ТИМ, можно ли работать в 2D и сдавать PDF” (ru); “la maggiorazione del 10% per il BIM vale anche per DL e CSE?” (it) | 41 rec. (41 real, 0 synth.); es 10, zh 10, it 7, en 3 | Rules are local and owner-specific, dates and thresholds change by circular, web summaries disagree, "BIM mandatory" is confused with "IFC mandatory" | Ask jurisdiction, client type, value/area and date; point to the primary source; mark unverified numbers |
| 3 | Local classification codes missing or wrong (КСИ/МССК, NL-SfB, Uniclass, DIN 276, SICLIC) | “в проекте СП модель предъявляется в RVT и DWG, а IFC нет; элементы должны быть…” (ru); “windveer is dakafwerking, NL-SfB code 27 is daarom niet juist, moet 47 zijn (47.12)” (nl); “implemented classification with IfcClassification; is there a guide to use UNICLASS 2015…” (en) | 25 rec. (15 real, 10 synth.); en 8, ru 6, nl 4, no 3 | IFC does not constrain IfcClassification values; each country has its own system and edition; presence is checked, validity often is not | Name system + edition, check presence and validity against the code list, map via IfcClassificationReference |
| 4 | Writing or reading an EIR/AIA/capitolato; which template? | “devo scrivere il capitolato informativo per una gara, cosa metto su formati e livelli di…” (it); “hva er POFIN og kan vi bruke det til å stille krav til informasjonsleveranser?” (no); “material layers are fundamental; the Reference View excludes them so he cannot specify it…” (en) | 24 rec. (19 real, 5 synth.); de 5, en 5, no 4, es 4 | Templates are recommendations, terms differ per country, EIRs omit schema/MVD/pset names, LOD vs LOIN confusion | Name schema identifier + MVD + exporter, property + pset + datatype, LOIN table, attach IDS |
| 5 | Code rules that need geometry (door/stair width, egress, heights, fire compartments) | “While working through accessibility code I see IfcStair has no direct width property…” (en); “new Dynamo user; large warehouses with conveyors and platforms; can Dynamo calculate…” (en); “wants checks IDS cannot express such as free space and accessibility” (en) | 21 rec. (5 real, 16 synth.); en 10, zh 3, ja 2, no 1 | Typical IFC carries no ready value (a stair has no width property; escape routes are not modelled) | Compute from geometry deterministically; PASS/FAIL/UNKNOWN; user supplies clause and threshold |
| 6 | Turning an EIR or regulation into IDS / machine-checkable rules | “EIRs often name a property but not its pset, while IDS requires the pset” (en); “only IfcValve with attribute operational relevant = yes need a field designation…” (en); “перевести нормативку в OWL, SWRL, IDS сложно, без основы получится работа в стол” (ru) | 20 rec. (11 real, 9 synth.); en 10, ru 4, ja 2, fr 1 | EIRs name a property but not its property set; IDS cannot express geometry, clearance or "only new components" filters | State pset + property, use applicability for conditions, keep non-IDS rules as separate geometric checks |
| 7 | Export drops, ignores or renames the fields the authority needs | “深圳SZ-IFC审查项目基点坐标、高差、正北为空，导出丢字段” (zh); “Mapping lines for Pset_WallCommon LoadBearing have no effect; works for other common…” (en); “IfcExportAs=IfcSpace.EXTERNAL becomes NOTDEFINED; mandatory in Chilean public deliveries…” (en) | 14 rec. (14 real, 0 synth.); en 9, zh 3, ru 2 | Built-in parameter wins a name clash; standard Qto sets are fixed; IFC2x3 enums are too small; IfcExportAs not honoured everywhere | Custom pset names, exporter update, IfcPatch/script post-fix, IFC4 where allowed |
| 8 | Room/zone areas do not match the declared figures (ТЭП, floor-area tables) | “площади ТЭП в xml расходятся на 20 м2, дубли не найти, как править IFC без ревита и…” (ru); “部屋名・用途・床面積がIFCに出て別ビューアで読めるか。面積が合わない時は境界・計算方法・単位・版を確認” (ja) | 13 rec. (4 real, 9 synth.); en 4, ru 3, ja 2, zh 2 | Zones vs rooms, duplicates, zones without geometry, different area definitions, attribute vs geometry | Compare attribute vs geometric area per space, detect duplicates, journal fixes by GlobalId |
| 9 | Which IFC version / view is accepted (IFC2x3 vs IFC4 Reference View vs 4.3) | “got IFC0000101 update file to supported IFC version, I exported ifc2x3, how to export…” (en); “формат IFC 2x3 и выше для обмена моделями” (ru) | 12 rec. (8 real, 4 synth.); en 4, ru 4, zh 3, ja 1 | Contracts say "IFC" without version; header is only the exporter's claim; MVDs not interchangeable | Read FILE_SCHEMA and view in the header, compare with the contract, re-export (cannot be repaired by editing) |
| 10 | Portal rejects the file for technical reasons (error codes, text instead of numbers, duplicate GUIDs, size, old checker) | “portal says IfcShapeRepresentation.ContextOfItems is required, code IFC0000104, which…” (en); “ClearWidth is '1000 mm' text and FireRating '1 hr', mapping wants number, how to bulk fix” (en); “1.1.0版本自检通过的模型2024年起传不上去政府报建系统，要更新到1.3.0吗” (zh) | 12 rec. (9 real, 3 synth.); en 6, zh 3, ru 3 | Schema-level defects (missing ContextOfItems), value types, copied GlobalIds, toolchain versions | Locate entities behind the code, targeted repair in a copy, re-validate |
| 11 | Delivery scope: what to hand over, what to strip, COBie vs IFC, partial deliveries | “which parameters should I export for QS, coordination, construction and FM?” (en); “controlling level of information per exchange agreement” (en); “agreed with client to deliver information only for new elements in scope, but mixed…” (en) | 12 rec. (3 real, 9 synth.); en 9, de 1, it 1, es 1 | Exporters write everything; EIR/BEP list is shorter; need-to-know and refurbishment cases | Export only what the BEP lists, filtered copy with backup, verify counts |
| 12 | Coordinates and georeferencing demanded by a portal | “is my ifc georeferenced to SVY21 EPSG 3414, do i need SITEBOUNDARY IfcGeographicElement” (en); “GEO Coordinatiepunt en BIM nulpunt los gedefinieerd, maar samen beschrijven ze dezelfde…” (nl); “深圳SZ-IFC审查项目基点坐标、高差、正北为空，导出丢字段” (zh) | 10 rec. (6 real, 4 synth.); zh 6, en 2, nl 2 | National CRS (SVY21, CGCS2000), several Revit origins, IfcMapConversion only in IFC4+ | Set base point/CRS before export, verify IfcProjectedCRS + IfcMapConversion, check range after unit conversion |
| 13 | Model or drawing: which one counts legally? | “屋宇署：呈交的建築信息模型屬補充資料僅供參考，圖則與模型不一致以圖則為準；提供Revit/ArchiCAD外掛核查樓面面積、衞生設備、消防” (zh); “BIM図面審査では確認申請書+BIM書き出しPDF+同時書き出しIFC+誓約書を提出。IFCは審査対象外。AIはどこまで入る？” (ja); “cosa dicono le linee guida MIT 2026 su ACDat, ruoli e formato IFC? il modello prevale sul…” (it) | 9 rec. (9 real, 0 synth.); zh 6, ja 1, it 1, ru 1 | Legal status of the model differs per country and phase (supplementary, reference, prevailing) | Ask jurisdiction and phase; offer consistency checks, never decide legal precedence |

## Problems in depth

The "assistant" paragraphs describe what a good AI/MCP assistant should do. Facts about thresholds and dates are as reported in the sources and the national reference files; treat them as "verify before relying".

### 1. "Will my IFC pass the checker?" (pre-submission completeness)

**Symptoms in users' words**
- “тяжёлая модель выгружается 2 часа, ошибки видно только после загрузки в строимпросто, зоны пропадают, площади задваиваются” (ru; EN: Heavy model exports IFC in 2 hours and errors only show after upload to the Moscow AGR checker; rooms vs zones, vanished zones, area overcounting; [source](https://habr.com/ru/articles/1089018/))
- “报建前能不能在Revit里先自检，不用每次导出IFC再检测” (zh; EN: Pre-check the model inside Revit before exporting SZ-IFC for Shenzhen filing.; [source](https://zhuanlan.zhihu.com/p/633827596))
- “pre-check ifc+sg against COP 3.1 or COP 4 before submitting, select failing elements, export bcf” (en; [source](https://github.com/OrvenBentleySystems/sg-ifc-microstation-eap))
- “部屋名・用途・床面積がIFCに出て別ビューアで読めるか。面積が合わない時は境界・計算方法・単位・版を確認” (ja; EN: Prepare for 2029 data review by exporting one room to IFC and re-reading it in another viewer; [source](https://note.com/t_note_memo/n/n8903305b00fb))

**Why it happens.** Each authority publishes its own list. Singapore: IFC+SG data structure, Excel mapping file and a Model Checker with a schema layer and a quality layer. Moscow AGR: Habr write-ups say IFC conforming to IDS is required; the start date is reported differently by different sources, so treat it as unverified. Shenzhen: a converter plugin plus an official checker (old checker versions stopped being accepted from 2024). Japan: since April 2026 BIM drawing review, with IFC attached for reference only. The official checkers are black boxes run only after upload, and a heavy Revit model can take minutes to hours to export, so people loop "export, upload, read errors, fix, export again" ([source](https://habr.com/ru/companies/pik_digital/articles/1057314/)).

**What fixes it.** Check inside the authoring tool before exporting (one team validates the RVT against IDS with a mapping file in about 30 minutes), run a small test export (one room or level) and read it in another viewer, and scan the IFC for the mandatory items.

**A good assistant** runs a completeness scan (class, property set, classification, storey, base point), groups the gaps per IFC class with counts, GlobalId and storey, says clearly that this is a data pre-check and not approval, and does not invent authority-specific rules it was not given.

**Clarifying questions.** Which authority/portal and which stage (planning, construction permit, completion)? Which checker or rule-set edition? Do you have the official mapping file / IDS, or should I only check generic completeness? Report only, or also write a repaired copy?

### 2. "Is BIM or IFC mandatory for me, since when, above what threshold?"

**Symptoms in users' words**
- “da quando e obbligatorio il BIM negli appalti e sopra che soglia? serve per forza l'IFC?” (it; EN: When is BIM mandatory in Italian public procurement (over 2 million euro, from 1 Jan 2025) and which open format is required?; [source](https://biblus.acca.it/nuovo-codice-appalti-il-bim-e-obbligatorio/))
- “нужно ли с 01.07.2019 переходить на ТИМ, можно ли работать в 2D и сдавать PDF” (ru; EN: Since 01.07.2019 BIM is required?; can we keep 2D and PDF? Is IFC the format?; [source](https://forum.dwg.ru/showthread.php?t=153428))
- “深圳哪些项目要用SZ-IFC报建，几个阶段提交” (zh; EN: Shenzhen SJG114-2022 SZ-IFC: projects over 10M yuan and 1,000 m2 must apply BIM from 2023; models submitted at planning, construction permit…; [source](https://zjj.sz.gov.cn/attachment/0/678/678888/7768421.pdf))
- “in gara serve per forza l'oGI? se non la presento vengo escluso?” (it; EN: Is the offerta di gestione informativa (oGI) mandatory in BIM tenders? (Consiglio di Stato 6834/2026); [source](https://biblus.acca.it/notizie/appalti-bim-lofferta-di-gestione-informativa-e-obbligatoria/))
- “What does South Africa's national BIM strategy require, and does it name IFC or any standard?” (en; [source](https://www.cidb.org.za/innovation/cidb-bim-adoption-strategy/))

**Why it happens.** Rules are local and they move. As reported in the sources: Italy requires BIM above EUR 2 million for new works since 1 January 2025 and names *open non-proprietary formats* (IFC ISO 16739 as reference), not "IFC" as law; Spain's Plan BIM starts for high-value public contracts from April 2024 (EUR 5.538 million in one article); Hong Kong's roadmap tentatively makes BIM submission mandatory in 2029; Shenzhen applies to projects over CNY 10 million and 1,000 m2 from 2023 (per a third-party summary of the standard; verify); German AIA/BAP templates are recommendations; Peru's decree date is "unverified". Singapore articles that say "30,000 m2 from 1 October 2025" are superseded by the 23 July 2026 circular (5,000 m2 from 1 October 2026) according to [the Singapore file](../../02_standards_regulations/national/singapore.md). Also, "BIM required" (a process) is not "IFC required" (a file), and the requirement often sits in the tender documents, not in the law.

**What fixes it.** A primary source per jurisdiction, with date. In China, the city (Guangzhou, Nanjing, Shenzhen, Shanghai) matters more than the country.

**A good assistant** does not answer thresholds and dates from memory with confidence. It states what the knowledge base says, the date of that statement, and that it must be verified; it separates three questions: is BIM required, is an open format required, which IFC version/view.

**Clarifying questions.** Country and city? Public or private client? Contract value or floor area? When was the tender/permit application filed? Are you designer or contractor (in Italy the requirement can sit with the group)?

### 3. Local classification codes (КСИ, NL-SfB, Uniclass, DIN 276, SICLIC)

**Symptoms in users' words**
- “в проекте СП модель предъявляется в RVT и DWG, а IFC нет; элементы должны быть классифицированы” (ru; EN: Draft national BIM standard recognizes RVT and DWG as model formats, not IFC?; [source](https://forum.dwg.ru/showthread.php?t=134394&page=33))
- “windveer is dakafwerking, NL-SfB code 27 is daarom niet juist, moet 47 zijn (47.12)” (nl; EN: Windveer is roof finishing so NL-SfB code 27 is wrong, should be 47.12; [source](https://github.com/Aedes-datastandaarden/ILS-woco/issues/2))
- “implemented classification with IfcClassification; is there a guide to use UNICLASS 2015 properly, ideally sample IFC, and an existing mapping table?” (en; [source](https://forums.buildingsmart.org/t/uniclass-2015-and-ifc/4423))
- “Uniformat is irrelevant in many markets; we use Assembly Code with a custom classification file; need Uniformat suppressed. Tested in DEU UI, 'Baugruppenkennzeichen' does not work” (en; [source](https://github.com/Autodesk/revit-ifc/issues/856))
- “verify that NL-SfB codes in the model are valid, not merely present” (en; [source](https://github.com/OpenAEC-Foundation/OpenAEC-BIM-validator/issues/22))

**Why it happens.** IFC does not constrain the values of `IfcClassification`, so the same thing is written differently by different exports; every country has its own system and edition (КСИ/МССК in Russia, NL-SfB in the Netherlands, Uniclass 2015 in the UK, DIN 276 Kostengruppe in Germany, SICLIC in Brazil, NS 3451/MMI in Norway). Mappings between systems are not one-to-one. In Revit the *Assembly Code* field assumes Uniformat and Uniformat is still written when another system is used. Presence of a code is easy to check; validity against the official list is a separate, often missing check.

**What fixes it.** Attach `IfcClassificationReference` with the right source and edition, use a custom classification file for Assembly Code, validate the code against the list; dictionaries can be published through bSDD (the SICLIC dictionary needed activating out of Demo mode, [source](https://community.osarch.org/discussion/3680/bsdd-dictionaries)).

**A good assistant** asks which system and edition, reports three states (no reference, reference from another system, code not in the list), groups by IFC class, and does not invent mappings between systems.

**Clarifying questions.** Which classification system, edition and table (Ss/Pr for Uniclass)? Where is the code list? Presence only, or validity too? Classification on the occurrence or on the type?

### 4. Writing or reading an EIR / AIA / capitolato

**Symptoms in users' words**
- “devo scrivere il capitolato informativo per una gara, cosa metto su formati e livelli di dettaglio?” (it; EN: How to write a capitolato informativo (EIR) with open data formats and ISO 19650 CDE.; [source](https://biblus.acca.it/capitolato-informativo-come-redigerlo-con-la-metodologia-bim/))
- “hva er POFIN og kan vi bruke det til å stille krav til informasjonsleveranser?” (no; EN: What is POFIN and can I use it to set openBIM requirements in a contract?; [source](https://www.buildingsmart.no/pofin.html))
- “tabla que asocia parámetro con atributo IFC, Pset y propiedad, requerido u opcional, exportación automática o 'a ingresar'” (es; EN: Planbim information matrix v3.0 maps each parameter to IFC attribute, Pset, property, required/optional, auto/manual export, COBie; [source](https://planbim.cl/documentos/mide/))
- “material layers are fundamental; the Reference View excludes them so he cannot specify it in contracts” (en; [source](https://forums.buildingsmart.org/t/3638))
- “how will the upcoming ISO 7817-3 level-of-information-need schema relate to IDS?” (en; [source](https://forums.buildingsmart.org/t/5533))

**Why it happens.** Good templates exist (German Muster-AIA/BAP as recommendations, Norway's POFIN 1.0 with 14 documents and 2 spreadsheets, Chile's Planbim information matrix that maps each parameter to an IFC attribute, Pset and property, the UK IMI framework, Korean procurement guidelines), but they must be adapted. Typical weaknesses: the EIR says only "IFC" or "AIM compatible", names a property but not its property set, mixes the client's requirement with the supplier's plan (EIR vs BEP), or asks for a Reference View deliverable with material layers although that view excludes them.

**What fixes it.** Name the schema identifier, MVD and exporter version; give property + pset + data type; use a LOIN table instead of "LOD 300"; attach an IDS; fix coordinates and classification ([clause patterns](../../02_standards_regulations/requirements_in_contracts_eir_bep.md)).

**A good assistant** reads what the delivered IFC actually contains and compares it with the requirement the user pasted; it drafts requirement wording as a checklist, offers to turn it into IDS, and points out ambiguity (property without pset, no schema). It does not invent clause numbers or claim that a template is mandatory.

**Clarifying questions.** Are you the client or the supplier? Which national template? Which use (coordination, quantities, FM)? Which IFC version and view? Should the output be a checklist, an IDS or plain clauses?

### 5. Code rules that need geometry (widths, egress, heights, compartments)

**Symptoms in users' words**
- “While working through accessibility code I see IfcStair has no direct width property; suggest Width/StairWidth in Pset_StairCommon to support rule-based compliance checks.” (en; [source](https://github.com/buildingSMART/IFC4.x-development/issues/976))
- “model_summary, check_door_widths(min 850), run_rules, export_issues” (en; [source](https://github.com/zeussilver/bim-ifc-mcp))
- “new Dynamo user; large warehouses with conveyors and platforms; can Dynamo calculate egress distance from any point on a platform to nearest ground-floor exit; any generic script” (en; [source](https://forum.dynamobim.com/t/exit-access-travel-distance/115179))
- “wants checks IDS cannot express such as free space and accessibility” (en; [source](https://github.com/OpenAEC-Foundation/OpenAEC-BIM-validator/issues/20))

**Why it happens.** The IFC a client receives rarely contains the number the rule needs. An `IfcStair` has no width property (the maintainer prefers geometric rule checking), escape routes and fire compartments are not modelled objects, "clear width" differs from the door's overall width, and clearance or accessibility rules cannot be written as IDS.

**What fixes it.** Compute from geometry deterministically, state which property or method was used, keep the threshold and clause as input from the user, and return PASS / FAIL / UNKNOWN rather than a guess. A published design rule for such tools is "model proposes, code executes" ([source](https://github.com/zeussilver/bim-ifc-mcp)).

**A good assistant** never estimates numbers, reports unknowns separately, states units, and says that the legal threshold is the user's, not something it verified.

**Clarifying questions.** Which code and clause, which threshold? Which door/stair property counts (overall width, clear width, geometry)? How are escape routes identified (spaces, zone, naming, drawn)? Should missing values be UNKNOWN or computed from geometry?

### 6. Turning requirements into IDS (and what IDS cannot do)

**Symptoms in users' words**
- “EIRs often name a property but not its pset, while IDS requires the pset” (en; [source](https://github.com/buildingSMART/IDS/issues/189))
- “only IfcValve with attribute operational relevant = yes need a field designation; IfcClass alone can't separate them” (en; [source](https://github.com/buildingSMART/IDS/issues/176))
- “agreed with client to deliver information only for new elements in scope, but mixed elements (old wall with new void) cannot be split; wants a global filter across all IDS specs on a project pset…” (en; [source](https://community.osarch.org/discussion/2969/filtering-new-building-components-in-ids-for-refurbishment-projects))
- “発注者の要求がExcelやPDFでバラバラで、納品IFCのチェックが人力。IDSで機械的に検証できる？” (ja; EN: What power does IDS give for operating IFC correctly (clients checking contractor IFC automatically)?; [source](https://zenn.dev/miyamiyaumya/articles/6714ef2c6e2c6c))
- “перевести нормативку в OWL, SWRL, IDS сложно, без основы получится работа в стол” (ru; EN: Turning human-readable regulations into machine-readable form (OWL, SWRL, IDS) is hard and may become 'work for the drawer'; [source](https://t.me/s/ifc_ru))

**Why it happens.** IDS 1.0 (official since June 2024) states *applicability* (which elements) and *requirements* (what they must have) with six facets: entity, attribute, property, classification, material, part-of. The property facet needs the property set name, but UK EIR templates name only the property. An AND condition across attributes ("only valves with operational relevant = yes") must be put into applicability. IDS cannot check geometry, clashes, clearance or accessibility, and covers only the alphanumeric part of LOIN. Refurbishment ("deliver data only for new components") needs a filter that is awkward in IDS. Translating prose regulation into OWL/SWRL/IDS is hard.

**What fixes it.** Ask for pset + property + type; split rules into IDS-checkable and geometry-checkable; keep the IDS small and testable; remember that a specification with no matching elements may be reported as skipped, not failed ([source](https://github.com/IfcOpenShell/IfcOpenShell/issues/9112); see also the [programming file](programming_and_automation.md)).

**A good assistant** drafts IDS from a pasted requirement, shows the facets it used, flags what could not be expressed, and runs the check if a validator tool exists. It does not call a model compliant because the IDS passed on zero matched elements.

**Clarifying questions.** Which pset holds the property? Required, optional or prohibited? Only new elements, or all? Which IFC version (property names differ)? Who receives the failure list?

### 7. Export drops, ignores or renames the required fields

**Symptoms in users' words**
- “深圳SZ-IFC审查项目基点坐标、高差、正北为空，导出丢字段” (zh; EN: Shenzhen SZ-IFC review tool shows empty base-point values after export.; [source](https://zhuanlan.zhihu.com/p/673078056))
- “Mapping lines for Pset_WallCommon LoadBearing have no effect; works for other common properties.” (en; [source](https://github.com/Autodesk/revit-ifc/issues/833))
- “Czech-named shared parameters (Objem, Plocha) in user-defined pset are replaced by built-in Volume/Area values despite mapping file.” (en; [source](https://github.com/Autodesk/revit-ifc/issues/989))
- “IfcExportAs=IfcSpace.EXTERNAL becomes NOTDEFINED; mandatory in Chilean public deliveries; manual text edit workaround” (en; [source](https://github.com/Autodesk/revit-ifc/issues/247))
- “косоуры всё равно выгружаются при IfcExportAs нет, пандус уходит как IfcRampFlight, МССК коды помещениям вручную” (ru; EN: Preparing a model for AGR: each element needs IFC class and attributes; stair stringers still export when set to No; ramp as IfcRampFlight needs…; [source](https://habr.com/ru/articles/1098340/))

**Why it happens.** In the Revit exporter a built-in parameter beats a shared parameter with the same name (so a custom `LoadBearing` cannot override `Pset_WallCommon.LoadBearing`; tracked internally, open), the standard `Qto_*` sets are fixed by design, the IFC2x3 space enumeration has only USERDEFINED/NOTDEFINED so `IfcSpace.EXTERNAL` becomes NOTDEFINED ("by design", although a Chilean public delivery required it), Uniformat is written whenever Assembly Code is filled, localized parameter names fail, and `IfcExportAs` set to No does not stop some elements (stair stringers) from exporting. Empty review nodes in the Shenzhen checker are read by users as "fields lost during export"; the suggested remedies (reinstall, export on another machine) are anecdotal. See [Revit export reference](../../03_software/revit/ifc_export_reference.md).

**What fixes it.** Use custom pset names that do not clash with built-ins, full `Pset_X.Property` names in the mapping, the latest exporter, post-processing of the IFC (a script or IfcPatch recipe), and IFC4 where the authority permits it.

**A good assistant** separates three layers: the authoring model, the export setting and the IFC file. With only an IFC loaded it cannot see Revit parameters or `IfcExportAs`, and should say so instead of guessing; it should not promise that editing the IFC satisfies an authority that wants a native export.

**Clarifying questions.** Revit and IFC exporter version? IFC version? Which property set and property name does the authority expect? Is the value empty in Revit or missing in the IFC?

### 8. Areas and rooms that do not match the declared figures

**Symptoms in users' words**
- “площади ТЭП в xml расходятся на 20 м2, дубли не найти, как править IFC без ревита и переслать правки” (ru; EN: TEP areas differ ~20 m2 from AGR XML; duplicates hard to find; how to post-process IFC without Revit and share fixes without resending big files; [source](https://habr.com/ru/articles/1100956/))
- “тяжёлая модель выгружается 2 часа, ошибки видно только после загрузки в строимпросто, зоны пропадают, площади задваиваются” (ru; EN: Heavy model exports IFC in 2 hours and errors only show after upload to the Moscow AGR checker; rooms vs zones, vanished zones, area overcounting; [source](https://habr.com/ru/articles/1089018/))
- “部屋名・用途・床面積がIFCに出て別ビューアで読めるか。面積が合わない時は境界・計算方法・単位・版を確認” (ja; EN: Prepare for 2029 data review by exporting one room to IFC and re-reading it in another viewer; [source](https://note.com/t_note_memo/n/n8903305b00fb))

**Why it happens.** Authorities compare `IfcSpace` data with declared figures (technical-economic indicators in XML for Moscow; room name, use and floor area for Japan). Typical causes: rooms mixed up with zones, duplicates invisible in 3D, zones without solid geometry, a different area definition (boundary, calculation method, unit, version), and a custom attribute (`RUS_Area`) that differs from the geometric area.

**What fixes it.** Compare the declared area with the geometric area per space within a tolerance, detect duplicates (for example by bounding box), and keep a change journal keyed by GlobalId so fixes can be sent without resending a huge file.

**A good assistant** shows both numbers per space with the method, separates `Qto_SpaceBaseQuantities` (NetFloorArea/GrossFloorArea) from custom attributes, flags spaces without geometry, and asks which area definition the authority uses.

**Clarifying questions.** Net, gross or authority-specific area? Which attribute holds the declared value? Tolerance? Rooms or zones?

### 9. Which IFC version and view is accepted

**Symptoms in users' words**
- “got IFC0000101 update file to supported IFC version, I exported ifc2x3, how to export ifc4 with IFC+SG settings” (en; [source](https://github.com/noddlesskcho/IFC-Repair-Studio))
- “формат IFC 2x3 и выше для обмена моделями” (ru; EN: SP 333 recommends exchanging digital models in IFC 2x3 or higher and requires elements to be classified and uniquely identified; [source](http://docs.cntd.ru/document/556793897))
- “в проекте СП модель предъявляется в RVT и DWG, а IFC нет; элементы должны быть классифицированы” (ru; EN: Draft national BIM standard recognizes RVT and DWG as model formats, not IFC?; [source](https://forum.dwg.ru/showthread.php?t=134394&page=33))
- “検定対象ソフトはMVDに合致する必要。結果は管理台帳とサイトで公表” (ja; EN: buildingSMART Japan IFC certification (IFC検定): software must conform to an MVD; [source](https://www.building-smart.or.jp/ifc/whatsifcverifi/))

**Why it happens.** Contracts say "IFC" without a version. Singapore requires IFC4 Reference View (IFC0000101 means unsupported version *or* view). Japan's verification targets a view that may not match a Revit IFC4 export. Russian SP 333 says "IFC 2x3 or higher". The `FILE_SCHEMA` header is the exporter's claim, not proof, and "IFC4" in contracts normally means IFC4 ADD2 TC1 ([versions](../../01_ifc_basics/01_what_is_ifc_and_versions.md)). Coordination View 2.0 and Reference View are not interchangeable.

**What fixes it.** Read the header, compare with the contract, and re-export; a wrong version cannot be repaired by editing the file.

**A good assistant** reports the schema identifier and view claim with that caveat, does not silently convert, and mentions that IFC4.3 is generally not mandated.

**Clarifying questions.** Which version and view does the contract or portal name? Which exporter and version produced the file? Do you also need the native file?

### 10. The portal rejects the file for technical reasons

**Symptoms in users' words**
- “portal says IfcShapeRepresentation.ContextOfItems is required, code IFC0000104, which shape and how to fix without re-exporting” (en; [source](https://github.com/noddlesskcho/IFC-Repair-Studio))
- “ClearWidth is '1000 mm' text and FireRating '1 hr', mapping wants number, how to bulk fix” (en; [source](https://github.com/LUOaini1213/ifcsg-precheck))
- “1.1.0版本自检通过的模型2024年起传不上去政府报建系统，要更新到1.3.0吗” (zh; EN: Models passed with self-check tool 1.1.0 can no longer be uploaded to the Shenzhen filing system from 2024-01-01; update to 1.3.0.; [source](https://zhuanlan.zhihu.com/p/672903162))
- “SZ-IFC转换和自检遇到构件偏移、信息缺失、文件大、各软件读取不一致、转换慢” (zh; EN: Notes from a product manager on SZ-IFC: offsets, missing info, big files, viewer differences, slow conversion, coordinate rules.; [source](https://www.sunyuanrui.com/works/sz-ifc-research/))

**Why it happens.** Singapore's Model Checker reports schema errors by code (IFC0000001 unreadable, 101 unsupported version/view, 102 no IfcSite, 103 non-standard or abstract entities, 104 invalid or incomplete data, 106 no valid IfcProject). Other causes: values stored as text (`'1000 mm'`, `'1 hr'`) where a number is expected, copied GlobalIds in blocks or templates, a checker version that is no longer accepted, files over a size limit (limits quoted in the sources, such as 500 MB for Moscow or 2 GB for Singapore, come from secondary summaries: unverified).

**What fixes it.** Find the exact entities behind the code (for example the shape with no `ContextOfItems`), repair in a copy (link the shape to the single matching context; if zero or several match, only report), convert text to numbers with the unit carried separately, regenerate duplicate GlobalIds, update the toolchain.

**A good assistant** locates and lists the offenders (GlobalId, name, class), proposes fixes without deleting elements, keeps the original, and re-validates after the change.

**Clarifying questions.** Exact error code and message? Portal and checker version? May I write a repaired copy? Is deleting an element ever acceptable?

### 11. Delivery scope: what to hand over, what to strip

**Symptoms in users' words**
- “which parameters should I export for QS, coordination, construction and FM?” (en; [source](https://bimcorner.com/ifc-export-rules-part-2-what-parameters-to-export-dos-and-donts/))
- “controlling level of information per exchange agreement” (en; [source](https://github.com/specklesystems/speckle-sharp/issues/1778))
- “agreed with client to deliver information only for new elements in scope, but mixed elements (old wall with new void) cannot be split; wants a global filter across all IDS specs on a project pset…” (en; [source](https://community.osarch.org/discussion/2969/filtering-new-building-components-in-ids-for-refurbishment-projects))

**Why it happens.** Exporters write everything unless told otherwise, while the EIR/BEP asks for a shorter list; some projects need need-to-know filtering per exchange or data only for new components (refurbishment). Handover for FM raises "COBie or IFC with property sets?" and whether the EIR's "AIM compatible" is specific enough.

**What fixes it.** Export only the parameters listed in the BEP, no schedules or legends, a key that links FM data to an external database; make a filtered copy and keep the original.

**A good assistant** treats stripping data as destructive: writes a new file, confirms the keep-list first, reports counts before/after, and does not delete anything the user did not list.

**Clarifying questions.** Which document is the keep-list (EIR, BEP, IDS)? Remove or hide? Is the original archived? Do you want COBie as well?

### 12. Coordinates and georeferencing demanded by a portal

**Symptoms in users' words**
- “is my ifc georeferenced to SVY21 EPSG 3414, do i need SITEBOUNDARY IfcGeographicElement” (en; [source](https://github.com/chunyen93/ifcgref-corenetx))
- “GEO Coordinatiepunt en BIM nulpunt los gedefinieerd, maar samen beschrijven ze dezelfde transformatie als IfcMapConversion: translatie op het GEO punt, rotatie tussen beide punten” (nl; EN: GEO coordination point and BIM origin are defined separately but together equal IfcMapConversion; clarify their relationship; [source](https://github.com/nl-digigo/GeoBIM_Georefereren/issues/5))
- “深圳SZ-IFC审查项目基点坐标、高差、正北为空，导出丢字段” (zh; EN: Shenzhen SZ-IFC review tool shows empty base-point values after export.; [source](https://zhuanlan.zhihu.com/p/673078056))
- “positie van aspectmodellen ten opzichte van het nulpunt coordineren; nulpunt buiten het gebouw; referentieobject 100% overlappend” (nl; EN: Coordinate aspect models relative to an origin placed outside the building; optional reference object; geo-reference as model property; [source](https://www.digigo.nu/ilsen-en-richtlijnen/bim-basis-ils/3-2-lokale-positie))

**Why it happens.** National systems are specified (SVY21 / EPSG:3414 and Singapore Height Datum; CGCS2000 for Shenzhen), Dutch rules describe a GEO coordination point plus a BIM zero point that together equal IFC's `IfcMapConversion`, and Revit has three origins (project base point, survey point, internal origin). `IfcMapConversion`/`IfcProjectedCRS` exist only in IFC4 and later ([coordinates](../../01_ifc_basics/06_geometry_placement_coordinates_units.md)).

**What fixes it.** Set the base point and CRS before export; verify the CRS name, eastings/northings, rotation and that the position lies inside the national range *after* unit conversion.

**A good assistant** reads `IfcMapConversion`, `IfcProjectedCRS`, site placement and true north, notes that IFC2x3 has no map-conversion entity, checks plausibility against the region, and does not move geometry to "fix" a position without confirmation.

**Clarifying questions.** Target CRS and vertical datum (EPSG code)? Which Revit origin is the project zero? Is the file IFC2x3 or IFC4?

### 13. Model or drawing: which one counts?

**Symptoms in users' words**
- “屋宇署：呈交的建築信息模型屬補充資料僅供參考，圖則與模型不一致以圖則為準；提供Revit/ArchiCAD外掛核查樓面面積、衞生設備、消防” (zh; EN: HK Buildings Department: submitted BIM models are supplementary only; drawings prevail; plug-ins check GFA, sanitary, fire safety; Revit IFC export…; [source](https://www.bd.gov.hk/tc/resources/online-tools/building-information-modelling/index.html))
- “BIM図面審査では確認申請書+BIM書き出しPDF+同時書き出しIFC+誓約書を提出。IFCは審査対象外。AIはどこまで入る？” (ja; EN: BIM drawing review (Apr 2026) vs BIM data review (spring 2029): what is submitted and how IFC is used; [source](https://note.com/kensesu_ai/n/nee08ddde31f1))
- “cosa dicono le linee guida MIT 2026 su ACDat, ruoli e formato IFC? il modello prevale sul 2D?” (it; EN: What do the 2026 MIT guidelines on digital information management (GID) require: roles, ACDat, formats, model prevailing over 2D?; [source](https://biblus.acca.it/linee-guida-bim-2026-per-le-stazioni-appaltanti/))
- “施工图审查要同时上传二维图纸和BIM模型吗” (zh; EN: Guangzhou trial of BIM-assisted construction drawing review: upload 2D drawings and BIM model together; owner confirms consistency.; [source](https://zfcj.gz.gov.cn/gkmlpt/content/6/6434/post_6434530.html))

**Why it happens.** Legal status differs by country and phase: Hong Kong treats submitted models as supplementary (drawings prevail); Japan's current phase treats IFC as reference with PDFs as the document, and data review is planned for 2029 (dates from a vendor page); Italy's guidelines say the model prevails over 2D unless declared otherwise; the Guangzhou trial required uploading both and the owner confirming consistency, with advisory results during the trial; Singapore's 3D models take precedence unless the cover letter says otherwise.

**What fixes it.** Ask the jurisdiction and phase; offer consistency checks between model and drawing tables (areas, heights, storey list).

**A good assistant** never states which document is legally authoritative without a source for that jurisdiction, and offers to compare model figures with the drawing's area table instead.

**Clarifying questions.** Jurisdiction and permit stage? Which drawing table should the model match? Is the review advisory or binding in your case?

## Real questions

All rows are real, observed at the linked source and paraphrased in the original language (no usernames). "EN gloss" is shown for non-English rows. A few records tagged with a non-English language carry an English paraphrase in the dataset; they are shown as stored.

| lang | question (original-language paraphrase) | EN gloss | persona | source |
|---|---|---|---|---|
| ru | с 01.07.2019 госэкспертиза требует BIM, как проверять проект в Revit или IFC, можно ли PDF и чертежи, как быть с 87 постановлением, методики нет | From 1 July 2019 state expertise reportedly requires BIM; how do we check a Revit project or IFC model, can PDF drawings be used instead? | bim coordinator | [forum.dwg.ru](https://forum.dwg.ru/showthread.php?t=153428) |
| ru | тяжёлая модель выгружается 2 часа, ошибки видно только после загрузки в строимпросто, зоны пропадают, площади задваиваются | Heavy model exports IFC in 2 hours and errors only show after upload to the Moscow AGR checker; rooms vs zones, vanished zones, area overcounting | bim coordinator | [habr.com](https://habr.com/ru/articles/1089018/) |
| ru | экспорт в IFC занимает от минут до часов, ошибки находим итерациями, у окон нет параметра RUS_Height | Since 2 April 2026 IFC conforming to IDS is required for MGE/AGR; every check needs a full slow export | bim manager | [habr.com](https://habr.com/ru/companies/pik_digital/articles/1057314/) |
| ru | площади ТЭП в xml расходятся на 20 м2, дубли не найти, как править IFC без ревита и переслать правки | TEP areas differ ~20 m2 from AGR XML; duplicates hard to find; how to post-process IFC without Revit and share fixes without resending big files | bim coordinator | [habr.com](https://habr.com/ru/articles/1100956/) |
| ru | косоуры всё равно выгружаются при IfcExportAs нет, пандус уходит как IfcRampFlight, МССК коды помещениям вручную | Preparing a model for AGR: each element needs IFC class and attributes; stair stringers still export when set to No; ramp as IfcRampFlight needs another classifier code | bim coordinator | [habr.com](https://habr.com/ru/articles/1098340/) |
| ru | перевести нормативку в OWL, SWRL, IDS сложно, без основы получится работа в стол | Turning human-readable regulations into machine-readable form (OWL, SWRL, IDS) is hard and may become 'work for the drawer' | researcher academic | [t.me](https://t.me/s/ifc_ru) |
| ru | нужно ли с 01.07.2019 переходить на ТИМ, можно ли работать в 2D и сдавать PDF | Since 01.07.2019 BIM is required?; can we keep 2D and PDF? Is IFC the format? | architect | [forum.dwg.ru](https://forum.dwg.ru/showthread.php?t=153428) |
| ru | в проекте СП модель предъявляется в RVT и DWG, а IFC нет; элементы должны быть классифицированы | Draft national BIM standard recognizes RVT and DWG as model formats, not IFC? | bim manager | [forum.dwg.ru](https://forum.dwg.ru/showthread.php?t=134394&page=33) |
| ru | формат IFC 2x3 и выше для обмена моделями | SP 333 recommends exchanging digital models in IFC 2x3 or higher and requires elements to be classified and uniquely identified | reviewer authority | [docs.cntd.ru](http://docs.cntd.ru/document/556793897) |
| ru | новые BIM-требования в формате IDS | Mosoblexpertiza published new BIM requirements in IDS format for roads, utilities and buildings | reviewer authority | [t.me](https://t.me/s/ifc_ru) |
| zh | 报建前能不能在Revit里先自检，不用每次导出IFC再检测 | Pre-check the model inside Revit before exporting SZ-IFC for Shenzhen filing. | bim coordinator | [zhuanlan.zhihu.com](https://zhuanlan.zhihu.com/p/633827596) |
| zh | 1.1.0版本自检通过的模型2024年起传不上去政府报建系统，要更新到1.3.0吗 | Models passed with self-check tool 1.1.0 can no longer be uploaded to the Shenzhen filing system from 2024-01-01; update to 1.3.0. | bim manager | [zhuanlan.zhihu.com](https://zhuanlan.zhihu.com/p/672903162) |
| zh | 自检工具里审查节点有些值是空的，导出IFC丢字段了怎么办 | Some review node values are empty in the self-check tool, meaning fields were lost during IFC export. | bim coordinator | [blog.csdn.net](https://blog.csdn.net/weixin_42855822/article/details/139867051) |
| zh | 哪些项目要同步提交BIM模型做规划报批 | Guangzhou trial of BIM electronic planning approval: submit BIM model with planning technical review for gov projects over 20,000 m2, prefab, key zones, from 2020-10-01. | reviewer authority | [gz.gov.cn](https://www.gz.gov.cn/xw/tzgg/content/post_6469259.html) |
| zh | 施工图审查要同时上传二维图纸和BIM模型吗 | Guangzhou trial of BIM-assisted construction drawing review: upload 2D drawings and BIM model together; owner confirms consistency. | reviewer authority | [zfcj.gz.gov.cn](https://zfcj.gz.gov.cn/gkmlpt/content/6/6434/post_6434530.html) |
| zh | 设计师聊广州BIM审查，导GDB、改模型再导第二版 | Designers share what Guangzhou BIM review is like: export per-discipline GDB, expert comments, revise model, re-export version two. | architect | [zhuanlan.zhihu.com](https://zhuanlan.zhihu.com/p/504617257) |
| zh | 南京BIM规划报建要交原生模型和宁建模轻量化文件吗 | Nanjing BIM planning submission: from 2021-03-01 in pilot zones, projects submit native BIM plus lightweight 宁建模 file after QC; free aided-design software. | reviewer authority | [ghj.nanjing.gov.cn](http://ghj.nanjing.gov.cn/njsgtzyj/202103/t20210301_2834720.html) |
| zh | 上海审查用EDM还是IFC | Shanghai BIM smart-review modeling manual: EDM data file for architecture/MEP review, IFC for structural load review. | reviewer authority | [zjw.sh.gov.cn](https://zjw.sh.gov.cn/cmsres/4a/4a7bc95634cd4852b2399e57e9c692dd/a646541bab5ad86dc1684d1126e21e29.pdf) |
| zh | 深圳哪些项目要用SZ-IFC报建，几个阶段提交 | Shenzhen SJG114-2022 SZ-IFC: projects over 10M yuan and 1,000 m2 must apply BIM from 2023; models submitted at planning, construction permit, completion. | reviewer authority | [zjj.sz.gov.cn](https://zjj.sz.gov.cn/attachment/0/678/678888/7768421.pdf) |
| zh | 屋宇署：呈交的建築信息模型屬補充資料僅供參考，圖則與模型不一致以圖則為準；提供Revit/ArchiCAD外掛核查樓面面積、衞生設備、消防 | HK Buildings Department: submitted BIM models are supplementary only; drawings prevail; plug-ins check GFA, sanitary, fire safety; Revit IFC export text file provided. | reviewer authority | [bd.gov.hk](https://www.bd.gov.hk/tc/resources/online-tools/building-information-modelling/index.html) |
| zh | 上海试行BIM智能辅助审查，设计单位要导出什么格式 | Shanghai from 2024-02-01 trials BIM-assisted review (EDM format; IFC to be explored) | reviewer authority | [zhuanlan.zhihu.com](https://zhuanlan.zhihu.com/p/676069996) |
| zh | 深圳SZ-IFC审查项目基点坐标、高差、正北为空，导出丢字段 | Shenzhen SZ-IFC review tool shows empty base-point values after export. | bim coordinator | [zhuanlan.zhihu.com](https://zhuanlan.zhihu.com/p/673078056) |
| ja | 発注者の要求がExcelやPDFでバラバラで、納品IFCのチェックが人力。IDSで機械的に検証できる？ | What power does IDS give for operating IFC correctly (clients checking contractor IFC automatically)? | bim manager | [zenn.dev](https://zenn.dev/miyamiyaumya/articles/6714ef2c6e2c6c) |
| ja | BIM図面審査では確認申請書+BIM書き出しPDF+同時書き出しIFC+誓約書を提出。IFCは審査対象外。AIはどこまで入る？ | BIM drawing review (Apr 2026) vs BIM data review (spring 2029): what is submitted and how IFC is used | reviewer authority | [note.com](https://note.com/kensesu_ai/n/nee08ddde31f1) |
| ja | 国交省の基本構想では採光・換気、容積率、建蔽率、斜線など約10項目から。構造・省エネは検討中 | MLIT 2029 BIM data review: view review vs digital review, initial ~10 review items | reviewer authority | [note.com](https://note.com/ken_newslab/n/n9d7072936346) |
| ja | 部屋名・用途・床面積がIFCに出て別ビューアで読めるか。面積が合わない時は境界・計算方法・単位・版を確認 | Prepare for 2029 data review by exporting one room to IFC and re-reading it in another viewer | architect | [note.com](https://note.com/t_note_memo/n/n8903305b00fb) |
| ja | 個人開発のBIMCraft(MCP/CLI操作可)は審査用IFCに使えるか。RVTは読み取りのみ、カーテンウォールや階段は未対応 | Can the free Rust BIM app BIMCraft handle the 2029 review IFC? Reads IFC2x3/IFC4, writes IFC4 | owner client | [note.com](https://note.com/legal_tiger6680/n/n6781ba815061) |
| ja | 準一級・一級の実技で、審査フローに沿ってモデル作成、図面抽出、面積算定、IFCと図面の提出 | BIM利用技術者 exams: practical tasks include submitting IFC with drawings; IFC2x3 from FY2026 | student beginner | [note.com](https://note.com/aei830/n/ndfa486486036) |
| ko | IFC와 openBIM이 뭐고 왜 국제표준을 도입해야 하나 | What are IFC and openBIM, and why should Korea adopt international standards? | student beginner | [buildingsmart.or.kr](https://www.buildingsmart.or.kr/Home/BimOverview) |
| ko | 조달청 시설사업 BIM 적용 기본지침서 | PPS (Public Procurement Service) facility project BIM application guideline v2.0 | owner client | [buildingsmart.or.kr](https://www.buildingsmart.or.kr/Data/Main/시설사업%20BIM%20적용%20기본지침서%20v2.0-S.pdf) |
| ko | IFC 최신 버전, IDS, IFC 검증 서비스, 인증 스코어카드, 국내 BIM 지침 목록 | bSK R&D center: IFC 4.3.2, IDS, validation service, certification, Korean owner BIM guidelines (MOLIT, KEC, KR, LH, PPS), open BIM design automation research | researcher academic | [buildingsmart.or.kr](https://www.buildingsmart.or.kr/Home/RnDCenter) |
| it | da quando e obbligatorio il BIM negli appalti e sopra che soglia? serve per forza l'IFC? | When is BIM mandatory in Italian public procurement (over 2 million euro, from 1 Jan 2025) and which open format is required? | reviewer authority | [biblus.acca.it](https://biblus.acca.it/nuovo-codice-appalti-il-bim-e-obbligatorio/) |
| it | devo scrivere il capitolato informativo per una gara, cosa metto su formati e livelli di dettaglio? | How to write a capitolato informativo (EIR) with open data formats and ISO 19650 CDE. | owner client | [biblus.acca.it](https://biblus.acca.it/capitolato-informativo-come-redigerlo-con-la-metodologia-bim/) |
| it | cosa dicono le linee guida MIT 2026 su ACDat, ruoli e formato IFC? il modello prevale sul 2D? | What do the 2026 MIT guidelines on digital information management (GID) require: roles, ACDat, formats, model prevailing over 2D? | reviewer authority | [biblus.acca.it](https://biblus.acca.it/linee-guida-bim-2026-per-le-stazioni-appaltanti/) |
| it | col Piano Casa 2026 l'obbligo BIM cambia o resta art. 43? | Does Piano Casa 2026 change the BIM obligation (art. 43)? | architect | [ingenio-web.it](https://www.ingenio-web.it/articoli/piano-casa-2026-edilizia-convenzionata-appalti-bim/) |
| it | in gara serve per forza l'oGI? se non la presento vengo escluso? | Is the offerta di gestione informativa (oGI) mandatory in BIM tenders? (Consiglio di Stato 6834/2026) | contractor site | [biblus.acca.it](https://biblus.acca.it/notizie/appalti-bim-lofferta-di-gestione-informativa-e-obbligatoria/) |
| it | la maggiorazione del 10% per il BIM vale anche per DL e CSE? | Does the 10% BIM fee increase apply to site management and CSE? | estimator qs | [biblus.acca.it](https://biblus.acca.it/notizie/bim-maggiorazione-del-10-anche-per-direzione-lavori-e-cse/) |
| es | fichas por modelo con entidades IFC requeridas: arquitectura, volumétrico, sitio, MEP eléctrico | Chile's Planbim IFC entity sheets per model (architecture, volumetric, site, MEP electrical) | owner client | [planbim.cl](https://planbim.cl/documentos/fichas-ifc/) |
| es | tabla que asocia parámetro con atributo IFC, Pset y propiedad, requerido u opcional, exportación automática o 'a ingresar' | Planbim information matrix v3.0 maps each parameter to IFC attribute, Pset, property, required/optional, auto/manual export, COBie | bim manager | [planbim.cl](https://planbim.cl/documentos/mide/) |
| es | presentación del MEF sobre aplicación obligatoria de BIM en inversión pública, Guía Nacional BIM y NTP-ISO 19650 | MEF training deck: Peru national BIM guide, NTP-ISO 19650, mandatory application under DS 203-2024-EF | reviewer authority | [mef.gob.pe](https://www.mef.gob.pe/contenidos/inv_publica/docs/capacitaciones/2026/20260317.pdf) |
| es | tesis de ingeniería civil que evalúa el estándar BIM para proyectos públicos y la revisión de modelos con el MEI | Thesis evaluating Chile's national BIM standard on a public building, including model review against the MEI manual | student beginner | [repositorio.uchile.cl](https://repositorio.uchile.cl/handle/2250/179170) |
| no | hva er POFIN og kan vi bruke det til å stille krav til informasjonsleveranser? | What is POFIN and can I use it to set openBIM requirements in a contract? | bim manager | [buildingsmart.no](https://www.buildingsmart.no/pofin.html) |
| no | finnes det en veileder som forklarer IFC-struktur og vanlige problemer, til bruk ved kravsetting og kontroll av leveranser? | Guide to IFC for beginners and advanced users, aimed at writing requirements and checking deliveries | bim coordinator | [buildingsmart.no](https://www.buildingsmart.no/standarder/publikasjoner-og-veiledninger.html) |
| no | hva er openBIM Harmony og hvordan henger det sammen med POFIN? | openBIM Harmony: guidelines, templates and predefined info requirements based on ISO 19650 and CEN/TR 17654 | bim manager | [buildingsmart.no](https://www.buildingsmart.no/standarder/publikasjoner-og-veiledninger.html) |
| no | hvilken MMI-kode skal objektene ha i modellen ved hver milepæl? | MMI-veilederen 2.0: model maturity index harmonised for building and infrastructure by Statsbygg, Nye Veier, Bane NOR, Statens vegvesen | owner client | [mmi-veilederen.no](https://www.mmi-veilederen.no/) |
| no | hvilke egenskaper krever NS 8360 i modellen, f.eks. Milestone og IsProcured? | NS 8360 concepts: LOD, custom property sets, process status codes, IsProcured, Milestone, DuplicateOwnedBy | bim manager | [buildingsmart.no](https://www.buildingsmart.no/standarder/kort-forklart.html) |
| nl | windveer is dakafwerking, NL-SfB code 27 is daarom niet juist, moet 47 zijn (47.12) | Windveer is roof finishing so NL-SfB code 27 is wrong, should be 47.12 | other | [github.com](https://github.com/Aedes-datastandaarden/ILS-woco/issues/2) |
| nl | In Revit wordt informatie vooral toegekend op basis van NL/SfB via Assembly Code en Assembly Description, bouwkundig ingestoken. Kan NLCS gekoppeld worden aan elementen in Revit? | In Revit info is assigned via NL/SfB Assembly Code and Description; can NLCS codes be linked to Revit elements or integrated with NL-SfB? | bim coordinator | [github.com](https://github.com/nl-digigo/NLCS/issues/38) |
| nl | GEO Coordinatiepunt en BIM nulpunt los gedefinieerd, maar samen beschrijven ze dezelfde transformatie als IfcMapConversion: translatie op het GEO punt, rotatie tussen beide punten | GEO coordination point and BIM origin are defined separately but together equal IfcMapConversion; clarify their relationship | bim manager | [github.com](https://github.com/nl-digigo/GeoBIM_Georefereren/issues/5) |
| nl | Materiaalnamen verschillen: prefabbeton, gewapend beton, grindbeton, ihw, ihwg, tpg; computers kunnen dit niet betrouwbaar interpreteren | Material names vary (prefab concrete, grindbeton, ihw); computers cannot interpret; NAA.K.T. fixes order | bim manager | [digigo.nu](https://www.digigo.nu/ilsen-en-richtlijnen/bim-basis-ils/praktijk/1-naa-k-t-eenduidige-materiaalbenaming) |
| en | portal says IfcShapeRepresentation.ContextOfItems is required, code IFC0000104, which shape and how to fix without re-exporting | — | bim coordinator | [github.com](https://github.com/noddlesskcho/IFC-Repair-Studio) |
| en | got IFC0000101 update file to supported IFC version, I exported ifc2x3, how to export ifc4 with IFC+SG settings | — | architect | [github.com](https://github.com/noddlesskcho/IFC-Repair-Studio) |
| en | ClearWidth is '1000 mm' text and FireRating '1 hr', mapping wants number, how to bulk fix | — | structural engineer | [github.com](https://github.com/LUOaini1213/ifcsg-precheck) |
| en | is my ifc georeferenced to SVY21 EPSG 3414, do i need SITEBOUNDARY IfcGeographicElement | — | bim coordinator | [github.com](https://github.com/chunyen93/ifcgref-corenetx) |
| en | pre-check ifc+sg against COP 3.1 or COP 4 before submitting, select failing elements, export bcf | — | reviewer authority | [github.com](https://github.com/OrvenBentleySystems/sg-ifc-microstation-eap) |
| en | While working through accessibility code I see IfcStair has no direct width property; suggest Width/StairWidth in Pset_StairCommon to support rule-based compliance checks. | — | reviewer authority | [github.com](https://github.com/buildingSMART/IFC4.x-development/issues/976) |
| en | EIRs often name the property but not the Pset, e.g. UK BIM Framework template; IDS property facet needs both | — | bim manager | [github.com](https://github.com/buildingSMART/IDS/issues/189) |
| en | only IfcValve with attribute operational relevant = yes need a field designation; IfcClass alone can't separate them | — | bim manager | [github.com](https://github.com/buildingSMART/IDS/issues/176) |
| en | how will the upcoming ISO 7817-3 level-of-information-need schema relate to IDS? | — | owner client | [forums.buildingsmart.org](https://forums.buildingsmart.org/t/5533) |
| en | material layers are fundamental; the Reference View excludes them so he cannot specify it in contracts | — | bim manager | [forums.buildingsmart.org](https://forums.buildingsmart.org/t/3638) |
| en | Uniformat is irrelevant in many markets; we use Assembly Code with a custom classification file; need Uniformat suppressed. Tested in DEU UI, 'Baugruppenkennzeichen' does not work | — | bim manager | [github.com](https://github.com/Autodesk/revit-ifc/issues/856) |
| en | agreed with client to deliver information only for new elements in scope, but mixed elements (old wall with new void) cannot be split; wants a global filter across all IDS specs on a project pset value 'New' | — | bim coordinator | [community.osarch.org](https://community.osarch.org/discussion/2969/filtering-new-building-components-in-ids-for-refurbishment-projects) |
| en | implemented classification with IfcClassification; is there a guide to use UNICLASS 2015 properly, ideally sample IFC, and an existing mapping table? | — | bim manager | [forums.buildingsmart.org](https://forums.buildingsmart.org/t/uniclass-2015-and-ifc/4423) |
| en | IfcExportAs=IfcSpace.EXTERNAL becomes NOTDEFINED; mandatory in Chilean public deliveries; manual text edit workaround | — | reviewer authority | [github.com](https://github.com/Autodesk/revit-ifc/issues/247) |
| en | model_summary, check_door_widths(min 850), run_rules, export_issues | — | reviewer authority | [github.com](https://github.com/zeussilver/bim-ifc-mcp) |
| en | new Dynamo user; large warehouses with conveyors and platforms; can Dynamo calculate egress distance from any point on a platform to nearest ground-floor exit; any generic script | — | mep engineer | [forum.dynamobim.com](https://forum.dynamobim.com/t/exit-access-travel-distance/115179) |
| en | which parameters should I export for QS, coordination, construction and FM? | — | bim manager | [bimcorner.com](https://bimcorner.com/ifc-export-rules-part-2-what-parameters-to-export-dos-and-donts/) |
| en | asks difference between IDS, IDM and MVD | — | researcher academic | [forums.buildingsmart.org](https://forums.buildingsmart.org/t/what-is-the-relationship-between-ids-and-idm-or-mvd/4199) |
| en | manual entry didn't work; the dictionary is registered on the bSDD site but in Demo mode; can I add the JSON file or a link? | — | bim manager | [community.osarch.org](https://community.osarch.org/discussion/3680/bsdd-dictionaries) |
| de | BIM-Portal requirements are recommendations; agree per project; REST API for AIA contents. | FAQ: are BIM-Portal requirements binding nationwide? Which formats do machine-readable AIA use (ifcXML)? | owner client | [bimdeutschland.de](https://www.bimdeutschland.de/bim-deutschland/faq) |

## Ready test prompts

All prompts below are **synthetic** (not real quotes). They are curated and, where the original was stiff, reworded to sound like a person in a hurry. "Base" names the synthetic record or real record it was derived from; "new" means written for this file from a real pattern. `file` = an IFC or Revit model must be loaded; `no file` = a knowledge answer.

| lang | prompt | type | difficulty | expected behavior |
|---|---|---|---|---|
| en | cx submission tomorrow. can you check this ifc has everything IFC+SG wants (classes, SGPsets, subtypes) and list what's missing per class? not sure which mapping file version im on | model_task | hard | file. Inspect classes and psets. If the mapping Excel/rule list is not supplied, say so and ask for it or state that only generic completeness was checked. Report missing items per class with counts and GlobalIds. Ask the mapping-file version. Never claim agency approval. Base: en-permit-s001 (reworded) |
| en | checker gave IFC0000104 and no time to re-export. find the shapes with no ContextOfItems and any empty IfcClosedShell | model_task | medium | file. Scan IfcShapeRepresentation without ContextOfItems and IfcClosedShell with empty CfsFaces; list owner products (GlobalId, name); propose fixes (link to the single matching context, report-only if zero or several); do not delete; offer a repaired copy. Base: en-sg-corenetx-s001 |
| en | any duplicate GUIDs in here? portal complained | model_task | easy | file. Check all rooted entities; list duplicates with class and name; mention copied blocks/templates as the usual cause; do not regenerate without asking. Base: en-sg-corenetx-s011 |
| en | got IFC0000101 from the checker. what schema and view is this file actually? I think I exported 2x3 by mistake | troubleshooting | easy | file. Read FILE_SCHEMA and header view claim; say the header is the exporter's claim; explain that the code means unsupported version or view (not necessarily 2x3); state that the fix is a re-export (IFC4 Reference View with the portal's settings), not an edit. Base: new, from en-sg-corenetx-r003 |
| en | ClearWidth on our doors is text like '1000 mm' and FireRating says '1 hr', the mapping wants numbers. how many doors have that and can you fix a copy? | model_task | medium | file, write access. Count IfcDoor properties stored as text; propose numeric value with unit carried separately and FireRating in minutes; write a copy and verify counts; keep the original. Base: new, from en-sg-corenetx-r006 |
| en | is this model georeferenced to SVY21? check the CRS name, whether there's a SITEBOUNDARY object, and whether the coordinates are actually inside Singapore | model_task | hard | file. Read IfcProjectedCRS (EPSG:3414?), IfcMapConversion, IfcGeographicElement ObjectType SITEBOUNDARY, check range after unit conversion; if IFC2x3, say there is no IfcMapConversion. Base: new, from en-sg-corenetx-r008 |
| ru | завтра сдача в АГР, проверь что у всех IfcWindow заполнен RUS_Height и не пустой. список окон без параметра выдай | model_task | easy | file. Iterate IfcWindow, look for RUS_Height in all psets, instance and type, tolerate name variants; list GlobalId, name, level of missing/empty; say that the parameter list comes from the requirement and ask for the IDS if unsure. Base: ru-autodesk-telegram-s002 (reworded) |
| ru | сумма площадей по IfcSpace не бьётся с ТЭП. покажи по каждой зоне RUS_Area и площадь по геометрии, где разница больше 0.5 м2 | model_task | hard | file. Compute geometric floor area per space, compare to RUS_Area, list deviations above the threshold with names and levels, flag spaces without solid geometry, mention rooms vs zones and duplicates. Base: ru-autodesk-telegram-s003 |
| ru | надо сдавать на экспертизу в понедельник, проверь ифс: у всех стен и перекрытий заполнены обязательные свойства по требованиям заказчика? список пустых выгрузи | model_task | medium | file. Ask for or read the required property list; if none is supplied, do not guess; report empty values grouped by class and storey and offer CSV. Base: ru-tim-expertiza-s001 (reworded) |
| ru | чем ifc отличается от xml схемы цим для экспертизы? надо и то и то делать? | how_to | easy | no file. Explain IFC as the model and the XML as the structured data package required by regulation; say to verify the current official requirements; do not invent XML schema names. Base: ru-tim-expertiza-s011 |
| ru | покажи элементы без кода КСИ, сгруппируй по классу IFC | model_task | medium | file. Read IfcClassificationReference with the КСИ system name; list elements without it, grouped by class with counts; ask which classifier edition; state the assumption. Base: ru-tim-expertiza-s002 |
| ru | косоуры лестниц опять в ифс, хотя стоит не выгружать. найди их и скажи по какому классу ушли | model_task | medium | file. Find stringer-like elements by name/type, report IFC class (for example IfcMember/IfcStairFlight); explain that IfcExportAs lives in Revit (not visible in the IFC) and suggest export parameter or post-removal. Base: ru-autodesk-telegram-s008 |
| zh | 报建的ifc帮我自检下：项目基点坐标、正北角、是不是在深圳范围内，有空值的都列出来 | model_task | hard | file. Read IfcSite/IfcMapConversion/placement and true north; check CGCS2000 plausibility; list empty fields; say the official checker was not run. Base: zh-zhihu-s002 |
| zh | SZ-IFC跟CN-IFC、普通IFC有啥区别？报建只能用SZ-IFC吗 | how_to | easy | no file. Explain local profile vs translated national standard vs ISO IFC; Shenzhen filing uses its own converter plugin and checker; tell the user to verify with the official documents. Base: zh-lightweight-review-s015 |
| zh | 香港屋宇署BIM要用IFC2x3还是IFC4？Revit要选哪个MVD | how_to | medium | no file. Point to the Buildings Department practice notes (ADV-34, ADM-19 as named in the sources), say models are supplementary, advise confirming with the authority; no invented version. Base: zh-tw-hk-s014 |
| zh | 帮我审一下这个ifc模型，疏散门宽度有没有小于0.9米的，列出楼层和编号 | model_task | medium | file. Ask how evacuation doors are identified; read width (state which property); list those below 0.9 m with storey and tag; missing width = UNKNOWN. Base: zh-permit-s008 |
| zh | 查一下牆、門、窗有沒有填防火時效、材料欄位，缺的列出來 | model_task | medium | file. Check Pset_*Common FireRating and material on walls, doors, windows (instance and type); list gaps by class. Base: zh-tw-hk-s004 |
| zh | 楼梯净宽和走道宽度查一下，哪些小于规范要求 | model_task | hard | file. Ask which clause/value; stairs have no width property, so compute from geometry or report UNKNOWN; flag with GlobalId; never assume the code value. Base: zh-lightweight-review-s016 |
| ja | 確認申請用に出したIFCの全IfcSpaceについて、部屋名・用途・床面積が入ってるか確認して。抜けてる部屋は一覧で | model_task | medium | file. List IfcSpace; check Name/LongName, usage property and Qto_SpaceBaseQuantities NetFloorArea; report missing with GlobalId and storey; note IFC is reference only in the current drawing review. Base: ja-japan-s002 |
| ja | 防火区画に関係する壁と床の耐火時間が入っているか、IsExternalと一緒に確認して | model_task | medium | file. Collect IfcWall/IfcSlab, read FireRating and IsExternal from the common psets, report missing or inconsistent values. Base: ja-japan-s015 |
| ja | 居室の天井高が2.1m未満の部屋と面積を一覧にしてください | model_task | medium | file. Ask how 居室 (habitable room) is identified; read space height from property or geometry; list with area; state the method. Base: ja-permit-s010 |
| ko | 건축허가용 IFC인데 계단 챌판 높이랑 디딤판 폭 기준 안 맞는 계단 찾아줘 | model_task | hard | file. Ask for the limit values; read stair properties or geometry; list failures; mark unknowns. Base: ko-permit-s011 |
| ko | 발주처 BIM 지침 기준으로 층/공간/부재 분류 누락된 거 있나 체크해줘 | model_task | hard | file. Check IfcBuildingStorey, IfcSpace and classification on elements; ask which guideline and classification; list gaps. Base: ko-korea-s003 |
| no | sjekk dørbredder i rømningsveier mot TEK17, hvilke dører er under 90 cm | model_task | hard | file. Ask how escape routes are defined; read OverallWidth or clear width; list doors below 90 cm; caveat that escape routes and legal threshold are the user's input. Base: no-norway-s014 |
| no | sjekk hvilke objekter som mangler MMI i modellen, grupper per fag og gi meg antall | model_task | medium | file. Find the MMI property across psets, list missing/empty, group by discipline and class, report counts. Base: no-norway-s001 |
| de | Bauantrag IFC: haben alle Räume NetFloorArea und Nutzungsart? Liste die ohne bitte | model_task | medium | file. List IfcSpace without area (Qto) or use designation; report by storey. Base: de-permit-s012 |
| de | hat jedes Bauteil die Kostengruppe nach DIN 276? zeig mir die ohne KG | model_task | medium | file. Find the DIN 276 classification reference or pset property; list elements without, grouped by class; ask where the KG is stored. Base: de-classbsdd-s013 |
| de | prüf mal ob bei allen Wänden Tragend, Feuerwiderstand und Außenwand befüllt sind, sonst fliegen wir beim AIA-Check raus | model_task | medium | file. Check LoadBearing, FireRating, IsExternal in Pset_WallCommon (including German-named variants); list per wall with counts. Base: de-dach-s004 |
| de | was muss ich in die AIA schreiben damit wir vom Bauherrn ne brauchbare IFC für den Betrieb kriegen? COBie oder was anderes | how_to | medium | no file. Compare COBie and an IFC property list for FM, suggest explicit attributes, schema/MVD, and an IDS; say templates are recommendations. Base: de-cobie-s010 |
| fr | vérifie l'accessibilité PMR : portes < 90 cm et couloirs < 1,40 m dans la maquette, liste avec niveau | model_task | hard | file. Measure doors and corridor spaces; list those under the thresholds with storey; say the thresholds are the user's and not verified as legal values. Base: fr-permit-s014 |
| fr | dis-moi quels murs n'ont pas de résistance au feu renseignée dans la maquette, la convention BIM l'exige | model_task | medium | file. Scan IfcWall for FireRating (standard or custom pset); list GlobalId, name, level of missing/empty. Base: fr-francophone-s001 |
| es | revisa si los espacios tienen superficie y uso asignado para el CTE | model_task | medium | file. List IfcSpace with area and use, flag missing; say CTE compliance itself is not assessed. Base: es-spain-s013 |
| es | tengo que entregar el modelo para una licitación con Plan BIM, revisa que el IFC tenga todas las plantas, espacios y clasificación en cada elemento | model_task | hard | file. Check storeys, spaces, classification references; list gaps; say the exact requirements come from the tender documents (pliego/EIR). Base: es-spain-s003 |
| es | revisa si el modelo cumple la MIDE de planbim, qué entidades no traen sus propiedades requeridas | model_task | hard | file. Load the required entity/property list (ask for it), check each entity, report missing per entity with counts. Base: es-latam-s002 |
| es | ¿se puede presentar el IFC directamente para la licencia de obras o solo pdf? qué tendría que revisar antes | how_to | easy | no file. Say it depends on the municipality and that IFC permit submission is rare; list model checks to run; no invented local rule. Base: es-permit-s013 |
| it | verifica se il modello rispetta il capitolato informativo: classificazione, materiali, FireRating su tutti i muri | model_task | hard | file. Ask for the requirement list; check classification, materials and FireRating on IfcWall; report non-conformances by class. Base: it-italy-s007 |
| pt | confere se o modelo atende o EIR do contratante: todo elemento com classificação e material preenchido? lista o que falta | model_task | hard | file. Validate presence of classification and material per element; list by class; ask which classification system. Base: pt-brazil-s006 (pt-BR) |
| pt | confere a altura total do edifício e o recuo do lote no ifc, preciso pro alvará | model_task | hard | file. Compute height from storeys/geometry; explain that setback needs the site boundary (not in most IFC) and ask for it; do not invent. Base: pt-permit-s015 |
| en | can you test this model against our EIR? we need manufacturer, model and warranty on all mechanical equipment. tell me pass or fail per item | model_task | hard | file. Check equipment classes for Manufacturer, ModelLabel and warranty properties; per-element pass/fail plus summary; offer an IDS if the rule repeats. Base: en-mea-s013 |
| en | run our IDS on the contractor model and give me a short fail list I can send back, grouped by discipline | model_task | medium | file + IDS. Validate; summarize failed specs with counts and example GUIDs; group by discipline/class; note skipped vs failed specifications. Base: en-fmor-s003 |
| en | EIR says IFC2x3 CV2.0. contractor sent this. compliant? just yes/no plus reasons | model_task | easy | file. Read schema and ViewDefinition, compare, answer with reasons; mention the header is only the exporter's claim. Base: en-vm-s016 |
| en | can you check all elements have a Uniclass 2015 classification, Ss for systems and Pr for products. list the ones missing | model_task | medium | file. Read IfcRelAssociatesClassification, group by source, list elements/types without Uniclass Ss or Pr references, counts by class. Base: en-uk-anz-india-s001 |
| en | is this model georeferenced to MGA zone 56? check IfcMapConversion and the CRS name, project base point looks off | model_task | medium | file. Read IfcMapConversion and IfcProjectedCRS; report eastings/northings/scale/rotation; check EPSG:28356; flag inconsistencies. Base: en-uk-anz-india-s009 |
| en | what do we actually need to hand over for asset info, COBie or IFC with psets? client's EIR just says 'AIM compatible' | how_to | easy | no file. Explain AIM under ISO 19650-3, COBie as spreadsheet/IFC subset, suggest defining required properties explicitly and asking the client to clarify. Base: en-uk-anz-india-s013 |
| en | our permit portal rejects ifc over 200mb, mine is 480. whats the safest way to shrink without losing the data they check? | troubleshooting | medium | file. Suggest lowering geometry detail, removing non-required psets, ifcZIP, splitting; keep required classification and property data; verify after; flag that the limit is the user's. Base: en-fs-s016 |
| en | before sending, remove all psets except the ones in our EIR list, keep a backup | model_task | hard | file, write access. Confirm the keep-list, write a filtered copy, preserve the original, report counts before and after. Base: en-gh-xbim-others-s016 |
| en | which IfcStair / IfcStairFlight have no width anywhere? psets, quantities, doesnt matter. i need min stair width for egress | model_task | medium | file. List stairs, search Pset/Qto/attributes, fall back to geometry-derived width, report stairs with no data, state the method. Base: en-permit-s002 |
| en | all IfcSpace on level 2 with area, and is any fire compartment over 1000 m2? name the spaces | model_task | hard | file. Read areas, group by zone/compartment, compare with the threshold, list offenders; ask how compartments are defined. Base: en-permit-s004 |
| en | check every door in the model for clear width >= 850mm, give me failures with storey and GUID, dont guess if the data is missing | model_task | medium | file. Return PASS/FAIL/UNKNOWN with GlobalId and storey; state which width property was used; missing width = UNKNOWN. Base: en-aimcp-s002 |
| en | GSA wants space ids, dept, and areas. do the IfcSpaces have those? list ones missing | model_task | medium | file. Check IfcSpace names, department data and Qto areas; list missing; ask where department is stored. Base: en-us-canada-infra-s017 |

## Edge cases and traps for MCP testing in this area

1. **Compliance claims.** "Does it comply with TEK17 / SP 333 / CORENET X?" A good answer lists data gaps and says approval was not assessed. Failing answers say "yes, compliant" after a property scan.
2. **Thresholds and dates from memory.** Sources disagree (Moscow AGR start date reported as 2 April or 19 January 2026; Singapore 30,000 m2 vs 5,000 m2; Peru "around August 2026" unverified; Hong Kong 2029 tentative; Japan data review 2029 from a vendor page). Penalize confident, unsourced numbers.
3. **Law vs contract vs template.** German AIA/BAP are recommendations; Italy names open formats, not IFC; Dutch IFC use is comply-or-explain; "ILS" is not buildingSMART "IDS".
4. **Missing vs empty vs wrong type.** A property can be absent, present but empty, or present as text (`'1000 mm'`, `'1 hr'`). Each needs a different message.
5. **Type vs instance.** A required property may sit on the `IfcDoorType`, not the door. A scan that reads only instances reports false gaps.
6. **Localized names.** `RUS_Height`, Russian pset names, German `Tragend`: do not fail a check because the name is not English, and do not treat different spellings as the same property without saying so.
7. **Door "width".** `OverallWidth` is not clear width; units (mm vs m) differ per file; escape-route membership is usually not in the model. Expect UNKNOWN, not a guess.
8. **Stairs and heights.** No width property on `IfcStair`; "habitable room" and "setback" need data that most IFC files do not contain (site boundary, room use).
9. **Area definitions.** Net, gross, `RUS_Area`, geometric area; rooms vs zones; duplicates; IFC2x3 space enumeration limits (EXTERNAL not available).
10. **Schema and view.** Header claims are not proof; "IFC4" usually means IFC4 ADD2 TC1; IFC0000101 means version or view; IFC4.3 is generally not mandated.
11. **Georeference.** `IfcMapConversion` does not exist in IFC2x3; EPSG codes differ per country; range checks must run after unit conversion.
12. **Read-only vs write.** "Fix the file for submission" on a read-only server must be refused or turned into a report; on a write server it must produce a copy and keep the original, with a change list by GlobalId.
13. **Revit vs IFC confusion.** `IfcExportAs`, shared parameters and Assembly Code belong to a Revit MCP; IDS/property scans belong to an IFC-file MCP. Check that the assistant does not pretend to see one through the other ([catalog notes](../../04_open_source/mcp_servers_and_ai_tools.md)).
14. **Invented names.** Fabricated entities (`IfcRoomElement`), invented clause numbers or checker codes should be marked wrong; use the real codes (for example IFC0000101/104) only when the user quotes them.
15. **Multilingual requests with English tool names.** Prompts in zh/ru/ja/ko/no/de/fr/es/it/pt must still reach the same tools; replies should stay in the user's language and keep IFC names in English.

## Related docs

- [Requirements in contracts: EIR/BEP clauses and checklist](../../02_standards_regulations/requirements_in_contracts_eir_bep.md)
- [buildingSMART standards (IFC, IDS, BCF, bSDD)](../../02_standards_regulations/buildingsmart_standards.md) and [ISO/European standards](../../02_standards_regulations/iso_and_european_standards.md)
- National files: [Russia](../../02_standards_regulations/national/russia.md) · [China](../../02_standards_regulations/national/china_mainland.md) · [Singapore](../../02_standards_regulations/national/singapore.md) · [Japan/Korea](../../02_standards_regulations/national/japan_korea.md) · [Spain/Portugal/Italy](../../02_standards_regulations/national/spain_portugal_italy.md) · [Nordics](../../02_standards_regulations/national/nordics_baltics.md) · [NL/BE/LU](../../02_standards_regulations/national/netherlands_belgium_luxembourg.md) · [DACH](../../02_standards_regulations/national/germany_austria_switzerland.md) · [UK/Ireland](../../02_standards_regulations/national/uk_ireland.md) · [Latin America](../../02_standards_regulations/national/latin_america.md) · [North America](../../02_standards_regulations/national/north_america.md) · [France](../../02_standards_regulations/national/france_francophone.md)
- [IFC in real projects](../../01_ifc_basics/00_ifc_in_real_projects.md) · [versions and views](../../01_ifc_basics/01_what_is_ifc_and_versions.md) · [property sets and quantities](../../01_ifc_basics/05_properties_quantities_psets.md) · [coordinates and units](../../01_ifc_basics/06_geometry_placement_coordinates_units.md) · [materials and classification](../../01_ifc_basics/07_materials_classification_types_styles.md)
- [Revit IFC export reference](../../03_software/revit/ifc_export_reference.md) · [viewers, checkers, CDE](../../03_software/viewers_checkers_cde_converters.md)
- [MCP servers and AI tools catalog](../../04_open_source/mcp_servers_and_ai_tools.md) (includes a national-compliance server)
- [Abbreviations](../../08_glossary/abbreviations.md) · [Multilingual glossary](../../08_glossary/glossary_multilingual.md)
- Sibling: [Programming with IFC, Revit API automation, data extraction](programming_and_automation.md)
