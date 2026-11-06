# United Kingdom and Ireland: BIM/IFC requirements

## In plain words

The UK and Ireland are two separate jurisdictions with two separate BIM policies, but both are built on the same international process standard, **ISO 19650** (information management using BIM), and both name **Uniclass 2015** as the classification system. The UK (England-centred, central government) moved from a "Level 2 BIM mandate" (announced 2011, effective 2016) to a broader **Information Management Mandate** (2021) delivered through the **UK BIM Framework** (now branded the **IMI Framework**). Ireland has a newer, very concrete mandate: BIM requirements are written into public works contracts through the **Capital Works Management Framework (CWMF)**, rolled out in 12 dated milestones from 1 January 2024 to 1 January 2028, stepping down in project value from over EUR 100m to under EUR 1m. **Neither jurisdiction, in the sources I could read, prescribes one IFC version or MVD**: IFC is named as a core open standard, and the detail (versions, property sets, naming) is set per project in the client's information requirements (EIR) and BIM Execution Plan. For an MCP tester this means: expect IFC files in UK/Irish projects to carry Uniclass 2015 classification references, ISO 19650-style file naming and container statuses, and sometimes COBie spreadsheets, but the exact settings differ per project.

Last researched: 2026-11-06

> Research limits (read this first): the search budget was exhausted mid-task, several official pages returned HTTP 403 (gov.ie, buildingsmart.org, imiframework.org/faq), and several PDFs were unreadable. Items marked "(unverified)" come from search-result snippets, secondary sources or general knowledge and should be re-checked. See "Gaps".

---

## 1. United Kingdom

### 1.1 Policy timeline

| Year | Event | Source |
|---|---|---|
| 2011 | Government Construction Strategy: origin of the UK BIM mandate (BIM Level 2 on centrally procured projects) | [2] |
| 2016 | The original "UK BIM mandate" takes effect (collaborative 3D BIM, "Level 2", on centrally procured public projects) | [4], [5] |
| 2018 | "BIM Level 2" branding dropped; the framework is renamed the **UK BIM Framework** | [2] |
| 2019 | BS EN ISO 19650-1 and -2 published in the UK with a UK National Annex; BS 1192:2007+A2:2016 and PAS 1192-2:2013 withdrawn/superseded | (search snippet) [38] |
| 2020 | BIM Interoperability Expert Group report (March 2020) is referenced by the mandate text | [2] |
| 13 Sep 2021 | IPA publishes **Transforming Infrastructure Performance: Roadmap to 2030**; Annex B is the refreshed **Information Management Mandate**, "applicable immediately" and for the 10-year life of the plan | [2], [3] |
| Dec 2021 | UK BIM Framework updates guidance for the revised (2021) National Annex | (search snippet) [39] |
| Oct 2022 | UK BIM Alliance renamed **nima** | [9] |
| Nov 2024 | nima launches the **Information Management Initiative (IMI)**, backed by the Construction Leadership Council; the trade press says it replaces the 2021 mandate for the voluntary/sector side | [4] |
| 1 Apr 2025 | NISTA (National Infrastructure and Service Transformation Authority) launched; the mandates of NIC and IPA were "rolled forward" to it | [6] |

Whether NISTA has formally re-issued or replaced Annex B of the 2021 roadmap: **(unverified)**; I found no confirmation.

### 1.2 Who mandates what

- **Government client side (England-centred):** HM Treasury / Cabinet Office, via the Infrastructure and Projects Authority (IPA), now part of NISTA [2], [6]. The mandate sits in the roadmap, and public sector clients "should comply" as part of implementing the **Construction Playbook** (first published 8 Dec 2020, last updated 11 Jul 2023; central departments follow its 14 policies on a "comply or explain" basis) [3], [34].
- **Sector side:** nima (volunteer-led, not-for-profit) leads the IMI, and with BSI maintains the UK BIM Framework [7], [9]. IMI participants commit at top level and issue an internal mandate with five rules (capability, training, individual compliance, monitoring, sharing progress) [4].
- **Devolved administrations (Scotland, Wales, Northern Ireland):** their own BIM policies exist (for example via the Scottish Futures Trust), but I could not verify details (unverified).
- **Scope and thresholds:** the 2021 Information Management Mandate has **no value threshold** in the text I read; it sets requirements on clients (see 1.3). Do not invent a "GBP x million" threshold for the UK.

