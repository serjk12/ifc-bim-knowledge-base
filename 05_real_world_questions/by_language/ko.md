# Korean: how people ask about IFC, BIM and Revit

**Last compiled: 2026-11-06.** Language code `ko`. Built from `research_raw/wave1/ko/ko-korea.*` plus Korean-language synthetic prompts that other research cells produced.

## Read this first: this file is deliberately short and honest

- **The Korean research cell is thin.** Its search budget was exhausted before any search ran. The only pages read were four pages of buildingSMART Korea (bSK, `buildingsmart.or.kr`) and a few document links. **No Naver blog, Naver cafe, Tistory, Brunch, Autodesk Korea forum or Graphisoft Korea post was seen.**
- **Real records: 8.** Seven are institutional pages (overviews, guideline titles, news items, an exam page) and one is an English GitHub issue about Korean/Japanese/Chinese characters in STEP files. **None is a real user help request.** The report says explicitly that the cell must be re-run with search quota.
- **Everything about how Koreans phrase requests is assumed, not observed.** The 40 synthetic Korean prompts were written by researchers; their casual style (banmal-like `뽑아줘`, `봐줘`, `ㅠㅠ`) is a hypothesis. Do not treat the style notes below as measured fact.
- Reference: [Japan and Korea national requirements](../../02_standards_regulations/national/japan_korea.md) (its Korean mandate thresholds are also *unverified*).

**Suggested follow-up research (not done):** seed queries `레빗 IFC 내보내기`, `IFC 속성 누락`, `IFC 변환 오류`, `아키캐드 IFC`; Naver blogs/cafes (likely login-gated), Tistory, Brunch, Autodesk Korea community.

## Where people ask

