# Italian: how people ask about IFC, BIM and Revit

**Last researched: 2026-11-06** · Italy. Language code `it`.

## In plain words

IFC is the open file format used to hand a BIM model from one program to another. In Italy the topic is unusually tied to **law**: since 1 January 2025 public clients must use BIM methods on new works and interventions on existing buildings above EUR 2 million (Art. 43, D.Lgs. 36/2023), and the law asks for "open, non-proprietary formats", which in practice means IFC. So the Italian material is full of *capitolato informativo*, *stazione appaltante*, *oGI/pGI* and *ACDat*, next to the usual practical questions: Revit export loses properties, models do not overlap, walls turn into proxies, how to compare two revisions. Someone talking to an AI assistant with a loaded IFC will write short lowercase work orders: "quanti proxy ci sono?", "dammi l'area dei muri esterni per piano", "confronta rev A e rev B".

## How much data is behind this page (read first)

| Fact | Value |
|---|---|
| Italian records in the KB | 70 (28 real, 42 synthetic) |
| Real records that are a person's own forum post | **0** |
| What the 28 "real" records are | Real published Italian articles (vendor blog, trade site, regulation explainers). The text in the "question" field is the question each article answers, **rephrased by the research agent in a plausible user voice**. They are *not* verbatim posts. |
| Source bias | 24 of the 28 come from BibLus, the editorial site of the software vendor ACCA (which promotes its own usBIM, Edificius and EdiLus products); 4 come from Ingenio. Vendor framing is strong. |
| Evidence | 11 records read from page text, 17 from search snippets only |
| Synthetic prompts | 42, written by research agents from general knowledge of Italian BIM vocabulary |

The web-search budget ran out before the first search ([it-italy report](../../research_raw/wave1/it/it-italy.md)). Forums (Autodesk Italia returned HTTP 403), edilportale, Reddit, Telegram, Facebook groups, YouTube comments, ACCA's support forum and GitHub issues were **not reached**. Real user spelling, typos and frustration are therefore under-represented and **inferred**. Items from general knowledge are marked **(GK)**; items from synthetic prompts **(syn)**.

Evidence tags in the tables: **C** = published article or document (question reconstructed); **page** or **snippet** = how much the agent read.

## Where people ask

| Place | Evidence | Notes |
|---|---|---|
| BibLus (ACCA) editorial site, biblus.acca.it | **Read** (24 records) | Article titles are often questions ("L'offerta di gestione informativa è obbligatoria?"). Content is how-to plus product promotion (usBIM.revolution plugin, usBIM.checker). |
| Ingenio (ingenio-web.it) | **Read** (4 records) | Technical series ("IFC in pratica"), regulation news. |
| CNI report on digitalization (2026) | Linked from the report | Professional-body survey, not Q&A. |
| Autodesk Italia forum, edilportale, BIMportale, ACCA forum | **Not reached** (403 or nothing returned) | |
| Reddit (r/italy, r/Revit), Telegram, Facebook groups, YouTube | **Not reached** | |
| GitHub issues in Italian | **Not found** | |

## Top themes (ranked)

The report's ranking (from article frequency) combined with topic counts over the 70 records (`national_requirements` 11, `psets_properties` 8, `guid_change_tracking` 8, `validation_checking` 7, `class_mapping` 6).

| # | Theme | Typical need | Related KB doc |
|---|---|---|---|
| 1 | **Obbligo BIM** in public tenders: art. 43 D.Lgs. 36/2023, EUR 2 M threshold, from 1 Jan 2025, transitional rules, whether IFC is required | Is BIM mandatory for my tender? | [regulations_permits_contracts](../by_topic/regulations_permits_contracts.md) |
| 2 | *Capitolato informativo*, *offerta* (oGI) and *piano di gestione informativa* (pGI), ISO 19650 and UNI 11337 | Write or answer the information requirements | [regulations_permits_contracts](../by_topic/regulations_permits_contracts.md) |
| 3 | Revit to IFC export setup: class mapping, `IfcExportAs`, MVD (Coordination View 2.0), IFC2x3 vs IFC4 | A clean export | [revit_export_and_class_mapping](../by_topic/revit_export_and_class_mapping.md) |
| 4 | Properties lost on export, custom parameters to Psets, FireRating, units that are wrong in a valid file | Properties that survive | [properties_and_parameters](../by_topic/properties_and_parameters.md) |
| 5 | Coordinates, origin, georeferencing of IfcSite; models that do not overlap ("fuori di km") | Align disciplines | [coordinates_georef_units_levels](../by_topic/coordinates_georef_units_levels.md) |
| 6 | Editing a received IFC: proxies, read-only viewers, GUID changes after bulk edits | Change data without breaking GUIDs | [versions_mvd_encoding_guid](../by_topic/versions_mvd_encoding_guid.md) |
| 7 | Information checks (*verifica informativa*): required properties, classification coverage, IDS | Pass or fail lists | [validation_ids_model_checking](../by_topic/validation_ids_model_checking.md) |
| 8 | Comparing IFC revisions and exchanging issues with BCF | What changed | [coordination_clash_bcf_cde](../by_topic/coordination_clash_bcf_cde.md) |
| 9 | Conversions: DWG to IFC, IFC to DXF, IFC to IFC 2x3 for subcontractors | Convert | [file_size_viewing_conversion](../by_topic/file_size_viewing_conversion.md) |
| 10 | IFC 4.3 and infrastructure (roads, rail, viaducts) | Support in software | [infrastructure_site_gis_energy](../by_topic/infrastructure_site_gis_energy.md) |
| 11 | Fees and incentives linked to BIM (10% fee increase, 15% incentives), ACDat/CDE for contracting authorities | Money and platforms | [regulations_permits_contracts](../by_topic/regulations_permits_contracts.md) |

