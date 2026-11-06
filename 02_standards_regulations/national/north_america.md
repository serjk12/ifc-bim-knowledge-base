# USA and Canada: BIM/IFC requirements

## In plain words

Neither the USA nor Canada has a single national BIM/IFC mandate. In the USA, BIM requirements come from individual **owners**: federal agencies (GSA, US Army Corps of Engineers, Veterans Affairs and others), state departments of transportation (DOTs), universities and private owners. Each writes its own "owner project requirements". The nearest thing to a national standard is **NBIMS-US** from the National Institute of Building Sciences (NIBS), which is voluntary [6][10]. NBIMS-US now has a fourth version built around the handover spreadsheet format **COBie** and ISO 19650-style requirements/execution-plan documents [2][8]. On the infrastructure side, the Federal Highway Administration (FHWA) and AASHTO (the association of state highway and transportation officials) run a coordinated "BIM for Infrastructure" and "BIM for Bridges and Structures" effort. FHWA describes IFC as a voluntary, non-binding exchange format [13][15]. Canada is similar: BIM is not mandatory nationally [10]. The federal public-works department (PSPC) is reported to favour non-proprietary "OpenBIM" and the IFC format [10], and BIM community work is led by the Canada BIM Council (CanBIM) and buildingSMART Canada [10][12]. For an MCP tester, the practical result is that IFC files from North America vary a lot. Expect IFC2x3 or IFC4 exported from Revit, COBie spreadsheets at handover, OmniClass or Uniformat codes, and US-specific coordinates (State Plane, NAD83, NAVD88, US survey feet). Treat any claim of "the US IFC requirement" with suspicion.

Last researched: 2026-11-06. QA pass 2026-11-06: COBie timeline (Wikipedia), IFC version table (Wikipedia), revit-ifc and IfcOpenShell GitHub README claims were re-fetched and confirmed; NBIMS-US FAQ page re-read (it carries only generic, 2006-era text and no release date). See `_meta/qa/qa-standards-2.md`.

> Research limits (read first): the web-search budget for this run was exhausted before any search ran, so this document is based only on pages that could be fetched directly. Several official pages returned HTTP 403/404 (gsa.gov, buildingsmart.org, highways.dot.gov, transportation.org, quebec.ca, canada.ca). The GSA, USACE, state-DOT and Quebec parts below are therefore thin, and statements from general knowledge are marked "(unverified)". See "Gaps". Real forum questions could not be searched; every question listed is "(illustrative)".

---

## 1. USA: who requires what

### 1.1 Overview table

| Level | Body | What it does | Binding? | Source |
|---|---|---|---|---|
| National standard | NIBS (National Institute of Building Sciences), NBIMS-US | Consensus standard: BIM requirements, execution planning, BIM uses, COBie, product data | Voluntary; adopted by owners via contract | [1][6][8] |
| Federal owner | GSA (General Services Administration) | 3D-4D-BIM program and "BIM Guide" series (2000s); COBie in P-100 capital program documents from 2017 per Wikipedia | Contractual for GSA projects | [9]; guide numbers (unverified) |
| Federal owner | USACE (Army Corps of Engineers) | Originated COBie (Bill East, ERDC-CERL, 2007); requires COBie on its projects (unverified detail) | Contractual | [9][10] |
| Federal infrastructure | FHWA | BIM for Infrastructure, 3D engineered models, digital as-builts (DABs), BIM for Bridges and Structures | Promotional/technical assistance; not a mandate | [13][14][15][17] |
| States | State DOTs (Iowa, Florida, New York and others as case studies) | Own digital-delivery/3D-model practice | Per state | [14][16] |
| Standards bodies | buildingSMART International (IFC, IDS, bSDD, BCF), ISO | IFC is ISO 16739-1 | Voluntary, referenced by owners | [11][12][20] |

There is **no federal law** requiring BIM for private buildings. Wikipedia states the US "has not adopted a set of national BIM guidelines" comparable to the UK, so competing systems coexist [10]. NIBS is described there as having studied UK experience (2021) to build a national BIM program [10].

### 1.2 NBIMS-US (National BIM Standard-United States)

