# Russia: ТИМ/BIM and IFC requirements (very detailed)

## In plain words

In Russia BIM is officially called **ТИМ** (технологии информационного моделирования, "information modelling technologies"). The deliverable is called an **информационная модель объекта капитального строительства** (information model of a capital construction object), often **ЦИМ** (цифровая информационная модель). The state pushes ТИМ through three layers. First, Government decrees (постановления) say for which projects an information model must be formed and maintained. Second, the Градостроительный кодекс (Urban Planning Code) and a set of standards (СП, ГОСТ Р) define terms, process and exchange. Third, state expertise bodies (Главгосэкспертиза, regional expertise bodies) and classifier systems (КСИ in ФГИС ЦС) define what a model must look like when it is submitted. **IFC is the main open exchange format** for models submitted to state expertise [1], and the national IFC standard is the GOST R adoption of ISO 16739. A QA tester should expect Russian users to talk about "ТИМ", "ЦИМ", "экспертиза", "КСИ", "ФГИС ЦС" and "импортозамещение" (import substitution), not about "BIM execution plans" or "LOD/LOI" in the Western sense.

Last researched: 2026-11-06

**IMPORTANT research limitation (read before using this file).** The research tool's web-search budget was exhausted before any search could run, and most primary-source sites (gge.ru, buildingsmart.org, standards.buildingsmart.org, vendor sites) returned 403/404/connection errors from the fetch tool. Only a few Russian Wikipedia pages could be read. Therefore: facts marked **[n]** come from those pages; everything else comes from the author's background knowledge and is marked **(unverified)**. No document numbers, clause numbers or URLs were invented, but unverified numbers must be checked against the official text (publication.pravo.gov.ru, pravo.gov.ru, docs.cntd.ru, minstroyrf.gov.ru, gge.ru) before they are used as test oracles. See "Gaps".

---

## 1. Who mandates what

| Body | Russian name | Role in ТИМ |
|---|---|---|
| Ministry of Construction | Министерство строительства и ЖКХ РФ (Минстрой России) | Main regulator: draft decrees, orders (приказы), classifier (КСИ), technical committee ТК 465 "Строительство" for СП/ГОСТ (ТК 465 is unverified) |
| Ministry of Digital Development | Министерство цифрового развития (Минцифры) | Software registry (реестр российского ПО), class "9.9" for BIM software was proposed in June 2020 [1] |
| Federal Autonomous Institution | ФАУ «Федеральный центр нормирования, стандартизации и технической оценки соответствия в строительстве» (ФАУ ФЦС) | Operator of ФГИС ЦС (federal pricing/classifier system), КСИ operator (unverified), led the 2019 pilot on expertise of a model built in Russian software [1] |
| State expertise | ФАУ «Главгосэкспертиза России» | Federal expertise; receives models for review (see section 5) |
| Regional expertise | Мосгосэкспертиза (Moscow), СПб ГАУ «Центр государственной экспертизы» (St Petersburg, name unverified) | Regional expertise; took part in the pilot [1] |
| DOM.RF | ДОМ.РФ | Ran expert sessions on BIM transition from 26 April 2021 [1] |
| Rosstandart | Росстандарт | Approves ГОСТ Р national standards |
| SRO bodies | НОПРИЗ, НОСТРОЙ | Industry self-regulators; training and positions on ТИМ (unverified details) |

### Timeline of policy (verified items first)

| Date | Event | Source |
|---|---|---|
| 11 June 2016 | List of instructions (перечень поручений) approved to create the legal basis for BIM in construction, mainly for state orders | [1] |
| 19 July 2018 | Presidential instruction **№ Пр-1235**: move to lifecycle management of capital construction objects based on information modelling | [1] |
| late 2019 | Pilot (ФАУ ФЦС): state expertise of an information model made in Russian software; participants included Главгосэкспертиза, Moscow and St Petersburg expertise bodies, NEOLANT, Renga Software, СиСофт Девелопмент, Кредо-Диалог | [1] |
| 1 Jan 2021 | New ГОСТ Р 21.101-2020 (СПДС) in force | [1] |
| 1 Jan 2022 | Government decree: construction must begin transition to ТИМ, with priority for Russian software; Wikipedia gives no decree number [1] | [1] |
| 26 Apr 2021 | First ДОМ.РФ expert session on BIM transition | [1] |

### Government decrees (numbers and dates need checking)

The task brief listed "ПП № 331 (2022)" and "ПП № 1431". My recollection (unverified):

