# Australia, New Zealand, India and South Asia: BIM/IFC requirements

## In plain words

None of these countries has a single national law that says "deliver your building model as an IFC file". What exists is a patchwork. In Australia the rules are set by individual states and agencies (Transport for NSW, Queensland, Victoria) plus industry guides (NATSPEC). New Zealand has a government procurement guideline plus an industry handbook. India has government guidelines (CPWD) and strong but mostly unofficial claims about "mandates". Pakistan, Bangladesh, Sri Lanka and Nepal have academic discussion of BIM but, as far as this research could verify, no official BIM or IFC mandates.

For a tester this means: IFC requests in these markets are usually "IFC 2x3 or higher alongside native files", plus ISO 19650-style information management, plus local coordinate systems (GDA2020/MGA2020 in Australia, NZTM2000 in New Zealand). Do not expect a national checking portal or a national IFC property-set standard. Many claims found online (especially for India) are blog-level and conflict with each other; this document labels them.

Last researched: 2026-11-06

Research limits: the web-search quota was exhausted partway through the session, and many government PDFs (Transport for NSW, Queensland, NZ procurement, Victoria, PIB) returned HTTP 403 or unreadable binary. Where the content comes only from search-result snippets, it is marked "(snippet only)". Sri Lanka, Nepal and Pakistan are therefore thin (see Gaps).

---

## 1. Overview table

| Country | Level of official BIM/IFC requirement | Main documents | IFC-specific? |
|---|---|---|---|
| Australia (federal) | Policy framework and recommendations only; no federal IFC mandate found | Australian BIM Strategic Framework (ABAB, 2019); Infrastructure Australia plan 2021 | No |
| Australia: NSW (Transport for NSW) | Contractual standards for TfNSW Digital Engineering projects | Digital Engineering Standard Part 1 (DMS-ST-202 v4.1), Part 2 Requirements (DMS-ST-207 v4.1), Framework (DMS-ST-208) | Yes: IFC 2x3 or higher for survey models |
| Australia: Queensland | Principles for BIM implementation (policy) + non-mandated data guideline | Digital Enablement for Queensland Infrastructure, Principles for BIM Implementation; BIM projects data and information guideline v1.0.1 | Yes: native + IFC 2X3 at minimum ("should") |
| Australia: Victoria | Digital Asset Policy for agencies | Digital Asset Policy (2021); Victorian Digital Asset Strategy (March 2020) | Not verified |
| Australia: councils/utilities | Asset data handover | ADAC XML (IPWEA), v5.01 widely cited | No (own XML schema, not IFC) |
| New Zealand | Government guideline + industry handbook | MBIE BIM Construction Procurement Guidelines; NZ BIM Handbook (2023 edition) | Handbook page does not mention IFC |
| India | Guidelines and policy encouragement; mandate claims unverified | CPWD "Introducing BIM in CPWD" (2019 per secondary sources); Economic Survey 2023-24 | No official IFC requirement found |
| Pakistan, Bangladesh, Sri Lanka, Nepal | No official mandate verified | Academic papers only | No |

---

## 2. Australia

### 2.1 National level

- **Australian BIM Strategic Framework** was published by the Australasian BIM Advisory Board (ABAB) in 2019 and tied to the National Digital Engineering Policy Principles, which the Transport and Infrastructure Council endorsed in 2016 as a step towards national adoption [1][2]. It is a framework, not a regulation (snippet only; the PDF itself could not be fetched).
- **Infrastructure Australia, Australian Infrastructure Plan 2021** proposed that all federally funded infrastructure incorporate a digital twin within 10-15 years, digitalisation (including BIM) of all major infrastructure projects within 5 years, "digital asset champion" roles for projects over $50 million, and a national office for digital-by-default infrastructure. These are recommendations, not law [3].
- **AS ISO 19650** is adopted by Standards Australia as identical adoptions: AS ISO 19650.1:2019 (= ISO 19650-1:2018), AS ISO 19650.3:2021, AS ISO 19650.5:2021; committee BD-104 [4] (snippet only). "AS 7739" appeared in a search result as a RISSB document ("AS 7739.1 Digital Engineering") for rail; its content was not verified [5].
- **buildingSMART Australasia** became a Full Chapter of buildingSMART International on 29 April 2025 (together with Portugal) [6]. It runs the XChange conference series and the pCert professional certification program [7]. Its site mentions no national IFC mandate [7].

### 2.2 NATSPEC (industry guidance, not law)

