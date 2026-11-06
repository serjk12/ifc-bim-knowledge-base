# Mainland China: BIM/IFC standards and BIM-based review

**Last researched: 2026-11-06 (fact-checked in QA pass 2026-11-06; see `_meta/qa/qa-standards-2.md`)**

> **RESEARCH STATUS WARNING (read first).** This document was produced under a severely limited research session: the web-search budget was exhausted before any search ran, and most primary Chinese sources (MOHURD, the national standards platform, Baidu Baike, ISO, buildingSMART chapter pages) were unreachable (HTTP 403/404, DNS or TLS errors). Only two sources were actually read (listed in Sources). Everything else is background knowledge and is marked **(unverified)**. Treat every standard number, date and document number marked unverified as a lead to confirm, not a fact. No URLs were invented; where an official link is unknown it is omitted. A QA pass later the same day re-checked the standard numbers, effective dates, several MOHURD document numbers and the Shenzhen data standard against search results and standards-database pages; items it confirmed now carry a source number [3]-[16], the rest stay **(unverified)**.

## In plain words

China does not have one national law that says "all buildings must be delivered as IFC". Instead, the Ministry of Housing and Urban-Rural Development (MOHURD, 住房和城乡建设部) issues national BIM standards (the GB/T 51xxx series) and policy guidance, and provinces and cities add their own requirements: BIM in public-investment projects, BIM-based drawing review (施工图审查), and CIM (City Information Model) platforms. National standards are mostly "recommended" (GB/T = recommended national standard; GB = mandatory), but local governments can make BIM delivery mandatory for certain project types. IFC is the international exchange format that Chinese standards reference; the national storage standard GB/T 51447-2021 is built around IFC-like data organisation, while many local review platforms use their own data rules, often with domestic software and sometimes private/IFC-derived formats. For a QA tester: expect Chinese-language property names, GB/T-based classification codes, a CGCS2000 coordinate system, and MCP servers that must cope with GBK/UTF-8 text and non-English property sets.

## National standards (GB/T series) - status of knowledge

The only item directly confirmed in this session is the first row's name and its description as China's first engineering-construction BIM application standard [1]. All other details are from memory.

| Standard | Chinese name | English name | Notes |
|---|---|---|---|
| GB/T 51212-2016 | 建筑信息模型应用统一标准 | Unified Standard for BIM Application | Confirmed existence/name [1]. Defines BIM; issued 2016-12-02, effective 2017-07-01 [3]. |
| GB/T 51235-2017 | 建筑信息模型施工应用标准 | Standard for BIM Application in Construction | Issued 2017-05-04, effective 2018-01-01 [4]. |
| GB/T 51269-2017 | 建筑信息模型分类和编码标准 | BIM Classification and Coding Standard | Based on ISO 12006-2 / OmniClass-style tables; issued 2017-10-25, effective 2018-05-01 [5]. |
| GB/T 51301-2018 | 建筑信息模型设计交付标准 | Standard for BIM Delivery in Design | Defines model element granularity/LOD-like levels and delivery content; issued 2018-12-26, effective 2019-06-01 [6]. |
| GB/T 51447-2021 | 建筑信息模型存储标准 | BIM Storage Standard | Defines BIM data storage logical architecture, aligned with IFC; announced by MOHURD as announcement No. 160 of 2021 (2021-09-08), effective 2022-02-01 [7]. |
| JGJ/T 448-2018 | 建筑工程设计信息模型制图标准 | Standard for graphic expression of building information modeling (database title) | Industry standard (JGJ = construction industry); issued 2018-12-06, effective **2019-06-01** [8] (an earlier draft of this document said 2019-03-01, which was wrong). |
| GB/T 25507-2010 | 工业基础类平台规范 | IFC platform specification | Listed as an identical adoption (IDT) of **ISO/PAS 16739:2005 (IFC2x platform)**, i.e. the IFC2x generation, not IFC2x3 or IFC4; issued 2010-12-01, effective 2011-05-01 [9] (commercial database listing; status per that listing: valid). |

Practical consequences (all unverified unless stated):
- GB/T 51269 gives the classification table codes (e.g. 41-xx element classes, unverified) used in model properties; Chinese models often carry a "分类编码" / "构件编码" parameter.
- GB/T 51301 sets "模型精细度" (LOD 100-500 analogue, e.g. 1.0-4.0 levels) and requires property tables per discipline.
- GB/T 51447 is the standard to cite when a request says "store/exchange BIM as an open format in China"; it describes data layers (resource, core, shared, domain) closely following IFC (unverified detail).

## Policies and mandates

Federal-style "who mandates" in China is layered:

