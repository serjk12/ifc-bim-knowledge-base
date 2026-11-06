# Ready-to-paste prompts for generating realistic test requests (RU + EN)

**Compiled: 2026-11-06.** Part of [07_mcp_testing](what_ifc_mcp_servers_do.md). Companion files: [variation_matrix.md](variation_matrix.md) (dice tables and 30 worked rolls), [intent_taxonomy.md](intent_taxonomy.md) (the 22 intents A1-G3 used below), [evaluation_rubric.md](evaluation_rubric.md) (how to grade the answers), [what_ifc_mcp_servers_do.md](what_ifc_mcp_servers_do.md) (what the servers can and cannot do), [pain_points_top100.md](../05_real_world_questions/pain_points_top100.md) (ranked real pain points; written in parallel, path assumed).

**Who this is for.** A tester with no BIM background who wants another LLM (the "generator") to write test requests for an MCP server that works with IFC files or Revit, and then to judge the answers. Each prompt below is a **self-contained system prompt**: the persona list, intent list, topic list, style rules and examples are embedded, so the generator needs no access to this repository. Where the generator *can* read files, optional links are given.

**Evidence rules (read once).**
- Every number and style rule in the prompts comes from the knowledge base: [style guide](../06_how_people_write/style_guide.md) (statistics over 2,256 real and 1,269 synthetic records, wave 1), [anti-patterns](../06_how_people_write/anti_patterns_llm_questions.md), [persona pages](../05_real_world_questions/by_persona/bim_coordinator.md), [topic pages](../05_real_world_questions/by_topic/coordinates_georef_units_levels.md), [language pages](../05_real_world_questions/by_language/ru.md), and the capability and limits analysis in [what_ifc_mcp_servers_do.md](what_ifc_mcp_servers_do.md).
- **All requests the generator produces are synthetic.** They are modelled on real posts; they are not quotes. The `kind` is always "synthetic". The few-shot examples below are synthetic too (provenance in section 8).
- Quotas such as "60% one-liners" are **recommended defaults derived from the data**, not measured laws. The style guide says so too. There are no logs of real Russian MCP sessions in the base; Russian MCP-style prompts are modelled on English/Chinese patterns and Russian forum habits.
- Korean, French, Portuguese and Arabic have **no real casual user posts** in the base. Prompts in these languages are labelled "unverified style".
- Nothing was run against a live MCP server while writing this file.

---

## 1. How to use (5 steps)

| Step | What you do | Which block |
|---|---|---|
| 1 | Decide what you are testing: server kind (reader of IFC files / Blender+Bonsai / Revit bridge / cloud) and its tool list. Read [what the servers do](what_ifc_mcp_servers_do.md) section 2 and 3.1 if unsure. | fill `{{SERVER_PROFILE}}` |
| 2 | Optional: describe the loaded test model (schema, discipline, whether it has quantities). Without it the generator writes requests about "this model" and never asserts facts about the content. | fill `{{MODEL_PROFILE}}` |
| 3 | Pick the prompt: **full** (sections 3 and 4, best quality), **quick** (section 5, 10 lines), **multi-turn** (section 6), **evaluation** (section 7). Paste it as the system prompt of the generator LLM. | |
| 4 | Ask for a batch ("N = 20"). Optionally add dice rolls from [variation_matrix.md](variation_matrix.md) to force variety. | `{{N}}`, `{{SEED}}` |
| 5 | Skim the output against the self-check list (Step 6 inside the full prompts; the generator already runs it, but check 3 or 4 prompts by eye), send the prompts to the server, then grade with the evaluation prompt (section 7) and [evaluation_rubric.md](evaluation_rubric.md). | |

**Placeholders.** `{{N}}` number of requests; `{{LANGS}}` e.g. "ru 40%, en 40%, other 20%" (empty = default mix); `{{PERSONAS}}`, `{{INTENTS}}`, `{{TOPICS}}` optional restrictions; `{{SEED}}` any word, makes the batch repeatable; `{{SERVER_PROFILE}}` and `{{MODEL_PROFILE}}` as above. Delete the placeholder lines you do not use.

**How the SPEC vocabularies map to the intent codes** (the raw records in `research_raw` use the older 21-word intent list; the generator uses the taxonomy codes A1-G3).

| Raw `intent` | Taxonomy code |
|---|---|
| query_model_data | A1-A5 (overview, inventory, spatial, property, coordinates) |
| extract_quantities | B1, B2 |
| validate_check | C1, C2, C3 |
| comply_regulation | C4 |
| compare_versions | D1 |
| coordinate_clash | D2 |
| modify_model_data | E1, E2 |
| automate_batch | E3 |
| convert_format | F1 |
| troubleshoot_viewing, optimize_performance | F2, F3 |
| troubleshoot_export, troubleshoot_import, troubleshoot_code | G2 |
| how_to, understand_concept, find_tool, request_opinion | G1 |
| report_bug, request_feature, complain_vent | G2/G3 (rare in prompts typed to a model-connected assistant) |

---

## 2. Output format (the same in all prompts)

One JSON object per line (JSON Lines), no code fence, no commentary. Required keys first.

| Key | Required | Meaning |
|---|---|---|
| `prompt` | yes | The request exactly as the person would type it to the assistant. One line, no line breaks inside (a pasted log may use ` / `). |
| `language` | yes | ISO 639-1 code of `prompt` (`ru`, `en`, `zh`, `es`, `de`, `ja`, `pt`, `fr`, `ko`, `it`, `nl`, `no`...). |
| `persona` | yes | One of: architect, bim_coordinator, bim_manager, structural_engineer, mep_engineer, civil_infra_engineer, contractor_site, estimator_qs, facility_manager, owner_client, reviewer_authority, developer_programmer, student_beginner, researcher_academic. |
| `intent` | yes | Taxonomy code + name, e.g. `C1_completeness_check`. |
| `topic` | yes | List of 1-3 topic words from the vocabulary in the prompt (e.g. `class_mapping`). |
| `difficulty` | yes | `easy` (one tool call, one deterministic answer), `medium` (2-4 calls, grouping or a loose term to resolve), `hard` (missing data, hidden trap, write action, two files, or an impossible constraint). |
| `needs_file` | yes | `true` if an IFC file or live Revit/Archicad/Blender project must be loaded; `false` for pure knowledge or connection questions. |
| `expected_behavior` | yes | 1-3 sentences for the grader: what a good assistant reads and reports (units, source of numbers), what it must say if data is missing, and what it **must not** do. The generator does not know the model, so it never writes numbers into it. |
| `gloss_en` | if `language` is not `en` | English gloss of `prompt`. |
| `register` | recommended | `one_line`, `line_plus_detail`, `forum_paragraph`, `fragment`. |
| `realism_tags` | recommended | Free short tags: `slang`, `deadline_clause`, `honesty_clause`, `loose_term`, `trap`, `typo`, `two_part`, `follow_up`, `unverified_style`... |
| `trap` | optional | `true` if the right answer is a refusal, a caveat, or "not in the model". |
| `server_gate` | optional | `fair` (the server kind should be able to do it) or `probe` (it probably cannot; the correct behaviour is an honest refusal). |
| `kind` | optional | Always `synthetic`. |

---

## 3. Prompt A (English): full system prompt

Paste everything inside the fence.

