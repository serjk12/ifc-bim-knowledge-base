# How IFC requirements are written in EIR/BEP/BIM manuals (real examples)

## In plain words

A client (owner) who wants an IFC model does not just say "send us IFC". They write the rules into contract documents: the **EIR** (Exchange Information Requirements, the client's list of what information must be delivered, when, and in what format) and the supplier's answer, the **BEP / BIM Execution Plan** (how the team will meet it). National or owner BIM manuals (Statsbygg SIMBA, Dutch BIM basis ILS, Singapore CORENET X IFC-SG, Chilean Planbim, German AIA/BAP, UK DfE EIR) are reusable bundles of such rules. Typical clauses fix the IFC schema version, the Model View Definition (MVD, the subset of IFC to export), exchange rhythm, file naming, coordinates, mandatory properties and classification, how the model will be checked, the level of information need (LOIN), and increasingly a machine-readable IDS file and BCF for issues. For a QA tester of IFC/Revit MCP servers this document shows what "a correct IFC delivery" means in practice, which checks real BIM managers run, and which requests users really make.

Last researched: 2026-11-06

---

## 1. Vocabulary in one table

| Term | Meaning | Where it lives |
|---|---|---|
| EIR (Exchange Information Requirements) | Client's requirements for information deliverables; term from ISO 19650-2 (the DfE EIR cites clause 5.2.1 of ISO 19650-2) [1] | Tender/contract |
| BEP / BAP / PEB | Response of the supplier: BIM Execution Plan (English), BIM-Abwicklungsplan (German, BAP), Plan de Ejecución BIM (Spanish, PEB) [1][6][9] | Pre-appointment and post-appointment versions |
| AIA | German: Auftraggeber-Informationsanforderungen = client information requirements = the EIR equivalent [6] | Contract annex |
| MVD (Model View Definition) | Named subset of the IFC schema for a purpose, e.g. IFC2x3 Coordination View 2.0, IFC4 Reference View [10][11] | Export setting |
| LOIN (Level of Information Need) | ISO 7817-1 concept replacing LOD: which geometry, alphanumeric data and documents are needed per object, phase and use [6][12] | Table/annex in EIR |
| IDS (Information Delivery Specification) | buildingSMART XML (`.ids`) that states machine-checkable requirements for IFC [13][14] | Attachment to EIR |
| BCF (BIM Collaboration Format) | Open format for issues/comments tied to model viewpoints [6][7] | Coordination workflow |
| CDE | Common data environment, where deliveries are stored with status/revision codes [1] | Platform |

---

## 2. Typical clauses (what a real IFC requirement section contains)

### 2.1 IFC schema version

- UK Department for Education (DfE) EIR, January 2026: IFC-SPF files "shall be provided in accordance with either" IFC2x3 TC1 (PAS/ISO 16739:2005) or IFC4 ADD2 TC1 (ISO 16739-1:2018); geometric requirements are listed against IFC2x3 TC1 entities [1].
- Statsbygg (Norway): SIMBA 1.3 for IFC2x3, SIMBA 2.0 for IFC4, SIMBA X for existing buildings; requirement sets "written only for intended use against IFC4 models" for 2.0 [2]. A secondary (social media thread, unverified) report says SIMBA 2.1 requires IFC4 ADD2 TC1 with IFC2x3 as a fallback during the project [3].
- Chile, MINVU DS49 information request: use a neutral standard such as IFC; "IFC 4 is recommended, minimum IFC 2x3 as stated in the PEB" [9].
- Singapore CORENET X: IFC4 Reference View with the local IFC-SG extension [4].
- Moscow ЦИМ АГР (commercial summaries, not primary): IFC4 Reference View, IFC 4.0.2.1 schema per ГОСТ Р 10.0.02-2019 [15] (see section 3.6 for caveats).
- Germany (Bund Muster-AIA): the template asks the client to state "data formats with associated version number" and, if appropriate, to prescribe a standard MVD [6]. It also notes IFC4.3 brings IfcBridge, IfcRoad, IfcRailway [6].
- IFC 4.3 is ISO 16739-1:2024 (published April 2024 per a US pooled-fund study page) [16].

Practical wording that avoids ambiguity: name the schema identifier (`IFC2X3`, `IFC4` = IFC4 ADD2 TC1 = "IFC 4.0.2.1", `IFC4X3_ADD2`), the MVD, and the export tool version.

### 2.2 MVD (Model View Definition)

| MVD | Schema | Status/comment |
|---|---|---|
| Coordination View 2.0 (CV2) | IFC2x3 | Legacy, still the Revit default in older help pages [10][17] |
| Reference View (RV 1.2) | IFC4 ADD2 TC1 | Final; read-only coordination; "CV2.0 with slightly reduced and more focused range" per bSI MVD policy summary [10][11] |
| Design Transfer View (DTV) | IFC4 | bSI database lists it as Draft; a forum thread says it never became an official MVD (per search summary; verify) [10]. Practitioners still use "DTV" when editable data is wanted [18] |
| Alignment-based / other 4.3 views | IFC4.3 | Infrastructure; use only when needed [10] |

Dutch NLRS guide v3.0 says Revit users should treat an MVD "like a View Template" and names CV2, RV and DTV as the most used [8]. Chile asks for "the MVD corresponding to the delivery stage" plus the native file [9].

### 2.3 Exchange frequency and deliverables

- Germany Muster-AIA: a deliverables table per project phase/milestone with columns Liefergegenstand (deliverable), Beschreibung, AwF-Nr. (use case number), Lieferzeitpunkt (delivery time), Dateiformat (IFC, native). Digital deliverables go in neutral formats ("IFC für Modelle, DWG für Zeichnungen, PDF"); the client may additionally ask for native files; for every model delivery a concrete LOIN must be given via the LOIN annex; bidders may propose dates or exchange frequency [6].
- Germany quality checks: table "Qualitätsprüfung der Fachmodelle" with timing "at every coordination date and in depth at the end of a service phase (Leistungsphase)" [6].
- UK DfE: information management reports at completion of RIBA Stages 3, 4, 5, 6; COBie provided at specified RIBA stages; no file size limit prescribed but a federation strategy in the BEP must consider splitting (e.g. electrical, mechanical, public health as separate IFC files) [1].
- Chile: PEB must state deliverable formats; EAIM (Estado de Avance de la Información de los Modelos = model information progress state) drives NDI (Nivel de Información) per entity [9].
- Typical real rhythm (illustrative, not from one source): weekly or bi-weekly coordination exports, formal "issue for stage gate" exports at each design phase end.

### 2.4 File naming and model splitting

- Dutch BIM basis ILS 3.1: "uniform and consistent naming of (aspect) models within the project", example `<Bouwwerk>_<Discipline>_<Onderdeel>` [5].
- NLRS: IfcProject name `<project number per project agreements>_<aspect model type>` and IfcSite Name = cadastral designation, e.g. "Delft AB 1234" [8].
- Moscow АГР: regulated underscore-separated file names, full set of discipline files up to 500 MB, larger models split in 2-3 volumes (commercial summary) [15].
- Singapore: IFC-SG "block" mechanism aligns architectural, structural and MEP models; GUIDs must stay unique across blocks and copied templates [4].
- UK DfE: file naming examples are part of the project information standard (section 5.1.10 per its change log) [1].

### 2.5 Coordinates, units, georeferencing

| Source | Clause |
|---|---|
| Dutch ILS 3.2 | Local position of the building is mutually coordinated and lies "close to the zero point"; tip: a physical 0-point object at 0.0.0, exported to IFC [5] |
| NLRS (Revit) | Three points: Project Base Point, Survey Point, Startup (internal origin); advised to place all on one another; export setting "Project Origin" must be agreed in project agreements [8] |
| German Muster-AIA 8.3, 8.4 | Client states geodetic reference systems, project coordinate system, reference points (project zero, north direction) in a table; every model must contain the zero point "in verifiable form" and the north direction; client can require a BIM reference IFC file from the BIM coordinator with the coordinate/height system applied; units are fixed in 8.4 [6] |
| UK DfE | Coordinates of the building(s) and building storey (floor) nomenclature with elevation and height are project-information-standard items (2.2.11, 5.2.4) [1] |
| Singapore | Per a BCA webinar deck summary: SVY21 (EPSG:3414) and Singapore Height Datum; total models in one submission not over 2 GB (secondary summary, verify in the Code of Practice) [4][19] |
| Moscow АГР | One system for all discipline files; base point tied to real X, Y, Z and the Baltic height system; rotation to true north; scale 1:1 (commercial summary) [15] |

### 2.6 Mandatory properties, entities and classification

- **Correct IFC class** (Dutch ILS 3.4): floor = IfcSlab, wall = IfcWall, beam = IfcBeam, column = IfcColumn, stair = IfcStair, door = IfcDoor [5]. Singapore: correct entity per element, predefined types where possible, USERDEFINED only when an IFC-SG subtype requires it [4]. Moscow (commercial): IfcBuildingElementProxy forbidden when a specific class exists [15].
- **Type/name** (Dutch ILS 3.5): ObjectType/IfcType filled for every element, Name where applicable [5].
- **Storeys** (Dutch ILS 3.3): only storeys named as IfcBuildingStorey.Name, all objects assigned to a storey, same numeric-sortable naming e.g. "00 begane grond", "01 eerste verdieping" [5].
- **Material** (3.7): objects get an IfcMaterial description e.g. "kalkzandsteen" (calcium-silicate brick) [5].
- **No duplicates or intersections** within an aspect model (3.8) [5]. UK DfE reports must cover "duplication, clash detection" [1].
- **Common properties** (Dutch ILS 4.1-4.4): `LoadBearing`, `IsExternal`, `FireRating` in the right Pset (example `Pset_BeamCommon`); FireRating in minutes (30, 60, 90); further properties project-specific [5].
- **Classification:** Dutch ILS 3.6 four-digit NL-SfB variant element code (example 22.11) [5]; UK DfE uses Uniclass (PM table level 3 for document category; asset classification updated to latest Uniclass) [1]; Chile uses COBie parameters and the MEI (Manual Básico de Entrega de Información) required fields, with classification of spaces via a standardized system [9]; Statsbygg uses TFM properties (per vendor blog) [18].
- **National custom property sets:** Singapore SGPsets / IFC-SG data structure with an Excel mapping file [4][20]; Moscow `RusSet_*` sets and `RUS_FNO` (commercial summary) [15].
- **Quantities:** Chile's minimum parameters include volume/perimeter taken from IfcQuantities or quantity take-off [9]. In Revit this is the "Export base quantities" option under Modify setup > Property sets [17].

### 2.7 Model checking criteria

- UK DfE: reporting on IFC-SPF model checking requirements in the detailed EIR, COBie quality-control report, duplication and clash detection, CDE metadata compliance [1].
- Germany: focus areas for discipline-model checks include "correct use of coding and filing structure of the CDE", "correct splitting into sub-models", "correct IFC export parameters per BAP", "naming conventions"; checker software "must support IFC and BCF" [6].
- Statsbygg: machine-checkable requirements should be checked automatically, leaving QA time for human judgement; delivered as mvdXML plus PDF, with IDS announced as the replacement for requirement statements [2][21].
- Singapore: use correct entities, unique GUIDs, check clashes before submission; a model checker is part of the IFC-SG site [4][20].
- Moscow (commercial): no intersections between discipline files; comments as BCF [15].

### 2.8 LOIN tables

German Muster-AIA chapter 8.2 "Informationsbedarfstiefe" (LOIN) with an annex per object group: geometry (appearance etc.), alphanumeric information and documents per phase; each model delivery references a concrete LOIN [6]. Chile has NDI per EAIM table (table 10 of the Estándar BIM, pages 64-65 as cited in DS49) [9]. UK DfE sets detailed requirements as entity tables and COBie sheet/field tables (YES / PL placeholder / R reference markers) [1]. ISO 7817-1 is the LOIN standard (publication details not verified in this research) [12].

### 2.9 IDS delivery

- IDS 1.0 became an official buildingSMART standard on 1 June 2024 (search summary; GitHub release tag v1.0.0 published 3 June) [13][14].
- An `.ids` file holds Specifications; each has Applicability (which elements) and Requirements (what they must have), built from facets: entity, attribute, property, classification, material, partOf [14][22].
- Requirements can be required/optional/prohibited (cardinality) - general knowledge, not confirmed on the fetched page.
- 200+ people from 34 countries took part; 20+ products implement it; talks on CEN/ISO publication are mentioned in release notes [14].
- Statsbygg's site says IDS will replace mvdXML for stating model requirements [21].

### 2.10 BCF use

- German Muster-AIA 9.1.2: checking software must support IFC and BCF; collisions are displayed, commented, edited "e.g. using a BCF format" [6].
- Chile DS49: deliverables may be supported with BCF and LandXML where necessary [9].
- Moscow АГР: annotations delivered as BCF or txt/trm container (commercial summary) [15].

---

## 3. Public examples country by country

### 3.1 United Kingdom (UK BIM Framework, DfE)
- DfE "Exchange Information Requirements - Employer's requirements" (January 2026, OGL v3.0) is built on ISO 19650-2 and comes with detailed EIR tables (geometry per IFC2x3 entity, COBie sheets/fields), role matrices and report templates [1].
- Allowed formats: IFC-SPF (IFC2x3 TC1 or IFC4 ADD2 TC1), JPG, MPEG, native, PDF (v7.0+, indexed above 50 pages), XLSX, XLSM [1].
- Native models are asked to export IFC compliantly so both can be rule-checked [1].
- Older template: Cambridge CDBB BIM Toolkit EIR template and guidance (dated 2016, before ISO 19650) [23]. CEN/TR 17654 is a European guideline for EIR/BEP based on ISO 19650-1/-2 [23].

### 3.2 Norway (Statsbygg SIMBA)
- SIMBA = Statsbygg's information standard; roles: Tilbyder (bidder), Oppdragsansvarlig (commissioning lead), BIM-koordinator, Fagmodellansvarlig (discipline model owner) [21].
- New site simba.statsbygg.no with the requirements effective 2024-10-04; the old Google Sites version went offline 2025-03-05 [21][24].
- Earlier manual SBM 1.2.1 (older IFC2x-era text; seen only through a search summary) [25].
- Licence of the buildingSMART UCM entry: CC BY-NC-SA 4.0 [2].

### 3.3 Netherlands (BIM basis ILS)
- "BIM basis informatieleveringsspecificatie" v1.0, a two-page checklist by BIM Loket and buildingSMART Benelux (PDF metadata: created 28 Nov 2018) [5]. Principle: "nothing new is developed, existing structures based on openBIM IFC are used" [5].
- Clauses 3.1-3.8 and 4.1-4.4 summarized in section 2 above. Quality criteria for names: meaningful, understandable, logical, insightful, consistent, recognizable [5].
- NLRS guide (Revit to IFC) v3.0 maps Revit categories to IFC classes (IfcExportAs, IfcExportType shared parameters; IFC Export Mapping Table), tested with a Revit 2019-era exporter and cautions that results differ per Revit/exporter version [8].
- Project ILS built on top, e.g. ILS 28 steel structures (grid as IfcGrid and 1x1x1 m origin object, per search summary) [26].

### 3.4 Singapore (CORENET X, IFC-SG)
- IFC4 Reference View + IFC-SG; configuration covers BCA, LTA, NEA, NParks, PUB, SCDF, URA [4]; IFC+SG resources: Excel mapping file, data structure (SGPsets), authoring-tool guidance, model checker [20].
- Authoring tools: Revit (Autodesk interoperability tools with shared-parameter configuration XML, checkset) and Archicad (config files) [27].
- Mandatory scope: IFC-SG submission for new erections and major A&A with new GFA (BCA circular summary); a 5,000 m2 threshold from 1 Oct 2026 appears in one news article only (unverified) [4][19].
- Simplified objects accepted if the required IFC-SG data is embedded [4].

### 3.5 Chile (Planbim, MINVU)
- Estándar BIM para Proyectos Públicos: first edition June 2019, v1.1 June 2021; PEB templates in annexes IV (offer) and V (definitive) [9][28].
- MINVU DS49 SDI BIM: formats per 6.1 (minimum IFC 2x3, MVD for the stage, plus native file; BCF and LandXML as support); PEB must define nomenclature, classification, units, coordinates, level structure [9].
- Planbim IFC entity guides (architecture v2.2, volumetric v2.0, MEP, bridges) are tied to ISO 16739-1:2018 / IFC 4.0.2.1 [28].

### 3.6 Russia (ЦИМ - цифровая информационная модель, digital information model)
- ГОСТ Р 10.0.02-2019 is the Russian adoption of IFC data schema (analog of ISO 16739-1:2018), in force since 2019-09-01 [29].
- Moscow АГР (архитектурно-градостроительное решение, architectural-urban-planning solution): commercial sources say a mandatory IFC model is added to FBX models (НПМ - low-poly, ВПМ - high-poly) from spring 2026; they disagree on the start date (2 April 2026 vs 19 January 2026) and cite an order of the Moscow Committee for Architecture (ДГП) and IT Department of 16.01.2026 No. ДГП-Р-1/26/64-16-6/26 (unverified, not seen in primary text) [15][30][31].
- Reported content: IFC4 Reference View, IFC4.0.2.1; IfcSite with `RUS_LandID`, `RUS_AreaSquare`; IfcSpace per area methodology; custom sets `RusSet_ACR/Project/Common/Quantities/Location`; `RUS_FNO`; standard Pset_/Qto_ reportedly not counted; total up to 500 MB; Baltic height system; XML statements for ТЭП (технико-экономические показатели, technical-economic indicators); BCF annotations (all unverified) [15][30].
- Related: St Petersburg expert review (ГАУ «ЦГЭ») has IFC-class requirements for engineering systems models; the primary PDF could not be opened [32].
- Treat all of the above as "to verify against the official order", as aggregator sites disagree.

### 3.7 Germany (AIA/BAP)
- "BIM für Bundesbauten" Arbeitshilfe Muster-AIA (BIM-Handbuch): chapters include BIM goals and use cases (2), deliverables and dates, model structure and content (8: modelling rules, LOIN 8.2, coordinate systems 8.3, units 8.4, tolerances 8.5), technologies (9), standards (10) [6]. Matching Muster-BAP exists [33].
- Saxony SIB offers AIA, IDM, model guideline and Muster-BAP with annexes; Baden-Wuerttemberg publishes a Muster-AIA [33][34].
- Project spatial structure: IfcProject, IfcSite, IfcBuilding, optional IfcBuildingStorey [6].

### 3.8 United States (GSA, DOT)
- FHWA material states BIM data requirements and modelling standards are voluntary, not enforceable under federal statute or FHWA regulations [35].
- Pooled-fund study TPF-5(565), lead Iowa DOT, 2026-2028: IFC Validation Service and certification so DOTs can specify certified software and validate consultant deliverables; mentions AASHTO resolution to adopt IFC for BIM-based delivery of State DOT projects [16].
- GSA: the BIM Guide Series (e.g. 02 spatial program validation, 08 facility management) are older (2006-2012) documents; I could not confirm current GSA IFC requirements (gsa.gov page returned 404) [36].
- No state DOT contract language on IFC 4.3 found in this pass (unverified).

---

## 4. How the requirements are written in practice: sample wording (paraphrased)

1. "Models shall be delivered as IFC4 ADD2 TC1 using the Reference View, exported with the agreed exporter version, plus the native file."
2. "Each model contains one IfcProject, one IfcSite, one IfcBuilding and IfcBuildingStorey elements named `NN description`; all elements are contained in a storey." (cf. Dutch ILS 3.3 [5])
3. "Project base point and survey point are placed per Table X (EPSG code, vertical datum); true north angle is exported."
4. "Every IfcWall/IfcSlab/IfcDoor carries `Pset_*Common.IsExternal`, `LoadBearing`, `FireRating` where applicable; classification via IfcClassificationReference (Uniclass/NL-SfB/other) per IDS file `X.ids`."
5. "No IfcBuildingElementProxy except where agreed; no duplicate or overlapping elements within one discipline model."
6. "Issues are exchanged in BCF 2.1/3.0 (or BCF API) via the CDE; each issue references GUIDs."
7. "IFC validated by an IFC validator and by IDS check; reports delivered with each stage gate."

---

## 5. Checklist BIM managers use to review an IFC delivery

Derived from the sources above and common practice (checklist structure is the author's synthesis).

**A. File and metadata**
1. Opens without errors; correct schema in the header (`FILE_SCHEMA`: `IFC2X3`, `IFC4`, `IFC4X3_ADD2`) and the MVD named in the contract.
2. File name follows the convention; status/revision per CDE; file size within limits (e.g. 500 MB Moscow, 2 GB Singapore) [4][15].
3. Exporter name/version recorded (Revit version, open-source exporter); native file delivered when required [9].

**B. Spatial structure and coordinates**
4. One IfcProject, IfcSite, IfcBuilding; storeys named per convention; every element assigned to a storey [5].
5. Project zero and north match the agreed reference file; elements near origin, no huge offsets; units correct (mm/m) [5][6].
6. Georeference (IfcMapConversion / IfcProjectedCRS in IFC4) matches the required CRS (e.g. Singapore SVY21 per BCA slides, unverified) [19].

**C. Entities and types**
7. Correct IFC classes, few or no IfcBuildingElementProxy; predefined types sensible [4][5][15].
8. ObjectType/type filled; names meaningful [5].
9. Materials assigned [5].

**D. Properties, quantities, classification**
10. Mandatory Psets/properties present and non-empty (LoadBearing, IsExternal, FireRating etc.) [5].
11. Classification references present with the right system and code format (NL-SfB 4-digit, Uniclass) [1][5].
12. Base quantities (Qto_*) present when required [9][17].
13. COBie fields and QC report if COBie is required [1].

**E. Geometry and coordination**
14. No duplicates/overlaps in one discipline model; clash report agreed tolerances [1][5].
15. Unique GlobalIds across blocks and versions [4].
16. Federated model aligns (visual overlay of disciplines).

**F. Automated checks and reporting**
17. IDS / mvdXML / ruleset run, report attached [2][14].
18. IFC validator run for syntax/schema issues.
19. Issues logged in BCF and tracked to closure [6].
20. Information management report for the stage (UK: RIBA 3-6) [1].

---

## 6. Typical questions people ask about this

I could not retrieve live forum threads in this research pass (search budget ended), so all items below are marked (illustrative); they follow patterns seen in the source documents.

1. Which IFC version should I put in an EIR - IFC2x3, IFC4 or IFC4.3? (illustrative)
2. What is the difference between Reference View and Design Transfer View, and which one do I require? (illustrative)
3. Does Revit export IFC4 Reference View with base quantities? Why are Qto_ quantities missing? (illustrative; see [17])
4. How do I set Project Base Point vs Survey Point for IFC export and shared coordinates? (illustrative; see [8])
5. What coordinate reference system do I write into the EIR (EPSG code, vertical datum)? (illustrative)
6. How often should models be exchanged - weekly, bi-weekly, per milestone? (illustrative)
7. Which properties should be mandatory for walls, slabs and doors? (illustrative; compare [5])
8. How do I require a classification (Uniclass, NL-SfB, OmniClass) inside IFC? (illustrative)
9. Can I replace the LOD table with LOIN? How do I write a LOIN table? (illustrative)
10. What is IDS and can it replace the mvdXML/Excel property list in the EIR? (illustrative; [14][21])
11. How do I check an IFC against an IDS file, and what does the report look like? (illustrative)
12. Why was my IFC rejected: IfcBuildingElementProxy, empty properties, offset coordinates? (illustrative; [15])
13. How do I split a big building model into several IFC files and keep the same origin? (illustrative; [1][15])
14. Should we deliver native files together with IFC? (illustrative; [6][9])
15. How do I use BCF with a Revit-based team (BCF 2.1 vs 3.0, BCF API)? (illustrative)
16. What does the BEP need to prove if the EIR says "IFC4 certified export"? (illustrative)
17. How do I map Revit categories to IfcExportAs / predefined types? (illustrative; [8][17])
18. What are the IFC requirements for COBie handover? (illustrative; [1])
19. How should storeys be named so that IFC checks pass? (illustrative; [5])
20. What changes for infrastructure with IFC4.3 (IfcRoad, IfcBridge, IfcRailway)? (illustrative; [6][16])

### Test-request ideas for an IFC/Revit MCP server (illustrative)
- "Check that all walls in this IFC have `IsExternal` and `FireRating` and list those missing."
- "Report which elements are IfcBuildingElementProxy and suggest classes."
- "Which IFC schema and exporter does this file use? Is a georeference present?"
- "List storeys and elements not assigned to a storey."
- "Export from the open Revit model as IFC4 Reference View with base quantities" (verify the export settings used).
- "Run this IDS against the model and summarize failures by specification."

---

## 7. Common pitfalls and misconceptions

- **"IFC is IFC."** The schema version and the MVD change what is exported; CV2 and RV are not interchangeable, and a Reference View importer cannot import Design Transfer View data (per bSI MVD policy summary) [10].
- **Mixing "IFC4" labels.** IFC4 in contracts normally means IFC4 ADD2 TC1 (ISO 16739-1:2018, IFC 4.0.2.1); IFC4.3 is ISO 16739-1:2024 [1][16].
- **Quantities not exported.** Revit needs "Export base quantities"; some versions had issues with IFC4 Qto exports [17].
- **Origin confusion.** Revit has three points (Base Point, Survey Point, internal origin) and the IFC "Project Origin"/coordinate base setting must be fixed in agreements; wrong choice causes offsets between disciplines [8].
- **Aggregator sites as law.** Moscow АГР IFC rules appear on commercial sites with conflicting dates and prefixes; use the official order [15][30].
- **IFC with empty data.** A clean geometry with empty Psets still fails IDS/ILS checks; checking should cover data, not only 3D [5][14].
- **LOD vs LOIN.** LOIN is per object and purpose, includes alphanumeric and documents, not only geometry [6][12].
- **mvdXML vs IDS.** Statsbygg publishes mvdXML but states IDS will replace it for requirements; IDS is not a view definition and does not select the export subset [14][21].
- **Vendor behaviour differs.** NLRS warns that results differ across Revit versions and exporter versions; always re-check in several viewers [8].
- **File size.** Limits exist (500 MB, 2 GB) and some third-party exporters are limited in size (about 1.5 GB per a search snippet) [4][15][17].
- **FHWA voluntary.** US federal BIM data requirements are voluntary; owner-specific contract clauses drive IFC use [35].

---

## 8. Gaps and unverified items

- Full Statsbygg SIMBA text (current IFC version, georeference values) not retrieved: simba.statsbygg.no overview only; the search tool budget was exhausted before follow-up searches. Scribd copies of the old SBM manual were skipped as unofficial copies.
- Moscow АГР order text and the St Petersburg ЦГЭ PDF were not accessible (connection errors/401); Russian details come from commercial/consultancy pages [15][30].
- Planbim main Estándar BIM PDF was too large to fetch; Chile content is from MINVU DS49 and search summaries [9][28].
- buildingsmart.org, iso.org, standards.buildingsmart.org pages returned 403 to the fetch tool; IDS/MVD/IFC4.3 facts rely on GitHub release notes, search summaries, and the US pooled-fund page. ISO 7817-1 publication details not verified.
- Current GSA IFC requirements and state DOT clauses not found.
- Revit IFC export option names (Project Origin choices) beyond what the NLRS guide and Autodesk help snippets say were not verified.
- No suspicious/pirated sites were encountered.

---

## Sources

[1] UK DfE, Exchange Information Requirements (Jan 2026): https://assets.publishing.service.gov.uk/media/697206e4a1311bdcfa0ed8a5/ER-DFE-XX-XX-T-X-0001-Exchange_Information_Requirements-A-C01.pdf
[2] buildingSMART UCM, SIMBA - Statsbygg's BIM requirements: https://ucm.buildingsmart.org/use-case-details/2553/en
[3] Thread summarizing Statsbygg SIMBA 2.1 (secondary, social media): https://threadreaderapp.com/thread/1596398683565735942
[4] BCA CORENET X FAQ, new data requirements and technology (via search summary; direct fetch of the FAQ URL returned 404): https://www1.bca.gov.sg/regulatory-info/building-control/corenet-x/corenet-x-faq/new-data-requirements-and-technology ; CORENET X model setup page: https://info.corenet.gov.sg/ifc-sg/model-setup-and-coordination
[5] BIM basis informatieleveringsspecificatie v1.0 (BIM Loket / buildingSMART Benelux): https://digigo.nu/wp-content/uploads/2023/11/BIM_basis_ILS_v1_0_NL.pdf
[6] BIM für Bundesbauten, Arbeitshilfe Muster-AIA: https://fib-bund.de/Inhalt/Themen/BIM_fuer_Bundesbauten/BIM_AH_Muster-AIA.pdf
[7] buildingSMART BCF (page not retrievable; BCF facts from [6][9][15]): https://technical.buildingsmart.org/standards/bcf/
[8] Handleiding NLRS export IFC v3.0: https://www.cadix.nl/media/widhx21u/handleiding-nlrs-export-ifc.pdf
[9] MINVU, Solicitud de Información BIM DS49: https://www.minvu.gob.cl/wp-content/uploads/2023/10/minvu-bim-pro-ds49-sdi.pdf
[10] bSI MVD policy for IFC 4.x (via search summary): https://www.buildingsmart.org/wp-content/uploads/2021/05/20210425_MVD-policy_IFC4.x.pdf ; MVD database: https://technical.buildingsmart.org/standards/ifc/mvd/mvd-database/
[11] IFC4 Reference View 1.2: https://standards.buildingsmart.org/MVD/RELEASE/IFC4/ADD2_TC1/RV1_2/HTML/schema/views/reference-view/index.htm
[12] bSI Guidance for Regulators (lists LOIN, ISO 23386/23387, IDS; via search summary): https://www.buildingsmart.org/wp-content/uploads/2024/11/Guidance-for-Regulators_Industry_Insight_bSI_v3c1.pdf
[13] buildingSMART IDS page: https://www.buildingsmart.org/standards/bsi-standards/information-delivery-specification-ids/ ; IDS 1.0 approval news: https://www.buildingsmart.org/information-delivery-specification-ids-v1-0-is-approved-as-a-final-standard/
[14] GitHub buildingSMART/IDS release v1.0.0: https://github.com/buildingSMART/IDS/releases/tag/v1.0.0
[15] Moscow ЦИМ АГР requirements (commercial consultancy summary): https://www.nep.expert/info/ifc-dlya-agr-trebovaniya/
[16] Pooled fund TPF-5(565) IFC adoption: https://pooledfund.org/Details/Study/1798
[17] Autodesk support on Revit IFC base quantities: https://www.autodesk.com/support/technical/article/caas/sfdcarticles/sfdcarticles/How-to-export-model-from-Revit-to-IFC-export-with-quantities.html ; Revit 2026 help, Exporting to IFC: https://help.autodesk.com/cloudhelp/2026/ENU/Revit-DocumentPresent/files/GUID-6EB68CEC-6C17-4B16-A509-30537F666C1F.htm ; Revit IFC help: https://up.autodesk.com/2023/RVT/ADSKIFCExporterHelp.htm
[18] Construsoft Nordics blog (vendor), delivering Tekla IFC to standards: https://nordics.construsoft.com/blog/delivering-ifc-models-to-meet-bim-standards
[19] BCA CORENET X draft Code of Practice webinar (June 2023, via search summary): https://www1.bca.gov.sg/docs/default-source/docs-corp-regulatory/building-control/corenet-x/cx-draft-cop-webinar-15-june-2023.pdf ; URA circular: https://www.ura.gov.sg/guidelines/circulars/dc23-07/
[20] IFC+SG resource toolkit: https://info.corenet.gov.sg/ifc-sg/bim-data-(ifc-sg)/ifc-sg-resource-toolkit
[21] Statsbygg SIMBA site: https://simba.statsbygg.no
[22] IDS user manual: https://github.com/buildingSMART/IDS/blob/development/Documentation/UserManual/README.md
[23] Cambridge CDBB EIR guidance: https://www.cdbb.cam.ac.uk/files/eir_guidance.pdf ; CEN/TR 17654 listing: https://evs.ee/en/cen-tr-17654-2021
[24] Old SIMBA Google site notice: https://sites.google.com/view/simba-bim-krav
[25] SBM 1.2.1 (only via search summary; unofficial copy not linked)
[26] ILS 28 Staalconstructies: https://www.bouwenmetstaal.nl/uploads/themas/ILS_28_Staalconstructies_versie_1_0_ss.pdf
[27] Autodesk Singapore interoperability tools: https://interoperability.autodesk.com/singapore/ ; Graphisoft CORENET X: https://graphisoft.com/sg/solutions/corenet-x-and-ifc-sg
[28] Planbim / Construye2025: https://construye2025.cl/wp-content/uploads/2022/07/Estandar-BIM.pdf ; IFC guides: https://construye2025.cl/wp-content/uploads/2025/01/03_GUIA_DE_USUARIO_IFC_ARQ_V2.2.pdf
[29] ГОСТ Р 10.0.02-2019: https://cn.gostinfo.ru/catalog/Details/?id=6453898
[30] Moscow АГР, consultancy pages: https://agr-moscow.ru/trebovaniya-mka-k-agr ; https://rekro.ru/articles/trebovaniya-k-materialam-v-formate-ifc/ ; https://companies.rbc.ru/news/axjEyNHHOq/iz-za-chego-mogut-otkazat-v-soglasovanii-tsim-agr-v-formate-ifc/
[31] https://smway.ru/284-pp-trebovaniya-k-agr/
[32] St Petersburg ЦГЭ requirements: https://www.spbexp.ru/upload/iblock/ba2/trebovaniya_k_tsim_konstruktivnye_i_obemno_planirovochnye_resheniya.pdf
[33] SIB Sachsen BIM: https://sib.sachsen.de/bim-building-information-modeling-4089.html ; Muster-BAP: https://www.sib.sachsen.de/download/VVV/A03.07_Vertrag-Anlage_Muster_BAP_Vorlage.pdf
[34] BW Muster-AIA: https://vm.baden-wuerttemberg.de/fileadmin/redaktion/m-mvi/intern/Dateien/PDF/Rahmendokument_Projektvorbereitung_-_Muster-AIA_barrierefrei.pdf
[35] FHWA BIM administrative view: https://www.fhwa.dot.gov/construction/bim/pdfs/BIM_PPT_AnAdministrativeView_073020.pdf
[36] GSA BIM guides: https://origin-www.gsa.gov/system/files/largedocs/BIM_Guide_Series_Facility_Management.pdf (fetch returned 404); NIBS NBIMS-US V3 4.3 Spatial Validation: https://www.nibs.org/files/pdfs/nbimsv3/NBIMS-US_V3_4.3_Design_to_Spatial_Validation_SPV.pdf
