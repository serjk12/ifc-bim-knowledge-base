# Where to get sample IFC files for testing (and what each is good for)

## In plain words

IFC (Industry Foundation Classes, ISO 16739-1) is the neutral file format for building and infrastructure models. To test an MCP server that opens, queries or edits IFC (or that drives Revit and exports IFC), you need real files. Good ones are free and public. They differ in IFC version (2x3, 4, 4.3), discipline (architecture, structure, MEP, infrastructure), size, and how "clean" they are. This note is a map of the public sources, with link, licence, version and "what it is good for". It also lists purpose-built broken files and ways to make your own edge-case files. Links only: nothing here was downloaded, and nobody should download from this document blindly. Check each licence first.

Last researched: 2026-11-06

Research limits: the web-search tool ran out of budget early in this session. Everything below comes from direct page reads of GitHub repos, the IFC wiki and Wikipedia. No forum or blog search was possible, so the "questions" section is illustrative, not harvested (see Gaps).

---

## 1. Quick chooser

| I want to test... | Start with | Why |
|---|---|---|
| "Does it open an IFC at all?" (smoke test) | KIT `AC20-FZK-Haus.ifc` [3] or IfcOpenShell-style small models | Small, clean, IFC4, one building |
| IFC2x3 (still the most common in the field) | Duplex Apartment, Medical-Dental Clinic [2][5] | Classic IFC2x3 models, multi-discipline |
| MEP (ducts, pipes, electrical) | Duplex (MEP, Electrical, Plumbing files), Clinic (HVAC, Plumbing, Electrical) [5] | Separate discipline files |
| Structural | Clinic `Clinic_Structural.ifc` [5]; Simple-Scene `Building-Structural.ifc` [1] | |
| Multi-file federation (several models open together) | Duplex, Clinic, Simple-Scene (10 files) [1][5] | Needs a merge/federation scenario |
| Georeferencing / CRS | "Example project location" (IFC4, Amersfoort, EPSG 28992) [6]; xBIM `geographic-referencing-*.ifc` for 4.3 [11] | Documented coordinate pitfalls |
| IFC 4.3 infrastructure (road, rail, bridge, alignment) | Simple-Scene `Infra-*.ifc` [1]; KIT bridge/road [3]; Chesapeake Bay Bridge-Tunnel [7] | |
| Large size / performance | Chesapeake Bay Bridge-Tunnel (about 26 MB, 295k entities) [7]; Schependomlaan [8] | |
| Non-Latin text, encoding errors | xBIM `Wrongly1251Encoded.ifc`, `InvalidMultiByte.ifc` [10]; Estonian `Esplanades` [9] | Deliberately bad or non-English text |
| Broken / malformed files | xBIM `Tests/TestFiles` [10]; IfcOpenShell `files` repo [12] | Dozens of purpose-made failures |
| Geometry types (extrusion, BRep, NURBS, tessellation) | ISO spec example archive, NURBS folder, xBIM IFC4x3_ADD2 [11][13][14] | One feature per file |
| Real-world mess (planning, clashes, as-built) | Schependomlaan [8] | Real Dutch project with known errors |

---

## 2. buildingSMART official: Certification-datasets (formerly "Sample-Test-Files")

- Link: https://github.com/buildingSMART/Certification-datasets [1]
- The repo people remember as `buildingSMART/Sample-Test-Files` now opens as **Certification-datasets**. The README says previous user-curated content "has been moved" to the community organisation (see section 3) [1]. Old links and old tutorials may point to paths that no longer exist.
- Purpose (README): "simple models and files used for educational, implementation and certification purposes" [1].
- Licence: `LICENSE` file says the work is under Creative Commons Attribution 4.0 International; copyright buildingSMART International Ltd [1].
- Structure: one folder per schema version, named with the official identifier [1]:
  - `IFC 2.3.0.1 (IFC 2x3 TC1)`
  - `IFC 4.0.2.1 (IFC 4 ADD2 TC1)` : contains `Simple-Scene`, and `ISO Spec - ReferenceView_V1.2` [1]
  - `IFC 4.3.2.0 (IFC 4.3 ADD2)` : contains `Simple-Scene` [1]
