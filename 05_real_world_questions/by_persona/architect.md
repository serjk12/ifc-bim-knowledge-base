# Architect: who they are and what they do with IFC

**Last built: 2026-11-06 · Persona code:** `architect` · **Data behind this page:** 322 records (197 real, 125 synthetic; `python tools/kb.py stats --persona architect`). Languages: en 202, zh 28, ru 24, es 16, it 11, fr 9, ja 9, de 6, ko 3, nl 3, pt 3, pt-BR 3 (+ vi, no, da, tr, el).

## In plain words

An architect draws the building. In the model that means walls, floors, doors, windows, rooms, stairs and facades, built in a program such as Revit, Archicad, Allplan, Vectorworks, Renga, SketchUp or (for open-source fans) Bonsai/Blender. The architect's own work stays in that program's native file. **IFC is what they hand to others**: the engineer who needs the walls and floors, the cost estimator, the contractor, a city office that wants a model for permit review. And it is what they **receive** from consultants (structure, HVAC) to see the whole building.

For most architects IFC is a *black box*: you press "Export", something comes out, and a day later somebody says the walls are missing or the file has no colours. They rarely care about the IFC schema; they care about three questions: **Did everything come across? Is it still editable? Will the other side accept it?** That shows in the data: 120 of 322 records are troubleshooting (symptom-first), and 26% are tagged `confused`.

IFC for an architect is like exporting a Word document to PDF so someone else can read it. The difference: here the other party also wants to *work with* the PDF, and that expectation is where the pain starts.

## Daily IFC tasks

