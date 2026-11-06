# Properties, property sets and parameter mapping

Vocabulary topic covered: `psets_properties` (398 tagged records: 252 real, 146 synthetic).
Data basis: research wave 1 only (`research_raw/wave1/`, no wave 2 yet). Real records by language: 214 en, 10 ru, 8 zh, 5 de, 5 it, 3 es, 3 ja, 2 nl, 2 no. The 252 real records sit on about 214 distinct source URLs, because several research cells logged the same GitHub issue or forum thread; "records" below are not independent people. The topic overlaps strongly with [Revit export and class mapping](revit_export_and_class_mapping.md): 78 of the records are also tagged `export_revit`, 22 `class_mapping`, 17 `types_vs_instances`.

## In plain words

In an IFC file, almost every fact beyond shape and class (fire rating, "is this wall external?", manufacturer, a company code) is stored as a **property** inside a named **property set** ("pset"), for example `Pset_WallCommon.FireRating`. In Revit these facts live in **parameters** (instance parameters on one wall, type parameters on a wall type, shared and project parameters you add yourself). **Parameter mapping** is the step that decides which Revit parameter becomes which IFC property in which pset. Standard sets (`Pset_...`, `Qto_...`) have fixed names defined by buildingSMART; your own sets must use another name. Most trouble comes from three places: the parameter never reaches the pset (setup, mapping file, version), the value arrives on the wrong level or in the wrong data type, or a person or tool looks in the wrong place and concludes the data is missing. Properties can sit on the **type** or on the **occurrence**; if both have the same property the occurrence wins.

Background reading: [Properties, quantities and psets](../../01_ifc_basics/05_properties_quantities_psets.md) (property model, type vs occurrence, standard sets, pitfalls), [Revit IFC export reference](../../03_software/revit/ifc_export_reference.md) (Property Sets tab, user-defined pset file, parameter expressions), [materials, classification, types](../../01_ifc_basics/07_materials_classification_types_styles.md), [IFC in other authoring tools](../../03_software/authoring_tools_ifc.md) (Archicad, Tekla, Renga mapping approaches), [multilingual glossary](../../08_glossary/glossary_multilingual.md). Sister document: [Revit export and class mapping](revit_export_and_class_mapping.md).

Counting note: the "frequency signal" column uses keyword matches over the real records (title, paraphrase, answer summary); numbers are approximate and overlap. Synthetic prompts are counted separately, they show what test authors expect.

## Problem map

