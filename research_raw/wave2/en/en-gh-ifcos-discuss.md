# IfcOpenShell GitHub Discussions and docs questions (Python API, IfcPatch, IfcConvert usage)
Cell: en-gh-ifcos-discuss · Languages: English · Collected: 2026-11-06 · Records: 50 real / 18 synthetic · Communities covered: github.com/IfcOpenShell/IfcOpenShell Discussions (Q&A, General, Ideas; about 370 threads scanned via GraphQL, 2021-2026)

## Top themes (ranked by frequency)
- Reading psets/properties with util.element (get_psets vs api) and missing/mismatching values vs viewers
- Quantity takeoff: length/width/height, volumes, weight, per-layer volumes, BOQ from geometry
- IfcConvert usage: --model/--plan, include/exclude filters, centering, GLB/OBJ/DAE outputs, materials
- Geometry iterator/create_shape: failures, ordering, openings, multiprocessing, speed
- Spatial structure and relations (storeys, spaces, doors, decomposition tree to JSON)
- Performance on large files (IfcConvert memory, IDS validation time)
- IfcPatch recipes and use as a library, merging/extracting models
- Units and coordinates (mm to m, global to local, georeferencing)
- Authoring from scratch via api (psets, storeys, types, alignments IFC4.3)
- Installation/compile problems (pip, C++, Visual Studio, Mac)
- IDS/IfcTester validation
- AI/LLM interest (ChatGPT code failing, Claude Blender connector, TS port for AI project)

## What people want
Extract data (properties, quantities, hierarchy) into tables/JSON; convert to web-friendly formats (GLB) while keeping GlobalIds; batch-modify files; understand which API module does what; fast processing of big models.

## How people write here
Mostly developers; polite openers ("Hello all!", "Hi everyone!"), short problem statement then pasted code or traceback; newcomers say "new to IFC and Python"; many non-native English speakers; academic/thesis context. Fragments: "Any way around ?", "I am new in ifc parser", "struggling with --help", "ChatGPT code gives errors". Replies from maintainers are terse, point to docs or one function name.

## Local ecosystem
- IfcOpenShell: https://github.com/IfcOpenShell/IfcOpenShell ; docs https://docs.ifcopenshell.org
- Bonsai/BlenderBIM, IfcPatch, IfcConvert, IfcTester (IDS), IfcClash
- buildingSMART IFC4.3 docs: https://ifc43-docs.standards.buildingsmart.org
- OSArch wiki, Solibri, BIMcollab, BIMvision, three.js, CloudCompare

## Notable sources
All under https://github.com/IfcOpenShell/IfcOpenShell/discussions/ plus number: 7018, 1828, 2763, 2746, 3028, 3133, 3188, 7540, 8102, 2862, 2834, 3962, 4825, 2713, 7714, 8104, 3894, 4460, 4470, 5772, 5250, 6782, 7017, 4366, 5885, 7001, 6520, 5858, 4541, 5813, 4455, 4182, 3824, 2184, 2737, 3786, 7177, 8027, 9631.

## Gaps
docs.ifcopenshell.org pages fetched but only navigation text was extractable (very large pages), so docs-derived questions are not captured; the selecting_elements URL returned 404. Many answer_summary fields say the answer was not captured because only 260-character excerpts were read. Discussion bodies were truncated to about 420 characters.
