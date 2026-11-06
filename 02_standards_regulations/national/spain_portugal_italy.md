# Spain, Portugal, Italy: BIM/IFC requirements

## In plain words

Spain, Portugal and Italy all use BIM in public works, but in three different ways. Italy has the clearest hard rule: since 1 January 2025 public clients must use BIM methods for new works and for interventions on existing buildings with an estimated works cost above EUR 2 million, and the law requires open, non-proprietary, interoperable formats [1]. Spain has no single national "BIM law"; BIM is enabled by the public procurement law and pushed by an inter-ministerial commission (es.BIM), and buildingSMART Spain publishes the practical IFC delivery rules [2][3][4]. Portugal relies on a standardisation committee (CT 197) and guides (a contracting guide and a BIM execution plan guide) rather than a binding national mandate found in this research (unverified) [5][6]. For an MCP tester: IFC is the "open format" that these rules point to, but the exact IFC version and view definition (MVD) are usually fixed in each project's information requirements, not in the national law.

**Last researched: 2026-11-06** (QA pass 2026-11-06: Normattiva Art. 43 D.Lgs. 36/2023 and the Italian Wikipedia BIM page re-fetched and confirmed; see `_meta/qa/qa-standards-2.md`.)

> Research limitations for this document: the web search budget of the session ran out before any search could be run, so everything here comes from direct page fetches of primary sources plus clearly labelled background knowledge. Items marked "(unverified)" were not confirmed on a primary source in this session. See "Gaps" at the end.

---

## 1. Quick comparison

| Topic | Spain | Portugal | Italy |
|---|---|---|---|
| Binding BIM obligation for public works | No single national threshold confirmed; BIM allowed/encouraged via procurement law (Ley 9/2017) and es.BIM plan (unverified details) | No national mandate confirmed in this research (unverified) | Yes: Art. 43 D.Lgs. 36/2023, from 1 Jan 2025, works cost over EUR 2 M [1] |
| Main coordinating body | Comisión Interministerial BIM (es.BIM), under the Ministry of Transport (Ministerio de Transportes y Movilidad Sostenible) [3] | CT 197 (technical standardisation committee for BIM), coordinated by ONS/IST per buildingSMART Portugal [6] | MIT (Ministry of Infrastructure and Transport), ANAC, UNI [1][7] |
| National standard series | UNE (ISO 19650 adoptions; not verified here) | NP/IPQ via CT 197 (unverified) | UNI 11337 series, UNI EN ISO 19650 [7][8] |
| buildingSMART chapter | buildingSMART Spain (BSSP) [2] | buildingSMART Portugal [6] | buildingSMART Italia, run by IBIMI [9] |
| Practical IFC guidance | "Manual de Entrega de IFC (MEI) Edificación" v2.0 + IDS file; infrastructure manual [4][10][11] | Little IFC-specific national guidance found (unverified) | Several buildingSMART Italia IFC guides: bridges, roads, structures [12] |
| National classification | GuBIMClass (referenced by MEI) [4] | Not verified | Not defined in Code; client specifies in capitolato informativo (unverified) |

---

## 2. Spain

### 2.1 Who and what

- **Comisión Interministerial BIM / es.BIM**: a commission of Spanish ministries and public bodies promoting BIM in public procurement. buildingSMART Spain states that the "Comisión Interministerial BIM", through the Ministry of Transport and Sustainable Mobility, commissioned it to produce training videos for public-sector technicians on preparing, tendering and executing BIM contracts [13]. The commission's own site (esbim.es) could not be fetched in this session (TLS certificate error), so its exact documents, the dates of its "Plan de incorporación de BIM en la contratación pública" and any 2024+ phases are **unverified**.
- **Background (unverified):** in July 2015 a meeting at the Ministry launched the national BIM strategy, with a possible mandatory start in 2018 [14]. The commission was created in that period. A phased plan for BIM in public procurement and a set of "Guías uBIM" exist (the Guías uBIM are named on the buildingSMART Spain page [13]); their phase calendar and thresholds must be checked on esbim.es.
- **Legal anchor: Ley 9/2017 de Contratos del Sector Público (LCSP)**, BOE-A-2017-12902 [15]. The task brief asked to check its "additional provision 15". Confirmed: the law has a *Disposición adicional decimoquinta* on electronic communication rules (it is referenced by Art. 138.2.a and 140.1.a.4 for electronic access and notifications) [15]. The BIM sentence (use of "herramientas electrónicas específicas" such as building information modelling tools, derived from Directive 2014/24/EU Art. 22(4)) was **not located** in the text I could read, so its exact paragraph is **unverified**.
- **Adoption data:** the buildingSMART Spain "Estudio Adopción BIM 2024" reports 32% of organisations have implemented BIM and 26% are in process; the CIBIM observatory shows almost 12% of public tenders include BIM requirements; Catalonia leads, then Madrid, Andalusia, Valencian Community, Basque Country; users ask mainly for ISO 19650 and IFC [16].

