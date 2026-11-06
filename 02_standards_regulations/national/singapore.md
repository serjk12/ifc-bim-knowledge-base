# Singapore: CORENET X and IFC-SG (very detailed)

## In plain words

Singapore is one of the few countries where building permits are issued from a BIM model, not from drawings. The government platform is called **CORENET X**. It is run by BCA (Building and Construction Authority) and URA (Urban Redevelopment Authority) together with five other agencies (LTA, NEA, NParks, PUB, SCDF). Designers upload IFC files, a "Model Checker" validates them, and the agencies review the model and send comments back as BCF issues. The IFC flavour required is officially written **IFC+SG** (many people still write "IFC-SG"). It is standard IFC4 (Reference View) plus Singapore-specific property sets ("SGPsets"), controlled values and modelling rules. Since 1 October 2025 submission through CORENET X is mandatory for large new projects, and from 1 October 2026 for new projects of 5,000 m2 GFA and above [1][2].

For an MCP tester: expect requests like "check this IFC against IFC+SG", "set SGPset_Wall properties", "export IFC4 Reference View from Revit with the Singapore setup", "why does the Model Checker fail QC05", "is the model on SVY21 / EPSG:3414".

Last researched: 2026-11-06

Research note: this document was built from the official CORENET X site (info.corenet.gov.sg), which was fetched directly, and from the BCA/URA circular of 23 July 2026 (read in full). The web-search budget ran out before searching for community discussions, buildingSMART chapter pages and the pre-2023 history, so those parts are marked "(unverified)" or listed under Gaps.

---

## 1. Who mandates what, and since when

### 1.1 Agencies

| Agency | Full name | Role in CORENET X |
|---|---|---|
| BCA | Building and Construction Authority (under the Ministry of National Development, MND) | Co-owner of CORENET X; building plan, structural (ST) and building-control approvals; owns the CORENET X website and Model Checker [1][3] |
| URA | Urban Redevelopment Authority | Co-owner; planning permission (PP) at the Design Gateway, Written Permission (WP) at Construction Gateway; also co-signs the implementation circulars [2][3] |
| LTA | Land Transport Authority | Roads, parking, rail protection clearances [1][4] |
| NEA | National Environment Agency | Environmental/sanitary/pollution clearances [4] |
| NParks | National Parks Board | Landscape, tree conservation, greenery [4] |
| PUB | Public Utilities Board (national water agency) | Drainage, sewerage, water services [4] |
| SCDF | Singapore Civil Defence Force | Fire safety (fire code approvals) [4] |

The initiative was started in 2018 by BCA and URA, developed with the other agencies and industry. More than 100 public and private professionals took part in co-creation. It was announced by the Minister for National Development at the International Built Environment Week on 7 September 2021, and soft-launched on 18 December 2023 [3][5]. Industry training on IFC+SG began in August 2022 [3].

### 1.2 Legal basis

- "Building And Related Works (Miscellaneous Amendments) Bill 2023" (4 July 2023) is listed among the official CORENET X documents, short link `go.gov.sg/cxbill2023` [5]. The exact statute amended (presumably the Building Control Act) is (unverified) from the pages I could read.
- Agencies state that the Code of Practice does not replace agency handbooks, circulars or other regulatory publications [6].

### 1.3 Mandate timeline (what is verified)

