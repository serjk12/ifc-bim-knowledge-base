# IFC/BIM/Revit glossary for more languages (IT, TR, PL, NL, CS, VI, ID, FA, HE, UK, KK, Nordic)

**Last researched: 2026-11-06**

## In plain words

IFC (Industry Foundation Classes) is the open file format and data schema that BIM programs use to swap building models; Revit is Autodesk's BIM authoring program. Both speak English first: IFC entity names such as `IfcWall` or `IfcBuildingStorey`, property set names such as `Pset_WallCommon`, and the file contents are never translated, and only the display layer (menus, help pages, documentation, classification dictionaries) is localized [28][30][31]. This glossary lines up about 220 everyday terms in English, Italian, Turkish, Polish, Dutch, Czech, Vietnamese, Indonesian, Persian, Hebrew, Ukrainian, Kazakh, Norwegian, Swedish and Finnish, so a QA tester without a BIM background can read a request such as "Pokaż wszystkie drzwi na kondygnacji 1" or "Visa alla väggar på våning 2" and know that it means `IfcDoor` or `IfcWall` filtered by `IfcBuildingStorey`. It also helps judge whether an MCP tool answered in the right terms.

How reliable is each cell? Only some of the terms were checked against official localized software help (Graphisoft Archicad help in Italian, Polish, Czech [7][8][9][10]; Autodesk Revit help in Italian, Polish, Czech [13][14][15]) or against Wikidata labels and Wikipedia articles in the target language [1][2][3][17]-[26]. Everything else is professional usage from background knowledge and is **(unverified)**. Each table has a **Basis** column that says which kind of evidence applies; any cell not covered by the basis code of its row is background knowledge.

## How to read the tables

| Basis code | Meaning |
|---|---|
| **GS** | Verbatim from a localized Graphisoft Archicad help page (IT, PL, CS only) [7][8][9][10] |
| **RV** | Verbatim from a localized Autodesk Revit help page (IT, PL, CS only) [13][14][15] |
| **WD** | Label copied from Wikidata for the matching concept [1][2][3]. Real, but a generic encyclopedia label, not necessarily the term a BIM professional uses (see "Wikidata quirks" under the tables) |
| **WK** | Term seen in running text of that language's Wikipedia article about BIM [17]-[26] |
| **BG** | Background knowledge, **not verified in this session (unverified)** |
| **+BG** | Row is partly verified; gaps and replaced labels are background knowledge (unverified) |

Language notes. Persian (FA) and Hebrew (HE) are right-to-left; identifiers such as `IfcWall`, GUIDs and numbers stay left-to-right Latin text inside them. Norwegian (NO) is Bokmal (Wikidata and Wikipedia use the code `nb`/`no`) [4][24]. Kazakh (KK) is the weakest column: Wikipedia has no Kazakh article on BIM under the titles tried [27], Wikidata has no Kazakh label for BIM [3], and many Kazakh construction terms are Russian loans (Wikidata gives `колонна`, `лифт`, `клапан` as Kazakh labels [1]). A trailing `?` means "my best guess, low confidence".

Terms that are normally left in English in every language (unverified): IFC, openBIM, IDS, BCF, bSDD, MVD, CDE, EIR, BEP, LOD, LOIN, MEP, HVAC, GUID, GlobalId. The Dutch Wikipedia article keeps `openBIM`, `IFC`, `clashcontrole` as is [26]; the Ukrainian article keeps `BIM`, `LOD`, `IFC` [20]; the Persian article keeps `Interoperability`, `As Built` in Latin script [19].

## Scope, versions and ground facts

| Fact | Value | Source |
|---|---|---|
| IFC naming of the ISO standard | ISO 16739-1; the Italian adoption UNI EN ISO 16739-1:2020 was listed as superseded by UNI EN ISO 16739-1:2024 (seen in search results, not opened) | [36] |
| Current official IFC release | IFC 4.3.2.0 (`IFC4X3_ADD2`) is the "official" snapshot at standards.buildingsmart.org | [43] |
| Italian national BIM standard | UNI 11337-1:2017 exists (current edition, per shop listing); Italian tender documents also use UNI EN ISO 19650 and UNI EN 17412-1 (level of information need) | [36] |
| IFC translation workflow | Entity, attribute, property-set and property names are extracted from the UML on each commit, translated in Crowdin, pushed back to a Git branch, and shown in a language dropdown of the IFC 4.3 development docs site | [28] |
| Translation repository | `buildingSMART/IFC-translations` on GitHub: branch `input` filled automatically from the IFC development repo; `translations` filled from Crowdin; "30+ languages"; do not edit by hand | [32][33] |
| Translations NOT in the official snapshot | The translated display exists only on the development docs server, not in the static 4.3.2 snapshot | [28] |
| Approval | Chapters proofread; a translation appears in bSDD only after the responsible chapter approves. In April 2023 no IFC translations were yet approved in bSDD (may have changed since, unverified) | [30][31] |
| What translation does not change | The IFC file keeps its original English codes; translation is only a display layer. XSD and EXPRESS schemas contain English only | [30][31] |
| Docs language list | The IFC 4.3 documentation index showed flags for at least Arabic, Chinese (Simplified), Croatian, Czech, Danish, Dutch, Finnish, French, German, Greek, Hindi, Icelandic, Italian, Japanese, Korean (list cut off in the search result) | [34] |
| First chapters in the IFC4 translation initiative | Germany (initiator, 2018), Austria, Switzerland; Spain and Russia applying the same scheme | [29] |
| Software help available in these languages | Archicad help folders found for ITA, POL, CZE (plus GER, FRA, SPA, RUS, JPN, HUN); none found for TR, NL, FI, UK, SV, NO in the searches done. Revit help verified for ITA, PLK, CSY | [7][9][10][13][14][15][37] |

## Verified: IFC concepts as localized in Archicad help (IT, PL, CS)

Graphisoft's "IFC Data Types" help page is the closest thing to an official IFC glossary in these three languages. Note that these are **Archicad's** names for IFC concepts, not buildingSMART-approved translations. English meanings follow the English help page [11]. Basis: GS for every cell.

| English (IFC / meaning) | IT [9] | PL [8] | CS [10] |
|---|---|---|---|
| IFC entity (e.g. `IfcWall`) | Entità IFC | Jednostka IFC | Entity IFC |
| IFC type (group in IFC Project Manager tree) | Tipo IFC | Typ IFC | IFC typ |
| IFC type product (`IfcTypeProduct`, shared style such as window style) | Tipo di prodotto IFC | Typ produktu IFC | IFC produktový typ |
| IFC container (no own geometry; parts carry it) | Contenitore IFC | Zbiór IFC | IFC kontejner |
| IFC attributes (Name, Description, ObjectType, Tag) | Attributi IFC | Atrybuty IFC | IFC atributy |
| IFC properties | Proprietà IFC | Właściwości IFC | IFC vlastnosti |
| Classification reference (`IfcClassificationReference`) | Riferimento classificazione IFC | Odniesienie klasyfikacji IFC | Reference klasifikace IFC |
| Assignments (`IfcRelAssigns`) | Assegnazioni IFC | Przypisanie IFC | IFC zařazení |
| Group (`IfcGroup`) | Gruppo IFC | Grupa IFC | IFC skupiny |
| Zone (`IfcZone`, groups spaces) | Zona IFC | Strefa IFC | IFC zóny |
| System (`IfcSystem`, mostly MEP) | Sistema IFC | System IFC | IFC systémy |
| Spatial elements (project, site, building, storey, space) | Elementi spaziali IFC | Elementy przestrzenne IFC | Prostorové prvky IFC |
| Site (`IfcSite`) | Sito IFC | Lokalizacja (Otoczenie) | IfcSite (left untranslated) |
| Building (`IfcBuilding`) | Edificio IFC | Budynek | IfcBuilding (left untranslated) |
| Storey (`IfcBuildingStorey`) | Piano IFC | Kondygnacja | IfcBuildingStorey (left untranslated) |
| Space (`IfcSpace`, = Archicad Zone) | Zona | Strefa | IfcSpace (left untranslated) |
| Building material (`IfcMaterial`) | Materiale da Costruzione | Materiał budowlany | Stavební materiál |
| Composite / layer set (`IfcMaterialLayerSet`) | Struttura Composta | Struktura warstwowa | Sendvič |
| Surface (`IfcSurfaceStyleRendering`) | Superficie | Wykończenie | Plošné |
| Profile (`IfcProfileDef`) | Profilo | Profil | Profil |
| Layer (`IfcPresentationLayerAssignment`) | Lucido | Warstwa | Vrstva |
| Property set (names starting `Pset_`) | insiemi di proprietà | Zestaw właściwości | sady vlastností |
| GlobalId | GlobalId / ID Globale | GlobalID | GlobalId |
| Tag (Archicad element ID, not the GlobalId) | Tag | Metka | Visačka |

Other Polish Archicad menu names from the IFC help sidebar [7]: Eksport modelu IFC (export), Import modelu IFC (import), Otwórz model IFC (open), Łącz projekt IFC (link/merge), Moduł Hotlink pliku IFC, Menedżer projektu IFC (IFC Project Manager), Translatory IFC (translators), Filtruj model podczas importu (import filter), Definicje widoku modelu (model view definitions), Załącznik: Mapowanie danych IFC (data mapping appendix). Czech menu names seen in search results: Import IFC modelu, IFC převodníky (translators), Připojení IFC souboru (merge/link) [37]. Italian: Importazione del modello IFC, Importa Modello IFC, Esportare il Modello IFC [37]. Polish help uses "Modelowanie informacji o budynku" for BIM and "plik IFC" for IFC file [7].

## Verified: Revit terms in localized Autodesk help (IT, PL, CS)

Basis: RV for every cell. English column is the Revit English UI name.

| English (Revit) | IT [13] | PL [14] | CS [15] |
|---|---|---|---|
| Family | famiglia | rodzina | rodina |
| Type / family types | tipo / Tipi di famiglie | typ / typy rodziny | typ / typy rodin |
| Instance | istanza | wystąpienie (not "egzemplarz") | instance |
| System family | Famiglie di sistema | rodzina systemowa | systémová rodina |
| Loadable family | Famiglie caricabili | rodzina wczytywalna | načítatelné rodiny |
| In-place family | Famiglie locali | rodzina lokalna | rodiny na místě |
| Model family | Famiglie di modellazione | rodzina modelowania | modelované rodiny |
| Annotation family | Famiglie di annotazioni | rodzina opisów | rodiny poznámek |
| Category | Categoria | kategoria | kategorie |
| Instance properties | Proprietà di istanza | właściwości wystąpienia | vlastnosti instance |
| Type properties | Proprietà del tipo | właściwości typu | vlastnosti typu |
| Type Selector | Selettore di tipo | Wybór typu | Výběr typu |
| Properties palette | tavolozza Proprietà | okno Właściwości | (not seen) |
| Project Browser | Browser di progetto | Przeglądarka projektu | (not seen) |
| Duplicate (type) | (not seen) | Powiel | Duplikovat |
| Level | livello | poziom | podlaží (page text pairs it with "floor/level") |
| View (plan, elevation, section, 3D) | vista (pianta, prospetto, sezione, 3D) | widok | pohled |
| Wall | muro | ściana | stěna |
| Door | porta | drzwi | dveře |
| Window | finestra | okno | okno |
| Curtain wall | facciata continua | (not seen) | (not seen) |
| Roof | (not seen) | dach | střecha |
| Schedule | abaco [16] | zestawienie (unverified) | výkaz (unverified) |

