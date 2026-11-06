# Open-source IFC libraries and toolkits

**Last researched: 2026-11-06**

## In plain words

IFC (Industry Foundation Classes, ISO 16739) is a text/XML/JSON data format for building models. To read or change an IFC file from code you need a library, and most of the AI-to-IFC bridges (MCP servers) are thin wrappers around one. The dominant open-source libraries are **IfcOpenShell** (C++/Python), **xBIM** (.NET), **web-ifc** with **That Open Engine** (JavaScript/WebAssembly). Many other projects are viewers, converters, servers or niche formats. This page lists each one with license, language, purpose, maturity and typical user questions, followed by a "which library for what" table. Version numbers and star counts are a snapshot taken from the cited pages on 2026-11-06 and move fast.

Revit note: none of these libraries run inside Revit, except Autodesk's open-source Revit IFC exporter [45], which is a Revit add-in code base, not a general library. Revit models reach these tools as exported `.ifc` files.

---

## 1. IfcOpenShell (the reference open-source IFC toolkit)

| Item | Value |
|---|---|
| Description | "Open source IFC library and geometry engine" [1] |
| Languages | C++ core, Python API (SWIG bindings), JS/TS builds exist [1][2] |
| License | Core LGPL-3.0-or-later; some parts (Bonsai, ifcsverchok) GPL-3.0-or-later [1]. PyPI shows LGPL-3.0-or-later for the Python package [3] |
| Install | `pip install ifcopenshell` (Python 3.10 to 3.15 per PyPI) [3] |
| Latest stable | 0.9.0.post1, PyPI date 2026-10-15 [3]. Previous: 0.9.0 (PyPI 2026-09-29; the GitHub release page lists 01 Oct, so dates differ by source), 0.8.5 on 2026-04-13 [3][4] |
| Maturity / activity | Very high. About 23.6k commits, 2.9k stars, ~1.2k open issues [1]. Daily Bonsai alpha builds were still being published on 2026-11-06 [4] |

**Schemas.** The repository README says it parses IFC2x3 TC1, IFC4 Add2 TC1, IFC4x1, IFC4x2 and IFC4x3 Add2, with geometry for IFC2x3 and IFC4 [1]. The 0.9.0.post1 release notes say the shipped wheel now includes only IFC2X3, IFC4 and IFC4X3 (experimental schemas dropped) [4]. If a test depends on IFC4x1/4x2, check the installed version (partly unverified).

**0.9.0 highlights (2026-10).** Rewritten C++ data model and parser with plug-in architecture for schemas, geometry kernels and serializers; big parser performance gains; new Bonsai Viewer with a `.ifcview` cache format; Manifold and Passthrough geometry kernels [4].

### Python modules (the part MCP servers use most)

- **`ifcopenshell`** core: `ifcopenshell.open("model.ifc")` returns an `ifcopenshell.file`; `model.by_type("IfcWall")`, `model.by_guid(...)`, `model.create_entity(...)`, `model.write(...)`.
- **`ifcopenshell.api`**: high-level "do what a BIM tool does" functions, called as `ifcopenshell.api.run("root.create_entity", model, ifc_class="IfcWall")`. Module folders in v0.8.0: aggregate, alignment, attribute, boundary, classification, cogo, constraint, context, control, cost, document, drawing, feature, geometry, georeference, grid, group, layer, library, material, nest, owner, profile, project, pset, pset_template, resource, root, sequence, spatial, structural, style, system, type, unit [14]. Typical calls: `root.create_entity`, `spatial.assign_container`, `pset.add_pset` / `pset.edit_pset`, `material.assign_material`, `geometry.add_wall_representation`, `type.assign_type`, `project.create_file`. These keep relationships (IfcRelContainedInSpatialStructure, IfcRelDefinesByProperties, ...) and ownership history consistent, which raw `create_entity` does not.
- **`ifcopenshell.util`**: read-side helpers. Modules include element, selector, placement, pset, unit, shape, date, classification, cost, sequence, schema, representation, geolocation, system, type, fm [15]. Examples: `ifcopenshell.util.element.get_psets(wall)` returns property sets as a dict; `ifcopenshell.util.selector.filter_elements(model, "IfcWall, Pset_WallCommon.FireRating=2HR")` uses a CSS-like query syntax (selector syntax details: unverified here, see [2]).
- **`ifcopenshell.geom`**: geometry processing through `geom.create_shape(settings, element)` or the multi-threaded `geom.iterator`; returns triangulated meshes (verts/faces) with settings such as `USE_WORLD_COORDS`. The docs call out a boolean process and a geometry iterator [2].
- **`ifcopenshell.validate`** (schema/constraint validation; confirmed indirectly because `ifcquery validate` checks "schema and constraint violations" with an optional slower EXPRESS-rules mode [6]).

