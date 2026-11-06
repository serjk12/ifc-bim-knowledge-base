# Validation, model checking and IDS

## In plain words

"Checking an IFC model" means three different things, and people mix them up all the time:

1. **Is the file valid IFC?** (syntax and schema rules: no broken text, no impossible attribute values, a GlobalId that really is a GlobalId). The official referee is the buildingSMART Validation Service; IfcOpenShell has a local validator too. This says nothing about your project.
2. **Does the model contain what the client asked for?** ("every door has a fire rating", "every wall carries a Uniclass code"). This is the job of **IDS** (Information Delivery Specification, an XML file with machine-readable requirements), of Solibri-style rule sets, or of a home-made script.
3. **Do the parts fit together?** (clashes, duplicate elements, shared origin and units across the federated models). This is coordination checking and is mostly outside IDS.

A file can pass 1 and fail 2, pass 2 and fail 1, and still be a mess for 3. Most of the pain in the data comes from people (or tools, or AI assistants) answering the wrong one of these questions, or from checkers that disagree with each other. See [buildingSMART standards: IDS and the Validation Service](../../02_standards_regulations/buildingsmart_standards.md), [viewers, checkers, CDEs](../../03_software/viewers_checkers_cde_converters.md) and how requirements are written into contracts in [EIR/BEP requirements](../../02_standards_regulations/requirements_in_contracts_eir_bep.md). Unfamiliar words are in the [glossary](../../08_glossary/glossary_multilingual.md) and [abbreviations](../../08_glossary/abbreviations.md).

**Data basis (wave 1).** Topics `validation_checking` and `ids_requirements` together hold **362 records**: **229 real** (about 200 distinct source threads) and **133 synthetic** prompts. Real records by language: en 172, ru 22, ja 10, zh 8, nl 5, it 4, no 4, de 2, ko 1, es 1. There are **no real fr, pt or es questions on this topic** in wave 1; those languages appear only in synthetic prompts. Sources are mostly GitHub issues (84) and forums (84: buildingSMART, OSArch, Autodesk, Dynamo), then blogs (33). The asker is most often a BIM coordinator (80), developer (53) or BIM manager (49). Frequency numbers below count *records in this sample*, not market prevalence, and the same thread can appear as several records, so "threads" is given next to "records".

Two quirks of the source data to keep in mind: (a) a few non-English records have an English `question_paraphrase` because the researcher summarised a foreign-language page in English (e.g. the German IFC 5 blog); (b) many IDS threads are written by people who already know what a "facet" is, so the *beginner* voice is under-represented here. Beginner phrasing is better covered by the synthetic prompts below.

## Problem map

Ranked by how often the problem shows up in the real records of this sample (records / distinct threads). "Syn." = rough share of the 133 synthetic prompts that touch it.

| # | Problem | How users describe it | Frequency signal | Root cause | Typical fix |
|---|---|---|---|---|---|
| 1 | **IDS does not behave as the author expects** (wildcards, PredefinedType, skipped vs failed, data types, unknown pset) | "IDS applicability IFCELEMENT never passes"; "spec shows skipped, how make it fail?"; "EIR names the property but not the pset" | 37 records / 33 threads (all en: bSI forum, IDS repo, OSArch, IfcOpenShell). Syn.: about 22 prompts mention IDS | IDS is strict by design: uppercase, non-inheriting entity names; attribute facet reads the literal stored value; cardinality sits on applicability; a value needs a data type | List concrete subclasses; use the Entity facet's `predefinedType`; set `minOccurs/maxOccurs`; give the right data type; split into several specifications |
| 2 | **Same IDS, different verdicts in different checkers** | "IfcTester passes only 1 of 6 beams"; "specs with Classification/PartOf pass without checking"; "prohibited/optional inverted" | 20 records / 15 threads (en) | Engines implement facets differently or only partly (stubs); IFC2x3 type mapping; plain bugs; Python/XML type coercion | Run the official IDS test cases; name engine and version in the report; cross-check in a second tool; Audit the IDS first |
| 3 | **Pre-export / pre-submission self-check for a national portal** | "2 hours to export, errors appear only after upload"; "报建前能不能在Revit里先自检"; "pre-check against COP 3.1 before submitting" | 12 records / 11 threads (ru 5, zh 5, en 2) | Portal rules (AGR, SZ-IFC, CORENET X, permit systems) are checked after a slow IFC export | Check Revit parameters against the IDS/mapping *before* export; dedicated pre-flight tools; iterate on a small test export |
| 4 | **What IDS can and cannot say** (geometry, conditions, code-fits-element, federation, refurbishment) | "IDS не умеет геометрию и условную логику"; "pattern is right but 32.xx on an IfcWall passes"; "how do I merge IDS files for a federated model?" | 14 records / 13 threads (en 8, ru 2, nl, zh, ja, it) | IDS 1.0 covers alphanumeric requirements through six facets; no geometry, no relations beyond `partOf`, no code lists | Use Solibri-type rules or scripts for geometry/logic; keep one IDS per discipline; ship code lists as data; state the limit up front |
| 5 | **"Opens in Revit/viewer but fails the Validation Service"** | "file opens with no warnings in Revit, fails validate.buildingsmart.org"; "is the validator wrong?" | 6 records / 5 threads (en). Syn.: 3 prompts | Viewers are tolerant, the Validation Service applies EXPRESS rules strictly; some Revit exports do not pass; occasionally the validator itself is wrong | Read the rule code and entity; decide file-bug vs validator-bug; report to exporter vendor or validator repo |
| 6 | **Cryptic validator messages** (inverse cardinality, WHERE rules, derived units, rule codes) | "constraint violation in inverse attribute PlacesObject"; "Error message is unclear"; "validator flags a Name though docs say optional" | 9 records / 9 threads (en) | Messages quote EXPRESS rules (`WR1`, `[1:1]` inverses, rule codes like OJT001) without explaining them | Translate the rule into plain words, locate the offending entity, tell the generator what to change |
| 7 | **Invalid file at STEP level** (bad escapes/encoding, invalid GlobalId, hollow shapes) | "one malformed escape drops 68 of 78 products"; "IfcGuid is not a 128-bit number"; "IFCCLOSEDSHELL(()) in file, what to do" | 18 records / 17 threads (en 17, ja 1). Syn.: about 12 prompts mention GlobalIds | Writers emit invalid strings, GUIDs whose first character is above 3, empty shells/styles, placements nobody references | Fix the writer; targeted repair (with consent); lenient readers degrade to null values instead of crashing |
| 8 | **"Does the model contain what the client asked?"** (required properties lists) | "do all doors have FireRating?"; "check 212 doors"; "client requirements are in Excel/PDF, checking is manual" | 9 records / 8 threads (en, it, ja, nl, no). Syn.: the biggest block; about 20 prompts name a fire rating | Requirements live in Excel/PDF; Revit does not export empty parameters; value may sit on the type, not the occurrence | Write the list as IDS or a script; check type *and* occurrence; fix export settings |
| 9 | **Checking, authoring and viewing the IDS file itself** | "is there an online IDS validator?"; "Error 502"; "editor only reachable through VPN"; "show IDS as readable text" | 9 records / 8 threads (en 4, ru 4, ja) | XSD-valid is not the same as semantically valid; a hidden character makes the XML ill-formed; hand-written XML | IDS Audit tool; build the file with an authoring tool; read it with IfcTester's readable report |
| 10 | **Duplicate property sets, duplicate elements, "extra" data** | "IDS says ModelLabel is missing but I can see it"; "find duplicates invisible in 3D" | 5 records / 4 threads | Revit sometimes writes two psets of the same name on one object (invalid); copies stacked on each other; exporters add far more data than asked | Run schema validation first; IfcPatch recipe; match duplicates by bounding box and keep the richer copy |
| 11 | **Trust in AI-written IFC and AI claims about validation** | "the IFC you wrote won't open"; "AI invented Pset names"; "AI script returned an empty list" | 9 records / 9 threads (en 7, zh, ja). Syn.: 1 direct prompt | LLMs pattern-complete: they invent psets, put famous properties everywhere, skip mandatory attributes | Validate in a loop; check names against the schema; allow "I don't know"; require source quotes |
| 12 | **Validation Service: availability, installation, what "certified" means** | "502 on login"; "make start loops, worker restarts"; "is v24 certified, why no IFC4 certification docs?" | 6 records / 6 threads (en 4, ja 2) | Server faults; the self-host needs git submodules and Docker; validation, IDS support and certification are different things | Check service status; follow the tagged-commit/submodule steps; separate "validated" from "certified" from "IDS-supporting" |
| 13 | **Federation coherence: origin, units, version diff** | "models don't sit on the same zero point"; "GUID-only diff shows everything deleted and recreated" | 6 records / 4 threads (en 5, nl). Syn.: about 8 prompts | Each exporter treats georeference, units and GlobalIds its own way; Revit may regenerate GlobalIds | Report CRS, units and distance to origin per model; diff on type+name+position when GUIDs churn |

## Problems in depth

### 1. IDS does not behave as the author expects

