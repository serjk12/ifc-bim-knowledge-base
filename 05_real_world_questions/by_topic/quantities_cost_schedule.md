# Quantity takeoff, cost (5D) and scheduling (4D)

Topic tags covered: `quantities_qto`, `scheduling_4d_cost_5d`. Source data: wave-1 research cells. 145 distinct real records (111 tagged quantities, 51 tagged scheduling/cost, with overlap; 130 distinct source URLs) and 123 distinct synthetic prompts (113 quantity + 16 scheduling/cost, with 6 shared). Language skew of the real data: English 134, Chinese 3, Dutch 2, Spanish 2, Russian 1, Japanese 1, German 1, Vietnamese 1. The skew is real: the questions come from GitHub issues (Revit IFC exporter, IfcOpenShell/Bonsai) and OSArch/buildingSMART forums. Estimators in other countries mostly work in national tools and ask in national forums that the research cells could not reach; the synthetic prompts compensate by covering 13 languages and are labelled synthetic wherever they appear.

## In plain words

An estimator, quantity surveyor or site manager wants numbers from the building model: how much concrete per floor, how many square metres of wall, how many doors of each type, how many tonnes of steel. This is **quantity takeoff** (QTO, "ВОР / ведомость объёмов", "Mengenermittlung", "metrado", "computo metrico", "積算", "算量"). In an IFC file the numbers can live in three places: (1) in **quantity sets** called `Qto_...BaseQuantities` that the authoring tool wrote at export time (`Qto_WallBaseQuantities.NetSideArea`, `Qto_SlabBaseQuantities.NetVolume`, ...), (2) in ordinary property sets that someone filled in, or (3) nowhere, in which case a tool must **compute** them from the 3D shape. These three sources can give different numbers, and "gross" (ignoring openings such as windows) differs from "net" (after subtracting them). The numbers are **exported values, not live formulas**: change the model afterwards and the stored values stay old. See [properties, quantities and property sets](../../01_ifc_basics/05_properties_quantities_psets.md).

**5D** adds money: a cost schedule is a tree of cost items, each with a quantity and a unit rate, linked to model elements; the total is quantity times rate, summed up the tree. **4D** adds time: a work schedule is a tree of tasks with dates and predecessor links, linked to the elements each task builds, demolishes or moves, so that a viewer can play the construction as an animation. IFC can describe both (`IfcCostSchedule`, `IfcCostItem`, `IfcWorkSchedule`, `IfcTask`), but commercial authoring tools rarely write them; most real projects take quantities out to Excel or an estimating package and build 4D in a separate tool ([domain overview: 4D, 5D](../../01_ifc_basics/08_domains_mep_structural_infra_4d5d_fm.md)). So an honest assistant must often answer "there is no cost data or schedule in this file; I can compute quantities". Revit-side settings that decide whether quantities exist at all are in the [Revit IFC export reference](../../03_software/revit/ifc_export_reference.md). Companion document: [coordination, clash, BCF and CDE](coordination_clash_bcf_cde.md).

## Problem map

Ranked by number of real records (my manual clustering of the 145 records; a record can fit two clusters, so counts overlap; "urls" = distinct source pages). Every row is discussed in the section with the same number below. Row 12 groups three small Bonsai-workflow problems (CSV import errors 4 records, assignment by query 4, quantities not live 3).

| # | Problem | How users describe it | Frequency signal | Root cause | Typical fix |
|---|---|---|---|---|---|
| 1 | Revit IFC export has no, partial or wrong base quantities | "BaseQuantities missing on some walls and roofs"; "no quantities on storey/space/ramp/proxy"; "custom IfcQty parameter works in IFC4 not IFC2x3"; "IFC4x3 exporter has no quantity sets" | 18 records, 16 urls, all English; synthetic demand: about 15 prompts ask about missing or empty quantities | "Export base quantities" is off in default setups; exporter supports only a subset of classes; version-specific bugs; IFC4x3 path unfinished | Tick "Export base quantities"; check exporter version; use Reference View setups; shared parameters `IfcQty...` as workaround; verify per class before trusting |
| 2 | Gross equals net, openings not subtracted, tools disagree | "GrossSideArea == NetSideArea in Bonsai while Solibri says 20.08 vs 9.81"; "wall gross and net side area are identical despite openings"; "Bonsai differs from Blender engine" | 16 records, 11 urls, all English; synthetic demand: about 19 prompts mention gross/net/openings | Openings baked into the mesh instead of modelled as voids; tool checks only `IfcRelVoidsElement`; exporter writes same value twice | Check `IfcRelVoidsElement`/`IfcRelFillsElement`; read both gross and net; compare with a second tool; say which was used |
| 3 | 4D: tasks, MOVE/construct/demolish, animation, Gantt, performance | "how do I model a MOVE task?"; "4D exported to GLB does not play"; "assign_product is quadratic"; "2 GB IFC with P6 schedule loads very slowly" | 14 records, 14 urls, all English; synthetic demand: about 8 | IFC expresses tasks and products but not scheduling logic engines; animation features young; many viewers ignore `IfcTask` | Use the `sequence.*` API, give MOVE both input and output products, link by selectors, use a 4D tool for logic |
| 4 | IfcSpace and room areas wrong, missing or identical | "gross and net floor area identical for all rooms"; "FloorArea missing in Revit 2022 only"; "zone area differs from the registry XML by 20 m2" | 12 records, 11 urls (en 11, ru 1); synthetic demand: about 13 | Exporter regressions per version; boundary rules; ifc5d intentionally skips spaces (legal meaning of areas) | Custom property sets, compute from geometry and label as such, compare against Revit area parameter |
| 5 | Open-source QTO returns odd values | "door width equals height when width < height"; "slab depth and width swapped"; "footing: 1 of 10 quantities right"; "volume off by 2% far from origin" | 12 records, 10 urls, all English | Bugs in specific class formulas; bounding-box approach under rotation; floating-point loss at big coordinates | Update; test class by class against hand calculation; use local coordinates; report the engine |
| 6 | Missing quantity kinds: weight, per-layer volumes, earthworks, rebar | "IFC base quantities do not include weight"; "only layer thickness is exported, need area and volume per layer"; "automatic QTO returns nothing for earthworks" | 12 records, 12 urls, all English; synthetic demand: about 11 | Base quantity templates define only some quantities; density lives in materials; IFC4x3 classes new | Compute weight = volume x density or MassPerLength x length; custom Qto; manual Qto for earthworks |
| 7 | Getting a BoQ out to Excel, CSV, PDF, BC3 with links to elements | "CSV export has junk columns, no unit column"; "rows must stay traceable to IFC elements"; "export priced BoQ as PDF"; "BC3 export" | 12 records, 10 urls (en 11, nl 1); synthetic demand: about 26 prompts ask for a table or Excel | Exports built for developers; GlobalIds needed to trace; national formats (BC3, GAEB, NRM) not native | Spreadsheet import/export with grouping, GlobalId column, PDF through typst script, BC3 through a dedicated tool |
| 8 | Estimating ecosystem and national practice | "Revit to Glodon BIM5D: plugin or IFC?"; "how to read IFC for MasterFormat estimating software"; "rules for members that are not modelled"; "NL-SfB takeoff" | 12 records, 12 urls (en 7, zh 2, es 1, nl 1, ja 1) | Estimating is done in national packages with their own measurement rules | Know the target format; map classification; document what was not modelled |
| 9 | Cost schedule (5D) totals do not match | "total differs from volume x rate"; "crew resource total 2.62 vs 3.58"; "product resource adds one extra door"; "wrong total when cost values use different UnitBasis" | 10 records, 8 urls, all English | Display rounding vs full precision; unit conversion (day vs 8 h); UnitBasis; parent items without own rate | Recompute at full precision; check units and UnitBasis; sum children |
| 10 | AI/MCP quantity tools | "Run the HVAC takeoff on my current selection in detail mode"; "how many fire doors on Level 2"; "generate a BC3 budget" | 6 records, 6 urls (en 4, es 1, vi 1) | Tools mix Qto, property and geometry methods; report of method matters | Always report method, units and gaps |
| 11 | Phasing, revisions and GUID stability for 4D/5D | "re-export from Revit without losing cost and schedule data"; "demolished elements and phase data are lost in IFC" | 4 records, 4 urls (en 3, de 1); synthetic demand: about 5 | Revit exports one phase at a time; GUID churn breaks links | Export per phase, add phase pset, re-link by match |
| 12 | Bonsai workflow friction: CSV import errors, assigning by query, quantities not live | "work schedule CSV import fails", "assign walls with concrete by query", "run calculation again with Shift+Q" | 11 records (4 + 4 + 3), all English | Optional columns assumed present; manual selection; on-demand calculation | Use query fields and regex; recalculate explicitly |

## Problems in depth

### 1. Revit export without base quantities

