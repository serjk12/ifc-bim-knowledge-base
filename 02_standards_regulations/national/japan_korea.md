# Japan and South Korea: BIM/IFC requirements

**Last researched: 2026-11-06** (QA pass 2026-11-06: MLIT building BIM council page, bSJ certified-software page and bSK R&D page re-fetched; see `_meta/qa/qa-standards-2.md`)

## In plain words

Japan and South Korea both have strong BIM industries, but they regulate BIM in very different ways. Japan has a ministry-led (MLIT) programme with two tracks: building BIM (a "BIM drawing review" for building permits that started on 2026-04-01, with an IFC-based "BIM data review" planned for later) and civil BIM/CIM for public works. IFC in Japan is a certified exchange format, not yet the only legal deliverable. South Korea started earlier (procurement-agency BIM guidelines around 2010) and has a mature BIM service-record and certificate system run by buildingSMART Korea. Its current mandate schedule could **not** be verified in this research run (see Gaps), so treat Korean thresholds and years as unverified. For a QA tester: expect Japanese and Korean names, units, text in property values and file names, and "IFC2x3 plus a country-specific property set" to be the realistic test case, not clean IFC4.3 models.

> Research limit note: the search tool's quota was exhausted before the research started, so this document is built from direct page fetches (WebFetch) of official sites only. PDF files (guidelines) could not be text-extracted, so document contents are known from their official landing pages, not from reading the PDFs. Items from memory are marked "(unverified)".

---

## 1. Japan

### 1.1 Who is responsible

