# Central and Eastern Europe: BIM/IFC requirements

## In plain words

Central and Eastern Europe (CEE) is not one BIM market. Czechia has the most advanced legal mandate: Act No. 330/2025 Sb. starts to bind selected public contracting authorities on 1 January 2027, and it is backed by a state-run Building Data Standard (DSS) whose geometry layer is IFC. Hungary already requires BIM, with IFC and BCF deliverables, for all state construction investments, introduced in stages by sector. Croatia's new Building Act puts BIM into statute, but the obligation starts only in 2031 and 2035. Poland, Slovakia, Romania, Ukraine and Greece have roadmaps, strategies or draft bills but no general statutory mandate. For Bulgaria and Serbia no official mandate was verified. For a tester of IFC/Revit MCP servers, the practical point is that "IFC delivery" is the common denominator everywhere, but national rules rarely pin an exact IFC version. Test requests should therefore ask for IFC4 (ISO 16739-1:2018) as the safe default and check the project's own EIR (Exchange Information Requirements) for specifics.

Last researched: 2026-11-06

Research notes: the web-search quota ran out mid-session, so Bulgaria, Serbia and Romania are thinly covered, and several PDFs could not be read as text. Facts below are tagged with source numbers [n]. Anything uncertain is marked "(unverified)". Facts labelled "general knowledge" come from the author's background knowledge of IFC and EPSG, not from the national documents.

## Region at a glance

| Country | Status as of Nov 2026 | Who | Key document | IFC-specific |
|---|---|---|---|---|
| Czechia | Statutory mandate from 1 Jan 2027 for selected public bodies and above-threshold works contracts | Ministry of Industry and Trade (MPO), Czech Agency for Standardization (ČAS) | Act No. 330/2025 Sb. [1][2][3] | DSS built on IFC; law itself does not name IFC [2][4] |
| Hungary | In force for all state construction investments, staged by sector | Ministry of Construction and Transport (ÉKM) | Decree 31/2024 (VIII. 22.) ÉKM [5] | IFC from original format plus BCF; no IFC version named [5] |
| Croatia | BIM in Building Act; mandatory only from 2031 / 2035 | Ministry of Physical Planning, Construction and State Property (MPGI) | Zakon o gradnji, NN 155/2025 [6] | IFC not mentioned in the law text read [6] |
| Slovenia | GZ-1 requires BIM from 2025 for demanding buildings with public-procurement investors (conference report) | Ministry of Natural Resources and Spatial Planning (MNVP, unverified role) | Gradbeni zakon (GZ-1) [7] | IFC (ISO 16739-1:2018), IDS, BCF named in industry material [8] |
| Poland | No general mandate; Pzp lets authorities require BIM | Ministry of Development and Technology, UZP | Roadmap 2020; Pzp art. 69 [9][10][11] | Open formats such as IFC can be required without tool access [12] |
| Slovakia | Strategy being prepared; no mandate | Office for Spatial Planning and Construction (ÚPV SR) | Press release 22 Oct 2024 [13] | Formats to be defined in the strategy [13] |
| Romania | Roadmap (2022) targeting BIM level 2; status of formal adoption unclear | MDLPA and others | National Roadmap for BIM Implementation [14][15] | None found |
| Bulgaria | Nothing official verified | (unverified) | None found | None found |
| Serbia | No mandate found | Institute for Standardization (ISS) active in BIM standards | ISS BIM overview [16] | None found |
| Ukraine | Concept 2021, bill No. 6383 passed first reading only | Ministry for Development (Mindev, later Ministry of Recovery) | Concept of 17 Feb 2021 [17][18][19] | None found |
| Greece | National BIM Strategy approved 7 June 2024; no mandate found | Ministry of Infrastructure and Transport | National BIM Strategy [20][21] | None found |
| EU level | Proposal only (COM(2026) 590): BIM required for works of EUR 25 million or more | European Commission | Public Procurement Act proposal, art. 65 [22][23] | "Open, interoperable formats" [23] |

## Czechia

### Mandate and scope

