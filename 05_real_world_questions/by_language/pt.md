# Portuguese: how people ask about IFC, BIM and Revit

**Last researched: 2026-11-06** · Brazil (main) and Portugal. Language code `pt`.

## In plain words

IFC is the open file format used to pass a BIM model from one program to another. In Brazil the questions that matter for a test assistant are the everyday ones: a coordinator exports from Revit or Archicad and parts are lost; an estimator wants the *quantitativo* (quantity takeoff) for a budget; a contractor wants clashes (*incompatibilidades*) for the designers; a client's BIM requirements (EIR/BEP) must be checked before delivery. Portugal uses the same tools but different words (*ficheiro*, *piso*, *compartimento*, *mapa de quantidades*).

## How much data is behind this page (read first)

This is the **thinnest** of the language pages, and it says so on purpose.

| Fact | Value |
|---|---|
| Portuguese records in the KB | 29 (1 real, 28 synthetic) |
| Real Portuguese-language posts | **1** (a GitHub issue, 2025) |
| Real English-language posts by Portuguese speakers found in other cells | at least 1 (OSArch, bSDD / SICLIC) |
| Brazilian research cell | 0 real records. The web-search budget was exhausted, planalto.gov.br returned "Acesso Negado", a guessed AltoQi URL returned 404. See [pt-brazil report](../../research_raw/wave1/pt/pt-brazil.md). |
| Portugal | No research cell; only the national document, which is mostly unverified ([spain_portugal_italy.md](../../02_standards_regulations/national/spain_portugal_italy.md)). |

The requested 40-80 real examples **do not exist in the corpus**, and no examples were invented to fill the gap. Everything about "how people write" below comes from (a) the one real post and (b) synthetic prompts that research agents wrote from general knowledge. Treat it as a **hypothesis to be validated** with a second research pass (Brazilian forums, Reddit, YouTube comments, vendor forums, Telegram/WhatsApp groups). Items from general knowledge are marked **(GK)**.

## Where people ask