- **Постановление Правительства РФ № 331** — "Об установлении случаев, при которых застройщиком, техническим заказчиком ... обеспечиваются формирование и ведение информационной модели объекта капитального строительства". I recall it is dated **5 March 2021**, not 2022; 2022 is when it started to apply (from **1 January 2022**) to objects financed from budget funds. (unverified: date, title wording, exact exceptions and later amendments, including any postponement of thresholds).
- **Постановление Правительства РФ № 1431** — rules for forming and maintaining the information model, composition of data in the model, and requirements to the formats of electronic documents. I recall it is dated **15 September 2020** (unverified). It is the document that, together with Минстрой orders, fixes that the model is delivered in an open format with IFC and an XML description (unverified).
- **Градостроительный кодекс РФ (ГрК РФ)**: art. 48 includes the term "информационная модель" [1]. The dedicated article on the information model of an object (I recall ст. 57.4 introduced by Federal Law 342-ФЗ of 30.12.2020) and the ГИСОГД articles (ст. 56–57) are unverified.

Scope, as commonly described (unverified): mandatory for new construction/reconstruction financed from budget funds with design and expertise from 1 Jan 2022, with exceptions (e.g. linear objects, objects under state secrecy, some small objects) and a transition for projects already under contract. A tester should not assume ТИМ is mandatory for private projects; it is not, except where a customer or financing contract demands it (unverified).

---

## 2. Standards (СП, ГОСТ Р)

| Document | Title (Russian) | What it is for | Status of verification |
|---|---|---|---|
| СП 333.1325800.2020 | Информационное моделирование в строительстве. Правила формирования информационной модели объектов на различных стадиях жизненного цикла | Rules for forming the model at lifecycle stages; mentions "model is submitted to expertise" workflow | Number and title confirmed [1] |
| СП 328.1325800.2020 | Информационное моделирование в строительстве. Правила описания компонентов информационной модели | Describes model components: element naming, attributes, LOD-like levels ("уровень проработки") | Number from brief; title (unverified) |
| СП 331.1325800.2017 | Информационное моделирование в строительстве. Правила обмена между информационными моделями объектов и моделями, используемыми в программных комплексах | Exchange rules incl. data exchange between BIM and calculation software | Number from brief; title (unverified); check for newer editions |
| СП 301.1325800.2017 | Информационное моделирование в строительстве. Правила организации работ производственно-техническими отделами ... | Construction-stage rules | (unverified) |
| ГОСТ Р 21.101-2020 | Система проектной документации для строительства. Основные требования к проектной и рабочей документации | СПДС basic requirements, in force 1 Jan 2021 | Confirmed [1] |
| ГОСТ Р 10.0.03-2019 / ИСО 16739-1 | Система стандартов информационного моделирования зданий и сооружений. Отраслевые базовые классы (IFC) для обмена и совместного использования данных в строительстве и эксплуатации объектов недвижимости | National adoption of ISO 16739 (IFC) | Number from brief; exact title and ISO part/year (unverified) |
| ГОСТ Р 10.0.x (other parts, e.g. 10.0.01, 10.0.02) | "Система стандартов информационного моделирования зданий и сооружений" series | Basic provisions, information exchange | (unverified) |
| ГОСТ Р 57563 | Модели информационные в строительстве / описание процесса (exact title) | Listed in brief | (unverified) |

As of Q4 2020 Russia had published 16 ГОСТ and 6 СП on information modelling [1]; the count has certainly grown since (unverified current figure). Numbering conventions: "СП nnn.1325800.year" = code of practice, "1325800" is the Минстрой code block; "ГОСТ Р 10.0.xx-year" is the ТИМ standard series.

---

## 3. IFC-specific requirements in Russia

What is reasonably established:

- IFC is the base open format for models submitted to state expertise [1]; the Russian Wikipedia IFC article cites a Russian-language piece titled "Проходим государственную экспертизу в формате IFC" [2].
- Software commonly listed as exporting IFC for Russian workflows: Renga (IFC2x3 and IFC4) [2][3], nanoCAD (IFC2x3, IFC4, IFC4x2; non-authoritative statement) [2].
- IFC versions published (verified list, [2]): IFC2x3 (Feb 2006), IFC4 (Mar 2013), IFC4 Add1 (2015), IFC4 Add2 (Jul 2016), IFC4x1 (Jun 2018), IFC4x2 (Apr 2019, includes IfcBridge). IFC 4.3 documentation lives at standards.buildingsmart.org/IFC/DEV/IFC4_3/HTML/ (the old ifc43-docs host redirects there with HTTP 301) [4]; ISO designation of 4.3 is ISO 16739-1:2024 (unverified).