### Command-line and add-on tools shipped in the same repo

| Tool | What it does | Notes |
|---|---|---|
| **IfcConvert** | CLI converter IFC to OBJ, DAE (Collada), glTF/GLB, STEP, IGES, SVG, XML, HDF5 and IFC re-serialization (format list from general knowledge, unverified in the sources read; run `IfcConvert --help`) | Source folder also contains validators for space boundaries, storey containment, wall connectivity [16]. Common flags: `--use-element-guids`, `--include`/`--exclude`, `--filter-file`, `--threads`, `--weld-vertices` (unverified) |
| **IfcPatch** | "Recipes" that modify IFC. 38 recipes in v0.8.0, e.g. ExtractElements, MergeProjects, Migrate, ConvertLengthUnit, OffsetObjectPlacements, SetFalseOrigin, SplitByBuildingStorey, Optimise, Ifc2Sql, RegenerateGlobalIds, FixRevitTINs, FixArchiCADToRevitSpaces [7] | Includes Revit/ArchiCAD workaround recipes |
| **IfcDiff** | Compares two IFC files: added/deleted elements, geometry, attributes, properties, containers, classifications; shallow or deep mode; JSON output [11] | |
| **IfcCSV** | Export IFC data to CSV, ODS, XLSX or pandas; import edited sheets back [10] | Used for bulk property editing and schedules |
| **IfcTester** | Python library and (experimental) web app for auditing models against **IDS** (Information Delivery Specification) [9][43] | The v0.8.0 README is minimal [9]; feature details from [2] not verified |
| **IfcClash** | Clash detection: intersection, collision, clearance; within one model or across files; results to BCF-XML or JSON; selector-based filtering [8] | |
| **Ifc4D / Ifc5D** | 4D scheduling: MS Project, Primavera P6 (XML, XER), Asta Powerproject to IFC; IFC to P6 XML and MS Project. 5D = cost schedules [12][1] | CSV not mentioned in README [12] |
| **BCF (python `bcf`)** | BCF-XML (`bcfxml.py`) and BCF-API (`bcfapi.py`) implementation; README does not state versions [13]. Repo description says BCF-XML and OpenCDE BCF-API [1] | |
| **IfcFM / COBie** | Facility-management handover data (`ifcfm`) [1]. The repo lists no separate "IfcCOBie" entry; COBie-style spreadsheets are handled via ifcfm/ifccsv (partly unverified). For COBie in .NET see xBIM CobieExpress [19] | |
| **bSDD** | Queries the buildingSMART Data Dictionary API [1] | |
| **IfcCityJSON, Ifc2CA, IfcMax** | CityJSON to IFC; structural models to Code_Aster; historic 3ds Max extension [1] | niche |
| **ifcquery / ifcedit** | Newer CLIs. `ifcquery model.ifc summary|tree|info|select|relations|validate|schedule|cost|schema|contexts|materials|plot|render|clash`, JSON output by default; `ifcedit run/foreach` applies `ifcopenshell.api` calls from shell [6] | |
| **IfcMCP** | An **MCP server** wrapping ifcquery and ifcedit, keeping the model in memory between tool calls. Tools: `ifc_new`, `ifc_load`, `ifc_reset`, `ifc_save`, `ifc_summary`, `ifc_tree`, `ifc_info`, `ifc_select`, `ifc_relations`, `ifc_contexts`, `ifc_materials`, `ifc_clash`, `ifc_validate`, `ifc_schedule`, `ifc_cost`, `ifc_schema`, `ifc_quantify`, `ifc_plot`, `ifc_render`, `ifc_shape_list/docs/shape`, `ifc_list`, `ifc_docs`, `ifc_edit`. Install `pip install ifcopenshell-mcp`; stdio transport; edits are **not saved until `ifc_save`**. LGPLv3+ [5] | Directly relevant to MCP QA |
| **Bonsai** | See section 2 | |