- **Simple-Scene** (4.3 folder) lists 10 IFC files [1]: `Building-Architecture.ifc`, `Building-Hvac.ifc`, `Building-Landscaping.ifc`, `Building-Structural.ifc`, `Infra-Bridge.ifc`, `Infra-Electrical.ifc`, `Infra-Landscaping.ifc`, `Infra-Plumbing.ifc`, `Infra-Rail.ifc`, `Infra-Road.ifc`. The listing may be incomplete (the page said "View all files").
- Why it matters: the software-certification checklist uses this data. It has 15 criteria (0 to 14): load all 9 models together in one viewer; geometry; geolocation; projected CRS; spatial hierarchy (Project, Site, Building, Storey); materials; colours; properties at occurrence and type level with GUIDs; quantities; classification references; assemblies; IfcGroup/IfcSystem; IfcSpace; road surface and marking relationships (IFC 4.3 only) [15]. Those criteria are a ready-made list of "what a good IFC reader must show", useful for test-case design.
- Good for: a federated multi-discipline scene (building plus road, rail, bridge, electrical, plumbing, landscaping) and clean IFC 4.3 infrastructure.
- Not good for: stress or broken-file tests. These are small, clean demonstration files. File sizes not verified.

IFC version names used by buildingSMART (note the double naming): IFC2x3 TC1 = 2.3.0.1; IFC4 ADD2 TC1 = 4.0.2.1; IFC4.3 ADD2 = 4.3.2.0 [1]. The Wikipedia list gives IFC4.3 Add2 as 2024 and IFC4 Add2 TC1 as 2017 and registers IFC as ISO 16739-1:2024 [16]. Also on that page: formats `.ifc` (STEP, ISO 10303-21), `.ifcXML` (ISO 10303-28), `.ifcZIP` [16].

## 3. buildingSMART Community-Sample-Test-Files

- Link: https://github.com/buildingsmart-community/Community-Sample-Test-Files [2]
- README: community-made samples in IFC, BCF and IDS formats. They are "NOT official buildingSMART examples", and most do not pass the buildingSMART validation service [2]. Needs Git LFS to clone [2]. Contributions under CC BY 4.0 [2]. Contact given: technical@buildingsmart.org (organisation address).
- Folders [2]: `IFC 2.3.0.1 (IFC 2x3)`, `IFC 4.0.2.1 (IFC 4)`, `IFC 4.3.2.0 (IFC 4.3)`, `dev archive` (4.3 release-candidate archive).

Notable content (top-level listing only; sub-listings may be incomplete):

| Dataset | Path (under repo) | Version | What it is | Licence / terms | Good for |
|---|---|---|---|---|---|
| Duplex Apartment | IFC 2x3 / `Duplex Apartment` | IFC2x3 | Two-storey duplex. Files: `Duplex_A_20110907.ifc` (architecture), `Duplex_MEP_20110907.ifc`, `Duplex_Electrical_20121207.ifc`, `Duplex_Plumbing_20121113.ifc`, `Duplex_M_20111024_ROOMS_AND_SPACES.ifc`, plus COBie spreadsheets [4] | README asks to cite "BSI (2020) Duplex Apartment Test Files" [4]; licence line not confirmed in my read (unverified, probably CC BY 4.0 like the repo) | MEP, discipline split, rooms/spaces, COBie. Hosted by US NIBS 2009 to 2020, then moved [4] |
| Medical-Dental Clinic | IFC 2x3 / `Medical-Dental Clinic` | IFC2x3 | Real two-storey clinic, information redacted. `Clinic_Architectural/Electrical/HVAC/Plumbing/Structural.ifc` + COBie xlsx + `ClinicOM.zip` [5] | CC BY 4.0; credit "BSI (2020) Medical-Dental Test Files", state changes [5] | Full discipline set including structural + HVAC; shows size/complexity of Coordination MVD files; used in US "COBie Challenge" [5] |
| Schependomlaan | IFC 2x3 / `Schependomlaan` | IFC2x3 (folder), Archicad design model | Real Dutch housing project from a TU Eindhoven master's thesis: design IFC, subcontractor IFC/DWG, BCF clash issues, schedules, Synchro 4D IFC, point clouds, event logs [8] | No formal licence; "permission to use the data for scientific and academic purposes" [8] | Messy real-world data; 4D; BCF. Warning in README: "Some files contain some errors" [8] |
| Esplanades (Estonia) | IFC 2x3 / `Esplanades` | IFC2x3 | `1807_EP_AR_v18.ifc` architectural model by Esplan, plus Estonian modelling requirements xlsx [9] | CC BY 4.0 [9] | Non-English (Estonian) data, a national BIM requirement sheet |
| Molio | IFC 2x3 / `Molio` | IFC2x3 | `Molio_with_URIs.ifc`, `Molio_Example.ids`, video [17] | not stated in what I read | Classification URIs plus an IDS file |
| SDK - S1 | IFC 2x3 / `SDK - S1` | IFC2x3 | `bSDD_references_example.ifc`; the rest of the Sixty5/Strijp-S dataset is on external Trimble Connect links [18] | CC BY 4.0 [18] | bSDD references; student project data |
| Example project location | IFC 4 / `Example project location` | IFC4 (Revit 2020 export) | Sports hall in Amersfoort, NL; built to demonstrate IFC4 geolocation [6] | not confirmed (unverified) | Georeferencing traps: origin vs project base point, EPSG 28992 [6] |
| ISO Spec archive | IFC 4 / `ISO Spec archive` | IFC4 | ISO example files in four syntaxes (.ifc, .json, .ttl, .xml): beams, columns, basins, CSG, B-rep, tessellation, geographic-referencing, grid placement... [13] | not stated in what I read | One-feature-per-file geometry tests; README warns not all are valid [13] |
| NURBS | IFC 4 / `NURBS` | IFC4 | B-spline lines, surfaces, solids from different applications, each with a NURBS file and a tessellated fallback [14] | not stated | Curved geometry import; app-by-app comparison |
| Chesapeake Bay Bridge-Tunnel | IFC 4.3 / its folder | IFC4X3_ADD2 | Synthetic corridor model, about 26 MB, 295,445 entities, 17,553 elements, written with IfcOpenShell 0.8.0 [7] | folder has its own LICENSE; OpenStreetMap-derived geometry (ODbL) [7] | Large size; alignment-based infrastructure; explicit "not an as-built record" [7] |