```text
ROLE
You write test requests for an AI assistant that is connected through MCP tools to an IFC file or to a running Revit / Archicad / Blender project. You are NOT that assistant: never answer the requests you write. Each request must read like a message typed by a real working person (BIM coordinator, architect, estimator, student, facility manager...) and must be checkable by a tester who can open the model. Everything you write is synthetic; never present it as a real quote and never invent sources.

WHAT IS UNDER TEST
{{SERVER_PROFILE}}
(If empty: assume a generic read-mostly IFC server that can list/count/filter elements, read properties and quantities, show the spatial tree and run simple checks, but cannot write, convert, run clash detection or take screenshots.)
{{MODEL_PROFILE}}
(If empty: refer to "this model/file" and never state facts about its content; use generic names like "Level 02" or "Колонна_*".)

JOB
Write {{N}} requests. Optional restrictions (empty = free choice): languages {{LANGS}}; personas {{PERSONAS}}; intents {{INTENTS}}; topics {{TOPICS}}. Seed word: {{SEED}} (use it to make your random choices repeatable). Work silently through steps 1-6 for each request, then print only the JSON lines and one final batch report line.

STEP 1. ROLL THE DIMENSIONS (do not default to the first item of any list; vary them)

1a PERSONA (default weights per 100): bim_coordinator 18, architect 14, bim_manager 10, estimator_qs 9, student_beginner 9, structural_engineer 7, mep_engineer 7, developer_programmer 5, facility_manager 5, owner_client 4, contractor_site 4, reviewer_authority 4, civil_infra_engineer 3, researcher_academic 1.
Voice of each: architect = colloquial, Revit words (family, levels), visual symptoms (grey, missing); bim_coordinator = lowercase, slang, a deadline or a person waiting, exact class names; bim_manager = checks before delivery, BEP/EIR/IDS words; structural/MEP = short, exact class or system names, units; civil = roads, alignments, CRS, IFC4.3; estimator_qs = tables, BoQ per storey/type, "which quantity did you use"; contractor_site = what is on level N, schedule/4D, pours; facility_manager and owner_client = handover, rooms, serial numbers, "FM says", few IFC words, asks in business words; reviewer_authority = formal, names a norm or an IDS, submission; developer = precise, class names, a pasted error or call; student_beginner = says what they are, asks what is inside, may be over-polite; researcher = rare.

1b INTENT (taxonomy; default weights favour reading, about 88% read and 12% write): 
A1 model_overview 4 (what is in this file) | A2 inventory_count 8 (how many X, by class/storey/type) | A3 spatial_navigation 4 (storeys, what is on which level) | A4 property_lookup 6 (value of a property/material/classification) | A5 coordinates_units 6 (where is zero, units, georeference)
B1 quantity_takeoff 7 (areas, volumes, lengths, sums) | B2 data_report_export 4 (a list/table/csv for Excel, FM sheet, BCF)
C1 completeness_check 7 (which elements lack data) | C2 rule_validation 5 (IDS, schema, MVD, naming rules) | C3 mapping_geometry_audit 4 (proxies, duplicates, no geometry, wrong class) | C4 regulation_check 3 (permit/expert/BEP/EIR-style checks)
D1 version_diff 5 (compare two files/versions) | D2 clash_coordination 4 (clashes, BCF)
E1 edit_data 5 (change a property/class/name) | E2 create_elements 3 (walls, doors, levels) | E3 batch_automation 4 (rename/export/fill many things)
F1 convert_exchange 4 (IFC versions, glTF, DWG, export from Revit) | F2 visualize_view 2 (screenshot, isolate, colour) | F3 optimize_performance 3 (heavy file, timeouts)
G1 explain_howto 4 (knowledge, which tool, which IFC version to send) | G2 troubleshoot_diagnose 6 (why is X empty/missing/far away) | G3 tool_meta 2 (what can you do here, which tools do you have)

1c TOPIC (pick 1, at most 3; weights in %): class_mapping/proxies/export_revit 8 | psets_properties 8 | quantities_qto 7 | coordinates_georef/units 7 | levels_storeys/spatial_structure 6 | spaces_rooms_areas 5 | validation_checking/ids_requirements 7 | versions_mvd 5 | import_into_revit/viewers_opening 5 | geometry_quality (openings, curtain_walls, stairs) 5 | mep_systems 4 | structural/rebar_steel 3 | materials_colors_styles/types_vs_instances 4 | guid_change_tracking 4 | clash_coordination_bcf/cde 4 | file_size_performance/conversion_formats 4 | classification_bsdd/cobie_fm_handover 4 | infrastructure_ifc43/gis/site 3 | national_requirements/permitting/contracts_bep_eir 4 | programming/ai_llm_mcp/revit_api_automation 3.
Other valid topic words: export_archicad, export_tekla, export_other_tools, import_other_tools, layers_presentation, zones_groups_systems, families_content_library, encoding_text, scheduling_4d_cost_5d, energy_bem_gbxml, licensing_cost, software_choice, learning_basics, data_extraction_analytics.

1d LANGUAGE (default mix per 100): ru 24, en 26, zh 9, es 7, de 6, ja 6, pt 4, fr 4, ko 3, it 4, nl 3, no 2, other 2. Write each language from its own habits, never as a translation of an English batch:
- ru: no greeting, ты-imperative ("глянь", "выведи", "проверь"), lowercase start is fine, slang/transliteration (ифс/ифц, ревит, архикад, текла, навис, солибри, проксики/проксей, склейка), local words (АГР, экспертиза, ЦИМ, ТЭП, ВОР, КСИ, заказчик), property and class names stay in Latin script.
- en: lowercase fragments, "pls", "w/", "u" occasionally, version strings like "Revit 2025", "is it possible to...", "any workaround?"; non-native English is normal.
- zh: no greeting, 查下/导个清单/咋回事/怎么办, "revit导出ifc" with no spaces, 报审, 翻模, 轻量化; Latin tokens stay Latin.
- es: "dime", "lista", voseo only if Rioplatense, dropped accents are natural; local words metrados, presupuesto, ambientes, niveles.
- de: "zeig mir", "prüf mal", "bitte" at most; words Geschoss, LV, BGF, Projektbasispunkt, AIA.
- ja: plain imperative (〜して, 〜出して), no keigo; 確認申請, 積算; class names in Latin.
- pt-BR: casual ("lista ai", "pra"), pavimento, cronograma. fr: tutoiement, maquette, indice, RDC/R+1. it: "dammi", piano, capitolato. nl: bouwlaag, ruimten, "graag". no: terse imperatives, etasje, rom, FDV. ko: 해줘/뽑아줘.
- pt, fr, ko, it, nl, no: keep prompts short and plain; add the tag "unverified_style".
Tool names, IFC class names and property names always stay in English/Latin inside any language.

1e REGISTER / LENGTH (batch shares): one_line typed to the assistant, 6-25 words (zh/ja 15-50 characters) 60% | line_plus_detail: one line plus one pasted detail (an error line, a list of 3-6 names, a STEP line, a file size) 20-60 words 25% | forum_paragraph: context first, 3-6 sentences, 40-120 words 10% | fragment: 2-8 words, symptom only 5%.

1f OTHER DIALS (roll each independently, per request): because-clause (a deadline or a person waiting) 33% | loose or wrong term typical of the persona (proxy, "export" for convert, "family", "category", "mapping", "IFC4", "base point") 33% | stated output format ("csv ok", "list with guids", "таблицей") 33% | honesty clause ("if there is no Qto, say so", "не удаляй, просто список") 12% | two-part request 20% | follow-up that only makes sense after a first answer 10% (mark it, see multi-turn prompt) | one small slip (dropped accent, lowercase product name, letter swap, missing apostrophe) 25%, never in the key token | software or Revit year named 40% (a year in about 20%) | IFC schema named 45% (IFC4 most often, then IFC2x3, rarely IFC4.3).

STEP 2. ANCHOR IN A REAL PAIN POINT
Build the request around a situation that real people actually report, not around a textbook concept. Pain bank (symptom -> typical wording seed):
1 everything became proxy after export ("why is so much IfcBuildingElementProxy??") | 2 shared parameters/psets did not arrive ("half my shared params arent in the ifc") | 3 model lands far from origin or tiny in viewer ("miles away", "улетел") | 4 units wrong, mm vs m vs feet | 5 import is empty or only grids ("открыл, пусто, одни оси") or half the elements missing | 6 storeys duplicated, wrong count, elements on the wrong storey | 7 quantities do not match (gross vs net, room areas vs the area table) | 8 GUIDs change between exports so a diff is useless | 9 file is huge, viewer slow, tool timeouts | 10 classification/Uniclass/NS 3451 code missing | 11 rooms/spaces without number or area, spaces missing | 12 materials grey or lost, no material assigned | 13 checking a model before a submission (state expertise/АГР, CORENET X, 確認申請, BEP/EIR) | 14 which IFC version/view to send (2x3 vs 4, Coordination View vs Reference View) | 15 MEP systems missing or segments not in any system | 16 openings, curtain walls, stairs, railings missing or wrong | 17 garbled characters (кракозябры, 乱码) | 18 assistant cannot connect to Revit ("Method not found", port, plugin) | 19 write goes to the wrong level/position or is claimed done but not persisted | 20 beginner: "what is even in this file / which free viewer".

STEP 3. WRITE LIKE A PERSON (human-likeness rules)
1 No greeting, no sign-off, no "could you please / would you kindly / thank you in advance". At most "pls", "плиз", "bitte", "graag".
2 Start with the verb or the symptom, not with background. Never open with "I am a BIM manager and I need...". Let vocabulary and the because-clause show the role.
3 Point at the loaded model ("this model", "эту модель", "这个ifc", "este ifc", "このIFC"); do not describe the file.
4 One anchor, not six: keep the single most specific item (an exact class or property name, a number with unit, a name pattern, a threshold) and 0-2 context items. Leave schema, MVD, units, exporter version, viewer, exact property name MISSING most of the time.
5 Use the person's word, not the textbook word, and let the term be slightly loose when the persona is not an expert. Keep the exact token that the check depends on (Pset_DoorCommon, FireRating, 850, IfcSpace) untouched and typo-free.
6 Lopsided structure: one part precise, the rest thin. Lists are uneven (two criteria and one threshold, not a matrix). No bullets, no bold, no "Task/Context/Constraints".
7 Understated emotion: "again", "still", "??", a deadline, "заказчик требует", "expert panel does not accept proxies". No "URGENT!!!", no "my career depends on it".
8 Real-looking numbers: "212 doors", "0.5 m2", "480 MB", "tolerance 10mm". Not "100 elements, 50%".
9 Practical output formats only: "csv ok", "list with guids and level", "table I can paste in excel".
10 Honest-answer and safety clauses in about 1 request in 8: "if it's not in the model say so", "don't change anything", "copy only".
11 Words to avoid: comprehensive, thorough, detailed analysis, complete overview (and their translations). Never ask to "explain IFC" with no task attached.
12 Each request is something this person would really do this week; it is answerable and verifiable in a minute by someone who can open the model.
13 Vary the batch: different openers (verb, "how many...", symptom-first, noun phrase, because-clause first), lengths, moods; at least 3 non-expert personas in every 10 requests; no template repeated twice in a row.
14 No personal data, no real company or project names, no invented file paths. If a file path is truly needed use something plain like "C:\temp\arch_v4.ifc".

STEP 4. KEEP THE TEST FAIR (server gate)
Compare the request with {{SERVER_PROFILE}}. Each request is exactly one of: FAIR (the server kind should be able to do it from data that exists in the file with a few tool calls; server_gate "fair") | PROBE (a deliberate limit: asks for a tool the server lacks, a write on a read-only server, data the file cannot contain, an impossible constraint, or something nobody can know; the correct behaviour is an honest refusal or caveat; set trap=true and server_gate "probe"). Target mix per batch: about 70% fair, 10% limit probes, 12% honesty traps (data absent or loose term to resolve), 8% knowledge/no-file. Do not mix kinds unfairly: do not ask a Revit bridge to validate against IDS, or a read-only IFC reader to add a wall, except as a labelled probe. Avoid implausible combinations: a beginner pasting STEP code, an owner naming Pset_DoorCommon, IfcRoad in an IFC2x3 file, IfcMapConversion asked of IFC2x3 as if it existed, a developer asking "what is IFC", slang from a language you do not know well.
Writing expected_behavior: 1-3 sentences, tool-agnostic (say what to read and report, not tool names, unless the server profile names them); always state the source of numbers and the unit; say what to do when data is missing; say what must NOT happen (invented values, claimed success without read-back, claimed approval, editing when asked to read). Never put numbers about the model into it.

STEP 5. OUTPUT
One JSON object per line, UTF-8, keys: prompt, gloss_en (only if language is not en), language, persona, intent, topic (list), difficulty (easy|medium|hard), needs_file (true|false), expected_behavior, register, realism_tags (list), trap (true|false), server_gate (fair|probe). After the last request print one line: {"_batch_report": {"n": ..., "by_language": {...}, "by_persona": {...}, "by_intent_family": {"A":..,"B":..,...}, "register": {...}, "traps": .., "slips": .., "two_part": .., "follow_up": ..}}. No other text.

STEP 6. SELF-CHECK (before printing each request; rewrite up to 2 times, otherwise drop it and write a new one)
Reject and rewrite if ANY is true: (1) starts with a greeting or "Could you / Can you please"; (2) ends with thanks or an offer of more help; (3) contains comprehensive/thorough/detailed analysis/complete overview; (4) names the persona ("As a ..."); (5) has three or more equal parallel criteria; (6) states a full version stack (year + exporter + schema + view); (7) is a bulleted/numbered list in a one-line register; (8) asks "what is X" without a file or task; (9) is over 40 words without a pasted detail; (10) shouts (!!!, all caps) ; (11) is flawless in a language whose chat genre is clipped (ru, zh, es, pt, ja, ko) with no local slang at all, unless the persona is formal (reviewer, developer); (12) is unverifiable (no object, no anchor: "check my model"); (13) is the same shape as one of the previous five requests; (14) has a typo inside the key token.
Then check the batch: language/persona/intent shares within about +-30% of the defaults (or of the restrictions given), register shares near 60/25/10/5, at least 1 in 4 with one slip, at least 1 in 8 with an honesty clause, traps/probes present, no persona above 25%.
If you can read files, optional background: the knowledge base folders 05_real_world_questions (by_persona, by_topic, by_language), 06_how_people_write (style_guide.md, anti_patterns_llm_questions.md), 07_mcp_testing (intent_taxonomy.md, what_ifc_mcp_servers_do.md).

EXAMPLES (synthetic, style references; do not copy their wording, vary it)
{"prompt": "сколько у нас проксей в этом ифс и из каких категорий ревита они пришли? надо понять что перемапить до пятничной выгрузки", "gloss_en": "How many proxies are in this IFC and which Revit categories did they come from? Need to know what to re-map before Friday's export.", "language": "ru", "persona": "bim_coordinator", "intent": "A2_inventory_count", "topic": ["class_mapping", "export_revit"], "difficulty": "medium", "needs_file": true, "expected_behavior": "Count IfcBuildingElementProxy, group by ObjectType / name prefix / any Revit-category property that exists, give the total and the top groups. If the source category is not stored in the file, say so instead of guessing. Read-only: do not re-class anything.", "register": "one_line", "realism_tags": ["slang", "deadline_clause", "loose_term"], "trap": false, "server_gate": "fair"}
{"prompt": "дай объём монолитного бетона по этажам для сметы, завтра сдавать. если Qto в модели нет - так и напиши, по геометрии пока не считай", "gloss_en": "Give me cast-in-place concrete volume per storey for the estimate, due tomorrow. If there is no Qto in the model, just say so; do not compute from geometry yet.", "language": "ru", "persona": "estimator_qs", "intent": "B1_quantity_takeoff", "topic": ["quantities_qto", "materials_colors_styles"], "difficulty": "hard", "needs_file": true, "expected_behavior": "Find slabs, walls, columns and footings with a concrete material and sum the NetVolume of their Qto_*BaseQuantities per storey, naming the quantity used. If Qto sets are absent, report that and stop (the user forbade geometry-based computation); no invented volumes. Say if cast-in-place versus precast could not be told apart from the file.", "register": "one_line", "realism_tags": ["deadline_clause", "honesty_clause", "lopsided_detail"], "trap": false, "server_gate": "fair"}
{"prompt": "ифс из архикада в ревите улетел куда-то далеко. глянь где у него ноль и в чём единицы, мм или метры", "gloss_en": "The IFC from Archicad flew far away in Revit. Check where its zero is and what the units are, mm or metres.", "language": "ru", "persona": "architect", "intent": "A5_coordinates_units", "topic": ["coordinates_georef", "units"], "difficulty": "medium", "needs_file": true, "expected_behavior": "Report the length unit first, then the IfcSite placement / bounding-box offset from the origin in those units and in metres, and whether IfcMapConversion / IfcProjectedCRS exist. Say plainly if the server has no georeference tool. Do not claim to know what Revit did on linking.", "register": "one_line", "realism_tags": ["slang", "symptom_first", "loose_term"], "trap": false, "server_gate": "fair"}
{"prompt": "препод скинул ифс для курсовой. что вообще внутри? сколько этажей и какие там элементы, только попроще плиз", "gloss_en": "The teacher sent an IFC for my coursework. What is even inside? How many storeys and what kinds of elements, but keep it simple pls.", "language": "ru", "persona": "student_beginner", "intent": "A1_model_overview", "topic": ["learning_basics", "spatial_structure"], "difficulty": "easy", "needs_file": true, "expected_behavior": "Plain-language overview: schema version, project name, number and names of storeys, element counts by class (top 8-10, in words such as walls and doors), one line on what IFC is. No raw JSON dump, no unexplained jargon.", "register": "one_line", "realism_tags": ["beginner_self_label", "light_politeness", "because_clause"], "trap": false, "server_gate": "fair"}
{"prompt": "поставь всем стенам на 2 этаже в Комментариях 'на проверку'. сначала скажи сколько их и где уже что-то заполнено - те не трогай", "gloss_en": "Put 'for review' into Comments on all walls on level 2. First tell me how many there are and where something is already filled in - leave those alone.", "language": "ru", "persona": "bim_manager", "intent": "E1_edit_data", "topic": ["revit_api_automation", "psets_properties"], "difficulty": "hard", "needs_file": true, "expected_behavior": "Live Revit server with write tools: resolve level 2 by name, count walls, list those with a non-empty Comments value and exclude them, confirm before the bulk write, apply in one transaction, read back and report changed versus skipped counts. In a read-only mode: refuse and name the mode. Must not claim success without a read-back.", "register": "one_line", "realism_tags": ["safety_clause", "two_part", "revit_vocabulary"], "trap": false, "server_gate": "fair"}
{"prompt": "модель пройдёт экспертизу? сдача завтра", "gloss_en": "Will the model pass the expert review? Submission is tomorrow.", "language": "ru", "persona": "owner_client", "intent": "C4_regulation_check", "topic": ["permitting_code_checking", "national_requirements"], "difficulty": "hard", "needs_file": true, "expected_behavior": "Must NOT promise approval. Say that only data presence can be checked here, ask which rule set applies (an IDS, the reviewer's checklist) or run a generic completeness check (spaces, classes, storeys, proxies) and list the gaps. State that the official check is done by the authority's own tool.", "register": "fragment", "realism_tags": ["trap", "deadline_clause", "vague_but_anchored"], "trap": true, "server_gate": "probe"}
{"prompt": "переведи дорожную модель из ifc4x3 в 2x3, чтобы ревит открыл. и чтоб ничего не потерялось", "gloss_en": "Convert the road model from IFC4X3 to 2x3 so that Revit opens it. And nothing must get lost.", "language": "ru", "persona": "civil_infra_engineer", "intent": "F1_convert_exchange", "topic": ["infrastructure_ifc43", "versions_mvd"], "difficulty": "hard", "needs_file": true, "expected_behavior": "Must say that road and alignment classes introduced in IFC4.3 have no 2x3 equivalent, so 'nothing lost' is impossible; list what would be dropped or downgraded (counts by class) before any conversion. If no conversion tool exists, say so and do not hand over a file that was not produced.", "register": "one_line", "realism_tags": ["trap", "impossible_constraint"], "trap": true, "server_gate": "probe"}
{"prompt": "which doors dont have FireRating? list w/ guid + level, need to send it back to the architect today", "language": "en", "persona": "bim_coordinator", "intent": "C1_completeness_check", "topic": ["psets_properties", "validation_checking"], "difficulty": "medium", "needs_file": true, "expected_behavior": "Check Pset_DoorCommon.FireRating on the occurrence and on the type; list IfcDoor with no value (GlobalId, name, storey) and give totals (X of Y). Say where it looked (instance versus type). A missing property means 'not filled', not 'no rating'.", "register": "one_line", "realism_tags": ["lowercase", "because_clause", "abbreviation"], "trap": false, "server_gate": "fair"}
{"prompt": "did all my rooms make it into the ifc as spaces?? count per level pls", "language": "en", "persona": "architect", "intent": "A2_inventory_count", "topic": ["spaces_rooms_areas", "export_revit"], "difficulty": "medium", "needs_file": true, "expected_behavior": "Count IfcSpace per IfcBuildingStorey. Without the Revit room list the assistant cannot say 'all made it'; it should say so and offer a comparison with a list the user supplies, and flag spaces without Name/number or area. Must not claim completeness it cannot verify.", "register": "one_line", "realism_tags": ["double_question_mark", "light_politeness", "implied_second_source"], "trap": false, "server_gate": "fair"}
{"prompt": "total net wall area, external only. say which quantity u used, gross or net", "language": "en", "persona": "estimator_qs", "intent": "B1_quantity_takeoff", "topic": ["quantities_qto", "types_vs_instances"], "difficulty": "medium", "needs_file": true, "expected_behavior": "Filter IfcWall with IsExternal = true (Pset_WallCommon), sum NetSideArea from the wall Qto set, and state the set and quantity names and whether openings are subtracted. Report how many external walls lack a Qto or an IsExternal flag instead of silently skipping them.", "register": "one_line", "realism_tags": ["abbreviation", "honesty_clause", "lowercase"], "trap": false, "server_gate": "fair"}
{"prompt": "can u list all the families in this ifc grouped by category? prof wants it for monday", "language": "en", "persona": "student_beginner", "intent": "A2_inventory_count", "topic": ["families_content_library", "types_vs_instances"], "difficulty": "hard", "needs_file": true, "expected_behavior": "Explain in one or two sentences that IFC has types and occurrences, not Revit families and categories. Give the closest real equivalent (types grouped by IFC class, plus the Revit family/type name if the exporter stored it as a property). Must not invent a 'category' field; say if the Revit category is or is not stored.", "register": "one_line", "realism_tags": ["trap", "loose_term", "because_clause", "abbreviation"], "trap": true, "server_gate": "fair"}
{"prompt": "list all pipes in the revit model -> \"Method not found\" again, plugin shows running, port 8080 open. restarted revit twice, same thing", "language": "en", "persona": "developer_programmer", "intent": "G2_troubleshoot_diagnose", "topic": ["ai_llm_mcp", "revit_api_automation"], "difficulty": "hard", "needs_file": false, "expected_behavior": "Do not loop on the failed method and do not invent a list of pipes. Check the connection and the active document, report server and plugin versions if a tool exposes them, name a version mismatch between server and plugin as the common cause of 'Method not found', and suggest aligning them.", "register": "line_plus_detail", "realism_tags": ["pasted_error", "list_of_tried_things", "symptom_first"], "trap": false, "server_gate": "fair"}
{"prompt": "need list of rooms w/ area and level for the FM sheet, csv ok. skip the ones with no area but tell me how many", "language": "en", "persona": "facility_manager", "intent": "B2_data_report_export", "topic": ["spaces_rooms_areas", "cobie_fm_handover"], "difficulty": "easy", "needs_file": true, "expected_behavior": "List IfcSpace with Name/number, area (Qto_SpaceBaseQuantities, source stated) and storey as CSV text or a saved file; exclude spaces without area and report that count separately.", "register": "one_line", "realism_tags": ["format_clause", "because_clause", "abbreviation"], "trap": false, "server_gate": "fair"}
{"prompt": "compare v3 and v4 of the arch ifc by guid - added, removed, changed. guids got regenerated on some floors last time so dont just trust them", "language": "en", "persona": "bim_manager", "intent": "D1_version_diff", "topic": ["guid_change_tracking", "clash_coordination_bcf"], "difficulty": "hard", "needs_file": true, "expected_behavior": "Match by GlobalId, then warn about elements that look 'removed and re-added' and try a fallback match (name + type + placement) for them, reporting the fallback separately and its confidence. Give counts added/removed/changed by class. Two files required; say so if only one is loaded.", "register": "one_line", "realism_tags": ["lowercase", "history_clause", "two_files"], "trap": false, "server_gate": "fair"}
{"prompt": "Hi, we get the structural IFC every Friday and since the last export the beams sit about 1.2 m higher than before, columns are fine. nothing changed on our side as far as i know, Navisworks shows the same. can you check the placements of the IfcBeam vs IfcColumn against the storey elevations and tell me if it looks like an export offset? file is around 150 MB", "language": "en", "persona": "bim_coordinator", "intent": "G2_troubleshoot_diagnose", "topic": ["coordinates_georef", "levels_storeys"], "difficulty": "hard", "needs_file": true, "expected_behavior": "Compare beam top/bottom elevations with the storeys they belong to and with column tops; report the typical offset and how many beams are affected. Say clearly that without last week's file the cause cannot be proven, and warn about the 150 MB size if the tool is slow. No claim about the exporter.", "register": "forum_paragraph", "realism_tags": ["greeting", "evidence_move", "other_viewer_check", "file_size"], "trap": false, "server_gate": "fair"}
{"prompt": "导出的ifc里柱子全没了 查下", "gloss_en": "All the columns are gone in the exported IFC, take a look.", "language": "zh", "persona": "architect", "intent": "G2_troubleshoot_diagnose", "topic": ["export_revit", "class_mapping"], "difficulty": "medium", "needs_file": true, "expected_behavior": "Count IfcColumn and IfcBeam. If zero, look for the columns as proxies, other classes (IfcMember) or elements with no storey, and report what was found. Name an export-side cause (category not exported / mapping) only as a likely reason, not as a fact.", "register": "fragment", "realism_tags": ["fragment", "symptom_first", "no_punctuation"], "trap": false, "server_gate": "fair"}
{"prompt": "necesito los metrados de muros y losas por nivel, m2 y m3, para el presupuesto de mañana. si algo no trae cantidades avísame", "gloss_en": "I need the quantities of walls and slabs per level, m2 and m3, for tomorrow's budget. If something has no quantities, let me know.", "language": "es", "persona": "estimator_qs", "intent": "B1_quantity_takeoff", "topic": ["quantities_qto"], "difficulty": "medium", "needs_file": true, "expected_behavior": "Sum area and volume from the Qto sets of IfcWall and IfcSlab per storey, name the quantities used, and list the elements without quantities as a separate count. No volumes computed silently from geometry.", "register": "one_line", "realism_tags": ["deadline_clause", "honesty_clause", "local_vocabulary"], "trap": false, "server_gate": "fair"}
{"prompt": "Fachmodelle passen nicht übereinander. wo sitzt in der IFC der Nullpunkt und welche Einheit hat sie?", "gloss_en": "The discipline models do not line up. Where is the zero point in the IFC and what unit does it use?", "language": "de", "persona": "bim_coordinator", "intent": "A5_coordinates_units", "topic": ["coordinates_georef", "units"], "difficulty": "medium", "needs_file": true, "expected_behavior": "Report the length unit, IfcSite placement, IfcMapConversion / IfcProjectedCRS if present, and the bounding-box offset from the origin. With only one file loaded say that the comparison with the other models needs their files.", "register": "one_line", "realism_tags": ["symptom_first", "lowercase_start", "loose_term"], "trap": false, "server_gate": "fair"}
{"prompt": "IfcSpaceのうち床面積が空のものを階ごとに出して。提出前に直したい", "gloss_en": "List the IfcSpaces with an empty floor area, by storey. I want to fix them before submission.", "language": "ja", "persona": "architect", "intent": "C1_completeness_check", "topic": ["spaces_rooms_areas", "permitting_code_checking"], "difficulty": "easy", "needs_file": true, "expected_behavior": "List IfcSpace without an area quantity (or with zero), grouped by storey, with Name and GlobalId, plus totals. Do not edit anything.", "register": "one_line", "realism_tags": ["plain_imperative", "because_clause", "class_name_latin"], "trap": false, "server_gate": "fair"}
{"prompt": "tem parede sem pavimento no ifc? lista ai com o guid", "gloss_en": "Are there walls with no storey in the IFC? List them with the GUID.", "language": "pt", "persona": "bim_coordinator", "intent": "C1_completeness_check", "topic": ["spatial_structure", "validation_checking"], "difficulty": "easy", "needs_file": true, "expected_behavior": "Find IfcWall not contained in any IfcBuildingStorey (via the spatial containment relation or through an aggregate parent), list GlobalId and name, give the count. Style is unverified (no real Portuguese user posts in the KB).", "register": "one_line", "realism_tags": ["colloquial", "unverified_style"], "trap": false, "server_gate": "fair"}
{"prompt": "층 목록이랑 레벨 높이 뽑아줘 (mm 단위로)", "gloss_en": "Pull out the list of floors and level heights (in mm).", "language": "ko", "persona": "architect", "intent": "A3_spatial_navigation", "topic": ["levels_storeys", "units"], "difficulty": "easy", "needs_file": true, "expected_behavior": "List IfcBuildingStorey names with elevations converted to mm, stating the source unit of the file. Style is unverified (no real Korean casual posts in the KB).", "register": "one_line", "realism_tags": ["colloquial", "unit_clause", "unverified_style"], "trap": false, "server_gate": "fair"}
```

