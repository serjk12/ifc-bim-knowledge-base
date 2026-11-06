# Kazakhstan, Belarus, Uzbekistan, Caucasus, Central Asia: BIM/ТИМ and IFC

**Last researched: 2026-11-06**

## In plain words

In this region the only country with a binding, dated BIM mandate is **Kazakhstan**. There the local term for BIM is **ТИМСО** (технология информационного моделирования строительных объектов). Order No. 114 of the Minister of Industry and Construction (19 March 2026) lists the object types that must use ТИМСО, and the first group became mandatory on 1 August 2026 [1][2][3]. **Belarus** has had paper mandates since 2019 (Council of Ministers Resolution No. 296) but, as of an October 2025 official quote, still has almost no real BIM customers [4][5]. **Uzbekistan, Kyrgyzstan, Armenia, Georgia, Azerbaijan, Tajikistan** show roadmaps, conferences, pilot projects and university work, but I found **no confirmed binding BIM or IFC mandate** (details and gaps per country below). For a QA tester: Kazakhstan is where "BIM + IFC + state expertise" requests are realistic. Elsewhere, expect models in Revit, ArchiCAD, Renga or nanoCAD with Cyrillic names, exported to IFC, with no national IFC profile. Where a regional doc exists it mostly says "open format IFC" and nothing more specific.

Evidence quality warning: many facts below come from news items, vendor blogs and search-result summaries, not from the legal texts. The adilet.zan.kz (Kazakhstan legal portal) pages returned only a site header to the fetcher, so **I could not read the text of Order No. 114 or any СП РК/СН РК in full**. Anything about their internal clauses is marked (unverified).

---

## 1. Kazakhstan

### 1.1 Who and what

| Body | Role |
|---|---|
| Ministry of Industry and Construction (Минпромстрой, МПС РК) | Issues the mandate order, hosts policy meetings, publishes news at gov.kz [1][6] |
| RSE "Gosexpertiza" (РГП «Госэкспертиза») | State expertise of design documentation, now reviews information models; has a BIM development department [1] |
| JSC KazNIISA (КазНИИСА), Information Modeling Center (Центр науки и цифровизации строительства) | Wrote the Concept and the СН РК/СП РК set; member of buildingSMART International; runs buildingSMART certification training [7][8] |
| Qportal (qportal.kz, "Единый портал") | Submission portal for design documentation; named in 2026 as the common data environment (СОД) for ТИМСО [1][3] |
| Ministry of Digital Development | In May 2025 proposed BIM at all lifecycle stages plus one digital platform for construction and the urban-planning cadastre; no legal act cited [9] |

### 1.2 Timeline of official acts

| Date | Document | Content |
|---|---|---|
| 11 Apr 2017 | Order No. 197 of the Minister for Investments and Development (amended by Order No. 139, 27 Feb 2018) | Action plan for introducing BIM in design of construction objects; includes a task to develop a BIM-oriented classifier [7][10] |
| 2017-2019 | КазНИИСА set of СН РК/СП РК (see 1.4) | Process standards for design, expertise, lifecycle [7] |
| 1 Jan 2018 (press) | Concept of introducing ТИМСО (draft) | Planned: trial until 31 Dec 2019, mandatory for technically complex budget projects from 2020 (press plan, not a confirmed legal date) [11] |
| 3 Oct 2024 | Roundtable at the Ministry | Participants backed revising the Concept; vice-minister asked to add operation stage, ML data accumulation and "сквозная классификация" (cross-cutting classification) [6] |
| 9 Jan 2026 | Construction Code of RK No. 253-VIII, in force 1 Jul 2026 | Cited only by a vendor blog (unverified); the blog says it is the main lifecycle document [12] |
| 19 Mar 2026 | **Order No. 114** of the Minister of Industry and Construction | List of construction object types where ТИМСО is mandatory. Full text: adilet.zan.kz/rus/docs/G26IS000114 (not readable by me) [2][3] |
| 1 Jul 2026 | Order enters into force; phased transition | Per Gosexpertiza news item of 22 Apr 2026 [2] |
| 1 Aug 2026 | Phase 1 object list starts to apply | [1][2][3] |
| 29 Jul 2026 | Expert meeting "Обязательный BIM в Казахстане", Astana | Organized by ТОО "CAD системы" with Gosexpertiza speaker [1] |

