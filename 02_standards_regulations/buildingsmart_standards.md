# buildingSMART standards family: IFC, IDS, BCF, bSDD, MVD, IDM, OpenCDE, validation, certification

**Last researched: 2026-11-06**

## In plain words

buildingSMART International (bSI) is the non-profit that maintains the "openBIM" standards. Each standard solves one narrow problem:

- **IFC** is the data format (what a model contains).
- **MVD / mvdXML** says which subset of IFC a given exchange uses.
- **IDM** describes the exchange process (who sends what to whom, when).
- **IDS** is a machine-readable checklist of what an IFC must contain.
- **bSDD** is the shared dictionary of names, classes and properties.
- **BCF** is the format for issues and comments tied to model elements.
- **OpenCDE APIs** connect all this to document-management servers (CDEs).
- The **Validation Service** and **software certification** check files and programs against the standards.

For an MCP tester: when an AI tool "opens an IFC", "checks it against requirements" or "creates an issue", it is almost always using one of these. Expect questions such as "does my IFC pass validation?", "check walls against an IDS", "export BCF issues", "which IFC version should Revit export?". Several of these standards are not tied to a vendor, so correct answers must mention exact versions and names.

Evidence quality: primary sources (GitHub specs, docs, release notes) are marked [n]. Blogs and forums are labelled as community. Many buildingSMART web pages (buildingsmart.org, technical.buildingsmart.org, standards.buildingsmart.org, iso.org) returned HTTP 403 to the fetch tool, so some facts come from search-engine snippets of those pages (marked "snippet") or from background knowledge (marked "(unverified)").

## Map of the family

| Standard | Question it answers | Format | Status (as researched) |
|---|---|---|---|
| IFC (ISO 16739-1) | What is in the model? | STEP `.ifc` (also `.ifcXML`, `.ifcZIP`, IFC5: JSON-like IFCX) | IFC2x3 TC1, IFC4 ADD2 TC1, IFC4.3 ADD2 are the usable releases; IFC5 in development |
| MVD / mvdXML | Which part of IFC is used for this exchange? | mvdXML (XML) | mvdXML 1.1 (2016) [40]; IFC4 RV and DTV; IFC4.3 RV and Alignment-based View [31][32] |
| IDM (ISO 29481) | What information is exchanged, by whom, when? | Process maps; Part 3 is an XML/data schema | Part 1: 2016 edition; Part 2: 2025 edition; Part 3: 2022 [33][34][35] |
| IDS | Does this IFC contain what I asked for? | `.ids` (XML, XSD) | v1.0, final standard, June 2024 [5][17] |
| bSDD | What are the agreed names, classes, properties, units? | Online service, REST/GraphQL API | Live service; API v1 documented [27][28] |
| BCF | Which problem, where, who is responsible? | BCF-XML (zip `.bcf`), BCF-API (REST) | BCF-XML 2.1 and 3.0; BCF-API 3.0 [21][22][23] |
| OpenCDE | How does software talk to a CDE? | REST/JSON, OAuth 2 | Foundation API 1.1, Documents API 1.0, BCF API 3.0 [23][25][26] |
| Validation Service | Is this IFC valid? | Web app + API | v1.0.5 (30 Sep 2026), out of beta since 20 Mar 2026 [3] |
| Software certification | Does this program read/write IFC correctly? | Test routines (b-Cert) | Active for IFC2x3 CV 2.0 and IFC4 RV/DTV [36] |

### How they connect (typical flow)

1. A client writes information requirements as **IDM**-style process and **IDS** file (often citing **bSDD** classes and property names).
2. Authors export **IFC** from Revit/Archicad/etc. using an **MVD** (for example IFC4 Reference View).
3. The file is checked by the **Validation Service** (is it valid IFC at all?) and by an **IDS checker** (does it contain what the client asked for?). These are different checks [3 snippet][20].
4. Failures are reported as **BCF** issues, exchanged through a CDE via the **BCF-API / OpenCDE**.
5. Software that did steps 2 and 3 correctly may be **certified**.

## IFC (brief; the base of everything)

