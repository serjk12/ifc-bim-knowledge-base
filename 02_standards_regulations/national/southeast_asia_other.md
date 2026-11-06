# Malaysia, Vietnam, Indonesia, Thailand, Philippines: BIM/IFC requirements

## In plain words

Five Southeast Asian countries, five different levels of BIM regulation. Vietnam has a national Prime Minister decision (258/QD-TTg, 2023) that makes BIM mandatory for large public projects in stages. Malaysia combines a federal BIM push (projects of RM10 million and above, announced for 1 August 2024) with a CIDB-run BIM building-plan e-submission system called NBeS. Indonesia has had a BIM clause in the state-building regulation since 2018 (buildings over 2,000 m2 and over 2 floors). The Philippines has no general BIM mandate that I could verify, only a rail-sector one (DOTr) and an industry roadmap that mentions BIM standards. Thailand has voluntary, association-led BIM with no verified public-sector mandate. In none of the five did I find an official national text that prescribes a specific IFC version or MVD, so IFC requirements are mostly set per project or per authority (an MCP tester should not assume a national "IFC4 + MVD X" rule exists).

Last researched: 2026-11-06

Research limits: the web-search budget ran out part-way through this session, so several leads (Vietnamese Ministry of Construction guidance texts, Indonesian PUPR BIM guidelines, Thai government policy, Philippine DPWH) could not be followed up. Items from page text I could not fetch or that come only from search-result summaries are marked "(unverified)". See "Gaps".

---

## 1. Quick comparison

| Country | Main driver | Mandate status (as found) | Threshold / scope | IFC-specific rule found? |
|---|---|---|---|---|
| Malaysia | Ministry of Works (KKR) / JKR, CIDB, National Development Action Council | Announced mandate from 1 Aug 2024 for new government and private projects; earlier RM100m public-sector rule; NBeS pilot for local authorities | RM10 million and above (2024 announcement) [19][20] | No official IFC version found. NBeS is described as openBIM-based [11]; its guidebook is described as outlining an Autodesk Revit process [13]. |
| Vietnam | Prime Minister, Ministry of Construction (Bo Xay dung, MOC) | Decision 258/QD-TTg, 17 Mar 2023, staged mandate | Grade I and special-grade public/PPP works from 2023; Grade II and above from 2025 [1] | No. Decision names no data format [1][2]. |
| Indonesia | Ministry of Public Works and Housing (PUPR) | BIM mandatory in Permen PUPR 22/PRT/M/2018 for non-simple state buildings | Over 2,000 m2 and over 2 floors [25] | No. |
| Thailand | None binding found. Thai BIM Association (TBIM), ASA, universities | Voluntary / pilot level per a 2026 policy paper [31] | n/a | No. |
| Philippines | DOTr (rail), CIAP/DTI roadmap; DPWH not verified | Rail-sector BIM mandate (BIM Manual 2019, ISO 19650 maturity level 2) [32]; roadmap action item on digital standards [33] | Rail projects (MMSP, NSCR named) | No IFC rule found. |

---

## 2. Malaysia

### 2.1 Who and what

