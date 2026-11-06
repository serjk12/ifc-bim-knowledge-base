# File size and performance, viewing IFC, converting formats

Vocabulary topics covered: `file_size_performance`, `viewers_opening`, `conversion_formats`.
Built from the wave-1 research data (`research_raw/wave1/...`) with `tools/kb.py`; reference facts come from the docs linked below.

## In plain words

An IFC file is plain text: one line per fact about the building. A big project easily becomes hundreds of megabytes, and a few people report 1-2 GB. Opening it is then a different job from *reading* it: a program can count walls in a big file quite fast, but drawing the geometry (turning every curve and opening into triangles) needs far more memory than the file size, and a web browser has a hard ceiling of about 4 GB for the WebAssembly engines most web viewers use. That is why the same file "opens fine" in one program, takes ten minutes in another and crashes a third.

Three families of questions appear again and again:

1. **"My IFC is huge or slow."** Why is it so big (tessellated geometry, repeated geometry, rebar sets, insulation, ports), what can be left out, and how to open it at all. See [Inside an .ifc file](../../01_ifc_basics/02_ifc_file_anatomy.md) (ifcZIP, ifcXML sizes) and [Geometry, placement, coordinates, units](../../01_ifc_basics/06_geometry_placement_coordinates_units.md) (parametric vs tessellated vs B-rep).
2. **"I cannot see it / it looks different here."** Which free viewer to use without Revit, why a model is blank, why walls lose their holes, colours go white, or elements are missing. Different viewers make different choices, so one viewer is not proof. See [Viewers, checkers, CDE and converters](../../03_software/viewers_checkers_cde_converters.md).
3. **"Turn it into something else."** IFC to glTF/GLB/OBJ/3D Tiles for the web, to DWG/DXF/SVG for drawings, to GIS, to another IFC version, to Excel or a database, or a lighter or subset copy. Conversion nearly always loses meaning (properties, hierarchy, colours) or changes scale and position. See the [converter map](../../03_software/viewers_checkers_cde_converters.md) and [IFC versions and views](../../01_ifc_basics/01_what_is_ifc_and_versions.md).

For an MCP tester: the right behaviour is to profile first (size, entity counts per class, heavy representation types, schema, units, bounding box), recommend the cheapest fix, and never claim a result the tool did not produce. Writing a "light copy" must keep the original untouched and say what was removed.

**Data caveats.** After removing duplicates there are 402 real records (lang: en 297, zh 56, ru 21, ja 11, es 6, de 4, it 2, and one each of tr, sk, pt, ko, fr) from about 350 distinct source URLs. A very large share comes from GitHub issue trackers of IfcOpenShell/Bonsai, That Open (web-ifc, fragments, components), xBIM and Autodesk revit-ifc, so developers and library users are over-represented compared with site engineers and architects. Chinese material is strongest on "BIM lightweighting" (轻量化) blog posts; Russian and Japanese on forum, Qiita and Zenn posts. Many tracker records are title-only. Frequency numbers are keyword-cluster counts, approximate, with overlaps. Records are paraphrases, not copies.

## Problem map

Ranked by frequency in the data (approximate records / distinct source URLs, main languages).

| # | Problem | How users describe it | Frequency signal | Root cause | Typical fix |
|---|---|---|---|---|---|
| 1 | Desktop viewer or library is slow, hangs or runs out of memory on a big IFC | "Blender hangs loading an IFC", "780 MB eats 340 GB RAM", "15 MB file takes 5 minutes", "IfcOpenShell 2 GB out of memory" | ~90 rec / ~80 URLs; mostly en, some zh, ja, de | Full parse of every instance; geometry creation (booleans, B-rep with huge face counts, mapped items); memory held until close | Lazy open (IfcOpenShell 0.9), exclude heavy classes, filter/extract a subset, 64-bit and more RAM, other viewer |
| 2 | IFC too big for a browser / WebAssembly viewer | "program aborts on 300k components", "2 GB+ models fail inside wasm", "Out of memory in Chrome with a 33 MB file" | ~60 rec / ~50 URLs; en, zh, ja, ru | WASM32 memory ceiling (~4 GiB); merged-geometry demos; main-thread blocking; version mismatch of wrapper and wasm | Convert on the server (IFC to fragments/glTF), stream tiles, split by storey, pin matching library versions |
| 3 | "Why is my IFC so big?" / make it lighter | "100 MB Revit model becomes a 1 GB IFC", "720 MB because of pipe insulation", "rebar sets exported bar by bar", "BIM轻量化" | ~35 rec / ~30 URLs; zh strong (19), en | Tessellated or faceted geometry, repeated geometry not instanced, rebar sets, insulation, ports, duplicated types, long property sets | Zip (`.ifczip`), export fewer classes/views, Reference View, tune exporter options, post-process (patch/optimise), strip unused data |
| 4 | Revit IFC export is slow, hangs or fails | "export hangs 12 hours", "File is too large to export", "unrecoverable error ... Current View Only", "crashes at every export" | ~29 rec / ~22 URLs; en, zh, ru | Dense families (trusses, insulation), property reading, workshared models, add-in conflicts | Export current view or per level, simplify heavy families, split model, disable conflicting add-ins, update exporter |
| 5 | Viewer shows less than the file contains, or different from another viewer | "walls missing in Bonsai but fine in Solibri", "Opening cuts skipped", "white model", "tiny dot, nothing visible", "IfcSpace box above the roof" | ~40 rec / ~35 URLs; mostly en, zh | Viewer choices: voids limit, uncontained elements hidden, flipped normals, spaces drawn, no surface styles, coordinates far away, analytical members hidden | Check the file (containment, voids, styles, bounding box), toggle viewer options, compare in a second viewer |
| 6 | File will not open at all (invalid, truncated, unsupported schema/geometry) | "Out of table cursors", "TriangulateBounds Expected outer bound", "IFC4 not rendered but 2x3 is", "LLM-written IFC will not open", "Cyrillic path" | ~45 rec / ~38 URLs; en, ru, zh | Invalid STEP (encoding, header, missing attributes), unsupported entity types (e.g. IfcPolygonalFaceSet in older engines), tool version gaps | Validate, fix or re-export; try IFC2x3 or another viewer; update tool; ASCII-safe names |
| 7 | Colours, materials and transparency lost | "all geometry white", "mtl has no materials", "IFC4 loses colours vs 2x3", "FBX loses materials" | ~26 rec / ~24 URLs; en, zh | Colour is an `IfcStyledItem`/surface style on geometry; some exports have none; OBJ/GLB/FBX map materials differently | Check styles in the file, pick exporter option, map materials afterwards |
| 8 | IFC to glTF / GLB / OBJ / FBX / 3D Tiles for web, Unity, dashboards | "convert IFC to glTF but keep GlobalId", "components merged, expressID lost", "grey materials in Unity" | ~70 rec / ~64 URLs; en 45, zh 19 | Conversions keep geometry, not semantics; merging; unit and origin differences | IfcConvert/web-ifc plus a separate metadata JSON keyed by GlobalId; split by storey; explicit material map |
| 9 | Units, scale and position wrong after conversion | "STEP model 1000x too big", "IFC to GeoPackage lands in the ocean", "origin offset" | ~20 rec / ~19 URLs; en, zh, es | Millimetre vs metre; ignored `IfcMapConversion`; false origin; site vs building local placement | Read units and map conversion first; set converter placement options; shift to a false origin |
| 10 | IFC to GIS / CityGML / 3D Tiles / QGIS | "how to optimise IFC to GIS", "IFC to CityGML for Cesium", "CityGML has no colour in Cesium ion" | ~21 rec / ~20 URLs; en, zh, de, ja | Different data model (solids vs surfaces/LoD), CRS, units | Envelope extraction or converters (FME, ifc2gis, Cesium ion tiler), check CRS and units |
| 11 | IFC to or from DWG / DXF / SVG / PDF | "how to turn IFC into DWG", "floor plans as SVG", "DWG to IFC", "layers by IFC class" | ~23 rec / ~23 URLs; en, ru, it, zh | IFC has 3D objects; 2D needs section/projection and layer mapping; DWG has no BIM semantics | Generate plans/sections in a BIM tool or IfcConvert SVG; map classes to layers; expect limited DWG to IFC |
| 12 | Subset, split, light copy ("only walls and slabs", "save selected") | "export only selected elements", "one OBJ per level", "light version for site tablet" | ~37 rec / ~34 URLs; en, zh | Tools lack a simple "save selection"; per-element deletion is slow | Extract-by-class/storey recipes (ifcpatch), export filtered, keep GlobalIds |
| 13 | Which viewer to use / open IFC without Revit | "free IFC viewer with properties", "open IFC online without installing", "Mac viewer" | ~32 rec / ~30 URLs; en, zh, ja, ru, es, de | No authoring licence; privacy concern of uploads | Free desktop viewers, browser viewers, a neutral cross-check viewer |
| 14 | IFC version conversion (2x3, 4, 4.3) | "2x3 to 4 converter", "upgrade IFC4 to 4.3 to use IfcRoad", "IFC4 not opened but 2x3 is" | ~14 rec / ~13 URLs; en, zh | Different schemas and views; no lossless converter; viewer support lags | Re-export from source in the right version; upgrade tools with class reassignment; test the receiver |
| 15 | IFC to Excel / CSV / SQLite / database / COBie | "extract values without opening the model", "IFC stored as SQLite", "COBie tabs missing" | ~13 rec / ~13 URLs; en, ja | Properties are relations, not tables | IfcOpenShell scripts, Ifc2Sql, BIMvision reports, ETL (DuckDB/Parquet) |

