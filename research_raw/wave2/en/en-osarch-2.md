# OSArch 2: Bonsai workflows (modelling, drawings, IfcClash, IfcTester, IFC editing)
Cell: en-osarch-2 · Languages: English · Collected: 2026-11-06 · Records: 43 real / 16 synthetic · Communities covered: community.osarch.org (General category, front page only), GitHub IfcOpenShell issue tracker (Bonsai, IfcClash, IfcTester), docs.bonsaibim.org (index only)

## Top themes (ranked by frequency)
- Drawings and sheets in Bonsai: CSS classes, hatches, EPset_Drawing, titles overwriting files, camera/crop loss, RCP style reset, slow switching.
- Beginner onboarding and Revit migration: where to start, video series, UI feels intimidating, do not sync .blend and .ifc together.
- IfcClash and clash workflows: 0 clashes found, flipped result pairs, unclear clash points, units (feet vs mm), BCF snapshots, packaging (pip gives library only).
- IfcTester / IDS: type coercion, uppercase booleans, restriction facets crashing, webapp usability and large-model limits, translations.
- Direct IFC editing: wall types vs mesh geometry, openings/windows snapping, mirror tool, spreadsheet import/export selector syntax, edit-mode quirks.
- Multi-discipline workflow: splitting arch/structure/MEP, linking IFC, IfcMerge, voids vs quantities.
- AI/LLM and MCP use with Bonsai: Claude + Blender MCP drawings from PDF redlines, text-to-IFC tools, AI-written bug reports and PRs.
- National drawing standards (DIN 1356-1) and style as sidecar vs inside IFC.
- Georeferencing and units affecting drawings, BCF and clash locations.
- Install/platform issues: Apple ARM, add-on conflicts (Speckle), Blender version churn.
- Quantities (QTO) correctness with openings and layered walls.
- Structural analysis, parametric framing/curtain walls as new Bonsai features.

## What people want (the goals behind the questions)
- Produce real construction drawing sets (sections, tags, callouts, lineweights, hatches) natively from IFC without CAD.
- Leave Revit/proprietary tools with a clear roadmap and a less intimidating UI.
- Run clash detection and issue BCF with real snapshots, across several linked models, without Python.
- Check models against IDS requirements and get readable, trustworthy pass/fail results.
- Edit IFC data (psets, types, materials, classifications) in bulk and keep geometry stable.
- Collaborate across disciplines in open formats with predictable voids and quantities.
- Let AI assistants drive Bonsai/IFC reliably (redlines to model, text to IFC).
- Comply with local drawing standards and teach them reproducibly.

## How people write here
- Register: forum posts are polite, structured, often long with exact versions (Blender 5.2.3, Bonsai 0.9.0) and numbered steps; GitHub reports are terse, pasted debug dumps, sometimes with no description.
- Beginners self-deprecate and hedge: "maybe I'm too stupid for it", "probably in the roadmap", "sorry if this is not a good bug report".
- Jargon: Bonsai (formerly BlenderBIM, BBIM), pset/EPset, IDS, BCF, daily build, underlay, RCP, shading style, sheets/drawings, IfcMerge, LinkIFC, Qto, snapping, local view.
- Code-switching: German material name "Holz" inside an English rule; Spanish replies in a text-to-IFC thread.
- Typical fragments: "Weird glitch where projection lines go missing", "0 clashes found though I made one", "Bonsai windows", "absolute beginner", "zero design here".
- Context given: software versions, OS, screenshots, sometimes a file link; context omitted: the actual IFC file (often "can't share"), schema version, exact workflow steps.
- Maintainers push back on vague titles ("Probably bug") and ask for steps/files; recent threads include AI-assisted reports that maintainers sometimes reject as hallucinated.

