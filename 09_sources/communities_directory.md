# Communities directory: where people discuss IFC and Revit

## In plain words

When someone has trouble getting a building model out of Revit as an IFC file (IFC = Industry Foundation Classes, the open exchange format for building models), or wants to check one, they ask somewhere. This directory lists those "somewheres" around the world, by language and region. For each place you get: what it is, how active it looked in our research, whether an automated reader (a crawler or an AI agent with a fetch tool) can actually read it, what people talk about there, and anything odd worth knowing.

Why a tester needs it: a believable test request copies the voice of a real community. A Russian BIM coordinator posts on forum.dwg.ru or Habr, a Japanese developer on Qiita or Zenn, a Chinese student on Zhihu or CSDN, a worldwide IFC expert on the buildingSMART forum. Each place has its own habits (see [../06_how_people_write/style_guide.md](../06_how_people_write/style_guide.md) and [../05_real_world_questions/by_language/](../05_real_world_questions/by_language/)).

The companion file [sources_index.md](sources_index.md) lists the individual addresses (standards, laws, vendor pages, threads).

## How to read the columns

| Column | Meaning |
|---|---|
| **Type** | forum, issue tracker (GitHub), blog platform, Q&A site, chat/channel, vendor community, official body, wiki |
| **Activity** | Our evidence-based estimate, **not** traffic data. `High` = 40 or more real records in this KB spread over several years and recent items (2025-2026); `Medium` = 10 to 39 records, or recent but narrow; `Low` = fewer than 10 or old; `Official` = a standards body or government page with no user discussion; `Unknown` = we could not read it. The number in brackets is how many `real` records in `research_raw/wave1/` come from the site, plus the span of years where known. Counts depend on what could be fetched, so blocked sites look smaller than they are |
| **Automated reading** | `fetchable` = pages could be read by a plain fetch; `partly` = some page types worked, others did not; `blocked` = HTTP 403 / captcha / login / refused; `snippet only` = only search-result text was seen. Observed on 2026-11-06; access can change |
| **Dominant topics** | What the KB's records from the site are mostly about, in plain words |

Related documents: [sources_index.md](sources_index.md), [../04_open_source/community_projects_and_enthusiasts.md](../04_open_source/community_projects_and_enthusiasts.md), [../02_standards_regulations/national/](../02_standards_regulations/national/), [../07_mcp_testing/prompt_bank_multilingual.md](../07_mcp_testing/prompt_bank_multilingual.md).

## Overview: how much real material per language

Real (observed, not synthetic) records in the KB at the time of writing: English 1827, Chinese 170, Russian 109, Japanese 59, Spanish 34, Italian 29, German 23, Dutch 21, Norwegian 13, Korean 9, French 4, and single records in Slovak, Vietnamese, Portuguese, Turkish, Czech, Danish. The kinds of sources differ a lot by language, which shapes how "human" the material is:

| Language | Main source types in the KB | Voice you can imitate |
|---|---|---|
| English | GitHub issues, buildingSMART and OSArch forums, Dynamo/pyRevit forums | Real asker voice, many versions and error texts |
| Chinese | Blogs (89), Q&A (27), GitHub issues (14), official documents | Question-style blog titles, tutorial voice; thread comments mostly missing |
| Russian | Forum (45), blogs (37), Telegram (10), GitHub (8) | Real forum voice (dwg.ru) and professional developer essays (Habr) |
| Japanese | Blogs (53) | First-person developer notes; no Q&A voice |
| Spanish | Blogs, forum, official documents | Mostly articles; few genuine asker posts |
| Italian, German, Dutch, Norwegian, Korean, French | Trade articles, official documents, a few issues | Official or trade voice, not asker voice (these are the thinnest languages) |

---

## 1. International and English-language communities

### 1.1 Standards-body and expert forums

| Name | URL | Type | Activity | Automated reading | Dominant topics | Notes |
|---|---|---|---|---|---|---|
| buildingSMART Technical Forums | https://forums.buildingsmart.org/ | Forum (Discourse) | High (235 records, 2018-2026) | Mostly fetchable: topic pages (`/t/<id>`) and category pages worked; `search.json` works but returns HTTP 429 after a few calls; a few runs saw 403/404 on tag pages or search | IFC version differences and MVD (views), infrastructure IFC 4.3 (alignment, bridge, rail), property sets, georeferencing (`IfcMapConversion`), IDS rules, proxy elements, Revit export problems | Experts and vendor engineers answer; moderators redirect vendor-specific bugs to the vendor. Includes a few Spanish posts and a "bottlenecks" survey post (no replies). Good for precise, standard-aware questions |
| OSArch community | https://community.osarch.org/ | Forum | High (183 records, 2020-2026) | Fetchable (thread and tag pages such as `/discussions/tagged/ids`); search pages returned no listings during a site migration; some guessed wiki URLs 404 | IDS and IfcTester, IfcOpenShell scripting, Bonsai (Blender) problems, geometry quality, clash detection, quantity take-off and cost, learning/education | Open-source enthusiasts, architects leaving Revit, teachers. Has a Spanish category. German drawing-convention threads (DIN 1356-1). AI-with-Bonsai threads (Claude, "AI chat" on ifcopenshell.org) |
| OSArch wiki | https://wiki.osarch.org/ | Wiki | Low-Medium (8 address mentions) | Partly (some pages read, some 404) | Revit setup for openBIM, IFC geolocation, spatial hierarchy, materials, sequence concepts | Handy neutral explanations written by practitioners |
| OSArch chat | https://osarch.org/chat/ | Chat (Matrix `#OSArch:matrix.org`, IRC `#OSArch` on libera.chat) | Unknown | Not fetchable (live chat) | Open-source AEC in general | Official page says Discord is not used |
| OSArch news and events | https://osarch.org/ , https://osarch.org/events/ | News/calendar | Medium | Fetchable | Releases (Bonsai), hackathons, meetups | Event list is useful for regional communities (Porto, Sydney, Munich) |
| That Open Company community | https://people.thatopen.com | Vendor community | Unknown | Blocked (login via Auth0) | Web IFC viewers, components | Public help goes through GitHub instead |

