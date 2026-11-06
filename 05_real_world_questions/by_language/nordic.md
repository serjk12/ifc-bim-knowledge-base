# Nordic languages: how people ask about IFC, BIM and Revit

Language codes `no` (Norwegian), `da` (Danish), `sv` (Swedish), `fi` (Finnish). Built from research wave 1 (collected 2026-11-06).

**Read this first: this file is short and honest on purpose.**
The knowledge base holds 31 Nordic-language records: Norwegian 30 (13 real, 17 synthetic), Danish 1 (real), Swedish 0, Finnish 0 (`kb.py stats --lang no|da|sv|fi`). The web-search budget ran out before the first query, so no forum, Facebook group or Q&A site was reached. Consequences:

- **The 13 "real" Norwegian records are official or industry documents** (buildingSMART Norge, MMI-veilederen, Nye Veier, BIMpraten). Their "question" text is a plausible asker phrasing derived from the page, **not a quote from a person**.
- Only about five records anywhere in the data are texts written by actual practitioners with Nordic context: one Danish GitHub issue about `æ` showing up as `\X\E6`, three Norwegian-titled GitHub issues, and one Swedish-coordinate-system bug (written in English).
- **Swedish and Finnish have no real data at all.** Everything said about them comes from the [national doc](../../02_standards_regulations/national/nordics_baltics.md), which itself marks most facts "unverified".
- The synthetic Norwegian prompts are an informed guess at style. The Danish, Swedish and Finnish prompts below are new, written by the editor from national-doc vocabulary; they have no real-data backing for their phrasing.

Related docs: [Nordic and Baltic BIM/IFC requirements](../../02_standards_regulations/national/nordics_baltics.md); [versions, MVD, encoding](../by_topic/versions_mvd_encoding_guid.md); [infrastructure, site, GIS](../by_topic/infrastructure_site_gis_energy.md); [validation, IDS, checking](../by_topic/validation_ids_model_checking.md); [regulations, permits, contracts](../by_topic/regulations_permits_contracts.md); [IFC basics: what is IFC and versions](../../01_ifc_basics/01_what_is_ifc_and_versions.md); [multilingual glossary](../../08_glossary/glossary_multilingual.md).

## Where people ask

