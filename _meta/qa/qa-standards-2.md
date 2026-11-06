# QA log: standards-2 (national regulations + open-source catalog)

**Date:** 2026-11-06
**Scope:** `02_standards_regulations/national/` (all files that existed at start except the ones assigned to QA pass 1, plus `africa.md`, which appeared during the pass) and all `04_open_source/*.md`.
**Method:** each key claim (standard numbers, effective dates, decree and circular numbers, ISO/IFC versions, repo stars, licences, push dates, package versions, URLs) was compared with a primary or near-primary page where one was reachable. Fixes were made in place; unconfirmed items were marked "(unverified)" or given a caveat. Nothing was downloaded or executed; only web pages, public JSON metadata (GitHub API, PyPI, npm) and one official PDF circular (text extracted with a PDF reader) were read.

**Important limits of this pass**
- The shared WebSearch budget ran out after about a dozen searches (China only). After that only direct page fetches were possible, so the Russian decrees and several Latin America, Nordic and Baltic items could not be re-verified and keep their "(unverified)" marks.
- Blocked or unusable during the pass: iso.org (403), buildingsmart.org and technical.buildingsmart.org (403), planalto.gov.br (access denied page), pravo.gov.ru / consultant / garant (guessed document URLs gave 404 or connection refused), the buildingSMART Poland PDF (compressed, not machine-readable), GitHub API rate limit (about 55 repositories read, then 403).
- No pirated, crack, phishing or otherwise suspicious sites were encountered or linked in this pass.

## 1. Corrections made (errors found and fixed)

