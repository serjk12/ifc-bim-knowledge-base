# Vendor knowledge bases: known IFC issues (Autodesk, Graphisoft, Tekla, Bentley, Nemetschek, Solibri)
Cell: en-vendor-kb · Languages: English · Collected: 2026-11-06 · Records: 28 real / 16 synthetic · Communities covered: Autodesk revit-ifc GitHub tracker (vendor-run known-issues list, with vendor staff replies), one Tekla help page. All other vendor KBs were inaccessible (see Gaps).

## Top themes (ranked by frequency)
- Revit IFC exporter regressions between add-in builds (25.x, 26.x, 27.x): "worked in the old version, broken in the new one".
- Geometry displaced or wrong after export: joins, openings/voids, sloped floors, sweeps, hollow steel sections, assemblies.
- Link IFC vs Open IFC differences and bugs: Z offset, hangs, IfcSpace not becoming Rooms, in-place families.
- Coordinates, project north and base point problems on import and link.
- Property set export: custom parameters not written, name clashes with built-ins, Pset.Property naming.
- Class mapping and PredefinedType export (beams, columns, IfcFooting, civil elements).
- Validation failures in the buildingSMART Validation Service even though Revit opens the file.
- Units and quantities errors (feet/304.8, floor quantities copied to every part).
- IfcSpace/room geometry shifted or wrong height.
- IFC4x3 and MVD header correctness (Reference View vs Coordination View).
- Automation: batch export via Dynamo / Design Automation, config access, crashes in the cloud.
- Feature requests: ceiling grids, light sources, IDS checks inside Revit.

## What people want (the goals behind the questions)
- Export that reproduces Revit geometry and data faithfully, with no regressions on each add-in update.
- Round-tripping: bring Archicad/Tekla IFC into Revit with correct position, rooms, categories.
- Files that pass validation (bSI service, Solibri, viewers) before delivery.
- Reliable property set mapping so that client requirements (Psets, QTO, classification) are met.
- Scriptable, headless export for batches and cloud pipelines.
- Official acknowledgement: a Jira number, a workaround, or a backported fix.

## How people write here
Bug-report register, usually in English by non-native speakers (Dutch, Czech, German, Spanish, Portuguese hints). Titles are tagged by the repo template (PR:, ENH:, INQ:, BUG:). Reports are medium length, structured (description, version, add-in version, Windows version), with screenshots and attached sample files. People cite exact build numbers and compare "worked in 2024, broken in 2025-27". Tone: factual, mildly frustrated; polite openers ("Hi Revit IFC team") and thanks are common.
- "worked in Revit 2024, present in 2025-27"
- "Link IFC only hangs; terminate the Revit process"
- "Could a maintainer please change the label to bug?"
- Jargon: Open IFC / Link IFC, .ifc.rvt, mapping table, Pset, proxy, Export As, in-place family, base point.
- Missing context: often no model file shared ("can't share the file"), vendor then asks for a repro.

## Local ecosystem
- Autodesk revit-ifc open-source add-in and tracker: https://github.com/Autodesk/revit-ifc (staff reply, mirror issues into internal Jira IDs like REVIT-259235).
- buildingSMART IFC Validation Service: https://validate.buildingsmart.org/dashboard
- BIM Vision (free IFC viewer), Solibri, Tekla Structures (IFC 2x3, 4, 4.3 supported per Tekla docs), Archicad (source of many imported IFCs), Dynamo and Revit Batch Processor for automation, Autodesk Platform Services Design Automation.
- IDS (Information Delivery Specification) appears as a feature request (#902).
- Tekla IFC overview: https://support.tekla.com/doc/tekla-structures/2024/int_ifc_export
- Solibri Help Center: https://help.solibri.com/hc/en-us (not readable by the fetcher).

## Notable sources
- https://github.com/Autodesk/revit-ifc/issues/1021 export unrecoverable error 26.4.x
- https://github.com/Autodesk/revit-ifc/issues/1020 Yes/No parameter AboveGround not exported
- https://github.com/Autodesk/revit-ifc/issues/1019 windows outside wall on import
- https://github.com/Autodesk/revit-ifc/issues/1018 2D annotation shifts doors/windows
- https://github.com/Autodesk/revit-ifc/issues/1015 beam system spacing feet/304.8
- https://github.com/Autodesk/revit-ifc/issues/1014 joined mass wall opening lost
- https://github.com/Autodesk/revit-ifc/issues/1013 Reference View header label
- https://github.com/Autodesk/revit-ifc/issues/1012 ceiling grids export
- https://github.com/Autodesk/revit-ifc/issues/1010 hollow sections corrupt
- https://github.com/Autodesk/revit-ifc/issues/1004 sloped floor footprint
- https://github.com/Autodesk/revit-ifc/issues/1001 joins regression Revit 2026
- https://github.com/Autodesk/revit-ifc/issues/992 curtain wall crash on Design Automation
- https://github.com/Autodesk/revit-ifc/issues/990 Link IFC Z coordinate
- https://github.com/Autodesk/revit-ifc/issues/989 mapping ignores certain built-ins
- https://github.com/Autodesk/revit-ifc/issues/964 invalid PredefinedType IFC4x3
- https://github.com/Autodesk/revit-ifc/issues/952 predefined types stop beams/columns exporting
- https://github.com/Autodesk/revit-ifc/issues/951 Link IFC hang
- https://github.com/Autodesk/revit-ifc/issues/947 fails bSI validation (deep boolean tree)
- https://github.com/Autodesk/revit-ifc/issues/924 room geometry shifted
- https://github.com/Autodesk/revit-ifc/issues/710 project north inconsistency
- https://github.com/Autodesk/revit-ifc/issues/540 programmatic export configurations
- https://github.com/Autodesk/revit-ifc/issues/246 floor quantities
- https://github.com/Autodesk/revit-ifc/issues/223 Link vs Open
- https://github.com/Autodesk/revit-ifc/issues/15 IfcSpace to Room on Link
- https://github.com/Autodesk/revit-ifc/issues/902 IDS auditing request

## Gaps
- WebSearch budget was exhausted before any search ran (0 searches succeeded), so no discovery via search engines; only direct fetches and the gh CLI were possible. Total real tool calls fewer than the 20+ target for search.
- Blocked or unreadable: autodesk.com/support (403), forums.autodesk.com (403), community.graphisoft.com (403), help.solibri.com (403), community.solibri.com (DNS failure), help.graphisoft.com and support.tekla.com article URLs tried (404 / no listing). No Bentley or Nemetschek (Allplan, Vectorworks) pages were reached.
- Hence all 28 real records come from one source (Autodesk revit-ifc GitHub issues), skewed to Revit; Archicad, Tekla, Bentley, Solibri vendor KB phrasing is not covered. Recommend rerun with search budget.
- No suspicious or pirated sites encountered.
- Poster names are omitted; vendor-internal Jira IDs only quoted in summaries.
