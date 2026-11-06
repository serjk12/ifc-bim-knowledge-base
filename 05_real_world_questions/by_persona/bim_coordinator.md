# BIM coordinator: who they are and what they do with IFC

**Last built: 2026-11-06 · Persona code:** `bim_coordinator` · **Data behind this page:** 949 records in the knowledge base (529 real, 420 synthetic; `python tools/kb.py stats --persona bim_coordinator`). Languages: en 631, ru 94, zh 79, de 31, es 21, it 19, ja 15, ko 15, nl 14, fr 11, pt 8 (+ no, ar). The largest persona in the base, so it is the best-evidenced one.

## In plain words

A BIM coordinator is the person who makes sure the drawings of different teams fit together *before* anyone builds. The architect, the structural engineer and the ventilation/plumbing/electrical engineers each model their own part in their own program. Each team sends the coordinator a file. The coordinator stacks all the files into one big 3D model ("federated model"), checks that every file is in the right place and has the right data, and hunts for **clashes** (a duct drawn straight through a beam). Then the coordinator writes down the problems as short issues and sends them back to the authors, usually every week.

Think of a person who receives six jigsaw pieces from six companies and has to say: "piece 3 is rotated, piece 5 is two kilometres to the left, and pieces 2 and 4 overlap here."

IFC is the neutral file format that makes this possible when teams use different programs (Revit, Archicad, Tekla, Renga, Allplan). The coordinator does **not** usually design anything; the coordinator checks, reports, compares and nags. In practice most of their questions are about *why the file they received is wrong* or *how to tell the sender to export it better*.

**What this person is not:** not the BIM manager who writes company standards and templates (see [BIM manager](bim_manager.md)), not the architect who draws the building (see [Architect](architect.md)), and not the authority that approves it (see [Reviewer / authority](reviewer_authority.md)). In the data the labels blur: several questions tagged `bim_coordinator` are really "I am the one who has to fix the export", written by people who also author models.

## Daily IFC tasks