| Date | Event | Source |
|---|---|---|
| 2018 | CORENET X initiated by BCA and URA | [3] |
| 7 Sep 2021 | Minister's official announcement | [5] |
| Aug 2022 | First industry training (IFC+SG) | [3] |
| 1 Feb 2023 | "Circular on CORENET X" | [5] |
| 4 Jul 2023 | Building And Related Works (Miscellaneous Amendments) Bill 2023 | [5] |
| Sep 2023 | COP First Edition; 26 Sep 2023 "Circular on CORENET X Implementation Plan" | [5][6] |
| 18 Dec 2023 | Soft launch | [3] |
| 22 Dec 2023 | New Annex C (payment schedule) of Standard Consultancy Agreement for public projects | [5][7] |
| 23 Jan 2025 | Circular "Updates to CORENET X Implementation Plan" (content not read) | [5] |
| 10 Sep 2025 | Circular, BCA ref APPBCA-2025-20, URA ref URA/PB/2025/07-DCG: mandatory from 1 Oct 2025 for new projects >= 30,000 m2 GFA | [2][5] |
| 1 Oct 2025 | Mandatory CORENET X Gateway submission for new projects GFA >= 30,000 m2 | [2] |
| 23 Jul 2026 | Circular, BCA ref APPBCA-2026-12, URA ref URA/PB/2026/08-DCG: revised plan (below) | [2] |
| 1 Oct 2026 | Mandatory for all new projects GFA >= 5,000 m2 | [2] |
| Sep 2026 | COP Fourth Edition (COP 4.0) published | [6] |
| 1 Jan 2027 | COP 4.0 becomes mandatory for new gateway submissions | [6] |

### 1.4 Scope and thresholds (revised plan, circular of 23 July 2026) [2]

| Scope of projects | Requirement |
|---|---|
| All new projects with GFA >= 30,000 m2 | Mandatory via CORENET X Gateway Processes from 1 Oct 2025 (implemented) |
| All new projects with GFA >= 5,000 m2 | Mandatory via Gateway Processes from 1 Oct 2026 |
| Ongoing projects with GFA >= 5,000 m2 (already started submissions in CORENET 2 by 30 Sep 2026) | May continue in CORENET 2 "until further details are announced" |
| All projects with GFA < 5,000 m2 | Voluntary for now; may continue in CORENET 2. The earlier plan to force them in was dropped after industry feedback |

"New projects" means new buildings or works to existing buildings not yet formally submitted as a Development Application to URA or a Development Control application to LTA/NEA/NParks/PUB. Three triggers: (a) erection of building(s) with total GFA >= 5,000 m2; (b) additions or extensions creating >= 5,000 m2 additional GFA; (c) major A&A with affected or replaced GFA >= 5,000 m2 [2].

The circular states that BIM submissions in IFC+SG format are mandatory for new erections or major A&A projects with new GFA >= 5,000 m2 [2]. Smaller projects eligible for the Direct Submission Process are examples like single-unit landed houses, bus stops and linkways [2].

Reported adoption (as of July 2026): more than 140 projects and 300 firms had submitted via CORENET X, with claimed time savings of up to two months [2]. (Earlier page text: more than 100 firms by May 2025 [8].)

Important: the implementation-timeline web page shows its timeline as an image, so the figures above come from the circular, not the page text [5]. The page also says "Last Updated 16 May 2024" in its footer although it clearly has 2026 content; treat page footers as unreliable [5].

### 1.5 Earlier history: CORENET e-Submission and BIM e-Submission (unverified)

From general knowledge, not confirmed in this session: CORENET (Construction and Real Estate NETwork) e-Submission started in the late 1990s with 2D CAD submissions; BCA's BIM e-Submission became available around 2013 for architectural models, with structural and MEP following, and BIM submission became mandatory in stages from about 2013-2015 for large projects (thresholds around 20,000 m2 GFA were widely quoted). The BCA "BIM Roadmap" (2010) targeted 80% BIM use in the industry by 2015; the Wikipedia page for BCA confirms the 2015 80% target [9]. The legacy system is now called **CORENET 2.0** (CORENET 2), still used for smaller projects [2][10]. Treat all specific years here other than the 80%-by-2015 target as (unverified).

---

## 2. The CORENET X process

### 2.1 Gateways [4]