### 1.3 The Information Management Mandate: what clients must do (Annex B, point 8)

According to the roadmap text [2], clients must:

1. Make procurement and contractual processes comply with **UK BIM Framework** standards in force at the time of delivery.
2. Use the **ISO 19650-5** clause 4 sensitivity assessment to decide if a security-minded approach is needed; if so implement under ISO 19650-5 clauses 5 to 9.
3. Have the capability to carry out the information management function of ISO 19650-1 (in-house, external, or both).
4. Define information requirements under ISO 19650-2 and -3: **OIR, PIR, AIR, SIR** (security, where applicable) and **EIR**.
5. Have a digital mechanism to define requirements and to procure, receive, assure and store information immutably in a **system of record**.
6. Specify information requirements and their delivery fully in contract documents.
7. Apply the same governance and rigour to maintaining information (sharing, exploiting, regulatory availability).

The roadmap also says the mandate is expected to evolve towards the **Information Management Framework** (data interoperability) [2].

### 1.4 The UK BIM Framework / IMI Framework

- The UK BIM Framework was formerly called "BIM Level 2" (until 2018) [2]. The domain ukbimframework.org now redirects (HTTP 301) to **imiframework.org**, described as a set of standards, guidance and resources from **BSI and nima**, cited in the Construction Playbook, "Trust and Productivity" and the TIP Roadmap to 2030 [1].
- The site lists, per lifecycle stage: BS EN ISO 19650-1:2018, -2:2018, -3:2020, -4:2022, -5:2020, BS 8536 (2022), PAS 1192-6:2018 [1]. Guidance is hosted on the Morta app [1].
- **UK National Annex:** ISO 19650-1 and -2 are adopted as BS EN ISO 19650-1/-2 with a UK National Annex. The Annex is informative (does not override the base text), carries UK choices such as requiring **Uniclass 2015** as the ISO 12006-2 classification, and was revised in 2021 after feedback that the first (2018/2019) version did not perform as expected [39] (search snippets; exact Annex edition numbers **unverified**).
- **PAS 1192 history:** PAS 1192-2:2013 (capital/delivery phase), PAS 1192-3:2014 (operational phase), BS 1192:2007+A2:2016 (collaborative production, "BS 1192") were Level 2 documents; their concepts moved into ISO 19650-1 and requirements into -2, with unagreed items going into the National Annex [38]. PD 19650-0:2019 (transition guidance) is itself now withdrawn [38]. PAS 1192-6:2018 (health and safety information) is still listed by the IMI site [1].
- **BS 1192-4:2014** (COBie code of practice, "fulfilling Employer's Information Exchange Requirements using COBie") was published September 2014 and is closely aligned with PAS 1192-2 and ISO 16739 (IFC) [28]. Whether it is currently withdrawn: **(unverified)**.
- **Government Soft Landings (GSL)** (2012 onwards, handover/aftercare approach) and **BS 8536** (design for operability; the IMI site shows a 2022 edition) are part of the UK package [1]; GSL details **(unverified)** in this session.

### 1.5 IFC-specific requirements in the UK

What I could verify:

- The UK BIM Framework does not appear, in the pages read, to mandate a single IFC version or MVD. IFC (ISO 16739) is the open exchange format that BS 1192-4/COBie work was aligned with [28].
- NBS stated (2022) that it is working within the **Government and Industry Interoperability Group** on guidance for using **Uniclass in data transfer schemas such as COBie and IFC**; no completion date given [23].
- The **buildingSMART Data Dictionary (bSDD)** hosts Uniclass 2015 under an NBS namespace (`identifier.buildingsmart.org/uri/nbs/uniclass2015-1/`), so tools can look up Uniclass codes and map them to other systems [27].
- bSUKI publishes resources on **bSDD** and the **Information Delivery Specification (IDS)** (an XML schema `ids.xsd` for machine-checkable IFC information requirements) and lists IDS tools (IDS Editor, BIMcollab Nexus, xBIM, etc.) [32], [33].

Typical practice (general knowledge, **unverified in this session**; confirm per project EIR):

