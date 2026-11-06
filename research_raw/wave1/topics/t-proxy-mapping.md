# Class mapping and IfcBuildingElementProxy (why elements export as proxies; IfcExportAs; mapping tables)
Cell: t-proxy-mapping · Languages: English (real sources); ru, zh, es, pt, de, fr, ja, ko, it only as synthetic prompts · Collected: 2026-11-06 · Records: 41 real / 17 synthetic · Communities covered: GitHub (Autodesk/revit-ifc, IfcOpenShell, SketchUp-IFC-Manager, buildingSMART IFC4.x-development and bSDD), OSArch community

## Top themes (ranked by frequency)
- Specific Revit element types always or unexpectedly export as IfcBuildingElementProxy (wall sweeps, fascias, slab edges, nested sweeps, curtain wall profiles).
- IfcExportAs / IfcExportType parameters ignored by certain categories (curtain walls, ceilings, walls to IfcCovering, structural column assemblies).
- Revit 2023 replaced the shared IfcExportAs parameter with built-in "Export to IFC As" / "IFC Predefined Type"; old workflows (key schedules, API, groups) broke.
- Confusion over the precedence of category mapping, subcategory mapping, type override and instance override.
- PredefinedType problems: NOTDEFINED forced, custom or USERDEFINED types not exported, ObjectType ignored.
- Mapping table management: storage inside the model (Revit 2025 DataStorage), no external reference, mixing IFC2x3 and IFC4.3 classes, localized "Not exported" import bug.
- Import direction: IFC imported as Generic Models, class-to-category import tables, Link IFC creating generic models for openings and spaces.
- Auto-generated proxy types that cannot be edited, leaving data-less proxies.
- Quantities and psets that do not follow the overridden class (Qto_WallBaseQuantities on a furniture override, empty proxy Qto).
- QA of proxies: IDS rules and Solibri checks that fail when proxies exist; consultants delivering wrong classes despite instructions.
- Reclassifying proxies in open-source tools (Bonsai types, splitting proxies).
- Other exporters producing stray proxies (SketchUp IFC Manager).

## What people want (the goals behind the questions)
- Zero or minimal IfcBuildingElementProxy in deliverables, because clients, Solibri rules and IDS reject them.
- Predictable, documented rules for which IFC class Revit writes, and a way to see the intended class (IfcExportAs value) inside the exported file.
- Override any category or system family (sweeps, ceilings, curtain wall parts) with the correct class and PredefinedType.
- Reusable, version-controlled mapping tables across many models and for automation (Design Automation, API, Dynamo).
- A dropdown instead of free-typed class names to avoid typos.
- Bulk reclassification and audit of proxies in an already exported model, by name, category or geometry.

## How people write here
- GitHub issue style: short title with prefix (PR:, ENH:, INQ:), then Problem Description, Revit Version, IFC for Revit Addon Version, Windows Version, screenshots. Typical length is 3-10 lines.
- Heavy jargon with exact tokens: IfcExportAs, IfcExportType, "mapping table", "NOTDEFINED", "user defined parameter mapping file", "category mapping".
- Frustration is dry and understated; occasional strong lines: "makes us apologize to the customers every time".
- Client-facing framing: "when a client asks why the IFC classes are wrong".
- Misspellings seen: "IfcBuildingElementProxi", "IfcCoveting.CEILING", "IFC4 RV" shorthand for Reference View, "BBIM" for BlenderBIM.
- Short fragments: "Anyone?", "Any updates on this?", "no way to override the export IFC class".
- Context usually given: Revit version, exporter version, IFC schema and view (CV2.0, RV, DTV); context often omitted: sample file, which category.
- Synthetic prompts mimic chat-style brevity in each language, e.g. ru "глянь сколько в модели проксей", de "bitte als IfcColumn umklassifizieren", zh "一堆IfcBuildingElementProxy".

