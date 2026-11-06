# Intent taxonomy: what users want from an IFC / Revit assistant

**Compiled: 2026-11-06.** Built from 3,592 research records in `research_raw/` (2,304 real posts and README/issue texts, 1,288 synthetic prompts), of which **1,051 are `model_task` prompts** (synthetic requests that assume an IFC model or Revit project is already loaded). Read with the companion file [what_ifc_mcp_servers_do.md](what_ifc_mcp_servers_do.md), which defines the capability codes **K1-K15** and the weakness codes **L1-L25** used below.

How to use this file when you generate a test request:

1. Pick an intent (code A1...G3) and a sub-intent.
2. Check the "Needs" line: does the server under test have those capabilities ([capability matrix](what_ifc_mcp_servers_do.md#31-capability-matrix-by-server-group))? If not, the request becomes a refusal test, which is also valuable.
3. Pick a persona, tone and language (section 2), copy the *voice* of the example prompts, not their content.
4. Use the "Failure modes" line as the grading checklist.

> Plain-words reminder for non-BIM readers: an **IFC** file is an open, text-based database of a building (walls, doors, rooms, pipes and their data). **Revit** is a popular design program that holds the same information in its own project file. An **MCP server** gives a chat AI a menu of tools to read or change such a file or project ([explained here](what_ifc_mcp_servers_do.md#1-mcp-in-plain-words)). Terms such as GlobalId, Pset, IfcSpace, proxy, IDS, BCF are in the [abbreviations](../08_glossary/abbreviations.md) and [multilingual glossary](../08_glossary/glossary_multilingual.md).

## Labels used in example tables

| Label | Meaning |
|---|---|
| **S** | Synthetic prompt from the corpus (a research-agent draft inspired by real posts). Never a real quote. Id is the record id in `research_raw/`. |
| **R** | Real record (forum thread, GitHub issue, blog, README). The text shown is the corpus *paraphrase* in the asker's language, not a copy of the post; the link is the source. Most real records are problems or how-to questions *to humans*, so they show what people need, not how they would phrase it to an assistant. |
| **D** | Draft written by the compiler of this file to fill a gap (no corpus prompt exists). Modeled on S examples; use it as a style sample only. |

---

## 1. The taxonomy at a glance

22 intents in 7 families. Shares come from keyword triage of the corpus by the compiler (method and caveats in 1.2). Two measurements are given because they answer different questions:

- **model_task share**: of the 1,051 synthetic file-task prompts, how many ask for this. This is the best proxy for "what would people type to an assistant that can see their file". It is synthetic, so it reflects what the research agents judged plausible.
- **all-records share**: of all 3,592 records, using the record's own `intent` field refined by keywords. Real posts dominate here and are mostly "why is my export broken / how do I do X", so family G is large.

### 1.1 Overview table

| Code | Intent | One-line meaning | model_task n (%) | all records n (%) | Typical difficulty (agent labels) | Main capabilities (K) |
|---|---|---|---|---|---|---|
| **A** | **Understand the model** | read-only look-ups | 289 (27.5%) | 333 (9.3%) | | |
| A1 | model_overview | "What is in this file?" | 9 (0.9%) | 10 (0.3%) | easy | K1 K2 K3 |
| A2 | inventory_count | "How many / list all X" | 83 (7.9%) | 86 (2.4%) | mostly medium | K2 |
| A3 | spatial_navigation | storeys, rooms, containment, hierarchy | 16 (1.5%) | 20 (0.6%) | easy-medium | K4 K2 |
| A4 | property_lookup | read properties, materials, classification values | 106 (10.1%) | 117 (3.3%) | medium | K3 K2 |
| A5 | coordinates_units | georeference, origin, units, "model is far away" | 75 (7.1%) | 100 (2.8%) | medium-hard | K6 K3 |
| **B** | **Get numbers and deliverables** | | 140 (13.3%) | 191 (5.3%) | | |
| B1 | quantity_takeoff | areas, volumes, lengths, counts for cost or schedules | 121 (11.5%) | 162 (4.5%) | medium | K5 K2 |
| B2 | data_report_export | a table/CSV/Excel of model data | 19 (1.8%) | 29 (0.8%) | medium | K2 K3 K5 K10 |
| **C** | **Check quality and compliance** | | 314 (29.9%) | 487 (13.6%) | | |
| C1 | completeness_check | "which elements lack X" | 156 (14.8%) | 174 (4.8%) | medium (many hard) | K2 K3 |
| C2 | rule_validation | IDS, schema, MVD, EIR/BEP requirements | 58 (5.5%) | 108 (3.0%) | medium-hard | K7 K3 |
| C3 | mapping_geometry_audit | proxies, wrong classes, duplicates, broken geometry, encoding | 76 (7.2%) | 87 (2.4%) | medium | K2 K3 K4 (K15) |
| C4 | regulation_check | building code, permit, national submission rules | 24 (2.3%) | 118 (3.3%) | hard | K3 K5 K7 |
| **D** | **Compare and coordinate** | | 106 (10.1%) | 153 (4.3%) | | |
| D1 | version_diff | what changed between two files/versions | 72 (6.9%) | 94 (2.6%) | **hard** | K13 |
| D2 | clash_coordination | overlaps between disciplines, BCF issues, missing openings | 34 (3.2%) | 59 (1.6%) | **hard** | K12 K10 K14 |
| **E** | **Change the model** | | 110 (10.5%) | 203 (5.7%) | | |
| E1 | edit_data | change class, properties, names, storey assignment | 87 (8.3%) | 122 (3.4%) | medium-hard | K8 K0 |
| E2 | create_elements | draw walls, add storeys, build a small model | 12 (1.1%) | 19 (0.5%) | medium-hard | K9 K0 |
| E3 | batch_automation | rename 40 views, make sheets, clean up, run over many files | 11 (1.0%) | 62 (1.7%) | medium-hard | K8 K2 K15 |
| **F** | **Move, show, slim down** | | 58 (5.5%) | 244 (6.8%) | | |
| F1 | convert_exchange | IFC to GLB/DWG/IFC2x3/CityGML, or Revit to IFC | 35 (3.3%) | 154 (4.3%) | medium-hard | K11 K10 |
| F2 | visualize_view | screenshot, highlight, isolate, camera | 2 (0.2%) | 3 (0.1%) | medium | K14 |
| F3 | optimize_performance | "file too big / slow, what is heavy" | 21 (2.0%) | 87 (2.4%) | medium-hard | K2 K3 (K15) |
| **G** | **Ask about process, problem, assistant** | | 34 (3.2%) | 1,981 (55.2%) | | |
| G1 | explain_howto | concepts, "how do I do X in my software" | 0 | 544 (15.1%) | easy | none (knowledge) |
| G2 | troubleshoot_diagnose | "something went wrong after export/import, find out why" | 34 (3.2%) | 1,110 (30.9%) | medium-hard | K2 K3 K4 K6 K7 |
| G3 | tool_meta | "what can you do / connect / which tool" | 0 | 327 (9.1%) | easy | server self-description |

Family totals (model_task / all records): A 27.5% / 9.3%, B 13.3% / 5.3%, C 29.9% / 13.6%, D 10.1% / 4.3%, E 10.5% / 5.7%, F 5.5% / 6.8%, G 3.2% / 55.2%.

Reading the numbers:

- **Read-and-check dominates file tasks.** A + B + C = 70.7% of model_task prompts; the single biggest intent is C1 "which elements are missing X" (14.8%), followed by B1 takeoffs (11.5%) and A4 property look-ups (10.1%).
- **Real people mostly ask "why / how" (G, 55%), not "do this for me".** The bridge between the two is G2: many synthetic prompts rephrase a forum complaint into an assistant request ("half the elements are gone after export, find out what dropped"; see G2 examples).
- **Thin spots in the corpus:** F2 (0.2%), E2 (1.1%), E3 (1.0%), A1 (0.9%) are almost absent from `model_task` because they were mined from forums, whereas real MCP issues are full of exactly these: creating walls, bulk view/sheet work, screenshots, "what can you do" ([ai-mcp-usage](../research_raw/wave1/ai/ai-mcp-usage.md), [ai-revit-tasks](../research_raw/wave1/ai/ai-revit-tasks.md)). Weight them up when generating tests (section 4).
- **A5 is bigger than the companion file's quick count** (5.6% there, 7.1% here) because this file also counts mixed prompts such as "check georef and empty fields". Treat 6-7% as the real range.

### 1.2 Method and caveats

- The 22 intents are a tester's taxonomy; the corpus only has the coarser `intent` vocabulary (query_model_data, validate_check, ...), see [SPEC.md](../_meta/SPEC.md). The compiler mapped each record to one **primary** intent: first from the record's own `intent` field (for example `compare_versions` becomes D1, `convert_format` F1, `troubleshoot_*` G2, `find_tool`/`request_feature` G3), then split the two big buckets `query_model_data` and `validate_check` with multilingual keyword rules (coordinates, quantities, storeys, IDS/schema, proxies/geometry, regulations, deliverable format).
- About 8 random prompts per intent were read by eye to check the rules. The boundaries C1/C3, A2/A4 and B1/B2 are fuzzy; assume **plus or minus 3 percentage points** per intent. Compound prompts count once, under the main verb.
- `needs_file` is true for 1,050 of the 1,051 model_task prompts. 49% of them literally write "IFC" (or an Ifc class) in the prompt text; the expected-behaviour text mentions IFC in 76%. About 9% name Revit.
- Difficulty labels (easy 158, medium 557, hard 336) were assigned by the research agents, not measured.
- Tone: neutral 62%, urgent 13%, frustrated 9%, confused 7%, polite 3%, curious 3%, skeptical 2.5% (model_task).
- Because model_task prompts are synthetic, "share" says what is plausible, not what was measured in real MCP sessions. No log of real assistant conversations was available.

---

## 2. Cross-cutting dimensions (not intents, but they change how a request sounds)

Every intent can be combined with these. Generating variety along them is more useful than adding more intents.

| Dimension | Values seen in the data | What to vary |
|---|---|---|
| **Scope** | whole model; one discipline (arch/struct/MEP); one storey; one class; one element | "in the whole model" vs "on Level 2" vs "this wall" |
| **Output form** | answer in chat; list with GlobalId; grouped by storey (about 18% of prompts group by storey/level); table for Excel/CSV (5%); BCF issues (1.6%); a new IFC file (4% say "save as new file/copy") | Ask for a different form of the same question |
| **Strictness** | "don't guess if the data is missing", "if there is no Qto say so" (explicit in only ~0.2% of prompts but implied by the whole `expected_behavior` set), "don't delete yet", "propose, then apply" | Add one honesty or safety clause |
| **Language** | model_task: en 519, ru 121, zh 105, es 56, de 47, ja 42, it 38, fr 35, ko 27, pt+pt-BR 33, no 14, nl 12 | Same intent in 3 languages; tool and class names stay English (`IfcBuildingElementProxy`, `GlobalId`) |
| **Persona** | bim_coordinator 35%, bim_manager 12%, architect 10%, developer 8%, structural 6%, estimator 6%, MEP 5%, reviewer 4%, FM 4%, civil/infra 4%, contractor 2%, owner 2%, student 2% | Persona decides vocabulary: estimators say "ВОР/metrados/quantitativo", reviewers say "экспертиза/alvará/報建" |
| **Tone** | neutral, urgent ("завтра сдача", "submit tomorrow"), frustrated, confused (beginners), skeptical ("I don't trust the slab areas") | Urgent and skeptical prompts test whether the assistant stays careful under pressure |
| **Context given** | usually only the consuming tool ("Solibri", "Navis", "Revit 2025") or the source tool ("from Allplan", "Tekla IFC"); rarely IFC version or file size | Leave out what a real user leaves out |
| **Compound requests** | check + list ("which doors lack FireRating, csv with GUID and storey"); find + fix (count proxies, then reclassify); compare + report | 1 in 4 test prompts should contain two intents |

Frequent real-world "anchor topics" inside prompts (so you can reuse them): IfcBuildingElementProxy ("proxies") appears in 8% of model_task prompts; GlobalId in 6%; storeys/levels in 18%; Revit-to-IFC export problems are the background of a large share of C and G prompts (see [Revit export and class mapping questions](../05_real_world_questions/by_topic/revit_export_and_class_mapping.md)).

---

## 3. The intents in detail

Notation: "Needs" lists capability codes from [what_ifc_mcp_servers_do.md section 3](what_ifc_mcp_servers_do.md#3-capabilities-the-15-building-blocks); "Failure modes" lists weaknesses L1-L25 from [section 6](what_ifc_mcp_servers_do.md#6-limitations-to-probe-the-checklist) plus intent-specific traps.

### Family A. Understand the model (read-only)

#### A1 model_overview: "What is in this file?"

**Definition.** The user has an IFC or Revit project they did not make (or just opened) and wants a plain summary: schema version, who exported it, which disciplines, how many elements by class, which storeys.
**Share.** 9 prompts (0.9%) in model_task; almost all from beginners and handover situations. Under-represented in the corpus compared with real MCP READMEs, whose first example is nearly always "summarize this model".
**Sub-intents.** (a) first look by a beginner; (b) technical header: schema, view definition (MVD), exporter; (c) class inventory for a specific source tool (Civil 3D, Tekla); (d) handover summary for a client; (e) "does it contain X at all" (alignment, terrain).

| Id | Lang | Lbl | Request | Gloss / why it is a good test |
|---|---|---|---|---|
| p-student-s001 | en | S | `i just opened my first ifc for uni, what even is in it? can you give me a simple overview, like how many walls doors etc and the storeys` | Beginner: expects plain language, not raw JSON |
| en-beginner-qa-s001 | en | S | `just got this ifc from my architect. what is even in it? like how many floors and what kind of stuff` | Confused tone, no vocabulary |
| en-vm-s001 | en | S | `what schema is this file, 2x3 or 4? and does the header say CV2.0 / RV / DTV` | Header reading; MVD codes |
| ja-vm-s012 | ja | S | `このIFCのFILE_SCHEMAとエクスポートしたRevitのバージョン教えて` | Which schema and which Revit version exported it |
| es-latam-s017 | es | S | `resumen rápido de qué trae este ifc: disciplinas, versión, cantidad de elementos por clase` | Quick summary: disciplines, version, counts per class |
| it-italy-s013 | it | S | `riassumimi il modello: discipline, n. elementi per classe, livelli, per il verbale di consegna` | Handover minutes; summary has an audience |
| en-roundtrip-s017 | en | S | `civil 3d export - what ifc classes are in here? terrain, alignment, pipes? will revit even see them` | Source-tool specific; includes a prediction about another tool |
| en-graphisoft-s001 | en | S | `check which translator this ifc was exported with and whether my custom properties came through` | Exporter identity plus property survival |
| (no ru in corpus) | ru | D | `что вообще в этом файле? сколько этажей, стен, дверей, и чем его выгружали` | Russian gap filler, same shape as the English ones |

**Needs.** K1, K2, K3 (header/metadata), K4 for storeys. **Difficulty.** Easy. **Failure modes.** Invented numbers when only part of the file was read (L10); wrong schema claim (L11); dumping a 5,000-line class list instead of a summary (L24); unit blindness (L12).

#### A2 inventory_count: "How many / list all X"

**Definition.** Counting or listing elements by class, type, system or storey, with no judgement about correctness.
**Share.** 83 (7.9%). Top personas: bim_coordinator (40 of 83), MEP engineer, architect. Languages: en 47, ru 18, zh 11.
**Sub-intents.** (a) counts by IFC class ("how many windows, doors, ramps"); (b) proxy census: how many `IfcBuildingElementProxy` and from which Revit categories they came (the single most repeated prompt in the corpus, in 10 languages); (c) per-system lists for MEP (pipes with system and diameter); (d) per-storey inventories; (e) specific object families (mullions vs panels, alignments, assemblies).

| Id | Lang | Lbl | Request | Gloss / why it is a good test |
|---|---|---|---|---|
| ru-proxy-s001 | ru | S | `глянь сколько в модели проксей и из каких категорий ревита они пришли, надо понять что перемапить` | "Proxy" census; slang "проксей"; goal is remapping |
| ru-autodesk-telegram-s007 | ru | S | `выведи этажи с отметками и сколько элементов на каждом, лишние уровни тоже покажи` | Storeys with elevation and counts; "show extra levels too" |
| en-aimcp-s006 | en | S | `list all pipes in the model with system type and diameter` | Typical MEP list; also the shape of a real failing call (R below) |
| en-geom-s002 | en | S | `how many IfcMember mullions vs IfcPlate panels per curtain wall? i think mullions got dropped on export` | Suspicion built in; per-parent count |
| zh-csdn-dev-s005 | zh | S | `统计一下proxy有多少个，按Revit类别分组，看是不是导出映射没配好` | Count proxies by Revit category; check export mapping |
| es-spain-s001 | es | S | `cuantos IfcBuildingElementProxy hay en el ifc y de que categorias de revit vienen?` | Same census, Spanish |
| ja-japan-s001 | ja | S | `このIFC、IfcBuildingElementProxyが何個あるか数えて、元のRevitカテゴリ別に集計して。マッピング直す対象知りたい` | Count proxies per original category; wants mapping targets |
| no-norway-s007 | no | S | `list opp alle ventilasjonssystemer og antall kanaler i hvert system` | Ventilation systems and duct counts |
| en-aimcp-r028 | en | R | README example: `How many fire doors are on Level 2?` | [Daviidro/ifcopenshell-mcp](https://github.com/Daviidro/ifcopenshell-mcp): a count that needs property + storey |
| en-aimcp-r020 | en | R | user typed `list all pipes in the revit model`; server answered "Method not found" | [revit-mcp issue 28](https://github.com/mcp-servers-for-revit/revit-mcp/issues/28): connection/method failure, not a data answer |

**Needs.** K2 (class filter and grouping); K3 for "from which Revit category"; K4 for per-storey. **Difficulty.** Medium (59 of 83). **Failure modes.** Counting types instead of occurrences or vice versa; subclass handling (`IfcWall` vs `IfcWallStandardCase`); counting Revit "category" vs IFC class (L8, L9); no total; swallowing connection errors (L1, L2); silently truncating a long list.

#### A3 spatial_navigation: storeys, rooms, containment

**Definition.** Questions about the building's structure: which storey an element belongs to, what is in a room, hierarchy site > building > storey > space, openings in a wall, elements not attached to any storey.
**Share.** 16 (1.5%) strictly, but spatial grouping ("by storey") appears in 18% of all prompts as an output requirement.
**Sub-intents.** (a) list storeys with elevations; (b) element-to-storey mapping; (c) **orphans**: elements not under any `IfcBuildingStorey`; (d) space boundaries and zones; (e) host/opening relations.

| Id | Lang | Lbl | Request | Gloss / why it is a good test |
|---|---|---|---|---|
| en-reddit-s012 | en | S | `some stuff isnt under any level in the ifc tree, find elements w/o IfcBuildingStorey` | Orphan search |
| en-stackoverflow-s008 | en | S | `which storey is each column on? some come back None` | Missing relation; the user already saw `None` |
| p-student-s009 | ru | S | `покажи мне этажи в ифс и сколько элементов на каждом, для курсовой надо` | Student; storeys plus counts |
| es-coord-s009 | es | S | `dime qué elementos del IFC no están asignados a ningún nivel o planta, necesito corregirlos antes de la coordinación` | Orphans before coordination |
| zh-aimcp-s007 | zh | S | `这个ifc里每层有多少面墙？按楼层列一下，顺便看有没有没挂到楼层的` | Walls per floor plus orphans |
| en-spaces-s003 | en | S | `do we have IfcRelSpaceBoundary2ndLevel in this file? how many per space, any space with zero` | Advanced: boundary level |
| en-gh-xbim-others-s001 | en | S | `list the storeys in this ifc4x3 (from revit 2025) with elevation, some are partial floors i think` | IFC4x3 plus partial floors |
| en-bsforum-r018 | en | R | find the storey for a room number when only a text editor is available | [buildingSMART forum 5187](https://forums.buildingsmart.org/t/5187) |
| en-gh-thatopen-r036 | en | R | `IfcSpace` inside storeys not classified to a storey in the viewer | [That Open issue 414](https://github.com/ThatOpen/engine_components/issues/414) |
| zh-csdn-dev-r012 | zh | R | 从 IfcProject 递归，`IsDecomposedBy` 走聚合，`ContainsElements` 拿楼层里的墙门窗 | [cnblogs tutorial](https://www.cnblogs.com/SavionZhang/p/10983394.html): the structure a tool must walk |

**Needs.** K4, K2. **Difficulty.** Easy-medium. **Failure modes.** Confusing "contained in storey" with "aggregated by"; counting elements twice (once per relation); storeys named inconsistently (RDC, R+1, Level 02) mistaken for duplicates; double storeys from export (see G2 `no-norway-s004`).

#### A4 property_lookup: read properties, materials, classification

**Definition.** Read specific data from elements: a property in a Pset, a quantity, material layers, classification code, Name/Description/Tag fields, with or without filters.
**Share.** 106 (10.1%), the third-largest intent. Languages are the most varied of any intent (en 50, ja 10, zh 10, fr 7, ...).
**Sub-intents.** (a) attribute dump (Name, Reference, Description) to see how an exporter mapped fields; (b) one property across a class (FireRating on doors); (c) material layers and thicknesses; (d) classification code location (Pset vs `IfcClassificationReference`); (e) fill-rate statistics ("fill % per property"); (f) type-level vs instance-level values.

| Id | Lang | Lbl | Request | Gloss / why it is a good test |
|---|---|---|---|---|
| ru-autodesk-telegram-s010 | ru | S | `какие параметры ревита вообще дошли до ифс, покажи психеты у одной стены и скажи чего нет` | Which Revit parameters arrived; "психеты" slang for Psets |
| en-bsforum-s008 | en | S | `dump Name, Reference, Description for all walls, i think our export mixes them up` | Exporter field mix-up |
| en-psets-s008 | en | S | `where is the NL-SfB / Uniclass code stored, in a pset or IfcClassificationReference? how many elements have none` | Where plus how many |
| en-osarch-s016 | en | S | `what material layers does the exterior wall type have? thickness of each` | Type-level layers |
| en-blogs-linkedin-s010 | en | S | `which columns have no IsExternal in Pset_ColumnCommon` | Targeted absence (overlaps C1) |
| de-eng-s013 | de | S | `gib mir alle Rohre mit Nennweite und Material, TGA Modell` | Pipes with nominal diameter and material |
| p-student-s015 | de | S | `zeig mir bei allen Türen Name, Reference und ObjectType, welches ist jetzt der Instanzname? Allplan Export` | Student confusion over three name fields |
| en-eng-s003 | en | S | `pipes show material = system name (HOT WATER) not copper. can you list pipes and what material they actually have` | Real vs system material |
| ja-japan-s007 | ja | S | `設備IFCの空調ダクトをシステム名別・階別に本数と合計長さでまとめて` | Ducts by system and floor with total length (A4+B1) |
| en-cesium-r031 | en | R | cannot retrieve IFC properties; property keys combine pset and property | [Cesium forum](https://community.cesium.com/t/cant-retrieve-ifc-properties-and-attributes/40009): naming scheme confusion |
| en-gh-xbim-others-r011 | en | R | retrieve materials and colours via `HasAssociations` | [XbimEssentials issue 642](https://github.com/xBimTeam/XbimEssentials/issues/642) |

**Needs.** K3, K2. **Difficulty.** Medium (59), easy (29), hard (18). **Failure modes.** Reading type properties only (or instance only) (L14); Revit shared parameter vs IFC property name differences; value units (L12); listing property names that do not exist; encoding of non-ASCII names (L15); returning a property from a different Pset with the same name.

#### A5 coordinates_units: georeference, origin, units

**Definition.** Where the model sits in the world and what its units are: `IfcMapConversion`, coordinate reference system (CRS/EPSG), `IfcSite` lat/long, project base point vs survey point, true north, length unit, "my model is kilometres away".
**Share.** 75 (7.1%), the highest share of **urgent** tone of any intent (17 of 75). Personas: bim_coordinator (44), civil/infra (10). Languages: en 43, ru 12, zh 9, plus de, it, es, nl, no, ko, ja, fr.
**Sub-intents.** (a) "why is it far from the origin / mis-aligned with the other model"; (b) read the CRS and rotation; (c) are three discipline models in the same CRS; (d) units (mm vs m vs feet; "1000x too big"); (e) national submission check (China's SZ-IFC base-point rule, Singapore SVY21, Japan plane coordinates); (f) **double shift**: coordinates already projected AND a MapConversion on top.

| Id | Lang | Lbl | Request | Gloss / why it is a good test |
|---|---|---|---|---|
| ru-renga-nanocad-s008 | ru | S | `модель улетает далеко от начала координат, глянь в чем дело, привязка вообще есть?` | "Flies away from origin"; georef existence |
| en-navis-acc-s008 | en | S | `navis shows my ifc 1000x too big. what units is it in` | Unit-assignment lookup |
| mul-coord-s002 | en | S | `my model lands 5km off in civil3d, check if coords are already projected AND theres a mapconversion on top` | Double-shift trap |
| en-us-canada-infra-s004 | en | S | `this ifc lands miles away from the civil model. whats the IfcMapConversion / site lat-long and units? feet or meters? state plane?` | Feet, state plane |
| mul-coord-s013 | de | S | `pruef mal ob die drei IFCs dasselbe Koordinatensystem haben (ETRS89/UTM32), Rechtswert Hochwert Rotation` | Three files, same CRS? (multi-file) |
| es-latam-s007 | es | S | `el ifc de topografía viene en metros o milímetros? y tiene georreferencia? coordenadas muy lejos del origen?` | Units + georef + distance |
| fr-francophone-s010 | fr | S | `mon IFC est décalé de plusieurs km dans le viewer, regarde le géoréférencement RGF93 / Lambert 93 de la maquette` | French national CRS |
| it-italy-s008 | it | S | `in che unita e il file? mm o metri? cosa dice IfcUnitAssignment` | Units only |
| zh-lightweight-review-s001 | zh | S | `这个ifc报建自检能过吗？先看下项目基点坐标是不是2000的，还有哪些构件属性是空的` | Shenzhen submission self-check; base point and empty fields |
| ja-gis-s016 | ja | S | `このIFC、平面直角座標系の設定入ってる？なければ座標系と原点のずれ確認して` | Japanese plane rectangular coordinates present? |
| zh-revit-export-r015 | zh | R | 深圳SZ-IFC审查项目基点坐标、高差、正北为空，导出丢字段 | [Zhihu article](https://zhuanlan.zhihu.com/p/673078056): the real rule behind the prompt above |
| en-bsforum-r040 | en | R | IFC4X3 with `IfcMapConversion` all zero or NIL and missing axis: valid? | [buildingSMART forum 6331](https://forums.buildingsmart.org/t/6331) |
| en-osarch-r039 | en | R | `IfcClash` reports clash locations in mm although the project uses feet | [IfcOpenShell issue 7178](https://github.com/IfcOpenShell/IfcOpenShell/issues/7178) |

**Needs.** K6, K3; K1 to compare several files. Few servers expose georeferencing at all (see matrix). **Difficulty.** Medium-hard (hard 30 of 75, the highest hard share among A intents). **Failure modes.** Answering from an assumption about units (L12); saying "georeferenced" when only an `IfcSite` lat/long exists; reporting offsets in the wrong unit; not distinguishing project origin from the site; claiming CRS correctness for a national system the tool does not know; fabricating EPSG codes.

### Family B. Get numbers and deliverables

#### B1 quantity_takeoff: areas, volumes, lengths for cost and schedules

**Definition.** Sums and counts for estimating or reporting: wall area per storey, concrete volume per element type, room areas, door/window schedules, rebar weight, duct length per system. Often with a hidden question "which quantity source do you trust?".
**Share.** 121 (11.5%), the second-largest intent. Persona: estimator_qs (48 of 121), then facility managers and architects. Seventeen urgent prompts ("budget tomorrow", "bid").
**Sub-intents.** (a) net vs gross areas and whether openings are subtracted; (b) `Qto_*BaseQuantities` vs geometry-computed values and reconciliation; (c) totals by storey/type/system; (d) room/space area lists (экспликация, FM space lists); (e) BoQ-style schedule per trade; (f) infrastructure (rail alignment length in km, rebar per pier).

| Id | Lang | Lbl | Request | Gloss / why it is a good test |
|---|---|---|---|---|
| ru-spaces-s011 | ru | S | `посчитай суммарную площадь помещений по этажам, нужна таблица для экспликации` | Sum of room areas per floor for the explication table |
| ru-autodesk-telegram-s003 | ru | S | `сумма площадей по IfcSpace не бьётся с ТЭП, покажи по каждой зоне RUS_Area и реальную площадь по геометрии, где разница больше 0.5 м2` | Attribute vs geometry reconciliation, threshold 0.5 m2 |
| en-struct-s003 | en | S | `total rebar weight per column, from the IfcReinforcingBar geometry or Qto if there is one. kg` | Source fallback stated by the user |
| en-data-s004 | en | S | `slab volumes in my cost sheet are 8% off the model. which slabs have no Qto or odd units?` | Skeptical estimator; diagnose a mismatch |
| zh-csdn-dev-s007 | zh | S | `各楼层楼板和墙的体积汇总一下，用Qto里的NetVolume，没有的话用几何算，两个对一下` | Use Qto NetVolume, otherwise geometry, cross-check |
| de-s008 | de | S | `Mengen fuer die Ausschreibung ziehen: Mauerwerk Wandflaechen netto ohne Oeffnungen, nach Geschoss. Passt das mit Qto?` | Tender quantities: net without openings; does Qto agree |
| es-latam-s003 | es | S | `necesito los metrados de muros, losas y columnas por nivel, m2 y m3, para el presupuesto de mañana` | Urgent budget |
| ja-s013 | ja | S | `階ごとのコンクリート数量と型枠面積を拾いたいです。梁と柱と壁で分けて出せますか` | Concrete and formwork area per floor, split by element class |
| ko-korea-s006 | ko | S | `층별 콘크리트 물량 m3로 정리해줘 슬래브 벽 기둥 따로` | Concrete by floor, slab/wall/column separate |
| pt-qto-s014 | pt | S | `preciso do quantitativo das portas e janelas por tipo e pavimento, com largura e altura` | Door/window schedule by type and floor |
| fr-qto-s016 | fr | S | `j'ai besoin d'un métré par lot : maçonnerie en m3, cloisons en m2, menuiseries en nombre` | Takeoff per trade package |
| en-gh-ifcos-r002 | en | R | `GrossSideArea == NetSideArea` in Bonsai quantity takeoff of Revit walls; Solibri differs | [IfcOpenShell issue 9235](https://github.com/IfcOpenShell/IfcOpenShell/issues/9235): a real quantity-trust bug |
| es-aimcp-r032 | es | R | README: `Ejecuta la corrida 5 HVAC sobre mi selección actual en modo detalle.` | [RevitMCPBOQ](https://github.com/JefaturaBIM94/RevitMCPBOQ): takeoff on the current Revit selection |

**Needs.** K5, K2, K3; K4 for per-storey. **Difficulty.** Medium (77), easy (27), hard (17). **Failure modes.** L13 (which quantity source, openings subtracted or not); summing mixed units; double counting aggregated parts and their children; missing Qto treated as zero; type-based quantities multiplied wrongly; rounding to a "nice" number; no per-storey breakdown when asked; the total does not equal the sum of the rows.

#### B2 data_report_export: a table, CSV or Excel of model data

**Definition.** The deliverable is the point: a room schedule, equipment list with manufacturer, a CSV with GlobalId + Name + selected Pset values, a BoQ table.
**Share.** 19 (1.8%) as the primary intent, but "csv/excel/table" is requested in about 5% of all model_task prompts (it is an output-form modifier on B1, C1, A4).
**Sub-intents.** (a) FM handover lists (room no./name/area/finish); (b) per-class property dump; (c) check list for the dashboard with a given delimiter; (d) lookup from a spreadsheet the user already has (sensor ids to GlobalIds, BCF GUIDs that still exist); (e) one summary table over many files.

| Id | Lang | Lbl | Request | Gloss / why it is a good test |
|---|---|---|---|---|
| ru-aimcp-s011 | ru | S | `объём бетона по этажам, только монолит, ВОР в эксель. если в модели нет Qto - скажи прямо` | Concrete per floor, cast-in-place only, BoQ to Excel, say so if no Qto |
| ru-revit-auto-s009 | ru | S | `сделай ведомость помещений по этажам с площадью и итогом по этажу, в эксель выгрузи` | Room schedule with per-floor total |
| de-data-s012 | de | S | `welche Wände haben keine Feuerwiderstandsklasse? Liste mit GUID und Geschoss raus als csv, Semikolon als Trenner bitte` | CSV with semicolon (European Excel) |
| zh-data-s009 | zh | S | `帮我按楼层统计混凝土构件的体积，梁板柱分开，导出成excel能用的表` | Per floor, beams/slabs/columns separate, Excel-ready |
| ja-japan-s011 | ja | S | `維持管理用に、機器の名称・メーカー・型番・設置階と室をExcelに出して。空欄の項目も分かるように` | FM equipment list; blanks must be visible |
| en-mea-s008 | en | S | `room schedule pls - room no, name, area, floor finish, level. export to excel` | Casual, "pls" |
| en-gis-s004 | en | S | `I have sensor ids like TS-0412 in a spreadsheet, find which elements in the model have that in Tag or any pset and give me their GlobalIds` | Join external data to the model |
| en-guid-s004 | en | S | `here's a list of GUIDs from open BCF issues. which of them are gone in the new IFC and which changed geometry?` | Issue list vs new revision |
| ja-japan-r001 | ja | R | `IfcCSV` outputs only attributes; user wants PropertySet and Material in Excel too | [Zenn article](https://zenn.dev/miyamiyaumya/articles/19a4247133dde6) |
| en-data-r005 | en | R | tender spreadsheet rows must be traceable to IFC elements | [IfcOpenShell issue 7762](https://github.com/IfcOpenShell/IfcOpenShell/issues/7762) |

**Needs.** K10 plus K2/K3/K5 (and a file-writing channel: many servers return text only). **Difficulty.** Medium. **Failure modes.** Claims "exported" with no file or path; pasted table truncated; column mismatch with the request; delimiter/encoding ignored (Excel opens UTF-8 CSV wrongly); rows without GlobalId so they cannot be traced back; hidden filtering (only the first 100 rows).

### Family C. Check quality and compliance

#### C1 completeness_check: "which elements lack X"

**Definition.** Find elements with missing or empty data: no name, no FireRating, no classification, no material, no system, not in a storey, rebar without diameter. The cleanest deterministic test task.
**Share.** 156 (14.8%), the **largest** intent. Persona bim_coordinator (63), bim_manager (23), reviewer_authority (16). Urgent: 19.
**Sub-intents.** (a) per-property missing lists; (b) classification coverage ("what % have a Uniclass/NL-SfB/DIN 276 code"); (c) system membership (MEP elements in no system); (d) handover readiness (COBie fields, MMI, FDV data); (e) loss after export ("my shared parameters vanished, which elements have no custom Pset"); (f) logic traps (PredefinedType set on both occurrence and type).

| Id | Lang | Lbl | Request | Gloss / why it is a good test |
|---|---|---|---|---|
| en-arch-s007 | en | S | `does every IfcSpace have a name, number and area before we upload to the authority portal? list the ones missing` | Pre-submission check |
| ru-dwg-revit-s010 | ru | S | `у труб в модели есть имя системы и диаметр? выдай список без них` | Pipes without system name or diameter |
| ru-mep-s005 | ru | S | `покажи воздуховоды и трубы которые не входят ни в одну систему, ифс из ревита, нужно до сдачи` | Elements in no system; deadline |
| en-eng-s002 | en | S | `which pipes and fittings arent in any IfcSystem? need before coord meeting` | Same in English |
| zh-tw-hk-s004 | zh | S | `查一下牆、門、窗有沒有填防火時效、材料欄位，缺的列出來` | Fire rating and material present? (Traditional Chinese) |
| it-italy-s002 | it | S | `dimmi quali porte non hanno il FireRating nel Pset_DoorCommon` | Doors without FireRating |
| nl-dutch-s002 | nl | S | `welke elementen hebben geen NL-SfB code of niet 4 cijfers? lijst per IFC class graag` | Missing or malformed 4-digit code |
| no-norway-s001 | no | S | `sjekk hvilke objekter som mangler MMI i modellen, grupper per fag og gi meg antall` | Missing MMI maturity value |
| pt-brazil-s002 | pt-BR | S | `exportei do revit e sumiram meus parametros compartilhados no IFC. quais elementos ficaram sem pset customizado?` | Lost shared parameters |
| ko-korea-s002 | ko | S | `레빗에서 내보낸 ifc인데 공유 매개변수가 속성에 하나도 안 보여. 어떤 객체에 Pset이 비어있는지 확인해줘` | Same, Korean |
| en-val-s008 | en | S | `check every slab has Qto_SlabBaseQuantities NetVolume > 0` | Value rule on quantity |
| en-val-s007 | en | S | `any IfcBeam where PredefinedType is set while its type also has one?` | Logic trap |
| en-aimcp-r027 | en | R | README: `Find missing names, classifications, and suspicious property values in this IFC file.` | [flinker-app/ifc-mcp](https://github.com/flinker-app/ifc-mcp) |
| en-revit-auto-r010 | en | R | QC script for duplicate/missing Rooms and untagged Door Tags returned an empty list and a blank Excel; ChatGPT scripts failed | [Dynamo forum](https://forum.dynamobim.com/t/help-with-automated-quality-check-script-getting-empty-list-and-blank-excel/112252): a user already burned by AI |

**Needs.** K2, K3 (K4 for storey/system relations); optional K10 for the list. **Difficulty.** Medium (95), hard (33), easy (28). **Failure modes.** L7 (guessing, or treating "absent" as "zero"/PASS: correct output separates PASS / FAIL / UNKNOWN); L14 (checks only occurrence psets, misses type-level inheritance); empty string vs missing vs `NOTDEFINED` treated alike; incomplete list when more than the page size; false positives from the wrong Pset name (e.g., `Pset_DoorCommon` vs a custom pset); no GlobalId; over-reporting thousands of rows without grouping.

#### C2 rule_validation: IDS, schema, MVD, EIR/BEP requirements

**Definition.** Check the model against a formal rule set: an IDS file (machine-readable requirements), the IFC schema (does the file even parse and conform), a view definition (MVD), a client's information requirements (EIR, BEP, "capitolato", "MIDE"), a classification list.
**Share.** 58 (5.5%) in model_task; 108 (3.0%) overall. Personas: bim_manager (20), bim_coordinator (18), reviewer (7). Hard: 16.
**Sub-intents.** (a) run a **given** IDS and summarize failures (by class, by requirement, by discipline); (b) write an IDS from a sentence ("every IfcWall must have FireRating and IsExternal") and run it; (c) schema/syntax validation with top error types; (d) delivered version check ("the client wants IFC2x3, is this file 2x3 and the right view?"); (e) value validity (are the NL-SfB codes real codes?); (f) duplicate or invalid GlobalIds; (g) COBie readiness.

| Id | Lang | Lbl | Request | Gloss / why it is a good test |
|---|---|---|---|---|
| ru-autodesk-telegram-s012 | ru | S | `проверь модель по этому IDS ЦГЭ и дай сводку нарушений по классам, самые частые сверху` | Run a supplied IDS, summarize by class |
| en-permit-s003 | en | S | `run this IDS against the model and give me failures grouped by requirement, not one huge list` | Grouping requirement |
| en-fmor-s003 | en | S | `run our IDS on the contractor model and give me a short fail list I can send back, grouped by discipline` | Audience: the contractor |
| zh-tw-hk-s012 | zh | S | `樓梯踏面跟級高有沒有符合建築技術規則？列出不合格的` | Stair tread/riser vs building rules |
| en-val-s001 | en | S | `run the model thru schema validation, give me top 10 error types w/ counts` | Schema validation summary |
| de-err-s009 | de | S | `Prüf mal das Modell auf Schemafehler, Navisworks meckert beim Öffnen` | Schema errors; a viewer complained |
| zh-vm-s007 | zh | S | `甲方要求交付IFC2x3，帮我检查一下这个文件的版本和视图定义对不对` | Delivered version and view definition |
| pt-cobie-s012 | pt | S | `tem como ver quais elementos tao sem os campos obrigatorios do cobie? preciso entregar pro cliente` | COBie required fields |
| ko-korea-s015 | ko | S | `IDS 파일 기준으로 이 모델 검증하고 실패한 객체 알려줘` | IDS validation, list failing objects |
| en-val-s005 | en | S | `it says guid error, find dup or invalid GlobalIds in model` | GUID integrity |
| en-model-checking-s004 | en | S | `NL-SfB codes in here are all filled but are they actually valid codes?? check against the list` | Validity vs presence |
| ru-autodesk-telegram-r012 | ru | R | как проверять IFC по IDS пакетно, с отчётами html и json | [Habr 883016](https://habr.com/ru/articles/883016/) |
| en-fmor-r004 | en | R | 70 IFC models to check against 6 IDS files in specific pairs, with a script | [OSArch thread](https://community.osarch.org/discussion/2273/ifctester-script-for-testing-several-ifcs-with-several-ids) |
| en-bsforum-r036 | en | R | writing an IDS that proves a beam occurrence has a `PredefinedType` while the type also has one | [buildingSMART forum 6180](https://forums.buildingsmart.org/t/6180) |

**Needs.** K7 (IDS and schema checks exist in only a few servers), K3; K10 (BCF) optional. **Difficulty.** Medium-hard. **Failure modes.** L7, L10 (reports "valid" without running a validator); L11 (version rules differ: IDS facets and IFC2x3 occurrence types); confusing IDS pass with schema pass; inventing an IDS facet that does not exist; ignoring cardinality (optional/prohibited are subtle, see [That Open issue 821](https://github.com/ThatOpen/engine_components/issues/821)); producing an IDS that cannot be parsed; answering for a file it never loaded.

#### C3 mapping_geometry_audit: proxies, wrong classes, duplicates, broken geometry, encoding

**Definition.** Find *technical defects* in how the model was exported or built, rather than missing project data: elements exported as generic `IfcBuildingElementProxy`, wrong class/predefined type, duplicate elements or GlobalIds, geometry-less items, openings that do not cut, mangled characters (`\X2\...\X0\`), tessellated vs parametric representation.
**Share.** 76 (7.2%). Personas: bim_coordinator (33), bim_manager (14), architect (10).
**Sub-intents.** (a) proxy diagnosis (which categories, which should be what); (b) duplicates (same class same place) with a tolerance; (c) geometry presence and type (SweptSolid vs Tessellation, needed for a clash tool); (d) openings/voids exist where doors and windows are; (e) encoding corruption; (f) attribute vs geometry disagreement (areas, heights); (g) curtain wall structure (panels and mullions as children).

| Id | Lang | Lbl | Request | Gloss / why it is a good test |
|---|---|---|---|---|
| ru-habr-dev-s005 | ru | S | `найди дубли элементов - одинаковые стены стоящие друг в друге, по bbox в пределах 5 мм, не удаляй, просто список` | Duplicates by bbox tolerance, report only |
| zh-csdn-dev-s002 | zh | S | `这个ifc里构件名字全是\X2\xxxx\X0\这种，读出来是乱码，帮我看看哪些实体的Name有这个，解码后给我真实中文` | Decode `\X2\` escapes, show real Chinese |
| enc-s010 | de | S | `stimmen Umlaute und Dezimalkommas in den Psets, oder sind da \X\ Reste und Texte statt Zahlen` | Umlauts and decimal commas as text |
| en-s018 | en | S | `I dont trust the slab areas in this model. recompute from geometry and compare with Qto_SlabBaseQuantities, show anything off by more than 2%` | Recompute and compare (needs geometry kernel) |
| ja-proxy-s008 | ja | S | `IfcBuildingElementProxyになってる要素の中で、柱っぽいもの(縦長のやつ)を洗い出して、IfcColumnにすべきか教えて` | Heuristic reclassification suggestion |
| it-err-s013 | it | S | `dimmi quali elementi non hanno geometria, il viewer dice 'unexpected mesh type'` | Elements without geometry |
| fr-guid-s011 | fr | S | `verifie que tous les GlobalId sont valides (22 caracteres base64) et qu'il n'y a pas de doublons dans la maquette` | GlobalId format and uniqueness |
| en-autodesk-revit-export-s006 | en | S | `curtain wall - are panels and mullions children of the IfcCurtainWall? show the tree` | Hierarchy of a composite element |
| ru-dwg-other-s005 | ru | S | `в модели ренги какое представление геометрии у колонн и стен - SweptSolid или Tessellation? для нависа надо` | Representation type for Navisworks |
| en-blogs-linkedin-s001 | en | S | `how many IfcBuildingElementProxy in this one and which storeys have the most? need to send it back to the architect` | Proxy census with a destination |
| ru-habr-dev-r007 | ru | R | площадь по геометрии зон не сходится с атрибутом и с XML АГР | [Habr 1100956](https://habr.com/ru/articles/1100956/) |
| en-blogs-linkedin-r020 | en | R | my IFC has proxies and extra storeys, duplicates of other disciplines' walls | [BIM Corner: 10 common export mistakes](https://bimcorner.com/10-common-ifc-export-mistakes-to-avoid-part-1/) |

**Needs.** K2, K3, K4; geometry analysis (bounding boxes, representation type) is rarely a dedicated tool, so it often falls to K15 (code). **Difficulty.** Medium (46), hard (18). **Failure modes.** L16 (geometry-less file); L15 (cannot see escapes because the library already decoded them, or decodes wrongly); false duplicates (mapped instances share a representation but sit apart); "fixing" instead of reporting when told "don't delete"; L21 (uses the code tool silently); inventing a tolerance.

#### C4 regulation_check: building code, permit, national submission

**Definition.** Check against rules of an authority or a standard that live outside the model: egress door widths, accessibility, stair dimensions, setback and height for a permit, a national IFC submission profile (CORENET X, SZ-IFC, TEK17, state expertise).
**Share.** 24 (2.3%) of file tasks; 118 (3.3%) overall because real regulation threads are common ("what must we submit?"). Persona: reviewer_authority (14 of 24). Hard: 14 of 24.
**Sub-intents.** (a) metric rules computable from the file (clear width >= 850 mm, corridor width, stair width); (b) presence of mandated data ("does the model contain the classes and psets required for submission X"); (c) project-brief rules (client BIM guideline: classification, storeys named as in the structural model); (d) schema version required (IFC4 only?); (e) permit geometry (height, setback) which needs a site boundary.

| Id | Lang | Lbl | Request | Gloss / why it is a good test |
|---|---|---|---|---|
| en-aimcp-s002 | en | S | `check every door in the model for clear width >= 850mm, give me a list of failures with storey and GUID, dont guess if the data is missing` | The canonical honest-check prompt (PASS/FAIL/UNKNOWN) |
| en-permit-s001 | en | S | `need to submit to corenet x tomorrow, can u check if my ifc has all the IFC-SG required classes and psets? list what's missing` | Urgent; data presence only, no approval claim |
| ru-arch-s011 | ru | S | `проверь этажи и отметки в модели, чтобы совпадали с КР, завтра сдача на экспертизу` | Cross-discipline consistency before state review |
| no-norway-s014 | no | S | `sjekk dørbredder i rømningsveier mot TEK17, hvilke dører er under 90 cm` | Escape-route doors vs TEK17 |
| fr-permit-s014 | fr | S | `vérifie l'accessibilité PMR : portes < 90 cm et couloirs < 1,40 m dans la maquette, liste avec niveau` | Accessibility thresholds |
| zh-lightweight-review-s016 | zh | S | `楼梯净宽和走道宽度查一下，哪些小于规范要求` | "Smaller than the code requires" without naming the code |
| pt-permit-s015 | pt | S | `confere a altura total do edificio e o recuo do lote no ifc, preciso pro alvará` | Height and setback need a lot boundary |
| ko-korea-s003 | ko | S | `발주처 BIM 지침 기준으로 층/공간/부재 분류 누락된 거 있나 체크해줘` | Client guideline: classification gaps |
| en-sg-corenetx-s002 | en | S | `is this file ifc4 or 2x3? corenet x only takes ifc4 right` | Schema gate for Singapore |
| zh-zhihu-r025 | zh | R | 报批报建之 Revit 端自检工具 | [Zhihu 633827596](https://zhuanlan.zhihu.com/p/633827596) |
| ru-dwg-other-r017 | ru | R | с 01.07.2019 госэкспертиза: нужно ли переходить на ТИМ | [dwg.ru thread](https://forum.dwg.ru/showthread.php?t=153428) |
| no-norway-r012 | no | R | which properties does NS 8360 require in the model, e.g. Milestone and IsProcured | [buildingSMART Norge](https://www.buildingsmart.no/standarder/kort-forklart.html) |

**Needs.** K3, K5, K7; rules must be supplied by the user or encoded in a special server (e.g., `ifc-ruhsat` for Turkey). **Difficulty.** Hard. **Failure modes.** Claiming a pass of the official check (never possible; correct output: "data present / missing / cannot determine"); applying the wrong country's threshold; treating a missing width as compliant (L7); using nominal (type) width instead of clear opening width; unit errors in thresholds (L12); inventing clause numbers. See [regulations and permits questions](../05_real_world_questions/by_topic/regulations_permits_contracts.md).

### Family D. Compare and coordinate

#### D1 version_diff: what changed

**Definition.** Compare two revisions, two exports, or two disciplines' files: added, deleted, moved, changed property, changed class. Often by GlobalId, with the twist that exporters regenerate GlobalIds.
**Share.** 72 (6.9%), of which 59 are labeled hard, the **highest hard share** of any intent. Persona bim_coordinator (34), bim_manager (17). Urgent: 9.
**Sub-intents.** (a) added/deleted/changed by GlobalId; (b) **GUID churn**: match by type + name + position because IDs changed; (c) scope-limited diffs (only ducts, only walls); (d) what changed in properties vs geometry; (e) classes that exist in schema A but not B (IFC4 to IFC2x3); (f) compare counts per storey between disciplines; (g) check that issue GUIDs still exist.

| Id | Lang | Lbl | Request | Gloss / why it is a good test |
|---|---|---|---|---|
| ru-renga-nanocad-s006 | ru | S | `сравни две выгрузки, вчерашнюю и сегодняшнюю, что добавили что удалили что поменяли` | Daily exports |
| zh-guid-s007 | zh | S | `两次导出的IFC，GUID全不一样，帮我按类型和坐标匹配一下，看看到底哪些构件真的改了` | Every GUID different: match by type + position |
| en-coord-s003 | en | S | `compare last week's struct IFC with today's. guids got regenerated so match by type+name+position. what was added/removed/moved?` | Same trap, English |
| de-dach-s008 | de | S | `vergleich mal Stand 12 und Stand 14 vom Rohbau-IFC. was ist neu, was weg, was verschoben? GUIDs ändern sich bei uns teilweise` | GUIDs partly change |
| ja-japan-s006 | ja | S | `先週のIFCと今日のIFC比べて、追加・削除・変更された部材をGlobalIdベースで出して。変更は属性か形状かも` | Say whether property or geometry changed |
| es-latam-s009 | es | S | `compara el ifc de hoy con el de la semana pasada, qué elementos nuevos, borrados y movidos` | Weekly diff |
| fr-francophone-s005 | fr | S | `compare l'indice B et l'indice C de la maquette, je veux les éléments ajoutés/supprimés/modifiés avant la synthèse` | Revision indices B vs C |
| no-norway-s009 | no | S | `hva har endret seg i RIB-modellen siden forrige revisjon? trenger før møtet i morgen` | Before tomorrow's meeting |
| pt-vm-s009 | pt | S | `quais entidades do meu modelo ifc4 nao existem no ifc2x3? preciso entregar em 2x3` | Schema difference, not version diff |
| it-proxy-s010 | it | S | `confronta i due IFC (v1 e v2) e dimmi quanti proxy abbiamo ancora e quali sono stati riclassificati` | Diff plus proxy follow-up |
| en-osarch-guid-r001 | en | R | Revit regenerates GlobalIds for some categories, so a GlobalId-only diff marks everything as changed | [OSArch 3616](https://community.osarch.org/discussion/3616/browser-based-ifc-clash-version-diff-how-would-you-group-clashes-and-handle-guid-churn) |
| it-italy-r009 | it | R | due revisioni dello stesso IFC: come vedo cosa è cambiato (aggiunti, rimossi, modificati) | [Biblus](https://biblus.acca.it/rilevare-modifiche-nei-modelli-ifc/) |
| en-revit-auto-r025 | en | R | standard compare tools match by ElementId, so independently built models look entirely different | [pyRevit forum](https://discourse.pyrevitlabs.io/t/revit-model-compare-check-what-the-ai-actually-built/10681) |

**Needs.** K13 (rare; `ifcopenshell-mcp compare_ifc_models`, ifc-lite diff) or K2+K3 on both files; K1 must be able to hold **two** files. **Difficulty.** Hard. **Failure modes.** Loads only one file; GUID-only diff declares everything changed (L8); reports "moved" for rounding noise; does not state the matching rule; ignores deleted items; no count summary; truncated output on large diffs; compares the wrong pair.

#### D2 clash_coordination: overlaps, BCF issues, missing openings

**Definition.** Find where disciplines collide (ducts through beams, pipes through walls with no opening), set tolerances, group results, create BCF issues for the model owner. Also "which penetrations still need a sleeve".
**Share.** 34 (3.2%); urgent in 19 of 34, hard in 25, the highest urgency of any intent. Persona bim_coordinator (21), MEP (11).
**Sub-intents.** (a) hard clash between two systems with tolerance (10 mm, 20 mm, 50 mm); (b) grouping by storey/discipline so the list stays readable; (c) BCF output with GlobalIds and positions; (d) penetration/sleeve lists (pipe crosses wall/slab/beam without an opening); (e) soft/clearance clashes; (f) BCF round trip (do the issue GUIDs exist in the model).

| Id | Lang | Lbl | Request | Gloss / why it is a good test |
|---|---|---|---|---|
| ru-renga-nanocad-s014 | ru | S | `найди пересечения труб с балками и скинь в бцф` | Short, "бцф" for BCF |
| ru-openings-s010 | ru | S | `найди трубы и воздуховоды которые пересекают стены/перекрытия, а отверстия нет, список с отметками` | Missing openings |
| en-model-checking-s005 | en | S | `clash ducts vs structural beams, 10mm tolerance, group by level. dont give me 300 lines for one duct run` | Readable grouping requirement |
| en-allplan-vw-bentley-s011 | en | S | `run clash arch vs struct, hard clashes only, tolerance 10mm` | Minimal prompt |
| zh-eng-s012 | zh | S | `机电管线和结构梁碰撞结果导出成bcf，按楼层分组` | Export BCF, group by floor |
| de-dach-s015 | de | S | `mach mir aus den Kollisionen Rohr/Wand ein BCF mit Position und Bauteil-GUID, Durchbruch fehlt` | BCF with position and GUID |
| ja-japan-s008 | ja | S | `天井内のダクトと梁の干渉探して、BCFにして出して。クリアランス50mmで` | Clearance 50 mm |
| pt-brazil-s007 | pt-BR | S | `roda clash entre dutos e vigas da estrutura e gera os apontamentos em BCF pra mandar pro projetista` | Issues for the designer |
| fr-francophone-s017 | fr | S | `fais un clash gaines vs structure, tolérance 2 cm, et sors les points en BCF` | Tolerance 2 cm, points in BCF |
| no-norway-s010 | no | S | `kollisjonskontroll RIV mot RIB, lag BCF av de over 50 mm` | Only clashes over 50 mm |
| en-eng-r023 | en | R | the two clash points per clash vary with element order and do not match bbox corners | [IfcOpenShell issue 6138](https://github.com/IfcOpenShell/IfcOpenShell/issues/6138) |
| zh-revit-auto-r026 | zh | R | 机电管线穿过墙、板或梁时要逐笔确认穿透位置与开孔大小;希望AI回传候选清单 | [REVIT_MCP_study issue 99](https://github.com/shuotao/REVIT_MCP_study/issues/99): penetration list as an AI tool |

**Needs.** K12, K10 (BCF), K14 for viewpoints; the capability exists in few servers (Navisworks bridge, rvt-mcp, Horizun, Demolinator, ifc-lite CLI). **Difficulty.** Hard. **Failure modes.** Claims clashes without running a geometry test; wrong units for tolerance (L12, [IfcClash reported mm in a feet project](https://github.com/IfcOpenShell/IfcOpenShell/issues/7178)); one issue per triangle pair (hundreds of rows for one duct run); BCF references GUIDs not in the model; timeouts on large models (L3); mixes up the two model sets (A vs B reversed).

### Family E. Change the model

All E intents are **write** operations. They need the safety behaviours in section 6 of the companion file (L5, L6, L18-L22) and a server in write mode. About 10% of file-task prompts write; real MCP issues involve writing far more often.

#### E1 edit_data: change class, properties, names, storey assignment

**Definition.** Modify *existing* elements: re-class proxies, set or copy property values, add a classification code from a table, rename, move elements to a storey, fix units or encoding.
**Share.** 87 (8.3%); hard 43, medium 42. Persona bim_coordinator (24), architect (17), bim_manager (12).
**Sub-intents.** (a) reclassify by name pattern (proxy "Ограждение*" to `IfcRailing`); (b) bulk property set/copy (fire rating from type to instance); (c) add a classification from a lookup table, report unmatched; (d) rename to a naming convention; (e) move elements between storeys; (f) georeference an existing model; (g) repair (decode wrong code page, fix property data types).

| Id | Lang | Lbl | Request | Gloss / why it is a good test |
|---|---|---|---|---|
| ru-autodesk-telegram-s009 | ru | S | `перебей класс у всех IfcBuildingElementProxy с именем 'Ограждение*' на IfcRailing и сохрани новую версию` | Pattern + save new version |
| ru-habr-dev-s002 | ru | S | `исправь тип у RUS_Area и RUS_Volume на IfcReal, Pset_* не трогай. сохрани как новый файл` | Narrow scope, keep rest untouched |
| zh-revit-export-s008 | zh | S | `把所有名字带'柱'的代理构件改成IfcColumn，别的不要动` | "Change only these, leave the rest" |
| de-dach-s012 | de | S | `die Stützen sind alle als Proxy drin, kannst du die zu IfcColumn machen? Name fängt mit ST_ an` | Proxy to column by name prefix |
| es-proxy-s005 | es | S | `los zócalos y vierteaguas salen como proxy, cámbialos a IfcMember o IfcCovering segun el caso y dime cuales tocaste` | Decision per case, report touched |
| ja-japan-s009 | ja | S | `ドアにタイプ名ごとに分類コード付けたい。D-1→21-21 11みたいな対応表あるからそれで一括で` | Mapping table by type name |
| en-revit-auto-s004 | en | S | `copy Fire Rating from the type to a Fire_Rating_Inst shared param on every door, tell me which ones are blank` | Copy and report blanks |
| en-reddit-s007 | en | S | `assign concrete C30/37 to all IfcColumn that have no material` | Conditional assignment |
| ko-korea-s007 | ko | S | `proxy로 나온 것 중 이름에 '기둥' 들어간거 IfcColumn으로 바꿔줘` | Korean, same pattern |
| no-norway-s015 | no | S | `sett IsProcured = true på alle prefab betongelementer og lagre ny ifc` | Set a flag, save new file |
| mul-coord-s014 | fr | S | `peux-tu ajouter le géoréférencement Lambert 93 (EPSG:2154) à la maquette, X 652000 Y 6862000` | Write georeference |
| en-aimcp-r038 | en | R | README: `Find walls on Level 02, show their Comments values, and propose a batch update.` | [aec-model-bridge](https://github.com/Sam-AEC/aec-model-bridge): read, propose, then apply |
| en-gh-proxy-r033 | en | R | tried to split a proxy into pipe segments in Bonsai and got an error | [IfcOpenShell issue 6299](https://github.com/IfcOpenShell/IfcOpenShell/issues/6299) |

**Needs.** K8, K0 (preview/approve/undo), K2/K3 to select targets, K10 to save a copy. **Difficulty.** Medium-hard. **Failure modes.** L5 (claims done without persisting; correct: read back values and counts); L19 (overwrites the original); L20 (touches too much: "Wall*" matches more than intended; GUIDs regenerated); L18 (no preview of the planned changes); changing the class without moving the associated type/psets; saving a file with invalid schema attributes (L17); partial application reported as complete; instance vs type edit confusion (L14).

#### E2 create_elements: draw walls, add storeys, build a small model

**Definition.** Create **new** geometry or objects from a description: a wall between two points, a rectangle of walls, a door in a wall, storeys at heights, a clearance volume, a small building, a cost schedule.
**Share.** 12 (1.1%) in file tasks, but it is the most visible theme in real MCP issues and README examples (wall creation in 5 different servers, [companion file section 4.4](what_ifc_mcp_servers_do.md#44-how-real-prompts-look-use-this-when-generating-test-requests)).
**Sub-intents.** (a) single-element creation with coordinates and level; (b) small compositions (rectangle of 4 walls, then count them); (c) hosted elements (door/window in a wall); (d) DWG to model (turn a CAD layer into walls on a chosen level); (e) project scaffolding (storeys, grids); (f) non-physical objects (virtual element, cost schedule).

| Id | Lang | Lbl | Request | Gloss / why it is a good test |
|---|---|---|---|---|
| en-aimcp-s005 | en | S | `draw a 6m wall on level 2 from 0,0 to 6000,0 - make sure its really on level 2 and type is generic 200` | Level and type verification |
| es-aimcp-s016 | es | S | `creá cuatro muros de 3 m en rectángulo 5x4 y después contame cuántos hay` | Rioplatense voseo; create then count |
| zh-revit-auto-s012 | zh | S | `把DWG的A-WALL圖層翻成牆,放在2F,牆型用RC牆200` | DWG layer to walls on 2F with a named wall type |
| en-bsforum-s013 | en | S | `add a clearance volume IfcVirtualElement CLEARANCE around pump P-101 and assign it to the pump` | Non-physical element with relation |
| en-qto-s005 | en | S | `create a cost schedule 'Tender', add a cost item per wall type and link the quantities NetVolume` | IFC cost objects (rare) |
| en-aimcp-r037 | en | R | README: `place exterior walls around a 20x12m rectangle on the ground floor` | [ifcx-mcp](https://github.com/louistrue/ifcx-mcp) |
| en-aimcp-r044 | en | R | README: `create a wall between two 3D points` | [ifc-bonsai-mcp](https://github.com/Show2Instruct/ifc-bonsai-mcp) |
| en-aimcp-r003 | en | R | Claude says it will create a 10-metre wall once connected; port 8080 open, no luck | [mcp-servers-for-revit issue 1](https://github.com/mcp-servers-for-revit/mcp-servers-for-revit/issues/1): first thing newcomers try |
| zh-aimcp-r010 | zh | R | AI 建牆時沒有樓層參數就取第一個 Level，牆建到非預期樓層 | [REVIT_MCP_study issue 144](https://github.com/shuotao/REVIT_MCP_study/issues/144): wrong-level default |
| en-aimcp-r007 | en | R | door placed ignoring x/y/z and host: `FamilyInstance.Host` is null | [rvt-mcp issue 13](https://github.com/bimwright/rvt-mcp/issues/13) |
| en-aimcp-r006 | en | R | stairs: no tool, `send_code_to_revit` hung Revit for ~60 s then crashed | [rvt-mcp issue 14](https://github.com/bimwright/rvt-mcp/issues/14) |

**Needs.** K9, K0; K14 helps verification. **Difficulty.** Medium-hard; stairs, curtain walls, families and MEP joins are known-hard categories. **Failure modes.** L6 (wrong level/elevation/host, silent defaults); L3 (timeouts create duplicates on retry, [Tapir issue 23](https://github.com/SzamosiMate/tapir-archicad-MCP/issues/23)); L17 (invalid IFC from LLM-written code); no read-back; millimetres vs metres in coordinates; creating in a link or the wrong document.

#### E3 batch_automation: many items, many files, repeated chores

**Definition.** Rule-based bulk work, usually in Revit: rename all views by a pattern, make a sheet per level, number elements, clean up unused parameters or filters, run a check over many files, export one IFC per 3D view.
**Share.** 11 (1.0%) as primary file tasks; 62 (1.7%) overall (raw `automate_batch`: 64 records). Real Dynamo/pyRevit forums are full of these ([ai-revit-tasks](../research_raw/wave1/ai/ai-revit-tasks.md)): 40+ views duplicated, renamed and templated in one prompt is the typical success story.
**Sub-intents.** (a) naming conventions for views and sheets, no duplicate names; (b) sheet and viewport generation; (c) parameter housekeeping (find unused first, "don't delete yet"); (d) multi-file jobs (check six IFCs, one summary table); (e) numbering along a path; (f) pre-publish routines (unload links, close worksets).

| Id | Lang | Lbl | Request | Gloss / why it is a good test |
|---|---|---|---|---|
| ru-revit-auto-s008 | ru | S | `переименуй все виды этажей по шаблону ПЛ_{уровень}_{имя}, дубли имён не плодить` | Pattern, no duplicate names |
| en-revit-auto-s001 | en | S | `rename all floor plan views to 'L{level number}_{old name}' and skip anything already prefixed` | Idempotent: skip prefixed |
| en-revit-auto-s002 | en | S | `make a sheet per level, put the plan on it, number them A101 upward, use our A1 titleblock` | Sheets, numbering, titleblock |
| zh-revit-auto-s013 | zh | S | `每層平面圖自動出圖,圖號 A-101 往上編,視圖放到圖紙中間` | Same in Chinese, centered viewport |
| es-revit-auto-s014 | es | S | `renombra todas las vistas de planta con el nivel delante y crea una lámina por cada una, numeradas A-01, A-02...` | Spanish combination |
| ru-autodesk-telegram-s017 | ru | S | `прогони все 6 ифс из папки на наличие обязательных свойств и скинь одну сводную таблицу, сроки горят` | Multi-file, one summary |
| ja-aimcp-s014 | ja | S | `部屋名が空のものを一覧にして、変更案を出してから反映してください` | List empties, propose, then apply |
| en-revit-auto-s005 | en | S | `which project parameters, view filters and line patterns are unused? don't delete yet` | Report before cleaning |
| en-autodesk-revit-export-s010 | en | S | `batch export ifc for each 3D view in the revit project, ifc4 reference view, to a folder` | Batch export |
| en-revit-auto-r007 | en | R | make a view plan per apartment with the crop region exactly on the apartment's boundary walls | [Dynamo forum](https://forum.dynamobim.com/t/automate-the-creation-of-view-plans-of-each-appartment-with-the-cropzone-aligning-exactly-on-the-outer-boundary-of-the-boudnary-walls-of-each-appartment/115202) |
| en-revit-auto-r019 | en | R | deleting redundant ("zombie") project parameters that only hide from the UI | [Dynamo forum](https://forum.dynamobim.com/t/deleting-zombie-parameters/112603) |

**Needs.** K8, K2, K15 (Revit APIs are mostly reached through the code tool), K10. **Difficulty.** Medium-hard. **Failure modes.** L18 (no dry run); L3 (timeout in the middle leaves a half-renamed project); non-idempotent reruns; naming collisions; partial success reported as complete; context overflow on 100+ items (L4); destroying data that is used (deleting parameters used in schedules).

### Family F. Move, show, slim down

#### F1 convert_exchange: to another format or version, or into IFC

**Definition.** Produce another representation: IFC to GLB/glTF for a web viewer, DWG for AutoCAD, FBX, CityGML, SQLite, RDF; IFC4 to IFC2x3 for a subcontractor; a lightweight copy; Revit to IFC with a view definition; map one classification system to another.
**Share.** 35 (3.3%); 154 (4.3%) overall (real conversion questions are frequent). Persona bim_coordinator (12), developer (9).
**Sub-intents.** (a) IFC to visual formats keeping GlobalId/colours per mesh; (b) downgrade schema (what is lost?); (c) lightweight/filtered copy (walls and slabs only); (d) data formats (SQLite, RDF/SPARQL, Excel); (e) GIS (CityGML LoD2, GeoPackage) with a georeference sanity check first; (f) native Revit to IFC options.

| Id | Lang | Lbl | Request | Gloss / why it is a good test |
|---|---|---|---|---|
| zh-csdn-dev-s003 | zh | S | `帮我把这个ifc转成glb给前端用，每个mesh要带GlobalId，不然属性对不上，按楼层拆开最好` | GLB with GlobalId per mesh, split by floor |
| ru-viewconv-s011 | ru | S | `нужен dwg из этого ифс, чтоб слои по классам, а то в автокаде одним куском` | DWG with layers per class |
| fr-vm-s011 | fr | S | `peux tu me sortir une version ifc2x3 de ce modele, le sous-traitant n'ouvre pas l'ifc4` | IFC2x3 copy for a subcontractor |
| en-viewconv-s002 | en | S | `glb export but only walls+slabs, file is 600mb, wanna keep it under 50` | Filter plus size target |
| en-fs-s005 | en | S | `make me a light version for the web viewer - only walls slabs columns, no psets, and save as ifczip` | Light copy |
| de-gis-s014 | de | S | `kannst du aus dem Gebäude ne Außenhülle für CityGML LoD2 ableiten? nur Dach und Wände, Geschosse bitte als Attribut` | CityGML LoD2 shell with storey attribute |
| ko-viewconv-s014 | ko | S | `철골 기둥만 fbx로 뽑아줘 시각화팀 줘야돼` | Steel columns only to FBX |
| en-data-s003 | en | S | `convert this ifc to sqlite and then run a query for count of elements by ifc class, biggest first` | Convert, then query |
| ja-infra-s014 | ja | S | `道路の線形をIFC4.3に変換して、平面線形の曲線要素(クロソイド含む)がちゃんと入ってるか確認して` | Alignment to IFC4.3, check clothoid elements |
| en-viewconv-s006 | en | S | `before I push this to QGIS check units and IfcMapConversion, last time it landed in the ocean` | Pre-flight georef check (F1+A5) |
| it-classbsdd-s017 | it | S | `converti i codici da uniclass a omniclass usando la tabella excel e riscrivi le reference` | Reclassification (really E1) |
| it-italy-r023 | it | R | dall'IFC come estraggo piante e sezioni in DXF? | [Biblus guide](https://biblus.acca.it/una-guida-completa-per-convertire-file-ifc-in-dxf/) |
| en-civil-infra-r029 | en | R | `IfcConvert --site-local-placement` breaks positioning for a rail model | [IfcOpenShell issue 6102](https://github.com/IfcOpenShell/IfcOpenShell/issues/6102) |

**Needs.** K11 (few servers), K10; K6 for GIS targets. **Difficulty.** Medium-hard. **Failure modes.** L16 (no geometry); conversion silently drops data (alignments in IFC2x3, psets in GLB) without telling; writes over the source; wrong units in the target; output path invented; "converted" with no file; for Revit servers, no IFC export tool exists (use only for refusal tests).

#### F2 visualize_view: screenshot, highlight, isolate, camera

**Definition.** Ask to *see* something: capture the current view as an image, highlight failing elements, isolate a system, rotate or zoom the camera, open a viewer, apply a BCF viewpoint. Matters for multimodal models that verify what they built.
**Share.** 2 (0.2%) in the corpus; real MCP issues show the need clearly (screenshots for AI vision, camera control).
**Sub-intents.** (a) screenshot of the active view; (b) colour or isolate by property ("show all fire doors in red"); (c) camera/zoom commands; (d) show the result of a check in 3D; (e) verify a created object visually ("put the sofa by the window").

| Id | Lang | Lbl | Request | Gloss / why it is a good test |
|---|---|---|---|---|
| en-aimcp-r017 | en | R | wish: capture the current view as an image so the model can verify `put the sofa here, by the window` | [revit-mcp-server issue 16](https://github.com/LuDattilo/revit-mcp-server/issues/16) |
| sk-aimcp-r016 | sk | R | `Oddiaľ pôdorys o 15 percent.` / `Ukáž vzduchotechniku v perspektíve na celú obrazovku.` (zoom the plan out 15 percent; show the ventilation in perspective, full screen) | [AIMviewer issue 65](https://github.com/Menezeris/AIMviewer/issues/65): camera control as a tool |
| en-aimcp-r040 | en | R | README: `dimension every wall on this view; check the curtain-wall elevations` | [mcp-servers-for-revit](https://github.com/mcp-servers-for-revit/mcp-servers-for-revit): acts on the active view |
| en-mea-s006 | en | S | `model opens far from origin in the viewer. what coordinate system is it using? is there an IfcMapConversion, what are eastings northings` | Viewer symptom, but the work is A5 |
| mx-mcl-s001 | en | S | `half my walls come out grey in the viewer, which ones have no IfcSurfaceStyle at all?` | Viewer symptom, work is data lookup |
| (none) | en | D | `show me all fire doors on level 2 in red and take a screenshot` | Highlight + capture |
| (none) | ru | D | `покажи в 3D только трубы системы ОВ-1, остальное скрой, и скинь картинку` | Isolate by system, then image |
| (none) | zh | D | `把没填防火等级的门标成红色，截个图给我` | Visual output of a C1 check |

**Needs.** K14 (Bonsai, APS, some Revit servers). Pure IFC readers cannot. **Difficulty.** Medium. **Failure modes.** Pretends to have seen an image; claims a highlight with no tool result; screenshot of the wrong view; colour changes persisted into the model (a write!); hidden elements not restored.

#### F3 optimize_performance: "file too big / slow, what is heavy"

**Definition.** Diagnose size or speed: which classes or families dominate the file, duplicated geometry, empty/redundant Psets, the heaviest elements by triangles, whether it will fit browser limits; sometimes slim the file or split by storey.
**Share.** 21 (2.0%); 87 (2.4%) overall; bim_manager (9), developer (6). Languages: en 8, zh 6.
**Sub-intents.** (a) "900 MB, what takes the space" by class; (b) top-N heaviest elements by triangle count; (c) mapped-item reuse vs duplicated geometry; (d) remove 2D/annotations/empty psets and estimate the saving; (e) split by storey for a web viewer; (f) memory-aware reading (lazy open).

| Id | Lang | Lbl | Request | Gloss / why it is a good test |
|---|---|---|---|---|
| ru-fs-s006 | ru | S | `ифс весит 900 мб, откуда столько? глянь по классам что самое тяжёлое и что можно выкинуть не ломая модель` | Heaviest classes; what is safe to drop |
| en-graphisoft-s012 | en | S | `ifc is 900mb, what is eating the size` | Terse |
| en-geom-s003 | en | S | `file is 400mb, which elements are the heavy ones? faceted breps with crazy face counts, top 20 pls` | Top 20 by faces |
| en-fs-s003 | en | S | `check if repeated families are exported as IfcMappedItem or duplicated geometry, how much size would we save` | Geometry reuse |
| zh-csdn-dev-s010 | zh | S | `这个ifc 600多M前端根本加载不动，看看是什么占的体积，能不能砍掉不需要的东西` | What dominates; what can be cut |
| zh-tw-hk-s003 | zh | S | `IFC檔太大 300MB 傳不上系統，幫我看是哪些東西最肥` | Upload limit |
| de-fs-s011 | de | S | `die ifc ist 700 MB und solibri braucht ewig, kannst du leere psets und nicht benutzte Eigenschaften rausnehmen?` | Remove empty psets |
| es-fs-s009 | es | S | `el ifc me pesa 600mb, puedes quitar los elementos 2D y las anotaciones y decirme cuanto baja?` | Remove 2D, report the saving |
| ja-fs-s013 | ja | S | `400MBのIFCをlazyで開いて壁だけ数えて。メモリどれくらい使った？` | Lazy open and memory report |
| no-norway-s016 | no | S | `ifc-filen er 900 MB og tung å åpne. hva tar mest plass` | Norwegian |
| en-gh-ifcopenshell-r002 | en | R | a 2 GB IFC from Synchro, 16 GB RAM, `open()` runs out of memory | [IfcOpenShell issue 2025](https://github.com/IfcOpenShell/IfcOpenShell/issues/2025) |
| zh-csdn-dev-r001 | zh | R | 模型能导出、能加载、能显示，不等于能在浏览器里高效跑 | [Juejin article](https://juejin.cn/post/7698926562423357450) |

**Needs.** K2, K3 plus size statistics; geometry counts usually need K15. **Difficulty.** Medium-hard. **Failure modes.** L3 (timeout or out-of-memory with no message); invents byte sizes per class (must say "estimated by instance count"); suggests deleting needed data; writes over the original while slimming (L19); loads the whole file when lazy loading exists.

### Family G. Ask about the process, the problem, or the assistant

#### G1 explain_howto: concepts and "how do I do X in my software"

**Definition.** No model needed: what is IFC, what is an MVD, how do I get shared parameters into the export, which translator for the structural engineer. A general-knowledge intent that the assistant should answer without calling model tools (and without pretending to have looked at a file).
**Share.** 0 of the file-task prompts by definition; 544 records (15.1%) overall, in the real data usually long-form questions to humans. Synthetic how-to prompts (140, `needs_file: false`) are the best phrasing sample.
**Sub-intents.** (a) concepts for beginners; (b) software settings ("export Revit parameters as properties"); (c) workflow advice (IFC and native files for public tenders); (d) standards and national rules; (e) opinion ("is it worth delivering only IFC?").

| Id | Lang | Lbl | Request | Gloss / why it is a good test |
|---|---|---|---|---|
| ru-dwg-revit-s008 | ru | S | `как сделать чтоб мои параметры семейства уехали в ифс? галка экспорт параметров ревита вроде стоит а пусто` | Revit parameter export; "the tick is on but empty" |
| de-arch-s009 | de | S | `welchen Uebersetzer nehm ich fuer den Statiker mit Revit? Tragende Bauteile muessen als Struktur erkannt werden` | Which translator for the structural engineer |
| en-gh-revit-ifc-s014 | en | S | `how do i get Revit Category into my user defined pset txt file` | Mapping file question |
| en-stackoverflow-s009 | en | S | `export the current revit view to ifc4 with base quantities on, api call not the dialog` | API-level how-to |
| es-latam-s016 | es | S | `en las licitaciones públicas piden ifc y nativo, vale la pena entregar solo ifc?` | Opinion |
| ru-autodesk-telegram-r015 | ru | R | что такое IFC вообще | [Habr 460719](https://habr.com/ru/post/460719/) |
| it-italy-r003 | it | R | come carico il file di mappatura classi IFC in Revit prima di aprire l'IFC | [Biblus](https://biblus.acca.it/ifc-class-mapping-file/) |
| en-aimcp-r022 | en | R | `Could you please provide a simple tutorial?` (assuming users are not familiar with MCP) | [revit-mcp-plugin issue 5](https://github.com/mcp-servers-for-revit/revit-mcp-plugin/issues/5) |
| ko-korea-r001 | ko | R | IFC와 openBIM이 뭐고 왜 국제표준을 도입해야 하나 | [buildingSMART Korea](https://www.buildingsmart.or.kr/Home/BimOverview) |

**Needs.** None (knowledge), optionally the [KB](../01_ifc_basics/) or docs. **Difficulty.** Easy for facts, hard for software-version-specific steps. **Failure modes.** Calls a model tool for a concept question; answers about the user's file without loading it; outdated menu names (Revit year differences); confident claims about IFC4 vs IFC2x3 without checking the version; answers in English to a Russian question.

#### G2 troubleshoot_diagnose: "something went wrong, find out why"

**Definition.** The user reports a symptom after export, import or viewing and asks the assistant to look into the file to find the cause: elements missing, colours lost, doors invisible, storeys doubled, viewer refuses to open, shared parameters not in Psets, coordinates far away.
**Share.** 34 (3.2%) as file-based diagnosis; **1,110 records (30.9%)** overall, the largest group of real questions. Personas: bim_coordinator (12), architect (10), developer (7).
**Sub-intents.** (a) export-side loss ("half my elements are missing, compare to the Revit source"); (b) import-side problems (windows outside walls, openings not cutting); (c) viewer problems (nothing visible, mesh type errors); (d) parameter/property loss; (e) tool errors (IfcConvert crash on accents, ETABS rejects file, `ENDSEC` missing); (f) **connection problems of the MCP server itself** (see G3).

| Id | Lang | Lbl | Request | Gloss / why it is a good test |
|---|---|---|---|---|
| ja-japan-s003 | ja | S | `IFCに出したら半分くらい要素が無い…Revitの元モデルと比べて何が落ちてるか調べて。階に紐づいてないやつとか` | Half the elements are gone; check what dropped, e.g. unlinked to storeys |
| ru-habr-dev-s011 | ru | S | `в ифс не выгрузились зоны, хотя в ревите площадь есть. проверь IfcSpace и скажи что не так` | Zones missing though Revit shows areas |
| en-psets-s009 | en | S | `I added shared params to the doors family, they are in the Revit schedule but not in the ifc. check what psets doors actually have` | Look at actual Psets |
| zh-zhihu-s014 | zh | S | `tekla的ifc在viewer里正常，revit里3D视图啥也没有，查下是不是几何有问题` | Fine in viewer, empty in Revit |
| es-vm-s008 | es | S | `el ifc que saque de revit no abre en etabs, dice que falta ENDSEC. que version es y esta truncado?` | Truncated file check |
| it-geom-s015 | it | S | `nel modello IFC mancano i parapetti delle scale, controlli quali IfcStair non hanno IfcRailing?` | Specific missing relation |
| no-norway-s004 | no | S | `etasjene blir dobbelt i IFC etter eksport fra Revit, noen ide? sjekk modellen` | Duplicated storeys |
| pt-err-s008 | pt | S | `exportei pro IFC e sumiu um monte de elemento, da pra ver o que ficou de fora e porque?` | What was left out and why |
| fr-err-s010 | fr | S | `IfcConvert plante avec 'to_bytes error', y'a des accents dans le header, tu peux corriger le fichier ?` | Header encoding crash |
| p-student-s010 | ru | S | `почему после экспорта у меня всё стало IfcBuildingElementProxy?? препод сказал так не должно быть` | Beginner, no file needed (G1/G2 boundary) |
| en-aimcp-r013 | en | R | IFC made with an LLM cannot be opened: `IfcProject` has 8 attributes instead of 9 | [IfcOpenShell issue 7945](https://github.com/IfcOpenShell/IfcOpenShell/issues/7945) |
| ru-habr-dev-r012 | ru | R | косоуры лестниц и дубли кода МССК у пандусов: как чистить после экспорта | [Habr 1087472](https://habr.com/ru/articles/1087472/) |
| es-spain-r001 | es | R | al abrir el IFC y guardarlo en otro formato se pierden las coordenadas | [Autodesk forum](https://forums.autodesk.com/t5/revit-architecture-forum/problemas-con-ifc-s/td-p/10189111) |

**Needs.** Whatever the cause demands: K2/K3/K4 for loss, K6 for position, K7 for syntax. **Difficulty.** Medium-hard (hard 13 of 34). **Failure modes.** Guesses the cause without inspecting the file; stops at the first hypothesis; blames the user; suggests fixes that are specific to a different software version; gives a causal explanation the tool results do not support (state "likely" vs "found").

#### G3 tool_meta: "what can you do / how do I connect / which tool"

**Definition.** Questions about the assistant or its server: what tools are available, can it edit or only read, how to connect Claude/Cursor/a local model, why the connection fails, request for a missing tool, which external program to pick.
**Share.** 0 of file tasks; 327 records (9.1%) overall (raw `find_tool`, `request_feature`, `viewers_opening`). Of these, real MCP issues are a distinct cluster: **setup/connection failures dominate the AI cell** ([ai-mcp-usage](../research_raw/wave1/ai/ai-mcp-usage.md)).
**Sub-intents.** (a) capability probe ("can you actually edit this or just read it?"); (b) setup help (ports 8080/8964, plugin not loading, `Method not found`, Revit year support); (c) which LLM/client works (Mistral, Llama, Cursor, ChatGPT desktop); (d) feature requests ("add a screenshot tool", "config file for the port"); (e) tool-quality complaints (empty tool descriptions); (f) software choice (viewer, converter), usually out of scope for a model-bound server.

| Id | Lang | Lbl | Request | Gloss / why it is a good test |
|---|---|---|---|---|
| en-osarch-s017 | en | S | `can you actually edit this ifc or just read it? add a pset Pset_Custom to all IfcDoor and save` | Capability probe combined with a write task |
| en-aimcp-s017 | en | S | `can claude open ifc files directly or do i need an mcp server? which one for beginners` | Beginner MCP question |
| en-gh-ifcopenshell-s015 | en | S | `can i point claude at my ifc to edit it, whats the setup` | Setup |
| en-revit-auto-s006 | en | S | `claude sees the revit mcp tools but every call says Method not found, revit 2026, what am I missing` | Real-looking connection failure |
| ru-aimcp-s012 | ru | S | `клод пишет не могу подключиться к ревиту, плагин вроде стоит, что проверить` | Russian version |
| zh-aimcp-s009 | zh | S | `cursor里mcp是绿的但revit没反应，8964端口被占了？怎么查` | Green in Cursor, no reaction in Revit; port occupied |
| en-revit-auto-s017 | en | S | `whats the cheapest way to get an AI to do repetitive revit stuff, sheets/views/params? local model ok?` | Cost and local model |
| en-aimcp-r021 | en | R | `How Can i connect mistral or Llama with the revit MCP` | [revit-mcp issue 26](https://github.com/mcp-servers-for-revit/revit-mcp/issues/26): one-line beginner |
| zh-aimcp-r024 | zh | R | 如何和cursor对接 | [ZedMoster/revit-mcp issue 1](https://github.com/ZedMoster/revit-mcp/issues/1) |
| en-aimcp-r014 | en | R | 23 of 25 tools expose an empty description over MCP | [IfcOpenShell issue 8951](https://github.com/IfcOpenShell/IfcOpenShell/issues/8951) |
| en-aimcp-r001 | en | R | port 8080 is hardcoded and the plugin must be started manually after restarting Revit | [mcp-servers-for-revit issue 63](https://github.com/mcp-servers-for-revit/mcp-servers-for-revit/issues/63) |
| en-revit-auto-r022 | en | R | connected Claude to pyRevit MCP; wants a free agent; tried Gemini API and local Ollama, did not work | [pyRevit forum](https://discourse.pyrevitlabs.io/t/connecting-agent-to-pyrevit-mcp-newbie/10627) |

**Needs.** The server's own tool list (G3a); nothing for G3b-f. **Difficulty.** Easy for capability questions, medium for diagnosis. **Failure modes.** Over-promising ("I can run clash detection" without the tool); not listing real tool names; confusing the MCP server, the plugin, and the client; telling the user to reinstall in a loop; answering a connection problem as if it were a data problem (L1, L2, L4).

---

## 4. Using the taxonomy to build a test set

### 4.1 Suggested mix (recommendation, not measured data)

The corpus mirrors forum behaviour, so do not copy its shares one to one. Keep the read-heavy backbone, then oversample what real MCP issues show goes wrong.

| Block | Intents | Suggested share of a test batch | Why |
|---|---|---|---|
| Core reads (ground truth is computable) | A2, A3, A4, B1, C1 | 35% | The honest-baseline tasks; truth from an IfcOpenShell script |
| Reads that need a rare capability | A5, C2, C3, D1, F3 | 20% | Many servers lack the tool; tests honest refusal and real capability |
| Writes (on a copy) | E1, E2, E3 | 15% | Real issues are mostly writes; failure modes are the most harmful |
| Deliverables and convert | B2, F1, D2 | 10% | End-to-end flow; file output claims |
| Hardest judgment | C4, A1 for beginners, G2 | 10% | Abstention, plain-language summary, diagnosis honesty |
| Meta and knowledge | G1, G3, F2 | 10% | Routing (no model tool needed), self-description, vision |

### 4.2 Compound requests actually found

| Pattern | Example id | Intents |
|---|---|---|
| Find then export | `de-data-s012` (walls without fire rating, CSV with GUID and storey) | C1 + B2 |
| Count then fix | `ru-proxy-s001` count proxies "надо понять что перемапить"; follow-up `ru-autodesk-telegram-s009` reclass | A2/C3 then E1 |
| Check then report to someone | `en-fmor-s003` (fail list to send back to the contractor, grouped by discipline) | C2 + B2 |
| Diff then drill down | `it-proxy-s010` (compare v1/v2, how many proxies remain and which were reclassified) | D1 + C3 |
| Georef pre-flight before convert | `en-viewconv-s006` (check units and `IfcMapConversion` before QGIS) | A5 + F1 |
| Propose then apply | `ja-aimcp-s014` (list empty room names, propose changes, then apply) | C1 + E3 |
| Check, deliver, with urgency | `zh-lightweight-review-s001` (will it pass the Shenzhen self-check; base point; empty properties) | A5 + C1 + C4 |

### 4.3 Language and persona coverage hints

- Russian: the strongest slang cluster ("проксей", "психеты", "бцф", "ВОР", "ТЭП", "КР", "экспертиза", "до сдачи"). Typical form: imperative, no punctuation, sometimes "глянь" ([jargon dictionary](../06_how_people_write/jargon_slang_dictionary.md), [style guide](../06_how_people_write/style_guide.md)). All Russian MCP-style prompts in the corpus are synthetic.
- Chinese: "报建", "翻模", "轻量化", "钢筋", "项目基点"; Taiwan prompts use Traditional characters and often cite mm units and Revit levels like "2F".
- Spanish: voseo in Rioplatense prompts ("creá", "contame"); Spain vs LatAm vocabulary (`mediciones` vs `metrados`).
- German/Nordic: compound nouns and discipline abbreviations (TGA, RIV/RIB, MMI, FDV), regulations by name (TEK17, DIN 276).
- Japanese: polite request forms for managers ("〜してほしいです"), terse imperatives for developers; law-aware vocabulary (確認申請).
- English: shortest and most casual; lowercase, "pls", "u", abbreviations "coord", "struct", "arch".
- Beginners (student_beginner, 2% of model_task): A1, A2, A3 with confusion ("what even is in it?"); expects explanation, not tables.
- Reviewers/authorities: C4 and C2, polite, always about "what is missing before submission".
- Anti-patterns to avoid when writing tests (too clean, too textbook): see [anti-patterns of LLM-written questions](../06_how_people_write/anti_patterns_llm_questions.md).

### 4.4 Grading hooks per family

| Family | What a correct answer must contain | Ground truth source |
|---|---|---|
| A | Exact counts/values consistent with tool results; units; scope (whole model or storey) | IfcOpenShell script on a public sample file ([sample IFC files](../04_open_source/sample_ifc_files.md)) |
| B | Quantity source named (Qto vs geometry), openings handling, totals that add up | Same script; compare with the file's own `Qto_*` |
| C | PASS / FAIL / UNKNOWN separated; GlobalIds; no claim of official approval | Script with explicit rules; IDS reference run |
| D | Matching rule stated (GUID or type+position); added/removed/changed counts | Script on two sample revisions |
| E | Preview, read-back, original preserved, count of changes | Re-open the saved file and diff |
| F | A file or image actually produced; losses listed; units kept | File exists, opens, checksum |
| G | Correct routing (knowledge vs model tool vs self-description); honest uncertainty | Rubric review ([companion section 7](what_ifc_mcp_servers_do.md#7-how-to-judge-an-answer-short-rubric)) |

---

## 5. Gaps and honest caveats

- **No logs of real assistant sessions.** Shares for model_task are synthetic; "all records" shares are dominated by forum questions to humans. Neither equals the distribution of what people type to an MCP assistant.
- **Keyword triage, one primary intent per record, ±3 points.** Intent definitions here (22) are finer than the corpus vocabulary (21 intents, some for troubleshooting only).
- **F2, E2, E3, A1 and G3 rely on README prompts and issues** (real but not typed-by-user chat), and on three compiler-written drafts marked **D**. They should be treated as style samples.
- **Russian and other non-English MCP prompts are synthetic**: modeled on English and Chinese patterns (ai-mcp-usage report, gaps section).
- **Difficulty labels are agent opinions.**
- Not covered by intents because the data do not show them: multi-turn memory ("what we agreed last week", see [companion L-list](what_ifc_mcp_servers_do.md#43-unrealistic-or-must-be-refused--caveated-high-value-probes)), cost/time estimation (4D/5D scheduling appears in 68 records but as linking tasks inside A/B), generating design alternatives, and code generation for the user (programming intents are 176 `troubleshoot_code` records, a different use of the assistant: writing IfcOpenShell scripts, not operating on the model).

## 6. Related files

- [what_ifc_mcp_servers_do.md](what_ifc_mcp_servers_do.md): capability codes K1-K15, server groups, weaknesses L1-L25, judging rubric.
- [MCP servers and AI tools catalog](../04_open_source/mcp_servers_and_ai_tools.md) and [LLM + BIM research](../04_open_source/llm_bim_research_and_datasets.md): where the servers and benchmark categories come from.
- Questions by topic: [properties and parameters](../05_real_world_questions/by_topic/properties_and_parameters.md), [quantities and cost](../05_real_world_questions/by_topic/quantities_cost_schedule.md), [validation and IDS](../05_real_world_questions/by_topic/validation_ids_model_checking.md), [coordination, clash and BCF](../05_real_world_questions/by_topic/coordination_clash_bcf_cde.md), [coordinates and georef](../05_real_world_questions/by_topic/coordinates_georef_units_levels.md), [file size, viewing and conversion](../05_real_world_questions/by_topic/file_size_viewing_conversion.md), [AI, beginners and software choice](../05_real_world_questions/by_topic/ai_beginners_software_choice.md).
- How people write: [style guide](../06_how_people_write/style_guide.md), [jargon and slang](../06_how_people_write/jargon_slang_dictionary.md).