| # | Problem | How users describe it | Frequency signal | Root cause | Typical fix |
|---|---|---|---|---|---|
| 1 | My custom / shared parameters do not appear in the IFC | "user defined properties won't export", "общие параметры пропали", "共享参数导出后没了", "i miei parametri condivisi non ci sono nei Pset" | ≈44-52 real (38-46 en, 2 ru, 1-2 de, 1-2 zh, 1 it); 20 of 146 synthetic prompts in 8 languages (en 9, ru 3, zh 3, de/fr/it/ko/pt-BR 1 each) | Option off or file not selected; txt syntax (tabs, case, entity class); shared-parameter file confused with pset file; hidden parameters; builds differ between team members | Build the pset file from the shipped template, same exporter version for all, check element scope and binding |
| 2 | Revit 2027 new parameter/property mapping dialog is incomplete | "mapping parameters severely lacking", "where did the pset txt go?", "not all Revit parameters appear" | ≈19 real mention 2027 or the new dialog (17 en, 1 it, 1 zh) | New UI lists only parameters whose data type matches the property; some classes (IfcProject) missing; legacy checkboxes ignored in the new mode | Check data type of the parameter, version of add-in, Autodesk known-issue entries |
| 3 | Mapping onto standard Pset_*Common (FireRating, LoadBearing, IsExternal) does not override or collides | "can't overwrite LoadBearing", "built-in value wins", "IsExternal not filled for columns" | ≈31 real (25 en, 2 de, 2 it, 2 nl) | Built-in value takes precedence; case-insensitive name clash; type parameter ignored for entity-level instance properties | Mapping table or file with the exact IFC names, instance parameter, avoid same names as built-ins |
| 4 | Type vs instance: values on the wrong level, type properties missing | "only type parameters export", "(Type) in the pset name", "I/T flag?", "changing one door type changes the other" | ≈26 real (23 en, 2 de, 1 ja); 17 `types_vs_instances` records | Type psets written only when requested; psets shared between types; occurrence overrides type per property | List type class in the file, tick type-in-instance option, check both levels |
| 5 | Wrong data type or unit | "AboveGround shows UNKNOWN", "feet / 304.8", "15 degrees became 15.35", "1000 mm as text", "IfcArea instead of IfcReal" | ≈33 real (29 en, 2 de, 1 ru, 1 zh); a few synthetic prompts in en and ru | Yes/No maps to IfcLogical; unit conversion bugs; measure type in the mapping file must match the schema; text with units | Match data types, full pset-qualified name, store numbers and units separately |
| 6 | Empty values: not exported, or ambiguous (missing vs FALSE vs unknown) | "empty parameters are not exported", "which doors have no FireRating?" | ≈27 real (25 en, 2 de); 28 of 146 synthetic prompts mention fire rating (mostly completeness checks) in 9+ languages | Empty parameters skipped by design; "no value" is not FALSE; blank psets invalid | Fill before export; report "missing" separately from "false" |
| 7 | Revit data that is hard to map (category, room area, materials, parts, schedules, IfcSystem, phases, quantities) | "can't export room area to custom pset", "Revit Category as pset", "material not exported", "Qto missing" | about 8 distinct threads cited below (all en; mostly open Jira-tracked issues), plus ≈15 quantity mentions | Not all Revit built-ins are mappable; Parts/roofs/stairs/railings excluded; base quantities off by default | Use Revit property sets for built-ins, schedules-as-psets (with caution), enable base quantities, accept Jira-tracked gaps |
| 8 | "Where is my data?" (viewer, reader or script does not show it) | "properties missing in viewer", "Navisworks shows them from RVT but not from IFC", "includeTypeProperties returns empty" | ≈19 real about reading tools (18 en, 1 ja); 85 of 146 synthetic prompts mention psets/properties, many as "what does this element actually have" checks | Viewers show different subsets; type psets reached through IfcRelDefinesByType; psets on IfcProject not IfcSite | Inspect the file text, use a library that merges type and occurrence psets |
| 9 | Naming and validity: Pset_ prefix, duplicate or blank psets, AI-invented names, Name vs Reference | "Is Pset_Fire a valid name?", "multiple like-named psets", "AI gave me Pset_BuildingElementCommon" | ≈24 broad matches on Name/Reference/ObjectType (all en); naming-rule questions also from nl and en | `Pset_` reserved for the standard; unique pset names per object; LLMs predict plausible but invented names | Use `Company_` style names, verify against the schema |
| 10 | Adding, copying or editing properties inside an IFC file | "add a custom pset to slab S-01", "copy FireRating into a custom pset", "fill from CSV" | ≈44 broad matches on writing/editing (33 en, 3 it, 3 zh, 2 de, 2 ja, 1 ru); ≈34 synthetic model_task prompts that ask for a write | Needs relation entities (IfcRelDefinesByProperties); shared entities; units; GlobalId handling | Library API, dry run, save as new file |
| 11 | Classification codes in the wrong place | "Classification code lands on occurrences, not types", "duplicate IfcClassification", "NL-SfB in a custom pset" | ≈8 real in this topic (6 en, nl, ru) plus the classification cell | A classification is `IfcClassificationReference`, not a pset property | Map via classification settings, repair afterwards with a script |
| 12 | National or contractual property requirements and their checks | "MIDE", "NS 8360", "IFC+SG", "SZ-IFC", "МССК/ЦИМ", "ILS" | ≈12 real (en 5, es 2, no 2, ru 2, zh 1); validation/IDS ≈48 broad matches | Each program defines mandatory psets and formats; IDS and checkers need exact pset + property + type | Ask which rule set applies; run a checker; fix at source |
| 13 | Non-English parameter names and special characters | "Czech Objem/Plocha overwritten", "Cyrillic shows as gibberish", "Korean metadata not searchable" | ≈9 broad matches here, plus the `encoding_text` cell; synthetic in ru, zh, en | Mapping is by name, case-insensitive; text encoding `\X2\...\X0\` | Map explicitly, avoid clashes with built-in names, decode properly |

## Problems in depth

### 1. Custom and shared parameters do not appear in the IFC

**Symptoms in users' words**
- en: "Custom properties defined in the user-defined property set file do not appear in the exported IFC" [forums.autodesk.com](https://forums.autodesk.com/t5/revit-architecture-forum/revit-ifc-export-user-defined-properties-won-t-export/td-p/9767878). "Some shared parameters are exported by one team member and missing for another" [help.autodesk.com](https://help.autodesk.com/view/RVT/2025/ENU/?caas=caas%2Fsfdcarticles%2Fsfdcarticles%2FCertain-shared-parameters-not-exportetd-to-IFC-from-Revit.html).
- en: pointed "user defined property sets" at the shared parameter file and nothing exported; the answer: the pset file has its own format [forums.autodesk.com](https://forums.autodesk.com/t5/revit-architecture-forum/revit-ifc-export-user-defined-properties-won-t-export/td-p/9767878).
- it: *"esporto da Revit ma i parametri custom non finiscono nei Pset, come li mappo?"* (I export from Revit but custom parameters don't land in the Psets) [biblus.acca.it](https://biblus.acca.it/conversione-modello-bim-in-ifc5/).
- de: type parameters vanished after an exporter update although the file used to work [bim-me-up.com](https://bim-me-up.com/revit-typenparameter-nach-ifc-exportieren/).
- ru: *"как связать русские параметры Revit с именами свойств IFC"* (how to connect Russian Revit parameters with IFC property names) [habr.com](https://habr.com/ru/articles/1098340/).
- zh: *"自定义属性集里的材质导不进IFC"* (materials in the custom property set don't reach the IFC); known limitation, mapped parameters need a value on the element [autodesk.com.cn](https://www.autodesk.com.cn/support/technical/article/caas/sfdcarticles/sfdcarticles/CHS/Materials-are-not-exported-to-IFC-with-custom-property-sets-from-Revit.html).

**Why it happens.** Causes named in the threads: wrong txt format or scope (IfcElement vs IfcWall), type-vs-instance setting, duplicate parameter names [forums.autodesk.com](https://forums.autodesk.com/t5/revit-architecture-forum/revit-ifc-export-user-defined-properties-won-t-export/td-p/9767878), [forums.autodesk.com](https://forums.autodesk.com/t5/revit-api-forum/ifc-export-only-part-of-user-defined-property-set-are-exported/td-p/10027559); a pset defined for IfcElement not exported while IfcRoot worked [revit-ifc #879](https://github.com/Autodesk/revit-ifc/issues/879); hidden shared parameters are not available to the exporter [revit-ifc #38](https://github.com/Autodesk/revit-ifc/issues/38); user-defined psets are not exported for Parts (commenters report the same for roofs, stairs and railings) [revit-ifc #662](https://github.com/Autodesk/revit-ifc/issues/662); a different exporter version on another machine. Reference docs add: IFC class names are case-sensitive and fields must be separated by real tab characters ([properties doc, section 6.1](../../01_ifc_basics/05_properties_quantities_psets.md); partly marked unverified there).

**What fixes it.** Start from the shipped sample file (`DefaultUserDefinedParameterSets.txt`), load it in the export setup ("Export user defined property sets"), use the same shared parameter file and exporter version for the whole team [help.autodesk.com](https://help.autodesk.com/view/RVT/2025/ENU/?caas=caas%2Fsfdcarticles%2Fsfdcarticles%2FCertain-shared-parameters-not-exportetd-to-IFC-from-Revit.html), and verify in the exported file.

**What a good AI/MCP assistant should do.** Check the IFC first: list which psets the element really has, then say what the setup would have to contain. Never claim a parameter "was exported" without finding the property. Mention that a viewer may hide it (problem 8).
**Clarifying questions.** Revit and exporter version? Shared, project or family parameter? Type or instance? Which setup tab is ticked and which file is loaded? Is the new mapping dialog (2027) used?

### 2. Revit 2027: the new mapping dialog

**Symptoms in users' words**
- en: "The new Revit 2027 parameter mapping GUI replacing the pset.txt workflow lists only some parameters; project parameters are missing, some classes show empty lists" [forums.autodesk.com](https://forums.autodesk.com/t5/revit-architecture-forum/ifc-export-in-2027-mapping-parameters-severely-lacking/td-p/14229702).
- en: in the new Manage Default Property Sets dialog changing the data type to Length shows none; "What is Property Type?" [revit-ifc #984](https://github.com/Autodesk/revit-ifc/issues/984).
- en: "In Revit 2027 ... IfcProject is missing; before 2027 it was possible to add a user-defined pset to IfcProject" [revit-ifc #971](https://github.com/Autodesk/revit-ifc/issues/971).
- zh: a news article asks whether the 2027 IFC export dialog can create custom property sets directly, no manual text [zhuanlan.zhihu.com](https://zhuanlan.zhihu.com/p/2025149945674474186).

**Why it happens.** The picker only lists Revit parameters whose data type matches the property's type (maintainer explanation, tracked as REVIT-254494 [revit-ifc #984](https://github.com/Autodesk/revit-ifc/issues/984)); Autodesk acknowledged the empty-list issue with no ETA [forums.autodesk.com](https://forums.autodesk.com/t5/revit-architecture-forum/ifc-export-in-2027-mapping-parameters-severely-lacking/td-p/14229702). Per the [export reference](../../03_software/revit/ifc_export_reference.md), the new "Property Mapping" mode replaces the legacy checkboxes rather than adding to them.

**What fixes it.** Check the parameter's data type against the property type, use the exporter build that matches the Revit year, and track the issues. Some users keep the legacy txt approach where it still works.

**What a good AI/MCP assistant should do.** Ask the Revit year before giving UI steps, state that 2027 differs from older posts, and avoid mixing legacy instructions with the new dialog.
**Clarifying questions.** Revit year and add-in build? Legacy file or new dialog? Which property type (text, length, logical)?

### 3. Mapping onto the standard Pset_*Common sets

**Symptoms in users' words**
- en: "We implemented an office-wide ARC-Loadbearing parameter ... the *Common.LoadBearing in the IFC takes only the built-in value" [revit-ifc #833](https://github.com/Autodesk/revit-ifc/issues/833).
- en: Czech-named shared parameters (Objem, Plocha) in a user-defined pset are replaced by the built-in Volume/Area values [revit-ifc #989](https://github.com/Autodesk/revit-ifc/issues/989) (a case-insensitive clash, item REVIT-255184).
- de: IsExternal not filled for columns; since Revit 2023 type parameters no longer export to Pset_Common [bim-me-up.com](https://bim-me-up.com/ifc-tipp-revit-stutze-den-isexternal-standardparameter-zuweisen/).
- en: "if I make a user-parameter with the exact PSet-Property it is automatically mapped. I need my users to see the Revit parameters in our own language" [revit-ifc #735](https://github.com/Autodesk/revit-ifc/issues/735).
- en: wants Mark and Type Mark pointed at Name, but entity attributes need separate IfcName-style parameters [revit-ifc #205](https://github.com/Autodesk/revit-ifc/issues/205).
- it: *"dove trovo il FireRating di un muro in un IFC e come lo modifico?"* (where is a wall's FireRating in an IFC and how do I edit it?), answer: in Pset_WallCommon [ingenio-web.it](https://www.ingenio-web.it/articoli/proprieta-ifc-muro-firerating-pset-wallcommon/).

**Why it happens.** LoadBearing is an entity-level instance property, so a type parameter is ignored [revit-ifc #833](https://github.com/Autodesk/revit-ifc/issues/833). A parameter whose name equals a standard property name is picked up automatically and built-ins can win on name clashes. The exporter derives some values itself, for example `IsExternal` from the wall function ([properties doc, pitfall 11](../../01_ifc_basics/05_properties_quantities_psets.md)).

**What fixes it.** Make an instance parameter with the exact IFC names (Yes/No, tab-separated mapping line) [bim-me-up.com](https://bim-me-up.com/ifc-tipp-revit-stutze-den-isexternal-standardparameter-zuweisen/), or map it explicitly; avoid reusing built-in names; for attributes use the `Ifc...` override parameters ([export reference section 6](../../03_software/revit/ifc_export_reference.md)).

**What a good AI/MCP assistant should do.** Show where a value actually came from (built-in, mapped, or empty) and warn that "FireRating" is a text label, not minutes.
**Clarifying questions.** Standard pset required or is a custom one fine? Type or instance parameter? Which language are the Revit parameter names in?

### 4. Type vs instance

**Symptoms in users' words**
- en: "type parameters missing in IFC property sets after export"; fix: tick "Allow use of type properties in instance property sets" [forums.autodesk.com](https://forums.autodesk.com/t5/revit-architecture-forum/issues-with-exporting-type-parameters-from-revit-to-ifc/td-p/14004505).
- en: "custom Pset export only brings type parameters" [forums.autodesk.com](https://forums.autodesk.com/t5/revit-architecture-forum/ifc-export-pset-only-type-parameters-exporting/td-p/9555287); in 19.3.0 only type parameters appear on windows [revit-ifc #159](https://github.com/Autodesk/revit-ifc/issues/159).
- en: "I would like to ask what is the meaning of the I or T setting in the txt file" [revit-ifc #206](https://github.com/Autodesk/revit-ifc/issues/206) (answer: create two psets, one for the type class and one for the instance).
- en: editing IsExternal of one door type changes the other because Revit reuses property entities [community.osarch.org](https://community.osarch.org/discussion/1753/bbim-two-door-types-with-connected-properties), [IfcOpenShell #3957](https://github.com/IfcOpenShell/IfcOpenShell/issues/3957).
- en: when is "(Type)" appended to pset names? Only when no type entity is exported, mostly IFC2x3 [revit-ifc #493](https://github.com/Autodesk/revit-ifc/issues/493).

**Why it happens.** By the schema the effective value is the union of type and occurrence properties and the occurrence wins per property ([properties doc, section 2](../../01_ifc_basics/05_properties_quantities_psets.md)). The Revit exporter only writes type psets when asked, and shares identical property entities across types to save space.

**What fixes it.** Declare the type class in the pset file; tick the type-in-instance option; check both levels after export.

**What a good AI/MCP assistant should do.** Always say whether a value is on the type or the occurrence, flag shared property entities before any edit, and offer an occurrence-level override.
**Clarifying questions.** Should all elements of the type share the value? Which IFC version (the "(Type)" naming differs)?

### 5. Wrong data types and units

**Symptoms in users' words**
- en: Yes/No parameter named only `AboveGround` is not exported (IfcLogical) [revit-ifc #1020](https://github.com/Autodesk/revit-ifc/issues/1020); request for IfcLogical support [revit-ifc #678](https://github.com/Autodesk/revit-ifc/issues/678).
- en: in a millimetre project spacing is written as feet divided by 304.8 [revit-ifc #1015](https://github.com/Autodesk/revit-ifc/issues/1015); typing 15 degrees exports 15.35 [revit-ifc #954](https://github.com/Autodesk/revit-ifc/issues/954).
- en: entering the actual PanelWidth 930 mm gives 1, a ratio 0.5 gives 0.00164 [revit-ifc #199](https://github.com/Autodesk/revit-ifc/issues/199); CompressiveStrength is a multiline table value instead of a pressure [revit-ifc #534](https://github.com/Autodesk/revit-ifc/issues/534).
- en: IFC volumetric flow is m3/s but users want m3/h [forums.buildingsmart.org](https://forums.buildingsmart.org/t/supported-data-type-volumetricflowrate-m-h/4189).
- en: ClearWidth stored as text "1000 mm" and FireRating "1 hr" [github.com](https://github.com/LUOaini1213/ifcsg-precheck).
- ru: the validator complains that area is IfcArea instead of IfcReal; a global find-and-replace breaks `Pset_*` [habr.com](https://habr.com/ru/articles/1094224/).

**Why it happens.** Revit Yes/No maps to a logical; units are converted from internal units and bugs exist; the measure type in the mapping file must match the schema [forums.autodesk.com](https://forums.autodesk.com/t5/revit-architecture-forum/missing-properties-when-exporting-ifc-from-revit-using-custom/td-p/13217311); units come from `IfcProject.UnitsInContext` unless a property has its own unit ([properties doc, section 1.3](../../01_ifc_basics/05_properties_quantities_psets.md)).

**What fixes it.** Use the full pset-qualified name for logicals (`Pset_BuildingStoreyCommon.AboveGround` per the reference doc), match parameter and property types, keep numbers numeric with the unit carried by the property type.

**What a good AI/MCP assistant should do.** Report the value *with* type and unit, suspect factors of 304.8 or 1000, and refuse to silently convert text like "1000 mm".
**Clarifying questions.** Which unit is the project in? Is the property expected as number, text or boolean? Which schema/version?

### 6. Empty values and "missing vs false"

**Symptoms in users' words**
- en: "Empty parameters are not exported by design; no option today; may change" [revit-ifc #963](https://github.com/Autodesk/revit-ifc/issues/963) (tracked internally as REVIT-249181), repeated by [revit-ifc #963](https://github.com/Autodesk/revit-ifc/issues/963).
- it: *"come verifico che porte e muri abbiano FireRating e trasmittanza prima di consegnare l'IFC?"* (how do I check doors and walls have FireRating and U-value before delivering) [biblus.acca.it](https://biblus.acca.it/bim-validation-modelli-ifc/).
- nl: colour the model by property, "rood voor 'LoadBearing ontbreekt'" (red for LoadBearing missing) [OpenAEC-BIM-validator #17](https://github.com/OpenAEC-Foundation/OpenAEC-BIM-validator/issues/17).
- synthetic prompts show the same need in many languages: de "prüf mal ob bei allen Wänden Tragend, Feuerwiderstand und Außenwand befüllt sind", ru "проверь у всех стен заполнены огнестойкость и марка", zh "查一下牆、門、窗有沒有填防火時效".

**Why it happens.** Empty values are skipped, so the property simply does not exist; a property that is not set means "no value", not FALSE, and IfcLogical also has UNKNOWN ([properties doc, pitfall 3](../../01_ifc_basics/05_properties_quantities_psets.md)). A blank pset is invalid; one tool does not write a pset when one property lacks a value (same doc).

**What fixes it.** Fill values in Revit before export; a validation step (IDS, checker) after export.

**What a good AI/MCP assistant should do.** Report three separate counts: pset absent, property absent, property present but empty/unknown; look at both type and occurrence; never treat missing IsExternal as "internal".
**Clarifying questions.** Which pset and property exactly (and which IFC version)? Check type, occurrence or both? Is "empty" the same as "missing" for your rule?

### 7. Revit data that is hard to map: category, room area, materials, parts, schedules, IfcSystem, phases, quantities

**Symptoms in users' words**
- en: "If I export using Export Revit property sets I see Category, but in my user defined pset txt I tried Category, Revit Category, Category Id, Category Name and nothing comes out" [revit-ifc #960](https://github.com/Autodesk/revit-ifc/issues/960) (open, REVIT-248491).
- en: room area cannot go into a custom pset although the client requires it (works for area plan objects) [revit-ifc #855](https://github.com/Autodesk/revit-ifc/issues/855).
- en: built-in material parameters cannot be exported into standardised psets [revit-ifc #766](https://github.com/Autodesk/revit-ifc/issues/766).
- en: user-defined psets not exported for Parts (also Roof, Stair, Railing) [revit-ifc #662](https://github.com/Autodesk/revit-ifc/issues/662); properties of an IfcSystem cannot be exported [revit-ifc #523](https://github.com/Autodesk/revit-ifc/issues/523).
- en: "Is there any Pset or Parameter for IFC Phasing?" [revit-ifc #704](https://github.com/Autodesk/revit-ifc/issues/704); de: how to get phase created/demolished into IFC [bim-me-up.com](https://bim-me-up.com/revit-phasen-nach-ifc-exportieren/).
- en: ticking schedules-as-psets on the main model made a linked export fail [revit-ifc #882](https://github.com/Autodesk/revit-ifc/issues/882).
- en: some base quantities (NetFootprintArea) are missing [revit-ifc #144](https://github.com/Autodesk/revit-ifc/issues/144); request for quantity parameters [revit-ifc #688](https://github.com/Autodesk/revit-ifc/issues/688).

**Why it happens.** The mapping works on parameters, not on every built-in field; some categories are excluded; base quantities are off by default and custom quantities have no mapping (REVIT-239937).

**What fixes it.** "Export Revit property sets" for built-ins (noisy), schedules as psets with caution, copy values into your own parameter first, enable base quantities, phase through a custom pset, accept tracked gaps.

**What a good AI/MCP assistant should do.** Say honestly which route exists and which is a known gap; avoid promising an export path that the data shows as "open".
**Clarifying questions.** Which built-in value (category, room area, material, phase)? IFC version? Is base quantity export on?

### 8. "Where is my data?" Viewers, readers and scripts

**Symptoms in users' words**
- en: "Properties were actually present in an IFC viewer; Revit just does not display them" [forum.dynamobim.com](https://forum.dynamobim.com/t/ifc-export-missing-empty-properties/74624).
- en: custom NEOM_* parameters missing in the 22.6 output when walked with IsDefinedBy, yet viewers show them [IfcOpenShell #3978](https://github.com/IfcOpenShell/IfcOpenShell/issues/3978); the answer was to use `ifcopenshell.util.element.get_psets`.
- en: `getPropertySets` with `includeTypeProperties=true` returns an empty array [engine_web-ifc #1873](https://github.com/ThatOpen/engine_web-ifc/issues/1873); type properties missing because IFCRELDEFINESBYTYPE is not resolved [engine_fragment #168](https://github.com/ThatOpen/engine_fragment/issues/168).
- en: "Georeferenced IFC2x3 ... cannot find ePset_MapConversion in Bonsai" (they sit on IfcProject) [community.osarch.org](https://community.osarch.org/discussion/comment/29556/).
- en: "How do I get all properties and quantities of IfcDuctSegment instances; unsure how to relate IfcQuantityLength to the element" [IfcOpenShell #3910](https://github.com/IfcOpenShell/IfcOpenShell/issues/3910).
- ja: IfcCSV only writes attributes, wants PropertySet and Material in Excel as well [zenn.dev](https://zenn.dev/miyamiyaumya/articles/19a4247133dde6).
- zh: *"一堵墙的IFC文本里，哪些行是构件本身、哪些是连接关系、哪些是属性集"* (in the IFC text of one wall, which lines are the element, which are relations, which are property sets) [cnblogs.com](https://www.cnblogs.com/pandaNHF/p/16828047.html).

**Why it happens.** A property set is attached by a separate relation entity (`IfcRelDefinesByProperties`); type properties come through `IfcRelDefinesByType`; tools differ in which of these they merge and display.

**What fixes it.** Use a library call that merges both levels, or read the STEP text lines `IFCPROPERTYSET`, `IFCPROPERTYSINGLEVALUE`, `IFCRELDEFINESBYPROPERTIES`, `IFCRELDEFINESBYTYPE`; compare in a second viewer.

**What a good AI/MCP assistant should do.** Distinguish "not in the file" from "not shown by this viewer"; show psets per level; point out psets on IfcProject/IfcSite/IfcBuilding where relevant.
**Clarifying questions.** Which viewer or library? Is it the type or the occurrence you inspect? IFC2x3 or IFC4?

### 9. Naming and validity: Pset_ prefix, duplicates, blank sets, AI-invented names, Name vs Reference

**Symptoms in users' words**
- en: "AI gave me Pset_BuildingElementCommon and put IsExternal on footings; how do I know which property sets are real?" [bimcorner.com](https://bimcorner.com/ai-ifc-properties/).
- nl: *"eigen PropertySet-namen mogen niet met Pset beginnen"* (own property set names must not start with Pset) [digigo.nu](https://www.digigo.nu/ilsen-en-richtlijnen/bim-basis-ils/3-7-gebruik-propertysets).
- en: "can several property sets with the same name be attached to one IfcObject?" [forums.buildingsmart.org](https://forums.buildingsmart.org/t/5049) (not allowed); duplicate sets with the same name are invalid [IfcOpenShell #7095](https://github.com/IfcOpenShell/IfcOpenShell/issues/7095).
- en: "how should Name, Reference and PredefinedType be used in an office workflow (Name = door number vs wall type)?" [forums.buildingsmart.org](https://forums.buildingsmart.org/t/6429); Reference is deprecated in IFC4.3 ([properties doc](../../01_ifc_basics/05_properties_quantities_psets.md), pitfall 8).
- en: calculation software exports IfcMaterial in a custom property set which the BIM manager rejects [community.osarch.org](https://community.osarch.org/discussion/432/how-to-check-if-parameters-in-an-ifc-file-are-compliant-and-editable).
- en: a custom property that applies only to doors of predefined type DOOR [forums.buildingsmart.org](https://forums.buildingsmart.org/t/5779).

**Why it happens.** `Pset_` is reserved for sets defined in the IFC specification; property set names must be unique per object; a language model predicts plausible names rather than looking them up.

**What fixes it.** Use a company prefix (`ACME_...`), look up standard names in the buildingSMART documentation, validate the file.

**What a good AI/MCP assistant should do.** Check a requested name against the standard before using it, say when a name is custom, refuse to invent properties, and tell attributes (`Name`, `ObjectType`) from properties.
**Clarifying questions.** Is this meant to be a standard or a custom set? Which IFC version (names changed between versions)?

### 10. Adding, copying and editing properties inside an IFC file

**Symptoms in users' words**
- en: "Select by type or property, create pset, link with IfcRelDefinesByProperties, write new file" (a tutorial on adding properties with IfcOpenShell) [bimcorner.com](https://bimcorner.com/add-properties-to-ifc-using-ifcopenshell/).
- zh: *"读入IFC文件，按GlobalID找到梁，改名字，加属性集，再写出新文件"* (read the file, find the beam by GlobalId, rename, add a property set, write a new file) [cnblogs.com](https://www.cnblogs.com/herd/p/12183392.html).
- en: in Bonsai, editing attributes then saving removes ObjectType [IfcOpenShell #7259](https://github.com/IfcOpenShell/IfcOpenShell/issues/7259).
- en: Bonsai custom pset documentation is hard to find [community.osarch.org](https://community.osarch.org/discussion/3356/bonsai-defined-custom-psets-documentation-anywhere).
- en: few authoring tools write table or bounded values, the Blender add-on can add custom psets [forums.buildingsmart.org](https://forums.buildingsmart.org/t/3379).

**Why it happens.** A write needs three things: the property set, its properties, and the relation; units, types and shared property entities must be handled; a blank pset is invalid.

**What fixes it.** Use an IFC library API, work on a copy, report every change.

**What a good AI/MCP assistant should do.** Do a dry run first, name the target level (type or occurrence), keep existing psets unless told otherwise, save a new file, and re-read to verify. For a new pset it should pick a non-`Pset_` name.
**Clarifying questions.** Which elements exactly? Property type and unit? Type or occurrence? Where do the values come from (CSV key, rule)? What happens to elements with no match?

### 11. Classification codes in the wrong place

**Symptoms in users' words**
- en: "if I assign ClassificationCode[Type] to a type I expect it on IfcWallType; instead it lands on IfcWall" [revit-ifc #691](https://github.com/Autodesk/revit-ifc/issues/691).
- en: "Revit 2023.1.1 classifications settings are not exported properly", a regression from 22.5.0.0 to 22.5.1.0 [revit-ifc #556](https://github.com/Autodesk/revit-ifc/issues/556).
- en: with several classifications "it is unclear how to add the extra IfcClassification attributes" [revit-ifc #182](https://github.com/Autodesk/revit-ifc/issues/182).
- nl: can the NLCS classification be combined with NL/SfB coding via Assembly Code? [NLCS #38](https://github.com/nl-digigo/NLCS/issues/38).
- en: "bSDD classification mapping and specific pset values": classification properties vs generic properties [forums.buildingsmart.org](https://forums.buildingsmart.org/t/bsdd-classification-mapping-and-specific-pset-values/4538).

**Why it happens.** A classification is an `IfcClassificationReference` attached by a relation, not a pset property ([materials and classification doc](../../01_ifc_basics/07_materials_classification_types_styles.md)); the exporter uses special parameter names and a strict value format.

**What fixes it.** Use the classification settings and parameter format described in the threads; repair afterwards with a script where needed.

**What a good AI/MCP assistant should do.** Ask whether the code should be a property or a classification reference, and check both places.
**Clarifying questions.** Which classification system (Uniclass, NL-SfB, OmniClass, national)? On the type or the occurrence?

### 12. National and contractual property requirements and their checks

**Symptoms in users' words**
- es: *"tabla que asocia parámetro con atributo IFC, Pset y propiedad, requerido u opcional, exportación automática o 'a ingresar'"* (the table linking parameter, IFC attribute, Pset and property, required or optional) [planbim.cl](https://planbim.cl/documentos/mide/).
- no: *"hvilke egenskaper krever NS 8360 i modellen, f.eks. Milestone og IsProcured?"* (which properties does NS 8360 require, e.g. Milestone and IsProcured) [buildingsmart.no](https://www.buildingsmart.no/standarder/kort-forklart.html); MMI coding per milestone [mmi-veilederen.no](https://www.mmi-veilederen.no/).
- zh: audit nodes in the Shenzhen submission tool are empty, meaning fields were lost in export [blog.csdn.net](https://blog.csdn.net/weixin_42855822/article/details/139867051).
- ru: *"числовой параметр не переносится, если не запятая; помещения не классифицируются по МССК"* (a numeric parameter isn't transferred unless it uses a comma; rooms are not classified by MSSK) [habr.com](https://habr.com/ru/articles/1098340/).
- en: units as text and missing required psets in a Singapore pre-check [github.com](https://github.com/LUOaini1213/ifcsg-precheck); EIRs name a property but not its pset while IDS requires the pset [IDS #189](https://github.com/buildingSMART/IDS/issues/189).

**Why it happens.** Every program defines its own mandatory psets, data types and formats; checkers need exact pset + property + type.

**What fixes it.** Obtain the program's mapping file, fix at source (Revit), validate before submission; see the national documents in `02_standards_regulations/national/`.

**What a good AI/MCP assistant should do.** Ask which rule set applies, check against it property by property, and list failures with GlobalId and storey.
**Clarifying questions.** Which program or contract (EIR/BEP, IFC+SG, MIDE, NS 8360, expert review)? Which milestone or stage?

### 13. Non-English parameter names and special characters

**Symptoms in users' words**
- en: Czech-named shared parameters replaced by built-ins [revit-ifc #989](https://github.com/Autodesk/revit-ifc/issues/989).
- en: "IFC metadata is searchable in English but not in Korean" [community.cesium.com](https://community.cesium.com/t/ifc-metadata-not-shown-when-it-is-korean/44612).
- zh: Chinese in the exported IFC becomes `\X2\...\X0\`, a UTF-16 hex escape [blog.csdn.net](https://blog.csdn.net/qq_35042852/article/details/137257689).
- en: a multiline text parameter does not show in IFC4 [revit-ifc #721](https://github.com/Autodesk/revit-ifc/issues/721).
- ru: synthetic prompt (not a real quote): "в свойствах какие-то кракозябры вместо кириллицы, найди где именно и что за кодировка" (see test prompts).

**Why it happens.** Mapping is by name and case-insensitive, so local names can collide with built-ins; IFC text uses escape sequences that some readers decode poorly.

**What fixes it.** Map explicitly instead of relying on automatic name matching, avoid clashes with built-in names, use a reader that decodes `\X2\`.

**What a good AI/MCP assistant should do.** Keep original-language names intact in answers, decode escapes before showing them, and warn about case-insensitive name collisions.
**Clarifying questions.** Which languages are used in parameter names? Which viewer shows broken text?

## Real questions

Language is the language of the original post. English rows are my paraphrase of the stored paraphrase; for other languages the question is the stored original-language paraphrase, except rows marked † where the stored paraphrase was in English and I show the original thread title instead.

| lang | question (original-language paraphrase) | EN gloss | persona | source |
|---|---|---|---|---|
| en | Custom properties in my user-defined property set file don't show up in the exported IFC. | — | bim coordinator | [forums.autodesk.com](https://forums.autodesk.com/t5/revit-architecture-forum/revit-ifc-export-user-defined-properties-won-t-export/td-p/9767878) |
| en | How do I correctly set up user-defined property sets for IFC export? | — | bim manager | [forums.autodesk.com](https://forums.autodesk.com/t5/revit-architecture-forum/ifc-export-user-defined-property-sets/td-p/13167438) |
| en | Only part of my user-defined property set is exported. | — | developer programmer | [forums.autodesk.com](https://forums.autodesk.com/t5/revit-api-forum/ifc-export-only-part-of-user-defined-property-set-are-exported/td-p/10027559) |
| en | Some shared parameters export for one team member and are missing for another. | — | bim coordinator | [help.autodesk.com](https://help.autodesk.com/view/RVT/2025/ENU/?caas=caas%2Fsfdcarticles%2Fsfdcarticles%2FCertain-shared-parameters-not-exportetd-to-IFC-from-Revit.html) |
| en | I pointed "user defined property sets" at the shared parameter file and nothing exported. | — | bim coordinator | [forums.autodesk.com](https://forums.autodesk.com/t5/revit-architecture-forum/revit-ifc-export-user-defined-properties-won-t-export/td-p/9767878) |
| en | Properties from my custom pset mapping TXT are absent in the output. | — | bim coordinator | [forums.autodesk.com](https://forums.autodesk.com/t5/revit-architecture-forum/missing-properties-when-exporting-ifc-from-revit-using-custom/td-p/13217311) |
| en | My custom pset only exports type parameters. | — | bim coordinator | [forums.autodesk.com](https://forums.autodesk.com/t5/revit-architecture-forum/ifc-export-pset-only-type-parameters-exporting/td-p/9555287) |
| en | Type parameters are missing in the IFC property sets after export. | — | bim coordinator | [forums.autodesk.com](https://forums.autodesk.com/t5/revit-architecture-forum/issues-with-exporting-type-parameters-from-revit-to-ifc/td-p/14004505) |
| en | What does the I or T setting in the pset txt file mean? A pset can include both instance and type parameters. | — | student beginner | [revit-ifc #206](https://github.com/Autodesk/revit-ifc/issues/206) |
| en | Classification parameters in my custom pset weren't exported when the entity was IFCElement; IFCRoot worked. | — | bim coordinator | [revit-ifc #879](https://github.com/Autodesk/revit-ifc/issues/879) |
| en | I can't export any Part property with user-defined property sets. | — | bim coordinator | [revit-ifc #662](https://github.com/Autodesk/revit-ifc/issues/662) |
| en | My hidden shared parameters are ignored by the exporter, whichever of three approaches I try. | — | bim coordinator | [revit-ifc #38](https://github.com/Autodesk/revit-ifc/issues/38) |
| en | The Revit 2027 parameter mapping GUI lists only some parameters; project parameters are missing. | — | bim manager | [forums.autodesk.com](https://forums.autodesk.com/t5/revit-architecture-forum/ifc-export-in-2027-mapping-parameters-severely-lacking/td-p/14229702) |
| en | In the new Manage Default Property Sets dialog not all Revit parameters appear; changing the type to Length shows none. | — | bim coordinator | [revit-ifc #984](https://github.com/Autodesk/revit-ifc/issues/984) |
| en | In Revit 2027 how do I add a user-defined property set to the project (IfcProject is missing)? | — | bim manager | [revit-ifc #971](https://github.com/Autodesk/revit-ifc/issues/971) |
| en | Please restore a GUI for mapping project parameters to IFC property sets in 2027. | — | bim manager | [forums.autodesk.com](https://forums.autodesk.com/t5/revit-ideas/gui-for-project-parameter-mapping-in-ifc-export-missing-in-revit/idi-p/14097939) |
| en | I can't overwrite *_Common.LoadBearing with my own parameter; only the built-in value is exported. | — | architect | [revit-ifc #833](https://github.com/Autodesk/revit-ifc/issues/833) |
| en | Czech-named shared parameters (Objem, Plocha) are replaced by built-in Volume/Area despite my mapping file. | — | bim coordinator | [revit-ifc #989](https://github.com/Autodesk/revit-ifc/issues/989) |
| en | Can I map user-defined parameters to IFC common psets and keep the Revit parameter names in my language? | — | bim coordinator | [revit-ifc #735](https://github.com/Autodesk/revit-ifc/issues/735) |
| en | How do I map two different parameters to the same pset property depending on which exists (duct width/height vs diameter)? | — | mep engineer | [revit-ifc #303](https://github.com/Autodesk/revit-ifc/issues/303) |
| en | I can't point Mark and Type Mark at Name; every entity attribute needs its own Ifc parameter. | — | bim manager | [revit-ifc #205](https://github.com/Autodesk/revit-ifc/issues/205) |
| en | My Yes/No parameter AboveGround on Levels isn't exported to Pset_BuildingStoreyCommon (IfcLogical). | — | bim coordinator | [revit-ifc #1020](https://github.com/Autodesk/revit-ifc/issues/1020) |
| en | In a mm project the Pattern pset of a Beam System writes spacing as feet divided by 304.8. | — | developer programmer | [revit-ifc #1015](https://github.com/Autodesk/revit-ifc/issues/1015) |
| en | I type 15 degrees and the IFC says 15.35. | — | structural engineer | [revit-ifc #954](https://github.com/Autodesk/revit-ifc/issues/954) |
| en | Entering PanelWidth 930 mm gives 1 in the IFC; entering the ratio 0.5 gives 0.00164. | — | developer programmer | [revit-ifc #199](https://github.com/Autodesk/revit-ifc/issues/199) |
| en | IFC volumetric flow is m3/s; I want duct flow in m3/h and pipe flow in l/s. | — | mep engineer | [forums.buildingsmart.org](https://forums.buildingsmart.org/t/supported-data-type-volumetricflowrate-m-h/4189) |
| en | Can I export parameters with empty values (NominalValue null) for validation and later editing? | — | bim manager | [revit-ifc #963](https://github.com/Autodesk/revit-ifc/issues/963) |
| en | I can't export room area to a custom property set; the client requires it. | — | bim manager | [revit-ifc #855](https://github.com/Autodesk/revit-ifc/issues/855) |
| en | How do I export the Revit Category as a user-defined property? Family and Type work, Category doesn't. | — | bim coordinator | [revit-ifc #960](https://github.com/Autodesk/revit-ifc/issues/960) |
| en | I can't export built-in material parameters into standardised IFC psets. | — | developer programmer | [revit-ifc #766](https://github.com/Autodesk/revit-ifc/issues/766) |
| en | Linked-model export fails with a non-recoverable error when the main model has schedules-as-psets ticked. | — | bim manager | [revit-ifc #882](https://github.com/Autodesk/revit-ifc/issues/882) |
| en | Some base quantities (e.g. NetFootprintArea) aren't exported to IFC. | — | architect | [revit-ifc #144](https://github.com/Autodesk/revit-ifc/issues/144) |
| en | Some pile property sets are empty after a Dynamo export. | — | developer programmer | [forum.dynamobim.com](https://forum.dynamobim.com/t/ifc-export-missing-empty-properties/74624) |
| en | Walking IsDefinedBy, my custom NEOM_* parameters are missing in the 22.6 output but viewers show them. | — | developer programmer | [IfcOpenShell #3978](https://github.com/IfcOpenShell/IfcOpenShell/issues/3978) |
| en | getPropertySets with includeTypeProperties=true returns an empty array on an IFC2X3 model. | — | developer programmer | [engine_web-ifc #1873](https://github.com/ThatOpen/engine_web-ifc/issues/1873) |
| en | Type properties are missing compared with Solibri; IFCRELDEFINESBYTYPE not resolved? | — | bim coordinator | [engine_fragment #168](https://github.com/ThatOpen/engine_fragment/issues/168) |
| en | Georeferenced IFC2x3: where are my ePset values in Bonsai? | — | bim coordinator | [community.osarch.org](https://community.osarch.org/discussion/comment/29556/) |
| en | How do I get all properties and quantities of IfcDuctSegment instances and relate IfcQuantityLength to the element? | — | researcher academic | [IfcOpenShell #3910](https://github.com/IfcOpenShell/IfcOpenShell/issues/3910) |
| en | AI gave me Pset_BuildingElementCommon and put IsExternal on footings; how do I know which psets are real? | — | bim manager | [bimcorner.com](https://bimcorner.com/ai-ifc-properties/) |
| en | Can several property sets with the same name be attached to one IfcObject or its type? | — | developer programmer | [forums.buildingsmart.org](https://forums.buildingsmart.org/t/5049) |
| en | IDS requires ModelLabel and ModelReference under Pset_ManufacturerTypeInformation but the check says the pset is missing. | — | bim coordinator | [IfcOpenShell #7095](https://github.com/IfcOpenShell/IfcOpenShell/issues/7095) |
| en | How should Name, Reference and PredefinedType be used in an office workflow? | — | architect | [forums.buildingsmart.org](https://forums.buildingsmart.org/t/6429) |
| en | A custom property applies only to IfcDoor.DOOR; can properties apply to some predefined types within a pset? | — | bim manager | [forums.buildingsmart.org](https://forums.buildingsmart.org/t/5779) |
| en | A calculation program exports IfcMaterial in a custom pset which my BIM manager rejects. | — | structural engineer | [community.osarch.org](https://community.osarch.org/discussion/432/how-to-check-if-parameters-in-an-ifc-file-are-compliant-and-editable) |
| en | Doors from Revit show ObjectType but it vanishes after toggling edit attributes. | — | bim coordinator | [IfcOpenShell #7259](https://github.com/IfcOpenShell/IfcOpenShell/issues/7259) |
| en | ClearWidth is "1000 mm" text and FireRating "1 hr"; how do I bulk-fix to numbers? | — | structural engineer | [github.com](https://github.com/LUOaini1213/ifcsg-precheck) |
| en | My EIR names a property but not its pset; IDS requires the pset. How do I write the requirement? | — | bim coordinator | [IDS #189](https://github.com/buildingSMART/IDS/issues/189) |
| en | IfcStair has no direct width property; could Pset_StairCommon get one for code checks? | — | reviewer authority | [IFC4.x-development #976](https://github.com/buildingSMART/IFC4.x-development/issues/976) |
| en | ClassificationCode[Type] lands on the occurrences, not on the type. | — | bim coordinator | [revit-ifc #691](https://github.com/Autodesk/revit-ifc/issues/691) |
| en | Is there any Pset or parameter for IFC phasing? | — | bim coordinator | [revit-ifc #704](https://github.com/Autodesk/revit-ifc/issues/704) |
| en | Two door types share an IsExternal boolean; changing one changes the other. | — | bim coordinator | [community.osarch.org](https://community.osarch.org/discussion/1753/bbim-two-door-types-with-connected-properties) |
| de | † Revit Typenparameter nach IFC exportieren | Exporting Revit type parameters to IFC (they vanished after an exporter update). | bim coordinator | [bim-me-up.com](https://bim-me-up.com/revit-typenparameter-nach-ifc-exportieren/) |
| de | † Revit Phasen nach IFC exportieren | Exporting Revit phases to IFC (how to get phase created/demolished). | bim coordinator | [bim-me-up.com](https://bim-me-up.com/revit-phasen-nach-ifc-exportieren/) |
| de | † IFC Shared Parameters | IFC shared parameters (which to add, and why material layers differ from Revit). | bim coordinator | [bim-me-up.com](https://bim-me-up.com/ifc-shared-parameters/) |
| de | † Materialeigenschaften in IFC | Material properties in IFC (exported, but the viewer shows nothing). | bim coordinator | [bim-me-up.com](https://bim-me-up.com/materialeigenschaften-in-ifc/) |
| de | † IFC Tipp: Revit-Stütze den IsExternal Standardparameter zuweisen | Tip: give a Revit column the standard IsExternal parameter (not filled for columns). | architect | [bim-me-up.com](https://bim-me-up.com/ifc-tipp-revit-stutze-den-isexternal-standardparameter-zuweisen/) |
| it | Come verifico che porte e muri abbiano FireRating e trasmittanza prima di consegnare l'IFC? | How do I verify doors and walls have FireRating and thermal transmittance before delivering the IFC? | bim manager | [biblus.acca.it](https://biblus.acca.it/bim-validation-modelli-ifc/) |
| it | Esporto da Revit ma i parametri custom non finiscono nei Pset, come li mappo? | I export from Revit but my custom parameters don't land in the Psets; how do I map them? | bim coordinator | [biblus.acca.it](https://biblus.acca.it/conversione-modello-bim-in-ifc5/) |
| it | Dove trovo il FireRating di un muro in un IFC e come lo modifico? | Where do I find a wall's FireRating in an IFC and how do I edit it? | student beginner | [ingenio-web.it](https://www.ingenio-web.it/articoli/proprieta-ifc-muro-firerating-pset-wallcommon/) |
| ja | IfcOpenShellのIfcCSVだとAttributeしか書き出せないので、PropertySetとMaterialも一緒にExcelへ出したい | IfcCSV only writes attributes; I want property sets and materials in Excel too. | bim coordinator | [zenn.dev](https://zenn.dev/miyamiyaumya/articles/19a4247133dde6) |
| ja | IFCを可視化できたが形状や属性がどこにどんな形式で入っているのか分からない | I can visualize the IFC but don't know where and in what form shapes and attributes are stored. | developer programmer | [zenn.dev](https://zenn.dev/kiyuka/scraps/48157a38db558e) |
| nl | BIMcollab Smart Views, Dalux-filters en Solibri checking views kleuren op eigenschap: per brandwerendheid, NL-SfB-code, of rood voor 'LoadBearing ontbreekt' | Colour by property in BIMcollab, Dalux and Solibri: per fire resistance, NL-SfB code, or red for "LoadBearing missing". | bim coordinator | [OpenAEC-BIM-validator #17](https://github.com/OpenAEC-Foundation/OpenAEC-BIM-validator/issues/17) |
| nl | Pset_WallCommon: FireRating, LoadBearing, IsExternal; eigen PropertySet-namen mogen niet met Pset beginnen | Pset_WallCommon: FireRating, LoadBearing, IsExternal; own property set names must not start with Pset. | structural engineer | [digigo.nu](https://www.digigo.nu/ilsen-en-richtlijnen/bim-basis-ils/3-7-gebruik-propertysets) |
| no | Hvilke egenskaper krever NS 8360 i modellen, f.eks. Milestone og IsProcured? | Which properties does NS 8360 require in the model, e.g. Milestone and IsProcured? | bim manager | [buildingsmart.no](https://www.buildingsmart.no/standarder/kort-forklart.html) |
| es | Tabla que asocia parámetro con atributo IFC, Pset y propiedad, requerido u opcional, exportación automática o 'a ingresar' | Table linking parameter to IFC attribute, Pset and property, required or optional, automatic export or "to be entered". | bim manager | [planbim.cl](https://planbim.cl/documentos/mide/) |
| ru | Как связать русские параметры Revit с именами свойств IFC | How do I connect Russian Revit parameters with IFC property names? | bim coordinator | [habr.com](https://habr.com/ru/articles/1098340/) |
| ru | Валидатор ругается, что площадь IfcArea а не IfcReal; глобальная замена в блокноте ломает Pset_* | The validator complains area is IfcArea not IfcReal; a global replace in Notepad breaks Pset_*. | bim coordinator | [habr.com](https://habr.com/ru/articles/1094224/) |
| ru | Числовой параметр не переносится, если не запятая; помещения не классифицируются по МССК | A numeric parameter isn't transferred unless it uses a comma; rooms are not classified by MSSK codes. | bim coordinator | [habr.com](https://habr.com/ru/articles/1098340/) |
| ru | Часть свойств потерялась после импорта IFC, какие настройки экспорта выбрать, почему файл не читается | Some properties were lost after IFC import; which export settings, why is the file unreadable? | architect | [blog.rengabim.com](https://blog.rengabim.com/2021/08/ifc.html) |
| ru | Как добавить свойство Renga в экспорт IFC | How do I add a Renga property to the IFC export? | bim manager | [manual.rengabim.com](https://manual.rengabim.com/ehksport_atributov_obektov.html) |
| ru | Арматура неправильно отображается в BIMsight после экспорта, как передать свойства | Reinforcement displays wrongly in BIMsight after export; how to pass the properties? | structural engineer | [forum.dwg.ru](https://forum.dwg.ru/showthread.php?t=150272&page=2) |
| zh | 读入IFC文件，按GlobalID找到梁，改名字，加属性集，再写出新文件 | Read the IFC, find a beam by GlobalId, rename it, add a property set, write a new file. | developer programmer | [cnblogs.com](https://www.cnblogs.com/herd/p/12183392.html) |
| zh | 一堵墙的IFC文本里，哪些行是构件本身、哪些是连接关系、哪些是属性集；空的$字段应该是描述或类型吧 | In the IFC text of one wall, which lines are the element, the connections, the property sets? Are the empty $ fields description or type? | student beginner | [cnblogs.com](https://www.cnblogs.com/pandaNHF/p/16828047.html) |
| zh | 某楼板 楼板:JG-b-200-0现浇:394165 的属性：厚度200、面积19.25、体积3.85、顶标高7200底标高7000 | A slab named Family:Type:ElementId with properties thickness 200, area 19.25, volume 3.85, top level 7200, bottom 7000. | bim coordinator | [cnblogs.com](https://www.cnblogs.com/herd/p/14908387.html) |
| zh | 给IFCMaterial写多个属性集，读出来同一个Pset重复，值不同 | I wrote several property sets to IfcMaterial; reading back, the same Pset repeats with different values. | developer programmer | [ask.csdn.net](https://ask.csdn.net/questions/2665040) |
| zh | Revit导出IFC会丢哪些信息，共享参数、材质、族参数 | What does Revit lose when exporting IFC: shared parameters, materials, family parameters? | bim coordinator | [blog.csdn.net](https://blog.csdn.net/weixin_39590472/article/details/112503752) |
| zh | 自检工具里审查节点有些值是空的，导出IFC丢字段了怎么办 | In the self-check tool some review nodes are empty; the export lost fields, what now? | bim coordinator | [blog.csdn.net](https://blog.csdn.net/weixin_42855822/article/details/139867051) |
| zh | 自定义属性集里的材质导不进IFC | Materials in my custom property set don't reach the IFC. | bim coordinator | [autodesk.com.cn](https://www.autodesk.com.cn/support/technical/article/caas/sfdcarticles/sfdcarticles/CHS/Materials-are-not-exported-to-IFC-with-custom-property-sets-from-Revit.html) |

## Ready test prompts

Curated from the synthetic records (labelled synthetic; none are real quotes). Weak prompts were reworded to sound like a person typing to an assistant. Assume an IFC (or a live Revit session for rows that say so) is loaded.

| lang | prompt | type | difficulty | expected behavior |
|---|---|---|---|---|
| en | revit has FireRating on the walls but Pset_WallCommon.FireRating is empty in the ifc?? which walls, and where does the value live instead | model_task | medium | List walls with empty/absent property, search other psets and type level, report where the value is, not just "missing" |
| en | I added shared params to the doors family, they are in the Revit schedule but not in the ifc. check what psets doors actually have | model_task | medium | List real psets per door (type and occurrence), compare with the expected names, explain likely setup causes |
| en | revit 2027 where did the pset txt go? how do I map project parameters now | how_to | medium | Explain the new mapping dialog vs legacy file, ask Revit/add-in version, mention data-type matching |
| en | how do I write the property set definition txt so type params and instance params both land in one pset? | how_to | easy | Explain I/T flag and type class listing, or two psets; mark syntax as version dependent |
| en | how do i get Revit Category into my user defined pset txt file | how_to | medium | Say it is a known open gap, suggest Revit property sets or copying into an own parameter |
| en | walls have my custom pset on instances but type params missing, check which wall types dont have it | model_task | medium | Check both levels, list types without the pset, mention the type-in-instance option |
| en | do all walls have FireRating in Pset_WallCommon? also check the type not just the instance | model_task | medium | Resolve instance and type psets, report missing per level |
| en | run the usual check: every IfcWall has FireRating, IsExternal and LoadBearing filled? give me fail count per storey | model_task | medium | Per-storey table; separate absent pset, absent property and empty value |
| en | EIR says all doors need FireRating, AcousticRating and Manufacturer. which ones dont have them? need before the issue tonight | model_task | medium | List door GlobalIds with missing items, note Manufacturer lives in Pset_ManufacturerTypeInformation, report levels |
| en | my custom pset length values look way too big like feet to mm, whats wrong, check units on those props | model_task | hard | Compare values to project units, look for factors of 304.8 or 1000, report affected properties |
| en | any door props like ClearWidth with '1000 mm' strings instead of numbers? | model_task | medium | Find text values with units, propose numeric conversion, do not change without confirmation |
| en | list every pset in the model that isnt Pset_ or Qto_, and which classes they sit on | model_task | easy | Table of custom set names by class; flag names starting with Pset_ that are not standard |
| en | any objects with 2 psets of the same name? list them | model_task | medium | Detect duplicate set names per object, explain they are invalid |
| en | add pset ARC_Data to all IfcWall with props LoadBearing (bool) and CostGroup (text) from the Name prefix, dont touch existing psets | model_task | hard | Dry run, derive from Name prefix with confirmation, create set and relations, save as new file |
| en | can you add a property set called Pset_Custom with a field Author to the slab named S-01? first time doing this so tell me what you did | model_task | medium | Warn that the Pset_ prefix is reserved, propose another name, explain the steps taken |
| en | rename property Brandwerendheid to FireRating inside Pset_WallCommon everywhere | model_task | medium | Check for an existing FireRating, confirm, rename, report; do not overwrite values silently |
| en | fill empty IsExternal on walls from the type name containing 'EXT' and save as new ifc | model_task | hard | State it is a heuristic, dry-run list, keep existing values, new file; warn that missing is not FALSE |
| en | where is the NL-SfB / Uniclass code stored, in a pset or IfcClassificationReference? how many elements have none | model_task | medium | Check both, report counts per place |
| en | can u list everything in the ifc that has no property sets, navis shows empty tabs for a bunch of stuff | troubleshooting | medium | List elements without psets by class, mention viewer vs file |
| en | exported from revit but the ifc has no Qto sets at all, only pset stuff. which export setting do I need so my takeoff tool sees areas and volumes | how_to | easy | Explain base quantities option, confirm Qto absent in the file, ask Revit version |
| de | prüf mal ob bei allen Wänden Tragend, Feuerwiderstand und Außenwand befüllt sind, sonst fliegen wir beim AIA-Check raus | model_task | medium | Map German names to LoadBearing, FireRating, IsExternal; list wall GUIDs with gaps |
| de | meine eigenen Parameter kommen in der IFC nicht an obwohl Häkchen bei benutzerdefinierte Psets gesetzt ist, woran liegts | how_to | medium | Walk through file selection, syntax, scope, version, type vs instance |
| de | hat jedes Bauteil die Kostengruppe nach DIN 276 im Pset? zeig mir die ohne | model_task | medium | Find the property, list elements without it |
| es | he exportado a ifc y no me salen los parámetros compartidos en los psets, mira a ver cuáles faltan en los muros | model_task | hard | List wall psets, compare with expected shared parameters |
| es | revisa que todos los muros tengan Pset_WallCommon con FireRating y LoadBearing llenos, lista los vacíos | model_task | easy | Per-wall completeness list |
| es | revisa si el modelo cumple la MIDE de planbim, qué entidades no traen sus propiedades requeridas | model_task | hard | Ask for the MIDE, check required psets/properties per entity |
| fr | pourquoi mes paramètres partagés sortent pas dans l'IFC ? j'ai coché pset personnalisé | troubleshooting | medium | Same checklist as problem 1; ask Revit version and file |
| fr | peux-tu vérifier si toutes les portes ont bien la propriété FireRating et le bon niveau, avant l'export de vendredi | model_task | easy | Door completeness and storey assignment |
| it | da Revit esporto IFC ma i miei parametri condivisi non ci sono nei Pset, perché? | troubleshooting | medium | Checklist, list real psets |
| it | controlla che muri e solai abbiano Pset_Common con IsExternal e LoadBearing, elenca quelli senza | model_task | medium | Per element class completeness list; note Pset_WallCommon vs Pset_SlabCommon names |
| ja | 維持管理用に、機器の名称・メーカー・型番・設置階と室をExcelに出して。空欄の項目も分かるように | model_task | medium | Export a table, mark empty cells, say where each value comes from |
| ja | ドアにタイプ名ごとに分類コード付けたい。D-1→21-21 11みたいな対応表あるからそれで一括で | model_task | medium | Ask where the code goes (classification reference vs property), apply by type with a dry run |
| ja | 部屋名が空のものを一覧にして、変更案を出してから反映してください | model_task | medium | List, propose changes, apply only after confirmation |
| ko | 레빗에서 내보낸 ifc인데 공유 매개변수가 속성에 하나도 안 보여. 어떤 객체에 Pset이 비어있는지 확인해줘 | model_task | hard | List elements with empty/absent psets, mention viewer and setup |
| nl | welke wanden en vloeren missen LoadBearing of IsExternal in Pset_WallCommon? | model_task | easy | Check walls and note slabs use Pset_SlabCommon |
| no | sjekk hvilke objekter som mangler MMI i modellen, grupper per fag og gi meg antall | model_task | medium | Ask where MMI is stored, count per discipline |
| no | sett IsProcured = true på alle prefab betongelementer og lagre ny ifc | model_task | medium | Define "prefab concrete" first, set in the right set, new file |
| pt-BR | exportei do revit e sumiram meus parâmetros compartilhados no IFC. quais elementos ficaram sem pset customizado? | model_task | medium | List elements without the custom set |
| ru | выгрузил в ифс, а мои общие параметры (Марка_ЕСКД, Огнестойкость) куда-то пропали. проверь есть ли они хоть в каких-то псетах у стен | model_task | medium | Search all psets of walls for those names, report where found or absent |
| ru | как сделать чтоб мои параметры семейства уехали в ифс? галка экспорт параметров ревита вроде стоит а пусто | how_to | easy | Explain that the Revit property sets option is not the same as a mapping, check the setup |
| ru | найди в модели все свойства RUS_* где значение лежит как IfcLabel или IfcArea, а не IfcReal, список по элементам с GlobalId | model_task | medium | List by data type, do not touch Pset_* |
| ru | добавь всем дверям свойство огнестойкость из параметра FireRating если оно пустое, остальное не трогай | model_task | medium | Fill only empty ones, report |
| ru | в свойствах какие-то кракозябры вместо кириллицы, найди где именно и что за кодировка | model_task | medium | Find affected names/values, identify escape or encoding, show decoded text |
| zh | 导出的ifc里我自己加的共享参数属性集没了，帮我查下哪些构件有这个属性集 | model_task | medium | List elements having the set, explain setup if none |
| zh | revit里怎么把自定义参数导成ifc属性？要弄txt映射吗 | how_to | medium | Explain mapping options by version |
| zh | 这个ifc里构件名字全是\X2\xxxx\X0\这种，读出来是乱码，帮我看看哪些实体的Name有这个，解码后给我真实中文 | model_task | medium | Find, decode the UTF-16 escape, show original text |
| zh | 查一下牆、門、窗有沒有填防火時效、材料欄位，缺的列出來 | model_task | medium | Completeness list |
| zh | 我有个excel，GlobalId对应设备编码，帮我批量写进模型的自定义Pset_Asset里，写完另存一份 | model_task | medium | Warn about the Pset_ prefix, write under another name, new file, report unmatched ids |

## Edge cases and traps

- **`Pset_` is reserved.** Prompts such as "add Pset_Custom" or "Pset_Asset" should trigger a gentle correction, not silent compliance ([properties doc](../../01_ifc_basics/05_properties_quantities_psets.md), section 5). Renaming a *property* inside a standard set is a different, allowed request but check for collisions.
- **Missing is not false.** An absent `IsExternal` or `LoadBearing` is "no value", not FALSE; Revit may also derive `IsExternal` from the wall function. A rule such as "fill IsExternal from names containing EXT" is a guess and must be labelled so.
- **FireRating is a label.** It is text such as `EI60`/`REI60`/`2HR`, not a number; do not "convert" or compare numerically.
- **Always name the level.** Type vs occurrence for every read and write; shared property entities between types (two door types flipping together) [community.osarch.org](https://community.osarch.org/discussion/1753/bbim-two-door-types-with-connected-properties).
- **Revit parameter in the schedule is not an IFC property.** Hidden parameters, empty values and Parts are not exported [revit-ifc #38](https://github.com/Autodesk/revit-ifc/issues/38), [revit-ifc #963](https://github.com/Autodesk/revit-ifc/issues/963).
- **Version and UI drift.** Instructions for the legacy txt and the 2027 dialog differ; the new mode ignores the legacy checkboxes. Ask the Revit year before step-by-step help.
- **Viewer is not the file.** Some viewers hide type properties or non-standard sets; check the text of the IFC or a second tool [forum.dynamobim.com](https://forum.dynamobim.com/t/ifc-export-missing-empty-properties/74624).
- **Units and types.** Check `UnitsInContext`; suspicious factors are 304.8, 1000, 1,000,000; text such as "1000 mm" is data to fix, not a value to trust [github.com](https://github.com/LUOaini1213/ifcsg-precheck).
- **Blank or duplicated sets are invalid.** A write operation must not leave an empty pset or a second set with the same name on an object [forums.buildingsmart.org](https://forums.buildingsmart.org/t/5049).
- **Classification is not a property.** Ask whether a code belongs in `IfcClassificationReference` or a pset.
- **AI-invented names.** A model may confidently name a pset or property that does not exist [bimcorner.com](https://bimcorner.com/ai-ifc-properties/). Good behavior is to check the schema and admit "I do not know".
- **Local conventions.** `RUS_*`, MMI, MIDE, NS 8360, IFC+SG, МССК are local rule sets with their own mandatory properties; ask which applies.
- **Language and encoding.** Parameter names in Czech, Dutch, Russian, Chinese and Korean collide with built-ins or print as `\X2\` escapes; tests should include such names and expect them to be preserved [blog.csdn.net](https://blog.csdn.net/qq_35042852/article/details/137257689), [community.cesium.com](https://community.cesium.com/t/ifc-metadata-not-shown-when-it-is-korean/44612).
- **Write safety.** Any write should be preceded by a dry-run list, applied to a copy, and verified by re-reading; "save as new file" is the safe default, and an unmatched row (CSV key with no element) must be reported, not skipped silently.
- **Human voice.** Short, lowercase, missing context ("the usual check", "again"), mixed-language property names, typos; tests should include prompts without the pset name, without the IFC class or with only the local-language label.

## Related docs

- [Properties, quantities and psets](../../01_ifc_basics/05_properties_quantities_psets.md)
- [Revit IFC export reference](../../03_software/revit/ifc_export_reference.md)
- [Materials, classification, types, styles](../../01_ifc_basics/07_materials_classification_types_styles.md)
- [IFC in other authoring tools](../../03_software/authoring_tools_ifc.md)
- [Requirements in contracts (EIR/BEP)](../../02_standards_regulations/requirements_in_contracts_eir_bep.md) and [buildingSMART standards (IDS, bSDD)](../../02_standards_regulations/buildingsmart_standards.md)
- National requirement notes: [Singapore](../../02_standards_regulations/national/singapore.md), [Nordics](../../02_standards_regulations/national/nordics_baltics.md), [Netherlands/Belgium](../../02_standards_regulations/national/netherlands_belgium_luxembourg.md), [Russia](../../02_standards_regulations/national/russia.md), [China](../../02_standards_regulations/national/china_mainland.md), [Latin America](../../02_standards_regulations/national/latin_america.md)
- [Libraries and toolkits (IfcOpenShell and others)](../../04_open_source/libraries_and_toolkits.md) and [MCP servers and AI tools](../../04_open_source/mcp_servers_and_ai_tools.md)
- Sister document: [Revit export and class mapping](revit_export_and_class_mapping.md)
