# INDEX — every document in the knowledge base / Карта всех файлов

Back to [README](README.md) | New to BIM? [00_START_HERE_EN.md](00_START_HERE_EN.md) (EN) · [00_START_HERE_RU.md](00_START_HERE_RU.md) (RU)

All descriptions are in English; the base itself is mostly English with Russian-first entry points. Documents under `research_raw/` are raw material and are summarised per folder at the bottom. Research wave 2 (more languages and countries) is still being added, so this index will grow.

Quick picks:

| I want to... | Open |
|---|---|
| understand IFC from zero | [00_START_HERE_EN.md](00_START_HERE_EN.md) |
| generate realistic test requests with an LLM | [07_mcp_testing/llm_generation_prompt.md](07_mcp_testing/llm_generation_prompt.md) |
| take ready requests | [prompt_bank_en.md](07_mcp_testing/prompt_bank_en.md), [prompt_bank_ru.md](07_mcp_testing/prompt_bank_ru.md), [prompt_bank_multilingual.md](07_mcp_testing/prompt_bank_multilingual.md) |
| judge an answer | [07_mcp_testing/evaluation_rubric.md](07_mcp_testing/evaluation_rubric.md) |
| see what hurts people most | [05_real_world_questions/pain_points_top100.md](05_real_world_questions/pain_points_top100.md) |
| find a source or community | [09_sources/sources_index.md](09_sources/sources_index.md), [09_sources/communities_directory.md](09_sources/communities_directory.md) |

---

## Root

| File | Description |
|---|---|
| [README.md](README.md) | Bilingual (RU then EN) overview: purpose, audience, folder table, how to use with an LLM, quick start, coverage, methodology, disclaimer. |
| [00_START_HERE_RU.md](00_START_HERE_RU.md) | Russian primer for a tester with no BIM background: IFC in plain words, 15 terms, top-10 pain points, how to write test questions, links. |
| [00_START_HERE_EN.md](00_START_HERE_EN.md) | The same primer in English. |
| INDEX.md | This file. |

## 01_ifc_basics — IFC in plain words