Pitfall: "Duplex" and "Clinic" originally came from a US government hosting (NIBS). Many older blogs link to dead `nibs.org` URLs. The current home is this repo [4][5].

## 4. KIT (Karlsruhe Institute of Technology) examples: FZK-Haus, Institute, Smiley West, bridge, road

- Page: https://www.ifcwiki.org/index.php?title=KIT_IFC_Examples [3]. The KIT institute site only links to this wiki page [19].
- Terms: "unrestricted use"; if used in a publication, credit the Institute for Automation and Applied Informatics (IAI) at KIT [3].

| Model | Description | IFC | Origin |
|---|---|---|---|
| FZK Haus (`AC20-FZK-Haus.ifc`) | Fictional simple building | IFC4 | ArchiCAD 20 |
| Office Building (`AC20-Institute-Var-2.ifc`) | Fictional office building | IFC4 | ArchiCAD 20 |
| Smiley West (ZIP, `AC-20-Smiley-West-10-Bldg`) | Terraced houses | IFC4 | ArchiCAD 20 |
| KIT-Bridge (ZIP) | Fictional simple bridge | IFC 4x2 | SketchUp, hand-edited |
| KIT-Simple-Road-Test (ZIP) | Fictional simple road | IFC 4x3_RC2 | SketchUp, hand-edited |

Source: [3]. File sizes and disciplines are not on that page. FZK-Haus is a single-building architectural model (walls, windows, doors, roof, spaces) and is the de facto "hello world" in viewers. The same files are also shipped in other projects' test data: web-ifc's `tests/ifcfiles/public` contains `AC20-FZK-Haus.ifc` and `C20-Institute-Var-2.ifc` [20], and IfcOpenShell's `files/tests` has `AC20-Institute-Var-2_227944.ifc` [12].

Caution: the KIT road is **IFC4x3_RC2** (a release candidate), not the final IFC 4.3 ADD2. A reader strict about the final schema may reject or misread it. That makes it a useful "old 4.3 draft" test.

## 5. IfcOpenShell: `files` repo and test data

- Repo: https://github.com/IfcOpenShell/files [12]. Main IfcOpenShell repo: https://github.com/IfcOpenShell/IfcOpenShell (its `test/input` folder is a link to this `files` repo at a pinned commit) [21].
- README: "a collection of IFC files that are useful for testing" IfcOpenShell. Mostly regression/crash files named after bugs [12].
- Licence: not stated on the README page I read, and the library is LGPL (Bonsai GPL) [22]. Treat the sample files as licence-unknown (unverified). Do not redistribute inside your own deliverables without checking.
- Naming conventions (very useful when you pick a test) [12]:
  - number prefix = GitHub issue number (`487.ifc`)
  - `--augmented` = quantities added with `IfcConvert --calculate-quantities`
  - `--accept-errors` = file knowingly logs errors but must not crash
  - extension `.ifc_` = timeout-prone, excluded from normal runs
  - tags like `--segfault`, `--abort`, `--timeout`, `--no-geometry`, `--wrong-geometry`, `--missing-subtractions`; object tags like `--beam`, `--wall`, `--reinforcingBar`
  - examples: `1001--reinforcingBar--segfault.ifc`, `1948--wall--wrong-geometry--augmented.ifc`, `1269--Project_IfcDuctFitting.ifc` [12]
