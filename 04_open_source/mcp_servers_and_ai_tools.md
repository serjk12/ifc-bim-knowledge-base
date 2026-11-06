# MCP servers and AI tools for IFC, BIM and Revit (catalog)

**Last researched: 2026-11-06**

> QA pass 2026-11-06 (see `_meta/qa/qa-standards-2.md`): star counts, last-push dates, licences, archived flags and descriptions of about 45 repositories listed here were re-read from the GitHub API and repository pages on the same day and agree with this catalog, with the wording fixes noted inline (archived dates, "successor" vs "fork"). The registry/blog parts and the sub-repositories not re-checked (rate limit) keep their original confidence.

## In plain words

MCP (Model Context Protocol) is a standard way for an AI chat client (Claude Desktop, Claude Code, Cursor, VS Code Copilot, ChatGPT desktop) to call "tools" exposed by a small program called an MCP server. For BIM, such a server either (a) reads and edits an IFC file directly, usually through the open-source IfcOpenShell library, or (b) talks to a running desktop application (Revit, Archicad, Tekla, Blender with the Bonsai add-on, Navisworks, SketchUp) through that application's own API. The AI never "sees" the model by itself: it only sees what the tools return (JSON text, counts, GlobalIds, sometimes a screenshot), so the quality of an answer depends on which tools exist and how they are described. Most servers listed here are young (2025-2026), community-made, alpha or early quality, and tool lists differ a lot, so a tester should always check what the server really exposes before judging an answer.

Scope note: research was done on 2026-11-06 with GitHub search, npm and the official MCP Registry (all read as web pages/JSON, nothing downloaded or installed). The WebSearch budget ran out part-way, so web articles/blogs and the registries smithery.ai, mcp.so, glama.ai and mcpservers.org were NOT read (see Gaps). Star counts and "pushed" dates are snapshots from 2026-11-06.

---

## 1. How to read this catalog

- **IFC-file servers**: take a path to a `.ifc` file, no CAD application needed. They answer "what is in this file" questions. Safe to test with sample files.
- **Application-bridge servers**: need a licensed, running desktop application plus an add-in or plugin on the same Windows machine (Revit, Tekla, Navisworks: Windows only). They can change the live model. Results depend on the open document, active view and Revit year.
- **Code-execution tools** (`execute_blender_code`, `execute_ifc_code`, `send_code_to_revit`, `revit_execute_python`): let the AI run arbitrary code inside the host. Powerful, unpredictable, and the main security/QA risk. Several projects ship them off by default or warn about them [12][16][17][21].
- **Tool counts vary wildly**: from 7 fixed read-only tools [13] to 245 Revit tools [21] to "all commands via 3 generic tools" [22].

---

## 2. IFC-file MCP servers (no CAD application required)

| Server | URL | Language | Stars / activity (2026-11-06) | IFC versions | Notes |
|---|---|---|---|---|---|
| smartaec/ifcMCP | https://github.com/smartaec/ifcMCP | Python (FastMCP + ifcopenshell) | 34 stars, last push 2025-06-08, Apache-2.0 [1][13] | not stated | Early (June 2025) read-only server |
| ekkodale/IFC-MCP | https://github.com/ekkodale/IFC-MCP | Python (README also lists Node.js) | 11 stars, last push 2025-12-04, MIT [1][27] | not stated; tested with IFC4 sample files | Inventory/property queries |
| Daviidro/ifcopenshell-mcp | https://github.com/Daviidro/ifcopenshell-mcp | Python (IfcOpenShell) | 0 stars, push 2026-08-09, MIT [4][28] | IFC2x3, IFC4, IFC4.3 (`.ifc`, `.ifczip`, `.ifcxml`) | Local only, 8 tools |
| flinker-app/ifc-mcp (npm `ifc-mcp` 0.2.0) | https://github.com/flinker-app/ifc-mcp | Node.js + IfcOpenShell in Pyodide | 13 stars, push 2026-09-24, Apache-2.0 [1][25][30] | not stated | Has a local IFC viewer and BCF viewpoint tools; also in the official MCP Registry [32] |
| LTplus-AG/ifc-lite (npm `@ifc-lite/mcp` 0.29.0; the older URL louistrue/ifc-lite redirects here) | https://github.com/LTplus-AG/ifc-lite | TypeScript + Rust/WASM | 461 stars, push 2026-11-06, MPL-2.0 [1][26][30] | IFC2X3, IFC4, IFC4X3, IFC5 (IFCX) claimed | MCP over stdio or HTTP; individual tool names not published on the page I could read |
| j03rul4nd/ifc-viewer-online (npm `ifc-viewer-mcp`) | https://github.com/j03rul4nd/ifc-viewer-online | TypeScript | 18 stars, MIT [32][52] | IFC2x3, IFC4, IFC4x1, IFC4x3 | Browser viewer + validation/IDS/"health score"; MCP tool names not read |
| vinnividivicci/ifc-ids-mcp | https://github.com/vinnividivicci/ifc-ids-mcp | Python (fastmcp, ifctester) | 28 stars, push 2026-04-06, MIT [1][14] | IDS 1.0; examples use IFC4 | Creates/validates IDS files (see 2.3) |
| BerkantACUN/ifc-ruhsat (PyPI `ifc-ruhsat` 0.2.1) | https://github.com/BerkantACUN/ifc-ruhsat | Python | 3 stars, MIT [1][29][57] | checks for IFC4X3 | National compliance check, Turkey (see 2.4) |
| louistrue/ifcx-mcp | https://github.com/louistrue/ifcx-mcp | TypeScript | 26 stars, push 2026-04-12, license not stated [1][24] | IFC5 / IFCX (alpha) | Authoring only (see 2.5) |
| nbharathik/ifc-console | https://github.com/nbharathik/ifc-console | Python | 4 stars, Apache-2.0 [1] | not stated | "Terminal interface connecting IFC/BIM models to LLMs" (details not read) |

### 2.1 Tool lists (names + one-line purpose)

**smartaec/ifcMCP** [13] (names are from the README; purposes inferred from names, "(unverified)"):
`get_entities` (list entities), `get_named_property_of_entities` (one named property over many entities), `get_entity_properties`, `get_entity_location`, `get_entities_in_spatial` (entities inside a storey/space), `get_openings_on_wall`, `get_space_boundaries`. Run: `python server.py`, client config points to `http://127.0.0.1:8000/mcp`. No example prompts in the README (demo GIFs only).

**ekkodale/IFC-MCP** [27]: `get_entity_types`, `get_entities` (filter by attributes), `get_entity_info` (basic or recursive), `get_property_sets`, `get_property_names`, `get_entities_with_properties` (filters + statistics), `analyze_building_inventory` (counts per class). Typical questions from its business case: how many windows/doors/ramps, largest window, how many walls above a height, total wall area.