- Official schema releases commonly used: IFC2x3 (TC1), IFC4 (ADD2 TC1) and IFC4.3 (ADD2). Validation Service accepts exactly `IFC2X3`, `IFC4`, `IFC4X3_ADD2` in the schema identifier [1].
- ISO numbers: ISO 16739-1:2018 for IFC4 ADD2 TC1 and ISO 16739-1:2024 for IFC4.3 (unverified, from background knowledge; check iso.org).
- IFC4.3 adds infrastructure (alignment, roads, rail, bridges). `IfcAlignment` is valid only in IFC4X3_ADD2 [1].
- Files: STEP Physical File, ISO 10303-21, extension `.ifc`. The Validation Service accepts only unzipped `.ifc` up to 256 MB [1].

## IDS (Information Delivery Specification)

### What and status

- IDS defines information requirements in a form humans can read and software can check. It supports the "exchange information requirements" idea of ISO 19650 (snippet [17]).
- **IDS 1.0 became a buildingSMART Final Standard in June 2024** (announcement dated 4 June 2024; the standards page gives 1 June 2024 as the approval date; snippet [17]). Wikipedia also says v1.0 was published June 2024 [20].
- Source of truth: GitHub `buildingSMART/IDS`, schema file `Schema/ids.xsd`, user manual `Documentation/UserManual`, implementers docs `Documentation/ImplementersDocumentation`, test cases `TestCases` [5][6].
- IDS does not describe geometry in detail (from a pre-final announcement, snippet [17]; treat as unverified for current text).
- Supported IFC schemas: IFC2X3, IFC4, IFC4X3_ADD2 [7].
- File: `.ids`, XML validated against the XSD. Passing the XSD is necessary but not sufficient; the file must also pass the buildingSMART IDS Audit tool [15].

### Structure of an IDS file [6][7]

- One `.ids` file = metadata (title, author, date, version, purpose) + one or more **specifications**.
- Each specification has:
  - **Applicability**: which model objects are in scope (facets).
  - **Requirements**: what those objects must (or must not) have (facets).
  - Optional description/instructions, and the IFC version(s) it applies to.
- Example sentence: "All walls must have a fire rating property" (applicability: entity IFCWALL; requirement: property `Pset_WallCommon.FireRating`).

### Cardinality (required / optional / prohibited) [7]

| Where | Value | Meaning |
|---|---|---|
| Applicability `minOccurs`/`maxOccurs` | 1..unbounded | Required: at least one matching object must exist, and each must satisfy the requirements |
| | 0..unbounded | Optional: may or may not exist; those that exist must satisfy requirements |
| | 0..0 | Prohibited: no matching object may exist; requirements are ignored |
| Requirement facet | required / optional / prohibited | Property/attribute etc. must exist / is checked only if present / must not exist |

Other min/max combinations are not allowed [15]. If an optional requirement would fail when required, checkers should issue a warning rather than an error [15].

### The six facets

| Facet | Parameters | Key behaviour | Source |
|---|---|---|---|
| **Entity** | `name` (IFC class, UPPERCASE e.g. `IFCWALL`), `predefinedType` (optional) | No inheritance: each subtype must be listed explicitly (you list `IFCWALL`, `IFCDOOR`; abstract `IFCELEMENT` is useless). No cardinality. `USERDEFINED` resolves via type object `ElementType`, otherwise instance `ObjectType`. IFC2X3 uses an occurrence-type mapping table. | [13] |
| **Attribute** | `name` (e.g. `Name`, `Description`, `GlobalId`, `Tag`), `value` (optional) | Only fixed schema attributes (not inverse ones such as `ConnectedTo`). Empty value in applicability matches any filled attribute. Prohibited with value still allows null. | [14] |
| **Property** | `propertySet` (e.g. `Pset_WallCommon`), `baseName` (e.g. `FireRating`), `dataType` (e.g. `IFCLABEL`), `value`, `uri` | Same facet covers properties and quantities (`Qto_` sets; IFC2X3 has no quantity sets). Property must exist and be non-empty. A value needs a dataType. Measure types are compared in SI. `uri` (e.g. bSDD link) is metadata only, not checked. For ranges, all IFC values (both bounds of bounded values) must fall within the restriction. | [9] |
| **Classification** | `system` (e.g. ETIM, Uniclass 2015, CCI), `value` (e.g. `EC000009`), `uri` | System only = any classification of that system. Optional + system only is not allowed. Use this instead of Property for classification codes. | [11] |
| **Material** | `value` (name or category, supports restrictions), `uri` | Matches `IfcMaterial`, layer, profile, constituent or list. Matching is exact (spelling and case matter). Name `S275` with category `Steel` passes an IDS value `Steel`. No value = any material. | [12] |
| **partOf** | `entity` (required, container class e.g. `IFCSPACE`), `relation` (optional) | Follows recursively six relations: `IfcRelAggregates`, `IfcRelAssignsToGroup`, `IfcRelContainedInSpatialStructure` (primary container only), `IfcRelNests`, `IfcRelVoidsElement`, `IfcRelFillsElement`. Omitted relation = all six. Optional cardinality not allowed. | [8] |

