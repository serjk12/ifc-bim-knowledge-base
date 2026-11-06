# Российский софт и импортозамещение: Renga, nanoCAD BIM, Model Studio CS, Pilot-BIM, ЛИРА-САПР, SCAD, Credo, ГРАНД-Смета

Cell: g-ru-domestic-software · Languages: ru · Collected: 2026-11-06 · Records: 34 real / 16 synthetic · Communities covered: forum.dwg.ru (cp1251 decoded correctly via curl), forum.nanocad.ru (snippets), блог и руководство Renga, sapr.ru, cadmaster.ru, isicad.ru, habr.com, сайты Credo, CSoft, SCAD, Lira, АСКОН

## Top themes (ranked by frequency)
- Что теряется при обмене Revit/Archicad/Tekla -> расчётная программа (ЛИРА, SCAD, STARK): сечения, материалы, перекрытия, колонны, нагрузки.
- Настройка маппинга Renga: файлы сопоставления типов и параметров (JSON), почему свойства или инженерные объекты не попали в IFC.
- Выбор геометрического представления при экспорте (Reference View, Design Transfer View, SweptSolid/Brep/Tessellation) под целевую САПР или Navisworks.
- Подготовка IFC4 и IDS-проверка для Мосгосэкспертизы, СПб-экспертизы и ЦИМ АГР (сроки выгрузки, пустые параметры, RUS_*).
- Импортированный IFC как "мёртвые блоки" или нередактируемая подложка (nanoCAD, Revit, Renga).
- Версия схемы: IFC2x3 против IFC4, Renga отказался от IFC2x3, смежное ПО (DIALux, nanoCAD СКС) не читает IFC4.
- Инфраструктура: IFC из Credo в Revit без объёмов, IFC 4.3 для дорог, маппинг классов (по умолчанию proxy).
- Импортозамещение: Pilot-BIM вместо Navisworks/BIM 360, CAD-Farm, переход на нативные форматы Renga, мнение CSoft о национальном формате.
- Смещение координат и начало координат при передаче расчётных моделей.
- Законность и стандарты: ГОСТ Р 10.0.02-2019 (ISO 16739), выход buildingSMART из России.
- Передача спецификаций и объёмов в ГРАНД-Смету (прямого пути из IFC найдено не было, только таблицы/ГГЭ).

## What people want
- Чтобы модель из зарубежного ПО открывалась в Renga/nanoCAD/Credo и расчётных программах с редактируемой геометрией и параметрами.
- Предсказуемый маппинг классов и свойств под требования экспертизы без многочасовых повторных выгрузок.
- Проверка модели до выгрузки (IDS, обязательные атрибуты), чтобы не ждать ответ сервиса.
- Объёмы и материалы (грунт, дорожная одежда, перекрытия) из IFC для смет.
- Понять, что именно потеряется при IFC-обмене, и какой формат (IFC, нативный, плагин) надёжнее.
- Передача аналитической модели в ЛИРА/SCAD с сечениями, материалами и нагрузками.

## How people write here
- Регистр: форумный, вежливое "Добрый день!"/"Коллеги!", без лишнего контекста, часто сразу цель ("надо посчитать объём насыпи"). Объём: 2-6 предложений, иногда нумерованный список.
- Сленг: "ифс"/"ифц" (IFC), "ревит", "тёкла", "кредо", "улетает в прокси", "шляпа" (мусорный результат), "мёртвые блоки", "одни оси", "Шаманский бубен" (ирония).
- Опечатки и варианты: "icf", "ifc2x2", "IFC 2.3" вместо 2x3, "Лира САПР", "Архикад".
- Смешение языков: сообщения об ошибках цитируются по-английски ("System Error encountered during import"), названия параметров латиницей (IfcExportAs, RUS_Height).
- Версии указываются в подписи или заголовке: "Revit 2012", "SCAD 21", "Lira 9.6".
- Эмоции: раздражение при потере данных ("очень плохо, придется полностью переделывать"), растерянность у новичков ("Что такое IFC?").
- Короткие фрагменты: "в Ревите у них одни оси"; "встает нередактируемым блоком"; "Что такое IFC?"; "перекрытия съезжают".