### 1.2 GitHub issue trackers (the most honest "bug report" voice)

GitHub issues are fetchable (with the `gh` command line or plain pages), but the API rate-limits quickly (HTTP 403/429 during the research), so batch reads should be paced.

| Name | URL | Type | Activity | Automated reading | Dominant topics | Notes |
|---|---|---|---|---|---|---|
| Autodesk revit-ifc | https://github.com/Autodesk/revit-ifc/issues | Issue tracker | High (433 records, 2018-2026) | Fetchable | Revit IFC export (missing elements, wrong classes, property sets, GUIDs, shared coordinates) and import/link (class mapping, rotation, performance) | Autodesk staff quote internal ticket numbers `REVIT-nnnnnn`. Users are often Autodesk Community regulars; maintainers refer vendor-support issues here. Largest single source of real Revit-IFC pain |
| IfcOpenShell | https://github.com/IfcOpenShell/IfcOpenShell/issues , `/discussions` | Issue tracker and discussions | High (397 records, 2016-2026) | Fetchable | Python/C++ scripting, geometry failures, IFC 4.3 infrastructure, converters, validation, performance; real LLM/MCP complaints (issue 7945 LLM-fabricated IFC rejected by viewers; 8951 empty tool descriptions) | Maintainers answer quickly and bluntly; many reports include code and error text |
| That Open web-ifc / components / fragments | https://github.com/ThatOpen | Issue tracker | High (101 + 25 + 14 records, 2021-2026) | Fetchable | Browser IFC loading, huge files (2 GB models), memory, alignment display, properties | Developer voice (JavaScript, WebAssembly) |
| xBIM Toolkit | https://github.com/xBimTeam | Issue tracker | Medium (38 + 13 + 7 records, 2017-2026) | Fetchable | .NET reading, geometry, WexBIM, encoding, performance | Windows/.NET developers |
| buildingSMART repositories | https://github.com/buildingSMART | Issue tracker | Medium (IDS 17, IFC4.x-development 10, validate 6, BCF-XML 6, IDS-Audit-tool 4) | Fetchable | IDS edge cases, schema questions, validation service errors, BCF details | Precise, standard-lawyer tone |
| BIMserver, IFC++, Speckle, GeometryGym, FreeCAD | https://github.com/opensourceBIM/BIMserver , https://github.com/ifcquery/ifcplusplus , https://github.com/specklesystems/speckle-server , https://github.com/GeometryGym/GeometryGymIFC , https://github.com/FreeCAD/FreeCAD | Issue trackers | Low-Medium (3 to 12 records each) | Fetchable | Viewer behaviour, geometry, GUID tracking, quantities | BIMserver and COBie plugins are partly old (2014-2025) |
| Revit MCP servers | https://github.com/mcp-servers-for-revit/mcp-servers-for-revit , https://github.com/bimwright/rvt-mcp , https://github.com/shuotao/REVIT_MCP_study , https://github.com/LuDattilo/revit-mcp-server | Issue trackers of AI tools | Low-Medium per repository (2 to 7 records each) but many repositories; 2025-2026 only | Fetchable | Chat prompts that fail ("create a 10 m wall", "list all pipes", stairs, doors, mutating tools, context compaction, view screenshots for vision models) | The only place with real prompts to AI assistants; also issues in Traditional Chinese, Japanese, Spanish, Slovak and Vietnamese. These are the closest real analogue of what the test servers receive |
| IFC / Archicad / Tekla MCP servers | https://github.com/JotaDeRodriguez/Bonsai_mcp , https://github.com/flinker-app/ifc-mcp , https://github.com/SzamosiMate/tapir-archicad-MCP , https://github.com/teknovizier/tekla_mcp_server | READMEs and trackers | Low (1 to 2 records each) | Fetchable | Prompt lists ("You ask / It does"), duplicate elements on retry, setup | READMEs contain example prompts; useful for style |
| OpenAEC BIM validator (Netherlands) | https://github.com/OpenAEC-Foundation/OpenAEC-BIM-validator | Issue tracker | Low-Medium (9 records, 2026) | Fetchable | IDS-based validation, classification, clash | Issues in English and Dutch |