- **Act No. 330/2025 Sb., o správě informací o stavbě a vystavěném prostředí** (Act on management of information about a building and the built environment, the "BIM law"). Published in the Collection of Laws on 9 September 2025 per secondary sources; main obligations apply from **1 January 2027** [1][2][3].
- **Who is bound.** Selected public contracting authorities: state organisational units, state contributory organisations, state enterprises, regions and organisations they establish (Adeon explainer, § 3 to § 5). Municipalities are not automatically covered. The authority must own the building or hold the right to manage it, and the building must be in the cadastre or the regional digital technical map [2]. Exemptions in § 5 apply. The EU Public Buyers Community article names Ministries of Defence, Interior and Justice projects and projects abroad as excluded [3].
- **Threshold.** Above-threshold (nadlimitní) works contracts. For 2026 and 2027 the limit used is **CZK 134,764,000 excluding VAT** of estimated contract value [2]. The EU article rounds it to "CZK 135 million" [3]. One trade site claims "all public projects over 135 million", which is a simplification [1].
- **Deliverables.** An information model of the building (IMS, informační model stavby) kept in a common data environment (CDE) with an API and tamper-evident transaction records. Information containers cover permitting, execution and completion (§ 7(2)(a) to (c)) and handover, use and maintenance (§ 7(2)(d)) [2].
- **Transitional rule (§ 18).** If permit documentation was prepared before 1 Jan 2027 and the construction tender starts within five years, the model and containers (a) to (c) are not required. The model and container (d) are still needed no later than handover [2].
- **Later dates.** 1 Jan 2030: chapter III, the basic model of the built environment. A municipality may adopt it voluntarily from then. 1 Jan 2032: § 7(2)(e) and (3) for selected acquired or changed buildings [2].
- **Control and sanctions.** MPO is the supervisory body and deals with sanctions; ČAS helps contracting authorities prepare [24].
- **Implementing decree (prováděcí vyhláška).** As of Sept to Oct 2026 it was in the legislative process and not yet published [2][24]. ČAS reported final work on it on 24 Sept 2026 [2].
- **Policy background.** The government adopted the BIM concept in 2017, updated it on 24 July 2024, and approved the draft law in November 2024. A follow-up strategic document for 2028 to 2037 is due by the end of 2026 [25][26]. Earlier materials mention government resolution No. 41/2021 on the schedule (as reported) [4].

### IFC, DSS and standards

- **Datový standard staveb (DSS)**, formerly "Datový standard stavebnictví", is the national structure for building data: Architecture, Content and Governance parts. Geometry is exchanged as IFC. Properties per element type are defined by name, definition, unit and format, and depend on phase, classification, role and use (62 uses analysed in the 2020 article). It stores property lists only, not values, and is not a product library [4].
- **Early policy (2019 article, historical):** the plan was that an IFC information model built to the data standard would be the main condition, secured by a BIM protocol (contract annex) and a CDE [27]. This was the pre-law design, not today's text.
- **Milestones of DSS.** Document "Architektura datového standardu staveb" v0.9 (12 Feb 2026) [28]. Minimum data standard for permitting and occupancy added in April 2026; minimum standard for construction execution (earthworks, structures, building services, electrical) in early July 2026; minimum standard for the handover/use/maintenance container announced 12 Oct 2026 [24][29][30]. DSS is required for creating digital building models from 1 Jan 2027 [24].
- **Tools.** Web portal **dss.koncepcebim.gov.cz** (login via Identita občana) with an open API [24]. The state app **comBIMe** (gov.cz) ties purposes of use (účely užití) to regulation; templates cannot be created freely, missing ones are reported to ČAS [31]. The data dictionary is to be updated twice a year [31].
- **IFC version.** No IFC version was found in the sources read. ČSN ISO 16739 adopts IFC4 as the Czech national standard [32]. Use IFC4 as the working assumption and check the EIR (unverified for DSS).
- **Validators.** Validators check whether an IFC model contains the DSS-required data. As of the 2020 article no electronic checking existed and tests with CAD vendors were ongoing [4]. Current validator names are not verified.
- **Classification.** CCI (Construction Classification International), based on CCS and CoClass, is promoted on the Koncepce BIM site; the Prague Airport case is cited [4][29]. It is not part of DSS but needed in practice.
- **Methodologies (pilot versions, 19 Dec 2025):** "5.2 Metodika a smluvní rámec pro zadávání veřejných zakázek s využitím BIM", "5.5 Metodika modelování pro vybrané účely užití" with annexes (including base quantities and quantity accuracy), "5.6 Aktualizace souboru stávajících metodik" (catalogue of BIM goals, purposes of use), "5.7 Pravidla pro výměnu informací, které nemohou být umístěny v rámci řešení CDE" [33].
- **Standards referenced by practitioners.** EN ISO 19650 and follow-on standards [31]. The law does not name ISO 19650; its binding status depends on the ÚNMZ list and contract terms [2].
- **Portals and sites.** koncepcebim.gov.cz (run by ČAS and MPO), FAQ at dap.agenturacas.gov.cz [29].

### Key organizations (Czechia)

- ČAS (Česká agentura pro standardizaci), MPO (Ministerstvo průmyslu a obchodu), ÚNMZ (standards body), Czech Office for Surveying, Mapping and Cadastre (ČÚZK, co-prepared the draft law) [26].
- buildingSMART Czech Republic supports education, certification and engagement [3]. A direct fetch of its website failed (certificate error), so no further detail is given.
- Local enthusiasts and vendors (community, not official): Stavario, a Czech CDE-style tool, publishes a readiness checklist for 2027 [34].

## Hungary

