# English: how people ask about IFC, BIM and Revit

> **Basis.** 1,796 real records (1,463 distinct pages; 387 are snippet-level, meaning only a title or search summary was seen) and 618 synthetic prompts, all with `lang=en`, from `research_raw/wave1` (collected 6 Nov 2026). "Real" means observed at a public source. "Synthetic" means written by a research agent to imitate real patterns, and is always labelled so here. Real questions below are **paraphrases** by the research agents (titles are verbatim only when 20 words or shorter), so they show register and content but are not exact quotes. Short phrases in quotation marks in the writing-style sections are taken from the research reports and paraphrases; they illustrate the voice and are not guaranteed to be word-for-word.

> **Contents of this file:** 91 curated real questions (Real questions) and 77 ready test prompts (Ready test prompts), 10 of which are rewrites.
>
> **Language of this file:** English explanations; examples are English, so there is no gloss column. For other languages see the sibling files in this folder.

## Read this first: what this data can and cannot tell you

- **Region is not recorded.** The record schema has no country field. Regional statements below rest on hints: topic words (Uniclass, CORENET X, COBie, DOT), coordinate-system codes, openers such as "G'day all", and what the regional research cells reported. Treat them as hints, not statistics.
- **The real data leans technical.** 64% of real records are GitHub issues and 33% come from developers. Plain "I have a file and want an answer" voices are rarer in real data than in the synthetic prompts.
- **Several regional cells are thin or incomplete.** The Singapore "real" records are mostly tool READMEs, not forum posts. The Middle East/Africa cell has 3 real records. The Reddit and Stack Overflow cells have no real records at all (synthetic only). Australia/NZ and India share a research cell with the UK, and that cell reported no posts it could attribute to Australian, New Zealand or Indian authors.
- **45% of real records are from 2025-2026**, so examples reflect recent Revit (2025-2027 era) and Bonsai versions.
- **Some record ids are reused.** Ids marked † in the tables below are shared by two different records in the raw files; the source link identifies the right one.

| Quick facts | Real | Synthetic |
|---|---|---|
| Records | 1,796 | 618 |
| Mostly | troubleshooting (923), how-to (395), feature requests (211) | "model tasks" (513): check, count, list, compare, edit |
| Typical length | titles median 7 words | prompts median 15 words (range 5-31); 596 of 618 start in lowercase |
| Tone | neutral 524, frustrated 407, confused 402, curious 312, polite 83, skeptical 37, urgent 31 | neutral 316, confused 82, frustrated 80, urgent 63 |
| IFC versions named | IFC4 570, IFC2x3 210, IFC4.3 (all spellings) 171; the rest unknown, unspecified or blank | needs a model loaded: 525 of 618 |

Related KB documents: [IFC in real projects](../../01_ifc_basics/00_ifc_in_real_projects.md), [IFC versions](../../01_ifc_basics/01_what_is_ifc_and_versions.md), [abbreviations](../../08_glossary/abbreviations.md), [Revit export topic page](../by_topic/revit_export_and_class_mapping.md), [validation and IDS topic page](../by_topic/validation_ids_model_checking.md).

## Where people ask

| Platform | Real records (distinct pages) | Who writes there | What it looks like | Access notes from the research |
|---|---|---|---|---|
| **GitHub issues and discussions** | 1,177 (904) | Developers, power users, some coordinators | Template-driven bug reports; titles carry the symptom. Biggest sources: Autodesk/revit-ifc (426 records), IfcOpenShell/Bonsai (387), That Open web-ifc (98), xBIM (57), buildingSMART IDS (17) | Open and readable. Revit-ifc issues use `PR:` (problem report), `ENH:`, `INQ:` (inquiry) title prefixes |
| **buildingSMART International forum** (forums.buildingsmart.org) | 230 (201) | Implementers, BIM managers, civil/infra engineers, many non-native speakers | Long polite posts, numbered sub-questions, pasted STEP lines; opinion threads | Readable through its public JSON endpoints. Answers are often from standards staff and maintainers |
| **OSArch community** (community.osarch.org) | 179 (153) | Bonsai/IfcOpenShell users, architects leaving Revit, teachers, AI experimenters | Informal, collegial, version numbers almost always given; many "solved" self-answers | Readable. Dates show only month and day, so some years are inferred |
| **Dynamo forum** (forum.dynamobim.com) | 69 (69) | Revit automation users | 3-8 sentences with screenshot or graph; greeting and thanks common | Readable |
| **Autodesk forums** (Revit, Civil 3D) | 69 (65) | Architects, coordinators, structural/MEP engineers | Symptom-first titles with the Revit year; "Solved:" prefix added by the board | Returned HTTP 403 on fetch, so most records are **snippet-level** (title plus search summary) |
| **pyRevit discourse** | 18 (18) | Revit scripters | Short, polite, code-first | Readable |
| **Blogs** (BIM Corner) | 19 (19) | BIM managers writing for peers | Problem-then-solution, numbered checklists, concrete counts ("161 proxies") | Readable; questions appear mostly as reader comments |
| **Vendor help centres** (BIMcollab, Tekla) | 14 (13) | Coordinators using Solibri/BIMcollab/Tekla | "Why is/are/don't I...?" titles, no model context | Readable |
| **Other communities** (Cesium forum, Graphisoft) | 14 (14) | GIS / web 3D developers; one Archicad thread | Short technical posts about georeferencing and web viewers | Readable |
| **Official portals** (CORENET X, IMI Framework, cidb) | 5 | n/a (reference pages) | Not questions; used for context | Several pages returned 403/404 |

**Not covered by real data:** Reddit (r/Revit, r/bim, r/StructuralEngineering and others), Stack Overflow and Stack Exchange, LinkedIn, Quora, YouTube comments, Archicad/Graphisoft community (1 record), Navisworks/ACC forums, Allplan, Vectorworks and Bentley communities. The matching cells contain only synthetic prompts, whose style is **unvalidated**.


## Top themes (ranked)

Ranked by the number of distinct **real** records carrying any of the theme's topic tags (a record can carry up to four tags, so themes overlap and the numbers do not add up to the total). The second number counts synthetic prompts with the same tags. Where the two differ, real users are asking *why something broke*, while synthetic prompts ask the assistant *to do or check something*.

