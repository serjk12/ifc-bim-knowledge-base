# Students, beginners and educators: what confuses them about IFC

Cell: p-student · Languages: English (main), Japanese, Chinese, Spanish; synthetic prompts also in ru, pt, de, fr, ko, it · Collected: 2026-11-06 · Records: 36 real / 19 synthetic · Communities covered: community.osarch.org, forums.buildingsmart.org, GitHub issues (IfcOpenShell/Bonsai, Autodesk/revit-ifc), Qiita (ja), SegmentFault (zh)

IMPORTANT LIMITATION: the web search budget was exhausted before the first query ran, so no WebSearch was possible. All material came from direct page fetches (forum tag pages, buildingSMART search.json, gh CLI, Qiita and SegmentFault). Native-language coverage (ru, pt, de, fr, ko, it, most zh) is therefore thin; those languages appear only as synthetic records.

## Top themes (ranked by frequency)
- "Where do I even start learning IFC?" Beginners cannot find a structured guide (spec, MVD docs and tutorials feel developer-level).
- Same model looks different in each viewer or authoring tool (Bonsai file broken in Revit, Bricscad, Archicad).
- Class confusion: IfcWall vs IfcWallStandardCase, IfcWall vs IfcCurtainWall, proxy elements.
- Name vs ObjectType vs Reference vs type name; Revit puts the type name in ObjectType, which teachers repeatedly have to untangle.
- Property sets and quantities: where do they live, why BaseQuantities are missing, how to read them via IsDefinedBy.
- Materials: IfcMaterial vs layer set vs profile set vs constituent set.
- Spatial structure and spaces: IfcSpace boundaries, storeys, groups vs systems vs zones.
- Revit export settings: IfcExportAs, shared parameter files, custom pset mapping files, hidden "rules".
- Tool choice for learners: Revit vs Bonsai/Blender vs FreeCAD; software-neutral courses.
- Docs and tutorials gaps for open-source tools (missing pages, text-only tutorials, empty C++ examples).
- IFC 4.3 / infrastructure (alignment, rail) for newcomers; version confusion (2x3 vs 4 vs 4.3, deprecated attributes).
- GUID persistence and Revit UniqueId vs IFC GlobalId.
- Programming entry: IfcOpenShell, xBIM, web-ifc; geometry extraction and performance.

## What people want (the goals behind the questions)
- A learning path with a first project, a free viewer and plain-language explanations of concepts.
- To pass an assignment or thesis: counts, areas, material lists, storey trees from a given IFC.
- To know whether the problem is their file, their export settings or the viewer.
- Educators want reproducible course material, software-neutral content and local-language textbooks.
- Developers newly arrived in AEC want to read IFC without authoring software and keep IDs stable.

## How people write here
- English forums: friendly, informal, greeting and thanks, self-labels such as "absolute beginner", "complete freshies", "newbie". Examples: "I am a beginner!! I created a file...", "anyone? Bueller?".
- Non-native English is common (typos like "Documantation", loose grammar); questions are often 2 to 6 sentences with sparse context (no file, no version).
- GitHub issues by beginners are short, numbered lists of gripes; educators write in a measured, authoritative tone.
- Japanese Qiita: casual blog voice, emoticons, hedges ("調べてみた", "できなかった話"), first-person recaps.
- Chinese: plain FAQ headings ("是什么？用什么软件可以打开？"); content often promotional.
- Spanish: warm opener "¡Hola! Les comparto...", English terms kept (Clash Detection, add-on).
- Typical omissions: IFC schema version, MVD, exporter version, expected result. Typical code-switching: tool names and IFC class names stay in English inside local-language text.

## Local ecosystem
- buildingSMART International: https://technical.buildingsmart.org/ (Implementation Guidance), forums https://forums.buildingsmart.org/
- OSArch community and wiki (open source AEC, Bonsai/BlenderBIM): https://community.osarch.org/ , https://wiki.osarch.org/
- IfcOpenShell / Bonsai: https://github.com/IfcOpenShell/IfcOpenShell
- Autodesk IFC exporter: https://github.com/Autodesk/revit-ifc
- xBIM, IFC.js / That Open (web-ifc), FreeCAD BIM, Speckle mentioned as learner tools.
- Japan: TokyoAECDev IFC study group (via Qiita recap), Qiita IFC tag https://qiita.com/tags/ifc
- Brazil: engineering educators adopting BlenderBIM with software-neutral curriculum (OSArch thread).
- Germany: Allplan users, DIN drawing conventions discussed on OSArch (not opened).

## Notable sources
- https://community.osarch.org/discussion/3765/roadmap-for-revit-migrator-to-bonsai-bim-absolute-beginner
- https://community.osarch.org/discussion/3280/i-am-a-beginner-i-created-a-file-in-bonsai-but-it-doesnt-appear-correctly-in-3d-in-revit
- https://community.osarch.org/discussion/1506/blenderbim-in-university-curriculum
- https://community.osarch.org/discussion/316/beginners-ifc-course-free-available
- https://community.osarch.org/discussion/635/ifcspace-and-blenderbim
- https://community.osarch.org/discussion/2758/composite-wall-in-bonsai-bim
- https://community.osarch.org/discussion/1827/what-are-the-various-use-cases-of-ifcgroup
- https://community.osarch.org/discussions/tagged/education
- https://forums.buildingsmart.org/t/ifc-questions-from-a-beginner/2515
- https://forums.buildingsmart.org/t/education-and-training-for-new-ifc-users/4925
- https://forums.buildingsmart.org/t/ifc-schema/3540
- https://forums.buildingsmart.org/t/ifc-documantation/1454
- https://forums.buildingsmart.org/t/difference-between-expectations-and-reality-of-ifc-standards/1040
- https://forums.buildingsmart.org/t/ifc-materials/4861
- https://forums.buildingsmart.org/t/correct-use-of-ifc-name-and-reference-deprecated/6429
- https://forums.buildingsmart.org/t/understanding-ifc-alignment-and-rail-beginners-guide/4117
- https://github.com/Autodesk/revit-ifc/issues/502
- https://github.com/Autodesk/revit-ifc/issues/392
- https://github.com/Autodesk/revit-ifc/issues/364
- https://github.com/IfcOpenShell/IfcOpenShell/issues/4994
- https://github.com/IfcOpenShell/IfcOpenShell/issues/7244
- https://github.com/IfcOpenShell/IfcOpenShell/issues/3910
- https://qiita.com/msp0310/items/0d7966a93ff380e11970
- https://qiita.com/ktaroabobon/items/25349c7fa7bdb55c63b8
- https://qiita.com/Takashi_Kasuya/items/97899d15e7ec0186eecf
- https://segmentfault.com/a/1190000047698784

## Gaps
- WebSearch was unavailable (budget exhausted), so no Reddit, Stack Overflow (WebFetch blocked), Autodesk forums (403), Graphisoft, zhihu, csdn, cnblogs, cad.de, dwg.ru content was found. dwg.ru returned mis-encoded Cyrillic, so its IFC threads could not be read.
- No real Russian, Portuguese, German, French, Korean or Italian posts; only synthetic prompts in those languages.
- Some record years come from page text; the Chinese article year (2026) is inferred from site footer.
- buildingSMART search.json was rate-limited (429) after a few calls.
- No suspicious or pirated sites were encountered or linked.