- **NATSPEC National BIM Guide, October 2022 edition**, aligned with AS ISO 19650. The core Guide is aimed at executives and managers; technical detail moved to appendices. Documents: Appendix A Glossary, B AS ISO 19650 Resource Descriptions, C BIM Use and Enabler Descriptions, D Defining Information Requirements; templates for BIM Execution Plan (BEP), Project BIM Brief, AIR, PIR and EIR [8]. A NATSPEC index dated April 2026 still lists it as current [9] (snippet only).
- **Open BIM Object Standard (OBOS)**, version 1.0, 2018, published jointly by NATSPEC (Australia) and Masterspec (NZ). Built on IFC4: every object carries IFC4 properties; two properties, `IfcExportAs` and `IfcExportType`, tag the IFC entity and predefined type; if nothing fits, use `IfcBuildingElementProxy` with USERDEFINED and an `ElementType` property; property sets use prefixes such as `OBOS_`, `COBie_`, `ANZRS_` (expansion of ANZRS not verified); IFC sets keep `Pset_`/`Qto_` names [10]. Practical consequence for testers: a Revit family from an Australian manufacturer may carry `IfcExportAs` and should export to the intended IFC class.
- Other NATSPEC tools named on the NATSPEC BIM site: BIM Properties Generator, BIM Value Tool, Keynoting Framework, Classification and Filing tools, and an Excel version of a "National Classification" for the Autodesk Classification Import Template [8][9] (snippet only).

### 2.3 Transport for NSW (TfNSW)

The strongest IFC-specific requirement set in Australia is in TfNSW's Digital Engineering suite (all snippet only; the PDFs returned 403):

| Document | Number / version | Note |
|---|---|---|
| Digital Engineering Standard Part 1: Concepts and principles | DMS-ST-202, v4.1, December 2022, next review December 2024 | [11] |
| Digital Engineering Standard Part 2: Requirements | referred to as DMS-ST-207, v4.1 (2022) | The document numbers 207 and 208 are mixed in TfNSW material; Part 2 = 207, Framework = 208 per TfNSW's own guides [12][13] |
| Digital Engineering Framework | DMS-ST-208; v3.0 (2019), v4.0 (2022) | Lists IFC 3D model reviews as a review activity [14][15] |
| Digital Engineering Survey Requirements Guide | DMS-SD-142 (2024) | IFC files submitted as individual files in **IFC 2x3 or higher**, newer versions allowed if TfNSW approves; Part 2 governs on conflict [16] |
| Setting up for BIM | v3.1 (2023) | Says IFC suits small projects needing efficient federated models [17] |

A buildingSMART Australasia-contributed document states IFC requirements are included by TfNSW [12]. Exact IFC clause numbers could not be read; do not quote clause numbers.

### 2.4 Queensland

- **Digital Enablement for Queensland Infrastructure, Principles for BIM Implementation** (Department of State Development, Infrastructure, Local Government and Planning lineage; lead agency name varies by year, so check). Applies to government departments, agencies and statutory authorities; the principles reference major projects, including those of $50 million or more. Direction: Queensland will use an **Open BIM** approach (open, interoperable, archivable data standards); ISO 19650-1 and -2 were to be followed by the supply chain from 1 July 2019. The 2022 State Infrastructure Strategy committed to a review [18][19] (snippet only).
- **BIM projects - data and information guideline** (Queensland Government Enterprise Architecture, QGEA), Final v1.0.1, effective July 2020, **non-mandated** ("should") [20]. Key content (read directly from the page):
  - Deliver native format and **buildingSMART IFC 2X3** at a minimum; IFC is not parametric, so native files are needed for future redevelopment.
  - Classification: metadata/asset classification based on or mappable to **Uniclass 2015**; building agencies use the **Virtual Buildings Information System (VBIS)** schema with VBIS tags; ISO 12006-2 for classification, ISO 12006-3 for object information.
  - Georeferencing: **GDA2020**, lat/long or **MGA2020** (eastings, northings, zone); heights in **AHD**; record the choice in model metadata.
  - Level of development: **LOD300** recommended unless specified otherwise.
  - Container states per ISO 19650-1: Work in progress, Shared, Published. Date format dd/mm/yyyy. Discipline codes such as ST, ME, EP.
  - Security: classify under IS18 and the QGISCF; manage as asset under IS44.