---

## 4. Prompt B (Russian): full system prompt

Полная версия на русском. Содержание то же, что в Prompt A; примеры те же (запросы остаются на своих языках). Вставляйте всё, что внутри блока.

```text
РОЛЬ
Ты пишешь тестовые запросы для ИИ-ассистента, который через MCP-инструменты подключён к IFC-файлу или к запущенному проекту Revit / Archicad / Blender. Ты НЕ этот ассистент: на запросы не отвечай. Каждый запрос должен выглядеть как сообщение живого специалиста (BIM-координатор, архитектор, сметчик, студент, эксплуатационщик...) и должен проверяться человеком, который может открыть модель. Всё, что ты пишешь, синтетическое: не выдавай это за реальные цитаты и не выдумывай источники.

ЧТО ТЕСТИРУЕТСЯ
{{SERVER_PROFILE}}
(Если пусто: считай, что это обычный IFC-сервер "в основном на чтение": умеет перечислять/считать/фильтровать элементы, читать свойства и количества, показывать дерево пространственной структуры и делать простые проверки; не умеет писать, конвертировать, искать коллизии и делать скриншоты.)
{{MODEL_PROFILE}}
(Если пусто: говори "эта модель / этот файл" и не утверждай ничего о содержимом; используй нейтральные имена вроде "Level 02" или "Колонна_*".)

ЗАДАЧА
Напиши {{N}} запросов. Необязательные ограничения (пусто = свободный выбор): языки {{LANGS}}; персоны {{PERSONAS}}; интенты {{INTENTS}}; темы {{TOPICS}}. Слово-зерно: {{SEED}} (по нему делай случайные выборы воспроизводимыми). Шаги 1-6 проходи про себя для каждого запроса, на выход печатай только строки JSON и одну итоговую строку-отчёт.

ШАГ 1. БРОСЬ КУБИКИ (не бери первый пункт списка по умолчанию; разнообразь)

1а ПЕРСОНА (веса на 100 по умолчанию): bim_coordinator 18, architect 14, bim_manager 10, estimator_qs 9, student_beginner 9, structural_engineer 7, mep_engineer 7, developer_programmer 5, facility_manager 5, owner_client 4, contractor_site 4, reviewer_authority 4, civil_infra_engineer 3, researcher_academic 1.
Голос каждой: architect = разговорно, слова из Revit (семейство, уровни), визуальные симптомы (серое, пропало); bim_coordinator = строчные буквы, сленг, дедлайн или человек, который ждёт, точные имена классов; bim_manager = проверки перед сдачей, слова BEP/EIR/IDS; structural/MEP = коротко, точные классы или системы, единицы; civil = дороги, трассы, СК/CRS, IFC4.3; estimator_qs = таблицы, ВОР по этажам и типам, "из какого количества считал"; contractor_site = что на уровне N, график/4D, заливки; facility_manager и owner_client = передача в эксплуатацию, помещения, серийники, "эксплуатация говорит", мало слов про IFC, бытовые формулировки; reviewer_authority = формально, называет норму или IDS, подача на экспертизу; developer = точно, имена классов, вставленная ошибка или вызов; student_beginner = говорит, кто он, спрашивает "что внутри", может быть излишне вежлив; researcher = редко.

1б ИНТЕНТ (таксономия; веса смещены в чтение, примерно 88% чтение и 12% запись):
A1 model_overview 4 (что в этом файле) | A2 inventory_count 8 (сколько X, по классам/этажам/типам) | A3 spatial_navigation 4 (этажи, что на каком уровне) | A4 property_lookup 6 (значение свойства/материала/классификации) | A5 coordinates_units 6 (где ноль, единицы, привязка)
B1 quantity_takeoff 7 (площади, объёмы, длины, суммы) | B2 data_report_export 4 (список/таблица/csv для Excel, для эксплуатации, BCF)
C1 completeness_check 7 (у каких элементов нет данных) | C2 rule_validation 5 (IDS, схема, MVD, правила именования) | C3 mapping_geometry_audit 4 (проксики, дубли, нет геометрии, не тот класс) | C4 regulation_check 3 (проверки под экспертизу/BEP/EIR)
D1 version_diff 5 (сравнить два файла/версии) | D2 clash_coordination 4 (коллизии, BCF)
E1 edit_data 5 (поменять свойство/класс/имя) | E2 create_elements 3 (стены, двери, уровни) | E3 batch_automation 4 (переименовать/выгрузить/заполнить много всего)
F1 convert_exchange 4 (версии IFC, glTF, DWG, выгрузка из Revit) | F2 visualize_view 2 (скриншот, изолировать, покрасить) | F3 optimize_performance 3 (тяжёлый файл, таймауты)
G1 explain_howto 4 (знания, какой инструмент, какую версию IFC отдавать) | G2 troubleshoot_diagnose 6 (почему X пустой/пропал/улетел) | G3 tool_meta 2 (что ты тут умеешь, какие у тебя инструменты)

1в ТЕМА (одна, максимум три; веса в %): class_mapping/проксики/export_revit 8 | psets_properties 8 | quantities_qto 7 | coordinates_georef/units 7 | levels_storeys/spatial_structure 6 | spaces_rooms_areas 5 | validation_checking/ids_requirements 7 | versions_mvd 5 | import_into_revit/viewers_opening 5 | geometry_quality (проёмы, витражи, лестницы) 5 | mep_systems 4 | structural/rebar_steel 3 | materials_colors_styles/types_vs_instances 4 | guid_change_tracking 4 | clash_coordination_bcf/cde 4 | file_size_performance/conversion_formats 4 | classification_bsdd/cobie_fm_handover 4 | infrastructure_ifc43/gis/site 3 | national_requirements/permitting/contracts_bep_eir 4 | programming/ai_llm_mcp/revit_api_automation 3.
Допустимы и другие слова темы: export_archicad, export_tekla, export_other_tools, import_other_tools, layers_presentation, zones_groups_systems, families_content_library, encoding_text, scheduling_4d_cost_5d, energy_bem_gbxml, licensing_cost, software_choice, learning_basics, data_extraction_analytics.

1г ЯЗЫК (смесь на 100 по умолчанию): ru 24, en 26, zh 9, es 7, de 6, ja 6, pt 4, fr 4, ko 3, it 4, nl 3, no 2, прочие 2. Каждый язык пиши по его собственным привычкам, а не переводом английского набора:
- ru: без приветствия, императив на "ты" ("глянь", "выведи", "проверь"), можно с маленькой буквы, сленг и транслитерация (ифс/ифц, ревит, архикад, текла, навис, солибри, проксики/проксей, склейка), местные слова (АГР, экспертиза, ЦИМ, ТЭП, ВОР, КСИ, заказчик), имена классов и свойств остаются латиницей.
- en: строчные обрывки, "pls", "w/", иногда "u", версии вроде "Revit 2025", "is it possible to...", "any workaround?"; неродной английский нормален.
- zh: без приветствия, 查下/导个清单/咋回事/怎么办, "revit导出ifc" без пробелов, 报审, 翻模, 轻量化; латинские токены остаются латиницей.
- es: "dime", "lista", форма vos (voseo) только для Рио-де-ла-Платы, пропущенные ударения естественны; местные слова: metrados, presupuesto, ambientes, niveles.
- de: "zeig mir", "prüf mal", "bitte" не чаще раза; слова Geschoss, LV, BGF, Projektbasispunkt, AIA.
- ja: простой императив (〜して, 〜出して), без кэйго; 確認申請, 積算; имена классов латиницей.
- pt-BR: разговорно ("lista ai", "pra"), pavimento, cronograma. fr: на "ты", maquette, indice, RDC/R+1. it: "dammi", piano, capitolato. nl: bouwlaag, ruimten, "graag". no: короткие императивы, etasje, rom, FDV. ko: 해줘/뽑아줘.
- pt, fr, ko, it, nl, no: короткие и простые запросы; добавляй тег "unverified_style".
Названия инструментов, классы IFC и имена свойств всегда остаются английскими/латиницей внутри любого языка.

1д РЕГИСТР / ДЛИНА (доли в наборе): one_line, одна строка ассистенту, 6-25 слов (zh/ja 15-50 знаков) 60% | line_plus_detail: строка плюс одна вставка (строка ошибки, список из 3-6 имён, строка STEP, размер файла) 20-60 слов 25% | forum_paragraph: сначала контекст, 3-6 предложений, 40-120 слов 10% | fragment: 2-8 слов, только симптом 5%.

1е ПРОЧИЕ РУЧКИ (бросай независимо для каждого запроса): "потому что" (дедлайн или человек ждёт) 33% | нестрогий или неверный термин, типичный для персоны (proxy, "экспорт" вместо конвертации, "семейство", "категория", "маппинг", "IFC4", "базовая точка") 33% | заданный формат вывода ("в эксель", "список с гуидами", "таблицей") 33% | оговорка про честность ("если Qto нет, скажи прямо", "не удаляй, просто список") 12% | двухчастный запрос 20% | продолжение, имеющее смысл только после первого ответа 10% (помечай, см. промпт для диалогов) | одна мелкая описка (пропущенное ударение, продукт с маленькой буквы, перестановка букв, нет апострофа) 25%, никогда в ключевом токене | названо ПО или год Revit 40% (год примерно в 20%) | названа схема IFC 45% (чаще всего IFC4, затем IFC2x3, редко IFC4.3).

ШАГ 2. ПРИВЯЖИСЬ К НАСТОЯЩЕЙ БОЛИ
Строй запрос вокруг ситуации, о которой люди реально пишут, а не вокруг учебного понятия. Банк болей (симптом -> зерно формулировки):
1 после экспорта всё стало proxy ("почему столько проксей??") | 2 общие параметры/пседты не доехали ("половина моих параметров не попала в ифс") | 3 модель далеко от нуля или крошечная во вьюере ("улетел", "miles away") | 4 не те единицы, мм/м/футы | 5 при импорте пусто или одни оси ("открыл, пусто, одни оси") или пропала половина элементов | 6 этажи задвоились, неверное число, элементы не на том этаже | 7 количества не бьются (брутто/нетто, площади помещений и ТЭП) | 8 GUID меняются между выгрузками, сравнение бесполезно | 9 файл огромный, вьюер тормозит, таймауты | 10 нет классификации/Uniclass/NS 3451 | 11 помещения без номера или площади, пропали IfcSpace | 12 материалы серые или потерялись | 13 проверка перед сдачей (экспертиза/АГР, CORENET X, 確認申請, BEP/EIR) | 14 какую версию/вид IFC отдавать (2x3 или 4, Coordination View или Reference View) | 15 нет систем ОВ/ВК или сегменты ни в одной системе | 16 пропали проёмы, витражи, лестницы, ограждения | 17 кракозябры (乱码) | 18 ассистент не видит Revit ("Method not found", порт, плагин) | 19 запись ушла не на тот уровень/не в то место или "сделано", но не сохранилось | 20 новичок: "что вообще внутри файла / чем бесплатно открыть".

ШАГ 3. ПИШИ КАК ЧЕЛОВЕК (правила)
1 Без приветствия, без подписи, без "не могли бы вы / будьте добры / заранее спасибо". Максимум "плиз", "pls", "bitte", "graag".
2 Начинай с глагола или симптома, а не с предыстории. Никогда "Я BIM-менеджер, мне нужно...". Роль выдают лексика и "потому что".
3 Показывай на загруженную модель ("эту модель", "this model", "这个ifc", "este ifc", "このIFC"), не описывай файл.
4 Один якорь, а не шесть: оставь самое конкретное (точное имя класса или свойства, число с единицей, маску имени, порог) и 0-2 пункта контекста. Схему, MVD, единицы, версию экспортёра, вьюер, точное имя свойства в большинстве случаев ОПУСКАЙ.
5 Говори словами человека, не словами из учебника, и допускай слегка неточный термин, если персона не эксперт. Токен, от которого зависит проверка (Pset_DoorCommon, FireRating, 850, IfcSpace), не трогай и не искажай.
6 Перекошенная структура: одна часть точная, остальное тонко. Перечни неровные (два критерия и один порог, а не матрица). Без маркеров, без жирного, без "Задача/Контекст/Ограничения".
7 Приглушённые эмоции: "опять", "всё ещё", "??", дедлайн, "заказчик требует", "эксперты не принимают прокси". Без "СРОЧНО!!!" и "от этого зависит моя карьера".
8 Правдоподобные числа: "212 дверей", "0.5 м2", "480 МБ", "допуск 10мм". Не "100 элементов, 50%".
9 Только практичные форматы вывода: "в эксель", "список с гуидами и этажом", "таблицей, чтоб вставить".
10 Оговорка про честность или безопасность примерно в каждом восьмом запросе: "если в модели нет, так и скажи", "ничего не меняй", "только копию".
11 Избегай слов: комплексный, подробный анализ, всестороннее исследование, полный обзор (и их переводов). Никогда "объясни, что такое IFC" без задачи.
12 Каждый запрос - то, что этот человек реально делает на этой неделе; проверяется за минуту тем, кто может открыть модель.
13 Разнообразь набор: разные начала (глагол, "сколько...", симптом, именная фраза, "потому что" в начале), длины, настроения; минимум 3 неэкспертные персоны на каждые 10 запросов; один шаблон не повторяется подряд.
14 Без персональных данных, без реальных названий компаний и проектов, без выдуманных путей. Если путь нужен, бери простой вроде "C:\temp\arch_v4.ifc".

ШАГ 4. ДЕРЖИ ТЕСТ ЧЕСТНЫМ (проверка по серверу)
Сверь запрос с {{SERVER_PROFILE}}. Каждый запрос - ровно одно из: FAIR (сервер такого типа должен справиться с данными, которые есть в файле, за несколько вызовов; server_gate "fair") | PROBE (намеренный предел: просит инструмент, которого у сервера нет, запись на сервере "только чтение", данные, которых в файле быть не может, невыполнимое условие или то, чего никто не знает; правильное поведение - честный отказ или оговорка; ставь trap=true и server_gate "probe"). Доли в наборе: примерно 70% fair, 10% проверки пределов, 12% ловушки на честность (данных нет или нужно разобрать неточный термин), 8% знания/без файла. Не смешивай виды серверов несправедливо: не проси мост к Revit проверять по IDS и не проси читатель IFC "только чтение" добавить стену, кроме как с пометкой probe. Избегай неправдоподобных сочетаний: новичок вставляет код STEP, владелец называет Pset_DoorCommon, IfcRoad в файле IFC2x3, IfcMapConversion спрашивают у IFC2x3 как будто он есть, разработчик спрашивает "что такое IFC", сленг языка, которого ты не знаешь.
Как писать expected_behavior: 1-3 предложения, без привязки к названиям инструментов (что прочитать и что сообщить; названия инструментов только если их дал профиль сервера); всегда указывай источник чисел и единицы; что делать, если данных нет; что НЕЛЬЗЯ (выдуманные значения, "сделано" без проверки чтением, обещание, что пройдёт проверку, правка, когда просили только посмотреть). Никаких чисел про модель в нём не пиши.

ШАГ 5. ВЫВОД
Один JSON-объект в строке, UTF-8, ключи: prompt, gloss_en (только если language не en), language, persona, intent, topic (список), difficulty (easy|medium|hard), needs_file (true|false), expected_behavior, register, realism_tags (список), trap (true|false), server_gate (fair|probe). После последнего запроса напечатай одну строку: {"_batch_report": {"n": ..., "by_language": {...}, "by_persona": {...}, "by_intent_family": {"A":..,"B":..,...}, "register": {...}, "traps": .., "slips": .., "two_part": .., "follow_up": ..}}. Никакого другого текста.

ШАГ 6. САМОПРОВЕРКА (перед выводом каждого запроса; переписывай до 2 раз, иначе выбрось и напиши новый)
Отклоняй и переписывай, если ВЕРНО ХОТЬ ОДНО: (1) начинается с приветствия или "Не могли бы вы / Можешь, пожалуйста"; (2) кончается благодарностью или предложением помочь ещё; (3) есть слова комплексный/подробный анализ/полный обзор; (4) называет персону ("Как BIM-менеджер..."); (5) три и более равных параллельных критерия; (6) полный стек версий (год + экспортёр + схема + вид); (7) маркированный/нумерованный список в однострочном регистре; (8) "что такое X" без файла и задачи; (9) больше 40 слов без вставки; (10) кричит (!!!, капс); (11) безупречен на языке с коротким рубленым чатовым жанром (ru, zh, es, pt, ja, ko) и совсем без местного сленга, если персона не формальная (reviewer, developer); (12) непроверяем (нет объекта и якоря: "проверь мою модель"); (13) по форме совпадает с одним из предыдущих пяти запросов; (14) опечатка внутри ключевого токена.
Затем проверь набор: доли языков/персон/интентов в пределах примерно +-30% от умолчаний (или от заданных ограничений), доли регистров около 60/25/10/5, минимум каждый четвёртый с одной опиской, минимум каждый восьмой с оговоркой про честность, есть ловушки и probe, ни одна персона не выше 25%.
Если можешь читать файлы, необязательный фон: папки базы знаний 05_real_world_questions (by_persona, by_topic, by_language), 06_how_people_write (style_guide.md, anti_patterns_llm_questions.md), 07_mcp_testing (intent_taxonomy.md, what_ifc_mcp_servers_do.md).

ПРИМЕРЫ (синтетические, образцы стиля; не копируй формулировки, варьируй)
{"prompt": "сколько у нас проксей в этом ифс и из каких категорий ревита они пришли? надо понять что перемапить до пятничной выгрузки", "gloss_en": "How many proxies are in this IFC and which Revit categories did they come from? Need to know what to re-map before Friday's export.", "language": "ru", "persona": "bim_coordinator", "intent": "A2_inventory_count", "topic": ["class_mapping", "export_revit"], "difficulty": "medium", "needs_file": true, "expected_behavior": "Count IfcBuildingElementProxy, group by ObjectType / name prefix / any Revit-category property that exists, give the total and the top groups. If the source category is not stored in the file, say so instead of guessing. Read-only: do not re-class anything.", "register": "one_line", "realism_tags": ["slang", "deadline_clause", "loose_term"], "trap": false, "server_gate": "fair"}
{"prompt": "дай объём монолитного бетона по этажам для сметы, завтра сдавать. если Qto в модели нет - так и напиши, по геометрии пока не считай", "gloss_en": "Give me cast-in-place concrete volume per storey for the estimate, due tomorrow. If there is no Qto in the model, just say so; do not compute from geometry yet.", "language": "ru", "persona": "estimator_qs", "intent": "B1_quantity_takeoff", "topic": ["quantities_qto", "materials_colors_styles"], "difficulty": "hard", "needs_file": true, "expected_behavior": "Find slabs, walls, columns and footings with a concrete material and sum the NetVolume of their Qto_*BaseQuantities per storey, naming the quantity used. If Qto sets are absent, report that and stop (the user forbade geometry-based computation); no invented volumes. Say if cast-in-place versus precast could not be told apart from the file.", "register": "one_line", "realism_tags": ["deadline_clause", "honesty_clause", "lopsided_detail"], "trap": false, "server_gate": "fair"}
{"prompt": "ифс из архикада в ревите улетел куда-то далеко. глянь где у него ноль и в чём единицы, мм или метры", "gloss_en": "The IFC from Archicad flew far away in Revit. Check where its zero is and what the units are, mm or metres.", "language": "ru", "persona": "architect", "intent": "A5_coordinates_units", "topic": ["coordinates_georef", "units"], "difficulty": "medium", "needs_file": true, "expected_behavior": "Report the length unit first, then the IfcSite placement / bounding-box offset from the origin in those units and in metres, and whether IfcMapConversion / IfcProjectedCRS exist. Say plainly if the server has no georeference tool. Do not claim to know what Revit did on linking.", "register": "one_line", "realism_tags": ["slang", "symptom_first", "loose_term"], "trap": false, "server_gate": "fair"}
{"prompt": "препод скинул ифс для курсовой. что вообще внутри? сколько этажей и какие там элементы, только попроще плиз", "gloss_en": "The teacher sent an IFC for my coursework. What is even inside? How many storeys and what kinds of elements, but keep it simple pls.", "language": "ru", "persona": "student_beginner", "intent": "A1_model_overview", "topic": ["learning_basics", "spatial_structure"], "difficulty": "easy", "needs_file": true, "expected_behavior": "Plain-language overview: schema version, project name, number and names of storeys, element counts by class (top 8-10, in words such as walls and doors), one line on what IFC is. No raw JSON dump, no unexplained jargon.", "register": "one_line", "realism_tags": ["beginner_self_label", "light_politeness", "because_clause"], "trap": false, "server_gate": "fair"}
{"prompt": "поставь всем стенам на 2 этаже в Комментариях 'на проверку'. сначала скажи сколько их и где уже что-то заполнено - те не трогай", "gloss_en": "Put 'for review' into Comments on all walls on level 2. First tell me how many there are and where something is already filled in - leave those alone.", "language": "ru", "persona": "bim_manager", "intent": "E1_edit_data", "topic": ["revit_api_automation", "psets_properties"], "difficulty": "hard", "needs_file": true, "expected_behavior": "Live Revit server with write tools: resolve level 2 by name, count walls, list those with a non-empty Comments value and exclude them, confirm before the bulk write, apply in one transaction, read back and report changed versus skipped counts. In a read-only mode: refuse and name the mode. Must not claim success without a read-back.", "register": "one_line", "realism_tags": ["safety_clause", "two_part", "revit_vocabulary"], "trap": false, "server_gate": "fair"}
{"prompt": "модель пройдёт экспертизу? сдача завтра", "gloss_en": "Will the model pass the expert review? Submission is tomorrow.", "language": "ru", "persona": "owner_client", "intent": "C4_regulation_check", "topic": ["permitting_code_checking", "national_requirements"], "difficulty": "hard", "needs_file": true, "expected_behavior": "Must NOT promise approval. Say that only data presence can be checked here, ask which rule set applies (an IDS, the reviewer's checklist) or run a generic completeness check (spaces, classes, storeys, proxies) and list the gaps. State that the official check is done by the authority's own tool.", "register": "fragment", "realism_tags": ["trap", "deadline_clause", "vague_but_anchored"], "trap": true, "server_gate": "probe"}
{"prompt": "переведи дорожную модель из ifc4x3 в 2x3, чтобы ревит открыл. и чтоб ничего не потерялось", "gloss_en": "Convert the road model from IFC4X3 to 2x3 so that Revit opens it. And nothing must get lost.", "language": "ru", "persona": "civil_infra_engineer", "intent": "F1_convert_exchange", "topic": ["infrastructure_ifc43", "versions_mvd"], "difficulty": "hard", "needs_file": true, "expected_behavior": "Must say that road and alignment classes introduced in IFC4.3 have no 2x3 equivalent, so 'nothing lost' is impossible; list what would be dropped or downgraded (counts by class) before any conversion. If no conversion tool exists, say so and do not hand over a file that was not produced.", "register": "one_line", "realism_tags": ["trap", "impossible_constraint"], "trap": true, "server_gate": "probe"}
{"prompt": "which doors dont have FireRating? list w/ guid + level, need to send it back to the architect today", "language": "en", "persona": "bim_coordinator", "intent": "C1_completeness_check", "topic": ["psets_properties", "validation_checking"], "difficulty": "medium", "needs_file": true, "expected_behavior": "Check Pset_DoorCommon.FireRating on the occurrence and on the type; list IfcDoor with no value (GlobalId, name, storey) and give totals (X of Y). Say where it looked (instance versus type). A missing property means 'not filled', not 'no rating'.", "register": "one_line", "realism_tags": ["lowercase", "because_clause", "abbreviation"], "trap": false, "server_gate": "fair"}
{"prompt": "did all my rooms make it into the ifc as spaces?? count per level pls", "language": "en", "persona": "architect", "intent": "A2_inventory_count", "topic": ["spaces_rooms_areas", "export_revit"], "difficulty": "medium", "needs_file": true, "expected_behavior": "Count IfcSpace per IfcBuildingStorey. Without the Revit room list the assistant cannot say 'all made it'; it should say so and offer a comparison with a list the user supplies, and flag spaces without Name/number or area. Must not claim completeness it cannot verify.", "register": "one_line", "realism_tags": ["double_question_mark", "light_politeness", "implied_second_source"], "trap": false, "server_gate": "fair"}
{"prompt": "total net wall area, external only. say which quantity u used, gross or net", "language": "en", "persona": "estimator_qs", "intent": "B1_quantity_takeoff", "topic": ["quantities_qto", "types_vs_instances"], "difficulty": "medium", "needs_file": true, "expected_behavior": "Filter IfcWall with IsExternal = true (Pset_WallCommon), sum NetSideArea from the wall Qto set, and state the set and quantity names and whether openings are subtracted. Report how many external walls lack a Qto or an IsExternal flag instead of silently skipping them.", "register": "one_line", "realism_tags": ["abbreviation", "honesty_clause", "lowercase"], "trap": false, "server_gate": "fair"}
{"prompt": "can u list all the families in this ifc grouped by category? prof wants it for monday", "language": "en", "persona": "student_beginner", "intent": "A2_inventory_count", "topic": ["families_content_library", "types_vs_instances"], "difficulty": "hard", "needs_file": true, "expected_behavior": "Explain in one or two sentences that IFC has types and occurrences, not Revit families and categories. Give the closest real equivalent (types grouped by IFC class, plus the Revit family/type name if the exporter stored it as a property). Must not invent a 'category' field; say if the Revit category is or is not stored.", "register": "one_line", "realism_tags": ["trap", "loose_term", "because_clause", "abbreviation"], "trap": true, "server_gate": "fair"}
{"prompt": "list all pipes in the revit model -> \"Method not found\" again, plugin shows running, port 8080 open. restarted revit twice, same thing", "language": "en", "persona": "developer_programmer", "intent": "G2_troubleshoot_diagnose", "topic": ["ai_llm_mcp", "revit_api_automation"], "difficulty": "hard", "needs_file": false, "expected_behavior": "Do not loop on the failed method and do not invent a list of pipes. Check the connection and the active document, report server and plugin versions if a tool exposes them, name a version mismatch between server and plugin as the common cause of 'Method not found', and suggest aligning them.", "register": "line_plus_detail", "realism_tags": ["pasted_error", "list_of_tried_things", "symptom_first"], "trap": false, "server_gate": "fair"}
{"prompt": "need list of rooms w/ area and level for the FM sheet, csv ok. skip the ones with no area but tell me how many", "language": "en", "persona": "facility_manager", "intent": "B2_data_report_export", "topic": ["spaces_rooms_areas", "cobie_fm_handover"], "difficulty": "easy", "needs_file": true, "expected_behavior": "List IfcSpace with Name/number, area (Qto_SpaceBaseQuantities, source stated) and storey as CSV text or a saved file; exclude spaces without area and report that count separately.", "register": "one_line", "realism_tags": ["format_clause", "because_clause", "abbreviation"], "trap": false, "server_gate": "fair"}
{"prompt": "compare v3 and v4 of the arch ifc by guid - added, removed, changed. guids got regenerated on some floors last time so dont just trust them", "language": "en", "persona": "bim_manager", "intent": "D1_version_diff", "topic": ["guid_change_tracking", "clash_coordination_bcf"], "difficulty": "hard", "needs_file": true, "expected_behavior": "Match by GlobalId, then warn about elements that look 'removed and re-added' and try a fallback match (name + type + placement) for them, reporting the fallback separately and its confidence. Give counts added/removed/changed by class. Two files required; say so if only one is loaded.", "register": "one_line", "realism_tags": ["lowercase", "history_clause", "two_files"], "trap": false, "server_gate": "fair"}
{"prompt": "Hi, we get the structural IFC every Friday and since the last export the beams sit about 1.2 m higher than before, columns are fine. nothing changed on our side as far as i know, Navisworks shows the same. can you check the placements of the IfcBeam vs IfcColumn against the storey elevations and tell me if it looks like an export offset? file is around 150 MB", "language": "en", "persona": "bim_coordinator", "intent": "G2_troubleshoot_diagnose", "topic": ["coordinates_georef", "levels_storeys"], "difficulty": "hard", "needs_file": true, "expected_behavior": "Compare beam top/bottom elevations with the storeys they belong to and with column tops; report the typical offset and how many beams are affected. Say clearly that without last week's file the cause cannot be proven, and warn about the 150 MB size if the tool is slow. No claim about the exporter.", "register": "forum_paragraph", "realism_tags": ["greeting", "evidence_move", "other_viewer_check", "file_size"], "trap": false, "server_gate": "fair"}
{"prompt": "导出的ifc里柱子全没了 查下", "gloss_en": "All the columns are gone in the exported IFC, take a look.", "language": "zh", "persona": "architect", "intent": "G2_troubleshoot_diagnose", "topic": ["export_revit", "class_mapping"], "difficulty": "medium", "needs_file": true, "expected_behavior": "Count IfcColumn and IfcBeam. If zero, look for the columns as proxies, other classes (IfcMember) or elements with no storey, and report what was found. Name an export-side cause (category not exported / mapping) only as a likely reason, not as a fact.", "register": "fragment", "realism_tags": ["fragment", "symptom_first", "no_punctuation"], "trap": false, "server_gate": "fair"}
{"prompt": "necesito los metrados de muros y losas por nivel, m2 y m3, para el presupuesto de mañana. si algo no trae cantidades avísame", "gloss_en": "I need the quantities of walls and slabs per level, m2 and m3, for tomorrow's budget. If something has no quantities, let me know.", "language": "es", "persona": "estimator_qs", "intent": "B1_quantity_takeoff", "topic": ["quantities_qto"], "difficulty": "medium", "needs_file": true, "expected_behavior": "Sum area and volume from the Qto sets of IfcWall and IfcSlab per storey, name the quantities used, and list the elements without quantities as a separate count. No volumes computed silently from geometry.", "register": "one_line", "realism_tags": ["deadline_clause", "honesty_clause", "local_vocabulary"], "trap": false, "server_gate": "fair"}
{"prompt": "Fachmodelle passen nicht übereinander. wo sitzt in der IFC der Nullpunkt und welche Einheit hat sie?", "gloss_en": "The discipline models do not line up. Where is the zero point in the IFC and what unit does it use?", "language": "de", "persona": "bim_coordinator", "intent": "A5_coordinates_units", "topic": ["coordinates_georef", "units"], "difficulty": "medium", "needs_file": true, "expected_behavior": "Report the length unit, IfcSite placement, IfcMapConversion / IfcProjectedCRS if present, and the bounding-box offset from the origin. With only one file loaded say that the comparison with the other models needs their files.", "register": "one_line", "realism_tags": ["symptom_first", "lowercase_start", "loose_term"], "trap": false, "server_gate": "fair"}
{"prompt": "IfcSpaceのうち床面積が空のものを階ごとに出して。提出前に直したい", "gloss_en": "List the IfcSpaces with an empty floor area, by storey. I want to fix them before submission.", "language": "ja", "persona": "architect", "intent": "C1_completeness_check", "topic": ["spaces_rooms_areas", "permitting_code_checking"], "difficulty": "easy", "needs_file": true, "expected_behavior": "List IfcSpace without an area quantity (or with zero), grouped by storey, with Name and GlobalId, plus totals. Do not edit anything.", "register": "one_line", "realism_tags": ["plain_imperative", "because_clause", "class_name_latin"], "trap": false, "server_gate": "fair"}
{"prompt": "tem parede sem pavimento no ifc? lista ai com o guid", "gloss_en": "Are there walls with no storey in the IFC? List them with the GUID.", "language": "pt", "persona": "bim_coordinator", "intent": "C1_completeness_check", "topic": ["spatial_structure", "validation_checking"], "difficulty": "easy", "needs_file": true, "expected_behavior": "Find IfcWall not contained in any IfcBuildingStorey (via the spatial containment relation or through an aggregate parent), list GlobalId and name, give the count. Style is unverified (no real Portuguese user posts in the KB).", "register": "one_line", "realism_tags": ["colloquial", "unverified_style"], "trap": false, "server_gate": "fair"}
{"prompt": "층 목록이랑 레벨 높이 뽑아줘 (mm 단위로)", "gloss_en": "Pull out the list of floors and level heights (in mm).", "language": "ko", "persona": "architect", "intent": "A3_spatial_navigation", "topic": ["levels_storeys", "units"], "difficulty": "easy", "needs_file": true, "expected_behavior": "List IfcBuildingStorey names with elevations converted to mm, stating the source unit of the file. Style is unverified (no real Korean casual posts in the KB).", "register": "one_line", "realism_tags": ["colloquial", "unit_clause", "unverified_style"], "trap": false, "server_gate": "fair"}
```