| Gateway | Code | Purpose | Key approvals |
|---|---|---|---|
| Pre-Submission Consultation | - | Guidance/waivers before formal submission | none |
| Design Gateway | G1 / DG | Multi-agency parameters before detailed design | URA Provisional Permission (PP); LTA/NEA/PUB DC clearances; NParks DC approval |
| Piling Gateway (optional) | G1.5 / PG | Piling and foundations only (pile caps, rafts, earth retaining) | BCA ST approvals for permanent piling; LTA RPZ AIP |
| Construction Gateway | G2 / CG | Coordinated design before main structural works and sales launch | URA Written Permission (WP); BCA BP and ST approvals; LTA street plan/parking/rails; NEA and PUB BP clearance certificate; SCDF BP approval |
| Independent Submissions | IDP | Agency-specific items without cross-agency dependency, run in parallel | e.g. NParks tree felling; PUB earth control measures |
| Completion Gateway | G3 / TOP | As-built; Temporary Occupation Permit (TOP) / Certificate of Statutory Completion (CSC) | TOP / CSC |

Official claim: "more than 20 approval stages" are reduced to 3 key submission milestones [3]. Independent-submission processing times (updated July 2024): BCA 15 working days; LTA 20; NEA 20; NParks 20; PUB 14 (Form B, sewerage) or 21 (water service installation, CSC); SCDF 5 [4]. Design/Construction gateway processing is 20 working days, extended to 30 if URA needs a further Design Advisory Panel (DAP) session [11].

The **Direct Submission Process (DSP)** is a single-stage approval for small projects: single-unit landed houses (default), pavilions, linkways, racking, and small A&A (e.g. affected GFA <= 1,000 m2 or 50% of existing GFA whichever is less, with no change of use) [12]. The DSP page does not explicitly say IFC+SG is required, only that envelope/massing modelling should follow the Glossary [12].

**Part ST submissions** (split structural submissions): building projects with GFA above 40,000 m2 and either 5+ blocks of 4+ storeys or 3+ such blocks on a common podium/basement; infrastructure over 150 m (building-like) or 400 m (engineering works). The first CG submission must contain the full coordinated structural BIM carcass model [11].

### 2.2 Submission package at Construction Gateway (typical) [13]

- 3D IFC+SG models, all geo-referenced: Architecture (Block 1, Block 2, Site); C&S Engineering (Blocks, Site, Substructure); M&E (Blocks, Main for ground and substructure levels).
- 2D drawings for details and external works; design calculation reports; forms (e.g. B-Score BDAS form); catchment plan; piling items (site investigation report in PDF and AGS format).
- If both 3D models and 2D plans are submitted, the cover letter must state which 2D plans are for approval; otherwise the 3D models take precedence [13].

### 2.3 The portal [14][15]

- Production: `portal.corenet.gov.sg`. Login is via Corppass (Singpass for Business); the company's Corppass administrator must authorise the e-service "CORENET X Industry Portal".
- Training environment: `training.corenet.gov.sg`; registration with a valid email (no Singpass); mock accounts for different roles; BIM viewer not available there; never enter real project data.
- Roles include Developer, Consultants (QP), Builder, checkers, resident engineers, plumbers, fire safety engineers, peer reviewers, transport consultants.
- Release notes: R13.0 (26 Mar 2026), R14.0 (21 May 2026), R15.0 (9 Jul 2026), R16.1 (17 Sep 2026). Examples: coordinated BIM sections now require signed (.ent) files; Quality Check can start on uploaded models in Piling Gateway submissions; unsigned/compressed files cannot be tagged as "Plans for Approval" [16].
- Agency comments come as BCF tagged to the model; amendment submissions need only the amended model with automatic deviation detection [3].

Differences CORENET 2 vs CORENET X: web-based with no ES Pro download; forms auto-populated; digital appointments (no wet ink); fees paid in portal before submission; responses digitally signed but not encrypted [10].

---

## 3. IFC+SG: what it is and what it requires

### 3.1 Definition

- Official: "IFC+SG defines how BIM models are structured for CORENET X submission. It combines IFC with Singapore-specific information so agencies can read, review, and check model data." [17]
- Footnote of the circular: IFC is the openBIM standard of buildingSMART International; "IFC+SG is an extension of this openBIM standard that is developed to cater to local regulatory requirements." [2]
- Naming: official pages say **IFC+SG** (the user-facing brief says IFC-SG). Both refer to the same thing; the URL path is `/ifc-sg/`.
- Schema/MVD: the Model Checker states the export must be **IFC4 Reference View**, following the IFC+SG export settings; other IFC versions or MVDs are not supported for submission [18]. IFC4 Reference View is the buildingSMART MVD for IFC4 (ISO 16739-1:2018 is IFC4 ADD2 TC1; this ISO number is from general knowledge, (unverified) in this session). The Revit guide does not itself mention "Reference View" [19].
- Model Checker error code `IFC0000101` = "Unsupported IFC version or MVD" [18].

