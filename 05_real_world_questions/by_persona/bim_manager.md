# BIM manager: who they are and what they do with IFC

**Last built: 2026-11-06 · Persona code:** `bim_manager` · **Data behind this page:** 354 records (199 real, 155 synthetic; `python tools/kb.py stats --persona bim_manager`). Languages: en 212, ru 34, zh 31, es 12, it 12, ja 11, de 10, ko 8, nl 7, fr 6, no 5, pt 4 (+ sk, pt-BR).

## In plain words

A BIM manager is the person who decides **how a company or a project works with models**: which template everyone starts from, which IFC export settings are used, how things are named and classified, what the contract (the "EIR" and "BEP") promises, and which software versions are allowed. Where the coordinator checks *this week's files*, the manager sets *the rules those files must follow* and answers when a client says "your IFC does not meet our requirements".

A useful picture: the coordinator is the referee on the pitch; the BIM manager wrote the rulebook, trains the teams and gets the call when the referee and a team disagree.

For IFC this means mostly three things: (1) **configuring the exporters** so every author produces compliant files, (2) **writing and checking requirements** (what data, in which property set, in which IFC version), (3) **keeping the pipeline alive** when a software update breaks the setup. In the data a large share of this persona's records are issues and forum threads about the Revit IFC exporter, and many others are questions on buildingSMART's IDS threads.

Not to be confused with: the [BIM coordinator](bim_coordinator.md) (weekly model checks), the [architect](architect.md) (author), the [owner / client](owner_client.md) (who writes the EIR the manager must satisfy).

## Daily IFC tasks