- Supported schemas of the library: IFC2x3 TC1, IFC4 Add2 TC1, IFC4x1, IFC4x2, IFC4x3 Add2 parse fully; geometry mainly for 2x3 and 4 [22].
- Good for: geometry-kernel torture tests (bad extrusions, reinforcement, ducts, curves), "wrong geometry" regressions, quantity checks.
- Also look at: `IfcOpenHouse` (a sample generated by IfcOpenShell; referenced in web-ifc as `IfcOpenHouse_IFC4.ifc` [20]; the source path I tried returned 404, so the original location is unverified).

## 6. That Open / web-ifc, xBIM, BIMData

**That Open Company (web-ifc, engine_components)**
- Repo: https://github.com/ThatOpen/engine_web-ifc, licence MPL-2.0 [20][23].
- README: "a library of test models in the tests/public folder", PRs with new models are invited [23].
- `tests/ifcfiles/public` contains ~30 files [20], including: `AC20-FZK-Haus.ifc`, `dental_clinic.ifc`, `duplex.ifc`, `schependomlaan.ifc`, `Office_A_20110811.ifc`, `IfcOpenHouse_IFC4.ifc`, `KIT-Simple-Road-Test-Web-IFC4x3_RC2.ifc`, `Viadotto Acerno.ifc`, `ifcbridge-model01.ifc`, `advanced_model.ifc`, `Sample_entities.ifc`, and bug-driven files `ISSUE_nnn_*.ifc` (e.g. `ISSUE_053_20181220Holter_Tower_10.ifczip`, `LTU_A-House_redesign.ifczip`) [20]. Names such as `ISSUE_098_R8_F1_MAB_AR_M3_XX_XXX_MO_7000.ifc` show typical real project naming (long, code-based).
- Good for: browser/WASM viewer tests, mixed real files, `.ifczip` handling. Licence per file is not stated; treat as unverified.

**xBIM (Xbim Essentials)**
- Repo: https://github.com/xBimTeam/XbimEssentials, licence: xBIM licence, based on CDDL [10][24]. Supports IFC2x3, IFC4 (Add2), STEP, IfcXml, IfcZip [10].
- **Best public source of deliberately broken files**: `Tests/TestFiles` [10] includes
  - encoding: `Wrongly1251Encoded.ifc`, `InvalidMultiByte.ifc`, `EmptyMultibyteString.ifc`, `SpecicalSolidusEscape.ifc`, `DoubleBackSlashName.ifc`, `NewlinesInStrings.ifc`, `BackSpaceInFileName.ifc`
  - syntax/structure: `Badly formed Ifc file.ifc`, `FormallyIllegalFile.ifc`, `InvalidHeaderFileName.ifc`, `Large_entity_label.ifc`, `RealWithExponent.ifc`, `fileWithAbstractClass.ifc`, `InvalidType.ifc`
  - geometry/values: `Axis2PlacementError.ifc`, `RadianValuesOverPI.ifc`, `LargeTriangulatedCoordinates.ifc`, `InvalidTriangulatedFaceSet.ifc`, `InvalidMonetaryUnit.ifc`
  - other syntaxes: `.ifcxml`, `.ifczip` (e.g. `InvalidNan.ifcxml`, `IkeaKitchenCabinets.ifcXML`, `HelloWallXml.ifczip`)
  - small clean ones: `SmallModelIfc2x3.ifc`, `SmallModelIfc4.ifc`, `4walls1floorSite.ifc`, `SampleHouse4.ifc` (README example) [10]
- `IFC4x3_ADD2/` has 46 files, mostly one-feature IFC 4.3 geometry examples: `geographic-referencing-gk.ifc`, `geographic-referencing-utm.ifc`, `geographic-referencing-rigid-operation.ifc`, `linear-placement-of-signal.ifc`, `reinforcing-assembly.ifc`, `structural-curve-member.ifc`, `tessellation-with-image-texture.ifc`, `construction-scheduling-task.ifc` [11]. `IFC4x3/` has sweep/sectioned solid files and `Header example.ifc` [25].
- What a file name guarantees: I only know the names. What exactly is wrong inside each "Invalid*" file I did not verify.

