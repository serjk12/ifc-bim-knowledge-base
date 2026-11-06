# Autodesk Community: Revit IFC export problems
Cell: en-autodesk-revit-export · Languages: English · Collected: 2026-11-06 · Records: 44 real / 17 synthetic · Communities covered: Autodesk Community forums (Revit Architecture, Structure, MEP, API, Ideas), Autodesk help KB, GitHub Autodesk/revit-ifc issues

## Top themes (ranked by frequency, 8-15 bullets, one line each)
- Property sets and parameters missing from IFC: user-defined pset txt, shared/project parameters, duplicates, type vs instance.
- IfcExportAs / IFC class mapping: elements become IfcBuildingElementProxy, system families ignore the parameter, Revit 2023 built-in "Export to IFC As" replacing it.
- Revit 2027 Parameter Mapping GUI replacing pset.txt, with missing project parameters and empty lists.
- Shared coordinates, project base point vs survey point, wrong elevation or position after export or re-link.
- Rooms and IfcSpace: missing spaces, wrong storey or elevation, phase selection, excluding Areas and Rooms.
- Wrong IfcBuildingStorey assignment and level setup (building story flag, same-elevation levels).
- Curtain walls: panels and mullions hierarchy, ghost mullions, single IfcCurtainWall aggregate, nested shared families.
- Crashes, hangs and huge files (trusses, flex duct, add-in conflicts, update regressions).
- IFC version choice: 2x3 CV2.0 vs IFC4 Reference View vs IFC4x3 bugs (space boundaries, door errors).
- MEP class mapping (IfcFlowSegment in 2x3 vs duct/pipe segments in IFC4) and lost fitting materials.
- Base quantities missing or mislabeled (Net vs Gross), schedules as property sets.
- Colors and materials lost (view filter overrides, appearance).
- Exporting subsets: linked models, selected elements, split by level, multiple buildings in one project.
- Revit API / Dynamo automation of IFC export (IFCExportOptions, empty output, GUIDs).
- Classification (Uniformat default, Uniclass/BB-SfB overrides), stairs/railings, rebar sets, structural connections.

## What people want (the goals behind the questions)
- Make Revit categories and special elements land in the correct IFC class without hand-editing each family.
- Get custom data (company parameters, classification, fire rating, room data) reliably into psets for clients' EIR.
- Hand over a clean coordination model: right location, right storeys, no ghost geometry, reasonable size.
- Control scope: leave out Areas, rooms, links, other buildings; export parts of a model.
- Stable, scriptable, repeatable export (API/Dynamo, saved setups) that does not break between Revit versions.
- Autodesk acknowledgement and fixes for regressions (Revit 2023 parameters, 2027 GUI, rooms elevation).

## How people write here (register, typical length, jargon/slang with translations, misspellings of terms, code-switching, openers/closers, what context they give or omit, emotional tone) with short illustrative fragments (max 12 words each)
- Titles are short, symptom-first, often copying UI labels: "IfcExportAs Parameter doesn't work", "IFC export issue".
- Forum titles carry the Revit year and often "Solved:" prefix added by the board; exclamation marks when urgent ("crashes every time I export IFC!!!").
- Bodies are medium length: version, what was tried, screenshot; many omit exporter version and IFC schema.
- Jargon: proxy (IfcBuildingElementProxy), IfcExportAs, pset, mapping table, CV2.0, RV (Reference View), base point/survey point, "ghost mullions".
- Writers are frequently non-native English speakers (Europe), plain grammar, sometimes capitalised words ("IFC EXPORT APPEARS IN DIFFERENT COLOUR").
- GitHub issues use the template (Problem Description, Revit Version, Windows Version) and are terse and technical.
- Typical tone: frustrated but polite; no greeting; ask "why" and "is it possible to".
- Fragments: "Slab edges still export as proxy"; "Is it possible to exclude areas"; "mapping parameters severely lacking".