**Why this matters for MCP testing.** Many IFC MCP servers call `ifcopenshell.api` and `ifcopenshell.util` underneath. Typical failures come from the library semantics: unit conversion, units of length (project in mm vs metres), missing `IfcOwnerHistory` in IFC2x3, GlobalId (22-character base64-like string) collisions, and schema differences (e.g. IFC2x3 has no `IfcWallType` PredefinedType values that IFC4 has) (examples from general knowledge, unverified).

---

## 2. Bonsai (formerly BlenderBIM)

- **What:** "a family of open source apps for authoring, reviewing, and sharing IFC models": **Bonsai Studio** (full IFC authoring inside Blender), **Bonsai Viewer** (lightweight desktop viewer), **Bonsai Web** (coming soon) [17].
- **Principle:** every edit reads/writes native IFC; powered by IfcOpenShell; scriptable in Python [17].
- **License:** GPL-3.0-or-later per the IfcOpenShell README [1]; the Bonsai site does not state one [17].
- **Maturity:** daily alpha builds (e.g. bonsai-0.9.1-alpha2611060155 on 2026-11-06) and stable 0.9.0.post1 [4]. Supported Blender versions are not stated on the pages read (unverified; check docs [18]).
- **Typical features:** spatial structure, walls/slabs/doors, types, property sets, classification, quantity take-off, drawings/annotations, 4D/5D, IDS and BCF panels (feature list from general knowledge; docs pages read did not enumerate them [18]).
- **Rename:** BlenderBIM became Bonsai (the site says only "formerly BlenderBIM"; the date is not stated [17]).

---

## 3. xBIM Toolkit (.NET)

| Component | Role | License / notes |
|---|---|---|
| **XbimEssentials** | Core .NET library: reads, writes, validates, queries IFC in STEP, IfcXML, IfcZip; IFC2x3 and IFC4 incl. Add2; .NET Standard 2.0/2.1, .NET 8, .NET 10 [19] | CDDL. About 1.7k commits, 582 stars [19] |
| **Xbim.Geometry** | Geometry engine (CLR interop + C++ on Open Cascade 7.6.3) producing meshes; build instructions are Windows-centric [20] | CDDL; OpenCASCADE under LGPL 2.1 with exception [19][20] |
| **XbimXplorer / Xbim.WindowsUI (Xbim.Presentation)** | Windows desktop (WPF) viewer/demonstrator, BCF plugin [21] | Targets .NET Framework 4.7; licence file not named in the page [21] |
| **Xbim.CobieExpress** | COBie support [19] | |
| **Xbim.IDS.Validator** | Validates models against IDS (reads IDS 0.9 and 1.0; works with IFC2x3, IFC4, IFC4.3) [22] | **AGPL-3.0**, unlike other xBIM parts; commercial license on request [22] |
| **XbimWebUI / WeXplorer** | Browser viewer [19] | legacy |

Key point: xBIM is the main choice when the host application is C#/.NET (for example, Windows services or Revit-adjacent add-ins). The geometry engine is Windows-bound, so Linux/Docker pipelines usually prefer IfcOpenShell (assessment from [20], partially inferred).

Class names testers may meet: `IfcStore.Open(...)`, `Xbim3DModelContext` (geometry creation), `model.Instances.OfType<IIfcWall>()` (from general knowledge, unverified in fetched pages; see docs [46]).

---

## 4. web-ifc, That Open Engine (ex IFC.js), components, fragments

