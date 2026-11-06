# Software developers building IFC tools: schema intricacies, geometry, performance
Cell: p-developer · Languages: English only (native-language searches were NOT possible, see Gaps) · Collected: 2026-11-06 · Records: 41 real / 19 synthetic · Communities covered: GitHub issues (IfcOpenShell, ThatOpen web-ifc, xBIM Essentials/Geometry), community.osarch.org, forums.buildingsmart.org (titles only)

## Top themes (ranked by frequency)
- Performance and memory on large files (300MB to 2GB+): iterator speed, OOM, WASM 4GB ceiling, leaks after closing files
- Boolean/opening geometry failures (IfcOpeningElement, IfcBooleanClippingResult, wrong triangles over openings, kernel differences OCC vs CGAL)
- Mapped items / representation maps: instancing efficiency, wrong placement, MappingTarget vs ObjectPlacement
- Placement math: local vs world coordinates, axis of beams, units (feet vs metres)
- Inverse attributes and relationship traversal (HasOpenings, IsTypedBy, IsDefinedBy) in C++/Python/.NET APIs
- Tessellation/shell quality: open shells, non-manifold, face-based surface models, determinism of vertex order
- IFC4.3 and schema detection: typed select values, FILE_SCHEMA parsing, alignment/sweeps
- Library comparisons (IfcOpenShell vs xBIM vs web-ifc vs BIMvision/Solibri as reference viewer)
- Regressions between library versions (0.7 to 0.8, xBIM 6.0.442, web-ifc 0.0.59 to 0.0.68)
- Hangs with no error on specific solids (infinite loops in geometry engines)
- Mass edit speed (delete/extract thousands of elements, quadratic APIs)
- Undocumented internals (IfcFile indices, kernel selection, context ids)

## What people want
- Open any real-world (Revit/Archicad) export without crash or timeout, with geometry identical to commercial viewers.
- Deterministic, fast, memory-bounded geometry pipelines for servers and browsers.
- Understand which attribute is inverse and how to traverse the graph cheaply.
- Correct world coordinates for any element, including mapped items and units.
- Tools to detect bad geometry (open shells, voids without fills) and subset/split huge models.
- Large public test files (1M-element sets) for benchmarking.

## How people write here
- Bug-report register: title states symptom, body has "What happened / Version / repro", often code and screenshot, no greetings, sometimes closes with "Thanks for your support!".
- Benchmarks as numbers: "12MB: 222s vs 2s", "7,413,409 lines", "300000 components".
- Exact class names and API calls (GetFlatMesh, get_inverse, create_shape, IsTypedBy); frequent "Aborted()" / stack trace pastes.
- Comparative framing with another tool: "BIMvision shows it fine", "XBim is faster".
- Admitted newcomers: "I am completely new to both BIM and IfcConvert".
- Fragments: "I do not know what the index's meaning", "never completes", "Is there a fast way to do this?", "take the Z basis vector".
- Emotional tone mostly neutral/technical, frustration shown only via numbers and bold text. Maintainers reply tersely and ask for the model ("Can you share the model?").
- Misspellings seen: "Globel Id", "casuses", "Relatin" style typos, "IfcOpenning".

## Local ecosystem
- Open-source: IfcOpenShell / Bonsai (https://github.com/IfcOpenShell/IfcOpenShell), That Open web-ifc (https://github.com/ThatOpen/engine_web-ifc), xBIM (https://github.com/xBimTeam/XbimEssentials), Fragments.
- Standards bodies: buildingSMART (https://forums.buildingsmart.org), IFC4.3 infrastructure.
- Community: OSArch (https://community.osarch.org), tags ifc-geometry and ifcopenshell.
- Reference viewers cited: BIMvision, Solibri, BIMcollab Zoom, Xbim Xplorer.
- Third-party tools seen: IfcClash, ifc2duckdb, goifc (Go reader), bSDD-Toolkit.

## Notable sources
- https://github.com/IfcOpenShell/IfcOpenShell/issues/6712 (benchmark vs xBIM, mapped items)
- https://github.com/IfcOpenShell/IfcOpenShell/issues/6277 (mapped item coordinates)
- https://github.com/IfcOpenShell/IfcOpenShell/issues/3900 (inverse attributes C++)
- https://github.com/IfcOpenShell/IfcOpenShell/issues/4009 (IfcFile internals)
- https://github.com/IfcOpenShell/IfcOpenShell/issues/6142 (kernel difference)
- https://github.com/IfcOpenShell/IfcOpenShell/issues/6026 (OOM face-based surface)
- https://github.com/IfcOpenShell/IfcOpenShell/issues/6904 (iterator leak)
- https://github.com/IfcOpenShell/IfcOpenShell/issues/7829 (IfcFile memory)
- https://github.com/IfcOpenShell/IfcOpenShell/issues/2639 (bounding box substitution)
- https://github.com/ThatOpen/engine_web-ifc/issues/895 (mapped item wrong location)
- https://github.com/ThatOpen/engine_web-ifc/issues/1999 (WASM crash large MEP)
- https://github.com/ThatOpen/engine_web-ifc/issues/2097 (waffle slab hang)
- https://github.com/ThatOpen/engine_web-ifc/issues/1752 (parsing speed)
- https://github.com/ThatOpen/engine_web-ifc/issues/2269 (booleans IFC4.3)
- https://github.com/ThatOpen/engine_web-ifc/issues/933 (clipping result)
- https://github.com/xBimTeam/XbimEssentials/issues/531 (tessellation performance)
- https://github.com/xBimTeam/XbimEssentials/issues/674 (IsTypedBy regression)
- https://github.com/xBimTeam/XbimGeometry/issues/335 (hang)
- https://community.osarch.org/discussion/1682/how-exactly-is-ifcopenshell-geom-create-shape-parsing-the-geometry
- https://community.osarch.org/discussion/2704/get-ifcbeam-coordinates-in-3d-space
- https://community.osarch.org/discussion/1307/detect-and-fix-objects-where-the-shell-is-not-closed
- https://community.osarch.org/discussion/2673/deleting-many-objects-takes-forever
- https://community.osarch.org/discussions/tagged/ifc-geometry (index of 28 geometry threads)
- https://forums.buildingsmart.org/t/ifc4-designtransferview-geometry/3116

## Gaps
- The WebSearch budget was exhausted before any search ran, so only direct fetches and the GitHub CLI were used. The 20+ planned searches, all native-language (ru, zh, es, pt, de, fr, ja, ko, it) searches, Autodesk/Graphisoft forums, dwg.ru, csdn, zhihu, qiita and reddit were not covered. All real records are therefore English.
- stackoverflow.com cannot be fetched; Qiita tag pages returned no article list; cnblogs tag URL 404.
- Many forum records are snippet-level only (titles); OSArch threads were read via summary, not verbatim.
- Some synthetic `inspired_by` ids point approximately, not exactly, at the related real records.
- No suspicious sites encountered.
