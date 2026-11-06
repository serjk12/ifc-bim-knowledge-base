# Singapore: CORENET X and IFC-SG questions and guides

Cell: en-sg-corenetx · Languages: English · Collected: 2026-11-06 · Records: 14 real / 14 synthetic · Communities covered: GitHub practitioner tools (Singapore BIM), info.corenet.gov.sg

**INCOMPLETE CELL.** The WebSearch budget was exhausted before any search ran (all 4 attempts refused). Only about 12 WebFetch/gh calls were made, against a target of 25+ and 30-60 real records. The 14 real records come from tool READMEs and the official site, not from forum threads with real askers. Re-run this cell once search quota is restored.

## Top themes (ranked by frequency)
- Model Checker rejection codes (IFC0000101 not IFC4, IFC0000104 invalid/incomplete data)
- IFC4 requirement vs IFC2x3 exports
- Geometry defects: missing ContextOfItems, empty IfcClosedShell
- IFC+SG property sets and required properties (SGPset_*), value type and unit format
- Duplicate or old shared parameters in Revit versus approved IFC+SG ones
- Georeferencing: SVY21 / EPSG:3414, IfcMapConversion, SITEBOUNDARY
- Site objects wrongly exported as IfcSpace
- Spaces without geometry or area
- Spatial containment: elements not in a storey, duplicate GlobalIds
- Missing derived structural properties (stair risers/treads, slab thickness, MaterialGrade)
- Pre-submission checking tools versus the official checker; Code of Practice editions (COP 3.1, COP 4)
- Non-Revit authoring tools (Archicad, Tekla, MicroStation) and the Excel mapping file

## What people want
- Pass the CORENET X Model Checker on the first submission and avoid resubmission delays.
- Find the exact elements (GlobalId, name) that cause an error, and repair them without re-exporting everything.
- Bulk-fix property units, types and values to match the IFC+SG mapping.
- Pre-validate offline before uploading, because uploads of confidential models are a concern.
- Use their own authoring tool, not only Revit.

## How people write here
- Sources seen are tool READMEs, so the register is technical and terse. Genuine forum voice was not obtained.
- Error codes and portal messages are quoted verbatim ("IFC0000104", "CfsFaces must not be empty").
- Exact entity and pset names are used with CamelCase (IfcGeographicElement, SGPset_Beam).
- Jargon: "CX" (CORENET X), "IFC+SG" or "IFC-SG" (both spellings used), "COP" (Code of Practice), "shared params", "GUID".
- Synthetic prompts are lowercase, missing context, deadline pressure ("cx submission tomorrow").

## Local ecosystem
- BCA / CORENET X portal and info site: https://info.corenet.gov.sg/ (Code of Practice, IFC+SG Excel mapping file, BIM authoring tools, Model Checker, circulars, FAQ). Agencies: BCA, LTA, NEA, NParks, PUB, SCDF, URA.
- FAQ and support hub: https://support.corenet.gov.sg/hc/en-us (403 on fetch).
- Submission Portal user manual: go.gov.sg/cx-sp-user-manual (not opened).
- Community tools: ifcgref-corenetx, ifcsg-precheck, IFC-Repair-Studio, IFCSG-Parameter-Consolidator, ifc-sg-site-object-repair, sg-ifc-microstation-eap (all GitHub, unofficial).

## Notable sources
- https://info.corenet.gov.sg/ — official hub, IFC+SG sections
- https://github.com/noddlesskcho/IFC-Repair-Studio — IFC0000101/IFC0000104 repair
- https://github.com/noddlesskcho/IFCSG-Parameter-Consolidator — Revit duplicate shared parameters
- https://github.com/noddlesskcho/ifc-sg-site-object-repair — site objects and stair flights
- https://github.com/LUOaini1213/ifcsg-precheck — pre-submission checker and auto-fill
- https://github.com/chunyen93/ifcgref-corenetx — georeferencing check
- https://github.com/OrvenBentleySystems/sg-ifc-microstation-eap — MicroStation checker, COP 3.1/4
- https://github.com/samsonleegh/revit-coach — LLM Revit coach with SG context

## Gaps
- No web searches possible (budget exhausted): no Autodesk/Graphisoft forum, LinkedIn, Reddit or blog threads found.
- support.corenet.gov.sg returned 403; Autodesk forums returned 403; several info.corenet.gov.sg sub-pages 404 (guessed URLs).
- Real records are tool descriptions, not user questions; year values (2026) are approximate. Archicad and Tekla IFC-SG specifics not researched.
- No suspicious sites encountered. Nothing downloaded or executed.
