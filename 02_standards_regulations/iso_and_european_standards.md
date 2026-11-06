# ISO and CEN standards around IFC: 16739, 19650, 7817 (LOIN), 12006, 29481, 23386/23387, 21597, 10303

**Last researched: 2026-11-06** (fact-checked the same day; corrections are listed in [../_meta/qa/qa-standards-1.md](../_meta/qa/qa-standards-1.md))

## In plain words

IFC is only one piece of a family of standards. ISO 16739-1 defines the IFC data schema (the "vocabulary" of building objects). ISO 10303-11, -21 and -28 define the technology IFC is written in (the EXPRESS language, the `.ifc` text file, the XML form). ISO 19650 describes the project management process around the model: who asks for what information, who delivers it, and where it is stored. ISO 7817-1 (LOIN) says how to specify how much geometry, data and documentation each object needs at each milestone. ISO 12006, 23386/23387, 29481 and 21597 cover classification, property dictionaries, exchange-requirement documentation and document containers. For a QA tester: an MCP server that reads or edits IFC deals with ISO 16739 and 10303 directly; the other standards show up as the *reasons* behind user requests ("check the model meets our EIR", "does every wall have the required property?", "which LOD is this?").

How the pieces fit (one line each):

| Question the project asks | Standard that answers it | What it looks like in an IFC file or workflow |
|---|---|---|
| What are the object types and relations? | ISO 16739-1 (IFC) | `IfcWall`, `IfcRelAggregates`, `IfcPropertySet` ... |
| How is the data written down? | ISO 10303-21 (+ -11 schema language) | `ISO-10303-21;` header, `#123=IFCWALL(...)` lines |
| Who delivers what, when, where is it stored? | ISO 19650-1/-2/-3 | EIR, BEP, MIDP, CDE, file naming and status codes |
| How much information per object per milestone? | ISO 7817-1 (LOIN) | requirements on geometry, properties, documents |
| How are items classified and named? | ISO 12006-2 / -3 | `IfcClassification`, `IfcClassificationReference` |
| Where are the shared property definitions? | ISO 23386 / 23387 | bSDD (buildingSMART Data Dictionary) properties |
| How is the exchange requirement documented? | ISO 29481 (IDM) | process maps, exchange requirements, MVD / IDS |
| How to bundle model + documents + links? | ISO 21597 (ICDD) | `.icdd` container |

---

## 1. ISO 16739-1 (IFC): editions and how they map to IFC versions

buildingSMART's official version table maps IFC releases to ISO documents [1]:

| IFC version (buildingSMART name) | Common name | ISO document | Status per buildingSMART table [1] |
|---|---|---|---|
| IFC 2.3.0.1 | IFC2x3 TC1 | ISO/PAS 16739:2005 | official (still the most widely exchanged) |
| IFC 4.0.0.0 | IFC4 | ISO 16739:2013 | retired (row not re-checked in the QA pass; the database snippet shows 4.0.2.0 as Retired) |
| IFC 4.0.2.1 | IFC4 ADD2 TC1 | **ISO 16739-1:2018** | official (database date 2017-10) [1] |
| IFC 4.3.2.0 | IFC4.3 ADD2 | **ISO 16739-1:2024** | official, latest; database date 2024-04, ISO acceptance April 2024 [1][2] |
| IFC 4.4 / IFC5 | - | - | under development, not official |

(QA pass 2026-11-06: the ISO-number mapping for 4.0.2.1 and 4.3.2.0 was re-confirmed from the buildingSMART IFC Specifications Database via a search snippet; the page itself still returns HTTP 403 to the fetch tool.)

Notes:
- ISO approval of IFC 4.3 was first announced by buildingSMART in January 2024 and the formal ISO publication in April 2024 [2][3]. IFC 4.3 adds infrastructure (roads, rail, bridges, tunnels, ports and waterways) on top of building entities [2][4].
- The European adoption is **EN ISO 16739-1:2024**, which supersedes EN ISO 16739-1:2020 (catalogue mirror: stage 60.60 dated 3 Apr 2024, publication date 18 Jun 2024); the Slovak national notice gives CEN approval as 3 Feb 2024, without modification of the ISO text [4][4b]. The first European adoption of IFC was EN ISO 16739:2016 [23].
- In the file itself the schema is named in the header: `FILE_SCHEMA(('IFC2X3'));`, `FILE_SCHEMA(('IFC4'));` (IFC4 ADD2 TC1 is still written as `IFC4`) and, for IFC 4.3 ADD2, `FILE_SCHEMA(('IFC4X3_ADD2'));`. These three identifiers are the ones the buildingSMART Validation Service accepts (`IFC2X3`, `IFC4`, `IFC4X3_ADD2`) [33b].
- The ISO text is behind a paywall; the schema documentation itself is free at standards.buildingsmart.org (IFC4.3.2.0 documentation) [1] (the site returned HTTP 403 to the fetch tool used for this research, but is listed in search results).
- A planned CEN technical specification, **prCEN ISO/TS 25055 "Compatibility policy for EN ISO 16739-1 revisions"** (CEN project approved 10 Apr 2024), was **deleted (stage 30.98) on 28 Jan 2026** per a Serbian national-body listing; the ISO parent project ISO/CD TS 25055 (ISO/TC 59/SC 13) is also listed as deleted, with the date given as 3 Sep 2025 by one catalogue (no reason is stated anywhere) [5]. So there is no formal ISO-level backward-compatibility policy; compatibility between IFC2x3, IFC4 and IFC4.3 is a tool issue (see pitfalls).

