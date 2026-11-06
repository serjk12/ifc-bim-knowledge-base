# Africa: BIM/IFC adoption and requirements

## In plain words

No African country has a fully verified, binding, nationwide "submit IFC models" rule comparable to Singapore's CORENET or the UK Level 2 mandate. What exists is a patchwork. Egypt is the most advanced on paper: a 2025 ministerial decision adopting national BIM guidance standards, with a transition period that appears to end in November 2025 [13]. South Africa has the most mature standards work (ISO 19650 adopted as SANS 19650) but no statutory mandate, and the CIDB (Construction Industry Development Board) national BIM policy is still unfinished [3][5]. Morocco has an unverified press claim of a ministry circular with project-value thresholds [19]. Ethiopia, Kenya and Nigeria have announced plans, roundtables or draft frameworks, not enforced mandates [8][10][12]. In most of the rest of the continent (Ghana, Rwanda, Algeria, Tunisia, Senegal, Lusophone Africa) adoption is client-driven (World Bank / AfDB / foreign developers) and I found no official BIM requirement. IFC is almost never named in any African official text I could read; the practical IFC requirements come from private clients, international funders and ISO 19650-style BIM Execution Plans. For a QA tester: treat "Africa" requests as "ISO 19650 + IFC exchange per project EIR", not as a national IFC rulebook.

Last researched: 2026-11-06. QA pass 2026-11-06: the BIM Community Africa SANS 19650 post, the Al-Masdar report on Egyptian Decision 302/2025 and the Frontiers South Africa policy review were re-fetched and confirm the SANS 19650 dates and committee change, the Decision 302/2025 details (gazette issue 103, 10 May 2025, effect computed as 11 Nov 2025, which is a calculation and not a date stated in the source) and the 15% federated-model figure (the review gives it as "15%" in the abstract and "fewer than 15%" in section 6, and flags several uncited figures). The buildingSMART Morocco chapter page returned HTTP 403 again, so the Morocco chapter status stays from a search summary. See `_meta/qa/qa-standards-2.md`.

Research constraints: the shared web-search budget ran out mid-research, several primary sites returned HTTP 403 (buildingSMART chapter and technical pages, Engineering News), and many findings come from press and academic sources. Every statement marked "(unverified)" needs confirmation against an official gazette or ministry page.

---

## 1. Overview table: status by country (as of 2026-11-06)

| Country | Mandate status found | Who | Key document / fact | Confidence |
|---|---|---|---|---|
| Egypt | Adopted national BIM guidance standards; transition then phased obligation for consultants, engineering offices and developers | Ministry of Housing, Utilities and Urban Communities; HBRC (Housing and Building National Research Center) | Decision No. 302 of 2025, Waqa'i Misriyya issue 103, 10 May 2025 [13] | Medium (secondary press; number conflicts with another source) |
| South Africa | No statutory mandate; voluntary / client-driven | CIDB (policy), SABS (standards), National Treasury / DPWI (procurement) | SANS 19650-1:2022, SANS 19650-2 (June 2023); CIDB BIM policy/strategy in preparation [2][3][5] | High that no mandate exists |
| Morocco | Press claim of a circular for public projects above 50 M MAD (unverified) | Ministry of Equipment and Water (claimed) | marocbtp article dated 1 July 2025 [19] | Low |
| Ethiopia | Planned requirement for large public projects (above 250 M Birr), not confirmed in force | Construction Management Institute, Institute of Ethiopian Standards, Ministry of Urban and Infrastructure | Addis Fortune report [12] | Low-medium |
| Kenya | National BIM policy framework planned | State Department for Public Works; NCA; NHC | Conference 28 March 2025 [8] | Medium that it is only planned |
| Nigeria | None; academic roadmap and advocacy only | BIM Africa (private), RGU research | 2019 roundtable; ThisDay July 2025 says no public-project mandate [9][10][11] | High that no mandate exists |
| Rwanda | No BIM rule found; e-permit system KUBAKA (BPMIS 2.0) launched ~30 April 2025 | Rwanda Housing Authority | No 3D/BIM submission requirement mentioned [22] | Medium |
| Ghana | None; low adoption; no policy framework | - | KNUST studies [24] | Medium |
| Algeria | None found; IANOR standards are voluntary | IANOR | Decree 98-69 (IANOR) [25] | Low (search was thin) |
| Tunisia | None found; "isolated initiatives" | - | archibat article, 2018 ULiege presentation [26] | Low-medium |
| Senegal | None found | - | No BIM text found [27] | Low |
| Angola, Mozambique, Cabo Verde | None found; academic studies say early stage | - | Minho dissertation [28] | Low |
| Zambia, Tanzania, Uganda, Mauritius | Nothing verified; BIMobject lists Tanzania among countries with initiatives (unverified) [32][33] | - | - | Low |

