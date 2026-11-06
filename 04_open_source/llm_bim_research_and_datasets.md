# Research on natural-language querying of BIM/IFC and LLM agents (papers, datasets, benchmarks)

## In plain words

Since about 2016 researchers have tried to let people ask a building model questions in everyday language ("how many doors are on level 2?") instead of clicking through BIM software or writing code. Early work (2016-2022) parsed sentences with NLP rules and mapped words to IFC entities or to database/SPARQL queries. From 2023 large language models (LLMs) took over: first as prompt-based assistants (BIM-GPT, 2023), then as agents that write and run code against IfcOpenShell or the Revit API, and since 2025 as tool servers exposed via the Model Context Protocol (MCP). The first open benchmark with real IFC models and graded answers is IFC-Bench (v1 in 2025, v2 with 1,027 questions in 2026). For a QA tester of MCP servers this body of work is a ready-made source of question types, ground-truth methods and known failure modes.

Last researched: 2026-11-06

> Research limits for this document: the web-search tool hit its per-session budget early, so discovery was done by following the citation graph (Semantic Scholar listings of citing/cited papers) and by fetching primary pages (arXiv, Hugging Face, GitHub). Chinese- and Korean-language searches could not be run (see Gaps). Facts below are limited to what those pages state; anything seen only in a title list is flagged "(listing only)".

## 1. Timeline of the field

| Period | Typical approach | Representative work |
|---|---|---|
| 2016 | Rule/NLP parsing: split request into "keywords" (objects) and "constraints", map them to IFC entities/properties through a dictionary (IFD), traverse a graph built from the IFC schema | Lin, Hu, Zhang, Yu - natural-language approach for cloud BIM, tested on the Kunming Airport terminal data [14] |
| 2016 | Ontology layer for IFC: ifcOWL (EXPRESS-to-OWL conversion), the basis for SPARQL over IFC | Pauwels and Terkaj, Automation in Construction, 2016 [31] |
| 2020-2023 | Semantic parsing to SPARQL or BIMQL; graph neural nets; voice (ASR) front ends | Automatic SPARQL generation for BIM data extraction (Applied Sciences 2020, listing only) [21]; Text-to-BIMQL with GNNs (Automation in Construction 2023, listing only) [21]; BIMASR voice retrieval (2021, listing only) [21]; voice assistant for BIM data management (2022, listing only) [21]; NLP query-answering system for BIM (JCCE 2022, listing only) [21] |
| 2023 | Ontology-aided semantic parser producing SPARQL with reasoning rules | Yin et al. [13] |
| 2023 | First prompt-based GPT assistant for BIM search | BIM-GPT, Zheng and Fischer [3][4] |
| 2024 | LLM copilots inside authoring tools; chat/voice assistants wired to Revit | Copilot for Vectorworks [16]; DAVE for Revit [17]; Speech-to-BIM / NADIA-S [15][32] |
| 2024-2025 | LLMs generate building models from text | Text2BIM [1][2] |
| 2025-2026 | Code-generating agents, query DSLs, RAG over IFC properties, MCP servers, benchmarks | IFC-Bench v1/v2 [7][8][9], MCP4IFC [19], MCP reference architecture [18], Query2Property [20], IFCMemoryBench [11] |

## 2. Natural-language retrieval and question answering over BIM

### 2.1 Pre-LLM (2016-2022)

