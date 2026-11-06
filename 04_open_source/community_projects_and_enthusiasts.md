# Community projects, enthusiasts, add-ins and national templates around IFC

## In plain words

IFC (Industry Foundation Classes, ISO 16739) is an open file format for building models. Around it grows an ecosystem that is not a single vendor product: volunteer communities (OSArch, the IfcOpenShell/Bonsai developers), national buildingSMART chapters, government programs that publish their own export rules (Singapore, Netherlands, Denmark), and many small add-ins that fix or extend what Revit, Archicad, SketchUp or Rhino export. For a QA tester of MCP servers this matters because (a) test requests will mention these names ("export with the OSArch mapping", "check against IFC+SG", "open it in Bonsai"), (b) several community projects are themselves MCP-like tools (`ifcmcp` inside IfcOpenShell, an "IDS MCP Server" in awesome lists) and (c) national templates define what a "correct" IFC export looks like in a given country. This document maps that landscape, labels what was verified on primary pages, and flags what could not be verified.

Last researched: 2026-11-06

**Research limits (read first):** the web-search budget of this run was exhausted before any search could run, so everything below comes from direct page fetches of known primary URLs. buildingsmart.org and technical.buildingsmart.org returned HTTP 403 to the fetcher, so chapter lists and "rooms" pages could not be read. Items from general knowledge are marked "(unverified)". See "Gaps".

---

## 1. OSArch (Open Source Architecture)

OSArch describes itself as a news source and community for free software in the built environment; news is community-submitted and curated [1].

| Resource | What it is | URL |
|---|---|---|
| News site | Curated news (e.g. Bonsai 0.9.0, FreeCAD grants in 2026) | https://osarch.org/ [1] |
| Events calendar | Conferences, webinars, hackathons, meetups | https://osarch.org/events/ [2] |
| Wiki | Community knowledge base: software directories, IFC, MVD, BCF, Bonsai, Revit setup for OpenBIM | https://wiki.osarch.org/ [3] |
| Forum | Discourse-style forum; categories "General" and "Espanol / Spanish" (about 112 threads) | https://community.osarch.org/ [4] |
| Live chat | Matrix room `#OSArch:matrix.org` and IRC `#OSArch` on irc.libera.chat; Discord is NOT mentioned on the official chat page | https://osarch.org/chat/ [5] |
| Funding | Open Collective | https://opencollective.com/osarch [1] |

Notes useful for testers:
- Events seen on the calendar (as of research date): As Built with Speckle keynote 3 Nov 2026; BIM World Munich 24-25 Nov 2026; FOSDEM 2027 CAD devroom 31 Jan 2027; in 2026 an "openBIM Hackathon Porto" (22 Mar), "Sydney open source AEC meetup #5" (13 Mar), buildingSMART Australasia Xchange (24 Jun), Blender Conference (23 Sep) [2]. Meetups are therefore regional and irregular, not a fixed schedule.
- Wiki pages worth knowing: "Revit setup for OpenBIM", "Software Libraries for IFC", "Bonsai IFC Patch Recipes", "The OpenBIM Pledge", "AEC Open Data Standards Directory" [3].
- Forum threads seen: the "Bonsai new release!" thread (about 59K views), "Roadmap for Revit migrator to Bonsai BIM - absolute beginner", "German drawing conventions (DIN 1356-1) for Bonsai's 2D output", "Hello Wall - IfcWallElementedCase", "Text to IFC in the browser, built on IfcOpenShell" [4].

### OSArch Revit setup (a real, practical template)
The OSArch wiki page "Revit setup for OpenBIM" is the best community-made recipe for improving Revit's IFC export [6]:
- Install the latest open-source `revit-ifc` add-in (the bundled one "is outdated and buggy").
- Use the OSArch class-mapping file `exportlayers-ifc-osarch.txt` (grids to `IfcGrid`, structural connections as fasteners, topography to `IfcSite`, structural members to `IfcMember`). Wrong mappings (objects to `IfcSite`/`IfcGrid`) create invalid IFC.
- Load both IFC shared-parameter files (instances and types) into the `IFC Parameters` group.
- Use a property-set template file (`Revit-psets.txt`, default empty) for custom Psets.
- Enable *File > Export > IFC > Modify Setup > Advanced > "Store the IFC GUID in an element parameter after export"*.
- Parameter expressions such as `{$this("Description")}` let an `IfcDescription` type parameter remap a native field.
- The page says it was not audited for Revit versions above 2018 [6] - so treat menu details for 2023+ as potentially outdated.
- It references buildingSMART Denmark's "IFC Export Guide for Revit and ArchiCAD" [6] (the original Molio URL now redirects to a generic page [17]; content location unverified).

