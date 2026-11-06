# IFC viewers, model checkers, CDE platforms and converters

## In plain words

An IFC file is just a text file describing a building; nobody works with it raw. Four families of software sit around it. **Viewers** open it and let you look, filter and read properties. **Checkers** test it (does it have the required properties, do the walls clash with the ducts, is the schema valid). **CDEs** (Common Data Environments) are cloud project spaces where models, drawings and issues are stored and exchanged under rules such as ISO 19650. **Converters** turn IFC into something else (glTF, OBJ, DWG, PDF, Excel, a viewer's private format) or clean and merge it. An MCP server that "opens, queries and edits IFC" overlaps with all four, so a tester needs to know what a human would normally use for each job and what a reasonable answer looks like.

Last researched: 2026-11-06

> **Research limits (read first).** The web-search budget of this run was exhausted before the first query succeeded, so everything below is based on direct page fetches of vendor and standards pages (about 35 attempted, roughly half returned usable text; several returned 403/404 or an unreadable shell) plus the author's background knowledge. Facts with a [n] marker were read on the cited page. Everything without a marker, or marked **(unverified)**, is background knowledge and must be re-checked before it is used to judge an answer. Prices are almost never published on the vendor pages and are mostly **(unverified)**. See "Gaps".

---

## 1. Big picture and vocabulary

| Term | What it means for a tester |
|---|---|
| IFC | Open exchange format (ISO 16739). Versions seen in the wild: IFC2x3 (still the most common deliverable), IFC4 / IFC4x3 (IFC 4.3 for infrastructure). Many tools support only some of them. |
| MVD | Model View Definition: a "profile" of IFC for a purpose (Coordination View 2.0 for IFC2x3, Reference View / Design Transfer View for IFC4). |
| BCF | BIM Collaboration Format: small zip files / API carrying *issues* (title, comment, camera viewpoint, GUIDs of the elements). Not a model. Almost every viewer and CDE below speaks BCF. |
| IDS | Information Delivery Specification: XML file (`.ids`) with machine-readable requirements ("every IfcDoor must have Pset_DoorCommon.FireRating"). The schema file is `Schema/ids.xsd` in the buildingSMART repository [6]. The IDS repository ships over 250 paired `.ids` / `.ifc` test cases for implementers [7]. |
| CDE | Common Data Environment: the single controlled place for project information (ISO 19650 term). |
| bSDD | buildingSMART Data Dictionary: online dictionary of classifications and properties that checkers can look up. |
| Federated model | Several discipline models (architecture, structure, MEP) loaded together without merging the files. |

Key distinction a tester must keep: a **viewer** reads; a **checker** judges; a **CDE** stores and controls access; a **converter** transforms. Many products do two or three of these (BIMcollab ZOOM = checker + federated viewer; Trimble Connect = CDE + viewer; Simplebim = converter + data editor).

---

## 2. Viewers

### 2.1 Desktop viewers

| Viewer | Notes |
|---|---|
| **BIMvision** | Free IFC viewer by a Polish vendor (vendor claims "advanced, free IFC model viewer") [4]. Extended by plugins: Multifile (several models in one window), IFC Merge, IFC Split, IFC Edit, Clash Detection, Compare (revision comparison), Advanced Reports and Takeoff Reports with Excel export, 2D projections, saved views. Export plugins listed: BCF, glTF, COBie, STL, OBJ, X3D [4]. Plugins are sold separately through a plugin store and licence page; prices not published on the page [4]. Windows only **(unverified)**. |
| **xBIM Xplorer** | Open-source Windows desktop reference viewer from the xBIM toolkit, WPF components, BCF plugin, builds against .NET Framework 4.7 [12]. Intended for developers; the licence text was not shown on the fetched page (the toolkit is generally described as CDDL, **unverified**). |
| **FZKViewer (KIT, Karlsruhe)** | Freeware viewer for BIM and GIS semantic models (IFC, CityGML). Last release 6.5.1, build 2587, dated 31 Jan 2023, marked "NO further development"; successor named as **KITModelViewer** [13]. Good for checking IFC2x3/IFC4 geometry and structure; many classic IFC test files were authored against it **(unverified)**. |
| **usBIM.viewer+** | Commercial desktop/cloud viewer family from ACCA software (Italy) with IFC viewing, clash and BCF **(unverified)**. The vendor page returned only a title when fetched [no usable source]. |
| **Open IFC Viewer** | Free lightweight IFC viewer **(unverified, not researched)**. |
| **DDS-CAD Viewer** | Free viewer from Data Design System (Nemetschek group) for IFC and DDS-CAD files **(unverified, not researched)**. |
| **IFC++ viewer** | Open-source C++ IFC reader/viewer project **(unverified, not researched)**. |
| **Solibri Anywhere** | Historically a free Solibri viewer. Solibri now states that Solibri Anywhere, Solibri Office, CheckPoint and Site are **legacy offerings no longer available**; existing customers keep contractual support [2]. See 3.1. |
| **Navisworks (Freedom / Manage)** | Autodesk coordination tool that imports IFC; used heavily for clash and 4D **(unverified for IFC version support; check the "File Readers" documentation)**. |

### 2.2 Web and cloud viewers

| Viewer | Notes |
|---|---|
| **Autodesk Viewer** | Free online viewer; requires a WebGL browser (Chrome 56+, Firefox 51+, Edge 14+ per the page) [22]. The fetched page did not list formats; IFC support is common knowledge but **(unverified here)**. |
| **Trimble Connect** | Cloud CDE with 3D/BIM model viewing and BCF topics, plus REST APIs and JS/.NET SDKs [15]. IFC viewing is standard in practice but the fetched developer page does not say so [15] **(unverified)**. |
| **Dalux BIM Viewer** | Free web/mobile viewer that combines discipline models and drawings; Dalux Box is the CDE; Field Basic is a free snagging app [17]. IFC import is the usual route into Dalux **(unverified; page does not say)**. |
| **Catenda Hub** | Browser 2D/3D review opened from a link, federated viewer, BCF issues, ISO 19650 workflows; vendor claims support for IFC 4.3, BCF and IDS, and offers REST APIs and an **MCP server** [16]. |
| **BIMcollab WebViewer** | Part of BIMcollab Twin; uploaded models sync with ZOOM [1]. |
| **Solibri WebChecker** | Listed as a current Solibri solution [3]; no detail fetched. |
| **BIMData.io** | French cloud platform with IFC viewer and API **(unverified, not researched)**. |
| **BIMFACE (Glodon, 广联达)** | Chinese "lightweight BIM engine": upload originals, conversion runs in the cloud; 50+ formats including IFC, SKP, DWG, 3DS, FBX; web viewer and APIs (e.g. clash detection) [19]. |
| **usBIM.browser** | Browser viewer in the usBIM platform **(unverified)**. |
| **Speckle** | Open-source platform / "data hub" with connectors; **Explore (Free)** plan: 1 project, up to 3 users, 30-day version history, "all file importers & connectors"; paid custom plans add unlimited projects/users, CDE integrations (Forma, ProjectWise), Automate, SSO; free for academia [8]. Speckle converts IFC into its own object model rather than showing the raw IFC **(unverified detail)**. |

### 2.3 Viewer toolkits (what developers build viewers with)

| Toolkit | Facts |
|---|---|
| **xeokit SDK** | Open-source WebGL viewer toolkit, licence **AGPL-3.0**; commercial licences via Creoox AG for closed-source or SaaS. Loads IFC2x3 and IFC 4.3 (normally converted to its compressed **XKT** format first), glTF, OBJ, STL, CityJSON, LAS/LAZ. Features: section planes, tree views, measurement, BCF viewpoints, federated models, double-precision coordinates [9]. |
| **web-ifc** (That Open) | JavaScript/TypeScript IFC reader/writer compiled to WebAssembly, licence **MPL-2.0**; works in browser and Node.js; also usable as a C++ library. The page did not name the supported schemas or mention glTF export [10]. |
| **That Open Engine / Components** | "Free and open source" libraries for web, Node.js, Electron and mobile BIM apps; the docs list IFC import, display, navigation, editing and export [11]. Many hobby and company web viewers are built on web-ifc + That Open Components. |
| **IfcOpenShell** | Open-source IFC library (C++/Python) with IfcConvert, IfcTester, Bonsai (Blender BIM add-on). The 0.9.0post1 documentation contains pages for IfcConvert (Installation, Usage) [23]. The most common engine behind IFC-aware MCP servers **(unverified)**. |

---

## 3. Model checkers

Checking means three different things; confusing them is the number one source of bad test expectations.

1. **Schema/syntax validity**: is the file legal IFC STEP (ISO 10303-21) and does it obey EXPRESS rules? Tool: buildingSMART Validation Service, IfcOpenShell validation.
2. **Content/information requirements**: does it contain what the contract demands (property sets, classification, naming)? Tools: IDS checkers, Solibri, BIMcollab ZOOM, Simplebim dataflows, dRofus.
3. **Coordination/geometry**: clashes, clearances, accessibility. Tools: Navisworks, Solibri, BIMcollab ZOOM, Revizto, BIMvision plugin.

### 3.1 Products

| Checker | What it does |
|---|---|
| **Solibri (rule-based checking)** | Solibri's own site now offers tiers **Starter, Essential, Advanced, Premium and Security+** (air-gapped), and solution areas: clash detection, data validation, accessibility, fire stopping, point-cloud checking, an AI assistant, IDS workflows, automated workflows and WebChecker. "A Nemetschek company" [3]. **Solibri Office and Anywhere (and CheckPoint, Site) are described as legacy and no longer available** [2][3]. Many tutorials, forum answers and BIM execution plans still say "Solibri Office"; a tester should expect that wording in prompts. |
| **BIMcollab ZOOM** | Model checking tied to BIM coordination: model combining and clash detection, **Smart Issues** (tracks clash status, avoids duplicates, Nightshift automation), **Smart Properties** (rules that enrich/restructure data without changing source models), **Smart Views** (filter/colour), drag-and-drop **Lists** for quantities, and **IDS checking** against requirements defined in BIMcollab. A free trial exists; pricing and platforms are on a separate page not readable in this run [1]. |
| **Navisworks** | Clash detection (Clash Detective), TimeLiner 4D, quantification; reads IFC among many formats **(unverified details)**. |
| **Simplebim** (Datacubist Oy, Tampere, Finland) | Desktop IFC data processing: imports and merges IFC from any source, runs "dataflows" to clean up, restructure, enrich and validate, exports back to IFC or data tables; does not alter the original file; free trial, licence prices not shown [18]. |
| **IDS validators** | Any tool that reads `.ids` and tests an IFC: IfcTester (Python, part of IfcOpenShell), Solibri, BIMcollab ZOOM [1], Catenda [16], others. buildingSMART publishes the schema and 250+ test pairs [6][7]. (IfcTester documentation page could not be fetched: 404.) |
| **buildingSMART Validation Service** | Hosted at validate.buildingsmart.org. The open-source repository describes four checks that can be run separately or together: **syntax, schema, Gherkin-rules** (rules from a separate `ifc-gherkin-rules` submodule) and **bSDD** (currently disabled). It is built to be run locally via Docker, with a React UI, Django API and Celery worker [5]. The hosted page itself returned only its title. |
| **Revizto** | Collaboration platform: clash automation, issue management with 2D/3D markups, API and an MCP server; integrates with Revit, Rhino, OpenRoads and 100+ plugins, formats and CDEs. IFC not mentioned on the fetched page [20]. |
| **dRofus** | Requirements-management and space-planning database; connects to Revit, ACC and Archicad, supports openBIM/IFC, validates design against requirements; **priced by project area** (single project or enterprise) [21]. |
| **Dalux / Catenda / Trimble Connect** | Basic model review, BCF issues; Catenda advertises IDS support and clash resolution [16]. |

### 3.2 What each check looks like in practice

- **Schema error example (validator output):** an IfcWall referencing a non-existent IfcOwnerHistory, or a required attribute `Name` written as `$` where the schema demands a value.
- **Content error example (IDS/Solibri):** "IfcDoor 2:3gSl... has no Pset_DoorCommon.FireRating" or "IfcSpace has no Qto_SpaceBaseQuantities.NetFloorArea".
- **Coordination example (ZOOM/Navisworks):** "Duct ID 0xA3 intersects beam B12 by 85 mm; hard clash; tolerance 10 mm".

---

## 4. CDE platforms

| Platform | Vendor / region | Facts |
|---|---|---|
| **Autodesk Construction Cloud (ACC) / BIM 360** | Autodesk | ACC replaced BIM 360 as the product line; Docs, Model Coordination, Build. Whether ACC opens/translates IFC is widely stated but the docs page fetched returned 404 **(unverified)**. |
| **Trimble Connect** | Trimble | Cloud CDE: file folders, 3D/BIM viewing, BCF topics, APIs (Core, Model, Organizer, Property Set, Topics), JS and .NET SDKs, extensions as iframes, embeddable components. New integrations should use latest API versions; legacy access applies to credentials issued in or before early 2026 [15]. Free and paid tiers exist **(unverified)**. |
| **Dalux (Build/Box, Field, FM, Handover)** | Dalux, Denmark | Box = CDE; BIM Viewer free; Field Basic free; FM and Handover modules; apps on iOS/Android; prices on request [17]. |
| **Catenda Hub** | Catenda, Norway **(unverified)** | "BIM-based CDE" with ISO 19650 workflows, BCF, IFC 4.3, IDS support, REST APIs, MCP server, AI assistants; document management advertised with unlimited users, no per-seat price; also Catenda Site and Catenda Duo [16]. Successor line of bimsync **(unverified)**. |
| **ProjectWise** | Bentley | CDE strong in infrastructure; Speckle lists ProjectWise as a CDE integration [8]. |
| **Aconex** | Oracle | Document/correspondence-centric CDE, strong for large owners **(unverified)**. |
| **Asite** | Asite, UK | Document/CDE platform, ISO 19650 messaging **(unverified)**. |
| **Thinkproject** | Germany/UK | CDE focused on documents and contracts **(unverified)**. |
| **KROQI** | Not confirmed (site did not resolve) | Described in discussions as a BIM collaboration platform **(unverified; fetch failed)**. |
| **Pilot-BIM** (ASCON / АСКОН) | Russia | Russian BIM-oriented CDE (СОД, среда общих данных). Fetch failed (connection refused) **(unverified)**. |
| **BIMFACE** | Glodon, China | Engine/API platform for web display, conversion and clash, rather than a classic CDE [19]. |
| **BIMcollab** (Nexus, ZOOM, Twin) | KUBUS, Netherlands **(unverified)** | Issue management (BCF) with ZOOM checking; Nexus listed under BIM Coordination, WebViewer under Twin [1]. |

---

## 5. Converters

### 5.1 Conversion map

| From -> To | Typical tool | Caveats |
|---|---|---|
| IFC -> glTF/GLB (3D web) | **IfcConvert** (IfcOpenShell), CAD Exchanger, BIMvision glTF plugin [4], web-ifc based pipelines | Geometry only plus limited properties; GUID-based element naming recommended for traceability. |
| IFC -> OBJ / DAE | IfcConvert, BIMvision PolyExt plugin [4] | Loses semantics (OBJ has no properties). |
| IFC -> STEP/IGES | IfcConvert, CAD Exchanger | Proper BReps only; very large models heavy. |
| IFC -> SVG / PDF drawings | IfcConvert (SVG plan/section output) then PDF printer | Not a replacement for a drawing set. |
| IFC -> DWG/DXF | ODA / Teigha based tools, Revit export, commercial converters | Quality varies; layers come from class names. |
| IFC -> Excel/CSV | Simplebim data tables [18], BIMvision Takeoff Reports [4], Blender Bonsai, IfcOpenShell scripts | Excel is for properties/quantities, never geometry. |
| IFC -> viewer-native format | xeokit **XKT** conversion [9], Autodesk Model Derivative (APS) | Closed or vendor-specific output. |
| IFC -> COBie | BIMvision COBie plugin [4], Bonsai | Spreadsheet-format COBie; check version. |

### 5.2 Products

- **IfcConvert (IfcOpenShell).** Open-source command line tool; the 0.9.0post1 documentation lists "Installation" and "Usage" pages [23] (body text could not be read in this run). From general knowledge (**unverified in this session**): output formats include OBJ, DAE, GLB, STP, IGS, SVG, XML, IFC and HDF5; options such as `--use-element-guids`, `--include` / `--exclude` filters, multithreading with `-j`, and local placement flags (e.g. `--site-local-placement`). Typical command: `IfcConvert model.ifc model.glb`. Run `IfcConvert --help` for the authoritative list.
- **CAD Exchanger.** Commercial SDK for reading, writing and visualising 30+ CAD/BIM formats, IFC included; exports include STEP, JT, glTF, FBX; callable from C++, Python, C#, Java and JavaScript, runs in Docker; pricing not stated; separate "Lab" desktop product exists [14].
- **Simplebim.** See 3.1 [18].
- **ODA (Open Design Alliance).** Offers an IFC SDK/toolkit used inside many CAD products **(unverified; the vendor page returned 404)**.
- **APS Model Derivative (Autodesk Platform Services).** Cloud API that translates uploaded design files into viewable formats (SVF/SVF2) and some neutral formats **(unverified; both documentation pages returned empty shells)**. Billing uses a consumption model **(unverified)**.
- **Online converters** (IFC to glTF, OBJ, DWG, PDF, Excel). Many free websites exist. They require uploading a model (possibly confidential) to a third party; a tester should avoid real project files and treat result quality as unverified. No specific site is recommended or linked here.
- **web-ifc / That Open** can be used to write custom converters in JS/Node [10][11].

---

## 6. Comparison table

| Platform | Category | Price model | IFC versions | Strengths |
|---|---|---|---|---|
| BIMvision | Desktop viewer | Free viewer; paid plugins [4] | Not stated on page | Plugin ecosystem (merge, split, edit, clash, reports, glTF/COBie/BCF export) [4] |
| xBIM Xplorer | Desktop viewer (dev) | Open source | Not stated [12] | .NET reference, BCF plugin [12] |
| FZKViewer | Desktop viewer | Freeware, discontinued (2023) [13] | Not stated [13] | Semantic BIM/GIS inspection; successor KITModelViewer [13] |
| Solibri tiers | Checker | Tiered subscriptions (Starter..Security+) [3]; Office/Anywhere legacy [2] | Not stated | Rule-based QA, IDS workflows, accessibility, fire-stopping, AI assistant [3] |
| BIMcollab ZOOM | Checker + viewer | Subscription; trial [1] | Not stated [1] | Smart Issues, Smart Properties, IDS, BCF, clash [1] |
| Simplebim | Converter / data tool | Licence + trial [18] | Not stated [18] | Merge, clean, validate, export without touching source [18] |
| buildingSMART Validation | Validator | Free hosted service; open-source code [5] | Not stated [5] | Official syntax/schema/Gherkin rule checks [5] |
| Revizto | Coordination | Paid; pricing page not read [20] | Not stated [20] | Clash automation, issues, API, MCP [20] |
| dRofus | Requirements | Priced by project area [21] | IFC (versions not stated) [21] | Requirements vs model, Revit/ACC/Archicad [21] |
| Trimble Connect | CDE + viewer | Tiered (unverified) [15] | Not stated [15] | APIs, BCF, extensions [15] |
| Dalux | CDE/field/FM | Free viewer and Field Basic; quote for rest [17] | Not stated [17] | Mobile, site quality, FM [17] |
| Catenda Hub | CDE | Quote; unlimited users in document mgmt [16] | IFC 4.3 claimed [16] | IDS, BCF, MCP server, REST [16] |
| Speckle | Data platform | Free tier 1 project/3 users; custom plans [8] | Via importers [8] | Connectors, versioning, Automate [8] |
| xeokit | Web SDK | AGPL-3.0 or commercial [9] | IFC2x3, IFC 4.3 [9] | High-performance WebGL, XKT [9] |
| web-ifc | Library | MPL-2.0 [10] | Not stated [10] | WASM, browser and Node [10] |
| CAD Exchanger | Converter SDK | Commercial, price not shown [14] | Not stated [14] | 30+ formats, glTF/STEP export [14] |
| BIMFACE | Cloud engine | Pricing link, not read [19] | IFC listed [19] | Cloud conversion, large-model web view [19] |
| IfcConvert | Converter CLI | Open source | See `--help` | OBJ/GLB/STEP/SVG output **(unverified)** |

---

## 7. Why this matters for MCP-server testing

- An IFC MCP server is not a viewer: it can return counts, properties and GUIDs, but usually not a picture. A good test asks for numbers or element lists, then verifies them in a real viewer (BIMvision, FZKViewer, Dalux, Trimble Connect, xeokit demo).
- To judge "validate my model" answers, check which of the three meanings of checking (schema, content, coordination, see section 3) the server actually performed. A server that parses the file and finds no errors has not run the buildingSMART Gherkin rules.
- "Export to glTF/OBJ/Excel" answers can be cross-checked: glTF/OBJ geometry vs the viewer; Excel contents vs property sets [4][18].
- Revit-side tasks (drive Revit) should be compared with the Revit IFC export dialog, not with a viewer. Viewers only show the result.
- Several vendors now advertise their own MCP servers (Catenda [16], Revizto [20]); a tester can use them as reference behaviour. Their completeness is **(unverified)**.

---

## Typical questions people ask about this

None of these were found live (search unavailable); all are **(illustrative)** unless noted.

1. What is the best free IFC viewer for a non-BIM person? (illustrative)
2. Can I open an IFC file in the browser without installing anything? (illustrative)
3. Is BIMvision really free, and what do the plugins cost? (illustrative)
4. Solibri Office is gone, what do I use for rule checking now? (illustrative; see [2][3])
5. How do I check my IFC against an IDS file? (illustrative; see [1][6])
6. What does the buildingSMART validation service actually check? (illustrative; see [5])
7. Why does my IFC open in one viewer but not in another? (illustrative)
8. How do I convert IFC to glTF/GLB for the web? (illustrative; see [10][14])
9. How do I convert IFC to Excel with all properties? (illustrative; see [4][18])
10. Which IFC version should I send to the checker, IFC2x3 or IFC4? (illustrative)
11. How do I share BCF issues between Revit, Solibri and BIMcollab? (illustrative)
12. Does ACC/BIM 360 open IFC natively? (illustrative)
13. What is the difference between a CDE and a viewer? (illustrative)
14. How can I merge several IFC models into one? (illustrative; see [4][18])
15. Is xeokit free for commercial use? (illustrative; see [9])
16. What is XKT and why do I need to convert IFC first? (illustrative; see [9])
17. Which tool shows clashes between structure and MEP? (illustrative)
18. What happened to FZKViewer? (illustrative; see [13])
19. Can I use Speckle with IFC and what does the free plan include? (illustrative; see [8])
20. How does dRofus compare room requirements with an IFC? (illustrative; see [21])
21. Which CDE is ISO 19650 compliant and supports IDS? (illustrative; see [16])
22. Are online IFC converters safe for confidential projects? (illustrative)
23. Why is my converted OBJ missing colours or in the wrong place? (illustrative)

---

## Common pitfalls and misconceptions

- **"Validated" is ambiguous.** Valid schema != meets the client's information requirements != no clashes. See section 3.
- **Outdated tool names.** Prompts and old documents still mention Solibri Office/Anywhere, which the vendor lists as legacy, no longer available [2].
- **Discontinued software.** FZKViewer has had no development since 2023 [13]; do not expect IFC4.3 support from it **(unverified)**.
- **Viewer differences.** Different viewers triangulate, colour and place the same file differently; a "wrong" display in one viewer is not proof the IFC is broken.
- **Licensing of toolkits.** xeokit is AGPL-3.0 and needs a commercial licence for closed-source use [9]; web-ifc is MPL-2.0 [10].
- **BCF is not IFC.** Opening a BCF in a viewer needs the matching model loaded; GUID mismatch is the usual reason an issue "doesn't show".
- **CDE != storage only.** Features such as IFC viewing and checking vary per vendor; vendor claims such as "supports IFC 4.3" [16] should be tested.
- **Converting loses information.** OBJ/glTF carry little semantic data; Excel carries no geometry; "round trip" IFC -> X -> IFC is lossy.
- **Prices change.** Treat any price statement as stale unless read on the vendor page; most vendors here publish none [3][14][17][19].
- **Upload risk.** Online converters and free cloud viewers may keep a copy; use sample models.

---

## Gaps

- **Search unavailable.** The run's web-search budget (200 per turn, shared) was already used up; zero searches succeeded. No forum or community questions could be collected, no native-language (Russian, Chinese, German, Norwegian, Italian) searches were done, and the "typical questions" are illustrative.
- **Pages that failed to fetch:** technical.buildingsmart.org software page (403), buildingsmart.org IDS page (403), technical.buildingsmart.org IDS project page (403), pricing.bimcollab.com (404), ACC help pages (404), APS Model Derivative pages (empty shells), ODA IFC page (404), IfcTester docs (404), IfcOpenShell IfcConvert usage body (not returned), usBIM (title only), validate.buildingsmart.org (title only), pilot-bim.ru (connection refused), kroqi.io (DNS failure), Solibri legacy page (404).
- **Not researched at all:** Open IFC Viewer, DDS-CAD Viewer, IFC++ viewer, Navisworks IFC import versions, ProjectWise, Aconex, Asite, Thinkproject, BIMData, online converter sites (none linked; no suspicious sites were deliberately visited), IFC schema version support per product.
- **Needs re-verification:** every **(unverified)** item and every price/tier statement.

---

## Sources

Only pages that returned readable content are cited; all were read on 2026-11-06.

- [1] https://bimcollab.com/en/products/bimcollab-zoom
- [2] https://www.solibri.com/solibri-anywhere
- [3] https://www.solibri.com/
- [4] https://bimvision.eu/en/ (content returned in German)
- [5] https://github.com/buildingSMART/validate
- [6] https://github.com/buildingSMART/IDS
- [7] https://github.com/buildingSMART/IDS/blob/development/Documentation/README.md
- [8] https://speckle.systems/pricing/
- [9] https://xeokit.io/
- [10] https://github.com/ThatOpen/engine_web-ifc
- [11] https://docs.thatopen.com/intro
- [12] https://github.com/xBimTeam/XbimWindowsUI
- [13] https://www.iai.kit.edu/english/1302.php
- [14] https://cadexchanger.com/products/sdk/
- [15] https://developer.trimble.com/docs/connect/
- [16] https://catenda.com/
- [17] https://www.dalux.com/
- [18] https://www.simplebim.com/
- [19] https://www.bimface.com/
- [20] https://revizto.com/en/
- [21] https://www.drofus.com/en
- [22] https://viewer.autodesk.com/
- [23] https://docs.ifcopenshell.org/ifcconvert/usage.html (navigation only; body not read)