## Local ecosystem (official/government bodies, regulations and standards, local software, enthusiasts/educators, open-source projects encountered, with URLs)
- Autodesk Revit IFC exporter open source: https://github.com/Autodesk/revit-ifc
- Autodesk Revit help / KB: https://help.autodesk.com
- Revit Ideas board: https://forums.autodesk.com/t5/revit-ideas/idb-p/revit-ideas-en
- Revit API forum and The Building Coder (developer community): https://forums.autodesk.com/t5/revit-api-forum/bd-p/160
- Viewers/checkers cited by users: Solibri, Navisworks, BIMvision, BIMcollab, Trimble Connect, OpenIFCViewer.
- buildingSMART IFC MVDs mentioned: IFC2x3 Coordination View 2.0, IFC4 Reference View, IFC4 Design Transfer View, IFC4x3.
- Add-in conflicts: Graphisoft ArchiCAD IFC add-in, third-party BIM add-ins; Dynamo for batch parameter setting.
- No government regulations appeared in this cell.

## Notable sources (15-30 best URLs, one line each)
- https://github.com/Autodesk/revit-ifc/issues/541 - IfcExportAs ignored since Revit 2023, workflow impact.
- https://github.com/Autodesk/revit-ifc/issues/907 - rooms elevation with survey-point levels.
- https://github.com/Autodesk/revit-ifc/issues/676 - auto-generated proxy types from curtain wall pieces.
- https://github.com/Autodesk/revit-ifc/issues/490 - excluding spaces; DontExport replaced by Export to IFC.
- https://github.com/Autodesk/revit-ifc/issues/374 - nested shared families lack decomposition.
- https://github.com/Autodesk/revit-ifc/issues/583 - generic export error, downgrade fix.
- https://help.autodesk.com/view/RVT/2025/ENU/?caas=caas%2Fsfdcarticles%2Fsfdcarticles%2FCertain-shared-parameters-not-exportetd-to-IFC-from-Revit.html - official KB on missing shared parameters.
- https://forums.autodesk.com/t5/revit-architecture-forum/ifc-export-in-2027-mapping-parameters-severely-lacking/td-p/14229702 - Revit 2027 mapping GUI complaints.
- https://forums.autodesk.com/t5/revit-ideas/gui-for-project-parameter-mapping-in-ifc-export-missing-in-revit/idi-p/14097939 - GUI idea.
- https://forums.autodesk.com/t5/revit-structure-forum/ifcexportas-parameter-doesn-t-work/td-p/8219179 - classic IfcExportAs thread.
- https://forums.autodesk.com/t5/revit-architecture-forum/revit-ifc-export-user-defined-properties-won-t-export/td-p/9767878 - user-defined psets.
- https://forums.autodesk.com/t5/revit-architecture-forum/ifc-export-location-issue/td-p/14205433 - location issue 2025.
- https://forums.autodesk.com/t5/revit-structure-forum/ifc-shared-coordinates-export-issue/td-p/10143119 - shared coordinates.
- https://forums.autodesk.com/t5/revit-architecture-forum/revit-ifc4x3-export-incorrect-space-boundaries/m-p/14048745 - IFC4x3 vs Reference View.
- https://forums.autodesk.com/t5/revit-architecture-forum/elements-are-being-exported-to-the-wrong-ifc-level/td-p/11927737 - storey assignment.
- https://forums.autodesk.com/t5/revit-architecture-forum/export-curtain-wall-to-ifc-as-a-single-object/td-p/12907563 - curtain wall aggregate.
- https://forums.autodesk.com/t5/revit-architecture-forum/revit-2024-3-update-revit-crashes-every-time-i-export-ifc/td-p/13030432 - crash after update.
- https://forums.autodesk.com/t5/revit-mep-forum/ifc-export-ducts-and-pipes/td-p/12370919 - MEP classes.
- https://forums.autodesk.com/t5/revit-api-forum/ifc-export-options/td-p/9686404 - IFCExportOptions via API.
- https://forums.autodesk.com/t5/revit-ideas/support-revit-extended-properties-in-ifc-export/idi-p/14151910 - extended properties idea.
- https://forums.autodesk.com/t5/revit-architecture-forum/multiple-buildings-in-one-revit-project-ifc-export-issues/td-p/13781660 - multiple buildings.

## Gaps (what you could not access or find; suspicious sites skipped)
- forums.autodesk.com returned HTTP 403 to every WebFetch, so thread bodies and accepted answers could not be read; 40 of 44 real records are from search-result snippets (evidence "snippet") and the answer_summary fields are as summarized there, not verified in full.
- Year values for forum threads are estimated from thread-ID ranges and search context.
- Only English forum posts; no videos, blogs or Reddit were searched in this cell. The Revit 2027 behaviour comes from snippets only.
- No suspicious sites encountered.
