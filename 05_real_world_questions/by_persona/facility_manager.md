# Facility manager: who they are and what they do with IFC

**Last built: 2026-11-06 · Persona code:** `facility_manager` · **Data behind this page:** 67 records (25 real, 42 synthetic; `python tools/kb.py stats --persona facility_manager`). Languages: en 44, es 4, zh 4, fr 3, ja 3, de 2, ru 2, it 1, ko 1, nl 1, no 1, pt 1. **Real facility-side voices are rare.** The real list below deduplicates a handful of GitHub and forum threads and adds adjacent records about COBie and handover that the research tagged to other personas. Non-English real FM posts exist only for Dutch and Japanese; the other languages are synthetic.

## In plain words

A facility manager (FM) runs a building *after* it has been built: heating and ventilation maintenance, cleaning, tenant requests, space allocation, replacing equipment at the end of its life. They work in a **CAFM / CMMS** system (computer-aided facility management / maintenance management; in French GMAO, in Norwegian FDV, in Japanese 維持管理, in Chinese 运维). The system wants tidy tables: one row per room, one row per piece of equipment, each with an ID, a location and a manufacturer.

They do not want a 3D model. They want **the data inside it, in a table**. IFC is a container that might hold that data, and COBie is the standard spreadsheet layout many handovers use. The facility manager's whole relationship to IFC is: *"Can I get my lists out of it, are they complete, and will the IDs still match next year?"*

An analogy: the building model is a warehouse database; the FM wants a printout of the stock list, plus a flag on every row where the supplier forgot to fill in the serial number.

## Daily IFC tasks

