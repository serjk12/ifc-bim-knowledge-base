# Spanish: how people ask about IFC, BIM and Revit

**Last researched: 2026-11-06** · Covers Spain and Latin America (Chile, Peru, Colombia, Mexico, Argentina and others). Language code `es`.

## In plain words

IFC is the open file format that lets a model made in one BIM program (Revit, Archicad, Allplan) be opened in another program or checked by a tool. Spanish speakers mostly meet IFC in three situations: (1) they export from Revit or Archicad and something is wrong (elements come out as "proxy", custom properties are missing, coordinates are lost); (2) a public client asks for IFC (Plan BIM in Spain, Planbim in Chile, Plan BIM Peru) and they need to know what to deliver; (3) they need numbers out of the model (quantities for a budget, room areas, lists of elements without data). When a Spanish speaker types to an AI assistant connected to an IFC file, the request is almost always short, lowercase, task-like ("dame...", "revisa...", "lista...") and assumes the file is already loaded.

## How much data is behind this page (read first)

| Fact | Value |
|---|---|
| Spanish records in the KB | 100 (33 real, 67 synthetic) |
| Genuine user-voiced posts among the "real" records | 7 distinct posts (one thread is stored twice) |
| README example prompts from Spanish-language MCP tools | 2 |
| Real records that are documents, news or vendor help (the "question" is a topic label, not a person's words) | 23 |
| Synthetic prompts | 67, all written by research agents, not sampled from users |

The web-search budget ran out during research, so the Spanish user voice is **under-sampled**. Both Spanish cells say so in their gaps sections ([es-spain](../../research_raw/wave1/es/es-spain.md), [es-latam](../../research_raw/wave1/es/es-latam.md)). The quota of 50-90 real examples could not be met honestly: this page lists every real Spanish record that exists (32 distinct entries) plus 26 English-language real threads that were collected for the Spanish cells, and labels each by evidence level. Where something below comes from general knowledge rather than the data, it is marked **(GK)**.

Evidence levels used in the tables:

| Tag | Meaning |
|---|---|
| **A** | A person's own post, issue or forum thread, in Spanish |
| **B** | A prompt written by developers as an example in an MCP tool README (real text, but a demo, not a support question) |
| **C** | Official, vendor, news or educational document; the "question" column is the research agent's topic summary |
| **D** | English-language real post found while researching Spanish-speaking communities (poster language not always known) |
| page / snippet | Whether the research agent read the page text or only a search-result snippet |

## Where people ask

| Place | What is there | Evidence and access notes |
|---|---|---|
| Autodesk Forums (Revit, Spanish-language forum "Revit - ACC - Navisworks") | The one Spanish forum thread found: "Problemas con IFC's" (2021). A Spanish-forum attachment "Exportar IFC.pdf" explains IFC formats. The research found far more English-language IFC export threads than Spanish ones (group D below), but the posters' nationality is unknown. | Pages returned HTTP 403 to the fetch tool, so content is from search snippets. |
| buildingSMART International forums | A thread in Spanish about exporting a structural Revit model to ETABS via IFC (2020, polite and formal, thesis context). The buildingSMART Spain chapter also posts there (in English). | Read. Thread had no resolution. |
| GitHub issues | Spanish-language issues exist even in international repos (IfcOpenShell: geometry "loss" in Bonsai Viewer) and in small local repos (ingetrazo, calculadora-RIC). Spanish MCP tools (archicad-mcp, RevitMCPBOQ) publish Spanish example prompts in their READMEs. | Read. |
| OSArch community | A Spanish post sharing a BlenderBIM clash detection video tutorial (2020). The Spanish category was reported as "largely spam". | Read one post. |
| Trade and training portals (not Q&A) | Espacio BIM, e-zigurat, BIMnD, construible.es, interempresas, esmartcity, OBCP. They answer questions like "what is IFC", "10 tips for a good IFC from Revit", "what does the Plan BIM require". | Read or snippet. Useful for how the profession talks, not for user phrasing. |
| Government and programme portals | Planbim (Chile), MEF Plan BIM Peru, MinVivienda (Colombia), Comisión Interministerial BIM (Spain), Junta Consultiva (Hacienda). | Several PDFs were not machine-readable. |
| Vendor help | Graphisoft Archicad 28 Spanish help, Trimble Access Spanish help, Arkance (Autodesk reseller) KB. | Read. |
| **Not reached** | Reddit, YouTube comments, Telegram and Facebook groups, bimcommunity.com, CYPE forums, es.BIM, Spanish Archicad community, Mexican/Argentine/Colombian blogs. | Search budget exhausted. Do not assume anything about activity there. |

Practical consequence: Spanish speakers appear in the data mostly **writing English** on international forums, or **writing very short Spanish** in issue trackers. Long, detailed Spanish support posts were not observed.

## Top themes (ranked)

Ranking combines the two research reports with topic counts over the 100 Spanish records (`national_requirements` 18, `psets_properties` 11, `quantities_qto` 9, `class_mapping` 9, `export_revit` 8, `mep_systems` 7, `coordinates_georef` 7). Note that the counts are inflated by synthetic prompts and by documents about national plans.

| # | Theme | What the person actually wants | Related KB doc |
|---|---|---|---|
| 1 | Elements exported as **proxy** (IfcBuildingElementProxy), class mapping, `IFCExportAs` | Make families come out as walls, columns, pumps, not as generic proxies | [revit_export_and_class_mapping](../by_topic/revit_export_and_class_mapping.md) |
| 2 | Parameters and property sets missing after export (shared parameters, type vs instance, mapping txt, Revit 2027 new mapping UI) | Keep custom data as Psets | [properties_and_parameters](../by_topic/properties_and_parameters.md) |
| 3 | National requirements: Plan BIM Spain, Planbim Chile (Fichas IFC, MIDE), Plan BIM Peru, BIM Colombia | Know what to deliver in IFC and check it | [regulations_permits_contracts](../by_topic/regulations_permits_contracts.md) |
| 4 | Coordinates and origin: IFC opens "very far from origin", coordinates lost when re-saved, models do not overlap | Correct shared coordinates, ETRS89 UTM30N (Spain) or SIRGAS-based systems (LatAm) | [coordinates_georef_units_levels](../by_topic/coordinates_georef_units_levels.md) |
| 5 | Quantities for budgets: **mediciones** / **metrados** / **cómputos** | Wall, slab, column quantities per level, in m2 and m3, for a budget (Presto BC3 in Spain) | [quantities_cost_schedule](../by_topic/quantities_cost_schedule.md) |
| 6 | Round trips between programs: Archicad to Revit (windows outside walls in Revit 2025-2027), Allplan colours lost, Revit to ETABS error | Know why data or geometry is lost | [import_and_interoperability](../by_topic/import_and_interoperability.md) |
| 7 | Validation: required properties, classification coverage, GlobalId stability, comparing versions | "Which elements are missing X?" lists | [validation_ids_model_checking](../by_topic/validation_ids_model_checking.md) |
| 8 | Big or broken files and viewers ("pesa 800mb", normals flipped, normals look like lost geometry) | Open, lighten, or understand a file | [file_size_viewing_conversion](../by_topic/file_size_viewing_conversion.md) |
| 9 | MEP: systems, ducts without system, crossings with beams, sleeves (pasamuros) | Coordination lists, BCF | [mep_structural_rebar](../by_topic/mep_structural_rebar.md) |
| 10 | Learning and tool finding: free viewers (BIMvision), CYPE IFC Builder, whether a small app can import IFC | "Can I...", "what is..." | [community_projects_and_enthusiasts](../../04_open_source/community_projects_and_enthusiasts.md) |

## Local ecosystem

Short version. Full detail and uncertainty flags are in [latin_america.md](../../02_standards_regulations/national/latin_america.md) and [spain_portugal_italy.md](../../02_standards_regulations/national/spain_portugal_italy.md).

**Spain**
- Comisión Interministerial BIM (CIBIM, Ministerio de Transportes): per the research cell, the Plan BIM was approved by the Consejo de Ministros on 27 June 2023, with rollout from April 2024 for high-value public contracts (a threshold of 5,538,000 EUR was reported) through 2030, using five BIM levels ([news](https://www.esmartcity.es/2023/06/30/plan-bim-incorporara-metodologia-bim-contratos-publicos-construccion), [trade article](https://www.interempresas.net/ObrasPublicas/565188-BIM-la-tecnologia-capaz-de-revolucionar-la-Ingenieria-del-Terreno.html)). The national KB document could not confirm a single hard national mandate, so treat exact thresholds as **to check**.
- buildingSMART Spain publishes the **Manual de Entrega de IFC (MEI) Edificación** plus an IDS file, and the classification **GuBIMClass** is named in it (see [spain_portugal_italy.md](../../02_standards_regulations/national/spain_portugal_italy.md)). Name collision to remember: in Chile "MEI" is a different thing (a model review manual); same acronym, different document.
- Standard: UNE-EN ISO 16739 (IFC). Software: CYPE (IFC Builder, BIMserver.center), Datacomp BIMvision (free viewer, see [Espacio BIM](https://www.espaciobim.com/bimvision)), Presto (cost estimating; BC3 files), Archicad, Allplan, Tricalc, Solibri.
- Educators and portals: Espacio BIM, e-zigurat, BIMnD, Arkance, construible.es.

**Latin America**
- Chile: Planbim (https://planbim.cl/) with "Fichas de Entidades IFC", the **MIDE** matrix (maps each parameter to an IFC attribute, Pset and property, with required/optional and automatic/manual export), the **MEI** manual for model review, and free e-learning.
- Peru: MEF Plan BIM Peru, Guía Nacional BIM, NTP-ISO 19650; a 2026 MEF training deck says application is mandatory in public investment (date reported as around August 2026, **unverified**).
- Colombia: MinVivienda BIM portal and the Camacol BIM Forum "BIM Kit" (includes licence-application requirements). Mexico uses the term MIC. Argentina: no usable data.
- Regional: Red BIM de Gobiernos Latinoamericanos; a CAF study cited by El Peruano counts 14 of 15 countries with a private-sector BIM initiative and 9 with a public one.
- Georeferencing: SIRGAS-based systems, ETRS89 in Spain (the prompts mention ETRS89 UTM 30N, EPSG 25830). Check the owner's EPSG code. **(GK for SIRGAS; ETRS89 appears in synthetic prompts)**
- Tools and small projects: Revit (dominant, **GK**), Archicad IFC Manager, Trimble Access (IFC for stakeout; not on Android per Trimble help), Bonsai/IfcOpenShell, ingelibre/ingetrazo (exports IFC but cannot import yet), calculadora-RIC (planned IFC export for the Chilean low-voltage regulation).
- Spanish-language MCP tools: [archicad-mcp by joacos](https://github.com/joacos/archicad-mcp) (rioplatense voseo), [RevitMCPBOQ](https://github.com/JefaturaBIM94/RevitMCPBOQ) (takeoff "corridas"). See [mcp_servers_and_ai_tools](../../04_open_source/mcp_servers_and_ai_tools.md).

**Local-language Revit gotcha.** Two English-language threads report that Revit IFC export produced an empty or no file after the Revit interface language was changed (one reproduced on a Spanish UI with exporter 23.4.0, fixed in later exporters). Test requests about "IFC export gives an empty file" with a localized Revit are realistic. Sources: [revit-ifc #718](https://github.com/Autodesk/revit-ifc/issues/718), [forum thread](https://forums.autodesk.com/t5/revit-architecture-forum/ifc-export-empty-file/m-p/8336603).

## How people write

### Register, length, structure

- **Very short.** One line to three lines. Real examples: "quisiera saber si será posible importar archivos IFC?" (one line, no context); "problemas con los ifc: al abrirlo y guardarlo en otro formato se pierden las coordenadas que traia".
- **No version, no steps.** Revit/IFC version and export settings are usually omitted (in the whole Spanish set, only the IFC2x3 geometry issue and the ETABS thesis post give an IFC version).
- **Polite and formal exceptions.** Students, researchers and some issue reporters open with "Buenas tardes", "¡Hola!", "Hola ... Que tengan un buen día", add thanks, and offer to send the file. This is the register of someone writing to a forum of strangers.
- **Imperative when talking to a tool.** README prompts and synthetic prompts use bare imperatives: "dame", "revisa", "lista", "compara", "pásame", "ponle", "agrúpame", "sácame", "mira a ver" (Spain), "creá" (Argentina, voseo; seen only in the archicad-mcp README).
- **No greeting, no closing** when addressing an assistant. Urgency appears as a reason: "para el presupuesto de mañana", "antes de la coordinación", "es para mi tarea de la uni".
- **Fragments as symptoms:** "se pierden las coordenadas", "no abre", "sale como proxy", "pesa 800mb", "se cuelga el visor".
- **Tone.** Mostly neutral. Frustration shows in the Archicad-to-Revit regression ("en el 2024 andaba bien, qué onda") and "lejísimos del origen" prompts. Anger is rare; confusion is common.

### Jargon and slang

| Term | Meaning | Standard / IFC term | Evidence |
|---|---|---|---|
| proxy, proxys, "sale como proxy" | element exported as a generic placeholder | IfcBuildingElementProxy | data (reports and prompts) |
| ifc, IFC's | the file; the apostrophe plural is an English habit | IFC | data (thread title "Problemas con IFC's") |
| pset | property set | Pset / IfcPropertySet | data |
| nativo | the original authoring file (rvt, pln) | native file | data (es-latam report) |
| mediciones (Spain) | quantity takeoff for a budget | Qto / quantity take-off | data (prompts), glossary |
| metrados (Peru, Chile) | same | Qto | data (es-latam report) |
| cómputo | same | Qto | data (es-latam report) |
| corrida | one takeoff run (MCP tool jargon) | takeoff run | data (RevitMCPBOQ README) |
| cuantía(s) | an amount or quantity value; in the prompt "falta algun cuantia" it means a missing quantity (in structural work "cuantía" also means reinforcement ratio) | quantity value | data (synthetic prompt), **GK** for the second meaning |
| plantas (Spain) / niveles, pisos (LatAm) | storeys | IfcBuildingStorey / Revit Level | data (prompts and reports) |
| cota | elevation of a storey | Elevation | data |
| ambientes (LatAm) / estancias, locales, espacios (Spain) | rooms | IfcSpace / Revit Room | data (es-latam report); "estancias" in a Spain prompt |
| forjado (Spain) / losa | floor slab | IfcSlab | data (prompts use both) |
| hormigón (Spain) / concreto | concrete | material name | "hormigón" in prompts; "concreto" **GK** |
| hueco, abertura, vano | opening in a wall | IfcOpeningElement | "hueco" in prompt; others **GK** |
| pasamuros | sleeve through a wall or slab | provision for void | data (Spanish prompt) |
| muro cortina, baranda, escalera, zócalo, vierteaguas | curtain wall, railing, stair, skirting, window sill | IfcCurtainWall, IfcRailing, IfcStair, IfcMember/IfcCovering | data (prompts) |
| ductos / conductos | air ducts (ductos in LatAm prompts, conductos in Spain prompts) | IfcDuctSegment | data |
| interferencias (Spain) / colisiones, clash | clashes | clash detection | data |
| pliego, licitación, licencia de obras | tender specs, tender, building permit | EIR source, procurement | data (Spain prompts) |
| CTE | Spain's technical building code | national regulation | data (one prompt) |
| BC3 | Spanish construction-price exchange format used by Presto | cost file | data (one prompt); detail **GK** |
| MIDE, MEI, Fichas IFC | Chilean Planbim documents (information matrix, review manual, IFC entity sheets) | national requirement | data |
| SIG | GIS | GIS | data (prompt) |
| "qué onda" | Mexican informal "what's up with this" | filler | data (es-latam report) |
| uni | university | context | data (prompt) |

### Misspellings, name variants, code-switching

- Missing accents: "Exportacion", "Descripcion", "conductos que no esten en ningun sistema", "tuberia" (prompts and the calculadora-RIC issue). Accents are often dropped when the text is typed fast or in an issue template.
- Typos and caps: "SOPOTARÁ ARCHIVOS IFC?" (all caps and a letter swapped).
- Chat abbreviations: "q" for "que" ("revisa q todos los elementos tengan codigo uniclass"). It appears in one synthetic prompt only; other shortcuts are plausible but not observed.
- Program names lowercase and without version: "revit", "etabs", "archicad", "ifcopenshell". Versions are given as years when given at all: "revit 2025", "la 2024".
- English terms stay English: Pset, proxy, clash detection, export, IfcExportAs, IFCExportType, Bonsai, add-on, BCF, Qto, GlobalId, IfcBuildingElementProxy. Class names are typed in English exactly ("IfcColumn", "IfcStair"), even in otherwise Spanish sentences.
- Mixed sentences are normal: "cuantos IfcBuildingElementProxy hay en el ifc y de que categorias de revit vienen?"
- On English forums, posters whose first language may be Spanish write short English with typos ("Quesion: IFC mapping, dissappearing objects in export"; the poster's language is not confirmed).

### What context is given, what is left out

| Usually given | Usually missing |
|---|---|
| The program ("revit", "archicad", "etabs") | Revit and exporter version, export setup, IFC schema/MVD |
| The symptom ("se pierden las coordenadas") | Steps to reproduce, screenshot, file |
| The reason or deadline ("para el presupuesto", "para la licitación") | The exact requirement text (pliego, EIR) the person must meet |
| A discipline hint ("sanitaria y estructura", "ductos nivel 2") | Names of IFC properties; people say "el fuego del muro", not `Pset_WallCommon.FireRating` |

When the person does name an IFC property, it is usually a developer or a coordinator who has already looked at the file: "Pset_WallCommon con FireRating y LoadBearing", "IfcExportAs".

## Real questions

### A. People's own posts (Spanish)

| ID | Original (title or paraphrase, Spanish) | English gloss | Persona | Evidence | Source |
|---|---|---|---|---|---|
| es-spain-r001 | "Problemas con IFC's": problemas con los ifc: al abrirlo y guardarlo en otro formato se pierden las coordenadas que traia | IFC problems: opening and re-saving in another format loses the coordinates it carried. Workarounds in the answer: check coordinates after each conversion, link the IFC instead of re-saving, or go via a Navisworks NWD / new project link. | architect, 2021 | A, snippet | [Autodesk forum](https://forums.autodesk.com/t5/revit-architecture-forum/problemas-con-ifc-s/td-p/10189111) |
| es-latam-r001 | "SOPOTARÁ ARCHIVOS IFC?": quisiera saber si será posible importar archivos IFC? | Will the app be able to import IFC files? (Answer: it exports IFC but cannot import yet; a PR was in progress.) | student_beginner, 2026 | A, page | [ingetrazo #1033](https://github.com/ingelibre/ingetrazo/issues/1033) |
| es-latam-r002 | "Pérdida de la geometría de los objetos": al abrir un archivo IFC (2x3) se pierde parte de la información geométrica; adjunto captura en Bonsai y Bonsai Viewer, puedo enviar el archivo | Opening an IFC2x3 file loses part of the geometry; screenshots from Bonsai and Bonsai Viewer attached. (Answer: flipped face normals, not lost geometry; recalculate normals and re-export.) | other, 2026 | A, page | [IfcOpenShell #8131](https://github.com/IfcOpenShell/IfcOpenShell/issues/8131) |
| es-latam-r003 | "Exportacion BIM: DXF/IFC para Revit y AutoCAD": mapeo de conductores calculados a entidades, generar IFC con propiedades eléctricas, endpoint export/ifc | Feature request (developer checklist): export electrical calculation results as DXF/IFC with electrical Psets. | mep_engineer, 2026 | A, page | [calculadora-RIC #10](https://github.com/jmarinderko/calculadora-RIC/issues/10) |
| es-err-r038 / es-bsmart-r007 (same thread, two records) | "Como poder exportar un modelo 3D estructural realizado en Revit a ETABS por medio del formato IFC?": formal, "Buenas tardes", step-by-step; ETABS says it could not find ENDSEC at end of file; exported IFC2x3; asks how to change the grid export option | How to export a structural Revit model to ETABS via IFC? Import error "Could not find ENDSEC", grids marked not exported. Answerers asked for schema, encoding, truncation; no resolution. | structural_engineer (thesis researcher), 2020 | A, page | [buildingSMART forum](https://forums.buildingsmart.org/t/como-poder-exportar-un-modelo-3d-estructural-realizado-en-revit-a-etabs-por-medio-del-formato-ifc/2985) |
| p-student-r035 | "Cómo detectar colisiones con BlenderBIM (IFC Clash Detection)": ¡Hola! Les comparto un tutorial en video para detectar colisiones entre elementos de archivos IFC con BlenderBIM. | Sharing a video tutorial on IFC clash detection with BlenderBIM. Replies are thanks. | student_beginner, 2020 | A, page | [OSArch](https://community.osarch.org/discussion/312/como-detectar-colisiones-con-blenderbim-ifc-clash-detection) |
| es-bsi-gis-r011 | RFI: Urban and Land Management think-tank (written in English by the buildingSMART Spain chapter) | Chapter asks for international groups working on land models via IFC or CityGML. Answer: German openBIM landscape group and the new BIM & GIS Integration group. | reviewer_authority, 2023 | A, page | [buildingSMART forum](https://forums.buildingsmart.org/t/rfi-urban-and-land-management-think-tank-room-group/4754) |

### B. Prompts shown in Spanish MCP tool READMEs

| ID | Original | English gloss | Persona | Evidence | Source |
|---|---|---|---|---|---|
| es-aimcp-r031 | "Creá cuatro muros de 3 m de alto formando un rectángulo de 5 × 4 m" (also "qué elementos tengo seleccionados en Archicad") | Create four 3 m walls forming a 5 x 4 m rectangle in Archicad. README notes: undo cannot be grouped, 120 s timeout. Rioplatense voseo ("Creá"). | architect, 2026 | B, page | [archicad-mcp](https://github.com/joacos/archicad-mcp) |
| es-aimcp-r032 | "Ejecuta la corrida 5 HVAC sobre mi selección actual en modo detalle." | Run takeoff run 5 (HVAC) on the current selection in detail mode; show ducts and fittings with size, length, area, gauge and kilos. Imperative; "corrida" is the tool's jargon. | estimator_qs, 2026 | B, page | [RevitMCPBOQ](https://github.com/JefaturaBIM94/RevitMCPBOQ) |

### C. Documents and articles (the "question" is a topic, not a person's words)

| ID | Title / what it covers | Gloss | Evidence | Source |
|---|---|---|---|---|
| es-latam-r011 | Fichas de Entidades IFC - Planbim | Chile: IFC entities required per model (architecture, volumetric, site, electrical MEP). | C, snippet | [planbim.cl](https://planbim.cl/documentos/fichas-ifc/) |
| es-latam-r012 | Matriz de Información de Entidades (MIDE) - Planbim | Chile: v3.0 maps parameter to IFC attribute, Pset, property; required/optional; automatic or "a ingresar". | C, snippet | [planbim.cl](https://planbim.cl/documentos/mide/) |
| es-latam-r013 | IFC y sus actualizaciones IFC 4.3 e IFC 4.4 | Planbim article (17 Oct 2022); headline only. | C, page | [planbim.cl](https://planbim.cl/ifc-y-actualizaciones/) |
| es-latam-r014 | Evaluación de la aplicabilidad del estándar nacional BIM de PlanBIM en un edificio público | Chilean civil-engineering thesis (2020) applying the standard and the MEI review. | C, page | [U. de Chile](https://repositorio.uchile.cl/handle/2250/179170) |
| es-latam-r015 | Capacitación MEF 2026 - Plan BIM Perú | MEF training deck: mandatory BIM in public investment, Guía Nacional BIM, NTP-ISO 19650 (date unverified). | C, snippet | [MEF](https://www.mef.gob.pe/contenidos/inv_publica/docs/capacitaciones/2026/20260317.pdf) |
| es-latam-r016 | Plan BIM Perú (documento MEF) | Policy document for progressive BIM adoption. | C, snippet | [MEF](https://www.mef.gob.pe/planbimperu/docs/planBIMpE.pdf) |
| es-latam-r017 | Avance de la implementación del Building Information Modeling en América Latina | El Peruano, CAF study of 15 countries; no mention of IFC. | C, page | [El Peruano](https://www.elperuano.pe/noticia/213920-avance-de-la-implementacion-del-building-information-modeling-en-america-latina) |
| es-latam-r018 | Trabajar con IFC (Ayuda Archicad 28) | Graphisoft Spanish help: IFC2x3 and IFC4, "Gestor IFC", traductores, filtros de modelo. | C, page | [Graphisoft](https://help.graphisoft.com/AC/28/SPA/_AC28_Help/121_IFC/121_IFC-1.htm) |
| es-latam-r019 | Modelos BIM e IFC (Trimble Access) | IFC for stakeout and COGO, layers from presentation layers, not on Android. | C, page | [Trimble](https://help.fieldsystems.trimble.com/trimble-access/2021.20/es/Map-files-BIM-and-IFC.htm) |
| es-latam-r020 | 10 licencias (bim.minvivienda.gov.co) | Colombia: BIM document about licences; IFC content unverified. | C, snippet | [MinVivienda](https://bim.minvivienda.gov.co/sites/default/files/doc-bim-2022-09/10_licencias_.pdf) |
| es-spain-r016 | Using IFC files with a Shared Coordinates system (Arkance, Spanish version) | A linked or opened IFC in Revit gives no coordinate-system choice; workaround steps. | C, snippet | [Arkance](https://emea.support.arkance.world/hc/es/articles/36464850969234-Using-IFC-files-with-a-Shared-Coordinates-system) |
| es-spain-r017 | IFC o Industry Foundation Classes, ¿qué es IFC? | Build your own mapping file (class per Revit category), then Exportar > IFC; some data still lost. | C, page | [Espacio BIM](https://www.espaciobim.com/ifc) |
| es-spain-r018 | BIMvision, de Datacomp | Free IFC viewer overview; plugins paid. | C, page | [Espacio BIM](https://www.espaciobim.com/bimvision) |
| es-spain-r019 | IFC Builder, de CYPE | Free tool to create IFC; imports from Allplan/Archicad/Revit. | C, page | [Espacio BIM](https://www.espaciobim.com/ifc-builder) |
| es-spain-r020 | IFC e interoperabilidad en BIM (e-zigurat) | Revit-to-Archicad exchange can lose information; test each case. | C, page | [e-zigurat](https://www.e-zigurat.com/es/blog/ifc-e-interoperabilidad-en-bim/) |
| es-spain-r021 | 10 Consejos Para Exportar un buen IFC con REVIT (BIMnD) | Default templates lack IFC parameters; avoid in-situ and nested families; levels should be building floors only. | C, snippet | [BIMnD](https://www.bimnd.es/blog/10-consejos-para-exportar-un-buen-ifc-con-revit/) |
| es-spain-r022 | Mitma aprueba la propuesta de Plan de implantación BIM... | News: commission approved the plan proposal; guide, BIM standard and observatory in preparation. | C, page | [construible](https://www.construible.es/2023/05/02/mitma-aprueba-propuesta-plan-implantacion-bim-contratacion-publica) |
| es-spain-r023 | El Plan BIM incorporará la metodología BIM en los contratos públicos | Five levels, from April 2024 to 2030. | C, page | [esmartcity](https://www.esmartcity.es/2023/06/30/plan-bim-incorporara-metodologia-bim-contratos-publicos-construccion) |
| es-spain-r024 | BIM, la tecnología capaz de revolucionar la Ingeniería del Terreno | Threshold 5,538,000 EUR; plan active since 1 April. | C, page | [interempresas](https://www.interempresas.net/ObrasPublicas/565188-BIM-la-tecnologia-capaz-de-revolucionar-la-Ingenieria-del-Terreno.html) |
| es-spain-r025 | Ayudas para la formación BIM aplicada a la contratación pública | Grants to professional associations (BOE 28 July 2023). | C, page | [construible](https://www.construible.es/2023/08/02/ayudas-para-la-formacion-bim-aplicada-a-la-contratacion-publica-para-los-colegios-profesionales) |
| es-spain-r026 | Informe 2023-23 Junta Consultiva - MTMAU BIM | Official report on the draft plan; PDF unreadable. | C, snippet | [Hacienda](https://www.hacienda.gob.es/DGPatrimonio/Junta%20Consultiva/informes/informes2023/2023-23-MTMAU-BIM.pdf) |
| es-spain-r028 | La implementación de la metodología BIM en la contratación pública | Opinion piece from a procurement observatory. | C, snippet | [OBCP](https://obcp.es/opiniones/la-implementacion-de-la-metodologia-bim-en-la-contratacion-publica) |
| es-spain-r029 | Exportar IFC.pdf (foro Autodesk ES) | Spanish IFC primer: .ifc, ifcXML, ifcZIP, versions, free viewers. | C, page | [Autodesk forum attachment](https://forums.autodesk.com/autodesk/attachments/autodesk/revit-acc-navisworks-forum-es/19931/1/Exportar%20IFC.pdf) |

### D. English-language real threads gathered for the Spanish cells

These are in English. Several clearly come from Spanish-speaking regions, but for most the poster's native language is unknown. They are the best evidence of **what** Spanish-speaking Revit users get stuck on. Spanish-speaker posters are noted where the research said so.

| Title (verbatim) | Persona | Note | Source |
|---|---|---|---|
| Quesion: IFC mapping, dissappearing objects in export | bim_coordinator | escalator family (generic model, proxy class) missing in export | [forum](https://forums.autodesk.com/t5/revit-architecture-forum/quesion-ifc-mapping-dissappearing-objects-in-export/td-p/7181576) |
| Mapping of Revit Parameters to IFC Parameters for Export | bim_coordinator | wants IFC class and properties per family; uses IFCExportAs | [forum](https://forums.autodesk.com/t5/revit-architecture-forum/mapping-of-revit-parameters-to-ifc-parameters-for-export/td-p/7638232) |
| IFC Parameters IFCExportAs and IFCExportType not outputting to IFC file | bim_coordinator | still proxy after setting the parameters | [forum](https://forums.autodesk.com/t5/revit-architecture-forum/ifc-parameters-ifcexportas-and-ifcexporttype-not-outputting-to/td-p/7511389) |
| Issues with exporting type parameters from Revit to IFC | bim_coordinator | type parameters missing in Psets | [forum](https://forums.autodesk.com/t5/revit-architecture-forum/issues-with-exporting-type-parameters-from-revit-to-ifc/td-p/14004505) |
| IFC export - Pset - only type parameters exporting | bim_coordinator | custom Pset only carries type parameters | [forum](https://forums.autodesk.com/t5/revit-architecture-forum/ifc-export-pset-only-type-parameters-exporting/td-p/9555287) |
| Revit IFC Export user defined properties won't export | bim_coordinator | shared parameter file pointed to; nothing exported | [forum](https://forums.autodesk.com/t5/revit-architecture-forum/revit-ifc-export-user-defined-properties-won-t-export/td-p/9767878) |
| Ifc export in 2027 - mapping parameters severely lacking | bim_manager | new graphical mapping replaces pset.txt; empty lists for some classes | [forum](https://forums.autodesk.com/t5/revit-architecture-forum/ifc-export-in-2027-mapping-parameters-severely-lacking/td-p/14229702) |
| Missing properties when exporting IFC from Revit using custom property set mapping TXT file | bim_coordinator | properties absent in output | [forum](https://forums.autodesk.com/t5/revit-architecture-forum/missing-properties-when-exporting-ifc-from-revit-using-custom/td-p/13217311) |
| PSet parameters | bim_coordinator | reply advises avoiding proxy | [forum](https://forums.autodesk.com/t5/revit-architecture-forum/pset-parameters/td-p/9926144) |
| Steel connections - IFC exporter | structural_engineer | connections missing from IFC | [forum](https://forums.autodesk.com/t5/revit-structure-forum/steel-connections-ifc-exporter/td-p/10698321) |
| Missing parts when exporting from Revit to IFC via Naviate IFC | structural_engineer | parts missing | [forum](https://forums.autodesk.com/t5/revit-structure-forum/missing-parts-when-exporting-from-revit-to-ifc-via-naviate-ifc/td-p/7809342) |
| Solved: IFC Export Issue - Revit 2021 | architect | wrong output in Revit 2021 | [forum](https://forums.autodesk.com/t5/revit-architecture-forum/ifc-export-issue-revit-2021/td-p/9438686/page/2) |
| Solved: Structural Connections not exported via Document.Export (Revit 2018/Python) | developer_programmer | API export omits connections | [forum](https://forums.autodesk.com/t5/revit-api-forum/structural-connections-not-exported-via-document-export-revit/td-p/8253027) |
| IFC export/import Revit (Graphisoft community) | bim_coordinator | Base Point and Survey Point set, but imported model sits at Base Point | [forum](https://community.graphisoft.com:443/t5/Collaborate-forum/IFC-export-import-Revit/td-p/352151) |
| IFC EXPORT PROBLEM | architect | export fails, asks for help | [forum](https://forums.autodesk.com/t5/revit-architecture-forum/ifc-export-problem/m-p/11003278) |
| Couldn't able to export the IFC file | architect | cannot export | [forum](https://forums.autodesk.com/t5/revit-architecture-forum/couldn-t-able-to-export-the-ifc-file/m-p/11319947) |
| IFC export: empty file | bim_coordinator | cause traced to interface language change | [forum](https://forums.autodesk.com/t5/revit-architecture-forum/ifc-export-empty-file/m-p/8336603) |
| REVIT2023 - Fail export when change language. | bim_coordinator | Spanish-speaking reporter, terse; reproduced on a Spanish UI | [GitHub](https://github.com/Autodesk/revit-ifc/issues/718) |
| REVIT 2026 Won't export to IFC? | bim_manager | duplicated exporters, mapped network drives mentioned | [forum](https://forums.autodesk.com/t5/revit-architecture-forum/revit-2026-won-t-export-to-ifc/m-p/13821992/highlight/true) |
| Issues exporting IFC4x3: Unexpected errors occurred while exporting these elements | bim_coordinator | IFC4x3 export errors | [forum](https://forums.autodesk.com/t5/revit-architecture-forum/issues-exporting-ifc4x3-quot-unexpected-errors-occurred-while/m-p/13415457) |
| PR: 2D symbol/annotation causes doors and windows to be incorrectly positioned in the wall | architect | Archicad IFC into Revit: windows outside wall, fine in 2024, broken 2025-2027 | [GitHub](https://github.com/Autodesk/revit-ifc/issues/1018) |
| Windows positioned outside wall in 3D view on IFC import | architect | same regression | [GitHub](https://github.com/Autodesk/revit-ifc/issues/1019) |
| Rvt/IFC to 3D tiles | developer_programmer | Spanish-speaking poster writing English; wants command-line conversion | [Cesium](https://community.cesium.com/t/rvt-ifc-to-3d-tiles/42154) |
| Plan BIM (Spain) - European Commission public buyers community | reviewer_authority | English summary of Spain's Plan BIM (document) | [EC PDF](https://public-buyers-community.ec.europa.eu/system/files/2024-05/AIDA%20240322_GabSUB_DGGROWPPUnit_PlanBIM_en_v1_0.pdf) |
| Optimal settings for Ifc Export from Revit | bim_coordinator | settings list (vendor KB, document) | [dRofus](https://support.drofus.com/en/support/solutions/articles/16000118323-optimal-settings-for-ifc-export-from-revit) |

## Ready test prompts

All prompts below are **synthetic**: they were written by research agents, then lightly rewritten here for realism. None is a real quote. The "Src" column gives the record each one is based on. "File" means the request assumes an IFC (or open Revit/Archicad project) is loaded. Variants: **ES** = Spain wording, **LA** = Latin America, **AR** = rioplatense voseo, **neutral**.

Expected behavior is what a good MCP-connected assistant should do. General rules that apply to all: state which tool or data supported each number; say when a value is missing instead of guessing; never write to the model without saying so; keep GlobalIds in outputs that list elements.

### Inventory and model questions

| # | Prompt (synthetic) | Var. | Intent, difficulty, persona | Src | Expected behavior |
|---|---|---|---|---|---|
| 1 | oye, cuántos proxy tiene el ifc que me han pasado? y de qué categorías de revit vienen, tengo que corregir la tabla de mapeo | ES | query_model_data, medium, bim_coordinator, file | es-spain-s001 | Count IfcBuildingElementProxy, group by ObjectType or the Revit-category property, suggest IfcExportAs / mapping fixes. Do not reclassify anything. |
| 2 | cuántos elementos quedaron como proxy en el ifc? y de qué categorías de revit venían | LA | query_model_data, medium, bim_coordinator, file | es-latam-s001 | Same as 1; report counts per category and say if the category property is absent. |
| 3 | resumen rápido de qué trae este ifc: disciplinas, versión, cantidad de elementos por clase | neutral | query_model_data, easy, bim_coordinator, file | es-latam-s017 | Report schema (IFC2x3/IFC4), authoring app from the header, counts per class, storeys, obvious problems. |
| 4 | dime las plantas del modelo con su cota y cuantos elementos tiene cada una | ES | query_model_data, easy, bim_coordinator, file | es-spain-s006 | List IfcBuildingStorey with Elevation and contained element counts. State units. |
| 5 | lista los niveles con su cota y cuántos elementos tiene cada uno, y dime cuáles no están asignados a ningún nivel | LA | query_model_data, easy, bim_coordinator, file | es-latam-s005, es-coord-s009 | As 4, plus elements with no spatial containment in a storey, by class. |
| 6 | dime qué elementos del IFC no están asignados a ningún nivel o planta, necesito corregirlos antes de la coordinación | neutral | validate_check, medium, bim_coordinator, file | es-coord-s009 | Find products without containment in a storey, group by class, offer a list with GlobalIds. |
| 7 | el ifc de topografía viene en metros o milímetros? y tiene georreferencia? las coordenadas están muy lejos del origen? | LA | query_model_data, medium, civil_infra_engineer, file | es-latam-s007 | Read the unit assignment, IfcMapConversion / site placement; report units, offset from origin, and whether a CRS exists (IFC2x3 has none in the same form). |
| 8 | dame todos los espacios con nombre y area, por planta, es para el plan de mantenimiento | ES | query_model_data, easy, facility_manager, file | en-fmor-s016 | List IfcSpace with Name, area and storey; flag spaces without area. |
| 9 | dame la superficie total por tipo de estancia | ES | query_model_data, easy, architect, file | es-spain-s016 | Sum area of IfcSpace grouped by Name or LongName; say which area attribute was used (net or gross). |
| 10 | qué sistemas de tuberías hay en el modelo y cuáles tubos no están conectados a ningún sistema? | LA | query_model_data, medium, mep_engineer, file | es-latam-s012 | List systems and members; find pipe segments with no system. Explain if systems were not exported at all. |
| 11 | hay conductos que no esten en ningun sistema? sacame la lista | ES | query_model_data, medium, mep_engineer, file | es-spain-s010 | Find duct segments not assigned to a system; list with GlobalId, name, storey. |
| 12 | dame todos los dampers cortafuegos con planta y local, para el mantenimiento | ES | query_model_data, easy, facility_manager, file | es-cobie-s011 | Filter by class/type/name, report storey and containing space; note naming-based matching is fuzzy. |
| 13 | agrúpame los elementos por nivel y tipo para armar paquetes de obra, solo estructura | LA | query_model_data, medium, contractor_site, file | es-latam-s015 | Group structural classes by storey and type; table suitable for scheduling. |

### Quantities and data extraction

| # | Prompt (synthetic) | Var. | Intent, difficulty, persona | Src | Expected behavior |
|---|---|---|---|---|---|
| 14 | necesito los metrados de muros, losas y columnas por nivel, m2 y m3, para el presupuesto de mañana | LA | extract_quantities, medium, estimator_qs, file | es-latam-s003 | Read base quantity sets, group by storey; flag elements without quantities; say whether quantities came from Qto or computed geometry. |
| 15 | necesito mediciones de muros por planta en m2 y m3 para el presupuesto | ES | extract_quantities, medium, estimator_qs, file | es-spain-s007 | Same; mind net vs gross area (openings). |
| 16 | necesito las mediciones de losas y vigas por planta para el presupuesto, en m3 y m2, y avísame si falta alguna cuantía | ES | extract_quantities, medium, estimator_qs, file | es-s009 | Aggregate slab and beam volume/area per storey; list elements missing quantities. |
| 17 | dame el volumen de hormigón por planta, solo pilares y vigas | ES | extract_quantities, medium, structural_engineer, file | es-eng-s014 | Sum volume of columns and beams per storey; verify concrete via material association, do not assume. |
| 18 | dame el volumen por material de todos los muros, por capa, para el presupuesto | LA | extract_quantities, medium, contractor_site, file | mx-mcl-s017 | Per wall, layer thickness x area by material; total per material; note if layers are missing. |
| 19 | necesito las mediciones por capítulos (muros, forjados, carpintería) para pasarlas a presupuesto en bc3 | ES | extract_quantities, hard, estimator_qs, file | es-qto-s012 | Group into chapters, list quantities with units, offer CSV; state the limits of writing BC3 (do not claim a BC3 file was produced if the tool cannot). |
| 20 | dame los ductos por nivel con longitud, area y kilos, solo los de la selección | LA | extract_quantities, medium, estimator_qs, live Revit | es-aimcp-s015, es-aimcp-r032 | Use the current selection only; group by level; report the method for weight (direct, geometric estimate or factor). |
| 21 | como saco el area neta de todos los muros con ifcopenshell en python? me da None | neutral | how_to, medium, developer_programmer | es-latam-s013 | Explain psets/qtos retrieval and why None appears (no Qto set in file); show a geometry-based fallback. |
| 22 | como saco con ifcopenshell todas las propiedades de los muros a un excel? | ES | how_to, easy, developer_programmer | es-spain-s015 | Show property-set extraction and export with pandas; mention type vs occurrence properties. |

### Validation, requirements and comparisons

| # | Prompt (synthetic) | Var. | Intent, difficulty, persona | Src | Expected behavior |
|---|---|---|---|---|---|
| 23 | he exportado a ifc y no me salen los parametros compartidos en los psets, mira a ver cuales faltan en los muros | ES | validate_check, hard, bim_coordinator, file | es-spain-s002 | List Psets and properties on walls, compare with expected shared parameters, report missing ones and likely causes (export Revit property sets option, mapping txt, type vs instance). |
| 24 | revisa que todos los muros tengan FireRating y material asignado, dime los que no | neutral | validate_check, easy, reviewer_authority, file | es-latam-s011 | Check the fire-rating property and material association on walls; list offenders. |
| 25 | revisa que todos los muros tengan Pset_WallCommon con FireRating y LoadBearing llenos, lista los vacios | neutral | validate_check, easy, bim_coordinator, file | es-psets-s017 | Distinguish "property absent" from "present but empty". |
| 26 | revisa si el modelo cumple la MIDE de planbim, qué entidades no traen sus propiedades requeridas | LA (Chile) | validate_check, hard, reviewer_authority, file | es-latam-s002 | Needs the list of required entities and properties; if not supplied, ask for it or say it cannot access Planbim documents. Report missing properties per entity with counts. |
| 27 | tengo que entregar el modelo para una licitacion con Plan BIM, revisa que el IFC tenga todas las plantas, espacios y clasificacion en cada elemento | ES | validate_check, hard, bim_manager, file | es-spain-s003 | Check storeys, spaces and classification references; list gaps; say the exact requirement is in the pliego / EIR and do not invent it. |
| 28 | revisa q todos los elementos tengan codigo uniclass, dime cuales no | neutral | validate_check, medium, bim_manager, file | es-classbsdd-s011 | List elements without a classification reference, counts by class; confirm which classification system the references use. |
| 29 | que porcentaje de elementos tiene clasificación (uniclass o gtc)? y sácame un csv por nivel para el dashboard | ES | validate_check, medium, bim_manager, file | es-spain-s017, es-data-s010 | Compute coverage by class and level; CSV output; do not claim "gtc" is a known system if unrecognised, ask. |
| 30 | para la entrega a mantenimiento, comprueba que los equipos tengan marca, modelo y numero de serie | ES | validate_check, medium, facility_manager, file | es-spain-s011 | Check manufacturer-type properties on equipment; list blanks. |
| 31 | revisa si los espacios tienen superficie y uso asignado para el CTE | ES | comply_regulation, medium, reviewer_authority, file | es-spain-s013 | List spaces with area and usage, flag missing; make clear that CTE compliance itself is not decided by the assistant. |
| 32 | compara el ifc de hoy con el de la semana pasada, qué elementos nuevos, borrados y movidos | LA | compare_versions, hard, bim_coordinator, file | es-latam-s009 | Match by GlobalId; list added, removed, changed by class; warn if GlobalIds were regenerated. |
| 33 | revisa si los GlobalId de estos 50 elementos siguen iguales entre la v3 y la v4 del modelo | neutral | query_model_data, easy, bim_coordinator, file | es-guid-s009 | Look up each id in both files; report present, missing, changed. |
| 34 | revisa si el ifc trae el sistema de coordenadas (ETRS89 UTM 30N, EPSG 25830) bien puesto, que lo voy a cargar en el SIG | ES | validate_check, medium, civil_infra_engineer, file | es-gis-s012 | Read CRS name/EPSG and map conversion; compare with 25830; report mismatch. |
| 35 | puedes validar este IFC de carretera contra el esquema 4.3 y decirme los errores principales | neutral | validate_check, medium, reviewer_authority, file | es-infra-s011 | Run schema and basic rule checks, group errors by type; mention the buildingSMART validation service for full rules. |

### Edits (writes)

| # | Prompt (synthetic) | Var. | Intent, difficulty, persona | Src | Expected behavior |
|---|---|---|---|---|---|
| 36 | los modelos genericos salen como proxy, pasalos a IfcColumn los que tengan 'pilar' en el nombre | ES | modify_model_data, medium, architect, file | es-spain-s004 | Select proxies by name, show the count, confirm before reclassifying; save as a new file; advise fixing IFCExportAs in Revit for a durable fix. |
| 37 | los zócalos y vierteaguas salen como proxy, cámbialos a IfcMember o IfcCovering segun el caso y dime cuales tocaste | ES | modify_model_data, medium, architect, file | es-proxy-s005 | Apply a stated rule per name pattern, list every changed element. |
| 38 | cuantos proxy hay colgando de muros cortina y sin psets? salen un monton de tipos proxy | ES | query_model_data, hard, bim_coordinator, file | es-proxy-s015 | Find proxies aggregated to curtain walls, report those without property sets. |
| 39 | agrégale a todas las luminarias la propiedad frecuencia_mantenimiento y que tome el valor del tipo | LA | modify_model_data, hard, facility_manager, file | es-latam-s008 | Create or update a custom Pset on luminaire occurrences, copy from type, save a new IFC, report count. |
| 40 | los materiales vienen con nombres raros, listame los distintos y unifica los de hormigon | ES | modify_model_data, medium, bim_coordinator, file | es-spain-s014 | List material names, propose normalised names, apply only after approval. |
| 41 | copia el area de cada espacio a un pset propio Pset_Area_Cliente, el cliente lo pide | ES | modify_model_data, medium, bim_coordinator, file | es-spaces-s013 | Create a custom Pset on each IfcSpace with the area value; report spaces without area. |
| 42 | ponle acero S275 a todas las vigas y pilares del modelo y mételo en un pset propio | ES | modify_model_data, medium, structural_engineer, file | es-struct-s010 | Confirm the counts before writing; create a custom property; do not overwrite existing material data. |
| 43 | renombra todas las vistas de planta con el nivel delante y crea una lámina por cada una, numeradas A-01, A-02... | neutral | automate_batch, medium, architect, live Revit | es-revit-auto-s014 | Rename plan views, create sheets with sequential numbers, place views, report conflicts. A Revit-side write: confirm scope first. |
| 44 | creá cuatro muros de 3 m en rectángulo 5x4 y después contame cuántos hay | AR | modify_model_data, easy, architect, live Archicad | es-aimcp-s016 | Create four walls, count them, avoid duplicates on retry (the real tool warns that undo is not grouped). |

### Troubleshooting

| # | Prompt (synthetic) | Var. | Intent, difficulty, persona | Src | Expected behavior |
|---|---|---|---|---|---|
| 45 | abro el ifc en revit y sale lejisimos del origen, no se ve nada. por que? | ES | troubleshoot_import, medium, architect, file | es-spain-s005 | Inspect site placement and map conversion, explain large coordinates, suggest a shared-coordinates workflow. |
| 46 | las ventanas no hacen hueco en el muro en el ifc, que pasa? | ES | troubleshoot_export, hard, bim_coordinator, file | es-spain-s012 | Check opening elements and void relationships; find walls with windows but no void; give causes. |
| 47 | importé el ifc de archicad en revit 2025 y las ventanas quedaron fuera del muro, en el 2024 andaba bien, qué onda | LA | troubleshoot_import, medium, architect | es-latam-s004 | Explain the known regression (see GitHub issues), offer to verify hosting and openings in the file so the problem is placed on the import side. |
| 48 | importe el IFC de Archicad en Revit y se perdieron los colores, revisa si los estilos de superficie estan en el archivo | LA | validate_check, medium, architect, file | mx-mcl-s004 | Check surface styles on shapes and materials; report whether the data exists in the file. |
| 49 | el ifc pesa 800mb y no abre, se cuelga el visor, qué hago | LA | troubleshoot_viewing, easy, structural_engineer | es-latam-s010 | Suggest filtering by discipline or storey, a lighter viewer, integrity check, split export. |
| 50 | el ifc me pesa 600mb, puedes quitar los elementos 2D y las anotaciones y decirme cuanto baja? | ES | optimize_performance, medium, architect, file | es-fs-s009 | Detect annotations, 2D items and proxies, remove in a copy, report resulting size and counts. |
| 51 | la escalera y la baranda salen raras en el ifc, la baranda flotando. puedes revisar la geometria de las IfcStair y IfcRailing? | ES | troubleshoot_viewing, hard, architect, file | es-geom-s009 | Compare placements and bounding boxes, detect offsets or missing representations. |
| 52 | el ifc que saque de revit no abre en etabs, dice que falta ENDSEC. que version es y esta truncado? | LA | troubleshoot_import, medium, structural_engineer, file | es-vm-s008 | Check schema, encoding and whether the file ends correctly; report cause and re-export advice. Based on the real buildingSMART thread. |
| 53 | exporté de revit a etabs por ifc y me sale error al importar, que config del exportador debo usar? | LA | troubleshoot_import, medium, structural_engineer | es-err-s007 | Explain structural export options and which IFC views fit analysis exchange; set expectations about analytical data in IFC. |
| 54 | dime los ductos que cruzan vigas en el nivel 2 y de que sistema son, para mandar el BCF | LA | coordinate_clash, hard, bim_coordinator, file | es-mep-s009 | Find intersecting duct and beam pairs on that storey, list with system, propose BCF topics. |
| 55 | revisa interferencias entre sanitaria y estructura en el ifc federado, quita duplicados y dime cuantas hay por planta | ES | coordinate_clash, medium, bim_coordinator, file | es-clash-s010 | Run interference check, deduplicate pairs, count by storey. |
| 56 | detecta colisiones entre la estructura y las instalaciones en este ifc, es para mi tarea de la uni | neutral | coordinate_clash, hard, student_beginner, file | p-student-s013 | Run structure vs MEP clash, report counts and top clashes, offer BCF, explain terms simply. |
| 57 | dame los pasamuros que faltan donde las tuberias cruzan muros y forjados | ES | validate_check, medium, bim_coordinator, file | es-openings-s014 | Detect MEP crossings without sleeves or openings, list by level. |

### How-to, concept and opinion questions (often no file)

| # | Prompt (synthetic) | Var. | Intent, difficulty, persona | Src | Expected behavior |
|---|---|---|---|---|---|
| 58 | como exporto a ifc desde revit para que las columnas no salgan como proxy? uso la 2024 | LA | how_to, easy, student_beginner | es-latam-s006 | Explain the mapping table and Export to IFC As on the family, with a short checklist. |
| 59 | que configuracion uso para exportar ifc desde revit para coordinacion, 2x3 o ifc4? | ES | how_to, easy, student_beginner | es-spain-s008 | Explain Coordination View 2.0 on IFC2x3 vs IFC4 Reference View, property sets, rooms as spaces; mention that the project requirements decide. |
| 60 | como paso este ifc a sketchup sin perder los grupos x categoria? | neutral | convert_format, medium, architect, file | es-viewconv-s007 | Explain import options and category grouping, caveats; or export geometry grouped by class. |
| 61 | en las licitaciones públicas piden ifc y nativo, vale la pena entregar solo ifc? | LA | request_opinion, easy, bim_manager | es-latam-s016 | Discuss IFC as an open deliverable and its limits; follow the contract's information requirements; do not invent local rules. |
| 62 | se puede presentar el IFC directamente para la licencia de obras o solo pdf? que tendria que revisar antes | ES | understand_concept, easy, architect | es-permit-s013 | Say it depends on the municipality and that IFC submission for permits is uncommon; list model checks worth running. |

## Tips for generating authentic Spanish prompts

**Do**
- Keep it short: one or two lines, no greeting, imperative verb first ("dame", "revisa", "lista", "compara").
- Name the **purpose or deadline** in a trailing clause: "para el presupuesto de mañana", "antes de la coordinación", "para la entrega a mantenimiento", "es para mi tarea de la uni".
- Use regional vocabulary consistently within one prompt: Spain (plantas, mediciones, forjado, estancias, hormigón, licitación, "mira a ver"), Latin America (niveles, metrados or cómputos, losa, ambientes, "qué onda" in Mexico), Argentina (voseo: "creá", "contame").
- Keep IFC class and program names in English and often lowercase for programs: "los proxy", "IfcColumn", "revit 2025", "ifcopenshell", "etabs".
- Drop accents or question marks sometimes; use "q" for "que" occasionally; allow plural apostrophes ("IFC's").
- Mix levels of knowledge: a coordinator says "proxy", "Pset_WallCommon", "GlobalId"; a student says "colisiones", "no abre"; an estimator never names an IFC class and asks for "mediciones".
- Ask for **lists of problems** ("dime cuáles no", "lista los vacíos") more than for explanations; this is the most frequent shape in the data.
- Include some requests that hit a limit: no file loaded, a requirement document the assistant cannot see (Plan BIM, MIDE, pliego), a bulk edit that needs confirmation.

**Don't**
- Don't write textbook Spanish ("Por favor, ¿podría usted indicarme...?") unless the persona is a formal researcher; real posts were either one-line or politely formal with "Buenas tardes" and thanks, nothing in between.
- Don't give full version numbers, export settings and file names in the first message; real people omit them.
- Don't translate IFC terms into Spanish ("elemento proxy de construcción"); people keep them in English.
- Don't mix Spain and Latin America words in the same message without a reason (for example "forjado" together with "metrados").
- Don't present these prompts as quotes from users, and don't invent national rules (thresholds, dates, article numbers) in the expected behavior: the KB marks them unverified.
- Don't assume Spanish speakers always write Spanish: on international forums they write short English, so a Spanish-speaking persona sometimes sends English with Spanish typos.

## Related KB documents

- [Latin America: BIM/IFC requirements](../../02_standards_regulations/national/latin_america.md) and [Spain, Portugal, Italy](../../02_standards_regulations/national/spain_portugal_italy.md)
- [Revit IFC export reference](../../03_software/revit/ifc_export_reference.md) and [IFC import/link reference](../../03_software/revit/ifc_import_link_reference.md)
- [Multilingual glossary](../../08_glossary/glossary_multilingual.md) (Spanish column, with Spanish Revit menu names)
- [Viewers, checkers, CDE, converters](../../03_software/viewers_checkers_cde_converters.md)
- [IFC basics: properties, quantities, Psets](../../01_ifc_basics/05_properties_quantities_psets.md)
- Other languages: [pt](pt.md), [fr](fr.md), [it](it.md)