**BIMData**
- GitHub organisation https://github.com/bimdata has 47 repos, none of which I found to be a sample-model collection [26]. BIMData's docs sometimes use demo IFC files; I could not find a stable public sample link (unverified, gap).

## 7. Open IFC Model Repository (University of Auckland)

- Site: http://openifcmodel.cs.auckland.ac.nz/ (title "OpenIFC Model Repository") [27].
- My fetch returned only the page title, so model count, versions, licence and whether it is still maintained are **unverified**. From general knowledge it is an older academic repository of user-submitted IFC2x3-era models. Treat it as a historical source: links may be broken, and per-model licences vary. Check the site in a browser before relying on it.

## 8. Revit-side sources (the file is RVT, you export IFC)

For a Revit MCP, there are no IFC files to download. You use Autodesk sample projects and export. Autodesk's sample page lists [28]:
- Snowdon Towers (coordinated multi-discipline: Architectural, Electrical, Facades, HVAC, Plumbing, Site, Structural, plus point clouds)
- Architecture: `rac_basic_sample_project.rvt`, `rac_advanced_sample_project.rvt`, `DACH_sample_project.rvt`
- Structure: `rst_basic_sample_project.rvt`, `rst_advanced_sample_project.rvt`, `Technical_school-current_m.rvt` (the architectural link for the advanced structural sample)
- MEP: `rme_basic_sample_project.rvt`, `rme_advanced_sample_project.rvt`

Sizes and the file-format version per Revit year are not given on that page. Open in the matching or newer Revit; older Revit refuses newer files. Then File > Export > IFC (menu name per standard Revit; unverified for your year). Export settings (IFC2x3 Coordination View 2.0 vs IFC4 Reference View / Design Transfer View) change what the result is good for; the Amersfoort README itself shows how a Revit export can put the origin 100 m off [6].

## 9. IFC 4.3 / infrastructure: where it lives

- Official spec home: https://ifc43-docs.standards.buildingsmart.org/ (redirects to standards.buildingsmart.org [29]; my direct fetch of the target returned 403, so version text there is unverified). Development repo `buildingSMART/IFC4.3.x-development`: branch `ifc4.3-main` is IFC4.3.2.0 with post-ISO corrections; formal static releases are CC BY-ND 4.0 [30]. I did not find an examples folder there.
- Practical infra files, in order of usefulness: Simple-Scene `Infra-*` [1]; Chesapeake Bay Bridge-Tunnel (big, synthetic) [7]; KIT bridge (IFC 4x2) and road (4x3_RC2) [3]; web-ifc `Viadotto Acerno.ifc` and `ifcbridge-model01.ifc` [20]; xBIM `linear-placement-of-signal.ifc` and `geographic-referencing-*` [11]; Community "IFC 4.3 RC Archive" [2].
- Watch out: IFC4x1 / 4x2 / 4x3_RC are different schema identifiers. A tool that supports "IFC 4.3" may mean only `IFC4X3_ADD2` [22]. IFC 4.2 and 4.1 are withdrawn/intermediate [16].

## 10. Large and messy real-world files

Public, free, big IFC files are rare because real projects are confidential. Realistic options:
1. Chesapeake Bay Bridge-Tunnel, ~26 MB, 295k entities (synthetic but large) [7].
2. Schependomlaan, real project with real errors, multiple disciplines, 4D/BCF side data [8].
3. Snowdon Towers exported from Revit yourself [28]. You control the export settings.
4. Concatenate/duplicate: copy a building many times in IfcOpenShell (see section 11) to reach 100 to 500 MB. This is synthetic, but useful for timeout and memory tests.
5. Real files from open competitions or public clients exist (e.g. municipalities), but I did not verify any specific one.

"Messy" signs to look for: exporter-default names (`Basic Wall:Generic - 200mm:123456`), duplicated GUIDs between files, Synchro-changed storey trees [8], huge `IfcBuildingElementProxy` counts, missing units, origin far from 0,0,0 (millions of metres in national CRS), mixed units in one project.

## 11. How to construct edge-case files yourself

