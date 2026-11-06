# Facility managers, owners/clients and reviewers/authorities: handover, compliance, checking deliverables
Cell: p-fm-owner-reviewer · Languages: English (native-language searches NOT possible, see Gaps) · Collected: 2026-11-06 · Records: 37 real / 19 synthetic · Communities covered: community.osarch.org (IDS tag), forums.buildingsmart.org (Users category), GitHub issues (IfcOpenShell, buildingSMART/IDS, IDS-Audit-tool)

## Top themes (ranked by frequency)
- IDS (Information Delivery Specification): writing, syntax, regex, cardinality, and running it to accept or reject deliverables
- Checking contractor deliverables against client requirements and returning a fail list
- Batch validation of many IFC files against many IDS files, with reports (HTML, ODS, BCF)
- Proxies and wrong classes as a deliverable quality check (IfcBuildingElementProxy)
- COBie / FM handover export: missing tabs, empty Systems tab, Excel vs ODS errors
- Manufacturer and asset data (Pset_ManufacturerTypeInformation, serial, warranty) for CAFM
- Redundant or duplicated properties across psets versus single source of truth
- IFC2x3 vs IFC4 quirks in checking (occurrence type mapping, PredefinedType)
- Partial scope deliveries (refurbishment: new vs existing elements)
- Understanding Qto expectations, actor/roles, GUID stability across versions
- Heavy files / polygon counts that make review hard
- Readable, non-coder-friendly reports of requirements and check results

## What people want
- Owners and reviewers: a quick pass/fail with counts and a list of offending elements they can send back, without scripting.
- FMs: spaces, systems, equipment with manufacturer, model, serial and warranty in a CAFM-importable sheet (COBie or Excel).
- Coordinators serving owners: repeatable, scheduled batch checks (70 models x 6 IDS) with reports.
- Everyone: clarity on what a requirement means (cardinality, empty strings, which pset) and trust that the checker is right.

## How people write here
- Register: collegial, polite in forums; terse dev-style titles on GitHub.
- Users openly say they lack coding skills ("no coding experience", "basic scripting"); they want GUI or ready scripts.
- Jargon: IDS, ifctester, Bonsai/BlenderBIM, IfcFM, COBie tabs, pset, proxy, applicability/requirements/facet.
- Openers: "G'day all", "Hi Everyone"; closers thank-you or "Cheers".
- Context given: software version (Blender 4.0.2, add-on build), IFC version, attached files (xlsx, error log); often omitted: the actual IFC file.
- Frustration shows as "I will go crazy" repeating manual checks; ChatGPT-failed attempts are mentioned.
- Fragments: "5 out of standard 20 tabs missing"; "only the PyPI page documents it"; "prefer to receive only what is requested".
- No non-English register could be sampled (see Gaps); synthetic de/ru/es/fr records are written from general knowledge of the register, unverified.

## Local ecosystem
- buildingSMART International: IDS standard (https://github.com/buildingSMART/IDS), IDS Audit tool (https://github.com/buildingSMART/IDS-Audit-tool), forums (https://forums.buildingsmart.org/), bSDD.
- IfcOpenShell / IfcTester / Bonsai (BlenderBIM) / IfcFM for COBie and IDS (https://github.com/IfcOpenShell/IfcOpenShell).
- OSArch community (https://community.osarch.org/) with IDS tag (https://community.osarch.org/discussions/tagged/ids).
- COBie UK (Uniclass 2015) and US (OmniClass) templates mentioned.
- Prairie Sky Consulting example files used for FM tests (mentioned in a GitHub issue).

## Notable sources
- https://community.osarch.org/discussion/2658/non-compliance-check : checking IFC against IDS, redundant data debate
- https://community.osarch.org/discussion/2273/ifctester-script-for-testing-several-ifcs-with-several-ids : batch IDS validation
- https://community.osarch.org/discussion/2969/filtering-new-building-components-in-ids-for-refurbishment-projects : partial scope
- https://community.osarch.org/discussion/3303/ids-check-for-ifcbuildingelementproxy-question : proxy check
- https://community.osarch.org/discussion/2678/view-ids-xml-file-as-simplified-text-human-friendly-readable-ids : readable IDS
- https://community.osarch.org/discussions/tagged/ids : 27 IDS threads
- https://github.com/IfcOpenShell/IfcOpenShell/issues/5926 : COBie missing tabs
- https://github.com/IfcOpenShell/IfcOpenShell/issues/6068 : COBie Systems empty
- https://github.com/IfcOpenShell/IfcOpenShell/issues/3901 : IfcFM Excel export error
- https://github.com/IfcOpenShell/IfcOpenShell/issues/3978 : Revit exporter versions, COBie properties
- https://github.com/IfcOpenShell/IfcOpenShell/issues/7095 : manufacturer pset reporting
- https://github.com/buildingSMART/IDS/issues/403 : empty string and cardinality
- https://github.com/buildingSMART/IDS/issues/189 : property in unknown pset
- https://github.com/buildingSMART/IDS-Audit-tool/issues/56 : IFC2x3 occurrence mapping
- https://forums.buildingsmart.org/c/users/6 : Users category
- https://forums.buildingsmart.org/t/qto-properties-expectations/6298 : Qto expectations

## Gaps
- The WebSearch budget for the whole run was exhausted at the start of this cell, so NO searches were possible: no native-language (Russian, Chinese, Spanish, Portuguese, German, French, Japanese, Korean, Italian) communities were sampled, and no Autodesk forum, Stack Overflow, Reddit, Graphisoft or national-authority material was found.
- Only direct fetches and the gh CLI worked; GitHub search hit a rate limit partway.
- 28 of 37 real records have snippet/title-level evidence only (5 OSArch + 4 GitHub pages were read).
- Few genuine FM or authority voices were found; most askers are coordinators/tool users. Needs a re-run with search quota restored.
- No suspicious sites encountered.
