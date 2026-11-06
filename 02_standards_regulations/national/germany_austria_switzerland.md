# Germany, Austria, Switzerland: BIM/IFC requirements

## In plain words

None of the three countries has a statute that says "every building must be delivered as an IFC model". What exists is a mix of (a) government roadmaps and circulars that make BIM the standard process for federal clients (roads in Germany since 2026, federal buildings via a phased Masterplan, rail operators with their own rules), (b) standards that clients put into contracts (VDI 2552, DIN SPEC 91391, ISO 19650 in Germany; ÖNORM A 6241 in Austria; formerly SIA 2051 in Switzerland), and (c) client documents (AIA = client information requirements, BAP = BIM execution plan) which in practice define the real IFC rules: version, view, property sets, classification, file naming, checking. For a tester of MCP servers that open, query and edit IFC models, the practical consequence is that "correct" depends on the project's AIA/BAP, and typical DACH requests are about IFC2x3 / IFC4 exports from Revit or Archicad/Allplan, German-language property names, DIN 276 cost groups, and rule-based checks (now increasingly IDS).

Last researched: 2026-11-06

Research limits: the web search quota ran out partway through, several government pages were unreachable and PDFs could not be text-extracted. Facts that rest only on search snippets are marked "(unverified)". See "Gaps".

---

## 1. Germany

### 1.1 Who mandates what

| Level | Body | Instrument | Since / status | Scope |
|---|---|---|---|---|
| Federal transport infrastructure | BMVI, now BMV (Federal Ministry of Transport; named BMDV in 2022-2025) | Stufenplan Digitales Planen und Bauen (staged plan) | Published 15 Dec 2015 [1]. Phase 1 preparation 2015-2017, phase 2 extended pilots 2017-2020, phase 3 gradual roll-out from 2020 with "Leistungsniveau 1" (performance level 1) for new BMVI tenders [1] | Federal transport infrastructure |
| Federal trunk roads | BMV, Autobahn GmbH des Bundes, DEGES, Länder (Auftragsverwaltung) | Masterplan BIM Bundesfernstraßen V1.0 (published 12.10.2021) [2] and ARS 05/2026 "Building Information Modeling (BIM) im Bundesfernstraßenbau" (Allgemeines Rundschreiben Straßenbau) [3] | BIM is the regular process ("Regelprozess") from 2026 for state road administrations, DEGES, Autobahn GmbH [3][4]. Roll-out announced 27 March 2026 at the "Dialogforum Bundesfernstraßen Digital" by the Federal Transport Minister [4][5] | "All relevant projects" of federal trunk roads. No numeric size threshold found (unverified whether one exists) |
| Federal buildings (Bundesbau) | BMI (2021 Masterplan), now BMWSB (housing/building), with BMVg and BImA | Masterplan BIM für Bundesbauten (Sept 2021), Erlass dated 27 Jan 2022, Umsetzungsstrategie March 2023 [6] | Three-stage introduction of BIM over the building life cycle; steering group (Lenkungsgruppe) financed equally by BMVg, BImA, BMWSB [6]. A trade article claims BIM has been required in Hochbau since end of 2022 [1b] (secondary source, unverified) | Federal construction projects; thresholds not verified |
| Central contact | BIM Deutschland (Zentrum für Digitalisierung des Bauwesens) | Joint initiative of BMDV, BMWSB, BMVg, founded October 2022 [7][8] | Operates the BIM-Portal; promotes Open BIM [8] | Information, standards, tools |
| Rail | DB InfraGO AG | Own binding BIM requirements (see 1.5) | Ongoing | DB projects |
| States and cities | e.g. Hamburg, Baden-Württemberg, Saxony (SIB), Lower Saxony, Bavaria (BIM Bayern, a promotion platform) | Own Muster-AIA/BAP, guides, pilots | Varies | State/municipal clients |

