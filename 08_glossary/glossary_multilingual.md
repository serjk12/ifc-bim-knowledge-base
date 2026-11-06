# Multilingual IFC/BIM/Revit glossary (EN, RU, ZH, ES, PT, DE, FR, JA, KO, AR)

**Last researched: 2026-11-06**

## In plain words

IFC (Industry Foundation Classes) is the open, vendor-neutral file format and data schema that BIM programs use to swap building models. It is standardised by buildingSMART and by ISO as ISO 16739-1 [1][2]. Revit is Autodesk's BIM authoring program, and it has its own vocabulary (family, type, instance, workset, phase) that only partly matches IFC vocabulary (entity, type object, occurrence, spatial structure). BIM project management has a third vocabulary (EIR, BEP, CDE, LOIN) from ISO 19650 and ISO 7817. This glossary lines up the three vocabularies in ten languages, so a QA tester can read a user's request written in Russian, German or Japanese and still know which IFC entity, Revit object or process document is meant. It also helps judge whether an MCP tool answered in the right terms.

How to read the table: **[V:n]** means the localized words were checked in the page(s) with source number n, which are vendor help or Wikipedia interlanguage links fetched during this research. **No tag** means the translation is established professional usage from background knowledge and was NOT individually verified in this session. Treat untagged cells as "(unverified)" before you hard-code them in test expectations. Arabic cells are the weakest of the ten: Arabic BIM terminology is not uniform across countries, and Revit has no Arabic UI that I could confirm (unverified). IFC entity names (IfcWall, IfcBuildingStorey) are never translated; they stay in Latin script in every language.

## Scope, versions and ground facts

| Fact | Value | Source |
|---|---|---|
| Current IFC edition at ISO | ISO 16739-1:2024, "Industry Foundation Classes (IFC) for data sharing in the construction and facility management industries, Part 1: Data schema", 2nd edition, adds infrastructure (roads, rail, bridges, waterways, ports) | [1] |
| Previous ISO edition | ISO 16739-1:2018 (withdrawn, replaced by the 2024 edition) | [2] |
| Latest official buildingSMART release | IFC 4.3.2.0 (commonly called IFC4.3) | [3] |
| Russian adoption of the 2018 edition | ГОСТ Р 10.0.02-2019/ИСО 16739-1:2018, "Отраслевые базовые классы (IFC) для обмена и управления данными об объектах строительства. Часть 1. Схема данных", effective 2019-09-01 | [33] |
| IDS | IDS 1.0 approved as a Final Standard by buildingSMART (approval dated 1 June 2024 per buildingSMART) | [5] |
| BCF | BCF 3.0 final release of the BCF-API; BCF 3.0 builds on BCF 2.1 | [6] |
| GlobalId format | `IfcGloballyUniqueId` = STRING(22) FIXED, a compressed 128-bit GUID using a custom base-64 alphabet `0-9A-Za-z_$`; first character is 0-3. Example: UUID f70dd363-bfe3-495d-84a0-2c02dcb7d4d2 compresses to `3t3TDZl_D9NOIWB0BSjzJI` | [4] |
| Level of information need | ISO 7817-1:2024 "Building information modelling, Level of information need, Part 1: Concepts and principles"; Part 2 (guidance) and Part 3 (data model/XSD) were still drafts (DTS / DIS) when searched | [9][54] |
| ISO 19650 series | -1 concepts and principles, -2 delivery phase, -3 operational phase, -5 security-minded approach | [37][44] |
| European guidance | CEN/TR 17654:2021 (EIR and BEP guideline, based on EN ISO 19650-1/-2); CEN/TR 18093:2024 (CDE solutions and workflows) | [37] |
| Chinese national standards | GB/T 51212 (BIM application unified standard, 2016, in force 2017-07-01), GB/T 51301 (BIM design delivery, 2018, in force 2019-06-01; defines 模型精细度), GB/T 51447 (BIM storage standard, 2021, in force 2022-02-01) | [34] |
| Revit localizations seen in help | German, French, Spanish, Brazilian Portuguese, Japanese, Korean, Russian, Simplified Chinese help pages exist at `help.autodesk.com/cloudhelp/<year>/<DEU|FRA|ESP|PTB|JPN|KOR|RUS|CHS>/...` | [11]-[29] |

## Master glossary (single table)

Columns: **Grp** = area (IFC = IFC schema and exchange, RVT = Revit, PRC = BIM process and standards, ELM = building elements, MEP = services, GEO = site, geo and infrastructure). Languages: EN, RU, ZH (Simplified Chinese), ES (Spain/LatAm neutral, Spain-specific noted), PT (Brazilian first, European noted), DE, FR, JA, KO, AR.