## Local ecosystem

Full detail with unverified flags: [spain_portugal_italy.md](../../02_standards_regulations/national/spain_portugal_italy.md) (Italy section).

- **Law**: D.Lgs. 36/2023 (Codice dei contratti pubblici), Art. 43 and Allegato I.9 (CDE, capitolato informativo, offerta and piano di gestione informativa; UNI EN ISO 19650 named; UNI 11337 as a reference, not mandatory). Corrective decree D.Lgs. 209/2024. The older DM 560/2017 ("decreto BIM") is superseded for new procedures (how transitional rules apply: unverified). **The law text read does not name IFC**; it requires open non-proprietary formats; IFC (ISO 16739) appears as the reference in explainers and the capitolato informativo of each client.
- **Institutions** cited in the articles: MIT (Ministero delle Infrastrutture e dei Trasporti; "Linee guida GID 2026", opinions 3416/2025, 3368/2025, 2877/2024), ANAC (opinion 37; bando tipo 2/2026), a Consiglio di Stato ruling 6834/2026 on the oGI. These come from vendor/trade articles; verify before relying on numbers.
- **Standards**: UNI 11337 series (LOD A-G with LOG geometry and LOI information), UNI EN ISO 19650, ISO 16739.
- **buildingSMART Italia**, run by IBIMI: IFC guides for structures (2024), roads (2022), bridges and viaducts (2020), capitolati informativi (2019, 2025), openBIM for airports and others.
- **Vendors**: ACCA software (BibLus, Edificius, EdiLus, usBIM platform with usBIM.viewer+, usBIM.checker, usBIM.revolution plugin for Revit), Autodesk Revit, Graphisoft Archicad, Tekla, ZWCAD, Harpaceas **(GK)**, DDS-CAD and SCIA appear in synthetic prompts.
- **Coordinate systems**: synthetic prompts cite EPSG:7791 and EPSG:3003 (the latter is Monte Mario / Italy zone 1 **(GK)**); the IFC coordinate-system article lists WGS84, ED50, Roma40 and EPSG references.
- **Italian Excel gotcha**: CSV exported with a dot as decimal separator turns into text in an Italian-locale Excel (comma decimal, semicolon delimiter). A test case: `it-data-s016`.

## How people write

**No real Italian forum posts were collected.** The notes below combine the report's observations from titles and headings, the synthetic prompts **(syn)**, and general knowledge **(GK)**.

### Register, length, structure

- **Two registers coexist.** (1) *Procedural / institutional* (from articles): question-form titles ("da quando è obbligatorio...", "serve per forza l'IFC?"), heavy vocabulary (*soglia, stazione appaltante, DOCFAP, ACDat, RTI, RUP*). (2) *Terse work orders to the tool* **(syn)**: "quanti IfcBuildingElementProxy ci sono nel modello?", "dimmi quali porte non hanno il FireRating nel Pset_DoorCommon", "confronta rev A e rev B".
- **Questions, not imperatives, are common** in Italian: "ci sono elementi non contenuti in nessun piano?", "terminali impianto non collegati a nessun sistema?" (fragment with a question mark, no verb).
- **Imperatives when asking for output**: *dammi, dimmi, elencami, lista, trova, controlla, verifica, confronta, converti, assegna, mi serve*.
- **Purpose clause**: "per il verbale di consegna", "mi servono per il computo oggi", "è per la tesi", "per la gara".
- **Fragments from articles**: "IFC VS RVT: quali sono le principali differenze", "IFC class mapping file", "Come creare un file IFC".
- **Accents.** The reconstructed questions in the data write "e" for "è" ("e obbligatoria", "cosa e cambiato", "il modello o il viewer?"). This may be the research agent's ASCII normalisation; informal Italian typing does often drop or replace the accent (with "e'" as a common variant) **(GK)**. Both forms are plausible; do not use only one.
- **Tone**: mostly neutral or polite; frustration around exports ("perché?", "sballato"); legal worry in procurement questions ("vengo escluso?").