| Platform | Status in the data | Notes |
|---|---|---|
| buildingSMART Korea site (`buildingsmart.or.kr`) | 4 pages read (BIM overview, R&D center, news items, exam info) | Institutional voice only: formal, IFC/openBIM/bSI/IDS written in Latin inside Korean. 7 distinct URLs logged |
| GitHub | 1 English issue (FreeCAD STEP export writes raw CJK characters instead of `\X2\` escapes) | Shows that Korean/Japanese/Chinese text in STEP is a known pain point, not that Korean users asked |
| Naver blogs, Naver cafes, Tistory, Brunch, community forums of Autodesk Korea / Graphisoft Korea | **Not reached** | Likely the real home of Korean practitioner questions; unknown |
| Open BIM Research Group site (`kbims.or.kr`) | Listed, not fetched | Research group 2017-2021; KBIMS is a standard/library set, **not** a submission portal |

## Top themes

Only the first column of evidence is real (what the institutional pages emphasise). The "assumed" rows come from the synthetic prompts and are plausible but unobserved.

| Rank | Theme | Basis | Typical wording (from KB) |
|---|---|---|---|
| 1 | IFC / openBIM as the neutral international standard (ISO 16739), why Korea should adopt it | observed (bSK overview) | `IFC와 openBIM이 뭐고 왜 국제표준을 도입해야 하나` |
| 2 | Owner and agency BIM guidelines: MOLIT, PPS (조달청), LH, Korea Expressway Corp., Korea Rail Network Authority | observed (bSK R&D page; names only) | `발주처 BIM 지침 기준으로 …` (synthetic) |
| 3 | IFC versions (2x3, 4, 4.3.2), IDS, buildingSMART validation service and scorecard | observed (bSK R&D page) | `IDS 파일 기준으로 이 모델 검증하고…` (synthetic) |
| 4 | BIM qualification exams and the BIM certificate ladder | observed (bSK exam page) | `BIM 자격시험 정보` |
| 5 | ArchiCAD alongside Revit in the local market | observed (bSK news: ArchiCAD 30 launch event, 2026-10-29) | `아키캐드 30 발표회` |
| 6 | Korean text (한글) in IFC property names and values; mojibake when linking into Revit | assumed (synthetic), supported by the English FreeCAD issue | `ifc 레빗으로 링크하니까 한글이 깨지고 너무 느려요 ㅠㅠ` (synthetic) |
| 7 | Revit proxy/class mapping, missing shared parameters, coordinates | assumed (synthetic) | `일반 모델 패밀리가 전부 프록시로 나가는데…` (synthetic) |
| 8 | Quantities by storey, room area tables, revision comparison, clash false positives | assumed (synthetic) | `층별 콘크리트 물량 m3로 정리해줘` (synthetic) |

## Local ecosystem

| Item | Fact | Confidence |
|---|---|---|
| **buildingSMART Korea (빌딩스마트협회, bSK)** | Founded 1998 as IAI Korea, renamed 2008; about 200 member companies; runs the magazine *The BIM*, BIM Awards, BIM service-record registration (BIM 적용 용역실적 등록) and BIM exams. Site states the latest official IFC is 4.3.2.0 and IFC 5 is in development | verified from bSK pages (per national doc) |
| **BIM certificates** | Ladder: BIM 모델러, BIM 테크니션, BIM 코디네이터, BIM CM 코디네이터, BIM 매니저; pass mark 60/100 per written and practical part | verified (bSK exam page) |
| **MOLIT (국토교통부)** | Architectural BIM guide (2010) hosted on the bSK site; a 2022 construction-industry BIM implementation guideline is referenced on the bSK R&D page | titles verified; contents not read |
| **PPS (조달청)** | Facility project BIM application guideline v2.0 hosted on the bSK site | title verified; contents not read |
| LH, Korea Expressway Corp. (한국도로공사), Korea Rail Network Authority | Listed as owner guideline issuers | names only; requirements unverified |
| **KBIMS / 개방형 BIM 연구단** | Open BIM Research Group 2017-2021 led by bSK with Kyung Hee University and KICT; outputs: KBIMS 2.0, equipment library, Revit/ArchiCAD templates | verified; **not a government portal** |
| Mandate thresholds and years (e.g. PPS BIM for projects above a cost level) | Background knowledge only | **unverified**; do not write tests that depend on them |
| Software | Revit and ArchiCAD both visible in the local market (bSK news mentions both); local MEP/structure vendors exist but were not identified | partly verified |
| Open source | none seen | - |
| IFC as a Korean standard | bSK FAQ says IFC was recognised as an e-commerce standard (ECIF132:2005) | from the national doc; single-source |

Links: [Japan and Korea national doc](../../02_standards_regulations/national/japan_korea.md), [buildingSMART standards](../../02_standards_regulations/buildingsmart_standards.md), [authoring tools](../../03_software/authoring_tools_ifc.md).

## How people write

**Not observed.** The institutional pages are formal, with English acronyms (IFC, openBIM, bSI, IDS) in Latin script. What follows is a *working hypothesis* for generating prompts; verify it against real Korean posts before relying on it.

### Assumed register (from the synthetic prompts)

- Short imperatives to an assistant, dropping politeness: `뽑아줘`, `봐줘`, `정리해줘`, `알려줘`, `찾아줘`. Polite `-요` forms appear for managers or when a request is long (`확인해줘요`, `어떻게 해요?`).
- Casual particles and emoticons for frustration: `ㅠㅠ`, trailing `왜 이래요?`.
- Units and quantities typed compactly: `m3`, `mm 단위로`, `200MB`.

### Vocabulary table (mixes the KB glossary and the synthetic prompts)

| Term | Meaning | Standard / English | Basis |
|---|---|---|---|
| 레빗 | Revit as people say it | Revit | assumed in the research report; unverified |
| 아키캐드 | ArchiCAD | ArchiCAD | observed in a bSK news title; casual use assumed |
| IFC 내보내기 / IFC 가져오기 / 링크 | export / import / link IFC | Export / Import / Link | glossary |
| 공유 매개변수 | Revit shared parameter | shared parameter | glossary (Autodesk Korean UI) |
| 프로젝트 기준점 / 측량점 | project base point / survey point | Revit locating points | glossary |
| 층 / 레벨 | storey / Revit level | IfcBuildingStorey / Level | glossary |
| 룸 / 실 / 실명 | room / room (Korean architectural word) / room name | IfcSpace | 룸 glossary; 실, 실명 from synthetic prompts |
| 부재 | structural/building member (element) | element (IfcProduct) | synthetic prompts |
| 프록시 | proxy element | IfcBuildingElementProxy | glossary and synthetic |
| 속성 세트 (PSET) | property set | Pset | glossary |
| 존 | zone | IfcZone | glossary and synthetic |
| 간섭 체크 / 오탐 | clash check / false positives | clash detection | glossary; 오탐 from synthetic |
| 물량 산출 / 물량 | quantity takeoff / quantities | QTO | glossary; synthetic |
| 발주처 | client/owner | owner | synthetic |
| 슬리브 | sleeve for pipe penetrations | sleeve / opening | synthetic |
| 한글이 깨진다 | Korean text is garbled | mojibake / `\X2\...\X0\` | synthetic; supported by the FreeCAD issue |

### Code-switching

Entity and property names stay in Latin (`IfcBuildingElementProxy`, `IfcSpace`, `Pset`, `GlobalId`); product names are either Latin or transliterated (`Revit`/`레빗`, `ArchiCAD`/`아키캐드`). Whether Korean users write Latin or Hangul for product names in practice was not measured.

### Context given and omitted

Unknown for real users. The synthetic prompts mostly give the software (`레빗`), sometimes the version (`Revit 2024`), and almost never the IFC version in the text.

## Real questions

All eight real records are listed; **none is an end-user question**. They show the institutional vocabulary and what the Korean community body considers worth saying.


| ID | Original (title; paraphrase where it adds something) | English gloss | Persona · tone | Source |
|---|---|---|---|---|
| `ko-korea-r001` | BIM 기술 개요 — IFC와 openBIM이 뭐고 왜 국제표준을 도입해야 하나 | What are IFC and openBIM, and why should Korea adopt international standards? | student_beginner · curious | [bSK](https://www.buildingsmart.or.kr/Home/BimOverview) (official_doc, 2025) |
| `ko-korea-r002` | 기술연구소 — IFC 최신 버전, IDS, IFC 검증 서비스, 인증 스코어카드, 국내 BIM 지침 목록 | bSK R&D center: IFC 4.3.2, IDS, validation service, certification, Korean owner BIM guidelines (MOLIT, KEC, KR, LH, PPS), open BIM design automation research | researcher_academic · neutral | [bSK](https://www.buildingsmart.or.kr/Home/RnDCenter) (official_doc, 2026) |
| `ko-korea-r003` | 국토교통부 건축분야 BIM 적용가이드 — 국토부 건축 BIM 적용가이드 내용 | MOLIT architectural BIM application guide (2010) hosted by bSK | reviewer_authority · neutral | [bSK](https://www.buildingsmart.or.kr/Data/Main/BIM%20Guide_MLTL_Korea_2010.pdf) (regulation, 2010) |
| `ko-korea-r004` | 조달청 시설사업 BIM 적용 지침서 V2.0 — 조달청 시설사업 BIM 적용 기본지침서 | PPS (Public Procurement Service) facility project BIM application guideline v2.0 | owner_client · neutral | [bSK](https://www.buildingsmart.or.kr/Data/Main/시설사업%20BIM%20적용%20기본지침서%20v2.0-S.pdf) (regulation, 2020) |
| `ko-korea-r005` | BIM 표준화 현황 및 활성화 세미나 안내 — BIM 표준화 현황 세미나 | Seminar on current state and activation of BIM standardization (Korea Engineering Association, 11 Nov 2026) | bim_manager · curious | [bSK](https://www.buildingsmart.or.kr/Home/NewsDetail?board=1&id=3446) (official_doc, 2026) |
| `ko-korea-r006` | 아키캐드 30, 공식 발표회 초대 — 아키캐드 30 발표회 | ArchiCAD 30 official launch event invitation relayed by bSK | bim_manager · neutral | [bSK](https://www.buildingsmart.or.kr/Home/NewsDetail?board=1&id=3451) (official_doc, 2026) |
| `ko-korea-r007` | BIM 자격시험 — BIM 자격시험 정보 | bSK BIM certification exam info page | student_beginner · curious | [bSK](https://www.buildingsmart.or.kr/Home/Testinfo) (course, 2026) |
| `en-gh-encoding-r030` | Export: STEP AP214 exports raw non-ASCII characters instead of escaped Unicode | FreeCAD STEP export writes raw Korean/Japanese/Chinese characters instead of \X2\ escapes so commercial CAD cannot open it. | developer_programmer · neutral | [GitHub](https://github.com/FreeCAD/FreeCAD/issues/33914) (github_issue, 2026) |

*The last row is an English-language GitHub issue; it is included because its example text is Korean/Japanese/Chinese. For genuine Korean practitioner questions the data is empty.*

## Ready test prompts

All prompts are **synthetic**. Because no real Korean help requests were seen, treat register and slang as a *first guess* to be corrected later; the technical content (what a good answer must do) is solid because it mirrors the IFC problems seen in other languages. Prompts that mention Korean owner guidelines must not make the assistant claim a specific MOLIT/PPS/LH requirement: the KB has not verified their contents.

### A. Counting and querying the model

| ID | Prompt (synthetic) | Intent · difficulty · file | Expected behavior (EN) |
|---|---|---|---|
| `ko-korea-s001` | 이 ifc에 IfcBuildingElementProxy 몇 개야? 레빗 카테고리별로 나눠줘<br>*EN: Count proxies and their source categories* | query_model_data · medium · needs model | Count IfcBuildingElementProxy, group by Revit category/ObjectType property, report. |
| `ko-korea-s004` | 층 목록이랑 레벨 높이 뽑아줘 (mm 단위로)<br>*EN: List storeys with elevations* | query_model_data · easy · needs model | List IfcBuildingStorey names and elevations converted to mm. |
| `ko-korea-s010` | 덕트 중에 시스템 지정 안된거 있나 봐줘<br>*EN: Ducts without system* | query_model_data · medium · needs model | Check IfcDuctSegment membership in systems, list unassigned. |
| `ko-korea-s012` | 재료 안 붙은 구조부재 리스트 줘<br>*EN: Elements without material* | validate_check · easy · needs model | List structural elements with no material association. |
| `ko-korea-s013` | 실별 면적표 만들어줘 실명 번호 면적<br>*EN: Room area schedule* | extract_quantities · easy · needs model | Extract IfcSpace LongName/Number and area quantities into a table. |
| `ko-mep-s013` | 시스템별로 배관 개수랑 총 길이 뽑아줘 IFC 파일 기준<br>*EN: Pipes by system* | query_model_data · medium · needs model | Group IfcPipeSegment by IfcDistributionSystem, count and sum length from quantities or geometry. |
| `ko-geom-s014` | 형상이 없는 객체 찾아줘, 뷰어에서 안 보이는 요소들<br>*EN: Find elements with empty geometry* | query_model_data · easy · needs model | List products with no Representation or empty body, group by class. |
| `ko-spaces-s017` | 존에 안 들어간 실(IfcSpace) 찾아줘<br>*EN: Spaces without zone* | validate_check · easy · needs model | List spaces not in any IfcZone. |
| `ko-struct-s016` | 레빗에서 IFC 내보냈는데 철근이 안 보여요 왜 그런가요<br>*EN: Rebar not visible in IFC exported from Revit* | troubleshoot_export · medium · needs model | Check IfcReinforcingBar presence, explain Revit export options for rebar, check geometry/viewer. |
| `ko-korea-s006` | 층별 콘크리트 물량 m3로 정리해줘 슬래브 벽 기둥 따로<br>*EN: Concrete volume per floor* | extract_quantities · medium · needs model | Sum NetVolume/GrossVolume by storey and class, flag elements without quantities. |

### B. Export, import and coordinates problems

| ID | Prompt (synthetic) | Intent · difficulty · file | Expected behavior (EN) |
|---|---|---|---|
| `ko-korea-s002` | 레빗에서 내보낸 ifc인데 공유 매개변수가 속성에 하나도 안 보여. 어떤 객체에 Pset이 비어있는지 확인해줘<br>*EN: Properties missing after export* | validate_check · hard · needs model | List elements lacking custom Psets, compare with expected shared parameters, suggest enabling export of user-defined property sets. |
| `ko-korea-s008` | 레빗 ifc 내보내기 하면 좌표가 이상하게 멀리 가는데 공유좌표 설정 어떻게 해야해?<br>*EN: Coordinates far away after export* | troubleshoot_export · medium · no file | Explain Shared Coordinates / Project Base Point vs Survey Point and IFC export site placement options. |
| `ko-err-s012` | 레빗에서 IFC 내보내기 하면 '복구할 수 없는 오류' 뜨는데 어떻게 해요?<br>*EN: IFC export unrecoverable error in Revit* | troubleshoot_export · easy · no file | Suggest updating exporter, disabling add-ins, current view only, filters, bisecting. |
| `ko-proxy-s009` | 일반 모델 패밀리가 전부 프록시로 나가는데 IFC 클래스 매핑 테이블 어떻게 설정해야 돼요?<br>*EN: Generic model families all export as proxy, how to fix* | troubleshoot_export · easy · needs model | Explain category mapping table and per-type Export Type to IFC As, with caveats. |
| `ko-korea-s014` | ifc 레빗으로 링크하니까 한글이 깨지고 너무 느려요 ㅠㅠ<br>*EN: Korean text garbled and import slow* | convert_format · hard · no file | Discuss Korean text encoding in IFC (\X2\ escapes), link vs open, file size reduction. |
| `enc-s007` | 한글 매개변수 이름이랑 값이 IFC에 제대로 들어갔는지 확인해줘요. 깨진 거 있으면 알려주세요<br>*EN: Check whether Korean parameter names and values survived export.* | validate_check · medium · needs model | Inspect property sets and values for Korean text, report broken ones with entity ids. |
| `ko-gis-s017` | 한글 속성값이 깨진 요소 찾아줘. 웹뷰어에서 검색이 안돼<br>*EN: Find elements with broken Korean property values.* | validate_check · medium · needs model | Detect encoding issues in Korean property strings, list elements, suggest fixes. |
| `ko-roundtrip-s015` | civil3d ifc랑 revit 모델 좌표가 안맞아요 z값이 이상함 어디서 틀어진건지 봐줘<br>*EN: Civil 3D IFC and Revit model do not align; check coordinates.* | troubleshoot_import · hard · needs model | Inspect placement, map conversion, units and elevation; explain Link IFC Z behavior. |
| `ko-coord-s014` | 이 IFC 단위가 mm 맞는지 그리고 층 레벨 높이가 건축이랑 구조 모델이 같은지 확인해줘<br>*EN: Check units and storey elevations.* | validate_check · medium · needs model | Check IfcUnitAssignment and storey elevations versus another file. |
| `ko-vm-s013` | 레빗에서 IFC4 내보낼때 Reference View랑 Design Transfer View 중에 뭐 써야돼요?<br>*EN: Which Revit export setting for IFC4* | how_to · easy · no file | Explain RV is the certified/common one, DTV unofficial with advanced BReps; recommend RV for coordination. |

### C. Checking and compliance

| ID | Prompt (synthetic) | Intent · difficulty · file | Expected behavior (EN) |
|---|---|---|---|
| `ko-korea-s003` | 발주처 BIM 지침 기준으로 층/공간/부재 분류 누락된 거 있나 체크해줘<br>*EN: Check against Korean delivery requirements* | comply_regulation · hard · needs model | Check IfcBuildingStorey/IfcSpace presence and classification on elements; report gaps; state which guideline assumptions were used. **Note:** The KB has not verified any Korean guideline's content; the assistant should state which checks it assumed (storey, space and classification presence) and must not cite thresholds or clause numbers it cannot see. |
| `ko-korea-s015` | IDS 파일 기준으로 이 모델 검증하고 실패한 객체 알려줘<br>*EN: IDS check* | validate_check · hard · needs model | Run IDS validation and list failing elements per specification. **Note:** IDS file must be supplied; the assistant should say if none is loaded. |
| `ko-permit-s011` | 건축허가용 IFC인데 계단 챌판 높이랑 디딤판 폭 기준 안 맞는 계단 찾아줘<br>*EN: Check stair tread and riser dimensions* | validate_check · hard · needs model | Read stair geometry or properties, compare riser and tread against supplied limits, list failures. **Note:** The riser/tread limits must come from the user or be requested; do not assume a Korean code value. |
| `ko-classbsdd-s016` | 분류체계 코드 없는 부재 찾아서 리스트 뽑아줘<br>*EN: Check missing classification codes.* | validate_check · easy · needs model | List elements lacking classification references with GUID and name. |

### D. Comparison, clash and openings

| ID | Prompt (synthetic) | Intent · difficulty · file | Expected behavior (EN) |
|---|---|---|---|
| `ko-korea-s009` | 어제 올린 ifc랑 오늘 거 비교해서 추가/삭제/변경된 부재 알려줘<br>*EN: Compare two revisions* | compare_versions · hard · needs model | Match by GlobalId, report added/removed/changed elements and property diffs. |
| `ko-clash-s015` | ifc 간섭검토 할때 오탐이 너무 많은데 어떻게 줄여요? 접촉은 제외하고 싶음<br>*EN: How to reduce false-positive clashes in IFC for a federated model* | coordinate_clash · easy · no file | Explain tolerance, allow touching, rule-sets by discipline, openings/sleeves, grouping and clash filtering. |
| `ko-openings-s018` | 배관이 벽 관통하는데 슬리브 안 들어간 곳 뽑아줘<br>*EN: List walls penetrated by pipes needing sleeves* | coordinate_clash · medium · needs model | Find pipe-wall crossings with no sleeve/opening, list. |
| `ko-s014` | 공정표랑 연결 안 된 부재 층별로 뽑아줘. 4D 시뮬 돌리기 전에 확인해야돼<br>*EN: Check which elements are not linked to the schedule.* | query_model_data · medium · needs model | List elements without task links per storey. |

### E. Data, FM, conversion and tooling

| ID | Prompt (synthetic) | Intent · difficulty · file | Expected behavior (EN) |
|---|---|---|---|
| `ko-korea-s007` | proxy로 나온 것 중 이름에 '기둥' 들어간거 IfcColumn으로 바꿔줘<br>*EN: Reassign proxies to columns* | modify_model_data · hard · needs model | Find proxies by Name match, change class to IfcColumn, preserve psets, report count. |
| `ko-korea-s011` | ifcopenshell로 벽 이름이랑 면적 엑셀로 뽑는 코드 짜줘<br>*EN: ifcopenshell batch export to spreadsheet* | automate_batch · medium · no file | Provide IfcOpenShell script iterating IfcWall, reading Qto_WallBaseQuantities, writing CSV. |
| `ko-cobie-s015` | 시설관리 시스템에 엑셀 올리면 오류 나는데 어느 행이 문제인지 찾아줘, 자산코드 중복인가?<br>*EN: CAFM import fails with the exported spreadsheet; find which rows break it.* | troubleshoot_import · medium · needs model | Check duplicates and blank mandatory fields in exported asset table; list offending rows. |
| `ko-viewconv-s014` | 철골 기둥만 fbx로 뽑아줘 시각화팀 줘야돼<br>*EN: Export steel columns to FBX for visualisation* | convert_format · medium · needs model | Filter columns, explain FBX not directly supported, export OBJ/GLB and convert. |
| `ko-infra-s015` | 교량 IFC 4.3 모델에서 교각 목록이랑 선형 기준 거리(DistanceAlong) 뽑아줘<br>*EN: List all bridge piers and their positions along the alignment.* | query_model_data · hard · needs model | List pier elements, their linear placement distance along alignment, tabulate. |
| `mx-mcl-s009` | IFC 열면 유리가 불투명하게 나오는데 투명도 값이 파일에 들어있는지 확인해줘<br>*EN: Transparent glass shows opaque* | troubleshoot_viewing · medium · needs model | Check IfcSurfaceStyleShading Transparency on glass materials/windows; explain viewer support limits. |
| `p-student-s018` | IFC 파일이 뭐예요? 레빗 없이 열려면 어떻게 해요?<br>*EN: What is an IFC file and how do I open it without Revit?* | understand_concept · easy · no file | Explain IFC briefly and suggest free viewers; offer to summarize a loaded file. |
| `ko-korea-s005` | ifc 파일 열면 아무것도 안 보이는데 왜 이래요? 용량은 200MB<br>*EN: IFC shows nothing when opened* | troubleshoot_viewing · medium · no file | Check header, geometry presence, units, far-from-origin coordinates; suggest causes. |

### F. Rewritten (new for this file; register is a guess)

| ID | Prompt (synthetic, rewritten) | Intent · difficulty · file | Expected behavior (EN) | Inspired by |
|---|---|---|---|---|
| `KO-X1` | 아키캐드에서 IFC 내보냈는데 레빗에서 열면 층이 두 개씩 생겨요. 이 IFC의 층 이름이랑 높이 좀 뽑아주세요<br>*EN: I exported IFC from ArchiCAD and in Revit every storey appears twice; list this IFC's storey names and elevations.* | troubleshoot_import · medium · needs model | List IfcBuildingStorey names and elevations in mm, flag duplicate or near-equal elevations and storeys that differ only in name, explain that Revit levels and IFC storeys are mapped on import and the cause may be on the Revit side. | `ko-korea-r006` (ArchiCAD context), `ko-korea-s004` |
| `KO-X2` | 조달청 납품용으로 IFC 뽑았는데 검수 전에 빠진 거 없는지 봐줄래요? 실명, 면적, 층 분류 위주로<br>*EN: I made an IFC for delivery to the Public Procurement Service; before inspection, check for gaps, mainly room names, areas, storey classification.* | validate_check · hard · needs model | Check IfcSpace name and area presence, storey assignment of all elements, classification presence; list gaps with GlobalId; say which items were assumed because the actual PPS guideline contents are not available to the assistant; no claim of acceptance. | `ko-korea-r004`, `ko-korea-s003` |
| `KO-X3` | 한글로 만든 공유 매개변수(내화시간 같은 거) 값이 IFC에서 \X2\로 나오는데 이게 정상인지 확인해줘<br>*EN: Values of Korean-named shared parameters (for example fire-resistance time) appear as \X2\ in the IFC: check whether that is normal.* | validate_check · medium · needs model | Show raw STEP lines for a few such properties, decode the UTF-16 hex to Hangul, state that the escapes are normal STEP encoding, and flag any value that fails to decode or is truncated; read-only. | `enc-s007`, `en-gh-encoding-r030` |

*Prompts listed: 39 (of which 3 rewritten for this file).*

## Tips for generating authentic prompts in this language

Because the data is thin, these tips are partly assumptions; they are labelled.

| Do | Don't |
|---|---|
| Keep identifiers in Latin (`IfcBuildingElementProxy`, `IfcSpace`, `GlobalId`) and use the Korean Revit UI words from the glossary (`공유 매개변수`, `프로젝트 기준점`) | Don't invent Korean mandate thresholds, project-cost limits or guideline clause numbers (unverified in the KB) |
| Vary register: short banmal-like imperatives for coordinators (assumed), polite `-요` for managers or owners (assumed) | Don't present the register as measured; flag it as a guess in test notes |
| Include Hangul content in the model when testing text: 실명, 벽, 슬래브, 기둥 and Korean property values | Don't assume the loaded model has Korean property names; check first |
| Mention ArchiCAD as well as Revit; both are visible in the Korean market | Don't treat KBIMS as a submission system; it is a research-group standard/library set |
| Tie tasks to owners' delivery requirements (`발주처 기준`) only with a generic check list | Don't have the assistant claim a delivery "passes" a MOLIT/PPS/LH guideline |
| Add emoticon frustration (`ㅠㅠ`) sparingly, as in the synthetic prompts | Don't over-use slang; no real Korean posts confirm it |
| Re-run the research for Korean (Naver, Tistory, Autodesk Korea) before turning these into scored test sets | Don't treat this file as equal in weight to the Chinese or Japanese files |

Related: [multilingual glossary](../../08_glossary/glossary_multilingual.md), [IFC in real projects](../../01_ifc_basics/00_ifc_in_real_projects.md).
