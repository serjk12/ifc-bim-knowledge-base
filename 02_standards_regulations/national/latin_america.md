# Latin America: BIM/IFC requirements

## In plain words

Latin America has no single BIM rule. Each country sets its own policy, and the pace is uneven. Brazil has a federal decree that makes BIM mandatory in phases. Chile's public programme Planbim publishes a BIM standard for public projects. Peru runs a "Plan BIM" tied to public investment. Colombia's rules come mostly from industry (Camacol "BIM Forum" and its BIM Kit) and a national strategy. Most mandates require "BIM" and "open formats", and say little about IFC itself: typically a deliverable "in IFC" plus a BIM Execution Plan (BEP/PEB), with details left to each owner's contract annex. For an MCP tester this means: IFC files from the region are usually exported from Revit, ArchiCAD or local structural tools; they are Spanish- or Portuguese-labelled (names, property values, classification); they are georeferenced against SIRGAS-based coordinate systems; and they are checked against a contract annex, not a national IFC "profile".

Last researched: 2026-11-06

> **Research status warning.** This document was written under degraded research conditions. The web-search quota was exhausted before the first query, and many government sites (planalto.gov.br, gob.pe, buildingSMART technical pages) blocked or returned errors to the fetch tool. Only the facts with a [n] marker were read from a fetched page. Everything marked "(unverified)" comes from background knowledge or the task brief and must be re-checked against the official text before it is used to grade an answer. No standard numbers, dates or URLs were invented; where a detail could not be confirmed it is flagged. See "Gaps".

---

## 1. Country snapshot

| Country | Main actor(s) | Instrument | What is mandated / recommended | Confidence |
|---|---|---|---|---|
| Chile | Planbim (public BIM programme; its web footer says "una iniciativa de ..." but the sponsor name was cut off in the fetch) [1][2]; Minvu; MOP (unverified) | Estándar BIM para Proyectos Públicos (Planbim) (unverified: version/year) | Standard for public projects; Planbim worked with the housing ministry Minvu on BIM implementation, reported 6 Sep 2022 [5] | Medium for existence; low for details |
| Brazil | Federal government (MDIC/ABDI, unverified) | Decreto 9.983/2019, Decreto 10.306/2020 (unverified: text not retrievable) | Phased BIM in federal works (see 2.2) | Medium |
| Peru | MEF (Ministerio de Economía y Finanzas) (unverified) | DS 289-2019-EF; Plan BIM Perú; Guía Nacional BIM (names from the task brief) | Progressive BIM in public investment (unverified: thresholds, dates) | Low-medium |
| Colombia | Camacol BIM Forum [8][9]; national strategy led by government bodies (unverified) | BIM Kit (Camacol) [9]; Estrategia Nacional BIM (unverified) | BIM Kit is a verified, public set of documents; national mandate details unverified | Medium for BIM Kit |
| Mexico | CMIC and others (unverified) | "Estrategia MIC" (MIC = Modelado de Información de la Construcción) (unverified) | No verified federal mandate | Low |
| Argentina, Uruguay, Costa Rica, Ecuador, Panama, Dominican Republic | Various ministries, professional colleges (e.g. CFIA in Costa Rica) | Strategies and roadmaps of varying status | Not verified; the CFIA homepage fetched in this research [10] showed no BIM content on its front page | Low |
| Regional | Red BIM de Gobiernos Latinoamericanos ("Red BIM Gob Latam"), supported by the IDB/BID | Annual "encuentros"; the Planbim site refers to the 11th meeting [1]; joint BID-Planbim guide for BIM pilots in the public sector, announced 7 Dec 2022 [3] | Knowledge exchange, not a legal mandate | Medium |

## 2. Country detail

### 2.1 Chile: Planbim

- Planbim is the public-sector BIM programme in Chile. Its site (planbim.cl) offers articles, a free e-learning course (new versions announced) and project news [1].
- Verified items on the site: an article on IFC and its updates "IFC 4.3 e IFC 4.4" dated 2022-10-17 (body text not retrievable) [2]; the BID + Planbim "guía para la implementación de pilotos con BIM en el sector público", 7 Dec 2022 [3]; a Red BIM Gob Latam seminar on Chilean BIM progress, 7 Dec 2022 [4]; completion of Planbim's work to implement BIM in Minvu, 6 Sep 2022 [5]; a meeting with Spain's Ministry of Transport, Mobility and Urban Agenda [1].
- The "Estándar BIM para Proyectos Públicos" is named in the task brief. A direct fetch of planbim.cl/estandar-bim/ and planbim.cl/estandar/ returned 404, so the exact version, year and IFC clauses are unverified. Background knowledge (unverified): the standard is organised as a main document plus annexes (BIM uses, roles, BEP, LOD/level-of-information definitions, deliverables) and asks for native files plus IFC exports.
- Chile classification: unverified. Do not assume a national classification table; tests should ask the model's own `ClassificationReference` values.
- Related regulation: Planbim publishes content about the OGUC (Ordenanza General de Urbanismo y Construcciones) as the normative backbone of Chilean construction [1]; BIM is not a substitute for permit requirements.

