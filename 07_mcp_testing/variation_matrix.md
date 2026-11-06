# Variation matrix: dice-style tables for randomizing realistic test requests

**Compiled: 2026-11-06.** Part of [07_mcp_testing](what_ifc_mcp_servers_do.md). Use together with [llm_generation_prompt.md](llm_generation_prompt.md) (the ready-to-paste prompts), [intent_taxonomy.md](intent_taxonomy.md) (intents A1-G3), [evaluation_rubric.md](evaluation_rubric.md) and [what_ifc_mcp_servers_do.md](what_ifc_mcp_servers_do.md) (what each server kind can do).

**Why dice.** When an LLM is asked to "write 20 varied test requests" it drifts to the same persona (a BIM coordinator), the same language (English), the same intent (validate), and the same tidy shape (see [anti-patterns](../06_how_people_write/anti_patterns_llm_questions.md), section 4). Rolling the dimensions first, then writing, breaks that drift and makes a batch reproducible. The tables below can be rolled with real dice (d100 = two d10), with a script (section 11), or by the LLM itself ("commit to a random number before reading the table").

**Evidence and honesty notes.**
- Weights are **design defaults** built from counts in the knowledge base (3,592 records at the time of writing: 2,304 real, 1,288 synthetic; persona, topic, intent, software and schema tag frequencies; the length and roughness statistics of the [style guide](../06_how_people_write/style_guide.md)). Where the corpus is skewed (coordinators 950 and developers 825 of 3,592 records; English 2,452 records) the weights were deliberately flattened. They are **not** measured shares of real MCP usage; no logs of real MCP chats exist in the base.
- Every request in the 30 worked examples (section 9) is **synthetic**, written for this file and modelled on records that are named in the examples; none is a real quote.
- Korean, French and Portuguese have no real casual-style posts in the base (rows tagged `unverified_style`); Italian, Dutch, Norwegian, Spanish and German are thin.
- Nothing was run against a live MCP server.

---

## 1. The roll order

Roll in this order, because later rolls depend on earlier ones. Re-roll (or repair) at step 12 if the combination fails the plausibility check of sections 5-8.

| Step | Table | Die | Decides |
|---|---|---|---|
| 1 | T1 Language | d100 | the voice and the local vocabulary |
| 2 | T2 Persona | d100 | who is typing, how rough, what words |
| 3 | T3 Topic cluster | d100 | the pain point and the anchor tokens |
| 4 | T4 Intent | d100 | what the person wants done (and which server kinds are fair) |
| 5 | T5 Software named? then tool, then Revit year | d100 x 2-3 | the context word that sounds real |
| 6 | T6 IFC schema stated | d100 | schema mention (not the real schema of the file) |
| 7 | T7 Context items: how many, which | d100 + d12 | how much background |
| 8 | T8 Register / length | d100 | one line, line + detail, paragraph, fragment |
| 9 | T9 Emotion | d100 | tone, in one marker |
| 10 | T10 Slip | d100 | typo / casing / accent |
| 11 | T11 Flags | d100 each | because-clause, loose term, format, honesty, two-part, follow-up, trap |
| 12 | Plausibility gate | - | sections 5-8; repair or re-roll |
| 13 | T12 Derived fields | - | difficulty, needs_file, server_gate |

**Quick shortcut:** roll only T1, T2, T4, T11 and let the generator choose the rest in the way the human-likeness rules say.

---

## 2. Tables T1-T4 (who, where, what)

### T1. Language (d100)

| d100 | Language | Voice kit and evidence |
|---|---|---|
| 1-24 | ru | ты-imperative (глянь, выведи, проверь), no greeting; ифс/ревит/архикад/проксики; АГР, экспертиза, ТЭП, ВОР, КСИ. Evidence medium; real MCP prompts: none, modelled on EN/ZH patterns |
| 25-50 | en | lowercase fragments, pls, w/, u; version strings; non-native English is normal. Evidence strong (GitHub/forum bias) |
| 51-59 | zh | 查下 / 咋回事 / 导个清单, no spaces in revit导出ifc; 报审, 翻模, 轻量化. Evidence good for titles |
| 60-66 | es | dime / lista; dropped accents natural; metrados, presupuesto, ambientes, niveles. Evidence thin |
| 67-72 | de | zeig mir / prüf mal; Geschoss, LV, BGF, Projektbasispunkt, AIA. Evidence thin |
| 73-78 | ja | plain imperative (出して, 確認して), no keigo; 確認申請, 積算. Evidence medium (blogs) |
| 79-82 | pt | casual (lista ai, pra); pavimento, cronograma. No real posts: tag unverified_style |
| 83-86 | fr | tutoiement; maquette, indice, RDC / R+1. No real posts: tag unverified_style |
| 87-89 | ko | 해줘 / 뽑아줘. No real casual posts: tag unverified_style |
| 90-93 | it | dammi / confronta; piano, capitolato. Thin: tag unverified_style |
| 94-96 | nl | bouwlaag, ruimten, ILS, graag. Thin |
| 97-98 | no | terse imperatives; etasje, rom, FDV, NS 3451. Thin |
| 99-100 | other (tr, ar, vi, sk, cs, el, da) | one record each in the KB; keep to one short line, tag unverified_style |

Tool names, IFC class names and property names stay in English / Latin script inside every language.

### T2. Persona (d100)

| d100 | Persona | Voice and roughness (style guide 12.1) |
|---|---|---|
| 1-18 | bim_coordinator | high roughness: lowercase, slang, deadline clause, exact class names |
| 19-32 | architect | high: colloquial, Revit words (family, levels), visual symptoms |
| 33-42 | bim_manager | medium: checks before delivery, BEP / EIR / IDS words |
| 43-51 | estimator_qs | medium: tables, BoQ per storey/type, source-of-quantity clause |
| 52-60 | student_beginner | high on vocabulary, low on slang: self-label, what is inside, tools |
| 61-67 | structural_engineer | medium: short, exact class names (IfcColumn, IfcBeam), units |
| 68-74 | mep_engineer | medium: systems, segments, lengths; clash with structure |
| 75-79 | developer_programmer | low (terse): class names, pasted error or call, API questions |
| 80-84 | facility_manager | medium: handover, rooms, asset data, 'FM says', few IFC terms |
| 85-88 | owner_client | medium: business words, 'does it have', 'is it OK', few IFC terms |
| 89-92 | contractor_site | medium: what is on level N, pours, 4D schedule links |
| 93-96 | reviewer_authority | low: formal, names a norm / IDS / submission |
| 97-99 | civil_infra_engineer | medium: roads, alignments, CRS, IFC4.3 |
| 100 | researcher_academic | rare: benchmarks, datasets, 'how reliable is' |

Roughness modifier for T10: coordinators, architects and students roll the slip table with +1 (roll twice, keep the worse); reviewers and developers roll it with -1 (re-roll a slip once). See the [persona pages](../05_real_world_questions/by_persona/bim_coordinator.md) for each role's daily tasks.

### T3. Topic cluster (d100)

| d100 | Topic cluster | Anchor tokens to borrow (pick one) |
|---|---|---|
| 1-8 | 1 Class mapping, proxies, Revit export classes | IfcBuildingElementProxy, IfcExportAs, 'proxy', mapping table, Revit categories |
| 9-16 | 2 Property sets and parameters missing | Pset_WallCommon, FireRating, IsExternal, LoadBearing, shared parameters, Mark |
| 17-23 | 3 Quantities, cost, BoQ, 4D / 5D links | Qto_WallBaseQuantities NetSideArea / GrossSideArea, NetVolume, Qto_SpaceBaseQuantities, 'gross or net', elements with no schedule task |
| 24-30 | 4 Coordinates, georeference, units | IfcSite, IfcMapConversion, IfcProjectedCRS, IfcUnitAssignment, base point, 'miles away' |
| 31-36 | 5 Levels, storeys, spatial structure | IfcBuildingStorey, elevations, 'elements without a storey', duplicated storeys |
| 37-41 | 6 Spaces, rooms, zones, areas | IfcSpace, LongName, area, department, room number, zones |
| 42-48 | 7 Validation, IDS, model checking | IDS, schema errors, required properties, naming rules, PASS / FAIL |
| 49-53 | 8 IFC versions, views (MVD), schema choice | IFC2x3 vs IFC4, Coordination View, Reference View, Design Transfer View |
| 54-58 | 9 Import / link into Revit, viewers, 'opens empty' | Link IFC, only grids, empty view, BIM Vision, Solibri |
| 59-63 | 10 Geometry: openings, curtain walls, stairs, railings | IfcOpeningElement, IfcCurtainWall, IfcStair, IfcRailing, missing or doubled |
| 64-67 | 11 MEP systems | IfcDuctSegment, IfcPipeSegment, IfcCableCarrierSegment, IfcSystem, 'not in any system' |
| 68-70 | 12 Structural, rebar, steel | IfcColumn, IfcBeam, IfcMember, IfcReinforcingBar, Tekla, analytical model |
| 71-74 | 13 Materials, colours, types vs instances | IfcMaterial, layer sets, grey elements, type vs occurrence, 'families' |
| 75-78 | 14 GUIDs, change tracking, compare | GlobalId churn, added / removed / changed, v3 vs v4 |
| 79-82 | 15 Clash, BCF, CDE | clash tolerance, hard vs soft, BCF, grouping, issues |
| 83-86 | 16 File size, performance, conversion | 480 MB, timeouts, glTF / GLB, DWG, lightweighting (轻量化) |
| 87-90 | 17 Classification, COBie, FM handover | IfcClassificationReference, Uniclass, NS 3451, COBie, serial number, manufacturer |
| 91-93 | 18 Infrastructure, IFC4.3, site, GIS | IfcAlignment, IfcRoad (4.3 only), EPSG, CityGML, terrain |
| 94-97 | 19 National rules, permits, contracts | АГР / экспертиза, CORENET X, 確認申請, BEP / EIR, ILS, 报审 |
| 98-100 | 20 Programming, automation, AI / MCP itself | ifcopenshell, Revit API, pyRevit, MCP connection, 'Method not found' |

