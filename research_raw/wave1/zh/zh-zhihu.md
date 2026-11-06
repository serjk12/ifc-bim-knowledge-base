# 知乎: IFC/BIM 问题 (IFC是什么, 导出, 国产BIM, 轻量化)
Cell: zh-zhihu · Languages: Chinese (zh-CN) · Collected: 2026-11-06 · Records: 45 real / 16 synthetic · Communities covered: Zhihu Q&A and Zhuanlan articles (via search snippets), plus CSDN, cnblogs and bilibili hits that surfaced in the same searches

Note: zhihu.com returned 403 on every fetch, so nearly all real records are `evidence: snippet` (titles plus search-result summaries). Answers are summarised from snippets only. Years are estimated from article ID ranges where the page did not show a date.

## Top themes (ranked by frequency)
- What IFC is, and how it differs from RVT or other native formats ("IFC是什么", "RVT和IFC关系").
- Which software opens or views IFC (BIM Vision, BIMSee, online viewers, ZWCAD), and requests for free tools.
- Revit IFC export failures: no response, greyed-out option, missing IFC exporter add-in, GUID not generated.
- Export mapping: category to IFC class, IfcExportAs, IfcBuildingElementProxy as a dumping ground.
- Information loss on export (colors, materials, properties, geometry) and distrust of IFC as a round-trip format.
- BIM lightweighting (轻量化): web viewers, glTF conversion, three.js / web-ifc / xeokit, engine vendors.
- Local government submission requirements (报建/报审): Shenzhen SZ-IFC, Shanghai EDM, Chengdu / Wuhan IFC review.
- Domestic BIM software (国产BIM) comparisons: Glodon Shuwei, PKPM-BIM / BIMBase, EasyBIM, Sware ueBIM, with IFC compatibility as the sore point.
- Importing IFC into Revit: not editable, links versus plugin import, coordinates and base-point offsets, file bloat.
- Python / C# parsing of IFC (IfcOpenShell, xBIM) for data extraction and Excel reports.
- IFC versions (IFC2x3 versus IFC4, IFC4.3 infrastructure) and IDS.
- AI / MCP / LLM with Revit and BIM (2025-2026 emerging).

## What people want (the goals behind the questions)
- Understand IFC quickly in a few lines, usually as a beginner or student.
- Open and inspect an IFC without installing Revit (free, lightweight, preferably Chinese-language).
- Get a clean export that passes a government reviewer's automated check, especially Shenzhen's SZ-IFC self-check.
- Stop elements from landing in IfcBuildingElementProxy or going missing.
- Shrink huge models (hundreds of MB to GB) for the web or for mobile.
- Choose a domestic software stack without losing data, and find out how well it handles IFC.
- Pull quantities and properties out of IFC into Excel (造价/算量 workflows).
- Let an LLM drive Revit or query IFC, with doubt about reliability.

## How people write here
- Register: short, direct, colloquial. Titles are often a bare term plus a question (`IFC是什么意思?`) or the classic `如何评价…`, `有没有…推荐一下？`, `…是为什么？`.
- Length: titles are 10-30 characters. Question bodies are usually one or two lines with a version and a symptom. Zhuanlan articles are long tutorials or vendor pieces.
- Code-switching: English terms are kept unspaced next to Chinese (`revit 2020 ifc guid不生成是为什么?`, `exportlayers-ifc-IAI`). Software names are often lowercase (`revit`, `tekla`, `rvt`).
- Slang and idioms: `减肥` (slim down a file), `神器` (killer tool), `合模` (merge models), `轻量化` (lightweighting), `报建/报审` (permit submission/review), `信创` (domestic-IT-stack compliance), `打脸` (clickbait), `干货` (substance), `保姆级教程` (step-by-step tutorial).
- Typical gaps: users give the Revit version but rarely the IFC version, MVD or export settings. The symptom is described but not the viewer used.
- Punctuation is mixed: half-width commas inside Chinese titles, and bracket tags like `【BIM】` or `【模型查看】`.
- Tone: mostly neutral or curious. Frustration shows as bare symptoms (`没有反应`, `不显示`). Vendor posts use exclamation marks and superlatives.
- Illustrative fragments: `导出位置只有一个schema文档`; `IFC到底是什么意思`; `如何评价广联达数维建筑和构力BimBase`; `3D视图不显示`; `完全免费！`.