Not found in the three pages: Italian pavimento/tetto/soffitto/scala, Polish parametr/zestawienie/schody, Czech strop/schodiště/parametr/výkaz [13][14][15]. The Italian word "abaco" for Revit schedule comes from a search-result snippet of an Italian Autodesk help page [16].

## Main glossary (15 languages)

Column order in every table: EN | IT | TR | PL | NL | CS | VI | ID | FA | HE | UK | KK | NO | SV | FI | Basis. Alternatives are separated by `/`. Where the IFC entity is known it is shown in the first column in backticks.

### A. Core BIM and IFC concepts

| EN | IT | TR | PL | NL | CS | VI | ID | FA | HE | UK | KK | NO | SV | FI | Basis |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| BIM (building information modelling) | BIM / Building Information Modeling | Yapı Bilgi Modellemesi | Modelowanie informacji o budynku | bouwwerkinformatiemodellering | informační model budovy | mô hình thông tin xây dựng | pemodelan informasi bangunan | مدل‌سازی اطلاعات ساختمان | מידול האינפורמציה של המבנה | інформаційне моделювання будівель | ақпараттық модельдеу? | bygningsinformasjonsmodellering | byggnadsinformationsmodellering | rakennuksen tietomallintaminen | WD+WK+GS(PL)+BG |
| building information model (the model itself) | modello informativo | yapı bilgi modeli | model informacyjny budynku | bouwwerkinformatiemodel | informační model stavby | mô hình thông tin công trình | model informasi bangunan | مدل اطلاعات ساختمان | מודל מידע של מבנה | інформаційна модель будівлі | ақпараттық модель? | bygningsinformasjonsmodell | byggnadsinformationsmodell | tietomalli / rakennuksen tietomalli | WK+BG |
| information model | modello informativo | bilgi modeli | model informacyjny | informatiemodel | informační model | mô hình thông tin | model informasi | مدل اطلاعات | מודל מידע | інформаційна модель | ақпараттық модель? | informasjonsmodell | informationsmodell | tietomalli | BG |
| 3D model | modello 3D | 3B model | model 3D | 3D-model | 3D model | mô hình 3 chiều | model 3D | مدل سه‌بعدی | מודל תלת-ממדי | 3D-модель | 3D модель | 3D-modell | 3D-modell | 3D-malli | WK(VI)+BG |
| IFC (Industry Foundation Classes) | IFC | IFC | IFC | IFC | IFC | IFC | IFC | کلاس‌های بنیادین صنعت / IFC | IFC | IFC | IFC | IFC | IFC | IFC | WD |
| IFC file | file IFC | IFC dosyası | plik IFC | IFC-bestand | soubor IFC | tệp IFC | berkas IFC | فایل IFC | קובץ IFC | файл IFC | IFC файлы | IFC-fil | IFC-fil | IFC-tiedosto | GS(PL,CS)+BG |
| IFC schema (IFC2X3, IFC4, IFC4X3) | schema IFC | IFC şeması | schemat IFC | IFC-schema | schéma IFC | lược đồ IFC | skema IFC | شمای IFC | סכמת IFC | схема IFC | IFC сызбасы? | IFC-skjema | IFC-schema | IFC-skeema | BG |
| open standard (openBIM) | standard aperto | açık standart | otwarty standard | open standaard | otevřený standard | tiêu chuẩn mở | standar terbuka | استاندارد باز | תקן פתוח | відкритий стандарт | ашық стандарт? | åpen standard | öppen standard | avoin standardi | WD+BG |
| interoperability | interoperabilità | birlikte çalışabilirlik | interoperacyjność | interoperabiliteit | interoperabilita | tính tương tác | interoperabilitas | میان‌کنش‌پذیری | תפעוליות בינית | інтероперабельність | өзара әрекеттестік? | interoperabilitet | interoperabilitet | yhteentoimivuus | WD+WK+BG |
| entity (`IfcRoot` subtypes) | entità | varlık | jednostka / encja | entiteit | entita | thực thể | entitas | موجودیت | ישות | сутність | нысан? | entitet | entitet | entiteetti | GS(IT,PL,CS)+BG |
| attribute | attributo | öznitelik | atrybut | attribuut | atribut | thuộc tính | atribut | ویژگی | תכונה | атрибут | атрибут | attributt | attribut | attribuutti | GS(IT,PL,CS)+BG |
| property | proprietà | özellik | właściwość | eigenschap | vlastnost | đặc tính | properti | خاصیت | מאפיין | властивість | қасиет | egenskap | egenskap | ominaisuus | GS(IT,PL,CS)+BG |
| property set (`IfcPropertySet`, `Pset_*`) | insieme di proprietà | özellik kümesi | zestaw właściwości | eigenschappenset | sada vlastností | bộ thuộc tính | set properti | مجموعه ویژگی‌ها | קבוצת מאפיינים | набір властивостей | қасиеттер жиынтығы? | egenskapssett | egenskapsuppsättning | ominaisuusjoukko | GS(IT,PL,CS)+BG |
| quantity set (`Qto_*`, base quantities) | insieme di quantità | miktar kümesi | zestaw ilości | hoeveelhedenset | sada množství | bộ khối lượng | set kuantitas | مجموعه مقادیر | קבוצת כמויות | набір кількостей | көлем жиынтығы? | mengdesett | mängduppsättning | määräjoukko | BG |
| relationship (`IfcRelationship`) | relazione | ilişki | relacja | relatie | vztah | quan hệ | relasi | رابطه | יחס | зв'язок | қатынас | relasjon | relation | suhde | BG |
| type object (`IfcTypeObject`, e.g. `IfcWallType`) | tipo | tip | typ | type | typ | kiểu / loại | tipe | نوع | סוג | тип | түр | type | typ | tyyppi | RV(IT,PL,CS)+BG |
| occurrence / instance | istanza | örnek | wystąpienie | exemplaar / instantie | instance | thể hiện | instans | نمونه | מופע | екземпляр | дана? | forekomst | instans | esiintymä | RV(IT,PL,CS)+BG |
| GlobalId (`IfcGloballyUniqueId`, 22 characters) | GlobalId / ID Globale | GlobalId | GlobalID | GlobalId | GlobalId | GlobalId | GlobalId | GlobalId | GlobalId | GlobalId | GlobalId | GlobalId | GlobalId | GlobalId | GS(IT,PL,CS)+BG |
| classification (`IfcClassification`) | classificazione | sınıflandırma | klasyfikacja | classificatie | klasifikace | phân loại | klasifikasi | طبقه‌بندی | סיווג | класифікація | жіктеу | klassifikasjon | klassificering | luokittelu | GS(PL)+BG |
| spatial structure | struttura spaziale | mekânsal yapı | struktura przestrzenna | ruimtelijke structuur | prostorová struktura | cấu trúc không gian | struktur spasial | ساختار فضایی | מבנה מרחבי | просторова структура | кеңістіктік құрылым? | romlig struktur | rumslig struktur | tilarakenne | BG |
| geometry / representation | geometria / rappresentazione | geometri / temsil | geometria / reprezentacja | geometrie / representatie | geometrie / reprezentace | hình học / biểu diễn | geometri / representasi | هندسه | גיאומטריה | геометрія | геометрия | geometri | geometri | geometria | BG |
| coordinate system | sistema di coordinate | koordinat sistemi | układ współrzędnych | coördinatenstelsel | souřadnicový systém | hệ tọa độ | sistem koordinat | سیستم مختصات | מערכת קואורדינטות | система координат | координаттар жүйесі | koordinatsystem | koordinatsystem | koordinaatisto | BG |
| unit of measurement (`IfcUnit`) | unità di misura | ölçü birimi | jednostka miary | maateenheid | fyzikální jednotka | đơn vị đo | satuan ukuran | یکا | יחידת מידה | одиниця вимірювання | бірлік | måleenhet | måttenhet | mittayksikkö | WD |
| model view definition (MVD) | definizione della vista del modello | model görünüm tanımı | definicje widoku modelu | model view definition (MVD) | definice pohledu modelu | định nghĩa khung nhìn mô hình | definisi tampilan model | تعریف نمای مدل | הגדרת תצוגת מודל | визначення подання моделі | модель көрінісінің анықтамасы? | modellvisningsdefinisjon | modellvydefinition | mallinäkymämäärittely | GS(PL)+BG |
| federated model | modello federato | birleştirilmiş model | model federacyjny / skoordynowany | gefedereerd model / coördinatiemodel | federovaný model | mô hình liên kết | model gabungan | مدل ترکیبی | מודל מאוחד | федеративна модель | біріктірілген модель? | koordineringsmodell | samordningsmodell | yhdistelmämalli | BG |
| discipline model | modello disciplinare | disiplin modeli | model branżowy | disciplinemodel | profesní model | mô hình theo bộ môn | model disiplin | مدل تخصصی | מודל דיסציפלינרי | галузева модель | салалық модель? | fagmodell | disciplinmodell | alakohtainen malli | BG |
| clash detection | rilevamento interferenze | çakışma kontrolü | wykrywanie kolizji | clashcontrole | detekce kolizí | kiểm tra xung đột | deteksi benturan | تشخیص تصادم / تداخل | בדיקת התנגשויות | виявлення колізій | коллизияларды анықтау? | kollisjonskontroll | kollisionskontroll | törmäystarkastelu | WD+WK+BG |
| coordination | coordinamento | koordinasyon | koordynacja | coördinatie | koordinace | phối hợp | koordinasi | هماهنگی | תיאום | координація | үйлестіру | koordinering | samordning | koordinointi | WK+BG |
| quantity take-off | computo metrico | metraj | przedmiar / obmiar | hoeveelhedenstaat / uittrekstaat | výkaz výměr | bóc tách khối lượng | perhitungan kuantitas | متره | חישוב כמויות | відомість обсягів робіт | көлемдерді есептеу? | mengdeuttak | mängdavtagning | määrälaskenta | WK+WD(IT,PL)+BG |
| schedule (table of elements) | abaco | tablo / çizelge | zestawienie | overzicht / uittrekstaat | výkaz | bảng thống kê | tabel / jadwal | جدول | טבלה | специфікація / відомість | кесте | tabell | tabell / lista | taulukko / luettelo | RV(IT via [16])+BG |
| bill of quantities | computo metrico estimativo | keşif / metraj cetveli | przedmiar | bestek / hoeveelhedenstaat | výkaz výměr | bảng khối lượng | daftar kuantitas (BoQ) | فهرست مقادیر | כתב כמויות | відомість обсягів | көлем ведомосы? | mengdebeskrivelse | mängdförteckning | määräluettelo | WD(IT,PL,HE)+BG |
| facility management | facility management | tesis yönetimi | facility management | facilitair management | facility management | quản lý vận hành công trình | manajemen fasilitas | مدیریت تأسیسات | תחזוקת מבנים | фасіліті-менеджмент | нысанды басқару? | eiendomsforvaltning | facility management / fastighetsförvaltning | toimitilajohtaminen | WD+BG |
| digital twin | gemello digitale | dijital ikiz | cyfrowy bliźniak | digitale tweeling | digitální dvojče | bản sao số | kembaran digital | همزاد دیجیتال | תאום דיגיטלי | цифровий двійник | цифрлық егіз? | digital tvilling | digital tvilling | digitaalinen kaksonen | WD+BG |
| point cloud | nuvola di punti | nokta bulutu | chmura punktów | puntenwolk | mračno bodů | đám mây điểm | awan titik | ابر نقاط | ענן נקודות | хмара точок | нүктелер бұлты? | punktsky | punktmoln | pistepilvi | WD+BG |
| laser scanning | laser scanner | lazer tarama | skanowanie laserowe | laserscannen | laserové skenování | quét laser | pemindaian laser | اسکن لیزری | סריקת לייזר | лазерне сканування | лазерлік сканерлеу? | laserskanning | laserskanning | laserkeilaus | WD+BG |
| GIS | sistema informativo geografico | coğrafi bilgi sistemi | system informacji geograficznej | geografisch informatiesysteem | geografický informační systém | hệ thống thông tin địa lý | sistem informasi geografis | سامانه اطلاعات جغرافیایی | מערכת מידע גאוגרפית | геоінформаційна система | географиялық ақпараттық жүйе | GIS / geografisk informasjonssystem | geografiskt informationssystem | paikkatietojärjestelmä | WD+BG |
| CAD (computer-aided design) | CAD | bilgisayar destekli tasarım | projektowanie wspomagane komputerowo | CAD | CAD | CAD | CAD | طراحی رایانه‌ای | תכנון בעזרת מחשב | САПР | автоматтандырылған жобалау жүйесі | CAD / dataassistert konstruksjon | CAD | tietokoneavusteinen suunnittelu | WD |
| parametric design | progettazione parametrica | parametrik tasarım | projektowanie parametryczne | parametrisch ontwerpen | parametrické navrhování | thiết kế tham số | desain parametrik | طراحی پارامتریک | עיצוב פרמטרי | параметричне проєктування | параметрлік жобалау? | parametrisk design | parametrisk design | parametrinen suunnittelu | WD+WK(UK)+BG |
| 4D (time) / 5D (cost) | 4D / 5D | 4B / 5B | 4D / 5D | 4D / 5D | 4D / 5D | BIM 4D / 5D | 4D / 5D | بعد چهارم (زمان) / بعد پنجم (هزینه) | 4D / 5D | 4D (час) / 5D (витрати) | 4D / 5D | 4D / 5D | 4D / 5D | 4D / 5D | WK(FA,UK,VI)+BG |