### 3.2 Data structure [20]

- Spatial structure: IfcProject > IfcSite > IfcBuilding > IfcBuildingStorey > IfcSpace. The site stresses that IFC+SG is not a single top-down hierarchy; property sets attach data to objects.
- Property sets: standard Psets (Pset_WallCommon, Pset_DoorCommon, Pset_SpaceCommon) plus **SGPsets** named by pattern `SGPset_<Thing>`, e.g. SGPset_Wall, SGPset_Door, SGPset_Space.
- The full list of SGPsets, properties and controlled values lives in the **IFC+SG Excel Mapping File** (see 3.3). Individual SGPset property names are not reproduced here because the page text did not list them (unverified).
- Subtypes: use standard IFC PredefinedType where available, and `USERDEFINED` with a Singapore subtype value where the IFC+SG requires it [21]. Revit setup includes "IFC+SG Subtype Files" [19].

### 3.3 Excel mapping file [22]

- File name: `industry-mapping-09-2026.xlsx`; page states "Version: 22 September 2026".
- Start at the tab "CX Pilot Mapping". It lists, for each building element: IFC entity (e.g. IfcWall, IfcSlab, IfcDoor, IfcSpace) and subtype, mandatory SGPsets, relevant standard Psets, property names, controlled values and submission checks.
- Use together with the COP and the **Glossary of Identified Components** [22][23].

### 3.4 Georeferencing, levels, GUIDs [6][21]

- Federated models are geo-referenced to **SVY21 (EPSG:3414)** for easting/northing and to **Singapore Height Datum (SHD)** for height [6].
- Set project coordinates before export; Revit guide says check **Coordinate Base** for all models [19].
- GUIDs must remain unique when copying blocks, templates or linking discipline models [21].
- Export gridlines across all storeys [21].
- Components need not look real, but must carry IFC+SG data and minimum dimensions (a tree can be a simple object with "Landscape Plants" parameters such as Girth, Height, Status) [6].
- Block mechanism: models are organised in blocks aligned across ARC/C&S/MEP (IFC+SG Block Mechanism, referenced in modelling practices) [21].

### 3.5 Model Checker (MVP) [18]

| Layer | Status | Content |
|---|---|---|
| IFC Schema Check | Live | File validity, schema, integrity, mandatory attributes, spatial hierarchy |
| Quality Check (QC) | Live | QC01 building storey naming; QC02 clash detection (1 mm tolerance, structure prioritised); QC03 modelling inputs (properties, Psets, IFC entity mapping); QC04 room tagging coverage of slabs (structural areas excluded); QC05 coordinate alignment across discipline models; QC06 level consistency (storey names and finished floor levels) |
| Regulatory Compliance Check (RC) | Upcoming | Automated assessment of selected regulatory requirements |

Result classes: **Pass**, **Fail** (must fix), **Alert** (QP to verify). Results can be downloaded as BCF. Schema error codes: IFC0000001 file cannot be read; IFC0000101 unsupported IFC version/MVD; IFC0000102 no IfcSite; IFC0000103 non-standard or abstract entity types; IFC0000104 invalid or incomplete IFC data; IFC0000106 no valid IfcProject [18]. It can be used as a Pre-Submission Check or inside a formal submission. Release notes also mention "hygiene check" modals and throttled pre-check QC per project [16].

### 3.6 Classification

No national classification system dedicated to IFC+SG was found in the sources read. Classification in IFC+SG is done through IFC entity + subtype + SGPset values, and the Archicad workflow lists a "Classification" step [24]. Whether Uniclass or another scheme is required is (unverified).