---

## 2. South Africa

### 2.1 Who and what
- **CIDB** (Construction Industry Development Board, a statutory body under the Department of Public Works and Infrastructure) leads national BIM policy. In 2023 it began drafting a national BIM policy aiming for gazetting by end-2025 [4]. In May 2026 it still reported being "on track" with a 2022 phased roadmap, and was finalising a BIM Strategy before forming a Steering Committee and Working Groups; no gazetted policy is evident as of the 6 May 2026 workshop [3]. The 2025 target therefore appears to have slipped (the workshop page does not say so explicitly).
- **SABS** (South African Bureau of Standards) runs the SANS (South African National Standards) process. Per BIM Community Africa [2]:
  - SANS 19650-1: approved without changes on 16 September 2022.
  - SANS 19650-2: published 5 June 2023, apparently identical to ISO 19650-2; it was to be accompanied by a **National Annex** adapting terminology and process to South African contracts.
  - SANS 19650-3: public comment closed 25 May 2023 and approval was expected shortly (current status not verified).
  - SABS Technical Committee 59 (Construction Standards) declined the work; **TC 267 (Facilities Management)** took it over.
  - As of May 2026, the CIDB "intends to lead" drafting of the National Annex; whether it has been published is not confirmed [3].
- **BIM Institute** (biminstitute.org.za): non-profit describing itself as "Africa's official voice for BIM", software-agnostic, publishes a National BIM Guide and training [1][7]. Its status is self-described; it is not a government body.
- **BIM Community Africa / BIM CoDE-SA**: an industry convention series ("Convention for a Digital South Africa") that supports CIDB policy work and held its 8th workshop on 6 May 2026 on SANS 19650 [3][4].
- Procurement: a 2025 peer-reviewed policy review states that public clients "recommend" rather than "require" models, that National Treasury PPP rules are model-agnostic, and that no Treasury directive hard-codes IFC deliverables [5]. It recommends (not adopted) amending the PPP Manual and Treasury Regulation 16A.3.1 to require ISO 19650/IFC federated models and COBie handover [5].
- Adoption data from that review: about 15% of firms produce federated models; the paper classes the country at BIM Stage 0-1. Some figures in its recommendation section cite an unpublished Treasury baseline (unverified) [5].
- An Engineering News opinion piece (September 2026) argues BIM must become a national mandate and cites a survey where 81% of respondents said a mandate from the National Department of Public Works is needed (seen via search summary only; the page itself returned 403) [6].

### 2.2 IFC-specific requirements
None official. IFC enters through private clients, ISO 19650 EIRs, and international funders. Typical practice (general knowledge, not from a South African primary source): IFC 2x3 Coordination View or IFC4 Reference View for coordination, COBie for handover.

### 2.3 Local georeferencing (general knowledge, unverified in this session)
South Africa uses Hartebeesthoek94 with Lo (longitude-belt) systems, e.g. "Hartebeesthoek94 / Lo29" (EPSG:2053 (unverified)). In IFC4 this maps to `IfcProjectedCRS` + `IfcMapConversion`; IFC2x3 has no such entities (use `ePSet_MapConversion` property-set convention or note coordinates in a Pset).