| # | Task | What it looks like in practice | Evidence in the base |
|---|---|---|---|
| 1 | Export IFC for engineers, cost, contractor | Pick IFC version/view (2x3 CV2.0 or IFC4 RV), a translator (Archicad), the right levels, and hope the result opens. | `export_revit` 63, `versions_mvd`; synthetic `it-italy-s011` "per la gara cosa esporto, 2x3 CV2.0 o IFC4 RV?" |
| 2 | Open or link consultants' IFC for reference | Link IFC into Revit; the walls arrive as generic models; windows may sit outside the wall. | `import_into_revit` 44; [en-autodesk-revit-import-r022](https://github.com/Autodesk/revit-ifc/issues/1019) |
| 3 | Make rooms show up with the right areas | Rooms/zones/areas must become IfcSpace with name, number and area (for the area schedule, ТЭП, экспликация, Raumliste). | `spaces_rooms_areas` 33 |
| 4 | Get classes right | Foundation walls as footings, wall sweeps as coverings, curtain wall as one object, boiler vs heat pump as different classes. | `class_mapping` 45 |
| 5 | Carry materials, layers, colours | Layered walls, surface colours; "everything is grey" after import. | `materials_colors_styles` 29 |
| 6 | Keep openings working | Door/window holes in walls, shafts through floors, roof windows. | `openings_voids` 26 |
| 7 | Produce drawings from IFC (Bonsai users) | Plans, sections, annotation, hatches, drawing sheets from an IFC-native model. | `layers_presentation` 23; [en-osarch-r002](https://community.osarch.org/discussion/3783/claude-bonsai-construction-drawings) |
| 8 | Convert for other programs | IFC to DWG/DXF, SketchUp, OBJ, QGIS. | `conversion_formats`; [it-italy-r022](https://biblus.acca.it/come-convertire-un-file-dwg-in-ifc-in-modo-semplice/) |
| 9 | Submit to an authority | CORENET X (Singapore), SZ-IFC (Shenzhen), state expertise (Russia); fix what the checker rejects. | [en-sg-corenetx-r003](https://github.com/noddlesskcho/IFC-Repair-Studio), [ru-dwg-other-r017](https://forum.dwg.ru/showthread.php?t=153428) |
| 10 | Let an AI act in the authoring tool | Ask an LLM to create walls, dimension a view, renumber sheets, count doors. | Block E below |

## Goals

- **Export once and have the other side get what they need**, with the right classes and properties, without a lecture about mapping tables.
- **Keep the model editable** after an IFC round trip (or at least know honestly that it will not be).
- **Rooms and areas that match the area schedule** exactly (the Japanese and Dutch records in this list are about area and height rules for rooms).
- **Colours, layers and materials preserved** for presentation and for energy analysis.
- **Fewer chores**: sheets per level, numbered views, tags, renamed views done by script or AI (for example [en-revit-auto-r008, a Dynamo thread on placing viewports on sheets](https://forum.dynamobim.com/t/how-to-add-viewport-in-sheets-by-dynamo/114310)).
- **A free alternative to expensive licences** for the few who try Bonsai ([ja-japan-r023](https://note.com/akram/n/n8a6e9c5602ca) weighs a free tool against 420,000 to 1,380,000 yen per year for commercial BIM).

## Pains (ranked)

_Quoted phrases in the last column are illustrative: some paraphrase real records, others are taken from the synthetic prompts further down. Only the tables of real records are evidence of what people actually wrote._

| Rank | Pain | Signal | Typical shape |
|---|---|---|---|
| 1 | **Export drops or mislabels things** | `export_revit` 63, `class_mapping` 45 | "wall sweeps arrive as proxy", "half the model is gone", "elements on the wrong IFC level", "rooms in the wrong storey" |
| 2 | **Import gives dead geometry or shifted objects** | `import_into_revit` 44, `geometry_quality` 32 | "my IFC walls are just generic models", "windows are outside the wall in Revit 2025-27, fine in 2024", "doors invisible in plan view" |
| 3 | **Rooms/areas don't match** | `spaces_rooms_areas` 33 | "area in IFC differs from my schedule", "rooms don't show up at all" |
| 4 | **Colours, materials and layers vanish** | `materials_colors_styles` 29 | "all grey in the viewer", "layered wall has one material" |
| 5 | **Openings don't cut** | `openings_voids` 26 | "windows float in front of the wall", "opening cuts skipped" |
| 6 | **2D drawings and annotation from IFC** | `layers_presentation` 23 | "no annotation context", "hatch by material", "dimension digits" |
| 7 | **Connecting an AI to the authoring tool** | `ai_llm_mcp` | "unable to connect to Revit", "door ends up unhosted at origin" |
| 8 | **Not knowing what an authority wants** | `permitting_code_checking`, `national_requirements` | "must I work in 3D now or can I submit PDF?" |

## Vocabulary they use (and what they do not know)

### Words and phrases you will see

| Phrase (language) | Plain meaning |
|---|---|
| "generic models", "dumb solids", "Imported Symbol", "обобщённые модели", "тела", "dumb objects" | What Revit/Archicad make of an IFC element when they cannot map its class: shape only, no behaviour, no parameters. |
| "half my walls are proxy", "stuff isn't under any level" | Elements exported as the catch-all class, or not attached to a floor. |
| link vs open, "Open IFC" / "Link IFC" | Two ways to bring IFC into Revit with very different results ([en-autodesk-revit-import-r003](https://github.com/Autodesk/revit-ifc/issues/223)). |
| translator, "Übersetzer", "транслятор" (Archicad) | Archicad's export preset; the choice decides what the receiver gets. |
| shared parameters, "общие параметры", "Projektparameter" | Custom fields in Revit; they do not reach IFC unless mapped. |
| room vs space, "Zone" vs "IfcSpace", Area plan | Revit rooms, areas and zones are not automatically IFC spaces. |
| ТЭП, экспликация помещений, Raumliste, NGF/BGF, SDP/surface utile, BTA/NTA, 面積表 | Area schedules; each country's wording. |
| sweeps, fascia, mullions, "ghost mullions", curtain wall panels | Elements that Revit exports in surprising ways. |
| 壁芯 (wall centre line), 間引き違い戸 | Japanese drafting conventions that open-source tools handle poorly ([ja-japan-r023](https://note.com/akram/n/n8a6e9c5602ca)). |

### What they typically do not know, or get wrong

- **That IFC is meant for sharing, not for exchange of editable models.** Japanese and Russian write-ups repeat it: parametric relations are lost, the receiver gets "geometry" ([ja-japan-r021](https://note.com/onestruction/n/ne8322e3be44d), [ru-autodesk-telegram-r020](https://sapr.ru/article/24777)).
- **That a shape drawn with the wrong tool is not a building element.** A 3D box or a solid, a layer not tied to a floor, or hidden elements will not come out as walls ([ja-japan-r015](https://note.com/toshio_nakamura/n/nc8db42ce3191)).
- **IFC class names and the schema**; they describe what they see ("a glass partition with a door"), not `IfcCurtainWall` vs `IfcWall` ([en-bsforum-r043](https://forums.buildingsmart.org/t/6609)).
- **That "Name", "Reference", "Description" and "Type" mean different things in IFC** and different tools fill them differently ([en-bsforum-r041 about Allplan](https://forums.buildingsmart.org/t/6429)).
- **That the exporter version matters**; they name their Revit year, rarely the exporter build.

Read next: [IFC in real projects](../../01_ifc_basics/00_ifc_in_real_projects.md), [entities cheat sheet](../../01_ifc_basics/03_entities_cheat_sheet.md), [spatial structure](../../01_ifc_basics/04_spatial_structure_and_relationships.md), [materials, classification, types](../../01_ifc_basics/07_materials_classification_types_styles.md), [Revit IFC export](../../03_software/revit/ifc_export_reference.md), [Revit IFC import/link](../../03_software/revit/ifc_import_link_reference.md), [authoring tools](../../03_software/authoring_tools_ifc.md), topic pages [import and interoperability](../by_topic/import_and_interoperability.md), [geometry, openings, curtain walls, stairs](../by_topic/geometry_openings_curtainwalls_stairs.md), [materials, spaces, zones](../by_topic/materials_spaces_zones.md), [programming and automation](../by_topic/programming_and_automation.md).

## Real questions (60, linked)

Paraphrases of questions or issues seen at the linked sources, kept in the asker's language. Language mix in this list: Russian 11, English 34, other languages 15. Where a source page is not in English but the stored paraphrase is, the Lang column still shows the page language.

### A. Sending IFC out: things go missing, change class or land on the wrong floor

The architect exports, the engineer complains. Symptoms are described visually ("half the model is gone", "wrong floor") rather than in IFC terms.

| # | Lang | Their words (paraphrase, original language) | English gloss / context | Source (record id, type, year) |
|---|---|---|---|---|
| 1 | ja | IFCに書き出したらモデルの半分が消えていた。ただのソリッド、階に紐づかないレイヤ、非表示要素が原因 | After IFC export about half the elements were missing | [ja-japan-r015](https://note.com/toshio_nakamura/n/nc8db42ce3191) blog, 2026 |
| 2 | en | Wall sweeps should come out as IfcCovering but arrive as IfcBuildingElementProxy; changing IFC Export Class and a global IfcExportAs parameter did not help. |  | [en-autodesk-revit-export-r002](https://forums.autodesk.com/t5/revit-architecture-forum/the-ifc-class-is-not-exported-correctly-to-the-ifc-model/td-p/11629864) forum, 2022 |
| 3 | en | Elevation is off in IFC even though the IfcSite elevation option is checked. |  | [en-autodesk-revit-export-r013](https://forums.autodesk.com/t5/revit-mep-forum/ifc-exports-at-wrong-elevation-even-when-ifcsite-is-ticked/td-p/11214407) forum, 2022 |
| 4 | en | Curtain wall panels are hidden deep in IFC hierarchy. |  | [en-autodesk-revit-export-r021](https://forums.autodesk.com/t5/revit-architecture-forum/advanced-ifc-export-of-curtain-wall-revit-2018/td-p/8590346) forum, 2019 |
| 5 | en | How to get the whole curtain wall as one IFC object. |  | [en-autodesk-revit-export-r022](https://forums.autodesk.com/t5/revit-architecture-forum/export-curtain-wall-to-ifc-as-a-single-object/td-p/12907563) forum, 2024 |
| 6 | en | Mullions show up in the IFC that are not in the Revit model. |  | [en-autodesk-revit-export-r023](https://forums.autodesk.com/t5/revit-architecture-forum/quot-ghost-quot-mullions-in-ifc-export/td-p/13056918) forum, 2024 |
| 7 | en | Elements land in the wrong IfcBuildingStorey. |  | [en-autodesk-revit-export-r026](https://forums.autodesk.com/t5/revit-architecture-forum/elements-are-being-exported-to-the-wrong-ifc-level/td-p/11927737) forum, 2023 |
| 8 | en | Rooms placed in wrong storey in IFC. |  | [en-autodesk-revit-export-r043](https://forums.autodesk.com/t5/revit-architecture-forum/revit-ifc-export-results-in-wrong-position-of-rooms/td-p/12156364) forum, 2023 |
| 9 | de | meine Fundamentwaende aus dem Wandwerkzeug werden IfcWall statt IfcFooting | Foundations modelled with Revit wall tool export as IfcWall; how to get IfcFooting? | [en-blogs-linkedin-r006](https://bim-me-up.com/wand-als-ifcfooting-exportieren/) blog, 2020 |
| 10 | de | IsExternal not filled for columns; since Revit 2023 type parameters no longer export to Pset_Common | Revit columns have no Function so Pset_ColumnCommon.IsExternal is empty; map a custom Yes/No parameter. | [en-blogs-linkedin-r018](https://bim-me-up.com/ifc-tipp-revit-stutze-den-isexternal-standardparameter-zuweisen/) blog, 2019 |
| 11 | en | contractor needs IFC for cost estimation but we have no BEP or template | ArchiCAD IFC pain points: stairs drawn as beams, wrong home storey, overlaps break quantities, no BEP. | [en-blogs-linkedin-r030](https://bimcorner.com/exporting-ifc-from-archicad/) blog, 2021 |
| 12 | ru | ревит надо настроить заранее: оси в IFCGrid, IFCExportAs в ФОП, разбивка стен по уровням | How to export plans from Revit via IFC to nanoCAD SPDS: map grids to IfcGrid, IfcExportAs in shared params, split walls by levels | [ru-autodesk-telegram-r019](https://sapr.ru/article/25825) blog, 2019 |
| 13 | ru | чем проверить корректность IFC, атрибуты могут не дойти | How to validate IFC from Archicad; attributes may not survive in AutoCAD. | [ru-dwg-other-r030](https://forum.dwg.ru/showthread.php?t=34919&page=3) forum, 2012 |
| 14 | es | problemas con los ifc: al abrirlo y guardarlo en otro formato se pierden las coordenadas que traia | Problems with IFC files: opening and re-saving an IFC in another format loses the coordinates it carried. | [es-spain-r001](https://forums.autodesk.com/t5/revit-architecture-forum/problemas-con-ifc-s/td-p/10189111) forum, 2021 |

### B. Getting someone else's IFC into Revit or Archicad

The most common disappointment: the file opens, but the walls are "generic models" or "dumb solids" and cannot be edited.

| # | Lang | Their words (paraphrase, original language) | English gloss / context | Source (record id, type, year) |
|---|---|---|---|---|
| 15 | en | Is there a way to get Revit to recognize walls when importing IFC? Currently all generic models. | IFC walls become generic models after import into Revit; how to make Revit recognize walls? | [en-us-canada-infra-r015](https://github.com/Autodesk/revit-ifc/issues/571) github_issue, 2022 |
| 16 | ru | при импорте IFC архитектурных моделей из других программ элементы приходят как тела, а не как родные объекты Ревита, хочу их редактировать | Imported IFC elements come in as dumb solids instead of editable Revit objects; which import settings? | [ru-dwg-other-r009](https://forum.dwg.ru/showthread.php?t=166052) forum, 2022 |
| 17 | ru | можно ли редактировать семейство из IFC в Ревите | Can an imported IFC be edited as a Revit family? | [ru-dwg-other-r023](https://forum.dwg.ru/showthread.php?t=130296&page=2) forum, 2016 |
| 18 | ru | при экспорте из Архикада в IFC и вставке в Ревит стёкла жёлтые и толщиной в метры, часть перегородок пропала | ArchiCAD IFC in Revit: glass yellow and meters thick, part of partitions/trusses missing; fix? | [ru-dwg-other-r029](https://forum.dwg.ru/showthread.php?t=154396) forum, 2019 |
| 19 | ru | часть свойств потерялась после импорта IFC, какие настройки экспорта выбрать, почему файл не читается | Why are properties missing after IFC import and which export settings to use from Renga (Reference View vs editable geometry)? | [ru-autodesk-telegram-r017](https://blog.rengabim.com/2021/08/ifc.html) blog, 2021 |
| 20 | en | Doors appear in 3D but are invisible in floor plan; the Model footprint representation is not displayed and visibility overrides do not help. | Archicad IFC4 doors are invisible in Revit plan views; the 2D swing only shows on hover. | [en-autodesk-revit-import-r010](https://github.com/Autodesk/revit-ifc/issues/358) github_issue, 2021 |
| 21 | en | Windows are positioned outside wall faces regardless of the 2D annotation setting; absent in Revit 2024. | Imported windows sit outside the wall face in Revit 2025-2027 but not in 2024. | [en-autodesk-revit-import-r022](https://github.com/Autodesk/revit-ifc/issues/1019) github_issue, 2026 |
| 22 | en | Plain walls import well, but a wall with a window gets family Imported Symbol and cannot be modified. | A round-tripped wall with a window reimports as Imported Symbol, not an editable Basic Wall. | [en-autodesk-revit-import-r023](https://github.com/Autodesk/revit-ifc/issues/729) github_issue, 2024 |
| 23 | en | Windows from an Archicad IFC are offset out of walls in Revit 2025-27. | IFC import: windows sit outside the wall face in 3D (not in Revit 2024). | [de-dach-r017](https://github.com/Autodesk/revit-ifc/issues/1019) github_issue, 2026 |
| 24 | it | come carico il file di mappatura classi IFC in Revit prima di aprire l'IFC cosi le porte restano porte? | How to load an IFC class mapping file in Revit/Archicad so IFC entities are recognized on import. | [it-italy-r003](https://biblus.acca.it/ifc-class-mapping-file/) vendor_kb, 2023 |
| 25 | ru | IFC из ifcopenshell в Revit не становится семейством | IFC created via ifcopenshell opens in Revit as a wall but not a native family | [ru-habr-dev-r027](https://github.com/Autodesk/revit-ifc/issues/777) github_issue, 2022 |

### C. Rooms, openings, materials, curtain walls

Spaces/areas for the area schedule, holes in walls for doors and windows, layers and colours.

| # | Lang | Their words (paraphrase, original language) | English gloss / context | Source (record id, type, year) |
|---|---|---|---|---|
| 26 | en | searching IFC text in Notepad++ for a room by room number; how to find the building storey it belongs to? |  | [en-bsforum-r018](https://forums.buildingsmart.org/t/5187) forum, 2024 |
| 27 | nl | Ruimte: toegankelijk, minimaal 1,5 m netto hoogte; Name (toilet) en ObjectType (toiletruimte); zones voor woning, brandcompartiment | IfcSpace needs min 1.5 m net height; Name plus ObjectType (Bouwbesluit function); IfcZone for dwelling type etc. | [nl-dutch-r021](https://www.digigo.nu/ilsen-en-richtlijnen/bim-basis-ils/4-1-ruimten) official_doc, 2024 |
| 28 | nl | Naamgeving bouwlagen gelijk in alle aspectmodellen; hulpbouwlagen alleen in bronbestanden; tussenverdieping met letter (00a) | One IfcBuildingStorey per floor, numeric-sortable names like '-1 kelder', '00 begane grond'; foundations not a separate storey | [nl-dutch-r018](https://www.digigo.nu/ilsen-en-richtlijnen/bim-basis-ils/3-3-bouwlaagindeling-en-naamgeving) official_doc, 2024 |
| 29 | ja | 部屋名・用途・床面積がIFCに出て別ビューアで読めるか。面積が合わない時は境界・計算方法・単位・版を確認 | Prepare for 2029 data review by exporting one room to IFC and re-reading it in another viewer | [ja-japan-r019](https://note.com/t_note_memo/n/n8903305b00fb) blog, 2026 |
| 30 | en | wanted two separate spaces, selecting walls gave one; Calculate All Quantities gave 0 ceiling area; later asks if IfcSpace includes finishes and void | Make two IfcSpaces in an apartment; ceiling areas 0; does IfcSpace span slab to slab? | [en-spaces-r035](https://community.osarch.org/discussion/comment/30080) forum, 2025 |
| 31 | en | How do I make an IfcSpace bounded by walls whose volume updates when walls change? The Space Boundaries list is empty. Later: how do I split one open room into two spaces? |  | [p-student-r009](https://community.osarch.org/discussion/635/ifcspace-and-blenderbim) forum, 2021 |
| 32 | en | wants auto room in closed wall loop; QTO says 34 records calculated but nothing in quantity sets | Room system too complicated; 34 records calculated but net floor area not shown anywhere | [en-gh-ifcopenshell-r025](https://github.com/IfcOpenShell/IfcOpenShell/discussions/9407) github_issue, 2026 |
| 33 | en | New user asks if multi-layer walls (concrete, insulation, concrete) are possible; Revit IFC vs Blender round-trip shows missing wall materials in Solibri. |  | [en-osarch-r029](https://community.osarch.org/discussion/261/layered-walls-in-blenderbim) forum, 2020 |
| 34 | en | only one material is output as material layer for a structural framing family mapped to IfcWall | Export a custom sandwich wall family with several materials as separate layers | [en-mcl-r006](https://github.com/Autodesk/revit-ifc/issues/929) github_issue, 2025 |
| 35 | en | numbered list of 4 problems: overlapping site meshes, overlapping wall faces, flipped faces on floors/parapets, and no idea how to store bitmaps in a shading style | IFC4 from Revit shows overlapping site meshes, wrong face orientation, and user cannot save bitmaps to a shading style in Bonsai | [en-gh-ifcopenshell-r001](https://github.com/IfcOpenShell/IfcOpenShell/issues/6283) github_issue, 2025 |
| 36 | en | Wall tagged EXISTING, opening tagged NEW (also tried DEMOLISH) but void is always applied to the wall in both plans. | Cannot make a NEW opening in an EXISTING wall; status filters do not hide the new void in existing-state drawings. | [en-openings-r003](https://github.com/IfcOpenShell/IfcOpenShell/issues/7472) github_issue, 2025 |
| 37 | en | Can no longer make arbitrary opening shapes; edits lost in IFC Edit mode and Blender crashes outside it. Argues software should warn about IFC limits. |  | [en-osarch-r025](https://community.osarch.org/discussion/3685/bonsai-0-9-blender-5-2-2-new-void-system-improved-until-ist-was-broken) forum, 2026 |
| 38 | en | Revit 2025 IFC reads fine in SketchUp but wall openings are partly ignored when imported in Blender 4.3 with Bonsai. |  | [en-osarch-r036](https://github.com/IfcOpenShell/IfcOpenShell/issues/6120) github_issue, 2025 |
| 39 | en | glass partition with door panel: IfcCurtainWall or IfcWall? |  | [en-bsforum-r043](https://forums.buildingsmart.org/t/6609) forum, 2026 |

### D. Drawings, conversions and tool choice (including free tools)

Architects who try Bonsai/Blender or must leave a paid tool, and everyone who needs DWG, DXF, SketchUp or OBJ out of an IFC.

| # | Lang | Their words (paraphrase, original language) | English gloss / context | Source (record id, type, year) |
|---|---|---|---|---|
| 40 | en | Revit veteran testing an AI assistant on Blender/Bonsai construction drawings; wants it to read redlines and update model and sheets, and asks how others balance 3D versus 2D detailing (sections, tags, callouts, lineweights, styles). |  | [en-osarch-r002](https://community.osarch.org/discussion/3783/claude-bonsai-construction-drawings) forum, 2026 |
| 41 | en | Furniture elements with plan annotation representations show a trace outline and a mesh overlaid in plan drawings; what is wrong? |  | [en-osarch-r013](https://community.osarch.org/discussion/3698/a-drawing-problem) forum, 2026 |
| 42 | ja | 年42万〜138万円の商用BIMに対し無料で。壁が芯でなく面基準、ハッチング、1間引き違い戸が作れない | Is open-source Bonsai usable for Japanese practice? Walls on face not 壁芯, hatches, sliding-door presets | [ja-japan-r023](https://note.com/akram/n/n8a6e9c5602ca) blog, 2026 |
| 43 | en | After cancelling Revit, user wants a paid helper or workaround to keep converting Revit files to IFC. |  | [en-osarch-r018](https://community.osarch.org/discussion/3043/canceled-revit-subscription-need-help-with-future-file-translations-to-ifc) forum, 2025 |
| 44 | ru | как перевести ifc в dwg и какими программами, работаю в Архикаде | How to convert IFC to DWG and with which programs? | [ru-dwg-other-r016](https://forum.dwg.ru/showthread.php?t=96356) forum, 2013 |
| 45 | ru | стоит ли переходить на Renga вместо Ревита, как у неё с обменом через IFC | Is Renga usable for design instead of Revit/ArchiCAD, including IFC exchange? | [ru-dwg-other-r006](https://forum.dwg.ru/showthread.php?t=149046) forum, 2018 |
| 46 | it | ho solo il DWG, come lo converto in IFC? | How to convert a DWG to IFC simply. | [it-italy-r022](https://biblus.acca.it/come-convertire-un-file-dwg-in-ifc-in-modo-semplice/) vendor_kb, 2023 |
| 47 | it | dall'IFC come estraggo piante e sezioni in DXF? | How to get 2D plans, sections, elevations in DXF from an IFC. | [it-italy-r023](https://biblus.acca.it/una-guida-completa-per-convertire-file-ifc-in-dxf/) vendor_kb, 2026 |

### E. "Can the AI just do it in my Revit / Archicad?"

Real users and tool authors testing LLM connections to Revit, Archicad and Bonsai. These are the closest thing in the base to the MCP test setup itself.

| # | Lang | Their words (paraphrase, original language) | English gloss / context | Source (record id, type, year) |
|---|---|---|---|---|
| 48 | en | Claude replies: unable to connect to Revit... will create a 10-meter wall once connected; port 8080 opened, no luck | Followed all steps, tried several Revit MCPs, Claude always says it cannot connect to Revit when asked to create a 10 m wall. | [en-aimcp-r003](https://github.com/mcp-servers-for-revit/mcp-servers-for-revit/issues/1) github_issue, 2026 |
| 49 | en | wall (0,2000)-(5000,2000); door at 2500,2000,0; FamilyInstance.Host is null | Placing a door with create_point_based_element ignores x/y/z and host; the door ends up unhosted at the origin. | [en-aimcp-r007](https://github.com/bimwright/rvt-mcp/issues/13) github_issue, 2026 |
| 50 | en | put the sofa here, by the window; verify a change actually looks correct | Wants a tool returning the current Revit view as an image so a multimodal LLM can place elements visually and verify changes. | [en-aimcp-r017](https://github.com/LuDattilo/revit-mcp-server/issues/16) github_issue, 2026 |
| 51 | en | How many fire doors are on Level 2? | Architects drag an IFC into Claude and ask: how many fire doors on Level 2, validate materials, concrete quantities, what changed since last week, convert to GLB. | [en-aimcp-r028](https://github.com/Daviidro/ifcopenshell-mcp) official_doc, 2026 |
| 52 | es | Creá cuatro muros de 3 m de alto formando un rectángulo de 5 × 4 m | Spanish prompts: what elements do I have selected in Archicad; create four 3 m walls forming a 5x4 m rectangle. | [es-aimcp-r031](https://github.com/joacos/archicad-mcp) official_doc, 2026 |
| 53 | ja | AIに『3〜10階に同じ部屋割りを作って』『窓幅を一括変更』『20m2未満の部屋を赤に』と頼めるか | Explainer for architects: using Revit-MCP so AI can create/modify Revit elements in natural language | [ja-japan-r004](https://zenn.dev/yuichi_ai/articles/879de49ee8e1bb) blog, 2025 |
| 54 | zh | 目前預覽只回傳數量,沒有座標,AI想把CAD牆圖層翻成Revit牆時拿不到每段位置,無法逐道create_wall,也無法在建模前檢查辨識結果 | Make the beam preview tool return centerline coordinates so CAD wall layers can be converted to Revit walls | [zh-revit-auto-r027](https://github.com/shuotao/REVIT_MCP_study/issues/150) github_issue, 2026 |
| 55 | ru | перенести модель из Archicad в Revit через IFC и управлять Revit из ИИ-клиента | Plugin combining MCP bridge, Archicad-to-Revit transfer via IFC/Tapir and HVAC calcs | [ru-habr-dev-r026](https://github.com/Davud77/bp-revit-tools) github_issue, 2026 |
| 56 | vi | Thống kê cửa, phòng; khối lượng tường, sàn | Vietnamese toolkit: Claude builds levels, walls, rooms from description or AutoCAD drawing; second part counts doors, rooms, quantities, exports Excel. | [vi-aimcp-r042](https://github.com/andyluu98/vn-revit-mcp) official_doc, 2026 |
| 57 | en | we type unit areas by hand into view titles and a unit-type schedule on the general sheet; could Dynamo take each unit's area from the area plan; we are new to Dynamo | Pull each unit's area from its area plan and fill unit sheet view titles and a unit-type schedule automatically | [en-revit-auto-r004](https://forum.dynamobim.com/t/extract-areas-from-area-plans/115283) forum, 2026 |

### F. Authority submissions



| # | Lang | Their words (paraphrase, original language) | English gloss / context | Source (record id, type, year) |
|---|---|---|---|---|
| 58 | ru | нужно ли с 01.07.2019 переходить на ТИМ, можно ли работать в 2D и сдавать PDF | Since 01.07.2019 BIM is required?; can we keep 2D and PDF? Is IFC the format? | [ru-dwg-other-r017](https://forum.dwg.ru/showthread.php?t=153428) forum, 2019 |
| 59 | en | got IFC0000101 update file to supported IFC version, I exported ifc2x3, how to export ifc4 with IFC+SG settings | Error IFC0000101 'Update file to a supported IFC version' because I exported IFC2x3. | [en-sg-corenetx-r003](https://github.com/noddlesskcho/IFC-Repair-Studio) blog, 2026 |
| 60 | en | site coverage and site boundary came out as IfcSpace, IFC+SG wants IfcGeographicElement, relationships too | Site coverage, site boundary and planting areas modelled as IfcSpace; need IfcBuildingElementProxy / IfcGeographicElement. | [en-sg-corenetx-r009](https://github.com/noddlesskcho/ifc-sg-site-object-repair) blog, 2026 |

## Ready test prompts (46, synthetic)

**All prompts below are SYNTHETIC.** Several are how-to questions with no file ("no file"); the assistant should answer from knowledge, not pretend to inspect a model.

### 1. Why is half of it a proxy? Reclassify

The classic architect complaint; the second half of each prompt is often "and fix it".

| # / id | Lang | Prompt (SYNTHETIC) | Meaning (EN) | Difficulty | A good answer should |
|---|---|---|---|---|---|
| S1 `en-allplan-vw-bentley-s001` | en | allplan IFC export - half my walls came out as proxy?? can u list what ifc class each wall got | Allplan walls exported as proxies; which IFC classes did each Allplan element get? | medium, file | List IfcWall vs IfcBuildingElementProxy counts, name affected elements, suggest Allplan attribute/IFC-type fixes. |
| S2 `en-graphisoft-s002` | en | half my walls are showing as proxy, why?? find them | Walls exported as IfcBuildingElementProxy | medium, file | List IfcBuildingElementProxy, group by name/type/layer, explain likely IFC Manager mapping causes and propose reclassification. |
| S3 `ru-renga-nanocad-s002` | ru | сколько в модели проксей и что это за элементы, из ренги выгружали | How many elements fell into IfcBuildingElementProxy and what they are | medium, file | Count IfcBuildingElementProxy, group by Name/ObjectType, report likely original Renga object types and suggest correct IFC classes. |
| S4 `en-blogs-linkedin-s007` | en | walls named Fundament should be IfcFooting not IfcWall can you fix that | Reclassify wall to footing | medium, file | Find IfcWall by name, change to IfcFooting with appropriate predefined type, warn on schema constraints. |
| S5 `es-proxy-s005` | es | los zócalos y vierteaguas salen como proxy, cámbialos a IfcMember o IfcCovering segun el caso y dime cuales tocaste | Change sweep elements from proxy to IfcMember | medium, file | Identify proxies from wall sweeps/fascias by name, reclassify per rule, list changes. |
| S6 `zh-revit-export-s008` | zh | 把所有名字带'柱'的代理构件改成IfcColumn，别的不要动 | Reclassify generic items as columns | hard, file | Find IfcBuildingElementProxy with name containing 柱, change class to IfcColumn, preview list before writing, save a copy. |
| S7 `ru-autodesk-telegram-s009` | ru | перебей класс у всех IfcBuildingElementProxy с именем 'Ограждение*' на IfcRailing и сохрани новую версию | Change class of selected elements and save | medium, file | Select proxies by name pattern, change entity class to IfcRailing preserving properties and GlobalId, write new file and report count. |
| S8 `pt-brazil-s014` | pt-BR | como faço uma família generic model sair como IfcWall no ifc? coloquei IfcExportAs mas não pegou | Export custom family as IfcColumn/IfcWall | medium, no file | Explain IfcExportAs parameter on family type, or mapping table, and re-check. |

### 2. Where did my parameters, materials and colours go?



| # / id | Lang | Prompt (SYNTHETIC) | Meaning (EN) | Difficulty | A good answer should |
|---|---|---|---|---|---|
| S9 `de-dach-s005` | de | meine eigenen Parameter kommen in der IFC nicht an obwohl Häkchen bei benutzerdefinierte Psets gesetzt ist, woran liegts | Why do my shared parameters not appear in the IFC. | medium, no file | Explain mapping txt file format, name clashes with built-ins, type vs instance parameters, how to verify. |
| S10 `it-italy-s010` | it | da Revit esporto IFC ma i miei parametri condivisi non ci sono nei Pset, perche? | Custom parameters missing from IFC export | medium, no file | Explain user-defined property set file / export options 'export schedules as Psets'; shared parameter requirements. |
| S11 `ru-dwg-revit-s002` | ru | выгрузил в ифс, а мои общие параметры (Марка_ЕСКД, Огнестойкость) куда-то пропали. проверь есть ли они хоть в каких-то псетах у стен | Check whether my shared parameters survived into property sets | medium, file | Search all Psets of IfcWall for those property names, report presence/absence and which Pset, explain export settings for user-defined Psets. |
| S12 `ru-dwg-revit-s011` | ru | найди элементы без материала, а у стен покажи слои и толщины | Which elements have no material | medium, file | Find elements without material association; for walls list IfcMaterialLayerSet layers with thickness. |
| S13 `mx-mcl-s015` | de | wie krieg ich die Farben von Archicad IFC in Revit rueber? Oberflaechen sind alle grau | How to keep colours between Archicad and Revit | medium, no file | Explain Revit import ignores styles, use link vs open, materials mapping; check file for styles first. |
| S14 `mx-mcl-s004` | es | importe el IFC de Archicad en Revit y se perdieron los colores, revisa si los estilos de superficie estan en el archivo | Why are the colours lost | medium, file | Check IfcStyledItem/IfcSurfaceStyle presence on shapes and materials; report whether data exists in the file so loss is an import-side issue. |
| S15 `zh-revit-export-s016` | zh | 导出ifc后颜色全灰了，材质怎么保留 | Colors lost in IFC after export | medium, no file | Explain surface style export, material color vs render appearance, viewer differences; options to check. |
| S16 `en-osarch-s016` | en | what material layers does the exterior wall type have? thickness of each |  | easy, file | Read IfcMaterialLayerSet for the type, list layers and thickness; note Revit export caveats. |

### 3. Rooms, areas, levels



| # / id | Lang | Prompt (SYNTHETIC) | Meaning (EN) | Difficulty | A good answer should |
|---|---|---|---|---|---|
| S17 `en-autodesk-revit-export-s003` | en | do we have IfcSpace for every room? rooms vs spaces count by level |  | medium, file | Count IfcSpace per storey, compare with a given room list, report missing, check Name/LongName. |
| S18 `en-reddit-s003` | en | give me a table of all IfcSpace with name, number, level and net floor area | List room areas by level | easy, file | Query IfcSpace, read Qto_SpaceBaseQuantities/Pset area values, group by storey, output table. |
| S19 `ja-japan-s010` | ja | IFCの面積がRevitの集計表と合わない。単位か境界の問題？部屋ごとに差を出して | Room area in IFC differs from the Revit schedule; check units and boundary | medium, file | Report project length unit and area unit, compare Qto NetFloorArea vs GrossFloorArea per space, list rooms with differences. |
| S20 `ru-permit-s007` | ru | выведи таблицей все помещения: номер, назначение, площадь, этаж. для экспликации | List rooms with area and purpose for explanatory note | easy, file | Extract IfcSpace data into a table, flag missing fields. |
| S21 `fr-francophone-s003` | fr | donne moi la surface par niveau des pièces (IfcSpace), SDP et surface utile si dispo | Sum the area of all spaces per storey | easy, file | Sum NetFloorArea/GrossFloorArea from Qto_SpaceBaseQuantities per IfcBuildingStorey; report which spaces lack values. |
| S22 `no-norway-s004` | no | etasjene blir dobbelt i IFC etter eksport fra Revit, noen ide? sjekk modellen | Storeys appear duplicated after IFC export | medium, file | List IfcBuildingStorey entries with elevations, detect duplicates/mismatched names, explain level export settings. |
| S23 `pt-brazil-s004` | pt-BR | lista os pavimentos do ifc com a cota e vê se os nomes batem com o padrão do BEP (Térreo, 1º Pav, etc) | List storeys with elevations and check that names match the project standard | easy, file | List IfcBuildingStorey names and elevations, flag deviations from naming pattern. |
| S24 `ko-korea-s004` | ko | 층 목록이랑 레벨 높이 뽑아줘 (mm 단위로) | List storeys with elevations | easy, file | List IfcBuildingStorey names and elevations converted to mm. |

### 4. Import into Revit or Archicad is broken

Many of these are how-to questions with no file loaded; the assistant must explain, not query.

| # / id | Lang | Prompt (SYNTHETIC) | Meaning (EN) | Difficulty | A good answer should |
|---|---|---|---|---|---|
| S25 `en-autodesk-revit-import-s004` | en | how many things in this ifc are proxies? want to fix import mapping so they dont end up generic models | Count proxies and unmapped classes | medium, file | Count entities per class, list proxies by ObjectType, propose import class mapping entries. |
| S26 `en-autodesk-revit-import-s010` | en | doors from archicad ifc invisible in plan in revit. do they even have a footprint rep? | Check Archicad door plan symbols | medium, file | Inspect IfcDoor representations for Plan/FootPrint contexts and report presence. |
| S27 `en-autodesk-revit-import-s013` | en | whats the diff open ifc vs link ifc in revit, which gives editable walls? | Open vs Link IFC | easy, no file | Explain Open (native elements/in-place, separate code path) vs Link (reference with .ifc.rvt cache, positioning options in 2026). |
| S28 `es-latam-s004` | es | importé el ifc de archicad en revit 2025 y las ventanas quedaron fuera del muro, en el 2024 andaba bien, qué onda | Doors and windows land outside the wall after importing Archicad IFC into Revit | medium, no file | Explain the known regression, suggest checking hosted-element relations and import options, and offer to verify openings in the IFC. |
| S29 `ru-roundtrip-s007` | ru | как из архикада ифс в ревит затащить чтоб были стены а не обобщенные модели? open или link? | Open or link IFC in Revit to get native walls? | medium, no file | Explain Open vs Link IFC, import class mapping, DirectShapes, and preparation in the Archicad translator. |
| S30 `ru-renga-nanocad-s007` | ru | ифс из ренги в ревит заходит какими-то глупыми телами, параметров нет, что не так | Renga IFC imports into Revit as dumb generic elements without parameters | medium, no file | Explain Revit link vs open/import of IFC, IFC class mapping, and that Pset properties arrive as parameters only on proper link/open; suggest checking the IFC version and export settings. |
| S31 `zh-revit-export-s014` | zh | ifc链进来的墙改不了啊，怎么变成revit自己的墙？ | Linked IFC can't be edited, how to turn into native elements | medium, no file | Explain linked/opened IFC objects are not native editable; options: open IFC to convert, rebuild, or edit in source; explain limits. |
| S32 `it-vm-s014` | it | ho esportato in ifc4 da archicad ma revit non lo apre, solo collegato. perche? | Why does this IFC4 not open in Revit | medium, file | Check schema, tessellated/polygonal face sets, explain Open vs Link limits, suggest IFC2x3 or faceted brep. |

### 5. Openings, curtain walls, stairs



| # / id | Lang | Prompt (SYNTHETIC) | Meaning (EN) | Difficulty | A good answer should |
|---|---|---|---|---|---|
| S33 `en-gh-thatopen-s009` | en | some walls dont show windows, check which walls have openings in the IFC but no voids processed | Compare walls with IfcRelVoidsElement openings to walls that look solid | medium, file | List walls with IfcRelVoidsElement and fillings, flag IfcOpeningElement without matching rep or placement. |
| S34 `pt-brazil-s009` | pt-BR | as portas e janelas não estão furando as paredes no ifc, vê quais não tem abertura | Check doors/windows without openings in walls | hard, file | Find IfcDoor/IfcWindow whose IfcOpeningElement fill relation is missing; list GUIDs. |
| S35 `en-openings-s006` | en | walls show no holes after opening this ifc, windows float in front. whats wrong | Openings not cutting the wall after import | medium, no file | Check IfcRelVoidsElement exists, void count limit, whether openings were applied; suggest Apply Openings or regenerate. |
| S36 `fr-geom-s012` | fr | le mur-rideau est bizarre dans l'IFC, les meneaux manquent. tu peux verifier les IfcCurtainWall et leurs composants ? | Curtain wall geometry exports wrong | medium, file | Inspect curtain wall decomposition, count members and plates, report missing parts. |
| S37 `it-geom-s015` | it | nel modello IFC mancano i parapetti delle scale, controlli quali IfcStair non hanno IfcRailing? | Stair railings missing | medium, file | Find IfcStair without associated IfcRailing and report. |
| S38 `en-geom-s004` | en | check stairs: any IfcStair with predefined type NOTDEFINED, and any stair with no railing nearby | Which stairs lack railings or a PredefinedType | medium, file | List IfcStair with PredefinedType; report NOTDEFINED; check IfcRailing presence via aggregation and bounding-box proximity. |

### 6. Writing to the model, sheets, submissions

For Revit/Archicad MCP servers that can create things. A good answer confirms level, type and coordinates, and reads back what it made.

| # / id | Lang | Prompt (SYNTHETIC) | Meaning (EN) | Difficulty | A good answer should |
|---|---|---|---|---|---|
| S39 `en-aimcp-s005` | en | draw a 6m wall on level 2 from 0,0 to 6000,0 - make sure its really on level 2 and type is generic 200 | Create wall on Level 2 not Level 1 | medium, file | Resolve Level by name, wall type by name, create wall, read back level and elevation. |
| S40 `es-aimcp-s016` | es | creá cuatro muros de 3 m en rectángulo 5x4 y después contame cuántos hay | Create rectangle of walls | easy, file | Create four walls, count, report; avoid duplicates on retry. |
| S41 `zh-revit-auto-s012` | zh | 把DWG的A-WALL圖層翻成牆,放在2F,牆型用RC牆200 | Build walls from a CAD wall layer on a chosen level | hard, file | Read the layer, detect centerlines, preview count, create walls on level 2F with the named type, report skipped segments. |
| S42 `en-revit-auto-s002` | en | make a sheet per level, put the plan on it, number them A101 upward, use our A1 titleblock | Create sheets for each level and place plans | medium, file | Find A1 titleblock type, create sheets with sequential numbers, place each level's plan viewport centered, report conflicts with existing sheet numbers. |
| S43 `en-permit-s001` | en | need to submit to corenet x tomorrow, can u check if my ifc has all the IFC-SG required classes and psets? list what's missing | Check whether the model has the data required for a Singapore CORENET X submission | hard, file | Inspect IFC classes and property sets against the IFC+SG requirements the user supplies or the tool knows; report missing items per class; do not claim agency approval. |
| S44 `zh-permit-s009` | zh | 报建用的模型导出IFC要注意什么？构件编码和属性怎么挂才能被智能审查识别 | How to prepare a model for automated review | medium, no file | Explain classification codes, property mapping, export settings; say specifics depend on local review platform. |
| S45 `ru-tim-expertiza-s006` | ru | как настроить экспорт из ревита в ifc чтобы прошло по требованиям экспертизы? какую версию и MVD ставить | How to export Revit to IFC so that the customer's requirements and expertise pass | medium, no file | Explain IFC version/MVD choice, export settings, mapping tables and property set export, noting to confirm the customer's EIR. |
| S46 `en-gh-ifcopenshell-s012` | en | why wont annotation work on this revit ifc, no annotation context? | Missing Annotation context | medium, file | Check IfcGeometricRepresentationContext list, report missing Annotation/PLAN_VIEW and offer to add. |

## How to role-play this persona in tests

**Voice.** Describes what is *visible*: "windows float in front", "everything is grey", "doors invisible in plan", "walls show no holes". Double question marks, "??", "whats wrong", "заходит какими-то глупыми телами" are normal. Names the program and the year ("revit 2024", "archicad 22") but not the IFC exporter build. German: "woran liegts"; French: "pourquoi mes paramètres partagés sortent pas"; Spanish: "qué onda"; Japanese: ends with "…" and asks "何が落ちてるか調べて". Many prompts are how-to questions, not model queries.

**Typical context.** One authoring program plus one receiving program (Archicad to Revit, Revit to Solibri, Renga to Revit). IFC2x3 vs IFC4 is a source of guesswork. In the base, architect records mention IFC4 126 times, IFC2x3 69 times, unknown 74. Often *no file is attached*, or the file is named only as "this ifc".

**Knowledge level.** Expert in the authoring tool, novice in IFC. Understands "class" when told it is the category an element belongs to; does not know about relationships, representations or MVDs. Will accept a UI step list ("Export > IFC > Modify setup > ...") more readily than a schema explanation.

**Typical follow-ups.**
- "ok but where do I click"
- "so is it the file or my Revit?" (the assistant can only inspect the file; it should say so)
- "can you just fix it and give me a new ifc" / "dont touch my file"
- "I need walls not generic models. open or link?"
- "will the structural engineer see this in Tekla / Solibri?"
- "that worked in revit 2024, why not 2025?"

**Traps worth including.** Prompts with no file but an expectation of file inspection; a question where the right answer is a setting in the authoring tool, not in the IFC; an edit request on a Revit-exported file where annotations or openings might break; "put the sofa by the window" style requests that need a view or coordinates; creating a wall without saying the level (see synthetic `en-aimcp-s005`: "make sure its really on level 2"); units (mm vs m) in create-geometry prompts.

**How to judge the answer.**
1. Separates *what is in the IFC* from *what Revit/Archicad will do on import*; does not claim to know Revit settings it cannot see.
2. Gives the lever, not only the diagnosis: which export option, which mapping parameter, which import mode.
3. For write requests: confirms level, wall type and coordinates, creates exactly the requested objects, reads back the result, and does not silently use "the first level" (a defect reported in [zh-aimcp-r010](https://github.com/shuotao/REVIT_MCP_study/issues/144): the tool picked the first Level and Z=0 when no level was given).
4. Uses the user's language and measurements; mm vs m stated.
5. When asked to list rooms, areas or classes, results match what a human would check in the viewer (count, names, levels).
6. Does not promise that an authority will accept the file.

**Related personas.** [BIM coordinator](bim_coordinator.md) (who reports the problem), [BIM manager](bim_manager.md) (who owns the export template), [Reviewer / authority](reviewer_authority.md), [Owner / client](owner_client.md).