- Published by NIBS (a US non-profit chartered by Congress, home of the NIBS BIM Council and the former buildingSMART alliance, the US buildingSMART chapter (unverified detail on chapter status)). Landing page: <https://www.nibs.org/nbims> [1].
- **Versions**: V1 (2007) and V2 (2012) are older (years unverified; the COBie article does say COBie 2.26 was approved into NBIMS-US v2 in December 2011 [9]); **V3 was published in 2015** and included COBie, the BIM Project Execution Planning Guide and Templates, BIM-use definitions and a contracting framework [7]. **V4** moves from one PDF to a library of modules, with a full update every three years and interim modules [7]. V1-V3 remain available at nationalbimstandard.org with archival copies [2].
- **V4 modules** (seven): Introduction, Project BIM Requirements (PBR), BIM Execution Planning (BEP), BIM Use Definitions (BUD), Information Exchange Guidelines (not yet released), Product Data Requirements, and **COBie V3** [2].
- **V4 aligns with ISO 19650.** Figures map PBR, BEP and COBie to ISO 19650-2 processes. Owner = "Appointing Party", delivery team = "Appointed Parties" [2][4]. The V4 FAQ itself does not mention ISO 19650 or a mandate; adoption is voluntary [6].
- **IFC**: NBIMS-US uses ISO 16739 (IFC) as the common data schema for the COBie exchange. The BEP supports buildingSMART **Information Delivery Specifications (IDS)** as IFC exchange definitions where available, and references the BIMForum LOD Specification [2]. The PBR module mentions IDS only once ("eMVD or IDS") and does not name IFC [4].
- **Replaced content**: the V2 BEP Guide is replaced by the BEP module, V3 "The Uses of BIM" by the BIM Use Definitions module, and COBie 2.4 by COBie V3 [2].
- It also references ANSI/ASHRAE/NIBS Standard 224-2023, which draws on the same National BIM Guide for Owners as the PBR module [2].

### 1.3 COBie (Construction Operations Building information exchange)

COBie is the most commonly encountered US "BIM deliverable" an MCP tester will meet.

| Item | Detail | Source |
|---|---|---|
| Origin | Devised by Bill East at the US Army Corps of Engineers (Construction Engineering Research Laboratory) in 2007 | [9][10] |
| 2009 | COBie 2.26 published as a buildingSMART "Basic FM Handover" Model View Definition (MVD) on IFC2x3 | [9] |
| 2011 | Approved in NBIMS-US v2 (December 2011 per another page) | [9][10] |
| 2014 | UK BS 1192-4:2014 (COBie in UK practice) | [9] |
| 2015 | COBie 2.4 in NBIMS-US Chapter 4.2, based on IFC4 | [9] |
| 2017 | GSA required COBie in P-100 capital program documents | [9] |
| 2023 | **COBie V3** published as part of NBIMS-US V4 (developed 2015-2022, 58 updates) | [3] |
| 2021 | buildingSMART dropped the COBie name for its ISO-track successor, now "Facility Management Handover - Equipment Maintenance" | [9] |

COBie V3 facts [3]:
- It is a "data format and process standard" for maintainable assets: space, product and equipment schedules plus as-built, O&M and commissioning data, delivered at handover.
- It is an MVD (subset of IFC); V2.4 was updated to IFC4; the page cites IFC as ISO 16739-1:2018.
- Delivered as a SpreadsheetML (Excel-type) workbook, JSON, or IFC.
- **19 data tables**: Overall (Facility, Company); Spatial (Level, SpaceType, Space, Zone, Coordinate); Asset (Type, Component, System, Attribute); Process (Instruction, Job, Event, Package, Risk); Support (Document, Resource, PickList).
- Fill rule: use "n/a" for text and "0" for numeric fields when no value applies.
- The Instruction table holds units, measurement standards and submittal information.
- Validation: automated tools are recommended; reviewers are assigned in the BIM/COBie execution plan (specific tools not named on the fetched page).

### 1.4 Project requirements and execution plans (what an "EIR/BEP" looks like in the US)

- **PBR (Project BIM Requirements)** has three levels modelled on ISO 12911: 5.1 Executive (deliverables, quality, IP, security), 5.2 Management (BEP, roles, CDE, collaboration), 5.3 Working/Technical (BIM uses, model requirements, modeling requirements, data requirements). Most elements use "The OPR shall..." (Owner Project Requirements). Deliverable formats are left to the OPR; data deliverables must be "an industry standard format (e.g., COBie)" or owner-defined [4].
- **BEP module** fields relevant to model checking [5]:
  - Information Exchange table with a format field; example "IFC 4 Design Transfer View by BuildingSMART International"; ".idsxml" as an example exchange definition.
  - Software compatibility testing (export/import application, test date).
  - **Georeferencing** (Section 5.11): reference coordinate system (State Plane, UTM), UTM zone, horizontal and vertical units, datums (examples **NAD 83/2011** and **NAVD 88**), project origin latitude/longitude/elevation, grid offset from true north, reference survey path. The page notes that in Table 13 the origin longitude/latitude field names appear swapped relative to their descriptions.
  - **Naming convention** table (files, models, levels, elements), with the "NBIMS-US Core BIM Filename Convention" given as an example.
  - **Classification**: facility type by **OmniClass Table 11** or owner list; model element categories from OmniClass, Uniclass or CSI Uniformat (OmniClass Table 21 in examples).
  - **LOD / LOI / LOA**: BIMForum LOD Specification (2023), "BIMForum LOD 300" as example; USIBD Level of Accuracy ("USIBD LoA20").
  - Native formats are recorded per exchange (.rvt, .dgn, .xls).

