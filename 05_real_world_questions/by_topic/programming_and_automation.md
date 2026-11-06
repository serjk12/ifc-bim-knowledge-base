# Programming with IFC, Revit API automation, data extraction

Vocabulary topics covered: `programming_ifcopenshell`, `programming_web_ifc`, `programming_xbim_dotnet`, `programming_other`, `revit_api_automation`, `data_extraction_analytics`.
Built from the wave-1 research records (619 records carry at least one of these topics: 532 real, 87 synthetic; languages: en 482, zh 57, ru 31, ja 30, es 7, it 2, ko 2, de 2, fr 2, and one each of da, no, pt, cs). The audience is mostly developers (158 of the 218 IfcOpenShell records come from `developer_programmer`), so the language mix is far more English than in the permit/contract file. Last built: 2026-11-06.

## In plain words

Three groups of people write code around building models:

1. **Reading and editing IFC files from code.** They use a library: **IfcOpenShell** (Python and C++; the one most AI/MCP servers wrap), **web-ifc** with That Open Engine (JavaScript compiled to WebAssembly, for browsers and Node), **xBIM** (C#/.NET), plus smaller ones (IFC++, GeometryGym, BIMserver). Typical jobs: list walls and their fire rating, add a property to every door, convert to glTF, count things, compare two versions.
2. **Driving Revit from code.** They use the Revit API (C#), Dynamo, pyRevit, or an **MCP server + Revit add-in** that lets an AI assistant call Revit commands. Typical jobs: batch-export IFC for many views, rename views, create sheets, fill parameters, build walls from a CAD drawing.
3. **Getting data out of models into tables.** Excel/CSV, SQLite, Power BI, DuckDB, cost sheets, dashboards.

Most questions come from the same few root causes: an IFC file is **not a table** (properties hang off relationships, can sit on the type instead of the instance, and placements are nested); library **versions and schema support** differ; **big files hit memory limits**, especially in WebAssembly; **text must be escaped** in IFC (`\X2\...\X0\`); and Revit's exporter has many options with surprising defaults. A good AI assistant here must produce correct API calls, tell whether it actually ran the code, verify the result (re-open the saved file, re-read the Revit state) and be honest about limits.

Background: [open-source libraries and toolkits](../../04_open_source/libraries_and_toolkits.md), [MCP servers and AI tools](../../04_open_source/mcp_servers_and_ai_tools.md), [Revit IFC export reference](../../03_software/revit/ifc_export_reference.md) (including batch export through the API, Dynamo and pyRevit), [Revit IFC import/link](../../03_software/revit/ifc_import_link_reference.md), [IFC file anatomy](../../01_ifc_basics/02_ifc_file_anatomy.md) (header, `\X2\` escapes, GlobalId), [property sets and quantities](../../01_ifc_basics/05_properties_quantities_psets.md), [geometry, placement, coordinates](../../01_ifc_basics/06_geometry_placement_coordinates_units.md), [community projects](../../04_open_source/community_projects_and_enthusiasts.md), [LLM/BIM research](../../04_open_source/llm_bim_research_and_datasets.md) and the [glossary](../../08_glossary/glossary_multilingual.md).

### Words you will meet in the data

| Word | Plain meaning |
|---|---|
| `get_psets` | IfcOpenShell helper that returns all property sets of an element, instance and type together; preferred over walking relationships by hand |
| `IsDefinedBy` / `IsTypedBy` | The links from an element to its own property sets / to its type object (which may hold properties too) |
| Qto, base quantities | Quantity sets such as `Qto_WallBaseQuantities`; present only if the exporter wrote them |
| Geometry kernel | The engine that turns IFC geometry into meshes (opencascade, cgal, cgal-simple, manifold in IfcOpenShell) |
| WASM / wasm32 | WebAssembly build of web-ifc; about a 4 GB memory ceiling per module |
| `\X2\...\X0\` | How IFC (STEP) writes non-ASCII text; readers decode it |
| wexbim, fragments, XKT, glTF | Viewing formats made from IFC; fast but they drop or reshape the data |
| Transaction / ExternalEvent | Revit API rules for changing a model (changes in a transaction; add-ins call Revit through external events) |
| IFCExportOptions / `AddOption` | The Revit API object that holds IFC export settings; some option keys are undocumented |
| Dynamo, pyRevit | Visual and Python scripting environments inside Revit |
| MCP tool (`create_wall`, `send_code_to_revit`) | A function an AI assistant may call; "send code" tools run arbitrary code in Revit |
| UniqueId vs GlobalId | Revit's element id string vs IFC's 22-character identifier; related but not identical |

## Problem map

Ranked by number of matching records (real + synthetic). Records were hand-grouped; one record can appear in several problems, so counts overlap and are a signal, not a statistic.

| # | Problem | How users describe it | Frequency signal | Root cause | Typical fix |
|---|---|---|---|---|---|
| 1 | Large files: out of memory, very slow, crashes | “2 GB IFC from Synchro, 16 GB RAM, open() runs out of memory; asks about lazy loading, renumbered STEP, or…” (en); “converting an IFC larger than ~2GB crashes with Aborted, emscripten_resize_heap fails past ~4 GiB, same with…” (en); “Deleting 1000 of 20k elements takes over 10 minutes.” (en) | 63 rec. (56 real, 7 synth.); en 58, ja 4, ru 1 | Everything is parsed up front; geometry iterators hold memory; WebAssembly 4 GB ceiling; per-element deletes; regressions between versions | Lazy open, extract a subset, chunk and limit threads, stream meshes, free objects, batch/patch recipes |
| 2 | Geometry, placement and georeference come out wrong or empty | “After upgrading from 0.7 to 0.8.1 a slab produces no geometry in a script but renders in Bonsai.” (en); “Signed tetrahedra volume at projected coordinates loses precision; 2.8 m3 wall gives 2.75.” (en); “Extracting elements with IfcPatch drops georeferencing; eastings and northings turn into Blender…” (en) | 55 rec. (48 real, 7 synth.); en 53, zh 2 | Kernel and settings, local vs world coordinates, float precision far from origin, mapped items with two transforms, patches that drop georeferencing | Pick kernel and contexts, compute relative to a local origin, apply both transforms, re-add georeference |
| 3 | Dumping model data to Excel/CSV/SQL/BI | “IfcOpenShellのIfcCSVだとAttributeしか書き出せないので、PropertySetとMaterialも一緒にExcelへ出したい” (ja); “In Poland Excel regional settings follow the interface language, so dotted numbers become text…” (en); “Tender and cost work runs on spreadsheets; I need rows traceable to IFC elements, e.g. ventilators…” (en) | 51 rec. (38 real, 13 synth.); en 41, ja 3, es 1, ko 1 | IFC is a graph; flat tables need traversal; CSV tools export attributes only; locale decimals; no stable key kept | `get_psets`, IfcCSV with qualifiers, ifc2sql/DuckDB, keep GlobalId and storey columns, set delimiter/decimal for locale |
| 4 | Batch IFC export from Revit through API / Dynamo / pyRevit | “automating IFC export of several Revit files from BIM 360; every IFC from the script is empty…” (en); “each exported IFC is about 13 KB” (en); “using AddOption ClassificationName and ClassificationFieldName from Python has no effect; data only…” (en) | 47 rec. (41 real, 6 synth.); en 43, ru 4 | `IFCExportOptions` subtleties, active vs background document, view filter ids, undocumented options, locale decimal comma, version changes (2027) | Use the right export node/call, set view ids, explicit options, absolute paths, verify the output file |
| 5 | Reading properties and quantities reliably | “I loop over all IFC in a folder and write an Excel sheet per file with chosen entity parameters…” (en); “setting includeTypeProperties=true gives empty array on an IFC2X3 model in node” (en); “pasted an ExtractMaterialData helper that checks HasAssociations and IfcRelAssociatesMaterial; some…” (en) | 35 rec. (22 real, 13 synth.); en 22, zh 6, ja 3, es 2 | Properties live behind relationships, on the type or the instance; exporter structure changes; helpers missing for some schemas | `util.element.get_psets`, resolve type properties, check material on type/layer set/representation |
| 6 | AI-driven Revit automation (Revit MCP) fails or does the wrong thing | “Claude replies: unable to connect to Revit... will create a 10-meter wall once connected; port 8080…” (en); “list all pipes in the revit model -> Get element information failed: Method not found” (en); “AI 建牆時沒有樓層參數就取 FirstOrDefault Level，牆建到非預期樓層、無法指定牆型” (zh) | 33 rec. (30 real, 3 synth.); en 17, zh 10, ja 4, es 1 | Server/plugin version mismatch, hardcoded port, lost arguments, silent defaults (first level, Z=0), hosted families, hangs on stairs | Align versions, pass explicit level/type/host, dry-run then apply, read back the result |
| 7 | Editing or creating IFC without breaking it | “assign_containerを忘れると床が表示されない。開口を作ってからドア窓をadd_filling” (ja); “удалил элемент - файл открывается, но валидатор падает; смена класса требует смены типа” (ru); “IFC generated by the user's own Python app fails to import: IfcAxis2Placement3D has no attribute…” (en) | 33 rec. (24 real, 9 synth.); en 25, ru 5, ja 1, zh 1 | Raw `create_entity` skips relationships; deleting leaves orphans; class change without type change; invalid placements | `ifcopenshell.api`, validate after editing, write to a new file, keep a change journal |
| 8 | Which library / tool, and building viewers or converters | “C# developer of a pipeline CAD must build an IFC export; asks where to start, about certification…” (en); “Discord удалили, документация пропала; GLTF в разы больше IFC; остались на 1.5.1” (ru); “IFC里有大量非几何信息，viewer用不上；用xbim读到内存再整理几何输出成gltf，文件能小一半，但不保证每个都变小” (zh) | 33 rec. (30 real, 3 synth.); en 14, zh 13, ru 5, it 1 | Many libraries with different languages, licenses and maturity; viewing formats lose semantics; project continuity | Pick by language + task + license, pin versions, keep properties linked by GlobalId |
| 9 | Version, install and environment mismatches | “Worked in 0.0.72, aborts in 0.0.77; trying 0.0.78 yields 'function StreamMeshes called with 4…” (en); “npm装的web-ifc-three运行报WebAssembly LinkError (Import function not…” (zh); “edit_georeferencing() rejects map_conversion keyword in IfcOpenShell 0.7.10 though the script…” (en) | 26 rec. (23 real, 3 synth.); en 18, zh 5, ja 2, ru 1 | Wrapper vs wasm version mismatch, stray modules, conda vs pip builds, renamed API arguments | Match versions exactly, read release notes, check which schemas the build contains |
| 10 | Non-ASCII text garbled or truncated | “which chinese encoding pattern do you use in IFC generation? tried utf-8 but still messy code” (en); “'\X2\7d20586b571f\X0\' decodes wrong; uppercase hex decodes right” (en); “ifcopenshell.Error: Unable to parse IFC SPF header; resaving without BOM works.” (en) | 25 rec. (24 real, 1 synth.); en 15, zh 3, ja 2, ru 1 | STEP needs `\X2\` escapes; some exporters write raw bytes; BOM; decoder bugs | Let the library encode/decode, strip BOM, fix the exporter, validate |
| 11 | Housekeeping scripts in Revit (views, sheets, parameters, duplicates) | “my script finds and deletes the duplicate instances listed in the error; with 4 identical instances…” (en); “my script creates View Filters; works with instance parameters but throws object reference error…” (en); “I create sheets and place views with Dynamo but can't find how to add a viewport; later wanted to…” (en) | 24 rec. (19 real, 5 synth.); en 20, ru 2, zh 1, es 1 | Type vs instance parameters, element vs type duplication, creation order, closed worksets | Dry-run list, one transaction, old to new report, skip already processed |
| 12 | Quantities that do not match the model, Revit or the cost sheet | “IfcOpenShell QTO gives wrong area for an IfcWindow defined by an IfcWindowType with mesh geometry…” (en); “объёмы в Ревите 17 кликов, в ifcopenshell 40 строк; IFC слишком сложный” (ru); “Cost rows are not one-to-one with model quantities (installation rows skipped, others split); wants…” (en) | 23 rec. (15 real, 8 synth.); en 15, zh 3, ru 3, es 1 | Qto absent or net/gross mix, geometry-derived values, units, cost rows not one-to-one | Prefer Qto, geometry as flagged fallback, cross-reference ID |
| 13 | IFC schema version not supported (IFC4X3, IFC2x3 differences) | “i am trying to open a IFC4x3 file with ifcopenshell python but i get the error that IFC4x3 is not…” (en); “web-ifcを上げる前に何が変わるか。0.0.50はIFC4X3_ADD2でUnsupported Schema、0.0.78のブラウザ版StreamMeshesでBindingError” (ja); “IFC4x3 IfcProduct lacks the GetPropertySet helper known from other schemas” (en) | 22 rec. (20 real, 2 synth.); en 20, ja 2 | Exact identifier `IFC4X3_ADD2`; schemas compiled per build; helper methods per schema | Check build schemas and the file's `FILE_SCHEMA`, upgrade, migrate schema-aware |
| 14 | GlobalId vs Revit UniqueId, diffs and change tracking | “Revit UniqueId and IFC GUID look unrelated; how does Revit convert between them and can I reproduce…” (ja); “any other identifier than GlobalId to know an object's geometry is unchanged between versions? the…” (en); “when a tool re-issues GlobalIds the same element shows as one deletion and one addition; want to…” (en) | 20 rec. (19 real, 1 synth.); en 15, ja 4, zh 1 | Ids are regenerated by exporters; conversion rules; diffs compare the wrong things | Match by type + geometry + position, content hash, store the exported GUID |
| 15 | Checking IFC against IDS from code | “как проверять IFC по IDS пакетно, с отчётами html и json” (ru); “spec fails vs skipped changes compliance report” (en) | 10 rec. (9 real, 1 synth.); en 8, ru 2 | Skipped vs failed specs, abstract classes (`IfcElement` has no instances), type coercion | Use concrete classes, require at least one match, batch with HTML/JSON reports |

## Problems in depth

The "assistant" paragraphs describe what a good AI/MCP assistant should do. API names are those that appear in the sources and reference files; if an assistant uses a function that is not in the library, treat it as a hallucination and check against the documentation.

### 1. Large files: out of memory, slow, crashes

**Symptoms in users' words**
- “2 GB IFC from Synchro, 16 GB RAM, open() runs out of memory; asks about lazy loading, renumbered STEP, or another storage tech” (en; [source](https://github.com/IfcOpenShell/IfcOpenShell/issues/2025))
- “大きいIFCを開くと全インスタンス・属性を先にパースして遅くメモリを食う” (ja; EN: Opening huge IFC with IfcOpenShell is slow and memory-hungry; lazy loading in 0.9.0; [source](https://qiita.com/kiyuka/items/0d2ef739a0d34606a52f))
- “converting an IFC larger than ~2GB crashes with Aborted, emscripten_resize_heap fails past ~4 GiB, same with readFromCallback” (en; [source](https://github.com/ThatOpen/engine_fragment/issues/258))
- “Deleting 1000 of 20k elements takes over 10 minutes.” (en; [source](https://community.osarch.org/discussion/2673/deleting-many-objects-takes-forever))
- “calling IsTypedBy for each element is much slower since 6.0.442; supplies repro solution comparing 5.1.341 and 6.0.442 on a public MEP sample model” (en; [source](https://github.com/xBimTeam/XbimEssentials/issues/674))

**Why it happens.** IfcOpenShell used to parse every instance and attribute on open; version 0.9.0 adds `lazy=True` (a 393 MB file: 11.3 s to 1.4 s and roughly 3 GB to 1 GB, per one benchmark). The geometry iterator keeps memory until iteration ends, so many threads on a huge file can exceed 60 GB; the kernel choice (opencascade vs cgal-simple) changes memory use. web-ifc compiled to WebAssembly has a 32-bit ceiling of about 4 GB, chunked input does not help until a 64-bit build exists, and walking relations in JavaScript is slow compared with C++. Calling `GetFlatMesh` in a loop without `delete()` on each result leaks. Deleting 1,000 of 20,000 elements one by one took over 10 minutes. xBIM regressed in `IsTypedBy` speed (6.0.442) and leaks unmanaged resources (geometry engine, Esent store).

**What fixes it.** Open lazily (0.9+), extract only what is needed (an IfcPatch recipe that keeps one class instead of deleting many), process in chunks with fewer threads, stream meshes, free native objects, build a type lookup once instead of calling `IsTypedBy` per element, split by storey or discipline.

**A good assistant** measures and reports time and memory, picks lazy/subset strategies before brute force, says plainly when a limit is architectural (WASM 4 GB) and offers a split, and never claims "done" if the run was cancelled (cancelling in one MCP server does not stop the Python process).

**Clarifying questions.** File size and library version? Do you need geometry or only data? Python, Node or browser? How much RAM? Which elements matter?

### 2. Geometry, placement and georeferencing come out wrong or empty

**Symptoms in users' words**
- “After upgrading from 0.7 to 0.8.1 a slab produces no geometry in a script but renders in Bonsai.” (en; [source](https://github.com/IfcOpenShell/IfcOpenShell/issues/6142))
- “Signed tetrahedra volume at projected coordinates loses precision; 2.8 m3 wall gives 2.75.” (en; [source](https://github.com/IfcOpenShell/IfcOpenShell/issues/9770))
- “IfcCsv export returns 0 for x,y,z of elements represented by mapped items; the mapped item transformation is ignored.” (en; [source](https://github.com/IfcOpenShell/IfcOpenShell/issues/6277))
- “Extracting elements with IfcPatch drops georeferencing; eastings and northings turn into Blender offset.” (en; [source](https://github.com/IfcOpenShell/IfcOpenShell/issues/8199))
- “Opening meshes correct with recursive transform, misplaced via GetFlatMesh; suspects a normalize/translation line.” (en; [source](https://github.com/ThatOpen/engine_web-ifc/issues/1462))

**Why it happens.** `create_shape` depends on the kernel and settings: after an upgrade from 0.7 to 0.8 a script with plain opencascade and no context ids produced no slab, while Bonsai (hybrid kernel with contexts) rendered it. World coordinates far from the origin (projected coordinates around 5,000,000 m) lose float precision in a volume computed as tetrahedra around the origin (2.8 m3 became 2.75). Mapped items have two transforms and the CSV selector read only `ObjectPlacement`, so x,y,z came out 0. web-ifc does not apply `IfcMapConversion`; opening meshes can be misplaced through `GetFlatMesh` but right when composed recursively. IfcPatch `ExtractElements` drops georeferencing (open bug). The manifold kernel does not support sweeps (IfcSweptDiskSolid). `edit_georeferencing()` renamed a keyword in 0.7.10.

**What fixes it.** Choose the kernel and pass the right context, compute volumes relative to a local centroid, multiply both transforms for mapped items, re-add `IfcMapConversion` after extraction, and compare the same file in a second viewer before blaming the data.

**A good assistant** states which kernel and settings it used, says whether coordinates are local or world, warns about precision far from the origin, and reports which element failed instead of silently skipping it.

**Clarifying questions.** Local or world coordinates? Which units? Library and version, which kernel? Does the file carry `IfcMapConversion`? Can you share a minimal file with the single failing element?

### 3. Dumping model data to Excel, CSV, SQL or BI

**Symptoms in users' words**
- “IfcOpenShellのIfcCSVだとAttributeしか書き出せないので、PropertySetとMaterialも一緒にExcelへ出したい” (ja; EN: IfcCSV only exports attributes; how do I dump attributes, property sets and materials of an IFC to Excel?; [source](https://zenn.dev/miyamiyaumya/articles/19a4247133dde6))
- “In Poland Excel regional settings follow the interface language, so dotted numbers become text; today I fix types in Power Query. XLSX and ODS export fine.” (en; [source](https://github.com/IfcOpenShell/IfcOpenShell/issues/4290))
- “Tender and cost work runs on spreadsheets; I need rows traceable to IFC elements, e.g. ventilators FAN-01..03 per room, and summarise equal elements by floor.” (en; [source](https://github.com/IfcOpenShell/IfcOpenShell/issues/7762))
- “協力会社の重いモデルや古いモデルを開かずに値だけ取り出したい。API/プラグイン経由は遅くAPSは組織整備が前提” (ja; EN: Extract values from heavy Revit models from subcontractors without opening them; ETL to columnar store; [source](https://zenn.dev/tomosandego/articles/59e6cf8dfe60bc))
- “junior data specialist wants Revit data incl. custom psets in a database for a webapp and maintenance without paying heavily for Autodesk APIs” (en; [source](https://forums.buildingsmart.org/t/6034))

**Why it happens.** The project, site, building and storey tree comes from aggregation and containment relations; properties come from `IfcRelDefinesByProperties`, materials from association relations. IfcCSV exports attributes only unless property-set qualifiers (or regex wildcards) are given. Excel in a Polish or Italian locale turns dotted numbers into text; CSV exports can carry junk columns and no unit column. For cost work, rows must stay traceable to elements (GlobalId) because cost rows are not one-to-one with model quantities. Heavy or old subcontractor models are better extracted once into a columnar store (Parquet queried with DuckDB) than opened repeatedly.

**What fixes it.** `get_psets` plus pandas, IfcCSV with qualifiers, the ifc2sql patch for SQLite/MySQL, tidy long tables, delimiter and decimal chosen for the user's locale, and always a `GlobalId` and storey column.

**A good assistant** asks for grain and locale, includes keys, reports empty columns and elements without quantities, and states which source (Qto, property, geometry) each number came from.

**Clarifying questions.** What is one row (element, type, storey)? Which properties? Which Excel locale (decimal comma, semicolon)? One file or a whole folder? Should the table be loadable into Power BI or SQL?

### 4. Batch IFC export from Revit (API, Dynamo, pyRevit)

**Symptoms in users' words**
- “automating IFC export of several Revit files from BIM 360; every IFC from the script is empty, manual export fine; checked classification and LOI mapping and phases” (en; [source](https://forum.dynamobim.com/t/ifc-export-node-return-an-empty-ifc/82822))
- “tried several Revit/Dynamo versions, reset Dynamo, disabled add-ins, reinstalled Revit” (en; [source](https://forum.dynamobim.com/t/unrecoverable-error-during-ifc-export-using-dynamo/113291))
- “converted Python scripts to Revit 2027; IFC export scripts fail incl. custom export setups and basic doc.Export; generic PythonEvaluator error” (en; [source](https://forum.dynamobim.com/t/are-anyone-able-to-export-ifc-using-dynamo-in-revit-2027/115000))
- “using AddOption ClassificationName and ClassificationFieldName from Python has no effect; data only exported when set from UI” (en; [source](https://github.com/Autodesk/revit-ifc/issues/277))
- “недокументированные опции IFC-экспортёра ведут себя по-разному, поэтому стандартное окно экспорта” (ru; EN: Undocumented IFC exporter options behave differently between Revit versions; [source](https://habr.com/ru/articles/1087472/))

**Why it happens.** Export runs through `Document.Export` with `IFCExportOptions`; many keys are added with `AddOption` and are documented mainly in the exporter source ([option list](../../03_software/revit/ifc_export_reference.md)). Reported traps: a custom node exports only the open document (hence 13 KB files) while another node is meant for background documents; export of the current view needs `ActiveViewId`/`FilterViewId`; classification options had no effect from code (tracked internally); a tessellation value written with a decimal comma in a non-English locale broke the export; in Revit 2027 the IFC configuration classes moved namespace; the reports disagree on whether an open transaction is needed (one 2027 report says yes, one 2025 report says no), so treat it as version-dependent; geometry generated by Dynamo is not exported as native elements.

**What fixes it.** Use the node or call meant for background documents, set view ids, pass absolute paths, use invariant number formatting, load the saved configuration instead of hand-building options, and check that the output file exists and has a plausible size.

**A good assistant** asks the Revit year and exporter version, does not assume transaction rules, verifies the output instead of trusting "no error", and offers a dry run on one view first.

**Clarifying questions.** Revit version and IFC add-in version? Active document or files opened in the background? IFC version/view and which saved setup? Output folder (local or network)? One IFC per view, level or phase?

### 5. Reading properties and quantities reliably

**Symptoms in users' words**
- “I loop over all IFC in a folder and write an Excel sheet per file with chosen entity parameters. Exporter 22.1 works, 22.6 changes the structure and COBie/custom properties are missed.” (en; [source](https://github.com/IfcOpenShell/IfcOpenShell/issues/3978))
- “How do I get all properties and quantities (length, area) of IfcDuctSegment instances; unsure how to relate IfcQuantityLength to the element.” (en; [source](https://github.com/IfcOpenShell/IfcOpenShell/issues/3910))
- “setting includeTypeProperties=true gives empty array on an IFC2X3 model in node” (en; [source](https://github.com/ThatOpen/engine_web-ifc/issues/1873))
- “pasted an ExtractMaterialData helper that checks HasAssociations and IfcRelAssociatesMaterial; some elements return no material” (en; [source](https://github.com/xBimTeam/XbimEssentials/issues/642))
- “给IFCMaterial写多个属性集，读出来同一个Pset重复，值不同” (zh; EN: Adding multiple property sets to IfcMaterial then reading: same Pset shows up duplicated with different values.; [source](https://ask.csdn.net/questions/2665040))

**Why it happens.** A property is not an attribute of the element: it sits in a property set reached through a relationship, and may be on the type (`IfcRelDefinesByType`) instead of the instance. A script that walks relationships by hand broke when the exporter changed its structure between versions; `ifcopenshell.util.element.get_psets` is the robust answer. In web-ifc, `includeTypeProperties=true` returned an empty array on an IFC2X3 model until fixed; in xBIM the `GetPropertySet` helper was missing for IFC4x3; material may sit on the representation item, type or layer set, so a naive check returns "No Material". Quantities exist only if the exporter wrote them.

**What fixes it.** Use the library helper, resolve both instance and type, and treat "not found" as a question about exporter settings (base quantities, property-set options) as much as about code.

**A good assistant** says where a value was found (instance or type, which set) and, when nothing is found, lists the sets that do exist before saying "missing".

**Clarifying questions.** Instance or type property? Which property-set name (custom or `Pset_*Common`)? IFC schema and exporter version? Qto or computed value?

### 6. AI-driven Revit automation (Revit MCP) fails or does the wrong thing

**Symptoms in users' words**
- “Claude replies: unable to connect to Revit... will create a 10-meter wall once connected; port 8080 opened, no luck” (en; [source](https://github.com/mcp-servers-for-revit/mcp-servers-for-revit/issues/1))
- “list all pipes in the revit model -> Get element information failed: Method not found” (en; [source](https://github.com/mcp-servers-for-revit/revit-mcp/issues/28))
- “revit_create_level {elevation:900,name:'GL+900'} returns isError; reads like get_current_view_info work” (en; [source](https://github.com/bimwright/rvt-mcp/issues/21))
- “AI 建牆時沒有樓層參數就取 FirstOrDefault Level，牆建到非預期樓層、無法指定牆型” (zh; EN: create_wall silently uses the first Level in the project and Z=0; propose explicit level and wall type parameters.; [source](https://github.com/shuotao/REVIT_MCP_study/issues/144))
- “wall (0,2000)-(5000,2000); door at 2500,2000,0; FamilyInstance.Host is null” (en; [source](https://github.com/bimwright/rvt-mcp/issues/13))
- “用 OSI 七層模型分析 MCP 與 pyRevit 按鈕呼叫的介面隔離” (zh; EN: MCP only reaches the DB API, not UI buttons, so AI cannot trigger pyRevit Reload or test a button it just edited.; [source](https://github.com/shuotao/REVIT_MCP_study/issues/110))

**Why it happens.** A Revit MCP setup is an MCP server plus a Revit add-in; failures are mostly plumbing: the port is hardcoded and the plugin must be started after each restart, the server and plugin tool registries drift ("Method not found"), arguments disappear when a fresh server process is spawned per call, commands must be enabled in the settings. Silent defaults are worse: `create_wall` took the first level and Z=0 and never read the wall-type parameter; a hosted door needed `host_id`; stairs hung Revit for about a minute and crashed it. Users note a 10 s command timeout and 2 min websocket timeout ([source](https://zenn.dev/yuichi_ai/articles/879de49ee8e1bb)), errors hidden in dialogs ([source](https://zenn.dev/aec/articles/58aa31c1089332)), and that a benchmark found models "confidently claimed success without persisted state" ([source](https://github.com/mcp-servers-for-revit/mcp-servers-for-revit/issues/30)). UI buttons and dynamic commands are not reachable through the database API.

**What fixes it.** Align server and plugin versions, give explicit level, type and host, use a dry run, apply, then read the state back; one transaction per logical change; clear error messages.

**A good assistant** previews before it writes (list, propose, ask, apply, read back), never invents a level or wall type, reports Revit year and unit assumptions, and says "I could not verify" when read-back fails.

**Clarifying questions.** Which level and wall/door type? Which host element? Units (millimetres vs feet)? Do you want a preview first? Which Revit year and MCP server/plugin versions?

### 7. Editing or creating IFC without breaking it

**Symptoms in users' words**
- “assign_containerを忘れると床が表示されない。開口を作ってからドア窓をadd_filling” (ja; EN: Create floors, walls, a door and a window from scratch with IfcOpenShell: units, placement, containment, opening order; [source](https://zenn.dev/toggle_inc/articles/cf8df02f7b4ba7))
- “удалил элемент - файл открывается, но валидатор падает; смена класса требует смены типа” (ru; EN: Deleting elements or changing class via web-ifc passes basic checks but breaks strict schema validation; [source](https://habr.com/ru/articles/1094224/))
- “IFC generated by the user's own Python app fails to import: IfcAxis2Placement3D has no attribute PlacementRelTo.” (en; [source](https://community.osarch.org/discussion/1622/blenderbim-import-error))
- “started from the HelloWall sample and added an opening via IfcRelVoidsElement in a transaction; viewers show no hole” (en; [source](https://github.com/xBimTeam/XbimEssentials/issues/633))
- “how to add a custom pset to all walls where Domain=Bridge without commercial software” (en; [source](https://bimcorner.com/add-properties-to-ifc-using-ifcopenshell/))

**Why it happens.** An IFC edit must keep relationships valid. Forgetting `assign_container` leaves a floor invisible; a door needs the opening created first and then `add_filling`; an IFC2x3 validator required each `IfcLocalPlacement` to be referenced by exactly one product; deleting an element can leave orphan representations and placements (the file opens, the strict validator fails); changing a class without changing the type is inconsistent; web-ifc keeps showing the old class of a rewritten entity; typed values like `NominalValue` need the typed wrapper. Using raw `create_entity` instead of `ifcopenshell.api` gives files that open but have broken relationships. IfcMCP-style servers do not auto-save.

**What fixes it.** Use `ifcopenshell.api` (for example the pset functions), validate after editing, write to a new file, and keep a change journal keyed by GlobalId.

**A good assistant** says up front whether it can edit or only read, writes to a copy, validates, reports counts and does not delete silently.

**Clarifying questions.** May I write a new file or modify in place? What is the rule that selects elements (class, name, type)? Overwrite existing values? Which schema?

### 8. Which library or tool, and building viewers or converters

**Symptoms in users' words**
- “C# developer of a pipeline CAD must build an IFC export; asks where to start, about certification, and how to map table/variable data to IFC” (en; [source](https://forums.buildingsmart.org/t/4561))
- “Discord удалили, документация пропала; GLTF в разы больше IFC; остались на 1.5.1” (ru; EN: IFC.js project shut down, Discord deleted, docs vanished; GLTF bigger than IFC; settled on v1.5.1; [source](https://habr.com/ru/articles/846382/))
- “IFC里有大量非几何信息，viewer用不上；用xbim读到内存再整理几何输出成gltf，文件能小一半，但不保证每个都变小” (zh; EN: Introduces Xbim.GLTF: converts IFC to glTF dropping non-geometry data; sample file shrinks 2269KB to 989KB but a tiny sample grew.; [source](https://www.cnblogs.com/flowell/p/10838972.html))
- “how can i export dwg to ifc4 by ifcopenshell, my language is C++, is there an example for CAD to ifc4” (en; [source](https://github.com/IfcOpenShell/IfcOpenShell/issues/3124))
- “building an offline desktop app; ChatGPT code gives errors with xBIM assemblies” (en; [source](https://github.com/xBimTeam/XbimWebUI/issues/483))

**Why it happens.** The right library depends on language and task ([comparison table](../../04_open_source/libraries_and_toolkits.md)): IfcOpenShell for Python/C++ reading and safe editing, xBIM for .NET, web-ifc and That Open components for browsers. Licenses differ (LGPL, CDDL, MPL-2.0; AGPL for BIMserver and Xbim.IDS.Validator). Projects change: the IFC.js project shut down, its Discord and docs vanished and a team stayed on v1.5.1. Viewer formats (wexbim, fragments, XKT, glTF) drop properties, so geometry must stay linked to the data by GlobalId. DWG is not a starting point for IFC authoring.

**What fixes it.** Choose by language, task and license; pin versions; convert on the client or server and keep a separate property file.

**A good assistant** asks language, runtime, license and scale before recommending, never invents package names, and states that a viewing format is not IFC.

**Clarifying questions.** Language and runtime? Read-only or write? Browser or server? Commercial product (license)? Maximum file size?

### 9. Version, install and environment mismatches

**Symptoms in users' words**
- “Worked in 0.0.72, aborts in 0.0.77; trying 0.0.78 yields 'function StreamMeshes called with 4 arguments, expected 3'.” (en; [source](https://github.com/ThatOpen/engine_web-ifc/issues/2360))
- “npm装的web-ifc-three运行报WebAssembly LinkError (Import function not callable)，最后自己编译web-ifc替换node_modules并给nginx配wasm MIME” (zh; EN: React project with web-ifc-three throws WebAssembly LinkError; fixed by building web-ifc from source, copying the wasm, and serving .wasm with…; [source](https://blog.csdn.net/pumbkin/article/details/141029954))
- “list all pipes in the revit model -> Get element information failed: Method not found” (en; [source](https://github.com/mcp-servers-for-revit/revit-mcp/issues/28))
- “edit_georeferencing() rejects map_conversion keyword in IfcOpenShell 0.7.10 though the script worked before.” (en; [source](https://github.com/IfcOpenShell/IfcOpenShell/issues/5055))
- “conda环境里装ifcopenshell，PyCharm里要指定同一个环境” (zh; EN: Using ifcopenshell-python in a conda environment (title with three exclamation marks).; [source](https://blog.csdn.net/yhj_911/article/details/120957269))

**Why it happens.** web-ifc's JavaScript wrapper and its `.wasm` file must come from the same version ("StreamMeshes called with 4 arguments, expected 3"); the `.wasm` must be served with the right type and found by the configured path; a stray `pathlib.py` in site-packages broke imports; conda and pip builds contain different compiled schemas; arguments get renamed between releases (`map_conversion` to `coordinate_operation`); Revit 2027 changed namespaces and the Python engine.

**What fixes it.** Pin matching versions, copy the wasm from the same package version, set the wasm path, read the release notes, and check `pip show`/the build's schema list.

**A good assistant** asks for exact versions and the full traceback first, checks a version matrix before suggesting an upgrade, and avoids "just reinstall".

**Clarifying questions.** Exact package and version of each part? Bundler or environment (conda, pip, Vite)? Full error text? Did it work on an older version?

### 10. Non-ASCII text garbled or truncated

**Symptoms in users' words**
- “which chinese encoding pattern do you use in IFC generation? tried utf-8 but still messy code” (en; [source](https://github.com/IfcOpenShell/IfcOpenShell/issues/571))
- “IFCBUILDINGELEMENTPROXY name mixes \X2\ escapes with raw Cyrillic; Python exception on read” (ru; EN: SolidWorks IFC has Cyrillic names written raw alongside \X2\ pieces, Python read fails.; [source](https://github.com/IfcOpenShell/IfcOpenShell/issues/3182))
- “'\X2\7d20586b571f\X0\' decodes wrong; uppercase hex decodes right” (en; [source](https://github.com/ThatOpen/engine_web-ifc/issues/949))
- “ifcopenshell.Error: Unable to parse IFC SPF header; resaving without BOM works.” (en; [source](https://github.com/IfcOpenShell/IfcOpenShell/issues/4256))
- “euro symbol makes wofstream and wcout crash; need raw string” (de; EN: The Euro sign decoded from \X2\ crashes wofstream/wcout; can the conversion be disabled?; [source](https://github.com/IfcOpenShell/IfcOpenShell/issues/388))

**Why it happens.** IFC files are ASCII STEP text; any other character must be escaped (`\X2\hex\X0\` for Unicode, `\X\` for ISO 8859-1). Libraries decode this on read and encode on write, so the right approach is to hand them plain Unicode strings. Problems come from exporters that write raw Cyrillic or Chinese (invalid), a byte-order mark before the header, a doubled backslash, lowercase hex in `\X2\` that one decoder rejected (fixed in web-ifc), an ifcXML parser that truncated strings (disabled), and consoles that cannot print the result.

**What fixes it.** Let the library do the encoding, strip the BOM, repair or replace the exporter, validate the file.

**A good assistant** shows the raw escaped text next to the decoded text, decides whether the file is invalid or the viewer is wrong, and does not "fix" mojibake by re-saving the file as UTF-8.

**Clarifying questions.** Which exporter wrote the file? Does the problem appear in more than one viewer? Raw bytes of the bad line? Which library and version reads it?

### 11. Housekeeping scripts in Revit (views, sheets, parameters, duplicates)

**Symptoms in users' words**
- “my script finds and deletes the duplicate instances listed in the error; with 4 identical instances in the same place only one is removed and I have to rerun until one is left” (en; [source](https://forum.dynamobim.com/t/deleting-duplicate-instances-in-revit/115296))
- “duplicated a structural foundation with Element.Duplicate then SetParameter on width, length, thickness doesn't work; sizes are in an Excel file” (en; [source](https://forum.dynamobim.com/t/updating-structural-foundation-size-parameters-via-excel-input/115236))
- “my script creates View Filters; works with instance parameters but throws object reference error with type parameters” (en; [source](https://forum.dynamobim.com/t/automating-filter-creation/108901))
- “I create sheets and place views with Dynamo but can't find how to add a viewport; later wanted to move the view title but selection grabs the whole viewport” (en; [source](https://forum.dynamobim.com/t/how-to-add-viewport-in-sheets-by-dynamo/114310))
- “want to automate pre-publishing in Forma: unload all links, close worksets, save; API can't unload a link whose workset is closed” (en; [source](https://forum.dynamobim.com/t/unload-revit-linked-with-its-worksets-closed/115193))

**Why it happens.** Revit rules trip scripts: type parameters must be read from the type element (an instance lookup returns null); to change sizes you duplicate the family *type*, not the element; create all views first and only then export or place them (a reported workaround for the last elevation landing differently); a link cannot be unloaded while its worksets are closed unless transmission data is set; deleting "project parameters" only hides them. Length values in the Revit API are internal units (feet), which surprises people who think in millimetres (general Revit knowledge, not from the records).

**What fixes it.** Collect first and show the list, change in one transaction, produce an old-to-new table, skip items already processed, and guard against name collisions.

**A good assistant** works dry-run first, asks for confirmation before bulk changes, reports exactly what changed, and treats localized names (German or Russian family and parameter names) carefully.

**Clarifying questions.** Which elements are in scope (this view, level, whole project)? Naming pattern and what to do on collision? Type or instance parameter? OK to run on a copy first?

### 12. Quantities that do not match the model, Revit or the cost sheet

**Symptoms in users' words**
- “IfcOpenShell QTO gives wrong area for an IfcWindow defined by an IfcWindowType with mesh geometry, Blender shows right value; attached test file” (en; [source](https://github.com/IfcOpenShell/IfcOpenShell/issues/5349))
- “объёмы в Ревите 17 кликов, в ifcopenshell 40 строк; IFC слишком сложный” (ru; EN: Quantity takeoff is 17 clicks in Revit/Solibri vs ~40 lines in IfcOpenShell; flat formats beat IFC; [source](https://habr.com/ru/articles/868186/))
- “Cost rows are not one-to-one with model quantities (installation rows skipped, others split); wants not to build in-house.” (en; [source](https://community.osarch.org/discussion/comment/27265))
- “console app generates wexbim and a props file; wants X,Y,Z, area and volume per object; bounding-box attempt is wrong because units are not converted” (en; [source](https://github.com/xBimTeam/XbimEssentials/issues/619))
- “spreadsheet-based BoQ is how tenders work; wants a simple CSV BoQ export preserving GlobalId/Tag/location links to IFC elements” (en; [source](https://github.com/IfcOpenShell/IfcOpenShell/issues/7762))

**Why it happens.** Qto sets exist only if the exporter wrote them and may be net or gross; geometry-derived volumes are reliable only for closed solids and ignore how a Revit schedule counts openings and overlaps; an area computed from a type mesh can differ from Blender's; units may not be converted; and cost sheets are not one-to-one with model quantities (installation rows skipped, others split). An xBIM maintainer's advice is that areas and dimensions are subjective, so prefer Qto/properties.

**What fixes it.** Take Qto first, compute from geometry as a flagged fallback, convert units explicitly, and define a cross-reference ID between cost rows and elements.

**A good assistant** reports the source of each number (Qto, property or geometry), the unit, the elements with no quantities, and likely reasons for a percentage gap.

**Clarifying questions.** Which quantity (net/gross, area/volume)? Compare against what (Revit schedule, cost sheet)? Are openings subtracted? Which units?

### 13. IFC schema version not supported (IFC4X3 and friends)

**Symptoms in users' words**
- “i am trying to open a IFC4x3 file with ifcopenshell python but i get the error that IFC4x3 is not supported” (en; [source](https://github.com/IfcOpenShell/IfcOpenShell/issues/6886))
- “so i wanted to test it with a simple example: schema_by_name IFC4x3 throws No schema named IFC4x3” (en; [source](https://github.com/IfcOpenShell/IfcOpenShell/issues/2382))
- “web-ifcを上げる前に何が変わるか。0.0.50はIFC4X3_ADD2でUnsupported Schema、0.0.78のブラウザ版StreamMeshesでBindingError” (ja; EN: Comparing 13 web-ifc versions on the same IFC: unsupported IFC4.3 in old versions, geometry count changes, StreamMeshes BindingError in 0.0.78; [source](https://zenn.dev/grok_prtex/articles/webifc-version-compare))
- “IFC4x3 IfcProduct lacks the GetPropertySet helper known from other schemas” (en; [source](https://github.com/xBimTeam/XbimEssentials/issues/610))
- “Short problem statement, entities named IfcTransportElement, IfcDiscreteAccessory.” (en; [source](https://forums.buildingsmart.org/t/merging-ifc2-3-elntities-in-a-ifc4-file/2846))

**Why it happens.** The schema identifier must match exactly and case-sensitively (`IFC4X3_ADD2`, not `IFC4x3`), and the compiled schemas depend on the build: a conda-forge package had it where a bundled build did not, and the catalog notes that a 0.9.0.post1 wheel lists only 2X3, 4 and 4X3. web-ifc read IFC4.3 only from version 0.0.53; xBIM lacked 4x3 helper methods; `add()` does not work across schemas; migrating 4x3 to IFC4 drops entities such as alignments.

**What fixes it.** Read `FILE_SCHEMA` first, check what the installed build supports, upgrade the library, and migrate with schema-aware tools while listing what is lost.

**A good assistant** reports the file's schema before anything else, says which library version supports it, and never calls a conversion lossless.

**Clarifying questions.** What does `FILE_SCHEMA` say? Which library build and install method? Do you need geometry or only data? Is a downgrade acceptable, and what loss is OK?

### 14. GlobalId vs Revit UniqueId, diffs and change tracking

**Symptoms in users' words**
- “RevitのUniqueIdとIFCのGUIDが全然違って見えるので、どう対応するのか知りたい。” (ja; EN: Converting between Revit UniqueId and IFC GUID; [source](https://qiita.com/Takashi_Kasuya/items/97899d15e7ec0186eecf))
- “any other identifier than GlobalId to know an object's geometry is unchanged between versions? the authoring tool regenerates the GlobalIds every week, only geometric extents matter” (en; [source](https://community.osarch.org/discussion/comment/12255#Comment_12255))
- “when a tool re-issues GlobalIds the same element shows as one deletion and one addition; want to treat element as unchanged if placement within 5 cm” (en; [source](https://github.com/IfcOpenShell/IfcOpenShell/issues/8412))
- “IFCGuid parameter differs from the GUID in exported file.” (en; [source](https://forums.autodesk.com/t5/revit-api-forum/ifc-guid-is-different-in-the-ifcguid-parameter-written-by-revit/td-p/12650094))
- “all 1,025 matched elements flagged as property changes because pset STEP ids are compared; geometry not checked without MODEL_VIEW; wall thickened 1.5x gave empty change register” (en; [source](https://github.com/IfcOpenShell/IfcOpenShell/issues/9610))

**Why it happens.** The two ids are not the same: per one write-up, Revit keeps an imported IFC GUID, otherwise derives it from the UniqueId and the element id, and some entities get fresh ones; the `IFCGuid` parameter can differ from the exported GUID depending on settings. When an authoring tool regenerates GlobalIds, a diff shows one deletion and one addition for the same wall. A diff that compared property-set STEP ids flagged all 1,025 matched elements as changed (fixed in a pull request). `by_guid` failed for ids that were legal but not valid base64.

**What fixes it.** Match by class, geometry fingerprint and position when ids churn, compare content rather than STEP ids, store the exported GUID in a parameter, keep a mapping table.

**A good assistant** warns when ids do not match across versions, offers a fallback with a stated confidence, and does not equate Revit element ids, UniqueIds and GlobalIds.

**Clarifying questions.** Which two files and from which tool and export settings? Is the same element expected to keep its id? What counts as "changed" (geometry, properties, both)?

## Real questions

All rows are real, observed at the linked source and paraphrased in the original language (no usernames). "EN gloss" is shown for non-English rows. Sources are mostly GitHub issues, community forums and developer blogs, so the personas are mostly developers. Where a record tagged with a non-English language carries an English paraphrase in the dataset, it is shown as stored.

| lang | question (original-language paraphrase) | EN gloss | persona | source |
|---|---|---|---|---|
| en | 2 GB IFC from Synchro, 16 GB RAM, open() runs out of memory; asks about lazy loading, renumbered STEP, or another storage tech | — | developer programmer | [github.com](https://github.com/IfcOpenShell/IfcOpenShell/issues/2025) |
| en | I loop over all IFC in a folder and write an Excel sheet per file with chosen entity parameters. Exporter 22.1 works, 22.6 changes the structure and COBie/custom properties are missed. | — | developer programmer | [github.com](https://github.com/IfcOpenShell/IfcOpenShell/issues/3978) |
| en | i am trying to open a IFC4x3 file with ifcopenshell python but i get the error that IFC4x3 is not supported | — | developer programmer | [github.com](https://github.com/IfcOpenShell/IfcOpenShell/issues/6886) |
| en | Deleting 1000 of 20k elements takes over 10 minutes. | — | developer programmer | [community.osarch.org](https://community.osarch.org/discussion/2673/deleting-many-objects-takes-forever) |
| en | After upgrading from 0.7 to 0.8.1 a slab produces no geometry in a script but renders in Bonsai. | — | developer programmer | [github.com](https://github.com/IfcOpenShell/IfcOpenShell/issues/6142) |
| en | Signed tetrahedra volume at projected coordinates loses precision; 2.8 m3 wall gives 2.75. | — | researcher academic | [github.com](https://github.com/IfcOpenShell/IfcOpenShell/issues/9770) |
| en | Cannot get start and end points of a beam axis from its placement; both come out identical. | — | structural engineer | [community.osarch.org](https://community.osarch.org/discussion/2704/get-ifcbeam-coordinates-in-3d-space) |
| en | IFC generated by the user's own Python app fails to import: IfcAxis2Placement3D has no attribute PlacementRelTo. | — | developer programmer | [community.osarch.org](https://community.osarch.org/discussion/1622/blenderbim-import-error) |
| en | python geometry iterator memory grows until iteration ends; very large IFC files on 64 GB machines; num_threads=32 gives >60GB, 1 thread ~25GB | — | developer programmer | [github.com](https://github.com/IfcOpenShell/IfcOpenShell/issues/6905) |
| en | Extracting elements with IfcPatch drops georeferencing; eastings and northings turn into Blender offset. | — | bim coordinator | [github.com](https://github.com/IfcOpenShell/IfcOpenShell/issues/8199) |
| en | edit_georeferencing() rejects map_conversion keyword in IfcOpenShell 0.7.10 though the script worked before. | — | developer programmer | [github.com](https://github.com/IfcOpenShell/IfcOpenShell/issues/5055) |
| en | how to add a custom pset to all walls where Domain=Bridge without commercial software | — | developer programmer | [bimcorner.com](https://bimcorner.com/add-properties-to-ifc-using-ifcopenshell/) |
| en | two walls overlap by 50mm but no clash found; section faces meet perfectly on the same axis. shift 2mm and clash is detected. corner walls that overshoot also missed | — | developer programmer | [github.com](https://github.com/IfcOpenShell/IfcOpenShell/issues/4594) |
| en | IfcCsv export returns 0 for x,y,z of elements represented by mapped items; the mapped item transformation is ignored. | — | developer programmer | [github.com](https://github.com/IfcOpenShell/IfcOpenShell/issues/6277) |
| en | ifcopenshell.Error: Unable to parse IFC SPF header; resaving without BOM works. | — | developer programmer | [github.com](https://github.com/IfcOpenShell/IfcOpenShell/issues/4256) |
| en | hi, program exits unexpectedly on a model with 300000 components, Aborted() from the wasm node build | — | developer programmer | [github.com](https://github.com/ThatOpen/engine_web-ifc/issues/538) |
| en | I need to iterate all flat geometries; StreamAllMeshes blocks the UI so I loop GetFlatMesh over express ids, memory is much higher | — | developer programmer | [github.com](https://github.com/ThatOpen/engine_web-ifc/issues/1380) |
| en | simple ifc works on 0.0.36 (geometry and data) but on 0.0.39 and above getting props throws | — | developer programmer | [github.com](https://github.com/ThatOpen/engine_web-ifc/issues/402) |
| en | converting an IFC larger than ~2GB crashes with Aborted, emscripten_resize_heap fails past ~4 GiB, same with readFromCallback | — | developer programmer | [github.com](https://github.com/ThatOpen/engine_fragment/issues/258) |
| en | '\X2\7d20586b571f\X0\' decodes wrong; uppercase hex decodes right | — | developer programmer | [github.com](https://github.com/ThatOpen/engine_web-ifc/issues/949) |
| en | Worked in 0.0.72, aborts in 0.0.77; trying 0.0.78 yields 'function StreamMeshes called with 4 arguments, expected 3'. | — | developer programmer | [github.com](https://github.com/ThatOpen/engine_web-ifc/issues/2360) |
| en | Mesh coordinates are not changed per IfcMapConversion in web-ifc 0.0.68. | — | developer programmer | [github.com](https://github.com/ThatOpen/engine_web-ifc/issues/1404) |
| en | calling IsTypedBy for each element is much slower since 6.0.442; supplies repro solution comparing 5.1.341 and 6.0.442 on a public MEP sample model | — | developer programmer | [github.com](https://github.com/xBimTeam/XbimEssentials/issues/674) |
| en | pasted an ExtractMaterialData helper that checks HasAssociations and IfcRelAssociatesMaterial; some elements return no material | — | developer programmer | [github.com](https://github.com/xBimTeam/XbimEssentials/issues/642) |
| en | started from the HelloWall sample and added an opening via IfcRelVoidsElement in a transaction; viewers show no hole | — | developer programmer | [github.com](https://github.com/xBimTeam/XbimEssentials/issues/633) |
| en | IFC4x3 IfcProduct lacks the GetPropertySet helper known from other schemas | — | developer programmer | [github.com](https://github.com/xBimTeam/XbimEssentials/issues/610) |
| en | Express type lookup uses ToUpper() so 'i' becomes dotted capital I and no type matches under tr-TR; proposes ToUpperInvariant and gives an xUnit test | — | developer programmer | [github.com](https://github.com/xBimTeam/XbimEssentials/issues/670) |
| en | building an offline desktop app; ChatGPT code gives errors with xBIM assemblies | — | developer programmer | [github.com](https://github.com/xBimTeam/XbimWebUI/issues/483) |
| en | own converter writes IFC2x3; IfcCheckingTool reports a cardinality violation of inverse PlacesObject on parent IfcLocalPlacements of IfcDistributionFlowElement instances; cannot understand the rule | — | developer programmer | [forums.buildingsmart.org](https://forums.buildingsmart.org/t/4372) |
| en | reading IFC into an own system; proxies appear that are really walls or doors; is there a generic way to detect what a proxy is rather than one converter per CAD workflow? | — | developer programmer | [forums.buildingsmart.org](https://forums.buildingsmart.org/t/5130) |
| en | GUIDs produced have a letter as the first character; asks if this is known | — | developer programmer | [github.com](https://github.com/ifcquery/ifcplusplus/issues/305) |
| ja | IfcOpenShellのIfcCSVだとAttributeしか書き出せないので、PropertySetとMaterialも一緒にExcelへ出したい | IfcCSV only exports attributes; how do I dump attributes, property sets and materials of an IFC to Excel? | bim coordinator | [zenn.dev](https://zenn.dev/miyamiyaumya/articles/19a4247133dde6) |
| ja | IFCファイルから階の名前と高さ(Elevation)をIfcOpenShellで取り出したい | How to get the storey names and elevations from an IFC with IfcOpenShell | developer programmer | [zenn.dev](https://zenn.dev/cote2/articles/6459c1c44091da) |
| ja | 大きいIFCを開くと全インスタンス・属性を先にパースして遅くメモリを食う | Opening huge IFC with IfcOpenShell is slow and memory-hungry; lazy loading in 0.9.0 | developer programmer | [qiita.com](https://qiita.com/kiyuka/items/0d2ef739a0d34606a52f) |
| ja | assign_containerを忘れると床が表示されない。開口を作ってからドア窓をadd_filling | Create floors, walls, a door and a window from scratch with IfcOpenShell: units, placement, containment, opening order | developer programmer | [zenn.dev](https://zenn.dev/toggle_inc/articles/cf8df02f7b4ba7) |
| ja | web-ifcを上げる前に何が変わるか。0.0.50はIFC4X3_ADD2でUnsupported Schema、0.0.78のブラウザ版StreamMeshesでBindingError | Comparing 13 web-ifc versions on the same IFC: unsupported IFC4.3 in old versions, geometry count changes, StreamMeshes BindingError in 0.0.78 | developer programmer | [zenn.dev](https://zenn.dev/grok_prtex/articles/webifc-version-compare) |
| ja | RevitのUniqueIdとIFCのGUIDが全然違って見えるので、どう対応するのか知りたい。 | Converting between Revit UniqueId and IFC GUID | developer programmer | [qiita.com](https://qiita.com/Takashi_Kasuya/items/97899d15e7ec0186eecf) |
| ja | 協力会社の重いモデルや古いモデルを開かずに値だけ取り出したい。API/プラグイン経由は遅くAPSは組織整備が前提 | Extract values from heavy Revit models from subcontractors without opening them; ETL to columnar store | developer programmer | [zenn.dev](https://zenn.dev/tomosandego/articles/59e6cf8dfe60bc) |
| ja | AIに『3〜10階に同じ部屋割りを作って』『窓幅を一括変更』『20m2未満の部屋を赤に』と頼めるか | Explainer for architects: using Revit-MCP so AI can create/modify Revit elements in natural language | architect | [zenn.dev](https://zenn.dev/yuichi_ai/articles/879de49ee8e1bb) |
| ja | Revitのエラーはダイアログに隠れてエージェントが結果を見られない。DLLロックやPDB無しで行番号が出ない | Letting Claude Code build Revit add-ins autonomously; MCP found a poor fit versus running C# in the live model | developer programmer | [zenn.dev](https://zenn.dev/aec/articles/58aa31c1089332) |
| zh | ifcxml里Name含中文或西里尔字符，读出来被截断，非拉丁字符成了字符串起点 | Strings with Chinese/Cyrillic characters get truncated when reading an ifcXML file with IfcOpenShell. | developer programmer | [github.com](https://github.com/IfcOpenShell/IfcOpenShell/issues/3499) |
| zh | 用ifcopenshell.geom把每个构件的顶点面取出来，自己拼成gltf | Python code to generate glTF from an IFC model with IfcOpenShell geometry. | developer programmer | [blog.csdn.net](https://blog.csdn.net/liuzk423/article/details/136849803) |
| zh | python viewer 碰到 IfcRelNests 直接崩溃，删掉那行就能加载 | IfcOpenShell python viewer segfaults on IfcRelNests; removing the line lets the file load. | developer programmer | [ask.csdn.net](https://ask.csdn.net/questions/5599889) |
| zh | npm装的web-ifc-three运行报WebAssembly LinkError (Import function not callable)，最后自己编译web-ifc替换node_modules并给nginx配wasm MIME | React project with web-ifc-three throws WebAssembly LinkError; fixed by building web-ifc from source, copying the wasm, and serving .wasm with application/wasm in nginx. | developer programmer | [blog.csdn.net](https://blog.csdn.net/pumbkin/article/details/141029954) |
| zh | AI 建牆時沒有樓層參數就取 FirstOrDefault Level，牆建到非預期樓層、無法指定牆型 | create_wall silently uses the first Level in the project and Z=0; propose explicit level and wall type parameters. | bim coordinator | [github.com](https://github.com/shuotao/REVIT_MCP_study/issues/144) |
| zh | 用 OSI 七層模型分析 MCP 與 pyRevit 按鈕呼叫的介面隔離 | MCP only reaches the DB API, not UI buttons, so AI cannot trigger pyRevit Reload or test a button it just edited. | developer programmer | [github.com](https://github.com/shuotao/REVIT_MCP_study/issues/110) |
| zh | 读入IFC文件，按GlobalID找到梁，改名字，加属性集，再写出新文件 | Modify an IfcBeam's name and add a property set by looking it up via GlobalId in Java and writing a new IFC file. | developer programmer | [cnblogs.com](https://www.cnblogs.com/herd/p/12183392.html) |
| zh | 用xBIM遍历IFC空间写入Excel，面积体积优先取Quantity | xBIM: output IFC space data to an Excel report | developer programmer | [cnblogs.com](https://www.cnblogs.com/w2011/p/8424405.html) |
| ru | объёмы в Ревите 17 кликов, в ifcopenshell 40 строк; IFC слишком сложный | Quantity takeoff is 17 clicks in Revit/Solibri vs ~40 lines in IfcOpenShell; flat formats beat IFC | developer programmer | [habr.com](https://habr.com/ru/articles/868186/) |
| ru | как проверять IFC по IDS пакетно, с отчётами html и json | How to check IFC models against IDS requirements (example from SPb CGE) in batch with reports | developer programmer | [habr.com](https://habr.com/ru/articles/883016/) |
| ru | удалил элемент - файл открывается, но валидатор падает; смена класса требует смены типа | Deleting elements or changing class via web-ifc passes basic checks but breaks strict schema validation | developer programmer | [habr.com](https://habr.com/ru/articles/1094224/) |
| ru | после переписывания сущности web-ifc показывает старый класс | web-ifc keeps the original class of a rewritten entity so viewer and IDS show old class | developer programmer | [habr.com](https://habr.com/ru/articles/1100956/) |
| ru | Discord удалили, документация пропала; GLTF в разы больше IFC; остались на 1.5.1 | IFC.js project shut down, Discord deleted, docs vanished; GLTF bigger than IFC; settled on v1.5.1 | developer programmer | [habr.com](https://habr.com/ru/articles/846382/) |
| ru | выгрузить пачку rvt в IFC с разными настройками, экономя память | Batch export many .rvt to IFC with per-model Excel/JSON settings and workset exclusion | bim coordinator | [github.com](https://github.com/i-savelev/BatchIfcExporter) |
| ru | недокументированные опции IFC-экспортёра ведут себя по-разному, поэтому стандартное окно экспорта | Undocumented IFC exporter options behave differently between Revit versions | developer programmer | [habr.com](https://habr.com/ru/articles/1087472/) |
| ru | нужно выгрузить 3D модель из Plant 3D в IFC; Codemill платный и с ручным маппингом, через Navisworks не экспортирует, в Ревите объекты не распознаются | How to get an IFC from a Plant 3D 2025 project without losing 3D objects and data? | developer programmer | [forum.dwg.ru](https://forum.dwg.ru/showthread.php?t=173570) |
| es | Creá cuatro muros de 3 m de alto formando un rectángulo de 5 × 4 m | Spanish prompts: what elements do I have selected in Archicad; create four 3 m walls forming a 5x4 m rectangle. | architect | [github.com](https://github.com/joacos/archicad-mcp) |
| en | automating IFC export of several Revit files from BIM 360; every IFC from the script is empty, manual export fine; checked classification and LOI mapping and phases | — | developer programmer | [forum.dynamobim.com](https://forum.dynamobim.com/t/ifc-export-node-return-an-empty-ifc/82822) |
| en | converted Python scripts to Revit 2027; IFC export scripts fail incl. custom export setups and basic doc.Export; generic PythonEvaluator error | — | developer programmer | [forum.dynamobim.com](https://forum.dynamobim.com/t/are-anyone-able-to-export-ifc-using-dynamo-in-revit-2027/115000) |
| en | adapted Genius Loci script with many AddOption values but still plain IFC; is AddOption documented | — | developer programmer | [forum.dynamobim.com](https://forum.dynamobim.com/t/ifc-export-settings-ifcfiletype/91626) |
| en | tried several Revit/Dynamo versions, reset Dynamo, disabled add-ins, reinstalled Revit | — | developer programmer | [forum.dynamobim.com](https://forum.dynamobim.com/t/unrecoverable-error-during-ifc-export-using-dynamo/113291) |
| en | Document.Export produces empty IFC. | — | developer programmer | [forums.autodesk.com](https://forums.autodesk.com/t5/revit-api-forum/ifc-export-result-empty-files/td-p/11082264) |
| en | using AddOption ClassificationName and ClassificationFieldName from Python has no effect; data only exported when set from UI | — | developer programmer | [github.com](https://github.com/Autodesk/revit-ifc/issues/277) |
| en | Claude replies: unable to connect to Revit... will create a 10-meter wall once connected; port 8080 opened, no luck | — | architect | [github.com](https://github.com/mcp-servers-for-revit/mcp-servers-for-revit/issues/1) |
| en | revit_create_level {elevation:900,name:'GL+900'} returns isError; reads like get_current_view_info work | — | developer programmer | [github.com](https://github.com/bimwright/rvt-mcp/issues/21) |
| en | stairs are the hard case: Error-severity failure hung Revit ~60s then crashed | — | structural engineer | [github.com](https://github.com/bimwright/rvt-mcp/issues/14) |
| en | wall (0,2000)-(5000,2000); door at 2500,2000,0; FamilyInstance.Host is null | — | architect | [github.com](https://github.com/bimwright/rvt-mcp/issues/13) |
| en | list all pipes in the revit model -> Get element information failed: Method not found | — | mep engineer | [github.com](https://github.com/mcp-servers-for-revit/revit-mcp/issues/28) |
| en | benchmark of 15 deterministic BIM tasks: model confidently claimed success without persisted state | — | developer programmer | [github.com](https://github.com/mcp-servers-for-revit/mcp-servers-for-revit/issues/30) |
| en | my script finds and deletes the duplicate instances listed in the error; with 4 identical instances in the same place only one is removed and I have to rerun until one is left | — | bim coordinator | [forum.dynamobim.com](https://forum.dynamobim.com/t/deleting-duplicate-instances-in-revit/115296) |
| en | connected Claude to pyRevit MCP; want a free agent for pyRevit 7 to duplicate and rename sheets; tried Gemini API with Continue and local Ollama qwen2.5, didn't work | — | bim coordinator | [discourse.pyrevitlabs.io](https://discourse.pyrevitlabs.io/t/connecting-agent-to-pyrevit-mcp-newbie/10627) |
| en | Tender and cost work runs on spreadsheets; I need rows traceable to IFC elements, e.g. ventilators FAN-01..03 per room, and summarise equal elements by floor. | — | estimator qs | [github.com](https://github.com/IfcOpenShell/IfcOpenShell/issues/7762) |
| en | In Poland Excel regional settings follow the interface language, so dotted numbers become text; today I fix types in Power Query. XLSX and ODS export fine. | — | bim coordinator | [github.com](https://github.com/IfcOpenShell/IfcOpenShell/issues/4290) |
| en | Browser view has no PDF/print export; CSV export has junk columns, no unit column, no decimal setting; I just ctrl+C into Excel. | — | estimator qs | [github.com](https://github.com/IfcOpenShell/IfcOpenShell/issues/5736) |
| en | Use bcf.v3 to create one issue per missing/wrong property; library demands IFC instances; any standard way to push only GUIDs? | — | bim coordinator | [community.osarch.org](https://community.osarch.org/discussion/3695/bcf-from-xlsx-file) |
| en | Cost rows are not one-to-one with model quantities (installation rows skipped, others split); wants not to build in-house. | — | estimator qs | [community.osarch.org](https://community.osarch.org/discussion/comment/27265) |
| en | junior data specialist wants Revit data incl. custom psets in a database for a webapp and maintenance without paying heavily for Autodesk APIs | — | developer programmer | [forums.buildingsmart.org](https://forums.buildingsmart.org/t/6034) |
| en | when a tool re-issues GlobalIds the same element shows as one deletion and one addition; want to treat element as unchanged if placement within 5 cm | — | bim coordinator | [github.com](https://github.com/IfcOpenShell/IfcOpenShell/issues/8412) |
| en | any other identifier than GlobalId to know an object's geometry is unchanged between versions? the authoring tool regenerates the GlobalIds every week, only geometric extents matter | — | developer programmer | [community.osarch.org](https://community.osarch.org/discussion/comment/12255#Comment_12255) |

## Ready test prompts

All prompts below are **synthetic** (not real quotes). They are curated and, where the original was stiff, reworded to sound like a person at a keyboard. "Base" names the synthetic or real record it was derived from; "new" means written for this file from a real pattern. `file` = an IFC or Revit model (or folder of files) must be available; `no file` = a knowledge or code-writing answer. Where the assistant has no code-execution tool, "run" means "write the code and say it was not run".

| lang | prompt | type | difficulty | expected behavior |
|---|---|---|---|---|
| en | how do i loop over 40 ifc files in a folder and dump all wall areas to one csv with ifcopenshell | how_to | easy | no file. Loop with `ifcopenshell.open`, `by_type("IfcWall")`, read the area from `Qto_WallBaseQuantities` (say which area: net or gross), one CSV with a file-name column; mention walls without Qto and closing files. Base: en-mea-s014 |
| en | get all walls with their fire rating pset, list name + value | model_task | medium | file. Return IfcWall name/GlobalId with `Pset_WallCommon.FireRating`, resolve the type as well, flag missing or empty values; mention IfcWallStandardCase in IFC2x3. Base: en-stackoverflow-s001 |
| en | add a pset ARC_Data to all IfcWall with Loadbearing (bool) and CostGroup (text) taken from the Name prefix. dont touch the existing psets | model_task | hard | file, write access. Create the pset through the API (pset add/edit functions), derive CostGroup from the prefix, leave other sets untouched, write a new file, report counts and examples. Base: en-psets-s004 (reworded) |
| en | rename the property Brandwerendheid to FireRating inside Pset_WallCommon everywhere | model_task | medium | file, write access. Find the property in all psets and on types, move or rename it into `Pset_WallCommon.FireRating` keeping values, handle clashes with an existing FireRating, report changes. Base: en-psets-s012 |
| en | my get_volume numbers are off by 2% on elements at state plane coords. whats going on | how_to | medium | file or no file. Explain float precision far from the origin when summing tetrahedra, suggest computing relative to a local origin; reproduce on one wall if a file is loaded. Base: en-us-canada-infra-s012 |
| es | como saco el area neta de todos los muros con ifcopenshell en python? me da None | how_to | medium | no file. Show `get_psets` with Qto filter, explain that Qto sets exist only if exported, give a geometry fallback and say it is a fallback. Base: es-latam-s013 |
| ko | ifcopenshell로 벽 이름이랑 면적 엑셀로 뽑는 코드 짜줘 | how_to | medium | no file. Script over IfcWall reading `Qto_WallBaseQuantities`, write CSV/Excel with GlobalId and Name; mention missing quantities. Base: ko-korea-s011 |
| no | æøå blir rare tegn i navnene når jeg leser IFC med ifcopenshell, hvorfor | troubleshooting | medium | file or no file. Explain `\X2\` escaping, check whether the raw file is escaped or contains raw bytes/BOM, advise not to re-encode the file by hand. Base: no-norway-s012 |
| en | for each IfcWall give me HasOpenings -> IfcOpeningElement -> FillsVoids, i keep mixing up which side is the inverse | model_task | medium | file. Traverse `IfcRelVoidsElement` and `IfcRelFillsElement`; output wall, opening, filler; say which attributes are inverse. Base: en-dev-s003 |
| en | get world coords of the start/end of every IfcBeam axis, ignore the box geometry | model_task | medium | file. Compute the placement matrix and axis endpoints (not the mesh); fall back to extrusion direction and depth; state coordinates are world. Base: en-dev-s008 |
| en | delete everything except IfcWall and IfcSlab, file has 20k elements and my delete loop takes 10 min. do it fast | model_task | medium | file, write access. Extract a subset by class with a batch/patch recipe rather than per-element deletion; save a new file; report counts before and after. Base: en-dev-s011 |
| ru | добавь всем IfcDoor пропертю Pset_Custom.FireRating=EI30 где пусто | model_task | hard | file, write access. Add the property only where empty or missing, create the pset if needed, save to a new file, report how many were changed. Base: ru-dwg-other-s012 |
| ru | смени класс у IfcBuildingElementProxy с именем Колонна* на IfcColumn вместе с типом, чтоб не сломать валидацию | model_task | hard | file, write access. Change class and type together, keep relationships valid, run validation, report results; do not touch other proxies. Base: ru-habr-dev-s008 |
| en | how do i make a basic IfcRoad w/ a straight alignment between two points in ifcopenshell? just a minimal example | how_to | medium | no file. `root.create_entity` for IfcRoad, alignment API for a horizontal segment, aggregate under the site; say there is no dedicated road API and that the file schema must be IFC4X3_ADD2. Base: en-infra-s017 |
| en | how do i get the element on the other side of a duct port in ifcopenshell? ports are nested but i keep getting None | troubleshooting | medium | no file. Explain nesting via `IsNestedBy`/`Nests`, `IfcRelConnectsPorts` (ConnectedTo/ConnectedFrom), and the system helpers; note some attributes do not exist on the entity. Base: en-mep-s015 |
| en | my generated ifc wont open, error says PlacementRelTo missing. validate it? | model_task | medium | file. Run validation, find an `IfcLocalPlacement` pointing at an axis placement, suggest the fix in a copy. Base: en-osarch-s014 |
| en | can you actually edit this ifc or just read it? add a pset Pset_Custom to all IfcDoor and save | model_task | medium | file. First state honestly whether editing tools exist; if yes add the pset through the API, save to a new file, report count and verify by re-reading; if no, say read-only. Base: en-osarch-s017 |
| en | ids shows the spec as skipped, not failed, when no elements match. how do i make it fail? | troubleshooting | medium | no file. Explain applicability and `minOccurs`/`maxOccurs` semantics and how to require at least one match; mention abstract classes like `IfcElement` have no instances. Base: en-val-s009 |
| en | need this 4x3 file in ifc4 for a legacy tool. migrate and tell me whats lost (alignments etc) | model_task | hard | file, write access. Migrate with schema-aware tooling, list entities with no IFC4 equivalent (alignment, pavement...), never call it lossless. Base: en-vm-s015 |
| en | triangulate the doors and give me the vertex count per door, geometry seems broken on some | model_task | medium | file. Iterate IfcDoor with `create_shape`/iterator settings, report vertex and face counts, list the doors that fail and the error. Base: en-stackoverflow-s003 |
| en | how far from 0,0,0 are the elements? any precision risk with float | model_task | medium | file. Compute the world bounding box, report the maximum distance from origin in model units and metres, warn above about 10 km. Base: mul-coord-s003 |
| ja | 400MBのIFCをlazyで開いて壁だけ数えて。メモリどれくらい使った？ | model_task | medium | file. Open with lazy loading (needs 0.9+; say if the version is older), count IfcWall, report time and memory. Base: ja-fs-s013 |
| zh | ifcopenshell怎么转gltf，构件属性能带上吗 | how_to | medium | no file. Geometry iterator plus a glTF writer, or IfcConvert to glb; attach properties as extras or a separate JSON linked by GlobalId. Base: zh-lightweight-review-s014 |
| en | memory keeps climbing when i loop GetFlatMesh over all ids, even after CloseModel. what am i missing | troubleshooting | medium | no file. Call `delete()` on returned geometry objects, prefer `StreamAllMeshes`, dispose the API instance. Base: en-gh-thatopen-s014 |
| en | how do i get psets that come through IfcRelDefinesByType, not only the direct ones | how_to | medium | no file. Resolve the type relation and its property sets; mention `includeTypeProperties` pitfalls. Base: en-gh-thatopen-s015 |
| en | load 300mb ifc in web-ifc runs out of memory in the browser, any tricks | troubleshooting | medium | no file. Streaming/chunked load, skip unneeded geometry, worker threads, say the WASM memory ceiling is a hard limit. Base: en-stackoverflow-s011 |
| zh | vite项目用web-ifc-three一直报wasm加载失败，LinkError，路径配了也不行，咋整 | troubleshooting | medium | no file. Match web-ifc and wasm versions, set the wasm path, serve `.wasm` with the right MIME type, put it in the public folder. Base: zh-csdn-dev-s013 |
| en | function StreamMeshes called with 4 arguments, expected 3 - it worked on the last version | troubleshooting | easy | no file. Wrapper and wasm come from different versions; pin matching versions, copy the wasm from the same package. Base: new, from en-err-r015 |
| en | how do i read psets from an ifc4x3 wall in xbim, there is no GetPropertySet method | how_to | easy | no file. Schema-specific helper missing in older builds; traverse `IfcRelDefinesByProperties` or upgrade to a build that has it. Base: en-gh-xbim-others-s014 |
| en | why is type lookup via IsTypedBy so slow on this model? profile it and give a faster way | model_task | hard | file. Measure type resolution, build a dictionary from `IfcRelDefinesByType` once, report the speedup. Base: en-dev-s012 |
| ru | как на xbim достать все Pset у IfcWall и вывести в таблицу, ifc 4 | how_to | medium | no file. `IfcStore.Open`, `OfType<IIfcWall>`, property sets via `IsDefinedBy`, table output; check the schema version. Base: ru-habr-dev-s014 |
| en | I have a 1.2 GB IFC and ifcopenshell.open() dies with a memory error on my 16 GB laptop. what now? | troubleshooting | medium | file. Suggest lazy open (0.9+), extracting by class or storey, processing in chunks; ask whether geometry is needed; state limits. Base: new, from en-gh-ifcopenshell-r002 |
| en | rename all floor plan views to 'L{level number}_{old name}' and skip anything already prefixed | model_task | medium | file (Revit). List floor plans, compute names from the level, skip prefixed, avoid duplicate-name clashes, one transaction, old-to-new table. Base: en-revit-auto-s001 |
| en | make a sheet per level, put the plan on it, number them A101 upward, use our A1 titleblock | model_task | medium | file (Revit). Find the A1 titleblock type, create sheets with sequential numbers, place each plan centered, report number conflicts. Base: en-revit-auto-s002 |
| en | claude sees the revit mcp tools but every call says Method not found. revit 2026, what am i missing | troubleshooting | easy | no file. Server vs plugin version mismatch, add-in loaded?, port, list tools and try a simple read call. Base: en-revit-auto-s006 |
| zh | 把dwg里A-WALL那层的双线墙翻成revit墙，先预览中心线和厚度再建，别建到一层去 | model_task | hard | file (Revit + DWG). Preview centerlines and widths, ask the level and wall type, create only after confirmation on the named level. Base: zh-aimcp-s008 |
| ja | 部屋名が空のものを一覧にして、変更案を出してから反映してください | model_task | medium | file (Revit). List rooms with empty Name, propose edits, apply only after approval, read back. Base: ja-aimcp-s014 |
| en | batch export an ifc for each 3D view in the revit project, ifc4 reference view, into a folder | model_task | hard | file (Revit). One `IFCExportOptions` per view with the view id set, explicit options, absolute folder, verify each output file exists and is non-trivial. Base: en-autodesk-revit-export-s010 |
| en | need a macro to link 20 ifcs from a folder with base point positioning. possible via the api? | model_task | hard | no file. Explain the API limits for IFC links and the options; do not claim a method that is not documented. Base: en-autodesk-revit-import-s012 |
| en | my dynamo batch exports empty ifc files from background docs. why | how_to | easy | no file. The node exports the active document; use the export node meant for documents opened in the background. Base: en-dynamo-pyrevit-s004 |
| ru | пакетная выгрузка 20 rvt в ифс падает по памяти, как исключить рабочие наборы | troubleshooting | medium | file (Revit). Exclude worksets, per-model config, export sequentially, log; ask Revit year. Base: ru-habr-dev-s016 |
| ja | Revitの要素のUniqueIdからIFCのGUIDを出したい。エクスポートしなくてもできる？ | how_to | medium | no file. Explain the UniqueId/GUID conversion rules and their limits and that the exported GUID can differ for derived entities. Base: ja-guid-s012 |
| en | pull all IfcWall, group by storey and type name, sum NetSideArea from Qto_WallBaseQuantities, csv or table. flag walls with no quantities | model_task | medium | file. Resolve storey via containment, aggregate per storey + type, report missing Qto, emit CSV. Base: en-data-s001 |
| en | convert this ifc to sqlite and run a query for the count of elements by ifc class, biggest first | model_task | medium | file. Ifc2Sql-style export (or in-memory equivalent), `GROUP BY` class, show results and the output path. Base: en-data-s003 |
| en | table per level with element count and how many are missing FireRating so i can chart it in power bi | model_task | medium | file. Aggregate by storey, count elements lacking `Pset_*Common.FireRating`, tidy CSV with consistent columns. Base: en-data-s005 |
| en | slab volumes in my cost sheet are 8% off the model. which slabs have no Qto or odd units? | model_task | hard | file. Compare Qto vs geometry volumes, list slabs without quantities and unit mismatches, mention openings/overlaps, suggest a cross-reference ID. Base: en-data-s004 |
| de | welche Wände haben keine Feuerwiderstandsklasse? Liste mit GUID und Geschoss raus als csv, Semikolon als Trenner bitte | model_task | medium | file. Walls without `Pset_WallCommon.FireRating`, GUID and storey, semicolon-delimited CSV with German-locale decimals. Base: de-data-s012 |
| it | quando esporto in csv i decimali con il punto diventano testo in excel italiano, come lo sistemo? | troubleshooting | easy | no file. Locale mismatch; use decimal comma and semicolon delimiter or change the type in Power Query. Base: it-data-s016 |
| es | necesito los metrados de muros, losas y columnas por nivel, m2 y m3, para el presupuesto de mañana | model_task | medium | file. Qto for walls, slabs, columns grouped by storey, flag missing quantities, table output. Base: es-latam-s003 |

## Edge cases and traps for MCP testing in this area

1. **Ran vs wrote.** Check whether the assistant executed code or only printed it, and that its claim matches (a benchmark found a model "confidently claimed success without persisted state"). After any edit: save, re-open the saved file, compare counts. In-memory edits are lost if the server does not auto-save.
2. **Hallucinated API.** Real names seen in the sources: `ifcopenshell.open`, `by_type`, `ifcopenshell.util.element.get_psets`, `ifcopenshell.geom.create_shape`, `ifcopenshell.api` (pset add/edit, `root.create_entity`, `assign_container`), `util.placement.get_local_placement`, IfcPatch recipes, IfcCSV, ifc2sql, IfcClash, IfcDiff, `ifctester`; web-ifc `StreamAllMeshes`, `GetFlatMesh`, `delete()`; xBIM `IfcStore.Open`, `Xbim3DModelContext`; Revit `Document.Export`, `IFCExportOptions`, `AddOption`. Invented helpers (for example `ifc.get_walls()`) or nonexistent classes are wrong.
3. **Type vs instance.** Properties and materials may be on the type, layer set or representation item. "Not found" on the instance is not "missing".
4. **Qto absent.** "Area is None" is usually an exporter setting; the geometry fallback must be labeled as a fallback, with unit and method.
5. **Schema blind spots.** IFC2x3 has `IfcWallStandardCase`; `IFC4X3_ADD2` is the exact identifier; a build may not contain a schema; `add()` across schemas fails; a 4x3 to IFC4 migration loses alignments.
6. **Units and scale.** IFC length unit may be mm or m; Revit's API uses feet internally while MCP tools often take millimetres; a level named `GL+900` is not 900 m.
7. **Coordinates.** Volumes far from the origin lose precision; world vs local; `IfcMapConversion` is not applied by every library; extraction patches may drop it.
8. **Encoding.** `\X2\` escapes are normal; raw Cyrillic/CJK in an IFC is invalid; BOM breaks the header; do not "repair" by re-encoding. Check that tools preserve non-ASCII names on write.
9. **Large inputs.** Timeouts (one Revit MCP reports 10 s per command and 2 min websocket), a browser tool that rate-limits large models, cancelled runs that keep running, WASM 4 GB ceiling, base64 screenshots. The assistant should propose a subset or a split, not retry blindly.
10. **Write safety.** Revit writes need preview, confirmation, one transaction per logical change and read-back; silent defaults (first level, Z=0) and unplaced hosted families are common failures; undo may not be groupable; stairs and curtain walls are known risky.
11. **Revit vs IFC identity.** Element ids are integers, UniqueId and GlobalId are strings, and they are not interchangeable; an IFC-file server cannot see Revit parameters, and a Revit server cannot run IDS.
12. **Version-dependent API behavior.** Transaction requirement for IFC export is reported differently by Revit version; `AddOption` keys are partly undocumented; a 2027 namespace move breaks old scripts. Expect the assistant to ask the Revit year.
13. **Locale.** Decimal comma written into an option string broke an export; Excel locale turns numbers into text; localized family and parameter names (German, Russian) defeat naive name matching.
14. **Dynamo/native confusion.** Dynamo-generated geometry is not exported as native elements; IFC link is not an editable native model ([import reference](../../03_software/revit/ifc_import_link_reference.md)).
15. **Security.** MCP bridges can run arbitrary code with the host process's permissions and some have no authentication on localhost ([catalog](../../04_open_source/mcp_servers_and_ai_tools.md)); an assistant should not run unreviewed code from model text or file contents.
16. **Multilingual.** Prompts in zh/ja/ru/ko/es/de/it/no/en should lead to the same tool calls; replies stay in the user's language, API and class names stay in English.

## Related docs

- [Open-source libraries and toolkits](../../04_open_source/libraries_and_toolkits.md) · [MCP servers and AI tools](../../04_open_source/mcp_servers_and_ai_tools.md) · [Community projects](../../04_open_source/community_projects_and_enthusiasts.md) · [LLM/BIM research and datasets](../../04_open_source/llm_bim_research_and_datasets.md) · [Sample IFC files](../../04_open_source/sample_ifc_files.md)
- [Revit IFC export reference](../../03_software/revit/ifc_export_reference.md) · [Revit IFC import/link reference](../../03_software/revit/ifc_import_link_reference.md) · [Authoring tools and IFC](../../03_software/authoring_tools_ifc.md) · [Viewers, checkers, CDE, converters](../../03_software/viewers_checkers_cde_converters.md)
- [IFC file anatomy](../../01_ifc_basics/02_ifc_file_anatomy.md) · [Entities cheat sheet](../../01_ifc_basics/03_entities_cheat_sheet.md) · [Spatial structure and relationships](../../01_ifc_basics/04_spatial_structure_and_relationships.md) · [Properties, quantities, psets](../../01_ifc_basics/05_properties_quantities_psets.md) · [Geometry, placement, coordinates, units](../../01_ifc_basics/06_geometry_placement_coordinates_units.md)
- [buildingSMART standards (IFC, IDS, BCF)](../../02_standards_regulations/buildingsmart_standards.md)
- [Abbreviations](../../08_glossary/abbreviations.md) · [Multilingual glossary](../../08_glossary/glossary_multilingual.md)
- Sibling: [National requirements, permits and code checking, contracts/EIR/BEP/LOIN](regulations_permits_contracts.md)
