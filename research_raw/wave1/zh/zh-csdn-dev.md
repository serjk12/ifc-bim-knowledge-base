# CSDN / 博客园 / 掘金 / Gitee: IFC 开发 (IfcOpenShell, xBIM, web-ifc, 解析, glTF)
Cell: zh-csdn-dev · Languages: Chinese (some English-titled GitHub/CSDN-mirror items) · Collected: 2026-11-06 · Records: 36 real / 16 synthetic · Communities covered: CSDN blog and CSDN 问答, 博客园 (cnblogs), 掘金 (juejin), Gitee, GitHub issues by Chinese-speaking users, Bilibili (titles only)

## Top themes (ranked by frequency, 8-15 bullets, one line each)
- IFC to glTF/GLB/3D Tiles conversion for web, digital twin and Cesium (IfcConvert, DAE then COLLADA2GLTF, Xbim.GLTF, custom IfcOpenShell code, GISBox).
- Properties lost after conversion: expressID/GlobalId not carried, so the property table cannot be linked back to meshes.
- Large-model performance in the browser: lag, main-thread blocking, draw calls, picking at 20k+ elements, BIM "lightweighting" (轻量化) engines.
- Unit and origin problems: mm vs m scale x1000, IFC origin vs project base point, geo-referencing for Cesium.
- Chinese text encoding: Revit writes `\X2\...\X0\` escapes; GetLine / ifcXML parsing bugs; Chinese file paths breaking command-line tools.
- web-ifc / web-ifc-three setup pain: wasm path, WebAssembly LinkError, MIME type, version mismatches, npm/polyfill conflicts.
- xBIM (.NET) tutorials: IfcStore.Open, Xbim3DModelContext, wexbim, spatial hierarchy, triangulation, Excel reports.
- IfcOpenShell Python getting-started and install problems (conda vs pip, PyCharm interpreter, IFC2x3 vs IFC4 build).
- Revit export quality: class mapping to IfcBuildingElementProxy, lost shared parameters, IfcExportAs, category mapping file.
- Understanding raw IFC/STEP: reading a single wall, Pset attachment via IfcRelDefinesByProperties, spatial containment.
- Materials/colours turning grey in Unity/Three.js after export.
- Modifying IFC and writing back (Java, IfcOpenShell), GlobalId lookups.
- Domestic lightweight engines and open-source on Gitee (BIMI, BIM-LW, GimViewer) as alternatives to IFC viewers.

## What people want (the goals behind the questions)
- Get a BIM/IFC model into a browser, Unity or Cesium page that is fast and still clickable with properties (digital twin, smart-site dashboards).
- Keep component identity (GlobalId) and attributes when converting to lightweight formats.
- Extract geometry, coordinates and quantities programmatically for custom systems (cost, simulation, GIS).
- Understand IFC structure well enough to write their own parser; avoid Revit proprietary data.
- Fix Revit export so classes and properties arrive correctly.
- Find free/open tools that avoid commercial licences (xeokit licence concern, BIMserver) and domestic alternatives.
- Make Chinese names/properties display correctly.

## How people write here (register, typical length, jargon/slang with translations, misspellings of terms, code-switching, openers/closers, what context they give or omit, emotional tone) with short illustrative fragments (max 12 words each)
- Register: blog "笔记/实战/教程" voice, first person, step lists, code blocks, little greeting. Series numbering is common ("xBIM 基础16", "实战01", "（一）").
- Titles are keyword-stuffed and often sensational on CSDN ("【亲测免费】", "真复杂！", "！！！"); many CSDN items are auto-generated summaries of GitHub READMEs (gitblog accounts) and are low trust.
- Code-switching: tool and class names stay in English (IfcStore, GetLine, draw call, LOD, GLB, wasm); Chinese for narrative. Users say "ifc模型", "构件" (element), "属性集" (Pset), "轻量化" (lightweighting/decimation), "拾取" (picking), "三角面" (triangles), "卡顿" (lag), "乱码" (mojibake), "踩坑" (pitfall).
- Context given: library name and sometimes version, pasted error text; omitted: IFC schema version, Revit version, model size.
- Tone: neutral-instructional; frustration shows in titles with exclamation marks; hedging "应该是" (should be) from learners.
- Illustrative fragments: "ifc 到底如何渲染，真复杂！"; "模型能导出、能加载、能显示"; "全英文路径，否则会转换出错"; "转换后墙面可能全变灰"; "IfcConvert 会合并构件、丢 expressID".
- Chinese-speaking users on GitHub write short, polite English with little context ("which Chinese encoding pattern do you use").
- Vocabulary variants: 构件/要素 (element), 属性集/属性表, 楼层/标高 (storey), 工业基础类 (IFC full name), 国产 (domestic).

## Local ecosystem (official/government bodies, regulations and standards, local software, enthusiasts/educators, open-source projects encountered, with URLs)
- Standards: GB/T 25507-2010 (national adoption of IFC2x3-era "工业基础类平台规范"; not verified here, listing at https://www.chinesestandard.net/PDF/English.aspx/GBT25507-2010). Academic work notes IFC needs proxies/property sets to express Chinese cost-estimating data: https://salford-repository.worktribe.com/output/1443918/application-and-extension-of-the-ifc-standard-in-construction-cost-estimating-for-tendering-in-china
- Domestic BIM platform data format: BIMBase PModel exchange format mentioned in a 2024 paper as alternative to IFC (see Gaps).
- Gitee open source: BIMI lightweight engine https://gitee.com/xujunpro2/bim-example, IFC-Export https://gitee.com/xujunpro2/ifc-export, BIM-LW https://gitee.com/liuxinfeng/bim-lw, GimViewer https://gitee.com/cangyundashuju/gimviewer, Awesome BIM https://gitee.com/ironmanzzm/awesome-bim, topic page https://gitee.com/explore/topic/BIM
- Commercial tools mentioned: MinBIM (lightweight engine), GISBox, CesiumLab (Cesium实验室), 迪威模型网 online converter.
- Enthusiast bloggers (cnblogs): 西北逍遥 (IFC document series) https://www.cnblogs.com/herd/, 张传宁 xBIM series https://www.cnblogs.com/SavionZhang/
- Open-source libraries encountered: IfcOpenShell, xBIM Essentials/WebUI/Xbim.GLTF, web-ifc, web-ifc-three, web-ifc-viewer (ifcjs / That Open), xeokit/xeogl, three-mesh-bvh, gltf-transform, COLLADA2GLTF, BlenderBIM/Bonsai.
- Video: Bilibili BlenderBIM tutorials by iBlender (Chinese-dubbed).

## Notable sources (15-30 best URLs, one line each)
- https://juejin.cn/post/7698926562423357450 - 2026 large BIM on web retrospective, pain list.
- https://juejin.cn/post/7691297274821705728 - 2026 Revit/IFC to Three.js pipeline with concrete pitfalls.
- https://www.cnblogs.com/LeeSki/p/14293418.html - IFC to DAE to glTF steps, Chinese-path caveat.
- https://www.cnblogs.com/nihaozhe/articles/13651935.html - BIM lightweighting survey (Unity, WebGL, BIMserver).
- https://www.cnblogs.com/SavionZhang/p/10984048.html - xBIM IFC in browser via wexbim.
- https://www.cnblogs.com/SavionZhang/p/10983394.html - xBIM spatial hierarchy.
- https://www.cnblogs.com/flowell/p/10838972.html - Xbim.GLTF intro.
- https://www.cnblogs.com/herd/p/12183392.html - modify IFC property and write back (Java).
- https://www.cnblogs.com/liaocheng/p/15905467.html - Revit category to IFC class mapping.
- https://www.cnblogs.com/pandaNHF/p/16828047.html - reading a single wall in IFC text.
- https://www.cnblogs.com/herd/p/14908387.html - slab property log from Revit IFC.
- https://github.com/IfcOpenShell/IfcOpenShell/issues/571 - Chinese encoding question.
- https://github.com/ThatOpen/engine_web-ifc/issues/949 - GetLine lowercase \X2\ bug.
- https://github.com/IfcOpenShell/IfcOpenShell/issues/3499 - non-ASCII truncation in ifcXML.
- https://github.com/IfcOpenShell/IfcOpenShell/issues/777 - IfcConvert unable to parse Revit 2018 IFC.
- https://blog.csdn.net/liuzk423/article/details/136849803 - IfcOpenShell to glTF code.
- https://blog.csdn.net/pumbkin/article/details/141029954 - React + web-ifc-three wasm LinkError.
- https://blog.csdn.net/qq_35042852/article/details/137257689 - Revit Chinese transcoding in IFC.
- https://blog.csdn.net/Kobayashiqaq/article/details/130361282 - XBIM element coordinates.
- https://blog.csdn.net/vcit102/article/details/135365455 - how IFC is rendered.
- https://blog.csdn.net/liyan_gis/article/details/100132931 - BIM to 3D Tiles positioning.
- https://ask.csdn.net/questions/3915684 - xBIM missing walls.
- https://ask.csdn.net/questions/8391346 - Revit opening IFC loses elements.
- https://gitee.com/xujunpro2/ifc-export - domestic IFC lightweighting tool.
- https://www.bilibili.com/video/BV1Lx4y1L7P7/ - BlenderBIM Chinese tutorial.

## Gaps (what you could not access or find; suspicious sites skipped)
- csdn.net pages returned HTTP 521 on direct fetch, so CSDN records are mostly snippet-level; their years are inferred from article IDs or titles. ask.csdn.net years are estimates.
- zhihu.com returned 403; no Zhihu content read. segmentfault.com and oschina.net returned nothing relevant in searches; 51cto only tangential results.
- Real "asker" threads with a question and answers are scarce in this community: most posts are tutorials/notes. The genuine Q&A content came from GitHub issues by Chinese-speaking users and CSDN Q&A mirrors of English issues.
- Many CSDN "gitblog_*" posts are auto-generated README rewrites with unverified performance claims; deliberately not used as records.
- GB/T 25507 full title/scope was not verified; Chinese national IFC guidance and domestic software (广联达, 鲁班, 品茗, 盈建科, 构力 BIMBase) IFC export behaviour not covered here.
- No pirated/crack sites linked; online converter vendor pages (e.g. 迪威模型网, GISBox) treated as marketing and only cited as such.