## Problems in depth

### 1. Desktop viewer or library is slow, hangs or runs out of memory

**Symptoms.**
- EN: "Sample IFCs of 10-350 MB freeze Bonsai on open although BIMcollab opens them slowly" - the reporter found one handwash basin held half of all polygons ([IfcOpenShell #7632](https://github.com/IfcOpenShell/IfcOpenShell/issues/7632)).
- EN: "A 780 MB IFC eats 340 GB RAM in Bonsai and never loads, while the ODA viewer opens it with 12 GB" ([#9826](https://github.com/IfcOpenShell/IfcOpenShell/issues/9826)).
- EN: "2 GB federated 4D IFC runs out of RAM on 16 GB when opened; what strategies exist?" ([#2025](https://github.com/IfcOpenShell/IfcOpenShell/issues/2025)).
- EN: "One IFC loads in 25 s in Open IFC Viewer but 5 min in Bonsai Viewer" ([#9055](https://github.com/IfcOpenShell/IfcOpenShell/issues/9055)).
- JA: "大きいIFCを開くと全インスタンス・属性を先にパースして遅くメモリを食う" (opening a huge IFC parses everything first; slow and memory-hungry) - answer: IfcOpenShell 0.9 `lazy=True`, 392 MB from 11.3 s to 1.4 s, memory about 3 GB down to about 1 GB ([Qiita](https://qiita.com/kiyuka/items/0d2ef739a0d34606a52f)).
- EN: "Why does buildingSMART certification not require speed? Benchmarks show some tools need hours for a 240 MB IFC" - answer: speed is not a certification criterion ([forum](https://forums.buildingsmart.org/t/processing-speed-ifc-imports/2622)).

**Why.** Reading the file is cheap compared with building geometry. Time and memory are dominated by a few heavy items (faceted B-reps, face-based surface models, many openings/booleans, thousands of fasteners), by memory that is not released until the model is closed, and by how many threads run the geometry iterator ([#6026](https://github.com/IfcOpenShell/IfcOpenShell/issues/6026), [#6905](https://github.com/IfcOpenShell/IfcOpenShell/issues/6905)).

**What fixes it.** Open lazily or without geometry for counting; exclude heavy classes in the viewer's advanced open; extract a subset; fewer threads; more RAM; try another viewer; ask the sender for a lighter export.

**Good assistant behaviour.**
- Never try to build geometry for the whole file just to answer a counting question. Count by class first, then rank by representation type and face count.
- Report time, size, number of entities, top heavy classes. Offer a filtered copy, not a promise to "optimise".
- Clarifying questions: "File size and IFC version?", "Which program freezes (Bonsai, BIMcollab, Solibri, web)?", "How much RAM and which OS?", "Do you need geometry, or only data?"

### 2. Too big for a browser / WebAssembly viewer

**Symptoms.**
- EN: "Program aborts on a model with about 300,000 components" ([web-ifc #538](https://github.com/ThatOpen/engine_web-ifc/issues/538)); "Models of about 2 GB or larger fail inside the wasm module" ([#419](https://github.com/ThatOpen/engine_web-ifc/issues/419)); "400 MB+ Revit IFC4 MEP models: memory access out of bounds in GetFlatMesh" ([#1999](https://github.com/ThatOpen/engine_web-ifc/issues/1999)).
- EN: "A 1.3 GB IFC crashes the viewer though it works in APS Viewer; 300 GB of models planned" - answer: convert to fragments in the backend ([fragments #129](https://github.com/ThatOpen/engine_fragment/issues/129)); "IfcImporter aborts on IFC larger than 2 GB: WASM32 ceiling" ([#258](https://github.com/ThatOpen/engine_fragment/issues/258)).
- EN: "A 33 MB IFC causes Out of memory in Chrome" ([components #458](https://github.com/ThatOpen/engine_components/issues/458)).
- ZH: "大型 BIM 模型在 Web 端为什么这么卡" (why large BIM models lag in the browser) - parsing blocks the main thread, too many draw calls, merged geometry loses component identity ([Juejin](https://juejin.cn/post/7698926562423357450)).
- RU (synthetic): "web-ifc на 300мб файле вешает вкладку, как грузить кусками / в воркере".

**Why.** The WebAssembly engines are 32-bit (about 4 GiB heap); chunked input does not help until a 64-bit build exists. Maintainers state that the same indexing done in C++ handles a 4 GB file in under two minutes, so slow browser indexing is a JavaScript cost ([#1816](https://github.com/ThatOpen/engine_web-ifc/issues/1816)). Wrapper and wasm versions must match (BindingError reports).

**What fixes it.** Server-side conversion to a streaming format (fragments, glTF, XKT), split by storey or discipline, web workers, keep a viewer-ready copy separate from the IFC. See the [viewer toolkits](../../03_software/viewers_checkers_cde_converters.md).

**Good assistant behaviour.** Given a file, report size, entity count and a rough "will it fit" judgement; say clearly that the 4 GB figure is a ceiling of the engine, not of the file format. Ask which library and version, browser or Node, and whether the user can convert server-side.

### 3. "Why is my IFC so big?" and making it lighter

**Symptoms.**
- ZH: "IFC比rvt大很多，轻量化怎么做" - a 100 MB Revit model exports to a 1 GB IFC and 3 GB OBJ ([cnblogs](https://www.cnblogs.com/nihaozhe/articles/13651935.html), [CSDN](https://blog.csdn.net/nihaozhe/article/details/108704151)).
- EN: "Pipe insulation geometry is 1749 faces at all detail levels; export takes hours and 720 MB" ([revit-ifc #892](https://github.com/Autodesk/revit-ifc/issues/892)); "Revit exports every bar of a rebar set as a separate IfcReinforcingBar" ([#76](https://github.com/Autodesk/revit-ifc/issues/76)); "option to not export IfcDistributionPort" ([#630](https://github.com/Autodesk/revit-ifc/issues/630)).
- EN: "Decimating a wall in Bonsai does not persist; how to cut IFC file size?" - decimate works only on tessellated geometry; overly detailed doors and furniture are the usual culprit ([OSArch](https://community.osarch.org/discussion/comment/23266)).
- EN: "ifcpatch Optimise cut file size 60% on small files but takes half an hour and 20 GB RAM on a 500 MB file" ([#1603](https://github.com/IfcOpenShell/IfcOpenShell/issues/1603)).
- EN: manufacturer geometry with engraved logos and finely triangulated pipes ([forum](https://forums.buildingsmart.org/t/4699)).

**Why.** Cost comes from geometry representation (parametric extrusions are tiny, tessellated and faceted surfaces are large), repeated geometry that is not shared through mapped items, per-bar rebar, insulation and ports, and thousands of tiny parts. Packaging helps a lot: vendor figures say ifcZIP shrinks `.ifc` by about 60-80% and ifcXML is roughly 300-400% larger than `.ifc` ([file anatomy](../../01_ifc_basics/02_ifc_file_anatomy.md)); one Chinese source says IFCZIP is small but not openable in Revit, while the [file anatomy doc](../../01_ifc_basics/02_ifc_file_anatomy.md) lists `.ifcZIP` among the types Revit opens, so test the receiving program before relying on it.

**What fixes it.** Zip it; export only what is needed (class/view/level filters); change exporter options; use Reference View/tessellation where acceptable; post-process (extract, optimise); agree LOD in the BEP.

**Good assistant behaviour.** Rank classes by instance count and by estimated bytes, list the top heavy elements (face counts), check for `IfcMappedItem` use, and propose removals as options with their cost (for example "removing IfcReinforcingBar drops X MB but loses rebar for take-off"). Offer to produce a copy; never delete in place.
Clarifying questions: "Is the file for viewing, take-off, clash or handover?", "Which classes must stay?", "Must GlobalIds and property sets be preserved?"

### 4. Revit IFC export is slow, hangs or fails

**Symptoms.**
- EN: "IFC export hangs for 12+ hours" - trusses and dense families; lower LOD, split the model, find the stalling element in the journal ([Autodesk forum](https://forums.autodesk.com/t5/revit-structure-forum/export-to-ifc-is-not-working-the-revit-file-stays-not-responding/td-p/9912833)).
- EN: "Revit 2022 IFC export fails with File is too large to export" ([#458](https://github.com/Autodesk/revit-ifc/issues/458)); "Unrecoverable error during export ... Try using filters and Current View Only mode" ([#1021](https://github.com/Autodesk/revit-ifc/issues/1021)); "600 MB project crashes Revit on IFC export" ([#88](https://github.com/Autodesk/revit-ifc/issues/88)).
- EN: "Exporting with properties is extremely slow" - property reading through the API is the bottleneck ([#492](https://github.com/Autodesk/revit-ifc/issues/492)); "Exporter should degrade or skip slow objects and report what it did" ([#831](https://github.com/Autodesk/revit-ifc/issues/831)).
- RU (synthetic): "ревит экспорт в ifc висит уже 3 часа, 500 мб rvt, что отключить чтоб побыстрее?"

**Why.** The exporter has to read every parameter and build geometry for heavy families; some objects fail validation; add-in conflicts and workshared models add failures. See the [Revit IFC export reference](../../03_software/revit/ifc_export_reference.md).

**What fixes it.** Export the current view or by level; filter categories; drop 2D elements, linked files, base quantities, and heavy families; update the exporter; remove conflicting add-ins.

**Good assistant behaviour.** Ask Revit and exporter version, workshared or not, model size, what the journal says, and what is needed from the export. Do not claim a specific hidden "fast mode" exists.

### 5. Viewer shows less than the file contains, or differs between viewers

**Symptoms.**
- EN: "Masonry around windows (lintels, sills) is visible in Solibri but missing in Bonsai" - 324 elements without spatial containment went to a hidden Unsorted collection ([#9372](https://github.com/IfcOpenShell/IfcOpenShell/issues/9372)).
- EN: "Opening Cuts Skipped warning when opening Revit and Archicad IFCs; Apply Openings fixes it" - void limit setting ([OSArch](https://community.osarch.org/discussion/3754/opening-cuts-skipped-in-bonsai-studio-0-9)).
- ES: "al abrir un archivo IFC (2x3) se pierde parte de la información geométrica" - actually flipped face normals; Blender draws double-sided, the viewer single-sided ([#8131](https://github.com/IfcOpenShell/IfcOpenShell/issues/8131)).
- EN: "One IfcSpace (\"4 - Roof\") renders as a large solid box in That Open app but not in Dalux or BIMvision" ([fragments #301](https://github.com/ThatOpen/engine_fragment/issues/301)).
- EN: "All geometry renders white though BIMvision shows colours" - the files contained no surface styles ([components #745](https://github.com/ThatOpen/engine_components/issues/745)).
- EN: "ETABS structural analysis view export shows nothing in Solibri or BIMsight" ([forum](https://forums.buildingsmart.org/t/ifc-structural-analysis-view/1267)).
- EN: "Wall missing in Bonsai compared to other viewers" ([#8026](https://github.com/IfcOpenShell/IfcOpenShell/issues/8026)).

**Why.** Each viewer decides how to draw spaces and openings, which elements to show when containment is missing, how to treat booleans, normals and styles. "Different from viewer X" is not the same as "wrong file".

**Good assistant behaviour.** Check the file for facts: every product contained in a storey? voids present (`IfcRelVoidsElement`)? representations in the Plan context only? styles present? bounding box and units? Then explain the likely viewer-side reason. Ask which two viewers disagree and which version of each.

### 6. File will not open at all

**Symptoms.**
- EN: "Basic MEP IFC file cannot be opened" - made by an LLM for testing; header says generated by OpenAI; IfcProject has 8 attributes instead of 9; answer: not a Bonsai bug, run the buildingSMART validation service ([#7945](https://github.com/IfcOpenShell/IfcOpenShell/issues/7945)).
- EN: "BIMserver can't render IFC4 RV from ArchiCAD 23, same project in IFC2X3 displays fine" - IfcPolygonalFaceSet unsupported ([#1103](https://github.com/opensourceBIM/BIMserver/issues/1103)); "After the Revit IFC exporter update, Navisworks IFC Modern can no longer load IFC2x3; IFC4 works" ([#580](https://github.com/Autodesk/revit-ifc/issues/580)).
- EN: "xBIM throws Out of table cursors when processing IFC files over 100-150 MB" ([#551](https://github.com/xBimTeam/XbimEssentials/issues/551)); "Demo page crashes on a 130 MB IFC with TriangulateBounds Expected outer bound" ([#1326](https://github.com/ThatOpen/engine_web-ifc/issues/1326)).
- EN: "Special unicode characters in the name of an IfcWall cause no geometry in Xbim Xplorer" ([#512](https://github.com/xBimTeam/XbimEssentials/issues/512)); property string with a line break inside a Cyrillic escape ([#660](https://github.com/xBimTeam/XbimEssentials/issues/660)).
- EN: "how can I tell whether a file is IFC2x3 or IFC4? File properties show nothing" - read `FILE_SCHEMA` in the header, unzip `.ifczip` first ([forum](https://forums.buildingsmart.org/t/4802)).
- RU: "IFC из Сапфира в автокад не импортируется, системная ошибка, в BimSight открывается нормально" ([forum.dwg.ru](https://forum.dwg.ru/showthread.php?t=160240)).

**Why.** Invalid STEP syntax, unsupported entities in older engines, non-ASCII text not escaped, memory limits, tool version differences.

**Good assistant behaviour.** Read the header (`FILE_SCHEMA`, application), check the end of file, validate, look for suspicious bytes, then say whether it is the file or the tool. Offer re-export in IFC2x3 as a test.

### 7. Colours, materials and transparency lost

**Symptoms.**
- EN: "IFC4 export from Revit renders grey in a web viewer while IFC2x3 is coloured" ([web-ifc #1793](https://github.com/ThatOpen/engine_web-ifc/issues/1793)).
- EN: "material info present in IFC and XML export but not in .mtl on OBJ export" ([#4846](https://github.com/IfcOpenShell/IfcOpenShell/issues/4846)); "IFCINDEXEDCOLOURMAP not implemented - colours missing after IFC to GLB" ([#2824](https://github.com/IfcOpenShell/IfcOpenShell/issues/2824)).
- ZH: "Revit转fbx丢失材质问题" ([Bilibili](https://www.bilibili.com/read/cv18398331/)); "rvt和ifc什么关系，导成ifc颜色为什么变了" ([Zhihu](https://www.zhihu.com/question/49455994)).
- EN: "Why is it so difficult to get colors to show up?" - colour or transparency via IfcStyledItem shows in some viewers and not others ([forum](https://forums.buildingsmart.org/t/why-is-it-so-difficult-to-get-colors-to-show-up/2312)).

**Why.** In IFC colour is a style attached to the shape or the material; exporters, viewers and converters read different places. OBJ/GLB/FBX map materials differently. See [Materials, classification, types, styles](../../01_ifc_basics/07_materials_classification_types_styles.md).

**Good assistant behaviour.** Inspect style assignment (representation vs material), report if styles exist at all, then explain. Ask the target format and viewer.

### 8. IFC to glTF / GLB / OBJ / FBX / 3D Tiles ("lightweighting")

**Symptoms.**
- ZH: "IfcConvert 会合并构件、丢 expressID，要额外写入 GlobalId 才能和属性表关联；材质全变灰；毫米和米单位导致放大1000倍；IFC原点和项目基点不一致" ([Juejin](https://juejin.cn/post/7691297274821705728)).
- ZH: "转glTF保留属性与几何一一对应" ([Zhihu](https://zhuanlan.zhihu.com/p/2021897410683650709)); "IFC到底怎么轻量化" series ([Zhihu](https://www.zhihu.com/question/385964946)).
- JA: "IFCをglTFにして階層構造(Project>Site>Building>階>要素)も残したい。IfcOpenShellは遅い" - own converter with pygltflib; web-ifc about 30x faster but glTF export unsolved ([Zenn](https://zenn.dev/kiyuka/scraps/a054a249f42a93)).
- EN: "GLB output grew after upgrading from 0.7 to 0.8" - regression in style identity handling ([#5486](https://github.com/IfcOpenShell/IfcOpenShell/issues/5486)); "IFC to GLB conversion hangs 12+ hours on steel pylon model" - a plate had 181 voids ([#4247](https://github.com/IfcOpenShell/IfcOpenShell/issues/4247)).
- ZH: "100M的模型导出IFC有1GB，转OBJ变3GB，机器卡死" ([CSDN](https://blog.csdn.net/nihaozhe/article/details/108704151)).

**Why / fix.** Meshes carry geometry; properties live elsewhere. A good pipeline converts geometry (IfcConvert or web-ifc), exports properties to a JSON keyed by GlobalId, splits by storey, adds LOD and picking structures, and keeps an explicit unit and origin policy.

**Good assistant behaviour.** Ask "what will consume the result (browser, Unity, GIS, dashboard)", whether properties and element identity must survive, and what size budget exists. After conversion report element count, size before and after, and what was dropped.

### 9. Units, scale and position wrong after conversion

**Symptoms.** EN: "Exporting IFC to STEP with IfcConvert gives a model 1000x too large whatever --length-unit is set to" ([OSArch](https://community.osarch.org/discussion/2781/ifcconvert-how-to-control-the-resulting-step-models-scale)). EN: "EPSG:27700 coordinates set in Bonsai, ifc2gis output loads in the wrong place" - m vs mm mismatch and a web-ifc bug ignoring `IfcMapConversion` ([OSArch](https://community.osarch.org/discussion/3037/ifc-to-qgis-geopackage)). ZH: BIM没有地理坐标，需要原点经纬度加xyz旋转角度 ([CSDN](https://blog.csdn.net/liyan_gis/article/details/100132931)). EN: IfcConvert breaks positioning with `--site-local-placement` ([#6102](https://github.com/IfcOpenShell/IfcOpenShell/issues/6102)).

**Why.** Unit assignment of the IFC, missing or ignored map conversion, local placement options, a false origin. See [Geometry, placement, coordinates, units](../../01_ifc_basics/06_geometry_placement_coordinates_units.md).

**Good assistant behaviour.** Read `IfcUnitAssignment`, `IfcMapConversion`/`IfcProjectedCRS`, `IfcSite` placement, and the bounding box; give corrected numbers; state which converter option changes what.

### 10. IFC to GIS, CityGML, 3D Tiles

**Symptoms.** EN: "I want to optimize the workflow for transferring geometry and information from IFC to the GIS" - replies: ArcGIS tools, OGC IFC/GML paper, TU Delft envelope extractor, ifc2gis; georeferencing is key ([forum](https://forums.buildingsmart.org/t/ifc-to-gis/6115)). EN: "mago-3d-tiler loads 0 files from the official AC20-FZK-Haus sample" - the library used does not fully support IFC4 ([issue](https://github.com/Gaia3D/mago-3d-tiler/issues/79)). EN: "CityGML has no colour after uploading to Cesium ion" - app:theme tag from FME ([Cesium](https://community.cesium.com/t/citygml-has-no-color-after-uploading-to-cesium-ion/31018)). ZH: GISBox 3D Tiles conversion with a base reference point ([CSDN](https://blog.csdn.net/GISBox/article/details/149612800)). JA: PLATEAU CityGML in ArcGIS ([Qiita](https://qiita.com/masumur/items/8362a1ed91048e26ed2a)).

**Why / fix.** GIS wants envelopes and LoD surfaces, not detailed solids; check CRS and units; use a converter that supports the schema; derive the envelope for CityGML.

**Good assistant behaviour.** Ask target (CityGML LoD, GeoPackage, 3D Tiles), CRS, and whether interior detail is needed; check units and map conversion before conversion.

### 11. IFC to and from DWG, DXF, SVG and PDF

**Symptoms.**
- RU: "как перевести ifc в dwg и какими программами, работаю в Архикаде" ([forum.dwg.ru](https://forum.dwg.ru/showthread.php?t=96356)); "нужны тела DWG Solid а не сетки" ([forum.dwg.ru](https://forum.dwg.ru/showthread.php?t=75883)).
- IT: "dall'IFC come estraggo piante e sezioni in DXF?" ([ACCA Biblus](https://biblus.acca.it/una-guida-completa-per-convertire-file-ifc-in-dxf/)); "ho solo il DWG, come lo converto in IFC?" ([ACCA Biblus](https://biblus.acca.it/come-convertire-un-file-dwg-in-ifc-in-modo-semplice/)).
- EN: "need to deliver IFC plus DXF/DWG; in Revit there is a layer translation table, can Bonsai do that?" ([#8009](https://github.com/IfcOpenShell/IfcOpenShell/issues/8009)); "How do I turn a 30-storey IFC into 2D SVG floor plans with IfcConvert?" ([#585](https://github.com/IfcOpenShell/IfcOpenShell/issues/585)); "how can I export DWG to IFC4 by IfcOpenShell" - answer: BIM data is not just a 3D format; use DXF and the dxf2ifc script ([#3124](https://github.com/IfcOpenShell/IfcOpenShell/issues/3124)).

**Why.** Plans, sections and elevations are views generated from the 3D model, with a layer mapping decision. DWG to IFC creates geometry without semantics.

**Good assistant behaviour.** Ask which level/section, desired layer scheme, and the CAD version; say what will not be produced (hatches, annotation, 3D PDF).

### 12. Subset, split, "light copy"

**Symptoms.** EN: "Wants to export only selected elements to a new IFC to share a slice with a client" - exists as Extract Elements in Bonsai Quality Control > Patch ([#6118](https://github.com/IfcOpenShell/IfcOpenShell/issues/6118)); "ExtractElements is extremely slow for a 9,289-element selection" ([#9247](https://github.com/IfcOpenShell/IfcOpenShell/issues/9247)); "Can IfcConvert split a model into one OBJ per building level?" ([OSArch](https://community.osarch.org/discussion/2726/export-obj-per-level-using-ifcconvert)); "Deleting 1000 of 20k elements takes over 10 minutes" ([OSArch](https://community.osarch.org/discussion/2673/deleting-many-objects-takes-forever)); "Export linked .rvt in a single IFC file" ([#439](https://github.com/Autodesk/revit-ifc/issues/439)). ZH (synthetic): "这个ifc有800多M，网页里卡死了，帮我按楼层拆成几个小文件".

**Why / fix.** Per-element deletion is slow; extraction by class, storey or selection is the right operation, and it must keep spatial structure, types, materials and relationships consistent.

**Good assistant behaviour.** Make a new file, preserve GlobalIds, report counts and size before/after, list what was dropped (and relationships that became dangling), and verify by reopening.

### 13. Which viewer, and how to open IFC without Revit

**Symptoms.** ZH: "求推荐好用方便的IFC查看工具" - BIM Vision, BIMSee ([Zhihu](https://www.zhihu.com/question/583830829)); "想不装软件在线打开IFC文件" ([Zhihu](https://zhuanlan.zhihu.com/p/651323857)). DE: "Die populärsten IFC Viewer" - keep one vendor-neutral viewer for cross-checks ([BIM me up](https://bim-me-up.com/die-popularsten-ifc-viewer/)). JA: small MEP office needs to see architect IFC for free ([note](https://note.com/limber_stork5044/n/n68df8d5a268b)). RU: "Как корректно открыть IFC" - first check the file in a free viewer ([forum.dwg.ru](https://forum.dwg.ru/showthread.php?t=154396)). EN: IFC viewer for site staff who cannot install multi-GB software ([Zenn](https://zenn.dev/kazuyamaeda/articles/97933cdafce6d8)).

**Good assistant behaviour.** Suggest options by constraint (no install, Mac, properties, large files), warn that uploading confidential models to an online viewer is a privacy decision, and offer to give a data summary instead. Do not invent prices or licences.

### 14. IFC version conversion

**Symptoms.** EN: "I have an IFC2x3 from Revit but no Revit; can I upgrade it to IFC4?" ([forum](https://forums.buildingsmart.org/t/convert-upgrade-ifc2x3-to-ifc4/5210)); "How do I convert an IFC2x3 file to IFC4?" - no off-the-shelf conversion ([xBIM #645](https://github.com/xBimTeam/XbimEssentials/issues/645)); "Upgrading IFC4 into IFC4.3 to use IfcRoad" ([#4921](https://github.com/IfcOpenShell/IfcOpenShell/issues/4921)). ZH: "revit低版本的模型能在高版本打开吗" - export IFC2x3 for an older Revit ([Zhulong](https://www.zhulong.com/zt_bim_3002296/detail42826395/)). EN: "Is the industry ready for IFC4?" - stay on IFC2x3 when building from models ([BIM Corner](https://bimcorner.com/is-the-industry-ready-for-ifc4/)).

**Good assistant behaviour.** Read the schema and view from the header, list entities that do not exist in the target schema, convert a copy, and list what changed. Recommend IFC2x3 Coordination View 2.0 only as the compatibility default.

### 15. IFC to Excel, SQL, databases and COBie

**Symptoms.** JA: "協力会社の重いモデルや古いモデルを開かずに値だけ取り出したい" - ETL to a columnar store ([Zenn](https://zenn.dev/tomosandego/articles/59e6cf8dfe60bc)). EN: IFC stored as SQLite/MySQL - load time 28 s down to 4.6 s ([OSArch](https://community.osarch.org/discussion/1535/ifc-stored-as-sqlite-and-mysql)); "how to open .ifcsqlite files?" ([#4920](https://github.com/IfcOpenShell/IfcOpenShell/issues/4920)); COBie export missing five of 20 tabs ([#5926](https://github.com/IfcOpenShell/IfcOpenShell/issues/5926)).

**Good assistant behaviour.** Confirm what a row should be (one per element, type or space), pick properties and quantities, flag missing values, and give the output path and counts.

## Real questions

Paraphrased questions from the dataset (original-language paraphrase, English gloss, persona, source). A trailing "*" (de*, fr*, tr*) means the source is non-English but the dataset stores the paraphrase in English.

| lang | question (original-language paraphrase) | EN gloss | persona | source |
|---|---|---|---|---|
| en | 2 GB IFC from Synchro, 16 GB RAM, open() runs out of memory; asks about lazy loading or another storage tech | How to work with a 2 GB IFC | bim_manager | [#2025](https://github.com/IfcOpenShell/IfcOpenShell/issues/2025) |
| en | Downloaded BIM4LCA sample IFCs; bigger ones freeze Bonsai with no error; BIMcollab opens them | Bonsai freezes on 10-350 MB samples | student_beginner | [#7632](https://github.com/IfcOpenShell/IfcOpenShell/issues/7632) |
| en | Tried to open a 780 MB IFC in Bonsai on an M4 Max with 128 GB; Blender memory climbs to 340+ GB; ODA viewer opens it | Huge old file kills Bonsai | bim_coordinator | [#9826](https://github.com/IfcOpenShell/IfcOpenShell/issues/9826) |
| en | Compares load times: Open IFC Viewer 25 s, BIMVision about 1 min, Bonsai Viewer 5 min | One file, three viewers | bim_coordinator | [#9055](https://github.com/IfcOpenShell/IfcOpenShell/issues/9055) |
| en | Architect copies a structural IFC, deletes unneeded objects to link only a glass roof; open and first save are slow | Slow save for a consultant's IFC | architect | [#8099](https://github.com/IfcOpenShell/IfcOpenShell/issues/8099) |
| en | Program exits unexpectedly on a model with 300000 components; Aborted() from the wasm node build | web-ifc aborts on a super large model | developer_programmer | [#538](https://github.com/ThatOpen/engine_web-ifc/issues/538) |
| en | Building a viewer, traversing property relations for 400-500 MB files to cache psets; how long is expected? | Indexing time for big IFC in WebIFC | developer_programmer | [#1816](https://github.com/ThatOpen/engine_web-ifc/issues/1816) |
| en | Large ifc 1.3 GB, viewer crashes, processing in fragments works, same model works in APS viewer; will have 300 GB total | Viewer cannot open 1.3 GB IFC | bim_manager | [fragments #129](https://github.com/ThatOpen/engine_fragment/issues/129) |
| en | Integrating fragments into a construction PM platform; 2 GB industrial IFC loads very slow; needs P6 schedule | Slow 2 GB IFC for constructability viewer | contractor_site | [fragments #315](https://github.com/ThatOpen/engine_fragment/issues/315) |
| en | Testing the viewer on a real project with 40 models, 1 GB of frag files; unresponsive after 20 models | Multi-model scene becomes unresponsive | bim_manager | [fragments #228](https://github.com/ThatOpen/engine_fragment/issues/228) |
| en | Fragment load of a 33 MB ifc gives Out of memory in Chrome; Firefox RAM grows to 15-16 GB | Small file, huge memory | developer_programmer | [components #458](https://github.com/ThatOpen/engine_components/issues/458) |
| en | DWG-based software stands still importing IFC; what certification demands exist on speed? | Is import speed certified? | bim_manager | [forum](https://forums.buildingsmart.org/t/processing-speed-ifc-imports/2622) |
| en | Receives manufacturer geometry with engraved logos and finely triangulated pipes; how is such heavy geometry handled? | Opinion on high polygon count | bim_manager | [forum](https://forums.buildingsmart.org/t/4699) |
| en | Timing table shows export taking minutes with psets enabled versus 45 s without | Revit IFC export slow with properties | bim_manager | [#492](https://github.com/Autodesk/revit-ifc/issues/492) |
| en | IFC export hangs for 12+ hours (Revit 2020 structure model) | Revit export never finishes | structural_engineer | [Autodesk forum](https://forums.autodesk.com/t5/revit-structure-forum/export-to-ifc-is-not-working-the-revit-file-stays-not-responding/td-p/9912833) |
| en | Many projects fail with 'File is too large to export', intermittent, persists after exporter update | Revit 2022 export fails | bim_manager | [#458](https://github.com/Autodesk/revit-ifc/issues/458) |
| en | Rebar sets split into many entities; file went 200 MB to 70 MB after SimpleBIM merge | Rebar set bloat | bim_coordinator | [#76](https://github.com/Autodesk/revit-ifc/issues/76) |
| en | Industrial plant export 6h16 and 720 MB with insulation vs 2h43 without | Pipe insulation makes export huge | bim_manager | [#892](https://github.com/Autodesk/revit-ifc/issues/892) |
| en | Exporter 26.4.0/26.4.1 fails on a workshared model uploaded to Forma; fine in older exporter | Export error on workshared model | bim_coordinator | [#1021](https://github.com/Autodesk/revit-ifc/issues/1021) |
| en | Opening cuts skipped message when opening Revit and ArchiCAD IFC; Apply Openings fixes it | Is this a bug or intended? | bim_coordinator | [OSArch](https://community.osarch.org/discussion/3754/opening-cuts-skipped-in-bonsai-studio-0-9) |
| en | Host walls load with rectangular holes; lintels and sills absent; 324 IfcElements have no spatial containment | Missing masonry in Bonsai | bim_coordinator | [#9372](https://github.com/IfcOpenShell/IfcOpenShell/issues/9372) |
| en | All geometry renders entirely white though colours are visible in BIMvision | White model in web viewer | bim_coordinator | [components #745](https://github.com/ThatOpen/engine_components/issues/745) |
| en | Comparing same model in Dalux, BIMvision and That Open BIM App: one IfcSpace is a big solid box only here | Space drawn as geometry | facility_manager | [fragments #301](https://github.com/ThatOpen/engine_fragment/issues/301) |
| en | How can I tell whether a file is IFC2x3 or IFC4? File properties show nothing | Read the header schema | student_beginner | [forum](https://forums.buildingsmart.org/t/4802) |
| en | Header says originating_system OpenAI; IfcProject has 8 attributes instead of 9 | LLM-made IFC will not open | student_beginner | [#7945](https://github.com/IfcOpenShell/IfcOpenShell/issues/7945) |
| en | After installing IFC exporter 2022.6.0 I can no longer load IFC in Navisworks (IFC Modern); IFC2x3 error, IFC4 fine | Navisworks stops reading IFC2x3 | bim_coordinator | [#580](https://github.com/Autodesk/revit-ifc/issues/580) |
| en | Converting the official AC20-FZK-Haus IFC to 3DTiles: log says 'Finished loading 0 files' | Tiler loads nothing | developer_programmer | [mago-3d-tiler #79](https://github.com/Gaia3D/mago-3d-tiler/issues/79) |
| en | Same settings now give much larger GLB and more primitives after upgrading | GLB grew in 0.8 | developer_programmer | [#5486](https://github.com/IfcOpenShell/IfcOpenShell/issues/5486) |
| en | Conversion to GLB times out even after 12 hours, geometry complex (bent plates, shop-welded pipes) | IFC to GLB hangs on steel model | structural_engineer | [#4247](https://github.com/IfcOpenShell/IfcOpenShell/issues/4247) |
| en | Exporting IFC to STEP for a simulation tool gives a model 1000x too large whatever --length-unit is set to | Wrong scale in STEP | researcher_academic | [OSArch](https://community.osarch.org/discussion/2781/ifcconvert-how-to-control-the-resulting-step-models-scale) |
| en | EPSG:27700 coordinates set in Bonsai, ifc2gis output loads in the wrong place | IFC to GeoPackage in the ocean | civil_infra_engineer | [OSArch](https://community.osarch.org/discussion/3037/ifc-to-qgis-geopackage) |
| en | I want to optimize the workflow for transferring geometry and information from IFC to the GIS system | IFC to GIS workflow | bim_manager | [forum](https://forums.buildingsmart.org/t/ifc-to-gis/6115) |
| en | I have IFC2x3 from Revit, no Revit access, believe Archicad needs IFC4 | Upgrade 2x3 to 4 without Revit | student_beginner | [forum](https://forums.buildingsmart.org/t/convert-upgrade-ifc2x3-to-ifc4/5210) |
| en | Large model, want to slice a portion for a client, like obj export of selection | Save only selected elements | bim_coordinator | [#6118](https://github.com/IfcOpenShell/IfcOpenShell/issues/6118) |
| en | Need to deliver IFC plus DXF/DWG; Revit has a layer translation table, can Bonsai do that? | IFC to CAD layers | architect | [#8009](https://github.com/IfcOpenShell/IfcOpenShell/issues/8009) |
| en | Material info present in IFC and XML export but not in .mtl on OBJ export | OBJ without materials | architect | [#4846](https://github.com/IfcOpenShell/IfcOpenShell/issues/4846) |
| en | Large tool catalogs eat the context window before real work starts (Revit MCP, local agents) | MCP tool list too big | developer_programmer | [rvt-mcp #23](https://github.com/bimwright/rvt-mcp/issues/23) |
| en | Wants a tool returning the current Revit view as an image so a multimodal LLM can place elements visually | Screenshot tool for AI | architect | [revit-mcp-server #16](https://github.com/LuDattilo/revit-mcp-server/issues/16) |
| en | A validation report lists errors, but how do I find them in the raw file? | Analyzing IFC files with a text editor and checkers | bim_coordinator | [BIM Corner](https://bimcorner.com/analyzing-ifc-files/) |
| zh | 大型BIM模型在Web端为什么这么卡：能导出、能加载、能显示，不等于能高效跑 | Why do large BIM models lag in the browser? | developer_programmer | [Juejin](https://juejin.cn/post/7698926562423357450) |
| zh | IfcConvert会合并构件、丢expressID，要额外写入GlobalId才能和属性表关联；材质全变灰；毫米和米单位导致放大1000倍 | IFC to glTF pitfalls | developer_programmer | [Juejin](https://juejin.cn/post/7691297274821705728) |
| zh | 100M的模型导出IFC有1GB，转OBJ变3GB，机器卡死 | A 100 MB model becomes 1 GB IFC and 3 GB OBJ | developer_programmer | [CSDN](https://blog.csdn.net/nihaozhe/article/details/108704151) |
| zh | 模型导进Unity后管道材质变灰；超过100M的模型就卡死；WebGL三角面多了内存爆 | Grey materials and freezes in Unity/WebGL | developer_programmer | [cnblogs](https://www.cnblogs.com/nihaozhe/articles/13651935.html) |
| zh | Tekla、Revit加载慢，IFC里筛构件、出材料清单、找小零件都难 | Heavy desktop tools load slowly on steel projects | bim_manager | [cnblogs](https://www.cnblogs.com/lingyanspace/p/19739094) |
| zh | BIM轻量化的原理是什么 | What is the principle of BIM lightweighting? | developer_programmer | [Zhihu](https://www.zhihu.com/question/385964946) |
| zh | 转glTF保留属性与几何一一对应 | Keep properties linked one-to-one with geometry | developer_programmer | [Zhihu](https://zhuanlan.zhihu.com/p/2021897410683650709) |
| zh | 求推荐好用方便的IFC查看工具 | Any good IFC viewer to recommend? | bim_coordinator | [Zhihu](https://www.zhihu.com/question/583830829) |
| zh | 想不装软件在线打开IFC文件 | Open IFC online without installing | student_beginner | [Zhihu](https://zhuanlan.zhihu.com/p/651323857) |
| zh | rvt和ifc什么关系，导成ifc颜色为什么变了 | Why do colours change after RVT to IFC? | student_beginner | [Zhihu](https://www.zhihu.com/question/49455994) |
| zh | Revit转fbx材质丢失，试过各种办法 | Revit to FBX loses materials | architect | [Bilibili](https://www.bilibili.com/read/cv18398331/) |
| zh | 高版本revit的模型低版本打不开，导出ifc行不行 | Can IFC2x3 open in an older Revit? | bim_coordinator | [Zhulong](https://www.zhulong.com/zt_bim_3002296/detail42826395/) |
| zh | 先用IfcConvert把ifc转成dae，再用COLLADA2GLTF转gltf，路径里有中文好像会失败 | Two-step IFC to glTF; Chinese path fails | student_beginner | [cnblogs](https://www.cnblogs.com/LeeSki/p/14293418.html) |
| zh | BIM没有地理坐标，需要原点经纬度加xyz旋转角度，原点又不在模型中心 | Positioning after BIM to 3D Tiles | developer_programmer | [CSDN](https://blog.csdn.net/liyan_gis/article/details/100132931) |
| zh | 南京BIM规划报建要交原生模型和宁建模轻量化文件吗 | Do permit submissions need a lightweight file? | reviewer_authority | [Nanjing planning bureau](http://ghj.nanjing.gov.cn/njsgtzyj/202103/t20210301_2834720.html) |
| zh | Revit传到Robot/ETABS/SAP2000，IFC方式资料遗失或更动，原生档与API较佳 | IFC route loses data in analysis transfer | structural_engineer | [NTU thesis](https://tdr.lib.ntu.edu.tw/handle/123456789/90111) |
| ru | как перевести ifc в dwg и какими программами, работаю в Архикаде | IFC to DWG, with which programs? | architect | [forum.dwg.ru](https://forum.dwg.ru/showthread.php?t=96356) |
| ru | как лучше перенести 3D из Солида в Ревит, теряются ли параметры и материалы | SolidWorks to Revit: format and losses | architect | [forum.dwg.ru](https://forum.dwg.ru/showthread.php?t=159973) |
| ru | после экспорта в IFC из Ревита часть элементов и параметров потерялась, как проверить где проблема - в экспорте или в просмотрщике | Check the export or the viewer? | bim_coordinator | [forum.dwg.ru](https://forum.dwg.ru/showthread.php?t=154396) |
| ru | экспорт в ifc из Теклы 2017 для Field 3D не работает как надо, настройки не помогают | Tekla export for a viewer app misbehaves | structural_engineer | [forum.dwg.ru](https://forum.dwg.ru/showthread.php?t=146367) |
| ru | не все элементы передаются из Ревита 2016 в Старк ЕС, IFC пробовала - результат плохой | Revit to analysis software drops elements | structural_engineer | [forum.dwg.ru](https://forum.dwg.ru/showthread.php?t=133669) |
| ru | Discord удалили, документация пропала; GLTF в разы больше IFC; остались на 1.5.1 | IFC.js viewer project: library risks, glTF larger than IFC | developer_programmer | [Habr](https://habr.com/ru/articles/846382/) |
| ru | просмотр IFC, RVT, NWD моделей с серверной конвертацией | Vitro-CAD viewing with server conversion | bim_manager | [Telegram](https://t.me/s/bimacad?before=557) |
| ru | онлайн-инструмент преобразования Revit в IFC без лицензии | Online Revit to IFC converter | bim_coordinator | [Telegram](https://t.me/s/bimsk?before=133) |
| ja | IFCをglTFにして階層構造(Project>Site>Building>階>要素)も残したい。IfcOpenShellは遅い | Convert IFC to glTF keeping the hierarchy | developer_programmer | [Zenn](https://zenn.dev/kiyuka/scraps/a054a249f42a93) |
| ja | 大きいIFCを開くと全インスタンス・属性を先にパースして遅くメモリを食う | Lazy loading in IfcOpenShell 0.9 | developer_programmer | [Qiita](https://qiita.com/kiyuka/items/0d2ef739a0d34606a52f) |
| ja | 協力会社の重いモデルや古いモデルを開かずに値だけ取り出したい。API/プラグイン経由は遅い | Extract values from heavy models without opening them | bim_coordinator | [Zenn](https://zenn.dev/tomosandego/articles/59e6cf8dfe60bc) |
| ja | 管理タブの未使用の項目を削除を繰り返し、CAD読込・点群・ビューを先に削除 | Reduce Revit file size by purging | bim_coordinator | [Zenn](https://zenn.dev/malme/articles/2bfe2ffb1da08b) |
| ja | IFCを少し見るだけで数GBのソフトが必要。現場担当は開く環境がない | Site staff cannot open IFC without huge software | contractor_site | [Zenn](https://zenn.dev/kazuyamaeda/articles/97933cdafce6d8) |
| ja | Jw_cadで2D図面。元請から意匠IFCを受けて設備ルートを3D確認したい。ソフトを買う根拠がない | Small MEP office wants a free IFC viewer | mep_engineer | [note](https://note.com/limber_stork5044/n/n68df8d5a268b) |
| de | Welche kostenlosen IFC-Viewer sind am populärsten und warum einen herstellerneutralen Viewer für Gegenprüfungen behalten? | Which IFC viewer to cross-check exports | bim_coordinator | [BIM me up](https://bim-me-up.com/die-popularsten-ifc-viewer/) |
| de | Materialeigenschaften in IFC (exported material properties are not visible in every IFC viewer) | Material properties not shown in a viewer | bim_coordinator | [BIM me up](https://bim-me-up.com/materialeigenschaften-in-ifc/) |
| de* | Export to GML works in KITModelViewer but reimport fails with an XML error because the header comment is malformed | IFC to GML round trip in KITModelViewer | researcher_academic | [KIT SDM #13](https://github.com/KIT-IAI/SDM_KITModelViewer/issues/13) |
| es | al abrir un archivo IFC (2x3) se pierde parte de la información geométrica; adjunto captura en Bonsai y Bonsai Viewer | Geometry seems lost (flipped normals) | other | [#8131](https://github.com/IfcOpenShell/IfcOpenShell/issues/8131) |
| es | problemas con los ifc: al abrirlo y guardarlo en otro formato se pierden las coordenadas que traia | Coordinates lost on re-save | architect | [Autodesk forum](https://forums.autodesk.com/t5/revit-architecture-forum/problemas-con-ifc-s/td-p/10189111) |
| es | archivos IFC para replanteo, COGO, capas desde presentation layer, no soportado en Android | Using IFC in Trimble Access | contractor_site | [Trimble help](https://help.fieldsystems.trimble.com/trimble-access/2021.20/es/Map-files-BIM-and-IFC.htm) |
| it | dall'IFC come estraggo piante e sezioni in DXF? | Get plans/sections as DXF from an IFC | architect | [ACCA Biblus](https://biblus.acca.it/una-guida-completa-per-convertire-file-ifc-in-dxf/) |
| it | ho solo il DWG, come lo converto in IFC? | Convert DWG to IFC | architect | [ACCA Biblus](https://biblus.acca.it/come-convertire-un-file-dwg-in-ifc-in-modo-semplice/) |
| sk | Oddiaľ pôdorys o 15 percent. / Ukáž vzduchotechniku v perspektíve na celú obrazovku. | Relative camera zoom and MEP perspective in an AI viewer | bim_manager | [AIMviewer #65](https://github.com/Menezeris/AIMviewer/issues/65) |
| fr* | IFC with accented characters in the header FILE_NAME gives a wstring_convert error when converting to XML; DAE works | IfcConvert fails on accents in header | bim_coordinator | [#1016](https://github.com/IfcOpenShell/IfcOpenShell/issues/1016) |
| tr* | Surface style name with Turkish dotted I and C-cedilla encoded via \X2\ makes OBJ conversion fail | Unicode in style name breaks OBJ export | developer_programmer | [#101](https://github.com/IfcOpenShell/IfcOpenShell/issues/101) |

## Ready test prompts

Synthetic prompts (not real quotes), curated from the dataset and rewritten to sound like quick messages to an assistant connected to an IFC model or Revit. "Base" is the dataset synthetic id the prompt was adapted from. Difficulty is for the assistant. All assume a file is loaded unless noted.

| # | lang | prompt | type | difficulty | expected behavior | base |
|---|---|---|---|---|---|---|
| 1 | en | architect sent a 480mb ifc and the site tablet chokes on it. quickest way to get just the structure and level 2 so we can view it on site | how_to | easy | Suggest filtering by class and storey, offer to write a subset copy, report size before and after | en-s005 |
| 2 | en | this ifc is 1.4GB, whats taking all the space? list classes by count and by rough bytes | model_task | medium | Scan without building geometry, count instances per class, estimate bytes, give top contributors and options | en-fs-s001 |
| 3 | en | which proxies use FaceBasedSurfaceModel or a tessellated brep with huge face counts? i think thats why it runs out of memory | model_task | hard | List proxies by representation type with face/vertex counts and rank them | en-fs-s002 |
| 4 | en | check if repeated families are exported as mapped items or just duplicated geometry, and how much size we could save | model_task | hard | Compare identical-geometry instances against RepresentationMap use; estimate savings | en-fs-s003 |
| 5 | en | make me a light version for the web viewer: only walls slabs columns, no psets, save as ifczip | model_task | medium | Create a filtered copy, strip property sets, write compressed ifcZIP, report before/after; keep original | en-fs-s005 |
| 6 | en | file is 400mb, which elements are the heavy ones? faceted breps with crazy face counts, top 20 pls | model_task | hard | Compute face counts per product, rank top 20 with class, name, type, share of total | en-geom-s003 |
| 7 | en | file is 700MB, drop the insulation and ports, keep everything else, tell me the size after | model_task | hard | Remove coverings and `IfcDistributionPort` in a copy, save, compare sizes, confirm relationships | en-mep-s016 |
| 8 | en | blender freezes opening this 300mb ifc but bimcollab opens it. which classes are the heavy ones | troubleshooting | medium | Count classes, estimate geometry weight, suggest excluding heavy classes | en-gh-ifcopenshell-s013 |
| 9 | en | file is like 1.3 GB, dont crash, just give me the storeys, element counts per class and total size | model_task | hard | Use streaming or lazy parsing, avoid geometry, return storeys and counts | en-gh-thatopen-s007 |
| 10 | en | will this ifc blow the 4GB wasm limit? give me size, entity count and a recommendation | model_task | medium | Report size, count, rough memory estimate, advise server-side conversion; state the limit belongs to the engine | en-gh-thatopen-s017 |
| 11 | en | our permit portal rejects ifc over 200mb, mine is 480. whats the safest way to shrink it without losing what they check? | troubleshooting | medium | Ask what the portal checks; reduce detail, zip, drop non-required data; verify required classes and properties remain | en-fs-s016 |
| 12 | en | revit crashes exporting ifc4 on a huge model, any way to split it or find the bad element? | troubleshooting | medium | Suggest current-view/per-level export, journal check, per-category tests, add-in conflicts; ask versions | en-gh-revit-ifc-s013 |
| 13 | en | ifc export of the mep model is 600mb because of flex duct, how do i reduce that | troubleshooting | easy | Suggest detail level, view-based export, excluding flex duct, zipping; no invented menu names | en-autodesk-revit-export-s012 |
| 14 | en | opened the ifc and its blank/white?? file is 40mb | troubleshooting | medium | Check geometry presence, surface styles, units, far-away coordinates, bounding box | en-beginner-qa-s011 |
| 15 | en | ifc opens but I see nothing, just a tiny dot somewhere. whats wrong | troubleshooting | medium | Report bounding box, distance from origin, units; suggest false origin or zoom to extents | en-viewconv-s017 |
| 16 | en | some elements show in other viewers but not here. check which ones only have a Plan-context representation instead of Model | model_task | medium | Inspect representation contexts, list products whose body is only in a 2D context | en-gh-xbim-others-s008 |
| 17 | en | walls show no holes after opening this ifc and the windows float in front. whats wrong | troubleshooting | medium | Check `IfcRelVoidsElement`, number of openings per element, viewer void limit; suggest Apply Openings or another viewer | en-openings-s006 |
| 18 | en | I dont have revit, whats the easiest free way to look at this ifc? no install if possible, and I need to see properties | how_to | easy | Suggest free desktop and browser viewers with caveats; warn about uploading confidential files; offer a data summary | en-beginner-qa-s003 |
| 19 | en | does the bim360 viewer open ifc4 or only 2x3? asking before the client sends | how_to | easy | Explain how to read the schema from the header; say supported versions must be confirmed in current docs | en-navis-acc-s013 |
| 20 | en | ifc upload failed in acc docs, no error, just 'failed to process'. file is 900mb. whats wrong with it? | troubleshooting | hard | Inspect validity, schema, units and size; suggest splitting or reducing; do not invent a size limit | en-navis-acc-s006 |
| 21 | en | convert this 2x3 file to ifc4 and tell me what got lost | model_task | hard | Write an IFC4 copy, summarise changed or dropped entities; leave the original untouched | en-gh-xbim-others-s007 |
| 22 | en | the step export is 1000x too big, units in the ifc are mm. whats going on | model_task | medium | Read `IfcUnitAssignment`, explain unit mismatch, export with the right length unit, verify bounding box | en-osarch-s009 |
| 23 | en | convert this to glb but keep the colors, web-ifc or ifcconvert whichever | model_task | medium | Check styles exist; explain options and limits; export and report size and element count | en-stackoverflow-s004 |
| 24 | en | glb of just walls and slabs, the file is 600mb and I want it under 50 | model_task | medium | Filter by class, export, report size, suggest decimation if still large | en-viewconv-s002 |
| 25 | en | need a dwg of the level 2 plan with layers by ifc class, walls A-WALL doors A-DOOR. can u do it | model_task | hard | Resolve the storey, map classes to layers, produce DXF/DWG or say what is not possible and offer an alternative | en-viewconv-s001 |
| 26 | en | before I push this to QGIS check units and IfcMapConversion, last time it landed in the ocean | model_task | medium | Read units and map conversion/CRS, flag mm vs m, give corrected values | en-viewconv-s006 |
| 27 | en | convert this ifc to sqlite and then count elements by ifc class, biggest first | model_task | medium | Run an Ifc2Sql-style export (or equivalent), run the GROUP BY query, report path and counts | en-data-s003 |
| 28 | en | tekla precast ifc with rebar kills my web viewer. can u make a lighter copy without the reinforcing bars | troubleshooting | medium | Explain cause, create a filtered copy without `IfcReinforcingBar`, report size and what was removed | en-struct-s005 |
| 29 | en | delete everything except IfcWall and IfcSlab, file has 20k elements and my delete loop takes 10 min. do it fast | model_task | medium | Use batch extraction rather than per-element deletion; save a new file; report counts | en-dev-s011 |
| 30 | en | opening a 200MB ifc is slooow and memory keeps growing in my api, what do I change | troubleshooting | medium | Explain model provider/disposal, avoiding geometry context, reusing lookups; ask library and version | en-gh-xbim-others-s013 |
| 31 | ru | ифс весит 900 мб, откуда столько? глянь по классам что самое тяжёлое и что можно выкинуть не ломая модель | model_task | medium | Count entities by class and size, list heavy items and safe removals | ru-fs-s006 |
| 32 | ru | ревит экспорт в ifc висит уже 3 часа, 500 мб rvt, что отключить чтоб побыстрее? | troubleshooting | easy | Explain what affects speed (current view only, per level, 2D elements, links, quantities, heavy families) without inventing options | ru-fs-s007 |
| 33 | ru | ифс на 1.5 гига, вьюер у экспертизы виснет, чем можно облегчить не потеряв свойства | troubleshooting | medium | Reduce geometry, split by discipline or zone, keep property sets, inspect heaviest entities | ru-tim-expertiza-s014 |
| 34 | ru | чем бесплатно открыть ifc, без регистрации и чтоб свойства смотреть можно было | how_to | easy | Suggest free viewers, mention properties panel and privacy of web upload | ru-autodesk-telegram-s014 |
| 35 | ru | навис не показывает ифс4 из ревита, 2x3 нормально открывается. че делать | troubleshooting | medium | Explain geometry support limits in older importers; recommend 2x3 CV2.0 or update tools | ru-vm-s017 |
| 36 | ru | нужен dwg из этого ифс, чтоб слои по классам, а то в автокаде одним куском | model_task | hard | Map classes to layers, export DWG/DXF or advise a route | ru-viewconv-s011 |
| 37 | ru | web-ifc на 300мб файле вешает вкладку, как грузить кусками или в воркере | troubleshooting | hard | Suggest worker, fragments/streaming, server-side conversion; mention wasm limits | ru-habr-dev-s015 |
| 38 | zh | 这个ifc有800多M，网页里卡死了，帮我按楼层拆成几个小文件 | model_task | hard | Split by `IfcBuildingStorey` preserving shared context; report counts and sizes | zh-fs-s008 |
| 39 | zh | 帮我把这个ifc转成glb给前端用，每个mesh要带GlobalId，不然属性对不上，按楼层拆开最好 | model_task | hard | Export geometry, map each mesh to GlobalId, split by storey, write metadata JSON, warn about lost properties | zh-csdn-dev-s003 |
| 40 | zh | 对方revit版本低，我导ifc给他行吗，选2x3还是4 | how_to | easy | Recommend IFC2x3 Coordination View 2.0 for compatibility, note losses | zh-revit-export-s017 |
| 41 | zh | 这个IFC4的模型能不能转成IFC2x3？帮我看看会丢哪些东西 | model_task | hard | Check schema and entities not in 2x3, convert a copy, list losses | zh-vm-s006 |
| 42 | zh | ifc 1.2G 太大了打不开，看看是哪类构件占体积最大，螺栓之类的能不能删 | model_task | hard | Rank classes by count and size, flag fasteners, offer to filter into a smaller file | zh-zhihu-s006 |
| 43 | ja | 400MBのIFC重すぎ。エンティティ別にインスタンス数とサイズ内訳出して、何が原因か教えて | model_task | hard | Count instances per type, estimate size shares, suggest reductions | ja-japan-s016 |
| 44 | ja | MacでIFCを開ける無料のビューアってありますか？属性も見たいです | how_to | easy | Recommend browser and Mac-capable viewers and how to inspect properties | ja-viewconv-s013 |
| 45 | es | el ifc me pesa 600mb, puedes quitar los elementos 2D y las anotaciones y decirme cuanto baja? | model_task | medium | Detect annotation and 2D items, remove in a copy, report size and counts | es-fs-s009 |
| 46 | de | die ifc ist 700 MB und solibri braucht ewig, kannst du leere psets und nicht benutzte Eigenschaften rausnehmen? | model_task | medium | Find empty and unused property sets, strip in a copy, validate references, report before/after | de-fs-s011 |
| 47 | fr | mon ifc de 1,2 go plante dans le navigateur, mémoire insuffisante, comment on fait pour l'afficher quand même ? | troubleshooting | easy | Explain streaming/tiled viewers, conversion to fragments or glTF, splitting; desktop viewers for very large files | fr-fs-s012 |
| 48 | it | trova gli elementi con più di 50000 triangoli, secondo me sono quelli che appesantiscono il file | model_task | hard | Inspect representations, list elements above the threshold with class, name and triangle count | it-fs-s015 |
| 49 | pt | qual a diferença de tamanho entre ifc, ifczip e ifcxml? posso mandar o zip pro cliente? | how_to | easy | Explain STEP text vs XML vs zip with typical ratios (vendor figures), tool support; ifcZIP is a valid delivery format | pt-fs-s010 |
| 50 | ko | ifc 파일 열면 아무것도 안 보이는데 왜 이래요? 용량은 200MB | troubleshooting | medium | Check header, geometry presence, units, far-from-origin coordinates | ko-korea-s005 |

## Edge cases and traps for MCP testing in this area

1. **"Performance" is ambiguous.** It can mean the IFC file size, the Revit (RVT) file size, export time, viewer speed, parsing time, or even the MCP tool catalogue eating the model's context window (see [rvt-mcp #23](https://github.com/bimwright/rvt-mcp/issues/23)). A good assistant asks which, or states its reading.
2. **Do not build geometry to answer a counting question.** Counting classes, storeys, or listing property sets works on the raw data. A tester should check that a 1 GB file does not trigger a full geometry run, and that long jobs report progress or time out gracefully.
3. **Memory is several times the file size.** Even with lazy open, the Qiita benchmark reports memory about 2.7x file size for the largest (393 MB) file. An answer promising "fine on a laptop" for a 2 GB file without a basis is suspect.
4. **Browser limit is an engine limit.** The roughly 4 GiB WebAssembly ceiling belongs to the viewer engine, not to IFC itself. Chunked input does not lift it until a 64-bit build exists (fragments #258).
5. **Light copies must be honest.** A filtered or stripped copy should keep GlobalIds, report which classes/psets were removed, warn about dangling relationships (containment, voids/fills, type links), save as a new file, and be re-verified by reopening. Removing `IfcReinforcingBar` or `IfcDistributionPort` changes what take-off and MEP checks can see.
6. **Editing is in-memory until saved.** Some IFC MCP servers keep edits in memory and write only on an explicit save call ([MCP servers doc](../../04_open_source/mcp_servers_and_ai_tools.md)). A "done" message before a save is a failure.
7. **ifcZIP and friends.** `.ifczip` (single IFC inside a zip), plain `.zip` with several IFCs, ifcXML, ifcJSON: ask the tool to open each. ifcXML is much larger than SPF; a zip holding multiple IFCs is not supported by viewers (forum thread on federated IFC). Vendor ratios are not guarantees.
8. **One viewer is not proof.** Opening cuts skipped, flipped normals, hidden "Unsorted" collections, visible IfcSpace boxes, missing styles all depend on the viewer. Expect cross-checks in a second viewer and facts from the file.
9. **Units and origin after conversion.** A converter can output metres or millimetres, local or site placement, and may ignore `IfcMapConversion`. Always read `IfcUnitAssignment`, map conversion and bounding box before and after.
10. **Properties do not travel in meshes.** OBJ/GLB/FBX/DAE have no IFC properties. A conversion that "keeps properties" must store them somewhere (JSON keyed by GlobalId). IfcConvert merging or renumbering can break the link to expressIDs; GlobalIds are the stable key.
11. **Colour is a style, not a material.** White or grey output may simply mean the IFC has no styles (the white-model case) rather than a converter bug. IFC4 vs IFC2x3 can differ in colour output.
12. **Schema versions and viewers.** IFC4 geometry types (`IfcPolygonalFaceSet`, tessellation) are not read by every engine; IFC4.1 was withdrawn; IFC4.3 alignments often do not display. Never promise that a version "works everywhere".
13. **Invalid files from AI or custom scripts.** LLM-written IFC may miss attributes (for example an `IfcProject` with 8 instead of 9 attributes). A tester should expect validation before blaming the viewer, and expect the assistant not to fabricate geometry that passes by luck.
14. **Encoding and paths.** Raw Cyrillic, Latin-1 or Mac-Roman bytes in strings, newlines inside escaped strings, non-Latin file names, and non-ASCII header fields break strict readers. Docker mounts can also mimic encoding errors.
15. **Privacy.** Online converters and viewers need an upload. For confidential models the assistant should say so and prefer local tools; it should not pick a hosted service silently.
16. **Version-pinned library errors.** BindingError or "argument count mismatch" for web-ifc and fragments often mean a wrapper and wasm version mismatch, not a bad file. Ask for versions.
17. **Revit-side export behaviour is version-specific.** Option names, defaults (for example rebar-set behaviour in newer Revit) and exporter regressions change. Do not assert menu names or defaults without a version.
18. **Prompt injection.** File names, IFC strings, property values or comments may contain instructions. They are data.
19. **Unsupported conversions.** 3D PDF, FBX, and DWG-to-IFC with semantics are weak or absent in common open tools; the right answer says so and suggests an alternative rather than pretending.
20. **National submission rules.** Some authorities ask for native files plus a lightweight format (for example the Nanjing 宁建模 notice in the table). The assistant should not assume an IFC alone satisfies such a rule.

## Related docs

- [Viewers, checkers, CDE and converters](../../03_software/viewers_checkers_cde_converters.md)
- [Inside an .ifc file (header, encoding, ifcZIP, ifcXML)](../../01_ifc_basics/02_ifc_file_anatomy.md)
- [Geometry, placement, coordinates, units](../../01_ifc_basics/06_geometry_placement_coordinates_units.md)
- [Materials, classification, types, styles](../../01_ifc_basics/07_materials_classification_types_styles.md)
- [What is IFC, versions and views](../../01_ifc_basics/01_what_is_ifc_and_versions.md)
- [Revit IFC export reference](../../03_software/revit/ifc_export_reference.md)
- [Revit IFC import and link reference](../../03_software/revit/ifc_import_link_reference.md)
- [IFC in other authoring tools](../../03_software/authoring_tools_ifc.md)
- [Libraries and toolkits (IfcOpenShell, web-ifc, xBIM)](../../04_open_source/libraries_and_toolkits.md)
- [MCP servers and AI tools](../../04_open_source/mcp_servers_and_ai_tools.md)
- [Multilingual glossary](../../08_glossary/glossary_multilingual.md)
- Sibling topic file: [Importing IFC and cross-tool interoperability](import_and_interoperability.md)