### Restrictions [10]

Facet parameters can use a restriction instead of a simple value:

- **Enumeration**: one of a list (e.g. strength 25/30/35/40; 31 fails).
- **Pattern** (regex, simplified): `DT[0-9]{2}` matches `DT24`, not `DT123`; `DT.*` matches anything starting with DT.
- **Bounds**: min/max, each inclusive or exclusive.
- **Length**: exact, min, or max character count.
- Case sensitivity is not stated on the restrictions page (unverified); the material page says matching is case-exact [12].
- Float tolerance: relative 1e-6 plus absolute 1e-6; TotalDigits and FractionDigits are not supported [15].

### Tools

| Tool | Role | Notes | Source |
|---|---|---|---|
| **IfcTester** (part of IfcOpenShell) | Read/write IDS and check IFC | Python library, CLI (`python -m ifctester example.ids example.ifc`, `-r Html -o report.html`), experimental web app. Reporters: Console, Json, Ods, Html, Bcf. Install: `pip install ifctester`. Argument names changed between versions (older: `name`, `datatype`, `minOccurs`; newer: `baseName`, `dataType`, `cardinality`). | snippet [19] |
| **IDS Audit tool** (`ids-tool`) | Quality-check `.ids` files (XSD plus extra audits) | Official buildingSMART .NET console app and library, MIT license; NuGet package `ids-tool.CommandLine`, verb `audit`. A browser version (Xbim IDS auditing service) runs locally without uploading files. | [16][15] |
| **Xbim.IDS.Validator** | Check IFC against IDS in .NET | Community/open-source library, not an IDS-file auditor | snippet [39] |
| **IDS authoring/checking in products** | BIMcollab, usBIM (ACCA), IDS4Revit (DiRoots), ALLPLAN, Solibri (named in Wikipedia) | The bSI "IDS software implementations" list is self-reported by vendors and is not certification | snippet [18][20] |
| **IDS editors** | Free editors exist (Wikipedia names IDS Maker from bimvision and usBIM.IDS) | Check each vendor | [20] |

Test-suite rule: software that checks IDS against IFC must pass the IFC/IDS test cases in the repository `TestCases` folder [15].

### Results and BCF

Audit results can be saved as BCF-XML or sent through BCF-API, but the BCF structure for IDS results is "not yet specified" per the developer guide [15].

## buildingSMART Validation Service

URL: validate.buildingsmart.org (web); documentation at buildingsmart.github.io/validate [1][2].

### What it checks (layers) [1]

1. **STEP syntax**: valid ISO 10303-21 physical file. Since v0.7.7 syntax check is split into header and data parts; v1.0.1 raises a syntax error for BOM8 formatting [3].
2. **Schema version**: only `IFC2X3`, `IFC4`, `IFC4X3_ADD2`.
3. **Schema compliance** (EXPRESS): attributes, inverse attributes, entity-scoped WHERE rules, global rules; flags entities not in the declared schema (e.g. `IfcAlignment` in IFC4) and instantiation of abstract entities.
4. **Normative rules**:
   - *Implementer Agreements* (ratified by software implementers).
   - *Informal Propositions* (not ratified but still mandatory for validity).
5. **Industry practices** (non-normative): common practice and sensible defaults. They produce **warnings**, never make a file invalid [1].