**Daviidro/ifcopenshell-mcp** [28]: `query_ifc_elements` (by type/level/property), `get_ifc_statistics`, `get_element_properties` (by GUID), `list_ifc_spaces`, `validate_ifc_model` (materials, properties, containment, naming), `compare_ifc_models` (diff two versions), `extract_ifc_quantities` (markdown/CSV/JSON), `convert_ifc_to_gltf` (GLB). README prompts: "How many fire doors are on Level 2?", "Validate that all elements have materials", "Extract concrete quantities for Level 1", "What changed since last week's version?". Limits: GLB conversion fails on semantic-only IFCs without geometry; clash detection, COBie export, Uniclass/OmniClass validation are roadmap only.

**flinker-app/ifc-mcp** [25]: viewer tools `open-ifc-viewer`, `show-ifc-file`, `set-bcf-view` (apply a BCF viewpoint), `clear-ifc-viewer`; other tools for inspection, report creation and IFC creation exist but are not named on the page. README prompts: summarize a model; count walls/doors/windows/spaces/property sets; find missing names, classifications and suspicious property values; create a CSV room-area report; create a simple IFC with one building, one storey, four walls. Limits: large IFC can take over a minute; cancelling does not stop the running Python; generated files are temporary download links, not written to the project folder.

**ifc-lite** [26]: the CLI can start an MCP server (stdio/HTTP); `ifc-lite ask model.ifc "how many walls?"` answers natural-language questions; also IDS validation, clash detection, diff, merge, conversion, BCF. Limits (stated): boolean-heavy geometry is slower, browser viewing needs WebGPU, 500 MB+ files should use the desktop path.

### 2.2 Registry-listed IFC servers
The official MCP Registry search for "ifc" returned: `io.github.BerkantACUN/ifc-ruhsat` 0.2.0 (PyPI), `io.github.flinker-app/ifc-mcp` (npm, latest 0.2.0), `io.github.j03rul4nd/ifc-viewer-mcp` 1.0.0 (npm) [32]. Other hits were unrelated ("IFC" = International Finance Corporation, India import duty, etc.).

### 2.3 IDS authoring: ifc-ids-mcp [14]
17 tools: document (`create_ids`, `load_ids`, `export_ids`, `get_ids_info`), `add_specification` (IFC version + cardinality), facets (`add_entity_facet`, `add_property_facet`, `add_attribute_facet`, `add_classification_facet`, `add_material_facet`, `add_partof_facet`), restrictions (`add_enumeration_restriction`, `add_pattern_restriction`, `add_bounds_restriction`, `add_length_restriction`), validation (`validate_ids` against the XSD, `validate_ifc_model` against an IDS). Uses IfcOpenShell's IfcTester. Target: IDS 1.0. Gotchas from the README: IDS 1.0 allows one entity facet per specification applicability, so different entity types need separate specifications; property facets require `property_set`. Tool-call example: `add_property_facet(property_name="FireRating", property_set="Pset_WallCommon")`.

### 2.4 National compliance: ifc-ruhsat [29][57]
Tools (Turkish names): `yonetmelik_kontrolu` (audit, findings with article, EK-9 row, GlobalIds), `ek9_formu` (EK-9 quality-control form), `model_ozeti`, `ek5_siniflar` (mandatory/optional IFC classes), `ek6_gerekenler` (required attributes/psets per class), `yonetmelik_bilgisi`. It claims to implement a Turkish regulation on digital preparation of projects ("RG 33331", IFC 4.3 / TS EN ISO 16739-1, effective 1 Sept 2027, IFC delivery phased from 2029); these regulation details come only from the repo README and are "(unverified)". IFC4 files are flagged as not meeting 4.3. Example prompt (Turkish): "does A_blok.ifc comply with the regulation, produce the EK-9 form".

### 2.5 IFC5 / IFCX authoring: ifcx-mcp [24]
In-memory drafts, exported as alpha JSON `.ifcx`, tiered `index.ifcx`, or zipped packages. Tools include `ifcx_plan_model`, `ifcx_create_model`, `ifcx_create_spatial_structure`, `ifcx_create_element`, `ifcx_create_wall_from_axis`, `ifcx_create_window_with_void`, `ifcx_resolve_bsdd_classification`, `ifcx_create_georeference_layer`, `ifcx_validate_ifc5_compliance`, `ifcx_validate_ids`, `ifcx_create_bcf_from_validation`, `ifcx_write_alpha`/`_tiered`/`_zipped`, `ifcx_publish_layer_version` (dry-run by default). README prompts: "Create an IFCX model called Campus", add storeys at 0 m and 3.5 m, classify walls as Uniclass Ss_25_10_30 via bSDD, georeference Zurich (EPSG:2056). Limits: drafts lost if server stops before export; IFC5 itself is still in development, so output is not production IFC4/IFC4.3.

---

## 3. Blender + Bonsai (formerly BlenderBIM) servers

Bonsai is the IfcOpenShell-based IFC authoring add-on for Blender. These servers bridge an MCP client to a running Blender via a socket add-on.

| Server | URL | Stars / activity | Tools | Notes |
|---|---|---|---|---|
| JotaDeRodriguez/Bonsai_mcp | https://github.com/JotaDeRodriguez/Bonsai_mcp | 66 stars, MIT, push 2026-09-06 [5][12] | 15 IFC tools + `execute_blender_code` | Fork of BlenderMCP (ahujasid/blender-mcp) |
| Show2Instruct/ifc-bonsai-mcp | https://github.com/Show2Instruct/ifc-bonsai-mcp | 67 stars, MIT, push 2026-07-10 [1][15] | ~60 tools | Basis of the MCP4IFC paper [46] |
| Show2Instruct/bonsai-mcp | https://github.com/Show2Instruct/bonsai-mcp | 13 stars, MIT, push 2026-08-20 [4][16] | 14 tools | Rewrite, "code-generation focused"; authors recommend it over the old one |
| ProfRino/bonsai-bim-skills | https://github.com/ProfRino/bonsai-bim-skills | 7 stars, GPL-3.0 [1] | 7 Claude Code skills | Skills (prompts), not an MCP server [11] |
| lfniederauer/blender-agentic-bonsai-sketcher-mcp, sinsunsan/blender-bonsai-bim-mcp | see [5][11] | 2 and 5 stars | n/a | Small experiments |

