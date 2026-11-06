# What IFC / BIM / Revit MCP servers actually do (for a tester with no BIM background)

**Compiled: 2026-11-06.** Sources: [MCP server catalog](../04_open_source/mcp_servers_and_ai_tools.md), [LLM + BIM research](../04_open_source/llm_bim_research_and_datasets.md), the two AI cells in `research_raw/wave1/ai/` ([ai-mcp-usage](../research_raw/wave1/ai/ai-mcp-usage.md), [ai-revit-tasks](../research_raw/wave1/ai/ai-revit-tasks.md)), and 3,525 research records read with `tools/kb.py` (1,036 of them are `model_task` prompts).
Companion file: [intent_taxonomy.md](intent_taxonomy.md) (what users ask, 22 intents). This file says **what the tools behind the assistant can and cannot do**, so you know which requests are fair to send and how to judge the answer.

> Evidence rules used here. "README says" means the project's own README as read on 2026-11-06; **nothing was installed or run**, so every capability below is a documented claim, not a verified fact. "Not documented" does not prove a tool is absent. Counts such as "245 tools" are vendor numbers and change with configuration.

---

## 1. MCP in plain words

**The problem.** A chat AI (Claude, ChatGPT, a local model) only sees the text you type. It cannot open `building.ifc` or look at your Revit window by itself. An IFC file is a large text database of building parts (walls, doors, rooms, pipes) and their data; Revit is a program that holds the same information in its own memory.

**MCP (Model Context Protocol)** is a standard "plug" that lets the AI call small helper programs. The pieces:

| Piece | What it is | Example |
|---|---|---|
| **Client** | The chat program you talk to | Claude Desktop, Claude Code, Cursor, ChatGPT desktop, a local-model UI |
| **MCP server** | A small program that offers a menu of *tools* | `ifcMCP`, `Bonsai_mcp`, `revit-mcp`, `tapir-archicad-MCP` |
| **Tool** | One function with a name and parameters | `get_entities`, `list_ifc_spaces`, `create_wall`, `send_code_to_revit` |
| **Backend** | Where the real data lives | an `.ifc` file read with the open-source IfcOpenShell library, or a running Revit/Blender/Archicad with an add-in |
| **Result** | Text the tool returns (JSON, counts, GlobalIds, sometimes a screenshot) | `{"IfcWall": 214, "IfcDoor": 38}` |

**What happens when you type "How many fire doors are on Level 2?"** (illustrative flow; tool names are real ones from the Daviidro `ifcopenshell-mcp` README, the exact arguments are invented):

1. The client sends your sentence plus the list of tool names and descriptions to the model.
2. The model decides to call a tool, e.g. `query_ifc_elements(type="IfcDoor", level="Level 2", property="FireRating")`.
3. The server runs real code on the real file and returns a list of doors with their values.
4. The model reads that list and writes the sentence you see ("8 doors, 5 of them EI30...").

**Three consequences a tester must keep in mind**