| # | Task | What it looks like in practice | Evidence |
|---|---|---|---|
| 1 | Get the room list | Room number, name, level, net area, department or finish, one row per room, for the CAFM. | synthetic `en-cobie-s004`, `de-cobie-s009`, `zh-lightweight-review-s017`; room-list prompts exist in nine languages in the base |
| 2 | Get the equipment list | Tag, class/type, system, manufacturer, model, serial, warranty, room. Often by system (AHU-03). | synthetic `en-reddit-s011`, `fr-cobie-s013`, `ja-cobie-s014` |
| 3 | Find what is missing before taking over | Equipment without type, space or manufacturer; spaces with no name; empty Systems. | synthetic `en-cobie-s001` ("handover is friday ...") |
| 4 | Produce or repair a COBie spreadsheet | 15 of 20 tabs present, Systems empty, Type length empty, an Excel export that fails while ODS works. | [en-gh-ifcopenshell-r027](https://github.com/IfcOpenShell/IfcOpenShell/issues/5926), [en-gh-ifcopenshell-r028](https://github.com/IfcOpenShell/IfcOpenShell/issues/6068), [en-cobie-r011](https://github.com/IfcOpenShell/IfcOpenShell/issues/3901) |
| 5 | Keep IDs alive | Link CAFM assets to GlobalId; survive new phases and new versions. | [en-gh-revit-ifc-r048](https://github.com/Autodesk/revit-ifc/issues/65), [nl-cobie-r016](https://github.com/OpenAEC-Foundation/open-bim-platform/issues/10) |
| 6 | Ask relationship questions | What does AHU-03 serve; which spaces belong to which zone; which door connects which rooms (access control). | [en-spaces-r028](https://forums.buildingsmart.org/t/space-data-depending-on-zone/4434), [en-spaces-r029](https://forums.buildingsmart.org/t/relation-between-doors-to-rooms/3961) |
| 7 | Add operations data | Warranty duration, service interval, maintenance frequency to a class of equipment. | synthetic `en-fmor-s010`, `es-latam-s008` |
| 8 | Run a multi-building estate | Equipment codes across ~100 buildings; mixed Revit, ArcGIS and EAM tools. | [en-osarch-gis-r014](https://community.osarch.org/discussion/1118/operation-and-maintenance-on-campus-site-with-ifc) |

## Goals

- **CAFM-importable lists on the first try** (right columns, no blanks in required fields, unique codes).
- **Know what is missing** before signing off the handover, in a form that can be sent back to the contractor ([Owner / client](owner_client.md)).
- **Stable IDs** between model versions so asset records do not detach ([en-gh-revit-ifc-r048](https://github.com/Autodesk/revit-ifc/issues/65): new phases change GUIDs and break external databases keyed on them).
- **Manufacturer and warranty data in a standard place**, ideally `Pset_ManufacturerTypeInformation` for types and `Pset_ManufacturerOccurrence` for serial numbers (see [IFC FM domain overview](../../01_ifc_basics/08_domains_mep_structural_infra_4d5d_fm.md)).
- **Low-cost tools** (free viewer, open-source FM) instead of heavy licences ([ja-qiita-r036](https://qiita.com/watanabe-tsubasa/items/bcd3cfbd7dc653a580b5), [en-osarch-gis-r014](https://community.osarch.org/discussion/1118/operation-and-maintenance-on-campus-site-with-ifc)).

## Pains (ranked)

_Quoted phrases in the last column are illustrative: some paraphrase real records, others are taken from the synthetic prompts further down. Only the tables of real records are evidence of what people actually wrote._

Ranked by topic counts (cobie_fm_handover 56, spaces_rooms_areas 25, zones_groups_systems 9) and the records' content.

| Rank | Pain | Signal | Typical shape |
|---|---|---|---|
| 1 | **COBie output incomplete or empty** | `troubleshoot_export` 12 | "5 of the standard 20 tabs missing", "Systems tab empty though Bonsai lists 214 systems", "COBie.Type.Length always empty" |
| 2 | **Required handover fields blank** | `validate_check` 6 + synthetic | "which equipment has no manufacturer or serial number? need it for handover friday" |
| 3 | **Spaces: unnamed, unassigned, or duplicated numbers** | `spaces_rooms_areas` 25 | "spaces all say Room", "furniture sits under storeys not spaces, FM says rooms are empty" |
| 4 | **Spreadsheet import fails in the CAFM** | synthetic | "upload to the FM system gives an error; find which row; duplicate asset code?" |
| 5 | **Identity drift between versions** | `guid_change_tracking` 2 | GUID changes with new phases; keys in external databases |
| 6 | **Excel vs ODS, units and encoding quirks** | tooling | "exporting to Excel errors, ODS works"; metres and millimetres on one sheet ([en-cobie-r022](https://community.osarch.org/discussion/comment/30246)) |
| 7 | **Not knowing which tool does what** | `find_tool` | "I need a free 3D viewer from IFC and an IFC entity for unique equipment codes" |

## Vocabulary they use (and what they do not know)

### Words and phrases you will see

| Phrase (language) | Plain meaning |
|---|---|
| CAFM / CMMS / IWMS / GMAO (fr) / FDV (no) / 运维 (zh) / 維持管理 (ja) / DOE (fr, as-built file) | The operations software that must receive the data. |
| handover, as-built, O&M manual, "asset register", asset tag, serial, warranty, PPM (planned maintenance) | The vocabulary of getting a building into operation. |
| COBie, "COBie tabs", Type / Component / Space / System / Floor, UK vs US template (Uniclass vs OmniClass) | The spreadsheet layout and its two regional flavours. |
| room list, "Raumliste", "liste des locaux", "лист помещений", 部屋一覧, 房间清单, NGF/BTA/NTA | One row per room. |
| zone, system, "AHU-03", "ПВ-03" | A group of rooms (zone) or equipment (system). |
| NEN 2767 (nl) | Dutch condition-assessment scale for building parts. |
| "what is blank?", "show me the empties", "mark the missing ones" | The FM's native verification step. |

### What they typically do not know, or get wrong

- **IFC names.** They say room, equipment, system; IFC says `IfcSpace`, equipment classes, `IfcSystem`/`IfcZone`. The assistant should translate silently.
- **Where each fact lives.** Manufacturer and model usually sit on the **type**, the serial number on the individual **occurrence** (general IFC practice; see the pset overview). A request "list equipment with manufacturer and serial" therefore needs both levels.
- **That a COBie sheet is a derived view.** An empty Systems tab typically means systems are missing upstream, not that the export button is broken (see the [COBie topic page](../by_topic/classification_cobie_fm.md)).
- **That equipment may be stored as generic proxies**, so "list all pumps" can return nothing.
- **Net vs gross area** and which area field the CAFM expects.

Read next: [Classification, COBie and FM handover (topic page)](../by_topic/classification_cobie_fm.md), [materials, spaces, zones](../by_topic/materials_spaces_zones.md), [FM in the IFC domain overview](../../01_ifc_basics/08_domains_mep_structural_infra_4d5d_fm.md), [spatial structure](../../01_ifc_basics/04_spatial_structure_and_relationships.md), [properties and quantities](../../01_ifc_basics/05_properties_quantities_psets.md), [viewers, checkers, CDE, converters](../../03_software/viewers_checkers_cde_converters.md), [EIR / BEP clauses](../../02_standards_regulations/requirements_in_contracts_eir_bep.md).

## Real questions (32, linked)

Paraphrases of questions or issues seen at the linked sources, kept in the asker's language. Language mix in this list: Russian 0, English 28, other languages 4. Where a source page is not in English but the stored paraphrase is, the Lang column still shows the page language. Honest limit: only groups A to C are tagged `facility_manager`; group D is tagged to neighbouring personas.

### A. The spreadsheet that comes out is wrong (COBie / IfcFM)

The same Bonsai issues were recorded several times by different research cells (for example the 5-of-20-tabs issue appears four times under `facility_manager` alone); each is listed once here.

| # | Lang | Their words (paraphrase, original language) | English gloss / context | Source (record id, type, year) |
|---|---|---|---|---|
| 1 | en | compares two xlsx exports of Clinic model | Bonsai COBie export lacks 5 of 20 standard tabs vs BIM Vision output | [en-gh-ifcopenshell-r027](https://github.com/IfcOpenShell/IfcOpenShell/issues/5926) github_issue, 2025 |
| 2 | en | 214 systems in Bonsai but empty tab in spreadsheet | COBie systems sheet empty though Bonsai lists 214 systems | [en-gh-ifcopenshell-r028](https://github.com/IfcOpenShell/IfcOpenShell/issues/6068) github_issue, 2025 |
| 3 | en | Any idea what is happening here? (console log of import process) | Error when exporting COBie; pastes long console log and asks what is happening. | [en-us-canada-infra-r011](https://github.com/IfcOpenShell/IfcOpenShell/issues/5702) github_issue, 2024 |
| 4 | en | multiple IFCs selected in FM tab, export to Excel fails, ODS fine; used CC BY-SA sample files | Exporting several IFC files to one Excel in IfcFM errors, but ODS export works. | [en-cobie-r011](https://github.com/IfcOpenShell/IfcOpenShell/issues/3901) github_issue, 2023 |
| 5 | en | COBIE.Type.Length, Width, Height always empty. | COBie.Type Length/Width/Height fields are always empty on export. | [en-us-canada-infra-r027](https://forums.autodesk.com/t5/revit-architecture-forum/cobie-type-length-cobie-type-width-cobie-type-height-is-always/td-p/11009379) forum, 2022 |
| 6 | en | Can extra parameters be added to COBie export? | Does the COBie Extension allow adding extra parameters? | [en-us-canada-infra-r029](https://forums.autodesk.com/t5/revit-architecture-forum/does-cobie-extension-allow-adding-extra-parameters-in-revit/td-p/8188015) forum, 2018 |
| 7 | en | spec permits spaces in names, QC serializer should match | COBie QC report seemed to reject underscores and spaces in Name fields. | [en-cobie-r014](https://github.com/opensourceBIM/COBie-plugins/issues/6) github_issue, 2015 |
| 8 | en | serializer exports IfcSpaceType, IfcWallType, IfcWall that are not COBie types | COBie spreadsheet serializer exports non-COBie types like IfcWallType and IfcSpaceType. | [en-cobie-r019](https://github.com/opensourceBIM/COBie-plugins/issues/7) github_issue, 2015 |

### B. "Can IFC carry my operations data, and which tool do I use?"

The truest facility-side voices in the base: a campus O&M manager, a Dutch facility-app specification, a Japanese low-cost-FM blog, a politely hedged newcomer.

| # | Lang | Their words (paraphrase, original language) | English gloss / context | Source (record id, type, year) |
|---|---|---|---|---|
| 9 | en | asks politely, uncertain, whether IFC can carry room areas, doors, windows and fire extinguishers for FM without geometry | Can IFC hold FM data (room areas, doors, windows, extinguishers) without a full 3D model? | [en-cobie-r002](https://community.osarch.org/discussion/449/ifc-and-input-data-for-facility-management) forum, 2021 |
| 10 | en | Does anyone know a similar project? Which IFC entity assigns a unique code to each piece of equipment so plumbing, ventilation and electrical items can be identified during O&M? | MEP O&M manager for ~100 buildings uses Revit, ArcGIS and InforEAM in separate departments; wants a free 3D viewer from IFC and an IFC entity for unique equipment codes. | [en-osarch-gis-r014](https://community.osarch.org/discussion/1118/operation-and-maintenance-on-campus-site-with-ifc) forum, 2022 |
| 11 | nl | manager clicks an installation and sees data, maintenance and reports; data from IFC or COBie; IDS for handover; GlobalIds must survive versions | Facility management app on the as-built model: link assets via GlobalId, maintenance plans, fault reports to ERP work orders, NEN 2767 condition. | [nl-cobie-r016](https://github.com/OpenAEC-Foundation/open-bim-platform/issues/10) github_issue, 2026 |
| 12 | ja | Bonsai as a low-cost alternative for facility management | Managing facilities cheaply with Blender and Bonsai instead of Revit. | [ja-qiita-r036](https://qiita.com/watanabe-tsubasa/items/bcd3cfbd7dc653a580b5) blog, 2025 |
| 13 | en | US state DOT with 500+ projects/year wants system-wide asset query (e.g., bridges with certain bearings and their age) from as-built IFC | How to keep IFC organized for asset management and query assets across hundreds of project models? | [en-cobie-r008](https://community.osarch.org/discussion/comment/25545) forum, 2025 |
| 14 | en | question about COBie-compliant storage of manufacturer data | Are nominated manufacturers and procurement data stored in a COBie-compliant way? | [en-cobie-r024](https://community.osarch.org/discussion/comment/12333) forum, 2022 |
| 15 | en | which parameters should I export for QS, coordination, construction and FM? | IFC export rules and pain points per purpose: coordination, QS, construction, FM. | [en-blogs-linkedin-r023](https://bimcorner.com/ifc-export-rules-part-2-what-parameters-to-export-dos-and-donts/) blog |

### C. Spaces, zones, identifiers and viewers

Rooms that belong to two zones, doors that need from/to rooms for access control, GUIDs that change between phases, a roof "space" that renders as a solid box.

| # | Lang | Their words (paraphrase, original language) | English gloss / context | Source (record id, type, year) |
|---|---|---|---|---|
| 16 | en | five candidate options: psets, classification, proxies, extra zone, IfcAsset | One space belongs to zones M and N with different room numbers; how to represent in IFC? | [en-spaces-r028](https://forums.buildingsmart.org/t/space-data-depending-on-zone/4434) forum, 2022 |
| 17 | en | fromRoom/toRoom relation between IfcDoor and IfcSpace for locking systems | Should IFC link doors to from/to rooms for access control? | [en-spaces-r029](https://forums.buildingsmart.org/t/relation-between-doors-to-rooms/3961) forum, 2021 |
| 18 | en | Can't export Pset_SpaceParking | Pset_SpaceParking cannot be exported. | [en-ghrevitifc-r033](https://github.com/Autodesk/revit-ifc/issues/618) github_issue, 2023 |
| 19 | en | New phases change GUIDs and break external databases keyed on them. |  | [en-gh-revit-ifc-r048](https://github.com/Autodesk/revit-ifc/issues/65) github_issue, 2018 |
| 20 | en | comparing same model in Dalux, BIMvision and That Open BIM App, one IfcSpace at roof level is a big solid box above the roof only here | One IfcSpace ("4 - Roof") renders as a large solid box in That Open app but not in Dalux or BIMvision | [en-gh-thatopen-r055](https://github.com/ThatOpen/engine_fragment/issues/301) github_issue, 2026 |
| 21 | en | importing types referencing the same IfcClassification creates a new duplicate IfcClassification each time | Importing types from a library duplicates IfcClassification for each imported type. | [en-ios-r020](https://github.com/IfcOpenShell/IfcOpenShell/issues/7150) github_issue, 2025 |

### D. Adjacent: Revit COBie, thin extraction and as-built delivery rules

Tagged as coordinator, manager or owner in the raw files, but the job is handover data.

| # | Lang | Their words (paraphrase, original language) | English gloss / context | Source (record id, type, year) |
|---|---|---|---|---|
| 22 | en | Mapped COBie data to Revit parameters, exported with COBie 2.4 Design Deliverable setup, but COBie type/component names are missing from the IFC; do not want to remap. | COBie parameters mapped in Revit (Type Name, Component Name) are missing in IFC exported with the 'IFC 2x3 COBie 2.4 Design Deliverable' setup. | [en-us-canada-infra-r001](https://forums.buildingsmart.org/t/cobie-to-ifc-export-issues/1860) forum, 2019 |
| 23 | en | COBie data export problem in Revit MEP. | Revit MEP COBie data export issue. | [en-us-canada-infra-r028](https://forums.autodesk.com/t5/revit-mep-forum/revit-mep-cobie-data-export-issue/td-p/11566679) forum, 2022 |
| 24 | en | Parameter mapping not working in Interoperability Tools. | Interoperability Tools parameter mapping is not working. | [en-us-canada-infra-r030](https://forums.autodesk.com/t5/revit-architecture-forum/revit-interoperability-tools-parameter-mapping-is-not-working/td-p/11512969) forum, 2022 |
| 25 | en | COBie Type spreadsheet missing families. | COBie Type spreadsheet is missing families. | [en-us-canada-infra-r031](https://forums.autodesk.com/t5/revit-architecture-forum/bim-interoperability-tool-cobie-type-spreadsheet-missing/td-p/9628148) forum, 2020 |
| 26 | en | tested on Dormitory sample project; sorting Type.Name revealed blanks; asks to check all sheets | COBie.xls export inserted 47 blank rows in most sheets. | [en-cobie-r013](https://github.com/opensourceBIM/COBie-plugins/issues/13) github_issue, 2015 |
| 27 | en | COBie issue where metres and millimetres appear on the same sheet | COBie sheet mixes metres and millimetres. | [en-cobie-r022](https://community.osarch.org/discussion/comment/30246) forum, 2026 |
| 28 | en | walks IsDefinedBy and matches property names; custom NEOM_* parameters missing in 22.6 output, viewers show them | Script reading COBie and custom parameters worked for exporter 22.1 but not 22.6. | [en-cobie-r017](https://github.com/IfcOpenShell/IfcOpenShell/issues/3978) github_issue, 2023 |
| 29 | en | thesis on COBie delivery for a curtain wall company; edited ignore XML files without effect; items show in Document sheet only | Curtain wall panels (IfcPlate) and mullions (IfcMember) do not appear in the COBie Type and Component sheets, only in Document. | [en-cobie-r005](https://github.com/opensourceBIM/COBie-plugins/issues/10) github_issue, 2015 |
| 30 | en | python script exports parameters per IFC entity to Excel per file; works for exporter 22.1 but structure changes in 22.6; includes COBie properties and client-specific operations/BOQ/LOD parameters | Script extracting COBie and custom client parameters to Excel breaks between Revit IFC exporter versions | [en-fmor-r009](https://github.com/IfcOpenShell/IfcOpenShell/issues/3978) github_issue, 2023 |
| 31 | zh | 竣工模型交付用什么格式，要在施工图模型基础上加变更信息吗 | Nanjing local standard for as-built (completion) BIM delivery; format preferably 宁建模. | [zh-lightweight-review-r025](https://amr.nanjing.gov.cn/ztzl/bzhzl/tzgg/202302/P020230216538033075572.pdf) regulation, 2023 |
| 32 | es | tabla que asocia parámetro con atributo IFC, Pset y propiedad, requerido u opcional, exportación automática o 'a ingresar' | Planbim information matrix v3.0 maps each parameter to IFC attribute, Pset, property, required/optional, auto/manual export, COBie | [es-latam-r012](https://planbim.cl/documentos/mide/) official_doc, 2022 |

## Ready test prompts (45, synthetic)

**All prompts below are SYNTHETIC.** Ids starting `new-fm-` were written for this page, each inspired by the record named in its tag; the rest come from the research files. The first column keeps the id so you can trace the origin.

### 1. Room and space lists

The most frequent FM request in every language: number, name, level, area, sometimes department or finish.

| # / id | Lang | Prompt (SYNTHETIC) | Meaning (EN) | Difficulty | A good answer should |
|---|---|---|---|---|---|
| S1 `en-beginner-qa-s009` | en | need list of rooms with area and level for the FM sheet | Room areas list | medium, file | List IfcSpace name, number, level, net floor area; flag missing areas. |
| S2 `en-fmor-s002` | en | give me all spaces with number, name, net area and department/occupant, sorted by floor | List rooms with area and department for space management | easy, file | Query IfcSpace, read Qto_SpaceBaseQuantities.NetFloorArea and relevant psets, show spaces by storey; note missing values. |
| S3 `en-autodesk-revit-export-s017` | en | list all rooms with area and department from the ifc for FM, spaces only |  | easy, file | Extract IfcSpace Name, area quantity and department property. |
| S4 `en-gh-revit-ifc-s010` | en | total net floor area per storey from IfcSpace, and which spaces have no area at all | Space areas | easy, file | Sum area quantities per storey, list spaces with missing quantities. |
| S5 `en-gh-thatopen-s002` | en | list all IfcSpaces per storey, and tell me which ones arent attached to any storey | List all IfcSpace per storey and flag spaces not contained in any storey | medium, file | Traverse IfcRelAggregates/ContainedInStructure, list spaces by storey, report orphan spaces. |
| S6 `ru-renga-nanocad-s015` | ru | таблицу помещений: номер, название, площадь, этаж | Table of rooms with names, numbers and areas | easy, file | List IfcSpace with Name/LongName, NetFloorArea from Qto_SpaceBaseQuantities, and containing storey; flag spaces without area. |
| S7 `new-fm-n02` (new, inspired by de-cobie-s009) | ru | в каких помещениях нет номера? CAFM не принимает импорт без номера | Which rooms have no number; CAFM refuses import without it | easy, file | List IfcSpace with empty or missing number (state which attribute is the number: Name, LongName or a property); counts; storey; GlobalId. |
| S8 `new-fm-n04` (new, inspired by en-cobie-s004) | en | our CAFM wants one row per room with a unique room code. are there duplicate room numbers in the model? | Duplicate room numbers before CAFM import | easy, file | Group IfcSpace by the room-number field; list duplicates with storeys and GlobalIds; mention spaces with empty numbers. |
| S9 `en-mea-s008` | en | room schedule pls - room no, name, area, floor finish, level. export to excel | Room schedule with areas and finishes for handover. | easy, file | Read IfcSpace with Qto area and finish properties, group by storey, output a table and offer CSV/XLSX; warn on missing data. |
| S10 `de-dach-s014` | de | Raumliste mit Nutzung und Fläche für die FM-Übergabe, Räume ohne Namen markieren | List all rooms with area and usage for FM handover. | easy, file | List IfcSpace with Name, LongName, area from Qto_SpaceBaseQuantities, flag unnamed. |
| S11 `de-cobie-s009` | de | prüf mal ob jeder Raum eine Raumnummer und NGF hat, sonst klappt der CAFM-Import nicht | Check rooms for room numbers and area before CAFM import. | easy, file | List IfcSpace missing Number/LongName/NetFloorArea; duplicates of room numbers. |
| S12 `fr-gis-s015` | fr | sors moi la liste des locaux avec surface, niveau et nom pour la GMAO, et dis moi lesquels n'ont pas de surface | List rooms with area and level for the CMMS. | easy, file | List IfcSpace with area, storey, name; flag missing area; table. |
| S13 `it-italy-s014` | it | lista locali con superficie e nome, quelli senza nome segnali | Rooms with area and name | easy, file | List IfcSpace with Name and area; flag missing names. |
| S14 `ko-korea-s013` | ko | 실별 면적표 만들어줘 실명 번호 면적 | Room area schedule | easy, file | Extract IfcSpace LongName/Number and area quantities into a table. |
| S15 `no-norway-s013` | no | lag romliste med romnr, navn og BTA/NTA fra modellen | Space list with area and number for the building | easy, file | Extract IfcSpace with name, long name, area quantities and export a table. |
| S16 `zh-lightweight-review-s017` | zh | 出个房间清单，编号、名称、面积，运维交付用 | Room list with area and department for handover. | easy, file | List IfcSpace with number, name, area per storey as table. |
| S17 `zh-tw-hk-s016` | zh | 竣工模型要交FM，幫我匯出房間清單：編號、名稱、面積、樓層 | Export room list for FM handover | medium, file | List IfcSpace with number, name, area, storey as table. |
| S18 `en-fmor-s016` | es | dame todos los espacios con nombre y area, por planta, es para el plan de mantenimiento | List rooms and areas for the maintenance plan | easy, file | Query IfcSpace with name/area grouped by storey. |

### 2. Equipment and asset lists

Manufacturer, model, serial, warranty and location for the CAFM/CMMS. Empty fields must be shown, not filled.

| # / id | Lang | Prompt (SYNTHETIC) | Meaning (EN) | Difficulty | A good answer should |
|---|---|---|---|---|---|
| S19 `en-reddit-s011` | en | could you pull all equipment with manufacturer, model and serial number for our FM system | Asset list for FM | medium, file | List IfcDistributionElement/equipment with Pset_ManufacturerTypeInformation and serial fields; flag blanks. |
| S20 `en-viewconv-s016` | en | give me equipment list w/ serial number + space it sits in, excel for FM team | List all equipment with serial and location to Excel for FM | medium, file | Query equipment elements, psets serial, containing space, export xlsx, flag missing. |
| S21 `en-uk-anz-india-s003` | en | pull out a COBie style Type and Component list from this IFC - name, category, manufacturer, serial no, space. just spot check for now | Prepare COBie Type and Component data | medium, file | Collect types and occurrences, map to COBie columns, flag empty fields, return a table or CSV. |
| S22 `en-gis-s003` | en | list every piece of MEP equipment with its tag/asset id + classification ref, as a table, I need to push this into our CMMS | List all equipment with asset tag and classification for loading into a CMMS and GIS. | medium, file | Enumerate MEP element classes, extract Tag/Name/Pset asset identifiers and IfcClassificationReference, flag missing values, return a table/CSV. |
| S23 `ru-cobie-s005` | ru | перед сдачей эксплуатации проверь у всего оборудования есть серийник и дата монтажа? что пустое - списком | Check that every equipment has a serial number and installation date before handover to operations. | medium, file | Scan equipment elements for SerialNumber and InstallationDate properties; list those missing grouped by system/floor. |
| S24 `new-fm-n01` (new, inspired by ru-cobie-s005) | ru | список оборудования по системам: производитель, модель, серийник, помещение. в эксель для CAFM, пустые поля выдели | Equipment by system with manufacturer, model, serial, room; Excel for CAFM, mark empties | medium, file | Table of equipment (class, tag, system, manufacturer, model, serial, space); empty cells shown explicitly, not invented; state which pset each column came from; xlsx or csv. |
| S25 `fr-francophone-s011` | fr | fais moi la liste des équipements avec fabricant et référence pour le DOE / GMAO | List equipment with manufacturer and model for the DOE handover | medium, file | Export equipment elements with Pset_ManufacturerTypeInformation fields to a table; flag blanks. |
| S26 `ja-japan-s011` | ja | 維持管理用に、機器の名称・メーカー・型番・設置階と室をExcelに出して。空欄の項目も分かるように | Export equipment list with maker, model number and install location to Excel | medium, file | Query IfcDistributionElement/IfcFlowTerminal, read manufacturer/model properties, containing storey and space, write table, mark blanks. |
| S27 `es-spain-s011` | es | para la entrega a mantenimiento, comprueba que los equipos tengan marca, modelo y numero de serie | Check COBie readiness | medium, file | Check Pset_ManufacturerTypeInformation fields on equipment, report missing. |
| S28 `pt-data-s011` | pt | preciso da lista de equipamentos com tag, ambiente e fabricante pra entrega do FM, em planilha | Extract an equipment list with tag, space and manufacturer for FM handover | medium, file | List mechanical/electrical equipment with Tag, containing space and manufacturer from psets, flag missing manufacturer, output spreadsheet-ready table. |
| S29 `zh-cobie-s007` | zh | 把模型里所有设备按楼层和房间导成表格，资产编号、系统、厂家都要，给运维系统导入用 | Export asset list of equipment with floor and room to Excel for the FM system. | medium, file | Query equipment with floor, space, system, manufacturer, tag; export spreadsheet; flag missing asset IDs. |
| S30 `ja-cobie-s014` | ja | 部屋ごとの設備一覧を出して。型番とメーカーも。FM台帳に入れたい | List equipment per room for the facility management ledger. | medium, file | Group equipment by IfcSpace; include model number and manufacturer; list items without room. |
| S31 `fr-cobie-s013` | fr | sors moi l'inventaire des équipements avec fabricant, garantie et local pour la GMAO | Export equipment inventory with manufacturer and warranty for the CMMS. | medium, file | Extract equipment properties and spaces to table; flag blanks. |
| S32 `es-cobie-s011` | es | dame todos los dampers cortafuegos con planta y local, para el mantenimiento | List all fire dampers with their floor and space. | easy, file | Filter IfcAirTerminal/IfcDamper by type/name; report storey and containing space. |
| S33 `en-allplan-vw-bentley-s009` | en | door schedule per level w/ fire rating from the ifc | List door counts per floor with fire rating | easy, file | Group IfcDoor by storey, include FireRating, output table; flag missing values. |
| S34 `en-gh-xbim-others-s010` | en | list all IfcSensor + their pset values, i need them for FM system | List sensors/equipment with a given Pset for FM import | medium, file | Query IfcSensor (and related flow controllers), output name, GUID, space and all psets as table. |

### 3. What is missing, what depends on what



| # / id | Lang | Prompt (SYNTHETIC) | Meaning (EN) | Difficulty | A good answer should |
|---|---|---|---|---|---|
| S35 `en-cobie-s001` | en | handover is friday, which equipment in the ifc has no type or space or manufacturer? cobie wants all 3 | Which equipment components lack Type, Space or Manufacturer for COBie handover? | medium, file | List IfcElement occurrences lacking type assignment, spatial containment/space, and Pset_ManufacturerTypeInformation.Manufacturer; report counts and names. |
| S36 `en-blogs-linkedin-s009` | en | furniture sits under storeys not spaces, FM says rooms are empty. confirm? | Check furniture containment | medium, file | List IfcFurnishingElement containers, count under storey vs IfcSpace, report. |
| S37 `en-fmor-s012` | en | cobie sheet comes out with empty System tab but the model has systems, why | COBie spreadsheet from our IFC has empty Systems sheet | medium, file | Check whether systems are IfcSystem with members assigned, check exporter assumptions, suggest fixes. |
| S38 `en-gh-ifcopenshell-s010` | en | bonsai shows 214 systems but my cobie systems tab is empty, check why | Systems for COBie | hard, file | List IfcSystem and members via IfcRelAssignsToGroup, check assignments, explain. |
| S39 `en-spaces-s005` | en | show all IfcZones and which spaces are in each, flag spaces in more than one zone | List zones and member spaces | medium, file | Query IfcRelAssignsToGroup for IfcZone, list members, flag multi-membership. |
| S40 `en-fmor-s005` | en | whats served by AHU-03? list components and the rooms | Which equipment belongs to the AHU-03 system | hard, file | Traverse IfcSystem/IfcRelAssignsToGroup and IfcRelServicesBuildings/Spaces for AHU-03; list components with tags and served spaces. |
| S41 `new-fm-n03` (new, inspired by en-fmor-s005) | ru | что обслуживает вентустановка ПВ-03? перечисли оборудование и помещения | What is served by supply unit PV-03: equipment and rooms | hard, file | Find the unit by tag/name; follow system membership and flow connections to list equipment and, where available, served spaces; explain if systems or relationships are not modelled. |

### 4. Adding or fixing data for operations

Write requests: a good answer changes a copy and lists what it touched.

| # / id | Lang | Prompt (SYNTHETIC) | Meaning (EN) | Difficulty | A good answer should |
|---|---|---|---|---|---|
| S42 `en-fmor-s010` | en | add warranty duration 5y and service interval 12 months to all fire dampers | Add warranty and maintenance interval properties to all fire dampers | medium, file | Select fire-damper IfcDamper types, add warranty/service properties, confirm count changed, save a new file copy. |
| S43 `es-latam-s008` | es | agrégale a todas las luminarias la propiedad frecuencia_mantenimiento y que tome el valor del tipo | Add a maintenance property to all luminaires and set the value from the type | hard, file | Create or update a custom Pset on all luminaire occurrences, copy values from type, save a new IFC, report changes. |
| S44 `en-us-canada-infra-s009` | en | spaces all say Room. rename from the room number prop and make sure each one is under the right storey | Set space names and floor refs for COBie | medium, file | Rename IfcSpace Name from a given property, verify spatial containment, report changes. |
| S45 `en-dynamo-pyrevit-s016` | en | need area and volume of all slabs in linked ifc, import dropped quantities | Quantities from linked IFC. | hard, file | Read Qto or compute from geometry. |

## How to role-play this persona in tests

**Voice.** Task-first, list-style, output-specified, often lower-case and clipped: "room schedule pls - room no, name, area, floor finish, level. export to excel" (`en-mea-s008`); "need a room list for the CAFM: space number, name, floor, net area, one row each" (`en-cobie-s004`); "pull out a COBie style Type and Component list ... just spot check for now" (`en-uk-anz-india-s003`); "handover is friday, which equipment in the ifc has no type or space or manufacturer? cobie wants all 3" (`en-cobie-s001`). Other languages are equally terse: "таблицу помещений: номер, название, площадь, этаж"; "維持管理用に、機器の名称・メーカー・型番・設置階と室をExcelに出して。空欄の項目も分かるように"; "fais moi la liste des équipements avec fabricant et référence pour le DOE / GMAO"; "lag romliste med romnr, navn og BTA/NTA fra modellen".

**Typical context.** A completed project's as-built IFC from the design or construction team, a named target system (CAFM, CMMS, FM sheet, COBie, "digital twin platform"), a deadline (handover). The FM often does not know which authoring tool produced the file, the IFC version, or whether the model has classification. Sometimes no model is loaded and the FM asks a concept question ("do we still need cobie or is ifc + ids enough?").

**Knowledge level.** Operations expert, IFC novice. Knows asset terms and the target system's import template. Treats the model as a database to query. Will not know a property-set name; may know "COBie".

**Typical follow-ups.**
- "mark the empty ones" / "which rows will break the import?"
- "csv with ; as separator" / "one row per room" / "sorted by floor"
- "only mechanical" / "only level 2" / "only fire dampers"
- "add warranty 5y and service interval 12 months to all of them" (write; ask for a new file)
- "what did you use as the room number?" (the assistant must state which field)
- "does this match what the contractor gave us in excel?" (compare two sources)

**Traps worth including.** Spaces named "Room" for all; room numbers in LongName instead of Name; area given in square millimetres or feet; equipment as proxies; duplicate asset codes; type-level vs occurrence-level properties; furniture or equipment attached to a storey instead of a space; a Systems tab that is empty because no `IfcSystem` exists; requests mixing languages (Cyrillic room names, Japanese property names), where encoding matters.

**How to judge the answer.**
1. All requested columns present, in the requested order, one row per entity.
2. Empty cells stay empty and are flagged; nothing is invented (serials, warranty dates).
3. States which property or attribute filled each column and whether it came from the type or the occurrence.
4. Counts reconcile (rooms listed + rooms excluded = rooms in the file).
5. File output is importable: delimiter, encoding and units stated; no formulas or merged cells in CSV.
6. For write requests: operates on a copy, lists what was changed, reports unmatched rows.
7. Explains an empty COBie sheet as a data cause first, tool cause second.

**Related personas.** [Owner / client](owner_client.md) (who receives the handover), [BIM manager](bim_manager.md) (who must deliver it), [BIM coordinator](bim_coordinator.md), [Reviewer / authority](reviewer_authority.md).
