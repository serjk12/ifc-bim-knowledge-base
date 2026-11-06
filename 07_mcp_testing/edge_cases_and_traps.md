# Edge cases and traps that break IFC / Revit assistants

**Compiled: 2026-11-06.** For a tester with no BIM background. Companion files: [what_ifc_mcp_servers_do.md](what_ifc_mcp_servers_do.md) (what the tools can do), [evaluation_rubric.md](evaluation_rubric.md) (how to score an answer), [intent_taxonomy.md](intent_taxonomy.md) (what users ask), [sample IFC files](../04_open_source/sample_ifc_files.md) (where to get test files).

## 0. How to read this document

**Plain words.** An IFC file is a text database of building parts (walls, doors, rooms, pipes) plus their data. Real files are messy: the same fact can be stored in two places, a value can be absent, a unit can differ, a class name changed between versions. An AI assistant connected to such a file through MCP (a "plug" that lets the AI call small programs on the file) usually works well on a clean demo file and fails on a messy one. This document lists 22 families of mess ("traps"). For each one you get: what goes wrong, real evidence from the research corpus, how to get or build a test file, probe prompts in Russian and English (sometimes other languages), and what a correct answer looks like.

**Evidence rules.**
- "Real evidence" lines cite records from `research_raw/` by id and link to the public source the record came from. Nothing in this document was run against a live MCP server; "expected behavior" is what a careful BIM person would accept, not a measured result.
- Probe prompts are **synthetic** (written for this document, modeled on the phrasing patterns in [style_guide](../06_how_people_write/style_guide.md) and the synthetic prompts in the corpus). They are not quotes. Where a probe is close to a corpus prompt, its id is given.
- File-construction recipes are general IFC/IfcOpenShell knowledge, not run here. Confirm API names at <https://docs.ifcopenshell.org>. Keep originals; work on copies.
- A few facts are flagged "(general knowledge)" where the KB reference docs do not state them.

**Probe-writing conventions.** Probes are shown as they would be typed: lower case, missing punctuation, mixed terms are on purpose. Each probe has a language tag. `needs_file` is always true unless said otherwise.

### 0.1 Index

| # | Trap | Typical symptom for the user | Best test file (see [sample files](../04_open_source/sample_ifc_files.md)) |
|---|---|---|---|
| E1 | Schema differences (2x3 / 4 / 4.3, StandardCase, BuiltElement) | Count is 0 or half of expected | Duplex (2x3) vs FZK-Haus (4) vs Simple-Scene Infra (4.3) |
| E2 | Element in no storey / wrong storey | "Level 2 has 0 doors" but doors exist | Construct (section 11) or Schependomlaan |
| E3 | Several sites / buildings / federated models | Totals mix buildings; "the building" is ambiguous | Simple-Scene (10 files), Duplex + MEP |
| E4 | Odd storey names and elevations | Wrong level matched, duplicate names | Construct; Clinic |
| E5 | Type vs occurrence properties | Property "missing" or wrong value | Any Revit export; construct |
| E6 | Look-alike property sets | Two FireRating values; wrong one reported | Revit export with custom mapping; construct |
| E7 | Missing or doubtful quantities | Invented areas, openings not deducted | IfcOpenShell `--augmented` files; Duplex |
| E8 | Units (length, area, volume, flow, angle) | Numbers 1000x or 10.76x off | Construct (mm / m / ft projects) |
| E9 | Absent or contradictory georeferencing | Wrong coordinates, "no CRS" answered as a fact | Amersfoort (IFC4), xBIM `geographic-referencing-*` |
| E10 | Huge files, timeouts, context overflow | Hang, truncation, partial answer given as complete | Chesapeake bridge-tunnel; Schependomlaan; self-made 100+ MB |
| E11 | Proxies everywhere | "Walls: 0", everything is `IfcBuildingElementProxy` | Revit export with default mapping |
| E12 | Non-Latin text and STEP escapes | Mojibake, `\X2\` shown raw | xBIM encoding files; Esplanades; construct |
| E13 | Duplicate or unstable GlobalIds | Edit hits the wrong element; compare says "everything changed" | Construct; two exports of one project |
| E14 | Invalid, broken, truncated, wrong-format files | Crash, silent partial read | xBIM `Tests/TestFiles`; IfcOpenShell `files` |
| E15 | Empty vs missing vs zero | "No fire rating" vs "fire rating not filled" | Construct |
| E16 | Materials: layer sets, constituents, none | "Material: none" for a layered wall | Revit export; BlenderBIM layered wall |
| E17 | Openings and fills | Door count wrong; opening counted as a part | Duplex; FZK-Haus |
| E18 | Curtain walls and aggregates | Panels hidden, double count | Revit curtain wall export |
| E19 | MEP ports, systems, segments | Pipes without systems; flow direction | Duplex MEP / Clinic HVAC |
| E20 | Tool fingerprints (Revit, Archicad, Tekla, Renga, nanoCAD, ...) | Same question, different answer per tool | One project exported from several tools |
| E21 | Spaces, zones, room areas | Areas doubled; zone missing | Duplex rooms file; Clinic |
| E22 | Write traps (edit, rename, delete) | Silent overwrite, partial edit, no read-back | Any small copy |

### 0.2 Reference answers: how to get ground truth

Never use another LLM as truth. Use a short script on the same file (general knowledge, not run):

```python
import ifcopenshell, ifcopenshell.util.element as E, ifcopenshell.util.unit as U
f = ifcopenshell.open("copy_of_test.ifc")
print(f.schema)                                  # IFC2X3 / IFC4 / IFC4X3_ADD2
print(U.calculate_unit_scale(f))                 # length unit in metres (0.001 = mm, 0.3048 = ft)
walls = f.by_type("IfcWall")                     # includes subtypes such as IfcWallStandardCase
print(len(walls), len(f.by_type("IfcWallStandardCase")))
for w in walls[:5]:
    print(w.GlobalId, w.Name, E.get_container(w), list(E.get_psets(w)))   # psets merged type+occurrence
print(f.by_type("IfcMapConversion"), f.by_type("IfcProjectedCRS"))       # IFC4+ only
```

Write the expected numbers (counts per class, per storey, units, schema) into a one-page "answer key" **before** running the probes.

---

## E1. Schema differences: IFC2x3 vs IFC4 vs IFC4.3

**What goes wrong.** The same question gets a different correct answer depending on the schema in the file header (`FILE_SCHEMA(('IFC2X3'))`, `IFC4`, `IFC4X3_ADD2`). Typical failures: the assistant filters `IfcBuildingElement` on an IFC4.3 file (the class is now `IfcBuiltElement`, so it returns nothing) or the other way round; it reports only `IfcWall` and misses `IfcWallStandardCase` (or counts both and double counts); it asks for `IfcDuctSegment` in an IFC2x3 file, where only the generic `IfcFlowSegment` exists; it claims "this server supports IFC 4.3" when the file is an old release candidate (`IFC4X3_RC2`).

**Plain explanation.** IFC is versioned like a language with dialects. 2x3 (2006) is still very common in the field; IFC4 (2012/2017) adds many things; IFC4.3 (ISO 16739-1:2024) adds roads, rails and bridges and renames some classes. See [versions](../01_ifc_basics/01_what_is_ifc_and_versions.md) and the [entity cheat sheet](../01_ifc_basics/03_entities_cheat_sheet.md).

| Item | IFC2x3 | IFC4 | IFC4.3 (ADD2) |
|---|---|---|---|
| Parent of walls, doors, slabs | `IfcBuildingElement` | `IfcBuildingElement` | `IfcBuiltElement` (renamed, no longer abstract) |
| `IfcWallStandardCase` | normal; Revit Coordination View 2.0 writes walls this way | deprecated since IFC4 ADD2 TC1 (may be read, should not be written) | still readable, deprecated |
| Duct / pipe segment classes | only `IfcFlowSegment` | `IfcDuctSegment`, `IfcPipeSegment` | same as IFC4 |
| Triangulated mesh geometry | not available | `IfcTriangulatedFaceSet` | yes |
| Georeferencing | by convention (Pset on site) | `IfcMapConversion` + `IfcProjectedCRS` | same, plus scaled / rigid variants |
| Roads, bridges, alignments | no | partial intermediate versions (4.1, 4.2) | `IfcRoad`, `IfcBridge`, `IfcAlignment` |

**Real evidence.**
- Walls exported inconsistently as `IfcWall` or `IfcWallStandardCase` from the same Revit project; both valid in the 2x3 Coordination View: `p-student-r015` (<https://forums.buildingsmart.org/t/difference-between-expectations-and-reality-of-ifc-standards/1040>). `IfcWall` lacking base quantities that `IfcWallStandardCase` had: `p-student-r024` (<https://github.com/Autodesk/revit-ifc/issues/364>).
- Ducts and pipes arrive as generic types in 2x3: `en-autodesk-revit-export-r024` (<https://forums.autodesk.com/t5/revit-mep-forum/ifc-export-ducts-and-pipes/td-p/12370919>).
- Old release candidates are a separate trap: KIT road is `IFC4x3_RC2`, KIT bridge is `IFC 4x2` ([sample files, section 4 and 9](../04_open_source/sample_ifc_files.md)).

**Test files.** Duplex Apartment or Medical-Dental Clinic (IFC2x3), FZK-Haus (IFC4), Simple-Scene `Infra-*.ifc` (IFC4.3), KIT road (4x3_RC2). Same questions on all four.

**Probes.**
- EN: `how many walls are in this model? total, and split by type if there's more than one wall class`
- RU: `сколько стен в модели? только не потеряй StandardCase, в 2x3 они почему-то отдельно`
- EN (on IFC4.3): `list every IfcBuildingElement and count them` (the class is gone in 4.3; a good answer says so and uses the 4.3 name)
- RU: `покажи все воздуховоды` (on a 2x3 file: expect "в IFC2x3 нет IfcDuctSegment, воздуховоды лежат как IfcFlowSegment" and a count)
- EN: `does this server handle ifc 4.3? give me the road alignment length` (on a 2x3 building file: no alignment, say so)

