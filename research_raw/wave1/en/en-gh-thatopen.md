# GitHub: That Open Company (web-ifc, components, fragments; ex IFC.js) issues
Cell: en-gh-thatopen · Languages: English · Collected: 2026-11-06 · Records: 64 real / 17 synthetic · Communities covered: ThatOpen/engine_web-ifc, engine_components, engine_fragment issue trackers; legacy IFCjs/web-ifc-viewer and IFCjs/web-ifc-three; docs.thatopen.com (partial)

## Top themes (ranked by frequency)
- Large IFC files: memory crashes, "memory access out of bounds", Aborted(), WASM 4 GB ceiling, 1-2 GB models, 40-model federations
- Slow load or conversion: IFC to .frag takes minutes, infinite loading, slow property indexing and slow hover/raycast
- Missing or wrong geometry: extrusions, sweeps, breps, roofs, curtain wall members, triangles sticking out
- Openings and booleans: walls without windows, openings shown in the wrong place, void regressions between releases
- Colours and materials: everything white, IFC4 vs IFC2x3 colour loss, colour via material or type not applied, transparency ignored
- Properties and psets: missing type-level psets (IfcRelDefinesByType), "not all properties", slow getPropertySets, writing typed values
- Spatial structure: IfcSpace and roof elements not under storeys, classifier by storey, alignment children missing
- Coordinates and georeferencing: COORDINATE_TO_ORIGIN, IfcMapConversion, IfcProjectedCRS, models misplaced when several are loaded
- IFC4.3 and civil: IFC4X3_ADD1/ADD2 not recognised, alignments from Civil 3D, new pset in 4x3
- IDS and BCF conformance: facet stubs, inverted cardinality, BCF 3.0 not schema-valid
- 2D plans, sections and clipping: Views, ClipStyler, hollow walls, missing elements in plans
- Install/bundling friction: wasm path, Vite/Next/Angular, three.js version mismatches, API breakage between versions
- Comparing with other viewers (BIMvision, Solibri, Dalux, usBIM, APS): "it works there, why not here"

## What people want (the goals behind the questions)
- Open the real, big project model in a browser without it crashing, and have it be fast
- Trust that what the viewer shows equals what Revit/ArchiCAD/Civil 3D exported (geometry, colours, openings)
- Get properties (including type psets, quantities, georeference) out of the model quickly and completely
- Group and filter by storey, type, category, predefined type; hide spaces; see plans and sections
- Place models correctly (origin, CRS, shared coordinates across several models)
- Validate against IDS and exchange BCF that other tools accept
- Edit properties and geometry and export back to valid IFC; convert IFC to fragments on a backend
- Support IFC4.3 infrastructure (alignments, tunnels, bridges)
- Build construction apps on top (4D/P6 schedule, AWP, federated multi-model viewers)

## How people write here
- Register: GitHub bug-template English, technical, mostly non-native speakers; very short bodies with a screenshot or a private file link; polite or neutral, frustration shows mainly as "crashes", "stuck", "infinite loading".
- Typical length: 1-5 lines plus stack trace; a few maintainers-style detailed reports (markdown tables, entity chains) in 2026.
- Jargon: "frag" (fragments file), "proxy", "pset", "express ID", "wasm", "StreamMeshes", "culler", "hider", "classifier", "OBC", "storey", "IfcSpace visible box".
- Misspellings and variants: "properites", "Mo" for MB, "Spacial", "IFC 4x3 add2", "ifc.js", "ifcs".
- Code-switching: rare; occasional French/German property names and units (Tragendes Material, Mo).
- Context given: library version, browser, a screenshot comparing with another viewer; often omitted: the IFC file itself (confidential, sent privately), IFC schema, authoring app version.
- Fragments: "my browser crashes when loading" · "works in BIMvision but not here" · "same model works in APS viewer" · "how to bypass loading screen" · "any news? already released?"
- Emotional tone: patient to confused; occasional "infinite loading", "super large model"; thanks and closing remarks when fixed.