### Jargon and slang

| Term | Meaning | Standard / IFC term | Evidence |
|---|---|---|---|
| capitolato informativo (CI) | client's information requirements | EIR | article titles, national doc |
| offerta di gestione informativa (oGI) | bidder's pre-contract BIM plan | pre-appointment BEP | articles |
| piano di gestione informativa (pGI) | post-award BIM execution plan | BEP | articles |
| ACDat (ambiente di condivisione dati) | common data environment | CDE | articles |
| stazione appaltante | contracting authority | appointing party | articles |
| DOCFAP, RUP, RTI | feasibility-alternatives document, procedure manager, temporary consortium | procurement terms | report, articles |
| gara, bando, appalto | tender, notice, contract | procurement | articles, syn |
| verifica informativa | information check against requirements | validation | articles |
| computo (metrico) | quantity takeoff for cost | Qto | syn |
| piano | storey (also "livello") | IfcBuildingStorey | syn |
| quota | elevation | Elevation | syn |
| locali, ambienti, stanze | rooms | IfcSpace | syn |
| muri, solai, pilastri, travi, parapetti, forature | walls, slabs, columns, beams, railings, openings | IfcWall, IfcSlab, IfcColumn, IfcBeam, IfcRailing, openings | syn |
| impianti, terminali | MEP systems, terminals | IfcDistributionElement | syn |
| proxy | element exported as placeholder | IfcBuildingElementProxy | articles, syn |
| Pset, viewer, export, round-tripping, class mapping, workflow, clash detection | English terms used as-is | | articles |
| sballato / sballata | "off", "wrong" (informal) | | syn ("l'origine è sballata", "i colori sono sballati") |
| fuori di km | "kilometres away" (models not overlapping) | | article summary |
| rev A / rev B, v1 / v2 | revisions | revision | syn |
| MIT, ANAC | ministry, anti-corruption authority | | articles |
| template | requirements template used for a check | | articles |
| tesi | thesis (student context) | | syn |

### Misspellings, name variants, code-switching

- English technical vocabulary is kept: *export, class mapping, Pset, viewer, proxy, clash detection, workflow, GlobalId, GUID, FireRating, LoadBearing, IsExternal*. Italian prompts typically name the property (FireRating, IsExternal) but call the group by its English name.
- Program names without version and sometimes without capitals: "da Revit esporto IFC", "bonsai", "usBIM".
- Italianised forms: *il Pset, i proxy, georeferenziare, rigenerare i GUID*.
- Software-driven titles in the articles: "Conversione modello BIM in IFC5" (this title says IFC5 although the content is about the Revit export; do not take it as a statement that IFC5 exists in the way the title suggests).

### What context is given or omitted

Given **(syn)**: the program ("da Archicad", "Revit"), the schema when relevant, the tender context ("per la gara"). Omitted: file name, exporter version, the exact capitolato text. In the articles, context such as "IFC ricevuto da un altro studio" or "modelli multidisciplinari" frames the question.

## Real questions

All 28 are **C-level**: published articles, with the question rephrased by the research agent. Where the article is about a regulation, the "persona" is the likely reader. Do not quote these as user posts.