| Level | Body | What (all unverified; confirm numbers) |
|---|---|---|
| National | MOHURD | 2015 "关于推进建筑信息模型应用的指导意见" (document number 建质函〔2015〕159号, cited as such in several provincial documents [10]): targets BIM usage rate in new large public projects by 2020 (target details unverified). |
| National | MOHURD | 2016-2020 "建筑业信息化发展纲要" (建质函〔2016〕183号, issued 2016-08-23 per a secondary list [11]): lists accelerating BIM adoption as a main task. |
| National | MOHURD and other ministries | 2020 "关于推动智能建造与建筑工业化协同发展的指导意见" (建市〔2020〕60号, confirmed by local implementing documents [12]): smart construction and industrialised building; targets 2025 and 2035. |
| National | MOHURD | 14th Five-Year Plan for the construction industry (2022, believed 建市〔2022〕11号): BIM-based review and delivery, CIM platforms. |
| National | MOHURD | CIM basic platform technical guidelines (2020, number unverified). |
| Provincial/municipal | Housing bureaus, planning/natural resources bureaus | Local BIM application guidelines; BIM mandatory for government-invested projects above an area/investment threshold (thresholds vary by city, unverified). |

Thresholds typically appear as "public buildings above N m2 or investment above N million RMB" with N set locally. Do not state a single national threshold.

## Local BIM review / permit systems and CIM platforms (all unverified)

China has an unusual feature: some cities accept or require **BIM models in drawing review and permits**.

| City/area | Known concept | Notes |
|---|---|---|
| Shenzhen | BIM-based building permit and drawing review; local data standard SJG 114-2022 "建筑信息模型数据存储标准" (Standard for Data Storage of BIM), issued 2022-05-25, effective 2022-06-15 [13]; the IFC-based submission format is referred to as "SZ-IFC" | The standard is real and IFC-based (Pset keyword and IFC object types kept, Chinese descriptions added); a buildingSMART Poland material states that from 2023-01-01 new projects above 10 million RMB and 1,000 m2 must use BIM and submit SZ-IFC models at permit stages [14] (secondary; unverified against the Shenzhen notice). Shenzhen also has SJG 76-2020 (BIM design delivery) and SJG 157-2024 (BIM semantic dictionary) used in model quality checks [13]. |
| Guangzhou | CIM platform with BIM-based drawing review pilot (since about 2019, unverified) | Reported as a pioneer of "BIM审查". |
| Nanjing, Hunan, Chongqing | Provincial/municipal BIM review pilots | Unverified. |
| Xiong'an New Area | Strong digital twin approach, "XDB" digital building concept in the task brief | Unverified; format details unknown. |

Typical workflow people describe (illustrative, not verified): design team models in Revit/PKPM/BIMBase, exports to platform-required format (IFC or a proprietary/derived format), uploads to the local review portal, the platform auto-checks rule clauses (e.g. fire-protection distances, egress widths, floor-area calculations) against the model, human reviewers confirm. Rules are derived from mandatory national codes (GB 50016 fire code etc.).

## IFC-specific requirements in China

Verified in this session: IFC4.3 Add2 (2024) and ISO 16739-1:2024 are the current international state; IFC4.1/4.2 are withdrawn [2]. Everything about China-specific IFC use is unverified:
- Most Chinese national standards reference IFC conceptually; there is no widely cited "China MVD" equivalent to Reference View in national law (unverified).
- Local review platforms usually specify IFC2x3 or IFC4 Reference View plus property-set tables in Chinese (unverified).
- Georeferencing: official coordinate system is CGCS2000 (China Geodetic Coordinate System 2000, EPSG:4490 geographic; projected zones use Gauss-Kruger 3 degree zones). IFC4 IfcMapConversion/IfcProjectedCRS is the way to carry it; IFC2x3 lacks it (general IFC knowledge). Revit users often have survey coordinate mismatch.
- Naming: file and element naming follow local guides; Chinese characters in IFC strings require \X2\ encoding in STEP files (general IFC knowledge: IFC SPF uses ISO 10303-21 escapes). A common failure is mojibake when the tool writes UTF-8 raw.
- Units: millimetres in Chinese design practice.

## Official templates, tools and portals

Not verified in this session. Expected categories: local review portals (per city), national "全国工程质量安全监管信息平台"-type platforms (unverified), CIM platforms. Do not give URLs.

## Local software ecosystem

| Product | Vendor | Notes (unverified) |
|---|---|---|
| Revit | Autodesk | Still very widely used; many Chinese plug-ins (e.g. 橄榄山, 鸿业, isBIM). |
| 广联达 (Glodon) | Glodon | Cost estimating, BIM 5D, BIMFACE web viewer/API. |
| PKPM / PKPM-BIM | 北京构力科技 (Beijing Glory PKPM Technology) [16] | Structural design; PKPM-BIM runs on BIMBase; IFC export (unverified). |
| YJK | 盈建科 | Structural analysis; IFC link. |
| BIMBase | Developed by China Academy of Building Research (CABR) and launched 2021 as a domestic BIM platform with its own geometry/rendering/data engines (vendor claims) [16] | PKPM-BIM and other PKPM products from Beijing Glory PKPM Technology (北京构力科技) are built on BIMBase; relevant to 自主可控 (self-reliant) policy. |

