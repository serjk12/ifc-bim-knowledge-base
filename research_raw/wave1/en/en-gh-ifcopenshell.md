# GitHub: IfcOpenShell / Bonsai issues and discussions (user-facing)
Cell: en-gh-ifcopenshell · Languages: English · Collected: 2026-11-06 · Records: 48 real / 16 synthetic · Communities covered: IfcOpenShell GitHub issues and Discussions (Bonsai, IfcConvert, IfcTester, IfcClash, IfcDiff, IfcPatch, ifcopenshell.api)

## Top themes (ranked by frequency)
- Import/open failures and crashes in Bonsai on files from Revit, Vectorworks, Archicad (invalid placements, huge files, freezes)
- Large file and performance: slow open, slow save, slow print, memory not reclaimed, 2 GiB IfcConvert limit
- Quantity take-off accuracy (Gross vs Net areas, bounding box dimensions, non-manifold volumes) and comparison with Solibri
- Georeferencing and large coordinates: drawings, BCF cameras, linked models, units in feet vs mm
- IDS / IfcTester validation quirks (PredefinedType USERDEFINED, regex, duplicate psets, optional facets)
- Clash detection (ifcclash crashes, clash point semantics, BCF compatibility with BIMcollab)
- Drawings and SVG output (material layers merged, link matrix, headless rendering)
- COBie / FM handover export gaps (missing tabs, empty systems)
- Python API how-tos (create_shape failures, representation contexts, structural model, alignment)
- IFC4X3 infrastructure/bridge needs (IfcProjectionElement, alignments)
- Cost/schedule (5D/4D) CSV and cost-total bugs
- bSDD classification errors and rate limits
- Diffing models (IfcDiff misses or over-reports changes)
- AI/LLM connectors (Claude, ifcmcp) asked about as a new theme in 2026

## What people want
- Open any vendor IFC without crashes and get the same geometry as other viewers
- Trustworthy numbers: quantities that match commercial checkers
- A way to automate batch jobs (headless drawings, patching, validation) from scripts
- Use IFC as a database: query, diff, validate against IDS, hand over COBie
- Georeferenced multi-building federation that survives save/reopen
- Guidance on how to model semantics (balcony, facade, structural analysis) rather than just geometry
- Chat-driven editing of IFC with an agent (ifcmcp)

## How people write here
- Bug template structure: "Bug Description", repro steps, pasted traceback and environment dump; little prose.
- Short, screenshot-led: "Attributes get messed up", "bug".
- Polite openers on older or beginner posts: "I wanted to reach out", "Hi all".
- Developers write longer numbered lists with code and ask "best practices".
- Frustration is mild and often self-deprecating: "Or am I just too stupid".
- Jargon: "proxy", "pset", "QTO", "false origin", "federate", "Gesamtmodell" (German code-switch in file names).
- Comparisons to other tools are common: "BIMcollab opens it", "Solibri gives".
- Typical omissions: IFC schema version, exporter version; maintainers reply "please share the file".
- Illustrative fragments: "IFC Files do not open (Filesize??)", "it shouldn't crash IMO", "Any way around?".

## Local ecosystem
- IfcOpenShell: https://github.com/IfcOpenShell/IfcOpenShell ; docs https://docs.ifcopenshell.org
- Bonsai (formerly BlenderBIM): https://docs.bonsaibim.org
- OSArch community: https://community.osarch.org
- buildingSMART IFC4X3 docs: https://ifc43-docs.standards.buildingsmart.org ; IDS: https://github.com/buildingSMART/IDS ; bSDD
- Competing/adjacent: xBIM, web-ifc, BIMcollab, Solibri, BIM Vision, Revit IFC exporter, Vectorworks, Archicad
- BIM for Bridges US: https://bimforbridgesus.com
- ifcmcp (agent interface shipped with ifcopenshell), referenced in discussion 8027

## Notable sources
- https://github.com/IfcOpenShell/IfcOpenShell/issues/6283 Revit IFC rendering problems
- https://github.com/IfcOpenShell/IfcOpenShell/issues/2025 large IFC datasets
- https://github.com/IfcOpenShell/IfcOpenShell/issues/7632 big files freeze
- https://github.com/IfcOpenShell/IfcOpenShell/issues/7259 Revit attributes lost
- https://github.com/IfcOpenShell/IfcOpenShell/issues/6655 invalid placement
- https://github.com/IfcOpenShell/IfcOpenShell/issues/3115 annotation context
- https://github.com/IfcOpenShell/IfcOpenShell/issues/6120 Revit wall openings
- https://github.com/IfcOpenShell/IfcOpenShell/issues/8205 georeferenced drawings and BCF
- https://github.com/IfcOpenShell/IfcOpenShell/issues/7016 linked georeferenced plan
- https://github.com/IfcOpenShell/IfcOpenShell/issues/9235 Gross vs Net area
- https://github.com/IfcOpenShell/IfcOpenShell/issues/7095 IDS duplicate psets
- https://github.com/IfcOpenShell/IfcOpenShell/issues/7856 IDS USERDEFINED
- https://github.com/IfcOpenShell/IfcOpenShell/issues/10119 IfcConvert >2 GiB
- https://github.com/IfcOpenShell/IfcOpenShell/issues/7152 BCF with BIMcollab
- https://github.com/IfcOpenShell/IfcOpenShell/issues/5926 COBie tabs
- https://github.com/IfcOpenShell/IfcOpenShell/issues/8214 IfcDiff
- https://github.com/IfcOpenShell/IfcOpenShell/discussions/8134 slow save and print
- https://github.com/IfcOpenShell/IfcOpenShell/discussions/8102 dimensions for QTO
- https://github.com/IfcOpenShell/IfcOpenShell/discussions/8027 Claude connector
- https://github.com/IfcOpenShell/IfcOpenShell/discussions/7912 semantic ambiguity
- https://github.com/IfcOpenShell/IfcOpenShell/discussions/7749 structural model from scratch
- https://github.com/IfcOpenShell/IfcOpenShell/discussions/7714 alignment representation
- https://github.com/IfcOpenShell/IfcOpenShell/discussions/9433 feature elements on import
- https://github.com/IfcOpenShell/IfcOpenShell/discussions/9407 room system complaint

## Gaps
- No Revit-side (Revit plugin) issues; those live in the Autodesk repos, covered by other cells.
- Many answers were read only from first comment; some "answer_summary" values note unresolved status.
- Several gh issue searches returned empty (rate limiting on multi-word queries), so some topics (IFC4X3 alignment, web-ifc, memory) were thinly sampled.
- WebFetch of docs.ifcopenshell.org/ifcmcp.html gave no usable content; ifcmcp details unconfirmed.
- Fewer than 25 distinct web searches; GitHub CLI queries (about 60 sub-queries) used instead. No suspicious sites encountered. Poster names omitted.
