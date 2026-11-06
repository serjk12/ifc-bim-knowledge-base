# Официальные разъяснения и FAQ: Минстрой, ФАУ ФЦС, Главгосэкспертиза, вебинары по ЦИМ/IFC

Cell: ru-gov-faq · Languages: ru · Collected: 2026-11-06 · Records: 37 real / 17 synthetic · Communities covered: официальные FAQ и письма (Минстрой, СПб ГАУ «ЦГЭ»), московская система согласования АГР (ЦИМ АГР в IFC), статьи АРД-эксперт, Telegram-каналы «Всё про IFC» и BIMCAP, Habr, NormaCS, консалтинговые сайты по АГР

## Top themes (ranked by frequency)
- ЦИМ АГР в IFC (Москва, с 02.04.2026): что подавать вместе с FBX, наборы RUS_*, RUS_SET_AGR, IfcSite/IfcSpace, пробелы в именах параметров
- Причины возврата и отказов: пустые/неверные атрибуты (54% отказов по пилоту), неполный комплект, отсутствие модели
- Версия IFC и MVD для экспертизы: IFC4 Reference View против IFC2x3 Coordination View 2.0; Москва против СПб
- Маппинг классов IFC при экспорте и подмена класса (IfcEntityType/IfcObjectType), IfcBuildingElementProxy
- Названия и наборы атрибутов у разных экспертиз не совпадают; свой шаблон проекта
- Классификация: КСИ, МССК, Приложение Г СП 333, расхождения между ними
- Коллизии (допуск 15 мм в Москве, СП 333 п. 6.4.4) и отчёты из Solibri/Navisworks
- Правовой статус: ПП 614, приказ 783/пр, XML-схемы против IFC, письма Минстроя «не нормативные акты»
- Что такое ЦИМ/ИМ/ТИМ/СОД: терминологическая путаница в ГОСТ, СП, ПП
- IDS и автоматическая проверка (СПб ЦГЭ выпустил машиночитаемые требования в IDS 1.0; Мособлэкспертиза тоже)
- Сопоставление ЦИМ и чертежей/ПД, целостность данных
- Интероперабельность отечественного ПО (Renga, nanoCAD, КРЕДО), выгрузка из Revit
- Региональность: требования Москвы не действуют в МО и СПб
- Сроки, стоимость и штрафы за расхождение с согласованным АГР (в основном из маркетинговых материалов)

## What people want
- Понять, какой именно набор файлов и атрибутов не вернут на доработку, до подачи (pre-check, IDS, чек-листы)
- Узнать, какая версия требований/даты действует, и применимы ли они к их региону и стадии
- Получить рабочую настройку экспорта (Revit, Renga, ArchiCAD, nanoCAD) с корректными классами и параметрами
- Единые, машиночитаемые и публичные правила проверки вместо закрытых правил экспертов
- Автоматически находить в модели пустые параметры, неверные классы, коллизии, расхождения КСИ/СП 333
- Меньше ручного переделывания: переиспользовать один шаблон проекта и один маппинг
- Юридическую ясность: что именно считать ЦИМ и достаточно ли IFC

## How people write here
- Официальные FAQ: нейтральный канцелярский вопрос, длинное название, например «Названия атрибутов в проекте не совпадают... Что делать?». Практики (консалтинг, Telegram) пишут короче и разговорнее.
- Аббревиатуры без расшифровки: ЦИМ, АГР, НПМ/ВПМ, ТЭП, КСИ, МССК, СОД, ЕГРЗ, МГЭ, МКЭ.
- Слэнг и транскрипции: «ифс» (IFC), «прокси», «маппинг/маппировать», «выгрузка», «завернули/вернули на доработку», «замечания эксперта».
- Смешение латиницы и русского: «параметры RUS_Zone», «IfcSpace», «Reference View», «Export Revit property sets».
- Фрагменты: «Можно ли подать АГР со старым комплектом FBX»; «Нужна ли модель в IFC, если проект в чертежах»; «Что делать?»; «Будет ли достаточно качественного IFC?».
- Опускают контекст: версию Revit/IFC, MVD, размер файла почти никогда не указывают; называют только регион или экспертизу.
- Тон: деловой, часто тревожный перед дедлайном («иначе вернут»), скептицизм у экспертов («путь в никуда», «костыли»).
- Закрытие: нет приветствий и благодарностей, заканчивается вопросом.