**JotaDeRodriguez/Bonsai_mcp tools** [12]: `get_ifc_project_info`, `list_ifc_entities`, `get_ifc_properties` (by GlobalId or selection), `get_ifc_spatial_structure`, `get_ifc_relationships`, `get_selected_ifc_entities`, `get_user_view` (viewport as base64 image), `export_ifc_data` (JSON/CSV), `place_ifc_object` (create + position), `get_ifc_quantities`, `get_ifc_total_structure`, `export_drawing_png`, `get_ifc_georeferencing_info`, `georeference_ifc_model` (CRS EPSG/custom, map conversion), `export_bc3_budget` (BC3 / FIEBDC-3/2016 cost file, Spanish or English). Also a Sequential Thinking tool, an MCP resource `table_of_contents.md` and a prompt `Technical_building_report`. Requirements: Blender 4.0+, Python 3.12+, uv, Bonsai add-on. README prompts: count walls/doors/windows; show spatial structure; generate a BC3 budget in Spanish. Stated caveats: `execute_blender_code` runs arbitrary Python (save first); complex models should be handled in smaller steps; README says "eleven IFC tools" but lists fifteen; IFC versions not stated.

**ifc-bonsai-mcp (Show2Instruct) tools** [15], grouped: screenshots (`capture_blender_window_screenshot`, `capture_blender_3dviewport_screenshot`); scene (`get_scene_info`, `get_selected_objects`, `get_object_info`, `get_ifc_scene_overview`, `execute_blender_code`, `execute_ifc_code_tool` with security restrictions); element creation/update (`create_wall`, `create_two_point_wall`, `create_polyline_walls`, `update_wall`, `create_roof`, `create_slab`, `create_door`, `create_window`, `create_stairs`, plus `update_*`/`get_*_properties`/`delete_*` variants); mesh (`create_trimesh_ifc`, `create_mesh_ifc`); styles (`create_surface_style`, `create_pbr_style`, `apply_style_to_object`, `list_styles`); RAG (`ensure_ifc_knowledge_ready`, `search_ifc_knowledge`, `find_ifc_function`, `get_ifc_function_details`). Requirements: Blender 4.4+, Bonsai 0.8.2+, ifcopenshell >= 0.7.0. Limits: an empty IFC must be created and saved first or changes do not reach the scene; the "Connect to MCP server" button in the add-on panel must be clicked; the generic code tool "behaves unpredictably with IFC operations".

**Show2Instruct/bonsai-mcp tools** [16]: read-only `get_scene_info`, `get_selected_objects`, `list_elements` (class, name, storey, or IfcOpenShell selector), `get_psets`, `get_viewport_screenshot`, `get_ifc_project_info` (schema, counts, materials, classifications), `get_spatial_structure`, `get_quantities`; mutating `execute_ifc_code` (IfcOpenShell/Bonsai API, `bpy` blocked), `execute_blender_code` (full bpy), `refresh_view`, `refresh_geometry`, `reload_project`, `save_ifc_file`. README prompt: "List every wall in the model with its fire rating." The bridge binds to 127.0.0.1 without authentication; treat it as an open Python REPL. Not on PyPI (run from a git clone).

**Research papers**: MCP4IFC (arXiv 2511.05533, submitted 2025-10-29, title "MCP4IFC: IFC-Based Building Design Using Large Language Models", 7 authors) describes the above framework: BIM query tools, predefined creation/modification functions, and code generation with in-context learning + RAG; results are qualitative (build a simple house, query/edit existing IFC) [46]. A second paper proposes a modular, API-agnostic reference architecture for BIM MCP servers with an adapter layer, prototype on IfcOpenShell (arXiv 2601.00809; first submitted 21 Dec 2025, revised 28 Mar 2026, per the arXiv page re-read in QA) [47]. A third studies building-code review with MCP vs RAG pipelines (arXiv 2510.02634, submitted 3 Oct 2025, "Automatic Building Code Review: A Case Study"): the MCP route calls the U.S. DOE COMcheck engine through its API, the RAG route retrieves code provisions; the authors found the MCP pipeline more rigorous and reliable than RAG (the ASHRAE 90.1 lighting detail in an earlier draft of this catalog was not re-found on the abstract page, so treat it as (unverified)) [48].

---

## 4. Revit MCP servers

Revit is Windows-only; every server below needs a running licensed Revit plus an add-in. Revit years supported differ (the 2025+ API moved to .NET 8, 2027 to .NET 10 [19][21][49]).

| Server | URL | Language | Stars / activity | Revit years | Tool count |
|---|---|---|---|---|---|
| mcp-servers-for-revit/mcp-servers-for-revit (continuation monorepo; npm `mcp-server-for-revit`; its GitHub description calls it a "Sparx fork of the mcp-servers-for-revit/revit-mcp project") | https://github.com/mcp-servers-for-revit/mcp-servers-for-revit | TS server + C# plugin | 428 stars, MIT, push 2026-04-05 [2][17][31] | 2020-2026 | 26 |
| mcp-servers-for-revit/revit-mcp (original; archived, last push 2026-02-25; the older URL github.com/revit-mcp/revit-mcp redirects here) | https://github.com/mcp-servers-for-revit/revit-mcp | TypeScript | 477 stars [2][18] | not specified | 25 |
| mcp-servers-for-revit/mcp-server-for-revit-python | https://github.com/mcp-servers-for-revit/mcp-server-for-revit-python | Python (pyRevit Routes) | 228 stars, push 2026-10-26 [2] | (not read) | (not read) |
| Sam-AEC/aec-model-bridge | https://github.com/Sam-AEC/aec-model-bridge | Python hub + C# add-in | 118 stars, GPL-3.0 (+Revit linking exception) [2][19] | 2024-2027 builds | 219 default (103 Revit) |
| bimwright/rvt-mcp | https://github.com/bimwright/rvt-mcp | C# (.NET 8) | 117 stars, Apache-2.0, push 2026-11-05 [2][21] | 2022-2027 | 245 fresh install, 58 bare, 98 read-only |
| shuotao/REVIT_MCP_study (npm `@shuotao/revit-mcp-server` 1.6.0) | https://github.com/shuotao/REVIT_MCP_study | TS + C# | 110 stars, MIT [2][31][49] | 2022-2026 | 239 |
| HorizunGroup/horizun-revit-mcp | https://github.com/HorizunGroup/horizun-revit-mcp | C# | 79 stars, Apache-2.0 [2][20] | 2023-2027 | 125 tools, 481 sub-operations |
| LuDattilo/RevitCortex / revit-mcp-server | https://github.com/LuDattilo/RevitCortex | C# | 28 and 87 stars, MIT [2] | 2023-2027 | 173 / 80+ |
| oakplank/RevitMCP | https://github.com/oakplank/RevitMCP | Python | 66 stars, MIT [2] | (not read) | (not read) |
| Demolinator/revit-mcp-server | https://github.com/Demolinator/revit-mcp-server | Python (pyRevit) | 41 stars, MIT [2][51] | 2024-2027 | 48 |
| kaitpw/Rvt_Docs_MCP | https://github.com/kaitpw/Rvt_Docs_MCP | TypeScript | 31 stars [2] | n/a | Exposes Revit API docs, not a model |
| aecomcps.com "Revit MCP" (registry) | https://aecomcps.com/revit | remote streamable-http | v0.7.30 [33] | 2024-2027 | n/a |
| Innoprovn/vn-revit-mcp (registry) | https://github.com/Innoprovn/vn-revit-mcp | MCPB | v0.8.1 [33] | 2025+ | n/a ("queries, QA-QC, CAD-to-model, rebar, sheets") |
| sharafutdinovdi/revit-model-mcp | https://github.com/sharafutdinovdi/revit-model-mcp | (not read) | listed in awesome-mcp-servers [38] | | read-only by default |

