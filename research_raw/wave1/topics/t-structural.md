# Structural in IFC: rebar, steel, precast, analytical model exchange (Robot, ETABS, SAP2000, SCIA, Dlubal, Tekla)
Cell: t-structural · Languages: English (real sources); ru/zh/es/pt/de/fr/ja/ko/it only as synthetic prompts · Collected: 2026-11-06 · Records: 36 real / 16 synthetic · Communities covered: GitHub issue trackers (Autodesk/revit-ifc, IfcOpenShell, ThatOpen/engine_web-ifc), community.osarch.org

## Top themes (ranked by frequency)
- Revit IFC export options for steel: "Include Steel Elements/Connections" drops, displaces or duplicates beams, columns, bolts, plates (issues 890, 952, 972, 1010, 746, 708)
- Rebar geometry: IfcSweptDiskSolid not supported or rendered wrongly in viewers/converters (IfcConvert Manifold, web-ifc, BlenderBIM)
- Rebar sets exported one entity per bar: huge files, poor usability in Solibri etc. (revit-ifc 76)
- Rebar quantities and weight: no standard Qto in practice, custom Qto, Pset_ConcreteElementGeneral ReinforcementVolumeRatio
- Structural analysis model (IfcStructuralCurveMember, point connections, loads) round trips with RFEM, STAAD, AxisVM, Code_Aster, OpenSees
- Missing analytical data on import to solvers: density, units, yield strength, supports, axes (Z-down)
- Property/Pset export on structural connections and beams (NetWeight, user Psets on plates)
- Fasteners/welds: IfcFastener at origin, IfcMechanicalFastener removal errors
- Precast + Tekla IFC heavy files freezing web viewers; IfcElementAssembly aggregation handling
- Rebar parameter fidelity: rounding, hook/shape text, container via API, height offsets
- Authoring structural/rebar IFC in open-source tools (Bonsai, FreeCAD Rebar workbench)

## What people want (the goals behind the questions)
- Get steel framing, connections, bolts and rebar reliably out of Revit/Tekla into IFC with correct class, predefined type, location and Psets.
- Compact rebar representation (sets as one instance) and lighter files for review and web viewing.
- Reliable rebar take-off: counts, diameter, length, weight, per host element.
- Hand an analytical model (members, nodes, supports, loads, sections) to a solver and get results back, without manual rebuilding.
- Know what a structural IFC lacks before sending it to analysis (material properties, units, supports).
- Open-source authoring and checking of structural models with textbook-level analysis.

## How people write here
- Register: GitHub bug reports are terse and templated ("PR:", "ENH:", "INQ:" title prefixes in revit-ifc); versions and exporter build numbers always given (Revit 2026.4, add-in 26.4.1). Forum posts (OSArch) are friendly, long, open with greetings ("G'day all") and sometimes carry "AI assisted" disclosures.
- Length: titles one line; bodies 3-15 lines with numbered repro steps; users attach screenshots or sample RVT/IFC.
- Jargon: "rebar sets", "swept disk", "analytical model", "Include steel elements", "predefined type", "Pset/Qto", "BOQ", "proxy".
- Misspellings seen: "Strucutral ifc", "OpenCeepy" for OpenSees.
- Fragments: "Rebar exports with wrong height"; "using revit api to create rebarcontainer does not export"; "Not all elements ... are displayed"; "any update on this?" (repeated for years).
- Context given: software + version, IFC version (often IFC2x3 CV2.0 or IFC4 RV), but file rarely public; sample "cannot be shared (workshared)".
- Tone: mostly neutral; frustration shows as repeated "update?" comments and mentions of QA tools (Solibri) failing.
- Synthetic prompts are modelled on this: lowercase, brief, missing context (e.g. "глянь арматура в ифс пришла как...", "帮我查下...", "mach mir ne Stahlliste...").