## Local ecosystem
- buildingSMART (IFC, IDS, BCF, bSDD): https://www.buildingsmart.org ; IDS test cases referenced in ifctester bug reports.
- IfcOpenShell / Bonsai / IfcClash / IfcTester: https://github.com/IfcOpenShell/IfcOpenShell , docs https://docs.bonsaibim.org , https://docs.ifcopenshell.org
- OSArch community and wiki: https://community.osarch.org , https://wiki.osarch.org
- Tools mentioned: Blender, FreeCAD, IfcMerge (Bruno Postle), ifc_structural_mechanics, PyNite, RFEM, Solibri, Inkscape, OpenAEC (Open PDF Studio / Open CAD Studio), BIMCompiler (red1), Speckle, OpenDesign/OpeningDesign libraries and tutorials.
- Standards: DIN 1356-1 (German drawing conventions), Eurocode, ISO 19650, IFC 4.3, OpenUSD debate vs IFC5.

## Notable sources
- https://community.osarch.org/discussion/3765/roadmap-for-revit-migrator-to-bonsai-bim-absolute-beginner : Revit migrator beginner roadmap.
- https://community.osarch.org/discussion/3783/claude-bonsai-construction-drawings : AI/MCP drawing workflow.
- https://community.osarch.org/discussion/3782/native-ifc-as-the-source-a-reproducible-project-template-for-bonsai-and-two-questions : native IFC template.
- https://community.osarch.org/discussion/3750/german-drawing-conventions-din-1356-1-for-bonsais-2d-output-a-reference-from-vocational-training : DIN drawings, CSS classes.
- https://community.osarch.org/discussion/2736/clash-detection-how-to/p1 : clash set how-to with wishes.
- https://community.osarch.org/discussion/3415/a-standard-bim-workflow-in-bonsai-arch-structure-mep : split models.
- https://community.osarch.org/discussion/3772/bonsai-windows : window snapping problem.
- https://community.osarch.org/discussion/3699/structural-analysis-in-bonsai-what-im-working-on : structural features.
- https://community.osarch.org/discussion/3741/add-parametric-framing-systems-railings-curtain-walls-storefronts : framing system.
- https://community.osarch.org/discussion/3779/openaec-moves-away-from-bonsai-to-homegrown-bim-app : UI pain points.
- https://community.osarch.org/discussion/3030/video-tutorial-series-for-blender-bonsai : tutorial series.
- https://community.osarch.org/discussion/3700/text-to-ifc-in-the-browser-built-on-ifcopenshell-looking-for-feedback : text to IFC.
- https://community.osarch.org/discussion/3214/bonsai-on-apple-arm-latest-macos : install problems.
- https://github.com/IfcOpenShell/IfcOpenShell/issues/6109 : clash bugs.
- https://github.com/IfcOpenShell/IfcOpenShell/issues/6138 : clash point semantics.
- https://github.com/IfcOpenShell/IfcOpenShell/issues/4278 : IfcClash upgrade plan.
- https://github.com/IfcOpenShell/IfcOpenShell/issues/4919 : ifcclash on shell.
- https://github.com/IfcOpenShell/IfcOpenShell/issues/7245 : IDS value coercion.
- https://github.com/IfcOpenShell/IfcOpenShell/issues/7415 : IfcTester webapp material rule.
- https://github.com/IfcOpenShell/IfcOpenShell/issues/5635 : drawing title overwrite.
- https://github.com/IfcOpenShell/IfcOpenShell/issues/7451 : type vs mesh geometry.
- https://github.com/IfcOpenShell/IfcOpenShell/issues/6937 : spreadsheet selector syntax.
- https://github.com/IfcOpenShell/IfcOpenShell/issues/8205 : georeferenced drawings/BCF.
- https://github.com/IfcOpenShell/IfcOpenShell/issues/4994 : beginner usability review.

## Gaps
- WebSearch budget was exhausted before the first query, so no search was possible; discovery relied on the OSArch front page, GitHub issue search via gh, and known thread links. Breadth across OSArch categories (Bonsai category, IFC category) is limited: category URLs returned 404 and OSArch search returned nothing.
- OSArch thread years are not shown on pages (only month/day); years are inferred from Bonsai/Blender versions and are approximate.
- Fewer than 20 independent searches were run (about 25 fetch/gh calls instead); no reddit, YouTube or LinkedIn coverage in this cell.
- Some GitHub issue answers were not fully read; no suspicious sites encountered. Forum is migrating software (Aug 15-16 banner), so URLs may change.
