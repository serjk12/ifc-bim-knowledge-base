# Middle East and Turkey: BIM/IFC requirements

## In plain words

The region has no single BIM rule. Each country, and often each city or agency, does its own thing. The only fully published, IFC-specific national rule found in this research is Turkey's August 2026 pair of regulations: from 2027-2033 permit projects must be delivered as IFC (per ISO 16739-1) through a ministry portal called e-PYS. In the Gulf, requirements come from municipalities and public-works agencies (Dubai Municipality, Abu Dhabi DMT, Qatar's Ashghal) and are usually written as ISO 19650-style documents (EIR, BEP, MIDP) with Revit/Navisworks as the working tools and IFC as an exchange or submission format. For Saudi Arabia, Oman, Kuwait, Bahrain, Israel, Iran, Egypt and Jordan, only fragments could be verified; many claims on the web are vendor or press statements and are marked "(unverified)" below. A tester should treat the country as a parameter: coordinate system, naming scheme, classification and "which IFC version" all change per jurisdiction.

Last researched: 2026-11-06

> Research limits: the web-search quota ran out mid-session, so Iran, Jordan, Saudi giga-project requirements, Israeli government policy, local open-source projects and real practitioner forum questions could NOT be researched. They are listed under "Gaps". Several official PDFs (Dubai circulars, Turkish annexes EK-5..EK-9, buildingSMART chapter pages) could not be read by the fetch tool.

---

## 1. Snapshot by country

| Country | Who mandates | Status of mandate (as researched) | IFC-specific? | Confidence |
|---|---|---|---|---|
| UAE - Dubai | Dubai Municipality (DM) | Circular 196 (2013) and 207 (2015) for large/government buildings; digital BIM model required with permit applications from 1 Jan 2024 for defined categories [1][2][3][4] | Government-project submissions must include IFC [4] | Medium-high |
| UAE - Abu Dhabi | Department of Municipalities and Transport (DMT), "Municipal Infrastructure and Assets Sector" | BIM Code of Practice v1 (Oct 2020) for municipal infrastructure projects [6]; no general building-permit mandate verified | Native + IFC at every data drop [6] | Medium-high (infrastructure only) |
| Saudi Arabia | Reported: municipal/housing ministry; "January 2024" [2][15][16] | Press/thesis claim only; no official text found | Not found | Low (unverified) |
| Qatar | Public Works Authority (Ashghal) | ABIMS - Ashghal BIM Standards, 20 documents [11] | IFC for infrastructure "to be confirmed in a later revision" [12]; COBie template exists [11] | High for Ashghal projects |
| Oman | Ministry of Housing and Urban Planning (MoHUP) | National Building Requirements and Standards Guide; pilot 2026-2027, full adoption by 2030; no BIM mention in the article [32] | No | Low |
| Kuwait | Ministry of Public Works (MPW) | 2015 tender to buy a BIM solution [33]; 2024 academic paper treats BIM as not yet a mature requirement [34] | No | Low |
| Bahrain | Municipalities ministry + iGA | Pilot linking BIM to the Benayat permit system [35]; no mandate text found | No | Low |
| Israel | Standards Institution of Israel (SII) for standards; government policy not verified | SI 19650 Part 1 is a published national standard [29]; no mandate found | Not found | Medium for the standard, none for mandate |
| Turkey | Ministry of Environment, Urbanization and Climate Change (Çevre, Şehircilik ve İklim Değişikliği Bakanlığı) | Two regulations, Resmî Gazete 5 Aug 2026, no. 33331; phased 2027-2033 [19][21] | Yes: IFC per TS EN ISO 16739-1 [19][21] | High for headline, annex details not read |
| Iran | - | Not researched (quota) | - | None |
| Egypt | Housing and Building National Research Center (HBRC) drafted a code | Egyptian BIM Code draft G01 (June 2018), v2 listed 2020; no nationwide mandate found [36][37][38] | Not stated | Low-medium |
| Jordan | - | Not researched (quota) | - | None |

---

## 2. United Arab Emirates

### 2.1 Dubai

**Timeline (secondary sources unless stated):**

| Year | Document | Content |
|---|---|---|
| 2013 | Dubai Municipality Circular No. 196 | First BIM requirement in Dubai: architectural and MEP work on buildings above 40 floors, buildings over 300,000 sq ft, specialist buildings (hospitals, universities), buildings requested on behalf of a foreign office [1] |
| 2015 | Circular No. 207 | Widened scope: above 20 floors, buildings/facilities/compounds over 200,000 sq ft, all government projects, projects requested from a foreign office; consulting offices responsible for applying it; 196 stays in force [1] |
| 13 Oct 2023 (per a search summary; unverified) | Circular 9-1-2 (2023), "mandatory BIM model submission with building permit applications for certain categories of buildings" | Effective 1 Jan 2024; issued under the Dubai Building Code and "Dubai BIM" standards [3][4] |
| Feb 2026 (file path suggests this) | Circular 9-1-3 (2026) - "Updated BIM Mandate for building approvals in Dubai" | Listed on Global BIM Network as outlining CAD/BIM submission requirements for planning data [5]. The PDF could not be read; a social-media post (unverified) says it adds triggers such as adding/removing floors or +1,500 m2 of built area |