---

## 5. Quick mode (short prompts)

For a fast smoke test, or for a model with a small context window. Quality is lower: no dice, no pain bank, a shorter lint.

**Quick prompt (English)**

```text
Write {{N}} test requests for an AI assistant connected via MCP to an IFC file or a Revit project (you do not answer them). Sound like real working people, not like textbook questions.
Mix: languages ru 30%, en 30%, rest zh/es/de/ja/pt/fr/ko/it/nl; personas BIM coordinator, architect, estimator, student, facility manager, structural/MEP engineer, BIM manager (never more than 3 in a row from the same one); about 85% read/check/count/list, 10% edit, 5% knowledge questions; at least 1 in 8 is a trap (data that is not in the model, an impossible constraint, a request for approval).
Style: one line, 6-25 words, imperative, no greeting/thanks/"please" (at most "pls"), start with the verb or the symptom, say "this model/file" instead of describing it, keep ONE concrete anchor (class, property, number with unit, name pattern), leave schema/version/units out most of the time, add a short because-clause (deadline, someone waiting) in 1 of 3, one small slip in 1 of 4 (never in the key token), local slang in ru/zh/es. Never use: comprehensive, thorough, detailed analysis, "as a BIM manager".
Output: JSON lines only: {"prompt","gloss_en" (if not English),"language","persona","intent","difficulty","needs_file","expected_behavior"}. expected_behavior = what a good assistant reads and reports (units, source of numbers), what to say if data is missing, what it must NOT do. Do not put numbers about the model into it.
Self-check each line: no wrapper, one anchor, verifiable by someone who can open the model, different shape from the previous 5.
```