- **Decree 31/2024. (VIII. 22.) ÉKM rendelet** on conditions for BIM-based design and technical implementation (építményinformációs modell, BIM) for state construction investments, issued under Act LXIX of 2023 (Ábtv.). Consolidated version 1 Jan 2026 [5].
- **Scope.** All state construction investments (new builds, reconstruction, extension, renovation, demolition), clients, participants, permit authorities, owners and operators across the lifecycle. **No monetary threshold** (§ 9). Individual items outside the unified item catalogue are limited to 0.5% (§ 7(3)) [5].
- **Staged application (§ 22(1))** for procedures started after: building and road works from entry into force; **rail 1 July 2026; water 1 July 2027; utilities 1 July 2028**. State facilities without a model must get one by 31 Dec 2035 (§ 22(2)) [5].
- **Documents.** EIR is prepared by the client as part of the tender documents (annex 1); pre-BEP at tender, BEP after contract (§ 17). Use cases are coded 010 to 250 (annex 2) [5].
- **IFC.** IFC is defined as an open, standardised model-based format, with **no version stated**. BCF is defined as the open issue exchange format. **Delivery (§ 20(2))**: (a) IFC saved from the original format, (b) a BCF project with metadata, (c) native files and other data per the EIR. Acceptance only on delivery of a complete usable data set (§ 20(1)) [5].
- **CDE.** Defined in § 3. § 19 (CDE requirements) enters into force on **1 July 2028** (§ 21(2)) [5].
- **Authorities.** The minister publishes the unified item catalogue, BIM levels (§ 16), EIR templates (§ 18(3)) and guidance on the government investment portal, run with KTI [5].
- **Caution on related decree.** Decree 27/2025 (VIII. 28.) ÉKM concerns operation of state-investment buildings and operator selection; the text read does not mention CDE, IFC or BCF. A recruitment website linked the 2028 CDE date to 27/2025, which does not match the text of 31/2024 § 19 [35][5].
- **Market reality.** A May 2026 article says BIM-based design of state investments has not spread widely because of regulatory gaps [36].
- **Local software.** Graphisoft (Budapest) Archicad: perpetual licences are being phased out in favour of subscription in 2026; Graphisoft took over sales from resellers in Hungary; MEP Designer on Archicad is promoted with IFC support [36]. Graphisoft's Hungarian help pages cover "IFC-vel végzett műveletek" (working with IFC) [37].
- **buildingSMART Hungary:** direct fetch failed; no details verified.

## Poland

- **No general BIM mandate** as of March and later 2026 sources [10][12].
- **Legal hook: Prawo zamówień publicznych (Pzp, Act of 11 Sept 2019), art. 69 ust. 1.** Authorities may require offers and design contest entries to be prepared with electronic building-data modelling tools or similar, if those are not generally available; ust. 2 requires alternative access. Requiring a proprietary format such as .rvt triggers the access duty; an open format such as .ifc does not [12]. Art. 103 lists project documentation and STWiORB (or PFU in design-and-build) as description means; BIM is not among them [38].
- **Proposed amendment (BIM Klaster, Sept 2024):** add the BIM model as an optional description method in art. 103 and art. 102. Voluntary for authorities. Final approval stage among partner organisations as of June 2025 [38].
- **Roadmap.** "Mapa drogowa dla wdrożenia metodyki BIM w zamówieniach publicznych" (2020, Ministry of Development, project "Cyfryzacja procesu budowlanego w Polsce", prepared by PwC) [9][11]. It proposed mandatory BIM for large contracts from 2025 and for all public works from 2030, but never became law. **The threshold is reported inconsistently: EUR 410 million in one source [10], EUR 10 million in another [12] (unverified, check the roadmap PDF).**
- **Ministry follow-ups.** BIM working group at the Ministry of Development and Technology (March 2022). "SMART report" (Oct 2024), proposing a BIM implementation team, BIM level 2 information requirements for public works contracts from 2026, a 2025 to 2030 financing plan and open IFC data standards by end 2026 (as reported; not adopted) [10].
- **Standards.** BIM Standard PL 2.0 (2020): ISO 19650-aligned handbook with EIR, BEP, MPDT and MIDP templates and LOD descriptions. Supported by PZITB, SARP, PZPB; UZP reviewed it positively. Voluntary [10][12].
- **Old interoperability regulation.** A 2019 article noted the 12 April 2012 regulation on formats for electronic documents did not list .ifc [39]. It may be outdated; unverified today.
- **Pilots.** Józef Piłsudski Museum, Sulejówek (2014, first tender with BIM requirements); GDDKiA Zator bypass (DK28), a BIM pilot with technical dialogue. A bid criterion awarded points for a reference BIM model "in correct IFC schema" [10][40].
- **PKP PLK and other agencies:** no BIM guidelines were found (unverified).
- **Organizations.** buildingSMART Polska (Warsaw; "Technical Rooms" working groups; annual openBIM Poland conference; professional certification) [41]. Others in the 2025 consultation: Izba Architektów RP, PIIB, SARP, PZPB, PZITB, BIM Klaster, Stowarzyszenie BIM, Europejskie Centrum Certyfikacji BIM, Fundacja BIM MEETUP [38]. buildingSMART Professional Certification in Poland is delivered by authorised providers such as Man and Machine Software [12].
- **Classification:** no mandatory national BIM classification was found (unverified).

