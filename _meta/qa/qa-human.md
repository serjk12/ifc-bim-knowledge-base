# QA log: realism audit of the test prompts (human-voice pass)

**Date:** 2026-11-06. **Pass name:** qa-human. **Scope:** do the test requests in the prompt banks and in the "Ready test prompts" sections sound like real people typing to an AI that sees an IFC model or a Revit project, and are the "Expected" lines right about IFC and Revit?

**Files audited (read in full):**
- [prompt_bank_ru.md](../../07_mcp_testing/prompt_bank_ru.md): 272 single-turn prompts + 20 dialogs (80 turns)
- [prompt_bank_en.md](../../07_mcp_testing/prompt_bank_en.md): 283 prompts + 20 dialogs (79 turns)
- [prompt_bank_multilingual.md](../../07_mcp_testing/prompt_bank_multilingual.md): 170 prompts in 14 languages
- [ru.md, section 6 "Ready test prompts"](../../05_real_world_questions/by_language/ru.md): 130 prompts (P-001 to P-130)
- [en.md, "Ready test prompts"](../../05_real_world_questions/by_language/en.md): 77 prompts (P01 to P77)

**Files changed:** those five and this log. Nothing else was edited. Git was not used.

**Standard used:** [style_guide.md](../../06_how_people_write/style_guide.md) (ten rules, section 6 politeness, section 12 assistant-prompt register, section 14 checklist, section 16 knobs) and [anti_patterns_llm_questions.md](../../06_how_people_write/anti_patterns_llm_questions.md) (AP1 to AP19, batch targets in section 4, lint in section 6).

---

## 1. Verdict

The banks were already close to the standard. They are short, lowercase where the language allows it, point at "this model", carry exact class and property names, include deadlines and honest-answer clauses, and avoid greetings. The weak spots were few and specific:

1. **Wrong or too flat facts in Expected lines** (20 edits). The worst: a Revit family type (типоразмер) was said *not* to be an IFC type object (it is: Family Type -> `IfcXxxType`); "IFC2x4 does not exist" (it was the working name of IFC4); "IFC has no standard vertical-datum field" (`IfcProjectedCRS` has an optional `VerticalDatum`); "spaces/grids are normal" as geometry-free items (spatial structure elements are, spaces are not); `FireRating` offered as a way to tell exterior walls (the property is `IsExternal`); `PILECAP` as a value of an `IfcBeam` predefined type (it is not).
2. **Near-duplicates inside one file** (10 edits). Replaced with a different, still realistic task so the counts stay the same.
3. **Over-polished or caricatured wording** (17 edits). "Could you ... so I can", "kindly tell me how many number of", "Добрый день! Подскажите, пожалуйста", "sir please", "Quick one." and similar. In Russian, politeness markers in typed-to-AI prompts are about 1% in the data; in English "could you / please" is 7%.

47 edits logged (46 distinct rows; `en.md` P32 was edited twice): 20 fact, 10 duplicate, 17 tone. Row counts, IDs and the smoke-set lists are unchanged; the summary tables at the top of the three banks and the difficulty line in `ru.md` were recomputed (section 7).

---

## 2. Method

| Step | What was done |
|---|---|
| Real-voice calibration | `python tools/kb.py stats --kind real --lang ru` (109 records) and `--lang en` (2,245 records); `filter --kind real --lang ru` read in pages (60 records); `filter --kind real --lang en --text "(claude\|chatgpt\|llm\|mcp).*(prompt\|asked\|ask)"` (19 records, the only real typed-to-AI material: README prompt lists and quotes inside GitHub issues). These README prompts are imperative and plain ("How many fire doors are on Level 2?", "Find missing names, classifications, and suspicious property values in this IFC file.", "Georeference this IFC model using EPSG:4326"), which is what the banks imitate. |
| Mechanical lint on every prompt | Word counts, greeting / please / thanks / persona-costume / "comprehensive" markers (anti-patterns section 6), comma-list and parallel-criteria detector, newline and markdown detector, first-word distribution, contraction and slang rate. A token-overlap scan (stemmed Jaccard >= 0.33 inside each bank) found the near-duplicates; pairs that are deliberate (parallel sets across languages, cross-file copies) were ignored. |
| Fact check | Every Expected line in the three banks, plus the dialog turns and the Expected lines in `ru.md` / `en.md`, was read against [01_ifc_basics](../../01_ifc_basics/), [03_software/revit](../../03_software/revit/), [02_standards_regulations](../../02_standards_regulations/) and the raw records. Claims the KB marks "unverified" were hedged, not asserted. |
| Edit rules | Row IDs, backend tags, file flags and column layout were kept; difficulty and persona changed only where the new task needed it. Where a duplicate was replaced, the origin became `N` and the summary tables were recomputed with a script that first reproduced the old numbers exactly. Original line endings (the files mix CRLF and LF) were preserved. |

Not done: nothing was run against a real MCP server; Korean, French, Portuguese and Arabic casual style remains unverified by a native speaker (the style guide says the same).

---

## 3. Batch profile before and after (typed-to-AI prompts, single-turn)

