# IFC version and MVD choice (IFC2x3 vs IFC4 vs IFC4.3; CV2.0, RV, DTV) and compatibility
Cell: t-versions-mvd · Languages: English (deep), Spanish, Japanese real samples; Russian, Chinese, German, French, Portuguese, Korean, Italian synthetic only · Collected: 2026-11-06 · Records: 40 real / 18 synthetic · Communities covered: forums.buildingsmart.org, GitHub (Autodesk/revit-ifc, IfcOpenShell, BIMserver), community.osarch.org, qiita.com

## Top themes (ranked by frequency)
- Which version/view to deliver: IFC2x3 CV2.0 still the safe default vs IFC4 Reference View.
- IFC4 RV lacks material layer sets (constituent sets instead); users see "materials missing".
- Design Transfer View: unofficial, never finalized, advanced BReps/CSG; where is the spec?
- Receiving tools fail on IFC4 geometry (IfcTriangulatedFaceSet, PolygonalFaceSet, AdvancedBrep): Revit Open, BIMserver, Solibri, Trimble.
- Revit Open IFC vs Link IFC: different code paths, partial IFC4 support.
- Converting/downgrading between schemas (4 to 2x3, 4.3 to 4) and what is lost.
- IFC4.3 adoption: exporter maturity, quantity sets, IfcOpenShell schema id IFC4X3_ADD2, official MVDs.
- Exporter bugs that differ per schema (curtain walls IFC4 crash, 2x3 displaced columns, wrong header view).
- Reading the header: FILE_SCHEMA and ViewDefinition to identify version/MVD.
- Renamed entities/properties between 2x3 and IFC4 and missing changelogs.
- Certification trust (bSI certification, pass/fail, outdated vs new software versions).
- Georeferencing and colour/style storage differing between 2x3 and IFC4.
- Confusion over terms: MVD vs IDM vs COBie, CV vs implementer agreements.

## What people want (the goals behind the questions)
- A clear recommendation of which schema/MVD to export for a given receiving tool or contract.
- Confirmation that a delivered file really is the required schema and view.
- A lossless (or clearly loss-reported) way to move between IFC2x3, IFC4 and IFC4.3.
- Documentation: Revit exchange requirement effects, DTV definition, 4.3 MVDs, changelogs.
- Receiving software that supports modern geometry and layered materials.
- Predictable exporter behaviour per version (mappings, psets, quantities).

## How people write here
- Forum posts (buildingSMART): polite, structured, often non-native English; greeting and sign-off; citing schema names ("IFC4ADD2TC1", "IFC2x3 CV2.0", "IFC4RV"). Fragments: "Is it safe to say that every CV...", "Thoughts?", "L.S.".
- GitHub: template-driven ("PR:", "ENH:", "INQ:", "BUG:" prefixes), include Revit/add-in versions, short repro steps; mild frustration.
- OSArch beginners: emotive and brief ("I am a beginner!!"), little version context given.
- Typical omissions: schema version and MVD frequently not stated; users say "IFC4" meaning RV or DTV interchangeably.
- Jargon/abbreviations: CV2.0, RV, DTV, "4x3", "2x3", "advanced brep", "faceted brep", "tessellation", "MVD", "ADD2 TC1".
- Spelling traps seen: "Elntities", "EnvironmenalClass", "ContructionType", "IFC 4.3" vs "IFC4X3".
- Japanese blog tone is hedged hearsay ("...そうです"); Spanish formal ("Buenas tardes", thesis context).
- Synthetic Russian/Chinese prompts are lowercase, slangy ("ифс", "навис", "солибри"); these are inferred, not sampled from real posts.