### What "IFC" includes beyond the schema
ISO 16739-1 covers the data schema, its documentation, property and quantity set definitions and the exchange file format mechanism [4]. Practical deliverables built on top of it are *not* in the ISO text but are buildingSMART standards:
- **MVD (Model View Definition)**: subset of IFC for a use case, e.g. IFC2x3 Coordination View 2.0, IFC4 Reference View, IFC4 Design Transfer View. IFC 4.3 Reference View exchange requirements were added to the open-source Revit exporter in releases 24.3.40, 25.4.40 and 26.4.1 [31].
- **IDS (Information Delivery Specification) 1.0**, approved as a final buildingSMART standard in June 2024 [28].
- **bSDD**, **BCF**, **ICDD**-related work (see below).

## 2. ISO 10303-11, -21, -28 (the technology under IFC)

| Part | Role for IFC | Practical meaning |
|---|---|---|
| ISO 10303-11 (EXPRESS) | Language in which the IFC schema is written [7] | Entity inheritance, WHERE rules, derived attributes live here |
| ISO 10303-21 (STEP physical file, "p21") | Default `.ifc` file encoding [6][7] | Clear-text file: `HEADER;` and `DATA;` sections, `#16=IFCWALL(...)`, unset attribute `$`, derived `*` |
| ISO 10303-28 (XML) | Basis of `.ifcXML` [7] | Generated from EXPRESS; much more verbose than `.ifc` (one source says 300-400% larger) [7] |

Facts from the Wikipedia article on ISO 10303-21 [6]:
- Editions: 1st 1994, 2nd 2002, 3rd 2016 (added anchor/reference/signature sections, ZIP compression, digital signatures, UTF-8). One source notes that tool support of the 2016 edition lagged the older editions in early 2017 [7] - in practice most IFC files are still "edition 1" style.
- Header groups: `FILE_DESCRIPTION` (contains the MVD name, e.g. `ViewDefinition [ReferenceView_V1.2]`), `FILE_NAME` (name, ISO 8601 timestamp, author, organization, originating system), `FILE_SCHEMA`.
- Each instance has a local id `#16`; references may point forward; `$` is "not set".
- `.ifczip` (zipped p21) and `.ifcxml` are also allowed IFC serialisations; an IFC4 XML is less verbose than IFC2x3 XML [7].

Why QA cares: an MCP tool reporting "schema version" should read `FILE_SCHEMA`, not guess from the file extension; a tool that rewrites a file should preserve header schema and produce valid p21 (balanced parentheses, unique `#ids`, all references resolved).

## 3. ISO 19650 (information management using BIM)

### 3.1 Parts

| Part | Title (short) | Year | Notes |
|---|---|---|---|
| 1 | Concepts and principles | 2018 (published 7 Dec 2018; catalogue stage 90.92 "to be revised" since 7 Nov 2024) | terms, information requirements, roles [8][34] |
| 2 | Delivery phase of assets | 2018 (published 7 Dec 2018; stage 90.92 since 7 Nov 2024) | design and construction processes; adopted as EN ISO 19650-2 in 2019 [8][9][34] |
| 3 | Operational phase of assets | 2020 (published 29 Jul 2020; stage 90.92 since 7 Nov 2024) | PIM-to-AIM handover, trigger events [8][34] |
| 4 | Information exchange | 2022 | exchange process, acceptance criteria (year from secondary summaries, not re-checked against ISO) [8] |
| 5 | Security-minded approach | 2020 (ISO news of June 2020) | sensitive information [8] |
| 6 | Health and safety information | 2025 (approved January 2025; ISO 19650-6:2025 listed by national bodies) | [8][10][34b] |