## Slovakia

- Office for Spatial Planning and Construction (**Úrad pre územné plánovanie a výstavbu SR, ÚPV SR**) was established on 1 June 2022 and became the central authority on 1 Jan 2023. The spatial planning law **No. 200/2022 Z.z.** took effect 1 April 2024 and created a mandatory information system for planning; construction e-filing is voluntary [13].
- **22 Oct 2024:** ÚPV SR said it would ask the government by year-end for a mandate to develop a **Národná BIM stratégia**. Pillars: standards (naming, classification, scope of model content), adapting technical standards, technical requirements (CDE rules, file formats), **automated checking** of projects against information delivery specification rules, public procurement rules "from a certain value", pilot projects, research, training [13].
- **No mandate** and no IFC rule were found. The strategy explicitly does not change laws or procedures [13].
- Industry context: a survey reported 71 percent of designers think public administration is not ready (undated) [42]. An epravo article points to the absence of clear legal regulation of information models (not read in full) [43].
- Czech documents are often used in practice by Slovak teams (informal observation, unverified).

## Romania

- **National Roadmap for BIM Implementation in investment projects financed from public funds.** A Ministry of Development, Public Works and Administration (MDLPA) document submitted to the Ministry of Investments and European Projects and the head of ANAP for approval. Linked to the Renovation Wave component of the recovery plan (PNRR) [14]. One academic source says the memorandum was signed in September 2022 and sets BIM level 2 as the starting level; the EU Transition Pathways page says the roadmap was still being approved. Treat adoption status as conflicting [14][15].
- A governmental committee implements it. Measures include BIM occupations in the national occupation framework and training for public servants [15].
- **Mandate date.** An association press release claims 2028 is the deadline for mandatory BIM in public projects. No legal instrument is cited (unverified) [44].
- **Practice.** CNIR (national road agency) put BIM requirements into the feasibility-study specification of the București–Giurgiu expressway [45].
- No IFC-specific rule was found.
- Civil society: Asociatia BIMtech, Leviatan Association [44][46].

## Bulgaria

No official BIM mandate, ministry document or Bulgarian IFC requirement was verified. Searches in Bulgarian returned only other countries. Suggested direct checks for a human: mrrb.bg (Ministry of Regional Development and Public Works), aop.bg (public procurement portal) and the State Gazette (unverified suggestions). Do not assume a Bulgarian mandate in test scenarios.

## Slovenia

- **Gradbeni zakon (GZ-1).** Adopted December 2021 [8]. A conference report says that from **2025** project documentation must be prepared using BIM tools for new construction of demanding buildings, including environmentally significant ones whose investors are contracting authorities under public procurement law [7]. A pre-2025 paper cites art. 39(9) as the basis (unverified) [47].
- **Open standards named in industry material:** IFC (ISO 16739-1:2018), IDS and BCF (presentation by Matjaž Šajn for public administration, 2024) [8]. The PDF could not be read as text, so this comes via search snippets.
- **Guidance.** "BIM Smernice za modeliranje" (BIM modelling guidelines, version 3, 2023) covers IFC use in permitting; the issuing institute is reported as the Jožef Stefan Institute (unverified) [48].
- buildingSMART Slovenia and GZS (Chamber of Commerce) pages host material [8][48]. The Slovenian procurement mandate for BIM could not be confirmed.
- Search found no evidence for a "ZGO-2" law despite the seed hint.

## Croatia

- **Zakon o gradnji (Building Act), NN 155/2025**, proclaimed 18 Dec 2025, published 23 Dec 2025, in force 1 Jan 2026 [6].
- **Art. 3(1) item 1** defines BIM as information modelling of a building and/or construction, organising and digitising information through BIM models.
- **Art. 30(3):** "Projects are prepared in a BIM environment for all buildings, except less complex buildings" and works buildable without a permit. Less complex building (Art. 3(1) item 32): residential building with up to two dwellings and up to 400 m2 gross floor area, or agricultural building up to 600 m2 [6].
- **Start dates (Art. 162):** Art. 30(3) applies from **1 January 2031** for buildings whose permits the Ministry issues and **1 January 2035** for permits issued by local administrative bodies [6]. Read through a summarising fetch tool; verify in the official text.
- **Rulebooks.** The Minister must adopt rulebooks under Art. 30(5)(6) within 90 days of entry into force (Art. 156). Existing rulebook on project content and equipment (NN 118/19, 65/20) stays until replaced [6]. BIM detail (IFC etc.) is expected in rulebooks, not in the Act (unverified).
- **Platforms.** eDozvola, the electronic permit system (Art. 47, 48, 51, 77) [6]. MPGI upgraded its **hrBIM** platform with an urban/infrastructure project module (TED notice of 30 April 2026; contract concluded 27 April 2026) [49].
- HR BIM TaskGroup and HKIG guidance work date from 2019 [50]. buildingSMART Croatia: not verified.

