# IFC in other authoring tools: Archicad, Tekla, Allplan, Vectorworks, Bentley, Civil 3D, BricsCAD, Renga, nanoCAD, BIMBase/Glodon/PKPM, GLOOBE, Edificius, SketchUp, Rhino, FreeCAD, Bonsai

Last researched: 2026-11-06

## In plain words

IFC (Industry Foundation Classes, buildingSMART, ISO 16739) is the neutral file format that lets different BIM programs exchange a building model. Revit is only one of many programs that write and read IFC; each other tool has its own export dialog, its own way of mapping its internal objects and properties to IFC entities (IfcWall, IfcBeam, IfcSpace...) and property sets (Pset_WallCommon...), and its own list of supported IFC versions. The same model exported from two programs, or opened in two viewers, will therefore often look slightly different. For a QA tester of MCP servers (tools that open, query and edit IFC files and drive Revit), this matters because test files will come from many different authoring tools, and the "same" IFC concept can show up under different names, different schemas (IFC2x3 vs IFC4 vs IFC4.3) and with different completeness.

**Research-quality warning (read first).** This document was produced under a hard limit: the web-search tool refused every query (search budget exhausted at the start of the run), so only direct page fetches of guessed or known URLs were possible. Many vendor help sites returned 403/404 or empty shells. Facts confirmed from a fetched page carry a [n] marker. Everything else comes from general domain knowledge and is marked "(unverified)". Treat unverified items as leads to check, not as facts. See "Gaps" at the end.

## Background: IFC versions and views (context for all tools)

- IFC2x3 was released in February 2006; IFC4 in March 2013 (with later add-ons in 2015, 2016, 2017); IFC4.3 is listed up to "IFC4.3 Add2" (2024). IFC4.1 and IFC4.2 are shown as withdrawn. IFC is registered with ISO as ISO 16739-1:2024. [1]
- Model View Definitions (MVD) are subsets of the schema for a specific exchange purpose. Typical ones (from general knowledge, unverified in this run because buildingSMART pages returned 403): IFC2x3 Coordination View 2.0 (the long-time default), IFC4 Reference View (read-only coordination), IFC4 Design Transfer View (editable transfer between authoring tools). IFC4.3 has no widely adopted certified MVD yet for most vendors (unverified).
- buildingSMART certification program: software is certified per schema + MVD + direction (import or export). The official list of participants is at buildingsmart.org / technical.buildingsmart.org; the page returned 403 to the fetch tool in this run, so certification statuses below are only as good as the vendor pages that were readable. [3]
- Revit itself (for contrast): IFC support is provided by the open-source Autodesk "revit-ifc" add-on (LGPLv2), which overrides the built-in IFC support; the current annual version and two previous ones receive fixes; downloads on GitHub Releases. [2]

## Per-tool reference

### Summary comparison table

| Tool | IFC schemas (as found) | Certification (as found) | Where settings live | Evidence |
|---|---|---|---|---|
| Archicad (Graphisoft) | IFC2x3 and IFC4 (unverified) | Certified for several MVDs (unverified detail) | File > Interoperability > IFC (translators, IFC Manager) (unverified path) | Only Wikipedia/marketing pages readable [4] |
| Tekla Structures | IFC2X3, IFC4, IFC4.3 listed; ifcXML only with 2x3 | buildingSMART certification for IFC2x3 and IFC4 import and export | Export dialog; File > Settings > IFC object conversion settings; Manage tab > Convert IFC objects | Official docs [5][6] |
| Allplan | IFC2x3, IFC4 (unverified) | Certified (unverified detail) | File > Export > IFC (unverified path) | Not verified |
| Vectorworks | IFC2x3, IFC4 (partly unverified) | First architectural developer with IFC4 Export Certification, April 2019 | File > Export > Export IFC Project (unverified) | Wikipedia [7] |
| Bentley (OpenBuildings, OpenRoads, etc.) | IFC2x3, IFC4 (unverified) | Not verified | iModel/IFC export in each product (unverified) | Not verified |
| Civil 3D | IFC 4.3 via an extension | Not verified | "IFC 4.3 Extension for Autodesk Civil 3D" topic exists in the 2025 Help | Help index [8] |
| BricsCAD BIM | IFC 4.3 (per Wikipedia) | Described as certified for IFC 4.3 import and export | Commands such as IFCEXPORT/IFCIMPORT (unverified) | Wikipedia [9] |
| Renga | IFC2x3, IFC4 (unverified) | Not verified | Not verified | Not verified |
| nanoCAD | IFC export in BIM modules (unverified) | Not verified | Not verified | Not verified |
| BIMBase / Glodon / PKPM | Own formats plus IFC (unverified) | Not verified | Not verified | Not verified |
| GLOOBE | Not verified | Not verified | Not verified | Not verified |
| Edificius (ACCA) | IFC2x3/IFC4 (unverified) | Not verified | Not verified | Not verified |
| SketchUp | IFC listed as ".IFC (.IFCZIP)" import and export | Not verified | File > Import / Export (unverified); plan scope not stated | Wikipedia [10] |
| Rhino | Not verified (Rhino 8 IFC support is a lead to check) | Not verified | Not verified | Not verified |
| FreeCAD (BIM workbench) | Default export IFC4; schema from IfcOpenShell | Not verified | Preference `DefaultIfcExportVersion` | Source code [11], Wikipedia [12] |
| Bonsai (ex-BlenderBIM) | IFC2X3, IFC4, IFC4X3 selectable at project creation | Not verified | Project Info panel; File > Save IFC Project | Official docs [13] |

