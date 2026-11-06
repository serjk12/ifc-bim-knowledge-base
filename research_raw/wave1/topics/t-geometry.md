# Geometry problems: missing elements, faceted/heavy geometry, openings lost, curtain walls, stairs, railings, nested families

Cell: t-geometry · Languages: English (real sources), Japanese (1 source); synthetic in en, ru, zh, es, pt, de, fr, ja, ko, it · Collected: 2026-11-06 · Records: 35 real / 17 synthetic · Communities covered: Autodesk/revit-ifc GitHub, ThatOpen/engine_web-ifc GitHub, IfcOpenShell/Bonsai GitHub, OSArch community forum, Qiita

Important limitation: the WebSearch budget was exhausted before any search ran, and GitHub CLI search was rate-limited (HTTP 403). All real records came from first-party site pages fetched directly (GitHub issue lists and issues, OSArch forum search). No native-language community (dwg.ru, csdn, cnblogs, cad.de, zhihu, Autodesk forums, buildingSMART forums, Stack Overflow) could be read. Only the 35 real records exist; 6 are snippet-only (listing titles).

## Top themes (ranked by frequency)
- Openings and voids lost, duplicated, displaced or mis-cut (IfcOpeningElement, IfcRelVoidsElement), the biggest cluster, both on export and in viewers.
- Viewer or engine renders the model incorrectly (web-ifc, Bonsai) while another viewer (BIMvision, Solibri, xeokit) shows it fine.
- Whole elements or categories silently missing from export (floors, steel connections, masonry, fittings, walls).
- Regressions between exporter builds; users bisect versions and ask which build works.
- Curtain walls: mullions dropped, only panels exported.
- Stairs and railings: predefined type lost, railings exported inconsistently with stairs.
- Heavy or faceted geometry: IfcFacetedBrep, tessellation resolution, decimation, huge file size.
- Boolean/tolerance failures: sliver cutters, coplanar faces, near-degenerate openings, hangs on waffle slabs.
- Elements present but uncontained in the spatial structure, hence hidden in viewers.
- Beam, column and slab openings displaced (Z offset in IFC4 vs correct IFC2x3), wrong base quantities.
- Quantities and psets of openings inconsistent between door/window openings and void families.
- MEP fittings and swept disk solids dropped by kernels.

## What people want (the goals behind the questions)
- Find out which elements or categories went missing and why, ideally automatically across IFC received from others.
- A reliable export setting or workaround per Revit/exporter version (IFC2x3 CV2.0 vs IFC4 RVArch, revert to older add-in).
- Openings that appear, carry correct type (HOLE/CUTOUT) and quantities for BoQ and coordination.
- Lighter files: lower triangle counts, replace breps with swept solids.
- Faithful curved geometry instead of coarse facets.
- Native parametric curtain walls, railings and stairs in open tools.
- Reproducible bug reports with minimal files; maintainers' root-cause explanations.

## How people write here
- Register: terse, technical bug-report style on GitHub (templates: Revit version, exporter build, Windows version, schema, steps). Forum posts are longer and more tentative.
- Typical length: 2-8 sentences plus version list; titles often prefixed "PR:" (problem report) or "[Bug]:".
- Jargon: "proxy", "voids", "cutters", "booleans", "tessellation", "faceted brep", "mapped representation", "CV2.0", "RVArch", "Coordination View".
- Code-switching in Japanese: katakana-English terms plus hedging ("to omoimasu", "kamoshiremasen"); the author frames failure as a lesson.
- Context given: exact build numbers ("25.4.30.30 broken, 25.4.0.32 worked"), viewers compared (Solibri, BIMvision, xeokit).
- Context omitted: no sample file ("cannot share the model"), unknown representation type, no Revit version.
- Tone: frustrated regression language, politely escalating ("any update?"); one bounty offered (1000 USD).
- Fragments: "Removing the door fixes the wall." / "worked in 1.5.1" / "same file fine in BIMvision" / "Apply Openings fixes it".
- Synthetic prompts mimic lowercase, double question marks and mixed English class names (IfcRelFillsElement) inside non-English sentences.

