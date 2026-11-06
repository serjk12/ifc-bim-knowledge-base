# Openings and penetrations: provision for voids, MEP-structure coordination via IFC, Durchbruchsplanung
Cell: t-openings-penetrations · Languages: English (real sources); synthetic prompts in en, de, ru, zh, es, pt, fr, ja, ko, it · Collected: 2026-11-06 · Records: 35 real / 19 synthetic · Communities covered: GitHub issues (IfcOpenShell/Bonsai, Autodesk/revit-ifc, That Open web-ifc, BIMserver), buildingSMART forums (Discourse search.json), OSArch community

Important limitation: the WebSearch budget was exhausted before any search ran, so all real records come from GitHub CLI search, and from forum-internal search pages fetched with WebFetch. No native-language (ru/zh/de/...) real posts were obtained. Native-language content exists only in the synthetic records, which are marked synthetic.

## Top themes (ranked by frequency)
- Revit IFC exporter gets openings wrong: floors, shafts, joined geometry, elongated or missing IfcOpeningElement (revit-ifc issues 530, 609, 763, 985).
- Opening/void geometry not cutting walls in viewers and libraries (IfcOpenShell, web-ifc, BIMserver, Bonsai void limit).
- Provision for void: IfcBuildingElementProxy with PROVISIONFORVOID versus IfcOpeningElement; reservation versus real opening.
- Future of provision for void in IFC4.3 after proxy deprecation (IfcVirtualElement, IfcVoidingFeature); German VDI/bS 2552.2.
- Automated MEP penetration creation: parametric sleeves, clearance offsets, clash-to-opening generation (Bonsai/IfcOpenShell requests).
- Gross versus net quantities when openings are present (Bonsai QTO, Revit exporter).
- Missing property sets and base quantities on openings, per origin (door/window versus generic-model void).
- Schema questions: which elements may be voided (beams yes, reinforcement no), one opening with several hosts, FillsVoids limits.
- Phase handling (existing/new/demolish) for openings in renovation drawings.
- Opening-related viewer and library UX (toggle openings, orphan openings, void limit warning).
- Change management between disciplines (BCF for opening requests, rule checks in Solibri).

## What people want (the goals behind the questions)
- Structural engineers want MEP void requests as discrete, checkable objects they can compare against their own openings.
- MEP engineers want openings to follow pipes/ducts automatically, with clearance, fire rating and sealing data.
- Coordinators want a list of crossings with no opening, exported as issues (BCF).
- Estimators want net area and volume that really deduct openings.
- Developers want a high-level API instead of hand-rolling boolean void logic.
- Everyone wants Revit exports where voids survive joins, shafts and edge cases.

## How people write here
- GitHub issues: structured templates, numbered repro steps, versions in the text ("Revit 2026 (Build 26.4.0.32, DEU)", "exporter 23.2.5"), screenshots, minimal .rvt attached. Tone mostly neutral, occasionally frustrated.
- Forum posts (buildingSMART): longer, polite, often start with context ("project experience", "we attended the meeting"), cite schema entity names and MVD/IDM documents.
- Short informal titles from newer users: "Void not voiding at certain positions.", "Opening hole in wall failed".
- Jargon: void, opening, provision for void, reservation, clearance, host, fills, "apply openings", proxy, sleeve, penetration.
- Misspellings seen: "IFCELEMENTASSEMLBY", "casuses", "do not fills".
- Code-switching in the German-engineering strand: terms such as Durchbruch, Aussparung, TGA, Statik appear in the synthetic prompts (not verified on real posts).
- Typical context given: exporter version, IFC schema (2x3 CV2.0, IFC4 RVArch), viewer. Often omitted: the actual file, the host element type, units.

## Local ecosystem
- buildingSMART International: https://forums.buildingsmart.org (Discourse; search.json works for fetching).
- German VDI/bS 2552 Blatt 2 (IDM for provision for voids) referenced in the forum thread https://forums.buildingsmart.org/t/provision-for-voids-in-ifc4x3-rc1/2998 (document itself not read).
- IFC schema: IfcOpeningElement, IfcRelVoidsElement, IfcRelFillsElement, IfcBuildingElementProxy PROVISIONFORVOID, Pset_BuildingElementProxyProvisionForVoid, Pset_OpeningElementCommon.
- Software: Solibri Model Checker (rule sets for void fit), Allplan (ProvisionForVoid works), Revit with open-source IFC exporter (https://github.com/Autodesk/revit-ifc), Bonsai/BlenderBIM (https://github.com/IfcOpenShell/IfcOpenShell), IfcClash, That Open web-ifc (https://github.com/ThatOpen/engine_web-ifc), BIMvision, BIMserver.
- Community: OSArch (https://community.osarch.org).

## Notable sources
- https://github.com/IfcOpenShell/IfcOpenShell/issues/10012 headless opening API request
- https://github.com/IfcOpenShell/IfcOpenShell/issues/8037 MEP penetration tool request
- https://github.com/IfcOpenShell/IfcOpenShell/issues/7472 new opening in existing wall
- https://github.com/IfcOpenShell/IfcOpenShell/issues/7626 orphan openings in Bonsai
- https://github.com/IfcOpenShell/IfcOpenShell/issues/6641 Add Void visibility
- https://github.com/IfcOpenShell/IfcOpenShell/issues/9235 gross versus net side area
- https://github.com/IfcOpenShell/IfcOpenShell/issues/8431 idempotent regeneration
- https://github.com/Autodesk/revit-ifc/issues/530 openings in floors
- https://github.com/Autodesk/revit-ifc/issues/609 shaft openings
- https://github.com/Autodesk/revit-ifc/issues/763 super long openings
- https://github.com/Autodesk/revit-ifc/issues/621 door/window opening psets
- https://github.com/Autodesk/revit-ifc/issues/985 flush beam, no opening
- https://github.com/ThatOpen/engine_web-ifc/issues/1462 GetFlatMesh and openings
- https://github.com/ThatOpen/engine_web-ifc/issues/2269 triangles over openings
- https://forums.buildingsmart.org/t/provisionforvoid/1279
- https://forums.buildingsmart.org/t/what-is-the-right-ifc-entity-for-water-outlet-into-a-structural-ifc-model/1410
- https://forums.buildingsmart.org/t/use-of-ifcopeningelement/4334
- https://forums.buildingsmart.org/t/provision-for-voids-in-ifc4x3-rc1/2998
- https://forums.buildingsmart.org/t/limit-of-fillsvoids/5124
- https://forums.buildingsmart.org/t/openings-with-multiple-hosts/1165
- https://forums.buildingsmart.org/t/can-opening-element-geometry-have-any-material-associated-with-it/4621
- https://community.osarch.org/discussion/3754/opening-cuts-skipped-in-bonsai-studio-0-9

## Gaps
- WebSearch quota exhausted at the start: no general web search, so no Autodesk forums, Stack Overflow, Reddit, or vendor knowledge-base threads.
- No real native-language posts (ru, zh, de, es, pt, fr, ja, ko, it). forum.dwg.ru fetch returned corrupted Cyrillic; cnblogs search returned 404; Autodesk forums search returned 403; Stack Overflow is blocked for fetch.
- The German Durchbruchsplanung strand (VDI/bS 2552, TGA-Statik workflows, Allplan, cad.de) is only visible indirectly through English forum threads.
- Several real records are snippet-only (titles from GitHub search or forum search blurbs), flagged evidence "snippet".
- No suspicious sites encountered or linked.
