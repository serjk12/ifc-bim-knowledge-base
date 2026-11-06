# Taiwan, Hong Kong, Macau: BIM/IFC requirements

## In plain words

Three places, three very different situations. **Hong Kong** has the strictest and best-documented regime: since 2018 the government requires BIM on public capital works above HK$30 million, and since 1 April 2025 the design BIM model is part of the tender and contractually binding for construction tenders [1][8]. The Buildings Department (BD) accepts BIM as supplementary material with statutory plans, and the government plans to make electronic submission of BIM-generated plans and BIM models mandatory around 2029 [4][5][7]. IFC 4 is the official "shareable" format for government departments [3]. **Taiwan** has no single national BIM mandate that I could find. BIM is driven project by project through procurement documents from the Public Construction Commission (PCC, 工程會), the Ministry of the Interior (內政部) and agencies such as the Railway Bureau, backed by a research-based "BIM Collaboration Guide" (我國BIM協同作業指南) [14][15]. **Macau** is the least documented: I found only an unverified indication that the public works bureau now asks designers on new design projects to submit BIM models, and no standard, circular or IFC rule [21]. For a QA tester this means: Hong Kong questions will usually have a precise, citable answer (circular numbers, file name patterns, coordinate system); Taiwan answers are guideline-level and contract-specific; Macau answers should be treated as "no published national requirement found".

Last researched: 2026-11-06

---

## 1. Quick comparison

| Topic | Hong Kong | Taiwan | Macau |
|---|---|---|---|
| Main driver | Development Bureau (發展局, DEVB), Works Branch (工務科) [1] | PCC (行政院公共工程委員會), Ministry of the Interior (內政部) and its Architecture and Building Research Institute (建築研究所), Land Administration Agency (國土管理署, formerly Construction and Planning Agency 營建署) [14][15] | Public works bureau (DSOP / DSSOPT, now apparently 土地工務局 DSSCU) (unverified) [21][28] |
| Legal force | Technical circulars binding on Works Departments and their consultants/contractors; not a statute for private sector yet | Guidelines and contract templates; applied per tender | Not found |
| Threshold | Capital works with project estimate above HK$30 million [1] | None found at national level; project by project | Not found |
| Start | Pilots 2013; mandatory design BIM from 2018 [1][8] | PCC BIM promotion platform May 2014 (per search summary, unverified); pilot-based [14] | Not found |
| IFC | IFC 4 for shareable models; Reference View v1.2 (Coordination View v2.0 for Civil 3D) [3] | IFC cited in research and test projects; COBie requested in contracts; no national IFC version found [15][16] | Not found |
| Classification | OmniClass Table 23 for object library folders; CIC Master Type List [3] | LOD per AIA E202 in some specs; COBie-TW research; classification code not verified [15][16] | Not found |
| Coordinates | HK 1980 Grid + Hong Kong Principal Datum (HKPD) [3] | Not found | Not found |
| buildingSMART chapter | buildingSMART Hong Kong, China (incorporated 2019, per search summary) [20] | Not confirmed | None found |

---

## 2. Hong Kong

### 2.1 Who mandates what

- **Development Bureau (DEVB), Works Branch** issues the Technical Circulars (Works), abbreviated TC(W). The current one is **DEVB TC(W) No. 1/2025, "Adoption of Building Information Modelling for Capital Works Projects in Hong Kong"**, dated 21 January 2025, effective 1 February 2025, ref DEVB(W) 430/80/01, 29 pages. It supersedes TC(W) No. 2/2021 [1].
- Policy line in the circular: capital works projects with project estimates **more than HK$30 million** shall use BIM; it applies to investigation, feasibility, planning, design and construction stages irrespective of delivery mode (para 10). It applies to works done by government staff, consultants or contractors [1].
- Circular history as described in the circular itself (paras 5-9): WPCC endorsed an incremental strategy in April 2013 (pilots); wider use in 2014; TC(W) 7/2017 required consultants and contractors to use BIM for design of major capital works from 2018; TC(W) 18/2018 added 4D (construction planning) and 5D (cost); TC(W) 9/2019 added investigation/feasibility/planning, design for digital fabrication and sustainability (6D); TC(W) 12/2020 added asset management, underground utilities survey, engineering analysis, 3D control and planning; TC(W) 2/2021 added enhanced workflow, Common Data Environment, data harmonisation and information security; a June 2023 memo set the target of contractually binding models and a common data platform [1].
- TC(W) 8/2021 introduced the **DEVB BIM Harmonisation Guidelines** (for tenders from 1 January 2022) [1][11]. Current version **3.0, December 2025** [3].
- The DEVB Secretary's blog (23 Nov 2025) says mandatory BIM on public works above HK$30 million has applied since 2018, models were added to tender documents in April 2025, and the CITF (Construction Innovation and Technology Fund) supports BIM training and tools [8].