Note on wording: "BIM-Pflicht" (BIM obligation) in German media usually means "the federal client puts BIM requirements into its tenders", not a law that binds private builders. A trade blog on the 2026 road roll-out states that it applies to the federal road clients and that other contracting authorities are only encouraged to prepare voluntarily [5].

Lobbying point: buildingSMART Deutschland filed a Lobbyregister entry on 2 March 2026 titled "Präzisierung der Masterpläne BIM für Bundesbauten und Fernstraßen", asking the government to add binding Open BIM requirements to the Masterplans [9]. This shows that the Masterplans do not yet make Open BIM (IFC) formally binding in a strong sense. Treat claims "IFC4.3 is mandatory in Germany" as false unless a project AIA says so.

### 1.2 Key official documents (Germany)

| Document | Version/date | Notes |
|---|---|---|
| Stufenplan Digitales Planen und Bauen | 15 Dec 2015 | BMVI [1] |
| Masterplan BIM Bundesfernstraßen | V1.0, Oct 2021 | [2][10] |
| AIA Rahmendokument (roads) | V1.0, Oct 2021 | Listed IFC 4.0.2.1 MVD, IFC4 Design Transfer View, BCF 2.1 (from search snippet, unverified against full text) [10][11] |
| BAP Rahmendokument (roads) | V1.0, Oct 2021 | [10] |
| Anwendungsfälle für den Regelprozess | V3.0, Feb 2026 | Use cases for roads [10] |
| Objektkatalog Bundesfernstraßen | V1.0, Feb 2024; Anlage Mustermodell Apr 2024 | OKSTRA-based object catalogue [10] |
| Digitaler Zwilling Bundesfernstraßen (definition) | V1.0, Oct 2024 | [10] |
| Datenmanagement; Definition der Fachmodelle | V1.0, Oct 2021 | [10] |
| BIM-Leistungskatalog Bundesfernstraßen | agreed spring 2024 by Autobahn GmbH, DEGES and construction associations | Standardises tendering/billing of BIM services [5] |
| "Grundlagen der modellbasierten Genehmigung im Bereich der Bundesfernstraßen" | Annex to ARS 05/2026 | Model requirements for approval procedures (from search snippet, unverified) |
| Masterplan BIM für Bundesbauten | Sept 2021 | [6] |
| Umsetzungsstrategie BIM Bundesbauten | March 2023 | [6] |
| Muster-AIA, Muster-BAP, Anwendungsfall-Steckbriefe (Bundesbau) | Steckbriefe 2023; "AwF-Steckbriefe 2.0" July 2024 | Hosted on fib-bund.de and bundesbau.de [12] |
| DEGES AIA Muster | V2.01 | Typical formats listed: IFC2x3 or IFC4 for object structures, OKSTRA for alignment, GAEB-DA-XML and IFC for quantities/BoQ (snippet, unverified) [11] |

### 1.3 Standards used in German contracts

| Standard | What it is | Notes |
|---|---|---|
| VDI 2552 series | German BIM guideline series (VDI, many co-published with buildingSMART as VDI/bS) | See table below |
| DIN SPEC 91391-1 and -2 | Common Data Environment: functions of a CDE (Part 1) and open data exchange between CDEs, "openCDE" interface (Part 2) | Presented March 2019; free to download in German/English [13][14] |
| DIN EN ISO 19650 (parts 1-6) | Information management | A DIN overview lists DIN EN ISO 19650-1 as draft 2026-04 and -6 as 2025-10 (snippet, unverified) [14] |
| ISO 16739-1:2024 (IFC4.3) / ISO 16739-1:2018 (IFC4) | IFC data schema; DIN EN ISO 16739-1 national adoption | ISO 16739-1:2024-03 cited as current [15] |
| DIN 276 | Cost groups (Kostengruppen), widely used as classification in AIAs (from background knowledge, unverified here) | |

VDI 2552 sheets per the VDI handbook page (dates as listed there) [16]:

