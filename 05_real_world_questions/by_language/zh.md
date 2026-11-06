# Chinese: how people ask about IFC, BIM and Revit

**Last compiled: 2026-11-06.** Language codes: `zh` (Simplified, Mainland China, the large majority) and `zh` in Traditional script (Taiwan and Hong Kong, about one in nine real records). Built from `research_raw/wave1/zh/*` plus the Chinese-language records found in the AI/MCP, topic and role cells.

## Read this first (what the data can and cannot tell you)

- **Size of the evidence.** 166 real records (150 distinct URLs; some pages were logged by several research cells) and 132 synthetic prompts. About 19 real records and 15 synthetic prompts are in Traditional script.
- **"Real" here means "observed at a real page", not "a help-desk question".** Most real records are blog titles, Zhihu column articles, search-result snippets, government notices and GitHub issues. Zhihu returned HTTP 403, CSDN returned 521 and PTT returned 403 during collection, so question bodies and answers were mostly **not** read. The `question_paraphrase` fields are reconstructions from titles and snippets, and years are partly estimated from article IDs.
- **Genuine asker voice is thin.** The closest things to it are Baidu Zhidao and Zhihu question titles, CSDN Q&A titles, GitHub issues by Chinese speakers, and the short symptom-style titles of personal blogs.
- **Not reached at all:** PTT, Mobile01, Facebook BIM groups, WeChat public accounts, Xiaohongshu, Douyin, Hong Kong forums. Do not assume the habits of those communities match this file.
- Standard numbers in the "Local ecosystem" section are taken from the research records; where a record says "unverified" the national document does too. See [Mainland China national requirements](../../02_standards_regulations/national/china_mainland.md).

## Where people ask

Counts are distinct source URLs among the 150 real pages. They show where the *research found material*, not the real size of each community.

| Platform | Script | Distinct URLs | What you find there | Access notes |
|---|---|---|---|---|
| Zhihu (`zhuanlan.zhihu.com` articles, `www.zhihu.com` questions) | Simplified | 36 + 12 | "IFC是什么意思?", "有没有好用的IFC查看工具", "如何评价广联达数维和构力BimBase", Revit export failures, SZ-IFC how-tos, AI/MCP hype pieces | 403 on fetch; titles and snippets only. Many columns are vendor marketing |
| CSDN (`blog.csdn.net`, `ask.csdn.net`) | Simplified | 23 + 6 | Developer notes (IfcOpenShell, xBIM, web-ifc, glTF), Revit export tips; Q&A pages that mirror English GitHub issues | 521 on fetch. Some posts are auto-generated README rewrites ("gitblog" accounts): low trust, not used |
| cnblogs (博客园) | Simplified | 15 | Enthusiast series: xBIM 基础/实战, IFC document walk-throughs, Revit export tables, "BIM轻量化之路" | Fetchable. Best source of real long-form learner voice |
| Baidu Zhidao (百度知道), Zhulong (筑龙), CO188 (土木在线), Jianshu | Simplified | 3 + 3 + 1 + 2 | Plain Revit users: "ifc导入revit后三维不可见", base-point set-up, BIM5D import, Revit version compatibility | Zhidao readable; Jianshu 403; Zhulong mostly snippets |
| Juejin, SegmentFault, Gitee | Simplified | 2 + 3 + 1 | Front-end engineers: large BIM in the browser, Three.js pipelines, RVT to SVF stuck at 35% | Fetchable; Gitee hosts domestic lightweight-engine projects |
| bilibili | Simplified | 4 | Video series: Revit 2023 new features (IFC mapping dialog), Chinese-dubbed BlenderBIM tutorials | Read pages return captcha; titles only |
| GitHub issues | Simplified, Traditional, English | 14 | Chinese-speaking users of Revit-MCP projects (`shuotao/REVIT_MCP_study`, `ZedMoster/revit-mcp`, `mcp-servers-for-revit`) write in Chinese; users of IfcOpenShell, web-ifc, revit-ifc write short English | Open. Best source of structured, honest bug/feature wording |
| Government and standards bodies (Shenzhen, Guangzhou, Nanjing, Shanghai, Hubei; HK BD/DEVB/CIC; Taipei, New Taipei) | Simplified and Traditional | ~12 | Not questions: they define what people later ask (SZ-IFC, 宁建模, 竣工模型上繳) | Some PDFs unreadable; used as titles or snippets |
| Vendor help (Autodesk China KB, Graphisoft Taiwan help), theses (NTU, NTUST, NCU) | both | 3 + 5 | Formal wording of known problems: missing elements, custom property sets, IFC data loss between Revit and ETABS/SAP2000/Robot | Fetchable |

## Top themes (ranked)

Ranking combines the record counts per KB topic (real records, distinct URLs; a record can carry up to four topics) with the research reports. Counts are indicative.