### 2.4 Classification
No national classification system adopted for BIM was found. SANS 1200 (civil works) and the SANS 10400 building regulations are the existing code frameworks (names from general knowledge, unverified here).

---

## 3. Egypt

### 3.1 Timeline of documents
| Year | Item | Status |
|---|---|---|
| June 2018 | Egyptian BIM Code drafted via HBRC, described as based on British codes and guidance [16][18] | Voluntary guidance |
| 2020 | Ministerial Decision No. 62 of 2020: trial use ("تجريبي") of the Egyptian code for building information models; the code is not binding until updated and a decision issued [13] | Trial |
| 2020 | "Egyptian BIM Code v2" circulated (hosted as a resource on GlobalBIM by Luqman Academy, a training provider, not an official issuer) [17] | Guidance |
| 15 March 2025 | Press (Watan Raqami) reports a Housing Ministry decision, quoted as "No. 30 of 2025", requiring consultants, engineering offices and developers to apply BIM per new Egyptian standards [14][15] | Number unverified; conflicts with item below |
| 10 May 2025 | **Decision No. 302 of 2025** of the Minister of Housing, Utilities and Urban Communities adopting the "Egyptian Guidance Standards for Building Information Modeling" (المعايير الإرشادية المصرية لنمذجة معلومات البناء), published in Waqa'i Misriyya issue 103 [13] | Primary decision text read via news summary |

Decision 302/2025 details [13]: Article 1 adopts the standards; Article 2 tasks HBRC with publishing them, introducing them and providing training; Article 3 sets effect from the day after six months from publication (computed as 11 November 2025) and assigns implementation to the competent authorities each within its remit. The decision text itself names no thresholds or penalties.

### 3.2 What practitioners report [15] (interview, community/press)
- Phased approach: an initial non-mandatory period with a government electronic platform for technical support; then new projects (major and government first); then BIM models for existing strategic facilities (hospitals, universities, airports, large hotels, utilities, main infrastructure). No dates given.
- Standards referenced as studied: ISO 19650, BS 1192, PAS 1192, CIC Hong Kong 2022, Singapore's integrated system; COBie mentioned for operations handover; includes "10D BIM" concept. The interview does not mention IFC or LOD.
- The New Administrative Capital (renamed "The New Capital" in November 2025) reportedly applied BIM in its government district [14].
- Obliged parties: consulting bodies (الجهات الاستشارية), engineering offices (المكاتب الهندسية), real estate developers (المطورين العقاريين) [15].

### 3.3 Not verified
Exact IFC version/MVD, naming convention, classification (Uniclass/Omniclass?), submission portal URL. If asked, the correct answer is: "The decision adopts guidance standards; I could not verify IFC-specific clauses."

### 3.4 Organizations
HBRC (المركز القومي لبحوث الإسكان والبناء), under the Ministry of Housing; Egyptian Engineers Syndicate (نقابة المهندسين) hosts BIM training/events per recruitment-site text (weak evidence). No Egyptian buildingSMART chapter or "Egyptian BIM Society" was found.

---

## 4. Morocco

- **buildingSMART Morocco**: listed in the buildingSMART chapter directory as a "Developing Chapter"; Morocco's application was approved in June 2022, making Africa a chapter continent [20]. Operating organization is reported as "My African Competition (M.A.C.)", founded 2018 (from a search summary; unverified). buildingSMART held its International Summit in Marrakesh, 1-3 October 2024, billed as its first in Africa, with the openBIM Awards ceremony on 3 October at Beldi Country Club [21].
- **Public-procurement mandate claim**: a Moroccan construction news site (marocbtp, 1 July 2025) says the Ministry of Equipment and Water issued a circular making BIM compulsory for public projects above 50 M MAD, with phases: >100 M MAD in 2025-2026, 50-100 M MAD in 2027, all public construction 2028-2030; tenders to include BIM requirements and bidders to show certified BIM skills [19]. The article gives no circular number, date or link, and its own introduction and timeline conflict. Treat as **unverified**. My Arabic and French searches of ministry and procurement pages found no corroboration.
- General procurement framework: Decree No. 2-22-431 of 8 March 2023, in force 1 September 2023 (reform of public procurement) [36]; no BIM clause was confirmed in it.
- Press context: BIM is "far from democratised", mainly imposed by foreign clients because of cost barriers [36]; drivers cited include the 2030 World Cup and development-bank pressure [19].
- Georeferencing (general knowledge, unverified): Merchich / Lambert Nord Maroc (EPSG:26191).