| Blatt | Title | Date |
|---|---|---|
| 1 | Grundlagen | 2020-07 |
| 2 | Begriffe (terms) | 2022-08 |
| 3 | Modellbasierte Mengenermittlung (model-based quantity take-off) | 2018-05 |
| 4 | Anforderungen an den Datenaustausch (data exchange requirements) | 2020-08 (new draft "Modellierung von Fach- und Teilmodellen" 2026-05) |
| 5 | Datenmanagement | 2018-12 |
| 6 | Betrieb (operation) | 2026-04 |
| 7 | Prozesse | 2020-06 |
| 8.1 / 8.2 / 8.3 | Qualifikationen (qualifications) | 2019 / 2022 / 2022 |
| 9 | Klassifikationssysteme (classification systems) | 2022-03 |
| 10 | AIA und BAP | 2021-02 |
| 11.1 | Informationsaustauschanforderungen zu BIM-Anwendungsfällen (exchange requirements for use cases) | 2021-10 [17] |
| 11.2 | Schlitz- und Durchbruchsplanung (slots and openings) | 2022-06 |
| 11.3 | Schalungs- und Gerüsttechnik (formwork/scaffolding) | 2020-07 |
| 11.5 / 11.7 / 11.8 | Aufzugstechnik / Türplanung / Fabrikplanung | 2023-09 / 2026-02 / 2023-09 |
| 11.9, 11.10 | Bauphysik, Gebäudeautomation | drafts (2026) |
| 12.1 / 12.2 | Structure and metadata for describing BIM use cases | 2022-10 / 2024-03 |

buildingSMART Deutschland states that the 11.x sheets aim at Open BIM exchange, especially IFC4 with the MVDs Reference View and Design Transfer View [18]. Sheet 11.1 describes methods to define exchange requirements (ER) that can be implemented in software and used as basis for technical certificates [17].

### 1.4 IFC-specific requirements in practice

What is firmly sourced:
- IFC versions seen in German public-client documents: IFC2x3 and IFC4 [11]; roads Rahmendokument names IFC4 (ADD2 TC1, written "4.0.2.1") MVD, Design Transfer View, and BCF 2.1 [11].
- IFC4.3 is the version that adds road/rail/bridge/tunnel/waterway entities; the Rahmendokument/ARS context says infrastructure classes in IFC versions are still developing, and IFC4.3 does not appear in the searched AIA snippets (unverified) [11].
- Alignment data in roads: OKSTRA (Objektkatalog für das Straßen- und Verkehrswesen) alongside IFC [10][11].
- Property and requirement handling is moving to buildingSMART IDS (Information Delivery Specification): the BIM-Portal removed ifcXML and mvdXML exports in favour of IDS and now checks that classification values are correct, not just present [19].
- Delivery: IFC required in addition to native files on DB passenger-station projects [20].

Typical AIA/BAP content (general practice, partly from background knowledge, unverified for any single AIA):
- Naming of model files and elements, usually per discipline and phase.
- Project origin / coordinates: a shared project base point and survey point, often ETRS89 / UTM zone 32 (EPSG:25832) or a Gauss-Krüger zone; IfcMapConversion in IFC4+ is the correct carrier for georeferencing.
- Classification: DIN 276 cost group per element, sometimes a client-specific Merkmal (property) such as a KG code; for roads OKSTRA object classes.
- Level of information need (LOIN, German "Informationsbedarfstiefe"), replacing the older LOD discussions.
- Quality assurance in staged checks: discipline model check, coordination model check, release (Muster-BAP structure) [12].
- Clash/issue communication via BCF.

### 1.5 Official templates, tools and portals

