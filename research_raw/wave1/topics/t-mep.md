# MEP in IFC: systems, connectivity, ports, insulation, hangers, MEP exports (Revit, MagiCAD, DDS-CAD)

Cell: t-mep · Languages: English (real records); synthetic prompts in en, ru, de, zh, es, pt, fr, ja, ko, it · Collected: 2026-11-06 · Records: 38 real / 17 synthetic · Communities covered: GitHub issues (Autodesk/revit-ifc, IfcOpenShell, buildingSMART IFC4.x-development, That Open, ifc-lite), buildingSMART forums, OSArch

NOTE: the WebSearch budget was exhausted before the first search ran, so no web searches were possible. All real records come from GitHub CLI issue search and a few WebFetch reads of known forum URLs. No native-language real records exist in this cell (see Gaps).

## Top themes (ranked by frequency)
- Colours and materials of MEP in IFC: system material vs real material, fittings lose colour, grey MEP (#577, #579, #373, #112, #915)
- Duplicate or exploding IfcElementTypes for fittings and fabrication parts (#510, #524)
- IfcDistributionSystem / IfcSystem export: missing, no psets, cannot override membership, missing with visible-only export (#523, #900, #959)
- IfcDistributionPort: ports cannot be disabled, have no properties, are lost in library import (#630, #188, IfcOpenShell #6687, #7496)
- Port connectivity (IfcRelConnectsPorts, IfcRelNests) for network selection and tracing (That Open #27, IfcOpenShell #8085)
- Insulation: merged into the pipe, heavy geometry, huge file and export time (#416, #892)
- Which IFC class and PredefinedType for a given MEP part (TRANSITION vs CONNECTOR, earthing rod, hangers)
- Units on flow and quantities (L/s vs ft3/s) (#444)
- Missing centre line and axis geometry for ducts and pipes (#33)
- Authoring systems in open-source tools (nesting, hierarchy, circular dependency) (IfcOpenShell #7062, #2578, #1576)
- Performance and size of large MEP models (#892, IfcOpenShell #9247)
- AI-generated MEP IFC that does not validate or open (IfcOpenShell #7945)

## What people want (the goals behind the questions)
- IFC where each pipe, duct and fitting has the correct class, real material, system membership and visible colour
- A connected network: ports linked, flow direction right, so coordinators can select or trace a whole system
- Control over what is exported (ports, insulation geometry, LOD) to keep file size and time down
- Properties on systems and ports (flow, pressure) for engineering and FM handover
- Separate insulation elements with quantities
- Rules for choosing IFC classes, plus mapping from MagiCAD, Revit and DDS-CAD export
- Ability to author and edit systems in open-source tools

## How people write here
- GitHub issues: template-based (Version / Issue description), short, often just a title plus a screenshot, versions given only after maintainers ask. Example: "Both pipe/duct and their insulation get exported as one element".
- Enterprise users stress scale and cost with numbers: "6:16 hours ... 720 MB".
- Typical jargon: "IfcDistributionPort", "system type", "by category", "fittings", "MEP coordinator", "Design Transfer", "Fabrication".
- Apologies for old versions: "sorry, I know it's annoying with bugreports of older versions".
- Forum posts are polite, short, with a "Thanks." closer; beginners write "new to IFC".
- Feature requests from developers are long and structured (Summary / Problem), sometimes LLM-polished.
- Non-native run-on text with no punctuation appears (IfcOpenShell #6100).
- Tone: frustrated about colour and duplicate types; curious or neutral about class choice.
- Labels added to titles: "PR:", "ENH:", "INQ:".

## Local ecosystem
- Autodesk Revit IFC exporter and add-on: https://github.com/Autodesk/revit-ifc
- IfcOpenShell / Bonsai (BlenderBIM): https://github.com/IfcOpenShell/IfcOpenShell
- buildingSMART IFC4.x development (schema Q&A): https://github.com/buildingSMART/IFC4.x-development
- buildingSMART forums: https://forums.buildingsmart.org
- buildingSMART validation service: https://validate.buildingsmart.org/
- OSArch community: https://community.osarch.org
- That Open Company (Fragments, web viewers): https://github.com/ThatOpen/platform_services
- MagiCAD (Finnish vendor, mentioned by forum users as using TRANSITION for reducers), DDS-CAD (Nordic/German MEP), Solibri (coordinator tool): no vendor pages read.
- ifc-lite (viewer library): https://github.com/LTplus-AG/ifc-lite

## Notable sources
- https://github.com/Autodesk/revit-ifc/issues/416 insulation merged into pipe
- https://github.com/Autodesk/revit-ifc/issues/892 pipe insulation control, file size
- https://github.com/Autodesk/revit-ifc/issues/577 system material vs real material
- https://github.com/Autodesk/revit-ifc/issues/579 grey MEP components
- https://github.com/Autodesk/revit-ifc/issues/523 properties on IfcSystem
- https://github.com/Autodesk/revit-ifc/issues/900 override IfcDistributionSystem
- https://github.com/Autodesk/revit-ifc/issues/959 circuits missing with visible-only export
- https://github.com/Autodesk/revit-ifc/issues/630 option not to export ports
- https://github.com/Autodesk/revit-ifc/issues/188 port properties
- https://github.com/Autodesk/revit-ifc/issues/510 fabrication duplicate types
- https://github.com/Autodesk/revit-ifc/issues/524 fitting duplicate types
- https://github.com/Autodesk/revit-ifc/issues/444 flow units
- https://github.com/Autodesk/revit-ifc/issues/915 fitting colour IFC4x3
- https://github.com/IfcOpenShell/IfcOpenShell/issues/8085 generic MEP port model
- https://github.com/IfcOpenShell/IfcOpenShell/issues/7062 system hierarchy
- https://github.com/IfcOpenShell/IfcOpenShell/issues/7945 AI-generated MEP IFC fails to open
- https://github.com/IfcOpenShell/IfcOpenShell/issues/6687 ports on library import
- https://github.com/buildingSMART/IFC4.x-development/issues/147 port axis logic
- https://github.com/ThatOpen/platform_services/issues/27 connectivity preserved in Fragments
- https://forums.buildingsmart.org/t/best-ifc-classification-for-a-reducing-coupling/5963
- https://forums.buildingsmart.org/t/mep-system-classification/2464
- https://forums.buildingsmart.org/t/ifc-mapping-in-revit-mep/4591
- https://community.osarch.org/discussion/2885/ifcpipefittingtype-does-not-import-ports-from-a-library

## Gaps
- WebSearch budget was exhausted before any search ran, so the required 20+ searches and all native-language searches (ru, zh, es, pt, de, fr, ja, ko, it) were not done. Records are only English; no dwg.ru, csdn, cnblogs, zhihu, cad.de, qiita, or Autodesk forum threads (forums.autodesk.com returned 403).
- Not covered: reddit, Graphisoft community, Stack Overflow, vendor KBs (MagiCAD, DDS-CAD), hangers/supports as a topic (only a synthetic prompt exists).
- Years for forum records (2020-2024) are estimated from thread numbering. Records r020, r036-r038 are snippet-level only.
- No suspicious or pirated sites were encountered.
- A follow-up run with a fresh search budget is recommended for native-language communities.