What I could not confirm (all **unverified**; treat as hypotheses to check in the Минстрой order texts and gge.ru instructions):

- Accepted versions: IFC2x3 and IFC4 are the versions typically named for expertise; IFC4x3 is not expected to be accepted.
- MVD: Coordination View 2.0 for IFC2x3; Reference View / Design Transfer View for IFC4.
- Accompanying XML: the information model package is usually described as an IFC file plus XML files whose schemas are published by Минстрой/ФАУ ФЦС, with model composition per object type (ЦИМ + документы в формате XML).
- Classification: elements/spaces should carry КСИ codes (see section 4), typically as a Pset/classification reference.
- Naming: file-name masks and element naming per СП 328 / customer ТИМ requirements (требования заказчика, "ТЗ на ТИМ") (unverified).
- Georeferencing: coordinate system requirements (MSK/СК-63/ГСК-2011 style) and IfcMapConversion/IfcProjectedCRS use are not confirmed; typical practice is project base point tied to a local coordinate system (МСК) (unverified).

### What this means for MCP-server testing

- Test models with IFC2x3 and IFC4 both; add one IFC4x3 file to check graceful handling.
- Check that Cyrillic text in IfcLabel/IfcText, property set names and file names round-trips (IFC SPF escapes non-ASCII as `\X2\...\X0\` in ISO 10303-21).
- Russian-localised Revit/Renga exports may carry Russian pset names ("Основные характеристики", "Обозначение" etc., unverified) next to standard `Pset_WallCommon`; a good test is whether a query for `Pset_WallCommon.FireRating` still works when only Russian-named sets exist.
- Request "check model for expertise" – a tool cannot prove acceptance by Главгосэкспертиза; it can only report schema/MVD/classification/property completeness.

---

## 4. Classification systems

| System | Russian name | Notes |
|---|---|---|
| КСИ | Классификатор строительной информации | National classifier of construction information, run on ФГИС ЦС (Федеральная государственная информационная система ценообразования в строительстве). Used for coding elements, materials, resources, works and documents in models and estimates. Approving order of Минстрой, its number and date: (unverified). The Wikipedia page for КСИ did not exist at the tested URL, so no verification [1] |
| ФГИС ЦС | Федеральная государственная информационная система ценообразования в строительстве | Site: fgiscs.minstroyrf.ru (unverified URL, not fetched) |
| СПДС / ГОСТ Р 21.101-2020 | System of design documentation | Marking of documents, e.g. sheet codes [1] |
| Registry class 9.9 | Системы информационного моделирования зданий и сооружений (BIM, AEC CAD) | Proposed by Минцифры June 2020; before its adoption BIM software was classed as "информационные системы для решения специфических отраслевых задач" [1]; whether it is now adopted: (unverified) |
| ГИСОГД | Государственная информационная система обеспечения градостроительной деятельности | Regional/municipal urban planning information system; link to ТИМ via the information model of the object (unverified details) |
| ОКПД2, ОКВЭД2 | Product / activity classifiers | Often requested in specifications; not IFC-specific |

IFC side: КСИ codes are usually carried through `IfcClassificationReference` (Identification = code) tied to an `IfcClassification` named "КСИ", or as a custom property. Which of the two the expertise requires is unverified.

---

## 5. State expertise and submission procedure

Known facts [1]: IFC adopted as the main open format for models in state expertise; pilot of late 2019 by ФАУ ФЦС with Главгосэкспертиза and regional bodies.

Typical practice (unverified, from general knowledge):

1. Designer prepares project documentation (PD) plus information model (ЦИМ) per customer's ТИМ requirements.
2. Model exported to IFC (usually IFC4 Reference View or IFC2x3 Coordination View) with the property set structure demanded by the expertise body.
3. Upload through the expertise body's portal (Главгосэкспертиза: личный кабинет at gge.ru; Мосгосэкспертиза: its own portal; for several regions through ЕГРЗ, the unified register of expertise conclusions; details unverified).
4. Expertise checks: formal composition, geometry/clash sanity, linkage between model and documentation, classification and property completeness. Typical remarks (illustrative): elements without КСИ code, spaces missing area/name, wrong storey assignment, model exceeding file-size limit, mismatched coordinates.

Regional practice: Moscow (Мосгосэкспертиза) and St Petersburg ran their own ТИМ pilots [1]. Moscow additionally has requirements through Москомстройинвест/Комплекс градостроительной политики (unverified); details to be checked on official sites.

---

## 6. Software ecosystem and import substitution

| Product | Vendor | IFC / expertise notes |
|---|---|---|
| Renga (Architecture, Structure, MEP, merged 2020) | Renga Software (JV of Аскон and 1С, formed 2016; dev started 2012; first release 31 Mar 2015) | Reads IFC2x3 and IFC4, exports IFC, in registry of Russian software, took part in the 2019–2020 pilot [3][2] |
| nanoCAD BIM (Конструкции/ОВиК/ВК/Электро etc.) | Нанософт (Nanosoft) | IFC2x3, IFC4, IFC4x2 per Wikipedia (non-authoritative) [2] |
| Model Studio CS | СиСофт Девелопмент (CSoft) | Engineering/MEP BIM on top of nanoCAD/AutoCAD; participant in the pilot [1]; IFC details unverified |
| Pilot-BIM / Pilot-ICE | АСКОН | CDE-style management of models; participant details unverified |
| CREDO | Кредо-Диалог | Roads/infrastructure/topography; pilot participant [1] |
| NEOLANT | НЕОЛАНТ | Integrator, pilot participant [1] |
| Foreign tools still widely used | Revit, ArchiCAD, Tekla, Infraworks | The five most used per a survey cited in [1]; mostly model creation, not management |

Import substitution (импортозамещение): the 2022 decree direction gives priority to Russian software [1]; after 2022 Autodesk, Graphisoft/Nemetschek and others limited sales or support in Russia (unverified specifics), which explains why Russian users ask about moving Revit models to Renga/nanoCAD via IFC. Adoption level in 2019: 22% of 541 surveyed organisations used BIM; main obstacles were cost and lack of staff [1].

Open-source/enthusiast scene (unverified, none fetched): Russian-speaking users of IfcOpenShell/BlenderBIM (now Bonsai), Habr articles on IFC, Telegram chats and forums of Renga and nanoCAD users. Label them community material, not standards.

---

## 7. Organisations and associations

- buildingSMART International chapter for Russia: existence and current name unverified (historical "buildingSMART Russia" / Russian chapter; check buildingsmart.org chapter list).
- Industry bodies: НОПРИЗ, НОСТРОЙ, ДОМ.РФ expert working groups [1]; "BIM-ассоциации" and "Ассоциация ТИМ" type groups – names unverified.
- Government: Минстрой, Минцифры, ФАУ ФЦС, Главгосэкспертиза.

---

## 8. Local terminology

| Native term | Transliteration | English |
|---|---|---|
| Технологии информационного моделирования (ТИМ) | Tekhnologii informatsionnogo modelirovaniya | BIM / information modelling technologies |
| Информационная модель объекта капитального строительства | Informatsionnaya model ob'ekta kapital'nogo stroitel'stva | Information model of a capital construction object |
| Цифровая информационная модель (ЦИМ) | Tsifrovaya informatsionnaya model | Digital information model |
| Государственная экспертиза | Gosudarstvennaya ekspertiza | State design review/expertise |
| Классификатор строительной информации (КСИ) | Klassifikator stroitel'noi informatsii | Construction information classifier |
| Градостроительный кодекс | Gradostroitel'nyi kodeks | Urban Planning Code |
| Постановление Правительства | Postanovlenie Pravitel'stva | Government decree |
| Свод правил (СП) | Svod pravil | Code of practice |
| Заказчик / застройщик / технический заказчик | Zakazchik / zastroishchik / tekhnicheskii zakazchik | Client / developer / technical client |
| Требования заказчика к ТИМ | Trebovaniya zakazchika k TIM | Employer's information requirements (EIR-like) |
| План реализации ТИМ-проекта | Plan realizatsii TIM-proekta | BIM execution plan (BEP-like), term (unverified) |
| Уровень проработки | Uroven' prorabotki | Level of development/detail (LOD-like) |
| Свойство / набор свойств | Svoistvo / nabor svoistv | Property / property set |
| Импортозамещение | Importozameshchenie | Import substitution |
| Реестр российского ПО | Reestr rossiiskogo PO | Registry of Russian software |
| Общая среда данных (СОД) | Obshchaya sreda dannykh | Common data environment (CDE) |
| Коллизии | Kollizii | Clashes |
| Обменный формат | Obmennyi format | Exchange format |
| Штамп / основная надпись | Shtamp / osnovnaya nadpis' | Title block |

---

## Typical questions people ask about this

None of these were found as live links because search failed; all are illustrative.

1. (illustrative) С какого года ТИМ обязателен для объектов, финансируемых из бюджета? / Since when is BIM mandatory for budget-funded projects in Russia?
2. (illustrative) Какой версией IFC нужно экспортировать модель для Главгосэкспертизы – IFC2x3 или IFC4?
3. (illustrative) Принимает ли экспертиза IFC4x3?
4. (illustrative) Как настроить экспорт IFC в Revit для госэкспертизы (Файл > Экспорт > IFC)?
5. (illustrative) Как привязать код КСИ к элементам IFC-модели?
6. (illustrative) Какие наборы свойств (Pset) обязательны для стен/перекрытий/помещений?
7. (illustrative) Чем ЦИМ отличается от обычной 3D-модели?
8. (illustrative) Как импортировать IFC из Revit в Renga без потери свойств?
9. (illustrative) Что такое СП 333.1325800.2020 и чем он отличается от СП 328.1325800.2020?
10. (illustrative) Как проверить IFC на соответствие требованиям заказчика перед отправкой на экспертизу?
11. (illustrative) Можно ли в IFC хранить кириллицу в именах свойств и файлов?
12. (illustrative) Как задать систему координат (МСК) в IFC?
13. (illustrative) Какие типичные замечания экспертизы к ЦИМ?
14. (illustrative) Нужно ли заказчику на частном объекте делать ТИМ по ПП № 331?
15. (illustrative) Заменяет ли IFC модель пакет проектной документации?
16. (illustrative) Какое российское ПО из реестра умеет экспортировать IFC4?
17. (illustrative) Как MCP-сервер должен вести себя, если в IFC нет КСИ-кодов?
18. (illustrative) Как посчитать объёмы (BaseQuantities) по IFC для сметы в ФГИС ЦС?

## Common pitfalls and misconceptions

- Confusing **ТИМ** (the technology/process) with **ЦИМ** (the model file). Users often say "ТИМ-модель".
- Assuming "IFC" in Russia means only the file: expertise packages also include documents and XML (unverified).
- Assuming ПП № 331 = 2022: the application date (1 Jan 2022) is not the signing date (I recall 5 March 2021; unverified).
- Assuming ГОСТ Р 10.0.03-2019 is the full IFC schema: it is the national adoption (translation) of ISO 16739 and may lag the latest IFC version (unverified).
- Assuming Revit's default English property sets satisfy a Russian customer's requirements; Russian customers often demand custom Russian-named attributes.
- Forgetting that wiki-style numbers in this file are partly unverified.
- Treating Russian Wikipedia as authoritative: the IFC article carries a maintenance note about missing sources [2].

## Gaps

- Web search was unavailable (budget exhausted) so no queries on ПП 331/1431 text, СП 328/331/333 title verification, Главгосэкспертиза IFC requirements, КСИ order number, Мосгосэкспертиза/СПб requirements, buildingSMART Russia chapter, forums/Habr discussions could run.
- Fetch errors: gge.ru (403), buildingsmart.org (403), standards.buildingsmart.org (403), renga.software (DNS failure), nanocad.ru product page (404), pilot-bim.ru (connection refused); several ru.wikipedia guesses returned 404 (КСИ, Главгосэкспертиза, Мосгосэкспертиза, Pilot-ICE, ГИСОГД, ФЦС).
- No suspicious or pirated sites were encountered or linked.
- Recommended follow-up: re-run this task with working search and verify items marked (unverified).

## Sources

- [1] https://ru.wikipedia.org/wiki/BIM (also read: https://ru.wikipedia.org/wiki/Информационная_модель_здания) – Russian policy timeline, ГрК ст. 48, СП 333, ГОСТ Р 21.101-2020, pilot, class 9.9, survey. Secondary source.
- [2] https://ru.wikipedia.org/wiki/Industry_Foundation_Classes – IFC version list, Renga/nanoCAD IFC claims (non-authoritative; page flagged as lacking sources).
- [3] https://ru.wikipedia.org/wiki/Renga – developer, release years, IFC support, registry, pilot.
- [4] https://ifc43-docs.standards.buildingsmart.org/ (301 redirect to https://standards.buildingsmart.org/IFC/DEV/IFC4_3/HTML/, itself returned 403 to the fetch tool) – only the redirect was observed.