### 1.5 Federal agencies (thin; verify before relying)

- **GSA**: runs a "3D-4D-BIM" program and a numbered "GSA BIM Guide" series (a 12 January 2009 "BIM Guide For 3D Imaging" is cited on Wikipedia [10]). Direct gsa.gov program pages returned 404, so exact guide numbers/titles (BIM Guide 01 Overview ... 08 Facility Management, etc.) are **(unverified)**. COBie in P-100: 2017 per [9].
- **USACE**: origin of COBie [9]; its CAD/BIM Technology Center and BIM Minimum Modeling Matrix (M3) are **(unverified)**; the cadbim host could not be resolved from here.
- **VA, NASA, DoD, Navy**: BIM manuals exist (VA BIM Manual) **(unverified)**; page not reachable.

---

## 2. USA: infrastructure (FHWA, AASHTO, state DOTs)

| Item | Detail | Source |
|---|---|---|
| FHWA BIM for Infrastructure | Program to describe BIM, share DOT practice, and help DOTs move between maturity levels; frames BIM as "data is an asset"; four components: tools/technology, people/skills, data/standards, policies/processes | [13][14] |
| FHWA 2020 products | Tech briefs HIF-20-055 "Advancing the Development and Deployment of BIM for Infrastructure", HIF-20-056 "The Dimensions of BIM for Infrastructure", HIF-20-084 "Hybrid Approach to BIM in Iowa"; case studies: Iowa DOT I-80/I-380 ramps (3D model deliverable), NYSDOT Kew Gardens, FDOT data governance | [14] |
| FHWA Bridges and Structures | IFC described as a voluntary, non-binding exchange format; page names **IFC4x2** via the "IFC Bridge Design to Construction Exchange (U.S.)" developed by NIBS in 2016; does not mention IFC 4.3 | [15] |
| AASHTO roadmap | "AASHTO BIM Roadmap for Bridges and Structures", December 2020 | [15] |
| FHWA bridge reports | FHWA-HIF-16-003 (2013), -16-010 (2015), -16-011 (2016), -21-031 "Demonstration of Bridge Project Delivery Using BIM" (2021), -24-004 "BIM Workflows and Centralized BIM Transportation Library for Bridges and Roadways" (2024), -24-060 (2024) | [15] |
| Pooled funds | TPF-5(372) "BIM for Bridges and Structures"; "BIM for Infrastructure" solicitation 1547, lead agency Iowa DOT, 24 partner states, commitment period 2021-2026, solicitation expires 31 Dec 2026 | [15][16] |
| Digital as-builts (DABs) | Digital project records (searchable, geospatial, interoperable) for lifecycle asset management; part of FHWA Every Day Counts; page does not mention LandXML or IFC | [17] |
| 3D engineered models | FHWA EDC technology; page (2017) lists case studies and training; no file formats named | [18] |

Important for testers: the fetched FHWA pages **do not state a mandate** and **do not say "AASHTO has adopted IFC 4.3"**. The claim in the task brief ("AASHTO adoption of IFC 4.3 for bridges and roads") is **(unverified)**; what is verified is the FHWA IFC4x2 bridge exchange (2016) and the AASHTO roadmap (2020). In practice, much DOT digital delivery is LandXML/CAD-based (unverified), not IFC.

---

## 3. IFC in the North American workflow