| Grp | English | Russian | Chinese | Spanish | Portuguese | German | French | Japanese | Korean | Arabic | Short definition |
|---|---|---|---|---|---|---|---|---|---|---|---|
| IFC | IFC (Industry Foundation Classes) | Отраслевые базовые классы (IFC) [V:33] | 工业基础类 / 工业基础分类 (IFC) [V:31] | Industry Foundation Classes (IFC), usually kept in English | Industry Foundation Classes (IFC) | Industry Foundation Classes (IFC) [V:31] | Industry Foundation Classes (IFC) [V:31] | Industry Foundation Classes (IFC) [V:31] | Industry Foundation Classes (IFC) [V:31] | فئات أسس الصناعة (IFC) [V:31] | Open BIM data schema and file format, ISO 16739-1 |
| IFC | buildingSMART | buildingSMART | buildingSMART | buildingSMART | buildingSMART | buildingSMART | buildingSMART | buildingSMART | buildingSMART | buildingSMART | Standards body behind IFC, IDS, BCF, bSDD (brand name, not translated) |
| IFC | openBIM | openBIM (открытый BIM) | 开放BIM (openBIM) | openBIM | openBIM | openBIM | openBIM | オープンBIM | 오픈BIM | BIM المفتوح | Vendor-neutral BIM workflows based on open standards |
| IFC | Schema | схема [V:33] | 模式 / 架构 | esquema | esquema | Schema | schéma | スキーマ | 스키마 | مخطط | Formal definition of all entities and attributes (EXPRESS or XSD) |
| IFC | EXPRESS | EXPRESS | EXPRESS | EXPRESS | EXPRESS | EXPRESS | EXPRESS | EXPRESS | EXPRESS | EXPRESS | Data modelling language (ISO 10303-11) in which the IFC schema is written [57] |
| IFC | STEP physical file (.ifc) | физический файл STEP (.ifc) | STEP 物理文件 (.ifc) | archivo físico STEP (.ifc) | arquivo físico STEP (.ifc) | STEP-Datei (.ifc) | fichier physique STEP (.ifc) | STEP物理ファイル (.ifc) | STEP 물리 파일 (.ifc) | ملف IFC (STEP) | Plain-text IFC serialization; one line per instance (#123=IFCWALL(...)) |
| IFC | ifcXML | ifcXML | ifcXML | ifcXML | ifcXML | ifcXML | ifcXML | ifcXML | ifcXML | ifcXML | XML serialization of IFC (.ifcxml), rarely used in practice |
| IFC | ifcZIP | ifcZIP | ifcZIP | ifcZIP | ifcZIP | ifcZIP | ifcZIP | ifcZIP | ifcZIP | ifcZIP | Compressed IFC file (.ifczip) |
| IFC | IFC version (IFC2x3, IFC4, IFC4.3) | версия IFC | IFC 版本 | versión de IFC | versão do IFC | IFC-Version | version IFC | IFCバージョン | IFC 버전 | إصدار IFC | Schema generation; IFC2x3 TC1 and IFC4 (ADD2 TC1) remain very common in tools |
| IFC | Entity | сущность | 实体 | entidad | entidade | Entität | entité | エンティティ | 엔티티 | كيان | A named class in the schema, e.g. IfcWall |
| IFC | Class | класс | 类 | clase | classe | Klasse | classe | クラス | 클래스 | صنف | Loose synonym for entity; also "IFC class" = entity name |
| IFC | Attribute | атрибут | 属性 | atributo | atributo | Attribut | attribut | 属性 (アトリビュート) | 속성 (어트리뷰트) | سمة | Fixed field defined by the schema, e.g. Name, Description, GlobalId |
| IFC | Property | свойство | 属性 | propiedad | propriedade | Eigenschaft (also Merkmal) | propriété | プロパティ | 속성 / 프로퍼티 | خاصية | Extensible name/value stored in a property set (IfcPropertySingleValue) |
| IFC | Property set (Pset) | набор свойств | 属性集 | conjunto de propiedades | conjunto de propriedades | Eigenschaftsset / Merkmalgruppe | jeu de propriétés | プロパティセット | 속성 세트 (PSET) [V:51] | مجموعة خصائص | Named group of properties; standard ones start with `Pset_` (e.g. Pset_WallCommon) [7] |
| IFC | Custom property set | пользовательский набор свойств | 自定义属性集 | conjunto de propiedades personalizado | conjunto de propriedades personalizado | benutzerdefiniertes Eigenschaftsset | jeu de propriétés personnalisé | カスタムプロパティセット | 사용자 정의 속성 세트 | مجموعة خصائص مخصصة | Project/company-specific set; must NOT start with `Pset_` (convention) |
| IFC | Quantity set (Qto) | набор количественных показателей | 工程量集 / 数量集 | conjunto de cantidades | conjunto de quantidades | Mengenset | jeu de quantités | 数量セット | 수량 세트 | مجموعة كميات | Measured quantities (Length, Area, Volume); standard ones start `Qto_` [8] |
| IFC | Base quantities | базовые количества | 基础工程量 | cantidades base | quantidades base | Basismengen | quantités de base | 基本数量 | 기본 수량 | الكميات الأساسية | Standard `Qto_*BaseQuantities` sets, e.g. Qto_WallBaseQuantities |
| IFC | Quantity | количество | 工程量 | cantidad | quantidade | Menge | quantité | 数量 | 수량 | كمية | One value in a quantity set (IfcQuantityArea etc.) |
| IFC | Type object / element type | объект типа (тип) | 类型对象 | tipo de elemento | tipo de elemento | Typobjekt | type d'élément | タイプオブジェクト | 유형 객체 | كائن النوع | IfcTypeObject, e.g. IfcWallType, shared by many occurrences |
| IFC | Occurrence | вхождение (экземпляр) | 实例 | ocurrencia | ocorrência | Vorkommen / Instanz | occurrence | オカレンス | 인스턴스 / 발생 | نسخة | The placed element in the model, e.g. one IfcWall |
| IFC | Instance (of an entity) | экземпляр | 实例 | instancia | instância | Instanz | instance | インスタンス | 인스턴스 | نسخة / مثيل | One record in the file (#id) |
| IFC | Predefined type | предопределённый тип | 预定义类型 | tipo predefinido | tipo predefinido | vordefinierter Typ | type prédéfini | 定義済みタイプ | 사전 정의 유형 | نوع معرّف مسبقًا | Enum such as STANDARD, USERDEFINED, NOTDEFINED |
| IFC | GUID / GlobalId | глобальный уникальный идентификатор (GUID) | 全局唯一标识符 (GUID) | identificador único global (GUID) | identificador único global (GUID) | global eindeutige Kennung (GUID) | identifiant unique global (GUID) | グローバル一意識別子 (GUID) | 전역 고유 식별자 (GUID) | المعرّف الفريد العالمي | 22-character IfcRoot.GlobalId that should survive re-exports [4] |
| IFC | Name | имя | 名称 | nombre | nome | Name | nom | 名前 | 이름 | الاسم | IfcRoot.Name |
| IFC | Description | описание | 描述 | descripción | descrição | Beschreibung | description | 説明 | 설명 | الوصف | IfcRoot.Description |
| IFC | Tag | метка | 标签 | etiqueta | etiqueta | Kennzeichen / Tag | repère / tag | タグ | 태그 | وسم | IfcElement.Tag, often the source-application ID (Revit ElementId) |
| IFC | ObjectType | тип объекта (ObjectType) | 对象类型 (ObjectType) | ObjectType | ObjectType | ObjectType | ObjectType | ObjectType | ObjectType | ObjectType | Free-text subtype used with USERDEFINED |
| IFC | Product | продукт | 产品 | producto | produto | Produkt | produit | プロダクト | 프로덕트 | منتج | IfcProduct: anything with placement and shape |
| IFC | Element | элемент | 构件 / 元素 | elemento | elemento | Bauteil / Element | élément | 要素 | 요소 | عنصر | IfcElement: physical thing in a building |
| IFC | Building element | строительный элемент | 建筑构件 | elemento de construcción | elemento de construção | Bauelement | élément de construction | 建築要素 | 건축 요소 | عنصر إنشائي | IfcBuildingElement (renamed IfcBuiltElement in IFC4.3) |
| IFC | Proxy | прокси-элемент | 代理构件 | proxy | proxy | Proxy-Element | élément proxy | プロキシ | 프록시 | عنصر وكيل | IfcBuildingElementProxy: generic fallback when no class fits |
| IFC | Relationship | связь (отношение) | 关系 | relación | relacionamento | Beziehung | relation | リレーションシップ | 관계 | علاقة | IfcRelationship objectified relations (IfcRelAggregates etc.) |
| IFC | Aggregation | агрегация | 聚合 | agregación | agregação | Aggregation | agrégation | 集約 | 집합 | تجميع | IfcRelAggregates: whole/part, also project→site→building→storey |
| IFC | Spatial containment | пространственное вхождение | 空间包含 | contención espacial | contenção espacial | räumliche Zuordnung | confinement spatial | 空間包含 | 공간 포함 | احتواء مكاني | IfcRelContainedInSpatialStructure: element belongs to storey/space [40] |
| IFC | Type assignment | назначение типа | 类型关联 | asignación de tipo | atribuição de tipo | Typzuweisung | affectation de type | タイプの割り当て | 유형 할당 | إسناد النوع | IfcRelDefinesByType |
| IFC | Material association | связь с материалом | 材料关联 | asociación de material | associação de material | Materialzuweisung | association de matériau | 材料の関連付け | 재료 연관 | ربط المادة | IfcRelAssociatesMaterial |
| IFC | Opening element | проём (элемент) | 洞口构件 | elemento de hueco | elemento de abertura | Öffnungselement | élément d'ouverture | 開口要素 | 개구부 요소 | عنصر فتحة | IfcOpeningElement: void cut in a wall/slab, filled by door/window |
| IFC | Project (IfcProject) | проект | 项目 | proyecto | projeto | Projekt | projet | プロジェクト | 프로젝트 | مشروع | Root of the spatial hierarchy; units and contexts live here |
| IFC | Site (IfcSite) | участок | 场地 | emplazamiento / parcela | terreno / lote | Grundstück | site / terrain | 敷地 | 대지 | موقع | Land area containing buildings |
| IFC | Building (IfcBuilding) | здание | 建筑物 | edificio | edifício | Gebäude | bâtiment | 建物 | 건물 | مبنى | One building under a site |
| IFC | Building storey (IfcBuildingStorey) | этаж | 楼层 | planta | pavimento / andar | Geschoss | étage / niveau | 階 | 층 | طابق | Horizontal slice of a building with Elevation attribute [31] |
| IFC | Space (IfcSpace) | пространство (помещение) | 空间 | espacio | espaço / ambiente | Raum | espace / pièce | 空間 / 室 | 공간 / 실 | حيّز / غرفة | Bounded area or volume (rooms, shafts); Revit Room usually becomes IfcSpace |
| IFC | Zone (IfcZone) | зона | 分区 | zona | zona | Zone | zone | ゾーン | 존 | منطقة | Grouping of spaces (fire, HVAC, tenancy); not a spatial-structure level |
| IFC | Spatial structure | пространственная структура | 空间结构 | estructura espacial | estrutura espacial | räumliche Struktur | structure spatiale | 空間構造 | 공간 구조 | البنية المكانية | Project > Site > Building > Storey > Space hierarchy |
| IFC | Facility (IFC4.3) | сооружение (объект) | 设施 | instalación (facility) | instalação (facility) | Bauwerk / Anlage | ouvrage / installation | 施設 | 시설 | منشأة | IfcFacility: generic parent of IfcBuilding, IfcBridge, IfcRoad etc. in IFC4.3 |
| IFC | Facility part | часть сооружения | 设施部分 | parte de instalación | parte da instalação | Bauwerksteil | partie d'ouvrage | 施設の部分 | 시설 부분 | جزء المنشأة | IfcFacilityPart, e.g. bridge pier |
| IFC | Group | группа | 组 | grupo | grupo | Gruppe | groupe | グループ | 그룹 | مجموعة | IfcGroup: logical collection |
| IFC | System | система | 系统 | sistema | sistema | System | système | システム | 시스템 | نظام | IfcSystem / IfcDistributionSystem, e.g. supply-air system |
| IFC | Assembly | сборка | 组件 / 装配体 | ensamblaje | montagem | Baugruppe | assemblage | アセンブリ | 어셈블리 | تجميعة | Element composed of parts (IfcElementAssembly) |
| IFC | Port | порт | 端口 | puerto | porto | Anschluss / Port | port | ポート | 포트 | منفذ | IfcDistributionPort: connection point of MEP elements |
| IFC | Grid (IfcGrid) | сетка осей | 轴网 | rejilla / retícula | grade / malha de eixos | Raster | quadrillage / trame | 通り芯 / グリッド | 그리드 / 축선 | شبكة المحاور | Structural grid axes |
| IFC | Representation | представление (геометрия) | 表达 | representación | representação | Repräsentation | représentation | 表現 | 표현 | تمثيل | Geometry of a product (IfcProductDefinitionShape) |
| IFC | Extruded area solid | тело выдавливания | 拉伸实体 | sólido de extrusión | sólido extrudado | Extrusionskörper | solide d'extrusion | 押し出しソリッド | 압출 솔리드 | جسم مبثوق | IfcExtrudedAreaSolid: profile plus direction and depth |
| IFC | Boundary representation (B-rep) | граничное представление | 边界表示 | representación de contorno (B-rep) | representação de contorno (B-rep) | Begrenzungsflächenmodell (B-Rep) | représentation par frontières | 境界表現 | 경계 표현 | تمثيل الحدود | IfcFacetedBrep etc., faces and edges |
| IFC | Tessellation | тесселяция | 网格化 | teselación | tesselação | Tesselierung | tessellation | テッセレーション | 테셀레이션 | تقسيم شبكي | IfcTriangulatedFaceSet (IFC4): triangle mesh |
| IFC | Mapped item / representation map | отображаемый элемент (повторное использование) | 映射项 | elemento mapeado | item mapeado | Abbildungselement | élément mappé | マップ項目 | 매핑 항목 | عنصر مُعيَّن | Shared geometry reused by many occurrences of a type |
| IFC | Local placement | локальное размещение | 局部定位 | emplazamiento local | posicionamento local | lokale Platzierung | placement local | ローカル配置 | 로컬 배치 | تموضع محلي | IfcLocalPlacement relative to parent (storey etc.) |
| IFC | Profile | профиль | 截面轮廓 | perfil | perfil | Profil | profil | プロファイル | 프로파일 | مقطع / بروفايل | 2D section used for extrusion (IfcIShapeProfileDef) |
| IFC | Material | материал | 材料 | material | material | Material / Baustoff | matériau | 材料 | 재료 | مادة | IfcMaterial |
| IFC | Material layer set | набор слоёв материала | 材料层集 | conjunto de capas de material | conjunto de camadas de material | Materialschichtaufbau | jeu de couches de matériau | 材料レイヤセット | 재료 레이어 세트 | مجموعة طبقات المادة | IfcMaterialLayerSet: wall/slab build-up |
| IFC | Classification | классификация | 分类 | clasificación | classificação | Klassifikation | classification | 分類 | 분류 | تصنيف | IfcClassification / IfcClassificationReference (Uniclass, OmniClass, etc.) |
| IFC | Unit (project unit) | единицы измерения | 单位 | unidad | unidade | Einheit | unité | 単位 | 단위 | وحدة | IfcUnitAssignment on IfcProject; IFC length is often millimetres or metres |
| IFC | Georeferencing | геопривязка | 地理配准 / 地理参考 | georreferenciación [V:31] | georreferenciamento [V:31] | Georeferenzierung [V:31] | géoréférencement [V:31] | ジオリファレンス [V:31] | 지오레퍼런싱 / 지리참조 | الإسناد الجغرافي | Placing the model in a map CRS: IfcMapConversion + IfcProjectedCRS (IFC4+) |
| IFC | Coordinate reference system (CRS) | система координат (СК) | 坐标参考系 | sistema de referencia de coordenadas | sistema de referência de coordenadas | Koordinatenbezugssystem | système de coordonnées de référence | 座標参照系 | 좌표 참조 시스템 | نظام الإسناد الإحداثي | e.g. EPSG:25832 |
| IFC | Coordinate system | система координат [V:31] | 坐标系 [V:31] | sistema de coordenadas [V:31] | sistema de coordenadas [V:31] | Koordinatensystem [V:31] | système de coordonnées [V:31] | 座標系 [V:31] | 좌표계 [V:31] | نظام إحداثيات [V:31] | Axes and origin |
| IFC | True north | истинный север | 正北 / 真北 | norte verdadero | norte verdadeiro | geografisch Nord (Nordrichtung) | nord géographique | 真北 | 진북 | الشمال الحقيقي | IfcGeometricRepresentationContext.TrueNorth |
| IFC | Model View Definition (MVD) | определение модельного представления (MVD) | 模型视图定义 (MVD) | definición de vista de modelo (MVD) | definição de vista de modelo (MVD) | Modellansichtsdefinition (MVD) | définition de vue de modèle (MVD) | モデルビュー定義 (MVD) | 모델 뷰 정의 (MVD) | تعريف عرض النموذج (MVD) | Subset of IFC needed for one exchange scenario [7][50] |
| IFC | Reference View (RV 1.2) | эталонное представление | 参考视图 | vista de referencia | vista de referência | Reference View | vue de référence | リファレンスビュー | 참조 뷰 | عرض مرجعي | IFC4 MVD for read-only coordination (usual "IFC4 export" choice) |
| IFC | Design Transfer View (DTV) | представление для передачи проекта | 设计传递视图 | vista de transferencia de diseño | vista de transferência de projeto | Design Transfer View | vue de transfert de conception | 設計転送ビュー | 설계 전달 뷰 | عرض نقل التصميم | IFC4 MVD for editable hand-over between authoring tools |
| IFC | Coordination View 2.0 | представление для координации 2.0 | 协调视图 2.0 | Coordination View 2.0 | Coordination View 2.0 | Coordination View 2.0 | Coordination View 2.0 | コーディネーションビュー 2.0 | 코디네이션 뷰 2.0 | Coordination View 2.0 | Classic IFC2x3 MVD, default Revit IFC2x3 export |
| IFC | Information Delivery Manual (IDM) | руководство по передаче информации (IDM) | 信息交付手册 (IDM) | Manual de entrega de información (IDM) | Manual de entrega de informação (IDM) | Informationslieferhandbuch (IDM) | manuel de livraison d'information (IDM) | 情報デリバリーマニュアル (IDM) | 정보 전달 매뉴얼 (IDM) | دليل تسليم المعلومات (IDM) | Process-level description of an exchange (ISO 29481) |
| IFC | Information Delivery Specification (IDS) | спецификация передачи информации (IDS) | 信息交付规范 (IDS) | especificación de entrega de información (IDS) | especificação de entrega de informação (IDS) | Informationslieferspezifikation (IDS) | spécification de livraison d'information (IDS) | 情報納品仕様 (IDS) | 정보 전달 사양 (IDS) | مواصفة تسليم المعلومات (IDS) | Machine-readable XML rules (.ids) checking IFC content; v1.0 final [5] |
| IFC | BIM Collaboration Format (BCF) | формат совместной работы BIM (BCF) | BIM 协作格式 (BCF) | formato de colaboración BIM (BCF) | formato de colaboração BIM (BCF) | BIM-Kollaborationsformat (BCF) | format de collaboration BIM (BCF) | BIMコラボレーションフォーマット (BCF) | BIM 협업 포맷 (BCF) | صيغة التعاون في BIM (BCF) | Issues exchanged as .bcf/.bcfzip or BCF-API (REST); v3.0 [6][7] |
| IFC | BCF topic / issue | тема (замечание) BCF | BCF 问题 | tema / incidencia BCF | tópico / questão BCF | BCF-Thema / Issue | sujet / point BCF | BCF課題 | BCF 이슈 | موضوع BCF | One issue with title, status, comments |
| IFC | Viewpoint | точка обзора | 视点 | punto de vista | ponto de vista | Ansicht (Viewpoint) | point de vue | ビューポイント | 뷰포인트 | وجهة نظر | Camera + visible components stored in a BCF topic |
| IFC | buildingSMART Data Dictionary (bSDD) | словарь данных buildingSMART (bSDD) | buildingSMART 数据字典 (bSDD) | diccionario de datos buildingSMART (bSDD) | dicionário de dados buildingSMART (bSDD) | buildingSMART Data Dictionary (bSDD) | dictionnaire de données buildingSMART (bSDD) | buildingSMART データ辞書 (bSDD) | buildingSMART 데이터 사전 (bSDD) | قاموس بيانات buildingSMART (bSDD) | Online classifications, properties and translations linked to IFC [7] |
| IFC | Model validation / checker | валидация модели | 模型验证 | validación de modelo | validação de modelo | Modellprüfung | validation de modèle | モデル検証 | 모델 검증 | التحقق من النموذج | Checking IFC syntax/schema and project rules (IDS) |
| IFC | IFC export | экспорт в IFC | 导出 IFC | exportar a IFC | exportar para IFC | IFC-Export | export IFC | IFC出力 (エクスポート) | IFC 내보내기 | تصدير IFC | Native-to-IFC translation; lossy by nature |
| IFC | IFC import / link | импорт / связь IFC | 导入 / 链接 IFC | importar / vincular IFC | importar / vincular IFC | IFC-Import / -Verknüpfung | import / lien IFC | IFC読み込み / リンク | IFC 가져오기 / 링크 | استيراد / ربط IFC | Open or link IFC inside an authoring tool |
| IFC | Interoperability | интероперабельность (совместимость) | 互操作性 | interoperabilidad | interoperabilidade | Interoperabilität | interopérabilité | 相互運用性 | 상호운용성 | قابلية التشغيل البيني | Ability of tools to exchange and use data |
| IFC | Task (4D) | задача (4D) | 任务 (4D) | tarea (4D) | tarefa (4D) | Vorgang (4D) | tâche (4D) | タスク (4D) | 태스크 (4D) | مهمة (4D) | IfcTask in IfcWorkSchedule (time) |
| IFC | Cost item (5D) | позиция стоимости (5D) | 成本项 (5D) | partida de coste (5D) | item de custo (5D) | Kostenposition (5D) | poste de coût (5D) | コスト項目 (5D) | 비용 항목 (5D) | بند التكلفة (5D) | IfcCostItem in IfcCostSchedule |
| IFC | Actor / Person / Organization | участник / лицо / организация | 参与方 / 人员 / 组织 | agente / persona / organización | ator / pessoa / organização | Akteur / Person / Organisation | acteur / personne / organisation | 関係者 / 個人 / 組織 | 참여자 / 개인 / 조직 | جهة فاعلة / شخص / منظمة | IfcActor, IfcPerson, IfcOrganization |
| IFC | Document reference | ссылка на документ | 文档引用 | referencia de documento | referência de documento | Dokumentverweis | référence de document | 文書参照 | 문서 참조 | مرجع مستند | IfcDocumentReference |
| IFC | Pset_WallCommon | Pset_WallCommon | Pset_WallCommon | Pset_WallCommon | Pset_WallCommon | Pset_WallCommon | Pset_WallCommon | Pset_WallCommon | Pset_WallCommon | Pset_WallCommon | Standard wall set: IsExternal, LoadBearing, FireRating, Reference, ThermalTransmittance (not translated) [42] |
| IFC | IsExternal | наружный (IsExternal) | 是否外部 (IsExternal) | es exterior (IsExternal) | é externo (IsExternal) | Außenbauteil (IsExternal) | extérieur (IsExternal) | 外部か (IsExternal) | 외부 여부 (IsExternal) | خارجي (IsExternal) | Boolean property in Pset_*Common; drives energy and fire checks |
| IFC | LoadBearing | несущий (LoadBearing) | 承重 (LoadBearing) | portante (LoadBearing) | portante / estrutural (LoadBearing) | tragend (LoadBearing) | porteur (LoadBearing) | 耐力 (LoadBearing) | 내력 (LoadBearing) | حامل (LoadBearing) | Boolean property in Pset_*Common |
| IFC | FireRating | предел огнестойкости (FireRating) | 耐火等级 (FireRating) | resistencia al fuego (FireRating) | resistência ao fogo (FireRating) | Feuerwiderstand (FireRating) | résistance au feu (FireRating) | 耐火等級 (FireRating) | 내화 등급 (FireRating) | مقاومة الحريق (FireRating) | Text property in Pset_*Common, free-form values like "REI 60" or "EI60" |
| RVT | Revit | Revit | Revit | Revit | Revit | Revit | Revit | Revit | Revit | Revit | Autodesk BIM authoring software (.rvt) |
| RVT | Family | семейство [V:17] | 族 [V:26] | familia [V:21] | família [V:22] | Familie [V:19] | famille [V:20] | ファミリ [V:23] | 패밀리 [V:24] | عائلة | Parametric content definition; all Revit elements belong to a family [46] |
| RVT | System family | системное семейство | 系统族 | familia de sistema [V:47] | família de sistema | Systemfamilie | famille système [V:46] | システム ファミリ | 시스템 패밀리 | عائلة نظام | Built into Revit (walls, floors, roofs, levels); cannot be loaded or deleted [46] |
| RVT | Loadable family | загружаемое семейство | 可载入族 | familia cargable [V:47] | família carregável | ladbare Familie | famille de composants / chargeable | ロード可能ファミリ | 로드 가능 패밀리 | عائلة قابلة للتحميل | .rfa file loaded into project (doors, furniture) |
| RVT | In-place family (model in place) | контекстное семейство | 内建族 / 在位族 | familia in situ | família no local | Family im Kontext (In-Place) | famille in situ | 内部ファミリ | 내부 패밀리 | عائلة مباشرة | One-off geometry made inside the project |
| RVT | Family Editor | редактор семейств [V:25] | 族编辑器 [V:26] | editor de familias [V:21] | editor de família [V:22] | Familieneditor [V:19] | éditeur de familles [V:20] | ファミリ エディタ [V:23] | 패밀리 편집기 [V:24] | محرر العائلات | Tool to author .rfa |
| RVT | Family type | типоразмер | 类型 | tipo de familia | tipo de família | Familientyp | type de famille | タイプ | 유형 | نوع العائلة | Named variant with fixed type parameters (e.g. 900x2100) [46] |
| RVT | Type parameter | параметр типа | 类型参数 | parámetro de tipo | parâmetro de tipo | Typparameter | paramètre de type [V:48] | タイプ パラメータ | 유형 매개변수 | معامل النوع | Value shared by all elements of that type |
| RVT | Instance (Element) | экземпляр | 实例 | ejemplar | instância | Exemplar | occurrence [V:48] | インスタンス | 인스턴스 | نسخة | One placed element in the project (maps to IFC occurrence) |
| RVT | Instance parameter | параметр экземпляра | 实例参数 | parámetro de ejemplar [V:47] | parâmetro de instância | Exemplarparameter | paramètre d'occurrence [V:48] | インスタンス パラメータ | 인스턴스 매개변수 | معامل النسخة | Value specific to one placed element |
| RVT | Category | категория [V:25] | 类别 | categoría | categoria [V:22] | Kategorie | catégorie | カテゴリ [V:23] | 카테고리 | فئة | Top-level classification (Walls, Doors); Revit category drives IFC class mapping |
| RVT | Subcategory | подкатегория | 子类别 | subcategoría | subcategoria | Unterkategorie | sous-catégorie | サブカテゴリ | 하위 카테고리 | فئة فرعية | Child of a category (e.g. door panel) |
| RVT | Parameter | параметр [V:25] | 参数 [V:26] | parámetro [V:21] | parâmetro [V:22] | Parameter [V:19] | paramètre [V:20] | パラメータ [V:23] | 매개변수 [V:24] | معامل / وسيط | Named property of element, category or family |
| RVT | Shared parameter | общий параметр [V:25] | 共享参数 [V:26] | parámetro compartido [V:21] | parâmetro compartilhado [V:22] | gemeinsam genutzter Parameter [V:19] | paramètre partagé [V:20] | 共有パラメータ [V:23] | 공유 매개변수 [V:24] | معامل مشترك | Definition with GUID in a text file reusable across families/projects; values are not shared automatically [52] |
| RVT | Shared parameter file | файл общих параметров [V:25] | 共享参数文件 [V:26] | archivo de parámetros compartidos [V:21] | arquivo de parâmetros compartilhados [V:22] | Datei mit gemeinsam genutzten Parametern [V:19] | fichier de paramètres partagés [V:20] | 共有パラメータ ファイル [V:23] | 공유 매개변수 파일 [V:24] | ملف المعاملات المشتركة | .txt; Revit references only one file per session [52] |
| RVT | Project parameter | параметр проекта | 项目参数 | parámetro de proyecto | parâmetro de projeto | Projektparameter | paramètre de projet | プロジェクト パラメータ | 프로젝트 매개변수 | معامل المشروع | Parameter bound to categories in one project; can be scheduled |
| RVT | Family parameter | параметр семейства | 族参数 | parámetro de familia | parâmetro de família | Familienparameter | paramètre de famille | ファミリ パラメータ | 패밀리 매개변수 | معامل العائلة | Exists only in the family; cannot be tagged or scheduled unless shared |
| RVT | Global parameter | глобальный параметр | 全局参数 | parámetro global | parâmetro global | globaler Parameter | paramètre global | グローバル パラメータ | 글로벌 매개변수 | معامل عام | Project-wide value driving dimensions/constraints, not category-bound |
| RVT | Built-in (system) parameter | встроенный параметр | 内置参数 | parámetro integrado | parâmetro integrado | integrierter Parameter | paramètre intégré | 組み込みパラメータ | 기본 제공 매개변수 | معامل مدمج | Cannot be renamed or deleted |
| RVT | IFC Parameters group | группа «Параметры IFC» | “IFC 参数”组 | grupo «Parámetros IFC» | grupo «Parâmetros IFC» | Gruppe «IFC-Parameter» | groupe «Paramètres IFC» | 「IFC パラメータ」グループ | “IFC 매개변수” 그룹 | مجموعة معاملات IFC | Properties-palette group holding Export to IFC As, IfcGUID, IfcName, IfcType etc. (exact UI labels per version unverified) |
| RVT | Export to IFC As | экспортировать в IFC как | 导出到 IFC 为 | exportar a IFC como | exportar para IFC como | Exportieren nach IFC als | exporter vers IFC en tant que | IFC としてエクスポート | IFC로 내보내기 | تصدير كـ IFC | Per-element override of the IFC class (e.g. IfcWall vs IfcCurtainWall) |
| RVT | IFC Mapping Table | таблица сопоставления IFC | IFC 映射表 | tabla de asignación IFC | tabela de mapeamento IFC | IFC-Zuordnungstabelle | table de correspondance IFC | IFC マッピング テーブル | IFC 매핑 테이블 | جدول مطابقة IFC | Text file mapping Revit category/type to IFC class/type [50] |
| RVT | Project file / Family file / Template | файл проекта / семейства / шаблон | 项目文件 / 族文件 / 样板 | archivo de proyecto / familia / plantilla | arquivo de projeto / família / modelo | Projektdatei / Familiendatei / Vorlage | fichier projet / famille / modèle | プロジェクト / ファミリ / テンプレート | 프로젝트 / 패밀리 / 템플릿 | ملف مشروع / عائلة / قالب | .rvt / .rfa / .rte (family template .rft) |
| RVT | Project Browser | диспетчер проекта | 项目浏览器 [V:18] | navegador de proyectos [V:13] | navegador de projeto [V:14] | Projektbrowser [V:11] | navigateur de projet | プロジェクト ブラウザ | 프로젝트 탐색기 [V:16] | متصفح المشروع | Tree of views, sheets, schedules, families, Revit Links |
| RVT | Properties palette | палитра свойств | 属性选项板 | paleta de propiedades | paleta de propriedades | Eigenschaftenpalette | palette des propriétés | プロパティ パレット | 특성 팔레트 | لوحة الخصائص | Panel showing instance (and type) parameters |
| RVT | View | вид | 视图 | vista | vista | Ansicht | vue | ビュー | 뷰 | عرض | Floor plan, section, 3D, schedule etc. |
| RVT | Floor plan | план этажа | 楼层平面 | planta | planta baixa | Grundriss | plan d'étage | 平面図 | 평면도 | مسقط أفقي | Horizontal view tied to a level |
| RVT | Section | разрез | 剖面 | sección | corte | Schnitt | coupe | 断面図 | 단면도 | مقطع | |
| RVT | Elevation | фасад | 立面 | alzado | elevação | Ansicht (Fassade) | élévation | 立面図 | 입면도 | واجهة | |
| RVT | 3D view | 3D-вид | 三维视图 | vista 3D | vista 3D | 3D-Ansicht | vue 3D | 3Dビュー | 3D 뷰 | عرض ثلاثي الأبعاد | |
| RVT | Sheet | лист | 图纸 | plano / lámina | prancha | Plan (Blatt) | feuille | シート | 시트 | لوحة رسم | Drawing sheet holding view placements |
| RVT | Schedule | спецификация | 明细表 | tabla de planificación | tabela de quantidades | Bauteilliste | nomenclature | 集計表 (スケジュール) | 일람표 | جدول | Tabular view of element parameters; basis for QTO |
| RVT | Material takeoff | ведомость материалов | 材料提取 | tabla de cantidades de material | levantamento de materiais | Materialauszug | relevé de matériaux | マテリアル集計 | 재료 일람표 | حصر المواد | Schedule by material layers |
| RVT | View template | шаблон вида | 视图样板 | plantilla de vista | modelo de vista | Ansichtsvorlage | modèle de vue | ビュー テンプレート | 뷰 템플릿 | قالب العرض | Reusable view settings |
| RVT | Visibility/Graphics | видимость/графика | 可见性/图形 | visibilidad/gráficos | visibilidade/gráficos | Sichtbarkeit/Grafiken | visibilité/graphismes | 表示/グラフィックス | 가시성/그래픽 | الرؤية/الرسوميات | VG dialog; controls link visibility too |
| RVT | Level | уровень | 标高 | nivel | nível | Ebene | niveau | レベル | 레벨 | منسوب / مستوى | Horizontal datum plane; usually becomes IfcBuildingStorey on export [38] |
| RVT | Grid | сетка осей | 轴网 | rejilla | grade | Raster | quadrillage | 通り芯 | 그리드 | شبكة | |
| RVT | Reference plane | рабочая плоскость (опорная) | 参照平面 | plano de referencia | plano de referência | Referenzebene | plan de référence | 参照面 | 참조 평면 | مستوى مرجعي | |
| RVT | Phase | стадия [V:17] | 阶段 [V:18] | fase [V:13] | fase [V:14] | Phase [V:11] | phase [V:12] | フェーズ [V:15] | 단계 [V:16] | مرحلة | Construction timeline (Existing/New); linked-model phases map by name [10] |
| RVT | Phase filter | фильтр стадий | 阶段过滤器 | filtro de fases | filtro de fases | Phasenfilter | filtre de phase | フェーズ フィルタ | 단계 필터 | مرشح المراحل | |
| RVT | Design option | вариант конструкции | 设计选项 | opción de diseño | opção de projeto | Entwurfsoption | option de conception | 設計オプション | 디자인 옵션 | خيار التصميم | Alternate design branches in one model |
| RVT | Worksharing | совместная работа [V:17] | 工作共享 [V:18] | uso compartido / trabajo compartido [V:29][49] | compartilhamento de trabalho (unverified) | Arbeitsteilung [V:27] | partage de projet [V:28] | ワークシェアリング [V:15] | 작업 공유 [V:16] | العمل المشترك | Multi-user editing of one model via central/local files |
| RVT | Workset | рабочий набор [V:17] | 工作集 [V:18] | subproyecto [V:29][49] | workset [V:14] (conjunto de trabalho in general usage) | Bearbeitungsbereich [V:27] | sous-projet [V:28] | ワークセット [V:15] | 작업세트 [V:16] | مجموعة عمل | Ownership/visibility partition; default sets: Shared Levels and Grids + one per loaded family [30] |
| RVT | Central model | центральная модель | 中心文件 | modelo central | modelo central | zentrales Modell | modèle central | セントラル モデル | 중앙 모델 | النموذج المركزي | Master file for worksharing |
| RVT | Local file | локальный файл | 本地文件 | archivo local | arquivo local | lokale Datei | fichier local | ローカル ファイル | 로컬 파일 | ملف محلي | User's copy of the central |
| RVT | Synchronize with Central | синхронизация с central | 与中心文件同步 | sincronizar con el modelo central | sincronizar com o central | Mit zentralem Modell synchronisieren | synchroniser avec le fichier central | セントラル モデルと同期 | 중앙 모델과 동기화 | المزامنة مع المركز | |
| RVT | Linked model (Revit Link) | связанная модель [V:17] | 链接模型 [V:18] | modelo vinculado [V:13] | modelo vinculado [V:14] | verknüpftes Modell [V:11] | modèle lié [V:12] | リンク モデル [V:15] | 링크된 모델 [V:16] | نموذج مرتبط | A .rvt referenced by another; browser branch "Revit Links" [10] |
| RVT | Revit Links (browser branch) | Связи Revit | Revit 链接 [V:18] | Vínculos de Revit [V:13] | Vínculos do Revit [V:14] | Revit-Verknüpfungen [V:11] | Liens Revit [V:12] | Revit リンク | Revit 링크 [V:16] | روابط Revit | Project Browser node |
| RVT | Host model | главная модель [V:17] | 主体模型 | modelo anfitrión [V:13] | modelo hospedeiro [V:14] | Hostmodell | modèle hôte [V:12] | ホスト モデル [V:15] | 호스트 모델 | النموذج المضيف | The model that contains the link |
| RVT | Phase mapping | сопоставление стадий | 阶段映射 | correspondencia de fases | mapeamento de fases | Phasenzuordnung | correspondance des phases | フェーズのマッピング [V:15] | 단계 매핑 | مطابقة المراحل | |
| RVT | Copy/Monitor | копирование/мониторинг | 复制/监视 | copiar/supervisar | copiar/monitorar | Kopieren/Überwachen | copier/surveiller | コピー/モニタ | 복사/모니터 | نسخ/مراقبة | Coordination of levels/grids from a link |
| RVT | Coordination Review / Interference Check | проверка пересечений | 碰撞检查 | comprobación de interferencias | verificação de interferência | Kollisionsprüfung | contrôle des interférences | 干渉チェック | 간섭 검사 | فحص التداخل | Built-in clash tool inside Revit |
| RVT | CAD link / import | связь / импорт CAD | 链接 / 导入 CAD | vincular / importar CAD | vincular / importar CAD | CAD-Verknüpfung / -Import | lien / import CAO | CADリンク / 読み込み | CAD 링크 / 가져오기 | ربط / استيراد CAD | DWG/DGN/SAT |
| RVT | Project Base Point | базовая точка проекта | 项目基点 | punto base del proyecto | ponto base do projeto | Projektbasispunkt | point de base du projet | プロジェクト基準点 | 프로젝트 기준점 | نقطة أساس المشروع | Model origin reference; central to georeferencing |
| RVT | Survey Point | точка съёмки | 测量点 | punto topográfico | ponto de levantamento | Vermessungspunkt | point de relevé | 測量点 | 측량점 | نقطة المساحة | Real-world anchor |
| RVT | Shared coordinates | общие координаты | 共享坐标 | coordenadas compartidas | coordenadas compartilhadas | gemeinsame Koordinaten | coordonnées partagées | 共有座標 | 공유 좌표 | إحداثيات مشتركة | Coordinate system shared between linked models |
| RVT | Project North / True North | направление проекта / истинный север | 项目北 / 正北 | norte del proyecto / norte real | norte do projeto / norte real | Projektnorden / geografisch Nord | nord du projet / nord réel | プロジェクト北 / 真北 | 프로젝트 북쪽 / 진북 | شمال المشروع / الشمال الحقيقي | |
| RVT | Room | помещение | 房间 | habitación | ambiente | Raum | pièce | 部屋 | 룸 | غرفة | Revit room; exports as IfcSpace |
| RVT | Area (Revit) | площадь (зона) | 面积 | área | área | Fläche | surface | 面積 | 면적 | مساحة | Area plan object, not a room |
| RVT | Space (MEP) | пространство (MEP) | 空间 (MEP) | espacio (MEP) | espaço (MEP) | MEP-Raum | espace (MEP) | スペース (MEP) | 스페이스 (MEP) | حيّز (MEP) | Thermal-analysis volume; also exports as IfcSpace |
| RVT | Room bounding | ограничивающий помещение | 房间边界 | delimitación de habitación | delimitação de ambiente | raumbegrenzend | délimitation de pièce | 部屋境界 | 룸 경계 | حد الغرفة | Whether an element closes a room |
| RVT | Group | группа | 组 | grupo | grupo | Gruppe | groupe | グループ | 그룹 | مجموعة | Revit group of elements |
| RVT | Tag | марка | 标记 | etiqueta | etiqueta | Beschriftung (Tag) | repère | タグ | 태그 | وسم | Annotation reading parameter values |
| RVT | Dynamo | Dynamo | Dynamo | Dynamo | Dynamo | Dynamo | Dynamo | Dynamo | Dynamo | Dynamo | Visual scripting add-on shipped with Revit |
| RVT | Revit API / add-in | Revit API / плагин | Revit API / 插件 | API de Revit / complemento | API do Revit / suplemento | Revit-API / Add-In | API Revit / complément | Revit API / アドイン | Revit API / 애드인 | واجهة برمجة Revit / إضافة | How most Revit MCP servers drive Revit |
| RVT | ElementId / UniqueId | ElementId / UniqueId | ElementId / UniqueId | ElementId / UniqueId | ElementId / UniqueId | ElementId / UniqueId | ElementId / UniqueId | ElementId / UniqueId | ElementId / UniqueId | ElementId / UniqueId | Revit's integer id (session/file-local) vs UniqueId string; neither equals IFC GlobalId unless exported/stored |
| RVT | Detach from Central | отсоединить от central | 脱离中心文件 | desvincular del modelo central | desanexar do central | vom zentralen Modell trennen | détacher du fichier central | セントラルから切り離し | 중앙에서 분리 | فصل عن المركز | |
| RVT | Purge Unused | удалить неиспользуемое | 清除未使用项 | purgar no utilizados | limpar não utilizados | Nicht verwendete entfernen | purger les éléments inutilisés | 未使用を整理 | 사용하지 않는 항목 소거 | حذف غير المستخدم | |
| PRC | BIM (Building Information Modeling) | информационное моделирование (BIM) | 建筑信息模型 (BIM) [V:31] | modelado de información de construcción (BIM) [V:31] | BIM [V:31] | Building Information Modeling [V:31] | Building information modeling [V:31] | BIM [V:31] | 빌딩 정보 모델링 [V:31] | نمذجة معلومات المباني [V:31] | Process and models for digital building information |
| PRC | Information model | информационная модель | 信息模型 | modelo de información | modelo de informação | Informationsmodell | modèle d'information | 情報モデル | 정보 모델 | نموذج المعلومات | |
| PRC | Common Data Environment (CDE) | среда общих данных (СОД) | 公共数据环境 / 通用数据环境 | entorno común de datos | ambiente comum de dados | gemeinsame Datenumgebung | environnement commun de données | 共通データ環境 [V:35] | 공통데이터환경 | بيئة البيانات المشتركة | Agreed source of project information with workflow states [45][37] |
| PRC | Exchange Information Requirements (EIR) | требования к обмену информацией (EIR) | 信息交换要求 (EIR) | requisitos de intercambio de información (EIR) | requisitos de troca de informações (EIR) | Auftraggeber-Informationsanforderungen (AIA) [V:32] | exigences d'échange d'informations (EIR) | 発注者情報要件 (EIR) [V:35] | 발주자 정보요구사항 (EIR) | متطلبات تبادل المعلومات (EIR) | Client's information needs for an appointment; "Employer's" is a synonym in UK/HK usage [44] |
| PRC | BIM Execution Plan (BEP) | план реализации проекта с применением BIM (BEP) | BIM 实施计划 / 执行计划 (BEP) | plan de ejecución BIM (BEP) | plano de execução BIM (BEP) | BIM-Abwicklungsplan (BAP) [V:32] | plan d'exécution BIM (BEP) | BIM実行計画 (BEP) [V:35] | BIM 실행계획 (BEP) | خطة تنفيذ BIM (BEP) | Supplier's response to the EIR; pre- and post-appointment versions [37] |
| PRC | Organizational information requirements (OIR) | организационные информационные требования (OIR) | 组织信息需求 (OIR) | requisitos de información de la organización (OIR) | requisitos de informação da organização (OIR) | Organisations-Informationsanforderungen (OIR) | exigences d'information de l'organisation (OIR) | 組織情報要件 (OIR) | 조직 정보 요구사항 (OIR) | متطلبات معلومات المنظمة (OIR) | ISO 19650-1 |
| PRC | Project information requirements (PIR) | информационные требования проекта (PIR) | 项目信息需求 (PIR) | requisitos de información del proyecto (PIR) | requisitos de informação do projeto (PIR) | Projekt-Informationsanforderungen (PIR) | exigences d'information du projet (PIR) | プロジェクト情報要件 (PIR) | 프로젝트 정보 요구사항 (PIR) | متطلبات معلومات المشروع (PIR) | |
| PRC | Asset information requirements (AIR) | информационные требования к активу (AIR) | 资产信息需求 (AIR) | requisitos de información del activo (AIR) | requisitos de informação do ativo (AIR) | Asset-Informationsanforderungen (AIR) | exigences d'information de l'actif (AIR) | 資産情報要件 (AIR) | 자산 정보 요구사항 (AIR) | متطلبات معلومات الأصل (AIR) | |
| PRC | Project information model (PIM) | информационная модель проекта (PIM) | 项目信息模型 (PIM) | modelo de información del proyecto (PIM) | modelo de informação do projeto (PIM) | Projekt-Informationsmodell (PIM) | maquette d'information du projet (PIM) | プロジェクト情報モデル (PIM) | 프로젝트 정보 모델 (PIM) | نموذج معلومات المشروع (PIM) | Delivery-phase model |
| PRC | Asset information model (AIM) | информационная модель актива (AIM) | 资产信息模型 (AIM) | modelo de información del activo (AIM) | modelo de informação do ativo (AIM) | Bestands-Informationsmodell (AIM) | maquette d'information de l'actif (AIM) | 資産情報モデル (AIM) | 자산 정보 모델 (AIM) | نموذج معلومات الأصل (AIM) | Operation-phase model |
| PRC | Appointing party | назначающая сторона (заказчик) | 委托方 / 业主 | parte contratante | parte contratante | Auftraggeber | maître d'ouvrage / partie contractante | 発注者 | 발주자 | الطرف المُعيِّن | ISO 19650 role [44] |
| PRC | Lead appointed party | ведущая назначенная сторона | 牵头受托方 | parte designada principal | parte nomeada principal | federführender Auftragnehmer | partie désignée principale | 主たる受注者 | 주 수급자 | الطرف المعيَّن الرئيسي | Manages information production, usually runs the CDE [45] |
| PRC | Task team | рабочая группа | 任务团队 | equipo de tarea | equipe de tarefa | Aufgabenteam | équipe de tâche | タスクチーム | 태스크 팀 | فريق المهمة | |
| PRC | Information manager | менеджер по информации | 信息经理 | gestor de información | gerente de informação | Informationsmanager | gestionnaire d'information | 情報マネージャー | 정보 관리자 | مدير المعلومات | |
| PRC | BIM manager / coordinator | BIM-менеджер / BIM-координатор | BIM 经理 / BIM 协调员 | BIM manager / coordinador BIM | gerente BIM / coordenador BIM | BIM-Manager / BIM-Koordinator | BIM manager / coordinateur BIM | BIMマネージャー / BIMコーディネーター | BIM 매니저 / BIM 코디네이터 | مدير BIM / منسق BIM | |
| PRC | Master information delivery plan (MIDP) | сводный план передачи информации (MIDP) | 主信息交付计划 (MIDP) | plan maestro de entrega de información (MIDP) | plano mestre de entrega de informação (MIDP) | Master-Informationslieferplan (MIDP) | plan directeur de livraison d'information (MIDP) | マスター情報納品計画 (MIDP) | 마스터 정보 인도 계획 (MIDP) | خطة التسليم الرئيسية (MIDP) | |
| PRC | Task information delivery plan (TIDP) | план передачи информации по задаче (TIDP) | 任务信息交付计划 (TIDP) | plan de entrega de información de tarea (TIDP) | plano de entrega de informação da tarefa (TIDP) | Aufgaben-Informationslieferplan (TIDP) | plan de livraison d'information de tâche (TIDP) | タスク情報納品計画 (TIDP) | 태스크 정보 인도 계획 (TIDP) | خطة تسليم المهمة (TIDP) | |
| PRC | Information container | информационный контейнер | 信息容器 | contenedor de información | contêiner de informação | Informationscontainer | conteneur d'information | 情報コンテナ | 정보 컨테이너 | حاوية المعلومات | Named file/model/doc in the CDE |
| PRC | WIP / Shared / Published / Archive | В работе / Общий доступ / Опубликовано / Архив | 工作中 / 共享 / 发布 / 归档 | En curso / Compartido / Publicado / Archivo | Em andamento / Compartilhado / Publicado / Arquivado | In Bearbeitung / Geteilt / Veröffentlicht / Archiviert | En cours / Partagé / Publié / Archivé | 作業中 / 共有 / 公開 / アーカイブ | 작업 중 / 공유 / 발행 / 보관 | قيد العمل / مشترك / منشور / أرشيف | ISO 19650-2 CDE states (the German states list given in search results as in Arbeit/geteilt/veröffentlicht/archiviert) |
| PRC | Level of Development / Detail (LOD) | уровень проработки (LOD) | 模型精细度 (LOD) [V:34] | nivel de desarrollo (LOD) | nível de desenvolvimento (LOD) | Fertigstellungsgrad (LOD) | niveau de développement (LOD) | 詳細度 (LOD) | 상세 수준 (LOD) | مستوى التطوير (LOD) | Geometry/detail maturity; superseded in ISO by LOIN |
| PRC | Level of Information (LOI) | уровень информации (LOI) | 信息深度 (LOI) | nivel de información (LOI) | nível de informação (LOI) | Informationstiefe (LOI) | niveau d'information (LOI) | 情報レベル (LOI) | 정보 수준 (LOI) | مستوى المعلومات (LOI) | Non-graphical data richness |
| PRC | Level of Geometry (LOG) | уровень геометрии (LOG) | 几何表达精度 (LOG) | nivel de geometría (LOG) | nível de geometria (LOG) | Geometriegrad (LOG) | niveau de géométrie (LOG) | 幾何レベル (LOG) | 형상 수준 (LOG) | مستوى الهندسة (LOG) | |
| PRC | Level of information need (LOIN) | уровень информационной потребности (LOIN) | 信息需求深度 (LOIN) | nivel de información necesario (LOIN) | nível de necessidade de informação (LOIN) | Informationsbedarfstiefe (LOIN) | niveau de besoin d'information (LOIN) | 情報需要レベル (LOIN) | 정보 요구 수준 (LOIN) | مستوى الحاجة للمعلومات (LOIN) | ISO 7817-1:2024: geometry + alphanumeric + documentation per purpose [9] |
| PRC | Information requirement | информационное требование | 信息需求 | requisito de información | requisito de informação | Informationsanforderung | exigence d'information | 情報要件 | 정보 요구사항 | متطلب معلومات | |
| PRC | Deliverable | поставляемый результат | 交付物 | entregable | entregável | Lieferobjekt | livrable | 納品物 | 납품물 | مُخرَج | |
| PRC | Milestone / data drop | веха / передача данных | 里程碑 / 数据交付点 | hito / entrega de datos | marco / entrega de dados | Meilenstein / Datenlieferung | jalon / livraison de données | マイルストーン / データ納品 | 마일스톤 / 데이터 인도 | معلم / تسليم بيانات | |
| PRC | Clash detection | проверка на коллизии (пересечения) | 碰撞检查 | detección de interferencias (colisiones) | detecção de interferências (conflitos) | Kollisionsprüfung | détection de conflits (clash) | 干渉チェック | 간섭 체크 | كشف التعارضات | Finding geometry overlaps between disciplines |
| PRC | Clash (conflict) | коллизия | 碰撞 | interferencia (colisión) | interferência (conflito) | Kollision | conflit (clash) | 干渉 | 간섭 | تعارض | One detected overlap; often a BCF issue |
| PRC | Hard clash / soft clash | жёсткая / мягкая коллизия | 硬碰撞 / 软碰撞 | colisión dura / blanda | interferência rígida / flexível | harte / weiche Kollision | conflit dur / mou | ハード干渉 / ソフト干渉 | 하드 / 소프트 간섭 | تعارض صلب / ناعم | Solid overlap vs clearance violation |
| PRC | Coordination | координация | 协调 | coordinación | coordenação | Koordination | coordination | 調整 | 조정 | تنسيق | |
| PRC | Federation (federated model) | сводная модель | 联合模型 / 整合 | modelo federado | modelo federado | Koordinationsmodell | maquette fédérée / de synthèse | 統合モデル | 통합 모델 | النموذج المدمج | Discipline models combined without merging them |
| PRC | Discipline model | модель раздела (дисциплины) | 专业模型 | modelo de disciplina | modelo de disciplina | Fachmodell | maquette métier | 専門分野モデル | 분야별 모델 | نموذج التخصص | ARC/STR/MEP models |
| PRC | Handover | передача (сдача) | 移交 | entrega / traspaso | entrega (handover) | Übergabe | remise / livraison | 引き渡し | 인도 | تسليم | Delivery of information to the owner/operator |
| PRC | As-built (record) model | исполнительная модель (as-built) | 竣工模型 | modelo as-built (conforme a obra) | modelo as built (como construído) | As-built-Modell (Bestandsmodell) | maquette as-built / DOE | 竣工モデル | 준공 모델 | نموذج كما بُني | Model updated to what was actually built |
| PRC | Digital twin | цифровой двойник | 数字孪生 | gemelo digital | gêmeo digital | digitaler Zwilling | jumeau numérique | デジタルツイン | 디지털 트윈 | التوأم الرقمي | |
| PRC | COBie | COBie | COBie | COBie | COBie | COBie | COBie | COBie | COBie | COBie | Spreadsheet-based FM handover data (Construction-Operations Building information exchange) |
| PRC | Facility management (FM) | эксплуатация (FM) | 设施管理 | gestión de instalaciones (FM) | gestão de facilidades (FM) | Facility Management (FM) | gestion technique du patrimoine (FM) | ファシリティマネジメント | 시설 관리 | إدارة المرافق | |
| PRC | Quantity take-off (QTO) | ведомость объёмов работ | 工程量统计 | mediciones | levantamento de quantitativos | Mengenermittlung | métré | 数量拾い | 물량 산출 | حصر الكميات | |
| PRC | 4D / 5D BIM | 4D / 5D BIM | 4D / 5D BIM | BIM 4D / 5D | BIM 4D / 5D | 4D- / 5D-BIM | BIM 4D / 5D | 4D / 5D BIM | 4D / 5D BIM | BIM رباعي / خماسي الأبعاد | Time / cost-linked models |
| PRC | Naming convention | соглашение об именовании | 命名规则 | convención de nomenclatura | convenção de nomenclatura | Namenskonvention | convention de nommage | 命名規則 | 명명 규칙 | اصطلاح التسمية | |
| PRC | Responsibility matrix | матрица ответственности | 责任矩阵 | matriz de responsabilidades | matriz de responsabilidades | Verantwortungsmatrix | matrice de responsabilités | 責任分担表 | 책임 매트릭스 | مصفوفة المسؤوليات | |
| PRC | Model checking (QA) | проверка модели | 模型检查 | verificación del modelo | verificação do modelo | Modellprüfung | contrôle de maquette | モデルチェック | 모델 검토 | فحص النموذج | |
| PRC | Rule set | набор правил | 规则集 | conjunto de reglas | conjunto de regras | Regelwerk | jeu de règles | ルールセット | 규칙 세트 | مجموعة قواعد | |
| PRC | Information exchange | обмен информацией | 信息交换 | intercambio de información | intercâmbio de informação | Informationsaustausch | échange d'information | 情報交換 | 정보 교환 | تبادل المعلومات | |
| PRC | Open standard | открытый стандарт | 开放标准 | estándar abierto | padrão aberto | offener Standard | norme ouverte | オープン標準 | 개방형 표준 | معيار مفتوح | |
| PRC | Parametric | параметрический | 参数化 | paramétrico | paramétrico | parametrisch | paramétrique | パラメトリック | 파라메트릭 | بارامتري | |
| PRC | Scope of services | объём услуг | 服务范围 | alcance de servicios | escopo de serviços | Leistungsumfang | périmètre de prestation | 業務範囲 | 업무 범위 | نطاق الخدمات | |
| PRC | Digital delivery | цифровая передача | 数字化交付 | entrega digital | entrega digital | digitale Übergabe | livraison numérique | デジタル納品 | 디지털 납품 | التسليم الرقمي | |
| ELM | Wall | стена [V:31] | 墙 [V:31] | pared / muro [V:31] | parede (muro [V:31]) | Wand (Mauer [V:31]) | mur [V:31] | 壁 [V:31] | 벽 [V:31] | جدار [V:31] | IfcWall |
| ELM | Curtain wall | навесная стена | 幕墙 | muro cortina | parede cortina | Vorhangfassade | mur-rideau | カーテンウォール | 커튼월 | جدار ستاري | IfcCurtainWall |
| ELM | Slab | плита перекрытия | 楼板 | losa / forjado | laje | Geschossdecke / Platte | dalle | スラブ | 슬래브 | بلاطة | IfcSlab (FLOOR, ROOF, LANDING) |
| ELM | Floor (surface) | пол [V:31] | 地板 [V:31] | piso / suelo [V:31] | pavimento [V:31] | Fußboden [V:31] | plancher / sol [V:31] | 床 [V:31] | 마루 / 바닥 [V:31] | أرضية [V:31] | Revit "Floor" exports as IfcSlab |
| ELM | Roof | крыша (кровля) [V:31] | 屋顶 [V:31] | cubierta [V:31] | telhado / cobertura [V:31] | Dach [V:31] | toit / toiture [V:31] | 屋根 [V:31] | 지붕 [V:31] | سقف [V:31] | IfcRoof |
| ELM | Ceiling | потолок [V:31] | 天花板 [V:31] | techo / cielo raso [V:31] | teto / forro [V:31] | Decke (abgehängte) [V:31] | plafond [V:31] | 天井 [V:31] | 천장 [V:31] | سقف داخلي [V:31] | IfcCovering (CEILING) |
| ELM | Column | колонна [V:31] | 柱 [V:31] | columna / pilar [V:31] | coluna / pilar [V:31] | Stütze / Säule [V:31] | poteau / colonne [V:31] | 柱 [V:31] | 기둥 [V:31] | عمود [V:31] | IfcColumn |
| ELM | Beam | балка [V:31] | 梁 [V:31] | viga [V:31] | viga [V:31] | Träger / Unterzug [V:31] | poutre [V:31] | 梁 (はり) [V:31] | 보 / 들보 [V:31] | جائز [V:31] | IfcBeam |
| ELM | Door | дверь [V:31] | 门 | puerta [V:31] | porta [V:31] | Tür [V:31] | porte [V:31] | ドア / 扉 [V:31] | 문 [V:31] | باب [V:31] | IfcDoor |
| ELM | Window | окно | 窗 | ventana [V:31] | janela | Fenster [V:31] | fenêtre [V:31] | 窓 [V:31] | 창 / 창문 | نافذة [V:31] | IfcWindow |
| ELM | Stair | лестница [V:31] | 楼梯 [V:31] | escalera [V:31] | escada [V:31] | Treppe [V:31] | escalier [V:31] | 階段 [V:31] | 계단 [V:31] | درج [V:31] | IfcStair |
| ELM | Stair flight | марш | 梯段 | tramo | lance | Treppenlauf | volée | 階段の段部 | 계단 런 | ذراع الدرج | IfcStairFlight |
| ELM | Landing | площадка | 平台 | descanso / rellano | patamar | Podest | palier | 踊り場 | 계단참 | بسطة | |
| ELM | Ramp | пандус | 坡道 | rampa | rampa | Rampe | rampe | スロープ | 경사로 | منحدر | IfcRamp |
| ELM | Railing | ограждение | 栏杆 | barandilla | guarda-corpo | Geländer | garde-corps | 手すり | 난간 | درابزين | IfcRailing |
| ELM | Foundation | фундамент [V:31] | 基础 / 地基 [V:31] | cimentación [V:31] | fundação [V:31] | Gründung / Fundament [V:31] | fondation [V:31] | 基礎 [V:31] | 기초 [V:31] | أساس [V:31] | |
| ELM | Footing | фундаментная плита/опора | 独立基础 | zapata | sapata | Einzelfundament | semelle | フーチング | 기초판 | قاعدة | IfcFooting |
| ELM | Pile | свая | 桩 | pilote | estaca | Pfahl | pieu | 杭 | 말뚝 | خازوق | IfcPile |
| ELM | Covering | отделка (покрытие) | 饰面 / 覆层 | revestimiento | revestimento | Bekleidung | revêtement | 仕上げ | 마감재 | كسوة | IfcCovering |
| ELM | Opening | проём | 洞口 | hueco / abertura | abertura / vão | Öffnung / Durchbruch | ouverture / réservation | 開口 | 개구부 | فتحة | |
| ELM | Elevator | лифт [V:31] | 电梯 [V:31] | ascensor [V:31] | elevador [V:31] | Aufzug [V:31] | ascenseur [V:31] | エレベーター [V:31] | 엘리베이터 [V:31] | مصعد [V:31] | IfcTransportElement |
| ELM | Shaft | шахта | 井道 | patinillo / hueco | shaft / poço | Schacht | gaine | シャフト | 샤프트 | مجرى رأسي | |
| ELM | Balcony | балкон [V:31] | 阳台 / 露台 [V:31] | balcón [V:31] | varanda / sacada [V:31] | Balkon [V:31] | balcon [V:31] | バルコニー [V:31] | 발코니 [V:31] | شرفة [V:31] | |
| ELM | Furniture | мебель | 家具 | mobiliario | mobiliário | Möblierung / Möbel | mobilier | 家具 | 가구 | أثاث | IfcFurnishingElement / IfcFurniture |
| ELM | Plate | пластина | 板 | placa | placa | Platte / Blech | plaque | プレート | 플레이트 | لوح | IfcPlate (steel plate etc.) |
| ELM | Member | элемент каркаса | 杆件 | miembro | membro | Stab | élément (barre) | 部材 | 부재 | عضو | IfcMember (brace, purlin) |
| ELM | Reinforcing bar | арматурный стержень | 钢筋 | barra de refuerzo | barra de armadura | Bewehrungsstab | barre d'armature | 鉄筋 | 철근 | حديد تسليح | IfcReinforcingBar |
| ELM | Door/Window panel | полотно | 门窗扇 | hoja | folha | Flügel | vantail | 扉パネル | 문짝 | ضلفة | |
| ELM | Shading device | солнцезащитное устройство | 遮阳装置 | dispositivo de sombreado | dispositivo de sombreamento | Sonnenschutz | protection solaire | 日除け | 차양 장치 | جهاز تظليل | |
| MEP | MEP (building services) | инженерные системы (MEP) | 机电 / MEP | instalaciones (MEP) | instalações (MEP) | TGA (Technische Gebäudeausrüstung) | lots techniques (CVC-plomberie-électricité) | 設備 (MEP) | 설비 (MEP) | الأعمال الكهروميكانيكية (MEP) | |
| MEP | HVAC | ОВК (отопление, вентиляция, кондиционирование) [V:31] | 暖通空调 [V:31] | climatización [V:31] | climatização / AVAC (PT) [V:31] | Klimatechnik [V:31] | CVC (chauffage, ventilation, climatisation) [V:31] | 空気調和 [V:31] | 공기조화 [V:31] | التدفئة والتهوية وتكييف الهواء [V:31] | |
| MEP | Pipe | труба [V:31] | 管道 [V:31] | tubería [V:31] | tubo / tubulação [V:31] | Rohr [V:31] | tuyau [V:31] | パイプ (配管) [V:31] | 파이프 (배관) [V:31] | أنبوب [V:31] | IfcPipeSegment |
| MEP | Pipe fitting | фитинг | 管件 | accesorio de tubería | conexão de tubo | Rohrformstück | raccord | 配管継手 | 관 이음 | وصلة أنبوب | IfcPipeFitting |
| MEP | Duct | воздуховод | 风管 | conducto [V:31] | duto | Lüftungskanal [V:31] | gaine / conduit d'air | ダクト [V:31] | 덕트 | مجرى هواء [V:31] | IfcDuctSegment |
| MEP | Duct fitting | фасонная часть воздуховода | 风管管件 | accesorio de conducto | conexão de duto | Kanalformstück | raccord de gaine | ダクト継手 | 덕트 이음 | وصلة مجرى | IfcDuctFitting |
| MEP | Air terminal | воздухораспределитель | 风口 | difusor / rejilla | difusor | Luftdurchlass | bouche d'air | 吹出口 | 공기 터미널 | فتحة هواء | IfcAirTerminal |
| MEP | Pump | насос | 水泵 | bomba | bomba | Pumpe | pompe | ポンプ | 펌프 | مضخة | IfcPump |
| MEP | Fan | вентилятор | 风机 | ventilador | ventilador | Ventilator | ventilateur | ファン | 팬 | مروحة | IfcFan |
| MEP | Boiler | котёл | 锅炉 | caldera | caldeira | Heizkessel | chaudière | ボイラー | 보일러 | غلاية | IfcBoiler |
| MEP | Valve | клапан (арматура) | 阀门 | válvula | válvula | Ventil | vanne | バルブ | 밸브 | صمام | IfcValve |
| MEP | Cable tray / carrier | кабельный лоток | 电缆桥架 | bandeja de cables | eletrocalha | Kabeltrasse | chemin de câbles | ケーブルラック | 케이블 트레이 | مجرى كابلات | IfcCableCarrierSegment |
| MEP | Light fixture | светильник | 灯具 | luminaria | luminária | Leuchte | luminaire | 照明器具 | 조명기구 | وحدة إنارة | IfcLightFixture |
| MEP | Electrical panel / distribution board | распределительный щит | 配电箱 | cuadro eléctrico | quadro elétrico | Verteiler | tableau électrique | 分電盤 | 배전반 | لوحة توزيع | IfcElectricDistributionBoard |
| MEP | Sanitary terminal | сантехнический прибор | 卫生器具 | aparato sanitario | aparelho sanitário | Sanitärobjekt | appareil sanitaire | 衛生器具 | 위생기구 | تجهيز صحي | IfcSanitaryTerminal |
| MEP | Sensor | датчик | 传感器 | sensor | sensor | Sensor | capteur | センサー | 센서 | مستشعر | IfcSensor |
| MEP | Distribution system | система распределения | 分配系统 | sistema de distribución | sistema de distribuição | Verteilsystem | système de distribution | 配管・配線系統 | 배분 시스템 | نظام توزيع | IfcDistributionSystem |
| GEO | Georeferencing (Revit) | геопривязка | 地理定位 | georreferenciación | georreferenciamento | Georeferenzierung | géoréférencement | ジオリファレンス | 지오레퍼런싱 | إسناد جغرافي | Revit "Specify Coordinates at Point" / "Acquire Coordinates" workflows |
| GEO | Terrain / topography | рельеф | 地形 | terreno [V:31] | terreno | Gelände | terrain | 地形 | 지형 | تضاريس | IfcGeographicElement / site surface |
| GEO | Alignment | трасса | 线形 | trazado / alineación | alinhamento / traçado | Trassierung / Achse | tracé / axe | 線形 | 선형 | محور المسار | IfcAlignment (IFC4.3) |
| GEO | Road | дорога | 道路 | carretera | rodovia / estrada | Straße | route | 道路 | 도로 | طريق | IfcRoad (IFC4.3) |
| GEO | Bridge | мост | 桥梁 | puente | ponte | Brücke | pont | 橋 | 교량 | جسر | IfcBridge (IFC4.3) |
| GEO | Railway | железная дорога | 铁路 | ferrocarril | ferrovia | Eisenbahn | voie ferrée | 鉄道 | 철도 | سكة حديدية | IfcRailway (IFC4.3) |
| GEO | Infrastructure | инфраструктура | 基础设施 | infraestructura | infraestrutura | Infrastruktur | infrastructure | インフラ | 인프라 | بنية تحتية | |
| GEO | Map conversion | преобразование в карту | 地图转换 | conversión de mapa | conversão de mapa | Kartenumrechnung | conversion cartographique | 地図変換 | 지도 변환 | تحويل الخريطة | IfcMapConversion: eastings, northings, orthogonal height, rotation, scale |
| GEO | Eastings / Northings | восточное / северное смещение | 东坐标 / 北坐标 | coordenada Este / Norte | coordenada Leste / Norte | Rechtswert / Hochwert | est / nord | 東距 / 北距 | 동거리 / 북거리 | الإحداثي الشرقي / الشمالي | |
| GEO | EPSG code | код EPSG | EPSG 代码 | código EPSG | código EPSG | EPSG-Code | code EPSG | EPSGコード | EPSG 코드 | رمز EPSG | e.g. EPSG:4326, EPSG:3857 |
| GEO | Site boundary | граница участка | 场地边界 | límite de parcela | limite do terreno | Grundstücksgrenze | limite de parcelle | 敷地境界 | 대지 경계 | حدود الموقع | |
| GEO | Bounding box | габаритный параллелепипед | 包围盒 | caja delimitadora | caixa delimitadora | Hüllquader | boîte englobante | バウンディングボックス | 바운딩 박스 | صندوق محيط | Used by tools to compare / locate elements |
| GEO | Origin | начало координат | 原点 | origen | origem | Ursprung | origine | 原点 | 원점 | نقطة الأصل | Far-from-origin models cause precision/visual problems |
| GEO | Units (metric/imperial) | единицы (метрические/имперские) | 单位 (公制/英制) | unidades (métricas/imperiales) | unidades (métricas/imperiais) | Einheiten (metrisch/imperial) | unités (métriques/impériales) | 単位 (メートル/ヤード・ポンド) | 단위 (미터법/야드파운드) | الوحدات (متري/إمبراطوري) | Mismatched units are a classic export bug |
| ELM | Wall type | тип стены | 墙类型 | tipo de muro | tipo de parede | Wandtyp | type de mur | 壁タイプ | 벽 유형 | نوع الجدار | IfcWallType |
| ELM | Door type | тип двери | 门类型 | tipo de puerta | tipo de porta | Türtyp | type de porte | ドアタイプ | 문 유형 | نوع الباب | IfcDoorType (IFC4 has IfcDoorStyle legacy in IFC2x3) |
| ELM | Window type | тип окна | 窗类型 | tipo de ventana | tipo de janela | Fenstertyp | type de fenêtre | 窓タイプ | 창 유형 | نوع النافذة | IfcWindowType |
| ELM | Slab type | тип плиты | 楼板类型 | tipo de losa | tipo de laje | Deckentyp | type de dalle | スラブタイプ | 슬래브 유형 | نوع البلاطة | IfcSlabType |
| ELM | Fire rating | предел огнестойкости | 耐火等级 | resistencia al fuego | resistência ao fogo | Feuerwiderstandsklasse | résistance au feu | 耐火等級 | 내화 등급 | مقاومة الحريق | |
| ELM | Thermal transmittance (U-value) | коэффициент теплопередачи (U) | 传热系数 (U值) | transmitancia térmica (U) | transmitância térmica (U) | Wärmedurchgangskoeffizient (U-Wert) | transmittance thermique (U) | 熱貫流率 (U値) | 열관류율 (U값) | معامل انتقال الحرارة (U) | Pset_*Common.ThermalTransmittance |
| ELM | Finish | отделка | 装修面层 | acabado | acabamento | Oberfläche / Ausbau | finition | 仕上げ | 마감 | تشطيب | |
| ELM | Load-bearing | несущий | 承重 | portante | estrutural / portante | tragend | porteur | 耐力 | 내력 | حامل | |
| ELM | Structure (discipline) | конструкции (КР) | 结构 | estructura | estrutura | Tragwerk | structure | 構造 | 구조 | إنشائي | |
| ELM | Architecture (discipline) | архитектура (АР) | 建筑 | arquitectura | arquitetura | Architektur | architecture | 意匠 | 건축 | عمارة | |
| ELM | Material takeoff / bill of materials | ведомость материалов | 物料清单 [V:31] | lista de materiales | lista de materiais / estrutura de produto [V:31] | Stückliste [V:31] | nomenclature [V:31] | 部品表 (BOM) [V:31] | 자재 명세서 [V:31] | قائمة المواد [V:31] | |
| ELM | Thickness | толщина | 厚度 | espesor | espessura | Dicke | épaisseur | 厚さ | 두께 | سماكة | Width/Thickness attributes in Qto sets |
| ELM | Height | высота | 高度 | altura | altura | Höhe | hauteur | 高さ | 높이 | ارتفاع | NominalHeight, Height |
| ELM | Area / Volume / Length | площадь / объём / длина | 面积 / 体积 / 长度 | área / volumen / longitud | área / volume / comprimento | Fläche / Volumen / Länge | surface / volume / longueur | 面積 / 体積 / 長さ | 면적 / 체적 / 길이 | مساحة / حجم / طول | NetArea, GrossVolume, Length in Qto_* |
| ELM | Gross / Net | брутто / нетто | 毛 / 净 | bruto / neto | bruto / líquido | brutto / netto | brut / net | 総 / 正味 | 총 / 순 | إجمالي / صافي | Gross vs Net quantity variants |

## What the verified translations show

- Vendor-localized Revit help is the best evidence for the Revit-side terms, and the languages disagree more than expected [11]-[29]:
  - **Workset** has five different words: ワークセット (JA), 작업세트 (KO), 工作集 (ZH), рабочий набор (RU), and the German **Bearbeitungsbereich**. French uses **sous-projet** and Spanish uses **subproyecto**. The Brazilian Portuguese help keeps the English **worksets** [27][28][29][14].
  - **Worksharing** is Arbeitsteilung (DE), partage de projet (FR), uso compartido (ES), совместная работа (RU), 工作共享 (ZH), 작업 공유 (KO) and ワークシェアリング (JA).
  - **Phase** is стадия in Russian (not "фаза") and 단계 in Korean.
  - **Instance** is Exemplar (DE), ejemplar (ES) and **occurrence** (FR) in Revit usage. The French and Spanish forms were seen in training-material titles and help wording [47][48], while the German form is from my background knowledge (unverified).
  - **Family type** in Russian Revit is **типоразмер**, a word that usually means "size variant" in Russian engineering and does not exactly equal IFC "type".
- In German, **Merkmal** (attribute/characteristic) and **Eigenschaft** (property) compete. Many German BIM documents say "Merkmale" and "Merkmalgruppe" for properties/property sets, while Revit and IFC tool UIs usually say "Eigenschaften" (unverified).
- In Chinese, 属性 is used for both IFC *attribute* and IFC *property*; use 属性集 for property set and 参数 for Revit parameter.

## Typical questions people ask about this

Real questions (linked) came from Autodesk/revit-ifc issue tracker, Autodesk Community and buildingSMART forums. Their wording is paraphrased; I did not copy poster identities.

1. Why are only some Revit Levels exported as IfcBuildingStorey, e.g. only levels that host a floor? [38] (real, GitHub issue)
2. Why does Revit export storey height as "Height" when the IFC schema expects "NominalHeight"? [39] (real)
3. How do I relate IfcDoor to IfcSpace, since Revit only writes IfcRelContainedInSpatialStructure to the storey? [40] (real)
4. Why are some elements exported into the wrong storey in IFC? [41] (real, Autodesk Community)
5. How can I export an already-defined `Pset_*` property from the "IFC Parameters" group, and why does my custom IsExternal parameter not override the Pset value? [42] (real)
6. How do I validate quantities (Qto) with IDS, given that quantities are treated like properties? [43] (real, buildingSMART forum)
7. What is the difference between a Revit Room, a Revit MEP Space and an IfcSpace, and which one ends up in the IFC? (illustrative)
8. In Revit, what is the difference between a Family, a Type and an Instance, and which of them becomes IfcWallType and IfcWall? (illustrative)
9. Why do two sources translate "workset" differently (Bearbeitungsbereich, sous-projet, subproyecto)? (illustrative)
10. Is "EIR" the same as "AIA"/"発注者情報要件"/"Требования к обмену информацией"? (illustrative)
11. What is the difference between LOD and LOIN, and which does the ISO standard use now? (illustrative)
12. Is the IFC GlobalId the same as the Revit UniqueId or ElementId? (illustrative)
13. What does "Reference View" vs "Design Transfer View" mean when choosing the IFC4 export option? (illustrative)
14. How do I make a model georeferenced in IFC (IfcMapConversion and IfcProjectedCRS) rather than just shifting the Revit Survey Point? (illustrative)
15. Which Pset applies to doors: `Pset_DoorCommon`? And what is `IsExternal`? (illustrative)
16. Can an IDS file check that every IfcWall has `Pset_WallCommon.FireRating`? (illustrative)
17. Why does the same word "type" mean different things in Revit, IFC and classification systems? (illustrative)
18. Show me all "Wände / murs / стены / 墙" of one storey in the IFC. How does the MCP tool map a non-English word to IfcWall? (illustrative, multilingual test)
19. Translate this clash report from French ("conflit entre gaine et poutre") into a BCF topic title in English. (illustrative)
20. What is the difference between "federated model" and "linked model"? (illustrative)

### Illustrative multilingual prompts for MCP testers (illustrative)

| Language | Prompt | Expected IFC/Revit mapping |
|---|---|---|
| RU | «Покажи все помещения на этаже 2 и их площади» | IfcSpace on IfcBuildingStorey "2"; Qto_SpaceBaseQuantities.NetFloorArea |
| DE | „Liste alle tragenden Wände mit Feuerwiderstand" | IfcWall with Pset_WallCommon.LoadBearing = TRUE, FireRating |
| FR | « Quels sont les murs extérieurs du bâtiment ? » | IfcWall with Pset_WallCommon.IsExternal = TRUE |
| ES | «¿Cuántas puertas hay por planta?» | Count IfcDoor grouped by containing IfcBuildingStorey |
| JA | 「ファミリとタイプの違いを教えて」 | Explanation: Revit Family and Type vs IfcTypeObject |
| ZH | “把标高 1 的所有构件导出为 IFC” | Revit Level 1 elements, export to IFC4 Reference View |
| KO | “링크된 모델의 작업세트를 알려줘” | Revit Link worksets (note: worksets inside linked model) |
| AR | «كم عدد النوافذ في كل طابق؟» | Count IfcWindow by storey |
| PT | «Liste as interferências entre dutos e vigas» | Clash (IfcDuctSegment vs IfcBeam), possible BCF output |

## Common pitfalls and misconceptions

- **Revit "Type" is not always IFC "Type".** A Revit Family Type becomes an IfcXxxType (e.g. IfcWallType) only when the exporter writes type objects; system families like walls may export with type info in the name/properties only (unverified, depends on version and settings).
- **Level is not guaranteed to be Storey.** Exporter settings and level definitions (building story flag, hosting a floor) change what appears as IfcBuildingStorey [38]; the same GitHub issue shows a user losing levels that host no floor.
- **Room vs Space vs Area.** Revit Rooms and MEP Spaces both appear as IfcSpace; Revit Areas may also be exported as spaces in newer versions (unverified) [42].
- **IFC "Zone" is not a spatial structure level.** IfcZone groups spaces; Revit also has a distinct HVAC "Zone".
- **GlobalId vs Revit ids.** GlobalId is a 22-character compressed GUID [4]; Revit ElementId is an integer. Do not use ElementId as a stable key across files.
- **Property vs attribute.** Attributes are fixed by the schema (Name, Description, ObjectType, Tag); properties live in property sets. Chinese and Korean use one word for both.
- **Standard Pset names are not translated.** `Pset_WallCommon` stays in English in every language; only property labels may be localized in UI. A test expecting "Feuerwiderstand" in an IFC file will fail.
- **Custom Psets must not start with `Pset_`.** Reserved for buildingSMART standard sets [7].
- **LOD, LOI, LOG vs LOIN.** LOD (Level of Development) is US/BIMForum, while ISO 7817-1 replaces it with LOIN, which covers geometry, alphanumeric information and documentation per purpose [9]. In Chinese standards the term 模型精细度 is defined in GB/T 51301 [34].
- **EIR terminology differences.** ISO 19650 uses "exchange information requirements", older UK/HK documents use "employer's information requirements", the terms are noted as synonymous in the Hong Kong appendix [44]. German practice uses AIA / BAP [32].
- **Federation is not merging.** A federated model is a coordination view of separate discipline models; linking in Revit is a Revit-only mechanism.
- **IFC is not a lossless native file.** Round trips lose parametrics (families, constraints). Re-importing IFC into Revit gives non-parametric geometry (unverified for newest versions).
- **Localized UIs are not interchangeable.** A test script matching the English UI string "Worksets" fails on a German Revit ("Bearbeitungsbereiche") [27].
- **Arabic**: no single standard translation list found; verify against project/regional standards before using as pass/fail criteria.

## Gaps and limitations

- **buildingSMART pages returned HTTP 403** to the fetch tool (technical.buildingsmart.org terminology page and the IFC4.3 documentation index). The buildingSMART definitions above therefore come from search-result summaries of those pages [7][8], not from reading the pages themselves.
- **No Arabic-language official source** was found for Revit or ISO 19650 terminology; Arabic cells are best-effort and untagged (unverified). Searches in Arabic returned general IFC articles and a Syrian Virtual University course on BIM management, not term lists.
- **Korean**: the Korean search returned academic papers on IFC property sets [51] but no official EIR/BEP/CDE wording; the Korean process terms are unverified.
- **Chinese CDE wording**: the Chinese standards search did not show the national-standard term for CDE; "公共数据环境 / 通用数据环境" are common usage (unverified).
- **Portuguese**: Brazilian Revit help keeps "worksets" [14]; European Portuguese (AVAC, conjunto de trabalho) was not checked.
- **Russian standards**: ГОСТ Р 10.0.02-2019 is the IFC adoption, not a terminology standard [33]. Search results reported a separate terminology standard (ГОСТ Р 10.00.00.01, ">70 terms") but I did not open its text, so Russian process terms are not taken from it (unverified).
- **Localized help pages**: only the pages for linked models, shared parameters and worksets planning were fetched in the eight Revit languages. Other Revit terms (Level, Room, Sheet, Schedule, Project Base Point, etc.) are from background knowledge and unverified.
- **No suspicious or pirated sites** appeared in the results that I used. I skipped (did not open) vendor-training and e-learning shops (elephorm, quizzly, LinkedIn, Scribd) as unreliable for terminology and did not link them.

## Sources

[1] ISO 16739-1:2024 (IFC data schema): https://www.iso.org/standard/84123.html
[2] ISO 16739-1:2018: https://www.iso.org/standard/70303.html
[3] buildingSMART Technical, IFC standard page (latest 4.3.2.0): https://technical.buildingsmart.org/standards/ifc/
[4] IfcGloballyUniqueId, IFC4.3.2.0 documentation: https://standards.buildingsmart.org/IFC/RELEASE/IFC4_3/HTML/lexical/IfcGloballyUniqueId.htm
[5] IDS v1.0 approved as a Final Standard: https://www.buildingsmart.org/information-delivery-specification-ids-v1-0-is-approved-as-a-final-standard/
[6] BCF-API 3.0 final release: https://github.com/buildingSMART/BCF-API/releases/tag/v3.0
[7] buildingSMART user knowledge base, terminology (search-summary only, 403 on fetch): https://user.buildingsmart.org/knowledge-base/terminology/
[8] IfcQuantitySet (IFC4.3 documentation, search-summary only): https://standards.buildingsmart.org/IFC/DEV/IFC4_3/HTML/lexical/IfcQuantitySet.html
[9] ISO 7817-1:2024 Level of information need: https://www.iso.org/standard/82914.html
[10] Autodesk Revit help (EN), About Linked Models: https://help.autodesk.com/cloudhelp/2019/ENU/Revit-Collaborate/files/GUID-2F5D69C7-A934-481F-A0EF-D1324577F5E1.htm
[11] same page, German: https://help.autodesk.com/cloudhelp/2019/DEU/Revit-Collaborate/files/GUID-2F5D69C7-A934-481F-A0EF-D1324577F5E1.htm
[12] same page, French: https://help.autodesk.com/cloudhelp/2019/FRA/Revit-Collaborate/files/GUID-2F5D69C7-A934-481F-A0EF-D1324577F5E1.htm
[13] same page, Spanish: https://help.autodesk.com/cloudhelp/2019/ESP/Revit-Collaborate/files/GUID-2F5D69C7-A934-481F-A0EF-D1324577F5E1.htm
[14] same page, Brazilian Portuguese: https://help.autodesk.com/cloudhelp/2019/PTB/Revit-Collaborate/files/GUID-2F5D69C7-A934-481F-A0EF-D1324577F5E1.htm
[15] same page, Japanese: https://help.autodesk.com/cloudhelp/2019/JPN/Revit-Collaborate/files/GUID-2F5D69C7-A934-481F-A0EF-D1324577F5E1.htm
[16] same page, Korean: https://help.autodesk.com/cloudhelp/2019/KOR/Revit-Collaborate/files/GUID-2F5D69C7-A934-481F-A0EF-D1324577F5E1.htm
[17] same page, Russian: https://help.autodesk.com/cloudhelp/2019/RUS/Revit-Collaborate/files/GUID-2F5D69C7-A934-481F-A0EF-D1324577F5E1.htm
[18] same page, Simplified Chinese: https://help.autodesk.com/cloudhelp/2019/CHS/Revit-Collaborate/files/GUID-2F5D69C7-A934-481F-A0EF-D1324577F5E1.htm
[19] Shared parameter files, German: https://help.autodesk.com/cloudhelp/2016/DEU/Revit-Model/files/GUID-1929027A-B304-401E-BCDC-11ED3D3E67CE.htm
[20] same, French: https://help.autodesk.com/cloudhelp/2016/FRA/Revit-Model/files/GUID-1929027A-B304-401E-BCDC-11ED3D3E67CE.htm
[21] same, Spanish: https://help.autodesk.com/cloudhelp/2016/ESP/Revit-Model/files/GUID-1929027A-B304-401E-BCDC-11ED3D3E67CE.htm
[22] same, Brazilian Portuguese: https://help.autodesk.com/cloudhelp/2016/PTB/Revit-Model/files/GUID-1929027A-B304-401E-BCDC-11ED3D3E67CE.htm
[23] same, Japanese: https://help.autodesk.com/cloudhelp/2016/JPN/Revit-Model/files/GUID-1929027A-B304-401E-BCDC-11ED3D3E67CE.htm
[24] same, Korean: https://help.autodesk.com/cloudhelp/2016/KOR/Revit-Model/files/GUID-1929027A-B304-401E-BCDC-11ED3D3E67CE.htm
[25] same, Russian: https://help.autodesk.com/cloudhelp/2016/RUS/Revit-Model/files/GUID-1929027A-B304-401E-BCDC-11ED3D3E67CE.htm
[26] same, Simplified Chinese: https://help.autodesk.com/cloudhelp/2016/CHS/Revit-Model/files/GUID-1929027A-B304-401E-BCDC-11ED3D3E67CE.htm
[27] About Planning Worksets, German ("Planen von Bearbeitungsbereichen"): https://help.autodesk.com/cloudhelp/2024/DEU/Revit-Collaborate/files/GUID-6054CEF3-C4E6-4334-BA43-568DF5DF5702.htm
[28] same, French ("sous-projets"): https://help.autodesk.com/cloudhelp/2024/FRA/Revit-Collaborate/files/GUID-6054CEF3-C4E6-4334-BA43-568DF5DF5702.htm
[29] same, Spanish ("subproyectos"): https://help.autodesk.com/cloudhelp/2024/ESP/Revit-Collaborate/files/GUID-6054CEF3-C4E6-4334-BA43-568DF5DF5702.htm
[30] Revit help (EN), About Planning Worksets / Default Worksets: https://help.autodesk.com/cloudhelp/2024/ENU/Revit-Collaborate/files/GUID-6054CEF3-C4E6-4334-BA43-568DF5DF5702.htm and https://help.autodesk.com/cloudhelp/2027/ENU/Revit-Collaborate/files/GUID-559664E7-9232-448A-A5AD-60F1B4E70636.htm
[31] Wikipedia interlanguage links (MediaWiki API, `prop=langlinks`) used for general terms in all ten languages, e.g. https://en.wikipedia.org/w/api.php?action=query&titles=Column|Door|Wall&prop=langlinks&lllimit=500&format=json&redirects=1 (community source; titles are Wikipedia article titles, which can differ from professional vocabulary). Also https://fr.wikipedia.org/wiki/IFC_(format_informatique)
[32] buildingSMART Deutschland glossary table of contents (AIA, BAP, Vor-BAP), via search result: https://www.lehmanns.ch/media/948484/1
[33] ГОСТ Р 10.0.02-2019/ИСО 16739-1:2018 catalog entry: https://cn.gostinfo.ru/catalog/Details/?id=6453898
[34] GB/T 51212-2016 (China): https://www.chinesestandard.net/PDF/English_MS.aspx/GBT51212-2016 (GB/T 51301 and 51447 details are from search-result summaries of related standard pages, e.g. https://www.ttbz.org.cn/upload/file/20230630/6382374283696803072890588.pdf)
[35] Japan MLIT, BIM EIR/BEP template documents: https://www.mlit.go.jp/common/001311476.pdf and https://www.mlit.go.jp/jutakukentiku/build/content/001974590.pdf
[37] CEN/TR 17654:2021 (EIR and BEP guideline): https://evs.ee/en/cen-tr-17654-2021
[38] Autodesk/revit-ifc issue #518, levels not exported as IfcBuildingStorey: https://github.com/Autodesk/revit-ifc/issues/518
[39] Autodesk/revit-ifc issue #863, IfcBuildingStorey and IfcSpace attributes: https://github.com/Autodesk/revit-ifc/issues/863
[40] Autodesk/revit-ifc issue #91, IfcDoor to IfcSpace relation: https://github.com/Autodesk/revit-ifc/issues/91
[41] Autodesk Community, IFC export some elements in wrong storey: https://forums.autodesk.com/t5/revit-architecture-forum/ifc-export-some-elements-in-wrong-storey/td-p/9706744
[42] Autodesk Community, export already defined Pset IFC parameters: https://forums.autodesk.com/t5/revit-architecture-forum/export-already-defined-pset-ifc-parameters-under-ifc-parameters/td-p/12215203
[43] buildingSMART forum, validation of quantities using IDS: https://forums.buildingsmart.org/t/validation-of-quantities-using-ids/5326
[44] Hong Kong DEVB, ISO 19650 terminologies (EIR = employer's information requirements, synonymous): https://www.devb.gov.hk/filemanager/en/content_1287/Appendix%20I%20-%20ISO%2019650%20Terminologies%20(v2).pdf
[45] Catenda, ISO 19650 glossary (community/vendor source, not normative): https://catenda.com/glossary/iso-19650
[46] Autodesk University (FR), Revit families step by step: https://www.autodesk.com/autodesk-university/fr/article/Revit-Families-Step-Step-Introduction-2018
[47] Autodesk University (ES), same article: https://www.autodesk.com/autodesk-university/es/article/Revit-Families-Step-Step-Introduction-2018
[48] French education resource, type vs instance ("paramètres de type et d'occurrence"): https://sti.eduscol.education.fr/sites/eduscol.education.fr.sti/files/ressources/pedagogiques/9793/9793-les-parametres-de-type-et-doccurrence.pdf
[49] Autodesk Community PDF (ES), "Trabajo compartido" (subproyectos): https://forums.autodesk.com/autodesk/attachments/autodesk/317/4301/1/Trabajo%20Compartido.pdf
[50] Revit IFC manual (Autodesk Community attachment; MVD definition, mapping tables): https://forums.autodesk.com/autodesk/attachments/autodesk/311/12625/1/Revit%20IFC%20Manual%20202.0.pdf
[51] KoreaScience paper on IFC Property Set extension and compatibility: https://koreascience.kr/article/JAKO201118565337761.pdf
[52] Autodesk Revit help (EN), shared parameter files: https://help.autodesk.com/cloudhelp/2016/ENU/Revit-Model/files/GUID-1929027A-B304-401E-BCDC-11ED3D3E67CE.htm
[54] ISO/DTS 7817-2 and ISO/DIS 7817-3 (draft status when searched): https://www.iso.org/standard/89075.html and https://www.iso.org/standard/89077.html
[57] French Wikipedia, IFC (EXPRESS, ISO 10303-11): https://fr.wikipedia.org/wiki/IFC_(format_informatique)
