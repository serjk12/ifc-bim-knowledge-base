# Japanese: how people ask about IFC, BIM and Revit

**Last compiled: 2026-11-06.** Language code `ja`. Built from `research_raw/wave1/ja/ja-japan.*` plus Japanese records found in the AI/MCP, topic and role cells.

## Read this first (what the data can and cannot tell you)

- **Size of the evidence.** 57 real records pointing to 47 distinct pages (several cells logged the same Qiita/Zenn article) and 47 synthetic prompts.
- **Almost no help-seeking threads.** The research tool could not run keyword searches, so discovery went through Zenn's topic pages, a note.com hashtag page and direct fetches. The "real" records are therefore mostly **articles, working notes (Zenn scraps) and explainers** in which the author states the problem. Genuine Q&A voices (Teratail, OKWave, Autodesk and Graphisoft Japan forums, X/Twitter) were **not reached**. Treat the "questions" below as problem statements written by practitioners, not as forum posts from beginners.
- **Dates:** many note.com posts have years inferred as 2026 from their content. Dates for the future rollout of "BIM data review" come from secondary sources and one vendor page; see the caveat in the ecosystem section.
- Reference: [Japan and Korea national requirements](../../02_standards_regulations/national/japan_korea.md).

## Where people ask

Counts are distinct source URLs among the 47 real pages.