### 1.3 Scope and thresholds of Order No. 114

Official title as quoted by the Ministry: «Об утверждении Перечня строительных объектов, при создании и эксплуатации которых обязательно применение ТИМСО» (one source adds "видов" after "Перечня") [1][3].

| Phase | Start | Objects | Sources |
|---|---|---|---|
| 1 | 1 Aug 2026 | General-education schools (gymnasiums, lyceums) for **600+ pupils**; airports, passenger terminals and other aviation infrastructure; railway and road tunnels and metro; bridges **100 m or longer** on roads of all categories; unique construction objects | [2][3][13] |
| 2 | 1 Jan 2028 | Sources disagree. Bizmedia: healthcare and education objects; engineering, transport, energy, oil and gas infrastructure. Orda.kz: kindergartens with 95+ places, boarding schools, university campuses, residential and public buildings of 3-6 floors; plus energy, oil and gas, transport and healthcare with no date | [14][15] |
| 3 | 1 Jan 2030 | All construction objects except technically simple objects of responsibility level III (третий уровень ответственности) | [14][15] |

Applies to projects whose development starts after the dates above; reconstruction and capital repair are included [14]. **The phase-2 composition is not settled in my sources; do not state it as fact. Check the order text.**

Other reported rules:

- No fines are provided; incomplete documentation is rejected at expertise with notification to the customer [14].
- Pricing coefficient **1.2** applies to the cost of the design sections developed with information modeling, not to the whole project (ПСД) [14].
- Expertise cannot be done on a model alone; model and drawings are reviewed together and cross-checked. Refusing drawings is "impossible at this stage" per the Ministry [14].
- Qportal does not yet automatically block submissions without a model; moderators and expert staff screen manually [14].
- Design documentation for covered objects must be submitted according to **СП РК 1.02-117-2018** (the procedure for expertise of information models); the ТИМСО standards list is on Qportal [2].
- Gosexpertiza notes the workload of experts rose during pilots; cases of model/drawing divergence were found [14].

### 1.4 The КазНИИСА standards set

Listed on the KazNIISA site as "Building codes of the Republic of Kazakhstan" (СН РК or СП РК; the site says "building codes" and the exact prefix per document should be checked on adilet) [7][8]:

| Number | Year | Title (English as published; Russian paraphrased) |
|---|---|---|
| РДС РК 1.02-04-2018 | 2018 | Concept-level guidance document for information modeling (listed as "RDS RK 1.02-04-2018") |
| 1.02-111-2017 | 2017 | Application of information modeling in a design organization (на русском: Применение информационного моделирования в проектной организации; also called the organization standard for ТИМСО) [16] |
| 1.02-112-2018, 1.02-113-2018, 1.02-114-2018 | 2018 | Life cycle of construction projects, parts 1, 2, 3 (Жизненный цикл строительных объектов) |
| 1.02-115-2018 | 2018 | Rules for organizing joint creation of information (Среда общих данных, CDE) |
| 1.02-116-2018 | 2018 | Requirements for design of project documentation |
| 1.02-117-2018 | 2018 | Procedure for the examination of information models |
| 1.02-119-2019 | 2019 | Life cycle, part 5: requirements for models at operation stage |
| 1.02-121-2019 | 2019 | Application of information modeling in the operating organization |
| (no number found) | 2019 | Life cycle part 4 (construction stage) and application in a construction organization |