### B. Spatial structure, project and dimensions

| EN | IT | TR | PL | NL | CS | VI | ID | FA | HE | UK | KK | NO | SV | FI | Basis |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| project (`IfcProject`) | progetto | proje | projekt | project | projekt | dự án | proyek | پروژه | פרויקט | проєкт | жоба | prosjekt | projekt | hanke / projekti | BG |
| site (`IfcSite`) | sito / lotto | arsa / saha | działka / teren | terrein / kavel | pozemek | khu đất | tapak / lahan | محوطه / زمین | אתר / מגרש | ділянка / майданчик | жер учаскесі | tomt | tomt | tontti | GS(IT,PL)+BG |
| building (`IfcBuilding`) | edificio | bina | budynek | gebouw | budova | tòa nhà | bangunan | ساختمان | בניין | будівля | ғимарат | bygning | byggnad | rakennus | WD+GS(IT,PL)+BG |
| storey / level (`IfcBuildingStorey`) | piano | kat | kondygnacja | bouwlaag / verdieping | podlaží | tầng | lantai / tingkat | طبقه | קומה | поверх | қабат | etasje | våningsplan | kerros | WD+GS(IT,PL)+BG |
| space / room (`IfcSpace`) | spazio / ambiente | mekân / oda | pomieszczenie / strefa | ruimte | místnost / prostor | phòng / không gian | ruang | فضا / اتاق | חלל / חדר | приміщення / кімната | бөлме | rom | rum | tila / huone | WD(room)+GS(IT,PL)+BG |
| zone (`IfcZone`, grouping of spaces) | zona | bölge | strefa | zone | zóna | khu vực | zona | ناحیه | אזור | зона | аймақ | sone | zon | vyöhyke | GS(IT,PL,CS)+BG |
| system (`IfcSystem`) | sistema | sistem | system | systeem | systém | hệ thống | sistem | سامانه | מערכת | система | жүйе | system | system | järjestelmä | GS(IT,PL,CS)+BG |
| group (`IfcGroup`) | gruppo | grup | grupa | groep | skupina | nhóm | grup | گروه | קבוצה | група | топ | gruppe | grupp | ryhmä | GS(IT,PL,CS)+BG |
| ground floor | piano terra | zemin kat | parter | begane grond | přízemí | tầng trệt | lantai dasar | همکف | קומת קרקע | перший поверх | бірінші қабат | første etasje | bottenvåning / plan 1 | pohjakerros / 1. kerros | BG |
| basement | seminterrato / interrato | bodrum | piwnica | kelder | suterén | tầng hầm | basemen / ruang bawah tanah | زیرزمین | מרתף | підвал | жертөле | kjeller | källare | kellari | BG |
| area | area / superficie | alan | powierzchnia | oppervlakte | plocha | diện tích | luas | مساحت | שטח | площа | аудан | areal | area | pinta-ala | BG |
| volume | volume | hacim | objętość / kubatura | volume / inhoud | objem | thể tích | volume | حجم | נפח | об'єм | көлем | volum | volym | tilavuus | BG |
| height | altezza | yükseklik | wysokość | hoogte | výška | chiều cao | tinggi | ارتفاع | גובה | висота | биіктік | høyde | höjd | korkeus | BG |
| length | lunghezza | uzunluk | długość | lengte | délka | chiều dài | panjang | طول | אורך | довжина | ұзындық | lengde | längd | pituus | BG |
| width | larghezza | genişlik | szerokość | breedte | šířka | chiều rộng | lebar | عرض | רוחב | ширина | ені | bredde | bredd | leveys | BG |
| thickness | spessore | kalınlık | grubość | dikte | tloušťka | độ dày | tebal | ضخامت | עובי | товщина | қалыңдық | tykkelse | tjocklek | paksuus | BG |
| floor plan | pianta | kat planı | rzut | plattegrond | půdorys | mặt bằng | denah | پلان | תוכנית | план поверху | жоспар | plantegning | planritning | pohjapiirros | WD+WK(VI)+BG |
| section (drawing) | sezione | kesit | przekrój | doorsnede | řez | mặt cắt | potongan | برش | חתך | розріз | қима | snitt | sektion / snitt | leikkaus | WK(VI)+BG |
| elevation (facade view) | prospetto | görünüş / cephe | elewacja | gevelaanzicht | pohled | mặt đứng | tampak | نما | חזית | фасад | қасбет | fasade | fasad | julkisivu | RV(IT,PL,CS)+WK(VI)+BG |
| site plan | planimetria generale | vaziyet planı | plan zagospodarowania terenu | situatie | situace | tổng mặt bằng | rencana tapak | پلان استقرار | תוכנית פיתוח | генеральний план | бас жоспар | situasjonsplan | situationsplan | asemapiirros | BG |
| opening (`IfcOpeningElement`) | apertura / vano | boşluk / açıklık | otwór | sparing / opening | otvor | lỗ mở | bukaan | بازشو | פתח | отвір | саңылау | åpning / hull | öppning | aukko | BG |

### C. Building elements and materials