Other npm packages found [31]: `revit-mcp` 2.3.0 (vespo92), `@rui.branco/revit-mcp` 1.0.8, `revit-mcp-server` 2.0.1 ("179 tools, Revit 2020-2026"), `@kimminsub/revit-mcp` 0.4.0 (20 tools), `hill-revit-mcp`, `pi-revit`. Many are forks or near-duplicates of the revit-mcp lineage.

### 4.1 Common tool vocabulary (revit-mcp lineage) [17][18]
Query: `get_current_view_info`, `get_current_view_elements`, `get_available_family_types`, `get_selected_elements`, `get_material_quantities`, `ai_element_filter`, `analyze_model_statistics`. Create: `create_point_based_element` (door/window/furniture), `create_line_based_element` (wall/beam/pipe), `create_surface_based_element` (floor/ceiling/roof), `create_grid`, `create_level`, `create_room`, `create_structural_framing_system`, `create_dimensions`. Modify: `delete_element`, `operate_element`, `color_elements`, `tag_all_walls`, `tag_all_rooms`. Data: `export_room_data`, `store_project_data`, `store_room_data`, `query_stored_data`. Escape hatch: `send_code_to_revit` (AI-written C#), `say_hello` (connection test). No IFC tools in this lineage [17].

### 4.2 Safety-oriented servers
- **aec-model-bridge** [19]: modes `look_only` (blocks all write tools), `ask_first` (default; AI drafts a plan, a human approves in a Revit panel or CLI, never over MCP), `auto`. Each action in its own transaction (Ctrl+Z per action). IFC provider reads IFC without Revit (7 tools: `ifc_get_spatial_structure`, `ifc_get_properties`, `ifc_validate`...), does not edit IFC. Speckle (17 tools) and Navisworks (15, in progress) providers. Stated limitation: nothing verified in a live Revit session, behaviour marked UNVERIFIED. README prompts: group Revit warnings by description; find walls on Level 02 and propose Comments = "Coordination reviewed"; show an IFC file's storeys and schema issues.
- **rvt-mcp** [21]: read-only mode, `--disable-send-code`, document-identity check before writes, mm units at the tool boundary, toolsets (query, create, modify, delete, export "PDF/DWG/IFC/NWC helpers", mep, sheets, rooms, links, parameters, structural...). Built-in MCP prompts: `revit_getting_started`, `revit_drawing_layout`, `revit_change` (survey, propose, confirm, write), `revit_model_audit`, `revit_pre_issue_check`, `revit_stairs`. Limits: Family Editor out of scope; one Revit instance per session; Revit Viewer not supported; `send_code` runs arbitrary C#.
- **Horizun** [20]: permission profiles `safe_write`, `full_write`, `unsafe_code`; starts with a 14-tool `esencial` profile; rehearsal + post-commit verification; jobs with persistent IDs. **IFC/openBIM tools**: `horizun_plan_from_ifc` (plan Revit elements from an IFC under a declared mapping, no import), `horizun_apply_ifc_plan`, `horizun_deliver_ifc` (export IFC and check IDS, pset mapping, georeference, BCF of failures), `horizun_validate_ids`, `horizun_export` format `ifc`, `horizun_information_container` (ISO 19650), `horizun_cde_cloud` (ACC/OpenCDE). Self-reported benchmark: local qwen3:8b completed 12 of 27 test tasks, Claude Haiku 26 of 27 (vendor claim, "(unverified)"). Registry shows v4.0.0 as an MCPB bundle [33]; the README mixes version labels.
- **Demolinator pyRevit server** [51]: only server read with a plain `export_ifc` tool: "exports the model to IFC2x3 or IFC4". Also `check_clashes`, `link_file` (DWG, DXF, DGN, SAT, SKP, 3DM, RVT), `execute_revit_code` (IronPython).
- **shuotao REVIT_MCP_study** [49]: 239 tools, 94 domain SOP files, 61 skills; interactive clash viewer (`detect_clashes`) via the MCP Apps extension; one AI client at a time (second client gets HTTP 409); WebSocket `ws://localhost:8964`. README is English with a Traditional Chinese version (README.zh-TW). Prompts: "dimension every wall on this view", "check the curtain-wall elevations".

### 4.3 Revit and IFC specifically
Only a minority of Revit servers have any IFC tool: Horizun (`deliver_ifc`, `plan_from_ifc`) [20], Demolinator (`export_ifc`, IFC2x3/IFC4) [51], rvt-mcp (export helpers, details not read) [21]. The popular revit-mcp lineage has none [17]. Therefore "export this Revit model to IFC4 with Reference View" may simply have no tool on many servers; the correct behaviour is then an honest refusal or fallback to `send_code_to_revit` (risky). (General Revit knowledge, not from these READMEs: Revit's own IFC export uses the Autodesk open-source IFC exporter with settings such as IFC2x3 Coordination View 2.0 or IFC4 Reference/Design Transfer View; a tool that does not expose these options cannot be expected to choose them correctly.)

---

## 5. Other authoring tools

| Product | Server | URL | Stars | Notes |
|---|---|---|---|---|
| Archicad | tapir-archicad-MCP | https://github.com/SzamosiMate/tapir-archicad-MCP | 131, MIT [6][22] | Wraps community Tapir add-on + official JSON API; 191+ commands exposed through 3 generic tools: `archicad_list_commands`, `archicad_get_command_schema`, `archicad_call_tool`; plus `discovery_list_active_archicads`, `archicad_get_job` (long commands > 45 s return a job handle). Alpha. Multi-instance by port. README prompts: "check what Archicad projects I have running", "using port 19723 get all Wall elements" |
| Archicad | lgradisar/archicad-mcp (37), alesdev88/Archicad-MCP (10), bleufeng/mepbridge-acaistr, Boti-Ormandi, chronista-club (C++ add-on over Unix socket), davidharutyunyan/archicad-mcp-connector (250+ tools, Archicad 26) | [6] | | alesdev88 is in the MCP Registry v0.13.1, "delivery-readiness QA ... Archicad 29" with Windows/macOS MCPB bundles [35] |
| Archicad (Russian UI) | streletskiy/archi-helper | https://github.com/streletskiy/archi-helper | 2, MIT [6][50] | Windows chat app (README in Russian, "describe the task in plain words"); modes: view-only / confirm changes / full access; needs Tapir; not a Graphisoft product; advises saving a PLN backup |
| Tekla Structures | teknovizier/tekla_mcp_server | https://github.com/teknovizier/tekla_mcp_server | 62, GPL-3.0 [7][23] | Modules: Selection, View, Properties, Components, Operations, Drawings, Modeling; read-only mode; tested with Tekla 2022 and 2026; semantic attribute mapping opt-in. Others: YuriyKirillov/TeklaMCPServer, osc-bouw/TeklaMCP, iflow-mcp 115-tool variant [7] |
| Navisworks | HorizunGroup/naviscoord-mcp | https://github.com/HorizunGroup/naviscoord-mcp | 21, MIT [3][8] | Navisworks 2024-2026, clash detection/coordination. Others: Aitology/Navisworks_MCP, bimwright/nwd-mcp, kikki PoC for Manage 2026 [8] |
| Multi-app | General-Soju/BimOnMcp, hmertkaramann/aec-pilot-mcp ("550+ actions"), BURAK-BIM, ScanBIM (npm `@scanbim-labs/scanbim-mcp`, 46 tools via APS) | [8][34] | | Revit + Navisworks + AutoCAD (+Dynamo) in one server |
| Multi-app (registry) | bim-cli | https://github.com/HelloHowAreYouHaveANiceDay/bim-cli-plugin | | "Lets agents drive Revit, AutoCAD, SketchUp, Blender, and PDF sets on a Windows desktop" v0.35.1 [34] |
| Vectorworks | vicquick/vwx-mcp | https://github.com/vicquick/vwx-mcp | 20, MIT [1] | "Vectorworks 2026, 248 tools" |
| SketchUp | mhyrr/sketchup-mcp (534), zinin/sketchup-mcp2 (58), iamahsanmehmood/saie (14; 67+ tools) | [54][3] | | Mostly mesh/SketchUp modeling, little IFC |
| Rhino | tanishqbhattad/rhino-mcp | | 34 [3] | Rhino 8, 128 tools |
| Browser 3D editor | pascalorg/editor | https://github.com/pascalorg/editor | 25,350 [3] | "3D architectural editor with CLI and MCP tools" (not read in detail; "BIM" hit is by popularity, not IFC depth, "(unverified)") |
| Speckle | bimgeek/speckle-mcp (14), Daviidro/speckle-mcp (8 tools) | [9] | | No official Speckle MCP repo found in the specklesystems org via GitHub search [9][59] (checked 2026-11-06 only) |
| Cost/BIM data | Daviidro, BC3 export in Bonsai_mcp | [12] | | |

---

## 6. Autodesk Platform Services (APS) and cloud-data servers

| Server | Status | What it does |
|---|---|---|
| Autodesk/ai-integrations (official) [42] | Public repo, 1 star, 17 commits | Two official integrations: **Autodesk Product Help MCP** (hosted, Streamable HTTP, read-only access to Autodesk Help docs, "over 110 products", no API key; registry name `com.autodesk.aps.api/product-help-mcp` v1.0.12) and **Autodesk Fusion MCP** (local, creates/inspects geometry in running Fusion; v1.0.1) [36][42]. Revit, AEC Data Model, ACC are NOT mentioned in that repo [42] |
| autodesk-platform-services/aps-aecdm-mcp-dotnet [41][43] | 40 stars, MIT, "first experiment", .NET 8 | 7 tools: `GetToken` (PKCE), `GetHubs`, `GetProjects`, `GetElementGroupsByProject`, `GetElementsByElementGroupWithCategoryFilter`, `RenderModel`, `HighLightElements` (AEC Data Model GraphQL + Viewer). Hubs must be provisioned for your APS app |
| autodesk-platform-services/aps-mcp-server-nodejs [39] | Archived (last push 2026-05-07), 25 stars | ACC access using Secure Service Accounts; prompts: "What ACC projects do I have access to?", "Give me a visual dashboard of all issues in project XYZ" |
| autodesk-platform-services/aps-mcp-app-example [40] | Active, push 2026-11-05 | MCP Apps example: viewer UI resource + tools `preview-design`, `get-viewer-token`, and viewer tools `select`, `isolate`, `color`; prompts "Are there any Revit designs?", "Show me the HVAC design" |
| aps-mcp-auth-examples, aps-mcp-server-python, aps-aecdm-plant3D-mcp-python [10][43] | examples | Reference auth approaches / Plant 3D via AECDM |
| petrbroz/aps-mcp-server (41), kpphillips/aps-mcp-server, KenLP/acc-forma-mcp-server (approval-gated writes + audit log), vidatayebati/Autodesk-MCP (read-only Forma) [10] | community | |
| Sam-AEC/autodesk-revit-mcp-server (registry) | third-party despite the name | Local bridge, env vars `MCP_REVIT_WORKSPACE_DIR`, `MCP_REVIT_ALLOWED_DIRECTORIES`, `MCP_REVIT_MODE` [36] |

The APS blog has "MCP" and "AI" tags and an "AEC Data Model API" tag, but I could not load individual posts (see Sources, https://aps.autodesk.com/blog). "Autodesk Assistant" product pages returned 403/404 in this research, so its exact capabilities and any MCP link are "(unverified)".

---

## 7. Vendor AI assistants and MCP offerings

| Vendor | What was verified | Source |
|---|---|---|
| **Autodesk** | Official, small-scope MCP servers published in `Autodesk/ai-integrations` (Product Help, Fusion). APS team publishes sample/experimental MCP servers for ACC and AEC Data Model (see section 6). "Autodesk Assistant" is referenced as a navigation item on Autodesk help pages, but its features were not retrievable ("unverified"). No official Autodesk Revit MCP server was found in the registry or GitHub orgs searched | [36][42][43] |
| **Bentley** | Official **Bentley MCP servers** page: STAAD.Pro and STAAD Foundation Advanced (downloadable; sandboxed), MicroStation (Early Access, DGN read/write through Python API), iTwin IoT, AssetWise ALIM (built on Microsoft Copilot), ProjectWise (semantic search/Q&A over documents, multilingual), PLS-CADD (read-only PLS-GRID queries), TOWER and PLS-POLE (loopback only). Works with Claude, GitHub Copilot, Gemini. Most are "request access". No named tool lists published. Page copyright 2026; a news item dated 2026-08-13 | [44][45][61] |
| **Graphisoft (Archicad)** | No official MCP server found; the Archicad ecosystem relies on the community Tapir add-on + JSON API, wrapped by community MCP servers (section 5). Graphisoft AI pages I tried returned 404, so official AI Visualizer / AI Assistant status is "(unverified)" | [22][50] |
| **Trimble** | No official Trimble MCP repo found on GitHub; community servers: Trimble Connect (nhantruong96/trimble-connect-mcp, Core API v2), SketchUp (sheares/sketchup-mcp), AutoCAD + Trimble Connect Desktop (xuantinhnbs-rgb, Vietnamese docs), Trimble X9 scanner API. Official AI products (e.g. in Trimble Connect/SketchUp) not verified | [53] |
| **Speckle** | No official MCP repo found; community: bimgeek/speckle-mcp, Daviidro/speckle-mcp | [9][59] |
| **buildingSMART / IfcOpenShell** | GitHub search for "mcp" inside the buildingSMART and IfcOpenShell organisations returned zero repos; MCP for IFC is entirely community-driven | [60] |

**BIM GPTs / copilots**: not systematically researched (no web search budget left); do not assume specific GPT-store names exist. Related open-source: `mac999/BIM_LLM_code_agent` (39 stars, LLM code agent for BIM with vector + graph RAG), `louistrue/agentic-bim-team` (multi-agent Swiss residential design), `alvin528/CAD2BIM` (agent skill: floor plan to IFC/GLB/OBJ/STL), `ArchSightLabs/archsight-aios` (skills for BIM/IFC/RAG/code review, 29 stars) [1][3][62].

---

## 8. Registries and lists

| Registry | Result |
|---|---|
| Official MCP Registry (registry.modelcontextprotocol.io API) | Read. Hits: IFC (3 real: ifc-ruhsat, flinker-app/ifc-mcp, ifc-viewer-mcp), Revit (aecomcps, Horizun, vn-revit-mcp), BIM (scanbim, bim-cli, bim.house remote `https://bim.house/mcp` "generates BIM, checks code and structure, and quotes materials"), Archicad (alesdev88), Autodesk (3), Blender (generic only), Speckle (0) [32][33][34][35][36][37] |
| punkpeye/awesome-mcp-servers | Only the first 100k chars of a ~1.5 MB README were read: entries for Blender, FreeCAD, SolidWorks, Fusion 360, Maya, Inventor and `sharafutdinovdi/revit-model-mcp` (under Art & Culture). IFC entries not confirmed; the rest of the list was not read [38] |
| modelcontextprotocol/servers | Not read |
| smithery.ai, mcp.so, glama.ai, mcpservers.org | Not read (WebSearch budget exhausted; direct fetch not attempted). Many listed servers are probably mirrors of the GitHub repos above |
| PyPI | Only `ifc-ruhsat` 0.2.1 verified [57]. Most Python servers here say "clone the repo" and are not on PyPI (e.g. [16]) |
| npm | `ifc-mcp` 0.2.0, `@ifc-lite/mcp` 0.29.0, `@shuotao/revit-mcp-server`, `revit-mcp`, `mcp-server-for-revit`, etc. [30][31] |

---

## 9. Capability matrix (from READMEs; blank/"?" = not documented)

Legend: R = read/query, W = create/edit elements, X = arbitrary code tool, IFC-in = reads IFC files, IFC-out = exports IFC, IDS = IDS authoring/validation, BCF = BCF, Qty = quantities, Clash = clash detection, Img = screenshot/render.

| Server | Needs app | R | W | X | IFC-in | IFC-out | IDS | BCF | Qty | Clash | Img |
|---|---|---|---|---|---|---|---|---|---|---|---|
| smartaec/ifcMCP | no | yes | no | no | yes | no | no | no | no | no | no |
| ekkodale/IFC-MCP | no | yes | no | no | yes | no | no | no | stats | no | no |
| Daviidro/ifcopenshell-mcp | no | yes | no | no | yes | GLB only | no | no | yes | no (roadmap) | no |
| flinker-app/ifc-mcp | no | yes | creates simple IFC | Python (Pyodide) | yes | yes (generated) | ? | yes (view) | CSV reports | no | viewer |
| ifc-lite MCP | no | yes | yes (edit/undo) | ? | yes | yes | yes (CLI) | yes | ? | yes (CLI) | viewer |
| ifc-ids-mcp | no | IDS | IDS files | no | validate | no | yes | no | no | no | no |
| ifc-ruhsat | no | yes | no | no | yes | no | IDS files | no | no | no | no |
| ifcx-mcp | no | no | yes (IFC5) | no | no | IFCX | validate | yes | no | no | glTF preview |
| Bonsai_mcp (Jota) | Blender+Bonsai | yes | place object | yes | yes | saved IFC | no | no | yes | no | yes |
| ifc-bonsai-mcp | Blender+Bonsai | yes | many | yes | yes | yes | no | no | ? | no | yes |
| Show2Instruct/bonsai-mcp | Blender+Bonsai | yes | via code | yes | yes | `save_ifc_file` | no | no | yes | no | yes |
| revit-mcp lineage | Revit | yes | yes | C# | no | no | no | no | material qty | no | no |
| rvt-mcp | Revit | yes | yes | C# | ? | export helpers | no | no | ? | yes | ? |
| aec-model-bridge | Revit (+IFC w/o) | yes | yes (approval) | IronPython | yes (read) | via Revit? | no | no | ? | Navisworks (WIP) | ? |
| Horizun | Revit | yes | yes | Python (opt-in) | plan from IFC | yes + verify | yes | yes | yes | yes | ? |
| Demolinator pyRevit | Revit | yes | yes | IronPython | link | IFC2x3/IFC4 | no | no | yes | yes | no |
| Tapir Archicad MCP | Archicad | yes | yes | no | not mentioned | not mentioned | no | no | ? | no | ? |
| tekla_mcp_server | Tekla | yes | yes | ? | not mentioned | not mentioned | no | no | ? | no | ? |
| naviscoord-mcp | Navisworks | yes | n/a | ? | ? | n/a | no | no | ? | yes | ? |
| APS AECDM dotnet | Autodesk cloud | yes | no | no | no | no | no | no | ? | no | Viewer |

---

## 10. What this means for realistic test requests

1. **Match the request to the server class.** For IFC-file servers ask "inventory/property/space/quantity/validate/diff" questions. For Revit servers ask about the *active view*, levels, rooms, parameters, sheets. Do not ask a Revit server to "validate against IDS" or a read-only IFC server to "add a wall".
2. **Identifiers matter.** IFC answers should use `GlobalId` (22-character base64-like string), IFC class names (`IfcWall`, `IfcDoor`, `IfcSpace`, `IfcBuildingStorey`) and psets such as `Pset_WallCommon.FireRating`. Revit answers use element IDs (integers) and Revit categories/parameters (Comments, Mark, Level). A judge should reject mixing them up.
3. **Schema awareness.** Several READMEs never state IFC versions [12][13][15][16][25][27]. Good test: give an IFC2x3 file and an IFC4X3 file and check whether the server notices differences (e.g. IFC4X3 `IfcFacility`/`IfcRoad` do not exist in 2x3; ifc-ruhsat flags IFC4 as insufficient [29]).
4. **Write operations are the risky class.** Test dry-run/approval behaviour (`ask_first`, `look_only`, rehearsal) [19][20], undo (Ctrl+Z per action), and unsaved-model behaviour (Bonsai: `save_ifc_file`, empty IFC must be saved first [15][16]).
5. **Expected honest failures**: tool not present (IFC export on revit-mcp lineage), no active document, view not a plan, Revit year unsupported, Blender add-on not connected, unloaded links [17][20], large file timeout (>1 min in flinker-app) [25], geometry-less IFC cannot become GLB [28].
6. **Code-execution tools change the evaluation.** If an answer was produced by `send_code_to_revit` / `execute_blender_code`, check it was necessary; results are "self-reported" in Horizun (`host_verified: false`) [20].
7. **Language of prompts.** READMEs include Turkish (ifc-ruhsat), Traditional Chinese (REVIT_MCP_study), Russian (archi-helper), Vietnamese docs [29][49][50][53]. Multilingual prompts (RU/ZH) are realistic, but tool names stay English; elements keep their Revit-localized family names, which breaks naive name matching.
8. **Model quality matters**: with Horizun's own benchmark, small local models failed over half of 27 tasks [20]; expect weaker tool selection on small models and on servers with 200+ tools (hence "facade"/"compact" schema modes and 3-tool designs like Tapir [20][22]).

### Example test requests by category (illustrative)
- IFC file: "How many IfcWall and IfcDoor are in model.ifc, grouped by storey?"; "List spaces with area over 20 m2 and their names"; "Which walls have no FireRating in Pset_WallCommon?"; "Compare v1.ifc and v2.ifc: which GlobalIds were added or deleted?"; "Convert this IFC to GLB."
- IDS: "Create an IDS 1.0 spec requiring every IfcWall to have Pset_WallCommon.FireRating from the list 30/60/90, then check model.ifc."
- Bonsai: "Create a 5 m wall from (0,0) to (5,0), height 3 m, then add a door in it; save the IFC"; "Georeference the model to EPSG:2056."
- Revit: "List all rooms on Level 2 with area"; "Tag all walls in the active view"; "Create a level at 3.0 m"; "Export the model to IFC4" (expect refusal on servers without IFC tools).
- Archicad/Tekla: "Get all Wall elements" (Tapir); "Select beams with profile HEA200" (Tekla; illustrative, "(unverified)").
- ACC/APS: "What ACC projects do I have access to?", "Are there any Revit designs?" [39][40].

---

## Typical questions people ask about this

Real README examples are linked; others are marked illustrative.

1. "Analyze this IFC model and tell me how many walls, doors and windows it has." (README prompt [12])
2. "Show me the spatial structure of this building model." (README [12])
3. "Generate a BC3 budget file in Spanish for the current IFC model." (README [12])
4. "List every wall in the model with its fire rating." (README [16])
5. "How many fire doors are on Level 2?" (README [28])
6. "What changed since last week's version?" (README [28])
7. "Count the walls, doors, windows, spaces, and property sets in sample.ifc." (README [25])
8. "Find missing names, classifications, and suspicious property values in this IFC file." (README [25])
9. "Apply this BCF viewpoint in the open IFC viewer." (README [25])
10. "Read the active model's warnings, group them by description and show affected element IDs." (README [19])
11. "Find walls on Level 02 and propose setting Comments to 'Coordination reviewed'." (README [19])
12. "What ACC projects do I have access to?" (README [39])
13. "Dimension every wall on this view." (README [49])
14. "Classify all walls as Uniclass Ss_25_10_30 and resolve via bSDD." (README [24])
15. "Using port 19723, get all the Wall elements from the project." (README [22])
16. "Which MCP server should I use to let Claude edit my Revit model safely?" (illustrative)
17. "Does any MCP server export Revit to IFC4 with a given MVD?" (illustrative; see 4.3)
18. "Can the AI check my IFC against my project's IDS and give a BCF?" (illustrative; ifc-ids-mcp [14], Horizun [20], ifcx-mcp [24])
19. "Why does the server say 'No active document' / 'Blender not connected'?" (illustrative)
20. "Is it safe to let the AI run `execute_blender_code` or `send_code_to_revit`?" (illustrative; vendors warn [12][17][21])
21. "Is there an official Autodesk / Graphisoft / Trimble / Bentley MCP?" (illustrative; see section 7)
22. "Why are there so many Revit MCP servers and which is the maintained one?" (illustrative; original revit-mcp archived, successor monorepo [17][18])

---

## Common pitfalls and misconceptions

- **"IFC MCP" search noise**: IFC also means information flow control, International Finance Corporation, "IFC" import duty; GitHub results include many unrelated repos [1][32].
- **Star count is not quality**: 25k-star `pascalorg/editor` is a general 3D editor, not an IFC QA tool [3]; Revit lineage stars (477) belong to an archived repo [18].
- **Archived/renamed projects**: `revit-mcp` archived (last push 2026-02-25) in favour of `mcp-servers-for-revit` [18]; `aps-mcp-server-nodejs` archived (last push 2026-05-07) [39]; `ifc-bonsai-mcp` superseded by `bonsai-mcp` [16].
- **README inconsistencies**: "Eleven IFC tools" vs fifteen [12]; 90 vs 94 SOP files [49]; 38 vs 44 validation rules [52]; mixed version labels [20]. Do not use README numbers as ground truth for test expectations.
- **Tool counts depend on config**: rvt-mcp has 58/98/245/248 depending on mode [21]; Horizun 4/70/79/80 [20]; Tapir exposes 191+ commands through only 3 tools [22].
- **Revit is not IFC-native**: IFC content read from a Revit session reflects Revit's categories/parameters, not IFC classes/psets; and servers that read IFC files (aec-model-bridge IFC provider) are read-only [19].
- **"Works with Revit 2026" is not verified**: aec-model-bridge states none of its builds were verified in live Revit [19].
- **Security**: Bonsai bridge has no authentication on localhost [16]; some servers enable CORS for all origins in Docker mode [12]; code tools run with the host process's permissions [19][21]. Never expose these ports to a network.
- **Not published packages**: many repos require cloning; running unvetted code is out of scope for this catalog (nothing was installed during research).
- **Vendor-claimed benchmarks and regulation details** (Horizun's 12/27 vs 26/27, Turkish regulation numbers) are self-reported (unverified).

---

## Gaps

- WebSearch ran out of budget after the first GitHub/registry queries; **Chinese, Japanese and Russian** web content (blogs, CSDN, Zenn/Qiita, Habr, Telegram) could not be searched. Only repo-level evidence in those languages was found: a Chinese-described `wbh0168/revit_mcp` (0 stars) [58], Traditional-Chinese README [49], Russian README `archi-helper` [50] and Russian-described `Davud77/bp-revit-tools` (Revit 2026, Codex MCP, Archicad-to-Revit transfer; not read in detail) [6]. Qiita and Habr direct fetches returned no usable results.
- Not read: smithery.ai, mcp.so, glama.ai, mcpservers.org, modelcontextprotocol/servers; full awesome-mcp-servers list (only first ~100k of 1.5M chars).
- Not read in detail: oakplank/RevitMCP, LuDattilo servers, mcp-server-for-revit-python, vn-revit-mcp, lgradisar/alesdev88 Archicad servers, ifc-lite MCP tool list, ifc-viewer-mcp tool list, ifc-console, pascalorg/editor.
- Vendor AI: Autodesk Assistant, Graphisoft AI Assistant/AI Visualizer, Trimble official AI offerings, and BIM GPTs (GPT store) could not be verified; some vendor URLs returned 403/404 (I did not retry via mirrors).
- No suspicious/pirated sites were encountered or linked.
- No real forum questions (e.g. Autodesk/OSArch forums) were retrieved; "typical questions" are README-derived or illustrative.

---

## Sources

GitHub search (API JSON pages, read 2026-11-06):
[1] https://api.github.com/search/repositories?q=ifc+mcp&sort=stars&per_page=20
[2] https://api.github.com/search/repositories?q=revit+mcp&sort=stars&per_page=20
[3] https://api.github.com/search/repositories?q=bim+mcp&sort=stars&per_page=20
[4] https://api.github.com/search/repositories?q=ifcopenshell+mcp&sort=stars&per_page=15
[5] https://api.github.com/search/repositories?q=bonsai+mcp&sort=stars&per_page=15
[6] https://api.github.com/search/repositories?q=archicad+mcp&sort=stars&per_page=15
[7] https://api.github.com/search/repositories?q=tekla+mcp&sort=stars&per_page=15
[8] https://api.github.com/search/repositories?q=navisworks+mcp&sort=stars&per_page=12
[9] https://api.github.com/search/repositories?q=speckle+mcp&sort=stars&per_page=12
[10] https://api.github.com/search/repositories?q=autodesk+aps+mcp&sort=stars&per_page=12
[11] https://api.github.com/search/repositories?q=blender+bim+mcp&sort=stars&per_page=12

Repositories (README pages):
[12] https://github.com/JotaDeRodriguez/Bonsai_mcp
[13] https://github.com/smartaec/ifcMCP
[14] https://github.com/vinnividivicci/ifc-ids-mcp
[15] https://github.com/Show2Instruct/ifc-bonsai-mcp
[16] https://github.com/Show2Instruct/bonsai-mcp
[17] https://github.com/mcp-servers-for-revit/mcp-servers-for-revit
[18] https://github.com/mcp-servers-for-revit/revit-mcp
[19] https://github.com/Sam-AEC/aec-model-bridge
[20] https://github.com/HorizunGroup/horizun-revit-mcp
[21] https://github.com/bimwright/rvt-mcp
[22] https://github.com/SzamosiMate/tapir-archicad-MCP
[23] https://github.com/teknovizier/tekla_mcp_server
[24] https://github.com/louistrue/ifcx-mcp
[25] https://github.com/flinker-app/ifc-mcp
[26] https://github.com/LTplus-AG/ifc-lite
[27] https://github.com/ekkodale/IFC-MCP
[28] https://github.com/Daviidro/ifcopenshell-mcp
[29] https://github.com/BerkantACUN/ifc-ruhsat
[39] https://github.com/autodesk-platform-services/aps-mcp-server-nodejs
[40] https://github.com/autodesk-platform-services/aps-mcp-app-example
[41] https://github.com/autodesk-platform-services/aps-aecdm-mcp-dotnet
[42] https://github.com/Autodesk/ai-integrations (and https://raw.githubusercontent.com/Autodesk/ai-integrations/main/README.md)
[49] https://github.com/shuotao/REVIT_MCP_study
[50] https://github.com/streletskiy/archi-helper
[51] https://github.com/Demolinator/revit-mcp-server
[52] https://github.com/j03rul4nd/ifc-viewer-online

Package registries and MCP registry:
[30] https://registry.npmjs.org/-/v1/search?text=ifc%20mcp&size=20
[31] https://registry.npmjs.org/-/v1/search?text=revit%20mcp&size=20
[32] https://registry.modelcontextprotocol.io/v0/servers?search=ifc&limit=30
[33] https://registry.modelcontextprotocol.io/v0/servers?search=revit&limit=40
[34] https://registry.modelcontextprotocol.io/v0/servers?search=bim&limit=40
[35] https://registry.modelcontextprotocol.io/v0/servers?search=archicad&limit=20
[36] https://registry.modelcontextprotocol.io/v0/servers?search=autodesk&limit=40
[37] https://registry.modelcontextprotocol.io/v0/servers?search=blender&limit=40
[38] https://raw.githubusercontent.com/punkpeye/awesome-mcp-servers/main/README.md
[56] https://registry.modelcontextprotocol.io/v0/servers?search=speckle&limit=20 (0 results)
[57] https://pypi.org/pypi/ifc-ruhsat/json

Other searches:
[43] https://api.github.com/search/repositories?q=aec+data+model+mcp&per_page=10
[53] https://api.github.com/search/repositories?q=mcp+trimble&sort=stars&per_page=10
[54] https://api.github.com/search/repositories?q=mcp+sketchup&sort=stars&per_page=8
[58] https://api.github.com/search/repositories?q=revit+mcp+模型上下文 (URL-encoded); and https://aps.autodesk.com/blog and https://aps.autodesk.com/blog?tag=MCP (tags only)
[59] https://api.github.com/search/repositories?q=mcp+org:specklesystems (0 results) and https://github.com/specklesystems
[60] https://api.github.com/search/repositories?q=mcp+org:buildingSMART and ...org:IfcOpenShell (0 results each)
[62] https://api.github.com/search/repositories?q=ifc+llm+agent&sort=stars&per_page=12

Vendors and papers:
[44] https://www.bentley.com/en/infrastructure-ai/mcp-servers/
[45] https://www.bentley.com/en/infrastructure-ai/
[61] https://www.bentley.com/software/itwin-platform/
[46] https://arxiv.org/abs/2511.05533 (MCP4IFC)
[47] https://arxiv.org/abs/2601.00809 (modular reference architecture)
[48] http://export.arxiv.org/api/query?search_query=all:%22model+context+protocol%22+AND+all:BIM&max_results=10 (lists 2510.02634 building code review; 2611.02286 review of agentic AI-ready workflows, dated 2026-11-01, not read in detail)