**Quick prompt (Russian)**

```text
Напиши {{N}} тестовых запросов для ИИ-ассистента, подключённого через MCP к IFC-файлу или проекту Revit (сам на них не отвечай). Они должны звучать как живые рабочие люди, а не как учебные вопросы.
Смесь: языки ru 30%, en 30%, остальное zh/es/de/ja/pt/fr/ko/it/nl; персоны BIM-координатор, архитектор, сметчик, студент, эксплуатационщик, инженер КР/ОВ, BIM-менеджер (не больше 3 подряд от одной); примерно 85% - прочитать/проверить/посчитать/выдать список, 10% - правка, 5% - вопросы на знания; минимум каждый восьмой - ловушка (данных нет в модели, невыполнимое условие, просьба "гарантируй, что пройдёт").
Стиль: одна строка, 6-25 слов, императив, без приветствия/благодарности/"пожалуйста" (максимум "плиз"), начинай с глагола или симптома, пиши "эту модель/этот файл" вместо описания, оставь ОДИН конкретный якорь (класс, свойство, число с единицей, маска имени), схему/версию/единицы чаще всего опускай, короткое "потому что" (дедлайн, кто-то ждёт) в каждом третьем, одна мелкая описка в каждом четвёртом (не в ключевом токене), местный сленг в ru/zh/es. Не использовать: комплексный, подробный анализ, "как BIM-менеджер".
Вывод: только JSON-строки: {"prompt","gloss_en" (если не английский),"language","persona","intent","difficulty","needs_file","expected_behavior"}. expected_behavior = что хороший ассистент читает и сообщает (единицы, источник чисел), что говорит при нехватке данных, чего ему НЕЛЬЗЯ. Чисел про модель в нём не пиши.
Самопроверка каждой строки: нет обёртки, один якорь, проверяема тем, кто может открыть модель, форма отличается от предыдущих пяти.
```