| EN | IT | TR | PL | NL | CS | VI | ID | FA | HE | UK | KK | NO | SV | FI | Basis |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| wall (`IfcWall`) | muro | duvar | ściana | muur / wand | stěna / zeď | tường | dinding | دیوار | קיר | стіна | қабырға / дуал | vegg / mur | vägg / mur | seinä | RV(IT,PL,CS)+WD+BG |
| door (`IfcDoor`) | porta | kapı | drzwi | deur | dveře | cửa đi | pintu | در | דלת | двері | есік | dør | dörr | ovi | RV+WD+BG |
| window (`IfcWindow`) | finestra | pencere | okno | raam / venster | okno | cửa sổ | jendela | پنجره | חלון | вікно | терезе | vindu | fönster | ikkuna | RV+WD |
| roof (`IfcRoof`) | tetto | çatı | dach | dak | střecha | mái | atap | بام | גג | дах | төбе / шатыр | tak | tak / yttertak | katto | RV(PL,CS)+WD+BG |
| column (`IfcColumn`) | pilastro / colonna | kolon / sütun | słup / kolumna | kolom / zuil | sloup | cột | kolom | ستون | עמוד | колона | бағана | søyle | pelare / kolonn | pilari / pylväs | WD+BG |
| beam (`IfcBeam`) | trave | kiriş | belka | ligger / balk | nosník | dầm | balok | تیر | קורה | балка | арқалық | bjelke | balk | palkki | WD+BG |
| stairs (`IfcStair`) | scala | merdiven | schody | trap | schodiště | cầu thang | tangga | پلکان | מדרגות | сходи | баспалдақ | trapp | trappa | portaat | WD+BG |
| ramp (`IfcRamp`) | rampa | rampa | rampa | helling / hellingbaan | rampa | dốc / đường dốc | ramp | رمپ / سطح شیب‌دار | רמפה | пандус | пандус | rampe | ramp | luiska / ramppi | BG |
| slab / floor slab (`IfcSlab`) | solaio / soletta | döşeme | płyta stropowa / strop | vloer | stropní deska / strop | sàn / bản sàn | pelat lantai | دال / سقف | תקרה / רצפה | плита перекриття | аражабын плитасы? | dekke | bjälklag | laatta / välipohja | BG |
| ceiling / covering (`IfcCovering`) | soffitto / controsoffitto | tavan | sufit | plafond | podhled / strop | trần | langit-langit | سقف کاذب / سقف | תקרה | стеля | төбе | himling | innertak | sisäkatto | WD+BG |
| foundation (`IfcFooting`, `IfcPile`) | fondazioni | temel | fundament | fundering | základy | móng | fondasi | پی / شالوده | יסודות | фундамент | іргетас | fundament | grund / fundament | perustus | WD+BG |
| curtain wall (`IfcCurtainWall`) | facciata continua | giydirme cephe | ściana kurtynowa | vliesgevel | lehký obvodový plášť / fasáda | tường kính / vách kính | dinding tirai | نمای شیشه‌ای / دیوار پرده‌ای | קיר מסך | навісний фасад | шыны қасбет? | glassfasade / curtain wall | glasfasad / curtain wall | verhoseinä | RV(IT)+BG |
| handrail / railing (`IfcRailing`) | corrimano / ringhiera | korkuluk | poręcz / balustrada | leuning / hekwerk | madlo / zábradlí | tay vịn / lan can | susur tangan / pagar | نرده | מעקה | перила / огорожа | қоршау? | gelender / rekkverk | räcke | kaide | WD+BG |
| elevator (`IfcTransportElement`, ELEVATOR) | ascensore | asansör | winda | lift | výtah | thang máy | lift / pengangkat | آسانسور | מעלית | ліфт | лифт | heis | hiss | hissi | WD |
| balcony | balcone | balkon | balkon | balkon | balkon | ban công | balkon | بالکن / ایوان | מרפסת | балкон | балкон | balkong | balkong | parveke | BG |
| chimney | camino / canna fumaria | baca | komin | schoorsteen | komín | ống khói | cerobong | دودکش | ארובה | димар | мұржа | skorstein | skorsten | savupiippu | BG |
| furniture (`IfcFurniture`) | arredi / mobili | mobilya | meble | meubilair | nábytek | đồ nội thất | furnitur | مبلمان | ריהוט | меблі | жиһаз | møbler | möbler | kalusteet | BG |
| reinforcement bar (`IfcReinforcingBar`) | armatura | donatı | zbrojenie | wapening | výztuž | cốt thép | tulangan | میلگرد | זיון / מוטות זיון | арматура | арматура | armering | armering | raudoitus | BG |
| concrete | calcestruzzo | beton | beton | beton | beton | bê tông | beton | بتن | בטון | бетон | бетон | betong | betong | betoni | WD |
| reinforced concrete | calcestruzzo armato | betonarme | żelbet | gewapend beton | železobeton | bê tông cốt thép | beton bertulang | بتن مسلح | בטון מזוין | залізобетон | темірбетон | armert betong | armerad betong | teräsbetoni | WD |
| steel | acciaio | çelik | stal | staal | ocel | thép | baja | فولاد | פלדה | сталь | болат | stål | stål | teräs | WD |
| brick | mattone | tuğla | cegła | baksteen | cihla | gạch | batu bata | آجر | לבנה | цегла | кірпіш | murstein | tegel / murtegel | tiili | WD |
| glass | vetro | cam | szkło | glas | sklo | thủy tinh / kính | kaca | شیشه | זכוכית | скло | әйнек | glass | glas | lasi | WD |
| wood / timber | legno | ahşap / tahta | drewno | hout | dřevo | gỗ | kayu | چوب | עץ | деревина | ағаш | tre / treverk | trä | puu / puuaines | WD+BG |
| thermal insulation | isolamento termico | ısı yalıtımı | izolacja cieplna | warmte-isolatie | tepelná izolace | cách nhiệt | insulasi termal | عایق حرارتی | בידוד תרמי | теплоізоляція | жылу оқшаулағыш | termisk isolasjon | värmeisolering | lämmöneriste | WD+BG |
| material (`IfcMaterial`) | materiale | malzeme | materiał | materiaal | materiál | vật liệu | bahan | مواد | חומר | матеріал | материал | materiale | material | materiaali | WD+GS |
| aluminium | alluminio | alüminyum | aluminium | aluminium | hliník | nhôm | aluminium | آلومینیوم | אלומיניום | алюміній | алюминий | aluminium | aluminium | alumiini | BG |
| plaster | intonaco | sıva | tynk | pleisterwerk | omítka | vữa trát | plester | گچ‌کاری / اندود | טיח | штукатурка | сылақ | puss | puts | rappaus | BG |
| gypsum board | cartongesso | alçıpan | płyta gipsowo-kartonowa | gipsplaat | sádrokarton | tấm thạch cao | papan gipsum | گچ‌برد | גבס | гіпсокартон | гипсокартон | gipsplate | gipsskiva | kipsilevy | BG |
| stone | pietra | taş | kamień | steen | kámen | đá | batu | سنگ | אבן | камінь | тас | stein | sten | kivi | BG |
| tile | piastrella | fayans / seramik | płytka | tegel | dlažba / obklad | gạch ốp lát | ubin | کاشی | אריח | плитка | плитка | flis | kakel | laatta | BG |
| mortar | malta | harç | zaprawa | mortel | malta | vữa xây | mortar | ملات | טיט | розчин | ерітінді | mørtel | murbruk | laasti | BG |
| finish (surface finish) | finitura | kaplama / finisaj | wykończenie | afwerking | povrchová úprava | hoàn thiện | finishing | نازک‌کاری | גימור | оздоблення | әрлеу | overflate / finish | ytskikt | pintakäsittely | GS(PL)+BG |
| load-bearing | portante | taşıyıcı | nośny | dragend | nosný | chịu lực | penahan beban | باربر | נושא | несучий | көтергіш | bærende | bärande | kantava | BG |
| external / internal | esterno / interno | dış / iç | zewnętrzny / wewnętrzny | buiten / binnen | vnější / vnitřní | ngoài / trong | eksterior / interior | خارجی / داخلی | חיצוני / פנימי | зовнішній / внутрішній | сыртқы / ішкі | ytre / indre | yttre / inre | ulko / sisä | BG |
| fire rating | resistenza al fuoco | yangın dayanımı | odporność ogniowa | brandwerendheid | požární odolnost | giới hạn chịu lửa | ketahanan api | مقاومت در برابر آتش | עמידות אש | вогнестійкість | отқа төзімділік | brannmotstand | brandmotstånd | palonkestävyys | BG |
| thermal transmittance (U-value) | trasmittanza termica | ısı geçirgenlik katsayısı | współczynnik przenikania ciepła | warmtedoorgangscoëfficiënt | součinitel prostupu tepla | hệ số truyền nhiệt | transmitansi termal | ضریب انتقال حرارت | מקדם מעבר חום | коефіцієнт теплопередачі | жылу берілу коэффициенті | U-verdi | U-värde / värmegenomgångskoefficient | lämmönläpäisykerroin | BG |

### D. MEP (building services) and electrical

| EN | IT | TR | PL | NL | CS | VI | ID | FA | HE | UK | KK | NO | SV | FI | Basis |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| MEP | impianti (MEP) | mekanik, elektrik, tesisat (MEP) | instalacje (MEP) | installaties | TZB | cơ điện (MEP) | mekanikal, elektrikal, dan perpipaan | تأسیسات | מערכות (אינסטלציה, חשמל, מיזוג) | інженерні системи | инженерлік жүйелер | tekniske fag (VVS / el) | installationer / VVS och el | talotekniikka (LVI ja sähkö) | WD(ID)+WK(TR,FA,NO,FI)+BG |
| HVAC | climatizzazione (HVAC) | iklimlendirme (HVAC) | ogrzewanie, wentylacja, klimatyzacja | klimaatinstallatie | vytápění a vzduchotechnika | điều hòa thông gió | tata udara (HVAC) | تهویه مطبوع | מיזוג אוויר | ОВіК | желдету және ауаны баптау | VVS (ventilasjon) | VVS / ventilation | LVI / ilmanvaihto | WK(HE,NO,FI)+BG |
| plumbing | idraulica | sıhhi tesisat | instalacje sanitarne | sanitair / loodgieterswerk | zdravotechnika | cấp thoát nước | perpipaan / plambing | لوله‌کشی | אינסטלציה | водопостачання та каналізація | су құбыры мен кәріз | rørlegger | VA / rör | LVI / vesi ja viemäri | BG |
| electrical | impianti elettrici | elektrik tesisatı | instalacje elektryczne | elektrotechniek | elektroinstalace | điện | kelistrikan | برق | חשמל | електрика | электр | elektro | el | sähkö | WK(ID)+BG |
| fire protection | antincendio | yangın koruma | ochrona przeciwpożarowa | brandbeveiliging | požární ochrana | phòng cháy chữa cháy | proteksi kebakaran | حفاظت در برابر حریق | בטיחות אש | протипожежний захист | өрттен қорғау | brannsikring | brandskydd | palontorjunta | BG |
| pipe / pipe segment (`IfcPipeSegment`) | tubo | boru | rura | buis | trubka | ống | pipa | لوله | צינור | труба | құбыр | rør | rör | putki | WD |
| duct / duct segment (`IfcDuctSegment`) | canalizzazione aeraulica | hava kanalı | kanał wentylacyjny | luchtkanaal | vzduchovod | ống gió | saluran udara | کانال هوا | תעלת אוויר | повітровід | ауа өткізгіш? | ventilasjonskanal | ventilationskanal | ilmanvaihtokanava | WD+BG |
| pipe / duct fitting (`IfcPipeFitting`) | raccordo | bağlantı parçası / fitting | kształtka | hulpstuk / fitting | tvarovka | phụ kiện ống | fitting pipa | اتصالات لوله | אביזר צנרת | фасонна частина | құбыр фитингі? | rørdel | rördel | putkiosa | BG |
| pump (`IfcPump`) | pompa | pompa | pompa | pomp | čerpadlo | máy bơm | pompa | پمپ | משאבה | насос / помпа | сорғы | pumpe | pump | pumppu | WD |
| fan (`IfcFan`) | ventilatore | vantilatör / fan | wentylator | ventilator | ventilátor | quạt | kipas | فن | מאוורר | вентилятор | желдеткіш | vifte / ventilator | fläkt | puhallin / tuuletin | WD+BG |
| boiler (`IfcBoiler`) | caldaia | kazan | kocioł | verwarmingsketel / ketel | kotel | nồi hơi / lò hơi | boiler / ketel uap | بویلر / دیگ | דוד חימום | котел | қазандық | kjele | värmepanna / panna | lämpökattila | WD+BG |
| heat exchanger (`IfcHeatExchanger`) | scambiatore di calore | ısı eşanjörü | wymiennik ciepła | warmtewisselaar | tepelný výměník | thiết bị trao đổi nhiệt | penukar panas | مبدل حرارتی | מחליף חום | теплообмінник | жылуалмастырғыш | varmeveksler | värmeväxlare | lämmönsiirrin | WD |
| valve (`IfcValve`) | valvola | vana / valf | zawór | ventiel / klep | ventil / armatura | van | katup / valve | شیر | שסתום | клапан / вентиль | клапан | ventil | ventil | venttiili | WD |
| chiller | refrigeratore (chiller) | soğutma grubu / chiller | agregat chłodniczy | koelmachine | chladicí jednotka | máy làm lạnh nước | chiller | چیلر | צ'ילר | чилер | чиллер | kjølemaskin | kylmaskin | jäähdytyskone | BG |
| air handling unit (AHU) | unità di trattamento aria (UTA) | klima santrali | centrala wentylacyjna | luchtbehandelingskast | vzduchotechnická jednotka | tổ hợp xử lý không khí | unit pengolah udara | هواساز | יחידת טיפול באוויר | вентиляційна установка | желдету қондырғысы | ventilasjonsaggregat | ventilationsaggregat | ilmanvaihtokone | BG |
| air terminal / diffuser (`IfcAirTerminal`) | diffusore / bocchetta | difüzör / menfez | anemostat / nawiewnik | luchtrooster / diffuser | vyústka | miệng gió | diffuser udara | دریچه هوا / دیفیوزر | מפזר אוויר | дифузор | ауа таратқыш? | tilluftsventil / don | luftdon | ilmanvaihdon päätelaite | BG |
| damper (`IfcDamper`) | serranda | damper / klape | przepustnica | klep | klapka | van điều tiết gió | damper | دمپر | דמפר | заслінка / клапан | дроссель? | spjeld | spjäll | pelti | BG |
| radiator | radiatore | radyatör | grzejnik | radiator | otopné těleso | bộ tản nhiệt | radiator | رادیاتور | רדיאטור | радіатор | радиатор | radiator | radiator | lämpöpatteri | BG |
| heat pump | pompa di calore | ısı pompası | pompa ciepła | warmtepomp | tepelné čerpadlo | bơm nhiệt | pompa kalor | پمپ حرارتی | משאבת חום | тепловий насос | жылу сорғысы? | varmepumpe | värmepump | lämpöpumppu | BG |
| tank (`IfcTank`) | serbatoio | tank / depo | zbiornik | tank / reservoir | nádrž | bể chứa | tangki | مخزن | מיכל | резервуар / бак | резервуар | tank | tank | säiliö | BG |
| sanitary terminal (`IfcSanitaryTerminal`) | apparecchio sanitario | sıhhi armatür | przybór sanitarny | sanitair | zařizovací předmět | thiết bị vệ sinh | perlengkapan saniter | وسایل بهداشتی | כלים סניטריים | сантехнічний прилад | санитарлық аспап? | sanitærutstyr | sanitetsporslin / armatur | vesikalusteet | BG |
| sprinkler | sprinkler | sprinkler | tryskacz (sprinkler) | sprinkler | sprinkler | đầu phun sprinkler | sprinkler | اسپرینکلر | ספרינקלר | спринклер | спринклер | sprinkler | sprinkler | sprinkleri | BG |
| light fixture (`IfcLightFixture`) | apparecchio illuminante / lampada | aydınlatma armatürü | oprawa oświetleniowa | lichtarmatuur | svítidlo | thiết bị chiếu sáng | lampu / luminer | چراغ | גוף תאורה | світильник | шам? | lysarmatur | belysningsarmatur | valaisin | WD+BG |
| cable (`IfcCableSegment`) | cavo elettrico | kablo | kabel elektryczny | kabel | kabel | dây cáp | kabel | کابل | כבל | електричний кабель | кабель | kabel | kabel | sähkökaapeli | WD |
| cable tray / carrier (`IfcCableCarrierSegment`) | passerella portacavi | kablo kanalı / tavası | drabinka / korytko kablowe | kabelgoot | kabelový žlab | máng cáp | rak kabel | سینی کابل | סולם כבלים / מגש כבלים | кабельний лоток | кабель науасы? | kabelrenne | kabelstege / kabelränna | kaapelihylly | BG |
| circuit breaker (`IfcProtectiveDevice`) | interruttore magnetotermico | kesici / sigorta | wyłącznik | installatieautomaat | jistič | aptomat / cầu dao tự động | pemutus daya | مدارشکن / کلید خودکار | מפסק זרם | автоматичний вимикач | автоматты ажыратқыш? | automatsikring | dvärgbrytare | johdonsuoja / suojakatkaisija | WD+BG |
| switchboard / distribution board | quadro elettrico | elektrik panosu | rozdzielnica | verdeelkast | rozvaděč | tủ điện | panel listrik | تابلو برق | לוח חשמל | розподільний щит | электр щиті? | tavle / sikringsskap | elcentral / ställverk | sähkökeskus | BG |
| socket outlet (`IfcOutlet`) | presa | priz | gniazdo wtykowe | stopcontact | zásuvka | ổ cắm | stopkontak | پریز | שקע | розетка | розетка | stikkontakt | eluttag | pistorasia | BG |
| switch (`IfcSwitchingDevice`) | interruttore | anahtar | łącznik | schakelaar | vypínač | công tắc | saklar | کلید | מתג | вимикач | ажыратқыш | bryter | strömbrytare | kytkin | BG |
| transformer (`IfcTransformer`) | trasformatore | transformatör | transformator | transformator | transformátor | máy biến áp | transformator | ترانسفورماتور | שנאי | трансформатор | трансформатор | transformator | transformator | muuntaja | BG |
| sensor (`IfcSensor`) | sensore | sensör | czujnik | sensor | senzor | cảm biến | sensor | حسگر | חיישן | датчик | бергіш / сенсор | sensor | sensor | anturi | WD |
| thermostat | termostato | termostat | termostat | thermostaat | termostat | bộ điều nhiệt | termostat | ترموستات | תרמוסטט | термостат | термостат | termostat | termostat | termostaatti | BG |
| meter | contatore | sayaç | licznik | meter | měřič | đồng hồ đo | meteran | کنتور | מונה | лічильник | есептегіш | måler | mätare | mittari | BG |
| building automation | automazione degli edifici | bina otomasyonu | inteligentny budynek / automatyka budynkowa | gebouwautomatisering | automatizace budov | tự động hóa tòa nhà | otomasi bangunan | ساختمان هوشمند | אוטומציה בבניין | іммотика | ғимарат автоматикасы? | bygningsautomatisering | fastighetsautomation | rakennusautomaatio | WD+WK(TR)+BG |

