# BIM practitioners blogs, LinkedIn articles, Medium: IFC pain points and opinions
Cell: en-blogs-linkedin · Languages: English (plus German posts from bim-me-up.com) · Collected: 2026-11-06 · Records: 34 real / 18 synthetic · Communities covered: BIM Corner (bimcorner.com), BIM me UP! (bim-me-up.com)

IMPORTANT LIMITATION: the WebSearch budget was already exhausted when this task started (every search returned "budget used up"). No search was possible. All 34 real records come from pages opened with WebFetch on two blogs found via their home pages, archive and sitemap. LinkedIn Pulse and Medium were NOT covered (LinkedIn topic page returned generic content; medium.com/tag/ifc returned HTTP 403). All 34 are evidence "page". Only about 33 fetches were made, below the 45 aimed for.

## Top themes (ranked by frequency)
- Wrong or generic IFC classes (IfcBuildingElementProxy, mapping table one row per category, IfcExportAs workarounds)
- Properties and psets missing or not exported (user-defined psets, shared parameters, type vs instance, Pset_ naming)
- Coordinates, base points, rotation and georeferencing causing misplaced or jittering models
- Spatial structure errors (extra storeys, wrong storey assignment, single IfcSite/IfcBuilding, furniture not in spaces)
- Exporting too much (all parameters, schedules, over-detailed geometry, other disciplines' placeholders) and file size
- IFC2x3 vs IFC4 readiness and certification gaps
- Viewer differences: properties not visible, which neutral viewer to trust
- Validation and requirements: buildingSMART Validation Service, IDS, Solibri, BEP/EIR
- Outdated Revit IFC exporter versions and parameter-file changes between versions
- Opinions on IFC itself: dated documentation, confusing version names, acronyms, "IFC is not lossless"
- IFC 5 / IFC 4.3 infrastructure hopes
- AI and IFC: invented property sets, ChatGPT plus IfcOpenShell scripting

## What people want
- Files that arrive in the partner's tool with correct class, storey, properties and location, so coordination and quantity take-off work
- A repeatable export checklist tied to BEP/EIR, and a way to verify a received file quickly
- Revit/ArchiCAD/Tekla-specific recipes for pset and class mapping
- Trustworthy automation (scripts, AI) that does not hallucinate standard property names

## How people write here
Register is professional, explanatory blog prose in the first person, fairly short; problem then solution structure; numbered checklists; concrete counts (161 proxies). Questions appear mostly in comments, terse and technical.
- Jargon: proxy (IfcBuildingElementProxy), pset, BEP/EIR/LOIN, federation, base point, MVD, IDS, bSDD
- German posts use English terms mixed in: "Typenparameter", "Data Exchange", "Shared Parameters"
- Illustrative fragments: "What happened to number three?"; "A valid file is not yet a complete file"; "Never export all parameters"; "IFC is not for visualisations or gaming"
- Emotional tone mostly neutral or mildly frustrated; opinion pieces are skeptical about vendor support.
- Context given: Revit version, IFC version, the exporter config file; commonly omitted: schema/MVD and viewer used.

## Local ecosystem
- buildingSMART International (https://www.buildingsmart.org) and Validation Service; IDS 1.0; bSDD
- Revit IFC exporter (Autodesk App Store, GitHub), Autodesk Data Exchange
- Viewers: BIM Vision, BIMcollab ZOOM, FZKViewer, Solibri, DDS-CAD Viewer, Areddo, usBIM
- Open source: IfcOpenShell, Bonsai (Blender), IfcQuickBrowser
- Trimble Quadri, Tekla, ArchiCAD, Civil 3D (infrastructure IFC 4.3)
- BIM Corner (Poland) and BIM me UP! (Germany/Austria) as educators

## Notable sources
- https://bimcorner.com/same-bridge-three-ifc-files/ - three bridge exports compared (2026)
- https://bimcorner.com/ai-ifc-properties/ - AI invents psets (2026)
- https://bimcorner.com/what-is-an-ifc-concept/ - IFC 4.3 concepts (2026)
- https://bimcorner.com/is-the-industry-ready-for-ifc4/ - IFC4 test results (2022)
- https://bimcorner.com/10-common-ifc-export-mistakes-to-avoid-part-1/ - mistakes 1-5 (2021)
- https://bimcorner.com/10-common-ifc-export-mistakes-to-avoid-part-2/ - mistakes 6-10 (2021)
- https://bimcorner.com/ifc-export-rules-part-2-what-parameters-to-export-dos-and-donts/ - dos and don'ts
- https://bimcorner.com/what-i-dont-like-about-ifc/ - complaints (2020)
- https://bimcorner.com/super-ifc/ - what a good IFC looks like (2024)
- https://bimcorner.com/exporting-ifc-from-revit-part-1-mapping/ - IfcExportAs (2021)
- https://bimcorner.com/exporting-ifc-from-archicad/ - ArchiCAD pain points (2021)
- https://bimcorner.com/export-a-tekla-structures-model-to-an-ifc-file/ - Tekla (2021)
- https://bimcorner.com/model-validation-as-a-key-step-in-the-bim-workflow/ - IDS and Solibri (2024)
- https://bimcorner.com/use-ai-to-manipulate-your-ifc/ - ChatGPT with IfcOpenShell (2024)
- https://bimcorner.com/analyzing-ifc-files/ - inspecting raw IFC (2024)
- https://bim-me-up.com/revit-ifc-und-koordinatensysteme/ - coordinates in Revit (2023)
- https://bim-me-up.com/revit-typenparameter-nach-ifc-exportieren/ - type parameters (2023)
- https://bim-me-up.com/ifc-5-eine-neue-hoffnung-fuer-interoperabilitaet/ - IFC 5 (2025)
- https://bim-me-up.com/ifc-verlinken-vs-data-exchange-laden-in-revit/ - link vs Data Exchange (2025)
- https://bim-me-up.com/ifc-struktur/ - spatial structure (2024)
- https://bim-me-up.com/ifcbuildingstorey/ - storey assignment (2024)
- https://bim-me-up.com/revit-phasen-nach-ifc-exportieren/ - phases (2023)
- https://bim-me-up.com/die-popularsten-ifc-viewer/ - viewers (2020)

## Gaps
- Web search unavailable (budget exhausted): no LinkedIn Pulse or Medium articles, no other blogs; those must be re-run in a follow-up.
- medium.com tag page returned 403; LinkedIn topics page returned unrelated content.
- Only 34 real records (below the 30-60 target only in breadth of sources: two blogs). Many records share one author per blog, so askers are not diverse.
- Reader comments were mostly not loaded (bim-me-up comments load dynamically).
- Year missing for one record (export rules part 2); stored as null.
- No suspicious sites encountered.