### 2.2 buildingSMART Spain and IFC rules

buildingSMART Spain (BSSP) is the chapter; it runs working tables (constructors, design, public administrations), an openBIM section (IFC, IDS, bSDD, BCF, IFC validation, FAQ), certification (Initial, Fundamentals, Practitioner) and a BIM tenders observatory [2][17][18].

**Manual de Entrega de IFC (MEI) en Edificación, v2.0** [4]:
- Purpose: recommended information requirements so IFC building models are consistent and structured.
- Principles: define the project origin point; name building levels properly; use IFC entities and properties correctly; apply classification systems.
- Sections (titles only on the page): naming, local position, levels, entities, structure, classification, property sets (Psets), duplicates, partial models, spaces, systems, load-bearing elements, exterior elements, fire protection, physical properties, materials, project information.
- Adapted from a document by DIGIGO; authors David Delgado Vendrell and Sergio Muñoz, with voluntary collaboration from BIM Loket (named on the page; individuals credited publicly as authors).
- A companion **IDS file** automatically checks presence of minimum information: level ordering, entity use, classification (**GuBIMClass**), space naming, properties (load-bearing, interior/exterior, fire resistance, thermal transmittance) and material. It does not check specific values, geometry or coordination [4][19].
- The page does **not** state the IFC schema version, MVD or georeferencing details; those are in the downloadable PDF (not read) [4]. Treat "IFC4 Reference View vs IFC2x3 Coordination View" as a project-level choice (unverified).

**Manual de Entrega de Información en Infraestructuras** [11]: two parts, "BIM Básico Infra" (principles, adapted from BIM Loket) and "Anexo IFC" (still in development). A reference point (Punto de Referencia v1.0) is offered in IFC4 ADD2 TC1 and IFC2x3 TC1. Coordinators credited: Jose Carlos Rico (FCC), Jorge Torrico (INECO).

**IDS example from BSSP** [19]: a requirement that walls carry thermal transmittance between 0.6 and 0.7 in `Pset_WallCommon`; the demo result is 7 of 10 walls compliant, 2 missing the property, 1 out of range (0.58). Only IDS 1.0 is a final standard; the page's own sample references 0.9.7.

**IFC validation** [20]: the buildingSMART validation service (validate.buildingsmart.org) checks STEP syntax and the IFC schema (including EXPRESS rules and implementer agreements), reports bSDD reference mismatches as warnings, does not check project- or country-specific rules (use IDS) and does not display geometry. Account required; files processed on Azure (Amsterdam and Dublin).

### 2.3 Classification and naming

- **GuBIMClass** is the classification named in the MEI IDS checks [4]. Its website could not be read (only a tracking pixel returned), so its basis (understood to be a Spanish classification related to Uniclass; unverified) is not confirmed here.
- buildingSMART Spain also publishes "Nomenclatura Documentos BIM" (document naming) and an EN-ISO 19650 resource with FAQs [17].

### 2.4 Typical Spanish workflow in a tender

From the BSSP training page [13]: the contracting body assesses needs and defines BIM scope (objectives, uses, deliverables, review and delivery, human and technical resources); the contractor writes the **BIM Execution Plan (BEP)** and the contracting body approves it; the **MIDP** (Master Information Delivery Plan) is annexed to the BEP; requirements can be checked by opening IFC models in IFC viewers; automatic model quality checks include clash detection.

---

## 3. Portugal

