# France and the French-speaking world: BIM/IFC requirements

## In plain words

France, French-speaking Belgium, Switzerland, Quebec and francophone Africa all use IFC (Industry Foundation Classes, ISO 16739), but almost none of them has a single law that says "deliver IFC version X". Instead there are national or owner-level BIM plans, owner-specific BIM requirement documents, and a national chapter of buildingSMART that promotes openBIM. In France the state plan was the PTNB (2015), replaced by the Plan BIM 2022 (2018); public buyers may require BIM tools under EU Directive 2014/24/EU. In Quebec the strongest evidence is a 2021-2026 government roadmap and the SQI's own BIM requirement documents, which are written in French and do not name IFC on the pages I could read. Belgium's most concrete recent item is a 2026 "IFC-first" policy from Brussels Airport. Swiss practice is documented by the association Bauen digital Schweiz / buildingSMART Switzerland. For Morocco, Algeria, Senegal and Cote d'Ivoire I could verify almost nothing official (see Gaps).

For a QA tester: expect test requests in French (or German-Swiss terms), expect "maquette numerique" instead of "BIM model", and expect owner-specific rules instead of one national IFC rule.

Last researched: 2026-11-06. QA pass 2026-11-06: the French Wikipedia BIM page and two SQI (Quebec) pages were re-fetched; most dates and figures are confirmed, with a few precision fixes noted inline. See `_meta/qa/qa-standards-2.md`.

**Research limits (read first).** In this run the web-search tool refused all queries (search budget exhausted), and several official sites returned HTTP 403 to the fetch tool (batiment-numerique.fr, mediaconstruct.fr, buildingsmart.org, technical.buildingsmart.org, iso.org). The document is therefore built from the pages that could be fetched (Wikipedia, SQI Quebec, buildingSMART Belgium, Bauen digital Schweiz, KROQI, buildingSMART GitHub). Everything not backed by a fetched page is marked "(unverified)". Treat unverified items as leads to check, not as facts.

## 1. France

### 1.1 Policy timeline

