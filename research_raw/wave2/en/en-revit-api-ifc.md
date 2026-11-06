# Revit API and Design Automation: programmatic IFC export/import questions
Cell: en-revit-api-ifc · Languages: English · Collected: 2026-11-06 · Records: 37 real / 15 synthetic · Communities covered: GitHub Autodesk/revit-ifc issue tracker (main source), revitapidocs.com, a Design Automation scheduler repo README

## Top themes (ranked by frequency, 8-15 bullets, one line each)
- Passing export settings through the API (IFCExportOptions.AddOption vs IFCExportConfiguration vs JSON settings); many options silently ignored via AddOption.
- Coordinate base / SitePlacement set from code not taking effect, or changing the project location as a side effect.
- Linked files: ExportLinkedFiles and "separate IFCs" not honored from add-ins, cloud (BIM 360/ACC) links failing.
- Saved export configurations not visible to scripts (Dynamo, Python, Batch Processor) until the dialog is opened once.
- Design Automation for Revit: crashes (curtain walls IFC4), engine/version rules, time limits, settings JSON, view filters.
- Class mapping (IfcExportAs, category tables, DataStorage in 2025) in batch workflows; duplicate or ignored parameters.
- Export differs between UI and API (IFC4 Reference View geometry, file size, MVD header values).
- Linking/importing IFC by API: bulk linking, hangs, empty links, no documented IFC-to-category mapping.
- Validation against buildingSMART service: header MVD, deprecated entities, schema errors.
- Property sets: user-defined pset files, built-in parameters overriding shared ones, Category property missing.
- Filtering by view (FilterViewId plus VisibleElementsOfCurrentView) producing empty or whole-model files.
- Stability and large models: unrecoverable errors, crashes, no progress feedback.
- GUID determinism and tracking across exports.

## What people want (the goals behind the questions)
- Fully unattended, repeatable IFC export (batch, nightly, cloud) that matches the manual UI result exactly.
- One central place for export settings and class mapping shared across many models.
- Reliable error reporting and partial output instead of silent failures or crashes.
- Programmatic control of coordinate base, linked-model handling, header metadata, classification fields.
- Bulk linking and checking of incoming IFC, with mapping to Revit categories under their control.
- IFC that passes the bSI validation service.

## How people write here (register, typical length, jargon/slang with translations, misspellings of terms, code-switching, openers/closers, what context they give or omit, emotional tone) with short illustrative fragments (max 12 words each)
- Register: technical, code-first; often a pasted C#, Python or VB snippet with little prose. Issue templates (PR/ENH/INQ) impose Problem Description, Revit version, add-in version.
- Length: short for how-to questions, long structured for enhancement requests.
- Jargon: "add-in", "appbundle", "work item" (Design Automation job), "export setup/config", "mapping table", "IfcExportAs", "proxy", "CV2.0", "RV/DTV".
- Typos and odd phrasing: "IFC export trough API", "doesn't have any affect", "Curren project location".
- Openers/closers: "Thanks for the work you are doing!", "Please provide any solution", "Bug?".
- Context given: Revit year, exporter add-in version, code; often omitted: model sample, journal files (maintainers ask for them).
- Tone: frustrated when UI works but API does not; polite and exploratory in INQ items.
- Fragments: "Am I missing a reference?"; "works via UI, ignored from my addin"; "Maybe I'm doing something wrong..."

## Local ecosystem (official/government bodies, regulations and standards, local software, enthusiasts/educators, open-source projects encountered, with URLs)
- Autodesk revit-ifc (open-source IFC export/Link IFC, UI): https://github.com/Autodesk/revit-ifc
- Revit API docs mirror: https://www.revitapidocs.com/
- Design Automation scheduler sample/fork: https://github.com/libnypacheco/revit-design-automation-ifc-scheduler
- buildingSMART validation service: https://validate.buildingsmart.org/dashboard
- Dynamo, Revit Batch Processor, pyRevit-style tooling used for mass export; IfcOpenShell as a comparison/test producer.
- Autodesk Platform Services (APS) Design Automation for Revit; ACC/BIM 360 cloud models.

## Notable sources (15-30 best URLs, one line each)
- https://github.com/Autodesk/revit-ifc/issues/411 - empty IFC with FilterViewId from add-in
- https://github.com/Autodesk/revit-ifc/issues/761 - coordinate base through API, JSON config advice
- https://github.com/Autodesk/revit-ifc/issues/820 - SitePlacement set_SitePlacement not found
- https://github.com/Autodesk/revit-ifc/issues/781 - ExportLinkedFiles ignored from custom add-in
- https://github.com/Autodesk/revit-ifc/issues/222 - ExportLinkedFiles has no effect
- https://github.com/Autodesk/revit-ifc/issues/540 - export configs not accessible until dialog opened
- https://github.com/Autodesk/revit-ifc/issues/93 - AddSavedConfigurations returns null
- https://github.com/Autodesk/revit-ifc/issues/992 - Design Automation IFC4 curtain wall crash
- https://github.com/Autodesk/revit-ifc/issues/798 - import class mapping tables, DA4R category table
- https://github.com/Autodesk/revit-ifc/issues/840 - external export class mapping request
- https://github.com/Autodesk/revit-ifc/issues/380 - linking IFC via API in bulk
- https://github.com/Autodesk/revit-ifc/issues/826 - IfcTemplate/mapping for import from code
- https://github.com/Autodesk/revit-ifc/issues/778 - import mapping documentation
- https://github.com/Autodesk/revit-ifc/issues/808 - ExporterIFC object not obtainable
- https://github.com/Autodesk/revit-ifc/issues/397 - IFC4RV via API differs from UI
- https://github.com/Autodesk/revit-ifc/issues/740 - project location changed by JSON export
- https://github.com/Autodesk/revit-ifc/issues/1011 - bSI validation, MVD header
- https://github.com/Autodesk/revit-ifc/issues/951 - Link IFC hangs
- https://github.com/Autodesk/revit-ifc/issues/368 - cloud linked model export fails
- https://github.com/Autodesk/revit-ifc/issues/541 - IfcExportAs ignored in 2023
- https://github.com/Autodesk/revit-ifc/issues/960 - Category in user-defined pset
- https://www.revitapidocs.com/2024/7efa4eb3-8d94-b8e7-f608-3dbae751331d.htm - Document.Export reference
- https://github.com/libnypacheco/revit-design-automation-ifc-scheduler - DA export limits

## Gaps (what you could not access or find; suspicious sites skipped)
- The WebSearch budget for the turn was exhausted before any search ran, so no discovery by search was possible; sources came from GitHub CLI and direct fetches.
- forums.autodesk.com returned 403; stackoverflow.com is blocked for fetching; thebuildingcoder.typepad.com redirected to a hosting vendor (Typepad shutdown); aps.autodesk.com pages returned navigation only; forum.dynamobim.com search was not usable.
- So Revit API forum, StackOverflow, Building Coder and APS blog voices are missing; the cell is dominated by GitHub issue phrasing (developers and BIM managers) and is thin on forum-style language.
- Real record count (37) is within the target; counts of Design Automation specific user threads are low (3 items).
- No suspicious sites encountered. Note: a scratchpad script name collision with another agent caused one unrelated output (en-anz.jsonl) to be rewritten with that agent's own script, no content change intended.