## Serbia

- BIM Serbia association founded April 2017 in Belgrade (academic source) [51].
- The Institute for Standardization of Serbia (ISS) published an overview of national, international and European BIM standardization bodies and Serbian standards on BIM terms (26 pages; not readable as text here) [16].
- No mandate, no link to the Law on Planning and Construction or to CEOP (central register of unified procedures) was verified. Serbian BIM-related legislation: unverified.

## Ukraine

- **Concept for implementing BIM in construction**: approved by the Cabinet on 17 Feb 2021 (order number 152-r in search snippets, unverified). Stage 1 (2021 to 2022): amend legislation, harmonise standards, national classifiers, training. Stage 2 (2023 to 2025): update building codes (DBN), pilot projects covering at least 10 percent of state-funded projects [17][19].
- **Dec 2020:** Mindev announced the concept and said amendments already allowed BIM in design documentation and electronic submission; 20 DBN being updated [18].
- **Bill No. 6383** (BIM across the facility lifecycle). Passed first reading in July 2022. Amends urban planning, architecture, procurement and building-code laws; BIM would become mandatory five years after entry into force for certain state-funded objects [19]. In Oct 2024 work was under way toward second reading with the Ministry of Recovery [52]. On 23 Sept 2025 it was discussed in a Rada subcommittee; no adoption reported [53].
- **Pushback.** The National Union of Architects estimated at least 30 percent higher design costs and cited Prozorro lowest-price criteria as a barrier [53].
- IFC or open-format requirements: none found.
- Recovery context: BIM and the DREAM system are discussed for state or donor-funded reconstruction [52].

## Greece

- **National BIM Strategy** approved on **7 June 2024** by Minister of Infrastructure and Transport Christos Staikouras after public consultation. Measures: standards and legislative changes, training of public staff, BIM hub on yme.gr, and "BIM Roadmap in Greece including pilot projects" with DG REFORM (TSI 2023). Gradual adoption, SME emphasis [20][21].
- No thresholds or open-format rules are in the sources read. A commentary citing a "EUR 25 million, Article 65" requirement most likely refers to the EU proposal (below), not to a Greek law. This is an inference (unverified) [54][23].

## EU level: Public Procurement Act proposal

- **COM(2026) 590 final**, 9 Sept 2026, proposal for a Regulation on public contracts and concessions (procedure 2026/0265 (COD)). It would replace Directives 2014/23, 24 and 25 and apply two years after entry into force (Art. 149) [22][23].
- **Article 65, Building information modelling:** for works contracts of **EUR 25 million or more** public buyers must require BIM during execution. BIM means collaborative digital processes using **open, interoperable formats**. Derogations for disproportionate burden or security reasons. The Commission may lower the threshold by delegated act [23].
- It is a proposal and may change. National rules would be overridden for covered contracts only after adoption (assumption).

## IFC-specific practice for testers

| Topic | What the sources say | Practical default for tests |
|---|---|---|
| IFC version | Hungary and Czech law do not name one; Czech standard ČSN ISO 16739 = IFC4 [5][32]; Slovenia cites ISO 16739-1:2018 [8] | IFC4 (ISO 16739-1:2018), also test IFC2x3 import and IFC4.3 (ISO 16739-1:2024, general knowledge) |
| MVD | None of the national documents read names an MVD | Reference View vs Design Transfer View (general knowledge) |
| Property sets | Czech DSS defines property lists by phase, classification, role and use [4]; Czech base quantities annex [33] | Pset_WallCommon etc. plus custom Pset names; ask the model to check DSS-style property completeness |
| Classification | Czech CCI [4]; Slovak strategy plans rules [13]; Polish none found | Expect classification as IfcClassificationReference |
| Georeferencing | Not covered in the sources read | IfcMapConversion plus IfcProjectedCRS in IFC4 (general knowledge). Typical EPSG codes (general knowledge, verify): Czechia S-JTSK 5514; Poland PL-1992 2180, PL-2000 2176 to 2179; Hungary EOV 23700; Slovenia D96/TM 3794; Croatia HTRS96/TM 3765; Romania Stereo 70 3844; Greece GGRS87 2100; Bulgaria CCS2005 7801 |
| Delivery | Hungary: IFC + BCF + native per EIR [5]. Czechia: IMS in CDE with API [2] | Request IFC export plus BCF issues |
| Checking | Czech validators for DSS [4]; Slovak automated checking planned [13]; IDS named in Slovenia and Poland [8][12] | Use IDS files for rule checks (IDS is a buildingSMART standard) |
| Naming and language | Czech: terminology translation is a practical problem [31] | Test non-English property names and diacritics |

## Local terminology