- **Cloud BIM retrieval (2016).** Requests are decomposed into keywords and constraints, mapped to IFC entities/properties via the International Framework for Dictionaries (IFD), and answered by path-finding in a graph generated from the IFC schema. Prototype used real data from a large airport terminal; the arXiv page gives no quantitative metrics [14].
- **ifcOWL and SPARQL.** ifcOWL converts the IFC EXPRESS schema into an OWL ontology so IFC data can be stored as RDF and queried with SPARQL; the 2016 paper by Pauwels and Terkaj is the standard citation [31]. The W3C Linked Building Data group also publishes the small Building Topology Ontology (BOT: Site, Building, Storey, Space, Element, plus relations such as `containsZone`, `adjacentElement`, `hasSubElement`) which has an alignment module to ifcOWL [29]. These ontologies are what text-to-SPARQL systems target.
- **Automatic SPARQL generation (2020), Text-to-BIMQL with GNNs (2023), BIMASR voice retrieval (2021), NLP QA system (2022)** appear in the reference list of the 2026 ifc-bench v2 paper, which treats them as the prior art in the field; details were not retrieved [21].
- **Ontology-aided multi-constraint querying (Yin et al., 2023).** A modular ontology holds natural-language expressions of IFC concepts and relations, is populated with entities of the target model, and a parser progressively extracts concepts, relations and value restrictions to emit SPARQL with reasoning rules. Evaluation: 225 natural-language queries collected from BIM users, 91% accuracy, plus a design-checking case study on a residential building [13].

### 2.2 Prompt-based and fine-tuned LLM systems (2023-2025)

- **BIM-GPT (Zheng and Fischer, 2023; Automation in Construction, DOI 10.1016/j.autcon.2023.105067).** A prompt manager plus dynamic prompt templates let GPT models interpret a user query, retrieve BIM information, summarize it and answer BIM questions. Query classification accuracy was 83.5% with no BIM data in the prompt and 99.5% when 2% of the data was included. Validated with a hospital-building prototype [3][4].
- **DAVE (Fernandes et al., Buildings 2024).** Text or voice assistant on a GPT model, connected to Revit through Python scripts and the Revit API; reported 94% correct answers on single-function queries, with response times and validation errors discussed [17].
- **Fine-tuning vs prompting (Gao et al., arXiv 2508.05676, Aug 2025).** Two-stage pipeline (intent recognition, then table-based QA); dataset of 1,740 annotated queries "of varying types". Result: fine-tuning is better at intent recognition, prompting (GPT-4o) is better at table QA, and a hybrid is the most balanced [12]. (Category names and metric values were not retrievable.)
- **Query2Property (Lamsal and Zlatanova, ISPRS Annals 2026).** Embeds IFC property descriptions and user queries and matches by similarity so that only relevant properties go into the prompt, not the whole schema. On 55 representative BIM queries: 87.3% top-1 and 100% top-3 accuracy [20].
- **Metadata-grounded retrieval in VR (Buildings 2026, DOI 10.3390/buildings16163168).** LLM turns the question into structured metadata filters executed deterministically; on a 30-query benchmark it reports precision 99.94%, recall 100%, F1 99.97%, 0.347 s mean runtime, and the authors warn this holds only for a controlled schema [5].
- **Other 2025-2026 works seen only as titles (listing only):** BuildingGPT (vector-graph RAG, Building and Environment 2025); BIMCoder (Applied Sciences 2025); LLM query DSL with library-function alignment; multi-LLM agent code generation for cost-effective retrieval; balancing cost and performance of LLMs in a multi-agent BIM retrieval framework; text-to-structure interpretation of user requests; natural-language interaction with 4D BIM; interactive 3D spatial relationship query with an LLM agent; BuildingQA (QA benchmark over building knowledge graphs, BuildSys 2025); AECBench (hierarchical LLM benchmark for AEC); RAG code generation for dynamic IFC query (Buildings 2026) [5][6][21].

### 2.3 Agents that write code against IFC (2025-2026)

The newest line of work treats the IFC file as a runtime puzzle: the LLM writes Python (usually IfcOpenShell), runs it, reads the output, and repeats.