| Place | Evidence | Notes |
|---|---|---|
| GitHub issues of international tools | **Seen**: IfcOpenShell issue in Portuguese about a Bonsai import failure ([#7305](https://github.com/IfcOpenShell/IfcOpenShell/issues/7305)) | Numbered reproduction steps in Portuguese plus an error log. |
| OSArch community (English) | **Seen**: a Portuguese speaker writing English about adding the Brazilian SICLIC dictionary to bSDD ([thread](https://community.osarch.org/discussion/3680/bsdd-dictionaries)); the student-persona report also mentions Brazilian engineering educators adopting BlenderBIM in an OSArch thread | Posters write English with local standard names (ABNT NBR 15965). |
| Revit / Dynamo / pyRevit forums (English) | **Seen only indirectly**: the en-dynamo-pyrevit report notes some posters with a Portuguese/Brazilian context writing English | No URLs recorded for these. |
| Brazilian forums, blogs, YouTube, vendor support (AltoQi, TQS, Autodesk Brasil), Facebook/Telegram/WhatsApp groups, Reddit | **Not reached** | Do not assume anything about activity or tone there. |
| Portugal (buildingSMART Portugal, CT 197, Facebook/LinkedIn groups) | **Not reached** | The national document lists them as leads only. |

## Top themes (ranked)

There is no measured ranking. The order below is the research agent's expectation from prior knowledge (flagged unverified in the report), cross-checked with how often a topic appears in the 28 synthetic prompts (`class_mapping` 5, `mep_systems` 3, `conversion_formats` 3, `quantities_qto` 3).

| # | Theme | Typical need | Related KB doc |
|---|---|---|---|
| 1 | Elements exported as **proxy** / class mapping (IfcExportAs stops working in Revit 2023; fittings and pumps as proxy) | Reclassify or fix the mapping | [revit_export_and_class_mapping](../by_topic/revit_export_and_class_mapping.md) |
| 2 | Parameters and Psets lost between programs; round trips Archicad to Revit | Know what disappeared | [properties_and_parameters](../by_topic/properties_and_parameters.md) |
| 3 | *Compatibilização* (clash coordination) and BCF between disciplines | Send issues to designers | [coordination_clash_bcf_cde](../by_topic/coordination_clash_bcf_cde.md) |
| 4 | *Quantitativo* for budgets (doors and windows by type and floor, rooms, slabs) | Tables for Excel | [quantities_cost_schedule](../by_topic/quantities_cost_schedule.md) |
| 5 | Client requirements: EIR/BEP, COBie fields, classification (SICLIC / NBR 15965) | Validation lists | [validation_ids_model_checking](../by_topic/validation_ids_model_checking.md) |
| 6 | Georeferencing in SIRGAS 2000 and models that do not overlap | Correct coordinates | [coordinates_georef_units_levels](../by_topic/coordinates_georef_units_levels.md) |
| 7 | IFC version and format choice: 2x3 vs 4, ifc vs ifczip vs ifcxml; delivering in 2x3 | Which to send | [versions_mvd_encoding_guid](../by_topic/versions_mvd_encoding_guid.md) |
| 8 | Heavy files and slow viewers | Find the heavy families | [file_size_viewing_conversion](../by_topic/file_size_viewing_conversion.md) |
| 9 | Accented characters (ç, ã, é) in IFC text | Files from Brazilian tools that do not open | [versions_mvd_encoding_guid](../by_topic/versions_mvd_encoding_guid.md) |
| 10 | Compliance for permits (*alvará*: building height, setbacks) | Quick checks from the model | [regulations_permits_contracts](../by_topic/regulations_permits_contracts.md) |

## Local ecosystem

Details and uncertainty flags: [latin_america.md](../../02_standards_regulations/national/latin_america.md) (Brazil) and [spain_portugal_italy.md](../../02_standards_regulations/national/spain_portugal_italy.md) (Portugal). Everything in the "Brazil" list below is **unverified**: the sources could not be fetched in this research.

**Brazil**
- Federal policy: Estratégia BIM BR and Decreto 10.306/2020 (BIM in federal works in phases); Decreto 9.983/2019. Dates and scope must be checked in the Diário Oficial.
- Standards: ABNT NBR 15965 (construction classification, whose BIM dictionary is called **SICLIC**; an OSArch thread confirms SICLIC exists as a bSDD dictionary), ABNT NBR ISO 19650 series. Cost reference: **SINAPI**.
- Software named in the reports: AltoQi (Eberick, QiBuilder), TQS (structural, IFC export), Autodesk Revit and Navisworks, Solibri, BIMcollab; cost/management tools Orçafascio and Sienge **(GK)**.
- Coordinate systems: SIRGAS 2000 (EPSG:4674) and SIRGAS 2000 / UTM zones (EPSG:31978-31985) per the national document, which flags them as general knowledge. One synthetic prompt cites EPSG 31983.
- State guides called *cadernos BIM* exist in several states (unverified).
- Open-source: Bonsai/IfcOpenShell is in use in Brazil (real issue in Portuguese; Brazilian educators in OSArch).

**Portugal**
- CT 197 (national BIM standardisation committee; coordinated by ONS/IST per buildingSMART Portugal), buildingSMART Portugal, *Guia de Contratação BIM* (published) and a *Plano de Execução BIM* guide (in development). No Portuguese BIM mandate or IFC delivery manual was confirmed. Public procurement code: Código dos Contratos Públicos (does it cite BIM? unverified).

## How people write

**Only one real sample exists.** The IfcOpenShell issue (Portuguese, 2025) uses numbered steps and pastes an error log; the reporter is a beginner on Ubuntu 24.04 who does not have the source software. Everything else in this section is **from synthetic prompts and general knowledge** and should be re-checked when real posts are available.

### Register, length, structure (hypothesis)

- Informal, lowercase, direct, usually **no greeting**. Typical length one line. The pt-brazil report says the same and flags it as illustrative.
- Brazilian chat features seen in the synthetic prompts: "pra", "tá/ta", "ai" ("lista ai"), "da pra", "n" for "não" ("coordenada compartilhada n funciona"), missing accents ("nao tem", "tubulacao", "tao" for "estão"), superlatives like "pesadissimo".
- Purpose clause at the end: "preciso pro 4D da obra", "preciso entregar pro cliente", "pra planilha da obra", "preciso pro alvará".
- Mixed English: "pset", "export", "clash", "BEP", "EIR", "proxy", "IfcExportAs", "BCF", "COBie", "Pset_WallCommon".

### Jargon and slang

| Term | Meaning | Standard / IFC term | Evidence |
|---|---|---|---|
| compatibilização | clash coordination between disciplines | clash detection / coordination | pt-brazil report (GK) |
| incompatibilidades | the clashes themselves | clashes | synthetic prompt |
| quantitativo | quantity takeoff | Qto | synthetic prompts, report |
| pavimento | storey (Brazil) | IfcBuildingStorey / Level | synthetic prompts, glossary |
| ambiente | room | IfcSpace / Revit Room | synthetic prompts, glossary |
| pilar, viga, laje, parede | column, beam, slab, wall | IfcColumn, IfcBeam, IfcSlab, IfcWall | synthetic prompts |
| furos, aberturas, shafts, prumadas | openings and vertical risers | IfcOpeningElement | synthetic prompt |
| tubulação, conexões, reduções | piping, fittings, reducers | IfcPipeSegment, IfcPipeFitting | synthetic prompts |
| cronograma, 4D | schedule | 4D | synthetic prompts |
| alvará, recuo | building permit, setback | permit check | synthetic prompt |
| SICLIC | Brazilian classification dictionary (NBR 15965) | classification | OSArch thread, synthetic prompt |
| SINAPI | Brazilian public cost reference | cost database | report (GK) |
| planilha | spreadsheet | Excel/CSV | synthetic prompts |
| parâmetro compartilhado | Revit shared parameter | shared parameter | glossary (Brazilian Revit term) |
| ficheiro, piso, compartimento, mapa de quantidades (Portugal) | file, storey, room, quantity takeoff | Portuguese (PT-PT) variants | **GK**, not in the corpus |

### Misspellings, name variants, code-switching (hypothesis)

- Program names lowercase and without version: "revit 2023", "tekla", "robot", "navisworks".
- Class names exactly as in English: "IfcExportAs", "IfcPump", "IfcPipeFitting", "TRANSITION".
- Brazilian vs European spelling: "compartilhado" (BR) vs "partilhado" (PT); "arquivo" (BR) vs "ficheiro" (PT). A prompt should not mix them.

### What context is given or omitted

From the synthetic set: the purpose and the target (client, designer, 4D schedule) is stated; the Revit year is sometimes given ("no revit 2023"); IFC schema rarely; no file names.

## Real questions

| ID | Original (title as posted / paraphrase) | English gloss | Persona | Evidence | Source |
|---|---|---|---|---|---|
| en-gh-encoding-r019 | "Falha de importação de arquivo IFC com Bonsai". The post has numbered steps in Portuguese and an error log. | IFC from Archstation does not open in Bonsai on Ubuntu 24.04, even after downgrading Blender. The file contains raw 0xE7 / 0xE3 bytes (ç, ã in Latin-1) instead of the `\X\` escapes IFC requires; the maintainers' analysis said it needs a policy decision on lenient decoding. Reporter has no access to the source software. Frustrated tone. | student_beginner, 2025 | A, page | [IfcOpenShell #7305](https://github.com/IfcOpenShell/IfcOpenShell/issues/7305) |
| (OSArch thread, English) | "bsDD Dictionaries": a Portuguese speaker writing English; manual entry did not work; the dictionary is registered on the bSDD site but in "Demo" mode; can I add the JSON file or a link? Thanks at the end. | How to add the Brazilian SICLIC (ABNT NBR 15965) dictionary to the bSDD list. Answer: activate it on the bSDD management page; confirmed working. | bim_manager, 2025 | D, page | [OSArch #3680](https://community.osarch.org/discussion/3680/bsdd-dictionaries) |

The reporter of #7305 is a good model for a "frustrated beginner whose Brazilian tool wrote an invalid IFC": accented characters in names from a Brazilian program are the likely cause of silent failures. See [versions_mvd_encoding_guid](../by_topic/versions_mvd_encoding_guid.md).

## Ready test prompts

All **synthetic**. The first 28 are rewritten from the research agents' prompts (Src = record id). Items 29-36 are **adapted** from Spanish records into Portuguese by the author of this page, to reach a usable set; they are not in the corpus and the Portuguese-from-Portugal ones (33-35) use PT-PT forms from general knowledge. Variants: **BR** = Brazil, **PT** = Portugal.

| # | Prompt (synthetic) | Var. | Intent, difficulty, persona | Src | Expected behavior |
|---|---|---|---|---|---|
| 1 | me dá a área de todos os ambientes por pavimento com o total, e exporta pra planilha | BR | extract_quantities, easy, estimator_qs, live Revit | pt-revit-auto-s015 | Group rooms by level, sum area, flag unplaced rooms, output a CSV/Excel file. |
| 2 | valida esse IFC contra a planilha de requisitos do EIR, preciso ver quais paredes estão sem classificação e sem Pset_WallCommon | BR | validate_check, medium, bim_coordinator, file | pt-coord-s010 | Check walls for classification reference and Pset_WallCommon; report. If the spreadsheet is not provided, ask for it. |
| 3 | quais elementos do pavimento 2 ainda não têm atividade no cronograma? preciso pro 4D da obra | BR | query_model_data, medium, contractor_site, file | pt-s010 | Find level-2 products with no task assignment, list by class. If there is no schedule data in the file, say so. |
| 4 | tem tubulação sem pavimento associado no modelo? lista aí | BR | validate_check, medium, mep_engineer, file | pt-eng-s015 | Find flow elements not contained in any storey. |
| 5 | qual a diferença entre IFC e openBIM? a norma brasileira exige IFC no trabalho da faculdade? | BR | understand_concept, easy, student_beginner | p-student-s014 | Explain IFC as a data schema vs openBIM as an approach; do not state what Brazilian norms require unless confirmed; say the client's requirements decide. |
| 6 | como mando as incompatibilidades em BCF pro arquiteto e ele consegue abrir no Revit com o elemento certo? | BR | how_to, easy, bim_coordinator | pt-clash-s011 | Explain BCF export, GUID matching, plugin round trip, status updates. |
| 7 | adiciona a classificação SICLIC nas paredes pelo nome do tipo, tabela que te passei | BR | modify_model_data, hard, bim_coordinator, file | pt-classbsdd-s012 | Create the classification, add references per wall type from the table, list unmatched types. Needs the table. |
| 8 | tem como ver quais elementos tão sem os campos obrigatórios do cobie? preciso entregar pro cliente | BR | validate_check, medium, bim_coordinator, file | pt-cobie-s012 | Validate required attributes for components, types and spaces; report missing by sheet. |
| 9 | como deixar o ifc georreferenciado em SIRGAS 2000 saindo do revit? coordenada compartilhada n funciona | BR | how_to, medium, architect | mul-coord-s012 | Explain shared coordinates, IFC4 map conversion with an EPSG code, and the limits of IFC2x3. |
| 10 | preciso da lista de equipamentos com tag, ambiente e fabricante pra entrega do FM, em planilha | BR | extract_quantities, medium, facility_manager, file | pt-data-s011 | List equipment with tag, containing space and manufacturer; flag missing manufacturer. |
| 11 | exportei pro IFC e sumiu um monte de elemento, dá pra ver o que ficou de fora e por quê? | BR | troubleshoot_export, hard, bim_coordinator, file | pt-err-s008 | Compare counts per class against expected categories; report missing categories and likely causes (filters, mapping). Cannot see the Revit file if only IFC is loaded: say so. |
| 12 | qual a diferença de tamanho entre ifc, ifczip e ifcxml? posso mandar o zip pro cliente? | BR | understand_concept, easy, student_beginner | pt-fs-s010 | Explain text vs XML vs compressed; ifcZIP is a valid delivery format; check the client's requirements. |
| 13 | o ifc tá pesadíssimo, quais famílias têm mais faces? o mobiliário deve ser | BR | optimize_performance, medium, bim_manager, file | pt-geom-s010 | Rank elements/types by triangle or face count; highlight furniture; suggest simplification. |
| 14 | como levo o ifc do revit pro qgis mantendo as coordenadas? tem que converter pra geopackage? | BR | convert_format, easy, architect | pt-gis-s013 | Explain georeferencing on export, converters, CRS and units checks. |
| 15 | o que mudou da revisão anterior pra essa? preciso saber quais elementos já estão no cronograma 4D e foram alterados | BR | compare_versions, hard, contractor_site, file | pt-guid-s010 | Diff revisions by GlobalId, intersect with scheduled elements, report. Warn if ids were regenerated. |
| 16 | qual o comprimento de cada eixo ferroviário no modelo? em km por favor | BR | extract_quantities, easy, civil_infra_engineer, file | pt-infra-s012 | Find alignments (IFC4.3), compute length, convert to km. |
| 17 | pinta todas as lajes de cinza claro no modelo, cria o estilo de superfície e liga no material | BR | modify_model_data, medium, bim_manager, file | mx-mcl-s005 | Create a surface style and assign it to the material or to the slabs; save a new file. |
| 18 | as conexões estão vindo como proxy, muda tudo pra IfcPipeFitting e põe o tipo TRANSITION nas reduções | BR | modify_model_data, hard, mep_engineer, file | pt-mep-s010 | Identify proxies named as fittings, change class, set the predefined type for size changes, report every change. |
| 19 | lista os furos nas lajes pra passagem de shafts e prumadas, tem algum sem abertura? | BR | coordinate_clash, medium, mep_engineer, file | pt-openings-s015 | Find vertical MEP elements crossing slabs with no opening element. |
| 20 | confere a altura total do edifício e o recuo do lote no ifc, preciso pro alvará | BR | validate_check, hard, architect, file | pt-permit-s015 | Compute building height from storeys; say that setback needs a site boundary the model may not have. Do not certify code compliance. |
| 21 | no revit 2023 o IfcExportAs parou de funcionar, tudo sai como proxy. qual parâmetro uso agora? | BR | how_to, easy, bim_manager, file | pt-proxy-s006 | Explain the built-in "Export to IFC As" and predefined type parameters that replaced the shared parameter; mention upgrade behavior. |
| 22 | tem uns proxy que são bombas, muda pra IfcPump com o type certo e predefined type | BR | modify_model_data, medium, bim_coordinator, file | pt-proxy-s017 | Reclassify to IfcPump with a type and predefined type; note abstract supertypes cannot be used. |
| 23 | preciso do quantitativo das portas e janelas por tipo e pavimento, com largura e altura | BR | extract_quantities, easy, estimator_qs, file | pt-qto-s014 | Count doors/windows by type and storey with width and height; table. |
| 24 | comparar os psets do ifc que saiu do archicad com o que voltou do revit, o que sumiu? | BR | compare_versions, hard, bim_manager, file | pt-roundtrip-s011 | Diff property sets per element; list lost, changed, added properties. |
| 25 | preciso rodar simulação energética, verifica se os ambientes estão fechados e têm limite de espaço | BR | validate_check, hard, mep_engineer, file | pt-spaces-s014 | Check space closedness and presence of boundaries; say what the IFC can and cannot prove. |
| 26 | como levar o modelo da estrutura metálica do Tekla pro Robot via IFC sem perder os perfis? | BR | convert_format, hard, structural_engineer | pt-struct-s011 | Explain profiles in IFC, limits for analysis transfer, alternatives; inspect profiles if a file is given. |
| 27 | quais entidades do meu modelo ifc4 não existem no ifc2x3? preciso entregar em 2x3 | BR | compare_versions, medium, bim_coordinator, file | pt-vm-s009 | List entity classes used in the file that are absent or renamed in IFC2x3, with counts and mapping suggestions. |
| 28 | exporta pra excel a lista de ambientes com área e nível, tô precisando pra planilha da obra | BR | convert_format, easy, bim_coordinator, file | pt-viewconv-s008 | Query spaces with area and storey, write an xlsx/CSV. |
| 29 | preciso do quantitativo de paredes, lajes e pilares por pavimento, em m² e m³, pro orçamento de amanhã. se faltar quantidade em algum elemento me avisa | BR | extract_quantities, medium, estimator_qs, file | adapted from es-latam-s003 | Group by storey, flag elements without quantities, say whether values come from quantity sets or geometry. If the user later asks for SINAPI prices, do not invent prices. |
| 30 | o ifc tá com 800mb e não abre no visualizador, trava tudo. como faço? | BR | troubleshoot_viewing, easy, structural_engineer | adapted from es-latam-s010 | Suggest filtering by discipline or storey, a lighter viewer, integrity check, split export. |
| 31 | quantos proxy tem no ifc e de quais categorias do revit eles vieram? | BR | query_model_data, medium, bim_coordinator, file | adapted from es-latam-s001 | Count proxies, group by category property, suggest mapping fixes. |
| 32 | lista os pavimentos com a cota e quantos elementos cada um tem, e quais elementos não estão em nenhum pavimento | BR | query_model_data, easy, bim_coordinator, file | adapted from es-latam-s005 | List storeys with elevation and counts; elements without containment. |
| 33 | diz-me quais os compartimentos sem área atribuída e lista-os por piso | PT | query_model_data, easy, architect, file | adapted from fr-fs / es spaces records | List spaces without area per storey. PT-PT wording (GK). |
| 34 | preciso do mapa de quantidades das paredes e lajes por piso, em m2 e m3, para o orçamento. avisa-me se faltarem quantidades | PT | extract_quantities, medium, estimator_qs, file | adapted from es-spain-s007 | As 29. PT-PT wording (GK). |
| 35 | o ficheiro IFC tem 700 MB e não abre. o que posso fazer? | PT | troubleshoot_viewing, easy, bim_coordinator | adapted from es-latam-s010 | As 30. PT-PT wording (GK). |
| 36 | exportei o IFC do Revit e os parâmetros compartilhados não aparecem nos Psets, vê quais faltam nas paredes | BR | validate_check, hard, bim_coordinator, file | adapted from es-spain-s002 | List Psets and properties on walls, compare with expected shared parameters, report causes (export option, mapping file, type vs instance). |

## Tips for generating authentic Portuguese prompts

**Do**
- Pick **one** variant per prompt: Brazil (*pavimento, ambiente, quantitativo, arquivo, compartilhado*) or Portugal (*piso, compartimento, mapa de quantidades, ficheiro, partilhado*).
- Keep it short and informal for Brazilian chat: "pra", "tá", "aí", "dá pra", drop a few accents, and end with the purpose ("pra entrega do FM", "pro alvará").
- Keep English technical words as they are: pset, proxy, clash, EIR, BEP, COBie, BCF, IfcExportAs, class names.
- Use local anchors: SICLIC / NBR 15965, SIRGAS 2000, SINAPI, *alvará*, *compatibilização*, AltoQi / TQS / Eberick.
- Include one or two **encoding** cases: names with ç, ã, é, õ, to test accent handling.
- Mix a few "no file loaded" or "needs a document you did not give" cases (EIR spreadsheet, SICLIC table, schedule).

**Don't**
- Don't invent Brazilian law or standard details in the expected behavior (Decreto dates, NBR part numbers, thresholds). The KB marks them unverified.
- Don't mix Brazilian and European Portuguese in one message.
- Don't present these prompts as quotes from real users: there is only one real Portuguese-language post in the corpus.
- Don't assume a Brazilian user writes long polite emails to an assistant; the only observed real sample is a structured issue by a beginner, and the rest is hypothesis.

## Gaps and next steps

- A research pass with working web search is needed: Autodesk Brasil forum, Reddit, YouTube comments, AltoQi/TQS support forums, Telegram/WhatsApp groups, Portuguese forums and buildingSMART Portugal.
- Verify the Brazilian decrees, NBR numbers and Portuguese CT 197 documents against primary sources.
- Replace synthetic prompts 29-36 with prompts derived from real Portuguese posts once available.

## Related KB documents

- [Latin America national requirements (Brazil section)](../../02_standards_regulations/national/latin_america.md), [Spain, Portugal, Italy](../../02_standards_regulations/national/spain_portugal_italy.md)
- [Revit IFC export reference](../../03_software/revit/ifc_export_reference.md), [Multilingual glossary](../../08_glossary/glossary_multilingual.md) (Portuguese column)
- Other languages: [es](es.md), [fr](fr.md), [it](it.md)