- **web-ifc** [23]: "Reading and writing IFC files with Javascript, at native speeds." C++ compiled to WebAssembly with JS/TS API; also usable from C++. License **MPL-2.0**. `npm install web-ifc`. Basic flow: create `IfcAPI`, `Init()`, `OpenModel(data)`, query, `CloseModel()`. About 1.1k stars. Releases list shows 0.78 as latest (21 Sep, year not shown on the page) with 0.77 (6 Mar) and 0.76 (2 Mar) before it; recent work covers alignment, clothoid, sectioned-solid and boolean controls [24]. Version numbers are 0.x: API can break between versions.
- **@thatopen/components** [25]: MIT, built on Three.js; features such as postproduction, dimensions, floorplan navigation, DXF export. Two packages: `@thatopen/components` (browser and Node) and `@thatopen/components-front` (browser only). About 729 stars [25].
- **@thatopen/fragments** [26]: MIT. An open BIM format built on Google FlatBuffers, optimised for large datasets, with a Three.js-based viewer layer. It is **not IFC itself**; the built-in **IfcImporter** converts IFC to Fragments (frontend or backend) [26].
- **Naming history:** the project was formerly called IFC.js and is now "That Open Company/Engine". The pages read do not describe the rename; stated from general knowledge (unverified). Docs: [27].
- **Typical use:** browser viewers, apps that load an IFC, show properties, hide/isolate by category, export screenshots. Not an authoring/edit tool in the IfcOpenShell sense.

---

## 5. Other libraries and tools (one by one)

| Project | Language / license | Purpose | Maturity / notes |
|---|---|---|---|
| **IFC++ (IfcPlusPlus)** | C++, MIT [28] | IFC class model and STEP reader/writer, simple Qt/OpenSceneGraph viewer | README says it is **no longer actively developed** and recommends xeoIFC for new projects (WebAssembly/WebGPU) [28]. Supported IFC versions not stated on page |
| **GeometryGym IFC** | C#, MIT (LICENSE file reads "The MIT License (MIT)") [29][30] | Classes to generate and parse IFC (IFC2x3, IFC4, infrastructure extensions IFC4.3/4.4 and early newer-version support) [29] | Used by GeometryGym's Rhino/Grasshopper/Tekla-oriented plugins (plugin list not verified). About 312 stars [29] |
| **BIMserver** | Java, AGPL-3.0 (bundled plugins may differ) [31] | Server storing IFC as objects, not files; query, merge, filter, versioning, multi-user, notifications | Latest seen release 1.5.188 (31 Jul, year not shown) [32]. IFC schema support not stated. Aging stack, but still widely referenced in research |
| **Apstex IFC Framework** | Java; free for research/prototypes, **commercial licence for commercial use** [33] | Toolboxes plus Java and WebGL viewers; 2010 fork of the discontinued Open IFC Tools; supports buildingSMART IFC4 certification | Not "open source" in the OSI sense; the page does not mention an "IfcSDK" [33] |
| **IfcDoc** | C#, buildingSMART tool historically used to author IFC schema documentation (general knowledge) | Schema documentation generator | Repo URL not verified (guessed GitHub paths returned 404); the IFC4.3 docs are now built from other repos (e.g. "Standards-builds" in the buildingSMART org [44]). Treat as **legacy (unverified)** |
| **ifcJSON** | Spec + Python converters, MIT [34] | JSON serialization of IFC (ifcJSON-4 for IFC4 and IFC4.3), round-trip with SPF, JSON Schema generation | 80 commits, 169 stars; no releases; community, not an ISO format [34]. Do not confuse with IFC5 "IFCX" (a different JSON-based approach) |
| **Hypar Elements** | C#/.NET, MIT [35] | Code library for generating buildings ("smallest useful BIM"); `Elements.Serialization.IFC` serializes models to IFC (export; import not mentioned) [35] | 5.5k commits, 421 stars [35] |
| **Speckle** | Connectors in C#, Apache-2.0 [36]; platform has web IFC upload [37] | Data platform with connectors (Revit, Rhino, AutoCAD/Civil 3D, ETABS, Tekla). Docs say IFC files can be dragged into the web app [37] | The connectors repo shows no IFC component [36]; the mechanism of the IFC importer is not described in the pages read (unverified). IFC export is not described [37] |
| **xeokit-sdk** | JavaScript (WebGL), **AGPL-3.0**, commercial licence available from Creoox [38] | Browser 3D BIM viewer. Loads XKT, CityJSON, glTF, LAS, OBJ; IFC must be converted first [38] | 6.3k commits, 949 stars. From Sept 2026 the npm package is to ship ES-module builds only [38] |
| **xeokit-convert** | JS/Node, AGPL-3.0 [39] | `convert2xkt` CLI: `node convert2xkt.js -s model.ifc -o model.ifc.xkt -l`. Direct IFC conversion uses web-ifc and is labelled **alpha**, with limited property-set support; production recommendation is IFC to GLB (cxConverter) then GLB to XKT [39] | Replaces deprecated xeokit-gltf-to-xkt |
| **dotbim (.bim)** | JSON format, MIT; libraries in C# (NuGet), Python (`dotbimpy`, `dotbim-community`), Rust (`dotbim_rust`), TypeScript [40] | Minimalist BIM: only triangulated meshes plus attributes; converters to and from IFC (`dotbim-ifc`) [40] | Schema 1.1.0, 203 stars. Not a replacement for IFC semantics |
| **ifc-lite** | Rust core to WASM + TypeScript, MPL-2.0 [41] | Parse/view/query/edit/validate IFC client-side; IFC2X3, IFC4, IFC4X3 and IFC5 (IFCX); WebGPU viewer; IDS validation, clash, diff, BCF, DuckDB SQL; CLI and **an MCP server** [41] | Newer project: 6k commits, 461 stars [41]. Relevant as an alternative MCP backend |
| **Autodesk Revit IFC (revit-ifc)** | C#/.NET, LGPL-2.0; includes one proprietary DLL [45] | Open-source Revit add-in code for IFC export, link and export UI (Revit/Revit LT 2019+) [45] | Autodesk supports the current and two previous annual versions [45]. Import logic mostly stays inside Revit, not open [45] |
| **IDS Audit Tool** | .NET, MIT, buildingSMART [42] | Validates whether an `.ids` file itself is valid | Not a model checker |
| **Rust / Go / other** | See ifc-lite, dotbim_rust above | Dedicated pure-Rust crate "ifc-rs" and Go libraries: not verified (a guessed repo URL returned 404; the web-search quota was exhausted) | Mentioned only as a gap |

