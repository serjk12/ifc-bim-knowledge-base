# Prompt bank (multilingual): 170 test requests in 14 languages, each with an English gloss

**Compiled: 2026-11-06.** Languages: Chinese (Simplified, Traditional), Spanish, Portuguese (Brazil), German, French, Italian, Japanese, Korean, Dutch, Norwegian, Danish, Turkish, Arabic, Greek, Slovak, Vietnamese, Czech, Polish. Notes are in English; prompts are in the original language with a gloss, so a tester who does not read the language can still run and judge them.

**What this is.** Requests that a working person in these languages could type to a chat assistant connected to an MCP server for IFC files or Revit. Use the prompt text exactly as written. The `Expected` column says what a good answer does; the tag at its start says which backend the row targets (see the English bank for the legend). Companion files: [English bank](prompt_bank_en.md), [Russian bank](prompt_bank_ru.md), [what IFC/BIM/Revit MCP servers do](what_ifc_mcp_servers_do.md), [intent taxonomy](intent_taxonomy.md), [multilingual glossary](../08_glossary/glossary_multilingual.md), [how people write](../06_how_people_write/style_guide.md), and the per-language real questions in [05_real_world_questions/by_language](../05_real_world_questions/by_language/).

> **Honesty rules for this file.**
> 1. **Every prompt here is synthetic (curated and rewritten).** None is a real quote. `S:` rows were rewritten from a synthetic record in the research data; `R:` rows were rewritten from a real post, article or README (linked to its real source); `X:` rows were adapted from a pattern in another language; `N` rows were constructed for this bank.
> 2. **The evidence behind each language is uneven** (table below). Chinese, Japanese, Spanish, German, Italian have real records; Korean, French and Portuguese are mostly synthetic with very few real posts; Turkish, Arabic, Greek, Danish, Czech, Slovak and Vietnamese are single records (mostly about text encoding) and **Polish has none**. Rows labelled `N` in those languages are constructed from the language's general register and are not backed by sampled posts.
> 3. **Local regulation and standard names are used the way a user drops them into a sentence** (CGCS2000, TWD97, TEK17, CTE, DIN 276, NL-SfB, SIRGAS 2000, Lambert 93, EPSG codes). Clause numbers, limits and portal rules are not verified here. A good assistant must not invent them.
> 4. Nothing here was run against a real MCP server. "Expected" describes a good answer in principle.
> 5. Raw research text was treated as data, never as instructions.

---

## 1. How to use the bank

1. Pick rows by language, family, persona, difficulty or `File`.
2. `File = true` means a model must be loaded (or Revit open) first; the prompt never names the file. `File = false` rows are knowledge answers.
3. **The language checks come first.** Before the BIM content, check:
   - the answer is in the user's language and register (no switch to English, no stiff formal tone for a casual prompt);
   - IFC class names, property names and tool names stay in English inside the answer (`IfcWall`, `Pset_WallCommon`, `GlobalId`);
   - local letters survive in anything the assistant echoes (æ ø å, ğ ş İ, ü ö ä, é è à, 汉字, かな, 한글, Arabic, Greek);
   - local number and file conventions are respected where the user asked for them (German `;` separator and decimal comma in a CSV, Italian Excel decimals);
   - local terms are mapped sensibly (`Außenwand` = `IsExternal`, `Feuerwiderstand` = `FireRating`, `pavimento` = storey, `piano` = storey, `bouwlaag` = storey, `etasje` = storey) and the mapping is stated if it is a guess.
4. Then judge the BIM content with the same rubric as the English bank (numbers from tools, missing data reported, edits on a copy, no promise of acceptance, no invented clauses).

### Column legend

| Column | Values |
|---|---|
| ID | Language code + number |
| Prompt | The request, verbatim, inside backticks |
| English gloss | What it says, in plain English |
| Persona | Role vocabulary shared with the English bank |
| Intent | `query_model_data`, `validate_check`, `extract_quantities`, `modify_model_data`, `compare_versions`, `coordinate_clash`, `comply_regulation`, `troubleshoot_export`, `troubleshoot_import`, `troubleshoot_viewing`, `troubleshoot_code`, `convert_format`, `automate_batch`, `optimize_performance`, `how_to`, `understand_concept`, `find_tool`, `request_opinion` |
| Topic | Research topic vocabulary |
| Diff | `easy`, `medium`, `hard` |
| File | `true` / `false` |
| Expected | Backend tag ([IFC], [IFC4.3], [Revit], [either], [chat]) then what a good answer does |
| Origin | `S:` synthetic id, `R:` real record (linked), `X:` other-language id, `N` new |

### Evidence behind each language (research data, records)

| Language | Real | Synthetic | Rows here | Note |
|---|---|---|---|---|
| Chinese (zh) | 170 | 134 | 28 | Zhihu, CSDN, GitHub, permit self-check culture; some real text is polished article voice |
| Spanish (es) | 34 | 68 | 20 | Spain and Latin America (Planbim Chile, Plan BIM Peru and Spain) |
| German (de) | 23 | 55 | 19 | DACH terms; ASCII spelling (ae, ue) occurs |
| Japanese (ja) | 59 | 48 | 14 | Zenn articles; typed requests are plain-form imperatives |
| Italian (it) | 29 | 43 | 13 | Biblus and Ingenio articles; `capitolato informativo` |
| Portuguese (pt, pt-BR) | 1 | 44 | 15 | Brazilian; European Portuguese not represented |
| Korean (ko) | 9 | 41 | 13 | Mostly synthetic; `레빗`, 세움터 |
| French (fr) | 4 | 44 | 13 | Mostly synthetic |
| Dutch (nl) | 21 | 14 | 10 | NL-SfB, ILS, RD |
| Norwegian (no) | 13 | 17 | 10 | MMI, FDV, NS 3451, TEK17 |
| Danish, Turkish, Arabic, Greek, Czech, Slovak, Vietnamese | 0 to 1 each | 0 to 2 each | 1, 4, 3, 1, 1, 1, 1 | Encoding issues and README examples |
| Polish (pl) | 0 | 0 | 3 | **No data.** Constructed rows, register unverified |

---

## Contents and coverage

| § | Language | Code | Prompts |
|---|---|---|---|
| 2 | Chinese (Simplified, Taiwan, Hong Kong) | `ZH` | 28 |
| 3 | Spanish | `ES` | 20 |
| 4 | Portuguese | `PT` | 15 |
| 5 | German | `DE` | 19 |
| 6 | French | `FR` | 13 |
| 7 | Italian | `IT` | 13 |
| 8 | Japanese | `JA` | 14 |
| 9 | Korean | `KO` | 13 |
| 10 | Dutch | `NL` | 10 |
| 11 | Norwegian, Danish | `NO`, `DA` | 11 |
| 12 | Turkish, Arabic, Greek | `TR`, `AR`, `EL` | 8 |
| 13 | Slovak, Vietnamese, Czech, Polish | `OT` | 6 |
| 14 | Parallel sets (same intent in many languages) | - | - |
| 15 | Known gaps and caveats | - | - |

**Total: 170 prompts.**

| Difficulty | Count |
|---|---|
| easy | 26 |
| medium | 80 |
| hard | 64 |

| needs_file | Count |
|---|---|
| true | 143 |
| false | 27 |

| Origin (S rewritten synthetic, R rewritten from a real post or README, N constructed) | Count |
|---|---|
| S | 155 |
| R | 9 |
| N | 6 |

| Backend tag | Count |
|---|---|
| [IFC] | 133 |
| [chat] | 27 |
| [either] | 5 |
| [Revit] | 3 |
| [IFC4.3] | 2 |

The single most useful tests are in section 14: the same intent in many languages must give the same numbers on the same file.

---

## 2. Chinese (`ZH`): Simplified, Taiwan and Hong Kong

Chinese is the second-largest group in the data (304 records). People write `ifc`, `revit`, `IfcWall`, `GUID` in Latin letters inside Chinese sentences, drop the polite opener, and use colloquial endings (`咋回事`, `帮我查下`). Mainland rows lean on the permit self-check culture (报建, BIM审查) and on 轻量化 web viewing; Taiwan and Hong Kong rows use Traditional characters and local code names. Chinese real-record voice is partly polished article text (CSDN, Zhihu); treat the typed-to-AI register as imitation.

