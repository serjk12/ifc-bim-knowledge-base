# Tekla Structures community: IFC export/import and reference models

Cell: en-tekla · Languages: English · Collected: 2026-11-06 · Records: 17 real / 14 synthetic · Communities covered: GitHub issues of third-party tools handling Tekla IFC (IfcOpenShell, xBIM, Autodesk revit-ifc, buildingSMART, BHoM, Speckle, Grasshopper-TeklaDrawingLink, tekla-mcp-server, AWARE); Tekla User Assistance (support.tekla.com). NOT covered: forum.tekla.com threads (see Gaps).

## Top themes (ranked by frequency)
- Wrong location / base point / rotation of Tekla IFC in other tools (IfcMapConversion vs IfcSite, project north, reference model rotation)
- Revit import of Tekla IFC: Open vs Link, in-place families, duplicated assembly + parts, .ifc.rvt
- IfcElementAssembly wrapping (single-part assemblies, doubled element counts) and hosting of rebar
- Choosing export type/view (Reference, Design transfer, Precast, Bridge; IFC2x3 Surface geometry, CV2.0, Steel fabrication)
- Geometry that fails in viewers (curved members, booleans, B-rep fallback)
- Property sets and UDAs not appearing, empty numeric values
- Checking export: reference model overlay vs original, object counts, export log
- Precision/tolerance loss when importing into analysis tools
- Grids, braces as lines, and other non-solid objects dropped by consumers
- AI agents / MCP driving Tekla (reference model coordination, attribute audits)

## What people want (the goals behind the questions)
- Send structure to architect/MEP and have it land in the right place with the right north
- Get clean, class-correct elements (no proxies, no duplicated assemblies) in Revit/Navisworks
- Carry custom attributes (UDAs, quantities, weights) in property sets
- Prove the exported IFC matches the Tekla model (counts, geometry)
- Use IFC as lightweight reference in Tekla and align it correctly
- Automate export and checking in scripts and LLM agents

## How people write here
- GitHub reporters: short, factual, attach a minimal file; "Can't drop an IFC file created in Tekla"; "Hello! ... Thanks in advance".
- Compare working vs failing path: "If I export directly from Tekla it works".
- Version pinning in newer reports: "Tekla 2026 SP5", "Tekla 2025".
- Jargon: reference model, base point, Brep, CV2.0, UDA, assembly, cast unit, pour object, Organizer.
- Context often omitted: IFC schema version and export type.
- Tone mostly neutral/polite; frustration in Revit-import complaints.

## Local ecosystem
- Tekla User Assistance (Trimble): https://support.tekla.com/doc/tekla-structures/2024/int_ifc_export
- Tekla forum structure (Interoperability section): https://forum.tekla.com/forum/253-usage-interoperability/
- buildingSMART IFC4.x development: https://github.com/buildingSMART/IFC4.x-development
- IfcOpenShell/BlenderBIM: https://github.com/IfcOpenShell/IfcOpenShell
- Autodesk revit-ifc: https://github.com/Autodesk/revit-ifc
- xBIM: https://github.com/xBimTeam/XbimGeometry
- LetsConstructIT Grasshopper-TeklaDrawingLink: https://github.com/LetsConstructIT/Grasshopper-TeklaDrawingLink
- tekla-mcp-server (LLM tooling for Tekla): https://github.com/tempalg1n/tekla-mcp-server
- BHoM, Speckle connectors

## Notable sources
- https://support.tekla.com/doc/tekla-structures/2024/int_ifc_export
- https://support.tekla.com/doc/tekla-structures/2024/int_exporting_into_ifc
- https://support.tekla.com/doc/tekla-structures/2024/int_checking_exported_ifc_model
- https://support.tekla.com/doc/tekla-structures/2024/int_defining_property_sets_using_property_set_definitions
- https://github.com/LetsConstructIT/Grasshopper-TeklaDrawingLink/issues/147
- https://github.com/IfcOpenShell/IfcOpenShell/issues/2150
- https://github.com/Autodesk/revit-ifc/issues/223
- https://github.com/Autodesk/revit-ifc/issues/710
- https://github.com/buildingSMART/IFC4.x-development/issues/205
- https://github.com/xBimTeam/XbimGeometry/issues/527
- https://github.com/tempalg1n/tekla-mcp-server/issues/44
- https://github.com/tempalg1n/tekla-mcp-server/issues/25
- https://github.com/BHoM/ETABS_Toolkit/issues/548
- https://github.com/specklesystems/speckle-server/issues/1128
- https://github.com/aware-aeco/aware/issues/422
- https://github.com/youshengCode/IfcToolbox/issues/21

## Gaps
- The WebSearch budget was exhausted at the start of the run (0 searches succeeded), so no query-based discovery was possible.
- forum.tekla.com: internal search returned 0 results to anonymous fetch and section listings returned HTTP 403, so no genuine forum posts were read. This is the main gap: the real Tekla user voice (forum threads) is missing; real count is 17 instead of 30-60 and 4 of the 17 are official docs.
- Several guessed support.tekla.com URLs (object converter, reference model import) returned 404; not recorded.
- Total tool calls were fewer than the 25-search target.
- No suspicious sites encountered. Recommend a re-run of this cell with search available.