## Local ecosystem
- That Open Company (Spain/global) maintains web-ifc, components, fragments; docs https://docs.thatopen.com/intro, community (login-gated) https://people.thatopen.com
- buildingSMART standards used in the threads: IFC2x3, IFC4, IFC4X3_ADD2, IDS, BCF 3.0 (https://www.buildingsmart.org)
- Other viewers used as ground truth: BIMvision, Solibri, Dalux, usBIM, BIMCollab, OpenIFC Viewer, APS Viewer
- Authoring tools in reports: Revit, ArchiCAD, Civil 3D, Tekla, Cadwork, ACCA Edificius, AutoCAD
- Open-source neighbours: IfcOpenShell, three.js, three-edge-projection, bimledger (https://github.com/tomvandig/bimledger), xBIM sample files
- Legacy: IFC.js, web-ifc-three, web-ifc-viewer (now superseded by components since Sept 2023)

## Notable sources
- https://github.com/ThatOpen/engine_web-ifc/issues/538 - super large model aborts
- https://github.com/ThatOpen/engine_web-ifc/issues/419 - 2 GB models fail
- https://github.com/ThatOpen/engine_web-ifc/issues/1816 - indexing properties on 400-500 MB models
- https://github.com/ThatOpen/engine_web-ifc/issues/967 - why demo vs template differ (geometry merging)
- https://github.com/ThatOpen/engine_web-ifc/issues/1793 - IFC4 loses colours vs IFC2x3
- https://github.com/ThatOpen/engine_web-ifc/issues/1833 - material colour chain ignored
- https://github.com/ThatOpen/engine_web-ifc/issues/2235 - type-level material colour
- https://github.com/ThatOpen/engine_web-ifc/issues/1171 - IFC4X3_ADD2 won't open
- https://github.com/ThatOpen/engine_web-ifc/issues/1873 - type properties empty
- https://github.com/ThatOpen/engine_components/issues/515 - big IFC crashes the app
- https://github.com/ThatOpen/engine_components/issues/414 - IFCSPACE not classified in storeys
- https://github.com/ThatOpen/engine_components/issues/653 - byIfcBuildingStorey misses elements
- https://github.com/ThatOpen/engine_components/issues/745 - all geometry white
- https://github.com/ThatOpen/engine_components/issues/642 - first-time evaluation complaints
- https://github.com/ThatOpen/engine_components/issues/495 - georeferenced IFC orientation
- https://github.com/ThatOpen/engine_components/issues/743 - alignment children in spatial structure
- https://github.com/ThatOpen/engine_components/issues/830 - IDS facets as stubs
- https://github.com/ThatOpen/engine_components/issues/825 - BCF 3.0 export validity
- https://github.com/ThatOpen/engine_fragment/issues/129 - 1.3 GB model
- https://github.com/ThatOpen/engine_fragment/issues/258 - >2 GB WASM ceiling
- https://github.com/ThatOpen/engine_fragment/issues/315 - 2 GB industrial model with P6 schedule
- https://github.com/ThatOpen/engine_fragment/issues/228 - 40 models performance
- https://github.com/ThatOpen/engine_fragment/issues/160 - projected CRS placement
- https://github.com/ThatOpen/engine_fragment/issues/168 - missing type properties vs Solibri
- https://github.com/ThatOpen/engine_fragment/issues/301 - IfcSpace box above roof
- https://github.com/ThatOpen/engine_fragment/issues/164 - indexed queries in .frag
- https://github.com/IFCjs/web-ifc-viewer/issues/205 - spatial tree (legacy)
- https://github.com/IFCjs/web-ifc-three/issues/125 - slow getPropertySets (legacy)
- https://docs.thatopen.com/Tutorials/Components/Core/IfcLoader - official IfcLoader tutorial

## Gaps
- WebSearch budget was exhausted by the shared turn limit, so no web searches ran. Stack Overflow, blog posts and the three.js forum were therefore not covered.
- people.thatopen.com "Ask the community" requires login (redirects to auth0), so forum threads were not read.
- GitHub search API was rate-limited; issues were listed through GraphQL (latest ~400 per repo), so older components/web-ifc-viewer history is thinner.
- Tool calls totalled about 25 including the gh calls; the target of 30-45 was not fully met. Evidence is "page" (issue bodies and the latest comment), not full comment threads.
- Only English issues; a few reporters shared files privately, so the exact models are not visible.
- No suspicious or pirated sites were encountered.