| File | Was | Now | Evidence |
|---|---|---|---|
| `national/china_mainland.md` | JGJ/T 448-2018 effective 2019-03-01 | Effective **2019-06-01** (issued 2018-12-06) | chinesestandard.net listing (commercial database) |
| `national/china_mainland.md` | GB/T 25507-2010 "believed IFC2x3-era" | Identical adoption (IDT) of **ISO/PAS 16739:2005 (IFC2x)**, effective 2011-05-01 | chinesestandard.net listing; ISO page for the withdrawn PAS edition |
| `national/china_mainland.md` | GB/T 51447-2021 effective "believed early 2022" | MOHURD announcement No. 160 of 2021, effective **2022-02-01** | ndls.org.cn and search results; database page confirms "Valid" |
| `national/china_mainland.md` | GB/T 51212 / 51235 / 51269 / 51301 dates marked unverified | Confirmed: 2017-07-01, 2018-01-01, 2018-05-01, 2019-06-01 (issue dates added) | chinesestandard.net listings |
| `national/china_mainland.md` | Shenzhen "SZ-IFC" only "in the task brief" | Real: local standard **SJG 114-2022** (issued 2022-05-25, effective 2022-06-15); SJG 76-2020 and SJG 157-2024 also named; mandate figures from a buildingSMART Poland material kept as secondary/unverified | zjj.sz.gov.cn documents surfaced by search |
| `national/china_mainland.md` | buildingSMART China chapter "not verified" | Chapter exists in the official directory; Hong Kong is a separate full chapter (2019) | buildingsmart.org directory entries |
| `national/china_mainland.md` | BIMBase vendor "unverified" | Developed by China Academy of Building Research (launched 2021, vendor claim); PKPM-BIM (Beijing Glory PKPM Technology) runs on it | CABR article reprint, CIC exhibit page |
| `national/china_mainland.md` | MOHURD document numbers "believed" | 建质函〔2015〕159号, 建质函〔2016〕183号 (2016-08-23), 建市〔2020〕60号 confirmed via secondary/local documents; 建市〔2022〕11号 still unverified | provincial documents, industry portal |
| `national/russia.md` | Art. 57.4 ГрК attributed to "Federal Law 342-ФЗ of 30.12.2020" | Attribution removed and flagged as likely wrong (342-ФЗ is dated 3 Aug 2018 by recollection; real law unverified, possibly 472-ФЗ of 27.12.2019) | recollection only, flagged unverified |
| `national/russia.md` | IFC4 Add1 "(2015)" | IFC4 Add1 (Jun 2015) | ru.wikipedia IFC page |
| `national/uk_ireland.md` | IMI Framework lists "PAS 1192-6:2018" and years for each ISO 19650 part | Current page lists **BS EN ISO 19650-6** (health and safety), plus BS 8587, BS 8544, BS EN ISO 41001; no PAS 1192-6; part years (6 = 2025) added from Wikipedia | imiframework.org/standards; en.wikipedia ISO 19650 |
| `national/france_francophone.md` | "68.75% of competitions" and undated 15.34% market share | 68.75% is the share where BIM competence was required in the team; 15.34% is undated on the page (earlier points 5.39%, 11.74%) | fr.wikipedia |
| `national/france_francophone.md` | SQI 6D "2024-2026", PTNB year 2015 stated flatly | 6D exploration 2024-2025, deployment 2025-2026; PTNB "20 janvier" has no year on the page (2015 inferred) | SQI roadmap page; fr.wikipedia |
| `national/germany_austria_switzerland.md` | VDI 2552 Blatt 4 draft title "Modellierung von Fach- und Teilmodellen" | "Anforderungen an die Modellierung von Fach- und Teilmodellen" (draft, 2026-05) | vdi.de handbook page |
| `national/spain_portugal_italy.md` | "since Revit 2023 the open-source exporter is bundled" | Claim downgraded to unverified; open-source (LGPLv2) status confirmed | revit-ifc README |
| `national/nordics_baltics.md` | Randselva bridge Tekla award stated as sourced | Not found on the cited Norwegian Wikipedia page: marked unverified | no.wikipedia |
| `04_open_source/mcp_servers_and_ai_tools.md` | revit-mcp "archived 2026-02-25"; aps-mcp-server-nodejs "archived 2026-05-07" | These are the last-push dates of archived repositories; wording fixed | GitHub API |
| `04_open_source/mcp_servers_and_ai_tools.md` | mcp-servers-for-revit described as "successor monorepo" | Its own description calls it a "Sparx fork" of revit-mcp; wording fixed | GitHub API |
| `04_open_source/mcp_servers_and_ai_tools.md` | arXiv 2510.02634 described as an "ASHRAE 90.1 lighting case" | Abstract describes DOE COMcheck energy-code review; ASHRAE detail marked unverified; dates added for 2601.00809 (v1 21 Dec 2025, v2 28 Mar 2026) and 2511.05533 | arxiv.org abstract pages |
| `04_open_source/libraries_and_toolkits.md` | ifcJSON repo path `buildingSMART/ifcJSON` | Repository now `buildingsmart-community/ifcJSON` | GitHub API |
| `04_open_source/libraries_and_toolkits.md` | IFC++ "not actively developed" without nuance | Confirmed in README, but API shows a push on 2026-10-26; caveat added; also noted PyPI has an unrelated `ifc-mcp` 0.2.12 package | GitHub README/API; PyPI JSON |
| `04_open_source/sample_ifc_files.md` | Certification-datasets licence stated as CC BY 4.0 flatly | Only the copyright line was visible; GitHub reports NOASSERTION: caveat added | GitHub page/API |
| `04_open_source/llm_bim_research_and_datasets.md` | ifc-bench v2 paper "submitted to Automation in Construction" | Dataset card now cites it as published (AiC 2026, vol. 192); arXiv submission date 3 May 2026 added | Hugging Face card; arXiv |

## 2. Claims confirmed against sources (no change needed beyond a "re-confirmed" note)