- **Queensland Transport and Main Roads (TMR)** publishes "A guide to enabling BIM on Road Infrastructure Projects" (BIM guideline PDF) [21]; content could not be read. Search results said TMR committed to being digital by default by 2032 and has adopted IFC (snippet only, from a vendor/third-party summary).

### 2.5 Victoria

- **Victorian Digital Asset Strategy (VDAS)**, March 2020, and **Digital Asset Policy** (2021, Office of Projects Victoria, with Department of Treasury and Finance hosting). Applies to departments and bodies under the Financial Management Act 1994; business case required for investments with Total Estimated Investment of $10 million or more; requirements scaled to project value and risk [22][23]. No IFC clause verified.

### 2.6 ADAC (civil asset data, not IFC)

**ADAC = Asset Design and As Constructed**, an XML data standard developed by IPWEA (Queensland) for local government and water utilities. Councils require designers and surveyors to submit asset data as ADAC XML at handover. Logan City Council states the current version is **5.01**; for operational works approved from 1 July 2024 compliant 5.01 XML is required for all asset classes (transport, stormwater, open space, water supply, sewerage); exemptions for 50 m or less of water/sewer/stormwater, or 4 or fewer lots; water/sewer files also need the SEQ Code Asset Information Specification [24]. Ipswich cites 5.0.1 for developments approved after 1 July 2021 [25]. An ADAC "Version 6" launch was reported in 2024 (details not verified) [25]. FME has ADAC reader/writer support [26]. Important: ADAC is not IFC; a request to "convert IFC to ADAC" is a data-mapping task, not a format export.

---

## 3. New Zealand

- **NZ BIM Handbook, 2023 Fourth Edition** (A guide to enabling Building Information Modelling for the built environment), part of the "Digital Guidance Suite 2023". Funded by the Construction Sector Accord, expert input from the BIMinNZ Steering Group, project-managed by the NZ Institute of Building. Appendices: A Modelling and documentation best practice; B Model coordination and issue tracking; C LOD definitions and notations; D 21 defined BIM Uses; E alignment of NZ project phases with ISO 19650-2 and procurement methods; F EIR template; G Model element author and LOD schedule; H BIM evaluation and response template for RFPs; J BIM Execution Plan; K Model Description Document. The page does not mention IFC; ISO 19650 appears in Appendix E [27].
- Earlier editions: 2nd edition 2016; 3rd edition April/May 2019 published by the BIM Acceleration Committee, funded by BRANZ levy, referencing ISO 19650-1/-2 [28][29].
- **MBIE Building Information Modelling (BIM) Construction Procurement Guidelines**, v2.0 October 2019 (snippet only): agencies "must adopt" BIM for design, construction and maintenance in line with the NZ BIM Handbook; at minimum prepare a project BIM brief. The Government Procurement Rules 4th edition (in force 1 October 2019) changed construction procurement (Rules 18, 64, 69); a 5th edition ("Responsible expenditure of public funds") appeared in 2025, and whether it altered BIM provisions was not checked [30][31][32]. The globalbim entry calls the guidelines guidance, not mandatory; the procurement document is described as "live" [33].
- **Building consents**: no national IFC-based e-consent standard found. An Auckland University proof of concept with a consent authority produced minimum data requirements for BIM submissions [34]. Christchurch City Council has BIM implementation guidelines referencing ISO 19650 (content unreadable) [35]. Platforms (Simpli, Objective Build, AlphaOne) are vendor systems whose IFC acceptance is unknown [36].
- **Masterspec** (Construction Information Ltd, Auckland) is NATSPEC's NZ counterpart and co-publisher of OBOS [10].
- **Georeferencing** (general knowledge, not from a fetched NZ source): New Zealand Transverse Mercator NZTM2000 (EPSG:2193) on NZGD2000 (EPSG:4167). Verify project-specific requirements.

---

## 4. India

### 4.1 What is verifiable