| Rank | Theme | Real / synthetic records | What it sounds like | Examples |
|---|---|---|---|---|
| 1 | Revit-to-IFC export goes wrong: classes become proxies, objects vanish, custom properties are missing, Revit hangs | 365 / 70 | "IfcExportAs doesn't work", "user defined properties won't export", "Revit crashes every time I export IFC!!!" | [Autodesk forum](https://forums.autodesk.com/t5/revit-structure-forum/ifcexportas-parameter-doesn-t-work/td-p/8219179); [Autodesk forum](https://forums.autodesk.com/t5/revit-architecture-forum/revit-ifc-export-user-defined-properties-won-t-export/td-p/9767878); [Autodesk forum](https://forums.autodesk.com/t5/revit-architecture-forum/quot-ghost-quot-mullions-in-ifc-export/td-p/13056918) |
| 2 | Developer questions: reading and writing IFC from code, memory, performance, quantities | 358 / 39 | "2 GB IFC, 16 GB RAM, open() runs out of memory", "CreateContext hits 100% CPU" | [GitHub IfcOpenShell #2025](https://github.com/IfcOpenShell/IfcOpenShell/issues/2025); [GitHub xBIM #569](https://github.com/xBimTeam/XbimGeometry/issues/569) |
| 3 | Geometry quality and openings: missing, shifted or solid walls, windows without holes, faceted curves | 284 / 61 | "Revit to IFC, Wall is dislocated", "Opening Cuts Skipped", "opens in BIM Vision but not Revit" | [bSI forum](https://forums.buildingsmart.org/t/revit-to-ifc-wall-is-dislocated/4575); [OSArch](https://community.osarch.org/discussion/3754/opening-cuts-skipped-in-bonsai-studio-0-9) |
| 4 | MEP, structural, rebar, materials and colours: semantic mismatches (system name as material, grey pipes) | 252 / 66 | "Pipes export using system material not actual material" | [GitHub revit-ifc #577](https://github.com/Autodesk/revit-ifc/issues/577) |
| 5 | Properties and property sets: which pset, which units, empty values not written | 241 / 95 | "is there a way to export parameters with empty values", "flow in L/s is exported in ft3/s" | [GitHub revit-ifc #963](https://github.com/Autodesk/revit-ifc/issues/963); [GitHub revit-ifc #1015](https://github.com/Autodesk/revit-ifc/issues/1015) |
| 6 | Big or heavy files and viewers: freezing, crashing, blank or white model | 235 / 44 | "IFC Files do not open (Filesize??)", "Loading big IFC model crashes application" | [GitHub IfcOpenShell #7632](https://github.com/IfcOpenShell/IfcOpenShell/issues/7632); [GitHub That Open components #515](https://github.com/ThatOpen/engine_components/issues/515) |
| 7 | Checking a file: is it valid, does it meet the client's requirements (IDS), who can say pass/fail | 172 / 86 | "IfcTester not properly check PredefinedType", "How to validate IDS files?" | [OSArch](https://community.osarch.org/discussion/3478/ifctester-not-properly-check-predefinedtype-requirements); [GitHub IDS #189](https://github.com/buildingSMART/IDS/issues/189) |
| 8 | Coordinates, georeferencing and units: model far from origin, wrong position, feet vs mm | 152 / 48 | "Export IFC - wrong position !", "lands in the ocean in QGIS" | [Autodesk forum](https://forums.autodesk.com/t5/civil-3d-forum/export-ifc-wrong-position/td-p/11945739); [OSArch](https://community.osarch.org/discussion/3037/ifc-to-qgis-geopackage) |
| 9 | Spaces, storeys and spatial structure: rooms missing or at the wrong level | 146 / 71 | "Elements are being exported to the wrong IFC level" | [Autodesk forum](https://forums.autodesk.com/t5/revit-architecture-forum/elements-are-being-exported-to-the-wrong-ifc-level/td-p/11927737) |
| 10 | Clash, BCF and change tracking: GUIDs regenerated, clash lists too long | 138 / 58 | "IfcGuid behaviour change", "how would you group clashes and handle GUID churn?" | [GitHub revit-ifc #696](https://github.com/Autodesk/revit-ifc/issues/696); [OSArch](https://community.osarch.org/discussion/3616/browser-based-ifc-clash-version-diff-how-would-you-group-clashes-and-handle-guid-churn) |
| 11 | Quantities and cost: areas and volumes that do not match, takeoff from IFC | 135 / 55 | "GrossSideArea == NetSideArea", "Quantity cross-check" | [GitHub IfcOpenShell #9235](https://github.com/IfcOpenShell/IfcOpenShell/issues/9235); [OSArch](https://community.osarch.org/discussion/comment/27265) |
| 12 | Importing IFC into Revit: Link IFC vs Open IFC, position, elevation | 129 / 14 | "Link IFC fail", "Problem with Z coordinate when using Link IFC" | [GitHub revit-ifc #223](https://github.com/Autodesk/revit-ifc/issues/223); [GitHub revit-ifc #990](https://github.com/Autodesk/revit-ifc/issues/990) |
| 13 | Classification and handover: Uniclass, OmniClass, COBie tabs, FM data | 129 / 46 | "UNICLASS 2015 and Ifc", "Cobie export - systems tab empty" | [bSI forum](https://forums.buildingsmart.org/t/uniclass-2015-and-ifc/4423); [GitHub IfcOpenShell #6068](https://github.com/IfcOpenShell/IfcOpenShell/issues/6068) |
| 14 | Schema versions and views: IFC2x3 vs IFC4 vs IFC4.3, Coordination View vs Reference View vs Design Transfer | 122 / 22 | "Is the industry ready for IFC4?", "Why are material layer sets excluded from the Reference View?" | [BIM Corner blog](https://bimcorner.com/is-the-industry-ready-for-ifc4/); [bSI forum](https://forums.buildingsmart.org/t/3638) |
| 15 | Infrastructure with IFC 4.3: alignments, bridges, roads, which class to use | 122 / 37 | "IfcBridge or IfcRoad?", "alignment is not opening in Civil 3D" | [bSI forum](https://forums.buildingsmart.org/t/exporting-bridge-elements-to-ifc-4-3-ifcbridge-or-ifcroad/5811); [bSI forum](https://forums.buildingsmart.org/t/ifc-4x1-file-containing-alignment-is-not-opening-in-civil-3d/3830) |
| 16 | AI, LLM and MCP: connection problems, tool errors, "did it really do it?", trust in invented property names | 56 / 5 | "Connection issue", "Method not found", "Can you trust AI with IFC properties?" | [GitHub mcp-servers-for-revit #1](https://github.com/mcp-servers-for-revit/mcp-servers-for-revit/issues/1); [GitHub revit-mcp #28](https://github.com/mcp-servers-for-revit/revit-mcp/issues/28) |
| 17 | Learning IFC from zero | 33 / 15 | "How do I begin learning IFC?", "absolute beginner" | [bSI forum](https://forums.buildingsmart.org/t/ifc-schema/3540); [OSArch](https://community.osarch.org/discussion/3765/roadmap-for-revit-migrator-to-bonsai-bim-absolute-beginner) |

**Reading the gap (share of records carrying the tag, real vs synthetic).** Over-represented in the synthetic prompts: *guid_change_tracking* (3.3% vs 6.6%), *spatial_structure* (3.1% vs 5.7%), *validation_checking* (6.2% vs 10.0%), *quantities_qto* (5.7% vs 8.1%). These are the "check or count something in my model" jobs an MCP server is built for, so the synthetic set leans on them on purpose. Under-represented in the synthetic prompts: *export_revit* (15.4% vs 5.5%), *import_into_revit* (7.2% vs 2.3%), *viewers_opening* (6.3% vs 2.9%), *programming_ifcopenshell* (8.6% vs 3.7%), *revit_api_automation* (4.6% vs 1.3%). A tester should include both kinds: *tasks on a loaded model* and *help with an export or import that went wrong*.

**Person types behind the questions (real):** developer 597, BIM coordinator 443, architect 149, BIM manager 141, structural engineer 82, civil/infrastructure engineer 81, MEP engineer 79, student/beginner 66, estimator/QS 50, researcher 31. Facility managers, owners and authority reviewers are present but few; their voice is mostly in the synthetic set.


## Local ecosystem

English is the working language of several very different regimes. The facts below come from the KB's national documents (linked) and the regional research cells; statements marked *thin* rest on very little evidence.

| Region | What shapes the questions | Where to read more |
|---|---|---|
| **United States** | No national IFC mandate. Requirements come from each owner (GSA, USACE, state DOTs). COBie is the handover format people meet most; NBIMS-US version 4 includes COBie V3 (2023). Infrastructure is driven by FHWA/AASHTO work on bridges and the TPF-5(372) pooled-fund test suite. Imperial units, State Plane coordinates, OmniClass/Uniformat. Words: "DOT", "pay items", "stationing", "kerbs/curbs". | [USA and Canada](../../02_standards_regulations/national/north_america.md); real examples in groups C and E |
| **Canada** | *Thin.* BIM not mandatory nationally; buildingSMART Canada and an openBIM roadmap exist. No genuine Canadian user questions were found. | same document |
| **United Kingdom (and Ireland)** | ISO 19650 with the UK National Annex, delivered through the IMI Framework (imiframework.org). Uniclass 2015 classification, EIR/AIM/BEP vocabulary, COBie UK, British National Grid (EPSG:27700). Ireland has a milestone-based public-works mandate from 2024. The UK documents do not fix one IFC version: the EIR decides. | [UK and Ireland](../../02_standards_regulations/national/uk_ireland.md) |
| **Singapore** | CORENET X portal run by BCA and URA with other agencies; submissions are **IFC+SG** (written "IFC-SG" by many people): IFC4 Reference View plus Singapore property sets (`SGPset_*`), SVY21 / EPSG:3414 coordinates, and a Model Checker with codes such as IFC0000101 (unsupported IFC version or MVD) and IFC0000104 (invalid or incomplete data). Community tools for pre-checking exist on GitHub. Thresholds and dates changed in 2025-2026, so tests should not hard-code them. | [Singapore](../../02_standards_regulations/national/singapore.md) |
| **Australia / New Zealand** | *Thin.* The KB has no national document, and the UK/ANZ/India research cell found no post it could attribute to an Australian or NZ author. Seen only as hints: openers like "G'day all" (OSArch), a thread mentioning EPSG:28356 (an Australian map grid zone), and a synthetic prompt about "MGA zone 56". NATSPEC's BIM portal (bim.natspec.org) was noted but not read. | none yet |
| **India** | *Thin.* The same cell found no post attributable to an Indian author. One real thread (an India-based estimating-software vendor asking how to read IFC for buyers, [bSI forum](https://forums.buildingsmart.org/t/3953)). No national document. Non-native, polite, formal phrasing appears widely in the technical forums but cannot be tied to a country from the data. | none yet |
| **Middle East and Africa** | *Thin.* 3 real records. South Africa's cidb published a BIM adoption strategy 2025-2030 that names no IFC standard. Nothing usable was found for UAE, Saudi Arabia, Qatar, Nigeria or Kenya. Synthetic prompts assume "submit to the municipality tomorrow" pressure. | [cidb strategy](https://www.cidb.org.za/innovation/cidb-bim-adoption-strategy/) |

**Open source and enthusiasts (international, English-first):** IfcOpenShell and Bonsai (formerly BlenderBIM), the OSArch community, That Open Engine (web-ifc, fragments), xBIM (.NET), Autodesk's open-source `revit-ifc` exporter, the buildingSMART IDS and BCF repositories, and a growing set of MCP servers for Revit and IFC. See [libraries and toolkits](../../04_open_source/libraries_and_toolkits.md), [community projects](../../04_open_source/community_projects_and_enthusiasts.md), [MCP servers and AI tools](../../04_open_source/mcp_servers_and_ai_tools.md) and [Revit software notes](../../03_software/revit/).


## How people write

Evidence: the research reports for every English cell plus the 1,796 records themselves. Where a point rests on only a few records it is said so.

### Register, length and structure

- **Titles do the work.** The median real title is 7 words and often *is* the question: "Export IFC - wrong position !", "Link IFC fail", "Floors not exporting". Body text is usually 1-5 sentences plus a screenshot, a pasted error or an attached file.
- **GitHub reports** follow the template (Problem Description / Revit Version / Windows Version, or Bug Description / steps / environment) and are terse and exact. Version strings matter: "22.4.2 ok, 23.2.3 not ok".
- **Forum posts** (buildingSMART, Autodesk) are longer and politer; numbered sub-questions are common; some read like letters ("Dear IFC developers", "Good day").
- **Comparison with another tool** is the standard way to say "the file is fine": "works in BIMvision but not here", "opens fine in Solibri", "BIMcollab opens it".
- **Numbers instead of adjectives** from developers: "12MB: 222s vs 2s", "7,413,409 lines", "2 GB IFC, 16 GB RAM".
- **Synthetic prompts** (what an assistant user would type) are shorter than real posts: median 15 words, mostly lowercase, often no question mark (352 of 618 have none), with an urgent tone in 63 of 618 ("before the issue tonight", "need it for the coord meeting in an hour").

### Openers and closers

| Where | Typical openers | Typical closers |
|---|---|---|
| GitHub | none, or "Hi Team", "Hello, team!", "Dear XBim Team"; older posts "I wanted to reach out" | "Thanks in advance", "Thanks already!", "Thanks for your support!" |
| buildingSMART / Autodesk forums | "Hello everyone", "Hi all", "Hello IFC gurus", "Dear IFC developers", "Good day" | "Thank you in advance!", "Can anyone shed some light?", "Thanks" |
| OSArch | "G'day all", "Hi, I am an absolute beginner", "Hello community" | "Cheers", "hope it's not lost!", self-posted "[solved]" |
| Dynamo / pyRevit | "Hi all", "Hello" | "Thanks in advance", "weird error, cheers" |
| AI/MCP issues | none; sometimes "Dear authors" | quoting the assistant's reply back |

### Tone

Real tone is mostly *neutral* (524 of 1,796) with a large share of *frustrated* (407) and *confused* (402). Frustration is usually restrained: version-regression complaints ("fine in 2023/2024, broken in 2025-2027"), "unacceptable in a production environment", exclamation marks in the title ("crashes every time I export IFC!!!"), and self-deprecation ("Or am I just too stupid"). Forums skew *curious* (199 of 578); GitHub skews *neutral/frustrated*. Sceptical voices appear in opinion posts about IFC4, MVD, certification and AI ("Can you trust AI with IFC properties?"). People often admit their level: "absolute beginner", "newbie", "no coding experience", "ChatGPT and Gemini didn't help".

### What context people give, and what they leave out

| Usually given | Usually missing |
|---|---|
| Revit year or add-in version; Blender/Bonsai version; library version | IFC schema version and view (IFC2x3 / IFC4 / Reference View / Design Transfer) |
| A screenshot; a pasted traceback or validator message | The exporter settings; units; the file itself ("cannot share, confidential") |
| The other tool that works ("opens in BIMvision") | What the expected result is; which element ids are affected |
| Their role, sometimes ("I'm a land surveyor", "BIM coordinator") | Whether the problem is in the source model or the export |

Maintainers' standard reply is "please share the file" or "which version?". An assistant tested with these prompts should also ask, or read the header and report what it finds.

### Jargon and slang

Terms marked * appear mainly in the synthetic prompts, not in real records.

| Term as written | Meaning | Standard term |
|---|---|---|
| proxy, proxies, "painful BuildingElementProxy" | An object the exporter could not give a real class | `IfcBuildingElementProxy` |
| pset, ePset | Property set; ePset = extra set with an `EPset_` prefix (Bonsai custom sets, IFC2x3 georeferencing) | `IfcPropertySet` |
| Qto, QTO, "takeoff", BoQ | Quantities for pricing | `Qto_*BaseQuantities` / `IfcElementQuantity` |
| GUID | Element identity | `GlobalId` |
| mapping table, IfcExportAs | Revit setting that turns categories into IFC classes | IFC export class mapping |
| Link IFC / Open IFC | Two ways to bring IFC into Revit | n/a (Revit commands) |
| CV2 / CV2.0, RV, DTV | Coordination View 2.0, Reference View, Design Transfer View | MVD (Model View Definition) |
| IA | Implementation agreement (certification) | buildingSMART term |
| IDS, facet, applicability | Machine-readable requirements and their parts | Information Delivery Specification |
| EIR, OIR, AIM, BEP, MIDP | Client requirements and plans (UK usage) | ISO 19650 terms |
| "issue" / "the issue tonight" | Formal release of a model or file (UK) | information delivery |
| federate; "append"*, "coord meeting"* | Combine discipline models and review | coordination |
| PBP, survey point, "false origin", base point | Origin/coordinate reference points | project base point, survey point |
| BBIM, Bonsai, dailies | Bonsai (formerly BlenderBIM); nightly builds | n/a |
| frag, wasm, express ID | That Open fragments file; WebAssembly; STEP line id | n/a |
| CX, IFC+SG / IFC-SG, COP, SGPset | CORENET X, Singapore IFC, Code of Practice, Singapore pset | n/a |
| DOT, pay items, stationing, PI/PVI, state plane | US infrastructure vocabulary | n/a |
| kerb / curb | UK vs US spelling | n/a |
| navis*, ACC*, c3d* | Navisworks, Autodesk Construction Cloud, Civil 3D | n/a |
| MCP, tool call, "Method not found", agent | AI assistant tooling | Model Context Protocol |

### Misspellings and name variants (all seen in the data)

- **Typos in titles:** "Professioonals", "Documantation", "Quesion" / "dissappearing", "appartment" / "boudnary", "properites", "Informatoin", "effectivly", "swiching" / "avialable", "talkes", "Costum Export Setup", "Handeling Revitparameters", "allignment", "Strucutral", "Globel Id", "IfcOpenning", "COBIe", "expoted", "developpements".
- **Entity names:** typed in STEP style (IFCWALL, IFCRELAGGREGATES), in plural ("IfcBuildingElementProxies"), or all lowercase ("ifc4x3", "ifcalignment").
- **Product-name variants:** Bonsai = BlenderBIM = BBIM; IFC+SG = IFC-SG; "Navis" = Navisworks; "c3d" = Civil 3D; several unrelated repositories are all called some form of "revit mcp".
- **Capitalisation:** shouting titles ("IFC EXPORT PROBLEM", "REVIT 2026 Won't export to IFC?").
- **Punctuation and numbers:** decimal commas ("0,xx degrees"), "Mo" for MB (French), unit slips (feet vs mm).

### Code-switching and non-native English

Non-native English is **common** in the technical forums and GitHub, especially from Europe and Asia (the buildingSMART-forum report also names India; none of this can be proven per record, because records carry no country). Signs: "I wants to display...", "Couldn't able to export", "Hallo all", "vom" in an English title, German UI strings in Dynamo posts (e.g. "Leerrohr"), file names like "Gesamtmodell", French "Mo" for megabytes, Dutch and Norwegian words next to English tool names in GitHub titles. A typical non-native post is formal ("Dear authors", "Dear IFC developers", "Good day"), grammar is plain, and the message is short. Whether Indian, Gulf or African English has a distinct voice here could **not** be verified: no record is labelled by country.

### Voices by situation (short fragments from the data)

| Situation | Fragments |
|---|---|
| Frustrated coordinator | "Link IFC only hangs", "opens fine in other viewers", "I struggle with this for a year" |
| Developer | "Aborted()", "never completes", "Is there a fast way to do this?" |
| Beginner | "I am a beginner!!", "absolute beginner", "shed some light" |
| Regression complaint | "22.4.2 ok, 23.2.3 not ok", "broken since 2015" |
| Sceptic | "IMHO", "we (the BIM industry) have a problem", "IFC is not for visualisations or gaming" |
| AI user | quotes the assistant ("Method not found"), "tried apparently everything", "model confidently claimed success without persisted state" |


## Real questions

Each row is a **real** record (observed at the source). *Paraphrase* is the research agent's wording; *Title* is verbatim (shortened with "..." only if over 20 words). ◇ = snippet-level record (only title and search summary were seen, so the paraphrase is thin). † = the id is shared by two records; trust the link. Persona and tone are the KB's inference. "Note" says what the row teaches about phrasing or content, using the thread's answer where one was captured.


### A. Newcomers, beginners and non-native English

| # | Who · tone · year | Title (verbatim) | Paraphrase (KB) | Note | Source |
|---|---|---|---|---|---|
| R01 | student beginner · neutral · 2021 | IFC Schema | How do I begin learning IFC? I cannot find a structured guide online. | Broadest possible ask, no context at all. The thread answer pointed to buildingSMART implementation guidance. | [bSI forum](https://forums.buildingsmart.org/t/ifc-schema/3540)<br>`p-student-r018` |
| R02 | student beginner · confused · 2019 | IFC Documantation | Beginner asks why Assign model view is missing in IfcDoc as in the tutorial video, and for resources to learn IFC. | Typo in the title. Follows a video tutorial whose software UI no longer matches. | [bSI forum](https://forums.buildingsmart.org/t/ifc-documantation/1454)<br>`p-student-r017` |
| R03 | student beginner · curious · 2023 | IFC Schema Identifier | how can I tell whether a file is IFC2x3 or IFC4? File properties show nothing; only found out by opening in a viewer | Basic: how to tell IFC2x3 from IFC4. Poster only found out by opening a viewer (answer: read FILE_SCHEMA in the header). | [bSI forum](https://forums.buildingsmart.org/t/4802)<br>`en-bsforum-r013` |
| R04 | student beginner · confused · 2025 | I am a beginner!! I created a file in Bonsai but it doesn't appear correctly in 3D in Revit | House exported from Bonsai looks fine in Blender and some viewers, but in Revit wall heights and door/window positions are lost and elements vanish. Is there an export setting that fixes it? | Self-label plus double exclamation. File 'looks fine' in other viewers, wrong in Revit. | [OSArch](https://community.osarch.org/discussion/3280/i-am-a-beginner-i-created-a-file-in-bonsai-but-it-doesnt-appear-correctly-in-3d-in-revit)<br>`p-student-r002` |
| R05 | student beginner · polite · 2026 | Roadmap for Revit migrator to Bonsai BIM - absolute beginner | Long-time Revit user new to IFC and Bonsai asks for a learning roadmap and first steps while modelling a small timber house as practice. | Experienced Revit user, new to IFC: asks for a learning path, not a fix. | [OSArch](https://community.osarch.org/discussion/3765/roadmap-for-revit-migrator-to-bonsai-bim-absolute-beginner)<br>`en-osarch-r001` |
| R06 | architect · confused · 2022 | Couldn't able to export the IFC file | user cannot export the IFC file from Revit ◇ | Non-native grammar, no version, no cause. Snippet-level record. | [Autodesk forum](https://forums.autodesk.com/t5/revit-architecture-forum/couldn-t-able-to-export-the-ifc-file/m-p/11319947)<br>`es-latam-r007` |
| R07 | bim coordinator · confused · 2017 | Quesion: IFC mapping, dissappearing objects in export | an escalator family (generic model, class IfcBuildingElementProxy) does not show up in the exported IFC ◇ | Typos in the title. An escalator family silently becomes a proxy and disappears downstream. | [Autodesk forum](https://forums.autodesk.com/t5/revit-architecture-forum/quesion-ifc-mapping-dissappearing-objects-in-export/td-p/7181576)<br>`es-spain-r002` |
| R08 | civil infra engineer · confused · 2019 | Exporting a bridge vom Civil 3D/ Infraworks to Revit | Exporting a bridge from Civil 3D/InfraWorks to Revit. ◇ | German 'vom' leaks into an English title. Snippet-level record. | [Autodesk forum](https://forums.autodesk.com/t5/civil-3d-forum/exporting-a-bridge-vom-civil-3d-infraworks-to-revit/td-p/8841283)<br>`en-us-canada-infra-r023` |
| R09 | developer programmer · frustrated · 2025 | I wants to display an IFC file in windows form application using C# code | building an offline desktop app; ChatGPT code gives errors with xBIM assemblies | Run-on first-person title; admits ChatGPT-generated code fails against the library. | [GitHub xBIM #483](https://github.com/xBimTeam/XbimWebUI/issues/483)<br>`en-gh-xbim-others-r031` |
| R10 | bim coordinator · confused · 2023 | IFC mapping in Revit MEP | Hi all, new to IFC. I created a shared parameter named like the duct Pset Material attribute but it does not appear in the exported IFC. Can anyone shed some light? | 'Hi all, new to IFC'; asks someone to 'shed some light'. Shared parameter did not reach the IFC. | [bSI forum](https://forums.buildingsmart.org/t/ifc-mapping-in-revit-mep/4591)<br>`en-coord-r005†` |
| R11 | student beginner · confused · 2021 | "IFC Parameters" in Revit | land surveyor new to IFC; should instance parameters be grouped under IFC Parameters when exporting via IfcExportAs, mapping or Classification Manager | Land surveyor new to IFC, unsure how Revit parameter groups become property sets. | [bSI forum](https://forums.buildingsmart.org/t/ifc-parameters-in-revit/3854)<br>`en-bsi-r036` |
| R12 | bim coordinator · curious · 2026 | Bottlenecks faced by BIM Professioonals | what is the most annoying thing in your day to day bim work and how much time do you lose to it | Survey-style post with a typo in the title; no software, region or file. Zero replies. | [bSI forum](https://forums.buildingsmart.org/t/bottlenecks-faced-by-bim-professioonals/6633)<br>`en-mea-r002` |
| R13 | developer programmer · curious · 2020 | IFC - Questions from a beginner | New to BIM, building a Unity LCA app: where to learn IFC, do element IDs persist across exports, how to read IFC independent of authoring software? | Developer new to BIM: do element IDs persist between exports? Several questions in one post. | [bSI forum](https://forums.buildingsmart.org/t/ifc-questions-from-a-beginner/2515)<br>`p-student-r013` |
| R14 | student beginner · confused · 2025 | How Can i connect mistral or Llama with the revit MCP | one-line question | One-line question, odd capitalisation, no environment given. | [GitHub revit-mcp #26](https://github.com/mcp-servers-for-revit/revit-mcp/issues/26)<br>`en-aimcp-r021` |
| R15 | student beginner · polite · 2025 | Could you please provide a simple tutorial? | Dear authors..., assuming users are not very familiar with MCP | Very polite ('Dear authors'), assumes the user is not familiar with MCP. | [GitHub revit-mcp-plugin #5](https://github.com/mcp-servers-for-revit/revit-mcp-plugin/issues/5)<br>`en-aimcp-r022` |

### B. Revit IFC export and import (coordinators, BIM managers, architects)

| # | Who · tone · year | Title (verbatim) | Paraphrase (KB) | Note | Source |
|---|---|---|---|---|---|
| R16 | structural engineer · frustrated · 2018 | IfcExportAs Parameter doesn't work | Slab edges still export as IfcBuildingElementProxy even though an IfcExportAs parameter set to IfcSlab was added. ◇ | Title copies the Revit parameter name. Slab edges stay proxies; system families cannot take the parameter. Snippet-level. | [Autodesk forum](https://forums.autodesk.com/t5/revit-structure-forum/ifcexportas-parameter-doesn-t-work/td-p/8219179)<br>`en-autodesk-revit-export-r001` |
| R17 | bim coordinator · frustrated · 2020 | Revit IFC Export user defined properties won't export | Custom properties defined in the user-defined property set file do not appear in the exported IFC. ◇ | Classic 'my custom properties are missing'. Typical causes in the thread: txt format, wrong element scope, type vs instance. Snippet-level. | [Autodesk forum](https://forums.autodesk.com/t5/revit-architecture-forum/revit-ifc-export-user-defined-properties-won-t-export/td-p/9767878)<br>`en-autodesk-revit-export-r004` |
| R18 | bim manager · frustrated · 2026 | Ifc export in 2027 - mapping parameters severely lacking | The new Revit 2027 parameter mapping GUI replacing the pset.txt workflow lists only some parameters; project parameters are missing from the selection list, some classes show empty lists. ◇ | Complaint about a new mapping dialog. Autodesk acknowledged the empty-list problem as known. Snippet-level. | [Autodesk forum](https://forums.autodesk.com/t5/revit-architecture-forum/ifc-export-in-2027-mapping-parameters-severely-lacking/td-p/14229702)<br>`en-autodesk-revit-export-r008` |
| R19 | bim manager · urgent · 2024 | Revit 2024.3 Update - Revit crashes every time I export IFC!!! | After the 2024.3 update Revit crashes at every IFC export. ◇ | Three exclamation marks in the title; urgent tone. Fix reported: remove a conflicting add-in. Snippet-level. | [Autodesk forum](https://forums.autodesk.com/t5/revit-architecture-forum/revit-2024-3-update-revit-crashes-every-time-i-export-ifc/td-p/13030432)<br>`en-autodesk-revit-export-r030` |
| R20 | architect · confused · 2024 | Solved: "Ghost" Mullions in IFC Export | Mullions show up in the IFC that are not in the Revit model. ◇ | Elements in the IFC that are not in the model. Cause: duplicate or overlapping curtain walls. Snippet-level. | [Autodesk forum](https://forums.autodesk.com/t5/revit-architecture-forum/quot-ghost-quot-mullions-in-ifc-export/td-p/13056918)<br>`en-autodesk-revit-export-r023` |
| R21 | architect · frustrated · 2023 | Solved: Elements are being exported to the wrong IFC level | Elements land in the wrong IfcBuildingStorey. ◇ | Levels disagree between Project Base Point and Survey Point. Snippet-level. | [Autodesk forum](https://forums.autodesk.com/t5/revit-architecture-forum/elements-are-being-exported-to-the-wrong-ifc-level/td-p/11927737)<br>`en-autodesk-revit-export-r026` |
| R22 | bim manager · confused · 2020 | IFC Import - Link Vs Open | Asks for official feedback on the two import methods; Open yields in-place families without IFC data and cannot map classes for Tekla assembly sub-elements, Link duplicates geometry. | Asks for an 'official word' on two import paths that give different results. | [GitHub revit-ifc #223](https://github.com/Autodesk/revit-ifc/issues/223)<br>`en-autodesk-revit-import-r003` |
| R23 | bim coordinator · curious · 2021 | Is there a way to import an IFC using the Revit project base point as an origin? | Export offers internal origin, survey point or PBP; import offers nothing; cites an old Revit Ideas post saying it is not possible. | Feature gap since 2021; the thread says Link IFC gained a positioning option in Revit 2026. | [GitHub revit-ifc #320](https://github.com/Autodesk/revit-ifc/issues/320)<br>`en-autodesk-revit-import-r004` |
| R24 | other · frustrated · 2026 | PR: Link IFC fail | One chair family exports fine and displays in BIM Vision, but Revit cannot link it back; Link IFC just hangs. | 'PR:' prefix = problem report. Opens in BIM Vision but Revit hangs on the same file. | [GitHub revit-ifc #951](https://github.com/Autodesk/revit-ifc/issues/951)<br>`en-autodesk-revit-import-r002` |
| R25 | bim coordinator · frustrated · 2026 | PR: Problem with Z coordinate when using "Link IFC" | In 2025-2027 Link IFC positions geometry higher than it should be and creates levels at twice the correct elevation. Open IFC is fine. In 2023/2024 Z maps correctly to Project Base Point. | Version-comparison complaint: fine in 2023/2024, broken in 2025-2027. Confirmed by Autodesk. | [GitHub revit-ifc #990](https://github.com/Autodesk/revit-ifc/issues/990)<br>`en-autodesk-revit-import-r001` |
| R26 | mep engineer · frustrated · 2023 | Pipes / ducts / etc export using system material not actual material | Pipes export the pipe system material instead of their actual material such as PVC or copper. | Semantic complaint: pipe material is the system name, not copper/PVC. | [GitHub revit-ifc #577](https://github.com/Autodesk/revit-ifc/issues/577)<br>`en-gh-revit-ifc-r041` |
| R27 | developer programmer · neutral · 2026 | Beam System spacing exported as feet / 304.8 in mm project | In a millimetre project the Pattern pset of a Beam System writes spacing as feet divided by 304.8 when the value is a whole number of feet (0.0065 instead of 609.6). | Developer-grade bug report: unit conversion error in a millimetre project. | [GitHub revit-ifc #1015](https://github.com/Autodesk/revit-ifc/issues/1015)<br>`en-gh-revit-ifc-r001` |
| R28 | bim manager · frustrated · 2023 | INQ: IfcGuid behaviour change | Since Revit 2023 IfcGuid follows UniqueId so moving a door with Disjoin changes its GUID; can it be locked? | 'INQ:' prefix = inquiry. Since Revit 2023 the GUID follows the element's UniqueId, so some edits change it and tracking breaks. | [GitHub revit-ifc #696](https://github.com/Autodesk/revit-ifc/issues/696)<br>`en-gh-revit-ifc-r044` |
| R29 | bim coordinator · frustrated · 2023 | Revit to IFC, Wall is dislocated | exported Revit to IFC4 and one wall is dislocated; I struggle with this for a year - how to fix? | 'I struggle with this for a year'. Known bug for voided walls in IFC4 Reference View; IFC2x3 avoids it. | [bSI forum](https://forums.buildingsmart.org/t/revit-to-ifc-wall-is-dislocated/4575)<br>`en-coord-r004†` |
| R30 | bim coordinator · neutral · 2026 | INQ: Exporting parameters with empty values | is there a way to export parameters with empty values, maybe an IFC setting switch | Short, polite. Answer: empty parameters are not exported by design. | [GitHub revit-ifc #963](https://github.com/Autodesk/revit-ifc/issues/963)<br>`en-uk-anz-india-r014` |
| R31 | developer programmer · frustrated · 2026 | Are anyone able to export IFC using Dynamo in Revit 2027? | converted Python scripts to Revit 2027; IFC export scripts fail incl. custom export setups and basic doc.Export; generic PythonEvaluator error | Script broke after a Revit major version; question is shaped like a bug report. | [Dynamo forum](https://forum.dynamobim.com/t/are-anyone-able-to-export-ifc-using-dynamo-in-revit-2027/115000)<br>`en-dynamo-pyrevit-r003` |
| R32 | structural engineer · frustrated · 2026 | Angle / slope gets 0,xx degrees added | Typed 15 degrees exports as 15.35. | Decimal comma in the title; 15 degrees exports as 15.35. Unit conversion problem. | [GitHub revit-ifc #954](https://github.com/Autodesk/revit-ifc/issues/954)<br>`en-gh-revit-ifc-r058` |

### C. Classification, EIR, COBie and handover (UK and US flavour, one India-based voice)

| # | Who · tone · year | Title (verbatim) | Paraphrase (KB) | Note | Source |
|---|---|---|---|---|---|
| R33 | bim manager · skeptical · 2022 | UNICLASS 2015 and Ifc | implemented classification with IfcClassification; is there a guide to use UNICLASS 2015 properly, ideally sample IFC, and an existing mapping table? | UK classification question: wants a guide, a sample IFC and a mapping table. Sceptical tone. | [bSI forum](https://forums.buildingsmart.org/t/uniclass-2015-and-ifc/4423)<br>`en-bsi-r030` |
| R34 | bim coordinator · confused · 2022 | Classification manager values to IFC | Standard Data Tool creates number and description parameters; old way was 'number : description' giving Identification and Name; how to get good IFC with Classification Manager | Uniclass codes entered in Revit's Classification Manager do not land as Identification and Name in the IFC. | [GitHub revit-ifc #456](https://github.com/Autodesk/revit-ifc/issues/456)<br>`en-uk-anz-india-r006` |
| R35 | bim coordinator · neutral · 2023 | How to define Property requirements in an unknown/unstated PropertySet | EIRs often name a property but not its pset, while IDS requires the pset | EIRs name a property but not its property set; IDS needs both. The record mentions the UK BIM Framework template. | [GitHub IDS #189](https://github.com/buildingSMART/IDS/issues/189)<br>`en-bsforum-r050` |
| R36 | estimator qs · curious · 2022 | BBIM \| Classification in Cost Schedule Exported .csv | assigning a Uniclass 2015 reference to entities and cost items, how does classification appear in the cost CSV ◇ | Uniclass 2015 reference on model elements and cost items; how it shows in a CSV. Snippet-level. | [OSArch](https://community.osarch.org/discussion/2014/bbim-classification-in-cost-schedue-exported-csv)<br>`en-osarch-r026†` |
| R37 | owner client · curious · 2018 | How does IFC work with existing classification systems such as Omniclass, Uniformat, etc? | model as IfcDoor, classify with OmniClass, or both? will growing IFC entity vocabulary make OmniClass obsolete | 2018 concept question from an owner: classify with OmniClass or model as IfcDoor, or both? | [bSI forum](https://forums.buildingsmart.org/t/how-does-ifc-work-with-existing-classification-systems-such-as-omniclass-uniformat-etc/804)<br>`en-bsi-r032` |
| R38 | bim coordinator · frustrated · 2019 | Cobie to IFC export issues | Mapped COBie data to Revit parameters, exported with COBie 2.4 Design Deliverable setup, but COBie type/component names are missing from the IFC; do not want to remap. | COBie 2.4 setup exports without Type and Component names. Answer: export IFC4 first, then derive COBie from the IFC. | [bSI forum](https://forums.buildingsmart.org/t/cobie-to-ifc-export-issues/1860)<br>`en-us-canada-infra-r001` |
| R39 | facility manager · frustrated · 2022 | COBIE.Type.Length, COBIE.Type.Width, COBIE.Type.Height is always empty | COBIE.Type.Length, Width, Height always empty. ◇ | Facility-management voice: fields always empty. Answer: they are not auto-filled, map a length parameter. Snippet-level. | [Autodesk forum](https://forums.autodesk.com/t5/revit-architecture-forum/cobie-type-length-cobie-type-width-cobie-type-height-is-always/td-p/11009379)<br>`en-us-canada-infra-r027` |
| R40 | facility manager · confused · 2025 | Cobie export - systems tab empty | 214 systems in Bonsai but empty tab in spreadsheet | Bonsai lists 214 systems but the COBie systems sheet is empty. | [GitHub IfcOpenShell #6068](https://github.com/IfcOpenShell/IfcOpenShell/issues/6068)<br>`en-gh-ifcopenshell-r028` |
| R41 | facility manager · frustrated · 2025 | COBie export - missing Instruction, Impact, Coordinate, Issue, PickLists tabs | COBie spreadsheet exported from IFC (BIM Vision and Bonsai) lacks 5 of the 20 standard tabs; calls it a COBie nonconformity though the other 15 tabs have data | Counts tabs (5 of 20 missing), calls it a 'COBie nonconformity' and asks about the UK vs US template. | [GitHub IfcOpenShell #5926](https://github.com/IfcOpenShell/IfcOpenShell/issues/5926)<br>`en-uk-anz-india-r001` |
| R42 | owner client · curious · 2025 | Using IFC models for asset management | US state DOT with 500+ projects/year wants system-wide asset query (e.g., bridges with certain bearings and their age) from as-built IFC | US state DOT with 500+ projects a year wants to query assets across as-built IFC. Replies: use a database or GIS, not files. | [OSArch](https://community.osarch.org/discussion/comment/25545)<br>`en-cobie-r008` |
| R43 | estimator qs · polite · 2021 | Help regarding extracting/ importing data from IFC to Estimation software | India-based estimating software vendor (Masterformat, RS Means-style) is asked by buyers to link to design software; non-programmer wants to know how to read IFC data incl. Revit keynotes/parameters | India-based estimating-software vendor, non-programmer, asked by buyers to link to design tools. Polite, no code. | [bSI forum](https://forums.buildingsmart.org/t/3953)<br>`en-bsforum-r002` |

### D. Coordinates, units and georeferencing

| # | Who · tone · year | Title (verbatim) | Paraphrase (KB) | Note | Source |
|---|---|---|---|---|---|
| R44 | civil infra engineer · frustrated · 2024 | We have a problem with IfcMapConversion | two products write IfcMapConversion while also using projected coordinates as model coordinates, so double application gives wildly wrong positions; few tools read IfcMapConversion at all | Opinion-framed ('we have a problem'): two tools apply the same shift twice, few tools read the conversion. | [bSI forum](https://forums.buildingsmart.org/t/5695)<br>`en-bsforum-r025` |
| R45 | civil infra engineer · frustrated · 2025 | IFC to QGIS (GeoPackage) | Model georeferenced to EPSG:27700 in Bonsai lands in the ocean in QGIS after converting to GeoPackage. | Model georeferenced to EPSG:27700 (British National Grid) lands in the ocean in QGIS. Causes: mm vs m and a reader bug. | [OSArch](https://community.osarch.org/discussion/3037/ifc-to-qgis-geopackage)<br>`en-osarch-r017` |
| R46 | bim coordinator · neutral · 2025 | IFC clash returns location in mm when ifc project in feet | clash annotation shows far from objects because project units are feet | Imperial-units project; clash markers land far away because millimetres are assumed. | [GitHub IfcOpenShell #7178](https://github.com/IfcOpenShell/IfcOpenShell/issues/7178)<br>`en-gh-ifcopenshell-r008` |
| R47 | bim manager · curious · 2020 | IFC files that reference one another | How discipline IFC files can inherit georeferencing (IfcProjectedCRS EPSG:28356 + IfcMapConversion). ◇ | The record mentions EPSG:28356, a code used for an Australian map grid zone, with IfcMapConversion. Snippet-level. | [bSI forum](https://forums.buildingsmart.org/t/ifc-files-that-reference-one-another/1804)<br>`en-coord-r037` |
| R48 | civil infra engineer · frustrated · 2023 | Export IFC - wrong position ! | Export IFC - wrong position. ◇ | Civil 3D export lands in the wrong place; answer: Civil 3D uses absolute coordinates, Revit a base point. Snippet-level. | [Autodesk forum](https://forums.autodesk.com/t5/civil-3d-forum/export-ifc-wrong-position/td-p/11945739)<br>`en-us-canada-infra-r025` |

### E. Infrastructure and bridges (US DOT flavour)

| # | Who · tone · year | Title (verbatim) | Paraphrase (KB) | Note | Source |
|---|---|---|---|---|---|
| R49 | civil infra engineer · curious · 2024 | Exporting bridge elements to IFC 4.3: IfcBridge or IfcRoad? | Should wearing surface, kerbs, junction boxes go inside the IfcBridge model or in a separate IfcRoad model, and are there criteria? | Uses 'kerbs' and 'wearing surface'. Answer: everything between approach slabs is bridge except the asphalt wearing course. | [bSI forum](https://forums.buildingsmart.org/t/exporting-bridge-elements-to-ifc-4-3-ifcbridge-or-ifcroad/5811)<br>`en-us-canada-infra-r002` |
| R50 | civil infra engineer · confused · 2021 | IFC 4x1 file containing alignment is not opening in Civil 3D | Highway project; exported alignment as IFC 4x1, import into Civil 3D 2022 completes but nothing shows, even zoom extents. Ground and corridor surfaces worked with IFC 2x3. | 'Nothing visible even after Zoom Extents'. Answer: IFC 4.1 was withdrawn and never certified. | [bSI forum](https://forums.buildingsmart.org/t/ifc-4x1-file-containing-alignment-is-not-opening-in-civil-3d/3830)<br>`en-us-canada-infra-r003` |
| R51 | civil infra engineer · frustrated · 2026 | Why are IfcFeatureElement filtered out on IFC import? | US bridge IDM models shear keys as IfcProjectionElement; Bonsai import drops them | US bridge IDM models keep shear keys as IfcProjectionElement; the Bonsai importer drops them. | [GitHub IfcOpenShell #9433](https://github.com/IfcOpenShell/IfcOpenShell/discussions/9433)<br>`en-gh-ifcopenshell-r024` |
| R52 | civil infra engineer · frustrated · 2024 | Upgrading IFC4 into IFC4.3 file using Blender to use IfcRoad and related classes | how can I introduce IfcRoad and related classes instead of painful BuildingElementProxy to my IFC model? upgrade gives a python error | Emotive 'painful BuildingElementProxy' for roads; wants IfcRoad classes. | [GitHub IfcOpenShell #4921](https://github.com/IfcOpenShell/IfcOpenShell/issues/4921)<br>`en-civil-infra-r002` |

### F. Singapore (CORENET X): tool-README voice, not forum posts

These rows come from tool README files, not forum threads. The title is the KB label (repository name plus topic), and the paraphrase reconstructs the question the tool was built to answer. Use them for vocabulary (error codes, entity names, deadline pressure), not for human phrasing. For Singapore forum voice there is no real data yet.

| # | Who · tone · year | Title (verbatim) | Paraphrase (KB) | Note | Source |
|---|---|---|---|---|---|
| R53 | bim coordinator · frustrated · 2026 | IFC-Repair-Studio: IFC0000104 ContextOfItems | portal says IfcShapeRepresentation.ContextOfItems is required, code IFC0000104, which shape and how to fix without re-exporting | README-derived. Quotes the checker's error code and the missing attribute verbatim. | [GitHub noddlesskcho/IFC-Repair-Studio](https://github.com/noddlesskcho/IFC-Repair-Studio)<br>`en-sg-corenetx-r001` |
| R54 | architect · confused · 2026 | IFC-Repair-Studio: IFC0000101 not IFC4 | got IFC0000101 update file to supported IFC version, I exported ifc2x3, how to export ifc4 with IFC+SG settings | README-derived. Exported IFC2x3 by mistake; the portal needs IFC4. | [GitHub noddlesskcho/IFC-Repair-Studio](https://github.com/noddlesskcho/IFC-Repair-Studio)<br>`en-sg-corenetx-r003` |
| R55 | bim coordinator · frustrated · 2026 | IFC-Repair-Studio: empty IfcClosedShell | IfcClosedShell.CfsFaces must not be empty from the checker, IFCCLOSEDSHELL(()) in file, what to do | README-derived. STEP fragment pasted instead of a description. | [GitHub noddlesskcho/IFC-Repair-Studio](https://github.com/noddlesskcho/IFC-Repair-Studio)<br>`en-sg-corenetx-r002` |
| R56 | structural engineer · neutral · 2026 | ifcsg-precheck: units as text | ClearWidth is '1000 mm' text and FireRating '1 hr', mapping wants number, how to bulk fix | README-derived. '1000 mm' and '1 hr' stored as text where numbers are required. | [GitHub LUOaini1213/ifcsg-precheck](https://github.com/LUOaini1213/ifcsg-precheck)<br>`en-sg-corenetx-r006` |
| R57 | bim coordinator · curious · 2026 | ifcgref-corenetx geo-reference check | is my ifc georeferenced to SVY21 EPSG 3414, do i need SITEBOUNDARY IfcGeographicElement | README-derived, lowercase. Asks if the model is on SVY21 (EPSG:3414) and has a site boundary object. | [GitHub chunyen93/ifcgref-corenetx](https://github.com/chunyen93/ifcgref-corenetx)<br>`en-sg-corenetx-r008` |

### G. Developers and open-source users

| # | Who · tone · year | Title (verbatim) | Paraphrase (KB) | Note | Source |
|---|---|---|---|---|---|
| R58 | developer programmer · curious · 2022 | Strategies on dealing with large IFC datasets | 2 GB IFC from Synchro, 16 GB RAM, open() runs out of memory; asks about lazy loading, renumbered STEP, or another storage tech | Numbers instead of adjectives: 2 GB file, 16 GB RAM. | [GitHub IfcOpenShell #2025](https://github.com/IfcOpenShell/IfcOpenShell/issues/2025)<br>`en-gh-ifcopenshell-r002` |
| R59 | developer programmer · curious · 2026 | Best practices for extracting accurate Length, Thickness, and Height (Bounding Box) for quantity takeoff without rotation distortion? | building a QTO viewer table; bounding box from geometry is distorted by world rotation; asks if USE_WORLD_COORDS False is right | Developer building a quantity table; bounding boxes distorted by rotation. | [GitHub IfcOpenShell #8102](https://github.com/IfcOpenShell/IfcOpenShell/discussions/8102)<br>`en-gh-ifcopenshell-r015` |
| R60 | developer programmer · confused · 2026 | Struggling to define semantic rules in IFC processing (balconies, facades, etc.) how do you approach ambiguity? | geometry deterministic but semantics ambiguous: what is a balcony, which elements belong, facade vs exterior wall | Reflective: geometry is deterministic, meaning is not (what is a balcony?). | [GitHub IfcOpenShell #7912](https://github.com/IfcOpenShell/IfcOpenShell/discussions/7912)<br>`en-gh-ifcopenshell-r017` |
| R61 | developer programmer · frustrated · 2024 | Loading big IFC model crashes application | loading a big ifc my browser crashes; same model loads in the web-ifc demo; cannot share the model | Cannot share the model; compares to a demo that works. | [GitHub That Open components #515](https://github.com/ThatOpen/engine_components/issues/515)<br>`en-gh-thatopen-r029` |
| R62 | bim coordinator · frustrated · 2026 | IFC model materials/colors not applied - all geometry renders white | all geometry renders entirely white regardless of materials in the IFC, colours visible in BIMvision are absent in the web viewer | 'Works in BIMvision but not here' pattern. Finding: the files had no colour entities at all. | [GitHub That Open components #745](https://github.com/ThatOpen/engine_components/issues/745)<br>`en-gh-thatopen-r034` |
| R63 | developer programmer · frustrated · 2025 | CreateContext hits 100% CPU and never completes on specific IFC models | hang in Xbim3DModelContext.CreateContext on a sample IFC; other viewers fine | Names the exact API call; other viewers open the file. | [GitHub xBIM #569](https://github.com/xBimTeam/XbimGeometry/issues/569)<br>`en-gh-xbim-others-r022` |
| R64 | developer programmer · confused · 2024 | How to find out what a IfcBuildingElementProxies is | reading IFC into an own system; proxies appear that are really walls or doors; is there a generic way to detect what a proxy is rather than one converter per CAD workflow? | Plural of an entity name; wants a generic way to guess what a proxy really is. | [bSI forum](https://forums.buildingsmart.org/t/5130)<br>`en-bsforum-r016` |
| R65 | developer programmer · frustrated · 2023 | A number of interesting Revit IFC parsing errors. | Revit-generated IFC4 (ODA toolkit) fails a strict parser: odd date format, extraneous parentheses in list elements of IFCCARTESIANPOINTLIST; also fails in ArchiCAD but not in BlenderBIM | Understated tone ('interesting') for hard failures in a strict parser. | [bSI forum](https://forums.buildingsmart.org/t/4605)<br>`en-bsforum-r011` |
| R66 | student beginner · confused · 2026 | IFC Files do not open (Filesize??) | downloaded BIM4LCA sample IFCs; bigger ones freeze Bonsai with no error; BIMcollab opens them | Question marks in the title. Cause found by the poster: one handwash basin held half of all polygons. | [GitHub IfcOpenShell #7632](https://github.com/IfcOpenShell/IfcOpenShell/issues/7632)<br>`en-gh-ifcopenshell-r003` |
| R67 | bim coordinator · neutral · 2026 | Opening Cuts Skipped in Bonsai Studio 0.9 | G'day all, when I open IFC from Revit (and one from ArchiCAD) I get Opening Cuts Skipped; Apply Openings fixes it. Bug or intended? It did not happen in earlier versions. | Opens with 'G'day all'. Asks 'bug or intended?' about Revit and Archicad files. | [OSArch](https://community.osarch.org/discussion/3754/opening-cuts-skipped-in-bonsai-studio-0-9)<br>`en-coord-r013†` |

### H. Checking, IDS, clash and quantities

| # | Who · tone · year | Title (verbatim) | Paraphrase (KB) | Note | Source |
|---|---|---|---|---|---|
| R68 | bim coordinator · confused · 2024 | Requiring the existence of Predefined Type | needs IDS 1.0 syntax requiring a valid PredefinedType on IfcCovering occurrence or type, as previously done in mvdXML from BIMQ; unsure if authoring tool output is valid; xBIM service gives Error 502 | Migrating a check from an older rule format to IDS; unsure if the authoring tool output is valid. | [bSI forum](https://forums.buildingsmart.org/t/5760)<br>`en-bsforum-r028` |
| R69 | bim coordinator · confused · 2026 | IfcTester not properly check PredefinedType requirements | IDS rule restricting IfcBeam PredefinedType to BEAM or PILECAP passes only one of six beams; user asks if this is a bug in IfcTester or a misunderstanding of IDS. | 'Bug in the tool or a misunderstanding of IDS?' Passes one of six beams. | [OSArch](https://community.osarch.org/discussion/3478/ifctester-not-properly-check-predefinedtype-requirements)<br>`en-osarch-r007` |
| R70 | bim coordinator · frustrated · 2024 | IfcTester - Script for testing several IFCs with several IDS | needs to check around 70 IFC models against 6 IDS files (specific pairs), export ODS/HTML/BCF reports; no coding experience, ChatGPT did not help, only PyPI docs; dreads manual repetition | No coding experience, ChatGPT did not help; 70 models against 6 IDS files. | [OSArch](https://community.osarch.org/discussion/2273/ifctester-script-for-testing-several-ifcs-with-several-ids)<br>`en-fmor-r004` |
| R71 | bim coordinator · polite · 2025 | Filtering "New" Building Components in IDS for Refurbishment Projects | agreed with client to deliver information only for new elements in scope, but mixed elements (old wall with new void) cannot be split; wants a global filter across all IDS specs on a project pset value 'New' | Refurbishment: mixed old/new elements cannot be split cleanly. | [OSArch](https://community.osarch.org/discussion/2969/filtering-new-building-components-in-ids-for-refurbishment-projects)<br>`en-fmor-r002` |
| R72 | bim coordinator · curious · 2025 | Clash detection: How to? | want clash sets and BCF projects. six steps: pick first file and filters, second file, output ifc, run; 0 clashes found even with deliberate clash. also false clashes, check multiple linked models, BCF viewpoints with snapshots | Six numbered steps, then '0 clashes found' even with a deliberate clash. | [OSArch](https://community.osarch.org/discussion/2736/clash-detection-how-to/p1)<br>`en-clash-r009` |
| R73 | bim coordinator · curious · 2026 | Browser-based IFC clash + version diff: how would you group clashes and handle GUID churn? | Is system x storey x source object the right granularity for clash lists? When Revit regenerates GlobalIds a GUID-only diff shows everything deleted and recreated - any heuristic that holds on real exports? Do non-viewer users want a PDF/HTML change log or is BCF enough? | Coordinator pain: hundreds of clashes from one duct run, GUIDs regenerated on every export. | [OSArch](https://community.osarch.org/discussion/3616/browser-based-ifc-clash-version-diff-how-would-you-group-clashes-and-handle-guid-churn)<br>`en-coord-r009†` |
| R74 | estimator qs · neutral · 2026 | Bug: GrossSideArea == NetSideArea in Bonsai QTO | compares QTO with Solibri table | Estimator compares against Solibri's table. | [GitHub IfcOpenShell #9235](https://github.com/IfcOpenShell/IfcOpenShell/issues/9235)<br>`en-gh-ifcopenshell-r034` |
| R75 | estimator qs · confused · 2026 | BOQ extraction using Python Code - Civil & Structure | count beams correctly but cannot get dimensions | Counts beams correctly but cannot get dimensions. | [GitHub IfcOpenShell #7540](https://github.com/IfcOpenShell/IfcOpenShell/discussions/7540)<br>`en-gh-ifcopenshell-r021` |
| R76 | estimator qs · frustrated · 2025 | Quantity cross-check | Cost rows are not one-to-one with model quantities (installation rows skipped, others split); wants not to build in-house. | Cost rows do not map one-to-one to model quantities; wants a ready-made tool. | [OSArch](https://community.osarch.org/discussion/comment/27265)<br>`en-data-r031` |
| R77 | student beginner · curious · 2024 | Which Software to create lists of quantities of the used building materials | Measuring in PDF for life cycle assessment; want IFC takeoff tool, free if possible. | Student doing life-cycle assessment, measuring in PDF today; asks for a free takeoff tool. | [bSI forum](https://forums.buildingsmart.org/t/which-software-to-create-lists-of-quantities-of-the-used-building-materials/5181)<br>`en-data-r023` |

### I. Complaints and opinions

| # | Who · tone · year | Title (verbatim) | Paraphrase (KB) | Note | Source |
|---|---|---|---|---|---|
| R78 | bim manager · frustrated · 2020 | What I don't like about IFC | why is it IFC2x3, IFC4add1, TC1 - what happened to number three? and why is the documentation so hard to navigate? | Blog title in complaint voice: version names, hard-to-navigate docs. The author still defends IFC. | [BIM Corner blog](https://bimcorner.com/what-i-dont-like-about-ifc/)<br>`en-blogs-linkedin-r019` |
| R79 | bim manager · frustrated · 2021 | Why are material layer sets excluded from IFC4 Reference View MVD? | material layers are fundamental; the Reference View excludes them so he cannot specify it in contracts | Contract-minded: cannot demand material layers if the view omits them. | [bSI forum](https://forums.buildingsmart.org/t/3638)<br>`en-bsforum-r044` |
| R80 | reviewer authority · frustrated · 2019 | Difference between expectations and reality of IFC Standards | Revit exports similar walls inconsistently as IfcWall or IfcWallStandardCase; layer data missing for thermal analysis; questions how interoperability can claim success. | Reviewer sceptical that 'interoperability' works when walls arrive as IfcWall or IfcWallStandardCase at random. | [bSI forum](https://forums.buildingsmart.org/t/difference-between-expectations-and-reality-of-ifc-standards/1040)<br>`p-student-r015` |
| R81 | architect · frustrated · 2026 | Bonsai 0.9 & Blender 5.2.2 new Void system improved until ist was broken? | Can no longer make arbitrary opening shapes; edits lost in IFC Edit mode and Blender crashes outside it. Argues software should warn about IFC limits. | Typo ('ist') in a frustrated title: a feature got 'improved until it was broken'. | [OSArch](https://community.osarch.org/discussion/3685/bonsai-0-9-blender-5-2-2-new-void-system-improved-until-ist-was-broken)<br>`en-osarch-r025†` |
| R82 | bim manager · skeptical · 2022 | Is the industry ready for IFC4? | IFC4 exports lose geometry, change property sets and show glitches; should we switch from IFC2x3? | Blog: IFC4 exports lose geometry and change property sets; verdict was to stay on IFC2x3 for now. | [BIM Corner blog](https://bimcorner.com/is-the-industry-ready-for-ifc4/)<br>`en-blogs-linkedin-r022` |

### J. AI, LLM and MCP users

| # | Who · tone · year | Title (verbatim) | Paraphrase (KB) | Note | Source |
|---|---|---|---|---|---|
| R83 | architect · frustrated · 2026 | Connection issue | Claude replies: unable to connect to Revit... will create a 10-meter wall once connected; port 8080 opened, no luck | Quotes the assistant's own reply back ('unable to connect to Revit'); port number given. | [GitHub mcp-servers-for-revit #1](https://github.com/mcp-servers-for-revit/mcp-servers-for-revit/issues/1)<br>`en-aimcp-r003` |
| R84 | developer programmer · neutral · 2026 | All mutating tools fail with 'An error occurred invoking' | revit_create_level {elevation:900,name:'GL+900'} returns isError; reads like get_current_view_info work | Read tools work, write tools fail; reporter found tool arguments lost per call. | [GitHub rvt-mcp #21](https://github.com/bimwright/rvt-mcp/issues/21)<br>`en-aimcp-r005` |
| R85 | mep engineer · frustrated · 2025 | Keep getting 'Method XXX not found' errors despite MCP server and Revit plugin working | list all pipes in the revit model -> Get element information failed: Method not found | Pastes the exact tool error; cause was version mismatch between server and plugin. | [GitHub revit-mcp #28](https://github.com/mcp-servers-for-revit/revit-mcp/issues/28)<br>`en-aimcp-r020` |
| R86 | student beginner · confused · 2026 | Basic (MEP) IFC file cannot be opened | header says originating_system OpenAI; IfcProject has 8 attributes instead of 9 (Phase missing) | An LLM-written IFC fails in Bonsai (missing attribute). Advice: validate and loop until it passes. | [GitHub IfcOpenShell #7945](https://github.com/IfcOpenShell/IfcOpenShell/issues/7945)<br>`en-aimcp-r013` |
| R87 | bim coordinator · neutral · 2026 | Proposal: opt-in idempotency for mutating tool calls | Claude Code ~60s client timeout during batch element creation; duplicate elements | Client timeout during batch creation produced duplicate elements. | [GitHub tapir-archicad-MCP #23](https://github.com/SzamosiMate/tapir-archicad-MCP/issues/23)<br>`en-aimcp-r019` |
| R88 | architect · polite · 2026 | Feature request: Add a tool to capture the current view as an image (for AI vision) | put the sofa here, by the window; verify a change actually looks correct | Wants the AI to look at the result ('put the sofa here, by the window'). | [GitHub revit-mcp-server #16](https://github.com/LuDattilo/revit-mcp-server/issues/16)<br>`en-aimcp-r017` |
| R89 | bim manager · skeptical · 2026 | Can you trust AI with IFC properties? 4 ways it makes them up | AI gave me Pset_BuildingElementCommon and put IsExternal on footings; how do I know which property sets are real? | Sceptical blog: AI invents Pset names and attaches IsExternal to footings. | [BIM Corner blog](https://bimcorner.com/ai-ifc-properties/)<br>`en-blogs-linkedin-r002` |
| R90 | architect · curious · 2026 | Claude Bonsai Construction Drawings | Revit veteran testing an AI assistant on Blender/Bonsai construction drawings; wants it to read redlines and update model and sheets, and asks how others balance 3D versus 2D detailing (sections, tags, callouts, lineweights, styles). | Revit veteran testing an AI assistant on drawings; mentions redlines and 3D vs 2D balance. | [OSArch](https://community.osarch.org/discussion/3783/claude-bonsai-construction-drawings)<br>`en-osarch-r002` |
| R91 | bim coordinator · curious · 2026 | Connecting agent to Pyrevit MCP - newbie | connected Claude to pyRevit MCP; want a free agent for pyRevit 7 to duplicate and rename sheets; tried Gemini API with Continue and local Ollama qwen2.5, didn't work | Self-labelled newbie; lists failed attempts (Gemini API, local Ollama model). | [pyRevit forum](https://discourse.pyrevitlabs.io/t/connecting-agent-to-pyrevit-mcp-newbie/10627)<br>`en-revit-auto-r022` |

## Ready test prompts

All prompts here are **synthetic** (written to imitate the voices above); none is a real quote. Unmarked prompts are taken verbatim from the KB's synthetic records; look the id up in the raw files to see its `inspired_by` list of real records. Prompts marked **R** are rewritten or newly combined for this file, each derived from the listed records. Fields: **Intent** (KB vocabulary), **Diff.** E/M/H (easy/medium/hard), **File?** whether a loaded IFC or Revit model is assumed, **Expected behaviour** (what a good assistant should do, and what it should not claim).

General expectations for every prompt that needs a model: read before writing, say which tool or data the answer came from, report counts with ids or GlobalIds, say "unknown" when data is missing instead of guessing, and never state that a regulator or checker will accept the file.


### 1. Singapore (CORENET X / IFC+SG)

Prompts imitate people who work against the Singapore portal's Model Checker. Terse, lowercase, deadline pressure. Rule details are in [Singapore](../../02_standards_regulations/national/singapore.md).

| # | Prompt (synthetic) | Intent | Diff. | File? | Expected behaviour |
|---|---|---|---|---|---|
| P01 | cx submission tomorrow, checker gave IFC0000104. find shapes w/o ContextOfItems and empty IfcClosedShell in this ifc | validate_check | M | yes | Scan IfcShapeRepresentation without ContextOfItems and IfcClosedShell with empty CfsFaces; list GlobalIds and names; propose fixes without deleting elements.<br><sub>`en-sg-corenetx-s001`</sub> |
| P02 | is this file ifc4 or 2x3? corenet x only takes ifc4 right | validate_check | E | yes | Read FILE_SCHEMA header, state the version, confirm CORENET X IFC+SG expects IFC4, advise re-export if not.<br><sub>`en-sg-corenetx-s002`</sub> |
| P03 | check georef - SVY21 3414? and is there a SITEBOUNDARY object | validate_check | M | yes | Inspect IfcMapConversion / IfcProjectedCRS name for EPSG:3414, find IfcGeographicElement with ObjectType SITEBOUNDARY, verify site placement plausible for Singapore and units.<br><sub>`en-sg-corenetx-s003`</sub> |
| P04 | which elems arent assigned to a storey? only building/site level | validate_check | M | yes | Walk IfcRelContainedInSpatialStructure, list elements whose container is IfcBuilding or IfcSite or none, grouped by class; also check duplicate storey names/elevations.<br><sub>`en-sg-corenetx-s005`</sub> |
| P05 | list spaces with no geometry or area 0, with guid so i can find them in revit | query_model_data | M | yes | Find IfcSpace with no Representation, zero NetFloorArea or height; output name, number, GlobalId, likely cause.<br><sub>`en-sg-corenetx-s008`</sub> |
| P06 | new to corenet x, how do i set up revit for ifc-sg export? template? shared params? ifc4? | how_to | M | no | Explain loading IFC+SG template/shared parameters, IFC4 export setup, class mapping, then running the Model Checker; note to check current official guidance.<br><sub>`en-sg-corenetx-s013`</sub> |
| P07 **R** | got IFC0000101 from the checker. i think i exported 2x3 by mistake? can you confirm what schema this file is and tell me what to change in revit | troubleshoot_export | E | yes | Read the FILE_SCHEMA header and report IFC2X3 vs IFC4. Explain that the portal needs IFC4 (Reference View) with the IFC+SG setup, that the file cannot be repaired by editing, and that a re-export is required. Do not claim the file will pass.<br><sub>derived from en-sg-corenetx-r003, en-sg-corenetx-s002</sub> |

### 2. United Kingdom and Australia/NZ (ISO 19650, Uniclass, EIR)

UK-office shorthand ('before the issue tonight', 'P02 and P03'). The MGA zone 56 prompt is the only Australian-flavoured prompt in the KB. See [UK and Ireland](../../02_standards_regulations/national/uk_ireland.md).

| # | Prompt (synthetic) | Intent | Diff. | File? | Expected behaviour |
|---|---|---|---|---|---|
| P08 | check all elements have a Uniclass 2015 classification, Ss for systems and Pr for products. list the ones missing | validate_check | M | yes | Read IfcRelAssociatesClassification, group by classification source, list elements/types without Uniclass Ss or Pr reference, report counts by class.<br><sub>`en-uk-anz-india-s001`</sub> |
| P09 | EIR says all doors need FireRating, AcousticRating and Manufacturer. which ones dont have them? need before the issue tonight | validate_check | E | yes | Find IfcDoor/types, look in Pset_DoorCommon and any pset for the properties, report missing per door with names and levels.<br><sub>`en-uk-anz-india-s002`</sub> |
| P10 | compare P02 and P03 ifc - what walls got added, deleted or changed. by GlobalId | compare_versions | H | yes | Load both models, diff IfcWall by GlobalId, list added/removed/modified (property or geometry-level where possible).<br><sub>`en-uk-anz-india-s006`</sub> |
| P11 | got a spreadsheet mapping type names to Uniclass Pr codes. apply them to the types and save a new ifc | modify_model_data | H | yes | Read the mapping, create/associate IfcClassificationReference to matching types, write a new file, report unmatched types.<br><sub>`en-uk-anz-india-s008`</sub> |
| P12 | is this model georeferenced to MGA zone 56? check IfcMapConversion and the CRS name, project base point looks off | validate_check | M | yes | Read IfcMapConversion and IfcProjectedCRS, report eastings/northings/scale/rotation and whether CRS is EPSG:28356, flag inconsistencies.<br><sub>`en-uk-anz-india-s009`</sub> |
| P13 | client wants IFC per ISO 19650 EIR but doesnt say which one. 2x3 coordination view or IFC4 reference view? we are on Revit 2024 | troubleshoot_export | M | no | Explain differences, recommend asking the appropriate appointing party, suggest default (IFC4 Reference View for coordination, 2x3 CV2.0 if tools demand it), mention EIR clarification.<br><sub>`en-uk-anz-india-s012`</sub> |
| P14 | what do we actually need to hand over for asset info, COBie or IFC with psets? client's EIR just says 'AIM compatible' | how_to | E | no | Explain AIM under ISO 19650-3, COBie as spreadsheet/IFC subset, suggest defining required properties explicitly, advise clarifying the EIR.<br><sub>`en-uk-anz-india-s013`</sub> |
| P15 **R** | EIR says FireRating has to be in Pset_DoorCommon but our sub put it in a custom pset on some doors. find where each door's fire rating actually lives and flag any that have it in two places | validate_check | M | yes | Scan IfcDoor and door types for FireRating in Pset_DoorCommon and in any other pset; report per door where the value sits, list doors with it in both places or in neither, and say which values conflict. Do not pick a winner silently.<br><sub>derived from en-uk-anz-india-r013, en-fmor-s019</sub> |
| P16 **R** | g'day, can you check the map conversion on this one? supposed to be MGA zone 56 but the eastings look like they're in mm | validate_check | M | yes | Read IfcProjectedCRS and IfcMapConversion, compare the CRS name with EPSG:28356 (GDA94 / MGA 56) or EPSG:7856 (GDA2020 / MGA 56), whichever datum the project states, check the project length unit, and say whether the eastings/northings are plausible in metres or look 1000 times too large. Report the numbers and the unit used.<br><sub>derived from en-uk-anz-india-s009, en-gh-ifcopenshell-r008</sub> |

### 3. United States and Canada (COBie, DOT bridges, imperial units)

US owner and DOT wording: 'owe COBie to the owner Friday', 'pay item', 'state plane', 'USACE', 'GSA'. See [USA and Canada](../../02_standards_regulations/national/north_america.md).

| # | Prompt (synthetic) | Intent | Diff. | File? | Expected behaviour |
|---|---|---|---|---|---|
| P17 | we owe COBie to the owner friday. check the ifc for type names, component names, spaces w/o floor, systems empty. what will fail the QC | validate_check | M | yes | Verify Type/Component/Space/Floor/System population, list missing names and orphan spaces, summarize likely COBie QC failures.<br><sub>`en-us-canada-infra-s002`</sub> |
| P18 | this ifc lands miles away from the civil model. whats the IfcMapConversion / site lat-long and units? feet or meters? state plane? | query_model_data | M | yes | Report IfcProjectedCRS, IfcMapConversion, IfcSite ref lat/long, length unit, and diagnose likely offset cause.<br><sub>`en-us-canada-infra-s004`</sub> |
| P19 | list the IfcAlignments, their start/end stations, and tell me which elements use IfcLinearPlacement and at what station | query_model_data | H | yes | Enumerate IfcAlignment, horizontal/vertical segments, length, and elements with linear placement and distance along.<br><sub>`en-us-canada-infra-s005`</sub> |
| P20 | check this bridge ifc against our dot delivery reqs - every girder needs material, pay item no., and a predefined type. list failures by GlobalId | validate_check | M | yes | Validate required properties per element class (IDS-style), return failing GlobalIds with reasons.<br><sub>`en-us-canada-infra-s006`</sub> |
| P21 | pull rebar from the ifc - bar mark, size, length, count and total weight per pier. need it for the bid | extract_quantities | H | yes | Query IfcReinforcingBar elements, group by mark/diameter and containing pier, sum length and weight, flag missing quantities.<br><sub>`en-us-canada-infra-s007`</sub> |
| P22 | usace job wants COBie. do i export ifc then convert or use the cobie extension? which IFC version | how_to | M | no | Explain COBie Extension vs IFC-first workflows, recommend IFC4 COBie MVD, parameter mapping and QC; note project spec decides.<br><sub>`en-us-canada-infra-s011`</sub> |
| P23 | my get_volume numbers are off by 2% on elements at state plane coords. whats going on | troubleshoot_code | M | no | Explain precision loss far from origin, suggest translating vertices or using local coordinates.<br><sub>`en-us-canada-infra-s012`</sub> |
| P24 | upgrade this ifc4 to 4.3 and move the bridge proxies to IfcBridge stuff, keep guids | convert_format | H | yes | Upgrade schema, reclassify per mapping preserving GlobalIds, report changes.<br><sub>`en-us-canada-infra-s016`</sub> |
| P25 **R** | bridge model from our consultant is in feet and the clash markers land in the middle of nowhere. what units is the project in and does anything in there look like it assumes mm? | query_model_data | M | yes | Read IfcUnitAssignment (length unit and any conversion factor), compare placement magnitudes with the unit, and say whether the offset matches a feet/mm mix-up. State that clash coordinates must be converted before use; do not silently rescale the model.<br><sub>derived from en-gh-ifcopenshell-r008, en-us-canada-infra-s004</sub> |

### 4. Gulf, Africa and other non-native English (phrasing assumed, not evidenced)

The first six come from the KB's Middle-East/Africa cell, which found almost no real posts from the region (3 real records). The wording is therefore a plausible imitation. The two rewrites (R) add the formal, polite style often seen in non-native posts on forums.

| # | Prompt (synthetic) | Intent | Diff. | File? | Expected behaviour |
|---|---|---|---|---|---|
| P26 | need to submit this to the municipality tomorrow. can u check every wall, slab and door has a classification code + fire rating + level name filled? list whatever is missing | validate_check | M | yes | Iterate walls, slabs, doors; check classification references, Pset FireRating, and containing storey; return a grouped list of missing items with GlobalIds and counts; do not invent authority-specific rules.<br><sub>`en-mea-s001`</sub> |
| P27 | give me total concrete volume per level from the structural ifc, and confirm the units are m3 not mm3, the numbers look off | extract_quantities | M | yes | Read project length/volume units, sum NetVolume or Qto_*BaseQuantities for concrete elements per storey, flag unit scale issues, report table.<br><sub>`en-mea-s003`</sub> |
| P28 | model opens far from origin in the viewer. what coordinate system is it using? is there an IfcMapConversion, what are eastings northings | query_model_data | M | yes | Report IfcProjectedCRS and IfcMapConversion if present, else say absent; show site placement and bounding box; suggest fix.<br><sub>`en-mea-s006`</sub> |
| P29 | this ifc is 900MB and my laptop dies. what is making it so big? can we strip out the furniture and landscaping | troubleshoot_viewing | M | yes | Report element counts and geometry weight by class, identify heavy classes, offer a reduced copy without selected classes.<br><sub>`en-mea-s009`</sub> |
| P30 | client says deliver in IFC. ifc2x3 or ifc4? what is coordination view? im using revit 2023 | understand_concept | E | no | Explain IFC2x3 vs IFC4 and Coordination View vs Reference View; advise confirming with EIR; give Revit export setting names.<br><sub>`en-mea-s011`</sub> |
| P31 | windows are showing but wall openings are missing in the ifc from revit. walls solid. what setting | troubleshoot_export | M | yes | Check whether IfcOpeningElement and voids relations exist; advise on export options for openings and wall-hosted elements.<br><sub>`en-mea-s012`</sub> |
| P32 **R** | Hello, I received IFC file from structural consultant. How many columns and beams are there level wise, and which concrete grade is used? Thank you | query_model_data | M | yes | Count IfcColumn and IfcBeam per storey; read the material or grade from material association or psets; list elements with no grade instead of guessing; answer in plain language; mirroring the formality is not required.<br><sub>derived from en-mea-s010, en-uk-anz-india-s014</sub> |
| P33 **R** | pls check this ifc, my client say rooms not showing in his software. i only see Spaces. what is problem and how to correct in Revit | troubleshoot_export | M | yes | Check whether IfcSpace entities exist, whether they have geometry and areas, and how they relate to storeys. Explain that 'Rooms' in Revit become IfcSpace in IFC and that the viewer decides what it shows; suggest the Revit export option for room bounding elements only if relevant.<br><sub>derived from en-uk-anz-india-s011, en-autodesk-revit-export-r015</sub> |

### 5. Beginners, students and 'I just got this file'

Plain words, no entity names. The model has to translate. Matches the voices in Real questions, group A.

| # | Prompt (synthetic) | Intent | Diff. | File? | Expected behaviour |
|---|---|---|---|---|---|
| P34 | just got this ifc from my architect. what is even in it? like how many floors and what kind of stuff | understand_concept | E | yes | Report IFC schema version, project name, storeys, count of elements by class, in plain language.<br><sub>`en-beginner-qa-s001`</sub> |
| P35 | I dont have revit, whats the easiest free way to look at this ifc? no install if possible | find_tool | E | no | Suggest browser-based or free viewers, note limits; if a model is loaded offer a summary instead.<br><sub>`en-beginner-qa-s003`</sub> |
| P36 | why are so many things IfcBuildingElementProxy?? this came out of revit | validate_check | M | yes | Count proxies, group by ObjectType/category, suggest export mapping fixes.<br><sub>`en-beginner-qa-s005`</sub> |
| P37 | can i actually edit this ifc in revit or is it just a reference? tried open and link, different results | convert_format | M | no | Explain Link vs Open, in-place families, loss of parametrics; edits belong in the source model.<br><sub>`en-beginner-qa-s008`</sub> |
| P38 | opened the ifc and its blank/white?? file is 40mb | troubleshoot_viewing | M | yes | Check for geometry representations, units, far-away coordinates; report findings.<br><sub>`en-beginner-qa-s011`</sub> |
| P39 | is this file even valid ifc? my viewer complains | validate_check | M | yes | Parse and validate schema conformance, list errors, state IFC version.<br><sub>`en-beginner-qa-s015`</sub> |
| P40 | my prof says walls should be IfcWall but i see IfcWallStandardCase and some IfcWall, why? list which is which | query_model_data | M | yes | Count IfcWall vs IfcWallStandardCase, list examples, explain that StandardCase is the typical IFC2x3 Coordination View 2.0 output and that IFC4 exports use plain IfcWall (StandardCase is discouraged in newer IFC4 revisions; the exact version is unverified in this KB).<br><sub>`p-student-s002`</sub> |
| P41 | what is ObjectType vs the actual type of this wall? it shows the revit type name, is that the ifc type?? | query_model_data | M | yes | Show ObjectType, PredefinedType, IfcRelDefinesByType type entity for the selected wall; explain differences.<br><sub>`p-student-s003`</sub> |
| P42 | can you add a property set called Pset_Custom with a field Author to the slab named S-01? first time doing this so tell me what you did | modify_model_data | M | yes | Create pset and property on the named slab, save to new file, explain steps and entities created.<br><sub>`p-student-s006`</sub> |
| P43 **R** | hi, new to this. i exported ifc from revit 2024 and in navisworks nothing has any properties, is the file broken or did i click the wrong thing?? | troubleshoot_viewing | M | yes | Check how many elements carry property sets at all and which sets; check the schema and whether geometry-only export options might have been used. Explain in plain language, say what cannot be known without export settings, and avoid blaming the user.<br><sub>derived from en-navis-acc-s001, en-navis-acc-s014</sub> |

### 6. Coordinators and BIM managers (checking, clash, versions)

The largest group in real traffic. Typical lines: 'need it for the coord meeting', 'dont give me 300 lines'.

| # | Prompt (synthetic) | Intent | Diff. | File? | Expected behaviour |
|---|---|---|---|---|---|
| P44 | compare v3 and v4 of the struct ifc, what got added/deleted/moved? need it for the coord meeting in an hour | compare_versions | H | yes | Diff by GlobalId: added, removed, changed placement/properties; summarize.<br><sub>`en-reddit-s005`</sub> |
| P45 | arch ifc and struct ifc dont line up when appended, one is like 2km off. whats the placement/site origin in each? | query_model_data | H | yes | Report IfcSite/IfcMapConversion/placement and bounding box origin of each model, estimate offset vector, suggest fix at export.<br><sub>`en-navis-acc-s002`</sub> |
| P46 | before I push to ACC how many IfcBuildingElementProxy are in here and which categories | query_model_data | E | yes | Count proxies, group by ObjectType/Revit category, advise mapping.<br><sub>`en-navis-acc-s004`</sub> |
| P47 | ACC keeps saying new version but clash results reset, are GUIDs stable? check dups in this file | validate_check | M | yes | Detect duplicate GlobalIds within the file; explain that GUID changes across exports break issue tracking; cannot compare to prior version unless provided.<br><sub>`en-navis-acc-s005`</sub> |
| P48 | navis shows my ifc 1000x too big. what units is it in | query_model_data | E | yes | Report IfcUnitAssignment length unit and conversion; likely mm vs m mismatch.<br><sub>`en-navis-acc-s008`</sub> |
| P49 | any duplicate elements in the arch model? same class same spot, list them w/ guids | validate_check | H | yes | Detect elements of same class with near-identical placement/geometry or repeated GlobalId; list GUIDs, names, storeys.<br><sub>`en-model-checking-s001`</sub> |
| P50 | NL-SfB codes in here are all filled but are they actually valid codes?? check against the list | validate_check | H | yes | Extract classification codes, compare to a supplied code list, report invalid or malformed ones.<br><sub>`en-model-checking-s004`</sub> |
| P51 | clash ducts vs structural beams, 10mm tolerance, group by level. dont give me 300 lines for one duct run | coordinate_clash | H | yes | Run clash between duct segments/fittings and beams with tolerance, group by storey and system.<br><sub>`en-model-checking-s005`</sub> |
| P52 | are the 3 models on same coordinates? one seems to be 40 km off | validate_check | M | yes | Compare IfcSite RefLatitude/Longitude, IfcMapConversion and bounding box origins across models.<br><sub>`en-model-checking-s008`</sub> |
| P53 | archicad ifc into revit and slabs are gone, can u check if theyre even in the file | troubleshoot_import | M | yes | Check IfcSlab/IfcCovering count and representations in the file, report missing geometry items.<br><sub>`en-graphisoft-s003`</sub> |
| P54 | guids changed after re-export, clash issues cant track | troubleshoot_export | H | yes | Explain IFC ID persistence in Archicad, compare GUIDs between files, report matches by name/position.<br><sub>`en-graphisoft-s016`</sub> |
| P55 | did the base point export go via IfcMapConversion or IfcSite? need to know before linking into revit | validate_check | M | yes | Look for IfcMapConversion/IfcProjectedCRS and IfcSite placement/RefLatitude; report which is present with values.<br><sub>`en-tekla-s002`</sub> |
| P56 | linked tekla ifc in revit and everything is doubled, assembly + parts. how to avoid? | troubleshoot_import | M | no | Explain assembly plus sub-parts import; suggest excluding single-part assemblies or mapping assembly class to deleted category.<br><sub>`en-tekla-s012`</sub> |
| P57 | allplan IFC export - half my walls came out as proxy?? can u list what ifc class each wall got | convert_format | M | yes | List IfcWall vs IfcBuildingElementProxy counts, name affected elements, suggest Allplan attribute/IFC-type fixes.<br><sub>`en-allplan-vw-bentley-s001`</sub> |
| P58 **R** | which levels in this model have no rooms at all? and is any IfcSpace sitting above or below its own level, we had the offset problem again | validate_check | M | yes | Count IfcSpace per storey, list storeys with none, compare each space's Z position and height with its storey elevation, and list outliers with GlobalId and name. Report numbers, not impressions.<br><sub>derived from en-gh-revit-ifc-r024, en-gh-revit-ifc-r025</sub> |

### 7. Engineers, estimators, contractors, FM and owners

Role-specific asks. Several include a quiet distrust of the numbers ('I dont trust the slab areas').

| # | Prompt (synthetic) | Intent | Diff. | File? | Expected behaviour |
|---|---|---|---|---|---|
| P59 | pipes show material = system name (HOT WATER) not copper. can you list pipes and what material they actually have | query_model_data | M | yes | Read material associations for IfcPipeSegment, list names, point out system-name materials, suggest where real material may be in psets.<br><sub>`en-eng-s003`</sub> |
| P60 | gross side area = net side area on most walls here, but theres windows in them. are the openings actually modelled as voids or is it baked in the mesh? | validate_check | H | yes | Check IfcRelVoidsElement/IfcRelFillsElement for walls, compare Gross/NetSideArea, report walls where they match despite fills, explain the cause.<br><sub>`en-s002`</sub> |
| P61 | architect sent a 480mb ifc, site tablet chokes on it. whats the quickest way to get just the structure + level 2 to view on site | troubleshoot_viewing | E | no | Suggest splitting/filtering by class and storey, removing unused geometry/psets, or converting to a lighter format; offer to export a subset if a file is loaded.<br><sub>`en-s005`</sub> |
| P62 | I dont trust the slab areas in this model. recompute from geometry and compare with Qto_SlabBaseQuantities, show anything off by more than 2% | validate_check | H | yes | Compute geometry-based area, compare with stored quantities, list outliers with ratios.<br><sub>`en-s018`</sub> |
| P63 | which equipment in this model has no manufacturer or serial number? need it for handover friday | validate_check | M | yes | List IfcElement occurrences of equipment classes missing Pset_ManufacturerTypeInformation Manufacturer/ModelLabel and serial number; group by type and storey; output table.<br><sub>`en-fmor-s001`</sub> |
| P64 | run our IDS on the contractor model and give me a short fail list I can send back, grouped by discipline | validate_check | M | yes | Validate model against provided IDS, summarize failed specs with counts and example GUIDs, group by discipline/class, concise report.<br><sub>`en-fmor-s003`</sub> |
| P65 | cobie sheet comes out with empty System tab but the model has systems, why | troubleshoot_export | M | yes | Check whether systems are IfcSystem with members assigned, check exporter assumptions, suggest fixes.<br><sub>`en-fmor-s012`</sub> |
| P66 | c3d corridor export - how many proxies and what should they be, IfcPavement? IfcCourse? | query_model_data | M | yes | Count IfcBuildingElementProxy, group by name/ObjectType, propose IFC4.3 classes (IfcPavement, IfcCourse, IfcKerb) per group.<br><sub>`en-civil-infra-s002`</sub> |
| P67 | whats the diff between horizontal vertical and cant in ifcalignment, where does the 3d curve come from? | understand_concept | E | no | Explain the nested layout (horizontal, vertical, cant) and IfcGradientCurve / segmented reference curve representation.<br><sub>`en-civil-infra-s014`</sub> |

### 8. AI and MCP-style asks (Revit and IFC)

Prompts a person types to an assistant that has Revit or IFC tools attached. They stress verification, because real users report assistants claiming success without changing anything (see Real questions, group J).

| # | Prompt (synthetic) | Intent | Diff. | File? | Expected behaviour |
|---|---|---|---|---|---|
| P68 | check every door in the model for clear width >= 850mm, give me a list of failures with storey and GUID, dont guess if the data is missing | validate_check | M | yes | Run door width check, return PASS/FAIL/UNKNOWN with GlobalId, storey; mark missing widths UNKNOWN.<br><sub>`en-aimcp-s002`</sub> |
| P69 | the ifc you wrote wont open in bonsai, validate it and fix till it passes | validate_check | H | yes | Run schema validation, report errors such as wrong attribute counts, repair and re-validate.<br><sub>`en-aimcp-s003`</sub> |
| P70 | draw a 6m wall on level 2 from 0,0 to 6000,0 - make sure its really on level 2 and type is generic 200 | modify_model_data | M | yes | Resolve Level by name, wall type by name, create wall, read back level and elevation.<br><sub>`en-aimcp-s005`</sub> |
| P71 | can claude open ifc files directly or do i need an mcp server? which one for beginners | how_to | E | no | Explain IFC is not natively readable; need IFC MCP; recommend local read-only server.<br><sub>`en-aimcp-s017`</sub> |
| P72 | rename all floor plan views to 'L{level number}_{old name}' and skip anything already prefixed | automate_batch | M | yes | List floor plan views, compute names from GenLevel, skip already-prefixed, avoid duplicate-name clashes, apply in one transaction, report old->new table.<br><sub>`en-revit-auto-s001`</sub> |
| P73 | before issue tonight - list rooms not placed / not enclosed / redundant and doors with no tag. excel pls | validate_check | M | yes | Query rooms with Area==0 and Location null, redundant warnings, doors without tags in views; return grouped lists with element ids and offer an Excel/CSV export.<br><sub>`en-revit-auto-s003`</sub> |
| P74 | claude sees the revit mcp tools but every call says Method not found, revit 2026, what am I missing | troubleshoot_code | E | no | Explain plugin/server version mismatch, check Revit add-in loaded, port, server vs commandset, suggest listing tools and a simple read call.<br><sub>`en-revit-auto-s006`</sub> |
| P75 | whats the cheapest way to get an AI to do repetitive revit stuff, sheets/views/params? local model ok? | find_tool | E | no | Compare MCP servers for Revit and pyRevit, paid vs local models, note reliability and token cost, recommend starting small with read-only tasks.<br><sub>`en-revit-auto-s017`</sub> |
| P76 **R** | list all the walls on level 2 with whatever is in their Comments. then set Comments to TBC on the ones that are empty. dont touch anything else and tell me exactly what you changed | modify_model_data | M | yes | Read first and show the list. Apply the change only to walls on level 2 with empty Comments, change nothing else, read the values back after the write, and report the exact element ids changed. If a wall cannot be changed, say so.<br><sub>derived from en-aimcp-r038, en-aimcp-s005</sub> |
| P77 **R** | you said done but I opened the file and the wall is still on level 1. did it actually save? | report_bug | H | yes | Do not repeat the earlier claim. Re-read the wall's level and elevation from the model, report what is actually stored, find whether the write failed, was rolled back, or went to a different document, and retry only with the user's agreement.<br><sub>derived from en-aimcp-r002, en-aimcp-r005</sub> |

## Tips for generating authentic English prompts

**Do**

- Keep it short. A typical assistant request is one or two sentences, 8-25 words, lowercase start, little punctuation: "how many IfcBuildingElementProxy in here and what revit category did they come from".
- Use the **user's** words for things, not schema words: "doors", "floors", "rooms", "that pipe system", "the architect's file", "the contractor model". Add one precise term only when the persona would know it (coordinators say "proxy", "GUID", "pset"; estimators say "takeoff", "BoQ", "net area").
- Put the **reason or deadline** in: "before the issue tonight", "for the coord meeting in an hour", "client rejected it", "handover is Friday".
- Mention the **other tool** that behaves differently: "fine in BIMvision", "Navis shows it 1000x too big".
- Leave context out on purpose. Most real posts omit the schema version, units and exporter settings; test whether the assistant checks them.
- Vary voice by persona: coordinators terse and busy; architects describing what they see; estimators asking for numbers; students naming their level ("first time doing this so tell me what you did"); developers giving counts, versions and exact calls.
- Mix regional hooks only where the data supports them: Uniclass / EIR / "the issue" (UK), COBie / DOT / feet / state plane (US), CORENET X / IFC+SG / SVY21 (Singapore), "G'day" and an Australian map grid (Australia).
- Include false premises and half-right claims people actually make: "corenet x only takes ifc4 right", "is it just a reference?", "it opens in my viewer so the file must be fine".
- Include **trust-checking** follow-ups, because real AI users report assistants saying "done" with nothing saved: "did it actually save?", "dont guess if the data is missing".
- For non-native voices, use plain grammar slips and formal politeness ("Dear authors", "Good day", "Couldn't able to export"), but do not overdo them and do not attach a nationality to them.

**Don't**

- Don't write textbook questions ("Explain the difference between IfcRelAggregates and IfcRelNests") unless the persona is a developer or a student asking exactly that.
- Don't write long polished paragraphs for coordinators or site staff; real ones are short and a bit sloppy.
- Don't state the IFC version or exporter settings in every prompt; real users rarely do.
- Don't clean up spelling in every prompt. A few typos and a missing question mark are normal; keep entity names recognisable.
- Don't claim a country-specific rule as fact in a prompt (CORENET X thresholds, Irish milestones) without checking the national document; those dates changed recently.
- Don't present synthetic prompts as real quotes in any report. Use the real rows above only as paraphrases, with their links.
- Don't assume the Indian, Gulf or African English voice is documented here; it is **not**. The related prompts are plausible imitations.

**Judging answers (from what real threads showed)**

- A good answer says what is in the file (schema, units, counts) before explaining.
- It separates "the data is not in the model" from "the tool could not read it".
- It names the usual cause when the thread did: unit mix-ups (mm / m / feet), missing coordinates conversion, classes exported as proxies, Revit Link IFC vs Open IFC, empty parameters not exported, GUID changes between exports.
- It does not invent property set names (a documented AI failure in the data), and it checks IFC4 vs IFC2x3 before naming a class or pset.
- It does not promise portal acceptance (CORENET X, an owner's COBie QC) from its own checks.