**Wikidata quirks (what the label literally says versus what a BIM person would write).** These labels are encyclopedia concept names, not BIM vocabulary [1][2]: Turkish `wall` = "dik duvar" (upright wall; in practice "duvar"), Turkish `beam` = "Kiriş (mimarlık)"; Finnish `wall` = "muuri" (masonry wall or fence; the building wall is "seinä"); Finnish `column` = "Pylväs" and Swedish `column` = "kolonn" (architectural column; the structural member is "pilari" / "pelare"); Norwegian `mechanical fan` = "kjøkkenventilator" (kitchen extractor hood); Norwegian `boiler` = "dampkjele" (steam boiler); Swedish `boiler` = "Oljepanna" (oil boiler); Dutch `boiler` = "stoomketel" (steam boiler); Dutch `window` = "venster" (the everyday and construction word is "raam"); Dutch `storey` = "etage" (BIM and construction use "bouwlaag"); Kazakh `beam` is a long label meaning "statically determinate beam"; Hebrew `material` = "חומר גלם" (raw material); Vietnamese `storey` = "lầu" (southern colloquial; standard is "tầng") and `boiler` = "Lò hơi công nghiệp" (industrial boiler); Indonesian `storey` = "tingkat" (the common building word is "lantai"); Polish `room` = "pokój" (a living room; IFC `IfcSpace` is "pomieszczenie"); Czech `curtain wall` has no label (only the English name is used). I replaced or supplemented these in the tables with the usual professional term, which is background knowledge (unverified).

### E. Documentation, process, roles and information requirements

| EN | IT | TR | PL | NL | CS | VI | ID | FA | HE | UK | KK | NO | SV | FI | Basis |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| technical drawing | disegno tecnico | teknik resim | rysunek techniczny | technisch tekenen / tekening | technické kreslení / výkres | bản vẽ kỹ thuật | gambar teknik | نقشه‌کشی / نقشه | שרטוט טכני | креслення | сызба | teknisk tegning | teknisk ritning | tekninen piirustus | WD+BG |
| drawing sheet | tavola | pafta / çizim paftası | arkusz rysunkowy | tekenblad | výkres / list | tờ bản vẽ | lembar gambar | برگه نقشه | גיליון שרטוט | аркуш креслення | сызба парағы | tegningsark | ritningsblad | piirustusarkki | BG |
| scale | scala | ölçek | skala | schaal | měřítko | tỷ lệ | skala | مقیاس | קנה מידה | масштаб | масштаб | målestokk | skala | mittakaava | BG |
| dimension | quota | ölçü | wymiar | maat / maatvoering | kóta | kích thước | dimensi | اندازه / ابعاد | מידה | розмір | өлшем | mål | mått | mitta | BG |
| annotation / tag | etichetta | etiket / not | opis / etykieta | tag / annotatie | popisek / štítek | ghi chú / nhãn | anotasi / tag | برچسب | תגית / הערה | позначка / анотація | белгі | merke / annotasjon | etikett | tunniste / huomautus | BG |
| revision | revisione | revizyon | rewizja | revisie | revize | bản sửa đổi | revisi | بازنگری | רוויזיה | ревізія | қайта қарау | revisjon | revision | versio / revisio | BG |
| issue / clash report (BCF topic) | segnalazione | sorun / konu | zgłoszenie | issue / probleem | problém / podnět | vấn đề | isu | مسئله | בעיה | зауваження / проблема | мәселе | avvik / sak | ärende | ongelma / huomautus | BG |
| deliverable | elaborato / consegna | teslim edilecek ürün | dokumentacja / produkt końcowy | op te leveren product | výstup | sản phẩm bàn giao | luaran / dokumen serah | تحویلی | תוצר | результат / документація | нәтиже | leveranse | leverans | toimitus / tuotos | BG |
| specification | capitolato / specifica | şartname | specyfikacja | specificatie / bestek | specifikace | đặc tả / yêu cầu kỹ thuật | spesifikasi | مشخصات فنی | מפרט | специфікація | техникалық сипаттама | spesifikasjon / beskrivelse | specifikation / beskrivning | erittely / selostus | BG |
| client / employer | committente | işveren / yatırımcı | zamawiający / inwestor | opdrachtgever | objednatel / investor | chủ đầu tư | pemberi tugas / pemilik | کارفرما | מזמין / יזם | замовник | тапсырыс беруші | byggherre | byggherre / beställare | rakennuttaja / tilaaja | BG |
| contractor | appaltatore / impresa | müteahhit / yüklenici | wykonawca | aannemer | zhotovitel / dodavatel | nhà thầu | kontraktor | پیمانکار | קבלן | підрядник | мердігер | entreprenør | entreprenör | urakoitsija | BG |
| designer / consultant | progettista | proje müellifi / tasarımcı | projektant | ontwerper / adviseur | projektant | nhà thiết kế / tư vấn | perencana / konsultan | طراح / مشاور | מתכנן / יועץ | проєктувальник | жобалаушы | prosjekterende / rådgiver | projektör / konsult | suunnittelija | BG |
| architect | architetto | mimar | architekt | architect | architekt | kiến trúc sư | arsitek | معمار | אדריכל | архітектор | сәулетші | arkitekt | arkitekt | arkkitehti | WD |
| structural engineer | ingegnere strutturista | statik mühendisi / inşaat mühendisi | konstruktor | constructeur | statik | kỹ sư kết cấu | insinyur struktur | مهندس سازه | מהנדס קונסטרוקציה | інженер-конструктор | құрылым инженері? | konstruktør | konstruktör | rakennesuunnittelija | WK(FI)+BG |
| MEP engineer | ingegnere impiantista | tesisat mühendisi | projektant instalacji | installatieadviseur | projektant TZB | kỹ sư cơ điện | insinyur MEP | مهندس تأسیسات | מהנדס מערכות | інженер інженерних систем | инженерлік жүйелер инженері? | rådgivende ingeniør VVS/el | installationskonsult | LVI-suunnittelija / sähkösuunnittelija | BG |
| BIM coordinator | coordinatore BIM | BIM koordinatörü | koordynator BIM | BIM-coördinator | BIM koordinátor | điều phối viên BIM | koordinator BIM | هماهنگ‌کننده BIM | מתאם BIM | BIM-координатор | BIM үйлестірушісі | BIM-koordinator | BIM-samordnare | BIM-koordinaattori / tietomallikoordinaattori | BG |
| BIM manager | BIM manager | BIM yöneticisi | BIM manager | BIM-manager | BIM manažer | quản lý BIM | manajer BIM | مدیر BIM | מנהל BIM | BIM-менеджер | BIM-менеджер | BIM-leder | BIM-ansvarig | BIM-päällikkö / tietomallipäällikkö | BG |
| common data environment (CDE) | ambiente di condivisione dei dati | ortak veri ortamı | wspólne środowisko danych | gemeenschappelijke data-omgeving | společné datové prostředí | môi trường dữ liệu chung | lingkungan data bersama | محیط داده مشترک | סביבת נתונים משותפת | загальне середовище даних | ортақ деректер ортасы | felles datamiljø | gemensam datamiljö | yhteinen tietoympäristö | BG |
| employer's information requirements (EIR) | capitolato informativo | işveren bilgi gereksinimleri | wymagania wymiany informacji | uitwisselingsinformatie-eisen | požadavky na výměnu informací | yêu cầu trao đổi thông tin | persyaratan pertukaran informasi | الزامات تبادل اطلاعات | דרישות להחלפת מידע | вимоги до обміну інформацією | ақпарат алмасу талаптары? | informasjonskrav fra byggherre | beställarens informationskrav | tilaajan tietovaatimukset | BG (IT: "capitolato informativo" appears in an Italian contract listing seen in search [36]) |
| BIM execution plan (BEP) | piano di gestione informativa | BIM uygulama planı | BIM plan realizacji | BIM-uitvoeringsplan | plán realizace BIM | kế hoạch thực hiện BIM | rencana pelaksanaan BIM | برنامه اجرایی BIM | תוכנית ביצוע BIM | план реалізації BIM | BIM іске асыру жоспары? | BIM-gjennomføringsplan | BIM-genomförandeplan | BIM-toteutussuunnitelma | BG |
| level of detail / development (LOD) | livello di sviluppo (LOD) | detay seviyesi (LOD) | poziom szczegółowości (LOD) | detailniveau (LOD) | úroveň podrobnosti (LOD) | mức độ chi tiết (LOD) | tingkat detail (LOD) | سطح جزئیات (LOD) | רמת פירוט (LOD) | рівень деталізації (LOD) | егжей-тегжей деңгейі (LOD)? | detaljeringsgrad | detaljeringsgrad | tarkkuustaso (LOD) | WK(UK,FA)+BG |
| level of information need (LOIN) | livello di fabbisogno informativo | gerekli bilgi seviyesi | poziom potrzeb informacyjnych | informatiebehoefteniveau | úroveň potřeby informací | mức độ cần thông tin | tingkat kebutuhan informasi | سطح نیاز اطلاعاتی | רמת צורך במידע | рівень потреби в інформації | ақпарат қажеттілігі деңгейі? | informasjonsbehovsnivå | informationsbehovsnivå | tietotarvetaso | IT via [36] (UNI EN 17412-1); rest BG |
| as-built model / drawings | modello as-built / come costruito | as-built / uygulama sonrası | dokumentacja powykonawcza | as-built / revisietekeningen | dokumentace skutečného provedení | bản vẽ hoàn công | gambar terbangun (as-built) | نقشه‌های اجرایی (As Built) | תכניות עדות (As Made) | виконавча документація | орындаушылық құжаттама | som bygget (SOM-bygget) | relationshandlingar | toteumamalli / toteutumapiirustukset | WK(FA)+BG |
| contract | contratto | sözleşme | umowa | contract / overeenkomst | smlouva | hợp đồng | kontrak | قرارداد | חוזה | договір | шарт | kontrakt | avtal | sopimus | BG |

