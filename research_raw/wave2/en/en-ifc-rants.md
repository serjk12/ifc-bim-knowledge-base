# Complaints and debates about IFC quality between consultants (rants, opinion threads)
Cell: en-ifc-rants · Languages: English · Collected: 2026-11-06 · Records: 31 real / 17 synthetic · Communities covered: GitHub issue trackers (Autodesk/revit-ifc, IfcOpenShell), buildingSMART forums, OSArch community

NOTE: the WebSearch budget was exhausted at the start of this run, so Reddit, LinkedIn and blogs could not be searched. Material comes from direct fetches of forum pages, forum-internal search (OSArch) and the GitHub CLI. 3 of the 31 real records are snippet-only (title seen, body not read).

## Top themes (ranked by frequency)
- Wrong or generic IFC class: everything lands in IfcBuildingElementProxy (fascias, sweeps, curtain wall parts) and IfcExportAs does not help.
- Silent data loss on export: elements skipped, type properties or material psets missing, IFC4 drops what IFC2x3 keeps.
- Units and quantities wrong: IfcReal instead of measure types, mm-project BaseQuantities off, feet/304.8 bugs.
- Georeferencing: true north vs grid north conflated, project north differs between link methods.
- Bloated geometry and file size: fillets meshed into huge triangle counts, manufacturer objects too detailed, slow export with properties.
- Viewer/importer inconsistency: Navisworks drops elements, Revit mis-places windows or fails on valid IFC, so clash checking is untrusted.
- GlobalId problems: duplicates across files, unstable IDs breaking change tracking.
- Schema noncompliance: ObjectType filled with Family:Type, Name/Reference misuse, Reference deprecated.
- Types vs instances: one-off types (fabrication ducts), authoring tools with no type support (Allplan).
- Consultants unable or unwilling to supply precise classes, forcing receivers to build import mapping tables.
- Vendor behaviour and certification: MVD certification costly, vendors leave gaps, Revit stagnation.
- Debate: native vs IFC, open tools (Bonsai/IfcOpenShell) opening files Revit chokes on.

## What people want
- IFC that is correct without hand-tuning: right classes, units, psets, georef.
- A checklist or guide to hand to consultants so deliveries stop being junk.
- Automated validation and requirements checking (IDS, validation service, quality reports).
- Logs and diagnostics from exporters instead of silent failure.
- Diffing and GUID stability between deliveries.
- Lighter geometry, LOD control for manufacturer content.
- Contract language that makes IFC quality enforceable.

## How people write here
- GitHub issues: structured (problem, versions, steps), very technical, sometimes tabular benchmarks; frustration shows in one line ("STILL no fix!").
- Forum posts: informal openers ("Hi everyone", "G'day all"), IMHO, rhetorical questions, anecdotes (fire extinguishers "too realistic").
- Jargon: proxy, DTV (Design Transfer View), CV2.0, RV, pset, Qto, GUID, IfcExportAs, mapping table, "native".
- Emotional markers: capitals and exclamation ("Systematic(!) RevitIFCUnitBug!"), sarcasm about vendors, "unacceptable in a production environment".
- Context given: Revit version, exporter version, MVD, units; often omitted: the receiving software, the file itself.
- Short fragments: "no solution, that's the limit of Revit"; "2578 duplicate GlobalIds"; "clients will see generic proxy elements".
- Many posts are by BIM coordinators who receive models, so wording is about "consultants" and "clients".

## Local ecosystem
- buildingSMART International, forums and Validation Service: https://forums.buildingsmart.org
- Autodesk open-source Revit IFC exporter: https://github.com/Autodesk/revit-ifc
- IfcOpenShell / Bonsai (formerly BlenderBIM): https://github.com/IfcOpenShell/IfcOpenShell
- OSArch community: https://community.osarch.org
- OpenBIM Pledge (consultant contract tiers): https://community.osarch.org/discussion/comment/24566#Comment_24566
- Standards named: IFC2x3 CV2.0, IFC4 Reference/Design Transfer View, IFC4.3, IDS, LOIN (EN 17412-1), ISO 19650.
- Other tools named: Navisworks, BIMcollab, Allplan, Archicad, Tekla, MicroStation, Speckle, Web-IFC, IFC Lite, differential.tools.

## Notable sources
- https://github.com/Autodesk/revit-ifc/issues/481 - proxy override for fascias/sweeps
- https://github.com/Autodesk/revit-ifc/issues/759 - floors not exporting
- https://github.com/Autodesk/revit-ifc/issues/576 - systematic unit bug
- https://github.com/Autodesk/revit-ifc/issues/378 - duplicate GlobalIds
- https://github.com/Autodesk/revit-ifc/issues/381 - bloated meshing
- https://github.com/Autodesk/revit-ifc/issues/361 - wrong BaseQuantities
- https://github.com/Autodesk/revit-ifc/issues/452 - Navisworks missing elements
- https://github.com/Autodesk/revit-ifc/issues/510 - duplicate ElementTypes
- https://github.com/Autodesk/revit-ifc/issues/886 - ObjectType noncompliance
- https://github.com/Autodesk/revit-ifc/issues/676 - auto-generated proxy types
- https://github.com/Autodesk/revit-ifc/issues/798 - import class mapping tables
- https://github.com/Autodesk/revit-ifc/issues/492 - slow export
- https://github.com/Autodesk/revit-ifc/issues/465 - grid vs true north
- https://github.com/Autodesk/revit-ifc/issues/1015 - feet/304.8 bug (2026)
- https://forums.buildingsmart.org/t/opinion-about-high-polygon-count-in-ifc/4699 - polygon count debate
- https://forums.buildingsmart.org/t/correct-use-of-ifc-name-and-reference-deprecated/6429 - Name/Reference, Allplan
- https://community.osarch.org/discussion/2108/revit-save-to-ifc-guide - guide for consultants
- https://community.osarch.org/discussion/comment/13048 - MVDs irrelevant debate
- https://community.osarch.org/discussion/comment/13115 - Autodesk letter debate
- https://community.osarch.org/discussion/comment/30052 - free viewer thread
- https://community.osarch.org/discussion/3386/addressing-some-core-ifcopenshell-issues - IfcOpenShell weaknesses
- https://github.com/IfcOpenShell/IfcOpenShell/issues/8053 - Qto_SlabBaseQuantities swap
- https://github.com/IfcOpenShell/IfcOpenShell/issues/1151 - Archicad materials

## Gaps
- Reddit, LinkedIn, personal blogs and Autodesk/Graphisoft forums not covered: web search quota was used up and Autodesk forums returned 403.
- Many OSArch pages carry no year; years are inferred from listing dates.
- Few "pure rant" posts were reachable; most real records are bug reports with embedded frustration.
- Three real records are snippet-only. No suspicious sites encountered.