| Platform | Distinct URLs | What you find there | Access notes |
|---|---|---|---|
| **Zenn** (articles and *scraps*, i.e. open-ended working notes) | 17 | IfcOpenShell recipes (attributes/Psets/materials to Excel, storeys), IDS explained, IFC Validation Service in Docker, web-ifc version comparison, browser IFC viewers, Revit-MCP and Claude Code add-ins, BIM ETL | Fetchable via topic API. Scraps show honest "分からない" and quoted errors |
| **Qiita** | 13 | IfcOpenShell lazy loading, IFC structure decoding, Revit UniqueId vs IFC GUID, PLATEAU/CityGML, Bonsai for facility management, IDS "ゆるく説明" | Article lists are JS-rendered; individual articles readable |
| **note.com** | 12 | Practitioner essays: BIM図面審査 (2026-04) and BIMデータ審査 (2029), "IFCは万能ではない", Bonsai in practice, a small MEP office's first BIM, BIMCraft, BIM利用技術者 | Hashtag page worked; some posts partly paywalled |
| **GitHub** | 4 | Japanese AI/BIM projects (`ifc-bim-llm-finetuning`, `revit-mcp-toolkit` with a Japanese disclaimer) and English issues by Japanese users (xBIM load failure with Japanese `\X2\` text, Bonsai external style with a Japanese material name) | Open |
| **buildingSMART Japan** (official) | 1 | IFC検定 explanation | Open |
| Not reached | - | Autodesk Japan forum (403), Graphisoft Japan community, Teratail / OKWave, Qiita Q&A, X/Twitter, MLIT pages (a guessed URL gave an unrelated page) | Gap in the data |

## Top themes (ranked)

Counts are real records per KB topic tag among the distinct pages (a record can carry several tags).

| Rank | Theme | Records | Typical wording | Related KB doc |
|---|---|---|---|---|
| 1 | **確認申請 and BIM**: BIM図面審査 (since 2026-04-01; PDF drawings plus IFC as reference) and BIMデータ審査 (IFC as review object, targeted spring 2029) | national 6 + permitting 5 | "確認申請の「図面の突き合わせ」が変わった" | [Regulations, permits, contracts](../by_topic/regulations_permits_contracts.md) |
| 2 | **IFC basics for newcomers**: IFC, BCF, IDS, bSDD, OpenCDE, "IT人向けのopenBIM入門" | 8 | "IFCとは何か？" | [What is IFC](../../01_ifc_basics/01_what_is_ifc_and_versions.md) |
| 3 | **IfcOpenShell in Python**: dump attributes, Psets, materials, storeys to Excel/CSV; build IFC from scratch | 7 | "IfcOpenShellで階情報を取得する" | [Programming and automation](../by_topic/programming_and_automation.md) |
| 4 | **IDS and validation**: automatic checking of delivered IFC; IFC Validation Service | ids 5 + validation 5 | "納品IFCのチェックが人力" | [Validation, IDS, model checking](../by_topic/validation_ids_model_checking.md) |
| 5 | **"IFCは万能ではない"**: information loss, IFC is for sharing not editing, expectation gaps; half the elements missing after export | 4 export + essays | "IFCに出したら、半分なかった" | [Revit export and class mapping](../by_topic/revit_export_and_class_mapping.md) |
| 6 | **AI/LLM with Revit and IFC**: Revit-MCP, Claude Code add-ins, small-model fine-tuning on IFC Q&A, RAG on defect cases | 6 | "AIに『3〜10階に同じ部屋割りを作って』と頼めるか" | [MCP servers and AI tools](../../04_open_source/mcp_servers_and_ai_tools.md) |
| 7 | **Viewers and large files**: browser viewers (web-ifc, Three.js), glTF conversion, lazy loading, ETL to Parquet/DuckDB, free tools for site staff | viewers 5 + size 4 | "IFCを少し見るだけで数GBのソフトが必要" | [File size, viewing, conversion](../by_topic/file_size_viewing_conversion.md) |
| 8 | **Versions and MVD**: IFC2x3 still dominant in practice; IFC4/4.3 coexistence; web-ifc support for IFC4X3 | 5 | "IFC2x3が主流らしい" | [Versions, MVD, encoding, GUID](../by_topic/versions_mvd_encoding_guid.md) |
| 9 | **Cheap and open-source tooling** for small offices (Bonsai, FreeCAD, BIMvision, BIMCraft) vs expensive licences | ~4 | "ソフトを買う根拠がない" | [Open-source community](../../04_open_source/community_projects_and_enthusiasts.md) |
| 10 | **Quantities and estimating (積算)** from IFC; BIM/CIM; room, area and unit consistency | ~4 | "モデル化されない部材の数量ルールは？" | [Quantities, cost, schedule](../by_topic/quantities_cost_schedule.md) |
| 11 | **Revit API and GUID**: UniqueId vs IFC GlobalId; converting imported IFC to native MEP elements (failure story) | 5 | "IFCをMEP要素へ変換するアドインを作ろうとしてできなかった話" | [Programming and automation](../by_topic/programming_and_automation.md) |
| 12 | **Certification**: IFC検定 (for software), BIM利用技術者 (for people) | 2 | "IFC検定とは？" | [buildingSMART standards](../../02_standards_regulations/buildingsmart_standards.md) |

Personas among the real pages: developers 13, students 8, architects 6, BIM managers 5; coordinators, reviewers and site staff 2-3 each. The synthetic prompts add estimators, MEP and structural engineers.

## Local ecosystem

| Item | What it is | Source / caveat |
|---|---|---|
| **MLIT (国土交通省)** and the **建築BIM推進会議** | Ministry-led programme. The BIM図面審査 (BIM drawing review) for building permits started 2026-04-01; the guideline's first edition is dated 2026-03-24 with 入出力基準, 誓約書 and 確認申請図書表現標準 annexes | [Japan national doc](../../02_standards_regulations/national/japan_korea.md). MLIT PDFs themselves were not text-readable in the research run |
| **BIMデータ審査** | The later IFC-based phase. A 2026-09 basic concept is reported; "spring 2029" appears in note.com explainers and a vendor page. Reported first review items: lighting/ventilation, floor-area ratio, building coverage, oblique-line limits (about 10 items); structure and energy under study | `ja-japan-r016`, `ja-japan-r017`. Official wording **not verified**; do not write tests that depend on exact dates |
| What the applicant submits now | Per the explainer records: permit application + BIM-exported PDF + simultaneously exported IFC + a compliance pledge; the IFC is *not* the review object in this phase | `ja-japan-r016` (secondary source) |
| **buildingSMART Japan (bSJ)** and **IFC検定** | IFC検定 verifies *software* against an MVD (not an exam for people); results are published. People-side certificate: buildingSMART professional certification | `ja-japan-r031`; national doc |
| **BIM利用技術者** (ACSP) | Skills exam; practical tasks follow the permit flow including drawing extraction, area calculation and IFC + drawing submission; IFC2x3 from FY2026 | `ja-japan-r022` |
| Local software | GLOOBE Architect and ARCHITREND ZERO (福井コンピュータ), Jw_cad, Vectorworks, Archicad, Revit (with the "J tool" IFC2X3 add-in), Rebro for MEP (IFC support not confirmed); free viewers BIMvision, Autodesk Viewer | [Authoring tools](../../03_software/authoring_tools_ifc.md), [viewers](../../03_software/viewers_checkers_cde_converters.md) |
| Civil / infrastructure | MLIT BIM/CIM (NILIM portal), J-LandXML (not IFC), 土木基本IFC検定; PLATEAU 3D city models (CityGML) are used by GIS people | national doc; `ja-qiita-r035` |
| Open source and tooling | IfcOpenShell (`IfcCsv`, `IfcTester`, `IfcDiff`, `IfcClash`), Bonsai, web-ifc, Three.js, Babylon.js, FreeCAD, BIMCraft (personal Rust app) | [Libraries](../../04_open_source/libraries_and_toolkits.md) |
| Companies and enthusiasts visible in records | ONESTRUCTION (openBIM, bSDD essays), Obayashi and Maeda (IFC to estimating), as named in the research report, many individual Zenn/Qiita authors writing IfcOpenShell notes | `research_raw/wave1/ja/ja-japan.md` |
| Subsidy context | 建築GX・DX推進事業 mentioned by a small MEP office; MLIT 建築BIM加速化事業 | `ja-japan-r025`, national doc |

## How people write

### Register and structure

- **Zenn / Qiita:** terse and code-first. Plain form (だ/である) or simple です/ます. Scraps are chronological notes with failures and "よく分からない" left in. Titles often state the action: `〜を取得する`, `〜を比べた検証ログ`, `〜を作った話`.
- **note.com:** first-person, polite です/ます, sections marked with `■`, hedged claims (`〜と思います`, `〜かもしれません`), invitations to correct errors. Titles can be full sentences with `｜` separators: `確認申請の「図面の突き合わせ」が変わった｜2026年4月の…`.
- **Pain statements as fragments:** `IFCに出したら、半分なかった`, `IFCは万能ではありません`, `Attributeしか書き出せないので…`.
- **Closers:** rare; essays end with a call for feedback. Synthetic prompts to an assistant use `〜して`, `〜出して`, `〜教えて` (casual) or `〜してください` / `〜できますか` (polite).

### Jargon and slang

| Term | Meaning | Standard / English |
|---|---|---|
| 確認申請 | building permit application | building confirmation application |
| BIM図面審査 / BIMデータ審査 | drawing review from a BIM model / review of the BIM data itself | MLIT permit phases |
| 入出力基準 | input/output criteria for BIM-based permit submission | MLIT annex |
| 意匠 / 構造 / 設備 | architectural design / structure / MEP (building services) | discipline names (意匠IFC = architect's IFC) |
| 元請 / 協力会社 | general contractor / partner subcontractor | main contractor / subcontractor |
| 施工前検討会 | pre-construction review meeting | constructability review |
| 納品IFC / 納品 | IFC delivered to the client | IFC deliverable |
| 野良データ | "stray" data: unmanaged, inconsistent files | uncontrolled data |
| 軽量化 | make a model or file lighter | decimation / lightweight format |
| 干渉チェック | clash check | clash detection |
| 属性 / プロパティ / プロパティセット | attribute / property / property set | IFC attribute, property, Pset |
| 書き出し / 読み込み / リンク | export / import / link | export, import, link IFC |
| 壁芯 / 1間 | wall centre-line / the traditional 1-ken span (about 1.82 m) used in Japanese drafting | Japanese drafting conventions that Bonsai trials stumbled on |
| 積算 | cost estimating, quantity takeoff | QTO |
| スリーブ / 吊りボルト | sleeve / hanger rod | MEP penetration / support items |
| 型枠 | formwork | formwork area |
| 文字化け | mojibake | encoding error (`\X2\...\X0\`) |
| 遅延読み込み | lazy loading | IfcOpenShell `lazy=True` |

### Name variants and spelling

- Tool names are Latin and inconsistent: `IfcOpenShell`/`ifcopenshell`, `Archicad`/`ARCHICAD`, `Revit`; `Jw_cad`, `GLOOBE`, `Bonsai` (formerly BlenderBIM), `web-ifc`, `Three.js`.
- IFC entity names are copied in Latin, sometimes in upper case as they appear in the STEP file (`IFCBUILDINGSTOREY`, `IFCCOLUMN`), and by beginners wrongly typed into code.
- UI terms follow the Japanese Revit UI in katakana (the glossary lists ファミリ, プロジェクト基準点, 測量点, 共有パラメータ). See the [multilingual glossary](../../08_glossary/glossary_multilingual.md).
- Mixed width: full-width `（）` and `｜` in titles, half-width in code; emoji appear in some Zenn titles.

### Code-switching

Heavy. Katakana loanwords (ファイル, プロパティ, ビューア, ダイアログ), English acronyms (IFC, IDS, BCF, bSDD, MVD, CDE, LOD), and **entity/attribute names unchanged** (`IfcBuildingElementProxy`, `FlangeSlope`, `assign_container`, `Qto_SpaceBaseQuantities`). Explanations use analogies for IT readers ("IFCはUSB Type-C、BCFはGitHub Issues、IDSはlinter").

### Tone

Mostly neutral or curious (real: neutral 19, curious 14, frustrated 6, skeptical 3, confused 3, worried 1). Frustration is understated and located in the situation (`重いアプリを起動`, `人力`), almost never in insults. Synthetic prompts include 11 with a polite tone, which matches the polite です/ます note.com voice but is not directly observed in help requests.

### Context given and omitted

| Usually given | Usually omitted |
|---|---|
| Software names (Revit, Archicad, Vectorworks, IfcOpenShell version), a code snippet or error, numbers (400 MB, 393 MB to 1.4 s), the purpose (確認申請, 積算, 施工前検討会) | IFC schema version (unknown in 26 of 47 pages), the exact software version, whether the model is architecture or MEP, the viewer used |

## Real questions

Problem statements and titles in the original, with an English gloss, persona, tone and source. Each page appears once.

### 1. Building permit and policy (確認申請, BIM図面審査, BIMデータ審査, certification)

| ID | Original (title; paraphrase where it adds something) | English gloss | Persona · tone | Source |
|---|---|---|---|---|
| `ja-japan-r016` | 確認申請の「図面の突き合わせ」が変わった｜2026年4月のBIM図面審査と、2029年春のBIMデータ審査 — BIM図面審査では確認申請書+BIM書き出しPDF+同時書き出しIFC+誓約書を提出。IFCは審査対象外。AIはどこまで入る？ | BIM drawing review (Apr 2026) vs BIM data review (spring 2029): what is submitted and how IFC is used | reviewer_authority · curious | [note](https://note.com/kensesu_ai/n/nee08ddde31f1) (blog, 2026) |
| `ja-japan-r017` | BIMデータがそのまま審査対象に。2029年春スタートの新制度を整理してみた — 国交省の基本構想では採光・換気、容積率、建蔽率、斜線など約10項目から。構造・省エネは検討中 | MLIT 2029 BIM data review: view review vs digital review, initial ~10 review items | reviewer_authority · neutral | [note](https://note.com/ken_newslab/n/n9d7072936346) (blog, 2026) |
| `ja-japan-r019` | 2029年のBIMデータ審査に備えるなら、まず一室を「書き出して読む」 — 部屋名・用途・床面積がIFCに出て別ビューアで読めるか。面積が合わない時は境界・計算方法・単位・版を確認 | Prepare for 2029 data review by exporting one room to IFC and re-reading it in another viewer | architect · neutral | [note](https://note.com/t_note_memo/n/n8903305b00fb) (blog, 2026) |
| `ja-japan-r020` | 建築BIM：国交省の2029年春審査、BIMCraftは使えるか — 個人開発のBIMCraft(MCP/CLI操作可)は審査用IFCに使えるか。RVTは読み取りのみ、カーテンウォールや階段は未対応 | Can the free Rust BIM app BIMCraft handle the 2029 review IFC? Reads IFC2x3/IFC4, writes IFC4 | owner_client · curious | [note](https://note.com/legal_tiger6680/n/n6781ba815061) (blog, 2026) |
| `ja-japan-r022` | BIM利用技術者とは？｜「未来の建築確認に直結する資格」になる？ — 準一級・一級の実技で、審査フローに沿ってモデル作成、図面抽出、面積算定、IFCと図面の提出 | BIM利用技術者 exams: practical tasks include submitting IFC with drawings; IFC2x3 from FY2026 | student_beginner · curious | [note](https://note.com/aei830/n/ndfa486486036) (course, 2026) |
| `ja-japan-r031` | IFC検定とは？ — 検定対象ソフトはMVDに合致する必要。結果は管理台帳とサイトで公表 | buildingSMART Japan IFC certification (IFC検定): software must conform to an MVD | vendor_support · neutral | [bSJ](https://www.building-smart.or.jp/ifc/whatsifcverifi/) (official_doc, 2023) |

### 2. IFC limits and export problems

| ID | Original (title; paraphrase where it adds something) | English gloss | Persona · tone | Source |
|---|---|---|---|---|
| `ja-japan-r015` | IFCに出したら、半分なかった。3Dの箱と、壁ツールの壁は別物です — IFCに書き出したらモデルの半分が消えていた。ただのソリッド、階に紐づかないレイヤ、非表示要素が原因 | After IFC export about half the elements were missing | architect · frustrated | [note](https://note.com/toshio_nakamura/n/nc8db42ce3191) (blog, 2026) |
| `ja-japan-r018` | BIMを解く #09―IFCは万能なのか — Rhinoで作ったモデルをIFCに出して確認申請用BIMや引き渡しに使えるのか。見た目は合っていても分類や属性が使えない | IFC is not omnipotent: editing, live links and classifications are lost; creating IFC is not the same as delivering information | bim_manager · skeptical | [note](https://note.com/bim_tool_lab/n/nf529aa5d5cc0) (blog, 2026) |
| `ja-japan-r021` | IFCとは何か？BIM実務で「期待がズレやすい理由」と正しい使い方 — IFCにすれば別ソフトで編集を続けられると思われがち。実際はパラメトリック関係や独自パラメータが落ちる | Why expectations of IFC drift from reality: sharing not exchange; loss of parametrics; IFC2x3/4/4.3 coexist | bim_manager · neutral | [note](https://note.com/onestruction/n/ne8322e3be44d) (blog, 2026) |
| `en-gh-encoding-r015` | IFC file fails to load due to invalid string | File with Japanese \X2\ text and a doubled backslash loads only 10 of 78 products. | developer_programmer · polite | [GitHub](https://github.com/xBimTeam/XbimEssentials/issues/605) (github_issue, 2025) |
| `en-gh-encoding-r029` | Error when style references to an external material | Browse External Style fails when the external material name is Japanese. | architect · neutral | [GitHub](https://github.com/IfcOpenShell/IfcOpenShell/issues/6496) (github_issue, 2025) |

### 3. openBIM, IDS, validation and learning

| ID | Original (title; paraphrase where it adds something) | English gloss | Persona · tone | Source |
|---|---|---|---|---|
| `ja-japan-r003` | IFCデータを正しく運用する為のIDSの威力とは？ — 発注者の要求がExcelやPDFでバラバラで、納品IFCのチェックが人力。IDSで機械的に検証できる？ | What power does IDS give for operating IFC correctly (clients checking contractor IFC automatically)? | bim_manager · curious | [Zenn](https://zenn.dev/miyamiyaumya/articles/6714ef2c6e2c6c) (blog, 2023) |
| `ja-japan-r005` | 情報系のためのopenBIM入門 — IT出身者向けに、IFCはUSB Type-C、BCFはGitHub Issues、IDSはlinterのようなものと説明 | Intro to openBIM/IFC/BCF/IDS/LOD for IT people using software analogies | student_beginner · curious | [Zenn](https://zenn.dev/mikan_atomoki/articles/ea27c5466ff71f) (blog, 2026) |
| `ja-japan-r026` | openBIM ワークフローについて — 全てのopenBIMはbSDDから始まる、というワークフロー整理 | openBIM workflow centered on bSDD with IFC, IDS, BCF, openCDE | bim_manager · neutral | [Zenn](https://zenn.dev/miyamiyaumya/articles/fc19330aa071ba) (blog, 2024) |
| `ja-japan-r029` | Open BIM・OpenCDE・IFC・BCFとは？BIM初心者でも分かるデータ連携の基本 — IFCにしても同じ結果になるとは限らない。BCFで梁とダクトの干渉を共有 | Beginner explanation of Open BIM, OpenCDE, IFC, BCF; converting to IFC does not guarantee identical results | student_beginner · curious | [note](https://note.com/hip_sedum1639/n/n14c9af7dd03e) (blog, 2026) |
| `en-val-r029` | Information Delivery Specification (IDS) をゆるく説明する | A casual explanation of IDS: rules for checking IFC data, eight rule patterns, six facets | student_beginner · curious | [Qiita](https://qiita.com/kiyuka/items/62e30208c035e828714b) (blog, 2025) |
| `ja-japan-r007` | IFC Validation Service をローカルで動かす — 公式手順どおりmake startしたらhttp://localhostがエラー、backendとworkerが再起動を繰り返す | Running buildingSMART IFC Validation Service locally in Docker: workers restart, uploads never process | developer_programmer · frustrated | [Zenn](https://zenn.dev/kiyuka/scraps/e07bf799384b52) (blog, 2026) |
| `p-student-r031` | BIMを表現するためのIFCファイルについて調べてみた — BIMのデータがIFCでどう表現されるのか調べてみた。STEP形式で書かれていて、IFC2x3が主流らしい。 | Looked into IFC files that represent BIM | student_beginner · neutral | [Qiita](https://qiita.com/msp0310/items/0d7966a93ff380e11970) (blog, 2023) |
| `p-student-r032` | IFC勉強会に参加してきた — 初のIFC勉強会に参加。IFCは3Dモデルより情報モデリングが大事という話が印象的。IFC4.3で土木にも広がる。 | Attended the first IFC study session | student_beginner · curious | [Qiita](https://qiita.com/ktaroabobon/items/25349c7fa7bdb55c63b8) (blog, 2022) |
| `ja-roundtrip-r032` | IFCファイルの中身を解読する | Decoding an IFC file; IFC is used as the intermediate format between Archicad and Revit. | student_beginner · curious | [Qiita](https://qiita.com/kiyuka/items/00434f1b8e0b38c621fb) (blog, 2022) |
| `ja-japan-r008` | IFCのデータの紐づけ構造を理解したい — IFCを可視化できたが形状や属性がどこにどんな形式で入っているのか分からない | Wants to understand where geometry, attributes and relations live in IFC and how entities link | developer_programmer · confused | [Zenn](https://zenn.dev/kiyuka/scraps/48157a38db558e) (blog, 2024) |
| `ja-japan-r006` | IFCのProfileDefのSlopeの解釈が知りたい — IfcIShapeProfileDefのFlangeSlopeは正の値でどっち向き？基準位置はフランジのどこ？公式は説明が少ない | Interpretation of FlangeSlope in IfcIShapeProfileDef: sign and reference position are unspecified | researcher_academic · confused | [Zenn](https://zenn.dev/kiyuka/scraps/2894037aa4f997) (blog, 2026) |

### 4. IfcOpenShell, Revit API and code

| ID | Original (title; paraphrase where it adds something) | English gloss | Persona · tone | Source |
|---|---|---|---|---|
| `ja-japan-r001` | IFCのAttribute、PropertySet、Materialを一式書き出す — IfcOpenShellのIfcCSVだとAttributeしか書き出せないので、PropertySetとMaterialも一緒にExcelへ出したい | IfcCSV only exports attributes; how do I dump attributes, property sets and materials of an IFC to Excel? | bim_coordinator · neutral | [Zenn](https://zenn.dev/miyamiyaumya/articles/19a4247133dde6) (blog, 2024) |
| `ja-japan-r002` | IfcOpenShellで階情報を取得する — IFCファイルから階の名前と高さ(Elevation)をIfcOpenShellで取り出したい | How to get the storey names and elevations from an IFC with IfcOpenShell | developer_programmer · neutral | [Zenn](https://zenn.dev/cote2/articles/6459c1c44091da) (blog, 2023) |
| `ja-japan-r027` | ゼロから始めるPythonとIfcOpenShellでのBIM/3D建築モデル作成入門 建築編 — assign_containerを忘れると床が表示されない。開口を作ってからドア窓をadd_filling | Create floors, walls, a door and a window from scratch with IfcOpenShell: units, placement, containment, opening order | developer_programmer · neutral | [Zenn](https://zenn.dev/toggle_inc/articles/cf8df02f7b4ba7) (blog, 2025) |
| `ja-japan-r028` | IfcOpenShellのインストール及び使い方 — GitHubのZipを解凍しifcopenshell等をsite-packagesへコピー。by_type('IfcColumn')で柱名を一覧 | Installing IfcOpenShell by copying folders to site-packages and listing IfcColumn names; bundled tools (IfcTester, IfcCsv, IfcDiff, IfcClash) | student_beginner · confused | [Zenn](https://zenn.dev/miyamiyaumya/articles/909be24ee185ac) (blog, 2024) |
| `ja-japan-r011` | IfcOpenShell の遅延読み込み — 大きいIFCを開くと全インスタンス・属性を先にパースして遅くメモリを食う | Opening huge IFC with IfcOpenShell is slow and memory-hungry; lazy loading in 0.9.0 | developer_programmer · neutral | [Qiita](https://qiita.com/kiyuka/items/0d2ef739a0d34606a52f) (blog, 2026) |
| `ja-coord-r014` | Revit のUniqueIdとIFC のGUIDとの変換 | How Revit converts UniqueId to IFC GlobalId so that elements can be matched across Revit and IFC. | developer_programmer · curious | [Qiita](https://qiita.com/Takashi_Kasuya/items/97899d15e7ec0186eecf) (blog, 2019) |
| `ja-coord-r015` | IFCをMEP要素へ変換するアドインを作ろうとしてできなかった話 | Story of trying to build an add-in converting imported IFC elements into native Revit MEP elements and failing. | bim_coordinator · frustrated | [Qiita](https://qiita.com/KengoTanaka-BIM/items/6cec74e04bf581b21cf5) (blog, n.d.) |
| `ja-coord-r016` | IFC のデータ構造を可視化する「IFC graph viewer」を作ったよ | Tool that visualizes IFC data structure as a graph so people understand entity relations. | developer_programmer · curious | [Qiita](https://qiita.com/kiyuka/items/116f29df6a4e91d062ae) (blog, n.d.) |
| `en-spaces-r037` | IFCのモデルをplotlyで表示する | Displaying IFC models in plotly, excluding room info and openings. | developer_programmer · neutral | [Qiita](https://qiita.com/kiyuka/items/ef4b197fa28d3a96d068) (blog, 2024) |

### 5. Viewers, large files and conversion

| ID | Original (title; paraphrase where it adds something) | English gloss | Persona · tone | Source |
|---|---|---|---|---|
| `ja-japan-r009` | IFCをglTFに変換する — IFCをglTFにして階層構造(Project>Site>Building>階>要素)も残したい。IfcOpenShellは遅い | Convert IFC to glTF keeping the spatial hierarchy; IfcOpenShell slow, web-ifc fast but glTF export unsolved | developer_programmer · frustrated | [Zenn](https://zenn.dev/kiyuka/scraps/a054a249f42a93) (blog, 2024) |
| `ja-japan-r012` | web-ifc 13 バージョンを同じ IFC で比べた検証ログ（0.0.50〜0.0.78） — web-ifcを上げる前に何が変わるか。0.0.50はIFC4X3_ADD2でUnsupported Schema、0.0.78のブラウザ版StreamMeshesでBindingError | Comparing 13 web-ifc versions on the same IFC: unsupported IFC4.3 in old versions, geometry count changes, StreamMeshes BindingError in 0.0.78 | developer_programmer · neutral | [Zenn](https://zenn.dev/grok_prtex/articles/webifc-version-compare) (blog, 2026) |
| `ja-japan-r013` | WebAssembly × Three.js でブラウザ完結の無料 IFC ビューアを作った話 — IFCを少し見るだけで数GBのソフトが必要。現場担当は開く環境がなく設計変更のたび重いアプリを起動 | Site staff cannot open IFC without multi-GB software; built a browser-only IFC viewer with clash check | contractor_site · frustrated | [Zenn](https://zenn.dev/kazuyamaeda/articles/97933cdafce6d8) (blog, 2026) |
| `ja-japan-r014` | BIMデータをETLしよう - OLAP向けにEAVで正規化して列指向に保存する理由 — 協力会社の重いモデルや古いモデルを開かずに値だけ取り出したい。API/プラグイン経由は遅くAPSは組織整備が前提 | Extract values from heavy Revit models from subcontractors without opening them; ETL to columnar store | developer_programmer · frustrated | [Zenn](https://zenn.dev/tomosandego/articles/59e6cf8dfe60bc) (blog, 2025) |
| `ja-japan-r030` | Revit｜ファイルを軽量化する方法 — 管理タブの未使用の項目を削除を繰り返し、CAD読込・点群・ビューを先に削除 | Reduce Revit file size by purging unused items; 222MB to 200MB | bim_coordinator · neutral | [Zenn](https://zenn.dev/malme/articles/2bfe2ffb1da08b) (blog, 2025) |

### 6. Small offices, free tools, estimating

| ID | Original (title; paraphrase where it adds something) | English gloss | Persona · tone | Source |
|---|---|---|---|---|
| `ja-japan-r023` | オープンソースBIM Bonsai(Blender BIM)は実務に使えるか？ — 年42万〜138万円の商用BIMに対し無料で。壁が芯でなく面基準、ハッチング、1間引き違い戸が作れない | Is open-source Bonsai usable for Japanese practice? Walls on face not 壁芯, hatches, sliding-door presets | architect · curious | [note](https://note.com/akram/n/n8a6e9c5602ca) (blog, 2026) |
| `ja-japan-r025` | 小さな設備設計事務所のためのBIM入門 — Jw_cadで2D図面。元請から意匠IFCを受けて設備ルートを3D確認したい。ソフトを買う根拠がない | Small MEP office on Jw_cad: how to prepare for BIM cheaply, view architect IFC for free | mep_engineer · worried | [note](https://note.com/limber_stork5044/n/n68df8d5a268b) (blog, 2026) |
| `ja-qiita-r036` | BlenderでBIMをいじって安価に施設を管理する（Bonsai） | Managing facilities cheaply with Blender and Bonsai instead of Revit. | facility_manager · neutral | [Qiita](https://qiita.com/watanabe-tsubasa/items/bcd3cfbd7dc653a580b5) (blog, 2025) |
| `ja-japan-r024` | BIMを活用した積算業務 ── 数量算出の仕組みから導入の勘所まで — 図面から数量を拾うのが時間と精度の両立が難しい。モデル化されない部材の数量ルールは？ | BIM-based quantity takeoff: reading IFC from ArchiCAD for estimating; unmodeled members need rules | estimator_qs · neutral | [note](https://note.com/bold_cobra9180/n/n4f52d62f230f) (blog, 2026) |

### 7. AI, MCP and LLM

| ID | Original (title; paraphrase where it adds something) | English gloss | Persona · tone | Source |
|---|---|---|---|---|
| `ja-japan-r004` | 意匠設計者のためのRevit-MCP解説：AIとRevitの連携で設計業務を効率化 — AIに『3〜10階に同じ部屋割りを作って』『窓幅を一括変更』『20m2未満の部屋を赤に』と頼めるか | Explainer for architects: using Revit-MCP so AI can create/modify Revit elements in natural language | architect · curious | [Zenn](https://zenn.dev/yuichi_ai/articles/879de49ee8e1bb) (blog, 2025) |
| `ja-japan-r010` | Claude CodeでRevitアドインを自律的に開発できるようにした話 — Revitのエラーはダイアログに隠れてエージェントが結果を見られない。DLLロックやPDB無しで行番号が出ない | Letting Claude Code build Revit add-ins autonomously; MCP found a poor fit versus running C# in the live model | developer_programmer · skeptical | [Zenn](https://zenn.dev/aec/articles/58aa31c1089332) (blog, 2026) |
| `ja-aimcp-r034` | ifc-bim-llm-finetuning — 建物の設計データに関する質問に答えられるよう、AIモデルを追加学習させた実験 | Fine-tuned a small model on 42,680 IFC Q&A examples; errors remain: confusing WHERE rules, mixing attribute names, repetition, wrong general answers. | researcher_academic · skeptical | [GitHub](https://github.com/matsuokakoki/ifc-bim-llm-finetuning) (paper, 2026) |
| `ja-aimcp-r041` | revit-mcp-toolkit README — 日本独自の基準・法規に沿った運用設計 | Japanese Revit MCP aims at operations under Japanese standards like the Building Standards Act; schedules via HTML/Excel round trip. | bim_manager · neutral | [GitHub](https://github.com/okuno-dsi/revit-mcp-toolkit) (official_doc, 2026) |
| `ja-data-r035` | 施工前検討会で過去の不具合事例を参照する：IFC部位情報×構造化ナレッジRAGのデモ — クリックした部材のプロパティからAIがタグを生成し、過去の不具合事例を検索して原因と対策を表示する。 | Demo where clicking an IFC element in a browser viewer fetches its properties, generates semantic tags with AI and matches them to a structured defect-report knowledge b… | contractor_site · curious | [Qiita](https://qiita.com/dnp-hiraoka/items/aa1d12e5784485542583) (blog, 2026) |

### 8. GIS and 3D city models

| ID | Original (title; paraphrase where it adds something) | English gloss | Persona · tone | Source |
|---|---|---|---|---|
| `ja-qiita-r034` | 3D都市モデルのCityGMLの現在とこれから — CityGMLを都市シミュレーションのデータとして使う論文紹介、CesiumJSにも言及 | Present and future of CityGML 3D urban models, simulations, CesiumJS, i-UR, smart city. | researcher_academic · neutral | [Qiita](https://qiita.com/tosseto/items/34a2a801b8eb299453d1) (blog, 2020) |
| `ja-qiita-r035` | _PLATEAU_のCityGMLをArcGISで表示する — PLATEAUのCityGMLをArcGISで表示できる形式に変換する手順 | How to display PLATEAU CityGML in ArcGIS with a conversion workspace. | architect · neutral | [Qiita](https://qiita.com/masumur/items/8362a1ed91048e26ed2a) (blog, 2021) |

*Real questions listed: 47 distinct pages.*

## Ready test prompts

All prompts below are **synthetic**. IDs like `ja-japan-s001` come from the research cells; IDs starting `JA-X` are rewrites for this file. "Needs model" means an IFC (or Revit project) is assumed to be loaded. Review-related prompts must never lead the assistant to claim official acceptance for 確認申請: it can only report what the file contains. The KB's own national document says the exact IFC version and MVD required by the 入出力基準 are **not verified**, so a good answer reads the file's `FILE_SCHEMA` and says so.

Registers: casual (`出して`, `教えて`, `〜いい？`), polite (`〜してください`, `〜できますか`), and frustrated fragments (`半分くらい要素が無い…`).

### A. Permit preparation and checks

| ID | Prompt (synthetic) | Intent · difficulty · file | Expected behavior (EN) |
|---|---|---|---|
| `ja-japan-s002` | 確認申請用に出したIFCの全IfcSpaceについて、部屋名・用途・床面積が入ってるか確認して。抜けてる部屋は一覧で<br>*EN: For BIM drawing review check each IfcSpace has a name, usage and floor area* | validate_check · medium · needs model | List IfcSpace, check Name/LongName, usage property and Qto_SpaceBaseQuantities NetFloorArea, report missing ones with GlobalId and storey. **Note:** Do not claim the file satisfies the BIM図面審査 入出力基準; report presence of name, use and area per space only. |
| `ja-permit-s010` | 確認申請用のIFCです。居室の天井高が2.1m未満の部屋と面積を一覧にしてください<br>*EN: Check ceiling height for building confirmation* | validate_check · medium · needs model | List IfcSpace with height and area, filter by 2.1 m, tabulate. **Note:** The 2.1 m threshold is the user's; the assistant should state it used that value and that official rules should be checked. |
| `ja-japan-s015` | 防火区画に関係する壁と床の耐火時間が入っているか、IsExternalと一緒に確認して<br>*EN: Check fire-compartment related properties on walls and slabs for permit review* | validate_check · medium · needs model | Collect IfcWall/IfcSlab, read FireRating and IsExternal from Pset common, report missing or inconsistent. |
| `ja-japan-s005` | うちのIDSで納品IFCをチェックして。壁にFireRatingが入ってないものと、PredefinedType未設定のものを出して<br>*EN: Check against our IDS that every wall has FireRating and report failures* | validate_check · medium · needs model | Run or emulate IDS facets (Entity IfcWall, Property Pset_WallCommon.FireRating, PredefinedType attribute), list failing elements. |
| `ja-japan-s010` | IFCの面積がRevitの集計表と合わない。単位か境界の問題？部屋ごとに差を出して<br>*EN: Room area in IFC differs from the Revit schedule; check units and boundary* | query_model_data · medium · needs model | Report project length unit and area unit, compare Qto NetFloorArea vs GrossFloorArea per space, list rooms with differences. |
| `ja-gis-s016` | このIFC、平面直角座標系の設定入ってる？なければ座標系と原点のずれ確認して<br>*EN: Check Japanese plane rectangular coordinate settings.* | validate_check · medium · needs model | Check IfcProjectedCRS for Japan plane rectangular CRS, report map conversion and offset. |
| `mul-coord-s015` | 平面直角座標系の第9系でIFC出力したら原点からめちゃ遠い、どう直す？測量点と基準点の違いも<br>*EN: Plane rectangular CRS zone IX IFC export far from origin; survey point vs base point* | troubleshoot_export · medium · no file | Explain Japan Plane Rectangular CS (EPSG:6677), shared coordinates, and moving origin/offset on export. |

### B. Export mapping, missing elements, versions

| ID | Prompt (synthetic) | Intent · difficulty · file | Expected behavior (EN) |
|---|---|---|---|
| `ja-japan-s001` | このIFC、IfcBuildingElementProxyが何個あるか数えて、元のRevitカテゴリ別に集計して。マッピング直す対象知りたい<br>*EN: Count proxy elements and which Revit categories they came from* | query_model_data · medium · needs model | Count IfcBuildingElementProxy, group by ObjectType/Revit category property, report counts, suggest IfcExportAs mapping fixes. |
| `ja-japan-s003` | IFCに出したら半分くらい要素が無い…Revitの元モデルと比べて何が落ちてるか調べて。階に紐づいてないやつとか<br>*EN: Half of the elements are missing in the IFC; find out why* | troubleshoot_export · hard · needs model | Compare element counts per category/class vs expectation, find elements not contained in any IfcBuildingStorey, report likely causes (visibility, level, category mapping). |
| `ja-proxy-s008` | IfcBuildingElementProxyになってる要素の中で、柱っぽいもの(縦長のやつ)を洗い出して、IfcColumnにすべきか教えて<br>*EN: List proxies that look like columns by geometry* | query_model_data · hard · needs model | Analyze proxy bounding boxes, flag tall slender ones as column candidates, suggest IfcColumn with caveats. |
| `ja-mep-s012` | Revitの吊りボルトとサポートをIFCに出したいけど、クラスはどれが正解？<br>*EN: Export hangers and supports* | how_to · medium · no file | Recommend IfcDiscreteAccessory (or IfcPipeSegment-adjacent support classes) via export class mapping, avoiding IfcBuildingElementProxy; explain how to set IfcExportAs on the family. |
| `ja-japan-s017` | 材料が付いてない壁をタイプ別に出して。レイヤ構成も無いやつ<br>*EN: Find walls with no material assigned and list them by type* | modify_model_data · easy · needs model | For IfcWall check IfcRelAssociatesMaterial (IfcMaterialLayerSetUsage), list missing by type. |
| `ja-vm-s012` | このIFCのFILE_SCHEMAとエクスポートしたRevitのバージョン教えて<br>*EN: Show FILE_SCHEMA and which Revit exported it* | query_model_data · easy · needs model | Return FILE_SCHEMA, header application/preprocessor, exporter version. |
| `ja-roundtrip-s014` | ArchicadのIFC、クラス別の数をだして。Revitに入れたときカテゴリがどうなるか知りたい<br>*EN: List IFC classes and counts to predict Revit categories.* | query_model_data · medium · needs model | Count by IFC class, map to likely Revit categories, flag generic ones. |
| `ja-japan-s013` | IFCをRevitで開くと属性が全然出てこない…リンクとか開くとか何が違う？<br>*EN: IFC opens in Revit but properties and parameters are missing* | troubleshoot_import · medium · no file | Explain Open vs Link IFC, parameter mapping, IFC version/MVD, how to check Pset presence in file. |

### C. Counting, quantities, equipment and FM

| ID | Prompt (synthetic) | Intent · difficulty · file | Expected behavior (EN) |
|---|---|---|---|
| `ja-aimcp-s013` | 階ごとの柱と梁の数を出して、断面サイズ別に集計して<br>*EN: List columns and beams by level* | query_model_data · medium · needs model | Count IfcColumn/IfcBeam per storey, group by profile. |
| `ja-japan-s004` | 積算用に、階ごとのRC壁・柱・梁のコンクリ体積を合計して。Qtoが無いものは形状から出せる？<br>*EN: Total concrete volume of walls, columns and beams by storey for estimating* | extract_quantities · hard · needs model | Aggregate NetVolume from Qto per IfcWall/IfcColumn/IfcBeam by storey and material, flag elements missing Qto and say whether geometry-derived values are available. |
| `ja-japan-s007` | 設備IFCの空調ダクトをシステム名別・階別に本数と合計長さでまとめて<br>*EN: List ducts per system and their storey* | query_model_data · medium · needs model | Collect IfcDuctSegment, group by IfcSystem membership and containing storey, sum Length quantity, report ungrouped. |
| `ja-japan-s012` | 鉄骨の梁をプロファイル別に本数と重量集計して。H-400x200とか<br>*EN: List steel beam profiles and total weight* | query_model_data · medium · needs model | List IfcBeam with IfcIShapeProfileDef, group by ProfileName, sum weight from quantities or computed, flag missing. |
| `ja-struct-s015` | このIFCの鉄筋、径ごとの本数と総延長を出してもらえますか<br>*EN: Count rebar by diameter and total length* | query_model_data · medium · needs model | Group IfcReinforcingBar by NominalDiameter, count, sum length. |
| `ja-qto-s015` | 部屋ごとの床面積と壁の面積を拾って、積算用の表にしてほしい<br>*EN: Floor area per room for takeoff* | extract_quantities · medium · needs model | List IfcSpace with net floor area and wall areas per space, output table, flag spaces missing quantities. |
| `ja-japan-s011` | 維持管理用に、機器の名称・メーカー・型番・設置階と室をExcelに出して。空欄の項目も分かるように<br>*EN: Export equipment list with maker, model number and install location to Excel* | extract_quantities · medium · needs model | Query IfcDistributionElement/IfcFlowTerminal, read manufacturer/model properties, containing storey and space, write table, mark blanks. |
| `ja-cobie-s014` | 部屋ごとの設備一覧を出して。型番とメーカーも。FM台帳に入れたい<br>*EN: List equipment per room for the facility management ledger.* | query_model_data · medium · needs model | Group equipment by IfcSpace; include model number and manufacturer; list items without room. |
| `ja-data-s014` | 大梁を階ごとに一覧にして、断面とスパンと材料も出して。施工前検討会で使いたい<br>*EN: List main beams by level with section and span for pre-construction review* | query_model_data · medium · needs model | List IfcBeam by level with profile, length/span and material, output table, state missing values. |
| `mx-mcl-s008` | 壁ごとの材料レイヤーと厚みを一覧にして、レイヤー無い壁はどれか教えて<br>*EN: List layer thickness per wall* | query_model_data · medium · needs model | For each wall read IfcMaterialLayerSet layers with names and thickness; list walls without layers. |

### D. Clash, comparison, GUID and classification

| ID | Prompt (synthetic) | Intent · difficulty · file | Expected behavior (EN) |
|---|---|---|---|
| `ja-japan-s006` | 先週のIFCと今日のIFC比べて、追加・削除・変更された部材をGlobalIdベースで出して。変更は属性か形状かも<br>*EN: Diff last week's IFC and today's: added, removed, changed elements* | compare_versions · hard · needs model | Match by GlobalId, report added/removed, compare attributes/properties and placement/geometry hash for modified. |
| `ja-japan-s008` | 天井内のダクトと梁の干渉探して、BCFにして出して。クリアランス50mmで<br>*EN: Find clashes between ducts and beams in the ceiling zone and create BCF issues* | coordinate_clash · hard · needs model | Run clash with 50 mm tolerance between IfcDuctSegment and IfcBeam, produce BCF topics with viewpoints and GUIDs. |
| `ja-clash-s014` | 設備と構造のIFCで干渉チェックして、階ごとに数をまとめて。許容差5mm<br>*EN: Run interference check between equipment and structure IFC and list groups* | coordinate_clash · medium · needs model | Run clash with 5 mm tolerance, group by storey and report counts. |
| `ja-openings-s017` | 梁貫通スリーブが必要な箇所を一覧にしてください。スリーブ未設定のものだけで<br>*EN: Find sleeves needed at beam penetrations* | coordinate_clash · hard · needs model | List MEP crossings of beams lacking sleeve/opening, with sizes. |
| `ja-geom-s013` | 梁の開口位置がZ方向にずれている気がします。IFC4で出したものを確認してもらえますか<br>*EN: Check beam openings displaced in Z* | validate_check · hard · needs model | Compare IfcOpeningElement placement against host beam bounding box; list those offset in Z. |
| `ja-guid-s012` | Revitの要素のUniqueIdからIFCのGUIDを出したい。エクスポートしなくてもできる？<br>*EN: How to get the IFC GUID from a Revit element in the add-in* | convert_format · medium · no file | Explain the ExporterIFCUtils.CreateAlternateGUID / UniqueId conversion rules and their limits, and note that actual exported GUID may differ for derived entities. |
| `p-student-s017` | この壁のIFCのGUIDとRevitのIDを一覧にして。卒論で対応表が必要<br>*EN: Give me a list of IFC GlobalId and Revit element id for these walls, need a mapping table for my thesis* | convert_format · medium · needs model | Export mapping of GlobalId and Tag/ElementId from IfcWall; note Revit UniqueId vs GUID conversion. |
| `ja-japan-s009` | ドアにタイプ名ごとに分類コード付けたい。D-1→21-21 11みたいな対応表あるからそれで一括で<br>*EN: Add classification code to all doors by type name* | modify_model_data · medium · needs model | Create IfcClassification/IfcClassificationReference and assign to each IfcDoor by type mapping, report unmapped types. |

### E. Encoding, performance and tooling

| ID | Prompt (synthetic) | Intent · difficulty · file | Expected behavior (EN) |
|---|---|---|---|
| `enc-s003` | IFCを別のビューアで開くとプロパティの日本語が文字化けしてる。ファイル側の問題か確認して<br>*EN: Property values in Japanese appear garbled in a viewer; verify the file.* | validate_check · medium · needs model | Read raw STEP text, verify \X2\ UTF-16 escapes decode to Japanese, determine whether the defect is in the file or the viewer. |
| `enc-s013` | 前回のIFCと今回のIFCで、日本語の名称が変わってるものだけ差分出して<br>*EN: Compare two exports to see which Japanese names changed.* | compare_versions · hard · needs model | Compare Names between files by GlobalId, list differences, separating encoding-only differences. |
| `ja-japan-s016` | 400MBのIFC重すぎ。エンティティ別にインスタンス数とサイズ内訳出して、何が原因か教えて<br>*EN: Model is 400MB; find what takes the space* | optimize_performance · hard · needs model | Count instances per type, estimate size share (e.g. IfcFacetedBrep/IfcCartesianPoint), suggest reductions. |
| `ja-fs-s013` | 400MBのIFCをlazyで開いて壁だけ数えて。メモリどれくらい使った？<br>*EN: Open large IFC lazily and count walls* | optimize_performance · medium · needs model | Open with lazy loading, count IfcWall instances, report time and memory usage. |
| `ja-err-s011` | このIFC、ブラウザビューアで開けない。重すぎ？どの要素が原因か見て<br>*EN: Why viewer will not open large file* | troubleshoot_viewing · hard · needs model | Report file size, entity counts, heaviest geometry, suggest splitting. |
| `ja-japan-s014` | IfcOpenShellで壁の名前一覧出したいんだけどby_typeの書き方これで合ってる？<br>*EN: Beginner asks how to list wall names with IfcOpenShell* | how_to · easy · no file | Show ifc.by_type('IfcWall') and .Name loop, mention IfcWallStandardCase in IFC2x3. |
| `ja-viewconv-s013` | MacでIFCを開ける無料のビューアってありますか？属性も見たいです<br>*EN: Free IFC viewer on Mac to check an IFC* | find_tool · easy · no file | Recommend browser/Mac viewers and describe property inspection. |
| `ja-infra-s014` | 道路の線形をIFC4.3に変換して、平面線形の曲線要素(クロソイド含む)がちゃんと入ってるか確認して<br>*EN: Convert the road alignment to IFC 4.3 and check horizontal curves.* | convert_format · hard · needs model | Export/convert alignment, inspect IfcAlignmentHorizontalSegment types (LINE, CIRCULARARC, CLOTHOID), report. |

### F. AI/MCP flavoured

| ID | Prompt (synthetic) | Intent · difficulty · file | Expected behavior (EN) |
|---|---|---|---|
| `ja-aimcp-s014` | 部屋名が空のものを一覧にして、変更案を出してから反映してください<br>*EN: Fill empty room names* | automate_batch · medium · needs model | List rooms with empty Name, propose edits, apply only after approval, read back. |

### G. Rewritten for realism (new for this file)

Mixed polite and casual registers, katakana loanwords and unchanged IFC identifiers, as in the real notes.

| ID | Prompt (synthetic, rewritten) | Intent · difficulty · file | Expected behavior (EN) | Inspired by |
|---|---|---|---|---|
| `JA-X1` | 確認申請用にIFCを書き出したんですが、まず一室だけ見てほしいです。部屋名・用途・床面積が入っているか、あと面積がRevitの面積表とズレていないか確認できますか？<br>*EN: I exported an IFC for the permit; check one room first: name, use, floor area present, and does the area match the Revit schedule?* | validate_check · medium · needs model | Pick the named room (ask which if not given), read Name/LongName, usage property and area quantity; compare with the Revit value the user supplies; if different, report unit, boundary and calculation-method possibilities; do not claim it satisfies the permit criteria. | `ja-japan-r019`, `ja-japan-s002`, `ja-japan-s010` |
| `JA-X2` | ifcopenshellでIFCから階名と高さ取りたい。IFC2x3でElevationがNoneの階があるんだけど何で？<br>*EN: With ifcopenshell I want storey names and heights; some storeys have Elevation None in IFC2x3: why?* | troubleshoot_code · easy · needs model | List IfcBuildingStorey with Name and Elevation; explain that Elevation is optional and may be unset, fall back to the storey's ObjectPlacement; show a short ifcopenshell snippet. | `ja-japan-r002` |
| `JA-X3` | Vectorworksから出したIFC、開いたら壁が半分ない…階に紐づいてないレイヤのせい？どの要素が階なしか出して<br>*EN: Half the walls are missing in the IFC from Vectorworks - is it layers not linked to a storey? List elements without a storey.* | troubleshoot_export · medium · needs model | Find products not contained in any IfcBuildingStorey, list by class and layer name, mention visibility and plain-solid-vs-wall-tool causes as hypotheses, and say what cannot be checked from the IFC. | `ja-japan-r015`, `ja-japan-s003` |
| `JA-X4` | 設備事務所なんですが、元請からもらった意匠IFCでダクトのルートを3Dで確認したいです。ソフトを買わずに見るなら何がいいですか？あと、このIFCの階ごとの天井高だけ先に教えてください<br>*EN: MEP office: how to view the architect's IFC free to plan duct routes, and tell me ceiling heights by storey now.* | find_tool · medium · needs model | Recommend free viewers (for example BIMvision, Autodesk Viewer, browser viewers) with honest limits; then read storey elevations and space heights from the loaded model and tabulate. | `ja-japan-r025` |
| `JA-X5` | RevitのMCP経由で、20㎡未満の部屋だけ一覧にして。赤く色を付けるのは私がOKしてからでお願いします<br>*EN: Via Revit MCP, list only rooms under 20 m2; colour them red only after I approve.* | modify_model_data · medium · needs model | Read-only room list with area < 20 m2 (units checked), propose a view filter or colour override, wait for explicit approval, apply, read back and report; Revit project only, not an IFC. | `ja-japan-r004`, `ja-aimcp-s014` |

*Prompts listed: 47 (of which 5 rewritten for this file).*

## Tips for generating authentic prompts in this language

| Do | Don't |
|---|---|
| Use the real task vocabulary: 確認申請, 納品IFC, 積算, 施工前検討会, 干渉チェック, 文字化け | Don't translate IFC entity names (IfcWall stays `IfcWall`) or Pset names |
| Name the purpose (permit, estimating, FM handover); Japanese users usually justify a request by the downstream use | Don't write bare technical commands with no business reason for the "owner/reviewer" personas |
| Keep casual prompts short and fragmentary (`半分くらい要素が無い…`, `IFC重すぎ`); polite ones end `〜してください` / `〜できますか` | Don't pile on honorific keigo (`〜していただけますでしょうか`); the data shows plain polite です/ます at most |
| Leave out the IFC version unless the story needs it (unknown on 26 of 47 pages); IFC2x3 is a safe default for MEP/Revit J-tool stories | Don't state that BIM data review (IFC-based) is already in force: only BIM図面審査 has started (2026-04-01) according to the KB; data review is planned |
| Use mixed Japanese/English identifiers (`assign_container`, `Qto_SpaceBaseQuantities`, `lazy=True`) for developer personas | Don't make developer prompts Japanese-only; the real notes are code-first |
| Mention Japanese drafting conventions when the persona is an architect: 壁芯, 1間, 平面直角座標系 (e.g. 第9系) | Don't invent MLIT clause numbers, attribute-list codes or 入出力基準 contents |
| Let the user ask for a preview-then-apply flow (`変更案を出してから反映`, `私がOKしてから`); this matches the cautious tone of AI-use essays | Don't assume users trust the AI to write changes silently |
| For Japanese text in the model, ask about `\X2\...\X0\` and viewer mojibake | Don't use Japanese property names in prompts without checking the loaded model actually contains them |

Related: [multilingual glossary](../../08_glossary/glossary_multilingual.md), [IFC in real projects](../../01_ifc_basics/00_ifc_in_real_projects.md).
