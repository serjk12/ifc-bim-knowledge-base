# Sources index: where the knowledge in this base comes from

## In plain words

This file is a map of every useful web address that the research agents and the reference documents of this knowledge base (KB) relied on. It answers two questions for a tester who does not come from the BIM world:

1. "Where does this fact come from, and can I check it?" (standards, laws, vendor manuals, forum threads)
2. "Where do real people talk about this, so I can imitate how they write?" (forums, blogs, issue trackers)

IFC (Industry Foundation Classes) is the open file format for building models; Revit is Autodesk's design program that exports to it. The sources below are grouped by kind, then by country or language. Every entry is one line: the address, then what it is good for.

How this index was built: it merges (a) the "Notable sources" and "Local ecosystem" sections of all 78 wave-1 research reports in `research_raw/wave1/`, (b) the "Sources" lists of the reference documents in `01_ifc_basics/`, `02_standards_regulations/`, `03_software/`, `04_open_source/` and `08_glossary/`, and (c) the `source_url` field of the 2304 real records (see [../_meta/SPEC.md](../_meta/SPEC.md)). Duplicates were merged. Nothing here was invented: if an address appears, an agent saw it in a search result, opened it, or found it linked on a page that was opened.

## Reading guide and caveats

- **Status tags** (given where the research recorded them): `[read]` = an agent opened the page and read it; `[snippet]` = seen only as a search-result title or summary; `[blocked]` = the fetch tool got HTTP 403 or another refusal, so the content was never read by us; `[unverified]` = named in a source but not opened. Untagged entries were listed in a report as sources without a recorded status.
- The research ran on 2026-11-06 with a nearly exhausted web-search budget, so many pages were opened directly rather than discovered by search. Several large communities (Reddit, Stack Overflow, Autodesk Community, Graphisoft Community, Zhihu, CSDN) could not be read at all. See [communities_directory.md](communities_directory.md) for the access picture and "Gaps" at the end of this file.
- Thread-level addresses (single forum threads, single GitHub issues) are in the appendices at the end, because they are examples of real user language rather than general references. The full per-question mapping is in the JSONL files under `research_raw/wave1/`; use `python tools/kb.py filter --kind real --text <regex>` to find the matching records.
- Related KB documents: [IFC basics](../01_ifc_basics/01_what_is_ifc_and_versions.md), [buildingSMART standards](../02_standards_regulations/buildingsmart_standards.md), [ISO and European standards](../02_standards_regulations/iso_and_european_standards.md), [Revit IFC export](../03_software/revit/ifc_export_reference.md), [viewers and checkers](../03_software/viewers_checkers_cde_converters.md), [open-source libraries](../04_open_source/libraries_and_toolkits.md), [MCP servers](../04_open_source/mcp_servers_and_ai_tools.md), [LLM/BIM research](../04_open_source/llm_bim_research_and_datasets.md), [sample IFC files](../04_open_source/sample_ifc_files.md), [glossary](../08_glossary/glossary_multilingual.md).

## Contents

