# Revit to IFC export, class mapping, proxies, types, families

Vocabulary topics covered: `export_revit`, `class_mapping`, `types_vs_instances`, `families_content_library`.
Data basis: research wave 1 only (`research_raw/wave1/`, no wave 2 yet). The four topics together hold 517 real records and 187 synthetic prompts (452 + 275 + 62 + 38 tagged records, with a lot of overlap). Real records are English-heavy (418 en, 41 zh, 27 ru, 10 de, 6 ja, 5 es, 5 it, 4 nl, 1 fr). About 438 distinct source URLs sit behind the 517 real records, because the same GitHub issue or forum thread was logged by several research cells. Do not read "records" as "independent people".

## In plain words

Revit keeps its own model (walls, floors, "Generic Models", families). When you export to IFC, an add-in called the IFC exporter decides, for every Revit object, which IFC class (IfcWall, IfcColumn, IfcCovering ...) to write. The default decision comes from a **category mapping table** inside the export setup; you can override it per family type or per element with the parameters **Export to IFC As** / **Export Type to IFC As** (older Revit versions used shared parameters called `IfcExportAs` / `IfcExportType`). Anything that the exporter cannot or will not classify becomes **IfcBuildingElementProxy**, the "unknown object" bucket, which is the single most common complaint in this area. Revit **types** (a family type such as "Door 900x2100") become IFC *types* and each placed copy (**instance**) becomes an IFC *occurrence*; many bugs and surprises come from which of the two carries a value. **Families** are Revit's content library objects; they matter here because nested families, in-place families and generic-model families each export differently, and because people try to bring IFC library content back into Revit as families.

Background reading: [Revit IFC export reference](../../03_software/revit/ifc_export_reference.md) (settings, mapping, override parameters), [Revit IFC import and link reference](../../03_software/revit/ifc_import_link_reference.md) (the opposite direction), [materials, classification, types, styles](../../01_ifc_basics/07_materials_classification_types_styles.md) (IFC types and ObjectType/PredefinedType), [entities cheat sheet](../../01_ifc_basics/03_entities_cheat_sheet.md), [multilingual glossary](../../08_glossary/glossary_multilingual.md) (Russian "ифс/прокси", Chinese 代理构件, etc.), and the sister document [properties and parameter mapping](properties_and_parameters.md).

Counting note: the "frequency signal" column below uses keyword matches over the real records (title, paraphrase, answer summary), so numbers are approximate and overlapping. Synthetic prompts are counted separately because they show what test authors expect, not what people asked.

## Problem map

Ranked by how often the theme shows up (real records first, synthetic as a second signal).