## Local ecosystem
- Минстрой России: ПП 614 (17.05.2024), приказ 783/пр о XML-схемах, письма (24935-ОГ/14, 7552-ОГ/14), https://minstroyrf.gov.ru
- ФАУ «ФЦС»: Классификатор строительной информации (КСИ), синхронизирован с IFC 4.0.2.1, http://ksi.faufcc.ru/
- Главгосэкспертиза: ГИС ЕГРЗ, учебный центр https://edu.gge.ru/, вебинары по изменениям законодательства
- Региональные экспертизы: СПб ГАУ «ЦГЭ» (https://www.spbexp.ru/bim/faq/, требования в IDS 1.0), Мосгосэкспертиза (МССК, ExpCheck), Мособлэкспертиза, Управление госэкспертизы Свердловской области (Tangl Control)
- Москва: Департамент градостроительной политики и Москомархитектура, АГР, портал «СтроимПросто», плагин «Якорь IFC»
- Нормы/стандарты: ГОСТ Р 10.0.02-2019 (= ISO 16739-1:2018), СП 333.1325800.2020, ГОСТ Р 10.00.00.00-2023
- ПО: Renga, nanoCAD BIM, КРЕДО, Pilot-BIM, Tangl, 1С:Смета ТИМ, Revit, ArchiCAD, Solibri, Navisworks
- Энтузиасты/просветители: Telegram «Всё про IFC» (https://t.me/s/ifc_ru), BIMCAP (https://t.me/s/bimcap); Habr (ifc_checker, ifctester)
- Open-source: ifcopenshell, ifctester, Bonsai/Blender

## Notable sources
- https://www.spbexp.ru/bim/faq/ — официальный FAQ СПб ЦГЭ по ЦИМ
- https://www.spbexp.ru/docs/tipovye-oshibki/tsifrovye-informatsionnye-modeli-obekta-kapitalnogo-stroitelstva/ — типовые ошибки ЦИМ
- https://www.spbexp.ru/bim/faq/kakuyu-mvd-luchshe-ispolzovat/ — какой MVD
- https://www.spbexp.ru/bim/faq/nashi-nazvaniya-parametrov-v-proekte-ne-sovpadayut-s-trebovaniyami-chto-delat/ — несовпадение имён параметров
- https://smway.ru/ifc-model-dlya-agr-trebovaniya/ — требования IFC для АГР и FAQ (коммерческий источник)
- https://smway.ru/metodicheskie-rekomendacii-agr-3d-modeli/ — НПМ/ВПМ, лимиты, FAQ
- https://smway.ru/bim-model-i-format-ifc-dlya-agr-v-2026-godu-chto-izmenilos-i-kak-podgotovitsya/ — даты и вопросы практиков
- https://companies.rbc.ru/news/axjEyNHHOq/iz-za-chego-mogut-otkazat-v-soglasovanii-tsim-agr-v-formate-ifc/ — причины отказов (только сниппет)
- https://360.ru/tekst/moskva/ovchinskij-novye-tsifrovye-trebovanija-pri-soglasovanii-agr-primenili-bolee-chem-v-100-proektah/ — статистика отказов
- https://riamo.ru/news/nedvizhimost/ovchinskij-v-stolitse-provodjat-konsultatsii-po-podache-materialov-v-ifc-formate/ — еженедельные консультации
- https://aif.ru/moscow/ovchinskiy-servis-proverki-cim-zarabotaet-s-cifrovymi-modelyami-bystree — сервис проверки ЦИМ
- https://ardexpert.ru/article/19356 — подготовка BIM-модели к экспертизе
- https://ardexpert.ru/article/19592 — Москва против СПб
- https://ardexpert.ru/article/25029 — охват ТИМ, единые требования
- https://ardexpert.ru/article/25755 — трактовка ТИМ и СОД
- https://ardexpert.ru/article/25845 — КСИ и СП 333 в экспертизе
- https://ardexpert.ru/article/27185 — конференция лучших практик ТИМ
- https://www.comnews.ru/content/235588/2024-11-07/2024-w45/1013/chto-predstavlyaet-soboy-cim-posle-postanovleniya-614 — ЦИМ после ПП 614
- https://www.kontur-extern.ru/info/normativ/document/8/479825-pismo-minstroya-rf-ot-20-09-2024-n-24935-og-14 — письмо про XML
- https://pravo.ppt.ru/pismo/minstroy/n-7552-og-14-317524 — письмо про ТИМ и разрешение на строительство
- https://t.me/s/ifc_ru — «Всё про IFC»
- https://t.me/s/bimcap — BIMCAP
- https://habr.com/p/883016 — проверка IFC через IDS
- https://www.normacs.info/news/74243 — пилот экспертизы ЦИМ в Свердловской области
- http://ksi.faufcc.ru/ — КСИ
- https://iek-digital.ru/upload/iblock/685/4jzi0mt4ob86xb78imiswfg6dngrrots/Instruktsiya-po-eksportu-IFC-dlya-REVIT.pdf — экспорт IFC из Revit (только сниппет)

## Gaps
- Прямых FAQ Минстроя/ФАУ ФЦС/Главгосэкспертизы именно по IFC не найдено: поиск по minstroyrf.gov.ru, faufcc.ru, gge.ru вернул в основном новости о КСИ и общие вебинары. Записей вебинаров с вопросами слушателей по IFC нет.
- WebFetch недоступен или заблокирован: spbexp.ru (connection refused, использованы сниппеты поиска), gge.ru (403), companies.rbc.ru (401), minstroyrf.gov.ru (connection refused в одном случае), docs.google.com не открывали.
- Мосгосэкспертиза, Мособлэкспертиза: собственных страниц с требованиями не найдено, только косвенные упоминания.
- Живых форумных веток (dwg.ru, Renga, Autodesk) в этой ячейке не собирали; реальные вопросы взяты из официальных FAQ, консалтинговых FAQ и Telegram-постов, поэтому реплики более формальные, чем на форумах.
- Часть источников (smway.ru, hh.ru) коммерческая: цены, сроки и штрафы нужно проверять; даты (19.01 против 02.04.2026) в источниках расходятся.
- Подозрительных сайтов со взломанным ПО не встречалось; ничего не скачивалось.
