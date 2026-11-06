# Русскоязычные сообщества Autodesk, блоги и Telegram-каналы: вопросы про IFC

Cell: ru-autodesk-telegram · Languages: Russian · Collected: 2026-11-06 · Records: 38 real / 18 synthetic · Communities covered: forum.dwg.ru, Habr (блоги практиков и компаний), Telegram (Всё про IFC, RevitHelper, BIMLIB, Просто о BIM, Академия BIM, BIM Solutions), блог и справка Renga, sapr.ru, YouTube-уроки, нормативные тексты (Минстрой, СП 333).

## Top themes (ranked by frequency)
- Выгрузка IFC для Москвы (АГР/МГЭ, с 2026): проверка по IDS, "строимпросто", долгий экспорт, итерации "выгрузил - нашёл ошибку - снова".
- Маппинг классов: IfcExportAs, ФОП, UDPS, проксики (IfcBuildingElementProxy), косоуры/пандусы уходят не в тот класс.
- Помещения и зоны (IfcSpace), ТЭП: расхождение площадей, зоны без геометрии, дубли.
- Потеря данных и "мёртвая геометрия" при импорте IFC в Revit; потерянные свойства и параметры.
- IDS и машиночитаемые требования экспертиз (ЦГЭ СПб, Мособлэкспертиза, Мосгосэкспертиза), классификаторы КСИ/МССК.
- Какая версия IFC и MVD (2x3 CV2.0 или IFC4 RV) нужна заказчику/экспертизе.
- Координаты: базовая точка, точка съёмки, внутреннее начало, абсолютные координаты.
- Совместимость с отечественным ПО: Renga, Сапфир, nanoCAD СПДС, Pilot-BIM, Vitro-CAD, Credo.
- Просмотрщики и проверка файла (xBIM, BIMvision, онлайн-вьюеры) как первый шаг диагностики.
- Постобработка IFC без Revit: Blender/Bonsai, ifcopenshell, web-ifc, правка по GlobalId.
- Региональные ТИМ-стандарты и инструкции по экспорту (Свердловская область, ГИП-уровень).

## What people want (the goals behind the questions)
- Пройти экспертизу/АГР с первого раза и не гонять двухчасовой экспорт.
- Проверять модель до выгрузки (плагины на Revit API, IDS).
- Чтобы элементы приходили в нужном IFC-классе с нужными свойствами.
- Передать модель смежникам и расчётчикам без потерь; открыть чужой IFC в Revit и продолжить работу.
- Понять формальную сторону: версия схемы, вид модели, классификаторы, требования региона.
- Бесплатно открыть и посмотреть свойства IFC без лицензии на Revit.

## How people write here
- Форумы (dwg.ru): короткие, без приветствий, часто без версии ПО и без файла; пишут "ифс", "ревит", "текла", "сапфир". Заголовок = симптом ("Не происходит экспорт модели").
- Habr и Telegram: профессиональный жаргон, смесь русского и английского: ЦИМ, АГР, ТЭП, ФОП, "маппинг", "постобработка", "дубли", IfcExportAs, IDS, GlobalId.
- Ошибки Revit цитируют по-английски в русской фразе: "System Error encountered during import".
- Эмоции: усталость от итераций ("ради пустого параметра"), скепсис к требованиям ("работа в стол"), лёгкая ирония.
- Контекст часто опущен: версия IFC, настройки экспорта, ПО-источник.
- Короткие фрагменты: "ошибки видно только после загрузки"; "зоны пропадают"; "теряются свойства"; "мёртвая геометрия".