Notes: 1.02-118 and 1.02-120 were not listed [8]. The КазНИИСА page says these documents "currently allow ТИМСО at the design and expert review stages" and does not itself mention IFC or a classifier [7][8]. The 1.02-111-2017 text on adilet reportedly references ISO 16739:2013 (IFC), via a secondary description [16]. Whether the 2018 docs are still in force after the 2026 Construction Code is (unverified).

### 1.5 IFC-specific requirements

- Policy: the state does not tie participants to specific software. The program must create and export the model in open **IFC** format, which is what goes to expertise. Free and Kazakh developments are acceptable [14].
- Gosexpertiza's March-July 2026 communications cite IFC advantages but the pages I read give **no IFC version, no MVD, no property-set list, no naming rule and no georeferencing rule** [1][2]. Treat all of these as (unverified / not found).
- Structure and content of the "электронная модель строительного объекта" (ЭМСО) are said to be defined, and the customer sets "ИТЗ" (информационные требования заказчика) [1]; details not found.
- Classifier: the 2017 action plan tasked a BIM-oriented classifier harmonized with the resource-method classifier; a "ТИМСО-классификатор 2018 scope" is listed as a deliverable [7][8][10]. In 2024 the vice-minister still asked for a "сквозная классификация", so no single final national classifier is confirmed [6]. The SD Soft blog says attributes must link to "a classifier" but does not name it (unverified) [12].
- Estimating (сметы): the cad.kz seminar (7-11 Sep 2026, Astana, organizers ТОО АВС-К and Лайнпрактик) says quantities from the model are converted to estimate form and exported in **KENML 2.0** format. Software listed there: Revit, Renga, Allplan, ARCHICAD, IndorCAD/Road, MagiCAD, nanoCAD, AVEVA E3D, Model Studio CS, ТИМ-Кредо, Топоматик Robur [17].

### 1.6 Organizations

- **buildingSMART Kazakhstan**: approved by buildingSMART International as a **Developing Chapter** in March 2024, host KazNIISA (from search-result summaries of buildingsmart.org; the chapter page itself returned 403 to the fetcher) [18].
- KazNIISA Information Modeling Center (also "Центр науки и цифровизации строительства"): standards, audits, training, "e-qurylys" IT systems [7].
- ТОО "CAD системы" (cad.kz): reseller/integrator that organizes the market meetings (commercial) [1][17].
- SD Soft (sdsoft.kz): Autodesk/Nemetschek reseller blog (commercial) [12].
- Gosexpertiza: expertise practice presentations [1][6].

### 1.7 Local ecosystem

Revit, ArchiCAD, Allplan, Tekla and Bentley have long been used; IndorCAD (IndorSoft) road BIM was in use in KZ since the early 2000s per a 2014 meeting at the Ministry of Regional Development (then also promoted 5D/6D modules; the ABC estimating system with Allplan was tested on a 40-apartment house in Astana) [19]. Russian software (Renga, nanoCAD, Model Studio CS, Credo, Topomatic) is part of the vendor mix at Kazakh training events [17].

---

## 2. Belarus

| Item | What I found |
|---|---|
| Standards committee | Standardization work started in 2015; subcommittee ПК-5 (BIM) under ТК-465 "Строительство"; first national standards based on ISO 12911, 16739, 12006 (a conference paper, not an official page) [20] |
| Adopted standard | **СТБ ISO/TS 12911-2015** "Basic guidance on BIM" (introduced 28.08.2015) [21] |
| Government acts | Ministry of Architecture and Construction (Минстройархитектуры) Order No. 70 of 16 Mar 2018 "on the introduction of BIM technology"; President's Directive No. 8 (4 Mar 2019); Council of Ministers Resolution No. 296 (14 May 2019) [21] |
| Mandates in Res. 296 | By December 2019: mandatory BIM for construction fully or partly financed from republican or local budgets; by January 2022: for other construction (as quoted by a 2020 university paper) [21] |
| Reality in 2025 | Deputy Minister of Communications Anton Alekseev (INNOPROM.Belarus, 8 Oct 2025): "almost no BIM clients in Belarus because it is complex" [5] |
| Pilots | 23 pilot projects were selected in the plan; Belarusfilm production building (Belpromproekt) and Dynamo stadium reconstruction (Minskproekt) are named [20][21] |
| Russia link | June 2023: Rosatom's Tsifrum and OTsKS signed cooperation with the Republican Union of Builders (Республиканский союз строителей) and RNTC CS on harmonizing information-modeling standards; Belarus was interested in Rosatom's Multi-D products [4] |