| File | Confirmed |
|---|---|
| `national/singapore.md` | 23 Jul 2026 circular (APPBCA-2026-12 / URA/PB/2026/08-DCG): mandatory for new projects of 5,000 m2 GFA and above from 1 Oct 2026; below 5,000 m2 voluntary; ongoing CORENET 2 projects may continue; 10 Sep 2025 circular reference numbers; more than 140 projects and 300 firms; COP editions (First Sep 2023 ... Fourth Sep 2026, effective 1 Jan 2027); mapping file `industry-mapping-09-2026.xlsx`, version 22 September 2026. Not confirmable on the timeline page: the 18 Dec 2023 soft-launch date. |
| `national/uk_ireland.md` | All 12 CWMF milestones and the Stage 1 rule; four core standards (ISO 19650, Uniclass, IFC, ICMS) with no IFC version; Construction Playbook first published 8 Dec 2020, last updated 11 Jul 2023, 14 policies; NISTA launched 1 Apr 2025 with NIC and IPA absorbed; roadmap published 13 Sep 2021. |
| `national/north_america.md` | COBie timeline (2007, 2.26 in 2009, Dec 2011, 2014, 2015, 2017); IFC version table (IFC4.1 and 4.2 withdrawn, IFC4.3 Add2 2024, ISO 16739-1:2024); revit-ifc LGPLv2 and "latest + two previous" policy; IfcOpenShell parse/geometry support statement. |
| `national/japan_korea.md` | BIM drawing review start 2026-04-01; BIM data review basic concept September 2026; CDE spec Ver 1.00 Rev 1.00a (March 2024); bSJ certified software, MVD versions and certification periods; bSK statement of IFC 4.3.2.0 as latest and IFC5 in development. |
| `national/netherlands_belgium_luxembourg.md` | IFC 2x3 TC1 on "pas toe of leg uit" (registered 26-05-2011, decided 15-11-2011); NL-SfB ownership to Ketenstandaard on 1 Apr 2026; BIM basis ILS v1.0 / v2.0 file sets and the "ILH" German title quirk. |
| `national/germany_austria_switzerland.md` | BMV press release 24/2026 dated 27.03.2026 (BIM becomes "Regelprozess" for federal trunk roads); all VDI 2552 sheet dates; ÖNORM A 6241-2 2026-09-01 shop entry (draft/current ambiguity remains); Vienna openBIM permit page (versions, IFC2x3 and IFC4 Add2 TC1, WienBV, parallel PDF submission). |
| `national/spain_portugal_italy.md` | Art. 43 D.Lgs. 36/2023 (1 Jan 2025, EUR 2 million, open non-proprietary formats, comma 5 repealed by D.Lgs. 209/2024); DM 560/2017 of 1 Dec 2017; UNI 11337-4:2017 LOD A to G and -6 dimensions. |
| `national/latin_america.md` | Camacol BIM Kit Vol. 1 to 3 document list (page does not mention IFC). |
| `national/africa.md` | SANS 19650-1 (16 Sep 2022), -2 (5 Jun 2023), -3 pending, TC 59 to TC 267; Egypt Decision 302/2025 (gazette issue 103, 10 May 2025, effect computed 11 Nov 2025); South Africa review ("15%", Stage 0-1, recommendations not adopted). |
| `national/nordics_baltics.md` | Statsbygg 2.7 million m2 in 2,350 buildings (115 abroad); BIM-tekniker 60 credits since 2008. |
| `national/france_francophone.md` | SQI roadmap April 2021 to March 2026, eight committed owners, update of 31 March 2025, Sommet BIM+ 17-18 Nov 2026; SQI thresholds CAD 50 M (2021) and 10 M (2023); JO term 29 Jan 2019; professional titles by arretes of 12 Jul 2019. |
| `04_open_source/mcp_servers_and_ai_tools.md` | About 45 repositories: stars, licences, last-push dates and archived flags match the catalog (for example IfcOpenShell 2.9k stars, ifc-lite 461, revit-mcp 477 archived, rvt-mcp 117, Horizun 79, aec-model-bridge 118, tapir 131, ifc-ruhsat 3, Daviidro 0); npm versions (`@ifc-lite/mcp` 0.29.0, `ifc-mcp` 0.2.0, `@shuotao/revit-mcp-server` 1.6.0, `mcp-server-for-revit` 1.0.0, `ifc-viewer-mcp` 1.0.0) and PyPI `ifc-ruhsat` 0.2.1; Bentley MCP server list and availability; MCP4IFC and building-code-review papers. |
| `04_open_source/libraries_and_toolkits.md` | ifcopenshell 0.9.0.post1 (2026-10-15), 0.9.0 (2026-09-29), 0.8.5 (2026-04-13); Python `>=3.10,<3.16`; `ifcopenshell-mcp` 0.9.0 on PyPI; web-ifc 0.0.78 MPL-2.0; @thatopen/components and fragments 3.6.0 MIT; xBIM 582 stars, CDDL, .NET Standard 2.0/2.1, .NET 8, .NET 10; xeokit-sdk 949 stars AGPL-3.0; BIMserver 1.8k stars AGPL-3.0. |
| `04_open_source/sample_ifc_files.md` | Certification-datasets folder structure and move of community content; Community-Sample-Test-Files structure, "NOT official", Git LFS; IfcOpenShell `files` naming rules; KIT examples table and "unrestricted use" terms. |
| `04_open_source/llm_bim_research_and_datasets.md` | ifc-bench dataset card (1,027 pairs, 51 models, 22 projects, category counts 152/569/112/194, 514-question test split, GPLv3 models); arXiv 2605.01698 (1,027 tasks, 37 models, 21 projects), 2607.26072 (143 tasks, 19 projects, 4,016 sessions, 32.4%), 2408.08054 (v1 15 Aug 2024, v2 11 Jul 2025), 2508.05676 (1,740 queries). |
| `04_open_source/community_projects_and_enthusiasts.md` | OSArch chat (Matrix and IRC only, no Discord); OSArch Revit setup page and its "not audited above Revit 2018" caveat; revit-ifc tags (IFC_v27.4.0.30 latest); IFC+SG mapping file page; Awesome-AECO exists (39 stars, CC0). |

