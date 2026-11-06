# Abbreviations and acronyms (international and national)

**Last researched: 2026-11-06**

## In plain words

BIM and openBIM are full of three-to-five-letter acronyms, and the same letters often mean different things in different places (for example LOD, CIM or "ЦИМ"). This file expands each acronym, gives the original-language term plus English, and states in one line what it means in practice. It is split into: (1) buildingSMART / openBIM data standards, (2) ISO 19650 information-management terms, (3) detail/information-level terms, (4) data exchange and domain terms, (5) national terms (Russia, Singapore, Netherlands, DACH, Spain, Chile, UK). For a QA tester of IFC/Revit MCP servers: when a request mentions an acronym, first decide which family it belongs to (file format and schema, process document, or national rule), because the test question and the expected answer differ completely.

**Evidence labels.** `[n]` marks a fact seen on the cited page during this research run. "(unverified)" marks facts from general domain knowledge that this run could not confirm on a primary source, because most official sites (buildingsmart.org technical pages, iso.org, standards.buildingsmart.org, gge.ru, Autodesk help) returned HTTP 403/404 or were unreachable and the search tool budget was exhausted (see Gaps). Treat "(unverified)" entries as leads to check, not as ground truth.

---

## 1. buildingSMART / openBIM data standards

| Acronym | Expansion (English) | Original-language form | One-line meaning |
|---|---|---|---|
| **bSI** (buildingSMART International) | buildingSMART International | - | The non-profit that develops and maintains IFC and related openBIM standards [8][9]. |
| **IFC** | Industry Foundation Classes | - | Open, vendor-neutral data schema for AEC/FM data; current ISO edition is ISO 16739-1:2024; releases run from IFC 1.0 (1996) to IFC4.3 Add2 (2024) [8]. |
| **IFC-SPF** | IFC STEP Physical File | - | The common text serialization, extension `.ifc`; other serializations are IFC-XML, IFC-ZIP, RDF/Turtle, ifcJSON, ifcHDF [8]. |
| **IFC2x3 / IFC4 / IFC4.3** | schema versions | - | IFC2x3 (February 2006) [8], IFC4, IFC4.3 (infrastructure: roads, rail, bridges). ISO numbers for the older editions (ISO/PAS 16739:2005, ISO 16739:2013, ISO 16739-1:2018) are (unverified); only ISO 16739-1:2024 was confirmed [8]. |
| **EXPRESS** | EXPRESS data modelling language (ISO 10303-11) | - | Language in which the IFC schema is written [8] (ISO part number unverified). |
| **MVD** | Model View Definition | - | A subset of IFC for a specific exchange purpose; software certifies against an MVD. COBie is itself an MVD [5]. |
| **mvdXML** | MVD in XML | - | Machine-readable MVD format; versions 1.1 and 1.2. The repo is archived; per its README, with the MVD policy and IDS in place mvdXML is "only used as internal structure for Software Certification", and 1.2 is being used for IFC 4.3 certification [11]. |
| **RV** | Reference View | - | MVD for IFC4 (and IFC4.3): reference-geometry exchange for coordination; read-only use of the model. (Definition from general knowledge, unverified.) |
| **DTV** | Design Transfer View | - | MVD for IFC4: exchange where the receiving tool may edit and continue the design. (unverified) |
| **CV2.0** | Coordination View 2.0 | - | The long-standing MVD for IFC2x3, which most older Revit exports use. (unverified) |
| **IDM** | Information Delivery Manual | - | Process-level method (ISO 29481) that documents who needs what information when; the human-readable ancestor of MVD/IDS. (ISO number unverified.) |
| **IDS** | Information Delivery Specification | - | Computer-interpretable XML standard defining IFC-based information requirements, published as an XSD (`Schema/ids.xsd`) plus examples [1]. Used to audit a model against requirements (typical tooling: IfcOpenShell's IfcTester, unverified in this run). |
| **BCF** | BIM Collaboration Format | - | Standard for exchanging issues/viewpoints between BIM tools; file-based XML spec in the BCF-XML repo (release_3_0 branch), API-based BCF in a separate repo; developed by the Open CDE workgroup [2]. File extension `.bcf`/`.bcfzip` (unverified). |
| **bSDD** | buildingSMART Data Dictionary | - | Online service hosting classifications, properties, allowed values, units and translations; read via API (Swagger docs, TEST environment); authors publish via API or Manage portal [3]. |
| **OpenCDE API** | Open Common Data Environment API | - | buildingSMART API family for linking CDEs and BIM tools [2] (details unverified). |
| **PSet / Qto** | Property Set / Quantity Set | - | IFC containers for properties (e.g. `Pset_WallCommon`) and quantities (e.g. `Qto_WallBaseQuantities`). Names from general knowledge (unverified). |
| **GlobalId / GUID** | Globally Unique Identifier | - | 22-character base-64 identifier of every rooted IFC object. (unverified) |
| **IfcProject** | - | - | Every valid IFC file must contain exactly one IfcProject [8]. |

## 2. ISO 19650 and information management terms

ISO 19650 parts: Part 1 Concepts and principles (2018); Part 2 Delivery phase of assets (2018); Part 3 Operational phase (2020); Part 4 Information exchange (2022); Part 5 Security-minded approach (2020); Part 6 Health and safety information (2025) [4]. The data above was taken from a secondary encyclopedia page, not from iso.org.

| Acronym | Expansion | One-line meaning |
|---|---|---|
| **EIR** | Exchange Information Requirements | What the appointing party needs delivered (formats, LOIN, naming, exchange dates) for a given appointment [4]. |
| **OIR** | Organizational Information Requirements | What an organization needs to know about its assets to run its business [4]. |
| **AIR** | Asset Information Requirements | What information is required to operate and maintain an asset [4]. |
| **PIR** | Project Information Requirements | What information is required to make decisions during project delivery [4]. |
| **BEP** | BIM Execution Plan | Supplier's plan on how information will be produced and exchanged; pre-appointment and post-appointment versions exist [4] (the pre/post split is from general knowledge, unverified). |
| **MIDP** | Master Information Delivery Plan | Consolidated schedule of all information deliverables of a project [4]. |
| **TIDP** | Task Information Delivery Plan | Per-task-team schedule of deliverables; MIDP is the sum of TIDPs [4]. |
| **CDE** | Common Data Environment | The agreed source of information for a project or asset [4,12]. Containers typically move through the states WIP, Shared, Published, Archive (unverified in this run). |
| **PIM / AIM** | Project / Asset Information Model | The PIM, built during delivery, transitions into the AIM used in operation [4]. |
| **IM** | Information Management | Process-side term; the Wikipedia article spells it out rather than defining it [4]. |
| **Appointing party / Lead appointed party / Task team** | ISO 19650 role terms | Client-like party; main contractor/designer-like party; group producing one set of deliverables. Roles named but not defined in the secondary article [4]; definitions unverified. |
| **UK BIM Framework** | - | UK guidance aligned with ISO 19650 since 2019 [6]. Older British documents PAS 1192-2/-3 and BS 1192 were its predecessors (unverified); BS 1192-4:2014 is the COBie code of practice [5]. |

## 3. Detail and information level terms

| Acronym | Expansion | One-line meaning |
|---|---|---|
| **LOD** | Level of Development (also read as Level of Detail) | Ambiguous: US usage (BIMForum) means model element development; many people say "detail" [6]. Levels 100-500 incl. 350 are from general knowledge (unverified). In Germany VDI 2552 Part 1 grades information from 0 up to 500 [7]. |
| **LOI** | Level of Information | Alphanumeric/property side of LOD; VDI 2552 Part 1 uses the term [7]. |
| **LOG** | Level of Geometry | Geometry side of LOD (unverified). |
| **LOIN** | Level of Information Need | Standardized replacement for LOD/LOI: defines the minimum geometry, alphanumeric information and documentation needed for a purpose. Referenced as ISO 7817-1:2024 [10] and DIN EN 17412-1 (2021) [7]; the DIN page gives 2021 while EN 17412-1:2020 is the usual citation (unverified). |

## 4. Exchange formats, domain and discipline terms

| Acronym | Expansion | One-line meaning |
|---|---|---|
| **COBie** | Construction Operations Building information exchange | Spreadsheet/IFC-based handover data for facility management; British code of practice BS 1192-4:2014; US NBIMS-US chapter 4.2 published COBie 2.4 in March 2015, based on IFC4 (earlier 2.26 of 2009 used IFC2x3) [5]. Formats: spreadsheet, STEP Part 21, ifcXML [5]. |
| **gbXML** | Green Building XML | Open schema moving building data from BIM to energy/engineering analysis tools; exported geometry quality is often poor, and HVAC/loads are often re-entered manually [13]. |
| **QTO** | Quantity Take-Off | Extracting quantities (areas, volumes, counts) from the model for cost or procurement; BIM allows automated take-off [7]. Expansion itself is general knowledge. |
| **MEP** | Mechanical, Electrical, Plumbing | Building services disciplines [6]. |
| **HVAC** | Heating, Ventilation and Air Conditioning | Subset of MEP; in IFC the entities include IfcDuctSegment, IfcAirTerminal etc. (unverified). |
| **FM** | Facility Management | Coordinating the physical workplace with people and the work of the organization (IFMA definition) [14]. |
| **CAFM** | Computer-Aided Facility Management | IT support for FM; often used interchangeably with CMMS (computerized maintenance management system) [14]. IWMS (Integrated Workplace Management System) is the broader sibling (unverified). |
| **GIS** | Geographic Information System | Spatial data systems (maps, coordinates); BIM-GIS link needs CRS handling via IfcMapConversion in IFC4 (unverified). |
| **CIM** | City / Civil / Construction Information Model - ambiguous | Depending on author: City Information Modelling, Civil Information Modelling. In Russian, ЦИМ means "цифровая информационная модель", a different thing [15]. Do not assume. |
| **AEC / AECO** | Architecture, Engineering, Construction (and Operations) | Industry label (general knowledge). |
| **BIM** | Building Information Modeling/Modelling (Spanish: Modelado de Información de Construcción) | Processes and methods for creating and managing data about a building or civil work in a shared digital model across its life cycle [16]. |
| **GFA** | Gross Floor Area | Used in CORENET X thresholds (30,000 m2) [17]. |
| **RVT / RFA / RTE / RFT** | Revit Project / Family / Template / Family Template files | Native Revit file extensions (general knowledge, unverified). |
| **ACC** | Autodesk Construction Cloud | Autodesk CDE/cloud platform, successor of BIM 360 (unverified). |

## 5. National and regional terms

### 5.1 Russia

| Acronym | Expansion (Russian) | English | One-line meaning |
|---|---|---|---|
| **ТИМ** | технологии информационного моделирования | information modelling technologies | Russian umbrella term for the BIM approach in regulations (expansion from general knowledge; the cited pages list ТИМ as a topic without expanding it [18]) (unverified). |
| **ИМ** | информационная модель | information model | The model itself; the term appears in Article 48 of the Градостроительный кодекс (Town Planning Code) in connection with architectural and construction design [15]. |
| **ЦИМ** | цифровая информационная модель | digital information model | Called the Russian analogue of BIM [15]. |
| **КСИ** | Классификатор строительной информации | Construction information classifier | National classifier used to code elements of information models; listed with its basis documents and a Ministry (Минстрой) order on the FAU FCS site [18]; details unverified. |
| **СП** | свод правил | set of rules | Standardization document with rules to meet technical regulation requirements; not part of the national standardization system, though some SPs (updated SNiP) are mandatory under Federal Law 384-FZ (list in Government Decree No. 815 of 2021) [19]. |
| **СП 333.1325800.2020** | Информационное моделирование в строительстве. Правила формирования информационной модели объектов на различных стадиях жизненного цикла | BIM: rules for forming the information model of objects at various life-cycle stages | Key Russian rule set on information model formation [15]. |
| **ГОСТ Р** | национальный стандарт Российской Федерации (ГОСТ Р) | Russian national standard | Issued by Росстандарт; "Р" marks use inside Russia only; plain ГОСТ = interstate standard [20]. |
| **ГОСТ Р 21.101-2020** | Система проектной документации для строительства. Основные требования к проектной и рабочей документации | Design documentation system: basic requirements | In force from 1 January 2021 [15]. |
| **ГОСТ Р 10.0.xx series** | Система стандартов информационного моделирования зданий и сооружений | BIM standards system | Series of BIM standards (numbers such as 10.0.02-2019 are from general knowledge) (unverified). |
| **ГГЭ** | Главная государственная экспертиза (Главгосэкспертиза России) | Main State Expert Review (Glavgosexpertiza) | State expert review body for design documentation, including review of information models. The page for the body could not be fetched; the same-letters ГГЭ expansion and function are (unverified) [15 mentions only the topic]. |
| **ПП РФ 331 / 1431** | постановления Правительства РФ | Government decrees | Decrees on information model composition and rules; numbers from the task brief were not confirmed on any fetched page [15] (unverified). |
| **Пр-1235 (19.07.2018)** | поручение Президента | Presidential instruction | Instruction to move to life-cycle management of capital construction objects based on information modelling technology [15]. |

### 5.2 Singapore

| Acronym | Expansion | Meaning |
|---|---|---|
| **CORENET X** | Construction and Real Estate NETwork (X) - expansion unverified | Joint government-industry effort redesigning building regulatory submission with BIM and automation, phased rollout [17]. |
| **IFC+SG** (written IFC-SG in some documents) | IFC for Singapore | BIM submission format; site covers data structure, Excel mapping file, modelling practices, authoring tools, plug-ins, glossary; a Model Checker MVP checks IFC compliance before submission [17]. |
| **BCA, LTA, NEA, NParks, PUB, SCDF, URA** | Building and Construction Authority, Land Transport Authority, National Environment Agency, National Parks Board, Public Utilities Board, Singapore Civil Defence Force, Urban Redevelopment Authority | Participating agencies [17] (expansions are general knowledge except where the site gives them). |
| **Gateways** | Design, Construction, Completion (plus Piling, Pre-Submission Consultation, Independent Submissions) | New submission stages [17]. |
| **DSP** | Direct Submission Process | Simplified route for small projects such as single landed homes [17]. |
| **Key date** | 1 Oct 2025 | New projects with GFA of 30,000 m2 or more must onboard and submit through the Submission Portal [17]. |

### 5.3 Netherlands

| Acronym | Expansion | Meaning |
|---|---|---|
| **ILS** | Informatie Leverings Specificatie (Dutch; expansion unverified) | Family of delivery specifications on digiGO: BIM basis ILS, ILS Ontwerp & Engineering, BIM basis Infra, Basis ILS Puntenwolk, ILS Bestaande Bouw, ILS-woco, MiniBIM, MiniGIM, plus an ILS Configurator [21]. |
| **NL-SfB** | Nederlandse SfB classificatie (unverified) | Dutch building-element classification listed under standards on digiGO [21]; details unverified. |
| **Rgd BIM Standard** | Rijksgebouwendienst BIM Standard | Introduced 1 November 2011, updated 1 July 2012 [6]. |

### 5.4 Germany, Austria

| Acronym | Expansion | Meaning |
|---|---|---|
| **AIA** | Auftraggeber-Informations-Anforderungen (client information requirements) | German-language equivalent of EIR [unverified; term absent from the fetched page [7]]. |
| **BAP** | BIM-Abwicklungsplan (BIM execution plan) | German-language equivalent of BEP (unverified). |
| **VDI 2552** | VDI guideline series on BIM | Part 1 grades Level of Information 0 to 500 [7]. |
| **Stufenplan Digitales Planen und Bauen** | Phased plan for digital planning and construction | BMDV plan; BIM mandatory for new infrastructure-related projects since 2020 [7]. |
| **ÖNORM A 6241** | Austrian standard | Summarizes Austrian digital modelling standards, published 15 March 2015 [6]. |

### 5.5 Spain, Chile

| Acronym | Expansion | Meaning |
|---|---|---|
| **es.BIM** | Comisión interministerial es.BIM (unverified) | Spanish national BIM commission. The es.BIM website could not be fetched (certificate error). A July 2015 national strategy made BIM mandatory for public projects, possible start 2018 [6]. |
| **Planbim / Plan BIM** | Plan BIM Chile | Chilean BIM programme; planbim.cl covers technology, construction and BIM, a guide with BID for public-sector BIM pilots, MINVU implementation, Red BIM de Gobiernos Latinoamericanos, a free e-learning course and an article on IFC 4.3 and 4.4 [22]. Who runs it (CORFO) is (unverified). |
| **BID** | Banco Interamericano de Desarrollo | Inter-American Development Bank [22]. |
| **MINVU** | Ministerio de Vivienda y Urbanismo | Chilean housing ministry [22]. |

### 5.6 Other national references

- **Italy:** D.Lgs. 50/2016 art. 23 and DM 560 of 1 Dec 2017 are cited as the legal basis for BIM mandates in public works [23].
- **Finland:** Senate Properties (Senaatti) modeling guidelines; Senate Properties required IFC-compatible software from 2017 [8,23].
- **Denmark:** IFC required for publicly aided building projects from 2010 [8].

---

## Typical questions people ask about this

I could not retrieve real forum threads in this run (search budget exhausted), so all questions below are (illustrative).

1. What is the difference between IFC, MVD and IDS? (illustrative)
2. Which MVD should I choose when exporting from Revit: Coordination View 2.0, Reference View or Design Transfer View? (illustrative)
3. What does "LOD 350" mean, and how does it relate to LOIN? (illustrative)
4. What is the difference between EIR, OIR, AIR and PIR? (illustrative)
5. Is the MIDP the same as the TIDP? (illustrative)
6. What is a BEP, and is it the same as the German BAP? (illustrative)
7. What is COBie and which IFC version does it use? (illustrative)
8. Is BCF a file or an API? (illustrative)
9. What is bSDD and how does it differ from an IFC property set? (illustrative)
10. Is an IDS file the same as an mvdXML file? (illustrative)
11. What does the MCP server mean by "validate against IDS"? (illustrative)
12. What does ЦИМ mean and is it the same as BIM? (illustrative)
13. Что такое ТИМ и чем он отличается от BIM? (illustrative)
14. What is the difference between СП and ГОСТ Р? (illustrative)
15. What is CORENET X and why must the model be IFC+SG? (illustrative)
16. Is CIM city or civil information modelling? (illustrative)
17. What is gbXML and when do I use it instead of IFC? (illustrative)
18. What is the difference between CAFM, CMMS and FM? (illustrative)
19. Does an IFC export from Revit contain quantities (Qto) by default? (illustrative)
20. What does a CDE state like WIP or Shared mean? (illustrative)

## Common pitfalls and misconceptions

- **LOD is not one thing.** Level of Development, Level of Detail, and the German LOI/VDI 2552 scale (0-500) are different scales; LOIN (ISO 7817-1:2024 / EN 17412-1) is the intended replacement [6,7,10].
- **MVD, mvdXML, IDM and IDS are not interchangeable.** MVD = subset of IFC; mvdXML = machine form of it, now mainly used for certification [11]; IDM = process method; IDS = XML requirements you can check models against [1].
- **BCF is both file and API.** The file-based spec and the API spec live in different repos [2].
- **COBie is an MVD / spreadsheet profile, not a separate schema.** Version 2.4 is based on IFC4; 2.26 used IFC2x3 [5].
- **gbXML is not IFC.** It is an energy-analysis schema; geometry transferred through it is often poor [13].
- **"CIM" and "ЦИМ" are different abbreviations in practice.** One is Latin letters in English contexts, the other a Russian term meaning digital information model [15].
- **IFC+SG vs IFC-SG.** The CORENET X site writes IFC+SG [17]; test prompts may use either spelling.
- **СП is not a ГОСТ.** СП sits outside the national standardization system although some are mandatory [19][20].
- **ISO 16739-1:2024 is current**, but Revit exports and older tools still produce IFC2x3 or IFC4; a model labelled "IFC" can be any of these [8].
- **AIA** in German BIM means client information requirements; in the US AIA is the American Institute of Architects (general knowledge). Check language context.
- **ILS expansion and NL-SfB details are not verified here**; do not quote them as authoritative.

## Gaps

- Official pages returned HTTP 403: technical.buildingsmart.org (IFC, IDS, BCF), standards.buildingsmart.org (IFC4.3 docs), iso.org (ISO 19650-1 page), gge.ru; Autodesk help URL tried was not found; minstroyrf.gov.ru refused the connection; esbim.es failed certificate validation; ru.wikipedia pages for Главгосэкспертиза and Wikipedia pages for level of development, NL/SfB and CDE returned 404. These were not worked around.
- The web search tool reported its budget used up on first use, so no search for real user questions, native-language forum threads or official announcements was possible. Everything marked (unverified) should be rechecked.
- No suspicious, pirated or phishing sites were encountered or linked.

## Sources

1. https://github.com/buildingSMART/IDS (IDS README, XSD)
2. https://github.com/buildingSMART/BCF-XML (BCF file-based standard, release_3_0)
3. https://github.com/buildingSMART/bSDD (bSDD README)
4. https://en.wikipedia.org/wiki/ISO_19650 (secondary source: parts, terms)
5. https://en.wikipedia.org/wiki/COBie (secondary source)
6. https://en.wikipedia.org/wiki/Building_information_modeling (secondary source; national mandates, LOD)
7. https://de.wikipedia.org/wiki/Building_Information_Modeling (secondary source; VDI 2552, DIN EN 17412-1, Stufenplan)
8. https://en.wikipedia.org/wiki/Industry_Foundation_Classes (secondary source; ISO 16739-1:2024, formats)
9. https://github.com/buildingSMART (organization, used only via the repos above)
10. Reference list of the English Wikipedia BIM article (offset 100000 of https://en.wikipedia.org/wiki/Building_information_modeling) citing ISO 7817-1:2024
11. https://github.com/buildingSMART/mvdXML (archived, mvdXML 1.1/1.2)
12. https://en.wikipedia.org/wiki/ISO_19650 (CDE definition; the dedicated CDE page was a 404)
13. https://en.wikipedia.org/wiki/GbXML (secondary source)
14. https://en.wikipedia.org/wiki/Computer-aided_facility_management (secondary source)
15. https://ru.wikipedia.org/wiki/BIM (secondary source; ЦИМ, СП 333.1325800.2020, ГОСТ Р 21.101-2020, Пр-1235)
16. https://es.wikipedia.org/wiki/Modelado_de_información_de_construcción (secondary source)
17. https://info.corenet.gov.sg/ (official CORENET X site)
18. https://www.faufcc.ru/technical-regulation-in-construction/ksi/ (official FAU FCS page; only headings readable)
19. https://ru.wikipedia.org/wiki/Свод_правил (secondary source)
20. https://ru.wikipedia.org/wiki/ГОСТ_Р (secondary source)
21. https://www.digigo.nu/ (Dutch digiGO site; ILS listing)
22. https://planbim.cl/ (Plan BIM Chile)
23. https://en.wikipedia.org/wiki/Building_information_modeling (reference list: Italy D.Lgs. 50/2016, DM 560/2017; Finland Senate Properties)