Approach: write them with IfcOpenShell (Python), or edit a small clean file by hand. IFC-SPF is plain text (ISO 10303-21), so a text editor works. Method below is general knowledge of the format; confirm the exact API call names against https://docs.ifcopenshell.org (my read of the "Hello World" page returned only navigation) [31]. Always keep the original; test copies only; never open unknown IFC from the internet in a production environment.

| Edge case | How to build | What to check in the MCP server |
|---|---|---|
| Non-Latin names (Cyrillic, CJK, Arabic) | Set `Name` of a wall to e.g. "Стена наружная 380" via the API; IFC-SPF stores Unicode as `\X2\0421\X0\...` escapes. Compare with xBIM `Wrongly1251Encoded.ifc` [10] | Query returns readable text, not `\X2\` codes or mojibake; round-trip write keeps it |
| Quotes, backslash, newline in a string | `'` is doubled `''`; `\\` is a backslash; see `DoubleBackSlashName.ifc`, `NewlinesInStrings.ifc` [10] | No parse crash, exact round trip |
| Empty / huge model | `ifcopenshell.file(schema="IFC4")` with only IfcProject; or loop-create 100,000 walls | Graceful "no elements"; timeouts on listing |
| Missing storeys / elements outside the hierarchy | Create IfcWall without `IfcRelContainedInSpatialStructure` | "Where is it?" queries; orphan reporting |
| Duplicate GlobalIds | Assign same GUID to two elements | Update-by-GUID picks which? Expect error |
| Missing or odd units | Omit `IfcUnitAssignment`, or set millimetres/feet | Units reported correctly; unit-conversion of quantities |
| Far-away origin (georef) | Place at Easting about 155000, Northing about 463000 (Dutch RD, EPSG 28992) with `IfcMapConversion` + `IfcProjectedCRS` [6] | Coordinates reported correctly; no float precision loss |
| Schema mismatch | Ask for an IFC4-only entity (e.g. `IfcTriangulatedFaceSet`) in a 2x3 file; or `IfcWallStandardCase` removed in 4.3 | Clear error, not silent success |
| Corrupt file | Truncate a copy mid-file; remove `ENDSEC;`; bad header `FILE_SCHEMA` (compare `InvalidHeaderFileName.ifc`, `Badly formed Ifc file.ifc` [10]) | Clear error message, no hang |
| Wrong extension / compressed | Rename `.ifc` to `.txt`; make `.ifczip` (ZIP containing .ifc) [16] | Format detection |
| Deep relationship graphs | Nested assemblies (IfcRelAggregates 5+ levels), type with 1000 occurrences | Traversal limits |
| Very long strings / many properties | 5000 property sets on one element | Output truncation |