- **CT 197**: the Portuguese technical committee for BIM standardisation. A general reference states CT197-BIM was created in 2015 and produced a strategic document for "construction 4.0" [14]. buildingSMART Portugal says the committee is coordinated by ONS/IST and lists two documents: the **Guia de Contratação BIM** (published; year not stated) and a **Plano de Execução BIM** guide (in development) [21]. The CT 197 website (ct197.pt) refused connection in this session, so the exact standard numbers (NP / IPQ), dates and any national roadmap are **unverified**. IPQ is the national standardisation body; the catalogue is at ipq.pt/normalizacao [22].
- **Mandate:** no Portuguese law or decree making BIM compulsory in public works was confirmed. A generic buildingSMART Portugal introduction page covers only international examples and does not describe a Portuguese mandate [23]. Treat any statement of a national BIM mandate for Portugal as **unverified**. Public contracts are governed by the *Código dos Contratos Públicos* (CCP); whether it explicitly cites BIM is **unverified**.
- **buildingSMART Portugal**: mission "Liderar a transformação digital em Portugal"; working groups, international domains, OpenBIM Day 2026, a certification programme listed as "coming soon" [6].
- **IFC specifics:** no Portuguese national IFC delivery manual, MVD or property-set convention was found (unverified). Projects typically adopt ISO 19650 terminology and buildingSMART International standards [24].

---

## 4. Italy

### 4.1 The legal chain

| Instrument | What it does | Status |
|---|---|---|
| D.Lgs. 50/2016 (old Code), Art. 23 | Introduced "progressive adoption of digital methods" such as BIM [14] | Replaced by D.Lgs. 36/2023 |
| **DM MIT 560/2017** (1 December 2017; date confirmed on Italian Wikipedia in QA, which gives no phase thresholds) | Implements Art. 23 of the old Code; sets phased adoption of BIM by tender amount [25]. The schedule was reported as starting 1 Jan 2019 for the largest contracts with a general 2025 horizon [14]. Exact yearly thresholds **unverified** | Superseded for new procedures by the 2023 Code (unverified how transitional rules apply) |
| **DM MIT 312/2021** | Amends/integrates DM 560/2017 (understood to concern information-management requirements and dates; exact content **unverified**: the Normattiva page failed to load) | Unverified |
| **D.Lgs. 36/2023 (new Codice dei contratti pubblici)**, Art. 43 | Current BIM rule (see below) [1] | In force |
| **Allegato I.9** to D.Lgs. 36/2023 | Operating rules for "metodi e strumenti di gestione informativa digitale delle costruzioni" [1][26] | In force |
| D.Lgs. 209/2024 (31 Dec 2024) | Corrective decree; repealed comma 5 of Art. 43 [1] | In force |

### 4.2 Art. 43 D.Lgs. 36/2023 (text in force from 31-12-2024) [1]

QA re-check on Normattiva: comma 1 (1 January 2025, works cost above EUR 2 million, or the Art. 14(1)(a) threshold for protected cultural-heritage buildings, maintenance excluded unless previously done with BIM), comma 3 (interoperable platforms, open non-proprietary formats) and the repeal of comma 5 by D.Lgs. 31 December 2024, n. 209 were all confirmed on the primary page.

- **Comma 1:** from **1 January 2025** contracting authorities and concession-granting entities adopt BIM methods and tools for new works and for interventions on existing buildings where the estimated works cost is **above EUR 2 million** (or, for certain cultural heritage buildings under Art. 10(1) of D.Lgs. 42/2004, the threshold in Art. 14(1)(a)). Ordinary and extraordinary maintenance is excluded unless it concerns works previously done with BIM.
- **Comma 2:** below the thresholds, authorities may still adopt BIM and award scoring points for it, provided they adopt the Allegato I.9 measures.
- **Comma 3:** tools must run on interoperable platforms using **open, non-proprietary formats** ("formati aperti non proprietari"), to avoid restricting competition and to allow data transfer.
- **Comma 4:** Allegato I.9 defines training/tools/organisation of staff, uniform adoption criteria, interoperability with the national public works archive and investment-monitoring systems, data exchange, applicable standards and the minimum content of the **capitolato informativo**.

### 4.3 Allegato I.9 (single Art. 1, commi 1 to 13) [26]