Out of scope: project-, national- or organisation-specific requirements. bSI points to IDS for that (snippet [4]).

### Outcomes and rules

- Outcome statuses: pass, error, warning; plus *not applicable* and *disabled* (hidden by default; a checkbox shows them) [1]. Pass results are hidden by default.
- *Activation rules* never return an error; used to collect metrics (e.g. DOC000, TAS000 tessellated geometry activation) [3 snippet].
- Rules are Gherkin `.feature` files in the `ifc-gherkin-rules` repository, each tagged exactly one of `@implementer-agreement`, `@informal-proposition`, `@industry-practice`. Rule code = three letters (functional part) + three digits, e.g. `ALB002` (alignment layout), `ALB003` (allowed entities nested in alignment), `SPS001` (spatial structure), `GEM...` (geometry), `IFC430`/`IFC431` (entities excluded from IFC4.3 Reference View and Alignment-based View MVDs) [2][3].
- bSDD compliance check: temporarily disabled since v0.6.6 [1].
- Allowlisting (v1.0.0+) suppresses specific outcomes without disabling the whole rule [3 snippet].
- Account needed (sign-up); API exists with rate limiting, file size limits and pagination (v0.7.8 to v0.8.1) [3]. The user guide does not cover the API; a separate developer guide does [1].

### Recent versions [3]

| Version | Date | Notable |
|---|---|---|
| 1.0.0 | 2026-03-20 | Exit from beta, DOC000 activation rule, allowlisting, digital signature toggle |
| 1.0.1 | 2026-04-29 | IFC106 replaces IFC105, BOM8 syntax error |
| 1.0.2 | 2026-06-30 | IFC430, IFC431 (IFC4.3 MVD exclusions) |
| 1.0.3 | 2026-08-06 | TAS000, preview environment for next major release |
| 1.0.4 | 2026-09-01 | RFT000/RFT001 (IfcReferent), invalid MVD headers shown in UI |
| 1.0.5 | 2026-09-30 | Fixes to ALS005, ALS006, ALB023 |

The user guide page I fetched described version 0.8.4 [1], i.e. the documentation can lag behind the service.

### Validation vs IDS (do not confuse)

Validation Service = "is this valid IFC, regardless of project?" IDS = "does this IFC satisfy this project's requirements?" (snippet from the openBIM workflow page and [4]).

## MVD and mvdXML

- **MVD** = a defined subset of the IFC schema for a use case. **mvdXML** is the machine-readable format for MVD rules; latest mvdXML is 1.1 (February 2016) [40].
- **IFC2x3 Coordination View 2.0 (CV2.0)**: the most widely implemented view; architecture, structure and MEP coordination; Archicad is certified for import and export [30].
- **IFC4** splits CV into **Reference View (RV)** (one-way, reference-model workflows) and **Design Transfer View (DTV)** (limited editable exchange; "not meant for round-trip") [30].
- **IFC4.3**: two official MVDs per the IFC 4.3.2 documentation: **Reference View** and **Alignment-based View (AbV)** (infrastructure superset of RV). The Design Transfer View was intended but never published as an official MVD for 4.3 [31]. An AbV 1.0 for IFC 4.3.2.0 went to a Standards Committee vote closing 18 Sept 2025; the outcome was not confirmed in my sources (snippet [32]). The IFC4.3 MVD documentation was marked "under development" in 2024-era forum discussion [31]. The `IFC4.3.mvdxml` file is a generated artifact in the output repository [31].
- Practical: Revit and Archicad offer IFC export settings named after these views (Archicad "Model View Definitions" help [30]). Revit export option names ("IFC2x3 Coordination View 2.0", "IFC4 Reference View", "IFC4 Design Transfer View") come from the open-source Revit IFC exporter (unverified here; the Autodesk help page could not be fetched).

## IDM (ISO 29481)

- **IDM** documents business processes and the information exchanged: who, when, what information, in which format.
- ISO 29481-1 (methodology and format): 2016 edition published 1 May 2016; a later edition may exist (sources disagree; check iso.org) [35].
- ISO 29481-2 (interaction framework): 2012 edition withdrawn; edition 2 of 2025 (one ISO page still labelled it a Final Draft) [33].
- ISO 29481-3:2022 (data schema): machine-readable storage/exchange of IDM specifications [34].
- Relation: IDM (process) leads to MVD (technical subset of IFC) and IDS (checkable requirements) (summary of [30][31][20]; conceptual).