Parts 1-3 have been under review since 2024: catalogue pages show ISO/DIS 19650-1 and ISO/DIS 19650-2 (and a separate ISO/DIS 19650-3) as drafts "in development" [34]. A national-body listing shows the Part 2 DIS ballot initiated 10 Mar 2026 at stage 40.20, and BSI/nima opened UK consultation on the Part 1 and 2 drafts from 11 Mar to 3 May 2026 (search snippets, secondary). Per a consultancy blog (not an official source; stage code not independently confirmed): voting closed 3 June 2026, and by 18 Aug 2026 both sat at stage 40.93 (decision on a second DIS ballot), so publication in 2027 is more realistic than late 2026; the blog says Part 3 would be merged into Part 2, although the ISO catalogue still lists a separate DIS 19650-3 draft (conflict, unresolved) [10]. The 2018 editions remain in force until a revised standard is published. The same blog says the draft drops "BIM" from the title and renames BEP to "Information Production Plan", EIR to "Information Production Requirements" and TIDP to "Information Production Schedule" [10]. **Until published, the 2018/2020 terminology below is the one in force.** The UK BIM Framework was reportedly rebranded "IMI Framework" in May 2025 [10] (blog claim).

### 3.2 Key concepts and artefacts

| Term | Meaning | IFC/QA relevance |
|---|---|---|
| **OIR** Organizational Information Requirements | what the owner organization needs to know to run its business | rarely reaches the model directly |
| **AIR** Asset Information Requirements | information needed to operate an asset | what the as-built IFC handed to facility management should contain |
| **PIR** Project Information Requirements | information needed at project decision points | defines milestones |
| **EIR** Exchange Information Requirements | what the appointing party asks one appointed party to deliver, in what format and when | where "deliver IFC4 Reference View, with Pset_WallCommon.FireRating on all walls" is written |
| **PIM / AIM** | Project / Asset Information Model | the aggregate of all containers (models, documents, schedules) |
| **BEP** BIM Execution Plan | pre-appointment BEP (tender) and post-appointment BEP (confirmed by the delivery team) | contains naming, coordinate system, IFC version, LOIN tables |
| **MIDP** Master Information Delivery Plan | all information deliverables, by whom, when | list of IFC exports per milestone |
| **TIDP** Task Information Delivery Plan | per task team; the MIDP aggregates the TIDPs | |
| **CDE** Common Data Environment | agreed source of information with states WIP, Shared, Published, Archive [8] | where exported IFC is uploaded |
| Appointing party / lead appointed party / task team | roles in Part 2 | |

Part 2 organizes the process into stages (general knowledge, not re-verified here): assessment and need, invitation to tender, tender response, appointment, mobilization, collaborative production of information, information model delivery, project close-out (unverified numbering 5.1-5.8).

### 3.3 CDE status codes and file naming

ISO 19650 itself only prescribes the four CDE states (WIP, Shared, Published, Archive); detailed status codes and the container naming scheme come from national annexes, notably the UK National Annex to BS EN ISO 19650-2 [8][30][32]. Autodesk documents this status code set in its CDE help [29]:

| Code | Meaning | CDE state |
|---|---|---|
| S0 | initial status | WIP |
| S1 | suitable for coordination | Shared |
| S2 | suitable for information | Shared |
| S3 | suitable for review and comment | Shared |
| S4 | suitable for stage approval | Shared |
| S5 | "withdrawn (no longer used)" in Autodesk's table; other guidance describes S5 differently (one search snippet: "review and acceptance"), so do not rely on S5 (unverified) | Shared (non-contractual) in Autodesk's table |
| S6 / S7 | suitable for PIM / AIM authorization | Shared (non-contractual) |
| A1, An | authorized and accepted | Published (contractual) |
| B1, Bn | partial sign-off with comments | Published (contractual) |
| CR | as-constructed record document | Published (for AIM acceptance) |

The table was re-checked against the Autodesk help page in the QA pass [29]; the UK National Annex text itself was not read (the CDBB/NBS pages found were not opened), so the exact UK definitions of S5, S6, A, B and CR are not independently confirmed.

Typical UK-style container ID (from a practitioner blog [30]): `Project-Originator-Volume/System-Level/Location-Type-Role-Number`, e.g. `ARCH01-AGN-XX-ZZ-M3-A-0001` (type `M3` = 3D model, `DR` drawing, `SP` specification; role `A` architect, `S` structural; `XX` = not applicable, `ZZ` = all). Revisions: `P01` preliminary, `C01` contractual. The BEP sets the exact lists; other countries use different fields (national annexes elsewhere were not researched - gap).

### 3.4 How ISO 19650 translates into IFC deliverables
- EIR/BEP state *IFC version and MVD*, e.g. "IFC4 Reference View" or "IFC2x3 Coordination View 2.0" - so the exported `FILE_SCHEMA` and `FILE_DESCRIPTION` must match.
- File name = container ID; status/revision typically stored as CDE metadata, not necessarily in the name [30].
- Project data: `IfcProject`, `IfcSite`, `IfcBuilding`, `IfcBuildingStorey` hierarchy, units and coordinate reference (`IfcMapConversion`, IFC4+) set per BEP.
- Required properties (property sets) and classification per LOIN/EIR; checked with IDS or a model checker.
- Handover (Part 3 / AIR): as-built IFC plus COBie-like data and documents.

## 4. ISO 7817-1:2024 Level of Information Need (LOIN)