"Domestic software policy" (国产化/自主可控, XinChuang) pushes government-related projects towards domestic BIM platforms; the exact rules are not verified.

## Key organizations

- MOHURD (住房和城乡建设部): standards and policy.
- Standards committees and institutes: China Academy of Building Research (中国建筑科学研究院), China Institute of Building Standard Design (中国建筑标准设计研究院) (roles unverified).
- buildingSMART: a buildingSMART China chapter exists in the official directory (secretariat at China Institute of Building Standard Design & Research, CBS) and buildingSMART Hong Kong is a separate full chapter incorporated 2019 [15]; Taiwan's status is unverified.
- BIM alliances and societies (e.g. China BIM Alliance, 中国勘察设计协会 BIM committee): unverified.

## Local terminology

| Chinese | Pinyin | English |
|---|---|---|
| 建筑信息模型 | jiànzhù xìnxī móxíng | Building Information Model (BIM) [1] |
| 工业基础类 | gōngyè jīchǔ lèi | Industry Foundation Classes (IFC) |
| 施工图审查 | shīgōngtú shěnchá | Construction drawing review |
| 城市信息模型 | chéngshì xìnxī móxíng | City Information Model (CIM) |
| 模型精细度 | móxíng jīngxìdù | Level of model detail (LOD analogue) |
| 分类和编码 | fēnlèi hé biānmǎ | Classification and coding |
| 住房和城乡建设部 | zhùfáng hé chéngxiāng jiànshè bù | MOHURD |
| 自主可控 | zìzhǔ kěkòng | Self-reliant / independently controllable (software policy) |
| 报建 | bàojiàn | Building permit application |
| 交付 | jiāofù | Delivery |
| 构件 | gòujiàn | Building component / element |
| 属性集 | shǔxìng jí | Property set |
| 坐标系 | zuòbiāo xì | Coordinate system |

## Typical questions people ask about this

All questions below are **(illustrative)**; no real forum questions could be retrieved in this session.

1. (illustrative) Is IFC mandatory for BIM delivery in China?
2. (illustrative) Which GB/T standard defines BIM data storage, and does it use IFC?
3. (illustrative) How do I export IFC from Revit with Chinese property names without garbled text?
4. (illustrative) What coordinate system should an IFC model use for a Chinese project (CGCS2000)?
5. (illustrative) Which IFC version do Chinese review platforms accept: IFC2x3 or IFC4?
6. (illustrative) What does the classification code from GB/T 51269 look like and where is it stored in IFC (IfcClassificationReference)?
7. (illustrative) What model detail level does GB/T 51301 require at construction-drawing stage?
8. (illustrative) How does BIM-based drawing review work in Shenzhen or Guangzhou?
9. (illustrative) Can I submit Revit RVT instead of IFC to a local review portal?
10. (illustrative) How do I check an IFC file against Chinese property-set requirements (IDS)?
11. (illustrative) Which Chinese software exports IFC4 and how good is it?
12. (illustrative) What are CIM platforms and how do they consume BIM models?
13. (illustrative) How are millimetre units and elevation conventions handled when exchanging IFC with foreign partners?

## Common pitfalls and misconceptions

- Assuming there is a single national "BIM mandate" with one threshold: it is local and project-type specific (unverified).
- Assuming GB/T means mandatory: GB/T is recommended; local rules or contracts can make it binding.
- Confusing GB/T 51447 (storage) with GB/T 51301 (design delivery) or GB/T 25507 (IFC platform spec) (unverified numbers; double-check).
- Encoding: Chinese characters in IFC STEP files must be escaped; a tool that writes raw UTF-8 may fail validation (general IFC knowledge).
- Mixing coordinate systems: local site coordinates vs CGCS2000 vs WGS84 for CIM.
- Trusting this document's unverified items without checking the official standard text.

## Test ideas for MCP servers (derived, not from sources)

- Open an IFC with Chinese names in IfcProject/IfcSpace and verify round-trip of text.
- Query properties by Chinese property-set names; filter elements by classification code.
- Set IfcMapConversion with CGCS2000-like projected CRS and read it back.
- Ask the MCP to list required property sets for a "construction drawing review" and expect a clear "needs official standard" answer rather than invented numbers.

## Sources