- **CIDB (Construction Industry Development Board, Lembaga Pembangunan Industri Pembinaan Malaysia)** is the main BIM promoter. Its subsidiary **CIDB E-Construct Services Sdn Bhd** runs the **myBIM Centre** and **NBeS** [10][17].
- **JKR (Jabatan Kerja Raya, Public Works Department)** introduced BIM in 2007 and the first public BIM project was the National Cancer Institute, Sepang, in 2010 [18]. JKR's Strategic Plan 2021-2025 sets BIM-adoption targets; sources conflict on the figure (50% rising 10 points a year, 80% by 2025, or 90% of projects above RM10m) (unverified which is right) [17][20][22].
- **Kementerian Kerja Raya (KKR, Ministry of Works)** announced on 27 Aug 2024 that JKR had integrated BIM in 455 projects since 2021 [22].
- **National Development Action Council** approved extending BIM to government and private projects (Prime Minister's announcement in June 2024, effective 1 August) [19][21].
- **KPKT** (housing and local government ministry) owns the OSC 3.0 Plus One Stop Centre manual into which NBeS is to be integrated [13].

### 2.2 Mandate timeline (with source conflicts)

| Date | Event | Source |
|---|---|---|
| 2007 | JKR formally introduces BIM | [18] |
| 2010 | National Cancer Institute, Sepang, first public BIM project | [18] |
| 2014 | CIDB/CREAM/UiTM workshop report "BIM Roadmap for Malaysia's Construction Industry (2014-2020)", proposing a buildingSMART chapter, a national BIM library, standards, guidelines | [24] |
| 2016-2020 | Construction Industry Transformation Programme (CITP) promotes BIM | [17][18] |
| Nov 2017 | myBIM Centre opens at Menara Sunway Putra, Kuala Lumpur (12 satellite centres) | [17] |
| 2018 or 2019 | Public-sector projects of RM100 million and above must use BIM. One source says 2018 [18], NST of 18 Mar 2019 says "starting this year" [16], another says "since 2019" [17] | conflict |
| 2019 | NST: CIDB recommends mandatory BIM in certain private projects (by 2020 per NST; another source says 2021); no threshold, enforcement period not set | [16][17] |
| 13 Jul 2023 | NBeS initiative formally launched at KL BIM Day 2023 | [12] |
| 1 Aug 2024 | Mandate for new government, GLC and private projects of RM10 million and above announced by PM (June) and repeated by Deputy Works Minister on 4 Sep 2024; applies also to roads, bridges, sewerage | [19][20] |
| 20-21 May 2025 | Sarawak: "100 per cent integration policy" by 2030; buildings over RM10m and infrastructure over RM100m must adopt BIM | [23] |
| 28 Sep 2026 | Kota Kinabalu City Hall (DBKK) launches NBeS for initial digital screening; online e-submission planned from 2027 | [15] |

The 2024 articles do not cite a circular or gazette number; I did not find an official instrument text (unverified legal form). A new "New Construction Technologies Committee", chaired by the Ministry's secretary-general and merged with the IBS (Industrialised Building System) committee, was announced to standardise BIM [19]. The Deputy Minister also said the government would work with universities on local BIM software to reduce reliance on foreign software, and one report quotes about RM45,000 for CIDB-issued software (as reported by media, unverified) [19][20].

### 2.3 NBeS (National BIM e-Submission)

- CIDB describes NBeS as a "first-of-its-kind Auto Checker" that reviews 3D BIM models against Uniform Building By-Laws (UBBL), MS 1184 and other rulesets for the local authority (PBT) approval stage, fully online, built on "OpenBIM technology" [11][12][13].
- Prototype produced January 2017; pilot with five authorities in 2019: Putrajaya Corporation (PPj), Petaling Jaya City Council (MBPJ), Kangar Municipal Council (MPK), Historic Melaka City Council (MBMB), Kuching North City Hall (DBKU). The Fire and Rescue Department (JBPM) rules (UBBL fire safety) were added in 2018 [11][13].
- Claimed outcomes: review in 24-48 hours instead of 7-21 days (CIDB figures vary by article) [9][12][17]; a 2024 academic paper cites a 92% pilot assessment score and a simulated 70% process improvement once integrated with OSC 3.0 Plus Online [13].
- Rollout examples: Kulim Municipal Council (MPKK) workshop 23 Jan 2025 [14]; DBKK Sep 2026 [15]. The number of authorities currently on NBeS is not stated in the sources I could read.
- Documents: **"National BIM e-Submission (NBeS) Guide Book for PSP/SP, Version 2.0" (CIDB, 2021)** is cited by an academic paper, which says it outlines an Autodesk Revit process and defines PSP duties (setting up the NBeS account, approving BIM e-submission documents, ensuring correct model) but not PBT officer duties [13]. I could not read the guidebook itself.
- Portal: nbes.gov.my (the production host failed TLS validation from my tooling, so I did not read it); a demo host shows a login page ("Login to Proceed", register link for PSP) [38]. Sample models and submission rules were not accessible. A secondary summary from search results claimed NBeS uses IFC2x3 and lists sample .ifc files; I could not confirm it (unverified).
- Terminology: **PSP** = Perunding/Pengamal Profesional (Submitting Person/Professional), **PBT** = Pihak Berkuasa Tempatan (local authority), **ATD/ATL** = officers who check; exact expansions of ATD/ATL are not given in the source (unverified) [13].

### 2.4 Other Malaysian resources

- **myBIM Centre** (Kuala Lumpur plus satellites, training and certification; >7,000 certified, 12 modules, some BSI-endorsed) [17].
- **National BIM Library (NBL)**, "more than 10,000 objects" per CIDB, at mybimlibrary.my [17].
- **National BIM Steering Committee**: Ministry of Works, JKR, CIDB and industry [17].
- **buildingSMART**: the 2014 roadmap proposed forming a Malaysian buildingSMART chapter [24]; I could not confirm an active chapter (unverified). buildingSMART's chapter directory page returned HTTP 403 to my tool.
- **Classification**: no Malaysian national classification system was verified. (General knowledge, unverified: CIDB/JKR specs use local product libraries rather than Uniclass or OmniClass.)

---

## 3. Vietnam

### 3.1 Key documents (verified)

| Document | Content | Source |
|---|---|---|
| **Quyet dinh 258/QD-TTg** of 17/03/2023, signed by Deputy PM Tran Hong Ha: "Phe duyet Lo trinh ap dung Mo hinh thong tin cong trinh (BIM) trong hoat dong xay dung" (Approving the roadmap for applying BIM in construction) | Effective from signing (Dieu 3); based on MOC Submission 51/TTr-BXD (05/12/2022) | [1] |
| Quyet dinh 2500/QD-TTg (2016) | Earlier scheme (De an) to apply BIM in construction and operation; only the title and year were visible to me | [5] |
| Quyet dinh 347/QD-BXD and 348/QD-BXD (2021) | MOC detailed guidance for civil and urban technical infrastructure works, and general BIM guidance; exact dates not visible | [5] |
| Cong van 4730/BXD-KTXD of 19/10/2023 | BIM cost: per Circular 12/2021/TT-BXD Appendix VIII, BIM cost is by estimate, capped at 50% of design cost; MOC will issue further cost guidance | [5] |
| TCVN 14177-1:2024 and TCVN 14177-2:2024 | Vietnamese standards equivalent to ISO 19650 parts, referenced in a MOC guidance document found via search; I could not open the document (connection refused) | [8] (unverified) |

### 3.2 The roadmap in detail (Decision 258) [1][2][3][4]

| Stage | From | Works | Funding |
|---|---|---|---|
| 1 | 2023 | Grade I and special-grade (cap I, cap dac biet) | Public investment, non-public state capital, PPP, for new projects at the start of preparation |
| 2 | 2025 | Grade II and above | Same |
| "Other capital" (von khac) | 2024 | Grade I and special | Private/other, BIM file required |
| "Other capital" | 2026 | Grade II added | Private/other |

- BIM files become part of design and as-built records and are submitted with feasibility study appraisal, post-basic-design appraisal, construction permit and acceptance files (Dieu 1.3.c) [1].
- Owner decides scope and level of detail of the model (Dieu 1.3.d/dd); owner must keep the model updated for operation and maintenance [1].
- Minimum BIM content: architecture and main dimensions, 3D of main structural elements, HVAC/ventilation/water supply-drainage layouts; drawings and quantities must be extractable from the model [1][2].
- MOC duties: monitor, amend norms and standards, run a unified national BIM database integrated with the construction database [1].
- State authorities may use BIM to support appraisal, permitting and acceptance from 2023 [1].
- The decision gives no IFC version, MVD, naming rule or classification; the owner's requirements (EIR in ISO 19650 language) fill the gap [1][2].

Local implementation: Lao Cai Department of Construction seminar 29/03/2024 with the Institute of Construction Economics (MOC), reporting up to 12% cost savings and 12-15% schedule reduction from MOC monitoring 2017-2021 [4]; EVNNPT (power transmission) steering committee approved its BIM roadmap on 30/05/2023 for 220-500 kV projects [6]. A research paper proposes an ISO 19650-based process (EIR, BEP, CDE) for Vietnamese firms, noting most firms use BIM merely as software [7].

### 3.3 Classification, organisations, ecosystem

- No Vietnamese BIM classification system verified.
- No buildingSMART Vietnam chapter found (not in the directory snippets I could read) (unverified).
- Local software ecosystem and enthusiast/open-source projects: not researched successfully (unverified gap). General knowledge, unverified: Revit and Tekla dominate; practitioners often exchange IFC for coordination in Navisworks/Solibri.

---

## 4. Indonesia

### 4.1 Verified legal text

- **Peraturan Menteri PUPR Nomor 22/PRT/M/2018 tentang Pembangunan Bangunan Gedung Negara**, "ditetapkan di Jakarta pada tanggal 14 September 2018", diundangkan 15 Oktober 2018. Implements Perpres 73/2011 [25].
- BIM clause is in **Lampiran I, section A (Penyedia Jasa Perencanaan Konstruksi), item 13**: use of BIM is mandatory ("wajib diterapkan") for **non-simple state buildings with floor area above 2,000 m2 and above 2 floors**. Design outputs to be produced with BIM: architectural drawings, structural drawings, MEP (utility) drawings, landscape drawings, quantity details (rincian volume), and cost estimate (RAB) [25]. I read this from the official JDIH PUPR PDF.
- 2021 reporting: PUPR described this as its only legal basis for BIM and recommended extending it to all PUPR units and infrastructure; the PUPR BIM roadmap had four phases (adoption, digitalization, collaboration, system integration) with a 2024 target of a cloud construction management system [26]. Projects named as BIM-applied included Gelora Bung Karno stadium renovation and several markets [26].
- **SE Dirjen Bina Marga 11/2021** reportedly allows BIM in technical planning, construction and maintenance of roads and bridges (reported by a UGM webinar article; text not read) [27]. **PP 16/2021** (implementing rules of the Building Law) is also cited for BIM in secondary sources [28] (unverified details).
- Not verified: any PUPR BIM guideline number, national SNI for BIM, or e-permit (SIMBG) BIM requirement. The "Surat Edaran 18/SE/M/2021" in the task hint could not be confirmed; do not cite it.

### 4.2 Terminology and ecosystem

- Standard Indonesian term: "pemodelan informasi bangunan" [28].
- IFC rule: none found. Classification: none found. buildingSMART Indonesia: not found (unverified). Community: universities such as UGM's CoE Smart and Green BIM and the Archilantis community ran the "Pekan Konstruksi Digital" webinar [27] (community/academic, not official).

---

## 5. Thailand

- No binding national BIM mandate was found. A 2026 qualitative policy paper (Kasem Bundit University per search summary) describes BIM as voluntary and pilot-driven rather than integrated into public construction policy, and recommends legal framework, ISO 19650/IFC/COBie benchmarks and a national CDE [31].
- **TBIM (Thai Building Information Modeling Association, สมาคมแบบจำลองสารสนเทศอาคาร)**, founded 2019, Bangkok; about 650 members and 25 corporate members; mission to develop and promote BIM standards; roadmap items include publishing a BIM standard and "BIM adoption for regulators" as goals; training (BIM Bootcamp 2026 was postponed due to flooding) [29]. Launch coverage (5 Nov 2019): real-estate-sector backed, government architects/engineers on committees, standards subcommittee expected output ~2020, public-sector BIM use cited at MRT pink and orange line stations [30]. No published TBIM standard was named on the site [29].
- A Chulalongkorn thesis (found via search, unfetched) referencing an Association of Siamese Architects "Thai BIM Guideline (2015)" focused on modelling, and noting weak BIM content in government TOR documents (unverified; no URL fetched).
- IFC rule, classification system, georeferencing rule: none found.
- Terms: BIM = แบบจำลองสารสนเทศอาคาร (baepchamlong sarasonthet arkhan) [29][37].

---

## 6. Philippines

- **DOTr BIM Manual (2019)**: DOTr mandated BIM across design, construction and operation of rail-sector projects; projects must reach BIM maturity level 2 per ISO 19650; manual produced under ADB's Infrastructure Preparation and Innovation Facility (IPIF); applied to MMSP and NSCR railways; a CDE is used; LOD per AIA E203-2013 and BIMForum LOD spec; "open source as-built BIM models" for operations [32].
- **Georeferencing note**: the national geodetic system is PRS92 managed by NAMRIA, with PageNET CORS; it is not satellite-based, so positions shift versus WGS84 GNSS (relevant for IfcMapConversion/IfcProjectedCRS tests) [32].
- **Construction Industry Roadmap 2020-2030** (CIAP/DTI/PCA, launched March 2019, theme "Tatag at Tapat 2030"): Action Plan 14 institutionalises digital technology across the regulatory, permitting and infrastructure life cycle and proposes a Technical Council to propose digitisation standards, with BIM as an example; **no BIM mandate** [33].
- **DPWH**: JICA's 2021 survey recommends BIM-related digitalisation for DPWH and DOTr but I found no DPWH BIM department order (unverified) [32].
- **Organizations**: buildingSMART International approved the Philippines as a "chapter-in-formation" (38th chapter, announced about 25 July 2025, per a buildingsmart.org news item seen via search; page itself returned 403) (unverified details) [36]. In 2016 PICE's president called for a BIM roadmap and mandate; TESDA considered BIM Modeler courses [34]. 18-22 May 2026: ILO-Korea programme trained 10 BIM master trainers with TESDA, PCA and CMDF [35].
- IFC rule, classification: none found.

---

## 7. IFC and openBIM across the five countries (what a tester can assume)

| Topic | Finding |
|---|---|
| IFC version / MVD | Not prescribed in any national document I could read. The mandates are about "BIM file" or "BIM model" in general terms [1][25]. Treat IFC2x3 Coordination View 2.0 or IFC4 Reference View as practical defaults, but say "per project EIR". |
| Property sets | None national. Use standard buildingSMART Pset_*Common sets plus project psets (general IFC knowledge). |
| Classification | No national BIM classification verified in any of the five. |
| Georeferencing | Philippines: PRS92 vs WGS84 issue noted [32]. Others: not researched (Vietnam VN-2000 and Malaysia/Indonesia national grids are general knowledge, unverified). |
| Delivery and checking | Vietnam: BIM files submitted with appraisal/permit/acceptance files [1]. Malaysia: NBeS rule-checks models online [11]. Indonesia: BIM-produced drawings, quantities and budget [25]. |
| Templates / portals | Malaysia: NBeS portal and guidebook (Revit-oriented process) [13][38]. No official IFC templates found elsewhere. |

---

## 8. Terminology table

| Native term | Transliteration / language | English |
|---|---|---|
| Pemodelan Maklumat Bangunan (BIM) | Malay (media use "Pemodelan Maklumat Bangunan (BIM)") [19] | Building Information Modelling |
| Pihak Berkuasa Tempatan (PBT) | Malay | Local authority |
| Lembaga Pembangunan Industri Pembinaan | Malay | Construction Industry Development Board (CIDB) |
| Undang-Undang Kecil Bangunan Seragam (UBBL) | Malay | Uniform Building By-Laws |
| Mo hinh thong tin cong trinh (BIM) | Vietnamese, "Mô hình thông tin công trình" [1] | Building/construction information model |
| Lo trinh | Vietnamese "Lộ trình" | Roadmap |
| Cong trinh cap I / cap dac biet | Vietnamese "cấp I / cấp đặc biệt" | Grade I / special-grade works |
| Chu dau tu | Vietnamese "chủ đầu tư" | Investor/owner |
| Pemodelan informasi bangunan | Indonesian [28] | BIM |
| Bangunan gedung negara tidak sederhana | Indonesian [25] | Non-simple state building |
| Penyedia jasa perencanaan konstruksi | Indonesian [25] | Design service provider |
| แบบจำลองสารสนเทศอาคาร | Thai [29][37] | BIM |
| สมาคมแบบจำลองสารสนเทศอาคาร | Thai | Thai BIM Association |

---

## Typical questions people ask about this

Real forum questions could not be retrieved (search budget exhausted); all below are illustrative unless stated.

1. Is BIM mandatory in Malaysia and from when? (illustrative; sources: [19][20])
2. What is the project value threshold for the Malaysian BIM mandate: RM10 million or RM100 million? (illustrative; answer: RM100m earlier public rule, RM10m in 2024 announcement [16][19])
3. Which file format does NBeS require, native Revit or IFC? (illustrative; answer: not confirmed, guidebook is described as Revit-oriented [13])
4. Which Malaysian local authorities accept NBeS submissions? (illustrative; pilot five [13], more joining [14][15])
5. In Vietnam, from which year is BIM mandatory for Grade II works? (illustrative; 2025 for public funds, 2026 for other capital [1])
6. What counts as a "Grade I" work in Vietnam and who classifies it? (illustrative; not defined in Decision 258 [2])
7. What must be in the BIM file Vietnamese owners submit for a building permit? (illustrative; [1])
8. How much can I charge for BIM design services in Vietnam? (illustrative; 50% of design cost cap in CV 4730 [5])
9. Does Vietnam use TCVN equivalents of ISO 19650? (illustrative; TCVN 14177 reported, unverified [8])
10. Which Indonesian buildings must use BIM? (illustrative; [25])
11. Where in Permen PUPR 22/2018 is the BIM clause? (illustrative; Lampiran I A.13 [25])
12. Does Indonesian private construction have to use BIM? (illustrative; no private mandate found)
13. Is BIM mandatory in Thailand's government projects? (illustrative; no, per [31])
14. Where do I find Thai BIM standards and training? (illustrative; TBIM [29])
15. Does the Philippines have a BIM mandate for DPWH projects? (illustrative; none found; rail only [32])
16. Which ISO 19650 level does DOTr require? (illustrative; maturity level 2 [32])
17. What coordinate system should IFC models use in the Philippines? (illustrative; PRS92 vs WGS84 [32])
18. Which IFC version should I export from Revit for Malaysian NBeS or a Vietnamese permit? (illustrative; ask the authority/EIR)
19. Is there a buildingSMART chapter in my country? (illustrative; only Philippines chapter-in-formation seen [36])
20. Which MCP checks would a tester run to verify an IFC against an EIR for a Vietnamese Grade I project? (illustrative; see pitfalls)

## Common pitfalls and misconceptions

- "Malaysia requires IFC": no official IFC requirement was found; NBeS is called openBIM yet its guidebook is described as Revit-oriented [11][13]. Do not generate tests asserting a specific NBeS IFC version.
- Conflicting figures: RM100m (2018/2019) versus RM10m (2024); JKR targets 50%/80%/90%; NBeS approval times 24-48 hours versus 2-48 hours or "less than 10 days" (DBKK) [15][17][18]. Always cite date and source.
- Vietnam: Grade I/special mandatory from 2023 applies to public/PPP and new projects at preparation stage; private-capital projects start in 2024 [1]. Some sites describe it differently ("official from 2024") [2][3 conflict in snippets].
- Indonesia: the BIM duty covers non-simple state buildings above 2,000 m2 and above 2 floors, both conditions [25]; it is not a general mandate for private buildings.
- Philippines: the Construction Industry Roadmap is not a BIM mandate [33]; do not confuse DOTr rail rules with national law.
- Thailand: TBIM is an association, not a regulator [29].
- Task hints that did not verify: "Permen PU 9/2021" and "SE 18/SE/M/2021" (no source found); "Arahan Teknik BIM" JKR (not found).

## Gaps

- Not found or not readable: NBeS Guide Book contents, nbes.gov.my production pages (TLS error), IFC version for NBeS; MOC Decisions 347/348 text; TCVN 14177 document (connection refused); Indonesian PUPR BIM guideline and SE texts; Thai government policy (DPW, Treasury); DPWH BIM orders; local software and open-source projects; buildingSMART chapters in Malaysia, Vietnam, Indonesia, Thailand; real community questions; JKR "BIM Garis Panduan".
- Sites skipped or failing: buildingsmart.org pages returned HTTP 403; prachachat.net 403; researchgate 403; several MOC/PUPR hosts refused connections.
- One fetched Vietnamese law-site page contained embedded text instructing formatting of the answer; it was ignored as untrusted content.
- No suspicious download sites were encountered; none linked.

## Sources

[1] https://luatvietnam.vn/xay-dung/quyet-dinh-258-qd-ttg-246386-d1.html (Decision 258/QD-TTg text)
[2] https://doanhnghiephoinhap.vn/chinh-thuc-ap-dung-mo-hinh-thong-tin-cong-trinh-doi-voi-cong-trinh-cap-1-cap-dac-biet.html
[3] https://luatvietnam.vn/legal-updates/roadmap-for-application-of-building-information-modeling-bim-in-construction-892-93517-article.html
[4] https://baolaocai.vn/hoi-thao-pho-bien-lo-trinh-ap-dung-mo-hinh-thong-tin-cong-trinh-bim-tren-dia-ban-tinh-lao-cai-post382061.html
[5] https://hethongphapluat.com/cong-van-4730-bxd-ktxd-nam-2023-xac-dinh-chi-phi-ap-dung-mo-hinh-thong-tin-cong-trinh-bim-do-bo-xay-dung-ban-hanh.html
[6] https://tapchicongthuong.vn/tong-cong-ty-truyen-tai-dien-quoc-gia-evnnpt-hop-phe-duyet-lo-trinh-ap-dung-bim-105638.htm
[7] https://vjol.info.vn/tcvienvatlieu/article/view/136902
[8] https://dns1.moc.gov.vn/Images/editor/files/TL%20KT%20Xay%20dung/Tai%20lieu%20huong%20dan%20Bo%20TCVN%2014177.pdf (seen in search results only)
[9] https://www.cidb.gov.my/eng/cidb-launches-national-bim-e-submission-initiative
[10] https://smart.cidb.gov.my/article/nbes-at-a-glance-8
[11] https://smart.cidb.gov.my/program/nbes
[12] https://www.edgeprop.my/content/1906624/cidb-launches-national-building-information-modelling-e-submission-initiative
[13] https://mail.planningmalaysia.org/index.php/pmj/article/download/1560/1239/2448 (Planning Malaysia 2024 paper on NBeS competency)
[14] https://pbt.kedah.gov.my/index.php/2025/01/29/bengkel-transformasi-digital-national-bim-e-submission-bagi-kelulusan-pelan-bagunan/
[15] https://newswav.com/article/dbkk-rolls-out-nbes-for-digital-building-plan-screening-A2609_BgJIKa
[16] https://www.nst.com.my/amp/news/nation/2019/03/470468/cidb-recommends-mandatory-use-bim-certain-private-sector-projects
[17] https://www.cidb.gov.my/bim-digitising-construction-beyond-2020/
[18] https://smart.cidb.gov.my/article/bim-in-malaysia-a-constructive-journey-41
[19] https://www.thestar.com.my/news/nation/2024/09/04/all-projects-worth-rm10mil-and-above-to-use-construction-software-bim-says-ahmad-maslan
[20] https://thesun.my/business/building-information-modelling-to-be-implemented-at-all-levels-from-august-OD12554912
[21] https://www.planradar.com/sg/malaysian-construction-bim-implementation-august-2024/ (vendor blog)
[22] https://bernama.com/en/news.php?id=2333859
[23] https://dayakdaily.com/sarawak-mandates-full-building-information-modelling-adoption-for-major-construction-infrastructure-projects-by-2030
[24] https://smart.cidb.gov.my/media/vm2/download-page-files/62/roadmapreport2-1667141384400.pdf (BIM Roadmap workshop report series 2)
[25] https://jdih.pu.go.id/internal/assets/assets/produk/PermenPUPR/2021/03/PermenPUPR22.pdf (Permen PUPR 22/PRT/M/2018)
[26] https://www.industry.co.id/read/82964/kementerian-pupr-tingkatkan-pemanfaatan-teknologi-bim-dalam-pembangunan-infrastruktur
[27] https://ugm.ac.id/?p=3243
[28] https://id.wikipedia.org/wiki/Pemodelan_informasi_bangunan (community encyclopedia)
[29] https://www.tbim.or.th/
[30] https://marketeeronline.co/archives/129382
[31] https://so04.tci-thaijo.org/index.php/archkmitl/article/view/283010
[32] https://openjicareport.jica.go.jp/pdf/12360814_03.pdf (JICA survey, March 2021)
[33] https://globalbim.org/info-collection/philippine-construction-industry-roadmap-2020-2030/
[34] https://marketmonitor.com.ph/philippines-adopt-bim-technology-infra-projects/
[35] https://www.asiaeducationreview.com/technology/news/philippines-expands-bim-training-for-future-workforce-nwid-6068.html
[36] https://www.buildingsmart.org/?p=32542 (Philippines chapter-in-formation; seen via search snippet, fetch returned 403)
[37] https://th.wikipedia.org/wiki/แบบจำลองสารสนเทศอาคาร
[38] https://demo.nbes.gov.my/ (login page only)
