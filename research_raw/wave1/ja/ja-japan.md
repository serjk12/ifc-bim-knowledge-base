# 日本: Qiita/Zenn/ブログ/フォーラム: IFC 出力・読み込み・BIM確認申請

Cell: ja-japan · Languages: Japanese · Collected: 2026-11-06 · Records: 31 real / 17 synthetic · Communities covered: Zenn (articles and scraps via topic API), Qiita (one article), note.com (IFC/BIM hashtag), buildingSMART Japan (official)

## Top themes (ranked by frequency)
- BIM確認申請: BIM図面審査 (from Apr 2026, PDF plus IFC as reference) and BIMデータ審査 (target spring 2029), IFC as review object
- IfcOpenShell Python: extracting attributes, Psets, materials, storeys, to Excel/CSV
- "IFCは万能ではない": information loss, IFC is for sharing not editing, expectation gaps
- Export problems: elements missing, class mapping, levels/stories not linked, visibility
- openBIM basics for newcomers: IFC, BCF, IDS, bSDD, OpenCDE
- IDS and validation (IfcTester, IFC Validation Service, buildingSMART)
- Browser IFC viewers (web-ifc, Three.js, Babylon.js), version regressions
- Large-file performance and conversion (glTF, lazy loading, ETL to Parquet/DuckDB)
- Quantity takeoff 積算 from IFC; BIM/CIM
- Free/open-source tools for small offices (Bonsai, FreeCAD, BIMCraft, BIMvision) vs expensive licences
- AI/LLM with Revit (Revit-MCP, Claude Code add-ins)
- Qualifications: IFC検定 (software), BIM利用技術者 (people)
- Room/area/unit consistency between authoring model and IFC

## What people want
- Know what IFC the building authority will read and what to put in it (rooms, uses, areas).
- Export from Revit/Archicad/Vectorworks without losing elements or attributes; verify in a second viewer.
- Dump IFC data to Excel/CSV/databases for checking and estimating.
- Open IFC cheaply on site or in small offices without multi-GB software.
- Automatic checking of delivered IFC against client requirements (IDS).
- Let AI drive Revit or read IFC, with trustworthy results and clear accountability.

## How people write here
- Zenn/Qiita: terse, code first, plain da/dearu or desu/masu; scraps are working notes with honest "分からない".
- note: first-person, polite desu/masu, headed sections (■), hedged claims, invite corrections.
- Heavy code-switching: IFC entity names in English (IfcBuildingElementProxy), katakana jargon, English acronyms.
- Jargon: 確認申請, 図面審査, 入出力基準, 壁芯, 1間, 野良データ (stray data), 軽量化, 干渉チェック, 属性, 書き出し (export), 読み込み (import), リンク.
- Fragments: "IFCに出したら、半分なかった", "IFCは万能ではありません", "全てのopenBIMはbSDDから", "Attributeしか書き出せないので".
- Usually little context: software named, version rarely; IFC schema often omitted. Tone mostly neutral or mildly frustrated, rarely rude.

## Local ecosystem
- 国土交通省 (MLIT): BIM図面審査 guideline (Mar 2026), 建築BIM推進会議, 審査/標準化タスクフォース; 2029 basic concept https://www.mlit.go.jp/
- buildingSMART Japan (bSJ): IFC検定, MVD, certified software list https://www.building-smart.or.jp/
- ACSP: BIM利用技術者 exams (Revit, Archicad, GLOOBE Architect, Vectorworks; IFC2x3 submission)
- Local software: GLOOBE Architect, Jw_cad, Archicad, Vectorworks, Revit; free viewers BIMvision, Autodesk Viewer
- Open source: IfcOpenShell, Bonsai, web-ifc, Three.js, BIMCraft, FreeCAD
- Companies/enthusiasts: ONESTRUCTION (openBIM, bSDD), Obayashi, Maeda (IFC to estimating)

## Notable sources
- https://zenn.dev/miyamiyaumya/articles/19a4247133dde6 IFC attributes/Psets/materials to Excel
- https://zenn.dev/miyamiyaumya/articles/6714ef2c6e2c6c IDS explained
- https://zenn.dev/miyamiyaumya/articles/909be24ee185ac IfcOpenShell install/usage
- https://zenn.dev/cote2/articles/6459c1c44091da storeys with IfcOpenShell
- https://zenn.dev/toggle_inc/articles/cf8df02f7b4ba7 build IFC from scratch
- https://zenn.dev/kiyuka/scraps/2894037aa4f997 FlangeSlope question
- https://zenn.dev/kiyuka/scraps/e07bf799384b52 IFC Validation Service local
- https://zenn.dev/kiyuka/scraps/48157a38db558e IFC relationship structure
- https://zenn.dev/kiyuka/scraps/a054a249f42a93 IFC to glTF
- https://qiita.com/kiyuka/items/0d2ef739a0d34606a52f IfcOpenShell lazy loading
- https://zenn.dev/grok_prtex/articles/webifc-version-compare web-ifc versions
- https://zenn.dev/kazuyamaeda/articles/97933cdafce6d8 browser IFC viewer
- https://zenn.dev/tomosandego/articles/59e6cf8dfe60bc BIM ETL
- https://zenn.dev/yuichi_ai/articles/879de49ee8e1bb Revit-MCP
- https://zenn.dev/aec/articles/58aa31c1089332 Claude Code Revit add-in
- https://note.com/toshio_nakamura/n/nc8db42ce3191 half of the elements missing
- https://note.com/kensesu_ai/n/nee08ddde31f1 BIM図面審査 / データ審査
- https://note.com/ken_newslab/n/n9d7072936346 2029 review overview
- https://note.com/t_note_memo/n/n8903305b00fb one-room export test
- https://note.com/legal_tiger6680/n/n6781ba815061 BIMCraft and 2029
- https://note.com/bim_tool_lab/n/nf529aa5d5cc0 IFC not omnipotent
- https://note.com/onestruction/n/ne8322e3be44d IFC expectation gaps
- https://note.com/aei830/n/ndfa486486036 BIM利用技術者
- https://note.com/akram/n/n8a6e9c5602ca Bonsai in practice
- https://note.com/limber_stork5044/n/n68df8d5a268b small MEP office
- https://www.building-smart.or.jp/ifc/whatsifcverifi/ IFC検定

## Gaps
- WebSearch budget was exhausted at the start (all four initial searches refused), so no keyword search was run; discovery was via Zenn topic API, note hashtag page and direct fetches only. Fewer than the target 20 searches/fetches of the search kind; fetches totalled about 50.
- Not reached: Autodesk Japanese forum (403), Graphisoft Japan community, Qiita article lists (JS-rendered; only one article visible), Qiita Q&A, Teratail/OKWave questions, MLIT official pages (a guessed URL returned an unrelated page/404, so no official MLIT URL is cited), Twitter/X.
- Publication years of several note posts are inferred (2026) from content. Many real records are tutorials/essays rather than forum questions, so genuine question phrasing (help-seeking) is under-represented.
- No suspicious sites encountered.