**2024 thresholds** (consistent across Global Construction Review, LRQA, Autodesk) [2][3][4]:

- Architectural BIM: buildings/facilities above 20 floors.
- Structural BIM: buildings above 40 floors.
- Complexes: above 20,000 m2 (architectural) or 30,000 m2 (structural).
- Specialised facilities, e.g. hospitals and universities.
- Government projects (utility infrastructure excluded; some smaller/less complex facilities excepted [2][4]).
- Applications without the model are not accepted [3].

**Platform and tools:** "Build in Dubai" (buildindubai.gov.ae) is the online construction-services platform that uses BIM and E-Checking; a "BIM E-Submission User Manual" covers model development and best practice [4]. A Dubai Municipality GIS page describes a BIM roadmap with short- and long-term plans, unified standards for design submission, automatic design audit, and a link to the Dubai Digital Twin initiative [9]. A "Dubai BIM Roadmap" PDF is listed at bim.geodubai.ae (attributed to RTA on the Global BIM page, but the host name suggests Dubai Municipality GIS; inconsistent, unverified) [5].

**IFC:** the Autodesk summary of the mandate says that for government projects BIM submissions must include models in IFC format [4]. IFC version, MVD, property sets and classification for Dubai could not be verified.

**Georeferencing (general knowledge, unverified for DM rules):** Dubai uses a local projected grid (Dubai Local Transverse Mercator) and UTM zone 40N is common in the UAE; always check the project EIR.

**Pitfall:** the 2017 CMS legal guide says Dubai circulars set no minimum BIM level and that Abu Dhabi had no mandate [1]. It is dated 30 June 2017 and is outdated on Abu Dhabi.

### 2.2 Abu Dhabi