- **Adaptive exploration + ifc-bench v2 (Hellin, Jang, Fuchs, Nousias, Borrmann; arXiv 2605.01698, May 2026; submitted to Automation in Construction).** Argues static "question to query" translation breaks because IFC models are heterogeneous (different authoring tools, property-set names, units). The agent instead discovers each model's structure at runtime. In a factorial ablation (two LLM capability levels x four augmentation strategies) adaptive exploration beat static query generation in every configuration [7][8].
- **Cobbie** (code repository for the same work) is a multi-agent system with agents for code generation, verification, tool creation, debugging and assessment; tools created during a training split are reused at inference; documentation comes from a RAG index over IfcOpenShell docs [10].
- **IFCMemoryBench (Du, Vosseler, Mazza, Borrmann; arXiv 2607.26072, Jul 2026; KDD 2026 workshop).** Tests whether agents can combine facts remembered from earlier sessions with live IFC queries: 143 multi-session tasks, 19 projects, 4,016 prior sessions. Best memory system: 32.4% answer accuracy in a deployment-realistic setting, still under 60% in favourable ones [11].
- **Benchmarking LLMs on production BIM workflows (Buildings 2026, DOI 10.3390/buildings16214183).** Ten LLMs inside one commercial Revit add-in, four tracks (requirement extraction from an ISO 19650 BIM Execution Plan, rules from an 88-page scanned Arabic building code, multimodal drawing review, ten colloquial prompts with adversarial probes); 218 logged calls; top score 88.7/100. Finding: fuzzy name resolution (matching a colloquial name to the real family/type/parameter name), not code generation, caused 60% of lost agentic points [5].
- **Conversational MCP-Navisworks (Construction Innovation 2026, DOI 10.1108/ci-05-2026-0181).** LLM connected to Navisworks Clash Detective via MCP; 45 clashes grouped into 20 prioritised groups in three cases from a real residential project; authors call it a viability study, not a performance measure [5].

## 3. LLM generation and editing of BIM (not just querying)

| System | What it does | Evaluation facts |
|---|---|---|
| **Text2BIM** (Du, Esser, Nousias, Borrmann; arXiv 2408.08054, first Aug 2024, v2 Jul 2025) | Multi-agent LLM workflow turns a text brief into code calling a BIM authoring API; a rule-based model checker feeds issues back for iterative repair; prototype inside Vectorworks; output is editable BIM with interior layout, envelope and semantics [1][2] | v2: 25 prompts across 8 capability aspects (base geometry, multi-storey composition, materials, roofs, space layout, openings, circulation, dimensional accuracy); 3 LLMs (o4-mini-high, Claude-sonnet-4, Gemini-2.5-Pro); each prompt run 3 times (534 IFC models incl. intermediates); pass rate against 30 Solibri rule checks mostly above 0.95; issue counts dropped over 3 repair rounds (about 70% resolved by the best models); 4 experts rated prompt adherence (-1 to 1) and realism (1-5); CodeBERTScore F1 about 0.82-0.96 [2] |
| **Copilot for BIM authoring** (Du, Nousias, Borrmann; arXiv 2406.16903) | LLM agent answers software-usage questions, interprets design intent, calls tools; Vectorworks prototype [16] | Compares planning/reasoning of different LLMs on complex instructions; details not on the abstract page [16] |
| **Speech-to-BIM / NADIA-S** (Lee, Jang, Hyun; arXiv 2409.18345; CIB W78 2024) | Six-step "interpret-fill-match-structure-execute-check" framework for LLM-augmented BIM; demo is voice-driven exterior wall detailing [15]. Original NADIA paper: Jang, Lee, Oh, Lee, Koo, Advanced Engineering Informatics 2024 [32] | Abstract-level only [15][32] |
| **MCP4IFC** (Nithyanantham et al.; arXiv 2511.05533, Oct 2025) | Open-source MCP framework giving an LLM scene-query tools, predefined create/modify functions, and dynamic code generation (in-context learning + RAG) for everything else; examples include building a simple house and querying/editing existing IFC data [19] | Abstract states experiments succeeded; no benchmark named [19] |
| **Modular MCP reference architecture** (Heimig-Elschner, Du, Scheuvens, Borrmann, Beetz; arXiv 2601.00809; accepted at a TUM symposium, May 2026) | Microservice design with an explicit adapter contract separating the MCP interface from the BIM API; IfcOpenShell prototype; requirements derived from a systematic review of LLM/MCP BIM agents [18] | "Representative scenarios" on modification and generation tasks [18] |
| BIMgent (arXiv 2506.07217), Sketch2BIM (arXiv 2510.20838), Text-to-Code for modular layouts (arXiv 2509.23713), KIR typed IR for agent-authored BIM (arXiv 2609.14578) | Listed as papers citing Text2BIM (listing only) [23] | - |