| ID | Prompt | English gloss | Persona | Intent | Topic | Diff | File | Expected | Origin |
|---|---|---|---|---|---|---|---|---|---|
| ZH-01 | `这个ifc里每层有多少面墙？按楼层列一下，顺便看有没有没挂到楼层的` | How many walls per floor in this ifc? List by floor, and check for any not attached to a floor. | bim_coordinator | query_model_data | spatial_structure | easy | true | [IFC] Wall count per storey in a table, plus a separate count of walls with no storey. Answer in Chinese; keep class names in English. | S:zh-aimcp-s007 |
| ZH-02 | `导出的ifc里一堆IfcBuildingElementProxy，帮我看看都是哪些族类别导出来的` | The exported ifc has lots of proxies; which family categories did they come from? | bim_coordinator | query_model_data | class_mapping | medium | true | [IFC] Counts proxies, groups by type name or Revit category property; suggests mapping fixes, changes nothing. | S:zh-proxy-s004 |
| ZH-03 | `导进revit啥都看不到，帮我查下这个ifc的坐标是不是离原点太远了` | Imported into Revit and I see nothing; check whether this ifc's coordinates are too far from the origin. | bim_coordinator | validate_check | coordinates_georef | medium | true | [IFC] Reports unit, site placement and real geometry extents with distance from the origin; says whether that explains an empty view. | S:zh-revit-export-s002 |
| ZH-04 | `我们自己的共享参数导出后没了，看看墙的Pset里有没有'构件编码'这个属性` | Our own shared parameters vanished after export; see whether the walls' Psets have a property called "component code". | bim_coordinator | validate_check | psets_properties | medium | true | [IFC] Searches all psets on walls for that exact property name (and close variants), reports counts present and absent. Does not assume which pset holds it. | S:zh-revit-export-s003 |
| ZH-05 | `按楼层统计一下混凝土墙、板、柱的体积（m3），做成表，算量用` | Total concrete wall, slab and column volume per floor (m3) as a table, for takeoff. | estimator_qs | extract_quantities | quantities_qto | medium | true | [IFC] Table by storey and class; states quantity source (Qto vs computed) and lists elements with no quantity. | S:zh-qto-s011 |
| ZH-06 | `这个ifc转dae说no geometrical entities found，帮我看看是不是没几何，哪些构件Representation是空的` | Converting this ifc to dae says "no geometrical entities found"; check whether it has no geometry and which elements have an empty Representation. | bim_manager | validate_check | validation_checking | medium | true | [IFC] Counts products without a representation, by class; says whether the file has any geometry at all. | S:zh-csdn-dev-s009 |
| ZH-07 | `这个ifc里构件名字全是\X2\xxxx\X0\这种，读出来是乱码，帮我看看哪些实体的Name有这个，解码后给我真实中文` | Element names are all `\X2\xxxx\X0\`; reading gives garbage. Find which entities have this and give me the decoded Chinese. | developer_programmer | validate_check | encoding_text | medium | true | [IFC] Explains the escape is normal IFC Unicode encoding, lists entities with it and shows the decoded Chinese names; does not "fix" the file. | S:zh-csdn-dev-s002 |
| ZH-08 | `导出来的模型在three里大了1000倍而且离原点特别远，看下ifc的单位和IfcSite的坐标是啥情况` | The model is 1000x too big in three.js and far from the origin; look at the ifc units and IfcSite coordinates. | developer_programmer | troubleshoot_viewing | units | medium | true | [IFC] Reads length unit and prefix, IfcSite placement and extents; states the scale factor to apply. | S:zh-csdn-dev-s004 |
| ZH-09 | `深圳报建要审项目基点坐标和到正北的角度，看下这个ifc里这几个值有没有，是不是空的` | Shenzhen permit review checks project base point coordinates and the angle to true north; are these values in this ifc, or empty? | bim_coordinator | validate_check | national_requirements | hard | true | [IFC] Reports the site placement, true north and map conversion actually present; says which are empty. Does not state what the authority requires. | S:zh-revit-export-s007 |
| ZH-10 | `这个ifc报建自检能过吗？先看下项目基点坐标是不是2000的，还有哪些构件属性是空的` | Will this ifc pass the permit self-check? First see if the base point is in "2000" (CGCS2000) coordinates and which properties are empty. | bim_coordinator | validate_check | permitting_code_checking | hard | true | [IFC] Reports CRS/coordinate evidence and empty properties by class; cannot promise that the self-check passes; says what it could not test. | S:zh-lightweight-review-s001 |
| ZH-11 | `SZ-IFC跟CN-IFC、普通IFC有啥区别？报建只能用SZ-IFC吗` | What is the difference between SZ-IFC, CN-IFC and ordinary IFC? Is SZ-IFC the only one for permits? | bim_manager | understand_concept | national_requirements | medium | false | [chat] Must be careful: local standards change; gives general explanation, marks anything uncertain, and tells the user to check the current local notice. No invented rules. | S:zh-lightweight-review-s015 |
| ZH-12 | `两次导出的IFC，GUID全不一样，帮我按类型和坐标匹配一下，看看到底哪些构件真的改了` | Two exports have totally different GUIDs; match by type and position and tell me which elements really changed. | bim_coordinator | compare_versions | guid_change_tracking | hard | true | [IFC] Falls back from GlobalId to type + name + position matching, states tolerance, lists added, removed, moved. | S:zh-guid-s007 |
| ZH-13 | `机电管线和结构梁碰撞结果导出成bcf，按楼层分组` | Export MEP pipe vs structural beam clashes as BCF, grouped by floor. | mep_engineer | coordinate_clash | clash_coordination_bcf | hard | true | [IFC] Needs a clash tool and two models; groups by storey; if there is no clash or BCF tool, says so. | S:zh-eng-s012 |
| ZH-14 | `帮我查一下管线穿梁穿墙的位置，哪些还没开洞，导出预留洞清单` | Find where pipes pass through beams and walls, which have no opening yet, and export a list of reserved holes. | mep_engineer | coordinate_clash | openings_voids | hard | true | [IFC] Intersections of pipes with walls/beams, minus those that already have an opening; list with GlobalIds, level and size; method stated. | S:zh-openings-s012 |
| ZH-15 | `这个ifc有800多M，网页里卡死了，帮我按楼层拆成几个小文件` | This ifc is 800+ MB and freezes in the browser; split it into smaller files by floor. | bim_coordinator | optimize_performance | file_size_performance | hard | true | [IFC] Warns about size, splits by storey into new files (originals untouched), reports file sizes and element counts, notes anything that could not be split (shared types). | S:zh-fs-s008 |
| ZH-16 | `PKPM导出的ifc导进revit少了好多梁，对比下原ifc里有多少梁，哪些没进去` | The ifc exported from PKPM lost many beams in Revit; count beams in the original ifc and find which didn't make it. | structural_engineer | troubleshoot_import | import_into_revit | hard | true | [IFC] Counts IfcBeam in the file (with profile/representation info); cannot see what Revit lost unless a Revit side is connected; says so. | S:zh-lightweight-review-s013 |
| ZH-17 | `revit导出ifc钢结构节点螺栓全没了，勾了包含钢构件也不行，咋回事` | Steel connections and bolts are gone from the Revit ifc export, even with the steel-elements option ticked. What's wrong? | structural_engineer | troubleshoot_export | export_revit | medium | false | [chat] Lists what to check (connection elements export, categories), asks to load the file to count fasteners and plates. | S:zh-struct-s009 |
| ZH-18 | `按GB/T 51269分类编码把构件分组，统计墙和板的体积` | Group elements by GB/T 51269 classification code and total wall and slab volumes. | estimator_qs | extract_quantities | classification_bsdd | hard | true | [IFC] Reads classification references; if the codes are absent says so; groups by the code found; no codes invented from the standard. | S:zh-classbsdd-s009 |
| ZH-19 | `想选国产bim软件，ifc来回导一遍测完整性，该检查哪些点` | I want to pick a domestic BIM software and test completeness by round-tripping ifc; what should I check? | bim_manager | request_opinion | software_choice | medium | false | [chat] Gives a short test plan (class counts, ids, properties, geometry, units) and offers to compare two files. Names no vendor as best. | S:zh-zhihu-s016 |
| ZH-20 | `幫我檢查這個IFC每層樓的樓地板面積總和，跟送審圖面積表對不對得上` | Check the sum of floor areas per storey in this IFC against the submission drawing's area table. | architect | validate_check | permitting_code_checking | medium | true | [IFC] Floor area per storey from stored quantities or spaces; needs the area table from the user to compare; asks for it. Traditional Chinese reply. | S:zh-tw-hk-s001 |
| ZH-21 | `座標是不是TWD97？原點對不對，有沒有設IfcMapConversion` | Are the coordinates TWD97? Is the origin right, and is IfcMapConversion set? | bim_coordinator | validate_check | coordinates_georef | hard | true | [IFC] Reports CRS name and map conversion as written; says whether TWD97 is mentioned; does not judge the origin without a reference. | S:zh-tw-hk-s010 |
| ZH-22 | `樓梯踏面跟級高有沒有符合建築技術規則？列出不合格的` | Do stair treads and risers meet the building technical regulations? List the non-compliant ones. | reviewer_authority | comply_regulation | permitting_code_checking | hard | true | [IFC] Reads riser and tread values; asks for the limits (or accepts the user's numbers); does not quote the regulation from memory. | S:zh-tw-hk-s012 |
| ZH-23 | `香港屋宇署BIM要用IFC2x3還是IFC4？Revit要選哪個MVD` | Does the HK Buildings Department BIM need IFC2x3 or IFC4? Which MVD to choose in Revit? | bim_coordinator | how_to | versions_mvd | medium | false | [chat] Says this is set by the current submission requirements; explains the MVD options generally; tells the user to confirm in the department's current guidance. | S:zh-tw-hk-s014 |
| ZH-24 | `revit2019导ifc点了没反应只出个schema文件，咋回事` | In Revit 2019, exporting ifc does nothing and only produces a schema file. What's going on? | architect | troubleshoot_export | export_revit | easy | false | [chat] Likely export/add-in problem; gives a short check list and asks for the error text or log. No invented fix. | S:zh-zhihu-s012 |
| ZH-25 | `ifc和rvt到底有啥区别？我直接导出ifc发给老师可以吗` | What is the real difference between ifc and rvt? Can I just export ifc and send it to my teacher? | student_beginner | understand_concept | learning_basics | easy | false | [chat] Plain explanation: rvt is Revit's own file, ifc is an open exchange file; yes if the teacher can open it, but check what the assignment asks. | S:p-student-s012 |
| ZH-26 | `ifcopenshell读出来的中文是\X2\开头的，怎么转成正常汉字` | Chinese strings read by IfcOpenShell start with `\X2\`; how do I convert them to normal characters? | developer_programmer | troubleshoot_code | encoding_text | medium | false | [chat] Explains that the library normally decodes this and shows the usual cause (reading raw text instead of through the API); short code idea. | S:enc-s012 |
| ZH-27 | `这个ifc有没有地理参考？IfcSite经纬度和IfcMapConversion有没有，没有的话给我原点和旋转怎么取` | Does this ifc have georeferencing? Does it have IfcSite lat/long and IfcMapConversion; if not, how do I get the origin and rotation? | developer_programmer | query_model_data | gis_citygml_digital_twin | medium | true | [IFC] Reports site lat/long and map conversion; if absent says so and describes where an origin and rotation would have to come from. | S:zh-csdn-dev-s015 |
| ZH-28 | `把dwg里A-WALL那层的双线墙翻成revit墙，先预览中心线和厚度再建，别建到一层去` | Turn the double-line walls on the A-WALL layer of the dwg into Revit walls; preview centerlines and thickness first, and don't put them on level 1. | architect | modify_model_data | levels_storeys | hard | true | [Revit] Reads the layer, shows centerlines and thickness, waits, then builds on the level the user names (asks which). Reads back level and count. | S:zh-aimcp-s008 |

---

## 3. Spanish (`ES`): Spain and Latin America

Two registers: Spain (tuteo, `mira a ver`, `mediciones`, `presupuesto`, BC3, CTE, Plan BIM) and Latin America (voseo in Argentina and Uruguay, `metrados` in Peru and Chile, `qué onda` in Mexico, Planbim in Chile). Accents are often dropped in real typing (`cuantos`, `que`); keep it.

| ID | Prompt | English gloss | Persona | Intent | Topic | Diff | File | Expected | Origin |
|---|---|---|---|---|---|---|---|---|---|
| ES-01 | `cuántos elementos quedaron como proxy en el ifc? y de qué categorías de revit venían` | How many elements ended up as proxy and from which Revit categories? | bim_coordinator | query_model_data | class_mapping | medium | true | [IFC] Count and grouping of IfcBuildingElementProxy, with suggestions only. Reply in Spanish. | S:es-latam-s001 |
| ES-02 | `creá cuatro muros de 3 m en rectángulo 5x4 y después contame cuántos hay` | Create four 3 m walls in a 5x4 rectangle and then tell me how many there are. | architect | modify_model_data | levels_storeys | easy | true | [Revit] Creates four walls, then counts all walls in the project (not just the four), reads back. Voseo kept in the reply is a plus, not a requirement. | S:es-aimcp-s016 / R:[es-aimcp-r031](https://github.com/joacos/archicad-mcp) |
| ES-03 | `necesito los metrados de muros, losas y columnas por nivel, m2 y m3, para el presupuesto de mañana` | I need quantity takeoffs of walls, slabs and columns per level, m2 and m3, for tomorrow's budget. | estimator_qs | extract_quantities | quantities_qto | medium | true | [IFC] Table by level and class with the quantity source stated; missing quantities listed. | S:es-latam-s003 |
| ES-04 | `importé el ifc de archicad en revit 2025 y las ventanas quedaron fuera del muro, en el 2024 andaba bien, qué onda` | I imported the Archicad ifc in Revit 2025 and the windows sit outside the wall; it worked in 2024. What's up? | architect | troubleshoot_import | import_into_revit | hard | true | [IFC] Checks window placement relative to the wall and the opening/fill relations; does not claim to know what changed between Revit versions. | S:es-latam-s004 |
| ES-05 | `revisa si el modelo cumple la MIDE de planbim, qué entidades no traen sus propiedades requeridas` | Check whether the model meets Planbim's MIDE; which entities lack the required properties? | reviewer_authority | comply_regulation | national_requirements | hard | true | [IFC] Needs the MIDE table (asks for it or a list of required properties); then reports gaps by entity. Does not invent the table's contents. | S:es-latam-s002 / R:[es-latam-r012](https://planbim.cl/documentos/mide/) |
| ES-06 | `agrégale a todas las luminarias la propiedad frecuencia_mantenimiento y que tome el valor del tipo` | Add the property frecuencia_mantenimiento to all luminaires and take the value from the type. | facility_manager | modify_model_data | cobie_fm_handover | hard | true | [IFC] Finds luminaires (IfcLightFixture), reads the type-level value, writes the property on a copy; reports those with no type value. | S:es-latam-s008 |
| ES-07 | `compara el ifc de hoy con el de la semana pasada, qué elementos nuevos, borrados y movidos` | Compare today's ifc with last week's: new, deleted and moved elements. | bim_coordinator | compare_versions | guid_change_tracking | hard | true | [IFC] Needs the two files; added, deleted, moved with counts by class. | S:es-latam-s009 |
| ES-08 | `el ifc pesa 800mb y no abre, se cuelga el visor, qué hago` | The ifc weighs 800 MB and won't open; the viewer hangs. What do I do? | structural_engineer | troubleshoot_viewing | viewers_opening | medium | false | [chat] Practical options (desktop viewer, split by storey, strip unneeded classes); offers to analyse the file if it can load it. | S:es-latam-s010 |
| ES-09 | `he exportado a ifc y no me salen los parametros compartidos en los psets, mira a ver cuales faltan en los muros` | I exported to ifc and my shared parameters don't appear in the psets; see which are missing on the walls. | architect | validate_check | psets_properties | hard | true | [IFC] Lists psets and properties actually on walls; the user did not list the parameter names, so after showing what exists it asks for two or three names. | S:es-spain-s002 |
| ES-10 | `tengo que entregar el modelo para una licitacion con Plan BIM, revisa que el IFC tenga todas las plantas, espacios y clasificacion en cada elemento` | I must deliver the model for a tender under Plan BIM; check the IFC has all the floors, spaces and a classification on every element. | bim_manager | validate_check | national_requirements | hard | true | [IFC] Three checks: storeys, spaces, classification coverage, with counts. Does not state what the Plan BIM requires. | S:es-spain-s003 |
| ES-11 | `los modelos genericos salen como proxy, pasalos a IfcColumn los que tengan 'pilar' en el nombre` | Generic models come out as proxy; turn those with "pilar" in the name into IfcColumn. | architect | modify_model_data | class_mapping | medium | true | [IFC] Previews matches, reclassifies on a copy, keeps GlobalIds, lists what remains proxy. | S:es-spain-s004 |
| ES-12 | `necesito mediciones de muros por planta en m2 y m3 para el presupuesto` | I need wall measurements per floor in m2 and m3 for the budget. | estimator_qs | extract_quantities | quantities_qto | medium | true | [IFC] Per-storey areas and volumes of walls, with source and missing flags. | S:es-spain-s007 |
| ES-13 | `para la entrega a mantenimiento, comprueba que los equipos tengan marca, modelo y numero de serie` | For handover to maintenance, check that equipment has make, model and serial number. | facility_manager | validate_check | cobie_fm_handover | medium | true | [IFC] Missing make, model and serial by equipment class; counts and examples. | S:es-spain-s011 |
| ES-14 | `revisa si los espacios tienen superficie y uso asignado para el CTE` | Check whether spaces have area and use assigned, for the CTE. | reviewer_authority | validate_check | permitting_code_checking | medium | true | [IFC] Spaces without area or use, counts; no statement of what the CTE demands. | S:es-spain-s013 |
| ES-15 | `exporté de revit a etabs por ifc y me sale error al importar, que config del exportador debo usar?` | I exported from Revit to ETABS via ifc and get an import error; which exporter settings should I use? | structural_engineer | troubleshoot_export | export_revit | medium | false | [chat] Asks for the exact error; if it is a truncated-file error (missing ENDSEC), says to check that the export completed. No invented ETABS settings. | S:es-err-s007 / R:[es-arch-r045](https://forums.buildingsmart.org/t/como-poder-exportar-un-modelo-3d-estructural-realizado-en-revit-a-etabs-por-medio-del-formato-ifc/2985) |
| ES-16 | `pon el modelo en ETRS89 UTM30N, este 440000 norte 4470000, y dime si queda coherente con el IfcSite` | Place the model in ETRS89 UTM 30N, east 440000 north 4470000, and tell me whether it is consistent with IfcSite. | bim_coordinator | modify_model_data | coordinates_georef | hard | true | [IFC] Writes a map conversion on a copy with those values, then compares with IfcSite lat/long (converted) and reports the difference; does not claim "coherent" without computing. | S:mul-coord-s011 |
| ES-17 | `necesito las mediciones por capitulos (muros, forjados, carpinteria) para pasarlas a presupuesto en bc3` | I need measurements by chapter (walls, slabs, joinery) to pass to a budget in BC3. | estimator_qs | extract_quantities | quantities_qto | hard | true | [IFC] Groups by chapter; a BC3 file is a specific format, so either produces it or says it can only give a table. | S:es-qto-s012 |
| ES-18 | `dime los ductos que cruzan vigas en el nivel 2 y de que sistema son, para mandar el BCF` | Tell me the ducts that cross beams on level 2 and what system they belong to, to send the BCF. | mep_engineer | coordinate_clash | clash_coordination_bcf | hard | true | [IFC] Intersections of ducts and beams on one storey with system names; BCF only if it has the tool. | S:es-mep-s009 |
| ES-19 | `dame todos los espacios con nombre y area, por planta, es para el plan de mantenimiento` | Give me all spaces with name and area, per floor, for the maintenance plan. | facility_manager | extract_quantities | spaces_rooms_areas | easy | true | [IFC] Table of spaces by storey; spaces without area marked. | S:en-fmor-s016 |
| ES-20 | `detecta colisiones entre la estructura y las instalaciones en este ifc, es para mi tarea de la uni` | Detect clashes between structure and MEP in this ifc; it's for my uni assignment. | student_beginner | coordinate_clash | clash_coordination_bcf | hard | true | [IFC] Runs a clash check if a tool exists (states tolerance and counts by pair); otherwise says it cannot; explains results in simple Spanish. | S:p-student-s013 |

---

## 4. Portuguese (`PT`): mostly Brazilian

The data is Brazilian (`pt-BR` and `pt`). Typical words: `compatibilização`, `pavimento`, `quantitativo`, `apontamentos`, `cara olha`. European Portuguese is not represented in the data.

| ID | Prompt | English gloss | Persona | Intent | Topic | Diff | File | Expected | Origin |
|---|---|---|---|---|---|---|---|---|---|
| PT-01 | `cara olha o ifc e me fala quantos elementos viraram proxy e de qual categoria do revit, preciso mandar a compatibilização hoje` | Look at the ifc and tell me how many elements became proxy and from which Revit category; I have to send the coordination today. | bim_coordinator | validate_check | class_mapping | medium | true | [IFC] Counts and groups proxies; short table; Brazilian Portuguese reply. | S:pt-brazil-s001 |
| PT-02 | `exportei do revit e sumiram meus parametros compartilhados no IFC. quais elementos ficaram sem pset customizado?` | I exported from Revit and my shared parameters vanished in the IFC. Which elements have no custom pset? | bim_coordinator | validate_check | psets_properties | medium | true | [IFC] Elements without any non-standard pset, by class; lists the custom psets that do exist. | S:pt-brazil-s002 |
| PT-03 | `lista os pavimentos do ifc com a cota e vê se os nomes batem com o padrão do BEP (Térreo, 1º Pav, etc)` | List the storeys with elevation and check the names match the BEP pattern (Ground floor, 1st floor, etc.). | architect | query_model_data | levels_storeys | easy | true | [IFC] Storeys with elevations; compares names to the pattern the user gave; flags the odd ones. | S:pt-brazil-s004 |
| PT-04 | `preciso do quantitativo de área de parede e volume de concreto por pavimento pra planilha de orçamento` | I need wall area and concrete volume takeoff per storey for the budget spreadsheet. | estimator_qs | extract_quantities | quantities_qto | medium | true | [IFC] Per-storey table, source stated, missing flagged. | S:pt-brazil-s005 |
| PT-05 | `roda clash entre dutos e vigas da estrutura e gera os apontamentos em BCF pra mandar pro projetista` | Run a clash between ducts and structural beams and generate BCF issues to send the designer. | bim_coordinator | coordinate_clash | clash_coordination_bcf | hard | true | [IFC] Needs a clash tool; groups by level; BCF with viewpoints; otherwise an honest "cannot". | S:pt-brazil-s007 |
| PT-06 | `as portas e janelas não estão furando as paredes no ifc, vê quais não tem abertura` | The doors and windows are not cutting the walls in the ifc; see which have no opening. | architect | troubleshoot_viewing | openings_voids | hard | true | [IFC] Doors and windows with no opening or void relation; counts and GlobalIds. | S:pt-brazil-s009 |
| PT-07 | `me mostra as propriedades do pilar P12: seção, fck e em qual pavimento tá` | Show me the properties of column P12: section, fck, and which storey it's on. | contractor_site | query_model_data | psets_properties | easy | true | [IFC] Finds the column by name or tag, shows profile, material or concrete strength, storey; says if fck is not stored. | S:pt-brazil-s010 |
| PT-08 | `meu IFC tá com 800mb, o que tá pesando? tem muita coisa duplicada?` | My IFC is 800 MB; what's heavy? Is much of it duplicated? | bim_coordinator | optimize_performance | file_size_performance | hard | true | [IFC] Weight by class, duplicated geometry detection if possible, honest about limits on a big file. | S:pt-brazil-s011 |
| PT-09 | `como deixar o ifc georreferenciado em SIRGAS 2000 saindo do revit? coordenada compartilhada n funciona` | How do I get the ifc georeferenced in SIRGAS 2000 from Revit? Shared coordinates don't work. | architect | how_to | coordinates_georef | medium | false | [chat] Steps in general terms (shared coordinates, base point, export option); offers to read the exported file's map conversion to see what came out. | S:mul-coord-s012 |
| PT-10 | `quais elementos do pavimento 2 ainda nao tem atividade no cronograma? preciso pro 4D da obra` | Which elements of floor 2 have no activity in the schedule yet? I need it for the 4D. | contractor_site | query_model_data | scheduling_4d_cost_5d | hard | true | [IFC] Needs work-schedule data in the model; if none exists, says so instead of listing all elements. | S:pt-s010 |
| PT-11 | `adiciona a classificação NBR 15965 nas paredes pelo nome do tipo, usa a tabela que te passei` | Add the NBR 15965 classification to the walls by type name, using the table I gave you. | bim_manager | modify_model_data | classification_bsdd | hard | true | [IFC] Needs the table; applies by type name on a copy; reports matched and unmatched types. No codes invented. | S:pt-classbsdd-s012 |
| PT-12 | `no revit 2023 o IfcExportAs parou de funcionar, tudo sai como proxy. qual parametro uso agora?` | In Revit 2023 IfcExportAs stopped working and everything is proxy. Which parameter do I use now? | bim_manager | how_to | class_mapping | medium | false | [chat] Describes the mapping options without asserting version-specific facts it is unsure of; offers to count proxies in the exported file. | S:pt-proxy-s006 |
| PT-13 | `tem como ver quais elementos tao sem os campos obrigatorios do cobie? preciso entregar pro cliente` | Can you see which elements lack the required COBie fields? I must deliver to the client. | bim_coordinator | validate_check | cobie_fm_handover | medium | true | [IFC] Checks type, space, manufacturer and serial by class; says it is not a full COBie conformance test. | S:pt-cobie-s012 |
| PT-14 | `preciso da lista de equipamentos com tag, ambiente e fabricante pra entrega do FM, em planilha` | I need an equipment list with tag, room and manufacturer for the FM handover, in a spreadsheet. | facility_manager | extract_quantities | cobie_fm_handover | medium | true | [IFC] Equipment table with the three columns saved as a spreadsheet; blanks marked. | S:pt-data-s011 |
| PT-15 | `compara o IFC estrutural do Eberick com o da arquitetura, quantos pilares, vigas e lajes por pavimento em cada um` | Compare the structural IFC from Eberick with the architectural one: how many columns, beams and slabs per storey in each. | structural_engineer | compare_versions | export_other_tools | hard | true | [IFC] Two files; per-storey counts side by side; notes storey naming differences between the two. | S:pt-brazil-s003 |

---

## 5. German (`DE`): Germany, Austria, Switzerland

Rows use `prüf mal`, `zeig mir`, `kannst du`, DACH terms (`AIA`, `BAP`, `TGA`, `Durchbruch` vs `Aussparung`, `LV`, `KG` after DIN 276, `NGF`, `Rechtswert/Hochwert`, `OKRD/OKFF` for slab-top vs finished-floor levels), and sometimes ASCII spelling (`ae`, `ue`) as typed in real chat.

| ID | Prompt | English gloss | Persona | Intent | Topic | Diff | File | Expected | Origin |
|---|---|---|---|---|---|---|---|---|---|
| DE-01 | `wieviele IfcBuildingElementProxy sind in dem Export und aus welchen Revit-Kategorien kommen die? Mapping stimmt irgendwie nicht` | How many proxies are in the export and which Revit categories do they come from? The mapping is off somehow. | bim_coordinator | query_model_data | class_mapping | medium | true | [IFC] Counts and groups proxies; German reply, IFC terms unchanged. | S:de-dach-s002 |
| DE-02 | `wo sitzt der Projektbasispunkt in der IFC und stimmt die Nordrichtung? Fachmodelle passen nicht übereinander` | Where is the project base point in the IFC and is the north direction right? Discipline models don't line up. | bim_coordinator | validate_check | coordinates_georef | hard | true | [IFC] Reads site placement, true north, map conversion; says it cannot know the Revit base point from the IFC alone, only what the file contains. | S:de-dach-s003 |
| DE-03 | `prüf mal ob bei allen Wänden Tragend, Feuerwiderstand und Außenwand befüllt sind, sonst fliegen wir beim AIA-Check raus` | Check that all walls have load-bearing, fire resistance and external filled in, otherwise we fail the AIA check. | bim_manager | validate_check | psets_properties | medium | true | [IFC] Maps the three German terms to LoadBearing, FireRating, IsExternal; reports counts of empty values. | S:de-dach-s004 |
| DE-04 | `meine eigenen Parameter kommen in der IFC nicht an obwohl Häkchen bei benutzerdefinierte Psets gesetzt ist, woran liegts` | My own parameters don't arrive in the IFC although "user-defined psets" is ticked; why? | architect | troubleshoot_export | psets_properties | medium | false | [chat] Common causes (mapping file path and format, parameter names); offers to check which psets exist in the exported file. | S:de-dach-s005 |
| DE-05 | `Elemente auf OKRD-Ebenen bitte dem jeweiligen OKFF-Geschoss zuordnen, wir haben pro Geschoss zwei Ebenen` | Assign elements on OKRD levels to the matching OKFF storey; we have two levels per floor. | bim_coordinator | modify_model_data | levels_storeys | hard | true | [IFC] Needs the pairing rule (by name or elevation); previews, applies on a copy, counts moved. | S:de-dach-s006 |
| DE-06 | `Wandflächen und Volumen je Geschoss als Liste fürs LV, nur Außenwände. werden Öffnungen abgezogen? bitte angeben` | Wall areas and volumes per storey as a list for the bill of quantities, external walls only. Are openings deducted? Please state. | estimator_qs | extract_quantities | quantities_qto | medium | true | [IFC] External walls via IsExternal; states if openings are deducted in the stored quantity or in its own calculation. | S:de-dach-s007 |
| DE-07 | `vergleich mal Stand 12 und Stand 14 vom Rohbau-IFC. was ist neu, was weg, was verschoben? GUIDs ändern sich bei uns teilweise` | Compare revision 12 and 14 of the shell IFC. What is new, gone, moved? Our GUIDs partly change. | bim_coordinator | compare_versions | guid_change_tracking | hard | true | [IFC] Matches by GlobalId and falls back to type/position where ids changed; states which method per element. | S:de-dach-s008 |
| DE-08 | `welche Lüftungskanäle > 300 mm durchdringen F90 Wände? mit Geschoss und Position` | Which ventilation ducts larger than 300 mm pass through F90 walls? With storey and position. | mep_engineer | coordinate_clash | openings_voids | hard | true | [IFC] Needs wall fire rating (F90 = 90 min) and duct size; says if the rating is stored in a differently named property; lists ducts with storey and position. | S:de-dach-s009 |
| DE-09 | `die Stützen sind alle als Proxy drin, kannst du die zu IfcColumn machen? Name fängt mit ST_ an` | The columns are all proxies; can you make them IfcColumn? The name starts with ST_. | bim_coordinator | modify_model_data | class_mapping | medium | true | [IFC] Previews the ST_* proxies, reclassifies on a copy, keeps psets and ids, lists non-matching proxies. | S:de-dach-s012 |
| DE-10 | `Raumliste mit Nutzung und Fläche für die FM-Übergabe, Räume ohne Namen markieren` | Room list with use and area for FM handover; mark rooms without names. | facility_manager | extract_quantities | cobie_fm_handover | easy | true | [IFC] Table of spaces with use and area; unnamed rooms flagged. | S:de-dach-s014 |
| DE-11 | `hat jedes Bauteil eine Kostengruppe DIN 276? zeig mir die ohne KG` | Does every element have a DIN 276 cost group? Show me those without. | bim_manager | validate_check | classification_bsdd | medium | true | [IFC] Counts elements with and without a cost-group classification or property; lists by class. | S:de-classbsdd-s013 |
| DE-12 | `welche Wände haben keine Feuerwiderstandsklasse? Liste mit GUID und Geschoss raus als csv, Semikolon als Trenner bitte` | Which walls have no fire-resistance class? List with GUID and storey as csv, semicolon as separator please. | bim_coordinator | query_model_data | psets_properties | easy | true | [IFC] CSV with `;` separator (German Excel), columns GlobalId and storey; reports the path. | S:de-data-s012 |
| DE-13 | `zeig mir alle Leitungen TGA die durch Wände/Decken gehen und noch keinen Durchbruch haben, DN und Wandstärke dazu` | Show me all MEP lines that go through walls and slabs and have no opening yet, with nominal diameter and wall thickness. | mep_engineer | coordinate_clash | openings_voids | hard | true | [IFC] Intersections minus existing openings; DN and thickness columns; states tolerance and method. | S:de-openings-s007 |
| DE-14 | `mach mal Kollisionsprüfung TGA gegen Tragwerk im Koordinationsmodell, Toleranz 10 mm, pro Geschoss gruppieren und als BCF raus` | Run a clash check MEP vs structure in the coordination model, tolerance 10 mm, grouped by storey, BCF out. | bim_coordinator | coordinate_clash | clash_coordination_bcf | hard | true | [IFC] Needs a clash tool; counts per storey; BCF; honest "cannot" if no tool. | S:de-clash-s012 |
| DE-15 | `AG fordert IFC4 Reference View. Prüf mal ob die Datei wirklich RV ist und nicht 2x3 oder IFC4x3` | The client demands IFC4 Reference View. Check whether the file really is RV and not 2x3 or IFC4x3. | bim_manager | validate_check | versions_mvd | easy | true | [IFC] Header schema and view definition; evidence and caveat that headers can be wrong. | S:de-vm-s010 |
| DE-16 | `meine Fundamentwände aus dem Wandwerkzeug werden IfcWall statt IfcFooting` | My foundation walls made with the wall tool come out as IfcWall instead of IfcFooting. | architect | troubleshoot_export | class_mapping | medium | false | [chat] Explains class mapping by family/type and category; offers to find the foundation walls in the file and show their current class. | R:[en-blogs-linkedin-r006](https://bim-me-up.com/wand-als-ifcfooting-exportieren/) |
| DE-17 | `wie krieg ich die Farben von Archicad IFC in Revit rueber? Oberflaechen sind alle grau` | How do I get the colours of the Archicad IFC across into Revit? Surfaces are all grey. | architect | how_to | materials_colors_styles | medium | true | [IFC] Checks that surface styles exist in the file and how they are attached; then a short explanation of the import side. | S:mx-mcl-s015 |
| DE-18 | `was ist der Unterschied zwischen Reference View und Design Transfer View? welche nimmt man fürs Austauschen mit dem TGA Planer` | What is the difference between Reference View and Design Transfer View? Which one for exchange with the MEP planner? | student_beginner | understand_concept | versions_mvd | easy | false | [chat] Plain comparison; says the receiving software and project requirements decide. | S:de-dach-s010 |
| DE-19 | `kannst du pruefen ob Waende, Decken und Dach als IfcWall/IfcSlab/IfcRoof drin sind und nicht als Proxy? Tragwerksplaner braucht das heute noch` | Can you check that walls, slabs and roof are IfcWall, IfcSlab, IfcRoof and not proxy? The structural engineer needs it today. | architect | validate_check | export_archicad | medium | true | [IFC] Counts the three classes and proxies by name pattern; reports mismatches. | S:de-arch-s008 |

---

## 6. French (`FR`)

French uses `maquette` for the model, `convention BIM`, `DOE`, `GMAO`, `DPGF`, `PMR`, Lambert 93, and tutoiement with an assistant (`dis moi`, `fais moi`). Accents and hyphens are often dropped when typing fast.

| ID | Prompt | English gloss | Persona | Intent | Topic | Diff | File | Expected | Origin |
|---|---|---|---|---|---|---|---|---|---|
| FR-01 | `dis moi quels murs n'ont pas de résistance au feu renseignée dans la maquette, la convention BIM l'exige` | Tell me which walls have no fire resistance filled in; the BIM convention requires it. | bim_coordinator | validate_check | psets_properties | medium | true | [IFC] Walls with an empty or missing fire-rating property, by storey, with GlobalIds. French reply. | S:fr-francophone-s001 |
| FR-02 | `j'ai plein de proxy dans mon IFC, c'est quoi comme catégories revit ? faut que je corrige la table de correspondance` | I have lots of proxies in my IFC; which Revit categories are they? I need to fix the mapping table. | bim_manager | query_model_data | class_mapping | medium | true | [IFC] Count and group proxies by source category; suggests mapping corrections. | S:fr-francophone-s002 |
| FR-03 | `donne moi la surface par niveau des pièces (IfcSpace), SDP et surface utile si dispo` | Give me the area per level of the rooms (IfcSpace), floor area (SDP) and usable area if available. | architect | extract_quantities | spaces_rooms_areas | easy | true | [IFC] Per-level totals from spaces; for "SDP" (surface de plancher) says it is a regulatory measure not stored as a single IFC value, reports what is available. | S:fr-francophone-s003 |
| FR-04 | `vérifie que les niveaux sont nommés comme dans la convention BIM (RDC, R+1...) et que les altitudes sont cohérentes` | Check that the levels are named as in the BIM convention (ground floor, R+1...) and elevations are consistent. | bim_manager | validate_check | levels_storeys | medium | true | [IFC] Storey names vs the pattern given; elevations in order and in sensible steps; lists oddities. | S:fr-francophone-s004 |
| FR-05 | `compare l'indice B et l'indice C de la maquette, je veux les éléments ajoutés/supprimés/modifiés avant la synthèse` | Compare revision B and C of the model; I want added, removed, modified elements before the synthesis meeting. | bim_coordinator | compare_versions | guid_change_tracking | hard | true | [IFC] Added, removed, modified with counts by class; method for "modified" stated. | S:fr-francophone-s005 |
| FR-06 | `mon IFC est décalé de plusieurs km dans le viewer, regarde le géoréférencement RGF93 / Lambert 93 de la maquette` | My IFC is shifted by several km in the viewer; look at the model's RGF93 / Lambert 93 georeferencing. | bim_coordinator | validate_check | coordinates_georef | hard | true | [IFC] Reports map conversion and CRS name as written; says whether EPSG:2154 is stated; does not guess. | S:fr-francophone-s010 |
| FR-07 | `fais moi la liste des équipements avec fabricant et référence pour le DOE / GMAO` | Make me the equipment list with manufacturer and reference for the as-built file / CMMS. | facility_manager | extract_quantities | cobie_fm_handover | medium | true | [IFC] Equipment table; blanks marked; saved as a spreadsheet. | S:fr-francophone-s011 |
| FR-08 | `pourquoi mes paramètres partagés sortent pas dans l'IFC ? j'ai coché pset personnalisé` | Why don't my shared parameters come out in the IFC? I ticked custom pset. | architect | troubleshoot_export | psets_properties | medium | false | [chat] Likely causes (mapping file, names); offers to list the psets in an exported file. | S:fr-francophone-s013 |
| FR-09 | `fais un clash gaines vs structure, tolérance 2 cm, et sors les points en BCF` | Run a clash of ducts vs structure, tolerance 2 cm, and output the points as BCF. | bim_coordinator | coordinate_clash | clash_coordination_bcf | hard | true | [IFC] Needs a clash tool; reports counts; BCF; or an honest "cannot". | S:fr-francophone-s017 |
| FR-10 | `je dois sortir les métrés pour le DPGF : surfaces de murs nettes des ouvertures par niveau, et le nb de portes par type` | I must produce quantities for the DPGF: wall areas net of openings per level, and the number of doors by type. | estimator_qs | extract_quantities | quantities_qto | medium | true | [IFC] Net wall area per level (source stated) and door count by type. | S:fr-s012 |
| FR-11 | `vérifie l'accessibilité PMR : portes < 90 cm et couloirs < 1,40 m dans la maquette, liste avec niveau` | Check accessibility: doors under 90 cm and corridors under 1.40 m in the model, list with level. | reviewer_authority | comply_regulation | permitting_code_checking | hard | true | [IFC] Uses the user's limits as given; doors by width; corridor widths are hard to read from an IFC, so it says what it can and cannot measure. | S:fr-permit-s014 |
| FR-12 | `mon obj exporté depuis l'ifc n'a plus aucune couleur, pourquoi ?` | My obj exported from the ifc has no colours any more; why? | student_beginner | troubleshoot_viewing | materials_colors_styles | medium | false | [chat] The OBJ format keeps colours in a separate material file; checks that the IFC has styles if the file is loaded. | S:fr-viewconv-s010 |
| FR-13 | `IfcConvert plante avec 'to_bytes error', y'a des accents dans le header, tu peux corriger le fichier ?` | IfcConvert crashes with 'to_bytes error'; there are accents in the header; can you fix the file? | developer_programmer | troubleshoot_code | encoding_text | medium | true | [IFC] Finds accented characters in the header, shows them, fixes on a copy (escaped form), re-reads. | S:fr-err-s010 / R:[en-gh-encoding-r018](https://github.com/IfcOpenShell/IfcOpenShell/issues/1016) |

---

## 7. Italian (`IT`)

Italian rows use `capitolato informativo`, `computo metrico`, `piano` for storey, `forature`, and the accent-less `e` for `è` (real typing).

| ID | Prompt | English gloss | Persona | Intent | Topic | Diff | File | Expected | Origin |
|---|---|---|---|---|---|---|---|---|---|
| IT-01 | `quanti IfcBuildingElementProxy ci sono nel modello? da che categorie Revit arrivano?` | How many proxies are in the model and which Revit categories do they come from? | bim_coordinator | query_model_data | class_mapping | medium | true | [IFC] Count and grouping. Italian reply. | S:it-italy-s001 |
| IT-02 | `i modelli non si sovrappongono. controlla IfcSite lat/long/quota e il CRS e dimmi se l'origine e sballata` | The models don't overlap. Check IfcSite lat/long/elevation and the CRS and tell me if the origin is off. | bim_coordinator | validate_check | coordinates_georef | hard | true | [IFC] Reads site coordinates, CRS and extents; compares both files if two are loaded. | S:it-italy-s003 |
| IT-03 | `confronta rev A e rev B, cosa e stato aggiunto/rimosso/modificato per GUID?` | Compare rev A and rev B: what was added, removed, modified by GUID? | bim_coordinator | compare_versions | guid_change_tracking | hard | true | [IFC] Added, removed, modified, with counts by class. | S:it-italy-s004 |
| IT-04 | `verifica se il modello rispetta il capitolato informativo: classificazione, materiali, FireRating su tutti i muri` | Check whether the model meets the information requirements: classification, materials, FireRating on all walls. | reviewer_authority | comply_regulation | national_requirements | hard | true | [IFC] Three checks with counts; the capitolato is not available, so only the three named items are tested and it says so. | S:it-italy-s007 |
| IT-05 | `mi serve il computo metrico dai muri e solai per piano, con m2 e m3, e dimmi se ci sono elementi senza quantita` | I need the bill of quantities from walls and slabs per floor, m2 and m3, and tell me if some elements have no quantities. | estimator_qs | extract_quantities | quantities_qto | medium | true | [IFC] Table per storey plus a list of elements without quantities. | S:it-s015 |
| IT-06 | `i proxy con nome 'Pilastro' mettili come IfcColumn` | Make the proxies named "Pilastro" into IfcColumn. | bim_coordinator | modify_model_data | class_mapping | hard | true | [IFC] Previews matches, reclassifies on a copy, keeps GlobalIds. | S:it-italy-s009 |
| IT-07 | `volume solai per piano, mi servono per il computo oggi` | Slab volume per floor, I need it for the quantities today. | contractor_site | extract_quantities | quantities_qto | easy | true | [IFC] Slab volume per storey with source. | S:it-italy-s017 |
| IT-08 | `controlla se l'ifc è georeferenziato in EPSG:7791 e se la rotazione rispetto al nord è coerente con l'IfcSite` | Check whether the ifc is georeferenced in EPSG:7791 and whether the rotation to north is consistent with IfcSite. | bim_coordinator | validate_check | coordinates_georef | hard | true | [IFC] Reports the CRS name or code as written, rotation, and site true north; compares them; no assumption about 7791. | S:mul-coord-s017 |
| IT-09 | `quando esporto in csv i decimali con il punto diventano testo in excel italiano, come lo sistemo?` | When I export to csv, decimals with a dot become text in Italian Excel; how do I fix it? | bim_coordinator | troubleshoot_export | data_extraction_analytics | easy | false | [chat] Explains the locale issue (decimal comma, separator) and offers to write the file with a semicolon and comma decimals. | S:it-data-s016 |
| IT-10 | `controlla se nel modello analitico ci sono vincoli e carichi assegnati, altrimenti SCIA non lo calcola` | Check whether the analytical model has supports and loads assigned, otherwise SCIA can't calculate it. | structural_engineer | validate_check | structural_analytical | hard | true | [IFC] Counts structural members, supports, load cases; says if the file has no analysis model at all. | S:it-struct-s017 |
| IT-11 | `come georeferenzio un ifc cosi lo vedo in qgis al posto giusto? uso bonsai, EPSG 3003` | How do I georeference an ifc so I see it in QGIS in the right place? I use Bonsai, EPSG 3003. | civil_infra_engineer | how_to | gis_citygml_digital_twin | easy | false | [chat] Explains map conversion and CRS in simple steps; offers to write the values if the user gives eastings, northings, rotation. | S:it-gis-s018 |
| IT-12 | `come verifico che porte e muri abbiano FireRating e trasmittanza prima di consegnare l'IFC?` | How do I check that doors and walls have FireRating and transmittance before delivering the IFC? | bim_manager | validate_check | psets_properties | medium | true | [IFC] Does the check on the loaded file (FireRating and the thermal property in Pset_*Common), counts missing. | R:[it-italy-r008](https://biblus.acca.it/bim-validation-modelli-ifc/) |
| IT-13 | `ho due revisioni dello stesso IFC, come vedo cosa e cambiato (aggiunti, rimossi, modificati)?` | I have two revisions of the same IFC; how do I see what changed (added, removed, modified)? | bim_coordinator | compare_versions | guid_change_tracking | medium | true | [IFC] If both are loaded, does the comparison; otherwise explains the method and asks for the files. | R:[it-italy-r009](https://biblus.acca.it/rilevare-modifiche-nei-modelli-ifc/) |

---

## 8. Japanese (`JA`)

Japanese real posts are mostly Zenn articles; typed requests to an AI are short plain-form imperatives (`〜して`, `〜出して`) mixed with Latin identifiers. Terms: 確認申請 (building confirmation application), 積算 (cost estimating), 平面直角座標系 (plane rectangular coordinate system, zones I to XIX).

| ID | Prompt | English gloss | Persona | Intent | Topic | Diff | File | Expected | Origin |
|---|---|---|---|---|---|---|---|---|---|
| JA-01 | `このIFC、IfcBuildingElementProxyが何個あるか数えて、元のRevitカテゴリ別に集計して。マッピング直す対象知りたい` | Count the proxies in this IFC and group them by original Revit category; I want to know what to fix in the mapping. | bim_coordinator | query_model_data | class_mapping | medium | true | [IFC] Count and grouping; Japanese reply. | S:ja-japan-s001 |
| JA-02 | `確認申請用に出したIFCの全IfcSpaceについて、部屋名・用途・床面積が入ってるか確認して。抜けてる部屋は一覧で` | For the IFC submitted for building confirmation, check every IfcSpace has room name, use and floor area; list the rooms that lack any. | reviewer_authority | validate_check | spaces_rooms_areas | medium | true | [IFC] Table of spaces missing each of the three; no statement about acceptance. | S:ja-japan-s002 |
| JA-03 | `IFCに出したら半分くらい要素が無い…Revitの元モデルと比べて何が落ちてるか調べて。階に紐づいてないやつとか` | Half of the elements are missing after export to IFC. Compare with the Revit source and find what dropped, e.g. things not tied to a floor. | architect | troubleshoot_export | export_revit | hard | true | [either] Counts elements by class and storey in the IFC; a real comparison needs the Revit side; says so if it is not connected. | S:ja-japan-s003 |
| JA-04 | `積算用に、階ごとのRC壁・柱・梁のコンクリ体積を合計して。Qtoが無いものは形状から出せる？` | For estimating, total RC wall, column and beam concrete volume per floor. Can you compute from geometry where there's no Qto? | estimator_qs | extract_quantities | quantities_qto | hard | true | [IFC] Per-storey volumes from Qto; offers or performs geometry computation for the rest and labels them separately. | S:ja-japan-s004 |
| JA-05 | `うちのIDSで納品IFCをチェックして。壁にFireRatingが入ってないものと、PredefinedType未設定のものを出して` | Check the delivered IFC with our IDS: walls without FireRating and elements with PredefinedType unset. | bim_manager | validate_check | ids_requirements | medium | true | [IFC] Needs the IDS; reports both failure types separately with GlobalIds. | S:ja-japan-s005 |
| JA-06 | `先週のIFCと今日のIFC比べて、追加・削除・変更された部材をGlobalIdベースで出して。変更は属性か形状かも` | Compare last week's IFC and today's: added, removed, changed members by GlobalId, and whether the change is attribute or geometry. | bim_coordinator | compare_versions | guid_change_tracking | hard | true | [IFC] Three lists, each change labelled attribute or geometry. | S:ja-japan-s006 |
| JA-07 | `天井内のダクトと梁の干渉探して、BCFにして出して。クリアランス50mmで` | Find clashes between ducts and beams in the ceiling space and output as BCF, with 50 mm clearance. | contractor_site | coordinate_clash | clash_coordination_bcf | hard | true | [IFC] Needs a clash tool; clearance check, not only hard clashes; BCF or honest "cannot". | S:ja-japan-s008 |
| JA-08 | `IFCの面積がRevitの集計表と合わない。単位か境界の問題？部屋ごとに差を出して` | IFC areas don't match the Revit schedule. A unit or boundary issue? Give the difference per room. | architect | troubleshoot_export | spaces_rooms_areas | hard | true | [either] IFC side: area per space with units. The difference to Revit needs the Revit schedule values (from Revit or pasted); asks for them. | S:ja-japan-s010 |
| JA-09 | `鉄骨の梁をプロファイル別に本数と重量集計して。H-400x200とか` | Total steel beams by profile, count and weight, e.g. H-400x200. | structural_engineer | extract_quantities | rebar_steel_precast | medium | true | [IFC] Groups IfcBeam by profile name; weight from stored quantities or profile area x density, with the method. | S:ja-japan-s012 |
| JA-10 | `平面直角座標系の第9系でIFC出力したら原点からめちゃ遠い、どう直す？測量点と基準点の違いも` | After exporting the IFC in plane rectangular CRS zone IX it's far from the origin; how do I fix it? Also, survey point vs base point. | bim_coordinator | how_to | coordinates_georef | medium | false | [chat] Explains the two points and the usual remedies in simple steps; offers to measure the offset in the exported file. | S:mul-coord-s015 |
| JA-11 | `部屋名が空のものを一覧にして、変更案を出してから反映してください` | List the rooms with empty names, propose changes, and apply them after that. | bim_manager | automate_batch | revit_api_automation | medium | true | [Revit] List first, proposal, wait for approval, then write. | S:ja-aimcp-s014 |
| JA-12 | `このIFC、ブラウザビューアで開けない。重すぎ？どの要素が原因か見て` | This IFC won't open in the browser viewer. Too heavy? Look at which elements cause it. | bim_coordinator | troubleshoot_viewing | file_size_performance | hard | true | [IFC] Size and weight per class; heavy elements; says if it hit a limit. | S:ja-err-s011 |
| JA-13 | `MacでIFCを開ける無料のビューアってありますか？属性も見たいです` | Is there a free IFC viewer for Mac? I also want to see properties. | architect | find_tool | viewers_opening | easy | false | [chat] A short list of real options with an honest note about what it has not verified. | S:ja-viewconv-s013 |
| JA-14 | `IfcCSVだとAttributeしか出ないから、PropertySetとMaterialも一緒にExcelに書き出して` | IfcCSV only outputs attributes; write the property sets and materials to Excel as well. | developer_programmer | convert_format | data_extraction_analytics | medium | true | [IFC] One workbook or sheet per element class with attributes, psets, material; reports file path and row counts. | R:[ja-japan-r001](https://zenn.dev/miyamiyaumya/articles/19a4247133dde6) |

---

## 9. Korean (`KO`)

Korean rows use `레빗` for Revit, `해줘` / `줘` endings, `ㅠㅠ` as emotion, and Latin identifiers. Permit workflow: the Korean building-permit portal (세움터). Politeness levels vary: `-해줘`, `-해주세요`, `-돼요?`.

| ID | Prompt | English gloss | Persona | Intent | Topic | Diff | File | Expected | Origin |
|---|---|---|---|---|---|---|---|---|---|
| KO-01 | `이 ifc에 IfcBuildingElementProxy 몇 개야? 레빗 카테고리별로 나눠줘` | How many IfcBuildingElementProxy in this ifc? Split by Revit category. | bim_coordinator | query_model_data | class_mapping | medium | true | [IFC] Count and grouping; Korean reply. | S:ko-korea-s001 |
| KO-02 | `레빗에서 내보낸 ifc인데 공유 매개변수가 속성에 하나도 안 보여. 어떤 객체에 Pset이 비어있는지 확인해줘` | An ifc from Revit; none of the shared parameters show as properties. Check which objects have empty Psets. | bim_coordinator | validate_check | psets_properties | hard | true | [IFC] Elements with no custom pset, by class; lists the psets that exist. | S:ko-korea-s002 |
| KO-03 | `발주처 BIM 지침 기준으로 층/공간/부재 분류 누락된 거 있나 체크해줘` | Check against the client's BIM guideline whether any storey/space/element classification is missing. | owner_client | comply_regulation | national_requirements | hard | true | [IFC] The guideline is not available, so it asks for it or checks the three named items and says so. | S:ko-korea-s003 |
| KO-04 | `층별 콘크리트 물량 m3로 정리해줘 슬래브 벽 기둥 따로` | Concrete quantity per floor in m3, slab, wall, column separately. | contractor_site | extract_quantities | quantities_qto | medium | true | [IFC] Table by storey and class, source stated. | S:ko-korea-s006 |
| KO-05 | `proxy로 나온 것 중 이름에 '기둥' 들어간거 IfcColumn으로 바꿔줘` | Among the proxies, change those with "기둥" (column) in the name to IfcColumn. | bim_coordinator | modify_model_data | class_mapping | hard | true | [IFC] Previews matches, reclassifies on a copy, counts. | S:ko-korea-s007 |
| KO-06 | `어제 올린 ifc랑 오늘 거 비교해서 추가/삭제/변경된 부재 알려줘` | Compare yesterday's uploaded ifc with today's; tell me added/deleted/changed members. | bim_manager | compare_versions | guid_change_tracking | hard | true | [IFC] Needs two files; added, deleted, changed with counts. | S:ko-korea-s009 |
| KO-07 | `ifc 레빗으로 링크하니까 한글이 깨지고 너무 느려요 ㅠㅠ` | Linking the ifc into Revit garbles the Korean text and is very slow. | bim_coordinator | troubleshoot_import | encoding_text | hard | true | [IFC] Checks how Korean strings are stored (escaped Unicode vs raw bytes) and the file size; explains which part it can judge; no promise about Revit. | S:ko-korea-s014 |
| KO-08 | `IDS 파일 기준으로 이 모델 검증하고 실패한 객체 알려줘` | Validate this model against the IDS file and tell me the failing objects. | reviewer_authority | validate_check | ids_requirements | medium | true | [IFC] Needs an IDS; failing elements grouped by specification. | S:ko-korea-s015 |
| KO-09 | `인허가용 IFC 내보내기 할 때 어떤 변환 설정 써야 돼요? 세움터에 올릴 건데` | Which conversion settings should I use when exporting IFC for the permit? I'll upload it to Seumteo. | architect | how_to | permitting_code_checking | medium | false | [chat] Must not invent the portal's requirements; points to the portal's current guideline and offers to check an exported file for general quality. | S:ko-arch-s018 |
| KO-10 | `레빗에서 IFC 내보내기 하면 '복구할 수 없는 오류' 뜨는데 어떻게 해요?` | Exporting IFC from Revit shows an "unrecoverable error"; what do I do? | architect | troubleshoot_export | export_revit | easy | false | [chat] Asks for the Revit and exporter version and the log; gives a short generic check list; no invented fix. | S:ko-err-s012 |
| KO-11 | `교량 IFC 4.3 모델에서 교각 목록이랑 선형 기준 거리(DistanceAlong) 뽑아줘` | From the bridge IFC 4.3 model, list the piers and their distance along the alignment. | civil_infra_engineer | query_model_data | infrastructure_ifc43 | hard | true | [IFC4.3] Lists piers and linear placement distances; says if linear placement is not used. | S:ko-infra-s015 |
| KO-12 | `IFC 파일이 뭐예요? 레빗 없이 열려면 어떻게 해요?` | What is an IFC file? How do I open it without Revit? | student_beginner | understand_concept | learning_basics | easy | false | [chat] One plain explanation and two viewer options with honest caveats. | S:p-student-s018 |
| KO-13 | `한글 속성값이 깨진 요소 찾아줘. 웹뷰어에서 검색이 안돼` | Find elements whose Korean property values are broken; search doesn't work in the web viewer. | bim_coordinator | validate_check | encoding_text | hard | true | [IFC] Scans property values for malformed escapes or raw non-ASCII; lists entities and property names. | S:ko-gis-s017 |

---

## 10. Dutch (`NL`)

Dutch rows are shaped by Dutch practice: NL-SfB codes, `BIM basis ILS`, RD coordinates (EPSG:28992), `bouwlagen`, `aspectmodel`. The writer drops articles and uses `graag` rather than `alstublieft`.

| ID | Prompt | English gloss | Persona | Intent | Topic | Diff | File | Expected | Origin |
|---|---|---|---|---|---|---|---|---|---|
| NL-01 | `hoeveel IfcBuildingElementProxy zitten er in dit model en uit welke Revit categorieen komen die? wil ze goed mappen voor de export` | How many proxies are in this model and from which Revit categories? I want to map them properly for export. | bim_coordinator | validate_check | class_mapping | medium | true | [IFC] Count and grouping. Dutch reply. | S:nl-dutch-s001 |
| NL-02 | `welke elementen hebben geen NL-SfB code of niet 4 cijfers? lijst per IFC class graag` | Which elements have no NL-SfB code or not 4 digits? List per IFC class please. | bim_coordinator | validate_check | classification_bsdd | medium | true | [IFC] Elements without a classification reference or with a code that is not four digits, by class. | S:nl-dutch-s002 |
| NL-03 | `kloppen de bouwlagen met de ILS? alleen IfcBuildingStorey, namen als '00 begane grond', en elk element aan de juiste laag` | Do the storeys match the ILS? Only IfcBuildingStorey, names like '00 begane grond', and every element on the right storey. | bim_manager | validate_check | levels_storeys | medium | true | [IFC] Checks storey class and name pattern as given, and containment of elements; the ILS itself is not available, so only the user's stated pattern is tested. | S:nl-dutch-s004 |
| NL-04 | `architectuur en constructie liggen niet op elkaar, check nulpunt en IfcMapConversion, RD of lokaal?` | Architecture and structure don't line up; check the zero point and IfcMapConversion, RD or local? | bim_manager | validate_check | coordinates_georef | hard | true | [IFC] Compares both files' placement and map conversion; says whether EPSG:28992 is named. | S:nl-dutch-s007 |
| NL-05 | `welke wanden en vloeren missen LoadBearing of IsExternal in Pset_WallCommon?` | Which walls and floors lack LoadBearing or IsExternal in Pset_WallCommon? | architect | validate_check | psets_properties | easy | true | [IFC] Lists them; slabs use Pset_SlabCommon, so the assistant notes that rather than looking in the wrong set. | S:nl-dutch-s005 |
| NL-06 | `m2 binnenwand per NL-SfB code en aantal deuren met FireRating, naar excel kan?` | m2 of interior wall per NL-SfB code and number of doors with FireRating, to Excel possible? | estimator_qs | extract_quantities | quantities_qto | medium | true | [IFC] Area per code, door count with a fire rating; spreadsheet output. | S:nl-dutch-s009 |
| NL-07 | `wat is er veranderd tussen v3 en v4 van het constructie ifc? nieuwe, verwijderde en gewijzigde elementen op GUID` | What changed between v3 and v4 of the structural ifc? New, deleted and changed elements by GUID. | bim_coordinator | compare_versions | guid_change_tracking | medium | true | [IFC] Added, deleted, changed with counts. | S:nl-dutch-s010 |
| NL-08 | `mijn kozijn familie komt als proxy in het ifc ipv IfcWindow, wat moet ik instellen in Revit?` | My window frame family comes out as proxy instead of IfcWindow; what do I set in Revit? | architect | troubleshoot_export | class_mapping | medium | false | [chat] Explains IfcExportAs on the family/type and the category mapping; offers to count proxies in the file. | S:nl-dutch-s011 |
| NL-09 | `kun je een IDS maken van BIM basis ILS en daarmee dit model toetsen?` | Can you make an IDS from BIM basis ILS and use it to check this model? | bim_manager | how_to | ids_requirements | hard | true | [either] Needs the requirement text; if the user pastes it, writes an IDS; does not recall the ILS from memory. | S:nl-dutch-s012 |
| NL-10 | `zijn er dubbele objecten in dit aspectmodel? en wanden die elkaar doorsnijden` | Are there duplicate objects in this discipline model? And walls that intersect each other? | bim_coordinator | validate_check | geometry_quality | hard | true | [IFC] Duplicates by class and position; wall-wall intersections need a geometry tool and are reported or declined honestly. | S:nl-dutch-s014 |

---

## 11. Nordic: Norwegian and Danish (`NO`, `DA`)

Norwegian terms: `MMI` (modellens modenhetsindeks), `FDV`, `NS 3451`, `TEK17`, `RIB/RIV` (structural and ventilation consultants), `EUREF89 NTM`. Special letters (æ, ø, å) are a recurring encoding problem. The Danish row is based on a real English-language issue about Danish letters; its Danish wording is mine (no Danish prompts in the data).

| ID | Prompt | English gloss | Persona | Intent | Topic | Diff | File | Expected | Origin |
|---|---|---|---|---|---|---|---|---|---|
| NO-01 | `sjekk hvilke objekter som mangler MMI i modellen, grupper per fag og gi meg antall` | Check which objects lack MMI in the model, group by discipline and give me the count. | bim_coordinator | validate_check | psets_properties | medium | true | [IFC] Finds where MMI is stored (asks if several candidates), counts missing per discipline. Norwegian reply. | S:no-norway-s001 |
| NO-02 | `hvorfor er det så mange IfcBuildingElementProxy her?? hvilke kategorier fra Revit kommer de fra` | Why are there so many proxies here?? Which Revit categories do they come from? | bim_coordinator | query_model_data | class_mapping | medium | true | [IFC] Count and grouping. | S:no-norway-s002 |
| NO-03 | `etasjene blir dobbelt i IFC etter eksport fra Revit, noen ide? sjekk modellen` | The storeys are doubled in the IFC after export from Revit, any idea? Check the model. | architect | troubleshoot_export | levels_storeys | medium | true | [IFC] Lists storeys with elevations, duplicates by name or elevation, counts per storey. | S:no-norway-s004 |
| NO-04 | `har alle tekniske komponenter FDV-info og NS 3451-kode? vil ha liste over de som mangler` | Do all technical components have FDV info and an NS 3451 code? I want the list of those missing. | owner_client | validate_check | cobie_fm_handover | medium | true | [IFC] Missing FDV-type properties and classification, by class; asks which property carries FDV info. | S:no-norway-s006 |
| NO-05 | `trenger mengder: netto areal yttervegger per etasje, uten åpninger` | I need quantities: net area of external walls per storey, without openings. | estimator_qs | extract_quantities | quantities_qto | medium | true | [IFC] Net side area of IsExternal walls per storey, source stated. | S:no-norway-s008 |
| NO-06 | `kollisjonskontroll RIV mot RIB, lag BCF av de over 50 mm` | Clash check RIV against RIB, make BCF of those over 50 mm. | bim_coordinator | coordinate_clash | clash_coordination_bcf | hard | true | [IFC] Needs a clash tool; "over 50 mm" interpreted (penetration depth) and stated; BCF or honest "cannot". | S:no-norway-s010 |
| NO-07 | `sjekk dørbredder i rømningsveier mot TEK17, hvilke dører er under 90 cm` | Check door widths on escape routes against TEK17; which doors are under 90 cm? | reviewer_authority | comply_regulation | permitting_code_checking | hard | true | [IFC] Doors under 90 cm by width property; escape routes are not marked in an IFC unless they are tagged, so it asks or says so; does not quote TEK17. | S:no-norway-s014 |
| NO-08 | `æøå blir rare tegn i navnene når jeg leser IFC med ifcopenshell, hvorfor` | æøå turn into strange characters in names when I read the IFC with ifcopenshell; why? | developer_programmer | troubleshoot_code | encoding_text | medium | false | [chat] File encoding vs escape sequences vs console encoding; short checks; offers to inspect a name in the file. | S:no-norway-s012 |
| NO-09 | `ligger veimodellen i riktig koordinatsystem (EUREF89 NTM sone?) Hva er origo og rotasjon` | Is the road model in the right coordinate system (EUREF89 NTM zone?) What are the origin and rotation? | civil_infra_engineer | validate_check | coordinates_georef | hard | true | [IFC] Reports CRS and map conversion as written; the NTM zone is not guessed. | S:no-norway-s005 |
| NO-10 | `IFC4.3-filen fra Civil 3D viser ikke aksen i viewer, ligger den i filen?` | The IFC4.3 file from Civil 3D doesn't show the alignment in the viewer; is it in the file? | civil_infra_engineer | troubleshoot_viewing | infrastructure_ifc43 | hard | true | [IFC4.3] Counts IfcAlignment and its representations; viewer support is a separate question. | S:no-norway-s017 |
| DA-01 | `de danske bogstaver æ ø å står som \X\E6 i værdierne, er filen i stykker eller er det bare viseren?` | The Danish letters æ ø å appear as `\X\E6` in values; is the file broken or just the viewer? | bim_coordinator | validate_check | encoding_text | medium | true | [IFC] Explains that `\X\E6` is a valid escape for æ in IFC strings; shows examples from the file and notes that the viewer should decode them. Danish reply. | R:[en-gh-encoding-r022](https://github.com/ThatOpen/engine_web-ifc/issues/358) |

---

## 12. Turkish, Arabic, Greek (`TR`, `AR`, `EL`)

Only a handful of rows exist in the data, all about **encoding of local letters** in IFC, plus constructed requests. The encoding rows are the strongest ones; the rest are labelled `N` and their register is unverified.

| ID | Prompt | English gloss | Persona | Intent | Topic | Diff | File | Expected | Origin |
|---|---|---|---|---|---|---|---|---|---|
| TR-01 | `modeldeki isimlerde ş ğ ı İ gibi türkçe karakter geçen elemanları listele, doğru okunuyor mu bak` | List the elements whose names contain Turkish letters like ş ğ ı İ, and check they are read correctly. | architect | query_model_data | encoding_text | easy | true | [IFC] Lists names with those characters, shows the decoded text and the stored escape form; flags any that look corrupted. Turkish reply. | S:enc-s004 |
| TR-02 | `ifc dosyasında ğ ü ş harfleri neden \X2\ diye kodlanıyor? bozuk mu?` | Why are the letters ğ ü ş encoded as `\X2\` in the ifc file? Is it broken? | student_beginner | understand_concept | encoding_text | easy | false | [chat] Normal IFC Unicode escaping; the file is not broken. | S:enc-s015 |
| TR-03 | `OBJ'ye çevirirken yüzey stili isimlerindeki İ ve Ç yüzünden hata veriyor, dosyada hangi isimler \X2\ ile kodlanmış göster` | Converting to OBJ fails because of İ and Ç in surface style names; show which names in the file are encoded with `\X2\`. | developer_programmer | troubleshoot_code | encoding_text | medium | true | [IFC] Lists IfcSurfaceStyle names with escapes and their decoded text; suggests a workaround without rewriting the file unasked. | R:[en-gh-encoding-r020](https://github.com/IfcOpenShell/IfcOpenShell/issues/101) |
| TR-04 | `ruhsat için bu ifc'de kapı genişlikleri ve oda alanları eksik mi, eksikleri listele` | For the permit, are door widths and room areas missing in this ifc? List what is missing. | reviewer_authority | validate_check | permitting_code_checking | medium | true | [IFC] Doors with no width and spaces with no area; no statement about the permit rules. | N |
| AR-01 | `أسماء الغرف بالعربي تظهر علامات استفهام بعد تصدير IFC، شو المشكلة؟` | Arabic room names show question marks after the IFC export; what's the problem? | bim_coordinator | troubleshoot_export | encoding_text | medium | false | [chat] Likely lost encoding on export; explains escapes vs question marks; offers to inspect space names if a file is loaded. Arabic reply. | S:enc-s005 |
| AR-02 | `كم عدد الجدران والأبواب في كل طابق في هذا الملف؟` | How many walls and doors are on each floor in this file? | architect | query_model_data | spatial_structure | easy | true | [IFC] Table of walls and doors per storey. | N |
| AR-03 | `النموذج اللي أرسله الاستشاري يطلع بعيد عن النموذج حقنا، شنو أسوي حتى تتصحح الإحداثيات؟` | The model the consultant sent comes out far from our model; what do I do to correct the coordinates? (Gulf Arabic wording) | bim_coordinator | troubleshoot_import | coordinates_georef | medium | true | [IFC] Measures the offset and units first; then short options. Arabic reply. | N |
| EL-01 | `δείξε μου τα ονόματα των χώρων στα ελληνικά, βγαίνουν σωστά ή με περίεργους χαρακτήρες;` | Show me the space names in Greek; do they come out correctly or with strange characters? | architect | query_model_data | encoding_text | easy | true | [IFC] Lists IfcSpace names, decoded, flags corrupted ones. | S:enc-s006 |

---

## 13. Other languages (`OT`): Slovak, Vietnamese, Czech, Polish

Single rows from README examples and one encoding issue. Polish has **no** records in the data; its rows are constructed and flagged.

| ID | Prompt | English gloss | Persona | Intent | Topic | Diff | File | Expected | Origin |
|---|---|---|---|---|---|---|---|---|---|
| OT-01 | `Oddiaľ pôdorys o 15 percent. Ukáž vzduchotechniku v perspektíve na celú obrazovku.` | Zoom the floor plan out by 15 percent. Show the ventilation in perspective, full screen. | architect | modify_model_data | viewers_opening | medium | true | [either] A camera or viewer command; works only if the server controls a viewer, otherwise says it has no camera tool. Slovak reply. | R:[sk-aimcp-r016](https://github.com/Menezeris/AIMviewer/issues/65) |
| OT-02 | `Thống kê số cửa, số phòng, khối lượng tường và sàn trong mô hình` | Count the doors and rooms and give wall and slab quantities in the model. | estimator_qs | extract_quantities | quantities_qto | easy | true | [either] Counts and quantities with the source stated. Vietnamese reply. | R:[vi-aimcp-r042](https://github.com/andyluu98/vn-revit-mcp) |
| OT-03 | `po exportu z web-ifc jsou české znaky v názvech rozbité, é se mění na E9, najdi ty prvky` | After export from web-ifc, Czech characters in names are broken, é turns into E9; find those elements. | developer_programmer | validate_check | encoding_text | hard | true | [IFC] Finds names with malformed escapes (for example E9 without the escape marker), lists entities. Czech reply. | R:[en-gh-encoding-r021](https://github.com/ThatOpen/engine_web-ifc/issues/440) |
| OT-04 | `ile ścian i drzwi jest na każdej kondygnacji w tym ifc?` | How many walls and doors are on each storey in this ifc? | architect | query_model_data | spatial_structure | easy | true | [IFC] Table by storey. Polish reply. | N (no PL records in the data; register unverified) |
| OT-05 | `sprawdź czy wszystkie pomieszczenia mają numer, nazwę i powierzchnię, wyślemy to jutro do inwestora` | Check that all rooms have number, name and area; we send it to the client tomorrow. | bim_coordinator | validate_check | spaces_rooms_areas | easy | true | [IFC] Missing number, name or area per space, counts and list. | N (no PL records in the data; register unverified) |
| OT-06 | `model od branży instalacyjnej ląduje kilometr od naszego, sprawdź współrzędne i jednostki` | The MEP discipline's model lands a kilometre from ours; check coordinates and units. | bim_coordinator | validate_check | coordinates_georef | medium | true | [IFC] Reads units, site placement, map conversion and extents; distance in stated units. | N (no PL records in the data; register unverified) |

---

## 14. Parallel sets: the same intent in many languages

Load one model, send every prompt of a set (one per chat), and compare. The numbers must be identical; only the language of the answer changes. Differences point to a language-handling weakness (a name mapped differently, a tool called with the wrong argument, a hallucinated number).

| Set | What it asks | IDs |
|---|---|---|
| Proxy count and source categories | Count `IfcBuildingElementProxy`, group by Revit category | ZH-02, ES-01, PT-01, DE-01, FR-02, IT-01, JA-01, KO-01, NL-01, NO-02; English: INV-03 in [prompt_bank_en.md](prompt_bank_en.md) |
| Compare two versions | Added, removed, changed (needs two files) | ZH-12, ES-07, DE-07, FR-05, IT-03, JA-06, KO-06, NL-07; English: CMP-02 |
| Georeferencing and offset | CRS, map conversion, distance from origin | ZH-03, DE-02, FR-06, IT-02, JA-10, NL-04, NO-09, OT-06; English: CRD-01 |
| Quantities per storey | Walls, slabs, columns per storey with source | ZH-05, ES-03, PT-04, IT-05, KO-04, FR-10, NO-05, DE-06; English: QTY-11 |
| Encoding of local letters | Names with non-ASCII characters | ZH-07, KO-13, TR-01, AR-01, EL-01, NO-08, DA-01, OT-03, FR-13 |
| Reclassify proxies by name | Make "column" proxies into `IfcColumn` on a copy | ES-11, DE-09, IT-06, KO-05; English: MOD-03 |
| Rooms missing data | Area, number, name or use | JA-02, ES-14, OT-05, TR-04, DE-10; English: VAL-27 |

## 15. Known gaps and caveats

- **Synthetic by design.** 155 of 170 rows come from synthetic research drafts (rewritten), 9 from real posts or READMEs, 6 are constructed. Real "typed to an assistant" prompts in these languages are almost absent from the data (a handful of README examples: Spanish `Creá cuatro muros de 3 m...`, Slovak and Vietnamese commands).
- **Register is partly imitation.** Chinese real text is partly polished article voice; Korean and French have only a few real posts; Japanese real text is article titles and bodies. Check any language you plan to rely on with a native speaker.
- **Languages with no or little data.** Polish: none. Arabic, Greek, Danish, Czech, Slovak, Vietnamese, Turkish: one to four records each, mostly about encoding. European Portuguese, Swedish, Finnish, Hindi (written in Devanagari or Hinglish), Thai, Indonesian, Hebrew, Russian-adjacent languages: not covered here; Russian has its own [bank](prompt_bank_ru.md).
- **Regulation content is unverified.** Names such as Planbim MIDE, Plan BIM, CTE, TEK17, DIN 276, NL-SfB, SZ-IFC, CGCS2000, TWD97, EPSG codes and portals (세움터, 確認申請, 报建) are used as a user would. Re-check against current official texts before treating any Expected line as ground truth.
- **Expected lines assume a reasonably complete tool menu.** Where a server lacks a tool (clash detection, BCF, IDS, IFC export), the correct answer is an honest "cannot", in the user's language, not a pretend result.
- **Dialects.** Latin American vs Peninsular Spanish, Brazilian Portuguese, Gulf vs Levantine Arabic, Swiss German and Austrian terms are only lightly sampled. Rows that use a regional form say so in the gloss or the section intro.
- **Missing areas.** No multi-turn dialogs in these languages (see the English and Russian banks for dialog patterns); little on energy models, 4D scheduling and terrain; the Revit-live family is thin (3 rows) because few non-English Revit-MCP prompts exist in the data.