### 1.3 Vendor and software communities

| Name | URL | Type | Activity | Automated reading | Dominant topics | Notes |
|---|---|---|---|---|---|---|
| Autodesk Community (Revit, Revit API, Revit Ideas, Civil 3D) | https://forums.autodesk.com/ | Vendor forum | High (80 records, 2017-2026; almost all snippet-level) | Blocked: HTTP 403 for nearly every page; records are search-snippet level | IFC export settings, mapping, shared coordinates, levels, Revit 2026/2027 export UI complaints, import/link | Boards are language-specific (a Spanish board exists). The "Revit Ideas" board holds feature wishes ("GUI for parameter mapping in IFC export") |
| Dynamo forum | https://forum.dynamobim.com/ | Forum (Discourse) | High (69 records, 2016-2026) | Fetchable (`search.json` and tag pages) | Revit automation: batch IFC export by script, parameter clean-up, schedules, areas, AI/MCP opinions ("would you use an MCP assistant for Dynamo?") | Autodesk-staffed moderators steer to packages (Clockwork, Orchid, Genius Loci, IFCNodes). Practical, short, screenshot-driven questions |
| pyRevit forum | https://discourse.pyrevitlabs.io/ | Forum (Discourse) | Medium (18 records, 2021-2026) | Fetchable | IFC export by script, command-line export, built-in MCP in pyRevit 7, "check what the AI actually built" | Developer-leaning Revit power users |
| Graphisoft Community | https://community.graphisoft.com/ | Vendor forum | Low-Medium (10 records, 2019-2025; snippet-level) | Blocked (HTTP 403); snippet only | Archicad-to-Revit IFC exchange, plugin crashes, "Revit IFC to Archicad is fundamentally flawed" | Archicad users with openBIM views; German-language boards exist |
| Tekla User Assistance and forum | https://support.tekla.com/ , https://forum.tekla.com/ | Vendor docs and forum | Docs: 5 records (2024); forum unknown | Docs fetchable; forum listings blocked (403) | Tekla IFC export, property sets, checking exports | Real Tekla user voice is missing from the KB |
| Allplan, Vectorworks, Bentley communities | https://connect.allplan.com , https://forum.vectorworks.net , Bentley community (ServiceNow) | Vendor forums | Unknown | Blocked (403) / JavaScript-only | - | Not researched; candidates for later runs |
| Cesium community | https://community.cesium.com/ | Forum | Medium (13 records, 2021-2026) | Fetchable | IFC/BIM to 3D Tiles, georeferencing, property display | GIS and web-3D people |
| BIMcollab help center | https://helpcenter.bimcollab.com | Vendor knowledge base | Medium (9 records) | Fetchable | BCF issue sync with Solibri, missing viewpoint components, colouring | Answers in "why does X not show" form |
| Pix4D community, AUGI, CADTutor | https://community.pix4d.com/t/export-ifc-from-revit-geolocation/29413 , https://augi.com/articles/detail/ifc-for-the-win , https://www.cadtutor.net/forum/topic/65270-ifc-open-vs-linking | Forums and articles | Low (single threads) | Snippet / fetchable | IFC geolocation, open vs link | Occasional hits |

### 1.4 Blogs and educators in English

| Name | URL | Type | Activity | Automated reading | Dominant topics | Notes |
|---|---|---|---|---|---|---|
| BIM Corner | https://bimcorner.com/ | Blog (Poland, English) | Medium (19 records, 2020-2026) | Fetchable | Common IFC export mistakes, class mapping, validation, IFC 4.3, AI with IFC | "What I don't like about IFC" style opinion posts; good for complaint tone |
| Other English blogs | https://thinkmoult.com/ , https://archgyan.com/ , https://teocomi.com/ , https://bimfix.blogspot.com/ , https://novedge.com/ | Blogs | Low | Fetchable | Georeferencing, coordination, naming, BCF | Single-author voices |
| LinkedIn, Medium | https://www.linkedin.com/ , https://medium.com/ | Social/blog | Unknown | Blocked / unrelated results | - | Highly relevant for BIM managers' opinions but not reachable |
| Reddit (for example r/Revit) | https://www.reddit.com/ | Social | Unknown | Not reachable without search; no Reddit record exists in the KB | Expected: Revit help, jobs, software choice | Biggest gap for casual user voice |
| Stack Overflow, GIS Stack Exchange | https://stackoverflow.com/ , https://gis.stackexchange.com/ | Q&A | Unknown | Blocked for the fetch tool | Expected: IfcOpenShell/Revit API code questions | Developer questions live here but were unreachable |
| YouTube | https://www.youtube.com/ | Video | Unknown | Not searched (one Russian lecture noted) | Tutorials | Comments not read |

---

## 2. Russian-speaking community