### Archicad (Graphisoft, Hungary / Nemetschek group)

- Graphisoft was a founder of the OPEN BIM concept and is an active buildingSMART member. [4][14] Wikipedia lists Archicad version 30 (2026) as current stable. [4]
- Import/export: Archicad imports and exports IFC, DWG, DXF and BCF. [4]
- Settings (all unverified, the help site would not load): export and import behaviour is controlled by "IFC Translators" (named presets for export and import). A translator bundles schema/MVD choice, geometry conversion (extrusions/BREP), what is exported (properties, classification, element types), and the mapping rules. The "IFC Manager" holds mapping tables: Type mapping (Archicad element/classification to IFC entity), Property mapping (Archicad properties to IFC property sets) and Classification mapping. Look under File > Interoperability > IFC. Archicad 28 help is at help.graphisoft.com/AC/28/INT/ (the root page loads but its IFC topic URLs could not be discovered).
- Typical issues users report (unverified, general community knowledge): wrong IFC entity because of missing mapping (Objects exported as IfcBuildingElementProxy), property sets missing because the translator does not export user-defined properties, walls and slabs exported as Breps with no type information when "Export geometry as BREP" is chosen, large model size from composite structures, and differences between IFC2x3 and IFC4 handling of quantities.

### Tekla Structures (Trimble)

- Official docs (2025): IFC schemas listed are IFC 2X3, IFC 4 and IFC 4.3. Certified MVDs cover IFC 2x3 and IFC 4, for both import and export. IFC export has buildingSMART International certification. [5]
- Formats: .ifc and .ifcXML (ifcXML only with IFC 2x3), compressed (.ifcZIP) or uncompressed. [5]
- Objects exported: beams, columns, braces, slabs, panels, plates, reinforcing bars, pours, bolts with nuts and washers. [5]
- Property mapping: IFC property sets are defined in property set configuration files. You can modify existing sets and their binding to IFC entities, add buildingSMART property sets, or create new sets from template attributes and user-defined attributes (UDAs). [5] The product guide has separate topics "Modify property sets for IFC export" and "Create new property sets for IFC export". [5]
- Import side ("IFC object converter"): reference models are inserted as IFC. To turn IFC objects into native Tekla objects: File menu > Settings > IFC object conversion settings; Manage tab > Convert IFC objects (for selected reference-model objects); or open a reference model in the Reference models list and click the Start IFC object conversion change management button. [6]
- Converter configuration: Set handles to top flange; Convert B-rep object (becomes items in shape catalog, class 996); primary/secondary profile mapping by name or dimensions; tolerance; property-to-UDA copying (names limited to 20 characters, UDA must exist in objects.inp, types string/int/double); a Check button to list missing profiles and materials. Mapping and catalog files live in the model's attributes folder. [6]
- Converter limits: IFC2x3 Coordination View 2.0 is required for conversion to native profiles, otherwise objects become items; IFC4 formats (4.0, 4.1 and later) are not supported by the converter; bolts, reinforcement and welds cannot be converted; supported entities include IfcBeam, IfcColumn, IfcMember, IfcPlate, IfcSlab, IfcWall; only SweptSolid, Brep, CSG and Clipping representations; special profiles (WQ, Deltabeam) and profile offsets are not handled well; chamfers may convert incorrectly. [6]
- Checking exports: insert the exported IFC as a reference model in the original model, colour the two differently, use clip planes, compare object counts and read the export log; objects that fail to export are often caused by unnecessary cuts; fix by remodelling or set the object's IFC export type to Brep. Trimble Connector is recommended for viewing. [15]
- Note: the "Export in IFC format" topic and the exact dialog fields (output type, property set selection, entity override, coordinate system choices) could not be fetched; consult the linked Tekla topic. [5]