## BCF (BIM Collaboration Format)

### BCF-XML (file) [21][22]

- Versions: **2.1** and **3.0** (3.0 documented on the `release_3_0` branch; 3.0 is based on 2.1). Extension `.bcf` (since 2.1; earlier `.bcfzip`) [22].
- A BCF file is a zip: root files `bcf.version`, `extensions.xml` (required in 3.0), optional `project.bcfp`, `documents.xml`; one folder per topic named by lowercase GUID containing `markup.bcf`, `.bcfv` viewpoints, snapshots (PNG/JPEG, longest side up to 1500 px), optional bitmaps; attachments in `Documents/` [22].
- Topic required fields: `Guid`, `TopicType`, `TopicStatus`, `Title`, `CreationDate`, `CreationAuthor`. Optional: `Priority`, `Labels`, `DueDate`, `AssignedTo`, `Description`, `Stage`, `ServerAssignedId`, `ReferenceLink` [22].
- Viewpoints are immutable; contain camera (perspective or orthogonal), component selection/visibility/colouring, clipping planes, lines. Components identified by `IfcGuid` (preferred) or `AuthoringToolId`, plus `OriginatingSystem` [22].
- 2.0 to 2.1 schema changes: project name added, due date added, comment status fields removed, etc. [24]. A direct 2.1 to 3.0 changelog was not found in the sources fetched (gap).

### BCF-API [23]

- RESTful, version 3.0; all implementations must implement the OpenCDE Foundation API; TLS required.
- Resources: `/bcf/{version}/projects/...` with projects, topics, comments, viewpoints (snapshots, bitmaps, selection/colouring/visibility), documents, event feeds; project extensions define allowed statuses, labels, users.
- Swagger/OpenAPI file is the reference and may be updated at any time [23].

### In tools

IfcOpenShell's BCF library supports BCF-XML 2.1 and 3.0 and BCF-API 3.0 (snippet [41]); IfcTester can emit BCF [19].

## bSDD (buildingSMART Data Dictionary)

- Online service hosting dictionaries (classifications, properties, allowed values, units, translations), all linked in one canonical database [27].
- Terminology: *Dictionary* (formerly domain) contains *Classes* (formerly classifications) and *Properties*; class-to-property links use a *ClassProperty* object. Without custom URI, items get `https://identifier.buildingsmart.org/...` URIs (snippet [29]).
- API base `https://api.bsdd.buildingsmart.org`; test environment `https://test.bsdd.buildingsmart.org` (no SLA, developers only) [28].
- Public methods need no login; secured methods use Azure AD B2C / OAuth2 with a client id obtained from buildingSMART [28].
- Documented endpoints: Dictionary, SearchList (search classes in a dictionary), Class (details plus properties). Contract on SwaggerHub `buildingSMART/Dictionaries/v1`. GraphQL at `/graphqls` (secured) [27][28].
- Clients must send a `User-Agent`/`X-User-Agent` as `application/version`. Breaking changes yield a new API version; the old one is supported for six months. The `identifier.buildingsmart.org` JSON output is deprecated for system-to-system calls [28].
- The bSDD repository does not host the data or the service code, only docs and templates [27].
- In IDS the `uri` parameter can point to bSDD, but is not checked [9][11].

## OpenCDE APIs [25][26][23]

- **Foundation API 1.1** (released together with Documents API 1.0): `GET /foundation/versions` (public), `GET /foundation/{version}/auth` (OAuth 2.0 details: authorization code, implicit, password grants; dynamic client registration), `GET /foundation/{version}/current-user`.
- **Documents API 1.0**: user selects documents in the CDE web UI; client gets download links (`/select-documents`, `/upload-documents`, `/document-versions`); polling no more often than every 5 minutes. Automatic CDE-to-CDE sync not yet supported.
- **BCF API 3.0**: issues. BCF can reference files through `open-cde-documents` URLs.
- Governance: the Open CDE workgroup meets fortnightly [21][23].

