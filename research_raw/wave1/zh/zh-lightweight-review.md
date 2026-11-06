# BIM轻量化, BIM审查/报建 (深圳 SZ-IFC, 广州, 南京, 湖南, 雄安 XDB) 与国产平台 (BIMBase, 广联达, PKPM)

Cell: zh-lightweight-review · Languages: Chinese (zh-CN) · Collected: 2026-11-06 · Records: 31 real / 18 synthetic · Communities covered: Zhihu columns (snippets only), CSDN, cnblogs, CO188 (土木在线), city government portals (Shenzhen, Guangzhou, Nanjing), Autodesk China KB, Chinese academic abstracts.

Important caveat: the WebSearch budget ran out after about 12 searches, and zhihu.com returned 403 while csdn.net returned 521 on most fetches. Most "real" records are therefore article titles and snippets, not Q&A threads. Many are `evidence: snippet`. Treat the question paraphrases as reconstructions of what the article answers.

## Top themes (ranked by frequency)
- Shenzhen SZ-IFC filing (报建): converter plugin, self-check tool (自检工具), versions (1.1.0 invalid, 1.3.0 required), failing checks.
- Properties or fields lost or empty in the exported IFC (审查节点值为空, custom Pset not exported).
- Project base point and coordinates (CGCS2000, 国家2000坐标系), far-from-origin values, missing IfcMapConversion.
- Revit export mapping to IFC classes (IfcExportAs, IfcBuildingElementProxy fallback, missing elements, unloaded links).
- BIM lightweighting (轻量化) for web: IFC too heavy, IFC to glTF / 3D Tiles / OBJ / FBX chains, Forge vs BimFace vs in-house.
- File size blow-up and slow conversion (100MB model becomes 1GB IFC then 3GB OBJ).
- City-specific BIM review systems and formats: Guangzhou GDB, Nanjing 宁建模, Shanghai EDM, Shenzhen SZ-IFC, Hubei H-IFC, Taizhou/Anhui XDB-like review databases.
- Scope rules: which projects must submit BIM (area/investment thresholds, pilot zones, prefab, government-funded).
- Drawing-model consistency (图模一致 / 图模对位) between 2D CAD and BIM.
- Domestic platforms and formats: BIMBase PModel vs IFC, PKPM, Glodon; autonomous and controllable (自主可控) BIM.
- Handover and completion models (竣工模型交付) and feeding the CIM platform.
- Pre-check inside Revit before export to save review rounds.

## What people want (the goals behind the questions)
- Pass the automated check on the first upload to the government system with no repeated export cycles.
- Know exactly what the review system requires (coordinates, attributes, class names, versions) and whether the file meets it.
- Find out why attributes or components vanished and fix it at the source (Revit parameters, export mapping).
- Show a heavy model in a browser quickly, keep the component ID and property link, and filter/select by attribute.
- Convert between domestic formats and IFC without losing data; pick a lightweighting platform or build one.
- Keep the 2D drawings and the model consistent for reviewers.
- Understand the policy: thresholds, stages, which standard version is current.

## How people write here
- Register: Chinese technical blogs are tutorial-style, often with hype hooks such as 干货满满 ("packed with substance"); official notices use formal 通知/试行/辅助审查.
- Short noun-phrase titles combined with English acronyms: "Revit二次开发——SZ-IFC", "revit导出ifc没有东西".
- Heavy code-switching: IFC, Revit, glTF, three.js, proxy and IfcExportAs stay in English, and the rest is Chinese. IFC often lowercase "ifc".
- Jargon: 报建 (permit filing), 报批 (approval submission), 审图 (drawing review), 自检 (self-check), 轻量化 (lightweighting, i.e. converting to a light viewable format), 图模一致 (drawing-model consistency), 构件 (component), 基点 (base point), 2000坐标 (CGCS2000), 存证 (certified record), 宁建模 (Nanjing model format), 自主可控 (self-reliant and controllable).
- Casual advice: "重装软件或换一台电脑导出" (reinstall or switch computer) shows trial-and-error culture.
- Context given: city name, tool version numbers (1.1.0, 1.3.0), file sizes in M/G; rarely IFC schema version.
- Fragments: "没有模型结构树", "导出ifc没有东西", "100M的模型导出IFC可能有1GB", "审查节点值是空的".
- Tone: pragmatic, mildly frustrated at repeated rounds; vendor posts promotional.