Summary of the version read (a third-party mirror of the Code; check Normattiva for the consolidated text):
- The authority adopts its own **CDE** (ambiente di condivisione dei dati) and appoints a CDE manager and at least one digital process manager.
- **Capitolato informativo**: required for architecture/engineering services (comma 8) and for works contracts with executive design or design-and-build (comma 9), covering information requirements, production and archiving rules, CDE conditions and interoperability.
- Bidders in best-value tenders submit an **offerta di gestione informativa**; the awardee prepares the **piano di gestione informativa** after contract signature and before execution (comma 10).
- Standards hierarchy (comma 6): European (UNI EN / UNI EN ISO), then international (UNI ISO), then national (UNI). Comma 7 names the **UNI EN ISO 19650 series**; the **UNI 11337 series** is described as a useful reference, not mandatory.
- **IFC is not named** in the text read; open formats are required in general terms. In practice the capitolato informativo of each client names IFC (typically IFC4 or IFC2x3; project-specific, unverified).
- Allegato I.13 applies a 10% design-fee increase for contracts requiring these methods [26].

### 4.4 UNI 11337 and ISO 19650

- UNI 11337 is the Italian BIM series. Reported by a general reference: parts 1, 4 and 5 published January 2017 [14]; Part 4 (2017) defines LOD A (symbolic) to G (updated) made of LOG (geometry) and LOI (information); Part 6 defines BIM dimensions 1D to 7D (1D concept design, 2D drawings, 3D model, 4D scheduling, 5D costs, 6D operation and maintenance, 7D sustainability) [27] (UNI 11337-4:2017 and -6 re-confirmed on Italian Wikipedia in QA; other part years remain unverified). The full list of parts and their years is **unverified** (UNI site did not give it). 
- UNI EN ISO 19650-1/-2 (information management) are the European/international reference named by Allegato I.9 [26].

### 4.5 buildingSMART Italia and IFC guidance

buildingSMART Italia is operated by IBIMI (Istituto per il BIM Italia), a non-profit; national domains cover software, professions, products, infrastructure, buildings, and contracting authorities. It offers software certification, professional certification and accreditation of training organisations [9]. Publications relevant to IFC and tenders [12]:
- Guida all'IFC per il progetto strutturale degli edifici (2024; IFCStructure Italia).
- Guida all'IFC per il progetto stradale (2022; IFC Road).
- Linea guida all'applicazione dell'IFC per ponti e viadotti (2020).
- Linee guida per la compilazione della sezione tecnica dei capitolati informativi: formato file (2019).
- Linee Guida Capitolati Informativi: procedure propedeutiche per le Stazioni Appaltanti (2025) and "Questionario Maturità per le Stazioni Appaltanti" (2024).
- Buone pratiche per la modellazione informativa delle strutture (2026; IFC4, IfcStructuralAnalysisDomain).
- Linea guida per l'applicazione dell'OpenBIM alla modellazione degli impianti IRAI (2024); Scan to BIM (2024); openBIM for Airports (2026).
- BIMcert Handbook (2025).

---

## 5. IFC-specific requirements across the three countries

| Item | Spain | Portugal | Italy |
|---|---|---|---|
| IFC version | Not fixed nationally; MEI v2.0 does not state it on its web page [4]; infra reference point in IFC4 ADD2 TC1 and IFC2x3 TC1 [11] | Not found | Not fixed in law; set per project in capitolato informativo (unverified); IFC4 used in structural good practice guide [12] |
| MVD | Not stated on the web page [4] | Not found | Not found in law |
| Property sets | Standard IFC Psets (e.g. `Pset_WallCommon`) checked via MEI IDS [19] | Not found | Per capitolato |
| Classification | GuBIMClass [4] | Not found | Per capitolato |
| Georeferencing | MEI defines "project origin point" and "local position" sections [4]; exact CRS rules not read | Not found | Not found |
| Naming | MEI naming + "Nomenclatura Documentos BIM" [4][17] | ISO 19650 style (unverified) | UNI 11337 / capitolato |
| Checking | IFC validation service + IDS [19][20] | Not found | CDE and client checks (Allegato I.9) [26] |
| Submission portals | No national BIM portal confirmed | None confirmed | CDE of each authority; Allegato I.9 links to national public works archive [1] |

Important for testers: a model that passes buildingSMART IFC validation can still fail a country rule; country rules live in IDS or in the project's information requirements [20].

---

## 6. Software and tools (practical)

**Revit and IFC (general, not national):** Revit exports IFC from File > Export > IFC; the IFC exporter is open source (Autodesk/revit-ifc on GitHub, LGPLv2, re-confirmed in QA; the README says the latest annual Revit version plus two previous versions are supported); the exact Revit release from which it is bundled (earlier text said 2023) is unverified. In localised Revit the menu is "Archivo > Exportar > IFC" (ES, PT: "Ficheiro > Exportar > IFC") and "File > Esporta > IFC" (IT) (unverified wording). Classification and Psets are normally mapped through the export "User Defined Property Set" and "Parameter mapping" files.