- Exchange formats stated in EIRs: **IFC2x3 Coordination View 2.0** (legacy default), increasingly **IFC4 Reference View**; deliverable pairs of native + IFC; **COBie UK 2012** spreadsheet for asset data (Level 2 legacy), or IFC property sets plus Excel.
- Classification in IFC: one `IfcClassification` (Name "Uniclass 2015", Source "NBS", Edition/date) and `IfcClassificationReference` per element, with Identification like `EF_25_10` (element/function) or `Ss_25_10_30` (system) or `Pr_...` (product).
- Georeferencing: UK British National Grid (EPSG:27700) with Ordnance Datum Newlyn heights; in IFC4+ via `IfcMapConversion` and `IfcProjectedCRS`; in IFC2x3 via site `RefLatitude/RefLongitude` and shared coordinates (unverified practice).
- File naming per ISO 19650-2 UK National Annex: fields separated by hyphens, typically Project-Originator-Volume-Level-Type-Role-Number (unverified exact field set; check the Annex).
- Containers with metadata statuses (WIP / Shared / Published / Archive) and suitability codes in the CDE (ISO 19650-2 concept; UK Annex defines suitability codes S0..S7 etc. -- unverified).

### 1.6 Classification: Uniclass 2015

- Owned and maintained by **NBS**; **free to download and use**; a suite of **12 tables**; API available; mapped to IFC 2x3 TC1 (relationship tables, not a file format) [24]. Quarterly updates; the latest I saw is the **April 2026 update** (second quarterly update of 2026, "improvements across six tables") [25].
- Tables (prefix: name): Co Complexes, En Entities, Ac Activities, SL Spaces/locations, EF Elements/functions, Ss Systems, Pr Products, TE Tools and equipment, PM Project management, FI Form of information, Ro Roles, Zz CAD [26] (first eight partly confirmed by NBS pages; Ss/Pr/TE/Ro/Zz names from general knowledge, **unverified**).
- Code pattern: `Table_Group_Subgroup_Section_Object`, e.g. `Ss_25_10_30` (the numbers/titles in the examples are illustrative; look up exact titles in NBS data).
- Uniclass 2015 is the UK implementation of the ISO 12006-2 framework, and the National Annex requires it for ISO 19650-2 classification [39].
- The **NBS BIM Toolkit** and the web **Digital Plan of Work** were retired (web tool ended end of June 2022); NBS recommends the **RIBA Plan of Work Toolbox** (RIBA Plan of Work 2020) [23]. Uniclass stays free and NBS Chorus/Source use it as primary classification [23].

### 1.7 Official tools, templates and portals

- **imiframework.org** (standards, guidance via Morta, resources, FAQ) [1]
- **NBS Uniclass** page and tables with API [24]; NBS **National BIM Library** (manufacturer objects, IFC at the core since 2013) see bSUKI/NBS snippet in [8]; NBS Chorus/Source (specification) [23]
- **RIBA Plan of Work Toolbox** (replacement for NBS Digital Plan of Work) [23]
- **bSDD** (technical.buildingsmart.org/services/bsdd/, search.bsdd.buildingsmart.org) [27]
- There is **no single UK public IFC submission portal** comparable to a building-permit upload service in the sources I read. Public clients define their own CDE/system of record under the mandate [2] ("Planning Portal" and Building Safety Regulator gateways are not BIM/IFC portals; unverified).

### 1.8 Key organisations

| Organisation | Role |
|---|---|
| **nima** (formerly UK BIM Alliance, est. 2016; renamed Oct 2022) | Volunteer-led not-for-profit; runs IMI and bSUKI; with BSI maintains UK BIM Framework [7], [9] |
| **bSUKI** (buildingSMART UK & Ireland) | UK & Ireland chapter of buildingSMART International; hosted under the UK BIM Alliance/nima umbrella since 2017; rooms (Buildings, Infrastructure, Railway, Airports...), IDS/bSDD resources, certification module (it does not deliver training itself) [7], [8] |
| **BSI** | National standards body; BS EN ISO 19650, PAS, BS 8536, BS 1192-4 [1], [28] |
| **NBS** (RIBA Enterprises) | Uniclass, National BIM Library, annual survey (2025 edition titled Digital Construction Report 2025) [24], [30] |
| **NISTA / IPA** (HMT + Cabinet Office) | Government infrastructure body hosting the mandate [6] |
| **CIC, RIBA, CIBSE, ICE, Construction Leadership Council** | Professional bodies and industry leadership (roles not verified in this session) |