- [1] Chinese Wikipedia, "建筑信息模型": https://zh.wikipedia.org/wiki/建筑信息模型 (read; confirms GB/T 51212-2016 name and BIM definition; no MOHURD document numbers).
- [2] English Wikipedia, "Industry Foundation Classes": https://en.wikipedia.org/wiki/Industry_Foundation_Classes (read; IFC version table, IFC4.3 Add2 2024, ISO 16739-1:2024).
- buildingSMART GitHub organisation: https://github.com/buildingSMART (read; lists IFC4.x-development, validate, IDS, bSDD repositories).
- [3] GB/T 51212-2016 listing: https://www.chinesestandard.net/PDF/English.aspx/GBT51212-2016 (commercial database; issue 2016-12-02, effective 2017-07-01).
- [4] GB/T 51235-2017 listing: https://www.chinesestandard.net/PDF/English.aspx/GBT51235-2017 (issue 2017-05-04, effective 2018-01-01).
- [5] GB/T 51269-2017 listing: https://www.chinesestandard.net/PDF/English.aspx/GBT51269-2017 (issue 2017-10-25, effective 2018-05-01).
- [6] GB/T 51301-2018 record in the national standards library (ndls.org.cn) as surfaced by search: https://ndls.org.cn/standard/detail/dfa334cb2d5e042ed34efe57c30e44d2 (issue 2018-12-26, effective 2019-06-01; re-check the entry on the page).
- [7] GB/T 51447-2021: https://www.chinesestandard.net/PDF/English.aspx/GBT51447-2021 (status valid, issuers MOHURD and SAMR) and MOHURD announcement No. 160 of 2021 with effective date 2022-02-01 as reported by search results (dates not shown on the database page itself).
- [8] JGJ/T 448-2018 listing: https://www.chinesestandard.net/PDF/English.aspx/JGJT448-2018 (issue 2018-12-06, effective 2019-06-01).
- [9] GB/T 25507-2010 listing: https://www.chinesestandard.net/PDF/English.aspx/GBT25507-2010 and ISO/PAS 16739:2005 page https://www.iso.org/standard/38056.html (withdrawn ISO edition).
- [10] Provincial documents citing 建质函〔2015〕159号 (found via search): https://www.gz.gov.cn/attachment/0/53/53174/5566422.docx
- [11] 建质函〔2016〕183号 date (secondary list): https://www.chyxx.com/industry/202001/829993.html (industry portal, secondary).
- [12] 建市〔2020〕60号 implementing documents: https://www.cq.gov.cn/zwgk/zfxxgkml/szfwj/qtgw/202307/W020230713556032236919.doc (Chongqing government file).
- [13] Shenzhen Housing and Construction Bureau, SJG 114-2022 and BIM quality-check points: https://zjj.sz.gov.cn/attachment/1/1455/1455847/9822299.pdf and https://zjj.sz.gov.cn/attachment/1/1538/1538395/11962319.docx
- [14] buildingSMART Poland, "IFC Mandate" material: https://buildingsmart.org.pl/wp-content/uploads/2024/10/IFC-Mandate-Final-1.pdf (PDF text not machine-readable in this session; the Shenzhen figures come from a search-engine summary of it, unverified).
- [15] buildingSMART chapter directory: https://www.buildingsmart.org/community/chapter-directory/buildingsmart-china and https://www.buildingsmart.org/community/chapter-directory/buildingsmart-hong-kong
- [16] BIMBase / PKPM-BIM context (CABR article reprint and CIC exhibit page, vendor claims): https://m.thepaper.cn/baijiahao_29995484 and https://citac.cic.hk/en-hk/exhibitions/exhibits/611

## Gaps

- The web-search budget was exhausted (zero searches ran); no search-engine results were available.
- QA pass: MOHURD full-text notices, 建市〔2022〕11号, Guangzhou/Nanjing/Hunan/Chongqing/Xiong'an specifics and the GB/T 51447 clause details could still not be confirmed from primary pages; commercial standards-database listings [3]-[9] were used for dates and are not official MOHURD pages.
- Unreachable or failed (original session): mohurd.gov.cn (DNS error), buildingsmart.org chapters pages (HTTP 403), iso.org (403), standards.buildingsmart.org IFC4.3 docs (403), Baidu Baike (403), bimbase.com (TLS error), zh.wikipedia IFC page (404), en.wikipedia "BIM in China" (404).
- Not verified at all: effective dates of all GB/T standards, MOHURD document numbers, Shenzhen "SZ-IFC", Guangzhou/Nanjing/Hunan/Chongqing/Xiong'an specifics, GB/T 51447 content details, buildingSMART China chapter, official portals, real forum questions, open-source projects.
- No suspicious or pirated sites were encountered.
- Recommended follow-up: rerun with search access, targeting MOHURD standards announcements, the national standards platform, and city housing bureau sites.
