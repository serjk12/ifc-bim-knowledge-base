# Latinoamérica (México, Colombia, Perú, Chile, Argentina): preguntas sobre IFC
Cell: es-latam · Languages: Spanish (some English forum threads) · Collected: 2026-11-06 · Records: 20 real / 17 synthetic · Communities covered: planbim.cl, MEF Perú, MinVivienda Colombia, Autodesk forums (search snippets only), GitHub issues (Spanish-language), Graphisoft/Trimble Spanish help

**Important caveat:** this cell is THIN. The WebSearch budget was exhausted after 4 searches, GitHub search hit its rate limit, and the Autodesk/Graphisoft community pages returned 403. Only 20 real records were possible (target was 25-50), several by snippet only. Few are genuine LatAm user questions; most are official documents and a few Spanish-language GitHub issues. Synthetic prompts lean on knowledge of general Spanish BIM jargon and should be validated against real posts in a follow-up run.

## Top themes (ranked by frequency)
- National BIM standards and requirements (Planbim Chile, Plan BIM Perú, BIM Colombia) and what IFC deliverables they demand
- Revit IFC export failures (empty file, crashes, add-in conflicts, 2026 / IFC4x3 errors)
- Archicad-to-Revit IFC exchange (door/window placement regressions in Revit 2025-2027)
- Class mapping: elements exported as IfcBuildingElementProxy
- Property sets and required parameters (Planbim MIDE: IFC attribute, Pset, property)
- Quantities / metrados for budgets from IFC
- Viewers and files that will not open or lose geometry (normals, large files)
- Whether an app can import or export IFC at all (small tools, calculators)
- IFC versions (2x3 vs 4 vs 4.3/4.4) and what to deliver
- Field use: IFC in survey stakeout (Trimble)
- Teaching/learning: Planbim e-learning, webinars on IFC with Archicad

## What people want (the goals behind the questions)
- Meet public-sector delivery rules (IFC + required Psets) without rework
- Get a clean export from Revit/Archicad: correct classes, properties, storeys
- Take off quantities and feed budgets/schedules from the model
- Open and inspect models in free viewers; understand why geometry looks wrong
- Know whether small local tools can read or write IFC
- Automate checks (MIDE compliance, missing properties) instead of manual review

## How people write here
- Register: informal, lowercase, short; formal openers ("Hola", "Que tengan un buen día") in bug reports to international repos.
- Length: one line for tool questions; checklist style in dev issues.
- Jargon: "metrados" (quantities), "nativo" (native file), "proxy", "ifc" lowercase, "ambientes" (spaces/rooms), "niveles" (storeys), "cómputo" (takeoff), "MIDE", "MEI", "Fichas IFC".
- Typos/caps: "SOPOTARÁ ARCHIVOS IFC?" (all caps, typo); missing accents ("Exportacion", "Descripcion").
- Code-switching: English product terms (Export, Pset, Bonsai, Revit versions), mixed with Spanish verbs.
- Context given: often only the app name and IFC version; rarely the Revit export settings.
- Tone: neutral to urgent ("para mañana"), occasional frustration at regressions.
- Fragments: "se pierde parte de la información"; "no abre"; "pesa 800mb"; "qué onda" (Mexico).

## Local ecosystem
- Chile: Planbim (Corfo) https://planbim.cl/ ; Fichas de Entidades IFC, MIDE matrix, MEI manual, Estándar BIM para Proyectos Públicos, free e-learning; Red BIM de Gobiernos Latinoamericanos.
- Perú: MEF Plan BIM Perú https://www.mef.gob.pe/planbimperu/docs/planBIMpE.pdf ; Guía Nacional BIM; NTP-ISO 19650 (RD 004-2021-INACAL/DN); DS 203-2024-EF reported as mandating application (date unverified).
- Colombia: MinVivienda BIM portal https://bim.minvivienda.gov.co/ (redirects to minvivienda.gov.co at fetch time); BIM Forum, BIM Academic Forum.
- México: Iniciativa BIM (per CAF/El Peruano summary); Argentina: centralized public model (same source).
- Software: Revit, Archicad (IFC Manager), Trimble Access, Bonsai/IfcOpenShell, Autodesk IFC for Revit add-on (https://github.com/Autodesk/revit-ifc).
- Small local OSS: ingelibre/ingetrazo (exports IFC), jmarinderko/calculadora-RIC (planned IFC export for Chilean RIC).

## Notable sources
- https://planbim.cl/ - Chile national BIM program
- https://planbim.cl/ifc-y-actualizaciones/ - IFC 4.3/4.4 article
- https://planbim.cl/documentos/fichas-ifc/ - IFC entity sheets (seen in search; direct fetch returned 404)
- https://planbim.cl/documentos/mide/ - MIDE matrix (search only; fetch 404)
- https://repositorio.uchile.cl/handle/2250/179170 - thesis on Planbim standard
- https://www.mef.gob.pe/planbimperu/docs/planBIMpE.pdf - Plan BIM Perú
- https://www.mef.gob.pe/contenidos/inv_publica/docs/capacitaciones/2026/20260317.pdf - MEF 2026 training
- https://www.elperuano.pe/noticia/213920-avance-de-la-implementacion-del-building-information-modeling-en-america-latina - LatAm BIM status
- https://bim.minvivienda.gov.co/sites/default/files/doc-bim-2022-09/10_licencias_.pdf - Colombia BIM doc
- https://github.com/ingelibre/ingetrazo/issues/1033 - IFC import question
- https://github.com/IfcOpenShell/IfcOpenShell/issues/8131 - geometry loss (normals)
- https://github.com/jmarinderko/calculadora-RIC/issues/10 - IFC export feature
- https://github.com/Autodesk/revit-ifc/issues/1018 and /1019 - Archicad to Revit placement regression
- https://help.graphisoft.com/AC/28/SPA/_AC28_Help/121_IFC/121_IFC-1.htm - Spanish IFC help
- https://help.fieldsystems.trimble.com/trimble-access/2021.20/es/Map-files-BIM-and-IFC.htm - IFC in the field
- https://forums.autodesk.com/t5/revit-architecture-forum/revit-2026-won-t-export-to-ifc/m-p/13821992/highlight/true - Revit 2026 export
- https://forums.autodesk.com/t5/revit-architecture-forum/issues-exporting-ifc4x3-quot-unexpected-errors-occurred-while/m-p/13415457 - IFC4x3 errors
- https://forums.autodesk.com/t5/revit-architecture-forum/ifc-export-empty-file/m-p/8336603 - empty file

## Gaps
- Search budget exhausted after 4 queries; GitHub API rate-limited. Not searched: planbim YouTube titles, Reddit (r/BIM, r/Revit, Spanish subs), Spanish Autodesk forum, BIM Community, Telegram/Facebook groups, Colombian/Mexican/Argentine blogs, buildingSMART Spanish-language chapter, Archicad Spanish community.
- Autodesk forum and Graphisoft community pages returned 403, so the Autodesk threads are snippet-only and in English; no genuine Spanish forum Q&A was read.
- planbim.cl subpages for Fichas/MIDE returned 404 on fetch (seen only in search); MEF PDFs were not machine-readable.
- Mexico and Argentina have almost no coverage; Colombia only one snippet.
- No suspicious sites encountered.
- Recommended: rerun with a fresh search budget focusing on Spanish forum/YouTube/Reddit phrasing.