- **Economic Survey 2023-24** (tabled July 2024) has a section on adopting BIM to reduce project delays and cost. It says BIM is extensively used by some ministries and departments (NCRTC, metro rails, airports, CPWD), that **NITI Aayog** identified challenges, solutions and enablers and has a roadmap for faster BIM adoption, and that guidance is given to projects such as Central Vista and the New Parliament. Quoted benefit figures (e.g. up to 30% construction cost reduction) are claimed potential. A news summary does not mention any BIM mandate [37][38] (PIB page itself returned 403).
- **CPWD technical publication "Introducing BIM in CPWD"** is listed among eight publications released at CPWD's 170th anniversary (PIB) [39] (snippet only). Secondary sources say CPWD BIM guidelines date from 2019 and cover BIM execution plan, common data environment and COBie handover; these claims come from blogs [40][41].
- **IIT Palakkad MoU with MoHUA and CPWD** (PIB release) makes IIT Palakkad a National Centre of Excellence for BIM training and digital transformation (five-year collaboration; curriculum, certification, research); a related release says a National BIM and Digital Project Delivery training programme started with CPWD engineers [39][42] (snippets; dates not verified).
- **BIS**: a 2026 third-party snapshot says BIS has published no Indian Standard on BIM and that projects reference ISO 19650 directly [43]. This was not confirmed on bis.gov.in (unverified). The National Building Code of India (NBC 2016, BIS) is the general building regulation; no BIM clause was verified.
- **buildingSMART India**: the Confederation of Digital Construction Practitioners India (CDCPIndia, founded 2020) was approved as a **Developing Chapter** of buildingSMART International at the June 2023 conference in Slovenia (press release coverage) [44][45]. A 2025 press item says the chapter endorses pCert as national competency standard (snippet only) [44]. NITI Aayog reportedly evaluated a Gati Shakti-like common data platform (snippet) [46].

### 4.2 Conflicting, unverified mandate claims

| Claim | Where | Status |
|---|---|---|
| CPWD requires BIM above Rs 20 crore (2024) | blogs, one citing an office memorandum of 14 Nov 2023 | (unverified) |
| CPWD requires BIM above Rs 100 crore | EPC World article (17 Jul 2025), no primary source | (unverified) [40] |
| CPWD mandate for Rs 50 crore+ projects from April 2026 | YouTube short | (unverified) |
| MoHUA mandates BIM above Rs 500 crore (central projects) | Studio Matrx, blog | (unverified) |
| NHAI requires BIM / BIM deliverables in tenders | blogs | (unverified); no NHAI circular found in a search of policy circulars |
| National BIM platform under development | EPC World | proposed, not in force |
| No national mandate, no BIS BIM standard | infralens.in 2026 snapshot | secondary but consistent with the primary sources above |

Rule for test authors: do not assert a specific rupee threshold as fact. If a model answers with "Rs 20 crore", the correct evaluation is "plausible claim in blogs, not verified in a primary document".

### 4.3 IFC in India

No official IFC version, MVD or property set requirement was found. Practice follows project contracts (metro rails, airports, EPC contractors) that typically reference ISO 19650-style EIR/BEP and request native files plus IFC/COBie (EPC World says IFC and COBie are poorly known outside Tier 1 cities) [40]. Classification: none national for BIM; people use Uniclass 2015, OmniClass or CPWD/DSR item codes (general knowledge, unverified for BIM use). Georeferencing: Survey of India grids, UTM zones or local grids vary by project (general knowledge).

---

## 5. Pakistan, Bangladesh, Sri Lanka, Nepal

| Country | Finding | Evidence |
|---|---|---|
| Pakistan | No PEC BIM guideline and no NHA BIM mandate found. NHA uses FIDIC forms. PEC endorsed BIM events (2015 NED University workshop). PEC has adopted green and energy codes as bye-laws (not BIM). CDA Islamabad made NEECA energy conservation building codes mandatory (Sept 2025), unrelated to BIM. Academic papers describe very low BIM use and a shortage of professionals | [47][48][49] |
| Bangladesh | No PWD/RAJUK BIM guideline or mandate found. A 2026 paper (American Journal of Civil Engineering and Constructions, Vol. 2 No. 2) says adoption is limited by cost, skills, interoperability and culture and recommends government mandates and open standards (IFC, ISO 19650) | [50] |
| Sri Lanka | No result on a BIM policy from CIDA or other bodies; search returned only ICT-sector material | gap |
| Nepal | Search budget exhausted before this query | gap |

Treat any claim like "Bangladesh mandates BIM" or "Sri Lanka requires IFC" as unverified. No buildingSMART chapter in these four countries was confirmed (not verified either way).

---

## 6. IFC technical notes for testing in this region (general knowledge)

These are standard buildingSMART facts, not region-specific findings; they are labelled general knowledge.