Text2BIM sample instruction style (paraphrased from the paper's worked example): a two-storey hotel with 16 rooms, central corridor, pitched timber roof and brick walls [2].

## 4. Datasets and benchmarks of natural-language questions over building models

### 4.1 IFC-Bench (the main open dataset)

- **Hosting:** Hugging Face dataset `sylvainHellin/ifc-bench` (CSV, about 2 GB with models) [9]; code in GitHub `sylvainHellin/cobbie` [10]. Dataset license CC BY 4.0; each IFC model keeps its own licence (most CC BY 4.0 or MIT, four GPLv3) [9].
- **Versions:** v1 = 99 queries per the v2 paper [8] (the dataset card shows a preserved v1 subset of 105 rows [9]; the discrepancy is unexplained). The prior agent with 29 hand-coded tools reached 80% on v1 [8]. v2 = 1,027 QA pairs; the paper says 37 models from 21 projects [8], while the dataset card says 51 IFC models in 22 projects and counts 1,026-1,027 pairs [9]. Treat the card as the newer figure (unverified which is final). The cobbie README separately mentions a 200-question, 10-model, 8-category subset [10].
- **Fields:** `id`, `question`, `ground_truth`, `ifc_model`, `project`, `category` (1-4) [9].
- **Model sources named:** BIMserver TestFiles, KIT IFC examples, buildingSMART sample files, RWTH E3D, OpenIFC, WBDG, TUM BIM-fundamentals student models; examples `ac20`, `dental_clinic`, `west_riverside_hospital` [9].
- **Categories (v2 card counts):** [9]

| Cat. | Name | Count | Paraphrased example (from the paper [8]) |
|---|---|---|---|
| 1 | Direct Information Retrieval | 152 | What is the fire rating of door D-201? |
| 2 | Computational Aggregation (counting, summing) | 569 | How many walls are on the second floor? |
| 3 | Geometric/Spatial Computation | 112 | What is the total window area on the south facade? |
| 4 | Incomplete Information (missing, ambiguous or must be estimated) | 194 | Answer should say the model does not contain the information |

  The 514-question fixed test split has 72 / 283 / 57 / 102 questions in categories 1-4 [8]. Dataset card topics include software and IFC version, space areas by floor, door/window types and counts, wall volumes/lengths, slab and concrete volumes, MEP components, and whether data is missing [9].
- **Grading:** LLM-as-judge, not exact match. The judge sees question, ground truth, system answer and full execution trace and scores five binary criteria: abstention, faithfulness, completeness, transparency, relevance; "correct" requires faithfulness, completeness, transparency and relevance all pass. The paper reports judges had higher inter-rater reliability (Krippendorff's alpha 0.70-1.00) than human experts (0.32-0.57) in a companion study [8].
- **Headline results (test set, GLM 4.7 / GLM 4.5 Air):** adaptive exploration 56.0% / 25.7% with no augmentation; static one-shot generation 19.1% (4.7); static abstains on roughly 43-55% of questions vs under 7% for adaptive [8]. These are low absolute numbers: even a strong model answers about half of realistic questions correctly.

### 4.2 Mapping common question families onto the benchmark

The paper uses four categories, not six. The mapping below is this document's own (illustrative):

| Family a tester will think of | Where it falls in IFC-Bench |
|---|---|
| Existence ("Is there a lift?") | Category 1 or 4 (a "no" must be distinguished from "model lacks the data") |
| Attribute lookup (fire rating, material, name) | Category 1 |
| Counting | Category 2 |
| Aggregation (sum of areas/volumes, group by storey/type) | Category 2 |
| Spatial (areas, clearances, facade orientation, which room contains X) | Category 3 |
| Relational (what is connected to/hosted in/inside what) | Mixed 1-3 (not a separate category in the paper) |
| Unanswerable / ambiguous | Category 4 |

### 4.3 Other datasets and evaluation efforts (mostly listing only)

| Resource | Facts |
|---|---|
| 1,740 annotated BIM queries (Gao et al.) | Used for intent recognition + table QA; availability not confirmed [12] |
| 225 NL queries from BIM users (Yin et al.) | 91% accuracy of ontology-aided parser [13] |
| 55 queries (Query2Property), 30 queries (VR retrieval) | Small hand-built sets [20][5] |
| IFCMemoryBench | 143 multi-session tasks derived from the incomplete-information questions of IFC-Bench v2 [11] |
| BuildingQA, AECBench | Titles seen; details not retrieved [6][5] |
| "Enabling cross-study comparison: a framework for automated BIM-QA evaluation" and "A systematic evaluation framework for AI-driven BIM question answering systems" | Cited by the ifc-bench v2 paper as evaluation-framework work; abstracts could not be retrieved (rate limit) [21] |
| Text2BIM checks | 30 Solibri rule checks used as an automatic quality gate for generated IFC [2] |

## 5. Evaluation methods in use

1. **Exact/numeric match against ground truth computed with a script** (typical for counts and areas; used implicitly in small benchmarks) - hence the need to define tolerance for floats and units.
2. **LLM-as-judge with trace access** (IFC-Bench v2) - judges whether the answer is faithful to what the code actually returned, not only whether it matches [8].
3. **Retrieval metrics** (precision/recall/F1, top-k accuracy) for systems that select properties or filter elements [5][20].
4. **Intent/query classification accuracy** (BIM-GPT) [3].
5. **Rule-based model checking** of generated models (Solibri rule sets in Text2BIM) plus issue counts per repair round [2].
6. **Expert rating** (adherence scale, realism Likert) and Turing-style tests for generation [2].
7. **Code similarity** (CodeBERTScore) when reference code exists [2].
8. **Repeated runs** - Text2BIM ran each prompt three times and reported mean and standard deviation [2].
9. **Abstention / hallucination handling** as an explicit criterion [8].
10. **Operational metrics**: response time per query [17][5], logged tool calls and cost [5].

## 6. Tooling used by the agents (what MCP servers wrap)

- **IfcOpenShell** (GitHub IfcOpenShell/IfcOpenShell): open-source IFC library; parsing of IFC2x3 TC1, IFC4 Add2 TC1, IFC4x1, IFC4x2, IFC4x3 Add2; geometry processing mainly IFC2x3 and IFC4; includes the Bonsai Blender add-on, IfcConvert, ifcclash, ifcpatch, ifctester, BCF and IDS support; LGPL-3.0 core, GPL-3.0 for Bonsai [24].
- **Bonsai MCP** (JotaDeRodriguez/Bonsai_mcp, MIT, community fork of BlenderMCP): tools to list entities by type, get properties by GlobalId, spatial hierarchy, relationships, quantities, selected objects, viewport image, georeferencing, create an element at coordinates, and export JSON/CSV/PNG plans/BC3 budgets; a README caveat says large models are slow and complex tasks should be split; also exposes a raw Python execution tool that the README says to use with caution [27].
- **revit-mcp** (revit-mcp/revit-mcp, archived) -> **mcp-servers-for-revit** (mono-repo): TypeScript MCP server, Revit plugin over WebSocket/socket, C# command set; 26 tools in the mono-repo: query (current view elements, selected elements, family types, material quantities, general element filter, model statistics), create (point/line/surface-based elements, grids, levels, rooms, dimensions, structural framing), modify (delete, operate, colour by parameter, tag walls/rooms), data (export room data, store/query project data), and `send_code_to_revit` for AI-generated C#. Revit 2020-2026 (2020-2024 on .NET Framework 4.8, 2025-2026 on .NET 8). The original README noted `send_code_to_revit` has uneven success [25][26].
- **MCP** is an open standard for connecting AI applications to external data sources, tools and workflows [28].
- **IDS** (buildingSMART Information Delivery Specification): XML standard (XSD) for machine-readable IFC information requirements; useful to turn "does the model contain X" into a checkable rule [30]. (The buildingSMART website returned HTTP 403 to the fetcher, so only the GitHub repository was read.)

## 7. Failure modes reported in the literature

- **Heterogeneous models:** the same fact lives in different property sets or under different names in different IFC files; static query templates fail (core motivation of adaptive exploration) [7].
- **Silent abstention:** static generation refused to answer on roughly half of questions in IFC-Bench v2 [8].
- **Name resolution:** colloquial names vs real family/type/parameter names caused most agent point losses in a Revit add-in benchmark [5].
- **Incomplete information:** models that guess instead of saying "not in the model" (Category 4) [8][9].
- **Context overload:** feeding the whole schema or all properties raises cost and error; hence retrieval of relevant properties (Query2Property) [20].
- **Generation realism:** Text2BIM outputs lacked stairs, columns and beams, had weak door/window placement and structural flaws, and the weakest model hallucinated openings [2].
- **Code execution tools:** arbitrary-code tools (`send_code_to_revit`, Blender Python) give flexibility but uneven reliability and a safety surface [25][27].
- **Memory across sessions:** best memory system 32.4% accuracy on IFCMemoryBench [11].
- **Controlled-schema caveat:** near-perfect scores on small hand-made benchmarks do not generalise (stated by the authors) [5].

## 8. Implications for testing MCP servers for IFC/Revit

1. **Build a ground-truth fixture set.** Pick 3-5 public IFC models of different origin and size (IFC-Bench lists such sources [9]), compute answers with a short IfcOpenShell script, store question + expected answer + category, as in IFC-Bench's `question / ground_truth / ifc_model / category`.
2. **Cover all four categories**, including at least 20% Category 4 (unanswerable) questions; in IFC-Bench v2 it is 194 of 1,027 questions [9]. Expected good behaviour: a clear "this model has no such data", not an invented number.
3. **Check the trace, not just the answer.** Mirror the judge criteria: abstention, faithfulness (answer matches tool output), completeness, transparency (says how it got it), relevance [8].
4. **Test colloquial names and typos** ("window", "glazing", "Fenster"; type names that differ from IFC class names) - fuzzy name resolution was the biggest loss source in [5].
5. **Test across IFC versions and authoring tools** (IFC2x3 vs IFC4 vs IFC4x3; Revit vs ArchiCAD exports). IfcOpenShell geometry support is strongest for IFC2x3 and IFC4 [24], so spatial/geometric questions on IFC4x3 are higher risk (inference from [24], unverified in practice).
6. **Repeat runs** (at least 3) and report variance; LLM agents are non-deterministic [2].
7. **Separate read tools from write tools.** Write-capable servers (create, modify, delete, run code) need pre/post-state diff checks and a rollback path; consider rule checks after generation, as Text2BIM did with a model checker [2].
8. **Measure efficiency:** tool calls per question, latency (DAVE reported response times [17]), token cost, failure to terminate.
9. **Multi-session memory** is a separate test dimension [11].
10. **Large models:** the Bonsai MCP README warns of slowness on large models; include one big model and a timeout test [27].
11. **Revit specifics:** version matrix (2020-2026 in the mono-repo [26]), plugin not running / Revit modal dialog open, no document open, linked models, worksets - the last four are illustrative edge cases, not drawn from the sources.
12. **Reference architecture:** the adapter-contract design [18] suggests testing that the same natural-language task gives equivalent results through different back-ends (IfcOpenShell vs Revit).

## Typical questions people ask about this

Questions marked with a link come from the benchmark/papers (paraphrased); the rest are illustrative.

1. What is the fire rating of door D-201? ([8] example, Category 1)
2. How many walls are on the second floor? ([8] example, Category 2)
3. What is the total window area on the south facade? ([8] example, Category 3)
4. Which IFC schema version and authoring software produced this file? (type listed in dataset card [9])
5. What is the area of each space on level 1? (type listed in dataset card [9])
6. How many doors of each type are there? (type listed in dataset card [9])
7. What is the total concrete volume of the slabs? (type listed in dataset card [9])
8. Does the model contain information on X? (expect "no data" answer, Category 4 [9])
9. Show me all walls with fire rating of at least 60 minutes and external (multi-constraint query style from [13]) (illustrative)
10. List all rooms adjacent to the corridor on level 2 (relational) (illustrative)
11. Is there an element with no assigned material? (existence/quality) (illustrative)
12. Which storey contains the room named "Server"? (spatial containment) (illustrative)
13. How many clashes between ducts and beams are there, and group them by priority? (cf. MCP-Navisworks [5]) (illustrative)
14. Create a two-storey hotel with 16 rooms, a central corridor and a pitched roof (cf. Text2BIM [2]) (illustrative)
15. Which Revit view elements are currently selected, and what are their parameters? (illustrative; tool types in [25])
16. Colour all walls by fire rating and tag all rooms (illustrative; tools in [25])
17. What did we agree last week about the level naming? (memory question, cf. [11]) (illustrative)
18. Can the assistant explain how it got the number? (transparency criterion [8]) (illustrative)
19. Why does the same question give different answers on two IFC files? (heterogeneity [7]) (illustrative)
20. Why does it say "I cannot find this property" when Revit shows it? (property set / name mismatch [5][7]) (illustrative)

## Common pitfalls and misconceptions

- **"A high demo accuracy means it works."** Small controlled benchmarks (30-225 queries on a fixed schema) report 87-100% [5][13][20]; IFC-Bench v2 shows about 56% for the best configuration of the tested models [8]. Numbers are not comparable across papers: different models, question sets, graders.
- **Mixing up categories.** The IFC-Bench paper has 4 categories; "counting, attribute, spatial, relational, aggregation, existence" is a tester's taxonomy, not the paper's [8].
- **Counting dataset size.** v1 is quoted as 99 [8] or 105 [9]; v2 as 1,026-1,027 questions, 37 or 51 models, 21 or 22 projects. Quote the source you used.
- **Exact string match grading.** The benchmark uses LLM judges with execution traces precisely because correct answers vary in wording and units [8].
- **"LLM reads the IFC file."** Real systems do not paste the file into the prompt; they retrieve properties [20], write code [7][10], or call fixed tools [19][27].
- **IFC is not Revit.** An IFC export may drop or rename parameters; MCP servers for IFC (IfcOpenShell-based) and for Revit (Revit API) answer from different data models [24][26].
- **Generated models are not design-ready.** Text2BIM passes rule checks but experts found missing stairs, columns and beams [2].
- **Preprint status.** Many 2025-2026 items are arXiv preprints or workshop papers, and some journal entries here are known only from citation lists.
- **Dates and ids.** Some arXiv numbers (26xx.xxxxx) are cited from listings; open them to confirm before quoting.

## Gaps

- The web-search tool's per-session budget was exhausted before any query returned results, so no keyword searches were done in English, Chinese or Korean. Chinese-language (e.g. 自然语言查询 BIM, 大语言模型 IFC) and Korean-language (e.g. BIM 자연어 질의, 거대언어모델) literature were not searched directly. Relevant authors do appear: Korean-affiliated work on NADIA / Speech-to-BIM [15][32] and Chinese-affiliated work on cloud BIM retrieval, ontology-aided querying and fine-tuning comparison [12][13][14]; native-language terms and CNKI/KCI sources remain to be covered.
- buildingSMART pages (technical.buildingsmart.org ifcOWL page, IDS page) returned HTTP 403; ifcOWL status/version details come from secondary sources [29][31].
- Publisher pages (Elsevier, MDPI, ASCE) were blocked or redirected; DOIs are reported as listed by Semantic Scholar. Abstracts for BuildingGPT, BIMCoder, BuildingQA, AECBench, Text-to-BIMQL, the BIM-QA evaluation frameworks and others were not retrieved.
- No real forum/community questions (e.g. from buildingSMART forums, OSArch) were retrieved, so the question list is mostly illustrative.
- No suspicious or pirated sites were encountered. Nothing was downloaded or executed; one PDF fetched by the fetch tool was saved by the harness and could not be rendered.

## Sources

Primary papers and datasets
- [1] Text2BIM abstract: https://arxiv.org/abs/2408.08054
- [2] Text2BIM full text (HTML v2): https://arxiv.org/html/2408.08054v2
- [3] BIM-GPT (arXiv): https://arxiv.org/abs/2304.09333
- [4] BIM-GPT bibliographic record (Semantic Scholar): https://api.semanticscholar.org/graph/v1/paper/DOI:10.1016/j.autcon.2023.105067?fields=title,year,venue,abstract,authors,citationCount
- [7] Adaptive exploration / ifc-bench v2 abstract: https://arxiv.org/abs/2605.01698
- [8] Same, full text: https://arxiv.org/html/2605.01698v1
- [9] IFC-Bench dataset: https://huggingface.co/datasets/sylvainHellin/ifc-bench
- [10] Cobbie repository: https://github.com/sylvainHellin/cobbie
- [11] IFCMemoryBench: https://arxiv.org/abs/2607.26072
- [12] Fine-tuning vs prompting for BIM retrieval: https://arxiv.org/abs/2508.05676
- [13] Ontology-aided multi-constraint BIM querying: https://arxiv.org/abs/2303.15116
- [14] Natural-language approach for cloud BIM (2016): https://arxiv.org/abs/2411.09951
- [15] Speech-to-BIM / NADIA-S: https://arxiv.org/abs/2409.18345
- [16] Copilot in BIM authoring tool: https://arxiv.org/abs/2406.16903
- [17] DAVE GPT assistant for Revit (Semantic Scholar record): https://api.semanticscholar.org/graph/v1/paper/DOI:10.3390/buildings14082499?fields=title,year,venue,abstract,authors
- [18] Modular reference architecture for MCP servers: https://arxiv.org/abs/2601.00809
- [19] MCP4IFC: https://arxiv.org/abs/2511.05533
- [20] Query2Property (Semantic Scholar record): https://api.semanticscholar.org/graph/v1/paper/DOI:10.5194/isprs-annals-xi-4-2026-323-2026?fields=title,year,venue,abstract,authors
- [31] ifcOWL paper record: https://api.semanticscholar.org/graph/v1/paper/DOI:10.1016/j.autcon.2015.12.003?fields=title,year,venue,abstract,authors,citationCount
- [32] NADIA record: https://api.semanticscholar.org/graph/v1/paper/DOI:10.1016/j.aei.2024.102532?fields=title,year,venue,abstract,authors

Citation-graph listings (used for discovery; titles, years, DOIs, some abstracts)
- [5] Papers citing BIM-GPT, page 1 (with abstracts): https://api.semanticscholar.org/graph/v1/paper/DOI:10.1016/j.autcon.2023.105067/citations?fields=title,year,venue,externalIds,abstract&limit=100
- [6] Papers citing BIM-GPT, page 2: https://api.semanticscholar.org/graph/v1/paper/DOI:10.1016/j.autcon.2023.105067/citations?fields=title,year,venue,externalIds&limit=100&offset=100
- [21] References of the ifc-bench v2 paper: https://api.semanticscholar.org/graph/v1/paper/arXiv:2605.01698/references?fields=title,year,venue,externalIds&limit=100
- [22] References of Text2BIM: https://api.semanticscholar.org/graph/v1/paper/arXiv:2408.08054/references?fields=title,year,venue,externalIds&limit=100
- [23] Papers citing Text2BIM: https://api.semanticscholar.org/graph/v1/paper/arXiv:2408.08054/citations?fields=title,year,venue,externalIds&limit=100

Tools, standards, ontologies
- [24] IfcOpenShell: https://github.com/IfcOpenShell/IfcOpenShell
- [25] revit-mcp (archived): https://github.com/revit-mcp/revit-mcp
- [26] mcp-servers-for-revit: https://github.com/mcp-servers-for-revit/mcp-servers-for-revit
- [27] Bonsai MCP (community project): https://github.com/JotaDeRodriguez/Bonsai_mcp
- [28] Model Context Protocol introduction: https://modelcontextprotocol.io/docs/getting-started/intro
- [29] BOT, W3C Linked Building Data CG: https://w3c-lbd-cg.github.io/bot/
- [30] buildingSMART IDS repository: https://github.com/buildingSMART/IDS