### 2.2 What TC(W) 1/2025 actually requires (verified from the circular text) [1]

| Item | Requirement |
|---|---|
| Contractually binding models | For construction tenders with BIM adoption invited **on or after 1 April 2025**, the design BIM models form part of tender information and are contractually binding for the parts matching the 2D tender drawings. MEP installations, existing site conditions and proprietary-product attributes are "reference" only (Annex 3, 4) |
| Design stage | BIM mandatory for projects designed under DC/IDC consultancy agreements or in-house |
| Construction stage | All construction tenders must stipulate BIM, including Design-Build and Design-Build-Operate |
| BIM uses (Annex 1) | 20 BIM uses, each mandatory/optional per stage: design authoring, design review, existing conditions modelling, site analysis, 3D coordination, cost estimation (5D), engineering analysis, facility energy analysis, sustainability evaluation, space programming, phase planning (4D), digital fabrication, site utilization planning, 3D control and planning, as-built modelling, project systems analysis, maintenance scheduling, space management, asset management, drawing generation |
| Drawings | 2D drawings must be generated from the 3D model; stop producing 2D elsewhere if they can come from the model (para 27) |
| Common Data Collaboration Platform (BIM CDCP) | Works Departments should adopt it; consider "open BIM" approach; build departmental CDCP roadmaps that connect to the Government BIM Data Repository (para 25) |
| Software neutrality | Brand names must not be written in tender specs; specs must be performance/function based; priority to open BIM strategy (para 26) |
| Asset management | As-built BIM in **open BIM format** should be prepared for asset management; native format only if the maintenance agent requires it (para 17) |
| To Lands Department | Design and as-built BIM models go to LandsD for the BIM data repository (para 19) |
| People | BIM Team Leader should be a CIC-Certified BIM Manager (CCBM); BIM Coordinator a CIC-Certified BIM Coordinator (CCBC) or CCBC (Associate), with at least half of coordinators holding CCBC (annex sample text); training via CITF-listed courses [1] |
| Exemptions | Heads of Works Departments may exempt projects of little technical content (e.g. paving, painting, slope maintenance, greening, term-contract maintenance) |
| Entrusted/private-to-be-handed-over projects | Scope aligned with the entrusting organisation's policy; as-built models for government-maintained parts follow the Harmonisation Guidelines (para 20) |
| Security | Public cloud use must follow Baseline IT Security Policy [S17] and IT Security Guidelines [G3] from the Digital Policy Office (para 31) |

A sample "BIM files" table inside the circular lists native models (`XXXX-XXX-XX-XX-AR_ARC-ST.rvt`, `...AR_FAC...`, `...ST_STR...`, `...AR_LAN...`, `...BS_FS...`, `...BS_AC...`, `...BS_UU...`, existing site model `...ZZ-CM_E.rvt`) and the same set in open format with `.ifc` extension [1]. Useful as a naming example for tests.

### 2.3 DEVB BIM Harmonisation Guidelines for Works Departments, v3.0 (December 2025) [3]

Key IFC-relevant rules (quoted/paraphrased from the text):

- **IFC version:** "For the shareable BIM format, IFC v4 will be used" (2.2.1.5). The Government BIM Data Repository (GBDR, launched May 2022) hosts native models, shareable IFC models and CityGML (2.1.6).
- **MVD:** when preparing IFC for GBDR, set **Reference View v1.2** in ArchiCAD, OpenBuildings Designer and Revit, or **Coordination View v2.0** in Civil 3D (5.3.4 h).
- **Geometry vs data:** geometry exchanged as IFC; non-geometric attributes exported in tabular form such as **COBie** (2.4.3).
- **Coordinates:** all BIM files authored directly in **Hong Kong 1980 Grid and Hong Kong Principal Datum (HKPD)** (5.3.1). Units metric (mm for buildings, m for infrastructure).
- **File sizes:** each model capped at **500 MB**; each BIM object file preferably under **5 MB** (2.3).
- **Model naming:** an ISO 19650-2 information container ID, max **43 characters** (excluding extension); fields include project code, originator (Agent Responsible Code, ARC, published by DEVB), volume/system, location, discipline, type (Section 4, Appendix VIII-X).
- **Object naming:** `<Category>-<Functional Type>-<Originator>-<Descriptor 1>-<Descriptor 2>.<ext>`, max **30 characters**, aligned with the CIC Production of BIM Object Guide (Version 2 - 2021) (3.4).
- **Classification:** CIC BIM Portal supports **OmniClass**; object folders follow OmniClass 2012 Table 23 first level (3.6.1). The CIC Master Type List holds the local classification and codification.
- **LOD:** LOD-G (graphics) and LOD-I (information) 100-500, consistent with CIC BIM Standards (5.4, 5.5, Appendix VI).
- **Practical IFC export traps listed by the guideline:** linked files are not exported to IFC by default; only objects existing in the last phase are exported (do not set "Phase Created" = "Phase Demolished"); do not add IFC class names in user-defined attributes; do not create user parameters with the same name as built-in ones (use a department prefix) (5.3.4 c, d, f, g).