## Local ecosystem
- Разработчики: Renga (АСКОН) https://rengabim.com , Pilot-BIM https://ascon.ru ; nanoCAD BIM (Нанософт) https://www.nanocad.ru ; Model Studio CS, CADLib (CSoft) https://modelstudiocs.ru ; ТИМ КРЕДО https://credo-dialogue.ru ; ЛИРА-САПР https://www.liraland.ru , https://lira-soft.com ; SCAD https://scadsoft.com ; ГРАНД-Смета https://www.grandsmeta.ru .
- Renga IFC mapping файлы на GitHub: https://github.com/RengaSoftware/IFCMappingFiles (export_type.json, export_layer.json, export_attr_qto_pset.json).
- Стандарты и регуляторика: ГОСТ Р 10.0.02-2019 (идентичен ISO 16739-1:2018), Минстрой (проблемы импортозамещения ТИМ, 2022), Мосгосэкспертиза и ДГП Москвы (IDS для ЦИМ АГР с 2026), СПб ГАУ "Центр государственной экспертизы".
- Сообщества: forum.dwg.ru, forum.nanocad.ru, sapr.ru, cadmaster.ru, isicad.ru, habr.com.
- Открытые проекты и инструменты: ifcopenshell и ifctester, Национальная ТИМ Платформа (ИСП РАН), xbim, ACCA usBIM.IDS, RusBIMExpert.

## Notable sources
- https://forum.dwg.ru/showthread.php?t=166052 - IFC из Credo в Revit без объёмов (2022)
- https://forum.dwg.ru/showthread.php?t=160240 - САПФИР IFC: System Error при импорте
- https://forum.dwg.ru/showthread.php?t=33352 - ArchiCAD IFC в Lira/SCAD, 2009-2016
- https://forum.dwg.ru/showthread.php?t=142967 - Revit <-> SCAD, стальной каркас
- https://forum.dwg.ru/showthread.php?t=62339 - Revit Structure в SCAD через r2s
- https://forum.dwg.ru/showthread.php?t=133669 - Revit в STARK ES
- https://forum.dwg.ru/showthread.php?t=68789 - Revit Architecture в Lira, съезжающие перекрытия
- https://forum.dwg.ru/showthread.php?t=146029 - Tekla в Revit, одни оси
- https://blog.rengabim.com/2021/08/ifc.html - как принять IFC в Renga
- https://blog.rengabim.com/2020/09/ifc-ifc-ifc.html - Reference View и Design Transfer View
- https://blog.rengabim.com/2021/09/ifc.html - редактируемая геометрия при экспорте (настройки)
- https://manual.rengabim.com/opredelenie_geometricheskikh_predstavlenij_obektov_dlya_ehksporta.html - геометрические представления
- https://manual.rengabim.com/sopostavlenie_kategorij_obektov_inzhenernykh_sistem.html - инженерные объекты в mapping
- https://manual.rengabim.com/zhurnal_oshibok_ehksporta.html - журнал ошибок экспорта
- https://sapr.ru/article/26143 - госэкспертиза и IFC из Renga
- https://habr.com/ru/articles/1089018/ - IDS Core, ЦИМ для АГР в Revit
- https://habr.com/ru/companies/pik_digital/articles/1057314/ - BIM Inspector, МГЭ/АГР
- https://habr.com/ru/companies/nanosoft/articles/1038142/ - nanoCAD, маппинг для АГР
- https://habr.com/ru/articles/883016/ - проверка IFC по IDS
- https://www.cadmaster.ru/magazin/articles/cm_90_17.html - Revit IFC в nanoCAD СПДС
- https://credo-dialogue.ru/tekhnologii/kommunikacii.html - Credo, IFC 4.3
- https://modelstudiocs.ru/press/20250908-data-transmission-format.html - мнение CSoft о формате
- https://scadsoft.com/help/SCAD/ru/SCAD1049/import_loading_diagram.htm - импорт в SCAD
- https://help.liraland.ru/829/3441/ - интеграция Lira с Revit
- https://github.com/RengaSoftware/IFCMappingFiles - JSON mapping Renga
- https://cn.gostinfo.ru/catalog/Details/?id=6453898 - ГОСТ Р 10.0.02-2019

## Gaps
- WebFetch отдаёт кракозябры для forum.dwg.ru (cp1251); читать удалось через curl с декодированием cp1251 (в сессии, без сохранения файлов). Несколько страниц читались только по первым постам, часть ответов не получена.
- forum.nanocad.ru, forum.renga.ru, forum.csoft.ru: прямая загрузка дала 404 или не индексировалась; nanoCAD-записи имеют evidence "snippet".
- Почти нет реальных вопросов пользователей по Model Studio CS, Pilot-BIM, ГРАНД-Смете и Топоматик (вендорские материалы доминируют); прямой импорт IFC в ГРАНД-Смету не обнаружен.
- Не охвачены: Telegram, VK, Rutube. Рекомендованные вендором IFC-настройки Model Studio CS и nanoCAD в источниках не раскрыты, для Renga и Credo описаны.
- Подозрительные и пиратские сайты не посещались и не цитировались.