## Software certification

- Two active tracks: **IFC2x3 Coordination View 2.0** and **IFC4** (Reference View and Design Transfer View, export and import certified separately; round-trip is not covered) (snippet [36]).
- Process: vendors run automated test routines defined by bSI and receive a certificate only after passing all tests; certified vendors may display the logo (snippet [36]).
- Examples: Bricsys got IFC4 Architectural Reference Exchange export certification (announced 28 Jan 2025); Vectorworks IFC4 RV 1.2 import certification (2023); Graphisoft IFC4 RV import certification listed as delivered in March 2025 (snippets [36]).
- Criticism (community forum): a user described the process as a black box and expensive; another noted listings lacked reports; "snapshot in time or renewed?" is a recurring question [36].
- Certification is not the same as the Validation Service, and IDS support lists are not certification [18].
- bSI also has "use case certification" and a redeveloped certification programme; I could not fetch those pages (gap).

## Chapters and rooms

- Chapter types: **Full Chapters** (vote in governance), **Developing Chapters**, **Chapters In-Formation** (12 months to progress). An April 2025 announcement said 19 Full Chapters and 37 chapters in total (snippet [38]).
- Examples seen in results: Australasia, Benelux, Canada, China, Finland, France, German speaking, Hong Kong, Italy, Japan, Korea, Malaysia, Nordic, North America, Norway, Singapore, Spain, Switzerland, Austria, Sweden, Portugal (now full), Poland and Greece (in development/formation) (snippets [38]; list is Wikipedia-derived and may be out of date).
- **Rooms**: bSI organises technical work in "rooms" (for example Infrastructure, Building, Regulatory, Product, Openings rooms). I could not confirm the current list because the web search budget was exhausted (unverified). Ask for a follow-up if this matters.

## IFC5 / IFCX

- Repository `buildingSMART/IFC5-development` holds "IFC 5 alpha Examples" that are preliminary, "not suitable for production use"; the schema is written in TypeSpec in `/schema`; JSON schemas to be published at ifcx.dev [37].
- bSI announced that the "IFCX Core & Modularisation" final project plan passed a further approval stage and moves to funding and delivery, seeking sponsors (dated 26 Aug 2026 per search snippet; unverified, page returned 403) [37].
- Community reaction (forum, OSArch): some expect 5-10 years before real use; concern about proprietary extensions (community opinion) [37].
- Third-party summary claims OpenUSD-influenced composition and JSON-first serialisation (unverified).
- Practical for testers: no mainstream tool exports IFC5 production models; expect MCP servers to say "IFC5 not supported".

## Typical questions people ask about this