### 2.4 CIC (Construction Industry Council, 建造業議會) standards [10][11][19]

- **CIC BIM Standards - General**: first published September 2015; Version 2 (December 2020) aligned with ISO 19650 and provided a Hong Kong Local Annex to ISO 19650-2:2018; Version 2.1 (2021); the **2024 edition** supersedes 2.1 and adds Appendix D templates: D1 OIR, D2 AIR, D3 PIR, D4 security information requirements, D5 pre-appointment implementation plan, D6 pre-appointment BIM Execution Plan, D7 BIM capability assessments, D8 capability summary/software schedule, D9 project member resume; plus a separate EIR template [10].
- Discipline volumes exist: Architecture and Structural Engineering, MEP, Underground Utilities (as of 2021 per search summary) [19]. CIC Production of BIM Object Guide (Version 2 - 2021) and BIM Object Library/portal [3][19].
- CIC page "Global IFC Mandates" (publication_detail/153) is a buildingSMART International compilation hosted on the CIC site; the page text I could read does not list HK specifics [22].
- CIC certification: CCBM, CCBC; the CCBC(A) application deadline is shown as **31 December 2026** on the CIC BIM site [30].

### 2.5 Buildings Department (屋宇署) and BIM e-submission [4][5][6][9]

- **Not mandatory yet.** PNAP **ADV-34** (first issue September 2016, revised May 2023) says BD encourages Authorized Persons (AP), Registered Structural Engineers (RSE) and Registered Geotechnical Engineers (RGE) to use BIM; plans in paper/2D PDF are what BD approves; BIM files are used for checking against plans; **in case of discrepancy the plans prevail** [6]. **ADM-19** covers plan approval procedures and the "Guidelines for using BIM in General Building Plans Submission" [5][6].
- **Electronic Submission Hub (ESH, 電子資料呈交及處理系統)** at esh.bd.gov.hk: Stage 1 (30 June 2022), Stage 2 (2023), Stage 3 launched **30 June 2024** accepting all plan types under the Buildings Ordinance (Cap. 123); 35 government departments/organisations receive plans simultaneously [4][9]. ESH accepts BIM files up to **500 MB per file** [4].
- **Tentative schedule (BD newsletter, June 2024):** mandatory e-submission of plans by **mid-2027**; mandatory e-submission of **BIM-generated plans and BIM model by 2029** [4]. The December 2023 consultation roadmap proposed: government-related bodies (HK Housing Society, Urban Renewal Authority, MTR) submit BIM plans in groups from 2024-2025; large private residential developments from 2026; all private development from 2029 after legislative amendment [7]. The final published roadmap text was not verified; use [4] and [8] as the stable facts.
- **BD automated checking tools (BIM Area Tool etc.)** [5]: BIM Area Tool (floor area, BD and Lands Department common method; launched March 2024 [9]), BIM SF Tool (sanitary fitments), BIM FS Tool (fire safety), BIM Building Separation Tool (openBIM, volumetric permeability method), BIM Structure Tool (BST) Phase 1 and Phase 2 (Phase 2 rolled out December 2025: overlay native BIM and structural analysis models, conversion between openBIM and structural analysis models). Plug-ins for Revit 2023-2026 (Area/SF/FS), ArchiCAD 26/27; BST plug-in for Revit 2024-2026; an **IFC property set text file for exporting IFC from Revit** (file name pattern `IFC_PropertySet_BUD_Str_v1_1_Revit_to_IFC`) is downloadable. Support: bim-helpdesk@bd.gov.hk, BIM hotline 2152 2849 [5] (organisational contacts, not personal data).
- ESH helpdesk: hotline 3580 1000, esh-helpdesk@bd.gov.hk [9].

### 2.6 Other public bodies [7][12][13]