## Local ecosystem
- Нормативка: СП 333.1325800.2017 (IFC 2x3 и выше), правила формирования ИМ ОКС (Минстрой, допускаются IFC/LandXML), ПНСТ 909-2024. http://docs.cntd.ru/document/556793897 ; https://minstroyrf.gov.ru/press/utverzhdeny-pravila-formirovaniya-i-vedeniya-informatsionnoy-modeli-obekta-kapitalnogo-stroitelstva/
- Экспертизы: Мосгосэкспертиза (требования ТИМ, АГР, IDS, "Строим просто"), СПб ГАУ ЦГЭ (IDS-файлы), Мособлэкспертиза, ФАУ ФЦС (пилот экспертизы в формате модели).
- Классификаторы: КСИ, МССК (Москва).
- Отечественное ПО: Renga (https://rengabim.com), Pilot-BIM/PilotICE, nanoCAD BIM/СПДС, Сапфир, Vitro-CAD, Credo, BIM42, BIMvision (польский бесплатный вьюер).
- Сообщества: forum.dwg.ru, Telegram "Всё про IFC" (t.me/ifc_ru), RevitHelper, BIMLIB, Просто о BIM, Академия BIM, Habr (kirbim, ПИК).
- Открытые проекты: ifcopenshell/ifctester, Bonsai (Blender), web-ifc, xBIM.

## Notable sources
- https://forum.dwg.ru/showthread.php?t=153428 - Экспертиза проекта в Revit (2019)
- https://forum.dwg.ru/showthread.php?t=154396 - Как корректно открыть IFC
- https://forum.dwg.ru/showthread.php?t=160240 - Сапфир и IFC, System Error
- https://forum.dwg.ru/showthread.php?t=166052 - Импорт IFC в Revit 2022
- https://forum.dwg.ru/showthread.php?t=146029 - Tekla в Revit, тема 2018-2024
- https://forum.dwg.ru/showthread.php?t=133669 - Revit-STARK ES
- https://forum.dwg.ru/showthread.php?t=173570 - Plant 3D 2025 в IFC
- https://habr.com/ru/articles/1089018/ - Два часа выгрузки ради пустого параметра
- https://habr.com/ru/articles/1098340/ - AGR.Checker
- https://habr.com/ru/articles/1100956/ - Постобработка IFC без Revit, ч.2
- https://habr.com/ru/articles/1094224/ - IDS Core в браузере
- https://habr.com/ru/articles/883016/ - Проверка IFC по IDS
- https://habr.com/ru/articles/908192/ - Спецификация IDS
- https://habr.com/ru/companies/pik_digital/articles/1057314/ - BIM Inspector (ПИК)
- https://habr.com/ru/articles/1075736/ - плагин под Revit и АГР
- https://blog.rengabim.com/2021/08/ifc.html - Как принять IFC (Renga)
- https://rengabim.com/stati/bol-she-10-formatov-eksporta-importa-v-renga-kakoj-iz-nih-vybrat/
- https://sapr.ru/article/25825 - nanoCAD СПДС и IFC из Revit
- https://t.me/s/ifc_ru - Всё про IFC
- https://t.me/s/revithelper_kmv/146 - инструкция Свердловской области
- https://t.me/s/bimlib_pro - BIMLIB
- https://t.me/s/prostobim?before=267 - Просто о BIM
- https://t.me/s/bimacad?before=557 - Академия BIM
- https://iek-digital.ru/upload/iblock/685/4jzi0mt4ob86xb78imiswfg6dngrrots/Instruktsiya-po-eksportu-IFC-dlya-REVIT.pdf
- https://www.youtube.com/watch?v=VPlQf3fv908 - Лекция: экспорт в IFC и IFC Viewers
- https://minstroyrf.gov.ru/press/pervyy-proekt-polnostyu-sproektirovannyy-na-osnove-bim-tekhnologiy-proshel-gosekspertizu/

## Gaps
- Русскоязычных разделов forums.autodesk.com по IFC поиск практически не показал (выдача в основном англоязычная); Autodesk-ветки не включены в записи.
- Страницы dwg.ru отдаются с битой кодировкой, формулировки реконструированы по пересказу, а не цитатам; в части тем ответы не видны.
- Многие Telegram-страницы показывают только время без даты; годы в этих записях и в нескольких snippet-записях оценочные.
- vk.com недоступен для поиска; VK-группы и чаты Telegram (закрытые) не охвачены. tgstat.ru вернул 403.
- Ничего подозрительного (кряки, пиратские ссылки) не использовано; сайты с торрентами Archicad из выдачи пропущены.