I did **not** verify: a Belarus ТКП on information modeling, СТБ ISO 16739 or СТБ ISO 19650 adoption, or a Belarus-specific IFC/MVD/classification requirement. The task brief suggested "ТКП/СТБ on information modeling": only the СТБ ISO/TS 12911-2015 above was confirmed. (unverified) for anything else. The ТКП 45-1.02-295-2014 (composition of project documentation) is confirmed but is not a BIM standard [21].

Software named in Belarus literature: Revit, Tekla, Navisworks, Civil 3D, IDEA StatiCa, Credo Dorogi, ABC-RNTS [21].

---

## 3. Uzbekistan

- No BIM decree, resolution or mandate found. A 16 Apr 2024 UzA report from the "Central Asian BIM-TIME" forum (Tashkent) quotes Alizhon Alimukhamedov of the Ministry of Construction and Housing and Communal Services (strategic development department): wide BIM adoption needs a supporting legal framework, and the Kazakh and Russian laws "still need refinement" [22].
- Digital-twin and BIM mentions: Ministry of Construction developing digital twins of Tashkent and Nukus (secondary, ResearchAndMarkets, Oct 2024); UNDP/SRI of Technical Norms trainings on BIM in energy-efficient design, Apr-Jun 2024 [23].
- Related but not BIM: QR-code passports for all construction projects (Kun.uz, Apr 2025, from September) and a ban on design changes to approved residential projects (Dec 2025) [24]. Do not confuse them with a BIM mandate.
- Strategy context named by sources: Digital Uzbekistan 2030, New Uzbekistan Strategy 2022-2026; none linked to BIM by a primary document [23].
- Local agencies likely relevant to future rules (unverified for BIM): Ministry of Construction and Housing and Communal Services; lex.uz is where decrees would appear.
- Market players: BI Construction & Engineering (private developer reporting BIM use on school and residential projects), CAD Systems [22].

---

## 4. Kyrgyzstan

- July 2024: Госстрой (State Committee for Construction) deputy director met a technology distributor; announced a **roadmap for BIM introduction** to be discussed at a roundtable (date not given) [25]. No order number found.
- No mandate, no standard, no IFC rules found.

## 5. Tajikistan

- Nothing found. A 2016 government resolution appeared in a database entry but its relevance to BIM was not visible. (unverified)

## 6. Armenia

- 2 Aug 2019 (NUACA news): the Urban Development Committee approved a BIM implementation roadmap unanimously; a joint working group of the Committee, NUACA and outside experts was proposed; no timeline or legal act in the text [26].
- A LinkedIn interview (not fetched; link was a proxy) reportedly says Armenia lacks BIM regulation; single undated source, (unverified).
- No national BIM/IFC mandate confirmed.

## 7. Georgia

- No BIM mandate found. Georgian-language press (Entrepreneur Georgia) covers private consultancies (BIM Solutions Georgia, "BIM Cube") and a Tbilisi digital-construction forum; it says local architects use ArchiCAD and Revit [27]. These are commercial sources.
- Beware: "Georgia BIM guide" search hits (gsfic.georgia.gov) refer to the **US state**.
- Possible regulatory home (unverified): Ministry of Regional Development and Infrastructure and technical regulations on matsne.gov.ge.

## 8. Azerbaijan