- **Housing Authority (HA):** using BIM in public housing since 2005; 3-tier BIM/GIS management structure from 2007; standard modular flats 2008; QSBIM research 2012; BIM-GIS site planning 2014; statutory submission pilot where 2D GBP and foundation plans derive from the 3D model and RTTV (a calculation required in general building plan submissions; abbreviation not expanded in the source) is computed by BIM. Current **HA BIM Standards and Guidelines Version 5.0** (Volume 1 Introduction and Quick Guide, Volume 2 Detail Guide, Annexes) per the HA page; the 2023 roadmap annex lists version 3.0, so the page was updated since [7][12].
- **Lands Department:** "BIM and GIS Data Integration Guidelines", June 2023 edition (v1.0); requirements: mapping BIM elements to GIS, unique identifiers for BIM objects, delineation of units, subtype definition for space use; conversion LOD, GIS schema, filling interstitial spaces between units [13]. LandsD runs the Government BIM Data Repository (GBDR).
- **EMSD** (Electrical and Mechanical Services Department): BIM-AM (BIM for Asset Management) system since 2014 with Standards and Guidelines v3.0, handover and acceptance guidelines [7].
- Roadmap annex also lists BD guidelines for BIM statutory submissions (general building plans and other plans), PNAP APP-151 [7].

### 2.7 Organisations, software, community

- **buildingSMART Hong Kong, China** chapter: incorporated 2019 (per search summary); hosted the buildingSMART International Asia Summit in Hong Kong in June 2024 [20]. Its relation to the Hong Kong Alliance of Built Asset & Environment Information Management Associations is unclear in my sources (unverified).
- **HKIBIM** (Hong Kong Institute of Building Information Modelling): professional body with individual and corporate members, China Division, awards, annual conferences; founding year given as January 2009 in a search summary (unverified); the website does not mention openBIM or buildingSMART [25].
- **CIC** runs BIM standards, certification and the BIM object portal. **CITF** subsidises software and training [1][8].
- **Software ecosystem:** Revit and ArchiCAD are the platforms with official BD tools; OpenBuildings Designer and Civil 3D named in the harmonisation guidelines; Civil 3D used for civil/UU. Local enthusiasts/open source: I did not find a verifiable HK open-source IFC project (gap). The engineering resource site kctang.com.hk mirrors CIC and DEVB documents (community, label as such) [19].

---

## 3. Taiwan (臺灣)

### 3.1 Who and what

- **Public Construction Commission (行政院公共工程委員會, PCC)** runs the "BIM zone" (公共工程運用建築資訊建模(BIM)專區). The page lists [14]:
  1. BIM quantity takeoff import into PCCES demo (May 2016, 105年5月);
  2. Final report of the PCC commissioned study "機關辦理公共工程導入建築資訊建模BIM技術" (January 2017, 106年1月), the basis of the **"機關辦理公共工程導入建築資訊建模(BIM)技術作業參考手冊"** (agency reference manual: scope, timing, introduction process, fee budgeting principles, reference contract documents, Q&A; prepared with National Central University per search summary);
  3. Taoyuan public housing design-build BIM experience sharing (Nov 2017);
  4. **New Taipei City Public Works Department BIM Work Reference Manual** (新北市政府工務局BIM工作參考手冊, October 2018);
  5. **Railway Bureau (交通部鐵道局) Railway BIM Guide (鐵道工程BIM作業指引) V2.0** (October 2019);
  6. **Land Administration Agency (內政部國土管理署) "施工階段BIM建置規範 (適用建築、水電、空調合併招標)"** (October 2022, 111年10月);
  7. Land Administration Agency commissioned planning/design work instructions (excerpt of the BIM specification, page published May 2023).
  The page states no mandate or threshold; it lists reference documents. Page "last updated" shown as 115-11-06 (ROC year, = 2026-11-06) [14].
- **Ministry of the Interior (內政部)**: Construction and Planning Agency (營建署) was reorganised as the Land Administration Agency (國土管理署) (date not verified here; the 2022 spec PDF still says copyright belongs to 營建署 [16]). Its **Architecture and Building Research Institute (建築研究所, ABRI)** funds BIM research [15].
- **"我國 BIM 協同作業指南" (Taiwan BIM Collaboration Guide):** developed by ABRI from 2015 on (104年 draft with contract "BIM special clauses"; 105年 implementation items: **6 project stages and 25 BIM uses**; later years: training materials, handover info for as-built models, maintenance guide 109年). Parts use document codes such as TW-00-3 (public design-build contract template with BIM clauses), TW-01 (BIM special clauses), TW-02 (collaboration guide), TW-03 (organisational BIM adoption), TW-04 (BIM Execution Plan), Appendix D (modelling guidelines), **Appendix E (BIM common data environment)**. In 2023 a project by **Taiwan Architecture and Building Center (財團法人台灣建築中心, TABC)** funded by ABRI updated the Guide towards **ISO 19650** and CDE (draft/research recommendations "do not represent the agency's opinion"); it recommends compiling a new edition [15].
- Tests in 2015: Revit, Archicad and Tekla exchanged most model info via IFC but with information loss due to differing component definitions [15].
- ABRI mid-term programmes: 108-111 (2019-2022) "建築資訊整合應用躍升計畫", then 112-115 (2023-2026) "建築資訊跨領域整合創新應用計畫" [15].

