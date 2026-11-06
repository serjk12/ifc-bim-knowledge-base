# Importing IFC and cross-tool interoperability

Vocabulary topics covered: `import_into_revit`, `import_other_tools`, `export_archicad`, `export_tekla`, `export_other_tools`.
Built from the wave-1 research data (`research_raw/wave1/...`) with `tools/kb.py`; reference facts come from the docs linked below.

## In plain words

An IFC file is a neutral "exchange" file: one program writes it, another reads it. In practice the receiving program rarely shows the model the way the sender saw it. The most common story in the data is someone with a Revit project who receives an IFC from an architect (Archicad, Allplan, Renga), a structural engineer (Tekla, SCAD, Robot) or a civil designer (Civil 3D), and then something looks wrong: it sits in the wrong place, it is rotated, everything is a "Generic Model", windows float outside walls, only the grid lines show, the link hangs for an hour, or the walls cannot be edited.

Most of these are not "broken file" problems. They come from four plain facts:

1. **Revit has two different IFC doors.** *Link IFC* keeps the model as a read-only reference (every element becomes a frozen "DirectShape" in a hidden cache file `<name>.ifc.RVT`). *Open IFC* builds a new Revit project and tries to create editable-looking Revit elements, usually poorly. See [Revit IFC import and link reference](../../03_software/revit/ifc_import_link_reference.md).
2. **IFC is a reference format, not a round-trip editing format.** The parametric "intelligence" (families, constraints) does not travel. See [IFC in real projects](../../01_ifc_basics/00_ifc_in_real_projects.md).
3. **Every exporter makes its own choices** (which IFC class an object gets, which geometry type, which IFC version and view, where the zero point is). Archicad "translators", Tekla "export types", Renga mapping files are all just different knobs for the same thing. See [IFC in other authoring tools](../../03_software/authoring_tools_ifc.md).
4. **Coordinates, units and file text encoding are easy to get wrong** and the symptoms look like geometry problems. See [Geometry, placement, coordinates, units](../../01_ifc_basics/06_geometry_placement_coordinates_units.md) and [Inside an .ifc file](../../01_ifc_basics/02_ifc_file_anatomy.md).

For an MCP tester: a good assistant should treat "my IFC looks wrong in Revit" as a diagnosis task. It should first ask *how* the file was brought in (Link or Open), then check facts that can be read from the IFC itself (classes, proxies, placements, map conversion, units, assemblies, header), and be honest about what only Revit can show.

**Data caveats.** After removing duplicates there are 282 real records (lang: en 209, ru 35, zh 18, ja 6, es 6, it 3, de 2, pt 1, no 1, ko 1) from about 214 distinct source URLs; 105 of the records come from the Autodesk `revit-ifc` GitHub tracker, so the English, Revit-import, regression-style view is over-represented (many tracker records are title-only). Russian forum material (forum.dwg.ru) and Chinese Q&A sites (Zhihu, CSDN, Baidu) are the main non-English voices. Frequency numbers below are keyword-cluster counts, approximate, and one record can fall in several clusters. Records are paraphrases, not copies of what people wrote; the "English-labelled" rows from non-English sources keep the dataset's English paraphrase.

## Problem map

Ranked by how often the problem shows up in the data (approximate records / distinct source URLs, main languages).

