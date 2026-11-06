# GUID stability, model versioning, comparing versions (IfcDiff), change tracking
Cell: t-guid-versioning · Languages: English (real sources), Japanese (1 real); ru/zh/de/es/pt/fr/ko/it only as synthetic · Collected: 2026-11-06 · Records: 30 real / 14 synthetic · Communities covered: community.osarch.org, GitHub (Autodesk/revit-ifc, IfcOpenShell), qiita.com

## Top themes (ranked by frequency)
- GlobalIds regenerated between exports, so a GlobalId-only diff shows "everything deleted and re-added" (GUID churn)
- Revit exporter GUID determinism: same GUID after delete, copies of files produce duplicates, "Reset Document GUID" missing
- Duplicate GlobalIds across copied or split files in federated projects
- IfcDiff correctness and usability: false positives (pset STEP ids), missed geometry changes, crashes, 1 hour runtime on 10 models
- Matching without GUIDs: type + name/Tag + placement tolerance + geometry hash/bounding box
- Linked-model federated export producing new GUIDs (hash of link instance GUID + element GUID), breaking BCF traceability
- Design options, groups and type elements losing or duplicating IfcGUID
- Round trips: linking/reloading an updated IFC (shared parameter GUIDs, duplicates on re-import, incremental reload)
- Version control for IFC (git merge, STEP ids as unstable identity, ifcmerge, IfcGit)
- UniqueId to IFC GUID conversion rules for Revit API developers
- GUID persistence as buildingSMART certification requirement and basis for BCF, 4D caches, IDS checks

## What people want
- A trustworthy "what changed since last revision" report (added/deleted/modified, per storey or discipline) for coordination meetings.
- Stable identifiers so BCF issues, schedules, 4D links and external databases survive re-export.
- Diff tolerant of regenerated IDs, with tolerance for tiny geometry moves and a way to review uncertain matches.
- Controls: store GUID in a parameter, regenerate random GUIDs, keep original GUIDs for linked models.
- Merge/update an existing model with a revised IFC without duplicates.

## How people write here
- Register: developer/English forum voice, short and technical; GitHub issues use repro steps and templates with prefixes "PR:", "ENH:", "INQ:".
- Length: titles short; bodies numbered steps, versions, tracebacks. Hedged openers ("am I misusing X or is this a bug?").
- Jargon: "GUID churn", "GlobalId", "IfcGUID", "STEP ids", "Reload", "diff", "orphaned elements", "geometry hash".
- Context given: Revit year, exporter version (e.g. 22.5.2.0), OS, Blender/Bonsai version; often omit schema version and file.
- Tone: frustrated about traceability ("defeats the purpose of a GUID"), curious in design threads.
- Fragments: "Revit regenerates GlobalIds for some categories"; "nothing really changed" (typical); "should the object retain their GlobalID?".
- Japanese blogs: tutorial style with C# code samples, precise rules.
- Synthetic prompts (ru/zh/de/...) mimic brevity and mixed terms: "ифс", "guid опять поменялись", "GUID全不一样".

## Local ecosystem
- Autodesk revit-ifc exporter (open source): https://github.com/Autodesk/revit-ifc
- IfcOpenShell / Bonsai / IfcDiff, ifcmerge, ifcpatch, IfcClash: https://github.com/IfcOpenShell/IfcOpenShell , https://docs.ifcopenshell.org
- OSArch community: https://community.osarch.org
- buildingSMART (GUID certification requirement, BCF, IDS): https://www.buildingsmart.org
- TopologicPy / Syntopy (TopologicCompare) and a commercial browser diff tool (web-ifc) mentioned on OSArch
- Japanese Revit API blogger on Qiita: https://qiita.com/Takashi_Kasuya

## Notable sources
- https://community.osarch.org/discussion/3616/browser-based-ifc-clash-version-diff-how-would-you-group-clashes-and-handle-guid-churn
- https://community.osarch.org/discussion/comment/12255#Comment_12255
- https://community.osarch.org/discussion/comment/11630#Comment_11630
- https://community.osarch.org/discussion/comment/8352#Comment_8352
- https://community.osarch.org/discussion/comment/13211#Comment_13211
- https://community.osarch.org/discussion/3537/ifcdiff-in-bonsai-with-property-enabled-results-in-error
- https://community.osarch.org/discussion/3768/syntopy-ifc-apps-powered-by-topologicpy
- https://github.com/Autodesk/revit-ifc/issues/521
- https://github.com/Autodesk/revit-ifc/issues/617
- https://github.com/Autodesk/revit-ifc/issues/378
- https://github.com/Autodesk/revit-ifc/issues/512
- https://github.com/Autodesk/revit-ifc/issues/314
- https://github.com/Autodesk/revit-ifc/issues/408
- https://github.com/Autodesk/revit-ifc/issues/164
- https://github.com/Autodesk/revit-ifc/issues/825
- https://github.com/Autodesk/revit-ifc/issues/880
- https://github.com/IfcOpenShell/IfcOpenShell/issues/8412
- https://github.com/IfcOpenShell/IfcOpenShell/issues/9610
- https://github.com/IfcOpenShell/IfcOpenShell/issues/8905
- https://qiita.com/Takashi_Kasuya/items/97899d15e7ec0186eecf

## Gaps
- The WebSearch budget was exhausted before any search ran (0 successful searches), and the GitHub CLI hit a rate limit. Everything came from direct page fetches, including GitHub web search pages and OSArch/Qiita internal search.
- Not accessible: forums.autodesk.com (403), community.graphisoft.com (403), stackoverflow.com and the Stack Exchange API (blocked), forums.buildingsmart.org search (empty), dwg.ru search (garbled/no results), Habr (results did not load), cnblogs search (404), Zenn (no results).
- No real non-English sources except one Japanese Qiita article; Russian, Chinese, German, Spanish, Portuguese, French, Korean and Italian communities are not covered by real records. Synthetic records in those languages are guesses at style and need a follow-up pass.
- Several records are snippet-only (osarch 3580, 3678, 3303, 3782, 28133, 28448, 13484, revit-ifc 909, IfcOpenShell 9312, 9830).
- No suspicious or pirated sites were encountered.