| Measure | RU bank | EN bank | Multilingual bank | Target from style guide |
|---|---|---|---|---|
| Rows | 272 | 283 | 170 | |
| Median words | 12 | 15 | 13.5 -> 14 | 14 to 15 |
| 5 words or fewer (title-only style) | 11 (4%) | 11 (4%) | n/a | about 5% |
| More than 25 words | 0 | 7 -> 5 | 0 | rare, only with a pasted detail |
| Contains please / could you / kindly / sir / thanks / пожалуйста / bitte | 2 -> 1 | 19 -> 11 | 3 -> 3 | EN about 7%, RU about 1% |
| Greeting or self-introduction | 0 | 1 (PRS-08, kept) | 0 | none |
| Line breaks, bullets, bold in a prompt | 0 | 0 | 0 | none |
| Slang / transliteration (RU) or dropped apostrophes and abbreviations (EN) | 103 (38%) | 66 (23%) | n/a | RU slang concentrated, EN mostly plain with a few abbreviations |
| Has an explicit motive (deadline, person waiting, "for X"), keyword heuristic | about 50 (18%) | about 44 (16%) | n/a | about 1 in 3 (see section 8) |

---

## 4. Changes

Each item gives the file, the row ID, why it was changed, and the text before and after. "Expected" is the English column that tells a tester what a good answer does. Prompts are quoted in their original language.

### 4.1 Wrong, shaky or over-flat IFC/Revit facts in Expected behaviour or in the prompt (20)

- **prompt_bank_ru.md INV-08**. IfcMapConversion is IFC4+, TrueNorth lives on the geometric context in every schema; IFC2x3 has the EPset convention.
  - Expected before: [IFC] IfcSite coordinates and true north, projected or local. Read RefLatitude/RefLongitude/RefElevation, IfcMapConversion/TrueNorth if IFC4; say clearly "local" if no map conversion; do not name a CRS the file does not state.
  - Expected after: [IFC] IfcSite coordinates and true north, projected or local. Read RefLatitude/RefLongitude/RefElevation and the context TrueNorth (any schema); IfcMapConversion + IfcProjectedCRS exist only in IFC4 and later (on IFC2x3 look for EPset_MapConversion / EPset_ProjectedCRS property sets); say clearly "local" if no map conversion is found; do not name a CRS the file does not state.
- **prompt_bank_ru.md INV-12**. FireRating does not tell exterior from interior; IsExternal does.
  - Expected before: [IFC] Layer build-up of exterior walls. Read IfcMaterialLayerSet per wall type; "exterior" must come from IsExternal/FireRating-style property, otherwise say it cannot be told and ask.
  - Expected after: [IFC] Layer build-up of exterior walls. Read IfcMaterialLayerSet per wall type; "exterior" must come from the IsExternal property (Pset_WallCommon) or from a type-name convention the user states, otherwise say it cannot be told and ask.
- **prompt_bank_ru.md INV-20**. "spaces are normal" was wrong: IfcSpace normally has geometry; the geometry-free ones are spatial structure elements and sometimes grids.
  - Expected before: [IFC] Elements with no geometry. Find IfcProduct with no Representation, group by class; explain spaces/grids are normal.
  - Expected after: [IFC] Elements with no geometry. Find IfcProduct with no Representation, group by class; explain which geometry-free items are normal (IfcSite, IfcBuilding, IfcBuildingStorey, sometimes IfcGrid) and which are suspicious (an IfcSpace, wall or door with no representation).
- **prompt_bank_ru.md EDG-14**. IFC2x4 was the working name of IFC4 (01_ifc_basics/01_what_is_ifc_and_versions.md), not a schema that "does not exist" in the abstract.
  - Expected before: [IFC] IFC2x4 does not exist. Say that no such schema exists; show the real FILE_SCHEMA; ask whether the brief means IFC2x3 or IFC4.
  - Expected after: [IFC] IFC2x4 was only the development name of IFC4; no published schema carries that name. Show the real FILE_SCHEMA from the header (IFC2X3 or IFC4), say that "IFC2x4" in the brief most likely means IFC4 and ask the user to confirm; must not report having "checked IFC2x4".
- **prompt_bank_ru.md MOD-11**. IFC2x3 has no map-conversion entities but a property-set convention exists; rotation is stored as an x-axis vector, so "12 degrees" has to be converted.
  - Expected before: [IFC] Set map conversion: eastings/northings/rotation. Needs IFC4 IfcMapConversion + IfcProjectedCRS; on IFC2x3 explain the limitation; do not invent the EPSG code for "МСК-50" (zone-specific, user must confirm).
  - Expected after: [IFC] Set map conversion: eastings/northings/rotation. IFC4 and later: IfcMapConversion + IfcProjectedCRS, rotation stored as XAxisAbscissa/XAxisOrdinate (so 12 degrees must be converted and the values shown). IFC2x3 has no such entities; the convention is the EPset_MapConversion / EPset_ProjectedCRS property sets (say which route was taken). Do not invent the EPSG code for "МСК-50" (zone-specific, user must confirm). Write on a copy.
- **prompt_bank_ru.md TRB-01**. The phase explanation comes from forum guesses, not a confirmed cause.
  - Expected before: [either] IFC opens in Revit empty, only grids. Typical cause: phase of the linked IFC / view filters; check if the file itself has geometry; explain Link vs Open.
  - Expected after: [either] IFC opens in Revit empty, only grids. Forum answers point at the phase assigned to a linked IFC or at view settings, but the cause is not confirmed; check if the file itself has geometry; explain Link vs Open.