## Local ecosystem
- Autodesk revit-ifc open-source exporter: https://github.com/Autodesk/revit-ifc (issues tracked internally as REVIT-nnnnnn Jira items).
- buildingSMART IFC4.x development and bSDD: https://github.com/buildingSMART/IFC4.x-development , https://github.com/buildingSMART/bSDD
- IfcOpenShell / Bonsai (open source): https://github.com/IfcOpenShell/IfcOpenShell
- OSArch community: https://community.osarch.org (documents Revit and IFC classes rules in its wiki)
- Solibri, IfcTester / IDS for proxy audits.
- SketchUp IFC Manager: https://github.com/BIM-Tools/SketchUp-IFC-Manager
- No government or regulation sources found for this cell.

## Notable sources
- https://github.com/Autodesk/revit-ifc/issues/229 wall sweeps always proxy
- https://github.com/Autodesk/revit-ifc/issues/481 fascias and wall sweeps cannot override proxy
- https://github.com/Autodesk/revit-ifc/issues/541 Revit 2023 IfcExportAs ignored
- https://github.com/Autodesk/revit-ifc/issues/614 Revit 2023.1 no longer recognizes IfcExportAs
- https://github.com/Autodesk/revit-ifc/issues/906 classes and predefined types ignored, proxy NOTDEFINED
- https://github.com/Autodesk/revit-ifc/issues/676 auto-generated proxy types
- https://github.com/Autodesk/revit-ifc/issues/171 curtain walls and IfcExportAs
- https://github.com/Autodesk/revit-ifc/issues/155 walls to IfcCoveringType
- https://github.com/Autodesk/revit-ifc/issues/392 IfcExportAs not in psets, eight class rules
- https://github.com/Autodesk/revit-ifc/issues/391 duplicate IfcExportAs parameters
- https://github.com/Autodesk/revit-ifc/issues/183 data should not rely on user input
- https://github.com/Autodesk/revit-ifc/issues/248 subcategories in mapping table
- https://github.com/Autodesk/revit-ifc/issues/775 subcategory mapping purpose
- https://github.com/Autodesk/revit-ifc/issues/840 external class mapping
- https://github.com/Autodesk/revit-ifc/issues/876 mapping and IFC version consistency
- https://github.com/Autodesk/revit-ifc/issues/798 import class mapping tables
- https://github.com/Autodesk/revit-ifc/issues/859 localized Not exported string
- https://github.com/Autodesk/revit-ifc/issues/684 custom predefined type
- https://github.com/Autodesk/revit-ifc/issues/497 quantities despite override
- https://github.com/Autodesk/revit-ifc/issues/571 imported walls as generic models
- https://github.com/Autodesk/revit-ifc/issues/398 nested wall sweeps
- https://community.osarch.org/discussion/3303/ids-check-for-ifcbuildingelementproxy-question IDS proxy check
- https://community.osarch.org/discussion/3598/add-subtypes reclassifying proxies in Bonsai
- https://community.osarch.org/discussion/comment/3574 roof from Revit
- https://github.com/IfcOpenShell/IfcOpenShell/issues/4740 proxy quantities in BBIM
- https://github.com/BIM-Tools/SketchUp-IFC-Manager/issues/63 stray proxies from SketchUp

## Gaps
- The WebSearch budget was exhausted before any search ran (all four attempted calls returned "budget used up"), so no search with allowed_domains was possible. All real records come from the GitHub CLI and direct page fetches.
- No native-language real records (ru, zh, es, pt, de, fr, ja, ko, it): dwg.ru, qiita, cnblogs search URLs returned 404 or empty; csdn, zhihu and similar not reachable without search. Non-English content exists only as synthetic prompts; a follow-up pass with search is needed.
- Not accessible: forums.autodesk.com (403 on direct fetch), stackoverflow.com (blocked in fetch), forums.buildingsmart.org (search page unusable), reddit (no search), wiki.osarch.org Revit and IFC classes page (404 at guessed URL).
- Records 36-41 are title-only (snippet evidence). OSArch years are approximate from thread order. No suspicious sites encountered.