---

## 2. IfcOpenShell and Bonsai community

**IfcOpenShell** = open-source IFC library and geometry engine (C++ and Python), supporting IFC2x3, IFC4, IFC4x1, IFC4x2, IFC4x3 [7]. The monorepo also contains: Bonsai (Blender add-on, GPL-3.0), IfcConvert (CLI converter), and tools `bcf`, `bsdd`, `ifc4d`, `ifc5d`, `ifccityjson`, `ifcclash`, `ifccsv`, `ifcdiff`, `ifcedit`, `ifcfm`, `ifcmcp`, `ifcpatch`, `ifcquery`, `ifcsverchok`, `ifctester` (IDS checker). Core libraries are LGPL-3.0-or-later [7].
- **Version:** "IfcOpenShell v0.9.0" was announced 1 Oct 2026 on GitHub Discussions [8]; OSArch news mentions Bonsai 0.9.0 [1].
- **Bonsai** (formerly BlenderBIM; the rename is background knowledge, not stated on the Bonsai front page) is now presented as a family: Bonsai Studio (authoring in Blender), Bonsai Viewer (desktop review app), Bonsai Web ("coming soon") [9].
- **Where the community talks:** GitHub Discussions (categories: Announcements, BlenderBIM User Interface, General, Ideas, Polls, Q&A, Show and tell) [10]; OSArch forum and chat; Bonsai's own community page lists the OSArch forum, live chat, GitHub, X/Twitter and Open Collective - and no Discord [11].
- **Localization:** a Discussions thread proposes localizing the Bonsai documentation starting with Brazilian Portuguese (pt-BR) [10]. The OSArch forum has a Spanish category [4].
- Other threads seen: "Native SketchUp (.skp) import for Bonsai", "A TypeScript/Node.js port of ifcopenshell-python", clash-detection performance benchmark for IfcClash 0.8.4 [10]. Note that some of these are AI-assisted contributions (unverified) - treat claims in them as unreviewed.

**Web/JS side:** That Open Company (`engine_web-ifc`, `engine_components`, `engine_fragment`, `web-ifc-three`) - JS/TS libraries to read/write IFC in the browser [12]. The company launched "That Open Platform" (public launch announced for 23 Nov per its site; AI agents performing modeling/clash checks are advertised) [13]. Other open IFC libraries seen in GitHub topic lists: xBIM (.NET), BIMserver, BIMsurfer, xeokit BIM viewer [14].

---

## 3. buildingSMART: international, chapters, rooms, community GitHub

- **Official technical GitHub** (github.com/buildingSMART): IDS, IFC4.x-development, IFC5-development, bSDD, BCF-XML, BCF-API, `validate` (validation service), `ifc-gherkin-rules`, `Certification-datasets`, `documents-API` (openCDE) [15].
- **bSI InfraRoom** GitHub: IFC-Specification baseline, IFC4.3.x-development, tunnel/bridge test instructions, MVD-Infra test instructions for IFC4.3 alignment-based reference view certification [16]. This shows how "rooms" (domain working groups such as Infrastructure) work in practice: public repos with documentation and test instructions. (The official rooms page could not be fetched - 403.)
- **buildingsmart-community** GitHub organization: community-led, explicitly "not officially owned by bSI" but supported by it; new repos are requested by contacting buildingSMART's technical team (see the org page). Repos: ifcJSON, ifcOWL, IFC2RDF, Community-Sample-Test-Files, bSDD-Revit-plugin, bSDD-Tekla-plugin, bSDD-filter-UI, dictionary-manager, Excel2IDS (GPL-3.0), ifc5-git [18].
- **bSDD Revit plugin** (community build, MIT): validates types against bSDD dictionaries, applies bSDD classes to elements, generates persistent shared-parameter GUIDs, exports IFC via the built-in Revit exporter and post-processes `IfcClassificationReference` locations; installer supports Revit 2023 and 2024 per the page (check for newer builds) [19].
- **Chapters** (examples verified):