---

## 4. Official documents

| Document | Version/date | Link / short link | Source |
|---|---|---|---|
| CORENET X Code of Practice (COP) | Fourth Edition (COP 4.0), Sep 2026; 3.1 (Dec 2025); Third (Sep 2025); 2.1 and Second (Nov 2024); First (Sep 2023). COP 4.0 effective 1 Jan 2027; vendor config files expected Nov 2026 | `go.gov.sg/cxcop`; PDF names such as `corenet-x-cop---4-edition-2026.pdf` | [6] |
| Circular APPBCA-2025-20 / URA/PB/2025/07-DCG | 10 Sep 2025 | info.corenet.gov.sg circulars page | [2][5] |
| Circular APPBCA-2026-12 / URA/PB/2026/08-DCG | 23 Jul 2026 | `.../docs/default-source/bca-circulars/circular-for-updates-to-corenet-x-implementation-plan.pdf` | [2] |
| CORENET X Good Practices Guidebook | Dec 2025 | `go.gov.sg/cxgoodpracticesguide` | [2][8] |
| Submission Portal User Manual | Jan 2026 | `go.gov.sg/cx-sp-user-manual` | [2] |
| IFC+SG Knowledge Hub | 2026 | `info.corenet.gov.sg/ifc-sg/start-here/WhatIsIFCSG` | [2][17] |
| Singapore BIM Guide V2 | no date on page | via relevant-documents page | [25] |
| BIM Handover Technical Guide; BIM Particular Conditions V2; BIM Essential Guide for BIM Execution Plan; Model Contents Requirements | no dates on page | via relevant-documents page | [25] |
| Helpdesk / queries | - | `go.gov.sg/cxenquiry`; FAQ `go.gov.sg/corenetx-faq` | [2] |
| Assisted onboarding registration | - | `go.gov.sg/cx-onboarding` | [2][8] |

Regarding the COP edition conflict: the 23 July 2026 circular says the "latest" is 3.1 and the next edition would come before October 2026; the COP page now lists 4.0 (Sep 2026) [2][6]. Always check which edition applies to a given submission date: ongoing submissions can finish on the old edition, new gateway submissions and amendments from 1 Jan 2027 need COP 4.0 [6].

---

## 5. Tools, templates and software

### 5.1 Official authoring-tool guides [24]

| Tool | Guide page | Notes |
|---|---|---|
| Autodesk Revit | `info.corenet.gov.sg/ifc-sg-2/modelling---authoring/bim-authoring-tools/revit` | Setup packages by version: Revit 2024-2026, 2023, 2022 and below; JSON IFC Exporter files for 2020-2023. Requires latest IFC Exporter and **Revit Interoperability Tools**. Files: IFC+SG Shared Parameters, Property Set Files, IFC+SG Subtype Files. Standard "IFC-SG Regulatory Requirements View Setup" is locked; duplicate it to change the Property Sets file [19] |
| Graphisoft Archicad | `.../archicad` | Steps: Classification, Property Mapping, IFC Export, CORENET X review. Configuration files for "COP Fourth Edition (September 2026)"; older ones under "Previous COP Configuration & Resources". Graphisoft maintains content [26] |
| Tekla Structures | `.../tekla` and `support.tekla.com/corenet-x-ifc-sg` | Maintained by Trimble; plugins, Tekla Structural Designer Data Extractor, Trimble Connect plugins [27] |
| Bentley OpenBuildings Designer | `info.corenet.gov.sg/ifc-sg/modelling---authoring/bim-authoring-tools/openbuildings` | listed [24] |
| BricsCAD BIM | `.../bricscad-bim` | "Pilot testers welcome" [24] |
| SketchUp, Rhino | `.../sketchup`, `.../rhinoceros-3d` | IFC+SG via GingerBIM (Beta), paid; project teams should verify exported IFC themselves [24] |