Per-topic background: [topic pages](../05_real_world_questions/by_topic/coordinates_georef_units_levels.md) and, once available, [pain_points_top100.md](../05_real_world_questions/pain_points_top100.md) (path assumed; written in parallel).

### T4. Intent (d100; read about 88%, write about 12%)

[intent_taxonomy.md, section 4.1](intent_taxonomy.md) suggests about 15% writes (E1-E3) for a full test set because real MCP issues are write-heavy; this table uses 12% to stay near the read-heavy shape of real model-task prompts (about 89% read). To oversample writes, add 3 points to E1-E3 and take them from A2, A4 and C1. Intent shares inside the taxonomy file's corpus counts (C1 14.8%, B1 11.5%, A4 10.1% of model-task prompts) were flattened here on purpose.

The last column is the server gate: which server groups can serve the intent (from [capability file, section 5](what_ifc_mcp_servers_do.md); group codes 1a, 1b, 2, 3a, 3b, 3c, 4 are defined there, `3x` means all Revit / Archicad / Tekla / Navisworks bridges). If the target server is not in the list, either re-roll or keep the request as a **probe** (`trap: true`, `server_gate: probe`).

| d100 | Intent | Typical meaning | Server groups that can serve it |
|---|---|---|---|
| 1-4 | A1 model_overview | what is in this file | 1a 1b 2 |
| 5-12 | A2 inventory_count | how many X, by class / storey / type | 1a 1b 2 3a 3b 3c 4 |
| 13-16 | A3 spatial_navigation | storeys, what is on level N | 1a 2 (3x partly) |
| 17-22 | A4 property_lookup | value of a property / material / classification | 1a 1b 2 3x |
| 23-28 | A5 coordinates_units | where is zero, units, georeference | 2, 1a (limited), Horizun (3b) |
| 29-35 | B1 quantity_takeoff | areas, volumes, lengths, sums | 1a (ifcopenshell-mcp), 2, 3a |
| 36-39 | B2 data_report_export | list / table / csv / BCF | 1a 2 3x |
| 40-46 | C1 completeness_check | which elements lack data | 1a 1b 2 3x |
| 47-51 | C2 rule_validation | IDS, schema, MVD, naming rules | 1b, Horizun (3b) |
| 52-55 | C3 mapping_geometry_audit | proxies, duplicates, no geometry, wrong class | 1a 1b 2 |
| 56-58 | C4 regulation_check | permit / expert / BEP-EIR style check | 1a 2, special servers (e.g. ifc-ruhsat) |
| 59-63 | D1 version_diff | compare two files / versions | 1a (ifcopenshell-mcp), 1b (ifc-lite) |
| 64-67 | D2 clash_coordination | clashes, BCF | 3c (Navisworks), 3b (rvt-mcp, Horizun, Demolinator) |
| 68-72 | E1 edit_data | change a property / class / name | 2, 3x, ifc-lite (1b) |
| 73-75 | E2 create_elements | walls, doors, levels | 2, 3x, ifcx-mcp (1b) |
| 76-79 | E3 batch_automation | rename / export / fill many things | 3x, 2 |
| 80-83 | F1 convert_exchange | IFC versions, glTF, DWG, export from Revit | 1b, a few 3b |
| 84-85 | F2 visualize_view | screenshot, isolate, colour | 2, 4, some 3x |
| 86-88 | F3 optimize_performance | heavy file, timeouts | 1a 1b 2 |
| 89-92 | G1 explain_howto | knowledge, which tool, which IFC version to send | any (no file needed) |
| 93-98 | G2 troubleshoot_diagnose | why is X empty / missing / far away | 1a 2 |
| 99-100 | G3 tool_meta | what can you do here, which tools | any |

---

## 3. Tables T5-T11 (how it is said)

### T5. Software mention (three small rolls)

**T5a. Is software named at all? (d100)**

| d100 | Option | What it looks like |
|---|---|---|
| 1-60 | no software named | 'this model', 'this ifc' |
| 61-80 | a tool named, no version | 'из архикада', 'tekla export', 'in solibri' |
| 81-100 | Revit year named | 'Revit 2025', 'ревит 2024' |

**T5b. Which tool? (d100, only if a tool is named)**

| d100 | Tool | Notes |
|---|---|---|
| 1-44 | Revit (then roll the year) | most mentioned authoring tool in the records (1,077 software tags) |
| 45-54 | Archicad | version rarely stated; 'ifc из архикада' |
| 55-62 | Solibri | viewer / checker; 'in solibri it is fine' |
| 63-69 | Bonsai / BlenderBIM / Blender | mostly EN, also ES / ZH; 'blenderbim' is the old name still used |
| 70-75 | Tekla (Structures) | structural; 'текла', '参' |
| 76-80 | Navisworks | 'навис', clash and federation |
| 81-84 | BIM Vision | free viewer; 'BIMvision' |
| 85-87 | Allplan | DACH |
| 88-90 | Renga | ru only (reroll for other languages) |
| 91-92 | Civil 3D | infra |
| 93-94 | BIMcollab / BCF tools | issues |
| 95-97 | Dynamo / pyRevit | automation |
| 98 | nanoCAD | ru only |
| 99-100 | Vectorworks / Bentley / other | rare |

Tendencies, not rules: Renga and nanoCAD questions in the base are in Russian-language sources (cell `ru-renga-nanocad`), Allplan mostly in German-language ones, Bonsai / Blender in English, Spanish and Chinese ones. Reroll odd pairs unless you want a deliberate probe. Counts behind the weights (software tags in the records): Revit 1,077; Archicad 127 + 40; Solibri 96; Bonsai 243 + BlenderBIM 79; Navisworks 49; Tekla 48 + 28; BIMcollab 25; Civil 3D 23; Allplan 21; Renga 20.

**T5c. Which Revit year? (d100, only if a year is named)**

| d100 | Year | Notes |
|---|---|---|
| 1-4 | 2019 or older |  |
| 5-9 | 2020 |  |
| 10-15 | 2021 |  |
| 16-28 | 2022 |  |
| 29-43 | 2023 |  |
| 44-62 | 2024 |  |
| 63-81 | 2025 | Archicad IFC import regressions are reported for 2025 |
| 82-98 | 2026 |  |
| 99-100 | 2027 | appears in the records; rare |

The shape follows the year tags in the records (2024: 71, 2022: 69, 2023: 68, 2025: 60, 2026: 46, 2020: 38, 2021: 34, 2027: 28, 2019: 25, 2018: 10), smoothed. A year is named in about 1 request in 5 (style guide section 16).

### T6. IFC schema stated in the text (d100)

| d100 | Stated schema | Notes |
|---|---|---|
| 1-55 | not stated | about half of real posts never say it; short prompts almost never do |
| 56-83 | IFC4 | most common when stated; often means Reference View or just 'newer than 2x3' |
| 84-95 | IFC2x3 | legacy Coordination View world; often with Revit, Tekla, authorities |
| 96-99 | IFC4.3 / IFC4X3 | infrastructure; spelled 'IFC 4.3', 'IFC4X3', 'ifc4x3_add2' |
| 100 | IFC5 / ifcx (draft) | only developers and curious people |

Important: this rolls what the **person says**, not the real schema of the test file. The generator must never state a schema that contradicts the loaded file (if the model profile is known). Across the records the stated schemas are: IFC4 1,457, IFC2x3 586 (+17 spelled 2X3), IFC4X3 / 4.3 about 240, IFC5 3; about 1,200 say nothing or "unknown".

### T7. Context: how many items, and which

**T7a. Number of context items (d100)**

| d100 | Items given | Linked register |
|---|---|---|
| 1-25 | 0 items: only the ask + 'this model' | R1 or R4 |
| 26-65 | 1 item | the default; R1 |
| 66-92 | 2 items | R1 or R2 |
| 93-100 | 3+ items (pasted detail, forum narrative) | R2 needs at least 1 pasted detail; R3 needs 3+ items; mostly developers, managers, forum-minded people |

**T7b. Which item (roll a d12 once per item)**