**Symptoms in users' words.**
- "BaseQuantities property set missing on some walls and roofs, mostly with voids." [Autodesk forum](https://forums.autodesk.com/t5/revit-structure-forum/ifc-basequantities-missing-on-some-elements/td-p/9943386)
- "Some base quantities (e.g. NetFootprintArea) are not exported though other tools show them." [GH Autodesk/revit-ifc#144](https://github.com/Autodesk/revit-ifc/issues/144)
- "Floors exported as IfcRamp have no BaseQuantities." [GH Autodesk/revit-ifc#969](https://github.com/Autodesk/revit-ifc/issues/969); "IfcBuildingStorey does not export with base quantities" [GH Autodesk/revit-ifc#479](https://github.com/Autodesk/revit-ifc/issues/479)
- "IfcWall lacks BaseQuantities unlike IfcWallStandardCase; forcing the class does not help." [GH Autodesk/revit-ifc#364](https://github.com/Autodesk/revit-ifc/issues/364)
- "IFC4x3 is official but the exporter lacks quantity sets; when?" [GH Autodesk/revit-ifc#768](https://github.com/Autodesk/revit-ifc/issues/768)
- "Wall overridden to IfcFurniture still exports with Qto_WallBaseQuantities." [GH Autodesk/revit-ifc#497](https://github.com/Autodesk/revit-ifc/issues/497)
- Non-programmer layman asking how to read IFC data for an estimating product, and an Indian estimating-software vendor asked to link to design software: [bSI forum](https://forums.buildingsmart.org/t/3953).
- Chinese test log of one slab, showing that Revit names are Family:Type:ElementId and the numbers (thickness 200, area 19.25, volume 3.85) come in model units: 某楼板……厚度200、面积19.25、体积3.85 ([cnblogs.com](https://www.cnblogs.com/herd/p/14908387.html)).

**Why it happens.** In Revit the quantity sets are written only if **Export base quantities** is ticked; the default IFC2x3 Coordination View setup has it off, the Reference View and Design Transfer View setups have it on ([Revit IFC export reference](../../03_software/revit/ifc_export_reference.md)). Autodesk documents the option as exporting the subset of quantities Revit supports. Several classes (storey, space, ramp, proxies, custom IFC2x3 quantities) have open bugs logged in Autodesk's tracker; a BEP that forbids "all parameters" ([bimcorner.com](https://bimcorner.com/ifc-export-rules-part-2-what-parameters-to-export-dos-and-donts/)) can leave estimators without what they need.

**What fixes it.** Check the export setup (base quantities on, IFC4 Reference View or equivalent), the exporter version, and the IFC class actually exported (a wall can become IfcCovering, a floor an IfcRamp); fall back to computing from geometry when the set is missing; as a workaround the data mentions shared parameters named like `IfcQtyNetVolume`.

**Good assistant behavior.** Before totalling, count elements per class with and without quantity sets and report that table. Say which classes have no quantities and why that may be (export setting, class mapping, version). Offer a geometry-derived value only as a labelled fallback.

**Clarifying questions.** Which authoring tool and exporter version? Which export setup/MVD? IFC2x3 or IFC4/4x3? Do you accept geometry-derived numbers where quantity sets are missing?

### 2. Gross equals net; openings; tools disagree

**Symptoms.**
- "After Perform Quantity Takeoff Bonsai reports Gross 9.81 = Net 9.81 whereas Solibri gives Gross 20.08; affects almost all walls." [GH IfcOpenShell/IfcOpenShell#9235](https://github.com/IfcOpenShell/IfcOpenShell/issues/9235), [GH IfcOpenShell/IfcOpenShell#9235](https://github.com/IfcOpenShell/IfcOpenShell/issues/9235)
- Autodesk tracker: "Wall gross side area and net side area are identical" [GH Autodesk/revit-ifc#496](https://github.com/Autodesk/revit-ifc/issues/496); "Base quantities wrong for concrete columns with openings" [GH Autodesk/revit-ifc#644](https://github.com/Autodesk/revit-ifc/issues/644)
- "IfcOpenShell QTO gives a wrong area for an IfcWindow defined by an IfcWindowType with mesh geometry; Blender shows the right value." [GH IfcOpenShell/IfcOpenShell#5349](https://github.com/IfcOpenShell/IfcOpenShell/issues/5349)
- "Wall-based openings from doors and windows behave differently from void families" [GH Autodesk/revit-ifc#621](https://github.com/Autodesk/revit-ifc/issues/621); an estimator wants HOLE/CUTOUT/EDGE voids distinguishable to filter provisions for the BoQ [GH Autodesk/revit-ifc#755](https://github.com/Autodesk/revit-ifc/issues/755).

**Why it happens.** Gross ignores openings, net subtracts them ([quantities reference](../../01_ifc_basics/05_properties_quantities_psets.md)). If the exporter bakes openings into the mesh (no `IfcRelVoidsElement`), a tool that decides "has openings?" from that relationship sees none and returns net = gross; the maintainers' own analysis in [GH IfcOpenShell/IfcOpenShell#9235](https://github.com/IfcOpenShell/IfcOpenShell/issues/9235) says exactly this. Different tools also use different rules for what counts (core only, finishes, connection geometry for NetVolume).

**What fixes it.** Check the relationships, compare Gross/Net pairs for walls that have windows, and recompute from geometry for suspect walls; always name the source.

**Good assistant behavior.** If a user says gross equals net and the walls have windows, check `IfcRelVoidsElement` and `IfcRelFillsElement` first; say whether openings are real voids or baked in; compare with the stored Qto; never silently "fix" by picking the larger number.

**Clarifying questions.** Do you want gross or net, and does your measurement rule deduct openings below a size (e.g. 0.5 m2)? Which tool is the reference (Solibri, Revit schedule, hand count)?

### 3. 4D: tasks, MOVE, animation, performance

**Symptoms.**
- "Construction and demolition tasks work, but where do I put the displacement for a MOVE task?" [OSArch forum](https://community.osarch.org/discussion/1131/ifcopenshell-python-ifctask-predefinedtype-construction-demolition-move)
- "Two identical walls, three tasks (construct, move, demolish): animation misbehaves." [GH IfcOpenShell/IfcOpenShell#2413](https://github.com/IfcOpenShell/IfcOpenShell/issues/2413)
- "4D simulation exported to GLB does not play in a GLB viewer." [GH IfcOpenShell/IfcOpenShell#3738](https://github.com/IfcOpenShell/IfcOpenShell/issues/3738)
- "P6 imported; only an interactive Gantt HTML; want a synced animated timeline like Fuzor or Synchro." [GH IfcOpenShell/IfcOpenShell#2050](https://github.com/IfcOpenShell/IfcOpenShell/issues/2050)
- "Assigning many products to a task via the API is O(n^2)." [GH IfcOpenShell/IfcOpenShell#9253](https://github.com/IfcOpenShell/IfcOpenShell/issues/9253); "4D playback on large models; JSON cache keyed by GlobalId." [OSArch forum](https://community.osarch.org/discussion/3580/4d-playback-performance-in-bonsai-on-large-models-what-i-found-and-where-im-stuck)
- Business context: a ~2 GB industrial IFC needs a P6 schedule, AWP/IWP and lookahead in a construction PM platform ([GH ThatOpen/engine_fragment#315](https://github.com/ThatOpen/engine_fragment/issues/315)).
- Open-source scheduler that stores plans as IFC 4.3 `IfcWorkPlan`/`IfcTask`; the 4D link to the building model is not implemented yet ([OSArch forum](https://community.osarch.org/discussion/3738/open-planner-studio-open-source-construction-scheduler-with-ifc-4-3-as-its-native-file-format)).

**Why it happens.** IFC holds the chain `IfcWorkPlan` → `IfcWorkSchedule` → `IfcTask`, dependency logic in `IfcRelSequence`, dates in `IfcTaskTime`, and links from tasks to products. It does not recalculate a critical path; a viewer or planner must. `IfcRelNests` only orders the display. A MOVE needs both an input and an output product, so the accepted answer was to duplicate the element at the new location and link the old one as input and the new one as output ([OSArch forum](https://community.osarch.org/discussion/1131/ifcopenshell-python-ifctask-predefinedtype-construction-demolition-move)). Many viewers do not show `IfcTask` at all, and Revit has no 4D of its own (reference doc, unverified background).

**What fixes it.** Build schedules through the `sequence.*` API, not by hand; keep task logic in a planner and write the result into IFC; link elements by selectors (class, storey, type); test playback on a small model first.

**Good assistant behavior.** Distinguish "list the tasks" (reading) from "shift a task and tell me what moves" (needs a scheduling engine). Report elements with no task and tasks with no elements. State that dates and float were taken from the file, not recomputed. Ask before creating a work schedule or assigning products.

**Clarifying questions.** Is there already a schedule in the file or must I create one? Source format (P6 XER, MS Project, Excel/CSV)? Which relation do you want between task and element (builds, demolishes, moves, uses)? Calendar and working days?

### 4. IfcSpace and room areas

**Symptoms.**
- "GrossFloorArea and NetFloorArea in Qto_SpaceBaseQuantities come out identical; only volumes differ." [GH Autodesk/revit-ifc#742](https://github.com/Autodesk/revit-ifc/issues/742)
- "FloorArea missing for rooms and areas only in Revit 2022." [GH Autodesk/revit-ifc#751](https://github.com/Autodesk/revit-ifc/issues/751); "In Revit 2023 NetFloorArea no longer exported, +1 from 2022 users." [GH Autodesk/revit-ifc#529](https://github.com/Autodesk/revit-ifc/issues/529)
- "Mass exported as IfcSpace swaps height and depth." [GH Autodesk/revit-ifc#908](https://github.com/Autodesk/revit-ifc/issues/908)
- "ifc5d QTO calculator never produces quantities for IfcSpace: all 13 formulas null." [GH IfcOpenShell/IfcOpenShell#8570](https://github.com/IfcOpenShell/IfcOpenShell/issues/8570) (maintainer answer: intentionally empty, areas have legal implications and rules are ambiguous)
- Russian: "площадь по геометрии зон не сходится с атрибутом и с XML АГР" (zone area from geometry differs from the attribute and from the registry XML, ~20 m2; [Habr](https://habr.com/ru/articles/1100956/))
- "I have two IfcSpaces to make, selecting walls gave one; Calculate All Quantities gives 0 ceiling area." [OSArch forum](https://community.osarch.org/discussion/comment/30080)

**Why it happens.** Space areas depend on boundary rules (core centre, finish face, room-bounding elements), exporter version, and national definitions (net floor area vs living area; German DIN 277, Russian TEP rules). The "planned" areas on spaces (GrossPlannedArea) are programme values, not measured ones ([quantities reference](../../01_ifc_basics/05_properties_quantities_psets.md)).

**What fixes it.** Custom property sets or user-defined mapping for the national measure; compute from geometry and label; compare to the authoring-tool area parameter and list differences above a threshold.

**Good assistant behavior.** Never present a space area as legally valid; say which attribute or computation it came from. List spaces with missing or zero area. When asked "total area per level" clarify GFA vs NFA vs sum of rooms.

**Clarifying questions.** Which area definition (gross, net, usable, national method)? Include shafts and stairs? Compare against what (brief, registry, Revit)?

### 5. Odd values from open-source QTO engines

**Symptoms.**
- "Qto_DoorBaseQuantities Width is right if width > height, otherwise it reports the height." [OSArch forum](https://community.osarch.org/discussion/comment/28629#Comment_28629)
- "Depth and Width in Qto_SlabBaseQuantities are swapped." [GH IfcOpenShell/IfcOpenShell#8053](https://github.com/IfcOpenShell/IfcOpenShell/issues/8053)
- "Table review: strip/beam footings under the IfcOpenShell engine get 1 of 10 quantities right, rest missing or swapped." [GH IfcOpenShell/IfcOpenShell#6305](https://github.com/IfcOpenShell/IfcOpenShell/issues/6305)
- "NetSideArea/GrossSideArea pick the wrong face on walls oriented along Y." [GH IfcOpenShell/IfcOpenShell#9237](https://github.com/IfcOpenShell/IfcOpenShell/issues/9237)
- "util.shape.get_volume loses precision far from origin: a 2.8 m3 wall gives 2.75 at E 500000, N 5000000." [GH IfcOpenShell/IfcOpenShell#9770](https://github.com/IfcOpenShell/IfcOpenShell/issues/9770)
- "Calculate All Quantities doesn't fill Qto_BuildingElementProxyQuantities for proxies." [GH IfcOpenShell/IfcOpenShell#4740](https://github.com/IfcOpenShell/IfcOpenShell/issues/4740)
- "Bounding box from geometry is distorted by world rotation; is USE_WORLD_COORDS False right?" [GH IfcOpenShell/IfcOpenShell#8102](https://github.com/IfcOpenShell/IfcOpenShell/discussions/8102)

**Why it happens.** Quantity formulas are written per class; a bounding box is not a dimension for rotated or non-rectangular elements; summing signed tetrahedra at coordinates in the millions loses floating-point precision ([geometry and units](../../01_ifc_basics/06_geometry_placement_coordinates_units.md)).

**What fixes it.** Update to a fixed build; recompute with a second method for a sample of elements; compute volumes relative to a local origin; use stored Qto where trustworthy.

**Good assistant behavior.** When asked for "length, width, height" of rotated elements, say which method was used (Qto, bounding box in local or world coordinates, profile). Spot-check a few elements against a manual calculation and mention the tolerance. For georeferenced models, warn about precision.

**Clarifying questions.** Local or world coordinates? Is the model georeferenced with large offsets? Which class (doors, slabs, footings are known trouble spots)?

### 6. Missing quantity kinds: weight, layers, earthworks, rebar

**Symptoms.**
- "Revit knows material density but IFC base quantities lack weight; how to get weight for costing and LCA?" [GH Autodesk/revit-ifc#545](https://github.com/Autodesk/revit-ifc/issues/545)
- "Calculate Gross/NetWeight from Pset_ProfileMechanical.MassPerLength times length, so hollow steel sections need not be modelled at LOD200." [GH IfcOpenShell/IfcOpenShell#6344](https://github.com/IfcOpenShell/IfcOpenShell/issues/6344)
- "Only layer thickness is exported; area and volume per layer needed for LCA." [GH Autodesk/revit-ifc#753](https://github.com/Autodesk/revit-ifc/issues/753)
- "Rebar not modelled; compute rebar weight per concrete volume as a custom Qto." [OSArch forum](https://community.osarch.org/discussion/2578/how-to-create-a-custom-qto-calculation); "How to quantify rebar in FreeCAD?" [OSArch forum](https://community.osarch.org/discussion/2549/freecad-quantity-schedule)
- "IfcEarthworksElement gets no quantities on automatic QTO." [GH IfcOpenShell/IfcOpenShell#6325](https://github.com/IfcOpenShell/IfcOpenShell/issues/6325); "UndisturbedVolume for IfcEarthworksCut returns the cut body, not the removed material" (fixed; [GH IfcOpenShell/IfcOpenShell#9376](https://github.com/IfcOpenShell/IfcOpenShell/issues/9376))
- "IfcGeographyElement has no base quantities." [GH IfcOpenShell/IfcOpenShell#6508](https://github.com/IfcOpenShell/IfcOpenShell/issues/6508); "Which IFC material entity should I use for a full material list?" [bSI forum](https://forums.buildingsmart.org/t/ifc-materials/4861)

**Why it happens.** Base quantity templates define length, area, volume and (in some classes) weight, not density, per-layer values or reinforcement ratios. Layered elements are one object in IFC; the per-material split must be derived from layer thickness, net area and density, or from modelling each layer as a separate part. New IFC4x3 classes are only partly supported by tools.

**What fixes it.** Compute weight = volume x density (state the density and where it came from) or MassPerLength x length; use `Qto_ReinforcingElementBaseQuantities` or `Pset_ConcreteElementGeneral.ReinforcementVolumeRatio` when rebar is not modelled (the options given in [OSArch forum](https://community.osarch.org/discussion/2578/how-to-create-a-custom-qto-calculation)); define a custom Qto with a clear name (never `Pset_`/`Qto_` prefixes for non-standard sets).

**Good assistant behavior.** Do not invent density or reinforcement ratio; ask or state a clearly labelled assumption (for example steel 7850 kg/m3 appears in synthetic prompts) and return the formula. Say when quantities are impossible because the model has no such element (rebar not modelled).

**Clarifying questions.** Which density or ratio does your cost method use? Layers as separate elements or as a layer set? Measured per layer or per element?

### 7. Getting the BoQ out: Excel, CSV, PDF, BC3

**Symptoms.**
- "Tender and cost work runs on spreadsheets; I need rows traceable to IFC elements (FAN-01..03 per room) and equal elements summed by floor." [GH IfcOpenShell/IfcOpenShell#7762](https://github.com/IfcOpenShell/IfcOpenShell/issues/7762)
- "CSV export has junk columns (Id, Hierarchy, Index, Children), lacks a unit column and decimal control; I just ctrl+C into Excel." [GH IfcOpenShell/IfcOpenShell#5736](https://github.com/IfcOpenShell/IfcOpenShell/issues/5736)
- "Script to print an IfcCostSchedule PRICEDBILLOFQUANTITIES to PDF; fill n/a/b/c columns from the quantity Formula (e.g. 2*1*1*8)." [OSArch forum](https://community.osarch.org/discussion/2963/small-script-to-print-pricedbillofquantities-to-pdf)
- "Replies ask about exporting budgets back to BC3 (Spanish FIEBDC)." [OSArch forum](https://community.osarch.org/discussion/3437/openconstructionerp-qto-boq-and-ai-estimating-with-ifc-and-revit)
- Dutch: "Opdrachtgever en calculator gebruiken tabellen om te controleren wat geleverd is: 'hebben alle 212 deuren een FireRating?' of 'm2 binnenwand per NL-SfB-code'" (client and estimator use tables to check what was delivered: do all 212 doors have FireRating, m2 interior wall per NL-SfB code; [GH OpenAEC-Foundation/OpenAEC-BIM-validator#19](https://github.com/OpenAEC-Foundation/OpenAEC-BIM-validator/issues/19))
- Russian developer: "объёмы в Ревите 17 кликов, в ifcopenshell 40 строк; IFC слишком сложный" (quantities are 17 clicks in Revit, 40 lines in IfcOpenShell; IFC is too complex; [Habr](https://habr.com/ru/articles/868186/))

**Why it happens.** Estimators think in tables with units and trace codes; IFC tools output hierarchies. Each country has its own export format (BC3/FIEBDC, GAEB, NRM, MasterFormat, NL-SfB codes).

**What fixes it.** One row per element or per group with GlobalId, class, type, storey, material, quantity name, unit and source; grouping by a code or aggregator; separate national export step.

**Good assistant behavior.** Put the unit and source in column headers, include an "unquantified" list, include a total with the grouping rule, and say the format limits (what a BC3 or GAEB writer can and cannot carry). Do not paste rates from memory.

**Clarifying questions.** Which breakdown (storey, zone, type, classification code)? One row per element or aggregated? Which receiving system and format?

### 8. Estimating ecosystem and national practice

**Symptoms.** Chinese: "revit模型怎么导进广联达BIM5D，插件和IFC哪个好" (how to get a Revit model into Glodon BIM5D, plug-in or IFC; [bbs.zhulong.com](https://bbs.zhulong.com/106010_group_3002227/detail33178172/); answer in the record: the plug-in reads Revit source data directly and is richer than IFC) and the MEP route "机电模型从Revit出IFC再导进BIM5D的步骤" ([zhulong.com](https://www.zhulong.com/zt_bim_3002296/detail40283815/)). Japanese: "図面から数量を拾うのが時間と精度の両立が難しい。モデル化されない部材の数量ルールは？" (time and accuracy conflict when taking quantities off drawings; what are the rules for members that are not modelled; [note](https://note.com/bold_cobra9180/n/n4f52d62f230f)). Dutch contractor experiment with NLCS classification in IBIS ([GH nl-digigo/NLCS#687](https://github.com/nl-digigo/NLCS/issues/687)). Spanish: Planbim's information matrix mapping each parameter to IFC attribute/pset/property and required/optional ([planbim.cl](https://planbim.cl/documentos/mide/)). English: Masterformat-based estimating vendor ([bSI forum](https://forums.buildingsmart.org/t/3953)), "Qto_*** properties expectations" ([bSI forum](https://forums.buildingsmart.org/t/6298)).

**Why it happens.** Quantity rules (what is deducted, how finishes are counted, how unmodelled items are added) are national and company conventions; IFC base quantities are deliberately independent of any measurement method.

**What fixes it.** Make the rule explicit in the request and the answer; use classification codes to group; keep a list of items that need manual takeoff.

**Good assistant behavior.** Say that base quantities are geometry-based and that a national method may differ. Ask for the measurement rule before totalling for a tender.

**Clarifying questions.** Which method (NRM, DIN 277/VOB, CTE, GB, national)? Which classification? Which software receives the numbers?

### 9. Cost schedule totals that do not match

**Symptoms.**
- "Cost total does not match displayed volume times rate." [GH IfcOpenShell/IfcOpenShell#6401](https://github.com/IfcOpenShell/IfcOpenShell/issues/6401) (answer: display rounding; real volume 3.956403 x 1945.71 = 7698.01)
- "Constituent resources of a crew sum to 2.62 after assigning to a cost article, panel shows 3.58." [GH IfcOpenShell/IfcOpenShell#5706](https://github.com/IfcOpenShell/IfcOpenShell/issues/5706) (suspected day vs hours, 8 h assumed)
- "Product resource 'Doors' counts 1 before assigning elements; total one too many." [GH IfcOpenShell/IfcOpenShell#5155](https://github.com/IfcOpenShell/IfcOpenShell/issues/5155)
- "A single cost item with several cost values of different UnitBasis shows wrong total." [GH IfcOpenShell/IfcOpenShell#8625](https://github.com/IfcOpenShell/IfcOpenShell/issues/8625) (confirmed, fixed)
- "Parents of subitems show summed quantities but not summed total cost." [GH IfcOpenShell/IfcOpenShell#7354](https://github.com/IfcOpenShell/IfcOpenShell/issues/7354)
- "Resource usage decimals affect the cost calculation." [GH IfcOpenShell/IfcOpenShell#5693](https://github.com/IfcOpenShell/IfcOpenShell/issues/5693)

**Why it happens.** `IfcCostValue` multiplies a unit cost by summed quantities; nested items sum by cost type; unit bases and time units are converted; the UI rounds for display ([5D overview](../../01_ifc_basics/08_domains_mep_structural_infra_4d5d_fm.md)).

**What fixes it.** Recompute at full precision; list every cost value with its UnitBasis and quantity; check unit conversions; sum children for parents.

**Good assistant behavior.** Show the arithmetic ("3.956403 m3 x 1945.71 = 7698.01") and mention rounded vs unrounded; never invent rates or currency; if there is no cost schedule in the file say "no cost data" (the 5D section of the reference states that a Revit schedule with prices is not exported as `IfcCostSchedule`).

**Clarifying questions.** Which currency and price list? Rounded or full-precision quantities for pricing? Do you want me to create a schedule, or analyse an existing one?

### 10. AI/MCP quantity tools: what existing ones do

README prompts show what users will ask: "How many fire doors are on Level 2?", "Extract concrete quantities for Level 1" ([GitHub](https://github.com/Daviidro/ifcopenshell-mcp)); "how many windows, doors, chimneys or ramps; largest window; total wall area for painters" ([GitHub](https://github.com/ekkodale/IFC-MCP)); "Generate a BC3 budget file in Spanish" ([GitHub](https://github.com/JotaDeRodriguez/Bonsai_mcp)); Spanish: "Ejecuta la corrida 5 HVAC sobre mi selección actual en modo detalle" (run HVAC takeoff run 5 on my current selection in detail mode; fittings area is direct, geometric estimate or fallback factor, and the method is reported; [GitHub](https://github.com/JefaturaBIM94/RevitMCPBOQ)); Vietnamese: "Thống kê cửa, phòng; khối lượng tường, sàn" (count doors and rooms; wall and slab quantities; try it on a draft model first; [GitHub](https://github.com/andyluu98/vn-revit-mcp)).

**Good assistant behavior.** Reporting the method used for each number (Qto, property, geometry, fallback factor) is the pattern to reward. Run on the current selection when asked, not on the whole model. Retried write calls must not duplicate cost items.

### 11. Phasing, revisions and keeping 4D/5D links alive

**Symptoms.** "How can a Revit model be re-exported to IFC and updated in BlenderBIM without losing cost and schedule data added to the earlier IFC?" ([OSArch forum](https://community.osarch.org/discussion/1131/ifcopenshell-python-ifctask-predefinedtype-construction-demolition-move), forum thread on versioning; answers: a reload-link feature or an import-and-relink of 4D/5D data). German: "Revit Phasen nach IFC exportieren": Revit exports one phase at a time, demolished elements and phase data are lost; export per phase, filter in the viewer, add a custom pset with phase created/demolished ([bim-me-up.com](https://bim-me-up.com/revit-phasen-nach-ifc-exportieren/)). English: "Is there any Pset or parameter for IFC phasing?" ([GH Autodesk/revit-ifc#704](https://github.com/Autodesk/revit-ifc/issues/704)).

**Why it happens.** Cost items and tasks point at elements through GlobalIds; if the exporter regenerates GlobalIds the links break (see GUID churn in the [coordination document](coordination_clash_bcf_cde.md)). Phase is a Revit concept without a standard IFC property.

**Good assistant behavior.** For "which priced or scheduled elements changed since the last revision", first diff by GlobalId, report the overlap, then intersect the changed set with elements that have cost items or tasks. Flag links that point to removed elements.

### 12. Bonsai workflow friction: CSV import, assignment by query, stale quantities

**Symptoms.** "Work schedule CSV import fails; CSV lacks Relationships column" ([GH IfcOpenShell/IfcOpenShell#8580](https://github.com/IfcOpenShell/IfcOpenShell/issues/8580), fixed: treat the optional column as blank); "error while importing cost-schedule CSV" ([GH IfcOpenShell/IfcOpenShell#6920](https://github.com/IfcOpenShell/IfcOpenShell/issues/6920)); "assigning elements to a cost item needs select, unit, click; want a query such as walls with concrete" ([GH IfcOpenShell/IfcOpenShell#5390](https://github.com/IfcOpenShell/IfcOpenShell/issues/5390), later implemented); formwork item over walls and columns whose quantity property names differ, so regex per element ([GH IfcOpenShell/IfcOpenShell#6616](https://github.com/IfcOpenShell/IfcOpenShell/issues/6616)); "ifc5d filter by location Somelevel returns nothing" with the workaround of using the containing-structure name ([GH IfcOpenShell/IfcOpenShell#7371](https://github.com/IfcOpenShell/IfcOpenShell/issues/7371)); "Problems with quantity take-offs: some quantities in the IFC are not correct" (answer: QTO is not live, run the calculation explicitly, Shift+Q; aggregates were missing too; [GH IfcOpenShell/IfcOpenShell#4964](https://github.com/IfcOpenShell/IfcOpenShell/issues/4964)); "34 records calculated but nothing in the quantity sets" ([GH IfcOpenShell/IfcOpenShell#9407](https://github.com/IfcOpenShell/IfcOpenShell/discussions/9407)).

**Good assistant behavior.** After editing geometry, re-run the quantity calculation before reporting numbers and say that it was done. Before importing a CSV, check required columns and report which optional ones are absent. Use query selectors rather than manual selection when the user describes a rule ("all concrete walls").

## Real questions

All rows are real records (paraphrased by the research cells). Non-English rows keep the original language; where the cell stored only an English paraphrase, the original-language page title is given and noted. Persona is the inferred role of the asker.

| # | Lang | Question (original-language paraphrase) | EN gloss | Persona | Source |
|---|---|---|---|---|---|
| R1 | en | BaseQuantities property set missing on some walls and roofs, mostly with voids | Revit IFC2x3 export without base quantities on some walls | structural_engineer | [Autodesk forum](https://forums.autodesk.com/t5/revit-structure-forum/ifc-basequantities-missing-on-some-elements/td-p/9943386) |
| R2 | en | some base quantities (e.g. NetFootprintArea) are not exported to IFC; shows Solibri comparison | quantities other tools show are missing | architect | [GH Autodesk/revit-ifc#144](https://github.com/Autodesk/revit-ifc/issues/144) |
| R3 | en | IfcWall lacks BaseQuantities unlike IfcWallStandardCase; forcing the class does not help. Is this normal? | class affects whether quantities exist | bim_coordinator | [GH Autodesk/revit-ifc#364](https://github.com/Autodesk/revit-ifc/issues/364) |
| R4 | en | IfcRamp from floors has no BaseQuantities; IFC2x3 works; test RVT linked | ramps without quantities in IFC4 | architect | [GH Autodesk/revit-ifc#969](https://github.com/Autodesk/revit-ifc/issues/969) |
| R5 | en | empty issue body; commenters confirm same on Revit 2022/2023 for storeys and spaces | storey exported without base quantities | bim_manager | [GH Autodesk/revit-ifc#479](https://github.com/Autodesk/revit-ifc/issues/479) |
| R6 | en | tested IfcQtyNetVolume parameter from the exporter's shared parameter file; appears for proxies in IFC4 but not IFC2x3 | custom base quantity works in IFC4 only | bim_coordinator | [GH Autodesk/revit-ifc#594](https://github.com/Autodesk/revit-ifc/issues/594) |
| R7 | en | IFC4x3 is official but the exporter lacks quantity sets; when will it be supported? | IFC4x3 quantity sets in Revit | bim_coordinator | [GH Autodesk/revit-ifc#768](https://github.com/Autodesk/revit-ifc/issues/768) |
| R8 | en | Qto_CoveringBaseQuantities lacks Width for basic walls mapped to IfcCovering | wall exported as covering misses width | estimator_qs | [GH Autodesk/revit-ifc#872](https://github.com/Autodesk/revit-ifc/issues/872) |
| R9 | en | NetWeight shared parameter errors on export or does not appear in IFC | beam weight not exported | estimator_qs | [GH Autodesk/revit-ifc#764](https://github.com/Autodesk/revit-ifc/issues/764) |
| R10 | en | Exported schedule property sets lack area and perimeter | schedule-as-pset incomplete | estimator_qs | [Autodesk forum](https://forums.autodesk.com/t5/revit-architecture-forum/revit-schedule-as-property-sets-missing-area-and-perimeter-in/td-p/8835632) |
| R11 | en | Bonsai gross side area is the same as net, Solibri gives different gross; no IfcRelVoidsElement in the model | openings baked into mesh | estimator_qs | [GH IfcOpenShell/IfcOpenShell#9235](https://github.com/IfcOpenShell/IfcOpenShell/issues/9235) |
| R12 | en | Bonsai GrossSideArea equals NetSideArea while Solibri gives 20.08 vs 9.81 | tool disagreement on wall area | estimator_qs | [GH IfcOpenShell/IfcOpenShell#9235](https://github.com/IfcOpenShell/IfcOpenShell/issues/9235) |
| R13 | en | 6 walls of different geometry show identical first NetSideArea; second NetSideArea correct | duplicate parameter names in IfcWallStandardCase quantities | bim_coordinator | [GH Autodesk/revit-ifc#141](https://github.com/Autodesk/revit-ifc/issues/141) |
| R14 | en | IfcOpenShell QTO gives wrong area for an IfcWindow defined by an IfcWindowType with mesh geometry; Blender shows right value | engines disagree for mesh-based types | estimator_qs | [GH IfcOpenShell/IfcOpenShell#5349](https://github.com/IfcOpenShell/IfcOpenShell/issues/5349) |
| R15 | en | all three appear as IfcOpening.OPENING in Solibri; want to distinguish HOLE, CUTOUT, EDGE to filter provisions for BoQ | void types lost | estimator_qs | [GH Autodesk/revit-ifc#755](https://github.com/Autodesk/revit-ifc/issues/755) |
| R16 | en | gross and net floor area in Qto_SpaceBaseQuantities have the same value in the IFC; only volumes differ | identical space areas | bim_coordinator | [GH Autodesk/revit-ifc#742](https://github.com/Autodesk/revit-ifc/issues/742) |
| R17 | en | FloorArea missing for rooms and areas only in Revit 2022; workaround user-defined pset txt file | version-specific missing area | bim_coordinator | [GH Autodesk/revit-ifc#751](https://github.com/Autodesk/revit-ifc/issues/751) |
| R18 | en | German Revit: can Qto_SpaceBaseQuantities be extended or overridden via map.txt? | standard Qto sets are fixed; use custom Psets | bim_manager | [GH Autodesk/revit-ifc#865](https://github.com/Autodesk/revit-ifc/issues/865) |
| R19 | en | all 13 Qto_SpaceBaseQuantities formulas are null so no quantities and no warning | ifc5d silently skips IfcSpace | developer | [GH IfcOpenShell/IfcOpenShell#8570](https://github.com/IfcOpenShell/IfcOpenShell/issues/8570) |
| R20 | ru | площадь по геометрии зон не сходится с атрибутом и с XML АГР | zone area from geometry differs from attribute and registry XML | bim_coordinator | [Habr](https://habr.com/ru/articles/1100956/) |
| R21 | en | Qto_DoorBaseQuantities Width is right if width>height, otherwise reports the height | door width bug | architect | [OSArch forum](https://community.osarch.org/discussion/comment/28629#Comment_28629) |
| R22 | en | slab base quantities swap depth and width | slab width/depth swapped | architect | [GH IfcOpenShell/IfcOpenShell#8053](https://github.com/IfcOpenShell/IfcOpenShell/issues/8053) |
| R23 | en | table review: strip/beam footings under IfcOpenShell engine only get 1 of 10 quantities right | footing quantities | structural_engineer | [GH IfcOpenShell/IfcOpenShell#6305](https://github.com/IfcOpenShell/IfcOpenShell/issues/6305) |
| R24 | en | Qto on roof slab and door yields wrong numbers; screenshots only | wrong QTO on roof slab and door | estimator_qs | [GH IfcOpenShell/IfcOpenShell#4011](https://github.com/IfcOpenShell/IfcOpenShell/issues/4011) |
| R25 | en | Signed tetrahedra volume at projected coordinates loses precision; 2.8 m3 wall gives 2.75 | volume error far from origin | researcher_academic | [GH IfcOpenShell/IfcOpenShell#9770](https://github.com/IfcOpenShell/IfcOpenShell/issues/9770) |
| R26 | en | building a QTO viewer table; bounding box from geometry is distorted by world rotation | best practice for length/thickness/height | developer | [GH IfcOpenShell/IfcOpenShell#8102](https://github.com/IfcOpenShell/IfcOpenShell/discussions/8102) |
| R27 | en | count beams correctly but cannot get dimensions | beam BoQ dimensions inaccurate | estimator_qs | [GH IfcOpenShell/IfcOpenShell#7540](https://github.com/IfcOpenShell/IfcOpenShell/discussions/7540) |
| R28 | en | console app generates wexbim and a props file; wants X,Y,Z, area and volume per object; bounding-box attempt is wrong because units are not converted | areas and dimensions are subjective, prefer Qto | developer | [GH xBimTeam/XbimEssentials#619](https://github.com/xBimTeam/XbimEssentials/issues/619) |
| R29 | en | trying to get a budget for a small toilet building but some quantities in the IFC are not correct | stale or missing quantities; recalc | estimator_qs | [GH IfcOpenShell/IfcOpenShell#4964](https://github.com/IfcOpenShell/IfcOpenShell/issues/4964) |
| R30 | en | wants auto room in closed wall loop; QTO says 34 records calculated but nothing in quantity sets | room system and QTO output | architect | [GH IfcOpenShell/IfcOpenShell#9407](https://github.com/IfcOpenShell/IfcOpenShell/discussions/9407) |
| R31 | en | base quantities in IFC do not include weight though weight is critical for costing and LCA | weight missing | estimator_qs | [GH Autodesk/revit-ifc#545](https://github.com/Autodesk/revit-ifc/issues/545) |
| R32 | en | calculate Gross/NetWeight from MassPerLength times length so hollow steel sections need not be modelled in detail | steel weight at low LOD | estimator_qs | [GH IfcOpenShell/IfcOpenShell#6344](https://github.com/IfcOpenShell/IfcOpenShell/issues/6344) |
| R33 | en | only layer thickness is exported by Revit; area and volume per layer needed for LCA | per-layer quantities | researcher_academic | [GH Autodesk/revit-ifc#753](https://github.com/Autodesk/revit-ifc/issues/753) |
| R34 | en | wants rebar weight per concrete volume as custom Qto for cost schedule; rebar not modeled | rebar estimate without rebar | estimator_qs | [OSArch forum](https://community.osarch.org/discussion/2578/how-to-create-a-custom-qto-calculation) |
| R35 | en | wants to use IfcEarthworks elements but automatic quantity take-off returns nothing | earthworks QTO unsupported | civil_infra_engineer | [GH IfcOpenShell/IfcOpenShell#6325](https://github.com/IfcOpenShell/IfcOpenShell/issues/6325) |
| R36 | en | Measuring in PDF for life cycle assessment; want IFC takeoff tool, free if possible | which software lists material quantities | student_beginner | [bSI forum](https://forums.buildingsmart.org/t/which-software-to-create-lists-of-quantities-of-the-used-building-materials/5181) |
| R37 | en | Tender and cost work runs on spreadsheets; need rows traceable to IFC elements | BoQ CSV with element links | estimator_qs | [GH IfcOpenShell/IfcOpenShell#7762](https://github.com/IfcOpenShell/IfcOpenShell/issues/7762) |
| R38 | en | Browser view has no PDF/print export; CSV export has junk columns, no unit column, no decimal setting | BoQ export usability | estimator_qs | [GH IfcOpenShell/IfcOpenShell#5736](https://github.com/IfcOpenShell/IfcOpenShell/issues/5736) |
| R39 | en | how to keep a CSV BoQ linked to the IFC cost schedule, and let one cost item match differently named quantities | linked CSV cost schedule | estimator_qs | [OSArch forum](https://community.osarch.org/discussion/2887/dynamic-csv-to-cost-schedule-now-available) |
| R40 | en | author asks for feedback; replies ask about Apple ARM, BricsCAD, and exporting budgets back to BC3 | open-source QTO/BOQ with BC3 | vendor_support | [OSArch forum](https://community.osarch.org/discussion/3437/openconstructionerp-qto-boq-and-ai-estimating-with-ifc-and-revit) |
| R41 | en | Three-tier quantity source; outputs Excel and PDF; wants honest accuracy feedback | BaseQuantities then Psets then geometry | developer | [OSArch forum](https://community.osarch.org/discussion/3418/free-ifc-concrete-boq-looking-for-test-files-and-honest-feedback) |
| R42 | en | Cost rows are not one-to-one with model quantities; wants software to overlay and compare | quantity cross-check | estimator_qs | [OSArch forum](https://community.osarch.org/discussion/comment/27265) |
| R43 | en | attached model and screenshot showing a calculation difference in cost item; asks for 'fixed' value vs 'fixed rate' | total vs volume x rate | estimator_qs | [GH IfcOpenShell/IfcOpenShell#6401](https://github.com/IfcOpenShell/IfcOpenShell/issues/6401) |
| R44 | en | constituent resources of a crew resource sum to 2.62 but the resource panel shows 3.58 | crew total mismatch | estimator_qs | [GH IfcOpenShell/IfcOpenShell#5706](https://github.com/IfcOpenShell/IfcOpenShell/issues/5706) |
| R45 | en | resource assigned to cost item already counts 1 before any elements are added | product resource off by one | estimator_qs | [GH IfcOpenShell/IfcOpenShell#5155](https://github.com/IfcOpenShell/IfcOpenShell/issues/5155) |
| R46 | en | a single IfcCostItem with multiple IfcCostValue records of different UnitBasis shows wrong Total Cost | UnitBasis bug | estimator_qs | [GH IfcOpenShell/IfcOpenShell#8625](https://github.com/IfcOpenShell/IfcOpenShell/issues/8625) |
| R47 | en | parents of subitems show summed quantities but not summed total cost | parent totals | estimator_qs | [GH IfcOpenShell/IfcOpenShell#7354](https://github.com/IfcOpenShell/IfcOpenShell/issues/7354) |
| R48 | en | assigning elements to cost item needs select, unit, click; wants query such as walls with concrete | query-based assignment | estimator_qs | [GH IfcOpenShell/IfcOpenShell#5390](https://github.com/IfcOpenShell/IfcOpenShell/issues/5390) |
| R49 | en | work schedule CSV import fails; CSV lacks Relationships column | CSV import crash | contractor_site | [GH IfcOpenShell/IfcOpenShell#8580](https://github.com/IfcOpenShell/IfcOpenShell/issues/8580) |
| R50 | en | While following a 5D costing crash course I imported, exported and re-imported the cost CSV and got an error | cost CSV round trip | student_beginner | [GH IfcOpenShell/IfcOpenShell#5492](https://github.com/IfcOpenShell/IfcOpenShell/issues/5492) |
| R51 | en | construct and demolish tasks show objects appearing and vanishing; where do I put the displacement for a MOVE task? | MOVE in 4D | contractor_site | [OSArch forum](https://community.osarch.org/discussion/1131/ifcopenshell-python-ifctask-predefinedtype-construction-demolition-move) |
| R52 | en | 4D simulation I export to glb file format but its not working in glb viewer | 4D GLB export | bim_coordinator | [GH IfcOpenShell/IfcOpenShell#3738](https://github.com/IfcOpenShell/IfcOpenShell/issues/3738) |
| R53 | en | P6 schedule imported, only an interactive Gantt HTML is produced; wants native synced animated timeline like Fuzor/Synchro | P6 timeline animation | contractor_site | [GH IfcOpenShell/IfcOpenShell#2050](https://github.com/IfcOpenShell/IfcOpenShell/issues/2050) |
| R54 | en | integrating fragments into a construction PM platform, 2 GB industrial IFC loads very slow, need IFC plus Primavera P6 schedule, AWP/IWP, lookahead | large IFC with P6 | contractor_site | [GH ThatOpen/engine_fragment#315](https://github.com/ThatOpen/engine_fragment/issues/315) |
| R55 | en | Connect to Claude/ChatGPT and let the AI model prepare and edit plans! (open-source scheduler with IFC 4.3 as native format) | AI-edited IFC schedule | developer | [OSArch forum](https://community.osarch.org/discussion/comment/30650) |
| R56 | en | How can a Revit model be re-exported to IFC and updated in BlenderBIM without losing cost and schedule data? | revision update keeps 4D/5D | estimator_qs | [OSArch forum](https://community.osarch.org/discussion/1131/ifcopenshell-python-ifctask-predefinedtype-construction-demolition-move) |
| R57 | de | Revit Phasen nach IFC exportieren (cell stored an English paraphrase: how to get phase created/demolished into IFC) | phases lost in IFC export | bim_coordinator | [bim-me-up.com](https://bim-me-up.com/revit-phasen-nach-ifc-exportieren/) |
| R58 | en | Hello, is there any Pset or Parameter for IFC Phasing? | phasing in IFC | bim_coordinator | [GH Autodesk/revit-ifc#704](https://github.com/Autodesk/revit-ifc/issues/704) |
| R59 | ru | объёмы в Ревите 17 кликов, в ifcopenshell 40 строк; IFC слишком сложный | QTO is 17 clicks in Revit, ~40 lines in IfcOpenShell | developer | [Habr](https://habr.com/ru/articles/868186/) |
| R60 | ja | 図面から数量を拾うのが時間と精度の両立が難しい。モデル化されない部材の数量ルールは？ | taking quantities off drawings costs time and accuracy; rules for unmodelled members? | estimator_qs | [note](https://note.com/bold_cobra9180/n/n4f52d62f230f) |
| R61 | nl | Opdrachtgever en calculator gebruiken tabellen om te controleren wat geleverd is: 'hebben alle 212 deuren een FireRating?' of 'm2 binnenwand per NL-SfB-code' | client and estimator check delivery with tables: do all 212 doors have FireRating, m2 interior wall per NL-SfB code | estimator_qs | [GH OpenAEC-Foundation/OpenAEC-BIM-validator#19](https://github.com/OpenAEC-Foundation/OpenAEC-BIM-validator/issues/19) |
| R62 | nl | Experiment Hoeveelheden berekenen met NLCS Classificatie VH door VolkerWessels | quantity takeoff experiment with NLCS classification, tested in IBIS | estimator_qs | [GH nl-digigo/NLCS#687](https://github.com/nl-digigo/NLCS/issues/687) |
| R63 | zh | revit模型怎么导进广联达BIM5D，插件和IFC哪个好 | how do I get a Revit model into Glodon BIM5D, plug-in or IFC? | contractor_site | [bbs.zhulong.com](https://bbs.zhulong.com/106010_group_3002227/detail33178172/) |
| R64 | zh | 机电模型从Revit出IFC再导进BIM5D的步骤 | steps to export a Revit MEP model as IFC and import into BIM5D | mep_engineer | [zhulong.com](https://www.zhulong.com/zt_bim_3002296/detail40283815/) |
| R65 | zh | 某楼板 楼板:JG-b-200-0现浇:394165 的属性：厚度200、面积19.25、体积3.85、顶标高7200底标高7000 | test log: one slab with thickness, area, volume and elevations from IFC | bim_coordinator | [cnblogs.com](https://www.cnblogs.com/herd/p/14908387.html) |
| R66 | es | Ejecuta la corrida 5 HVAC sobre mi selección actual en modo detalle. | run HVAC takeoff run 5 on my current selection in detail mode | estimator_qs | [GitHub](https://github.com/JefaturaBIM94/RevitMCPBOQ) |
| R67 | es | Matriz de Información de Entidades (MIDE) - Planbim (cell stored an English paraphrase: table linking each parameter to IFC attribute, Pset, property, required or optional) | national information matrix with Qto_SiteBaseQuantities as required | bim_manager | [planbim.cl](https://planbim.cl/documentos/mide/) |
| R68 | vi | Thống kê cửa, phòng; khối lượng tường, sàn | count doors and rooms; wall and slab quantities | architect | [GitHub](https://github.com/andyluu98/vn-revit-mcp) |
| R69 | en | How many fire doors are on Level 2? | README prompt for an IFC MCP server | architect | [GitHub](https://github.com/Daviidro/ifcopenshell-mcp) |
| R70 | en | Georeference this IFC model using EPSG:4326... Generate a BC3 budget file in Spanish | README prompt for Bonsai MCP | bim_coordinator | [GitHub](https://github.com/JotaDeRodriguez/Bonsai_mcp) |
| R71 | en | how many windows, doors, chimneys, or ramps (glass cleaner, painters ask for largest window and total wall area) | persona-driven non-expert questions | owner_client | [GitHub](https://github.com/ekkodale/IFC-MCP) |
| R72 | en | Qto_*** properties expectations: are Qto_* quantities filled manually or computed by vendors? | who fills Qto sets | civil_infra_engineer | [bSI forum](https://forums.buildingsmart.org/t/6298) |
| R73 | en | asks whether IDS can verify quantities exist in the model; later found she used IfcQuantityLength instead of IfcLengthMeasure as data type | checking quantities with IDS | student_beginner | [bSI forum](https://forums.buildingsmart.org/t/validation-of-quantities-using-ids/5326) |
| R74 | en | wants an IDS that detects whether an IfcWall in IFC2x3 has any quantity set (name unknown) | IDS needs a set name | bim_coordinator | [bSI forum](https://forums.buildingsmart.org/t/5745) |
| R75 | en | contractor needs IFC for cost estimation but we have no BEP or template (ArchiCAD export pain points) | export for estimators without a BEP | architect | [bimcorner.com](https://bimcorner.com/exporting-ifc-from-archicad/) |

## Ready test prompts

All prompts are **synthetic** (written for testing and inspired by the real records named in the last column; not real quotes). They were rewritten to sound like people typing quickly: terse, lowercase, units dropped, tool names as nouns. Difficulty is for the assistant. All assume a model is loaded unless the type says knowledge or how_to.

How estimators actually write these (from the 145 real records): they ask for a table ("as csv", "to excel", "ВОР"), say "net", "per level", "by type", mention the source ("from Qto", "from BaseQuantities") or demand a fallback ("if no Qto, compute from geometry"), and often paste a number that does not match another tool.

| # | Lang | Prompt | Type | Difficulty | Expected behavior (inspired by) |
|---|---|---|---|---|---|
| Q1 | en | net wall area per storey excl openings, csv pls. say which qto source you used | model_task | medium | Group walls by storey; use Qto NetSideArea else compute; export CSV; state source and missing (en-aimcp-s004) |
| Q2 | ru | объём бетона по этажам, только монолит, ВОР в эксель. если в модели нет Qto - скажи прямо | model_task | medium | Filter concrete by material, sum volume per storey, flag elements without Qto, do not hide gaps (ru-aimcp-s011) |
| Q3 | es | dame los ductos por nivel con longitud, área y kilos, solo los de la selección | model_task | medium | Revit selection only; group by level; report method for fittings; say weight source (es-aimcp-s015, es-aimcp-r032) |
| Q4 | de | Wandflächen und Volumen je Geschoss als Liste fürs LV, nur Außenwände. werden Öffnungen abgezogen? bitte angeben | model_task | medium | Filter IsExternal; read Net/Gross; state whether openings are deducted (de-dach-s007) |
| Q5 | en | gross side area = net side area on most walls here, but theres windows in them. are the openings modelled as voids or baked in the mesh? | troubleshooting | hard | Check IfcRelVoidsElement/IfcRelFillsElement; compare gross/net; report walls with equal values despite fills (en-s002, en-gh-ifcos-r002) |
| Q6 | en | why does solibri show 20 m2 and my script 9.8 for the same wall? gross vs net? | troubleshooting | easy | Explain gross/net, openings, exporter differences; suggest checking Qto_WallBaseQuantities (en-qto-s006) |
| Q7 | en | half my elements dont have any quantities after the revit export. which ones, by class? | model_task | medium | Count elements per class with and without IfcElementQuantity; suggest "Export base quantities" (en-qto-s002) |
| Q8 | ru | после выгрузки в ифс нет базовых количеств у половины элементов, какие классы без них? | model_task | medium | Same in Russian; mention Revit setting and exporter version (ru-qto-s010) |
| Q9 | en | exported from revit but the ifc has no Qto sets at all, only pset stuff. which export setting do I need | how_to | easy | Enable base quantities in the IFC setup; mention MVD setups; verify in the file if loaded (en-s016) |
| Q10 | en | gross and net floor area look identical on all my rooms, is that an export bug? check the model | model_task | medium | Compare Gross/NetFloorArea per space, report count of equal values, explain known exporter issue (en-spaces-s002) |
| Q11 | ru | у меня площадь по зонам не сходится с RUS_Area, посчитай по геометрии IfcSpace и покажи где расхождение больше 0.5 м2 | model_task | hard | Compute geometry area; compare with attribute; list over 0.5 m2; label legal-area caveat (ru-habr-dev-s004) |
| Q12 | fr | je dois sortir les métrés pour le DPGF : surfaces de murs nettes des ouvertures par niveau, et le nb de portes par type | model_task | medium | Net wall areas per storey; count IfcDoor by type; flag missing quantities (fr-s012) |
| Q13 | it | mi serve il computo metrico dai muri e solai per piano, con m2 e m3, e dimmi se ci sono elementi senza quantità | model_task | medium | Aggregate by storey; list elements without quantities (it-s015) |
| Q14 | pt-BR | preciso do quantitativo de área de parede e volume de concreto por pavimento pra planilha de orçamento | model_task | medium | Read Qto_Wall/Slab; aggregate by storey; table; note missing (pt-brazil-s005) |
| Q15 | zh | 按楼层统计混凝土墙、板、柱的体积（m3），做成表，算量用；缺工程量的构件单独列出来 | model_task | medium | Group by storey and class; sum NetVolume; separate list of elements lacking quantities (zh-s011, zh-qto-s011) |
| Q16 | ja | 階ごとのコンクリート数量と型枠面積を拾いたいです。梁と柱と壁で分けて出せますか | model_task | hard | Volume and formwork-related surface area by class and storey; explain assumptions for formwork (ja-s013) |
| Q17 | ko | 층별 콘크리트 물량 m3로 정리해줘. 슬래브 벽 기둥 따로 | model_task | medium | Sum NetVolume/GrossVolume by storey and class; flag missing (ko-korea-s006) |
| Q18 | nl | m2 binnenwand per NL-SfB code en aantal deuren met FireRating, naar excel kan? | model_task | medium | Aggregate NetSideArea by classification; count doors with FireRating; export table; list doors without it (nl-dutch-s009, nl-dutch-r011) |
| Q19 | no | trenger mengder: netto areal yttervegger per etasje, uten åpninger | model_task | medium | Sum NetSideArea of external walls by storey; note missing (no-norway-s008) |
| Q20 | es | necesito las mediciones por capítulos (muros, forjados, carpintería) para pasarlas a presupuesto en bc3 | model_task | hard | Group into chapters; offer CSV for BC3 import; state limits of BC3 writing (es-qto-s012) |
| Q21 | de | Mauerwerk-Mengen nach Geschoss ziehen, netto ohne Öffnungen, fürs LV (GAEB) | model_task | medium | Net wall volume/area per storey; table suited to GAEB positions; no rates (de-qto-s013) |
| Q22 | en | total weight of steel beams by profile name pls | model_task | medium | Group IfcBeam by profile; weight from quantity or MassPerLength x length; state source and units (en-tekla-s008, en-gh-ifcos-r006) |
| Q23 | en | pull rebar from the ifc - bar mark, size, length, count and total weight per pier. need it for the bid | model_task | hard | Query IfcReinforcingBar; group by mark/diameter and host; sum length and weight; flag missing quantities (en-us-canada-infra-s007) |
| Q24 | en | I dont trust the slab areas in this model. recompute from geometry and compare with Qto_SlabBaseQuantities, show anything off by more than 2% | model_task | hard | Geometry vs stored area; list outliers with ratios; mention which engine (en-s018) |
| Q25 | en | slab volumes in my cost sheet are 8% off the model. which slabs have no Qto or odd units? | model_task | hard | Compare Qto vs geometry vs sheet if loaded; units; slabs lacking quantities (en-data-s004) |
| Q26 | en | my get_volume numbers are off by 2% on elements at state plane coords. whats going on | how_to | medium | Explain precision loss far from origin; suggest local coordinates (en-us-canada-infra-s012, en-us-canada-infra-r019) |
| Q27 | en | compare rev B and rev C ifc - what changed in slab areas and column counts since the bid set? just give me deltas I can price | model_task | hard | Match by GlobalId; deltas of area and count; caveat about unmatched GUIDs (en-s004) |
| Q28 | en | what are the cut and fill volumes in this model? earthworks elements | model_task | hard | Read Qto_Earthworks Cut/Fill; warn if missing; offer geometry computation; mention known issues (en-qto-s017) |
| Q29 | en | total insulation per system - is it a separate element or merged into the pipe? | model_task | hard | Detect IfcCovering INSULATION vs inside segment geometry; explain unavailability if merged (en-mep-s004) |
| Q30 | en | make a BoQ per storey: slabs m2, walls m2, doors count, as a table I can paste in excel | model_task | medium | Group by storey; correct units; state source of each quantity (en-qto-s004) |
| Q31 | en | create a cost schedule 'Tender', add a cost item per wall type and link the NetVolume quantities | model_task | hard | Write operation: confirm, then create IfcCostSchedule/items, assign elements and NetVolume, report totals; no rates unless given (en-qto-s005) |
| Q32 | en | my cost item total is a bit off from volume x rate, is it rounding? | troubleshooting | medium | Recompute with full precision; explain display rounding; check unit basis and multiple cost values (en-qto-s018, en-qto-r005) |
| Q33 | en | whats the total cost of the walls on level 2? | model_task | medium | Look for IfcCostItem links; if none, say there is no cost data and offer quantities; never invent rates (trap, new; see 5D note in the domain overview) |
| Q34 | en | which elements on level 3 arent linked to any task in the work schedule? need the list before tomorrows 4D review | model_task | medium | Query task assignments, list level-3 products without tasks, grouped by class and name (en-s003) |
| Q35 | pt | quais elementos do pavimento 2 ainda não têm atividade no cronograma? preciso pro 4D da obra | model_task | medium | Same in Portuguese; list by class (pt-s010) |
| Q36 | ko | 공정표랑 연결 안 된 부재 층별로 뽑아줘. 4D 시뮬 돌리기 전에 확인해야돼 | model_task | medium | List elements without task links per storey (ko-s014) |
| Q37 | en | make a work schedule with a task per level (foundation, L1..L5 structure), 5 days each, and link all columns slabs and beams on that level | model_task | hard | Create IfcWorkSchedule and tasks; assign by storey and class; report counts; confirm before writing (en-s017) |
| Q38 | pt-BR | o que mudou da revisão anterior pra essa? preciso saber quais elementos já estão no cronograma 4D e foram alterados | model_task | hard | Diff by GlobalId; intersect changed set with task-assigned elements (pt-guid-s010) |
| Q39 | zh | 机电和土建ifc我要导BIM5D，先帮我按楼层统计下各类构件数量，看有没有楼层对不上的 | model_task | medium | Counts and Qto by storey; flag elements with no storey (zh-revit-export-s006, zh-revit-export-r011) |
| Q40 | es | agrúpame los elementos por nivel y tipo para armar paquetes de obra, solo estructura | model_task | medium | Group structural elements by storey and class/type; table suited to scheduling (es-latam-s015) |
| Q41 | en | i need to move a wall in the 4D sim, demolish it here and build it 3m over. how do i model that task? | how_to | medium | MOVE needs input and output products; duplicate at new location and link both; offer to do it after confirmation (en-osarch-r011) |
| Q42 | en | architects reissued the model. which cost items now point at elements that no longer exist? | model_task | hard | Diff by GlobalId; list cost items assigned to removed elements; mention GUID churn caveat (en-osarch-s011) |
| Q43 | ru | объём бетона по IfcWall и IfcSlab по этажам в эксель, если нет Qto - посчитай по геометрии | model_task | medium | Qto first, geometry fallback; mark which rows used which; units (ru-habr-dev-s010) |
| Q44 | en | which of the 212 doors have no FireRating? count by level | model_task | easy | Query IfcDoor, read Pset_DoorCommon.FireRating, count missing by storey (nl-dutch-r011, adapted) |
| Q45 | en | the model has no rebar. give me rebar kg for the slabs at 100 kg/m3 | model_task | medium | Volume x ratio, state assumption and that rebar is not modelled; return formula (en-struct-r006, new) |
| Q46 | en | bonsai says 34 records calculated but i see nothing in the quantity sets. what did i do wrong | troubleshooting | medium | Ask which tool/version; check that the calculation was run after the last edit and rules match the classes (en-gh-ifcopenshell-r025) |

## Edge cases and traps for MCP testing in this area

1. **Quantity source.** Qto set, ordinary property, attribute (door OverallWidth) or geometry computation give different numbers. The answer must name the source per number; "I used geometry because no Qto exists" is correct, silent substitution is not.
2. **Gross vs net.** The same wall has two areas and two volumes. A prompt that says "wall area" without gross/net needs a stated reading. Net equal to gross on walls with windows is a flag, not a result.
3. **Openings baked into meshes.** No `IfcRelVoidsElement` does not prove there are no openings in the geometry.
4. **Units.** mm vs m, m2 vs m3 vs mm3, area units in a mm project. Exports that dump numbers in model units (the Chinese test log in the data shows thickness 200 and elevations 7200 in a millimetre project) need the unit stated in the answer.
5. **Precision far from origin.** Georeferenced models with coordinates in the millions can give volume errors of a few percent in computed geometry.
6. **Missing is not zero.** A wall without `NetVolume` is "no quantity", not 0 m3; totals must show how many elements were skipped.
7. **Double counting.** Aggregates and their parts, copied or duplicated files in a federation, the same element in a type and as occurrences, linked models counted twice.
8. **Layered elements.** Per-material volumes of a wall cannot be read from one `NetVolume`; derive from layers, thickness and area, and state the assumption.
9. **Material filters.** "Concrete" is a material name in the model's own language and spelling; elements without material assignment drop silently from a filtered total.
10. **Counts vs quantities.** "How many doors" is a count by type; "door area" needs width x height or a Qto.
11. **Stale values.** Stored quantities do not update after geometry edits unless the tool recalculates; an MCP that edits geometry and then reports totals must recompute or warn.
12. **No cost data in the file.** "Total cost of the walls" has no answer without cost items; rates, currency and price lists must come from the user. Never fabricate a unit price.
13. **Rounding.** Display rounding vs full precision; a sum of rounded rows differs from the rounded sum.
14. **Cost schedule writes.** Creating or changing a schedule, cost items or assignments is a write action: confirm; avoid duplicates on retry (the data has an idempotency proposal for timeout retries).
15. **Product resource off-by-one and UnitBasis traps.** Check sums by hand when a tool reports totals for resources and multiple cost values.
16. **4D logic.** IFC stores dates and sequence links but does not recalculate; "shift this task and tell me what moves" needs an engine, else the answer must say it only reads. Calendars, lag and float are easy to get wrong.
17. **Unscheduled and unattached.** Elements with no task, tasks with no elements, tasks nested but not sequenced (`IfcRelNests` vs `IfcRelSequence`).
18. **Phasing.** Demolished or temporary elements exist only if the exporter wrote the phase; existing-versus-new splits are often missing.
19. **Revisions.** Priced or scheduled elements change GlobalIds on re-export; the diff must report overlap and fall back to heuristics, labelled.
20. **National formats.** BC3, GAEB, NRM, MasterFormat, NL-SfB, GB/T 51269: the assistant should say what it can produce (table, CSV) and what it cannot guarantee (a valid BC3/GAEB file).
21. **Legal areas.** Net/gross floor area as defined by a regulation or registry is not what a geometry sum gives; the maintainers of an open-source engine deliberately skip spaces for this reason.
22. **Infrastructure.** IFC4x3 earthworks, alignments and linear quantities (cut/fill, km of track) have thin tool support; "unsupported" is a valid answer.
23. **Selection scope.** "Only my selection" or "only Level 2" in a Revit-driven server must be honoured; whole-model totals are a failure.
24. **Language.** Prompts in Russian, Chinese, Japanese etc. use local terms (ВОР, 算量, 積算, metrado, computo) and local units; replies should follow the language but keep identifiers.

## Related docs

- [Properties, quantities and property sets (Qto_ base quantities, gross vs net)](../../01_ifc_basics/05_properties_quantities_psets.md)
- [Domain overviews: 4D schedule, 5D cost, MEP, structural, infrastructure](../../01_ifc_basics/08_domains_mep_structural_infra_4d5d_fm.md)
- [Geometry, placement, coordinates and units](../../01_ifc_basics/06_geometry_placement_coordinates_units.md)
- [Materials, classification, types and styles](../../01_ifc_basics/07_materials_classification_types_styles.md)
- [Spatial structure and relationships (storeys, containment)](../../01_ifc_basics/04_spatial_structure_and_relationships.md)
- [Revit IFC export reference (Export base quantities, mapping)](../../03_software/revit/ifc_export_reference.md)
- [Authoring tools and their IFC export](../../03_software/authoring_tools_ifc.md)
- [Open-source libraries and toolkits](../../04_open_source/libraries_and_toolkits.md) and [MCP servers and AI tools](../../04_open_source/mcp_servers_and_ai_tools.md)
- [Multilingual glossary](../../08_glossary/glossary_multilingual.md) and [abbreviations](../../08_glossary/abbreviations.md)
- Sibling topic files: [coordinates, georeferencing, units and levels](coordinates_georef_units_levels.md), [versions, MVD, encoding and GUID changes](versions_mvd_encoding_guid.md), [validation, IDS and model checking](validation_ids_model_checking.md), [MEP, structural and rebar](mep_structural_rebar.md), [import and interoperability](import_and_interoperability.md)
- Companion topic file: [Coordination, clash detection, BCF and CDE](coordination_clash_bcf_cde.md)
