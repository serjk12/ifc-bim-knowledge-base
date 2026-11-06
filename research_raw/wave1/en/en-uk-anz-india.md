# UK, Australia/NZ, India practitioners: IFC deliverables, ISO 19650, Uniclass, NATSPEC
Cell: en-uk-anz-india · Languages: English · Collected: 2026-11-06 · Records: 16 real / 15 synthetic · Communities covered: GitHub issue trackers (Autodesk/revit-ifc, IfcOpenShell/Bonsai, buildingSMART/IDS), UK IMI Framework hub. This cell is INCOMPLETE (see Gaps).

## Top themes (ranked by frequency)
- Classification (Uniclass 2015, Assembly Code, ClassificationCode) not exporting cleanly from Revit to IFC
- COBie / FM handover from IFC (missing sheets, empty Systems tab, export errors)
- Property requirements from EIR vs IDS (property named but Pset unstated)
- Revit IFC exporter version regressions and data-structure changes
- Empty or missing parameters not exported to IFC
- Phasing, linked models and single-file export limits
- Need for local classification systems beyond Uniformat
- Programmatic extraction of Psets to Excel

## What people want
- Pass a client's EIR or IDS check without manual rework
- Hand over COBie-like asset data from IFC for AIM
- Get Uniclass codes into IFC reliably, via Revit or Bonsai
- Know why an export differs between exporter versions
- Quick counts, missing-data lists and diffs on issued models before an information delivery deadline

## How people write here
- GitHub style: short, polite, often templated (Summary / Current Behaviour / Requested Enhancement) or one-liners ("Any idea what's happening here?").
- Standards-aware terms: EIR, AIM, COBie, Uniclass Ss/Pr, "nonconformity", "issue" (information delivery).
- Often omit version, file and model context; paste raw logs or screenshots.
- Opener "I know this is not a new topic"; closer "Thank you in advance!".
- Synthetic prompts mimic UK site/office shorthand: "before the issue tonight", "loads of proxies", "pls".

## Local ecosystem
- UK: IMI Framework (BSI and nima), https://imiframework.org/ (ukbimframework.org redirects here); ISO 19650-1 to -5 via BSI shop; PAS 1192-6; BS 8536; Uniclass 2015 (NBS); COBie.
- Australia: NATSPEC BIM Portal and National BIM Guide, https://bim.natspec.org (not read in detail).
- Open source: IfcOpenShell / Bonsai https://github.com/IfcOpenShell/IfcOpenShell ; Autodesk revit-ifc https://github.com/Autodesk/revit-ifc ; buildingSMART IDS https://github.com/buildingSMART/IDS

## Notable sources
- https://github.com/Autodesk/revit-ifc/issues/456 Uniclass via Classification Manager to IFC
- https://github.com/Autodesk/revit-ifc/issues/489 Duplicate Uniclass classification reference
- https://github.com/Autodesk/revit-ifc/issues/509 Assembly Code classification regression
- https://github.com/Autodesk/revit-ifc/issues/856 Non-Uniformat classification via Assembly Code
- https://github.com/Autodesk/revit-ifc/issues/439 Linked RVT to single IFC
- https://github.com/Autodesk/revit-ifc/issues/704 Phasing in IFC
- https://github.com/Autodesk/revit-ifc/issues/963 Empty parameters not exported
- https://github.com/IfcOpenShell/IfcOpenShell/issues/5926 COBie missing tabs
- https://github.com/IfcOpenShell/IfcOpenShell/issues/6068 COBie Systems tab empty
- https://github.com/IfcOpenShell/IfcOpenShell/issues/5702 COBie export error
- https://github.com/IfcOpenShell/IfcOpenShell/issues/3978 Exporter version differences
- https://github.com/IfcOpenShell/IfcOpenShell/issues/7038 Classification display request
- https://github.com/buildingSMART/IDS/issues/189 EIR property without Pset
- https://github.com/buildingSMART/IDS/issues/176 AND conditions in IDS
- https://github.com/buildingSMART/IDS/issues/223 Classification facet behaviour
- https://imiframework.org/ UK ISO 19650 hub

## Gaps
- The WebSearch budget for the turn was exhausted before any search ran (all 6 attempts refused), so no forum/LinkedIn/Indian community/Australian forum discovery happened. Only direct fetches and the GitHub CLI were used.
- Real records are 16 instead of 30-60; none are from Australian, NZ or Indian posters specifically (regional origin of GitHub posters is unverified). thenbs.com article guess returned 404; NATSPEC homepage mentions no IFC resources; TfNSW, ukbimframework Uniclass/COBie UK pages, and India-specific sources were not reached.
- Should be re-run once search budget is available (seed queries: IFC deliverable ISO 19650, Uniclass IFC, NATSPEC IFC, TfNSW Digital Engineering IFC, India BIM IFC).
- No suspicious sites encountered.
