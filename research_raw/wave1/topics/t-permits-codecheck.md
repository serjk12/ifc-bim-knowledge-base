# IFC in building permits and automated code checking (Singapore, Estonia, Norway, Japan, Korea, China, Russia, Dubai)
Cell: t-permits-codecheck · Languages: en (real); ru, zh, ja, ko, de, es, fr, pt, it (synthetic only) · Collected: 2026-11-06 · Records: 4 real / 16 synthetic · Communities covered: GitHub (buildingSMART IFC4.x-development, OpenPermit), OSArch forum, Singapore CORENET X official portal

**This cell is INCOMPLETE.** The shared WebSearch budget ran out before any useful search ran (all search calls were refused). Only a handful of direct page fetches and gh queries were possible. Treat this as a thin seed, not a survey. Re-run after raising the search limit.

## Top themes (ranked by frequency, only from what was seen)
- Regulation-relevant properties missing from the IFC schema (e.g. stair width) blocking automated rule checks.
- Hybrid approach debate: property-based checks (fast, explicit) vs geometric rule checking (robust, complex).
- National submission portals defining their own IFC profile (IFC+SG, mapping file, identified components).
- IDS-based validation of deliveries and delivery comparison as the practical "does the model contain required info" step.
- Readiness self-checks and model checkers before official submission.

## What people want
- A pre-submission check that the IFC has the classes and properties the authority expects.
- Schema support so accessibility and fire-safety quantities can be read directly.
- Reports usable in review or coordination meetings, grouped, not long flat lists.

## How people write here
- Schema proposals: formal, polite, bulleted benefits ("Support automated rule-based compliance checks").
- Practitioner tool posts: framed as three plain questions ("What changed since the previous delivery?").
- Official portals: bureaucratic labels (IFC+SG, mapping file, identified components, Model Checker).
- Native-language phrasing in the synthetic records is invented, not observed; verify before relying on it.

## Local ecosystem
- Singapore: CORENET X, agencies BCA, LTA, NEA, NParks, PUB, SCDF, URA; IFC+SG; https://info.corenet.gov.sg/general/corenet-x.aspx
- GitHub projects seen by search only (not opened): chunyen93/ifcgref-corenetx (IFC georeference inspector with CORENET X checks), OrvenBentleySystems/sg-ifc-microstation-eap (Singapore IFC plugin for MicroStation), noddlesskcho/ifc-sg-site-object-repair.
- Open source: TopologicPy / Syntopy (IDS check, compare), OSArch/Bonsai community.
- Not covered: Estonia, Norway, Japan, Korea, China, Russia, Dubai.

## Notable sources
- https://github.com/buildingSMART/IFC4.x-development/issues/976 (stair width, code checking, CORENET X)
- https://info.corenet.gov.sg/general/corenet-x.aspx (CORENET X portal)
- https://community.osarch.org/discussion/3768/syntopy-ifc-apps-powered-by-topologicpy (IDS check tools)
- https://github.com/SheetPros/OpenPermit/issues/27 (permitting automation initiatives, title only)
- https://github.com/chunyen93/ifcgref-corenetx (repo, not opened)

## Gaps
- WebSearch budget exhausted: no searches in any language, no native-language communities (dwg.ru, csdn, zhihu, qiita, etc.) reached.
- Requested 25-50 real records; only 4 obtained (1 snippet-only). Requested 12-20 synthetic: 16 written, not grounded in observed native phrasing.
- buildingSMART Regulatory Room page returned 403; CORENET IFC+SG subpages returned 404 or empty; buildingSMART forum listing had no on-topic threads.
- No suspicious sites encountered.
