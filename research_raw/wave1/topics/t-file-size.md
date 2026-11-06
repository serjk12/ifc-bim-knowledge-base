# File size and performance: huge IFC, slow export/import/viewing, optimization, web viewers on big models

Cell: t-file-size · Languages: English (real sources), Japanese (1 real); ru/zh/es/pt/de/fr/ja/ko/it only as synthetic prompts · Collected: 2026-11-06 · Records: 32 real / 16 synthetic · Communities covered: GitHub issues (IfcOpenShell, ThatOpen web-ifc and components, Autodesk revit-ifc, xBIM, BIMserver), buildingSMART forum, OSArch, Qiita

IMPORTANT LIMITATION: the WebSearch budget was exhausted before any search ran (every call was refused). Evidence comes only from the `gh` CLI and direct WebFetch of known URLs. Native-language communities (dwg.ru, csdn, cnblogs, zhihu, cad.de, foros) could NOT be searched. Non-English real coverage is one Japanese Qiita post. Non-English phrasing in the synthetic records is an informed guess, not observed.

## Top themes (ranked by frequency)
- Browser/WASM viewers run out of memory or abort on 30-500 MB IFCs (web-ifc, That Open Components, Fragments).
- Memory blow-ups in IfcOpenShell/Bonsai on 400-800 MB files (hundreds of GB RAM, geometry iterator growth).
- Comparisons with other tools as the yardstick ("Solibri / ODA viewer / xBIM opens it fine").
- Geometry-heavy culprits: proxies with face-based surface models, MEP repeated parts, duplicated vertices.
- Slow or hanging Revit IFC export; wish for diagnostics and a "fast export" mode.
- Optimisation tools (ifcpatch Optimise) that are themselves slow or memory hungry on big files.
- Parsing and indexing time for properties in JS versus C++.
- Multi-threading trade-offs: faster but far more RAM.
- Streaming/tiling approaches (IfcStreamer, tilers, fragments, 3D Tiles) as the recommended answer.
- Lazy loading and database-backed access (IfcOpenShell 0.9 lazy=True, SQLite/WASM).
- Compression and packaging (.ifczip naming) and delivery limits.
- Certification and buying: no speed requirement in buildingSMART certification.