| # | Problem | How users describe it | Frequency signal | Root cause | Typical fix |
|---|---|---|---|---|---|
| 1 | Open vs Link confusion; "imported IFC is not editable" | "dumb solids, not Revit objects", "in-place families without IFC data", "how do I edit the family from an IFC" / "элементы приходят как тела", "ifc链进来的墙改不了" | ~54 rec / ~40 URLs; en, ru, ja, zh | Link = DirectShape reference; Open = old import path with in-place or generic elements; IFC is not an editing format | Use Link for coordination; edit in the source tool; if you must rebuild, model over the linked geometry or use Open and accept loss |
| 2 | Wrong position, rotation or height after linking | "linked IFC far from origin", "rotated to true north", "levels at double height", "works in viewers but not in Revit" | ~43 rec / ~31 URLs; mostly en, some zh, es, ja, ru | IFC has no Autodesk "shared coordinates"; importer maps IfcMapConversion / IfcSite to Revit origin and true north; version regressions; huge survey coordinates | Agree one origin/CRS before export; check IfcSite, IfcMapConversion, units; use positioning option (Revit 2026+); move the link; test on another Revit/add-in build |
| 3 | Everything is a Generic Model / wrong category | "all my walls are generic models", "IfcFlowSegment everywhere", "колонны пришли обобщёнными" | ~36 rec / ~27 URLs; en, ru, ja | Hardcoded class-to-category table; elements exported as `IfcBuildingElementProxy`; materially incomplete type info | Fix classes at the source (IFC mapping in the authoring tool); use the Import IFC Class Mapping file; accept DirectShape for Link |
| 4 | Link/Open hangs or takes hours; project bloats | "Link IFC hangs, kill Revit", "40 minutes then 800 MB", "151 MB Tekla IFC becomes 2 GB" | ~30 rec / ~26 URLs; en, zh, ru, de | Building the DirectShape cache is expensive; tiny parts (bolts), assemblies, tessellated geometry; some Revit 2025-2027 bugs | Link into a new empty file first; delete small parts/assemblies; export fewer elements; try Open; lighter exchange (see [large files topic](file_size_viewing_conversion.md)) |
| 5 | Model imported but nothing visible in 3D / only grids | "ifc导入revit后三维不可见", "одни оси видны", "plan shows it but 3D does not" | ~11 rec / ~9 URLs; zh, ru, en | View phase / phase filter or link phase mismatch; 3D view created before import; far-from-origin geometry | Set the phase of the link and view; recreate the 3D view; check coordinates and visibility |
| 6 | Windows, doors, openings wrong | "windows outside the wall face (2025-2027)", "door swings missing in plan", "openings do not cut walls", "openings as generic models" | ~20 rec / ~13 URLs; en | Hosted-element placement regression; 2D footprint geometry from Archicad; IfcOpeningElement imported as separate geometry | Hide the opening subcategory; Link then bind for voids; try other Revit/add-in version; report with sample file |
| 7 | IfcSpace does not become Room/Space | "spaces as generic models obstruct views", "MEP needs Spaces" | ~8 rec / 4 URLs; en | Link IFC keeps IfcSpace as Generic Model (`IfcSpace.INTERNAL`); a space is a 3D shape, a Room is defined by level and point | Hide the subcategory; use Open IFC for Rooms; room separation lines from space boundaries |
| 8 | Tekla / steel specifics | "assemblies doubled", "only the grids come through", "rebar and bolts lost", "stray points on direct shapes" | ~42 rec / ~32 URLs; en, ru, zh | `IfcElementAssembly` plus its parts both imported; export type surface/B-rep vs editable; rebar/bolts/welds not convertible; IFC4 import bugs | Pick the right Tekla export type; set phase of link; delete assemblies or map to a deletable category; check export log |
| 9 | Properties and parameters lost or unstable on update | "properties missing after import", "new shared-parameter GUIDs on every re-link", "Comments/Mark do not come back" | ~37 rec / ~34 URLs; en, ru, it, ja | Psets become read-only parameters in Link only; shared-parameter file rebuilt on re-link; Open drops IFC data | Link (not Open); keep the IFC in the same folder when updating; schedule on `IfcExportAs`/Pset parameters |
| 10 | IFC4 / IFC4.3 / civil geometry not read | "can't import IfcTriangulatedFaceSet", "IFC4X3_ADD2 header fails", "alignment imports but nothing shows" | ~28 rec / ~22 URLs; en | Open IFC has only partial IFC4 support; some IFC4 geometry types unsupported in old builds; IFC4.1 was withdrawn; IFC4.3 header variants | Link instead of Open; request IFC2x3 or a supported IFC4 view; change the header schema string only as a documented workaround |
| 11 | Colors and materials lost | "glass yellow and meters thick", "colours show in the viewer, not in Revit", "materials gone from Max/SketchUp" | ~20 rec / ~17 URLs; en, ru, zh | Color is a style on the geometry, material is only a name; Revit uses its own materials | Map colors to Revit materials after import; ask for styled representations; pre-create materials |
| 12 | Text encoding / broken or truncated file | "umlauts wrong", "Tekla wants Latin file name", "could not find ENDSEC", "IFC from SolidWorks reads with Python error" | ~16 rec / ~15 URLs; en, ru, es, pt, ko | Non-ASCII must be written as `\X2\...\X0\` escapes; raw bytes, Mac Roman, truncated/zero-byte files | Re-export from the source with a fixed exporter; check file ends with `ENDSEC; END-ISO-10303-21;`; Latin path/name |
| 13 | Opening IFC in non-Revit tools (AutoCAD, ETABS, SCAD, Navisworks, Civil 3D, Bonsai) | "AutoCAD can't import IFC", "IFC into ETABS errors", "structural IFC does not load in Bonsai" | ~28 rec / ~27 URLs; en, ru, zh, es, it | Not every tool imports IFC; analysis tools need analytical models, not solids; some exporters write invalid IFC | Use a tool that does import IFC or a converter; export analytical data separately; validate the file |
| 14 | Which export setting to choose at the source (Archicad translator, Tekla export type, Renga/Allplan/SAPFIR, 2x3 vs 4) | "which translator for Revit?", "reference view or design transfer?", "IFC2x3 or IFC4 for Navisworks?" | ~121 rec / ~112 URLs across the three export_* topics; en, ru, zh, ja, es, it | Each exporter has presets that trade geometry fidelity, editability and file size | Pick purpose first: viewing/coordination = Reference View or CV2.0; editing in the receiver = test Design Transfer; verify by re-opening |
| 15 | Non-IFC sources into Revit/IFC (DWG, SketchUp, 3ds Max, ArchiCAD .pln) | "how do I bring a pln file into Revit", "SU import always loses materials" | ~24 rec / ~22 URLs; ru, zh, en, it | No direct importer; DWG has no BIM semantics | Go via IFC or DWG; remodel; use classification and mapping tools; expect limited semantics |

## Problems in depth

Each section lists symptoms in users' words (original-language paraphrases with an English gloss, linked to the source), why it happens, what fixes it, and how a good AI/MCP assistant should respond, including questions to ask first.

### 1. Open IFC vs Link IFC, and "I cannot edit what I imported"

**Symptoms.**
- EN: "asks for official feedback on the two import methods; Open yields in-place families without IFC data ..., Link duplicates geometry" ([revit-ifc #223](https://github.com/Autodesk/revit-ifc/issues/223)).
- RU: "при импорте IFC архитектурных моделей из других программ элементы приходят как тела, а не как родные объекты Ревита, хочу их редактировать" (gloss: imported elements arrive as dumb solids, not native objects; I want to edit them) ([forum.dwg.ru](https://forum.dwg.ru/showthread.php?t=166052)).
- RU: "можно ли редактировать семейство из IFC в Ревите" (can an IFC be edited as a family?) ([forum.dwg.ru](https://forum.dwg.ru/showthread.php?t=130296&page=2)).
- ZH (synthetic prompt inspired by the cluster): "ifc链进来的墙改不了啊，怎么变成revit自己的墙？" (the linked wall can't be edited; how to make it a Revit wall?). Compare the real record: [round-trip wall with window arrives as Imported Symbol, #729](https://github.com/Autodesk/revit-ifc/issues/729).

**Why.** Link IFC creates a cache `<name>.ifc.RVT` full of DirectShapes; Open IFC is a separate, older code path that sometimes creates native walls or floors (for example when a wall carries an `IfcMaterialLayerSetUsage`) and otherwise in-place families or generic models. Maintainers have said the plan is to move both workflows onto the newer Link code ([ref doc, sections 1 and 7](../../03_software/revit/ifc_import_link_reference.md)). No official one-click "convert to native" exists.

**What fixes it.** Decide the purpose. Coordination, clash, section, measure: Link. Editing or reuse: ask the author for a native file or exchange add-in; otherwise model over the linked geometry (snaps work) or accept Open with its losses. Never treat the re-imported IFC as the new master.

**Good assistant behaviour.**
- Explain both paths in two sentences before anything else; do not promise native, parametric walls.
- If an IFC server is connected, report what the file actually contains (IfcWall with a material layer set? `IfcBuildingElementProxy`? type objects?) because that decides how Open IFC will behave.
- Clarifying questions: "Did you use Insert > Link IFC or File > Open > IFC?", "Which Revit version and IFC add-in version?", "What do you need to do with it: look, coordinate, or edit?", "Which program made the IFC and which IFC version/view?"

### 2. Wrong position, rotation or height

**Symptoms.**
- EN: "Georeferenced IFCs line up in Trimble and BIM Vision but not when linked in Revit 2022; is there an easy way?" ([#566](https://github.com/Autodesk/revit-ifc/issues/566)).
- EN: "In 2025-2027 Link IFC positions geometry higher than it should be and creates levels at twice the correct elevation; Open IFC is fine" ([#990](https://github.com/Autodesk/revit-ifc/issues/990)).
- EN: "Linking aligns IFC +Y to true north instead of keeping project north; worked in 2020" ([#522](https://github.com/Autodesk/revit-ifc/issues/522)); linking the IFC and linking its `.ifc.rvt` give different rotations ([#710](https://github.com/Autodesk/revit-ifc/issues/710)).
- EN: "Export lets you choose the origin but import always uses the internal origin; can import use the project base point?" ([#320](https://github.com/Autodesk/revit-ifc/issues/320)).
- EN/ES: Archicad IFC "always lands at the Revit Base Point even with Survey Point set" ([Graphisoft community](https://community.graphisoft.com:443/t5/Collaborate-forum/IFC-export-import-Revit/td-p/352151)); Arkance article on linking with shared coordinates ([Arkance](https://emea.support.arkance.world/hc/es/articles/36464850969234-Using-IFC-files-with-a-Shared-Coordinates-system)).
- RU (synthetic): "ифс из аллплана улетел на 3 км от начала координат в ревите".

**Why.** IFC has no Autodesk-style "shared coordinates". Georeferencing is `IfcMapConversion` / `IfcProjectedCRS` (IFC4) or `IfcSite` lat/long/elevation (IFC2x3); Revit's link logic applies origin-to-origin placement, derives true north from the map conversion, and has had version-specific bugs (duplicated Z offset 2025-2027; project-north regression since 2022; 2021.4.x add-in builds placing models wrongly; large coordinates). Revit 2026 added a Positioning option (internal origin, project base point, survey point) according to the maintainer reply on #320. Release 27.3.0.12 reports a fix for levels from a linked IFC placed in the wrong position ([ref doc, sections 5 and 8](../../03_software/revit/ifc_import_link_reference.md)). A buildingSMART thread also shows two products writing `IfcMapConversion` while their model coordinates are already projected, so the offset gets applied twice ([forum](https://forums.buildingsmart.org/t/5695)).

**What fixes it.** Agree one origin or CRS per project before anyone exports; link first with a known reference object (grid intersection, survey point) and measure; move or rotate the link instance; re-export from the source with the agreed base point; test a different add-in build when the same file worked in an older Revit.

**Good assistant behaviour.**
- Read from the IFC: `IfcSite` placement and lat/long, `IfcMapConversion` and `IfcProjectedCRS`, unit scale, `TrueNorth` in the geometric context, bounding box and distance from the origin. Report numbers, not guesses.
- State which part is a file fact and which is Revit behaviour that depends on version; do not claim a bug is "fixed" without a version.
- Clarifying questions: "Revit and IFC add-in versions?", "Which positioning option did you use?", "Do you have a known survey point or grid intersection to compare?", "Does it look right in a neutral viewer?"

### 3. Everything arrives as Generic Model; class mapping

**Symptoms.**
- EN: "Is there a way to get Revit to recognize walls when importing IFC? Currently all generic models" ([#571](https://github.com/Autodesk/revit-ifc/issues/571)).
- EN: consultants send generic `IfcFlowSegment`; the team built HVAC class-mapping tables but has to select them under Open > IFC Options each time ([#798](https://github.com/Autodesk/revit-ifc/issues/798)); the table seemed ignored for several MEP classes in Revit 2024 ([#803](https://github.com/Autodesk/revit-ifc/issues/803)).
- IT: "come carico il file di mappatura classi IFC in Revit prima di aprire l'IFC cosi le porte restano porte?" (how do I load the class mapping file before opening so doors stay doors?) ([ACCA Biblus](https://biblus.acca.it/ifc-class-mapping-file/)).
- RU: "при экспорте из Архикада в IFC и вставке в Ревит стёкла жёлтые и толщиной в метры, часть перегородок пропала" ([forum.dwg.ru](https://forum.dwg.ru/showthread.php?t=154396)).

**Why.** On Link, the entity-to-category mapping is a compiled table of 100+ entries (`IFCCategoryUtil.cs`); there is no external file for it. The user-visible *Import IFC Class Mapping* text file works through File > Open > IFC Options and has had regressions. Many "generic" objects are in fact `IfcBuildingElementProxy` in the file, i.e. the sender never gave them a class. An IfcOpenShell wall with no material layer opens as a generic object ([#778](https://github.com/Autodesk/revit-ifc/issues/778)).

**What fixes it.** Fix at the source (IFC type per object in the authoring tool); edit/choose the import mapping file before Open; for Link accept DirectShape and use filters on `IfcExportAs`-style parameters; script-based reclassification of proxies on the IFC side when the author cannot re-export.

**Good assistant behaviour.**
- Count entities per class and list proxies grouped by `Name` / `ObjectType` / classification, then say what the likely real class is. This is the highest-value, verifiable answer.
- Never edit the original IFC in place; offer a "save as" copy and keep GlobalIds.
- Clarifying questions: "Link or Open?", "Which program exported it and with which translator/mapping?", "Do you need native walls, or is a categorised reference enough?"

### 4. Link hangs, takes hours, or the project bloats

**Symptoms.**
- EN: "A Revit-exported single-chair IFC shows in BIM Vision but Link IFC hangs and the process must be killed" ([#951](https://github.com/Autodesk/revit-ifc/issues/951)).
- RU (synthetic): "ифс открывается в ревите минут 40 и потом файл 800 мб, что делать, связью лучше?".
- ZH: "IFC转Revit模型后体积暴涨怎么减肥" (a 151 MB Tekla IFC becomes 2 GB; slim it down) - answer: delete bolts, make a parametric bolt family ([CSDN](https://blog.csdn.net/zzutt/article/details/121492254)).
- DE: "IFC verlinken vs. Data Exchange laden in Revit" - linked IFC bloats the project ([BIM me up](https://bim-me-up.com/ifc-verlinken-vs-data-exchange-laden-in-revit/)).
- KO (synthetic): "ifc 레빗으로 링크하니까 한글이 깨지고 너무 느려요 ㅠㅠ".

**Why.** The first Link builds the whole DirectShape cache; tiny parts, assemblies and tessellated geometry are expensive. Some Revit 2024-2027 reports describe hangs even on ~5 MB files, tracked internally at Autodesk. Community workaround: link the IFC into a new empty Revit file, wait for the `.ifc.RVT`, then link that file into the project; check antivirus; try another IFC import template. More in [ref doc, section 4](../../03_software/revit/ifc_import_link_reference.md) and the [large-file topic](file_size_viewing_conversion.md).

**Good assistant behaviour.**
- Ask for file size, number of elements (offer to count), originating tool, and whether the same file opens in a viewer.
- Report heavy contributors from the IFC (counts of `IfcMechanicalFastener`, `IfcReinforcingBar`, assemblies, tessellated representation types).
- Do not tell the user the file is "corrupt" when a viewer opens it fine.
- Clarifying questions: "Is Revit frozen or just slow (is the `.ifc.RVT` growing)?", "Does Open IFC work?", "Can the sender export a filtered subset?"

### 5. Imported but nothing visible in 3D (or only grids)

**Symptoms.**
- ZH: "ifc导入revit之后三维视图里什么都看不到，是哪里的问题" (nothing visible in 3D after import) - answers list link/category visibility, phase filter, huge coordinates, view range ([Baidu Zhidao](https://zhidao.baidu.com/question/341569640619976845.html)).
- ZH-TW: plan shows the objects but 3D does not; set the 3D view phase to the latest phase created by the import ([Pixnet](https://housegear.pixnet.net/blog/posts/3042268210)); merge all phases into one ([cnblogs](https://www.cnblogs.com/OverloadBachPunk/p/14452654.html)).
- RU: "заказчик требует выдавать IFC и грузить в Ревит, стандартный экспорт с настройками по умолчанию даёт в Ревите только оси" - answers: choose surface geometry, check the phase of the link ([forum.dwg.ru](https://forum.dwg.ru/showthread.php?t=146029)).

**Why.** Imported elements get a creation phase; a view with an unsuitable phase or phase filter hides them. Also a 3D view made earlier, geometry very far from the origin, or exporter settings that dropped geometry.

**Good assistant behaviour.**
- Check the file first: how many elements have a `Representation`? Are the only things with geometry grids (`IfcGrid`)? Where is the bounding box?
- Then give the Revit-side checklist (phase of the link and the view, phase filter, visibility of the link and its categories, recreate the 3D view).
- Clarifying questions: "Plan view shows it but 3D empty, or both empty?", "Linked or opened?", "What phase and phase filter does the view use?"

### 6. Windows, doors and openings

**Symptoms.**
- EN: "Windows are positioned outside wall faces regardless of the 2D annotation setting; absent in Revit 2024" ([#1019](https://github.com/Autodesk/revit-ifc/issues/1019), [#1018](https://github.com/Autodesk/revit-ifc/issues/1018)).
- EN: "Doors appear in 3D but are invisible in floor plan; the Model footprint representation is not displayed" ([#358](https://github.com/Autodesk/revit-ifc/issues/358)).
- DE: "IFC ProvisionForVoid in Revit - Öffnen vs. Referenzieren / Binden": openings do not cut the walls; answer: link, then bind the link so openings become native ([BIM me up](https://bim-me-up.com/ifc-provisionforvoid-in-revit-offnen-vs-referenzieren-binden/)).
- EN: openings as separate generic models, hard to hide ([#110](https://github.com/Autodesk/revit-ifc/issues/110), [#483](https://github.com/Autodesk/revit-ifc/issues/483)).
- ES (synthetic): "importé el ifc de archicad en revit 2025 y las ventanas quedaron fuera del muro, en el 2024 andaba bien".

**Why.** Archicad-IFC2x3 doors/windows in Revit 2025-2027 are mis-placed in a regression (also related to 2D symbol geometry); `IfcOpeningElement` is imported as its own Generic Model geometry by design; plan symbols arrive as footprint geometry. Hide opening/space helper geometry in Revit Links display settings (subcategories `IfcOpeningElements`, `IfcSpace.INTERNAL`).

**Good assistant behaviour.** Inspect `IfcRelFillsElement` / `IfcRelVoidsElement`, local placements of windows vs the host wall, presence of a footprint ("Plan") representation. Say clearly that a version-specific Revit regression is not something the file can fix.

### 7. IfcSpace does not become a Room or MEP Space

**Symptoms.** EN: "IfcSpace imported as generic models obstructs views; MEP engineers must use Open IFC just to get Rooms" ([#15](https://github.com/Autodesk/revit-ifc/issues/15), open since 2018).

**Why.** Link keeps IfcSpace as Generic Model with subcategory `IfcSpace.INTERNAL`; a Room needs a level and a placement point, a space is a 3D solid. Workarounds: hide the subcategory, use Open IFC for Rooms, or make room separation lines from space boundaries.

**Good assistant behaviour.** Count spaces and list names/areas from the IFC; explain that Revit will not create rooms from a link; ask "do you need room areas or just a visual?"

### 8. Tekla and steel/precast specifics

**Symptoms.**
- RU: "как перекинуть модель из Теклы в Ревит, IFC не работает; позже свойства и геометрия теряются" ([forum.dwg.ru](https://forum.dwg.ru/showthread.php?t=146029)); "колонны из Теклы в Ревите: материал и тонирование не меняются; арматура и узлы не переносятся" ([forum.dwg.ru](https://forum.dwg.ru/showthread.php?t=155997)).
- ZH: "tekla导出ifc到revit后3D视图里看不到模型" - delete the original 3D view and create a new one ([Zhihu](https://www.zhihu.com/question/60173683)).
- EN: "Linking a Tekla IFC4 model in Revit 2024 shows many stray points on direct shapes" ([#943](https://github.com/Autodesk/revit-ifc/issues/943)); "Tekla steel models wrap nearly everything in IfcElementAssembly, doubling element count" ([IFC4.x-development #205](https://github.com/buildingSMART/IFC4.x-development/issues/205)).
- EN (official Tekla docs): reference view for viewing, design transfer for handover; base point export via IfcMapConversion or IfcSite; 247-character path limit ([Tekla 2024](https://support.tekla.com/doc/tekla-structures/2024/int_ifc_export)).

**Why.** Link imports each `IfcElementAssembly` and its sub-elements, so geometry doubles; rebar/bolts/welds are not reconstructed as native Revit elements; export type decides whether you get editable geometry or B-rep surfaces; objects that fail export can be forced to B-rep per object; property sets come from configuration files ([Tekla property sets](https://support.tekla.com/doc/tekla-structures/2024/int_defining_property_sets_using_property_set_definitions)).

**Good assistant behaviour.** Count assemblies and single-child assemblies, list sub-parts, count `IfcReinforcingBar` / `IfcMechanicalFastener`, find elements without representation, check which coordinate mechanism the export used. Advise to verify the export by inserting it back as a reference model in Tekla and comparing counts ([Tekla check](https://support.tekla.com/doc/tekla-structures/2024/int_checking_exported_ifc_model)).

### 9. Properties lost, parameters unstable on update, GUIDs

**Symptoms.**
- RU: "при импорте IFC геометрия есть, но элементы не распознаются как объекты, пропадают параметры" ([forum.dwg.ru](https://forum.dwg.ru/showthread.php?t=166052)).
- EN: "Linking an updated IFC generates a new rvt and a new shared parameter file with different GUIDs even for identical pset names" ([#408](https://github.com/Autodesk/revit-ifc/issues/408)); "shared parameter file is deleted once linking is done" ([#970](https://github.com/Autodesk/revit-ifc/issues/970)).
- JA: "IFCをRevitで開くと属性が全然出てこない…リンクとか開くとか何が違う？" (synthetic).
- RU: "часть свойств потерялась после импорта IFC, какие настройки экспорта выбрать" - Renga: edit type and parameter mapping files; default RV 1.2 is not for editing ([Renga blog](https://blog.rengabim.com/2021/08/ifc.html)).

**Why.** In Link, IFC property sets appear as read-only parameters; Open IFC historically drops IFC data; shared-parameter GUIDs can change on re-link; the exporter must have written the Psets in the first place (Archicad translator, Tekla pset config, Renga mapping JSON).

**Good assistant behaviour.** Check the IFC for the expected Psets on the relevant classes (e.g. whether custom properties exist at all) before blaming Revit; compare GlobalIds between revisions; note that GUIDs may be regenerated by the exporter.

### 10. IFC4, IFC4.3 and civil geometry

**Symptoms.**
- EN: "Revit can't open an IFC containing IfcTriangulatedFaceSet (new in IFC4); do I need to link instead?" - Open IFC only partly supports IFC4; Link works for the reference view ([#587](https://github.com/Autodesk/revit-ifc/issues/587), [osarch](https://community.osarch.org/discussion/898/ifc-file-doesnt-import-open-into-revit)).
- EN: "Files with the official IFC4X3_ADD2 header error on link or import in Revit 2024" ([#928](https://github.com/Autodesk/revit-ifc/issues/928)).
- EN: "Alignment exported as IFC 4x1 from ProVI imports into Civil 3D 2022 but nothing is visible even after Zoom Extents" - IFC 4.1 was withdrawn and never certified ([buildingSMART forum](https://forums.buildingsmart.org/t/ifc-4x1-file-containing-alignment-is-not-opening-in-civil-3d/3830)).

**Why.** Support depends on the Revit build and the IFC add-in; IFC4.x and infrastructure content is only partly readable in building-oriented tools.

**Good assistant behaviour.** Read `FILE_SCHEMA` and the view definition from the header, list representation types used, and recommend the lowest-risk IFC version/view for the receiver ("IFC2x3 CV2.0 if unsure; IFC4 RV when confirmed"). Do not claim that Revit "supports IFC4.3" without a verified version.

### 11. Colors and materials

**Symptoms.**
- EN: pipe colors set by system in Revit do not appear in Archicad; layer mapping works but colors do not ([buildingSMART forum](https://forums.buildingsmart.org/t/how-can-i-control-the-ifc-pipes-colors-revit-to-archicad/2729)).
- EN: colors from Allplan (encoding bar diameter) vanish in Revit and BricsCAD but show in a viewer; style attached to the shape, not the material; 428 duplicate materials ([buildingSMART forum](https://forums.buildingsmart.org/t/where-and-how-will-my-colors-be-saved-in-ifc/1806)).
- ZH: "MAX模型导进Revit材质全没了" ([CSDN](https://ask.csdn.net/questions/8796533)), "Su 导入 Revit 材质总是丢失怎么办？" ([Zhihu](https://zhuanlan.zhihu.com/p/372183287)).

**Why.** In IFC a material is mostly a name, colour is an `IfcSurfaceStyle` attached to the representation or the material; a receiving tool may read only one of these.

**Good assistant behaviour.** Inspect where styles are attached (representation vs material) and report duplicates; suggest mapping materials after import.

### 12. Text encoding, invalid or truncated files

**Symptoms.**
- RU: "Текла просит переименовать файл без спецсимволов, имя только латиница, не помогает" - Cyrillic in the header path suspected ([forum.dwg.ru](https://forum.dwg.ru/showthread.php?t=159943)).
- ES: "ETABS: Could not find ENDSEC at end of file" for a Revit IFC2x3 ([buildingSMART forum](https://forums.buildingsmart.org/t/como-poder-exportar-un-modelo-3d-estructural-realizado-en-revit-a-etabs-por-medio-del-formato-ifc/2985)).
- PT: "Falha de importação de arquivo IFC com Bonsai" - raw Latin-1 bytes instead of `\X\` escapes ([IfcOpenShell #7305](https://github.com/IfcOpenShell/IfcOpenShell/issues/7305)); KO: STEP export writes raw Korean characters instead of escapes ([FreeCAD #33914](https://github.com/FreeCAD/FreeCAD/issues/33914)).
- EN: umlauts wrong in the German Revit mapping file ([revit-ifc #7](https://github.com/Autodesk/revit-ifc/issues/7)).

**Why.** IFC files are ASCII; non-Latin text must be escaped (`\X2\...\X0\`). Exporters that write raw bytes, Mac-Roman text or truncated files fail in strict readers. See [Inside an .ifc file](../../01_ifc_basics/02_ifc_file_anatomy.md).

**Good assistant behaviour.** Check file ending, header, schema string, suspicious bytes; explain it is an exporter defect, not user error; suggest re-export with ASCII-safe path/name.

### 13. Importing IFC into non-Revit tools

**Symptoms.**
- RU: "IFC из Сапфира в автокад не импортируется, системная ошибка, в BimSight открывается нормально" - AutoCAD has no native IFC import ([forum.dwg.ru](https://forum.dwg.ru/showthread.php?t=160240)); "нужно открыть 3D модель IFC в автокаде, редактировать и проектировать по ней" - options: BricsCAD BIM to DWG, IfcConvert, DXF tools ([forum.dwg.ru](https://forum.dwg.ru/showthread.php?t=158006)).
- EN: Tekla models lose connectivity in ETABS because coordinates with 10 decimals are rounded ([BHoM #548](https://github.com/BHoM/ETABS_Toolkit/issues/548)); structural IFC from AXISVM will not load in Bonsai ([IfcOpenShell #6459](https://github.com/IfcOpenShell/IfcOpenShell/issues/6459)).
- RU: "как перенести модель из архитектурной программы в расчётную... через IFC можно?" - IFC is the most practical route but needs cleanup ([forum.dwg.ru](https://forum.dwg.ru/showthread.php?t=33352)).
- ES: "SOPOTARÁ ARCHIVOS IFC?" - an app exports IFC but cannot import it yet ([IngeTrazo #1033](https://github.com/ingelibre/ingetrazo/issues/1033)).

**Why.** Support for IFC import varies by product; analysis software needs members and nodes (analytical model), not solids; IFC from a physical model gives odd wall junctions.

**Good assistant behaviour.** Ask the target program, the purpose (view, check, analysis, editing) and the IFC schema/view. Do not suggest that IFC carries an analytical model unless the file contains `IfcStructuralAnalysisModel`.

### 14. Which export setting should I pick at the source?

**Symptoms.**
- RU: "какой транслятор в Архикаде выбрать для передачи в Ревит, и IFC2x3 или IFC4?" (synthetic); RU (real): how to save an Archicad file via IFC so a lower version can open it ([forum.dwg.ru](https://forum.dwg.ru/showthread.php?t=75685)).
- EN: "what export types exist and when to use Reference vs Design transfer view; how Location by base point works" ([Tekla 2024](https://support.tekla.com/doc/tekla-structures/2024/int_ifc_export)).
- RU: "какой формат выбрать для экспертизы, коллизий, расчёта" - Renga: IFC4 for merge, clash and expertise ([Renga](https://rengabim.com/stati/bol-she-10-formatov-eksporta-importa-v-renga-kakoj-iz-nih-vybrat/)); "при выгрузке в Navisworks SweptSolid отображается некорректно, нужна Tessellation" ([Renga](https://rengabim.com/stati/prohodim-gosekspertizu-informacionnoj-modeli-pravilno/)).
- EN: ArchiCAD pain points - stairs drawn as beams, wrong home storey, overlaps break quantities, no BEP ([BIM Corner](https://bimcorner.com/exporting-ifc-from-archicad/)); proxies and extra storeys from export mistakes ([BIM Corner](https://bimcorner.com/10-common-ifc-export-mistakes-to-avoid-part-1/)).
- IT: "come si esporta un IFC? meglio 2x3 o IFC4?" ([ACCA Biblus](https://biblus.acca.it/come-creare-un-file-ifc/)).
- ZH-TW: CIC Hong Kong workshop on IFC exchange Archicad and Revit with clash checks ([CIC](https://www.bim.cic.hk/zh-hant/events/detail/304)).

**Why / fix.** Pick the purpose first. Viewing and coordination: IFC2x3 Coordination View 2.0 (the classic safe default) or IFC4 Reference View. Editing in the receiver: Design Transfer View is unofficial and must be tested. Tekla: "surface geometry" for viewing; Coordination View 2.0 for editable geometry; "steel fabrication view" to keep assembly presentation. Verify by re-opening the file in a neutral viewer. See [IFC versions and views](../../01_ifc_basics/01_what_is_ifc_and_versions.md).

**Good assistant behaviour.** Ask who receives the file and for what, then recommend one setting and say what it costs. If a file is loaded, read the header (`FILE_SCHEMA`, view definition, exporting application) to learn which translator/version actually produced it.

### 15. Non-IFC sources: DWG, SketchUp, 3ds Max, ArchiCAD `.pln`

**Symptoms.**
- ZH: "archicad的pln文件怎么弄进revit" - typically via IFC or DWG ([Baidu Zhidao](https://zhidao.baidu.com/question/593298625.html)).
- RU: "как перевести ifc в dwg и какими программами" ([forum.dwg.ru](https://forum.dwg.ru/showthread.php?t=96356)).
- IT: "ho solo il DWG, come lo converto in IFC?" ([ACCA Biblus](https://biblus.acca.it/come-convertire-un-file-dwg-in-ifc-in-modo-semplice/)).
- ZH: "[提案] preview_dwg_beams 加 includeGeometry 參數..." - an MCP user wants CAD wall layers turned into Revit walls ([REVIT_MCP_study #150](https://github.com/shuotao/REVIT_MCP_study/issues/150)).

**Why.** DWG has lines and layers, not walls; native pln has no direct Revit importer.

**Good assistant behaviour.** Be explicit that conversions create geometry with little semantics; propose previewing detected elements before creating anything; confirm level, wall type and layer names; report skipped segments.

## Real questions

Paraphrased questions from the dataset (original-language paraphrase, English gloss, persona, source). Persona values are the dataset's inferred roles. A trailing "*" (es*, ko*) means the source is non-English but the dataset stores the paraphrase in English; German rows show the original German title plus the dataset's English paraphrase.

| lang | question (original-language paraphrase) | EN gloss | persona | source |
|---|---|---|---|---|
| en | Asks for official feedback on the two import methods; Open yields in-place families without IFC data and cannot map classes for Tekla assembly sub-elements, Link duplicates geometry | Why do Open and Link give such different results? | bim_manager | [#223](https://github.com/Autodesk/revit-ifc/issues/223) |
| en | Export offers internal origin, survey point or PBP; import offers nothing; cites an old Ideas post saying it is not possible | Can import use the project base point? | bim_coordinator | [#320](https://github.com/Autodesk/revit-ifc/issues/320) |
| en | Models with shared coordinates look right in other viewers but not in Revit; googled and watched videos but unsure how to link properly | Georeferenced IFCs line up elsewhere but not in Revit 2022 | bim_coordinator | [#566](https://github.com/Autodesk/revit-ifc/issues/566) |
| en | In 2025-2027 Link IFC positions geometry higher and creates levels at twice the correct elevation; Open IFC is fine | Wrong height after Link in new Revit | bim_coordinator | [#990](https://github.com/Autodesk/revit-ifc/issues/990) |
| en | IFC project north ends up pointing to Revit true north; regression since 2022 | Link rotates my model | bim_coordinator | [#522](https://github.com/Autodesk/revit-ifc/issues/522) |
| en | Link IFC versus linking the cached .ifc.rvt yields opposite rotation; people link the .ifc.rvt to avoid reload distrust | Same file, two rotations | bim_coordinator | [#710](https://github.com/Autodesk/revit-ifc/issues/710) |
| en | One chair family exports fine and displays in BIM Vision, but Revit cannot link it back; Link just hangs | Link hangs on a tiny file | other | [#951](https://github.com/Autodesk/revit-ifc/issues/951) |
| en | Is there a way to get Revit to recognize walls when importing IFC? Currently all generic models | Why are my walls generic? | architect | [#571](https://github.com/Autodesk/revit-ifc/issues/571) |
| en | Consultants send IfcFlowSegment instead of specific classes; team built HVAC mapping tables but must navigate IFC Options every time | Make the import mapping table easier to reuse | bim_manager | [#798](https://github.com/Autodesk/revit-ifc/issues/798) |
| en | Wants IfcSpace converted to Rooms (architectural link) or Spaces (MEP link) | Spaces should become Rooms | mep_engineer | [#15](https://github.com/Autodesk/revit-ifc/issues/15) |
| en | Windows from an Archicad IFC are offset out of walls in Revit 2025-27 | Windows float outside walls | architect | [#1019](https://github.com/Autodesk/revit-ifc/issues/1019) |
| en | Doors appear in 3D but are invisible in floor plan; the Model footprint representation is not displayed | Archicad door swings missing in plan | architect | [#358](https://github.com/Autodesk/revit-ifc/issues/358) |
| en | Wants to link many IFCs from a macro; the C# code makes the link but no data comes in | Bulk-link IFCs through the API | developer_programmer | [#380](https://github.com/Autodesk/revit-ifc/issues/380) |
| en | Linking an updated IFC generates a new rvt and a new shared parameter file with different GUIDs | Re-link breaks schedules | bim_coordinator | [#408](https://github.com/Autodesk/revit-ifc/issues/408) |
| en | Files with the official IFC4X3_ADD2 header error on link in Revit 2024; user traced it to the header schema name | IFC4.3 file will not link | civil_infra_engineer | [#928](https://github.com/Autodesk/revit-ifc/issues/928) |
| en | Revit cannot open an IFC with IfcTriangulatedFaceSet; do I need to link instead? | IFC4 geometry fails on Open | bim_coordinator | [#587](https://github.com/Autodesk/revit-ifc/issues/587) |
| en | Blender monkey mesh exported to IFC only partly appears in Revit; primitives work | Why does my Blender IFC half-appear? | student_beginner | [osarch](https://community.osarch.org/discussion/95/ifc-export-newbie-question) |
| en | House exported from Bonsai looks fine elsewhere, but in Revit wall heights and door/window positions are lost | Beginner's IFC breaks in Revit | student_beginner | [osarch](https://community.osarch.org/discussion/3280/i-am-a-beginner-i-created-a-file-in-bonsai-but-it-doesnt-appear-correctly-in-3d-in-revit) |
| en | Terrain TINs from 12D with very obtuse triangles break the spot-elevation tool in Revit | Civil terrain IFC unusable for spot elevations | civil_infra_engineer | [#511](https://github.com/Autodesk/revit-ifc/issues/511) |
| en | Alignment exported as IFC 4x1 imports into Civil 3D 2022 but nothing is visible | Alignment IFC shows nothing | civil_infra_engineer | [forum](https://forums.buildingsmart.org/t/ifc-4x1-file-containing-alignment-is-not-opening-in-civil-3d/3830) |
| en | Tekla IFC4 export component ignores a custom base point and uses the model origin | Base point not honored | developer_programmer | [Grasshopper-TeklaDrawingLink #147](https://github.com/LetsConstructIT/Grasshopper-TeklaDrawingLink/issues/147) |
| en | Reference-model placement from an MCP tool ignores the model's 3D rotation, so a rotated IFC overlay is reported in the wrong place | MCP tool misplaces rotated reference model | bim_coordinator | [tekla-mcp-server #44](https://github.com/tempalg1n/tekla-mcp-server/issues/44) |
| en | Contractor needs IFC for cost estimation but we have no BEP or template; stairs as beams, overlaps | Archicad IFC pain points | architect | [BIM Corner](https://bimcorner.com/exporting-ifc-from-archicad/) |
| en | Got IFC0000101 "update file to supported IFC version"; exported IFC2x3, how to export IFC4 with IFC+SG settings | Wrong IFC version for the checker | architect | [IFC-Repair-Studio](https://github.com/noddlesskcho/IFC-Repair-Studio) |
| en | Revit-generated IFC4 fails a strict parser: odd date format, extra parentheses in point lists | Strict readers reject a Revit file | developer_programmer | [forum](https://forums.buildingsmart.org/t/4605) |
| en | Archicad exports a revised IFC; how to update the already imported model without re-import? | Update an imported model | architect | [osarch](https://community.osarch.org/discussion/comment/13211#Comment_13211) |
| en | Blender cube shows in BIMVision but not in Revit 2021 | Simple cube invisible in Revit | student_beginner | [osarch](https://community.osarch.org/discussion/462/blenderbim-add-on-ifc-export-not-visible-in-revit) |
| en | Revit user is an absolute beginner in IFC and Bonsai; what next steps to build foundations? | Migrating from Revit to Bonsai | bim_coordinator | [osarch](https://community.osarch.org/discussion/3765/roadmap-for-revit-migrator-to-bonsai-bim-absolute-beginner) |
| en | Autodesk asks users how Revit should better support IFC workflows | Do you need better IFC in Revit? | owner_client | [buildingSMART forum](https://forums.buildingsmart.org/t/next-steps-for-ifc-support-in-revit/3580) |
| ru | заказчик требует выдавать IFC и грузить в Ревит, стандартный экспорт с настройками по умолчанию даёт в Ревите только оси | Tekla default export shows only grids in Revit | structural_engineer | [forum.dwg.ru](https://forum.dwg.ru/showthread.php?t=146029) |
| ru | через IFC конструкции из Теклы в Ревит не передаются нормально, при открытии в Ревите элементы теряются, подскажите как передать | Tekla structures lose elements on opening in Revit | structural_engineer | [forum.dwg.ru](https://forum.dwg.ru/showthread.php?t=146029) |
| ru | при импорте IFC архитектурных моделей из других программ элементы приходят как тела, а не как родные объекты Ревита, хочу их редактировать | Imported elements are dumb solids, I want to edit | architect | [forum.dwg.ru](https://forum.dwg.ru/showthread.php?t=166052) |
| ru | можно ли редактировать семейство из IFC в Ревите | Can an imported IFC be edited as a family? | architect | [forum.dwg.ru](https://forum.dwg.ru/showthread.php?t=130296&page=2) |
| ru | при экспорте из Архикада в IFC и вставке в Ревит стёкла жёлтые и толщиной в метры, часть перегородок пропала | Archicad IFC in Revit: yellow thick glass, missing partitions | architect | [forum.dwg.ru](https://forum.dwg.ru/showthread.php?t=154396) |
| ru | импортирую IFC из сапфира, выдаёт System Error encountered during import, как правильно экспортировать | SAPFIR IFC gives a system error on import | structural_engineer | [forum.dwg.ru](https://forum.dwg.ru/showthread.php?t=160240) |
| ru | Текла просит переименовать файл без спецсимволов, имя только латиница, не помогает | Tekla refuses a Latin-named IFC (header path suspected) | structural_engineer | [forum.dwg.ru](https://forum.dwg.ru/showthread.php?t=159943) |
| ru | нужно открыть 3D модель IFC в автокаде, редактировать и проектировать по ней, у кого получилось | Need to open IFC in AutoCAD and design on it | structural_engineer | [forum.dwg.ru](https://forum.dwg.ru/showthread.php?t=158006) |
| ru | как обмениваются данными Advance Steel и Archicad, какая последовательность для правильной передачи модели | How to move a model from Advance Steel into Archicad | structural_engineer | [forum.dwg.ru](https://forum.dwg.ru/showthread.php?t=163697) |
| ru | колонны из Теклы в Ревите: материал и тонирование не меняются; арматура и узлы не переносятся | Tekla columns in Revit: material fixed, rebar missing | structural_engineer | [forum.dwg.ru](https://forum.dwg.ru/showthread.php?t=155997) |
| ru | экспорт в ifc из Теклы 2017 для Field 3D не работает как надо, настройки не помогают | Tekla 2017 export for Field 3D misbehaves | structural_engineer | [forum.dwg.ru](https://forum.dwg.ru/showthread.php?t=146367) |
| ru | часть свойств потерялась после импорта IFC, какие настройки экспорта выбрать, почему файл не читается | Renga IFC: properties missing after import | architect | [Renga blog](https://blog.rengabim.com/2021/08/ifc.html) |
| ru | как перенести модель из архитектурной программы в расчётную, какой формат лучше, через IFC можно? | Archicad to analysis software via IFC? | structural_engineer | [forum.dwg.ru](https://forum.dwg.ru/showthread.php?t=33352) |
| ru | нужны тела DWG Solid а не сетки, цепочка Archicad-IFC2x3-AutoCAD Architecture | Get solids, not meshes, from Archicad into AutoCAD | architect | [forum.dwg.ru](https://forum.dwg.ru/showthread.php?t=75883) |
| ru | при выгрузке в Navisworks SweptSolid отображается некорректно, нужна Tessellation | What geometry type should Renga export for Navisworks? | bim_coordinator | [Renga](https://rengabim.com/stati/prohodim-gosekspertizu-informacionnoj-modeli-pravilno/) |
| ru | нужно выгрузить 3D модель из Plant 3D в IFC; Codemill платный и с ручным маппингом, через Navisworks не экспортирует | Plant 3D to IFC without losing data | developer_programmer | [forum.dwg.ru](https://forum.dwg.ru/showthread.php?t=173570) |
| ru | стоит ли переходить на Renga вместо Ревита, как у неё с обменом через IFC | Is Renga ready; how reliable is its IFC? | architect | [forum.dwg.ru](https://forum.dwg.ru/showthread.php?t=149046) |
| zh | ifc导入revit之后三维视图里什么都看不到，是哪里的问题 | Nothing in 3D after IFC import | architect | [Baidu Zhidao](https://zhidao.baidu.com/question/341569640619976845.html) |
| zh | Revit导入IFC后一片空白怎么办 | Blank view after IFC import | bim_coordinator | [cnblogs](https://www.cnblogs.com/OverloadBachPunk/p/14452654.html) |
| zh | 把REVIT、ARCHICAD、TEKLA匯出的IFC再匯入REVIT，平面看得到物件，3D卻找不到 | Plan shows the objects, 3D does not | bim_coordinator | [Pixnet](https://housegear.pixnet.net/blog/posts/3042268210) |
| zh | tekla导出ifc到revit后3D视图里看不到模型 | Tekla IFC invisible in Revit 3D | structural_engineer | [Zhihu](https://www.zhihu.com/question/60173683) |
| zh | Revit打开IFC元素丢失或变形怎么办 | Missing or distorted elements when opening IFC | bim_coordinator | [CSDN](https://ask.csdn.net/questions/8391346) |
| zh | IFC转Revit模型后体积暴涨怎么减肥 | 151 MB Tekla IFC becomes 2 GB; slim down | structural_engineer | [CSDN](https://blog.csdn.net/zzutt/article/details/121492254) |
| zh | MAX模型导进Revit材质全没了 | Materials lost from Max into Revit | architect | [CSDN](https://ask.csdn.net/questions/8796533) |
| zh | archicad的pln文件怎么弄进revit | How to bring a pln file into Revit | architect | [Baidu Zhidao](https://zhidao.baidu.com/question/593298625.html) |
| zh | Tekla和Revit互转 | How to convert between Tekla and Revit | structural_engineer | [Zhihu](https://www.zhihu.com/question/30485422) |
| zh | 無論IFC匯入或匯出到各BIM軟體，模型失真或遺失的情況仍會發生 | Thesis: IFC exchange still loses or distorts geometry | researcher_academic | [NCU thesis](https://ir.lib.ncu.edu.tw/ir/bitstream/987654321/64812/1/index.html) |
| ja | Rhinoで作ったモデルをIFCに出して確認申請用BIMや引き渡しに使えるのか。見た目は合っていても分類や属性が使えない | Can a Rhino model go to IFC for permit/handover? Looks right but classification/attributes unusable | bim_manager | [note](https://note.com/bim_tool_lab/n/nf529aa5d5cc0) |
| ja | IFCに書き出したらモデルの半分が消えていた。ただのソリッド、階に紐づかないレイヤ、非表示要素が原因 | Half the elements vanished after IFC export | architect | [note](https://note.com/toshio_nakamura/n/nc8db42ce3191) |
| ja | IFC由来の要素をMEP要素に変換するアドインを作ろうとしたが、編集不可だったりパラメータが設定できず断念した | Tried to convert imported IFC into MEP elements, gave up | developer_programmer | [Qiita](https://qiita.com/KengoTanaka-BIM/items/6cec74e04bf581b21cf5) |
| de | IFC verlinken vs. Data Exchange laden in Revit (linked IFC bloats my project; should I use Data Exchange?) | Link IFC or Autodesk Data Exchange? | bim_coordinator | [BIM me up](https://bim-me-up.com/ifc-verlinken-vs-data-exchange-laden-in-revit/) |
| de | IFC ProvisionForVoid in Revit - Öffnen vs. Referenzieren / Binden (openings do not cut walls) | Openings from IFC do not cut my walls | bim_coordinator | [BIM me up](https://bim-me-up.com/ifc-provisionforvoid-in-revit-offnen-vs-referenzieren-binden/) |
| es* | opening or linking an IFC gives no choice of coordinate system (Arkance article) | No coordinate-system choice when linking | bim_coordinator | [Arkance](https://emea.support.arkance.world/hc/es/articles/36464850969234-Using-IFC-files-with-a-Shared-Coordinates-system) |
| es | Problema al importar modelo de Revit en plantilla de estructuras; todos los elementos asignados a IFC pero ETABS muestra mensaje de error | Revit IFC into ETABS errors ("Could not find ENDSEC") | structural_engineer | [buildingSMART forum](https://forums.buildingsmart.org/t/como-poder-exportar-un-modelo-3d-estructural-realizado-en-revit-a-etabs-por-medio-del-formato-ifc/2985) |
| es | quisiera saber si será posible importar archivos IFC? | Will the app import IFC? | student_beginner | [IngeTrazo #1033](https://github.com/ingelibre/ingetrazo/issues/1033) |
| it | come carico il file di mappatura classi IFC in Revit prima di aprire l'IFC cosi le porte restano porte? | How to load the class mapping file so doors stay doors | architect | [ACCA Biblus](https://biblus.acca.it/ifc-class-mapping-file/) |
| it | come si esporta un IFC? meglio 2x3 o IFC4? | Export an IFC: 2x3 or 4? | student_beginner | [ACCA Biblus](https://biblus.acca.it/come-creare-un-file-ifc/) |
| it | ho solo il DWG, come lo converto in IFC? | Convert a DWG to IFC | architect | [ACCA Biblus](https://biblus.acca.it/come-convertire-un-file-dwg-in-ifc-in-modo-semplice/) |
| pt | Falha de importação de arquivo IFC com Bonsai (IFC from ArchiStation does not open in Bonsai on Ubuntu 24.04, even after downgrading Blender) | ArchiStation IFC will not open in Bonsai (raw Latin-1 bytes) | student_beginner | [IfcOpenShell #7305](https://github.com/IfcOpenShell/IfcOpenShell/issues/7305) |
| ko* | several third-party commercial 3D CAD apps fail to open or display characters from a STEP export with raw non-ASCII text | FreeCAD writes unescaped Korean/Japanese/Chinese | developer_programmer | [FreeCAD #33914](https://github.com/FreeCAD/FreeCAD/issues/33914) |
| no | hvordan går vi fra armeringsmodell til bestilling og produksjon med åpne standarder? | From rebar model to ordering/production with open standards | structural_engineer | [buildingSMART Norge](https://www.buildingsmart.no/standarder/publikasjoner-og-veiledninger.html) |
| zh | [提案] 預覽只回傳數量，AI想把CAD牆圖層翻成Revit牆時拿不到每段位置 | MCP preview returns only counts, no coordinates for converting CAD walls | architect | [REVIT_MCP_study #150](https://github.com/shuotao/REVIT_MCP_study/issues/150) |

## Ready test prompts

Synthetic prompts (not real quotes), curated from the dataset and rewritten to sound like people typing quickly to an assistant connected to an IFC model or Revit. "Base" = the dataset synthetic id it was adapted from, or "new" if written here from a real record. Difficulty is for the assistant. All assume a file or Revit model is loaded unless the expected behavior says otherwise.

| # | lang | prompt | type | difficulty | expected behavior | base |
|---|---|---|---|---|---|---|
| 1 | en | whats the diff between open ifc and link ifc in revit? which one gives me editable walls | how_to | easy | Explain Link (DirectShape reference, `.ifc.RVT` cache) vs Open (separate path, in-place or generic, loses IFC data); say neither gives parametric walls; ask what the user needs to do | en-autodesk-revit-import-s013 |
| 2 | en | linked an archicad ifc in revit and its rotated wrong. true north vs project north?? it was fine in 2020 | troubleshooting | medium | Read `IfcGeometricRepresentationContext` true north and `IfcMapConversion`; explain Revit's true-north handling and the reported 2022+ behavior; ask Revit/add-in version and positioning used | en-autodesk-revit-import-s015 |
| 3 | en | linked ifc sits way too high in revit 2026 and the levels are at double height. open ifc was fine, whats going on | troubleshooting | medium | Check site/building elevation and Z in the file; mention the reported duplicated-Z bug in Link for Revit 2025-2027 and Open IFC as comparison; do not claim a fix without a version | en-gh-revit-ifc-s015 |
| 4 | en | archicad ifc just came in. how many IfcBuildingElementProxy are there and what are they actually, walls? need to fix before it goes to revit | model_task | medium | Count proxies, group by Name/ObjectType/layer/classification, suggest classes; no writes without confirmation | en-roundtrip-s001 |
| 5 | en | revit makes all my walls generic models. what class and predefined type do they have in the ifc, IfcWall or proxy? | model_task | easy | Report class, PredefinedType and type object for sample walls; explain import category mapping | en-us-canada-infra-s010 |
| 6 | en | linked the tekla ifc and now everything is doubled, assembly plus parts. how do i avoid that | troubleshooting | medium | Explain assembly + sub-parts both imported; list assemblies and children from `IfcRelAggregates`; suggest mapping/deleting assemblies | en-tekla-s012 |
| 7 | en | windows from the archicad ifc end up outside the wall in revit 2025, in 2024 fine. can u check the file | troubleshooting | hard | Inspect `IfcRelFillsElement`/`IfcRelVoidsElement` and window vs wall placements; say a Revit regression is possible and cannot be fixed in the file | new (from #1019) |
| 8 | en | tekla ifc: list every IfcElementAssembly with its child parts and tell me if parts will double up when i link it in revit | model_task | hard | Traverse `IfcRelAggregates`, list assemblies/children, state duplication risk | en-roundtrip-s004 |
| 9 | en | did the tekla base point export go through IfcMapConversion or IfcSite? need to know before linking into revit | model_task | medium | Look for map conversion/projected CRS vs `IfcSite` placement and lat/long; report values and what that means for placement | en-tekla-s002 |
| 10 | en | I exported from revit, edited in archicad, got it back. did the GUIDs survive? compare original.ifc and returned.ifc, whats lost | model_task | hard | Match GlobalIds, list matched/added/removed, property-set and geometry differences; caveat that exporters may regenerate IDs | en-roundtrip-s003 |
| 11 | en | exported 4000 objects from tekla, the import shows 3900. which ones have no representation? | model_task | medium | List elements without `Representation`, group by class; suggest B-rep fallback at source | en-tekla-s009 |
| 12 | en | my cube from blender shows in bimvision but not in revit. is it even in a storey? | model_task | easy | Check spatial containment, assign to a storey only after confirmation, check vertices; mention outdated IFC add-on | en-osarch-s007 |
| 13 | en | doors from the archicad ifc are invisible in plan in revit. do they even have a footprint rep | model_task | medium | Inspect door representations for Plan/FootPrint contexts and report presence | en-autodesk-revit-import-s010 |
| 14 | en | linked the ifc and the openings dont cut my walls in revit | troubleshooting | medium | Explain `IfcOpeningElement` imported as separate geometry, link-then-bind trade-off, hiding subcategories | en-blogs-linkedin-s016 |
| 15 | en | Link IFC hangs forever on a 5 MB file, kill Revit every time. Open IFC works. is my file corrupt? | troubleshooting | medium | Do not call it corrupt; check file for obvious issues and element counts; report the known hang class and the "empty file then link the `.ifc.RVT`" workaround | new (from #951) |
| 16 | en | I need to link 40 ifc files into Revit from a script, whats the proper way and what breaks? | how_to | hard | Explain API link route (Importer/RevitLinkType from IFC, UI thread, no open transaction), caveats from #380; offer to prepare the list; ask Revit version | new (from #380) |
| 17 | en | check which translator this archicad ifc was exported with and if my custom properties made it through | model_task | medium | Read header/`IfcApplication`, list property sets present, report presence of user-defined ones per class | en-graphisoft-s001 |
| 18 | en | which archicad translator should i use when sending to a structural engineer on revit? | how_to | easy | Explain Coordination View 2.0 vs Reference/Design Transfer and trade-offs; ask IFC2x3 vs IFC4 and whether editing is needed | en-graphisoft-s014 |
| 19 | en | reference view or design transfer when i send tekla to the architect to link in revit | how_to | easy | Reference for viewing/linking, Design Transfer only if the receiver edits; recommend per use | en-tekla-s011 |
| 20 | en | my UDA isnt in the tekla ifc, the numeric ones come out empty | troubleshooting | medium | Check pset config contains the UDA and types; list properties on beams; mention reported numeric-UDA gaps | en-tekla-s013 |
| 21 | en | civil 3d export, what ifc classes are in here? terrain, alignment, pipes? will revit even see them | model_task | medium | List classes, alignments, geographic elements; state Revit import limits for IFC4.3-type content; do not overclaim | en-roundtrip-s017 |
| 22 | en | ifc import into vectorworks gives dumb solids, no walls. whats the geometry representation in this file | model_task | hard | Report representation types (Brep, tessellation, swept solid) per class and explain why they import as generic solids | en-allplan-vw-bentley-s004 |
| 23 | en | allplan export - half my walls came out as proxy?? list what ifc class each wall got | model_task | medium | List `IfcWall` vs `IfcBuildingElementProxy`, name affected elements, suggest source-side fix | en-allplan-vw-bentley-s001 |
| 24 | en | the ifc i got from revit wont open in etabs, says ENDSEC missing. what version is it and is it truncated? | troubleshooting | medium | Check schema, end-of-file, size sanity, encoding; report cause and re-export advice | es-vm-s008 |
| 25 | en | i get an error linking a file with IFC4X3_ADD2 in the header in revit 2024, can u look | troubleshooting | medium | Read `FILE_SCHEMA`; explain reported header issue and the `IFC4X3` workaround as unofficial; recommend a supported schema | new (from #928) |
| 26 | en | the allplan colors dont show in revit. do they have an IfcSurfaceStyle and what is it attached to | model_task | medium | Inspect style assignment on representation vs material, report duplicates | es-roundtrip-s010 |
| 27 | en | hey the architects ifc wasnt delivered with any rooms. everything is IfcSpace and they obstruct my views in the link, how do i hide them | how_to | easy | Explain `IfcSpace.INTERNAL` subcategory hiding in Revit Links Display Settings; say Link will not make Rooms | new (from #15) |
| 28 | en | I want to send IFC to the contractor from Archicad but there is no BEP. what do I even check before I send | how_to | medium | Ask purpose and receiver; checklist (classification, storeys, survey point, properties mapped, overlap check); verify in a neutral viewer | new (from BIM Corner) |
| 29 | ru | ифс открывается в ревите минут 40 и потом файл 800 мб, что делать, связью лучше? | troubleshooting | medium | Explain Link vs Open/cache; ask file size and element mix; propose reducing the model | ru-dwg-revit-s009 |
| 30 | ru | открыл ифс в ревите, пусто, одни оси видны. файл весит нормально. что не так | troubleshooting | easy | Check how many elements carry geometry; then phase of the link and view, visibility; recommend recreating the 3D view | ru-autodesk-telegram-s013 |
| 31 | ru | из робота выгрузил ифс, в ревит колонны пришли обобщенными, как сделать чтоб были колоннами | troubleshooting | medium | Check IfcColumn vs proxy; explain import class mapping; advise Link vs Open | ru-eng-s010 |
| 32 | ru | все проксики с именем Wall* переделай в IfcWall и сохрани новый файл | model_task | hard | Find proxies by name, reclassify, preserve GlobalIds, save as a new file, report counts; confirm before writing | ru-dwg-other-s007 |
| 33 | ru | в нависе ифц улетел куда-то в сторону, координаты проверь, единицы ок? | troubleshooting | medium | Check `IfcSite` placement, units, large coordinates; suggest shifting | ru-dwg-other-s014 |
| 34 | ru | ифс из архикада в ревите уехал и повернут, глянь IfcMapConversion, site и CRS, где у него ноль | model_task | hard | Report site placement, map conversion, true north, bounding box and distance from origin | ru-roundtrip-s006 |
| 35 | ru | как из архикада ифс в ревит затащить чтоб были стены а не обобщенные модели? open или link? | how_to | medium | Explain Open vs Link, class mapping, DirectShapes, translator preparation | ru-roundtrip-s007 |
| 36 | ru | bcf из нависа в ревит не наводится на элементы, пишет не найдено. ифс подгружен как link | how_to | medium | Explain BCF viewpoint IfcGuid vs Revit element identity; linked-IFC limitations; ask how the IFC GlobalId parameter is exposed | ru-clash-s008 |
| 37 | ru | какую версию ифс выбрать при экспорте из ренги, 2x3 или 4? координатор сидит в нависе | how_to | easy | Explain 2x3 vs 4 trade-offs and view; recommend IFC4 Reference View unless the receiver is limited; ask Navisworks version | ru-renga-nanocad-s013 |
| 38 | ru | ифс из аллплана улетел на 3 км от начала координат в ревите, глянь где у него смещение и какие координаты у IfcSite | model_task | medium | Report site placement and extents, compute offset to origin, suggest georeference fix | mul-coord-s007 |
| 39 | zh | 把DWG的A-WALL图层翻成墙，放在2F，墙型用RC墙200 | model_task | hard | Read the layer, detect centerlines, preview count and skipped segments, ask to confirm before creating; level 2F and named type | zh-revit-auto-s012 |
| 40 | zh | tekla导出的钢结构ifc导进revit构件丢了不少，怎么设置才能完整导入 | how_to | medium | Explain export type, link vs open, class mapping, assemblies, verification by counts | zh-roundtrip-s009 |
| 41 | zh | 结构ifc和建筑ifc合不上，差了好远，对比下两个文件的原点和基点 | model_task | hard | Compare site refs, map conversion, placements, units; report offset and likely cause | zh-zhihu-s007 |
| 42 | zh | IFC匯入Revit後平面有3D看不到，是不是階段的問題 | how_to | easy | Explain phase filter / view phase, link vs open | zh-tw-hk-s015 |
| 43 | ja | IFCをRevitで開くと属性が全然出てこない…リンクとか開くとか何が違う？ | troubleshooting | medium | Explain Open vs Link, parameter mapping, IFC version/MVD; check whether Psets exist in the file | ja-japan-s013 |
| 44 | es | importé el ifc de archicad en revit 2025 y las ventanas quedaron fuera del muro, en el 2024 andaba bien, qué onda | troubleshooting | medium | Explain the known regression, check hosting relations and offer to verify openings | es-latam-s004 |
| 45 | de | wie krieg ich beim IFC Export aus Archicad den Projektnullpunkt und die Vermessungskoordinaten sauber rein? | how_to | medium | Explain survey point/project origin settings and `IfcMapConversion`; ask Archicad version | de-coord-s018 |
| 46 | fr | Quels réglages d'export IFC dans Archicad pour que Revit récupère correctement murs et dalles ? | how_to | medium | Explain translator, view/IFC version, element classification and geometry options | fr-roundtrip-s013 |
| 47 | ko | civil3d ifc랑 revit 모델 좌표가 안맞아요 z값이 이상함 어디서 틀어진건지 봐줘 | troubleshooting | hard | Inspect placement, map conversion, units and elevation; explain Link IFC Z behavior | ko-roundtrip-s015 |
| 48 | pt | como levar o modelo da estrutura metálica do Tekla pro Robot via IFC sem perder os perfis? | how_to | hard | Explain profiles in `IfcMaterialProfileSet`, IFC limits for analysis transfer, alternatives; inspect profiles if a file is given | pt-struct-s011 |

## Edge cases and traps for MCP testing in this area

1. **"Import" is ambiguous.** Users say import for Link IFC, Open IFC, Insert, or even drag-and-drop. A good assistant asks which, because Link and Open behave differently.
2. **No file or no Revit session.** "My IFC is rotated" with nothing loaded: the assistant should say what it can read (nothing yet) and request the file or the Revit session, not invent numbers.
3. **Predicting Revit from an IFC.** An IFC-only server cannot know what Revit will draw. It can report class counts, proxies, assemblies, placements and header facts, and should label Revit-side behavior as version-dependent. Good oracle: element counts per IFC class vs counts per category in the linked model.
4. **Version-specific bugs.** Claims like "this is fixed in Revit 2027" or "Open IFC reads IFC4" need a Revit build and add-in version. An answer that sounds certain without a version is a failure. The tracker facts are as reported by users and maintainers.
5. **The `.ifc.RVT` cache.** Deleting it forces a rebuild; linking it instead of the IFC can rotate differently (#710). A tester can check whether the assistant knows this file exists and is derived.
6. **"It opens fine in my viewer, so the file is fine."** Viewers are lenient. Don't conclude Revit is wrong or the file is wrong from one viewer; also don't declare corruption.
7. **Write requests on the original file.** "Turn all proxies named Wall* into IfcWall" must produce a copy, preserve GlobalIds, report counts, and flag that predefined types and type objects may not be valid. Never overwrite silently.
8. **Coordinate traps.** Double application of `IfcMapConversion` when the model is already in projected coordinates; geometry far from the origin; units mm vs m; true north vs project vs grid north. Check units before reporting offsets in metres.
9. **Header and schema strings.** `IFC4X3_ADD2` vs `IFC4X3`, withdrawn IFC4.1 files, ifcXML/ifcZIP/ifcJSON inputs. An assistant should read `FILE_SCHEMA` before advising.
10. **Encoding.** Cyrillic, umlaut, Chinese or Korean names stored raw or as `\X2\`; paths with non-Latin characters; Tekla path limit (247 characters). Test with names in several scripts.
11. **Truncated/zero-byte or ZIP-wrapped files** (e.g. "could not find ENDSEC"): the assistant should detect and say so rather than hallucinate content.
12. **Tekla assemblies.** `IfcElementAssembly` with many parts, single-child assemblies, rebar/bolts present or absent; multiple `IfcBuilding` under one site; check the assistant doesn't double count.
13. **Rotated reference models.** The tekla-mcp-server issue #44 pattern: the position is applied, the rotation is not; a tester should check that the tool's output reports both.
14. **IfcSpace and openings.** Items intended as helper geometry (`IfcOpeningElement`, `IfcSpace`) should not be reported as "extra walls" or "errors"; the assistant should know they become Generic Model subcategories.
15. **Prompt-injection in IFC strings.** Names, descriptions or property values may contain instruction-like text. They are data; the assistant must not follow them.
16. **Revit MCP operations.** Linking through the API needs the UI thread and no open transaction on the host; elements inside a linked IFC are DirectShapes reached through the link instance, so check that a tool handles links and not only host elements; destructive actions (delete assemblies, unload links) need confirmation.
17. **Round-trip expectation.** "Export, edit in another tool, import back" should trigger a gentle correction (IFC is a reference format) plus a GlobalId comparison offer, not a promise.
18. **Out-of-scope software.** Questions about Renga, SAPFIR, nanoCAD, PKPM, Edificius settings where the KB is thin: the assistant should say what it knows and mark the rest as unverified.

## Related docs

- [Revit IFC import and link reference](../../03_software/revit/ifc_import_link_reference.md)
- [Revit IFC export reference](../../03_software/revit/ifc_export_reference.md)
- [IFC in other authoring tools (Archicad, Tekla, Allplan, Renga, ...)](../../03_software/authoring_tools_ifc.md)
- [Viewers, checkers, CDE and converters](../../03_software/viewers_checkers_cde_converters.md)
- [IFC in real projects (reference vs design transfer)](../../01_ifc_basics/00_ifc_in_real_projects.md)
- [What is IFC, versions and views](../../01_ifc_basics/01_what_is_ifc_and_versions.md)
- [Inside an .ifc file (header, encoding, ifcZIP)](../../01_ifc_basics/02_ifc_file_anatomy.md)
- [Geometry, placement, coordinates, units](../../01_ifc_basics/06_geometry_placement_coordinates_units.md)
- [Materials, classification, types, styles](../../01_ifc_basics/07_materials_classification_types_styles.md)
- [MCP servers and AI tools](../../04_open_source/mcp_servers_and_ai_tools.md)
- [Multilingual glossary](../../08_glossary/glossary_multilingual.md)
- Sibling topic file: [File size, viewing IFC, converting formats](file_size_viewing_conversion.md)
