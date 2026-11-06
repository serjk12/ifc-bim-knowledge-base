# USA and Canada: AASHTO/FHWA IFC for bridges and roads, GSA, USACE, COBie
Cell: en-us-canada-infra · Languages: English · Collected: 2026-11-06 · Records: 36 real / 17 synthetic · Communities covered: buildingSMART International forums, OSArch, GitHub (IfcOpenShell/Bonsai, Autodesk revit-ifc), Autodesk Community forums (snippets), FHWA/DOT/NIBS official pages

## Top themes (ranked by frequency)
- COBie export from Revit/IFC: missing parameters, empty fields (Type dimensions, Systems tab), wrong IFC version (2x3 vs IFC4 MVD), Interoperability Tools parameter mapping.
- Revit IFC export failures and quality: missing elements, openings, version-specific exporter differences, empty-value parameters not exported.
- IFC4.3 infrastructure basics: IfcBridge vs IfcRoad, IfcBridgePart nesting, alignment, IfcLinearPlacement.
- Civil 3D / InfraWorks / ProVI interop: wrong position, alignments invisible, everything becomes IfcBuildingElementProxy.
- Coordinates and georeferencing: state-plane/large coordinates, shared coordinates in Revit link, precision loss far from origin, feet vs mm.
- Schema-version confusion: IFC4.1 never certified, 4.3 RC vs final, upgrade IFC4 to IFC4.3, ADD2.
- Test files and validation: bSI Validation Service, TPF-5(372) Unit Test Suite, certified-software requirements for DOTs.
- DOT digital delivery: TxDOT OpenBridge and Model Development Standards, PennDOT first contractual IFC bridge model with rebar, Iowa-led pooled funds.
- Federal handover requirements (GSA BIM Guides, USACE CAD-BIM Center PxP/M3/CHX, NBIMS-US COBie) driven by contract language.
- Open-source tooling for civil work (Bonsai, Saikei Civil, ifcopenshell scripting).
- Quantities and fabrication use cases (rebar IFC, steel girder fabricators needing newer IFC).

## What people want (the goals behind the questions)
- Get a clean COBie spreadsheet out of the model that passes owner QC, without remapping everything.
- Make Revit and Civil 3D export correct IFC classes instead of proxies and in the right place.
- Understand which IFC4.3 class and spatial container to use for bridge components (AASHTO-aligned hierarchy).
- Exchange bridge design to construction/fabrication in an open format that opens in the contractor's software without data loss.
- Find sample files, validators and certified software so DOT requirements can be enforced.
- Open tools for alignment and corridor authoring with familiar civil conventions (bearings, stations, PI/PVI).

## How people write here
- Register: concise, technical, often one to three sentences; issue-template style on GitHub, longer polite posts on buildingSMART and Autodesk forums.
- Jargon: COBie tabs, Type/Component, proxy, alignment, stationing, PI/PVI, "IFC4x3", "ADD2", "AbRV", "pay items", "LOD", "state plane".
- Titles are often the whole question ("Export IFC - wrong position !", "REVIT 2026 Won't export to IFC?").
- Context given: software and version names; context omitted: file, exporter settings, schema version.
- Fragments: "Any idea what's happening here?"; "nothing visible even after Zoom Extents"; "painful BuildingElementProxy"; "Thanks in advance".
- Misspellings seen: "vom" (non-native), "COBIe", "expoted", "developpements".
- Imperial units/US vocabulary (feet, kerbs vs curbs, state DOT, plans sealed) appear; Canadian content was thin.