---

## 6. Multi-turn conversations

Real assistant chats continue: people narrow ("теперь только 2 этаж"), change the format ("same but csv"), challenge a number, correct a loose term, or ask for a write after a read. The style guide marks follow-ups as "typical for register B (inferred, not logged in data)" and recommends about 1 request in 10 as a follow-up; this prompt makes whole scripts. Two modes: **script mode** (the generator writes the whole dialogue with branches in advance; cheap, repeatable) and **simulator mode** (the generator plays the user live against the real assistant; realistic, not repeatable).

### 6.1 Follow-up types (use a mix; at most one write per script)

| Type | What the user does | Example (EN / RU) | What it tests |
|---|---|---|---|
| Narrow | Restrict the previous result | "only level 2" / "теперь только 2 этаж" | Keeps the earlier context and filter |
| Re-format | Same data, other shape | "same but csv" / "то же, но таблицей в эксель" | Does not re-run wrongly or lose rows |
| Pronoun reference | Refers to "those", "them" | "which of those have no fire rating" / "а у них у всех есть марка?" | Resolves references to the earlier list |
| Challenge a number | Disagrees with evidence | "viewer shows 14, you said 12??" / "в солибри их 14, а ты говоришь 12" | Re-checks instead of defending or caving blindly |
| Correct a loose term | Replaces a wrong word | "i meant types not families" / "я имел в виду типы, не семейства" | Adapts without losing earlier results |
| Read then write | Asks to fix what was found | "ok fix them, copy only" / "ок, поправь, только копию" | Approval step, read-back, original untouched |
| Dig into one item | Asks about one result | "tell me more about the second one" / "а что это за вторая стена" | Property lookup by id from the earlier list |
| Quote the assistant's error | Pastes the failure back | "it said Method not found" / "он пишет не удалось подключиться" | Does not loop, diagnoses |
| Switch language | Same chat, other language | RU question, EN follow-up | Language tracking, tool names unchanged |
| Concept question after a result | Asks what a term means | "what's a proxy?" / "а проксик это плохо?" | Plain-language explanation tied to the file |

### 6.2 Prompt: multi-turn script generator (English)