**Symptoms in users' words**
- en: "assigned unique parameters in Revit; IDS applies to IFCELEMENT min/max 1; check fails" ([bSI forum](https://forums.buildingsmart.org/t/applicability-for-all-elements/6234)).
- en: "IDS rule restricting IfcBeam PredefinedType to BEAM or PILECAP passes only one of six beams; is this a bug in IfcTester or do I misunderstand IDS?" ([OSArch](https://community.osarch.org/discussion/3478/ifctester-not-properly-check-predefinedtype-requirements)).
- en: "an IDS spec shows as skipped, not failed, when no elements match" ([IfcOpenShell#9112](https://github.com/IfcOpenShell/IfcOpenShell/issues/9112)).
- en: "EIRs often name a property but not its pset, while IDS requires the pset" ([IDS#189](https://github.com/buildingSMART/IDS/issues/189)).
- en: "an empty IFCLABEL value passes a required check" ([IDS#403](https://github.com/buildingSMART/IDS/issues/403)); "IFCTEXT instead of IFCLABEL is silently omitted" ([IDS#337](https://github.com/buildingSMART/IDS/issues/337)).
- en: "can IDS verify that quantities exist in the model?" (she had written `IfcQuantityLength` as the data type instead of the measure type `IfcLengthMeasure`) ([bSI forum](https://forums.buildingsmart.org/t/validation-of-quantities-using-ids/5326)).

**Why it happens**
- Entity names are UPPERCASE and **do not inherit**: `IFCELEMENT` is abstract and has no instances, so you must list `IFCWALL`, `IFCDOOR` and so on.
- The **Attribute facet reads the literal stored value** (`PredefinedType` = `USERDEFINED` stays `USERDEFINED`); the **Entity facet's `predefinedType`** is the one that looks through the type object (`USERDEFINED` resolves via the type's `ElementType`, otherwise the occurrence's `ObjectType`). Attributes are not inherited from the type, so occurrence and type are tested separately.
- **Cardinality is on the applicability**: required = at least one matching element must exist *and* each must satisfy the requirements; optional (0..n) = only those that exist are checked; prohibited (0..0) = none may exist. With *optional* applicability (`minOccurs=0`) a specification that matches nothing is reported as skipped/not applicable; with *required* applicability the same situation is a failure (the reference doc: "at least one matching object must exist"). Whether a missing `minOccurs/maxOccurs` counts as required is itself under discussion in [IfcOpenShell#9112](https://github.com/IfcOpenShell/IfcOpenShell/issues/9112). A property facet treats quantities and properties the same way and needs a data type when a value is given.
- IFC2x3 has no `IfcAirTerminal`: occurrences are `IfcFlowTerminal`; IDS handles this with an IFC2x3 type-mapping table that not every engine implements.

**What fixes it**
- Enumerate concrete classes; use two or three specifications for "either A or B but never mixed"; put the discriminating property into the applicability (valves with `operational relevant = yes` need a field designation: that is "property in applicability, other property in requirements", [IDS#176](https://github.com/buildingSMART/IDS/issues/176)); use `maxOccurs=0` for "no proxies allowed".
- Quantities: use the measure type (`IfcLengthMeasure`, `IfcAreaMeasure`...) as `dataType`, not the quantity class; IFC2x3 has no `Qto_` sets.

**What a good AI/MCP assistant should do**
- Explain in one sentence *why* an IDS spec skipped, passed or failed, and say which semantic it used (required/optional/prohibited).
- Never write `IFCELEMENT` as applicability; expand to concrete classes present in the model.
- Ask: Which IFC schema (2X3 / 4 / 4X3)? Do you have the `.ids` file or only a requirement list? Should the rule apply to occurrences, types, or both? What should happen when no element matches: skipped or fail?

### 2. Same IDS, different verdicts in different checkers

**Symptoms**
- en: "IDSClassification and IDSPartOf bodies are commented out; against buildingSMART test cases 27/33 select nothing so failing cases pass" ([ThatOpen engine_components#830](https://github.com/ThatOpen/engine_components/issues/830)).
- en: "prohibited inverts each match, optional forces pass, no matching pset pushes fail" ([engine_components#821](https://github.com/ThatOpen/engine_components/issues/821)).
- en: "PredefinedType in different facets yields inconsistent results" ([IfcOpenShell#7855](https://github.com/IfcOpenShell/IfcOpenShell/issues/7855)); "IfcTester ignores IFC2x3 occurrence type mapping" ([#7212](https://github.com/IfcOpenShell/IfcOpenShell/issues/7212)); "uppercase boolean FALSE read as True" ([#9856](https://github.com/IfcOpenShell/IfcOpenShell/issues/9856)); "regex with negative lookahead raises RegexError" ([#7359](https://github.com/IfcOpenShell/IfcOpenShell/issues/7359)).
- en: "vendors produce IDS files differently so interoperability is unclear" ([bSI forum](https://forums.buildingsmart.org/t/how-to-validate-ids-files/5993)).

**Why it happens**
IDS is a standard, but each tool (IfcTester, Solibri, BIMcollab, the xbim checker, That Open components, Bonsai) re-implements it. Facets are sometimes stubs, edge cases (USERDEFINED, optional, prohibited, tolerance, data-type coercion) differ, and bugs are fixed at different speeds. The IDS regex is the XSD dialect, which has no lookahead. The reference doc notes that float tolerance is 1e-6 relative plus absolute and that software must pass the repository test cases.

**What fixes it**
Test the checker, not only the model: run the buildingSMART IDS test cases, update the engine, and treat a green result from a checker with stub facets as "not checked". When two tools disagree, minimise the case (one element, one spec) and look at the engine version.

**What a good AI/MCP assistant should do**
- Always print the engine and version used and list facets it could *not* evaluate; never turn "facet unsupported" into "pass".
- On a suspicious result (e.g. 0 failures on a model you know is messy), say so and offer a cross-check.
- Ask: Which checker does the client use (Solibri, BIMcollab, IfcTester)? Which version? Is the model IFC2x3?

### 3. Pre-export / pre-submission self-check for a national portal

**Symptoms**
- ru: "тяжёлая модель выгружается 2 часа, ошибки видно только после загрузки в строимпросто, зоны пропадают, площади задваиваются" (Eng: a heavy model exports in 2 hours and errors appear only after upload to the Moscow AGR checker; zones vanish, areas are counted twice) ([Habr](https://habr.com/ru/articles/1089018/)).
- ru: "косоуры всё равно выгружаются при IfcExportAs нет, пандус уходит как IfcRampFlight" (Eng: stair stringers still export when set to No; the ramp leaves as IfcRampFlight) ([Habr](https://habr.com/ru/articles/1098340/)).
- zh: "报建前能不能在Revit里先自检，不用每次导出IFC再检测" (Eng: can we self-check inside Revit before filing, without exporting IFC every time?) ([Zhihu](https://zhuanlan.zhihu.com/p/633827596)); "自检工具里审查节点有些值是空的，导出IFC丢字段了怎么办" ([CSDN](https://blog.csdn.net/weixin_42855822/article/details/139867051)).
- en: "pre-check ifc+sg against COP 3.1 or COP 4 before submitting, select failing elements, export bcf" ([sg-ifc-microstation-eap](https://github.com/OrvenBentleySystems/sg-ifc-microstation-eap)).
- ru: 2019 thread asking how a state expertise can check a Revit/IFC model at all, no agreed method ([dwg.ru](https://forum.dwg.ru/showthread.php?t=153428)).

**Why it happens**
National portals (Moscow AGR/MGE, Shenzhen SZ-IFC, Singapore CORENET X, Taiwanese permit systems) apply their own rules to an IFC. The IFC export from Revit is slow, so every wrong parameter costs hours. A Habr article states that since 2 April 2026 IDS-conforming IFC is required for MGE/AGR (reported in a [Habr article](https://habr.com/ru/companies/pik_digital/articles/1057314/), record `ru-autodesk-telegram-r009`; verify against the portal). See [Russia](../../02_standards_regulations/national/russia.md), [China](../../02_standards_regulations/national/china_mainland.md), [Singapore](../../02_standards_regulations/national/singapore.md).

**What fixes it**
Run the same IDS/mapping against the *authoring model's parameters* before exporting (Revit-side plug-ins, `IfcExportAs` mapping checks), then do a final check on the real IFC. Pre-flight tools are explicit that they are "not a compliance decision".

**What a good AI/MCP assistant should do**
- Say plainly that it cannot reproduce the official portal verdict; it can check a stated list of rules and report which it covered.
- Check the typical culprits: IFC class missing, empty or wrong-format values, open zone contours, duplicates, coordinates/CRS (CGCS2000 for Shenzhen).
- Ask: Which portal and which rule/version (COP 3.1 or COP 4, AGR requirements edition)? Do you have the IDS or the requirements table? Revit export setup and exporter version?

### 4. What IDS can and cannot say

**Symptoms**
- ru: "IDS не умеет геометрию и условную логику - что делать" (Eng: IDS 1.0 cannot express geometry, spatial or conditional rules) ([Habr](https://habr.com/ru/articles/908192/)).
- nl: "IDS controleert alleen het patroon van de NL-SfB code, niet of de code bij het element past; IfcWall met 32.xx is formeel goed en inhoudelijk fout" (Eng: IDS checks only the pattern of the code; an IfcWall with 32.xx, a door code, passes formally) ([OpenAEC-BIM-validator#22](https://github.com/OpenAEC-Foundation/OpenAEC-BIM-validator/issues/22)).
- en: "can IDS require a type of geometric representation?" (answer: not at present) ([bSI forum](https://forums.buildingsmart.org/t/5452)); "how to apply several IDS files to a federated IFC?" (keep one IDS per discipline) ([forum](https://forums.buildingsmart.org/t/ids-and-federated-ifc-file/5654)); "supply data only for new elements in a refurbishment" ([OSArch](https://community.osarch.org/discussion/2969/filtering-new-building-components-in-ids-for-refurbishment-projects)).
- ja: "発注者の要求がExcelやPDFでバラバラで、納品IFCのチェックが人力。IDSで機械的に検証できる？" (Eng: client requirements are scattered across Excel/PDF and checking the delivered IFC is manual; can IDS verify it mechanically?) ([Zenn](https://zenn.dev/miyamiyaumya/articles/6714ef2c6e2c6c)).

**Why it happens**
IDS 1.0 (a buildingSMART Final Standard since June 2024) states *information* requirements through six facets (entity, attribute, property, classification, material, partOf). It does not check clashes, clearances, wall thickness, or whether a code *makes sense* for the element. It also cannot match an unnamed pset, and it is not an MVD/IDM replacement: MVD defines software certification subsets, IDM business use cases, IDS project-level data requirements (the alphanumeric part of LOIN).

**What fixes it**
Use IDS for what it is good at, scripts or Solibri-style rules for the rest; give code lists to the checker as data (see [classification file](./classification_cobie_fm.md)); split IDS per discipline instead of building one giant file.

**What a good AI/MCP assistant should do**
Say "IDS cannot express that" instead of faking a spec, and offer the nearest honest alternative (a script check, a manual list). Ask: Is this requirement about *data* or about *geometry/relationships*? Who consumes the result, the client's checker or you?

### 5. "Opens in Revit/viewer but fails the Validation Service"

**Symptoms**
- en: "file opens with no warnings in Revit, fails validate.buildingsmart.org" ([validate#267](https://github.com/buildingSMART/validate/issues/267)).
- en: "PR: IFC opens normally in Revit, but fails buildingSMART IFC Validation Service (Schema check)" ([revit-ifc#947](https://github.com/Autodesk/revit-ifc/issues/947)).
- en: "Validator crashes with unsupported operand on IfcSurfaceWeightsPositive though weights are positive" ([validate#266](https://github.com/buildingSMART/validate/issues/266)).

**Why it happens**
A viewer's job is to show something; the Validation Service checks syntax, schema (EXPRESS attributes, inverses, WHERE rules, global rules), then normative rules (implementer agreements, informal propositions); "industry practice" findings are only warnings. In #267 the root cause was a boolean subtraction tree about 500 levels deep that broke a derived-attribute calculation; Autodesk's reply was that Revit files will not all pass the current tests, and in #947 the answer was "validator issue". So the file can be the problem, the exporter can be the problem, or the validator can be the problem.

**What fixes it**
Read the rule code and the entity it names, run a local validation to cross-check, and decide: fix the generator, report to the exporter vendor, or report to the validator repo. Do not tell a user to "fix Revit".

**What a good AI/MCP assistant should do**
Never conclude "your file is broken" from a failure alone; list failing rules by code and count, explain each, and say which are warnings vs errors. Ask: Which exporter and setup (MVD)? Does the client actually require a Validation Service pass, or only that the file opens?

### 6. Cryptic validator messages

**Symptoms**
- en: "own converter writes IFC2x3; IfcCheckingTool reports a cardinality violation of inverse PlacesObject on parent IfcLocalPlacements; cannot understand the rule" ([forum #4372](https://forums.buildingsmart.org/t/4372)).
- en: "wants IfcBuildingElementProxy without ObjectPlacement but the validator complains" ([forum #5260](https://forums.buildingsmart.org/t/5260)); "validator flags a Name though the documentation lists Name as optional" ([forum #5951](https://forums.buildingsmart.org/t/5951)).
- en: "Error message is unclear... units conform to guide" ([validate#77](https://github.com/buildingSMART/validate/issues/77)); "what is the default for a derived unit that isn't set in the file?" ([forum #5759](https://forums.buildingsmart.org/t/what-is-the-default-for-a-derived-unit-that-isnt-set-in-the-file/5759)).

**Why it happens (and the plain-language reading)**
- `PlacesObject [1:1]`: every `IfcLocalPlacement` must be referenced by exactly one product. Parent placements referenced only by other placements, or shared by two products, break it.
- Formal rule: if a product has a shape it must also have an `ObjectPlacement`; for library objects use a type with representation maps.
- `IfcBuildingElementProxy.WR1`: a WHERE rule in the schema requires a `Name`, even though the attribute is listed as optional.
- Units: the attribute must be *derived* (`*`, not `$`); an unset derived unit is, per the community, invalid.
- Rule codes such as OJT001 (a PredefinedType set on an occurrence whose type also has one) and QTY001 appear in the report.

**What a good AI/MCP assistant should do**
Translate each error into: what rule, which entity (step id and GlobalId, class, name, storey), likely cause, what to change in the generator. Do not paraphrase an error it has not seen. Ask for the exact message text and the IFC version.

### 7. Invalid file at STEP level (encoding, GUIDs, hollow shapes)

**Symptoms**
- en: "one malformed escape in IFCPROPERTYSINGLEVALUE drops many entities; wants the parser to skip and log" (only 10 of 78 products loaded, [XbimEssentials#605](https://github.com/xBimTeam/XbimEssentials/issues/605)); "incorrectly escaped sequence breaks decoding of the entire file" ([web-ifc#1559](https://github.com/ThatOpen/engine_web-ifc/issues/1559)).
- en: "IfcGuid is not a 128-bit number" ([forum #3137](https://forums.buildingsmart.org/t/fatal-error-ifcguid-is-not-a-128-bit-number/3137)); "Are IfcGuids starting with k valid?" ([forum #3776](https://forums.buildingsmart.org/t/guid-valid-invalid/3776)).
- en: "IfcClosedShell.CfsFaces must not be empty from the checker, IFCCLOSEDSHELL(()) in file" ([IFC-Repair-Studio](https://github.com/noddlesskcho/IFC-Repair-Studio)); "IfcSurfaceStyle with empty Styles" ([IfcOpenShell#6972](https://github.com/IfcOpenShell/IfcOpenShell/issues/6972)); "IfcGridAxis without curves" ([forum #3836](https://forums.buildingsmart.org/t/error-when-import-file-of-ifc3x2-into-blenderbim-do-the-shape-or-filesize-have-some-limits/3836)).

**Why it happens**
STEP (ISO 10303-21) strings have strict escapes (a doubled backslash means a literal backslash, `\X2\...\X0\` encodes Unicode); a single bad one invalidates text and, in strict parsers, much more. IFC GUIDs are 22 characters of a base-64 alphabet and the first one can only be 0-3. Some writers emit empty shells, empty style lists or grid axes with no curves. Home-made converters and (see problem 11) AI-generated IFC are the usual sources.

**What a good AI/MCP assistant should do**
Locate the entity by step id, show the raw line, explain, and propose a **minimal repair with consent**, saving a new file and never overwriting the original. Removing an empty shell can remove geometry: say so. Ask: Where does the file come from (own converter, vendor, AI)? May I write a repaired copy?

### 8. "Does the model contain what the client asked?"

**Symptoms**
- it: "come verifico che porte e muri abbiano FireRating e trasmittanza prima di consegnare l'IFC?" (Eng: how do I check that doors and walls have FireRating and U-value before handing over the IFC?) ([ACCA Biblus](https://biblus.acca.it/bim-validation-modelli-ifc/)).
- nl: "'hebben alle 212 deuren een FireRating?' of 'm2 binnenwand per NL-SfB-code'" (Eng: client and cost estimator ask whether all 212 doors have a FireRating, or interior wall m2 per NL-SfB code) ([OpenAEC-BIM-validator#19](https://github.com/OpenAEC-Foundation/OpenAEC-BIM-validator/issues/19)).
- en: "check that all IfcDoor have Fire Rating in a given pset with allowed values" ([BIM Corner](https://bimcorner.com/model-validation-as-a-key-step-in-the-bim-workflow/)); "one bridge exported three ways: 161 proxies, random GlobalIds, no quantities" ([BIM Corner](https://bimcorner.com/same-bridge-three-ifc-files/)).
- en: "Reports psets/properties in an IFC that the IDS did not ask for" (extra data; replies split between "keep as fallback" and "redundant data conflicts with required data") ([OSArch](https://community.osarch.org/discussion/2658/non-compliance-check)).

**Why it happens**
Requirements are written in Excel/PDF; Revit does not export empty parameters, so "missing" may mean "never filled"; the value can sit on the *type* while the check looks at the *occurrence* (or the other way round); property names differ (`FireRating` vs `Fire Rating` vs a custom pset). Many exports are full of `IfcBuildingElementProxy` because the class mapping was not set.

**What a good AI/MCP assistant should do**
Check type and occurrence, say where the value was found, separate "property absent", "property present but empty" and "value not in the allowed list", and group by class and storey with GlobalIds. Ask: Which pset/property names does the client use? Allowed values? Does the requirement apply to all elements of a class or only some?

### 9. Checking, authoring and viewing the IDS file itself

**Symptoms**
- en: "how can I make sure an IDS file is well formed before using it, and will bSI offer an online validator?" ([forum #5993](https://forums.buildingsmart.org/t/how-to-validate-ids-files/5993)).
- en: "my generated IDS fails with error 502" (answer: the XML was not well-formed because of a hidden character; use an authoring tool and the Audit tool) ([forum #5760](https://forums.buildingsmart.org/t/requiring-the-existence-of-predefined-type/5760)).
- ru: "редактор доступен только через VPN, для больших спецификаций неудобен" (Eng: the visual IDS editor is reachable only through a VPN and is unwieldy for large specs) ([Telegram](https://t.me/s/ifc_ru)).
- en: "how to view an IDS XML as simple human-readable text" ([OSArch](https://community.osarch.org/discussion/2678/view-ids-xml-file-as-simplified-text-human-friendly-readable-ids)).

**Why / fix**
XSD validation is necessary but not sufficient: the official **IDS Audit tool** also checks that entities exist in the declared IFC version, that pset names make sense and that cardinalities are legal. One answer notes that Solibri rejected an IDS mixing IFC2X3 and IFC4 scopes. Use the Audit tool, build files with an editor rather than by hand, and render the IDS as readable text for the human client.

**What a good AI/MCP assistant should do**
Audit before running; say what the Audit covers; produce a short plain-language reading of each specification ("Applies to: IfcWall. Requires: Pset_WallCommon.FireRating, non-empty."). Ask: Which IFC version(s) does the IDS target?

### 10. Duplicate property sets, duplicate elements, "extra" data

**Symptoms**
- en: "IDS says ModelLabel and ModelReference under Pset_ManufacturerTypeInformation are missing, but the Revit model has them" ([IfcOpenShell#7095](https://github.com/IfcOpenShell/IfcOpenShell/issues/7095)). Answer: two property sets of the same name on one object are invalid; run `ifcopenshell.validate` first, then an IfcPatch recipe or report to Autodesk.
- ru: "как найти дубли в IFC которых не видно" (Eng: how to find duplicate elements that cannot be seen in 3D, and forward the edits to a colleague) ([Habr](https://habr.com/ru/articles/1100956/)): match by bounding box, keep the element with more filled parameters, store edits by GlobalId.
- en: Dynamo script deletes only one of four identical duplicates per run ([Dynamo forum](https://forum.dynamobim.com/t/deleting-duplicate-instances-in-revit/115296)).

**What a good AI/MCP assistant should do**
When an IDS reports "missing" for something the user can see, look for duplicate pset names and wrong data types *before* blaming the user or the tool. For duplicates, show pairs with GlobalIds, tolerance used and which copy has more data; never delete without asking.

### 11. Trust in AI-written IFC and AI claims about validation

**Symptoms**
- en: "Basic (MEP) IFC file cannot be opened": header says `originating_system OpenAI`, IfcProject has 8 attributes instead of 9 ([IfcOpenShell#7945](https://github.com/IfcOpenShell/IfcOpenShell/issues/7945)). Answer: not a Bonsai bug; LLM-written IFC is non-conformant; validate and loop until it passes.
- en: "AI gave me Pset_BuildingElementCommon and put IsExternal on footings; how do I know which property sets are real?" ([BIM Corner](https://bimcorner.com/ai-ifc-properties/)).
- en: "ChatGPT and others gave a script returning an empty list and an Excel with headers only" ([Dynamo forum](https://forum.dynamobim.com/t/help-with-automated-quality-check-script-getting-empty-list-and-blank-excel/112252)).
- zh/ja: wishes for AI that previews changes, asks for confirmation, logs and allows undo ([Yang-Agent_Revit](https://github.com/5788324/Yang-Agent_Revit)); fine-tuned models still confuse WHERE rules and attribute names ([ifc-bim-llm-finetuning](https://github.com/matsuokakoki/ifc-bim-llm-finetuning)).

**What a good AI/MCP assistant should do**
Check every pset/property name against the schema before asserting it; separate what it *measured* in the file from what it *remembers*; run validation after any write and report the result; distinguish "parsed OK" from "passed the buildingSMART rules"; admit when a check was not run. Ask before writing: new file or in place?

### 12. Validation Service: availability, installation, what "certified" means

**Symptoms**
- en: "[Service Unreachable?] 502 on login" ([validate#335](https://github.com/buildingSMART/validate/issues/335)); "installing the Validation Service on Windows... git submodules and docker as non-expert" ([validate#279](https://github.com/buildingSMART/validate/issues/279)).
- ja: "公式手順どおりmake startしたらhttp://localhostがエラー、backendとworkerが再起動を繰り返す" (Eng: following the official steps, `make start` gives an error and the backend and worker keep restarting) ([Zenn](https://zenn.dev/kiyuka/scraps/e07bf799384b52)); fix: align the submodule to the tagged commit, create and activate the Django SYSTEM user.
- en: "bSI Software Certification and IFC4: is v24 certified and why no IFC4 certification docs?" ([forum #3192](https://forums.buildingsmart.org/t/bsi-software-certification-and-ifc4/3192)).

**Why / fix**
Validation Service (is the file valid?), software certification (does this product import/export a given MVD?), and "IDS support" (vendor self-reported) are three different things. The service needs an account, has a file-size limit (the reference doc gives 256 MB unzipped) and an API. Self-hosting is possible but fiddly.

**What a good AI/MCP assistant should do**
Know that uploading a client's IFC to a public service may be forbidden; offer a local check and mention self-hosting. Do not claim a file is "buildingSMART validated" unless the Validation Service report exists.

### 13. Federation coherence: origin, units, version diff

**Symptoms**
- nl: "In een federatie ... gaat het vaak mis doordat modellen niet op hetzelfde nulpunt liggen. Rapporteer per model schema, lengte-eenheid, IfcSite ref, MapConversion (EPSG 28992), afstand tot oorsprong" (Eng: federated models are often not on the same zero point; report per model schema, length unit, IfcSite reference, MapConversion and distance to origin) ([OpenAEC-BIM-validator#21](https://github.com/OpenAEC-Foundation/OpenAEC-BIM-validator/issues/21)).
- en: "Some software writes projected coordinates as model coordinates AND an IfcMapConversion so coordinates end up far off" ([forum #5695](https://forums.buildingsmart.org/t/we-have-a-problem-with-ifcmapconversion/5695)).
- en: "When Revit regenerates GlobalIds a GUID-only diff shows everything deleted and recreated" ([OSArch](https://community.osarch.org/discussion/3616/browser-based-ifc-clash-version-diff-how-would-you-group-clashes-and-handle-guid-churn)); "IfcDiff misses removal of PredefinedType" ([IfcOpenShell#8214](https://github.com/IfcOpenShell/IfcOpenShell/issues/8214)).

**What a good AI/MCP assistant should do**
Report CRS, units, `IfcMapConversion` and distance to origin per file; flag a possible *double* shift (projected coordinates plus a conversion); when GlobalIds differ between versions, say the diff is heuristic and report confidence. Ask: Same project base point in all models? Which EPSG code does the client use?

## Real questions

These are paraphrases kept in the language of the source, one row per record (one record per source thread where possible). The "EN gloss" column is the researcher's English gloss for non-English rows; English rows need none. Quotation of a source's own title appears before `--` when the paraphrase alone was too thin. Language of rows is the `lang` tag of the record (see data-basis note above).

### Is my IFC even valid? (schema, Validation Service, broken files)

| lang | question (original language, paraphrased) | EN gloss | persona | source |
|---|---|---|---|---|
| en | file opens with no warnings in Revit, fails validate.buildingsmart.org | — | bim_coordinator | [GitHub buildingSMART/validate#267](https://github.com/buildingSMART/validate/issues/267) `en-val-r016` |
| en | Error message is unclear -- new error messages in VS 0.6.4, file attached, units conform to guide | — | civil_infra_engineer | [GitHub buildingSMART/validate#77](https://github.com/buildingSMART/validate/issues/77) `en-val-r018` |
| en | own converter writes IFC2x3; IfcCheckingTool reports a cardinality violation of inverse PlacesObject on parent IfcLocalPlacements of IfcDistributionFlowElement instances; cannot understand the rule | — | developer_programmer | [bSI forum #4372](https://forums.buildingsmart.org/t/4372) `en-bsforum-r007` |
| en | wants IfcBuildingElementProxy without ObjectPlacement (use global coordinates) but the validator complains when placement is $ while a representation exists | — | developer_programmer | [bSI forum #5260](https://forums.buildingsmart.org/t/5260) `en-bsforum-r020` |
| en | validator flags IfcBuildingElementProxy without a Name though the documentation lists Name as optional | — | developer_programmer | [bSI forum #5951](https://forums.buildingsmart.org/t/5951) `en-bsforum-r032` |
| en | What is the default for a derived unit that isn't set in the file? -- file uses cubic metres and years; asks what unit applies | — | developer_programmer | [bSI forum #5759](https://forums.buildingsmart.org/t/what-is-the-default-for-a-derived-unit-that-isnt-set-in-the-file/5759) `en-val-r012` |
| en | GUID valid/invalid -- asks if GUID like k0el31... is allowed | — | developer_programmer | [bSI forum #3776](https://forums.buildingsmart.org/t/guid-valid-invalid/3776) `en-val-r013` |
| en | Validation error IfcSurfaceWeightsPositive -- quotes rule text and instance of IfcRationalBSplineSurfaceWithKnots | — | developer_programmer | [GitHub buildingSMART/validate#266](https://github.com/buildingSMART/validate/issues/266) `en-val-r017` |
| en | generating IFC4 with xbim; validator flags IFCCARTESIANPOINTLIST3D((...),$) because TagList is not in IFC4; raised before, advice was to go IFC4x3 but IFC4 still needed | — | developer_programmer | [GitHub xBimTeam/XbimEssentials#661](https://github.com/xBimTeam/XbimEssentials/issues/661) `en-gh-xbim-others-r007` |
| en | one malformed escape in IFCPROPERTYSINGLEVALUE drops many entities; wants the parser to skip and log instead | — | developer_programmer | [GitHub xBimTeam/XbimEssentials#605](https://github.com/xBimTeam/XbimEssentials/issues/605) `en-gh-xbim-others-r019` |
| en | incorrectly escaped sequence breaks decoding of entire file, subsequent correct strings fail too | — | developer_programmer | [GitHub ThatOpen/engine_web-ifc#1559](https://github.com/ThatOpen/engine_web-ifc/issues/1559) `en-gh-encoding-r009` |
| en | IfcClosedShell.CfsFaces must not be empty from the checker, IFCCLOSEDSHELL(()) in file, what to do | — | bim_coordinator | [GitHub noddlesskcho/IFC-Repair-Studio](https://github.com/noddlesskcho/IFC-Repair-Studio) `en-sg-corenetx-r002` |
| en | '#4005782=IfcSurfaceStyle('ACCENT - DARK',.BOTH.,())' causes error on append. | — | architect | [GitHub IfcOpenShell/IfcOpenShell#6972](https://github.com/IfcOpenShell/IfcOpenShell/issues/6972) `en-err-r031` |
| en | Import breaks on IfcSweptDiskSolid style; python -m ifcopenshell.validate --rules gives 'No validation issues found'. | — | bim_coordinator | [GitHub IfcOpenShell/IfcOpenShell#8194](https://github.com/IfcOpenShell/IfcOpenShell/issues/8194) `en-err-r028` |
| en | header says originating_system OpenAI; IfcProject has 8 attributes instead of 9 (Phase missing) | — | student_beginner | [GitHub IfcOpenShell/IfcOpenShell#7945](https://github.com/IfcOpenShell/IfcOpenShell/issues/7945) `en-aimcp-r013` |
| en | [ Service Unreachable? ] -- 502 on login | — | other | [GitHub buildingSMART/validate#335](https://github.com/buildingSMART/validate/issues/335) `en-val-r019` |
| en | [Documentation] Installing the Validation Service on Windows -- shares struggles with git submodules and docker as non-expert | — | student_beginner | [GitHub buildingSMART/validate#279](https://github.com/buildingSMART/validate/issues/279) `en-val-r020` |
| ja | 公式手順どおりmake startしたらhttp://localhostがエラー、backendとworkerが再起動を繰り返す | Running buildingSMART IFC Validation Service locally in Docker: workers restart, uploads never process | developer_programmer | [Zenn](https://zenn.dev/kiyuka/scraps/e07bf799384b52) `ja-japan-r007` |
| it | dove sono dichiarate le unita nell'IFC? il file valido ma le misure sono sballate | Where are units declared in an IFC and why schema validity does not guarantee correct measures? | developer_programmer | [Ingenio](https://www.ingenio-web.it/articoli/ifc-in-pratica-unita-di-misura-dove-trovarle-e-come-leggerle/) `it-italy-r013` |
| ru | IFC из Сапфира в автокад не импортируется, системная ошибка, в BimSight открывается нормально; как правильно экспортировать | IFC exported from SAPFIR opens in BIMsight but AutoCAD 2020 import fails with System Error; how to export/import correctly? | bim_coordinator | [dwg.ru forum](https://forum.dwg.ru/showthread.php?t=160240) `ru-dwg-other-r003` |
| ru | удалил элемент - файл открывается, но валидатор падает; смена класса требует смены типа | Deleting elements or changing class via web-ifc passes basic checks but breaks strict schema validation | developer_programmer | [Habr](https://habr.com/ru/articles/1094224/) `ru-habr-dev-r005` |
| en | How does bSI software certification work? ArchiCAD 24 got many IFC fixes but certification dates from 2019; is v24 certified and why no IFC4 certification docs? | — | bim_manager | [bSI forum #3192](https://forums.buildingsmart.org/t/bsi-software-certification-and-ifc4/3192) `en-bsmart-r005` |

### Writing and reading IDS (authoring pitfalls)

| lang | question (original language, paraphrased) | EN gloss | persona | source |
|---|---|---|---|---|
| en | wants IDS files to be correctly formatted before validating IFC; vendors produce them differently; asks if an online IDS validator is planned | — | bim_coordinator | [bSI forum #5993](https://forums.buildingsmart.org/t/how-to-validate-ids-files/5993) `en-val-r001` |
| en | needs PredefinedType required to separate ceilings, flooring, insulation; had mvdXML rule in BIMQ; generated IDS fails with error 502 | — | bim_coordinator | [bSI forum #5760](https://forums.buildingsmart.org/t/requiring-the-existence-of-predefined-type/5760) `en-val-r004` |
| en | assigned unique parameters in Revit; IDS applies to IFCELEMENT min/max 1; check fails | — | bim_coordinator | [bSI forum #6234](https://forums.buildingsmart.org/t/applicability-for-all-elements/6234) `en-val-r006` |
| en | spent hours on IDS files that were invalid or missed it; ReferenceView 1.2 file | — | bim_coordinator | [bSI forum #6180](https://forums.buildingsmart.org/t/the-predefinedtype-shall-only-be-used/6180) `en-val-r007` |
| en | IDS - Allowing two entities, but they have different PredefinedTypes -- wants either option allowed but mixed combos blocked | — | bim_manager | [bSI forum #5794](https://forums.buildingsmart.org/t/ids-allowing-two-entities-but-they-have-different-prefinedtypes/5794) `en-val-r009` |
| en | Pset_SoundGeneration SoundCurve is IfcPropertyTableValue with two measure types | — | mep_engineer | [bSI forum #5740](https://forums.buildingsmart.org/t/specifying-data-type-for-table-value-with-multiple-data-types/5740) `en-val-r010` |
| en | asks whether IDS can verify quantities exist in the model; user later found she used IfcQuantityLength instead of IfcLengthMeasure as data type | — | student_beginner | [bSI forum #5326](https://forums.buildingsmart.org/t/validation-of-quantities-using-ids/5326) `en-val-r003` |
| en | asks if IDS can validate upper/lower bound of a bounded value property and how the XML looks | — | mep_engineer | [bSI forum #5736](https://forums.buildingsmart.org/t/using-ids-to-validate-property-attributes/5736) `en-val-r002` |
| en | IfcTester. USERDEFINED in PredefinedType gives unpredictable results -- no elements matched even valid ones; screenshots | — | bim_coordinator | [GitHub IfcOpenShell/IfcOpenShell#7856](https://github.com/IfcOpenShell/IfcOpenShell/issues/7856) `en-val-r024` |
| en | ifctester ids simple value pset prop checks on integers and strings -- 4-case matrix of model type vs python value type | — | developer_programmer | [GitHub IfcOpenShell/IfcOpenShell#7245](https://github.com/IfcOpenShell/IfcOpenShell/issues/7245) `en-val-r022` |
| en | ifctester: IDS-valid uppercase boolean FALSE is read as True | — | developer_programmer | [GitHub IfcOpenShell/IfcOpenShell#9856](https://github.com/IfcOpenShell/IfcOpenShell/issues/9856) `en-val-r034` |
| en | a property with IFCTEXT instead of IFCLABEL is silently omitted from the check | — | bim_coordinator | [GitHub buildingSMART/IDS#337](https://github.com/buildingSMART/IDS/issues/337) `en-bsforum-r051` |
| en | Empty string and cardinality of requirements -- an empty IFCLABEL value passes a required check | — | bim_coordinator | [GitHub buildingSMART/IDS#403](https://github.com/buildingSMART/IDS/issues/403) `en-bsforum-r052` |
| en | EIRs often name the property but not the Pset, e.g. UK BIM Framework template; IDS property facet needs both | — | bim_manager | [GitHub buildingSMART/IDS#189](https://github.com/buildingSMART/IDS/issues/189) `en-uk-anz-india-r013` |
| en | only IfcValve with attribute operational relevant = yes need a field designation; IfcClass alone can't separate them | — | bim_manager | [GitHub buildingSMART/IDS#176](https://github.com/buildingSMART/IDS/issues/176) `en-uk-anz-india-r012` |
| en | How to differentiate requirements for objects within the same IFC entity? -- different objects of same entity need different requirements | — | bim_manager | [GitHub buildingSMART/IDS#400](https://github.com/buildingSMART/IDS/issues/400) `en-val-r027` |
| en | What is the relationship between IDS and IDM or MVD? | — | researcher_academic | [bSI forum #4199](https://forums.buildingsmart.org/t/what-is-the-relationship-between-ids-and-idm-or-mvd/4199) `en-val-r008` |
| en | railway station project, many authoring tools; asks how to combine IDS files for a federated model | — | bim_manager | [bSI forum #5654](https://forums.buildingsmart.org/t/ids-and-federated-ifc-file/5654) `en-val-r005` |
| en | RegexError with negative lookahead pattern in IDS/ifctester -- validation crashes on pattern with (?!...) | — | bim_manager | [GitHub IfcOpenShell/IfcOpenShell#7359](https://github.com/IfcOpenShell/IfcOpenShell/issues/7359) `en-gh-ifcopenshell-r037` |
| en | wants IDS that fails when a proxy exists and lists those entities; first draft added redundant GlobalId requirement, second draft passed/failed right but did not list entities | — | bim_coordinator | [OSArch forum](https://community.osarch.org/discussion/3303/ids-check-for-ifcbuildingelementproxy-question) `en-fmor-r003` |
| ru | как проверять IFC по IDS пакетно, с отчётами html и json | How to check IFC models against IDS requirements (example from SPb CGE) in batch with reports | developer_programmer | [Habr](https://habr.com/ru/articles/883016/) `ru-autodesk-telegram-r012` |
| ru | редактор доступен только через VPN, для больших спецификаций неудобен | Visual IDS editor reachable only via VPN and unwieldy for large real specifications | developer_programmer | [Telegram channel](https://t.me/s/ifc_ru) `ru-autodesk-telegram-r024` |
| ja | 発注者の要求がExcelやPDFでバラバラで、納品IFCのチェックが人力。IDSで機械的に検証できる？ | What power does IDS give for operating IFC correctly (clients checking contractor IFC automatically)? | bim_manager | [Zenn](https://zenn.dev/miyamiyaumya/articles/6714ef2c6e2c6c) `ja-japan-r003` |
| ja | explains IDS 1.0 as rule format; needs separate software to check | A casual explanation of IDS: rules for checking IFC data, eight rule patterns, six facets | student_beginner | [Qiita](https://qiita.com/kiyuka/items/62e30208c035e828714b) `en-val-r029` |

### Checkers disagree, what IDS cannot do, federation coherence

| lang | question (original language, paraphrased) | EN gloss | persona | source |
|---|---|---|---|---|
| en | IDS rule restricting IfcBeam PredefinedType to BEAM or PILECAP passes only one of six beams; user asks if this is a bug in IfcTester or a misunderstanding of IDS. | — | bim_coordinator | [OSArch forum](https://community.osarch.org/discussion/3478/ifctester-not-properly-check-predefinedtype-requirements) `en-osarch-r007` |
| en | IDSClassification and IDSPartOf bodies are commented out; against buildingSMART test cases all 27/33 select nothing so failing cases pass | — | reviewer_authority | [GitHub ThatOpen/engine_components#830](https://github.com/ThatOpen/engine_components/issues/830) `en-gh-thatopen-r039` |
| en | cardinality optional/prohibited does not follow IDS: prohibited inverts each match, optional forces pass, no matching pset pushes fail | — | reviewer_authority | [GitHub ThatOpen/engine_components#821](https://github.com/ThatOpen/engine_components/issues/821) `en-gh-thatopen-r040` |
| en | IfcTester does not support the Ifc2x3 Occurrence type mapping implementor agreement -- sample IDS ifcVersion IFC2X3 requiring Name regex AIR-\d{2,5}$ | — | bim_coordinator | [GitHub IfcOpenShell/IfcOpenShell#7212](https://github.com/IfcOpenShell/IfcOpenShell/issues/7212) `en-cobie-r020` |
| en | ModelLabel and ModelReference under Pset_Pset_ManufacturerTypeInformation not reporting correctly -- check warns pset lacks property | — | bim_manager | [GitHub IfcOpenShell/IfcOpenShell#7095](https://github.com/IfcOpenShell/IfcOpenShell/issues/7095) `en-gh-ifcopenshell-r038` |
| en | coordinator wrote a python script that reports psets/properties in an IFC that the IDS did not ask for, since authoring tools bloat files; asks feedback | — | bim_coordinator | [OSArch forum](https://community.osarch.org/discussion/2658/non-compliance-check) `en-fmor-r001` |
| en | needs to check around 70 IFC models against 6 IDS files (specific pairs), export ODS/HTML/BCF reports; no coding experience, ChatGPT did not help, only PyPI docs; dreads manual repetition | — | bim_coordinator | [OSArch forum](https://community.osarch.org/discussion/2273/ifctester-script-for-testing-several-ifcs-with-several-ids) `en-fmor-r004` |
| en | agreed with client to deliver information only for new elements in scope, but mixed elements (old wall with new void) cannot be split; wants a global filter across all IDS specs on a project pset value 'New' | — | bim_coordinator | [OSArch forum](https://community.osarch.org/discussion/2969/filtering-new-building-components-in-ids-for-refurbishment-projects) `en-fmor-r002` |
| nl | IDS controleert alleen het patroon van de NL-SfB code, niet of de code bij het element past; IfcWall met 32.xx is formeel goed en inhoudelijk fout. Wil codelijst, koppeling IfcWall->21/22, IfcDoor->31/32 en controle waar de code… | An IDS can check the pattern of an NL-SfB code but not whether the code fits the element; an IfcWall with 32.xx (doors) passes formally | bim_coordinator | [GitHub OpenAEC-Foundation/OpenAEC-BIM-validator#22](https://github.com/OpenAEC-Foundation/OpenAEC-BIM-validator/issues/22) `nl-dutch-r002` |
| ru | IDS не умеет геометрию и условную логику - что делать | IDS 1.0 cannot express geometry, spatial or conditional rules | bim_manager | [Habr](https://habr.com/ru/articles/908192/) `ru-habr-dev-r015` |
| it | con che tool verifico i requisiti informativi del modello IFC? | usBIM.checker for information verification of the model. | bim_manager | [ACCA Biblus](https://biblus.acca.it/usbim-checker-verifica-informativa-del-modello/) `it-italy-r027` |
| en | Some software writes projected coordinates as model coordinates AND an IfcMapConversion so coordinates end up far off; very little software reads IfcMapConversion. | — | bim_manager | [bSI forum #5695](https://forums.buildingsmart.org/t/we-have-a-problem-with-ifcmapconversion/5695) `en-coord-r027` |
| nl | In een federatie van bouwkunde, constructie en installaties gaat het vaak mis doordat modellen niet op hetzelfde nulpunt liggen. Rapporteer per model schema, lengte-eenheid, IfcSite ref, MapConversion (EPSG 28992), afstand tot… | Federated models often don't share the same origin so clash detection is pointless; report CRS, units, distance to origin per model | bim_coordinator | [GitHub OpenAEC-Foundation/OpenAEC-BIM-validator#21](https://github.com/OpenAEC-Foundation/OpenAEC-BIM-validator/issues/21) `nl-dutch-r008` |
| en | Is system x storey x source object the right granularity for clash lists? When Revit regenerates GlobalIds a GUID-only diff shows everything deleted and recreated - any heuristic that holds on real exports? Do non-viewer users… | — | bim_coordinator | [OSArch forum](https://community.osarch.org/discussion/3616/browser-based-ifc-clash-version-diff-how-would-you-group-clashes-and-handle-guid-churn) `en-coord-r009` |

### Client requirements and national submissions (before you send it)

| lang | question (original language, paraphrased) | EN gloss | persona | source |
|---|---|---|---|---|
| it | come verifico che porte e muri abbiano FireRating e trasmittanza prima di consegnare l'IFC? | How to check required properties and values (e.g. FireRating) in an IFC against a template. | bim_manager | [ACCA Biblus](https://biblus.acca.it/bim-validation-modelli-ifc/) `it-italy-r008` |
| en | one bridge exported three ways: 161 proxies, random GlobalIds, no quantities, national-grid mm coordinates making viewers jitter. How to tell a good file from a bad one? | — | bim_manager | [BIM Corner blog](https://bimcorner.com/same-bridge-three-ifc-files/) `en-blogs-linkedin-r001` |
| no | finnes det en veileder som forklarer IFC-struktur og vanlige problemer, til bruk ved kravsetting og kontroll av leveranser? | Guide to IFC for beginners and advanced users, aimed at writing requirements and checking deliveries | bim_coordinator | [bSI Norge](https://www.buildingsmart.no/standarder/publikasjoner-og-veiledninger.html) `no-norway-r003` |
| ru | с 01.07.2019 госэкспертиза требует BIM, как проверять проект в Revit или IFC, можно ли PDF и чертежи, как быть с 87 постановлением, методики нет | From 1 July 2019 state expertise reportedly requires BIM; how do we check a Revit project or IFC model, can PDF drawings be used instead? | bim_coordinator | [dwg.ru forum](https://forum.dwg.ru/showthread.php?t=153428) `ru-autodesk-telegram-r001` |
| ru | тяжёлая модель выгружается 2 часа, ошибки видно только после загрузки в строимпросто, зоны пропадают, площади задваиваются | Heavy model exports IFC in 2 hours and errors only show after upload to the Moscow AGR checker; rooms vs zones, vanished zones, area overcounting | bim_coordinator | [Habr](https://habr.com/ru/articles/1089018/) `ru-autodesk-telegram-r008` |
| ru | косоуры всё равно выгружаются при IfcExportAs нет, пандус уходит как IfcRampFlight, МССК коды помещениям вручную | Preparing a model for AGR: each element needs IFC class and attributes; stair stringers still export when set to No; ramp as IfcRampFlight needs another classifier code | bim_coordinator | [Habr](https://habr.com/ru/articles/1098340/) `ru-autodesk-telegram-r011` |
| ru | валидатор ругается, что площадь IfcArea а не IfcReal; глобальная замена в блокноте ломает Pset_* | Exporter writes areas/volumes as IfcArea or IfcLabel instead of IfcReal and the IDS validator rejects them | bim_coordinator | [Habr](https://habr.com/ru/articles/1094224/) `ru-habr-dev-r004` |
| ru | как найти дубли в IFC которых не видно и переслать правки коллеге | Find and remove duplicate elements invisible in 3D; keep an edit journal keyed by GlobalId applicable to later exports | bim_coordinator | [Habr](https://habr.com/ru/articles/1100956/) `ru-habr-dev-r008` |
| ru | чем проверить корректность IFC, атрибуты могут не дойти | How to validate IFC from Archicad; attributes may not survive in AutoCAD. | bim_manager | [dwg.ru forum](https://forum.dwg.ru/showthread.php?t=34919&page=3) `ru-dwg-other-r030` |
| zh | 报建前能不能在Revit里先自检，不用每次导出IFC再检测 | Pre-check the model inside Revit before exporting SZ-IFC for Shenzhen filing. | bim_coordinator | [Zhihu](https://zhuanlan.zhihu.com/p/633827596) `zh-lightweight-review-r002` |
| zh | 自检工具里审查节点有些值是空的，导出IFC丢字段了怎么办 | Some review node values are empty in the self-check tool, meaning fields were lost during IFC export. | bim_coordinator | [CSDN](https://blog.csdn.net/weixin_42855822/article/details/139867051) `zh-lightweight-review-r004` |
| zh | 新北市建照查核系統，團隊須將BIM模型IFC檔上傳，依建築技術規則定義元件參數 | Thesis: New Taipei permit rule-check system requires submitting IFC from Revit model with parameters defined by Taiwan building technical regulations. | researcher_academic | [etheses.lib.ntust.edu.tw](https://etheses.lib.ntust.edu.tw/thesis/detail/2e82ca6d84bfe5f839f58b35029a1d54) `zh-tw-hk-r009` |
| zh | Revit导出IFC后会丢哪些信息？ | What information is lost when a Revit model is exported to IFC? | bim_manager | [Zhihu](https://www.zhihu.com/question/264127961) `zh-zhihu-r011` |
| nl | Opdrachtgever en calculator gebruiken tabellen om te controleren wat geleverd is: 'hebben alle 212 deuren een FireRating?' of 'm2 binnenwand per NL-SfB-code' | Quantity tables from the model to Excel: e.g. do all 212 doors have FireRating, m2 interior wall per NL-SfB code | estimator_qs | [GitHub OpenAEC-Foundation/OpenAEC-BIM-validator#19](https://github.com/OpenAEC-Foundation/OpenAEC-BIM-validator/issues/19) `nl-dutch-r011` |
| en | pre-check ifc+sg against COP 3.1 or COP 4 before submitting, select failing elements, export bcf | — | reviewer_authority | [GitHub OrvenBentleySystems/sg-ifc-microstation-eap](https://github.com/OrvenBentleySystems/sg-ifc-microstation-eap) `en-sg-corenetx-r011` |
| ko | IFC 최신 버전, IDS, IFC 검증 서비스, 인증 스코어카드, 국내 BIM 지침 목록 | bSK R&D center: IFC 4.3.2, IDS, validation service, certification, Korean owner BIM guidelines (MOLIT, KEC, KR, LH, PPS), open BIM design automation research | researcher_academic | [bSI Korea](https://www.buildingsmart.or.kr/Home/RnDCenter) `ko-korea-r002` |
| de | why is IFC criticized as heavy and STEP-based, and what will IFC 5 (ECS, JSON, incremental) change? | IFC 5 as a new hope for interoperability: IFC is slow, heavy, monolithic, no incremental updates. | bim_manager | [bim-me-up.com](https://bim-me-up.com/ifc-5-eine-neue-hoffnung-fuer-interoperabilitaet/) `en-blogs-linkedin-r005` |

### AI, scripts and MCP-style validation

| lang | question (original language, paraphrased) | EN gloss | persona | source |
|---|---|---|---|---|
| en | AI gave me Pset_BuildingElementCommon and put IsExternal on footings; how do I know which property sets are real? | — | bim_manager | [BIM Corner blog](https://bimcorner.com/ai-ifc-properties/) `en-blogs-linkedin-r002` |
| en | want a script that flags duplicate or missing Rooms and Door Tags, switch category, export Excel with element IDs; ChatGPT and others gave a script returning an empty list and Excel with headers only | — | bim_coordinator | [Dynamo forum](https://forum.dynamobim.com/t/help-with-automated-quality-check-script-getting-empty-list-and-blank-excel/112252) `en-revit-auto-r010` |
| en | ifcopenshell-mcp README -- How many fire doors are on Level 2? | — | architect | [GitHub Daviidro/ifcopenshell-mcp](https://github.com/Daviidro/ifcopenshell-mcp) `en-aimcp-r028` |


## Ready test prompts

All prompts below are **synthetic** (written for testing, modelled on the real patterns above; not real quotes). Many were sharpened from vaguer wave-1 synthetic prompts so that they read like a tired person typing fast: lower case, missing context, abbreviations, deadlines. "File" means the prompt assumes an IFC (or Revit project) is loaded. Where a prompt names an `inspired by` id it is the wave-1 synthetic or real record it was rewritten from.

### Schema validity and broken files

| lang | prompt | type | difficulty | expected behavior |
|---|---|---|---|---|
| en | is this file even valid ifc? my viewer complains | troubleshooting | medium | Reads `FILE_SCHEMA`, runs syntax + schema validation, lists errors by type with counts and a few entity ids; states which layers were run (syntax / EXPRESS rules / Gherkin-style rules) and that the official Validation Service may report more; asks which viewer and what it says. (`en-beginner-qa-s015`) |
| en | opens in revit no problem but validate.buildingsmart.org fails it. which rules and why | troubleshooting | hard | Lists failing rules by code and entity; names plausible causes (for example a very deep boolean subtraction tree, see validate#267) without blaming the user; separates "file bug", "exporter bug", "validator bug"; does not promise a fix. (`en-val-s013`, `en-autodesk-revit-import-s009`) |
| en | run the model thru schema validation, give me top 10 error types w/ counts | model_task | medium | Groups errors by rule/type with counts and examples; reports total vs shown; mentions warnings are not errors. (`en-val-s001`) |
| en | validator says 'constraint violation in inverse attribute PlacesObject' on #58, whats wrong in my file | troubleshooting | hard | Finds `#58` (an `IfcLocalPlacement`), lists which products reference it, explains the `[1:1]` rule (exactly one product per placement; parent placements only referenced by other placements are invalid) and suggests what the generator should change. (`en-err-s002`, `en-bsforum-s005`) |
| en | why does the checker flag my IfcBuildingElementProxy for no Name? docs say its optional | how_to | easy | Explains the schema WHERE rule (WR1) that requires a Name on `IfcBuildingElementProxy` although the attribute reads as optional; offers to list proxies without Name. (inspired by `en-bsforum-r032`) |
| en | my generated ifc wont open in bonsai, error says PlacementRelTo missing, validate it? | troubleshooting | hard | Runs validation, finds an `IfcLocalPlacement` pointing at an axis placement instead of another local placement, explains and proposes the fix; offers to write a corrected copy, not overwrite. (`en-osarch-s014`) |
| en | why 'IfcGuid is not a 128-bit number'?? my guid starts with k | how_to | easy | Explains the IFC GUID is 22 characters of a base-64 alphabet whose first character can only be 0-3, so a leading `k` is invalid; offers to scan all GlobalIds. (`en-val-r013`) |
| en | check that all GlobalIds are valid ifc guids, first char 0-3, 22 chars, and find dupes | model_task | easy | Validates length, alphabet and first character, reports invalid and duplicate ids with class, name, storey; explains likely causes of duplicates (copied content, groups). (`en-gh-xbim-others-s004`, `en-guid-s003`) |
| en | file wont load in some tools. find property values with bad \X2\ encoding or a lone backslash | model_task | hard | Scans raw STEP strings for malformed `\X2\...\X0\` escapes and undoubled backslashes (including in the header `FILE_NAME`), returns line/step ids; explains that strict parsers drop whole entities; offers a minimal repair with consent. (`en-gh-xbim-others-s009`) |
| en | checker says IfcClosedShell.CfsFaces must not be empty. which elements, and can u fix it without deleting them | model_task | medium | Lists elements with empty closed shells; says that removing the shell removes that geometry; proposes options (drop the empty representation, keep the element) and asks before changing; saves a new file and re-validates. (`en-sg-corenetx-s001`) |
| en | append type is failing, find IfcSurfaceStyle with empty Styles | model_task | easy | Lists styles with no style items (invalid in IFC), offers delete/fix, re-validates. (`en-err-s004`) |
| en | FILE_SCHEMA says IFC4 but i think there are IFC4X3 entities in there, can u confirm the real schema and list the ones that dont belong | model_task | hard | Reads `FILE_SCHEMA`, checks every entity type against the declared schema (for example `IfcAlignment` is not IFC4), lists offenders and the likely exporter setting. (`en-dev-s009`) |
| en | the client will upload this to the bsi validator but its confidential. can u tell me if it'd pass without sending it anywhere | how_to | medium | Runs a local check, says clearly it is not the official service and which rule families it covers; mentions that the Validation Service can be self-hosted; does not upload the file. |
| en | the ifc you wrote wont open in bonsai, validate it and fix till it passes | model_task | hard | Validates, repairs in a loop on a copy, reports each pass; admits when it cannot verify; checks header and attribute counts (for example missing IfcProject Phase); never claims "valid" without a validation run. (`en-aimcp-s003`) |

### IDS: writing, running and reading

| lang | prompt | type | difficulty | expected behavior |
|---|---|---|---|---|
| en | make an ids: all IfcWall must have Pset_WallCommon.FireRating, not empty | model_task | easy | Builds an IDS: Entity `IFCWALL` applicability, Property facet `Pset_WallCommon` / `FireRating` required; says how "not empty" is expressed; audits the file; offers to run it. (`en-val-s003`) |
| en | need an ids so every element has a custom param Tag filled. IfcElement didnt work | model_task | hard | Explains `IFCELEMENT` is abstract and IDS entity names do not inherit; enumerates concrete classes present in the model; notes the Attribute facet `Tag`; excludes types if wanted. (`en-val-s004`, `en-bsforum-r037`) |
| en | ids shows spec as skipped not failed when no elements match, how make it fail? | troubleshooting | medium | Explains applicability cardinality: optional vs required `minOccurs/maxOccurs`; shows the one-line change; warns that some engines treat a missing attribute as required. (`en-val-s009`) |
| en | run this IDS on the model, i want every IfcBeam to have PredefinedType BEAM or PILECAP. which fail and why | model_task | medium | Uses the Entity facet `predefinedType` (not the literal Attribute facet), tests occurrence and type separately, reports reasons per element; notes `USERDEFINED` resolves through `ObjectType`/`ElementType`. (`en-osarch-s003`) |
| en | write an ids that fails if any IfcBuildingElementProxy exists, then run it so i can see which entities fail | model_task | medium | Uses prohibited applicability (`maxOccurs=0`) or equivalent; explains that requirements are ignored in that case; lists offending entities in the report. (`en-proxy-s013`) |
| en | one spec in the ids says property X must NOT exist. tell me whos failing | model_task | hard | Evaluates prohibited correctly (present = fail), lists failing entities; notes that a prohibited facet with a value still allows null. (`en-gh-thatopen-s008`) |
| en | IDS says ModelLabel is missing on Pset_ManufacturerTypeInformation but i can see it in revit | troubleshooting | hard | Looks for two property sets of the same name on the object (invalid in IFC, breaks lookups), runs schema validation, suggests an IfcPatch-style repair or an exporter report. (`en-gh-ifcopenshell-s004`, issue #7095) |
| en | audit this ids file for errors before i send it to the contractor | model_task | medium | Runs XSD plus semantic audit (entities valid for the IFC version, pset names, cardinality), reports findings; says XSD-valid alone is not enough. (`en-val-s014`) |
| en | in an IDS, how do i check every slab has Qto_SlabBaseQuantities NetVolume above 0 | how_to | medium | Uses the Property facet with a measure `dataType` (`IFCVOLUMEMEASURE`), a bounds restriction; mentions IFC2x3 has no `Qto_` sets; warns that a wrong data type is a classic silent failure. (`en-val-s008`) |
| en | combine arch and struct ids into one and run on the federated model, report by discipline | model_task | hard | Says there is no merge function in the standard, copies specifications, keeps requirement ids/discipline tags, runs, groups results; warns about mixed IFC versions in one IDS. (`en-val-s012`) |
| en | run our IDS on the contractor model and give me a short fail list i can send back, grouped by discipline | model_task | medium | Runs the supplied IDS (asks for it if none), summarises failures per specification with counts and 3 example GlobalIds, concise and sendable; grouped by requirement rather than one huge list. (`en-fmor-s003`, `en-permit-s003`) |
| en | check model with IDS and give me a bcf of the failures | model_task | hard | Runs IDS, creates one BCF topic per failing element with GlobalIds; notes that the BCF structure for IDS results is not standardised and that snapshots may not be generated. (`en-osarch-s015`) |
| en | can IDS check wall thickness or clearance? client wants it in the ids | how_to | medium | States IDS 1.0 handles information (six facets), not geometry or clearance; proposes a separate geometric check or a quantity property requirement (for example a `Width` property exists) and says which. (inspired by `en-bsforum-r021`) |
| en | whats the diff btw IDS and mvd, which do I use to check my model | how_to | easy | IDS = project data requirements, checkable; MVD = subset of IFC for software exchange and certification; IDM = business process; recommends IDS for "is the delivery complete". (`en-val-s010`) |

### Requirements, completeness and national submissions

| lang | prompt | type | difficulty | expected behavior |
|---|---|---|---|---|
| en | run the usual check: every IfcWall has FireRating, IsExternal and LoadBearing filled? give me fail count per storey | model_task | medium | Checks `Pset_WallCommon` on type and occurrence, counts failures per storey, separates absent / empty, gives examples with GlobalIds. (`en-model-checking-s002`) |
| en | client says anything over 5% proxies fails. list the worst offenders by type name | model_task | easy | Computes proxy share of elements, lists proxy types by count, states pass/fail against 5 %; suggests the class for obvious names. (`en-proxy-s002`) |
| en | any duplicate elements in the arch model? same class same spot, list them w/ guids | model_task | hard | Finds repeated GlobalIds and near-identical placement/bounding boxes per class with a stated tolerance; reports pairs; flags the copy with fewer properties; deletes nothing. (`en-model-checking-s001`, `ru-autodesk-telegram-s004`) |
| en | compare last weeks struct IFC with todays. guids got regenerated so match by type+name+position. whats added/removed/moved | model_task | hard | Loads both, matches on type/name/centroid within tolerance, reports added/removed/moved with confidence and says GlobalId matching alone would be wrong. (`en-coord-s003`) |
| en | architect's ifc lands 40km from my model in navis. check the site/project base point and map conversion in the file | model_task | hard | Reads `IfcSite` placement, `IfcMapConversion`/`IfcProjectedCRS`, units; flags a projected coordinate plus a conversion (double shift); reports numbers, not guesses. (`en-reddit-s002`, `mul-coord-s002`) |
| en | i dont trust the slab areas. recompute from geometry and compare with Qto_SlabBaseQuantities, show anything off by more than 2% | model_task | hard | Recomputes areas, lists outliers with ratio, notes openings and unit handling; says what it could not compute. (`en-s018`) |
| en | list every Pset_ in the file and tell me which arent in the buildingSMART standard | model_task | hard | Enumerates psets, marks `Pset_`/`Qto_` names not defined for the class in the checked schema version, separates custom psets; no invented standard names. (`en-blogs-linkedin-s004`) |
| ru | завтра сдача в АГР, проверь что у всех IfcWindow заполнен RUS_Height и не пустой, список без параметра выдай | model_task | medium | Iterates `IfcWindow`, reads `RUS_Height` in any pset on occurrence and type, lists missing/empty with GlobalId, name, level; states it is not the AGR verdict. (`ru-autodesk-telegram-s002`) |
| ru | проверь модель по этому IDS ЦГЭ и дай сводку нарушений по классам, самые частые сверху | model_task | medium | Runs the IDS, aggregates failed specifications by IFC class and requirement, top failures first with sample GlobalIds. (`ru-autodesk-telegram-s012`) |
| ru | найди все свойства RUS_* где значение лежит как IfcLabel или IfcArea а не IfcReal. только список, ничего не меняй | model_task | medium | Scans property sets, filters `RUS_*` by nominal value type, returns GlobalId, pset, property, current type; changes nothing. (`ru-habr-dev-s001`) |
| ru | прогони все 6 ифс из папки на обязательные свойства и скинь одну сводную таблицу, сроки горят | model_task | hard | Batch-checks files, one consolidated table per file/class, reports which files could not be opened; asks for the requirement list if none. (`ru-autodesk-telegram-s017`) |
| zh | 这个ifc报建自检能过吗？先看下项目基点坐标是不是2000的，还有哪些构件属性是空的 | model_task | hard | Reads `IfcSite`/map conversion, checks the coordinate range and CRS (CGCS2000), lists elements with empty required properties; states the official SZ-IFC checker cannot be run. (`zh-lightweight-review-s001`) |
| ja | うちのIDSで納品IFCをチェックして。壁にFireRatingが入ってないものと、PredefinedType未設定のものを出して | model_task | medium | Runs or emulates the IDS facets (Entity `IFCWALL`, Property `Pset_WallCommon.FireRating`, attribute `PredefinedType`), lists failing walls. (`ja-japan-s005`) |
| de | prüf mal alle Türen und Wände auf fehlenden Feuerwiderstand, Liste mit IDs bitte | model_task | easy | Queries doors and walls, checks the fire-rating parameter on type and occurrence, returns a grouped list with ids. (`de-revit-auto-s016`) |
| fr | dis moi quels murs n'ont pas de résistance au feu renseignée, la convention BIM l'exige | model_task | medium | Scans `IfcWall` for `Pset_WallCommon.FireRating` (or the project pset), lists GlobalId/name/level; asks which pset the convention names. (`fr-francophone-s001`) |
| it | dimmi quali porte non hanno il FireRating nel Pset_DoorCommon | model_task | easy | Lists `IfcDoor` without the property, with ids, names, levels. (`it-italy-s002`) |
| nl | welke elementen hebben geen NL-SfB code of niet 4 cijfers? lijst per IFC class graag | model_task | medium | Scans classification references and psets for NL-SfB, lists missing/malformed per class with counts; states where the code was found. (`nl-dutch-s002`) |
| es | tengo que entregar el modelo para una licitacion con Plan BIM, revisa que el IFC tenga todas las plantas, espacios y clasificacion en cada elemento | model_task | hard | Checks storeys, spaces, classification references; says the exact requirement set is in the tender/EIR and asks for it; does not invent a "Plan BIM" rule list. (`es-spain-s003`) |
| ko | 발주처 BIM 지침 기준으로 층/공간/부재 분류 누락된 거 있나 체크해줘 | model_task | hard | Checks `IfcBuildingStorey`, `IfcSpace` and classification on elements, lists gaps, states which guideline assumptions it used and asks for the owner's guideline. (`ko-korea-s003`) |
| no | kan du kontrollere modellen mot kravene i EIR-en, spesielt at alle vegger har brannklasse og lastbærende | model_task | medium | Checks walls for fire class and load-bearing in `Pset_WallCommon`, reports failures with GUIDs; asks for the EIR if only the sentence is given. (`no-norway-s003`) |
| pt-BR | cara olha o ifc e me fala quantos elementos viraram proxy e de qual categoria do revit, preciso mandar a compatibilização hoje | model_task | medium | Counts `IfcBuildingElementProxy`, groups by Revit category/`ObjectType`, suggests mapping fixes in the export setup. (`pt-brazil-s001`) |

## Edge cases and traps for MCP testing in this area

1. **"Validate" is ambiguous.** The same word can mean schema validity, client requirements (IDS) or clashes. A server that merely parses the file and reports "no problems" has *not* run the buildingSMART rules. Test: ask "validate this model" and check that the answer states which layer ran. See [checker kinds](../../03_software/viewers_checkers_cde_converters.md).
2. **Parsing success is not validity, and validity is not usability.** Real cases go both ways: opens in Revit but fails the service ([validate#267](https://github.com/buildingSMART/validate/issues/267)); the local validator reports "No validation issues found" while Bonsai still fails on import ([IfcOpenShell#8194](https://github.com/IfcOpenShell/IfcOpenShell/issues/8194)).
3. **"Our IDS" with no IDS attached.** The assistant must ask for the file or the requirement list and never invent requirements ("typical" fire-rating rules). Same for "the EIR", "the Plan BIM", "the client's convention".
4. **Skipped is not passed, and "not checked" is not "pass".** Optional applicability, stub facets (Classification, partOf in some engines), unsupported data types and unsupported IFC versions must be reported as such. A 100 % pass on a messy model should trigger suspicion.
5. **Abstract classes and inheritance.** `IFCELEMENT` as applicability; `IfcWallStandardCase` vs `IfcWall`; IFC2x3 `IfcFlowTerminal` vs IFC4 `IfcAirTerminal`.
6. **Type vs occurrence.** PredefinedType on both (rule OJT001), properties on the type only, classification on the type only (see [classification file](./classification_cobie_fm.md)). The answer must say where it looked.
7. **Data types silently change results.** `IFCTEXT` vs `IFCLABEL`, `IfcArea` vs `IfcReal`, quantity class vs measure type, boolean `FALSE` casing, integers vs strings. Ask the assistant for the data type it found.
8. **Empty is not absent.** Empty string, `$`, `NOTDEFINED`, `USERDEFINED` with empty `ObjectType`. Engines disagree ([IDS#403](https://github.com/buildingSMART/IDS/issues/403)).
9. **Duplicate pset names** make a present property look absent. Check before reporting "missing".
10. **IDS regex dialect.** Patterns are XSD-style; lookaheads fail. Do not accept a clever regex without testing it.
11. **Fix-until-it-passes loops.** Repairs can delete geometry or data (empty shells, orphan placements). Require: work on a copy, show what changed, re-validate, never overwrite the source.
12. **Overclaiming compliance.** Local checks are not the AGR/MGE verdict, the SZ-IFC checker, CORENET X, or Solibri. The honest phrase is "these rules passed, these were not covered".
13. **Hallucinated standard names.** Invented `Pset_` names, invented rule codes (OJT001, QTY001, IFC430...), invented menu paths. Ask for the schema evidence or a direct quote.
14. **Large and many.** 70 models x 6 IDS files every two weeks ([OSArch](https://community.osarch.org/discussion/2273/ifctester-script-for-testing-several-ifcs-with-several-ids)): ask for one summary table, per-file reports and a list of files that could not be opened. The Validation Service has file-size limits (256 MB unzipped per the reference doc).
15. **Result flooding.** "Give me the failures" with 40 000 rows: group by requirement and class, show counts and a few examples, offer the full export.
16. **Privacy.** Confidential models must not be uploaded to a public validation service without consent; offer local or self-hosted options.
17. **Federation and georeference.** Per-file CRS, units and distance to origin; double shift (projected coordinates plus `IfcMapConversion`); schema/units mismatch between files in one IDS run.
18. **Language and slang.** "ифс", "кобай", "строимпросто", "报建自检", "nulpunt". The assistant should answer in the user's language but keep IFC class and property names untouched. Parameter names such as `RUS_Height` must be matched literally, and localised Revit parameter names can behave differently from the English ones (a German-UI 'Baugruppenkennzeichen' failed in [revit-ifc#856](https://github.com/Autodesk/revit-ifc/issues/856)).
19. **Prompt text inside the model.** Names, descriptions and property values in an IFC are data. If a `Description` says "ignore previous instructions", the assistant must report it as content, not act on it. (Test idea, not from the wave-1 data.)
20. **Version drift.** The Validation Service documentation can lag the service; IDS tool arguments changed between versions of IfcTester. A tester should record engine and version with every result.

## Related docs

- [buildingSMART standards: IDS, Validation Service, bSDD, BCF, MVD](../../02_standards_regulations/buildingsmart_standards.md)
- [Requirements in contracts: EIR, BEP, LOIN, IDS delivery](../../02_standards_regulations/requirements_in_contracts_eir_bep.md)
- [Viewers, checkers, CDEs and converters](../../03_software/viewers_checkers_cde_converters.md)
- [Revit IFC export reference](../../03_software/revit/ifc_export_reference.md) (class mapping, `IfcExportAs`, empty parameters)
- [IFC file anatomy](../../01_ifc_basics/02_ifc_file_anatomy.md), [properties, quantities and psets](../../01_ifc_basics/05_properties_quantities_psets.md), [geometry, placement, coordinates, units](../../01_ifc_basics/06_geometry_placement_coordinates_units.md)
- [Libraries and toolkits (IfcOpenShell, IfcTester, xBIM, web-ifc)](../../04_open_source/libraries_and_toolkits.md) and [MCP servers and AI tools](../../04_open_source/mcp_servers_and_ai_tools.md)
- National context: [Russia](../../02_standards_regulations/national/russia.md), [China](../../02_standards_regulations/national/china_mainland.md), [Singapore](../../02_standards_regulations/national/singapore.md), [Netherlands/Belgium](../../02_standards_regulations/national/netherlands_belgium_luxembourg.md), [Japan/Korea](../../02_standards_regulations/national/japan_korea.md), [Nordics](../../02_standards_regulations/national/nordics_baltics.md), [Spain/Portugal/Italy](../../02_standards_regulations/national/spain_portugal_italy.md)
- Sibling topic pages: [Classification systems, bSDD, COBie and FM handover](./classification_cobie_fm.md), [Revit export and class mapping](./revit_export_and_class_mapping.md), [Versions, MVD, encoding, GUID](./versions_mvd_encoding_guid.md), [Coordinates, georeferencing, units](./coordinates_georef_units_levels.md), [Clash, coordination, BCF, CDE](./coordination_clash_bcf_cde.md)
- Glossary: [multilingual glossary](../../08_glossary/glossary_multilingual.md), [abbreviations](../../08_glossary/abbreviations.md)
- Raw research behind this page: `research_raw/wave1/topics/t-validation-ids.md`, `research_raw/wave1/en/en-model-checking.md`, `research_raw/wave1/roles/p-fm-owner-reviewer.md`