| # | Problem | How users describe it | Frequency signal | Root cause | Typical fix |
|---|---|---|---|---|---|
| 1 | Many objects come out as IfcBuildingElementProxy | "everything is proxy", "walls became proxy", "Zonder de correcte exportinstelling ... BuildingElementProxy", "прокси", "代理构件" | ≈54 real (46 en, 5 zh, 1 each it/nl/ru); 82 of 187 synthetic prompts, in 13 languages | Category has no mapping or is Generic Models; sub-elements (sweeps, fascias, slab edges) follow the host; wrong or lost override | Map the category, or set the type-level override; check the mapping template is the one saved in this model |
| 2 | Override parameter (IfcExportAs / Export to IFC As) "does nothing" | "IfcExportAs ignored", "Revit 2023 no longer recognizes IfcExportAs", "IfcExportAs в ФОП" | ≈44 real (36 en, 5 ru, 1 each de/it/zh) | Revit 2023 replaced the shared parameters with built-in ones; wrong level (type vs instance); schema lacks the class | Move values to the built-in "Export to IFC As"/"Export Type to IFC As"; verify with a test export |
| 3 | Some categories ignore overrides (curtain walls, wall sweeps, fascias, ceilings, assemblies, stair stringers) | "Curtain Walls doesn't obey IfcExportAs", "косоуры всё равно выгружаются", "Walls to IfcCovering" | ≈34 real (curtain 16, sweeps/fascia/ceiling/stringer 18; en, ru) | Class partly hard-coded in the exporter; sub-elements inherit the host | Model differently, use another category, or post-process the IFC; accept as a known limitation |
| 4 | Wrong or missing PredefinedType / ObjectType | "PredefinedType NOTDEFINED", "custom predefined type not exported", "ObjectType holds the type name" | ≈38 real (33 en, 4 zh, 1 nl) | Value must belong to the enum of the chosen class and schema; USERDEFINED needs a label; Revit writes the type name into ObjectType | Set the type-level predefined type; pick an IFC4 schema when the value does not exist in 2x3 |
| 5 | Elements missing from the IFC | "half the model is gone", "floors and stairs not exported", "revit导出ifc没有东西" | ≈90 broad matches (76 en, 9 zh, 3 ru, 1 de, 1 ja) | Export to IFC = No, category "Not exported", Include steel elements, view/phase filter, links not exported, exporter regression | Walk the checklist (parameter, mapping, view, phase, links, exporter version) |
| 6 | Export fails, aborts, produces an empty file or the command is greyed out | "unrecoverable error", "empty file", "没反应", "选项是灰的" | ≈46 real (42 en, 4 zh); synthetic prompts in ko, ru, zh | Add-in conflicts, exporter regression, language/encoding issue, write-permission check, missing exporter add-in | Roll back or update the exporter, disable other add-ins, export locally, export per view |
| 7 | Type properties and type objects behave oddly | "type parameters missing", "changing one door type changes the other", "10 instances became 3 IFC types" | 46 real tagged `types_vs_instances` (≈40 en; de, ru, ja, nl one or two each) | Exporter only writes type psets when asked; psets are shared between types; IFC type generation depends on class | Declare the type class in the pset file; tick "Allow use of type properties in instance property sets"; check which level a value lives on |
| 8 | Families: nested, in-place, parts, library content | "nested shared family exports as separate objects", "avoid in-place families", "IFC walls with windows have no system family" | 36 real tagged `families_content_library` (≈28 en, 3 ru, 2 zh, 1 each ja/nl/pt-BR) | Nested families have no parent relation in IFC; in-place and parts lose data; imported content becomes DirectShape or Imported Symbol | Keep families flat and categorized; avoid in-place; use Link IFC for reference only |
| 9 | Mapping table management | "mapping is inside the model", "'Not exported' string in my language", "mix of IFC2x3 and 4.3 classes" | ≈10 real (revit-ifc #840, #859, #876, #775, #201, zh/it how-tos) | Mapping lives in the model (DataStorage); localized strings and encodings break import of the txt; no schema binding | Keep one template per schema; export/import the txt; check locale |
| 10 | Which IFC class for MEP, structural, site, civil items | "best class for a reducing coupling", "ducts and pipes show as generic", "road model all proxy" | ≈38 MEP + ≈29 structural keyword matches; mostly en | No obvious class in the schema or version too old (IfcFlowSegment in 2x3, IfcDuctSegment from IFC4) | Use the closest class + predefined type (e.g. TRANSITION); use IFC4 or 4.3; ask the community/standard owner |
| 11 | Which IFC version and view (2x3 CV2.0, IFC4 RV, DTV, 4.3) to export | "2x3 or 4?", "what is Coordination View 2.0", "DTV experiences?" | ≈70 broad matches (64 en, 3 it); synthetic prompts in ru, ko, pt-BR, es, no, en | Class and predefined-type availability, material and geometry handling differ by schema/view; requirements often unstated | Ask the receiver's requirement (EIR/BEP); default to what the receiver's checker accepts |
| 12 | Opposite direction: IFC arrives as Generic Models or dumb solids in Revit | "my IFC walls are just generic models", "элементы приходят как тела", "Imported Symbol" | ≈50 broad matches (41 en, 4 ru, 2 zh); 22 records also tagged `import_into_revit` | Link IFC makes DirectShapes; Open IFC logic is largely closed; import class mapping table is limited | Load an import mapping file before opening; use Link for reference; remodel natively |
| 13 | Expectation gap: "IFC should be lossless" | "Die Wunderwaffe IFC", "при каждой конвертации теряются данные", "Revit导出IFC会丢哪些信息" | ≈10 real across de, ru, zh, it, ja | IFC carries semantics, not parametric intelligence; each tool has its own mapping | Define purpose first; keep native files for editing; use IFC for exchange and checks |

## Problems in depth

### 1. Everything becomes IfcBuildingElementProxy

**Symptoms in users' words**
- en: "No way to override the IFC class of wall sweeps; they always export as proxy" [revit-ifc #229](https://github.com/Autodesk/revit-ifc/issues/229). "Security devices export as proxies while electrical equipment exports correctly" [forums.autodesk.com](https://forums.autodesk.com/t5/revit-mep-forum/ifc-export-issue/m-p/12250648).
- it: *"i muri sono finiti come proxy, come faccio senza rompere i GUID?"* (walls ended up as proxy, how do I fix without breaking GUIDs?) [biblus.acca.it](https://biblus.acca.it/problemi-editing-file-ifc/).
- nl: *"Zonder de correcte exportinstelling wordt een element vaak een BuildingElementProxy"* (without the right export setting an element often becomes a proxy), from a national guideline [digigo.nu](https://www.digigo.nu/ilsen-en-richtlijnen/bim-basis-ils/3-4-correct-gebruik-entiteiten).
- zh: *"IfcBuildingElementProxy是什么"* (what is IfcBuildingElementProxy) [cnblogs.com](https://www.cnblogs.com/herd/p/15765322.html).
- ru: a forum voice calls Proxy a crutch (*"это костыль, нужен ручной маппинг"*) [habr.com](https://habr.com/ru/articles/590819/comments/).

**Why it happens.** Proxy is the schema's "object without a specific class" bucket; a developer reading the file cannot tell what a proxy really is without vendor knowledge [forums.buildingsmart.org](https://forums.buildingsmart.org/t/5130). In Revit the usual sources are Generic Models, categories mapped to nothing, and sub-elements that follow their host (see problem 3). A model can also contain legitimate proxies (a community answer suggests a proxy with predefined type PROVISIONFORVOID for void requests [forums.buildingsmart.org](https://forums.buildingsmart.org/t/what-is-the-right-ifc-entity-for-water-outlet-into-a-structural-ifc-model/1410)), so "zero proxies" is not always the right target.

**What fixes it.** Set the category in the mapping table, or set "Export Type to IFC As" on the family type (instance override wins over type, see [export reference section 5-6](../../03_software/revit/ifc_export_reference.md)). After export, check the result in the file, not in the dialog. An IFC-side clean-up with a script is possible but does not recreate the standard psets or quantities of the new class (see problem 3 for the quantity example).

**What a good AI/MCP assistant should do.** Count proxies, group them by type name and name pattern, and say clearly that the Revit category is usually *not* stored in the IFC (the IFC Name often looks like `Family:Type:ElementId`, see [cnblogs.com](https://www.cnblogs.com/herd/p/14908387.html)); it is only recoverable if Revit property sets were exported. Propose a mapping, show a dry-run list, and only then change anything.
**Clarifying questions.** Is the IFC from Revit or another tool (check the header application)? Do you want the source Revit model fixed or only the IFC file? What does the receiver accept (a percentage limit, an IDS)? Which IFC schema?

### 2. IfcExportAs / Export to IFC As is ignored (Revit 2023 change)

**Symptoms in users' words**
- en: "Since Revit 2023 new built-in IFC parameters exist and the old IfcExportAs is ignored; instance IfcExportAs in groups and key schedules workflow break" [revit-ifc #541](https://github.com/Autodesk/revit-ifc/issues/541). "During QA in Solibri none of the objects carry the values from IfcExportAs/IfcExportType after moving to Revit 2023.1" [revit-ifc #614](https://github.com/Autodesk/revit-ifc/issues/614).
- ru: *"в 2022 и старше только IfcExportAs"*; the author says the category-to-class table "lies" and the class really comes from export parameters [habr.com](https://habr.com/ru/articles/1089018/).
- en (2017 forum): values typed into IFCExportAs/IFCExportType on a family, output still proxy [forums.autodesk.com](https://forums.autodesk.com/t5/revit-architecture-forum/ifc-parameters-ifcexportas-and-ifcexporttype-not-outputting-to/td-p/7511389).

**Why it happens.** From Revit 2023 the exporter reads built-in parameters ("Export to IFC As", "Export Type to IFC As", plus predefined-type parameters) and no longer the old shared `IfcExportAs`/`IfcExportType`; a maintainer said the old ones were dropped for performance and old files should be upgraded by moving the values [revit-ifc #614](https://github.com/Autodesk/revit-ifc/issues/614) (open internal item REVIT-240196 [revit-ifc #541](https://github.com/Autodesk/revit-ifc/issues/541)). In older versions the shared parameters took precedence over the category mapping [forums.autodesk.com](https://forums.autodesk.com/t5/revit-architecture-forum/mapping-of-revit-parameters-to-ifc-parameters-for-export/td-p/7638232). Other causes in old threads: parameter bound to the wrong level (type vs instance), misspelled name, a class that the chosen schema does not have [forums.autodesk.com](https://forums.autodesk.com/t5/revit-architecture-forum/ifc-parameters-ifcexportas-and-ifcexporttype-not-outputting-to/td-p/7511389). The shared parameter is also not exported as a normal pset because the "IFC Parameters" group is excluded [revit-ifc #392](https://github.com/Autodesk/revit-ifc/issues/392).

**What fixes it.** Copy old values into the built-in parameters; scripts can set the type-level one through `BuiltInParameter.IFC_EXPORT_ELEMENT_TYPE_AS` [forum.dynamobim.com](https://forum.dynamobim.com/t/set-export-type-to-ifc-as-parameter/110128). Re-export and verify in the IFC.

**What a good AI/MCP assistant should do.** Read both the old shared parameter and the new built-in one, report per element which class it *should* get and which class the exported IFC actually has, and explain the precedence (instance beats type).
**Clarifying questions.** Revit year and IFC exporter add-in version? Was the project upgraded from 2022 or older? Is the value on the type or the instance? Is the target class valid in the chosen IFC schema?

### 3. Categories that ignore the override (curtain walls, sweeps, fascias, ceilings, assemblies, stair stringers)

**Symptoms in users' words**
- en: "Curtain wall ignores IfcExportAs; BIM manager wants all subparts as IfcCurtainWall" [revit-ifc #171](https://github.com/Autodesk/revit-ifc/issues/171). "Walls export as IfcWallStandardCase regardless of IFCExportType ... works for ceilings and floors but not walls or curtain walls" [revit-ifc #155](https://github.com/Autodesk/revit-ifc/issues/155). "Assemblies given IfcExportAs on type work (e.g. IfcStair) except structural column/framing assemblies" [revit-ifc #213](https://github.com/Autodesk/revit-ifc/issues/213).
- ru: *"косоуры выгружаются при Нет"* (stringers are exported although the parameter says No) [habr.com](https://habr.com/ru/articles/1098340/); also ramps leave as IfcRampFlight and room codes are filled by hand [habr.com](https://habr.com/ru/articles/1098340/).
- en: wall sweeps should be IfcCovering but arrive as proxy [forums.autodesk.com](https://forums.autodesk.com/t5/revit-architecture-forum/the-ifc-class-is-not-exported-correctly-to-the-ifc-model/td-p/11629864); fascias and sweeps cannot override the class [revit-ifc #481](https://github.com/Autodesk/revit-ifc/issues/481).
- zh: *"类别对不上IFC类、坐标转换没了"* (categories do not match IFC classes, the coordinate transform is lost) [bbs.co188.com](https://bbs.co188.com/thread-10112116-1-1.html).

**Why it happens.** For some categories the exporter fixes the structure itself: a curtain wall becomes an IfcCurtainWall container with IfcMember mullions and IfcPlate panels [revit-ifc #171](https://github.com/Autodesk/revit-ifc/issues/171); sub-elements follow the host. Status changes between versions: ceilings were reported as hard-coded to CEILING, later Autodesk said the override works in 2023-2026 and could not reproduce [revit-ifc #475](https://github.com/Autodesk/revit-ifc/issues/475). Quantities may also ignore the new class (a wall forced to IfcFurniture still gets `Qto_WallBaseQuantities`) [revit-ifc #497](https://github.com/Autodesk/revit-ifc/issues/497).

**What fixes it.** Accept the limitation, change how it is modelled (another category, a generic model), or reclassify after export. For a glass partition the community answer was to choose by context: use IfcWall, not IfcCurtainWall [forums.buildingsmart.org](https://forums.buildingsmart.org/t/6609).

**What a good AI/MCP assistant should do.** Not promise that every override works. Test with one element and a real export, list which categories honored the override, and mention the version dependency.
**Clarifying questions.** Which category and Revit/exporter version? Is the element a system family, a loadable family or a sub-element? Is the aim a specific class or just "not a proxy"?

### 4. PredefinedType and ObjectType go wrong

**Symptoms in users' words**
- en: custom stair type cannot be forced; always STRAIGHT_RUN_STAIR [revit-ifc #684](https://github.com/Autodesk/revit-ifc/issues/684). IfcFlowMeterType + WATERMETER gets the class but PredefinedType NOTDEFINED [revit-ifc #525](https://github.com/Autodesk/revit-ifc/issues/525). "Revit puts the type name in ObjectType, so IFC beginners think it is the IFC type name" [revit-ifc #502](https://github.com/Autodesk/revit-ifc/issues/502).
- en: IfcSpace predefined type not exported; closed as by design because IFC2x3 space enum only has USERDEFINED/NOTDEFINED [revit-ifc #247](https://github.com/Autodesk/revit-ifc/issues/247).
- nl: guideline text says use the TypeEnumeration and NOTDEFINED when you do not choose; some values exist only in IFC4 [digigo.nu](https://www.digigo.nu/ilsen-en-richtlijnen/bim-basis-ils/3-4-correct-gebruik-entiteiten).

**Why it happens.** The predefined type must be a value of the chosen class' enumeration in the chosen schema; USERDEFINED additionally needs a label in `ObjectType` (occurrence) or `ElementType` (type), see [IFC types](../../01_ifc_basics/07_materials_classification_types_styles.md). Revit often fills ObjectType with the family/type name even when the predefined type is not USERDEFINED. A file where both the occurrence and its type carry a PredefinedType is invalid per the schema rule, and IDS only checks valid files [forums.buildingsmart.org](https://forums.buildingsmart.org/t/the-predefinedtype-shall-only-be-used/6180).

**What fixes it.** Set the predefined-type parameter on the type; pick IFC4 or later when the value is missing in 2x3; check the exported attribute.

**What a good AI/MCP assistant should do.** Show `PredefinedType` on the occurrence *and* on the type, flag both-set conflicts and NOTDEFINED/empty values, and explain that ObjectType is not "the IFC type".
**Clarifying questions.** Which schema? Is the value in that schema's enumeration? Do you need a standard value or a company-specific label (USERDEFINED)?

### 5. Elements are missing from the exported IFC

**Symptoms in users' words**
- ja: *"IFCに書き出したらモデルの半分が消えていた"* (half the model vanished when I exported to IFC); causes named: plain solids, layers not tied to a storey, hidden elements [note.com](https://note.com/toshio_nakamura/n/nc8db42ce3191).
- en: floors and stairs vanish when Export to IFC is "By Type" [forums.autodesk.com](https://forums.autodesk.com/t5/revit-architecture-forum/revit-2023-ifc-export-issue-floors-stair-was-not-exported-export/td-p/11530572); "Floors not exporting" fixed by changing the Windows language [revit-ifc #759](https://github.com/Autodesk/revit-ifc/issues/759); beams and columns "vanish", cause was the "Include steel elements" option [revit-ifc #952](https://github.com/Autodesk/revit-ifc/issues/952).
- zh: *"revit导出ifc没有东西"* (the exported IFC has nothing in it) [blog.csdn.net](https://blog.csdn.net/d001014/article/details/140438872).
- ru: after export part of the elements and parameters were lost, *"как проверить где проблема - в экспорте или в просмотрщике"* (how to tell whether the problem is the export or the viewer) [forum.dwg.ru](https://forum.dwg.ru/showthread.php?t=154396).

**Why it happens.** The usual suspects: Export to IFC = No/By Type, category mapped to "Not exported", "Include steel elements", export of only visible elements or the wrong phase, links not exported, an exporter regression (steel connections disappeared in 25.4.3.0, fixed in 25.4.40.0 [revit-ifc #890](https://github.com/Autodesk/revit-ifc/issues/890)), or a mapping text file read in the wrong encoding on a non-English system [revit-ifc #759](https://github.com/Autodesk/revit-ifc/issues/759). Linked models are not merged into one IFC by default [revit-ifc #439](https://github.com/Autodesk/revit-ifc/issues/439).

**What fixes it.** Check, in order: the per-element/per-type parameter, the category row in the mapping table, "Export only elements visible in view", phase and filter, links (separate IFC option), exporter version.

**What a good AI/MCP assistant should do.** Compare element counts per category in Revit with IFC class counts, then name the likely filter. In an IFC-only context it can only report what *is* there and say what it cannot know.
**Clarifying questions.** Which view/phase was exported? Were links expected inside the same file? Which exporter version? Does a viewer or the file itself lack the objects?

### 6. Export aborts, returns an empty file, or the command is greyed out

**Symptoms in users' words**
- en: exporter 26.4.0/26.4.1 aborts with the "unrecoverable error" dialog on a workshared cloud model, 26.1.0.23 was fine [revit-ifc #1021](https://github.com/Autodesk/revit-ifc/issues/1021). Built-in and GitHub exporters all fail on tiny models, "2020 worked" [revit-ifc #590](https://github.com/Autodesk/revit-ifc/issues/590).
- zh: *"revit2019点击导出IFC后没反应，导出位置只有一个schema文档"* (nothing happens on export, only a schema document appears) [zhihu.com](https://www.zhihu.com/question/455661969); *"Revit2020导出IFC选项是灰的"* (the IFC export option is greyed out) [zhuanlan.zhihu.com](https://zhuanlan.zhihu.com/p/611709017).
- en: crash after an update, solved by removing a conflicting add-in [forums.autodesk.com](https://forums.autodesk.com/t5/revit-architecture-forum/revit-2024-3-update-revit-crashes-every-time-i-export-ifc/td-p/13030432); empty IFC from an API/Dynamo script [forum.dynamobim.com](https://forum.dynamobim.com/t/ifc-export-node-return-an-empty-ifc/82822).

**Why it happens.** Reported causes: older Enscape versions blocking export [revit-ifc #590](https://github.com/Autodesk/revit-ifc/issues/590), a second IFC add-in installed, interface-language change [revit-ifc #718](https://github.com/Autodesk/revit-ifc/issues/718), exporter regressions fixed by rolling back [revit-ifc #583](https://github.com/Autodesk/revit-ifc/issues/583), a missing or outdated IFC exporter add-in on older Revit versions (the Chinese answers say to install it and update Revit), and for scripts a missing transaction or view id [forum.dynamobim.com](https://forum.dynamobim.com/t/ifc-export-node-return-an-empty-ifc/82822). Curtain-wall access violations are tracked separately [revit-ifc #992](https://github.com/Autodesk/revit-ifc/issues/992).

**What fixes it.** Update or roll back the exporter, remove other IFC add-ins, export to a local drive, try per-view export, and send the maintainers a sample file and journal.

**What a good AI/MCP assistant should do.** Ask for the exact message and versions, avoid guessing model corruption, offer a short ordered checklist, and for scripted exports check the transaction and view setup.
**Clarifying questions.** Exact dialog text? Revit and exporter versions? Local or network/cloud file? Which other add-ins? Does a small test model export?

### 7. Type vs instance: missing type properties, shared psets, duplicate types

**Symptoms in users' words**
- de: *"Revit Typenparameter nach IFC exportieren"*: type parameters disappeared after an exporter update although the user-defined pset file worked before [bim-me-up.com](https://bim-me-up.com/revit-typenparameter-nach-ifc-exportieren/).
- en: "type parameters missing in IFC property sets after export" and the answer: tick "Allow use of type properties in instance property sets" [forums.autodesk.com](https://forums.autodesk.com/t5/revit-architecture-forum/issues-with-exporting-type-parameters-from-revit-to-ifc/td-p/14004505).
- en: editing IsExternal on one door type changes the other, because Revit reuses single-value entities to keep files small [community.osarch.org](https://community.osarch.org/discussion/1753/bbim-two-door-types-with-connected-properties), [IfcOpenShell #3957](https://github.com/IfcOpenShell/IfcOpenShell/issues/3957).
- en: "One alarm type with 10 instances exports as 3 IFC types" [revit-ifc #809](https://github.com/Autodesk/revit-ifc/issues/809); hundreds of auto-generated proxy types that cannot be edited [revit-ifc #676](https://github.com/Autodesk/revit-ifc/issues/676).
- en: ClassificationCode[Type] lands on the occurrences, not the IfcWallType [revit-ifc #691](https://github.com/Autodesk/revit-ifc/issues/691); LoadBearing "is an entity-level instance property so a type parameter is ignored" [revit-ifc #833](https://github.com/Autodesk/revit-ifc/issues/833).

**Why it happens.** In IFC the effective value is the union of type and occurrence properties; the occurrence wins per property (see [properties doc](../../01_ifc_basics/05_properties_quantities_psets.md), section 2). The Revit exporter writes type-level psets only when the type class is listed in the user-defined file and, in newer exporters, type-level `IsExternal` support was removed (same doc). Work on consistent type GUIDs shipped in Revit 2023.1 [revit-ifc #512](https://github.com/Autodesk/revit-ifc/issues/512).

**What fixes it.** List the type class (IfcWallType, IfcElementType) next to the instance class in the pset file, tick the type-in-instance option when an instance-level pset is wanted, keep decisions per property ("varies per instance? then instance").

**What a good AI/MCP assistant should do.** Always say which level a value came from; before editing a type or a shared property entity, warn that other types or all occurrences change; offer an occurrence-level override.
**Clarifying questions.** Should this value be identical for every element of the type? Is the property entity shared? Which exporter version?

### 8. Families: nested, in-place, parts and library content

**Symptoms in users' words**
- en: "Nested shared families export as separate objects with no relation to parent (e.g. door leaf, frame, closer)" [revit-ifc #374](https://github.com/Autodesk/revit-ifc/issues/374). Parts miss IsExternal, FireRating and type name from the host [revit-ifc #120](https://github.com/Autodesk/revit-ifc/issues/120). A family with several material layers outputs only one layer [revit-ifc #929](https://github.com/Autodesk/revit-ifc/issues/929).
- es: a tips article says "avoid in-place families" and put IFC parameters into templates [bimnd.es](https://www.bimnd.es/blog/10-consejos-para-exportar-un-buen-ifc-con-revit/).
- ru: *"можно ли редактировать семейство из IFC в Ревите"* (can I edit a family that came from IFC in Revit?), answer: IFC is an exchange format, not editable [forum.dwg.ru](https://forum.dwg.ru/showthread.php?t=130296&page=2).
- en: walls with windows imported from IFC have "family Imported Symbol" and cannot be modified [revit-ifc #729](https://github.com/Autodesk/revit-ifc/issues/729); MEP types imported from a library lose ports [IfcOpenShell #6687](https://github.com/IfcOpenShell/IfcOpenShell/issues/6687).
- en (MCP-flavoured): a Revit MCP tool placing a hosted door ignored the host and position until `host_id` became mandatory [rvt-mcp #13](https://github.com/bimwright/rvt-mcp/issues/13).

**Why it happens.** IFC has aggregation but Revit's nested families do not automatically become a parent/child structure; in-place families and Parts are special categories; imported IFC content becomes DirectShape/Imported Symbol, not parametric families ([import reference](../../03_software/revit/ifc_import_link_reference.md), section 7).

**What fixes it.** Flat, categorized loadable families; no in-place families for exported content; model over a Link IFC underlay when native elements are needed; copy values from the host to parts by script.

**What a good AI/MCP assistant should do.** Distinguish "family type" from "placed instance", say what survives in IFC, never promise to turn IFC objects back into parametric families, and read back after placing a family (position, host, level).
**Clarifying questions.** Loadable, in-place, nested or system family? Is the goal exchange, checking or re-use inside Revit?

### 9. Mapping table management

**Symptoms in users' words**
- en: "Class mapping now stored in a DataStorage object inside each model; doesn't scale across many models" [revit-ifc #840](https://github.com/Autodesk/revit-ifc/issues/840); the table "lets users mix IFC2x3 and IFC4.3 classes regardless of target schema" [revit-ifc #876](https://github.com/Autodesk/revit-ifc/issues/876); "What is the purpose of subcategory-level class mapping?" [revit-ifc #775](https://github.com/Autodesk/revit-ifc/issues/775); importing the txt with a localized "Not exported" string no longer works [revit-ifc #859](https://github.com/Autodesk/revit-ifc/issues/859).
- zh: *"需要导出的构件在exportlayers-ifc-IAI里找不到对应类别，怎么改导出选项"* (the category I need is not in exportlayers-ifc-IAI, how do I change the export options) [zhihu.com](https://www.zhihu.com/question/418802002); a tutorial shows the mapping table saved as txt and shared [zhuanlan.zhihu.com](https://zhuanlan.zhihu.com/p/649792298).
- en: a script-driven export ignores the mapping options of the normal export [forum.dynamobim.com](https://forum.dynamobim.com/t/ifc-export-does-not-respect-mapping/112777).

**Why it happens.** The setup (including the mapping template name) lives in the model, so another model or machine can differ ([export reference section 4](../../03_software/revit/ifc_export_reference.md)); in multi-model export only the model that holds the mapping applies it [revit-ifc #840](https://github.com/Autodesk/revit-ifc/issues/840). Revit converts IFC4.3-only classes to the nearest class when exporting 2x3 [revit-ifc #876](https://github.com/Autodesk/revit-ifc/issues/876).

**What fixes it.** One template per schema, export the txt and import it into other models, check locale/encoding, and for scripts start from a saved configuration.

**What a good AI/MCP assistant should do.** Show which mapping template and setup name are active, compare two setups, warn when a class is not valid for the schema.
**Clarifying questions.** Which setup is active? Same template in all linked models? Which schema and locale?

### 10. Which IFC class for MEP, structural, site and civil items

**Symptoms in users' words**
- en: "Best IFC classification for a reducing coupling" (answer: TRANSITION) [forums.buildingsmart.org](https://forums.buildingsmart.org/t/best-ifc-classification-for-a-reducing-coupling/5963); ducts and pipes show as generic types [forums.autodesk.com](https://forums.autodesk.com/t5/revit-mep-forum/ifc-export-ducts-and-pipes/td-p/12370919) (in 2x3 only IfcFlowSegment exists; IfcDuctSegment/IfcPipeSegment arrive with IFC4); equipment in one Revit category must become different classes [bimcorner.com](https://bimcorner.com/exporting-ifc-from-revit-part-1-mapping/).
- en: site coverage and site boundary came out as IfcSpace but IFC+SG wants IfcGeographicElement [github.com](https://github.com/noddlesskcho/ifc-sg-site-object-repair); area plans exported as IfcSpace ("IfcSpace is default/recommended") [revit-ifc #671](https://github.com/Autodesk/revit-ifc/issues/671); a Civil 3D road model arrives as proxies [forums.autodesk.com](https://forums.autodesk.com/t5/civil-3d-forum/ifc-exporting-road-model/td-p/12923665).
- es: a thesis researcher exporting a structural model to ETABS gets an error in the target program [forums.buildingsmart.org](https://forums.buildingsmart.org/t/como-poder-exportar-un-modelo-3d-estructural-realizado-en-revit-a-etabs-por-medio-del-formato-ifc/2985).

**Why it happens.** The schema may simply not have an obvious class, the schema version may be too old, or the Revit category covers several real-world things.

**What fixes it.** Use the closest class plus a predefined type or USERDEFINED + ObjectType, use IFC4/4.3 where the class exists, and follow the receiving standard (for example a national site rule).

**What a good AI/MCP assistant should do.** Propose a class with the reason and a fallback, and note the schema version; never present a guess as the official mapping.
**Clarifying questions.** Which IFC schema? Which discipline and receiving software? Is there a national or project rule?

### 11. Which IFC version and view to export (2x3 CV2.0, IFC4 RV, DTV, IFC4.3)

**Symptoms in users' words**
- it: *"cos'e la Coordination View 2.0 e quando usarla?"* [biblus.acca.it](https://biblus.acca.it/ifc-2x3-coordination-view-2-0/).
- en: "IFC4 Design Transfer View experiences?" Answer: DTV was never finalized, Revit's DTV is CV2.0 plus advanced BReps, now marked unofficial; RV 1.2 is the most common [forums.buildingsmart.org](https://forums.buildingsmart.org/t/ifc4-design-transfer-view-experiences/4362).
- en: IFC4x3 Reference View writes `CoordinationView` in the header [revit-ifc #1013](https://github.com/Autodesk/revit-ifc/issues/1013); space boundaries wrong under IFC4x3 but fine in IFC4 Reference View [forums.autodesk.com](https://forums.autodesk.com/t5/revit-architecture-forum/revit-ifc4x3-export-incorrect-space-boundaries/m-p/14048745).
- ru: a Russian forum post notes the default is RV 1.2, not meant for editing [blog.rengabim.com](https://blog.rengabim.com/2021/08/ifc.html).

**Why it happens.** Class and predefined-type availability, material handling and geometry type (for example IfcAdvancedBrep) differ by schema and view [revit-ifc #480](https://github.com/Autodesk/revit-ifc/issues/480); the receiver's requirement is often not stated.

**What fixes it.** Ask for the requirement (EIR/BEP/expert review). The exporter's own code default is IFC2x3 Coordination View 2.0, but that is a tool default, not a recommendation; confirm with the receiver (see [export reference section 3](../../03_software/revit/ifc_export_reference.md)).

**What a good AI/MCP assistant should do.** Present options with consequences instead of picking silently; read `FILE_SCHEMA` and `FILE_DESCRIPTION` of an existing file to say what it already is.
**Clarifying questions.** Who receives the file and what checker do they run? Do they need to edit it? Which Revit year and exporter version?

### 12. The opposite direction: IFC comes into Revit as Generic Models, solids or Imported Symbols

**Symptoms in users' words**
- en: "After importing an IFC all walls are just Generic Models; how to make Revit recognise walls?" [revit-ifc #571](https://github.com/Autodesk/revit-ifc/issues/571); the maintainers ask for version, Link vs Open and a sample.
- ru: *"элементы приходят как тела, а не как родные объекты Ревита, хочу их редактировать"* [forum.dwg.ru](https://forum.dwg.ru/showthread.php?t=166052); ArchiCAD to Revit: *"стёкла жёлтые и толщиной в метры, часть перегородок пропала"* [forum.dwg.ru](https://forum.dwg.ru/showthread.php?t=154396).
- it: *"come carico il file di mappatura classi IFC in Revit prima di aprire l'IFC cosi le porte restano porte?"* [biblus.acca.it](https://biblus.acca.it/ifc-class-mapping-file/).

**Why it happens.** Link IFC converts everything to DirectShapes; Open IFC logic is largely closed [revit-ifc #223](https://github.com/Autodesk/revit-ifc/issues/223); no single official document defines the import mapping [revit-ifc #778](https://github.com/Autodesk/revit-ifc/issues/778). See the [import reference](../../03_software/revit/ifc_import_link_reference.md).

**What fixes it.** Choose Link or Open deliberately, set the import class mapping before opening, accept that the result is a reference, not an editable model.

**What a good AI/MCP assistant should do.** Explain Link vs Open before acting, state that native parametric families are not recreated, and offer to list what the file contains by class.
**Clarifying questions.** Link or Open? Which source application? Is editing really required?

### 13. Expectation gap: "IFC should be lossless"

**Symptoms in users' words**
- de: *"Die Wunderwaffe IFC"*: the partner imports my IFC and windows and walls arrive as plain dumb objects [bim-me-up.com](https://bim-me-up.com/die-wunderwaffe-ifc/).
- ru: *"при каждой конвертации в IFC и обратно теряются данные, элементы возвращаются мёртвой геометрией"* [sapr.ru](https://sapr.ru/article/24777).
- zh: *"Revit导出IFC会丢哪些信息，共享参数、材质、族参数"* (what information does Revit lose when exporting IFC: shared parameters, materials, family parameters) [blog.csdn.net](https://blog.csdn.net/weixin_39590472/article/details/112503752).
- it: *"cosa si perde esportando da Revit in IFC? le famiglie e le relazioni vengono mappate bene?"* [biblus.acca.it](https://biblus.acca.it/ifc-vs-rvt-quali-sono-le-principali-differenze-tra-revit-e-ifc-in-termini-di-interoperabilita-e-scambio-dati/).
- ja: *"IFCにすれば別ソフトで編集を続けられると思われがち"* (people assume IFC lets them keep editing in another tool) [note.com](https://note.com/onestruction/n/ne8322e3be44d).

**Why it happens.** IFC records classes, geometry, properties and relations, not the authoring tool's parametric rules or families; every tool maps in its own way.

**What fixes it.** State the purpose of the exchange (view, check, quantity, handover), keep native files for editing, and test one round trip on a small sample.

**What a good AI/MCP assistant should do.** Explain what IFC will and will not carry in plain words, and offer a loss report (what exists in source categories vs IFC classes) rather than a promise.
**Clarifying questions.** What does the receiver need to do with the file? Is a round trip required?

## Real questions

Language is the language of the original post. English rows are my paraphrase of the stored paraphrase; for other languages the question is the stored original-language paraphrase, except rows marked † where the stored paraphrase was in English and I show the original thread title instead. Each row links to the source.

| lang | question (original-language paraphrase) | EN gloss | persona | source |
|---|---|---|---|---|
| en | Wall sweeps always export as IfcBuildingElementProxy, and I can't override the IFC class. | — | bim coordinator | [revit-ifc #229](https://github.com/Autodesk/revit-ifc/issues/229) |
| en | Slab edges still export as IfcBuildingElementProxy although I added an IfcExportAs parameter set to IfcSlab. | — | structural engineer | [forums.autodesk.com](https://forums.autodesk.com/t5/revit-structure-forum/ifcexportas-parameter-doesn-t-work/td-p/8219179) |
| en | Security devices export as proxies while electrical equipment exports correctly. | — | mep engineer | [forums.autodesk.com](https://forums.autodesk.com/t5/revit-mep-forum/ifc-export-issue/m-p/12250648) |
| en | I typed values into IFCExportAs/IFCExportType on the family but the IFC still says IfcBuildingElementProxy. | — | bim coordinator | [forums.autodesk.com](https://forums.autodesk.com/t5/revit-architecture-forum/ifc-parameters-ifcexportas-and-ifcexporttype-not-outputting-to/td-p/7511389) |
| en | Since Revit 2023 the old IfcExportAs is ignored; our groups and key-schedule workflow broke. | — | bim manager | [revit-ifc #541](https://github.com/Autodesk/revit-ifc/issues/541) |
| en | In Solibri none of the objects carry the IfcExportAs/IfcExportType values after moving to Revit 2023.1. | — | bim coordinator | [revit-ifc #614](https://github.com/Autodesk/revit-ifc/issues/614) |
| en | Curtain walls don't obey IfcExportAs; I want all subparts as IfcCurtainWall. | — | bim manager | [revit-ifc #171](https://github.com/Autodesk/revit-ifc/issues/171) |
| en | Walls come out as IfcWallStandardCase whatever IfcExportType says; I want IfcCovering. | — | architect | [revit-ifc #155](https://github.com/Autodesk/revit-ifc/issues/155) |
| en | Assemblies with an IfcExportAs on the type export fine, but structural column assemblies won't become IfcColumn. | — | structural engineer | [revit-ifc #213](https://github.com/Autodesk/revit-ifc/issues/213) |
| en | How can I export a custom predefined type for a stair? IfcExportAs/IfcExportType does nothing. | — | architect | [revit-ifc #684](https://github.com/Autodesk/revit-ifc/issues/684) |
| en | IfcExportAs=IfcFlowMeterType and IfcExportType=WATERMETER give the class but PredefinedType NOTDEFINED. | — | mep engineer | [revit-ifc #525](https://github.com/Autodesk/revit-ifc/issues/525) |
| en | A wall overridden to IfcFurniture still gets Qto_WallBaseQuantities. | — | estimator qs | [revit-ifc #497](https://github.com/Autodesk/revit-ifc/issues/497) |
| en | Eight convoluted rules decide the IFC class; consultants deliver wrong classes despite instructions. I want the IfcExportAs value visible in the IFC. | — | bim manager | [revit-ifc #392](https://github.com/Autodesk/revit-ifc/issues/392) |
| en | What is subcategory-level class mapping for? It seems to have no effect. | — | bim manager | [revit-ifc #775](https://github.com/Autodesk/revit-ifc/issues/775) |
| en | Can the class mapping be referenced from an external file instead of living in every model? | — | bim manager | [revit-ifc #840](https://github.com/Autodesk/revit-ifc/issues/840) |
| en | Floors and stairs vanish when Export to IFC is "By Type". | — | structural engineer | [forums.autodesk.com](https://forums.autodesk.com/t5/revit-architecture-forum/revit-2023-ifc-export-issue-floors-stair-was-not-exported-export/td-p/11530572) |
| en | Is it possible to exclude Areas from the IFC export? | — | architect | [forums.autodesk.com](https://forums.autodesk.com/t5/revit-architecture-forum/is-it-possible-to-exclude-areas-from-ifc-export/td-p/9513180) |
| en | Floors, roofs, slabs and stairs are dropped; only 1 of 7 PCs exports them. | — | bim manager | [revit-ifc #759](https://github.com/Autodesk/revit-ifc/issues/759) |
| en | Exporter 26.4 aborts with the unrecoverable error dialog; 26.1.0.23 worked fine. | — | bim coordinator | [revit-ifc #1021](https://github.com/Autodesk/revit-ifc/issues/1021) |
| en | Built-in and GitHub exporters give "unrecoverable error ... file too large" on tiny models; 2020 worked. | — | bim coordinator | [revit-ifc #590](https://github.com/Autodesk/revit-ifc/issues/590) |
| en | An escalator family (generic model, IfcBuildingElementProxy) does not show up in the exported IFC. | — | bim coordinator | [forums.autodesk.com](https://forums.autodesk.com/t5/revit-architecture-forum/quesion-ifc-mapping-dissappearing-objects-in-export/td-p/7181576) |
| en | Two door types from a Revit IFC share an IsExternal boolean; change one and the other changes. Is that right? | — | bim coordinator | [community.osarch.org](https://community.osarch.org/discussion/1753/bbim-two-door-types-with-connected-properties) |
| en | One alarm type with 10 instances exports as 3 IFC types. | — | mep engineer | [revit-ifc #809](https://github.com/Autodesk/revit-ifc/issues/809) |
| en | Revit auto-generates hundreds of IfcBuildingElementProxyType I can't edit, so clients see proxies without data. | — | reviewer authority | [revit-ifc #676](https://github.com/Autodesk/revit-ifc/issues/676) |
| en | Nested shared families export as separate objects with no relation to the parent (door leaf, frame, closer). | — | bim coordinator | [revit-ifc #374](https://github.com/Autodesk/revit-ifc/issues/374) |
| en | Revit puts the type name in ObjectType, so beginners think that is the IFC type. | — | researcher academic | [revit-ifc #502](https://github.com/Autodesk/revit-ifc/issues/502) |
| en | I assign ClassificationCode[Type] to a type but it lands on the occurrences, not on IfcWallType. | — | bim coordinator | [revit-ifc #691](https://github.com/Autodesk/revit-ifc/issues/691) |
| en | Best IFC class for a PVC reducing coupling joining two sizes? | — | mep engineer | [forums.buildingsmart.org](https://forums.buildingsmart.org/t/best-ifc-classification-for-a-reducing-coupling/5963) |
| en | Ducts and pipes show as generic types after export. | — | mep engineer | [forums.autodesk.com](https://forums.autodesk.com/t5/revit-mep-forum/ifc-export-ducts-and-pipes/td-p/12370919) |
| en | Proxies in the files I read are really walls or doors; is there a generic way to tell what a proxy is? | — | developer programmer | [forums.buildingsmart.org](https://forums.buildingsmart.org/t/5130) |
| en | After importing an IFC all my walls are just Generic Models. How do I get Revit to recognise walls? | — | architect | [revit-ifc #571](https://github.com/Autodesk/revit-ifc/issues/571) |
| en | Plain walls import well, but a wall with a window gets family "Imported Symbol" and cannot be modified. | — | architect | [revit-ifc #729](https://github.com/Autodesk/revit-ifc/issues/729) |
| en | IFC4 Design Transfer View: any experiences? | — | bim manager | [forums.buildingsmart.org](https://forums.buildingsmart.org/t/ifc4-design-transfer-view-experiences/4362) |
| en | Site coverage and site boundary came out as IfcSpace; IFC+SG wants IfcGeographicElement. | — | architect | [github.com](https://github.com/noddlesskcho/ifc-sg-site-object-repair) |
| en | My export script ignores the mapping settings of the normal export. | — | developer programmer | [forum.dynamobim.com](https://forum.dynamobim.com/t/ifc-export-does-not-respect-mapping/112777) |
| en | I want a single IFC from linked RVTs without Navisworks; binding loses geometry. | — | bim manager | [revit-ifc #439](https://github.com/Autodesk/revit-ifc/issues/439) |
| en | create_point_based_element ignores x/y/z and host for a hosted door (FamilyInstance.Host is null). | — | architect | [rvt-mcp #13](https://github.com/bimwright/rvt-mcp/issues/13) |
| en | My IFC has proxies, extra storeys and duplicates of other disciplines' walls. | — | bim coordinator | [bimcorner.com](https://bimcorner.com/10-common-ifc-export-mistakes-to-avoid-part-1/) |
| de | Meine Fundamentwände aus dem Wandwerkzeug werden IfcWall statt IfcFooting. | My foundation walls modelled with the wall tool become IfcWall instead of IfcFooting. | architect | [bim-me-up.com](https://bim-me-up.com/wand-als-ifcfooting-exportieren/) |
| de | † Revit Typenparameter nach IFC exportieren | Exporting Revit type parameters to IFC (they vanished after an exporter update). | bim coordinator | [bim-me-up.com](https://bim-me-up.com/revit-typenparameter-nach-ifc-exportieren/) |
| de | † Die Wunderwaffe IFC | "The miracle weapon IFC": partner imports my IFC and windows/walls arrive as plain dumb objects. | bim manager | [bim-me-up.com](https://bim-me-up.com/die-wunderwaffe-ifc/) |
| de | † IFC Tipp: Revit-Stütze den IsExternal Standardparameter zuweisen | IFC tip: give a Revit column the standard IsExternal parameter (not filled for columns). | architect | [bim-me-up.com](https://bim-me-up.com/ifc-tipp-revit-stutze-den-isexternal-standardparameter-zuweisen/) |
| es | Problema al importar modelo de Revit en plantilla de estructuras; todos los elementos asignados a IFC pero ETABS muestra mensaje de error. | Problem importing a Revit model into the structure template; all elements are assigned to IFC but ETABS shows an error. | structural engineer | [forums.buildingsmart.org](https://forums.buildingsmart.org/t/como-poder-exportar-un-modelo-3d-estructural-realizado-en-revit-a-etabs-por-medio-del-formato-ifc/2985) |
| es | † 10 Consejos Para Exportar un buen IFC con REVIT | 10 tips for exporting a good IFC from Revit (answer: add IFC parameters to templates, avoid in-place families). | bim coordinator | [bimnd.es](https://www.bimnd.es/blog/10-consejos-para-exportar-un-buen-ifc-con-revit/) |
| it | Ho un IFC ricevuto dal collega, devo modificare le proprietà ma il viewer è in sola lettura e i muri sono finiti come proxy, come faccio senza rompere i GUID? | I got an IFC from a colleague, need to edit properties, viewer is read-only and walls ended up as proxy; how without breaking GUIDs? | bim coordinator | [biblus.acca.it](https://biblus.acca.it/problemi-editing-file-ifc/) |
| it | Come carico il file di mappatura classi IFC in Revit prima di aprire l'IFC così le porte restano porte? | How do I load the IFC class mapping file in Revit before opening the IFC so doors stay doors? | architect | [biblus.acca.it](https://biblus.acca.it/ifc-class-mapping-file/) |
| it | Esporto da Revit ma i parametri custom non finiscono nei Pset, come li mappo? | I export from Revit but custom parameters don't end up in the Psets; how do I map them? | bim coordinator | [biblus.acca.it](https://biblus.acca.it/conversione-modello-bim-in-ifc5/) |
| it | Cos'è la Coordination View 2.0 e quando usarla? | What is Coordination View 2.0 and when should I use it? | architect | [biblus.acca.it](https://biblus.acca.it/ifc-2x3-coordination-view-2-0/) |
| it | Cosa si perde esportando da Revit in IFC? Le famiglie e le relazioni vengono mappate bene? | What is lost when exporting from Revit to IFC? Are families and relations mapped well? | bim manager | [biblus.acca.it](https://biblus.acca.it/ifc-vs-rvt-quali-sono-le-principali-differenze-tra-revit-e-ifc-in-termini-di-interoperabilita-e-scambio-dati/) |
| ja | IFCに書き出したらモデルの半分が消えていた。ただのソリッド、階に紐づかないレイヤ、非表示要素が原因 | Half the model disappeared on IFC export; causes: plain solids, layers not tied to a storey, hidden elements. | architect | [note.com](https://note.com/toshio_nakamura/n/nc8db42ce3191) |
| ja | IFCにすれば別ソフトで編集を続けられると思われがち。実際はパラメトリック関係や独自パラメータが落ちる | People think IFC lets you keep editing elsewhere; in fact parametric relations and custom parameters drop out. | bim manager | [note.com](https://note.com/onestruction/n/ne8322e3be44d) |
| nl | Zonder de correcte exportinstelling wordt een element vaak een BuildingElementProxy; gebruik TypeEnumeration, NOTDEFINED als je niet kiest | Without the right export setting an element often becomes a BuildingElementProxy; use the type enumeration, NOTDEFINED if you do not choose. | bim coordinator | [digigo.nu](https://www.digigo.nu/ilsen-en-richtlijnen/bim-basis-ils/3-4-correct-gebruik-entiteiten) |
| ru | Таблица категория-класс врёт, в IFC класс берётся из параметров экспорта; в 2022 и старше только IfcExportAs | The category-to-class table "lies"; the IFC class comes from export parameters; in 2022 and older only IfcExportAs. | bim coordinator | [habr.com](https://habr.com/ru/articles/1089018/) |
| ru | Стандартный параметр «Экспорт в IFC» ненадёжен: косоуры выгружаются при «Нет»; категория Стена - откатные ворота | The standard "Export to IFC" parameter is unreliable: stair stringers are exported when it says No; sliding gates are modelled as the Wall category. | bim coordinator | [habr.com](https://habr.com/ru/articles/1098340/) |
| ru | Косоуры всё равно выгружаются при IfcExportAs нет, пандус уходит как IfcRampFlight, МССК коды помещениям вручную | Stringers are still exported when IfcExportAs is "no", the ramp goes out as IfcRampFlight, room codes are entered by hand. | bim coordinator | [habr.com](https://habr.com/ru/articles/1098340/) |
| ru | Ревит надо настроить заранее: оси в IFCGrid, IFCExportAs в ФОП, разбивка стен по уровням | Revit has to be set up beforehand: grids as IFCGrid, IFCExportAs in the shared parameter file, walls split by level. | architect | [sapr.ru](https://sapr.ru/article/25825) |
| ru | При импорте IFC геометрия есть, но элементы не распознаются как объекты, пропадают параметры, нужно получить модель для чертежей | On IFC import the geometry is there but elements are not recognized as objects, parameters disappear; I need a model for drawings. | bim coordinator | [forum.dwg.ru](https://forum.dwg.ru/showthread.php?t=166052) |
| ru | При импорте IFC архитектурных моделей из других программ элементы приходят как тела, а не как родные объекты Ревита, хочу их редактировать | Importing architectural IFC from other programs, elements arrive as solids not native Revit objects; I want to edit them. | architect | [forum.dwg.ru](https://forum.dwg.ru/showthread.php?t=166052) |
| ru | После экспорта в IFC из Ревита часть элементов и параметров потерялась, как проверить где проблема - в экспорте или в просмотрщике | After exporting from Revit to IFC some elements and parameters are lost; how to check if it is the export or the viewer? | bim coordinator | [forum.dwg.ru](https://forum.dwg.ru/showthread.php?t=154396) |
| ru | Можно ли редактировать семейство из IFC в Ревите | Can I edit a family that came from IFC in Revit? | architect | [forum.dwg.ru](https://forum.dwg.ru/showthread.php?t=130296&page=2) |
| ru | При экспорте из Архикада в IFC и вставке в Ревит стёкла жёлтые и толщиной в метры, часть перегородок пропала | Exporting from Archicad to IFC and inserting into Revit: glass is yellow and metres thick, some partitions vanished. | architect | [forum.dwg.ru](https://forum.dwg.ru/showthread.php?t=154396) |
| ru | Как открыть IFC в ревите корректно, выгружал экспортёром, импортированная модель кривая | How do I open IFC in Revit correctly? I exported with the exporter and the imported model is crooked. | student beginner | [forum.dwg.ru](https://forum.dwg.ru/showthread.php?t=154396) |
| ru | При каждой конвертации в IFC и обратно теряются данные, элементы возвращаются мёртвой геометрией | Every conversion to IFC and back loses data; elements come back as dead geometry. | bim manager | [sapr.ru](https://sapr.ru/article/24777) |
| zh | Revit导出IFC时各类别对应哪个IFC类，贴出导出图层/类别映射文件 | Which IFC class does each Revit category map to when exporting? (pastes the layer/category mapping file) | bim coordinator | [cnblogs.com](https://www.cnblogs.com/liaocheng/p/15905467.html) |
| zh | 需要导出的构件在exportlayers-ifc-IAI里找不到对应类别，怎么改导出选项 | The element I need to export has no matching category in exportlayers-ifc-IAI; how do I change the export options? | bim coordinator | [zhihu.com](https://www.zhihu.com/question/418802002) |
| zh | 介绍Revit 2023里IFC参数和导出映射对话框怎么改导出的实体和预定义类型 | How the Revit 2023 IFC parameters and export mapping dialog change the exported entity and predefined type. | bim manager | [bilibili.com](https://www.bilibili.com/video/BV1Ba41177xJ/) |
| zh | Revit2020导出IFC选项是灰的 | In Revit 2020 the IFC export option is greyed out. | bim coordinator | [zhuanlan.zhihu.com](https://zhuanlan.zhihu.com/p/611709017) |
| zh | revit2019点击导出IFC后没反应，导出位置只有一个schema文档 | Revit 2019: nothing happens on IFC export; only a schema document appears in the export folder. | architect | [zhihu.com](https://www.zhihu.com/question/455661969) |
| zh | revit2020导出的ifc没有guid，为什么 | The IFC exported from Revit 2020 has no GUID; why? | bim coordinator | [zhihu.com](https://www.zhihu.com/question/625548241) |
| zh | IFC导出参数里插入点和项目基点关系 | What is the relation between the insertion point and the project base point in the IFC export parameters? | bim coordinator | [jianshu.com](https://www.jianshu.com/p/76e051ccd5eb) |
| zh | IfcBuildingElementProxy是什么 | What is IfcBuildingElementProxy? | developer programmer | [cnblogs.com](https://www.cnblogs.com/herd/p/15765322.html) |
| zh | revit导出ifc没有东西 | The IFC exported from Revit has nothing in it. | bim coordinator | [blog.csdn.net](https://blog.csdn.net/d001014/article/details/140438872) |
| zh | Revit导IFC哪些信息会丢，类别对不上IFC类、坐标转换没了 | What information is lost exporting IFC from Revit: categories don't match IFC classes, the coordinate transform is gone. | bim coordinator | [bbs.co188.com](https://bbs.co188.com/thread-10112116-1-1.html) |
| zh | Revit导出IFC会丢哪些信息，共享参数、材质、族参数 | What does Revit lose when exporting IFC: shared parameters, materials, family parameters? | bim coordinator | [blog.csdn.net](https://blog.csdn.net/weixin_39590472/article/details/112503752) |
| zh | Revit傳到Robot/ETABS/SAP2000，IFC方式資料遺失或更動，原生檔與API較佳 | Transferring from Revit to Robot/ETABS/SAP2000 via IFC loses or alters data; native file and API work better. | structural engineer | [tdr.lib.ntu.edu.tw](https://tdr.lib.ntu.edu.tw/handle/123456789/90111) |

## Ready test prompts

Curated from the synthetic records (labelled synthetic; none are real quotes). Weak ones were reworded to sound like a person typing to an assistant. `needs file` is true for almost all: assume an IFC (or a live Revit session for "Revit live" rows) is loaded.

| lang | prompt | type | difficulty | expected behavior |
|---|---|---|---|---|
| en | how many IfcBuildingElementProxy in here and what revit category did they come from | model_task | medium | Count proxies, group by type/name/ObjectType, say Revit category is only available if Revit property sets were exported, suggest mapping fixes |
| en | client says anything over 5% proxies fails. what's our share and who are the worst offenders by type name | model_task | easy | Proxy share of all IfcElement, top proxy types, explicit pass/fail |
| en | how do i make my generic model families export as IfcColumn instead of proxy? tried the mapping table, still proxy | how_to | medium | Explain type-level override vs category mapping, precedence, check Revit year and exporter version |
| en | since we moved to Revit 2023 my IfcExportAs values do nothing. which parameter do i set now? | troubleshooting | medium | Explain built-in Export to IFC As / Export Type to IFC As, migrate old values, verify in a test export |
| en | set IfcExportAs to IfcCovering for all wall sweeps in the revit model | model_task | medium | Revit live: set the type-level export class (built-in param), confirm sweeps may still follow host, report changed list, ask before changing the model |
| en | fascias are proxy in the export, change them to IfcCovering and save as a new ifc | model_task | hard | IFC-side: list candidates by name/type first, reclassify only after confirmation, write a new file, warn that psets/quantities of the new class are not created |
| en | stairs are missing in the ifc, check the Export to IFC param on the stair types | model_task | medium | Read per-type parameter values, report No/By Type, check category row and steel/stair options, do not invent values |
| en | set predefined type TRANSITION on all reducer pipe fittings | model_task | medium | Find IfcPipeFitting with differing port sizes, set TRANSITION, report each change, note IFC schema must have the value |
| en | do all IfcCovering have PredefinedType set? list the ones with NOTDEFINED or empty | model_task | easy | Query occurrences and their types; show both levels |
| en | the two door types share IsExternal, change one and the other flips. check if the pset props are shared entities | model_task | hard | Inspect property relations, detect shared single-value entities, offer to split after confirmation |
| en | updated the ifc exporter and my type params are gone from the psets, what changed | troubleshooting | medium | Explain type-class listing in the pset file and the type-in-instance option, ask exporter versions |
| en | for doors, show me which psets/props come from the type and which from the occurrence, flag dupes | model_task | medium | Show both levels separately, flag duplicated names/values |
| en | my prof says walls should be IfcWall but i see IfcWallStandardCase and some IfcWall, why? list which is which | model_task | medium | Count both, explain 2x3 vs IFC4 and that StandardCase is deprecated in IFC4 |
| en | what is ObjectType vs the actual type of this wall? it shows the revit type name, is that the ifc type?? | model_task | medium | Show ObjectType, PredefinedType and the IfcRelDefinesByType type entity; explain the difference |
| en | the classification landed on the instances not the types, move it to IfcWallType and dedupe | model_task | hard | Move per type, report conflicts, do not delete before confirming |
| en | curtain wall panels vanish in the ifc but mullions export fine?? revit 2024 | troubleshooting | medium | Check curtain wall structure (IfcCurtainWall, IfcMember, IfcPlate), exporter version, panel visibility |
| en | find all IfcFlowSegment that are not duct or pipe segments, hvac model from consultant | model_task | medium | Group by predefined type/name, note IfcDuctSegment/IfcPipeSegment exist from IFC4 |
| en | client wants IFC per ISO 19650 EIR but doesn't say which one. 2x3 coordination view or IFC4 reference view? we are on Revit 2024 | how_to | medium | Present options and consequences, ask the receiver's checker/requirement before recommending |
| en | export the current revit view to ifc4 with base quantities on, api call not the dialog | how_to | medium | Options object, active view id, base-quantity flag, transaction handling, read back the result file |
| en | check if repeated families are exported as IfcMappedItem or duplicated geometry, how much size would we save | model_task | hard | Compare identical-geometry instances vs shared representation maps, estimate saving |
| en | write an IDS that fails if any IfcBuildingElementProxy exists, and run it on the loaded model | model_task | medium | Valid IDS, run it, list failing elements |
| de | die Stützen sind alle als Proxy drin, kannst du die zu IfcColumn machen? Name fängt mit ST_ an | model_task | medium | Dry-run list, reclassify after OK, report remaining proxies |
| de | Deckendurchbrüche fehlen in der IFC, in Revit sind sie da (Schacht). Export 2x3 CV. was tun? | troubleshooting | medium | Check IfcOpeningElement/IfcRelVoidsElement, known shaft-opening bug, suggest modelling opening differently |
| de | prüf ob die exportierten IFC-Klassen mit dem was in IfcExportAs steht übereinstimmen, wir hatten wieder Abweichungen | model_task | hard | Compare parameter vs actual class per element, list deviations |
| ru | глянь сколько в модели проксей и из каких категорий ревита пришли, надо понять что перемапить | model_task | medium | Count/group proxies, state the category limitation, propose mapping |
| ru | косоуры лестниц опять в ифс хотя стоит не выгружать, найди их и скажи по какому классу ушли | model_task | medium | Find stringer-like elements, report class, suggest excluding via parameter or post-process |
| ru | перебей класс у всех IfcBuildingElementProxy с именем «Ограждение*» на IfcRailing и сохрани новую версию | model_task | medium | List matches, confirm, reclassify, save as new file |
| ru | у всех типов обобщённых моделей с «Колонна» в имени проставь IfcExportAs=IfcColumn, остальные не трогай | model_task | medium | Revit live: set the override only on matching types, report changed list, mention built-in parameter in 2023+ |
| ru | для экспертизы какой ифс выгружать, 2х3 или 4, и какой вид, CV2 или RV? | how_to | medium | Ask the expert body's requirement, present options |
| ru | ревит валится при экспорте в ифс, «неустранимая ошибка». глянь в модели что может ломать - помещения без границ, битые стены? | model_task | hard | Look for suspect rooms/walls, but also ask exporter version and add-ins; do not blame the model without evidence |
| zh | 类别映射表和族类型上的 IfcExportAs 哪个优先？我设了两个不一样，导出还是proxy | how_to | easy | Explain priority (override over category mapping), check subcategory and built-in parameter |
| zh | 导出的ifc里一堆IfcBuildingElementProxy，帮我看看都是哪些族类别导出来的，是不是通用模型 | model_task | medium | Group proxies, check generic-model pattern |
| zh | 幕墙导出IFC后竖梃都没了，只剩玻璃嵌板，帮我看看哪些幕墙缺竖梃 | model_task | medium | Per curtain wall compare IfcMember vs IfcPlate parts |
| zh | Revit匯IFC 門都變proxy 是哪裡設定錯了？ | troubleshooting | medium | Check category mapping for Doors and any type-level override |
| zh | revit导出ifc钢结构节点螺栓全没了，勾了包含钢构件也不行，咋回事 | troubleshooting | medium | Steel connections limitation, exporter version, option behaviour |
| zh | revit2019导ifc点了没反应只出个schema文件，咋回事 | troubleshooting | easy | Missing/outdated IFC exporter add-in, install/update |
| es | los zócalos y vierteaguas salen como proxy, cámbialos a IfcMember o IfcCovering según el caso y dime cuáles tocaste | model_task | hard | Propose per case, ask before changing, list changed elements |
| es | los modelos genéricos salen como proxy, pásalos a IfcColumn los que tengan 'pilar' en el nombre | model_task | medium | Name-filtered reclassification with dry run |
| it | i proxy con nome 'Pilastro' mettili come IfcColumn | model_task | hard | Dry-run and confirm; keep GlobalIds |
| it | confronta i due IFC (v1 e v2) e dimmi quanti proxy abbiamo ancora e quali sono stati riclassificati | model_task | hard | Match by GlobalId, report class changes |
| ja | このIFC、IfcBuildingElementProxyが何個あるか数えて、元のRevitカテゴリ別に集計して。マッピング直す対象知りたい | model_task | medium | Count, group, state the category caveat |
| ja | IFCに出したら半分くらい要素が無い…Revitの元モデルと比べて何が落ちてるか調べて。階に紐づいてないやつとか | model_task | hard | Compare categories, check storey assignment, hidden/unmapped items |
| ko | 레빗에서 IFC4 내보낼때 Reference View랑 Design Transfer View 중에 뭐 써야돼요? | how_to | easy | Explain options, ask receiver requirement |
| ko | 일반 모델 패밀리가 전부 프록시로 나가는데 IFC 클래스 매핑 테이블 어떻게 설정해야 돼요? | how_to | easy | Explain category mapping and type override |
| pt-BR | como faço uma família generic model sair como IfcWall no ifc? coloquei IfcExportAs mas não pegou | how_to | medium | Explain the 2023+ built-in parameter, level, schema |
| pt | tem uns proxy que são bombas, muda pra IfcPump com o type certo e predefined type | model_task | medium | Reclassify with the matching IfcPumpType and predefined type; confirm |
| nl | mijn kozijn familie komt als proxy in het ifc ipv IfcWindow, wat moet ik instellen in Revit? | troubleshooting | easy | Window category mapping vs family category, type override |
| fr | j'ai plein de proxy dans mon IFC, c'est quoi comme catégories revit ? faut que je corrige la table de correspondance | model_task | medium | Count/group, advise mapping table changes |
| no | hvordan eksporterer jeg fra Revit til IFC så bestiller godtar den? hvilken MVD og innstillinger | how_to | easy | Ask what the client requires before recommending |

## Edge cases and traps

- **Proxy is not always a bug.** Provisions for voids and truly generic objects can legitimately be proxies. A "zero proxies" demand should come from the receiver's rule, not from the assistant.
- **"Which Revit category did it come from?"** is not an IFC attribute. The IFC `Name` is often `Family:Type:ElementId` [cnblogs.com](https://www.cnblogs.com/herd/p/14908387.html), `ObjectType` often holds the Revit type name [revit-ifc #502](https://github.com/Autodesk/revit-ifc/issues/502), and a category appears only in Revit property sets if they were exported. A tool that "knows" the category without evidence is guessing.
- **Reclassifying inside the IFC is not the same as fixing the Revit export.** The new class has no matching psets or quantities, types may be missing, and quantities may follow the old class [revit-ifc #497](https://github.com/Autodesk/revit-ifc/issues/497). A good tool says so and offers the source-side fix.
- **Substring rules overreach.** "Everything with Колонна in the name" or "ST_*" may hit decorative or unrelated objects. Require a dry-run list and confirmation before writing.
- **Schema-dependent classes.** IfcWallStandardCase belongs to IFC2x3; IfcDuctSegment/IfcPipeSegment appear from IFC4; some predefined types exist only in IFC4 ([export reference](../../03_software/revit/ifc_export_reference.md), [digigo.nu](https://www.digigo.nu/ilsen-en-richtlijnen/bim-basis-ils/3-4-correct-gebruik-entiteiten)). A request for a class that does not exist in the file's schema must be flagged.
- **Version and year.** Exporter behaviour differs between Revit years and add-in builds; several reported bugs are "open", "cannot reproduce" or "fixed in 2027". Do not assert a fix without the version.
- **Local conventions are not Autodesk rules.** `IfcExportAs = -1` to exclude objects, `RUS_*` parameters and national checkers (Russian expert review, Singapore IFC+SG) are local practice [habr.com](https://habr.com/ru/articles/1098340/), [github.com](https://github.com/noddlesskcho/ifc-sg-site-object-repair); ask which rule set applies.
- **The file may not be from Revit.** Archicad, Tekla, Renga or SketchUp exports produce proxies too [SketchUp-IFC-Manager #63](https://github.com/BIM-Tools/SketchUp-IFC-Manager/issues/63); check the header application before blaming the Revit mapping.
- **Type vs instance in every edit.** Ask which level; check for shared property entities before editing one type [community.osarch.org](https://community.osarch.org/discussion/1753/bbim-two-door-types-with-connected-properties).
- **Live-Revit tools can silently ignore parameters.** One MCP tool ignored position and host for hosted families until it required `host_id` [rvt-mcp #13](https://github.com/bimwright/rvt-mcp/issues/13). After any create/modify call, read back and compare.
- **Do not trust the viewer alone.** Missing properties or objects can be a viewer limit; check the text of the IFC or a second viewer [forum.dwg.ru](https://forum.dwg.ru/showthread.php?t=154396).
- **Human voice.** Informal and abbreviated: "ифс", "проксей", "кобай", lowercase "revit", no punctuation, missing context ("again", "the usual check"). Tests should include prompts that omit the file name, schema or tool.
- **Duplicates in the data.** Many threads are logged by several research cells; frequency counts are not independent.

## Related docs

- [Revit IFC export reference](../../03_software/revit/ifc_export_reference.md)
- [Revit IFC import and link reference](../../03_software/revit/ifc_import_link_reference.md)
- [Materials, classification, types, styles](../../01_ifc_basics/07_materials_classification_types_styles.md)
- [Entities cheat sheet](../../01_ifc_basics/03_entities_cheat_sheet.md)
- [Properties, quantities and psets](../../01_ifc_basics/05_properties_quantities_psets.md)
- [IFC in other authoring tools](../../03_software/authoring_tools_ifc.md)
- [Glossary (multilingual)](../../08_glossary/glossary_multilingual.md) and [abbreviations](../../08_glossary/abbreviations.md)
- Sister document: [Properties, property sets and parameter mapping](properties_and_parameters.md)