| # | Task | What it looks like in practice | Evidence in the base |
|---|---|---|---|
| 1 | Collect the weekly files | Download IFC (or Revit links) from every discipline, check names and versions, load them into one place (Navisworks, Solibri, BIMcollab, ACC, a browser viewer). | [en-bsforum-r046](https://forums.buildingsmart.org/t/1957) (federated IFC), synthetic `en-navis-acc-s006`: "ifc upload failed in acc docs ... file is 900mb" |
| 2 | Intake check of every file | Right IFC version and view (2x3 Coordination View vs IFC4 Reference View), right units, right place, floors present, no pile of "proxy" objects, mandatory properties filled. | `validation_checking` 102 records, `versions_mvd` 47, `coordinates_georef` 139 |
| 3 | Run clash detection | Architecture vs structure, ducts vs beams, with a tolerance (for example 10 mm), usually "hard clashes only". | `clash_coordination_bcf` 96; synthetic `en-reddit-s010` |
| 4 | Make the clash list usable | Group hundreds of hits by system, floor or source object; send as BCF so the author's tool jumps to the element. | [en-coord-r009](https://community.osarch.org/discussion/3616/browser-based-ifc-clash-version-diff-how-would-you-group-clashes-and-handle-guid-churn) |
| 5 | Compare this week with last week | Which elements were added, deleted, moved or got different properties. Breaks when the exporter regenerates GlobalIds. | `guid_change_tracking` 61; `compare_versions` intent 42 |
| 6 | Tell the author what to change | "Map generic models to the right IFC class", "your shared parameters are not reaching the IFC", "use the same base point as the others". | `export_revit` 201, `class_mapping` 115, `psets_properties` 149 |
| 7 | Prepare submissions for a client or authority | Moscow AGR / state expertise, Shenzhen SZ-IFC self-check, Singapore CORENET X: run the checker's rules early, not after a 2-hour export. | [ru-autodesk-telegram-r008](https://habr.com/ru/articles/1089018/), [zh-lightweight-review-r002](https://zhuanlan.zhihu.com/p/633827596), synthetic `en-sg-corenetx-s001` |
| 8 | Small repairs when the author cannot | Re-class proxies to the right class, fill a missing property, reduce a heavy file. Risky: changes someone else's model. | synthetic `ru-dwg-revit-s004`, `de-dach-s012` |

## Goals

What the questions are really *for* (from the research reports and the records):

- **A weekly export that just works:** correct classes, properties, storeys and coordinates, so the federated model needs no rework.
- **Fast answers to "what is missing or wrong" before the meeting:** counts, lists by floor, GlobalIds the author can search for.
- **Short clash lists** grouped by system/floor/cause, with issues passed on as BCF.
- **Diffs that survive regenerated GUIDs** ("everything shows as deleted and re-created" is a known complaint).
- **To know whose fault it is:** the exporter, its settings, the receiving viewer, or the checker's rule. A recurring wish is a way to run the checker's rules *inside* the authoring tool before the slow export ([ru-autodesk-telegram-r008](https://habr.com/ru/articles/1089018/), [zh-lightweight-review-r002](https://zhuanlan.zhihu.com/p/633827596)).
- **Free or cheaper tools** that replace Navisworks/Solibri-style checks, plus a way to learn them.

## Pains (ranked)

_Quoted phrases in the last column are illustrative: some paraphrase real records, others are taken from the synthetic prompts further down. Only the tables of real records are evidence of what people actually wrote._

Ranked by how many records touch the topic (a record can have up to four topics, so counts overlap) and by how heated the tone is (roughly 27% of the persona's records are tagged `frustrated`, 16% `confused`, 7% `urgent`).

| Rank | Pain | Signal | Typical shape of the complaint |
|---|---|---|---|
| 1 | **Revit (or other) IFC export produces wrong or incomplete data** | `export_revit` 201, `psets_properties` 149, `class_mapping` 115 | "half my shared params aren't in the ifc", "everything is IfcBuildingElementProxy", "elements on the wrong floor", "type parameters gone after the exporter update" |
| 2 | **Files do not sit on top of each other** | `coordinates_georef` 139 | "arch ifc and struct ifc dont line up, one is 2 km off"; "levels at double height after Link IFC"; Russian: "улетает на километры от нуля" |
| 3 | **No quick way to know if a model is acceptable** | `validation_checking` 102, `ids_requirements` 57 | "check all IfcWall have FireRating before we send"; authority checker finds 200 clashes where Navisworks finds 1500 ([ru-habr-dev-r003](https://habr.com/ru/articles/1089018/)) |
| 4 | **Too many clashes, clumsy BCF** | `clash_coordination_bcf` 96 | "one misplaced run produces hundreds of clashes"; BCF viewpoints missing or statuses reset when syncing Solibri and BIMcollab |
| 5 | **Imported IFC is dead geometry in Revit** | `import_into_revit` 93 | "geometry is there but elements are not real objects and properties are missing" (Russian, Chinese, English alike) |
| 6 | **Version comparison and GUID churn** | `guid_change_tracking` 61 | "compare v3 and v4, what changed by guid"; issue history lost because GUIDs changed |
| 7 | **Slow, huge, crashing exports and viewers** | `geometry_quality` 66, `viewers_opening` 51, `file_size_performance` | Export "2 hours", "800 MB, viewer freezes", "crashes every time I export" |
| 8 | **Not knowing where to start / what the others expect** | `learning_basics`, unanswered surveys | Open pain-point surveys get zero replies ([en-coord-r001](https://forums.buildingsmart.org/t/bottlenecks-faced-by-bim-professioonals/6633)) |

## Vocabulary they use (and what they do not know)

### Words and phrases you will see

| Phrase (language) | What it means in plain terms |
|---|---|
| proxy, "проксей", "проксики", "プロキシ", "代理构件" (many) | An element the exporter could not classify; stored as the catch-all `IfcBuildingElementProxy`. Coordinators hate them because checks and quantities ignore them. |
| federate / federated model / "合模" (zh) / "Koordinationsmodell" (de) | Stacking all discipline files in one scene. |
| clash, "коллизии", "пересечения", "Kollisionen", "碰撞", "interferência" | Two objects occupy the same space. "Hard" clash = overlap; "soft" = too close. |
| BCF, "бцф", "BCF-Liste" | Small file or API object carrying an issue plus a camera view and the affected GlobalIds. |
| GUID / GlobalId / "GUID churn" | The 22-character identity of an element. "Churn" = it changes between exports. |
| mapping table, IfcExportAs, "таблица соответствия", "Mapping" | The setting that decides which IFC class each Revit category/family becomes. |
| pset, "психеты", Pset_WallCommon, "custom pset", UDPS | Named property groups on elements (fire rating, is-external, load-bearing). |
| CV2.0, RV, DTV, "MVD", "Fachmodell" | Which "view" of IFC the export follows; the sender must match what the receiver expects. |
| PBP, survey point, shared coordinates, "базовая точка", "Projektbasispunkt", "项目基点" | Revit's reference points; the source of most "model lands far away" problems. |
| "ифс", "ифц", "ревит", "навис" (ru slang) | IFC, Revit, Navisworks written phonetically. Common in chat-style Russian requests. |
| "АГР", "экспертиза", "ТЭП", "МССК", "КСИ" (ru) | Moscow architectural approval, state expertise, technical-economic indicators, classifier codes. See [Russia](../../02_standards_regulations/national/russia.md). |
| "SZ-IFC", "IFC+SG/CORENET X" | Local IFC profiles with their own self-check tools ([China](../../02_standards_regulations/national/china_mainland.md), [Singapore](../../02_standards_regulations/national/singapore.md)). |

### What they typically do not know, or get wrong

- **That the answer depends on the exporter version and settings.** The same Revit file gives different results with different exporter builds ([en-fmor-r009](https://github.com/IfcOpenShell/IfcOpenShell/issues/3978)); they rarely name the build.
- **That the Revit category does not decide the IFC class.** Several Russian posts learn this the hard way: the class comes from the "Export to IFC / IfcExportAs" parameters, not from the category ([ru-habr-dev-r009](https://habr.com/ru/articles/1098340/)).
- **That "Open IFC" and "Link IFC" in Revit behave differently**, and neither gives editable native walls ([en-autodesk-revit-import-r003](https://github.com/Autodesk/revit-ifc/issues/223); also [ru-dwg-other-r008](https://forum.dwg.ru/showthread.php?t=154396)).
- **That very little software reads `IfcMapConversion`** (the record that ties the model to map coordinates) ([en-coord-r027](https://forums.buildingsmart.org/t/we-have-a-problem-with-ifcmapconversion/5695)), so "it has georeferencing" does not mean the receiver will use it.
- **That IDS cannot check geometry or conditional logic** ([ru-habr-dev-r015](https://habr.com/ru/articles/908192/)); an IDS that checks a code *pattern* cannot tell whether the code *fits* the element ([nl-dutch-r002](https://github.com/OpenAEC-Foundation/OpenAEC-BIM-validator/issues/22)).
- **What to attach.** Responders keep asking for the IFC and software version; askers omit them. Test prompts should do the same.

For definitions behind these terms see [IFC in real projects](../../01_ifc_basics/00_ifc_in_real_projects.md), [spatial structure](../../01_ifc_basics/04_spatial_structure_and_relationships.md), [geometry/coordinates/units](../../01_ifc_basics/06_geometry_placement_coordinates_units.md), the [glossary](../../08_glossary/glossary_multilingual.md) and the topic pages [Revit export and class mapping](../by_topic/revit_export_and_class_mapping.md), [coordinates](../by_topic/coordinates_georef_units_levels.md), [clash/BCF/CDE](../by_topic/coordination_clash_bcf_cde.md), [validation/IDS](../by_topic/validation_ids_model_checking.md), [versions/MVD/GUID](../by_topic/versions_mvd_encoding_guid.md).

## Real questions (60, linked)

Paraphrases of questions seen at the linked sources, kept in the asker's language and register (not verbatim quotes except short titles). "Lang" is the language of the post. The English gloss is the researcher's summary. Language mix in this list: Russian 15, English 24, other languages 21. Where a source page is not in English but the stored paraphrase is (the researcher wrote it in English), the Lang column still shows the page language.

### A. The export is wrong: classes, properties, levels, areas

Mostly Revit, mostly "my IFC arrives with things missing or mislabeled". The Russian block comes from people preparing models for a state checker (АГР / expertise) and shows how much the checker's rules shape the question.

| # | Lang | Their words (paraphrase, original language) | English gloss / context | Source (record id, type, year) |
|---|---|---|---|---|
| 1 | ru | таблица категория-класс врёт, в IFC класс берётся из параметров экспорта; в 2022 и старше только IfcExportAs | Revit category-to-IFC-class table is unreliable; export actually reads Export to IFC / IfcExportAs parameters | [ru-habr-dev-r001](https://habr.com/ru/articles/1089018/) blog, 2026 |
| 2 | ru | стандартный параметр Экспорт в IFC ненадёжен: косоуры выгружаются при Нет; категория Стена - откатные ворота | Revit category does not determine IFC class; a Wall-category element turned out to be a sliding gate family | [ru-habr-dev-r009](https://habr.com/ru/articles/1098340/) blog, 2026 |
| 3 | ru | тяжёлая модель выгружается 2 часа, ошибки видно только после загрузки в строимпросто, зоны пропадают, площади задваиваются | Heavy model exports IFC in 2 hours and errors only show after upload to the Moscow AGR checker; rooms vs zones, vanished zones, area overcounting | [ru-autodesk-telegram-r008](https://habr.com/ru/articles/1089018/) blog, 2026 |
| 4 | ru | числовой параметр не переносится, если не запятая; помещения не классифицируются по МССК | Numeric parameter in IFC needs a comma, otherwise value is not transferred; rooms not classified by MSSK | [ru-habr-dev-r011](https://habr.com/ru/articles/1098340/) blog, 2026 |
| 5 | ru | валидатор ругается, что площадь IfcArea а не IfcReal; глобальная замена в блокноте ломает Pset_* | Exporter writes areas/volumes as IfcArea or IfcLabel instead of IfcReal and the IDS validator rejects them | [ru-habr-dev-r004](https://habr.com/ru/articles/1094224/) blog, 2026 |
| 6 | en | Custom properties defined in the user-defined property set file do not appear in the exported IFC. |  | [en-autodesk-revit-export-r004](https://forums.autodesk.com/t5/revit-architecture-forum/revit-ifc-export-user-defined-properties-won-t-export/td-p/9767878) forum, 2020 |
| 7 | en | Some shared parameters are exported by one team member and missing for another; how to create a property set so parameters are included. |  | [en-autodesk-revit-export-r010](https://help.autodesk.com/view/RVT/2025/ENU/?caas=caas%2Fsfdcarticles%2Fsfdcarticles%2FCertain-shared-parameters-not-exportetd-to-IFC-from-Revit.html) vendor_kb, 2025 |
| 8 | de | type parameters missing in IFC after exporter update; user-defined pset file worked before | Type parameters no longer export through user-defined property sets in new exporter versions. | [en-blogs-linkedin-r009](https://bim-me-up.com/revit-typenparameter-nach-ifc-exportieren/) blog, 2023 |
| 9 | de | elements end up on the wrong floor in IFC | Elements on levels not flagged Building Story land on the wrong IfcBuildingStorey. | [en-blogs-linkedin-r016](https://bim-me-up.com/ifcbuildingstorey/) blog, 2024 |
| 10 | zh | Revit导出IFC时各类别对应哪个IFC类，贴出导出图层/类别映射文件 | Dumps the Revit IFC export category-to-IFC-class mapping table (walls->IfcWall, pipes->IfcPipeSegment, many annotation categories unmapped). | [zh-csdn-dev-r007](https://www.cnblogs.com/liaocheng/p/15905467.html) blog, 2022 |
| 11 | zh | Revit导IFC哪些信息会丢，类别对不上IFC类、坐标转换没了 | What information is lost when exporting Revit to IFC (class mapping, predefined type, no IfcMapConversion, proxy fallback). | [zh-lightweight-review-r006](https://bbs.co188.com/thread-10112116-1-1.html) forum, 2022 |
| 12 | it | esporto da Revit ma i parametri custom non finiscono nei Pset, come li mappo? | Revit to IFC conversion setup: class mapping, IfcExportAs, MVD, shared coordinates, custom Psets via schedules or parameter file. | [it-italy-r011](https://biblus.acca.it/conversione-modello-bim-in-ifc5/) vendor_kb, 2026 |

### B. The models do not line up: origin, base point, shared coordinates

"Lands miles away", "rotated", "levels at double height". Usually a coordinate-system mismatch, and the asker rarely says which Revit point they used.

| # | Lang | Their words (paraphrase, original language) | English gloss / context | Source (record id, type, year) |
|---|---|---|---|---|
| 13 | ru | базовая точка, точка съёмки, внутреннее начало | All about points in Revit: project base point, survey point, internal origin | [ru-autodesk-telegram-r035](https://www.youtube.com/watch?v=soPG0YMueqY) video, 2022 |
| 14 | en | In 2025-2027 Link IFC positions geometry higher than it should be and creates levels at twice the correct elevation. Open IFC is fine. In 2023/2024 Z maps correctly to Project Base Point. | Link IFC in Revit 2025-2027 puts the building too high and levels at double the elevation; Open IFC handles it better. | [en-autodesk-revit-import-r001](https://github.com/Autodesk/revit-ifc/issues/990) github_issue, 2026 |
| 15 | en | Export offers internal origin, survey point or PBP; import offers nothing; cites an old Revit Ideas post saying it is not possible. | Export lets you choose the origin but import always uses the internal origin; can import use the project base point? | [en-autodesk-revit-import-r004](https://github.com/Autodesk/revit-ifc/issues/320) github_issue, 2021 |
| 16 | en | Models with shared coordinates look right in other viewers but not in Revit; has googled and watched videos but is unsure how to link IFC properly. | Georeferenced IFCs line up in Trimble and BIM Vision but not when linked in Revit 2022; is there an easy way? | [en-autodesk-revit-import-r005](https://github.com/Autodesk/revit-ifc/issues/566) github_issue, 2022 |
| 17 | es | opening or linking an IFC gives no choice of coordinate system | Arkance article: a linked/opened IFC in Revit offers no coordinate system choice, so shared coordinates and origin are absent; workaround steps. | [es-spain-r016](https://emea.support.arkance.world/hc/es/articles/36464850969234-Using-IFC-files-with-a-Shared-Coordinates-system) vendor_kb, 2025 |
| 18 | zh | 链接的各个模型基点不一致怎么办 | Imported models have inconsistent base points; what to do? | [zh-revit-export-r021](https://www.jianshu.com/p/409188142cfa) blog |
| 19 | zh | 群楼每人建一栋，测量点基点怎么设才能定位拼起来，求教 | Several people model podium buildings separately; how to set survey/base point to position each building? | [zh-revit-export-r023](https://zhidao.baidu.com/question/1755259387786621668.html) qa_site |
| 20 | it | i modelli IFC non si sovrappongono, uno e fuori di km, dove imposto origine e coordinate del sito prima di esportare? | My IFC models do not line up / float; how to set origin and georeference IfcSite before export? | [it-italy-r005](https://biblus.acca.it/ifc-coordinate-system/) vendor_kb, 2023 |
| 21 | nl | In een federatie van bouwkunde, constructie en installaties gaat het vaak mis doordat modellen niet op hetzelfde nulpunt liggen. Rapporteer per model schema, lengte-eenheid, IfcSite ref, MapConversion (EPSG 28992), afstand tot oorsprong | Federated models often don't share the same origin so clash detection is pointless; report CRS, units, distance to origin per model | [nl-dutch-r008](https://github.com/OpenAEC-Foundation/OpenAEC-BIM-validator/issues/21) github_issue, 2026 |
| 22 | de | model lands in the wrong place or invisible in viewer after IFC export; which Revit origin should be used? | Revit has several origins; where does my IFC land in other software and does shared coordinates matter for GIS? | [en-blogs-linkedin-r007](https://bim-me-up.com/revit-ifc-und-koordinatensysteme/) blog, 2023 |

### C. Federation, clashes and BCF issues

Turning many raw clashes into something a human can act on, and moving issues between tools.

| # | Lang | Their words (paraphrase, original language) | English gloss / context | Source (record id, type, year) |
|---|---|---|---|---|
| 23 | en | Is system x storey x source object the right granularity for clash lists? When Revit regenerates GlobalIds a GUID-only diff shows everything deleted and recreated - any heuristic that holds on real exports? Do non-viewer users want a PDF/HTML change log or is BCF enough? | How to group clash lists sensibly and how to diff model versions when Revit/Archicad regenerate GlobalIds. | [en-coord-r009](https://community.osarch.org/discussion/3616/browser-based-ifc-clash-version-diff-how-would-you-group-clashes-and-handle-guid-churn) forum, 2026 |
| 24 | ru | Навис показывает 1500 коллизий, сервис 200 - почему разное число | Navisworks finds ~1500 clashes, the check service ~200 on the same model | [ru-habr-dev-r003](https://habr.com/ru/articles/1089018/) blog, 2026 |
| 25 | ru | при выгрузке в Navisworks SweptSolid отображается некорректно, нужна Tessellation | What geometry representation should Renga IFC use for Navisworks? | [ru-dwg-other-r028](https://rengabim.com/stati/prohodim-gosekspertizu-informacionnoj-modeli-pravilno/) blog, 2022 |
| 26 | en | distribute multiple IFC files as a single file; ifczip with multiple IFCs is unsupported by viewers; STEP references also unsupported |  | [en-bsforum-r046](https://forums.buildingsmart.org/t/1957) forum, 2019 |
| 27 | en | asks for a standardized catalog of spatial/clash rules (collision, above, front, parallel) like IDS but for 3D data |  | [en-bsforum-r039](https://forums.buildingsmart.org/t/6311) forum, 2025 |
| 28 | en | clash annotation shows far from objects because project units are feet | Clash visualization assumes mm so markers appear far away when project is in feet | [en-gh-ifcopenshell-r008](https://github.com/IfcOpenShell/IfcOpenShell/issues/7178) github_issue, 2025 |
| 29 | it | come uso i BCF per segnalare errori nell'IFC all'autore? | BCF markups in openBIM workflows. | [it-italy-r024](https://biblus.acca.it/markups-bcf-workflow-openbim/) vendor_kb, 2026 |
| 30 | en | my custom Solibri statuses turn into Active after sync, why | Issue statuses in Solibri change after syncing to BIMcollab | [en-model-checking-r001](https://helpcenter.bimcollab.com/en/articles/340730-why-is-issue-status-in-solibri-changed-after-synchronization-to-bimcollab) vendor_kb |
| 31 | en | my edits to issues in BIMcollab got overwritten after Solibri sync | Issue data was overwritten by Solibri | [en-model-checking-r005](https://helpcenter.bimcollab.com/en/articles/340732-why-was-my-issue-data-overwritten-by-solibri) vendor_kb |

### D. "Is this model OK?" Checks, IDS, classification, authority checkers

The coordinator as gatekeeper before a delivery.

| # | Lang | Their words (paraphrase, original language) | English gloss / context | Source (record id, type, year) |
|---|---|---|---|---|
| 32 | ru | с 01.07.2019 госэкспертиза требует BIM, как проверять проект в Revit или IFC, можно ли PDF и чертежи, как быть с 87 постановлением, методики нет | From 1 July 2019 state expertise reportedly requires BIM; how do we check a Revit project or IFC model, can PDF drawings be used instead? | [ru-autodesk-telegram-r001](https://forum.dwg.ru/showthread.php?t=153428) forum, 2019 |
| 33 | ru | косоуры всё равно выгружаются при IfcExportAs нет, пандус уходит как IfcRampFlight, МССК коды помещениям вручную | Preparing a model for AGR: each element needs IFC class and attributes; stair stringers still export when set to No; ramp as IfcRampFlight needs another classifier code | [ru-autodesk-telegram-r011](https://habr.com/ru/articles/1098340/) blog, 2026 |
| 34 | ru | площади ТЭП в xml расходятся на 20 м2, дубли не найти, как править IFC без ревита и переслать правки | TEP areas differ ~20 m2 from AGR XML; duplicates hard to find; how to post-process IFC without Revit and share fixes without resending big files | [ru-autodesk-telegram-r010](https://habr.com/ru/articles/1100956/) blog, 2026 |
| 35 | en | if models are federated into one IFC file, how to merge or apply the several IDS files that validate each discipline? |  | [en-bsforum-r024](https://forums.buildingsmart.org/t/5654) forum, 2024 |
| 36 | en | a property with IFCTEXT instead of IFCLABEL is silently omitted from the check |  | [en-bsforum-r051](https://github.com/buildingSMART/IDS/issues/337) github_issue, 2024 |
| 37 | en | an empty IFCLABEL value passes a required check |  | [en-bsforum-r052](https://github.com/buildingSMART/IDS/issues/403) github_issue, 2025 |
| 38 | en | IDS rule restricting IfcBeam PredefinedType to BEAM or PILECAP passes only one of six beams; user asks if this is a bug in IfcTester or a misunderstanding of IDS. |  | [en-osarch-r007](https://community.osarch.org/discussion/3478/ifctester-not-properly-check-predefinedtype-requirements) forum, 2026 |
| 39 | nl | IDS controleert alleen het patroon van de NL-SfB code, niet of de code bij het element past; IfcWall met 32.xx is formeel goed en inhoudelijk fout. Wil codelijst, koppeling IfcWall->21/22, IfcDoor->31/32 en controle waar de code staat (IfcClassificationReference) | An IDS can check the pattern of an NL-SfB code but not whether the code fits the element; an IfcWall with 32.xx (doors) passes formally | [nl-dutch-r002](https://github.com/OpenAEC-Foundation/OpenAEC-BIM-validator/issues/22) github_issue, 2026 |
| 40 | nl | BIMcollab Smart Views, Dalux-filters en Solibri checking views kleuren op eigenschap: per brandwerendheid, NL-SfB-code, of rood voor 'LoadBearing ontbreekt' | Colour/filter elements by property (fire rating, NL-SfB code, red for 'LoadBearing missing') to see model gaps at a glance | [nl-dutch-r012](https://github.com/OpenAEC-Foundation/OpenAEC-BIM-validator/issues/17) github_issue, 2026 |
| 41 | zh | 报建前能不能在Revit里先自检，不用每次导出IFC再检测 | Pre-check the model inside Revit before exporting SZ-IFC for Shenzhen filing. | [zh-lightweight-review-r002](https://zhuanlan.zhihu.com/p/633827596) blog, 2023 |
| 42 | en | validation report gives errors but how do I find them in the file | How to inspect raw IFC files and trace errors flagged by the validation service. | [en-blogs-linkedin-r032](https://bimcorner.com/analyzing-ifc-files/) blog, 2024 |

### E. Versions and GUID churn: what changed since last week?

Comparing exports and keeping issue history alive when identifiers change.

| # | Lang | Their words (paraphrase, original language) | English gloss / context | Source (record id, type, year) |
|---|---|---|---|---|
| 43 | en | exported the same file twice with identical settings and Room GUIDs differ when store-GUID-in-parameter option is checked, also on 22.5.2.0 | Room IFC GUIDs change on every export when 'Store the IFC GUID in an element parameter' is enabled | [en-revitifc-guid-r012](https://github.com/Autodesk/revit-ifc/issues/521) github_issue, 2023 |
| 44 | en | model and linked model exported into same IfcSite give IfcGuids in the file that differ from the GUIDs reported by the API/UI | Federated export of host plus linked model gives IfcGuids that differ from the ones returned by ExportIFCUtils and shown in UI | [en-revitifc-guid-r013](https://github.com/Autodesk/revit-ifc/issues/825) github_issue, 2024 |
| 45 | it | ho due revisioni dello stesso IFC, come vedo cosa e cambiato (aggiunti, rimossi, modificati)? | How do I detect what changed between two IFC versions of a model? | [it-italy-r009](https://biblus.acca.it/rilevare-modifiche-nei-modelli-ifc/) vendor_kb, 2025 |
| 46 | zh | revit2020导出的ifc没有guid，为什么 | Why does Revit 2020 not generate IFC GUIDs? | [zh-revit-export-r017](https://www.zhihu.com/question/625548241) qa_site, 2023 |
| 47 | it | ho un IFC ricevuto dal collega, devo modificare le proprieta ma il viewer e solo lettura e i muri sono finiti come proxy, come faccio senza rompere i GUID? | Editing an IFC is painful: walls turn into proxies, properties are read-only, GUIDs change after bulk edits. | [it-italy-r001](https://biblus.acca.it/problemi-editing-file-ifc/) blog, 2025 |
| 48 | en | Linking an updated IFC generates a new rvt and a new shared parameter file with different GUIDs even for identical pset names. | Every re-link of an updated IFC creates new shared parameter GUIDs, breaking schedules. | [en-autodesk-revit-import-r017](https://github.com/Autodesk/revit-ifc/issues/408) github_issue, 2022 |
| 49 | en | Exporting IFC4x3 Reference View yields header ViewDefinition [CoordinationView] instead of ReferenceView. |  | [en-gh-revit-ifc-r019](https://github.com/Autodesk/revit-ifc/issues/1013) github_issue, 2026 |
| 50 | en | Space boundaries lose links to envelope elements under IFC4x3 but IFC4 Reference View works. |  | [en-autodesk-revit-export-r033](https://forums.autodesk.com/t5/revit-architecture-forum/revit-ifc4x3-export-incorrect-space-boundaries/m-p/14048745) forum, 2025 |

### F. Import, viewing, size, and the "where do I even start" questions

Including one real survey of pains that got zero replies (a lesson in how not to phrase a test).

| # | Lang | Their words (paraphrase, original language) | English gloss / context | Source (record id, type, year) |
|---|---|---|---|---|
| 51 | ru | при импорте IFC геометрия есть, но элементы не распознаются как объекты, пропадают параметры, нужно получить модель для чертежей | On IFC import geometry stays but elements are not real objects and properties are missing; which export settings or software to use? | [ru-autodesk-telegram-r004](https://forum.dwg.ru/showthread.php?t=166052) forum, 2022 |
| 52 | ru | IFC из Сапфира в автокад не импортируется, системная ошибка, в BimSight открывается нормально; как правильно экспортировать | IFC exported from SAPFIR opens in BIMsight but AutoCAD 2020 import fails with System Error; how to export/import correctly? | [ru-dwg-other-r003](https://forum.dwg.ru/showthread.php?t=160240) forum, 2021 |
| 53 | ru | после экспорта в IFC из Ревита часть элементов и параметров потерялась, как проверить где проблема - в экспорте или в просмотрщике | Newcomer: Revit IFC export loses elements and parameters; how to check the exported data? | [ru-dwg-other-r008](https://forum.dwg.ru/showthread.php?t=154396) forum, 2019 |
| 54 | ja | I tried to make a Revit add-in that converts IFC elements into MEP elements and could not make it work. | Story of trying to build an add-in converting imported IFC elements into native Revit MEP elements and failing. | [ja-coord-r015](https://qiita.com/KengoTanaka-BIM/items/6cec74e04bf581b21cf5) blog |
| 55 | zh | Revit打开IFC元素丢失或变形怎么办 | Opening IFC in Revit loses elements or deforms them; how to fix? | [zh-csdn-dev-r031](https://ask.csdn.net/questions/8391346) qa_site, 2025 |
| 56 | en | Revit-exported IFCs show an 'Opening Cuts Skipped' message on opening; pressing Apply Openings fixes it. Bug or intended? |  | [en-osarch-r012](https://community.osarch.org/discussion/3754/opening-cuts-skipped-in-bonsai-studio-0-9) forum, 2026 |
| 57 | en | tried to open 780 MB IFC in Bonsai 5.2/5.3 on M4 Max 128 GB; Blender memory climbs to 340+ GB; a similar 400 MB file uses 8-11 GB; ODA OpenIFCViewer opens it fine | A 780 MB IFC exported from proprietary software eats 340 GB RAM in Bonsai and never loads, while the ODA viewer opens it with 12 GB | [en-fs-r002](https://github.com/IfcOpenShell/IfcOpenShell/issues/9826) github_issue, 2026 |
| 58 | ru | выгрузить пачку rvt в IFC с разными настройками, экономя память | Batch export many .rvt to IFC with per-model Excel/JSON settings and workset exclusion | [ru-habr-dev-r024](https://github.com/i-savelev/BatchIfcExporter) github_issue, 2025 |
| 59 | en | I have a question for BIM professionals: what is the most annoying, frustrating thing in everyday work and how much time does it waste per day? | Asks BIM professionals what the most frustrating thing in daily work is and how much time it wastes. | [en-coord-r001](https://forums.buildingsmart.org/t/bottlenecks-faced-by-bim-professioonals/6633) forum, 2026 |
| 60 | de | linked IFC bloats my project; should I use Data Exchange instead? | Linked IFC vs Autodesk Data Exchange in Revit: size, performance, use cases. | [en-blogs-linkedin-r010](https://bim-me-up.com/ifc-verlinken-vs-data-exchange-laden-in-revit/) blog, 2025 |

## Ready test prompts (48, synthetic)

**All prompts below are SYNTHETIC**: written by the research agents in the style of the real questions above (see `inspired_by` in `research_raw/`), never real quotes. They assume an IFC file is loaded unless the last column says "no file". The "good answer" column is the researchers' expected behavior, shortened.

### 1. "What is in this file?" Proxies, properties, summary

Typically the first thing asked on a model received from somebody else.

| # / id | Lang | Prompt (SYNTHETIC) | Meaning (EN) | Difficulty | A good answer should |
|---|---|---|---|---|---|
| S1 `en-aimcp-s001` | en | how many IfcBuildingElementProxy in here and what revit category did they come from | How many elements are proxies and where from | medium, file | Count proxies, group by Pset/ObjectType/Revit category, report counts and suggest remapping. |
| S2 `ru-autodesk-telegram-s001` | ru | глянь сколько в модели проксей и из каких категорий ревита пришли, надо понять что перемапить | Count proxies and list which Revit categories they came from | medium, file | Count IfcBuildingElementProxy, group by Revit category/ObjectType property, report counts and propose IfcExportAs mapping fixes. |
| S3 `pt-brazil-s001` | pt-BR | cara olha o ifc e me fala quantos elementos viraram proxy e de qual categoria do revit, preciso mandar a compatibilização hoje | List elements exported as IfcBuildingElementProxy and the Revit category each came from | medium, file | Count IfcBuildingElementProxy, group by Revit category/ObjectType, report counts and mapping fixes. |
| S4 `ja-japan-s001` | ja | このIFC、IfcBuildingElementProxyが何個あるか数えて、元のRevitカテゴリ別に集計して。マッピング直す対象知りたい | Count proxy elements and which Revit categories they came from | medium, file | Count IfcBuildingElementProxy, group by ObjectType/Revit category property, report counts, suggest IfcExportAs mapping fixes. |
| S5 `de-dach-s002` | de | wieviele IfcBuildingElementProxy sind in dem Export und aus welchen Revit-Kategorien kommen die? Mapping stimmt irgendwie nicht | Count proxies and their Revit categories. | medium, file | Count IfcBuildingElementProxy, group by category/ObjectType, suggest mapping table fixes. |
| S6 `ru-autodesk-telegram-s010` | ru | какие параметры ревита вообще дошли до ифс, покажи психеты у одной стены и скажи чего нет | Which Revit parameters ended up in IFC property sets | easy, file | Dump property sets and quantity sets of a sample IfcWall, note presence/absence of expected custom parameters, mention export 'Revit property sets' option. |
| S7 `en-navis-acc-s001` | en | can u list everything in the ifc that has no property sets, navis shows empty tabs for a bunch of stuff | Check which elements in the Navisworks-bound IFC have no properties at all | medium, no file | List elements with zero IfcPropertySet/QTO relations, group by IFC class, flag likely export-setting causes. |

### 2. Where does the model sit? Coordinates, origin, units



| # / id | Lang | Prompt (SYNTHETIC) | Meaning (EN) | Difficulty | A good answer should |
|---|---|---|---|---|---|
| S8 `en-autodesk-revit-import-s002` | en | this ifc keeps showing up miles away in revit when i link, check if coords are huge | Check for huge coordinates that break the Revit link | medium, file | Compute geometry extents, flag values beyond ~10 km, suggest re-export or shifting origin. |
| S9 `ru-autodesk-telegram-s006` | ru | АР и ОВ в ифс не совмещаются по координатам, вроде одна точка съёмки везде, глянь где у них смещение | ARC and MEP models land in different places after IFC export | hard, file | Read IfcMapConversion/IfcSite location and placement origins of each file, compute offset, explain base point vs survey point export setting. |
| S10 `de-dach-s003` | de | wo sitzt der Projektbasispunkt in der IFC und stimmt die Nordrichtung? Fachmodelle passen nicht übereinander | Check where the project base point and the site are located and whether rotation is correct. | hard, file | Read IfcMapConversion, IfcProjectedCRS, IfcSite reference lat/long, placements; report offsets and true north, compare across files. |
| S11 `it-italy-s003` | it | i modelli non si sovrappongono. controlla IfcSite lat/long/quota e il CRS e dimmi se l'origine e sballata | Check IfcSite coordinates and CRS | hard, file | Read IfcSite RefLatitude/RefLongitude/RefElevation, IfcMapConversion/CRS, placement offsets; report anomalies. |
| S12 `fr-francophone-s010` | fr | mon IFC est décalé de plusieurs km dans le viewer, regarde le géoréférencement RGF93 / Lambert 93 de la maquette | Check georeferencing and project base point of the model | hard, file | Read IfcMapConversion/IfcProjectedCRS, site placement; report CRS, offsets, suggest fixes. |
| S13 `en-reddit-s002` | en | architect's ifc lands 40km from my model in navis. can you check the site/project base point and map conversion in the file | Check why the model sits far from origin | hard, file | Inspect IfcSite placement, IfcMapConversion/IfcProjectedCRS, report offsets and likely cause. |
| S14 `en-tekla-s006` | en | compare site placement and true north of struc IFC vs arch IFC, why 9 m off? | Compare placement of the structure and architecture IFCs | hard, file | Read IfcSite/IfcMapConversion, project north angle of both files, compute offset/rotation difference. |

### 3. Clashes and BCF

Tolerances, grouping and BCF output are the three details a good answer must not forget.

| # / id | Lang | Prompt (SYNTHETIC) | Meaning (EN) | Difficulty | A good answer should |
|---|---|---|---|---|---|
| S15 `en-reddit-s010` | en | run clash between ducts and structural beams, hard clashes only, tolerance 10mm, group by level | Find hard clashes between disciplines | hard, file | Compute geometric intersections, filter tolerance, group by storey, optionally emit BCF. |
| S16 `ru-renga-nanocad-s014` | ru | найди пересечения труб с балками и скинь в бцф | Find clashes between pipes and structural beams, export as BCF | hard, file | Compute geometric intersections between IfcPipeSegment and IfcBeam, list clashing GlobalId pairs, and produce BCF-ready data. |
| S17 `ru-clash-s007` | ru | прогони коллизии вентиляция vs балки, допуск 20мм, сгруппируй по этажам, без касаний | Find clashes between ventilation ducts and beams, group by level | medium, file | Run clash between IfcDuctSegment/fittings and IfcBeam with 20 mm tolerance, exclude touching, group per IfcBuildingStorey and report counts. |
| S18 `de-coord-s011` | de | kannst du mir Kollisionen zwischen Lüftungskanälen und Unterzügen im Koordinationsmodell raussuchen und nach Geschoss gruppieren? für die BCF Liste | Hard clashes between TGA ducts and structural beams. | hard, file | Run clash between IfcDuctSegment and IfcBeam across federated files, group by storey, prepare BCF-style issue list. |
| S19 `zh-clash-s009` | zh | 帮我把机电和结构ifc做个碰撞检查，管线和梁柱，容差5mm，导出报告和bcf | Check pipe vs structure clashes in IFC and export a report | medium, file | Run MEP-vs-structure clash, tolerance 5 mm, produce report grouped by clash pair and export BCF. |
| S20 `fr-francophone-s017` | fr | fais un clash gaines vs structure, tolérance 2 cm, et sors les points en BCF | Find clashes between ducts and structure and export BCF | hard, file | Run clash between IfcDuctSegment and structural elements with tolerance; output grouped clashes and BCF. |
| S21 `no-norway-s010` | no | kollisjonskontroll RIV mot RIB, lag BCF av de over 50 mm | Find clashes between ventilation and structure and export as BCF | hard, file | Run clash check with tolerance, filter, create BCF topics with viewpoints and GUIDs. |
| S22 `pt-brazil-s007` | pt-BR | roda clash entre dutos e vigas da estrutura e gera os apontamentos em BCF pra mandar pro projetista | Find clashes between ducts and structural beams and create BCF issues | hard, file | Run geometric clash between MEP and structure elements, output list with GUIDs, export BCF topics. |
| S23 `ko-clash-s015` | ko | ifc 간섭검토 할때 오탐이 너무 많은데 어떻게 줄여요? 접촉은 제외하고 싶음 | How to reduce false-positive clashes in IFC for a federated model | easy, no file | Explain tolerance, allow touching, rule-sets by discipline, openings/sleeves, grouping and clash filtering. |

### 4. Checks before the meeting or submission



| # / id | Lang | Prompt (SYNTHETIC) | Meaning (EN) | Difficulty | A good answer should |
|---|---|---|---|---|---|
| S24 `ru-autodesk-telegram-s002` | ru | завтра сдача в АГР, проверь что у всех IfcWindow заполнен RUS_Height и не пустой, список без параметра выдай | Before submitting to AGR check all windows have RUS_Height filled | easy, file | Iterate IfcWindow, read property RUS_Height in all psets, list GlobalId/Name/level of elements with missing or empty values. |
| S25 `ru-tim-expertiza-s001` | ru | надо сдавать на экспертизу в понедельник, проверь ифс что у всех стен и перекрытий заполнены обязательные свойства по требованиям заказчика, список пустых выгрузи | Check whether the IFC is ready to submit for state expertise: required properties filled | medium, file | Iterate walls and slabs, check the required property list (ask for it or read from a loaded requirements file), report elements with missing or empty values grouped by class and storey. |
| S26 `en-osarch-s003` | en | run this IDS against the model, I want every IfcBeam to have PredefinedType BEAM or PILECAP. which ones fail and why? |  | medium, file | Run IDS audit with entity facet predefinedType, list failing GlobalIds and failure reasons, note occurrence vs type PredefinedType. |
| S27 `en-osarch-s015` | en | check model with IDS and give me a bcf of the failures |  | hard, file | Run IDS, create BCF topics per failing element with GlobalIds; mention snapshot limits. |
| S28 `en-model-checking-s003` | en | how many elements have no classification reference at all? by IFC class pls | Classification completeness | easy, file | Count elements without IfcClassificationReference, group by class, report percentage. |
| S29 `nl-dutch-s003` | nl | check of de NL-SfB codes wel kloppen bij het element, die IfcWall met 32.xx bijv | Does code match element type | hard, file | Check main group vs IFC class (walls 21/22, doors 31/32), report mismatches, state mapping is interpretive. |
| S30 `en-model-checking-s016` | en | color elements by FireRating, grey for empty - and tell me how many are empty | Smart view by fire rating | medium, file | Group elements by FireRating value, report counts including empty, suggest color mapping. |
| S31 `en-sg-corenetx-s001` | en | cx submission tomorrow, checker gave IFC0000104. find shapes w/o ContextOfItems and empty IfcClosedShell in this ifc | Check the IFC for causes of IFC0000104 before CX submission | medium, file | Scan IfcShapeRepresentation without ContextOfItems and IfcClosedShell with empty CfsFaces; list GlobalIds and names; propose fixes without deleting elements. |
| S32 `ru-habr-dev-s001` | ru | найди в модели все свойства RUS_* где значение лежит как IfcLabel или IfcArea, а не IfcReal, список по элементам с GlobalId | Find properties where value is IfcLabel/IfcArea instead of IfcReal | medium, file | Scan property sets, filter RUS_* by nominal value type, report GlobalId, pset, property, current type; change nothing. |

### 5. Compare two versions



| # / id | Lang | Prompt (SYNTHETIC) | Meaning (EN) | Difficulty | A good answer should |
|---|---|---|---|---|---|
| S33 `en-reddit-s005` | en | compare v3 and v4 of the struct ifc, what got added/deleted/moved? need it for the coord meeting in an hour | Compare two IFC revisions | hard, file | Diff by GlobalId: added, removed, changed placement/properties; summarize. |
| S34 `ru-renga-nanocad-s006` | ru | сравни две выгрузки, вчерашнюю и сегодняшнюю, что добавили что удалили что поменяли | Compare two IFC exports, show added, deleted and changed elements | hard, file | Match elements by GlobalId, report added/removed, and changed properties or geometry placement; note if GUIDs are unstable. |
| S35 `es-latam-s009` | es | compara el ifc de hoy con el de la semana pasada, qué elementos nuevos, borrados y movidos | Compare two model versions by GlobalId | hard, file | Match by GlobalId, list added/deleted/changed geometry or property elements, summarize per discipline. |
| S36 `fr-francophone-s005` | fr | compare l'indice B et l'indice C de la maquette, je veux les éléments ajoutés/supprimés/modifiés avant la synthèse | Compare two IFC versions and list added, deleted, modified elements | hard, file | Diff by GlobalId; report added/removed/changed elements with property deltas, grouped by discipline. |
| S37 `nl-dutch-s010` | nl | wat is er veranderd tussen v3 en v4 van het constructie ifc? nieuwe, verwijderde en gewijzigde elementen op GUID | Compare IFC v3 and v4 | medium, file | Diff by GlobalId, report added/removed/changed. |
| S38 `ja-japan-s006` | ja | 先週のIFCと今日のIFC比べて、追加・削除・変更された部材をGlobalIdベースで出して。変更は属性か形状かも | Diff last week's IFC and today's: added, removed, changed elements | hard, file | Match by GlobalId, report added/removed, compare attributes/properties and placement/geometry hash for modified. |
| S39 `en-uk-anz-india-s006` | en | compare P02 and P03 ifc - what walls got added, deleted or changed. by GlobalId | Compare two issued versions | hard, file | Load both models, diff IfcWall by GlobalId, list added/removed/modified (property or geometry-level where possible). |
| S40 `de-dach-s008` | de | vergleich mal Stand 12 und Stand 14 vom Rohbau-IFC. was ist neu, was weg, was verschoben? GUIDs ändern sich bei uns teilweise | Compare two IFC exports and say what changed, GUIDs may have changed. | hard, file | Diff by GUID, fall back to geometry/name matching, report added/removed/moved. |

### 6. Light fixes, conversions, heavy files, how-to

Some prompts change the file; a good answer saves a NEW file and says what it touched.

| # / id | Lang | Prompt (SYNTHETIC) | Meaning (EN) | Difficulty | A good answer should |
|---|---|---|---|---|---|
| S41 `ru-dwg-revit-s004` | ru | все проксей с именем 'Колонна_*' переведи в IfcColumn, остальное не трогай | Reassign proxies for generic-model columns to IfcColumn | medium, file | Select proxies by name pattern, change class to IfcColumn preserving properties and relationships, save a new file, report count. |
| S42 `de-dach-s012` | de | die Stützen sind alle als Proxy drin, kannst du die zu IfcColumn machen? Name fängt mit ST_ an | Reclassify proxies that are really columns. | medium, file | Find proxies with matching name, change class to IfcColumn, preserve psets, report changes. |
| S43 `en-blogs-linkedin-s012` | en | need this as ifc2x3 for the contractors site app, whats going to break | Downgrade to 2x3 | hard, file | Explain conversion, warn about loss (alignment, classes, properties), run if supported and report differences. |
| S44 `ru-tim-expertiza-s014` | ru | ифс на 1.5 гига, вьюер у экспертизы виснет, чем можно облегчить не потеряв свойства | The IFC is huge and the expertise viewer chokes | medium, file | Suggest reducing size: remove unused types/2D, split by discipline/zone, reduce geometry detail, keep property sets; inspect file for heaviest entities. |
| S45 `en-navis-acc-s006` | en | ifc upload failed in acc docs, no error just 'failed to process'. file is 900mb. whats wrong w it? | Why did my IFC upload fail in ACC | hard, no file | Inspect file validity, schema header, size, units; suggest splitting or reducing and checking supported IFC versions. |
| S46 `ru-err-s005` | ru | ревит валится при экспорте в ифс, 'неустранимая ошибка'. глянь в модели что может ломать - помещения без границ, битые стены? | Find what may cause unrecoverable export error | hard, file | Check rooms not enclosed/redundant, areas, elements with null geometry; suggest filtering by view and bisecting categories. |
| S47 `ru-autodesk-telegram-s015` | ru | для экспертизы какой ифс выгружать, 2х3 или 4, и какой вид, CV2 или RV? | Which IFC version and view for expertise | medium, no file | Explain that it depends on customer requirements (SP 333 allows 2x3 and higher; Moscow AGR uses IFC4 with IDS), describe CV2.0 vs RV and advise to check the customer's IDS/requirements. |
| S48 `en-model-checking-s005` | en | clash ducts vs structural beams, 10mm tolerance, group by level. dont give me 300 lines for one duct run | Hard clashes between ducts and beams | hard, file | Run clash between duct segments/fittings and beams with tolerance, group by storey and system. |

## How to role-play this persona in tests

**Voice.** Short, lower-case, often no greeting, 1 to 3 lines, sometimes a deadline in the same sentence ("for the coord meeting in an hour", "завтра сдача в АГР", "handover is friday"). Slang for tools and standards (ифс, навис, бцф, proxy, pset). Non-native English is normal: missing articles, "doesnt", "pls", "b4". Russian requests are imperative and informal: "глянь", "скинь", "выдай списком". Chinese and Japanese ones are terse and noun-heavy ("柱子的名称是不是按我们的命名规则"). German adds a polite "bitte" or "mal": "prüf mal ...".

**Typical context.** A file received from another discipline ("this ifc", "the arch model"), exported from Revit (most often), Archicad, Tekla or Renga. IFC version often unspecified (in the base: IFC4 415, IFC2x3 199, unknown 149 for this persona). A viewer is already in the picture (Navisworks, Solibri, BIMcollab, ACC). Rarely any file name or element ID.

**Knowledge level.** Practical, tool-level, not schema-level. Knows what a proxy and a pset are, knows Revit's export dialog; does not know the IFC schema, does not know what `IfcMapConversion` or `IfcRelVoidsElement` are unless the test wants to see if the assistant explains them. Treats "IFC" as a thing that sometimes loses data.

**Typical follow-ups** (use these as the second turn):
- "ok and which floor are they on?" / "list with GUIDs so I can find them in Revit"
- "give that as an excel" / "as BCF" / "csv with ; separator"
- "only structure" / "hard clashes only" / "ignore touching"
- "dont change the file, just tell me" or the opposite: "fix it and save as new ifc"
- "is that the exporter or my settings?" (the assistant should say what it can and cannot know)
- "the checker says X, you say Y, who is right?" (a good assistant explains the difference in rules rather than picking a side)

**Traps worth including.** Missing units or feet vs millimetres ([en-gh-ifcopenshell-r008](https://github.com/IfcOpenShell/IfcOpenShell/issues/7178)); IFC2x3 vs IFC4 property placement; type-level vs instance-level properties; a "duplicate" that is just a repeated type; asking for a diff when GlobalIds changed; an IDS that passes "formally" but is wrong in content; a request that implies modifying the model when the user only wanted a report.

**How to judge the answer.**
1. Numbers are given with how they were counted (which classes, which storeys) and a way to find the elements (GlobalId, name, floor).
2. Nothing is invented: property sets named exist in the file or the standard; "unknown" is stated when the data is missing (compare the design rule "model proposes, code executes" in [bim-ifc-mcp](https://github.com/zeussilver/bim-ifc-mcp)).
3. The answer separates *what is in the file* from *what the authoring tool did* (it cannot see Revit settings from an IFC).
4. Edits go to a new file and are listed; the original is untouched.
5. For clashes: tolerance, grouping and output format (BCF) honored; no wall of 300 lines for one duct run.
6. It does not promise that an authority or checker will accept the model.

**Related personas.** [BIM manager](bim_manager.md) (owns the standard the coordinator enforces), [Architect](architect.md) (receives the coordinator's issues), [Reviewer / authority](reviewer_authority.md) (the downstream checker), [Owner / client](owner_client.md) (the one who pays for the checks). Also see the MCP server catalog in [04_open_source](../../04_open_source/mcp_servers_and_ai_tools.md).