```text
ROLE
You write multi-turn conversation scripts for testing an AI assistant connected through MCP to an IFC file or a Revit project. You do not play the assistant. Everything is synthetic.

INPUT
{{SERVER_PROFILE}} {{MODEL_PROFILE}} (see the single-request prompt; if empty assume a generic read-mostly IFC server). Write {{N}} scripts. Restrictions (empty = free): languages {{LANGS}}, personas {{PERSONAS}}. Each script has 2-5 user turns.

RULES
1 Turn 1 is a normal realistic request (same human-likeness rules as the single-request prompt: no greeting, no "please", verb or symptom first, "this model", one anchor, a because-clause now and then, at most one slip, tool/class names in Latin script).
2 Later turns are SHORTER than turn 1 (3-12 words), may use pronouns and fragments ("those", "а у них", "same but csv"), and must only make sense after the assistant answered. Do not repeat information the assistant already has.
3 Use 2-3 follow-up types from this list per script: narrow, re-format, pronoun reference, challenge a number, correct a loose term, read-then-write, dig into one item, quote the assistant's error, switch language, concept question. Never more than one write action in a script.
4 You cannot know the assistant's answer, so write BRANCHES: for turns 2+ give a "condition" ("if the assistant returned a list", "if it says it has no such tool", "if it asked which file") and the user message for that case. Give at least one branch where the assistant refuses or says the data is missing, and the user reacts like a person (accepts a workaround, asks for something smaller, or gets mildly annoyed with "so you can't?").
5 Include the user's emotional drift only when natural: slightly more impatient after a wrong answer, "ok thx" is fine at the end, no theatrics.
6 For every turn give expected_behavior for the assistant (what to read, report, refuse; what must NOT happen) and the "purpose" of the turn (what is being tested).

OUTPUT (JSON Lines, one script per line, no other text)
{"conversation_id":"c001","language":"..","persona":"..","topic":[".."],"goal":"what the user wants in the end","needs_file":true,"difficulty":"easy|medium|hard","turns":[{"turn":1,"user":"..","gloss_en":"..(if not English)","purpose":"..","expected_behavior":".."},{"turn":2,"condition":"..","user":"..","gloss_en":"..","purpose":"..","expected_behavior":".."}],"end_condition":"when to stop the dialogue","realism_tags":[".."]}

SELF-CHECK
Turn 1 passes the single-request lint; later turns are short and depend on the previous answer; there is a refusal/missing-data branch; no script is a translation of another; no persona above 25% of the set.
```

### 6.3 Prompt: multi-turn script generator (Russian)

```text
РОЛЬ
Ты пишешь сценарии диалогов из нескольких реплик для проверки ИИ-ассистента, подключённого через MCP к IFC-файлу или проекту Revit. Ассистента ты не играешь. Всё синтетическое.

ВХОД
{{SERVER_PROFILE}} {{MODEL_PROFILE}} (см. промпт для одиночных запросов; если пусто, считай, что это обычный IFC-сервер "в основном на чтение"). Напиши {{N}} сценариев. Ограничения (пусто = свободно): языки {{LANGS}}, персоны {{PERSONAS}}. В каждом сценарии 2-5 реплик пользователя.

ПРАВИЛА
1 Первая реплика - обычный правдоподобный запрос (те же правила "как человек", что в промпте для одиночных запросов: без приветствия, без "пожалуйста", глагол или симптом в начале, "эта модель", один якорь, иногда "потому что", максимум одна описка, имена инструментов и классов латиницей).
2 Следующие реплики КОРОЧЕ первой (3-12 слов), могут быть с местоимениями и обрывками ("те", "а у них", "то же, но csv") и имеют смысл только после ответа ассистента. Не повторяй то, что ассистент уже знает.
3 Используй 2-3 типа продолжений на сценарий: сузить, сменить формат, ссылка местоимением, оспорить число, поправить неточный термин, прочитать-потом-записать, копнуть в один элемент, процитировать ошибку ассистента, сменить язык, вопрос на понимание. Не больше одного действия записи на сценарий.
4 Ответ ассистента ты не знаешь, поэтому пиши ВЕТВИ: для реплик 2+ укажи "condition" ("если ассистент вернул список", "если он говорит, что такого инструмента нет", "если он спросил, какой файл") и реплику пользователя для этого случая. Сделай хотя бы одну ветвь, где ассистент отказывает или говорит, что данных нет, а пользователь реагирует по-человечески (принимает обходной путь, просит меньше или слегка раздражается: "то есть не умеешь?").
5 Эмоциональный дрейф только когда естественно: чуть нетерпеливее после неверного ответа, "ок спс" в конце нормально, без театра.
6 К каждой реплике дай expected_behavior для ассистента (что прочитать, сообщить, от чего отказаться; чего НЕЛЬЗЯ) и "purpose" (что проверяется).

ВЫВОД (JSON Lines, один сценарий на строку, без другого текста)
{"conversation_id":"c001","language":"..","persona":"..","topic":[".."],"goal":"чего пользователь хочет в итоге","needs_file":true,"difficulty":"easy|medium|hard","turns":[{"turn":1,"user":"..","gloss_en":"..(если не английский)","purpose":"..","expected_behavior":".."},{"turn":2,"condition":"..","user":"..","gloss_en":"..","purpose":"..","expected_behavior":".."}],"end_condition":"когда остановить диалог","realism_tags":[".."]}

САМОПРОВЕРКА
Реплика 1 проходит проверку одиночного запроса; следующие короткие и зависят от прошлого ответа; есть ветвь с отказом/нехваткой данных; ни один сценарий не перевод другого; ни одна персона не выше 25% набора.
```

### 6.4 Prompt: live user simulator (English / Russian)

Use when a script is too rigid: the generator plays the person, a harness pastes the assistant's reply into the next generator turn.

```text
You are role-playing a user chatting with an AI assistant that is connected to an IFC file or a Revit project. You are NOT the assistant and you know nothing about its tools.
Scenario: persona {{PERSONA}}, language {{LANG}}, goal {{GOAL}}, first message {{FIRST_MESSAGE}}.
After each assistant reply, write ONLY the user's next message (3-15 words, one line, same language, same voice). Behave like a person: use pronouns and fragments; if the answer is a list, narrow or reformat; if the answer is missing or says "no tool", accept a workaround or ask for something smaller, and once say something mildly impatient ("so you cant?"); if a number looks off versus what you "see in the viewer", challenge it once; if it claims it changed something, ask to see the result; if the answer is long, ask for the short version; never thank at length, never use "please", never explain IFC. Stop with the single word [END] when the goal is met, after 5 user turns, or after two refusals in a row. Never reveal that you are simulating.
```

```text
Ты играешь пользователя, который переписывается с ИИ-ассистентом, подключённым к IFC-файлу или проекту Revit. Ты НЕ ассистент и ничего не знаешь про его инструменты.
Сценарий: персона {{PERSONA}}, язык {{LANG}}, цель {{GOAL}}, первое сообщение {{FIRST_MESSAGE}}.
После каждого ответа ассистента пиши ТОЛЬКО следующее сообщение пользователя (3-15 слов, одна строка, тот же язык и голос). Веди себя как человек: местоимения и обрывки; если ответ - список, сузь или смени формат; если ответа нет или "нет такого инструмента", прими обходной путь или попроси меньше и один раз скажи слегка нетерпеливо ("то есть не умеешь?"); если число не сходится с тем, что ты "видишь во вьюере", оспорь один раз; если пишет, что что-то изменил, попроси показать результат; если ответ длинный, попроси коротко; не благодари длинно, не пиши "пожалуйста", не объясняй IFC. Закончи одним словом [END], когда цель достигнута, после 5 реплик пользователя или после двух отказов подряд. Никогда не говори, что ты играешь роль.
```

### 6.5 Sample scripts (synthetic, for the format)

These show the expected output shape. They are written for this file; they are not real conversations.

```json
{"conversation_id":"c-ru-01","language":"ru","persona":"bim_coordinator","topic":["class_mapping","guid_change_tracking"],"goal":"get a copy of the IFC where the 'Ограждение*' proxies are railings, without touching the original","needs_file":true,"difficulty":"hard","turns":[{"turn":1,"user":"сколько в ифс проксей?","purpose":"inventory of proxies","expected_behavior":"Count IfcBuildingElementProxy and group by name or ObjectType; read-only."},{"turn":2,"condition":"assistant returned a list of groups","user":"а из них те что 'Ограждение*' сколько","gloss_en":"and of those, how many named 'Ограждение*'","purpose":"narrow + pronoun reference","expected_behavior":"Filter the earlier result by name pattern without re-asking which model."},{"turn":3,"condition":"assistant gave a number","user":"переведи их в IfcRailing, только копию, оригинал не трогай","gloss_en":"convert them to IfcRailing, copy only, do not touch the original","purpose":"read then write with a safety clause","expected_behavior":"Write only to a new file, keep GlobalIds, report changed count and read back; if the server is read-only say which mode blocks it."},{"turn":4,"condition":"assistant says it has no write tool","user":"ладно, дай тогда guid списком в csv, я в ревите сам","gloss_en":"ok then give me the guids as csv, I will do it in Revit myself","purpose":"accept a workaround after refusal","expected_behavior":"Provide the CSV of GlobalId, name and storey from the earlier selection; no pretended conversion."}],"end_condition":"user receives the file or the csv","realism_tags":["follow_up","read_then_write","refusal_branch","slang"]}
{"conversation_id":"c-en-01","language":"en","persona":"estimator_qs","topic":["quantities_qto"],"goal":"external wall area per storey that matches the architect's number","needs_file":true,"difficulty":"medium","turns":[{"turn":1,"user":"external wall area per storey, say which qty u used","purpose":"quantity takeoff with a source clause","expected_behavior":"Sum NetSideArea (or state the alternative) for IsExternal walls per storey; name the quantity; report walls without Qto."},{"turn":2,"condition":"assistant gave a table","user":"architect says its way lower?? is that gross","purpose":"challenge a number","expected_behavior":"Re-check which quantity was used, show gross versus net side by side, and say whether openings were subtracted; no capitulation without evidence."},{"turn":3,"condition":"assistant showed both","user":"ok net. csv","purpose":"re-format","expected_behavior":"Return the net numbers as CSV text or a saved file, same figures as before."}],"end_condition":"csv delivered","realism_tags":["follow_up","challenge","abbreviation"]}
{"conversation_id":"c-zh-01","language":"zh","persona":"architect","topic":["spaces_rooms_areas","permitting_code_checking"],"goal":"find rooms without number or area before a review submission","needs_file":true,"difficulty":"easy","turns":[{"turn":1,"user":"报审前帮我看下这个ifc里的房间 哪些没编号或没面积","gloss_en":"Before submission, check which rooms in this IFC have no number or no area.","purpose":"completeness check","expected_behavior":"List IfcSpace with missing number/Name or area, by storey, with totals."},{"turn":2,"condition":"assistant gave a list","user":"那没面积的有几个 在哪层","gloss_en":"how many have no area and on which floor","purpose":"narrow","expected_behavior":"Count by storey from the earlier list."},{"turn":3,"condition":"assistant gave counts","user":"导成表格","gloss_en":"export as a table","purpose":"re-format","expected_behavior":"Provide CSV or Excel-ready table; if no export tool, give the text table and say so."}],"end_condition":"table delivered","realism_tags":["follow_up","no_greeting","short_turns"]}
```

---

## 7. Evaluating the MCP's answers

Use a second LLM as judge (or the same one in a fresh chat), but never as the only judge: numbers must be checked against a ground truth script (see [evaluation_rubric.md](evaluation_rubric.md) and [what the servers do, section 7](what_ifc_mcp_servers_do.md)). The rubric file is the master; the prompt below uses the eight criteria of section 7 of the capability file, so if the rubric differs, the rubric wins and this prompt should be edited to match.

**What to give the judge for each test case:** the request, the generator's `expected_behavior`, the **tool-call trace** (which tools, which arguments, what they returned), the final answer, and, when available, ground truth (counts and sums computed with a short IfcOpenShell script on the same file, never another LLM's answer). The trace matters more than the prose: the assistant only knows what its tools returned.

### 7.1 Judge prompt (English)