Validate generated files against the buildingSMART validation service (https://technical.buildingsmart.org/services/validation-service/; page not readable by my fetcher, so check manually). Note: valid-but-weird and invalid files are different test categories. The community repo says most of its files fail validation [2], so "does not validate" is not proof that a file is bad for testing.

## Typical questions people ask about this

All illustrative (no real posts were retrievable this session, see Gaps). Marked (illustrative).

1. Where can I download a small IFC file to test my IFC viewer or API? (illustrative)
2. What happened to buildingSMART/Sample-Test-Files? Why is it now called Certification-datasets? (illustrative; answer: section 2)
3. Which sample IFC has MEP (HVAC, plumbing, electrical)? (illustrative)
4. Is there a free IFC with structural elements (beams, columns, rebar)? (illustrative)
5. Where can I find IFC 4.3 files with roads, bridges, rail? (illustrative)
6. Can I use FZK-Haus in my commercial product's test suite or demo? (illustrative; KIT says "unrestricted use", credit IAI KIT on publication [3])
7. Is Duplex / Clinic really IFC4, or 2x3? (illustrative; the repo lists them under IFC 2x3 [4][5])
8. Where is a large IFC file (100 MB+) for performance testing? (illustrative)
9. Which sample files test georeferencing / IfcMapConversion / EPSG? (illustrative)
10. How do I test an IFC with Russian/Chinese text in names? (illustrative)
11. Where are intentionally broken IFC files for negative tests? (illustrative; xBIM test files [10])
12. Why does my viewer show the Amersfoort model 100 m from the real site? (illustrative; the README explains [6])
13. Do I need Git LFS to clone these sample repos? (illustrative; yes for the community repo [2] and Schependomlaan [8])
14. How do I get an IFC from Revit's sample project rac_basic_sample_project.rvt? (illustrative)
15. Which files pass the buildingSMART validator? (illustrative; community files mostly do not [2])
16. How can I combine Architecture, HVAC and Structural models in one view? (illustrative; Simple-Scene [1], Clinic [5])
17. Does the file use IFC4.3 final or the RC? (illustrative; KIT road is RC2 [3])
18. Are the IfcOpenShell test files licensed for reuse? (illustrative; licence not stated [12])
19. Where are IFC examples for each geometry type (extrusion, B-rep, NURBS, mapped item)? (illustrative; [11][13][14])
20. How do I make a synthetic big IFC with IfcOpenShell? (illustrative; section 11)

MCP-oriented test prompts an LLM can derive from these files (illustrative):
- "Open AC20-FZK-Haus.ifc and list all IfcWall elements with their names." (expect walls from one building)
- "Open the Duplex MEP file and count the ducts/pipes by system name."
- "Which storey contains the most spaces in the Clinic architectural model?"
- "What is the CRS and map conversion of the Amersfoort IFC4 file? Is the origin the same as the project base point?" (answer: not the same [6])
- "Load Infra-Road.ifc and Infra-Bridge.ifc together and tell me which IFC schema each uses."
- "Rename a wall to Стена-01 and save; reopen and check the name."
- "Open Wrongly1251Encoded.ifc and report the parse error clearly instead of crashing."

## Common pitfalls and misconceptions

- **"Sample-Test-Files" is a moving target.** The official repo is now Certification-datasets; most community content is under the `buildingsmart-community` organisation [1][2]. Old tutorial paths break.
- **"Official" vs "community".** Only Certification-datasets is the official buildingSMART set; the community repo says it is "NOT official" and most files fail validation [2].
- **Folder name versions are not the schema string.** "IFC 4.0.2.1 (IFC 4 ADD2 TC1)" corresponds to `FILE_SCHEMA(('IFC4'))` in the file header (the README of that folder gives schema identifier IFC4 [1]). The 4.3 identifier is `IFC4X3_ADD2` [7]. Read the `FILE_SCHEMA` line to know what you really have.
- **Duplex and Clinic are IFC2x3**, even though many people expect modern IFC4 [4][5]. IFC4-only features (e.g. `IfcTriangulatedFaceSet`, `IfcMapConversion`) will not appear there.
- **Clean vs messy.** KIT and Simple-Scene are tidy demos; they will make almost any server look good. Real value comes from Schependomlaan, xBIM broken files, and your own edge cases.
- **Licences differ file by file.** CC BY 4.0 (Certification-datasets, Clinic, Esplanades, S1) needs attribution; Schependomlaan is academic-use permission only [8]; IfcOpenShell files and web-ifc files have no stated licence in what I read [12][20]. Check before copying into a product or a public demo.
- **Synthetic is not as-built.** The Chesapeake model says "not an as-built record" [7].
- **ZIPs.** KIT Smiley West, bridge and road come as ZIP; `.ifczip` is also a legitimate IFC container [3][16]. A test harness must unpack it.
- **Do not download blindly.** This document gives page links, not file URLs. Open the repo page, check the licence, and download in an isolated test folder only when you intend to.
- **Git LFS pointers.** Cloning without Git LFS gives tiny text "pointer" files named `.ifc`; the MCP server will "fail to parse" them [2][8].

## Gaps

- The web-search tool hit its limit in this session, so no web or forum search was possible. I did not find real user questions, native-language (Dutch, German, Estonian, Russian, Chinese) sources, or blog tips. I read repo pages directly instead.
- File sizes and per-file licences: not given on most pages. Only the Chesapeake model had a size (about 26 MB) [7]. All other "small/large" statements are relative.
- buildingSMART technical pages (validation service, schema specification list) and iso.org returned 403 to my fetcher. ISO number rests on Wikipedia [16].
- Open IFC Model Repository (Auckland): page content not retrievable (section 7).
- BIMData and That Open: no dedicated sample catalogue found; Revit export menu text and IfcOpenShell API call names are from general knowledge.
- Duplex licence line, Molio licence, ISO-spec-archive licence, NURBS licence: not read. Also did not open the subfolders of the Schependomlaan "Coordination model" or "As Planned models".
- No suspicious or pirated sites were encountered or linked.

## Sources

[1] https://github.com/buildingSMART/Certification-datasets (also README: https://github.com/buildingSMART/Certification-datasets/blob/main/README.md ; LICENSE: https://github.com/buildingSMART/Certification-datasets/blob/main/LICENSE ; Simple-Scene: https://github.com/buildingSMART/Certification-datasets/tree/main/IFC%204.3.2.0%20(IFC%204.3%20ADD2)/Simple-Scene ; IFC4 folder: https://github.com/buildingSMART/Certification-datasets/tree/main/IFC%204.0.2.1%20(IFC%204%20ADD2%20TC1))
[2] https://github.com/buildingsmart-community/Community-Sample-Test-Files (README: https://github.com/buildingsmart-community/Community-Sample-Test-Files/blob/main/README.md ; dev archive: https://github.com/buildingsmart-community/Community-Sample-Test-Files/tree/main/dev%20archive)
[3] https://www.ifcwiki.org/index.php?title=KIT_IFC_Examples
[4] https://github.com/buildingsmart-community/Community-Sample-Test-Files/tree/main/IFC%202.3.0.1%20(IFC%202x3)/Duplex%20Apartment
[5] https://github.com/buildingsmart-community/Community-Sample-Test-Files/tree/main/IFC%202.3.0.1%20(IFC%202x3)/Medical-Dental%20Clinic (README: .../Medical-Dental%20Clinic/README.md)
[6] https://github.com/buildingsmart-community/Community-Sample-Test-Files/tree/main/IFC%204.0.2.1%20(IFC%204)/Example%20project%20location
[7] https://github.com/buildingsmart-community/Community-Sample-Test-Files/tree/main/IFC%204.3.2.0%20(IFC%204.3)/Chesapeake%20Bay%20Bridge-Tunnel%20IFC%20Model
[8] https://github.com/buildingsmart-community/Community-Sample-Test-Files/tree/main/IFC%202.3.0.1%20(IFC%202x3)/Schependomlaan (README: .../Schependomlaan/README.md ; design models: .../Schependomlaan/Design%20model%20IFC)
[9] https://github.com/buildingsmart-community/Community-Sample-Test-Files/tree/main/IFC%202.3.0.1%20(IFC%202x3)/Esplanades
[10] https://github.com/xBimTeam/XbimEssentials (test files: https://github.com/xBimTeam/XbimEssentials/tree/master/Tests/TestFiles)
[11] https://github.com/xBimTeam/XbimEssentials/tree/master/Tests/TestFiles/IFC4x3_ADD2
[12] https://github.com/IfcOpenShell/files (README: https://github.com/IfcOpenShell/files/blob/master/README.md ; tests: https://github.com/IfcOpenShell/files/tree/master/tests)
[13] https://github.com/buildingsmart-community/Community-Sample-Test-Files/tree/main/IFC%204.0.2.1%20(IFC%204)/ISO%20Spec%20archive
[14] https://github.com/buildingsmart-community/Community-Sample-Test-Files/tree/main/IFC%204.0.2.1%20(IFC%204)/NURBS
[15] https://github.com/buildingSMART/Certification-datasets/blob/main/import-certification.md
[16] https://en.wikipedia.org/wiki/Industry_Foundation_Classes (community encyclopedia, not normative)
[17] https://github.com/buildingsmart-community/Community-Sample-Test-Files/tree/main/IFC%202.3.0.1%20(IFC%202x3)/Molio
[18] https://github.com/buildingsmart-community/Community-Sample-Test-Files/tree/main/IFC%202.3.0.1%20(IFC%202x3)/SDK%20-%20S1
[19] https://www.iai.kit.edu/english/1302.php
[20] https://github.com/ThatOpen/engine_web-ifc/tree/main/tests/ifcfiles/public
[21] https://github.com/IfcOpenShell/IfcOpenShell/tree/v0.8.0/test
[22] https://github.com/IfcOpenShell/IfcOpenShell
[23] https://github.com/ThatOpen/engine_web-ifc
[24] https://github.com/xBimTeam/XbimEssentials/blob/master/LICENCE.md
[25] https://github.com/xBimTeam/XbimEssentials/tree/master/Tests/TestFiles/IFC4x3
[26] https://github.com/bimdata
[27] http://openifcmodel.cs.auckland.ac.nz/
[28] https://help.autodesk.com/view/RVT/2025/ENU/?guid=GUID-61EF2F22-3A1F-4317-B925-1E85F138BE88
[29] https://ifc43-docs.standards.buildingsmart.org/ (redirects to https://standards.buildingsmart.org/IFC/DEV/IFC4_3/HTML/ , not readable)
[30] https://github.com/buildingSMART/IFC4.3.x-development
[31] https://docs.ifcopenshell.org/ifcopenshell-python/hello_world.html