NBS Digital Construction Report 2025: 550+ respondents; only 15% describe BIM as "3D models with data"; 73% of manufacturers offer BIM/digital objects for some products (22% for all) [30].

### 1.9 Local software ecosystem and open source

- **Commercial:** Autodesk Revit (dominant authoring in surveys (unverified current share)), Graphisoft Archicad, Bentley, Tekla; CDEs such as Asite and BIMcollab/Autodesk Construction Cloud (unverified); Solibri and Navisworks for checking; NBS Chorus/Source for specification.
- **Open source with UK link:** **xBIM Essentials** (.NET IFC read/write/validate, CDDL licence; IFC2x3 and IFC4; Xbim.Ifc4x3 folder present; supports netstandard2.0/2.1, net8, net10) [31]; UK origin of the project **(unverified)**. IfcOpenShell/Bonsai and the OSArch community are international (not UK-specific).
- **Enthusiast/community (label: community):** nima volunteer networks (e.g. BIM4Water) [7]; CitA/BIM Ireland blogs in Ireland [22].

### 1.10 Local terminology (UK)

| Term used locally | Meaning | Note |
|---|---|---|
| Appointing party / lead appointed party / appointed party / task team | ISO 19650 roles replacing "employer / main contractor / supplier" | Used in UK Annex language |
| Employer's Information Requirements (EIR) -> **Exchange** Information Requirements | Pre-2018 PAS 1192-2 name vs ISO 19650 name | Common confusion |
| OIR, PIR, AIR, EIR | Organisational/Project/Asset/Exchange information requirements | [2] |
| BEP (pre-appointment / post-appointment) | BIM Execution Plan | |
| MIDP / TIDP | Master / Task Information Delivery Plan | |
| PIM / AIM | Project / Asset Information Model | |
| CDE | Common Data Environment; mandate says "system of record" | [2] |
| BIM Level 2 | Pre-2018 label for the 2016 mandate | [2] |
| RIBA Plan of Work 2020 stages 0-7 | Stages (Strategic Definition ... In Use) | [23] |
| Soft Landings / GSL | Handover and aftercare process | (unverified) |
| COBie UK 2012 | Spreadsheet asset-data format | [28] |

---

## 2. Ireland

### 2.1 Policy timeline

| Date | Event | Source |
|---|---|---|
| 2014 | Review of public works contracts begins the shift | [18] |
| Dec 2017 | National BIM Council (NBC, set up by Enterprise Ireland 2016) roadmap due (Oireachtas answer dates it Dec 2017); BIM Position Paper 2017 | [18], (search snippets) [41] |
| 2021 | Build Digital Project launched | [18] |
| 4 Jul 2023 | Ministerial announcement / OGP information note: BIM requirements to enter the CWMF; BIM standards compulsory for CWMF projects | [11], [18] |
| 1 Jan 2024 | Milestone 1: design teams, projects above EUR 100m | [12] |
| 1 Jan 2026 | Milestone 6: contractors/supply chain, above EUR 10m | [12], [19] |
| 31 Mar 2026 | **Information Manager (BIM) Role Profiles** published by the Department of Public Expenditure, Infrastructure, Public Service Reform and Digitalisation, Build Digital and NSAI | [16] |
| 1 Jul 2026 | Milestone 7: design teams, above EUR 5m (already in force at the research date) | [12] |
| 1 Jan 2027 | Milestones 8 and 9 (next) | [12] |
| 1 Jan 2028 | Milestone 12: all remaining projects incl. contractors under EUR 1m | [12] |

### 2.2 Who mandates what

- **Department of Public Expenditure, NDP Delivery and Reform** (now named Department of Public Expenditure, Infrastructure, Public Service Reform and Digitalisation per [16]) and its **Office of Government Procurement (OGP)**; contact: Infrastructure Division, construction@per.gov.ie [11], [14].
- Mechanism: the **Capital Works Management Framework (CWMF)** (public works contracts and procedures, cwmf.gov.ie). The public sector accounts for at least 25% of construction activity and the strategy uses that buying power; stated aims include measuring embodied carbon and improving time, cost and quality [11].
- **Applicability rule:** the mandate for both design teams and contractors applies to projects that **enter Stage 1 of the CWMF on or after the milestone date**, not retrospectively and not by construction start [12].
- The timeline is "subject to review based on monitoring feedback" [11], [12].