| Native term | Transliteration | English |
|---|---|---|
| informační model stavby (IMS) | informační model stavby | information model of a building (Czech law) |
| digitální model stavby (DiMS) | digitální model stavby | digital (3D) building model, geometric subset [31] |
| datový standard staveb (DSS) | datový standard staveb | building data standard |
| společné datové prostředí | společné datové prostředí | common data environment (CDE) |
| zadavatel | zadavatel | contracting authority |
| nadlimitní veřejná zakázka | nadlimitní veřejná zakázka | above-threshold public contract |
| építményinformációs modell | építményinformációs modell | building information model (Hungary) |
| közös adatkörnyezet | közös adatkörnyezet | CDE |
| építtető / tervező / kivitelező | építtető / tervező / kivitelező | client / designer / contractor |
| modelowanie informacji o budynku (BIM) | modelowanie informacji o budynku | building information modelling (general knowledge) |
| zamawiający | zamawiający | contracting authority (Poland) |
| program funkcjonalno-użytkowy (PFU) | program funkcjonalno-użytkowy | functional-utility programme (design-and-build) |
| STWiORB | STWiORB | technical specifications for execution and acceptance of works |
| informačný model stavby / spoločné dátové prostredie | informačný model stavby | information model of a building / CDE (Slovak, general knowledge) |
| Národná BIM stratégia | Národná BIM stratégia | National BIM strategy |
| informacijsko modeliranje gradenj | informacijsko modeliranje gradenj | BIM (Slovenia, general knowledge) |
| BIM okruženje / glavni projekt / idejni projekt | BIM okruženje | BIM environment / main design / conceptual design (Croatia) |
| информационо моделирање објеката | informaciono modelovanje objekata | BIM (Serbia) [16] |
| інформаційне моделювання будівель (ВІМ) | informatsiine modeliuvannia budivel | BIM (Ukraine) |
| τεχνολογία μοντελοποίησης (BIM) | technologia montelopoiisis | BIM, "modelling technology" (Greece, wording from news [21]) |
| Modelarea Informațiilor Construcțiilor | modelarea informațiilor | BIM (Romania, general knowledge) |
| информационно моделиране на сгради | informatsionno modelirane na sgradi | BIM (Bulgaria, unverified) |

## Typical questions people ask about this

1. Od kdy začne nový zákon platit? (When does the new Czech law apply?) Real FAQ heading [34]. Answer: 1 Jan 2027 [2].
2. Týká se povinnost všech stavebních firem? (Does it apply to all construction companies?) Real FAQ heading [34]. Answer: no, only selected public bodies and above-threshold contracts [2][24].
3. Musí mít každá stavební firma vlastního BIM manažera? Real FAQ heading [34].
4. Je BIM a CDE to samé? Real FAQ heading [34].
5. Does the Czech BIM law require IFC? (illustrative) The law text as summarised does not name IFC; DSS is IFC-based [2][4].
6. Which Czech threshold applies in 2027? (illustrative) CZK 134,764,000 excluding VAT [2].
7. Is BIM mandatory in Poland for public tenders? (illustrative) No general mandate [10][12].
8. Czy zamawiający może wymagać BIM w przetargu? (illustrative) Yes under Pzp art. 69, with access rules; open IFC does not need tool access [12].
9. Does Hungary have a minimum project size for BIM? (illustrative) No value threshold; all state construction investments [5].
10. Which Hungarian sectors need BIM and from when? (illustrative) Rail 1 July 2026, water 1 July 2027, utilities 1 July 2028 [5].
11. What files must a Hungarian designer deliver? (illustrative) IFC from original, BCF project, native files per EIR [5].
12. When does BIM become obligatory in Croatia? (illustrative) Art. 30(3) from 2031 and 2035 depending on permit authority [6].
13. Is BIM mandatory in Slovenia? (illustrative) From 2025 for demanding buildings with procurement-law investors [7]; check GZ-1.
14. Does Slovakia have a BIM mandate? (illustrative) No, only a national strategy in preparation [13].
15. Is the Ukrainian BIM bill in force? (illustrative) No; passed first reading only as far as found [19][53].
16. Is the EUR 25 million BIM rule in Greece or the EU? (illustrative) EU proposal art. 65 [23].
17. Which IFC version should I use for Central European projects? (illustrative) IFC4 unless the EIR says otherwise [32][8].
18. How do I check an IFC against Czech DSS property requirements? (illustrative) Use the DSS portal export and a validator [4][24].
19. Which coordinate system do I put in IfcProjectedCRS for Polish projects? (illustrative) EPSG:2180 or 2176 to 2179 (general knowledge).
20. Where do I find the Romanian BIM roadmap? (illustrative) See [14][15]; adoption status unclear.

## Common pitfalls and misconceptions