### 2.2 Brazil: federal decrees and ABNT

All items in this subsection are unverified: planalto.gov.br returned an "access denied" page to the fetch tool, and the Portuguese Wikipedia page fetched did not mention these decrees.

- **Decreto 9.983 of 22 Aug 2019**: "Estratégia Nacional de Disseminação do Building Information Modelling" (known as Estratégia BIM BR). Creates a governance committee (Comitê Gestor) and objectives. (unverified)
- **Decreto 10.306 of 2 Apr 2020**: sets the use of BIM in direct and indirect construction and engineering works by federal bodies, in three phases. As recalled (unverified): phase 1 from Jan 2021 (architecture and engineering design of new works and major refurbishments), phase 2 from Jan 2024 (extends to execution), phase 3 from Jan 2028 (extends to management and maintenance after delivery). It was reported as applying to works of the Ministry of Defence and of the Ministry of Infrastructure first. Always confirm dates and scope against the Diário Oficial text.
- **Lei 14.133/2021** (new procurement law) allows BIM preference in tenders (unverified).
- **ABNT NBR 15965** is the Brazilian construction-information classification (multi-part standard; commonly cited parts cover terminology, objects, processes, resources, results, units/spaces, construction information). (unverified: part titles and years)
- **ABNT NBR ISO 19650** parts 1 and 2 are the Portuguese-language adoption of ISO 19650 (unverified: year).
- **State "cadernos BIM"** exist in several states (examples recalled: Santa Catarina, Paraná, Minas Gerais, São Paulo's housing/works bodies) (all unverified, no URLs retrieved).
- A Portuguese Wikipedia page fetched in this research states that a 2017 decree by President Temer created a strategic committee to implement BIM at federal level, and that a national BIM dissemination strategy was due in May 2018 [6]. That reflects a Wikipedia summary, not the primary decree; the 2019 and 2020 decrees above supersede it.

### 2.3 Peru: Plan BIM Perú

Everything here comes from the task brief or memory (unverified). The gob.pe and mef.gob.pe pages returned HTTP 418 or empty content.

- Legal basis named in the brief: **Decreto Supremo 289-2019-EF**, adopting provisions for a progressive incorporation of BIM into public investment (the Peru "Plan BIM" is run by the MEF and linked to the Invierte.pe investment system, as recalled).
- **Guía Nacional BIM** is the national guidance document for the plan (name from the brief; year and version unverified).
- Thresholds and the date from which BIM becomes mandatory by investment size: unverified. Do not quote numbers without checking the DS text.

### 2.4 Colombia

- **Camacol BIM Forum** is an industry initiative for the digital transformation of construction. It lists member tiers (Élite, Consultor, Fundador, Empresa) and states a vision to become "referente nacional y autoridad técnica" for BIM [8]. The page also lists activities such as supporting the national BIM policy through an adoption strategy [8].
- **BIM Kit** (verified list of documents) [9]:
  - Vol. 1: Roles y Perfiles BIM; Modelado BIM; Flujos de trabajo; Gestión de la Información BIM; Indicadores BIM; Creación de contenido; Anexo Contractual.
  - Vol. 2: Hoja de Ruta para la Implementación BIM; Usos BIM; Requerimientos BIM para Trámites de Licencia; Plan de Implementación BIM (BEP); roadmaps for the "Solicitante" and for the "Curaduría o autoridad competente".
  - Vol. 3 (ISO 19650-style information management documents): Evaluación de capacidad y competencia (CCA); Matriz detallada de responsabilidades (MDR); Plan de ejecución BIM precontractual (PREBEP); Plan de movilización BIM; Planes de entrega (MIDP-TIDP); OIR; AIR; PIR; EIR; Glosario; Anexo Técnico BIM; Infraestructura Vial.
  - The page as fetched did not mention IFC, LOD or LOIN; IFC requirements inside these documents are therefore unverified [9].
- Interesting for testers: "Requerimientos BIM para Trámites de Licencia" shows a licence-application (curaduría) workflow where models are submitted for permit review [9].
- National strategy ("Estrategia Nacional BIM", period and owning agency) is unverified.

### 2.5 Mexico, Argentina, Uruguay, Costa Rica, Ecuador, Panama, Dominican Republic

No primary source was successfully read for these. They are listed so a test generator knows the names exist; treat every claim as unverified.

- Mexico: "Estrategia MIC" per the task brief; no verified mandate. Common acronym is MIC (Modelado de Información de la Construcción) rather than BIM.
- Argentina: national and provincial BIM initiatives and professional-college groups exist (unverified).
- Uruguay, Ecuador, Panama, Dominican Republic: public-works ministries have pilots or roadmaps (unverified).
- Costa Rica: the CFIA (Colegio Federado de Ingenieros y de Arquitectos) is the professional body; the front page fetched had no BIM content [10]. Costa Rica BIM strategy details are unverified.

### 2.6 Regional network

- **Red BIM de Gobiernos Latinoamericanos (Red BIM Gob Latam)**: the Planbim site refers to its "11vo encuentro" [1] and to a seminar with Planbim [4]. A BID (IDB) guide for BIM pilots in the public sector was published jointly with Planbim [3]. Membership list and founding year: unverified.
- The EU BIM Task Group's Latin American counterpart is the above network (unverified, background recollection).

## 3. IFC in the region: what is actually asked

### 3.1 What IFC is, as of today

- IFC is an ISO standard, ISO 16739-1:2024 for IFC4.3 ADD2 [7]. IFC versions timeline per Wikipedia: IFC2x3 (Feb 2006), IFC4 (Mar 2013), IFC4 Add1 (2015), IFC4 Add2 (2016), IFC4 Add2 TC1 (2017), IFC4.1 and IFC4.2 (withdrawn per that page), IFC4.3 Add2 (2024) [7].
- A Spanish Wikipedia page states IFC4 was published as ISO 16739 [11].
- buildingSMART GitHub hosts IFC4.x-development, IDS (Information Delivery Specification, XML), bSDD (data dictionary), validate (IFC Validation Service) and IFC5-development [12].

### 3.2 Typical requirements in LatAm BIM documents (pattern-level, unverified per country)

| Topic | Typical text in a Latin American BIM annex | What a test can check in the IFC |
|---|---|---|
| Version / MVD | "IFC 2x3 Coordination View 2.0" or "IFC4 Reference View" or "IFC4 Design Transfer View" | `FILE_SCHEMA(('IFC2X3'))` or `('IFC4')` in the STEP header; MVD stated in `FILE_DESCRIPTION` |
| Classification | National table (Brazil: NBR 15965) or Uniclass/Omniclass copy | `IfcClassificationReference` attached via `IfcRelAssociatesClassification` |
| Property sets | Standard `Pset_*Common` plus custom "Pset_<Owner>" with Spanish/Portuguese names | e.g. `Pset_WallCommon.IsExternal`, `FireRating`, `LoadBearing`; custom Pset names in Spanish |
| Georeferencing | Project location in a national CRS | IFC4 `IfcMapConversion` + `IfcProjectedCRS` (Name e.g. "EPSG:xxxx"); IFC2x3 uses `IfcSite` lat/long and a note |
| Naming | File naming per ISO 19650 style; level and discipline codes in Spanish/Portuguese | `IfcProject.Name`, `IfcBuildingStorey.Name` (e.g. "Nivel 1", "Pavimento Térreo") |
| Delivery / check | Native plus IFC; model checking in Solibri or similar; clash reports in BCF | BCF topics, IFC validation, IDS if the owner is advanced |

CRS notes (general geodesy knowledge, unverified for each national rule): Colombia uses MAGNA-SIRGAS "Origen Nacional" (EPSG:9377); Brazil uses SIRGAS 2000 (EPSG:4674) and SIRGAS 2000 / UTM zones (EPSG:31978-31985 for zones 18S-25S); Chile and Peru use SIRGAS/WGS84 UTM zones (Peru mostly UTM 18S/17S/19S). Check each EPSG code with the owner before testing.

## 4. Tools, templates and portals

- **Autodesk Revit** is dominant in Latin America (unverified claim of market share). Revit exports IFC via **File > Export > IFC**; the open-source IFC exporter is maintained by Autodesk on GitHub (unverified link). Revit is available in Spanish and Brazilian Portuguese, with different category names (see terminology).
- **Graphisoft ArchiCAD**, **Tekla**, **Bentley**, and **Solibri** (checking) are used (unverified).
- **Local software (unverified, names from background knowledge)**: Brazil: AltoQi (Eberick/Builder), TQS (structural, with IFC export), Orçafascio and Sienge (cost/management); these are examples to look up, not verified claims.
- **Templates**: Camacol BIM Kit documents (see 2.4) are the best verified public template set [9]. Planbim provides standard documents and free e-learning [1].
- **Submission portals**: Peru Invierte.pe (unverified link to BIM); Brazil federal contracting through Compras.gov.br (unverified); Chile "Mercado Público" (unverified). Colombia licence submission is mediated by curadurías, with "Requerimientos BIM para Trámites de Licencia" in the BIM Kit [9].
- **Open-source / enthusiasts**: IfcOpenShell and the Blender-based BIM add-on are the main open IFC toolchain worldwide; Latin American community projects were not verified in this research. YouTube and blogs in Spanish/Portuguese on "Revit a IFC" exist but none were fetched.

## 5. Key organisations

| Organisation | Role | Status |
|---|---|---|
| Planbim (Chile) | Public BIM programme | Verified site [1] |
| Camacol BIM Forum (Colombia) | Industry BIM forum | Verified [8] |
| Red BIM Gob Latam | Government network | Referenced [1][4] |
| BID (IDB) | Co-author of BIM pilot guide with Planbim | Verified title [3] |
| buildingSMART | Standards owner; Latin chapters exist (Spanish-language chapter, Brazil) | Chapters page returned 403; unverified |
| ABNT (Brazil), INN (Chile), ICONTEC (Colombia), INACAL (Peru) | National standards bodies (ISO 19650 adoption) | Unverified |
| CFIA (Costa Rica) | Professional college | Site seen [10] |

## 6. Local terminology table

| Native term | Transliteration / language | English |
|---|---|---|
| Modelado de Información de la Construcción (MIC) | Spanish | BIM |
| Modelagem da Informação da Construção (BIM) | Portuguese | BIM |
| Plan de Ejecución BIM (PEB / BEP) | Spanish | BIM Execution Plan |
| Plano de Execução BIM (PEB) | Portuguese | BIM Execution Plan |
| Requerimientos de intercambio de información (EIR) | Spanish | Exchange information requirements |
| Nivel de información necesario | Spanish | Level of information need (LOIN) |
| Nivel de desarrollo (LOD) | Spanish | Level of development |
| Muro / Parede | Sp. / Pt. | Wall (`IfcWall`) |
| Losa / Laje | Sp. / Pt. | Slab (`IfcSlab`) |
| Pilar (Pt.), Columna / Pilar (Sp.) | | Column (`IfcColumn`) |
| Viga | both | Beam (`IfcBeam`) |
| Nivel / Pavimento | Sp. / Pt. | Storey (`IfcBuildingStorey`) |
| Curaduría | Spanish (Colombia) | Licensing/permit authority |
| Caderno BIM | Portuguese | State BIM guide ("BIM notebook") |
| Estrategia BIM BR | Portuguese | Brazilian federal BIM strategy |
| Inversión pública | Spanish (Peru) | Public investment |
| Proyecto público | Spanish | Public project |

Note: "forjado" is the term in Spain; Latin America uses "losa". Tests should check that the MCP server tolerates Spanish/Portuguese names with accents (ñ, ç, ã, é) in IFC strings. IFC STEP encodes non-ASCII characters with `\X2\...\X0\` or `\X\xx` sequences, a common source of bugs.

## Typical questions people ask about this

All are illustrative unless a link is given.

1. (illustrative) "¿Qué versión de IFC exige el Estándar BIM de Planbim para proyectos públicos?"
2. (illustrative) "¿Desde cuándo es obligatorio BIM en las inversiones públicas del Perú?"
3. (illustrative) "Qual versão de IFC o Decreto 10.306 exige?" (the decree speaks of BIM generally; the IFC choice is in contract annexes)
4. (illustrative) "How do I georeference an IFC model for Colombia's Origen Nacional (EPSG:9377)?"
5. (illustrative) "¿Cómo exporto IFC4 desde Revit en español?" (File > Export > IFC)
6. (illustrative) "Which Revit categories must be exported to IFC for a curaduría licence submission?"
7. (illustrative) "How do I check an IFC against the BIM Kit 'Anexo Técnico BIM'?"
8. (illustrative) "Como classificar elementos IFC conforme a ABNT NBR 15965?"
9. (illustrative) "List all IfcWall with Pset_WallCommon.IsExternal = true in this model" (MCP query)
10. (illustrative) "Change the Name of all IfcBuildingStorey to 'Nivel 1', 'Nivel 2' ..." (MCP edit)
11. (illustrative) "¿Qué es la Red BIM de Gobiernos Latinoamericanos y quién participa?" (partial answer in [1][4])
12. (illustrative) "What is the BID guide for BIM pilots in the public sector?" (title and date in [3])
13. (illustrative) "¿Dónde descargo el BIM Kit de Camacol?" (BIM Forum page [8], kit page [9])
14. (illustrative) "Is IFC4.3 accepted by LatAm owners, or only IFC2x3?" (honest answer: IFC2x3/IFC4 are far more common; IFC4.3 is ISO 16739-1:2024 [7])
15. (illustrative) "¿Cómo valido un archivo IFC antes de entregarlo?" (buildingSMART validation service is on GitHub [12])

Real forum questions with links could not be collected because search was unavailable.

## Common pitfalls and misconceptions

- "The decree requires IFC." Mandates generally require BIM and often open formats; the IFC schema/MVD is stated in project documents, not necessarily in the law (unverified per country).
- Mixing up Spain and Latin America: UNE/BEDEC/"forjado" terminology and Spanish "BIM Commission" rules do not apply to Latin American projects.
- IFC4.1 and IFC4.2 are withdrawn per the Wikipedia version list [7]; do not assume they are valid deliverables.
- Non-ASCII text in IFC strings must be encoded; a naive writer corrupts "Piso técnico", "Edificação", "Ñuñoa".
- Using the wrong coordinate system: SIRGAS vs WGS84 differences are small but national CRS codes differ by country.
- Treating Wikipedia as a legal source: the Portuguese Wikipedia snippet on Brazil BIM [6] summarises older events and does not cite the 2019/2020 decrees.
- Colombia: the Camacol BIM Kit is an industry document, not a statute [8][9].

## Gaps

- The web-search quota was exhausted at the start, so no real forum questions, no national classification tables (Chile, Peru, Colombia, Mexico) and no GitHub/enthusiast projects from Latin America were verified.
- Blocked or failing pages: planalto.gov.br (access denied), in.gov.br (socket hang up), gob.pe and mef.gob.pe (HTTP 418), buildingsmart.org chapters and technical pages (403), gov.br/mdic BIM pages (404), redbimgoblatam.org (empty), planbim.cl/estandar* (404), abdi.com.br (403), camacol Ruta BIM (404).
- No suspicious, pirated or cracked-software sites were encountered.
- Needs follow-up: exact Planbim standard version and IFC clauses; text of Decretos 9.983/2019 and 10.306/2020; DS 289-2019-EF text and Guía Nacional BIM; Colombia's national BIM strategy document; Mexico "Estrategia MIC"; Argentina, Uruguay, Costa Rica, Ecuador, Panama and Dominican Republic status; buildingSMART Latin chapters.

## Sources

[1] Planbim home page - https://planbim.cl/
[2] Planbim, "IFC y sus actualizaciones IFC 4.3 e IFC 4.4" (2022-10-17; body not retrievable) - https://planbim.cl/ifc-y-actualizaciones/
[3] Planbim, BID + Planbim guide for BIM pilots in the public sector (7 Dec 2022) - https://planbim.cl/guia-bim-pilotos-bid-planbim/
[4] Planbim, seminar Red BIM Gob Latam and BIM progress in Chile (7 Dec 2022) - https://planbim.cl/seminario-redbimgoblatam-avances-chile/
[5] Planbim, end of work for BIM in Minvu (6 Sep 2022) - https://planbim.cl/termino-trabajo-planbim-minvu/
[6] Portuguese Wikipedia, BIM (Brazil snippet) - https://pt.wikipedia.org/wiki/BIM [7] English Wikipedia, Industry Foundation Classes - https://en.wikipedia.org/wiki/Industry_Foundation_Classes
[8] Camacol, BIM Forum Colombia - https://www.camacol.co/productividad-sectorial/digitalizacion/bim-forum
[9] Camacol, BIM Kit - https://www.camacol.co/productividad-sectorial/digitalizacion/bim-forum/bim-kit
[10] CFIA Costa Rica home - http://cfia.or.cr/
[11] Spanish Wikipedia, Industry Foundation Classes - https://es.wikipedia.org/wiki/Industry_Foundation_Classes
[12] buildingSMART on GitHub - https://github.com/buildingSMART