### 2.3 The 12-milestone adoption timeline (official)

| Milestone | Date | Project value | Applies to |
|---|---|---|---|
| 1 | 1 Jan 2024 | above EUR 100m | Design consultants |
| 2 | 1 Jan 2025 | above EUR 100m | Contractors and supply chain |
| 3 | 1 Jan 2025 | above EUR 20m | Design consultants |
| 4 | 1 Jul 2025 | above EUR 20m | Contractors and supply chain |
| 5 | 1 Jul 2025 | above EUR 10m | Design consultants |
| 6 | 1 Jan 2026 | above EUR 10m | Contractors and supply chain |
| 7 | 1 Jul 2026 | above EUR 5m | Design consultants |
| 8 | 1 Jan 2027 | above EUR 5m | Contractors and supply chain |
| 9 | 1 Jan 2027 | above EUR 1m | Design consultants |
| 10 | 1 Jul 2027 | above EUR 1m | Contractors and supply chain |
| 11 | 1 Jul 2027 | below EUR 1m | Design consultants |
| 12 | 1 Jan 2028 | below EUR 1m | Contractors and supply chain |

(Source: [12], official CWMF page; matches the third-party summary [20].) In 2024, eTenders.ie registered 1,652 public works projects: 160 above EUR 10m, 80 above EUR 5m, 322 above EUR 1m, 1,090 below EUR 1m [18]. A Dublin City Council strategy PDF (2026) reportedly describes threshold steps to over EUR 5m in early 2026; the official table above supersedes it (the PDF was unreadable by my tool).

### 2.4 Core BIM requirements and IFC

The CWMF "Core BIM Requirements" page lists exactly **four standards** that apply where BIM requirements are included in a CWMF public works project [13]:

1. **ISO 19650 series**
2. **Uniclass** (Uniclass 2015 per Build Digital) [21]
3. **Industry Foundation Classes (IFC)** ("a universal translator for BIM data")
4. **International Cost Management Standard (ICMS)** (classification of construction lifecycle costs and carbon); cost reporting templates incorporating ICMS were published from August 2023, with life-cycle costing in early 2024 and life-cycle analysis/embodied carbon in 2025 [11]

Not found in the accessible official pages: a specific **IFC version/MVD**, mandatory **property sets**, **COBie** requirement, or **georeferencing/naming** rules. The trade source [19] says IFC is not described as a contractor requirement and that contractors must deliver structured digital information, federated models, information delivery plans and asset data, include BIM workflow documentation in tenders, and appoint or train a BIM coordinator (trade commentary; treat as non-official).

Typical practice (general knowledge, **unverified**): Irish Transverse Mercator (ITM, EPSG:2157) horizontal and Malin Head vertical datum for georeferencing (legacy Irish Grid EPSG:29902); IFC2x3 CV2.0 and IFC4 RV in EIRs; Uniclass 2015 references in IFC `IfcClassificationReference`.

### 2.5 Official guidance, tools and portals

- **cwmf.gov.ie** BIM resources: Core BIM Requirements, Public Sector BIM Adoption Timeline, **Seven Steps to BIM for Construction Clients** [13], [12], [15]. The seven steps: appoint an Information Manager; develop a plan (BIM Implementation Plan, BIP) and adopt ISO 19650; choose software/hardware and a cloud CDE; set goals; choose the team; train; monitor and adjust. Named documents: OIR, PIR, AIR, EIR, BIP, CDE. No templates on that page [15].
- **Build Digital** (builddigital.ie, formerly builddigitalproject.ie): supports under Project Ireland 2040, hubs Digi Adopt / Digi Implement / Digi Innovate, supports "aligned with ISO 19650 and the Irish BIM mandate", annual survey (the 2025 survey had 205 participants per [19]; 2026 survey and conference announced) [21].
- **Information Manager (BIM) Role Profiles** (31 Mar 2026) [16].
- **NSAI** ISO 19650 certification scheme and consultation process [18], [19]; national adoption likely as I.S. EN ISO 19650 (unverified).
- **ISO 19650 event "Digital Delivery for Ireland's Infrastructure"** (27 Mar 2026) [17].
- Public sector BIM group, masterclasses and webinars [18].
- **TII (Transport Infrastructure Ireland)** has its own "BIM for Infrastructure" statement of intent and roadmap (document seen in search results; contents unverified) [40].
- **No national IFC upload portal** for permits found; public tenders go through eTenders.ie [18].