- State Committee for Urban Planning and Architecture backed an international conference on digitalization and BIM on the occasion of 10 April Builders' Day (year not confirmed); the item says more events will follow and conditions for studying/implementing BIM will be created [28].
- A 2021 job posting for a consultant to compile national laws for BIM implementation indicates a framework "being developed" at that time [29].
- The World Bank "B-Ready" construction-permit indicator page lists BIM integration among reform items (does not say compulsory) [29].
- No confirmed mandate.

---

## 9. National classification systems

| Country | Status |
|---|---|
| Kazakhstan | BIM-oriented classifier required by 2017 action plan; "ТИМСО-классификатор 2018" listed as a deliverable; 2024 call for "сквозная классификация". Final national classifier not confirmed [6][7][10] |
| Others | None found. Russian practice (ГОСТ/СП, Russian classifiers) is the reference but is outside this document's scope; see `russia.md` |

International classification tables (Uniclass, OmniClass, bSDD) are not mandated by any of these countries in the sources I read.

---

## 10. Terminology table

| Native term | Transliteration | English |
|---|---|---|
| ТИМ (технологии информационного моделирования) | TIM | BIM (Russian term, also in Belarus) |
| ТИМСО | TIMSO | BIM in Kazakhstan: information modeling technology for construction objects |
| ЭМСО (электронная модель строительного объекта) | EMSO | Electronic model of a construction object |
| ЦИМ (цифровая информационная модель) | TsIM | Digital information model |
| СОД (среда общих данных) | SOD | Common data environment (CDE) |
| ИТЗ (информационные требования заказчика) | ITZ | Employer's information requirements (EIR) |
| Комплексная вневедомственная экспертиза (КВЭ) | KVE | Comprehensive non-departmental expertise |
| Госэкспертиза | Goseksperitiza | State expertise body |
| Среда общих данных | Sreda obshchikh dannykh | Common data environment |
| Уровень ответственности | Uroven otvetstvennosti | Responsibility level (I, II, III) |
| Уникальный объект | Unikalnyi obyekt | Unique construction object |
| ГИП / ГАП | GIP / GAP | Chief project engineer / chief architect |
| ПСД | PSD | Design and estimate documentation |
| Сметы | Smety | Cost estimates |
| Minstroy / Госстрой | Gosstroi | State construction committee (Kyrgyzstan) |

Kazakh-language forms of ТИМСО such as «ақпараттық модельдеу» were not confirmed in sources.

---

## 11. Typical questions people ask about this

Real, from sources (topics the Ministry/Gosexpertiza had to answer):

1. Will there be fines for handing over an object without a digital model? (Ministry: no fines yet) [14]
2. Can expertise be done on the model only, without drawings? (No; both reviewed) [14]
3. Does the 1.2 coefficient raise the whole design price by 20%? (No, only model-based sections) [14]
4. Which software is allowed, and in what format must the model go to expertise? (Any; IFC export) [14]
5. Is there a shortage of BIM specialists and support for small design bureaus? (Ministry did not answer) [14]
6. From which date and for which object types is ТИМСО mandatory? [2][3]
7. How are cost estimates produced from the model? (KENML 2.0 workflow seminar) [17]

Illustrative (invented for testing):