- **"BIM is mandatory in the whole EU region."** No. Only Czechia (from 2027), Hungary (state investments) and, far in the future, Croatia have statutory duties found here; Poland, Slovakia, Romania, Ukraine and Greece do not.
- **"The Czech law requires IFC."** The summaries do not mention IFC by name; the DSS and national standards carry the IFC link [2][4]. Check the final implementing decree when published.
- **Czech threshold confusion.** The limit is above-threshold works contracts of selected authorities, about CZK 135 million excluding VAT [2][3], not every public project over CZK 135 million.
- **Mixing Hungarian decrees.** 31/2024 is the BIM decree; 27/2025 concerns operation. CDE rules start 1 July 2028 [5][35].
- **Croatia's dates.** 2026 is when the Act took effect, not when BIM becomes mandatory (2031 and 2035) [6].
- **Polish roadmap numbers.** The 2025 and 2030 targets never became law; sources disagree on the threshold [10][12].
- **EU proposal is not law.** Art. 65 is a Commission proposal [22][23].
- **Pre-law Czech articles (2019, 2020)** describe plans (reference date 1 Jan 2022) that were superseded [4][27].
- **Date conflicts.** Czech DSS user-interface release is dated both Jan 2026 and end of 2025 in one source [24].

## Gaps

- Bulgaria: no verified official information. Serbia and Romania: only partial. Search quota ran out before targeted queries for these.
- Unreadable PDFs: Slovenian BIM presentation and guidelines, Slovak/Czech DSS strategy PDF, Polish roadmap PDF, Serbian ISS overview, Romanian methodology, Hungarian cdn.kormany.hu PDF. Their content is not used except through search snippets.
- buildingSMART chapter list page returned HTTP 403; Czech, Hungarian chapter sites failed on certificates.
- Not verified: IFC version in the Czech DSS, current Czech validator names, Slovak, Romanian and Serbian classification systems, georeferencing rules in any national document.
- No suspicious or pirated sites were encountered; none linked.

## Sources