- **prompt_bank_ru.md VAL-15**. Revit puts the room number in IfcSpace.Name and the room name in LongName (01_ifc_basics/04_spatial_structure_and_relationships.md).
  - Expected before: [IFC] Rooms with no area, zero area or no name. List IfcSpace with empty/zero area quantity or name, by storey.
  - Expected after: [IFC] Rooms with no area, zero area or no name. List IfcSpace with empty/zero area quantity or name, by storey. In a Revit export Name usually holds the room number and LongName the room name, so "no name" must look at LongName too; say which attribute was used.
- **prompt_bank_en.md MOD-07**. IFC2x3 has no IfcMapConversion but the EPset convention exists; units trap for metre-based EPSG:28992.
  - Expected before: [IFC] Writes a map conversion with those values on a copy, mentions the model must be IFC4 or later and that this relocates the model in map space without moving its geometry.
  - Expected after: [IFC] Writes a map conversion with those values on a copy, mentions IfcMapConversion + IfcProjectedCRS exist only in IFC4 and later (on IFC2x3 the convention is the EPset_MapConversion / EPset_ProjectedCRS property sets), that this relocates the model in map space without moving its geometry, and that RD eastings/northings are in metres, so a model in millimetres needs the scale set.
- **prompt_bank_en.md VAL-13**. PILECAP is not a value of IfcBeamTypeEnum (pile caps are IfcFooting PILE_CAP); JOIST is a valid IfcBeam value.
  - Prompt before: `run this IDS against the model, I want every IfcBeam to have PredefinedType BEAM or PILECAP. which ones fail and why?`
  - Prompt after: `run this IDS against the model, I want every IfcBeam to have PredefinedType BEAM or JOIST. which ones fail and why?`
- **prompt_bank_en.md TRB-23**. PlacementRelTo is an optional attribute of IfcLocalPlacement; "missing" is not automatically a schema error.
  - Expected before: [IFC] Validates, shows the offending local placements, explains the missing reference; offers to repair on a copy.
  - Expected after: [IFC] Validates the file and lists local placements without PlacementRelTo. Notes that the attribute is optional in the schema (empty means placed directly in world coordinates), so the message may come from the loader, not from a schema violation; checks whether the affected elements should sit in a storey/building placement chain; offers to repair on a copy.
- **prompt_bank_en.md QTY-03**. Revit room number/name mapping (Name vs LongName).
  - Expected before: [IFC] One table, one row per space; marks spaces without area as "no area" instead of 0.
  - Expected after: [IFC] One table, one row per space; marks spaces without area as "no area" instead of 0. Says which attribute holds the number and which the name (a Revit export puts the number in Name and the room name in LongName).
- **prompt_bank_en.md VAL-27**. Revit room number/name mapping (Name vs LongName).
  - Expected before: [IFC] Missing name, number or area per space, counts, level, GlobalId. Does not say the portal will accept the file.
  - Expected after: [IFC] Missing name, number or area per space, counts, level, GlobalId. Checks LongName as well as Name (a Revit export puts the number in Name and the room name in LongName) and says which it used. Does not say the portal will accept the file.
- **ru.md P-085**. The claim comes from 2020-era forum answers, not from the vendor; hedged.
  - Before: Explain that AutoCAD has no native IFC import; the file opens in Revit or Tekla;
  - After: Forum answers of that period say AutoCAD has no native IFC import (newer versions and vertical products may differ, so hedge); the file opens in Revit or Tekla;