See also [../05_real_world_questions/by_language/ru.md](../05_real_world_questions/by_language/ru.md). Russian practice is driven by regulation: the state expertise bodies of Moscow and Saint Petersburg require an information model (ТИМ) in IFC for the urban-planning/architecture approval (АГР), checked with IDS packs, and national standard SP 333.1325800.2017 allows IFC.

| Name | URL | Type | Activity | Automated reading | Dominant topics | Notes |
|---|---|---|---|---|---|---|
| forum.dwg.ru | https://forum.dwg.ru/ (Revit board: https://forum.dwg.ru/forumdisplay.php?f=58) | Forum | High (43 records, 2009-2026) | Partly: thread pages (`showthread.php?t=<id>`) fetch but text is served in cp1251 and appears garbled without re-encoding; the forum's search returned 404 or a pinned FAQ | IFC between Revit, Tekla, ArchiCAD, Sapfir, SCAD, STARK ES, Bocad, AutoCAD, nanoCAD; "how to open IFC correctly"; state expertise and 2019 BIM requirements | Classic Russian engineer voice: short, direct, jargon-heavy ("выгрузка в IFC", "ИМ" = information model); long-running threads from 2009 to 2026 |
| Habr | https://habr.com/ | Developer blog/portal | Medium (32 records, 2019-2026) | Partly: article pages readable; search is JavaScript-rendered; comment text not returned | IDS checking (IfcOpenShell), AGR.Checker for Revit, IDS Core in the browser, post-processing IFC without Revit, IFC vs USD opinions, writing a BIM viewer | Long professional essays by BIM developers (PIK Digital, kirbim); data-first opinions. Questions appear in comments, which we could not read |
| Telegram channels | https://t.me/s/ifc_ru ("Всё про IFC"), https://t.me/s/revithelper_kmv (RevitHelper), https://t.me/s/bimlib_pro (BIMLIB), https://t.me/s/prostobim ("Просто о BIM"), https://t.me/s/bimacad ("Академия BIM") | Chat/channels | Medium (10 records, 2022-2026) | Partly: the public `t.me/s/<channel>` preview works for some channels; others return a stub without posts (`bimdigest`, `revitapi`); closed chats not reachable | IDS requirements for expertise, regional BIM instructions (Sverdlovsk region), export settings | Channel posts, not Q&A; discussion chats are closed |
| sapr.ru and dwg.ru news | https://sapr.ru/ , https://dwg.ru/ | Trade portals | Low (2 to 3 records) | Fetchable | nanoCAD SPDS and IFC from Revit; Revit vs Tekla vs Allplan | Trade-press voice |
| Renga vendor site and blog | https://rengabim.com/ , https://blog.rengabim.com/ | Vendor | Low (2 records) | Fetchable | How to accept IFC, export of attributes, formats | Russian BIM software with its own IFC mapping |
| YouTube (Russian) | https://www.youtube.com/watch?v=VPlQf3fv908 | Video | Low (4 records, 2020-2022) | Not read | IFC export and viewers | Lecture style |
| VK groups, tgstat, cyberforum, RBC | https://vk.com , https://tgstat.ru , cyberforum.ru , https://companies.rbc.ru/ | Social/portals | Unknown | Not searchable / 403 / 401 | - | Likely sources for casual chatter; unreachable |
| Official: Mosgosexpertiza, SPb state expertise, Minstroy | see [sources_index.md](sources_index.md#28-russia) | Official | Official | Partly | Requirements for ТИМ in IFC | The "regulation voice" |

---

## 3. Chinese-speaking community (mainland China, Taiwan, Hong Kong)

See [../05_real_world_questions/by_language/zh.md](../05_real_world_questions/by_language/zh.md). Mainland practice is driven by city-level review platforms (Shenzhen SZ-IFC, Guangzhou, Nanjing, Shanghai) and by domestic software (Glodon, PKPM/BIMBase, Revit with plug-ins). Questions are often "how to..." blog titles rather than forum threads.

| Name | URL | Type | Activity | Automated reading | Dominant topics | Notes |
|---|---|---|---|---|---|---|
| Zhihu (zhuanlan and Q&A) | https://zhuanlan.zhihu.com/ , https://www.zhihu.com/ | Q&A and articles | High (55 records: 41 zhuanlan + 14 Q&A, 2016-2026) | Blocked: HTTP 403 on every fetch; records are snippets | What IFC is and which software opens it, Revit IFC export losses and GUID, SZ-IFC, Shanghai review, domestic lightweight engines, MCP for Revit ("Revit接入大模型") | Mixture of explainer articles and genuine questions ("revit2019导出IFC没有反应") |
| CSDN | https://blog.csdn.net/ , https://ask.csdn.net/ | Developer blogs and Q&A | Medium (35 records, 2019-2025) | Blocked: frequent HTTP 521 or captcha; some pages read as snippets | glTF/Three.js pipelines, xBIM, IfcOpenShell, Chinese-text encoding in IFC, missing elements after opening in Revit | Code-heavy; error messages quoted verbatim |
| cnblogs | https://www.cnblogs.com/ | Developer blogs | Medium (18 records, 2018-2026) | Partly: article pages readable; search 404 or human-verification page | IFC document series, xBIM series, Revit category to IFC class mapping, lightweight viewers | Long-running enthusiast series (西北逍遥, 张传宁) |
| Juejin, SegmentFault, Jianshu | https://juejin.cn/ , https://segmentfault.com/ , https://www.jianshu.com/ | Blog platforms | Low-Medium (2 to 3 records each) | Partly (Jianshu 403, Juejin sometimes empty) | 2026 retrospectives on large BIM on the web, Revit-to-Three.js pitfalls, base-point settings | Recent (2026) developer experience |
| Baidu Zhidao | https://zhidao.baidu.com/ | Q&A | Low (3 records, 2025) | Fetchable | "IFC invisible in Revit - 7 causes", base point and survey point | Closest to everyday user-question voice |
| Zhulong (筑龙), co188 | https://bbs.zhulong.com/ , https://www.zhulong.com/ , https://bbs.co188.com/ | Construction forums | Low (2 records each) | Snippet / partly | Revit to BIM5D (Glodon) import, open newer RVT in older Revit via IFC2x3 | Industry-forum voice, many snippets |
| Gitee | https://gitee.com/explore/topic/BIM | Code host | Low | Fetchable | Chinese lightweight BIM engines, IFC export | Awesome-BIM list |
| bilibili | https://www.bilibili.com/ | Video | Low (5 records, 2022-2023) | Blocked (captcha on read pages) | BlenderBIM tutorials, Revit 2023 IFC mapping dialog | Chinese-dubbed Bonsai tutorials |
| Taiwan: PTT, blogs, city offices | https://www.ptt.cc/ , https://housegear.pixnet.net/ , https://dbadgp.gov.taipei/ , https://www.bim.ntpc.gov.tw/ | Forum, blogs, official | Low | PTT blocked (403); official PDFs partly fetchable | Importing IFC into Revit (2013 blog), as-built model upload, permit templates | Uses Traditional Chinese; vocabulary differs from mainland sources |
| Taiwan MCP community | https://github.com/shuotao/REVIT_MCP_study | Issue tracker | Low-Medium (7 records, 2026) | Fetchable | create_wall level choice, DWG beams to walls, pyRevit limits | Traditional Chinese prompts to AI tools |
| Hong Kong: Buildings Department, CIC | https://www.bd.gov.hk/ , https://www.bim.cic.hk/ | Official | Official | Partly (PDFs failed in places) | BIM plan submission, Archicad/Revit IFC workshops, openBIM beginner guide | Mixed Traditional Chinese and English |
| WeChat public accounts, Xiaohongshu, Douyin | - | Social | Unknown | Not reachable by this method | Expected: BIM tips and job content | Not researched |

---

## 4. Japanese-speaking community

See [../05_real_world_questions/by_language/ja.md](../05_real_world_questions/by_language/ja.md). Japan is currently moving to BIM-based drawing review (from April 2026, with a data review planned about 2029), which drives a lot of blog commentary.

| Name | URL | Type | Activity | Automated reading | Dominant topics | Notes |
|---|---|---|---|---|---|---|
| Qiita | https://qiita.com/tags/ifc | Developer articles | Medium (22 records, 2019-2026) | Partly: article pages fetch; list and search pages are JavaScript-rendered | IfcOpenShell (lazy loading in 0.9), Revit API and UniqueId vs IFC GUID, web-ifc, IFC to RAG, CityGML/PLATEAU | First-person developer notes; frequent authors: kiyuka, Takashi_Kasuya, dnp-hiraoka |
| Zenn | https://zenn.dev/ | Developer articles and "scraps" | Medium (18 records, 2023-2026) | Fetchable (topic API works) | IFC attributes to Excel, IDS explained, building IFC from scratch, IFC Validation Service local, Revit-MCP, Claude Code Revit add-in | Scraps are short question-like notes (e.g. FlangeSlope) |
| note | https://note.com/ | Blog platform | Medium (14 records, 2025-2026) | Fetchable (hashtag pages) | BIM drawing review, 2029 data review, "IFC is not omnipotent", Bonsai in practice, small MEP office | Business-professional and consultant voice (ONESTRUCTION, arent3d) |
| buildingSMART Japan | https://www.building-smart.or.jp/ | Chapter | Official | Fetchable | IFC certification (IFC検定), MVD, certified software list, summit 2026 | Mentions local software GLOOBE Architect, Jw_cad, Rebro |
| Study groups | TokyoAECDev IFC study group (via a Qiita recap) | Meetup | Unknown | Not researched | IFC study | Named only |
| Teratail, OKWave, Twitter/X, Autodesk Japan forum | - | Q&A / social / vendor | Unknown | Not reached (Autodesk JP 403) | - | Likely sources of real questions; missing |

---

## 5. Korean-speaking community

See [../05_real_world_questions/by_language/ko.md](../05_real_world_questions/by_language/ko.md).

| Name | URL | Type | Activity | Automated reading | Dominant topics | Notes |
|---|---|---|---|---|---|---|
| buildingSMART Korea | https://www.buildingsmart.or.kr/ | Chapter | Official (7 records, 2010-2026) | Fetchable | BIM overview, R&D centre, certification exams, guides (MOLIT 2010, facility BIM guideline v2.0) | Official voice; 2010 guide is old |
| Korea Open BIM Research Group | https://www.kbims.or.kr/ | Research group | Low | Not fetched (listed only) | Open BIM research 2017-2021 | - |
| Naver cafes, Seumteo permit portal | - | Community / government | Unknown | Not fetched (login-gated likely) | Permit BIM review | Gap |

---

## 6. German-speaking community (Germany, Austria, Switzerland)

See [../05_real_world_questions/by_language/de.md](../05_real_world_questions/by_language/de.md). Terms people use: AIA (client requirements), BAP (execution plan), Datenaustausch, Bauteil, Projektbasispunkt.

| Name | URL | Type | Activity | Automated reading | Dominant topics | Notes |
|---|---|---|---|---|---|---|
| BIM me UP! | https://bim-me-up.com/ | Educator blog | Medium (15 records, 2016-2025) | Fetchable | Revit IFC export: coordinates, type parameters, phases, storeys, IFC 5, link vs Data Exchange | German blog, also English; tutorial voice |
| BIM Deutschland | https://www.bimdeutschland.de/ | Federal initiative | Official (4 records, 2025) | Fetchable | AIA/BAP templates, MVD, CDE, FAQ | Machine-readable AIA portal with REST API |
| BIMpedia | https://www.bimpedia.de/ , https://www.bimpedia.eu/ | Wiki/articles | Unknown | Blocked (connection refused) | Openings and recesses, Archicad-Revit export | Articles seen only as titles |
| cad.de forum, Allplan forum, Autodesk DE forum, Graphisoft DE | https://forum.cad.de/ , https://forum.allplan.com/ | Forums | Unknown | DNS failure / 403 | - | The real German asker voice was not reached; German records are blog and official documents |
| OSArch (German drawing conventions) | https://community.osarch.org/discussion/3750/german-drawing-conventions-din-1356-1-for-bonsais-2d-output-a-reference-from-vocational-training | Forum thread | Low | Fetchable | DIN 1356-1 for Bonsai 2D output | Vocational-training angle |
| Baunetzwissen, Bavaria, Saxony, DB InfraGO | https://www.baunetzwissen.de/ , https://www.bim.bayern.de , https://sib.sachsen.de/ | Trade and official | Low | Partly | LOD/LOI, BAP templates, railway BIM | Official voice |
| Switzerland: bauen digital, SBB, Geneva | https://bauen-digital.ch/ , https://company.sbb.ch/ , https://www.ge.ch/ | Official / chapter | Low | Fetchable (Geneva), others partly | IFC deposit standard for permits (Geneva), Swiss glossary | French and German |

---

## 7. Dutch and Nordic communities

| Name | URL | Type | Activity | Automated reading | Dominant topics | Notes |
|---|---|---|---|---|---|---|
| digiGO (BIM basis ILS) | https://www.digigo.nu/ | National information standard | Official (7 records, 2024) | Fetchable | IFC conventions: entities and proxies, storeys, local position, property sets, spaces, materials | Prescriptive Dutch voice; software manuals for Revit, Archicad, Tekla, Vectorworks etc. See [../05_real_world_questions/by_language/nl.md](../05_real_world_questions/by_language/nl.md) |
| nl-digigo GitHub (NLCS, IMWO, GeoBIM) | https://github.com/nl-digigo/NLCS | Issue tracker | Low-Medium (5 records, 2023-2025) | Fetchable | NL-SfB classification, export from Revit | Dutch-English mix |
| OpenAEC (Delft) | https://github.com/OpenAEC-Foundation | Open-source group | Low-Medium (2026) | Fetchable | IDS-based validation, "computational design day" materials | Dutch open-source AEC |
| Dutch forums (bimconnected, bimnieuws) | - | Forums | Unknown | Certificate expired / did not resolve | - | Not reachable |
| buildingSMART Norge | https://www.buildingsmart.no | Chapter | Official (10 records, 2025-2026) | Fetchable | IFC/IDS/BCF/bSDD explained in Norwegian, POFIN 1.0, infra domain, working groups | See [../05_real_world_questions/by_language/nordic.md](../05_real_world_questions/by_language/nordic.md) |
| BIMpraten podcast, MMI-veilederen | https://www.bimpraten.no/ , https://www.mmi-veilederen.no/ | Podcast / guide | Low | Fetchable | Model maturity index used by public clients | - |
| Sweden, Finland, Denmark, Baltics | https://www.bimalliance.se/ , https://www.buildingsmart.fi/ , https://www.molio.dk/ , https://www.skaitmeninestatyba.lt/ , https://www.digitaalehitus.ee/ | Chapters / bodies | Unknown | Home pages listed; content not read | - | Only named in reports |

---

## 8. Spanish- and Portuguese-speaking communities

See [../05_real_world_questions/by_language/es.md](../05_real_world_questions/by_language/es.md) and [../05_real_world_questions/by_language/pt.md](../05_real_world_questions/by_language/pt.md).

| Name | URL | Type | Activity | Automated reading | Dominant topics | Notes |
|---|---|---|---|---|---|---|
| OSArch Spanish category | https://community.osarch.org/ | Forum category | Medium (about 112 threads; 1 KB record) | Fetchable | Bonsai in Spanish, Revit migration | Mixed with English threads |
| Espacio BIM, e-zigurat, BIMnD, construible | https://www.espaciobim.com/ , https://www.e-zigurat.com/ , https://www.bimnd.es/ , https://www.construible.es/ | Educator blogs / trade press | Medium (3 + 2 records) | Fetchable | Exporting good IFC from Revit, IFC and interoperability, Plan BIM news | Educator voice (10 tips for exporting a good IFC) |
| buildingSMART Spain | https://www.buildingsmart.es/ | Chapter | Official | Fetchable | IFC delivery manual (MEI Edificacion), BIM in public contracts | - |
| Autodesk and Graphisoft Spanish boards | https://forums.autodesk.com/ | Vendor forum | Low (2 Spanish records) | Blocked (403) | Revit to ETABS via IFC, IFC problems | Seen only as titles |
| Planbim Chile | https://planbim.cl/ | National programme | Official (3 records, 2022) | Partly (several subpages 404) | IFC entity sheets, IFC 4.3/4.4, public-sector standards | Latin-American public-sector voice |
| Peru MEF, Colombia MinVivienda and Camacol, Costa Rica CFIA | https://www.mef.gob.pe/ , https://bim.minvivienda.gov.co/ , https://www.camacol.co/ , http://cfia.or.cr/ | Official | Official | PDFs often not machine-readable | National BIM plans and guides | - |
| Spanish MCP projects | https://github.com/joacos/archicad-mcp , https://github.com/JefaturaBIM94/RevitMCPBOQ | GitHub | Low | Fetchable | Archicad prompts, quantity take-off (BOQ) prompts in Spanish | Real Spanish prompt style for AI tools |
| Brazil / Portugal | https://buildingsmart.pt/ , https://www.buildingsmart.org.br/ , AltoQi | Chapters / vendor | Unknown | Home pages listed; planalto.gov.br blocked | Brazil Estrategia BIM BR, Decreto 10.306/2020, ABNT NBR 15965, SINAPI | Only one Portuguese real record exists; Brazilian forums were not reached |

---

## 9. Italian and French communities

| Name | URL | Type | Activity | Automated reading | Dominant topics | Notes |
|---|---|---|---|---|---|---|
| BibLus (ACCA software) | https://biblus.acca.it/ | Vendor trade portal | Medium (24 records, 2017-2026) | Fetchable | Italian BIM obligation (code art. 43, Annex I.9), capitolato informativo (EIR), oGI offer, IFC class mapping, coordinates, usBIM checker, DWG to IFC, IFC editing problems | Article titles read like questions; see [../05_real_world_questions/by_language/it.md](../05_real_world_questions/by_language/it.md) |
| Ingenio | https://www.ingenio-web.it/ | Trade portal | Low (4 records, 2026) | Fetchable | IFC units, FireRating in Pset_WallCommon, IFC for infrastructure | - |
| Italian forums (ACCA support, BIM Italia), Reddit | - | Forums | Unknown | Not reached (Autodesk IT 403) | - | Asker voice missing |
| KROQI (CSTB) | https://www.kroqi.fr/ | National collaborative platform | Official (read) | Fetchable | IFC and BCF collaboration, knowledge base | See [../05_real_world_questions/by_language/fr.md](../05_real_world_questions/by_language/fr.md) |
| BIM&CO | https://www.bimandco.com/ | Object platform with Revit plugin | Low | Fetchable | No IFC content found | - |
| MediaConstruct (buildingSMART France) | https://www.mediaconstruct.fr/ | Chapter | Unknown | Blocked (403); buildingsmart.fr is a parked domain | - | French voice is nearly absent (4 real records) |
| Quebec, Geneva, Brussels, Luxembourg | https://www.sqi.gouv.qc.ca/ , https://www.ge.ch/ , https://buildingsmart.be/ , https://www.crtib.lu/ | Official | Low | Fetchable | BIM roadmaps, permit IFC deposit | Francophone official voice |

---

## 10. Other regions and languages

| Name | URL | Type | Activity | Automated reading | Dominant topics | Notes |
|---|---|---|---|---|---|---|
| Singapore: CORENET X (BCA) and community tools | https://info.corenet.gov.sg/ | Government portal | Official; many pages read (3 official records plus 8 community-tool records) | Fetchable (support hub 403) | IFC+SG data structure, Excel mapping file, model checker, circulars, tool-specific setup (Revit, Archicad, Tekla) | Community GitHub tools repair IFC-SG validation errors (see [sources_index.md](sources_index.md#44-singapore-community-tools-unofficial-helpers-for-ifcsg-submissions)) |
| United Kingdom and Ireland | https://imiframework.org/ , https://cwmf.gov.ie/ | Frameworks | Official | Fetchable | ISO 19650, Uniclass, COBie, Irish public-sector requirements | UK asker voice sits on the English forums above |
| USA / Canada infrastructure | https://www.fhwa.dot.gov/bridge/bim/ , https://pooledfund.org/Details/Study/1798 | Government | Official | Fetchable | Bridge IFC, unit-test suites, digital delivery | Pooled-fund projects on IFC validation |
| Middle East and Africa | https://www.cidb.org.za/ , https://hub.dm.gov.ae/ | Government | Low | Partly | cidb BIM strategy; Dubai Municipality BIM submission (content unconfirmed) | No community forums found; OSArch search for "Dubai" returned nothing |
| India, Australia, New Zealand | https://bim.natspec.org | Portal | Unknown | Not read | NATSPEC National BIM Guide | No local forums found |
| Turkey | https://github.com/BerkantACUN/ifc-ruhsat | Open-source | Low | Fetchable | Turkish building-permit check for IFC 4.3 | README in Turkish |
| Slovakia, Vietnam, Czech Republic | https://github.com/Menezeris/AIMviewer , https://github.com/andyluu98/vn-revit-mcp , https://www.cadforum.cz/ | GitHub / blog | Low | Fetchable | AI viewer camera prompts (Slovak), Vietnamese Revit MCP, extended IFC for Revit 2026 (Czech) | Single records: shows that MCP users prompt in their own language |
| Arabic, Greek | - | - | Unknown | - | - | One stray record each; no community reached |

---

## 11. Which community to imitate for which kind of test request

| You want a test request that sounds like... | Imitate | Look at |
|---|---|---|
| A frustrated Revit user whose IFC lost something | Autodesk revit-ifc issues; Autodesk Community titles; Dynamo forum | `python tools/kb.py filter --kind real --topic export_revit --lang en --limit 20 --format brief` |
| An IFC-literate coordinator citing the standard | buildingSMART forum | `--topic versions_mvd` or `ids_requirements` |
| An open-source enthusiast or Python developer | OSArch, IfcOpenShell issues, Zenn/Qiita | `--topic programming_ifcopenshell` |
| A web developer with a huge file | That Open web-ifc issues, Juejin/CSDN | `--topic file_size_performance` |
| A Russian engineer worried about state expertise | forum.dwg.ru, Habr, Telegram | `--lang ru --topic national_requirements` |
| A Chinese user asking "how do I..." | Zhihu, Baidu Zhidao, CSDN | `--lang zh` |
| A Japanese developer note | Qiita, Zenn, note | `--lang ja` |
| A person talking to an AI assistant | Revit MCP issue trackers, Dynamo AI thread, Zhihu MCP articles | `--topic ai_llm_mcp` |

## 12. Practical notes for automated reading

- **Discourse forums** (buildingSMART, Dynamo, pyRevit, Cesium): append `.json` to topic and category addresses or use `search.json?q=...`; expect HTTP 429 if you query quickly.
- **GitHub**: use the issue and discussion pages or the `gh` command line; the REST search API rate-limits within a few dozen calls.
- **Telegram**: only `https://t.me/s/<channel>` previews, and not every channel shows posts.
- **Chinese platforms**: assume Zhihu, CSDN and bilibili are blocked; cnblogs article pages and Baidu Zhidao work, but their search pages do not.
- **forum.dwg.ru**: decode as cp1251; use thread IDs from [sources_index.md](sources_index.md#appendix-a-forum-threads-examples-of-real-user-language) instead of the search box.
- **Autodesk and Graphisoft communities, buildingSMART main sites**: treat as blocked; use GitHub copies of the standards and search-snippet text only.
- **Qiita**: list pages need JavaScript; use direct article addresses. **Zenn**: its topic API works.
- Do not treat a page as read just because it is listed; look for the `[read]` / `[snippet]` / `[blocked]` tags in [sources_index.md](sources_index.md).

## 13. Not yet covered (candidates for the next research wave)

Reddit and Stack Overflow; LinkedIn groups; Autodesk and Graphisoft communities (threads are known only as snippets); Tekla, Allplan, Vectorworks and Bentley forums; German forums (cad.de and vendor boards); Italian, French and Portuguese asker communities; Korean Naver cafes; Japanese Q&A sites (Teratail, OKWave); VK and closed Telegram chats; WeChat accounts; Middle East, Africa, India and Australia/New Zealand communities. The `research_raw/wave1/` reports for these cells (for example `en-reddit`, `en-stackoverflow`, `en-navis-acc`, `en-graphisoft`, `en-allplan-vw-bentley`, `ru-dwg-revit`, `ru-renga-nanocad`, `ru-tim-expertiza`, `pt-brazil`) record 0 real posts and should be re-run with search access.