- **IFC versions** [11]: IFC2x3 (2006), IFC4 (2013), IFC4 Add1 (2015), Add2 (2016), Add2 TC1 (2017), IFC4.1 (withdrawn), IFC4.2 (2019, withdrawn), **IFC4.3 Add2 (2024)**. **ISO 16739-1:2024** is the registered international standard for IFC 4.3 [11]; ISO 16739-1:2018 corresponds to IFC4 [3].
- **No US/Canadian national IFC profile** was found. IFC requirements are set per owner in the OPR/BEP; the NBIMS-US BEP simply names the IFC view (for example "IFC 4 Design Transfer View") [5].
- **Revit**: Autodesk's IFC exporter is open source (LGPLv2; re-confirmed in QA) at github.com/Autodesk/revit-ifc; its About section lists Revit 2019+ (and Navisworks 2019-2024); the README does not state which IFC schema versions it supports and does not mention IFC4.3, overrides the built-in component, and supports "the most current annual version and two previous versions"; the README references Revit 2027 branch Release_27.x.x [21]. Export path File > Export > IFC with named setups such as "IFC2x3 Coordination View 2.0", "IFC4 Reference View", "IFC4 Design Transfer View" is **(unverified, from general knowledge)**.
- **IfcOpenShell** parses IFC2x3 TC1, IFC4 Add2 TC1, IFC4x1, IFC4x2 and IFC4x3 Add2; geometry is extensive only for IFC2x3 and IFC4 Add2 TC1 [22] (re-confirmed in QA; the repository is licensed LGPL-3.0, with Bonsai and ifcsverchok GPL-3.0). Useful for QA scripts.
- **IDS (Information Delivery Specification)**: computer-readable XML checking rules for IFC; repository github.com/buildingSMART/IDS [20]; NBIMS-US BEP lists .idsxml as an exchange definition [5].
- **Classification**: OmniClass (Tables 11, 21), Uniformat, MasterFormat; Uniclass also allowed [5]. Which Canadian classification is mandated is unknown (unverified).
- **Georeferencing**: State Plane / UTM, NAD83(2011), NAVD88 [5]. In IFC, expect IfcMapConversion/IfcProjectedCRS (IFC4+) with an EPSG code (general IFC knowledge, unverified here); US survey feet vs international feet is a classic trap.

---

## 4. Canada

| Topic | Verified information | Source |
|---|---|---|
| Mandate | "BIM is not mandatory in Canada" (Wikipedia) | [10] |
| PSPC (Public Services and Procurement Canada, formerly PWGSC) | Reported as committed to non-proprietary "OpenBIM" standards; avoids specifying a proprietary format; designers must use IFC for interoperability. No year given. Primary PSPC page not retrievable | [10] |
| Canada BIM Council (CanBIM) | Founded 2008 to support BIM adoption; its web address now redirects to buildingtransformations.org, a community with events (Toronto Summit 2026, Halifax national summit, a 2026 US Summit), Innovation Spotlight Awards, membership and a certification link; the page does not confirm the relationship | [10][19] |
| Institute for BIM in Canada (IBC) | Supporter of BIM adoption; no year | [10] |
| buildingSMART Canada | Canadian chapter of buildingSMART International; listed among national chapters | [10][12] |
| Quebec | Roadmap/government requirements **not verified**; the quebec.ca page I guessed returned 404 | none |

Unverified, from general knowledge: Quebec has a provincial BIM adoption effort, and Canadian classification uses CSC/CSI MasterFormat and Uniformat; confirm with CanBIM/Quebec sources before using in tests.

---

## 5. Key organizations

| Organization | Role |
|---|---|
| NIBS | Publishes NBIMS-US; BIM Council; NBIMS-US Planning Committee oversees V4 content [7] |
| buildingSMART International | IFC, IDS, bSDD, BCF; has US, North America and Canada chapters [12] |
| BIMForum | LOD Specification (referenced by NBIMS-US BEP) [2] |
| USIBD | Level of Accuracy specification [5] |
| FHWA / AASHTO / state DOTs / pooled funds | Infrastructure BIM [13][15][16] |
| CanBIM / Building Transformations; IBC; buildingSMART Canada | Canadian community [10][19] |

Local software and community (partly unverified): Autodesk Revit/Civil 3D, Bentley, Trimble, Procore and Bluebeam are US/CA-widely used (general knowledge). Open source: IfcOpenShell/Bonsai [22], Autodesk revit-ifc [21]. COBie validation tools exist (free tools mentioned on the COBie page [3]; names not given there).

---

## 6. Local terminology