- **ru.md P-088**. Same source and same hedge as P-085.
  - Before: No native import; options:
  - After: Forum answers say plain AutoCAD does not edit IFC (verify for the user's version); options:
- **en.md P16**. MGA zone 56 exists in both datums; a modern project may use GDA2020.
  - Before: compare the CRS name with EPSG:28356,
  - After: compare the CRS name with EPSG:28356 (GDA94 / MGA 56) or EPSG:7856 (GDA2020 / MGA 56), whichever datum the project states,
- **en.md P40**. "deprecated in IFC4" is not settled in 01_ifc_basics/03_entities_cheat_sheet.md.
  - Before: explain CV2.0 rules and that StandardCase is deprecated in IFC4.
  - After: explain that StandardCase is the typical IFC2x3 Coordination View 2.0 output and that IFC4 exports use plain IfcWall (StandardCase is discouraged in newer IFC4 revisions; the exact version is unverified in this KB).
- **prompt_bank_ru.md KNW-04**. Wrong: a Revit family type (типоразмер) normally becomes the IFC type object (IfcXxxType via IfcRelDefinesByType), see 01_ifc_basics/03_entities_cheat_sheet.md.
  - Expected before: [chat] IFC type vs occurrence compared to Revit family/type. Partial mapping; the "типоразмер" word is a family type, not an IFC type object; do not oversimplify to "same".
  - Expected after: [chat] IFC type object vs occurrence compared with Revit family / type / instance. Partial mapping: the Revit family type (типоразмер) normally becomes the IFC type (IfcWallType etc., linked by IfcRelDefinesByType) and each Revit instance becomes an occurrence (IfcWall); the family itself has no separate IFC object, and the link exists only if the exporter wrote it. Do not oversimplify to "same".
- **prompt_bank_ru.md KNW-19**. Open IFC tries to build native-looking elements, Link IFC makes DirectShapes (03_software/revit/ifc_import_link_reference.md); "imported elements are non-native" was too flat.
  - Expected before: [chat] Can an IFC element be edited as a Revit family. IFC is exchange; imported elements are non-native; rebuild or use workarounds.
  - Expected after: [chat] IFC is an exchange format. In Revit, Link IFC freezes the geometry as DirectShapes and Open IFC tries to build native-looking elements (editability varies, data may be lost), so a real family usually has to be rebuilt; verify the Open/Link behaviour for the Revit version in use.
- **prompt_bank_ru.md DEV-09**. Same Open/Link correction as KNW-19.
  - Expected before: [chat] IFC made with IfcOpenShell opens in Revit as a wall, not a family: bug? Not a bug: Revit imports IFC as non-native elements; link or open mapping.
  - Expected after: [chat] Not a bug: Revit does not turn IFC into families. Link IFC gives DirectShapes, Open IFC builds native-looking elements through the class mapping (walls, in-place families); neither creates loadable families.
- **prompt_bank_en.md DLG-11 turn 4**. "no standard vertical-datum field" was wrong: IfcProjectedCRS has an optional VerticalDatum (01_ifc_basics/06_geometry_placement_coordinates_units.md).
  - Before: Says IFC has no standard vertical-datum field in the same way; reports what is stored and suggests a note in the project documentation.
  - After: Says IFC4 has an optional VerticalDatum on IfcProjectedCRS and an OrthogonalHeight on IfcMapConversion, but they are rarely filled; reports what is stored (or that nothing is) and suggests stating the datum in the project documentation.

### 4.2 Near-duplicates replaced (counts kept: the row stays, the content changes) (10)

- **prompt_bank_ru.md REG-12**. Near-duplicate of VAL-02 (elements without a КСИ code); replaced by a distinct-values check.
  - Prompt before: `у всех элементов есть код КСИ? выгрузи тех, у кого нет`
  - Prompt after: `какие значения КСИ вообще встречаются в файле? глянь нет ли опечаток и разных написаний одного кода`
  - Metadata: orig S:ru-classbsdd-s007 -> N
  - Expected before: [IFC] Does every element have a КСИ code; export those without. Find IfcClassificationReference with a КСИ system name; export list (CSV) with class and GlobalId.
  - Expected after: [IFC] Distinct КСИ values. Collect IfcClassificationReference Identification/Name (and the custom property if КСИ lives there), list distinct values with counts, group near-duplicates (case, spaces, dashes, Cyrillic/Latin look-alikes); do not check codes against the real classifier unless it has the table; read-only.
- **prompt_bank_ru.md QTY-19**. Near-duplicate of QTY-02 (wall area and volume by type and storey); replaced by a glazing-share quantity.
  - Prompt before: `вытащи в таблицу площадь стен по типам и этажам, Qto из файла, объём тоже`
  - Prompt after: `площадь остекления: окна отдельно, витражи отдельно, и сколько это в процентах от площади наружных стен`
  - Metadata: persona bim_manager -> architect; diff easy -> medium; orig S:ru-autodesk-telegram-s011 -> N
  - Expected before: [IFC] Wall area and volume by type and storey from Qto. Aggregate Qto_WallBaseQuantities, table; warn if Qto missing.
  - Expected after: [IFC] Glazing area and its share of external wall area. Windows: Qto_WindowBaseQuantities Area, or OverallWidth x OverallHeight if no quantity; curtain walls: IfcCurtainWall panels or their quantities; external walls by IsExternal. Says which source was used per group and that the percentage changes with gross vs net wall area; flags windows with no size.
- **prompt_bank_ru.md QTY-05**. Near-duplicate of QTY-04 (room list for an explication); replaced by the Name/LongName confusion real Revit exports cause.
  - Prompt before: `таблицей все помещения: номер, назначение, площадь, этаж. для экспликации`
  - Prompt after: `в экспликации номер и название помещения перепутаны местами или мне кажется? глянь что у IfcSpace в Name, а что в LongName`
  - Metadata: persona architect -> bim_coordinator; intent extract_quantities -> query_model_data; orig S:ru-permit-s007 -> N
  - Expected before: [IFC] Explication table: number, purpose, area, floor. Extract IfcSpace name/LongName/category, area, storey; flag missing fields.
  - Expected after: [IFC] Name vs LongName on IfcSpace. Show a few spaces with both attributes. By default a Revit export puts the room number in Name and the room name in LongName, so the "swap" is usually that default, not an error; report what this file does, change nothing.
- **prompt_bank_ru.md PRS-10**. Near-duplicate of INV-19 (author and program from the header); replaced by an owner question about parking.
  - Prompt before: `кто автор файла и когда выгружали`
  - Prompt after: `машиномест в паркинге сколько по модели? они вообще заданы отдельными помещениями?`
  - Metadata: topic viewers_opening -> spaces_rooms_areas; diff easy -> medium
  - Expected before: [IFC] Who is the author and export date. Read the header (author, organization, timestamp); do not guess; mention if fields are empty.
  - Expected after: [IFC] Parking places. Look for IfcSpace with PredefinedType PARKING (IFC4) or names like "м/м", "машиноместо", "парковка"; count and say how they were identified; if the parking is one big space or nothing is marked, say so; no guess from a typical bay size.
- **prompt_bank_en.md VAL-29**. Near-duplicate of VAL-27 (rooms with name, number, area) plus caricature "kindly"; replaced by a missing/duplicate room number check.
  - Prompt before: `kindly check all rooms have area, name and number. client will reject otherwise. also share the list of those without`
  - Prompt after: `which rooms have no number or the same number as another room?? client will reject otherwise`
  - Expected before: [either] Lists rooms missing any of the three, by level, with counts; short answer in plain English.
  - Expected after: [either] IFC: reads IfcSpace.Name (the Revit room number by default; LongName holds the room name), lists blanks and repeated values with level and GlobalId. Revit: reads Room Number, includes unplaced rooms. Says which attribute was used.
- **prompt_bank_en.md PRS-09**. Near-duplicate of REG-19 (consultant model far from ours); replaced by a missing-furniture question in the same non-native voice.
  - Prompt before: `The consultant model is coming far away from our model, what we do to correct the coordinates please`
  - Prompt after: `architect sent ifc, no furniture inside, only walls and floors. is furniture not exported or i am not seeing it?`
  - Metadata: intent troubleshoot_import -> validate_check; topic coordinates_georef -> class_mapping
  - Expected before: [IFC] Measures the offset and shows the placement values; gives short options.
  - Expected after: [IFC] Counts IfcFurniture (IFC4) / IfcFurnishingElement (IFC2x3) and proxies with furniture-like names; says plainly if there are none, and that the export can leave whole categories out, so the IFC alone cannot show whether they were modelled. Does not comment on the grammar.
- **prompt_bank_en.md TRB-05**. Near-duplicate of TRB-04 (windows without wall holes, RelVoids); replaced by a no-quantities export question.
  - Prompt before: `walls missing their holes?? doors are in the model but wall is solid in viewer, can u check which IfcWalls have IfcRelFillsElement doors but no IfcRelVoidsElement`
  - Prompt after: `no quantities at all in this ifc, no areas no volumes. did i miss a tick in the export?`
  - Metadata: intent troubleshoot_viewing -> troubleshoot_export; topic openings_voids -> quantities_qto; diff hard -> medium; orig S:en-geom-s001 -> N
  - Expected before: [IFC] Walls hosting doors without a voiding relation; says that this explains solid walls only if the geometry has not already been cut.
  - Expected after: [IFC] Counts IfcElementQuantity / Qto_* sets per class. If none, says the file stores no quantities and points to the exporter option "Export base quantities" (off in some setups, on in the IFC4 Reference/Design Transfer setups); offers geometry-derived values only if asked and labels them. Does not claim the cause for this particular file.
- **prompt_bank_multilingual.md ES-12**. Near-duplicate of ES-03 (wall/slab takeoff per level for the budget); replaced by a missing-slabs complaint in Spanish.
  - Prompt before: `necesito mediciones de muros por planta en m2 y m3 para el presupuesto`
  - Prompt after: `faltan los forjados en el ifc del estructurista, solo veo muros y pilares. estan como proxy o no se exportaron?`
  - Gloss after: The slabs (forjados) are missing from the structural engineer's ifc, I only see walls and columns. Are they proxies or were they not exported?
  - Metadata: persona estimator_qs -> structural_engineer; intent extract_quantities -> troubleshoot_export; orig S:es-spain-s007 -> N
  - Expected before: [IFC] Per-storey areas and volumes of walls, with source and missing flags.
  - Expected after: [IFC] Counts IfcSlab and proxies or other classes with slab-like names (forjado, losa) per storey; says plainly if slabs are absent from the file (an export or category issue, not provable from the IFC alone). Reply in Spanish.
- **ru.md P-116**. Near-duplicate of P-057 (storeys with counts); replaced by the IfcWall / IfcWallStandardCase question, which the Russian list lacked.
  - Before: покажи этажи в ифс и сколько элементов на каждом, для курсовой | query_model_data, easy, F, STUD | List storeys and counts; explain what a storey is in IFC. | s:p-student-s009
  - After: препод сказал, что в ифс стены бывают IfcWall и IfcWallStandardCase. покажи у меня какие есть и в чём разница | query_model_data, medium, F, STUD | Count IfcWall vs IfcWallStandardCase, list examples; plain explanation: StandardCase is the typical IFC2x3 Coordination View output (constant-thickness walls), IFC4 exports use IfcWall, and the exact version that deprecated StandardCase is not settled in this KB. | new; s:p-student-s002
- **prompt_bank_en.md CMP-10**. Near-duplicate of CMP-02 and CMP-04 (what walls/columns were added, moved, deleted between versions); replaced by an export-size comparison.
  - Prompt before: `engineer sent v3 of the structural IFC, compare with v2 - what walls/columns got added, moved or deleted?`
  - Prompt after: `same revit model exported twice, one ifc is 80mb the other 140mb. whats different between them?`
  - Metadata: topic guid_change_tracking -> file_size_performance; orig S:en-arch-s003 -> N
  - Expected before: [IFC] Walls and columns only; added, moved, deleted with counts and a few examples each.
  - Expected after: [IFC] Needs both files. Counts entities per class in each and the difference (new classes, more tessellated or Brep geometry, quantity or property sets switched on), and points at the likely export-option differences without asserting which one was changed.

### 4.3 Prompts that sounded LLM-made, tidied to the standard (17)

- **prompt_bank_ru.md PRS-01**. AP1 over-polite wrapper ("Проверьте, пожалуйста"); formal register kept, politeness marker dropped.
  - Prompt before: `Проверьте, пожалуйста, в какой версии IFC предъявлена модель и каким приложением создана. В задании указана IFC4.`
  - Prompt after: `Какая версия IFC в предъявленной модели и в какой программе она создана? В задании указана IFC4.`
- **prompt_bank_ru.md QTY-17**. AP2/AP6 six equal fields in textbook phrasing; colloquial "спеку" and "штук".
  - Prompt before: `спецификацию дверей сделай: марка, ширина, высота, ADSK_Наименование, количество, итог внизу`
  - Prompt after: `спеку по дверям: марка, ширина, высота, ADSK_Наименование, штук, итого внизу`
- **prompt_bank_en.md VAL-10**. AP1 "can you" wrapper and AP2 redundant "in the model".
  - Prompt before: `can you check all elements in the model have a Uniclass 2015 classification, Ss for systems and Pr for products. list the ones missing`
  - Prompt after: `check all elements have a Uniclass 2015 classification, Ss for systems and Pr for products. list the ones missing`
- **prompt_bank_en.md MOD-05**. AP1 "can you" wrapper, over-complete sentence.
  - Prompt before: `I've got a spreadsheet mapping type names to Uniclass Pr codes. can you apply them to the types in the model and save a new ifc`
  - Prompt after: `got a spreadsheet mapping type names to Uniclass Pr codes. apply them to the types and save a new ifc`
- **prompt_bank_en.md QTY-22**. AP1 "Could you ... so I can" wrapper (typed-to-AI "could you" share is 7% in the synthetic set).
  - Prompt before: `Could you give me total gross floor area per level so I can check it against the brief?`
  - Prompt after: `gross floor area per level? want to check it against the brief`
- **prompt_bank_en.md REG-12**. Caricature register ("sir ... kindly"); India-voice rows have thin evidence (style_guide section 13.2), so only short lowercase phrasing is kept.
  - Prompt before: `sir client is asking for LOD 300 IFC. kindly tell which elements in this file are not LOD 300`
  - Prompt after: `client is asking for LOD 300 ifc. can u tell which elements in this file are not LOD 300`
- **prompt_bank_en.md PRS-01**. Caricature "kindly tell me how many number of"; keeps the Indian-English idiom "level wise".
  - Prompt before: `kindly tell me how many number of doors are there in this model level wise`
  - Prompt after: `how many doors are there in this model, level wise?`
- **prompt_bank_en.md PRS-13**. AP1 "Could you ... I would like to" textbook politeness; Expected gains the Name/LongName caveat.
  - Prompt before: `Could you tell me how many rooms have no name? I would like to fix it before submit.`
  - Prompt after: `how many rooms have no name? I want to fix it before submit`
  - Expected before: [IFC] Count and list of unnamed spaces by level.
  - Expected after: [IFC] Count and list of unnamed spaces by level. In a Revit export the room number sits in Name and the room name in LongName, so it checks LongName too and says which it used.
- **ru.md P-004**. AP1: "пожалуйста" in a Russian typed-to-AI prompt (1% in the data); formal "вы" register kept.
  - Before: Проверьте, пожалуйста, ifc на соответствие
  - After: Проверьте ifc на соответствие
- **ru.md P-014**. AP1: greeting plus "подскажите, пожалуйста" (dwg.ru has no greeting; typed-to-AI Russian has no "please").
  - Before: Добрый день! Подскажите, пожалуйста, у всех ли помещений в загруженном IFC есть код классификатора КСИ. Если нет, перечислите какие.
  - After: У всех ли помещений в загруженном IFC есть код классификатора КСИ? Если нет, перечислите какие.
- **ru.md P-068**. AP1/AP2: greeting, "составьте, пожалуйста", four equal fields in bureaucratic phrasing.
  - Before: Добрый день. Составьте, пожалуйста, ведомость объёмов работ по бетону для сметчика: тип конструкции, этаж, объём, единицы. Если данных не хватает, перечислите.
  - After: Нужна ведомость объёмов по бетону для сметчика: тип конструкции, этаж, объём, единицы. Чего не хватает в модели, перечислите отдельно.
- **en.md P08**. Same rewrite as bank VAL-10.
  - Before: can you check all elements in the model have a Uniclass 2015 classification, Ss for systems and Pr for products. list the ones missing
  - After: check all elements have a Uniclass 2015 classification, Ss for systems and Pr for products. list the ones missing
- **en.md P11**. Same rewrite as bank MOD-05.
  - Before: I've got a spreadsheet mapping type names to Uniclass Pr codes. can you apply them to the types in the model and save a new ifc
  - After: got a spreadsheet mapping type names to Uniclass Pr codes. apply them to the types and save a new ifc
- **en.md P32**. "Kindly tell me" dropped; this row stays as the one polite non-native example (style_guide section 6, beginners and non-native writers).
  - Before: Hello, I received IFC file from structural consultant. Kindly tell me how many columns and beams are there level wise, and which concrete grade is used. Thank you.
  - After: Hello, I received IFC file from structural consultant. How many columns and beams are there level wise, and which concrete grade is used? Thank you
- **en.md P32**. Expected no longer rewards a polite answer.
  - Before: answer in plain, polite language.
  - After: answer in plain language; mirroring the formality is not required.
- **en.md P33**. Caricature "sir please" removed.
  - Before: sir please check this ifc, my client say rooms not showing
  - After: pls check this ifc, my client say rooms not showing
- **en.md P58**. AP17-like opener "Quick one." and two tidy sentences; collapsed into one lowercase line.
  - Before: Quick one. Which levels in this model have no rooms at all, and is any IfcSpace sitting above or below its own level? we had the offset problem again
  - After: which levels in this model have no rooms at all? and is any IfcSpace sitting above or below its own level, we had the offset problem again

---

## 5. Checked and left unchanged (so nobody re-checks them)

| Claim in Expected | Where | Why it stands | Source |
|---|---|---|---|
| GlobalId is 22 characters, first character 0 to 3 | EN VAL-07 | `IfcGloballyUniqueId` = STRING(22) FIXED; 128 bits in a base64-like form leave 2 bits in the first character | [02_ifc_file_anatomy.md](../../01_ifc_basics/02_ifc_file_anatomy.md) |
| `IfcCourse` / `IfcAlignment` / `IfcRoad` need IFC4.3 | EN QTY-17, INV-16, EDG-11; RU CRD-12, PRS-23 | The KB states IfcAlignment is valid only in IFC4X3_ADD2; IfcCourse is in the 4.3 enum table | [buildingsmart_standards.md](../../02_standards_regulations/buildingsmart_standards.md), [03_entities_cheat_sheet.md](../../01_ifc_basics/03_entities_cheat_sheet.md) |
| 12 inches = 304.8 mm; 1 m2 = about 10.764 sqft; station 5+00 = 500 ft | EN EDG-20, EDG-21, KNW-09 | arithmetic | |
| `Qto_WallBaseQuantities` has GrossSideArea / NetSideArea / NetVolume; `Qto_WindowBaseQuantities` has Area | EN QTY-01, QTY-04; RU QTY-13 | listed property and quantity sets | [05_properties_quantities_psets.md](../../01_ifc_basics/05_properties_quantities_psets.md) |
| Revit "Export base quantities" is off by default and on for the RV/DTV setups | new EN TRB-05 | export reference table | [ifc_export_reference.md](../../03_software/revit/ifc_export_reference.md) |
| IfcSpace PredefinedType includes PARKING (IFC4); IfcFurniture is new in IFC4, IFC2x3 has `IfcFurnishingElement` | new RU PRS-10, new EN PRS-09 | entity cheat sheet | [03_entities_cheat_sheet.md](../../01_ifc_basics/03_entities_cheat_sheet.md) |
| `PlacementRelTo` is optional | EN TRB-23 (corrected in this pass) | | [06_geometry_placement_coordinates_units.md](../../01_ifc_basics/06_geometry_placement_coordinates_units.md) |
| Revit exports the room number to `IfcSpace.Name` and the room name to `LongName` | new RU QTY-05; Name/LongName notes | | [04_spatial_structure_and_relationships.md](../../01_ifc_basics/04_spatial_structure_and_relationships.md) |
| Open IFC builds native-looking elements; Link IFC creates DirectShape geometry | EN KNW-03, KNW-19; RU DEV-09, KNW-19 | | [ifc_import_link_reference.md](../../03_software/revit/ifc_import_link_reference.md) |
| IDS 1.0 does not cover geometry | RU KNW-02, `ru.md` P-003 | the wording "geometry and conditional logic" is quoted from a real Russian article (`habr-r015`), not invented | `ru.md` section 5 |
| `\X\E6` is a valid escape for the Latin-1 letter ae; `\X2\...\X0\` is the Unicode form | ML DA-01, OT-03, TR-02 | standard STEP string encoding | [02_ifc_file_anatomy.md](../../01_ifc_basics/02_ifc_file_anatomy.md) |
| IFC+SG / CORENET X error codes (IFC0000101, IFC0000104) | EN VAL-19, `en.md` P01, P07 | listed in the Singapore national doc | [singapore.md](../../02_standards_regulations/national/singapore.md) |
| Archicad to DWG solids via IFC2x3 and `_AecConvertTo3DSolids` | RU CNV-07 | taken from the real 2011 dwg.ru answer (`ru-dwg-other-r021`); old, flagged by the row | research_raw ru |
| Civil 3D reaches IFC 4.3 through an extension | RU CRD-12, ML NO-10 | the 2025 help index lists an "IFC 4.3 Extension"; the KB marks the detail unverified and the Expected lines do not depend on it | [authoring_tools_ifc.md](../../03_software/authoring_tools_ifc.md) |
| Moscow AGR checked by IDS from April 2026 | RU REG-14 | the row says "real article claims that date; verify with the source"; the KB cites a consultancy summary of an order dated 2 April 2026 (secondary source) | [russia.md](../../02_standards_regulations/national/russia.md) |

**Still unverified in the KB, hedged in the rows and not asserted:** that Navisworks drops IFC4 geometry (RU TRB-19, `ru.md` P-099); that the phase of a linked IFC explains an empty Revit view (RU TRB-01, DLG-02, EN DLG-02); that plain AutoCAD has no IFC import (hedged in `ru.md` P-085 and P-088); the Renga property-mapping location (RU TRB-17); the meaning of EPSG 7791 (ML IT-08, the row says "no assumption"); the IFC+SG class for site coverage (EN REG-06, the row says "must not assert the rule").

---

## 6. Kept on purpose

| Item | Why it stays |
|---|---|
| EN PRS-08 ("Hello, i need list of rooms ... my english is not very good sorry"), `en.md` P32 ("Hello ... Thank you"), EN PRS-02 / PRS-03 / PRS-07 / PRS-11 / PRS-12 / PRS-14 | The only polite or non-native samples. Style guide section 6: beginners and non-native writers on GitHub are over-polite. They carry a voice label and sit in the non-native section; the wording that read as caricature (kindly, sir, "how many number of") was removed. |
| RU PRS-01 (formal "Какая версия IFC в предъявленной модели ...") and the FORMAL rows of `ru.md` (P-004, P-009, P-014, P-039, P-068 and others) | The reviewer-from-authority persona is formal in the style guide (section 12.1); only greeting and "пожалуйста" went. |
| EN coordinates cluster (INV-05, TRB-03, CRD-01, CRD-04, CRD-07, CRD-08, REG-19) | Georeferencing is one of the most frequent real themes; the rows differ in file pair, unit, viewer and whether the user wants a read or a shift. |
| Parallel sets across languages (ML section 14) and the cross-file copies between `ru.md` / `en.md` and the banks | By design: same intent, same numbers, different language or file. |
| RU EDG-02 / EDG-16 ("проверь модель" / "проверь вообще всё в модели") | Deliberately vague pair; EDG-16 adds the scope trap (do not dump thousands of lines). |
| EN CMP-02 vs CMP-04 | One has a deadline and covers moved elements; the other is walls only by GlobalId. Only CMP-10 (a third wall/column diff) was replaced. |
| Round clash tolerances (10 mm, 20 mm) | Realistic for clash tool settings (AP16 targets measured quantities, not settings). Not varied, to avoid drifting from the matching `en.md` / `ru.md` copies. |
| RU `ADSK_*`, `RUS_*`, EN `Pset_Custom`, `L{level}_{name}` patterns | Anchor tokens a tester can verify; the style guide asks for one exact anchor per prompt. |

---

## 7. Counts after the pass

Row counts did not change: RU 272, EN 283, multilingual 170, `ru.md` 130, `en.md` 77. Dialogs are untouched except one Expected line (EN DLG-11 turn 4).

| Table (top of the bank) | Changed values |
|---|---|
| RU difficulty | easy 48 -> 46, medium 128 -> 130, hard 96 |
| RU origin | S 86 -> 83, N 134 -> 137 |
| RU persona | architect 50, bim_coordinator 79 -> 80, bim_manager 41 -> 40 |
| RU intent | query_model_data 47 -> 48, extract_quantities 31 -> 30 |
| EN difficulty | medium 125 -> 126, hard 87 -> 86 |
| EN origin | S 187 -> 185, N 70 -> 72 |
| EN intent | validate_check 51 -> 52, troubleshoot_import 12 -> 11, troubleshoot_export 9 -> 10, troubleshoot_viewing 9 -> 8 (table re-sorted) |
| Multilingual origin | S 155 -> 154, N 6 -> 7 (and the sentence in section 15 of that bank) |
| `ru.md` coverage line | easy 27 -> 26, medium 72 -> 73 |

Smoke sets in section 17 of both banks still point at the same IDs. The content behind RU QTY-19 (IFC read-only set) and EN PRS-09 (regional-voice and non-native sets) changed, but both remain read-only checks in the same voice.

---

## 8. Open items and follow-ups

**Outside the assigned files (not edited here; someone with those files should sync):**

| File | What is stale now |
|---|---|
| `exports/kb_compact.md` (near lines 1327 to 1328 and the curated rows for the changed IDs) | still quotes EDG-14 as "IFC2x4 does not exist" and the old texts of the replaced prompts |
| `exports/synthetic_prompts.jsonl` | holds the original synthetic versions of VAL-10, MOD-05, QTY-22, VAL-13, QTY-05, REG-12, TRB-05, ES-12, P08, P11 (fine as raw synthetic records; they now differ from the banks) |
| `05_real_world_questions/by_persona/bim_coordinator.md`, `by_topic/validation_ids_model_checking.md` | VAL-13 with `PILECAP` (not a value of the IfcBeam predefined type) |
| `05_real_world_questions/by_persona/owner_client.md`, `by_persona/architect.md`, `by_topic/classification_cobie_fm.md`, `by_language/es.md` | the old QTY-22, QTY-05, REG-12 and ES-12 texts |
| `research_raw/wave1/**` | untouched on purpose (raw data) |

**For the next wave (not fixed, because they need more evidence or a native reader):**
1. Motive clauses: by a keyword heuristic only about 16 to 18 percent of RU and EN prompts carry a deadline, a waiting person or a "for X" purpose, against the style-guide knob of about one in three. Adding motives to roughly 30 prompts per bank would close the gap without changing the tasks.
2. Native review for KO, FR, PT, AR, EL and the casual register of the Chinese rows.
3. Real typed-to-AI prompts remain almost absent from the data (19 records, mostly README lines). Collecting a few dozen from MCP issue threads would allow a re-calibration.
4. Facts that need a primary source: Navisworks IFC4 handling, the phase explanation for an empty linked IFC, plain AutoCAD IFC import by version, Renga property mapping.

**Reproduce the batch numbers:** the profile in section 3 comes from a small script that reads the `| ID | Prompt | ... |` rows of each bank (ID pattern `AAA-nn`) and counts words, politeness markers and slang tokens; the summary-table recomputation reproduced the old tables exactly before it was used on the new data.