| File | Description |
|---|---|
| [00_ifc_in_real_projects.md](01_ifc_basics/00_ifc_in_real_projects.md) | How IFC is used in real projects: why it exists, workflows, roles and deliverables; why a tester should care. |
| [01_what_is_ifc_and_versions.md](01_ifc_basics/01_what_is_ifc_and_versions.md) | What IFC is, history and version table (IFC2x3, IFC4, IFC4.3, IFC5), buildingSMART and ISO, MVDs, which version to pick. |
| [02_ifc_file_anatomy.md](01_ifc_basics/02_ifc_file_anatomy.md) | Inside an `.ifc` file: STEP/SPF syntax, header, instance lines, GlobalId, string encoding (`\X2\`), ifcXML/ifcZIP/ifcJSON, a tiny annotated example. |
| [03_entities_cheat_sheet.md](01_ifc_basics/03_entities_cheat_sheet.md) | The ~150 IFC classes people actually meet (`IfcWall`, `IfcSpace`, `IfcPipeSegment` ...). |
| [04_spatial_structure_and_relationships.md](01_ifc_basics/04_spatial_structure_and_relationships.md) | Project/site/building/storey hierarchy and `IfcRel*` relationships (what is "on level 2" and why). |
| [05_properties_quantities_psets.md](01_ifc_basics/05_properties_quantities_psets.md) | Property sets (`Pset_`), quantity sets (`Qto_`), where fire rating or area really live. |
| [06_geometry_placement_coordinates_units.md](01_ifc_basics/06_geometry_placement_coordinates_units.md) | Geometry representations, placement, coordinates, georeferencing and units. |
| [07_materials_classification_types_styles.md](01_ifc_basics/07_materials_classification_types_styles.md) | Materials, classification, types vs instances, colours/styles and layers. |
| [08_domains_mep_structural_infra_4d5d_fm.md](01_ifc_basics/08_domains_mep_structural_infra_4d5d_fm.md) | Domain slices: MEP, structural, infrastructure (IFC 4.3), 4D/5D, FM/COBie. |

## 02_standards_regulations — standards and national rules

| File | Description |
|---|---|
| [buildingsmart_standards.md](02_standards_regulations/buildingsmart_standards.md) | The buildingSMART family: IFC, IDS, BCF, bSDD, MVD, IDM, OpenCDE, validation, certification. |
| [iso_and_european_standards.md](02_standards_regulations/iso_and_european_standards.md) | ISO/CEN standards around IFC: 16739, 19650, 7817 (LOIN), 12006, 29481 and others. |
| [requirements_in_contracts_eir_bep.md](02_standards_regulations/requirements_in_contracts_eir_bep.md) | How IFC requirements are written into EIR/BEP/BIM manuals, with real examples. |
| [national/russia.md](02_standards_regulations/national/russia.md) | Russia (very detailed): ТИМ, expert review, АГР, national standards, IFC requirements. |
| [national/china_mainland.md](02_standards_regulations/national/china_mainland.md) | Mainland China: GB/T BIM standards and BIM-based review. |
| [national/singapore.md](02_standards_regulations/national/singapore.md) | Singapore (very detailed): CORENET X and IFC-SG. |
| [national/uk_ireland.md](02_standards_regulations/national/uk_ireland.md) | UK and Ireland: ISO 19650, Uniclass, national BIM policy. |
| [national/germany_austria_switzerland.md](02_standards_regulations/national/germany_austria_switzerland.md) | Germany, Austria, Switzerland: roadmaps and client requirements. |
| [national/france_francophone.md](02_standards_regulations/national/france_francophone.md) | France and the French-speaking world: BIM conventions and requirements. |
| [national/netherlands_belgium_luxembourg.md](02_standards_regulations/national/netherlands_belgium_luxembourg.md) | Benelux: public-client policies and information delivery specifications. |
| [national/nordics_baltics.md](02_standards_regulations/national/nordics_baltics.md) | Nordic and Baltic countries: early IFC adopters and client requirements. |
| [national/spain_portugal_italy.md](02_standards_regulations/national/spain_portugal_italy.md) | Spain, Portugal, Italy: public-works BIM rules (Italy's 2025 obligation). |
| [national/japan_korea.md](02_standards_regulations/national/japan_korea.md) | Japan and South Korea: ministry-led programmes, BIM drawing review. |
| [national/latin_america.md](02_standards_regulations/national/latin_america.md) | Latin America: Brazil, Chile and others. |
| [national/north_america.md](02_standards_regulations/national/north_america.md) | USA and Canada: owner-driven requirements (GSA, USACE, states). |
| [national/central_eastern_europe.md](02_standards_regulations/national/central_eastern_europe.md) | Central and Eastern Europe (Poland, Czechia, Slovakia, Hungary, Romania, Baltics and others): BIM/IFC requirements. |
| [national/cis_central_asia.md](02_standards_regulations/national/cis_central_asia.md) | Kazakhstan, Belarus, Uzbekistan, Caucasus, Central Asia: BIM/ТИМ and IFC. |
| [national/middle_east.md](02_standards_regulations/national/middle_east.md) | Middle East and Turkey: BIM/IFC requirements (UAE, Saudi Arabia, Qatar, Turkey and others). |
| [national/africa.md](02_standards_regulations/national/africa.md) | Africa: BIM/IFC adoption and requirements. |
| [national/oceania_south_asia.md](02_standards_regulations/national/oceania_south_asia.md) | Australia, New Zealand, India and South Asia: BIM/IFC requirements. |
| [national/southeast_asia_other.md](02_standards_regulations/national/southeast_asia_other.md) | Malaysia, Vietnam, Indonesia, Thailand, Philippines: BIM/IFC requirements. |
| [national/taiwan_hongkong_macau.md](02_standards_regulations/national/taiwan_hongkong_macau.md) | Taiwan, Hong Kong, Macau: BIM/IFC requirements. |

## 03_software — tools around IFC

| File | Description |
|---|---|
| [authoring_tools_ifc.md](03_software/authoring_tools_ifc.md) | IFC in other authoring tools: Archicad, Tekla, Allplan, Vectorworks, Bentley, Civil 3D, BricsCAD, Renga and more. |
| [revit/ifc_export_reference.md](03_software/revit/ifc_export_reference.md) | Revit IFC export in full: setups, class mapping, parameters, property sets, batch export, known problems. |
| [revit/ifc_import_link_reference.md](03_software/revit/ifc_import_link_reference.md) | Revit IFC import and link: Open vs Link, DirectShape, coordinates, performance, issues by source application. |
| [viewers_checkers_cde_converters.md](03_software/viewers_checkers_cde_converters.md) | Viewers, model checkers, CDE platforms and converters. |

## 04_open_source — libraries, MCP servers, research

| File | Description |
|---|---|
| [libraries_and_toolkits.md](04_open_source/libraries_and_toolkits.md) | Open-source IFC libraries (IfcOpenShell, xBIM, web-ifc and others); most MCP servers wrap these. |
| [mcp_servers_and_ai_tools.md](04_open_source/mcp_servers_and_ai_tools.md) | Catalog of MCP servers and AI tools for IFC, BIM and Revit (documentation-based, not run). |
| [llm_bim_research_and_datasets.md](04_open_source/llm_bim_research_and_datasets.md) | Research on natural-language querying of BIM/IFC and LLM agents: papers, datasets, benchmarks. |
| [sample_ifc_files.md](04_open_source/sample_ifc_files.md) | Where to get sample IFC files and what each is good for. |
| [community_projects_and_enthusiasts.md](04_open_source/community_projects_and_enthusiasts.md) | Community projects, add-ins, national templates and enthusiasts around IFC. |

## 05_real_world_questions — real pains and questions

| File | Description |
|---|---|
| [pain_points_top100.md](05_real_world_questions/pain_points_top100.md) | The 100 most common and costly IFC / Revit-IFC pain points with phrasing in several languages, frequency, cause and fix. |

**By topic** (`by_topic/`):

| File | Description |
|---|---|
| [revit_export_and_class_mapping.md](05_real_world_questions/by_topic/revit_export_and_class_mapping.md) | Revit to IFC export, class mapping, proxies, types, families. |
| [import_and_interoperability.md](05_real_world_questions/by_topic/import_and_interoperability.md) | Importing IFC and cross-tool interoperability. |
| [properties_and_parameters.md](05_real_world_questions/by_topic/properties_and_parameters.md) | Properties, property sets and parameter mapping. |
| [quantities_cost_schedule.md](05_real_world_questions/by_topic/quantities_cost_schedule.md) | Quantity takeoff, cost (5D) and scheduling (4D). |
| [geometry_openings_curtainwalls_stairs.md](05_real_world_questions/by_topic/geometry_openings_curtainwalls_stairs.md) | Geometry quality, openings/voids, curtain walls, stairs and railings. |
| [coordinates_georef_units_levels.md](05_real_world_questions/by_topic/coordinates_georef_units_levels.md) | Coordinates, georeferencing, units, levels/storeys, spatial structure. |
| [materials_spaces_zones.md](05_real_world_questions/by_topic/materials_spaces_zones.md) | Materials, colours, layers; spaces, rooms, areas, zones, systems. |
| [mep_structural_rebar.md](05_real_world_questions/by_topic/mep_structural_rebar.md) | MEP systems, structural and analytical models, rebar/steel/precast. |
| [classification_cobie_fm.md](05_real_world_questions/by_topic/classification_cobie_fm.md) | Classification systems, bSDD, COBie and FM handover. |
| [validation_ids_model_checking.md](05_real_world_questions/by_topic/validation_ids_model_checking.md) | Validation, model checking and IDS. |
| [coordination_clash_bcf_cde.md](05_real_world_questions/by_topic/coordination_clash_bcf_cde.md) | Coordination, clash detection, BCF and CDE platforms. |
| [versions_mvd_encoding_guid.md](05_real_world_questions/by_topic/versions_mvd_encoding_guid.md) | IFC versions and MVDs, text encoding, GUIDs and change tracking. |
| [file_size_viewing_conversion.md](05_real_world_questions/by_topic/file_size_viewing_conversion.md) | File size and performance, viewing IFC, converting formats. |
| [infrastructure_site_gis_energy.md](05_real_world_questions/by_topic/infrastructure_site_gis_energy.md) | Infrastructure (IFC 4.3), site and terrain, GIS and digital twins, energy analysis. |
| [programming_and_automation.md](05_real_world_questions/by_topic/programming_and_automation.md) | Programming with IFC, Revit API automation, data extraction. |
| [regulations_permits_contracts.md](05_real_world_questions/by_topic/regulations_permits_contracts.md) | National requirements, permits and code checking, contracts/EIR/BEP/LOIN. |
| [ai_beginners_software_choice.md](05_real_world_questions/by_topic/ai_beginners_software_choice.md) | AI/LLM/MCP with IFC, beginner questions, software choice, licensing. |

**By persona** (`by_persona/`): who the asker is and how they talk.

| File | Description |
|---|---|
| [architect.md](05_real_world_questions/by_persona/architect.md) | Architect: model authoring, export to consultants, rooms and doors. |
| [bim_coordinator.md](05_real_world_questions/by_persona/bim_coordinator.md) | BIM coordinator: combining models, clashes, checking. |
| [bim_manager.md](05_real_world_questions/by_persona/bim_manager.md) | BIM manager: templates, export settings, naming, contract requirements. |
| [structural_engineer.md](05_real_world_questions/by_persona/structural_engineer.md) | Structural engineer: Tekla/Revit structure, analytical models, rebar. |
| [mep_engineer.md](05_real_world_questions/by_persona/mep_engineer.md) | MEP engineer: ducts, pipes, systems, ports. |
| [civil_infra_engineer.md](05_real_world_questions/by_persona/civil_infra_engineer.md) | Civil/infrastructure engineer: roads, rail, bridges, terrain, IFC 4.3. |
| [contractor_site.md](05_real_world_questions/by_persona/contractor_site.md) | Contractor and site team: receiving and using IFC on site. |
| [estimator_qs.md](05_real_world_questions/by_persona/estimator_qs.md) | Estimator / quantity surveyor: quantities and cost. |
| [facility_manager.md](05_real_world_questions/by_persona/facility_manager.md) | Facility manager: handover data, COBie, CAFM. |
| [owner_client.md](05_real_world_questions/by_persona/owner_client.md) | Owner / client: requirements and acceptance of models. |
| [reviewer_authority.md](05_real_world_questions/by_persona/reviewer_authority.md) | Reviewer / authority: permit and expert review checks. |
| [developer_programmer.md](05_real_world_questions/by_persona/developer_programmer.md) | Developer / programmer: libraries, viewers, add-ins, scripts. |
| [researcher_academic.md](05_real_world_questions/by_persona/researcher_academic.md) | Researcher / academic: IFC as research material. |
| [student_beginner.md](05_real_world_questions/by_persona/student_beginner.md) | Student / beginner: first contact with IFC. |

**By language** (`by_language/`): how people ask in each language.

| File | Description |
|---|---|
| [en.md](05_real_world_questions/by_language/en.md) | English. |
| [ru.md](05_real_world_questions/by_language/ru.md) | Russian (primary language of this base). |
| [zh.md](05_real_world_questions/by_language/zh.md) | Chinese (Simplified and Traditional). |
| [ja.md](05_real_world_questions/by_language/ja.md) | Japanese. |
| [ko.md](05_real_world_questions/by_language/ko.md) | Korean. |
| [de.md](05_real_world_questions/by_language/de.md) | German (DACH). |
| [es.md](05_real_world_questions/by_language/es.md) | Spanish (Spain and Latin America). |
| [pt.md](05_real_world_questions/by_language/pt.md) | Portuguese (mostly Brazil; almost all synthetic). |
| [fr.md](05_real_world_questions/by_language/fr.md) | French. |
| [it.md](05_real_world_questions/by_language/it.md) | Italian. |
| [nl.md](05_real_world_questions/by_language/nl.md) | Dutch. |
| [nordic.md](05_real_world_questions/by_language/nordic.md) | Norwegian, Danish, Swedish, Finnish. |
| [other.md](05_real_world_questions/by_language/other.md) | Arabic, Turkish, Greek, Czech and others (very thin data). |

## 06_how_people_write — voice and style

| File | Description |
|---|---|
| [style_guide.md](06_how_people_write/style_guide.md) | How real people write about IFC, Revit and openBIM: register, brevity, tone, level of detail. |
| [jargon_slang_dictionary.md](06_how_people_write/jargon_slang_dictionary.md) | Jargon and slang by language. |
| [name_variants_and_misspellings.md](06_how_people_write/name_variants_and_misspellings.md) | How people spell IFC, Revit and tool names in each language. |
| [anti_patterns_llm_questions.md](06_how_people_write/anti_patterns_llm_questions.md) | Tell-tale signs of LLM-invented questions, with side-by-side rewrites. |

## 07_mcp_testing — testing MCP servers

| File | Description |
|---|---|
| [what_ifc_mcp_servers_do.md](07_mcp_testing/what_ifc_mcp_servers_do.md) | What IFC / BIM / Revit MCP servers do: four kinds, capability matrix, realistic vs unrealistic requests, limits to probe. |
| [intent_taxonomy.md](07_mcp_testing/intent_taxonomy.md) | The 22 intents users have toward an IFC / Revit assistant. |
| [test_scenarios_library.md](07_mcp_testing/test_scenarios_library.md) | Library of 156 test scenarios. |
| [edge_cases_and_traps.md](07_mcp_testing/edge_cases_and_traps.md) | 22 traps that break assistants (schema differences, units, georeferencing, proxies, encodings, write safety ...). |
| [evaluation_rubric.md](07_mcp_testing/evaluation_rubric.md) | How to score an answer: dimensions, anchors, critical failures, worked examples, checklist. |
| [llm_generation_prompt.md](07_mcp_testing/llm_generation_prompt.md) | Ready-to-paste prompts (RU and EN) to generate realistic requests, multi-turn scripts and judge prompts. |
| [variation_matrix.md](07_mcp_testing/variation_matrix.md) | Dice-style tables for randomising requests, with worked rolls. |
| [prompt_bank_en.md](07_mcp_testing/prompt_bank_en.md) | 280+ ready English test requests with notes. |
| [prompt_bank_ru.md](07_mcp_testing/prompt_bank_ru.md) | 220+ ready Russian test requests with English glosses. |
| [prompt_bank_multilingual.md](07_mcp_testing/prompt_bank_multilingual.md) | 170 requests in 14+ languages, each with an English gloss. |
| [revit_mcp_testing.md](07_mcp_testing/revit_mcp_testing.md) | Testing MCP servers that drive a running Revit: capabilities, 140+ task prompts, edge cases. |

## 08_glossary

| File | Description |
|---|---|
| [glossary_multilingual.md](08_glossary/glossary_multilingual.md) | Multilingual IFC/BIM/Revit glossary (EN, RU, ZH, ES, PT, DE, FR, JA, KO, AR). |
| [abbreviations.md](08_glossary/abbreviations.md) | Abbreviations and acronyms, international and national. |
| [glossary_more_languages.md](08_glossary/glossary_more_languages.md) | Glossary for 12 more languages: IT, TR, PL, NL, CS, VI, ID, FA, HE, UK, KK, Nordic. |

## 09_sources

| File | Description |
|---|---|
| [sources_index.md](09_sources/sources_index.md) | Map of the web addresses the research and reference documents relied on. |
| [communities_directory.md](09_sources/communities_directory.md) | Where people discuss IFC and Revit (forums, repos, chats), by language and region. |

## exports — machine-readable data

| File | Description |
|---|---|
| [real_questions.jsonl](exports/real_questions.jsonl) / [real_questions.csv](exports/real_questions.csv) | All real records (paraphrased, with `source_url`), one per line / per row. Open the CSV in a spreadsheet. |
| [synthetic_prompts.jsonl](exports/synthetic_prompts.jsonl) / [synthetic_prompts.csv](exports/synthetic_prompts.csv) | All synthetic prompts with `expected_behavior`, `difficulty`, `needs_file`. |
| `kb_compact.md` | Single-file compact version for upload to a chat LLM. Built at the end of assembly; not present in every copy yet. |

## _meta and tools

| File | Description |
|---|---|
| [_meta/SPEC.md](_meta/SPEC.md) | Record schema, vocabularies and rules that all research agents followed. |
| [_meta/coverage_report.md](_meta/coverage_report.md) | Statistics after wave 1: records per language, persona, intent, topic, source type, tone, IFC version, file. |
| `_meta/METHODOLOGY.md` | Methodology (linked from the README); written at the end of assembly. |
| [tools/kb.py](tools/kb.py) | Command-line helper: `stats`, `filter` (by kind, lang, topic, persona, intent, type, text), `sections`. |

---

## research_raw — raw research, summarised per folder

Each research "cell" has two files with the same name: `<cell>.jsonl` (one record per line, schema in [_meta/SPEC.md](_meta/SPEC.md)) and `<cell>.md` (human report: themes, how people write, local ecosystem, sources, gaps). Counts are records (real / synthetic); the total is 4,254 records in 93 cells (78 from wave 1, 15 from wave 2 so far). Browse with `python tools/kb.py filter ... research_raw/wave1/<folder>`.

| Folder | Cells | Records (real / synthetic) | What it covers |
|---|---|---|---|
| [research_raw/wave1/en/](research_raw/wave1/en/en-buildingsmart-forums.md) | 23 | 1,034 (674 / 360) | English-language communities and vendors: buildingSMART forums, OSArch, Autodesk Revit export/import forums, GitHub projects (IfcOpenShell, That Open, xBIM, revit-ifc), Dynamo/pyRevit, Graphisoft, Tekla, Navisworks/ACC, Allplan/Vectorworks/Bentley, model checking, civil/infra, Singapore CORENET X, UK/ANZ/India, Middle East/Africa, US/Canada, blogs, Reddit, Stack Overflow, beginner Q&A. |
| [research_raw/wave1/topics/](research_raw/wave1/topics/t-proxy-mapping.md) | 25 | 1,287 (861 / 426) | Cross-cutting topic cells: proxy/class mapping, psets/params, coordinates, file size, geometry, clash/BCF, quantities/cost, validation/IDS, classification/bSDD, IFC 4.3 infra, COBie/FM, MEP, structural, encoding, materials/colours, GUID/versioning, openings, spaces, round-trip, viewers/conversion, error messages, data extraction, GIS/digital twin, permits/code check, versions/MVD. |
| [research_raw/wave1/roles/](research_raw/wave1/roles/p-bim-coordinator.md) | 7 | 375 (246 / 129) | One cell per persona group: architect, BIM coordinator, contractor/estimator, developer, engineers (structural/MEP/civil), FM/owner/reviewer, student. |
| [research_raw/wave1/ru/](research_raw/wave1/ru/ru-tim-expertiza.md) | 6 | 194 (102 / 92) | Russian-language: forum.dwg.ru (Revit and other tools), Habr developer articles, Autodesk/Telegram communities, Renga/nanoCAD, ТИМ and expert review. |
| [research_raw/wave1/zh/](research_raw/wave1/zh/zh-zhihu.md) | 5 | 242 (158 / 84) | Chinese: Zhihu, CSDN developer posts, Revit export, lightweight/web review, Taiwan and Hong Kong. |
| [research_raw/wave1/ai/](research_raw/wave1/ai/ai-mcp-usage.md) | 2 | 117 (83 / 34) | AI and MCP: how people use MCP servers with IFC/Revit, and what tasks they ask AI to do in Revit. |
| [research_raw/wave1/es/](research_raw/wave1/es/es-spain.md) | 2 | 84 (50 / 34) | Spanish: Spain and Latin America. |
| [research_raw/wave1/ja/](research_raw/wave1/ja/ja-japan.md) | 1 | 48 (31 / 17) | Japanese (Qiita, Zenn, note and others). |
| [research_raw/wave1/it/](research_raw/wave1/it/it-italy.md) | 1 | 46 (28 / 18) | Italian. |
| [research_raw/wave1/de/](research_raw/wave1/de/de-dach.md) | 1 | 44 (28 / 16) | German (DACH). |
| [research_raw/wave1/nl/](research_raw/wave1/nl/nl-dutch.md) | 1 | 37 (23 / 14) | Dutch (Netherlands, Flanders). |
| [research_raw/wave1/no/](research_raw/wave1/no/no-norway.md) | 1 | 30 (13 / 17) | Norwegian. |
| [research_raw/wave1/ko/](research_raw/wave1/ko/ko-korea.md) | 1 | 22 (7 / 15) | Korean (thin real coverage). |
| [research_raw/wave1/fr/](research_raw/wave1/fr/fr-francophone.md) | 1 | 17 (0 / 17) | French (synthetic only after wave 1). |
| [research_raw/wave1/pt/](research_raw/wave1/pt/pt-brazil.md) | 1 | 15 (0 / 15) | Portuguese, Brazil (synthetic only after wave 1). |
| [research_raw/_smoke/](research_raw/_smoke/smoke-gh.md) | 2 | 2 small test cells (GitHub revit-ifc, Chinese) | Pipeline smoke tests; not part of the wave 1 statistics. |
| [research_raw/wave2/en/](research_raw/wave2/en/en-ifc-rants.md) | 15 | 662 (418 / 244) | Wave 2, English (so far): ANZ, India and Southeast Asia, Africa, Autodesk forums (second pass; MEP and structural), Revit API and IFC, vendor knowledge bases, CDE platforms, GitHub discussions (IfcOpenShell, buildingSMART standards repos), OSArch and Reddit second pass, Speckle/SketchUp/Rhino/FreeCAD, YouTube video titles, IFC complaints and rants. Other wave-2 languages are still being added. |