Revit known issues from the official guide: Property Sets file not selectable (locked view setup); not coordinated/georeference problems; "micro model" (model very small or far away); missing IfcSlab, IfcOpeningElement, IfcCovering in Revit 2025/2026 linked files, where the first value of IfcShapeRepresentation ('Body' or 'FootPrint') is `$` - the guide recommends an "IFC Repair Tool" [19].

### 5.2 Plug-ins and third-party tools listed on the official site [28]

BIMvision (viewer, pre-checks); BIMcollab Zoom (federated viewing); BIMcollab BCF Manager (BCF in Revit/Navisworks/Archicad/Tekla); 1IFC (merges IFC files, does not validate); DiRootsOne (Revit data to Excel); **Bimeco Validator** (browser IFC+SG validation incl. federated); **BuiltSearch IV** (IFC+SG Validator, IFC Writer, IFC GUID Checker, BCF Report, Custom IFC Mapping that converts the Excel mapping to a TXT for Revit IFC export, Revit Shared Parameters, Companion App); Revizto (review IFC+SG parameters, BCF); Dynamo script for IFC parameter export/import; **GingerBIM** (SketchUp/Rhino, beta); Revit Interoperability Tools (validate IFC+SG values within Revit). The official site lists these but does not endorse any; commercial tools. Enthusiast/open-source projects specific to Singapore: none found in the sources read (unverified; see Gaps).

### 5.3 Training and funding [29]

Providers named on the official page: ACEPLP, BCA Academy, BIMAGE Consulting, The Architects Academy, SP PACE, Bluskai, Innocom, Graphisoft (Archicad IFC+SG, 4 hours online). Revit courses: "Creating an IFC+SG Model from Revit for CORENET-X Submission" (ACEPLP, 1 day), "Advanced" (2 days), "CORENET X Essential for MEP Services" (SP PACE, 21 hours). No Tekla courses are listed. Funding: BCA **Productivity Solutions Grant (PSG) for the Built Environment**, up to 50% of qualifying costs for SMEs buying pre-approved BIM software; the circular says it also supports IFC+SG courses [2][29].

---

## 6. Organisations and ecosystem

- Government: BCA, URA, MND, GovTech (facilitated the 2018 visioning workshop) [3].
- Industry bodies in the CORENET X context: REDAS (developers), SIA (architects), ACES (engineering consultants) adjusted payment schedules in Oct 2025 [11]; the CORENET X Industry **Community of Practice (CoPr)** shares technical knowledge via FormSG registration (37 firms at the time of the overview page) [3][30].
- buildingSMART Singapore chapter: a chapter existing under buildingSMART International is likely, but its name, website and activities could not be verified (page fetches blocked) (unverified).
- BIM associations and enthusiasts: not verified (see Gaps).

## 7. Terminology table

| Native term | Transliteration | English |
|---|---|---|
| CORENET X (English) | - | Construction and Real Estate NETwork X, the new regulatory submission system |
| RABW | - | Regulatory Approval for Building Works |
| QP | - | Qualified Person (architect or professional engineer submitting plans) |
| SVY21 / EPSG:3414 | - | Singapore national projected coordinate system |
| SHD | - | Singapore Height Datum |
| Corppass / Singpass | - | Corporate / national digital identity logins |
| TOP / CSC | - | Temporary Occupation Permit / Certificate of Statutory Completion |
| PP / WP / BP | - | Provisional Permission / Written Permission / Building Plan |
| DSP | - | Direct Submission Process |
| SGPset | - | Singapore property set in IFC |
| Written Direction | - | Agency comment requiring response |
| 建筑信息模型 | jiànzhù xìnxī móxíng | BIM (Mandarin, official language of Singapore) (unverified) |
| Pemodelan Maklumat Bangunan | - | BIM in Malay (unverified) |

Singapore documents are in English; the Chinese/Malay/Tamil terms are not used in regulation (unverified).

---

## Typical questions people ask about this

None of the below were found as linked community threads in this session (the official FAQ at `support.corenet.gov.sg/hc/en-us` returned HTTP 403 to my fetch tool). All are marked illustrative, but they follow the topics of the official guides.