| ID | Reconstructed question (Italian) | English gloss | Persona | Evidence | Source |
|---|---|---|---|---|---|
| it-italy-r001 | ho un IFC ricevuto dal collega, devo modificare le proprieta ma il viewer e solo lettura e i muri sono finiti come proxy, come faccio senza rompere i GUID? | Editing a received IFC: read-only viewer, walls as proxies, how not to break GUIDs. Answer: IFC is an exchange format; use IFC editors; fix export upstream; report with BCF; avoid bulk edits that change GUIDs. | bim_coordinator, 2025 | C, page | [BibLus](https://biblus.acca.it/problemi-editing-file-ifc/) |
| it-italy-r002 | cosa si perde esportando da Revit in IFC? le famiglie e le relazioni vengono mappate bene? | What is lost exporting Revit to IFC; are families and relations mapped well? (Article promotes the usBIM.revolution plugin.) | bim_manager, 2024 | C, page | [BibLus](https://biblus.acca.it/ifc-vs-rvt-quali-sono-le-principali-differenze-tra-revit-e-ifc-in-termini-di-interoperabilita-e-scambio-dati/) |
| it-italy-r003 | come carico il file di mappatura classi IFC in Revit prima di aprire l'IFC cosi le porte restano porte? | How to load an IFC class-mapping file in Revit before opening so doors stay doors; Archicad uses translators. | architect, 2023 | C, page | [BibLus](https://biblus.acca.it/ifc-class-mapping-file/) |
| it-italy-r004 | da quando e obbligatorio il BIM negli appalti e sopra che soglia? serve per forza l'IFC? | When is BIM mandatory in tenders and above what threshold; is IFC required? Answer: above EUR 2 M from 1 Jan 2025; open non-proprietary formats; IFC (ISO 16739) as reference. | reviewer_authority, 2026 | C, page | [BibLus](https://biblus.acca.it/nuovo-codice-appalti-il-bim-e-obbligatorio/) |
| it-italy-r005 | i modelli IFC non si sovrappongono, uno e fuori di km, dove imposto origine e coordinate del sito prima di esportare? | Models do not overlap, one is kilometres off; where to set origin and site coordinates before export? | bim_coordinator, 2023 | C, page | [BibLus](https://biblus.acca.it/ifc-coordinate-system/) |
| it-italy-r006 | devo scrivere il capitolato informativo per una gara, cosa metto su formati e livelli di dettaglio? | I must write the capitolato informativo; what do I put on formats and levels of detail? | owner_client, 2026 | C, page | [BibLus](https://biblus.acca.it/capitolato-informativo-come-redigerlo-con-la-metodologia-bim/) |
| it-italy-r007 | come si esporta un IFC? meglio 2x3 o IFC4? | How to export an IFC; 2x3 or IFC4? (beginner) | student_beginner, 2025 | C, page | [BibLus](https://biblus.acca.it/come-creare-un-file-ifc/) |
| it-italy-r008 | come verifico che porte e muri abbiano FireRating e trasmittanza prima di consegnare l'IFC? | How to check that doors and walls have FireRating and thermal transmittance before delivery. | bim_manager, 2021 | C, page | [BibLus](https://biblus.acca.it/bim-validation-modelli-ifc/) |
| it-italy-r009 | ho due revisioni dello stesso IFC, come vedo cosa e cambiato (aggiunti, rimossi, modificati)? | Two revisions of the same IFC: how to see what changed. | bim_coordinator, 2025 | C, page | [BibLus](https://biblus.acca.it/rilevare-modifiche-nei-modelli-ifc/) |
| it-italy-r010 | cosa dicono le linee guida MIT 2026 su ACDat, ruoli e formato IFC? il modello prevale sul 2D? | What do the 2026 MIT guidelines say about ACDat, roles, IFC; does the model prevail over 2D? | reviewer_authority, 2026 | C, page | [BibLus](https://biblus.acca.it/linee-guida-bim-2026-per-le-stazioni-appaltanti/) |
| it-italy-r011 | esporto da Revit ma i parametri custom non finiscono nei Pset, come li mappo? | Custom parameters do not reach the Psets on Revit export; how to map? | bim_coordinator, 2026 | C, page | [BibLus](https://biblus.acca.it/conversione-modello-bim-in-ifc5/) |
| it-italy-r012 | dove trovo il FireRating di un muro in un IFC e come lo modifico? | Where is the wall FireRating in an IFC and how to edit it (Pset_WallCommon)? | student_beginner, 2026 | C, snippet | [Ingenio](https://www.ingenio-web.it/articoli/proprieta-ifc-muro-firerating-pset-wallcommon/) |
| it-italy-r013 | dove sono dichiarate le unita nell'IFC? il file valido ma le misure sono sballate | Where are units declared; the file is valid but measures are wrong. | developer_programmer, 2026 | C, snippet | [Ingenio](https://www.ingenio-web.it/articoli/ifc-in-pratica-unita-di-misura-dove-trovarle-e-come-leggerle/) |
| it-italy-r014 | col Piano Casa 2026 l'obbligo BIM cambia o resta art. 43? | Does Piano Casa 2026 change the BIM obligation or does art. 43 remain? | architect, 2026 | C, snippet | [Ingenio](https://www.ingenio-web.it/articoli/piano-casa-2026-edilizia-convenzionata-appalti-bim/) |
| it-italy-r015 | ha senso il BIM solo 3D? servono requisiti IDS? | Does 3D-only BIM make sense; are IDS requirements needed? (opinion essay) | bim_manager, 2026 | C, snippet | [Ingenio](https://www.ingenio-web.it/articoli/bim-oltre-3d-visione-sistemica-costruito/) |
| it-italy-r016 | IFC 4.3 cosa cambia per strade e ferrovie? i software lo supportano? | What does IFC 4.3 change for roads and rail; do programs support it? | civil_infra_engineer, 2026 | C, snippet | [BibLus](https://biblus.acca.it/ifc-4-3-approvato-come-standard-finale/) |
| it-italy-r017 | cos'e la Coordination View 2.0 e quando usarla? | What is Coordination View 2.0 and when to use it? | architect, 2023 | C, snippet | [BibLus](https://biblus.acca.it/ifc-2x3-coordination-view-2-0/) |
| it-italy-r018 | in gara serve per forza l'oGI? se non la presento vengo escluso? | Is the oGI mandatory in a tender; will I be excluded without it? (legal worry; court ruling discussed) | contractor_site, 2026 | C, snippet | [BibLus](https://biblus.acca.it/notizie/appalti-bim-lofferta-di-gestione-informativa-e-obbligatoria/) |
| it-italy-r019 | la maggiorazione del 10% per il BIM vale anche per DL e CSE? | Does the 10% BIM fee increase apply to site management and safety coordination? | estimator_qs, 2026 | C, snippet | [BibLus](https://biblus.acca.it/notizie/bim-maggiorazione-del-10-anche-per-direzione-lavori-e-cse/) |
| it-italy-r020 | nei raggruppamenti il requisito BIM lo deve avere il singolo o il gruppo? | In groupings (RTI), must the individual or the group meet the BIM requirement? | reviewer_authority, 2026 | C, snippet | [BibLus](https://biblus.acca.it/notizie/requisiti-bim-negli-rti-conta-il-professionista-o-il-gruppo-di-lavoro/) |
| it-italy-r021 | per completare un'opera incompiuta serve il BIM? | Is BIM needed to complete an unfinished work? (If remaining works exceed EUR 2 M.) | owner_client, 2025 | C, snippet | [BibLus](https://biblus.acca.it/notizie/c-e-l-obbligo-di-appalto-bim-anche-per-completare-un-opera-incompiuta/) |
| it-italy-r022 | ho solo il DWG, come lo converto in IFC? | I only have the DWG; how do I convert to IFC? (Limited semantics.) | architect, 2023 | C, snippet | [BibLus](https://biblus.acca.it/come-convertire-un-file-dwg-in-ifc-in-modo-semplice/) |
| it-italy-r023 | dall'IFC come estraggo piante e sezioni in DXF? | How to extract plans and sections as DXF from an IFC. | architect, 2026 | C, snippet | [BibLus](https://biblus.acca.it/una-guida-completa-per-convertire-file-ifc-in-dxf/) |
| it-italy-r024 | come uso i BCF per segnalare errori nell'IFC all'autore? | How to use BCF to report errors in the IFC to its author. | bim_coordinator, 2026 | C, snippet | [BibLus](https://biblus.acca.it/markups-bcf-workflow-openbim/) |
| it-italy-r025 | che differenza c'e tra BIM e IFC? | What is the difference between BIM and IFC? (beginner) | student_beginner, 2025 | C, snippet | [BibLus](https://biblus.acca.it/legame-bim-ifc/) |
| it-italy-r026 | come e strutturato un file IFC, IfcObjectDefinition e relazioni? | How an IFC file is structured: IfcObjectDefinition and relationships. | developer_programmer, 2023 | C, snippet | [BibLus](https://biblus.acca.it/architettura-file-ifc-ifcobjectdefinition/) |
| it-italy-r027 | con che tool verifico i requisiti informativi del modello IFC? | Which tool checks the information requirements of the IFC model? (usBIM.checker) | bim_manager, 2021 | C, snippet | [BibLus](https://biblus.acca.it/usbim-checker-verifica-informativa-del-modello/) |
| it-italy-r028 | il decreto BIM 560/2017 impone IFC o formati aperti? | Does the 2017 BIM decree impose IFC or open formats? Answer: interoperable open formats; phased deadlines. | bim_manager, 2017 | C, snippet | [BibLus](https://biblus.acca.it/obbligo-di-adozione-del-bim-capitolati-informativi-e-formati-di-interscambio-le-prime-osservazioni-ad-decreto-bim/) |

## Ready test prompts

All **synthetic**. Items 1-39 are rewritten or lightly edited from the research agents' prompts (Src = record id). Items 40-43 are **adapted** from the reconstructed questions of the real articles by the author of this page, to cover regulation and conversion cases. Typing style varies on purpose (with and without accents).

| # | Prompt (synthetic) | Intent, difficulty, persona | Src | Expected behavior |
|---|---|---|---|---|
| 1 | quanti IfcBuildingElementProxy ci sono nel modello? da che categorie Revit arrivano? | query_model_data, medium, bim_coordinator, file | it-italy-s001 | Count proxies, group by ObjectType / Revit category, suggest class-mapping fixes. |
| 2 | dimmi quali porte non hanno il FireRating nel Pset_DoorCommon | validate_check, easy, architect, file | it-italy-s002 | List doors lacking the property with id, name, level. Distinguish missing vs empty. |
| 3 | i modelli non si sovrappongono. controlla IfcSite lat/long/quota e il CRS e dimmi se l'origine è sballata | validate_check, hard, bim_coordinator, file | it-italy-s003 | Read site latitude, longitude, elevation, map conversion and CRS, placement offsets; report anomalies. |
| 4 | confronta rev A e rev B, cosa è stato aggiunto/rimosso/modificato per GUID? | compare_versions, hard, bim_coordinator, files | it-italy-s004 | Diff by GlobalId; added, removed, changed attributes and properties; summary by class. |
| 5 | ci sono elementi non contenuti in nessun piano (IfcBuildingStorey)? | validate_check, medium, bim_manager, file | it-italy-s005 | Find elements without storey containment, list them. |
| 6 | dammi l'area dei muri esterni per piano, da Qto | extract_quantities, medium, estimator_qs, file | it-italy-s006, it-coord-s015 | Sum net side area for external walls per storey; if Qto missing, say so or compute from geometry and state the method. |
| 7 | verifica se il modello rispetta il capitolato informativo: classificazione, materiali, FireRating su tutti i muri | validate_check, hard, reviewer_authority, file | it-italy-s007 | Needs the requirement list; check classification, material, FireRating on walls and report non-conformances. Do not invent the capitolato content. |
| 8 | in che unità è il file? mm o metri? cosa dice IfcUnitAssignment | query_model_data, easy, bim_coordinator, file | it-italy-s008 | Report unit assignment for length, area, volume; warn of mismatches. |
| 9 | i proxy con nome 'Pilastro' mettili come IfcColumn | modify_model_data, hard, bim_coordinator, file | it-italy-s009 | Reclassify matching proxies, report count, keep GlobalIds where possible; confirm first. |
| 10 | da Revit esporto IFC ma i miei parametri condivisi non ci sono nei Pset, perche? | troubleshoot_export, medium, architect | it-italy-s010 | Explain the user-defined property set file, export schedules as Psets, shared-parameter requirements. |
| 11 | per la gara cosa esporto, 2x3 CV2.0 o IFC4 RV? | how_to, easy, architect | it-italy-s011 | Explain Coordination View 2.0 vs Reference View, tell the user to check the capitolato informativo, tool support. Do not say the law fixes one. |
| 12 | elenco materiali usati dai muri con relativa quantità | query_model_data, medium, developer_programmer, file | it-italy-s012 | List materials and layer sets linked to walls with counts. |
| 13 | riassumimi il modello: discipline, n. elementi per classe, livelli, per il verbale di consegna | comply_regulation, medium, owner_client, file | it-italy-s013 | Inventory by class, storey, discipline, schema version. |
| 14 | lista locali con superficie e nome, quelli senza nome segnali | query_model_data, easy, facility_manager, file | it-italy-s014 | List spaces with name and area; flag spaces without a name. |
| 15 | terminali impianto non collegati a nessun sistema? | query_model_data, hard, mep_engineer, file | it-italy-s015 | Find MEP terminals lacking system membership. |
| 16 | nel viewer i colori sono sballati e c'è z-fighting, è il modello o il viewer? | troubleshoot_viewing, medium, bim_coordinator, file | it-italy-s016 | Check styled items and materials, duplicate overlapping geometry; explain viewer artifacts. |
| 17 | volume solai per piano, mi servono per il computo oggi | extract_quantities, medium, contractor_site, file | it-italy-s017 | Sum slab volume per storey from quantity sets or geometry, state the source. |
| 18 | quanti elementi hanno una classificazione (Uniclass, UniFormat)? elenca quelli senza | validate_check, medium, bim_manager, file | it-italy-s018 | Coverage of classification references by class. |
| 19 | mi serve il computo metrico dai muri e solai per piano, con m2 e m3, e dimmi se ci sono elementi senza quantità | extract_quantities, medium, estimator_qs, file | it-s015 | Aggregate by storey; list elements without quantities. |
| 20 | elencami le aree di tutti gli ambienti del modello IFC, serve per la tesi | extract_quantities, easy, student_beginner, file | p-student-s019 | List spaces with net floor area; flag missing quantities; explain terms simply. |
| 21 | controlla che tutti i topic del BCF puntino a GlobalId che esistono nel modello IFC caricato, elenca quelli orfani | validate_check, medium, bim_coordinator, files | it-clash-s016 | Parse BCF, compare ids with model GlobalIds, report orphaned topics. |
| 22 | converti i codici da uniclass a omniclass usando la tabella excel e riscrivi le reference | convert_format, hard, bim_coordinator, file | it-classbsdd-s017 | Read the mapping table, create the target classification, replace references, report unmapped. Needs the table. |
| 23 | assegna la classificazione Uniclass a tutte le apparecchiature in base a questa tabella e dimmi quelle senza match | modify_model_data, hard, bim_manager, file | it-cobie-s016 | Apply references through the mapping; report unmatched elements. |
| 24 | controlla se l'ifc è georeferenziato in EPSG:7791 e se la rotazione rispetto al nord è coerente con l'IfcSite | validate_check, hard, bim_coordinator, file | mul-coord-s017 | Read CRS and map conversion, compare rotation with true north and site data, report inconsistencies. |
| 25 | quando esporto in csv i decimali con il punto diventano testo in excel italiano, come lo sistemo? | troubleshoot_export, easy, bim_coordinator | it-data-s016 | Explain locale mismatch; use comma decimal and semicolon delimiter, or import with Power Query and set column type. |
| 26 | dimmi quali elementi non hanno geometria, il viewer dice 'unexpected mesh type' | validate_check, medium, bim_coordinator, file | it-err-s013 | List products without a representation and those with unsupported items. |
| 27 | trova gli elementi con più di 50000 triangoli, secondo me sono quelli che appesantiscono il file | validate_check, hard, bim_manager, file | it-fs-s015 | Inspect representations, list elements above the threshold with class, name, triangle count. |
| 28 | nel modello IFC mancano i parapetti delle scale, controlli quali IfcStair non hanno IfcRailing? | troubleshoot_viewing, medium, architect, file | it-geom-s015 | Find stairs without associated railings and report. |
| 29 | come georeferenzio un ifc cosi lo vedo in qgis al posto giusto? uso bonsai, EPSG 3003 | how_to, easy, civil_infra_engineer | it-gis-s018 | Explain projected CRS and map conversion in Bonsai, units, and verifying in QGIS. |
| 30 | abbiamo copiato il file e ora ci sono GlobalId doppi tra i due modelli, puoi rigenerarli solo per il secondo? | modify_model_data, medium, bim_coordinator, files | it-guid-s014 | Find shared ids, generate new ones for the second file only, report the mapping, warn about broken external references. |
| 31 | confronta le due versioni del viadotto e dimmi quali elementi sono cambiati o spostati | compare_versions, medium, structural_engineer, files (IFC4.3) | it-infra-s016 | Diff by GlobalId, report added, removed, modified, placement changes. |
| 32 | ci sono materiali duplicati con lo stesso nome nel modello, uniscili e tieni lo stile colore | modify_model_data, hard, architect, file | mx-mcl-s010 | Find duplicate material names, merge preserving surface styles, report merged count. |
| 33 | controlla se le porte dei raccordi hanno FlowDirection SOURCE/SINK coerente con il flusso, export DDS-CAD | validate_check, hard, mep_engineer, file | it-mep-s014 | Read port flow directions and connections, flag SOURCE-SOURCE or SINK-SINK pairs. |
| 34 | controlla che muri e solai abbiano Pset_Common con IsExternal e LoadBearing, elenca quelli senza | validate_check, medium, bim_manager, file | it-permit-s016 | Check Psets on walls and slabs, list missing. |
| 35 | confronta i due IFC (v1 e v2) e dimmi quanti proxy abbiamo ancora e quali sono stati riclassificati | compare_versions, hard, bim_coordinator, files | it-proxy-s010 | Diff classes by GlobalId between files; proxies resolved vs remaining. |
| 36 | confronta le due revisioni IFC da Tekla: quali travi sono nuove, spostate o cancellate? uso i GlobalId | compare_versions, hard, structural_engineer, files | it-roundtrip-s016 | Match by GlobalId, report added, removed, moved members. |
| 37 | controlla se nel modello analitico ci sono vincoli e carichi assegnati, altrimenti SCIA non lo calcola | validate_check, medium, structural_engineer, file | it-struct-s017 | Check the structural analysis model for boundary conditions and load groups; report missing. |
| 38 | ho esportato in ifc4 da archicad ma revit non lo apre, solo collegato. perche? | troubleshoot_import, medium, architect, file | it-vm-s014 | Check schema and tessellated or polygonal face sets; explain Open vs Link limits; suggest IFC2x3 or faceted brep. |
| 39 | mi serve un file leggero da dare a navisworks, solo strutture e architettonico | convert_format, medium, bim_manager, file | it-viewconv-s015 | Filter disciplines, save a reduced file, report counts and size. |
| 40 | da quando è obbligatorio il BIM negli appalti e sopra che soglia? serve per forza l'IFC? | comply_regulation, easy, reviewer_authority | adapted from it-italy-r004 | State what the sources say: above EUR 2 M from 1 Jan 2025 under art. 43 D.Lgs. 36/2023; open non-proprietary formats; IFC not named in the law text read, set in the capitolato informativo. Recommend checking the current Normattiva text; do not cite court rulings or opinion numbers from memory. |
| 41 | per la gara mi chiedono l'offerta di gestione informativa, cosa deve contenere e se non la presento vengo escluso? | comply_regulation, hard, contractor_site | adapted from it-italy-r018 | Explain oGI vs pGI at concept level; say exclusion depends on the tender documents and current case law; no invented rulings. |
| 42 | ho solo il DWG, come lo converto in IFC? | convert_format, easy, architect | adapted from it-italy-r022 | Explain that a DWG converted to IFC has little BIM meaning (geometry without classes or properties); options and limits. |
| 43 | dall'IFC come estraggo piante e sezioni in DXF? | convert_format, medium, architect | adapted from it-italy-r023 | Explain that 2D drawings must be generated from the 3D model; state what the connected tools can do; do not claim DXF was produced if it cannot be. |

## Tips for generating authentic Italian prompts

**Do**
- Use the tender vocabulary where the persona fits (*capitolato informativo, stazione appaltante, oGI/pGI, ACDat, gara, RTI, verifica informativa*), and the site vocabulary for contractors and estimators (*computo, solai, pilastri, piano, quota*).
- Write short, lowercase, often as a question: "ci sono elementi non contenuti in nessun piano?", "terminali impianto non collegati a nessun sistema?".
- Mix English technical words freely: Pset, proxy, viewer, export, clash, GUID, FireRating.
- Add the purpose: "per il verbale di consegna", "per la gara", "per il computo oggi", "per la tesi".
- Vary accents: some prompts with "è" and "perché", some with "e" and "perche".
- Use informal words for "wrong": *sballato*, *fuori di km*.
- Include Italian-locale details: comma decimals, semicolon CSV, "mm o metri?".
- Add legal-worry cases ("vengo escluso?") but make the expected behavior cautious: no invented rulings, no exact article numbers except those in the KB, no claim that the law names IFC.

**Don't**
- Don't turn the vendor blog framing into the user's voice: real users do not say "scopri come usBIM.revolution risolve...".
- Don't state UNI 11337 as mandatory (the national doc says Allegato I.9 treats it as a reference), don't give old DM 560/2017 deadlines as current law.
- Don't make every Italian prompt formal; the corpus has no real forum post, but the synthetic work-order style and the question fragments are the only observable patterns.
- Don't claim these prompts are real quotes.
- Don't use "IFC5" loosely: one article is titled "Conversione modello BIM in IFC5" but the content is a Revit-to-IFC export guide.

## Gaps and next steps

- No real forum posts. A research pass with working search should cover the Autodesk Italia forum, edilportale, BIMportale, ACCA's forum, Reddit, Telegram and Facebook groups, YouTube comments and GitHub issues in Italian.
- Many regulatory facts (MIT guideline dates, ANAC opinions, court ruling numbers) come from vendor articles read through snippets; confirm them on Normattiva, MIT, ANAC before using them to judge an assistant's answer.

## Related KB documents

- [Spain, Portugal, Italy: BIM/IFC requirements](../../02_standards_regulations/national/spain_portugal_italy.md)
- [Revit IFC export reference](../../03_software/revit/ifc_export_reference.md), [Multilingual glossary](../../08_glossary/glossary_multilingual.md) (note: the glossary has no Italian column; Italian terms are in the national doc's terminology table)
- [Viewers, checkers, CDE, converters](../../03_software/viewers_checkers_cde_converters.md) (usBIM tools are listed as unverified)
- Other languages: [es](es.md), [pt](pt.md), [fr](fr.md)