- BIM-Portal des Bundes (https://via.bund.de/bim/infrastruktur/landing): operated by BIM Deutschland; modules Merkmale (property knowledge base), AIA (checkable client information requirements), Objektkataloge/Objektvorlagen, and checking tools; release R 3.5.0 in June 2025; newsletter mentions R 3.14.0 in October 2026; filters by building type, project phase and actor [8][19][21].
- Muster-AIA / Muster-BAP: federal (fib-bund.de / bundesbau.de), state-level (Saxony SIB, Baden-Württemberg, Hamburg, Lower Saxony, Brandenburg) and city (Stuttgart) templates exist [12].
- Roads: the document portal at bundesfernstrassen-digital.de lists the Rahmendokumente (table 1.2) [10]. Autobahn GmbH uses cockpit.planner for BIM object management (trade-press snippet, unverified) and its service catalogue lists IFC among sub-model delivery formats with content defined by a LOIN concept [22].
- Deutsche Bahn: DB InfraGO Personenbahnhöfe publishes binding "Vorgaben zur Anwendung der BIM-Methodik", BIM-Pflichtenheft, Anlage A (digital component library in .rvt and .ifc), project template, georeferencing instructions and sample models, plus the PKP project communication platform [20][23]. DB InfraGO Fahrweg has its own BAP template (V6.0 external) and an object library (Musterantrag V4.1) [24]. A Richtlinie "826" for BIM was not confirmed (unverified).
- Building permits: XBau is the federal XÖV standard for exchange in building-supervision procedures [25]. The XBau site has a menu item "XStandards und BIM" but I could not read its content; I found no verified production BIM permit process in Germany. Pilots for BIM-based permits exist at research level (e.g. model-based approval for federal roads, see ARS 05/2026 annex) (unverified). XPlanung relation to IFC: not verified.

### 1.6 National classification and data systems

| System | Purpose |
|---|---|
| DIN 276 Kostengruppen | Cost groups, common element classification in AIAs |
| DIN 277 | Areas and volumes |
| STLB-Bau / GAEB | Standard specification texts and BoQ exchange (GAEB DA XML) |
| OKSTRA | Roads and traffic object catalogue (XML-based) |
| bSDD (international) | buildingSMART Data Dictionary; used for classification/property lookups |
| BIM-Portal Merkmale | National property knowledge base |

### 1.7 Organizations

- buildingSMART Deutschland e.V. (chapter; Lobbyregister number R000839) [9]; co-publishes VDI/bS guidelines [18].
- BIM Deutschland (federal) [8].
- VDI, DIN, BIM Cluster Bayern [26], BIM Institut Uni Wuppertal (scientific support for Bundesbau) [27], planen-bauen-4.0 (not verified), DEGES, Autobahn GmbH.

### 1.8 Local software ecosystem

- Nemetschek group (Munich): Allplan, Graphisoft Archicad (Budapest), Vectorworks, Solibri (Finland), Nevaris (AVA) (company facts from background knowledge, unverified here).
- RIB iTWO (Stuttgart, AVA/5D), California.pro, ORCA AVA (unverified).
- Revit is dominant in large practices; Revit IFC export uses the open-source IFC exporter with setups for IFC2x3 Coordination View 2.0 and IFC4 Reference View / Design Transfer View (background knowledge; menu path File > Export > IFC; unverified in this session).
- Enthusiast/open-source: IDS4All open-source converter (Excel to IDS) from the Austrian AIA4ALL project [28]; KIT's FZKViewer for IFC (unverified). BIMcollab, BIMQ feature server (unverified).

---

## 2. Austria

### 2.1 Mandate status
- BIM is not legally mandatory and has no general public-procurement requirement; the employer usually decides, and the ÖNORM is agreed contractually (CMS expert guide, last updated 2017, so possibly outdated) [29].
- ÖNORM A 6241-1 (BIM Level 2, replaced ÖNORM A 6240-4) and ÖNORM A 6241-2 (BIM Level 3 iBIM) were published in 2015 [29].
- A new ÖNORM A 6241-2 edition with issue date 2026-09-01 is in the Austrian Standards shop: "Digital structure documentation - Part 2: Building Information modeling (BIM)", 59 pages, German, committee 273; it covers open BIM over the life cycle with IFC including the extensions in ÖNORM EN ISO 12006-3. The shop shows both "Draft" and "Current", so the status needs confirming (unverified) [30].
- A research report says IFC-mapped definitions were adopted by Austrian Standards on 22 Nov 2023 and incorporated in ÖNORM A 6241-2 (snippet, unverified).

### 2.2 Vienna: openBIM building permit (MA 37)
- Pilot operation of the openBIM permit procedure of the Vienna Building Police (Magistratsabteilung 37), based on the research project BRISE-Vienna [31].
- Applicant submits the building application model (BAM, architectural model). IFC2x3 and IFC4 Add2 TC1 are permitted; ÖNORM A 6241-2 applies to modelling; requirements are delivered as PDF, XLSX and IDS files [31].
- Property sets: ISO 16739 standard Psets, quantity sets (Qto), and a Vienna-specific set "WienBV"; LOG + LOI define LOIN per element class [31].
- Status on the buildingSMART use case page: draft published 16 July 2024, last changed 13 Oct 2025; version 1.1 on 22 Nov 2024, 1.2 adds extended IDS with logical dependencies, 1.3 merges Excel files and improves PredefinedType export [31].
- Today BIM plus PDF are submitted in parallel (the BIM does not replace the drawings yet) [31].
- Actors: MA 37, applicant and plan author, TU Wien, Kammer der ZiviltechnikerInnen, buildingSMART Austria [31].

### 2.3 Other
- AIA4ALL (TU Wien, AIT lead, Plandata, e7, buildingSMART Austria; FFG-funded 2022-2025): machine-readable modular AIA/BAP generating IDS and checking rules [28].
- buildingSMART Austria (Vienna): BIMcert certification, Regelwerk AIA+BAP (2020), BIM-Leistungsbilder (2022), BIMcert handbook "Grundlagenwissen openBIM" (2024), BIM-Lake 2026 DACH meeting [32].
- Classification: ÖNORM-based; details (e.g. A 6241-2 Anhang) not verified.
- Software: Archicad is strong in Austria; Plandata (Vienna) as BIM consultant; ABK (unverified).

---

## 3. Switzerland

### 3.1 Mandate status
- No federal BIM law found. Roll-outs are done by large clients (SBB, federal real estate, cantons).
- SIA-Merkblatt 2051 "Building Information Modelling (BIM) - Grundlagen zur Anwendung der BIM-Methode" (December 2017) was reported withdrawn at the end of 2024 (search snippet from FHNW, unverified). A direct replacement was not identified. SIA D 0270 and D 0271 were supplementary documents (snippet).
- IFC is adopted in Switzerland as SN EN ISO 16739, published 1 May 2017 (snippet, unverified).
- SBB: introduces BIM in stages since 2025 ("Planen mit BIM" first); news Oct 2026: revised SN 506 512 (Baukostenplan Tiefbau), new BIM annex to regulation RTE 26201, Fachdatenkatalog (FDK) 17.0.0, new recommendation on data dictionaries; the page had no IFC requirement text [33]. FDK v15.2 dated March 2025 [33].
- Bauen digital Schweiz (buildingSMART Switzerland): platform for the digital transformation; publications section with glossary, roadmap (Stufenplan) and working documents; Sept 2026 recommendation on "Data Dictionaries"; Oct 2026 call for an Objektkatalog für die Bauausführung [34]. Its contract guidance recommends defining client expectations in an EIR [35] (snippet).
- CH Glossar digitale Bauwirtschaft (V2022.11, hosted by SBB) [36].

### 3.2 Classification
- eBKP-H (Baukostenplan Hochbau, SN 506 511) and eBKP-T (Tiefbau, SN 506 512) from CRB (background knowledge, partly confirmed by the SN 506 512 news) [33]; CRB Standardpositionen-Katalog (NPK) (unverified).

---

## 4. Local terminology

| Native term | Transliteration / pronunciation | English |
|---|---|---|
| Auftraggeber-Informationsanforderungen (AIA) | Auftraggeber-Informatsionsanforderungen | Employer/client information requirements (EIR) |
| BIM-Abwicklungsplan (BAP) | BIM-Abwicklungsplan | BIM execution plan (BEP) |
| Gemeinsame Datenumgebung (GDU) | Gemeinsame Datenumgebung | Common data environment (CDE) |
| Informationsbedarfstiefe | Informationsbedarfstiefe | Level of information need (LOIN) |
| Anwendungsfall (AwF) | Anwendungsfall | BIM use case |
| Fachmodell / Teilmodell / Koordinationsmodell | Fachmodell | Discipline model / part model / federated coordination model |
| Merkmal / Merkmalgruppe | Merkmal | Property / property set |
| Kostengruppe (KG) | Kostengruppe | Cost group (DIN 276) |
| Leistungsniveau | Leistungsniveau | Performance level (Stufenplan) |
| Regelprozess | Regelprozess | Standard process |
| Bauwerber/Planverfasser (AT) | Bauwerber | Applicant / plan author |
| Baueinreichung / Baugenehmigung | Baueinreichung | Building permit submission / approval |
| Bauantrag | Bauantrag | Building permit application (DE) |
| Baukostenplan (CH) | Baukostenplan | Cost plan (eBKP) |
| Objektkatalog | Objektkatalog | Object catalogue |
| Auftragsverwaltung | Auftragsverwaltung | Delegated administration (Länder administer federal roads) |
| Rundschreiben (ARS) | Rundschreiben | Circular |
| Ausführungsplanung / Bestandsmodell | Ausfuehrungsplanung | Execution design / as-built model |

---

## Typical questions people ask about this

All below are (illustrative) unless a source is given; I did not find directly linkable forum threads that I could read (one Graphisoft community thread titled "BIM mit der Deutschen Bahn" exists on IFC/DB requirements: https://community.graphisoft.com/t5/Projektdaten-BIM/BIM-mit-der-deutschen-Bahn/m-p/631852; content not read).

1. Is BIM mandatory for public projects in Germany? (illustrative) Short: no general law; mandatory in practice for federal road projects from 2026 and via federal client rules for Bundesbau.
2. Which IFC version does the Autobahn GmbH want, IFC2x3, IFC4 or IFC4.3? (illustrative) See 1.4: AIA documents name IFC4 ADD2 TC1 / Design Transfer View; check the project AIA.
3. What is the difference between AIA and BAP? (illustrative)
4. Where can I download a Muster-AIA for a federal building? (illustrative) Answer: fib-bund.de / bundesbau.de [12].
5. How do I export from Revit as IFC4 Reference View vs Design Transfer View? (illustrative)
6. Which property set holds the DIN 276 cost group? (illustrative) Usually a client-defined Merkmal; no universal Pset.
7. How is a project located (georeferenced) in IFC for German surveying coordinates (ETRS89/UTM32)? (illustrative) IfcMapConversion + IfcProjectedCRS.
8. What is IDS and can the BIM-Portal export one? (illustrative) Yes, IDS export; ifcXML/mvdXML exports removed [19].
9. What does VDI 2552 Blatt 11.1 add over Blatt 10? (illustrative) [17]
10. Is IFC4.3 required for road models? (illustrative) Not confirmed as mandatory; see 1.4.
11. What does the Vienna openBIM permit pilot accept? (illustrative) IFC2x3 or IFC4 ADD2 TC1 with IDS checks [31].
12. Is ÖNORM A 6241-2 mandatory? (illustrative) Contractual, not legal [29].
13. Is SIA 2051 still valid? (illustrative) Reported withdrawn end of 2024 [snippet, unverified].
14. What does the SBB require for BIM deliverables? (illustrative) See SBB BIM downloads [33].
15. What is DIN SPEC 91391 and do I need it? (illustrative) CDE functions and openCDE interface [13].
16. How should rooms and spaces (IfcSpace) be named according to a typical German AIA? (illustrative)
17. How do I check a model against an AIA automatically? (illustrative) IDS plus checkers (Solibri, BIMcollab Zoom, ifctester).
18. Which classification does DB InfraGO station BIM use? (illustrative)

## Common pitfalls and misconceptions

- "BIM-Pflicht" is not a general legal obligation; check the client's AIA and tender.
- Search snippets and trade articles disagree on dates (e.g. "BIM required since Jan 2021 / end of 2022" vs. official "Regelprozess from 2026" for roads). Prefer the ministry circular (ARS 05/2026).
- IFC4.3 is not mandated; many AIAs still require IFC2x3 or IFC4.
- "IFC4 ADD2 TC1" appears under several names (IFC 4.0.2.1, IFC4 Add2 TC1, Reference/Design Transfer View); testers should not treat these as different versions.
- SIA 2051 is reported withdrawn; do not cite it as current in Swiss answers.
- ÖNORM A 6241-2 now has a 2026 edition; the 2015 edition's text may differ.
- Austrian permit pilot: the IFC is submitted in parallel with PDF, so the model is not the legal document yet [31].
- Version names of ministries changed (BMVI, BMDV, BMV; BMI to BMWSB).
- Paywalled standards (ÖNORM, VDI, DIN, SIA) cannot be read in full; summaries are not substitutes.

## Gaps

- bmv.de was unreachable (connection refused), so the Masterplan text and ARS 05/2026 text were not read; PDF documents (AIA/BAP Rahmendokumente, DEGES AIA, Bundesbau strategy) could not be text-extracted; facts come from search summaries.
- buildingsmart.org, technical.buildingsmart.org and the standards site returned 403; IFC version facts come from other sources and background knowledge.
- The web search quota ran out before I could research XBau/XPlanung BIM pilots, the Vienna BRISE project beyond the UCM page, Swiss federal (BBL) and SIA successors, DB Richtlinie 826, forum threads, and open-source projects. Those parts are thin or unverified.
- No suspicious or pirated sites were encountered.

## Sources

[1] https://www.bmv.de/SharedDocs/DE/Artikel/G/bim-grundlagen-und-vorarbeiten.html (Stufenplan; reached via search results only)
[1b] https://www.ibau.de/akademie/wissenswertes/bim-nutzung-verpflichtend/
[2] https://www.bmv.de/SharedDocs/DE/Artikel/StB/masterplan-bim-bundesfernstrassen.html (search result only)
[3] https://www.bmv.de/SharedDocs/DE/Artikel/mFUND/Projekte/begebim.html (search snippet: ARS 05/2026 annex)
[4] https://www.bmv.de/SharedDocs/DE/Pressemitteilungen/2026/024-schnieder-deutschland-wird-bim-land.html (search snippet)
[5] https://blog.cosinex.de/2026/05/12/bim-bundesfernstrassen-oeffentliche-vergabe/
[6] https://fib-bund.de/Inhalt/Themen/BIM_fuer_Bundesbauten/2023-03_Umsetzungsstrategie_BIM_Bundesbauten.pdf and https://fib-bund.de/Inhalt/Themen/BIM_fuer_Bundesbauten/2021-11-01_BIM_Masterplan.pdf (search snippets only)
[7] https://www.baunetzwissen.de/integrales-planen/tipps/news/gebuendelte-informationen-im-bim-portal-9976724
[8] https://www.bimdeutschland.de
[9] https://www.lobbyregister.bundestag.de/inhalte-der-interessenvertretung/regelungsvorhabensuche/RV0022774/392709
[10] https://www.bundesfernstrassen-digital.de/bim/publikationen
[11] https://www.deges.de/wp-content/uploads/2023/03/BIM_AIA_Muster_V201_mit_Hinweisen.pdf and https://www.bim-bundesfernstrassen.de/fileadmin/user_upload/Rahmendokumente/bim-rd-aia.pdf (search snippets only)
[12] https://fib-bund.de/Inhalt/Themen/BIM_fuer_Bundesbauten/BIM_AH_Muster-AIA.pdf ; https://fib-bund.de/Inhalt/Themen/BIM_fuer_Bundesbauten/BIM_AH_Muster-BAP.pdf ; https://fib-bund.de/Inhalt/Themen/BIM_fuer_Bundesbauten/2024-07_BIM_AH_AwF-Steckbriefe_2.0.pdf ; https://bundesbau.de/fileadmin/user_upload/BIM_Roadmap/bbau_ah_anwendungsfallsteckbriefe_230516.pdf (search snippets only)
[13] https://www.dinmedia.de/de/technische-regel/din-spec-91391-1/302483139
[14] https://www.baunetzwissen.de/integrales-planen/tipps/news/neue-norm-din-spec-91391-fuer-die-bim-planung-6467834 ; https://www.dinmedia.de/resource/blob/1053828/510f2263a2443db8a02e6466ec31e41a/bim-normen-online-inhalt-data.pdf (snippet only)
[15] https://www.baunetzwissen.de/bim/fachwissen/standardisierung/ifc-der-offene-standard-fuer-bim-modelle-5288161
[16] https://www.vdi.de/richtlinien/details/vdi-handbuch-building-information-modeling
[17] https://www.vdi.de/richtlinien/details/vdibs-2552-blatt-111-building-information-modeling-informationsaustauschanforderungen-zu-bim-anwendungsfaellen
[18] https://www.buildingsmart.de/normen-und-richtlinien (search snippet)
[19] https://www.baunetzwissen.de/drucken/gebuendelte-informationen-im-bim-portal-9976724
[20] https://infoplattform-personenbahnhoefe.deutschebahn.com/pbhf/DB-BIM ; https://www.bim.bayern.de/wp-content/uploads/2024/10/DP.2024.50.10.16-Station-Ebermergen-Neubau-Bahnsteig-Gl-1-Harburg-Schwaben.pdf (snippet)
[21] https://via.bund.de/bim/infrastruktur/landing
[22] https://www.autobahn.de/storage/user_upload/qbank/Anlage_1_Leistungsbeschreibung_Autobahn.pdf (snippet)
[23] https://infoplattform-personenbahnhoefe.deutschebahn.com/resource/blob/7716924/1c84a39a003de7e327e4cd158cb87fb6/Vorgaben-zur-Anwendung-der-BIM-Methodik-data.pdf (snippet)
[24] https://bim.dbinfrago.com/resource/blob/12624362/8fe92b06fe672df3a1e5c3b4a44c1414/DB-InfraGO-Fahrweg-BAP-V-6-0-extern-data.pdf (snippet)
[25] https://www.xleitstelle.de/xbau
[26] https://www.bim.bayern.de
[27] https://biminstitut.uni-wuppertal.de/en/research/current-research-projects/bundesbau-wissenschaftliche-begleitung/ (search result)
[28] https://tuwien.at/cee/ibb/zdb/forschung/abgeschlossene-forschungsprojekte/aia4all-1
[29] https://cms.law/en/int/expert-guides/cms-expert-guide-to-building-information-modelling-bim/austria
[30] https://www.austrian-standards.at/en/shop/onorm-a-6241-2-2026-09-01~p5058043
[31] https://ucm.buildingsmart.org/use-case-details/3297/en
[32] https://www.buildingsmart.co.at/
[33] https://company.sbb.ch/de/bahnentwicklung/zukunft-bahn/bim.html
[34] https://www.bauen-digital.ch
[35] https://irf.fhnw.ch/entities/publication/ae3d27f4-e33b-4498-b495-efcc6ff48299/full (SIA 2051 record; withdrawal claim from search snippet)
[36] https://bimchange.sbb.ch/content/dam/internet/bimchange/downloads/de/CH%20Glossar%20digitale%20Bauwirtschaft%20(GLO_DE_V2022.11).pdf.sbbdownload.pdf (search snippet)