- **ISO 7817-1:2024** ("Building information modelling - Level of information need - Part 1: Concepts and principles", edition 1, June 2024, 23 pages) is the international version of **EN 17412-1:2020**; EN ISO 7817-1:2024 replaces EN 17412-1, which is withdrawn [11][12][13]. Catalogue mirror: EN 17412-1:2020 stage 99.60 (withdrawal effective) on 3 Jul 2024; EN ISO 7817-1:2024 stage 60.60 on 3 Jul 2024, publication date 18 Sep 2024 [13b]. Changes were minor: aligned terms with EN ISO 19650-4, new examples in Annex B, updated normative references [11][12].
- Part 2 (technical specification, application guidance) and Part 3 (schema for a machine-readable LOIN definition) were reported "under development" by a 2024 article [11]; current status not re-checked.
- **Concept:** LOIN is *not a scale*. It is a specification of the *minimum* information needed for a purpose, defined per **purpose, milestone, actor and object** (general knowledge of the standard - unverified in this research), in three categories: **geometrical information**, **alphanumerical information**, **documentation** [14]. German terminology: *Informationsbedarfstiefe* (LOIN) introduced by DIN EN 17412-1:2021-06; the DIN EN ISO 7817-1:2024-11 edition follows [14][12].
- The standard uses no numbered levels or acronyms; levels are defined per project in the BEP/EIR (German: BAP, *BIM-Abwicklungsplan*) [14].

### LOD vs LOI vs LOG vs LOIN

| Term | Origin | What it covers |
|---|---|---|
| **LOD** BIMForum "Level of Development" | AIA G202-2013 definitions, organised by CSI Uniformat 2010 [15] | scale 100/200/300/350/400/500 for element *geometry* (US practice) |
| **LOG** Level of Geometry | common in DACH/Europe | geometric content only [14] |
| **LOI** Level of Information | same | alphanumeric content only [14] |
| **LOIN** Level of Information Need | EN 17412-1 / ISO 7817-1 | need-based specification: geometry + data + documents |

BIMForum LOD Specification [15][16]:
- Current edition: **LOD Spec 2025**, labelled "Latest Version" on the BIMForum page (the page header shows 31 Dec 2024, which is the page date, not a release date; the official 2025 files appear to have been uploaded in Jan-Feb 2026 judging by file paths, so treat the exact release date as unverified); previous: 2023 edition (Part I dated 27 Feb 2024, Part II 28 Feb 2024; public comment draft dated 28 Dec 2023), 2021 edition (final dated 28 Dec 2021) [15][16]. The 2023 edition made few requirement changes, removed vague terms and **no longer addresses non-geometric information** (attributes can be attached at any LOD) [16].
- The specification "does not prescribe" what LOD is needed when; it states that definitions address *element geometry* for quantity take-off, 3D coordination and 3D control/planning [15].
- Customary meaning of levels (general knowledge, consistent with the German mapping in [14]): 100 concept/pre-design (DE *Vorentwurfsmodell*), 200 approximate geometry/design (*Entwurfsmodell*), 300 precise geometry/approval (*Genehmigungsmodell*), 350 includes interfaces/coordination (optional; tender pricing), 400 fabrication/construction (*Ausführungsmodell*), 500 field-verified/as-built (*As-built-Modell*) [14]. LOD is *not* the sum LOG + LOI [14]; there is no binding definition outside the project documents [14].

How to express LOIN in IFC deliverables: geometry -> representation types/detail (`IfcShapeRepresentation` with `Body`, `Axis`, `Box`...); alphanumeric -> `IfcPropertySet` / `IfcElementQuantity` values, classification references, materials; documentation -> `IfcDocumentReference` / `IfcRelAssociatesDocument` or linked files (ICDD). Per-milestone LOIN tables are best turned into an IDS file for automated checking [25][27].

## 5. ISO 12006-2 and -3 (classification and dictionaries)

- **ISO 12006-2** - framework for classification of construction information (it defines a framework, not a ready classification system or table content). The current ISO edition is **ISO 12006-2:2015** (edition 2, approved 8 May 2015, reviewed and confirmed in 2020); a revision draft titled ISO/DIS 12006-2.2 ("Framework for classification and breakdown structures") is listed, with no publication date found. An "EN ISO 12006-2:2020" designation (an Estonian catalogue lists it) could not be confirmed and is probably a catalogue artefact [17][17b]. Russia adopted the 2015 edition as GOST R ISO 12006-2-2017 (Rosstandart order 618-st of 30 Jun 2017, effective 1 Oct 2017) [17c]; see [national/russia.md](national/russia.md). National systems built on it: Uniclass (UK), OmniClass (US/Canada), CCI (Denmark/Sweden), Talo 2000/Kustannus (Finland), Omniclass; DIN 276/ STLB-Bau in Germany (the last two mentioned from general knowledge, unverified here).
- **ISO 12006-3:2022** "Building construction - Organization of information about construction works - Part 3: Framework for object-oriented information" - second edition (published 15 July 2022, replaces ISO 12006-3:2007, which is withdrawn): language-independent information model for dictionaries; works as ontology/taxonomy/thesaurus, and describes an API for interconnected dictionaries per ISO 23386 [17][17d]. bSDD is built on this logic (general knowledge).
- In IFC: `IfcClassification` (system, edition, source) + `IfcClassificationReference` (code) + `IfcRelAssociatesClassification` link the element to the code.