### F. Actions and software UI words

| EN | IT | TR | PL | NL | CS | VI | ID | FA | HE | UK | KK | NO | SV | FI | Basis |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| open (IFC model) | apri | aç | otwórz | openen | otevřít | mở | buka | باز کردن | פתח | відкрити | ашу | åpne | öppna | avaa | GS(PL: "Otwórz model IFC")+BG |
| import | importa / importazione | içe aktar | import | importeren | import | nhập | impor | وارد کردن | ייבוא | імпорт | импорттау | importer | importera | tuo | GS(IT,PL,CS)+BG |
| export | esporta / esportare | dışa aktar | eksport | exporteren | export | xuất | ekspor | خروجی گرفتن | ייצוא | експорт | экспорттау | eksporter | exportera | vie | GS(IT,PL)+BG |
| link / merge | collega / unisci | bağla / birleştir | łącz | koppelen / samenvoegen | připojit / sloučit | liên kết / hợp nhất | tautkan / gabungkan | پیوند / ادغام | קשר / מזג | зв'язати / об'єднати | байланыстыру / біріктіру | koble / flette | länka / slå ihop | linkitä / yhdistä | GS(PL "Łącz", CS "Připojení")+BG |
| save as | salva con nome | farklı kaydet | zapisz jako | opslaan als | uložit jako | lưu thành | simpan sebagai | ذخیره به عنوان | שמור בשם | зберегти як | ретінде сақтау | lagre som | spara som | tallenna nimellä | BG |
| filter | filtro / filtra | filtre | filtr / filtruj | filter | filtr | bộ lọc | filter | فیلتر | מסנן | фільтр | сүзгі | filter | filter | suodatin | GS(PL "Filtruj")+BG |
| select | seleziona | seç | zaznacz / wybierz | selecteren | vybrat | chọn | pilih | انتخاب | בחר | вибрати | таңдау | velg | markera / välj | valitse | BG |
| search / find | cerca | ara | szukaj | zoeken | hledat | tìm kiếm | cari | جستجو | חפש | пошук | іздеу | søk | sök | hae | BG |
| list / show all | elenca / mostra tutti | listele / tümünü göster | wyświetl / pokaż wszystkie | toon alle / lijst | zobrazit vše / seznam | liệt kê / hiển thị tất cả | tampilkan semua | فهرست / نمایش همه | הצג הכל | показати всі / перелік | барлығын көрсету | vis alle / list | visa alla / lista | näytä kaikki / luettele | BG |
| count | conta | say | policz | tellen | spočítat | đếm | hitung | شمارش | ספור | порахувати | санау | tell | räkna | laske | BG |
| create | crea | oluştur | utwórz | maken | vytvořit | tạo | buat | ایجاد | צור | створити | жасау | opprett | skapa | luo | BG |
| modify / edit | modifica | düzenle | modyfikuj / edytuj | wijzigen | upravit | sửa | ubah | ویرایش | ערוך | змінити | өзгерту | endre | ändra | muokkaa | BG |
| delete | elimina | sil | usuń | verwijderen | smazat | xóa | hapus | حذف | מחק | видалити | жою | slett | ta bort | poista | BG |
| move | sposta | taşı | przesuń | verplaatsen | přesunout | di chuyển | pindahkan | جابه‌جایی | הזז | перемістити | жылжыту | flytt | flytta | siirrä | BG |
| copy | copia | kopyala | kopiuj | kopiëren | kopírovat | sao chép | salin | کپی | העתק | копіювати | көшіру | kopier | kopiera | kopioi | BG |
| rotate | ruota | döndür | obróć | roteren | otočit | xoay | putar | چرخش | סובב | повернути | бұру | roter | rotera | kierrä | BG |
| mirror | specchia | aynala | odbij lustrzanie | spiegelen | zrcadlit | đối xứng | cerminkan | قرینه | שקף | віддзеркалити | айналау | speil | spegla | peilaa | BG |
| set parameter / property value | imposta parametro | parametre değeri ata | ustaw parametr | parameter instellen | nastavit parametr | đặt tham số | atur parameter | تنظیم پارامتر | קבע פרמטר | встановити параметр | параметрді орнату | sett parameter | ange parameter | aseta parametri | BG |
| validate / check | verifica / valida | doğrula / kontrol et | zweryfikuj / sprawdź | valideren / controleren | ověřit / zkontrolovat | kiểm tra / xác thực | validasi / periksa | اعتبارسنجی / بررسی | אמת / בדוק | перевірити | тексеру | valider / kontroller | validera / kontrollera | tarkista / validoi | BG |
| settings / options | impostazioni / opzioni | ayarlar / seçenekler | ustawienia / opcje | instellingen / opties | nastavení / možnosti | cài đặt / tùy chọn | pengaturan / opsi | تنظیمات | הגדרות | налаштування | баптаулар | innstillinger | inställningar | asetukset | BG |
| translator / converter (IFC export/import preset) | traduttore | çevirici | translator | vertaler | převodník | bộ chuyển đổi | penerjemah | مبدل | ממיר | транслятор | аудармашы / түрлендіргіш? | oversetter | översättare | kääntäjä | GS(PL "Translatory", CS "převodníky", NL via search summary)+BG |
| IFC Project Manager | gestione progetto IFC | IFC proje yöneticisi | Menedżer projektu IFC | IFC-projectbeheer | správce IFC projektu | trình quản lý dự án IFC | pengelola proyek IFC | مدیر پروژه IFC | מנהל פרויקט IFC | менеджер проєкту IFC | IFC жоба менеджері | IFC-prosjektbehandler | IFC-projekthanterare | IFC-projektinhallinta | GS(PL)+BG |

## Where official or semi-official localized IFC vocabulary actually lives

| Place | What it gives you | Notes |
|---|---|---|
| IFC 4.3 development docs (buildingSMART) | Language dropdown for entity, attribute and property-set names; German shown for `IfcWall` in the announcement | Dev server only, not in the official 4.3.2 snapshot [28][34] |
| `buildingSMART/IFC-translations` (GitHub) | Source `input` branch and Crowdin-fed `translations` branch, "30+ languages" | Do not edit by hand; "All rights reserved until formal release" per its README [32] |
| bSDD (buildingSMART Data Dictionary) | Same machine codes, translated display text; API returns one language per request via a `languageCode` parameter | Only chapter-approved translations appear for the IFC dictionary; non-IFC dictionaries can carry any translation [30][31] |
| Graphisoft Archicad help | Localized IFC chapter (translators, IFC Project Manager, data mapping) in IT, PL, CS and others | Archicad names, not buildingSMART names [7][8][9][10][37] |
| Autodesk Revit help | Localized Revit vocabulary in IT, PL, CS | Revit names; Revit's IFC export vocabulary was not fetched [13][14][15] |
| Wikipedia / Wikidata | Concept labels in all fifteen languages except Kazakh BIM article | Generic, community-edited [1]-[3][17]-[26] |

Because the IFC file keeps English codes, a user may type `стіна`, `קיר` or `دیوار` in a prompt, but an MCP server that filters by IFC class must still map it to `IfcWall`. Never expect `IfcWall` itself to appear in translated form in the model output [30][31].

## National and regional context (what was found)

