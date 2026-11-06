# Classification systems, bSDD, COBie and FM handover

## In plain words

Four ideas that are easy to confuse:

- **IFC class** (`IfcWall`, `IfcPump`) says what kind of object it is in the IFC language. **Classification** is a second, independent label from an industry catalogue (Uniclass 2015, NL-SfB, OmniClass, Uniformat, the Russian KSI, DIN 276 cost groups...). In IFC it lives in three entities: the *system* (`IfcClassification`, with edition and publisher), the *item/code* (`IfcClassificationReference`) and the link to the object (`IfcRelAssociatesClassification`). Revit has no native classification; people use *Assembly Code*, keynotes or shared parameters, and the IFC exporter has to be told how to turn them into references. See [materials, classification, types](../../01_ifc_basics/07_materials_classification_types_styles.md).
- **bSDD** (buildingSMART Data Dictionary) is an online dictionary where classifications, properties, allowed values, units and translations have stable web addresses (URIs) and an API. It is a reference library, not a checker and not a model editor. See [buildingSMART standards](../../02_standards_regulations/buildingsmart_standards.md).
- **COBie** is a data set for the building *operator*: facility, floors, spaces, zones, types, components, systems, contacts, documents. It is usually delivered as a spreadsheet, but it is really a subset (an MVD) of IFC, and the spreadsheet is a one-way, lossy view of the IFC. See [FM and COBie in the domain overview](../../01_ifc_basics/08_domains_mep_structural_infra_4d5d_fm.md).
- **FM handover** is the act of giving the owner usable asset and space data: room lists, equipment lists with manufacturer, model, serial number and warranty, and a link from each asset to an ID that survives in the FM/CAFM/CMMS system. What exactly to hand over is a *contract* question ([EIR/BEP](../../02_standards_regulations/requirements_in_contracts_eir_bep.md)), not an IFC question.

Most of the pain in the data is of two kinds: (1) the Revit exporter or a viewer put the classification somewhere unexpected (or not at all), and (2) a COBie sheet comes out empty because something upstream (types, containment, systems) was missing, which looks like a tool bug but is usually a data problem.

**Data basis (wave 1).** Topics `classification_bsdd` and `cobie_fm_handover` together hold **244 records**: **148 real** (about 122 distinct source threads) and **96 synthetic** prompts. Real records by language: en 129, nl 10, ru 3, ja 2, es 2, no 1, zh 1. There are **no real de, fr, it, ko or pt questions** on these two topics in wave 1; those languages exist only as synthetic prompts. Sources: GitHub issues 91, forums 43 (buildingSMART, OSArch, Autodesk), blogs 5, official docs 5, regulations 2. Askers: BIM coordinators (38), developers (37), facility managers (22), BIM managers (21), owners/clients (7).

Read the frequency numbers with care: **records are not threads**. Six records are the same Bonsai issue "COBie export - missing Instruction, Impact, Coordinate, Issue, PickLists tabs" and six more are "Cobie export - systems tab empty", because several research cells found them. The "threads" figure below de-duplicates by source URL. The synthetic prompts are skewed to *list-style* FM requests: of 96, about 28 ask for a room/space list, about 17 for an equipment list with manufacturer or serial number, about 39 touch classification coverage or assignment, and about 22 mention handover or FM systems (CAFM, CMMS, GMAO, FDV).

## Problem map

Ranked by real records in this sample (records / distinct threads); numbering matches the "Problems in depth" sections below. "Syn." = rough count of synthetic prompts that touch the topic.

| # | Problem | How users describe it | Frequency signal | Root cause | Typical fix |
|---|---|---|---|---|---|
| 9 | **COBie export from open-source tools incomplete or erroring** (missing tabs, empty Systems, crashes) | "COBie export: 5 of 20 tabs missing"; "Systems tab empty but Bonsai shows 214 systems"; "Error when exporting COBie" | 27 records / 12 threads (en). Six records are one issue, six another. Syn.: about 9 prompts on empty sheets | Exporter does not implement every sheet; COBie needs foreign keys (systems -> components -> types); old BIMserver-plugin bugs | Check types, containment and system membership first; know which sheets the tool implements |
| 4 | **What is a classification, and which IFC class do I pick?** (class vs predefined type vs classification vs bSDD) | "model as IfcDoor, classify with OmniClass, or both?"; "is a bSDD GUID the same as an IFC GUID?"; "best IFC classification for a reducing coupling?" | 16 records / 16 threads (en 14, no, ja) | Several layers describe "what it is"; no global registry of classification systems; people use "classification" for the IFC class choice too | Explain the layers (class, predefined type, user-defined type, reference, property) and who owns what |
| 1 | **Revit IFC exporter writes no / wrong / split classification** | "since the update each Assembly Code gives a different classification"; "classification settings are not exported properly"; "reference created twice" | 13 records / 12 threads (all en, mostly Autodesk/revit-ifc issues 2019-2023). Syn.: about 5 | Exporter regressions between versions; settings that depend on parameter names; relationship name changed in 2022.5.1.0 | Re-test with the exporter version in the BEP; read the classification from the *reference*, not the relationship name; report to Autodesk |
| 10 | **Revit to COBie: parameter mapping, empty fields, scripts that break** | "COBie type/component names are missing from the IFC"; "COBie.Type.Length always empty"; "parameter mapping not working" | 13 records / 10 threads (en). Syn.: about 8 | COBie fields are not auto-populated; setup must be ticked and mapped; empty Revit parameters are not exported; exporter versions change structure | Map a real parameter, tick the type export, export from the right setup, read psets with a helper, not by raw traversal |
| 2 | **Unwanted Uniformat, and getting "code + title" / several systems into IFC** | "we don't use Uniformat, how do I disable it?"; "number and description are two parameters now"; "multiple classifications need ClassificationName(n)" | 10 records / 7 threads (en) | Exporter built around one Uniformat-based system; strict value syntax; localised parameter names | Put the real code in the mapped parameter; concatenate "code : title"; remove the stray Uniformat entity on a copy |
| 7 | **Mapping tables and national systems** (Uniclass <-> OmniClass, NL-SfB, NLCS, KSI, SICLIC, GB/T 51269) | "is there a guide and mapping table for Uniclass 2015 in IFC?"; "семантический разрыв между сущностями требований и данными IFC, привязка к КСИ"; "windveer: code 27 is wrong, should be 47.12" | 10 records / 10 threads (nl 7, ru 2, en 1). Syn.: about 10 | No official 1:1 mapping tables; systems are re-issued several times a year | Use published mappings as hints, show confidence, never present a mapping as official |
| 5 | **bSDD tooling errors, limits and dictionaries** | "No bSDD Props Found for every classification"; "KeyError referenceCode adding NL-SfB"; "API returns only 1000 classes" | 10 records / 9 threads (en) | Rate limit (HTTP 429), IFC2X3 has no `Location`, paging limits, dictionary in "Demo mode", plugin bugs | Back-off/retry, pagination with a dictionary filter, activate the dictionary in bSDD management, create the `IfcClassification` first |
| 11 | **COBie vs IFC+IDS vs MVD, what to put in the EIR; fidelity inside the sheets** | "do we still need COBie or is IFC + IDS enough?"; "how do MVD, IDM, COBie differ?"; "COBie sheet mixes metres and millimetres" | 10 records / 10 threads (en). Syn.: about 8 | COBie is an old spreadsheet format and an MVD; IFC4 changed some mappings (`Pset_Warranty.PointOfContact`); units/dates not normalised | Decide the data list first, then the vehicle (COBie, IFC+IDS, CSV for the CAFM); test a sample |
| 13 | **Asset management at scale, and national handover specs** (Planbim Chile, Nanjing as-built standard, FDV in Norway) | "500+ projects a year, query bridges with certain bearings and their age"; "fichas por modelo con entidades IFC requeridas"; "竣工模型交付用什么格式" | 9 records / 9 threads (en 5, es 2, zh, ja). Syn.: several (no, fr, ja, de) | File-based IFC does not scale to portfolio queries; each owner/country defines its own fields and formats | Database/GIS layer with psets mapped to tables; CSV for field staff first; ask for the owner/national spec |
| 6 | **Checking classification validity, not just presence** | "IDS only checks the pattern of an NL-SfB code, not whether it fits the element" | 8 records / 6 threads (en 6, nl 2). Syn.: about 12 prompts on coverage | IDS Classification facet matches system/value; it has no code list or element-to-code logic; some engines stub the facet | Ship the code list as data; check existence, main group vs IFC class, and where the code is stored |
| 12 | **FM data needs beyond the model** (GlobalId stability, rooms/doors, no-geometry IFC, IoT) | "new phases change GUIDs and break external databases"; "can IFC carry room areas for FM without geometry?" | 5 records / 5 threads (en 4, nl). Syn.: the biggest block, about 28 room-list and 17 equipment-list prompts | FM databases key on IDs the authoring tool may regenerate; FM wants a flat table, IFC is a graph | Pick a stable key (Tag/asset ID, not only GlobalId); define the link schema; produce tables with blanks flagged |
| 8 | **Bulk / rule-based classification** (apply codes from my table) | "rule: non-external load-bearing walls get this code"; "apply the Uniclass codes from my spreadsheet" | 4 records / 4 threads (en). Syn.: about 10 prompts | Writing classification is a modelling operation with many ways to create duplicates; bSDD cannot express property-value rules | Dry-run, exact matches only, one system, work on a copy of the file |
| 3 | **Classification on the wrong object or duplicated** (occurrence vs type, duplicate systems) | "ClassificationCode[Type] ends up on IfcWall, not IfcWallType"; "importing a type duplicates the IfcClassification" | 3 records / 3 threads (en). Syn.: about 4 | Exporter and importer logic treats type vs occurrence differently; each import may create a new system | Check both type and occurrence; merge identical systems; one relationship can carry many objects |

## Problems in depth

### 1. Revit IFC exporter writes no / wrong / split classification