## 6. ISO 23386 and 23387 (property definitions and data templates)

- **ISO 23386:2020** - methodology to describe, author and maintain properties in interconnected data dictionaries (rules for properties, groups, applicants, expert roles, mapping between dictionaries); it does not provide the dictionary content itself. Published 12 Mar 2020; catalogue stage 90.93 "standard confirmed" on 24 Oct 2025; no amendment or revision project is listed (no 2025 edition) [21][21b].
- **ISO 23387** - data templates for construction objects (principles and structure, rules linking templates to IFC classes and classification systems; it also ships an XSD for the ISO 23387 / ISO 12006-3 data models). The **2020 edition was withdrawn and replaced by ISO 23387:2025** (edition 2, published 22 Sept 2025; one catalogue gives 21 Sept) [20][20b]. Cite the 2025 edition.
- Practical use: bSDD (buildingSMART Data Dictionary) is the best-known implementation of this approach; IDS can pull property definitions from it [27]. (bSDD's formal relation to 23386 is general knowledge - unverified here.)

## 7. ISO 29481 (Information Delivery Manual, IDM)

- **ISO 29481-1:2025** (third edition, November 2025, ISO/TC 59/SC 13): methodology and format - how to document a use case with its business context and exchange requirements [19]. Earlier edition ISO 29481-1:2016.
- **ISO 29481-2:2025** (second edition, December 2025) "Building information models - Information delivery manual - Part 2: Interaction framework" [18][19b]. (Earlier text of this file cited ISO 29481-2:2012, which is the superseded first edition; EN ISO 29481-2:2016 was the previous European version, per a Slovak national listing.)
- **ISO 29481-3:2022** "Building information models - Information delivery manual - Part 3: Data schema" (published 6 Sep 2022) - the machine-readable data schema complementing Parts 1 and 2 [19c]. A site that calls Part 3 "model view definitions" (working draft) was describing an earlier stage; the published title is "Data schema".
- IDM components: interaction maps, transaction maps, process maps, exchange requirements [18]. An IDM defines *what* must be exchanged; an **MVD** then maps it onto an IFC subset; **IDS** (computer-readable XML, `.ids`) is the modern, checkable way to say "elements X must have property Y" [25][26][27]. IDS 1.0 became an official buildingSMART standard in June 2024 [28]; its structure: a list of Specifications, each with Applicability and Requirements built from facets (entity, attribute, property, classification, material, partOf) [26]. Archicad 28+ can import an IDS to prepare property sets and classifications; adoption elsewhere was described as early [27].

## 8. ISO 21597 (ICDD)

- **ISO 21597-1:2020** - "Information container for linked document delivery - Exchange specification - Part 1: Container" (ICDD): an open container to exchange heterogeneous files (models, drawings, documents, remote resources) and the **relationships** among them; ontologies in a normative annex; published 14 Apr 2020, confirmed (stage 90.93) on 18 Sep 2025 [22][22b].
- **ISO 21597-2:2020** - "... Exchange specification - Part 2: Link types" (published 5 Nov 2020; confirmed, stage 90.93, 9 Apr 2026) [22c]. (Earlier text called Part 2 a "link set"; the published title is "Link types".)
- Use in practice: handover packages where IFC is delivered together with PDFs/spreadsheets and links; rarely seen in everyday Revit workflows.

## 9. CEN/TC 442 (European BIM standardisation)

- CEN technical committee "Building Information Modelling (BIM)", scope "structured semantic life-cycle information for the built environment"; working groups cover terminology, information exchange, information delivery specification, data dictionaries, infrastructure and horizontal roles [23].
- Works mostly via the **Vienna Agreement** with ISO/TC 59/SC 13: ISO standards are adopted as EN ISO (e.g. EN ISO 16739-1:2024, EN ISO 19650 series, EN ISO 7817-1:2024 [4][11][13b][23]; a European adoption of ISO 29481-1:2025 was assumed in the first draft and could not be confirmed - only the ISO edition is verified [19]). EN 17412-1 was CEN's own work, later raised to ISO level [11].
- CEN/TR 17920:2023 "BIM in infrastructure - Standardization need and recommendations" (published 15 May 2023) [23][23b]. A Buildwise overview (June 2026) lists published and in-development items, but its text could not be extracted [24].
- National mirror committees add annexes and guidance (UK National Annex; DIN German editions; Norwegian/Nordic guidance).

## 10. Putting it together for Revit / openBIM testing

- **Revit IFC export**: the open-source Autodesk Revit IFC exporter ("IFC Extension for Revit", GitHub; LGPLv2 and the "latest annual version plus two previous versions" support policy were confirmed in the repository README by a parallel QA pass, see [qa-standards-2](../_meta/qa/qa-standards-2.md); the releases page itself shows neither) publishes releases per Revit year; the QA pass saw release tags for Revit 2024, 2025, 2026 and 2027, and the 27.0.1 notes call it "the first version of IFC Extension for Revit 2027". The "Revit/Revit LT 2019+" part of the older claim came from the README and was not re-checked [31]. Release notes: "Added IFC4.3 Reference View exchange requirements" appears in 24.3.40, 25.4.40 and 26.4.1 (not in the 27.x notes), with fixes for IFC4 Reference View colours in 27.3.0.12; the newest listed release is 27.4.0.30 for Revit 2027 (30 Oct; the year is not shown on the page, presumably 2026) [31]. The IFC version/MVD is selected in the IFC export setup dialog, a named setup chosen via the "Modify Setup" button (setup names in the 2023 exporter help: "IFC 2x3 Coordination View 2.0", "IFC 4 Reference View", "IFC 4 Design Transfer View") [31b]; the exact File > Export > IFC menu path is general knowledge and was not found in the help pages fetched (unverified).
- A tester's typical oracle: open exported file, read `FILE_SCHEMA`, count entities by class, confirm required Psets/classification exist (IDS or manual).

## Typical questions people ask about this

None of the questions below were harvested from live forum threads (the search tool limit was reached before community-forum searching); all are written from the typical themes in the sources and are marked illustrative.

1. What is the difference between ISO 16739-1:2018 and ISO 16739-1:2024? (illustrative) - 2018 = IFC4 ADD2 TC1; 2024 = IFC4.3 ADD2 with infrastructure [1][2].
2. Which IFC version should I export from Revit for coordination? (illustrative) - set by EIR/BEP; IFC2x3 Coordination View 2.0 and IFC4 Reference View are the common choices; see section 1 and 10.
3. Is IFC4.3 only for roads and bridges? (illustrative) - no, it is the full schema including buildings plus infrastructure [2][4].
4. What does `FILE_SCHEMA(('IFC4X3_ADD2'))` mean? (illustrative)
5. Is the `.ifc` file STEP? What is ISO 10303-21? (illustrative) [6]
6. What is the difference between .ifc, .ifcXML and .ifcZIP? (illustrative) [6][7]
7. What do EIR, OIR, AIR and PIR stand for and who writes them? (illustrative) [8]
8. What is the difference between BEP, MIDP and TIDP? (illustrative)
9. Is ISO 19650 being replaced? When is the new version out? (illustrative) - drafts of Parts 1-2 in 2026; publication expected 2027 per one blog [10].
10. What are CDE status codes S0, S1, A1 and where do they come from? (illustrative) - UK National Annex, not ISO 19650 itself [29][30].
11. Is LOD 300 enough for a permit model? (illustrative) - LOD is not a legal requirement; define LOIN per milestone [14][15].
12. What replaced LOD, LOI and LOG in Europe? (illustrative) - LOIN, ISO 7817-1 [11][14].
13. Is EN 17412-1 still valid? (illustrative) - withdrawn, replaced by EN ISO 7817-1:2024 [11].
14. Does LOD 500 mean more detail than LOD 400? (illustrative) - no, 500 is about field verification, not more detail (general knowledge, unverified).
15. How do I add a classification (Uniclass/OmniClass/CCI) to walls in IFC? (illustrative) - `IfcClassificationReference` [section 5].
16. What is bSDD and how is it related to ISO 23386/23387? (illustrative) [20][21][27]
17. What is IDS and can it replace the Excel requirements table? (illustrative) [25][26][27]
18. What is IDM and how is it different from MVD and IDS? (illustrative) [18]
19. What is ICDD and when do I need it? (illustrative) [22]
20. Why does my IFC from a different tool open with missing properties? (illustrative) - MVD / property set mapping, see pitfalls.
21. Which standard says what an IFC delivery must contain? (illustrative) - none alone; EIR (19650), LOIN (7817), IDS/MVD together.
22. Can an MCP tool validate an IFC against the EIR? (illustrative) - only if requirements are given as IDS or a rule list.

## Common pitfalls and misconceptions

- **"IFC is ISO 19650."** No. IFC = ISO 16739-1 (data format); ISO 19650 = information management process.
- **"IFC4.3 replaced IFC4 in every tool."** Most project exchanges still use IFC2x3 or IFC4; Revit/Archicad IFC4.3 support is partial (the Revit exporter added IFC4.3 Reference View requirements recently [31]; treat the generic claim "default Revit export is IFC4.3" as unverified).
- **Mixing "IFC4" and "ISO 16739:2013".** IFC4 (4.0.0.0) = ISO 16739:2013 and is retired; practical IFC4 is ADD2 TC1 = ISO 16739-1:2018 [1].
- **"The ISO number tells the file version."** The file header does, `FILE_SCHEMA` is authoritative.
- **LOD numbers are universal.** BIMForum LOD is US geometry-focused; it explicitly leaves levels to the project and, since 2023, says nothing about attributes [15][16]. LOD 350 is optional/regional [14].
- **LOD = LOG + LOI.** Incorrect [14].
- **LOIN has numeric levels.** No; it is a per-purpose requirement set [11][14].
- **Status codes are in ISO 19650.** They are a national annex convention (UK); other countries differ [29][30].
- **Terminology drift.** After the 2026-27 revision, BEP/EIR/TIDP may be renamed IPP/IPR/schedule [10]; test data may mix both naming sets.
- **Citing withdrawn documents:** EN 17412-1:2020 (withdrawn) [11]; ISO 23387:2020 (withdrawn 2025) [20]; prCEN ISO/TS 25055 (deleted) [5].
- **ifcXML vs ifc size/support.** `.ifcxml` is verbose and less supported [7].
- **A passing IFC schema check does not mean EIR compliance.** Syntactic validity (ISO 10303-21 + EXPRESS rules) differs from requirement validation (IDS/LOIN).

## Gaps

- buildingsmart.org, technical.buildingsmart.org, standards.buildingsmart.org and iso.org returned HTTP 403 to the fetch tool, so the version table and IFC 4.3 announcement facts rest on search-result summaries of those pages [1][2][3] rather than direct reads. In the QA pass (2026-11-06) ISO catalogue facts were instead checked on national/commercial catalogue mirrors (genorma.com, scc-ccn.ca, evs.ee), which copy ISO stage data; they are treated as near-primary.
- The web-search limit was reached partway through the work, so the following were not researched: Revit IFC export dialog documentation (menu path, MVD list), forum threads with real questions, Russian/other national BIM standards (e.g. GOST/SP) and non-UK CDE naming annexes, ISO 29481-2/3 and 21597-2 current status, bSDD and 23386 relationship from primary source, Graphisoft/Tekla/Bentley IFC docs.
- The UK BIM Framework Guidance Part C PDF and the Buildwise CEN/TC 442 PDF were fetched but their compressed text could not be read [24][32].
- No pirated/suspicious sites were encountered; standards were only read through publisher/catalogue listings, so clause numbers were not verified.

## Sources

[1] buildingSMART IFC schema specifications / version table (via search summary): https://technical.buildingsmart.org/standards/ifc/ifc-schema-specifications/ ; IFC4.3.2.0 documentation: https://standards.buildingsmart.org/IFC/DEV/IFC4_3/HTML/ and https://standards.buildingsmart.org/IFC/RELEASE/IFC4_3/
[2] IFC 4.3 approved as a final standard: https://www.buildingsmart.org/ifc-4-3-approved-as-a-final-standard/
[3] IFC 4.3 formally approved and published as an ISO standard: https://www.buildingsmart.org/?p=29521
[4] EN ISO 16739-1:2024 listing: https://genorma.com/en/standards/en-iso-16739-1-2024 ; DIN Media: https://dinmedia.de/en/standard/din-en-iso-16739-1/379635818
[5] prCEN ISO/TS 25055 (deleted): https://genorma.com/en/standards/prcen-iso-ts-25055
[6] ISO 10303-21 (Wikipedia): https://en.wikipedia.org/wiki/ISO_10303-21
[7] xBIM, STEP to XML: https://docs.xbim.net/examples/step-to-xml-and-back-again.html ; EXPRESS standards: https://www.expresslang.org/standards (search results)
[8] ISO 19650 (Wikipedia, community source): https://en.wikipedia.org/wiki/ISO_19650
[9] EN ISO 19650-2:2018: https://www.evs.ee/en/evs-en-iso-19650-2-2018
[10] ISO 19650 revision, blog (secondary): https://jcvirtualpm.co.uk/2026/10/12/iso-19650-revision-2026-what-is-changing-and-when/
[11] Construction Management / BIMplus, new LOIN standard: https://constructionmanagement.co.uk/digital-construction/new-level-of-information-need-standard-published/
[12] DIN EN ISO 7817-1: https://www.dinmedia.de/de/norm/din-en-iso-7817-1/382382712
[13] EN ISO 7817-1:2024 (genorma): https://genorma.com/en/standards/fpren-iso-7817-1
[14] Baunetz Wissen, LOD/LOI (German, practitioner): https://www.baunetzwissen.de/bim/fachwissen/modellinhalte/was-bedeutet-lod-loi-5285890 ; LOIN glossary: https://www.baunetzwissen.de/glossar/l/loin-9963146?thema=bim
[15] BIMForum LOD page: https://bimforum.org/LOD/
[16] BIMForum 2023 LOD Specification: https://bimforum.org/2023-level-of-development-lod-specification/
[17] ISO 12006-3:2022: https://genorma.com/en/standards/iso-12006-3-2022 ; EVS: https://www.evs.ee/en/evs-en-iso-12006-3-2022
[18] Designing Buildings, IDM: https://www.designingbuildings.co.uk/wiki/Information_Delivery_Manual_(IDM)
[19] ISO 29481-1:2025: https://www.iso.org/standard/88515.html ; https://scc-ccn.ca/standardsdb/standards/8190063
[20] ISO 23387:2020 (withdrawn): https://www.iso.org/standard/75403.html
[21] ISO 23386 listing: https://isrsm.gov.mk/en/project/show/iso:proj:75401
[22] ISO 21597-1:2020: https://www.iso.org/standard/74389.html
[23] CEN/TC 442: https://standards.iteh.ai/catalog/tc/cen/b0e05107-d6bf-4c1c-b222-54dd974f1a96/cen-tc-442 ; https://www.en.une.org/normalizacion_documentos/CENTC-442-activities---Oivind-Rooth.pdf
[24] Buildwise CEN/TC 442 overview (PDF, unreadable text): https://www.buildwise.be/media/ml3foa2a/nabimdigitalconstruction_overviewcentc442_fr.pdf
[25] buildingSMART IDS repository: https://github.com/buildingSMART/IDS
[26] IDS user manual: https://github.com/buildingSMART/IDS/blob/development/Documentation/UserManual/README.md
[27] Nordic BIM Group on IDS (vendor blog): https://www.nordicbim.com/en/insights/what-is-the-buildingsmart-ids-standard
[28] IDS v1.0 approved: https://www.buildingsmart.org/?p=30065
[29] Autodesk CDE status codes: https://help.autodesk.com/cloudhelp/ENU/BIM360D-Document-Management/files/common-data-environment/Status_Codes.html
[30] Archgyan naming conventions (blog): https://archgyan.com/bim-naming-conventions-file-standards/
[31] Autodesk Revit IFC exporter: https://github.com/Autodesk/revit-ifc and https://github.com/Autodesk/revit-ifc/releases
[31b] Autodesk IFC exporter help (2023): https://up.autodesk.com/2023/RVT/ADSKIFCExporterHelp.htm
[4b] EN ISO 16739-1:2024 catalogue mirror: https://genorma.com/en/standards/en-iso-16739-1-2024
[13b] EN 17412-1:2020 (withdrawn) and EN ISO 7817-1:2024: https://genorma.com/en/standards/en-17412-1-2020 ; https://genorma.com/en/standards/en-iso-7817-1-2024
[17b] ISO 12006-2:2015 catalogue entry: https://www.iso.org/standard/61753.html
[17c] GOST R ISO 12006-2-2017 (Rosstandart order 618-st, 30 Jun 2017): https://pravo.ppt.ru/prikaz/rosstandart/n-618-st-185754
[17d] ISO 12006-3:2022 catalogue mirror: https://genorma.com/en/standards/iso-12006-3-2022
[19b] ISO 29481-2:2025 (edition 2, Dec 2025): https://www.iso.org/standard/88516.html
[19c] ISO 29481-3:2022 "Part 3: Data schema": https://genorma.com/en/standards/iso-29481-3-2022
[20b] ISO 23387:2025 catalogue mirror: https://genorma.com/en/standards/iso-23387-2025
[21b] ISO 23386:2020 catalogue mirror (stage 90.93, 24 Oct 2025): https://genorma.com/en/standards/iso-23386-2020
[22b] ISO 21597-1:2020 catalogue mirror: https://genorma.com/en/standards/iso-21597-1-2020
[22c] ISO 21597-2:2020 catalogue mirror: https://genorma.com/en/standards/iso-21597-2-2020
[23b] CEN/TR 17920:2023: https://genorma.com/en/standards/cen-tr-17920-2023
[33b] buildingSMART Validation Service user guide (accepted schema identifiers IFC2X3, IFC4, IFC4X3_ADD2): https://buildingsmart.github.io/validate/user/index.html
[34] ISO 19650-1/-2/-3 catalogue mirrors (stage 90.92 since 7 Nov 2024; ISO/DIS 19650-1/-2/-3 in development): https://genorma.com/en/standards/iso-19650-1-2018 ; https://genorma.com/en/standards/iso-19650-2-2018 ; https://genorma.com/en/standards/iso-19650-3-2020
[34b] ISO 19650-6:2025 listing: https://www.evs.ee/et/iso-19650-6-2025
[32] UK BIM Framework Guidance Part C: https://www.ukbimframework.org/wp-content/uploads/2021/02/Guidance-Part-C_Facilitating-the-common-data-environment-workflow-and-technical-solutions_Edition-1.pdf