**Expected correct behavior.**
- States the schema from the header before the numbers (or at least when it matters).
- Counts walls with subtypes included; says how many are `IfcWallStandardCase` and how many plain `IfcWall`; no double counting.
- Uses the class names that exist in this schema, or explains the rename; does not return "0" without checking the schema.
- Says plainly when a requested class cannot exist in this version.
- Does not claim a feature for an unsupported version (see [what servers do, L11](what_ifc_mcp_servers_do.md)).

---

## E2. Elements not contained in any storey (or contained in the wrong one)

**What goes wrong.** In IFC an element "belongs" to a floor only if a containment relationship (`IfcRelContainedInSpatialStructure`) says so. If it is missing, or the element is attached to the building or the site directly, "doors on Level 2" silently omits it. Assistants then report "0 doors on level 2" or, worse, a total that excludes the orphans without saying so. The opposite also happens: elements land on the wrong storey because of export settings.

**Real evidence.**
- Elements on levels not flagged as "Building Story" land on the wrong `IfcBuildingStorey`: `en-blogs-linkedin-r016` (<https://bim-me-up.com/ifcbuildingstorey/>); levels split between Project Base Point and Survey Point as base put elements on the wrong level: `en-autodesk-revit-export-r026` (<https://forums.autodesk.com/t5/revit-architecture-forum/elements-are-being-exported-to-the-wrong-ifc-level/td-p/11927737>).
- Pre-check tools flag "elements without storey ancestor": `en-sg-corenetx-r007` (<https://github.com/LUOaini1213/ifcsg-precheck>).
- A common export mistake list names extra storeys and duplicated walls of other disciplines: `en-blogs-linkedin-r020` (<https://bimcorner.com/10-common-ifc-export-mistakes-to-avoid-part-1/>).

**Test file.** Build: take a small model, delete the containment relationship for 3 doors (or attach them to `IfcBuilding`), see [sample files section 11, "Missing storeys / elements outside the hierarchy"](../04_open_source/sample_ifc_files.md). Real alternative: Schependomlaan (Synchro-changed storey trees).

**Probes.**
- EN: `how many doors on level 2?`
- EN: `give me door counts per storey and make sure the total matches the whole model`
- RU: `сколько дверей на втором этаже? а в целом по зданию?`
- RU: `есть элементы которые не привязаны ни к одному этажу? покажи`

**Expected correct behavior.**
- Per-storey counts plus an explicit line for "not assigned to any storey" so the sum equals the model total (for example 38 total = 12 + 14 + 9 + 3 unassigned).
- For the "per storey" request, a mismatch between sum and total is explained, not hidden.
- Names the storey by its actual `Name` and, if the user said "level 2", states which storey that is (see E4).

---

## E3. Multiple sites, buildings, or several federated models

**What goes wrong.** Many IFC files have exactly one project, one site, one building. Some have two buildings, two sites, or are a merge of architecture + structure + MEP. A question such as "what is the height of the building?" or "total floor area" then has no single answer. Assistants average, pick the first building without saying so, or add numbers of overlapping models (the architect's wall and the structural wall are two objects in one place). Revit exports only one site and one building per file; to get more, models are linked ([bim-me-up](https://bim-me-up.com/ifc-struktur/), `en-blogs-linkedin-r014`).

**Real evidence.** `en-blogs-linkedin-r014` (<https://bim-me-up.com/ifc-struktur/>): Revit exports one `IfcSite` and one `IfcBuilding`; link models into one `IfcProject` for several. Singapore guidance asks for one `IfcSite`: `en-arch-r031` (<https://info.corenet.gov.sg/ifc-sg/model-setup-and-coord>). Duplicated walls from other disciplines in a federated export: `en-blogs-linkedin-r020`.

**Test files.** Simple-Scene (10 files with building + infrastructure, [sample files section 2](../04_open_source/sample_ifc_files.md)); Duplex architecture + MEP files loaded together; or merge two copies of FZK-Haus in IfcOpenShell so you know there are two identical buildings.

**Probes.**
- EN: `what's the total gross floor area of the building?` (on a two-building file)
- RU: `сколько этажей в здании?` (two buildings with 3 and 5 storeys)
- EN: `i loaded the architecture and the hvac file together. how many walls?` (expect: asks or splits per file; does not add MEP "walls")
- ES: `¿cuántas plantas tiene el edificio?`

**Expected correct behavior.**
- Notices that there are two buildings (or two sites) and either asks "which one?" or gives a per-building breakdown with names.
- Never merges counts of different source files without saying "counted across both models; may include duplicates".
- Keeps `IfcSite` and `IfcBuilding` names in the answer so the user can verify.

---

## E4. Odd storey names, elevations and count

**What goes wrong.** Storey names are free text: "Level 1", "Этаж 1", "+0.000", "EG", "UG 01", "Roof", duplicates ("Level 1" twice from two linked models). Elevations may be in millimetres or metres, relative to the internal origin, project base point or survey point, so "Level 2 elevation = 3000" is not the same as "+3.00 m above ground". Revit "supporting levels" turned into storeys give extra storeys. Assistants match "level 2" to the wrong storey (the second in list order, not the one named "Level 2"), or compare elevations in different units.

**Real evidence.** Extra storeys in exported files: `en-blogs-linkedin-r020`. Rooms/levels exported high by the project elevation when levels use Survey Point as base: `en-gh-revit-ifc-r026` / `en-autodesk-revit-export-r014` (<https://github.com/Autodesk/revit-ifc/issues/907>). Link IFC in Revit 2025-2027 creates levels at double elevation: `en-gh-revit-ifc-r021` (<https://github.com/Autodesk/revit-ifc/issues/990>). Pre-check rule "non-unique storey names": `en-sg-corenetx-r007`. Corpus synthetic prompts for this: `ru-arch-s011`, `ru-autodesk-telegram-s007`, `p-student-s009`.

**Test file.** Construct: rename two storeys identically, set elevations 0, 3000, 3000, add a storey named "-0.150" and one named "Крыша" ("roof"). Real: Clinic (two storeys, check names).

**Probes.**
- RU: `выведи этажи с отметками и сколько элементов на каждом, лишние уровни тоже покажи` (close to `ru-autodesk-telegram-s007`)
- EN: `what's the elevation of level 2 in meters?`
- RU: `проверь этажи и отметки, чтобы совпадали с КР, завтра сдача` (close to `ru-arch-s011`; needs a second file to compare, otherwise a good answer asks for it)
- EN: `are there duplicate level names in this model?`

**Expected correct behavior.**
- Lists storeys in elevation order with their exact names, elevation with unit (e.g. `3000 mm = 3.000 m`), and element counts.
- When two storeys share a name, says so and uses GlobalId to tell them apart; does not silently merge them.
- Flags storeys with 0 elements and unusual elevation values; does not claim "levels match structure" without a second file.
- If asked "level 2" and names are in another language or scheme, asks or states the assumed mapping.

---

## E5. Type vs occurrence property overrides

**What goes wrong.** A property can sit on the occurrence (this particular wall) and/or on the type (the "wall type" shared by many walls). The occurrence value overrides the type value. Tools that read only one level report "no FireRating" while the value is on the type, or report the type value when this wall has its own different value. For Revit this is the "type parameter vs instance parameter" split.

**Real evidence.** Type parameters missing in IFC psets until the option "Allow use of type properties in instance property sets" is ticked: `es-spain-r005` (<https://forums.autodesk.com/t5/revit-architecture-forum/issues-with-exporting-type-parameters-from-revit-to-ifc/td-p/14004505>). Since Revit 2023 type parameters no longer export into the common instance Pset in some cases: `en-blogs-linkedin-r018`. One Revit type becomes 3 IFC types: `en-gh-revit-ifc-r056` (<https://github.com/Autodesk/revit-ifc/issues/809>). Scripts failing because type parameters must be read from the type element: `en-revit-auto-r018`. Italian beginner asking where a wall's FireRating lives: `it-italy-r012`.

**Test file.** Construct: wall type with `Pset_WallCommon.FireRating = "EI60"`; five occurrences, of which two carry their own `FireRating = "EI90"` and one has none anywhere. Expected: 2 x EI90, 2 x EI60 (inherited), 1 x not set.

**Probes.**
- EN: `which walls have fire rating EI60?`
- RU: `у каких стен огнестойкость EI90? покажи id`
- EN: `walls show FireRating in revit but it's empty in the ifc. why?` (needs an explanation, not only a query)
- EN: `change the fire rating of wall type W-200 to EI120` (type-level edit: affects all occurrences without their own override; a good answer says so and asks)

**Expected correct behavior.**
- Reads occurrence first, falls back to type, and says which level the value came from ("inherited from type W-200").
- Reports the five walls separately in the example above, not "5 walls with EI60".
- Explains in plain words why a value may appear on the type only.
- For edits: asks whether to change the type (all walls) or one wall; reports how many elements are affected (see E22).

---

## E6. Look-alike property sets

**What goes wrong.** The standard set `Pset_WallCommon` has a property `FireRating`. Real files also contain: a custom set `Pset_WallCommon_Custom`, a set named `Pset_WallCommon` written by a non-standard exporter with different fields, Revit's own "Identity Data"/"Dimensions" sets, a property `FireRating` in three different sets, `Fire Rating`, `Brandschutzklasse`, `Огнестойкость`, `RUS_FireResistance`. Assistants pick the first match, mix them, or confuse a custom set that starts with `Pset_` (reserved for buildingSMART) with the standard one.

**Real evidence.** User parameter cannot overwrite `Pset_WallCommon.LoadBearing`, built-in wins on name clash: `de-dach-r012` (<https://github.com/Autodesk/revit-ifc/issues/833>). Case-insensitive name clash overwrites user Volume/Area with built-in values: `de-dach-r021` (<https://github.com/Autodesk/revit-ifc/issues/989>). Dutch guideline: own property sets must not start with `Pset`: `nl-dutch-r020` (<https://www.digigo.nu/ilsen-en-richtlijnen/bim-basis-ils/3-7-gebruik-propertysets>). Custom properties not exported due to scope, type-vs-instance, duplicate names: `en-autodesk-revit-export-r004`. Russian practice with `RUS_*` properties: `ru-habr-dev-r004` (<https://habr.com/ru/articles/1094224/>).

**Test file.** Construct: one wall with `Pset_WallCommon.FireRating="EI60"`, `Revit_Identity.FireRating="EI30"`, `Pset_WallCommon_X.FireRating=""`. Real: any Revit export with a user mapping file.

**Probes.**
- EN: `what is the fire rating of wall 2O2Fr$t4X7Zf8NOew3FLOH?` (use a real GlobalId from your file)
- RU: `у этой стены две огнестойкости в разных наборах, какая правильная?`
- EN: `find all properties called FireRating in the file and tell me which property sets they come from`
- EN: `is Pset_Wall_Custom a standard buildingSMART pset?` (knowledge probe)

**Expected correct behavior.**
- Prefers the standard set name for a standard question, but shows the others and says they disagree.
- Does not merge values; reports `set.property = value` for each.
- Does not assert "standard" for a set that only looks like it; says the name pattern `Pset_*` is reserved for buildingSMART and custom sets should avoid it.

---

## E7. Missing or doubtful quantities

**What goes wrong.** Areas and volumes live in quantity sets (`Qto_WallBaseQuantities` in IFC4; many 2x3 exporters call the set `BaseQuantities`). Many files have none, some have them only for some classes, some have wrong ones. Questions like "net wall area per storey" force the assistant to choose: read the stored value, compute from geometry, or refuse. Common failures: invents a number, silently mixes stored and computed values, does not say whether openings are deducted, uses gross for net.

**Real evidence.** Six walls of different geometry show identical first `NetSideArea`: `en-qto-r024` (<https://github.com/Autodesk/revit-ifc/issues/141>). Base quantities missing on some walls and roofs, mostly with voids: `en-autodesk-revit-export-r028`. `Width` missing in `Qto_CoveringBaseQuantities`: `de-dach-r013` (<https://github.com/Autodesk/revit-ifc/issues/872>). Incorrect `GrossVolume`, `OuterSurfaceArea` in Revit 2022.1: `en-arch-r029` (<https://github.com/Autodesk/revit-ifc/issues/361>). Room QTO "34 records calculated but nothing in quantity sets": `en-gh-ifcopenshell-r025`. Corpus prompts: `en-aimcp-s004`, `de-dach-s007`.

**Test files.** IfcOpenShell `files` repo with `--augmented` in the name (quantities added by `IfcConvert --calculate-quantities`) vs the same file without it ([sample files section 5](../04_open_source/sample_ifc_files.md)); Duplex (quantities partial). Construct: delete all `IfcElementQuantity` from a copy.

**Probes.**
- EN: `net wall area per storey, tell me where the numbers come from`
- RU: `посчитай объём бетона по перекрытиям, в м3, и скажи откуда взяты значения`
- EN: `total window area on the south facade` (needs orientation data; a good answer says what is missing)
- RU: `площадь стен с учётом проёмов или без? в модели нет BaseQuantities`
- EN: `give me the quantity takeoff for the whole building` (broad request; expect scoping questions)

**Expected correct behavior.**
- Says which source it used per number: stored `Qto_*`, computed from geometry, or not available.
- Says whether openings are subtracted (net) or not (gross); does not label gross as net.
- For missing quantities, either computes with a named method and warns about accuracy, or says "not in the model" and offers options. Never produces a plausible number without a tool result.
- Totals add up; units stated (m2, m3).
- See [what servers do, L13](what_ifc_mcp_servers_do.md) and [quantities questions](../05_real_world_questions/by_topic/quantities_cost_schedule.md).

---

## E8. Units: length, area, volume, flow, angle

**What goes wrong.** Every IFC file declares units (in `IfcUnitAssignment`): length may be millimetre, metre or foot; area and volume units are separate and are often plain square/cubic metres even when length is millimetres. Numbers in property sets follow the unit of their *measure type* (an `IfcLengthMeasure` follows the length unit, an `IfcAreaMeasure` follows the area unit). Failures: reading `3000` as metres; reporting areas in mm2 when they are in m2; converting only length; treating feet as metres; ignoring the project unit when reporting "distance from origin"; flow rates and angles with the wrong unit.

Quick conversions (general knowledge): 1 ft = 304.8 mm = 0.3048 m; 1 m2 = 10.7639 ft2; 1 ft2 = 0.092903 m2; 1 ft3 = 0.0283168 m3. A typical door is 900 to 1000 mm wide, or 0.9 m, or about 3 ft; if a door is "900 m" the unit is wrong.

**Real evidence.**
- Clash annotation in mm for a project in feet: `en-gh-ifcopenshell-r008` (<https://github.com/IfcOpenShell/IfcOpenShell/issues/7178>).
- Beam system spacing exported as feet divided by 304.8 in a mm project (0.0065 instead of 609.6): `en-gh-revit-ifc-r001` (<https://github.com/Autodesk/revit-ifc/issues/1015>).
- Flow in L/s exported as ft3/s: `en-gh-revit-ifc-r042` (<https://github.com/Autodesk/revit-ifc/issues/444>). Typed 15 degrees exports as 15.35: `en-gh-revit-ifc-r058` (<https://github.com/Autodesk/revit-ifc/issues/954>).
- A "systematic unit bug" ticket: `en-autodesk-revit-import-r050` (<https://github.com/Autodesk/revit-ifc/issues/576>, title only seen).
- Areas written as `IfcArea` / `IfcLabel` instead of `IfcReal` rejected by IDS validator: `ru-habr-dev-r004`.
- Corpus synthetic: `ru-dwg-revit-s013`, `ru-tim-expertiza-s009`, `en-osarch-s009`.

**Test files.** Construct three copies: length unit mm, m, ft (with `IfcConversionBasedUnit`). Add a wall 5 m long. Expected answers: 5000 (mm file), 5 (m file), 16.404 (ft file), all meaning 5 m. Real mix: Revit sample projects exported in imperial vs metric templates ([sample files section 8](../04_open_source/sample_ifc_files.md)).

**Probes.**
- EN: `how long is the longest wall? in meters please`
- RU: `высота дверей какая? в миллиметрах`
- EN: `how far is the model from the origin?` (file in feet)
- RU: `площадь всех плит, в квадратных метрах` (file where lengths are mm but areas are already m2)
- EN: `the numbers look 1000x too big. what unit is this model in?`
- DE: `wie breit ist die breiteste tür, in zentimetern?`

**Expected correct behavior.**
- Reads and states the project units before giving numbers ("length unit: millimetre; area: square metre").
- Converts correctly and shows the converted number *and* the source value when it could confuse.
- Does not assume area unit = length unit squared.
- If values are implausible (door 900 m), flags a likely unit/scale problem instead of repeating them.
- See [coordinates, units](../01_ifc_basics/06_geometry_placement_coordinates_units.md).

---

## E9. Absent or contradictory georeferencing

**What goes wrong.** Georeferencing says where the building is on Earth. In IFC4 it is stored in `IfcMapConversion` + `IfcProjectedCRS`; in IFC2x3 only by convention. Files often have: none; site latitude/longitude but no map conversion; `IfcMapConversion` with Eastings/Northings = 0; two different positions (site placement and map conversion applied twice); a far-from-origin placement (hundreds of kilometres) that breaks viewers; true north in a different place than the conversion. Assistants answer "the building is at 0,0" or hallucinate an EPSG code, or add the offset twice.

**Real evidence.**
- Two products write `IfcMapConversion` while also using projected coordinates as model coordinates, so the offset is applied twice: `en-bsforum-r025` (<https://forums.buildingsmart.org/t/5695>).
- Site IFC and building IFC each carry the True North rotation, so the combination is rotated twice: `de-dach-r005` (<https://github.com/Autodesk/revit-ifc/issues/301>).
- Shared-coordinates export lands in a different place: `en-autodesk-revit-export-r011` (<https://forums.autodesk.com/t5/revit-structure-forum/ifc-shared-coordinates-export-issue/td-p/10143119>); wrong elevation even with the IfcSite option ticked, ~20 cm offsets: `en-autodesk-revit-export-r013`.
- Same bridge, three IFC files; national-grid coordinates make viewers jitter: `en-blogs-linkedin-r001` (<https://bimcorner.com/same-bridge-three-ifc-files/>).
- Pre-check flags "no IfcMapConversion": `en-sg-corenetx-r007`. Corpus prompts: `ru-autodesk-telegram-s016`, `ru-autodesk-telegram-s006`, `ru-dwg-other-s014`.
- Reference: [georeferencing section](../01_ifc_basics/06_geometry_placement_coordinates_units.md) (precedence: `IfcMapConversion` wins over site latitude/longitude; True North informational).

**Test files.** "Example project location" (Amersfoort, IFC4, EPSG 28992) with a known 100 m trap; xBIM `geographic-referencing-*.ifc` (IFC 4.3); a plain building (no georeference). Construct: copy the plain building and add Eastings 155000 / Northings 463000 (Dutch RD) per [sample files section 11](../04_open_source/sample_ifc_files.md).

**Probes.**
- EN: `what coordinate system is this model in? give me the epsg code`
- RU: `в файле какие координаты у IfcSite и угол истинного севера, в МСК или локальные` (close to `ru-autodesk-telegram-s016`)
- EN: `where on earth is this building? lat/lon please`
- RU: `АР и ОВ не совмещаются по координатам, глянь где у них смещение`
- ZH: `这个模型有地理参照吗？坐标系是什么？`

**Expected correct behavior.**
- Says explicitly "no `IfcMapConversion` / no `IfcProjectedCRS` in this file" when absent. Does not invent an EPSG.
- When both site lat/lon and map conversion exist and disagree, reports both and says which is authoritative (map conversion in IFC4).
- Gives the easting/northing with units and the CRS name exactly as stored; warns when the model sits far from the origin.
- For the AR vs MEP comparison: needs both files; computes the offset between their conversions and states the unit.
- Does not apply the transformation twice when converting local to global.

---

## E10. Huge files, timeouts, context overflow

**What goes wrong.** Models of 100 MB to several GB take minutes to open. MCP clients time out; the server returns half a list; the assistant dumps 50,000 rows into the chat or stops after the first 100 and presents them as complete. Loop-retries create duplicates on write. Also, large tool catalogs fill the context window before work starts.

**Real evidence.** Large files can take over a minute; cancelling does not stop Python: `en-aimcp-r027` (<https://github.com/flinker-app/ifc-mcp>). Timeouts on large models, base64 screenshots: `en-aimcp-r026` (<https://github.com/JotaDeRodriguez/Bonsai_mcp>). Context constantly compacted with large tool catalogs: `en-aimcp-r008` (<https://github.com/bimwright/rvt-mcp/issues/23>). Blender hanging while loading an IFC: `en-beginner-qa-r008` (<https://github.com/IfcOpenShell/IfcOpenShell/issues/6433>). Revit IFC export stalling 12+ hours: `en-autodesk-revit-export-r031`. Two-hour export before errors are visible: `ru-habr-dev-r001` (<https://habr.com/ru/articles/1089018/>). Single-element failures on a retry: Tapir idempotency issue ([what servers do, L3](what_ifc_mcp_servers_do.md)).

**Test files.** Chesapeake Bay Bridge-Tunnel (about 26 MB, 295k entities); Schependomlaan; self-made: copy a building 50 to 100 times with IfcOpenShell to reach 100 to 500 MB ([sample files section 10](../04_open_source/sample_ifc_files.md)). Never host or share the files; licences.

**Probes.**
- EN: `list every element in the model with its name and guid`
- RU: `выведи все стены с площадью, их тысяч пять наверное`
- EN: `count elements by ifc class and tell me when you're done` (large file; patience test)
- RU: `этот файл 400 мб, откроется вообще? сколько там элементов`
- EN: `export all property sets of all doors to a table` (expect: file output or paging, not a wall of text)

**Expected correct behavior.**
- Uses aggregate tools (counts by class) first, not full listings.
- When output is truncated or paged, says so ("showing 100 of 5,213; the rest is in `walls.csv`").
- On timeout: reports the timeout, says what was and was not completed, does not claim a partial list is complete, and does not retry writes blindly.
- Gives an honest time/size warning before a heavy operation when it can know.

---

## E11. Proxies everywhere

**What goes wrong.** `IfcBuildingElementProxy` is the "generic thing" class. Exporters use it when they cannot map an object (Revit Generic Models, in-place families, sweeps, fascias, anything with an invalid class name). A file with hundreds of proxies answers "how many walls?" with a low number because many walls are proxies, with names like "Wall". Assistants either count only `IfcWall` without warning or "fix" by guessing a class from the name.

**Real evidence.** Floors silently skipped while other categories fall back to proxy: `de-dach-r018` (<https://github.com/Autodesk/revit-ifc/issues/759>). Sub-elements follow host, fascias and wall sweeps stay proxy: `de-dach-r020` (<https://github.com/Autodesk/revit-ifc/issues/481>). One proxy type auto-generated per element, hundreds of them, likely from curtain wall reveals: `en-autodesk-revit-export-r019` (<https://github.com/Autodesk/revit-ifc/issues/676>). `IfcExportAs` ignored for slab edges: `en-autodesk-revit-export-r001`. Bridge exported three ways with 161 proxies: `en-blogs-linkedin-r001`. Russian debate "proxy is a crutch": `ru-habr-dev-r020` (<https://habr.com/ru/articles/590819/comments/>). Corpus prompt `ru-dwg-other-s007` ("все проксики с именем Wall* переделай в IfcWall").

**Test file.** Revit export of a model where Generic Models carry wall-like names; or construct: change 20 walls to `IfcBuildingElementProxy` keeping Name = "Wall-...".

**Probes.**
- EN: `how many walls are there?` (20 of 100 are proxies named "Wall")
- RU: `сколько в модели проксей и что это за элементы`
- RU: `все проксики с именем Wall* переделай в IfcWall, остальное не трогай`
- EN: `why is my IFC full of proxies?`

**Expected correct behavior.**
- Reports `IfcWall` count and the proxy count, and notes proxies whose names look like walls.
- Does not reclassify automatically; explains that a class change is an edit, lists the affected elements, keeps GlobalIds, and asks for confirmation (E22).
- Explanation in plain words: proxy = "exporter could not tell what this is"; root cause lies in export mapping settings, not in the file reader.

---

## E12. Non-Latin text and STEP escapes

**What goes wrong.** IFC is a plain-text file (STEP, ISO 10303-21) restricted to ASCII. Non-Latin characters are written as escapes: `\X2\0421\X0\` is a capital Cyrillic "С"; a whole word such as "Стена" is `\X2\042104420435043D0430\X0\` (general knowledge: UTF-16 hex code points). Real files also contain raw Cyrillic (invalid), mixed escapes and raw characters, a wrong code page (Windows-1251 read as UTF-8), a line break inside an escaped string, or an apostrophe/quote doubled (`''`). Assistants show the escapes raw, show mojibake, crash, or "fix" names wrongly.

**Real evidence.**
- Raw Cyrillic next to `\X2\` pieces in a SolidWorks export; Python read fails; maintainer: raw Cyrillic is invalid IFC, the exporter must escape all non-ASCII: `en-gh-encoding-r017` (<https://github.com/IfcOpenShell/IfcOpenShell/issues/3182>).
- Property string with Russian address containing a line break breaks geometry loading in a new xBIM Xplorer: `en-gh-xbim-others-r008` (<https://github.com/xBimTeam/XbimEssentials/issues/660>); one malformed escape drops many entities: `en-gh-xbim-others-r019` (<https://github.com/xBimTeam/XbimEssentials/issues/605>).
- Tekla refuses an IFC "with special characters in the name" though the name is Latin; Cyrillic in the header path suspected: `ru-dwg-other-r010` (<https://forum.dwg.ru/showthread.php?t=159943>).
- Revit parsing errors that were parser bugs (string ending in escaped quote `8''` is valid): `en-coord-r008` (<https://forums.buildingsmart.org/t/a-number-of-interesting-revit-ifc-parsing-errors/4605>).
- IfcXml failing under Turkish locale (culture-sensitive upper-casing): `en-gh-xbim-others-r003` (<https://github.com/xBimTeam/XbimEssentials/issues/670>).
- Corpus synthetic: `ru-renga-nanocad-s010`, `ru-tim-expertiza-s005`, `ru-dwg-other-s003`, `zh-csdn-dev-s002`.

**Test files.** xBIM `Wrongly1251Encoded.ifc`, `InvalidMultiByte.ifc`, `EmptyMultibyteString.ifc`, `SpecicalSolidusEscape.ifc`, `DoubleBackSlashName.ifc`, `NewlinesInStrings.ifc`; Estonian `Esplanades`; Russian-named model built by yourself ([sample files section 6 and 11](../04_open_source/sample_ifc_files.md)). What exactly each xBIM file contains was not verified, only the names.

**Probes.**
- RU: `в ифс кракозябры вместо русских названий, найди где поломано`
- EN: `some names show as weird codes with backslashes. what's wrong?`
- RU: `покажи все стены с названием «Стена наружная 380»` (name exists in file as escapes; the assistant must match)
- ZH: `名称显示乱码，帮我找出受影响的构件`
- EN: `rename wall "Стена-1" to "Стена-2" and show the result` (round-trip write; see E22)
- EN: `what's written in the file header? exporter, schema, any non-ascii paths`

**Expected correct behavior.**
- Displays decoded readable text for correct escapes (С т е н а), not `\X2\...`.
- For truly broken strings: lists affected entities (class, GlobalId, attribute) and distinguishes "invalid file" from "tool bug".
- Does not claim a parse crash is "your Cyrillic".
- After a write, re-reads the value and shows it identical, preserving non-Latin characters.
- Answers in the user's language (see rubric: language match).

---

## E13. Duplicate or unstable GlobalIds

**What goes wrong.** Each element has a 22-character GlobalId. It should be unique and stable across exports so that two versions can be compared. In practice: copied files keep the same GUIDs; some exporters regenerate them at each export; some elements share one; Civil 3D does not write them. Assistants that "find element by GlobalId" and "compare two files" then target the wrong element or report "everything changed / everything new".

**Real evidence.** Duplicate GlobalIds across files from one project (duplicating a Revit file preserves UniqueIds): `en-gh-revit-ifc-r043` (<https://github.com/Autodesk/revit-ifc/issues/378>). Walls get random GUIDs at each export after a collision: `de-dach-r007` (<https://github.com/Autodesk/revit-ifc/issues/109>); steel elements new GUIDs each export: `de-dach-r008`; `IFCGuid` parameter differs from exported GUID: `en-autodesk-revit-export-r038`. Civil 3D elements keep or lack GUIDs: `en-dynamo-pyrevit-r017`. Random GlobalIds in a bad bridge export: `en-blogs-linkedin-r001`. Pre-check "duplicate GlobalId": `en-sg-corenetx-r007`. Clash tracing needs GUID kept: `ru-dwg-other-r028` (<https://rengabim.com/stati/prohodim-gosekspertizu-informacionnoj-modeli-pravilno/>).

**Test file.** Construct: assign the same GlobalId to two walls ([sample files section 11](../04_open_source/sample_ifc_files.md)); export the same project twice from a tool that regenerates GUIDs; or open two copies of one model as "v1" and "v2".

**Probes.**
- EN: `are there any duplicate guids in this file?`
- RU: `сравни две версии модели, что изменилось` (v2 has entirely new GUIDs: expect a caution, not "all 4,000 elements changed")
- EN: `set Comments = "checked" on the element with guid <duplicate-guid>`
- RU: `найди дубли элементов — одинаковый класс, почти одинаковая геометрия или одинаковый GlobalId`

**Expected correct behavior.**
- Detects and reports duplicates with both elements' class and name.
- Refuses to edit "by GUID" when the GUID is ambiguous; asks which one.
- In a compare, notices when the share of matching GUIDs is near zero and falls back to a secondary key (name + class + storey) or says the comparison is unreliable.
- Never mixes up GlobalId (22 chars, IFC) and Revit ElementId (integer).

---

## E14. Invalid, truncated, wrong-format files; LLM-written IFC

**What goes wrong.** Files that are not valid IFC: truncated, missing `ENDSEC;`, wrong header, wrong attribute count, lower-case keywords, wrong extension, a zipped `.ifczip`, an XML `.ifcxml`, an empty project. Some parsers are strict, some lenient; the assistant may crash, hang, or answer from a partial read as if complete. AI-written IFC is a special case: an LLM generating STEP text often gets attribute counts wrong.

**Real evidence.** An IFC written by an LLM ("originating system OpenAI") has 8 attributes in `IfcProject` instead of 9 and does not open; maintainers: validate at the buildingSMART service and loop until it passes: `en-aimcp-r013` (<https://github.com/IfcOpenShell/IfcOpenShell/issues/7945>). Lower-case STEP names and enums from a Vectorworks combined model crash Blender: `en-gh-ifcopenshell-r030` (<https://github.com/IfcOpenShell/IfcOpenShell/issues/5213>). "Symbol error, unexpected character, parsing terminated": `en-gh-ifcopenshell-r041` (<https://github.com/IfcOpenShell/IfcOpenShell/issues/1501>). Exporter from SAPFIR 3D gives "System Error encountered during import": `ru-autodesk-telegram-r003`. Compact `IfcRelDefinesByProperties` with a set of psets reported invalid: `en-bsforum-r022` (<https://forums.buildingsmart.org/t/5521>). Empty export caused by the Revit interface language: `es-latam-r008`.

**Test files.** xBIM `Tests/TestFiles`: `Badly formed Ifc file.ifc`, `FormallyIllegalFile.ifc`, `InvalidHeaderFileName.ifc`, `InvalidType.ifc`, `fileWithAbstractClass.ifc`, `Large_entity_label.ifc`, `RealWithExponent.ifc`; IfcOpenShell `files` (`--accept-errors`); self-made truncated copy; renamed `.txt`; `.ifczip`. Note: "valid but weird" and "invalid" are different categories; many community files do not validate yet are fine for testing ([sample files section 3 and 11](../04_open_source/sample_ifc_files.md)).

**Probes.**
- EN: `open this file and tell me what's in it` (truncated copy)
- RU: `файл не открывается, посмотри что с ним`
- EN: `create a small ifc with one wall and one door, then open it` (generation; expect validation)
- EN: `is this file valid ifc? check it`
- RU: `открой model.txt` (an IFC with the wrong extension)

**Expected correct behavior.**
- Reports a parse error with location or message and states what could and could not be read.
- Distinguishes "file is broken" from "my tool failed".
- For generated IFC: validates (or says it cannot) and repairs; does not hand over an unchecked file as "ready".
- Identifies format by content, not only by extension; handles `.ifczip` or explains it is unsupported.
- No hang; a bounded time.

---

## E15. Empty vs missing vs zero vs "not applicable"

**What goes wrong.** In STEP, `$` means "unset". An empty string `''`, the value `0`, the text "n/a", "-", a whitespace string and a missing property are different things, though a user hears them all as "empty". Assistants conflate them: "no fire rating" when the property exists with `''`; "fire rating = 0" when it was unset; counting `''` as a rating; suggesting an element "fails" when its data was never expected.

**Real evidence.** Deleting parameters with blank values is unreliable (`HasValue` vs whitespace): `en-revit-auto-r014` (<https://forum.dynamobim.com/t/delete-parameters-with-blank-value/115164>). `IsExternal` empty for columns since Revit has no Function for them: `en-blogs-linkedin-r018`. One malformed value makes `NominalValue` null while the entity survives: `en-gh-xbim-others-r019`. Russian check "Two hours of export for an empty parameter": `ru-habr-dev-r001` (<https://habr.com/ru/articles/1089018/>). Design rule PASS / FAIL / UNKNOWN, never estimate: `en-aimcp-r029` (<https://github.com/zeussilver/bim-ifc-mcp>).

**Test file.** Construct five doors: FireRating `"EI30"`, `""`, `"-"`, property absent, pset absent. Expected report: 1 value, 1 empty string, 1 placeholder, 2 not present (property absent / pset absent).

**Probes.**
- EN: `which doors don't have a fire rating?`
- RU: `у каких дверей не заполнена огнестойкость? раздели «пусто» и «нет такого свойства»`
- EN: `check door clear width >= 850, don't guess` (some doors have no width; see [what servers do, L7](what_ifc_mcp_servers_do.md))
- EN: `what percent of walls have all required properties filled in?` (needs a definition of "required"; expect a question or a stated assumption)

**Expected correct behavior.**
- Separates "property absent", "present but empty", "placeholder", and "value" in the answer.
- Gives UNKNOWN (not PASS or FAIL) for missing data when asked to check a rule.
- Lists affected GlobalIds (or a count with a way to get the list).
- States the definition used for "empty".

---

## E16. Materials: layer sets, constituents, none

**What goes wrong.** Material information can be: a single material on the element; a layered build-up (`IfcMaterialLayerSet`, usually via `IfcMaterialLayerSetUsage`) with thicknesses; a list of constituents (`IfcMaterialConstituentSet`) for windows and doors; a material only on the *type*; a material on a geometry item (colour/style, not a real material); nothing. The IFC4 Reference View excludes layer sets, so a file may validly lack them. Assistants answer "Material: none" when it sits on the type or in a layer set, or "Concrete" for a wall made of concrete plus insulation plus plaster.

**Real evidence.** Material layers are excluded from the IFC4 Reference View: `en-bsforum-r044` (<https://forums.buildingsmart.org/t/3638>). Materials sit on representation items, types and layer sets; many assignment paths: `en-gh-xbim-others-r011` (<https://github.com/xBimTeam/XbimEssentials/issues/642>). Layer data missing for thermal analysis: `p-student-r015`. A wall is not a Revit wall until it has a layer set: `en-autodesk-revit-import-r014` (<https://github.com/Autodesk/revit-ifc/issues/778>). Duct fitting material lost; workaround `IfcSingleMaterialOverride`: `en-autodesk-revit-export-r025`. Coloring one layer colors the whole wall: `en-gh-thatopen-r023` (<https://github.com/ThatOpen/engine_web-ifc/issues/1733>). Layered walls in BlenderBIM: `en-osarch-r029` (<https://community.osarch.org/discussion/261/layered-walls-in-blenderbim>).

**Test files.** BlenderBIM/Bonsai layered wall; a Revit export in 2x3 Coordination View vs IFC4 Reference View of the same project; Duplex; or construct a wall with a 3-layer set (concrete 200 / insulation 100 / plaster 20).

**Probes.**
- EN: `what are the exterior walls made of? give me layers and thicknesses`
- RU: `из чего сделаны наружные стены, слои с толщинами`
- EN: `total volume of concrete in the building`
- RU: `у окон нет материала, это норма?`
- EN: `list all distinct materials in the model with usage counts`

**Expected correct behavior.**
- Reports layers in order with thickness and unit (e.g. "concrete 200 mm, insulation 100 mm, plaster 20 mm; total 320 mm") and that the data came from the layer set (or the type).
- Where only a single name exists, says "no layer breakdown in this file".
- For "volume of concrete", uses layer thickness times area or stored material quantities, says which; warns when volumes are totals of the element, not of one material.
- Explains in plain terms why windows often carry no single material.

---

## E17. Openings and fills

**What goes wrong.** A door in a wall is represented as three things: the door, an opening (void) cut into the wall (`IfcOpeningElement`, linked by `IfcRelVoidsElement`), and a "fills" link (`IfcRelFillsElement`). Questions such as "how many openings are in the wall" or "net area of the wall" depend on whether openings are present and whether the quantity set deducted them. Assistants count `IfcOpeningElement` as real parts, forget that doors and windows already imply openings, or double count door + opening. Exporters sometimes skip the opening cut.

**Real evidence.** Wall exported uncut with no opening when a beam top equals the wall top (1 mm offset fixes it): `de-dach-r002` (<https://github.com/Autodesk/revit-ifc/issues/985>). Shaft openings in floors missing: `de-dach-r001` (<https://github.com/Autodesk/revit-ifc/issues/609>). Floor openings broken by exporter version: `de-dach-r006` (<https://github.com/Autodesk/revit-ifc/issues/530>). Windows offset out of the wall face after importing Archicad IFC: `de-dach-r017` (<https://github.com/Autodesk/revit-ifc/issues/1019>). Door swings invisible in plan: `en-autodesk-revit-import-r010`. MEP penetrations workflow requested as AI tools: `zh-revit-auto-r026`. `get_openings_on_wall` exists in a server's tool list: `en-aimcp-r039` (<https://github.com/smartaec/ifcMCP>).

**Test file.** Duplex or FZK-Haus (walls with doors/windows); IfcOpenShell `files` with `--missing-subtractions` in the name; construct a wall with a 900 x 2100 mm door and check the `IfcOpeningElement` exists.

**Probes.**
- EN: `how many openings are in the exterior walls?`
- RU: `сколько проёмов в стене ... и какие двери/окна в них стоят`
- EN: `net wall area minus doors and windows, level 1`
- RU: `есть окна которые не вставлены ни в какой проём?`

**Expected correct behavior.**
- Distinguishes the opening (void) from the thing in it (door/window) and reports both without double counting.
- Reports openings that are empty (void without fill) separately.
- For net area, says whether openings were deducted from stored quantities or by calculation.
- Flags walls that clearly should have an opening but have none (only when the data supports it).

---

## E18. Curtain walls and aggregates

**What goes wrong.** A curtain wall is an assembly: an `IfcCurtainWall` with parts (panels as plates or windows, mullions as members) tied by `IfcRelAggregates`. Counting "windows" or "walls" may include or exclude panels; "area of the facade" may be one object or hundreds; quantities may be stored on the assembly or on the parts. Exporter bugs hide panels deep in the hierarchy or crash.

**Real evidence.** Panels hidden deep in the IFC hierarchy: `en-autodesk-revit-export-r021` (<https://forums.autodesk.com/t5/revit-architecture-forum/advanced-ifc-export-of-curtain-wall-revit-2018/td-p/8590346>). Export as a single IfcCurtainWall with parts retained: `en-autodesk-revit-export-r022` (<https://forums.autodesk.com/t5/revit-architecture-forum/export-curtain-wall-to-ifc-as-a-single-object/td-p/12907563>). Curtain wall export crashes in IFC4: `de-dach-r022` (<https://github.com/Autodesk/revit-ifc/issues/992>). Walls and curtain walls can not be forced to `IfcCovering` via `IfcExportAs`: `en-gh-proxy-r016` (<https://github.com/Autodesk/revit-ifc/issues/155>). Hundreds of auto-generated proxy types from reveals: `en-autodesk-revit-export-r019`.

**Test file.** A Revit export with a curtain wall (Snowdon Towers facade discipline; [sample files section 8](../04_open_source/sample_ifc_files.md)); or IFC4 files from Archicad with curtain walls.

**Probes.**
- EN: `how many windows are in the building? don't count curtain wall panels twice`
- RU: `сколько штук витражей и сколько в них панелей и импостов`
- EN: `total glazed area of the facade`
- RU: `почему в модели одни пластины вместо окон`

**Expected correct behavior.**
- Reports curtain walls as assemblies and their parts separately (e.g. "6 curtain walls, 148 panels, 92 mullions").
- Tells the user when a total includes or excludes panels.
- Does not add the assembly area and the part areas together.

---

## E19. MEP: ports, systems, segments

**What goes wrong.** Pipes and ducts are segments; fittings and equipment have ports (`IfcDistributionPort`) linked by `IfcRelConnectsPorts`; the logical network "Supply Air 1" is an `IfcDistributionSystem`, joined by `IfcRelAssignsToGroup`. Questions like "what is connected to this pump?" or "total length of the supply air system" need ports and systems, which many exports omit. Assistants sum all duct segments, invent connectivity from geometry, or confuse system type (supply) with flow direction (source/sink). In 2x3, segment classes are generic.

**Real evidence.** Ducts and pipes as generic types in 2x3: `en-autodesk-revit-export-r024`. Duct fitting material lost: `en-autodesk-revit-export-r025`. Linking an MEP IFC drops many elements as non-DirectShape, model ~70 m from origin: `en-autodesk-revit-import-r006` (<https://github.com/Autodesk/revit-ifc/issues/658>). Flow units wrong: `en-gh-revit-ifc-r042`. "list all pipes" failing with *Method not found* (server/plugin mismatch): `en-aimcp-r020` (<https://github.com/mcp-servers-for-revit/revit-mcp/issues/28>). MEP takeoff with duct size, length, area, gauge, kilos; fittings area direct, geometric estimate or fallback factor, method reported: `es-aimcp-r032` (<https://github.com/JefaturaBIM94/RevitMCPBOQ>). Contain cables and equipment in `IfcSpace`: `en-spaces-r036` (<https://community.osarch.org/discussion/3316/ifcspace-good-for-spatial-containment-of-ifcdistributionelements>). Reference: [domains: MEP](../01_ifc_basics/08_domains_mep_structural_infra_4d5d_fm.md).

**Test files.** Duplex MEP / Electrical / Plumbing; Clinic HVAC and Plumbing ([sample files section 3](../04_open_source/sample_ifc_files.md)); Simple-Scene `Building-Hvac.ifc`, `Infra-Plumbing.ifc`.

**Probes.**
- EN: `total length of ducts per system`
- RU: `что подключено к вентилятору В-1? покажи цепочку`
- EN: `which pipes aren't assigned to any system?`
- RU: `покажи все трубы` (Revit not running or file with no pipes: honest failure)
- EN: `what's the flow direction on this port?`

**Expected correct behavior.**
- Groups by system when system assignment exists; reports unassigned segments as their own group.
- States clearly when port/connection data is absent and does not infer connectivity from geometry unless it labels the result as an estimate.
- Handles the class availability by schema (E1).
- Lengths in stated units; ducts and pipes not mixed.

---

## E20. Authoring-tool fingerprints

**What goes wrong.** The tool that wrote the file shapes what is in it: names, classes, property sets, units, geometry type, how storeys and types are expressed. A question that works on one fingerprint fails on another. The assistant should recognise the exporter from the header (`FILE_NAME` originating system) and adapt, and must not apply Revit assumptions to a Tekla file.

| Source | Typical traits seen in corpus | Evidence |
|---|---|---|
| Revit | Names like `Basic Wall:Generic - 200mm:123456`; `IfcExportAs` / mapping file control classes; walls as `IfcWall` or StandardCase by setting; Revit-specific psets; proxies for Generic Models; levels vs Survey Point issues | `p-student-r015`, `en-autodesk-revit-export-r011`, `en-gh-proxy-r016` |
| Archicad | Classification and property mapping set up in export translator; doors' plan symbols; IFC4 common | `en-blogs-linkedin-r030` (<https://bimcorner.com/exporting-ifc-from-archicad/>), `en-autodesk-revit-import-r010` |
| Tekla | Brace as `IfcMember`; export type options (Coordination View 2.0, Steel Fabrication View); huge files; rebar | `en-blogs-linkedin-r033` (<https://bimcorner.com/export-a-tekla-structures-model-to-an-ifc-file/>), `ru-dwg-other-r018` (<https://forum.dwg.ru/showthread.php?t=150272&page=2>) |
| Renga | Properties exported via mapping JSON in the IFCMap folder; use IFC4 for coordination; tessellation recommended for Navisworks | `ru-dwg-other-r026`, `ru-dwg-other-r028` (<https://rengabim.com/stati/prohodim-gosekspertizu-informacionnoj-modeli-pravilno/>), `ru-autodesk-telegram-r018` |
| nanoCAD (SPDS) | Needs mapping of grids to `IfcGrid`, `IfcExportAs` in shared parameters, level splitting of walls | `ru-autodesk-telegram-r019` (<https://sapr.ru/article/25825>) |
| SolidWorks / SAPFIR-3D / Vectorworks | Raw non-ASCII, system errors on import, lower-case keywords | `en-gh-encoding-r017`, `ru-autodesk-telegram-r003`, `en-gh-ifcopenshell-r030` |
| Civil 3D | GUIDs not written by the exporter | `en-dynamo-pyrevit-r017` |

**Test file.** One small project exported from two or three tools (not available as a public set; build it yourself if you have licences) or use public models from different origins: Duplex (Revit 2x3), FZK-Haus (Archicad 20), Schependomlaan (Archicad design model plus subcontractor files), KIT bridge (SketchUp, hand-edited) ([sample files](../04_open_source/sample_ifc_files.md)).

**Probes.**
- EN: `which software made this file and which export settings?`
- RU: `этот файл из Ренги, посмотри свойства стен`
- EN: `why do the walls in this tekla file have no base quantities?`
- RU: `в Revit-экспорте названия типа "Базовая стена:Generic - 200мм:123456" — как получить чистое название типа?`

**Expected correct behavior.**
- Reads the originating-system and schema info from the header and states it.
- Names a plausible cause tied to the exporter without being certain ("Tekla exports this as `IfcMember`; that's a setting of the export, not a corrupt file").
- Does not claim to know the exporter's internal settings; points to the setting category.

---

## E21. Spaces, zones, room areas

**What goes wrong.** Rooms are `IfcSpace`; areas can be a stored quantity (`Qto_SpaceBaseQuantities`), a property from the authoring tool, or computed from geometry; they may differ (boundary rules, thickness of walls, zone curves). Zones/groups are not spatial; they live in `IfcZone`. Russian practice has area-of-flat computations (ТЭП) that differ from geometric area. Assistants add up areas that include "gross" and "net"; duplicates inflate totals.

**Real evidence.** Zones with imperfect boundaries compute in Revit but fail IFC export: `ru-habr-dev-r002` (<https://habr.com/ru/articles/1089018/>). Zones disappear and areas are doubled in an upload check: `ru-autodesk-telegram-r008`. Differences of ~20 m2 between ТЭП in XML and the IFC; duplicates by bounding box: `ru-autodesk-telegram-r010` (<https://habr.com/ru/articles/1100956/>). Room area cannot be mapped to custom pset: `en-gh-revit-ifc-r004` (<https://github.com/Autodesk/revit-ifc/issues/855>). Excluding Areas from the export with `IfcExportAs=DONTEXPORT`: `en-autodesk-revit-export-r016`. Rooms exported with wrong elevation: `en-gh-revit-ifc-r026`.

**Test file.** Duplex (rooms and spaces file `Duplex_M_..._ROOMS_AND_SPACES.ifc`); Clinic.

**Probes.**
- EN: `total area of all rooms on level 1, and list the ones larger than 30 m2`
- RU: `сумма площадей помещений по этажам, сравни с площадью по контуру`
- EN: `which rooms have no number or no name?`
- RU: `дубли помещений есть? одинаковые номера`

**Expected correct behavior.**
- States the source and kind of area (stored net floor area, gross, computed).
- Reports duplicate numbers and unnamed spaces with GlobalIds.
- Does not sum gross and net together; does not count duplicates twice.

---

## E22. Write traps: edit, rename, delete

**What goes wrong.** Everything above becomes dangerous the moment the request changes the model. Typical failures: edits applied without a preview or confirmation; the file overwritten in place; a type-level edit that touches hundreds of elements; "done" claimed without a read-back; wrong target (first level, origin) because a default was used; lost non-Latin text; duplicates on retry; code executed via the escape hatch although a specific tool exists.

**Real evidence.** `create_wall` used the first Level and Z=0 by default (<https://github.com/shuotao/REVIT_MCP_study/issues/144>, taken from [what servers do, L6](what_ifc_mcp_servers_do.md); not re-checked here); door unhosted at origin (<https://github.com/bimwright/rvt-mcp/issues/13>); all mutating tools failing while reads work: `en-aimcp-r005` (<https://github.com/bimwright/rvt-mcp/issues/21>); stairs hang and crash with the code escape hatch: `en-aimcp-r006` (<https://github.com/bimwright/rvt-mcp/issues/14>); a model "confidently claimed success" on 8 of 15 deterministic tasks (<https://github.com/mcp-servers-for-revit/mcp-servers-for-revit/issues/30>, via [what servers do, L5](what_ifc_mcp_servers_do.md); related record `en-revit-auto-r031`). Desired workflow: dry-run, confirmation, apply, log, undo: `zh-aimcp-r033` (<https://github.com/5788324/Yang-Agent_Revit>). Corpus prompts: `ru-revit-auto-s008`, `ru-dwg-other-s007`.

**Test file.** A copy of any small model. Work only on copies.

**Probes.**
- EN: `add a property FireRating=EI60 to all doors and save`
- RU: `поставь всем дверям на втором этаже огнестойкость EI30 и покажи что получилось`
- RU: `переименуй все виды по шаблону, но дубли имён не плодить` (close to `ru-revit-auto-s008`)
- EN: `delete all the empty storeys`
- EN: `set Comments = X on all walls on Level 02, then show me the result`
- RU: `удали все проксики` (destructive and ambiguous)

**Expected correct behavior.**
- Before writing: restates the target set and count ("27 doors on storey "Level 2""), asks for confirmation when the change is bulk, type-level or destructive.
- Writes to a copy or tells the user the original will change; mentions undo or backup.
- After writing: re-reads and reports the new values and the number of elements changed; reports failures per element.
- No silent default targets (level, position, type); asks.
- Uses the dedicated tool; declares it when running code.
- Never claims "done" without read-back.

---

## Appendix A. Combined stress scenarios

Use these when one probe at a time is not enough.

| Scenario | Combines | Setup | Probe (EN) | Probe (RU) |
|---|---|---|---|---|
| S1 "Messy Revit 2x3 export" | E1, E2, E5, E11, E12 | Revit-style IFC2x3; some walls proxies; Cyrillic names; type-level FireRating | `give me a quick health report of this file` | `сделай быстрый отчёт по файлу: что внутри, что не так` |
| S2 "Wrong units, far away" | E8, E9, E10 | Feet project, national grid coordinates | `why does the model look huge and far from the origin?` | `модель улетела далеко от нуля и вроде слишком большая, в чём дело` |
| S3 "Pre-handover check" | E2, E4, E9, E13, E15 | Duplicate GUID, orphans, no CRS, empty properties | `is this ready for submission? list everything missing` | `готов ли файл к сдаче на экспертизу, что не хватает` |
| S4 "Federated MEP" | E3, E19, E21 | Architecture + HVAC + rooms | `ducts per room per storey` | `воздуховоды по помещениям и этажам` |
| S5 "Edit on a messy file" | E5, E11, E13, E22 | Type + occurrence + duplicate GUID | `set all fire doors to EI60` | `сделай все противопожарные двери EI60` |

For each scenario the answer key must contain: schema, units, counts per class and storey, list of orphans, list of duplicates, CRS status, property fill rate. Score with the [rubric](evaluation_rubric.md).

## Appendix B. Mapping traps to the other KB documents

| Trap | Read also |
|---|---|
| E1, E11, E20 | [Revit export and class mapping questions](../05_real_world_questions/by_topic/revit_export_and_class_mapping.md), [versions, MVD, encoding, GUID](../05_real_world_questions/by_topic/versions_mvd_encoding_guid.md) |
| E2, E3, E4, E8, E9 | [Coordinates, georef, units, levels](../05_real_world_questions/by_topic/coordinates_georef_units_levels.md), [spatial structure](../01_ifc_basics/04_spatial_structure_and_relationships.md) |
| E5, E6, E15 | [Properties and parameters](../05_real_world_questions/by_topic/properties_and_parameters.md), [psets and quantities](../01_ifc_basics/05_properties_quantities_psets.md) |
| E7, E21 | [Quantities and cost](../05_real_world_questions/by_topic/quantities_cost_schedule.md), [materials, spaces, zones](../05_real_world_questions/by_topic/materials_spaces_zones.md) |
| E10, E14 | [File size, viewing, conversion](../05_real_world_questions/by_topic/file_size_viewing_conversion.md), [validation and IDS](../05_real_world_questions/by_topic/validation_ids_model_checking.md) |
| E12, E13 | [Versions, MVD, encoding, GUID](../05_real_world_questions/by_topic/versions_mvd_encoding_guid.md) |
| E16, E17, E18 | [Materials](../01_ifc_basics/07_materials_classification_types_styles.md), [openings, curtain walls](../05_real_world_questions/by_topic/geometry_openings_curtainwalls_stairs.md) |
| E19 | [MEP and structural questions](../05_real_world_questions/by_topic/mep_structural_rebar.md) |
| E22 | [what servers do, 6.4 Write safety](what_ifc_mcp_servers_do.md), [anti-patterns in LLM questions](../06_how_people_write/anti_patterns_llm_questions.md) |
| Vocabulary | [abbreviations](../08_glossary/abbreviations.md), [multilingual glossary](../08_glossary/glossary_multilingual.md) |

## Appendix C. Gaps and caveats

- Nothing here was run against a server or a file. Real-evidence records come from forum and GitHub threads; some answers in the corpus are "not read" or "open" and are cited only for the symptom.
- No real log of MCP user sessions exists in the corpus; probes are modeled on forum phrasing, not on measured assistant traffic.
- File recipes are general IFC knowledge. What exactly is inside each xBIM `Invalid*` file and each IfcOpenShell regression file was not verified (names only).
- Licence status of many public sample files is unconfirmed (see [sample files](../04_open_source/sample_ifc_files.md)); do not redistribute them.
- Numbers such as conversion factors and the `\X2\` code points are standard values (general knowledge) and are not taken from the corpus.
- Non-English coverage: Russian and English probes are in every case; German, Spanish and Chinese appear only where a corpus record supports the pattern. Add other languages by translating the English probe and keeping the same expected behavior.
