# Catalog of real error messages and symptoms people paste (Revit exporter, IfcOpenShell, web-ifc, viewers, validation service)

Cell: t-error-messages · Languages: English (real, almost all), Spanish and Chinese (a few real); synthetic also ru, zh, es, pt, de, fr, ja, ko, it · Collected: 2026-11-06 · Records: 46 real / 18 synthetic · Communities covered: GitHub issues (Autodesk/revit-ifc, ThatOpen/engine_web-ifc, IfcOpenShell), forums.buildingsmart.org, community.osarch.org, segmentfault.com

Note: the WebSearch budget was exhausted before the first query ran, so no keyword search was possible. Material came from `gh` issue search and direct fetches of site search pages and Discourse JSON. Non-English coverage is therefore thin (see Gaps).

## Top themes (ranked by frequency)
- Revit IFC exporter aborts: "There has been an unrecoverable error during export... Try using filters and Current View Only mode" (most repeated Revit string)
- Generic "The IFC export process encountered an error" dialog, usually posted as a bare screenshot with only version numbers
- Exporter regressions after add-in updates (26.4.x vs 26.1, 2022.6 vs 2022.5.1); fix is to roll back
- Interfering add-ins (Enscape) and Revit UI language causing export to fail or do nothing
- Rooms/areas/spaces and Pset schedules or link export triggering the abort
- web-ifc WASM crashes on big Revit MEP files: "memory access out of bounds", "Aborted()", "table index is out of bounds"
- web-ifc geometry log spam: "[WEB-IFC][error][TriangulateBounds()] No basis found for brep!", "[GetMesh()] unexpected mesh type"
- wrapper/WASM version mismatch: "BindingError: function StreamMeshes called with 4 arguments, expected 3"
- STEP syntax and encoding errors: "Unable to parse IFC SPF header" (UTF-8 BOM), "Unexpected 'A' ... Parsing terminated", "Token $ at N invalid string", `\X2\` lowercase hex, accents in header
- IfcOpenShell/Bonsai import failures on invalid files: "RuntimeError: Failed to process representation item", empty IfcSurfaceStyle, IfcGridAxis without curve
- Validator messages users do not understand: "constraint violation in inverse attribute PlacesObject", "IfcGuid is not a 128-bit number"
- Viewer cannot open or link the file back (Revit Link IFC hangs; Bonsai Viewer on Mac)
- Bonsai pasted error dialogs: long auto-generated "os / blender_version / last_actions / Traceback" blocks

## What people want (the goals behind the questions)
- Get any IFC file out of Revit, even a partial one, and be told which element broke it
- Know whether the error is in the exporter, the file or the viewer (cross-check in BIMvision, Bonsai, ifcopenshell.validate)
- Find the offending entity from an error number such as `#58`, `#4005782` or a brep id
- Make a strict tool (IfcConvert, Bonsai) tolerate a customer's slightly invalid file, or fix that file
- Handle huge files in the browser or node without WASM aborts
- Pin exact working versions (exporter, web-ifc, wrapper) because upgrades break things