### 2.6 Key organisations

| Organisation | Role |
|---|---|
| **OGP / Department of Public Expenditure...** | Policy owner of the CWMF BIM requirements [11] |
| **Build Digital** | Digital adoption programme, guidance and templates [21] |
| **CitA (Construction IT Alliance)** | Industry network; began 2001 at DIT Bolton St., company 2005; annual BIM Gathering since 2008; CitA Skillnet training; BICP with Enterprise Ireland [22] |
| **National BIM Council (NBC)** | Public-industry partnership set up by Enterprise Ireland in 2016; nine members including OPW, OGP, NDFA, Enterprise Ireland, CitA; produced a roadmap [41] (search snippets) |
| **NSAI** | National standards body; ISO 19650 certification [18] |
| **bSUKI** | Chapter covers UK **and Ireland** per nima; no dedicated Irish activity found [8] |
| **BIM Ireland** (bimireland.ie) | Community news site, partner of CitA [22] |

### 2.7 Local software and community

Revit and Archicad are widely used in Ireland (unverified); Irish-language BIM terms are not used in practice (English is the working language). Enthusiast training sites (for example S15Studio, MustDo Training) publish explainers; label as commercial/training blogs [20].

### 2.8 Terminology (Ireland)

| Term | Meaning |
|---|---|
| CWMF | Capital Works Management Framework: Irish public works procurement system |
| OGP | Office of Government Procurement |
| Stage 1 (CWMF) | The project stage whose entry date triggers the BIM milestone |
| Information Manager | Role profile published 2026 [16] |
| BIP | BIM Implementation Plan [15] |
| ICMS | International Cost Management Standard |
| Design consultants vs contractors and supply chain | The two groups in the milestone table |
| Public works contract | Irish term for the contract forms used on public capital works |

---

## 3. IFC-related quick reference for testing MCP servers

| Check | UK expectation | Ireland expectation |
|---|---|---|
| Process standard | BS EN ISO 19650 + UK National Annex | ISO 19650 series (CWMF) |
| Classification | Uniclass 2015 (National Annex) | Uniclass (2015) |
| IFC mention | Yes, open format; version per EIR | Yes, core standard; version per EIR |
| Cost classification | n/a | ICMS |
| COBie | Legacy BS 1192-4 (status unverified) | Not named in official core list |
| Georeference (typical) | EPSG:27700 (BNG) + ODN | EPSG:2157 (ITM) + Malin Head |
| Mandate scope | Central gov clients, no threshold | Public works, dated value thresholds |

Revit-specific tips (general knowledge, unverified): Revit's IFC export dialog (File > Export > IFC) offers IFC2x3 Coordination View 2.0 and IFC4 Reference/Design Transfer views; Uniclass codes are usually stored in the Assembly Code / Keynote parameters or shared parameters and mapped to classification on export; for georeferencing use project base point / survey point and shared coordinates. Test an MCP by asking it to list `IfcClassificationReference` entries for walls, or to verify file names against the project naming pattern.

---

## Typical questions people ask about this

No real forum threads were retrieved (search budget exhausted), so all are illustrative.

