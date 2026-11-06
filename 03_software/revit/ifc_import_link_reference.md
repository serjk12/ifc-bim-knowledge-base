# Revit IFC import and link: complete reference

## In plain words

Revit can bring an IFC file into a project in two quite different ways. **Open IFC** (File > Open > IFC) builds a *new* Revit project from the IFC and tries to create native-looking Revit elements (walls, floors, in-place families). **Link IFC** (Insert > Link IFC) builds a hidden Revit "cache" file next to the IFC (`<name>.ifc.RVT`) in which every IFC element becomes a **DirectShape** (a frozen piece of geometry with a category and parameters), and then links that cache like an ordinary Revit link. Link is the normal choice for coordination: you see, section, filter and measure the model, but you do not edit it. Open is the choice when you must *edit* or *re-use* the content, but its result is often poor. Most real-world problems are about three things: wrong position or rotation (coordinates), wrong category or clutter (IfcSpace, IfcOpeningElement, assemblies), and slowness or hangs.

Last researched: 2026-11-06

> Research note and limits (read this first). The web-search tool was exhausted in this run, and Autodesk Help (help.autodesk.com), buildingSMART and ISO pages were not fetchable (403 / page not found). Facts below therefore come mainly from the **official Autodesk `revit-ifc` GitHub repository** (README, releases, issues and maintainer comments, read through the GitHub API) and Wikipedia. Everything else is background knowledge and is marked **(unverified)**. Menu names and version numbers can differ between Revit releases; check against the Revit build you test.
>
> **QA pass 2026-11-06.** Release dates and years were re-read from the GitHub releases API: 27.3.0.12 = 2026-08-13, 25.4.3 = 2025-08-11, 24.3.40 = 2026-01-14 (all as already written here, confirmed). The Autodesk help topic for the Revit 2026 IFC section did not contain Link/Open IFC details (it only says Revit "provides fully certified IFC import and export based on buildingSMART IFC data exchange standards"), so the UI paths in section 2 stay "(unverified)". The GitHub issue statuses quoted below (#15, #223, #321, #522, #566, #710, #928, #951, #970, #990, #1019 ...) are as read in the first pass; a re-check through the GitHub API was blocked by rate limiting (HTTP 403), so "open"/"closed" may have changed since. Version fact added: from add-on 26.4.1 (Revit 2026), back-ported to 25.4.40 and 24.3.40, the *exporter* writes IFC4.3 (schema `IFC4X3_ADD2`) - this does not change how Revit's *importer* handles that header (see issue #928 in section 6).

---

## 1. Two paths: Open IFC vs Link IFC

| Aspect | Open IFC (File > Open > IFC) | Link IFC (Insert > Link IFC) |
|---|---|---|
| Result | New `.rvt` project; elements are created on import | Linked model; elements live in a cache file `<ifc name>.ifc.RVT` |
| Element type | Native Revit elements where Revit "understands" the IFC (e.g. a wall with `IfcMaterialLayerSetUsage` became a native Wall), otherwise in-place families / generic models [7] | **DirectShape** elements for everything [3][6] |
| Intent (API term) | `Parametric` (design transfer) or `Reference`; Action `Open` is the default [8][3] | `Intent = Reference` only; Action = `Link` [8] |
| Code base | Older internal Revit (native C++) pipeline, not open source [3][6] | Open-source C# add-in `Revit.IFC.Import` in `Autodesk/revit-ifc`; entry point `ImportIFC` in `Importer.cs`, but "much of the import logic is handled internally by Revit and is not open source" [1][3] |
| Editing | Elements editable (but often in-place/generic and without IFC data) [6] | Not editable; you can select, hide, override graphics, read parameters |
| Typical use | One-off reuse of existing-building geometry, converting to native | Federated coordination, clash checking, reference underlay |
| Rooms/Spaces from IfcSpace | Open can convert IfcSpace to Rooms [9] | Link imports IfcSpace as Generic Model (no Rooms) [9] |

Maintainers have said they plan to reconcile the two so that Link IFC supports both workflows, with no timeline given [6]. As of the latest comments read (2025-2026), the split still exists. A maintainer also said Open IFC was expected to be replaced by technology similar to Link IFC [10].

### What actually happens on Link IFC

1. Revit (the IFC add-in importer) reads the IFC and writes `<path of ifc>.RVT` next to the source file; this is why you see `model.ifc.RVT` in the folder. API view: `Importer` creates this intermediate RVT with DirectShapes; `RevitLinkType.CreateFromIFC` then links it and records the IFC as the external resource [8].
2. On later loads, an up-to-date cache is reused; the API flag `ForceImport = "true"` forces a rebuild, `"false"` reuses an up-to-date cache [8].
3. The `.ifc.RVT` can itself be linked as an ordinary Revit file (a common workaround, see section 6). Some users prefer this because they can clean it first (delete assemblies, tiny parts, add Comments for filtering, use phases) and "don't fully trust reloading a plain IFC link" (community comment) [11].

Known caution: the cache is a derived file. Do not hand-edit and expect the IFC to follow; edits are lost on a forced refresh (unverified in detail; logical from the mechanism above).

### DirectShape and categories

- IFC entity to Revit category mapping on Link/Reference import is a **hardcoded table of 100+ entries** in `IFCCategoryUtil.cs` (`InitEntityTypeToCategoryMaps()`); `PredefinedType` and `ObjectType` can refine the category. A maintainer states there is **no external mapping file** for this compiled table and "no API for configuring the category mapping" [3][12].
- In addition, the user-selectable **Import IFC Class Mapping** table (a text file chosen via File > Open > IFC Options) reclassifies IFC classes to Revit categories - e.g. to put `IfcFlowSegment` into MEP categories. A user feature request describes it as a table chosen per import via "Open > IFC Options" and that it must be reselected when an updated IFC arrives [13]. (The exact file name and column layout of the text file are **unverified**; users typically copy the shipped default file and edit it.)
- Reported behavior (Revit 2024 / add-in 24.x): some classes (`IfcAlarmType`, `IfcElectricTimeControlType`, `IfcOutletType`) went to Generic Model even though the mapping table said otherwise; the reporter noted this was a regression, fixed in Revit 25.1.0.15 (not backported to 2024) [14][15]. Workaround at that time: use the legacy Link IFC version [15].
- User trick: map `IfcSpace` to a category such as Planting via the class mapping file in order to hide it [9].
- Subcategories: current exporters/importers create `IfcOpeningElements` and `IfcSpace.INTERNAL` subcategories under Generic Models; hide them via Revit Links Display Settings > Custom > Model Categories [16].
- Visibility quirk: Revit visibility appears to depend on the *type representation map*; if a door type and a proxy share the same representation map, hiding the Door category hides both (open issue; mainly IFC2x3) [17].

---

## 2. Step-by-step: how to do it (UI paths, Revit 2023-2027)

All UI wording below is from background knowledge unless cited **(unverified)**.

**Link**
1. Insert tab > Link panel > **Link IFC** (some builds show it under Link Revit dropdown).
2. In the file dialog choose `*.ifc` (also filter for `.ifc.RVT`) and set **Positioning** (Auto - Origin to Origin, Auto - Project Base Point to Project Base Point, Auto - Center to Center, Manual variants). Origin-to-origin and project-base-point terms appear in the issue discussions [18].
3. Wait for the cache (`.ifc.RVT`) to be generated; large files can take minutes to hours (see section 4).

**Reload / update**
- Manage tab > Manage Links (or Insert > Manage Links) > **IFC** tab: Reload From..., Reload, Unload, Remove (unverified wording). When the IFC file changes on disk, reloading triggers a regenerate of the cache. API-side the same is `ForceImport` [8].
- A user reported that on a first link a shared parameter file appears briefly and is removed, whereas on update it persists; the Revit 2026 behavior is explained as the AnyCAD importer mapping IFC parameters to stable GUIDs so equal-name shared parameters get the same GUID across linked `.IFC.RVT` models. In Revit 2027 `ParameterUtils.WriteSharedParametersToFile` can write shared parameters from an `.IFC.RVT` into another model, and Transfer Project Standards can also do this [19].

**Open**
1. File > Open > IFC (not Open > Project).
2. Optional: **IFC Options...** to choose the class mapping file and options (auto-join, etc.) [13].
3. Revit creates an untitled project; save as `.rvt`. Choose carefully the project template - the IFC import template affects results (one user reported that changing the import template helped hangs) [20].

---

## 3. Editing limits

- **Linked IFC (DirectShape)**: no parametric edits. You can control Visibility/Graphics per category and subcategory, apply view filters on parameters (imported IFC properties appear as read-only parameters/Pset parameters (unverified exact grouping)), tag, dimension to and snap to the geometry. Moving a link instance moves the whole model.
- **Rooms/Spaces**: IfcSpace becomes Generic Model with subcategory `IfcSpace.INTERNAL`, not a Room; a long-running enhancement (issue #15) asks for promotion to Rooms/Spaces. Autodesk said it is non-trivial and on an extended roadmap because an IfcSpace is a 3D shape while Revit rooms are defined by level, offsets and a point [9]. Workarounds: open the space IFC with Open IFC, or generate room separation lines from space boundaries [9].
- **Imported properties**: in Open IFC the IFC data was reported to be lost in in-place families [6]; a custom parameter on IfcSpace exported from Revit is lost on re-open (issue #35) [21]. There is a request to import exported Comments/Mark back (issue #152) [21].
- **Grids/Levels**: levels and grids may come in as DirectShape/limited objects; Revit 25.4.3 notes "improved linking of some grid lines and axes from slightly invalid IFC4 files" and "templates with constrained levels" [2].
- **Openings**: `IfcOpeningElement` becomes separate Generic Model elements; a request for an import option to skip them is closed as completed (issue #483) [22].

---

## 4. Performance

- Link IFC cost is mostly spent building the DirectShape cache once; later loads use it. IFC with many tiny parts (steel details, bolts, rebar), assemblies and heavy tessellated geometry are the typical slow cases (unverified general experience).
- Reported: IFC links hanging or taking hours even for ~5 MB files in Revit 2024 and 2027, while Open IFC worked; Autodesk tracks it internally (ticket reference REVIT-249806) [20]. Workarounds reported in that thread (community, not official): (a) link the IFC into a **new empty Revit file**, wait 5-20 minutes for the `.ifc.RVT`, then link that `.ifc.RVT` into the project; (b) check antivirus interference (McAfee named); (c) clear Revit temp folders / reinstall; (d) change the IFC import template; (e) Autodesk suggests the **Coordination Model** (needs Navisworks or ACC, extra cost) [20].
- A user asked for a volumetric/lightweight-only link option; not available as of that thread [20].
- Cleanup scripts (Dynamo/IronPython 2.7) that delete tiny objects or `IfcElementAssembly` duplicates exist in community practice, but IronPython 2.7 may not run on Revit 2025+ [16].
- Linking via API: run on the UI thread, no open transaction on the host, close `IFCImportFile.TheFile` and `Importer.TheLog` yourself [8]. A crash on exit has been reported when a plugin referenced IFC (issue #789) [23].

---

## 5. Coordinates: origin to origin vs shared coordinates

Key concept: **IFC has no "shared coordinates" concept in the Autodesk sense**; georeferencing in IFC4+ uses `IfcMapConversion` / `IfcProjectedCRS` (and site placement in IFC2x3 via `IfcSite` lat/long/elevation and property sets). A forum answer states: "Shared coordinates is an Autodesk-specific concept and IFC files don't have shared coordinates" [24].

Observed behavior of Link IFC (from open issues and maintainer comments):

| Topic | What was reported | Source |
|---|---|---|
| Rotation | When linking Origin to Origin, the importer applies the IfcMapConversion X-axis rotation (which IFC defines as grid north) as Revit's true north; users cannot control it; reported present through Revit 2027 and exporter v27.0.1.1 | [25] |
| Project north | Since Revit 2022 (it worked in 2020) a linked IFC's +Y (project north) is aligned to the host's **true north** rather than project north (REVIT-245566 open) | [18] |
| `.ifc.RVT` vs `.IFC` | Linking the IFC directly and linking its `.ifc.RVT` gave different project-north rotations (REVIT-248571 open) | [11] |
| Z / levels | Revit 2025 to 2027: linked geometry too high, levels about doubled in elevation (duplicated Z offset); not seen in 2023/2024; open IFC gives correct coordinates; tracked as REVIT-237045 | [26][27] |
| Fix | Release 27.3.0.12 for Revit 2027 (2026-08-13): "fixed levels from a linked IFC file being placed in the wrong position" | [2] |
| Placement options | Requests to link relative to Site Survey Point and choose among sites; Autodesk epic Revit-165101 "In Progress" | [28] |
| Large coordinates | IFCs with large (survey) coordinates load mispositioned, selection frame stretching to origin (issue #712, closed) | [29] |
| Base point | Release 2021.4.2.0 stopped importing the base point (issue #370, closed) | [29] |

Practical rules of thumb (community practice, partly **unverified**):
- Agree a coordinate convention first: every discipline exports from the same shared origin or each exports to the agreed CRS; Revit exporters offer "Shared Coordinates / Project Base Point / Site Survey Point / Internal Origin" as the export coordinate base.
- Link first with Origin to Origin and verify with a known reference (grid intersection or a survey point); then adjust or "Acquire Coordinates" if working with shared coordinates.
- Four norths exist (project, grid, true, magnetic) but Revit supports only two, causing georeferencing and solar-analysis confusion [25].
- For rotation requirements the issue "Import an IFC using the angle to true north to influence rotation" (issue #321) is still open: Archicad exports, for instance, may be aligned to grid north [30].

---

## 6. Typical issues by source application

(IFC itself is the same standard, but exporters differ; the following were found in the Revit-IFC tracker. Treat Renga/Allplan items as thin.)

### Archicad (Graphisoft)
- **GDL objects** produce families with unclear numeric names and some empty families that cannot be purged (issue #324); reproduced on Revit 2024 (IFC 24.3.20.0), not on Revit 2025 and later (25.4.0.27); not backported - upgrade [31].
- Missing floors on ArchiCAD IFC import fixed for older versions (issue #322) [30].
- **Windows/doors positioned wrongly** in Revit 2025-2027 (not in 2024) with Archicad IFC2x3; 2D symbol/annotation geometry (FootPrint) carried on doors/windows is a separate issue (REVIT-259185 open); 27.3.0.12 notes "doors being misplaced when opening IFC files from other applications" [2][30][32].
- **Spaces**: Archicad zones come in as IfcSpace; an IfcOpenShell-based patch to convert ArchiCAD space exports was mentioned (2026 update runs headlessly) [9].
- Grid-north orientation (issue #321) [30].
- Practical: export with a translator that uses reference geometry for Revit (the "Revit" or coordination-view translators in Archicad; names **unverified**).

### Tekla Structures
- **Assemblies**: Link IFC imports each `IfcElementAssembly` and also its sub-elements, duplicating geometry; Open IFC cannot map sub-element classes to categories. The assembly can be mapped to its own category and deleted [6][33].
- **IFC4 stray points** around geometry in Revit 2024; Revit 2026 appears fixed (issue #943) [34].
- Steel details: very many small parts (bolts, welds) make links slow; delete small parts via script [16].

### Allplan
- No import-specific Allplan issue found; one reverse-direction report: Revit export with multiple levels at the same elevation collapses to one level and breaks the file structure when imported into Allplan (workaround: offset elevation slightly) [35]. Allplan to Revit specifics: **(unverified)**; typical advice is to export IFC4 reference view and test with Link first.

### Renga
- No Renga-specific item found in the tracker (searching returned 0 results) [36]. Renga is a Russian BIM tool (Рэнга, ASCON/Renga Software); general expectations (IFC2x3/IFC4 export, Link rather than Open) are **unverified**.

### Revit-origin IFCs (round trip)
- Re-importing an exported IFC with geographic north can create rotated duplicates of the coordination object and axis raster sharing the same GUID (issue #909) [18].
- Revit-specific export problem classes: joined geometry, Brep faults - not import issues [37].

### Schema-level
- IFC4: older Open IFC did not support IFC4 fully; "Link IFC supports IFC4 for reference viewing" [10]. `IfcTriangulatedFaceSet` could not be imported on Revit 2021 (issue #587) [38]. `IfcIndexedPolyCurve` with `IfcArcIndex` renders distorted (issue #359) [38].
- **IFC4.3**: IFC4X3_ADD2 header causes a Link error in Revit 2024; changing the header to `IFC4X3` works (issue #928, REVIT-245211 open) [39]. Wikipedia lists IFC4.3 Add2 as 2024 and ISO 16739-1:2024 [40]. Which Revit versions fully read IFC4.3 geometry: **(unverified)**.

---

## 7. Converting IFC elements to native Revit families

Revit has no official one-click "convert DirectShape to native families". Options:

| Approach | What you get | Limits |
|---|---|---|
| Open IFC (Parametric intent) | Some native elements (walls, floors, etc.) | Result depends on internal Open IFC logic, which is undocumented; "no published spec" for when native vs generic is chosen [3]; IFC data may be lost [6]; IFC walls with layers may stay BasicWall without layers [3][41] |
| Link IFC then model over | Clean native model drawn using DirectShapes as underlay (snap to geometry) | Manual; most reliable |
| Scripts/add-ins (Dynamo, pyRevit, API) that read DirectShape geometry and create in-place or Generic Model families | Semi-automatic | Geometry only, quality varies, third-party; no specific tool verified in this research |
| Third-party converters / viewers | Not verified | Do not rely on without testing |

Facts from the open-source tracker: the open-source code can split layered `IfcExtrudedAreaSolid` into per-layer solids on the DirectShape path (`CreateGeometryFromMaterialLayerUsage()`) but this does not make native walls [3]. Parameter transfer via the API: the Importer can be driven by `ReferenceIFC(doc, ifcPath)` [8].

---

## 8. Improvements in recent Revit versions (verified items only)

| Version / release | Item | Source |
|---|---|---|
| Revit 2024.1 | A commenter claims improved Link IFC geometry fidelity (not verified by maintainers) | [6] |
| Revit 2025 | Claimed partial metadata parity for Link IFC (unverified) | [6] |
| Revit 25.1.0.15 | Fixed class-mapping-table regression for Link IFC; not backported to 2024 | [15] |
| IFC for Revit 25.4.3 (2025-08-11) | Import of presentation layer assignment for Open IFC; improved linking with templates with constrained levels; improved linking of some grid lines/axes of slightly invalid IFC4 | [2] |
| Revit 2025+ | Hang on Link in some cases reported (2025.4) | [20] |
| Revit 2026 | AnyCAD importer maps IFC parameters to stable GUIDs; fixes Tekla IFC4 stray points; 2025+ fixes ArchiCAD family-naming problem | [19][31][34] |
| Revit 2027 / IFC 27.x | `ParameterUtils.WriteSharedParametersToFile`; 27.3.0.12 (2026-08-13) fixed levels from linked IFC and misplaced doors | [19][2] |
| Revit 2024 (24.3.40, 2026-01-14) | Fix geometry parts in wrong location on link | [2] |
| Repository policy | Current annual version plus the two previous receive fixes; older versions unsupported; 2019+ supported | [1] |

Regressions to know about: windows outside wall face on import in 2025-2027 (#1019), 2D annotation (#1018), Z offset (#990) [30][26].

---

## 9. Tips for testers and users

1. Always state **Revit version AND IFC add-in version** (e.g. 25.1.0.15 + 25.0.0.393); behavior changes between builds [15][1].
2. Test both **Link** and **Open** with the same file and compare; state the **schema** (IFC2x3 vs IFC4 vs IFC4X3) and source application.
3. Check the cache: find `*.ifc.RVT` beside the IFC; delete it to force a rebuild; timestamps matter [8].
4. If an IFC link seems hung, wait for the cache (large files take 5-20 min), then try the two-step approach [20].
5. Use Revit Links Display Settings > Custom to hide `IfcSpace.INTERNAL` and `IfcOpeningElements` [16].
6. For MEP, choose/edit the Import IFC Class Mapping file before linking; reselect it for each reload [13].
7. Verify position with a known reference object after link; log base-point settings [18].
8. When reporting bugs upstream: include the RVT, the IFC, reproduction steps, Revit version, exporter version and export settings [16].
9. Never assume the linked model is identical to source: verify element counts per IFC class between an IFC viewer and Revit (a good MCP test oracle).

---

## Typical questions people ask about this

Real questions (from the Autodesk revit-ifc tracker; paraphrased, no user names):

1. What is the difference between Open IFC and Link IFC, and which gives better results? [6] (issue #223)
2. Why does Link IFC import IfcSpace as Generic Model instead of Rooms/Spaces? [9] (issue #15)
3. Why is my linked IFC rotated to true north instead of project north? [18] (issue #522)
4. Why does linking the IFC and linking its `.ifc.RVT` give different rotations? [11] (issue #710)
5. Why are levels at about twice their elevation / geometry too high after Link IFC in Revit 2025-2027? [26] (issue #990)
6. Can I choose rotation/placement when linking an IFC (survey point)? [28] (issue #16)
7. How do I link multiple IFC files with shared coordinates so they align as in other viewers? [24] (issue #566)
8. Why does Link IFC hang for hours on a small file while Open works? [20] (issue #951)
9. Can I link IFC files through the Revit API and get the link's ElementId? [8][42] (issues #380, PR #423)
10. How can I switch off the generic models created from openings and rooms? [16] (issue #110)
11. How do I configure the IFC import mapping table / IfcTemplate in code? [43] (issue #826, closed, not planned)
12. Why do windows sit outside the wall face after import (Archicad IFC2x3) in 2025-2027? [30] (issue #1019)
13. Why do assemblies appear twice (assembly plus parts) in a Tekla link? [6] (issue #223)
14. Why does an IFC4X3_ADD2 file fail to link in Revit 2024? [39] (issue #928)
15. Why is the shared-parameter file deleted after the first link and are GUIDs the same across links? [19] (issue #970)

Illustrative (invented for test generation):
16. (illustrative) Can I edit a wall from a linked IFC? How do I turn it into a native wall?
17. (illustrative) Where is the `.ifc.RVT` file stored and can I delete it?
18. (illustrative) How do I update the link after the architect sends a new IFC?
19. (illustrative) Why do IFC properties appear as read-only parameters and can I schedule them?
20. (illustrative) Which IFC schema (2x3 or 4) should I request from the Archicad team for Revit?
21. (illustrative) How can I check that the number of IfcWall elements in the IFC equals the number of linked DirectShapes in Walls?
22. (illustrative) Why do the linked model's levels not show as Levels in my project?
23. (illustrative) Can Revit read IFC4.3 infrastructure (IfcRoad, IfcBridge)?

---

## Common pitfalls and misconceptions

- "Link IFC creates native Revit elements." No: DirectShapes; editing is limited [3][6].
- "There is a mapping file to configure the category for each class." Partly: the compiled table (100+ entries) is not user-editable [12]; the user-facing Import IFC Class Mapping text file works through IFC Options and has had regressions [13][14].
- "IFC has shared coordinates." No; it has map conversion / site placement, and Revit's rotation handling is lossy [24][25].
- "Reload will fix a wrong position." If the cause is the importer, e.g. duplicated Z offset, reload does not help (open bug) [26].
- "Opening is better because I can edit." Often poor: in-place families, lost IFC data, unmapped assembly subelements [6].
- "Linking .ifc.RVT is identical to linking .ifc." Reported to differ (rotation) [11].
- "IfcOpeningElement/IfcSpace geometry is a bug." It is intentional geometry; hide via subcategories [16].
- "The cache is optional." It is created automatically; deleting forces a rebuild but costs time.
- Do not assume forum-claimed improvements (2024.1 fidelity, 2025 metadata parity) without testing [6].

---

## Gaps

- Autodesk Help pages for Link IFC / Open IFC / IFC Options, buildingSMART certification pages and ISO catalogue pages could not be fetched (403 / not found); the web search budget was exhausted. Exact UI labels, default mapping file name/format, Revit-by-Revit certification, and detailed positioning options are therefore **unverified**.
- No Renga, Allplan (import into Revit) or Graphisoft official material was found; those sections are thin.
- Third-party converter tools (IFC to native) were not verified; none are recommended here.
- Native-language terms (e.g. Russian "связь IFC", German "IFC verknüpfen") were not verified against localized Revit UIs.

## Sources

[1] https://github.com/Autodesk/revit-ifc (README: scope, Revit 2019+, branch policy, ImportIFC entry point)
[2] https://api.github.com/repos/Autodesk/revit-ifc/releases?per_page=10 (releases 27.3.0.12, 25.4.3, 24.3.40)
[3] https://api.github.com/repos/Autodesk/revit-ifc/issues/778/comments (maintainer: IFCCategoryUtil.cs, native vs DirectShape); issue https://github.com/Autodesk/revit-ifc/issues/778
[4] (not used)
[5] (not used)
[6] https://api.github.com/repos/Autodesk/revit-ifc/issues/223/comments ; https://api.github.com/repos/Autodesk/revit-ifc/issues/223 ; https://github.com/Autodesk/revit-ifc/issues/223
[7] https://api.github.com/repos/Autodesk/revit-ifc/issues/778/comments
[8] https://api.github.com/repos/Autodesk/revit-ifc/issues/380/comments ; https://github.com/Autodesk/revit-ifc/issues/380
[9] https://api.github.com/repos/Autodesk/revit-ifc/issues/15/comments ; https://github.com/Autodesk/revit-ifc/issues/15
[10] https://api.github.com/repos/Autodesk/revit-ifc/issues/414/comments ; https://github.com/Autodesk/revit-ifc/issues/414
[11] https://api.github.com/repos/Autodesk/revit-ifc/issues/710/comments ; https://github.com/Autodesk/revit-ifc/issues/710
[12] https://api.github.com/repos/Autodesk/revit-ifc/issues/826 ; https://github.com/Autodesk/revit-ifc/issues/826
[13] https://api.github.com/repos/Autodesk/revit-ifc/issues/798 ; https://github.com/Autodesk/revit-ifc/issues/798
[14] https://api.github.com/repos/Autodesk/revit-ifc/issues/803 ; https://github.com/Autodesk/revit-ifc/issues/803
[15] https://api.github.com/repos/Autodesk/revit-ifc/issues/803/comments
[16] https://api.github.com/repos/Autodesk/revit-ifc/issues/110/comments ; https://github.com/Autodesk/revit-ifc/issues/110
[17] https://api.github.com/repos/Autodesk/revit-ifc/issues/362 ; https://github.com/Autodesk/revit-ifc/issues/362
[18] https://api.github.com/repos/Autodesk/revit-ifc/issues/522 and /522/comments ; https://github.com/Autodesk/revit-ifc/issues/522 ; https://github.com/Autodesk/revit-ifc/issues/909
[19] https://api.github.com/repos/Autodesk/revit-ifc/issues/970/comments ; https://github.com/Autodesk/revit-ifc/issues/970
[20] https://api.github.com/repos/Autodesk/revit-ifc/issues/951/comments ; https://github.com/Autodesk/revit-ifc/issues/951
[21] https://github.com/Autodesk/revit-ifc/issues/35 ; https://github.com/Autodesk/revit-ifc/issues/152 (titles from search listing)
[22] https://github.com/Autodesk/revit-ifc/issues/483 (title/summary from search listing)
[23] https://github.com/Autodesk/revit-ifc/issues/789
[24] https://api.github.com/repos/Autodesk/revit-ifc/issues/566/comments ; https://github.com/Autodesk/revit-ifc/issues/566
[25] https://api.github.com/repos/Autodesk/revit-ifc/issues/321/comments ; https://github.com/Autodesk/revit-ifc/issues/321
[26] https://api.github.com/repos/Autodesk/revit-ifc/issues/990 ; https://github.com/Autodesk/revit-ifc/issues/990
[27] https://api.github.com/repos/Autodesk/revit-ifc/issues/990/comments
[28] https://api.github.com/repos/Autodesk/revit-ifc/issues/16/comments ; https://github.com/Autodesk/revit-ifc/issues/16 ; https://api.github.com/repos/Autodesk/revit-ifc/issues/97/comments
[29] https://github.com/Autodesk/revit-ifc/issues/712 ; https://github.com/Autodesk/revit-ifc/issues/370 (search listing)
[30] https://github.com/Autodesk/revit-ifc/issues/1019 ; https://github.com/Autodesk/revit-ifc/issues/322 ; https://github.com/Autodesk/revit-ifc/issues/321 (search listing)
[31] https://api.github.com/repos/Autodesk/revit-ifc/issues/324/comments ; https://github.com/Autodesk/revit-ifc/issues/324
[32] https://api.github.com/repos/Autodesk/revit-ifc/issues/1018/comments ; https://github.com/Autodesk/revit-ifc/issues/1018
[33] https://github.com/Autodesk/revit-ifc/issues/223
[34] https://github.com/Autodesk/revit-ifc/issues/943
[35] https://github.com/Autodesk/revit-ifc/issues/285
[36] https://api.github.com/search/issues?q=repo:Autodesk/revit-ifc+Renga (0 results)
[37] https://github.com/Autodesk/revit-ifc/issues/1001 ; https://github.com/Autodesk/revit-ifc/issues/1014
[38] https://github.com/Autodesk/revit-ifc/issues/587 ; https://github.com/Autodesk/revit-ifc/issues/359
[39] https://api.github.com/repos/Autodesk/revit-ifc/issues/928/comments ; https://github.com/Autodesk/revit-ifc/issues/928
[40] https://en.wikipedia.org/wiki/Industry_Foundation_Classes (community encyclopedia)
[41] https://github.com/Autodesk/revit-ifc/issues/778
[42] https://github.com/Autodesk/revit-ifc/pull/423
[43] https://github.com/Autodesk/revit-ifc/issues/826