**Local software ecosystem (author knowledge, unverified in this session):**
- Spain: CYPE (IFC Builder, BIMserver.center), Presto (RIB Spain, cost estimating).
- Italy: ACCA software (Edificius, usBIM viewer, BIMcert-related tools), Harpaceas, Biblus.
- Portugal: CYPE Portugal (local presence; other local vendors not verified).
- Open source worldwide and used locally: IfcOpenShell/Bonsai (Blender), xBIM, BIMcollab Zoom (free viewer, Dutch), FreeCAD.

**Communities (labelled as community, not official):** buildingSMART Spain working tables, buildingSMART Italia domains, BIM Loket (collaborated on Spanish manuals) [4][11].

---

## 7. Local terminology table

| Native term | Transliteration / language | English |
|---|---|---|
| Comisión Interministerial BIM (es.BIM) | ES | Inter-ministerial BIM commission |
| Contratación pública | ES | Public procurement |
| Pliego de prescripciones técnicas | ES | Technical specifications of tender |
| Manual de Entrega de IFC (MEI) | ES | IFC delivery manual |
| Plan de Ejecución BIM (BEP) | ES | BIM execution plan |
| Licitación | ES | Tender |
| Modelo de información | ES | Information model |
| Georreferenciación / Punto de origen | ES | Georeferencing / project origin |
| Guia de Contratação BIM | PT | BIM contracting guide |
| Plano de Execução BIM | PT | BIM execution plan |
| Modelação da informação da construção | PT | Building information modelling |
| Código dos Contratos Públicos (CCP) | PT | Public contracts code |
| Ambiente de partilha de dados | PT | Common data environment (unverified wording) |
| Capitolato informativo | IT (capitolato informativo) | Employer's information requirements (EIR) |
| Offerta di gestione informativa (oGI) | IT | Pre-appointment BIM execution plan |
| Piano di gestione informativa (pGI) | IT | BIM execution plan (post-award) |
| Ambiente di condivisione dei dati (ACDat) | IT | Common data environment |
| Stazione appaltante | IT | Contracting authority |
| Gestione informativa digitale delle costruzioni | IT | Digital construction information management |
| Formati aperti non proprietari | IT | Open non-proprietary formats |

---

## Typical questions people ask about this

Real source pages worth linking (not forum questions): BSSP openBIM FAQ [28], BSSP certification FAQ pages [28], IDS explanation [19].

1. What is the difference between IFC, IDS and bSDD? (answered on the BSSP FAQ [28])
2. What is the role of IFC in ISO 19650 information containers? [28]
3. Is BIM mandatory in Italian public tenders after 1 January 2025, and above what value? (EUR 2 million works cost, Art. 43 [1])
4. Does Italian law require IFC specifically? (No: it requires open non-proprietary formats; project documents decide [1][26])
5. What must a capitolato informativo contain? (Allegato I.9 comma 8/9 [26])
6. What is the difference between offerta di gestione informativa and piano di gestione informativa? [26]
7. Is UNI 11337 still mandatory after D.Lgs. 36/2023? (It is described as a reference but not mandatory in Allegato I.9; check current text [26])
8. Which Spanish ministry runs BIM in public procurement and where are es.BIM guides? (illustrative)
9. Is BIM mandatory in Spanish public tenders? (illustrative; no single national obligation confirmed)
10. How do I set the project origin and levels in a Spanish IFC (MEI)? [4]
11. How can I check my IFC against the Spanish MEI automatically? (IDS file from BSSP [4][19])
12. How do I validate that my IFC is valid? (buildingSMART validation service [20])
13. Which classification should I use in Spain, GuBIMClass or Uniclass? (illustrative)
14. Does Portugal have a BIM mandate for public works? (illustrative; none confirmed)
15. Where can I find the Portuguese BIM contracting guide? (CT 197 [21])
16. Which IFC version should I deliver, IFC2x3 or IFC4? (illustrative; project-specific)
17. How do I export IFC from Revit with classification and property sets? (illustrative)
18. Why is my Revit-exported IFC missing wall thermal transmittance? (illustrative; check Pset mapping and IDS)
19. What are the minimum LOD levels for Italian projects? (UNI 11337-4 LOD A to G [27])
20. How do I ask an MCP server to list all IfcWall without `IsExternal` set? (illustrative)