### Allplan (Nemetschek group, Germany)

Not verified in this run (the help site root returned a nearly empty page and Wikipedia returned 404). Leads to check (unverified): export under File > Export (IFC), IFC2x3 and IFC4 options, property mapping through Allplan attributes assigned to IFC property sets, Allplan is generally listed as a certified implementation. Official starting point: help.allplan.com.

### Vectorworks (Vectorworks Inc., Nemetschek group)

- Wikipedia states Vectorworks was "the first architectural software developer to receive the IFC4 Export Certification" in April 2019 from buildingSMART International. [7]
- Settings (unverified): export via File > Export > Export IFC Project with options for IFC version and view definition; mapping through the IFC Data tool/palette on objects and IFC data in object info; custom property sets per object. Import via File > Import > Import IFC Project.
- Typical issues (unverified): objects exported with the wrong IFC entity unless IFC data is assigned; symbol-based objects losing parametric intelligence; large Brep outputs.

### Bentley Systems (OpenBuildings Designer, OpenRoads, MicroStation, iTwin)

Not verified in this run. Leads (unverified): Bentley exports IFC from MicroStation-based products and from iModel workflows; relevant for infrastructure (roads, rail, bridges) where IFC4.3 adoption matters; check docs.bentley.com and communities.bentley.com. IFC4.3 (ISO 16739-1:2024) adds alignment and infrastructure entities. [1]

### Autodesk Civil 3D

- The Civil 3D 2025 Help index lists a topic "IFC 4.3 Extension for Autodesk Civil 3D"; its URL and content could not be read. [8] This implies IFC 4.3 export is delivered as an extension rather than a native command in 2025 (inference).
- Typical flow (unverified): corridors, alignments and surfaces are mapped to IFC 4.3 infrastructure entities (IfcAlignment, IfcRoad, IfcFacility etc.); users should check results in a 4.3-capable viewer because many viewers still only handle IFC2x3/IFC4.

### BricsCAD BIM (Bricsys, Belgium, Hexagon group)

- Wikipedia says only BricsCAD BIM supports IFC, describes it as "certified for Industry Foundation Classes (IFC) 4.3 import and export", and says Bricsys joined buildingSMART International in December 2016. [9] This certification claim comes from Wikipedia, not from the buildingSMART list (unverified).
- BIMIFY uses AI to classify generic 3D geometry into IFC-compliant BIM elements. [9] That classification step is where IFC entities are assigned, so wrong classification gives wrong IfcType on export.
- Settings and commands: IFCEXPORT / IFCIMPORT and the BIM classification panel (unverified; the help page URL guessed returned 404).

### Renga (Russia; Renga Software, joint venture of ASCON and 1C)

Not verified. Wikipedia page and help site were not reachable. Leads (unverified): Renga Architecture / Renga Structure / MEP; import and export IFC (IFC2x3, IFC4); relevance for Russian state requirements for information models (see below). Native terms: Ренга; информационная модель = information model.

### nanoCAD (Nanosoft / Нанософт, Russia)

Not verified. Leads (unverified): nanoCAD BIM Стройплощадка / nanoCAD BIM Конструкции / nanoCAD ОПС exporting to IFC; IFC used to move models into Renga or Revit.

### BIMBase / Glodon / PKPM (China)