## Local ecosystem
- Standards and bodies. buildingSMART / ISO 16739 is the reference. Chinese IFC and BIM storage standards (e.g. GB/T 25507, GB/T 51447) are mentioned only from background knowledge, not verified in this run. The rail standard TB/T 10183-2021 appeared in a snippet.
- Local regulation. Shenzhen: SZ-IFC converter plugin plus self-check tool, with CGCS2000 coordinate checks (https://zhuanlan.zhihu.com/p/673078056, https://zhuanlan.zhihu.com/p/654458491). Shanghai: BIM-assisted review trial from 2024-02-01 using EDM, with IFC "to be explored" (https://zhuanlan.zhihu.com/p/676069996). EasyBIM claims Chengdu / Shenzhen / Shanghai / Wuhan IFC rules (https://zhuanlan.zhihu.com/p/2053415784773313709).
- Domestic software. Glodon (广联达数维, BIMFACE engine, GFC data standard, BIM5D, GQI), PKPM-BIM / 构力 BIMBase (P3D kernel), EasyBIM, Sware ueBIM (斯维尔), 中望CAD (IFCIMPORT), 译筑 EveryBIM, 葛兰岱尔 lightweight engine, 超图 SuperMap exporter, BIMSee (free IFC viewer).
- Foreign tools in use. Revit (IFC Exporter add-in), Tekla, Archicad, Navisworks, BIM Vision (DATACOMP).
- Open source. IfcOpenShell (and IfcConvert, IfcPatch), xBIM, web-ifc / web-ifc-three, xeokit (licence claims conflict between sources), three.js, mcp-servers-for-revit (an MCP project reported on Zhihu).
- Educators and enthusiasts. Personal series such as "BIM学习心得", the 西北逍遥 cnblogs blog on IFC, ShanghaiBIM, and "每日一练" Revit daily tips.

## Notable sources
- https://www.zhihu.com/question/527323998 — IFC是什么意思?
- https://zhuanlan.zhihu.com/p/2025170865478807871 — IFC格式是什么？用什么软件可以打开？
- https://zhuanlan.zhihu.com/p/667304620 — IFC标准及格式介绍 (Common Language)
- https://zhuanlan.zhihu.com/p/649792298 — 一文看懂什么是IFC
- https://www.zhihu.com/question/49455994 — RVT与IFC关系
- https://www.zhihu.com/question/264127961 — Revit导出IFC丢失哪些信息
- https://www.zhihu.com/question/583830829 — IFC查看工具推荐
- https://www.zhihu.com/question/455661969 — revit2019导出IFC没有反应
- https://zhuanlan.zhihu.com/p/611709017 — Revit2020无法导出IFC
- https://www.zhihu.com/question/625548241 — IFC GUID不生成
- https://www.zhihu.com/question/418802002 — 修改revit导出IFC选项
- https://www.zhihu.com/question/60173683 — tekla导出ifc到revit不显示
- https://www.zhihu.com/question/30485422 — Tekla与Revit互转
- https://zhuanlan.zhihu.com/p/673078056 — SZ-IFC
- https://zhuanlan.zhihu.com/p/676069996 — 上海BIM智能辅助审查
- https://www.zhihu.com/question/642487361 — 数维 vs BIMBase
- https://www.zhihu.com/question/385964946 — BIM轻量化原理
- https://zhuanlan.zhihu.com/p/350723733 — ThreeJs轻量化浏览器 IFC
- https://zhuanlan.zhihu.com/p/602546350 — BIMSee免费IFC浏览器
- https://zhuanlan.zhihu.com/p/662463406 — IDS信息交付规范
- https://zhuanlan.zhihu.com/p/101268159 — Python解析IFC
- https://zhuanlan.zhihu.com/p/2081844898991444652 — Revit接入大模型 (MCP)
- https://zhuanlan.zhihu.com/p/2097988751914022344 — AI能否看懂图纸建BIM
- https://www.cnblogs.com/liaocheng/p/15905467.html — Revit导出IFC对应类型
- https://www.bilibili.com/video/BV1Ba41177xJ/ — Revit 2023 IFC导出映射对话框
- https://blog.csdn.net/zzutt/article/details/121492254 — IFC转Revit后减肥
- https://www.cnblogs.com/w2011/p/8424405.html — xBIM输出Excel

## Gaps
- zhihu.com and zhuanlan.zhihu.com, csdn.net (521) and ask.csdn.net all failed on WebFetch (403/521). Answer text and question bodies were not read, and only cnblogs/herd (IFC2x3 vs IFC4) opened. Real records are therefore mostly snippet-level; reader comments and the asker's own wording were not captured.
- No verification of Chinese national standard numbers (GB/T 25507, GB/T 51447) or of current local rules beyond the secondary articles quoted.
- Thin coverage of Chengdu / Wuhan IFC rules, Archicad IFC to Glodon / Luban / Pinming, and shared-parameter loss on export.
- Many articles are vendor marketing (EasyBIM, Glodon, lightweighting engines); claims such as "300MB to 20MB" are unverified.
- No GitHub hits for the Chinese query "IFC BIM 轻量化" via gh search. Suspicious or pirated download sites were not encountered or linked.