---

## Common pitfalls and misconceptions

- "BIM is mandatory everywhere": true as a clear rule only in Italy (above EUR 2 M, from 2025) [1]; for Spain and Portugal no equivalent single hard rule was confirmed.
- "Italian law requires IFC": no, it requires open non-proprietary formats [1][26].
- Old DM 560/2017 schedules (2019-2025 table) should not be quoted as current law without checking transitional rules (unverified).
- Passing IFC validation does not mean passing national rules; use IDS [20].
- MEI IDS checks presence only, not values or geometry [4].
- Mixing up capitolato informativo (client requirement) with piano di gestione informativa (supplier plan).
- Third-party mirrors of the law (like the one used for Allegato I.9) may lag the consolidated text.

---

## Gaps

- Search budget exhausted at start: no web searches could be run; no forum or community questions were collected.
- esbim.es: TLS certificate mismatch; transportes.gob.es: HTTP 403. es.BIM plan phases and documents unverified.
- ct197.pt: connection refused. Portuguese standard numbers, mandate unverified.
- BOE Ley 9/2017 DA 15 BIM sentence not located in readable portion.
- DM 560/2017 thresholds and DM 312/2021 content: Normattiva page failed to load; unverified.
- UNI 11337 full list unverified.
- No suspicious or pirated sites were encountered.

---

## Sources

1. Normattiva, D.Lgs. 36/2023 Art. 43 (vigente): https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2023-03-31;36!vig=~art43
2. buildingSMART Spain: https://www.buildingsmart.es/
3. (via [13]) Comisión Interministerial BIM, Ministerio de Transportes: https://www.buildingsmart.es/recursos/cómo-emplear-bim-en-un-contrato-público/
4. MEI Edificación v2.0: https://www.buildingsmart.es/recursos/manual-de-entrega-de-ifc-edificación/
5. buildingSMART Portugal guides: https://buildingsmart.pt/guias/
6. buildingSMART Portugal: https://buildingsmart.pt/
7. UNI (index page; no UNI 11337 detail): https://www.uni.com/
8. (see [26] comma 7)
9. buildingSMART Italia: https://www.buildingsmartitalia.org/
10. buildingSMART Spain openBIM: https://www.buildingsmart.es/bim/openbim/
11. Infrastructure manual: https://www.buildingsmart.es/recursos/manual-de-entrega-de-información-infra/
12. buildingSMART Italia publications: https://www.buildingsmartitalia.org/utenti/pubblicazioni/
13. How to use BIM in a public contract: https://www.buildingsmart.es/recursos/cómo-emplear-bim-en-un-contrato-público/
14. Wikipedia, Building information modeling (background, secondary): https://en.wikipedia.org/wiki/Building_information_modeling
15. BOE, Ley 9/2017: https://www.boe.es/buscar/act.php?id=BOE-A-2017-12902
16. Estudio Adopción BIM 2024: https://www.buildingsmart.es/observatorio/estudios/estudio-adopción-bim-2024/
17. BSSP observatory: https://www.buildingsmart.es/observatorio/
18. BSSP BIM tenders: https://www.buildingsmart.es/observatorio/licitaciones-bim/
19. BSSP IDS: https://www.buildingsmart.es/bim/openbim/ids/
20. BSSP IFC validation: https://www.buildingsmart.es/bim/openbim/validación-de-ifc/
21. buildingSMART Portugal guides (CT 197): https://buildingsmart.pt/guias/ (CT 197 site http://www.ct197.pt/ not reachable)
22. IPQ: https://www.ipq.pt/
23. buildingSMART Portugal, what is BIM: https://buildingsmart.pt/o-que-e/
24. buildingSMART Portugal standards: https://buildingsmart.pt/normas/
25. Italian Wikipedia, BIM (DM 560/2017): https://it.wikipedia.org/wiki/Building_Information_Modeling
26. Allegato I.9 (mirror): https://www.bosettiegatti.eu/info/norme/statali/2023_0036_A.htm
27. (same as [25], UNI 11337-4 and -6)
28. BSSP openBIM FAQ: https://www.buildingsmart.es/bim/openbim/faq/