1. What is the difference between IFC validation and IDS checking? (illustrative; answer: [1][4][20])
2. Which IFC version should I export from Revit for coordination: IFC2x3 CV2.0 or IFC4 Reference View? (illustrative)
3. Is IFC4 Design Transfer View still worth using? (illustrative; see [30][31])
4. Is there an official IFC4.3 Design Transfer View? (real topic: [31], answer: no, never published)
5. Is certification a snapshot in time or renewed? (real thread: https://forums.buildingsmart.org/t/is-certification-a-snapshot-in-time-or-is-it-renewed/4862)
6. What does "IFC4 certified" actually verify? (real discussion, see forum thread above)
7. Why does the Validation Service say my IfcGuid is not a 128-bit number / GlobalId invalid? (real thread: https://forums.buildingsmart.org/t/fatal-error-ifcguid-is-not-a-128-bit-number/3137)
8. How do I write an IDS requiring `Pset_WallCommon.FireRating` on all walls? (illustrative; answer in property facet [9])
9. How do I make an IDS check all elements (there is no "IfcElement" wildcard)? (illustrative; answer: list subtypes, [13])
10. Can IDS check geometry (wall thickness, clearance)? (illustrative; mostly no, only properties/quantities)
11. Why does IDS fail a material named "S275" when I asked for "Steel"? (illustrative; name vs category [12])
12. Why does my IDS pass in one checker and fail in another? (illustrative; check IFC version, IDS Audit, test cases [15])
13. How do I convert IDS results to BCF issues? (illustrative; IfcTester `reporter.Bcf` [19], structure unspecified [15])
14. How do I get a bSDD class by code through API? (illustrative; SearchList and Class [28])
15. Do I need an account for the bSDD API? (illustrative; public methods no, secured yes [28])
16. BCF 2.1 vs 3.0: which should my tool write? (illustrative; see [22][24])
17. Why are my BCF viewpoints not showing the right elements? (illustrative; IfcGuid vs AuthoringToolId [22])
18. How do I connect to a CDE with BCF-API? (illustrative; OpenCDE Foundation then BCF-API [25][23])
19. What is the file size limit of the Validation Service? (answer: 256 MB, unzipped .ifc [1])
20. When will IFC5 be ready? (illustrative; see IFC5 section [37])
21. What is a "warning" vs "error" in validation? (answer: industry practice = warning [1])
22. Which MVD does an IFC4.3 infrastructure export use? (illustrative; AbV [31][32])

## Common pitfalls and misconceptions

- "Validated by buildingSMART" does not mean software is certified; and "IDS-supporting" in the bSI list is vendor self-reported [18].
- A file can pass the Validation Service and fail an IDS (and vice versa) [1][4].
- IDS entity names are UPPERCASE and non-inheriting; `IFCWALL` does not cover `IFCWALLSTANDARDCASE` unless listed (verify per schema version) [13].
- IDS `uri` is not checked; it is documentation only [9][11].
- IDS property facet treats quantities and properties the same; IFC2X3 has no `Qto_` sets [9].
- IDS pass for property requires non-empty value; an existing but empty property fails [9].
- Prohibited IDS facets with a value still allow null/missing [11][14].
- BCF 3.0 viewpoints are immutable; update by creating a new viewpoint [22].
- BCF files are zips with GUID folders; renaming to `.zip` helps inspection (practical tip, not from a source).
- Certificates cover import or export of a specific MVD; they do not cover round-trip [36].
- mvdXML is old (2016) and IFC4.3 MVD files are generated artifacts; many tools do not consume mvdXML at all (unverified).
- IFC5 is alpha; do not expect compatibility with IFC4 tooling.
- Validation Service documentation can lag the service (docs said 0.8.4 while release notes were at 1.0.5) [1][3].

## Gaps and notes

- Web search budget ran out before I could verify: current bSI "rooms" list, Revit/Autodesk IFC export documentation, certification fees and expiry, BCF 2.1 vs 3.0 official change list, bSDD API v2 (not mentioned in sources), mvdXML 1.1 current repository URL.
- Hosts that returned HTTP 403 to fetch: buildingsmart.org, technical.buildingsmart.org, standards.buildingsmart.org, iso.org, mdpi.com. Facts from these come from search snippets.
- No suspicious or pirated sites encountered; none linked.
- Mirrors of IfcOpenShell on third-party hosts appeared in search; I did not use them as sources.

## Sources

- [1] Validation Service user guide: https://buildingsmart.github.io/validate/user/index.html
- [2] Validation rule details: https://buildingsmart.github.io/validate/dev/rule_details.html
- [3] Validation Service release notes (forum): https://forums.buildingsmart.org/t/validation-service-updates/4992?page=2 and https://forums.buildingsmart.org/t/validation-service-updates/4992
- [4] bSI Validation Service page (snippet): https://technical.buildingsmart.org/services/validation-service/
- [5] IDS repository: https://github.com/buildingSMART/IDS
- [6] IDS user manual: https://github.com/buildingSMART/IDS/blob/development/Documentation/UserManual/README.md
- [7] IDS specifications: https://raw.githubusercontent.com/buildingSMART/IDS/development/Documentation/UserManual/specifications.md
- [8] partOf facet: https://raw.githubusercontent.com/buildingSMART/IDS/development/Documentation/UserManual/partof-facet.md
- [9] Property facet: https://raw.githubusercontent.com/buildingSMART/IDS/development/Documentation/UserManual/property-facet.md
- [10] Restrictions: https://raw.githubusercontent.com/buildingSMART/IDS/development/Documentation/UserManual/restrictions.md
- [11] Classification facet: https://raw.githubusercontent.com/buildingSMART/IDS/development/Documentation/UserManual/classification-facet.md
- [12] Material facet: https://raw.githubusercontent.com/buildingSMART/IDS/development/Documentation/UserManual/material-facet.md
- [13] Entity facet: https://raw.githubusercontent.com/buildingSMART/IDS/development/Documentation/UserManual/entity-facet.md
- [14] Attribute facet: https://raw.githubusercontent.com/buildingSMART/IDS/development/Documentation/UserManual/attribute-facet.md
- [15] IDS developer guide: https://raw.githubusercontent.com/buildingSMART/IDS/development/Documentation/ImplementersDocumentation/developer-guide.md
- [16] IDS Audit tool: https://github.com/buildingSMART/IDS-Audit-tool
- [17] IDS v1.0 final announcement (snippet): https://www.buildingsmart.org/?p=30065
- [18] IDS software implementations list (snippet): https://technical.buildingsmart.org/ids-software-implementations/
- [19] IfcTester docs (snippet): https://docs.ifcopenshell.org/ifctester.html ; https://www.pypi.org/project/ifctester
- [20] Wikipedia, Information Delivery Specification (community encyclopedia): https://en.wikipedia.org/wiki/Information_Delivery_Specification
- [21] BCF-XML repository: https://github.com/buildingSMART/BCF-XML
- [22] BCF-XML 3.0 specification: https://raw.githubusercontent.com/buildingSMART/BCF-XML/release_3_0/Documentation/README.md
- [23] BCF-API: https://github.com/buildingSMART/BCF-API
- [24] BCF-XML changelog: https://github.com/buildingSMART/BCF-XML/blob/release_3_0/ChangeLog.md
- [25] OpenCDE Foundation API: https://github.com/buildingSMART/foundation-API
- [26] OpenCDE Documents API: https://github.com/buildingSMART/documents-API
- [27] bSDD repository: https://github.com/buildingSMART/bSDD
- [28] bSDD API doc: https://raw.githubusercontent.com/buildingSMART/bSDD/master/Documentation/bSDD%20API.md
- [29] bSDD data dictionary page (snippet): https://standards.buildingsmart.org/DataDictionary/
- [30] Graphisoft Archicad MVD help: https://help.graphisoft.com/AC/29/INT/_AC29_Help/121_IFC/121_IFC-47.htm
- [31] Forum, official MVDs for IFC 4.3 (community): https://forums.buildingsmart.org/t/official-model-view-definitions-for-ifc-4-3/5737
- [32] Alignment-based View project plan (snippet): https://www.buildingsmart.org/?p=32589
- [33] ISO 29481-2:2025 (snippet): https://www.iso.org/standard/88516.html
- [34] ISO 29481-3:2022 (snippet): https://www.iso.org/standard/81261.html
- [35] ISO 29481-1:2016 news (snippet): https://committee.iso.org/sites/tc59/home/news/content-left-area/news-and-updates/iso-29481-12016-is-published.html
- [36] Certification (snippets): https://technical.buildingsmart.org/services/certification/benefits/ ; https://www.bricsys.com/news/bricscad-is-officially-ifc4-certified ; https://forums.buildingsmart.org/t/is-certification-a-snapshot-in-time-or-is-it-renewed/4862 ; https://www.buildingsmart.org/compliance/use-case-certification/
- [37] IFC5: https://github.com/buildingSMART/IFC5-development ; https://community.osarch.org/discussion/3587/ifcx-core-project-update-by-buildingsmart (community) ; https://www.buildingsmart.org/?p=33789 (snippet)
- [38] Chapters (snippets): https://www.buildingsmart.org/chapter-directory/ ; https://www.buildingsmart.org/?p=32217
- [39] Xbim IDS validator (snippet): https://www.github.com/xBimTeam/Xbim.IDS.Validator
- [40] MVD whitepaper and policy: https://standards.buildingsmart.org/documents/bS_LDWG_MVD_Whitepaper_final_2017.pdf ; https://www.buildingsmart.org/wp-content/uploads/2021/05/20210425_MVD-policy_IFC4.x.pdf
- [41] BCF in IfcOpenShell (snippet): https://docs.ifcopenshell.org/bcf.html