- IFC 2x3 (Coordination View 2.0) is the lowest common denominator named by Queensland and TfNSW; IFC4 Reference View / Design Transfer View and IFC4.3 (ISO 16739-1:2024) are newer. A request for "IFC 2x3 or higher" is satisfied by IFC4 export.
- IFC 2x3 has no native `IfcMapConversion`/`IfcProjectedCRS`; those are IFC4. For GDA2020 / MGA2020 zones the common EPSG codes are 7844 (geographic), 7854/7855/7856 (MGA zones 54/55/56); AHD is EPSG:5711; NZTM2000 is 2193. Verify codes against the EPSG registry before using.
- Revit IFC export: File > Export > IFC; the export setup includes IFC version, file type, Project Base Point/Shared Coordinates site placement, and property set options. When a TfNSW-style requirement says "IFC 2x3 or higher with shared coordinates", test that the exported file's site placement matches the survey coordinates.
- Tools useful for checking: IfcOpenShell (LGPL/GPL; supports IFC2x3, IFC4, IFC4.1, IFC4.2, IFC4.3; IfcTester for IDS audits; IfcClash; IfcDiff), Bonsai add-on for Blender [51]. buildingSMART IDS (Information Delivery Specification) and the bSDD are the modern route to machine-checkable requirements (general knowledge).

---

## 7. Key organizations

| Organization | Role | Source |
|---|---|---|
| buildingSMART Australasia | Full Chapter since 29 April 2025; XChange conference; pCert | [6][7] |
| NATSPEC / Masterspec | National BIM Guide, OBOS, classification and properties tools | [8][10] |
| Australasian BIM Advisory Board (ABAB) | Published the strategic framework (2019) | [1][2] |
| Standards Australia (BD-104) | AS ISO 19650 parts | [4] |
| IPWEA (Queensland) | ADAC | [24] |
| BIMinNZ / NZ Institute of Building | NZ BIM Handbook, Digital Guidance Suite | [27] |
| Construction Sector Accord, MBIE | NZ funding and government procurement guidance | [27][30] |
| BRANZ | Funded earlier handbook edition | [28] |
| CDCPIndia (buildingSMART India, Developing Chapter) | Indian chapter, pCert | [44][45] |
| CPWD, MoHUA, NITI Aayog, IIT Palakkad | Government and training bodies in India | [37][39][42] |
| RISSB | Rail standards incl. "AS 7739" digital engineering (unverified content) | [5] |

---

## 8. Software ecosystem and enthusiasts

- **Commercial** (vendor presence is general knowledge, not region-verified here): Autodesk Revit and Civil 3D, Graphisoft Archicad, Bentley, Tekla, Trimble; Australian civil package 12d Model (12d Synergy appears in search results) [52].
- **Open-source/enthusiast** (labelled community): IfcOpenShell and Bonsai; IfcOpenShell's project founders include Australian contributors (personal detail omitted) [51]. FME (Safe Software) has an ADAC reader/writer [26].
- **Community resources**: Google Sites mirror of BIM standards "plbimcom" [53] and the globalbim.org Collaborative Framework library [33] list national documents; these are aggregators, not authorities.
- **Training/vendors in India** (commercial, promotional): Novatr, Studio Matrx, ArchGyan, InfraLens blogs; usable for orientation only [40][41][43].

---

## 9. Local terminology

| Native term | Transliteration | English | Note |
|---|---|---|---|
| ADAC | "A-dack" | Asset Design and As Constructed | Australian council term |
| As-constructed / as-built | - | Final record model/drawings | Australian "As Constructed" |
| Building consent | - | NZ permit to build | NZ; issued by Building Consent Authority (BCA) |
| Code Compliance Certificate (CCC) | - | NZ completion certificate | NZ |
| Development Application (DA) | - | Australian planning approval | NSW/Qld |
| Digital Engineering (DE) | - | TfNSW term for BIM on infrastructure | Australia |
| Digital twin | - | Digital twin | Infrastructure Australia usage |
| भवन सूचना मॉडलिंग | bhavan sūchanā modeling | Building Information Modelling | Hindi; formal translation seen rarely; usually "BIM" (unverified) |
| करोड़ (Rs crore) | karoḍ | 10 million rupees | Indian threshold unit |
| डीएसआर | DSR | Delhi Schedule of Rates | CPWD costing reference |
| ভবন তথ্য মডেলিং | bhobon tôthyo modeling | Building Information Modelling | Bengali; illustrative (unverified) |
| عمارتی معلومات کی ماڈلنگ | imārati ma'lūmāt kī modeling | Building Information Modelling | Urdu; illustrative (unverified) |
| ගොඩනැගිලි තොරතුරු ආකෘතිකරණය | goḍanægili toratūru ākṛtikaraṇaya | Building Information Modelling | Sinhala; illustrative (unverified) |
| भवन सूचना मोडलिङ | bhavan sūchanā modeling | Building Information Modelling | Nepali; illustrative (unverified) |