| Rank | Theme | Records (topic tag) | Typical wording | Related KB doc |
|---|---|---|---|---|
| 1 | **Revit to IFC export problems**: export option greyed out or "no response", GUID not generated, "导出ifc没有东西", category-to-class mapping, shared parameters lost, colours grey | 29 | "revit2019导出IFC文件没有反应？" | [Revit export and class mapping](../by_topic/revit_export_and_class_mapping.md) |
| 2 | **Conversion and 轻量化 (lightweighting)** for web, Unity, Cesium: IFC to glTF/3D Tiles/FBX, keep component ID and properties, 100 MB model becomes 1 GB IFC | 29 conversion + 14 file size | "BIM轻量化的原理是什么" | [File size, viewing, conversion](../by_topic/file_size_viewing_conversion.md) |
| 3 | **Local government submission (报建/报审/审图)**: Shenzhen SZ-IFC self-check, Guangzhou GDB, Nanjing 宁建模, Shanghai EDM, Hubei H-IFC, HK BD, Taipei/New Taipei IFC upload | 26 national + 18 permitting | "审查节点有些值是空的" | [Regulations, permits, contracts](../by_topic/regulations_permits_contracts.md) |
| 4 | **Open and inspect IFC without Revit**; "what is IFC", RVT vs IFC | 25 viewers + 11 basics | "有没有好用、方便的IFC查看工具给推荐一下？" | [What is IFC](../../01_ifc_basics/01_what_is_ifc_and_versions.md) |
| 5 | **Importing IFC into Revit**: invisible in 3D, blank view, linked IFC not editable, far-from-origin, file bloat | 10 | "ifc导入revit后三维不可见" | [Import and interoperability](../by_topic/import_and_interoperability.md) |
| 6 | **Coordinates and base points**: 项目基点 vs 测量点, 2000坐标 (CGCS2000), multi-person podium models, SZ-IFC base-point checks | 12 | "怎么设置测量点和基点…求教" | [Coordinates, georeference, units](../by_topic/coordinates_georef_units_levels.md) |
| 7 | **Developers parsing IFC**: IfcOpenShell, xBIM, web-ifc setup, Chinese text as `\X2\...\X0\`, wasm LinkError | 10 + 8 | "ifcopenshell刚装好…import有时候报错" | [Programming and automation](../by_topic/programming_and_automation.md) |
| 8 | **国产BIM software choice** (广联达数维, 构力BimBase/PKPM, EasyBIM, 斯维尔) and how well each handles IFC | 11 | "如何评价…两款国产BIM软件？" | [Authoring tools](../../03_software/authoring_tools_ifc.md) |
| 9 | **Materials, colours and information lost** when moving between Max, SketchUp, Tekla, ArchiCAD and Revit | ~10 | "Su 导入 Revit 材质总是丢失怎么办？" | [Import and interoperability](../by_topic/import_and_interoperability.md) |
| 10 | **AI, LLM and MCP with Revit/IFC** (new in 2025-2026): connecting Cursor/Claude, safe batch edits, fear for 二开 jobs | 11 | "世界发展真快 马上二开要失业了" | [MCP servers and AI tools](../../04_open_source/mcp_servers_and_ai_tools.md) |
| 11 | **Data loss in IFC round trips between design and analysis tools** (mostly Taiwan theses: Revit to ETABS, SAP2000, Robot) | ~3 | "IFC方式資料遺失或更動" | [Import and interoperability](../by_topic/import_and_interoperability.md) |
| 12 | **Versions and validation**: IFC2x3 vs IFC4, IDS, IFC4.3 for roads | ~6 | "IFC2x3和IFC4之间的一些主要区别" | [Versions, MVD, encoding, GUID](../by_topic/versions_mvd_encoding_guid.md) |

Persona mix of the real records (distinct URLs): developers 53, BIM coordinators 28, students 18, BIM managers 12, architects 11, reviewers/authorities 11. Structural, MEP, estimator and facility personas are rare in real data; the synthetic prompts add them.

## Local ecosystem

Facts below come from the research records; items marked *(unverified)* are not confirmed in primary sources.

**Mainland China**

| Item | What it is | Source in KB |
|---|---|---|
| GB/T 51212-2016 (BIM unified standard); GB/T 51269, 51301, 51447; GB/T 25507 (IFC platform spec) | National recommended standards. Numbers other than 51212 are *(unverified)* in the national doc | [China national doc](../../02_standards_regulations/national/china_mainland.md) |
| **Shenzhen SZ-IFC** (SJG114-2022) | Storage standard; an SZ-IFC converter plug-in and a self-check tool. Records say tool 1.3.0 is required from 2024-01-01 and that 1.1.0-passed models stop uploading; projects above a size/cost threshold must apply BIM from 2023 (as reported). Common failures: empty base-point, elevation and true-north values, lost fields | `zh-lightweight-review-r001/r003/r027`, [SZ-IFC handbook post](https://www.sunyuanrui.com/works/sz-ifc-research/) |
| **Guangzhou** | BIM planning-approval trial from 2020-10-01 and BIM-assisted construction-drawing review (upload 2D drawings and BIM model together); GDB files per discipline; CIM platform and a 2025 white paper on 自主可控BIM | `zh-lightweight-review-r019/r020/r021/r023` |
| **Nanjing** | 宁建模 lightweight format, BIM smart review, local standard DB3201/T 1145-2023 for as-built delivery | `zh-lightweight-review-r024/r025` |
| **Shanghai** | BIM-assisted review trial from 2024-02-01 using the EDM data file; IFC used for structural loads | `zh-lightweight-review-r026`, `zh-zhihu-r024` |
| **Hubei** | H-IFC provincial BIM cloud platform (reported June 2026) | `zh-lightweight-review-r030` |
| Chengdu, Wuhan | Vendor claim that EasyBIM contains IFC review rules for four cities *(marketing, unverified)* | `zh-zhihu-r026` |
| Domestic software | 广联达 (Glodon: 数维建筑, BIM5D, BIMFACE), 构力 PKPM-BIM/BIMBase (PModel), EasyBIM, 斯维尔 ueBIM, 中望CAD (IFCIMPORT), SuperMap exporter, BIMSee (free IFC viewer), 迪威/GISBox/CesiumLab converters | [Authoring tools](../../03_software/authoring_tools_ifc.md), [viewers and converters](../../03_software/viewers_checkers_cde_converters.md) |
| Foreign tools in daily use | Revit (with IFC exporter), Tekla, ArchiCAD, Navisworks, BIM Vision | [Revit IFC export reference](../../03_software/revit/ifc_export_reference.md) |
| Open source | IfcOpenShell/IfcConvert, xBIM, web-ifc/web-ifc-three, xeokit (licence claims conflict), three.js, Bonsai/BlenderBIM; Gitee: BIMI, BIM-LW, GimViewer | [Libraries](../../04_open_source/libraries_and_toolkits.md), [community](../../04_open_source/community_projects_and_enthusiasts.md) |
| Educators and enthusiasts | cnblogs series by 西北逍遥 and 张传宁 (xBIM); Zhihu "BIM学习心得" series; bilibili iBlender BlenderBIM dubbing; "每日一练" Revit tips | `zh-zhihu-r013/r014`, `zh-csdn-dev-r036` |

**Hong Kong and Taiwan (Traditional script)**

- **Hong Kong:** Buildings Department (屋宇署) BIM page with Revit/ArchiCAD plug-ins that check floor area, sanitary and fire items; the submitted BIM model is *supplementary* and drawings prevail if they disagree. DEVB roadmap (Dec 2023) names 2029 as the tentative mandatory date for BIM plan submission. CIC runs open BIM workshops (ArchiCAD to Revit IFC exchange). Terms: 建築信息模擬, 認可人士 (AP), 圖則.
- **Taiwan:** Taipei as-built (使照竣工) model is uploaded as IFC then converted by the system; New Taipei has a Revit permit template and computer-aided checking (工務局BIM工作參考手冊108年版); rule-checking research is built on the 建築技術規則. ROC years (「108年版」 = 2019) are normal in official text.
- buildingSMART Taiwan, TW-BIM standards and Taiwan Construction and Planning Agency IFC guidance were **not found**.

## How people write

### Register, length and structure

- **Titles are the question.** Typical shapes: a bare term (`IFC是什么意思?`, `IfcBuildingElementProxy`), `XX怎么办 / 如何解决 / 是为什么 / 怎么回事`, `有没有…推荐一下？`, `如何评价…`, or a symptom with no verb (`ifc导入revit后三维不可见`, `revit导出ifc没有东西`). Titles run 10-30 characters.
- **Bodies are one or two lines** with a Revit version and a symptom (`revit2019点击导出IFC后没反应，导出位置只有一个schema文档`). Detail grows only on developer blogs, GitHub and CSDN, where error text is pasted verbatim.
- **Learner notes** use hedges (`应该是`, `好像`), numbered series (`xBIM 基础16`, `实战01`, `第二节`, `step7`, `BIM学习心得20`) and relief openers (`终于搞清了…`).
- **Closers:** `求教` / `请教` on Q&A boards; hype closers on vendor posts (`完全免费！`, `干货满满`). Almost no greetings or thanks inside titles.
- **Advice culture is trial-and-error:** "重装软件或换一台电脑导出" appears as a standard remedy.

### Simplified vs Traditional vocabulary

| Concept | Mainland (Simplified) | Taiwan / Hong Kong (Traditional) |
|---|---|---|
| export / import | 导出 / 导入, 导进, 链进来 | 匯出 / 匯入 (vendor help sometimes mainland-like 導入/導出) |
| model, element | 模型, 构件 | 模型, 元件 |
| permit submission | 报建, 报批, 审图 | 送審, 查核, 建照/使照 (permits), 竣工 (as-built) |
| drawings | 图纸 | 圖面, 圖則 (HK) |
| BIM | BIM, 建筑信息模型 | BIM, 建築信息模擬 (HK), 建築資訊模型 (TW) |
| openings / sleeves | 开洞, 预留洞, 套管 | 開孔, 套管, 貫穿 |
| convert CAD to Revit model | 翻模 | 翻模 |
| English kept inside Chinese | `revit`, `ifc`, `proxy`, `GUID`, `MVD`, `Pset` | `REVIT`, `ARCHICAD`, `proxy`, `MVD`, `GUID`, `Pset` |

Mixed-script posts occur (Traditional UI labels with Simplified comments). Generated prompts should pick one script and stay consistent.

### Jargon and slang

| Term | Meaning | Standard / neutral term |
|---|---|---|
| 轻量化 | converting a heavy model into a light, browser-friendly format; also "shrinking" | model decimation / lightweight format (glTF, 3D Tiles, wexbim) |
| 减肥 | slim down a bloated file (151 MB Tekla IFC became 2 GB in Revit) | reduce file size |
| 合模 / 合模神器 | merge discipline models and view them together | federated model / model merge |
| 神器 | "killer tool" (hype word for free viewers) | tool |
| 报建 / 报批 / 报审 / 审图 | submit to the authority; drawing review | permit submission / approval / review |
| 自检(工具) | the official pre-upload check tool (Shenzhen) | self-check / validation |
| 图模一致 / 图模对位 | drawings and model must agree | drawing-model consistency |
| 二开 | secondary development (writing add-ins) | custom development / API |
| 翻模 | rebuild a CAD drawing as a BIM model | scan-to-BIM style remodelling from 2D |
| 构件 | building component | element (IfcProduct) |
| 属性集 / 属性表 | property set | Pset |
| 项目基点 / 测量点 / 原点对原点 | project base point / survey point / origin-to-origin linking | Revit locating points |
| 2000坐标 | CGCS2000 national coordinate system | China Geodetic Coordinate System 2000 |
| 乱码 | mojibake | encoding error (`\X2\...\X0\` escapes) |
| 卡 / 卡顿 / 卡死 | laggy / freezing | performance problem |
| 拾取 | picking an object by click | raycast picking |
| 踩坑 | "stepped in a pit" - write-up of a pitfall | lessons learned |
| 导进 / 链进来 | import / link in | Open IFC / Link IFC |
| 丢了 / 丢失 / 变形 / 一片空白 | lost / distorted / blank | missing or deformed elements |
| 信创 / 自主可控 | domestic-IT-stack policy / "self-reliant and controllable" | domestic software requirement |
| 保姆级教程 / 干货 | hand-holding tutorial / substance | step-by-step guide |
| 打脸 | "slap in the face" (clickbait for "the standard says otherwise") | contradicts expectation |
| 宁建模 / EDM / GDB / H-IFC | city-specific review formats (Nanjing, Shanghai, Guangzhou, Hubei) | local review data formats |

### Name variants and misspelling style

- Software names are often lowercase or abbreviated: `revit`, `rvt`, `tekla`, `ifc`, `Su` (SketchUp), `MAX`, `pln` (ArchiCAD file), `BIMSee`/`BIMsee`, `BimBase`/`BIMBase`.
- IFC itself: `IFC`, `ifc`, 工业基础类 (formal, rarely used by askers). The proxy class is nearly always written `proxy` or `IfcBuildingElementProxy` in Latin, not translated as 代理构件.
- Storey: 楼层 (IFC) vs 标高 (Revit Level); askers mix the two.
- Punctuation: half-width commas inside Chinese titles, bracket tags (`【BIM】`, `【模型查看】`, `[Revit]`, `Revit|…`), spaces between CJK and ASCII (`revit 2020 ifc guid不生成是为什么?`) or none (`exportlayers-ifc-IAI`).
- Mapping file names appear raw: `exportlayers-ifc-IAI.txt` (the category-to-IFC-class table) is the thing many askers know by name.

### Code-switching

Narrative stays Chinese; every identifier stays English: class names (`IfcBuildingElementProxy`, `IfcExportAs`), error strings (`Unable to parse .ifc file or no geometrical entities found`), library names, and shorthand like `GUID`, `LOD`, `draw call`, `GLB`, `wasm`. Chinese-speaking GitHub users usually write short, polite English with little context ("which Chinese encoding pattern do you use").

### Tone

Mostly neutral or curious (real records: neutral 74, curious 40, frustrated 16, confused 10, skeptical 6). Frustration is carried by the bare symptom (`没有反应`, `不显示`, `一片空白`) or by exclamation marks in blog titles (`真复杂！`, `！！！`), not by insults. Skepticism shows in `如何评价` / `值不值得` questions about domestic software and xeokit licensing. Vendor posts use superlatives.

### Context given and omitted

| Usually given | Usually omitted |
|---|---|
| Revit year (`revit2019`, `Revit 2020`), the symptom, the city (for 报建), self-check tool version (`1.1.0`, `1.3.0`), file sizes in M/G, pasted error text on developer sites | **IFC version (IFC2x3 or IFC4), MVD/view definition, export settings, the viewer that shows the problem, source software of the IFC, model units, whether the file is linked or opened** |

For test prompts this means: real users rarely say IFC2x3 or IFC4. A model-backed assistant must read `FILE_SCHEMA` itself instead of expecting it in the question.

### What is observed vs assumed about prompts to an AI assistant

No real transcript of a Chinese user prompting an AI assistant about IFC was collected. The Chinese Revit-MCP issues show *tool-requests* (precise, numbered, with mm units), not chat prompts. The `帮我…` openers in the synthetic prompts below are plausible for assistants but are **not observed** data.

## Real questions

Paraphrased or verbatim titles in the original script, with an English gloss, the inferred persona and tone, and the source link. Duplicates (the same URL logged by several cells) are listed once.

### 1. What is IFC, learning and comparison (beginners)

| ID | Original (title; paraphrase where it adds something) | English gloss | Persona · tone | Source |
|---|---|---|---|---|
| `zh-zhihu-r001` | IFC是什么意思? — IFC到底是什么意思，是文件格式还是标准？ | What is IFC / what does IFC mean? | student_beginner · curious | [Zhihu Q&A](https://www.zhihu.com/question/527323998) (qa_site, 2022) |
| `zh-zhihu-r002` | IFC格式是什么？用什么软件可以打开？ — IFC格式是什么，用什么软件可以打开？ | What is the IFC format and what software opens it? | student_beginner · curious | [Zhihu article](https://zhuanlan.zhihu.com/p/2025170865478807871) (blog, 2026) |
| `zh-zhihu-r003` | 如何在线打开IFC格式的文件【BIM】 — 想不装软件在线打开IFC文件 | How to open IFC files online | student_beginner · curious | [Zhihu article](https://zhuanlan.zhihu.com/p/651323857) (blog, 2023) |
| `zh-zhihu-r010` | BIM中RVT格式和IFC格式关系？ — RVT和IFC是什么关系，导出后颜色为什么和rvt不一样 | What is the relationship between RVT and IFC? Colors differ after export. | student_beginner · curious | [Zhihu Q&A](https://www.zhihu.com/question/49455994) (qa_site, 2016) |
| `zh-revit-export-r013` | 一文看懂什么是IFC — IFC是什么，Revit里映射表怎么用 | Article: what is IFC; Revit mapping table is a shareable txt. | student_beginner · curious | [Zhihu article](https://zhuanlan.zhihu.com/p/649792298) (blog, 2023) |
| `zh-lightweight-review-r014` | IFC和BIM协同 — IFC到底是什么，怎么用来协同 | IFC and BIM collaboration: what IFC is and how it supports collaboration. | student_beginner · curious | [Zhihu article](https://zhuanlan.zhihu.com/p/108386827) (blog, 2020) |
| `zh-zhihu-r038` | IFC2x3和IFC4之间的一些主要区别 — IFC2x3和IFC4主要区别 | Main differences between IFC2x3 and IFC4 | developer_programmer · curious | [cnblogs](https://www.cnblogs.com/herd/p/17350345.html) (blog, 2023) |
| `zh-zhihu-r039` | Information Delivery Specification（IDS）：构建行业的信息交流标准 — IDS是什么 | Information Delivery Specification (IDS): building an industry info-exchange standard | bim_manager · curious | [Zhihu article](https://zhuanlan.zhihu.com/p/662463406) (blog, 2023) |
| `zh-csdn-dev-r008` | IFC文件解析 — 一堵墙的IFC文本里，哪些行是构件本身、哪些是连接关系、哪些是属性集；空的$字段应该是描述或类型吧 | Walks through a single IFCWALLSTANDARDCASE in a STEP file: identity/geometry, connections, property sets; guesses at the meaning of empty $ fields. | student_beginner · curious | [cnblogs](https://www.cnblogs.com/pandaNHF/p/16828047.html) (blog, 2022) |
| `p-student-r030` | IFC格式是什么？用什么软件可以打开？ — IFC是什么，有什么用，用哪些软件可以打开IFC文件？ | What is the IFC format and which software opens it? | student_beginner · neutral | [SegmentFault](https://segmentfault.com/a/1190000047698784) (blog, 2026) |
| `zh-tw-hk-r006` | IFC 簡介 (Archicad 29 說明) — IFC是開放中立的資料交換格式，Archicad支援IFC2x3、IFC4、IFC4.3 | Graphisoft Taiwan help page explaining IFC in Traditional Chinese. | student_beginner · neutral | [help.graphisoft.com](https://help.graphisoft.com/AC/29/TAI/_AC29_Help/121_IFC/121_IFC-1.htm) (vendor_kb, 2025) |

### 2. Finding a viewer or tool

| ID | Original (title; paraphrase where it adds something) | English gloss | Persona · tone | Source |
|---|---|---|---|---|
| `zh-zhihu-r004` | 有没有好用、方便的IFC查看工具给推荐一下？ — 求推荐好用方便的IFC查看工具 | Any good, convenient IFC viewer to recommend? | bim_coordinator · curious | [Zhihu Q&A](https://www.zhihu.com/question/583830829) (qa_site, 2023) |
| `zh-zhihu-r030` | BIMsee免费IFC格式浏览器 BIM模型集成浏览、碰撞检查、三维可视化交底 — BIMSee免费IFC浏览器，支持大文件 | BIMSee free IFC browser (IFC2x3, IFC4.x incl. IFC4.2 bridges, IFC4.3 rail) | developer_programmer · curious | [Zhihu article](https://zhuanlan.zhihu.com/p/602546350) (vendor_kb, 2023) |
| `zh-zhihu-r031` | 【模型查看】IFC文件专有轻量化查看平台BIM vision，完全免费！ — BIM vision 免费IFC查看 | BIM Vision: free dedicated IFC viewing platform | student_beginner · curious | [Zhihu article](https://zhuanlan.zhihu.com/p/700041984) (blog, 2024) |
| `zh-zhihu-r032` | 作为国网GIMer：终于找到一款免费能够同时浏览GIM、IFC、Revit的高效合模神器 — 国网GIM、IFC、Revit合模浏览 | As a State Grid GIMer: free tool to view GIM, IFC and Revit together | bim_coordinator · curious | [Zhihu article](https://zhuanlan.zhihu.com/p/634784856) (blog, 2023) |

### 3. Revit to IFC export problems and mapping

| ID | Original (title; paraphrase where it adds something) | English gloss | Persona · tone | Source |
|---|---|---|---|---|
| `zh-zhihu-r005` | revit2019导出IFC文件没有反应？ — revit2019点击导出IFC后没反应，导出位置只有一个schema文档 | Revit 2019 IFC export does nothing; only a schema file appears in the export folder | architect · confused | [Zhihu Q&A](https://www.zhihu.com/question/455661969) (qa_site, 2021) |
| `zh-revit-export-r016` | 如何解决REVIT2020无法导出为IFC文件？ — Revit2020导出IFC选项是灰的 | Revit 2020 cannot export IFC; option greyed out. | bim_coordinator · frustrated | [Zhihu article](https://zhuanlan.zhihu.com/p/611709017) (blog, 2023) |
| `zh-zhihu-r007` | revit 2020 ifc guid不生成是为什么? — Revit2020导出的IFC里GUID没有生成，原因是什么 | Why are IFC GUIDs not generated in a Revit 2020 export? | bim_coordinator · confused | [Zhihu Q&A](https://www.zhihu.com/question/625548241) (qa_site, 2023) |
| `zh-zhihu-r008` | 如何修改revit导出IFC选项？ — 需要导出的构件在exportlayers-ifc-IAI里找不到对应类别，怎么改导出选项 | How to modify Revit IFC export options when a category is missing from exportlayers-ifc-IAI? | bim_coordinator · neutral | [Zhihu Q&A](https://www.zhihu.com/question/418802002) (qa_site, 2020) |
| `zh-revit-export-r007` | Revit 2023 IFC 参数和导出映射对话框 — 介绍Revit 2023里IFC参数和导出映射对话框怎么改导出的实体和预定义类型 | Revit 2023 IFC parameters and export mapping dialog explained. | bim_manager · neutral | [bilibili](https://www.bilibili.com/video/BV1Ba41177xJ/) (video, 2022) |
| `zh-csdn-dev-r007` | revit导出ifc对应类型 — Revit导出IFC时各类别对应哪个IFC类，贴出导出图层/类别映射文件 | Dumps the Revit IFC export category-to-IFC-class mapping table (walls->IfcWall, pipes->IfcPipeSegment, many annotation categories unmapped). | bim_coordinator · neutral | [cnblogs](https://www.cnblogs.com/liaocheng/p/15905467.html) (blog, 2022) |
| `zh-zhihu-r011` | Revit模型按IFC标准导出后会丢失哪些信息？ — Revit导出IFC后会丢哪些信息？ | What information is lost when a Revit model is exported to IFC? | bim_manager · skeptical | [Zhihu Q&A](https://www.zhihu.com/question/264127961) (qa_site, 2018) |
| `zh-csdn-dev-r032` | Revit模型导出时，那些会被弄丢的信息 — Revit导出IFC会丢哪些信息，共享参数、材质、族参数 | What information gets lost when a Revit model is exported to IFC. | bim_coordinator · frustrated | [CSDN blog](https://blog.csdn.net/weixin_39590472/article/details/112503752) (blog, 2021) |
| `zh-lightweight-review-r006` | Revit模型导出时，那些会被弄丢的信息 — Revit导IFC哪些信息会丢，类别对不上IFC类、坐标转换没了 | What information is lost when exporting Revit to IFC (class mapping, predefined type, no IfcMapConversion, proxy fallback). | bim_coordinator · neutral | [CO188 forum](https://bbs.co188.com/thread-10112116-1-1.html) (forum, 2022) |
| `zh-lightweight-review-r007` | 从 Revit 导出的 IFC 文件中缺少图元或钢结构连接 — Revit导出IFC后缺图元和钢结构连接 | IFC exported from Revit is missing elements or steel connections. | bim_coordinator · neutral | [www.autodesk.com.cn](https://www.autodesk.com.cn/support/technical/article/caas/sfdcarticles/sfdcarticles/CHS/Missing-elements-or-steel-connections-in-IFC-file-exported-from-Revit.html) (vendor_kb, 2023) |
| `zh-lightweight-review-r018` | revit导出ifc（1） — revit导出ifc没有东西 | Revit IFC export produces nothing / empty file. | bim_coordinator · frustrated | [CSDN blog](https://blog.csdn.net/d001014/article/details/140438872) (blog, 2024) |
| `zh-revit-export-r014` | Revit 2027重大更新，图形加速器正式发布、欧特克AI来了！ — Revit 2027的IFC导出设置里能直接建自定义属性集了吗 | Revit 2027 adds parameter mapping UI and custom property sets in IFC export settings. | bim_manager · curious | [Zhihu article](https://zhuanlan.zhihu.com/p/2025149945674474186) (blog, 2026) |
| `zh-csdn-dev-r021` | Revit导出IFC格式时中文转码规则 — 导出的IFC里中文变成\X2\...\X0\，是UTF-16十六进制，怎么解回来 | Explains how Revit encodes Chinese in exported IFC as \X2\ hex UTF-16 ... \X0\ escapes. | developer_programmer · neutral | [CSDN blog](https://blog.csdn.net/qq_35042852/article/details/137257689) (blog, 2024) |

### 4. Importing IFC into Revit, base points and coordinates

| ID | Original (title; paraphrase where it adds something) | English gloss | Persona · tone | Source |
|---|---|---|---|---|
| `zh-revit-export-r001` | ifc导入revit后三维不可见 — ifc导入revit之后三维视图里什么都看不到，是哪里的问题 | After importing IFC into Revit nothing shows in 3D view. | architect · frustrated | [Baidu Zhidao](https://zhidao.baidu.com/question/341569640619976845.html) (qa_site, 2025) |
| `zh-revit-export-r002` | IFC格式用什么打开常见问题：Revit打开IFC文件时出现元素丢失或变形，如何解决？ — Revit打开IFC文件后元素丢失或者变形怎么办 | Revit shows missing or distorted elements when opening IFC; how to fix? | bim_coordinator · neutral | [CSDN Q&A](https://ask.csdn.net/questions/8391346) (qa_site, 2025) |
| `zh-revit-export-r003` | Revit在2000坐标下如何精确移动项目基点至0,0,0？ — 模型在2000坐标下，项目基点怎么精确挪到0,0,0 | Project is at 2000 coordinates, how to move Project Base Point precisely to 0,0,0? | bim_coordinator · confused | [CSDN Q&A](https://ask.csdn.net/questions/8816624) (qa_site, 2025) |
| `zh-revit-export-r009` | 如何解决Revit导入IFC文件后不可见 — Revit导入IFC后一片空白怎么办 | How to fix blank view after importing IFC into Revit. | bim_coordinator · neutral | [cnblogs](https://www.cnblogs.com/OverloadBachPunk/p/14452654.html) (blog, 2021) |
| `zh-revit-export-r010` | revit低版本的模型能在高版本打开吗 — 高版本revit的模型低版本打不开，导出ifc行不行 | Can a lower-version Revit open a higher-version model? Export IFC2x3? | bim_coordinator · curious | [Zhulong](https://www.zhulong.com/zt_bim_3002296/detail42826395/) (forum, 2021) |
| `zh-revit-export-r018` | 将IFC链接到Revit的多个图元的错误表示 — 链接IFC进Revit后好几个构件显示不对 | Wrong representation of several elements when linking IFC to Revit. | bim_coordinator · neutral | [Zhihu article](https://zhuanlan.zhihu.com/p/375018823) (blog, 2021) |
| `zh-revit-export-r023` | revit进行群楼建模时（每人分开建），怎么设置测量点和基点，对每栋楼进行定位？求教 — 群楼每人建一栋，测量点基点怎么设才能定位拼起来，求教 | Several people model podium buildings separately; how to set survey/base point to position each building? | bim_coordinator · polite | [Baidu Zhidao](https://zhidao.baidu.com/question/1755259387786621668.html) (qa_site, n.d.) |
| `zh-revit-export-r026` | 终于搞清了Revit的5个定位点都是啥？怎么用？怎么对齐？ — Revit的5个定位点到底啥意思，怎么对齐 | What are Revit's five positioning points and how to align them? | architect · curious | [Zhihu article](https://zhuanlan.zhihu.com/p/535737725) (blog, 2022) |
| `zh-zhihu-r009` | 关于tekla导出ifc到revit,3D视图不显示的问题？ — tekla导出ifc到revit后3D视图里看不到模型 | Tekla-exported IFC loaded in Revit shows nothing in the 3D view | structural_engineer · confused | [Zhihu Q&A](https://www.zhihu.com/question/60173683) (qa_site, 2017) |
| `zh-zhihu-r035` | 将IFC模型转换为Revit模型后减肥 — IFC转Revit模型后体积暴涨怎么减肥 | IFC converted to Revit bloats (151MB Tekla IFC becomes 2GB); how to slim down | structural_engineer · frustrated | [CSDN blog](https://blog.csdn.net/zzutt/article/details/121492254) (blog, 2021) |
| `zh-tw-hk-r001` | [IFC]REVIT匯入IFC時需注意的事項 — 把REVIT、ARCHICAD、TEKLA匯出的IFC再匯入REVIT，平面看得到物件，3D卻找不到 | After importing IFC from Revit/ArchiCAD back into Revit, objects show in plan but not in 3D. | bim_coordinator · neutral | [housegear.pixnet.net](https://housegear.pixnet.net/blog/posts/3042268210) (blog, 2013) |

### 5. Moving models between tools (materials, structure, cost software)

| ID | Original (title; paraphrase where it adds something) | English gloss | Persona · tone | Source |
|---|---|---|---|---|
| `zh-revit-export-r004` | MAX模型导入REVIT时材质丢失如何解决？ — MAX模型导进Revit材质全没了 | Materials lost when importing a Max model into Revit. | architect · frustrated | [CSDN Q&A](https://ask.csdn.net/questions/8796533) (qa_site, 2025) |
| `zh-revit-export-r005` | 怎样将archicad（pln）文件导入revit — archicad的pln文件怎么弄进revit | How to bring an ArchiCAD pln file into Revit? | architect · neutral | [Baidu Zhidao](https://zhidao.baidu.com/question/593298625.html) (qa_site, n.d.) |
| `zh-revit-export-r006` | Revit转fbx丢失材质问题解决方案探索 — Revit转fbx材质丢失，试过各种办法 | Revit export to FBX loses materials; solution exploration. | architect · frustrated | [bilibili](https://www.bilibili.com/read/cv18398331/) (blog, 2022) |
| `zh-revit-export-r020` | Su 导入 Revit 材质总是丢失怎么办？ — Su导进Revit材质总是丢 | SketchUp import to Revit always loses materials. | architect · frustrated | [Zhihu article](https://zhuanlan.zhihu.com/p/372183287) (blog, 2021) |
| `zh-zhihu-r045` | Tekla 与 Revit 模型的相互转换如何实现？ — Tekla和Revit互转 | How to convert between Tekla and Revit models? | structural_engineer · curious | [Zhihu Q&A](https://www.zhihu.com/question/30485422) (qa_site, 2016) |
| `zh-revit-export-r011` | revit插件 ——BIM5D — revit模型怎么导进广联达BIM5D，插件和IFC哪个好 | Revit plugin for exporting to Glodon BIM5D, richer than IFC. | contractor_site · neutral | [Zhulong forum](https://bbs.zhulong.com/106010_group_3002227/detail33178172/) (forum, n.d.) |
| `zh-revit-export-r012` | Revit机电专业IFC导入BIM5D操作过程 — 机电模型从Revit出IFC再导进BIM5D的步骤 | Process of exporting Revit MEP model as IFC and importing into BIM5D. | mep_engineer · neutral | [Zhulong](https://www.zhulong.com/zt_bim_3002296/detail40283815/) (forum, 2022) |
| `zh-tw-hk-r010` | BIM模型於結構分析軟體之資料傳遞研究（臺大碩士論文） — Revit傳到Robot/ETABS/SAP2000，IFC方式資料遺失或更動，原生檔與API較佳 | NTU thesis: IFC transfer from Revit to ETABS/SAP2000/Robot lost or changed data; native and API better. | structural_engineer · neutral | [tdr.lib.ntu.edu.tw](https://tdr.lib.ntu.edu.tw/handle/123456789/90111) (paper, 2022) |

### 6. Local submission and review (报建/报审/送審), Mainland, Hong Kong, Taiwan

| ID | Original (title; paraphrase where it adds something) | English gloss | Persona · tone | Source |
|---|---|---|---|---|
| `zh-lightweight-review-r001` | Revit二次开发——SZ-IFC — 想用Revit二次开发做SZ-IFC导出，要怎么实现，坑在哪 | How to do Revit add-in development to export SZ-IFC (Shenzhen BIM filing format)? | developer_programmer · neutral | [Zhihu article](https://zhuanlan.zhihu.com/p/673078056) (blog, 2023) |
| `zh-lightweight-review-r002` | BIM报批报建之Revit端自检工具 — 报建前能不能在Revit里先自检，不用每次导出IFC再检测 | Pre-check the model inside Revit before exporting SZ-IFC for Shenzhen filing. | bim_coordinator · neutral | [Zhihu article](https://zhuanlan.zhihu.com/p/633827596) (blog, 2023) |
| `zh-lightweight-review-r004` | 深圳BIM报建常见问题解析 — 自检工具里审查节点有些值是空的，导出IFC丢字段了怎么办 | Some review node values are empty in the self-check tool, meaning fields were lost during IFC export. | bim_coordinator · frustrated | [CSDN blog](https://blog.csdn.net/weixin_42855822/article/details/139867051) (blog, 2024) |
| `zh-lightweight-review-r005` | BIM 报建工具与 IFC 标准研究 — SZ-IFC转换和自检遇到构件偏移、信息缺失、文件大、各软件读取不一致、转换慢 | Notes from a product manager on SZ-IFC: offsets, missing info, big files, viewer differences, slow conversion, coordinate rules. | developer_programmer · curious | [www.sunyuanrui.com](https://www.sunyuanrui.com/works/sz-ifc-research/) (blog, 2026) |
| `zh-lightweight-review-r019` | 广州市规划和自然资源局关于试行建筑工程三维（BIM）规划电子报批辅助审查工作的通知 — 哪些项目要同步提交BIM模型做规划报批 | Guangzhou trial of BIM electronic planning approval: submit BIM model with planning technical review for gov projects over 20,000 m2, prefab, key zones, from 2020-10-01. | reviewer_authority · neutral | [www.gz.gov.cn](https://www.gz.gov.cn/xw/tzgg/content/post_6469259.html) (regulation, 2020) |
| `zh-lightweight-review-r020` | 广州市住房和城乡建设局关于试行开展房屋建筑工程施工图三维（BIM）电子辅助审查工作的通知 — 施工图审查要同时上传二维图纸和BIM模型吗 | Guangzhou trial of BIM-assisted construction drawing review: upload 2D drawings and BIM model together; owner confirms consistency. | reviewer_authority · neutral | [zfcj.gz.gov.cn](https://zfcj.gz.gov.cn/gkmlpt/content/6/6434/post_6434530.html) (regulation, 2020) |
| `zh-lightweight-review-r021` | 技术｜干货满满，设计师聊广州市BIM审查 — 设计师聊广州BIM审查，导GDB、改模型再导第二版 | Designers share what Guangzhou BIM review is like: export per-discipline GDB, expert comments, revise model, re-export version two. | architect · curious | [Zhihu article](https://zhuanlan.zhihu.com/p/504617257) (blog, 2022) |
| `zh-lightweight-review-r023` | 2025 广州市自主可控BIM应用与发展白皮书 — 自主可控BIM，审图后模型汇入CIM平台，图模对位不合格传不上去 | Guangzhou 2025 white paper on autonomous and controllable BIM: models flow into the CIM platform after review; drawing-model alignment check since 2023. | reviewer_authority · neutral | [zfcj.gz.gov.cn](https://zfcj.gz.gov.cn/attachment/7/7943/7943479/10589336.pdf) (official_doc, 2025) |
| `zh-lightweight-review-r024` | 《关于加快推进我市建筑信息模型（BIM）技术应用的通知》解读 — 南京BIM规划报建要交原生模型和宁建模轻量化文件吗 | Nanjing BIM planning submission: from 2021-03-01 in pilot zones, projects submit native BIM plus lightweight 宁建模 file after QC; free aided-design software. | reviewer_authority · neutral | [ghj.nanjing.gov.cn](http://ghj.nanjing.gov.cn/njsgtzyj/202103/t20210301_2834720.html) (official_doc, 2021) |
| `zh-lightweight-review-r025` | 建筑工程竣工信息模型交付规范 DB 3201/T 1145—2023 — 竣工模型交付用什么格式，要在施工图模型基础上加变更信息吗 | Nanjing local standard for as-built (completion) BIM delivery; format preferably 宁建模. | owner_client · neutral | [amr.nanjing.gov.cn](https://amr.nanjing.gov.cn/ztzl/bzhzl/tzgg/202302/P020230216538033075572.pdf) (regulation, 2023) |
| `zh-lightweight-review-r026` | 上海市工程建设项目BIM智能辅助审查建模手册 V1.0 — 上海审查用EDM还是IFC | Shanghai BIM smart-review modeling manual: EDM data file for architecture/MEP review, IFC for structural load review. | reviewer_authority · neutral | [zjw.sh.gov.cn](https://zjw.sh.gov.cn/cmsres/4a/4a7bc95634cd4852b2399e57e9c692dd/a646541bab5ad86dc1684d1126e21e29.pdf) (regulation, 2023) |
| `zh-lightweight-review-r027` | 深圳BIM存储标准 SZ-IFC (SJG114-2022) — 深圳哪些项目要用SZ-IFC报建，几个阶段提交 | Shenzhen SJG114-2022 SZ-IFC: projects over 10M yuan and 1,000 m2 must apply BIM from 2023; models submitted at planning, construction permit, completion. | reviewer_authority · neutral | [zjj.sz.gov.cn](https://zjj.sz.gov.cn/attachment/0/678/678888/7768421.pdf) (regulation, 2023) |
| `zh-lightweight-review-r030` | 湖北省工程建设BIM云平台 H-IFC — 湖北H-IFC数据规范是什么 | Hubei province BIM cloud platform (June 2026) with H-IFC localized data specification across planning to archiving. | reviewer_authority · neutral | [www.ctdsb.net](https://www.ctdsb.net/c1676_202606/2785613.html) (social, 2026) |
| `zh-zhihu-r024` | 上海住建委：2024年2月1日起，对房屋建筑工程试行BIM智能辅助审查 — 上海试行BIM智能辅助审查，设计单位要导出什么格式 | Shanghai from 2024-02-01 trials BIM-assisted review (EDM format; IFC to be explored) | reviewer_authority · neutral | [Zhihu article](https://zhuanlan.zhihu.com/p/676069996) (regulation, 2024) |
| `zh-tw-hk-r002` | 建築信息模擬技術 - 屋宇署 BIM自動核查工具 — 屋宇署：呈交的建築信息模型屬補充資料僅供參考，圖則與模型不一致以圖則為準；提供Revit/ArchiCAD外掛核查樓面面積、衞生設備、消防 | HK Buildings Department: submitted BIM models are supplementary only; drawings prevail; plug-ins check GFA, sanitary, fire safety; Revit IFC export text file provided. | reviewer_authority · neutral | [www.bd.gov.hk](https://www.bd.gov.hk/tc/resources/online-tools/building-information-modelling/index.html) (official_doc, 2025) |
| `zh-tw-hk-r003` | 採用BIM擬備和呈交建築圖則的路線圖 — 政府2023年12月公布全面採用BIM擬備及審批建築圖則路線圖，暫定2029年強制呈交 | HK roadmap for adopting BIM in building plan preparation and submission; mandatory BIM submission tentatively 2029. | owner_client · neutral | [www.devb.gov.hk](https://www.devb.gov.hk/filemanager/tc/content_2373/BIM-Book-content-cn.pdf) (regulation, 2023) |
| `zh-tw-hk-r007` | 使照竣工模型上繳操作手冊 — 使照竣工模型上繳：在系統BIM模型頁選擇上傳IFC檔，上傳完成後啟動模型轉檔 | Taipei building administration manual: upload as-built (use permit) BIM model as IFC then trigger model conversion. | reviewer_authority · neutral | [dbadgp.gov.taipei](https://dbadgp.gov.taipei/DownFiles/Login/使照竣工模型上繳操作手冊.pdf) (official_doc, 2023) |
| `zh-tw-hk-r009` | 新北市建照電腦輔助查核與Revit模型IFC匯出研究 — 新北市建照查核系統，團隊須將BIM模型IFC檔上傳，依建築技術規則定義元件參數 | Thesis: New Taipei permit rule-check system requires submitting IFC from Revit model with parameters defined by Taiwan building technical regulations. | researcher_academic · neutral | [etheses.lib.ntust.edu.tw](https://etheses.lib.ntust.edu.tw/thesis/detail/2e82ca6d84bfe5f839f58b35029a1d54) (paper, 2020) |

### 7. Web, 轻量化, glTF and big models

| ID | Original (title; paraphrase where it adds something) | English gloss | Persona · tone | Source |
|---|---|---|---|---|
| `zh-csdn-dev-r001` | 大型 BIM 模型在 Web 端为什么这么卡？一次引擎选型与技术复盘 — 模型能导出、能加载、能显示，不等于能在浏览器里高效跑；解析阻塞主线程、draw call 太多、拾取/隐藏/属性查询变慢，合并几何又丢构件语义 | Large Revit/BIM models are extremely laggy in the browser; exporting to FBX/GLB works but does not scale, so a dedicated lightweight engine was bought. | developer_programmer · frustrated | [Juejin](https://juejin.cn/post/7698926562423357450) (blog, 2026) |
| `zh-csdn-dev-r002` | AI 驱动三维大屏的端到端工程化：从 Revit/IFC 到 Three.js 的落地实践 — IfcConvert 会合并构件、丢 expressID，要额外写入 GlobalId 才能和属性表关联；材质全变灰；毫米和米单位导致放大1000倍；IFC原点和项目基点不一致 | End-to-end pipeline Revit IFC -> glTF + metadata.json for a Three.js 3D dashboard; lists pitfalls: lost expressID, grey materials, mm vs m scale x1000, origin offset, sl… | developer_programmer · neutral | [Juejin](https://juejin.cn/post/7691297274821705728) (blog, 2026) |
| `zh-csdn-dev-r003` | 将IFC转换成GLTF格式 — 先用IfcConvert把ifc转成dae，再用COLLADA2GLTF转gltf，在xeogl里打开；路径里有中文好像会失败，所以进工具目录里执行 | Converting Revit IFC to DAE with IfcConvert and then to glTF with COLLADA2GLTF to view in xeogl; suspects Chinese characters in the path break the command. | student_beginner · neutral | [cnblogs](https://www.cnblogs.com/LeeSki/p/14293418.html) (blog, 2021) |
| `zh-csdn-dev-r004` | BIM轻量化之路（一） — 模型导进Unity后管道材质变灰；超过100M的模型就卡死；WebGL三角面多了内存爆；BIMserver的viewer功能太少，xeokit要收费，xeogl文档又少 | Surveys how to make Revit models light enough for web/Unity: FBX, IFC, OBJ, glTF; materials turn grey in Unity, >100MB freezes, WebGL runs out of memory, xeokit licence… | developer_programmer · frustrated | [cnblogs](https://www.cnblogs.com/nihaozhe/articles/13651935.html) (blog, 2020) |
| `zh-lightweight-review-r010` | BIM轻量化之路（一）-unity展示 — 100M的模型导出IFC有1GB，转OBJ变3GB，机器卡死 | BIM lightweighting path (1): showing Revit models in Unity, with exporting FBX; 100MB model becomes 1GB IFC then 3GB OBJ. | developer_programmer · frustrated | [CSDN blog](https://blog.csdn.net/nihaozhe/article/details/108704151) (blog, 2020) |
| `zh-lightweight-review-r016` | IFC模型轻量化，数据结构化 — Tekla、Revit加载慢，IFC里筛构件、出材料清单、找小零件都难 | Heavy desktop BIM tools load slowly for steel projects with thousands of parts; need a web viewer that filters components and extracts material lists from IFC. | bim_manager · frustrated | [cnblogs](https://www.cnblogs.com/lingyanspace/p/19739094) (blog, 2026) |
| `zh-zhihu-r019` | bim轻量化的原理是什么？ — BIM轻量化的原理是什么 | What is the principle behind BIM lightweighting? | developer_programmer · curious | [Zhihu Q&A](https://www.zhihu.com/question/385964946) (qa_site, 2020) |
| `zh-zhihu-r020` | Xeokit 优缺点 — xeokit优缺点，值不值得商用 | Pros and cons of xeokit (conflicting license claims reported) | developer_programmer · skeptical | [Zhihu article](https://zhuanlan.zhihu.com/p/408412116) (blog, 2021) |

### 8. Developers: parsing IFC, Chinese text, library errors

| ID | Original (title; paraphrase where it adds something) | English gloss | Persona · tone | Source |
|---|---|---|---|---|
| `zh-csdn-dev-r005` | xBIM 实战01 在浏览器中加载IFC模型文件 — 要在网页里看IFC，得先用IfcStore打开，Xbim3DModelContext生成几何，SaveAsWexBim；web.config要加.wexbim的MIME，请求大小调到100MB | Load an IFC model in the browser with xBIM WebUI: set up ASP.NET project, MIME type for .wexbim, convert IFC to wexbim via IfcStore + Xbim3DModelContext. | developer_programmer · neutral | [cnblogs](https://www.cnblogs.com/SavionZhang/p/10984048.html) (blog, 2019) |
| `zh-csdn-dev-r006` | 修改IFC对象属性并写入IFC文件 — 读入IFC文件，按GlobalID找到梁，改名字，加属性集，再写出新文件 | Modify an IfcBeam's name and add a property set by looking it up via GlobalId in Java and writing a new IFC file. | developer_programmer · neutral | [cnblogs](https://www.cnblogs.com/herd/p/12183392.html) (blog, 2020) |
| `zh-csdn-dev-r012` | xBIM 基础16 IFC的空间层次结构 — 从IfcProject开始递归，IsDecomposedBy走聚合，ContainsElements拿楼层里的墙门窗 | Print the project/site/building/storey/space hierarchy recursively with xBIM, using IsDecomposedBy and ContainsElements. | developer_programmer · neutral | [cnblogs](https://www.cnblogs.com/SavionZhang/p/10983394.html) (blog, 2019) |
| `zh-csdn-dev-r013` | Chinese encode in IFC | Asks which Chinese encoding IfcOpenShell uses when generating IFC; UTF-8 still gives mojibake. | developer_programmer · polite | [GitHub](https://github.com/IfcOpenShell/IfcOpenShell/issues/571) (github_issue, 2019) |
| `zh-csdn-dev-r014` | [Bug]: The GetLine() API method has an error in parsing Chinese — IFCPROPERTYSINGLEVALUE里的\X2\...\X0\小写十六进制，GetLine读出来是错的，改成大写就对 | GetLine() returns wrong Chinese text for \X2\7d20586b571f\X0\ lowercase hex; uppercase hex decodes correctly; a commenter pinpoints missing a-f in getNextHex. | developer_programmer · neutral | [GitHub](https://github.com/ThatOpen/engine_web-ifc/issues/949) (github_issue, 2024) |
| `zh-csdn-dev-r015` | Wrong string value parsed from the file — ifcxml里Name含中文或西里尔字符，读出来被截断，非拉丁字符成了字符串起点 | Strings with Chinese/Cyrillic characters get truncated when reading an ifcXML file with IfcOpenShell. | developer_programmer · confused | [GitHub](https://github.com/IfcOpenShell/IfcOpenShell/issues/3499) (github_issue, 2023) |
| `zh-csdn-dev-r022` | react项目使用web-ifc-three、web-ifc导入ifc文件 — npm装的web-ifc-three运行报WebAssembly LinkError (Import function not callable)，最后自己编译web-ifc替换node_modules并给nginx配wasm MIME | React project with web-ifc-three throws WebAssembly LinkError; fixed by building web-ifc from source, copying the wasm, and serving .wasm with application/wasm in nginx. | developer_programmer · frustrated | [CSDN blog](https://blog.csdn.net/pumbkin/article/details/141029954) (blog, 2024) |
| `zh-zhihu-r013` | BIM学习心得20—使用Python解析IFC文件（一） — 用Python解析IFC文件读取构件 | BIM learning notes 20: parsing IFC files with Python (part 1) | developer_programmer · curious | [Zhihu article](https://zhuanlan.zhihu.com/p/101268159) (blog, 2019) |
| `zh-zhihu-r017` | xBIM IFC 输出 Excel 报表 — 用xBIM遍历IFC空间写入Excel，面积体积优先取Quantity | xBIM: output IFC space data to an Excel report | developer_programmer · neutral | [cnblogs](https://www.cnblogs.com/w2011/p/8424405.html) (blog, 2018) |

### 9. Choosing domestic (国产) BIM software

| ID | Original (title; paraphrase where it adds something) | English gloss | Persona · tone | Source |
|---|---|---|---|---|
| `zh-zhihu-r026` | EasyBIM 2026大更新：国产BIM软件的下一站，远远不只出图 — EasyBIM内置四地IFC审查要求并一键生成轻量化IFC | EasyBIM 2026 update: built-in IFC review rules for Chengdu, Shenzhen, Shanghai, Wuhan; one-click lightweight IFC | bim_manager · curious | [Zhihu article](https://zhuanlan.zhihu.com/p/2053415784773313709) (vendor_kb, 2026) |
| `zh-zhihu-r027` | 如何评价广联达数维建筑和构力BimBase两款国产BIM软件？ — 如何评价广联达数维建筑和构力BimBase | How to evaluate Glodon Shuwei vs PKPM BIMBase domestic BIM software? | bim_manager · skeptical | [Zhihu Q&A](https://www.zhihu.com/question/642487361) (qa_site, 2024) |
| `zh-zhihu-r028` | 如何中肯的评价构力科技的BIMBase平台和广联达的BIMMAKE平台？谁更具有发展优势？ — 构力BIMBase和广联达BIMMAKE谁更有发展优势 | Fair evaluation of BIMBase platform vs Glodon BIMMAKE: who has the advantage? | bim_manager · skeptical | [Zhihu Q&A](https://www.zhihu.com/question/458311613) (qa_site, 2021) |
| `zh-zhihu-r029` | 2026再看BIM软件国产化：算量、设计、AI，数维走到哪一步了？ — 国产BIM软件现状 | 2026 look at domestic BIM software: how far has Shuwei got | bim_manager · curious | [Zhihu article](https://zhuanlan.zhihu.com/p/2042916697968007094) (blog, 2026) |

### 10. AI, LLM and MCP with Revit

| ID | Original (title; paraphrase where it adds something) | English gloss | Persona · tone | Source |
|---|---|---|---|---|
| `zh-aimcp-r010` | [提案] 強化 create_wall 的樓層與牆型選擇，避免任意使用第一個樓層 — AI 建牆時沒有樓層參數就取 FirstOrDefault Level，牆建到非預期樓層、無法指定牆型 | create_wall silently uses the first Level in the project and Z=0; propose explicit level and wall type parameters. | bim_coordinator · neutral | [GitHub](https://github.com/shuotao/REVIT_MCP_study/issues/144) (github_issue, 2026) |
| `zh-aimcp-r011` | [提案] preview_dwg_beams 加 includeGeometry 參數 — 預覽只回傳數量與前5筆寬度，沒有座標，AI 無法把 CAD 牆圖層翻成 Revit 牆 | Asks preview_dwg_beams to return centerline coordinates so the AI can turn CAD wall layers into Revit walls. | bim_coordinator · neutral | [GitHub](https://github.com/shuotao/REVIT_MCP_study/issues/150) (github_issue, 2026) |
| `zh-aimcp-r023` | 世界发展真快 马上二开要失业了 — 二开 (secondary development) will be unemployed soon | World moves fast; worried that Revit plugin developers will lose their jobs to MCP. | developer_programmer · curious | [GitHub](https://github.com/mcp-servers-for-revit/revit-mcp-plugin/issues/11) (github_issue, 2025) |
| `zh-aimcp-r024` | 如何和cursor对接 | How to connect this Revit MCP to Cursor? | student_beginner · neutral | [GitHub](https://github.com/ZedMoster/revit-mcp/issues/1) (github_issue, 2025) |
| `zh-aimcp-r033` | Yang-Agent_Revit — 面向 Revit 使用者、BIM 团队、插件开发者 | Wants AI to export model health, preview then apply missing door/window marks, find duplicate room numbers and unplaced views, always with preview, confirm, apply, log,… | bim_manager · neutral | [GitHub](https://github.com/5788324/Yang-Agent_Revit) (official_doc, 2026) |
| `zh-aimcp-r045` | REVIT_MCP_study README — 切換/釋放連線; MCP 設定 | Prompts like dimension every wall and check curtain-wall elevations; troubleshooting list: port 8964, HTTP.sys PID 4, one AI client at a time, browser Origin blocked. | bim_coordinator · neutral | [GitHub](https://github.com/shuotao/REVIT_MCP_study) (official_doc, 2026) |
| `zh-revit-auto-r026` | [提案] 將 SC REVIT 的開孔定位流程整理成 AI 可用工具 — 機電管線穿過牆、樓板或樑時要逐筆確認穿透位置與開孔大小;希望AI能指定MEP/結構在主模型或連結模型、預留量、樓層與品類,回傳候選清單 | Turn the manual MEP-penetration opening-locating workflow into AI-callable tools that scan pipes crossing walls/floors/beams and propose opening sizes | mep_engineer · neutral | [GitHub](https://github.com/shuotao/REVIT_MCP_study/issues/99) (github_issue, 2026) |
| `zh-zhihu-r041` | 让 AI 直接建模型：这个开源项目把 Revit 接进了大模型，26 个工具管到底 — Revit接大模型MCP开源项目 | Let AI build models: open-source project connecting Revit to LLMs with 26 tools | developer_programmer · curious | [Zhihu article](https://zhuanlan.zhihu.com/p/2081844898991444652) (blog, 2026) |
| `zh-zhihu-r042` | AI 到底能不能看懂图纸、建BIM模型？小孩没娘，说来话长 — AI能不能看懂图纸建BIM模型 | Can AI really read drawings and build BIM models? (long story) | researcher_academic · skeptical | [Zhihu article](https://zhuanlan.zhihu.com/p/2097988751914022344) (blog, 2026) |

*Real questions listed: 95 distinct pages.*

## Ready test prompts

All prompts in this section are **synthetic**: they were written (or rewritten) to sound like the people above, they are not quotes. IDs of the form `zh-...-sNNN` come from the research cells; IDs starting `ZH-X` are new rewrites for this file. Every prompt marked "needs model" assumes an IFC or Revit model is loaded in the MCP server. "Expected behavior" is what a good assistant should do; for review-related prompts it must **never claim official acceptance** (the real Shenzhen self-check tool, Guangzhou GDB export or Hong Kong BD checker cannot be run by the assistant).

Language mix: Simplified, Traditional (marked TC), and Mainland/Taiwan/HK vocabulary. Difficulty is as set by the research cells.

### A. Export mapping, properties and other 'where did it go' checks

| ID | Prompt (synthetic) | Intent · difficulty · file | Expected behavior (EN) |
|---|---|---|---|
| `zh-zhihu-s001` | 这个ifc里有多少IfcBuildingElementProxy？按revit类别分一下，我要改导出映射<br>*EN: Count proxies and list their source categories* | query_model_data · medium · needs model | Count IfcBuildingElementProxy, group by Revit category/ObjectType property, report counts and suggest mapping fixes. |
| `zh-proxy-s014` | 类别映射表和族类型上的 IfcExportAs 哪个优先?我设了两个不一样,导出还是proxy<br>*EN: Difference between category mapping and per-type IfcExportAs* | understand_concept · easy · needs model | Explain priority: type/instance override over category mapping; check subcategory and built-in param; diagnose. |
| `zh-psets-s016` | 导出的ifc里我自己加的共享参数属性集没了，帮我查下哪些构件有这个属性集<br>*EN: Which elements lack the custom property set exported from Revit shared parameters* | query_model_data · medium · needs model | List elements carrying the custom pset by name and those missing it, grouped by class. |
| `zh-revit-export-s003` | 我们自己的共享参数导出后没了，看看墙的Pset里有没有'构件编码'这个属性<br>*EN: Which custom shared parameters are missing as properties* | validate_check · medium · needs model | List Psets on IfcWall, check for the custom property, report elements missing it and note the export option 'Export Revit property sets'. |
| `zh-revit-export-s008` | 把所有名字带'柱'的代理构件改成IfcColumn，别的不要动<br>*EN: Reclassify generic items as columns* | modify_model_data · hard · needs model | Find IfcBuildingElementProxy with name containing 柱, change class to IfcColumn, preview list before writing, save a copy. |
| `zh-revit-export-s004` | 帮我找出没有材质的构件，按楼层列出来<br>*EN: Which elements have no material* | query_model_data · medium · needs model | Traverse IfcRelAssociatesMaterial, list products lacking material grouped by IfcBuildingStorey. |
| `mx-mcl-s003` | 帮我查下这个IFC里墙的材质层有没有丢，是IfcMaterialLayerSetUsage还是只剩一个IfcMaterial<br>*EN: Check whether layer sets are preserved on walls* | validate_check · medium · needs model | For each IfcWall report material association type (LayerSetUsage, ConstituentSet, single IfcMaterial), count each and list walls reduced to single material. |
| `zh-struct-s009` | revit导出ifc钢结构节点螺栓全没了，勾了包含钢构件也不行，咋回事<br>*EN: Revit steel connections and bolts missing from IFC export* | troubleshoot_export · medium · no file | Explain Include Steel Elements/Connections options and known exporter regressions; check IFC for IfcMechanicalFastener/IfcPlate counts. |
| `zh-mep-s008` | revit导出ifc后管道颜色都是灰的，系统颜色没带出来，用的哪个设置？<br>*EN: MEP colours lost in IFC* | troubleshoot_export · medium · no file | Explain colour derives from materials/by-category, not view filters; guide setting system material and checking IfcStyledItem. |

### B. Coordinates, versions, GUID and comparison

| ID | Prompt (synthetic) | Intent · difficulty · file | Expected behavior (EN) |
|---|---|---|---|
| `mul-coord-s009` | 这个ifc模型离原点特别远，看看有没有坐标系和EPSG，是不是用的CGCS2000<br>*EN: Check whether IFC has a coordinate system and EPSG; model is far from origin* | validate_check · medium · needs model | Read IfcProjectedCRS name/EPSG, MapConversion, report distance from origin and whether CGCS2000 is declared. |
| `mul-coord-s010` | revit导出ifc到navisworks位置不对，共享坐标咋设置，基点测量点搞不清<br>*EN: Exported IFC lands at wrong place in Navisworks* | troubleshoot_export · medium · no file | Explain acquiring shared coordinates, choosing Shared Coordinates in export, differences of PBP/survey point. |
| `zh-revit-export-s002` | 导进revit啥都看不到，帮我查下这个ifc的坐标是不是离原点太远了<br>*EN: Check whether model is far from origin* | validate_check · medium · needs model | Read IfcSite/IfcMapConversion/placements, compute bounding box and distance to origin, flag >10km, suggest recentering. |
| `zh-zhihu-s007` | 结构ifc和建筑ifc合不上，差了好远，对比下两个文件的原点和基点<br>*EN: Compare placement/origin of two IFCs* | coordinate_clash · hard · needs model | Compare IfcSite RefLatitude/Elevation, IfcMapConversion, placements and units, report offset and likely cause. |
| `zh-guid-s007` | 两次导出的IFC，GUID全不一样，帮我按类型和坐标匹配一下，看看到底哪些构件真的改了<br>*EN: Every export has different GUIDs; find which elements have really changed* | compare_versions · hard · needs model | Detect GUID mismatch, pair elements by class, name and placement, list truly modified, added and removed elements. |
| `zh-vm-s006` | 这个IFC4的模型能不能转成IFC2x3？帮我看看会丢哪些东西<br>*EN: Downgrade IFC4 to IFC2x3 and report losses* | convert_format · hard · needs model | Check schema, entities not in 2x3 (e.g. PolygonalFaceSet, constituent sets), perform/describe conversion and list losses. |
| `zh-vm-s007` | 甲方要求交付IFC2x3，帮我检查一下这个文件的版本和视图定义对不对<br>*EN: Verify file delivered satisfies required IFC2x3* | validate_check · easy · needs model | Read FILE_SCHEMA and ViewDefinition, confirm IFC2X3 and CoordinationView 2.0, list deviations. |
| `zh-revit-export-s017` | 对方revit版本低，我导ifc给他行吗，选2x3还是4<br>*EN: Send model to old-version Revit user via IFC* | convert_format · easy · no file | Recommend IFC2x3 Coordination View 2.0 for compatibility, note losses (phases, parameters). |

### C. Local review, permit and classification (Shenzhen, Guangzhou, code checks)

| ID | Prompt (synthetic) | Intent · difficulty · file | Expected behavior (EN) |
|---|---|---|---|
| `zh-lightweight-review-s001` | 这个ifc报建自检能过吗？先看下项目基点坐标是不是2000的，还有哪些构件属性是空的<br>*EN: Check whether this IFC will pass the Shenzhen self-check: coordinates, empty fields.* | validate_check · hard · needs model | Read IfcSite/map conversion and placement, check coordinate range and CRS, list elements with empty required properties; state limits since the official checker cannot be run. **Note:** The assistant cannot run the official local checker and must not say the file 'passes' review. |
| `zh-revit-export-s007` | 深圳报建要审项目基点坐标和到正北的角度，看下这个ifc里这几个值有没有，是不是空的<br>*EN: Check project base point values for Shenzhen submission* | validate_check · hard · needs model | Read IfcProject/IfcSite placement, true north, elevation properties; report presence and values, flag empty fields. **Note:** The assistant cannot run the official local checker and must not say the file 'passes' review. |
| `zh-lightweight-review-s015` | SZ-IFC跟CN-IFC、普通IFC有啥区别？报建只能用SZ-IFC吗<br>*EN: Difference between SZ-IFC, CN-IFC and standard IFC4.* | understand_concept · easy · no file | Explain local profile vs translated standard vs ISO IFC; Shenzhen requires its conversion plugin and checker; verify with official docs. |
| `zh-permit-s008` | 帮我审一下这个ifc模型，疏散门宽度有没有小于0.9米的，列出楼层和编号<br>*EN: Check evacuation door widths* | validate_check · medium · needs model | Find IfcDoor on evacuation routes, read width, list those below 0.9 m with storey and tag. |
| `zh-permit-s009` | 报建用的模型导出IFC要注意什么？构件编码和属性怎么挂才能被智能审查识别<br>*EN: How to prepare a model for automated review* | understand_concept · medium · no file | Explain classification codes, property mapping, export settings; say specifics depend on local review platform. |
| `zh-lightweight-review-s007` | 核一下建筑面积和层高跟图纸报的数对不对，差多少<br>*EN: Check building area and floor height against drawing figures.* | validate_check · hard · needs model | Compute slab/space areas and storey heights from the model, compare to given values, report deviations and uncertainties. |
| `zh-lightweight-review-s018` | 每次改一点点就得重新导ifc再自检，转换慢得要死，有没有办法只导改动的？<br>*EN: Complaint about converter slowness and repeated review rounds.* | complain_vent · easy · no file | Explain incremental export is not generally supported; suggest worksets/scope export and pre-checks. |
| `zh-classbsdd-s009` | 按GB/T 51269分类编码把构件分组，统计墙和板的体积<br>*EN: Group quantities by GB/T 51269 code.* | extract_quantities · medium · needs model | Group elements by classification code from GB/T 51269 reference, sum volumes from Qto sets. **Note:** The GB/T 51269 code table is not verified in this KB: a good answer groups by whatever classification the file actually carries (or asks for the mapping table) and does not invent codes. |
| `zh-classbsdd-s010` | revit导出ifc怎么把自己的分类编码带出去？ 用的是国标那个<br>*EN: How to export Chinese classification codes into IFC.* | how_to · easy · no file | Explain ClassificationCode parameter or classification settings, mapping to IfcClassificationReference. |

### D. Quantities, rooms, cost and handover

| ID | Prompt (synthetic) | Intent · difficulty · file | Expected behavior (EN) |
|---|---|---|---|
| `zh-s011` | 帮我按楼层统计混凝土柱和梁的体积，导出表格，缺工程量的构件单独列出来<br>*EN: Count columns and beams volume by floor for quantity takeoff.* | extract_quantities · medium · needs model | Group columns and beams by storey, sum volumes, export table and list elements lacking quantity data. |
| `zh-csdn-dev-s007` | 各楼层楼板和墙的体积汇总一下，用Qto里的NetVolume，没有的话用几何算，两个对一下<br>*EN: Sum slab and wall volume by storey, check against Qto* | extract_quantities · hard · needs model | Read Qto_*BaseQuantities NetVolume, fall back to geometry volume, aggregate by storey, report mismatches and units. |
| `zh-revit-export-s006` | 机电和土建ifc我要导BIM5D，先帮我按楼层统计下各类构件数量，看有没有楼层对不上的<br>*EN: Count elements per storey before importing to BIM5D* | extract_quantities · medium · needs model | Group elements by storey, report counts and areas/volumes from Qto, flag elements with no storey. |
| `zh-cobie-s007` | 把模型里所有设备按楼层和房间导成表格，资产编号、系统、厂家都要，给运维系统导入用<br>*EN: Export asset list of equipment with floor and room to Excel for the FM system.* | convert_format · medium · needs model | Query equipment with floor, space, system, manufacturer, tag; export spreadsheet; flag missing asset IDs. |
| `zh-cobie-s008` | COBie导出来Component表是空的，是不是设备全变成IfcBuildingElementProxy了<br>*EN: COBie components sheet is empty after export; is it because everything became proxies?* | troubleshoot_export · medium · needs model | Check proxy counts and types; explain that COBie components require typed elements and fix mapping. |
| `zh-gis-s011` | 帮我按楼层统计一下构件数量，导出成表，数字孪生平台要用，顺便看看有没有没挂楼层的构件<br>*EN: Count components by floor for a digital twin platform.* | query_model_data · easy · needs model | Group elements by IfcBuildingStorey, list unassigned elements, output a table. |

### E. Developers, web viewers, encoding and size

| ID | Prompt (synthetic) | Intent · difficulty · file | Expected behavior (EN) |
|---|---|---|---|
| `enc-s002` | 这个ifc里中文名称是不是乱码了？帮我查一下墙和房间的名字，导出的时候哪里出问题<br>*EN: Check whether Chinese names in the model are escaped properly.* | validate_check · medium · needs model | Decode names of IfcWall/IfcSpace, report entries with raw non-ASCII or broken \X2\ sequences, explain Revit export settings. |
| `enc-s012` | ifcopenshell读出来的中文是\X2\开头的，怎么转成正常汉字<br>*EN: Python reads Chinese strings from IFC as hex escapes; how to decode?* | troubleshoot_code · easy · no file | Explain that ifcopenshell decodes automatically; if raw escapes are seen, inspect the file, show snippet. |
| `zh-csdn-dev-s002` | 这个ifc里构件名字全是\X2\xxxx\X0\这种，读出来是乱码，帮我看看哪些实体的Name有这个，解码后给我真实中文<br>*EN: Chinese names show up as \X2\ garbage, check which entities have it and decode* | validate_check · medium · needs model | Scan Name/ObjectType/property string values for \X2\ escapes, decode UTF-16 hex, list results, note whether the library already decodes and whether lowercase hex is a trigger. |
| `zh-csdn-dev-s003` | 帮我把这个ifc转成glb给前端用，每个mesh要带GlobalId，不然属性对不上，按楼层拆开最好<br>*EN: Convert to glb for web, keep GlobalId on each mesh* | convert_format · hard · needs model | Export geometry to glb, map each mesh to GlobalId (extras/node names), split by IfcBuildingStorey, produce metadata json, warn about lost properties. |
| `zh-csdn-dev-s004` | 导出来的模型在three里大了1000倍而且离原点特别远，看下ifc的单位和IfcSite的坐标是啥情况<br>*EN: Model is 1000x too large and far from origin; check units and placement* | troubleshoot_viewing · medium · needs model | Report IfcUnitAssignment length unit, IfcSite placement and map conversion, bounding box of elements, suggest scale and re-centering. |
| `zh-csdn-dev-s010` | 这个ifc 600多M前端根本加载不动，看看是什么占的体积，能不能砍掉不需要的东西<br>*EN: File too big for browser; what dominates its size* | optimize_performance · hard · needs model | Count entities by type, identify heavy geometry/properties/duplicate representations, suggest stripping or splitting without breaking references. |
| `zh-csdn-dev-s013` | vite项目用web-ifc-three一直报wasm加载失败，LinkError，路径配了也不行，咋整<br>*EN: wasm 404 / LinkError in Vite project, how to fix* | troubleshoot_code · medium · no file | Explain matching web-ifc and wasm versions, setWasmPath, serving .wasm with application/wasm, public folder placement. |
| `zh-csdn-dev-s015` | 要把这个ifc放到cesium上，模型有没有地理参考？IfcSite经纬度和IfcMapConversion有没有，没有的话给我原点和旋转怎么取<br>*EN: Extract georeference info needed for 3D Tiles* | convert_format · medium · needs model | Report IfcSite RefLatitude/RefLongitude/RefElevation, IfcMapConversion/CRS, True North, else explain manual origin. |
| `zh-fs-s008` | 这个ifc有800多M，网页里卡死了，帮我按楼层拆成几个小文件<br>*EN: IFC is too big and the viewer lags; split by floor* | optimize_performance · hard · needs model | Split the IFC by IfcBuildingStorey into several files preserving shared context, report counts and sizes. |
| `zh-zhihu-s013` | 想做个网页轻量化看ifc，用web-ifc还是转glTF？属性怎么带<br>*EN: How to get IFC into a lightweight web viewer* | find_tool · medium · no file | Compare web-ifc direct parse vs IfcConvert to glTF plus metadata JSON; note license and GlobalId linking. |

### F. Import, round trips, clashes, openings

| ID | Prompt (synthetic) | Intent · difficulty · file | Expected behavior (EN) |
|---|---|---|---|
| `zh-roundtrip-s008` | 这个ifc从archicad导出的，导入revit窗户跑到墙外面了，帮我查下门窗的IfcRelFillsElement和洞口位置<br>*EN: Windows/doors appear outside wall; check opening/filling relations.* | query_model_data · hard · needs model | Check IfcOpeningElement, IfcRelFillsElement, local placements of windows vs hosting wall; report offsets. |
| `zh-roundtrip-s009` | tekla导出的钢结构ifc导进revit构件丢了不少，怎么设置才能完整导入<br>*EN: How to bring Tekla steel IFC into Revit without losing members.* | how_to · medium · no file | Explain exporter settings, link vs open, class mapping, assemblies, and verification. |
| `zh-lightweight-review-s013` | PKPM导出的ifc导进revit少了好多梁，对比下原ifc里有多少梁，哪些没进去<br>*EN: Which structural members from PKPM disappeared after IFC import.* | convert_format · hard · needs model | Count IfcBeam in the source, compare with imported list, list missing by level and likely causes. |
| `zh-revit-export-s014` | ifc链进来的墙改不了啊，怎么变成revit自己的墙？<br>*EN: Linked IFC can't be edited, how to turn into native elements* | troubleshoot_import · medium · no file | Explain linked/opened IFC objects are not native editable; options: open IFC to convert, rebuild, or edit in source; explain limits. |
| `zh-zhihu-s014` | tekla的ifc在viewer里正常，revit里3D视图啥也没有，查下是不是几何有问题<br>*EN: Tekla IFC fine in viewer but empty in Revit* | troubleshoot_import · hard · needs model | Check representations/placements, units and extents; suggest recreating 3D view and linking vs importing. |
| `zh-clash-s009` | 帮我把机电和结构ifc做个碰撞检查，管线和梁柱，容差5mm，导出报告和bcf<br>*EN: Check pipe vs structure clashes in IFC and export a report* | coordinate_clash · medium · needs model | Run MEP-vs-structure clash, tolerance 5 mm, produce report grouped by clash pair and export BCF. |
| `zh-openings-s012` | 帮我查一下管线穿梁穿墙的位置，哪些还没开洞，导出预留洞清单<br>*EN: Find pipes through beams/walls needing reserved holes* | coordinate_clash · hard · needs model | Find MEP-structure intersections without openings, export reserved-hole list with size and location. |
| `zh-openings-s013` | 预留洞已经确认了，按清单在剪力墙上加洞口，尺寸加50mm余量<br>*EN: Add IfcOpeningElements for the confirmed reserved holes* | modify_model_data · hard · needs model | Create IfcOpeningElement with 50 mm clearance in walls, set IfcRelVoidsElement, report created GlobalIds. |

### G. Students and beginners

| ID | Prompt (synthetic) | Intent · difficulty · file | Expected behavior (EN) |
|---|---|---|---|
| `p-student-s011` | 帮我统计一下这个ifc里所有墙的数量和总面积，作业要用<br>*EN: Count walls and total wall area in the model, for homework* | extract_quantities · medium · needs model | Count IfcWall and sum NetSideArea/GrossSideArea from Qto; mention missing base quantities. |
| `p-student-s012` | ifc和rvt到底有啥区别？我直接导出ifc发给老师可以吗<br>*EN: What is the difference between IFC and RVT? Can I just send IFC to the teacher?* | understand_concept · easy · no file | Explain open exchange vs proprietary native, data loss, what to check before sending. |
| `zh-zhihu-s005` | 这个ifc的层级结构给我看下，项目-场地-建筑-楼层各有几个<br>*EN: Show the model structure from project to storeys* | query_model_data · easy · needs model | Return IfcProject>IfcSite>IfcBuilding>IfcBuildingStorey tree with element counts per storey. |
| `zh-zhihu-s012` | revit2019导ifc点了没反应只出个schema文件，咋回事<br>*EN: Export IFC does nothing* | troubleshoot_export · easy · no file | Explain missing/outdated IFC exporter, steps to install/update, check export folder permissions and settings. |
| `zh-revit-export-s015` | revit里怎么把自定义参数导成ifc属性？要弄txt映射吗<br>*EN: How to export custom parameters as IFC properties* | how_to · medium · no file | Describe user-defined property set file mapping, the 'Export Revit property sets' option, and 2027 UI changes. |

### H. AI/MCP flavoured requests (Revit)

| ID | Prompt (synthetic) | Intent · difficulty · file | Expected behavior (EN) |
|---|---|---|---|
| `zh-aimcp-s007` | 这个ifc里每层有多少面墙？按楼层列一下，顺便看有没有没挂到楼层的<br>*EN: How many walls on each floor?* | query_model_data · easy · needs model | Count IfcWall by storey via containment, list unassigned walls. |
| `zh-aimcp-s008` | 把dwg里A-WALL那层的双线墙翻成revit墙，先预览中心线和厚度再建，别建到一层去<br>*EN: Create walls from CAD layer* | modify_model_data · hard · needs model | Preview centerlines and widths, confirm, create walls on the specified level. |
| `zh-aimcp-s009` | cursor里mcp是绿的但revit没反应，8964端口被占了？怎么查<br>*EN: MCP connected but no Revit data* | troubleshoot_code · easy · no file | Check plugin running, port conflict, one client lock, config path. |
| `zh-revit-auto-s011` | 幫我掃一下水管穿樑的位置,列出每個穿透點需要的套管口徑,預留每邊30mm<br>*EN: Scan pipes crossing beams and list needed sleeve sizes* | coordinate_clash · hard · needs model | Find pipe-vs-StructuralFraming intersections, compute diameter + 2*30 mm, flag oblique or beam penetrations for review, read-only. |
| `zh-revit-auto-s013` | 每層平面圖自動出圖,圖號 A-101 往上編,視圖放到圖紙中間<br>*EN: Batch create sheets and place views* | automate_batch · medium · needs model | Create sheets with sequential numbers, place level plan viewports centered, report existing number collisions. |

### I. Traditional script (Taiwan and Hong Kong), TC

| ID | Prompt (synthetic) | Intent · difficulty · file | Expected behavior (EN) |
|---|---|---|---|
| `zh-tw-hk-s001` | 幫我檢查這個IFC每層樓的樓地板面積總和，跟送審圖面積表對不對得上<br>*EN: Check gross floor area per storey against the submission area table* | validate_check · medium · needs model | Sum IfcSpace/IfcSlab areas by IfcBuildingStorey, compare to given table, list mismatches. |
| `zh-tw-hk-s003` | IFC檔太大 300MB 傳不上系統，幫我看是哪些東西最肥<br>*EN: Find what bloats the IFC* | optimize_performance · hard · needs model | Rank products by geometry size/entity count (railings, MEP fittings), suggest exclusions or simplified export. |
| `zh-tw-hk-s005` | 模型裡中文名稱有亂碼嗎？列出哪些元件名稱怪怪的<br>*EN: Detect garbled Chinese names* | validate_check · medium · needs model | Scan Name/Description/property strings for mojibake or unescaped characters, list GlobalIds. |
| `zh-tw-hk-s006` | 這是第二次送審的IFC跟上一版比，哪些牆有改？GUID有沒有變<br>*EN: Diff two submission versions* | compare_versions · hard · needs model | Match by GlobalId, report added/removed/modified, flag GUID regeneration. |
| `zh-tw-hk-s010` | 座標是不是TWD97？原點對不對，有沒有設IfcMapConversion<br>*EN: Check coordinates TWD97 and map conversion* | validate_check · hard · needs model | Report IfcSite lat/long, IfcMapConversion/CRS, shared coordinates, flag missing. |
| `zh-tw-hk-s012` | 樓梯踏面跟級高有沒有符合建築技術規則？列出不合格的<br>*EN: Stair riser/tread code check* | validate_check · hard · needs model | Read IfcStair/IfcStairFlight riser/tread properties, compare to thresholds, list violations. |
| `zh-tw-hk-s013` | Revit匯IFC 門都變proxy 是哪裡設定錯了？<br>*EN: Why doors become proxy on export* | troubleshoot_export · medium · no file | Explain category mapping table, IfcExportAs, family category, check export settings. |
| `zh-tw-hk-s014` | 香港屋宇署BIM要用IFC2x3還是IFC4？Revit要選哪個MVD<br>*EN: Which IFC version for HK BD* | how_to · medium · no file | Explain that the IFC version and view definition must be confirmed against the Buildings Department's current published guidance, not guessed; describe the usual options (IFC2x3 Coordination View vs IFC4 Reference View) and what each loses; do not invent practice-note numbers. |
| `zh-tw-hk-s015` | IFC匯入Revit後平面有3D看不到，是不是階段的問題<br>*EN: IFC visible in plan not 3D* | how_to · easy · no file | Explain phase filter/view phase, linking vs opening IFC. |

### J. Opinion / selection

| ID | Prompt (synthetic) | Intent · difficulty · file | Expected behavior (EN) |
|---|---|---|---|
| `zh-zhihu-s016` | 想选国产bim软件，ifc来回导一遍测完整性，该检查哪些点<br>*EN: Plan an IFC roundtrip test to select domestic BIM software* | request_opinion · medium · no file | Propose a test checklist: class counts, GUID persistence, psets, geometry, materials, coordinates; compare before/after. |

### K. Rewritten for realism (new for this file)

These rewrites copy the bare-symptom style, mixed Latin/Chinese tokens and `求教`-type closers seen in the real titles.

| ID | Prompt (synthetic, rewritten) | Intent · difficulty · file | Expected behavior (EN) | Inspired by |
|---|---|---|---|---|
| `ZH-X1` | ifc导进revit之后3D视图里啥都没有，是不是模型离原点太远了？帮我看看这个ifc的坐标，求教<br>*EN: Nothing shows in the Revit 3D view after importing the IFC; is the model too far from the origin? Check the coordinates.* | troubleshoot_import · medium · needs model | Read IfcSite/IfcMapConversion/placements and the bounding box, report distance from origin and units; then list other usual Revit-side causes (phase filter, view range, 3D view regenerate). Say honestly that the Revit view itself cannot be inspected from the IFC. | `zh-revit-export-r001`, `zh-revit-export-s002` |
| `ZH-X2` | IFC檔太大傳不上系統，300多MB，幫我看看哪些類別佔最多，能刪的先列給我，不要直接動檔案<br>*EN: TC. IFC is 300+ MB and cannot be uploaded; show which classes are heaviest, list what could be removed, do not change the file.* | optimize_performance · medium · needs model | Count instances and estimate size by class (railings, MEP fittings, repeated geometry), propose exclusions, make no write operation, offer a smaller copy only after confirmation. | `zh-tw-hk-s003`, `zh-tw-hk-r002` context |
| `ZH-X3` | revit导出的ifc里中文名变成 \X2\...\X0\ 了，这是乱码还是正常编码？别改我原文件<br>*EN: Chinese names appear as \X2\...\X0\ escapes: is this mojibake or normal? Do not modify the original file.* | validate_check · easy · needs model | Explain that the escapes are standard STEP encoding of UTF-16; decode a sample to show the real names; check for lowercase-hex or truncation defects that some parsers mishandle; read-only. | `zh-csdn-dev-r021`, `zh-csdn-dev-r014`, `enc-s002` |
| `ZH-X4` | 屋宇署BIM自動核查要用IFC，幫我睇下呢個模型嘅樓面面積同衞生設備有冇齊。<br>*EN: HK colloquial written Cantonese. Does the model have floor areas and sanitary fixtures complete for the BD BIM check?* | validate_check · medium · needs model | List IfcSpace areas by storey and sanitary terminals (IfcSanitaryTerminal and related); flag missing values; state that the official BD plug-in is the authority and that the BIM model is supplementary to drawings. **Note:** written Cantonese is general knowledge, not observed in the research data; use sparingly. | `zh-tw-hk-r002` |
| `ZH-X5` | 我们下周要去深圳报建，ifc先帮我预检一下：基点坐标、正北角、楼层高程、构件属性有没有空的。自检工具1.3.0我这台电脑装不上<br>*EN: Pre-check for next week's Shenzhen filing: base point, true north, storey elevations, empty properties. The 1.3.0 self-check tool will not install.* | validate_check · hard · needs model | Read base-point/true-north/elevation values and list elements with empty properties; explain which checks it replicates and which only the official tool can do; do not claim a pass; do not invent the tool's rule list. | `zh-lightweight-review-r003`, `zh-lightweight-review-r004`, `zh-lightweight-review-s001` |
| `ZH-X6` | 我想二开一个revit的mcp工具，让AI批量改房间编号。先列出哪些房间编号重复了，先别动模型<br>*EN: I am building a Revit MCP add-in to bulk-edit room numbers: first list duplicate room numbers, do not touch the model.* | automate_batch · medium · needs model | Read-only duplicate detection on room numbers (name, level, id); present a proposed renumbering; apply only after explicit confirmation and report read-back. | `zh-aimcp-r023`, `zh-aimcp-r033` |
| `ZH-X7` | 老师让交ifc作业，我用revit导的。怎么知道导出来对不对？墙有几面、门窗有几个，帮我数一下<br>*EN: Homework: how do I know my Revit IFC export is right? Count walls, doors and windows.* | query_model_data · easy · needs model | Count IfcWall, IfcDoor, IfcWindow (and proxies), report FILE_SCHEMA and exporter header, flag elements exported as proxy; explain in plain words what to compare against the Revit schedule. | `p-student-s011`, `zh-zhihu-r010` |
| `ZH-X8` | web端打开这个ifc特别卡，是几何太多还是属性太多？draw call大概能估吗<br>*EN: The IFC is very laggy in the browser: too much geometry or too many properties? Can draw calls be estimated?* | optimize_performance · medium · needs model | Report element/instance counts, repeated vs unique geometry, triangle estimates and property volume; give an order-of-magnitude view of draw calls if each element becomes a mesh, with caveats; suggest splitting by storey or instancing. | `zh-csdn-dev-r001`, `zh-lightweight-review-s003` |

*Prompts listed: 78 (of which 8 rewritten for this file).*

## Tips for generating authentic prompts in this language

| Do | Don't |
|---|---|
| Write symptom-first and short: `revit导出ifc没有东西`, `门都变proxy`, `2D看得到3D找不到` | Don't write polished textbook questions; real titles drop the verb and the politeness |
| Give the Revit year (`revit2020`) but **leave out IFC version, MVD and export settings** most of the time | Don't have every user volunteer "IFC4 Reference View" |
| Keep identifiers in Latin: `IfcBuildingElementProxy`, `IfcExportAs`, `GUID`, `GlobalId`, `glTF`, `wasm`; lowercase brand names (`revit`, `tekla`, `ifc`) | Don't translate `proxy` into 代理构件 or IfcWall into 墙实体 inside a user's sentence |
| Use local words: 报建, 自检, 轻量化, 合模, 项目基点/测量点, 2000坐标, 二开, 翻模, 图模一致 | Don't use generic English-derived phrases like "进行模型验证" in a casual request |
| For permit tasks name the **city** and the tool version (`深圳`, `自检工具1.3.0`, `广州GDB`, `宁建模`) | Don't invent city rules or thresholds; ask the assistant to say when it needs the official document |
| Pick one script. TC: 匯出, 元件, 送審, 竣工模型, 圖則, 開孔. SC: 导出, 构件, 报建, 竣工模型, 图纸, 开洞 | Don't mix 匯出 with 报建 in one sentence unless modelling a cross-strait user on purpose |
| Add a human closer when it fits: `求教`, `请教`, `咋整`, `怎么办` on Q&A boards; `帮我…` or `看下…` to an assistant | Don't add exclamation hype (`神器！`, `干货满满`) to a user question; that voice belongs to vendors |
| Let frustration be the bare symptom plus a version (`没有反应`, `一片空白`, `不显示`) | Don't make users swear or write long emotional paragraphs |
| Mix tasks the way people do: count proxies by Revit category, then ask which mapping to fix; or ask for storey elevations before an upload | Don't assume the user has already read the IFC specification or knows STEP syntax |
| Expect honest limits in the answer: Revit-side visibility cannot be seen from the IFC; official checkers cannot be run | Don't score an answer as correct if it claims the file 'passes Shenzhen/Guangzhou review' |

Related: [multilingual glossary](../../08_glossary/glossary_multilingual.md), [abbreviations](../../08_glossary/abbreviations.md), [IFC in real projects](../../01_ifc_basics/00_ifc_in_real_projects.md).