---

## 6. Which library for what

| Task | Best choice | Alternatives / caveats |
|---|---|---|
| Read properties and structure from IFC in Python | IfcOpenShell (`open`, `by_type`, `util.element.get_psets`) | ifc-lite for TS/Rust; xBIM for C# |
| Edit/create IFC safely (keep relationships valid) | `ifcopenshell.api` | raw `create_entity` risks broken relations |
| Give an LLM tools to query and edit IFC | IfcMCP (`ifcopenshell-mcp`) [5]; ifc-lite MCP [41] | custom MCP built on ifcopenshell |
| Convert IFC to OBJ/glTF/DAE/STEP | IfcConvert | web-ifc + own export; xeokit-convert for XKT |
| Fix or transform an IFC (merge, split, change units, shift coordinates) | IfcPatch recipes | |
| Spreadsheet round trip (Excel properties) | IfcCSV | custom pandas code |
| Compare two versions of a model | IfcDiff | |
| Check against client requirements (IDS) | IfcTester (Python), Xbim.IDS.Validator (.NET, AGPL), ifc-lite | IDS Audit Tool checks the IDS file only |
| Clash detection scripts | IfcClash | Navisworks/Solibri (not open source) |
| 4D/5D scheduling in IFC | Ifc4D / Ifc5D | |
| BCF issues | `bcf` Python library, xBIM BCF plugin | |
| Authoring IFC natively with a GUI | Bonsai Studio | proprietary: Revit, ArchiCAD |
| Web viewer for IFC | That Open components + web-ifc + fragments | xeokit (AGPL; needs conversion) |
| Large federated model viewing on desktop | Bonsai Viewer | xBIM Xplorer (Windows) |
| .NET desktop/server app | xBIM Essentials + Geometry | GeometryGym, Hypar (generation) |
| Model server with versioning | BIMserver (AGPL) | Speckle (platform) |
| Generate buildings from code (C#) | Hypar Elements | IfcOpenShell api |
| Lightweight mesh interchange | dotbim | glTF |
| Export from Revit | Revit's built-in IFC exporter / revit-ifc [45] | then fix with IfcPatch recipes (FixRevitTINs etc.) [7] |
| Commercial closed-source product embedding | Prefer permissive/weak copyleft: IfcOpenShell (LGPL), xBIM (CDDL), web-ifc (MPL-2.0), IFC++ (MIT) | Avoid AGPL (BIMserver, xeokit, Xbim.IDS.Validator) without a commercial licence |

License cheat sheet (from the sources above): MIT = IFC++, GeometryGym, Hypar, ifcJSON, dotbim, That Open components/fragments, IDS Audit Tool. MPL-2.0 = web-ifc, ifc-lite. LGPL = IfcOpenShell core, revit-ifc (LGPL-2.0). GPL = Bonsai. CDDL = xBIM Essentials/Geometry. AGPL-3.0 = BIMserver, xeokit-sdk/convert, Xbim.IDS.Validator. Apache-2.0 = Speckle connectors. Commercial: Apstex.

---

## Typical questions people ask about this

I could not retrieve real forum threads (web-search quota exhausted during research), so all questions below are **(illustrative)**, but they match the type of requests seen around these tools.

1. (illustrative) Which Python library should I use to read IFC property sets, and how do I install it?
2. (illustrative) How do I list all walls with a FireRating of 2HR in an IFC file?
3. (illustrative) My IfcOpenShell script created a wall but it does not show in Bonsai or any viewer; why? (missing representation, container or placement)
4. (illustrative) How do I assign an element to a storey with the API (`spatial.assign_container`)?
5. (illustrative) Why does `ifcopenshell.api.run` complain about an unknown function or argument after I upgraded to 0.9?
6. (illustrative) What is the difference between IfcOpenShell, Bonsai and BlenderBIM?
7. (illustrative) Can I convert IFC to glTF/GLB without Blender? (IfcConvert)
8. (illustrative) How do I convert an IFC to Excel and push edited values back? (IfcCSV)
9. (illustrative) How do I merge two IFC files or change the units from mm to m? (IfcPatch MergeProjects, ConvertLengthUnit)
10. (illustrative) Why is my model 100 km from the origin in the viewer? (SetFalseOrigin, OffsetObjectPlacements, georeferencing)
11. (illustrative) How can I check if my IFC meets the client's IDS file, and which tool is free?
12. (illustrative) Does xBIM work on Linux or in a Docker container? (geometry engine is Windows-centric)
13. (illustrative) Can I use xeokit or BIMserver in a commercial product? (AGPL question)
14. (illustrative) How do I show an IFC in a web page with That Open components? Why do I need the `web-ifc` WASM file path?
15. (illustrative) Is IFC.js the same as That Open Engine / web-ifc?
16. (illustrative) What are Fragments and do I still need the original IFC?
17. (illustrative) Is IFC++ still maintained? What replaces it?
18. (illustrative) Which tool can compare two IFC versions and tell me what changed? (IfcDiff)
19. (illustrative) Does the MCP server save my IFC edits automatically? (IfcMCP: no, call `ifc_save`)
20. (illustrative) My Revit IFC export has wrong spaces or door swings in ArchiCAD; any free fix? (IfcPatch recipes)
21. (illustrative) Can Speckle import IFC, and does it keep property sets?
22. (illustrative) Is IFC5/IFCX supported by IfcOpenShell? (the 0.9.0.post1 wheel ships IFC2X3, IFC4, IFC4X3 only)
23. (illustrative) Is ifcJSON an official buildingSMART standard?

---

## Common pitfalls and misconceptions

- **"Open source" is not one license.** AGPL (BIMserver, xeokit, Xbim.IDS.Validator) forces source disclosure of network services. Apstex is free only for research/prototypes [33].
- **Fragments, XKT, .bim and glTF are not IFC.** They are viewing/transport formats; semantics (property sets, relationships) may be partly lost. xeokit-convert's direct IFC path is alpha with limited psets [39].
- **Bonsai is not a separate IFC library.** It is a Blender add-on (GPL) over IfcOpenShell.
- **IfcOpenShell schema support changes between versions.** Repo README lists 2x3, 4, 4x1, 4x2, 4x3 [1], the 0.9.0.post1 wheel only 2X3, 4, 4X3 [4].
- **Geometry vs data.** IfcOpenShell geometry covers 2x3 and 4 per README [1]; IFC4.3 infrastructure geometry (alignments, clothoids) is still evolving in web-ifc (releases mention clothoid and alignment fixes [24]).
- **Using `create_entity` instead of `ifcopenshell.api`** yields files that open but have broken relationships.
- **In-memory edits.** IfcMCP does not auto-save [5]; tests must call save before checking the file.
- **web-ifc is 0.x** and the exact release year is not displayed on the release page [24]; pin versions.
- **MCP vs Revit.** These libraries edit IFC files, not live Revit models. Revit-driving MCP servers use the Revit API (outside this document). Revit's IFC export is configured in the exporter [45].
- **BIMserver age.** It is stable but Java/AGPL and not the usual choice for new projects (assessment, unverified).
- **IfcDoc is a legacy documentation tool**, not an IFC reader library (unverified).

---

## Gaps and notes

- The web-search quota ran out at the start of the run, so only direct page fetches were possible. Consequently: no real user questions with links, no verified info on Go libraries, a separate Rust crate "ifc-rs", IfcDoc's current repo, buildingSMART's software-implementations page (HTTP 403), npm statistics (HTTP 403).
- IfcOpenShell docs pages for IfcConvert/IfcTester/IfcClash on docs.ifcopenshell.org returned only navigation; details come from GitHub READMEs at the v0.8.0 tag, which may lag the 0.9 release.
- No pirated, crack or suspicious sites were encountered or linked.
- Star/commit counts and dates were captured on 2026-11-06 and change daily.

## Sources

1. https://github.com/IfcOpenShell/IfcOpenShell
2. https://docs.ifcopenshell.org/
3. https://pypi.org/project/ifcopenshell/
4. https://github.com/IfcOpenShell/IfcOpenShell/releases
5. https://github.com/IfcOpenShell/IfcOpenShell/tree/v0.8.0/src/ifcmcp
6. https://github.com/IfcOpenShell/IfcOpenShell/tree/v0.8.0/src/ifcquery
7. https://github.com/IfcOpenShell/IfcOpenShell/tree/v0.8.0/src/ifcpatch
8. https://github.com/IfcOpenShell/IfcOpenShell/tree/v0.8.0/src/ifcclash
9. https://github.com/IfcOpenShell/IfcOpenShell/tree/v0.8.0/src/ifctester
10. https://github.com/IfcOpenShell/IfcOpenShell/tree/v0.8.0/src/ifccsv
11. https://github.com/IfcOpenShell/IfcOpenShell/tree/v0.8.0/src/ifcdiff
12. https://github.com/IfcOpenShell/IfcOpenShell/tree/v0.8.0/src/ifc4d
13. https://github.com/IfcOpenShell/IfcOpenShell/tree/v0.8.0/src/bcf
14. https://github.com/IfcOpenShell/IfcOpenShell/tree/v0.8.0/src/ifcopenshell-python/ifcopenshell/api
15. https://github.com/IfcOpenShell/IfcOpenShell/tree/v0.8.0/src/ifcopenshell-python/ifcopenshell/util
16. https://github.com/IfcOpenShell/IfcOpenShell/tree/v0.8.0/src/ifcconvert
17. https://bonsaibim.org/
18. https://docs.bonsaibim.org/
19. https://github.com/xBimTeam/XbimEssentials
20. https://github.com/xBimTeam/XbimGeometry
21. https://github.com/xBimTeam/XbimWindowsUI
22. https://github.com/xBimTeam/Xbim.IDS.Validator
23. https://github.com/ThatOpen/engine_web-ifc
24. https://github.com/ThatOpen/engine_web-ifc/releases
25. https://github.com/ThatOpen/engine_components
26. https://github.com/ThatOpen/engine_fragment
27. https://docs.thatopen.com/intro
28. https://github.com/ifcquery/ifcplusplus
29. https://github.com/GeometryGym/GeometryGymIFC
30. https://raw.githubusercontent.com/GeometryGym/GeometryGymIFC/master/LICENSE
31. https://github.com/opensourceBIM/BIMserver
32. https://github.com/opensourceBIM/BIMserver/releases
33. https://www.apstex.com/
34. https://github.com/buildingSMART/ifcJSON
35. https://github.com/hypar-io/Elements
36. https://github.com/specklesystems/speckle-sharp-connectors
37. https://docs.speckle.systems/
38. https://github.com/xeokit/xeokit-sdk
39. https://github.com/xeokit/xeokit-convert
40. https://github.com/paireks/dotbim
41. https://github.com/louistrue/ifc-lite
42. https://github.com/buildingSMART/IDS-Audit-tool
43. https://github.com/buildingSMART/IDS
44. https://github.com/buildingSMART
45. https://github.com/Autodesk/revit-ifc
46. https://docs.xbim.net/