### 3.2 Delivery requirements in a real spec [16]

The Land Administration Agency's construction-stage spec (public text, 12 pages) is a good example of what "Taiwan requirements" look like:
- BIM model in 3D parametric form; LOD per **AIA E202-2008** definitions LOD 100-500 (table copied from NTU research centre draft guide); contractors build **LOD 200 and 300** per element table (structure LOD 200 with material names; facade, finishing, MEP 300).
- Deliverables: clash analysis reports, **4D progress simulation**, as-built BIM model, a viewer-accessible 3D package (disc, 10 copies), **BIM maintenance model exportable in COBie format**, training sessions (5 sessions, 4 hours each), plus maintenance data (vendor, brand/model, specification, installation date, phone, warranty date, service frequency) for generators, pumps, elevators, HVAC etc.
- Payment: 30% after architecture+structure models, 80% after MEP models + 4D + clash report, 100% after completion; BIM copyright belongs to the Ministry of the Interior agency.
- The excerpt I read does **not** mandate IFC file delivery; native format is implied. IFC appears in Taiwan research (e.g. an IFC-to-maintenance-system pipeline for public buildings) [15][18].

### 3.3 Classification and codes

- No Taiwan-specific national BIM classification code verified. Related items: **PCCES** (the PCC's cost estimating system; BIM quantity takeoff demo by PCC) [14]; **COBie-TW** research ("臺灣 COBie-TW 標準與使用指南規劃與雛型建置", ABRI 2015, cited in [15]); OmniClass used by researchers for MEP object export (cited in [15] reference list). Whether "施工綱要" numbering is used as BIM classification: (unverified).

### 3.4 Organisations and ecosystem

- **TABC (台灣建築中心)**, **ABRI (建築研究所)**, **NTU BIM Research Center** (臺大BIM研究中心, ntubim.net) and **CPWEIA (中華民國公共工程資訊學會)** appear as BIM actors in sources [15][18]. CPWEIA lists BIM project cases including a rule-checking tool for New Taipei building permit review [18] (search summary, unverified).
- **buildingSMART Taiwan chapter:** I could not confirm one (chapter directory returned 403 to my fetch; search found nothing) (unverified).
- **Software:** Revit, Archicad (Graphisoft publishes Traditional Chinese Archicad help covering IFC, seen in search results), Tekla, Fuzor used in public projects [15]. Local open-source IFC projects: none verified (gap). Community articles in Chinese (iThome Ironman series on OpenBIM mentioning buildingSMART and OSArch) exist but I could not open them (403) [18].

### 3.5 Other agencies

- Railway: Railway Bureau guide V2.0 (2019) [14]. Others (Taipei, Taoyuan, New Taipei city guides) are listed by PCC [14]. Public participation platform contains a citizen proposal to introduce grading of BIM personnel into public works (join.gov.tw idea) [18].

---

## 4. Macau (澳門)

- **Finding:** a Portuguese Legislative Assembly (al.gov.mo, document dated September 2025) reportedly quotes the public works bureau (DSOP) saying that for recently developed design projects the designer must submit a BIM model (*Modelagem da Informação da Construção*), for use during construction. I could not open the document, so this is **unverified** and has no thresholds, dates or standards [21].
- Public procurement: new law **Law No. 10/2025** published July 2025 (per a law-firm article snippet); no evidence it mentions BIM (unverified) [27].
- Agency names: *Direcção dos Serviços de Solos, Obras Públicas e Transportes* (DSSOPT, 土地工務運輸局); the DSSCU site now titled 土地工務局 (the web page shows only that title) [28]. Treat renaming as unverified.
- No Macau BIM standard, classification, IFC rule or buildingSMART chapter was found (gaps). Practitioners typically follow Hong Kong, mainland Guangdong-Hong Kong-Macao Greater Bay Area or Portuguese references (unverified).

---

## 5. How to test MCP servers against these rules (practical hints)

- **Hong Kong IFC check ideas:** IFC schema should be IFC4 (Reference View) for government submissions; Revit exports should use the Reference View setup, project base point tied to HK 1980 Grid (IfcMapConversion / IfcProjectedCRS expected; EPSG code for HK1980 Grid is EPSG:2326 - general knowledge, unverified in these sources); file name pattern `PROJ-ORIG-VOL-LOC-DISC-TYPE-...` max 43 characters; file < 500 MB; linked Revit files not exported unless bound.
- **Revit menu path (general knowledge):** File > Export > IFC > Modify setup (IFC version, Project Base Point/Survey Point coordinate base, user-defined property set file).
- **Typical MCP test requests (illustrative):** "Check that this IFC file name follows DEVB 43-character container rule", "List all IfcWall without Pset_WallCommon.FireRating", "Is the model file under 500 MB?", "Which BIM uses are mandatory at construction stage under TC(W) 1/2025?" (answer from Annex 1).

---

## 6. Local terminology

| Native term | Transliteration | English |
|---|---|---|
| 建築信息模擬 (HK official) | jiànzhù xìnxī mónǐ / Cantonese gin3 zuk1 seon3 sik1 mou4 ngai5 | Building Information Modelling (BIM) |
| 建築資訊建模 / 建築資訊模型 (Taiwan) | jiànzhù zīxùn jiànmó / móxíng | BIM |
| 建築信息模型 (Mainland/Macau usage, unverified) | jiànzhù xìnxī móxíng | BIM model |
| 發展局 | Fāzhǎn jú | Development Bureau (HK) |
| 工務科 | gōngwù kē | Works Branch |
| 工務技術通告 | gōngwù jìshù tōnggào | Technical Circular (Works) |
| 建造業議會 | jiànzào yè yìhuì | Construction Industry Council (CIC) |
| 屋宇署 | wūyǔ shǔ | Buildings Department |
| 認可人士 | rènkě rénshì | Authorized Person (AP) |
| 電子資料呈交及處理系統 | diànzǐ zīliào chéngjiāo jí chǔlǐ xìtǒng | Electronic Submission Hub (ESH) |
| 房屋委員會 | fángwū wěiyuánhuì | Housing Authority |
| 地政總署 | dìzhèng zǒngshǔ | Lands Department |
| 行政院公共工程委員會 / 工程會 | gōngchénghuì | Public Construction Commission (Taiwan) |
| 內政部國土管理署 | guótǔ guǎnlǐ shǔ | Land Administration Agency (formerly 營建署 Construction and Planning Agency) |
| 內政部建築研究所 | jiànzhù yánjiū suǒ | Architecture and Building Research Institute (ABRI) |
| 財團法人台灣建築中心 | Táiwān jiànzhù zhōngxīn | Taiwan Architecture and Building Center (TABC) |
| 我國BIM協同作業指南 | wǒguó BIM xiétóng zuòyè zhǐnán | Taiwan BIM Collaboration Guide |
| 共用資料環境 / 共通資料環境 | gòngyòng/gòngtōng zīliào huánjìng | Common Data Environment (CDE) |
| 竣工模型 | jùngōng móxíng | As-built model |
| 統包 | tǒngbāo | Design-build |
| 碰撞/干涉檢討 | pèngzhuàng / gānshè jiǎntǎo | Clash detection |
| 工務工程 | gōngwù gōngchéng | Capital works (HK) |
| 土地工務局 (DSSCU) | tǔdì gōngwù jú | Land and Public Works Bureau (Macau, name unverified) |

---

## Typical questions people ask about this

1. Which Hong Kong public projects must use BIM, and what is the cost threshold? (Real topic: DEVB blog on BIM, HK$30 million) [8] https://www.devb.gov.hk/tc/home/my_blog/index_id_1597.html
2. Is BIM mandatory for private developments and for Buildings Department submissions? When? [4][8]
3. What happened to the 2017 to 2021 circulars; is TC(W) 2/2021 still valid? (Superseded by 1/2025 on 1 February 2025) [1]
4. What does "contractually binding BIM model" mean in tenders from 1 April 2025? [1]
5. Which IFC version and MVD should I use for Hong Kong government deliveries? (IFC4, Reference View v1.2) [3]
6. Which coordinate system should HK models use, and how do I set the Revit project base point? [3] (illustrative follow-up)
7. How long can an HK BIM model file name be? (43 characters; objects 30) [3]
8. How do I export IFC from Revit for the BD BIM Structure Tool? (BD publishes an IFC property set text file) [5]
9. If the BIM model and 2D plans disagree, which one prevails in HK statutory submission? (Plans) [5][6]
10. Is government BIM software-neutral? Can a tender specify Revit? (No) [1]
11. Does the Hong Kong government really not require BIM on all public works? (Earlier LegCo question on BIM application, 2013) https://www.info.gov.hk/gia/general/201301/30/P201301300294_print.htm [23] (search result, not opened)
12. Is there a Taiwan law that makes BIM mandatory on public works? (None found; PCC reference documents) [14]
13. Where is the PCC's reference manual for introducing BIM in public works? [14]
14. How should BIM clauses be written in Taiwan public design-build contracts? (TW-00-3 / TW-01 in the Collaboration Guide) [15]
15. How do you hand over a BIM model to maintenance in Taiwan public buildings (COBie)? [15][16]
16. Citizen proposal: should Taiwan grade BIM personnel like site managers' training? https://join.gov.tw/idea/detail/eecb28a1-88d2-4ebf-8284-a487ab436f8b [18] (title seen in search, not opened)
17. Does Macau require BIM for public works? (Unclear; possible DSOP requirement for designers) [21]
18. Is there a buildingSMART chapter in Taiwan or Macau? (Hong Kong yes; others not confirmed) [20]
19. (illustrative) Can an MCP tool validate that all IfcSpace have area quantities required for the BD BIM Area Tool?
20. (illustrative) Which Revit versions are supported by the BD BIM tools? (Area/SF/FS Revit 2023-2026; BST Revit 2024-2026) [5]
21. (illustrative) Which CIC templates must a tenderer provide with a BIM Execution Plan? (D5, D6, D7, D8, D9) [10]
22. (illustrative) What LOD does the Taiwan Land Administration Agency expect for facade and MEP? (LOD 300; structure 200) [16]

---

## Common pitfalls and misconceptions

- "Hong Kong requires IFC submission to BD." Not yet: BIM is supplementary, plans prevail; mandatory BIM e-submission is tentatively 2029 [4][6].
- "Mandatory BIM = all public works." Only capital works above HK$30 million, with exemptions for low-technical-content works [1].
- Confusing **TC(W) numbers**: 7/2017, 18/2018, 9/2019, 12/2020, 2/2021, 8/2021 (harmonisation), 1/2025 (current). Older ones are superseded [1].
- IFC version: HK says IFC4 with Reference View; many Revit users still export IFC2x3 Coordination View by habit, which violates the HK GBDR rule [3].
- Revit IFC export drops linked models and elements with identical Phase Created/Demolished [3].
- Taiwan BIM specification (建置規範) documents are contract-attached specifications for specific tenders, not national law; LOD is often AIA E202 style (100-500), not ISO 7817/LOIN [16].
- 營建署 vs 國土管理署: same function after reorganisation; older PDFs still say 營建署 [14][16].
- The Taiwan Collaboration Guide update report is a **research proposal**; it says it does not represent agency opinion [15].
- Traditional Chinese terminology differs: HK 建築信息模擬 vs Taiwan 建築資訊建模.
- Do not assume Macau follows Hong Kong rules.

---

## Gaps

- Could not open: BD ADM-19 and the BIM submission guidelines text; CIC BIM Standards PDF (over size limit); Railway Bureau guide (over size limit); Taiwan PCC reference manual (garbled PDF fonts); buildingSMART chapter directory (403); iThome article (403); Macau Legislative Assembly PDF (empty). Statements from these are marked unverified.
- No search budget remained after the first rounds, so Taiwan open-source/enthusiast projects, Macau, final HK roadmap and exact Taiwan IFC requirements are thin.
- Skipped: no suspicious or pirated sites were encountered.

## Sources

- [1] DEVB TC(W) No. 1/2025 - https://devb.gov.hk/filemanager/technicalcirculars/en/upload/1401/1/C-2025-01-01.pdf
- [2] CIC "BIM Policy in HK" - https://bim.cic.hk/en/bim_in_hk
- [3] DEVB BIM Harmonisation Guidelines for Works Departments v3.0 (Dec 2025) - https://www.devb.gov.hk/filemanager/en/content_1287/DEVB BIM Harmonisation Guidelines for WDs (v3_0).pdf
- [4] BD ESH Newsletter 2024-1 - https://bd.gov.hk/doc/en/resources/online-tools/electronic-submission-hub/newsletter/ESH_newsletter_2024_1.pdf
- [5] BD BIM Automated Checking Tools - https://www.bd.gov.hk/en/resources/online-tools/building-information-modelling/index.html (Chinese: https://www.bd.gov.hk/tc/resources/online-tools/building-information-modelling/index.html)
- [6] BD PNAP ADV-34 - https://www.bd.gov.hk/doc/en/resources/codes-and-references/practice-notes-and-circular-letters/pnap/ADV/ADV034.pdf
- [7] DEVB consultation roadmap on BIM building plan submission (Chinese, Dec 2023) - https://www.devb.gov.hk/filemanager/tc/content_2373/BIM-Book-content-cn.pdf
- [8] DEVB Secretary's blog, 23 Nov 2025 - https://www.devb.gov.hk/tc/home/my_blog/index_id_1597.html
- [9] Government press release, ESH Stage 3, 30 June 2024 - https://www.info.gov.hk/gia/general/202406/30/P2024062800711.htm
- [10] CIC BIM Standards - General (2024) - https://www.bim.cic.hk/en/resources/publications_detail/151
- [11] CIC page for TC(W) adoption circular - https://www.bim.cic.hk/en/resources/publications_detail/118
- [12] Housing Authority BIM page - https://www.housingauthority.gov.hk/en/business-partnerships/resources/building-information-modelling/
- [13] Lands Department BIM and GIS Data Integration Guidelines (June 2023) - https://www.landsd.gov.hk/doc/en/bim/BIM%20and%20GIS%20Data%20Integration%20Guidelines.pdf
- [14] PCC BIM zone - https://www.pcc.gov.tw/content/index?eid=1345&type=C
- [15] ABRI-funded TABC report, Dec 2023 (BIM application promotion plan) - https://ws.moi.gov.tw/001/Upload/404/relfile/9489/315634/0cccc6e2-2dc6-496f-a45f-69b60e2811b1.pdf
- [16] Land Administration Agency construction-stage BIM spec (hosted by PCC) - https://www.pcc.gov.tw/content/Download.ashx?u=LzAwMS9VcGxvYWQvMjk3L2NrZmlsZS8xYjRiYjdiMy03MTc3LTRmNTktODNkMy0xOGM3NWE4YjNiMjQucGRm&n=6ZmE5Lu2Ml%2FlhafmlL%2Fpg6jlnIvlnJ%2FnrqHnkIbnvbLmlr3lt6Xpmo7mrrVCSU3lu7rnva7opo%2Fnr4Qo6YGp55So5bu656%2BJ44CB5rC06Zu744CB56m66Kq%2F5ZCI5L215oub5qiZKSgxMTHlubQxMOaciCkucGRm&icon=.pdf
- [18] Search-result-only (not opened): NTU BIM center article https://www.ntubim.net/bim2356027396/1404527 ; CPWEIA https://www.cpweia.org.tw/project/bim-project/ ; join.gov.tw proposal above ; iThome https://ithelp.ithome.com.tw/articles/10374556 ; TWARCHINDEX https://twarchindex.blogspot.com/2018/06/108111112_29.html ; PCC manual article https://www.ciche.org.tw/wordpress/wp-content/uploads/2017/09/DB4404-P018-%E5%85%AC%E5%85%B1%E5%B7%A5%E7%A8%8B%E5%9F%B7%E8%A1%8C.pdf
- [19] CIC Production of BIM Object Guide (mirror on community site, search result) - https://kctang.com.hk/web/sites/default/files/UsefulReferences/CIC%20Production%20of%20BIM%20Object%20Guide%20-%20General%20Requirements%20(2021).pdf
- [20] buildingSMART Hong Kong chapter - https://www.buildingsmart.org/community/chapter-directory/buildingsmart-hong-kong (403 to fetch; from search summary)
- [21] Macau Legislative Assembly document (not opened) - https://al.gov.mo/uploads/attachment/2025-09/6993768b913889b988.pdf
- [22] CIC "Global IFC Mandates" page - https://www.bim.cic.hk/en/resources/publications_detail/153
- [23] LegCo LCQ5 BIM (2013) - https://www.info.gov.hk/gia/general/201301/30/P201301300294_print.htm
- [24] DEVB TC(W) archive examples - https://www.devb.gov.hk/filemanager/technicalcirculars/en/upload/354/1/C-2017-07-01.pdf ; https://www.devb.gov.hk/filemanager/technicalcirculars/en/upload/366/1/C-2018-18-01.pdf ; https://devb.gov.hk/filemanager/technicalcirculars/en/upload/387/1/C-2021-02-02.pdf
- [25] HKIBIM - https://www.hkibim.org
- [27] Chambers article on Macau Law 10/2025 - https://chambers.com/articles/macau-s-new-public-procurement-law-law-no-10-2025-a-long-overdue-update
- [28] DSSCU site - https://www.dsscu.gov.mo/pt/
- [30] CIC BIM about-us page (CCBC(A) deadline) - https://bim.cic.hk/en/about_us/page/task_force_on_bim_submissions_to_the_buildings_department