| # | Task | What it looks like in practice | Evidence in the base |
|---|---|---|---|
| 1 | Maintain the export setup | Class-mapping tables, parameter-to-property-set mapping files, shared parameter files, "IFC export template" per project; re-test after each Revit/exporter update. | [en-autodesk-revit-export-r008](https://forums.autodesk.com/t5/revit-architecture-forum/ifc-export-in-2027-mapping-parameters-severely-lacking/td-p/14229702), [en-gh-proxy-r013](https://github.com/Autodesk/revit-ifc/issues/840) |
| 2 | Translate the EIR into something checkable | Turn a contract clause ("all doors need FireRating") into a property set name, a data type and, increasingly, an IDS file. | [en-uk-anz-india-r013](https://github.com/buildingSMART/IDS/issues/189) |
| 3 | Check deliveries from partners and subcontractors | Run one set of rules over many files; report pass/fail per rule with counts; send back a list. | [ru-habr-dev-r014](https://habr.com/ru/articles/883016/), synthetic `ru-autodesk-telegram-s017` |
| 4 | Choose the IFC version and view | IFC2x3 Coordination View or IFC4 Reference View? What does the client's tool accept? | `versions_mvd` 35; synthetic `ru-vm-s005`, `de-vm-s010` |
| 5 | Keep identifiers and classification clean | Uniclass / NL-SfB / OmniClass / КСИ / DIN 276 on every element; stable GlobalIds between issues. | `classification_bsdd` 33, `guid_change_tracking` 30 |
| 6 | Reconcile with national rules | Moscow AGR / expertise, Shenzhen SZ-IFC, Singapore IFC+SG, Dutch ILS, Norwegian POFIN, Chilean MIDE. | `national_requirements` 50 ([Russia](../../02_standards_regulations/national/russia.md), [China](../../02_standards_regulations/national/china_mainland.md), [NL/BE](../../02_standards_regulations/national/netherlands_belgium_luxembourg.md), [Nordics](../../02_standards_regulations/national/nordics_baltics.md), [Latin America](../../02_standards_regulations/national/latin_america.md)) |
| 7 | Control file weight and speed | Why is the IFC 800 MB, why did the export take 6 hours, what can be switched off (ports, insulation, 2D). | `file_size_performance` 42; [en-mep-r006](https://github.com/Autodesk/revit-ifc/issues/892) |
| 8 | Automate chores with scripts or AI | Batch-export, batch-fill parameters, unused-parameter cleanup, dashboard feeds. | `automate_batch` 12; [zh-aimcp-r033](https://github.com/5788324/Yang-Agent_Revit) |

## Goals

- **One export setup that survives the next software update**, and an external mapping file instead of settings buried in each model ([en-gh-proxy-r013](https://github.com/Autodesk/revit-ifc/issues/840)).
- **Provable compliance:** a pass/fail list per requirement they can attach to a delivery before the client finds the gaps.
- **Requirements that machines can read** (IDS), written once, reused on every project; and trust that the checker is right.
- **Fewer surprises from the exporter:** warnings about what was skipped instead of a silent drop or a crash ([en-gh-revit-ifc-r028](https://github.com/Autodesk/revit-ifc/issues/831): "degrade or skip slow objects and report which decisions it made").
- **A defensible answer to "IFC2x3 or IFC4?"** and to "can we just send IFC and keep native files?".
- **Reasonable use of AI:** read-only questions first, edits only after preview and approval, never invented property names.

## Pains (ranked)

_Quoted phrases in the last column are illustrative: some paraphrase real records, others are taken from the synthetic prompts further down. Only the tables of real records are evidence of what people actually wrote._

| Rank | Pain | Signal | Typical shape |
|---|---|---|---|
| 1 | **Exporter setup breaks or is unclear after updates** | `export_revit` 61, `class_mapping` 32, `psets_properties` 66 | "Revit 2027 mapping parameters severely lacking"; "IfcExportAs is ignored since 2023"; "class mapping is stored inside each model, doesn't scale" |
| 2 | **Turning requirements into checkable rules** | `ids_requirements` 48, `validation_checking` 51, `contracts_bep_eir_loin` 14 | EIRs name the property but not the property set, but IDS needs both; "how do I ask for two attributes in an AND condition" |
| 3 | **National / client rulebooks differ and keep changing** | `national_requirements` 50 | Russian АГР and expertise rules, Shenzhen, Singapore, Dutch ILS, Norwegian POFIN and NS 8360, Chilean MIDE |
| 4 | **Heavy files and slow exports** | `file_size_performance` 42 | "export takes hours and 720 MB", "600 MB project crashes Revit", "2 GB IFC runs out of memory on 16 GB" |
| 5 | **Version and view choice; what survives a round trip** | `versions_mvd` 35 | "Is the industry ready for IFC4?"; "IFC is no miracle weapon: partner receives dumb objects" |
| 6 | **Classification systems that don't fit** | `classification_bsdd` 33 | "We don't use Uniformat, how do I stop it being exported"; Uniclass mapping guides |
| 7 | **GUID stability and duplicates across files** | `guid_change_tracking` 30 | "Why are GlobalIds not unique across files?"; "IfcGuid changes when I move a door" |
| 8 | **Trust in tools, including AI and checkers** | scattered | "AI invented Pset_BuildingElementCommon"; IDS tools that silently skip facets |

## Vocabulary they use (and what they do not know)

### Words and phrases you will see

| Phrase (language) | Plain meaning |
|---|---|
| EIR / AIA (de) / capitolato informativo (it) / cahier des charges BIM (fr) / ТЗ заказчика, требования к ТИМ (ru) / 発注者要求 (ja) | The client's list of what information must be delivered. See [EIR/BEP clauses](../../02_standards_regulations/requirements_in_contracts_eir_bep.md). |
| BEP / BAP (de) | The supplier's answer: how the team will deliver. |
| LOD, LOI, LOIN | How much geometry and data each element must have. Managers write "LOD" even when they mean information. |
| mapping file, pset.txt, map.txt, UDPS (user-defined property sets), shared parameter file | The files that tell the Revit exporter which parameters become which IFC properties. |
| IfcExportAs, "Export to IFC As" | The per-element or per-type parameter that picks the IFC class. |
| IDS, ifctester, "spec", "facet", cardinality | Checkable requirements file; a spec has "applicability" (which elements) and "requirements" (what they must have). |
| CV2.0, RV, DTV | IFC2x3 Coordination View 2.0; IFC4 Reference View; IFC4 Design Transfer View. |
| Uniclass, Uniformat, OmniClass, NL-SfB, DIN 276 "KG", КСИ, GuBIMClass, SICLIC | Classification systems; each country has its favourite. |
| АГР, ТЭП, МССК, RUS_Height, RUS_Area | Moscow submission vocabulary: approval, indicators, classifier, and custom property names the checker looks for. |
| SZ-IFC, IFC+SG, CORENET X, ILS, POFIN, MMI, MIDE | Local IFC profiles and national information-delivery packages. |
| dRofus, Power BI dashboard, Solibri ruleset, BIMcollab, Dalux | Typical neighbours in the manager's toolchain. |

### What they typically do not know, or get wrong

- **IDS limits.** IDS 1.0 cannot express geometry or conditional logic ([ru-habr-dev-r015](https://habr.com/ru/articles/908192/)); different vendors write IDS files differently ([en-bsforum-r033](https://forums.buildingsmart.org/t/5993)); an empty string or a wrong data type can slip through ([IDS issue 403 via en-bsforum-r052](https://github.com/buildingSMART/IDS/issues/403)).
- **IFC as a round-trip format.** The recurring disappointment is that parametric objects arrive as "dumb" geometry ([en-blogs-linkedin-r004](https://bim-me-up.com/die-wunderwaffe-ifc/), [ja-japan-r021](https://note.com/onestruction/n/ne8322e3be44d), [ru-autodesk-telegram-r020](https://sapr.ru/article/24777)). Managers know it in principle but keep asking for it to be fixed.
- **Which property set a property belongs to.** The UK EIR templates name a property such as GrossFloorArea without its set ([en-uk-anz-india-r013](https://github.com/buildingSMART/IDS/issues/189)).
- **That an AI assistant can make up standard-sounding property sets** ([en-blogs-linkedin-r002](https://bimcorner.com/ai-ifc-properties/)).
- **The IFC schema internals** (relationship objects, representation contexts). They think in "parameters and property sets", not entities.

Further reading in this base: [Revit IFC export reference](../../03_software/revit/ifc_export_reference.md), [properties and psets](../../01_ifc_basics/05_properties_quantities_psets.md), [classification](../../01_ifc_basics/07_materials_classification_types_styles.md), [IFC versions](../../01_ifc_basics/01_what_is_ifc_and_versions.md), [buildingSMART standards](../../02_standards_regulations/buildingsmart_standards.md), topic pages [validation / IDS](../by_topic/validation_ids_model_checking.md), [regulations, permits, contracts](../by_topic/regulations_permits_contracts.md), [properties and parameters](../by_topic/properties_and_parameters.md), [Revit export and class mapping](../by_topic/revit_export_and_class_mapping.md), [classification / COBie / FM](../by_topic/classification_cobie_fm.md), [file size and conversion](../by_topic/file_size_viewing_conversion.md).

## Real questions (57, linked)

Paraphrases of questions or issues seen at the linked sources, kept in the asker's language. Language mix in this list: Russian 10, English 35, other languages 12. Where a source page is not in English but the stored paraphrase is (the researcher wrote it in English), the Lang column still shows the page language. A few rows are official guideline pages rather than questions; the "question" column then says what a reader of that page wants to know.

### A. Export setup, mapping tables and what changed in the new Revit version

The BIM manager owns the setup that every author's export depends on. Most of these are feature requests or bug reports aimed at the Revit IFC exporter (GitHub `Autodesk/revit-ifc`, Autodesk forums).

| # | Lang | Their words (paraphrase, original language) | English gloss / context | Source (record id, type, year) |
|---|---|---|---|---|
| 1 | en | The new Revit 2027 parameter mapping GUI replacing the pset.txt workflow lists only some parameters; project parameters are missing from the selection list, some classes show empty lists. |  | [en-autodesk-revit-export-r008](https://forums.autodesk.com/t5/revit-architecture-forum/ifc-export-in-2027-mapping-parameters-severely-lacking/td-p/14229702) forum, 2026 |
| 2 | en | Asks to restore a GUI for mapping project parameters to IFC property sets in 2027. |  | [en-autodesk-revit-export-r009](https://forums.autodesk.com/t5/revit-ideas/gui-for-project-parameter-mapping-in-ifc-export-missing-in-revit/idi-p/14097939) forum, 2025 |
| 3 | en | Since 2023 the old IfcExportAs parameter is ignored; keyschedules and global parameters no longer useful; asks for fallback when built-in parameters are empty. |  | [en-autodesk-revit-export-r018](https://github.com/Autodesk/revit-ifc/issues/541) github_issue, 2022 |
| 4 | en | After the 2024.3 update Revit crashes at every IFC export. |  | [en-autodesk-revit-export-r030](https://forums.autodesk.com/t5/revit-architecture-forum/revit-2024-3-update-revit-crashes-every-time-i-export-ifc/td-p/13030432) forum, 2024 |
| 5 | en | In the new Revit 2027 dialog IfcProject is missing from the entity list, so how can a user-defined pset be added to IfcProject? |  | [en-gh-revit-ifc-r006](https://github.com/Autodesk/revit-ifc/issues/971) github_issue, 2026 |
| 6 | en | Class mapping now stored in a DataStorage object inside each model; doesn't scale across many models, wants an external reference file. |  | [en-gh-proxy-r013](https://github.com/Autodesk/revit-ifc/issues/840) github_issue, 2025 |
| 7 | en | Eight convoluted rules decide the IFC class; consultants get wrong classes despite instructions; want IfcExportAs value visible in the exported IFC to compare. |  | [en-gh-proxy-r021](https://github.com/Autodesk/revit-ifc/issues/392) github_issue, 2021 |
| 8 | en | we don't use Uniformat, how do I disable it from being exported? it seems to always be there | We do not use Uniformat; how to stop it from always being exported as an IfcClassification? | [en-gh-r004](https://github.com/Autodesk/revit-ifc/issues/486) github_issue, 2022 |
| 9 | en | Since Revit 2023 IfcGuid follows UniqueId so moving a door with Disjoin changes its GUID; can it be locked? |  | [en-gh-revit-ifc-r044](https://github.com/Autodesk/revit-ifc/issues/696) github_issue, 2023 |
| 10 | en | duplicate IFC+SG shared parameters same name different guid in my Revit model, values split between old and new, how to merge | Project has two shared parameters with same name but different GUIDs (old vs approved IFC+SG one); which one gets exported? | [en-sg-corenetx-r005](https://github.com/noddlesskcho/IFCSG-Parameter-Consolidator) blog, 2026 |
| 11 | en | Area of a room object can't go into custom pset (client requires it); works for area plan objects | Cannot export the Room Area parameter to a custom property set although Area objects work; client requirement. | [en-spaces-r004](https://github.com/Autodesk/revit-ifc/issues/855) github_issue, 2025 |
| 12 | ru | как добавить свойство Renga в экспорт IFC | How does Renga decide which properties go to IFC? | [ru-dwg-other-r026](https://manual.rengabim.com/ehksport_atributov_obektov.html) official_doc, 2024 |
| 13 | ru | коллеги из Минстроя Свердловской области написали инструкцию по экспорту ЦИМ из Autodesk Revit в IFC | Sverdlovsk region ministry wrote an instruction for exporting a CIM from Revit to IFC, to be part of the regional TIM standard | [ru-autodesk-telegram-r021](https://t.me/s/revithelper_kmv/146) social, 2025 |
| 14 | es | tabla que asocia parámetro con atributo IFC, Pset y propiedad, requerido u opcional, exportación automática o 'a ingresar' | Planbim information matrix v3.0 maps each parameter to IFC attribute, Pset, property, required/optional, auto/manual export, COBie | [es-latam-r012](https://planbim.cl/documentos/mide/) official_doc, 2022 |

### B. Requirements: EIR, IDS, national packages, authority rules

How to ask for data, how to check it, and what the local rulebook says. The Dutch, Norwegian and Chilean items are official guideline pages, which is how managers in those countries phrase "what do I have to deliver".

| # | Lang | Their words (paraphrase, original language) | English gloss / context | Source (record id, type, year) |
|---|---|---|---|---|
| 15 | en | EIRs often name the property but not the Pset, e.g. UK BIM Framework template; IDS property facet needs both | UK BIM Framework EIR templates name the property (e.g. GrossFloorArea) but not the property set; IDS requires a Pset | [en-uk-anz-india-r013](https://github.com/buildingSMART/IDS/issues/189) github_issue, 2023 |
| 16 | en | only IfcValve with attribute operational relevant = yes need a field designation; IfcClass alone can't separate them | Require valves to have a field designation only when they have 'operational relevant = yes' (AND condition across attributes) | [en-uk-anz-india-r012](https://github.com/buildingSMART/IDS/issues/176) github_issue, 2023 |
| 17 | en | vendors produce IDS files differently so interoperability is unclear; is there an online IDS validator? |  | [en-bsforum-r033](https://forums.buildingsmart.org/t/5993) forum, 2025 |
| 18 | en | railway station project, many authoring tools; asks how to combine IDS files for a federated model | Can I merge per-discipline IDS files to check a federated IFC? | [en-val-r005](https://forums.buildingsmart.org/t/ids-and-federated-ifc-file/5654) forum, 2024 |
| 19 | ru | как пакетно проверить кучу IFC по одному IDS и получить отчёт | How to check many IFC models against one IDS with ifcopenshell + ifctester and HTML reports | [ru-habr-dev-r014](https://habr.com/ru/articles/883016/) blog, 2025 |
| 20 | ru | IDS не умеет геометрию и условную логику - что делать | IDS 1.0 cannot express geometry, spatial or conditional rules | [ru-habr-dev-r015](https://habr.com/ru/articles/908192/) blog, 2025 |
| 21 | ru | что такое IDS, где поддерживается, какие ограничения | What is IDS in BIM: scenarios, limits, tool support | [ru-autodesk-telegram-r014](https://habr.com/ru/articles/908192/) blog, 2025 |
| 22 | ru | экспорт в IFC занимает от минут до часов, ошибки находим итерациями, у окон нет параметра RUS_Height | Since 2 April 2026 IFC conforming to IDS is required for MGE/AGR; every check needs a full slow export | [ru-autodesk-telegram-r009](https://habr.com/ru/companies/pik_digital/articles/1057314/) blog, 2026 |
| 23 | ja | 発注者の要求がExcelやPDFでバラバラで、納品IFCのチェックが人力。IDSで機械的に検証できる？ | What power does IDS give for operating IFC correctly (clients checking contractor IFC automatically)? | [ja-japan-r003](https://zenn.dev/miyamiyaumya/articles/6714ef2c6e2c6c) blog, 2023 |
| 24 | it | come verifico che porte e muri abbiano FireRating e trasmittanza prima di consegnare l'IFC? | How to check required properties and values (e.g. FireRating) in an IFC against a template. | [it-italy-r008](https://biblus.acca.it/bim-validation-modelli-ifc/) vendor_kb, 2021 |
| 25 | en | material layers are fundamental; the Reference View excludes them so he cannot specify it in contracts |  | [en-bsforum-r044](https://forums.buildingsmart.org/t/3638) forum, 2021 |
| 26 | no | hvilke egenskaper krever NS 8360 i modellen, f.eks. Milestone og IsProcured? | NS 8360 concepts: LOD, custom property sets, process status codes, IsProcured, Milestone, DuplicateOwnedBy | [no-norway-r012](https://www.buildingsmart.no/standarder/kort-forklart.html) official_doc, 2026 |
| 27 | no | hva er POFIN og kan vi bruke det til å stille krav til informasjonsleveranser? | What is POFIN and can I use it to set openBIM requirements in a contract? | [no-norway-r002](https://www.buildingsmart.no/pofin.html) official_doc, 2025 |
| 28 | nl | GEO Coordinatiepunt en BIM nulpunt los gedefinieerd, maar samen beschrijven ze dezelfde transformatie als IfcMapConversion: translatie op het GEO punt, rotatie tussen beide punten | GEO coordination point and BIM origin are defined separately but together equal IfcMapConversion; clarify their relationship | [nl-dutch-r006](https://github.com/nl-digigo/GeoBIM_Georefereren/issues/5) github_issue, 2026 |
| 29 | nl | Materiaalnamen verschillen: prefabbeton, gewapend beton, grindbeton, ihw, ihwg, tpg; computers kunnen dit niet betrouwbaar interpreteren | Material names vary (prefab concrete, grindbeton, ihw); computers cannot interpret; NAA.K.T. fixes order | [nl-dutch-r023](https://www.digigo.nu/ilsen-en-richtlijnen/bim-basis-ils/praktijk/1-naa-k-t-eenduidige-materiaalbenaming) official_doc, 2024 |
| 30 | ru | какой формат выбрать для экспертизы, коллизий, расчёта | Which of 10+ Renga export formats to choose; IFC4 for coordination, clashes, calculations or expertise | [ru-autodesk-telegram-r018](https://rengabim.com/stati/bol-she-10-formatov-eksporta-importa-v-renga-kakoj-iz-nih-vybrat/) blog, 2022 |
| 31 | ja | 全てのopenBIMはbSDDから始まる、というワークフロー整理 | openBIM workflow centered on bSDD with IFC, IDS, BCF, openCDE | [ja-japan-r026](https://zenn.dev/miyamiyaumya/articles/fc19330aa071ba) blog, 2024 |

### C. Which IFC, how much will survive, and who to believe

Version choice, honest expectations about what IFC can carry, and distrust of anything that sounds too confident (including AI).

| # | Lang | Their words (paraphrase, original language) | English gloss / context | Source (record id, type, year) |
|---|---|---|---|---|
| 32 | en | IFC4 exports lose geometry, change property sets and show glitches; should we switch from IFC2x3? | Is the industry ready for IFC4? Test on a 400-model hospital project says stay with IFC2x3. | [en-blogs-linkedin-r022](https://bimcorner.com/is-the-industry-ready-for-ifc4/) blog, 2022 |
| 33 | en | why is it IFC2x3, IFC4add1, TC1 - what happened to number three? and why is the documentation so hard to navigate? | What I don't like about IFC: documentation looks 20 years old, confusing version names, too many acronyms, redundant Ifc prefix. | [en-blogs-linkedin-r019](https://bimcorner.com/what-i-dont-like-about-ifc/) blog, 2020 |
| 34 | en | one bridge exported three ways: 161 proxies, random GlobalIds, no quantities, national-grid mm coordinates making viewers jitter. How to tell a good file from a bad one? | Same bridge exported three ways gives three very different IFC files; which one will the client send back? | [en-blogs-linkedin-r001](https://bimcorner.com/same-bridge-three-ifc-files/) blog, 2026 |
| 35 | en | AI gave me Pset_BuildingElementCommon and put IsExternal on footings; how do I know which property sets are real? | AI invents IFC property sets that sound standard but do not exist. | [en-blogs-linkedin-r002](https://bimcorner.com/ai-ifc-properties/) blog, 2026 |
| 36 | ja | Rhinoで作ったモデルをIFCに出して確認申請用BIMや引き渡しに使えるのか。見た目は合っていても分類や属性が使えない | IFC is not omnipotent: editing, live links and classifications are lost; creating IFC is not the same as delivering information | [ja-japan-r018](https://note.com/bim_tool_lab/n/nf529aa5d5cc0) blog, 2026 |
| 37 | ja | IFCにすれば別ソフトで編集を続けられると思われがち。実際はパラメトリック関係や独自パラメータが落ちる | Why expectations of IFC drift from reality: sharing not exchange; loss of parametrics; IFC2x3/4/4.3 coexist | [ja-japan-r021](https://note.com/onestruction/n/ne8322e3be44d) blog, 2026 |
| 38 | ru | при каждой конвертации в IFC и обратно теряются данные, элементы возвращаются мёртвой геометрией | With each IFC round trip data is lost; elements come back from IFC as non-editable dead geometry | [ru-autodesk-telegram-r020](https://sapr.ru/article/24777) blog, 2020 |
| 39 | ru | в проекте СП модель предъявляется в RVT и DWG, а IFC нет; элементы должны быть классифицированы | Draft national BIM standard recognizes RVT and DWG as model formats, not IFC? | [ru-dwg-other-r025](https://forum.dwg.ru/showthread.php?t=134394&page=33) forum, 2016 |
| 40 | ru | чем проверить корректность IFC, атрибуты могут не дойти | How to validate IFC from Archicad; attributes may not survive in AutoCAD. | [ru-dwg-other-r030](https://forum.dwg.ru/showthread.php?t=34919&page=3) forum, 2012 |
| 41 | en | Duplicate GlobalIds across IFC files from same project cause linking problems. |  | [en-gh-revit-ifc-r043](https://github.com/Autodesk/revit-ifc/issues/378) github_issue, 2021 |
| 42 | en | Office refining Allplan 2025 IFC; Name vs Reference, USERDEFINED, compared to Revit/Archicad. | How should Name, Reference and ObjectType be used in an Allplan IFC workflow; Allplan lacks types. | [en-roundtrip-r022](https://forums.buildingsmart.org/t/correct-use-of-ifc-name-and-reference-deprecated/6429) forum, 2026 |

### D. Heavy files, slow exports, data at scale



| # | Lang | Their words (paraphrase, original language) | English gloss / context | Source (record id, type, year) |
|---|---|---|---|---|
| 43 | en | industrial plant export 6h16 and 720 MB with insulation vs 2h43 without; LOD setting barely affects insulation | Pipe insulation geometry is 1749 faces at all detail levels; export takes hours and 720 MB; wants more control | [en-mep-r006](https://github.com/Autodesk/revit-ifc/issues/892) github_issue, 2025 |
| 44 | en | Optimise recipe reduced size by 60% for small files; on 100MB+ it takes very long, 20 GB RAM for 500 MB; asks max file size and whether split-optimise-merge is sensible | ifcpatch Optimise cut file size 60% on small files but takes half an hour and 20 GB RAM on a 500 MB file | [en-fs-r005](https://github.com/IfcOpenShell/IfcOpenShell/issues/1603) github_issue, 2021 |
| 45 | en | IFC from Synchro with verbose task info is 2 GB; ifcopenshell.open exhausts 16 GB. Is there another serialisation, preprocessor for lazy loading, or storage tech? | A 2 GB federated 4D IFC runs out of RAM on 16 GB when opened; what strategies exist to treat IFC as a queryable database? | [en-data-r003](https://github.com/IfcOpenShell/IfcOpenShell/issues/2025) github_issue, 2022 |
| 46 | en | Timing table shows export taking minutes with psets enabled versus 45 s without; any fix besides custom mapping files? |  | [en-gh-revit-ifc-r032](https://github.com/Autodesk/revit-ifc/issues/492) github_issue, 2022 |
| 47 | en | Want a single IFC from linked RVTs in Revit without Navisworks or other exporters; binding loses geometry. |  | [en-gh-revit-ifc-r039](https://github.com/Autodesk/revit-ifc/issues/439) github_issue, 2022 |
| 48 | en | python script exports parameters per IFC entity to Excel per file; works for exporter 22.1 but structure changes in 22.6; includes COBie properties and client-specific operations/BOQ/LOD parameters | Script extracting COBie and custom client parameters to Excel breaks between Revit IFC exporter versions | [en-fmor-r009](https://github.com/IfcOpenShell/IfcOpenShell/issues/3978) github_issue, 2023 |
| 49 | en | which parameters should I export for QS, coordination, construction and FM? | IFC export rules and pain points per purpose: coordination, QS, construction, FM. | [en-blogs-linkedin-r023](https://bimcorner.com/ifc-export-rules-part-2-what-parameters-to-export-dos-and-donts/) blog |

### E. Wishing the AI could do the chores: automation and agents

Managers are the persona most likely to ask for preview, confirm, apply, log and undo around any write operation.

| # | Lang | Their words (paraphrase, original language) | English gloss / context | Source (record id, type, year) |
|---|---|---|---|---|
| 50 | zh | 面向 Revit 使用者、BIM 团队、插件开发者 | Wants AI to export model health, preview then apply missing door/window marks, find duplicate room numbers and unplaced views, always with preview, confirm, apply, log, undo. | [zh-aimcp-r033](https://github.com/5788324/Yang-Agent_Revit) official_doc, 2026 |
| 51 | en | Find walls on Level 02, show their Comments values, and propose a batch update. | Prompts: list warnings and affected elements; find walls on Level 02 and propose batch Comments update; approval in Revit before apply. Not yet verified live. | [en-aimcp-r038](https://github.com/Sam-AEC/aec-model-bridge) official_doc, 2026 |
| 52 | en | Find affected elements and group warnings by description | Install prompt for agents and built-in prompts: model_audit, pre_issue_check, stairs; list known agent mistakes such as guessing target, case-sensitive parameters. | [en-aimcp-r043](https://github.com/bimwright/rvt-mcp) official_doc, 2026 |
| 53 | en | combine the agent with a larger persistent typed queryable memory of the model (walls, windows, levels, types, relations) with change history and atomic edits | Add a persistent knowledge-graph memory of the Revit model so the agent can trust and track changes | [en-revit-auto-r031](https://github.com/mcp-servers-for-revit/mcp-servers-for-revit/issues/30) github_issue, 2026 |
| 54 | ja | 日本独自の基準・法規に沿った運用設計 | Japanese Revit MCP aims at operations under Japanese standards like the Building Standards Act; schedules via HTML/Excel round trip. | [ja-aimcp-r041](https://github.com/okuno-dsi/revit-mcp-toolkit) official_doc, 2026 |
| 55 | en | how to remove parameters that have a blank value; I want to share a viewer file with easily understandable parameters | Remove project parameters with blank values before sharing a viewer file | [en-revit-auto-r014](https://forum.dynamobim.com/t/delete-parameters-with-blank-value/115164) forum, 2026 |
| 56 | en | deleting redundant project parameters hides them from UI but they remain in database; want SnoopDB-style Delete in bulk | Permanently delete redundant project/shared parameters in bulk; deleted ones linger as zombie parameters | [en-revit-auto-r019](https://forum.dynamobim.com/t/deleting-zombie-parameters/112603) forum, 2025 |
| 57 | en | AI revit coach with singapore corenet x ifc-sg context, describe goal not just symptom | Kit that gives an LLM a Revit troubleshooting playbook plus Singapore CORENET X / IFC-SG context. | [en-sg-corenetx-r014](https://github.com/samsonleegh/revit-coach) blog, 2026 |

## Ready test prompts (46, synthetic)

**All prompts below are SYNTHETIC** (written by the research agents from real patterns; ids tell you the origin). They assume a loaded IFC unless "no file" is shown.

### 1. Check a delivery against the EIR, BEP or IDS

The single most common manager prompt in the base: "which ones don't have X, list them".

| # / id | Lang | Prompt (SYNTHETIC) | Meaning (EN) | Difficulty | A good answer should |
|---|---|---|---|---|---|
| S1 `en-uk-anz-india-s002` | en | EIR says all doors need FireRating, AcousticRating and Manufacturer. which ones dont have them? need before the issue tonight | Check against the EIR property list before issue | easy, file | Find IfcDoor/types, look in Pset_DoorCommon and any pset for the properties, report missing per door with names and levels. |
| S2 `en-allplan-vw-bentley-s015` | en | check this against client IDS and give pass/fail per spec | Validate model against client IDS | hard, file | Run IDS validation, report failing entities per specification. |
| S3 `en-val-s012` | en | combine arch and struct ids into one and run on federated model, report by discipline | Merge IDS per discipline | hard, file | Merge specification lists, run, group results per discipline. |
| S4 `en-gh-ifcopenshell-s016` | en | check all IfcWall have FireRating matching 30, 60 or 90 | Write IDS spec | medium, file | Create IDS spec, run, report pass/fail, avoid unsupported regex. |
| S5 `de-dach-s004` | de | prüf mal ob bei allen Wänden Tragend, Feuerwiderstand und Außenwand befüllt sind, sonst fliegen wir beim AIA-Check raus | Check that all walls have LoadBearing, FireRating and IsExternal filled in. | medium, file | List walls missing Pset_WallCommon.LoadBearing, FireRating, IsExternal with GUIDs and counts. |
| S6 `no-norway-s003` | no | kan du kontrollere modellen mot kravene i EIR-en, spesielt at alle vegger har brannklasse og lastbærende | Validate the model against the property requirements from the client's EIR | medium, file | Check walls for fire rating and LoadBearing in Pset_WallCommon, report failures with GUIDs. |
| S7 `pt-brazil-s006` | pt-BR | confere se o modelo atende o EIR do contratante: todo elemento com classificação e material preenchido? lista o que falta | Check the model against the EIR required properties and classification (SINAPI/Uniclass) | hard, file | Validate required properties/classification presence per element, output non-conforming list by class. |
| S8 `nl-dutch-s012` | nl | kun je een IDS maken van BIM basis ILS en daarmee dit model toetsen? | IDS from BIM basis ILS | hard, no file | Draft IDS facets, run against model, report. |
| S9 `ja-japan-s005` | ja | うちのIDSで納品IFCをチェックして。壁にFireRatingが入ってないものと、PredefinedType未設定のものを出して | Check against our IDS that every wall has FireRating and report failures | medium, file | Run or emulate IDS facets (Entity IfcWall, Property Pset_WallCommon.FireRating, PredefinedType attribute), list failing elements. |
| S10 `ru-revit-auto-s010` | ru | глянь у каких стен и перекрытий не заполнен параметр Марка, список с id, до экспорта надо | Find elements missing required parameters before export | easy, file | Query walls and floors, check Mark parameter blank, return grouped list with ids. |
| S11 `zh-zhihu-s009` | zh | 按ids检查下：所有IfcWall必须有FireRating和IsExternal，不满足的导个清单 | Check against an IDS requirement | medium, file | Validate IfcWall for Pset_WallCommon FireRating/IsExternal, list failing GlobalIds and names. |
| S12 `es-spain-s003` | es | tengo que entregar el modelo para una licitacion con Plan BIM, revisa que el IFC tenga todas las plantas, espacios y clasificacion en cada elemento | Check model against Plan BIM style delivery requirements | hard, file | Check IfcBuildingStorey, IfcSpace and classification references per element; list gaps; note the exact requirements come from the EIR/pliego. |

### 2. Structure, classification, naming



| # / id | Lang | Prompt (SYNTHETIC) | Meaning (EN) | Difficulty | A good answer should |
|---|---|---|---|---|---|
| S13 `en-blogs-linkedin-s002` | en | why does the tree show 14 IfcBuildingStorey, bep says 8. which ones are supporting levels? | Check extra storeys | medium, file | List storeys with elevations and element counts, compare to expected count, flag likely supporting levels. |
| S14 `en-uk-anz-india-s005` | en | does the spatial structure follow our BEP? Site > Building > Storeys named L00, L01 etc. anything off? | Check naming of storeys and spatial structure vs BEP | easy, file | Traverse IfcSite/IfcBuilding/IfcBuildingStorey, check naming pattern and elevations, report deviations and unassigned elements. |
| S15 `fr-francophone-s004` | fr | vérifie que les niveaux sont nommés comme dans la convention BIM (RDC, R+1...) et que les altitudes sont cohérentes | Verify that storey names follow the convention (R+1, RDC, SS1) and elevations are consistent | medium, file | List IfcBuildingStorey names and elevations, compare against naming pattern, flag mismatches and duplicates. |
| S16 `ru-tim-expertiza-s002` | ru | покажи элементы у которых не проставлен код КСИ, сгруппируй по классу IFC | Find elements with no KSI classification code assigned | medium, file | Look for classification references (IfcClassificationReference) or a KSI code property; list elements lacking them grouped by IFC class with counts. |
| S17 `it-italy-s018` | it | quanti elementi hanno una classificazione (Uniclass, UniFormat)? elenca quelli senza | Classification coverage | medium, file | Check IfcClassificationReference coverage by class. |
| S18 `de-classbsdd-s013` | de | hat jedes Bauteil eine Kostengruppe DIN 276? zeig mir die ohne KG | Check DIN 276 cost group assigned to all components. | medium, file | List elements without DIN 276 classification reference; group by IFC class. |
| S19 `en-autodesk-revit-export-s009` | en | does every element have a classification ref? we need Uniclass, not uniformat |  | medium, file | List elements lacking IfcClassificationReference and which classification system is used. |
| S20 `en-classbsdd-s004` | en | strip the uniformat classification, we dont use it. add omniclass table 23 codes from the Assembly Code param instead | Remove Uniformat IfcClassification and replace with OmniClass 23. | hard, file | Delete Uniformat IfcClassification and its references, create OmniClass IfcClassification, create references from given property, report unmatched. |
| S21 `ja-japan-s009` | ja | ドアにタイプ名ごとに分類コード付けたい。D-1→21-21 11みたいな対応表あるからそれで一括で | Add classification code to all doors by type name | medium, file | Create IfcClassification/IfcClassificationReference and assign to each IfcDoor by type mapping, report unmapped types. |
| S22 `ru-classbsdd-s008` | ru | код классификатора из параметра ревита не попадает в ифс, в настройках экспорта указал, а в IfcClassificationReference пусто. почему | Classification code from Revit parameter does not appear in IFC. | medium, file | Check classification settings, parameter name ClassificationCode, report whether references exist; explain fixes. |

### 3. Which IFC version or view, and what changed between issues



| # / id | Lang | Prompt (SYNTHETIC) | Meaning (EN) | Difficulty | A good answer should |
|---|---|---|---|---|---|
| S23 `ru-vm-s005` | ru | подрядчик просит ифс, но не говорит какой. 2x3 или 4? какой вьюшкой выгружать | Which version to choose for contractors | easy, no file | Explain 2x3 CV2.0 vs IFC4 RV vs 4.3, recommend asking EIR, default to 2x3 CV2.0 for broad compatibility, RV where supported. |
| S24 `en-vm-s002` | en | client wants IFC4 RV. check this export - is it actually RV or is it the DTV with advanced breps? | Check whether an IFC4 export really is Reference View compliant | hard, file | Detect IfcAdvancedBrep/CSG/parametric profiles, material layer sets vs constituents, header view; conclude RV vs DTV-like and list violations. |
| S25 `de-vm-s010` | de | AG fordert IFC4 Reference View. Prüf mal ob die Datei wirklich RV ist und nicht 2x3 oder IFC4x3 | Check IFC4 RV vs AIA requirement | easy, file | Read schema and view; confirm IFC4 and ReferenceView, verify constituent material sets, note deviations. |
| S26 `zh-vm-s007` | zh | 甲方要求交付IFC2x3，帮我检查一下这个文件的版本和视图定义对不对 | Verify file delivered satisfies required IFC2x3 | easy, file | Read FILE_SCHEMA and ViewDefinition, confirm IFC2X3 and CoordinationView 2.0, list deviations. |
| S27 `en-blogs-linkedin-s015` | en | should our EIR demand ifc4 or stay on 2x3? what breaks | Should we require IFC4 | medium, no file | Give balanced view: certification, tool support, model view choice, test before demanding. |
| S28 `ru-autodesk-telegram-s005` | ru | сравни две выгрузки ifc (v3 и v4) по GlobalId, что добавилось, удалилось, у каких поменялись свойства | Compare two IFC exports by GlobalId | medium, file | Match by GlobalId, report added/removed/changed elements and changed property values, summarise by class. |
| S29 `en-mea-s004` | en | compare rev B and rev C of the architectural model. what was added, deleted or moved? just give me the list by level | Compare two issued models and list what changed. | hard, file | Match elements by GlobalId, report added, removed, and changed (placement or properties) grouped by storey; note when GUIDs were regenerated. |
| S30 `en-model-checking-s010` | en | do room areas in the model match the dRofus program? flag >5% off | Compare spaces with dRofus program | hard, file | Compare IfcSpace net floor area with supplied program values, flag deviations over 5 percent. |
| S31 `en-guid-s005` | en | how do i make the IFC GUIDs stay the same between exports from revit? contractor keeps complaining their links break every revision | How to keep IFC GUIDs stable between Revit exports | medium, no file | Explain that recent exporters derive GUIDs deterministically from Revit ids, advise using current exporter, storing IfcGUID in a parameter, avoiding re-created elements and file copies, and checking link/federated export options. |

### 4. Export settings, size, encoding



| # / id | Lang | Prompt (SYNTHETIC) | Meaning (EN) | Difficulty | A good answer should |
|---|---|---|---|---|---|
| S32 `en-autodesk-revit-export-s013` | en | revit 2027 where did the pset txt go? how do I map project parameters now |  | medium, no file | Explain new Parameter Mapping GUI and known limitations. |
| S33 `en-proxy-s002` | en | how many of our elements are IfcBuildingElementProxy? client says anything over 5% fails. list the worst offenders by type name | Fail the model if proxy share exceeds 5 percent | easy, file | Compute proxy share of IfcElement, list proxy types by count, state pass/fail against 5%. |
| S34 `ru-proxy-s011` | ru | у всех типов обобщенных моделей с 'Колонна' в имени проставь IfcExportAs=IfcColumn, остальные не трогай | Set IfcExportAs on generic model types by name | medium, file | Set export-as parameter on matching family types only, report list changed. |
| S35 `ru-dwg-revit-s013` | ru | в имена кракозябры вместо кириллицы, и единицы вроде в футах? проверь | Cyrillic names show as garbage and units look wrong | medium, file | Inspect IfcUnitAssignment and string encoding of names; report units and any escape-encoding issues. |
| S36 `en-blogs-linkedin-s011` | en | file is 800MB, what are the heaviest objects, bolts? triangle counts pls | Find overly detailed objects | hard, file | Estimate representation sizes per class/type, list top offenders, suggest filtering. |
| S37 `ru-fs-s007` | ru | ревит экспорт в ifc висит уже 3 часа, 500 мб rvt, что отключить чтоб побыстрее? | Revit IFC export hangs for hours | easy, no file | Explain export settings affecting speed: Current View Only, split by level, drop 2D elements, linked files, base quantities, geometry detail level; suggest steps. |
| S38 `zh-revit-export-s005` | zh | ifc文件1.2G也太大了吧，帮我看看哪些类型占的最多，能不能瘦身 | Why is this IFC so big, what dominates size | hard, file | Compute entity counts and byte share by class, report top contributors (property sets, repeated geometry), suggest export options. |

### 5. Batch jobs, reports, tools, handover data



| # / id | Lang | Prompt (SYNTHETIC) | Meaning (EN) | Difficulty | A good answer should |
|---|---|---|---|---|---|
| S39 `ru-autodesk-telegram-s017` | ru | прогони все 6 ифс из папки на наличие обязательных свойств и скинь одну сводную таблицу, сроки горят | Batch-check several IFC files for missing required psets | hard, file | Open each file, check required property sets/attributes, produce one consolidated table per file/class. |
| S40 `en-revit-auto-s005` | en | which project parameters, view filters and line patterns are unused? don't delete yet | Report unused project parameters and filters before cleaning | hard, file | Enumerate parameters, filters, line patterns, check usage in views/schedules/elements, return a read-only report and ask before any deletion. |
| S41 `en-revit-auto-s017` | en | whats the cheapest way to get an AI to do repetitive revit stuff, sheets/views/params? local model ok? | Cheapest way to let an AI agent automate Revit chores | easy, no file | Compare MCP servers for Revit and pyRevit, paid vs local models, note reliability and token cost, recommend starting small with read-only tasks. |
| S42 `en-model-checking-s013` | en | do I need Solibri if I already have simplebim and zoom? what does each one do for IFC QA | Which tool for what | easy, no file | Explain roles: Solibri rule-based checking, Simplebim data fixing, Zoom BCF issue handling. |
| S43 `en-psets-s010` | en | give me fill % per property for Pset_WallCommon across all walls, as table | Report fill rate of required properties | easy, file | Compute for each property in Pset_WallCommon the percent of IfcWall with non-empty values, output table. |
| S44 `en-cobie-s003` | en | take serials.csv and put SerialNumber + WarrantyEndDate on all IfcUnitaryEquipment matched by tag, then tell me what didnt match | Fill Pset_Warranty and serial number from a CSV for all air handling units. | hard, file | Match by Tag, write Pset_ManufacturerOccurrence.SerialNumber and Pset_Warranty dates, report unmatched rows both ways. |
| S45 `en-us-canada-infra-s002` | en | we owe COBie to the owner friday. check the ifc for type names, component names, spaces w/o floor, systems empty. what will fail the QC | Check COBie readiness before a federal handover | medium, file | Verify Type/Component/Space/Floor/System population, list missing names and orphan spaces, summarize likely COBie QC failures. |
| S46 `zh-zhihu-s016` | zh | 想选国产bim软件，ifc来回导一遍测完整性，该检查哪些点 | Plan an IFC roundtrip test to select domestic BIM software | medium, no file | Propose a test checklist: class counts, GUID persistence, psets, geometry, materials, coordinates; compare before/after. |

## How to role-play this persona in tests

**Voice.** Fuller sentences than the coordinator, but still work-chat style. Names the contract document ("EIR says...", "the BEP says 8 storeys", "client wants IFC4 RV", "наш ТЗ", "AIA-Check"). Wants a **yes/no plus reasons**, or **pass/fail per spec**, because the output goes into a delivery note. When angry, the target is the software vendor, not the assistant: "Revit 2027 mapping parameters severely lacking".

**Typical context.** Several files or several versions at once (v3 and v4; arch and struct), a named standard (Uniclass 2015, NL-SfB, КСИ, SZ-IFC, IFC+SG), a deadline tied to an issue date ("before the issue tonight", "we owe COBie to the owner friday"). Revit by far (named in 115 of the persona's 354 records, plus versioned entries such as Revit 2023 or 2027), then Archicad, Allplan, Tekla.

**Knowledge level.** High on process and contracts, medium on property sets (knows names like Pset_WallCommon.FireRating), low on schema internals. Understands IDS conceptually, struggles with its syntax. Will challenge a vague answer.

**Typical follow-ups.**
- "group the failures by discipline / by storey / by type name"
- "what's the percentage, not the count" (fill rate)
- "same check on the other 5 files and one summary table"
- "do it, but preview first, and save as a new ifc" (managers expect a preview-confirm-apply cycle)
- "is that in the standard or did you make it up?" (checks hallucination)
- "which IFC version does that need?" / "will it still work in 2x3?"

**Traps worth including.** A requirement that names a property without a set; Uniformat classification present but Uniclass required; type-level vs instance-level values; IFC4 vs IFC2x3 property placement; a file where "empty string" and "missing" differ; localized parameter names (German "Baugruppenkennzeichen"); a request that is really a policy question (should our EIR demand IFC4?), which needs a reasoned opinion with trade-offs, not a file query.

**How to judge the answer.**
1. Results are traceable: counts plus a way to list the failing elements (GlobalId, class, storey).
2. The assistant states which property set and which data type it looked at, and says "missing" vs "empty" vs "wrong type" separately.
3. No invented standards or property sets; "I cannot tell from the IFC" is accepted when it is true (for example, which Revit setting caused it).
4. Policy questions get a balanced answer (for example, one test on a 400-model hospital project in [en-blogs-linkedin-r022](https://bimcorner.com/is-the-industry-ready-for-ifc4/) argues for staying on IFC2x3), not a verdict.
5. Writes happen only after preview, to a new file, with a change log.
6. Multi-file requests give one table, not six separate answers.

**Related personas.** [Coordinator](bim_coordinator.md), [Architect](architect.md), [Owner / client](owner_client.md), [Reviewer / authority](reviewer_authority.md), [Facility manager](facility_manager.md).