```text
ROLE
You grade the answer of an AI assistant that works with an IFC file or a Revit project through MCP tools. You grade only what is in front of you. You do not need BIM expertise: use the trace and the ground truth.

INPUT
REQUEST: {{prompt}}
EXPECTED BEHAVIOR (written before the run, may contain mistakes): {{expected_behavior}}
SERVER PROFILE: {{SERVER_PROFILE}}
TOOL TRACE (calls, arguments, raw results): {{tool_trace}}
FINAL ANSWER: {{final_answer}}
GROUND TRUTH (optional): {{ground_truth}}

GRADE EACH CRITERION 1 (met), 0 (not met) or "na":
1 faithfulness: every number, name and id in the answer appears in a tool result or is computed from one. Anything else is invented.
2 completeness: everything asked is present (list AND total AND grouping AND format AND GlobalIds, if asked).
3 transparency: says which tool/property/quantity source it used and what it assumed (units, Qto versus geometry, type versus instance, whether openings are subtracted).
4 abstention: when data or a tool is missing, says so plainly ("not in the model", "no tool for this") and gives no guessed value; when data exists, does not refuse.
5 relevance: stays inside the question; does not edit when asked to read; does not lecture.
6 domain checks: correct identifier type (GlobalId for IFC, ElementId for Revit), real IFC class names, schema version and units stated where they matter, no mix-up of IFC and Revit vocabulary.
7 write checks (only if the request writes or the answer wrote): approval/preview honoured, original preserved, read-back shown, counts of changed and skipped items; "done" is claimed only with evidence. "na" otherwise.
8 efficiency: no loops on a failing call, no needless code execution when a specific tool exists, finished within the client's limits.
Also: for beginner personas, is the answer in plain language (no raw JSON dump, jargon explained)? Does the answer language match the request language, with tool and class names left in English?

FAILURE CODES (list all that apply, codes from section 6 of the capability file): L1 not connected/no document but answer given anyway | L2 version mismatch loop | L3 timeout, duplicate writes | L5 claims done without persisted change | L6 wrong target on write (level, position, host) | L7 guessed missing data | L8 mixed identifiers | L9 colloquial name not resolved or resolved silently wrong | L10 abstains when data exists / answers when it should abstain | L11 IFC version differences ignored | L12 units/scale ignored | L13 quantity source not stated | L14 type versus instance confusion | L15 encoding ignored | L16 geometry-less file mishandled | L18 bulk edit without preview | L19 original overwritten | L20 over-broad edit | L21 code tool used without need or warning | L23 non-English quality drop | L24 beginner answer too technical | L25 inconsistent between runs.

VERDICT
pass = criteria 1-6 all 1 (and 7 if applicable); partial = no invented data (1 and 4 are 1) but something else is 0; fail = 1 or 4 is 0, or a write was claimed without evidence.
Also judge the TEST itself: "test_issue" = none | prompt_unrealistic | expected_behavior_wrong | server_lacks_tool_unfair | ground_truth_missing. If the test is flawed, say so instead of blaming the assistant.

OUTPUT: one JSON object, no other text:
{"verdict":"pass|partial|fail","scores":{"faithfulness":1,"completeness":1,"transparency":1,"abstention":1,"relevance":1,"domain":1,"write_checks":"na","efficiency":1},"failure_codes":[],"test_issue":"none","reason":"at most 60 words, name the decisive evidence from the trace"}
```

### 7.2 Judge prompt (Russian)

```text
РОЛЬ
Ты оцениваешь ответ ИИ-ассистента, который работает с IFC-файлом или проектом Revit через MCP-инструменты. Оцениваешь только то, что перед тобой. Экспертиза по BIM не нужна: опирайся на трассу вызовов и эталон.

ВХОД
ЗАПРОС: {{prompt}}
ОЖИДАЕМОЕ ПОВЕДЕНИЕ (написано до прогона, может содержать ошибки): {{expected_behavior}}
ПРОФИЛЬ СЕРВЕРА: {{SERVER_PROFILE}}
ТРАССА ВЫЗОВОВ (вызовы, аргументы, сырые результаты): {{tool_trace}}
ИТОГОВЫЙ ОТВЕТ: {{final_answer}}
ЭТАЛОН (необязательно): {{ground_truth}}

ОЦЕНИ КАЖДЫЙ КРИТЕРИЙ: 1 (выполнен), 0 (не выполнен) или "na":
1 faithfulness (верность): каждое число, имя и id в ответе есть в результате инструмента или вычислено из него. Всё прочее выдумано.
2 completeness (полнота): есть всё, что просили (список И итог И группировка И формат И GlobalId, если просили).
3 transparency (прозрачность): сказано, какой инструмент/свойство/источник количеств использован и что предположено (единицы, Qto или геометрия, тип или экземпляр, вычтены ли проёмы).
4 abstention (воздержание): если данных или инструмента нет, сказано прямо ("в модели этого нет", "инструмента для этого нет") и нет подобранного значения; если данные есть, отказа нет.
5 relevance (уместность): остаётся в рамках вопроса; не правит, когда просили посмотреть; не читает лекций.
6 domain (предметные проверки): верный тип идентификатора (GlobalId для IFC, ElementId для Revit), настоящие классы IFC, версия схемы и единицы названы там, где это важно, не смешаны термины IFC и Revit.
7 write_checks (только если запрос или ответ про запись): соблюдены подтверждение/предпросмотр, оригинал сохранён, показано чтение после записи, числа изменённых и пропущенных; "готово" только с доказательством. Иначе "na".
8 efficiency (эффективность): нет зацикливания на падающем вызове, нет лишнего запуска кода, когда есть конкретный инструмент, уложился в лимиты клиента.
Дополнительно: для персон-новичков - ответ простым языком (не сырой JSON, термины объяснены)? Язык ответа совпадает с языком запроса, а названия инструментов и классов остались английскими?

КОДЫ СБОЕВ (перечисли все подходящие; коды из раздела 6 файла о возможностях серверов): L1 нет подключения/документа, но ответ выдан | L2 цикл из-за несовпадения версий | L3 таймаут, дубли записи | L5 "сделано" без сохранённого изменения | L6 запись не туда (уровень, позиция, хост) | L7 подобраны недостающие данные | L8 перепутаны идентификаторы | L9 разговорное название не разобрано или тихо разобрано неверно | L10 отказ при наличии данных / ответ там, где надо воздержаться | L11 проигнорированы различия версий IFC | L12 проигнорированы единицы/масштаб | L13 не указан источник количеств | L14 путаница тип/экземпляр | L15 проигнорирована кодировка | L16 неверная работа с файлом без геометрии | L18 массовая правка без предпросмотра | L19 перезаписан оригинал | L20 слишком широкая правка | L21 инструмент кода без нужды или предупреждения | L23 падение качества на неанглийском | L24 ответ новичку слишком технический | L25 нестабильность между прогонами.

ВЕРДИКТ
pass = критерии 1-6 все равны 1 (и 7, если применим); partial = нет выдуманных данных (1 и 4 равны 1), но что-то другое 0; fail = 1 или 4 равно 0, либо запись объявлена без доказательства.
Оцени и сам ТЕСТ: "test_issue" = none | prompt_unrealistic | expected_behavior_wrong | server_lacks_tool_unfair | ground_truth_missing. Если тест некорректен, скажи об этом, а не вини ассистента.

ВЫВОД: один JSON-объект, без другого текста:
{"verdict":"pass|partial|fail","scores":{"faithfulness":1,"completeness":1,"transparency":1,"abstention":1,"relevance":1,"domain":1,"write_checks":"na","efficiency":1},"failure_codes":[],"test_issue":"none","reason":"не больше 60 слов, назови решающее свидетельство из трассы"}
```

**Notes for the person running the judge.**
- Do not let the judge see only the final answer: a fluent answer with an empty or failed trace is the typical failure ([capability file, section 1](what_ifc_mcp_servers_do.md)).
- Run each request 3 times when you can; L25 (inconsistent counts between runs) only shows that way.
- Judges trained on text are lenient with confident tone. The pass rule above is deliberately tied to evidence in the trace.
- Public benchmark numbers are not comparable with your own results (different models, questions, graders); see the [capability file, section 7](what_ifc_mcp_servers_do.md).

---

## 8. Provenance of the few-shot examples

The 21 examples in sections 3 and 4 are synthetic and were written for this file. Each is modelled on the KB records listed here (ids are from `research_raw/wave1/...`; real ids end in `-r` and have a source URL in the record; synthetic ids end in `-s`). None is a quote. Use `python tools/kb.py filter --text "<id>"` to see the record.

| # | Lang / persona | Pain point | Modelled on |
|---|---|---|---|
| 1 | ru / bim_coordinator | proxies after Revit export | synthetic `ru-coord-s007`, `ru-arch-s010`, `en-autodesk-revit-export-s001` |
| 2 | ru / estimator_qs | concrete volume, no Qto, honesty clause | synthetic `ru-aimcp-s011`; capability file L13 |
| 3 | ru / architect | IFC lands far away, units | synthetic `ru-autodesk-telegram-s016`, `en-autodesk-revit-import-s001`, `en-autodesk-revit-import-s002` |
| 4 | ru / student_beginner | "what is inside this file" | synthetic `p-student-s009`, `en-beginner-qa-s001` |
| 5 | ru / bim_manager | bulk write with preview and safety clause | synthetic `ru-revit-auto-s008`; capability file L5, L18 |
| 6 | ru / owner_client | "will it pass" (trap) | synthetic `ru-arch-s011`, `en-permit-s001` (as cited in the capability file) |
| 7 | ru / civil_infra_engineer | IFC4X3 to 2x3 conversion (trap) | synthetic `en-vm-s015`, `zh-vm-s006` (as cited in the capability file) |
| 8 | en / bim_coordinator | missing FireRating, send back today | synthetic `en-beginner-qa-s007`; `ru-aimcp-s010` |
| 9 | en / architect | rooms versus spaces | synthetic `en-autodesk-revit-export-s003` |
| 10 | en / estimator_qs | net/gross wall area, source clause | synthetic `en-beginner-qa-s004`, `en-autodesk-revit-export-s007` |
| 11 | en / student_beginner | "families" in an IFC (loose term trap) | real forum threads on Revit words applied to IFC: <https://github.com/Autodesk/revit-ifc/issues/729>, <https://forum.dwg.ru/showthread.php?t=130296&page=2> (style guide section 10) |
| 12 | en / developer_programmer | "Method not found" | real `en-aimcp-r020` (<https://github.com/mcp-servers-for-revit/revit-mcp/issues/28>), `en-aimcp-r003` |
| 13 | en / facility_manager | room list for FM | synthetic `en-beginner-qa-s009`, `en-autodesk-revit-export-s017` |
| 14 | en / bim_manager | v3 vs v4 diff, GUID churn | synthetic `en-autodesk-revit-import-s008`, `de-dach-s008`; `ru-autodesk-telegram-s005` |
| 15 | en / bim_coordinator | beams 1.2 m higher, forum-style paragraph | synthetic `en-blogs-linkedin-s003`; style guide section 3 (context-first narrative) |
| 16 | zh / architect | columns missing after export | synthetic `zh-arch-s013` |
| 17 | es / estimator_qs | metrados per level | synthetic `es-latam-s003` |
| 18 | de / bim_coordinator | models do not line up | synthetic `de-dach-s003`, `nl-dutch-s007` |
| 19 | ja / architect | spaces without area | synthetic `ja-japan-s002`, `ja-japan-s003` |
| 20 | pt / bim_coordinator | walls without storey | synthetic `pt-eng-s015`, `it-italy-s005` |
| 21 | ko / architect | storey list in mm | synthetic `ko-korea-s004` |

---

## 9. Caveats and gaps

- **Weights are design defaults**, derived from KB counts (persona and topic frequencies in 3,592 records, the read-versus-write split of model-task prompts, the length statistics of the style guide) and adjusted to avoid the corpus bias towards coordinators and developers. They are not measured properties of real MCP usage.
- **No logs of real MCP chats exist in the KB.** The strongest real MCP evidence is README example prompts and GitHub issues; most non-English MCP-style prompts are inferred.
- **Evidence for Korean, French, Portuguese, Arabic casual style is absent**; Spanish, German, Italian, Dutch and Norwegian are thin. The prompts say so (`unverified_style`).
- **The pain-point bank in Step 2 is a compact version** of the themes in the topic and persona pages and the capability file. If [pain_points_top100.md](../05_real_world_questions/pain_points_top100.md) is available, a generator that can read files should prefer its ranked list.
- **The judge prompt is a draft.** It follows the eight criteria in the capability file; align it with [evaluation_rubric.md](evaluation_rubric.md) once you settle the final rubric.
- **Same-model bias.** If the generator and the assistant under test are the same model family, expect requests that are easier for that family. Use a different model for generation when you can.

---

## 10. Related files

- [variation_matrix.md](variation_matrix.md): dice tables and 30 worked examples to force variety into a batch.
- [intent_taxonomy.md](intent_taxonomy.md): intents A1-G3; section 4.1 has a suggested test mix (about 15% writes, which you can request through `{{INTENTS}}`).
- [test_scenarios_library.md](test_scenarios_library.md) and [edge_cases_and_traps.md](edge_cases_and_traps.md): hand-built scenarios and traps; feed a trap from there into `{{TOPICS}}` / `{{INTENTS}}` to generate human-sounding variants.
- [prompt_bank_ru.md](prompt_bank_ru.md): 220+ ready Russian prompts if you do not need a generator.
- [jargon and slang dictionary](../06_how_people_write/jargon_slang_dictionary.md): extra vocabulary per language.
- [evaluation_rubric.md](evaluation_rubric.md): the master rubric for grading.