## What people want (the goals behind the questions)
- Open a very large IFC at all, on a normal machine or in a browser, without crashing.
- Know which classes, geometry or properties make a file big, and cut them safely.
- Shorter Revit export times and a report of which objects are slow.
- Stream or tile a big model so a web viewer stays at 60 fps.
- Extract a small subset (one roof, one discipline) from a huge consultant IFC quickly.
- Predictable benchmarks: what load time and memory are "normal" for N MB.
- Process hundreds of MB programmatically (Python/C++/C#/JS) without leaks.

## How people write here
- Register: terse developer English in GitHub issues; bug template headings; stack traces and code pasted, little context about the building.
- Length: titles are error strings or symptoms ("Aborted() during StreamAllMeshes ..."); bodies range from two sentences to benchmark tables.
- Always quote sizes in MB/GB and times in seconds/minutes (e.g. "12MB: 222s vs 2s", "780 MB", "400MB+").
- Competitor comparison as evidence: "Solibri opens it just fine", "ODA viewer loads in a few minutes".
- Self-deprecation or hedging: "very crappy IFC exported from proprietary software", "possibly I use the lib incorrectly".
- Jargon: OOM, WASM, memory leak, fps, tiler/streamer, fragments, kernel (opencascade/cgal), proxy, ifczip.
- Shorthand in synthetic prompts mirrors expected forum slang: "ифс", "проксей", "psets", mixed English terms in ru/zh/ko/ja prompts.
- Emotional tone mostly frustrated or neutral; urgency appears when production deadlines are implied.
- Context given: file size, software and version, OS/RAM; context omitted: IFC schema version, export settings, what the model contains.
- Illustrative fragments: "memory climbs and climbs until the iterator finished"; "takes a lot to load and is super slow to move"; "waiting without knowing what is wrong is frustrating".

## Local ecosystem
- buildingSMART International forum (certification, IFC4.x implementers): https://forums.buildingsmart.org/ ; IFC4.x-IF repo https://github.com/buildingSMART/IFC4.x-IF
- IfcOpenShell / Bonsai (open source, Python/C++, ifcpatch recipes, 0.9 lazy loading): https://github.com/IfcOpenShell/IfcOpenShell
- That Open Company: web-ifc, Components, Fragments, IfcStreamer: https://github.com/ThatOpen/engine_web-ifc , https://github.com/ThatOpen/engine_components
- Autodesk Revit IFC exporter (open source, Jira-tracked): https://github.com/Autodesk/revit-ifc
- xBIM Toolkit (.NET, WexBIM, ESENT store): https://github.com/xBimTeam/XbimEssentials
- BIMserver (Java): https://github.com/opensourceBIM/BIMserver
- OSArch community (open source architecture): https://community.osarch.org/
- Commercial tools used as speed yardsticks: Solibri, BIMcollab ZOOM, Navisworks, BricsCAD BIM, Allplan, ODA OpenIFCViewer, BIMvision.
- Japanese engineers writing on Qiita about IfcOpenShell: https://qiita.com/

## Notable sources
- https://github.com/IfcOpenShell/IfcOpenShell/issues/6712 - IfcOpenShell vs xBIM timings, 12-700 MB.
- https://github.com/IfcOpenShell/IfcOpenShell/issues/9826 - 780 MB IFC, 340 GB RAM in Bonsai.
- https://github.com/IfcOpenShell/IfcOpenShell/issues/6905 - multi-threaded iterator memory.
- https://github.com/IfcOpenShell/IfcOpenShell/issues/6026 - 764 MB OOM from face-based surface models.
- https://github.com/IfcOpenShell/IfcOpenShell/issues/1603 - ifcpatch Optimise on large files.
- https://github.com/IfcOpenShell/IfcOpenShell/issues/8099 - slow save of subset-from-consultant workflow.
- https://github.com/IfcOpenShell/IfcOpenShell/issues/7829 - IfcFile memory when reopening.
- https://github.com/IfcOpenShell/IfcOpenShell/issues/7063 - 0.8.3 regression vs 0.7.1.
- https://github.com/ThatOpen/engine_web-ifc/issues/1999 - 400 MB+ Revit MEP IFC4 WASM crashes.
- https://github.com/ThatOpen/engine_web-ifc/issues/538 - 300k components abort.
- https://github.com/ThatOpen/engine_web-ifc/issues/1816 - property indexing time for 400-500 MB.
- https://github.com/ThatOpen/engine_web-ifc/issues/1064 - fragment geometry size / vertex welding.
- https://github.com/ThatOpen/engine_web-ifc/issues/1774 - memory out of bounds on frag conversion.
- https://github.com/ThatOpen/engine_components/issues/503 - 90 MB IFC at 10 fps; IfcStreamer answer.
- https://github.com/ThatOpen/engine_components/issues/458 - 33 MB IFC out of memory in Chrome.
- https://github.com/Autodesk/revit-ifc/issues/831 - request for fast export mode.
- https://github.com/Autodesk/revit-ifc/issues/1021 - unrecoverable export error on workshared model.
- https://github.com/xBimTeam/XbimEssentials/issues/551 - Out of table cursors above 100 MB.
- https://github.com/xBimTeam/XbimEssentials/issues/589 - Version store out of memory.
- https://github.com/opensourceBIM/BIMserver/issues/1162 - slow loading of large models.
- https://forums.buildingsmart.org/t/processing-speed-ifc-imports/2622 - certification and speed, Uptown.ifc benchmark.
- https://qiita.com/kiyuka/items/0d2ef739a0d34606a52f - IfcOpenShell 0.9 lazy loading benchmark (Japanese).
- https://community.osarch.org/discussion/comment/30702 - IFC to SQLite via WASM for large projects.
- https://github.com/buildingSMART/IFC4.x-IF/issues/6 - .ifczip extension suggestion.

## Gaps
- WebSearch was unavailable (budget exhausted), so no discovery search was possible: nothing from forums.autodesk.com Revit threads, Graphisoft community, Stack Overflow, Reddit, dwg.ru, csdn/cnblogs/zhihu, cad.de, foros/foruns, French, Korean or Italian communities.
- Autodesk forums search returned 403; buildingSMART forum JSON search was rate limited (429) after a few calls; OSArch search pages returned no listings; Habr search is JS-rendered; Stack Exchange API fetch is blocked.
- GitHub searches in Chinese, Japanese, Spanish, Portuguese, German, Russian and French returned nothing.
- Real records are therefore dominated by developer GitHub issues; end-user (architect, coordinator) phrasing about Revit export size, ArchiCAD, Navisworks and file-sharing limits is under-represented. Eight records are title-only (evidence "snippet").
- Non-English synthetic prompts are not validated against real community usage; a follow-up run with search access is recommended.
- No suspicious or pirated sites were encountered or linked.
