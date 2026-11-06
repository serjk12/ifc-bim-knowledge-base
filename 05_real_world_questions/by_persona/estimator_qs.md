# Estimator / quantity surveyor: who they are and what they do with IFC

> Persona tag in the data: `estimator_qs`. Evidence base: `kb.py stats --persona estimator_qs` gives 121 records (55 real, 66 synthetic) from `research_raw/wave1`. Last compiled 2026-11-06.
> Sibling pages: [contractor / site](contractor_site.md), [structural engineer](structural_engineer.md), [student / beginner](student_beginner.md), [developer](developer_programmer.md). Topic overview: [quantities, cost, schedule](../by_topic/quantities_cost_schedule.md); related: [properties and parameters](../by_topic/properties_and_parameters.md).

## In plain words

An estimator, cost planner or quantity surveyor (QS) puts a price on a building. The raw material is **quantities**: how many cubic metres of concrete, how many square metres of wall, how many doors of which type, how many metres of pipe. Traditionally these are measured from drawings ("taking off"). With a model, the hope is that the quantities can be read from the file, quickly and repeatably.

So the estimator's relationship with IFC is narrow and sharp: **"give me numbers I can price from, and tell me whether I can trust them."** They want tables per level, per type, per material, in a spreadsheet; sometimes grouped by a national classification or a bill-of-quantities structure (NRM2, Uniclass, NL-SfB, GB/T 51269, Masterformat-style, BC3, GAEB, DPGF, computo metrico). The big enemy is silent error: a "net" area that is really "gross" because openings were not subtracted, a volume in the wrong unit, a missing quantity set that looks like zero.

In the data this persona produces the most **reproducible numeric complaints**: the same wall measured by two tools gives 9.8 m2 and 20.1 m2 (`en-qto-r002` is the best-known example), a cost total is "one too many" because a resource counted 1 before any element was added (`en-gh-ifcos-r014`), a rate rounds badly (`en-gh-ifcos-r022`). Those make excellent test cases because the correct answer is checkable.

Evidence caveat: real records skew to English and to the open-source Bonsai / IfcOpenShell community (cost and QTO modules); users of commercial estimating and Revit / Navisworks workflows are underrepresented in the data. Russian estimators appear only in synthetic prompts. German, French, Italian, Portuguese, Korean estimation phrasing is also synthetic.

## Daily IFC tasks

| Task | What it looks like in practice | Typical tools | Example ids |
|---|---|---|---|
| Quantities per level / per type | Wall area, slab area, concrete volume, door counts; into Excel. | Spreadsheet, QTO tools, scripts | `en-qto-s004`, `ru-s007`, `de-s008`, `ja-s013` |
| Net vs gross check | "Do the openings get subtracted?" | Solibri, Bonsai, scripts | `en-gh-ifcos-r002`, `en-qto-s006`, `en-s002`, `en-qto-s003` |
| Fix missing quantities | Compute from geometry when the export has no Qto; compare both. | Scripts | `en-s018`, `zh-csdn-dev-s007`, `ru-habr-dev-s010`, `en-proxy-s012` |
| Weight of steel and rebar | Mass from profile or density times volume; rebar kg per column. | Spreadsheet | `en-gh-ifcos-r006`, `en-qto-r029`, `en-struct-s003`, `en-struct-r006` |
| Build a bill of quantities / cost schedule linked to the model | Cost items per wall type, linked to NetVolume; CSV round trip. | Bonsai cost module, spreadsheets | `en-qto-s005`, `en-osarch-r012`, `en-qto-r009`, `en-gh-ifcos-r015` |
| Tag elements with a classification code | Put NRM2 / Uniclass / NL-SfB / GB/T code on elements and group by it. | Scripts | `en-s006`, `zh-classbsdd-s009`, `nl-dutch-s009`, `en-osarch-r026` |
| Re-price after a design change | "What changed in slab areas and column counts since the bid set?" | Compare tools | `en-s004`, `en-osarch-r011` |
| Room areas for schedules | Area per room per level, with totals. | Scripts | `ru-revit-auto-s009`, `ru-spaces-s011`, `ja-qto-s015`, `en-spaces-s006` |

## Goals

- **Trustworthy numbers with a stated source**: "NetVolume from Qto_WallBaseQuantities, and list walls that don't have it" (`en-s001`); "say which qto source you used" (`en-aimcp-s004`).
- **No silent zeros or silent gross/net swaps.** Know which elements have no quantities (`ru-aimcp-s011`, `zh-s011`, `it-s015`).
- **A repeatable BoQ linked to the model** that survives file reloads and revisions (`en-osarch-r012`, `en-data-r031`, `en-qto-r009`).
- **Spreadsheet-ready output** with one row per element (GlobalId, tag, level) so the sheet can be traced back to the model (`en-data-r005`, `en-viewconv-s003`).
- **Weight and carbon-relevant data** (steel by profile, rebar per m3, layer volumes) for costing and life-cycle work (`en-qto-r029`, `en-qto-r026`).
- **National format output**: ВОР / смета, mediciones / BC3, GAEB LV, DPGF, computo metrico, 積算 (`ru-aimcp-s011`, `es-qto-s012`, `de-qto-s013`, `fr-s012`, `it-s015`, `ja-japan-s004`).

## Pains (ranked)

Editorial ranking by independent real threads.