| Chapter | What the site shows | Source |
|---|---|---|
| buildingSMART Japan (bSJ) | Working groups (architecture, civil, technical standards incl. ISO 19650, international), IFC certification and certified-software list, Professional Certification program, End User Guide, news: bSI International Summit 2026 in Tokyo | [20] |
| buildingSMART Spain | Working tables (contractors, design, public administrations), "Programa Impulso", openBIM Tour, resource "Manual de Entrega de IFC Edificacion" (IFC delivery manual for buildings); events BIMEXPO Madrid (10-13 Nov), Basque Tech Summit (19-21 Nov) | [21] |
| buildingSMART Brasil (bSBR) | Formed with support of BIM Forum Brasil; Portuguese-language openBIM information, forums, working groups, training/certification | [22] |
| buildingSMART Deutschland / Austria / Russia / China | Not verified (site empty or unreachable) | - |

---

## 4. Add-ins and plugins that change IFC export/import

| Tool | Host app | What it does | Verified? |
|---|---|---|---|
| **revit-ifc** (Autodesk, open source, LGPLv2) | Revit / Revit LT 2019+ | IFC export, link IFC, export UI; overrides the version shipped with Revit. Supports "current annual version and two previous"; issue templates (Problem Report, Enhancement, Inquiry). Recent tags: IFC_v27.4.0.30 and v27.3.0.12 (Revit 2027), IFC_v25.4.40 added IFC4.3 Reference View exchange requirements [23][24] | Yes |
| **OSArch mapping/psets files** | Revit | Class mapping, shared parameter files, Pset template (see section 1) [6] | Yes |
| **bSDD Revit plugin** | Revit | Classification via bSDD [19] | Yes |
| **pyRevit** | Revit | Rapid application development environment (Python/IronPython/CPython, C#); GPL-3.0; extensions can be installed/shared. No IFC-specific tool on the repo front page [25] | Yes (IFC extensions: none found) |
| **Dynamo scripts** "IFC Parameter Export & Import" | Revit | Listed by Singapore's CORENET X: creates schedules, exports IFC parameters to Excel, imports updated values [26] | Yes (listing only) |
| **DiRootsOne** | Revit | Export model data to Excel/Google Sheets and import back [26] | Yes (listing only) |
| **BIMcollab BCF Manager / Zoom** | Revit, Navisworks, Archicad, Tekla / viewer | BCF issue handling; free IFC viewer [26] | Yes (listing only) |
| **Revizto** | Revit etc. | Parameter review, IFC review before submission, BCF [26] | Yes (listing only) |
| **BuiltSearch, Bimeco Validator** | web | IFC+SG validation; Revit IFC mapping and shared-parameter generation [26] | Yes (listing only) |
| **GeometryGymIFC** | Rhino/Grasshopper and others | C# classes to generate and parse IFC; supports IFC2x3, IFC4, IFC4.3 and "early" later versions; the repo page itself does not describe it as a Grasshopper plugin (that relation is common knowledge, unverified) [27] | Partly |
| **Archicad IFC Manager / translators; SketchUp "IFC Manager"** | Archicad / SketchUp | Not retrievable in this run (Graphisoft help URL 404; SketchUp warehouse page empty) | No (unverified) |
| **Gingerbim** | SketchUp, Rhino | Paid beta CAD-to-BIM platform for IFC+SG modelling/export [26] | Listing only |
| **rvt-rs** (GitHub topic list) | none (standalone) | Rust reader for Revit files that claims to export IFC4/glTF/SVG without Revit [14]. Independent project, maturity unknown - treat as experimental (unverified) | Listing only |

**Important for testers:** an MCP "export IFC from Revit" tool will usually call the Revit API's built-in exporter, i.e. whichever revit-ifc version is installed. Results change with the add-in version, the chosen setup (IFC2x3 Coordination View 2.0, IFC4 Reference View, IFC4 Design Transfer View - background knowledge, unverified here) and the mapping files. Always record the add-in version in a test report.

---

## 5. National templates, mapping files and requirements

### Singapore: IFC+SG (CORENET X)
- Definition: "IFC+SG defines how BIM models are structured for CORENET X submission"; base standard labelled IFC4 [28]. It combines IFC with Singapore-specific property sets (SGPsets) [29].
- **IFC+SG Excel Mapping File**: for each building element lists the IFC entity, mandatory SGPsets, standard Psets, properties and controlled values. Download on the page: `industry-mapping-09-2026.xlsx`, "Version: 22 September 2026", start with the "CX Pilot Mapping" tab. Used with the CORENET X Code of Practice and the Glossary of Identified Components [29]. (The page also shows "Last Updated 16 May 2024", which is inconsistent.)
- Official ecosystem page lists 11 tools: BIMvision, BIMcollab Zoom and BCF Manager, 1IFC (IFC merge), DiRootsOne, Bimeco Validator, BuiltSearch, Revizto, Dynamo scripts, GingerBIM, Revit "Interoperability Tools (Model Checker)" [26].

### Netherlands: BIM basis ILS
- Published on digiGO (the old bimloket.nl URL redirects there) [30]. Version 2 of the application guideline. Guidance: name storeys only as `IfcBuildingStorey`, rooms as `IfcSpace`, zones as `IfcZone`; group building services in `IfcSystem`; assign an `IfcMaterial` to every object; use buildingSMART Psets where possible [31].
- The Downloads page contains the infographic (v2.0, 11 languages) and v1.0 documents in 18 languages including Russian, Chinese, Japanese, Portuguese, Spanish; it does NOT contain Revit/Archicad export settings or checking rules [32]. Do not assume "BIM basis ILS" ships a Revit template.

### Denmark
- buildingSMART Denmark (part of Molio) published an "IFC Export Guide for Revit and ArchiCAD" cited by OSArch [6]; its original URL redirects to a generic Molio page [17], so current location is unverified.

### Germany / Austria
- BIM Deutschland (federal portal) offers a BIM-Portal, standards pages (AIA - Auftraggeber-Informationsanforderungen, BAP - BIM-Abwicklungsplan, CDE, LOIN, MVD) and a downloads area; this run could not confirm any IFC export template there [33]. buildingSMART Deutschland site returned empty content. Austrian materials (e.g. Austrian Standards ON-A 6241) are background knowledge only (unverified).

### Russia (ЦИМ - цифровая информационная модель)
- Primary-source research failed (connection refused for the standards database, buildingsmart.ru does not resolve). What was verified: Renga (Russian BIM software by ASKON/Renga Software) uses IFC4 for data exchange and runs communities in VK, Yandex Zen, RuTube, Telegram and Max, plus an open API/SDK [34]; Russian Wikipedia says Renga supports IFC2x3 and IFC4, nanoCAD IFC2x3, IFC4 and IFC4x2, and mentions a Renga-sourced reference about state expertise (госэкспертиза) in IFC [35]. ROSTIM 2026 industry event: 10 November, Moscow [34].
- Russian ЦИМ export templates for Revit (шаблоны экспорта, файлы соответствия классов) exist as vendor/consultant materials but could not be located or verified here (unverified). Do not cite specific ГОСТ/СП numbers from this document.

### Denmark/Japan/Brazil/Spain/China in short
- Japan: bSJ runs IFC certification and lists certified software [20]; Japanese Wikipedia lists domestic IFC-capable software (Rebro, OpenAEC, SiTE-NEXUS, Orizuru 3D IFC Viewer, TREND-CORE, GLOOBE, ARCHITREND ZERO, V-nasClair, BimClip) and MLIT BIM/CIM and PLATEAU guidance [36].
- Spain: IFC delivery manual for buildings and working tables at bSES [21]; Spanish category on the OSArch forum [4].
- Brazil: bSBR (with BIM Forum Brasil) [22]; pt-BR documentation localization for Bonsai under discussion [10].
- China: nothing could be verified (Wikipedia page 404, test site unresolved). Chinese standards based on IFC (e.g. a national BIM storage standard) are background knowledge only (unverified).

---

## 6. Awesome-lists and curated indexes

- **`awesome-bim` / `awesome-openbim`:** the GitHub topic `awesome-bim` is unused and a repository search for "awesome-openbim" returned 0 results at research time [37][38]. So these exact names do not exist as popular lists - a tester should not expect them.
- **Awesome-AECO** (CC0-1.0): curated open-source AECO list with BIM/CAD/Revit plugins, parametric design, digital twins, etc. IFC-related entries include IfcOpenShell, xBIM, BIMserver, web-ifc, That Open components, Speckle, BHoM, BIMsurfer, xeokit, GeometryGymIFC, IDS, bSDD, Bonsai, bim2sim, Autodesk revit-ifc and an "IDS MCP Server". It also contains non-open-source/commercial entries and lacks a visible update date [39].
- GitHub topic `openbim` (131 repos): BIMserver, web-ifc-three, XbimEssentials, xeokit-bim-viewer, buildingSMART IDS/IFC5/bSDD, Excel2IDS, IFC-Language-Server (LSP for IFC STEP files), `ifc-sheet`, `dotbep` (machine-readable BIM execution plan), `Gridline` (AI agent skills for AEC) [14].
- OSArch wiki directories: AEC Free Software directory, Software Libraries for IFC, Software Comparison, AEC Open Data Standards Directory [3].

---

## 7. Chat and social communities

| Channel | Evidence | Note |
|---|---|---|
| OSArch Matrix `#OSArch:matrix.org`, IRC `#OSArch` | [5] | official |
| OSArch forum (English + Spanish) | [4] | official |
| IfcOpenShell GitHub Discussions | [10] | best place for tool bugs |
| Bonsai X/Twitter, Open Collective | [11] | |
| Renga communities (VK, Telegram, Max, RuTube, Zen) | [34] | Russian-language, vendor-run |
| Discord / Slack / other Telegram groups for IFC | not found | Official OSArch and Bonsai pages do not mention Discord [5][11]. Third-party Discord/Telegram servers likely exist (unverified) - never point testers to unknown invite links. |

### Bloggers, YouTubers, educators by language
Not verifiable in this run (no search). Verified pointers only: the OSArch wiki has "Bonsai video tutorials" and "OpenStudio video tutorials" pages [3]; the OSArch forum has a "Video tutorial series for Blender + Bonsai" thread [4]; buildingSMART Japan publishes seminar materials and an End User Guide [20]. Per-language lists (English, Russian, Chinese, Spanish, Portuguese, German, Japanese) should be built later from a live search; any name given from memory would be unverified.

---

## Typical questions people ask about this

1. Where can I ask a question about IfcOpenShell or Bonsai - forum, Discord or GitHub? [4][10][11] (answer: OSArch forum/Matrix and GitHub Discussions; no official Discord found)
2. "Roadmap for Revit migrator to Bonsai BIM - absolute beginner" - how do I move from Revit to Bonsai? [4]
3. How do I make Revit export grids as `IfcGrid` and topography as `IfcSite`? [6]
4. Where do the IFC shared parameters files for Revit come from, and into which group do they go (`IFC Parameters`)? [6]
5. Why does my Revit IFC lose its GlobalId on re-export - what does "Store the IFC GUID in an element parameter" do? [6]
6. Which revit-ifc version should I use for Revit 2027, and does it support IFC4.3? [23][24]
7. What is IFC+SG and where is the Excel mapping file? [28][29]
8. Which tools can pre-validate an IFC for CORENET X? [26]
9. Does BIM basis ILS include a Revit export template? (No; downloads are infographics/documents) [32]
10. How do I classify Revit elements with bSDD classes? [19]
11. Is there an "awesome-openbim" list? [37][38][39]
12. Is there an MCP server for IFC/IDS? (IfcOpenShell contains `ifcmcp`; awesome list mentions an "IDS MCP Server") [7][39]
13. Can pyRevit export IFC better than the built-in tool? (illustrative; no IFC extension was found [25])
14. How can I generate an IDS from Excel? [18]
15. Which Japanese software has IFC certification? [20][36]
16. Is Bonsai documentation available in Portuguese? [10]
17. Where is the IFC delivery manual in Spanish (Manual de Entrega de IFC Edificacion)? [21]
18. How do I convert a Revit UniqueId to an IFC GlobalId without exporting? [6]
19. Which community meetups and conferences are coming up? [2]
20. Which IFC viewer can I use for free to inspect an export before delivery? (illustrative; BIMcollab Zoom and BIMvision are listed by CORENET X [26])

---

## Common pitfalls and misconceptions

- **"The community Discord is the official support channel."** The official OSArch and Bonsai pages list Matrix/IRC, forum, GitHub; no Discord [5][11].
- **"Awesome-BIM exists."** The topic is unused and searches returned nothing; the nearest is Awesome-AECO [37][38][39].
- **"BIM basis ILS gives ready export templates."** Its downloads are documents/infographics only [32].
- **"The version of IFC export bundled with Revit is fine."** OSArch calls it outdated/buggy; open-source revit-ifc overrides it [6][23]. Release notes show fixes for geometry and property-set issues, so always note version numbers [24].
- **"IFC+SG is just IFC4."** It is IFC4 plus Singapore SGPsets and controlled values per the mapping file [28][29]. The mapping file is dated (22 Sep 2026) and changes - always re-download.
- **"buildingsmart-community repos are official."** The org is explicitly independent of bSI [18]; the bSDD Revit plugin is a "community build tool" [19].
- **Old guides:** the OSArch Revit page was not audited above Revit 2018 and links to App Store builds of 2019-2021 [6]; menu paths may differ.
- **Naming:** BlenderBIM became Bonsai (background knowledge); old tutorials use the old name.
- **AI-assisted contributions** appear in community lists (e.g. ports, benchmarks); verify claims before using as test oracles.

---

## Gaps

- Web search was unavailable (budget exhausted), so no search in Russian/Chinese/Spanish/Portuguese/German/Japanese was performed; bloggers/YouTubers by language, Telegram/Discord/Slack groups, Chinese/Brazilian national projects and Russian ЦИМ template repositories remain unresearched.
- buildingsmart.org and technical.buildingsmart.org: HTTP 403 (chapters list, rooms, Technical Roadmap unread).
- Not retrievable: Graphisoft Archicad IFC help page (404), SketchUp IFC Manager listing (empty), Dynamo package manager (redirect only), Autodesk Revit help IFC pages (404/403), docs.cntd.ru (connection refused), buildingsmart.ru (DNS failure), chinabim.org (DNS failure), buildingSMART Deutschland (empty).
- No suspicious, pirated or phishing sites were encountered or linked.

---

## Sources

[1] https://osarch.org/
[2] https://osarch.org/events/
[3] https://wiki.osarch.org/
[4] https://community.osarch.org/
[5] https://osarch.org/chat/
[6] https://wiki.osarch.org/revit-setup-for-openbim/
[7] https://github.com/IfcOpenShell/IfcOpenShell
[8] https://github.com/IfcOpenShell/IfcOpenShell/discussions/categories/announcements
[9] https://bonsaibim.org/
[10] https://github.com/IfcOpenShell/IfcOpenShell/discussions
[11] https://bonsaibim.org/community.html
[12] https://github.com/ThatOpen
[13] https://thatopen.com/
[14] https://github.com/topics/openbim
[15] https://github.com/buildingSMART
[16] https://github.com/bSI-InfraRoom
[17] https://molio.dk/support/vaerktojer/beskrivelsesvaerktojet-2-0/anvisninger/
[18] https://github.com/buildingsmart-community
[19] https://github.com/buildingsmart-community/bSDD-Revit-plugin
[20] https://www.building-smart.or.jp/
[21] https://www.buildingsmart.es/
[22] https://www.buildingsmart.org.br/
[23] https://github.com/Autodesk/revit-ifc
[24] https://github.com/Autodesk/revit-ifc/releases
[25] https://github.com/pyrevitlabs/pyRevit
[26] https://info.corenet.gov.sg/ifc-sg/modelling---authoring/3rdpartytools
[27] https://github.com/GeometryGym/GeometryGymIFC
[28] https://info.corenet.gov.sg/ifc-sg/start-here/WhatIsIFCSG
[29] https://info.corenet.gov.sg/ifc-sg/requirements---submission/ifc-sg-excel-mapping-file
[30] https://www.digigo.nu/
[31] https://www.digigo.nu/ils-en-richtlijnen/bim-basis-ils
[32] https://www.digigo.nu/ilsen-en-richtlijnen/bim-basis-ils/downloads/
[33] https://www.bimdeutschland.de/
[34] https://rengabim.com/ru/
[35] https://ru.wikipedia.org/wiki/Industry_Foundation_Classes
[36] https://ja.wikipedia.org/wiki/Industry_Foundation_Classes
[37] https://github.com/topics/awesome-bim
[38] https://github.com/search?q=awesome-openbim&type=repositories
[39] https://github.com/osama-ata/Awesome-AECO
