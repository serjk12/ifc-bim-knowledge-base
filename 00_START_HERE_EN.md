# Start here (for a tester with no BIM background)

[Русская версия: 00_START_HERE_RU.md](00_START_HERE_RU.md) | [README](README.md) | [Map of every file: INDEX.md](INDEX.md)

This page is for someone who has never worked with building models but has to **invent believable requests for IFC and Revit MCP servers and judge the answers**. Reading time is about 15-20 minutes. Everything said here about how common a problem is, and how people write, comes from the data in this base (wave 1: 3,592 records, 2,304 of them real, the rest synthetic) and from its reference documents. Where a statement is unverified, it is marked.

---

## 1. IFC in plain words

### What it is

**IFC (Industry Foundation Classes)** is an open file format for describing a building (or a road, or a bridge): not only 3D shapes, but also **what each object is** (wall, door, pipe, beam), **what it is made of**, **where it sits** (which floor, which room) and **what properties it has** (fire rating, area, manufacturer). It is maintained by buildingSMART International and is also the ISO standard 16739-1. See [01_ifc_basics/01_what_is_ifc_and_versions.md](01_ifc_basics/01_what_is_ifc_and_versions.md).

An analogy: IFC is to building models what PDF is to documents. A Word file opens only in Word, but almost any program can open a PDF. A PDF is also a "delivery copy", not a working file, and so is IFC: people work in native formats (RVT for Revit, PLN for Archicad), and IFC is a **snapshot for handing over**. Some information is lost on export (parametric behaviour, families, view settings). That is by design.

### Why it exists

One building is designed by architects, structural engineers, and heating/ventilation, plumbing and electrical engineers, each in their own program. A client, an approval authority or a contractor needs to **look at and check** these models without buying every program. Hence a neutral format. The usual life of IFC in a project (details in [01_ifc_basics/00_ifc_in_real_projects.md](01_ifc_basics/00_ifc_in_real_projects.md)):

1. Each discipline (architecture, structure, services) exports its own model to IFC.
2. A BIM coordinator combines the snapshots into one scene, looks for clashes (things that collide) and for gaps in the data.
3. Issues go back to the authors (often as BCF files); the authors fix them in their **native** tools and export again.
4. In some countries and cities IFC is also required for a submission to an authority (for example the expert review and AGR in Russia, CORENET X in Singapore: see [02_standards_regulations/national/](02_standards_regulations/national/singapore.md)).

### What is inside an `.ifc` file

It is a **plain text file**. Each line in the DATA section is one numbered "fact":

```
#4=IFCBUILDINGSTOREY('0szdNCWUTEzUZYNPGEsGHr',$,'Level 1',$,$,#32,$,$,.ELEMENT.,0.);
#5=IFCWALL('1h3LIRRmDdMXO0ere9cL3O',$,'Wall-001',$,$,#33,#40,$,.STANDARD.);
```

(simplified, from [01_ifc_basics/02_ifc_file_anatomy.md](01_ifc_basics/02_ifc_file_anatomy.md)). How to read it: `#5` is the line number, `IFCWALL` is the **class** (the "kind of object"), the long quoted string is the **GlobalId** (a 22-character "passport number" of the object), `'Wall-001'` is the name, `$` means "empty". What belongs to what (a wall to a floor, a door to a wall) is set by **separate relationship lines** (`IFCRELCONTAINEDINSPATIALSTRUCTURE` and similar). Nothing "sits inside" anything on its own, which matters when you check the answer to "how many doors on level 2?".

The header (first lines) says **which IFC version the file follows**: `FILE_SCHEMA(('IFC4'))`. Any sensible tool should start by reading that.

What the model holds besides geometry:

| What | In plain words | Details |
|---|---|---|
| Classes | the "kind" of object: `IfcWall`, `IfcDoor`, `IfcSpace`, `IfcPipeSegment` | [03_entities_cheat_sheet.md](01_ifc_basics/03_entities_cheat_sheet.md) |
| Hierarchy | project > site > building > storey > objects | [04_spatial_structure_and_relationships.md](01_ifc_basics/04_spatial_structure_and_relationships.md) |
| Properties and quantities | named groups of data (`Pset_WallCommon.FireRating`) and measured numbers (`Qto_WallBaseQuantities.NetArea`) | [05_properties_quantities_psets.md](01_ifc_basics/05_properties_quantities_psets.md) |
| Geometry, coordinates, units | shape, position, "where is zero" and "what is the ruler" | [06_geometry_placement_coordinates_units.md](01_ifc_basics/06_geometry_placement_coordinates_units.md) |
| Materials, types, classification | what it is made of, which "model/type", which classification code | [07_materials_classification_types_styles.md](01_ifc_basics/07_materials_classification_types_styles.md) |