---

## 5. Nigeria, Kenya, Ethiopia, Rwanda, Ghana

### Nigeria
- No federal BIM mandate. ThisDay (26 July 2025): Nigeria "has yet to mandate BIM on public projects"; calls on professional bodies (NIA, CORBON, NIQS) to embed BIM in licensure [9].
- **BIM Africa** (private, Abuja-based organisation running summits, awards, roundtables) hosted a National BIM Roundtable at the Sheraton, Abuja, in July 2019, sponsored by Autodesk, themed "Charting a Unified Consensus Towards a Nigerian BIM Mandate" [10]. No outcome document found.
- Academic: Hamma-Adama and Kouider (Robert Gordon University) produced a seed national BIM policy framework and a six-year roadmap (research, not adopted policy) [11].
- Georeferencing (general knowledge, unverified): Minna / Nigeria West Belt (EPSG:26391).

### Kenya
- State Department for Public Works held the "Digital Information Management for Public Sector Conference" on 28 March 2025, with NHC, NCA and the State Departments for Transport and Roads; facilitated by Autodesk (Africa lead and Kenya country manager) and WorldsView Technologies. It states the department expects to develop a **National BIM policy framework**; no date or publication found [8].
- NCA (National Construction Authority) is governed by the National Construction Authority Act, revised 2018, and is developing a new industry policy (BIM not confirmed in it). Academic papers recommend integrating BIM with existing e-permit systems; no Kenyan IFC rule or BIM association was found.

### Ethiopia
- Addis Fortune reports a plan requiring BIM software on large public projects above 250 million Birr, with the Construction Management Institute spearheading, the Institute of Ethiopian Standards finalising national BIM implementation guidelines and the Ministry of Urban and Infrastructure preparing regulations. Pilots: National Theatre (Gambia Street), a diplomat housing development, and Oromia Construction Authority projects [12]. The article date is inconsistent in tool output (search header shows 6 Sep 2020; the fetched text implies 4 May 2024 with a start "next year"); treat timing as **unverified** and enforcement as unconfirmed.

### Rwanda
- RHA (Rwanda Housing Authority, established by Law No. 40/2010) with the World Bank Group's IFC (International Finance Corporation, not the data schema) designed BPMIS in 2016; **KUBAKA** is the upgraded platform (BPMIS 2.0) launched around 30 April 2025 [22][23]. No BIM, 3D or IFC upload requirement was found. A BIM Africa announcement appointed a local lead to introduce BIM in Rwanda (press).
- Pitfall: "IFC Rwanda" in search results usually means the International Finance Corporation.

### Ghana
- KNUST studies show low adoption (about 7% of consultants in one study) and "Pre-BIM capable" readiness; absence of policy named as a barrier [24]. No Ministry of Works and Housing BIM instrument found.

---

## 6. Francophone and Lusophone Africa

