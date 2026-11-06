# What IFC is: history, versions, ISO, buildingSMART, software support

Last researched: 2026-11-06 (fact-checked 2026-11-06, see `_meta/qa/qa-basics-1.md`)

## In plain words

IFC (Industry Foundation Classes) is an open, vendor-neutral file format and data model for describing buildings and civil structures: not just 3D shapes, but also what each object *is* (wall, door, pipe, bridge), what it is made of, where it sits in the building, and what properties it has. It is maintained by buildingSMART International and published as the international standard ISO 16739-1. People use it to pass a model between programs that cannot read each other's native files (for example Revit to Archicad, Tekla or a model checker). Several versions exist side by side, and the "right" one depends on who receives the file, so most real-world IFC questions are version questions: IFC2x3 (old, still very common), IFC4 (modern buildings), IFC4.3 (adds roads, rail, bridges, ports, waterways), IFC5 (still experimental). An MCP server that opens or edits IFC must read the schema name in the file header first, because entity names and available features differ between versions.

## 1. Definition and where it sits

- **IFC** = a data schema (written in the EXPRESS language, ISO 10303-11) plus several file serialisations. The schema describes classes such as `IfcWall`, `IfcDoor`, `IfcBeam`, `IfcSpace`, `IfcBuildingStorey`, relationships such as `IfcRelAggregates`, property sets such as `Pset_WallCommon`, and geometry representations. [1][5]
- **Serialisations (file formats)** [1][23]:
  - IFC-SPF, `.ifc`: plain text, the most common; follows ISO 10303-21 ("STEP physical file"). The header contains `FILE_SCHEMA(('IFC4'))` or similar, which is how you tell the version.
  - IFC-XML, `.ifcXML` (ISO 10303-28).
  - IFC-ZIP, `.ifcZIP`: compressed SPF or XML.
  - Others: ifcJSON, ifcOWL (RDF/Turtle), ifcHDF. Rare in daily practice.