1. (illustrative) Is BIM mandatory on UK public projects, and since when? (2016 Level 2 mandate; 2021 Information Management Mandate [2], [3].)
2. (illustrative) Is the UK BIM mandate still in force after ISO 19650 and the IMI? What replaced BIM Level 2?
3. (illustrative) What is the difference between PAS 1192-2 and ISO 19650-2, and can I still cite PAS 1192-2?
4. (illustrative) What does the UK National Annex change compared with plain ISO 19650-2?
5. (illustrative) Which IFC version should I export for a UK project: IFC2x3 CV2.0 or IFC4?
6. (illustrative) How do I add Uniclass 2015 codes to IFC elements so the client's checker accepts them?
7. (illustrative) Where do I download Uniclass 2015, and is it free? (Yes, NBS [24].)
8. (illustrative) Is COBie still required in the UK, and what replaced the NBS BIM Toolkit?
9. (illustrative) What is the Information Management Initiative (IMI) and do I have to sign it?
10. (illustrative) What does an EIR / Exchange Information Requirements document need to contain for an IFC delivery?
11. (illustrative) When does the Irish BIM mandate apply to my project: by tender date, Stage 1 date or construction start? (Stage 1 of the CWMF [12].)
12. (illustrative) My project is EUR 7m: which Irish milestone applies and from when? (Design teams from 1 Jul 2026, contractors from 1 Jan 2027 [12].)
13. (illustrative) Which standards must Irish public works BIM deliverables follow? (ISO 19650, Uniclass, IFC, ICMS [13].)
14. (illustrative) Does the Irish mandate specify an IFC version or MVD?
15. (illustrative) What is an Information Manager and what qualifications does Ireland expect? ([16])
16. (illustrative) Do UK and Irish models use different coordinate systems (BNG vs ITM) and how do I set them in IFC?
17. (illustrative) How do I name files and containers in a CDE under the UK National Annex?
18. (illustrative) How can I automatically check an IFC against the client's requirements (IDS)? ([32], [33])
19. (illustrative) Does Northern Ireland follow the UK or the Irish mandate?
20. (illustrative) What are Government Soft Landings and BS 8536, and do they affect model deliverables?

## Common pitfalls and misconceptions

- **"UK BIM Level 2 is the current standard."** The label was dropped in 2018; the framework is now the UK BIM Framework / IMI Framework [2], [1].
- **PAS 1192-2 and BS 1192:2007+A2:2016 are withdrawn**; do not use them in new contracts (PAS 1192-6 is still listed) [1], [38].
- **"The mandate has a UK threshold."** The 2021 mandate does not state one [2]. Ireland does, and it is milestone-based [12].
- **Old Irish numbers:** "BIM only over EUR 100m" was the 2024 position; milestone 7 (EUR 5m design teams) is already in force as of 1 Jul 2026 [12].
- **Irish trigger date is CWMF Stage 1 entry,** not tender or construction date [12].
- **Ireland and UK are not one regime**; Northern Ireland is UK jurisdiction, the Republic of Ireland is separate (devolved details unverified).
- **IFC is named but not versioned:** do not assume a nationally mandated MVD in either country; check the EIR.
- **Uniclass 2015 is not the old Uniclass (1997) or Uniclass 2;** tables get quarterly updates, so record the edition [24], [25].
- **NBS BIM Toolkit / Digital Plan of Work are retired** (2022); do not send users there [23].
- **COBie UK 2012 vs IFC:** COBie is a spreadsheet exchange format; it is not an IFC schema (although aligned with it) [28].
- **Trade blogs are not official.** Fit-out and training sites [19], [20] summarize the CWMF; the official page is [12].

## Gaps

- The web-search quota ran out partway through; I could not search for real forum questions or for Scottish, Welsh and Northern Irish policies.
- HTTP 403 or unreadable PDFs: gov.ie "BIM and the CWMF", Oireachtas answers, buildingsmart.org chapter pages, imiframework.org/faq, ISO pages for 19650 and 16739, several CitA/OGP/DCC/EU PDFs. Any statement derived from these is marked as snippet or unverified.
- A redirect from sft.co.uk went to a domain-listing site (impact.co.uk); I skipped it as untrustworthy rather than follow it.
- Not verified: exact UK National Annex edition numbers, BS 1192-4 current status, UK file-naming field list and suitability codes, GSL publication details, Ireland's NBC roadmap document itself, Irish national adoption and National Annex of ISO 19650, any IFC version/MVD requirement in either country, georeferencing conventions.

## Sources

