# Revit 导出/导入 IFC 问题 (百度知道, 筑龙, CSDN问答, bilibili, 微信文章)
Cell: zh-revit-export · Languages: Chinese (zh-CN) · Collected: 2026-11-06 · Records: 28 real / 17 synthetic · Communities covered: Baidu Zhidao (read), Zhulong forum/resource pages (snippets), CSDN Q&A (snippets only, 521 on fetch), bilibili (one video page read, articles blocked by captcha), cnblogs, Jianshu, Zhihu zhuanlan/questions (snippets; fetch 403). WeChat (mp.weixin.qq.com) returned no hits.

## Top themes (ranked by frequency)
- IFC imported/linked into Revit is invisible or blank in 3D (phases, visibility, huge coordinates, view range).
- Coordinates and base points: project base point vs survey point, "origin to origin" linking, models far from origin.
- Elements or materials lost/deformed when opening IFC in Revit or after RVT to IFC (colors turn grey).
- Materials/textures lost moving models between tools (Max, SketchUp, FBX) via IFC-like exchange.
- Export mapping: Revit category to IFC class table (exportlayers-ifc-IAI.txt), many categories fall to IfcBuildingElementProxy.
- Custom/shared parameters not appearing as IFC properties; property-set mapping txt; Revit 2027 adds UI.
- Version compatibility: opening a newer RVT in an older Revit via IFC2x3, loss of phases.
- Exporter problems: IFC export greyed out in Revit 2020, missing GUID, crashes.
- Handover to Chinese downstream tools: Glodon BIM5D import of IFC vs native plugin.
- Local compliance: Shenzhen SZ-IFC review of base-point coordinates, elevation and true north.
- IFC file size far larger than RVT; lightweighting.
- Imported IFC objects not editable as native Revit elements.

## What people want (the goals behind the questions)
- Get IFC to show up correctly in Revit (position, visibility) without understanding the cause.
- Keep materials, colors and custom parameters through the exchange.
- Hand a model to another software or an older Revit version without losing data.
- Meet local submission/review requirements (Shenzhen SZ-IFC) and feed Glodon BIM5D for cost/construction.
- Align multi-person or multi-discipline models with consistent base points.
- Shrink huge IFC files.

## How people write here
- Titles are short symptom statements, often ending with 如何解决 / 怎么办 / 怎么回事 and a question mark; CSDN titles are long and templated (probably AI-assisted).
- Little context: seldom Revit version, IFC version or source software. Example: "ifc导入revit后三维不可见".
- Software names mixed: Revit/REVIT/revit in lowercase, "Su" for SketchUp, "MAX", "pln"; IFC terms kept in Latin (GUID, IfcBuildingElementProxy, MVD).
- Colloquial verbs: 导进 (import), 链进来 (link in), 丢了 / 丢失 (lost), 变形 (distorted), 卡 (laggy), 一片空白 (blank).
- Humble closer 求教 / 请教; opener-less. Example: "…怎么设置测量点和基点…求教".
- Blog titles use relief or series markers: "终于搞清了…", "第二节…", "[Revit]…", "Revit|…".
- Answers are numbered checklists (7 causes, phase merge) and often generic; tone mostly neutral to frustrated.
- Terms: 项目基点 (project base point), 测量点 (survey point), 原点对原点 (origin to origin), 映射表 (mapping table), 轻量化 (lightweighting), 报建 (permit submission), 阶段 (phase).

## Local ecosystem
- Glodon (广联达) BIM5D: https://www.glodon.com (IFC and Revit plugin import discussed on Zhulong).
- Shenzhen SZ-IFC review/conversion requirements (base point coordinates, elevation, true north): https://zhuanlan.zhihu.com/p/673078056
- Zhulong BIM forum (筑龙): https://bbs.zhulong.com/106010_group_3002227/detail33178172/
- Autodesk Revit IFC exporter (open source, revit-ifc): https://github.com/Autodesk/revit-ifc
- Enthusiast uploaders (bilibili "阿萌_BIM" 2023 new-features series), cnblogs/Jianshu/Zhihu bloggers.
- National BIM storage standard GB/T 51447 was not located in this pass.

## Notable sources
- https://zhidao.baidu.com/question/341569640619976845.html : IFC invisible in Revit, 7 causes (read).
- https://zhidao.baidu.com/question/1755259387786621668.html : multi-person base/survey point setup (read).
- https://zhidao.baidu.com/question/593298625.html : ArchiCAD pln to Revit.
- https://ask.csdn.net/questions/8391346 : Revit opens IFC with missing/deformed elements.
- https://ask.csdn.net/questions/8816624 : move base point from 2000 coordinates to 0,0,0.
- https://ask.csdn.net/questions/8796533 : Max to Revit materials lost.
- https://www.cnblogs.com/OverloadBachPunk/p/14452654.html : fix blank import by merging phases (read).
- https://www.cnblogs.com/liaocheng/p/15905467.html : category to IFC class table (read).
- https://www.cnblogs.com/nihaozhe/articles/13651935.html : BIM lightweighting, IFC size.
- https://www.cnblogs.com/herd/p/15765322.html : IfcBuildingElementProxy doc.
- https://www.bilibili.com/video/BV1Ba41177xJ/ : Revit 2023 IFC export mapping dialog (read).
- https://www.bilibili.com/read/cv18398331/ : Revit to FBX loses materials.
- https://www.bilibili.com/read/cv20354710/ : layer export settings.
- https://www.zhulong.com/zt_bim_3002296/detail42826395/ : open newer RVT in older Revit via IFC2x3.
- https://www.zhulong.com/zt_bim_3002296/detail40283815/ : Revit MEP IFC into BIM5D.
- https://bbs.zhulong.com/106010_group_3002227/detail33178172/ : Revit plugin for BIM5D.
- https://zhuanlan.zhihu.com/p/649792298 : what is IFC, mapping table.
- https://zhuanlan.zhihu.com/p/2025149945674474186 : Revit 2027 IFC property set UI.
- https://zhuanlan.zhihu.com/p/673078056 : SZ-IFC.
- https://zhuanlan.zhihu.com/p/611709017 : Revit 2020 cannot export IFC.
- https://www.zhihu.com/question/625548241 : Revit 2020 IFC GUID not generated.
- https://www.zhihu.com/question/49455994 : RVT vs IFC relationship, color differences.
- https://www.jianshu.com/p/76e051ccd5eb : IFC export parameters, insertion point.
- https://www.jianshu.com/p/409188142cfa : inconsistent base points.
- https://zhuanlan.zhihu.com/p/535737725 : Revit's five positioning points.

## Gaps
- WebSearch budget ran out after about 14 searches, so fewer searches than planned; WeChat (mp.weixin.qq.com) and most Zhulong forum threads produced no direct hits.
- Zhihu (403), Jianshu (403), CSDN (521) could not be fetched; many records are snippet-only. bilibili read pages returned captcha.
- Several record questions (e.g. GUID, Zhihu mislinked IFC) have no read answers; answer_summary for those is tentative.
- No explicit searches on file size, material loss and "no edit" completed beyond snippets; no Chinese government standard pages (GB/T 51447, 深圳 SJG) were opened.
- No suspicious or pirated-software sites were linked; none were visited.