Native-language terms were not found in official documents; entries marked illustrative are constructed translations. In practice all five South Asian countries say "BIM" in English.

---

## Typical questions people ask about this

1. Is there a national IFC mandate in Australia? (No federal one found; state/agency requirements such as TfNSW's exist [11][16].)
2. Which IFC version does Transport for NSW accept? (IFC 2x3 or higher, newer with approval, for survey models [16].)
3. Does Queensland require IFC? (The data guideline says deliverables "should" include native and IFC 2X3; the guideline is non-mandated [20].)
4. What coordinate system should an Australian BIM use? (GDA2020 / MGA2020, heights AHD per the Qld guideline [20].)
5. What is ADAC and is it the same as IFC? (No; it is an IPWEA XML asset standard, v5.01 commonly cited [24].)
6. Where do I get NATSPEC BIM templates (EIR, AIR, BEP)? (NATSPEC BIM site [8].)
7. What is OBOS and what are `IfcExportAs` and `IfcExportType`? [10]
8. Is ISO 19650 adopted in Australia? (Yes as AS ISO 19650.1/.3/.5 [4].)
9. Is BIM compulsory for NZ government projects? (MBIE guidelines say agencies must adopt BIM per the NZ BIM Handbook; check the current version [30][33].)
10. Which NZ BIM Handbook appendix gives the EIR template? (Appendix F [27].)
11. Does a NZ council accept IFC for building consent? (Varies by council; no national standard found [34][35].)
12. Is BIM mandatory in India for government projects above Rs 20 / 50 / 100 crore? (Conflicting blog claims, no primary document found [40][43].)
13. Has BIS published a BIM standard? (A 2026 snapshot says no; unverified on BIS site [43].)
14. Does India have a buildingSMART chapter? (CDCPIndia, Developing Chapter since June 2023 [44].)
15. What did the Economic Survey 2023-24 say about BIM? (Recommends adoption, cites NITI Aayog roadmap, no mandate in summary [37].)
16. Does NHAI require BIM? (Claimed in blogs; no circular found [40].)
17. What BIM requirements exist in Pakistan? (None official found [47].)
18. Is there a BIM mandate in Bangladesh or Sri Lanka? (None found [50].)
19. Why does my IFC from Revit lose shared coordinates when sent to an Australian client? (illustrative)
20. Can an MCP tool check that an IFC file is in GDA2020 / MGA zone 55? (illustrative)
21. How do I map Revit categories to `IfcExportAs` using OBOS conventions? (illustrative)
22. Which Uniclass 2015 codes does Queensland expect in properties? (illustrative)
23. What is the difference between IFC 2x3 CV2.0 and IFC4 Reference View for a TfNSW submission? (illustrative)

No real forum questions with usable links were found within the search quota; the questions above are mostly derived from the documents, those marked "(illustrative)" are invented.

---

## Common pitfalls and misconceptions

- **"Australia mandates IFC."** No federal mandate found; requirements are per agency (TfNSW, Qld guideline "should") [16][20].
- **Confusing document numbers**: TfNSW Part 2 is DMS-ST-207; DMS-ST-208 is the Framework; Part 1 is DMS-ST-202 [11][12][13].
- **ADAC is not IFC** and has its own version cycle [24].
- **IFC 2x3 lacks IfcMapConversion**; georeferencing must be carried by site placement or property sets. A model passes "IFC 2x3 or higher" yet may fail georeferencing checks (general knowledge).
- **Indian mandate thresholds** (Rs 20/50/100/500 crore) circulate widely but have no verified primary source [40][43].
- **"BIS has an IS code for BIM"**: not verified; the NBC 2016 is a building code, not a BIM standard.
- **NZ**: the Handbook is industry guidance co-funded by the Construction Sector Accord; compulsion comes from MBIE procurement guidance for government agencies [27][30].
- **Wrong ISO**: ISO 16739-1 is IFC; ISO 19650 is information management; ISO 12006 is classification. Mixing them confuses requirements.
- **Summaries on aggregators** (globalbim.org, plbimcom, blogs) may lag official documents; the NATSPEC date and TfNSW review dates have already passed.

---

## Gaps

- Primary PDFs not readable: TfNSW Part 2 and Survey Guide, Qld Principles, TMR BIM guideline, NZ MBIE BIM procurement guidelines, Victorian Digital Asset Policy, PIB releases (403 or binary). Details marked "snippet only".
- Official CPWD circular, MoHUA and NHAI BIM documents, and BIS documents not found.
- Sri Lanka and Nepal not researched beyond one failed query; Pakistan and Bangladesh only academic/news sources.
- Georeferencing and classification for NZ/India based on general knowledge.
- Skipped: Scribd copies of government documents (unofficial); YouTube short on CPWD; aggregator blogs flagged as marketing.

---

## Sources

[1] Australian BIM Strategic Framework (summary page) https://sites.google.com/view/plbimcom/standards/australia/australian-bim-strategic-framework
[2] globalbim.org info collection (framework) https://globalbim.org/node/841
[3] GovTech Review, "All govt infrastructure projects to use a digital twin" (13 Sep 2021) https://govtechreview.com.au/content/gov-digital/article/all-govt-infrastructure-projects-to-use-a-digital-twin-462082166
[4] Standards Australia store, AS ISO 19650.1:2019 https://store.standards.org.au/product/as-iso-19650-1-2019 (details via search snippet)
[5] RISSB AS 7739.1 Digital Engineering https://www.rissb.com.au/wp-content/uploads/2023/05/AS-7739.1-Digital-Engineering-1.pdf
[6] buildingSMART International, Australasia and Portugal become Full Chapters (29 Apr 2025) https://www.buildingsmart.org/news/page/2/
[7] buildingSMART Australasia https://www.buildingsmart.org.au/
[8] NATSPEC BIM, National BIM Guide https://bim.natspec.org/documents/natspec-national-bim-guide
[9] NATSPEC publications index (Apr 2026) https://www.natspec.com.au/images/PDF/NTN_INDEX.pdf
[10] OBOS summary (mirror) https://sites.google.com/view/plbimcom/standards/australia/open-bim-object-standard-obos ; original at https://bim.natspec.org
[11] TfNSW Digital Engineering Standard Part 1 v4.1 https://www.transport.nsw.gov.au/system/files/media/documents/2022/Digital-Engineering-Standard-Part-1-concepts-and-principles-v4.1.pdf
[12] TfNSW Digital Engineering Standard Part 2 v4.1 https://www.transport.nsw.gov.au/system/files/media/documents/2022/Digital-Engineering-Standard-Part-2-requirements-v4.1.pdf
[13] TfNSW Digital Engineering Framework page https://www.transport.nsw.gov.au/digital-engineering/digital-engineering-framework-0
[14] TfNSW Digital Engineering Framework v4.0 https://www.transport.nsw.gov.au/system/files/media/documents/2022/Digital-Engineering-Framework-v4.0.pdf
[15] TfNSW Digital Engineering Framework DMS-ST-208 v3.0 https://www.transport.nsw.gov.au/system/files/media/documents/2019/Digital%20Engineering%20Framework%20-%20DMS-ST-208%20.pdf
[16] TfNSW DMS-SD-142 Digital Engineering Survey Requirements Guide https://www.transport.nsw.gov.au/system/files/media/documents/2024/DMS-SD-142_Digital-Engineering-Survey-Requirements-Guide.pdf
[17] TfNSW Setting up for BIM v3.1 https://www.transport.nsw.gov.au/system/files/media/documents/2023/Setting-up-for-BIM-v3.1.pdf
[18] Queensland BIM principles https://www.statedevelopment.qld.gov.au/__data/assets/pdf_file/0020/32915/bim-principles.pdf
[19] Queensland BIM page https://dsdmip.qld.gov.au/bim
[20] QGEA BIM projects data and information guideline https://www.forgov.qld.gov.au/information-and-communication-technology/qgea-policies-standards-and-guidelines/bim-projects-data-and-information-guideline
[21] TMR BIM guideline https://www.tmr.qld.gov.au/_/media/busind/techstdpubs/road-planning-and-design/building-information-modelling/bim-guideline.pdf
[22] globalbim.org, Victorian Digital Asset Policy https://globalbim.org/info-collection/victorian-digital-asset-policy/
[23] Victorian Digital Asset Policy PDF https://www.vic.gov.au/sites/default/files/2023-02/Digital-Asset-Policy.pdf
[24] Logan City Council ADAC https://www.logan.qld.gov.au/planning-and-building/planning-and-development/development-in-logan/works-and-specifications/asset-design-and-as-constructed
[25] Ipswich City Council ADAC https://www.ipswich.qld.gov.au/Services/Planning-and-Building/Development-Assessment/Operational-Works-and-Construction/ADAC-As-Design-As-Constructed-As-Constructed-Information
[26] FME ADAC writer docs https://docs.safe.com/fme/2017.0/html/FME_Desktop_Documentation/FME_ReadersWriters/adac/ADAC_writer.htm
[27] BIMinNZ, NZ BIM Handbook https://www.biminnz.co.nz/nz-bim-handbook
[28] Launch of NZ BIM Handbook third edition https://www.biminnz.co.nz/bim-in-nz-news/2019/17/launch-bim-nw-zealand-handbook-third-edition
[29] globalbim.org, NZ BIM Handbook https://globalbim.org/info-collection/the-new-zealand-bim-handbook/
[30] MBIE/NZ Government Procurement, BIM construction procurement guidelines https://www.procurement.govt.nz/assets/procurement-property/documents/building-information-modelling-construction-procurement.pdf
[31] Government Procurement Rules 4th edition https://www.procurement.govt.nz/assets/procurement-property/documents/government-procurement-rules-4th-edition.pdf
[32] Government Procurement Rules 5th edition https://www.procurement.govt.nz/assets/procurement-property/documents/government-procurement-rules-5th-edition.pdf
[33] globalbim.org, MBIE BIM procurement guidelines https://globalbim.org/info-collection/bim-construction-procurement-guidelines/
[34] University of Auckland, BIM-based consent proof of concept https://researchspace.auckland.ac.nz/handle/2292/41608
[35] Christchurch City Council BIM guidelines https://www.ccc.govt.nz/assets/Documents/Consents-and-Licences/construction-requirements/BIM/BIM-Coordination-CCC-BIM-Implementation-Guidelines.pdf
[36] New Plymouth DC digital consents (govlaunch) https://govlaunch.com/projects/new-plymouth-district-council-nz-completely-digitized-its-building-consent-process
[37] PIB, Economic Survey 2023-24 on BIM https://www.pib.gov.in/PressReleasePage.aspx?PRID=2034917
[38] Fiinews summary of the Survey https://www.fiinews.com/2024/07/23/tenders-bim-can-reduce-infrastructure-costs
[39] PIB, CPWD 170 years (lists "Introducing BIM in CPWD") https://pib.gov.in/PressReleasePage.aspx?PRID=2032829
[40] EPC World, BIM Mandates (17 Jul 2025, blog-level) https://www.epcworld.in/bim-mandates-a-new-imperative-in-public-infrastructure-delivery/
[41] Novatr blog on CPWD (May 2026, promotional) https://www.novatr.com/blog/digital-construction-shift-with-cpwd
[42] PIB, IIT Palakkad MoU with MoHUA and CPWD https://www.pib.gov.in/PressReleasePage.aspx?PRID=2280652&reg=48&lang=2
[43] InfraLens, BIM in India 2026 snapshot (third-party) https://infralens.in/handbook/bim-india-snapshot
[44] buildingSMART India joins as Developing Chapter https://www.buildingsmart.org/india-joins-buildingsmart-international-as-a-developing-chapter/
[45] Press release (ThePrint/ANI) on CDCPIndia https://theprint.in/ani-press-releases/buildingsmart-international-bsi-announces-the-confederation-of-digital-construction-practitioners-cdcpindia-as-buildingsmart-india/1637811
[46] Press release on NITI Aayog endorsement https://theprint.in/ani-press-releases/niti-aayog-building-smart-international-endorse-cdcpindia-for-advancing-digitalization-bim-adoption-in-india/1006135
[47] Dawn, CDA energy codes (24 Sep 2025; no BIM content) https://www.dawn.com/news/amp/1944190
[48] Pakistan BIM conference paper (CUST) https://csce.cust.edu.pk/archive/CSCE_22_conference_proceedings/Paper ID.22-336.pdf
[49] Engineering Review (NHA/FIDIC) https://engineeringreview.com.pk/?p=12332
[50] Adoption of BIM to Improve Urban Construction in Bangladesh (2026) https://journals.e-palli.com/home/index.php/ajcec/article/view/7679
[51] IfcOpenShell on GitHub https://github.com/IfcOpenShell/IfcOpenShell
[52] 12d Synergy blog (vendor) https://12dsynergy.com/?p=7392
[53] plbimcom standards mirror https://sites.google.com/view/plbimcom/standards/new-zealand/nz-bim-handbook