1. [Official standards and specifications](#1-official-standards-and-specifications)
2. [Governments and regulators by country](#2-governments-and-regulators-by-country)
3. [Software vendor documentation](#3-software-vendor-documentation)
4. [Open-source projects](#4-open-source-projects)
5. [Forums and Q&A sites by language](#5-forums-and-qa-sites-by-language)
6. [Blogs, educators and enthusiasts](#6-blogs-educators-and-enthusiasts)
7. [Research papers and datasets](#7-research-papers-and-datasets)
8. [Gaps: addresses that could not be read](#8-gaps-addresses-that-could-not-be-read)
9. [Appendix A: forum threads](#appendix-a-forum-threads-examples-of-real-user-language)
10. [Appendix B: GitHub issue and discussion threads](#appendix-b-github-issue-and-discussion-threads)
11. [Appendix C: articles, regional pages and vendor knowledge-base pages by language](#appendix-c-articles-regional-pages-and-vendor-knowledge-base-pages-by-language)

---

## 1. Official standards and specifications

### 1.1 buildingSMART International (owner of IFC, IDS, BCF, bSDD)

buildingSMART is the non-profit that maintains the open building-data standards. Its main sites often refuse automated fetching (HTTP 403), so the GitHub repositories and the IFC 4.3 documentation host are the reliable readable copies.

| Address | Good for |
|---|---|
| https://www.buildingsmart.org/standards/bsi-standards/industry-foundation-classes/ | Official IFC overview page `[blocked]`; cite it, but read the schema docs instead |
| https://technical.buildingsmart.org/standards/ifc/ifc-schema-specifications/ | The list of all IFC schema versions and release notes (`/ifc-release-notes/`); `[blocked]`, content known from search excerpts |
| https://technical.buildingsmart.org/standards/ifc/ifc-formats/ | File formats (STEP .ifc, .ifcXML, .ifcZIP, ifcJSON) `[blocked]` |
| https://technical.buildingsmart.org/standards/ifc/mvd/mvd-database/ | Model View Definitions (MVD): which subset of IFC a given exchange uses |
| https://technical.buildingsmart.org/resources/software-implementations/ | Which programs are certified for which IFC views |
| https://technical.buildingsmart.org/services/certification/ifc-certification-participants/ | Official list of certified software `[blocked]` |
| https://technical.buildingsmart.org/resources/ifcimplementationguidance/string-encoding/ | How non-ASCII text (Cyrillic, Chinese) must be escaped inside an IFC file (`\X2\...\X0\`); central for encoding tests `[blocked]` |
| https://technical.buildingsmart.org/resources/ifcimplementationguidance/ifc-guid/ | How the 22-character IFC GUID is built; essential for "GUID changed" questions `[blocked]` |
| https://technical.buildingsmart.org/ | Implementation guidance hub (student-level entry point) `[blocked]` |
| https://www.buildingsmart.org/standards/rooms/infrastructure/ | Infrastructure room (road, rail, bridge, IFC 4.3) `[blocked]` |
| https://www.buildingsmart.org/chapter-directory/ | List of national chapters (Norway, Japan, Korea, Spain, Netherlands and others) |
| https://www.buildingsmart.org/wp-content/uploads/2024/10/IFC-Mandate-Final-1.pdf | "Global IFC Mandates 2024": which countries require IFC `[snippet]` |
| https://ucm.buildingsmart.org/use-case-details/2553/en | Use case management; example: Statsbygg (Norway) BIM requirements |
| https://user.buildingsmart.org/knowledge-base/terminology/ | Plain-language terminology `[blocked]`; also `/how-to-deal-with-ifcclassification-using-revit-2020/` |
| https://forums.buildingsmart.org/ | Technical forum (Discourse); the richest English source of expert answers. See section 5 and Appendix A |

### 1.2 IFC schema documentation (readable copies)

| Address | Good for |
|---|---|
| https://ifc43-docs.standards.buildingsmart.org/ | IFC 4.3.2 (ISO 16739-1:2024) reference; entity pages such as `/IFC/RELEASE/IFC4x3/HTML/lexical/Pset_WallCommon.htm`, `Qto_WallBaseQuantities.htm`, `Pset_DoorCommon.htm`, `Pset_SpaceCommon.htm`. Redirects to standards.buildingsmart.org and sometimes 403 |
| https://standards.buildingsmart.org/IFC/RELEASE/IFC4_3/HTML/ | Same IFC 4.3 content on the main standards host (e.g. `lexical/IfcRoot.htm`, `IfcGloballyUniqueId.htm`) |
| https://standards.buildingsmart.org/IFC/DEV/IFC4_3/HTML/lexical/IfcAlignment.html | Alignment (road/rail axis) entity; infrastructure questions; also `IfcText.html`, `IfcTask.htm` |
| https://standards.buildingsmart.org/IFC/RELEASE/IFC4_1/FINAL/HTML/ | IFC 4.1 pages (e.g. `ifcgloballyuniqueid.htm`) |
| https://standards.buildingsmart.org/IFC/RELEASE/IFC4/FINAL/HTML/ | IFC4 final HTML (e.g. `ifcbuildingstorey.htm`) `[snippet]` |
| https://standards.buildingsmart.org/MVD/RELEASE/IFC4/ADD2_TC1/RV1_2/HTML/schema/views/reference-view/index.htm | IFC4 Reference View 1.2 definition: what a "read-only coordination export" must contain |
| https://standards.buildingsmart.org/documents/20170830_LDWG_ifcOWLontology.pdf | ifcOWL (IFC as linked data) `[snippet]` |
| https://standards.buildingsmart.org/documents/Implementation/IFC2x_Model_Implementation_Guide_V2-0b.pdf | Old IFC2x implementation guide `[snippet]` |
| https://iaiweb.lbl.gov/Resources/IFC_Releases/R2x3_final/ifcmeasureresource/lexical/text/IFC_2x2_MeasureUnit_Examples.pdf | Legacy unit examples (IFC 2x2/2x3 era) `[snippet]` |
| https://www.expresslang.org/standards | EXPRESS language, the schema language behind IFC |
| https://www.steptools.com/stds/step/IS_final_p21e3.html#clause-6-4-3 | ISO 10303-21 (STEP physical file) clause on string escapes, cited by users in encoding bugs |
| https://en.wikipedia.org/wiki/ISO_10303-21 | Plain explanation of the .ifc text file layout `[read]` |
| https://github.com/buildingSMART/IFC4.x-development | Working repository for IFC4.x schema and Q&A issues; also `IFC4.3.x-development`, `IFC4.x-IF` (implementers forum), `IFC4.3.x-sample-models` |
| https://github.com/buildingSMART/IFC5-development | Next-generation IFC (IFC5 / IFCX) discussion |
| https://github.com/buildingSMART/ifcJSON | JSON encoding of IFC |
| https://github.com/buildingSMART/mvdXML | Machine-readable MVD format |
| https://www.buildingsmart.de/buildingsmart/aktuelles/ifc-roadmap-nach-porto-version-44-kommt-ifc-5-wird-zu-ifc-x | IFC roadmap after the Porto meeting (IFC 4.4 coming, IFC5 renamed IFC-X) `[snippet]` |

### 1.3 Checking and delivery standards from buildingSMART

| Address | Good for |
|---|---|
| https://validate.buildingsmart.org | IFC Validation Service: upload an IFC and get schema and rule errors; the neutral referee in many disputes |
| https://buildingsmart.github.io/validate/user/index.html | Validation Service user guide; also `/dev/rule_details.html` for rule descriptions |
| https://github.com/buildingSMART/validate | Validation service source and issue tracker |
| https://www.buildingsmart.org/standards/bsi-standards/information-delivery-specifications-ids/ | IDS (Information Delivery Specification) landing page `[snippet]` |
| https://github.com/buildingSMART/IDS | IDS 1.0 schema, documentation (`Documentation/README.md`) and issue tracker |
| https://github.com/buildingSMART/IDS-Audit-tool | Checks that an IDS file itself is valid |
| https://www.buildingsmart.org/?p=30065 | News: IDS v1.0 approved as final standard `[blocked]` |
| https://www.buildingsmart.org/standards/bsi-standards/bim-collaboration-format/ | BCF (issue-exchange format) landing page `[snippet]` |
| https://github.com/buildingSMART/BCF-XML | BCF file format spec; https://github.com/buildingSMART/BCF-API for the web API |
| https://github.com/buildingSMART/documents-API | openCDE documents API; also `foundation-API` |
| https://search.bsdd.buildingsmart.org | buildingSMART Data Dictionary (bSDD) search: classes, properties, classification codes |
| https://manage.bsdd.buildingsmart.org | bSDD dictionary management |
| https://github.com/buildingSMART/bSDD | bSDD API and docs |
| https://www.buildingsmart.org/ifc-4-3-approved-as-a-final-standard/ | News: IFC 4.3 approved `[snippet]`; companion https://www.buildingsmart.org/?p=29521 (published as ISO) |

### 1.4 ISO, CEN and national standards bodies

| Address | Good for |
|---|---|
| https://www.iso.org/standard/70303.html | ISO 16739-1:2018 (IFC4) catalogue entry |
| https://www.iso.org/standard/84123.html | ISO 16739-1:2024 (IFC 4.3) catalogue entry |
| https://genorma.com/en/standards/en-iso-16739-1-2024 ; https://dinmedia.de/en/standard/din-en-iso-16739-1/379635818 ; https://www.evs.ee/en/evs-en-iso-16739-1-2020 | European adoptions (EN ISO 16739-1) in CEN member catalogues |
| https://www.evs.ee/en/evs-en-iso-19650-2-2018 | EN ISO 19650-2:2018 (information management during delivery) |
| https://jcvirtualpm.co.uk/2026/10/12/iso-19650-revision-2026-what-is-changing-and-when/ | Secondary blog on the ISO 19650 revision |
| https://www.iso.org/standard/88515.html ; https://www.iso.org/standard/88516.html ; https://www.iso.org/standard/81261.html | ISO 29481-1/-2/-3 (Information Delivery Manual, the parent idea of IDS) `[snippet]` |
| https://committee.iso.org/sites/tc59/home/news/content-left-area/news-and-updates/iso-29481-12016-is-published.html ; https://scc-ccn.ca/standardsdb/standards/8190063 | ISO 29481-1 history |
| https://genorma.com/en/standards/cen-tr-17741-2021 ; https://evs.ee/en/cen-tr-17654-2021 | CEN technical reports on IDM guidance and EIR |
| https://genorma.com/en/standards/fpren-iso-7817-1 ; https://www.dinmedia.de/de/norm/din-en-iso-7817-1/382382712 | EN ISO 7817-1 (level of information need, LOIN) |
| https://genorma.com/en/standards/iso-12006-3-2022 ; https://www.evs.ee/en/evs-en-iso-12006-3-2022 ; https://isrsm.gov.mk/en/project/show/iso:proj:75401 | ISO 12006-3 and ISO 23386 (data dictionaries behind bSDD) |
| https://standards.iteh.ai/catalog/tc/cen/b0e05107-d6bf-4c1c-b222-54dd974f1a96/cen-tc-442 ; https://www.en.une.org/normalizacion_documentos/CENTC-442-activities---Oivind-Rooth.pdf ; https://www.buildwise.be/media/ml3foa2a/nabimdigitalconstruction_overviewcentc442_fr.pdf | CEN/TC 442, the European BIM standardisation committee |
| https://www.dinmedia.de/de/technische-regel/din-spec-91391-1/302483139 ; https://www.baunetzwissen.de/integrales-planen/tipps/news/neue-norm-din-spec-91391-fuer-die-bim-planung-6467834 | DIN SPEC 91391 (German CDE and exchange); the second link is a plain-German explainer |
| https://www.vdi.de/richtlinien/details/vdibs-2552-blatt-111-building-information-modeling-informationsaustauschanforderungen-zu-bim-anwendungsfaellen ; https://www.vdi.de/richtlinien/details/vdi-handbuch-building-information-modeling | VDI/buildingSMART 2552 series (use-case information requirements, e.g. openings) |
| https://www.austrian-standards.at/en/shop/onorm-a-6241-2-2026-09-01~p5058043 | ONORM A 6241-2 (Austria) |
| https://www.uni.com/ | UNI (Italy) index; UNI 11337 detail not found |
| https://cn.gostinfo.ru/catalog/Details/?id=6453898 | GOST R 10.0.02-2019 catalogue entry (Russian adoption of IFC concepts) |
| https://pravo.ppt.ru/prikaz/rosstandart/n-618-st-185754 ; https://www.normacs.info/articles/921 ; https://www.akm.ru/press/minstroy_rossii_obnovil_klassifikator_stroitelnoy_informatsii/ | Russian classifier of construction information (KSI) orders and news |
| https://www.chinesestandard.net/PDF/English.aspx/GBT25507-2010 ; https://www.chinesestandard.net/PDF/English_MS.aspx/GBT51269-2017 ; https://www.chinesestandard.net/PDF/English_MS.aspx/GBT51212-2016 | Chinese national standards (GB/T 25507 IFC adoption, GB/T 51269 classification, GB/T 51212 BIM application) as sold by a standards reseller; titles only |

### 1.5 Classification systems, COBie and level-of-detail

| Address | Good for |
|---|---|
| https://www.thenbs.com/tools/uniclass ; https://www.thenbs.com/knowledge/uniclass-tables-explained ; https://www.thenbs.com/knowledge/uniclass-2015-january-2022-update | Uniclass 2015 (UK classification) |
| https://www.thenbs.com/knowledge/what-is-the-buildingsmart-data-dictionary ; https://thenbs.com/knowledge/nbs-bim-toolkit-changes-in-2022 | NBS explanations of bSDD and the digital toolkit |
| https://www.csiresources.org/standards/omniclass/standards-omniclass-about | OmniClass / Uniformat (North America) |
| https://byggtjanstcms.byggtjanst.se/contentassets/d56221107b144d7496f2a9795882f851/coclass-blad-20201124.pdf ; https://vpp.sbuf.se/Public/Documents/ProjectDocuments/56b8fb0a-f12e-45b0-ab49-30521fa4b649/FinalReport/SBUF%2013172%20Slutdokumentation-CoClass-v1.2.pdf | CoClass (Sweden) |
| https://www.digigo.nu/standaarden/nlsfb/ ; https://ketenstandaard.nl/nlbe-sfb-facts/ | NL-SfB (Dutch classification, owned by Ketenstandaard Bouw en Techniek from 1 April 2026) |
| https://www.etim-international.com/etim-10-0-now-available-in-the-buildingsmart-data-dictionary/ | ETIM product classification inside bSDD |
| https://structurae.net/en/literature/journal-article/comparative-study-of-construction-information-classification-systems-cci-versus-uniclass-2015 ; https://architektur-informatik.scix.net/pdfs/w78-2023-paper_33.pdf | Comparative papers on classification systems |
| https://nibs.org/nbims/v3/cobie/ ; https://www.nibs.org/cobie ; https://nibs.org/nbims/v3/cobie/6-2/ | COBie v3 (building handover data); `6-2` maps COBie to IFC 4.3 |
| https://www.nibs.org/files/pdfs/nbimsv3/NBIMS-US_V3_4.2_COBie_Annex_A.pdf ; https://www.nationalbimstandard.org/files/pdfs/2023-05-26NBIMS-US_COBie_v3_Standard_DRAFT-20230501.pdf | COBie v3 annex and draft standard |
| https://catenda.com/glossary/construction-operations-and-building-information-exchange-cobie | Plain COBie glossary (vendor) |
| https://bimforum.org/LOD/ ; https://bimforum.org/2023-level-of-development-lod-specification/ | BIMForum LOD (level of development) specification |
| https://www.baunetzwissen.de/bim/fachwissen/modellinhalte/was-bedeutet-lod-loi-5285890 ; https://www.baunetzwissen.de/glossar/l/loin-9963146?thema=bim | German practitioner explainers: LOD, LOI, LOIN |
| https://nibs.org/nbims/v4/pbr/ ; https://nibs.org/nbims/v4/bep/ ; https://www.nibs.org/nbims/v4 | NBIMS-US v4 (project requirements and BIM execution plan) |

---

## 2. Governments and regulators by country

Each block lists official or quasi-official pages that define what an IFC delivery must contain. These matter to a tester because "can you check this model against our national rules?" is a very common real request. See also [../02_standards_regulations/national/](../02_standards_regulations/national/).

### 2.1 Singapore (CORENET X, IFC-SG)

| Address | Good for |
|---|---|
| https://info.corenet.gov.sg/ | Official hub of BCA/CORENET X: code of practice, IFC+SG rules, circulars, FAQ `[read]` |
| https://info.corenet.gov.sg/ifc-sg/start-here/WhatIsIFCSG | What IFC+SG is, in plain words; also `/ifcsg-onboarding-checklist` |
| https://info.corenet.gov.sg/ifc-sg/requirements---submission/ifc-sg-excel-mapping-file | The Excel mapping of Singapore IFC classes and property sets |
| https://info.corenet.gov.sg/ifc-sg/requirements---submission/ifcsg-data-structure | Required data structure |
| https://info.corenet.gov.sg/ifc-sg/modelling---authoring/bim-authoring-tools (and `/revit`, `/archicad`, `/tekla`, `/3rdpartytools`) | Tool-specific export setup for Revit, Archicad, Tekla and third-party add-ons |
| https://info.corenet.gov.sg/ifc-sg/modelling---authoring/GeneralModellingPractices ; https://info.corenet.gov.sg/ifc-sg/model-setup-and-coordination | Modelling practice and coordination model quality |
| https://info.corenet.gov.sg/submission-portal-resource/more/model-checker | The official model checker |
| https://info.corenet.gov.sg/regulatory-process/corenet-x-code-of-practice | Code of practice (COP) |
| https://info.corenet.gov.sg/overview/about-corenet-x/overview-of-corenet-x ; `/implementation-timeline` ; `/getting-ready-for-corenet-x` | Programme overview, dates, readiness |
| https://info.corenet.gov.sg/regulatory-process/about-the-new-submission-process/submission-workflows (also `/3-gateway-process`, `/direct-submission-process-(dsp)`, `/typical-submission-package`) | Submission workflows |
| https://info.corenet.gov.sg/docs/default-source/bca-circulars/circular-for-updates-to-corenet-x-implementation-plan.pdf?sfvrsn=d8a19259_1 | BCA circular of 23 Jul 2026 `[read]` |
| https://www.ura.gov.sg/guidelines/circulars/dc25-01/ | URA circular updating the CORENET X plan `[read]` |
| https://www1.bca.gov.sg/regulatory-info/building-control/corenet-x/corenet-x-faq/getting-ready | BCA FAQ `[snippet]` |
| https://portal.corenet.gov.sg/ ; https://training.corenet.gov.sg/ ; https://support.corenet.gov.sg/hc/en-us | Submission portal, training, support `[unverified]` / `[blocked]` |
| https://graphisoft.com/sg/solutions/corenet-x-and-ifc-sg ; https://interoperability.autodesk.com/singapore/ | Vendor tool pages for Singapore |

### 2.2 United Kingdom and Ireland

| Address | Good for |
|---|---|
| https://imiframework.org/ ; https://imiframework.org/standards/ | UK Information Management Initiative framework (formerly ukbimframework.org); ISO 19650 national annex and guidance |
| https://www.ukbimframework.org/wp-content/uploads/2021/02/Guidance-Part-C_Facilitating-the-common-data-environment-workflow-and-technical-solutions_Edition-1.pdf | CDE guidance (text could not be extracted) |
| https://www.cdbb.cam.ac.uk/files/eir_guidance.pdf ; https://www.cdbb.cam.ac.uk/files/national_annex_guidance.pdf | Cambridge CDBB: EIR and national annex guidance |
| https://wearenima.im/?p=160 ; https://wearenima.im/bsuki-introduction/ ; https://wearenima.im/resources/buildingsmart-data-dictionary-bsdd/ ; https://wearenima.im/resources/information-delivery-specification-ids/ | nima / bSUKI: UK bodies on ISO 19650, bSDD and IDS |
| https://www.gov.uk/government/publications/the-construction-playbook ; https://www.gov.uk/government/publications/nista-memorandum-of-understanding/nista-memorandum-of-understanding | UK public client policy |
| https://assets.publishing.service.gov.uk/media/697206e4a1311bdcfa0ed8a5/ER-DFE-XX-XX-T-X-0001-Exchange_Information_Requirements-A-C01.pdf | Real EIR example (UK Department for Education, Jan 2026) |
| https://www.designingbuildings.co.uk/wiki/Information_management_mandate ; `/Nima` ; `/Building_SMART` ; `/Information_Delivery_Manual_(IDM` | Encyclopedia-style UK explanations |
| https://bimblog.bondbryan.co.uk/guidance-notes-for-autodesk-revit-users-exchanging-models-with-graphisoft-archicad/ | Practice guide: Revit-to-Archicad exchange |
| https://cwmf.gov.ie/en/bim/ ; https://cwmf.gov.ie/en/resources/bim/core-bim-requirements/ ; https://cwmf.gov.ie/en/resources/bim/public-sector-bim-adoption-timeline/ ; https://cwmf.gov.ie/en/news/bim-requirements-in-the-cwmf-from-january-2024/ | Irish Construction Works Management Framework BIM requirements |
| https://www.tii.ie/media/krjpyopa/bim-for-infrastructure-statement-of-intent-and-roadmap.pdf ; https://bimireland.ie/?p=14168 ; https://builddigital.ie/ ; https://www.cita.ie/ | Irish infrastructure roadmap, national BIM council, industry bodies `[snippet]` |
| https://bim.natspec.org | Australia: NATSPEC BIM portal and National BIM Guide `[unverified]` |

### 2.3 Germany, Austria, Switzerland

| Address | Good for |
|---|---|
| https://www.bimdeutschland.de/ | Federal BIM initiative; downloads for AIA/BAP templates (`/bim-wissen/downloads`), MVD page, CDE page, FAQ `[read]` |
| https://www.bimdeutschland.de/fileadmin/media/Downloads/Download-Liste/BIM4INFRA/3_9_BIM4INFRA2020_AP4_Teil9.pdf | BIM4INFRA2020 part 9: IFC data exchange |
| https://fib-bund.de/Inhalt/Themen/BIM_fuer_Bundesbauten/BIM_AH_Muster-AIA.pdf ; `.../BIM_AH_Muster-BAP.pdf` ; `.../2021-11-01_BIM_Masterplan.pdf` ; `.../2023-03_Umsetzungsstrategie_BIM_Bundesbauten.pdf` | Federal building client model AIA (requirements) and BAP (execution plan), masterplan |
| https://bundesbau.de/fileadmin/user_upload/BIM_Roadmap/bbau_ah_anwendungsfallsteckbriefe_230516.pdf | Use-case sheets |
| https://www.bmv.de/SharedDocs/DE/Artikel/StB/masterplan-bim-bundesfernstrassen.html ; https://www.bundesfernstrassen-digital.de/bim/publikationen ; https://www.bim-bundesfernstrassen.de/fileadmin/user_upload/Rahmendokumente/bim-rd-aia.pdf ; https://www.deges.de/wp-content/uploads/2023/03/BIM_AIA_Muster_V201_mit_Hinweisen.pdf ; https://www.autobahn.de/storage/user_upload/qbank/Anlage_1_Leistungsbeschreibung_Autobahn.pdf ; https://via.bund.de/bim/infrastruktur/landing | Federal roads: masterplan, framework documents, sample AIA |
| https://www.bmv.de/SharedDocs/DE/Pressemitteilungen/2026/024-schnieder-deutschland-wird-bim-land.html ; https://blog.cosinex.de/2026/05/12/bim-bundesfernstrassen-oeffentliche-vergabe/ ; https://www.ibau.de/akademie/wissenswertes/bim-nutzung-verpflichtend/ | News and explainers on German BIM obligation |
| https://infoplattform-personenbahnhoefe.deutschebahn.com/pbhf/DB-BIM ; https://bim.dbinfrago.com/resource/blob/12624362/8fe92b06fe672df3a1e5c3b4a44c1414/DB-InfraGO-Fahrweg-BAP-V-6-0-extern-data.pdf | Deutsche Bahn BIM requirements and BAP |
| https://www.bim.bayern.de ; https://sib.sachsen.de/bim-building-information-modeling-4089.html ; https://www.sib.sachsen.de/download/VVV/A03.07_Vertrag-Anlage_Muster_BAP_Vorlage.pdf ; https://www.xleitstelle.de/xbau | State-level BIM guidance (Bavaria, Saxony) and digital building application standard XBau |
| https://ifcinfra.de/ | IFC-Infra project (alignment, bridge, tunnel, rail, road, ports) from the German ministry programme |
| https://biminstitut.uni-wuppertal.de/en/research/current-research-projects/bundesbau-wissenschaftliche-begleitung/ ; https://www.lobbyregister.bundestag.de/inhalte-der-interessenvertretung/regelungsvorhabensuche/RV0022774/392709 | Academic accompaniment and legislative register entry |
| https://www.buildingsmart.de/normen-und-richtlinien | buildingSMART Germany standards page (fetch returned empty) |
| https://www.bimpedia.de/ | German BIM wiki (connection refused during research); article https://www.bimpedia.de/artikel/16092-oeffnung-durchbruch-schlitz/ on openings |
| https://www.buildingsmart.co.at/ ; https://tuwien.at/cee/ibb/zdb/forschung/abgeschlossene-forschungsprojekte/aia4all-1 ; https://cms.law/en/int/expert-guides/cms-expert-guide-to-building-information-modelling-bim/austria | Austria: chapter, AIA4all research, legal guide |
| https://bauen-digital.ch/ ; `/publikationen/` ; `/themen/` | Switzerland: buildingSMART Switzerland / bauen digital Schweiz |
| https://company.sbb.ch/de/bahnentwicklung/zukunft-bahn/bim.html ; https://bimchange.sbb.ch/ (Glossar digitale Bauwirtschaft PDF under `/content/dam/internet/bimchange/downloads/de/`) | Swiss Federal Railways BIM; Swiss construction glossary |
| https://www.ge.ch/utiliser-bim-building-information-modeling/je-prepare-maquette-bim-autorisation-construire | Geneva: preparing an IFC model for a building permit |
| https://irf.fhnw.ch/entities/publication/ae3d27f4-e33b-4498-b495-efcc6ff48299/full | Swiss academic publication on BIM `[unverified]` |

### 2.4 Netherlands, Belgium, Luxembourg, France, Quebec

| Address | Good for |
|---|---|
| https://www.digigo.nu/ ; https://www.digigo.nu/ilsen-en-richtlijnen/bim-basis-ils/ | digiGO (successor of BIM Loket): Dutch BIM basis ILS (information delivery specification) for IFC; `/handleidingen/` per-software manuals, `/downloads/`, chapters `/3-4-correct-gebruik-entiteiten`, `/3-3-bouwlaagindeling-en-naamgeving`, `/3-2-lokale-positie`, `/3-7-gebruik-propertysets`, `/4-1-ruimten`, `/4-7-materiaal`, `/2-hoe-we-informatie-uitwisselen` `[read]` |
| https://www.bimloket.nl/ictstandaarden/ ; https://www.forumstandaardisatie.nl/open-standaarden/ifc ; https://www.forumstandaardisatie.nl/open-standaarden/lijst/verplicht | Dutch "comply or explain" open-standards list that includes IFC |
| https://www.buildingsmart.nl/ ; https://www.buildingsmart.nl/projecten | buildingSMART Netherlands |
| https://www.rijksvastgoedbedrijf.nl/onderwerpen/b/bouw-informatie-model | Dutch government real estate agency BIM standard (RVB) |
| https://buildingsmart.be/ ; `/downloads-resources/` ; `/brussels-airport-sets-new-standard-with-ifc-first-bim-policy/` | Belgium: chapter and an IFC-first airport policy |
| https://www.crtib.lu/fr/bim-au-luxembourg ; https://www.bimids.eu/lu-fr | Luxembourg BIM and IDS |
| https://www.kroqi.fr/ ; https://kb.kroqi.fr/base-de-connaissance-kroqi | KROQI (CSTB): French collaborative BIM platform with IFC and BCF `[read]` |
| https://www.mediaconstruct.fr/ | French buildingSMART chapter `[blocked]`; buildingsmart.fr is a parked domain |
| https://www.sqi.gouv.qc.ca/feuille-de-route-gouvernementale-pour-le-bim ; https://www.sqi.gouv.qc.ca/expertises/pratiques-integrees-bim-pci | Quebec government BIM roadmap and integrated practices |

### 2.5 Nordic and Baltic countries

| Address | Good for |
|---|---|
| https://www.buildingsmart.no ; https://www.buildingsmart.no/standarder/kort-forklart.html ; `/pofin.html` ; `/standarder/publikasjoner-og-veiledninger.html` ; `/standarder/standardiseringsarbeid.html` ; `/fagnettverk/infradomene.html` | buildingSMART Norway: short explainers of IFC, IDS, BCF, bSDD, POFIN 1.0 (property list), guidance publications `[read]` |
| https://www.mmi-veilederen.no/ | MMI guide 2.0: Norwegian model-maturity index adopted by public clients |
| https://kartlegg.buildingsmart.no/ ; https://www.bimpraten.no/ | Open-BIM maturity self-assessment; BIMpraten podcast |
| https://www.nyeveier.no/for-leverandoerene/ ; https://trv.banenor.no/ ; https://tekniskregelverk.banenor.no/tekniske-spesifikasjoner/ ; https://www.statsbygg.no/bim ; https://simba.statsbygg.no | Norwegian road, rail and state-building clients (BIM content not always visible) |
| https://www.bimalliance.se/ ; https://www.bimalliance.se/tjanster-produkter/buildingsmart-sweden/ ; https://praxi.bimalliance.se/ | Sweden: BIM Alliance / buildingSMART Sweden |
| https://www.buildingsmart.fi/ ; https://wiki.buildingsmart.fi/fi/04_Julkaisut_ja_Standardit/YTV | Finland: buildingSMART Finland and common BIM requirements (YTV) |
| https://www.molio.dk/ ; https://molio.dk/support/vaerktojer/beskrivelsesvaerktojet-2-0/anvisninger/ | Denmark: Molio description tool and guidance (Revit IFC property mapping) |
| https://www.skaitmeninestatyba.lt/ ; https://www.digitaalehitus.ee/ | Lithuania and Estonia digital construction portals |
| https://pub.norden.org/us2023-463/bim-maturity-in-the-nordics-and-estonia.html | Nordic Council study of BIM maturity |

### 2.6 Spain, Portugal, Italy

| Address | Good for |
|---|---|
| https://cibim.transportes.gob.es/ | Spain: Interministerial BIM Commission (formerly cibim.mitma.es); Plan BIM approved 27 June 2023 |
| https://www.hacienda.gob.es/DGPatrimonio/Junta%20Consultiva/informes/informes2023/2023-23-MTMAU-BIM.pdf ; https://www.boe.es/buscar/act.php?id=BOE-A-2017-12902 | Public Procurement Advisory Board report on BIM; Law 9/2017 |
| https://public-buyers-community.ec.europa.eu/system/files/2024-02/Executive%20Summary%20_EN%20A4%20web.pdf ; `.../2024-05/AIDA%20240322_GabSUB_DGGROWPPUnit_PlanBIM_en_v1_0.pdf` | EU summaries of the Spanish BIM plan (English) |
| https://www.buildingsmart.es/ ; `/recursos/manual-de-entrega-de-ifc-edificación/` ; `/recursos/cómo-emplear-bim-en-un-contrato-público/` ; `/bim/openbim/` | buildingSMART Spain: IFC delivery manual (MEI Edificación v2.0), BIM in public contracts |
| https://www.construible.es/2023/05/02/mitma-aprueba-propuesta-plan-implantacion-bim-contratacion-publica ; https://www.esmartcity.es/2023/06/30/plan-bim-incorporara-metodologia-bim-contratos-publicos-construccion ; https://obcp.es/opiniones/la-implementacion-de-la-metodologia-bim-en-la-contratacion-publica | Trade press on the Spanish plan |
| https://buildingsmart.pt/ ; `/guias/` ; `/normas/` ; http://www.ct197.pt/ ; https://www.ipq.pt/ | Portugal: chapter, guides, technical committee CT 197, standards body |
| https://www.buildingsmartitalia.org/ ; https://www.buildingsmartitalia.org/utenti/pubblicazioni/ | buildingSMART Italy |
| https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2023-03-31;36!vig=~art43 ; https://www.bosettiegatti.eu/info/norme/statali/2023_0036_A.htm | Italian procurement code art. 43 (BIM obligation) and Annex I.9 |
| https://biblus.acca.it/linee-guida-bim-2026-per-le-stazioni-appaltanti/ ; https://biblus.acca.it/nuovo-codice-appalti-il-bim-e-obbligatorio/ | ACCA explainers of the 2026 Italian BIM guidelines |

### 2.7 Latin America

| Address | Good for |
|---|---|
| https://planbim.cl/ ; `/ifc-y-actualizaciones/` ; `/guia-bim-pilotos-bid-planbim/` ; `/seminario-redbimgoblatam-avances-chile/` ; `/termino-trabajo-planbim-minvu/` | Chile Planbim (Corfo): national BIM programme, IFC entity sheets (`/documentos/fichas-ifc/`, 404 at fetch), MIDE matrix |
| https://construye2025.cl/wp-content/uploads/2022/07/Estandar-BIM.pdf ; https://construye2025.cl/wp-content/uploads/2025/01/03_GUIA_DE_USUARIO_IFC_ARQ_V2.2.pdf | Chile BIM standard and IFC user guide for architecture |
| https://repositorio.uchile.cl/handle/2250/179170 | Thesis on the Planbim standard |
| https://www.mef.gob.pe/planbimperu/docs/planBIMpE.pdf ; https://www.mef.gob.pe/contenidos/inv_publica/docs/capacitaciones/2026/20260317.pdf | Peru Plan BIM (PDF text not machine-readable) |
| https://www.elperuano.pe/noticia/213920-avance-de-la-implementacion-del-building-information-modeling-en-america-latina | Regional status summary |
| https://bim.minvivienda.gov.co/ ; https://bim.minvivienda.gov.co/sites/default/files/doc-bim-2022-09/10_licencias_.pdf ; https://www.camacol.co/productividad-sectorial/digitalizacion/bim-forum | Colombia: Ministry portal, licences document, Camacol BIM Forum and BIM Kit |
| http://cfia.or.cr/ | Costa Rica engineers' association |
| https://www.buildingsmart.org.br/ | buildingSMART Brazil `[unverified]`; Brazil policy (Estrategia BIM BR, Decreto 10.306/2020, ABNT NBR 15965) named in reports without addresses |

### 2.8 Russia

| Address | Good for |
|---|---|
| http://docs.cntd.ru/document/556793897 | Text of SP 333.1325800.2017 (information modelling rules; IFC 2x3 and higher) |
| https://minstroyrf.gov.ru/press/utverzhdeny-pravila-formirovaniya-i-vedeniya-informatsionnoy-modeli-obekta-kapitalnogo-stroitelstva/ | Ministry of Construction: rules for forming a project's information model |
| https://minstroyrf.gov.ru/press/pervyy-proekt-polnostyu-sproektirovannyy-na-osnove-bim-tekhnologiy-proshel-gosekspertizu/ | First fully BIM-designed project passing state expertise |
| https://spbexp.ru/upload/iblock/0b4/trebovaniya_k_tsim_model_razdela_ios.pdf ; https://www.spbexp.ru/upload/iblock/ba2/trebovaniya_k_tsim_konstruktivnye_i_obemno_planirovochnye_resheniya.pdf | St Petersburg expert body: requirements for the information model (MEP section; structural and planning sections) |
| https://digest.wizardsoft.ru/wp-content/uploads/media/doc/2025/MKE-OD-24-178Chast3.pdf | Mosgosexpertiza requirements document `[snippet]` |
| https://companies.rbc.ru/news/axjEyNHHOq/iz-za-chego-mogut-otkazat-v-soglasovanii-tsim-agr-v-formate-ifc/ | Reasons for refusal of an IFC architectural-urban-planning (AGR) model `[blocked]` |

### 2.9 China, Hong Kong, Taiwan

| Address | Good for |
|---|---|
| https://zjj.sz.gov.cn/attachment/0/678/678888/7768421.pdf | Shenzhen SJG114-2022 SZ-IFC storage standard (IFC-based submission) |
| https://www.gz.gov.cn/xw/tzgg/content/post_6469259.html ; https://zfcj.gz.gov.cn/gkmlpt/content/6/6434/post_6434530.html ; https://zfcj.gz.gov.cn/attachment/7/7943/7943479/10589336.pdf | Guangzhou BIM review notices and CIM white paper |
| https://amr.nanjing.gov.cn/ztzl/bzhzl/tzgg/202302/P020230216538033075572.pdf ; http://ghj.nanjing.gov.cn/njsgtzyj/202103/t20210301_2834720.html | Nanjing BIM review standard DB3201/T 1145-2023 and explainer |
| https://zjw.sh.gov.cn/cmsres/4a/4a7bc95634cd4852b2399e57e9c692dd/a646541bab5ad86dc1684d1126e21e29.pdf | Shanghai BIM smart review modelling manual (EDM files; IFC for structural loads) |
| https://www.bd.gov.hk/tc/resources/online-tools/building-information-modelling/index.html | Hong Kong Buildings Department BIM page (Revit/Archicad plug-ins, openBIM tools) |
| https://www.devb.gov.hk/filemanager/tc/content_2373/BIM-Book-content-cn.pdf ; https://www.careyourbuilding.bd.gov.hk/ors/tc/event/307.html | HK roadmap booklet (cover readable only) and consultation event |
| https://www.bim.cic.hk/zh-hant/resources/publications ; `/publications_detail/117` ; `/events/detail/304` | HK Construction Industry Council: publications (openBIM beginner guide 2025) and an Archicad/Revit IFC workshop |
| https://dbadgp.gov.taipei/DownFiles/Login/使照竣工模型上繳操作手冊.pdf | Taipei as-built model upload manual |
| https://www.bim.ntpc.gov.tw/Filedownload/新北市政府工務局BIM工作參考手冊108年版.pdf | New Taipei BIM reference manual (permit template) |
| https://etheses.lib.ntust.edu.tw/thesis/detail/2e82ca6d84bfe5f839f58b35029a1d54 ; https://tdr.lib.ntu.edu.tw/handle/123456789/90111 | Taiwanese theses on permit rule checking and IFC loss |
| https://www.sunyuanrui.com/works/sz-ifc-research/ | Handbook-style research on SZ-IFC pain points `[read]` |

### 2.10 Japan and Korea

| Address | Good for |
|---|---|
| https://www.mlit.go.jp/jutakukentiku/kenchikuBIMsuishinkaigi.html | MLIT Building BIM Promotion Council; BIM drawing review (from April 2026), data review planned about 2029 |
| https://www.mlit.go.jp/report/press/house05_hh_001157.html ; https://www.mlit.go.jp/jutakukentiku/build/index.html ; https://www.mlit.go.jp/jutakukentiku/build/bim.html | MLIT press release, Housing Bureau pages, BIM acceleration programme |
| https://www.mlit.go.jp/tec/tec_tk_000037.html ; https://www.nilim.go.jp/lab/qbg/bimcim/bimcimindex.html | MLIT BIM/CIM standards (civil) and NILIM portal |
| https://www.building-smart.or.jp/ ; `/ifc/whatsifcverifi/` ; `/ifc/mvd/` ; `/ifcc/software.html` ; `/pc/index.html` ; `/bsisummittokyo2026/` | buildingSMART Japan: IFC certification, MVD, certified software list, professional exam, 2026 summit |
| https://archi.fukuicompu.co.jp/feature/bim-shinsei/ ; https://rebro.jp/ | Vendor pages: BIM permit (Fukui Computer), Rebro MEP software |
| https://www.buildingsmart.or.kr/ ; `/Home/BimOverview` ; `/Home/RnDCenter` ; `/Home/Testinfo` ; `/Home/Certificate` ; `/Home/NewsList` | buildingSMART Korea: overview, R&D, exams, news |
| https://www.buildingsmart.or.kr/Data/Main/BIM%20Guide_MLTL_Korea_2010.pdf ; https://www.buildingsmart.or.kr/Data/Main/시설사업%20BIM%20적용%20기본지침서%20v2.0-S.pdf | Korean ministry BIM guide (2010) and facility BIM guideline v2.0 |
| https://www.kbims.or.kr/ ; `/notice` | Korea Open BIM Research Group |
| https://koreascience.kr/article/JAKO201608450940594.pdf | Korean paper on open-BIM building permits |

### 2.11 United States, Canada and others

| Address | Good for |
|---|---|
| https://www.fhwa.dot.gov/bridge/bim/ ; https://www.fhwa.dot.gov/infrastructure/bim/ ; https://www.fhwa.dot.gov/construction/bim/ ; https://www.fhwa.dot.gov/construction/dabs/ ; https://www.fhwa.dot.gov/construction/3d/ ; https://www.fhwa.dot.gov/bridge/pubs/hif21031.pdf | US Federal Highway Administration: BIM for bridges, digital delivery, Utah demonstration |
| https://pooledfund.org/Details/Study/1798 ; https://www.pooledfund.org/Details/Solicitation/1547 | Pooled fund TPF-5(372/480/523/565) on IFC validation and adoption for bridges |
| https://www.txdot.gov/business/resources/digital-delivery/digital-delivery-documents.html ; https://iowadot.gov/bridge/BIM/ ; https://www.paconstructors.org/news/first-contractual-ifc-model-delivered-nationally/ | State DOT digital delivery and first contractual IFC model (Pennsylvania) |
| https://www.nibs.org/nbims ; https://nibs.org/nbims/v4/faqs/ | NIBS National BIM Standard-US |
| https://origin-www.gsa.gov/system/files/largedocs/BIM_Guide_Series_Facility_Management.pdf | GSA BIM Guide for facility management and COBie |
| https://www.buildingtransformations.org/ | US research programme on building transformations `[snippet]` |
| https://buildingsmartcanada.ca/projects | buildingSMART Canada; openBIM roadmap with NRC (Jan 2024) |
| https://www.cidb.org.za/innovation/cidb-bim-adoption-strategy/ ; https://www.cidb.org.za/contractors/advisory/cidb-standards/ ; https://www.cidb.org.za/resource-centre/downloads-2/ | South Africa cidb BIM adoption strategy 2025-2030 |
| https://hub.dm.gov.ae/link/service ; https://dxmdigitaldocs.github.io/site/docs/dm-bim-submission/frequently-asked-technical-questions | Dubai Municipality: services hub and a community-hosted copy of the DM BIM submission FAQ (openBIM IFC, Revit template) |
| https://www.ashghal.gov.qa/en/Services/GIS%20and%20CAD%20Manuals/ASHGHAL%20BIM%20STANDARD/D0201_File%20Naming%20Convention%20for%20BIM%20%26%20CAD_V1.pdf | Qatar Ashghal BIM file-naming convention |
| https://www.bimafrica.org | Africa BIM community `[snippet]` |

---

## 3. Software vendor documentation

### 3.1 Autodesk (Revit, Civil 3D, Navisworks, Platform Services)

| Address | Good for |
|---|---|
| https://github.com/Autodesk/revit-ifc | The open-source IFC exporter/importer inside Revit: README, wiki, releases, and ~430 issues that are the single biggest source of real Revit-IFC pain in this KB. See [../03_software/revit/ifc_export_reference.md](../03_software/revit/ifc_export_reference.md) |
| https://github.com/Autodesk/revit-ifc/wiki/Revit-IfcExporter-parameter-expression | Parameter-expression syntax for property sets |
| https://github.com/Autodesk/revit-ifc/releases | Release notes (e.g. `IFC_v27.4.0.30`, `IFC_v27.3.0.12`, `IFC_v27.0.1`) |
| https://up1.autodesk.com/2026/RVT/ADSKIFCExporterHelp_26_4_1.htm ; https://up1.autodesk.com/2025/RVT/ADSKIFCExporterHelp_25_2.htm | Official Revit IFC exporter help for specific versions `[read]` |
| https://www.autodesk.com/blogs/aec/wp-content/uploads/sites/36/2022/02/revit-ifc-open-bim-manual-en.pdf | Official Revit IFC / openBIM manual |
| https://help.autodesk.com/view/RVT/2025/ENU/?guid=GUID-E029E3AD-1639-4446-A935-C9796BC34C95 | Revit help: IFC export setup options (older versions under `knowledge.autodesk.com` and `help.autodesk.com/cloudhelp/2024/ENU/...`) |
| https://help.autodesk.com/view/RVT/2025/ENU/?caas=caas%2Fsfdcarticles%2Fsfdcarticles%2FCertain-shared-parameters-not-exportetd-to-IFC-from-Revit.html | Official KB: shared parameters missing from the IFC |
| https://www.autodesk.com/support/technical/article/caas/sfdcarticles/sfdcarticles/Is-IFC2X3-format-supported-on-Revit.html ; `.../Missing-IFC-Options-for-export-from-Revit.html` ; `.../Ducts-not-split-with-the-option-split-walls-columns-ducts-by-level-while-exporting-IFC-from-Revit.html` | Support articles on IFC versions, missing options, split-by-level behaviour |
| https://www.autodesk.com.cn/support/technical/article/caas/sfdcarticles/sfdcarticles/CHS/Missing-elements-or-steel-connections-in-IFC-file-exported-from-Revit.html | Chinese-language KB on missing elements |
| https://help.autodesk.com/cloudhelp/2026/ENU/Revit-API-MainReference/files/html/209a8948-d2c0-0c4e-d3b7-241535ccbad8.htm | Revit API: `IFCExportOptions.ExportBaseQuantities` |
| https://blog.autodesk.io/unique-id-and-ifc-guid/ | The Building Coder: relation between Revit UniqueId and IFC GUID |
| https://help.autodesk.com/view/CIV3D/2025/ENU/ ; https://help.autodesk.com/view/CIV3D/2024/ENU/?guid=GUID-CD22FE6E-0AF9-45EF-B2FB-2B6F3C7DF25F | Civil 3D help; IFC 4.3 export extension |
| https://help.autodesk.com/cloudhelp/ENU/Docs-Files/files/files-naming-standard/Status_Codes.html | Autodesk Docs naming/status codes (ISO 19650 flavour) |
| https://aps.autodesk.com/en/docs/design-automation/v3/developers_guide/overview/ ; https://aps.autodesk.com/blog?tag=MCP | Autodesk Platform Services: cloud automation and MCP posts |
| https://viewer.autodesk.com/ | Free online viewer, often used as a "does it open" yardstick |
| https://forums.autodesk.com/t5/revit-ideas/idb-p/revit-ideas-en ; https://forums.autodesk.com/t5/revit-api-forum/bd-p/160 | Revit Ideas board and Revit API forum (see section 5) |
| https://trello.com/b/ldRXK9Gw/revit-public-roadmap | Revit public roadmap |
| https://github.com/Autodesk/ai-integrations | Official small MCP integrations (Product Help, Fusion) |

### 3.2 Graphisoft (Archicad)

| Address | Good for |
|---|---|
| https://help.graphisoft.com/AC/29/INT/_AC29_Help/121_IFC/121_IFC-1.htm | Archicad 29 "Working with IFC" (also `AC/29/TAI/` Traditional Chinese, `AC/28/SPA/` Spanish) `[read]` |
| https://help.graphisoft.com/AC/29/INT/_AC29_Help/121_IFC/121_IFC-47.htm | Model View Definitions in Archicad `[read]` |
| https://help.graphisoft.com/AC/30/INT/Topics/121_IFC/121_IFC-2.html | Supported IFC file types |
| https://help.graphisoft.com/AC/27/INT/_AC27_Help/121_IFC/121_IFC-50.htm | Predefined property mapping |
| https://helpcenter.graphisoft.com/de/user-guide/93090 | German help centre (IfcSystem mapping) |
| https://graphisoft.com/solutions/open-bim | Graphisoft openBIM positioning page |
| https://community.graphisoft.com/ | Community forum `[blocked]` for automated fetch; threads in Appendix A |
| https://community.graphisoft.com/t5/Data-Exchange-articles/Frequently-Asked-Questions-About-IFC/ta-p/304113 | Graphisoft FAQ about IFC `[blocked]` |
| https://community.graphisoft.com/t5/Product-Roadmap/IFC-4-Import-Certification/idi-p/632958 | Roadmap item: IFC4 import certification |

### 3.3 Trimble (Tekla Structures, Trimble Connect, Trimble Access)

| Address | Good for |
|---|---|
| https://support.tekla.com/doc/tekla-structures/2024/int_ifc_export ; `.../2025/int_ifc_export` ; `.../2026/int_exporting_into_ifc` | Tekla Structures IFC export manual by year |
| https://support.tekla.com/doc/tekla-structures/2024/int_checking_exported_ifc_model ; `.../int_defining_property_sets_using_property_set_definitions` ; `.../2025/int_ifc_general_info` ; `.../2025/int_ifc_interoperability_concepts` ; `.../2025/int_conversion_management` | Checking an export, property sets, geometry concepts, importing IFC objects as Tekla objects |
| https://support.tekla.com/doc/tekla-structures/2026/rel_int_enhanced_ifc_interoperability ; https://support.tekla.com/article/supported-ifc-schemas ; https://support.tekla.com/cs/doc/tekla-structures/2021/int_ifc_base_quantities | Release note, supported schemas, base quantities |
| https://support.tekla.com/corenet-x-ifc-sg | Tekla guidance for Singapore |
| https://forum.tekla.com/forum/253-usage-interoperability/ | Tekla user forum, interoperability section `[blocked]` (listings return 403) |
| https://developer.trimble.com/docs/connect/ | Trimble Connect developer docs (CDE) |
| https://help.fieldsystems.trimble.com/trimble-access/2021.20/es/Map-files-BIM-and-IFC.htm | Trimble Access (field software) IFC maps, Spanish |
| https://www.tek1.com.au/steel-detailing/difference-between-tekla-export-ifc-and-ifc4 | Steel-detailer blog: "IFC export" vs "IFC4 export" in Tekla |

### 3.4 Bentley, Nemetschek, Vectorworks, others (authoring)

| Address | Good for |
|---|---|
| https://docs.bentley.com/LiveContent/web/OpenRoads%20Designer-v2024.0.2/Help/en/topics/1296840/GUID-DB8BCC88-1756-4110-B5AC-C0E3758DD413.html | OpenRoads Designer: export to IFC |
| https://docs.bentley.com/LiveContent/web/OpenBuildings | OpenBuildings Designer: populating COBie |
| https://www.bentley.com/en/infrastructure-ai/mcp-servers/ ; https://www.bentley.com/en/infrastructure-ai/ ; https://www.bentley.com/software/itwin-platform/ | Bentley's MCP servers and iTwin platform |
| https://communities.bentley.com/products/building/building_analysis___design/f/aecosim-speedikon-forum/228189/ifc4-3-version-available-in-aecosim-update-4 | Community note on IFC 4.3 in AECOsim Update 4 (Bentley community moved to ServiceNow; JavaScript-only) |
| https://connect.allplan.com ; https://forum.vectorworks.net | Allplan and Vectorworks forums `[blocked]` (HTTP 403) |
| https://www.bricsys.com/news/bricscad-is-officially-ifc4-certified | BricsCAD IFC4 certification news |
| https://docs.sofistik.com/2025/en/fea/basic/interfaces/ifc_export.html | SOFiSTiK structural analysis IFC export |
| https://info.cype.com/en/subject/plugin-open-bim-revit-generating-native-revit-elements-from-an-ifc-file-of-piping-systems/ | CYPE open-BIM plugin for Revit |
| https://www.cadforum.cz/cz/rozsireny-ifc-import-export-pro-revit-2026-tip14516 | Arkance/CADforum: extended IFC import/export for Revit 2026 (Czech) |
| https://emea.support.arkance.world/hc/es/articles/36464850969234-Using-IFC-files-with-a-Shared-Coordinates-system | Arkance support: IFC with shared coordinates (Spanish) `[blocked]` |
| https://rengabim.com ; https://manual.rengabim.com/ehksport_atributov_obektov.html ; https://rengabim.com/stati/bol-she-10-formatov-eksporta-importa-v-renga-kakoj-iz-nih-vybrat/ ; https://blog.rengabim.com/2021/08/ifc.html | Renga (Russian BIM): attribute export, format choice, how to accept IFC |
| https://sapr.ru/article/25825 ; https://dwg.ru/cat/news/4048 | nanoCAD SPDS and IFC from Revit; nanoCAD IFC import news |
| https://www.glodon.com ; https://www.bimface.com/ | Glodon / BIMFACE (China), mentioned for BIM5D and lightweight viewing |

### 3.5 Viewers, checkers, CDE and conversion tools

| Address | Good for |
|---|---|
| https://www.solibri.com/ ; https://www.solibri.com/solibri-anywhere | Solibri Model Checker: the reference rule-based checker `[read]` |
| https://bimcollab.com/en/products/bimcollab-zoom ; https://helpcenter.bimcollab.com | BIMcollab ZOOM viewer and BCF issue management; help articles on Solibri BCF connector, status sync, viewpoint components |
| https://bimvision.eu/en/ | BIM Vision, free IFC viewer by Datacomp (content in German) |
| https://www.simplebim.com/ | Simplebim IFC data editing |
| https://www.drofus.com/en ; https://support.drofus.com/en/support/solutions/articles/16000118323-optimal-settings-for-ifc-export-from-revit | dRofus data management; recommended Revit IFC export settings |
| https://catenda.com/ ; https://www.dalux.com/ ; https://revizto.com/en/ | CDE and coordination platforms (Catenda Hub, Dalux, Revizto) |
| https://speckle.systems/pricing/ ; https://docs.speckle.systems | Speckle (data platform; connectors for Revit, Rhino, etc.) |
| https://xeokit.io/ | xeokit web viewer SDK |
| https://cadexchanger.com/products/sdk/ | CAD Exchanger SDK (commercial conversion) |
| https://www.iai.kit.edu/english/1302.php | KIT IFC Model Viewer (free, academic) |
| https://docs.intellicad.org/files/oda/2023_10/oda_ifc_docs/ifc_overview_file_formats.html | ODA IFC SDK (powers "Open IFC Viewer") |
| https://biblus.acca.it/usbim-checker-verifica-informativa-del-modello/ ; https://biblus.acca.it/markups-bcf-workflow-openbim/ | ACCA usBIM checker and BCF workflow |
| https://app.bimsupporters.com/courses/ifc/lessons/history-and-versions-of-ifc/ | Course lesson on IFC history |
| https://geometrygym.com | Geometry Gym: Rhino/Grasshopper IFC, diff/merge `[unverified]` |
| https://www.acca.it | ACCA cloud IFC refactoring tool mentioned in a forum |

---

## 4. Open-source projects

### 4.1 Core libraries and toolkits

| Address | Good for |
|---|---|
| https://github.com/IfcOpenShell/IfcOpenShell | THE open-source IFC toolkit (C++ and Python): read/write/validate, IfcConvert, IfcPatch, IfcClash, IfcTester (IDS), Bonsai add-on for Blender, `ifcmcp`. ~400 issues cited in the KB. See [../04_open_source/libraries_and_toolkits.md](../04_open_source/libraries_and_toolkits.md) |
| https://docs.ifcopenshell.org ; https://docs.ifcopenshell.org/ifctester.html ; https://docs.ifcopenshell.org/bcf.html ; https://docs.ifcopenshell.org/ifcconvert/usage.html ; https://docs.ifcopenshell.org/introduction/introduction_to_ifc.html ; https://docs.ifcopenshell.org/ifcopenshell-python/hello_world.html | API docs, IDS testing, BCF, converter, beginner introduction |
| https://ifcopenshell.org/ ; https://pypi.org/project/ifcopenshell ; https://pypi.org/project/ifctester | Project site and Python packages |
| https://github.com/IfcOpenShell/IfcOpenShell/discussions ; https://github.com/IfcOpenShell/files | Discussions (including announcements) and the project's own test files |
| https://bonsaibim.org/ ; https://bonsaibim.org/community.html ; https://docs.bonsaibim.org/ ; https://docs.bonsaibim.org/studio/guides/authoring/starting_new_project.html | Bonsai (formerly BlenderBIM): IFC-native BIM authoring in Blender |
| https://github.com/ThatOpen ; https://github.com/ThatOpen/engine_web-ifc ; https://github.com/ThatOpen/engine_components ; https://github.com/ThatOpen/engine_fragment ; https://github.com/ThatOpen/platform_services | That Open Company (ex IFC.js): web-ifc parser (WASM), components, fragments, services; ~140 issues cited |
| https://docs.thatopen.com/intro ; https://docs.thatopen.com/Tutorials/Components/Core/IfcLoader | Official docs and IfcLoader tutorial |
| https://people.thatopen.com | That Open community ("Ask the community") `[blocked]` (login required) |
| https://github.com/IFCjs/web-ifc-three ; https://github.com/IFCjs/web-ifc-viewer | Legacy viewers, superseded by components since Sept 2023 |
| https://github.com/xBimTeam ; https://github.com/xBimTeam/XbimEssentials ; https://github.com/xBimTeam/XbimGeometry ; https://github.com/xBimTeam/XbimWebUI ; https://github.com/xBimTeam/XbimWindowsUI ; https://github.com/xBimTeam/Xbim.IDS.Validator ; https://docs.xbim.net | xBIM toolkit (.NET): reader/writer, geometry, web UI, COBie, IDS validator |
| https://github.com/ifcquery/ifcplusplus | IFC++ (C++ reader/writer) |
| https://github.com/opensourceBIM/BIMserver ; https://github.com/opensourceBIM/COBie-plugins | BIMserver (Java model server, older) and COBie plugins |
| https://github.com/GeometryGym/GeometryGymIFC | Geometry Gym IFC library (.NET; Rhino/Grasshopper) |
| https://github.com/specklesystems ; https://github.com/specklesystems/speckle-server ; https://github.com/specklesystems/speckle-sharp ; https://github.com/specklesystems/speckle-sharp-connectors | Speckle data platform and connectors |
| https://github.com/xeokit/xeokit-sdk ; https://github.com/xeokit/xeokit-convert | xeokit viewer and converter (licence claims conflict between sources) |
| https://github.com/FreeCAD/FreeCAD | FreeCAD BIM workbench (IFC import/export; see `src/Mod/BIM/importers/exportIFC.py`) |
| https://github.com/paireks/dotbim | dotbim: minimal JSON mesh format with IFC converters |
| https://github.com/blox-eng/goifc ; https://github.com/openbimrs/ifc ; https://github.com/LTplus-AG/ifc-lite ; https://github.com/louistrue/ifc-lite | Go, Rust and browser/Rust-WASM IFC readers (ifc-lite also has clash and BCF) |
| https://github.com/hypar-io/Elements | Hypar Elements (.NET building elements library with IFC) |
| https://github.com/tomvandig/bimledger | Experimental ledger for BIM data |
| https://github.com/Gaia3D/mago-3d-tiler ; https://github.com/geosolutions-it/digital-twin-toolbox ; https://github.com/KIT-IAI/SDM_KITModelViewer ; https://github.com/dd-bim/City2BIM | GIS and digital-twin tools: 3D Tiles tiler, toolbox, KIT viewer, CityGML-to-BIM |
| https://github.com/BenzclyZhang/BimSPARQL ; https://github.com/buildingsmart-community/ifcOWL ; https://github.com/Nobuho/IFC-Neo4j-converter ; https://github.com/IFCManager/IFC_Graph_Database | Linked-data and graph-database approaches to IFC |
| https://github.com/chuongmep/Ifc-to-excel ; https://github.com/datadrivenconstruction/cad2data-Revit-IFC-DWG ; https://github.com/Arri-1/ifc-quantity-takeoff ; https://github.com/youshengCode/IfcToolbox | IFC-to-Excel exporters, converters and quantity take-off scripts |
| https://github.com/pyrevitlabs/pyRevit | pyRevit (Revit scripting; version 7 has a built-in MCP) |
| https://github.com/BIM-Tools/SketchUp-IFC-Manager ; https://github.com/BHoM/ETABS_Toolkit ; https://github.com/LetsConstructIT/Grasshopper-TeklaDrawingLink | SketchUp IFC manager, BHoM ETABS toolkit, Grasshopper-Tekla link |
| https://github.com/buildingsmart-community ; https://github.com/buildingsmart-community/bSDD-Revit-plugin ; https://github.com/bSI-InfraRoom ; https://github.com/bSI-RailwayRoom/IFC-Rail-Sample-Files | buildingSMART community org, bSDD plugin for Revit, infrastructure room, IFC-Rail sample files |
| https://github.com/osama-ata/Awesome-AECO ; https://github.com/topics/openbim ; https://github.com/topics/awesome-bim | Curated lists of open-source AEC projects |
| https://github.com/bimdata | BIMData (open-source platform components) |

### 4.2 Community hubs of the open-source world

| Address | Good for |
|---|---|
| https://osarch.org/ ; https://osarch.org/events/ ; https://osarch.org/chat/ | OSArch news, event calendar, Matrix/IRC chat |
| https://wiki.osarch.org/ | OSArch wiki: `Revit_setup_for_OpenBIM`, Revit IFC geolocation, spatial hierarchy, IFC materials, IFC sequence concepts |
| https://community.osarch.org/ | OSArch forum (Discourse); tag pages for IDS (`/discussions/tagged/ids`), education, `ifc-geometry` |
| https://thinkmoult.com/ifc-coordinate-reference-systems-and-revit.html | IfcOpenShell maintainer's blog post on CRS and Revit |

### 4.3 MCP servers and AI tools (the test targets themselves)

See [../04_open_source/mcp_servers_and_ai_tools.md](../04_open_source/mcp_servers_and_ai_tools.md) for tool lists. Repositories and issue trackers are also a source of real user prompts (see Appendix B).

| Address | Good for |
|---|---|
| https://github.com/mcp-servers-for-revit/mcp-servers-for-revit ; https://github.com/mcp-servers-for-revit/revit-mcp ; https://github.com/mcp-servers-for-revit/revit-mcp-plugin ; https://github.com/revit-mcp/revit-mcp | Main Revit MCP family (the older `revit-mcp` was archived in favour of the mono-repo); issues show real chat prompts |
| https://github.com/bimwright/rvt-mcp ; https://github.com/Sam-AEC/aec-model-bridge ; https://github.com/LuDattilo/revit-mcp-server ; https://github.com/LuDattilo/RevitCortex ; https://github.com/HorizunGroup/horizun-revit-mcp ; https://github.com/Demolinator/revit-mcp-server ; https://github.com/oakplank/RevitMCP ; https://github.com/okuno-dsi/revit-mcp-toolkit ; https://github.com/andyluu98/vn-revit-mcp ; https://github.com/ZedMoster/revit-mcp | Other Revit MCP servers (Japan, Vietnam, China among them) |
| https://github.com/shuotao/REVIT_MCP_study | Taiwan-based Revit MCP with Traditional-Chinese issues and 200+ tools |
| https://github.com/JefaturaBIM94/RevitMCPBOQ | Spanish-language Revit take-off (BOQ) MCP |
| https://github.com/samsonleegh/revit-coach ; https://github.com/Davud77/bp-revit-tools ; https://github.com/roosslan/ifc_exporter_revit_addin ; https://github.com/i-savelev/BatchIfcExporter | LLM Revit coach with Singapore context; Russian-speaking developer tools and batch IFC export add-ins |
| https://github.com/smartaec/ifcMCP ; https://github.com/JotaDeRodriguez/Bonsai_mcp ; https://github.com/Show2Instruct/ifc-bonsai-mcp ; https://github.com/Show2Instruct/bonsai-mcp | IFC / Bonsai MCP servers |
| https://github.com/flinker-app/ifc-mcp ; https://github.com/Daviidro/ifcopenshell-mcp ; https://github.com/zeussilver/bim-ifc-mcp ; https://github.com/louistrue/ifcx-mcp ; https://github.com/ekkodale/IFC-MCP ; https://github.com/vinnividivicci/ifc-ids-mcp ; https://github.com/j03rul4nd/ifc-viewer-online | More IFC MCP servers: prompt lists, deterministic checks, IFCX, business case, IDS authoring, viewer with validation |
| https://github.com/SzamosiMate/tapir-archicad-MCP ; https://github.com/joacos/archicad-mcp ; https://github.com/streletskiy/archi-helper | Archicad MCP servers (Spanish prompts; Russian-language chat app) |
| https://github.com/teknovizier/tekla_mcp_server ; https://github.com/tempalg1n/tekla-mcp-server | Tekla Structures MCP servers |
| https://github.com/BerkantACUN/ifc-ruhsat | Turkish building-permit check for IFC 4.3 |
| https://github.com/autodesk-platform-services/aps-aecdm-mcp-dotnet ; https://github.com/autodesk-platform-services/aps-mcp-app-example ; https://github.com/autodesk-platform-services/aps-mcp-server-nodejs ; https://github.com/autodesk-platform-services/aps-sample-revit-mcp-tools-bundle | Autodesk APS sample MCP servers (ACC, AEC Data Model, viewer UI, Revit tools) |
| https://github.com/Menezeris/AIMviewer | AI-driven viewer with camera-control prompts (issues in Slovak) |
| https://github.com/matsuokakoki/ifc-bim-llm-finetuning | Japanese experiment on fine-tuning LLMs for IFC and its error types |
| https://registry.modelcontextprotocol.io/v0/servers?search=ifc (also `search=revit`, `bim`, `archicad`, `autodesk`, `blender`) ; https://modelcontextprotocol.io/docs/getting-started/intro | Official MCP registry search API and protocol introduction |
| https://forum.dynamobim.com/t/ifcnodes-ai-powered-ifc-toolkit-for-dynamo/113569 ; https://community.osarch.org/discussion/3396/ai-chat-ifcopenshell-org-is-live | LLM-plus-IFC tools announced in community forums (IFCNodes for Dynamo; AI chat on ifcopenshell.org) |

### 4.4 Singapore community tools (unofficial helpers for IFC+SG submissions)

| Address | Good for |
|---|---|
| https://github.com/noddlesskcho/IFC-Repair-Studio ; https://github.com/noddlesskcho/IFCSG-Parameter-Consolidator ; https://github.com/noddlesskcho/ifc-sg-site-object-repair | Repair tools for IFC-SG validation errors (`IFC0000101/104`), duplicate shared parameters, site objects and stair flights |
| https://github.com/LUOaini1213/ifcsg-precheck ; https://github.com/chunyen93/ifcgref-corenetx ; https://github.com/OrvenBentleySystems/sg-ifc-microstation-eap | Pre-submission checker, georeference check, MicroStation checker |

### 4.5 Validators, rule sets and local-standard repositories

| Address | Good for |
|---|---|
| https://github.com/OpenAEC-Foundation/OpenAEC-BIM-validator ; https://github.com/OpenAEC-Foundation/open-bim-platform | Dutch open-source IDS-based validator and platform (issues in English and Dutch) |
| https://github.com/pragmaticBIM/pragmaticBIM-reference | Reference rule sets for model checking |
| https://github.com/nl-digigo/NLCS ; https://github.com/nl-digigo/imwo ; https://github.com/nl-digigo/GeoBIM_Georefereren ; https://github.com/Aedes-datastandaarden/ILS-woco ; https://github.com/Stichting-CROW/imbor ; https://github.com/Geonovum/GeoBIM_Georefereren | Dutch standards published on GitHub (NLCS, IMBOR, georeferencing guideline, housing-association ILS) |
| https://github.com/SheetPros/OpenPermit ; https://github.com/jmarinderko/calculadora-RIC ; https://github.com/ingelibre/ingetrazo ; https://github.com/aware-aeco/aware ; https://github.com/jwouellette/TPF-5_372-Unit_Test_Suite | Small national or niche projects: permit tool, Chilean RIC calculator, Chilean road tool, AWARE, US bridge IFC unit tests |
| https://github.com/IndustryFoundationClasses/Questions | A community question repository |

### 4.6 Sample IFC files (for creating test requests that need a model)

| Address | Good for |
|---|---|
| https://github.com/buildingsmart-community/Community-Sample-Test-Files | Community sample files for IFC 2x3, 4, 4.3 (Duplex Apartment, Schependomlaan, Molio, Chesapeake Bay Bridge-Tunnel, NURBS and more) |
| https://github.com/buildingSMART/Certification-datasets | Official certification datasets |
| https://github.com/buildingSMART/IFC4.3.x-sample-models | IFC 4.3 sample models |
| https://www.ifcwiki.org/index.php?title=KIT_IFC_Examples ; https://www.iai.kit.edu/english/1302.php | KIT example models |
| https://github.com/xBimTeam/XbimEssentials/tree/master/Tests/TestFiles | xBIM test files (also `IFC4x3_ADD2`) |
| https://github.com/ThatOpen/engine_web-ifc/tree/main/tests/ifcfiles/public | web-ifc public test files |
| http://openifcmodel.cs.auckland.ac.nz/ | Open IFC Model Repository (University of Auckland) |
| https://github.com/IfcOpenShell/IfcOpenShell/tree/v0.8.0/test | IfcOpenShell tests |

---

## 5. Forums and Q&A sites by language

Site-level entries; see [communities_directory.md](communities_directory.md) for activity and automated-access notes, and Appendix A for threads.

### 5.1 English

| Address | Good for |
|---|---|
| https://forums.buildingsmart.org/ | Expert forum run by buildingSMART: schema interpretation, IDS, MVD, georeferencing, infrastructure. 235 real records in the KB, 2018-2026. Discourse: category pages and `search.json` can be fetched, but the search endpoint rate-limits (HTTP 429) |
| https://forums.buildingsmart.org/tag/revit ; https://forums.buildingsmart.org/c/users/6 | Revit-tagged threads; "Users" category |
| https://community.osarch.org/ | OSArch forum: Bonsai/IfcOpenShell, IDS, clash, QTO; 183 real records, 2020-2026. Includes a Spanish category |
| https://github.com/Autodesk/revit-ifc/issues | Revit IFC exporter/importer tracker; 433 real records, 2018-2026; Autodesk staff quote internal `REVIT-nnnnnn` ticket numbers |
| https://github.com/IfcOpenShell/IfcOpenShell/issues | IfcOpenShell tracker; 397 real records, 2016-2026; one of the few places with real LLM/MCP complaints (issues 7945, 8951) |
| https://forums.autodesk.com/ (Revit, Revit API, Revit Ideas, Civil 3D) | Autodesk Community; 80 records, mostly snippet-level because pages return 403 to fetchers |
| https://forum.dynamobim.com/ | Dynamo forum: Revit automation, IFC export via script, AI/MCP opinions; 69 records |
| https://discourse.pyrevitlabs.io/ | pyRevit forum: IFC export scripting, built-in MCP; 18 records |
| https://community.graphisoft.com/ | Archicad IFC exchange threads; 10 records (mostly snippet) |
| https://community.cesium.com/ | Cesium forum: IFC/BIM to 3D Tiles and georeferencing; 13 records |
| https://forum.tekla.com/ | Tekla user forum `[blocked]` |
| https://www.reddit.com/ ; https://stackoverflow.com/ ; https://gis.stackexchange.com/ | Reddit and Stack Exchange could not be reached (see section 8) |
| https://augi.com/articles/detail/ifc-for-the-win ; https://forums.augi.com/archive/index.php/t-165346.html ; https://www.cadtutor.net/forum/topic/65270-ifc-open-vs-linking | AUGI article and forum archive, CADTutor forum thread |
| https://community.pix4d.com/t/export-ifc-from-revit-geolocation/29413 | Pix4D community: IFC geolocation from Revit |

### 5.2 Russian

| Address | Good for |
|---|---|
| https://forum.dwg.ru/ (Revit sub-forum: https://forum.dwg.ru/forumdisplay.php?f=58) | Biggest Russian CAD/BIM forum: IFC import/export between Revit, Tekla, ArchiCAD, Sapfir, SCAD, 2009-2026; 43 records. Pages are served in cp1251 and appear garbled without re-encoding; search is unreliable |
| https://habr.com/ (articles) | Developer essays on IDS, AGR checks, IFC post-processing (32 records). Article pages read well; search is JavaScript-rendered; comment text is not returned |
| https://t.me/s/ifc_ru ; https://t.me/s/revithelper_kmv ; https://t.me/s/bimlib_pro ; https://t.me/s/prostobim ; https://t.me/s/bimacad | Telegram channels "Всё про IFC", RevitHelper, BIMLIB, "Просто о BIM", "Академия BIM"; the public web preview (`t.me/s/`) works for some channels |
| https://sapr.ru/ ; https://dwg.ru/ | Trade portals and articles |
| https://rengabim.com/ ; https://blog.rengabim.com/ | Renga vendor knowledge and blog |
| https://www.youtube.com/watch?v=VPlQf3fv908 | Lecture: IFC export and IFC viewers (Russian) |

### 5.3 Chinese

| Address | Good for |
|---|---|
| https://zhuanlan.zhihu.com/ ; https://www.zhihu.com/ | Zhihu articles and Q&A: IFC basics, SZ-IFC, lightweight viewers; 55 records but `[blocked]` (403), so mostly snippet-level |
| https://blog.csdn.net/ ; https://ask.csdn.net/ | CSDN developer blogs and Q&A: xBIM, web-ifc, glTF pipelines; 35 records; often HTTP 521 or captcha |
| https://www.cnblogs.com/ | Developer blog platform: IFC document series, xBIM series; 18 records |
| https://juejin.cn/ ; https://segmentfault.com/ ; https://www.jianshu.com/ | Developer and general blog platforms |
| https://zhidao.baidu.com/ | Baidu Q&A; user-style Revit/IFC questions |
| https://bbs.zhulong.com/ ; https://www.zhulong.com/ ; https://bbs.co188.com/ | Construction-industry forums (Zhulong, co188) |
| https://gitee.com/explore/topic/BIM | Chinese open-source host; BIM lightweight engines |
| https://www.bilibili.com/ | Video site with Revit/BlenderBIM tutorials (captcha on read pages) |
| https://www.ptt.cc/ | Taiwan forum `[blocked]` |

### 5.4 Japanese, Korean

| Address | Good for |
|---|---|
| https://qiita.com/tags/ifc ; https://qiita.com/search?q=IFC+Revit | Qiita developer articles (IfcOpenShell, Revit API, web-ifc); 22 records; list pages are JavaScript-rendered |
| https://zenn.dev/ | Zenn articles and "scraps" (IDS, IfcOpenShell, Revit-MCP); 18 records; topic API works |
| https://note.com/ | note articles on BIM drawing review, Bonsai in practice; 14 records |
| https://www.buildingsmart.or.kr/ ; https://www.kbims.or.kr/ | Korean chapter and research group (official documents only; community forums such as Naver cafes were not reached) |

### 5.5 German, Dutch, Nordic, Romance languages

| Address | Good for |
|---|---|
| https://bim-me-up.com/ | German-language vendor/educator blog (also English): Revit IFC export tips; 15 records |
| https://www.bimpedia.de/ ; https://www.bimpedia.eu/ | German BIM wiki/articles `[blocked]` (connection refused) |
| https://forum.cad.de/ ; https://forum.allplan.com/ | German CAD forums (DNS failures) `[unverified]` |
| https://www.digigo.nu/ | Dutch: official ILS documentation (no open forum reached) |
| https://www.buildingsmart.no/ ; https://www.bimpraten.no/ | Norwegian chapter and podcast |
| https://biblus.acca.it/ ; https://www.ingenio-web.it/ | Italian trade portals (24 and 4 records) |
| https://www.espaciobim.com/ ; https://www.e-zigurat.com/ ; https://www.bimnd.es/ ; https://www.construible.es/ | Spanish BIM portals and educators |
| https://www.bimandco.com/ ; https://faq.bimandco.com/en/ | French object platform with Revit plug-in (no IFC content found) |

---

## 6. Blogs, educators and enthusiasts

| Address | Good for |
|---|---|
| https://bimcorner.com/ | Polish educator blog in English: "10 common IFC export mistakes", IFC 4.3, validation, AI with IFC (19 records, 2020-2026). Examples: `/10-common-ifc-export-mistakes-to-avoid-part-1/`, `/what-i-dont-like-about-ifc/`, `/super-ifc/`, `/use-ai-to-manipulate-your-ifc/`, `/ai-ifc-properties/` |
| https://bim-me-up.com/ | German/Austrian BIM educator: `/revit-ifc-und-koordinatensysteme/`, `/ifcbuildingstorey/`, `/ifc-5-eine-neue-hoffnung-fuer-interoperabilitaet/`, `/die-popularsten-ifc-viewer/` |
| https://www.nordicbim.com/en/insights/what-is-the-buildingsmart-ids-standard ; https://www.nordicbim.com/knowledge/en/ifc-4.3 | Vendor/educator explainers on IDS and IFC 4.3 |
| https://thinkmoult.com/ | Dion Moult (IfcOpenShell maintainer) blog |
| https://teocomi.com/bim-collaboration-format/ | BCF overview by a Speckle/BIM developer |
| https://archgyan.com/how-to-run-bim-coordination-meetings/ ; https://archgyan.com/bim-naming-conventions-file-standards/ | Coordination-meeting and naming blogs |
| https://bimfix.blogspot.com/ | Community blog on ISO suitability codes |
| https://novedge.com/blogs/design-news/revit-tip-revit-ifc-export-configuration-and-quality-control | Revit IFC export QC tips |
| https://ifc-navigator.pages.dev/blog/ifc2x3-vs-ifc4-vs-ifc4x3-differences/ ; https://infralens.in/handbook/bim-file-formats | Blog/handbook comparisons of IFC versions and BIM formats (secondary) |
| https://aecmag.com/collaboration/ifc-for-infrastructure/ ; https://architosh.com/2019/06/aia-archicad-users-among-first-to-benefit-from-ifc4-reference-view-export-certification ; https://constructionmanagement.co.uk/digital-construction/ifc-4-3-for-infrastructure-approved-as-final-standard/ | Trade press on IFC 4.3 and certification |
| https://specificationonline.co.uk/articles/2025-12-16/the-nbs/bim-comes-of-age-in-construction-as-most-professionals-now-consider-it-a-collaborative-p ; https://pbctoday.co.uk/news/?p=89330 | UK trade press (NBS reports; BIM framework updates) |
| https://www.ingenio-web.it/articoli/ifc-per-le-infrastrutture-solo-una-questione-di-volonta/ | Italian trade article on IFC for infrastructure |
| https://zenn.dev/miyamiyaumya/ ; https://qiita.com/Takashi_Kasuya ; https://qiita.com/kiyuka | Japanese individual authors (IDS, IfcOpenShell, Revit API, FILE_SCHEMA); kiyuka also writes on zenn.dev |
| https://note.com/onestruction/ | ONESTRUCTION (openBIM and bSDD consultancy, Japan) |
| https://www.cnblogs.com/herd/ ; https://www.cnblogs.com/SavionZhang/ | Chinese enthusiast series on IFC documents and xBIM |
| https://github.com/i-savelev | Russian BIM developer (BatchIfcExporter, ifc_checker); articles on Habr |
| https://medium.com/ (tag pages) ; https://www.linkedin.com/ | Medium and LinkedIn were not reachable (403 / unrelated content) |
| https://www.wikipedia.org (IFC, BIM, buildingSMART in en/ru/zh/ja/es/fr/it/pt/de) | General encyclopedia pages for terms in many languages; secondary only. Examples: https://en.wikipedia.org/wiki/Industry_Foundation_Classes, https://ru.wikipedia.org/wiki/Industry_Foundation_Classes, https://ja.wikipedia.org/wiki/Industry_Foundation_Classes, https://es.wikipedia.org/wiki/Industry_Foundation_Classes, https://fr.wikipedia.org/wiki/Industry_Foundation_Classes, https://it.wikipedia.org/wiki/Building_Information_Modeling, https://pt.wikipedia.org/wiki/BIM |

---

## 7. Research papers and datasets

For detailed summaries see [../04_open_source/llm_bim_research_and_datasets.md](../04_open_source/llm_bim_research_and_datasets.md). The first group is directly about LLM assistants working with BIM, so these papers also describe the kinds of requests the test targets are expected to handle.

| Address | Good for |
|---|---|
| https://arxiv.org/abs/2408.08054 (HTML: https://arxiv.org/html/2408.08054v2) | Text2BIM: natural-language prompts to BIM authoring commands |
| https://arxiv.org/abs/2304.09333 | BIM-GPT: prompt-based BIM information retrieval |
| https://arxiv.org/abs/2605.01698 (HTML: https://arxiv.org/html/2605.01698v1) | ifc-bench v2: adaptive exploration of IFC by an agent |
| https://huggingface.co/datasets/sylvainHellin/ifc-bench ; https://github.com/sylvainHellin/cobbie | IFC-Bench dataset (CC BY 4.0) and the Cobbie multi-agent code |
| https://arxiv.org/abs/2607.26072 | IFCMemoryBench |
| https://arxiv.org/abs/2508.05676 | Fine-tuning vs prompting for BIM retrieval |
| https://arxiv.org/abs/2303.15116 | Ontology-aided multi-constraint BIM querying |
| https://arxiv.org/abs/2411.09951 | Natural-language approach for cloud BIM |
| https://arxiv.org/abs/2409.18345 | Speech-to-BIM (NADIA-S) |
| https://arxiv.org/abs/2406.16903 | Copilot inside a BIM authoring tool |
| https://arxiv.org/abs/2511.05533 | MCP4IFC: MCP for IFC with Bonsai |
| https://arxiv.org/abs/2601.00809 | Modular reference architecture for MCP servers |
| http://export.arxiv.org/api/query?search_query=all:%22model+context+protocol%22+AND+all:BIM&max_results=10 | arXiv API query used to discover MCP-and-BIM papers |
| https://api.semanticscholar.org/graph/v1/paper/DOI:10.1016/j.autcon.2023.105067 ; `.../DOI:10.3390/buildings14082499` ; `.../DOI:10.5194/isprs-annals-xi-4-2026-323-2026` ; `.../DOI:10.1016/j.aei.2024.102532` ; `.../DOI:10.1016/j.autcon.2015.12.003` | Semantic Scholar records: BIM-GPT, DAVE (GPT assistant for Revit), Query2Property, NADIA, ifcOWL |
| https://w3c-lbd-cg.github.io/bot/ | W3C Building Topology Ontology (linked building data) |
| https://itcon.org/paper/2026/16 ; https://www.itcon.org/papers/2024_58-ITcon-SI-Cassandro.pdf ; https://re.public.polimi.it/retrieve/84b2e3ca-76b9-4b30-8a57-6e1c204a373b/EC32024_255.pdf | ITcon 2026 glTF/USD vs IFC; cost-estimation papers |
| https://salford-repository.worktribe.com/output/1443918/application-and-extension-of-the-ifc-standard-in-construction-cost-estimating-for-tendering-in-china | IFC extension for Chinese cost estimating |
| https://search.napstic.cn/literature/periodical/010tmjzgcxxjs202401009 ; https://search.napstic.cn/literature/periodical/010tmjzgcxxjs202404016 | Chinese journal papers (BIMBase PModel; SZ-IFC quality control) |
| https://www.fig.net/resources/proceedings/2018/05_bim/FIG2018_BIM_and_Surveying_03_02_IFC_Clemen.pdf ; https://isprs-archives.copernicus.org/articles/XLVIII-4-W11-2024/41/2024/isprs-archives-XLVIII-4-W11-2024-41-2024.pdf ; https://programm.dvw.de/intergeo-agenda-en/ergebnisse-des-buildingsmart-bim-fit-check-zur-georeferenzierung-und-trassierung | Georeferencing papers and the buildingSMART BIM fit check (PDFs unreadable) |
| https://repositorio.uchile.cl/handle/2250/179170 ; https://etheses.lib.ntust.edu.tw/thesis/detail/2e82ca6d84bfe5f839f58b35029a1d54 ; https://tdr.lib.ntu.edu.tw/handle/123456789/90111 | Theses (Chile, Taiwan) |
| https://skills.sh/openaec-foundation/computational-design-day-delft-march-2026/ifcos-impl-sequence | Community skill note on IfcOpenShell sequence (4D) implementation |

---

## 8. Gaps: addresses that could not be read

These were tried and failed during research. They are listed so nobody burns time or treats them as verified.

| Address or group | What happened |
|---|---|
| technical.buildingsmart.org, www.buildingsmart.org (rooms, chapter pages), standards.buildingsmart.org (some paths) | HTTP 403 to the fetch tool; content known only from search excerpts |
| forums.autodesk.com (all boards, Revit Ideas, Revit API forum) | HTTP 403; most Autodesk records are snippet-level |
| community.graphisoft.com | HTTP 403 |
| forum.tekla.com | Section listings return 403; internal search returns 0 anonymously |
| stackoverflow.com, api.stackexchange.com, gis.stackexchange.com | Fetch refused/blocked |
| Reddit | Not reachable without search; no record from Reddit exists in the KB |
| zhihu.com, zhuanlan.zhihu.com | 403 on every fetch |
| csdn.net | HTTP 521 or captcha |
| bilibili.com | Captcha on read pages |
| ptt.cc | 403 |
| cnblogs.com search, forum.dwg.ru search | Search URLs returned 404 or garbled text |
| people.thatopen.com | Login (Auth0) required |
| support.corenet.gov.sg | 403 |
| mediaconstruct.fr, buildingsmart.fr | 403; parked domain |
| forum.cad.de, forum.allplan.com, bimpedia.de, bimpedia.eu | DNS failure or connection refused |
| connect.allplan.com, forum.vectorworks.net | 403 |
| communities.bentley.com | JavaScript-only ServiceNow page |
| mohurd.gov.cn, bimbase.com | DNS error / TLS error |
| ksi.faufcc.ru, gge.ru, cyberforum.ru, tgstat.ru | Connection refused / 403 |
| bimconnected.com (expired certificate), bimnieuws.nl and thinkbim.org (did not resolve) | Not usable |
| forum.freecad.org | Anubis anti-bot page |
| planalto.gov.br | "Acesso Negado" |
| USACE CAD-BIM Center | Not reachable from the research environment |
| Naver cafes, VK groups, closed Telegram chats, LinkedIn, Facebook groups, Twitter/X | Not reached (login-gated or not searchable) |

Content gaps also remain by topic and language: for example, no real Italian, French, Portuguese or Dutch forum questions were read (the "real" records there are articles and official pages), and German forum voice is thin. See [communities_directory.md](communities_directory.md) for where to look next.

---

## Appendix A: forum threads (examples of real user language)

Each line is a thread address followed by what the research agent recorded about it (or, where the report gave none, a title taken from the address). Grouping is by the research cell where the address first appeared, which is a rough topic label (`t-` = topic cells, `p-` = persona cells, `en-` = English communities).

### A1. buildingSMART Technical Forums threads (Discourse)

**Research cell `en-buildingsmart-forums`**

- <https://forums.buildingsmart.org/t/5695> — IfcMapConversion written wrongly by software
- <https://forums.buildingsmart.org/t/6331> — empty/NIL IfcMapConversion in 4.3
- <https://forums.buildingsmart.org/t/4976> — how real-world placement is stored
- <https://forums.buildingsmart.org/t/5130> — what is a proxy
- <https://forums.buildingsmart.org/t/5951> — proxy Name rule WR1
- <https://forums.buildingsmart.org/t/5260> — proxy placement and validator
- <https://forums.buildingsmart.org/t/4272> — decomposition vs nesting
- <https://forums.buildingsmart.org/t/4372> — IfcCheckingTool PlacesObject
- <https://forums.buildingsmart.org/t/5049> — duplicate pset names
- <https://forums.buildingsmart.org/t/5521> — IfcRelDefinesByProperties with sets
- <https://forums.buildingsmart.org/t/5993> — validating IDS files
- <https://forums.buildingsmart.org/t/6234> — IDS applicability for all elements
- <https://forums.buildingsmart.org/t/5760> — IDS PredefinedType requirement
- <https://forums.buildingsmart.org/t/5740> — IDS table value data types
- <https://forums.buildingsmart.org/t/4199> — IDS vs IDM/MVD
- <https://forums.buildingsmart.org/t/3638> — material layers missing in Reference View
- <https://forums.buildingsmart.org/t/4605> — Revit IFC parsing errors
- <https://forums.buildingsmart.org/t/6528> — spatial reservation modeling
- <https://forums.buildingsmart.org/t/5239> — environmental impact values
- <https://forums.buildingsmart.org/t/6429> — Name/Reference usage

**Research cell `en-middle-east-africa`**

- <https://forums.buildingsmart.org/t/bottlenecks-faced-by-bim-professioonals/6633> — pain-point survey, no replies
- <https://forums.buildingsmart.org/t/bottlenecks-of-current-version-of-navisworks/6628> — beginner post, archived

**Research cell `en-us-canada-infra`**

- <https://forums.buildingsmart.org/t/cobie-to-ifc-export-issues/1860> — COBie from Revit, IFC4 MVD advice
- <https://forums.buildingsmart.org/t/exporting-bridge-elements-to-ifc-4-3-ifcbridge-or-ifcroad/5811> — bridge vs road scope
- <https://forums.buildingsmart.org/t/new-ifc-4x2-3-bridge-file-examples/5218> — sample bridge files
- <https://forums.buildingsmart.org/t/ifc-4x1-file-containing-alignment-is-not-opening-in-civil-3d/3830> — alignment interop
- <https://forums.buildingsmart.org/t/ifc-4x3-vs-4-1-changes/3217> — ifc 4x3 vs 4 1 changes
- <https://forums.buildingsmart.org/t/link-to-the-latest-ifc4-3-release-for-bridges-and-roads-developpements/4410> — link to the latest ifc4 3 release for bridges and roads developpements

**Research cell `p-architect`**

- <https://forums.buildingsmart.org/t/como-poder-exportar-un-modelo-3d-estructural-realizado-en-revit-a-etabs-por-medio-del-formato-ifc/2985> — Spanish ETABS
- <https://forums.buildingsmart.org/t/ids-and-federated-ifc-file/5654> — IDS on federated IFC

**Research cell `p-bim-coordinator`**

- <https://forums.buildingsmart.org/t/correct-use-of-ifc-name-and-reference-deprecated/6429> — naming attributes, Allplan, IFC 4.3
- <https://forums.buildingsmart.org/t/revit-to-ifc-wall-is-dislocated/4575> — IFC4 dislocated voided wall
- <https://forums.buildingsmart.org/t/ifc-mapping-in-revit-mep/4591> — shared parameter to duct Pset
- <https://forums.buildingsmart.org/t/roof-in-revit-and-ifcbuildingelementpart-ifc4/4989> — parts export
- <https://forums.buildingsmart.org/t/how-can-i-control-the-ifc-pipes-colors-revit-to-archicad/2729> — pipe colours Revit to ArchiCAD
- <https://forums.buildingsmart.org/t/a-number-of-interesting-revit-ifc-parsing-errors/4605> — parser errors on Revit IFC4

**Research cell `p-developer`**

- <https://forums.buildingsmart.org/t/ifc4-designtransferview-geometry/3116> — ifc4 designtransferview geometry

**Research cell `p-engineers`**

- <https://forums.buildingsmart.org/t/ifc-structural-analysis-view/1267> — ETABS export with no geometry
- <https://forums.buildingsmart.org/t/ifcstructuralanalysisdomain/832> — STAAD results via IFC
- <https://forums.buildingsmart.org/t/supported-data-type-volumetricflowrate-m-h/4189> — flow units MEP
- <https://forums.buildingsmart.org/t/ifc-files-that-reference-one-another/1804> — federation
- <https://forums.buildingsmart.org/t/rigid-link-representation-in-structural-analysis-model/1364> — rigid link representation in structural analysis model
- <https://forums.buildingsmart.org/t/user-defined-point-connection-between-structural-elements-structural-analysis-domain/2633> — user defined point connection between structural elements structural analysis domain
- <https://forums.buildingsmart.org/t/best-ifc-classification-for-a-reducing-coupling/5963> — best ifc classification for a reducing coupling
- <https://forums.buildingsmart.org/t/field-bent-rebar/5870> — field bent rebar
- <https://forums.buildingsmart.org/t/there-is-a-need-for-a-reinforcing-bar-group/5688> — there is a need for a reinforcing bar group
- <https://forums.buildingsmart.org/t/reinforcingbar-lap-lengths/6430> — reinforcingbar lap lengths

**Research cell `p-fm-owner-reviewer`**

- <https://forums.buildingsmart.org/t/qto-properties-expectations/6298> — Qto expectations

**Research cell `p-student`**

- <https://forums.buildingsmart.org/t/ifc-questions-from-a-beginner/2515> — ifc questions from a beginner
- <https://forums.buildingsmart.org/t/education-and-training-for-new-ifc-users/4925> — education and training for new ifc users
- <https://forums.buildingsmart.org/t/ifc-schema/3540> — ifc schema
- <https://forums.buildingsmart.org/t/ifc-documantation/1454> — ifc documantation
- <https://forums.buildingsmart.org/t/difference-between-expectations-and-reality-of-ifc-standards/1040> — difference between expectations and reality of ifc standards
- <https://forums.buildingsmart.org/t/ifc-materials/4861> — which material entity
- <https://forums.buildingsmart.org/t/understanding-ifc-alignment-and-rail-beginners-guide/4117> — understanding ifc alignment and rail beginners guide

**Research cell `t-classification-bsdd`**

- <https://forums.buildingsmart.org/t/uniclass-2015-and-ifc/4423> — Uniclass and IFC
- <https://forums.buildingsmart.org/t/bsdd-classification-mapping-and-specific-pset-values/4538> — bSDD NL-SfB mapping
- <https://forums.buildingsmart.org/t/how-does-ifc-work-with-existing-classification-systems-such-as-omniclass-uniformat-etc/804> — classic concept thread
- <https://forums.buildingsmart.org/t/lack-of-standardisation-of-ifcclassification/2581> — registry proposal
- <https://forums.buildingsmart.org/t/bsdd-access-for-products-and-classification-standard-bsdd-guid-vs-ifc-guid/1726> — bSDD GUIDs
- <https://forums.buildingsmart.org/t/bsdd-buildingsmart-data-dictionary-and-classification-of-ifc-4x3-domain-mapping/4854> — IFC4.3 domains

**Research cell `t-coordinates`**

- <https://forums.buildingsmart.org/t/we-have-a-problem-with-ifcmapconversion/5695> — we have a problem with ifcmapconversion
- <https://forums.buildingsmart.org/t/offset-stored-in-ifc-file-how-and-where/2848> — offset stored in ifc file how and where
- <https://forums.buildingsmart.org/t/how-is-the-real-world-placement-stored-in-a-ifc-file/4976> — how is the real world placement stored in a ifc file
- <https://forums.buildingsmart.org/t/article-about-ifc-coordinate-reference-systems-and-revit/1418> — article about ifc coordinate reference systems and revit
- <https://forums.buildingsmart.org/t/ifcsite-does-not-reference-the-epsg-code-for-wgs84-and-further-inconsistencies-with-georef/3499> — ifcsite does not reference the epsg code for wgs84 and further inconsistencies with georef

**Research cell `t-data-extraction`**

- <https://forums.buildingsmart.org/t/ifc-flat-data/4044> — ifc flat data
- <https://forums.buildingsmart.org/t/which-software-to-create-lists-of-quantities-of-the-used-building-materials/5181> — which software to create lists of quantities of the used building materials
- <https://forums.buildingsmart.org/t/ifc-for-relational-databases-ifcsql/1524> — ifc for relational databases ifcsql
- <https://forums.buildingsmart.org/t/store-modify-and-retrieve-ifc-data-with-ifcsql/1558> — store modify and retrieve ifc data with ifcsql
- <https://forums.buildingsmart.org/t/help-regarding-extracting-importing-data-from-ifc-to-estimation-software/3953> — help regarding extracting importing data from ifc to estimation software
- <https://forums.buildingsmart.org/t/ifc-to-gis/6115> — community state of IFC-to-GIS

**Research cell `t-error-messages`**

- <https://forums.buildingsmart.org/t/need-help-with-a-validation-issue/4372> — PlacesObject inverse violation
- <https://forums.buildingsmart.org/t/error-when-import-file-of-ifc3x2-into-blenderbim-do-the-shape-or-filesize-have-some-limits/3836> — "Failed to process representation item"
- <https://forums.buildingsmart.org/t/fatal-error-ifcguid-is-not-a-128-bit-number/3137> — GUID validity

**Research cell `t-file-size`**

- <https://forums.buildingsmart.org/t/processing-speed-ifc-imports/2622> — certification and speed, Uptown.ifc benchmark

**Research cell `t-gis-digital-twin`**

- <https://forums.buildingsmart.org/t/ifcprojectedcrs-epsg-code-not-known/972> — ifcprojectedcrs epsg code not known
- <https://forums.buildingsmart.org/t/the-future-of-ifc-for-urban-design-planning-development/3916> — the future of ifc for urban design planning development
- <https://forums.buildingsmart.org/t/rfi-urban-and-land-management-think-tank-room-group/4754> — rfi urban and land management think tank room group

**Research cell `t-infra-ifc43`**

- <https://forums.buildingsmart.org/t/startdistalong-in-ifcalignmenthorizontal-4-3-rc2/5118> — startdistalong in ifcalignmenthorizontal 4 3 rc2
- <https://forums.buildingsmart.org/t/new-alignment-and-need-for-stations-and-offsets/3330> — new alignment and need for stations and offsets
- <https://forums.buildingsmart.org/t/how-is-it-possible-to-import-german-rail-ver-esn-or-gnedit-in-ifc/2835> — how is it possible to import german rail ver esn or gnedit in ifc
- <https://forums.buildingsmart.org/t/alignment-based-reference-view/6414> — alignment based reference view
- <https://forums.buildingsmart.org/t/orientation-of-cross-sections-in-ifcsectionedsolidhorizontal-defined-by-ifcaxis2placementlinear/4696> — orientation of cross sections in ifcsectionedsolidhorizontal defined by ifcaxis2placementlinear
- <https://forums.buildingsmart.org/t/ifcalignment-axis-documentation-is-not-consistent-with-express-file-or-unit-tests/3695> — ifcalignment axis documentation is not consistent with express file or unit tests
- <https://forums.buildingsmart.org/t/exchange-road-network-with-ifc/1545> — exchange road network with ifc

**Research cell `t-materials-colors-layers`**

- <https://forums.buildingsmart.org/t/ifc-textures-and-colors-current-situation/2862> — inventory of colour/texture entities and support
- <https://forums.buildingsmart.org/t/why-is-it-so-difficult-to-get-colors-to-show-up/2312> — viewer inconsistency, precedence rule
- <https://forums.buildingsmart.org/t/where-and-how-will-my-colors-be-saved-in-ifc/1806> — Allplan colours lost
- <https://forums.buildingsmart.org/t/why-are-material-layer-sets-excluded-from-ifc4-reference-view-mvd/3638> — RV and layer sets
- <https://forums.buildingsmart.org/t/how-does-multiple-ifcpresentationlayerassignment-with-the-same-name-work/3126> — presentation layers

**Research cell `t-mep`**

- <https://forums.buildingsmart.org/t/mep-system-classification/2464> — mep system classification

**Research cell `t-openings-penetrations`**

- <https://forums.buildingsmart.org/t/provisionforvoid/1279> — provisionforvoid
- <https://forums.buildingsmart.org/t/what-is-the-right-ifc-entity-for-water-outlet-into-a-structural-ifc-model/1410> — what is the right ifc entity for water outlet into a structural ifc model
- <https://forums.buildingsmart.org/t/use-of-ifcopeningelement/4334> — use of ifcopeningelement
- <https://forums.buildingsmart.org/t/provision-for-voids-in-ifc4x3-rc1/2998> — provision for voids in ifc4x3 rc1
- <https://forums.buildingsmart.org/t/limit-of-fillsvoids/5124> — limit of fillsvoids
- <https://forums.buildingsmart.org/t/openings-with-multiple-hosts/1165> — openings with multiple hosts
- <https://forums.buildingsmart.org/t/can-opening-element-geometry-have-any-material-associated-with-it/4621> — can opening element geometry have any material associated with it

**Research cell `t-roundtrip-interop`**

- <https://forums.buildingsmart.org/t/strange-geometry-for-ifcopening/3869> — strange geometry for ifcopening
- <https://forums.buildingsmart.org/t/convert-upgrade-ifc2x3-to-ifc4/5210> — convert upgrade ifc2x3 to ifc4
- <https://forums.buildingsmart.org/t/next-steps-for-ifc-support-in-revit/3580> — next steps for ifc support in revit

**Research cell `t-spaces-areas`**

- <https://forums.buildingsmart.org/t/level1-boundary-generation-to-the-centre-line-or-inside-face/2724> — BEM boundary placement
- <https://forums.buildingsmart.org/t/space-data-depending-on-zone/4434> — space in several zones
- <https://forums.buildingsmart.org/t/relation-between-doors-to-rooms/3961> — doors to rooms
- <https://forums.buildingsmart.org/t/propertysets-of-ifcspace/3997> — IfcSpace property sets critique
- <https://forums.buildingsmart.org/t/ifcspace-and-ifcstair/1451> — space around stairs

**Research cell `t-validation-ids`**

- <https://forums.buildingsmart.org/t/how-to-validate-ids-files/5993> — how to validate ids files
- <https://forums.buildingsmart.org/t/applicability-for-all-elements/6234> — applicability for all elements
- <https://forums.buildingsmart.org/t/the-predefinedtype-shall-only-be-used/6180> — the predefinedtype shall only be used
- <https://forums.buildingsmart.org/t/requiring-the-existence-of-predefined-type/5760> — requiring the existence of predefined type
- <https://forums.buildingsmart.org/t/validation-of-quantities-using-ids/5326> — validation of quantities using ids
- <https://forums.buildingsmart.org/t/specifying-data-type-for-table-value-with-multiple-data-types/5740> — specifying data type for table value with multiple data types
- <https://forums.buildingsmart.org/t/what-is-the-relationship-between-ids-and-idm-or-mvd/4199> — what is the relationship between ids and idm or mvd
- <https://forums.buildingsmart.org/t/what-is-the-default-for-a-derived-unit-that-isnt-set-in-the-file/5759> — what is the default for a derived unit that isnt set in the file
- <https://forums.buildingsmart.org/t/guid-valid-invalid/3776> — guid valid invalid

**Research cell `t-versions-mvd`**

- <https://forums.buildingsmart.org/t/ifc4-design-transfer-view-experiences/4362> — DTV status
- <https://forums.buildingsmart.org/t/official-model-view-definitions-for-ifc-4-3/5737> — 4.3 MVDs
- <https://forums.buildingsmart.org/t/ifc4-design-transfer-view-spec/1737> — DTV spec missing
- <https://forums.buildingsmart.org/t/why-are-csg-representations-mandated-for-dtv/2311> — DTV debate
- <https://forums.buildingsmart.org/t/ifc-2x3-implementation-agreements-status-in-ifc4/2786> — CV in IFC4
- <https://forums.buildingsmart.org/t/ifc2x3-to-ifc4-mappings/3093> — migration mappings
- <https://forums.buildingsmart.org/t/list-of-changes-between-ifc-versions/4604> — changelog
- <https://forums.buildingsmart.org/t/ifc4-property-name-changes/2539> — renamed psets
- <https://forums.buildingsmart.org/t/geolocation-standards-in-ifc2x3-and-ifc4/2329> — georef across versions
- <https://forums.buildingsmart.org/t/bsi-software-certification-and-ifc4/3192> — certification
- <https://forums.buildingsmart.org/t/is-ifc-4-3-officially-a-change-in-the-naming-schema/5446> — naming

**Other buildingSMART forum pages**

- <https://forums.buildingsmart.org/tag/revit> — Revit-tagged thread list
- <https://forums.buildingsmart.org/c/users/6> — Users category

### A2. OSArch community threads (Discourse)

**Research cell `ai-mcp-usage`**

- <https://community.osarch.org/discussion/comment/30650> — AI-connected IFC 4.3 scheduler

**Research cell `en-osarch`**

- <https://community.osarch.org/discussion/3765/roadmap-for-revit-migrator-to-bonsai-bim-absolute-beginner> — Revit migrator
- <https://community.osarch.org/discussion/3783/claude-bonsai-construction-drawings> — claude bonsai construction drawings
- <https://community.osarch.org/discussion/3782/native-ifc-as-the-source-a-reproducible-project-template-for-bonsai-and-two-questions> — multi-file project trees
- <https://community.osarch.org/discussion/3750/german-drawing-conventions-din-1356-1-for-bonsais-2d-output-a-reference-from-vocational-training> — german drawing conventions din 1356 1 for bonsais 2d output a reference from vocational training
- <https://community.osarch.org/discussion/3478/ifctester-not-properly-check-predefinedtype-requirements> — ifctester not properly check predefinedtype requirements
- <https://community.osarch.org/discussion/2781/ifcconvert-how-to-control-the-resulting-step-models-scale> — ifcconvert how to control the resulting step models scale
- <https://community.osarch.org/discussion/3308/solved-ifctester-ifc-4-3-add2-support-question> — solved ifctester ifc 4 3 add2 support question
- <https://community.osarch.org/discussion/3754/opening-cuts-skipped-in-bonsai-studio-0-9> — Revit IFC openings warning
- <https://community.osarch.org/discussion/3685/bonsai-0-9-blender-5-2-2-new-void-system-improved-until-ist-was-broken> — bonsai 0 9 blender 5 2 2 new void system improved until ist was broken
- <https://community.osarch.org/discussion/3037/ifc-to-qgis-geopackage> — ifc to qgis geopackage
- <https://community.osarch.org/discussion/3043/canceled-revit-subscription-need-help-with-future-file-translations-to-ifc> — canceled revit subscription need help with future file translations to ifc
- <https://community.osarch.org/discussion/1753/bbim-two-door-types-with-connected-properties> — bbim two door types with connected properties
- <https://community.osarch.org/discussion/3514/rendering-png-snapshots-for-bcf-issues> — rendering png snapshots for bcf issues
- <https://community.osarch.org/discussion/3548/batch-editing-object-placement-for-multiple-editable-ifc-elements> — batch editing object placement for multiple editable ifc elements
- <https://community.osarch.org/discussion/2823/building-local-placement-in-bonsai> — building local placement in bonsai
- <https://community.osarch.org/discussion/3396/ai-chat-ifcopenshell-org-is-live> — ai chat ifcopenshell org is live
- <https://community.osarch.org/discussion/3567/should-a-drawing-in-bonsai-be-a-live-view-rather-than-a-generated-file> — should a drawing in bonsai be a live view rather than a generated file
- <https://community.osarch.org/discussion/3071/blender-bonsai-edit-ifc-file> — blender bonsai edit ifc file
- <https://community.osarch.org/discussion/261/layered-walls-in-blenderbim> — layered walls in blenderbim
- <https://community.osarch.org/discussion/95/ifc-export-newbie-question> — ifc export newbie question

**Research cell `en-us-canada-infra`**

- <https://community.osarch.org/discussion/2266/bbim-ifc-4x3-class-and-predefined-type-quick-guide-for-beginners> — bbim ifc 4x3 class and predefined type quick guide for beginners
- <https://community.osarch.org/discussion/3251/saikei-civil-native-ifc-for-horizontal-construction> — saikei civil native ifc for horizontal construction

**Research cell `p-architect`**

- <https://community.osarch.org/discussion/926/blenderbim-authoring-ifc-files-for-revit> — types for Revit
- <https://community.osarch.org/discussion/873/blenderbim-add-on-to-archicad-workflow> — Blender to Archicad
- <https://community.osarch.org/discussion/3541/long-term-workflow-blk360-revit-fiverr-ifc4-freecad-bim-ai-assisted-remodeling-is-this-a> — Revit IFC4 in FreeCAD

**Research cell `p-bim-coordinator`**

- <https://community.osarch.org/discussion/3616/browser-based-ifc-clash-version-diff-how-would-you-group-clashes-and-handle-guid-churn> — clash grouping and GUID churn
- <https://community.osarch.org/discussion/3579/clash-detection-error> — beginner clash error
- <https://community.osarch.org/discussion/3713/bonsaiviewer-and-clash-detection> — clash GUI
- <https://community.osarch.org/discussion/3768/syntopy-ifc-apps-powered-by-topologicpy> — clash/IDS/delivery compare apps
- <https://community.osarch.org/discussion/3568/massing-ifc-native-platform-from-feasibility-through-turnover-built-on-ifcopenshell-that-open> — federated clash, IDS, BCF

**Research cell `p-contractor-estimator`**

- <https://community.osarch.org/discussion/2887/dynamic-csv-to-cost-schedule-now-available> — CSV cost schedule discussion
- <https://community.osarch.org/discussion/1131/ifcopenshell-python-ifctask-predefinedtype-construction-demolition-move> — MOVE task in 4D

**Research cell `p-developer`**

- <https://community.osarch.org/discussion/1682/how-exactly-is-ifcopenshell-geom-create-shape-parsing-the-geometry> — how exactly is ifcopenshell geom create shape parsing the geometry
- <https://community.osarch.org/discussion/2704/get-ifcbeam-coordinates-in-3d-space> — get ifcbeam coordinates in 3d space
- <https://community.osarch.org/discussion/1307/detect-and-fix-objects-where-the-shell-is-not-closed> — detect and fix objects where the shell is not closed
- <https://community.osarch.org/discussion/2673/deleting-many-objects-takes-forever> — deleting many objects takes forever
- <https://community.osarch.org/discussions/tagged/ifc-geometry> — index of 28 geometry threads

**Research cell `p-engineers`**

- <https://community.osarch.org/discussion/3699/structural-analysis-in-bonsai-what-im-working-on> — structural analysis in bonsai what im working on

**Research cell `p-fm-owner-reviewer`**

- <https://community.osarch.org/discussion/2658/non-compliance-check> — checking IFC against IDS, redundant data debate
- <https://community.osarch.org/discussion/2273/ifctester-script-for-testing-several-ifcs-with-several-ids> — batch IDS validation
- <https://community.osarch.org/discussion/2969/filtering-new-building-components-in-ids-for-refurbishment-projects> — partial scope
- <https://community.osarch.org/discussion/3303/ids-check-for-ifcbuildingelementproxy-question> — IDS proxy check
- <https://community.osarch.org/discussion/2678/view-ids-xml-file-as-simplified-text-human-friendly-readable-ids> — readable IDS
- <https://community.osarch.org/discussions/tagged/ids> — 27 IDS threads

**Research cell `p-student`**

- <https://community.osarch.org/discussion/3280/i-am-a-beginner-i-created-a-file-in-bonsai-but-it-doesnt-appear-correctly-in-3d-in-revit> — i am a beginner i created a file in bonsai but it doesnt appear correctly in 3d in revit
- <https://community.osarch.org/discussion/1506/blenderbim-in-university-curriculum> — blenderbim in university curriculum
- <https://community.osarch.org/discussion/316/beginners-ifc-course-free-available> — beginners ifc course free available
- <https://community.osarch.org/discussion/635/ifcspace-and-blenderbim> — ifcspace and blenderbim
- <https://community.osarch.org/discussion/2758/composite-wall-in-bonsai-bim> — composite wall in bonsai bim
- <https://community.osarch.org/discussion/1827/what-are-the-various-use-cases-of-ifcgroup> — what are the various use cases of ifcgroup
- <https://community.osarch.org/discussions/tagged/education> — education

**Research cell `t-clash-bcf`**

- <https://community.osarch.org/discussion/2736/clash-detection-how-to/p1> — p1

**Research cell `t-classification-bsdd`**

- <https://community.osarch.org/discussion/3680/bsdd-dictionaries> — SICLIC dictionary
- <https://community.osarch.org/discussion/comment/29871#Comment_29871> — automatic rule based classification
- <https://community.osarch.org/discussion/comment/18591#Comment_18591> — export classification to CSV
- <https://community.osarch.org/discussion/2480/rfc-classification-s> — classification RFC

**Research cell `t-cobie-fm`**

- <https://community.osarch.org/discussion/726/how-to-convert-an-ifc-file-to-cobie-using-ifcopenshell-or-other-python-based-solution> — IFC to COBie via Python, COBie vs MVD
- <https://community.osarch.org/discussion/449/ifc-and-input-data-for-facility-management> — FM data without geometry
- <https://community.osarch.org/discussion/comment/25545> — asset management across many IFC projects
- <https://community.osarch.org/discussion/comment/30246> — COBie metres vs millimetres
- <https://community.osarch.org/discussion/3212/aec-open-source-framework> — CI export of validated IFC and COBie

**Research cell `t-coordinates`**

- <https://community.osarch.org/discussion/comment/29556/> — IFC2x3 georef psets in Bonsai

**Research cell `t-data-extraction`**

- <https://community.osarch.org/discussion/1535/ifc-stored-as-sqlite-and-mysql> — ifc stored as sqlite and mysql
- <https://community.osarch.org/discussion/3418/free-ifc-concrete-boq-looking-for-test-files-and-honest-feedback> — free ifc concrete boq looking for test files and honest feedback
- <https://community.osarch.org/discussion/3695/bcf-from-xlsx-file> — bcf from xlsx file
- <https://community.osarch.org/discussion/3519/exporting-ifc-file-schema> — exporting ifc file schema
- <https://community.osarch.org/discussion/comment/27265> — Quantity cross-check
- <https://community.osarch.org/discussion/comment/28482> — coordinates in spreadsheet exports

**Research cell `t-error-messages`**

- <https://community.osarch.org/discussion/3123/error-when-creating-custom-psets> — Bonsai traceback thread

**Research cell `t-file-size`**

- <https://community.osarch.org/discussion/comment/30702> — IFC to SQLite via WASM for large projects

**Research cell `t-geometry`**

- <https://community.osarch.org/discussion/3501/how-to-adjust-brep-tesselation-resolution-in-bonsai> — how to adjust brep tesselation resolution in bonsai
- <https://community.osarch.org/discussion/3741/add-parametric-framing-systems-railings-curtain-walls-storefronts> — add parametric framing systems railings curtain walls storefronts
- <https://community.osarch.org/discussion/comment/23266> — decimate IFC geometry

**Research cell `t-gis-digital-twin`**

- <https://community.osarch.org/discussion/comment/25984#Comment_25984> — IFC to QGIS GeoPackage
- <https://community.osarch.org/discussion/comment/27629#Comment_27629> — BlenderGIS moves IFC
- <https://community.osarch.org/discussion/comment/14415#Comment_14415> — IfcTimeSeries and sensors
- <https://community.osarch.org/discussion/comment/25545#Comment_25545> — IFC asset management at scale
- <https://community.osarch.org/discussion/1118/operation-and-maintenance-on-campus-site-with-ifc> — operation and maintenance on campus site with ifc
- <https://community.osarch.org/discussion/3136/georeferencing-mon-amour-first-steps> — georeferencing mon amour first steps

**Research cell `t-guid-versioning`**

- <https://community.osarch.org/discussion/comment/12255#Comment_12255> — 12255#Comment 12255
- <https://community.osarch.org/discussion/comment/11630#Comment_11630> — 11630#Comment 11630
- <https://community.osarch.org/discussion/comment/8352#Comment_8352> — 8352#Comment 8352
- <https://community.osarch.org/discussion/comment/13211#Comment_13211> — 13211#Comment 13211
- <https://community.osarch.org/discussion/3537/ifcdiff-in-bonsai-with-property-enabled-results-in-error> — ifcdiff in bonsai with property enabled results in error

**Research cell `t-materials-colors-layers`**

- <https://community.osarch.org/discussion/comment/30460> — layered walls in BlenderBIM

**Research cell `t-mep`**

- <https://community.osarch.org/discussion/2885/ifcpipefittingtype-does-not-import-ports-from-a-library> — ifcpipefittingtype does not import ports from a library

**Research cell `t-proxy-mapping`**

- <https://community.osarch.org/discussion/3598/add-subtypes> — reclassifying proxies in Bonsai
- <https://community.osarch.org/discussion/comment/3574> — roof from Revit

**Research cell `t-qto-cost`**

- <https://community.osarch.org/discussion/996/automating-cost-values-and-cost-quantities> — automating cost values and cost quantities
- <https://community.osarch.org/discussion/2963/small-script-to-print-pricedbillofquantities-to-pdf> — small script to print pricedbillofquantities to pdf
- <https://community.osarch.org/discussion/3437/openconstructionerp-qto-boq-and-ai-estimating-with-ifc-and-revit> — openconstructionerp qto boq and ai estimating with ifc and revit
- <https://community.osarch.org/discussion/3576/plan-measure-open-source-pdf-takeoff-tool-looking-for-aec-feedback> — plan measure open source pdf takeoff tool looking for aec feedback
- <https://community.osarch.org/discussion/comment/28629#Comment_28629> — door width Qto bug

**Research cell `t-spaces-areas`**

- <https://community.osarch.org/discussion/comment/30080> — IfcSpace and BlenderBim

**Research cell `t-structural`**

- <https://community.osarch.org/discussion/2578/how-to-create-a-custom-qto-calculation> — rebar weight Qto
- <https://community.osarch.org/discussion/2549/freecad-quantity-schedule> — rebar in FreeCAD
- <https://community.osarch.org/discussion/comment/30616#Comment_30616> — structural analysis in Bonsai / RFEM
- <https://community.osarch.org/discussion/3767/bim-the-untold-story> — STAAD from IFC

**Research cell `t-versions-mvd`**

- <https://community.osarch.org/discussion/898/ifc-file-doesnt-import-open-into-revit> — Revit Open limits

**Research cell `t-viewers-conversion`**

- <https://community.osarch.org/discussion/3150/free-standalone-revit-to-ifc-ifc2x3-ifc4-ifc4-3-ifcxml-conversion-without-revit-and-autodesk> — free standalone revit to ifc ifc2x3 ifc4 ifc4 3 ifcxml conversion without revit and autodesk

### A3. Dynamo forum threads

**Research cell `ai-revit-tasks`**

- <https://forum.dynamobim.com/t/would-you-use-an-mcp-based-ai-assistant-for-dynamo/114952> — AI opinions
- <https://forum.dynamobim.com/t/extract-areas-from-area-plans/115283> — extract areas from area plans
- <https://forum.dynamobim.com/t/automate-the-creation-of-view-plans-of-each-appartment-with-the-cropzone-aligning-exactly-on-the-outer-boundary-of-the-boudnary-walls-of-each-appartment/115202> — automate the creation of view plans of each appartment with the cropzone aligning exactly on the outer boundary of the boudnary walls of each appartment
- <https://forum.dynamobim.com/t/automatic-tagging/114838> — automatic tagging
- <https://forum.dynamobim.com/t/deleting-duplicate-instances-in-revit/115296> — deleting duplicate instances in revit
- <https://forum.dynamobim.com/t/updating-structural-foundation-size-parameters-via-excel-input/115236> — updating structural foundation size parameters via excel input
- <https://forum.dynamobim.com/t/issue-with-element-numbering-script-in-dynamo-revit/105235> — issue with element numbering script in dynamo revit
- <https://forum.dynamobim.com/t/help-with-automated-quality-check-script-getting-empty-list-and-blank-excel/112252> — help with automated quality check script getting empty list and blank excel
- <https://forum.dynamobim.com/t/extracting-telecom-data-port-quantities-from-bim-model-using-dynamo/114169> — extracting telecom data port quantities from bim model using dynamo
- <https://forum.dynamobim.com/t/set-room-style-based-on-room-name-input/115142> — set room style based on room name input
- <https://forum.dynamobim.com/t/automatically-fill-cable-tray-with-cables/115192> — automatically fill cable tray with cables
- <https://forum.dynamobim.com/t/delete-parameters-with-blank-value/115164> — delete parameters with blank value
- <https://forum.dynamobim.com/t/automating-wall-extraction-from-ifc/115089> — automating wall extraction from ifc
- <https://forum.dynamobim.com/t/exit-access-travel-distance/115179> — exit access travel distance
- <https://forum.dynamobim.com/t/fonts-update-all-project-fonts-to-a-different-font-attempt-at-aggregating-old-posts/113268> — fonts update all project fonts to a different font attempt at aggregating old posts
- <https://forum.dynamobim.com/t/deleting-zombie-parameters/112603> — deleting zombie parameters
- <https://forum.dynamobim.com/t/unload-revit-linked-with-its-worksets-closed/115193> — unload revit linked with its worksets closed
- <https://forum.dynamobim.com/t/automating-filter-creation/108901> — automating filter creation

**Research cell `en-dynamo-pyrevit`**

- <https://forum.dynamobim.com/t/ifc-export-node-return-an-empty-ifc/82822> — empty IFC, Export IFC in Document
- <https://forum.dynamobim.com/t/are-anyone-able-to-export-ifc-using-dynamo-in-revit-2027/115000> — Revit 2027 breakage
- <https://forum.dynamobim.com/t/ifc-export-settings-ifcfiletype/91626> — IFCFileType option
- <https://forum.dynamobim.com/t/completely-automated-ifc-export-on-remote-computer/30482> — nightly export
- <https://forum.dynamobim.com/t/unrecoverable-error-during-ifc-export-using-dynamo/113291> — decimal comma bug
- <https://forum.dynamobim.com/t/ifc-export-does-not-respect-mapping/112777> — mapping ignored
- <https://forum.dynamobim.com/t/ifc-batch-export-through-phases/31076> — ActivePhase option
- <https://forum.dynamobim.com/t/ifc-export-by-dynamo-internal-revit-property-set/22301> — Psets option
- <https://forum.dynamobim.com/t/store-ifc-guid-in-elements-without-exporting-ifc/24284> — GUID storage
- <https://forum.dynamobim.com/t/handle-ifc-guid-in-civil-3d/80717> — Civil 3D GUID
- <https://forum.dynamobim.com/t/set-export-type-to-ifc-as-parameter/110128> — IfcExportAs by script
- <https://forum.dynamobim.com/t/move-linked-ifc-to-right-coordinate-system/79767> — link placement
- <https://forum.dynamobim.com/t/ifc-revitlinkinstance-collect-data-from-ifc-elements/106608> — data from IFC link
- <https://forum.dynamobim.com/t/export-ifcrelspaceboundary-room-boundaries/91608> — space boundaries
- <https://forum.dynamobim.com/t/hide-ifc-element-in-a-view/79055> — IFC element filters
- <https://forum.dynamobim.com/t/ifcnodes-ai-powered-ifc-toolkit-for-dynamo/113569> — LLM + IFC
- <https://forum.dynamobim.com/t/duplicate-ifc-export-over-multiple-documents/115062> — multi-document pitfalls
- <https://forum.dynamobim.com/t/exporting-ifc-from-civil-3d-with-dynamo/114735> — Civil 3D IFC 4.3

### A4. pyRevit forum threads

**Research cell `ai-revit-tasks`**

- <https://discourse.pyrevitlabs.io/t/connecting-agent-to-pyrevit-mcp-newbie/10627> — connecting agent to pyrevit mcp newbie
- <https://discourse.pyrevitlabs.io/t/placing-elevations-on-sheet-one-elevation-behaves-differently/1467> — placing elevations on sheet one elevation behaves differently
- <https://discourse.pyrevitlabs.io/t/revit-model-compare-check-what-the-ai-actually-built/10681> — revit model compare check what the ai actually built

**Research cell `en-dynamo-pyrevit`**

- <https://discourse.pyrevitlabs.io/t/share-my-code-for-export-multiple-views-to-ifc/2553> — pyRevit multi-view export
- <https://discourse.pyrevitlabs.io/t/ifc-setup-loading-fails/9920> — config loading failure
- <https://discourse.pyrevitlabs.io/t/cliifc-export-does-not-output-ifc-file/8441> — CLI export
- <https://discourse.pyrevitlabs.io/t/access-to-ifcexporter/330> — reaching the IFC exporter DLLs
- <https://discourse.pyrevitlabs.io/t/ifcopenshell-how-to-start/8204> — IfcOpenShell newcomers
- <https://discourse.pyrevitlabs.io/t/how-to-use-python-package-like-langchain/2673> — packages in CPython

### A5. Autodesk forums threads (Revit, Revit API, Revit Ideas, Civil 3D)

**Research cell `en-autodesk-revit-export`**

- <https://forums.autodesk.com/t5/revit-architecture-forum/ifc-export-in-2027-mapping-parameters-severely-lacking/td-p/14229702> — Revit 2027 mapping GUI complaints
- <https://forums.autodesk.com/t5/revit-ideas/gui-for-project-parameter-mapping-in-ifc-export-missing-in-revit/idi-p/14097939> — GUI idea
- <https://forums.autodesk.com/t5/revit-structure-forum/ifcexportas-parameter-doesn-t-work/td-p/8219179> — classic IfcExportAs thread
- <https://forums.autodesk.com/t5/revit-architecture-forum/revit-ifc-export-user-defined-properties-won-t-export/td-p/9767878> — user-defined psets
- <https://forums.autodesk.com/t5/revit-architecture-forum/ifc-export-location-issue/td-p/14205433> — location issue 2025
- <https://forums.autodesk.com/t5/revit-structure-forum/ifc-shared-coordinates-export-issue/td-p/10143119> — shared coordinates
- <https://forums.autodesk.com/t5/revit-architecture-forum/revit-ifc4x3-export-incorrect-space-boundaries/m-p/14048745> — IFC4x3 vs Reference View
- <https://forums.autodesk.com/t5/revit-architecture-forum/elements-are-being-exported-to-the-wrong-ifc-level/td-p/11927737> — storey assignment
- <https://forums.autodesk.com/t5/revit-architecture-forum/export-curtain-wall-to-ifc-as-a-single-object/td-p/12907563> — curtain wall aggregate
- <https://forums.autodesk.com/t5/revit-architecture-forum/revit-2024-3-update-revit-crashes-every-time-i-export-ifc/td-p/13030432> — crash after update
- <https://forums.autodesk.com/t5/revit-mep-forum/ifc-export-ducts-and-pipes/td-p/12370919> — MEP classes
- <https://forums.autodesk.com/t5/revit-api-forum/ifc-export-options/td-p/9686404> — IFCExportOptions via API
- <https://forums.autodesk.com/t5/revit-ideas/support-revit-extended-properties-in-ifc-export/idi-p/14151910> — extended properties idea
- <https://forums.autodesk.com/t5/revit-architecture-forum/multiple-buildings-in-one-revit-project-ifc-export-issues/td-p/13781660> — multiple buildings

**Research cell `en-us-canada-infra`**

- <https://forums.autodesk.com/t5/civil-3d-forum/ifc-exporting-road-model/td-p/12923665> — td p
- <https://forums.autodesk.com/t5/revit-architecture-forum/cobie-type-length-cobie-type-width-cobie-type-height-is-always/td-p/11009379> — td p

**Research cell `es-latam`**

- <https://forums.autodesk.com/t5/revit-architecture-forum/revit-2026-won-t-export-to-ifc/m-p/13821992/highlight/true> — Revit 2026 export
- <https://forums.autodesk.com/t5/revit-architecture-forum/issues-exporting-ifc4x3-quot-unexpected-errors-occurred-while/m-p/13415457> — IFC4x3 errors
- <https://forums.autodesk.com/t5/revit-architecture-forum/ifc-export-empty-file/m-p/8336603> — empty file

**Research cell `es-spain`**

- <https://forums.autodesk.com/t5/revit-architecture-forum/problemas-con-ifc-s/td-p/10189111> — Spanish thread; 403 on fetch
- <https://forums.autodesk.com/t5/revit-architecture-forum/quesion-ifc-mapping-dissappearing-objects-in-export/td-p/7181576> — td p
- <https://forums.autodesk.com/t5/revit-architecture-forum/mapping-of-revit-parameters-to-ifc-parameters-for-export/td-p/7638232> — td p
- <https://forums.autodesk.com/t5/revit-architecture-forum/ifc-parameters-ifcexportas-and-ifcexporttype-not-outputting-to/td-p/7511389> — td p
- <https://forums.autodesk.com/t5/revit-architecture-forum/issues-with-exporting-type-parameters-from-revit-to-ifc/td-p/14004505> — td p
- <https://forums.autodesk.com/t5/revit-architecture-forum/missing-properties-when-exporting-ifc-from-revit-using-custom/td-p/13217311> — td p
- <https://forums.autodesk.com/t5/revit-structure-forum/steel-connections-ifc-exporter/td-p/10698321> — td p
- <https://forums.autodesk.com/autodesk/attachments/autodesk/revit-acc-navisworks-forum-es/19931/1/Exportar%20IFC.pdf> — Exportar IFC.pdf

**Research cell `p-architect`**

- <https://forums.autodesk.com/t5/revit-architecture-forum/problems-with-imported-ifc-from-archicad/td-p/11509535> — Archicad IFC into Revit problems
- <https://forums.autodesk.com/t5/revit-architecture-forum/ifc-import-problem-ceilings-walls/td-p/10593825> — ceilings/walls on import
- <https://forums.autodesk.com/t5/revit-architecture-forum/ifc-from-archicad-imported-into-revit-phasing-inconsistencies/td-p/13129044> — phasing lost
- <https://forums.autodesk.com/t5/revit-architecture-forum/ifc-exchange-revit-archicad/td-p/10357376> — IFC is not an intermediate format
- <https://forums.autodesk.com/t5/revit-structure-forum/ifc-export-option-include-steel-elements-messing-up-columns-and/m-p/9163932> — steel elements shift
- <https://forums.autodesk.com/t5/revit-structure-forum/is-there-a-final-answer-as-to-if-analytical-elements-can-be/m-p/9350321/highlight/true> — analytical elements via IFC

### A6. Graphisoft Community threads

**Research cell `p-architect`**

- <https://community.graphisoft.com/t5/Collaboration-with-other/Interoperability-issue-Share-model-with-consultants-working-in/td-p/341497> — sharing with Revit consultants
- <https://community.graphisoft.com/t5/Collaboration-with-other/Revit-IFC-to-Archicad-is-fundamentally-flawed/m-p/589984/highlight/true> — coordination not handover
- <https://community.graphisoft.com/t5/Collaboration-with-other/IFC-Model-Exchange-with-Archicad-for-Revit-2024-error/m-p/622653> — plugin crash
- <https://community.graphisoft.com/t5/Collaboration-with-other/Issues-with-exporting-Beams-from-Archicad-as-IFC-into-Revit/td-p/276679> — beams
- <https://community.graphisoft.com/t5/Modellierung/IFC-Export-aus-ArchiCAD-f%C3%BCr-Revit-MEP/m-p/544905> — German MEP export

### A7. Cesium community threads

**Research cell `t-gis-digital-twin`**

- <https://community.cesium.com/t/ifc-properties-for-geo-referencing-in-cesium-ion/43003> — which IFC fields ion actually uses
- <https://community.cesium.com/t/right-way-to-georeferencing-file-on-cesium/47030> — Revit IFC4 lands in the ocean
- <https://community.cesium.com/t/revit-coordinates-to-cesium-ion-viewer-coordinates/37407> — aligning IFC and tile coordinates
- <https://community.cesium.com/t/cant-retrieve-ifc-properties-and-attributes/40009> — reading IFC props in CesiumJS
- <https://community.cesium.com/t/how-to-get-features-in-bim-model/14683> — FME IFC to 3D Tiles
- <https://community.cesium.com/t/citygml-has-no-color-after-uploading-to-cesium-ion/31018> — CityGML colour bug
- <https://community.cesium.com/t/how-can-i-convert-my-ifc-files-into-citygml-files-in-order-to-visualize-them-on-cesium-globe/13781> — how can i convert my ifc files into citygml files in order to visualize them on cesium globe
- <https://community.cesium.com/t/ifc-metadata-not-shown-when-it-is-korean/44612> — Korean metadata
- <https://community.cesium.com/t/cesium-mcp-servers-for-ai-workflows-your-input-needed/44465> — MCP angle

**Additional Graphisoft thread (Spanish-language research cell `es-spain`)**

- <https://community.graphisoft.com/t5/Collaborate-forum/IFC-export-import-Revit/td-p/352151> — IFC export/import with Revit (page `[blocked]`, 403)

## Appendix B: GitHub issue and discussion threads

GitHub trackers are the only places where real chat prompts to AI assistants can be seen (MCP repositories) and where Revit IFC bugs are reported in the reporters' own words. For the four big repositories only a selection (those with a recorded one-line description) is shown; the repository's own issue list is the full source. Each KB record for these is a `real` record whose `source_url` is the issue address; use `python tools/kb.py filter --kind real --text <keyword>` to find them.

**Autodesk/revit-ifc** (205 threads cited in the research; 40 shown)

- <https://github.com/Autodesk/revit-ifc/issues/15> — Link IFC IfcSpace to Room
- <https://github.com/Autodesk/revit-ifc/issues/223> — Open vs Link IFC with Tekla assemblies
- <https://github.com/Autodesk/revit-ifc/issues/301> — double True North rotation
- <https://github.com/Autodesk/revit-ifc/issues/320> — Import at project base point, solved in 2026
- <https://github.com/Autodesk/revit-ifc/issues/378> — GlobalIds not unique
- <https://github.com/Autodesk/revit-ifc/issues/408> — Relinking and shared parameter GUIDs
- <https://github.com/Autodesk/revit-ifc/issues/480> — IfcAdvancedBrep
- <https://github.com/Autodesk/revit-ifc/issues/481> — fascias and wall sweeps cannot override proxy
- <https://github.com/Autodesk/revit-ifc/issues/492> — slow export
- <https://github.com/Autodesk/revit-ifc/issues/522> — Link IFC project north vs true north
- <https://github.com/Autodesk/revit-ifc/issues/541> — IfcExportAs ignored since Revit 2023, workflow impact
- <https://github.com/Autodesk/revit-ifc/issues/566> — IFC to Revit with shared coordinates
- <https://github.com/Autodesk/revit-ifc/issues/577> — system material vs real material
- <https://github.com/Autodesk/revit-ifc/issues/579> — grey MEP components
- <https://github.com/Autodesk/revit-ifc/issues/583> — generic export error, downgrade fix
- <https://github.com/Autodesk/revit-ifc/issues/587> — IfcTriangulatedFaceSet in Revit
- <https://github.com/Autodesk/revit-ifc/issues/609> — shaft openings in floors
- <https://github.com/Autodesk/revit-ifc/issues/658> — DirectShape validation errors in linked MEP IFC
- <https://github.com/Autodesk/revit-ifc/issues/676> — auto-generated proxy types from curtain wall pieces
- <https://github.com/Autodesk/revit-ifc/issues/710> — Link IFC vs .ifc.rvt rotation difference
- <https://github.com/Autodesk/revit-ifc/issues/752> — psets per predefined type
- <https://github.com/Autodesk/revit-ifc/issues/759> — floors not exporting, locale encoding root cause
- <https://github.com/Autodesk/revit-ifc/issues/768> — IFC4x3 quantities
- <https://github.com/Autodesk/revit-ifc/issues/778> — How IFC entities map to Revit on import
- <https://github.com/Autodesk/revit-ifc/issues/798> — Import class mapping tables
- <https://github.com/Autodesk/revit-ifc/issues/833> — LoadBearing overwrite
- <https://github.com/Autodesk/revit-ifc/issues/856> — disable Uniformat enhancement, localised parameter names
- <https://github.com/Autodesk/revit-ifc/issues/880> — linked files in one IFC
- <https://github.com/Autodesk/revit-ifc/issues/907> — rooms elevation with survey-point levels
- <https://github.com/Autodesk/revit-ifc/issues/924> — room geometry shifted
- <https://github.com/Autodesk/revit-ifc/issues/951> — Link IFC hangs on single chair
- <https://github.com/Autodesk/revit-ifc/issues/960> — category not exportable in UDPset
- <https://github.com/Autodesk/revit-ifc/issues/963> — empty parameter values not exported
- <https://github.com/Autodesk/revit-ifc/issues/984> — Revit 2027 Manage Property dialog
- <https://github.com/Autodesk/revit-ifc/issues/985> — missing opening cut at flush beam
- <https://github.com/Autodesk/revit-ifc/issues/990> — Link IFC Z coordinate doubled (2025-27)
- <https://github.com/Autodesk/revit-ifc/issues/992> — AccessViolationException curtain walls IFC4
- <https://github.com/Autodesk/revit-ifc/issues/1013> — Reference View header
- <https://github.com/Autodesk/revit-ifc/issues/1019> — Archicad windows outside wall in Revit 2025-2027
- <https://github.com/Autodesk/revit-ifc/issues/1021> — unrecoverable export error on workshared model

**IfcOpenShell/IfcOpenShell** (184 threads cited in the research; 40 shown)

- <https://github.com/IfcOpenShell/IfcOpenShell/issues/571> — Chinese encoding in IFC generation
- <https://github.com/IfcOpenShell/IfcOpenShell/issues/2025> — large IFC datasets
- <https://github.com/IfcOpenShell/IfcOpenShell/issues/3098> — IfcGradientCurve not implemented
- <https://github.com/IfcOpenShell/IfcOpenShell/issues/3115> — annotation context
- <https://github.com/IfcOpenShell/IfcOpenShell/issues/3464> — IfcRoad creation
- <https://github.com/IfcOpenShell/IfcOpenShell/issues/3499> — Cyrillic/Chinese truncation in ifcXML
- <https://github.com/IfcOpenShell/IfcOpenShell/issues/3901> — IfcFM Excel export error
- <https://github.com/IfcOpenShell/IfcOpenShell/issues/3978> — Revit exporter versions and property extraction
- <https://github.com/IfcOpenShell/IfcOpenShell/issues/4921> — IFC4 to IFC4.3 upgrade for IfcRoad
- <https://github.com/IfcOpenShell/IfcOpenShell/issues/4933> — alignment authoring proposal
- <https://github.com/IfcOpenShell/IfcOpenShell/issues/5049> — linear placement of signal
- <https://github.com/IfcOpenShell/IfcOpenShell/issues/5155> — product resource wrong quantity
- <https://github.com/IfcOpenShell/IfcOpenShell/issues/5349> — mesh window area differs between engines
- <https://github.com/IfcOpenShell/IfcOpenShell/issues/5471> — clearance volume from alignment
- <https://github.com/IfcOpenShell/IfcOpenShell/issues/5702> — COBie export traceback
- <https://github.com/IfcOpenShell/IfcOpenShell/issues/5926> — missing COBie tabs
- <https://github.com/IfcOpenShell/IfcOpenShell/issues/6026> — 764 MB OOM from face-based surface models
- <https://github.com/IfcOpenShell/IfcOpenShell/issues/6068> — empty Systems tab explained
- <https://github.com/IfcOpenShell/IfcOpenShell/issues/6120> — Revit wall openings
- <https://github.com/IfcOpenShell/IfcOpenShell/issues/6138> — clash point semantics
- <https://github.com/IfcOpenShell/IfcOpenShell/issues/6254> — infra authoring API RFC
- <https://github.com/IfcOpenShell/IfcOpenShell/issues/6401> — cost calculation discrepancy
- <https://github.com/IfcOpenShell/IfcOpenShell/issues/6712> — IfcOpenShell vs xBIM timings, 12-700 MB
- <https://github.com/IfcOpenShell/IfcOpenShell/issues/6886> — Unsupported schema IFC4X3
- <https://github.com/IfcOpenShell/IfcOpenShell/issues/6888> — railway parts
- <https://github.com/IfcOpenShell/IfcOpenShell/issues/7016> — linked georeferenced plan view
- <https://github.com/IfcOpenShell/IfcOpenShell/issues/7095> — manufacturer pset reporting
- <https://github.com/IfcOpenShell/IfcOpenShell/issues/7152> — BIMcollab no viewpoint to zoom
- <https://github.com/IfcOpenShell/IfcOpenShell/issues/7456> — facility spatial decomposition
- <https://github.com/IfcOpenShell/IfcOpenShell/issues/7621> — stringlines
- <https://github.com/IfcOpenShell/IfcOpenShell/issues/7829> — IfcFile memory when reopening
- <https://github.com/IfcOpenShell/IfcOpenShell/issues/7856> — IDS USERDEFINED
- <https://github.com/IfcOpenShell/IfcOpenShell/issues/7945> — LLM-fabricated IFC rejected by viewers
- <https://github.com/IfcOpenShell/IfcOpenShell/issues/8116> — sectioned surface with cant
- <https://github.com/IfcOpenShell/IfcOpenShell/issues/8205> — georeferenced drawings and BCF
- <https://github.com/IfcOpenShell/IfcOpenShell/issues/9055> — viewer load-time comparison
- <https://github.com/IfcOpenShell/IfcOpenShell/issues/9235> — gross vs net side area against Solibri
- <https://github.com/IfcOpenShell/IfcOpenShell/issues/9770> — precision far from origin
- <https://github.com/IfcOpenShell/IfcOpenShell/issues/9866> — Bonsai structural analysis plan
- <https://github.com/IfcOpenShell/IfcOpenShell/issues/10119> — IfcConvert >2 GiB

**ThatOpen/engine_web-ifc** (36 threads cited in the research; 25 shown)

- <https://github.com/ThatOpen/engine_web-ifc/issues/91> — Cesium + high coordinates
- <https://github.com/ThatOpen/engine_web-ifc/issues/302> — local vs global coordinates
- <https://github.com/ThatOpen/engine_web-ifc/issues/358> — Danish \X\E6
- <https://github.com/ThatOpen/engine_web-ifc/issues/419> — 2 GB models fail
- <https://github.com/ThatOpen/engine_web-ifc/issues/440> — Czech export corrupted
- <https://github.com/ThatOpen/engine_web-ifc/issues/468> — MacRoman in ArchiCAD files
- <https://github.com/ThatOpen/engine_web-ifc/issues/538> — super large model aborts
- <https://github.com/ThatOpen/engine_web-ifc/issues/895> — mapped item wrong location
- <https://github.com/ThatOpen/engine_web-ifc/issues/926> — and /878 alignment not read or displayed
- <https://github.com/ThatOpen/engine_web-ifc/issues/933> — clipping result
- <https://github.com/ThatOpen/engine_web-ifc/issues/948> — structural analytical items
- <https://github.com/ThatOpen/engine_web-ifc/issues/949> — `\X2\` lowercase hex Chinese text
- <https://github.com/ThatOpen/engine_web-ifc/issues/967> — why demo vs template differ (geometry merging)
- <https://github.com/ThatOpen/engine_web-ifc/issues/1171> — IFC4X3_ADD2 won't open
- <https://github.com/ThatOpen/engine_web-ifc/issues/1402> — "No basis found for brep"
- <https://github.com/ThatOpen/engine_web-ifc/issues/1559> — malformed escape breaks whole file
- <https://github.com/ThatOpen/engine_web-ifc/issues/1752> — parsing speed
- <https://github.com/ThatOpen/engine_web-ifc/issues/1793> — IFC4 loses colours vs IFC2x3
- <https://github.com/ThatOpen/engine_web-ifc/issues/1816> — indexing properties on 400-500 MB models
- <https://github.com/ThatOpen/engine_web-ifc/issues/1833> — material colour chain ignored
- <https://github.com/ThatOpen/engine_web-ifc/issues/1873> — type properties empty
- <https://github.com/ThatOpen/engine_web-ifc/issues/1999> — 400 MB+ Revit MEP IFC4 WASM crashes
- <https://github.com/ThatOpen/engine_web-ifc/issues/2097> — waffle slab hang
- <https://github.com/ThatOpen/engine_web-ifc/issues/2235> — type-level material colour
- <https://github.com/ThatOpen/engine_web-ifc/issues/2269> — triangle surfaces across openings, tolerance

**xBimTeam/XbimEssentials** (20 threads cited in the research; 15 shown)

- <https://github.com/xBimTeam/XbimEssentials/issues/93> — Civil 3D plugin with xBIM
- <https://github.com/xBimTeam/XbimEssentials/issues/531> — tessellation performance
- <https://github.com/xBimTeam/XbimEssentials/issues/605> — Japanese text, doubled backslash
- <https://github.com/xBimTeam/XbimEssentials/issues/614> — IFC4x3 class tree and psets
- <https://github.com/xBimTeam/XbimEssentials/issues/616> — storeys in Revit IFC4x3
- <https://github.com/xBimTeam/XbimEssentials/issues/619> — area and volume
- <https://github.com/xBimTeam/XbimEssentials/issues/620> — memory growth in server
- <https://github.com/xBimTeam/XbimEssentials/issues/633> — add opening to wall
- <https://github.com/xBimTeam/XbimEssentials/issues/642> — retrieving materials and colours
- <https://github.com/xBimTeam/XbimEssentials/issues/660> — newline in \X2\ string
- <https://github.com/xBimTeam/XbimEssentials/issues/661> — IFC4 TagList validation
- <https://github.com/xBimTeam/XbimEssentials/issues/665> — v6 export slowdown
- <https://github.com/xBimTeam/XbimEssentials/issues/666> — IFC4x3 colors missing
- <https://github.com/xBimTeam/XbimEssentials/issues/674> — IsTypedBy regression
- <https://github.com/xBimTeam/XbimEssentials/issues/676> — world vertices vs rotated IfcSite

**ThatOpen/engine_components** (11 threads cited in the research; 10 shown)

- <https://github.com/ThatOpen/engine_components/issues/414> — IFCSPACE not classified in storeys
- <https://github.com/ThatOpen/engine_components/issues/495> — georeferenced IFC orientation
- <https://github.com/ThatOpen/engine_components/issues/503> — 90 MB IFC at 10 fps; IfcStreamer answer
- <https://github.com/ThatOpen/engine_components/issues/515> — big IFC crashes the app
- <https://github.com/ThatOpen/engine_components/issues/642> — first-time evaluation complaints
- <https://github.com/ThatOpen/engine_components/issues/653> — byIfcBuildingStorey misses elements
- <https://github.com/ThatOpen/engine_components/issues/743> — alignment children in spatial structure
- <https://github.com/ThatOpen/engine_components/issues/745> — all geometry white
- <https://github.com/ThatOpen/engine_components/issues/825> — BCF export well-formedness
- <https://github.com/ThatOpen/engine_components/issues/830> — IDS facets as stubs

**buildingSMART/IDS** (8 threads cited in the research; 8 shown)

- <https://github.com/buildingSMART/IDS/issues/176> — AND conditions in IDS
- <https://github.com/buildingSMART/IDS/issues/189> — property without pset in EIRs
- <https://github.com/buildingSMART/IDS/issues/223> — Classification facet behaviour
- <https://github.com/buildingSMART/IDS/issues/337> — datatype mismatch bypasses checks
- <https://github.com/buildingSMART/IDS/issues/379> — conditional PartOf
- <https://github.com/buildingSMART/IDS/issues/400> — issues
- <https://github.com/buildingSMART/IDS/issues/403> — empty string and cardinality
- <https://github.com/buildingSMART/IDS/issues/447> — issues

**ThatOpen/engine_fragment** (8 threads cited in the research; 8 shown)

- <https://github.com/ThatOpen/engine_fragment/issues/129> — 1.3 GB model
- <https://github.com/ThatOpen/engine_fragment/issues/160> — projected CRS placement
- <https://github.com/ThatOpen/engine_fragment/issues/164> — indexed queries in .frag
- <https://github.com/ThatOpen/engine_fragment/issues/168> — missing type properties vs Solibri
- <https://github.com/ThatOpen/engine_fragment/issues/228> — 40 models performance
- <https://github.com/ThatOpen/engine_fragment/issues/258> — >2 GB WASM ceiling
- <https://github.com/ThatOpen/engine_fragment/issues/301> — IfcSpace box above roof
- <https://github.com/ThatOpen/engine_fragment/issues/315> — 2 GB industrial model with P6 schedule

**buildingSMART/IFC4.x-development** (5 threads cited in the research; 5 shown)

- <https://github.com/buildingSMART/IFC4.x-development/issues/147> — port axis logic
- <https://github.com/buildingSMART/IFC4.x-development/issues/205> — issues
- <https://github.com/buildingSMART/IFC4.x-development/issues/698> — Pset_Warranty vs COBie
- <https://github.com/buildingSMART/IFC4.x-development/issues/976> — stair width, code checking, CORENET X
- <https://github.com/buildingSMART/IFC4.x-development/issues/1212> — openings and decomposition

**OpenAEC-Foundation/OpenAEC-BIM-validator** (5 threads cited in the research; 5 shown)

- <https://github.com/OpenAEC-Foundation/OpenAEC-BIM-validator/issues/12> — issues
- <https://github.com/OpenAEC-Foundation/OpenAEC-BIM-validator/issues/17> — Smart Views
- <https://github.com/OpenAEC-Foundation/OpenAEC-BIM-validator/issues/19> — takeoff to Excel
- <https://github.com/OpenAEC-Foundation/OpenAEC-BIM-validator/issues/21> — federation georeferencing
- <https://github.com/OpenAEC-Foundation/OpenAEC-BIM-validator/issues/22> — NL-SfB content check

**opensourceBIM/BIMserver** (5 threads cited in the research; 5 shown)

- <https://github.com/opensourceBIM/BIMserver/issues/1103> — IFC4 ArchiCAD
- <https://github.com/opensourceBIM/BIMserver/issues/1162> — slow loading of large models
- <https://github.com/opensourceBIM/BIMserver/issues/1201> — JSON API query vs loops
- <https://github.com/opensourceBIM/BIMserver/issues/1327> — FM sensor updates discussion
- <https://github.com/opensourceBIM/BIMserver/issues/1334> — issues

**xBimTeam/XbimGeometry** (5 threads cited in the research; 5 shown)

- <https://github.com/xBimTeam/XbimGeometry/issues/335> — hang
- <https://github.com/xBimTeam/XbimGeometry/issues/511> — performance metrics
- <https://github.com/xBimTeam/XbimGeometry/issues/515> — Revit geometry wrong in xBIM
- <https://github.com/xBimTeam/XbimGeometry/issues/527> — issues
- <https://github.com/xBimTeam/XbimGeometry/issues/547> — invisible geometry due to Plan context

**bimwright/rvt-mcp** (4 threads cited in the research; 4 shown)

- <https://github.com/bimwright/rvt-mcp/issues/13> — door placement ignores coordinates
- <https://github.com/bimwright/rvt-mcp/issues/14> — stairs and send_code crash
- <https://github.com/bimwright/rvt-mcp/issues/21> — mutating tools fail
- <https://github.com/bimwright/rvt-mcp/issues/23> — context compaction

**LTplus-AG/ifc-lite** (4 threads cited in the research; 4 shown)

- <https://github.com/LTplus-AG/ifc-lite/issues/3612> — BCF import fails in three tools
- <https://github.com/LTplus-AG/ifc-lite/issues/4099> — free BCF viewer question
- <https://github.com/LTplus-AG/ifc-lite/issues/4806> — BCF without colliding objects
- <https://github.com/LTplus-AG/ifc-lite/issues/6459> — Solibri imports 0 topics

**mcp-servers-for-revit/mcp-servers-for-revit** (4 threads cited in the research; 4 shown)

- <https://github.com/mcp-servers-for-revit/mcp-servers-for-revit/issues/1> — connection failure with a 10 m wall prompt
- <https://github.com/mcp-servers-for-revit/mcp-servers-for-revit/issues/30> — knowledge-graph proposal with false-"done" benchmark
- <https://github.com/mcp-servers-for-revit/mcp-servers-for-revit/issues/48> — command instance failure
- <https://github.com/mcp-servers-for-revit/mcp-servers-for-revit/issues/63> — port and autostart config

**nl-digigo/NLCS** (4 threads cited in the research; 4 shown)

- <https://github.com/nl-digigo/NLCS/issues/38> — NLCS vs NL-SfB in Revit
- <https://github.com/nl-digigo/NLCS/issues/147> — IFC 4.3 alignment
- <https://github.com/nl-digigo/NLCS/issues/238> — Revit template question
- <https://github.com/nl-digigo/NLCS/issues/687> — Revit to IFC quantities experiment

**shuotao/REVIT_MCP_study** (4 threads cited in the research; 4 shown)

- <https://github.com/shuotao/REVIT_MCP_study/issues/99> — issues
- <https://github.com/shuotao/REVIT_MCP_study/issues/110> — pyRevit button limits
- <https://github.com/shuotao/REVIT_MCP_study/issues/144> — create_wall level selection (zh-TW)
- <https://github.com/shuotao/REVIT_MCP_study/issues/150> — DWG beams to walls

**buildingSMART/validate** (3 threads cited in the research; 3 shown)

- <https://github.com/buildingSMART/validate/issues/77> — issues
- <https://github.com/buildingSMART/validate/issues/266> — issues
- <https://github.com/buildingSMART/validate/issues/267> — issues

**ifcquery/ifcplusplus** (3 threads cited in the research; 3 shown)

- <https://github.com/ifcquery/ifcplusplus/issues/210> — bad openings / CSG eps
- <https://github.com/ifcquery/ifcplusplus/issues/303> — large coordinate precision
- <https://github.com/ifcquery/ifcplusplus/issues/305> — GUID first char regression

**mcp-servers-for-revit/revit-mcp** (3 threads cited in the research; 3 shown)

- <https://github.com/mcp-servers-for-revit/revit-mcp/issues/26> — using Mistral or Llama
- <https://github.com/mcp-servers-for-revit/revit-mcp/issues/28> — "list all pipes" Method not found
- <https://github.com/mcp-servers-for-revit/revit-mcp/issues/30> — issues

**specklesystems/speckle-server** (3 threads cited in the research; 3 shown)

- <https://github.com/specklesystems/speckle-server/issues/1128> — issues
- <https://github.com/specklesystems/speckle-server/issues/1168> — IFC traversal in connectors
- <https://github.com/specklesystems/speckle-server/issues/5773> — IFC importer missing quantities

**buildingSMART/BCF-XML** (2 threads cited in the research; 2 shown)

- <https://github.com/buildingSMART/BCF-XML/issues/358> — topic GUID mismatch
- <https://github.com/buildingSMART/BCF-XML/issues/399> — snapshots mandatory?

**mcp-servers-for-revit/revit-mcp-plugin** (2 threads cited in the research; 2 shown)

- <https://github.com/mcp-servers-for-revit/revit-mcp-plugin/issues/5> — tutorial request
- <https://github.com/mcp-servers-for-revit/revit-mcp-plugin/issues/11> — Chinese post on developer job fears

**opensourceBIM/COBie-plugins** (2 threads cited in the research; 2 shown)

- <https://github.com/opensourceBIM/COBie-plugins/issues/10> — curtain wall COBie export
- <https://github.com/opensourceBIM/COBie-plugins/issues/13> — blank rows in COBie.xls

**tempalg1n/tekla-mcp-server** (2 threads cited in the research; 2 shown)

- <https://github.com/tempalg1n/tekla-mcp-server/issues/25> — issues
- <https://github.com/tempalg1n/tekla-mcp-server/issues/44> — issues

**xBimTeam/XbimWebUI** (2 threads cited in the research; 2 shown)

- <https://github.com/xBimTeam/XbimWebUI/issues/438> — Archicad IFC in web viewer
- <https://github.com/xBimTeam/XbimWebUI/issues/490> — large wexbim in browser

**Aedes-datastandaarden/ILS-woco** (1 threads cited in the research; 1 shown)

- <https://github.com/Aedes-datastandaarden/ILS-woco/issues/2> — NL-SfB code correction

**aware-aeco/aware** (1 threads cited in the research; 1 shown)

- <https://github.com/aware-aeco/aware/issues/422> — issues

**BHoM/ETABS_Toolkit** (1 threads cited in the research; 1 shown)

- <https://github.com/BHoM/ETABS_Toolkit/issues/548> — issues

**BIM-Tools/SketchUp-IFC-Manager** (1 threads cited in the research; 1 shown)

- <https://github.com/BIM-Tools/SketchUp-IFC-Manager/issues/63> — stray proxies from SketchUp

**buildingsmart-community/bSDD-Revit-plugin** (1 threads cited in the research; 1 shown)

- <https://github.com/buildingsmart-community/bSDD-Revit-plugin/issues/77> — NL-SfB 2005 in bSDD Revit plugin

**buildingSMART/IDS-Audit-tool** (1 threads cited in the research; 1 shown)

- <https://github.com/buildingSMART/IDS-Audit-tool/issues/56> — IFC2x3 occurrence mapping

**buildingSMART/IFC4.x-IF** (1 threads cited in the research; 1 shown)

- <https://github.com/buildingSMART/IFC4.x-IF/issues/6> — .ifczip extension suggestion

**FreeCAD/FreeCAD** (1 threads cited in the research; 1 shown)

- <https://github.com/FreeCAD/FreeCAD/issues/33914> — STEP exports raw CJK characters

**Gaia3D/mago-3d-tiler** (1 threads cited in the research; 1 shown)

- <https://github.com/Gaia3D/mago-3d-tiler/issues/79> — IFC4 not loading in tiler

**GeometryGym/GeometryGymIFC** (1 threads cited in the research; 1 shown)

- <https://github.com/GeometryGym/GeometryGymIFC/issues/109> — local coordinate system extraction

**geosolutions-it/digital-twin-toolbox** (1 threads cited in the research; 1 shown)

- <https://github.com/geosolutions-it/digital-twin-toolbox/issues/68> — issues

**IFCjs/web-ifc-three** (1 threads cited in the research; 1 shown)

- <https://github.com/IFCjs/web-ifc-three/issues/125> — slow getPropertySets (legacy)

**IFCjs/web-ifc-viewer** (1 threads cited in the research; 1 shown)

- <https://github.com/IFCjs/web-ifc-viewer/issues/205> — spatial tree (legacy)

**IndustryFoundationClasses/Questions** (1 threads cited in the research; 1 shown)

- <https://github.com/IndustryFoundationClasses/Questions/issues/15> — tools for IFC to COBie

**ingelibre/ingetrazo** (1 threads cited in the research; 1 shown)

- <https://github.com/ingelibre/ingetrazo/issues/1033> — IFC import question

**jmarinderko/calculadora-RIC** (1 threads cited in the research; 1 shown)

- <https://github.com/jmarinderko/calculadora-RIC/issues/10> — IFC export feature

**LetsConstructIT/Grasshopper-TeklaDrawingLink** (1 threads cited in the research; 1 shown)

- <https://github.com/LetsConstructIT/Grasshopper-TeklaDrawingLink/issues/147> — issues

**LuDattilo/revit-mcp-server** (1 threads cited in the research; 1 shown)

- <https://github.com/LuDattilo/revit-mcp-server/issues/16> — view screenshot for vision models

**Menezeris/AIMviewer** (1 threads cited in the research; 1 shown)

- <https://github.com/Menezeris/AIMviewer/issues/65> — camera control prompts (Slovak)

**nl-digigo/GeoBIM_Georefereren** (1 threads cited in the research; 1 shown)

- <https://github.com/nl-digigo/GeoBIM_Georefereren/issues/5> — GEO point and BIM origin

**nl-digigo/imwo** (1 threads cited in the research; 1 shown)

- <https://github.com/nl-digigo/imwo/issues/52> — NL-SfB installations vs IfcDistributionSystem

**OpenAEC-Foundation/open-bim-platform** (1 threads cited in the research; 1 shown)

- <https://github.com/OpenAEC-Foundation/open-bim-platform/issues/10> — FM app on as-built model (Dutch)

**openbimrs/ifc** (1 threads cited in the research; 1 shown)

- <https://github.com/openbimrs/ifc/issues/477> — COBie export feature spec

**pragmaticBIM/pragmaticBIM-reference** (1 threads cited in the research; 1 shown)

- <https://github.com/pragmaticBIM/pragmaticBIM-reference/issues/55> — issues

**SheetPros/OpenPermit** (1 threads cited in the research; 1 shown)

- <https://github.com/SheetPros/OpenPermit/issues/27> — permitting automation initiatives, title only

**specklesystems/speckle-sharp** (1 threads cited in the research; 1 shown)

- <https://github.com/specklesystems/speckle-sharp/issues/1778> — MVD-like property filter

**Stichting-CROW/imbor** (1 threads cited in the research; 1 shown)

- <https://github.com/Stichting-CROW/imbor/issues/1254> — NAA.K.T. in IMBOR

**SzamosiMate/tapir-archicad-MCP** (1 threads cited in the research; 1 shown)

- <https://github.com/SzamosiMate/tapir-archicad-MCP/issues/23> — duplicate elements on retry

**ThatOpen/platform_services** (1 threads cited in the research; 1 shown)

- <https://github.com/ThatOpen/platform_services/issues/27> — connectivity preserved in Fragments

**xBimTeam/Xbim.IDS.Validator** (1 threads cited in the research; 1 shown)

- <https://github.com/xBimTeam/Xbim.IDS.Validator/issues/11> — COBie facets for IDS

**youshengCode/IfcToolbox** (1 threads cited in the research; 1 shown)

- <https://github.com/youshengCode/IfcToolbox/issues/21> — issues

## Appendix C: articles, regional pages and vendor knowledge-base pages by language

Blog posts, regional official pages and vendor support articles cited by the research, grouped by language and site. These are the best places to learn how non-English speakers name things and which regulations they cite.

### Russian

**forum.dwg.ru** (24)

- <https://forum.dwg.ru/showthread.php?t=160240> — SAPFIR IFC export / AutoCAD import
- <https://forum.dwg.ru/showthread.php?t=153428> — Экспертиза проекта в Revit (2019)
- <https://forum.dwg.ru/showthread.php?t=107461> — architect/structural collaboration (ru)
- <https://forum.dwg.ru/showthread.php?t=154396> — Как корректно открыть IFC
- <https://forum.dwg.ru/showthread.php?t=166052> — Импорт IFC в Revit 2022
- <https://forum.dwg.ru/showthread.php?t=146029> — Tekla в Revit, тема 2018-2024
- <https://forum.dwg.ru/showthread.php?t=133669> — Revit to STARK ES
- <https://forum.dwg.ru/showthread.php?t=173570> — Plant 3D 2025 to IFC
- <https://forum.dwg.ru/showthread.php?t=126080> — Bocad IFC
- <https://forum.dwg.ru/showthread.php?t=149046> — Renga alternative opinions
- <https://forum.dwg.ru/showthread.php?t=76210> — ArchiCAD IFC to r2s
- <https://forum.dwg.ru/showthread.php?t=159943> — IFC import error Tekla (Cyrillic)
- <https://forum.dwg.ru/showthread.php?t=158006> — IFC into AutoCAD
- <https://forum.dwg.ru/showthread.php?t=163697> — Advance Steel to Archicad
- <https://forum.dwg.ru/showthread.php?t=155997> — Tekla columns in Revit
- <https://forum.dwg.ru/showthread.php?t=146367> — Tekla Field 3D IFC
- <https://forum.dwg.ru/showthread.php?t=96356> — IFC to DWG
- <https://forum.dwg.ru/showthread.php?page=2&t=150272> — Tekla BIMsight IFC
- <https://forum.dwg.ru/showthread.php?t=142967> — Revit to SCAD
- <https://forum.dwg.ru/showthread.php?t=33352> — ArchiCAD to analysis
- <https://forum.dwg.ru/showthread.php?t=75883> — ArchiCAD to DWG solid
- <https://forum.dwg.ru/showthread.php?t=159973> — SolidWorks to Revit
- <https://forum.dwg.ru/showthread.php?t=130296&page=2> — Edit IFC family
- <https://forum.dwg.ru/showthread.php?t=75685> — Resave ArchiCAD files

**dwg.ru** (1)

- <https://dwg.ru/b/utrfm/263> — Revit vs Tekla vs Allplan

**habr.com** (19)

- <https://habr.com/ru/articles/1089018/> — Два часа выгрузки ради пустого параметра
- <https://habr.com/ru/articles/1098340/> — AGR.Checker details, UDPS
- <https://habr.com/ru/articles/1100956/> — post-processing part 2 (areas, duplicates)
- <https://habr.com/ru/articles/1094224/> — IDS Core browser post-processing
- <https://habr.com/ru/articles/883016/> — IDS checking with ifcopenshell
- <https://habr.com/ru/articles/908192/> — Спецификация IDS
- <https://habr.com/ru/companies/pik_digital/articles/1057314/> — BIM Inspector (ПИК)
- <https://habr.com/ru/articles/1075736/> — плагин под Revit и АГР
- <https://habr.com/ru/articles/1087472/> — AGR.Checker changes
- <https://habr.com/ru/articles/882890/> — IFC associations by text editing
- <https://habr.com/ru/articles/1063062/> — parametric geometry in IFC4
- <https://habr.com/ru/articles/846382/> — building a BIM viewer, lessons
- <https://habr.com/ru/articles/759230/> — IFC.js viewer tutorial
- <https://habr.com/ru/articles/868186/> — data-centric BIM opinion
- <https://habr.com/ru/articles/860936/> — IFC vs USD opinion
- <https://habr.com/ru/articles/590819/comments/> — debate in comments
- <https://habr.com/ru/articles/460719/> — IFC introduction
- <https://habr.com/ru/articles/784224/> — IDS (snippet)
- <https://habr.com/ru/articles/1054266/> — BIMIT analysis (snippet)

**t.me** (5)

- <https://t.me/s/ifc_ru> — Всё про IFC
- <https://t.me/s/revithelper_kmv/146> — инструкция Свердловской области
- <https://t.me/s/bimlib_pro> — BIMLIB
- <https://t.me/s/prostobim?before=267> — Просто о BIM
- <https://t.me/s/bimacad?before=557> — Академия BIM

**sapr.ru** (1)

- <https://sapr.ru/article/25825> — nanoCAD СПДС и IFC из Revit

**blog.rengabim.com** (1)

- <https://blog.rengabim.com/2021/08/ifc.html> — Как принять IFC (Renga)

**rengabim.com** (1)

- <https://rengabim.com/stati/bol-she-10-formatov-eksporta-importa-v-renga-kakoj-iz-nih-vybrat/> — bol she 10 formatov eksporta importa v renga kakoj iz nih vybrat

**manual.rengabim.com** (1)

- <https://manual.rengabim.com/ehksport_atributov_obektov.html> — Renga attribute export

**youtube.com** (1)

- <https://www.youtube.com/watch?v=VPlQf3fv908> — Лекция: экспорт в IFC и IFC Viewers

**iek-digital.ru** (1)

- <https://iek-digital.ru/upload/iblock/685/4jzi0mt4ob86xb78imiswfg6dngrrots/Instruktsiya-po-eksportu-IFC-dlya-REVIT.pdf> — Instruktsiya po eksportu IFC dlya REVIT.pdf

**minstroyrf.gov.ru** (1)

- <https://minstroyrf.gov.ru/press/pervyy-proekt-polnostyu-sproektirovannyy-na-osnove-bim-tekhnologiy-proshel-gosekspertizu/> — pervyy proekt polnostyu sproektirovannyy na osnove bim tekhnologiy proshel gosekspertizu

### Chinese (mainland, Taiwan, Hong Kong)

**zhuanlan.zhihu.com** (18)

- <https://zhuanlan.zhihu.com/p/673078056> — SZ-IFC Revit dev
- <https://zhuanlan.zhihu.com/p/633827596> — Revit-side self-check
- <https://zhuanlan.zhihu.com/p/672903162> — self-check 1.3.0
- <https://zhuanlan.zhihu.com/p/504617257> — Guangzhou designers on BIM review
- <https://zhuanlan.zhihu.com/p/157220418> — Guangzhou BIM review notice
- <https://zhuanlan.zhihu.com/p/350723733> — ThreeJs轻量化浏览器 IFC
- <https://zhuanlan.zhihu.com/p/649792298> — what is IFC, mapping table
- <https://zhuanlan.zhihu.com/p/2025149945674474186> — Revit 2027 IFC property set UI
- <https://zhuanlan.zhihu.com/p/611709017> — Revit 2020 cannot export IFC
- <https://zhuanlan.zhihu.com/p/535737725> — Revit's five positioning points
- <https://zhuanlan.zhihu.com/p/2025170865478807871> — IFC格式是什么？用什么软件可以打开？
- <https://zhuanlan.zhihu.com/p/667304620> — IFC标准及格式介绍 (Common Language)
- <https://zhuanlan.zhihu.com/p/676069996> — 上海BIM智能辅助审查
- <https://zhuanlan.zhihu.com/p/602546350> — BIMSee免费IFC浏览器
- <https://zhuanlan.zhihu.com/p/662463406> — IDS信息交付规范
- <https://zhuanlan.zhihu.com/p/101268159> — Python解析IFC
- <https://zhuanlan.zhihu.com/p/2081844898991444652> — Revit接入大模型 (MCP)
- <https://zhuanlan.zhihu.com/p/2097988751914022344> — AI能否看懂图纸建BIM

**zhihu.com** (11)

- <https://www.zhihu.com/question/625548241> — Revit 2020 IFC GUID not generated
- <https://www.zhihu.com/question/49455994> — RVT vs IFC relationship, color differences
- <https://www.zhihu.com/question/527323998> — IFC是什么意思?
- <https://www.zhihu.com/question/264127961> — Revit导出IFC丢失哪些信息
- <https://www.zhihu.com/question/583830829> — IFC查看工具推荐
- <https://www.zhihu.com/question/455661969> — revit2019导出IFC没有反应
- <https://www.zhihu.com/question/418802002> — 修改revit导出IFC选项
- <https://www.zhihu.com/question/60173683> — tekla导出ifc到revit不显示
- <https://www.zhihu.com/question/30485422> — Tekla与Revit互转
- <https://www.zhihu.com/question/642487361> — 数维 vs BIMBase
- <https://www.zhihu.com/question/385964946> — BIM轻量化原理

**blog.csdn.net** (12)

- <https://blog.csdn.net/liuzk423/article/details/136849803> — IfcOpenShell to glTF code
- <https://blog.csdn.net/pumbkin/article/details/141029954> — React + web-ifc-three wasm LinkError
- <https://blog.csdn.net/qq_35042852/article/details/137257689> — Revit Chinese transcoding in IFC
- <https://blog.csdn.net/Kobayashiqaq/article/details/130361282> — XBIM element coordinates
- <https://blog.csdn.net/vcit102/article/details/135365455> — how IFC is rendered
- <https://blog.csdn.net/liyan_gis/article/details/100132931> — BIM to 3D Tiles positioning
- <https://blog.csdn.net/weixin_42855822/article/details/139867051> — Shenzhen filing FAQ
- <https://blog.csdn.net/qq_35187495/article/details/118198777> — details
- <https://blog.csdn.net/nihaozhe/article/details/108704151> — details
- <https://blog.csdn.net/niuge8905/article/details/104366954> — details
- <https://blog.csdn.net/liuzk423/article/details/136850936> — details
- <https://blog.csdn.net/zzutt/article/details/121492254> — IFC转Revit后减肥

**ask.csdn.net** (4)

- <https://ask.csdn.net/questions/3915684> — xBIM missing walls
- <https://ask.csdn.net/questions/8391346> — Revit opens IFC with missing/deformed elements
- <https://ask.csdn.net/questions/8816624> — move base point from 2000 coordinates to 0,0,0
- <https://ask.csdn.net/questions/8796533> — Max to Revit materials lost

**cnblogs.com** (13)

- <https://www.cnblogs.com/LeeSki/p/14293418.html> — IFC to DAE to glTF steps, Chinese-path caveat
- <https://www.cnblogs.com/nihaozhe/articles/13651935.html> — BIM lightweighting survey (Unity, WebGL, BIMserver)
- <https://www.cnblogs.com/SavionZhang/p/10984048.html> — xBIM IFC in browser via wexbim
- <https://www.cnblogs.com/SavionZhang/p/10983394.html> — xBIM spatial hierarchy
- <https://www.cnblogs.com/flowell/p/10838972.html> — Xbim.GLTF intro
- <https://www.cnblogs.com/herd/p/12183392.html> — modify IFC property and write back (Java)
- <https://www.cnblogs.com/liaocheng/p/15905467.html> — Revit category to IFC class mapping
- <https://www.cnblogs.com/pandaNHF/p/16828047.html> — reading a single wall in IFC text
- <https://www.cnblogs.com/herd/p/14908387.html> — slab property log from Revit IFC
- <https://www.cnblogs.com/lingyanspace/p/19739094> — read; IFC lightweight web viewer
- <https://www.cnblogs.com/OverloadBachPunk/p/14452654.html> — fix blank import by merging phases (read)
- <https://www.cnblogs.com/herd/p/15765322.html> — IfcBuildingElementProxy doc
- <https://www.cnblogs.com/w2011/p/8424405.html> — xBIM输出Excel

**juejin.cn** (2)

- <https://juejin.cn/post/7698926562423357450> — 2026 large BIM on web retrospective, pain list
- <https://juejin.cn/post/7691297274821705728> — 2026 Revit/IFC to Three.js pipeline with concrete pitfalls

**segmentfault.com** (2)

- <https://segmentfault.com/a/1190000047698784> — a
- <https://segmentfault.com/q/1010000008553854/a-1020000008763944> — RVT to SVF stuck at 35% (Chinese)

**gitee.com** (1)

- <https://gitee.com/xujunpro2/ifc-export> — domestic IFC lightweighting tool

**bilibili.com** (4)

- <https://www.bilibili.com/video/BV1Lx4y1L7P7/> — BlenderBIM Chinese tutorial
- <https://www.bilibili.com/video/BV1Ba41177xJ/> — Revit 2023 IFC export mapping dialog (read)
- <https://www.bilibili.com/read/cv18398331/> — Revit to FBX loses materials
- <https://www.bilibili.com/read/cv20354710/> — layer export settings

**zhidao.baidu.com** (3)

- <https://zhidao.baidu.com/question/341569640619976845.html> — IFC invisible in Revit, 7 causes (read)
- <https://zhidao.baidu.com/question/1755259387786621668.html> — multi-person base/survey point setup (read)
- <https://zhidao.baidu.com/question/593298625.html> — ArchiCAD pln to Revit

**bbs.zhulong.com** (1)

- <https://bbs.zhulong.com/106010_group_3002227/detail33178172/> — Revit plugin for BIM5D

**zhulong.com** (2)

- <https://www.zhulong.com/zt_bim_3002296/detail42826395/> — open newer RVT in older Revit via IFC2x3
- <https://www.zhulong.com/zt_bim_3002296/detail40283815/> — Revit MEP IFC into BIM5D

**jianshu.com** (2)

- <https://www.jianshu.com/p/76e051ccd5eb> — IFC export parameters, insertion point
- <https://www.jianshu.com/p/409188142cfa> — inconsistent base points

**bbs.co188.com** (1)

- <https://bbs.co188.com/thread-10112116-1-1.html> — read; Revit export loss

**sunyuanrui.com** (1)

- <https://www.sunyuanrui.com/works/sz-ifc-research/> — read; SZ-IFC pain points

**housegear.pixnet.net** (1)

- <https://housegear.pixnet.net/blog/posts/3042268210> — Taiwanese blog on importing IFC into Revit (2013)

**search.napstic.cn** (2)

- <https://search.napstic.cn/literature/periodical/010tmjzgcxxjs202401009> — BIMBase PModel paper
- <https://search.napstic.cn/literature/periodical/010tmjzgcxxjs202404016> — SZ-IFC QC paper

**autodesk.com.cn** (1)

- <https://www.autodesk.com.cn/support/technical/article/caas/sfdcarticles/sfdcarticles/CHS/Missing-elements-or-steel-connections-in-IFC-file-exported-from-Revit.html> — Missing elements or steel connections in IFC file exported from Revit

**gz.gov.cn** (1)

- <https://www.gz.gov.cn/xw/tzgg/content/post_6469259.html> — post 6469259

**zfcj.gz.gov.cn** (2)

- <https://zfcj.gz.gov.cn/gkmlpt/content/6/6434/post_6434530.html> — post 6434530
- <https://zfcj.gz.gov.cn/attachment/7/7943/7943479/10589336.pdf> — 10589336.pdf

**ghj.nanjing.gov.cn** (1)

- <http://ghj.nanjing.gov.cn/njsgtzyj/202103/t20210301_2834720.html> — t20210301 2834720

**amr.nanjing.gov.cn** (1)

- <https://amr.nanjing.gov.cn/ztzl/bzhzl/tzgg/202302/P020230216538033075572.pdf> — P020230216538033075572.pdf

**zjw.sh.gov.cn** (1)

- <https://zjw.sh.gov.cn/cmsres/4a/4a7bc95634cd4852b2399e57e9c692dd/a646541bab5ad86dc1684d1126e21e29.pdf> — a646541bab5ad86dc1684d1126e21e29.pdf

**bd.gov.hk** (1)

- <https://www.bd.gov.hk/tc/resources/online-tools/building-information-modelling/index.html> — BD BIM tools and policy

**devb.gov.hk** (1)

- <https://www.devb.gov.hk/filemanager/tc/content_2373/BIM-Book-content-cn.pdf> — roadmap booklet (cover only readable)

**careyourbuilding.bd.gov.hk** (1)

- <https://www.careyourbuilding.bd.gov.hk/ors/tc/event/307.html> — roadmap consultation event

**bim.cic.hk** (2)

- <https://www.bim.cic.hk/zh-hant/events/detail/304> — CIC Archicad/Revit IFC workshop
- <https://www.bim.cic.hk/zh-hant/resources/publications_detail/117> — CIC publications list (openBIM beginner's guide 2025)

**dbadgp.gov.taipei** (1)

- <https://dbadgp.gov.taipei/DownFiles/Login/使照竣工模型上繳操作手冊.pdf> — Taipei as-built upload

**bim.ntpc.gov.tw** (1)

- <https://www.bim.ntpc.gov.tw/Filedownload/新北市政府工務局BIM工作參考手冊108年版.pdf> — New Taipei manual

**etheses.lib.ntust.edu.tw** (1)

- <https://etheses.lib.ntust.edu.tw/thesis/detail/2e82ca6d84bfe5f839f58b35029a1d54> — NTUST thesis on permit rule checking

**tdr.lib.ntu.edu.tw** (1)

- <https://tdr.lib.ntu.edu.tw/handle/123456789/90111> — NTU thesis on IFC loss to analysis software

### Japanese

**qiita.com** (10)

- <https://qiita.com/kiyuka/items/0d2ef739a0d34606a52f> — IfcOpenShell 0.9 lazy loading benchmark (Japanese)
- <https://qiita.com/Takashi_Kasuya/items/97899d15e7ec0186eecf> — Revit UniqueId vs IFC GUID
- <https://qiita.com/KengoTanaka-BIM/items/6cec74e04bf581b21cf5> — IFC to Revit MEP conversion attempt
- <https://qiita.com/msp0310/items/0d7966a93ff380e11970> — 0d7966a93ff380e11970
- <https://qiita.com/ktaroabobon/items/25349c7fa7bdb55c63b8> — 25349c7fa7bdb55c63b8
- <https://qiita.com/dnp-hiraoka/items/aa1d12e5784485542583> — aa1d12e5784485542583
- <https://qiita.com/tosseto/items/34a2a801b8eb299453d1> — CityGML (Japanese)
- <https://qiita.com/masumur/items/8362a1ed91048e26ed2a> — PLATEAU CityGML to ArcGIS
- <https://qiita.com/kiyuka/items/00434f1b8e0b38c621fb> — Japanese FILE_SCHEMA
- <https://qiita.com/kiyuka/items/62e30208c035e828714b> — 62e30208c035e828714b

**zenn.dev** (14)

- <https://zenn.dev/miyamiyaumya/articles/19a4247133dde6> — IFC attributes/Psets/materials to Excel
- <https://zenn.dev/miyamiyaumya/articles/6714ef2c6e2c6c> — IDS explained
- <https://zenn.dev/miyamiyaumya/articles/909be24ee185ac> — IfcOpenShell install/usage
- <https://zenn.dev/cote2/articles/6459c1c44091da> — storeys with IfcOpenShell
- <https://zenn.dev/toggle_inc/articles/cf8df02f7b4ba7> — build IFC from scratch
- <https://zenn.dev/kiyuka/scraps/2894037aa4f997> — FlangeSlope question
- <https://zenn.dev/kiyuka/scraps/e07bf799384b52> — IFC Validation Service local
- <https://zenn.dev/kiyuka/scraps/48157a38db558e> — IFC relationship structure
- <https://zenn.dev/kiyuka/scraps/a054a249f42a93> — IFC to glTF
- <https://zenn.dev/grok_prtex/articles/webifc-version-compare> — web-ifc versions
- <https://zenn.dev/kazuyamaeda/articles/97933cdafce6d8> — browser IFC viewer
- <https://zenn.dev/tomosandego/articles/59e6cf8dfe60bc> — BIM ETL
- <https://zenn.dev/yuichi_ai/articles/879de49ee8e1bb> — Revit-MCP
- <https://zenn.dev/aec/articles/58aa31c1089332> — Claude Code Revit add-in

**note.com** (12)

- <https://note.com/toshio_nakamura/n/nc8db42ce3191> — half of the elements missing
- <https://note.com/kensesu_ai/n/nee08ddde31f1> — BIM図面審査 / データ審査
- <https://note.com/ken_newslab/n/n9d7072936346> — 2029 review overview
- <https://note.com/t_note_memo/n/n8903305b00fb> — one-room export test
- <https://note.com/legal_tiger6680/n/n6781ba815061> — BIMCraft and 2029
- <https://note.com/bim_tool_lab/n/nf529aa5d5cc0> — IFC not omnipotent
- <https://note.com/onestruction/n/ne8322e3be44d> — IFC expectation gaps
- <https://note.com/aei830/n/ndfa486486036> — BIM利用技術者
- <https://note.com/akram/n/n8a6e9c5602ca> — Bonsai in practice
- <https://note.com/limber_stork5044/n/n68df8d5a268b> — small MEP office
- <https://note.com/arent3d/n/nc9cf79adcb17> — Japan BIM drawing review
- <https://note.com/iu_bimstudio_n/n/nf41bb9e91025> — Archicad IFC output (JP)

**building-smart.or.jp** (1)

- <https://www.building-smart.or.jp/ifc/whatsifcverifi/> — IFC検定

### Korean

**buildingsmart.or.kr** (7)

- <https://www.buildingsmart.or.kr/Home/BimOverview> — BimOverview
- <https://www.buildingsmart.or.kr/Home/RnDCenter> — RnDCenter
- <https://www.buildingsmart.or.kr/Data/Main/BIM%20Guide_MLTL_Korea_2010.pdf> — BIM Guide MLTL Korea 2010.pdf
- <https://www.buildingsmart.or.kr/Data/Main/시설사업%20BIM%20적용%20기본지침서%20v2.0-S.pdf> — 시설사업 BIM 적용 기본지침서 v2.0 S.pdf
- <https://www.buildingsmart.or.kr/Home/NewsDetail?board=1&id=3446> — NewsDetail?board=1&id=3446
- <https://www.buildingsmart.or.kr/Home/NewsDetail?board=1&id=3451> — NewsDetail?board=1&id=3451
- <https://www.buildingsmart.or.kr/Home/Testinfo> — Testinfo

**kbims.or.kr** (1)

- <http://www.kbims.or.kr/> — www.kbims.or.kr

### German

**bim-me-up.com** (8)

- <https://bim-me-up.com/revit-ifc-und-koordinatensysteme/> — coordinates in Revit (2023)
- <https://bim-me-up.com/revit-typenparameter-nach-ifc-exportieren/> — type parameters (2023)
- <https://bim-me-up.com/ifc-5-eine-neue-hoffnung-fuer-interoperabilitaet/> — IFC 5 (2025)
- <https://bim-me-up.com/ifc-verlinken-vs-data-exchange-laden-in-revit/> — link vs Data Exchange (2025)
- <https://bim-me-up.com/ifc-struktur/> — spatial structure (2024)
- <https://bim-me-up.com/ifcbuildingstorey/> — storey assignment (2024)
- <https://bim-me-up.com/revit-phasen-nach-ifc-exportieren/> — phases (2023)
- <https://bim-me-up.com/die-popularsten-ifc-viewer/> — viewers (2020)

**bimdeutschland.de** (3)

- <https://www.bimdeutschland.de/bim-wissen/standards-normen-richtlinien/common-data-environment> — common data environment
- <https://www.bimdeutschland.de/bim-wissen/downloads> — downloads
- <https://www.bimdeutschland.de/bim-deutschland/faq> — faq

**bimpedia.de** (1)

- <https://www.bimpedia.de/artikel/16092-oeffnung-durchbruch-schlitz/> — 16092 oeffnung durchbruch schlitz

**bimpedia.eu** (1)

- <https://www.bimpedia.eu/articles/15926-ifc-export-from-archicad-to-revit-structure/> — translator settings guide

### Italian

**biblus.acca.it** (19)

- <https://biblus.acca.it/problemi-editing-file-ifc/> — common IFC editing problems
- <https://biblus.acca.it/ifc-vs-rvt-quali-sono-le-principali-differenze-tra-revit-e-ifc-in-termini-di-interoperabilita-e-scambio-dati/> — Revit vs IFC
- <https://biblus.acca.it/ifc-class-mapping-file/> — class mapping
- <https://biblus.acca.it/nuovo-codice-appalti-il-bim-e-obbligatorio/> — obbligo BIM guide (thresholds, dates)
- <https://biblus.acca.it/ifc-coordinate-system/> — coordinates
- <https://biblus.acca.it/capitolato-informativo-come-redigerlo-con-la-metodologia-bim/> — EIR
- <https://biblus.acca.it/come-creare-un-file-ifc/> — creating IFC
- <https://biblus.acca.it/bim-validation-modelli-ifc/> — validation
- <https://biblus.acca.it/rilevare-modifiche-nei-modelli-ifc/> — version diff
- <https://biblus.acca.it/linee-guida-bim-2026-per-le-stazioni-appaltanti/> — MIT 2026 guidelines
- <https://biblus.acca.it/conversione-modello-bim-in-ifc5/> — Revit export setup
- <https://biblus.acca.it/ifc-4-3-approvato-come-standard-finale/> — IFC 4.3
- <https://biblus.acca.it/ifc-2x3-coordination-view-2-0/> — Coordination View
- <https://biblus.acca.it/notizie/appalti-bim-lofferta-di-gestione-informativa-e-obbligatoria/> — oGI
- <https://biblus.acca.it/notizie/requisiti-bim-negli-rti-conta-il-professionista-o-il-gruppo-di-lavoro/> — RTI
- <https://biblus.acca.it/notizie/bim-maggiorazione-del-10-anche-per-direzione-lavori-e-cse/> — fees
- <https://biblus.acca.it/markups-bcf-workflow-openbim/> — BCF
- <https://biblus.acca.it/come-convertire-un-file-dwg-in-ifc-in-modo-semplice/> — DWG to IFC
- <https://biblus.acca.it/usbim-checker-verifica-informativa-del-modello/> — checker

**ingenio-web.it** (3)

- <https://www.ingenio-web.it/articoli/proprieta-ifc-muro-firerating-pset-wallcommon/> — Pset FireRating
- <https://www.ingenio-web.it/articoli/ifc-in-pratica-unita-di-misura-dove-trovarle-e-come-leggerle/> — units
- <https://www.ingenio-web.it/articoli/piano-casa-2026-edilizia-convenzionata-appalti-bim/> — Piano Casa and BIM

### Spanish / Portuguese

**planbim.cl** (4)

- <https://planbim.cl/> — Chile national BIM program
- <https://planbim.cl/ifc-y-actualizaciones/> — IFC 4.3/4.4 article
- <https://planbim.cl/documentos/fichas-ifc/> — IFC entity sheets (seen in search; direct fetch returned 404)
- <https://planbim.cl/documentos/mide/> — MIDE matrix (search only; fetch 404)

**repositorio.uchile.cl** (1)

- <https://repositorio.uchile.cl/handle/2250/179170> — thesis on Planbim standard

**mef.gob.pe** (2)

- <https://www.mef.gob.pe/planbimperu/docs/planBIMpE.pdf> — Plan BIM Perú
- <https://www.mef.gob.pe/contenidos/inv_publica/docs/capacitaciones/2026/20260317.pdf> — MEF 2026 training

**elperuano.pe** (1)

- <https://www.elperuano.pe/noticia/213920-avance-de-la-implementacion-del-building-information-modeling-en-america-latina> — LatAm BIM status

**bim.minvivienda.gov.co** (1)

- <https://bim.minvivienda.gov.co/sites/default/files/doc-bim-2022-09/10_licencias_.pdf> — Colombia BIM doc

**espaciobim.com** (3)

- <https://www.espaciobim.com/ifc> — ifc
- <https://www.espaciobim.com/bimvision> — bimvision
- <https://www.espaciobim.com/ifc-builder> — ifc builder

**e-zigurat.com** (1)

- <https://www.e-zigurat.com/es/blog/ifc-e-interoperabilidad-en-bim/> — ifc e interoperabilidad en bim

**bimnd.es** (1)

- <https://www.bimnd.es/blog/10-consejos-para-exportar-un-buen-ifc-con-revit/> — 10 consejos para exportar un buen ifc con revit

**construible.es** (2)

- <https://www.construible.es/2023/05/02/mitma-aprueba-propuesta-plan-implantacion-bim-contratacion-publica> — mitma aprueba propuesta plan implantacion bim contratacion publica
- <https://www.construible.es/2023/08/02/ayudas-para-la-formacion-bim-aplicada-a-la-contratacion-publica-para-los-colegios-profesionales> — ayudas para la formacion bim aplicada a la contratacion publica para los colegios profesionales

**esmartcity.es** (1)

- <https://www.esmartcity.es/2023/06/30/plan-bim-incorporara-metodologia-bim-contratos-publicos-construccion> — plan bim incorporara metodologia bim contratos publicos construccion

**interempresas.net** (1)

- <https://www.interempresas.net/ObrasPublicas/565188-BIM-la-tecnologia-capaz-de-revolucionar-la-Ingenieria-del-Terreno.html> — 565188 BIM la tecnologia capaz de revolucionar la Ingenieria del Terreno

**hacienda.gob.es** (1)

- <https://www.hacienda.gob.es/DGPatrimonio/Junta%20Consultiva/informes/informes2023/2023-23-MTMAU-BIM.pdf> — 2023 23 MTMAU BIM.pdf

**obcp.es** (1)

- <https://obcp.es/opiniones/la-implementacion-de-la-metodologia-bim-en-la-contratacion-publica> — la implementacion de la metodologia bim en la contratacion publica

**public-buyers-community.ec.europa.eu** (1)

- <https://public-buyers-community.ec.europa.eu/system/files/2024-05/AIDA%20240322_GabSUB_DGGROWPPUnit_PlanBIM_en_v1_0.pdf> — AIDA 240322 GabSUB DGGROWPPUnit PlanBIM en v1 0.pdf

**emea.support.arkance.world** (1)

- <https://emea.support.arkance.world/hc/es/articles/36464850969234-Using-IFC-files-with-a-Shared-Coordinates-system> — 36464850969234 Using IFC files with a Shared Coordinates system

**help.graphisoft.com** (2)

- <https://help.graphisoft.com/AC/28/SPA/_AC28_Help/121_IFC/121_IFC-1.htm> — Spanish IFC help
- <https://help.graphisoft.com/AC/29/TAI/_AC29_Help/121_IFC/121_IFC-1.htm> — Archicad IFC help in Traditional Chinese

**help.fieldsystems.trimble.com** (1)

- <https://help.fieldsystems.trimble.com/trimble-access/2021.20/es/Map-files-BIM-and-IFC.htm> — IFC in the field

### French

**kroqi.fr** (1)

- <https://www.kroqi.fr/> — official product page, IFC/BCF mention

**kb.kroqi.fr** (1)

- <https://kb.kroqi.fr/base-de-connaissance-kroqi> — KB index; no IFC article located

**faq.bimandco.com** (1)

- <https://faq.bimandco.com/en/> — FAQ index, no IFC

**ge.ch** (1)

- <https://www.ge.ch/utiliser-bim-building-information-modeling/je-prepare-maquette-bim-autorisation-construire> — Geneva permit

### Dutch

**digigo.nu** (12)

- <https://www.digigo.nu/ilsen-en-richtlijnen/bim-basis-ils/> — BIM basis ILS overview
- <https://www.digigo.nu/ilsen-en-richtlijnen/bim-basis-ils/handleidingen/> — per-software manuals, Solibri/BIMcollab check guides
- <https://www.digigo.nu/ilsen-en-richtlijnen/bim-basis-ils/downloads/> — infographics, multilingual
- <https://www.digigo.nu/ilsen-en-richtlijnen/bim-basis-ils/3-4-correct-gebruik-entiteiten> — proxy and TypeEnumeration
- <https://www.digigo.nu/ilsen-en-richtlijnen/bim-basis-ils/3-3-bouwlaagindeling-en-naamgeving> — 3 3 bouwlaagindeling en naamgeving
- <https://www.digigo.nu/ilsen-en-richtlijnen/bim-basis-ils/3-2-lokale-positie> — 3 2 lokale positie
- <https://www.digigo.nu/ilsen-en-richtlijnen/bim-basis-ils/3-7-gebruik-propertysets> — 3 7 gebruik propertysets
- <https://www.digigo.nu/ilsen-en-richtlijnen/bim-basis-ils/4-1-ruimten> — 4 1 ruimten
- <https://www.digigo.nu/ilsen-en-richtlijnen/bim-basis-ils/4-7-materiaal> — 4 7 materiaal
- <https://www.digigo.nu/ilsen-en-richtlijnen/bim-basis-ils/praktijk/1-naa-k-t-eenduidige-materiaalbenaming> — 1 naa k t eenduidige materiaalbenaming
- <https://www.digigo.nu/ilsen-en-richtlijnen/bim-basis-ils/2-hoe-we-informatie-uitwisselen> — 2 hoe we informatie uitwisselen
- <https://www.digigo.nu/standaarden/nlsfb/> — nlsfb

### Norwegian

**buildingsmart.no** (7)

- <https://www.buildingsmart.no/standarder/kort-forklart.html> — IFC, IDS, BCF, bSDD, NS 8360, 19650 glossary
- <https://www.buildingsmart.no/pofin.html> — pofin
- <https://www.buildingsmart.no/standarder/publikasjoner-og-veiledninger.html> — publikasjoner og veiledninger
- <https://www.buildingsmart.no/standarder/standardiseringsarbeid.html> — standardiseringsarbeid
- <https://www.buildingsmart.no/fagnettverk/infradomene.html> — infradomene
- <https://www.buildingsmart.no/fagnettverk/bimpraten.html> — bimpraten
- <https://www.buildingsmart.no/fagnettverk/ressurser.html> — ressurser

**mmi-veilederen.no** (1)

- <https://www.mmi-veilederen.no/> — www.mmi veilederen.no

**bimpraten.no** (1)

- <https://www.bimpraten.no/> — www.bimpraten.no

**nyeveier.no** (1)

- <https://www.nyeveier.no/for-leverandoerene/> — for leverandoerene

### English blogs, vendor knowledge bases and others

**bimcorner.com** (15)

- <https://bimcorner.com/same-bridge-three-ifc-files/> — three bridge exports compared (2026)
- <https://bimcorner.com/ai-ifc-properties/> — AI invents psets (2026)
- <https://bimcorner.com/what-is-an-ifc-concept/> — IFC 4.3 concepts (2026)
- <https://bimcorner.com/is-the-industry-ready-for-ifc4/> — IFC4 test results (2022)
- <https://bimcorner.com/10-common-ifc-export-mistakes-to-avoid-part-1/> — mistakes 1-5 (2021)
- <https://bimcorner.com/10-common-ifc-export-mistakes-to-avoid-part-2/> — mistakes 6-10 (2021)
- <https://bimcorner.com/ifc-export-rules-part-2-what-parameters-to-export-dos-and-donts/> — dos and don'ts
- <https://bimcorner.com/what-i-dont-like-about-ifc/> — complaints (2020)
- <https://bimcorner.com/super-ifc/> — what a good IFC looks like (2024)
- <https://bimcorner.com/exporting-ifc-from-revit-part-1-mapping/> — IfcExportAs (2021)
- <https://bimcorner.com/exporting-ifc-from-archicad/> — ArchiCAD pain points (2021)
- <https://bimcorner.com/export-a-tekla-structures-model-to-an-ifc-file/> — Tekla (2021)
- <https://bimcorner.com/model-validation-as-a-key-step-in-the-bim-workflow/> — IDS and Solibri (2024)
- <https://bimcorner.com/use-ai-to-manipulate-your-ifc/> — ChatGPT with IfcOpenShell (2024)
- <https://bimcorner.com/analyzing-ifc-files/> — inspecting raw IFC (2024)

**helpcenter.bimcollab.com** (5)

- <https://helpcenter.bimcollab.com/en/articles/341453-solibri-bcf-live-connector-tips-and-troubleshooting> — 341453 solibri bcf live connector tips and troubleshooting
- <https://helpcenter.bimcollab.com/en/articles/340730-why-is-issue-status-in-solibri-changed-after-synchronization-to-bimcollab> — 340730 why is issue status in solibri changed after synchronization to bimcollab
- <https://helpcenter.bimcollab.com/en/articles/341451-why-are-viewpoint-components-missing-after-an-import> — 341451 why are viewpoint components missing after an import
- <https://helpcenter.bimcollab.com/en/articles/341452-why-don-t-i-see-selected-colored-components-in-other-bim-tools> — 341452 why don t i see selected colored components in other bim tools
- <https://helpcenter.bimcollab.com/en/collections/714834-integrations-and-desktop-apps> — 714834 integrations and desktop apps

**support.tekla.com** (4)

- <https://support.tekla.com/doc/tekla-structures/2024/int_ifc_export> — int ifc export
- <https://support.tekla.com/doc/tekla-structures/2024/int_exporting_into_ifc> — int exporting into ifc
- <https://support.tekla.com/doc/tekla-structures/2024/int_checking_exported_ifc_model> — int checking exported ifc model
- <https://support.tekla.com/doc/tekla-structures/2024/int_defining_property_sets_using_property_set_definitions> — int defining property sets using property set definitions

**support.drofus.com** (1)

- <https://support.drofus.com/en/support/solutions/articles/16000118323-optimal-settings-for-ifc-export-from-revit> — 16000118323 optimal settings for ifc export from revit

**help.autodesk.com** (1)

- <https://help.autodesk.com/view/RVT/2025/ENU/?caas=caas%2Fsfdcarticles%2Fsfdcarticles%2FCertain-shared-parameters-not-exportetd-to-IFC-from-Revit.html> — official KB on missing shared parameters

**docs.thatopen.com** (1)

- <https://docs.thatopen.com/Tutorials/Components/Core/IfcLoader> — official IfcLoader tutorial

**novedge.com** (1)

- <https://novedge.com/blogs/design-news/revit-tip-revit-ifc-export-configuration-and-quality-control> — export QC tips

**info.corenet.gov.sg** (3)

- <https://info.corenet.gov.sg/> — official hub, IFC+SG sections
- <https://info.corenet.gov.sg/ifc-sg/model-setup-and-coordination> — Singapore model quality
- <https://info.corenet.gov.sg/general/corenet-x.aspx> — CORENET X portal

**imiframework.org** (1)

- <https://imiframework.org/> — UK ISO 19650 hub

**cidb.org.za** (2)

- <https://www.cidb.org.za/innovation/cidb-bim-adoption-strategy/> — official strategy, South Africa
- <https://www.cidb.org.za/resource-centre/downloads-2/> — cidb downloads, not opened

**hub.dm.gov.ae** (1)

- <https://hub.dm.gov.ae/link/service> — Dubai Municipality services hub, not opened

**fhwa.dot.gov** (1)

- <https://www.fhwa.dot.gov/bridge/pubs/hif21031.pdf> — Utah demonstration

**paconstructors.org** (1)

- <https://www.paconstructors.org/news/first-contractual-ifc-model-delivered-nationally/> — first contractual ifc model delivered nationally

**pooledfund.org** (1)

- <https://pooledfund.org/Details/Study/1798> — Study

**nibs.org** (1)

- <https://nibs.org/nbims/v3/cobie/> — cobie