## 3. Residual uncertainty (still marked "(unverified)" or secondary)

- **Russia:** all Government decree numbers and dates (ПП 331, ПП 1431), the ГрК article for the information model, СП 328/331/301, ГОСТ Р 10.0.03 title, КСИ approving order, ФГИС ЦС URL. Search budget exhausted; official portals not reachable by guessed URLs.
- **China:** 建市〔2022〕11号, Guangzhou/Nanjing/Hunan/Chongqing/Xiong'an specifics, GB/T 51447 clause details, the Shenzhen mandate thresholds (secondary: search summary of a buildingSMART Poland PDF). Effective dates come from commercial standards databases, not MOHURD text.
- **Brazil:** Decreto 9.983/2019 and 10.306/2020 text and phase dates (planalto.gov.br blocked); the earlier first-strategy decree number is a recollection.
- **Nordics and Baltics:** Denmark (IKT-bekendtgørelsen, CCS), Sweden (CoClass vs BSAB, Trafikverket), Finland (COBIM, YTV), Estonia, Latvia, Iceland, Statsbygg BIM manual details: unchanged, still unverified.
- **Switzerland:** SIA 2051 withdrawal; **Austria:** ÖNORM A 6241-2 status; **Germany:** DIN overview dates, ARS 05/2026 and Masterplan texts (the press release does not name them).
- **Spain/Portugal/Italy:** es.BIM plan phases, CT 197 documents, DM 312/2021 content, UNI 11337 part list beyond -4 and -6.
- **Morocco chapter status and the 50 M MAD circular claim** (africa.md), Ethiopia/Kenya timing.
- **Open-source catalog:** star counts and push dates are snapshots and change daily; registries smithery.ai, mcp.so, glama.ai, mcpservers.org and most Chinese/Japanese/Russian blogs were never read. Repositories not re-read because of the GitHub rate limit: smartaec/ifcMCP (stars, licence, tool list confirmed by page only), vinnividivicci/ifc-ids-mcp (stars, licence, 17 tools confirmed by page), teknovizier/tekla_mcp_server (stars, licence, modules confirmed by page), xBimTeam sub-repos, xeokit-convert, specklesystems, sylvainHellin/cobbie, streletskiy/archi-helper, vicquick/vwx-mcp, sharafutdinovdi/revit-model-mcp.
- Vendor claims (BIMBase "100% own code", Horizun benchmark, ifc-ruhsat regulation details, Fukui Computer permit-timeline page) remain vendor-reported.

## 4. Not covered in this pass

- Files that appeared in `national/` while this pass was running (`central_eastern_europe.md`, `cis_central_asia.md`, `middle_east.md`, `oceania_south_asia.md`, `southeast_asia_other.md`, `taiwan_hongkong_macau.md`) were still being written and were not checked.
- Everything outside `02_standards_regulations/national/` and `04_open_source/` (including `01_ifc_basics/`, `03_software/`, `08_glossary/`) was not touched.