## Local ecosystem
- Autodesk revit-ifc exporter (open source add-on, issues tracked internally as REVIT-nnnnnn): https://github.com/Autodesk/revit-ifc
- That Open Company web-ifc / fragments: https://github.com/ThatOpen/engine_web-ifc
- IfcOpenShell, IfcConvert, Bonsai (Blender): https://github.com/IfcOpenShell/IfcOpenShell
- OSArch community: https://community.osarch.org
- Viewers named as references: Solibri, BIMvision, xeokit, Xbim Xplorer, Open IFC Viewer.
- Mapping files: exportlayers-ifc-IAI.txt, Revit IFC class mapping tables.
- Japanese: Qiita (Revit API / IFC articles).

## Notable sources
- https://github.com/Autodesk/revit-ifc/issues/944 (curtain wall mullions missing, fixed Revit 2027)
- https://github.com/Autodesk/revit-ifc/issues/759 (floors not exporting, locale encoding root cause)
- https://github.com/Autodesk/revit-ifc/issues/763 (elongated openings)
- https://github.com/Autodesk/revit-ifc/issues/643 (sketch openings in sloped slabs)
- https://github.com/Autodesk/revit-ifc/issues/708 (beam openings displaced in IFC4)
- https://github.com/Autodesk/revit-ifc/issues/394 (wall geometry missing near door)
- https://github.com/Autodesk/revit-ifc/issues/755 (void feature types by design)
- https://github.com/Autodesk/revit-ifc/issues/621 (door/window openings vs void families)
- https://github.com/Autodesk/revit-ifc/issues/890 (steel connections gone)
- https://github.com/Autodesk/revit-ifc/issues/715 (stairs and railings together)
- https://github.com/Autodesk/revit-ifc/issues/677 (stair predefined type)
- https://github.com/ThatOpen/engine_web-ifc/issues/2269 (triangle surfaces across openings, tolerance)
- https://github.com/ThatOpen/engine_web-ifc/issues/1057 (wall with opening wrong)
- https://github.com/ThatOpen/engine_web-ifc/issues/2097 (waffle slab hang)
- https://github.com/ThatOpen/engine_web-ifc/issues/927 (wall not rendered)
- https://github.com/ThatOpen/engine_web-ifc/issues/2111 (missing geometry)
- https://github.com/IfcOpenShell/IfcOpenShell/issues/9372 (masonry missing, uncontained)
- https://github.com/IfcOpenShell/IfcOpenShell/issues/9748 (Manifold crash on sliver openings)
- https://github.com/IfcOpenShell/IfcOpenShell/issues/10049 (iterator drops opening cut on mapped body)
- https://github.com/IfcOpenShell/IfcOpenShell/issues/9511 (pipe bends not loading)
- https://community.osarch.org/discussion/3754/opening-cuts-skipped-in-bonsai-studio-0-9
- https://community.osarch.org/discussion/3501/how-to-adjust-brep-tesselation-resolution-in-bonsai
- https://community.osarch.org/discussion/3741/add-parametric-framing-systems-railings-curtain-walls-storefronts
- https://community.osarch.org/discussion/comment/23266 (decimate IFC geometry)
- https://qiita.com/KengoTanaka-BIM/items/6cec74e04bf581b21cf5 (Japanese Revit API / IFC geometry)

## Gaps
- WebSearch unavailable (budget exhausted); no keyword searches, so no coverage of Autodesk forums (403 on direct fetch), buildingSMART forums (blocked), Stack Overflow (blocked), Reddit, Graphisoft, dwg.ru, csdn, cnblogs, zhihu, cad.de, foros/foruns.
- GitHub CLI search rate-limited; only web issue lists were readable.
- Non-English real data is a single Japanese Qiita article; Russian, Chinese, Spanish, Portuguese, German, French, Korean, Italian are covered only by synthetic records and should be treated as unverified phrasing.
- Nested families and detail on "heavy geometry" in Revit are thin; most real data is on openings and exporter regressions.
- Some GitHub dates look like future 2026 data as served by the pages; reported as seen.
- No suspicious sites encountered.
