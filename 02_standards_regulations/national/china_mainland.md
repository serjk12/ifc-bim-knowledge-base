# Mainland China: BIM/IFC standards and BIM-based review

**Last researched: 2026-11-06**

> **RESEARCH STATUS WARNING (read first).** This document was produced under a severely limited research session: the web-search budget was exhausted before any search ran, and most primary Chinese sources (MOHURD, the national standards platform, Baidu Baike, ISO, buildingSMART chapter pages) were unreachable (HTTP 403/404, DNS or TLS errors). Only two sources were actually read (listed in Sources). Everything else is background knowledge and is marked **(unverified)**. Treat every standard number, date and document number marked unverified as a lead to confirm, not a fact. No URLs were invented; where an official link is unknown it is omitted. A second pass is needed (see Gaps).

## In plain words

China does not have one national law that says "all buildings must be delivered as IFC". Instead, the Ministry of Housing and Urban-Rural Development (MOHURD, 住房和城乡建设部) issues national BIM standards (the GB/T 51xxx series) and policy guidance, and provinces and cities add their own requirements: BIM in public-investment projects, BIM-based drawing review (施工图审查), and CIM (City Information Model) platforms. National standards are mostly "recommended" (GB/T = recommended national standard; GB = mandatory), but local governments can make BIM delivery mandatory for certain project types. IFC is the international exchange format that Chinese standards reference; the national storage standard GB/T 51447-2021 is built around IFC-like data organisation, while many local review platforms use their own data rules, often with domestic software and sometimes private/IFC-derived formats. For a QA tester: expect Chinese-language property names, GB/T-based classification codes, a CGCS2000 coordinate system, and MCP servers that must cope with GBK/UTF-8 text and non-English property sets.

## National standards (GB/T series) - status of knowledge

The only item directly confirmed in this session is the first row's name and its description as China's first engineering-construction BIM application standard [1]. All other details are from memory.

| Standard | Chinese name | English name | Notes |
|---|---|---|---|
| GB/T 51212-2016 | 建筑信息模型应用统一标准 | Unified Standard for BIM Application | Confirmed existence/name [1]. Defines BIM; effective 2017-07-01 (unverified). |
| GB/T 51235-2017 | 建筑信息模型施工应用标准 | Standard for BIM Application in Construction | Effective 2018-01-01 (unverified). |
| GB/T 51269-2017 | 建筑信息模型分类和编码标准 | BIM Classification and Coding Standard | Based on ISO 12006-2 / OmniClass-style tables; effective 2018-05-01 (unverified). |
| GB/T 51301-2018 | 建筑信息模型设计交付标准 | Standard for BIM Delivery in Design | Defines model element granularity/LOD-like levels and delivery content; effective 2019-06-01 (unverified). |
| GB/T 51447-2021 | 建筑信息模型存储标准 | BIM Storage Standard | Defines BIM data storage logical architecture, aligned with IFC; effective date unverified (believed early 2022). |
| JGJ/T 448-2018 | 建筑工程设计信息模型制图标准 | Standard for Drawing of Building Design Information Models | Industry standard (JGJ = construction industry); effective 2019-03-01 (unverified). |
| GB/T 25507-2010 | 工业基础类平台规范 | IFC platform specification | Chinese adoption of IFC (believed IFC2x3-era); (unverified). |

Practical consequences (all unverified unless stated):
- GB/T 51269 gives the classification table codes (e.g. 41-xx element classes) used in model properties; Chinese models often carry a "分类编码" / "构件编码" parameter.
- GB/T 51301 sets "模型精细度" (LOD 100-500 analogue, e.g. 1.0-4.0 levels) and requires property tables per discipline.
- GB/T 51447 is the standard to cite when a request says "store/exchange BIM as an open format in China"; it describes data layers (resource, core, shared, domain) closely following IFC (unverified detail).

## Policies and mandates

Federal-style "who mandates" in China is layered:

| Level | Body | What (all unverified; confirm numbers) |
|---|---|---|
| National | MOHURD | 2015 "关于推进建筑信息模型应用的指导意见" (document number believed 建质函〔2015〕159号): targets BIM usage rate in new large public projects by 2020. |
| National | MOHURD | 2016-2020 "建筑业信息化发展纲要" (believed 建质函〔2016〕183号): BIM integration. |
| National | MOHURD and other ministries | 2020 "关于推动智能建造与建筑工业化协同发展的指导意见" (believed 建市〔2020〕60号): smart construction, BIM + digital delivery. |
| National | MOHURD | 14th Five-Year Plan for the construction industry (2022, believed 建市〔2022〕11号): BIM-based review and delivery, CIM platforms. |
| National | MOHURD | CIM basic platform technical guidelines (2020, number unverified). |
| Provincial/municipal | Housing bureaus, planning/natural resources bureaus | Local BIM application guidelines; BIM mandatory for government-invested projects above an area/investment threshold (thresholds vary by city, unverified). |

Thresholds typically appear as "public buildings above N m2 or investment above N million RMB" with N set locally. Do not state a single national threshold.

## Local BIM review / permit systems and CIM platforms (all unverified)

China has an unusual feature: some cities accept or require **BIM models in drawing review and permits**.

| City/area | Known concept | Notes |
|---|---|---|
| Shenzhen | BIM-based building permit and drawing review; local data standard referred to as "SZ-IFC" in the task brief | Name and exact documents not verified; do not rely on it. |
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
| PKPM / PKPM-BIM | 北京构力科技 (PKPM) | Structural design; IFC export. |
| YJK | 盈建科 | Structural analysis; IFC link. |
| BIMBase | domestic self-controlled platform (vendor unverified) | Own graphics engine; relevant to 自主可控 (self-reliant) policy. |

"Domestic software policy" (国产化/自主可控, XinChuang) pushes government-related projects towards domestic BIM platforms; the exact rules are not verified.

## Key organizations

- MOHURD (住房和城乡建设部): standards and policy.
- Standards committees and institutes: China Academy of Building Research (中国建筑科学研究院), China Institute of Building Standard Design (中国建筑标准设计研究院) (roles unverified).
- buildingSMART: the chapter structure for mainland China was not verified (the chapters page returned HTTP 403). Hong Kong and Taiwan have separate chapters (unverified).
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

## Gaps

- The web-search budget was exhausted (zero searches ran); no search-engine results were available.
- Unreachable or failed: mohurd.gov.cn (DNS error), buildingsmart.org chapters pages (HTTP 403), iso.org (403), standards.buildingsmart.org IFC4.3 docs (403), Baidu Baike (403), bimbase.com (TLS error), zh.wikipedia IFC page (404), en.wikipedia "BIM in China" (404).
- Not verified at all: effective dates of all GB/T standards, MOHURD document numbers, Shenzhen "SZ-IFC", Guangzhou/Nanjing/Hunan/Chongqing/Xiong'an specifics, GB/T 51447 content details, buildingSMART China chapter, official portals, real forum questions, open-source projects.
- No suspicious or pirated sites were encountered.
- Recommended follow-up: rerun with search access, targeting MOHURD standards announcements, the national standards platform, and city housing bureau sites.