## Local ecosystem
- buildingSMART International: technical specs and MVD pages https://technical.buildingsmart.org ; IFC4.3 docs https://ifc43-docs.standards.buildingsmart.org ; forum https://forums.buildingsmart.org
- ISO 16739-1:2018 (IFC4) and IFC4.3 ADD2 (schema id IFC4X3_ADD2).
- Autodesk revit-ifc open-source exporter: https://github.com/Autodesk/revit-ifc (Jira REVIT-xxxxx tracking).
- IfcOpenShell / Bonsai: https://github.com/IfcOpenShell/IfcOpenShell ; OSArch community https://community.osarch.org (incl. Spanish category).
- BIMserver https://github.com/opensourceBIM/BIMserver ; Geometry Gym (schema upgrade/downgrade) ; BIM Vision, Solibri, Trimble, BIMcollab ZOOM as receiving tools.
- Japanese Qiita IFC authors; Chinese resources only seen via snippets (skipped, see Gaps).

## Notable sources
- https://forums.buildingsmart.org/t/why-are-material-layer-sets-excluded-from-ifc4-reference-view-mvd/3638 RV vs layers
- https://forums.buildingsmart.org/t/ifc4-design-transfer-view-experiences/4362 DTV status
- https://forums.buildingsmart.org/t/official-model-view-definitions-for-ifc-4-3/5737 4.3 MVDs
- https://forums.buildingsmart.org/t/ifc4-design-transfer-view-spec/1737 DTV spec missing
- https://forums.buildingsmart.org/t/why-are-csg-representations-mandated-for-dtv/2311 DTV debate
- https://forums.buildingsmart.org/t/ifc-2x3-implementation-agreements-status-in-ifc4/2786 CV in IFC4
- https://forums.buildingsmart.org/t/ifc2x3-to-ifc4-mappings/3093 migration mappings
- https://forums.buildingsmart.org/t/list-of-changes-between-ifc-versions/4604 changelog
- https://forums.buildingsmart.org/t/ifc4-property-name-changes/2539 renamed psets
- https://forums.buildingsmart.org/t/geolocation-standards-in-ifc2x3-and-ifc4/2329 georef across versions
- https://forums.buildingsmart.org/t/bsi-software-certification-and-ifc4/3192 certification
- https://forums.buildingsmart.org/t/is-ifc-4-3-officially-a-change-in-the-naming-schema/5446 naming
- https://forums.buildingsmart.org/t/como-poder-exportar-un-modelo-3d-estructural-realizado-en-revit-a-etabs-por-medio-del-formato-ifc/2985 Spanish
- https://github.com/Autodesk/revit-ifc/issues/396 RV vs DTV materials
- https://github.com/Autodesk/revit-ifc/issues/480 AdvancedBrep
- https://github.com/Autodesk/revit-ifc/issues/587 IfcTriangulatedFaceSet import
- https://github.com/Autodesk/revit-ifc/issues/744 Exchange Requirement
- https://github.com/Autodesk/revit-ifc/issues/768 IFC4x3 exporter
- https://github.com/Autodesk/revit-ifc/issues/876 mapping per version
- https://github.com/Autodesk/revit-ifc/issues/1013 4x3 RV header bug
- https://github.com/IfcOpenShell/IfcOpenShell/issues/6886 IFC4X3 schema error
- https://github.com/IfcOpenShell/IfcOpenShell/issues/6174 RV vs 4x3 loading
- https://github.com/opensourceBIM/BIMserver/issues/1103 IFC4 ArchiCAD
- https://community.osarch.org/discussion/898/ifc-file-doesnt-import-open-into-revit Revit Open limits
- https://qiita.com/kiyuka/items/00434f1b8e0b38c621fb Japanese FILE_SCHEMA

## Gaps
- The WebSearch budget was exhausted at the start (all five initial searches refused), so no keyword search was possible; sources came from GitHub CLI search, buildingSMART forum JSON, OSArch pages and Qiita search.
- Not covered: forums.autodesk.com (403), stackoverflow.com and reddit (blocked), dwg.ru (search page unreadable), csdn/zhihu/cnblogs (captcha or not reachable), Graphisoft, Korean/Italian/French/German/Portuguese/Russian real posts. These languages are only synthetic.
- One Baidu results page was fetched in error as a workaround for the search limit; its redirect links were not used as sources and none of its content is in the records.
- OSArch Spanish category is largely spam; only a few IFC titles seen and not opened.
- One OSArch post (3150) is vendor self-promotion with closed-source licensing disputes; recorded as promo, not a recommendation.