## How people write here
- GitHub bug reports follow the template: Problem Description, Revit Version, IFC for Revit Addon Version, Windows Version. Often only a screenshot. Fragment: "PR: The IFC export process encountered an error".
- The full error dialog text is pasted as the issue title; titles are often prefixed "PR:" (Autodesk's problem-report label).
- Developers paste raw log lines and stack traces ("RuntimeError: memory access out of bounds"), STEP lines (`#1929=IFCCURVEBOUNDEDPLANE(#1928,#1926,$);`) and version numbers.
- Beginners misname things: "ifc3X2", "erros" for errors, "blenderbim" after the Bonsai rename.
- Users bisect by add-in version, by category or by cross-opening in another viewer: "BIMvision opens it fine".
- Non-native English writers keep it short and skip greetings; Spanish title "Como poder exportar un modelo 3D estructural..." is polite but omits versions.
- Tone ranges from neutral report to frustration at "well-known" errors on tiny models ("no more than five walls").
- Maintainers reply with: "attach the .ifc", "does the validator say anything", "this file is invalid".

## Local ecosystem
- buildingSMART International: validation service and forums, https://forums.buildingsmart.org
- Autodesk IFC for Revit open-source exporter: https://github.com/Autodesk/revit-ifc
- IfcOpenShell, IfcConvert, Bonsai (ex BlenderBIM): https://github.com/IfcOpenShell/IfcOpenShell ; `python -m ifcopenshell.validate`
- That Open Company web-ifc and Fragments: https://github.com/ThatOpen/engine_web-ifc
- OSArch community: https://community.osarch.org
- Other tools named by users: IfcCheckingTool, BIMvision, BIMcollab, Navisworks, ETABS, FreeCAD, VisualARQ, Autodesk Forge/APS, SuperMap export plugin
- Standard referenced for string escapes: ISO 10303-21 (STEP physical file) as constrained by IFC string-encoding guidance

## Notable sources
- https://github.com/Autodesk/revit-ifc/issues/1021 unrecoverable error, 26.4.x regression
- https://github.com/Autodesk/revit-ifc/issues/590 "unrecoverable error" on tiny Revit 2023 models, Enscape cause
- https://github.com/Autodesk/revit-ifc/issues/296 request to skip bad elements instead of aborting
- https://github.com/Autodesk/revit-ifc/issues/882 link export plus Pset schedules failure
- https://github.com/Autodesk/revit-ifc/issues/762 areas triggering irregular error
- https://github.com/Autodesk/revit-ifc/issues/718 export fails after changing Revit language
- https://github.com/Autodesk/revit-ifc/issues/583 error dialog, rollback to 2022.5.1
- https://github.com/Autodesk/revit-ifc/issues/992 AccessViolationException curtain walls IFC4
- https://github.com/Autodesk/revit-ifc/issues/951 Link IFC hangs
- https://github.com/Autodesk/revit-ifc/issues/411 empty IFC via API FilterViewId
- https://github.com/ThatOpen/engine_web-ifc/issues/1402 "No basis found for brep"
- https://github.com/ThatOpen/engine_web-ifc/issues/1999 WASM memory errors on big MEP IFC4
- https://github.com/ThatOpen/engine_web-ifc/issues/2360 Aborted() and BindingError on version change
- https://github.com/ThatOpen/engine_web-ifc/issues/949 `\X2\` lowercase hex Chinese text
- https://github.com/ThatOpen/engine_web-ifc/issues/208 IFCCURVEBOUNDEDPLANE unexpected mesh type
- https://github.com/IfcOpenShell/IfcOpenShell/issues/4256 "Unable to parse IFC SPF header" BOM
- https://github.com/IfcOpenShell/IfcOpenShell/issues/1501 IfcConvert "Unexpected 'A' ... Parsing terminated"
- https://github.com/IfcOpenShell/IfcOpenShell/issues/2009 "Token $ at ... invalid string"
- https://github.com/IfcOpenShell/IfcOpenShell/issues/1016 wstring_convert to_bytes error
- https://github.com/IfcOpenShell/IfcOpenShell/issues/7821 "Index 2 is out of range for variant of size 2"
- https://github.com/IfcOpenShell/IfcOpenShell/issues/6972 empty IfcSurfaceStyle
- https://github.com/IfcOpenShell/IfcOpenShell/issues/8194 AssertionError on swept disk solid, validator clean
- https://forums.buildingsmart.org/t/a-number-of-interesting-revit-ifc-parsing-errors/4605 parser errors on Revit IFC4
- https://forums.buildingsmart.org/t/need-help-with-a-validation-issue/4372 PlacesObject inverse violation
- https://forums.buildingsmart.org/t/error-when-import-file-of-ifc3x2-into-blenderbim-do-the-shape-or-filesize-have-some-limits/3836 "Failed to process representation item"
- https://forums.buildingsmart.org/t/fatal-error-ifcguid-is-not-a-128-bit-number/3137 GUID validity
- https://community.osarch.org/discussion/3123/error-when-creating-custom-psets Bonsai traceback thread
- https://segmentfault.com/q/1010000008553854/a-1020000008763944 RVT to SVF stuck at 35% (Chinese)

## Gaps
- WebSearch was unavailable (budget exhausted), so no queries ran in Russian, Chinese, Spanish, Portuguese, German, French, Japanese, Korean or Italian beyond direct site fetches. Real non-English records: one Spanish (buildingSMART), two Chinese (segmentfault). Synthetic records cover the other languages but are not grounded in real posts.
- Autodesk forums, Stack Overflow, Graphisoft, Zhihu, CSDN and dwg.ru were not reachable (403, blocked, or empty); cnblogs search returned 404. Reddit not queried.
- The buildingSMART validation service's own error messages were only seen indirectly (ifcopenshell.validate, IfcCheckingTool); no direct validation-service posts collected.
- Navisworks IFC error strings were not found; only one snippet-level thread.
- No suspicious or pirated sites were encountered or linked.