## Local ecosystem
- buildingSMART: IFC4 structural analysis examples (structural-curve-member.ifc), MVDs (Coordination View 2.0, Reference View) https://www.buildingsmart.org
- Autodesk IFC exporter (open source): https://github.com/Autodesk/revit-ifc (internal REVIT-nnnn tickets cited by Autodesk staff)
- IfcOpenShell / Bonsai: https://github.com/IfcOpenShell/IfcOpenShell ; ifc_structural_mechanics (CalculiX backend), ifc2ca (Code_Aster), analysis-models repo
- web-ifc / That Open: https://github.com/ThatOpen/engine_web-ifc
- FreeCAD BIM + Rebar workbench (amrit3701 add-on); OpenSeesPy; PyNite; structuralcodes
- Commercial tools named: Tekla, Revit, RFEM (Dlubal), STAAD.Pro, AxisVM, Solibri, BIMcollab, BimVision, SimpleBIM, DDScad
- Regional (ru/zh/de/ja etc.) ecosystems NOT reached: see Gaps.

## Notable sources
- https://github.com/Autodesk/revit-ifc/issues/76 rebar sets as one instance, fix in Revit 2025 option
- https://github.com/Autodesk/revit-ifc/issues/972 steel connections Psets, BRACE to MEMBER
- https://github.com/Autodesk/revit-ifc/issues/1010 hollow sections displaced
- https://github.com/Autodesk/revit-ifc/issues/952 Include steel elements hides beams/columns
- https://github.com/Autodesk/revit-ifc/issues/890 steel elements gone in 2025.4.3
- https://github.com/Autodesk/revit-ifc/issues/901 weld IfcFastener at origin
- https://github.com/Autodesk/revit-ifc/issues/870 structural connection user Pset
- https://github.com/Autodesk/revit-ifc/issues/764 NetWeight quantity
- https://github.com/Autodesk/revit-ifc/issues/335 rebar container API
- https://github.com/Autodesk/revit-ifc/issues/14 rebar rounding
- https://github.com/Autodesk/revit-ifc/issues/299 rebar parameter text
- https://github.com/Autodesk/revit-ifc/issues/746 openings in steel columns
- https://github.com/IfcOpenShell/IfcOpenShell/issues/9866 Bonsai structural analysis plan
- https://github.com/IfcOpenShell/IfcOpenShell/issues/10050 profile set destroys edge topology
- https://github.com/IfcOpenShell/IfcOpenShell/issues/6459 AxisVM IFC load failure
- https://github.com/IfcOpenShell/IfcOpenShell/issues/820 ifc2ca
- https://github.com/IfcOpenShell/IfcOpenShell/issues/5931 Tekla to OpenSees
- https://github.com/IfcOpenShell/IfcOpenShell/issues/9762 swept disk rebar in Manifold
- https://github.com/IfcOpenShell/IfcOpenShell/issues/3760 bSI structural sample
- https://github.com/ThatOpen/engine_web-ifc/issues/445 Tekla precast rebar rendering
- https://github.com/ThatOpen/engine_web-ifc/issues/1029 rebar rendering
- https://community.osarch.org/discussion/2578/how-to-create-a-custom-qto-calculation rebar weight Qto
- https://community.osarch.org/discussion/2549/freecad-quantity-schedule rebar in FreeCAD
- https://community.osarch.org/discussion/comment/30616#Comment_30616 structural analysis in Bonsai / RFEM
- https://community.osarch.org/discussion/3767/bim-the-untold-story STAAD from IFC

## Gaps
- WebSearch budget was exhausted at the start of this run (limit message), so no search-engine discovery was possible; sources come from direct fetches of GitHub issue-list HTML pages and OSArch search. Seed queries in the 9 other languages were therefore not run.
- No genuine non-English real posts (dwg.ru, csdn, cnblogs, zhihu, qiita, cad.de, foros) collected: cnblogs/dwg.ru search URLs returned 404, qiita search empty, cad.de redirected, forums.buildingsmart.org and forums.autodesk.com returned 403 / blocked page, Stack Exchange API not fetchable. All non-English items are synthetic.
- gh CLI search hit API rate limit after the first calls.
- Little direct coverage of ETABS, SAP2000, SCIA, Dlubal knowledge bases, Tekla Warehouse/precast docs; only RFEM and Tekla appear via third-party issues.
- Several 2018-2021 items are snippets of long threads; two web-ifc items and three IfcOpenShell/revit-ifc items are snippet-level evidence.
- No suspicious sites encountered.
