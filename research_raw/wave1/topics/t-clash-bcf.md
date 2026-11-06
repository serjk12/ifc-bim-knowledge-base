# Clash detection and coordination with IFC and BCF (Navisworks, Solibri, BIMcollab, Revizto, ACC)

Cell: t-clash-bcf · Languages: English (real sources); Russian, Chinese, Spanish, Portuguese, German, French, Japanese, Korean, Italian only as synthetic prompts · Collected: 2026-11-06 · Records: 30 real / 16 synthetic · Communities covered: GitHub issues (IfcOpenShell, buildingSMART BCF-XML and BCF-API, That Open engine_components, ifc-lite, Autodesk revit-ifc, small Navisworks/clash projects), community.osarch.org

NOTE: the WebSearch budget ran out before the first query returned, so no web search was done. All material comes from `gh` issue search and direct WebFetch of known pages. Real records are heavily developer-skewed (open-source tool authors), not a representative sample of Navisworks/Solibri end users.

## Top themes (ranked by frequency)
- BCF files that one tool exports and another cannot import: Solibri imports 0 topics, BIMcollab says "no viewpoint to zoom to"
- BCF spec ambiguity: file naming (viewpoint.bcfv, snapshot.png), folder entries, mandatory snapshots, GUID mismatches, 2.1 vs 3.0 support
- Open-source clash engines (ifcclash, Bonsai) returning wrong, missing or empty results ("0 clashes found")
- Missed clashes on touching or coplanar geometry, and false positives with "allow touching" or hidden representations
- Clash point and location problems: units (feet vs mm), false origin, two points per clash instead of a volume
- Result grouping: hundreds of clashes from one misplaced run, grouping by system, storey or source object
- GUID churn between revisions (Revit regenerates GlobalIds), so diffing clash sets across versions fails
- Exporting clash results: BCF viewpoint without the colliding elements selected, spreadsheet export, clipping planes in viewpoints
- Clashing many linked or federated models at once
- Free alternatives to paid Solibri / BIMcollab for viewing and creating BCF
- Revit IFC exporter updates breaking Navisworks IFC loading (IFC2x3 vs IFC4)
- Non-building cases: clearance volumes from IFC4x3 alignments

## What people want
- Reliable BCF round-trips between any pair of tools, with viewpoints, snapshots and selected components intact
- Clash tools that group, filter and dismiss false positives (saved rules per project, tolerance, discipline rule-sets)
- Clash points and volumes in correct project and world coordinates
- Version-to-version clash tracking (new, resolved, persistent) despite changing GUIDs
- Free or open BCF/clash tooling, and scriptable clash APIs
- Official clarification of the BCF spec where implementers disagree

## How people write here
- GitHub bug-report register: short title, minimal repro, screenshots instead of text, files "cannot be shared" (client confidentiality).
- Forum posters are chattier: "G'day all", "Thanks in advance!", lettered question lists (a to f).
- Beginners state their background first: "beginner... AutoCAD 2D experience".
- Typical fragments: "0 clashes found even with a deliberate clash", "imports 0 topics, no error", "Any updates?", "same issue, updated to latest build".
- Tool names are stacked as comparison lists (Solibri, BIMcollab, BIM+, usBIM) to show where it works and where not.
- Typos in titles occur ("shapshot"); verbs like "clash" are used for both noun and process.
- Synthetic non-English prompts (not from real sources) imitate lowercase, short-command style: "прогони коллизии вентиляция vs балки", "干渉チェックして".

## Local ecosystem
- buildingSMART International: BCF-XML and BCF-API specs, https://github.com/buildingSMART/BCF-XML , https://github.com/buildingSMART/BCF-API
- IfcOpenShell (ifcclash, bcf library) and Bonsai: https://github.com/IfcOpenShell/IfcOpenShell ; OSArch community: https://community.osarch.org
- That Open Company engine_components (BCFTopics): https://github.com/ThatOpen/engine_components
- ifc-lite (browser viewer with clash and BCF): https://github.com/LTplus-AG/ifc-lite
- Autodesk Revit IFC exporter: https://github.com/Autodesk/revit-ifc
- Commercial tools mentioned: Navisworks, Solibri, BIMcollab (Zoom/Nexus), BIM+, usBIM
- Not reached: Revizto, ACC, national bodies, local-language software (no regional sources accessed)

## Notable sources
- https://github.com/IfcOpenShell/IfcOpenShell/issues/4594 missed coplanar wall clash
- https://github.com/IfcOpenShell/IfcOpenShell/issues/5357 flipped a/b results
- https://github.com/IfcOpenShell/IfcOpenShell/issues/6109 Bonsai clash set bugs
- https://github.com/IfcOpenShell/IfcOpenShell/issues/6138 clash point semantics
- https://github.com/IfcOpenShell/IfcOpenShell/issues/7178 feet vs mm clash location
- https://github.com/IfcOpenShell/IfcOpenShell/issues/7152 BIMcollab no viewpoint to zoom
- https://github.com/IfcOpenShell/IfcOpenShell/issues/5471 clearance volume from alignment
- https://github.com/IfcOpenShell/IfcOpenShell/issues/8224 ifcclash AssertionError
- https://github.com/IfcOpenShell/IfcOpenShell/issues/4887 Solibri BCF 3 import
- https://community.osarch.org/discussion/2736/clash-detection-how-to/p1
- https://community.osarch.org/discussion/3616/browser-based-ifc-clash-version-diff-how-would-you-group-clashes-and-handle-guid-churn
- https://community.osarch.org/discussion/3579/clash-detection-error
- https://community.osarch.org/discussion/3713/bonsaiviewer-and-clash-detection
- https://github.com/buildingSMART/BCF-XML/issues/399 snapshots mandatory?
- https://github.com/buildingSMART/BCF-XML/issues/358 topic GUID mismatch
- https://github.com/LTplus-AG/ifc-lite/issues/6459 Solibri imports 0 topics
- https://github.com/LTplus-AG/ifc-lite/issues/4806 BCF without colliding objects
- https://github.com/LTplus-AG/ifc-lite/issues/3612 BCF import fails in three tools
- https://github.com/LTplus-AG/ifc-lite/issues/4099 free BCF viewer question
- https://github.com/Autodesk/revit-ifc/issues/580 Navisworks IFC import after exporter update
- https://github.com/ThatOpen/engine_components/issues/825 BCF export well-formedness

## Gaps
- WebSearch budget was exhausted at the first call; no general web search was possible and no search-engine workaround was used.
- No native-language real records (ru/zh/es/pt/de/fr/ja/ko/it): dwg.ru and cnblogs returned 404, Qiita search gave nothing relevant, Autodesk forums returned 403, buildingSMART forums gave no content, Stack Overflow is blocked for fetch. Non-English entries are synthetic only.
- Not covered: Revizto, ACC/BIM 360 issues, Navisworks forum threads, reddit, vendor knowledge bases, official/government rules.
- GitHub API rate limit was hit late; about 12 real records are snippet-only (title level).
- No suspicious or pirated sites were encountered.