[1] https://www.stavebniklub.cz/33/ceska-republika-zavadi-povinne-vyuzivani-bim-pro-velke-verejne-stavebni-projekty-od-roku-2027-uniqueidgOkE4NvrWuOKaQDKuox_Z3Uv1YeJb3DwsJ6my9IQOkA/?query=BIM&serp=1 (search result, not fetched; simplification noted)
[2] https://www.adeon.cz/bim-zakon/ (vendor explainer, not the statute)
[3] https://public-buyers-community.ec.europa.eu/communities/bim-and-public-procurement/news/czech-republic-adopts-bim-mandate-major-public
[4] https://www.tzb-info.cz/bim-informacni-model-budovy/20190-co-je-datovy-standard-stavebnictvi-dss (5 Feb 2020)
[5] https://njt.jog.gov.hu/jogszabaly/2024-31-20-8X
[6] https://narodne-novine.nn.hr/clanci/sluzbeni/full/2025_12_155_2316.html
[7] https://www.tax-fin-lex.si/dokument/podrobnosti/7b8fa287-7021-42ad-8da7-c49c21d7465c (conference report)
[8] https://www.gzs.si/Portals/Panoga-Gradbenistvo/BIM za javno upravo Megra 2024 - Matjaž Šajn.pdf (via search snippet)
[9] https://www.gov.pl/web/rozwoj-technologia/cyfryzacja-procesu-budowlanego-w-polsce--zakonczenie-projektu
[10] https://barvea.com/en/blog/bim-mandate-public-procurement-poland (vendor blog, Mar 2026)
[11] https://inzynierbudownictwa.pl/bim-w-zamowieniach-publicznych-w-polsce/ (search snippet)
[12] https://www.mum.pl/bim-a-polskie-prawodawstwo-jak-sie-certyfikowac (vendor/training site)
[13] https://uupv.sk/storage/app/media/Tlacove%20spravy/2024/1729597725-7641-2024_10_22_TS_N%C3%A1rodn%C3%A1%20BIM%20strat%C3%A9gia.pdf
[14] https://psc.ro/files/docs/METODOLOGIEBIM2022.pdf (unreadable; via search snippet)
[15] https://transition-pathways.europa.eu/construction/pledges-commitments/national-roadmap-bim-implementation-romania
[16] https://iss.rs/en/download/page-section/document/9626 (via search snippet)
[17] https://www.kmu.gov.ua/news/uryad-zatverdiv-koncepciyu-vprovadzhennya-v-ukrayini-vim-tehnologij-u-budivnictvi
[18] https://www.kmu.gov.ua/news/bim-tehnologiyi-pidvishchat-yakist-budivnictva-v-ukrayini
[19] https://www.kmu.gov.ua/news/oleksii-chernyshov-vr-pryiniala-u-pershomu-chytanni-zakonoproekt-shchodo-vprovadzhennia-bim-tekhnolohii-u-budivnytstvi
[20] https://www.cnn.gr/oikonomia/anaptyxi/story/423231/egkrithike-i-ethniki-stratigiki-gia-tin-efarmogi-tis-texnologias-montelopoiisis-stis-kataskeves
[21] https://www.parapolitika.gr/politiki/article/1405125/staikouras-egrithike-i-ethniki-stratigiki-gia-tin-efarmogi-tis-tehnologias-modelopoiisis-bim-ton-ergon/
[22] https://single-market-economy.ec.europa.eu/publications/proposal-regulation-public-contracts-and-concessions_en
[23] https://www.publicprocurementact.com/article-65/ (unofficial text site; compare with the Commission PDF)
[24] https://stavba.tzb-info.cz/30186-cas-rozsirila-datovy-standard-stavby-a-dokoncila-dalsi-milnik-zavadeni-bim-v-cesku (13 Aug 2026)
[25] https://www.tzb-info.cz/bim-informacni-model-budovy/27787-aktualizace-bim-a-navrh-zakona-o-sprave-informaci-o-stavbe-a-vystavenem-prostredi (29 Nov 2024)
[26] https://koncepcebim.gov.cz/wp-content/uploads/2024/09/2024-aktualizace-koncepce-bim-schvalena.pdf (search result, not read)
[27] https://www.pravniprostor.cz/clanky/ostatni-pravo/povinnost-bim-postupny-nabeh (Dec 2019, historical)
[28] https://koncepcebim.gov.cz/dokumenty/
[29] https://koncepcebim.gov.cz/
[30] https://www.ceskestavby.cz/clanky/cas-rozsirila-datovy-standard-stavby-a-dokoncila-dalsi-milnik-zavadeni-bim-v-cesku-36313.html (search result)
[31] https://www.zememeric.cz/pouzivani-metody-bim-od-ledna-2027-diskuze/ (trade press discussion, Sept 2026)
[32] https://www.tzb-info.cz/bim-informacni-model-budovy/11696-nova-norma-bim-pro-sdileni-dat-ve-stavebnictvi-a-ve-facility-managementu (search snippet)
[33] https://koncepcebim.gov.cz/dokumenty/ (list of pilot methodologies, same page as [28])
[34] https://www.stavario.com/cs/bim-2027 (vendor page, community)
[35] https://njt.jog.gov.hu/jogszabaly/2025-27-20-8X
[36] https://www.economx.hu/ingatlan/2026/05/26/a-graphisoft-megvaltoztatna-a-magyar-epiteszet-tortenetet/
[37] https://help.graphisoft.com/AC/30/HUN/Topics/121_IFC/121_IFC-1.html (search result)
[38] https://builderpolska.pl/2025/06/24/cyfrowe-budownictwo-potrzebuje-nowego-prawa/
[39] https://inzynierbudownictwa.pl/bim-obowiazek-czy-mozliwosc-stosowania-bim-w-prawie-zamowien-publicznych/ (older article)
[40] https://www.archiwum.gddkia.gov.pl/pl/d/a6f530eebe90c18cd5f1e6e63f11e56b (search snippet)
[41] https://buildingsmart.org.pl/
[42] https://sita.sk/verejna-sprava-nie-je-pripravena-na-digitalizaciu-stavebnictva-mysli-si-vacsina-projektovych-firiem/ (search snippet)
[43] https://www.epravo.sk/top/clanky/ostatne-pravne-odbory/?pg=19 (search snippet)
[44] https://agerpres.ro/ots/asociatia-leviatan-lanseaza-academia-excelentei-ca-obisnuinta-aeco-primul-centru-dedicat-adoptarii-b--660521 (press release, search snippet)
[45] https://www.agir.ro/univers-ingineresc/numar-16-2024/cnir-caietul-de-sarcini-pentru-studiul-de-fezabilitate-al-drumului-de-mare-viteza-bucuresti---giurgiu-include-modelarea-3-d-building-information-modelling-bim_8479.html (search snippet)
[46] https://financialintelligence.ro/asociatia-bimtech-sectorul-constructiilor-din-romania-are-nevoie-urgenta-de-introducerea-unor-standarde-moderne-de-lucru-si-este-in-urma-la-capitolul-digitalizare/ (search result)
[47] https://dlib.si/URN:NBN:SI:DOC-NUG1PQZR/EDM (search snippet)
[48] https://www.gzs.si/Portals/Panoga-Gradbenistvo/BIM_Smernice za modeliranje.pdf (not fetched successfully; search snippet)
[49] https://ted.europa.eu/en/notice/296689-2026/pdf (search snippet)
[50] https://www.hkig.hr/docs/Opatija_2019/prezentacije/Kvarner/4.%20BIM%20pristup%20u%20graditeljstvu/4.4.%20Predstavljanje%20smjernica%20za%20BIM_MMNahod.pdf (search snippet)
[51] https://zbornik.ftn.uns.ac.rs/index.php/zbornik/article/download/4332/3901/14596 (academic, via search snippet)
[52] https://news.dtkt.ua/society/economics/93693-bim-texnologiyi-u-budivnictvi-xocut-zrobiti-oboviazkovimi-dlia-okremix-objektiv (18 Oct 2024)
[53] https://interfax.com.ua/news/general/1107210.html (24 Sept 2025)
[54] https://www.powergame.gr/ikonomia/669550/kataskeves-prasino-stin-ethniki-stratigiki-me-technologia-bim/ (search result; the Article 65 commentary came from a LinkedIn post, not linked)
