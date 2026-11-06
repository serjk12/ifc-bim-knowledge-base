# Quantity takeoff and cost estimation (5D) from IFC

Cell: t-qto-cost · Languages: English (real sources); synthetic prompts also in ru, zh, es, de, pt, ja, fr · Collected: 2026-11-06 · Records: 37 real / 18 synthetic · Communities covered: GitHub issues (IfcOpenShell/Bonsai, Autodesk revit-ifc, Speckle, xBIM, buildingSMART), community.osarch.org

Important limitation: the WebSearch budget was exhausted at the start of the session, so no keyword web searches ran. Evidence comes from GitHub CLI issue search, direct page fetches and the site-internal search of OSArch. No native-language (ru/zh/es/pt/de/fr/ja/ko/it) community pages could be reached; all real records are English. Synthetic non-English prompts are translations of English patterns, not observed phrasing.

## Top themes (ranked by frequency)
- Quantities wrong or different between tools (IfcOpenShell vs Blender engine vs Solibri), usually Gross vs Net with openings.
- Revit IFC export lacks base quantities for some classes (storey, space, ramps, proxies, IFC2x3 custom Qto).
- Width/Height/Depth/Length swapped in Qto_*BaseQuantities (doors, slabs, footings).
- QTO is not live: users forget to re-run the calculation (Shift+Q) after editing geometry.
- Cost schedule math surprises in Bonsai 5D (rounding, unit basis, crew/resource totals, product resources).
- Getting a BoQ to Excel/CSV/PDF with links back to model elements.
- Missing quantity types: weight/density, per-layer volumes (LCA), earthworks, spaces.
- IFC4x3 infrastructure quantities (earthworks cut/fill) not supported or mis-defined.
- Tool discovery: open-source QTO/BOQ tools (StructBOQ, OpenConstructionERP, Plan Measure, ifc5d).
- Filtering/grouping takeoff by storey/location in spreadsheet/ifc5d rules.
- National BoQ formats (BC3/FIEBDC, GAEB, NRM, MasterFormat) as export targets.
- Fallback hierarchy: BaseQuantities, then Psets, then geometry computation.

## What people want
- Trustworthy numbers that match a reference tool, with an explanation when they differ.
- One-click grouped takeoff by type, storey, material, exportable to spreadsheet or tender format.
- Quantities that stay linked to cost items and update when the model changes.
- Weight, layer-level volumes and net/gross variants for costing and LCA.
- Clear statement of which quantity source was used (Qto, Pset or geometry).

## How people write here
- Bug reports in GitHub: structured templates, version numbers, attached IFC and screenshots; some are title-only with images ("Problems with Quantity take offs.").
- Forum posts (OSArch) are casual, show-and-tell, often introduce own tool and ask for "honest feedback".
- Beginners are polite and self-deprecating: "what am I doing wrong?", "knew I was doing something wrong".
- Estimators give arithmetic to prove a point: "$100/U x 5U = $500", "9.80815 m2 vs 20.08 m2".
- Jargon: QTO, BoQ, takeoff, Qto_WallBaseQuantities, NetVolume, GrossSideArea, SoR (schedule of rates), 5D, ifc5d, Shift-Q.
- Misspellings seen: "qantities" for quantities; "take offs" as plural noun; "Qto" vs "QTO" inconsistently.
- Feature requests end with thanks: "thanks for your efforts".
- Synthetic non-English prompts assume terse, lowercase, mixed terms (BoQ, Qto, GAEB, BC3).

## Local ecosystem
- IfcOpenShell / Bonsai (ifc5d module, cost and QTO rules): https://github.com/IfcOpenShell/IfcOpenShell
- Autodesk IFC for Revit exporter (Jira-tracked REVIT-xxxx issues): https://github.com/Autodesk/revit-ifc
- buildingSMART IFC4.x development (standard Qto proposals): https://github.com/buildingSMART/IFC4.x-development
- OSArch community: https://community.osarch.org
- OpenConstructionERP (cad2data, CWICR cost catalogue; BC3, GAEB, NRM, MasterFormat): described in the OSArch thread below
- Open Planner Studio (IFC4.3 scheduling, no cost/QTO yet): https://community.osarch.org/discussion/3738/open-planner-studio-open-source-construction-scheduler-with-ifc-4-3-as-its-native-file-format
- Solibri used as reference for quantity comparison; Speckle material quantities: https://github.com/specklesystems/speckle-sharp
- xBIM toolkit: https://github.com/xBimTeam/XbimEssentials
- Goifc reader and ifc-lite viewer: https://github.com/blox-eng/goifc , https://github.com/LTplus-AG/ifc-lite
- Small GitHub QTO scripts: https://github.com/Arri-1/ifc-quantity-takeoff