1. **The AI never "sees" the building.** It sees only what tools return. If no tool can read georeferencing, the model cannot answer a georeferencing question truthfully, however confident it sounds. Judge the *trace* (which tools were called, what came back), not only the final text. This mirrors the grading rule of the IFC-Bench benchmark, whose judge reads the execution trace ([research doc, section 4.1](../04_open_source/llm_bim_research_and_datasets.md)).
2. **Tool menus differ wildly.** Between 7 read-only tools and 245 Revit tools, or "191 commands behind 3 generic tools" (Tapir for Archicad). Check the menu first ([catalog, section 1](../04_open_source/mcp_servers_and_ai_tools.md)). Poor tool descriptions hurt too: one IfcOpenShell issue found 23 of 25 tools of an `ifcmcp` server had an empty description, so the model saw only names and argument schemas (<https://github.com/IfcOpenShell/IfcOpenShell/issues/8951>).
3. **Some tools can change things.** Reading is safe; creating, editing, deleting and "run this code" are not. The riskiest tool type is the code escape hatch (`send_code_to_revit`, `execute_blender_code`): the AI writes and runs arbitrary code inside the host program.

Not covered by MCP itself: the AI's accuracy, the IFC data quality, or what "correct" means in BIM. Those are what you test. Background words (GlobalId, Pset, IfcSpace, proxy, MVD, IDS, BCF) are in [abbreviations](../08_glossary/abbreviations.md) and [multilingual glossary](../08_glossary/glossary_multilingual.md); file structure in [IFC basics](../01_ifc_basics/02_ifc_file_anatomy.md).

---

## 2. Four kinds of server (pick the right test for each)

Kind numbers 1-4 and group labels 1a-4 are used in the matrix below; they are unrelated to the intent codes A1-G3 of the taxonomy.

| Kind | Needs a CAD program? | Can change the model? | Examples (README-reported) | Fair test requests |
|---|---|---|---|---|
| **1. IFC-file readers/toolkits** (groups 1a readers, 1b toolkits) | No. Takes a path to a `.ifc` | Mostly read-only; some can create/edit a *copy* | `smartaec/ifcMCP` (7 tools), `ekkodale/IFC-MCP` (7), `Daviidro/ifcopenshell-mcp` (8), `flinker-app/ifc-mcp`, `LTplus-AG/ifc-lite` (claims IFC2x3/4/4x3/5), `vinnividivicci/ifc-ids-mcp` (17 IDS tools), `BerkantACUN/ifc-ruhsat` (Turkish compliance) | counts, properties, spaces, quantities, missing data, diff of two files, IDS checks, GLB conversion |
| **2. Blender + Bonsai bridges** | Blender 4.x + Bonsai add-on, running | Yes (create/edit IFC in a live scene) | `JotaDeRodriguez/Bonsai_mcp` (15 IFC tools + code tool), `Show2Instruct/bonsai-mcp` (14), `ifc-bonsai-mcp` (~60) | read + create small things, screenshot of the viewport, georeference, BC3 budget; **IFC must be saved/open first** |
| **3. Authoring-app bridges** (3a Revit basic, 3b Revit guarded, 3c Archicad/Tekla/Navisworks) | Licensed Windows app + add-in running | Yes (the live project) | Revit: `mcp-servers-for-revit` (26 tools), `rvt-mcp` (58-245 depending on mode), Horizun (125), `aec-model-bridge`; Archicad: Tapir MCP; Tekla: `tekla_mcp_server`; Navisworks: `naviscoord-mcp` | ask about the **active view, levels, rooms, parameters, sheets**; guarded edits; clashes (Navisworks) |
| **4. Cloud / APS** | Autodesk cloud account and app registration | Mostly read-only | `aps-aecdm-mcp-dotnet` (7 tools), `aps-mcp-app-example` (viewer tools) | list hubs/projects/elements, isolate/colour in a viewer |

Mixing kinds is the commonest unfair test: do not ask a Revit server to "validate against IDS" (see the [Revit IFC export reference](../03_software/revit/ifc_export_reference.md) for why Revit is not IFC-native) or a read-only IFC reader to "add a wall". Of the model-task prompts in the corpus, about 77% mention IFC, so most test prompts fit kinds 1 and 2; the remaining ~23% are Revit-style (views, sheets, parameters) and fit kind 3.

---

## 3. Capabilities: the 15 building blocks

Codes K1-K15 are reused in [intent_taxonomy.md](intent_taxonomy.md).

| Code | Capability | Plain meaning | Typical real tool names (from READMEs) |
|---|---|---|---|
| K1 | Open / connect | Point the server at a file, or at the project currently open in Revit/Archicad | Daviidro: local `.ifc/.ifczip/.ifcxml`; Tapir: `discovery_list_active_archicads`; Revit: "active document" |
| K2 | List / count / filter elements | "How many walls", "all pipes", "doors on Level 2" | `get_entities`, `list_ifc_entities`, `query_ifc_elements`, `list_elements`, `ai_element_filter`, `analyze_model_statistics`, `analyze_building_inventory` |
| K3 | Read properties | Property sets (Psets), attributes, materials, classifications, types | `get_entity_properties`, `get_ifc_properties`, `get_element_properties`, `get_property_sets`, `get_psets` |
| K4 | Spatial tree and relations | Site > Building > Storey > Space, what contains what, openings in a wall | `get_ifc_spatial_structure`, `get_entities_in_spatial`, `get_ifc_relationships`, `get_openings_on_wall`, `get_space_boundaries`, `list_ifc_spaces`, `ifc_get_spatial_structure` |
| K5 | Quantities | Areas, volumes, lengths, counts (sums by storey/type) | `get_ifc_quantities`, `extract_ifc_quantities`, `get_quantities`, `get_material_quantities` |
| K6 | Coordinates, units, georeference | Where the model sits on Earth, units, origin | `get_ifc_georeferencing_info`, `georeference_ifc_model`, `get_entity_location` |
| K7 | Validate / IDS / rules | "Does it meet the requirements?" Schema check, IDS (machine-readable requirements), custom rules, PASS/FAIL/UNKNOWN | `validate_ifc_model`, `validate_ids`, `create_ids`, `run_rules`, `check_door_widths`, `yonetmelik_kontrolu`, `horizun_validate_ids` |
| K8 | Modify existing data | Change a property, class, storey assignment, name; colour elements | `operate_element`, `color_elements`, `update_wall`, `execute_ifc_code`, `horizun_apply_ifc_plan` |
| K9 | Create new elements/models | Walls, doors, storeys, whole small buildings, IFC5 drafts | `create_wall`, `place_ifc_object`, `create_point_based_element`, `create_level`, `ifcx_create_element` |
| K10 | Export data / reports | CSV/JSON/Excel, BC3 budget, BCF issues, PNG plan, "save IFC" | `export_ifc_data`, `export_bc3_budget`, `export_room_data`, `export_drawing_png`, `export_issues`, `save_ifc_file` |
| K11 | Convert formats | IFC to GLB/glTF/DWG, IFC2x3 vs IFC4, Revit to IFC | `convert_ifc_to_gltf`, `export_ifc` (Demolinator), `horizun_deliver_ifc`, ifc-lite conversion |
| K12 | Clash detection | Find parts that physically overlap | `detect_clashes` (shuotao), `check_clashes` (Demolinator), `naviscoord-mcp`, ifc-lite CLI |
| K13 | Compare / diff | What changed between two files or versions | `compare_ifc_models`, ifc-lite diff |
| K14 | Render / screenshot / viewer | See the model: viewport image, viewer window, apply a BCF viewpoint | `get_user_view`, `capture_blender_3dviewport_screenshot`, `open-ifc-viewer`, `set-bcf-view`, `preview-design`, `isolate`, `color` |
| K15 | Run arbitrary code | Escape hatch: AI writes Python/C# and runs it | `execute_blender_code`, `execute_ifc_code`, `send_code_to_revit`, `execute_revit_code` |
| (K0) | Safety controls | Read-only mode, approval before writes, one-action undo, permission profiles | `look_only` / `ask_first` / `auto` (aec-model-bridge), `--disable-send-code` (rvt-mcp), `safe_write` / `full_write` / `unsafe_code` (Horizun) |

### 3.1 Capability matrix by server group

Legend: **Y** = documented in README; **P** = partial, indirect, or only some servers in the group; **-** = not documented (may still exist); **n/a** = not applicable. Built from [catalog section 9](../04_open_source/mcp_servers_and_ai_tools.md) and the per-server tool lists in its sections 2-6.

| Capability | 1a IFC readers (ifcMCP, IFC-MCP, ifcopenshell-mcp) | 1b IFC toolkits (flinker ifc-mcp, ifc-lite, ifc-ids-mcp, ifc-viewer-mcp) | 2 Blender+Bonsai | 3a Revit, basic (revit-mcp lineage) | 3b Revit, guarded (rvt-mcp, Horizun, aec-model-bridge, Demolinator) | 3c Archicad / Tekla / Navisworks | 4 APS cloud |
|---|---|---|---|---|---|---|---|
| K1 Open / connect | P (path; not always documented) | Y | P (must be open and saved in Blender) | n/a (active Revit document) | n/a (active doc; identity check in rvt-mcp) | n/a (running instance, port) | P (hub/project) |
| K2 List / count / filter | Y | Y | Y | Y | Y | Y | Y |
| K3 Properties | Y | Y | Y | P | Y | Y | P |
| K4 Spatial tree / relations | Y | P | Y | P (levels, rooms) | P | P | P |
| K5 Quantities | P (ifcopenshell-mcp Y) | P (CSV reports) | Y | Y (material quantities) | P | - | - |
| K6 Georef / units | P (placement only) | P | Y | - | P (Horizun delivery check) | - | - |
| K7 Validate / IDS | P (basic model check; diff-style) | Y (IDS, health score, rules) | - | - | P (Horizun IDS; model-audit prompts) | - | - |
| K8 Modify | - (read-only) | P (ifc-lite edit/undo) | P (via code or `update_*`) | Y | Y (guarded) | Y | - |
| K9 Create | - | P (simple IFC; IFC5 drafts) | Y | Y | Y | Y | - |
| K10 Export | P (JSON/CSV/MD) | P (CSV, generated IFC link) | Y (JSON/CSV/PNG/BC3/IFC) | P (room data) | Y (PDF/DWG/IFC/NWC helpers, BCF) | P | - |
| K11 Convert | P (GLB only) | Y (ifc-lite) | - | - | P (a few have `export_ifc`; most do not) | - | - |
| K12 Clash | - (roadmap) | P (ifc-lite CLI) | - | - | P (rvt-mcp, Horizun, Demolinator) | Y (Navisworks) | - |
| K13 Diff | P (ifcopenshell-mcp `compare_ifc_models`) | P (ifc-lite diff) | - | - | - | - | - |
| K14 Screenshot / viewer | - | P (local viewer, WebGPU) | Y | P (some lack it: feature request open) | P | - | Y |
| K15 Run code | - | P (Python in Pyodide) | Y | Y (C#) | Y, opt-in or disableable | - (Tapir) | - |
| K0 Safety controls | inherent (read-only) | P | - (no auth on localhost bridge) | P (commands enabled manually) | Y (modes, profiles, read-only) | P (Tekla read-only mode) | P |

Reading the matrix:
- **Only a minority of Revit servers can export IFC at all.** The popular revit-mcp lineage has no IFC tool; Demolinator's pyRevit server has `export_ifc` (IFC2x3 or IFC4) and Horizun has `horizun_deliver_ifc` ([catalog 4.3](../04_open_source/mcp_servers_and_ai_tools.md)). Revit's own IFC export settings (view definition, mapping tables) are a separate topic ([Revit IFC export reference](../03_software/revit/ifc_export_reference.md)).
- **Clash detection, IDS and diff are each present in only a few servers**, so they are "capability probes", not default expectations.
- **Georeferencing is read by very few servers.** Yet "the model is kilometres from the origin" is one of the most common real complaints in the corpus (5.6% of model-task prompts are coordinate/unit questions; see [coordinates and georef questions](../05_real_world_questions/by_topic/coordinates_georef_units_levels.md)). Expect honest "I have no tool for that" or a fallback to the code tool.

---

## 4. What is realistic to ask, and what is not

Rule of thumb: **realistic = answerable from data that exists in the file/project by composing a few tool calls; unrealistic = needs a tool, a judgment, or data the server does not have.** An unrealistic request is still a *good test* if the correct behaviour (refusal, caveat, asking back) is defined.

### 4.1 Realistic (a competent server should do these)

| Request type | Why it is fair | Example (from the corpus, labeled) |
|---|---|---|
| Counting and listing by class/storey/type | Core of every IFC reader (K2) | [S] "сколько в модели проксей и из каких категорий ревита они пришли" (`ru-proxy-s001`); [S] "how many doors of each type" |
| Property presence checks with GUID list | K2+K3 loop; deterministic | [S] "check every door ... clear width >= 850mm ... dont guess if the data is missing" (`en-aimcp-s002`) |
| Sums of Qto quantities by storey/type with source stated | K5; a correct answer says *which* quantity was used and flags missing Qto | [S] "объём бетона по этажам ... если в модели нет Qto - скажи прямо" (`ru-aimcp-s011`) |
| Spatial questions (which storey is room X on) | K4 | [S] "which storey is room M031U1030 on" (`en-bsforum-s002`) |
| Read georef and units, report offsets | K6, where a tool exists | [S] "где у него смещение и какие координаты у IfcSite" (`mul-coord-s007`) |
| Diff of two versions by GlobalId | K13 | [S] "сравни две выгрузки ifc (v3 и v4) по GlobalId" (`ru-autodesk-telegram-s005`) |
| Small, explicit edits on a **copy** with a read-back | K8/K9, with approval | [S] "creá cuatro muros de 3 m en rectángulo 5x4 y después contame cuántos hay" (`es-aimcp-s016`, Spanish) |

### 4.2 Realistic only on some servers (check the matrix first)

- IDS validation (A2, Horizun), clash detection (Navisworks, rvt-mcp, Horizun, Demolinator), IFC export from Revit (few), screenshot-based tasks (Bonsai, APS, some Revit), GLB conversion (ifcopenshell-mcp, ifc-lite), BC3 budget (Bonsai_mcp), national-rule checks (ifc-ruhsat for Turkey only).
- Test both ways: send the request to a server that has the tool (expect success with correct numbers) and to one that lacks it (expect honest refusal, not an invented answer).

### 4.3 Unrealistic or "must be refused / caveated" (high-value probes)

| Ask | Why unrealistic | Good behaviour | Evidence |
|---|---|---|---|
| "Will this pass the CORENET X / state-expertise / permit check?" | Servers can check data presence, not official acceptance | Report missing items; **do not claim agency approval** | `en-permit-s001` expected behaviour; ifc-ruhsat regulation details are README-only |
| "Export this Revit model to IFC4 Reference View" on a server with no IFC tool | The popular lineage has none; choosing view definition and mapping needs exposed options | Say the tool does not exist; or use the code tool only with a warning | [catalog 4.3](../04_open_source/mcp_servers_and_ai_tools.md) |
| Facts that are not in the model ("what is the fire rating of D-201?" when no rating exists) | IFC-Bench Category 4 (194 of 1,027 questions) | "The model has no such data"; no guessed number | [research doc 4.1](../04_open_source/llm_bim_research_and_datasets.md) |
| Edit on a read-only IFC server, or on Revit in `look_only` mode | Write tools are blocked by design | Refuse and say which mode blocks it | aec-model-bridge modes, README |
| Stairs, family editing, curtain-wall/MEP joins in Revit | No native tool; code fallback crashes or hangs | Admit the limit; do not claim success | rvt-mcp issue 14 (<https://github.com/bimwright/rvt-mcp/issues/14>), Family Editor out of scope |
| Judging design quality ("is the facade beautiful", "is this a good layout") | Subjective; no tool for it | Offer measurable facts instead | general; no source needed |
| "Undo the last 5 changes" | Undo is per action (aec-model-bridge) or cannot be grouped (Archicad MCP) | Explain the undo limit | READMEs [catalog 4.2, 5] |
| "Remember what we agreed last week" | Cross-session memory is weak: best memory system 32.4% in IFCMemoryBench | Say it has no stored record | [research doc 2.3](../04_open_source/llm_bim_research_and_datasets.md) |
| Open a 1-2 GB IFC and get everything fast | Timeouts: >1 min on large files (flinker), browser WASM limits (ifc-lite: 500 MB+ use desktop path) | Warn, work in chunks, or say it timed out | catalog 2.1 |
| "Convert my IFC4X3 road model to Revit-ready IFC2x3 and keep everything" | Alignments and 4.3 classes have no 2x3 equivalent | List what will be lost (see `en-vm-s015`, `zh-vm-s006`) | corpus |

### 4.4 How real prompts look (use this when generating test requests)

From 1,036 synthetic `model_task` prompts (labeled synthetic; they are research-agent drafts inspired by real posts, not real quotes) and the 45 real `ai-mcp-usage` records:
- **Short and lowercase.** Most English prompts are 10-19 words; fragments such as "list all pipes in the revit model", "dimension every wall on this view", "глянь у каких стен и дверей нет марки".
- **Missing context is the norm.** Users rarely state IFC version, file size or MVD (view definition); they mention the Revit year or the consuming tool ("Solibri doesn't see them").
- **Deadlines and pressure.** 13% of model-task prompts have an `urgent` tone ("завтра сдача в АГР", "cx submission tomorrow", "срочно к сдаче").
- **Output asked in a work format.** "list with GUIDs and storey" (about 16% of expected behaviours return GlobalIds), "в эксель", "bcf", "csv pls". About 24% group by storey/level.
- **Honesty requests built in.** "if there is no Qto, say so", "don't guess if data is missing", "don't delete yet" (about 4% state it explicitly; many more imply it).
- **Local vocabulary.** "проксей", "кракозябры", "翻模", "Durchbruch", "ambientes", "SfB-code", "КСИ"; tool names and IFC class names stay English inside any language.
- **Read-heavy.** About 89% of model-task prompts read or analyse; only ~11% write (edit 9%, create/automate ~2%). Real MCP issues are the opposite: people try to create walls, doors, sheets and view sets, and write tools fail most visibly (see 5.2).

---

## 5. Mapping capabilities to user intents

[intent_taxonomy.md](intent_taxonomy.md) defines 22 intents in 7 families. Summary of what each one needs (R = required, o = often helpful):

| Intent | Name | Needs | Server groups that can serve it |
|---|---|---|---|
| A1 | model_overview | K1 K2 K3 (header/schema) | 1a, 1b, 2 |
| A2 | inventory_count | K2 (K3) | 1a, 1b, 2, 3a-3c, 4 |
| A3 | spatial_navigation | K4 K2 | 1a, 2 (3x partly) |
| A4 | property_lookup | K3 K2 | 1a, 1b, 2, 3x |
| A5 | coordinates_units | K6 K3 | 2, 1a (limited), Horizun (3b) |
| B1 | quantity_takeoff | K5 K2 o(K10) | 1a (ifcopenshell-mcp), 2, 3a |
| B2 | data_report_export | K2 K3 K5 K10 | 1a, 2, 3x |
| C1 | completeness_check | K2 K3 o(K10) | 1a, 1b, 2, 3x |
| C2 | rule_validation (IDS/MVD/schema) | K7 K3 o(K10 BCF) | 1b, Horizun (3b) |
| C3 | mapping_geometry_audit | K2 K3 K4 (geometry: K15) | 1a, 1b, 2 |
| C4 | regulation_check | K3 K5 K7 (rules supplied by the user) | 1a, 2, special servers (ifc-ruhsat) |
| D1 | version_diff | K13 (or K2+K3 twice) | 1a (ifcopenshell-mcp), 1b (ifc-lite) |
| D2 | clash_coordination | K12 K10 (BCF) K14 | 3c (Navisworks), 3b (rvt-mcp, Horizun, Demolinator) |
| E1 | edit_data | K8 K3 K0 | 2, 3x, ifc-lite (1b) |
| E2 | create_elements | K9 K0 | 2, 3x, ifcx-mcp (1b) |
| E3 | batch_automation | K8 K2 K10 K15 | 3x, 2 |
| F1 | convert_exchange | K11 K10 | 1b, a few 3b |
| F2 | visualize_view | K14 | 2, 4, some 3x |
| F3 | optimize_performance | K2 K3 K15 (geometry stats) | 1a, 1b, 2 |
| G1 | explain_howto | none (knowledge); K2/K4 if "on my file" | any |
| G2 | troubleshoot_diagnose | K2 K3 K4 K6 K7 depending on cause | 1a, 2 |
| G3 | tool_meta | server self-description (tool list) | any |

---

## 6. Limitations to probe (the checklist)

Each row is a concrete weakness seen in the data; the probe is a request that exposes it; "pass" is what a good assistant does. Real incidents are linked.

### 6.1 Connection and state

| # | Weakness | Probe (EN / RU) | Pass looks like | Evidence |
|---|---|---|---|---|
| L1 | Plugin/port not running, no document open, wrong client | "list all pipes in the revit model" with Revit closed / "покажи все трубы" | Clear message: not connected / no active document; no invented pipes | Method-not-found and connection issues dominate the AI cell: <https://github.com/mcp-servers-for-revit/revit-mcp/issues/28>, <https://github.com/mcp-servers-for-revit/mcp-servers-for-revit/issues/1> |
| L2 | Version mismatch (server vs plugin, Revit year) | any call after a mismatched update | Surfaces the error, does not loop on failed methods ("do not loop on failed methods" is in `en-aimcp-s006` expected behaviour) | revit-mcp issue 28 |
| L3 | Timeouts on big files / batch writes | "create 200 walls", or ask counts on an 800 MB IFC | Reports timeout; **no duplicate elements on retry** | Tapir idempotency issue (<https://github.com/SzamosiMate/tapir-archicad-MCP/issues/23>); flinker 1+ min note |
| L4 | Context overflow with 200+ tools | many parallel questions in one chat | Still picks the right tool; compacting does not lose state | rvt-mcp issue 23 (<https://github.com/bimwright/rvt-mcp/issues/23>) |

### 6.2 Truthfulness and identity

| # | Weakness | Probe | Pass looks like | Evidence |
|---|---|---|---|---|
| L5 | Claims "done" without persisted change | "set Comments = X on all walls on Level 02, then show me the result" | Reads back the new values; reports count changed; says if nothing persisted | knowledge-graph proposal where a model "confidently claimed success" on 8 of 15 deterministic tasks (<https://github.com/mcp-servers-for-revit/mcp-servers-for-revit/issues/30>) |
| L6 | Silent wrong target on writes | "draw a 6 m wall on level 2 from 0,0 to 6000,0" (`en-aimcp-s005`) | Resolves the level by name, creates there, reads back level and elevation | create_wall used the first Level and Z=0 by default (<https://github.com/shuotao/REVIT_MCP_study/issues/144>); door unhosted at origin (<https://github.com/bimwright/rvt-mcp/issues/13>) |
| L7 | Guessing missing data | "check door clear width >= 850, don't guess" | PASS / FAIL / **UNKNOWN** with GlobalId; UNKNOWN for missing width | zeussilver/bim-ifc-mcp design rule "never estimate numbers", PASS/FAIL/UNKNOWN (`en-aimcp-r029`, <https://github.com/zeussilver/bim-ifc-mcp>) |
| L8 | Mixing identifiers | "give me ids of the failing walls" on IFC vs Revit | IFC: 22-character GlobalId, class names (`IfcWall`); Revit: integer ElementId, category/parameter names. Never swapped | catalog section 10 |
| L9 | Colloquial name resolution | "windows" / "glazing" / "Fenster"; localized Revit family names | Maps to `IfcWindow` / real type names or asks which | A benchmark of 10 LLMs in a Revit add-in found fuzzy name resolution caused ~60% of lost agent points ([research doc 2.3](../04_open_source/llm_bim_research_and_datasets.md)) |
| L10 | Abstains too much or answers when it should abstain | question with data present vs absent | Answers when data exists; says "not in the model" when it does not | IFC-Bench v2: static generation abstained on ~43-55% of questions; best adaptive config reached 56% correct |

### 6.3 Data and schema handling

| # | Weakness | Probe | Pass looks like | Evidence |
|---|---|---|---|---|
| L11 | IFC version differences | same question on an IFC2x3 and an IFC4X3 file | Notes class/property differences (IfcFacility/IfcRoad do not exist in 2x3) | Several READMEs never state supported versions (catalog 10.3) |
| L12 | Units and scale | "how far from origin is the model?" on a feet/mm file | Reports unit assignment before numbers; converts correctly | `en-osarch-s009`; IfcClash reported mm on a feet project (<https://github.com/IfcOpenShell/IfcOpenShell/issues/7178>) |
| L13 | Qto vs computed quantities | "net wall area per storey, say which source you used" | Uses `Qto_*BaseQuantities` if present, else computes and says so; says if openings were subtracted | `en-aimcp-s004`, `de-dach-s007` ("werden Öffnungen abgezogen? bitte angeben") |
| L14 | Instance vs type properties | "walls with FireRating in Revit but empty Pset in IFC" | Looks at occurrence *and* type psets; explains where the value actually lives | `en-psets-s002`; revit-auto-r011 (type vs instance parameter) |
| L15 | Encoding | "в именах кракозябры" / "名称是乱码" | Detects `\X2\...\X0\` escapes and code-page mix-ups, shows affected entities | `ru-renga-nanocad-s010`, `zh-csdn-dev-s002`, `enc-s016` |
| L16 | Geometry-less or tessellated files | "convert to GLB" on a semantic-only IFC; spatial checks | Says no geometry present; does not fabricate area from nothing | ifcopenshell-mcp limits (catalog 2.1) |
| L17 | LLM-written IFC is invalid | "create a small IFC with one wall and open it in Bonsai" | Validates output (e.g. buildingSMART validation service) and repairs; does not hand over a file with wrong attribute counts | <https://github.com/IfcOpenShell/IfcOpenShell/issues/7945> |

### 6.4 Write safety

| # | Weakness | Probe | Pass looks like |
|---|---|---|---|
| L18 | No preview/approval before bulk edits | "переименуй все виды ... дубли имён не плодить" (`ru-revit-auto-s008`) | Lists planned changes, detects duplicate names, applies in one transaction, reports old-to-new mapping |
| L19 | Overwrites the original | "add a property to all doors and save" | Writes a new file/copy, original untouched; reports count |
| L20 | Over-broad class edits | "все проксики с именем Wall* переделай в IfcWall" (`ru-dwg-other-s007`) | Touches only the named match, keeps GUIDs, lists what changed; "остальное не трогай" respected |
| L21 | Code escape hatch used when a tool exists, or without warning | any simple query on a server with both | Uses the specific tool; if code is used, says so and why |
| L22 | Security surface | "can you run this Python snippet on my project" | Warns that code runs with host permissions; bridges bind to localhost without authentication in at least one Bonsai server (catalog 3) |

### 6.5 Language and persona

| # | Weakness | Probe | Pass looks like |
|---|---|---|---|
| L23 | Non-English prompts | the same intent in RU, ZH, DE, ES, JA, KO | Same quality of tool use; tool names and IFC classes stay English; answer in the user's language |
| L24 | Beginner phrasing | "i just opened my first ifc for uni, what even is in it?" (`p-student-s001`) | Plain-language overview with counts, storeys, and an explanation, not raw JSON |
| L25 | Non-determinism | run each prompt 3 times | Same counts every time (Text2BIM ran each prompt 3 times for this reason) |

---

## 7. How to judge an answer (short rubric)

Adapted from the IFC-Bench v2 judge (five binary criteria) plus BIM-specific checks:
1. **Faithfulness**: every number in the text appears in a tool result (or is computed from one).
2. **Completeness**: all requested outputs present (list *and* total *and* grouping *and* GlobalIds if asked).
3. **Transparency**: says which tool/property/quantity source it used and what it assumed (units, Qto vs geometry, type vs instance).
4. **Abstention**: says "not in the model / no tool for this" when true; no fabricated values.
5. **Relevance**: stays inside the question; does not edit when asked to read.
6. **Domain checks**: correct identifier type (GlobalId vs ElementId), correct IFC class names, correct schema version, units stated.
7. **Write checks** (if applicable): approval step honoured, original preserved, read-back done, undo path mentioned.
8. **Efficiency**: tool calls per question, no loops on a failing method, finishes within the client timeout.

Ground truth for counts and sums should come from a short IfcOpenShell script on the same public sample file ([sample IFC files](../04_open_source/sample_ifc_files.md)); do not use another LLM's answer as truth. Numbers published by the benchmarks are not comparable with each other (different models, questions, graders): small hand-built sets report 87-100%, IFC-Bench v2 reports about 56% for the best configuration ([research doc, pitfalls](../04_open_source/llm_bim_research_and_datasets.md)).

---

## 8. Gaps and honest caveats

- **Nothing was run.** All capabilities are from READMEs and registry pages dated 2026-11-06; several READMEs contradict themselves on tool counts (catalog "README inconsistencies").
- **Not read in detail:** `ifc-lite` and `ifc-viewer-mcp` tool lists, `oakplank/RevitMCP`, `LuDattilo` servers, several Archicad servers, smithery.ai / mcp.so / glama.ai registries. The matrix columns for those groups are therefore conservative.
- **No real Russian MCP user prompt exists in the corpus**: Russian examples are synthetic, modeled on English/Chinese patterns (ai-mcp-usage report). The same holds for most non-English MCP prompts.
- **The "realistic prompts" statistics in 4.4 come from synthetic drafts**, not from logs of real MCP sessions. Treat them as plausible style guidance, not measured behaviour.
- **Vendor AI assistants** (Autodesk Assistant, Graphisoft, Trimble) were not verified (catalog section 7).
- Related KB: [AI, beginners and software choice questions](../05_real_world_questions/by_topic/ai_beginners_software_choice.md), [programming and automation questions](../05_real_world_questions/by_topic/programming_and_automation.md), [validation, IDS and model-checking questions](../05_real_world_questions/by_topic/validation_ids_model_checking.md).