Not verified. Leads (unverified): BIMBase (from PKPM's developer, 构力) and Glodon (广联达) are Chinese BIM platforms with their own native formats; IFC import/export is secondary, and Chinese domestic IFC-based standards exist (names not verified). Search terms for later: 工业基础类 IFC 标准, BIMBase IFC 导出, 广联达 IFC 导入.

### GLOOBE (likely Fukui Computer, Japan; vendor unverified)

Not verified, including who makes it. Search terms for later: GLOOBE IFC 書き出し, 福井コンピュータ IFC, buildingSMART Japan IFC検定.

### Edificius (ACCA software, Italy)

Not verified. Leads (unverified): ACCA's Edificius is the architectural BIM tool in the usBIM ecosystem, with IFC import/export (IFC2x3/IFC4); Italian terms: esportazione IFC, modello BIM, "BIM autore" authoring tool.

### SketchUp (Trimble)

- IFC appears in SketchUp's supported 3D import and export formats as ".IFC (.IFCZIP)". [10] Which subscription (Pro/Studio) and which IFC versions are covered was not stated on the page read. [10]
- Typical workflow (unverified): assign IFC classification to groups/components (IFC 2x3 or IFC 4 classification schemas), then File > Export > 3D Model > IFC. Untagged geometry exports as IfcBuildingElementProxy.
- Tekla Structures also documents exporting to SketchUp (topic `int_exporting_to_sketchup`). [5]

### Rhino (McNeel)

Not verified. Docs page was empty. Leads (unverified): Rhino 8 added IFC import/export; Rhino.Inside.Revit, Grasshopper add-ons and Speckle are common bridges. Objects need IFC type assignment (user text or plugin) to export meaningfully.

### FreeCAD (BIM workbench)

- Wikipedia: FreeCAD 1.0 (November 2024) has a new integrated BIM workbench; IFC is a listed import/export format. [12]
- Source code: the exporter uses IfcOpenShell, which must be installed; the schema is taken from IfcOpenShell when available, otherwise from the `DefaultIfcExportVersion` preference, defaulting to IFC4. [11]
- Official wiki (wiki.freecad.org/Arch_IFC) sat behind bot protection and could not be read. Settings location is in Preferences > Import-Export > IFC (unverified).
- Typical issues (unverified): FreeCAD objects without IFC type become IfcBuildingElementProxy; tolerance issues; export of large models is slow; round-trip import-export-import can lose parametric data.

### Bonsai (formerly BlenderBIM, built on IfcOpenShell)

- Bonsai is a family of apps; Bonsai Studio (native IFC authoring in Blender), Bonsai Viewer (desktop viewer for large federated models), Bonsai Web (browser, docs not yet available); built on IfcOpenShell. [16]
- Schema choice: in the Project Info panel the user can choose IFC2X3, IFC4 or IFC4X3. [13]
- Saving: Ctrl+S or File > Save IFC Project saves only the .ifc file, not the .blend; Save IFC Project As writes a new location/name. [13]
- Bonsai is IFC-native: the IFC file is the model, unlike other tools where IFC is an export. This makes it a good reference for checking what a "clean" IFC should look like. Troubleshooting doc and community links: docs.bonsaibim.org troubleshooting; community.osarch.org (community resource). [16]

## Property mapping approaches (cross-tool concepts)

| Approach | What it means | Tools using it (as found / unverified) |
|---|---|---|
| Preset translator / configuration file | One saved config controls schema, MVD, and mapping | Archicad translators (unverified), Tekla property set configuration files [5] |
| Per-object IFC data | User assigns IFC type/attributes on each object | Vectorworks (unverified), SketchUp classification (unverified), FreeCAD IFC type per object (unverified) |
| Classification-driven | Classification (e.g. Uniclass/OmniClass) selects IFC entity | Archicad (unverified), BricsCAD BIMIFY [9] |
| UDA/attribute to property set | User-defined attributes become Psets | Tekla [5] |
| Native IFC | No mapping; the model is IFC | Bonsai [13] |

Key QA implication: when an MCP server reports "this IFC has 300 IfcBuildingElementProxy elements," the cause is usually an unmapped object in the authoring tool (unverified general knowledge), not a defect in the MCP server.

## Typical questions people ask about this

None of the questions below were found in live forums during this run (search was unavailable); all are illustrative.

1. Which IFC version should I export from Archicad/Tekla/Allplan to open the model in Revit? (illustrative)
2. What is the difference between IFC2x3 Coordination View 2.0 and IFC4 Reference View? (illustrative)
3. Why do my Tekla objects arrive in Revit as generic elements? (illustrative; see Tekla Brep export type note [15])
4. Can Tekla convert an IFC4 model into native parts? (answer from docs: the converter does not support IFC4 formats [6])
5. Why does Tekla's IFC export say certified for 2x3 and 4 but not 4.3? (illustrative; docs list 4.3 as a schema but certified MVDs only for 2x3 and 4 [5])
6. How do I add my own properties to an IFC export from Tekla? (answer: property set configuration files, UDAs [5])
7. Why are walls exported as IfcBuildingElementProxy from SketchUp? (illustrative)
8. Does BricsCAD really support IFC 4.3? (illustrative; Wikipedia says certified for import and export [9])
9. How do I export a Civil 3D corridor to IFC 4.3? (illustrative; extension topic exists [8])
10. Is Vectorworks IFC4 export certified? (answer: Wikipedia says yes since April 2019 [7])
11. Which free tool should I use to check an IFC from any authoring tool? (illustrative; Bonsai Viewer, FreeCAD, Trimble Connector are examples [16][11][15])
12. What IFC schema does FreeCAD write by default? (answer: IFC4 unless IfcOpenShell dictates otherwise [11])
13. How do I save only the IFC file in Bonsai without a .blend? (answer: File > Save IFC Project [13])
14. Why do object counts differ between my authoring model and the exported IFC? (illustrative; see Tekla check workflow [15])
15. Does the Revit IFC exporter get updated separately from Revit? (answer: yes, the open-source revit-ifc add-on [2])
16. Which Russian BIM software exports IFC and is it accepted by state expertise? (illustrative, unverified)
17. How do I get IFC out of Japanese BIM software like GLOOBE? (illustrative, unverified)
18. Why does my viewer show nothing for an IFC4.3 file? (illustrative; many viewers only support IFC2x3/IFC4 [1])

## Common pitfalls and misconceptions

- "IFC is IFC": schema (2x3/4/4.3), MVD and vendor mapping all differ; certification is per schema, MVD and import/export direction. [5]
- "Certified" does not mean lossless; Tekla's own docs tell users to verify exports by counting objects and visually comparing. [15]
- Converting IFC back to native objects is limited: Tekla converts only certain entities and requires IFC2x3 CV 2.0 for native profiles; bolts, reinforcement and welds are not converted. [6]
- IFC4.1 and IFC4.2 are withdrawn; IFC4.3 (ISO 16739-1:2024) is the infrastructure-capable current line. [1]
- Wikipedia statements about certification (BricsCAD, Vectorworks) are secondary and should be checked against the buildingSMART certified list. [7][9]
- A Brep export keeps shape but drops parametric type information, which is the usual trade-off when a tool "falls back" to Brep. [15]
- Do not assume an MCP test failure is an MCP bug; first check whether the IFC itself (schema, entity, property sets) was written correctly by the authoring tool.

## Gaps (what could not be done)

- Web search was unavailable for the whole run (budget exhausted before the first query), so no forum threads, blogs or native-language (German, Russian, Chinese, Japanese, Italian) searches were possible. Native-language terms above are from general knowledge and not verified.
- Pages that returned 403 or bot protection: buildingSMART certified-software and implementations pages, buildingSMART standards pages (IFC4.3 and MVD documentation), FreeCAD wiki (bot protection).
- Pages that returned 404 or empty content (guessed URLs): Graphisoft help topics, Allplan help, Autodesk Civil 3D export topic, Vectorworks, BricsCAD help, SketchUp help, Rhino docs, several Wikipedia pages.
- No suspicious or pirated sites were encountered; none were linked.
- Not covered with evidence: Archicad, Allplan, Bentley, Renga, nanoCAD, BIMBase/Glodon/PKPM, GLOOBE, Edificius, Rhino. Re-run with working search access before relying on this file for these tools.

## Sources

1. https://en.wikipedia.org/wiki/Industry_Foundation_Classes (versions, ISO 16739-1:2024; secondary)
2. https://github.com/Autodesk/revit-ifc (Revit IFC open-source add-on)
3. https://technical.buildingsmart.org/services/certification/ifc-certification-participants/ (target of Tekla's link; returned 403 when fetched, cited only as the official list location)
4. https://en.wikipedia.org/wiki/Archicad (secondary)
5. https://support.tekla.com/doc/tekla-structures/2025/int_ifc_export (Tekla IFC export)
6. https://support.tekla.com/doc/tekla-structures/2025/int_conversion_management (Tekla IFC object converter)
7. https://en.wikipedia.org/wiki/Vectorworks (secondary)
8. https://help.autodesk.com/view/CIV3D/2025/ENU/ (Civil 3D 2025 Help index, mentions IFC 4.3 extension topic)
9. https://en.wikipedia.org/wiki/BricsCAD (secondary)
10. https://en.wikipedia.org/wiki/SketchUp (secondary)
11. https://github.com/FreeCAD/FreeCAD/blob/main/src/Mod/BIM/importers/exportIFC.py (FreeCAD exporter source)
12. https://en.wikipedia.org/wiki/FreeCAD (secondary)
13. https://docs.bonsaibim.org/studio/guides/authoring/starting_new_project.html (Bonsai new project, schema, saving)
14. https://graphisoft.com/solutions/open-bim (Graphisoft openBIM marketing page, French content)
15. https://support.tekla.com/doc/tekla-structures/2025/int_checking_exported_ifc_model (Tekla export checking)
16. https://docs.bonsaibim.org/ (Bonsai docs home; community links osarch.org)
17. https://support.tekla.com/doc/tekla-structures/2025/int_ifc_general_info (Tekla IFC general info)
18. https://support.tekla.com/doc/tekla-structures/2025/int_ifc_interoperability_concepts (Tekla geometry concepts)