| Country / language | Found in this research | Source |
|---|---|---|
| Italy | UNI 11337-1:2017 (digital management of information processes, listed as current), UNI EN ISO 19650 and UNI EN 17412-1 (level of information need) referenced in Italian tenders; "capitolato informativo" is the Italian contract-document name used in tenders | [36] |
| Finland | New Building Act (Rakentamislaki) in force from 1 January 2025; a Ministry of the Environment decree on the content of design models and authority inspections; Archives Act requirements for building models; buildingSMART Finland; earlier ProIT product-model project 2002-2006; ISO/PAS 16739 and ISO 19650 named | [23] |
| Indonesia | Permen PUPR No. 22/PRT/M/2018 on state buildings and Government Regulation No. 16 of 2021 on buildings, named in the BIM article | [22] |
| Netherlands | Rijksvastgoedbedrijf (RVB) BIM norm, buildingSMART Benelux chapter, ISO 12006-3 (IFD), IDM named in the article | [26] |
| Ukraine | Article cites ISO 19650:2019 and ISO 16739:2013 (no DSTU named) | [20] |
| Israel | BIM ISRAEL forum (founded 2015) aims to write an Israeli BIM standard; status today is (unverified) | [18] |
| Norway | buildingSMART Norge and IFC named | [24] |
| Sweden | BIM Alliance listed among sources | [25] |
| Vietnam | Wikipedia article names no Vietnamese standard | [21] |
| Iran | Article names no Iranian guideline | [19] |
| Turkey, Czechia, Poland, Kazakhstan | No national BIM standard found (search budget ran out); see Gaps | none |

## Using the glossary to judge an MCP tool (illustrative prompts)

These test prompts are invented (illustrative) to show how a localized request maps to IFC; they were not harvested from real users.

| Language | Prompt (illustrative) | Expected IFC meaning |
|---|---|---|
| IT | "Elenca tutti i muri del piano terra" | `IfcWall` contained in the `IfcBuildingStorey` whose name matches "Piano terra" |
| TR | "2. kattaki tüm kapıları listele" | `IfcDoor` in storey named like "2. Kat" |
| PL | "Pokaż wszystkie drzwi na kondygnacji 1" | `IfcDoor` in `IfcBuildingStorey` "Kondygnacja 1" |
| NL | "Hoeveel ramen zitten er op de begane grond?" | count of `IfcWindow` in storey "Begane grond" |
| CS | "Vypiš všechny stěny na podlaží 2" | `IfcWall` in `IfcBuildingStorey` "Podlaží 2" |
| VI | "Liệt kê tất cả cửa sổ ở tầng 3" | `IfcWindow` in storey "Tầng 3" |
| ID | "Tampilkan semua kolom di lantai dasar" | `IfcColumn` in storey "Lantai dasar" |
| FA | "همه دیوارهای طبقه همکف را فهرست کن" | `IfcWall` in storey "همکف" |
| HE | "הצג את כל הדלתות בקומה 2" | `IfcDoor` in storey "קומה 2" |
| UK | "Покажи всі вікна на першому поверсі" | `IfcWindow` in storey "Перший поверх" |
| KK | "Бірінші қабаттағы барлық есіктерді көрсет" (low confidence) | `IfcDoor` in storey "Бірінші қабат" |
| NO | "Vis alle vegger i første etasje" | `IfcWall` in storey "1. etasje" |
| SV | "Visa alla dörrar på våning 2" | `IfcDoor` in storey "Våning 2" |
| FI | "Listaa kaikki ikkunat kerroksesta 2" | `IfcWindow` in storey "Kerros 2" |

Things the tester should check: the tool matches the storey by its *name string in the model* (which may be in any language or just "Level 1"), not by translating; the class names in the answer are IFC English names; counts are identical regardless of the request language; and ambiguous words ("floor", "zone") are clarified (see pitfalls).

## Typical questions people ask about this

Real threads found (links in Sources); others are marked (illustrative).

1. "Proper way to access translations of IFC entities?" Asked because the IFC HTML documentation shows translations but XSD and EXPRESS only have English; answer: use the buildingSMART translations platform output, bSDD and its API [30].
2. "Initiative IFC4-Translation: English to local language, call for bS chapter support" A call for chapters to back translating IFC4 definitions, enumerations and properties [29].
3. "Translations added to the IFC4.3 dev server" Announcement that a language dropdown now shows German terms for `IfcWall`; absent from the 4.3.2 snapshot [28].
4. "bSDD localization" Discussion of language codes, who may add translations, and approved versus community dictionaries [31].
5. A German question on the Graphisoft community asking whether an IFC4 translator following German rules exists in Archicad (seen in search results only, not opened) [39].
6. A Graphisoft community wish "Use bsDD translation for IFC content" (seen in search results only; page returned 403 when fetched) [40].
7. (illustrative) "Which Polish word does Archicad use for IfcZone and which for IfcSpace?" Answer from the PL help: "Strefa IFC" for `IfcZone` and "Strefa" for `IfcSpace`, so the same Polish word is used for two different IFC concepts [8].
8. (illustrative) "Why does my Italian Revit show 'istanza' but my colleague's Polish Revit shows 'wystąpienie'?" Both mean instance; Autodesk uses different words in each locale [13][14].
9. (illustrative) "Is 'Metka' (PL) or 'Visačka' (CS) the same as GlobalId?" No, it is the IFC `Tag`, derived from the Archicad element ID [8][10].
10. (illustrative) "Can I get the IFC file itself in Turkish or Hebrew?" No; only the documentation and dictionary display are localized, the file keeps English codes [30][31].
11. (illustrative) "Does the MCP tool understand 'quota' (IT) as dimension or as elevation?" In Italian drawings "quota" means both a dimension and a spot elevation (unverified); the tool should ask or check context.
12. (illustrative) "Which Norwegian word should I use for 'floor': etasje, gulv or dekke?" `IfcBuildingStorey` = etasje, floor finish = gulv, structural slab (`IfcSlab`) = dekke (unverified).
13. (illustrative) "Why is 'column' translated as 'pylväs' in Finnish but the structural engineer says 'pilari'?" Wikidata uses the architectural-column concept [1]; construction uses "pilari" (unverified).
14. (illustrative) "In Dutch do I say 'verdieping', 'etage' or 'bouwlaag' for IfcBuildingStorey?" Wikidata gives "etage" [1]; Dutch BIM practice commonly says "bouwlaag" (unverified).
15. (illustrative) "How do I ask for all rooms in Czech, 'místnost' or 'prostor'?" `IfcSpace` is "místnost" in everyday use; the Archicad CS help leaves `IfcSpace` untranslated [10].
16. (illustrative) "Does Kazakh have an official BIM glossary?" None found in this research; see Gaps.
17. (illustrative) "Does the Indonesian state require BIM?" Permen PUPR No. 22/PRT/M/2018 is named for state buildings; details of the obligation were not verified [22].
18. (illustrative) "Is there a Finnish standard word for IFC model?" Finnish practice says "tietomalli" (information model) and "IFC-tiedosto" [23].
19. (illustrative) "How is clash detection called in Swedish?" "kollisionskontroll" [25].
20. (illustrative) "Can the MCP server handle prompts mixing Persian text with `IfcWall` and Persian digits?" See pitfalls on directionality and digits.

## Common pitfalls and misconceptions

- **IFC class names are never translated.** `IfcWall`, `IfcBuildingStorey`, `Pset_WallCommon` are identical in every language; translation is only a display layer [30][31]. A tool that returns "IfcMur" or "IfcSciana" is wrong.
- **Same word, two IFC concepts.** In the Polish and Italian Archicad help, the plain word "Strefa" / "Zona" is `IfcSpace` (a room), while "Strefa IFC" / "Zona IFC" is `IfcZone` (a grouping of spaces) [8][9]. Many other languages blur the two.
- **Tag is not GlobalId.** Polish "Metka" and Czech "Visačka" are `Tag` (an application ID), not the 22-character `GlobalId` [8][10].
- **"Floor" has three meanings.** Level/storey (`IfcBuildingStorey`: piano, kat, kondygnacja, etasje, kerros), structural slab (`IfcSlab`: solaio, döşeme, dekke, laatta) and floor finish (`IfcCovering`: pavimento, zemin kaplaması). Czech Revit text uses "podlaží" for both "floor" and "level" [15]; Revit's own "Floor" category exports to `IfcSlab` (background, unverified).
- **Wikidata is not a BIM dictionary.** Examples: Norwegian "kjøkkenventilator" for fan, Finnish "muuri" for wall, Turkish "dik duvar" [1] (see the quirks note under table D).
- **Archicad terms are not buildingSMART terms.** The Italian "Struttura Composta" or Czech "Sendvič" (layer set) are Graphisoft choices [9][10]; the official translation of `IfcMaterialLayerSet` may differ (unverified).
- **Instance wording differs by Revit locale.** Italian "istanza", Polish "wystąpienie" (not "egzemplarz"), Czech keeps "instance" [13][14][15].
- **Right-to-left text.** Persian and Hebrew prompts mix RTL words with LTR identifiers such as `IfcWall`, GUIDs and numbers. Persian text may use Persian digits (۰-۹) or Arabic-Indic digits; Arabic letters ك/ي are sometimes typed instead of Persian ک/ی, so string matching should normalize them (background knowledge, unverified).
- **Turkish dotted/dotless I.** Case-insensitive matching with a Turkish locale can turn "IFC" into "ıfc" in some runtimes (a well-known behavior in .NET/Java, unverified for any particular MCP server); entity-name matching should be locale-independent.
- **Finnish and other inflection.** Finnish "seinä" becomes "seinät", "seinien", "seinässä"; Polish, Czech, Ukrainian and Kazakh also inflect nouns. A keyword search on "ściana" will miss "ścian" or "ścianę" (unverified for a specific tool).
- **Kazakh script.** Kazakh is written in Cyrillic today; a Latin-based alphabet has been planned for years, so a tester may see both (unverified).
- **English abbreviations stay.** Do not treat "BEP", "EIR", "CDE", "LOD" as untranslated errors; local texts keep them [20][26].
- **Machine-translated fields.** Do not expect translated property values (a wall named "Basic Wall: Generic - 200mm" stays as is). Names come from the authoring model and may be in any language.
- **bSDD approval status can change.** The April 2023 statement that no IFC translations were approved yet is old; check bSDD now [30].
- **Kazakh, Hebrew, Persian IFC documentation may not exist.** The IFC 4.3 docs language list seen in a search snippet did not show Persian, Hebrew, Kazakh, Vietnamese, Indonesian or Ukrainian among the first fifteen flags (the list was cut off, so unverified) [34].

## Gaps

- WebSearch budget for the session ran out after about 17 searches, so national BIM standards were not searched for Turkey, Netherlands (NEN), Czechia, Vietnam, Ukraine (DSTU), Kazakhstan (ST RK), Norway, Sweden, Poland. Native-language searches for these topics were attempted but returned "budget used up". Follow-up searches are needed.
- Pages that returned errors: ISO standard page iso.org/standard/84123.html (404), buildingSMART IFC page and IFC 4.3 development docs (403), Graphisoft Finnish IFC page (404, Finnish help not found), Graphisoft community wish thread (403), Autodesk "Terminologia di Revit" page (503), Kazakh Wikipedia BIM title (does not exist).
- translations.buildingsmart.org only showed a Crowdin Enterprise landing page; per-language progress could not be read [35].
- Revit's own IFC exporter vocabulary (export setups, "IFC Class" parameter names) in these languages was not fetched.
- Most cells marked BG are professional usage from background knowledge and not verified; Kazakh cells marked "?" are weakest.
- No suspicious, pirated or phishing sites were encountered or linked; nothing was downloaded or executed.