## Notable sources
- https://github.com/IfcOpenShell/IfcOpenShell/issues/9235 Gross==Net side area vs Solibri
- https://github.com/IfcOpenShell/IfcOpenShell/issues/5349 mesh window area differs between engines
- https://github.com/IfcOpenShell/IfcOpenShell/issues/4964 beginner budget with wrong quantities
- https://github.com/IfcOpenShell/IfcOpenShell/issues/6401 cost calculation rounding
- https://github.com/IfcOpenShell/IfcOpenShell/issues/2397 automating quantities
- https://github.com/IfcOpenShell/IfcOpenShell/issues/6325 earthworks quantities IFC4x3
- https://github.com/IfcOpenShell/IfcOpenShell/issues/5706 crew resource discrepancy
- https://github.com/IfcOpenShell/IfcOpenShell/issues/7762 CSV BoQ export with element linking
- https://github.com/IfcOpenShell/IfcOpenShell/issues/5155 product resource counts extra
- https://github.com/IfcOpenShell/IfcOpenShell/issues/8625 UnitBasis total cost bug
- https://github.com/IfcOpenShell/IfcOpenShell/issues/6570 improving ifc5d
- https://github.com/IfcOpenShell/IfcOpenShell/issues/6305 footing quantities table
- https://github.com/IfcOpenShell/IfcOpenShell/issues/9376 earthworks cut UndisturbedVolume
- https://github.com/IfcOpenShell/IfcOpenShell/issues/8570 ifc5d IfcSpace null formulas
- https://github.com/IfcOpenShell/IfcOpenShell/issues/7371 ifc5d location filter
- https://github.com/Autodesk/revit-ifc/issues/144 missing quantities
- https://github.com/Autodesk/revit-ifc/issues/141 wall base quantities wrong
- https://github.com/Autodesk/revit-ifc/issues/688 quantity parameters in pset mapping
- https://github.com/Autodesk/revit-ifc/issues/753 layer quantities for LCA
- https://github.com/Autodesk/revit-ifc/issues/545 weight quantities from Revit
- https://github.com/Autodesk/revit-ifc/issues/594 custom base quantities in IFC2x3
- https://github.com/Autodesk/revit-ifc/issues/479 storey without base quantities
- https://community.osarch.org/discussion/996/automating-cost-values-and-cost-quantities
- https://community.osarch.org/discussion/2963/small-script-to-print-pricedbillofquantities-to-pdf
- https://community.osarch.org/discussion/3437/openconstructionerp-qto-boq-and-ai-estimating-with-ifc-and-revit
- https://community.osarch.org/discussion/3418/free-ifc-concrete-boq-looking-for-test-files-and-honest-feedback
- https://community.osarch.org/discussion/3576/plan-measure-open-source-pdf-takeoff-tool-looking-for-aec-feedback
- https://community.osarch.org/discussion/comment/28629#Comment_28629 door width Qto bug

## Gaps
- No general web search possible (budget exhausted): no Autodesk forums, buildingSMART forum, Graphisoft, Stack Overflow (WebFetch blocked), Reddit threads.
- No native-language communities reached: dwg.ru search 404, cnblogs 404, Graphisoft 403, Autodesk forum 403, qiita search returned only an unrelated article, buildingSMART forum search blocked. Russian, Chinese, Spanish, Portuguese, German, French, Japanese, Korean and Italian real posts are missing; their phrasing in this file is synthetic only.
- 8 real records are snippet-only (title from search listing); the OSArch comment years are inferred from listing order.
- No suspicious or pirated sites were encountered.