| Body | Role |
|---|---|
| MLIT (国土交通省) Housing Bureau, Building Guidance Division (住宅局建築指導課, "DX team") | Building BIM policy, permit-process BIM, secretariat of the building BIM council [1][2] |
| 建築BIM推進会議 (Building BIM Promotion Council) | Public-private council, established June 2019; chair is a university president (松村秀一); meetings 14th (2025-03-27), 15th (2025-12-24), 16th (2026-03-24) [3] (QA: the MLIT page shows the 16th meeting's minutes published 2026-04-28; the 14th and 15th meeting dates were not visible on the re-read page, unverified) |
| 建築BIM環境整備部会 (Building BIM Environment Sub-committee) | Set up October 2019; 25th meeting held 2026-10-28 (agenda: progress toward BIM data review, and BIM data standardisation) [3][4] |
| MLIT Technical Affairs / NILIM (国土技術政策総合研究所) | Civil BIM/CIM standards and the BIM/CIM portal [5][6] |
| buildingSMART Japan (bSJ) | IFC specialist: runs one of the five working bodies under the council ("BIM information sharing infrastructure", BIMの情報共有基盤の整備検討部会) [3] |
| 一般社団法人BIM標準情報活用協会 (BIM standard information association) | Working body for the shape and attribute standardisation of BIM models (BIMモデルの形状と属性情報の標準化検討部会); rules dated 2026-04-14 [3] |
| 建築確認におけるBIM活用推進協議会 | Working body for BIM in building-permit inspection [3] |
| 日本建築積算協会 | Working body for BIM-based quantity take-off standardisation [3] |
| 設計三会 (the three designer associations) | Publish designer-side BIM guides (e.g. 設計BIMワークフローガイドライン 1st ed.; a 2026 guide on entering BIM data for design deliverables) [3] |

### 1.2 Timeline (building BIM)

| Date | Event |
|---|---|
| 2019-06 | Building BIM Promotion Council founded [3] (QA: the MLIT page re-read does not itself state the June 2019 founding date; it only dates the first roadmap to September 2019 (令和元年9月); founding month remains (unverified) here) |
| 2019-09 | 建築BIMの将来像と工程表 (Future vision and roadmap of building BIM), first edition [3] |
| 2020-03 / 2022-03 / 2026-03 | Guideline "標準ワークフローとその活用方策に関するガイドライン" Ver.1 / Ver.2 / Ver.3 (3rd ed.) [3] |
| 2023-03 | Roadmap supplementary edition (増補版) [3] |
| 2023-24 | 建築BIM加速化事業 (building BIM acceleration subsidy project; support office r5-6bim-shien.jp; briefing sessions 2023-12-27 and 2024-01-11) [7] |
| 2024-03 | 確認申請用CDE仕様書 Ver 1.00 Rev 1.00a (spec of the common data environment used for permit applications) [3] |
| 2025-03 | BIMを通じた建築データの活用に関するガイドライン Ver.1; standard attribute lists (construction/fabrication attributes Ver 1.0) [3] |
| 2026-03-24 | Initial edition of 建築確認におけるBIM図面審査ガイドライン and the application/review manual [3] |
| **2026-04-01** | **BIM図面審査 (BIM drawing review) started** [3] (QA: confirmed on the MLIT page as 「R8.4.1 BIM図面審査が開始されました」) |
| 2026-03 | Data-linkage standardisation task force (標準化TF) Ver 2.0 outputs [3] |
| 2026-09 | "建築確認・検査におけるBIMデータ審査の導入に関する基本構想" (basic concept for introducing BIM data review in building confirmation and inspection) published [3] (QA: listed as 2026年9月, posted 2026-09-18) |
| 2026-10-06..08 | buildingSMART International Summit held in Tokyo (Haneda), theme "openBIM: Built on Tradition, Shaping the Future" [8] |
| 2027 / 2029 | Nationwide rollout of BIM drawing review in 2027 and BIM data review (IFC-based) from spring 2029 are stated by **a software-vendor page only** [9]; check MLIT's basic concept [3] before relying on them (unverified officially) |

### 1.3 BIM drawing review (BIM図面審査) and the role of IFC

- Mechanism: the applicant (designer) produces permit drawings from a BIM model; the reviewers (特定行政庁 and 指定確認検査機関, i.e. local authorities and designated private inspection bodies) review drawings that come from a single model, so cross-drawing consistency is guaranteed by the model [9].
- Official document set [3]:
  - 建築確認におけるBIM図面審査ガイドライン (initial edition, 2026-03-24)
  - 別紙1 入出力基準 (input/output criteria) with an explanatory document (入出力基準の解説, 1st ed.)
  - 別紙2 入出力基準適合誓約書 (compliance pledge form, also in Excel)
  - 別紙3 確認申請図書表現標準 (permit drawing presentation standard)
  - BIM図面審査 申請・審査マニュアル (application/review manual)
  - Q&A of the briefing sessions, and the CDE specification for the "確認申請用CDE"
- IFC role (per a **vendor page**, labelled as such): in the current phase PDF drawings are submitted together with IFC exported from the BIM model; in the later BIM data review, IFC is used directly for automated checking [9]. The exact IFC version and MVD required by the 入出力基準 were **not verified** (the PDF could not be read).
- Supported software named on the vendor page [9]: GLOOBE Architect (RC/steel general buildings), ARCHITREND ZERO (wooden detached houses; standard IFC output from Ver.12). Other BIM tools (Revit, ARCHICAD, Vectorworks) also need to meet the 入出力基準 (the pledge form is the mechanism) (unverified detail).

### 1.4 Civil engineering: BIM/CIM (MLIT directly managed works)

- Policy documents currently listed by MLIT (revised March 2026) [5]:
  - 直轄土木業務・工事におけるBIM/CIM適用に関する実施方針 (implementation policy for BIM/CIM on directly-managed civil work and services) with annexes 1-4 (implementation guidelines for services, works, and integrated-model management support)
  - BIM/CIM取扱要領 (BIM/CIM handling guideline), annexes 1-4; annex 2 is a 3D model vs 2D drawing consistency check (draft), annex 3 is the オブジェクト分類 (object classification) with per-fiscal-year Excel files (R5, R6, R7), annex 4 is 3D model creation for quantity estimation
  - BIM/CIM活用ガイドライン(案) (March 2022), volumes 1-9 (common volume to telecom facilities volume)
  - J-LandXML Ver.1.8 (2026-07-31): 3D design data exchange standard based on LandXML 1.2 [5][6]
  - 事業監理のための統合モデル活用ガイドライン(素案) (March 2022)
- Mandate: MLIT stated BIM/CIM would be applied in principle to all public works from FY2023 (令和5年度), with exceptions (small-scale work); English Wikipedia summarises this as "all of its public works from fiscal 2023" [10]. The MLIT pages fetched in this run did not repeat the sentence, so the exact threshold wording is (unverified) against the primary 実施方針 PDF [5].
- BIM/CIM portal (NILIM) announced a "standard object library" (標準オブジェクトライブラリ) on 2026-10-06 [6].
- IFC role in civil: the BIM/CIM portal itself does not mention IFC [6]; the explicit civil exchange format is J-LandXML (alignments/terrain) and, for IFC, bSJ runs a 土木基本IFC検定 (see 1.5).

### 1.5 IFC in Japan: IFC検定 (IFC verification) and bSJ

- **IFC検定 is a software verification program, not an exam for people.** Software must conform to a given MVD; results are recorded in bSJ's register and published [11]. A separate human-oriented programme is "buildingSMART プロフェッショナル認証" (professional certification) [12].
- Current certified software list (土木基本IFC検定, since April 2022) [13]: SiTE-STRUCTURE Ver 6 (Construction System), TREND-CORE Ver.11 (Fukui Computer), Autodesk Revit 2026 + "J tool for Revit IFC2X3" (input only), V-nasClair 2026 + i-ConCIM_Kit + ModelCheck_Kit (Kawada Techno System). MVD in use: "BIM/CIM積算 MVD" v1.3 (v0.3 for the Revit tool). Certification periods run on a yearly basis, e.g. Revit entry (input only) 2026-02-12 to 2027-02-28 [13]. QA re-check of the list: SiTE-STRUCTURE Ver 6 input/output 2026-09-09 to 2027-09-30; TREND-CORE Ver.11 input/output 2026-03-17 to 2027-03-31; V-nasClair + i-ConCIM_Kit + ModelCheck_Kit 2026 input/output 2026-01-28 to 2027-01-31 [13].
- Legacy MEP MVD: 設備モデルビュー定義2014 (ID MVD_BS-Mode-View_2014, v1.0, 2014-11-26) on **IFC2x3**; property sets follow 設備IFC利用標準 1.0 and carry a `BS_2014` suffix, e.g. `IfcFlowSegment_Pset_BS_2014`; required entities IfcProject, IfcBuildingStorey, IfcFlowController, IfcFlowFitting, IfcFlowSegment, IfcFlowTerminal, IfcFlowTreatmentDevice; IfcSite/IfcBuilding optional [14].
- Practical consequence: many Japanese flows are still IFC2x3 based and use Japan-specific property sets (e.g. the Revit "J tool" is explicitly IFC2X3). A test model produced for Japan may therefore contain `Pset_..._BS_2014`-style names and Japanese `Name` values.
- bSJ activities: technical committee (IFC, IDM, MVD, BCF, bSDD; IFC検定; training IFC experts), architecture committee, civil committee, international committee [15][16].

### 1.6 Classification, attributes and naming

- Building: the "standard attribute list" (標準属性一覧) by the data-linkage standardisation task force, Ver 2.0 (March 2026), with attribute descriptions split into common, architectural, structural and MEP; plus construction/fabrication attributes Ver 1.0 (March 2025) [3]. Treat these as the national property-name vocabulary for BIM data entry.
- Civil: オブジェクト分類 (object classification) per fiscal year, annex 3 of the BIM/CIM handling guideline [5].
- No single "Uniclass-like" national building classification was found in this run; (unverified) whether the standard attribute list is accompanied by a code classification.
- Georeferencing: Japan uses the plane rectangular coordinate system (平面直角座標系, JGD2011, 19 zones) in civil practice (general knowledge, not verified from a BIM document in this run). For IFC tests check `IfcMapConversion` / `IfcProjectedCRS` (IFC4) vs. site `RefLatitude/RefLongitude` (IFC2x3) and units in metres vs millimetres.
- Naming and delivery: electronic delivery for civil works follows the CALS/EC electronic delivery rules (電子納品要領, cals-ed.go.jp) with 3D model handover sheet (3次元モデル作成引継書シート) and a check sheet for model review (3次元モデル照査時チェックシート) [5].

### 1.7 Local software ecosystem

| Product | Vendor | Note |
|---|---|---|
| GLOOBE Architect (GLOOBE 2026 released 2026-07-08) | Fukui Computer (福井コンピュータ) | Japanese building BIM/CAD, positioned for BIM drawing review [9] (vendor claim) |
| ARCHITREND ZERO | Fukui Computer | Wooden houses, standard IFC export from Ver.12 [9] |
| TREND-CORE Ver.11 | Fukui Computer | Civil, IFC-verified [13] |
| SiTE-STRUCTURE Ver 6 | Construction System (建設システム) | Civil, IFC-verified [13] |
| V-nasClair 2026 | Kawada Techno System (川田テクノシステム) | Bridge/civil, IFC-verified [13] |
| Rebro | NYK Systems (page title only; maker relationship not stated on the page) | MEP BIM; site rebro.jp [17]; IFC support not confirmed in this run |
| ARCHICAD, Revit, Vectorworks | Graphisoft, Autodesk, Vectorworks Japan | Widely used; Revit has a Japan "J tool" IFC2X3 add-in [13] |

Community/other hubs named on MLIT's page: BIM GATE (design associations) https://bimgate.jp/, BIMライブラリ技術研究組合 https://blcj.or.jp/sample_form/ [3]. No open-source Japanese IFC projects were verified in this run.

---

## 2. South Korea

### 2.1 What was verified

| Item | Detail |
|---|---|
| buildingSMART Korea (빌딩스마트협회) | Founded 1998-04-16 as IAI Korea, renamed 2008, non-profit corporation approved 2009; about 200 member companies; runs events, BIM Awards, the magazine "The BIM", a "BIM application service record registration" (BIM 적용 용역실적 등록) with operating guidelines revised 2020-06-17, BIM certificates [18][19][20] |
| Downloads on its site | 국토교통부 건축분야 BIM 적용가이드 (2010) and 조달청 시설사업 BIM 적용 지침서 V2.0 (Public Procurement Service) [18] |
| BIM certificate ladder | BIM 모델러, BIM 테크니션, BIM 코디네이터, BIM CM 코디네이터, BIM 매니저; pass mark 60/100 each for written and practical parts [21] |
| 개방형 BIM 연구단 (Open BIM Research Group) | Ran 2017-2021; lead organisation buildingSMART Korea with Kyung Hee University and KICT; site kbims.or.kr; outputs include "KBIMS 2.0" (listed as 기준/standard), KBIMS mechanical-equipment library v2.0, Revit/ARCHICAD templates and libraries [22][23][24] |
| IFC statement | bSK R&D page (re-confirmed in QA; it also names IFC 4.0.2.1 and IFC 2.3.0.1 as the earlier official versions): latest official IFC is IFC 4.3.2.0, IFC 5 in development; also describes IDS, BCF, bSDD; software IFC scoring via buildingSMART's validation service [24] |
| Standards history | IFC was recognised as a Korean e-commerce standard (ECIF132:2005) per bSK FAQ [25] |
| 2026 events | BIM AWARDS 2026 results 2026-10-19; MOU on MEP BIM with the facilities association 2026-07-01; seminar on BIM standardisation (Korea Engineering Association) 2026-11-11 [26][27] |

**KBIMS clarification**: KBIMS in this source is the name of the Open BIM research group and its output standard set, not a government portal [22][23]. A tester should not assume "KBIMS" is a submission system.

### 2.2 What could NOT be verified (do not treat as fact)

The following items come from background knowledge and were **not confirmed from a primary source in this run**:

- The Public Procurement Service (조달청) has required BIM for large facility projects since about 2010 and widened the scope over time; the thresholds (project cost in KRW, e.g. in the tens of billions) and exact years are (unverified).
- MOLIT (국토교통부) publishes a construction-industry BIM basic guideline and a roadmap towards broader mandatory BIM for public projects around 2025-2030; the exact name, edition and dates are (unverified). Do not generate tests that depend on specific Korean mandate thresholds without checking molit.go.kr and pps.go.kr first.
- LH (한국토지주택공사) requirements for housing projects (a LH apartment-BIM survey notice existed in 2019 on the KBIMS site [28]) and Korea Expressway Corporation (한국도로공사) BIM requirements: (unverified); no document found.
- Korean classification (a KBIMS-based object/space classification, or the older cost classification work of 2011 mentioned on bSK R&D page [24]): existence acknowledged, specifics (unverified).

### 2.3 Practical Korean ecosystem notes (partly unverified)

- ARCHICAD is a popular tool in Korean practice; a "ARCHICAD 30" launch event was advertised on bSK's news list on 2026-10-29 [29]. Revit is also widely used (Revit promotions appear in bSK news) [30].
- Korean-specific local BIM vendors (e.g. structural/MEP) exist (unverified names); the KBIMS library list includes Korean firms providing Revit, ARCHICAD and CATIA libraries [23].
- Korea participates in buildingSMART as a Regional Alliance (the English FAQ says so) [31]; bSK site hosts openBIM explanations (IFC, BCF, COBie, CityGML, gbXML) [31].

---

## 3. IFC-related guidance for MCP testing (Japan/Korea flavour)

| Topic | What to test |
|---|---|
| Character encoding | IFC STEP files encode non-ASCII text with `\X2\...\X0\` (UTF-16 hex) escapes; a model with Japanese (例: 外壁, 防火区画) or Korean (벽, 슬래브) names should round-trip through the MCP server without mojibake, and queries by Japanese/Korean names should match |
| Version | Expect IFC2x3 (Japan MEP/Revit J tool) and IFC4; ask the server what schema it reports |
| Property sets | Japan: `Pset_..._BS_2014` style names for MEP; custom national attributes from the standard attribute list; Korea: KBIMS attribute sets (unverified structure) |
| Units | Japanese civil data often millimetres vs metres: check `IfcUnitAssignment` |
| Georeferencing | Plane rectangular coordinates (Japan); check IfcMapConversion presence |
| Permit use case | "Export IFC for BIM図面審査" is IFC output + PDF drawings; MCP tools that claim to prepare submissions should not claim official acceptance |
| Civil | J-LandXML is not IFC; a tool that "opens LandXML" is a different path |

---

## 4. Terminology table

| Native term | Transliteration | English |
|---|---|---|
| 建築BIM推進会議 | Kenchiku BIM suishin kaigi | Building BIM Promotion Council |
| BIM図面審査 | BIM zumen shinsa | BIM drawing review (permit) |
| BIMデータ審査 | BIM dēta shinsa | BIM data review (IFC-based, planned) |
| 建築確認 | Kenchiku kakunin | Building confirmation (permit) |
| 確認申請 | Kakunin shinsei | Permit application |
| 特定行政庁 | Tokutei gyōseichō | Designated local building authority |
| 指定確認検査機関 | Shitei kakunin kensa kikan | Designated confirmation/inspection body |
| 入出力基準 | Nyūshutsuryoku kijun | Input/output criteria |
| 共通データ環境 (CDE) | Kyōtsū dēta kankyō | Common data environment |
| 標準属性一覧 | Hyōjun zokusei ichiran | Standard attribute list |
| オブジェクト分類 | Obujekuto bunrui | Object classification (civil) |
| IFC検定 | IFC kentei | IFC (software) verification |
| 直轄 | Chokkatsu | Directly managed (by MLIT) |
| 電子納品 | Denshi nōhin | Electronic delivery |
| 設計三会 | Sekkei sankai | The three designer associations |
| 設備 | Setsubi | MEP / building services |
| 빌딩스마트협회 | Bilding-seumateu hyeophoe | buildingSMART Korea |
| 개방형 BIM | Gaebanghyeong BIM | Open BIM |
| 조달청 | Jodalcheong | Public Procurement Service |
| 국토교통부 | Gukto-gyotongbu | MOLIT |
| 한국토지주택공사 (LH) | Hanguk tojijutaek gongsa | Korea Land & Housing Corporation |
| 용역실적 | Yongyeok siljeok | Service (work) record |
| 시설사업 BIM 적용 기본지침서 | Siseol saeop BIM jeogyong gibon jichimseo | Basic guideline for BIM in facility projects |
| 건설기준 (KDS/KCS) | Geonseol gijun | Korean Design/Construction Standards |

---

## Typical questions people ask about this

I could not retrieve real forum threads in this run, so all questions are illustrative.

1. (illustrative) Since when does the Japanese building-permit system accept BIM drawings, and is IFC required? (Answer: BIM図面審査 since 2026-04-01; IFC accompanying PDFs per vendor description; verify 入出力基準.)
2. (illustrative) What is the difference between BIM図面審査 and BIMデータ審査?
3. (illustrative) Which Japanese tools can export the IFC required for BIM drawing review?
4. (illustrative) Does Japan's IFC検定 certify people or software? (Software; people have the professional certification.)
5. (illustrative) Which IFC version does the Japanese BIM/CIM MVD (積算) use? (Revit "J tool" is IFC2X3.)
6. (illustrative) Is BIM/CIM mandatory for all MLIT civil works in Japan? (Principle application from FY2023; confirm thresholds.)
7. (illustrative) What is J-LandXML and how does it differ from IFC?
8. (illustrative) What is the 確認申請用CDE and who operates it?
9. (illustrative) Where do I find the Japanese standard attribute list for BIM data entry?
10. (illustrative) Why do my Japanese room names turn into `\X2\...\X0\` in the IFC file?
11. (illustrative) What does KBIMS mean in Korea?
12. (illustrative) Is BIM mandatory for public buildings in Korea and above what budget? (unverified; check 조달청 and 국토교통부.)
13. (illustrative) How do I register BIM project records with buildingSMART Korea (BIM 용역실적 등록)?
14. (illustrative) Which Korean BIM certificate should a modeler take first?
15. (illustrative) Does Korea have an IFC certification service? (bSK states IFC scoring via buildingSMART's validation service; round-trip certification still being researched.)
16. (illustrative) How do I model Korean-language property names so that MCP search finds them?

## Common pitfalls and misconceptions

- "IFC検定 = an exam for engineers" is wrong; it is software verification [11].
- "BIM data review has started in Japan" is wrong as of 2026-11: BIM drawing review started 2026-04-01; BIM data review is a planned later phase, with a basic concept published 2026-09 [3].
- "KBIMS is a Korean government submission portal" is wrong; it is a research-group standard/library set run by buildingSMART Korea consortium [22].
- Dates for nationwide rollout (2027) and data review (2029) come from a vendor page, not from MLIT text read by this research [9].
- J-LandXML is not IFC [5][6].
- A Revit model exported to IFC4 may not match a Japanese MVD that targets IFC2x3 [13][14].

## Gaps

- Web search quota was exhausted; no keyword searches could be run, so real practitioner questions, forum links, Korean mandate thresholds, LH and Korea Expressway requirements, and Korean classification systems are not verified.
- PDFs (BIM図面審査ガイドライン, 入出力基準, BIM/CIM取扱要領) could not be read as text; their clause contents are not summarised.
- Sites such as www.buildingsmartkorea.org, smartcon.or.kr and molit.go.kr main page were not reachable from the fetch tool at the time; the Namuwiki page returned 403.
- No suspicious or pirated sites were encountered.

## Sources

- [1] MLIT press release, 25th Building BIM Environment Sub-committee: https://www.mlit.go.jp/report/press/house05_hh_001157.html
- [2] MLIT Housing Bureau building administration page: https://www.mlit.go.jp/jutakukentiku/build/index.html
- [3] MLIT 建築BIM推進会議 page: http://www.mlit.go.jp/jutakukentiku/kenchikuBIMsuishinkaigi.html (document links: https://www.mlit.go.jp/jutakukentiku/content/001990514.pdf , https://www.mlit.go.jp/jutakukentiku/content/002023688.pdf , https://www.mlit.go.jp/jutakukentiku/content/002012930.pdf , https://www.mlit.go.jp/jutakukentiku/content/001603587.pdf , https://www.mlit.go.jp/jutakukentiku/content/001742200.pdf , https://www.mlit.go.jp/jutakukentiku/content/001993093.pdf)
- [4] https://www.mlit.go.jp/jutakukentiku/build/jutakukentiku_house_tk_000239.html and council page https://www.mlit.go.jp/jutakukentiku/build/jutakukentiku_house_tk_000181.html
- [5] MLIT BIM/CIM standards page: https://www.mlit.go.jp/tec/tec_tk_000037.html
- [6] NILIM BIM/CIM portal: https://www.nilim.go.jp/lab/qbg/bimcim/bimcimindex.html
- [7] MLIT 建築BIM加速化事業: https://www.mlit.go.jp/jutakukentiku/build/bim.html
- [8] buildingSMART International Summit Tokyo 2026: https://www.building-smart.or.jp/bsisummittokyo2026/
- [9] Fukui Computer (vendor) BIM permit page: https://archi.fukuicompu.co.jp/feature/bim-shinsei/ (vendor source)
- [10] Wikipedia, Building information modeling (Japan section): https://en.wikipedia.org/wiki/Building_information_modeling (secondary source)
- [11] bSJ IFC検定 overview: https://www.building-smart.or.jp/ifc/whatsifcverifi/
- [12] bSJ professional certification: https://www.building-smart.or.jp/pc/index.html
- [13] bSJ certified software list: https://www.building-smart.or.jp/ifcc/software.html
- [14] bSJ MVD page: https://www.building-smart.or.jp/ifc/mvd/
- [15] bSJ home: https://www.building-smart.or.jp/
- [16] bSJ technical committee: https://www.building-smart.or.jp/meeting/technology-standard/
- [17] Rebro: https://rebro.jp/
- [18] bSK home: https://www.buildingsmart.or.kr/
- [19] bSK services: https://www.buildingsmart.or.kr/Home/Service
- [20] bSK BIM overview: https://www.buildingsmart.or.kr/Home/BimOverview
- [21] bSK certificates: https://www.buildingsmart.or.kr/Home/Certificate
- [22] KBIMS site: https://www.kbims.or.kr/
- [23] KBIMS outputs: https://www.kbims.or.kr/test01
- [24] bSK R&D Center: https://www.buildingsmart.or.kr/Home/RnDCenter
- [25] bSK BIM overview/FAQ: https://www.buildingsmart.or.kr/Home/BimOverview
- [26] bSK news (association): https://www.buildingsmart.or.kr/Home/NewsList
- [27] bSK domestic news: https://www.buildingsmart.or.kr/Home/NewsList?board=1
- [28] KBIMS notices: https://www.kbims.or.kr/notice
- [29] bSK domestic news page 1: https://www.buildingsmart.or.kr/Home/NewsList?board=1
- [30] bSK domestic news page 2: https://www.buildingsmart.or.kr/Home/NewsList?board=1&Page=2
- [31] bSK openBIM FAQ: https://www.buildingsmart.or.kr/Home/BimOverview