## Sources

Wikidata and Wikipedia (labels and article text; read as web pages only):

- [1] Wikidata API labels, wall/door/window/roof/column/beam/stairs/storey/ceiling/foundation/curtain wall/handrail/elevator/pipe/duct/pump/fan/boiler/heat exchanger/valve: https://www.wikidata.org/w/api.php?action=wbgetentities&ids=Q42948|Q36794|Q35473|Q83180|Q4817|Q3705329|Q12511|Q831691|Q221706|Q191360|Q16770122|Q2051212|Q132911|Q41551|Q1453244|Q134574|Q6498398|Q3195517|Q189124|Q208443&props=labels&languages=en|it|tr|pl|nl|cs|vi|id|fa|he|uk|kk|nb|sv|fi&format=json&formatversion=2
- [2] Wikidata API labels, light fixture/cable/circuit breaker/sensor/room/building/concrete/steel/brick/glass/wood/insulation/material/unit/bill of quantities/floor plan/technical drawing/point cloud: https://www.wikidata.org/w/api.php?action=wbgetentities&ids=Q815738|Q188447|Q211058|Q167676|Q180516|Q41176|Q184190|Q22657|Q11427|Q40089|Q11469|Q287|Q918306|Q214609|Q47574|Q695894|Q18965|Q192521|Q1899648&props=labels&languages=en|it|tr|pl|nl|cs|vi|id|fa|he|uk|kk|nb|sv|fi&format=json&formatversion=2
- [3] Wikidata API labels, BIM/IFC/Revit/architect/CAD/interoperability/structural engineering/collision detection/open standard/FM/quantity surveyor/construction management/building automation/laser scanning/MEP/parametric design/digital twin/GIS: https://www.wikidata.org/w/api.php?action=wbgetentities&ids=Q842017|Q979630|Q1457492|Q42973|Q184793|Q749647|Q633538|Q1550329|Q681263|Q837060|Q2067634|Q811501|Q1149653|Q1361664|Q6804476|Q18386598|Q25099680|Q483130&props=labels&languages=en|it|tr|pl|nl|cs|vi|id|fa|he|uk|kk|nb|sv|fi&format=json&formatversion=2
- [4] Wikipedia API interlanguage links for BIM, IFC, Revit: https://en.wikipedia.org/w/api.php?action=query&titles=Building_information_modeling|Industry_Foundation_Classes|Revit|Autodesk_Revit|Level_of_detail_(BIM)|Common_data_environment|ISO_19650&prop=langlinks&lllimit=500&format=json&formatversion=2
- [5] Wikipedia API Wikibase IDs for building elements and materials: https://en.wikipedia.org/w/api.php?action=query&titles=Wall|Door|Window|Roof|Column|Beam_(structure)|Stairs|Storey|Ceiling|Foundation_(engineering)|Curtain_wall|Handrail|Ramp|Elevator|Pipe_(fluid_conveyance)|Duct_(flow)|Pump|Fan_(machine)|Boiler|Heat_exchanger|Valve|Light_fixture|Electrical_cable|Circuit_breaker|Sensor|Room|Building|Reinforced_concrete|Concrete|Steel|Brick|Glass|Wood|Thermal_insulation|Material|Unit_of_measurement|Bill_of_quantities|Floor_plan|Technical_drawing|Clash_detection|Point_cloud|Slab_(architecture)&prop=pageprops&ppprop=wikibase_item&format=json&formatversion=2&redirects=1
- [6] Wikipedia API Wikibase IDs for BIM concept pages: https://en.wikipedia.org/w/api.php?action=query&titles=Building_information_modeling|Industry_Foundation_Classes|Autodesk_Revit|Common_data_environment|Level_of_development|Computer-aided_design|Facility_management|Quantity_surveying|Building_automation|Interoperability|Open_standard|Architect|Structural_engineering|Mechanical,_electrical,_and_plumbing|Construction_management|Geographic_information_system|Digital_twin|Parametric_design|Laser_scanning|Collision_detection&prop=pageprops&ppprop=wikibase_item&format=json&formatversion=2&redirects=1

Graphisoft (Archicad help):

- [7] Polish IFC chapter start page and sidebar (Archicad 30): https://help.graphisoft.com/AC/30/POL/Topics/121_IFC/121_IFC-1.html
- [8] Polish "Rodzaje danych IFC" (Archicad 30): https://help.graphisoft.com/AC/30/POL/Topics/121_IFC/121_IFC-48.html (the appendix page 121_IFC-46.html contained only navigation)
- [9] Italian IFC data types (Archicad 27): https://help.graphisoft.com/AC/27/ITA/_AC27_Help/121_IFC/121_IFC-48.htm
- [10] Czech IFC data types (Archicad 25): https://help.graphisoft.com/AC/25/CZE/_AC25_Help/121_IFC/121_IFC-47.htm
- [11] English IFC Data Types (Archicad 27): https://help.graphisoft.com/AC/27/INT/_AC27_Help/121_IFC/121_IFC-48.htm
- [12] German IFC data types (Archicad 23, used only to confirm structure): https://help.graphisoft.com/AC/23/GER/_AC23_Help/115_IFC/115_IFC-48.htm

Autodesk Revit help:

- [13] Italian, Families (Revit 2025): https://help.autodesk.com/cloudhelp/2025/ITA/Revit-GetStarted/files/GUID-7AEC5D66-C2E0-40E2-9504-3CC13781B87A.htm
- [14] Polish, same page: https://help.autodesk.com/cloudhelp/2025/PLK/Revit-GetStarted/files/GUID-7AEC5D66-C2E0-40E2-9504-3CC13781B87A.htm
- [15] Czech, same page: https://help.autodesk.com/cloudhelp/2025/CSY/Revit-GetStarted/files/GUID-7AEC5D66-C2E0-40E2-9504-3CC13781B87A.htm
- [16] Italian help page seen in a search summary for "abaco" (schedule): https://help.autodesk.com/cloudhelp/2016/ITA/Revit-Customize/files/GUID-921F7A15-D191-4F75-8243-4989C482E253.htm

Wikipedia articles (running text used for terminology; community-edited, not official):

- [17] Turkish: https://tr.wikipedia.org/wiki/Yapı_bilgi_modellemesi
- [18] Hebrew: https://he.wikipedia.org/wiki/מידול_האינפורמציה_של_המבנה
- [19] Persian: https://fa.wikipedia.org/wiki/مدل‌سازی_اطلاعات_ساختمان
- [20] Ukrainian: https://uk.wikipedia.org/wiki/Інформаційне_моделювання_будівель
- [21] Vietnamese: https://vi.wikipedia.org/wiki/Mô_hình_thông_tin_xây_dựng
- [22] Indonesian: https://id.wikipedia.org/wiki/Pemodelan_informasi_bangunan
- [23] Finnish: https://fi.wikipedia.org/wiki/Rakennuksen_tietomalli
- [24] Norwegian: https://no.wikipedia.org/wiki/Bygningsinformasjonsmodellering
- [25] Swedish: https://sv.wikipedia.org/wiki/Building_Information_Model
- [26] Dutch: https://nl.wikipedia.org/wiki/Bouwwerkinformatiemodel
- [27] Kazakh title tried (does not exist): https://kk.wikipedia.org/wiki/Building_Information_Modeling

buildingSMART:

- [28] Translations added to the IFC4.3 dev server: https://forums.buildingsmart.org/t/translations-added-to-the-ifc4-3-dev-server/6299
- [29] Initiative IFC4-Translation, call for chapter support: https://forums.buildingsmart.org/t/initiative-ifc4-translation-english-local-language-call-for-bs-chapter-support/1817
- [30] Proper way to access translations of IFC entities: https://forums.buildingsmart.org/t/proper-way-to-access-translations-of-ifc-entities/4092
- [31] bSDD localization: https://forums.buildingsmart.org/t/bsdd-localization/5120
- [32] IFC translations repository: https://github.com/buildingSMART/IFC-translations
- [33] IFC4.3.x development repository (README points to the translations repo): https://github.com/buildingSMART/IFC4.3.x-development
- [34] IFC 4.3 documentation index (language flags seen in a search summary only): https://ifc43-docs.standards.buildingsmart.org/IFC/RELEASE/IFC4x3/HTML/index.htm
- [35] Translation platform landing page (Crowdin Enterprise, no detail): https://translations.buildingsmart.org/

Standards listings and other (seen in search results, not opened unless stated):

- [36] UNI 11337-1:2017 shop listing: https://shop.standards.ie/en-ie/standards/uni-11337-1-2017-1098422_saig_uni_uni_2555224 and UNI EN ISO 16739-1:2020 listing: https://infostore.saiglobal.com/en-au/standards/uni-en-iso-16739-1-2020-1184526_saig_uni_uni_2828105/ ; Italian "capitolato informativo" contract listing: https://lawinsider.com/it/contracts/j0J4OKQMjS
- [37] Localized Graphisoft IFC pages seen in search results (confirm which languages exist): https://help.graphisoft.com/AC/29/ITA/_AC29_Help/121_IFC/121_IFC-5.htm , https://help.graphisoft.com/AC/25/CZE/_AC25_Help/121_IFC/121_IFC-5.htm , https://help.graphisoft.com/AC/23/CZE/_AC23_Help/115_IFC/115_IFC-24.htm , https://help.graphisoft.com/AC/29/POL/_AC29_Help/121_IFC/121_IFC-5.htm , https://help.graphisoft.com/AC/27/HUN/_AC27_Help/121_IFC/121_IFC-4.htm
- [38] Polish Mechanik article describing BIM ("model informacyjny budynku"), seen in search results: https://www.mechanik.media.pl/pliki/do_pobrania/artykuly/19/0425-0434.pdf
- [39] Graphisoft community (German) IFC4 translator question, seen in search results: https://community.graphisoft.com/t5/Kollaboration-mit-anderer/Gibt-es-einen-IFC4-Translator-nach-deutschen-Regeln-in-der/m-p/694291
- [40] Graphisoft community wish, bSDD translation for IFC content (403 on fetch): https://community.graphisoft.com/t5/Wishlist/Use-bsDD-translation-for-IFC-content/idi-p/676779
- [41] Graphisoft Archicad 29 English "Import IFC Model" (External IFC ID behavior), seen in search results: https://help.graphisoft.com/AC/29/INT/_AC29_Help/121_IFC/121_IFC-5.htm
- [42] Graphisoft help site language coverage (Italian/Polish/Czech/Russian/Japanese/German/French/Spanish/Hungarian pages seen in search results, none in TR, NL, FI, UK, SV, NO): same pages as [37]
- [43] IFC 4.3.2.0 official snapshot (seen in search results): https://standards.buildingsmart.org/IFC/RELEASE/IFC4_3/HTML/lexical/IfcWall.htm