### How IFC relates to Revit

**Revit** (Autodesk) is the most widely used program for designing buildings; its native `.rvt` file is closed. There are two "doors" between Revit and IFC, and most everyday trouble happens at those doors:

- **Export (Revit writes IFC).** Done by an add-in called "IFC for Revit" (its source code is public on GitHub as Autodesk/revit-ifc). The result depends on the **export settings**: the schema version, which property sets to write, how to place the model in space, how detailed the geometry is, and a **mapping table** "Revit category to IFC class". With a poor table or settings, a wall may turn into an "unknown object" (`IfcBuildingElementProxy`), objects may vanish, or properties may go missing. Most "the IFC is wrong" complaints come from a bad setup, a wrong mapping or a known exporter bug, not from the format itself (see [03_software/revit/ifc_export_reference.md](03_software/revit/ifc_export_reference.md)).
- **Import (Revit reads somebody else's IFC).** Two modes. **Link IFC** attaches the file as an external reference: every element becomes a "frozen" piece of geometry; you can look, section and measure but not edit. This is the normal choice for coordination. **Open IFC** builds a new project and tries to create native Revit elements; the result is often poor (see [03_software/revit/ifc_import_link_reference.md](03_software/revit/ifc_import_link_reference.md)).

This matters because the MCP servers you test come in two kinds: some work **with an `.ifc` file** (they read it with a library such as IfcOpenShell), others **with a running Revit** (they can look at and change the live model). The differences are in [07_mcp_testing/what_ifc_mcp_servers_do.md](07_mcp_testing/what_ifc_mcp_servers_do.md) and [07_mcp_testing/revit_mcp_testing.md](07_mcp_testing/revit_mcp_testing.md).

### IFC versions

| Version | What to know | In the file header |
|---|---|---|
| **IFC2x3** (2006) | the oldest version still in mass use; many treat it as the "safest" choice for an unknown recipient | `IFC2X3` |
| **IFC4** (2013; ISO 16739-1:2018) | better geometry and properties; the usual flavour is the **Reference View** ("look and check only", simplified geometry) | `IFC4` |
| **IFC4.3** (ISO 16739-1:2024) | adds roads, railways, bridges, ports, alignments | `IFC4X3_ADD2` |
| **IFC5** | experimental JSON-based alpha; not used in real workflows | n/a |

The practical consequence for tests: **a class or property that exists in IFC4 may not exist in IFC2x3** (and the other way round). A good assistant reads the version in the file first; a bad one answers "from one schema for everything". The version chosen at export is often dictated by the recipient's software and the contract (see [01_what_is_ifc_and_versions.md](01_ifc_basics/01_what_is_ifc_and_versions.md), section 5).

---

## 2. 15 terms you must know

More terms: [08_glossary/glossary_multilingual.md](08_glossary/glossary_multilingual.md) and [08_glossary/abbreviations.md](08_glossary/abbreviations.md). How people shorten and spell them in real life ("ifc", "ифс", "ревит", "proxies"): [06_how_people_write/jargon_slang_dictionary.md](06_how_people_write/jargon_slang_dictionary.md).

| # | Term | Plain meaning | How people write it / example |
|---|---|---|---|
| 1 | **BIM** | an information model of a building: not a drawing but a "database with shape"; officially ТИМ in Russia | "BIM model", "the model" |
| 2 | **IFC** | the neutral exchange format for such a model | "ifc", "ифс", `.ifc` |
| 3 | **IFC class** (`IfcWall`, `IfcDoor`, `IfcSpace`) | the "kind of object" in the file | "my walls came out as IfcBuildingElementProxy" |
| 4 | **Proxy** (`IfcBuildingElementProxy`) | the "unidentified object" label: the export did not know what it is | "proxies", "everything is proxies" |
| 5 | **Pset / properties** (`Pset_WallCommon`) | a named group of properties on an object (fire rating, "is it an external wall") | "psets", "parameters are gone" |
| 6 | **Qto / quantities** | measured numbers (area, volume) stored in the file | "there is no Qto, where does the area come from?" |
| 7 | **GlobalId / GUID** | the 22-character id of an object; used to track changes between file versions | "GUIDs changed on re-export" |
| 8 | **Exporter / Link IFC / Open IFC** | how Revit writes IFC / attaches somebody's IFC / converts it into its own objects | "link it", "open as a project" |
| 9 | **MVD / view** (Coordination View, Reference View) | the "profile" of an exchange: which part of IFC this export uses | "Reference View or DTV?" |
| 10 | **Georeferencing / coordinates** (map conversion, IfcSite, true north) | tying the model's local zero point to real-world coordinates | "the model landed 100 km away", "survey coordinates" |
| 11 | **IDS** | a machine-readable list of data requirements, used to test an IFC | "check it against the IDS" |
| 12 | **BCF** | a small file carrying an issue (picture + camera + object ids) between programs | "send it as BCF" |
| 13 | **CDE** | common data environment: the shared project storage for models and issues | "exchange via the CDE" |
| 14 | **Clash / coordination** | elements of different disciplines colliding (a pipe through a beam) and the process of finding them | "clashes in Navisworks" |
| 15 | **MCP** | the "plug" that lets an AI chat call tools (read IFC, drive Revit) | "MCP server", "tools", "connected it to Claude" |

---

## 3. What people do with IFC and what hurts them (top 10)

Source: [05_real_world_questions/pain_points_top100.md](05_real_world_questions/pain_points_top100.md) (the top 100 with frequency, causes and usual fixes). Below is the first ten. The "how people write" quotes come from records in the base (titles or paraphrases, not always word-for-word); **synthetic** examples are labelled. The counts there are keyword tallies, not a survey: read them as relative size.

| # | Pain in plain words | How people write it | Typical cause > fix |
|---|---|---|---|
| 1 | **A big IFC freezes** the viewer or script, out of memory | EN (real): "Memory grows when holding xBIM entities for a big model." ([source](https://github.com/xBimTeam/XbimEssentials/issues/351)). RU (*synthetic*, `ru-tim-expertiza-s014`): "ифс на 1.5 гига, вьюер у экспертизы виснет, чем можно облегчить не потеряв свойства" = the IFC is 1.5 GB, the expert-review viewer hangs, how to make it lighter without losing properties | too much fine geometry and data > lighten the export, read in a streaming way |
| 2 | **Elements are missing** from the Revit export | EN (real): "Both Revit 21 and 23 show the same missing elements with IFC4." ([source](https://forums.autodesk.com/t5/revit-architecture-forum/expoted-ifc-is-missing-elements-while-using-ifc4-schema/m-p/11455810)). RU (paraphrase of a real post): zones with imperfect boundaries compute area in Revit but are not exported as a body in IFC ([source](https://habr.com/ru/articles/1089018/)) | hidden elements, not tied to a level, unsupported geometry > check visibility settings and mapping |
| 3 | **The IFC will not open at all** in a viewer, library or portal | RU (paraphrase of a real post): IFC from SAPFIR fails to import into AutoCAD (system error) but opens fine in BIMsight ([source](https://forum.dwg.ru/showthread.php?t=160240)) | a strict parser vs a non-standard spelling, schema version > check the header, try another viewer |
| 4 | **"Will my IFC pass the checker?"**: self-check before submission | ZH (real paraphrase): 报建前能不能在Revit里先自检，不用每次导出IFC再检测 = can I self-check inside Revit before filing, without exporting IFC every time ([source](https://zhuanlan.zhihu.com/p/633827596)). RU (real paraphrase): a heavy model takes two hours to export and errors show only after upload to the portal ([source](https://habr.com/ru/articles/1089018/)) | the authority's rules are stricter than authors see > run the model through a checker/IDS in advance |
| 5 | **Add or bulk-edit properties** in an existing IFC | EN (real): "how to add a custom pset to all walls where Domain=Bridge without commercial software" ([source](https://bimcorner.com/add-properties-to-ifc-using-ifcopenshell/)). RU: "как добавить свойство Renga в экспорт IFC" = how to add a Renga property to the IFC export ([source](https://manual.rengabim.com/ehksport_atributov_obektov.html)) | properties live in strictly structured sets > script it (IfcOpenShell) or change the export setup |
| 6 | **Openings missing or misplaced**: a wall without a hole, a window floating outside | EN (real): "beam voids misplaced in IFC4 only" ([source](https://github.com/Autodesk/revit-ifc/issues/708)). RU (*synthetic*, `ru-geom-s007`): "в ифс пропали проемы под двери, стена сплошная..." = door openings vanished, the wall is solid | openings are separate objects with relationships and are easy to lose > check for `IfcOpeningElement` |
| 7 | **IFC4.3 gives "Unsupported schema"** or does not open | EN (real): "schema_by_name IFC4x3 throws No schema named IFC4x3" ([source](https://github.com/IfcOpenShell/IfcOpenShell/issues/2382)). RU (*synthetic*, `ru-infra-s008`): "покажи все трассы (IfcAlignment) в модели и пикетаж начала и конца, ифс 4.3 из civila" = show all alignments and their start/end stationing, IFC 4.3 from Civil 3D | an old library does not know the new schema > update, check the version |
| 8 | **Georeferencing missing or wrong** | EN (real): "Georeferenced IFC2x3 with ePset_MapConversion and ePset_ProjectedCRS but cannot find them in Bonsai." ([source](https://community.osarch.org/discussion/comment/29556/)). ZH (real paraphrase): the BIM has no geographic coordinates, needs origin lat/lon plus rotation, and the origin is not at the model centre ([source](https://blog.csdn.net/liyan_gis/article/details/100132931)) | the file has its own frame of reference and tools read it differently > set or read the map conversion explicitly |
| 9 | **An IDS does not behave as its author expects** | EN (real): "no elements matched even valid ones; screenshots" ([source](https://github.com/IfcOpenShell/IfcOpenShell/issues/7856)). RU: "что такое IDS, где поддерживается, какие ограничения" = what is IDS, where is it supported, what are the limits ([source](https://habr.com/ru/articles/908192/)) | IDS is strict (letter case, class inheritance) > read the spec, test on a tiny example |
| 10 | **The AI-to-Revit link fails or does the wrong thing** (MCP server, plugin) | EN (real): "list all pipes in the revit model -> Get element information failed: Method not found" ([source](https://github.com/mcp-servers-for-revit/revit-mcp/issues/28)) | wrong arguments, no connection, missing function > this is exactly what you are testing |

Further down (11-100): GUIDs changing between exports, "too big for a browser", which export settings to choose in Archicad/Tekla/Renga, proxies instead of real classes, differences between viewers, unreadable geometry types, and so on. All in [pain_points_top100.md](05_real_world_questions/pain_points_top100.md) and by topic in [05_real_world_questions/by_topic/](05_real_world_questions/by_topic/revit_export_and_class_mapping.md).

**What this means for MCP tests:** most real requests are not "explain what IFC is" but **tasks on a specific model** (the data has 1,051 `model_task` and 1,127 `troubleshooting` records): "count", "find what is missing", "explain why it vanished", "export to Excel", "check before submission".

---

## 4. How to write test questions with this base, step by step

**Step 1. Understand what the server under test can do.** Open [07_mcp_testing/what_ifc_mcp_servers_do.md](07_mcp_testing/what_ifc_mcp_servers_do.md): four kinds of server, a capability matrix, and a section "what is realistic to ask and what must be refused". It is unfair to ask a server that only reads IFC to "recolour all walls in Revit".

**Step 2. Prepare a model.** Take a file from [04_open_source/sample_ifc_files.md](04_open_source/sample_ifc_files.md) and write down 5-10 facts about it for yourself (how many storeys, which version, whether it has properties, which classes). Without this you cannot judge the answer.

**Step 3. Pick an intent and a persona.** [07_mcp_testing/intent_taxonomy.md](07_mcp_testing/intent_taxonomy.md) lists 22 intents (count things, check requirements, compare versions, export to Excel, fix data, and so on). Pick a persona (BIM coordinator, architect, estimator...): [05_real_world_questions/by_persona/](05_real_world_questions/by_persona/bim_coordinator.md) explains what that person does and how they talk.

**Step 4. Take a "voice sample" from real records.** For English: [05_real_world_questions/by_language/en.md](05_real_world_questions/by_language/en.md) and the bank [07_mcp_testing/prompt_bank_en.md](07_mcp_testing/prompt_bank_en.md). To pick samples yourself use the helper:

```
python tools/kb.py stats --lang en
python tools/kb.py filter --kind real --lang en --topic export_revit --limit 20 --format brief
python tools/kb.py filter --kind synthetic --lang en --type model_task --persona bim_coordinator --limit 20 --format brief
```

Read in pages (`--limit` and `--offset`); do not dump everything at once. Real records carry a source link; synthetic ones are labelled `synthetic`.

**Step 5. Write the request the way a person would.** Rules from [06_how_people_write/style_guide.md](06_how_people_write/style_guide.md): short; use jargon ("ifc", "psets", "proxies", "schedule"); skip polite preambles when the person is in a hurry; state the goal in one phrase ("submission is tomorrow"); typos and mixed languages are fine. What to **avoid** is shown in [06_how_people_write/anti_patterns_llm_questions.md](06_how_people_write/anti_patterns_llm_questions.md) (64 "machine-made version > human version" pairs). How people spell product and format names: [name_variants_and_misspellings.md](06_how_people_write/name_variants_and_misspellings.md).

**Step 6. Add a trap if you want to test the assistant's care.** [07_mcp_testing/edge_cases_and_traps.md](07_mcp_testing/edge_cases_and_traps.md) has 22 traps: schema differences IFC2x3/IFC4/IFC4.3 (E1), missing or doubtful quantities (E7), units (E8), missing georeferencing (E9), proxies instead of classes (E11), non-Latin text and `\X2\` escapes (E12), duplicate GlobalIds (E13), risky write operations (E22).

**Step 7. Or let an LLM generate them.** A ready prompt (RU and EN), a quick mode, multi-turn scripts and a judge prompt: [07_mcp_testing/llm_generation_prompt.md](07_mcp_testing/llm_generation_prompt.md). For variety roll the "dice" in [07_mcp_testing/variation_matrix.md](07_mcp_testing/variation_matrix.md). More ready-made material: [prompt_bank_en.md](07_mcp_testing/prompt_bank_en.md), [prompt_bank_ru.md](07_mcp_testing/prompt_bank_ru.md), [prompt_bank_multilingual.md](07_mcp_testing/prompt_bank_multilingual.md), and 156 scenarios in [test_scenarios_library.md](07_mcp_testing/test_scenarios_library.md).

**Step 8. Judge the answer.** Use [07_mcp_testing/evaluation_rubric.md](07_mcp_testing/evaluation_rubric.md): a 0-4 scale on several dimensions, "critical failures" (for example invented data or a silently ignored error), worked examples and a checklist. Compare not "how nice the text is" but **whether the answer matches the facts about your model**, and whether the assistant honestly said "that is not in the file".

### Ground rules for an honest check

- A real question and a synthetic prompt are different things; in this base synthetic ones are always labelled.
- If a request needs Revit and only an IFC server is connected, the right answer is "I cannot do that", not an invention.
- If the file lacks data (areas, properties, georeferencing), the right answer says so rather than making up numbers.
- Verify critical regulatory claims against official sources, not this base (see the disclaimer in the [README](README.md)).

---

## 5. Where to go next

| You need | File |
|---|---|
| The ready generation prompt and the judge prompt | [07_mcp_testing/llm_generation_prompt.md](07_mcp_testing/llm_generation_prompt.md) |
| The answer-scoring rubric | [07_mcp_testing/evaluation_rubric.md](07_mcp_testing/evaluation_rubric.md) |
| Prompt banks | [RU](07_mcp_testing/prompt_bank_ru.md) · [EN](07_mcp_testing/prompt_bank_en.md) · [14 languages](07_mcp_testing/prompt_bank_multilingual.md) |
| What MCP servers can do | [what_ifc_mcp_servers_do.md](07_mcp_testing/what_ifc_mcp_servers_do.md) · [server catalog](04_open_source/mcp_servers_and_ai_tools.md) |
| Testing an MCP that drives Revit | [revit_mcp_testing.md](07_mcp_testing/revit_mcp_testing.md) |
| National context (for example Russia, Singapore, UK) | [02_standards_regulations/national/](02_standards_regulations/national/russia.md) |
| Every file in the base | [INDEX.md](INDEX.md) |

Research wave 2 (more languages and countries) is still being added; the figures in this document refer to wave 1.