## Local ecosystem
- FHWA BIM for Bridges and Structures: https://www.fhwa.dot.gov/bridge/bim (reports HIF-16-010/011, HIF-21-031 Utah demo, HIF-24-004).
- AASHTO COBS T-19; pooled funds TPF-5(372), TPF-5(523), TPF-5(480), TPF-5(565) IFC validation/certification: https://pooledfund.org/Details/Study/1798
- Unit Test Suite: https://github.com/jwouellette/TPF-5_372-Unit_Test_Suite ; Caltrans BIM4I page hosts IFC export guides.
- State DOTs: TxDOT digital delivery https://www.txdot.gov/business/resources/digital-delivery/digital-delivery-documents.html ; PennDOT contractual IFC pilot https://www.paconstructors.org/news/first-contractual-ifc-model-delivered-nationally/ ; Iowa DOT BIM https://iowadot.gov/bridge/BIM/
- NIBS / NBIMS-US COBie v3: https://nibs.org/nbims/v3/cobie/ ; Draft https://www.nationalbimstandard.org/files/pdfs/2023-05-26NBIMS-US_COBie_v3_Standard_DRAFT-20230501.pdf
- GSA BIM Guide series (Guide 08 facility management, COBie): https://origin-www.gsa.gov/system/files/largedocs/BIM_Guide_Series_Facility_Management.pdf
- USACE CAD-BIM Center (PxP, M3, CHX checklists; domain not reachable from this environment).
- buildingSMART Canada and NRC openBIM roadmap (Jan 2024): https://buildingsmartcanada.ca/projects
- bSI Validation Service: https://technical.buildingsmart.org/services/validation-service/
- Open source: IfcOpenShell/Bonsai, Saikei Civil, Autodesk revit-ifc (https://github.com/Autodesk/revit-ifc), Civil 3D IFC 4.3 extension.

## Notable sources
- https://forums.buildingsmart.org/t/cobie-to-ifc-export-issues/1860 - COBie from Revit, IFC4 MVD advice
- https://forums.buildingsmart.org/t/exporting-bridge-elements-to-ifc-4-3-ifcbridge-or-ifcroad/5811 - bridge vs road scope
- https://forums.buildingsmart.org/t/new-ifc-4x2-3-bridge-file-examples/5218 - sample bridge files
- https://forums.buildingsmart.org/t/ifc-4x1-file-containing-alignment-is-not-opening-in-civil-3d/3830 - alignment interop
- https://forums.buildingsmart.org/t/ifc-4x3-vs-4-1-changes/3217
- https://forums.buildingsmart.org/t/link-to-the-latest-ifc4-3-release-for-bridges-and-roads-developpements/4410
- https://community.osarch.org/discussion/2266/bbim-ifc-4x3-class-and-predefined-type-quick-guide-for-beginners
- https://community.osarch.org/discussion/3251/saikei-civil-native-ifc-for-horizontal-construction
- https://github.com/IfcOpenShell/IfcOpenShell/issues/5926 - COBie missing tabs
- https://github.com/IfcOpenShell/IfcOpenShell/issues/6068 - COBie systems empty
- https://github.com/IfcOpenShell/IfcOpenShell/issues/3978 - Revit exporter version differences
- https://github.com/IfcOpenShell/IfcOpenShell/issues/4921 - upgrade to IFC4.3 for IfcRoad
- https://github.com/IfcOpenShell/IfcOpenShell/issues/9770 - precision far from origin
- https://github.com/Autodesk/revit-ifc/issues/963 - empty parameter values
- https://github.com/Autodesk/revit-ifc/issues/566 - shared coordinates linking
- https://forums.autodesk.com/t5/civil-3d-forum/ifc-exporting-road-model/td-p/12923665
- https://forums.autodesk.com/t5/revit-architecture-forum/cobie-type-length-cobie-type-width-cobie-type-height-is-always/td-p/11009379
- https://www.fhwa.dot.gov/bridge/pubs/hif21031.pdf - Utah demonstration
- https://www.paconstructors.org/news/first-contractual-ifc-model-delivered-nationally/
- https://github.com/jwouellette/TPF-5_372-Unit_Test_Suite
- https://pooledfund.org/Details/Study/1798
- https://nibs.org/nbims/v3/cobie/

## Gaps
- reddit.com not accessible to search; Autodesk Community pages returned 403 on fetch, so ~14 Autodesk records are snippet-level (titles and search summaries only).
- No genuine Canada-specific user questions found (only buildingSMART Canada/NRC roadmap material); Ontario MTO, Infrastructure Canada, canbim.com not verified.
- USACE cadbimcenter domain did not resolve; USACE and GSA content came from search summaries, with no real user posts.
- Years for Autodesk snippet records are estimated from thread IDs.
- Little DOT-contractor voice; most real questions come from open-source and standards communities. Synthetic prompts partly fill this.
- No suspicious sites linked; a vendor blog (ehlist-ca.pages.dev) and Scribd copies were skipped as unreliable.