| US/Canadian term | English meaning |
|---|---|
| OPR (Owner's Project Requirements) | Owner's brief; US analogue of ISO 19650 EIR/OIR [4] |
| PBR / BEP / BUD | NBIMS-US modules: Project BIM Requirements / BIM Execution Plan / BIM Use Definitions [2] |
| CDE | Common Data Environment [4] |
| MET (Model Element Table) | Table of elements with required LOD/LOI [5] |
| LOD / LOI / LOA | Level of Development / Information / Accuracy [5] |
| COBie | Handover spreadsheet/IFC subset [3] |
| DAB | Digital As-Built [17] |
| DOT / FHWA / AASHTO | State/federal transportation bodies |
| EDC | FHWA "Every Day Counts" innovation program [17] |
| P-100 | GSA Facilities Standards (unverified detail) |
| OmniClass / Uniformat / MasterFormat | Classification systems (CSI); numbering of tables per [5] |
| State Plane, NAD83, NAVD88 | Coordinate/vertical datum |
| Modélisation des données du bâtiment (MDB) | Quebec French term for BIM (unverified) |
| PSPC (SPAC in French) | Public Services and Procurement Canada (unverified abbreviation) |

---

## Typical questions people ask about this

All are (illustrative); no real forum threads could be searched.

1. Does the US government require IFC for BIM deliverables? (illustrative)
2. Is there a US national BIM mandate like the UK's? (illustrative; see [10])
3. What is COBie and which IFC version does it use? (illustrative; see [3])
4. Do I submit COBie as a spreadsheet or inside IFC? (illustrative)
5. Which IFC export setup should I choose in Revit for a US project? (illustrative)
6. How should I georeference an IFC with State Plane coordinates in US survey feet? (illustrative)
7. What is the difference between NBIMS-US V3 and V4? (illustrative; see [2][7])
8. Do state DOTs accept IFC or LandXML for roads? (illustrative)
9. Has AASHTO adopted IFC 4.3 for bridges? (illustrative; unverified)
10. What does PSPC require for BIM on federal buildings? (illustrative)
11. Is BIM mandatory in Canada or Quebec? (illustrative; see [10])
12. Which classification do I use in the US: OmniClass or Uniformat? (illustrative)
13. How do I validate a COBie file and an IFC against owner requirements (IDS)? (illustrative)
14. What are digital as-builts and do they use IFC? (illustrative)

---

## Common pitfalls and misconceptions

- "The US mandates IFC" is false at national level; requirements are per owner [4][5][13][15].
- "COBie is only a spreadsheet": it is an MVD of IFC that can be spreadsheet, JSON or IFC [3].
- Version confusion: COBie 2.4 (NBIMS-US V3, IFC4-based) versus COBie V3 (NBIMS-US V4, 2023) [3][2].
- FHWA's 2016 bridge exchange used IFC4x2; do not assume IFC 4.3 adoption without a primary source [15].
- Units and datums: US survey foot, State Plane vs UTM, NAD83(2011), NAVD88 [5].
- NBIMS-US V4 Information Exchange Guidelines module was not released at V4 launch [2].
- The CanBIM web address now redirects to a different brand; do not assume the old site is live [19].

---

## Gaps

- Search was unavailable; GSA guide numbers and titles, USACE requirements, VA/NASA/DoD manuals, state DOT policies (Wisconsin, Texas, Ohio and others), AASHTO IFC 4.3 positions, buildingSMART US/Canada chapter details, PSPC documents and the Quebec roadmap were not verified.
- gsa.gov, buildingsmart.org, highways.dot.gov, transportation.org, quebec.ca, canada.ca and several nibs.org module paths returned 403/404 or certificate errors.
- No real community Q&A threads were reachable. No suspicious sites were encountered.

## Sources

[1] https://www.nibs.org/nbims
[2] https://www.nibs.org/nbims/v4/introduction
[3] https://nibs.org/nbims/v3/cobie/
[4] https://nibs.org/nbims/v4/pbr/
[5] https://nibs.org/nbims/v4/bep/
[6] https://nibs.org/nbims/v4/faqs/
[7] https://nibs.org/nbims/about/
[8] https://www.nibs.org/nbims/v4
[9] https://en.wikipedia.org/wiki/COBie
[10] https://en.wikipedia.org/wiki/Building_information_modeling
[11] https://en.wikipedia.org/wiki/Industry_Foundation_Classes
[12] https://en.wikipedia.org/wiki/BuildingSMART
[13] https://www.fhwa.dot.gov/infrastructure/bim/
[14] https://www.fhwa.dot.gov/construction/bim/
[15] https://www.fhwa.dot.gov/bridge/bim/
[16] https://www.pooledfund.org/Details/Solicitation/1547
[17] https://www.fhwa.dot.gov/construction/dabs/
[18] https://www.fhwa.dot.gov/construction/3d/
[19] https://www.buildingtransformations.org/
[20] https://github.com/buildingSMART/IDS
[21] https://github.com/Autodesk/revit-ifc
[22] https://github.com/IfcOpenShell/IfcOpenShell