- **Algeria**: IANOR (national standards institute) was created by Decree 98-69 of 21 February 1998; standards are voluntary unless made mandatory by a ministry [25]. No BIM standard or Housing Ministry BIM rule found.
- **Tunisia**: a 2025 industry article says BIM is emerging through isolated initiatives and calls for ministries to regulate [26]; a 2018 ULiege presentation lists a national BIM strategy and BIM-specific legal tools as stakes, not adopted [26]. No decree found.
- **Senegal**: Urbanism Code (Law 2008-43, plus a reported 2023 revision, unverified) and AGEROUTE tenders reviewed; no BIM provisions found [27].
- **Angola / Mozambique / Cabo Verde**: academic work says BIM is at an initial stage; no obligations [28]. (Portugal's licensing obligation under Lei 50/2023 is Europe, not applicable here.)

---

## 7. IFC and technical context for testing

(Items in this section are general openBIM knowledge, not African-specific findings; verified only partly.)
- IFC4.3 is ISO 16739-1:2024 [29]. IFC 2x3 (Coordination View 2.0) and IFC4 (Reference View, Design Transfer View) are still what African projects exchange in practice; IFC4.3 matters for roads/rail/ports.
- Revit export: File > Export > IFC; Revit 2023 and later use the open-source IFC exporter (Autodesk/revit-ifc on GitHub); settings include IFC version, file type, "Export base quantities", "Export Revit property sets" (unverified here).
- Typical EIR items on African international-funder projects (illustrative): IFC 2x3 or IFC4 RV, COBie 2.4 sheets, Pset_WallCommon IsExternal/FireRating, georeferenced to the national CRS, file naming per ISO 19650-2 (`Project-Originator-Volume-Level-Type-Role-Number`).
- Test ideas: ask an MCP to read `IfcSite.RefLatitude/RefLongitude` and `IfcMapConversion`; check for missing `IfcProjectedCRS` for Lo29/UTM; validate Arabic or French text in `Name`/`Description` (IFC STEP encodes non-ASCII with `\X2\...\X0\`).
- Classification: no national BIM classification system verified in any of these countries; Egypt's decision may reference one (unverified).

---

## 8. Key organizations and ecosystem

| Organization | Country | Type | Note |
|---|---|---|---|
| CIDB | South Africa | Statutory | Leads national BIM policy [3][4] |
| SABS (TC 267) | South Africa | Standards | SANS 19650 series [2] |
| The BIM Institute | South Africa / Africa | NPO | National BIM Guide, training [1][7] |
| BIM Community Africa / BIM CoDE-SA | South Africa | Industry network | Workshops since July 2023 [3][4] |
| BIM Africa | Nigeria / Africa | Private | Summits, roundtables [10] |
| HBRC | Egypt | Research center | Publishes and trains on standards [13] |
| buildingSMART Morocco | Morocco | Developing chapter | Hosted 2024 summit city [20][21] |
| Institute of Ethiopian Standards | Ethiopia | Standards | BIM guidelines (planned) [12] |
| Autodesk | Pan-African | Vendor | Sponsored Nigeria roundtable, Kenya conference, SA white paper [4][8][10] |

Software: Autodesk Revit/Navisworks/Civil 3D dominate in what was found; ArchiCAD and Tekla are mentioned in Nigerian curricula [9]. I found no African open-source BIM/IFC projects or enthusiast communities beyond the associations above (gap).

---

## 9. Local terminology

| Native term | Transliteration | English |
|---|---|---|
| نمذجة معلومات البناء | namdhajat ma'lumat al-bina' | Building Information Modeling |
| المعايير الإرشادية المصرية | al-ma'ayir al-irshadiyya al-misriyya | Egyptian guidance standards |
| الكود المصري لنمذجة معلومات البناء | al-kud al-misri | Egyptian BIM Code |
| المركز القومي لبحوث الإسكان والبناء | - | HBRC |
| الوقائع المصرية | al-waqa'i' al-misriyya | Egyptian Official Gazette |
| الجهات الاستشارية / المكاتب الهندسية | - | consulting bodies / engineering offices |
| المطورين العقاريين | al-mutawwirin al-'aqariyyin | real-estate developers |
| maquette numérique / modélisation des informations du bâtiment | - | BIM model / BIM |
| marchés publics | - | public procurement |
| cahier des charges BIM | - | BIM specification / EIR |
| circulaire | - | ministerial circular |
| BIM Execution Plan (BEP) / Plan d'exécution BIM | - | project BIM plan |
| modelagem da informação da construção | - | BIM (Portuguese; Portugal also uses "modelação") |
| Birr | - | Ethiopian currency |

---

## Typical questions people ask about this

1. Is BIM mandatory in South Africa? (illustrative; answer: no statutory mandate, CIDB policy pending [3][5])
2. Has the CIDB published its national BIM policy? (illustrative [4])
3. Is SANS 19650 the same as ISO 19650? (illustrative; parts 1 and 2 appear unchanged, with a National Annex planned [2])
4. How best do we fast-track BIM adoption in Nigeria: a mandate, a nudge or academia? (from the 2019 BIM Africa roundtable theme [10])
5. Does Nigeria have a BIM mandate for public projects? (illustrative [9])
6. Is BIM mandatory in Egypt under Ministry of Housing Decision 302/2025? (illustrative [13])
7. From when does the Egyptian BIM guidance take effect? (illustrative; computed 11 Nov 2025 [13])
8. Who must comply in Egypt: developers, engineering offices, consultants? (illustrative [15])
9. Is there a Moroccan circular requiring BIM above 50 million MAD? (illustrative; unverified [19])
10. Which Moroccan ministry regulates BIM in public tenders? (illustrative)
11. Does Kenya have a national BIM policy? (illustrative [8])
12. Does Ethiopia require BIM on projects above 250 million Birr? (illustrative [12])
13. Does Rwanda's KUBAKA platform accept BIM or IFC models? (illustrative [22])
14. Which IFC version should I deliver on an African project? (illustrative; depends on EIR)
15. How do I georeference an IFC for Lo29 or UTM 36N? (illustrative)
16. Is there an African buildingSMART chapter? (illustrative [20])
17. Which classification system should I use in Africa? (illustrative)
18. How do I export Arabic names from Revit to IFC without broken characters? (illustrative)
19. Does South Africa's Treasury require IFC deliverables? (illustrative; no, per [5])
20. Where can I find the Egyptian BIM code? (illustrative; the code is hosted by training sites, official HBRC distribution not verified [17])

---

## Common pitfalls and misconceptions

- "IFC" ambiguity: in African news, IFC often means the International Finance Corporation (e.g., Rwanda's permit system funding) [22].
- Assuming "Egyptian BIM Code" is binding. The 2020 code was a trial; Decision 302/2025 adopts guidance standards with a transition [13].
- Conflicting decision numbers for Egypt (30 vs 302 of 2025); only 302 has gazette details [13][15].
- Treating the Moroccan 50 M MAD threshold as official; it comes from a single unreferenced article [19].
- Assuming ISO 19650 adoption equals a mandate: SANS 19650 is a voluntary standard [2][5].
- Treating GlobalBIM or Luqman Academy listings as official issuers [16][17].
- Assuming blog or press timelines (for example Ethiopia) are enacted [12].
- Search results on "BIM mandate" often return UK/France/Lithuania items; do not transpose them to Africa.

---

## Gaps

- Search budget exhausted; not researched: Mauritius, Tanzania, Uganda, Zambia in depth, Libya, Sudan, Cameroon, Cote d'Ivoire, DRC.
- Primary pages that returned 403 (buildingSMART chapter and IFC pages, Engineering News, AllAfrica) were relied on via search summaries.
- No official text found for: Moroccan circular, Egyptian decision full text, Kenya framework, Ethiopian guidelines, CIDB policy draft, SANS 19650-3 and national annex status.
- No local open-source or enthusiast IFC projects found.
- Skipped as non-official or commercial: Scribd/SlideShare copies of codes, a retail store selling the Egyptian code, and recruitment/aggregator pages (cited only as weak context).

---

## Sources

[1] https://globalbim.org/news/info-country/south-africa
[2] https://www.bimcommunity.africa/post/update-on-iso-19650-as-a-sans-in-june-2023
[3] https://www.bimcommunity.africa/workshop-8-advancing-bim-implementation-through-sans19650
[4] https://it-online.co.za/2023/09/18/sa-built-environment-closer-to-adopting-national-bim-code/
[5] https://www.frontiersin.org/journals/built-environment/articles/10.3389/fbuil.2025.1685353/full
[6] https://engineeringnews.co.za/article/if-infrastructure-is-the-priority-bim-must-become-a-national-mandate-2026-09-02 (search summary only)
[7] https://www.biminstitute.org.za/ and https://globalbim.org/info-collection/bim-institute-website/
[8] https://publicworks.go.ke/node/310
[9] https://www.thisdaylive.com/2025/07/26/building-information-modelling-key-to-solving-nigerias-construction-crisis
[10] https://bimafrica.org/tag/roundtable/
[11] https://rgu-repository.worktribe.com/OutputFile/244513
[12] https://addisfortune.news/fed-ponders-mandatory-construction-software-for-large-public-projects
[13] https://www.almasdar.com/155662
[14] https://watanraqami.com/%D8%AA%D9%81%D8%A7%D8%B5%D9%8A%D9%84-%D9%82%D8%B1%D8%A7%D8%B1-%D9%86%D9%85%D8%B0%D8%AC%D8%A9-%D9%85%D8%B9%D9%84%D9%88%D9%85%D8%A7%D8%AA-%D8%A7%D9%84%D8%A8%D9%86%D8%A7%D8%A1-bim/
[15] https://watanraqami.com/%D8%AD%D9%88%D8%A7%D8%B1-%D9%88%D8%B7%D9%86-%D8%B1%D9%82%D9%85%D9%8A-%D8%B9%D9%86-%D9%86%D9%85%D8%B0%D8%AC%D8%A9-%D8%A7%D9%84%D8%A8%D9%86%D8%A7%D8%A1-bim/
[16] https://globalbim.org/info-collection/egyptian-bim-code-2018/
[17] https://globalbim.org/info-collection/egyptian-bim-code-v2-2020/
[18] https://pmo-eng.blogspot.com/2023/09/egyptian-code-for-building-information.html (community blog)
[19] https://www.marocbtp.com/news-bim-obligatoire.html
[20] https://www.buildingsmart.org/community/chapter-directory/buildingsmart-morocco/ (search summary only)
[21] https://www.buildingsmart.org/the-buildingsmart-openbim-awards-2024-winners-announced/
[22] https://www.newtimes.co.rw/article/26114/news/featured/rwanda-launches-upgraded-building-permit-platform-revised-national-urbanisation-policy
[23] https://bpmis.gov.rw/downloads/eBPMIS_Clients_User_Manual.pdf
[24] https://ir.knust.edu.gh/handle/123456789/10181
[25] https://www.ianor.dz/wp-content/uploads/2023/02/2-D_exe_98-69_instituant-IANOR-FR.pdf
[26] https://archibat.info/le-bimune-necessite-incontournable-pour-lavenir-de-la-construction and https://orbi.uliege.be/bitstream/2268/226575/1/180511_implementation%20du%20BIM%20en%20Tunisie_D2.pdf
[27] https://lesoleil.sn/opinions/point-de-vue/la-construction-au-senegal-face-aux-defis-du-numerique-et-de-lia/
[28] https://repositorium.sdum.uminho.pt/bitstream/1822/70337/1/Disserta%c3%a7%c3%a3o%20Chiamba%20Ricardo%20Chiteculo%20Canivete.pdf
[29] https://technical.buildingsmart.org/standards/ifc/ (search snippet)
[32] https://business.bimobject.com/resources/bim-mandates-guide-for-manufacturers (search snippet)
[33] https://research.mu.ac.zm/research/index.php/mu/article/download/234/90
[36] https://www.lavieeco.com/?p=171952 and https://www.labase-lextenso.fr/l-essentiel-droits-africains-des-affaires/2023-n6/maroc-un-nouveau-decret-relatif-aux-marches-publics-DAA201q5