**Symptoms in users' words**
- en: "since latest updates export of classifications like Assembly Code is wrong, I get a different classification for each Assembly code" ([revit-ifc#509](https://github.com/Autodesk/revit-ifc/issues/509); commenters confirm a regression between 22.5.0.0 and 22.5.1.0).
- en: "with the default exporter classification settings go into the IFC, with the open-source exporter 23.1.1 they do not; same in BIMvision, so not a Solibri issue" ([revit-ifc#556](https://github.com/Autodesk/revit-ifc/issues/556)).
- en: "ClassificationCode parameter leads to the same Uniclass 2015 reference assigned twice, invalid IFC" ([revit-ifc#489](https://github.com/Autodesk/revit-ifc/issues/489); maintainers could not reproduce in newer Revit versions).
- en: "Custom pset NL-SfB code is not filled from Classification Code on distribution elements and the pset shows twice in Solibri but once in BIMcollab Zoom" ([revit-ifc#252](https://github.com/Autodesk/revit-ifc/issues/252)).
- en: "Classification manager values to IFC: number and description are two parameters now" ([revit-ifc#456](https://github.com/Autodesk/revit-ifc/issues/456)).

**Why it happens**
Revit has no classification object. The exporter reads *Assembly Code* (Uniformat-based) or a parameter you name in *Classification Settings*, and builds `IfcClassification` plus `IfcClassificationReference` from it. What it writes depends on exporter version and setup. Since revit-ifc 2022.5.1.0 the relationship's `Name` became "Uniformat <code>" rather than "Uniformat Classification"; the maintainer called that by design, but some viewers then showed one tree per code. The lesson in the [reference doc](../../01_ifc_basics/07_materials_classification_types_styles.md): do not read the classification from the relationship name. Many viewers show property sets but not classification references, so users copy the code into a custom pset, which then appears twice or not at all.

**What fixes it**
Test the exact exporter version and setup named in the BEP; keep the Classification Settings tab and parameter names consistent; verify in a viewer that reads references (Solibri, BIMvision) *and* in the raw IFC; repair afterwards with IfcOpenShell where the exporter cannot.

**What a good AI/MCP assistant should do**
Report what is actually in the file: how many `IfcClassification` entities, their `Name`/`Edition`/`Source`, how many references, on types or occurrences. Do not infer the Revit setting from the file alone. Ask: Which Revit and exporter version? Which parameter holds the code (Assembly Code, a shared parameter)? Which system does the client expect?

### 2. Unwanted Uniformat, and getting "code + title" into IFC

**Symptoms**
- en: "we don't use Uniformat, how do I disable it from being exported? it seems to always be there" ([revit-ifc#486](https://github.com/Autodesk/revit-ifc/issues/486)).
- en: "Uniformat is irrelevant in many markets; we use Assembly Code with a custom classification file... Tested in DEU UI, 'Baugruppenkennzeichen' does not work" ([revit-ifc#856](https://github.com/Autodesk/revit-ifc/issues/856); the vendor said resolved, the reporter found localised parameter names still fail).
- en: "Change classification type in IFC: export labels BB/SfB codes as Uniformat" ([Autodesk forum](https://forums.autodesk.com/t5/revit-architecture-forum/change-classification-type-in-ifc/td-p/8579247)); answer: override in the export settings.
- en: "currently multiple classifications need ClassificationName(n) format with strict value syntax" ([revit-ifc#807](https://github.com/Autodesk/revit-ifc/issues/807), open in the vendor's tracker); "how to fill all seven IfcClassification attributes for several classifications?" ([revit-ifc#182](https://github.com/Autodesk/revit-ifc/issues/182)).
- en: "Classification Manager creates number and description parameters; the old way 'number : description' gave Identification and Name" ([revit-ifc#456](https://github.com/Autodesk/revit-ifc/issues/456)); suggested: concatenate into one parameter, as the COBie extension does for `COBie.Type.Category`.

**Why it happens**
The exporter was built around Uniformat and one system. A non-empty Assembly Code makes it write a "Uniformat 1998" classification even when the project uses something else. Parameter names are localised in non-English Revit UIs.

**What fixes it**
Put the real code in the Assembly Code (or the parameter named in the settings), set the system name and edition in the settings, concatenate "code : title" if both must be exported, and delete or ignore the stray Uniformat entity in the delivered file (with consent). See the [Revit IFC export reference](../../03_software/revit/ifc_export_reference.md).

**What a good AI/MCP assistant should do**
List all classification systems present and flag a Uniformat entry the project does not use; offer to remove it and its references on a copy. Ask: Which system should be the only one? Is the title needed as `Name`?

### 3. Classification on the wrong object, or duplicated

**Symptoms**
- en: "if I assign ClassificationCode[Type] to a type I expect it on IfcWallType; instead it lands on IfcWall. broken since 2021" ([revit-ifc#691](https://github.com/Autodesk/revit-ifc/issues/691), open).
- en: "importing types referencing the same IfcClassification creates a new duplicate IfcClassification each time" ([IfcOpenShell#7150](https://github.com/IfcOpenShell/IfcOpenShell/issues/7150)).
- en: "I added several classifications but the dropdown only has one element" ([IfcOpenShell#4612](https://github.com/IfcOpenShell/IfcOpenShell/issues/4612)).

**Why / fix**
A type carries data that every occurrence inherits, so "which elements have no classification?" must look at the occurrence *and* its type. One `IfcRelAssociatesClassification` can carry many objects, and an object can have several systems. Clean-up: one `IfcClassification` per system and edition, one reference per code, associations on the type where the code describes the product.

**What a good AI/MCP assistant should do**
Say whether a code was found on the type, the occurrence, or both; avoid double counting; when asked to "move classification to the type and dedupe", list conflicts (two occurrences of one type with different codes) before changing anything. Ask: Should the code live on types only?

### 4. What is a classification and how does it relate to IFC class, pset and bSDD

**Symptoms**
- en: "model as IfcDoor, classify with OmniClass, or both? Will growing IFC entity vocabulary make OmniClass obsolete?" ([bSI forum](https://forums.buildingsmart.org/t/how-does-ifc-work-with-existing-classification-systems-such-as-omniclass-uniformat-etc/804)); answer: a layered approach: IFC class, predefined type, USERDEFINED `ObjectType`, then `IfcClassificationReference`.
- en: "same thing is described with different values by different authoring tools; propose a published reference table of classification systems, like EPSG" ([bSI forum](https://forums.buildingsmart.org/t/lack-of-standardisation-of-ifcclassification/2581)).
- en: "NL-SfB example maps 22.21 to IFCWall with LoadBearing true, IsExternal false, but browsing the element those values are left open" ([bSI forum](https://forums.buildingsmart.org/t/bsdd-classification-mapping-and-specific-pset-values/4538)).
- en: "is the bSDD GUID the same as the IFC GUID?" ([bSI forum](https://forums.buildingsmart.org/t/bsdd-access-for-products-and-classification-standard-bsdd-guid-vs-ifc-guid/1726)); only the narrow part (property/pset GUIDs match IFC definitions) is answered in the data, so treat the rest as unresolved.
- en: "Best IFC classification for a reducing coupling: CONNECTOR or TRANSITION?" ([bSI forum](https://forums.buildingsmart.org/t/best-ifc-classification-for-a-reducing-coupling/5963)); answer: TRANSITION when the nominal diameter changes. Many askers use "classification" for the choice of IFC class/enum, not for Uniclass-type codes.
- no: "hva er forskjellen på IDS, BCF og bSDD?" (Eng: what is the difference between IDS, BCF and bSDD?) ([bSI Norge](https://www.buildingsmart.no/standarder/kort-forklart.html)).

**Why it happens**
IFC has *classes*, *predefined types*, *properties* and *classification references*, and each answers a different question. bSDD sits beside them: it can say that NL-SfB code 22.21 relates to `IfcWall` and suggest properties, but it does not put anything in your model by itself. Classification systems are edition-dated (`Edition`, `EditionDate`); Uniclass tables change several times a year.

**What a good AI/MCP assistant should do**
Answer in layers: "IfcWall is the class; `PredefinedType` refines it; the Uniclass code is a reference with an edition; the properties are in psets; bSDD is where definitions are published". Never claim a bSDD relation is enforced in the file.

### 5. bSDD tooling errors, limits and dictionaries

**Symptoms**
- en: "adding properties by bSDD classification says 'No bSDD Props Found' for every classification; API returns 429 rate limit" ([IfcOpenShell#7985](https://github.com/IfcOpenShell/IfcOpenShell/issues/7985), fix not merged at the time).
- en: "trying to add NL sfb reference from bSDD gives KeyError referenceCode" ([IfcOpenShell#9034](https://github.com/IfcOpenShell/IfcOpenShell/issues/9034), open).
- en: "Add Classification from bSDD crashes: IfcClassification.Location does not exist in IFC2X3" ([IfcOpenShell#4126](https://github.com/IfcOpenShell/IfcOpenShell/issues/4126), fixed).
- en: "Manual-entry classification reference fails with an error" (you must create the `IfcClassification` first) ([IfcOpenShell#7506](https://github.com/IfcOpenShell/IfcOpenShell/issues/7506)).
- en: "How do I get the whole list of IFC classes from bSDD for an IDS class picker? API returns only 1000" ([bSI forum](https://forums.buildingsmart.org/t/querry-the-whole-list-of-ifc-classes-to-bsdd-for-ids-writing/5395)); answer: dictionary filter plus offset/limit paging (2163 IFC classes); property sets are not bSDD objects.
- en: "the dictionary is registered on the bSDD site but in Demo mode; how do I add the Brazilian SICLIC dictionary?" ([OSArch](https://community.osarch.org/discussion/3680/bsdd-dictionaries)); answer: activate it on the bSDD management page.

**Why it happens**
The public API needs no login but is rate limited; the data model changed names (domain -> dictionary, classification -> class); IFC2X3 lacks `Location`/`Specification`; plug-ins lag behind the API. The Validation Service's own bSDD check has been disabled since v0.6.6, per the [reference doc](../../02_standards_regulations/buildingsmart_standards.md).

**What a good AI/MCP assistant should do**
Treat a failed bSDD call as "lookup failed", never as "no classes found"; retry with back-off; say if it used the live API, a cached copy or its own memory; do not invent a bSDD URI. Ask: Which dictionary and version? Is the IFC2x3? Do you have network access to the API?

### 6. Checking classification validity, not just presence

**Symptoms**
- nl: "IDS controleert alleen het patroon van de NL-SfB code, niet of de code bij het element past; IfcWall met 32.xx is formeel goed en inhoudelijk fout" (Eng: IDS checks only the pattern of the code; an IfcWall with a door code passes) ([OpenAEC-BIM-validator#22](https://github.com/OpenAEC-Foundation/OpenAEC-BIM-validator/issues/22)).
- en: "In IDS classification facet, does a value match any level of a multi-level classification, and what does URI mean?" ([IDS#223](https://github.com/buildingSMART/IDS/issues/223)); answer: the value is checked at any ancestor level.
- en: "IDS Classification and PartOf facets are stubs, so specs using them pass without checking" ([ThatOpen engine_components#830](https://github.com/ThatOpen/engine_components/issues/830)).
- nl: wish to colour elements by NL-SfB code and see "red for LoadBearing missing" ([OpenAEC-BIM-validator#17](https://github.com/OpenAEC-Foundation/OpenAEC-BIM-validator/issues/17)).

**Why / fix**
The IDS Classification facet takes a `system` and optionally a `value`; with the system alone any classification of that system matches; `uri` is documentation only. It has no code list and does not know that "main group 3x" means doors. Validity checks need data: the code table, a mapping from code to expected IFC class, and the location of the code (reference vs pset).

**What a good AI/MCP assistant should do**
Separate three findings: *no code*, *code present but not in the list/malformed*, *code present and valid but unlikely for this class*. Label the third as interpretive. Ask for the code list and edition.

### 7. Mapping tables and national systems

**Symptoms**
- en: "implemented classification with IfcClassification; is there a guide to use UNICLASS 2015 properly, ideally a sample IFC and an existing mapping table?" ([bSI forum](https://forums.buildingsmart.org/t/uniclass-2015-and-ifc/4423)); answer: NBS publishes IFC2x3 mappings; many concepts are not 1:1.
- nl: "In Revit wordt informatie vooral toegekend op basis van NL/SfB via Assembly Code ... Kan NLCS gekoppeld worden aan elementen in Revit?" (Eng: can NLCS be linked to Revit elements, given that data is assigned through NL/SfB in Assembly Code?) ([NLCS#38](https://github.com/nl-digigo/NLCS/issues/38)).
- nl: "windveer is dakafwerking, NL-SfB code 27 is daarom niet juist, moet 47 zijn (47.12)" ([ILS-woco#2](https://github.com/Aedes-datastandaarden/ILS-woco/issues/2)).
- ru: "семантический разрыв между сущностями требований и данными IFC, привязка к КСИ" (Eng: semantic gap between requirement entities and IFC data, tied to the frequently changing KSI classifier) ([Telegram](https://t.me/s/ifc_ru)); the author proposes `IfcClassificationReference` instead of hard-coded codes.
- ru: Moscow TIM requirements contain classification of CIM elements and IFC class mapping appendices ([MKE OD 24-178](https://digest.wizardsoft.ru/wp-content/uploads/media/doc/2025/MKE-OD-24-178Chast3.pdf)).

**Why / fix**
Classification systems differ in scope (elements, products, spaces, cost), in edition and in language; mapping between them or to IFC classes is judgement. National BIM documents (Dutch ILS with 4-digit NL-SfB, Russian KSI/MSSK, Brazilian SICLIC, Chinese GB/T 51269) fix a local choice. See [Netherlands](../../02_standards_regulations/national/netherlands_belgium_luxembourg.md), [Russia](../../02_standards_regulations/national/russia.md), [Latin America](../../02_standards_regulations/national/latin_america.md), [China](../../02_standards_regulations/national/china_mainland.md), [UK/Ireland](../../02_standards_regulations/national/uk_ireland.md).

**What a good AI/MCP assistant should do**
Always state which edition and whose mapping it used, flag ambiguous matches, and refuse to present a guessed mapping as official. Ask: Which system and edition does the client's document name? Do you have the mapping table?

### 8. Bulk and rule-based classification (writing codes into the model)

**Symptoms**
- en: "rule: non-external load-bearing IfcWalls get a given code; I wrote an ifcopenshell+IDS script but suspect a ready solution exists" ([OSArch](https://community.osarch.org/discussion/comment/29871#Comment_29871)); answer: bSDD cannot restrict classification by property values; only IDS can express class+property rules.
- ja (synthetic): "ドアにタイプ名ごとに分類コード付けたい。D-1→21-21 11みたいな対応表あるからそれで一括で" is typical of the many "apply codes from my table" requests.
- en: "IfcCSV: how to export IfcClassificationReference data to CSV; Uniclass code shows 'None' in ItemReference" ([OSArch](https://community.osarch.org/discussion/comment/18591#Comment_18591)).

**Why / fix**
Writing classification is a modelling operation: create or reuse one `IfcClassification` (with edition), create one `IfcClassificationReference` per code, associate to types or occurrences, avoid duplicates, save a new file. IFC2x3 uses `ItemReference` instead of `Identification`.

**What a good AI/MCP assistant should do**
Show a dry-run (matched / unmatched / ambiguous), apply only exact matches, save a copy, re-check counts, and return the unmatched list. Never silently overwrite an existing code. Ask: Types or occurrences? What if an element already has a code from another system?

### 9. COBie export from open-source tools: missing tabs, empty Systems, crashes

**Symptoms**
- en: "COBie export - missing Instruction, Impact, Coordinate, Issue, PickLists tabs" (the spreadsheet from BIMvision and Bonsai lacks 5 of the 20 standard tabs; calls it a nonconformity) ([IfcOpenShell#5926](https://github.com/IfcOpenShell/IfcOpenShell/issues/5926); maintainers later added Coordinate and Systems, the issue stayed open).
- en: "Cobie export - systems tab empty" (214 systems in Bonsai, empty tab in the spreadsheet) ([IfcOpenShell#6068](https://github.com/IfcOpenShell/IfcOpenShell/issues/6068)). The answer: COBie needs foreign keys, systems link to components and components need a type; the model had no types, so the output was correct.
- en: "Error when exporting COBie" (traceback in `cobie24.py`, fixed the same day) ([IfcOpenShell#5702](https://github.com/IfcOpenShell/IfcOpenShell/issues/5702)); "multi-file selection exported to Excel gives error, ODS fine" ([#3901](https://github.com/IfcOpenShell/IfcOpenShell/issues/3901)).
- en (older plug-in): "curtain wall panels and mullions do not appear in the COBie Type and Component sheets" ([COBie-plugins#10](https://github.com/opensourceBIM/COBie-plugins/issues/10)): the FM Handover MVD excludes `IfcPlate`/`IfcMember`; "47 blank rows inserted" ([#13](https://github.com/opensourceBIM/COBie-plugins/issues/13)).

**Why it happens**
A COBie workbook is a set of linked tables (Component -> Type, Component -> Space, System -> Components, Space -> Floor). If an upstream link is missing (no types, elements not contained in spaces, systems without members, everything exported as `IfcBuildingElementProxy`) the downstream sheet is empty or short. Tools also implement different subsets of COBie 2.4 or V3 and different templates (the US OmniClass or the UK Uniclass flavour).

**What fixes it**
Fix the data, not the spreadsheet: add types, containment, system membership; re-export. State which COBie version and template the tool targets.

**What a good AI/MCP assistant should do**
Before blaming the exporter, check the chain: counts of types, components with a type, components in a space, systems with members, proxies. Say which sheets the available tool can write. Ask: COBie 2.4 or V3? US or UK template? Do you need the IFC (MVD) or the spreadsheet?

### 10. Revit to COBie: parameter mapping and empty fields

**Symptoms**
- en: "Mapped COBie data to Revit parameters, exported with the COBie 2.4 Design Deliverable setup, but COBie type/component names are missing from the IFC; do not want to remap" ([bSI forum](https://forums.buildingsmart.org/t/cobie-to-ifc-export-issues/1860)); an answer: export IFC first and extract COBie from the IFC; Revit's default IFC output is weak, audit the IFC classes.
- en: "COBIE.Type.Length, Width, Height always empty" ([Autodesk forum](https://forums.autodesk.com/t5/revit-architecture-forum/cobie-type-length-cobie-type-width-cobie-type-height-is-always/td-p/11009379)); answer: not auto-populated, map a Length-type parameter.
- en: "COBie Type spreadsheet missing families" (the COBie.Type checkbox must be ticked to export a type) ([Autodesk forum](https://forums.autodesk.com/t5/revit-architecture-forum/bim-interoperability-tool-cobie-type-spreadsheet-missing/td-p/9628148)).
- en: "Can Revit export parameters that have empty values, so they can be validated and filled later?" ([revit-ifc#963](https://github.com/Autodesk/revit-ifc/issues/963)); answer: empty parameters are not exported by design.
- en: "Script extracting COBie and custom parameters works for exporter 22.1 but breaks for 22.6" ([IfcOpenShell#3978](https://github.com/IfcOpenShell/IfcOpenShell/issues/3978)); answer: use `ifcopenshell.util.element.get_psets`, the problem was query syntax.

**Why / fix**
Revit has no native "COBie IFC" button; flows use IFC setups (such as the `IFC2x3 COBie 2.4 Design Deliverable` preset with its property-set file) plus the COBie extension or interoperability tools. The presets also turn on 2nd-level space boundaries and bounding boxes. Fields only exist if a parameter is mapped *and* filled.

**What a good AI/MCP assistant should do**
Read the delivered IFC and list the COBie-relevant properties actually present (`Pset_ManufacturerTypeInformation`, `Pset_Warranty`, `Pset_ManufacturerOccurrence`, `Pset_ServiceLife`), with counts of empty/missing; separate "not exported", "exported empty" and "wrong name". Ask: Which Revit setup and COBie extension version? Is the delivery the IFC, the spreadsheet, or both?

### 11. COBie vs IFC+IDS vs MVD, and what to write in the EIR

**Symptoms**
- en: "How do MVD, IDM, COBie and OWL differ and do I have to choose among them?" ([bSI forum](https://forums.buildingsmart.org/t/question-about-mvd-idm-cobie-etc/2762)); answer: IFC is a schema; MVD is a subset for an exchange; COBie is an MVD for FM handover.
- en: "Pset_Warranty.PointOfContact changed type in IFC4 and no longer maps to COBie 2.4 contacts" ([IFC4.x-development#698](https://github.com/buildingSMART/IFC4.x-development/issues/698)).
- en: "experimental COBie support only does Attribute and EntityType facets; cross-sheet checks not possible" ([Xbim.IDS.Validator#11](https://github.com/xBimTeam/Xbim.IDS.Validator/issues/11)).
- en: "COBie sheet mixes metres and millimetres" ([OSArch](https://community.osarch.org/discussion/comment/30246)); "support IfcDate and IfcDuration data types in the exporter" ([revit-ifc#910](https://github.com/Autodesk/revit-ifc/issues/910)).
- en (blog): "never export all parameters, only those in the BEP; FM needs a key linking to an external database" ([BIM Corner](https://bimcorner.com/ifc-export-rules-part-2-what-parameters-to-export-dos-and-donts/)).

**Why / fix**
COBie is a long-standing format (UK COBie 2012 in BS 1192-4, US COBie 2.4; NIBS now publishes V3 with IFC 4.3 mappings); IDS is a newer way to state which properties are required. They are not rivals: IDS states and checks the requirement, COBie (or a CSV for the CAFM) is the container. IFC to spreadsheet is many-to-one, so the reverse is lossy.

**What a good AI/MCP assistant should do**
Help turn "AIM compatible" into an explicit list of required fields per asset class, then check the model against it. Do not claim a COBie spreadsheet can regenerate the IFC. Ask: What does the FM/CAFM system import? Which stage gates require which data?

### 12. FM data needs beyond the model (rooms, equipment, IDs, no-geometry IFC)

**Symptoms**
- en: "New phases change GUIDs and break external databases keyed on them" ([revit-ifc#65](https://github.com/Autodesk/revit-ifc/issues/65)).
- en: "Can IFC hold FM data (room areas, doors, windows, extinguishers) without a full 3D model?" ([OSArch](https://community.osarch.org/discussion/449/ifc-and-input-data-for-facility-management)); yes, a geometry-free IFC with empty objects; COBie wants at least basic coordinates.
- en: "which IFC entity assigns a unique code to each piece of equipment so plumbing, ventilation and electrical items can be identified during O&M?" ([OSArch](https://community.osarch.org/discussion/1118/operation-and-maintenance-on-campus-site-with-ifc)).
- en: "fromRoom/toRoom relation between IfcDoor and IfcSpace for locking systems" ([bSI forum](https://forums.buildingsmart.org/t/relation-between-doors-to-rooms/3961)); answers: `IfcRelConnectsWithRealizingElements` or `IfcRelSpaceBoundary`.
- nl: "manager clicks an installation and sees data, maintenance and reports; GlobalIds must survive versions" ([open-bim-platform#10](https://github.com/OpenAEC-Foundation/open-bim-platform/issues/10)).
- Synthetic (de, fr, ja, ko, zh, ru, pt, no): "room list with number, name, area, floor for the CAFM/GMAO"; "equipment list with manufacturer, model, serial number".

**Why / fix**
An FM system wants flat tables keyed on a stable asset ID; IFC is a graph keyed on GlobalIds that some tools regenerate. Room lists need `IfcSpace` with `Name`/`LongName`, floor containment and `Qto_SpaceBaseQuantities` areas; equipment lists need type data (manufacturer, model) and occurrence data (serial, installation date) and the containing space.

**What a good AI/MCP assistant should do**
Produce the table and flag blanks per column ("14 of 212 spaces have no area; 31 equipment items have no space"). Say which key was used. Ask: Which columns does the CAFM import need? Which ID is the master (Tag, asset code, GlobalId)? Net or gross area?

### 13. Asset management at scale, and national handover specs

**Symptoms**
- en: "US state DOT with 500+ projects/year wants system-wide asset query (e.g., bridges with certain bearings and their age) from as-built IFC" ([OSArch](https://community.osarch.org/discussion/comment/25545)); answers: file-based will not scale; use a database/GIS with psets mapped to tables; IfcSQL stalled; start with simple Excel/CSV for field staff.
- es: "fichas por modelo con entidades IFC requeridas: arquitectura, volumétrico, sitio, MEP eléctrico" (Eng: Chile's Planbim sheets of required IFC entities per model) ([Planbim](https://planbim.cl/documentos/fichas-ifc/)); "tabla que asocia parámetro con atributo IFC, Pset y propiedad, requerido u opcional, exportación automática o 'a ingresar'" ([MIDE](https://planbim.cl/documentos/mide/)).
- zh: "竣工模型交付用什么格式，要在施工图模型基础上加变更信息吗" (Eng: which format for the as-built delivery, and must change information be added to the drawing-review model?) ([Nanjing standard](https://amr.nanjing.gov.cn/ztzl/bzhzl/tzgg/202302/P020230216538033075572.pdf)).
- ja: "BlenderでBIMをいじって安価に施設を管理する" (Eng: managing facilities cheaply with Blender and Bonsai instead of Revit) ([Qiita](https://qiita.com/watanabe-tsubasa/items/bcd3cfbd7dc653a580b5)).

**What a good AI/MCP assistant should do**
Say that single-model tools answer single-model questions; for portfolio queries propose an extraction step (tables per project) and be honest about scale. For national specs, ask for the document and cite it rather than recalling it.

## Real questions

Paraphrases kept in the source language, one row per record (one per thread where possible). The EN gloss is the researcher's English gloss for non-English rows. `--` after a source title separates the thread title from the asker's paraphrase when the paraphrase alone was too thin. Row language is the record's `lang` tag.

### Classification written by the Revit IFC exporter

| lang | question (original language, paraphrased) | EN gloss | persona | source |
|---|---|---|---|---|
| en | since latest updates export of classifications like Assembly Code is wrong, I get a different classification for each Assembly code | — | bim_coordinator | [GitHub Autodesk/revit-ifc#509](https://github.com/Autodesk/revit-ifc/issues/509) `en-uk-anz-india-r007` |
| en | with the default exporter classification settings go into the IFC, with the open-source exporter 23.1.1 they do not; same in BIMvision, so not a Solibri issue | — | bim_coordinator | [GitHub Autodesk/revit-ifc#556](https://github.com/Autodesk/revit-ifc/issues/556) `en-gh-r002` |
| en | Classification Manager creates two parameters (number, description); the old manual way 'number : description' gave Identification and Name in IFC; now it doesn't work. Must I edit all the Excel tables? | — | bim_coordinator | [GitHub Autodesk/revit-ifc#456](https://github.com/Autodesk/revit-ifc/issues/456) `en-gh-r003` |
| en | we don't use Uniformat, how do I disable it from being exported? it seems to always be there | — | bim_manager | [GitHub Autodesk/revit-ifc#486](https://github.com/Autodesk/revit-ifc/issues/486) `en-gh-r004` |
| en | Uniformat is irrelevant in many markets; we use Assembly Code with a custom classification file; need Uniformat suppressed. Tested in DEU UI, 'Baugruppenkennzeichen' does not work | — | bim_manager | [GitHub Autodesk/revit-ifc#856](https://github.com/Autodesk/revit-ifc/issues/856) `en-gh-r005` |
| en | if I assign ClassificationCode[Type] to a type I expect it on IfcWallType; instead it lands on IfcWall. broken since 2021 | — | bim_coordinator | [GitHub Autodesk/revit-ifc#691](https://github.com/Autodesk/revit-ifc/issues/691) `en-gh-r008` |
| en | currently multiple classifications need ClassificationName(n) format with strict value syntax; propose naming the system in the parameter name instead | — | bim_manager | [GitHub Autodesk/revit-ifc#807](https://github.com/Autodesk/revit-ifc/issues/807) `en-gh-r006` |
| en | using AddOption ClassificationName and ClassificationFieldName from Python has no effect; data only exported when set from UI | — | developer_programmer | [GitHub Autodesk/revit-ifc#277](https://github.com/Autodesk/revit-ifc/issues/277) `en-gh-r010` |
| en | Change classification type in IFC. -- Export labels BB/SfB codes as Uniformat. | — | bim_manager | [Autodesk forum](https://forums.autodesk.com/t5/revit-architecture-forum/change-classification-type-in-ifc/td-p/8579247) `en-autodesk-revit-export-r039` |
| en | Classification reference is created twice leading to invalid IFC -- reference assigned twice, only with ClassificationCode parameter | — | bim_coordinator | [GitHub Autodesk/revit-ifc#489](https://github.com/Autodesk/revit-ifc/issues/489) `en-uk-anz-india-r015` |
| en | With 20.2.1 I have 2 issues with a custom property set. The Revit parameter Classification Code isn't exported to the custom property NL-SfB code... The custom property set is shown 2x in Solibri. | — | bim_coordinator | [GitHub Autodesk/revit-ifc#252](https://github.com/Autodesk/revit-ifc/issues/252) `en-ghrevitifc-r010` |
| en | land surveyor new to IFC; should instance parameters be grouped under IFC Parameters when exporting via IfcExportAs, mapping or Classification Manager | — | student_beginner | [bSI forum #3854](https://forums.buildingsmart.org/t/ifc-parameters-in-revit/3854) `en-bsi-r036` |

### Classification and bSDD in Bonsai / IfcOpenShell and the bSDD service

| lang | question (original language, paraphrased) | EN gloss | persona | source |
|---|---|---|---|---|
| en | clicking Add Classification from bSDD gives a traceback at classification.Location = domain.namespace_uri | — | bim_coordinator | [GitHub IfcOpenShell/IfcOpenShell#4126](https://github.com/IfcOpenShell/IfcOpenShell/issues/4126) `en-ios-r016` |
| en | Error when classifying elements using bSDD | — | bim_coordinator | [GitHub IfcOpenShell/IfcOpenShell#4112](https://github.com/IfcOpenShell/IfcOpenShell/issues/4112) `en-ios-r017` |
| en | stumbled across this: trying to add NL sfb reference from bSDD gives KeyError referenceCode | — | bim_coordinator | [GitHub IfcOpenShell/IfcOpenShell#9034](https://github.com/IfcOpenShell/IfcOpenShell/issues/9034) `en-ios-r018` |
| en | I added several classifications but the dropdown only has one element; I expected all added IfcClassifications listed | — | bim_coordinator | [GitHub IfcOpenShell/IfcOpenShell#4612](https://github.com/IfcOpenShell/IfcOpenShell/issues/4612) `en-ios-r019` |
| en | importing types referencing the same IfcClassification creates a new duplicate IfcClassification each time | — | facility_manager | [GitHub IfcOpenShell/IfcOpenShell#7150](https://github.com/IfcOpenShell/IfcOpenShell/issues/7150) `en-ios-r020` |
| en | adding properties by bSDD classification says 'No bSDD Props Found' for every classification; API returns 429 rate limit | — | bim_coordinator | [GitHub IfcOpenShell/IfcOpenShell#7985](https://github.com/IfcOpenShell/IfcOpenShell/issues/7985) `en-ios-r021` |
| en | step list: new file, wall, Classification References, Manual Entry, Add Reference, type Identification/Name, Save - error | — | student_beginner | [GitHub IfcOpenShell/IfcOpenShell#7506](https://github.com/IfcOpenShell/IfcOpenShell/issues/7506) `en-ios-r022` |
| en | manual entry didn't work; the dictionary is registered on the bSDD site but in Demo mode; can I add the JSON file or a link? | — | bim_manager | [OSArch forum](https://community.osarch.org/discussion/3680/bsdd-dictionaries) `en-osarch-r023` |
| en | rule: non-external load-bearing IfcWalls get a given code; I wrote an ifcopenshell+IDS script but suspect a ready solution exists | — | bim_manager | [OSArch forum](https://community.osarch.org/discussion/comment/29871#Comment_29871) `en-osarch-r024` |
| en | docs unclear; with bare 'classification' column I get raw IFC line; with bSDD Uniclass references name exports but code is None | — | researcher_academic | [OSArch forum](https://community.osarch.org/discussion/comment/18591#Comment_18591) `en-osarch-r025` |
| en | Querry the whole list of IFC classes to bSDD for IDS writing -- API returns only 1000 classes; search returns odd matches | — | developer_programmer | [bSI forum #5395](https://forums.buildingsmart.org/t/querry-the-whole-list-of-ifc-classes-to-bsdd-for-ids-writing/5395) `en-val-r011` |
| en | third-party bSDD integrations are clunky; wanted out of the box, like adding properties from shared parameter file but from enabled dictionaries | — | bim_manager | [GitHub Autodesk/revit-ifc#903](https://github.com/Autodesk/revit-ifc/issues/903) `en-gh-r007` |

### What is a classification, how does it relate to IFC classes and bSDD

| lang | question (original language, paraphrased) | EN gloss | persona | source |
|---|---|---|---|---|
| en | model as IfcDoor, classify with OmniClass, or both? will growing IFC entity vocabulary make OmniClass obsolete | — | owner_client | [bSI forum #804](https://forums.buildingsmart.org/t/how-does-ifc-work-with-existing-classification-systems-such-as-omniclass-uniformat-etc/804) `en-bsi-r032` |
| en | same thing is described with different values by different authoring tools; propose published reference table of classification systems | — | developer_programmer | [bSI forum #2581](https://forums.buildingsmart.org/t/lack-of-standardisation-of-ifcclassification/2581) `en-bsi-r033` |
| en | implemented classification with IfcClassification; is there a guide to use UNICLASS 2015 properly, ideally sample IFC, and an existing mapping table? | — | bim_manager | [bSI forum #4423](https://forums.buildingsmart.org/t/uniclass-2015-and-ifc/4423) `en-bsi-r030` |
| en | NL-SfB example maps 22.21 to IFCWall with LoadBearing true, IsExternal false, but browsing the element those values are left open | — | developer_programmer | [bSI forum #4538](https://forums.buildingsmart.org/t/bsdd-classification-mapping-and-specific-pset-values/4538) `en-bsi-r031` |
| en | who links national products to IFC via bSDD; must each implementer build the connection; is bSDD GUID the same as IFC GUID | — | vendor_support | [bSI forum #1726](https://forums.buildingsmart.org/t/bsdd-access-for-products-and-classification-standard-bsdd-guid-vs-ifc-guid/1726) `en-bsi-r037` |
| en | different companies name the same object differently and filters miss objects | — | bim_manager | [BIM Corner blog](https://bimcorner.com/bsdd-the-google-translate-of-bim-world/) `en-blogs-linkedin-r026` |
| en | how do classification systems relate to IFC and do they map directly to the schema | — | developer_programmer | [OSArch forum](https://community.osarch.org/discussion/340/ifc-schema-ontology-semantic-web) `en-osarch-r028` |
| en | coupling joins two segments; with ports of different sizes should it be TRANSITION | — | mep_engineer | [bSI forum #5963](https://forums.buildingsmart.org/t/best-ifc-classification-for-a-reducing-coupling/5963) `en-bsi-r034` |
| en | model garbage disposal and trap as single element assembly; USERDEFINED ObjectType in Revit not settable | — | mep_engineer | [bSI forum #5919](https://forums.buildingsmart.org/t/best-classification-for-an-assembly/5919) `en-bsi-r038` |
| en | Revit IFC 4.3 export places elements under Building domain so infrastructure domains can't filter; could bSDD relationship mapping control it? | — | civil_infra_engineer | [bSI forum #4854](https://forums.buildingsmart.org/t/bsdd-buildingsmart-data-dictionary-and-classification-of-ifc-4x3-domain-mapping/4854) `en-bsi-r035` |
| no | hva er forskjellen på IDS, BCF og bSDD? | Short Norwegian definitions of IDS, BCF, bSDD and openCDE | bim_coordinator | [bSI Norge](https://www.buildingsmart.no/standarder/kort-forklart.html) `no-norway-r011` |
| ja | 全てのopenBIMはbSDDから始まる、というワークフロー整理 | openBIM workflow centered on bSDD with IFC, IDS, BCF, openCDE | bim_manager | [Zenn](https://zenn.dev/miyamiyaumya/articles/fc19330aa071ba) `ja-japan-r026` |

### National systems (NL-SfB, KSI, NLCS) and checking them

| lang | question (original language, paraphrased) | EN gloss | persona | source |
|---|---|---|---|---|
| nl | windveer is dakafwerking, NL-SfB code 27 is daarom niet juist, moet 47 zijn (47.12) | Windveer is roof finishing so NL-SfB code 27 is wrong, should be 47.12 | other | [GitHub Aedes-datastandaarden/ILS-woco#2](https://github.com/Aedes-datastandaarden/ILS-woco/issues/2) `nl-dutch-r001` |
| nl | IDS controleert alleen het patroon van de NL-SfB code, niet of de code bij het element past; IfcWall met 32.xx is formeel goed en inhoudelijk fout. Wil codelijst, koppeling IfcWall->21/22, IfcDoor->31/32 en controle waar de code… | An IDS can check the pattern of an NL-SfB code but not whether the code fits the element; an IfcWall with 32.xx (doors) passes formally | bim_coordinator | [GitHub OpenAEC-Foundation/OpenAEC-BIM-validator#22](https://github.com/OpenAEC-Foundation/OpenAEC-BIM-validator/issues/22) `nl-dutch-r002` |
| nl | In Revit wordt informatie vooral toegekend op basis van NL/SfB via Assembly Code en Assembly Description, bouwkundig ingestoken. Kan NLCS gekoppeld worden aan elementen in Revit? | In Revit info is assigned via NL/SfB Assembly Code and Description; can NLCS codes be linked to Revit elements or integrated with NL-SfB? | bim_coordinator | [GitHub nl-digigo/NLCS#38](https://github.com/nl-digigo/NLCS/issues/38) `nl-dutch-r003` |
| nl | voor uitwisseling van 3D BIM-modellen is een classificatie nodig zoals NL-sfb; onderzoek hoe NLCS aligned kan worden met IFC 4.3, evt via bSDD | Exchanging 3D BIM models needs a classification like NL-SfB; research aligning NLCS with IFC 4.3 and bSDD | developer_programmer | [GitHub nl-digigo/NLCS#147](https://github.com/nl-digigo/NLCS/issues/147) `nl-dutch-r004` |
| nl | Waarom geen verwijzing naar Systems (IfcDistributionSystem)? NL/SfB-codes sluiten niet geheel aan op de praktijk; is classificeren op NL-SfB echt de bedoeling? | Why no reference to IfcDistributionSystem; NL-SfB codes do not fully match practice for installations - is NL-SfB really the intent? | mep_engineer | [GitHub nl-digigo/imwo#52](https://github.com/nl-digigo/imwo/issues/52) `nl-dutch-r014` |
| nl | Analyse Revit-workflow, beschrijving gewenste informatiestructuur, realiseren gewenste output in IFC voor eerste testbatch, testen in IBIS | Experiment: quantity take-off with NLCS classification; analyse Revit workflow, deliver desired IFC output for test batch and test it in IBIS | estimator_qs | [GitHub nl-digigo/NLCS#687](https://github.com/nl-digigo/NLCS/issues/687) `nl-dutch-r015` |
| nl | BIMcollab Smart Views, Dalux-filters en Solibri checking views kleuren op eigenschap: per brandwerendheid, NL-SfB-code, of rood voor 'LoadBearing ontbreekt' | Colour/filter elements by property (fire rating, NL-SfB code, red for 'LoadBearing missing') to see model gaps at a glance | bim_coordinator | [GitHub OpenAEC-Foundation/OpenAEC-BIM-validator#17](https://github.com/OpenAEC-Foundation/OpenAEC-BIM-validator/issues/17) `nl-dutch-r012` |
| ru | семантический разрыв между сущностями требований и данными IFC, привязка к КСИ | Critique of a methodology for digital requirements: semantic gap with IFC data, per-software connectors, tied to the frequently changing KSI classifier | researcher_academic | [Telegram channel](https://t.me/s/ifc_ru) `ru-autodesk-telegram-r023` |
| ru | требования к выгрузке элементов в IFC, соответствие классов IFC категориям | Collection of Moscow TIM requirements includes classification of CIM elements and rules for exporting elements to IFC with class mapping appendices | reviewer_authority | [digest.wizardsoft.ru](https://digest.wizardsoft.ru/wp-content/uploads/media/doc/2025/MKE-OD-24-178Chast3.pdf) `ru-autodesk-telegram-r038` |

### COBie export and conversion

| lang | question (original language, paraphrased) | EN gloss | persona | source |
|---|---|---|---|---|
| en | is it possible to convert ifc to cobie with python? later clarifies: wants to apply an MVD like COBie to get a smaller IFC, spreadsheet optional | — | developer_programmer | [OSArch forum](https://community.osarch.org/discussion/726/how-to-convert-an-ifc-file-to-cobie-using-ifcopenshell-or-other-python-based-solution) `en-cobie-r001` |
| en | asks for a simple standalone utility; remembers BIMserver and Bentley AECOsim from years ago, asks if newer options exist | — | developer_programmer | [GitHub IndustryFoundationClasses/Questions#15](https://github.com/IndustryFoundationClasses/Questions/issues/15) `en-cobie-r004` |
| en | COBie export - missing Instruction, Impact, Coordinate, Issue, PickLists tabs -- compares two xlsx exports of Clinic model | — | facility_manager | [GitHub IfcOpenShell/IfcOpenShell#5926](https://github.com/IfcOpenShell/IfcOpenShell/issues/5926) `en-gh-ifcopenshell-r027` |
| en | exported COBie 2.4 from Bonsai FM tab; Systems sheet empty; IFC private so not shared | — | bim_coordinator | [GitHub IfcOpenShell/IfcOpenShell#6068](https://github.com/IfcOpenShell/IfcOpenShell/issues/6068) `en-cobie-r010` |
| en | Error when exporting COBIe -- pastes traceback only, asks 'Any idea what is happening here?' | — | developer_programmer | [GitHub IfcOpenShell/IfcOpenShell#5702](https://github.com/IfcOpenShell/IfcOpenShell/issues/5702) `en-cobie-r009` |
| en | thesis on COBie delivery for a curtain wall company; edited ignore XML files without effect; items show in Document sheet only | — | student_beginner | [GitHub opensourceBIM/COBie-plugins#10](https://github.com/opensourceBIM/COBie-plugins/issues/10) `en-cobie-r005` |
| en | tested on Dormitory sample project; sorting Type.Name revealed blanks; asks to check all sheets | — | bim_coordinator | [GitHub opensourceBIM/COBie-plugins#13](https://github.com/opensourceBIM/COBie-plugins/issues/13) `en-cobie-r013` |
| en | Bonsai new release! (comment) -- COBie issue where metres and millimetres appear on the same sheet | — | bim_coordinator | [OSArch forum](https://community.osarch.org/discussion/comment/30246) `en-cobie-r022` |
| en | IFC2x3 used a reference to IfcOrganization that COBie 2.4 mapping relied on; IFC4 unclear whether email, name, id or actor | — | developer_programmer | [GitHub buildingSMART/IFC4.x-development#698](https://github.com/buildingSMART/IFC4.x-development/issues/698) `en-cobie-r006` |
| en | experimental COBie support only does Attribute and EntityType facets; cross-sheet checks not possible; proposes Classification->Category, Properties->Attributes, PartOf->containment/systems | — | developer_programmer | [GitHub xBimTeam/Xbim.IDS.Validator#11](https://github.com/xBimTeam/Xbim.IDS.Validator/issues/11) `en-cobie-r007` |
| en | multi-file selection in FM tab exported to Excel gives error log, ODS export fine | — | bim_coordinator | [GitHub IfcOpenShell/IfcOpenShell#3901](https://github.com/IfcOpenShell/IfcOpenShell/issues/3901) `en-fmor-r008` |
| en | How do MVD, IDM, COBie and OWL differ and do I have to choose among them? | — | student_beginner | [bSI forum #2762](https://forums.buildingsmart.org/t/question-about-mvd-idm-cobie-etc/2762) `en-bsmart-r009` |
| en | parity audit vs IfcOpenShell ifcfm; wants COBie 2.4 sheets, missing-field report, fixture checked against COBie rules | — | developer_programmer | [GitHub openbimrs/ifc#477](https://github.com/openbimrs/ifc/issues/477) `en-cobie-r015` |

### COBie from Revit and parameter mapping

| lang | question (original language, paraphrased) | EN gloss | persona | source |
|---|---|---|---|---|
| en | Mapped COBie data to Revit parameters, exported with COBie 2.4 Design Deliverable setup, but COBie type/component names are missing from the IFC; do not want to remap. | — | bim_coordinator | [bSI forum #1860](https://forums.buildingsmart.org/t/cobie-to-ifc-export-issues/1860) `en-us-canada-infra-r001` |
| en | COBIE.Type.Length, COBIE.Type.Width, COBIE.Type.Height is always empty | — | facility_manager | [Autodesk forum](https://forums.autodesk.com/t5/revit-architecture-forum/cobie-type-length-cobie-type-width-cobie-type-height-is-always/td-p/11009379) `en-us-canada-infra-r027` |
| en | Does COBie Extension allow adding extra parameters in Revit -- Can extra parameters be added to COBie export? | — | facility_manager | [Autodesk forum](https://forums.autodesk.com/t5/revit-architecture-forum/does-cobie-extension-allow-adding-extra-parameters-in-revit/td-p/8188015) `en-us-canada-infra-r029` |
| en | Revit Interoperability Tools, Parameter mapping is not working -- Parameter mapping not working in Interoperability Tools. | — | bim_coordinator | [Autodesk forum](https://forums.autodesk.com/t5/revit-architecture-forum/revit-interoperability-tools-parameter-mapping-is-not-working/td-p/11512969) `en-us-canada-infra-r030` |
| en | BIM INTEROPERABILITY TOOL: COBie. Type Spreadsheet missing families | — | bim_coordinator | [Autodesk forum](https://forums.autodesk.com/t5/revit-architecture-forum/bim-interoperability-tool-cobie-type-spreadsheet-missing/td-p/9628148) `en-us-canada-infra-r031` |
| en | wants all parameter types with NominalValue null for validation and later editing | — | bim_manager | [GitHub Autodesk/revit-ifc#963](https://github.com/Autodesk/revit-ifc/issues/963) `en-cobie-r018` |
| en | Script to dump parameters per IFC to Excel behaves differently by Revit IFC exporter version; COBie properties and custom parameters not extracted. | — | developer_programmer | [GitHub IfcOpenShell/IfcOpenShell#3978](https://github.com/IfcOpenShell/IfcOpenShell/issues/3978) `en-us-canada-infra-r013` |

### FM and handover needs (what the owner actually wants)

| lang | question (original language, paraphrased) | EN gloss | persona | source |
|---|---|---|---|---|
| en | asks politely, uncertain, whether IFC can carry room areas, doors, windows and fire extinguishers for FM without geometry | — | facility_manager | [OSArch forum](https://community.osarch.org/discussion/449/ifc-and-input-data-for-facility-management) `en-cobie-r002` |
| en | US state DOT with 500+ projects/year wants system-wide asset query (e.g., bridges with certain bearings and their age) from as-built IFC | — | owner_client | [OSArch forum](https://community.osarch.org/discussion/comment/25545) `en-cobie-r008` |
| en | Does anyone know a similar project? Which IFC entity assigns a unique code to each piece of equipment so plumbing, ventilation and electrical items can be identified during O&M? | — | facility_manager | [OSArch forum](https://community.osarch.org/discussion/1118/operation-and-maintenance-on-campus-site-with-ifc) `en-osarch-gis-r014` |
| en | fromRoom/toRoom relation between IfcDoor and IfcSpace for locking systems | — | facility_manager | [bSI forum #3961](https://forums.buildingsmart.org/t/relation-between-doors-to-rooms/3961) `en-spaces-r029` |
| en | Handling of the Guids when exporting a model for a new phase -- New phases change GUIDs and break external databases keyed on them. | — | facility_manager | [GitHub Autodesk/revit-ifc#65](https://github.com/Autodesk/revit-ifc/issues/65) `en-gh-revit-ifc-r048` |
| nl | manager clicks an installation and sees data, maintenance and reports; data from IFC or COBie; IDS for handover; GlobalIds must survive versions | Facility management app on the as-built model: link assets via GlobalId, maintenance plans, fault reports to ERP work orders, NEN 2767 condition. | facility_manager | [GitHub OpenAEC-Foundation/open-bim-platform#10](https://github.com/OpenAEC-Foundation/open-bim-platform/issues/10) `nl-cobie-r016` |
| en | [Discussion] Efficiency of Continuous IFC Data Updates in BIMserver -- IoT sensors updating IFC; each update creates a new revision | — | developer_programmer | [GitHub opensourceBIM/BIMserver#1327](https://github.com/opensourceBIM/BIMserver/issues/1327) `en-gh-xbim-others-r046` |
| en | which parameters should I export for QS, coordination, construction and FM? | — | bim_manager | [BIM Corner blog](https://bimcorner.com/ifc-export-rules-part-2-what-parameters-to-export-dos-and-donts/) `en-blogs-linkedin-r023` |
| ja | Bonsai as a low-cost alternative for facility management | Managing facilities cheaply with Blender and Bonsai instead of Revit. | facility_manager | [Qiita](https://qiita.com/watanabe-tsubasa/items/bcd3cfbd7dc653a580b5) `ja-qiita-r036` |
| es | fichas por modelo con entidades IFC requeridas: arquitectura, volumétrico, sitio, MEP eléctrico | Chile's Planbim IFC entity sheets per model (architecture, volumetric, site, MEP electrical) | owner_client | [planbim.cl](https://planbim.cl/documentos/fichas-ifc/) `es-latam-r011` |
| es | tabla que asocia parámetro con atributo IFC, Pset y propiedad, requerido u opcional, exportación automática o 'a ingresar' | Planbim information matrix v3.0 maps each parameter to IFC attribute, Pset, property, required/optional, auto/manual export, COBie | bim_manager | [planbim.cl](https://planbim.cl/documentos/mide/) `es-latam-r012` |
| zh | 竣工模型交付用什么格式，要在施工图模型基础上加变更信息吗 | Nanjing local standard for as-built (completion) BIM delivery; format preferably 宁建模. | owner_client | [amr.nanjing.gov.cn](https://amr.nanjing.gov.cn/ztzl/bzhzl/tzgg/202302/P020230216538033075572.pdf) `zh-lightweight-review-r025` |
| ru | как привязать документ и согласование к стенам правкой текста IFC | Link walls to documents and approvals by adding IFCDOCUMENTINFORMATION/IFCRELASSOCIATESDOCUMENT in a text editor | developer_programmer | [Habr](https://habr.com/ru/articles/882890/) `ru-habr-dev-r022` |


## Ready test prompts

All prompts below are **synthetic**: written for testing, modelled on the real patterns above, not real quotes. Several were sharpened from vaguer wave-1 synthetic prompts so they sound like a person under time pressure (lower case, missing context, a deadline, a pasted error). "File" means the prompt assumes an IFC (or Revit project) is loaded. The id in brackets is the wave-1 record each prompt was rewritten from or inspired by.

### Classification and bSDD

| lang | prompt | type | difficulty | expected behavior |
|---|---|---|---|---|
| en | does every element have a classification ref? we need Uniclass, not uniformat | model_task | medium | Counts elements without an `IfcClassificationReference` on occurrence *or* type, lists the systems present (name, edition) and flags Uniformat; reports share per IFC class. (`en-autodesk-revit-export-s009`) |
| en | what classification systems are in this ifc and how many elements use each? flag uniformat if its there | model_task | easy | Lists every `IfcClassification` (Name, Source, Edition), counts related objects via `IfcRelAssociatesClassification`, flags Uniformat. (`en-classbsdd-s001`) |
| en | which walls dont have a uniclass Ss code assigned | model_task | medium | Filters `IfcWall`/`IfcWallType`, checks references whose system is Uniclass and whose code starts with `Ss_`; reports whether a code might sit in a pset instead; returns GUIDs and names. (`en-classbsdd-s002`) |
| en | where is the NL-SfB / Uniclass code stored, in a pset or IfcClassificationReference? how many elements have none | model_task | medium | Looks in both places, reports the counts per place, does not assume; asks which one the client expects. (`en-psets-s008`) |
| en | why does each assembly code have its own IfcClassification entity in this file, should be one | troubleshooting | medium | Counts `IfcClassification` entities and their names, explains the reported exporter regression (22.5.1.0) without claiming it is the cause here, proposes a merge on a copy. (`en-classbsdd-s018`) |
| en | the classification landed on the instances not the types, move it to IfcWallType and dedupe | model_task | hard | For each occurrence with a reference finds its type, lists conflicts (same type, different codes) before acting, moves only consistent ones, saves a new file, reports counts. (`en-classbsdd-s003`) |
| en | strip the uniformat classification, we dont use it. add omniclass table 23 codes from the Assembly Code param instead | model_task | hard | Deletes the Uniformat system and its references (with a preview), creates one OmniClass system, creates references from the given property, reports unmatched values; asks for the edition. (`en-classbsdd-s004`) |
| en | i've got a spreadsheet mapping type names to Uniclass Pr codes. apply them to the types in the model and save a new ifc | model_task | hard | Dry-run first (matched / unmatched / ambiguous), creates one `IfcClassification` and one reference per code, associates to types, writes a new file, returns the unmatched list. (`en-uk-anz-india-s008`) |
| en | add classification ref (Uniclass) to all doors from their type name | model_task | hard | Does not guess a Uniclass code from a name; asks for a mapping table or proposes candidates with confidence labelled "suggested, not official". (`en-graphisoft-s005`) |
| en | whats the diff between IfcClassification and IfcClassificationReference, and where does the bsdd uri go | how_to | easy | System vs item/code; `Location` carries the URI; IFC2x3 has `ItemReference` instead of `Identification` and no `Location` on the system; mentions bSDD dictionary-to-IFC mapping. (`en-classbsdd-s005`) |
| en | api only gives me 1000 classes from bsdd, how do i get all the IFC classes for my IDS picker | how_to | medium | Explains paging with a dictionary filter plus offset/limit (the forum thread cites 2163 IFC classes), notes that property sets are not bSDD objects. (inspired by `en-val-r011`) |
| en | bonsai says 'No bSDD Props Found' for every classification. is bsdd down or is it me | troubleshooting | medium | Mentions the reported HTTP 429 rate limit case, checks connectivity, retries with back-off, says clearly that "found nothing" and "lookup failed" are different; does not invent properties. (inspired by `en-ios-r021`) |
| en | i want every non-external load-bearing wall to get cost group X automatically. bsdd can do that right? | how_to | hard | Says bSDD does not encode "class + property value -> code" rules; this is a script or IDS-driven job; offers a dry-run script. (inspired by `en-osarch-r024`) |
| nl | welke elementen hebben geen NL-SfB code of niet 4 cijfers? lijst per IFC class graag | model_task | medium | Scans classification references and psets for NL-SfB, lists missing/malformed per class with counts, says where each code was found. (`nl-dutch-s002`) |
| nl | check of de NL-SfB codes wel kloppen bij het element, die IfcWall met 32.xx bijv | model_task | hard | Compares code main group to IFC class (walls 21/22, doors 31/32 as in the source discussion), reports mismatches, states the mapping is interpretive and needs a code list. (`nl-dutch-s003`) |
| ru | проверь у всех элементов есть код КСИ? выгрузи тех, у кого нет | model_task | medium | Finds `IfcClassificationReference` with the KSI system name (or a KSI property), lists elements without, grouped by IFC class; states which system name it matched. (`ru-classbsdd-s007`) |
| ru | код классификатора из параметра ревита не попадает в ифс, в настройках экспорта указал, а в IfcClassificationReference пусто. почему | troubleshooting | medium | Reports whether any references exist, checks the system and parameter name pattern, lists exporter-side causes (parameter name/localisation, version, setting); does not claim to see Revit settings. (`ru-classbsdd-s008`) |
| ru | проставь код МССК помещениям по названию, где неоднозначно - не трогай, выведи список | model_task | medium | Applies codes only on exact name matches, leaves ambiguous ones untouched and lists them. (`ru-habr-dev-s013`) |
| zh | 按GB/T 51269分类编码把构件分组，统计墙和板的体积 | model_task | medium | Groups by the classification reference, sums volumes from `Qto_*BaseQuantities`, reports elements without code or volume. (`zh-classbsdd-s009`) |
| de | hat jedes Bauteil eine Kostengruppe DIN 276? zeig mir die ohne KG | model_task | medium | Lists elements without a DIN 276 classification reference, grouped by IFC class, states how the KG code was recognised. (`de-classbsdd-s013`) |
| pt | adiciona a classificação SICLIC nas paredes pelo nome do tipo, tabela que te passei | model_task | hard | Creates the SICLIC system, references per wall type from the table, reports unmatched; mentions the edition and the bSDD dictionary status if relevant. (`pt-classbsdd-s012`) |
| fr | comment je rattache mes éléments à un dictionnaire bSDD dans l'ifc ? | how_to | easy | Explains `IfcClassificationReference` with the bSDD class URI, the dictionary-to-`IfcClassification` mapping, and a check of the result. (`fr-classbsdd-s014`) |
| ja | ドアにタイプ名ごとに分類コード付けたい。D-1→21-21 11みたいな対応表あるからそれで一括で | model_task | hard | Creates the classification system and references from the supplied table by type name, assigns to each door type, reports unmapped types. (`ja-japan-s009`) |
| ko | 분류체계 코드 없는 부재 찾아서 리스트 뽑아줘 | model_task | easy | Lists elements without classification references with GUID and name, by IFC class. (`ko-classbsdd-s016`) |

### COBie, FM handover and asset data

| lang | prompt | type | difficulty | expected behavior |
|---|---|---|---|---|
| en | we owe COBie to the owner friday. check the ifc for type names, component names, spaces w/o floor, systems empty. what will fail the QC | model_task | medium | Verifies Type/Component/Space/Floor/System population, lists missing or duplicate names, orphan spaces and empty systems; summarises likely COBie QC failures; says it is not the official QC tool. (`en-us-canada-infra-s002`) |
| en | handover is friday, which equipment in the ifc has no type or space or manufacturer? cobie wants all 3 | model_task | medium | Lists equipment occurrences lacking a type, a containing space, or `Pset_ManufacturerTypeInformation.Manufacturer`; counts and names. (`en-cobie-s001`) |
| en | my cobie systems sheet is empty but theres loads of ductwork, whats missing in the model | troubleshooting | hard | Inspects `IfcSystem` and `IfcRelAssignsToGroup`, explains that COBie systems need member components and components need types; lists unassigned MEP elements; reports proxies. (`en-cobie-s002`) |
| en | bonsai shows 214 systems but my cobie systems tab is empty, check why | troubleshooting | hard | Lists systems and members, checks types on members, reports the likely cause (members without types) rather than blaming the exporter. (`en-gh-ifcopenshell-s010`) |
| zh | COBie导出来Component表是空的，是不是设备全变成IfcBuildingElementProxy了 | troubleshooting | medium | Counts proxies and untyped elements, explains that Component rows need typed equipment, points to the class-mapping fix. (`zh-cobie-s008`) |
| en | usace job wants COBie. do i export ifc then convert or use the cobie extension? which IFC version | how_to | medium | Explains the two routes, says the project spec decides the IFC version/MVD and COBie version, mentions the Design Deliverable preset and parameter mapping, recommends a small test export. (`en-us-canada-infra-s011`) |
| ru | как из ревита выгрузить кобай чтоб наш cafm его проглотил? ставил плагин, ругается на Type.Name | troubleshooting | medium | Explains mandatory fields and unique `Type.Name`, parameter mapping, CAFM template; asks for the exact plug-in message. (`ru-cobie-s006`) |
| en | do we still need cobie or is ifc + ids enough for our FM system handover | how_to | medium | Compares the vehicles (COBie spreadsheet/MVD, IFC with required psets checked by IDS, CSV for the CAFM), says to define the field list first, suggests asking what the FM system imports. (`en-fmor-s011`) |
| en | what do we actually need to hand over for asset info, COBie or IFC with psets? client's EIR just says 'AIM compatible' | how_to | easy | Explains the AIM idea under ISO 19650, says "AIM compatible" is not a field list, suggests an explicit per-class list and asks the client. (`en-uk-anz-india-s013`) |
| de | was muss ich in die AIA schreiben damit wir vom Bauherrn ne brauchbare IFC für den Betrieb kriegen? COBie oder was anderes | how_to | medium | Lists asset attributes per class (manufacturer, model, serial number, warranty, space), explains the FM handover MVD vs COBie, suggests IDS-based wording. (`de-cobie-s010`) |
| en | could you pull all equipment with manufacturer, model and serial number for our FM system | model_task | medium | Lists equipment with `Pset_ManufacturerTypeInformation` (type) and `Pset_ManufacturerOccurrence` (serial) fields, flags blanks, states where each value was found. (`en-reddit-s011`) |
| en | pull out a COBie style Type and Component list from this IFC - name, category, manufacturer, serial no, space. just spot check for now | model_task | medium | Maps types and occurrences to COBie columns, flags empty fields, returns a table; says it is a spot check, not a conformant workbook. (`en-uk-anz-india-s003`) |
| en | take serials.csv and put SerialNumber + WarrantyEndDate on all IfcUnitaryEquipment matched by tag, then tell me what didnt match | model_task | hard | Matches by `Tag`, writes `Pset_ManufacturerOccurrence.SerialNumber` and `Pset_Warranty` dates (with correct date type), saves a new file, reports unmatched rows both ways. (`en-cobie-s003`) |
| en | add warranty duration 5y and service interval 12 months to all fire dampers | model_task | medium | Selects fire-damper types/occurrences, adds the properties (asks where: type or occurrence), confirms the count changed, saves a copy. (`en-fmor-s010`) |
| en | need a room list for the CAFM: space number, name, floor, net area, one row each | model_task | easy | Exports `IfcSpace` with number, name, storey, `NetFloorArea` from `Qto_SpaceBaseQuantities`; flags blanks and duplicate numbers. (`en-cobie-s004`) |
| de | prüf mal ob jeder Raum eine Raumnummer und NGF hat, sonst klappt der CAFM-Import nicht | model_task | easy | Lists spaces missing number, `LongName` or net area, and duplicate numbers; asks which area definition the CAFM expects. (`de-cobie-s009`) |
| en | furniture sits under storeys not spaces, FM says rooms are empty. confirm? | model_task | medium | Counts `IfcFurnishingElement` by container (storey vs space), reports the share, explains the difference. (`en-blogs-linkedin-s009`) |
| fr | sors moi la liste des locaux avec surface, niveau et nom pour la GMAO, et dis moi lesquels n'ont pas de surface | model_task | easy | Space table with name, level, area; separate list of spaces without area. (`fr-gis-s015`) |
| no | har alle tekniske komponenter FDV-info og NS 3451-kode? vil ha liste over de som mangler | model_task | medium | Checks equipment for a classification reference and maintenance properties, lists gaps; states which code system it matched. (`no-norway-s006`) |
| ja | 維持管理用に、機器の名称・メーカー・型番・設置階と室をExcelに出して。空欄の項目も分かるように | model_task | medium | Queries equipment, reads manufacturer/model properties, containing storey and space, writes a table, marks blanks. (`ja-japan-s011`) |
| ko | 시설관리 시스템에 엑셀 올리면 오류 나는데 어느 행이 문제인지 찾아줘, 자산코드 중복인가? | troubleshooting | medium | Checks the exported table for duplicate asset codes and blank mandatory fields, lists offending rows; asks for the system's error text. (`ko-cobie-s015`) |
| pt | tem como ver quais elementos tao sem os campos obrigatorios do cobie? preciso entregar pro cliente | model_task | medium | Validates component/type/space required attributes and reports missing by sheet; asks which COBie version. (`pt-cobie-s012`) |
| es | para la entrega a mantenimiento, comprueba que los equipos tengan marca, modelo y numero de serie | model_task | medium | Checks `Pset_ManufacturerTypeInformation` and serial number on equipment, reports gaps by class. (`es-spain-s011`) |
| en | which doors connect which rooms? FM needs from-room and to-room for the locking system | model_task | hard | Looks for `IfcRelSpaceBoundary` or realizing-element relations; says if space boundaries were not exported (typically a setup option), does not guess from geometry silently. (inspired by `en-spaces-r029`) |
| en | the new phase export changed all our guids, our CMMS links are dead. how do we match old to new | troubleshooting | hard | Explains GlobalIds can be regenerated per export/phase; proposes matching on Tag/asset code, type+name+location with confidence, and recommends a stable key going forward. (inspired by `en-gh-revit-ifc-r048`) |

## Edge cases and traps for MCP testing in this area

**Classification**

1. **Type vs occurrence.** "Which elements have no classification?" must look at the occurrence *and* the type. A server that checks only one will give opposite answers on the same model (see [revit-ifc#691](https://github.com/Autodesk/revit-ifc/issues/691)).
2. **Do not read the classification from the relationship name.** Since revit-ifc 2022.5.1.0 the `IfcRelAssociatesClassification` name is "Uniformat <code>". Read `IfcClassificationReference.Identification` and its `ReferencedSource`.
3. **IFC2x3 vs IFC4/4.3 attribute names.** `ItemReference` became `Identification`; `Location` is missing on the IFC2x3 system (it crashed a bSDD add, [IfcOpenShell#4126](https://github.com/IfcOpenShell/IfcOpenShell/issues/4126)); `Specification` is the IFC4.3 URI attribute.
4. **Code in a reference or in a pset?** Both patterns exist in practice (the reference doc on Dutch practice notes `IfcClassificationReference`, and, in many Revit setups, a text parameter mapped into a property set). Report where the code was found; ask what the client expects.
5. **Presence, validity, plausibility.** Three different checks. "Has a code" is not "code exists in edition X" is not "code fits this class". Label the third as interpretive.
6. **Editions.** Uniclass tables change several times a year; KSI was updated; OmniClass tables are numbered. Never silently mix editions or answer "valid" without the edition.
7. **Stray Uniformat.** A non-empty Assembly Code can add a Uniformat entity the project never asked for. Do not report the project as "Uniformat-classified" without checking intent.
8. **Mapping tables.** Matching is brittle: `Ss_25_10_30` vs `Ss 25 10 30`, OmniClass tokens (`23-17 11 11`), case, trailing spaces. Report unmatched and ambiguous rows; never fill gaps by guessing.
9. **Hallucinated codes and titles.** LLMs invent plausible Uniclass/NL-SfB/KSI/DIN 276 codes and titles. Only use codes present in the file or in a supplied/queried table, and name the source.
10. **bSDD availability.** HTTP 429, offline, test vs production endpoint (the test server has no SLA), dictionary in Demo mode, paging beyond 1000 results. A failed lookup must not be reported as "class does not exist". Do not fabricate a bSDD URI.
11. **bSDD is not a rule engine and not a validator.** It cannot say "load-bearing external walls get code X"; the Validation Service's bSDD check has been disabled since v0.6.6; a bSDD URI in an IDS is metadata and is not checked.
12. **IDS Classification facet quirks.** System-only matches any classification of that system; value is tested at any ancestor level; some engines treat the facet as a stub and pass everything. Report engine and version.
13. **Writing classification.** Reuse an existing `IfcClassification`; create one reference per code; do not create a new system per import (duplicate-on-import bug, [IfcOpenShell#7150](https://github.com/IfcOpenShell/IfcOpenShell/issues/7150)); save a copy.
14. **Language and locale.** NL-SfB, КСИ/МССК, DIN 276 "KG", GB/T 51269, SICLIC; localised Revit parameter names ("Baugruppenkennzeichen"). Keep code strings and class names untouched in answers in any language.

**COBie and FM**

15. **"COBie" is ambiguous.** Spreadsheet vs IFC MVD; COBie 2.4 vs V3; UK COBie 2012 vs US; US OmniClass or UK Uniclass template; the "20 sheets" include optional ones (Instruction, Impact, Issue, PickLists). Ask which one before claiming conformity.
16. **Empty sheet = broken upstream link.** Empty Systems, empty Components, empty Types usually mean missing types, containment, system membership or proxies. A good answer walks the chain.
17. **Many-to-one and lossy.** IFC to COBie spreadsheet cannot be reversed. Do not offer to "convert the spreadsheet back to IFC".
18. **Names and IDs must be unique and present.** Duplicate `Type.Name`, spaces all called "Room", duplicate asset codes: typical reasons a CAFM import or COBie QC fails.
19. **Empty parameters are not exported by Revit.** "Missing" can mean "never filled" or "not exportable by design" ([revit-ifc#963](https://github.com/Autodesk/revit-ifc/issues/963)).
20. **Units and dates.** Metres vs millimetres in the Coordinate sheet; `IfcDate`/`IfcDuration` support; warranty date types. State the unit used.
21. **Stable keys.** GlobalIds can change between exports/phases; `Tag` and asset codes are usually safer for FM links. State which key a table uses.
22. **Area definitions.** NetFloorArea vs GrossFloorArea; NGF/BTA/NTA are national definitions. Ask which one the owner means.
23. **Space containment and boundaries.** Furniture contained in a storey is not "in the room"; door-to-room links need space boundaries or explicit relations, often a non-default export option.
24. **Write operations from CSV.** Match key (Tag), unmatched rows in both directions, date types, no overwrite, new file, re-read to verify.
25. **Scale and honesty.** One-file MCP servers answer one-file questions; "all our bridges" needs an extraction pipeline. Do not pretend otherwise.
26. **Deadline pressure.** "Handover is Friday" prompts invite overconfidence. The assistant should still say what it did not check (no official COBie QC, no CAFM import test).

## Related docs

- [Materials, classification, types, styles](../../01_ifc_basics/07_materials_classification_types_styles.md) (section 4: classification entities, systems, bSDD mapping rule)
- [Domain overviews: FM and COBie](../../01_ifc_basics/08_domains_mep_structural_infra_4d5d_fm.md) (section 7: COBie sheets and IFC mapping, assets, tools)
- [Properties, quantities and psets](../../01_ifc_basics/05_properties_quantities_psets.md) and [spatial structure](../../01_ifc_basics/04_spatial_structure_and_relationships.md) (spaces, containment, zones, systems)
- [buildingSMART standards: bSDD, IDS Classification facet, Validation Service](../../02_standards_regulations/buildingsmart_standards.md)
- [Requirements in contracts (EIR, BEP, LOIN, classification and COBie wording)](../../02_standards_regulations/requirements_in_contracts_eir_bep.md)
- [ISO and European standards](../../02_standards_regulations/iso_and_european_standards.md)
- [Revit IFC export reference](../../03_software/revit/ifc_export_reference.md) (Classification Settings tab, Assembly Code, COBie presets)
- [Authoring tools and IFC](../../03_software/authoring_tools_ifc.md); [viewers, checkers, CDEs, converters](../../03_software/viewers_checkers_cde_converters.md)
- [Libraries and toolkits](../../04_open_source/libraries_and_toolkits.md) (IfcOpenShell, IfcTester, ifcfm) and [MCP servers and AI tools](../../04_open_source/mcp_servers_and_ai_tools.md)
- National context: [Netherlands/Belgium/Luxembourg](../../02_standards_regulations/national/netherlands_belgium_luxembourg.md) (NL-SfB, NLCS, ILS), [UK/Ireland](../../02_standards_regulations/national/uk_ireland.md) (Uniclass, COBie UK), [Russia](../../02_standards_regulations/national/russia.md) (KSI), [China](../../02_standards_regulations/national/china_mainland.md) (GB/T 51269), [Nordics](../../02_standards_regulations/national/nordics_baltics.md), [Latin America](../../02_standards_regulations/national/latin_america.md) (Planbim), [North America](../../02_standards_regulations/national/north_america.md) (OmniClass, COBie US), [Germany/Austria/Switzerland](../../02_standards_regulations/national/germany_austria_switzerland.md), [Japan/Korea](../../02_standards_regulations/national/japan_korea.md), [Spain/Portugal/Italy](../../02_standards_regulations/national/spain_portugal_italy.md)
- Sibling topic pages: [Validation, model checking and IDS](./validation_ids_model_checking.md), [Revit export and class mapping](./revit_export_and_class_mapping.md)
- Glossary: [multilingual glossary](../../08_glossary/glossary_multilingual.md), [abbreviations](../../08_glossary/abbreviations.md)
- Raw research behind this page: `research_raw/wave1/topics/t-classification-bsdd.md`, `research_raw/wave1/topics/t-cobie-fm.md`, `research_raw/wave1/roles/p-fm-owner-reviewer.md`