| Place | Language | Kind | What we saw | Access note |
|---|---|---|---|---|
| [buildingSMART Norge](https://www.buildingsmart.no/) incl. [POFIN](https://www.buildingsmart.no/pofin.html), [Kort forklart](https://www.buildingsmart.no/standarder/kort-forklart.html), [publications](https://www.buildingsmart.no/standarder/publikasjoner-og-veiledninger.html), [infrastructure domain](https://www.buildingsmart.no/fagnettverk/infradomene.html) | Norwegian | Official chapter site; working groups (Armering, VA, Høyspent); Faglig Onsdag | 7 pages read | Open |
| [MMI-veilederen](https://www.mmi-veilederen.no/) | Norwegian | Joint guide by Statsbygg, Nye Veier, Bane NOR, Statens vegvesen and industry bodies | 1 page | Open |
| [BIMpraten](https://www.bimpraten.no/) podcast (Standard Norge and buildingSMART Norge) | Norwegian | Podcast site | 1 page | Open |
| [Nye Veier: for leverandørene](https://www.nyeveier.no/for-leverandoerene/) | Norwegian | Supplier page; BIM/IFC rules are not on it (they sit in tender documents on Doffin/Artifik) | 1 page | Open |
| GitHub: [Ed-Skiplum/ifc-check](https://github.com/Ed-Skiplum/ifc-check/issues/15), [DanGjer/CableTrayHandler](https://github.com/DanGjer/CableTrayHandler/issues/1), [DanGjer/InfoNodeHandler](https://github.com/DanGjer/InfoNodeHandler/issues/8) | Norwegian titles, English tool names | Small personal repos (Revit tools, dRofus, model reception control) | 3 issue titles only; bodies not read | Open |
| GitHub: [ThatOpen web-ifc #358](https://github.com/ThatOpen/engine_web-ifc/issues/358), [Autodesk revit-ifc #818](https://github.com/Autodesk/revit-ifc/issues/818) | Danish context (English text); Swedish CRS in English | Library and exporter trackers | 1 each | Open |
| dRofus support article ["Optimal settings for Ifc Export from Revit"](https://support.drofus.com/en/support/solutions/articles/16000118323-optimal-settings-for-ifc-export-from-revit) | English | Vendor knowledge base | Recommends a 3D view, IFC2x3 Coordination View, rooms as spaces | Open |
| Facebook groups (e.g. BIM Norge), Reddit, Norwegian Revit user forums, Byggeindustrien/Bygg.no, ByggSøk, Statens vegvesen håndbøker (V770), Statsbygg BIM manual (page rendered only a heading), Bane NOR technical rules | Norwegian | Most likely real asking places | **Not reached** | Gap |
| Denmark (Molio, bips, buildingSMART Danmark: connection refused), Sweden (BIM Alliance, Praxi, Trafikverket: only the national doc read), Finland (buildingSMART Finland wiki: title only; Senate Properties) | da, sv, fi | Official bodies | **No questions found** | Gap |

## Top themes (ranked)

Ranked by evidence in the pages read. For Norway the ranking reflects what the official sites emphasise, so it shows what people are *told* to care about, not necessarily what they ask in chat.

| Rank | Theme | What people want | Evidence |
|---|---|---|---|
| 1 | National frameworks for requirements: POFIN 1.0, openBIM Harmony, ISO 19650 terms (EIR, BEP, LOIN, CDE) | Know what the client (bestiller) requires in a delivery and prove compliance | no-norway r002, r006 |
| 2 | MMI (model maturity index, "modenhetsindeks") coding of objects | Which MMI per milepæl; find objects missing MMI, by discipline | r007; prompt NO1 |
| 3 | IFC versions: IFC2x3, IFC4, IFC4.3 (infra), outlook IFC4.4/IFC5; Revit export settings and MVD the client accepts | Export that the client accepts | r001; prompt NO11 |
| 4 | Infrastructure in IFC 4.3: roads, rail, VA (water and wastewater: kum, rør) | Alignments visible, correct georeference (EUREF89 NTM), detailed VA models | r004, r013; prompts NO5, NO17 |
| 5 | Machine-checkable requirements: IDS, IFC Validation Service, Solibri-style rules, model reception control ("mottakskontroll") | Automatic check with list of failures by discipline | r011; Ed-Skiplum issue; prompts NO3 |
| 6 | NS 8360 property sets and status codes (Milestone, IsProcured, DuplicateOwnedBy) | Set and check procurement and maturity properties | r012; prompt NO15 |
| 7 | Rebar (armering) from open models to ordering and production | Digital ordering from IFC | r005 |
| 8 | BCF and openCDE, clash coordination | BCF from clashes over a tolerance | r011; prompt NO10 |
| 9 | Classification and bSDD (NS 3451 in practice, SN/K 518) | Codes on all components | r008; prompts NO6 |
| 10 | FDV (operation and maintenance) handover, room lists (BTA/NTA) | Lists for facility management | prompts NO6, NO13 |
| 11 | Encoding of æ, ø, å (Danish and Norwegian) | Names that read correctly after IFC STEP escapes | web-ifc #358; prompt NO12 |
| 12 | National coordinate systems: EUREF89 NTM (Norway), SWEREF 99 (Sweden) | Right EPSG code in the file | revit-ifc #818; prompts NO5, NX4 |

## Local ecosystem

Short; confidence marks are in the [national doc](../../02_standards_regulations/national/nordics_baltics.md), which says most Nordic items are unverified.

- **Norway:** no national BIM mandate; big public clients (Statsbygg, Statens vegvesen, Nye Veier, Bane NOR) set requirements. buildingSMART Norge publishes POFIN 1.0 (14 documents and 2 spreadsheets), openBIM Harmony, IFC for begynnere, VA-detaljmodeller 1.0 (IFC 4.3, with Oslo VAV), Armeringsveileder 2.0, and from 2026 maintains the MMI-veilederen 2.0. Standard Norge committees SN/K 257 (BIM), 285 (FDVU), 380 (BIM objects), 401 (NS 3420), 518 (classification); CEN TC442. NS 3451 is the usual building-element table (unverified); NS 8360 defines process properties. Tools: Revit, Archicad, Solibri, Civil 3D, Novapoint, StreamBIM, dRofus, IfcOpenShell.
- **Denmark (all unverified):** IKT-bekendtgørelsen (executive order on ICT in construction), bips content now hosted by Molio, buildingSMART Danmark is part of Molio, CCS (Cuneco Classification System).
- **Sweden:** BIM Alliance hosts buildingSMART Sweden; Praxi portal (ISO 19650, openBIM, CoClass, value lists); Trafikverket for infrastructure (details unverified); classification CoClass (replacing BSAB 96, unverified); CRS SWEREF 99.
- **Finland:** buildingSMART Finland and the RYTV programme; requirement series YTV (buildings), YIV (infrastructure), YKV; Inframodel exchange format for infrastructure; Senate Properties (Senaatti-kiinteistöt) as state client; COBIM 2012 is the English version of the older YTV; Solibri (Finnish origin) and MagiCAD (Finnish vendor) (unverified).
- **Baltic states and Iceland** are in the national doc and have no questions in the data.

## How people write

### Evidence status

| Language | What is observed | What is inferred |
|---|---|---|
| Norwegian | Official-site wording; three GitHub issue titles (Norwegian, mixed with English tool names) | Chat phrasing, from 17 synthetic prompts (all written by an AI agent) |
| Danish | One GitHub issue quoting `V\X\E6gelement` | Everything else |
| Swedish | One issue naming "SWEREF 99 18 00" | Everything else |
| Finnish | Nothing | Everything |

### Norwegian (bokmål)

- **Register:** professional, short and practical; imperative or short question ("sjekk ...", "lag ...", "list opp ...", "kan du ..."). In the 17 synthetic prompts: 9 to 16 words, median 13; 16 of 17 start in lower case; no greeting; no "vennligst" or "takk"; 7 contain a question mark; mild frustration expressed with double question marks ("hvorfor er det så mange IfcBuildingElementProxy her??").
- **Openers (synthetic):** "sjekk hvilke ...", "hvorfor er ...", "kan du ...", "hva har ...", "har alle ...", "lag ...", "list opp ...", "trenger mengder: ...".
- **Code-switching:** very heavy. IFC, Pset, proxy, Solibri, Revit, BCF, clash, MVD, EIR stay in English; property names stay English inside Norwegian sentences (`IsProcured = true`, `Milestone`). Norwegian titles on GitHub mix both: "Mottakskontroll-typer on Eystein: scope config, Klar for Reduzer, quantities without Solibri".
- **Abbreviations as everyday vocabulary:** RIB, RIV, ARK (disciplines), FDV, BTA/NTA, TEK17, MMI, NS 3451, VA.
- **Context given:** the discipline pair ("RIV mot RIB"), a tolerance ("over 50 mm"), a threshold from a regulation (TEK17, 90 cm), the client role ("bestiller"). **Omitted:** file, version, Revit year, IFC schema.
- **Encoding:** `æøå` turning into odd characters is a stated concern (prompt NO12).

### Danish, Swedish, Finnish (very low confidence)

- **Danish** (one observed record): the reporter writes in English, states the country and the symptom, pastes a raw IFC line (`V\X\E6gelement`). `\X\E6` is the ISO 8859-1 escape for `æ`. Vocabulary from the national doc: byggherre (client), CCS, informationskrav, Molio.
- **Swedish** (one observed record): short English bug report that names the national CRS ("SWEREF 99 18 00", EPSG 3011) and shows that the exporter writes another EPSG code. Vocabulary from the national doc: BIM Alliance, Praxi, CoClass, Trafikverket, byggherre.
- **Finnish:** nothing observed. Vocabulary from the national doc: tietomalli / tietomallinnus (information model / BIM), YTV, YIV, Inframodel, Senaatti-kiinteistöt.

### Jargon and slang table

| Term | Language | Meaning | Standard term |
|---|---|---|---|
| MMI | no | model maturity index (e.g. MMI 300, 400) | process-status property per NS 8360 / MMI-veilederen |
| bestiller / leverandør | no | client / supplier | appointing / appointed party |
| byggherre | no, da, sv | client / owner | owner_client |
| RIB / RIV / ARK | no | structural / HVAC / architecture discipline | discipline models |
| FDV / FDVU | no | operation and maintenance documentation | FM handover |
| BTA / NTA | no | gross / net floor area | area quantities |
| TEK17 | no | Norwegian technical building regulation | permitting_code_checking |
| kum | no | manhole | VA model object |
| VA | no | water and wastewater | infrastructure domain |
| armering | no | reinforcement | `IfcReinforcingBar` |
| romliste | no | room list | `IfcSpace` export |
| etasje | no | storey | `IfcBuildingStorey` |
| mottakskontroll | no | model reception control | intake check |
| NS 3451 | no | table of building elements | classification |
| NS 8360 | no | process-information properties and status codes | custom psets |
| POFIN | no | national openBIM framework | requirements package |
| CCS | da | Cuneco Classification System | classification (unverified) |
| informationskrav | da | information requirements | EIR |
| CoClass | sv | Swedish classification system | classification (unverified) |
| SWEREF 99 | sv | Swedish CRS | EPSG:3006/3011 family |
| tietomalli | fi | information model, BIM | BIM model |
| YTV / YIV | fi | common BIM requirements for buildings / infrastructure | national requirement series (unverified) |
| Inframodel | fi | Finnish infrastructure exchange format | LandXML-based |

## Real questions

Be aware: rows from buildingSMART Norge, MMI-veilederen, Nye Veier and BIMpedia-like pages are **official documents**; the Norwegian phrasing in "Paraphrase" is the dataset's plausible asker wording and not a person's quote. Only sections B and C contain texts by practitioners, and those are titles or short bug reports.

### A. Norwegian: official and industry pages (13, `no`)

| # | Original title (verbatim) | Paraphrase in original language | Gist in English | Persona · type · year | Source |
|---|---|---|---|---|---|
| 1 | Kort forklart - IFC (buildingSMART Norge) | hvilke IFC-versjoner brukes i prosjekter nå, og hva er nytt i IFC4.3? | Which IFC versions are used in Norwegian projects and what does IFC4.3 add? | student_beginner · knowledge · 2026 | [buildingsmart.no](https://www.buildingsmart.no/standarder/kort-forklart.html) (official_doc) |
| 2 | POFIN - nasjonalt rammeverk for BIM | hva er POFIN og kan vi bruke det til å stille krav til informasjonsleveranser? | What is POFIN and can I use it to set openBIM requirements in a contract? | bim_manager · knowledge · 2025 | [buildingsmart.no](https://www.buildingsmart.no/pofin.html) (official_doc) |
| 3 | IFC for begynnere - og viderekomne | finnes det en veileder som forklarer IFC-struktur og vanlige problemer, til bruk ved kravsetting og kontroll av leveranser? | Guide to IFC for beginners and advanced users, aimed at writing requirements and checking deliveries | bim_coordinator · how_to · 2025 | [buildingsmart.no](https://www.buildingsmart.no/standarder/publikasjoner-og-veiledninger.html) (official_doc) |
| 4 | Retningslinjer for VA-detaljmodeller 1.0 | hvordan skal kummer, rør og rørdeler modelleres i IFC 4.3 for VA? | Guidelines for detailed VA (water and wastewater) models based on IFC 4.3, made with Oslo VAV | civil_infra_engineer · knowledge · 2025 | [buildingsmart.no](https://www.buildingsmart.no/standarder/publikasjoner-og-veiledninger.html) (official_doc) |
| 5 | Armeringsveileder 2.0 | hvordan går vi fra armeringsmodell til bestilling og produksjon med åpne standarder? | Reinforcement guide 2.0 on ordering and producing rebar digitally from open-standard models | structural_engineer · knowledge · 2025 | [buildingsmart.no](https://www.buildingsmart.no/standarder/publikasjoner-og-veiledninger.html) (official_doc) |
| 6 | openBIM Harmony | hva er openBIM Harmony og hvordan henger det sammen med POFIN? | openBIM Harmony: guidelines, templates and predefined info requirements based on ISO 19650 and CEN/TR 17654 | bim_manager · knowledge · 2025 | [buildingsmart.no](https://www.buildingsmart.no/standarder/publikasjoner-og-veiledninger.html) (official_doc) |
| 7 | MMI-veilederen 2.0 | hvilken MMI-kode skal objektene ha i modellen ved hver milepæl? | MMI-veilederen 2.0: model maturity index harmonised for building and infrastructure by Statsbygg, Nye Veier, Bane NOR, Statens vegvesen | owner_client · knowledge · 2026 | [mmi-veilederen.no](https://www.mmi-veilederen.no/) (official_doc) |
| 8 | Standardiseringsarbeid (buildingSMART Norge) | hvilke komiteer i Standard Norge styrer BIM-standarder og klassifisering? | Which Norwegian standardisation committees govern BIM and classification? | reviewer_authority · knowledge · 2026 | [buildingsmart.no](https://www.buildingsmart.no/standarder/standardiseringsarbeid.html) (official_doc) |
| 9 | For leverandorene (Nye Veier) | hvor finner jeg Nye Veiers krav til digitale leveranser? | Supplier page of Nye Veier: tenders via Doffin and Artifik, delivery through total contractors; no BIM/IFC rules stated | contractor_site · knowledge · 2026 | [nyeveier.no](https://www.nyeveier.no/for-leverandoerene/) (official_doc) |
| 10 | BIMpraten | finnes det norsk podcast om BIM og standarder? | BIMpraten podcast from Standard Norge and buildingSMART Norge | student_beginner · knowledge · 2026 | [bimpraten.no](https://www.bimpraten.no/) (official_doc) |
| 11 | Kort forklart - IDS, BCF, bSDD, openCDE | hva er forskjellen på IDS, BCF og bSDD? | Short Norwegian definitions of IDS, BCF, bSDD and openCDE | bim_coordinator · knowledge · 2026 | [buildingsmart.no](https://www.buildingsmart.no/standarder/kort-forklart.html) (official_doc) |
| 12 | Kort forklart - NS 8360 begreper | hvilke egenskaper krever NS 8360 i modellen, f.eks. Milestone og IsProcured? | NS 8360 concepts: LOD, custom property sets, process status codes, IsProcured, Milestone, DuplicateOwnedBy | bim_manager · knowledge · 2026 | [buildingsmart.no](https://www.buildingsmart.no/standarder/kort-forklart.html) (official_doc) |
| 13 | Infrastrukturdomene | finnes det et fagmiljo for IFC i veg og bane? | Infrastructure domain forum for roads, rail and VA at buildingSMART Norge | civil_infra_engineer · knowledge · 2026 | [buildingsmart.no](https://www.buildingsmart.no/fagnettverk/infradomene.html) (official_doc) |

### B. Texts by practitioners with Nordic context (6)

Danish (`da`), Norwegian-titled issues (tagged `en`), a Swedish CRS bug (tagged `en`), and a dRofus vendor article (dRofus is the tool named in two of the Norwegian issues). Titles are verbatim.

| # | Original title (verbatim) | Paraphrase in original language | Gist in English | Persona · type · year | Source |
|---|---|---|---|---|---|
| 1 | UTF-8 encoding |  | Danish letters in property values show as \X\E6; request UTF-8 style handling. | architect · feature_request · 2023 | [GH ThatOpen/engine_web-ifc#358](https://github.com/ThatOpen/engine_web-ifc/issues/358) (github_issue) |
| 2 | Mottakskontroll-typer on Eystein: scope config, Klar for Reduzer, quantities without Solibri |  | Reception-control types: quantities without Solibri | bim_manager · feature_request · 2026 | [GH Ed-Skiplum/ifc-check#15](https://github.com/Ed-Skiplum/ifc-check/issues/15) (github_issue) |
| 3 | Ønske om å oppdatere FOB_Sekvensnummer med serial number fra dRofus |  | Update a sequence-number parameter from the dRofus serial number | developer_programmer · feature_request · 2026 | [GH DanGjer/CableTrayHandler#1](https://github.com/DanGjer/CableTrayHandler/issues/1) (github_issue) |
| 4 | Oppslag i dRofus for subitem categories |  | Lookup in dRofus for subitem categories | developer_programmer · how_to · 2026 | [GH DanGjer/InfoNodeHandler#8](https://github.com/DanGjer/InfoNodeHandler/issues/8) (github_issue) |
| 5 | PR: Wrong EPSG-code when entering in GUI |  | Entering EPSG 3011 (SWEREF 99 18 00) in the exporter shows EPSG:6619 in the IFC file. | bim_coordinator · troubleshooting · 2024 | [GH Autodesk/revit-ifc#818](https://github.com/Autodesk/revit-ifc/issues/818) (github_issue) |
| 6 | Optimal settings for Ifc Export from Revit |  | dRofus recommends exporting from a 3D view with in-session settings, IFC2x3 Coordination View, rooms as spaces, Revit property sets on. | bim_coordinator · how_to · 2022 | [support.drofus.com](https://support.drofus.com/en/support/solutions/articles/16000118323-optimal-settings-for-ifc-export-from-revit) (vendor_kb) |

Counting: 13 + 6 = 19 records. The target of 20 to 50 is not reached; Swedish and Finnish contribute one (English) and zero records. Do not use this file as evidence of how Swedes or Finns write.

## Ready test prompts

All prompts are **synthetic**. 17 Norwegian prompts come verbatim from the dataset (source id shown); 14 are new (marked `new`), written for this document: 5 Norwegian, 3 Danish, 3 Swedish, 3 Finnish. Dataset prompts keep their difficulty tags; new prompts are tagged by the editor. Expected behaviors are in English.

### Norwegian: dataset prompts

| ID | Prompt (synthetic) | EN gloss | Persona · intent · difficulty | Expected behavior (what a good assistant does) |
|---|---|---|---|---|
| NO1<br><sub>no-norway-s001</sub> | sjekk hvilke objekter som mangler MMI i modellen, grupper per fag og gi meg antall | Check which objects lack an MMI value and list them by discipline | bim_coordinator · validate_check · medium · needs file | Scan property sets for an MMI property, list elements missing or empty, group by discipline/classification, report counts. |
| NO2<br><sub>no-norway-s002</sub> | hvorfor er det så mange IfcBuildingElementProxy her?? hvilke kategorier fra Revit kommer de fra | Why did so many elements come out as proxy and from which categories | bim_coordinator · query_model_data · medium · needs file | Count proxies, group by Revit category/ObjectType, suggest IfcExportAs fixes. |
| NO3<br><sub>no-norway-s003</sub> | kan du kontrollere modellen mot kravene i EIR-en, spesielt at alle vegger har brannklasse og lastbærende | Validate the model against the property requirements from the client's EIR | bim_manager · validate_check · medium · needs file | Check walls for fire rating and LoadBearing in Pset_WallCommon, report failures with GUIDs. |
| NO4<br><sub>no-norway-s004</sub> | etasjene blir dobbelt i IFC etter eksport fra Revit, noen ide? sjekk modellen | Storeys appear duplicated after IFC export | architect · troubleshoot_export · medium · needs file | List IfcBuildingStorey entries with elevations, detect duplicates/mismatched names, explain level export settings. |
| NO5<br><sub>no-norway-s005</sub> | ligger veimodellen i riktig koordinatsystem (EUREF89 NTM sone?) Hva er origo og rotasjon | Is the road alignment georeferenced in EUREF89 NTM and what is the offset? | civil_infra_engineer · query_model_data · hard · needs file | Read IfcMapConversion/IfcProjectedCRS, report EPSG, eastings/northings, rotation; flag missing georeferencing. |
| NO6<br><sub>no-norway-s006</sub> | har alle tekniske komponenter FDV-info og NS 3451-kode? vil ha liste over de som mangler | Do all technical equipment items have FDV data and a TFM/NS 3451 code? | owner_client · validate_check · medium · needs file | Check equipment for classification reference and maintenance properties, list gaps. |
| NO7<br><sub>no-norway-s007</sub> | list opp alle ventilasjonssystemer og antall kanaler i hvert system | List ventilation systems and the number of ducts per system | mep_engineer · query_model_data · easy · needs file | Query IfcSystem/IfcDistributionSystem and assigned duct segments, count per system. |
| NO8<br><sub>no-norway-s008</sub> | trenger mengder: netto areal yttervegger per etasje, uten åpninger | Total net area of external walls per floor | estimator_qs · extract_quantities · medium · needs file | Sum NetSideArea from Qto_WallBaseQuantities for external walls grouped by storey; note missing quantities. |
| NO9<br><sub>no-norway-s009</sub> | hva har endret seg i RIB-modellen siden forrige revisjon? trenger før møtet i morgen | What changed between the last two RIB model versions | structural_engineer · compare_versions · hard · needs file | Compare two files by GlobalId, report added/removed/modified elements and key property changes. |
| NO10<br><sub>no-norway-s010</sub> | kollisjonskontroll RIV mot RIB, lag BCF av de over 50 mm | Find clashes between ventilation and structure and export as BCF | bim_coordinator · coordinate_clash · hard · needs file | Run clash check with tolerance, filter, create BCF topics with viewpoints and GUIDs. |
| NO11<br><sub>no-norway-s011</sub> | hvordan eksporterer jeg fra Revit til IFC så bestiller godtar den? hvilken MVD og innstillinger | How do I export Revit to IFC so the client accepts it | student_beginner · how_to · easy | Explain MVD choice (Reference View / Design Transfer), property set export, mapping table, and checking against client requirements. |
| NO12<br><sub>no-norway-s012</sub> | æøå blir rare tegn i navnene når jeg leser IFC med ifcopenshell, hvorfor | Norwegian letters show garbled in names after reading IFC | developer_programmer · troubleshoot_code · medium | Explain IFC STEP \X2\ unicode escaping and how to decode; check source encoding. |
| NO13<br><sub>no-norway-s013</sub> | lag romliste med romnr, navn og BTA/NTA fra modellen | Space list with area and number for the building | facility_manager · query_model_data · easy · needs file | Extract IfcSpace with name, long name, area quantities and export a table. |
| NO14<br><sub>no-norway-s014</sub> | sjekk dørbredder i rømningsveier mot TEK17, hvilke dører er under 90 cm | Check door widths and escape routes for TEK17 | reviewer_authority · comply_regulation · hard · needs file | Filter doors on escape routes, read OverallWidth/clear width, list those below threshold with caveats on what is not modelled. |
| NO15<br><sub>no-norway-s015</sub> | sett IsProcured = true på alle prefab betongelementer og lagre ny ifc | Add procurement status to selected elements | contractor_site · modify_model_data · medium · needs file | Select precast elements, add/modify property in a custom Pset, save a new file preserving original. |
| NO16<br><sub>no-norway-s016</sub> | ifc-filen er 900 MB og tung å åpne. hva tar mest plass | IFC is huge and slow, find the cause | bim_manager · optimize_performance · medium · needs file | Profile entity counts and geometry representations, identify duplicated types or heavy meshes, suggest reductions. |
| NO17<br><sub>no-norway-s017</sub> | IFC4.3-filen fra Civil 3D viser ikke aksen i viewer, ligger den i filen? | Viewer does not show the IFC 4.3 alignment | civil_infra_engineer · troubleshoot_import · hard · needs file | Check for IfcAlignment and representation, report whether present and why viewers may skip it. |

### Norwegian: new

| ID | Prompt (synthetic) | EN gloss | Persona · intent · difficulty | Expected behavior (what a good assistant does) |
|---|---|---|---|---|
| NN1<br><sub>new</sub> | har alle bygningsdeler NS 3451-kode? list opp de som mangler, per fag | Does every building component have an NS 3451 code? List those missing, per discipline. | bim_manager · validate_check · medium · needs file | Look for IfcClassificationReference or a project property carrying an NS 3451 code; list elements without, grouped by IFC class and by discipline model if several files are loaded; state which system name was found; do not assume the code format. |
| NN2<br><sub>new</sub> | gi meg oversikt over MMI per fag: hvor mange objekter på 300, 350 og 400, og hvilke har ingen verdi? | Overview of MMI per discipline: how many objects at 300, 350, 400, and which have no value? | bim_coordinator · query_model_data · medium · needs file | Find the property that holds MMI (ask or detect its name and pset), count objects per value and discipline, list objects with empty or missing values with GUIDs; say which property was used; note that values must follow the project's MMI-veileder version. |
| NN3<br><sub>new</sub> | sjekk at alle kummer i VA-modellen har riktig IFC-klasse og at rørene er koblet til kummene | Check that all manholes in the VA model have the right IFC class and the pipes are connected to them. | civil_infra_engineer · validate_check · hard · needs file | List objects that look like manholes (by name or class), report class distribution including proxies, check port connections between pipes and manholes if present, list unconnected pipe ends; mention that the buildingSMART Norge VA guideline defines the expected classes and that the check used a generic rule. |
| NN4<br><sub>new</sub> | har alle prefab-elementene Milestone og IsProcured fra NS 8360? vis de som mangler | Do all precast elements have Milestone and IsProcured from NS 8360? Show those missing. | contractor_site · validate_check · medium · needs file | Select precast elements (by class, name or classification), look for the NS 8360 process properties Milestone and IsProcured in their psets, list elements missing either, with counts; report if the pset name could not be found. |
| NN5<br><sub>new</sub> | hva er forskjellen på IDS og BCF? og hvilken skal jeg bruke mot bestiller? | What is the difference between IDS and BCF, and which should I use towards the client? | student_beginner · understand_concept · easy | Explain IDS (machine-readable information requirements for automated checks) versus BCF (issue communication format) and that they complement each other: the client sends IDS as requirements, the team exchanges BCF issues; mention bSDD only if relevant. |

### Danish, Swedish, Finnish: new, unvalidated phrasing

These have no real-data backing for their wording. They are included so test sets cover the languages; a native speaker should review them before they are treated as realistic.

| ID | Prompt (synthetic) | EN gloss | Persona · intent · difficulty | Expected behavior (what a good assistant does) |
|---|---|---|---|---|
| NX1<br><sub>new</sub> | har alle bygningsdele en CCS-kode? vis dem uden, grupperet efter IFC-klasse | Does every building component have a CCS code? Show those without, grouped by IFC class. | bim_manager · validate_check · medium · needs file | Look for classification references named CCS (Cuneco Classification System) or a project property; list elements without, grouped by IFC class; state which classification name was found and do not assume Norwegian NS 3451. |
| NX2<br><sub>new</sub> | æ, ø og å ser forkerte ud i navnene efter eksport, jeg kan se noget med \X\E6. kan du tjekke modellen? | Æ, ø and å look wrong in names after export; I can see something like \X\E6. Can you check the model? | architect · troubleshoot_export · medium · needs file | Scan names and property values for IFC STEP escape sequences (\X\E6 is the ISO 8859-1 escape for æ, \X2\...\X0\ for Unicode); decode them, report which attributes carry them and whether the reading library or the exporter is at fault; explain that the file is valid and the viewer should decode it. |
| NX3<br><sub>new</sub> | lav en rumliste med rumnummer, navn og areal til driften, og marker rum uden navn | Make a room list with room number, name and area for operations, and mark rooms without a name. | facility_manager · extract_quantities · easy · needs file | List IfcSpace with Name, LongName, number and area from Qto_SpaceBaseQuantities; flag spaces without name or number; return a table suitable for export. |
| NX4<br><sub>new</sub> | ligger modellen i SWEREF 99 18 00 (EPSG:3011)? kolla koordinater och rotation | Is the model in SWEREF 99 18 00 (EPSG:3011)? Check coordinates and rotation. | civil_infra_engineer · query_model_data · medium · needs file | Read IfcProjectedCRS and IfcMapConversion (IFC4+); report the EPSG code actually written (a known exporter bug writes a different code than the one entered), eastings, northings, rotation; flag mismatch with EPSG:3011 and missing georeferencing in IFC2x3. |
| NX5<br><sub>new</sub> | har alla byggdelar en CoClass-kod? lista de som saknas, per disciplin | Do all building parts have a CoClass code? List those missing, per discipline. | bim_coordinator · validate_check · medium · needs file | Look for classification references or properties holding CoClass codes; list elements without, grouped by discipline model or IFC class; state which system name was found. |
| NX6<br><sub>new</sub> | vad har ändrats mellan version 3 och 4 av konstruktionsmodellen? nytt, borttaget och flyttat | What changed between version 3 and 4 of the structural model? New, removed and moved. | structural_engineer · compare_versions · hard · needs file | Compare the two files by GlobalId; report added, removed and moved elements (placement change above a tolerance); if GUIDs look unstable fall back to name/type/position matching and say so. |
| NX7<br><sub>new</sub> | onko kaikilla seinillä palonkestävyys, kantavuus ja ulkoseinätieto Pset_WallCommonissa? listaa puuttuvat | Do all walls have fire rating, load-bearing and external flag in Pset_WallCommon? List those missing. | bim_coordinator · validate_check · easy · needs file | Check Pset_WallCommon.FireRating, LoadBearing and IsExternal on all walls (instance and type); list walls missing any, with GUIDs and counts per storey. |
| NX8<br><sub>new</sub> | missä koordinaatistossa tietomalli on ja missä sen origo on? pitäisi täsmätä muiden osamallien kanssa | Which coordinate system is the model in and where is its origin? It should match the other discipline models. | bim_coordinator · coordinate_clash · medium · needs file | Read IfcMapConversion/IfcProjectedCRS where present, units, site placement and bounding box for each loaded file; compare across files and list offsets and rotation differences; state if the file is IFC2x3 and has no map conversion. |
| NX9<br><sub>new</sub> | onko tässä Inframodel- tai IFC 4.3 -tiedostossa tielinja mukana? näytä alku- ja loppupiste ja pituus | Does this Inframodel or IFC 4.3 file contain the road alignment? Show start and end point and length. | civil_infra_engineer · query_model_data · hard · needs file | For IFC 4.3 look for IfcAlignment with horizontal/vertical parts and report start and end stations and length; for an Inframodel (LandXML-based) file say the tool may not read it and ask for IFC; do not invent values if no alignment is present. |

(IDs inside the table: NN1 to NN5 Norwegian new; NX1 to NX3 Danish; NX4 to NX6 Swedish; NX7 to NX9 Finnish.)

## Tips for generating authentic prompts in this language

**Do**
- Norwegian: lower case, no greeting, imperative or one short question; keep IFC, Pset, proxy, Solibri, Revit, BCF, clash in English.
- Use the abbreviation set people use without explaining it: RIB, RIV, ARK, FDV, BTA/NTA, TEK17, MMI, NS 3451, VA.
- Put the check object and the grouping in the same line: "grupper per fag og gi meg antall", "RIV mot RIB, lag BCF av de over 50 mm".
- Mention the client role (bestiller, EIR) when the point is compliance; mention the client's name only if the test needs it (Statsbygg, Nye Veier, Bane NOR have their own rules that were not read).
- Include a deadline or mild frustration for a few prompts ("trenger før møtet i morgen", "??").
- Test `æøå` handling with at least one prompt per Nordic language; use the real `\X\E6` symptom for Danish.
- For infrastructure, use the real CRS names: EUREF89 NTM (Norway), SWEREF 99 18 00 / EPSG:3011 (Sweden).

**Don't**
- Do not present the Norwegian official-page paraphrases as things people said.
- Do not assume Denmark, Sweden or Finland follow Norwegian MMI or NS 3451; each country has its own classification (CCS, CoClass, Finnish YTV-based) per the national doc.
- Do not generate long polite Danish, Swedish or Finnish forum posts and call them realistic; there is no observed sample, keep them short and technical.
- Do not claim a Nordic "BIM law": requirements are client documents.
- Do not use Nynorsk or Sami unless the test explicitly targets them; the data covers bokmål only.