| d12 | Context item |
|---|---|
| 1 | Revit year or tool ('Revit 2025', 'из теклы') |
| 2 | File size ('480 MB', '90 мб', '100多M') |
| 3 | Cross-check in another viewer ('opens fine in BIM Vision') |
| 4 | A pasted error line or a quoted assistant reply |
| 5 | Motive or person waiting ('заказчик требует', 'before the coord meeting') |
| 6 | What was tried ('restarted revit twice', 'raised the limit, no effect') |
| 7 | Count mismatch ('viewer shows 14, BEP says 8') |
| 8 | Name pattern or threshold ('Колонна_*', '850', 'tolerance 10mm') |
| 9 | Destination ('для Солибри', 'to the architect', 'FM sheet', 'для АГР') |
| 10 | Time reference ('v3 vs v4', 'last week's', 'since the last export') |
| 11 | Schema or view ('IFC4 RV', '2x3 CV2.0') |
| 12 | Who produced it ('архитекторы прислали', 'from the engineer') |

Leave out on purpose (a real person usually does): IFC schema or view, exporter version, units, exact property name, which viewer, the file itself, what the model contains, the expected result. Give one or two items, not six ([style guide 4.4](../06_how_people_write/style_guide.md)).

### T8. Register and length (d100)

| d100 | Register | Length and shape |
|---|---|---|
| 1-60 | R1 one line typed to the assistant | 6-25 words (zh / ja 15-50 characters) |
| 61-85 | R2 line + one pasted detail | 20-60 words: an error line, 3-6 names, a STEP line, a size |
| 86-95 | R3 forum-style paragraph | 40-120 words, context first, 3-6 sentences; a 'hi' is allowed here |
| 96-100 | R4 fragment | 2-8 words, symptom only ('导出的ifc里柱子全没了') |

Check: a one-liner above 25 words (zh / ja above 50 characters) is a smell; the exception is a one-liner with a pasted detail, which then belongs to R2.

### T9. Emotion (d100)

| d100 | Tone | How it shows (one marker, never three) |
|---|---|---|
| 1-45 | neutral imperative | list X, проверь Y, 层别统计一下: no emotion words |
| 46-57 | curious / how-to | how come, а можно ли, 有没有办法 |
| 58-65 | confused | what is wrong, что не так, 咋回事 |
| 66-77 | understated frustration | again, still, опять, ??, 又 (one marker, not three) |
| 78-90 | urgency through a deadline | tomorrow, today, до пятницы, 报审前; never capital letters |
| 91-95 | skeptical / challenging | are you sure, в солибри 14, а ты говоришь 12 |
| 96-99 | light politeness | pls, плиз, bitte, graag |
| 100 | dry sarcasm / fatigue | ради пустого параметра, mission impossible (rare; strongest in RU / EN forums) |

Real forum and GitHub posts are more frustrated and confused (tone tags over 2,256 real records: neutral 33%, frustrated 20%, confused 20%, curious 19%, polite 4%); requests **typed to an assistant** are blunter and more neutral (no "please" in 93% to 100% of prompts). The table above is the second case. Never: "URGENT!!!", "my career depends on it".

### T10. Slip (d100; at most one per request)

| d100 | Slip | Notes |
|---|---|---|
| 1-70 | no slip | about 1 in 4 to 1 in 3 casual prompts may carry one |
| 71-78 | lowercase / casual casing of product or class ('revit', 'ifcwall', 'ifc') | not a typo, a habit |
| 79-84 | dropped accent / diacritic | es, pt, fr, de: cuantos, ambientes; also ё -> е in ru |
| 85-90 | letter swap or doubled letter in a non-key word | 'recieve', 'qantities', 'Querry' style |
| 91-95 | missing apostrophe or article | dont, cant, 'got ifc from architect' |
| 96-98 | run-on, no punctuation | whats the root cause of grey MEP-components in IFC |
| 99-100 | transliteration / mixed script | ифс, ревит, текла; revit导出ifc |

Never put the slip in the key token (class name, property name, number, threshold). About 1 in 4 casual prompts carries one; skip it for formal personas.

### T11. Flags (roll d100 separately for each; "yes" if the roll is at most the percentage)

| Flag | Yes if roll is at most | Looks like |
|---|---|---|
| because-clause (deadline or person waiting) | 33 | before the coord meeting; заказчик требует |
| loose or wrong term typical of the persona | 33 | proxy, 'export' for convert, family, category, mapping, 'IFC4', base point |
| stated output format | 33 | csv ok; list with guids; в эксель; 表格 |
| honesty / safety clause | 12 | if there's no Qto say so; don't change anything; копию только |
| two-part request | 20 | piggy-backed second check |
| follow-up (script it, see the multi-turn prompt) | 10 | only makes sense after a first answer |
| trap or probe (any kind) | 22 | data absent, impossible constraint, unknowable, server lacks the tool, loose term |

Style-guide defaults behind these numbers: because-clause 1 of 3, loose term 1 of 3, output format 1 of 3, honesty clause 1 of 8 (12%), two-part 1 of 5, follow-up 1 of 10. The 22% for "trap or probe" is a design choice that matches the mix in the prompt (about 10% limit probes plus 12% honesty traps).

---

## 4. Derived fields and how to assemble a request from the rolls

### 4.1 T12. Derived fields (no dice)

**Difficulty** (heuristic, override by judgement). Add points: needs grouping or 2+ tool calls +1 | loose term or ambiguity to resolve +1 | data may be absent, or an honesty clause +1 | source-of-number reasoning (Qto versus geometry, type versus instance, units) +1 | two files or an external input (IDS, EIR list, second model) +1 | write action +2 | trap or probe +3. Score 0-1 = easy, 2-3 = medium, 4 or more = hard.

**needs_file** = false for pure knowledge, tool-finding and connection questions (G1, G3, many T20 rolls); true otherwise.

**server_gate** = fair if the server kind of the target is in the last column of T4; probe otherwise (and then `trap = true`).

### 4.2 Assembly recipe (what the generator does with the numbers)

1. Write the **anchor** first: one exact token from T3 (a class, a pset, a number with unit, a name pattern).
2. Turn T4 into the **verb or the symptom**; start the sentence with it.
3. Put the persona's **own words** around it (T2 voice, T1 voice kit). Use "this model / эту модель / 这个ifc".
4. Add the T7 **context items** (exactly as many as rolled), the T5/T6 mentions, and the T11 flags that came up.
5. Cut to the T8 **length**; apply the T9 tone with one marker; apply the T10 slip (not in the anchor).
6. Run the lint of the [style guide, section 14](../06_how_people_write/style_guide.md) and the [anti-pattern quick lint](../06_how_people_write/anti_patterns_llm_questions.md), then write `expected_behavior`.

---

## 5. Realistic combinations: persona x intent family and persona x language

### 5.1 Persona x intent family

Families: **A** read the model (overview, inventory, spatial, property, coordinates) | **B** quantities and reports | **C** checks (completeness, rules, mapping and geometry audit, regulation) | **D** compare and clash | **E** write (edit, create, batch) | **F** convert, view, performance | **G** learn, troubleshoot, meta.
Legend: **●** frequent for this persona, **○** possible, **✗** avoid unless it is a labelled trap. Judged from the persona pages and the intent counts per persona in the records; a judgement table, not a measured one.

| Persona | A | B | C | D | E | F | G |
|---|---|---|---|---|---|---|---|
| architect | ● | ○ | ● | ○ | ○ | ○ | ● |
| bim_coordinator | ● | ○ | ● | ● | ○ | ○ | ● |
| bim_manager | ○ | ○ | ● | ● | ○ | ○ | ● |
| structural_engineer | ● | ● | ○ | ○ | ○ | ○ | ● |
| mep_engineer | ● | ● | ○ | ● | ○ | ○ | ● |
| civil_infra_engineer | ● | ○ | ○ | ○ | ✗ | ● | ● |
| estimator_qs | ○ | ● | ○ | ○ | ✗ | ○ | ○ |
| contractor_site | ● | ● | ○ | ○ | ✗ | ○ | ○ |
| facility_manager | ○ | ● | ● | ✗ | ✗ | ✗ | ○ |
| owner_client | ● | ○ | ● | ✗ | ✗ | ✗ | ● |
| reviewer_authority | ○ | ○ | ● | ○ | ✗ | ✗ | ○ |
| developer_programmer | ○ | ○ | ○ | ○ | ● | ● | ● |
| student_beginner | ● | ○ | ○ | ✗ | ✗ | ○ | ● |
| researcher_academic | ○ | ○ | ○ | ○ | ○ | ○ | ● |

Hints per cell worth remembering:
- **estimator_qs + B**: always add a source-of-number clause ("from Qto", "say gross or net", "if there's none say so").
- **facility_manager / owner_client + C**: asset words, not IFC words ("serial number", "does it have the data we asked for").
- **developer_programmer + E**: precise and short ("rename a pset across 40 files keeping guids"); may ask for code, which is a G1 no-file question.
- **bim_coordinator + D**: tolerance numbers, "hard only", "group by level", BCF for the author.
- **student_beginner + G**: "what is even in it", "which free viewer", over-polite is allowed here and nowhere else.

### 5.2 Persona x language (evidence limits)

| Combination | Status in the base | What to do |
|---|---|---|
| ru + bim_coordinator, architect, developer, bim_manager | real posts exist (dwg.ru, Habr, Telegram-derived cells) | write freely; keep RU slang |
| ru + estimator_qs, mep_engineer, facility_manager | no real Russian posts for these roles (style guide 13.1) | write as synthetic, modelled on `ru-s007`, `ru-eng-s009`, `en-fmor-s015` |
| ru + MCP-style prompts | no real Russian MCP prompt in the base (capability file, section 8) | modelled on EN / ZH patterns; mark synthetic |
| en + any persona | strong evidence, biased to GitHub / forums | keep plain; avoid forum-politeness unless R3 |
| zh + developer, architect, coordinator | real titles and blog posts (Zhihu, CSDN, GitHub) | use 查下 / 咋回事 / 求教 register for titles; plain imperative for prompts |
| es, de, ja + any persona | thin real evidence, good synthetic sets | short and plain; local role words (metrados, BGF, 積算) |
| pt, fr, ko, it, nl, no + any persona | no or very thin casual posts | short and plain; tag `unverified_style`; no invented slang |
| reviewer_authority + any language | formal everywhere | no slang; norm names (СП 333, IDS, 確認申請, ILS) |

---

## 6. Language hooks, and software / schema plausibility

### 6.1 Local hooks by language (use one, not five)

| Language | Standards, authorities, workflow words that appear in the base | Typical parameters / classifiers |
|---|---|---|
| ru | АГР (Moscow architectural council), государственная экспертиза, ЦИМ / ТИМ, СП 333, ТЭП, ВОР, КСИ, МССК, заказчик, IDS ЦГЭ (St Petersburg) | RUS_Area, RUS_Height, Марка, ФОП |
| en (UK) | ISO 19650, BEP, EIR, COBie, Uniclass | Uniclass codes |
| en (US) | feet, state DOT, OmniClass, LOD | feet / inches in units questions |
| en (SG, AU) | CORENET X (Singapore), IFC-SG | gateway submission |
| zh | 报审, SZ-IFC self-check (Shenzhen), GB/T, 翻模, 轻量化, 二开 | 房间编号, 面积 |
| es | metrados, presupuesto, ambientes, niveles, planbim MIDE (Chile) | m2 / m3 per nivel |
| de | AIA, BAP, LV, BGF, TGA, Projektbasispunkt, OKRD / OKFF levels | Geschoss, Tragend, Feuerwiderstand |
| ja | 確認申請, 積算 | 部屋名, 床面積 |
| pt-BR | SICLIC / ABNT NBR 15965, cronograma 4D, pavimento | classification codes |
| fr | indice B / C, cahier des charges BIM, RDC / R+1, maquette, synthèse | niveaux, altitudes |
| nl | ILS, NL-SfB, NAA.K.T., Bouwbesluit, RD coordinates, bouwlaag | begane grond |
| no | NS 3451, FDV, TFM, EUREF89 NTM | etasje, rom |
| it | capitolato informativo, rev A / B | piano, classificazione |
| ko | 물량, 공유좌표 | 층, 레벨 |

These were read from records and reference pages in the base (see [language pages](../05_real_world_questions/by_language/ru.md) and the [multilingual glossary](../08_glossary/glossary_multilingual.md)); verify a hook there before building a whole prompt around it.

### 6.2 IFC schema plausibility (do not ask a schema for something it does not have)

| Feature a prompt may rely on | IFC2x3 | IFC4 | IFC4.3 | Rule for generated prompts |
|---|---|---|---|---|
| `IfcMapConversion` + `IfcProjectedCRS` | not in the schema; people use `IfcSite` lat / long or a property set | yes | yes | With a 2x3 file ask "where is the site, any coordinate pset", not "MapConversion offsets" |
| Quantity set name | typically `BaseQuantities` | `Qto_<Class>BaseQuantities` | same | Do not insist on `Qto_WallBaseQuantities` for a 2x3 file |
| `IfcRoad`, `IfcBridge`, `IfcRailway`, reworked `IfcAlignment` | no | no | yes | Road / bridge prompts pair with IFC4.3 (or are an "IFC4X3 to 2x3" trap) |
| Reference View / Design Transfer View | no (Coordination View 2.0 is the 2x3 world) | yes | Reference View and Alignment-based View | "IFC4 RV" and "2x3 CV2.0" are the real shorthands |
| `IfcTask` schedule data in a file | possible | possible | possible | Rarely present in plain exports; "elements without a task" is a data-absent trap |
| IFC5 / ifcx | no | no | no | Only developers and researchers; label as draft |

Sources inside the base: [IFC versions](../01_ifc_basics/01_what_is_ifc_and_versions.md), [properties and quantities](../01_ifc_basics/05_properties_quantities_psets.md), [geometry and coordinates](../01_ifc_basics/06_geometry_placement_coordinates_units.md), [4D/5D/FM domains](../01_ifc_basics/08_domains_mep_structural_infra_4d5d_fm.md). Some details there are marked unverified.

### 6.3 Revit-only vocabulary

"Link IFC", "Export to IFC" parameter, `IfcExportAs`, mapping tables, Project Base Point / Survey Point, "family", "category", "phase", "workset" exist only in Revit. They are fine in a request **about Revit** (E1, E3, G2 import problems) and for a non-expert applying Revit words to an IFC (a deliberate loose-term trap). They are implausible from Archicad, Tekla or Renga users, who have their own words.

---

## 7. Designing fair tests and probes (server gate)

Use the last column of T4 plus this table. A request is **fair** if the target server group appears there; otherwise it is a **probe**. Both are useful; label them.

| Probe type | Roll that creates it | Expected honest behaviour | Source of the weakness |
|---|---|---|---|
| Missing tool | T4 intent not served by the target group (clash on a plain IFC reader, IDS on a Revit bridge, screenshot on a reader) | "I have no tool for this"; offers what it can do | capability matrix, [section 3.1](what_ifc_mcp_servers_do.md) |
| Write on read-only | E1 / E2 / E3 on groups 1a, or in `look_only` mode | Names the mode or limitation; no pretended edit | capability file L5, L18-L20 |
| Data absent | T3 topic 17, 18, 20 (4D, classification, COBie) with no such data in the file | "Not in the model"; no guessed value | L7, L10 |
| Loose term | T11 loose-term flag with "family", "category", "level" | Resolves or asks; says IFC has types, not families | L9 |
| Impossible constraint | "nothing lost", "100% pass", "all of it in one go" | Names what cannot be kept; refuses to promise | `en-vm-s015`, `zh-vm-s006` as cited in the capability file |
| Unknowable | "will it pass", "is it good", "remember what we agreed" | Does not claim approval or memory | capability file section 4.3 |
| Wrong state | "list all pipes" with no Revit document open | Clear "not connected / no active document" | L1, `en-aimcp-r020` |
| Heavy file | F3 or any query on a 500 MB to 2 GB IFC | Warns, chunks, or reports the timeout; no duplicate writes on retry | L3 |

**Safe batch mix:** about 70% fair, 10% limit probes (rows 1, 2, 7, 8), 12% honesty traps (rows 3-6), 8% knowledge / no-file.

---

## 8. Implausible combinations to avoid, and rejected-roll examples

### 8.1 Rules of thumb

| Implausible | Why | Repair |
|---|---|---|
| Owner or facility manager pasting STEP lines or naming `Pset_DoorCommon.FireRating` | They speak in business words ("fire rating", "serial number") | Move exact tokens to coordinator, developer or manager |
| Developer asking "what is IFC" | Role mismatch | Make it a student; or turn into a precise API question |
| Student running IDS validation in slang | Beginners do not have IDS files | G1 / A1 question instead |
| Reviewer from an authority using slang or "!!!" | Formal persona | Plain formal imperative with the norm name |
| Estimator asking for clash detection | Not their job | Quantity change between versions (D1 with quantities) |
| FM asking for GUID-level diff | Not their vocabulary | "what changed in the room list" |
| Contractor asking about the IfcOpenShell API | Not their tool | Developer or BIM manager |
| IFC2x3 + `IfcMapConversion`; IFC2x3 + `IfcRoad` | Not in that schema | See 6.2 |
| English prompt about Renga / nanoCAD | Rare in the base | Reroll tool or language |
| Revit-only words from an Archicad user | Wrong vocabulary | Use the persona's own tool words |
| Politeness stack ("could you kindly...") typed to an assistant | 93% to 100% of typed prompts have no "please" | Drop it |
| Full version stack ("Revit 2024.2, exporter 24.2.0, IFC4 RV") | Context is partial in real posts | One item |
| "Check my model" with nothing else | Real vagueness still names an observable | Add the observable ("half my walls came out grey") |
| Round tidy numbers everywhere (100 elements, 50%) | Real numbers look measured | 212 doors, 0.5 m2, 480 MB |
| Slip inside the key token | Tests luck, not the assistant | Move the slip |
| A named real company or project | No personal or company-internal details | Generic names (Колонна_*, Level 02) |

### 8.2 Eight rejected rolls (and the repair)

| # | Rolled combination | Why rejected | Repair |
|---|---|---|---|

| 1 | P owner_client + I E3 batch_automation + T20 programming | An owner does not script batch jobs; the vocabulary will sound invented. | Keep the topic, switch persona to developer_programmer, or keep the persona and switch intent to B2 ('give me a list I can send to the contractor'). |
| 2 | V IFC2x3 + I A5 asked as 'IfcMapConversion offsets' | IfcMapConversion / IfcProjectedCRS belong to IFC4 and later; in 2x3 people use IfcSite latitude / longitude or a property set. | Raise V to IFC4, or rewrite the ask as 'where is the site, lat / long, any coordinate pset'. |
| 3 | L en + S Renga | Renga and nanoCAD questions in the base are in Russian-language sources; an English prompt about them is possible but rare. | Reroll S, or reroll L to ru. |
| 4 | P student_beginner + I C2 (IDS) + R3 paragraph + slang | Beginners do not run IDS checks, and slang plus a long paragraph clash with the beginner voice (low slang, over-polite). | Reroll I to G1 / A1, or the persona to bim_manager. |
| 5 | Server 1a (read-only IFC reader) + I E2 create_elements, flag fair | The server cannot write; as a fair test it would be unfair. | Mark as probe (trap = true, expected: honest refusal) or reroll the intent to a read intent. |
| 6 | E 'URGENT!!!' + P reviewer_authority | Formal persona; shouting is theatrical (about 1% of real titles carry '!'). | Express urgency as a deadline in plain words ('до конца дня', 'by Friday'). |
| 7 | R4 fragment + I C2 (needs an IDS file) | A 4-word fragment cannot carry 'against the attached IDS' and still read natural. | Reroll R to R1, or reroll the intent to C1. |
| 8 | X slip inside the key token ('FireRaiting', 'Pset_WallComon') | The test would measure luck, not the assistant. | Move the slip to a non-key word, or drop it. |

---

## 9. Thirty worked examples

All requests are **synthetic** (written for this file, modelled on the records named under "Why it works"). The rolls are chosen to show variety, not drawn at random; in real use roll honestly. Language mix here: ru 7, en 8, zh 3, es 2, de 2, ja 2, pt 1, fr 1, ko 1, it 1, nl 1, no 1. Gloss is given for non-English prompts. `expected_behavior` is short here; in a real batch write it in full.

Roll codes: **L** language | **P** persona | **topic** = cluster number of T3 | **I** intent | **S** software | **V** schema stated | **C** context items | **R** register | **E** emotion | **X** slip | **F** flags.


**#1 - ru - mep_engineer** (difficulty medium, needs_file true)
- Rolls: `L ru | P mep_engineer | topic 11 | I B1 | S none | V not stated | C 1 item | R1 | E neutral | X none | F honesty`
- Request (synthetic): `по системам вентиляции: сколько воздуховодов и общая длина. у кого системы нет - отдельной строкой`
- English gloss: By ventilation system: how many ducts and the total length. Those with no system - on a separate row.
- Expected behavior: Group IfcDuctSegment by system membership (IfcSystem / distribution system), count and sum Length with the quantity source stated; add a 'no system' row with count and length. Do not invent systems from element names. Read-only.
- Why it works: Real-style MEP ask in a Russian engineer's voice (the base has no real Russian MEP posts, so this is modelled on synthetic `ru-eng-s009` and the English MEP cell). Follow-up possible: 'а теперь только 3 этаж'.

**#2 - ru - architect** (difficulty medium, needs_file true)
- Rolls: `L ru | P architect | topic 9 | I G2 | S Revit 2025 | V not stated | C 2 items (size, other viewer) | R2 | E confused | X lowercase product | F evidence move`
- Request (synthetic): `открыл ифс от конструкторов в ревите 2025, одни оси, остального нет. файл 90 мб. в бимвижне всё на месте`
- English gloss: Opened the structural engineers' IFC in Revit 2025: only grids, nothing else. File is 90 MB. In BIM Vision everything is there.
- Expected behavior: Check the IFC independently of Revit: schema, counts by class, share of elements with a geometric representation, bounding box and distance from the origin, units. If the file looks healthy say the cause is probably on the import / link side (phase, view, placement) and do not claim to know Revit's behaviour. Read-only.
- Why it works: Cross-check-in-another-viewer is the most habitual evidence move (style guide 4.3); 'только оси' is a documented complaint (synthetic `ru-autodesk-telegram-s013`).

**#3 - ru - estimator_qs** (difficulty hard, needs_file true)
- Rolls: `L ru | P estimator_qs | topic 3 | I B2 | S none | V not stated | C 1 item (destination) | R1 | E neutral | X none | F format + honesty`
- Request (synthetic): `ведомость дверей по типам и этажам: ширина, высота, количество. размеры из Qto, нет Qto - оставь пустым, не считай сам. для сметы`
- English gloss: Door schedule by type and storey: width, height, count. Dimensions from Qto; if no Qto leave blank, do not compute yourself. For the estimate.
- Expected behavior: Group IfcDoor by type name and storey; take width and height only from the door Qto set; leave blanks where absent and report how many; state the source. Must not fill blanks from geometry or from the OverallWidth / OverallHeight attributes (the user forbade it); may mention that the attributes exist.
- Why it works: Estimators ask for tables and for the source of each number; the 'do not compute' clause is the honesty dial.

**#4 - ru - reviewer_authority** (difficulty medium, needs_file true)
- Rolls: `L ru | P reviewer_authority | topic 7 | I C2 | S none | V IFC4 | C 0 items | R1 | E neutral | X none | F format + safety`
- Request (synthetic): `прогони модель по приложенному IDS, нарушения сверни по классам, частые сверху. без правок`
- English gloss: Run the model against the attached IDS, roll the violations up by class, most frequent first. No edits.
- Expected behavior: Needs an IDS file loaded and an IDS-capable tool (1b IFC toolkits, Horizun). If either is missing, say so and do not improvise rules. Otherwise report PASS / FAIL per specification and failures per entity class sorted by count. No edits.
- Why it works: Formal persona, so low roughness and no slang. A server gate probe: on a plain IFC reader the right answer is an honest 'no IDS tool' (mark `server_gate: probe`). Real IDS batch-checking context: `ru-autodesk-telegram-r012`.

**#5 - ru - bim_coordinator** (difficulty hard, needs_file true)
- Rolls: `L ru | P bim_coordinator | topic 15 | I D2 | S none (server: Navisworks / Revit bridge) | V not stated | C 2 items (threshold, grouping) | R2 | E neutral | X none | F format`
- Request (synthetic): `ОВ против КР, только жёсткие, допуск 10 мм, сгруппируй по этажам и дай пять самых плотных мест`
- English gloss: HVAC against structure, hard clashes only, tolerance 10 mm, group by storey and give the five densest spots.
- Expected behavior: Needs a clash tool. If present: run the two disciplines, hard only, 10 mm tolerance, group by storey, return top-5 clusters with counts and element ids, and say how pairs of the same two elements were collapsed. If absent: honest refusal (probe).
- Why it works: 'ОВ' (heating and ventilation) and 'КР' (structural design) are Russian discipline abbreviations; tolerance and 'hard only' are habitual (`en-allplan-vw-bentley-s011`).

**#6 - ru - facility_manager** (difficulty medium, needs_file true)
- Rolls: `L ru | P facility_manager | topic 17 | I C1 | S none | V not stated | C 1 item (motive) | R1 | E urgency (week) | X none | F because`
- Request (synthetic): `у всего оборудования есть серийник и производитель? эксплуатация принимает на этой неделе, нужен список чего нет`
- English gloss: Does all equipment have a serial number and a manufacturer? Operations takes over this week, I need a list of what is missing.
- Expected behavior: Select equipment elements, check serial number and manufacturer wherever they live (occurrence or type property sets, attributes), say where it looked, and list the elements missing each, with totals. Missing means 'not filled', not 'unknown manufacturer'.
- Why it works: FM / owner voices use asset words and few IFC terms (persona pages); handover pressure is the because-clause. Evidence: synthetic `en-fmor-s015`.

**#7 - ru - student_beginner** (difficulty easy, needs_file false)
- Rolls: `L ru | P student_beginner | topic 16 | I G1 | S none | V n/a | C 0 items | R1 | E curious | X none | F format`
- Request (synthetic): `чем бесплатно открыть ифс чтоб свойства смотреть? без регистрации желательно`
- English gloss: What can I open an IFC with for free to look at properties? No registration, ideally.
- Expected behavior: Knowledge answer (no file needed): name a few free viewers and say which show properties, without claiming exact feature lists it cannot verify; may offer to read properties from the file that is already loaded.
- Why it works: Close to synthetic `ru-autodesk-telegram-s014`; tool-finding is a very common beginner ask.

**#8 - en - civil_infra_engineer** (difficulty hard, needs_file true)
- Rolls: `L en | P civil_infra_engineer | topic 18 | I A5 | S none | V IFC4.3 | C 1 item (schema) | R1 | E light politeness | X none | F format`
- Request (synthetic): `is the road model in the right CRS? epsg code + offset from origin pls`
- Expected behavior: Read IfcProjectedCRS (name, EPSG) and IfcMapConversion (eastings, northings, height, rotation) and the bounding-box offset in file units. If absent, say the model has no georeference. 'Right' cannot be judged without the project's required CRS: ask for it; do not infer a CRS from coordinates.
- Why it works: 'Right CRS' hides a missing requirement, which is the trap; Norwegian synthetic `no-norway-s005` asks the same about EUREF89 NTM.

**#9 - en - bim_coordinator** (difficulty medium, needs_file true)
- Rolls: `L en | P bim_coordinator | topic 5 | I C1 | S none | V not stated | C 2 items (count mismatch, BEP) | R1 | E skeptical | X none | F format`
- Request (synthetic): `bep says 8 levels, this model has way more. list storeys w/ elevation + how many elements on each, flag the empty ones`
- Expected behavior: List every IfcBuildingStorey with name, elevation (unit stated) and contained-element count; flag storeys with zero elements; note elements related only through aggregation. Do not decide which storeys are 'extras' without the BEP list; may suggest candidates (empty, duplicate elevation).
- Why it works: Storey-count mismatch with a BEP is a documented coordinator problem (`en-blogs-linkedin-s002`). Follow-up possible: 'which of those have no walls at all'.

**#10 - en - structural_engineer** (difficulty easy, needs_file true)
- Rolls: `L en | P structural_engineer | topic 12 | I A2 | S Tekla | V not stated | C 1 item (source tool) | R1 | E neutral | X none | F lopsided`
- Request (synthetic): `steel model from tekla: how many IfcColumn vs IfcBeam vs IfcMember, and anything left as proxy?`
- Expected behavior: Count by class (IfcColumn, IfcBeam, IfcMember), count proxies and show what their names look like; read-only. May note that steel parts can legitimately appear as IfcMember or IfcPlate depending on the exporter.
- Why it works: Tekla IFC complaints are well documented in the structural cell; exact class names are normal for this persona.

**#11 - en - contractor_site** (difficulty medium, needs_file true)
- Rolls: `L en | P contractor_site | topic 3 | I A3 | S none | V not stated | C 1 item (motive) | R1 | E urgency | X none | F because`
- Request (synthetic): `how many walls, slabs and columns are on level 3? planning tomorrow's pour`
- Expected behavior: Resolve 'level 3' against the storey names (Level 3 / L03 / 03; if ambiguous list the candidates and ask), count IfcWall, IfcSlab, IfcColumn assigned to it, and note elements without any storey assignment. No volume claims unless asked.
- Why it works: Site people ask 'what is on level N'; the name-resolution step is the hidden test (capability file L9).

**#12 - en - developer_programmer** (difficulty medium, needs_file false)
- Rolls: `L en | P developer_programmer | topic 20 | I G1 | S none | V not stated | C 2 items (count, tool) | R1 | E neutral | X none | F loose`
- Request (synthetic): `need to rename a custom pset across ~40 ifc files w/ ifcopenshell, keep guids. is there a clean way or do i have to rewrite every pset`
- Expected behavior: Knowledge answer, no model needed: iterate files, find the pset by name on occurrences and types, rename or recreate it, save to new files; GlobalIds stay because only the pset entity changes. Recommend a dry-run count first and a read-back. A code sketch must be labelled untested and must not invent API names.
- Why it works: Developers are the second largest persona in the base (825 records); the 'rename a pset' task is typical (synthetic `en-beginner-qa-s010`).

**#13 - en - owner_client** (difficulty hard, needs_file true)
- Rolls: `L en | P owner_client | topic 19 | I C4 | S none | V not stated | C 0 items | R1 | E confused | X none | F trap (missing requirement source)`
- Request (synthetic): `does this model have what we asked for in the EIR? dont have the exact list, just tell me if anything big is missing`
- Expected behavior: Must ask for or locate the EIR requirements; without them compliance cannot be verified. May run a generic completeness scan (storeys, spaces, classes, materials, classification, share of proxies, property sets filled) and list gaps as 'common expectations', never as EIR compliance.
- Why it works: Owners do not have the list; the right behaviour is to say so (probe). Contract-term cell: `contracts_bep_eir_loin` topic.

**#14 - en - bim_manager** (difficulty medium, needs_file false)
- Rolls: `L en | P bim_manager | topic 8 | I G1 | S Revit 2024 | V not stated | C 3 items | R3 | E urgency through a deadline | X none | F because + two-part`
- Request (synthetic): `Hi, quick one. We export from Revit 2024 and the contractor (solibri + navis) asks for IFC but does not say which version, and our EIR says nothing either. Is 2x3 coordination view still the safe choice or should we go IFC4 reference view? Dont want a rejected delivery on friday`
- Expected behavior: Knowledge answer: the choice depends on the EIR and the receiving tools; explain Coordination View (2x3) versus Reference View (IFC4) in plain words; do not assert what the contractor's tools support beyond what it can verify; recommend asking for the requirement in writing; may read the loaded file's schema.
- Why it works: 'Which IFC version to send' is a standing question (`versions_mvd`, 215 records); the forum-style register (R3) is the 10% slot.

**#15 - en - mep_engineer** (difficulty medium, needs_file true)
- Rolls: `L en | P mep_engineer | topic 11 | I C3 | S none | V not stated | C 1 item | R1 | E neutral | X none | F two-part`
- Request (synthetic): `cable trays in this ifc, are they proper cable carrier segments or proxies? count them and say what system they belong to`
- Expected behavior: Count IfcCableCarrierSegment (and fittings) versus proxies whose names look like trays; report system membership; if the exporter used proxies, show the names. Read-only.
- Why it works: Class-or-proxy is the commonest MEP export doubt (`en-autodesk-revit-export-s008`).

**#16 - zh - bim_coordinator** (difficulty hard, needs_file true)
- Rolls: `L zh | P bim_coordinator | topic 4 | I A5 | S none | V not stated | C 1 item | R1 | E confused | X none | F two files`
- Request (synthetic): `两个专业的ifc对不上 查下各自的原点和单位 感觉一个是mm一个是m`
- English gloss: The IFCs of two disciplines don't line up. Check each one's origin and units. I feel one is mm and one is m.
- Expected behavior: Needs two files. For each: length unit, IfcSite placement, IfcMapConversion if present, bounding-box offset; compare after unit conversion. Do not conclude 'mm versus m' without the numbers.
- Why it works: Models that do not line up is the top coordinator pain (`coordinates_georef` 272 records); style modelled on `zh-coord-s008`.

**#17 - zh - estimator_qs** (difficulty medium, needs_file true)
- Rolls: `L zh | P estimator_qs | topic 3 | I B1 | S none | V not stated | C 0 items | R1 | E neutral | X none | F honesty`
- Request (synthetic): `按楼层统计墙体混凝土方量 没有工程量属性的单独列出来`
- English gloss: Total wall concrete volume per floor; list separately those without quantity properties.
- Expected behavior: Identify concrete walls (say how: material name or layer), sum NetVolume per storey from Qto, list walls without Qto separately with a count, and state the uncertainty of identifying concrete by name.
- Why it works: Short, no greeting, the 'list the missing ones separately' clause is the honesty dial.

**#18 - zh - student_beginner** (difficulty medium, needs_file true)
- Rolls: `L zh | P student_beginner | topic 16 | I F1 | S none | V not stated | C 1 item (size) | R1 | E curious | X none | F loose term`
- Request (synthetic): `100多M的ifc想轻量化给网页用 转glb属性会丢吗`
- English gloss: I want to 'lightweight' a 100+ MB IFC for the web. If I convert to GLB, will properties be lost?
- Expected behavior: Explain that GLB keeps geometry and structure but normally not IFC properties, so keep GlobalId as a key to a separate property table; if a conversion tool exists, run it and report sizes; do not promise what it has not checked. '轻量化' means making it viewable, not deleting data.
- Why it works: Grounded in a real Chinese record: IfcConvert merges parts and drops ids, so GlobalId must be written separately (`zh-csdn-dev-r002`).

**#19 - es - architect** (difficulty easy, needs_file true)
- Rolls: `L es | P architect | topic 6 | I A2 | S Archicad | V not stated | C 1 item (source tool) | R1 | E neutral | X dropped accents | F loose term`
- Request (synthetic): `los ambientes del ifc de archicad: cuantos hay por nivel y cuales no tienen area`
- English gloss: The 'ambientes' (rooms) of the Archicad IFC: how many per level and which have no area.
- Expected behavior: Count IfcSpace per storey ('ambientes' = spaces) and list those with no area quantity. Do not claim exporter-specific behaviour.
- Why it works: 'Ambientes' is Latin American room vocabulary; the missing accents are the one slip.

**#20 - es - contractor_site** (difficulty hard, needs_file true)
- Rolls: `L es | P contractor_site | topic 3 (4D links) | I C1 | S none | V not stated | C 1 item (motive) | R1 | E neutral | X none | F trap (data likely absent)`
- Request (synthetic): `elementos del nivel 2 sin tarea asignada en el cronograma, los necesito para el 4D`
- English gloss: Elements of level 2 with no task assigned in the schedule; I need them for the 4D.
- Expected behavior: Check whether the file carries schedule data (tasks and their assignments). If it does not, say so plainly (most exports do not) and offer to list the level-2 elements for linking elsewhere; do not invent a schedule.
- Why it works: Planned-versus-modelled links rarely exist in a plain export, so honest 'not in the file' is the expected answer; modelled on `pt-s010`.

**#21 - de - estimator_qs** (difficulty hard, needs_file true)
- Rolls: `L de | P estimator_qs | topic 3 | I B1 | S none | V not stated | C 0 items | R1 | E neutral | X none | F source clause`
- Request (synthetic): `BGF je Geschoss aus der IFC ziehen. steht die Fläche in den Spaces oder in den Geschossen? sag welche Quelle du nimmst`
- English gloss: Pull the gross floor area per storey from the IFC. Is the area stored in the spaces or in the storeys? Say which source you use.
- Expected behavior: Compare the storey quantity set (gross / net floor area) with the sum of IfcSpace areas, state which source was used and why, and flag differences. Missing quantities are reported, not computed silently.
- Why it works: Source-of-quantity questions are an estimator habit (`de-dach-s007`); 'BGF' is the German short form for gross floor area.

**#22 - de - mep_engineer** (difficulty hard, needs_file true)
- Rolls: `L de | P mep_engineer | topic 11 | I C1 | S none | V not stated | C 2 items | R1 | E neutral | X none | F format`
- Request (synthetic): `welche Rohre in der TGA-IFC gehören zu keinem System? Liste mit Geschoss und Länge, nur Abwasser`
- English gloss: Which pipes in the MEP IFC belong to no system? List with storey and length, wastewater only.
- Expected behavior: Find IfcPipeSegment without system membership, identify 'wastewater' by system name or predefined type and say how, list with storey and length (source stated). If wastewater cannot be identified, say so rather than guess.
- Why it works: 'TGA' (technical building services) is the DACH engineer word; the identification of 'Abwasser' is the hidden step.

**#23 - ja - bim_coordinator** (difficulty hard, needs_file true)
- Rolls: `L ja | P bim_coordinator | topic 14 | I D1 | S none | V not stated | C 1 item (time ref) | R1 | E neutral | X none | F two files + history clause`
- Request (synthetic): `先週と今週のIFCで消えた部材だけ出して。GlobalIdが変わってたら名前と位置で突き合わせて`
- English gloss: Show only the elements that disappeared between last week's and this week's IFC. If GlobalIds changed, match by name and position.
- Expected behavior: Needs two files. Removed by GlobalId first; for ids that vanished, try a fallback match on name, type and placement and report those separately with their confidence. Counts by class.
- Why it works: GUID churn is a recurring problem (`guid_change_tracking`, 158 records); plain imperative, no keigo.

**#24 - ja - structural_engineer** (difficulty hard, needs_file true)
- Rolls: `L ja | P structural_engineer | topic 1 | I E1 | S none | V not stated | C 0 items | R1 | E neutral | X none | F safety clause`
- Request (synthetic): `プロキシのうち名前に「柱」が入ってるものをIfcColumnに変えて。元ファイルは触らずコピーで`
- English gloss: Change the proxies whose name contains 柱 (column) to IfcColumn. Do not touch the original file, work on a copy.
- Expected behavior: Select IfcBuildingElementProxy by name match, list the matches first, change the class only in a copy, keep GlobalIds and property sets, report the changed count and the proxies left unmatched, and read back. If the server cannot write, say so. Must not touch the original and must not change proxies that do not match.
- Why it works: Re-classing proxies by name is a recurring wish (synthetic `ru-autodesk-telegram-s009`, `ko-korea-s007`, `it-italy-s009`); over-broad edits are a known failure (capability file L20).

**#25 - pt - estimator_qs** (difficulty medium, needs_file true)
- Rolls: `L pt | P estimator_qs | topic 3 | I B1+B2 | S none | V not stated | C 1 item (motive) | R1 | E urgency | X none | F two-part + because`
- Request (synthetic): `quantas portas por pavimento e qual a area total de piso por pavimento? pra planilha, preciso hoje`
- English gloss: How many doors per storey and what is the total floor area per storey? For a spreadsheet, I need it today.
- Expected behavior: Count IfcDoor per storey; floor area per storey from the storey quantity set or the sum of IfcSpace areas (source stated); give a table ready for a spreadsheet. Style is unverified (no real Portuguese posts in the KB).
- Why it works: Two piggy-backed questions (1 in 5 requests); Brazilian 'pavimento' for storey.

**#26 - fr - bim_manager** (difficulty hard, needs_file true)
- Rolls: `L fr | P bim_manager | topic 5 | I E3 | S none | V not stated | C 0 items | R1 | E neutral | X none | F safety clause`
- Request (synthetic): `renomme les niveaux selon leur altitude: RDC, R+1, R+2... mais montre-moi la liste avant et travaille sur une copie`
- English gloss: Rename the levels according to their elevation: RDC, R+1, R+2... but show me the list first and work on a copy.
- Expected behavior: List storeys with current names and elevations and a proposed old-to-new table; do not guess which storey is the ground floor (RDC) without asking or stating the rule used; check duplicate names and non-monotonic elevations; apply only to a copy after the user has seen the list; read back. If the server cannot write, give the mapping table only. Style is unverified (no real French posts in the KB).
- Why it works: Level-naming conventions are a French BIM-manager concern (`fr-francophone-s004`); the 'show me the list first' clause tests the preview step (capability file L18).

**#27 - ko - bim_coordinator** (difficulty easy, needs_file true)
- Rolls: `L ko | P bim_coordinator | topic 1 | I A2 | S none | V not stated | C 0 items | R1 | E neutral | X none | F loose term`
- Request (synthetic): `이 ifc에서 proxy로 나온 것들 층별로 몇 개인지 알려줘`
- English gloss: Tell me how many of the items that came out as proxy there are per floor in this IFC.
- Expected behavior: Count IfcBuildingElementProxy per storey and give the total; read-only. Style is unverified (no real Korean casual posts in the KB).
- Why it works: Latin 'proxy' inside Korean is the natural pattern.

**#28 - it - bim_manager** (difficulty medium, needs_file true)
- Rolls: `L it | P bim_manager | topic 17 | I C1 | S none | V not stated | C 1 item (destination) | R1 | E neutral | X none | F format`
- Request (synthetic): `ci sono elementi senza classificazione? lista per classe IFC, ci serve per il capitolato`
- English gloss: Are there elements without a classification? List by IFC class; we need it for the information requirements document.
- Expected behavior: Find elements with no IfcClassificationReference, group by IFC class with counts, and say which classification systems exist in the file. Style thin: tag unverified_style.
- Why it works: 'Capitolato informativo' is the Italian EIR; based on `it-italy-s007`.

**#29 - nl - architect** (difficulty easy, needs_file true)
- Rolls: `L nl | P architect | topic 5 | I C1 | S none | V not stated | C 0 items | R4 | E neutral | X none | F fragment`
- Request (synthetic): `wanden zonder bouwlaag?`
- English gloss: Walls without a storey?
- Expected behavior: Find IfcWall not contained in any IfcBuildingStorey, list GlobalId and name, give the count. The fragment is deliberate: the object (walls) and the check (no storey) are both present.
- Why it works: Fragment register (5% of a batch); Dutch uses 'bouwlaag' for storey (`nl-dutch-s004`).

**#30 - no - facility_manager** (difficulty easy, needs_file true)
- Rolls: `L no | P facility_manager | topic 6 | I B2 | S none | V not stated | C 1 item (destination) | R1 | E neutral | X none | F format`
- Request (synthetic): `list alle rom med areal og etasje, de uten areal nederst. skal inn i FDV-lista`
- English gloss: List all rooms with area and floor, those without area at the bottom. It goes into the FDV list.
- Expected behavior: List IfcSpace with name, area (source stated) and storey; rows without area last, with a count. Style thin (Norwegian synthetic only).
- Why it works: FDV (operations and maintenance documentation) is the Norwegian handover word (`no-norway-s006`).

### 9.1 Coverage of the thirty


- Intent families: A 6, B 6, C 9, D 2, E 2, F 1, G 4.
- Difficulty: easy 6, hard 11, medium 13.
- Registers: R1 26, R2 2, R3 1, R4 1 (a real batch should be nearer 60 / 25 / 10 / 5 per cent).
- Probe-like (a refusal or a caveat may be the right answer): #4 (IDS tool may be missing), #5 (clash tool may be missing), #8 (required CRS unknown), #13 (EIR list missing), #20 (schedule data probably absent); partly #3 and #17 (blank / separate-list clauses), #22 (identifying wastewater).
- Write intents are under-represented here (E1 #24, E3 #26: 2 of 30) because a write request needs a safety clause and a server that can write; the prompt keeps the 12% target, and the few-shot block in [llm_generation_prompt.md](llm_generation_prompt.md) has one more (#5 there).
- Needs two files: #16, #23. Needs no file: #7, #12, #14.

---

## 10. Batch-level balance (check after rolling, before writing)

| Check | Target for a batch of 20-30 | Why |
|---|---|---|
| No persona above 25%; at least 3 of every 10 non-expert (student, owner, FM, architect, contractor, estimator) | by T2 | Records are dominated by coordinators and developers (1,775 of 3,592) |
| English not above about 35% unless asked | by T1 | The base is 68% English by record count |
| Russian and English together about half; the other languages each at least once per 30 | by T1 | Task requirement: Russian and English richest, the rest represented |
| Register near 60 / 25 / 10 / 5 | T8 | Style guide section 2.3 |
| Slips in about 1 of 4 | T10 | Style guide section 8.3 |
| Honesty clause in about 1 of 8 | T11 | Style guide section 16 |
| Follow-ups about 1 of 10, marked | T11 | Style guide section 11 |
| Trap or probe about 1 of 5 | T11 | Prompt mix |
| Write intents (E) about 12%, never more than 2 in a row | T4 | Real MCP issues are write-heavy, but real model-task prompts are about 89% read-only (capability file 4.4) |
| Each pain point of the top list appears at most twice | T3 | Avoid the 20 variations of "proxy count" problem |
| No two consecutive requests with the same opener or length | all | Anti-pattern AP15 |

---

## 11. Roll it with a script (optional)

Plain Python 3, no packages. The weights below are copied from the tables above (they are generated from the same data). Pass a seed to repeat a batch.

```python
import random, sys

T = {
"language": [("ru", 24), ("en", 26), ("zh", 9), ("es", 7), ("de", 6), ("ja", 6), ("pt", 4), ("fr", 4), ("ko", 3), ("it", 4), ("nl", 3), ("no", 2), ("other (tr, ar, vi, sk, cs, el, da)", 2)],
"persona": [("bim_coordinator", 18), ("architect", 14), ("bim_manager", 10), ("estimator_qs", 9), ("student_beginner", 9), ("structural_engineer", 7), ("mep_engineer", 7), ("developer_programmer", 5), ("facility_manager", 5), ("owner_client", 4), ("contractor_site", 4), ("reviewer_authority", 4), ("civil_infra_engineer", 3), ("researcher_academic", 1)],
"topic": [("1 Class mapping, proxies, Revit export classes", 8), ("2 Property sets and parameters missing", 8), ("3 Quantities, cost, BoQ, 4D / 5D links", 7), ("4 Coordinates, georeference, units", 7), ("5 Levels, storeys, spatial structure", 6), ("6 Spaces, rooms, zones, areas", 5), ("7 Validation, IDS, model checking", 7), ("8 IFC versions, views (MVD), schema choice", 5), ("9 Import / link into Revit, viewers, 'opens empty'", 5), ("10 Geometry: openings, curtain walls, stairs, railings", 5), ("11 MEP systems", 4), ("12 Structural, rebar, steel", 3), ("13 Materials, colours, types vs instances", 4), ("14 GUIDs, change tracking, compare", 4), ("15 Clash, BCF, CDE", 4), ("16 File size, performance, conversion", 4), ("17 Classification, COBie, FM handover", 4), ("18 Infrastructure, IFC4.3, site, GIS", 3), ("19 National rules, permits, contracts", 4), ("20 Programming, automation, AI / MCP itself", 3)],
"intent": [("A1 model_overview", 4), ("A2 inventory_count", 8), ("A3 spatial_navigation", 4), ("A4 property_lookup", 6), ("A5 coordinates_units", 6), ("B1 quantity_takeoff", 7), ("B2 data_report_export", 4), ("C1 completeness_check", 7), ("C2 rule_validation", 5), ("C3 mapping_geometry_audit", 4), ("C4 regulation_check", 3), ("D1 version_diff", 5), ("D2 clash_coordination", 4), ("E1 edit_data", 5), ("E2 create_elements", 3), ("E3 batch_automation", 4), ("F1 convert_exchange", 4), ("F2 visualize_view", 2), ("F3 optimize_performance", 3), ("G1 explain_howto", 4), ("G2 troubleshoot_diagnose", 6), ("G3 tool_meta", 2)],
"software_named": [("no software named", 60), ("a tool named, no version", 20), ("Revit year named", 20)],
"tool": [("Revit (then roll the year)", 44), ("Archicad", 10), ("Solibri", 8), ("Bonsai / BlenderBIM / Blender", 7), ("Tekla (Structures)", 6), ("Navisworks", 5), ("BIM Vision", 4), ("Allplan", 3), ("Renga", 3), ("Civil 3D", 2), ("BIMcollab / BCF tools", 2), ("Dynamo / pyRevit", 3), ("nanoCAD", 1), ("Vectorworks / Bentley / other", 2)],
"revit_year": [("2019 or older", 4), ("2020", 5), ("2021", 6), ("2022", 13), ("2023", 15), ("2024", 19), ("2025", 19), ("2026", 17), ("2027", 2)],
"schema_stated": [("not stated", 55), ("IFC4", 28), ("IFC2x3", 12), ("IFC4.3 / IFC4X3", 4), ("IFC5 / ifcx (draft)", 1)],
"context_items": [("0 items: only the ask + 'this model'", 25), ("1 item", 40), ("2 items", 27), ("3+ items (pasted detail, forum narrative)", 8)],
"register": [("R1 one line typed to the assistant", 60), ("R2 line + one pasted detail", 25), ("R3 forum-style paragraph", 10), ("R4 fragment", 5)],
"emotion": [("neutral imperative", 45), ("curious / how-to", 12), ("confused", 8), ("understated frustration", 12), ("urgency through a deadline", 13), ("skeptical / challenging", 5), ("light politeness", 4), ("dry sarcasm / fatigue", 1)],
"slip": [("no slip", 70), ("lowercase / casual casing of product or class ('revit', 'ifcwall', 'ifc')", 8), ("dropped accent / diacritic", 6), ("letter swap or doubled letter in a non-key word", 6), ("missing apostrophe or article", 5), ("run-on, no punctuation", 3), ("transliteration / mixed script", 2)],
}
FLAGS = [("because-clause (deadline or person waiting)", 33), ("loose or wrong term typical of the persona", 33), ("stated output format", 33), ("honesty / safety clause", 12), ("two-part request", 20), ("follow-up (script it, see the multi-turn prompt)", 10), ("trap or probe (any kind)", 22)]   # percent chance of "yes"

def pick(rng, rows):
    r = rng.randint(1, 100); acc = 0
    for label, w in rows:
        acc += w
        if r <= acc:
            return label

def roll(seed):
    rng = random.Random(seed)
    out = {k: pick(rng, rows) for k, rows in T.items()}
    for name, pct in FLAGS:
        out["flag: " + name] = rng.randint(1, 100) <= pct
    out["context_item_d12"] = [rng.randint(1, 12) for _ in range(
        {"0 items": 0, "1 item": 1, "2 items": 2}.get(out["context_items"].split(":")[0], 3))]
    return out

if __name__ == "__main__":
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 10
    seed = sys.argv[2] if len(sys.argv) > 2 else "demo"
    for i in range(n):
        print(i + 1, roll(f"{seed}-{i}"))
```

`tool` and `revit_year` are rolled every time; use them only when `software_named` says a tool (or a Revit year) is named, and use the context-item d12 values only as many times as `context_items` says. Run: `python roll.py 20 myseed`. Then give each rolled line to the generator ("write one request that matches these rolls"), or paste the whole list into the full prompt as "forced rolls". Reject and repair rolls with sections 5-8. Log for every request: seed, rolls, final prompt, repairs made. That log lets you see later whether failures cluster in one persona, language or topic.

---

## 12. Caveats and gaps

- **Weights are defaults, not truths.** They flatten known corpus biases and encode the style guide's recommended shares (which the guide itself calls derived, not measured).
- **The plausibility tables (5.1, 5.2, 6) are judgement.** They summarise the persona pages, language pages and cell reports; they were not tested against a held-out set of real prompts. If a combination in section 8 is rejected but you have seen it in real life, trust your observation and tell the maintainers.
- **No real MCP chat logs.** The strongest real MCP evidence is README example prompts and GitHub issues (cell `ai-mcp-usage`); most non-English MCP-style requests are inferred.
- **Evidence gaps by language:** Korean, French, Portuguese, Arabic, Italian, Dutch and Norwegian casual style is thin or absent; Spanish and German thin. Keep those prompts short and plain.
- **Some IFC details are marked unverified** in the base documents referenced in 6.2; the generator should not use them as a basis for an `expected_behavior` that gives numbers.
- **Intent codes** follow `intent_taxonomy.md` as described in the capability file; if that file changes its codes, update T4.

---

## 13. Related files

- [llm_generation_prompt.md](llm_generation_prompt.md): the ready-to-paste prompts (RU and EN) that consume these rolls.
- [intent_taxonomy.md](intent_taxonomy.md): the 22 intents A1-G3 with examples per language.
- [test_scenarios_library.md](test_scenarios_library.md): 156 scenario cards with assumed file states; [edge_cases_and_traps.md](edge_cases_and_traps.md): traps behind the "probe" rows of section 7; [prompt_bank_ru.md](prompt_bank_ru.md): Russian ready-made prompts.
- [what_ifc_mcp_servers_do.md](what_ifc_mcp_servers_do.md): server kinds and the capability matrix behind the server gate.
- [style guide](../06_how_people_write/style_guide.md), [anti-patterns](../06_how_people_write/anti_patterns_llm_questions.md), [jargon and slang dictionary](../06_how_people_write/jargon_slang_dictionary.md): the human-likeness rules behind T8-T10.