## Local ecosystem
- Shenzhen: SJG114-2022 SZ-IFC storage standard; SZ-IFC converter plugin and self-check tool (1.3.0 mandatory from 2024-01-01); Qianhai IFC-based verifiable standard system. https://zjj.sz.gov.cn/attachment/0/678/678888/7768421.pdf
- Guangzhou: BIM planning approval (2020) https://www.gz.gov.cn/xw/tzgg/content/post_6469259.html ; construction drawing BIM review (2020) https://zfcj.gz.gov.cn/gkmlpt/content/6/6434/post_6434530.html ; delivery and data standards, GDB files; CIM white papers (2024, 2025) https://zfcj.gz.gov.cn/attachment/7/7943/7943479/10589336.pdf
- Nanjing: BIM intelligent review system, 宁建模 format, DB3201/T 1145-2023 https://amr.nanjing.gov.cn/ztzl/bzhzl/tzgg/202302/P020230216538033075572.pdf ; explainer http://ghj.nanjing.gov.cn/njsgtzyj/202103/t20210301_2834720.html
- Shanghai: EDM data and IFC for structural loads in the BIM review manual (V1.0, 2023).
- Hubei: H-IFC provincial cloud platform (2026). Anhui: 2025 BIM review data standard. Taizhou, Jiangsu: DB3212/T 1146-2023 defines XDB as an open database file for review delivery (mentioned in search summary only; URL not verified).
- Hunan: DBJ43/T 519-2020 prefab BIM delivery standard (search summary only); no provincial BIM review standard found.
- Xiong'an: no XDB standard found; the XDB association with Xiong'an could not be confirmed.
- buildingSMART China: CN-IFC (IFC4.3-based, 2022).
- Software: BIMBase / PModel (Beijing Glodon-independent vendor, 构力科技/PKPM family), Glodon (广联达), PKPM, SuperMap, CesiumLab, Forge, BimFace; open-source: IfcOpenShell, xBIM, three.js.
- Educators/individuals: sunyuanrui.com (SZ-IFC handbook author).

## Notable sources
- https://www.sunyuanrui.com/works/sz-ifc-research/ (read; SZ-IFC pain points)
- https://bbs.co188.com/thread-10112116-1-1.html (read; Revit export loss)
- https://www.cnblogs.com/lingyanspace/p/19739094 (read; IFC lightweight web viewer)
- https://zhuanlan.zhihu.com/p/673078056 (SZ-IFC Revit dev)
- https://zhuanlan.zhihu.com/p/633827596 (Revit-side self-check)
- https://zhuanlan.zhihu.com/p/672903162 (self-check 1.3.0)
- https://blog.csdn.net/weixin_42855822/article/details/139867051 (Shenzhen filing FAQ)
- https://zhuanlan.zhihu.com/p/504617257 (Guangzhou designers on BIM review)
- https://zhuanlan.zhihu.com/p/157220418 (Guangzhou BIM review notice)
- https://www.gz.gov.cn/xw/tzgg/content/post_6469259.html
- https://zfcj.gz.gov.cn/gkmlpt/content/6/6434/post_6434530.html
- http://ghj.nanjing.gov.cn/njsgtzyj/202103/t20210301_2834720.html
- https://amr.nanjing.gov.cn/ztzl/bzhzl/tzgg/202302/P020230216538033075572.pdf
- https://zjw.sh.gov.cn/cmsres/4a/4a7bc95634cd4852b2399e57e9c692dd/a646541bab5ad86dc1684d1126e21e29.pdf
- https://blog.csdn.net/qq_35187495/article/details/118198777
- https://blog.csdn.net/nihaozhe/article/details/108704151
- https://blog.csdn.net/niuge8905/article/details/104366954
- https://blog.csdn.net/liuzk423/article/details/136850936
- https://zhuanlan.zhihu.com/p/350723733
- https://www.autodesk.com.cn/support/technical/article/caas/sfdcarticles/sfdcarticles/CHS/Missing-elements-or-steel-connections-in-IFC-file-exported-from-Revit.html
- https://search.napstic.cn/literature/periodical/010tmjzgcxxjs202401009 (BIMBase PModel paper)
- https://search.napstic.cn/literature/periodical/010tmjzgcxxjs202404016 (SZ-IFC QC paper)
- https://zfcj.gz.gov.cn/attachment/7/7943/7943479/10589336.pdf

## Gaps
- WebSearch budget exhausted early (about 12 searches instead of 20+); no searches on Glodon, PKPM, BIMBase forums, Xiong'an XDB specifics, Hunan review, bilibili, juejin, gitee.
- zhihu.com returned 403 and most csdn.net pages 521; those records are snippet-only. GitHub CLI search hit a rate limit, so no open-source repos were enumerated.
- Real asker voices (threads with actual questions) are scarce; most records are articles and notices. Question paraphrases are inferred.
- No confirmed source for 雄安 XDB; XDB found only for Taizhou standard in a search summary. No Glodon GFC or PKPM IFC material found.
- No suspicious or pirated sites were encountered.