| Rank | Pain | What the user says (paraphrase) | Evidence ids |
|---|---|---|---|
| 1 | **Quantities disagree between tools** (gross vs net, openings baked into the mesh, orientation-dependent areas). | "Bonsai reports Gross 9.81 = Net 9.81 while Solibri gives Gross 20.08" / "side area depends on wall orientation" | `en-qto-r002`, `en-gh-ifcos-r002`, `en-gh-ifcos-r003`, `en-gh-ifcos-r001`, `en-gh-ifcopenshell-r034`, `en-geom-r028` |
| 2 | **Quantity sets missing or incomplete in the export.** | "BaseQuantities missing on walls with voids" / "exported schedule property sets lack area and perimeter" / "no weight in base quantities" | `en-autodesk-revit-export-r028`, `en-autodesk-revit-export-r029`, `en-qto-r029`, `en-struct-r026`, `en-ghrevitifc-r031`, `de-dach-r013` |
| 3 | **Cost schedule arithmetic surprises.** Totals one too many; fixed vs rate; rounding; resource sums wrong; parent items do not sum cost. | "resource counts 1 before any elements are added" / "constituent resources sum to 2.62 but panel shows 3.58" | `en-gh-ifcos-r014`, `en-qto-r005`, `en-qto-r008`, `en-qto-r011`, `en-gh-ifcos-r015`, `en-gh-ifcos-r022`, `en-qto-r034` |
| 4 | **Linking elements to cost items is manual.** | "assigning elements needs select, unit, click; want a query such as walls with concrete" | `en-gh-ifcos-r017`, `en-gh-ifcos-r013`, `en-osarch-r012` |
| 5 | **CSV/Excel round trip breaks or has junk columns.** | "CSV export has junk columns, no unit column, no decimal setting; I just copy into Excel" / "errors importing a cost schedule CSV" | `en-data-r007`, `en-qto-r033`, `en-osarch-r012`, `en-qto-r009`, `en-data-r005` |
| 6 | **Quantities for odd classes are empty** (proxies, footings, terrain, earthworks). | "Calculate All Quantities doesn't fill the quantity set for proxy elements" / "footings: 1 of 10 quantities right" | `en-gh-proxy-r034`, `en-qto-r013`, `en-gh-ifcos-r004`, `en-civil-infra-r031` |
| 7 | **Layered elements: only thickness exported, not layer area / volume.** | "only layer thickness is exported by Revit; area and volume per layer needed" | `en-qto-r026`, `en-mcl-r009`, `en-qto-r035` |
| 8 | **Classification mapping.** | "Uniclass reference on entities and cost items: how does it appear in the cost CSV?" | `en-osarch-r026`, `en-bsforum-r002` |
| 9 | **Rules for what is not modelled.** | "measuring from drawings takes time and precision is hard; what is the rule for parts not in the model?" | `ja-japan-r024`, `nl-dutch-r011` |
| 10 | **Contract/commercial context.** | "does the 10% BIM surcharge apply to other roles too?" | `it-italy-r019` |

## Vocabulary they use (and what they do not know)

| They say | Meaning for them | What they usually do not know / confuse |
|---|---|---|
| QTO, takeoff, BoQ, BQ, ВОР, смета, ведомость объёмов, mediciones, metrados, 积算, 算量, 数量, métré, DPGF, LV, computo | The quantity list and priced list | That a "quantity" in IFC is a stored number in a quantity set (Qto) that the exporter may or may not have written. |
| gross / net, brutto / netto, 净 / 毛, нетто | With or without openings or deductions | That IFC has both (NetSideArea, GrossSideArea) and that they can be identical if openings are not real voids (`en-s002`). |
| NetVolume, NetArea, "Qto_WallBaseQuantities" (the better-informed ones) | The quantity name | How to find them for other classes; that names differ between wall and column (`en-gh-ifcos-r013`). |
| cost item, rate, resource, unit rate, crew | Cost schedule vocabulary | That in IFC a cost item has values and a unit basis, and that a resource may be a separate object (`en-qto-r011`). |
| LCA, EPD, embodied carbon, weight | Sustainability data | That mass is not in base quantities and must be computed (`en-qto-r029`, `en-bsforum-r019`). |
| classification: NRM2, Uniclass, NL-SfB, GB/T 51269, Masterformat, Uniformat | Grouping codes | That a code is stored as a classification reference on elements, not as part of the name (`en-osarch-r026`, `en-s006`). |
| "по этажам", "per level", "por planta", "pro Geschoss", "par niveau" | Grouping axis | That elements not attached to a level drop out of such a table (`ru-revit-auto-s009`). |

Plain-language bridge: the estimator reads the file like a spreadsheet. If the spreadsheet has a hole (no quantity for a wall), they want it reported as a hole, not as zero. Background: [properties, quantities, psets](../../01_ifc_basics/05_properties_quantities_psets.md), [domains overview (4D/5D)](../../01_ifc_basics/08_domains_mep_structural_infra_4d5d_fm.md), [classification](../../01_ifc_basics/07_materials_classification_types_styles.md), [Revit export reference](../../03_software/revit/ifc_export_reference.md), [glossary](../../08_glossary/glossary_multilingual.md).

## Real questions

50 real questions, grouped loosely by theme (quantity disagreement, missing quantities, cost arithmetic, linking to cost items, CSV/Excel, special classes, layers, classification, national and commercial context). Language mix: en 45, nl 2, ja 1, it 1, es 1. The "Question" column is the research pass's **paraphrase** of the source (not a verbatim quote); English gloss appears only for non-English rows. A large share are GitHub issues from the Bonsai / IfcOpenShell cost and QTO modules.