8. (illustrative) Export my Revit school model to IFC for Kazakhstan Gosexpertiza; which IFC version should I choose?
9. (illustrative) Does my 120 m highway bridge fall under Order No. 114 phase 1, and does the date depend on when design started?
10. (illustrative) Check that every IfcWall has a property set with Cyrillic names and flag the missing ones.
11. (illustrative) How do I write ИТЗ (EIR) for a 700-pupil school so the IFC passes expertise?
12. (illustrative) Why does the IFC from Renga/nanoCAD show Cyrillic names as `\X2\...\X0\` escapes?
13. (illustrative) Is BIM mandatory in Uzbekistan for state projects?
14. (illustrative) What is the Belarus equivalent of ТИМСО and which СТБ applies?
15. (illustrative) Which local coordinate system does a Kazakhstan IFC need, and how is IfcMapConversion set?
16. (illustrative) How do I convert quantities from an IFC model to a Kazakh estimate system?
17. (illustrative) Does buildingSMART Kazakhstan offer a certification I can take?

---

## 12. Common pitfalls and misconceptions

- "Kazakhstan requires BIM for everything now." False: Phase 1 only (schools 600+, airports, tunnels/metro, bridges 100 m+, unique objects) from 1 Aug 2026; all except simple level-III objects from 2030 [2][14].
- "IFC version/MVD is fixed by the state." Not found; do not invent one.
- "Fines exist." Not reported; the penalty is expertise rejection [14].
- Sources conflict on the effective date: 1 July 2026 (order in force) vs 1 August 2026 (object list applies) [2][3]. Phase-2 composition also conflicts [14][15].
- Confusing "Georgia BIM guides" with the country; confusing Uzbek QR passports with BIM; confusing the 2018 press plan (mandatory from 2020) with the real 2026 mandate [11][22][24].
- Russian standards (ГОСТ Р, СП 333.1325800) are not Kazakh or Belarusian law, though many documents are harmonized or similar.
- Model plus drawings must agree: Gosexpertiza found divergence in pilots [14].
- Cyrillic: IFC STEP files encode non-ASCII as `\X2\` escapes (general IFC knowledge, not from these sources); tools that mishandle them break property-name checks.

---

## 13. Gaps and honesty notes

- Texts of Order No. 114, СП РК 1.02-117-2018 and the 1.02-111-2017 file were not readable; clause-level requirements (IFC version, property sets, LOD, naming, georeferencing) are not confirmed.
- Search quota ran out; I could not run targeted searches for Uzbekistan (lex.uz), Kyrgyzstan, Azerbaijan (e-qanun.az), Armenia (arlis.am) or Georgia (matsne.gov.ge) after the first pass. A follow-up pass is recommended.
- buildingSMART chapter pages for Kazakhstan and Russia returned 403; chapter status is from search summaries. bSI statement in March 2022 on suspending the Russian chapter was reported by search, not read [18].
- No suspicious or pirated sites were encountered; a proxy-hosted LinkedIn link (meilu1.jpshuntong.com) was skipped deliberately.
- Several sources are vendor or press (SD Soft, cad.kz, yestate.kz, bizmedia, orda.kz) and are labeled as such.

---

## Sources

[1] Ministry of Industry and Construction news, 30 Jul 2026: https://www.gov.kz/memleket/entities/mps/press/news/details/1265869?lang=ru
[2] Gosexpertiza, "С 1 июля 2026 года вводится обязательное применение ТИМСО при экспертизе": https://www.gosexpertiza.kz/node/316107
[3] Order No. 114 full text (not readable by me): https://adilet.zan.kz/rus/docs/G26IS000114
[4] ComNews, 28 Jun 2023, Rosatom and Belarus builders: https://www.comnews.ru/content/227099/2023-06-28/2023-w26/rosatom-i-stroiteli-belorussii-pristupayut-k-garmonizacii-standartov-oblasti-tekhnologiy-informacionnogo-modelirovaniya
[5] Normacs news, 8 Oct 2025, INNOPROM.Belarus: https://www.normacs.info/news/77674
[6] Ministry news, 7 Oct 2024 roundtable: https://www.gov.kz/memleket/entities/mps/press/news/details/860133?lang=ru
[7] KazNIISA Information Modeling Center: https://kazniisa.kz/eng/?p=8587
[8] KazNIISA regulatory documents: https://kazniisa.kz/eng/regulatory-documents
[9] Kursiv/kn.kz, 2 May 2025: https://www.kn.kz/news/56985
[10] GlobalBIM Kazakhstan entries: https://globalbim.org/news/info-country/kazakhstan
[11] Forbes.kz, concept of ТИМСО: https://forbes.kz/articles/progulka_pocherteju_1514532600
[12] SD Soft blog (vendor): https://sdsoft.kz/stati/stroitelnyy-kodeks-rk-2026-bim-timso-obyazatelno/
[13] cad.kz seminar page (confirms Order 114 effective 1 Aug 2026): https://cad.kz/about/news/prakticheskiy-seminar-razrabotka-smet-s-ispolzovaniem-bim-timso-s-7-po-11-sentyabrya-2026-goda-v-g-a
[14] Bizmedia.kz, 29 Sep 2026: https://bizmedia.kz/2026-09-29-czifrovizacziya-napolovinu-pochemu-innovaczii-poka-uslozhnyayut-a-ne-uproshhayut-strojku-v-kazahstane/
[15] Orda.kz, 8 Apr 2026: https://en.orda.kz/schools-bridges-and-power-plants-in-kazakhstan-to-be-built-under-new-bim-rules-10051
[16] Adilet, 1.02-111-2017 (listed in search; text not readable): https://adilet.zan.kz/rus/docs/W17NB312_11/download
[17] cad.kz seminar (software, KENML 2.0): same URL as [13]
[18] buildingSMART Kazakhstan chapter (403, status from search summary): https://www.buildingsmart.org/community/chapter-directory/buildingsmart-kazakhstan/ ; announcement: https://www.buildingsmart.org/iceland-and-kazakhstan-join-buildingsmart-international-as-developing-chapters/ ; Russia: https://www.buildingsmart.org/buildingsmart-russia/
[19] Zakon.kz, 25 Apr 2014: https://www.zakon.kz/redaktsiia-zakonkz/4619613-v-mrr-rk-rassmotreli-vozmozhnosti.html
[20] Normacs conference paper on Belarus standardization (search snippet): https://www.normacs.info/uploads/ckeditor/attachments/1875/korol-doklad.docx
[21] Lazarenko, Yagubkin, Vestnik PSU 2020: https://cyberleninka.ru/article/n/vnedrenie-bim-tehnologiy-v-otrasli-stroitelnogo-kompleksa-respubliki-belarus
[22] UzA, 16 Apr 2024: https://uza.uz/en/posts/nuzhdaetsya-li-stroitelnaya-otrasl-v-cifrovizacii_589343
[23] GlobalBIM Uzbekistan entries: https://globalbim.org/news/info-country/uzbekistan/page/2/
[24] Kun.uz QR passports: https://kun.uz/en/news/2025/04/18/government-to-enforce-qr-code-passports-for-all-construction-projects-from-september
[25] Economist.kg, 15 Jul 2024: https://economist.kg/novosti/2024/07/15/v-kyrghyzstanie-khotiat-vniedrit-bim-tiekhnologhii-v-stroitielnoi-otrasli.md
[26] NUACA news 2019: https://nuaca.am/archives/news/our-university-has-a-major-role-in-the-implementation-of-the-building-information-modeling-bim-in-the-field-of-urban-development/?lang=en
[27] Entrepreneur Georgia (commercial): https://www.entrepreneur.com/ka/zrdis-strategiebi/bim-solutions-georgia-samsheneblo/443793
[28] Azerbaijan SCUPA news (BIM conference): https://arxkom.gov.az/en/media/xeberler/komitesinin-tesebbusu-ve-desteyi-ile-10-aprel-insaatcilar-gunu-erefesinde-tikintide-reqemsallasdirma-bim-texnologiyalarina-hesr-olunmus-beynelxalq-konfrans-kecirilib (fetch failed; from search summary)
[29] Azerbaijan B-Ready reforms page: https://ereforms.gov.az/az/publication/32
[30] Habr, Savelev, IDS checking with ifcopenshell (practitioner blog, Feb 2025): https://habr.com/p/883016