| Year | Event | Source |
|---|---|---|
| 26 Feb 2014 | EU Directive 2014/24/EU, art. 22(4): member states may require "electronic modelling tools for buildings" in public works and design contests; transposition due 18 Apr 2016 | [1] |
| 2014 | AFNOR experimental standard XP P07-150 gives the French transcription "Modelisation des Informations d'une Construction" | [1] (QA: the page cites XP P07-150 without a year; 2014 is (unverified)) |
| 20 Jan 2015 | PTNB (Plan de Transition Numerique dans le Batiment) presented, chaired by Bertrand Delcambre, with a EUR 20 million fund; portal opened 1 Jul 2015 by minister Sylvia Pinel | [1] (QA: the French Wikipedia text gives "20 janvier" without a year, so 2015 is inferred from the 1 Jul 2015 portal footnote; the minister's name was not re-checked) |
| 2017 | PTNB launches a BIM training site; AND Construction founded | [1][2] |
| 2018 | Plan BIM 2022 replaces the PTNB; run by AND Construction; KROQI platform (CSTB) supports it (QA: Plan BIM 2022 appears in the English sources [2], not in the French Wikipedia page re-read). Trade press headline: "Le PTNB est mort, vive le Plan BIM 2022" (Le Moniteur, 20 Nov 2018) | [2] |
| 29 Jan 2019 | Journal officiel publishes the official French term "bati immobilier modelise" (Commission d'enrichissement de la langue francaise) | [1] |
| 12 Jul 2019 | Two professional titles created by arretes: "BIM modeleur du batiment" and "Coordinateur BIM du batiment" | [1] |

Plan BIM 2022 objective, governance details and any post-2022 successor: not verified in this run (official site not reachable). Do not assume a successor plan exists or has a given name.

### 1.2 What is (and is not) mandatory

- No verified French law obliges IFC delivery. The legal basis is permissive: public buyers *may* require BIM tools (Directive 2014/24/EU art. 22(4) [1]). The French transposition sits in the Code de la commande publique (article number R2132-10, unverified).
- In practice the requirement appears in each tender: a "cahier des charges BIM" / "exigences BIM" annex and a "convention BIM" signed by the project team (unverified in detail, standard French practice).
- Adoption data (CNOA, March 2018): BIM in architecture competitions rose from 0.49% (2013-2014) to 8.10% (2018); BIM competence required in the team in 68.75% of the competitions counted (as phrased on the French page); the overall market share of BIM was 15.34% in the latest figure cited, which the page does not date (earlier points on the page: 5.39% for 2013-2015 and 11.74% on 30 March 2016) [1]. These are old numbers; do not present them as current.

### 1.3 Standards used in France

| Standard | Notes | Source |
|---|---|---|
| NF EN ISO 19650-1 and -2 | AFNOR French edition of ISO 19650 parts 1-2 (information management; BIM execution plan, CDE) | [1] |
| ISO 19650 parts | Part 1 (2018), 2 (2018), 3 (2020), 4 (2022), 5 (2020), 6 (2025) | [5] |
| XP P07-150 | Older French experimental vocabulary standard | [1] |
| ISO 16739-1 (IFC) | ISO 16739-1:2024 is the current edition (IFC4.3 ADD2); earlier ISO 16739-1:2018 corresponds to IFC4 | [4] |

### 1.4 Organizations

- **Mediaconstruct** = French national chapter of buildingSMART (open standards: IFC, BCF, etc.) [3]. Also active in IFC evolution: the French research project MINnD (infrastructure) [1].
- **CSTB** (Centre Scientifique et Technique du Batiment) develops **KROQI**, a collaborative BIM platform: document management with versions and access rights, BIM viewer, visas, tasks, mobile app; it states it relies on buildingSMART open standards and supports **IFC and BCF**; data hosted in France; vendor claims a SecNumCloud-qualified SaaS and ISO 27001:2022 [6]. KROQI was cited as the supporting platform of Plan BIM 2022 [2].
- **AND Construction**: operator of Plan BIM 2022 [2]. **AFNOR**: standardisation body [1].
- Training ecosystem: CSTB BIM manager course (2014), ENPC/ESTP specialised master (2014), CESI option (2015) [1].

### 1.5 IFC specifics for France

Verified: IFC2x3 (Feb 2006; TC1 July 2007 flagged "recommended" on French Wikipedia), IFC4 (Mar 2013), IFC4 Add1 (2015), IFC4 Add2 (2016), IFC4 Add2 TC1 (2017), IFC4.3 ADD2 (2024) [3][4]. French practice note on Wikipedia (flagged citation-needed since 2017): IFC knowledge is limited and DWG/DXF still dominate exchange [3] - likely outdated.

Not verified (no French source read): any national MVD, French Psets, French classification mandate, French georeferencing rule (typically Lambert-93 / EPSG:2154 and CC zones EPSG:3942-3950; this is general knowledge, not from a fetched source), naming charter. In French projects these are normally defined in the project's "convention BIM". A test model should be checked against the *project* convention, not a national rule.

## 2. Belgium (French-speaking part)

- **buildingSMART Belgium** promotes openBIM standards; site offers downloads including an "IDS Escape Game + Crash Course" and Bonsai (Blender) slides [11][13].
- **Brussels Airport Company (BAC) Open BIM policy**, published 8 May 2026: IFC is the contractual final deliverable on all projects and basis for all quality checks ("single source of truth"); native as-built files must also be delivered but only for maintenance; IFC is the long-term archive format; scope = full portfolio and life cycle; Revit and Civil 3D are the tools BAC itself can maintain; IFC version and IDS are **not** specified in the article [12]. PDF: [13] (not read).
- Regional/federal Belgian rules (Wallonia, Brussels region, Regie des Batiments / Buildings Agency, Flanders), Digital Built Belgium, national BIM protocol: not verified.

## 3. Switzerland (French-speaking Romandie and national)

Association: **Bauen digital Schweiz / buildingSMART Switzerland**, Zurich, with French pages at /fr/ [14]. Verified publications [15][16]:

- Level of Information Need (LOIN) basics (2024), based on **SN EN 17412-1**; LOIN applications for building (Hochbau) and landscape (2024), building automation (2026).
- BIM-Projektabwicklungsplan (BIM execution plan, 2020), BIM Nutzungsplan (use plan, 2018/2021), BIM-Abwicklungsmodell (2022), BIM Vertrag/Rollen/Leistungen (2022), Stufenplan Schweiz (2018), Referenzmodell (NEST building, 2020).
- BIMcert Handbuch openBIM (2024, DACH harmonised; French translation planned Q4 2025 per the site), buildingSMART certification basis.
- Data Dictionaries (2026), bSDD-based EPD work; Datenfeldkatalog BIM2FM (2023) referencing ProLeMo, EN 15221, LEKAS and **eBKP-H** (Swiss cost classification for buildings, also used for model-based cost estimation).
- Expert groups: openBIM Standards & Solutions, BIM2FM, "IFC for Site, Landscape and urban Planning".

Not seen on these pages (so unverified): SIA 2051 (Swiss BIM method standard), KBOB federal recommendations, CRB role (CRB only named as glossary carrier).

## 4. Quebec (Canada)

All facts below from SQI pages [7][8][9][10] unless stated.

**Terminology.** The SQI calls BIM "modelisation des donnees des infrastructures (MDI)"; the OQLF proposed "modelisation des donnees d'un batiment" in 2008 [1]. PCI = "processus de conception integree" (integrated design process).

**Government roadmap.** "Feuille de route gouvernementale pour la modelisation des donnees des infrastructures (2021-2026)": five years, April 2021 - March 2026; derived from the "Plan d'action pour le secteur de la construction", which aims to make BIM a requirement for public infrastructure projects. Eight public owners signed: SQI, Ministere des Transports et de la Mobilite durable, Societe d'habitation du Quebec, Hydro-Quebec, Parc olympique, and the cities of Longueuil, Montreal and Quebec. Documents: roadmap updated at 31 March 2025 (PDF), summary, and "Constats et plan d'action - SOMMET BIM 2023". The page names no thresholds, no mandatory date and no IFC [8]. Upcoming event: Sommet BIM+, 17-18 Nov 2026, Centre des congres de Quebec [8] (QA: all of the roadmap period, the eight committed owners, the 31 March 2025 update and the event date were re-confirmed; the page says the owners are "engages" (committed), not necessarily "signatories"). A roadmap beyond March 2026 is not verified.

**SQI roadmap 2016-2026.** BIM-PCI deployment began 2016; 15 projects selected for BIM (3D) coordination reached by end 2019; target: from 2021 major projects of CAD 50 M and more in BIM (3D) coordination, from 2023 projects of CAD 10 M and more with PCI and BIM coordination; 4D/5D/7D uses in exploration from 2023-2024 (deployment from the following year), 6D (sustainability) exploration 2024-2025 and deployment planned 2025-2026 [10] (QA re-read of the SQI page; the 15 projects were selected for BIM 3D coordination against a 2021 target and the page says it was reached at end 2019). The page presents these as targets, so the contractual force is unclear.

**SQI tools** [9] (the page warns that tender documents prevail and tools may change):
- Guide d'application du BIM a la SQI (RF-GP-030.043); Cahier des exigences BIM de projet (FR-GP-030.079)
- Appendice A Glossaire BIM (RF-PI-020.001); B Dictionnaire des usages BIM (RF-PI-020.002); C Niveaux d'information requis (RF-PI-020.003)
- Gabarit Plan d'execution BIM (PEB, DOCX, FR-GP-040-013); Gabarit Grille des responsabilites detaillees (GRD, XLSX)
- Guide des services BIM v1.1; Guide d'application du PCI; Plan d'action PCI v7
- No IFC, Uniformat or OmniClass mention on that page. Whether the PDF "exigences BIM" requires IFC is **unverified**; testers should read the PDF before asserting it.

Other: Canadian federal PSPC requires IFC according to Wikipedia [2] (not Quebec-specific). buildingSMART Canada exists [2].

## 5. North and West Africa

- **BIM Africa** is a not-for-profit community (advocacy, education, research, community); publishes "The Future of BIM in Africa - 2024 Report"; events include BIM Africa Summit, Awards, and **BIM Day Tunisia** (first edition June 2025, with SMU MedTech) [17]. The site did not mention Morocco, Algeria, Senegal or Cote d'Ivoire [17].
- English Wikipedia lists reference titles such as "Driving digital transformation in West African construction sector" and "BIM Institute - Africa's voice for BIM" but no body text for these countries [2].
- Morocco, Algeria, Tunisia (government mandates), Senegal, Cote d'Ivoire: **no verified national mandate, ministry document, or buildingSMART chapter found**. Do not state any. Typical reality (unverified): large foreign-funded or Gulf/European-led projects impose BIM through the client's own requirements, while national authorities have studies and working groups but no IFC rule.

## 6. IFC and openBIM tools relevant to these markets

| Tool / service | What it is | Source |
|---|---|---|
| IfcOpenShell | Open-source (LGPL) IFC library, C++/Python; supports IFC2x3-IFC4x3 parsing; modules ifcopenshell.api, ifcclash, ifcdiff, ifcpatch; Bonsai (ex-BlenderBIM) add-on for Blender (GPL) | [18] |
| buildingSMART Validation Service | Open-source web app; checks syntax, schema, normative rules (Gherkin rules); bSDD check listed but disabled | [21] |
| IDS (Information Delivery Specification) | XML standard (XSD schema) defining IFC requirements checkable by machine | [19] |
| bSDD | Online dictionary of classifications, properties, units, translations; REST API; classifications can be published by registered organisations | [20] |
| IFC4.3 (ISO 16739-1:2024) | 4.3.2.0 approved by ISO | [22] |
| KROQI | CSTB collaboration platform with IFC and BCF | [6] |
| Revit | IFC export via File > Export > IFC (open-source IFC exporter on GitHub); general knowledge, not fetched in this run | (unverified) |

French-origin software and platforms (BIMData, BIM&CO, Graphisoft/Archicad users, Visiativ/Arkance resellers): plausible but not verified here.

## 7. Local terminology table

| Native term | Transliteration / note | English |
|---|---|---|
| maquette numerique | - | digital mock-up = BIM model (IFC file or native) |
| modelisation des informations de la construction | AFNOR, XP P07-150 / NF EN ISO 19650 | building information modelling |
| bati immobilier modelise | official JO term, 29 Jan 2019 | modelled built property (official BIM synonym) |
| modelisation des donnees des infrastructures (MDI) | Quebec government term | BIM |
| convention BIM | - | BIM agreement / BIM execution plan (project-level) |
| charte BIM | - | BIM charter (company/owner-level principles) |
| cahier des charges BIM / cahier des exigences BIM | - | employer's information requirements (EIR) |
| Plan d'execution BIM (PEB) | Quebec | BIM execution plan |
| Grille des responsabilites detaillees (GRD) | Quebec | detailed responsibility matrix |
| niveau d'information requis | - | level of information need (LOIN) |
| coordinateur BIM / BIM modeleur | titles of 12 Jul 2019 | BIM coordinator / BIM modeller |
| processus de conception integree (PCI) | Quebec | integrated design process |
| BIM-Projektabwicklungsplan | Swiss German | BIM execution plan |
| BIM Nutzungsplan | Swiss German | BIM use plan |
| eBKP-H | Swiss | elemental cost classification, buildings |
| DOE (dossier des ouvrages executes) | France | as-built handover file (unverified usage detail) |
| reservations | France | openings / penetrations coordination |

Arabic terms for Maghreb texts are not verified; do not invent them.

## Typical questions people ask about this

No community threads could be retrieved (search unavailable), so all questions are illustrative.

1. What is the difference between the PTNB and the Plan BIM 2022? (illustrative)
2. Is BIM mandatory in French public procurement? (illustrative)
3. Does France require IFC4 or IFC2x3 for public projects? (illustrative)
4. What goes into a convention BIM and who signs it? (illustrative)
5. Can KROQI open and share IFC files? Does it support BCF? (illustrative)
6. Which coordinate system should an IFC model of a French site use (Lambert-93)? (illustrative)
7. How do I export IFC from Revit with a French template and French Psets? (illustrative)
8. Which MVD should I choose, Reference View or Design Transfer View? (illustrative)
9. What does SQI require in the "cahier des exigences BIM de projet" and is IFC required? (illustrative)
10. At what project value does the SQI require BIM coordination (CAD 50 M, then 10 M)? (illustrative)
11. What replaces the Government of Quebec roadmap after March 2026? (illustrative)
12. What is the Brussels Airport IFC-first policy and which IFC version does it use? (illustrative)
13. Which Swiss classification (eBKP-H) maps to IFC elements? (illustrative)
14. What does LOIN (SN EN 17412-1) mean for my model's detail? (illustrative)
15. Is there a BIM mandate in Morocco, Algeria, Tunisia, Senegal or Cote d'Ivoire? (illustrative)
16. How do I validate an IFC file with the buildingSMART validation service and IDS? (illustrative)
17. Can an MCP tool create a PEB or GRD from a template? (illustrative)

## Common pitfalls and misconceptions

- Assuming "France mandates BIM": the verified legal basis is an EU option that buyers *may* use [1]. Rules sit in each tender.
- Assuming Quebec requires IFC: the SQI pages read do not mention IFC [8][9][10].
- Treating the 2018 CNOA statistics as current [1].
- Confusing "maquette numerique" (a model, possibly native) with an IFC file.
- Using the dead PTNB name as the current plan; its successor in 2018 was Plan BIM 2022 [2]; post-2022 status unverified.
- Quebec thresholds (CAD 50 M, 10 M) are roadmap targets, not necessarily contract clauses [10].
- Expecting Maghreb/West Africa documents: none verified.
- Wikipedia's French IFC page is partly outdated (lists ISO 16739:2018, says few French users know IFC) [3].

## Gaps

- Web search was unavailable; no official French documents (Plan BIM 2022 guides, Code de la commande publique article, Mediaconstruct MVDs/PPBIM, AFNOR catalogue) were read. Next step: fetch mediaconstruct, batiment-numerique, legifrance, AFNOR by hand.
- Skipped suspicious site: the domain plan-bim-2022 (.fr) currently serves an online-casino page, not the Plan; not used and not linked.
- Not verified: French classification and Psets, Belgian regional rules, Swiss SIA 2051/KBOB, Quebec IFC requirement and the post-2026 roadmap, all five African countries' official policies, buildingSMART chapters in Maghreb/West Africa.
- Not downloaded: the Brussels Airport PDF, SQI PDFs, roadmap PDFs (reading pages only, by policy).

## Sources

1. https://fr.wikipedia.org/wiki/Building_information_modeling
2. https://en.wikipedia.org/wiki/Building_information_modeling
3. https://fr.wikipedia.org/wiki/Industry_Foundation_Classes
4. https://en.wikipedia.org/wiki/Industry_Foundation_Classes
5. https://en.wikipedia.org/wiki/ISO_19650
6. https://www.kroqi.fr
7. https://www.sqi.gouv.qc.ca/expertises/pratiques-integrees-bim-pci
8. https://www.sqi.gouv.qc.ca/feuille-de-route-gouvernementale-pour-le-bim
9. https://www.sqi.gouv.qc.ca/expertises/pratiques-integrees-bim-pci/outils-dencadrement-des-pratiques-bim-pci
10. https://www.sqi.gouv.qc.ca/expertises/pratiques-integrees-bim-pci/feuille-de-route-bim-pci-de-la-sqi
11. https://buildingsmart.be/
12. https://buildingsmart.be/brussels-airport-sets-new-standard-with-ifc-first-bim-policy/
13. https://buildingsmart.be/downloads-resources/
14. https://bauen-digital.ch/
15. https://bauen-digital.ch/publikationen/
16. https://bauen-digital.ch/themen/
17. https://www.bimafrica.org
18. https://github.com/IfcOpenShell/IfcOpenShell
19. https://github.com/buildingSMART/IDS
20. https://github.com/buildingSMART/bSDD
21. https://github.com/buildingSMART/validate
22. https://github.com/buildingSMART/IFC4.3.x-development
23. https://github.com/buildingSMART