- [1] IMI Framework (formerly ukbimframework.org): https://imiframework.org/ and https://imiframework.org/standards/
- [2] IPA, Transforming Infrastructure Performance: Roadmap to 2030 (13 Sep 2021), Annex B: https://www.gov.uk/government/publications/transforming-infrastructure-performance-roadmap-to-2030/transforming-infrastructure-performance-roadmap-to-2030
- [3] Construction Management, "Updated information management mandate launched": https://constructionmanagement.co.uk/updated-information-management-mandate-launched/
- [4] Construction Management/BIM+, Information Management Initiative (8 Nov 2024): https://constructionmanagement.co.uk/digital-construction/information-management-initiative-information-management-for-all/
- [5] Designing Buildings, Information management mandate: https://www.designingbuildings.co.uk/wiki/Information_management_mandate
- [6] NISTA Memorandum of Understanding: https://www.gov.uk/government/publications/nista-memorandum-of-understanding/nista-memorandum-of-understanding
- [7] nima, What we do: https://wearenima.im/?p=160
- [8] bSUKI introduction: https://wearenima.im/bsuki-introduction/
- [9] Designing Buildings, nima: https://www.designingbuildings.co.uk/wiki/Nima
- [10] Designing Buildings, Building SMART: https://www.designingbuildings.co.uk/wiki/Building_SMART
- [11] CWMF, BIM requirements in the CWMF from January 2024 (4 Jul 2023): https://cwmf.gov.ie/en/news/bim-requirements-in-the-cwmf-from-january-2024/
- [12] CWMF, Public Sector BIM Adoption Timeline: https://cwmf.gov.ie/en/resources/bim/public-sector-bim-adoption-timeline/
- [13] CWMF, Core BIM Requirements: https://cwmf.gov.ie/en/resources/bim/core-bim-requirements/
- [14] CWMF, BIM page: https://cwmf.gov.ie/en/bim/
- [15] CWMF, Seven Steps to BIM for Construction Clients: https://cwmf.gov.ie/en/resources/bim/seven-steps-to-bim-for-construction-clients/
- [16] CWMF, Information Manager (BIM) Role Profiles (31 Mar 2026): https://cwmf.gov.ie/en/news/information-manager-role-profiles/
- [17] CWMF news listing: https://cwmf.gov.ie/en/news/
- [18] EU Public Buyers Community, The Irish experience implementing BIM: https://public-buyers-community.ec.europa.eu/communities/bim-and-public-procurement/news/irish-experience-implementing-bim-and-public
- [19] Fit Out Awards (trade commentary), Milestone 6: https://fitoutawards.ie/news/bim-is-now-a-fit-out-contractor-requirement-on-irish-public-projects-what-milestone-6-means-and-how-to-get-ahead-of-it
- [20] S15Studio (training blog), Irish BIM mandate: https://www.s15studio.com/post/bim-mandate-ireland
- [21] Build Digital: https://builddigital.ie/
- [22] CitA: https://www.cita.ie/
- [23] NBS, BIM Toolkit changes in 2022: https://thenbs.com/knowledge/nbs-bim-toolkit-changes-in-2022
- [24] NBS, Uniclass: https://www.thenbs.com/tools/uniclass
- [25] NBS knowledge listing (Uniclass April 2026 update): https://www.thenbs.com/knowledge/classification-systems
- [26] NBS, What is Uniclass 2015: https://www.thenbs.com/knowledge/uniclass-2015-an-update
- [27] NBS on bSDD: https://www.thenbs.com/knowledge/what-is-the-buildingsmart-data-dictionary ; nima bSDD page: https://wearenima.im/resources/buildingsmart-data-dictionary-bsdd/
- [28] Designing Buildings, BS 1192-4: https://www.designingbuildings.co.uk/wiki/BS_1192-4
- [30] NBS Digital Construction Report 2025 coverage: https://specificationonline.co.uk/articles/2025-12-16/the-nbs/bim-comes-of-age-in-construction-as-most-professionals-now-consider-it-a-collaborative-project-information-management-process
- [31] xBIM Essentials: https://github.com/xBimTeam/XbimEssentials
- [32] nima, IDS resource: https://wearenima.im/resources/information-delivery-specification-ids/
- [33] buildingSMART IDS repository: https://github.com/buildingSMART/IDS
- [34] Construction Playbook: https://www.gov.uk/government/publications/the-construction-playbook
- [38] (search snippets, pages not fetched): https://www.designingbuildings.co.uk/wiki/PAS_1192-2 , https://architecturaltechnology.com/resource/transition-from-1192-to-19650-avoiding-the-early-mistakes.html
- [39] (search snippets, pages not fetched): https://pbctoday.co.uk/news/?p=89330 , https://specificationonline.co.uk/articles/2021-12-15/bim-task-group/new-update-released-for-bim-framework
- [40] TII BIM for Infrastructure statement of intent (search result, unread): https://www.tii.ie/media/krjpyopa/bim-for-infrastructure-statement-of-intent-and-roadmap.pdf
- [41] NBC launch (search snippets): https://bimireland.ie/?p=14168