- Authority: Department of Municipalities and Transport (DMT); the "Municipality of Abu Dhabi City - Municipal Infrastructure and Assets Sector" published the **BIM Documentation Code of Practice, Version 1 (document header v1.1), October 2020**, 26 pages [6].
- Document set in the DMT e-library (January 2022 upload path): ADM-BIM-001 Pre-Qualification Questionnaire (assesses bidders' BIM capability incl. ISO 19650 alignment), ADM-BIM-002 Documentation Guidelines for Infrastructure Projects, ADM-BIM-005 Code of Practice, ADM-BIM-006 QA/QC Checklist for Infrastructure Projects [5][6][7].
- Scope: municipal infrastructure and assets; Autodesk markets it as the "Abu Dhabi Municipality BIM Mandate for Infrastructure Projects" [8].

**What the Code of Practice actually requires [6]:**

| Topic | Requirement |
|---|---|
| Standards referenced | ISO 19650-1/-2:2018 (PAS 1192-2:2013 as UK equivalent), ISO 16739-1:2018 (IFC), UniFormat II [6][7] |
| Documents | Employer's EIR, pre-appointment BEP, project BEP, MIDP/TIDPs, Employer's LOD Matrix |
| Authoring formats | DWG / RVT, "base version 2021" (Revit/Civil 3D class tools) |
| Coordination | NWC per discipline, NWD for federated model |
| Submission at each data drop | Native files **and IFC**; 2D extracts as PDF and DWG; 4D as "SP" and 5D as "ESF" file types |
| Coordinates | Must respect the ADM GIS system; BEP must state datum, units, offsets, origin rotation, shared coordinates |
| LOD | Employer's LOD Matrix mandatory across all infrastructure elements |
| Classification | CSI UniFormat II |
| File size | Placeholder "150 MB" maximum per file, split if exceeded |
| CDE | WIP / Shared / Published / Archive states with gateways |

The PIM (project information model) deliverable is "in IFC format" (ADM-BIM-002) [7].

### 2.3 Federal level, other emirates

No federal UAE BIM mandate was found (a 2017 article only speculated) [1]. Sharjah, Ajman, RAK etc. were not researched.

### 2.4 buildingSMART UAE and Dubai tech

On 27 Aug 2020 Dubai Municipality was chosen to host the UAE chapter of buildingSMART International, the first in the region; goals include working groups on building permit procedures, automated code checking and digital twins, BIM-GIS integration, Arabic translation of BIM standards and accredited training [10].

---

## 3. Saudi Arabia

- **Claim:** from January 2024 BIM is mandatory in Saudi Arabia. LRQA: "mandated the use of Building Information Modelling (BIM) Management for all major construction and engineering projects", tied to Vision 2030 [2]. A 2025 KFUPM master's thesis abstract: BIM required for architectural plans in all building projects, and engineering offices must submit 3D models to the municipal/housing ministry [16]. The two differ in scope (major projects vs all building projects) and neither cites an official decision. **(unverified)**
- **Saudi Building Code (SBC):** application law Royal Decree M/43 (2017) per a reference-site entry [17]; implementing regulations PDF hosted on momah.gov.sa [18]. Neither confirms a BIM clause in the excerpts read.
- **Balady** is the municipal permit platform; the thesis uses Revit 2024 + Dynamo 2.1 to check residential designs against SBC architectural requirements [16] (useful as a model of "BIM-based code compliance checking", not proof of a Balady BIM rule).
- Not verified: giga-project requirements (NEOM, Red Sea, Qiddiya, ROSHN), SASO standards, Saudi BIM authority [a journal paper proposes creating a "Saudi BIM Authority", i.e. none existed when written].

---

## 4. Qatar

Ashghal (Public Works Authority) publishes **ABIMS - Ashghal BIM Standards**, on its "BIM, CAD and GIS" page [11]:

| Code | Document | Version |
|---|---|---|
| D0102 | Abbreviations and Terminology | V1 |
| D0201 | File Naming Convention for BIM and CAD | V1 |
| D0301 | Master Information Delivery Plan Template (xlsx) | V1 |
| D0401 / D0402 | Level of Information Need Guide / Specification (xlsx) | V2 |
| D0501 / D0502 | Model Element Table Template Guide / Template | V2 |
| D0601 | Modelling and Data Management Guide | V1 (release date 15 March 2022) |
| D0701 | BIM Quality Assurance Checklist (xlsx) | V1 |
| D0801 | Process Diagram Guide | V1 |
| D1001 / D1002 | COBie Template Guide / Template | V1 |
| S0101 / S0102 | Revit Template Guide / Template (zip) | V1 |
| S0201 / S0202 | Civil 3D Template Guide / Template | V1 |
| S0301-S0304 | Clash Detection Matrix and Clash Detection templates | V1 |

**From D0601 (read as text) [12]:**

- Based on ISO 19650-2 (cites clause 5.6 for collaborative production); CDE states WIP/Shared/Published/Archive with suitability codes.
- **Georeferencing:** all models at true world coordinates on the **QND95 grid**; project base point format "2YYYYY.YYYN 4XXXXX.XXXE"; Revit models use Shared Coordinates for federation; Project Base Point set manually if single model; True North = real north; Civil 3D drawings in QND95 with UCS = World. Buildings: Z in **mm**; infrastructure: Z in **m**.
- Civil 3D layer naming based on Uniclass 2015.
- GUIDs are created on Revit-to-Navisworks export and must be stable.
- Section 7.9 "IFC for Infrastructure": "To be confirmed in a later revision of this document."
- Section 11 covers laser scanning; non-compliant Civil 3D models "will be rejected".
- Document warns that printed copies are uncontrolled; ask Ashghal's Engineering Services Department for the latest version.

Background: a Qatar University paper says departmental differences led to non-uniform BIM requirements, motivating ABIMS [14]. A 2023 Autodesk University class on "Qatar's Road Map and Strategy" exists (page could not be read) [13].

---

## 5. Oman, Kuwait, Bahrain

- **Oman:** MoHUP's National Building Requirements and Standards Guide (article datelined 6 Oct 2025) introduces a new licensing/inspection framework, pilot 2026-2027, full adoption by 2030; the article does not mention BIM [32][44]. A conference-site claim that BIM submittals are required for buildings over 4 storeys from 2026 comes from a mirror-like page and is **(unverified)** [41]. Academic papers say BIM adoption is limited.
- **Kuwait:** MEED (4 Aug 2015) reported an MPW tender for a BIM solution for its design department [33]. A 2024 *Buildings* paper studies barriers at MPW [34]. No binding public mandate found.
- **Bahrain:** a BIM project with iGA connects BIM to the *Benayat* system for automated design checks against planning rules; pilot areas Diyar Al Muharraq, Salman City, Bahrain International Investment Park [35]. Ministry names changed over time (Works / Municipalities Affairs / Housing and Urban Planning) - check the current name [43].

---

## 6. Turkey (Türkiye)

### 6.1 The 2026 regulations

Both published in Resmî Gazete **5 August 2026, no. 33331**, issued by the Ministry of Environment, Urbanization and Climate Change, legal basis Zoning Law No. 3194 [19][21]:

1. **Mimarlık ve Mühendislik Projelerinin Dijital Olarak Hazırlanması Hakkında Yönetmelik** (Regulation on Digital Preparation of Architecture and Engineering Projects) - in force **1 Sep 2027** (Madde 16).
2. **Mimarlık ve Mühendislik Projelerinin Elektronik Ortamda Teslimi ve Yönetilmesi Hakkında Yönetmelik** (electronic delivery and management) - in force **1 Sep 2028** [21].

Draft stage: a ministry draft (Nov 2025, csb.gov.tr) existed; it reportedly specified DXF for CAD files, the final text uses PDF/A [26] (the draft PDF itself could not be fetched).

Earlier legal hook: a 2025 amendment to the Planlı Alanlar İmar Yönetmeliği allowing BIM-standard project data to be stored in a ministry-run data infrastructure [27] (**unverified**, search snippet only).

**Key articles (from the Gazette page and secondary summaries) [19][21][22]:**

- Art. 4/2-3: 2D drawings and other documents are **PDF/A**; scanned PDFs not accepted; one sheet per file; A4-multiple sheets.
- Art. 4/4: 3D models are BIM-based, per **TS EN ISO 19650-1 and -2**.
- Art. 4/5: "BIM modeli TS EN ISO 16739-1'de tanımlanan IFC formatında teslim edilir" - BIM model delivered in IFC as defined in TS EN ISO 16739-1.
- Art. 9: each discipline prepares its own BIM model per EK-5, EK-6, EK-7; **CAD drawings are generated from the BIM model** and the model and PDF/A must be consistent; SI units.
- Art. 5: Turkish Standards first, then European, then international.

**Phase-in (Geçici Madde 1) [19][21][22]:**

| What | Where / size | Date |
|---|---|---|
| PDF/A | Provinces >2M pop., municipalities >600k, buildings >5,000 m2 | 1 Sep 2027 |
| PDF/A | All other buildings | 1 Mar 2029 |
| IFC/BIM | Buildings >10,000 m2: provinces >2M, municipalities >600k | 1 Sep 2029 |
| IFC/BIM | Provinces >2M, municipalities >400k | 1 Sep 2030 |
| IFC/BIM | Provinces >1M, municipalities >300k | 1 Sep 2031 |
| IFC/BIM | All other buildings | 1 Sep 2032 |
| Non-residential (other than housing and housing+commerce mixed) | whole regulation | not applied until 1 Sep 2033 |

Once IFC becomes mandatory for a group, the separate PDF/A duty is replaced by PDF/A derived from the model [21]. Exempt: detached buildings with no basement and max two storeys and total area up to 200 m2; agricultural/livestock buildings (unless integrated facilities); areas with no implementation zoning plan; applications filed, or public tenders decided, before the dates (Geçici Madde 2) [21]. Sources disagree on how the 2033 clause interacts with the 2032 row and with public buildings (one summary says public buildings are outside e-PYS under Madde 26 yet appear in the 2033 tier) [23] - check the Gazette text.

### 6.2 e-PYS (Elektronik Proje Yönetim Sistemi)

Ministry-operated system for delivery, review, deficiency notices, approval and notification; municipal e-permit systems remain but must integrate; only the project author (müellif) uploads and is responsible for accuracy; secure e-signature or else a signed printed copy; incomplete/incorrect files are returned [21][23]. No public portal address or Ministry guideline (kılavuz) was found.

### 6.3 Technical annexes (only partly known)

The annex PDF (resmigazete.gov.tr/eskiler/2026/08/20260805-2-1.pdf) exceeded the fetch size limit; the following is from secondary summaries [23][24][25]:

| Annex | Content (as summarised) |
|---|---|
| EK-1 | Project code algorithm (6 characters, e.g. 260001) |
| EK-2 | Discipline/sub-discipline codes (MM, ST, EE, MK, PY, YN ...) |
| EK-3 | Floor and room (mahal) naming, e.g. K01_D02_007 |
| EK-4 | CAD layers, line types, colours, text sizes |
| EK-5 | IFC classes and 3-letter category codes (e.g. DVR, KAP); room naming |
| EK-6 | Mandatory IFC attributes/properties per class (e.g. fire resistance) |
| EK-7 | Mandatory project properties (ada/parsel = block/parcel, author info) |
| EK-8 | Development level (gelişim seviyesi / LOD); one blog says LOD 300 typical for execution projects (author's opinion) |
| EK-9 | Model quality-control form to complete before delivery |

File names: 9 fields, e.g. `260001_00_MM_XXXX_PL_MMC_K00_01_000.pdf`; model entities `[Discipline]-[Category]-[Description]` with hyphens only [23]. Reported QC checks: model coordinates, floor/building placement, IFC classes, duplicate/clashing elements, mandatory properties, model-vs-sheet consistency, naming [24].

**Not found in any accessible source:** the IFC schema version (IFC2x3 vs IFC4), MVD, Pset names, coordinate reference system [23][24][25]. Do not assume IFC4. One source says these will be settled by ministry guidelines [24].

**Contradictory web claims:** one consultancy post states "BIM mandate started in Turkey" for public projects in 2025 [42]; this conflicts with the Gazette timetable above.

---

## 7. Israel

- **Standards Institution of Israel (SII, מכון התקנים הישראלי):** ת"י 19650 Part 1 (concepts and principles, "ארגון ותיעוד ספרתי של מידע על מבנים ... לרבות מידול מידע הבניין (BIM)") - published in the gazette (ילקוט הפרסומים 9278, dated 08/12/2020), standard dated 30/11/2020, corrigendum notice 14.2.2024; it is an adopted standard with Hebrew supplement [29]. Part 2 (delivery phase) is hosted on engineering.org.il [30].
- A government document on "Building regulations (Yaron Plus) - multidimensional tech as infrastructure" is listed on gov.il [30]; it could not be read, so its relation to 3D/BIM permit submission is **unverified**.
- **Pitfall:** ת"י 1918 is the accessibility standard series, not BIM [search result review]. 
- No Israeli government BIM mandate (Ministry of Construction and Housing, Planning Administration, Accountant General) was verified.
- Georeferencing (general knowledge, unverified here): Israeli Transverse Mercator grid (ITM, EPSG:2039).

---

## 8. Iran, Egypt, Jordan

- **Iran:** nothing verified. Persian Wikipedia's BIM article cites studies (e.g. barriers to BIM adoption in Iran) but no standard numbers or mandate [39]. Building Engineering Organization (سازمان نظام مهندسی ساختمان) exists as the professional body; its BIM role is not documented here.
- **Egypt:** the HBRC drafted "The Egyptian Code for Building Information Modeling (BIM), Draft Edition G01", June 2018, based on British codes [37]; a "v2, 2020" is listed on Global BIM Network with Luqman Academy named as organisation (so possibly a training-company copy, not an official issue) and no IFC/ISO 19650/mandate statement [36]. A vendor blog says no nationwide mandate exists [38].
- **Jordan:** not researched.

---

## 9. Classification, georeferencing and naming cheat-sheet

| Place | Classification | CRS / coordinates | Naming |
|---|---|---|---|
| Abu Dhabi infrastructure | UniFormat II [6] | ADM GIS system; datum/offsets declared in BEP [6] | ADM naming standards [5] |
| Qatar Ashghal | Uniclass 2015 for Civil 3D layers [12] | QND95 grid, Z in mm (buildings) / m (infra) [12] | D0201 File Naming Convention [11] |
| Turkey | Own IFC class + 3-letter category lists (EK-5) [23] | not found | 9-field file name, EK-1..EK-3 [23] |
| Dubai | not verified | not verified (DLTM/UTM-40 likely) | not verified |
| Israel | not verified | ITM (general knowledge) | not verified |

---

## 10. Organisations

| Organisation | Role |
|---|---|
| buildingSMART International chapter directory | Lists chapters; Türkiye chapter incorporated 2020, "Developing Chapter", chaired by Muhammed Maraşli (organisation-level info from directory snippets; pages returned 403) [28] |
| buildingSMART UAE | Hosted by Dubai Municipality, announced 27 Aug 2020 [10] |
| Standards Institution of Israel | National adoption of ISO 19650 as ת"י 19650 [29] |
| TSE (Turkish Standards Institution) | Adopts TS EN ISO 19650 / 16739-1 (implied by regulation text) [19] |
| Ashghal / DMT / Dubai Municipality | Public clients issuing BIM standards [5][6][11] |
| HBRC (Egypt) | Drafted Egyptian BIM Code [37] |

Israel, Iran, Saudi, Qatar, Egypt, Jordan chapters: not verified.

---

## 11. Software ecosystem

- **Dominant tools:** Autodesk Revit, Civil 3D, Navisworks (ADM and Ashghal templates are Revit/Civil 3D/Navisworks based) [6][11][12]. ADM base version 2021 [6].
- **Turkey:** a blog on the new regulations lists CYPE products (BIMserver.center, Open BIM Layout, Model Checker), Revit, Archicad, Allplan, Tekla Structures, ACCA (Edificius, usBIM), ProtaStructure and ideCAD Structural as candidates, stating none is automatically compliant; the author favours CYPE (opinion) [24]. ProtaStructure and ideCAD are Turkish structural packages.
- **Israel/Iran/Arab local software and open-source projects:** not researched (Gaps).

---

## 12. Local terminology

| Native term | Transliteration | English |
|---|---|---|
| Yapı Bilgi Modellemesi | - | Building Information Modelling |
| müellif | - | project author / responsible designer |
| mahal | - | room/space |
| pafta | - | drawing sheet |
| gelişim seviyesi | - | level of development (LOD) |
| Resmî Gazete | - | Official Gazette |
| Elektronik Proje Yönetim Sistemi (e-PYS) | - | electronic project management system |
| نمذجة معلومات البناء | namdhajat ma'lumat al-bina' | BIM |
| تعميم | ta'mim | circular |
| رخصة بناء | rukhsat bina' | building permit |
| كود البناء السعودي | kud al-bina' al-su'udi | Saudi Building Code |
| מידול מידע הבניין | modul meida habinyan | BIM |
| ת"י (תקן ישראלי) | Teken Yisraeli | Israeli Standard (SI) |
| היתר בנייה | heter bniya | building permit |
| مدل‌سازی اطلاعات ساختمان | model-sazi-ye eṭṭela'at-e sakhtemān | BIM (Persian) |
| سازمان نظام مهندسی ساختمان | Sazman-e Nezam-e Mohandesi-ye Sakhteman | Building Engineering Organization (Iran) |

(Transliterations of Arabic/Hebrew/Persian are approximations.)

---

## 13. What this means for MCP testing

- **Country-specific checks:** an LLM agent asked to "validate a Turkish permit IFC" should check: IFC file present; discipline-separate models; room names following EK-3 pattern; IFC classes per EK-5; mandatory attributes per EK-6; project code per EK-1. It must not assert IFC4 vs IFC2x3 - the schema version is not in accessible sources.
- **Qatar:** test that Revit's Project Base Point / Survey Point are in QND95 (northing 2xxxxx, easting 4xxxxx) and exported IFC contains map conversion; Z units mm for buildings.
- **Abu Dhabi:** test that a delivery contains both native and IFC, file size under the stated limit, and an NWC/NWD set.
- **Dubai:** thresholds are testable rules (floors >20, >40; area >20,000 / >30,000 m2) - ask the model to decide whether a building requires an architectural or structural BIM submission.
- **IFC concepts relevant everywhere:** IfcProject, IfcSite, IfcBuilding, IfcBuildingStorey, IfcSpace, IfcMapConversion / IfcProjectedCRS for georeferencing, Pset_*Common property sets; the regional documents mostly define their own required properties.

---

## Typical questions people ask about this

No real forum questions could be harvested (search quota exhausted). All below are (illustrative).

1. (illustrative) Is BIM mandatory for a 25-storey residential tower permit in Dubai from 2024?
2. (illustrative) Do I need an IFC file for a Dubai Municipality submission, or is native Revit enough?
3. (illustrative) What does Dubai Municipality Circular 9-1-3 (2026) change compared with 9-1-2 (2023)?
4. (illustrative) Which coordinate system does Ashghal require, and how do I set it in Revit?
5. (illustrative) What are Ashghal D0401/D0402 and how do I fill in a Level of Information Need?
6. (illustrative) Does Abu Dhabi require BIM for private building permits or only municipal infrastructure?
7. (illustrative) Is there an official Saudi BIM mandate, which authority issued it, and what are the thresholds?
8. (illustrative) Türkiye'de BIM zorunluluğu ne zaman başlıyor? (When does BIM become mandatory in Turkey?)
9. (illustrative) IFC2x3 mü IFC4 mü kullanmalıyım? (Which IFC version should I use for e-PYS?)
10. (illustrative) EK-5'teki IFC sınıflarına göre Revit kategorilerini nasıl eşlerim? (How do I map Revit categories to the EK-5 IFC classes?)
11. (illustrative) Does the Turkish 200 m2 detached-house exemption apply to a house with a basement?
12. (illustrative) האם יש חובה לעבוד ב-BIM בפרויקטים ציבוריים בישראל? (Is BIM mandatory in public projects in Israel?)
13. (illustrative) מה ההבדל בין ת"י 19650 ל-ISO 19650? (Difference between SI 19650 and ISO 19650?)
14. (illustrative) آیا در ایران استاندارد ملی BIM وجود دارد؟ (Is there a national BIM standard in Iran?)
15. (illustrative) Is the Egyptian BIM Code mandatory, and is the 2020 version official?
16. (illustrative) How do I convert a Revit model to IFC with shared coordinates for a Qatar project?
17. (illustrative) Which Revit version does Abu Dhabi accept (the Code of Practice cites 2021)?
18. (illustrative) Can I submit a COBie file to Ashghal and which template do I use (D1001/D1002)?

## Common pitfalls and misconceptions

- "Gulf = one BIM law." False: Dubai, Abu Dhabi, Qatar's Ashghal and Saudi arrangements are different, and several are agency-level.
- Treating press/vendor statements as law: Saudi "January 2024" and Turkey "BIM already mandatory in 2025" are not backed by an official text found here [2][15][42].
- Assuming IFC4 is required in Turkey: the regulation text read cites only ISO 16739-1 [19][21].
- Turkey dates: 1 Sep 2027 (digital preparation, PDF/A) and 2028 (e-PYS delivery) are not the IFC dates (2029-2033) [21].
- Abu Dhabi's mandate found is for municipal infrastructure, not all buildings; the 2017 CMS guide's "no mandate" is outdated [1][6].
- Mixing up Qatar's QND95 with UTM; Z in mm for buildings is easy to miss [12].
- ת"י 1918 (accessibility) is not the BIM standard; BIM is ת"י 19650 [29].
- Circular numbers: 196 (2013) and 207 (2015) are older Dubai circulars; the 2024 requirement is 9-1-2 (2023) and 9-1-3 (2026) per secondary sources [1][3][5].

## Gaps

- Not researched due to quota: Iran national BIM standards (Plan and Budget Organization / ministry), Jordan, Saudi official documents and giga-project EIRs, Israeli government policy, local open-source/enthusiast projects, real practitioner Q&A.
- Pages that failed to load: buildingSMART chapter directory (403), Autodesk Abu Dhabi page (403), Autodesk Qatar class (403), Dubai Circular 9-1-3 PDF (returned homepage), Turkish annex PDF (too large), ministry draft PDF (certificate error), Ashghal PDFs only via text extraction of the saved copy.
- No suspicious or pirated sites were encountered or linked.

## Sources

[1] CMS - BIM law and regulation in the UAE (30 Jun 2017): https://www.cms.law/en/int/expert-guides/cms-expert-guide-to-building-information-modelling-bim/united-arab-emirates
[2] LRQA - New BIM mandates in Dubai and Saudi Arabia: https://www.lrqa.com/en-ae/latest-news/new-bim-mandates-in-dubai-and-saudi-arabia/
[3] Global Construction Review - Dubai mandates BIM for new buildings (27 Nov 2023): https://www.globalconstructionreview.com/dubai-mandates-bim-for-new-buildings
[4] Autodesk - Dubai Municipality BIM Mandate board: https://boards.autodesk.com/dubai-bim-mandate
[5] Global BIM Network - UAE: https://globalbim.org/news/info-country/uae/ (lists https://www.dm.gov.ae/wp-content/uploads/2026/02/Circular-9-1-3.pdf, ADM-BIM-001/006, https://bim.geodubai.ae/Documents/Dubai_BIM_Roadmap.pdf)
[6] ADM BIM Code of Practice v1, Oct 2020: https://www.dmt.gov.ae/adm/-/media/Project/DMT/ADM/E-Library/0001-Jan-2022-Doc/ADM-BIM-005Code-of-Practice.pdf
[7] ADM-BIM-002 Documentation Guidelines for Infrastructure projects: https://dmt.gov.ae/adm/-/media/Project/DMT/ADM/E-Library/0001-Jan-2022-Doc/ADM-BIM-002Documentation-Guidelines-for-Infrastructure-projects.pdf
[8] Autodesk - Abu Dhabi infrastructure BIM mandate campaign (search snippet only): https://www.autodesk.com/ae/campaigns/infrastructure-bim-mandate-abudhabi
[9] Dubai Municipality GIS projects (BIM roadmap): https://www.dm.gov.ae/municipality-business/planning-and-construction/geographic-information-systems/gis-projects/
[10] Dubai Media Office - UAE buildingSMART chapter: https://www.mediaoffice.ae/en/news/2020/August/27-08/Dubai-chosen-to-host-UAE-Chapter
[11] Ashghal BIM, CAD and GIS page: https://www.ashghal.gov.qa/en/Services/Pages/BIMCADGIS.aspx
[12] Ashghal D0601 Modelling and Data Management Guide V1: https://www.ashghal.gov.qa/en/Services/GIS%20and%20CAD%20Manuals/ASHGHAL%20BIM%20STANDARD/D0601_Modelling%20and%20Data%20Management%20Guide_V1.pdf
[13] Global BIM Network - Qatar: https://globalbim.org/news/info-country/qatar ; Autodesk University class: https://www.autodesk.com/autodesk-university/fr/class/BIM-and-Digital-Construction-Qatars-Road-Map-and-Strategy-2023
[14] Qatar University - BIM on public projects in Qatar: https://qspace.qu.edu.qa/handle/10576/47062
[15] Global BIM Network - Saudi BIM mandates: https://globalbim.org/info-collection/saudi-bim-mandates-sustainable-building-standards-codes-and-certification-systems-the-status-quo-and-future-directions-in-saudi-arabia/
[16] KFUPM thesis (2025): https://eprints.kfupm.edu.sa/id/eprint/143307/
[17] Saudipedia - Saudi Building Code: https://saudipedia.com/en/saudi-building-code
[18] SBC implementing regulations (MOMAH): https://momah.gov.sa/sites/default/files/2022-03/allayht-altnfydhyt-lnzam-ttbyq-kwd-albna-alswdy-1443.pdf
[19] Resmî Gazete, 5 Aug 2026, no. 33331: https://www.resmigazete.gov.tr/eskiler/2026/08/20260805-2.htm (second regulation: https://www.resmigazete.gov.tr/eskiler/2026/08/20260805-3.htm)
[20] Annex PDF (not readable by tool): https://www.resmigazete.gov.tr/eskiler/2026/08/20260805-2-1.pdf
[21] Elçi law firm summary: https://www.elci.av.tr/makale/yapi-ruhsati-projeleri-artik-dijital-e-pys-ve-bim-zorunlulugu-ne-zaman-basliyor-5-agustos-2026-yonetmelikleri-189
[22] CADBIM summary (vendor): https://www.cadbim.com.tr/bim-yonetmeligi
[23] imarx guide (vendor): https://www.imarx.com.tr/e-pys-dijital-proje-rehberi/
[24] Statik Programlar blog: https://www.statikprogramlar.com/dijital-proje-hazirlama-yonetmeligi-bim-ifc-pdfa/
[25] BFTA blog: https://bfta.com.tr/2026/08/08/mimari-proje-dijital-teslim-yonetmeligi-rehberi/
[26] Ministry draft (Nov 2025): https://webdosya.csb.gov.tr/db/meslekihizmetler/icerikler/cal-stay-taslak-dokumanlar--20251107085546-20251110130354.pdf
[27] Planlı Alanlar İmar Yönetmeliği amendment (search snippet): https://www.resmigazete.gov.tr/eskiler/2025/03/20250311-1.htm
[28] buildingSMART chapter directory: https://www.buildingsmart.org/community/chapter-directory/ ; Türkiye: https://www.buildingsmart.org/community/chapter-directory/buildingsmart-turkiye/
[29] SII ת"י 19650 Part 1: https://www.sii.org.il/he/lobby/standardization/standard-page?id=7525
[30] Global BIM Network - Israel: https://globalbim.org/news/info-country/israel/
[31] Technion/ITcon 2016 review of BIM protocols: https://www.itcon.org/paper/2016/29
[32] Oman Observer: https://www.omanobserver.om/article/1177702/oman/housing-ministry-unveils-unified-building-code
[33] MEED, Kuwait MPW BIM tender (4 Aug 2015): https://www.meed.com/kuwait-public-works-ministry-to-implement-bim/
[34] MDPI Buildings 14(1):130 (Kuwait MPW): https://www.mdpi.com/2075-5309/14/1/130
[35] Zawya - Bahrain BIM permit project: https://www.zawya.com/en/business/construction/project-launched-to-speed-up-building-permits-in-bahrain-471481
[36] Global BIM Network - Egyptian BIM Code v2 (2020): https://globalbim.org/info-collection/egyptian-bim-code-v2-2020/
[37] Egyptian BIM Code draft G01 (2018) copy: https://www.luqmanacademy.com/courses/just-bim-it-40/pdfs/38b76f052105f0c450d0279afc3dc7baad78a928.pdf
[38] Bimstore blog on Egypt: https://www.bimstore.co/resources/egypts-rapid-bim-adoption-explained
[39] Persian Wikipedia BIM article: https://fa.wikipedia.org/wiki/مدل‌سازی_اطلاعات_ساختمان
[41] Conference-site Oman claim (unreliable): https://test4-clone-1724152277-clone-1753355115-connectoman.expoplatform.com/newfront/news/project-management-excellence-in-omans-built-environment-bim-digitalisation-and-the-new-code-of-delivery
[42] BIMCRONE blog (conflicting claim): https://bimcrone.com/2025/06/19/turkiyede-bim-zorunlulugu-basladi/
[43] Oxford Business Group - Bahrain construction: https://oxfordbusinessgroup.com/reports/bahrain/2024-report/construction-real-estate/construction-zone-infrastructure-projects-and-new-residential-developments-are-providing-various-opportunities-for-investors-overview/
[44] Muscat Daily (search snippet): https://www.muscatdaily.com/?p=90828