1. Is CORENET X mandatory for my project? (illustrative; answer from section 1.4: new projects with GFA >= 5,000 m2 from 1 Oct 2026)
2. Is it IFC+SG or IFC-SG, and is it different from IFC4? (illustrative)
3. Which IFC version and MVD must I export? (IFC4 Reference View per Model Checker [18]) (illustrative)
4. Where do I download the IFC+SG Excel mapping file and which tab do I start with? ("CX Pilot Mapping" [22]) (illustrative)
5. How do I set up SVY21 / EPSG:3414 and Singapore Height Datum in my model? (illustrative)
6. Revit: which setup package for my Revit version, and why can't I choose the Property Sets file? (locked default setup [19]) (illustrative)
7. Why does my model appear tiny or far away in the viewer ("micro model")? (illustrative [19])
8. Revit 2025/2026 export drops IfcSlab / IfcOpeningElement / IfcCovering - what to do? (illustrative [19])
9. What do Model Checker codes IFC0000102 and IFC0000106 mean? (illustrative [18])
10. What is the difference between a QC "Fail" and an "Alert"? (illustrative [18])
11. QC05 coordinate alignment fails between ARC and MEP models - how to fix? (illustrative)
12. How do I keep IFC GUIDs unique when copying blocks? (illustrative [21])
13. Can Archicad, Tekla, OpenBuildings, BricsCAD, SketchUp or Rhino be used? (yes, see 5.1) (illustrative)
14. Can I try the portal before a real project? (training.corenet.gov.sg [14]) (illustrative)
15. Do I need a Corppass account and who authorises it? (illustrative [14])
16. Which COP edition applies to my resubmission after a Written Direction? (illustrative [6])
17. Do I submit 2D drawings as well as 3D models? (illustrative [13])
18. What is the Piling Gateway and when is it worth using? (illustrative [4])
19. Is there funding for BIM software or IFC+SG courses? (PSG, illustrative [29])
20. Which third-party validator should I use before upload? (illustrative [28])

## Common pitfalls and misconceptions

- Assuming a plain IFC4 export is enough. IFC+SG needs SGPsets, subtype values and controlled values from the mapping file; the Model Checker rejects other IFC versions/MVDs [18][22].
- Using outdated numbers. Many web articles say "mandatory from 1 Oct 2025 for 30,000 m2". The 23 July 2026 circular lowers this to 5,000 m2 from 1 Oct 2026 and makes smaller projects voluntary [2].
- Confusing site footers with versions. info.corenet.gov.sg pages show "Last Updated 16 May 2024" even where they describe 2026 content; use the file versions (mapping file 22 Sep 2026, COP 4.0 Sep 2026) [5][6][22].
- Treating the 3-gateway process as a single approval; DG, PG (optional), CG and TOP are separate submissions with separate processing times [4].
- Forgetting that 3D models take precedence over 2D plans unless the cover letter says otherwise [13].
- Merging IFC files with 1IFC and believing it validates them; it does not [28].
- Expecting RC (Regulatory Compliance Check) to exist; only schema and quality checks are live [18].
- Georeferencing in local/shared coordinates instead of SVY21 and SHD [6].
- Assuming editing the locked Revit standard setup; duplicate it first [19].
- Assuming the Training Environment contains the BIM viewer; it does not [14].

## Gaps

- Web search was disabled after quota exhaustion, so no community Q&A threads (forums, LinkedIn, Reddit, Autodesk/Graphisoft forums) were found; all questions above are illustrative.
- The implementation-timeline graphic could not be read; the circular text was used instead. The 23 Jan 2025 and 26 Sep 2023 circulars were not read.
- Exact SGPset names and parameters, the Glossary content, Archicad and Tekla export settings were not retrievable from page text.
- buildingSMART Singapore chapter, BIM associations (e.g. professional institutes, BIM user groups), Singapore-specific open-source projects, and the pre-2023 BIM e-submission history are unverified.
- Blocked/failed fetches (HTTP 403/404): support.corenet.gov.sg FAQ, buildingsmart.org chapter pages, standards.buildingsmart.org, technical.buildingsmart.org, www1.bca.gov.sg BIM pages, Wikipedia CORENET page. No suspicious or pirated sites were encountered.