- **ISO**: the schema is ISO 16739-1 "Industry Foundation Classes (IFC) for data sharing in the construction and facility management industries - Part 1: Data schema". The 2024 edition (ISO 16739-1:2024) replaced the 2018 edition and added infrastructure (bridges, roads, railways, waterways, port facilities). [8][9] The technical committee is ISO/TC 59/SC 13. [8]
- **IFC is exchange, not authoring**: it is a neutral "delivery format". Native formats (RVT, PLN, DGN) remain the working formats. IFC export is lossy by design (parametric behaviour, families, many view settings do not survive).
- Words you will hear: *openBIM* (workflow built on open standards: IFC, BCF, IDS, bSDD), *MVD* (Model View Definition: a subset of IFC for one exchange purpose), *IDS* (Information Delivery Specification: machine-readable requirements for an IFC file's content), *BCF* (BIM Collaboration Format: issue tracking), *bSDD* (buildingSMART Data Dictionary). [2]

## 2. buildingSMART International and chapters

- **buildingSMART International (bSI)** is the non-profit that develops and maintains openBIM standards: IFC, MVD/IDM, bSDD, BCF, IDS, plus the software certification programme. [2][22]
- **Name history**: 1994 Autodesk invited about twelve US companies into a consortium to advise on C++ classes for integrated applications; September 1995 membership opened as the "Industry Alliance for Interoperability"; renamed "International Alliance for Interoperability" (IAI) in May 1996 (QA: Wikipedia gives May 1996; an earlier draft said "1996 or 1997"); 2005 renamed buildingSMART because the old name was judged too long and complex. [1][2][3]
- **Chapters**: bSI works through national or regional chapters (about 38 distinct chapters in the Wikipedia list at QA time; earlier draft said "roughly 30"; Wikipedia is a secondary source), for example UK & Ireland, German-speaking region, Nordic, Netherlands/Benelux, France, Italy, Spain, Japan, Korea, Singapore, Australasia, North America. Status levels exist ("Chapter-in-formation", "Developing Chapter", "Full Chapter"). [2][40] The exact current roster changes; use the official chapter directory (https://www.buildingsmart.org/chapter-directory/). Chapters publish local guidance (national IFC mandates, templates), which is often what a user actually asks about.
- The 2024 bSI publication "Global IFC Mandates" lists countries/clients that require IFC (it includes Singapore, Denmark, Japan, Poland, among others per search snippets; the PDF itself could not be fetched, so details are unverified). [34] A Nordic report states that IFC2x3 is the most used version and that BIM requirements usually come from clients (often public bodies), not from national law. [35]

## 3. History and version table

Dates differ between sources (publication date of a candidate, official release, ISO date). The buildingSMART "IFC Specifications Database" is the authoritative list; I could only see it through search-result summaries because the site blocked direct fetching (HTTP 403). [4]

### 3.1 Narrative

1. **1994-1996**: Autodesk-led consortium, then the Alliance; first IFC release **IFC 1.0 in June 1996**. [1][2]
2. **1997-1999**: IFC 1.5 (Nov 1997), 1.5.1 (Sept 1998), **IFC 2.0 (March 1999)**. [1]
3. **IFC2x** and **IFC2x2** (incl. Addendum 1, July 2004): intermediate, little used today. [1]
4. **IFC2x3 (Feb 2006)**: the first widely implemented version; submitted to ISO and published as **ISO/PAS 16739:2005** (Publicly Available Specification). **IFC2x3 TC1** (Technical Corrigendum 1; version 2.3.0.1, listed as published 2007-07) fixed problems and is the form people mean by "IFC2x3". [1][3][4]
5. **IFC4 (March 2013)**, formerly called IFC2x4, became **ISO 16739:2013**. [1][3]
6. **IFC4 Add1 (2015)** and **Add2 (2016)**: addenda fixing pilot-implementation issues; Add1 was the baseline for the first Reference View / Design Transfer View, Add2 improved geometry definitions for certification. **IFC4 Add2 TC1 (version 4.0.2.1, listed Oct 2017)** is what became **ISO 16739-1:2018**. [3][4][9]
7. **IFC4.1** (infrastructure alignment work, first extension) and **IFC4.2** (April 2019, per Wikipedia - checked in QA): research/intermediate releases, now listed as **withdrawn** by buildingSMART. [1][4] (The date given for IFC4.1 is garbled in Wikipedia ("2018-86"): unverified. The IFC release notes put alignment, linear placement and `IfcSectionedSolidHorizontal` in IFC4.1, and `IfcBridge` / `IfcFacilityPart` in IFC4.2.)
8. **IFC4.3**: development through release candidates (e.g. RC4, which some tools still reference), **approved by ISO in January 2024** (buildingSMART announcement 4 Jan 2024; its New Year message says 3 Jan), officially published **April 2024 (announcement 2 Apr 2024) as IFC 4.3.2.0 (= IFC4.3 ADD2) = ISO 16739-1:2024**; the specification database row reads "4.3.2.0 / IFC 4.3 ADD2 / ISO 16739-1:2024 / 2024-04 / Official" (seen in search results, QA-checked). [4][6][7][10] There is no separate "final" base IFC4.3 listed as official; people say "IFC4.3" but the schema identifier is `IFC4X3_ADD2`. [1][23]
9. **IFC4.4**: described in the buildingSMART database as in development, an extension of 4.3 (unverified in detail). [4]
10. **IFC5**: "next generation IFC", in development. The public repository `buildingSMART/IFC5-development` contains **alpha examples only** (JSON-based; the README says the JSON schema and extensions will be published on ifcx.dev - the term "IFCX" is not used in the README itself; schema source in TypeSpec; a viewer hosted at ifc5.technical.buildingsmart.org) and warns that the examples are preliminary, work in progress, "for educational and testing purposes only" and not suitable for production without refinement; it also asks not to create derivatives of the examples. [11] Community material says its composition model is influenced by OpenUSD and ECS-style data (secondary/unverified). IFC5 is not usable as a delivery format today.

### 3.2 Version table

| Version | Year | ISO / status | Schema id in file header | Key additions / notes |
|---|---|---|---|---|
| IFC 1.0 | 1996 (June) | none | n/a | First release |
| IFC 2.0 | 1999 (March) | none | n/a | Last of the early series |
| IFC2x / 2x2 | ~2000-2004 | none | `IFC2X`, `IFC2X2` (unverified spelling) | Intermediate; Revit still lists a "2x2 Coordination View" export setup [14] |
| IFC2x3 | 2006 | ISO/PAS 16739:2005 | `IFC2X3` | First mass-adopted version; Coordination View 2.0 etc. |
| IFC2x3 TC1 | 2007 (per bSI table) | Official [4] | `IFC2X3` | Corrigendum; de-facto standard; IfcCompoundPlaneAngleMeasure fix [3] |
| IFC4 | 2013 (March) | ISO 16739:2013 | `IFC4` | Better geometry (advanced B-rep, tessellation, B-splines), richer property templates and materials, 4D/5D/MEP/structural extensions, ifcXML improvements, new documentation format [3][28] |
| IFC4 Add1 | 2015 (July) | superseded | `IFC4` | Fixes; baseline for early RV/DTV [3] |
| IFC4 Add2 | 2016 (July) | retired | `IFC4` | Geometry definitions improved for certification [3][4] |
| **IFC4 Add2 TC1** | 2017 (Oct) | **ISO 16739-1:2018** | `IFC4` | Version 4.0.2.1; what "IFC4" means in practice today; Reference View 1.2 [4][9][20] |
| IFC4.1 | ~2018 | withdrawn [4] | `IFC4X1` (unverified) | Alignment research |
| IFC4.2 | 2019 (April) | withdrawn [4] | `IFC4X2` (unverified) | Intermediate |
| **IFC4.3 ADD2 (4.3.2.0)** | 2024 (April publication; ISO approval Jan 2024) | **ISO 16739-1:2024** | `IFC4X3_ADD2` | Infrastructure: facilities, alignment, roads, rail, bridges, ports, waterways; Alignment-based View [4][6][8][29] |
| IFC4.4 | in development | not published | n/a | Extension of 4.3 (unverified) [4] |
| IFC5 | alpha | none | n/a | JSON-based alpha examples (schema to be published on ifcx.dev per the repo README); not for production [11] |

National adoptions exist: for example Russia has **ГОСТ Р 10.0.02-2019/ИСО 16739-1:2018** (national version of the 2018 edition, reported as in force since 2019-09-01; the catalogue page timed out in QA, so the date is unverified; I found no sign of a GOST R for the 2024 edition); the European adoption **EN ISO 16739-1:2020** (title "Part 1: Data schema (ISO 16739-1:2018)", published 2 Mar 2020 in the Estonian EVS catalogue) is listed there as **withdrawn from 15 Apr 2024** and replaced by **EN ISO 16739-1:2024** (valid from 15 Apr 2024) (QA-verified in the EVS catalogue). [36]

## 4. What changed in IFC4.3 (infrastructure)

- ISO's description of the 2024 edition: added information for infrastructure facilities such as **bridges, roads, railways, waterways and port facilities**. [8]
- New spatial structure entities `IfcFacility` and `IfcFacilityPart` as base for infrastructure breakdown, with `IfcBridge` (+ `IfcBridgePart`), `IfcRoad`, `IfcRailway` (and marine/port-related parts; exact entity names for waterways/ports should be checked in the spec - unverified). [29][30]
- **`IfcAlignment`** reworked (horizontal, vertical, cant, segments), linear placement along an alignment, track/rail elements (`IfcRail`, `IfcTrackElement`), `IfcSectionedSurface`, `IfcOpenCrossProfileDef`, mooring and navigation devices. [29][30]
- The class hierarchy was reviewed because it was "very building-focused". [29] (From general spec knowledge, not verified in these sources: `IfcBuildingElement` was renamed `IfcBuiltElement` in 4.3.)
- For **building-only** projects 4.3 is mostly a backward-compatible superset of IFC4 and brings little extra. [28]
- Official MVDs for 4.3: a buildingSMART forum answer of 6 Nov 2024 says "there are two official ones for 4.3" without naming them; they are usually given as **Reference View** and **Alignment-based View (AbV)** (names from the 4.3 documentation as summarised earlier; not re-read in QA). A Design Transfer View for 4.3 "never materialised into an official MVD" (same forum answer). [19] AbV is described as a selection of concept templates for alignment-based exchange. [29]

## 5. Differences that matter to users

### 5.1 IFC2x3 is still dominant
- Practitioner and vendor sources agree that IFC2x3 (Coordination View 2.0) is the most supported and safest option for unknown recipients, e.g. an Autodesk manual calls it "the most supported and stable"; a Dutch Revit forum answer notes IFC2x3 is still the standard there. [14][37][35] Archicad's help calls IFC2x3 "the most widely used version" in older docs. [15]
- Some sources push the other way: IFC4 gives better curved geometry and properties and is recommended for modern projects. Sources disagree; the deciding factor is the receiving software and the project's BIM Execution Plan (BEP). [28][43]

### 5.2 IFC4 Reference View (RV) vs Design Transfer View (DTV) vs IFC2x3 Coordination View
- **Coordination View 2.0 (IFC2x3)**: the classic exchange for architecture/structure/MEP coordination. [14]
- **IFC4 Reference View (RV 1.2)**: official MVD on IFC4 Add2 TC1; geometry simplified (often tessellated meshes, smaller files); the receiver is *not supposed to modify* the model; it lacks some structures (e.g. material layer sets, named profiles like L/U) per forum critique. [18][20][28]
- **IFC4 Design Transfer View (DTV)**: intended as an extension of RV with richer parametric geometry (advanced B-rep, CSG) for further design work. The buildingSMART MVD database lists it as draft, and forum posts say it never became an official MVD; Revit's "IFC4 Design Transfer View" setup is therefore described as unofficial, "results may vary". [18][20]
- **Certification** covers RV (and for IFC2x3, CV 2.0) - not DTV. Revit's own help: IFC4 Reference View is a "certified version for Architectural and Structural export" (IFC4 RV 1.2); MEP export and import still "in progress". [14]

### 5.3 Practical rule of thumb (mine, synthesised)
| Situation | Pick |
|---|---|
| Recipient unknown / mixed old software / many subcontractors | IFC2x3 Coordination View 2.0 |
| Modern building project, recipients confirmed to read IFC4, viewing/checking/coordination | IFC4 Reference View |
| Receiver must edit/reuse geometry and both tools support it (test first) | IFC4 DTV (unofficial) or native exchange add-in |
| Roads, rail, bridges, tunnels, ports, alignments | IFC4.3 (Reference View / Alignment-based View) |
| Contract says "IFC4 certified" | RV from a tool certified for it; check the certified list |
| Research / early adopters | IFC5 alpha only for experiments |

## 6. Software support and certification

**Certification**: bSI runs a software certification programme (compliance). It is per tool, per version, per MVD and per direction (import/export); the certified list is on buildingSMART's site (b-cert). [22] A Nordic BIM guide (page dated 11 May 2026) states that **no software is currently certified for IFC4.3** and that certification is expected to start "soon" (status after May 2026 unverified: the buildingSMART certified-software page returned 403), and my search found no confirmation of an IFC4.3 or Alignment-based View certified product; the bSI "software implementations" list contains vendor self-declared claims that bSI does not verify. [10][22] Examples of IFC4 certification: Archicad received IFC4 Reference View export certification (v23, 2019) and import certification appears as delivered on Graphisoft's roadmap (2024 entry); BricsCAD announced "IFC4 Architectural Reference Exchange Export Certification" on 28 Jan 2025 (export only; QA-verified on the Bricsys news page). [21][45][46] Tekla's 2026 export help explicitly calls only the IFC2x3 **Coordination view 2.0** "certified" ("should be your default export type"); it does not state certification for its IFC4 or IFC4.3 views (an earlier draft claimed certification for IFC2x3 and IFC4 views, which the page does not say). [17]

| Product | IFC versions (per vendor docs, as found) | Notes |
|---|---|---|
| **Revit** (with Autodesk open-source IFC add-in, `Autodesk/revit-ifc`, LGPLv2) | Export setups: IFC 2x3 Coordination View 2.0, IFC 2x3 CV, IFC 2x2 CV, IFC 2x3 GSA Concept Design BIM 2010, IFC4 Reference View, IFC4 Design Transfer View. IFC4.3 is **not** in the version list of the Revit 2026 exporter help (26.4.1), but the exporter release notes for **24.3.40 / 25.4.40 / 26.4.1** (QA-corrected: an earlier draft said "25.3.40") each say "Added IFC4.3 Reference View exchange requirements", and releases 25.4.3 / 27.3.0.12 / 27.4.0.30 mention IFC4x3 export fixes (groups as IfcSystem types, IfcSlab entity type, pipe-fitting alignment, wall geometry) [12][13][14]. The 26.4.1 help also lists built-in setups "IFC 2x3 Basic FM Handover View", "IFC 2x3 COBie 2.4 Design Deliverable" and three IFC 4 Reference View setups (Architecture, Structural, BuildingService) [14] | Menu: File > Export > IFC (Modify Setup for options) - not confirmed on the fetched Autodesk help pages (unverified); import via File > Open > IFC or Insert > Link IFC. Open-source exporter is maintained for the current + two previous Revit versions (README, QA-verified) [12]. MEP incomplete. No official statement of full IFC4.3 export found (unverified) |
| **Archicad** (Graphisoft) | IFC2x3, IFC4, IFC4.3 import and export (Archicad 29 help) [15] | File > Interoperability > IFC (menu path not shown on the fetched help page: unverified); translators set in "IFC Translation Setup". Import by Open / Merge / Hotlink. A user thread reports 4.3 depth is limited (schema-specific entities/properties not fully handled) - single user opinion [16] |
| **Tekla Structures 2026** | Export IFC2x3, IFC4, IFC4.3 (IFC4X3_ADD2). Export types per the 2026 help: IFC2x3 - Coordination view 1.0 / 2.0, Surface geometry, Steel fabrication view; IFC4 and IFC4.3 - Reference view, Design transfer view; IFC4 only - Precast view; IFC4.3 only - Bridge view. IFC import of 4.3 supported; rebar assemblies need IFC4 not 2x3 [17] | File > Export > IFC (QA-verified) |
| **Bentley** OpenRoads / OpenRail Designer | Export to IFC; corridor options (alignment, semantics) available with IFC4x3 (older docs refer to Release Candidate 4) [24][25] | OpenBuildings: a community answer said no IFC4.3 export option at the time (undated); newer status unverified |
| **Autodesk Inventor 2026** | IFC 4x3 "has been included for both the Export Building Components workflow and Simplify to Revit" (QA-verified on the Inventor 2026 What's New page) [26] | |
| **IfcOpenShell / Bonsai** (open source) | Parsing of IFC2X3 TC1, IFC4 Add2 TC1, IFC4x1, 4x2, 4x3 Add2; geometry support mainly IFC2X3 and IFC4 per README (may be outdated) [23] | Python API used by many tools and test harnesses; `IFC4X3` maps to `IFC4X3_ADD2` |
| **BricsCAD BIM** | IFC4 certified export (2025) [21] | |

## 7. IFC vs native and other formats

| Format | What it is | IFC relationship |
|---|---|---|
| **RVT** (Revit) | Proprietary, parametric, full-fidelity project file; versions not backward compatible | IFC is the exchange layer. Re-importing IFC into Revit gives limited native fidelity (see pitfalls) |
| **PLN / PLA** (Archicad) | Proprietary Graphisoft project file; Archicad's IFC data model is closely tied to IFC | IFC is Archicad's main interoperability format |
| **DGN** (Bentley MicroStation) | Proprietary CAD/BIM file; Bentley also uses iModel | IFC export via connectors [24] |
| **DWG / DXF** | 2D/3D CAD | No BIM semantics |
| **gbXML** | XML for energy analysis (thermal zones, surfaces, materials, location); used by IES VE, EnergyPlus, DesignBuilder, eQUEST [31] | Use gbXML for energy simulation rather than IFC; IFC carries more semantics, not tailored to energy |
| **CityGML** (OGC) | City-scale 3D models with LODs, used by GIS | IFC -> CityGML is the usual direction; the reverse loses detail [31] |
| **LandXML** | Survey/civil data: surfaces, alignments, parcels [31] | IFC4.3 now carries alignments; LandXML stays common for survey/civil |
| **COBie** | Facility-management handover data as spreadsheet/data drops (not 3D), in UK BIM Level 2 [31] | Can be derived from IFC (FM Handover MVD) |
| **glTF / GLB** | Lightweight web/real-time mesh format | Visualisation only, no BIM semantics; IFC-to-glTF is common for web viewers |
| **dotbim (.bim)** | Very simple JSON format (meshes + key-value properties), not ISO; project README claims ~1 page of docs vs 100+ for IFC [32] | Easy to generate for scripts; far less expressive than IFC |
| **USD / OpenUSD** | Scene description format for layered collaboration (Omniverse etc.) | Research compares IFC, glTF and USD for BIM [33]; IFC5 alpha is influenced by USD-like composition (secondary source) |

Rule of thumb: native for authoring, IFC for BIM exchange and archive, gbXML for energy, CityGML for city/GIS, LandXML for survey/civil, COBie for asset handover, glTF/USD for visualisation.

## 8. Notes for testing MCP servers with IFC

(Practical synthesis for the QA audience, my interpretation.)
- Always check the schema in the file: `FILE_SCHEMA(('IFC2X3'))`, `IFC4`, `IFC4X3_ADD2`. A request like "list all IfcWall" works on all, but `IfcBuiltElement`, `IfcAlignment`, `IfcRoad`, tessellated geometry (`IfcTriangulatedFaceSet`) exist only in newer schemas. A good MCP answer states the schema version.
- Expect a tool built on IfcOpenShell to handle IFC2X3, IFC4, IFC4X3 differently (geometry coverage is better for 2X3 and 4). [23]
- A Revit-driving MCP should know which IFC export setup it uses (version + view). A request such as "export to IFC4.3" may legitimately be refused or limited in Revit. [14]
- IFC GlobalIds (22-character base64-like strings) persist across export where tools allow; Archicad Merge import generates new GlobalIds and stores the old as "External IFC ID". [15]

## Typical questions people ask about this

Real, found (links are in Sources):
1. "IFC4 Design Transfer View experiences?" - buildingSMART forum thread about whether DTV is official and usable. https://forums.buildingsmart.org/t/ifc4-design-transfer-view-experiences/4362
2. "Official Model View Definitions for IFC 4.3" - which MVDs exist. https://forums.buildingsmart.org/t/official-model-view-definitions-for-ifc-4-3/5737
3. "Exported IFC is missing elements while using IFC4 schema" - Revit users losing walls/windows/roofs when switching to IFC4. https://forums.autodesk.com/t5/revit-architecture-forum/expoted-ifc-is-missing-elements-while-using-ifc4-schema/m-p/11456115
4. "IFC 4.3 schema implementation in Archicad 29" - what Archicad actually supports. https://community.graphisoft.com/t5/Project-data-BIM/IFC-4-3-schema-implementation-in-Archicad-29/td-p/680785
5. "Are IFC2X3 or IFC4 format supported on Revit?" - Autodesk support article. https://www.autodesk.com/support/technical/article/caas/sfdcarticles/sfdcarticles/Is-IFC2X3-format-supported-on-Revit.html
6. "IFC open vs linking" in Revit - CAD Tutor thread. https://www.cadtutor.net/forum/topic/65270-ifc-open-vs-linking
7. "Difference between Tekla Export IFC and IFC4" - https://www.tek1.com.au/steel-detailing/difference-between-tekla-export-ifc-and-ifc4 (blog)
8. "IFC 4x3 vs 4.1 changes" - buildingSMART forum. https://forums.buildingsmart.org/t/ifc-4x3-vs-4-1-changes/3217

Illustrative (invented examples of what testers or users might ask):
9. (illustrative) "What IFC version is this file?" / "Show me the schema in the header."
10. (illustrative) "Which IFC version should I export from Revit for a client who uses Navisworks and Solibri?"
11. (illustrative) "Is IFC2x3 obsolete? Why do clients still ask for it?"
12. (illustrative) "What is the difference between IFC4 Reference View and Design Transfer View?"
13. (illustrative) "Does Revit export IFC4.3?"
14. (illustrative) "Is IFC4.3 only for infrastructure? Can I use it for a normal building?"
15. (illustrative) "Is any software certified for IFC4.3?"
16. (illustrative) "What's the difference between ISO 16739:2013 and ISO 16739-1:2018 and ISO 16739-1:2024?"
17. (illustrative) "Can I convert IFC back to a native Revit model without losing parametrics?"
18. (illustrative) "Is IFC5 ready? Should I wait for it?"
19. (illustrative) "Is IFC better than gbXML for energy analysis?"
20. (illustrative) "Why is my IFC file huge compared with the RVT?" / "Can I convert IFC to glTF for a web viewer?"
21. (illustrative) "Which IFC version should an MCP server use when creating a new model from scratch?"
22. (illustrative, Russian) "Какую версию IFC выбрать для экспорта из Revit - IFC2x3 или IFC4?" / (German) "Welche IFC-Version soll ich für den Austausch verwenden?"
23. (illustrative) "What is `IFC4X3_ADD2` in the file header and how is it different from `IFC4X3`?"

## Common pitfalls and misconceptions

- **"IFC4.3 is the newest, so always use it."** False for most building projects: tool support and certification lag (Nordic BIM, 11 May 2026: no certified software), and 4.3 adds little for buildings. Roads, rail, bridges need it. [10][28]
- **"IFC4 = IFC4.3."** Different editions: ISO 16739-1:2018 (IFC4 Add2 TC1) vs ISO 16739-1:2024 (IFC4.3.2.0). Entity names can differ (e.g. IfcBuiltElement, unverified).
- **"IFC2x3 is dead / not ISO."** IFC2x3 was published as ISO/PAS 16739:2005; it remains the commonly delivered version and the 2013/2018 editions are the ISO standards for IFC4. [3][4]
- **"Design Transfer View is an official, certified view."** It is not (draft/unofficial); only Reference View is certified. [18][20]
- **Version labels are ambiguous**: "IFC4.3" can mean RC4, 4.3.0.0, or 4.3.2.0 (ADD2); Bentley and Civil 3D docs still mention RC4. [24][44]
- **"IFC import gives me an editable Revit model."** Revit converts IFC to a Revit file (Link IFC creates an `.ifc.rvt` next to the file); elements often come in as generic/model-in-place objects, detail levels do not switch, MEP not natively editable. Practitioner reports, older. [38][39]
- **IFC export is not lossless round trip**: Revit help warns re-exported linked IFC may lose data. [14]
- **"IFC means certified."** "Exports IFC" is not "certified IFC4 RV export". Check the version, view, direction (import/export) and the product release.
- **Statements of "support" by vendors vs actual quality**: opening an IFC4.3 file does not guarantee correct data or geometry. [10]
- **IFC5 hype**: alpha JSON examples only; the repo README says they are for educational/testing purposes, not production, and asks not to create derivatives. [11]
- **Unrelated "IFC"**: International Finance Corporation (World Bank) pollutes search results; add "Industry Foundation Classes".

## Gaps

- buildingSMART.org, technical.buildingsmart.org, standards.buildingsmart.org and iso.org blocked direct fetching (HTTP 403); facts from them come from search-result summaries and are cross-checked against secondary pages. In particular the release dates for IFC2x3 TC1 (2007-07), IFC4 Add2 TC1 (2017-10) and IFC4.3 (2024-04) come from the bSI database as summarised by search, not read directly.
- Exact IFC4.1 date, schema ids `IFC4X1`/`IFC4X2`, `IFC2X2`: unverified.
- Current official list of IFC4.3-certified software: not found; check b-cert / buildingSMART certified software list (page returned 403 in QA on 2026-11-06).
- QA 2026-11-06: not re-verified (pages 403, timeout or search quota exhausted): ISO/TC 59/SC 13 assignment, IFC2x3 TC1 date (2007-07), IFC4.4 status, ГОСТ Р 10.0.02-2019 entry-into-force date, IfcOpenShell geometry-support statement (PyPI page failed to load), Bentley OpenRoads/OpenBuildings IFC4x3 statements, IFC4.1 date.
- Revit's native IFC4.3 export status: only the open-source exporter release notes were found.
- Global IFC Mandates PDF (2024) and national requirements: not read. 
- No suspicious or pirated sites were encountered or linked. Several mirror/aggregator pages (wiki mirrors, LLM-generated encyclopedias, converter-vendor marketing pages) were seen and deliberately not used as sources.

## Sources

[1] Wikipedia, Industry Foundation Classes - https://en.wikipedia.org/wiki/Industry_Foundation_Classes (secondary)
[2] Wikipedia, buildingSMART - https://en.wikipedia.org/wiki/BuildingSMART (secondary)
[3] BIMsupporters, History and versions of IFC - https://app.bimsupporters.com/courses/ifc/lessons/history-and-versions-of-ifc/ (training site, secondary)
[4] buildingSMART Technical, IFC Specifications Database / schema specifications - https://technical.buildingsmart.org/standards/ifc/ifc-schema-specifications/ (read via search summary; also https://technical.buildingsmart.org/?p=47)
[5] buildingSMART International, Industry Foundation Classes - https://www.buildingsmart.org/standards/bsi-standards/industry-foundation-classes/
[6] buildingSMART, IFC 4.3 approved as a final standard - https://www.buildingsmart.org/ifc-4-3-approved-as-a-final-standard/
[7] buildingSMART, IFC 4.3 formally approved and published as an ISO standard - https://www.buildingsmart.org/?p=29521
[8] ISO 16739-1:2024 - https://www.iso.org/standard/84123.html
[9] ISO 16739-1:2018 - https://www.iso.org/standard/70303.html
[10] Nordic BIM, IFC 4.3 - https://www.nordicbim.com/knowledge/en/ifc-4.3
[11] buildingSMART/IFC5-development - https://github.com/buildingSMART/IFC5-development
[12] Autodesk/revit-ifc - https://github.com/Autodesk/revit-ifc
[13] Autodesk/revit-ifc releases - https://github.com/Autodesk/revit-ifc/releases
[14] Autodesk, Revit IFC Help (Revit 2026 exporter 26.4.1) - https://up1.autodesk.com/2026/RVT/ADSKIFCExporterHelp_26_4_1.htm
[15] Graphisoft, Archicad 29 Working with IFC - https://help.graphisoft.com/AC/29/INT/_AC29_Help/121_IFC/121_IFC-1.htm
[16] Graphisoft Community (user thread), IFC 4.3 in Archicad 29 - https://community.graphisoft.com/t5/Project-data-BIM/IFC-4-3-schema-implementation-in-Archicad-29/td-p/680785
[17] Trimble, Tekla Structures 2026 IFC export - https://support.tekla.com/doc/tekla-structures/2026/int_exporting_into_ifc ; https://support.tekla.com/doc/tekla-structures/2026/rel_int_enhanced_ifc_interoperability
[18] buildingSMART Forums, IFC4 Design Transfer View experiences - https://forums.buildingsmart.org/t/ifc4-design-transfer-view-experiences/4362
[19] buildingSMART Forums, Official MVDs for IFC 4.3 - https://forums.buildingsmart.org/t/official-model-view-definitions-for-ifc-4-3/5737
[20] buildingSMART MVD, IFC4 Reference View 1.2 - https://standards.buildingsmart.org/MVD/RELEASE/IFC4/ADD2_TC1/RV1_2/HTML/schema/views/reference-view/index.htm ; MVD database https://technical.buildingsmart.org/standards/ifc/mvd/mvd-database/
[21] Bricsys, BricsCAD is officially IFC4-certified - https://www.bricsys.com/news/bricscad-is-officially-ifc4-certified
[22] buildingSMART, Software Certification Program - https://www.buildingsmart.org/compliance/software-certification/ ; implementations list https://technical.buildingsmart.org/resources/software-implementations/
[23] IfcOpenShell - https://pypi.org/project/ifcopenshell ; commit mapping IFC4X3 to IFC4X3_ADD2 https://www.github.com/IfcOpenShell/IfcOpenShell/commit/34a4e3f37a1429b048ee10039209dd6e019b1297
[24] Bentley, Export to IFC (OpenRoads Designer) - https://docs.bentley.com/LiveContent/web/OpenRoads%20Designer-v2024.0.2/Help/en/topics/1296840/GUID-DB8BCC88-1756-4110-B5AC-C0E3758DD413.html
[25] Bentley Communities, IFC4.3 version in AECOsim Update 4 - https://communities.bentley.com/products/building/building_analysis___design/f/aecosim-speedikon-forum/228189/ifc4-3-version-available-in-aecosim-update-4 (community)
[26] Autodesk, Inventor 2026 What's New - https://help.autodesk.com/cloudhelp/2026/ENU/Inventor-WhatsNew/files/IN2026-Overview.htm
[27] ARKANCE/CADforum, extended IFC import/export for Revit 2026 - https://www.cadforum.cz/cz/rozsireny-ifc-import-export-pro-revit-2026-tip14516 (third party, Czech)
[28] IFC Navigator blog, IFC2x3 vs IFC4 vs IFC4x3 - https://ifc-navigator.pages.dev/blog/ifc2x3-vs-ifc4-vs-ifc4x3-differences/ (blog)
[29] AEC Magazine, IFC for infrastructure - https://aecmag.com/collaboration/ifc-for-infrastructure/ ; IFC release notes https://technical.buildingsmart.org/standards/ifc/ifc-schema-specifications/ifc-release-notes/
[30] buildingSMART Forums, IFC 4x3 vs 4.1 changes - https://forums.buildingsmart.org/t/ifc-4x3-vs-4-1-changes/3217
[31] Infralens handbook, BIM file formats - https://infralens.in/handbook/bim-file-formats (informal handbook, secondary)
[32] dotbim - https://github.com/paireks/dotbim ; https://github.com/paireks/dotbim/issues/8 (project/community)
[33] ITcon 2026, glTF/USD vs IFC - https://itcon.org/paper/2026/16
[34] buildingSMART, Global IFC Mandates 2024 - https://www.buildingsmart.org/wp-content/uploads/2024/10/IFC-Mandate-Final-1.pdf (not fetched, search snippet only)
[35] Nordic Council, BIM maturity in the Nordics and Estonia - https://pub.norden.org/us2023-463/bim-maturity-in-the-nordics-and-estonia.html
[36] ГОСТ Р 10.0.02-2019 (catalogue) - https://cn.gostinfo.ru/catalog/Details/?id=6453898 ; EVS catalogue https://www.evs.ee/en/evs-en-iso-16739-1-2020
[37] Autodesk Forums, IFC4 missing elements - https://forums.autodesk.com/t5/revit-architecture-forum/expoted-ifc-is-missing-elements-while-using-ifc4-schema/m-p/11456115 (community)
[38] AUGI, IFC for the win - https://augi.com/articles/detail/ifc-for-the-win (community)
[39] CAD Tutor, IFC open vs linking - https://www.cadtutor.net/forum/topic/65270-ifc-open-vs-linking (community)
[40] buildingSMART chapter directory / news - https://www.buildingsmart.org/chapter-directory/ ; https://www.buildingsmart.org/greece-has-been-formally-approved-as-a-chapter-in-formation/
[41] SOFiSTiK IFC export docs - https://docs.sofistik.com/2025/en/fea/basic/interfaces/ifc_export.html
[42] Autodesk support, IFC2X3 supported on Revit - https://www.autodesk.com/support/technical/article/caas/sfdcarticles/sfdcarticles/Is-IFC2X3-format-supported-on-Revit.html
[43] Tek1, Tekla Export IFC vs IFC4 - https://www.tek1.com.au/steel-detailing/difference-between-tekla-export-ifc-and-ifc4 (blog)
[44] Autodesk Civil 3D Help (IFC4.3 RC4 note) - https://help.autodesk.com/view/CIV3D/2024/ENU/?guid=GUID-CD22FE6E-0AF9-45EF-B2FB-2B6F3C7DF25F
[45] Architosh, Archicad users among first to benefit from IFC4 Reference View export certification (2019) - https://architosh.com/2019/06/aia-archicad-users-among-first-to-benefit-from-ifc4-reference-view-export-certification (trade press, seen via search summary)
[46] Graphisoft Community, Product Roadmap: IFC 4 Import Certification - https://community.graphisoft.com/t5/Product-Roadmap/IFC-4-Import-Certification/idi-p/632958 (vendor roadmap, seen via search summary)