| # | ID | Lang | Question (paraphrase, original language) | English gloss | Outcome in source | Source |
|---|---|---|---|---|---|---|
| 1 | `en-qto-r002` | en | after Perform Quantity Takeoff Bonsai reports Gross 9.81 = Net 9.81 whereas Solibri gives Gross 20.08; affects almost all walls | — | Gross short-circuits to Net when no IfcRelVoidsElement; maintainers ask for a semantics decision. | [GitHub #9235](https://github.com/IfcOpenShell/IfcOpenShell/issues/9235) |
| 2 | `en-gh-ifcos-r002` | en | walls from Revit export: Bonsai gross side area is the same as net, Solibri gives different gross; no IfcRelVoidsElement in the model | — | Maintainer-side analysis: has_openings only checks IfcRelVoidsElement, so openings baked into the tessellation are not detected; needs a semantic decision. | [GitHub #9235](https://github.com/IfcOpenShell/IfcOpenShell/issues/9235) |
| 3 | `en-gh-ifcos-r003` | en | side area quantities depend on wall orientation in the model, giving wrong values for Y-oriented walls | — | Not read. | [GitHub #9237](https://github.com/IfcOpenShell/IfcOpenShell/issues/9237) |
| 4 | `en-gh-ifcos-r001` | en | IfcOpenShell QTO gives wrong area for an IfcWindow defined by an IfcWindowType with mesh geometry, Blender shows right value; attached test file | — | No answer in thread at time of reading. | [GitHub #5349](https://github.com/IfcOpenShell/IfcOpenShell/issues/5349) |
| 5 | `en-gh-ifcopenshell-r034` | en | compares QTO with Solibri table | — | Bug reported | [GitHub #9235](https://github.com/IfcOpenShell/IfcOpenShell/issues/9235) |
| 6 | `en-geom-r028` | en | all three appear as IfcOpening.OPENING in Solibri | — | By design: map to IfcOpeningElement USERDEFINED and store label in ObjectType. | [GitHub #755](https://github.com/Autodesk/revit-ifc/issues/755) |
| 7 | `en-openings-r006` | en | Compares Bonsai and Solibri numbers per wall to show gross side area ignores openings. | — | Discussion: has_openings only checks IfcRelVoids; semantic decision needed. | [GitHub #9235](https://github.com/IfcOpenShell/IfcOpenShell/issues/9235) |
| 8 | `en-geom-r025` | en | void-cut family loses some quantities too | — | Tracked REVIT-235661, open. | [GitHub #644](https://github.com/Autodesk/revit-ifc/issues/644) |
| 9 | `en-autodesk-revit-export-r028` | en | BaseQuantities property set missing on some walls and roofs, mostly with voids. | — | Version-dependent bug; labels NetSideArea vs gross mismatch in 2020 (GitHub #198). | [forums.autodesk.com](https://forums.autodesk.com/t5/revit-structure-forum/ifc-basequantities-missing-on-some-elements/td-p/9943386) |
| 10 | `en-autodesk-revit-export-r029` | en | Exported schedule property sets lack area and perimeter. | — | Check schedule export settings. | [forums.autodesk.com](https://forums.autodesk.com/t5/revit-architecture-forum/revit-schedule-as-property-sets-missing-area-and-perimeter-in/td-p/8835632) |
| 11 | `de-dach-r013` | en | Qto_CoveringBaseQuantities lacks Width for basic walls mapped to IfcCovering/USERDEFINED. | — | Open bug. | [GitHub #872](https://github.com/Autodesk/revit-ifc/issues/872) |
| 12 | `en-ghrevitifc-r031` | en | Support for custom base quantities export in IFC2x3 | — | Snippet only. | [GitHub #594](https://github.com/Autodesk/revit-ifc/issues/594) |
| 13 | `en-struct-r026` | en | beam NetWeight not exported as IfcQuantityWeight | — | UDPS text workaround; fix only in Revit 2026+, not backported. | [GitHub #764](https://github.com/Autodesk/revit-ifc/issues/764) |
| 14 | `en-qto-r029` | en | base quantities in IFC do not include weight though weight is critical for costing and LCA; Volume x Density works in Revit | — | Community agrees; multi-layer elements make it hard; viewers may not display what Revit writes. | [GitHub #545](https://github.com/Autodesk/revit-ifc/issues/545) |
| 15 | `en-gh-ifcos-r006` | en | calculate Gross/NetWeight from Pset_ProfileMechanical.MassPerLength times length, so hollow steel sections need not be modelled in detail for takeoff | — | Implemented for simple profile cases; fails with booleans or openings when net weight is computed. | [GitHub #6344](https://github.com/IfcOpenShell/IfcOpenShell/issues/6344) |
| 16 | `en-struct-r006` | en | wants rebar weight per concrete volume as custom Qto for cost schedule; rebar not modeled | — | Options: density on a 'rebar' material, Qto_ReinforcingElementBaseQuantities, Pset_ConcreteElementGeneral.ReinforcementVolumeRatio, script writing custom pset. | [community.osarch.org #2578](https://community.osarch.org/discussion/2578/how-to-create-a-custom-qto-calculation) |
| 17 | `en-gh-ifcos-r014` | en | resource assigned to cost item already counts 1 before any elements are added; after adding model elements the total is one too many | — | Maintainer asked what the expected behaviour is. | [GitHub #5155](https://github.com/IfcOpenShell/IfcOpenShell/issues/5155) |
| 18 | `en-qto-r005` | en | attached a simple 1-bed model and a screenshot showing cost total that does not match displayed volume times rate; also wants a 'fixed' cost value not driven by QTO (e.g. an unplanned extra bag of cement) | — | Rounding in display only; real volume 3.956403 x 1945.71 = 7698.01. Requester says rounded values should be used in practice. | [GitHub #6401](https://github.com/IfcOpenShell/IfcOpenShell/issues/6401) |
| 19 | `en-qto-r008` | en | constituent resources of a crew resource sum to 2.62 after assigning to a cost article but the resource panel shows 3.58 | — | Suspected unit conversion (day vs hours assumed 8h); maintainer asks for the project file. | [GitHub #5706](https://github.com/IfcOpenShell/IfcOpenShell/issues/5706) |
| 20 | `en-qto-r011` | en | a single IfcCostItem with multiple IfcCostValue records of different UnitBasis shows wrong Total Cost that persists after reopen | — | Confirmed; fix sums each cost value after applying its own unit basis; total becomes 55.00. | [GitHub #8625](https://github.com/IfcOpenShell/IfcOpenShell/issues/8625) |
| 21 | `en-gh-ifcos-r015` | en | parents of subitems show summed quantities but not summed total cost; subitem rates differ so parent has no rate of its own | — | Linked to related IfcSpace area fix PR. | [GitHub #7354](https://github.com/IfcOpenShell/IfcOpenShell/issues/7354) |
| 22 | `en-gh-ifcos-r022` | en | rounding in cost calculation too coarse | — | Not read. | [GitHub #6964](https://github.com/IfcOpenShell/IfcOpenShell/issues/6964) |
| 23 | `en-qto-r034` | en | cost calculation affected by resource usage decimals | — | not read | [GitHub #5693](https://github.com/IfcOpenShell/IfcOpenShell/issues/5693) |
| 24 | `en-gh-ifcos-r017` | en | assigning elements to cost item needs select, unit, click; wants query such as walls with concrete, saved in the quantity Formula | — | Implemented later with a query field in the Cost Items Quantities panel. | [GitHub #5390](https://github.com/IfcOpenShell/IfcOpenShell/issues/5390) |
| 25 | `en-gh-ifcos-r013` | en | formwork article for walls and columns, quantity property names differ between the two, so loop with regex match per element | — | Cross-referenced to forum thread; implementation discussed. | [GitHub #6616](https://github.com/IfcOpenShell/IfcOpenShell/issues/6616) |
| 26 | `en-osarch-r012` | en | how to keep a CSV BoQ linked to the IFC cost schedule, and let one cost item match differently named quantities across element types | — | Selectors work in Query and Spreadsheet but not Property; link persistence added via document reference; regex request filed on GitHub. | [community.osarch.org #2887](https://community.osarch.org/discussion/2887/dynamic-csv-to-cost-schedule-now-available) |
| 27 | `en-data-r005` | en | Tender and cost work runs on spreadsheets; I need rows traceable to IFC elements, e.g. ventilators FAN-01..03 per room, and summarise equal elements by floor. | — | Use Spreadsheet Import/Export and group/sum by an aggregator property; link to cost items via code or GUID. | [GitHub #7762](https://github.com/IfcOpenShell/IfcOpenShell/issues/7762) |
| 28 | `en-data-r007` | en | Browser view has no PDF/print export; CSV export has junk columns, no unit column, no decimal setting; I just ctrl+C into Excel. | — | Confirmed by another user: cost and totals show in UI but not in CSV; print-to-PDF suggested from browser. | [GitHub #5736](https://github.com/IfcOpenShell/IfcOpenShell/issues/5736) |
| 29 | `en-qto-r033` | en | errors when importing a cost schedule CSV into Bonsai | — | not read | [GitHub #6920](https://github.com/IfcOpenShell/IfcOpenShell/issues/6920) |
| 30 | `en-data-r031` | en | Cost rows are not one-to-one with model quantities (installation rows skipped, others split); wants not to build in-house. | — | A QS recommends defining a cross-reference ID, then Power Query or pandas. | [community.osarch.org](https://community.osarch.org/discussion/comment/27265) |
| 31 | `en-gh-proxy-r034` | en | Calculate All Quantities doesn't fill Qto_BuildingElementProxyQuantities for proxy elements. | — | Reported as bug; no discussion. | [GitHub #4740](https://github.com/IfcOpenShell/IfcOpenShell/issues/4740) |
| 32 | `en-qto-r013` | en | table review: strip/beam footings under IfcOpenShell engine only get 1 of 10 quantities right, rest missing or swapped | — | Engine-side geometry handling being fixed; some gross values only computed by Blender engine. | [GitHub #6305](https://github.com/IfcOpenShell/IfcOpenShell/issues/6305) |
| 33 | `en-gh-ifcos-r004` | en | IfcFooting quantities calculated wrongly in QTO | — | Not read; issue closed. | [GitHub #6305](https://github.com/IfcOpenShell/IfcOpenShell/issues/6305) |
| 34 | `en-civil-infra-r031` | en | IfcGeographyElement has no base quantities to quantify | — | Not read in detail. | [GitHub #6508](https://github.com/IfcOpenShell/IfcOpenShell/issues/6508) |
| 35 | `en-gh-proxy-r020` | en | Wall overridden to IfcFurniture still exports with Qto_WallBaseQuantities. | — | Maintainer: will root out places where quantities ignore the actual exported class. | [GitHub #497](https://github.com/Autodesk/revit-ifc/issues/497) |
| 36 | `en-qto-r026` | en | only layer thickness is exported by Revit; area and volume per layer needed for LCA through IFC; mentions Roombook extension | — | Logged as REVIT-239820, open. | [GitHub #753](https://github.com/Autodesk/revit-ifc/issues/753) |
| 37 | `en-mcl-r009` | en | wants each layer of floor and roof as IfcBuildingElementPart | — | Search snippet only; related to parts/layers export. | [GitHub #828](https://github.com/Autodesk/revit-ifc/issues/828) |
| 38 | `en-qto-r035` | en | material quantities are absent for some categories when converting Revit to Speckle | — | not read | [GitHub #2117](https://github.com/specklesystems/speckle-sharp/issues/2117) |
| 39 | `en-osarch-r026` | en | assigning a Uniclass 2015 reference to entities and cost items, how does classification appear in the cost CSV | — | Not read in detail. | [community.osarch.org #2014](https://community.osarch.org/discussion/2014/bbim-classification-in-cost-schedue-exported-csv) |
| 40 | `en-bsforum-r002` | en | India-based estimating software vendor (Masterformat, RS Means-style) is asked by buyers to link to design software; non-programmer wants to know how to read IFC data incl. Revit keynotes/parameters | — | Use IfcOpenShell (Python), IFC++ or xBIM to read elements, relationships and properties instead of parsing by hand. | [forums.buildingsmart.org](https://forums.buildingsmart.org/t/3953) |
| 41 | `en-qto-r004` | en | trying to get a budget for a small toilet building but some quantities in the IFC are not correct; asks what they are doing wrong | — | QTO is not live-updated: run the calculation explicitly (Shift-Q); aggregates were also missing. | [GitHub #4964](https://github.com/IfcOpenShell/IfcOpenShell/issues/4964) |
| 42 | `en-qto-r022` | en | lightweight alternative to full estimating suites; asks what prevents real-project use and what CSV export should contain | — | Shows 2D PDF takeoff remains a parallel workflow to IFC QTO. | [community.osarch.org #3576](https://community.osarch.org/discussion/3576/plan-measure-open-source-pdf-takeoff-tool-looking-for-aec-feedback) |
| 43 | `en-gh-ifcopenshell-r020` | en | prototype extracting wall lengths, thicknesses, opening W x H with coordinate proof overlay | — | No accepted answer read | [GitHub #7630](https://github.com/IfcOpenShell/IfcOpenShell/discussions/7630) |
| 44 | `en-gh-ifcopenshell-r021` | en | count beams correctly but cannot get dimensions | — | Depends on authoring tool; check psets via get_psets | [GitHub #7540](https://github.com/IfcOpenShell/IfcOpenShell/discussions/7540) |
| 45 | `ja-japan-r024` | ja | 図面から数量を拾うのが時間と精度の両立が難しい。モデル化されない部材の数量ルールは？ | BIM-based quantity takeoff: reading IFC from ArchiCAD for estimating; unmodeled members need rules | MLIT encourages IFC for takeoff; Maeda reads ArchiCAD IFC for exterior walls, columns, beams into estimating software. | [note.com](https://note.com/bold_cobra9180/n/n4f52d62f230f) |
| 46 | `nl-dutch-r011` | nl | Opdrachtgever en calculator gebruiken tabellen om te controleren wat geleverd is: 'hebben alle 212 deuren een FireRating?' of 'm2 binnenwand per NL-SfB-code' | Quantity tables from the model to Excel: e.g. do all 212 doors have FireRating, m2 interior wall per NL-SfB code | Proposal: takeoff definition grouped by class/type/storey/classification with warning on missing quantities. | [GitHub #19](https://github.com/OpenAEC-Foundation/OpenAEC-BIM-validator/issues/19) |
| 47 | `nl-dutch-r015` | nl | Analyse Revit-workflow, beschrijving gewenste informatiestructuur, realiseren gewenste output in IFC voor eerste testbatch, testen in IBIS | Experiment: quantity take-off with NLCS classification; analyse Revit workflow, deliver desired IFC output for test batch and test it in IBIS | Open; no results yet. | [GitHub #687](https://github.com/nl-digigo/NLCS/issues/687) |
| 48 | `it-italy-r019` | it | la maggiorazione del 10% per il BIM vale anche per DL e CSE? | Does the 10% BIM fee increase apply to site management and CSE? | Per ANAC opinion extended to DL and safety coordination. | [biblus.acca.it](https://biblus.acca.it/notizie/bim-maggiorazione-del-10-anche-per-direzione-lavori-e-cse/) |
| 49 | `es-aimcp-r032` | es | Ejecuta la corrida 5 HVAC sobre mi selección actual en modo detalle. | Run electrical or HVAC takeoff on the current selection; show only ducts and fittings with size, length, area, gauge and kilos. | Fittings area direct, geometric estimate or fallback factor, method reported. | [github.com](https://github.com/JefaturaBIM94/RevitMCPBOQ) |
| 50 | `en-osarch-r011` | en | construct and demolish tasks show objects appearing and vanishing; where do I put the displacement for a MOVE task? | — | MOVE needs both input and output products; duplicate the element at the new location and link old as process input and new as product output. | [community.osarch.org #1131](https://community.osarch.org/discussion/1131/ifcopenshell-python-ifctask-predefinedtype-construction-demolition-move) |

## Ready test prompts

49 prompts for an MCP server or assistant connected to an IFC file. **All are synthetic**: written for testing, modelled on the real records in the data files, never real quotes. Russian and English get the most rows; other languages one to two each. The "What a good answer does" column is the research pass's expected behavior for the judge; the key check for this persona is nearly always: *did it state the source of each number and flag what is missing?*

| # | ID | Lang | Prompt (synthetic, as the user would type it) | File needed | Difficulty | What a good answer does |
|---|---|---|---|---|---|---|
| 1 | `en-aimcp-s004` | en | net wall area per storey excl openings, csv pls. say which qto source you used | yes | medium | Group walls by storey, use Qto NetSideArea else compute, export CSV, state source. |
| 2 | `en-autodesk-revit-export-s007` | en | BaseQuantities on walls - NetSideArea and GrossSideArea look the same, can you check? | yes | medium | Read Qto/BaseQuantities on walls, compare Gross vs Net, flag identical values. |
| 3 | `en-beginner-qa-s013` | en | give me total concrete volume of slabs and columns | yes | medium | Sum NetVolume for IfcSlab/IfcColumn with concrete material, state source and gaps. |
| 4 | `en-blogs-linkedin-s008` | en | do the walls have BaseQuantities? give me total NetVolume per wall type, flag missing | yes | medium | Read Qto/BaseQuantities, sum per type, list elements without quantities. |
| 5 | `en-gh-ifcopenshell-s002` | en | list walls where GrossSideArea equals NetSideArea, those with openings look wrong | yes | hard | Read Qto_WallBaseQuantities, flag walls with openings where gross equals net, explain possible cause. |
| 6 | `en-gh-thatopen-s012` | en | sum NetVolume per wall type from the Qto sets, table pls | yes | medium | Group IfcWall by type, sum Qto_WallBaseQuantities.NetVolume, return table with units. |
| 7 | `en-mea-s003` | en | give me total concrete volume per level from the structural ifc, and confirm the units are m3 not mm3, the numbers look off | yes | medium | Read project length/volume units, sum NetVolume or Qto_*BaseQuantities for concrete elements per storey, flag unit scale issues, report table. |
| 8 | `en-uk-anz-india-s007` | en | need floor area by level and external wall area for the cost plan, from the Qto not calculated pls | yes | medium | Read Qto_SlabBaseQuantities / Qto_WallBaseQuantities per storey, sum, warn where quantity sets are missing. |
| 9 | `en-s001` | en | need concrete wall volume per level for the pour sheet. NetVolume from Qto_WallBaseQuantities, and list any walls that dont have it | yes | medium | Filter IfcWall by concrete material, group by storey, sum NetVolume, list walls lacking Qto_WallBaseQuantities or NetVolume, state which volume (net/gross) was used. |
| 10 | `en-s002` | en | gross side area = net side area on most walls here, but theres windows in them. are the openings actually modelled as voids or is it baked in the mesh? | yes | hard | Check IfcRelVoidsElement/IfcRelFillsElement for walls, compare Gross/NetSideArea, report walls where they match despite fills, explain the cause. |
| 11 | `en-s004` | en | compare rev B and rev C ifc - what changed in slab areas and column counts since the bid set? just give me deltas I can price | yes | hard | Load both files, match by GlobalId, report added/removed/modified slabs and columns with area/count deltas, note unmatched GUID caveat. |
| 12 | `en-s006` | en | tag all IfcSlab and IfcBeam with the NRM2 code from the Type name prefix, then export count/area/volume by code to csv | yes | hard | Parse type-name prefixes, add classification references, aggregate quantities by code, write csv, report unmatched elements. |
| 13 | `en-s016` | en | exported from revit but the ifc has no Qto sets at all, only pset stuff. which export setting do I need so my takeoff tool sees areas and volumes | no | easy | Explain enabling Export base quantities in Revit IFC export settings, check version; verify in the model if loaded. |
| 14 | `en-s018` | en | I dont trust the slab areas in this model. recompute from geometry and compare with Qto_SlabBaseQuantities, show anything off by more than 2% | yes | hard | Compute geometry-based area, compare with stored quantities, list outliers with ratios. |
| 15 | `en-data-s001` | en | pull all IfcWall, group by storey and type name, sum NetSideArea from Qto_WallBaseQuantities, output csv/table. flag walls with no quantities | yes | medium | Traverse walls, resolve storey via containment, read Qto_WallBaseQuantities.NetSideArea, aggregate per storey+type, report missing quantity sets, emit CSV/table. |
| 16 | `en-data-s004` | en | slab volumes in my cost sheet are 8% off the model. which slabs have no Qto or odd units? | yes | hard | Compute slab volumes from Qto and geometry, compare with provided sheet if loaded, list slabs lacking quantities, unit mismatches, openings/overlaps, suggest cross-ref by GlobalId. |
| 17 | `en-proxy-s012` | en | I need volumes for every IfcBuildingElementProxy grouped by type name, the Qto set is empty so calc from geometry | yes | medium | Compute geometry volumes per proxy type, group and total, note missing Qto_BuildingElementProxyQuantities. |
| 18 | `en-qto-s003` | en | check walls where GrossSideArea equals NetSideArea but they have windows or doors | yes | hard | Find walls with openings via IfcRelVoidsElement/fillings, compare Gross and Net side areas, list suspicious equal values and note possible export issue. |
| 19 | `en-qto-s004` | en | make a BoQ per storey: slabs m2, walls m2, doors count, as a table I can paste in excel | yes | medium | Group elements by containing storey, compute totals per class with correct units, output CSV-like table, state which quantity source was used. |
| 20 | `en-qto-s005` | en | create a cost schedule 'Tender', add a cost item per wall type and link the quantities NetVolume | yes | hard | Create IfcCostSchedule, IfcCostItems per wall type, assign elements and NetVolume quantities, report totals; confirm before writing. |
| 21 | `en-qto-s006` | en | why does solibri show 20 m2 and my script 9.8 for the same wall? gross vs net? | no | easy | Explain Gross vs Net definitions, openings subtraction, and possible exporter differences; suggest checking Qto_WallBaseQuantities and geometry. |
| 22 | `en-qto-s018` | en | my cost item total is a bit off from volume x rate, is it rounding? | yes | medium | Recompute total with full-precision quantity and rate; explain rounding vs display; check unit basis and multiple cost values. |
| 23 | `en-spaces-s006` | en | total NetFloorArea per storey and compare with the sum of slab areas | yes | medium | Sum Qto per storey, compare against slab quantities, note discrepancy. |
| 24 | `en-struct-s003` | en | total rebar weight per column, from the IfcReinforcingBar geometry or Qto if there is one. kg | yes | hard | Read Qto_ReinforcingElementBaseQuantities or compute from NominalDiameter, length and steel density, aggregate by host; state assumptions. |
| 25 | `en-viewconv-s003` | en | excel of all walls: type name, material, NetSideArea, NetVolume. one row per wall | yes | medium | Query IfcWall, read Qto and material, write xlsx/csv, flag missing quantities. |
| 26 | `en-openings-s004` | en | for every wall give gross and net side area and openings area, flag where gross == net | yes | medium | Read Qto_WallBaseQuantities GrossSideArea/NetSideArea, compute opening area from voids, flag walls with voids but equal gross/net. |
| 27 | `ru-aimcp-s011` | ru | объём бетона по этажам, только монолит, ВОР в эксель. если в модели нет Qto - скажи прямо *(EN: Concrete volume per floor)* | yes | medium | Aggregate concrete volumes per storey from Qto or computed, export, flag missing quantities. |
| 28 | `ru-revit-auto-s009` | ru | сделай ведомость помещений по этажам с площадью и итогом по этажу, в эксель выгрузи *(EN: Make a schedule of rooms with area per floor)* | yes | medium | Create room schedule grouped by level with totals, or compute values and export to Excel/CSV; note unplaced rooms. |
| 29 | `ru-s007` | ru | сделай ведомость объемов по стенам: тип, площадь, объем, сумма по этажам. для сметы, срочно *(EN: Make a bill of quantities by wall types with area and volume.)* | yes | medium | Group IfcWall by type and storey, sum area and volume from base quantities, output table, note missing quantities. |
| 30 | `ru-dwg-revit-s014` | ru | выгрузи ведомость: тип, количество, площадь, по этажам, в эксель *(EN: Export a quantity table to Excel)* | yes | medium | Aggregate by type name and storey, area from Qto, write xlsx/csv, note missing quantities. |
| 31 | `ru-habr-dev-s010` | ru | выгрузи в эксель объёмы бетона по IfcWall и IfcSlab, по этажам, если нет Qto - посчитай по геометрии *(EN: Volumes by class to Excel)* | yes | medium | Group by class/storey, use Qto else compute via geometry, export table. |
| 32 | `ru-renga-nanocad-s005` | ru | нужен объем бетона по типам стен и плит, из ифс, в м3 *(EN: Total concrete volume by wall and slab type)* | yes | medium | Read Qto_WallBaseQuantities/Qto_SlabBaseQuantities NetVolume, group by type and material, sum in m3, warn if quantities are missing. |
| 33 | `ru-qto-s009` | ru | дай объемы стен по типам в м3, для сметы. если нет Qto то посчитай по геометрии *(EN: Volumes of walls by type in m3 for a cost estimate)* | yes | medium | Read NetVolume from Qto_WallBaseQuantities; fall back to geometry; group by type; report units. |
| 34 | `ru-spaces-s011` | ru | посчитай суммарную площадь помещений по этажам, нужна таблица для экспликации *(EN: Sum room areas by floor)* | yes | easy | Sum Net/Gross floor areas per storey, output table. |
| 35 | `es-latam-s003` | es | necesito los metrados de muros, losas y columnas por nivel, m2 y m3, para el presupuesto de mañana *(EN: Quantity takeoff of walls, slabs and columns for a budget)* | yes | medium | Extract Qto_WallBaseQuantities, Slab and Column quantities grouped by storey, flag missing quantities, output a table. |
| 36 | `es-qto-s012` | es | necesito las mediciones por capitulos (muros, forjados, carpinteria) para pasarlas a presupuesto en bc3 *(EN: Make measurements by chapter for BC3)* | yes | hard | Group elements into chapters, list quantities with units, offer CSV for BC3 import, state limits of BC3 writing. |
| 37 | `de-dach-s007` | de | Wandflächen und Volumen je Geschoss als Liste fürs LV, nur Außenwände. werden Öffnungen abgezogen? bitte angeben *(EN: Export wall areas and volumes per storey for tendering.)* | yes | medium | Read Qto_WallBaseQuantities NetSideArea/GrossSideArea, group by storey, filter external, state openings treatment. |
| 38 | `de-qto-s013` | de | kannst du mir die Mauerwerk-Mengen nach Geschoss ziehen, netto ohne Öffnungen, fürs LV (GAEB) *(EN: Quantities for bill of works (GAEB))* | yes | medium | Compute net wall volume/area per storey excluding openings, present in table suitable for GAEB position mapping. |
| 39 | `de-s008` | de | Mengen fuer die Ausschreibung ziehen: Mauerwerk Wandflaechen netto ohne Oeffnungen, nach Geschoss. Passt das mit Qto? *(EN: Take out masses for the tender (LV), grouped by trade.)* | yes | medium | Read NetSideArea from wall quantities, compare with geometry-derived values, group by storey, flag inconsistencies. |
| 40 | `fr-s012` | fr | je dois sortir les metres pour le DPGF : surfaces de murs nettes des ouvertures par niveau, et le nb de portes par type *(EN: Quantities for the DPGF: wall surfaces net of openings, by level.)* | yes | medium | Net wall areas by storey, count IfcDoor by type, flag missing quantities. |
| 41 | `it-s015` | it | mi serve il computo metrico dai muri e solai per piano, con m2 e m3, e dimmi se ci sono elementi senza quantita *(EN: Compute quantities for the computo metrico by category.)* | yes | medium | Aggregate by storey, list elements without quantities. |
| 42 | `ja-japan-s004` | ja | 積算用に、階ごとのRC壁・柱・梁のコンクリ体積を合計して。Qtoが無いものは形状から出せる？ *(EN: Total concrete volume of walls, columns and beams by storey for estimating)* | yes | hard | Aggregate NetVolume from Qto per IfcWall/IfcColumn/IfcBeam by storey and material, flag elements missing Qto and say whether geometry-derived values are available. |
| 43 | `ja-s013` | ja | 階ごとのコンクリート数量と型枠面積を拾いたいです。梁と柱と壁で分けて出せますか *(EN: Pull concrete and formwork areas by floor for a cost estimate.)* | yes | hard | Group volume and formwork-related surface areas by class and storey, explain assumptions. |
| 44 | `nl-dutch-s009` | nl | m2 binnenwand per NL-SfB code en aantal deuren met FireRating, naar excel kan? *(EN: m2 interior walls per NL-SfB code)* | yes | medium | Aggregate NetSideArea by classification; door count; export table. |
| 45 | `no-norway-s008` | no | trenger mengder: netto areal yttervegger per etasje, uten åpninger *(EN: Total net area of external walls per floor)* | yes | medium | Sum NetSideArea from Qto_WallBaseQuantities for external walls grouped by storey; note missing quantities. |
| 46 | `pt-brazil-s005` | pt-BR | preciso do quantitativo de área de parede e volume de concreto por pavimento pra planilha de orçamento *(EN: Sum wall area and concrete volume by storey for the budget)* | yes | medium | Read Qto_WallBaseQuantities/Qto_*, aggregate by storey, return table; note missing quantities. |
| 47 | `zh-s011` | zh | 帮我按楼层统计混凝土柱和梁的体积，导出表格，缺工程量的构件单独列出来 *(EN: Count columns and beams volume by floor for quantity takeoff.)* | yes | medium | Group columns and beams by storey, sum volumes, export table and list elements lacking quantity data. |
| 48 | `zh-classbsdd-s009` | zh | 按GB/T 51269分类编码把构件分组，统计墙和板的体积 *(EN: Group quantities by GB/T 51269 code.)* | yes | medium | Group elements by classification code from GB/T 51269 reference, sum volumes from Qto sets. |
| 49 | `zh-csdn-dev-s007` | zh | 各楼层楼板和墙的体积汇总一下，用Qto里的NetVolume，没有的话用几何算，两个对一下 *(EN: Sum slab and wall volume by storey, check against Qto)* | yes | hard | Read Qto_*BaseQuantities NetVolume, fall back to geometry volume, aggregate by storey, report mismatches and units. |

## How to role-play this persona in tests

**Voice.** Working professional preparing a price, usually with a deadline ("для сметы, срочно" in `ru-s007`, "for the cost plan", "para o orçamento", "fürs LV"). Short imperative sentences that name the **table** they want: *"сделай ведомость объемов по стенам: тип, площадь, объем, сумма по этажам"*, *"need floor area by level and external wall area for the cost plan, from the Qto not calculated pls"* (`en-uk-anz-india-s007`), *"帮我按楼层统计混凝土柱和梁的体积，导出表格，缺工程量的构件单独列出来"* (`zh-s011`). Asks "in Excel" or "as CSV" almost every time. Sprinkles in the **trap question**: "is it gross or net?", "m3 not mm3?", "is the Qto even there?".

**Typical context.** One IFC (Revit, ArchiCAD, Allplan, Tekla export) and an Excel sheet or estimating package waiting. Rarely states the IFC version or the exporter. If the better-informed variant, names the quantity set (`Qto_WallBaseQuantities`, `NetSideArea`). The data shows that estimators who come from open-source BIM tools write in fairly precise terms; commercial-software estimators write more loosely ("метраж", "объёмы").

**Knowledge level.**
- Strong: measurement rules, cost structures, unit rates, national classification systems, what a sensible number looks like (they sense that "wall area 9.8 vs 20.1" is wrong).
- Medium: spreadsheets; knows that models carry "quantities" but not where.
- Weak: IFC schema, why a quantity is absent, how voids work, relationship between type and instance quantities, geometry vs stored quantities.
- Believes: "the model knows the quantities"; "net means the openings are already subtracted".
- Wants the numbers; will challenge any number that does not match their own hand check or a second tool.

**What to test with this persona.**
- Source transparency: stored quantity vs recomputed from geometry; the assistant must say which, and show both when they differ (`en-s018`, `zh-csdn-dev-s007`).
- Missing data: an element without Qto must be listed, not counted as zero (`en-s001`, `it-s015`).
- Gross = Net trap (`en-s002`, `en-qto-s003`): a good answer checks whether openings are real voids.
- Units and scale (m3 vs mm3, `en-mea-s003`).
- Grouping: by level, by type name, by classification code; elements without a level appear in an "unassigned" bucket.
- Language: same figures in ru / zh / es / de / fr / it / ja / nl / no / pt.
- Honest limits: the assistant should not claim a specific national BoQ format (BC3, GAEB) is produced unless a tool really writes it (`es-qto-s012`, `de-qto-s013`).

**Typical follow-ups.**
1. "А это нетто или брутто?" / "net or gross?"
2. "Why does your total differ from my Excel / from Solibri?" (expects reconciliation: openings, units, missing items)
3. "Group by material" / "по слоям" / "per layer" (expects an honest answer if layer quantities are absent)
4. "Add the NRM2 / Uniclass code from the type name" (expects scope confirmation, a new file)
5. "Export to CSV with GlobalId so I can trace each row."
6. "Compare rev B and rev C, give me just the deltas I can price." (`en-s004`)
7. "Which elements have no quantities at all?"

**Quick judge checklist.**
- Is every total accompanied by its quantity source (Qto name or recomputed) and unit?
- Are elements without quantities listed separately?
- Does the answer address openings when the user asks about "net"?
- Does it avoid inventing rates or prices (the persona prices later; the assistant only supplies quantities unless asked and given a rate)?
- Are the figures consistent when the same question is asked in another language?