## Sources

[1] https://info.corenet.gov.sg/ (home page and navigation)
[2] https://info.corenet.gov.sg/docs/default-source/bca-circulars/circular-for-updates-to-corenet-x-implementation-plan.pdf?sfvrsn=d8a19259_1 (Circular 23 Jul 2026, read in full)
[3] https://info.corenet.gov.sg/overview/about-corenet-x/overview-of-corenet-x
[4] https://info.corenet.gov.sg/regulatory-process/about-the-new-submission-process/3-gateway-process
[5] https://info.corenet.gov.sg/overview/about-corenet-x/implementation-timeline (circular list; includes go.gov.sg/cxbill2023, go.gov.sg/bca-circular-corenetx-implementation-plan, go.gov.sg/bca-circular-corenet-x, MND speech link https://www.mnd.gov.sg/newsroom/speeches/view/opening-address-by-minister-desmond-lee-at-the-opening-ceremony-of-the-international-built-environment-week-2021)
[6] https://info.corenet.gov.sg/regulatory-process/corenet-x-code-of-practice
[7] https://go.gov.sg/bca-circular-annex-c-payment-schedule-corenet-x
[8] https://info.corenet.gov.sg/overview/about-corenet-x/getting-ready-for-corenet-x
[9] https://en.wikipedia.org/wiki/Building_and_Construction_Authority (community-edited; BIM 80% by 2015 target)
[10] https://info.corenet.gov.sg/submission-portal-resource/more/corenet-x-and-corenet-2.0--key-differences
[11] https://info.corenet.gov.sg/regulatory-process/about-the-new-submission-process/refinements-to-the-new-process
[12] https://info.corenet.gov.sg/regulatory-process/about-the-new-submission-process/direct-submission-process-(dsp)
[13] https://info.corenet.gov.sg/regulatory-process/about-the-new-submission-process/typical-submission-package
[14] https://info.corenet.gov.sg/submission-portal-resource/corenet-x-submission-portal
[15] https://portal.corenet.gov.sg/ and https://training.corenet.gov.sg/ (linked, not opened)
[16] https://info.corenet.gov.sg/submission-portal-resource/release-notes
[17] https://info.corenet.gov.sg/ifc-sg/start-here/WhatIsIFCSG
[18] https://info.corenet.gov.sg/submission-portal-resource/more/model-checker
[19] https://info.corenet.gov.sg/ifc-sg-2/modelling---authoring/bim-authoring-tools/revit
[20] https://info.corenet.gov.sg/ifc-sg/requirements---submission/ifcsg-data-structure
[21] https://info.corenet.gov.sg/ifc-sg/modelling---authoring/GeneralModellingPractices
[22] https://info.corenet.gov.sg/ifc-sg/requirements---submission/ifc-sg-excel-mapping-file
[23] https://info.corenet.gov.sg/ifc-sg/glossary-of-identified-components
[24] https://info.corenet.gov.sg/ifc-sg/modelling---authoring/bim-authoring-tools
[25] https://info.corenet.gov.sg/ifc-sg/modelling---authoring/relevant-documents
[26] https://info.corenet.gov.sg/ifc-sg-2/modelling---authoring/bim-authoring-tools/archicad
[27] https://info.corenet.gov.sg/ifc-sg/modelling---authoring/bim-authoring-tools/tekla ; https://support.tekla.com/corenet-x-ifc-sg
[28] https://info.corenet.gov.sg/ifc-sg/modelling---authoring/3rdpartytools
[29] https://info.corenet.gov.sg/resources/corenet-x-training---funding
[30] https://info.corenet.gov.sg/ifc-sg/register-for-technical-updates---copr
Also: https://info.corenet.gov.sg/ifc-sg/start-here/ifcsg-onboarding-checklist (onboarding steps), https://info.corenet.gov.sg/resources/codes-and-regulations (agency code pages)
