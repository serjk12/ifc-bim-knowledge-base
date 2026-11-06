# MEP systems, structural and analytical models, rebar/steel/precast

Topics covered (vocabulary tags): `mep_systems`, `structural_analytical`, `rebar_steel_precast`.
Evidence base: 206 distinct real records (105 + 34 + 69, with a few overlaps) and up to 116 synthetic prompts in `research_raw/wave1`, read in full for this page. Last compiled: 2026-11-06.

## In plain words

A building file has two very different "engineering" layers. The **MEP layer** (ducts, pipes, cables, pumps, air terminals) is a network: every piece has a class (is this a duct segment, a fitting, a valve?), sits in a named **system** ("Supply Air 1"), and is joined to its neighbours through **ports**. The **structural layer** is either a **physical model** (solid beams, columns, slabs, plates, bolts, rebar bars that you can see and count) or an **analytical model** (centre-lines, nodes, supports and loads that a calculation program such as ETABS, Robot, SCAD, RFEM or STAAD understands). These are different branches of the file, and a beam in one is not automatically linked to its twin in the other. See [domain overview](../../01_ifc_basics/08_domains_mep_structural_infra_4d5d_fm.md) sections 2 and 3 for the entity names and [spatial structure and relationships](../../01_ifc_basics/04_spatial_structure_and_relationships.md) for how systems and groups work.

Most real complaints come from exporters and viewers, not from the user. Revit writes pipes with the *system* name as their material, loses the colour on fittings, drops steel connections when one checkbox is on, and writes rebar either as thousands of separate objects or not at all. Tekla and Revit disagree on what an "assembly" is. Analysis programs expect supports, loads and material strength that most architectural-style exports simply do not contain. The Revit side of this is documented in [Revit IFC export reference](../../03_software/revit/ifc_export_reference.md) and [Revit IFC import/link reference](../../03_software/revit/ifc_import_link_reference.md); other authoring tools are in [authoring tools](../../03_software/authoring_tools_ifc.md); the open-source tools mentioned (IfcOpenShell, Bonsai, web-ifc) are in [libraries and toolkits](../../04_open_source/libraries_and_toolkits.md).

For a tester with no BIM background, the one-sentence summary is: **the question sounds simple ("list the ducts without a system") but the honest answer depends on which program wrote the file, which IFC version it is, and which export checkbox was ticked. A good assistant says what it found, says what is absent, and does not invent a value to fill the gap.**

How to read this page: "real" rows are *paraphrases written by the research pass* of questions seen at the linked source (not verbatim quotes). Non-English rows keep the original language and add an English gloss. "Synthetic" prompts are written for testing and are never real quotes.

Coverage caveat (important for test design): the real evidence for MEP and structural IFC is overwhelmingly English (GitHub issue trackers, buildingSMART forum, OSArch, Autodesk forums). Real Russian items exist only for structural exchange (dwg.ru, Telegram-linked threads); Japanese, Chinese, Spanish, Dutch and Norwegian each have a handful. German, French, Portuguese, Korean and Italian appear only as synthetic prompts. This is a gap in the research, not proof that those users do not ask.

---

## Problem map

Roughly ranked by number of real records (a record is one observed question; several records can point at the same thread, so the "threads" number is the more honest signal).

| # | Problem | How users describe it | Frequency signal | Root cause | Typical fix |
|---|---|---|---|---|---|
| 1 | Structural analysis model does not travel between programs | "export to ETABS/SCAD/Robot via IFC gives error / loses elements", "nothing shows in Solibri", "how to get nodes and bars, not solids" | ~28 records, ~25 threads; en, ru, es, zh, ja | Physical model and analytical model are different IFC branches; Revit's default exporter does not write the analytical branch; receiving programs expect supports, loads, density, units | Use a vendor/direct link or an analysis-capable exporter; check what the IFC actually contains before sending; fill missing material data |
| 2 | MEP elements grey or with wrong material | "why are my pipes grey in IFC", "pipe material is the system name, not PVC", "fittings lose colour" | ~20 records, ~12 threads; en only | Colour and material come from the Material, not from view filters; Revit exports the *system* material for pipes/ducts; fittings use a different code path | Set colour on the material, use by-category plus system override, use IFC2x3 CV2.0 or IFC4 Reference View; accept that the exporter has open tickets |
| 3 | Wrong IFC class or PredefinedType for MEP parts | "security devices come out as proxies", "ducts are generic flow segments", "best class for a reducing coupling", "parameter I mapped does not appear" | ~20 records, ~13 threads; en | Category mapping/`IfcExportAs` not set; IFC2x3 has only generic `IfcFlowSegment`; no obvious class for some parts | Set class per family/type with Export-to-IFC-As; use IFC4; TRANSITION when the nominal size changes; verify the PredefinedType belongs to the class enum |
| 4 | Steel framing, connections, bolts disappear or move in Revit IFC | "beams and columns vanished after exporter update", "hollow sections displaced", "welds at origin", "connections have no parameters" | ~20 records, ~16 threads; en | "Include Steel Elements" option and specific exporter builds (25.4.3.0 etc.) have bugs; some elements need the Advance Steel path | Untick the option as workaround or revert to 25.4.0.27 / update to 25.4.40; check Autodesk ticket numbers; count beams/columns per level to detect loss |
| 5 | Rebar geometry invisible or wrong in a viewer/converter | "rebar not rendered", "swept disk fails in IfcConvert", "bars in wrong place after upgrade" | ~12 records, ~12 threads; en | Rebar is `IfcSweptDiskSolid` along a curve; kernels and viewers differ (Manifold kernel unsupported, composite curves, arcs) | Use another geometry kernel (OpenCascade), update the viewer, check the file in a second viewer |
| 6 | Rebar export: sets, containers, rounding, size | "rebar sets split into thousands of entities", "API-created rebar container not exported", "length 3422 instead of 3420" | ~10 records, ~7 threads; en | Each bar can become its own entity; API containers and rounding are not carried by the exporter (internal tickets open) | Revit 2025+ Advanced-tab option for uniform rebar sets; merge/filter after export; accept rounding drift |
| 7 | Rebar and steel quantities (weight, length, per host) | "total rebar kg per column", "NetWeight not exported", "no standard Qto" | ~16 records, ~14 threads; en, no | Rebar may not be modelled at all; no single standard quantity set is used in practice; host relation is unclear (assembly vs aggregate vs nest) | State the source of every number (Qto, pset, geometry, density x volume); aggregate per host; flag missing |
| 8 | Large MEP/rebar/Tekla files crash or hang | "400 MB MEP file aborts with memory error", "insulation doubles export time", "fabrication parts create hundreds of types" | ~16 records, ~12 threads; en | Detailed insulation geometry, duplicate types per fitting, web viewers with a 4 GB WASM limit, viewers choking on swept disks | Lower LOD, drop ports/insulation on a *copy*, filter classes before loading, newer exporter |
| 9 | MEP ports and connectivity | "cannot switch ports off", "ports have no properties", "ports lost on library import", "which way does flow point" | ~12 records, ~12 threads; en | Ports are added by the exporter after the fact; IFC4 uses `IfcRelNests`, IFC2x3 uses `IfcRelConnectsPortToElement`; tools handle only one | Check the IFC text for `IfcRelConnectsPorts` before blaming the exporter; align flow-direction convention |
| 10 | MEP systems missing, empty or without properties | "ventilation systems vanished after export", "cannot put psets on IfcSystem", "cannot override system membership" | ~12 records, ~10 threads; en, nl | Systems are groups (`IfcRelAssignsToGroup`); exporter drops them with some options, IFC4 vs 2x3 differ; membership cannot be overridden | Do not export "only visible" if you need circuits/systems; use custom property set mapping; report orphans |
| 11 | Tekla/precast assemblies double up or lose rebar in Revit | "everything doubled, assembly and parts", "rebar and connections not transferred from Tekla", "BIMsight shows rebar wrong" | ~9 records, ~8 threads; en, ru | Link IFC imports the assembly *and* its parts; Revit cannot natively import Tekla rebar | Map assembly class to a deletable category; use a Tekla export view (CV2.0 etc.) and set base point; rebuild rebar natively if needed |
| 12 | Units of MEP flow | "L/s exported as ft3/s", "I need m3/h but IFC says m3/s" | ~5 records, ~3 threads; en | Revit stores internal units; one flow data type; unit definition bug in some versions | Read the unit assignment; convert and say so; change display unit as workaround |
| 13 | Penetrations: where MEP crosses walls, slabs, beams | "which pipes pass through fire walls with no hole", "sleeve size per crossing" | ~6 real records, ~4 threads, plus 8 synthetic in 7 languages | No standard "penetration" object; openings are separate elements; clearance rules are project-specific | Scan crossings read-only, mark candidates for human review, never default a clearance |
| 14 | IFC to native Revit MEP elements | "I tried an add-in to turn IFC pipes into Revit pipes and failed" | ~6 records, ~3 threads; en, ja | Link IFC gives non-editable DirectShapes; diameters/system types cannot be set from geometry alone | Model over the linked IFC; do narrow tasks (quantities) instead of full conversion |

---

## Problems in depth

### 1. The analytical (calculation) model does not travel

**What users say**
- ru: «не все элементы передаются из Ревита 2016 в Старк ЕС, IFC пробовала — результат плохой» (EN: elements are missing in STARK ES, I tried IFC and the result is poor). [forum.dwg.ru](https://forum.dwg.ru/showthread.php?t=133669)
- ru: «как лучше передать конструктив из Ревита в СКАД, есть ли прямая связь, можно ли DWG/DXF» (EN: best way to get the structure from Revit into SCAD, is there a direct link, can I use DWG/DXF). [forum.dwg.ru](https://forum.dwg.ru/showthread.php?t=142967)
- es: «Problema al importar modelo de Revit en plantilla de estructuras... ETABS muestra mensaje de error» (EN: ETABS shows an error when importing the Revit IFC). [bSI forum](https://forums.buildingsmart.org/t/como-poder-exportar-un-modelo-3d-estructural-realizado-en-revit-a-etabs-por-medio-del-formato-ifc/2985)
- en: "ETABS model exported with Structural Analysis View shows nothing in Solibri or BIMsight". [bSI forum](https://forums.buildingsmart.org/t/ifc-structural-analysis-view/1267)
- zh: NTU master thesis finds that IFC transfer from Revit to Robot/ETABS/SAP2000 loses or alters data; native files and API links work better. [NTU repository](https://tdr.lib.ntu.edu.tw/handle/123456789/90111)

**Why it happens.** The analytical model is a separate set of entities (`IfcStructuralAnalysisModel`, curve members, point connections, load groups). Per forum reports collected in the [domain overview](../../01_ifc_basics/08_domains_mep_structural_infra_4d5d_fm.md), the default Revit exporter does not write it. Curve members have no solid, so general viewers show nothing or only corner points. Bonsai hides structural members by default (a "no longer display" bug turned out to be this filter, [IfcOpenShell #5788](https://github.com/IfcOpenShell/IfcOpenShell/issues/5788)). Even when present, an RFEM round trip in Bonsai lacked density, self-weight coefficients, units for inertia/modulus, yield strength, and had Z-down axes that flipped load directions ([OSArch](https://community.osarch.org/discussion/comment/30616#Comment_30616)). There is no dedicated rigid-link entity ([bSI forum](https://forums.buildingsmart.org/t/rigid-link-representation-in-structural-analysis-model/1364)); per-DOF releases go through `AppliedCondition` on `IfcRelConnectsStructuralMember` ([bSI forum](https://forums.buildingsmart.org/t/user-defined-point-connection-between-structural-elements-structural-analysis-domain/2633)). Tolerance rounding can disconnect nodes after import into ETABS ([BHoM #548](https://github.com/BHoM/ETABS_Toolkit/issues/548)). A real AxisVM export failed to load because it used an `IfcTopologyRepresentation` of "Undefined" and had ~18k validation errors ([IfcOpenShell #6459](https://github.com/IfcOpenShell/IfcOpenShell/issues/6459)).

**What fixes it.** Use a vendor or direct link where one exists (SCAD, Robot, STARK ES integrations are mentioned in the ru threads); otherwise export from a tool that writes the analytical branch and check the result file for members, supports, loads, materials before sending. Place the model near 0,0,0 to avoid offsets (ru thread). Engineer remains responsible for loads and reinforcement.

**What a good assistant should do.** First count what is in the file (analysis model present? curve members? point connections? supports? load cases?). If the file only has solid beams and columns, say so plainly and explain the physical/analytical difference instead of pretending to "convert". List what is missing before the solver: density, yield strength, units, supports.
**Clarifying questions:** Which program wrote this file and which will read it? Is it IFC2x3 or IFC4? Do you want the physical model (solids) or the calculation scheme (bars and nodes)? Which units does the solver expect?

### 2. Grey pipes, system names as material, fittings without colour

**What users say**
- en: "whats the root cause of grey MEP-components in IFC — some MEP IFCs show colours and others grey; is it an MVD issue?" [revit-ifc #579](https://github.com/Autodesk/revit-ifc/issues/579)
- en: "Pipes / ducts / etc export using system material not actual material... some systems mix PVC and HDPE". [revit-ifc #577](https://github.com/Autodesk/revit-ifc/issues/577)
- en: "How can I control the IFC pipes colors (Revit to ArchiCAD)": hot water red/cold blue/sewage green become beige/blue/blue. [bSI forum](https://forums.buildingsmart.org/t/how-can-i-control-the-ifc-pipes-colors-revit-to-archicad/2729)
- en: "Losing duct fitting material when exported to IFC". [Autodesk forum](https://forums.autodesk.com/t5/revit-mep-forum/losing-duct-fitting-material-when-exported-to-ifc-files/td-p/8736337)
- en: "Pipe/Duct Fittings material bug"; "Fittings system override material not exported". [#373](https://github.com/Autodesk/revit-ifc/issues/373), [#112](https://github.com/Autodesk/revit-ifc/issues/112)

**Why it happens.** Colour comes from the Material (or style) of the element. View filters and graphic overrides are view-specific and are not exported ([#579](https://github.com/Autodesk/revit-ifc/issues/579)). For pipes and ducts the exporter uses the *system* material, by design, because users once demanded system colours; a proposal is to use the system material as a style and the real material as `IfcMaterial` ([#577](https://github.com/Autodesk/revit-ifc/issues/577), internal ticket REVIT-236144, open). Fittings go through a different path and keep losing material (long-running issues #112, #373, #915).

**What fixes it.** Put the colour on the material itself, set pipes to by-category with system override, update the exporter, use IFC2x3 CV2.0 or IFC4 Reference View. For duct fittings the forum workaround is the `IfcSingleMaterialOverride` parameter naming a material.

**What a good assistant should do.** Inspect `IfcRelAssociatesMaterial` on pipe/duct segments *and* fittings, compare material names with system names (HOT WATER, SEWER...), report counts of "material = system name", and say where a real material might still live (a pset, the type name) without claiming it. Never say the model "has no colour" without checking `IfcStyledItem`/material styles.
**Clarifying questions:** Do you need the real material for take-off, or the colour for viewing? Which exporter version and MVD? Do fittings and straight segments behave differently?

### 3. Wrong IFC class, proxies, PredefinedType and unmapped parameters

**What users say**
- en: "Security devices export as proxies while electrical equipment exports correctly." [Autodesk forum](https://forums.autodesk.com/t5/revit-mep-forum/ifc-export-issue/m-p/12250648)
- en: "Ducts and pipes show as generic types after export." Answer: in 2x3 only `IfcFlowSegment`; `IfcDuctSegment`/`IfcPipeSegment` exist from IFC4. [Autodesk forum](https://forums.autodesk.com/t5/revit-mep-forum/ifc-export-ducts-and-pipes/td-p/12370919)
- en: "Best IFC classification for a reducing coupling: CONNECTOR for couplings, but two different ports suggest TRANSITION". [bSI forum](https://forums.buildingsmart.org/t/best-ifc-classification-for-a-reducing-coupling/5963)
- en: "IFC class for earthing rod — no obvious class for grounding rod". [bSI forum](https://forums.buildingsmart.org/t/ifc-class-for-earthing-rod/5632)
- en: "I created a shared parameter named like the duct Pset Material attribute but it does not appear in the exported IFC". [bSI forum](https://forums.buildingsmart.org/t/ifc-mapping-in-revit-mep/4591)
- en: `IfcExportAs=IfcFlowMeterType` + `IfcExportType=WATERMETER` gives the right class but `NOTDEFINED`. [#525](https://github.com/Autodesk/revit-ifc/issues/525)

**Why it happens.** The exporter decides the class from the category mapping first, then per-element override parameters (instance beats type). IFC2x3 simply has fewer MEP classes. Pset mapping for dimension-like values needs the right parameter source (rectangular width/height vs round diameter cannot be mapped to the same property conditionally, [#303](https://github.com/Autodesk/revit-ifc/issues/303)). Consultants also send `IfcFlowSegment` where the receiver wants duct/pipe classes ([#798](https://github.com/Autodesk/revit-ifc/issues/798)).

**What fixes it.** Set the class and PredefinedType per family/type, export IFC4, check that the PredefinedType belongs to the class enum. Reducers: TRANSITION when the nominal diameter changes (forum answer; MagiCAD does the same). Earthing rod: `IfcCableSegment` or protective device, or USERDEFINED; `IfcEarthingElement` was planned for 4.4.

**What a good assistant should do.** Group MEP elements by class and PredefinedType, flag `IfcBuildingElementProxy` and generic `IfcFlowSegment`, and propose a class **as a suggestion with reasons**. For write requests, show the list and count first, then ask for confirmation, then change class on a copy and report. Because name-based reclassification is a guess, say so.
**Clarifying questions:** IFC2x3 or IFC4? Reclassify by name, by category, or by size? Should GlobalIds be preserved? Is the target a receiver with a specific mapping table?

### 4. Steel beams, columns, connections, bolts vanish or move

**What users say**
- en: "PR: Steel elements / elements with structural connections gone from IFC using version 2025.4.3." [#890](https://github.com/Autodesk/revit-ifc/issues/890)
- en: "Revit 2026 IFC structural export: predefined types not exported (ifcbeam and ifc column)" — real cause was the "Include steel elements" option. [#952](https://github.com/Autodesk/revit-ifc/issues/952)
- en: "Closed square profiles (hollow sections) displaced in IFC2x3 and corrupt in IFC4." [#1010](https://github.com/Autodesk/revit-ifc/issues/1010)
- en: "IfcFastener / Revit Weld exports to 0.0" (welds at origin). [#901](https://github.com/Autodesk/revit-ifc/issues/901)
- en: "Structural connections IFC parameters" — support said not possible. [Autodesk forum](https://forums.autodesk.com/t5/revit-structure-forum/structural-connections-ifc-parameters/td-p/13252740)
- en: "Beam Openings get displaced in IFC4 (along Z-Axis)" — fixed Revit 2026, no backport. [#708](https://github.com/Autodesk/revit-ifc/issues/708)

**Why it happens.** The "Include Steel Elements" option and particular exporter builds are the usual suspects: with the option on, beams/columns connected to structural connections are excluded in 25.4.3.0 (fixed in 25.4.40; revert to 25.4.0.27) and in a Revit 2026 report unticking the box brought them back (REVIT-247661). Older open-source exporters dropped steel connection support altogether (uninstall to keep it, [#282](https://github.com/Autodesk/revit-ifc/issues/282)). Several items have internal Autodesk ticket numbers and are fixed only in newer Revit releases.

**What fixes it.** Know the exporter build number, toggle the option, count beams/columns/members per level in the IFC and compare with the Revit schedule.

**What a good assistant should do.** Count `IfcBeam`, `IfcColumn`, `IfcMember`, `IfcPlate`, `IfcMechanicalFastener`, `IfcFastener` per storey and report zero explicitly. Do not conclude "the model has no bolts" if the file has no `IfcMechanicalFastener`; say that the exporter option or build may have dropped them. Check hollow sections for XY displacement by comparing bounding boxes with the Revit values if provided.
**Clarifying questions:** Revit version and exporter build (e.g. 25.4.40)? Is "Include steel elements" ticked? Is the IFC2x3 or IFC4 view used? Do you have the Revit schedule to compare against?

### 5. Rebar sets become thousands of objects, or are not exported

**What users say**
- en: "Rebar export - Export rebar sets as one instance... 200MB->70MB after SimpleBIM merge". [#76](https://github.com/Autodesk/revit-ifc/issues/76)
- en: "using revit api to create rebarcontainer does not export to ifc" (exports without bars, item length zero). [#335](https://github.com/Autodesk/revit-ifc/issues/335)
- en: "Export Rebars - Rounded values missing (3422 instead of 3420)". [#14](https://github.com/Autodesk/revit-ifc/issues/14)
- en: "Support for Export Current View Colors" — rebar coloured by diameter. [#731](https://github.com/Autodesk/revit-ifc/issues/731)
- ko (synthetic only): "레빗에서 IFC 내보냈는데 철근이 안 보여요".

**Why it happens.** Each bar in a uniform set can become its own IFC entity; the thread answer for Revit 2025 points at the Advanced-tab option for exporting uniform rebar sets as separate entities (the [export reference](../../03_software/revit/ifc_export_reference.md) lists it as default off, so read the real setting rather than assume). API-created containers and rounding are not carried (REVIT-248997, REVIT-93920). View-based colour is not exportable by design (Autodesk: IFC is for classified geometry; workaround DirectShapes with materials).

**What fixes it.** Adjust the option, merge or filter after export, accept that rounding values are not preserved, ask the detailing tool for its own report.

**What a good assistant should do.** Count `IfcReinforcingBar` and group by host/IfcGroup/Pset; say whether sets are per-bar or per-instance and estimate the size effect; if there are zero rebar entities, check for proxies named like rebar before saying "no rebar".
**Clarifying questions:** Which tool created the rebar (Revit, Tekla, Allplan)? Do you need bars individually (bar marks) or only totals? Is file size or accuracy the priority?

### 6. Rebar geometry does not render or converts wrongly

**What users say**
- en: "Missing IfcReinforcingBar geometry... same file opens in BimVision, DDScad, Solibri" — fixed in a newer IfcOpenShell build. [#4945](https://github.com/IfcOpenShell/IfcOpenShell/issues/4945)
- en: "IfcConvert 0.9.0 Manifold: crash... unsupported swept-disk solid; OpenCascade is fine". [#9762](https://github.com/IfcOpenShell/IfcOpenShell/issues/9762)
- en: "Not able to render IFCs of precast concrete structures with rebars exported from Tekla" (web viewer). [web-ifc #445](https://github.com/ThatOpen/engine_web-ifc/issues/445)
- en: "V6 regression on geometry of a SweptDiskSolid rebar element" (composite curves). [xBIM #568](https://github.com/xBimTeam/XbimGeometry/issues/568)
- en: "Version 1.4.21 has a bug regarding the position of some objects, namely IFCREINFORCINGBAR". [web-ifc #773](https://github.com/ThatOpen/engine_web-ifc/issues/773)

**Why it happens.** Rebar is a circle swept along a centre-line (`IfcSweptDiskSolid`). Geometry engines handle curves, arcs and composite curves differently; the Manifold kernel only supports extrusions, shells and solids; the multithreaded CGAL-OpenCascade path dropped swept disks on pipe bends too ([#9511](https://github.com/IfcOpenShell/IfcOpenShell/issues/9511), a MEP case with the same geometry type).

**What a good assistant should do.** When a viewer shows nothing, first confirm the entities exist (count `IfcReinforcingBar`, list representation types), then say "this may be a viewer/kernel limit, try a second viewer or another kernel", rather than "the file is broken".
**Clarifying questions:** Which viewer or converter shows the problem? Does another viewer (Solibri, BIMvision) show it? Which software version?

### 7. Rebar and steel quantities

**What users say**
- en: "wants rebar weight per concrete volume as custom Qto for cost schedule; rebar not modeled". [OSArch](https://community.osarch.org/discussion/2578/how-to-create-a-custom-qto-calculation)
- en: "calculate Gross/NetWeight from Pset_ProfileMechanical.MassPerLength times length". [#6344](https://github.com/IfcOpenShell/IfcOpenShell/issues/6344)
- en: "Qto_BeamBaseQuantities.NetWeight[Type]: beam NetWeight not exported as IfcQuantityWeight" (fixed only in Revit 2026+). [#764](https://github.com/Autodesk/revit-ifc/issues/764)
- en: "Free IFC Concrete BOQ, looking for test files and honest feedback" (three-tier quantity source). [OSArch](https://community.osarch.org/discussion/3418/free-ifc-concrete-boq-looking-for-test-files-and-honest-feedback)
- en: "IfcFooting Quantity calculation issues" (1 of 10 quantities right under one engine). [#6305](https://github.com/IfcOpenShell/IfcOpenShell/issues/6305)
- no: «hvordan går vi fra armeringsmodell til bestilling og produksjon med åpne standarder?» (EN: how do we go from a rebar model to ordering and production with open standards). [buildingSMART Norge](https://www.buildingsmart.no/standarder/publikasjoner-og-veiledninger.html)

**Why it happens.** Quantities can come from four places: a `Qto_*` set, a custom pset, geometry, or density x volume. Exporters write them only if enabled; engines disagree; hosts are linked by assembly, aggregation or nesting without agreement ([IFC4.x-development #205](https://github.com/buildingSMART/IFC4.x-development/issues/205)). Lap lengths belong to individual bars, not the assembly ([bSI forum](https://forums.buildingsmart.org/t/reinforcingbar-lap-lengths/6430)).

**What a good assistant should do.** Always state *which* source each number came from and the density used (e.g. 7850 kg/m3 for steel as a stated assumption), flag missing diameters/lengths, and refuse to invent weights for bars that have no length. Aggregate per host element only if the host relation is actually in the file.
**Clarifying questions:** Per bar mark, per diameter, per host or total? Should the weight use the Qto if present or recompute? Which density or unit weight table (the project's, or a standard value)?

### 8. Big MEP files: crashes, insulation, duplicate types

**What users say**
- en: "GetFlatMesh/GetLine crashes with WASM memory errors on large Revit-exported IFC4 MEP models" (400MB+). [web-ifc #1999](https://github.com/ThatOpen/engine_web-ifc/issues/1999)
- en: "industrial plant export 6h16 and 720 MB with insulation vs 2h43 without." [#892](https://github.com/Autodesk/revit-ifc/issues/892)
- en: "Fabrication ductwork generates hundreds of duplicate IfcElementTypes". [#510](https://github.com/Autodesk/revit-ifc/issues/510)
- en: "ExtractElements is extremely slow for a 9,289-element selection in an IFC2X3 MEP model". [IfcOpenShell #9247](https://github.com/IfcOpenShell/IfcOpenShell/issues/9247)
- en: "ENH: Option to NOT export IfcDistributionPort". [#630](https://github.com/Autodesk/revit-ifc/issues/630)

**Why it happens.** Insulation is geometry that doubles the work (and is merged into the pipe in IFC4, [#416](https://github.com/Autodesk/revit-ifc/issues/416)); ports are extra entities; web viewers hit a ~4 GB memory ceiling.

**What a good assistant should do.** Offer to make a *lighter copy* (filter by class, drop insulation coverings or ports), always on a copy, always telling the user what disappears: removing ports removes the connectivity needed to trace systems. Report size before/after. Warn before loading a 700 MB file into a whole-file operation.
**Clarifying questions:** What is the file for (viewing, coordination, take-off)? Can I remove ports/insulation, or must connectivity stay? Where does it fail (export, load, query)?

### 9. Ports and connectivity

**What users say**
- en: "IfcDistributionPort: Properties — port property sets from the IFC spec not available". [#188](https://github.com/Autodesk/revit-ifc/issues/188)
- en: "IfcPipeFittingType does not import ports from a library". [OSArch](https://community.osarch.org/discussion/2885/ifcpipefittingtype-does-not-import-ports-from-a-library)
- en: "Request to preserve MEP connectivity relationships during native IFC to Fragments conversion" (network selection in a coordination app). [ThatOpen #27](https://github.com/ThatOpen/platform_services/issues/27)
- en: "What is the logic of requiring the axis of an IfcDistributionPort to point in the flow direction?" [IFC4.x-development #147](https://github.com/buildingSMART/IFC4.x-development/issues/147)
- en: "Heater-to-port relation changed in IFC4; how does Revit do dynamic port connection". [#162](https://github.com/Autodesk/revit-ifc/issues/162)

**Why it happens.** In IFC4 fixed ports hang on the element with `IfcRelNests`; in IFC2x3 `IfcRelConnectsPortToElement`. Revit's IFC4 exporter writes the nesting form. A reader that only knows one form sees "no ports". Real data point: a Revit 2025 IFC4 export had ~1,474 ports and ~691 `IfcRelConnectsPorts`; connectivity was lost later in a converter (see the [domain overview](../../01_ifc_basics/08_domains_mep_structural_infra_4d5d_fm.md) section 2.2).

**What a good assistant should do.** Walk ports through `IsNestedBy`/`Nests` and `ConnectedTo`/`ConnectedFrom`; list open ends with parent element, system, level and flow direction; flag SOURCE-SOURCE or SINK-SINK connections. If the user's software shows no connections, check the IFC text before blaming the exporter.
**Clarifying questions:** Which IFC version? Do you want open ends only, or a trace from one element downstream? Which end is the source?

### 10. Systems missing, empty or without properties

**What users say**
- en: "Revit cannot export properties of an IfcSystem" (first by-design, later revised via custom property set mapping). [#523](https://github.com/Autodesk/revit-ifc/issues/523)
- en: "INQ: Override IfcDistributionSystem of elements" (REVIT-244685, open). [#900](https://github.com/Autodesk/revit-ifc/issues/900)
- en: "Issue with IfcSystem export when using 'Export only elements visible in view'" (circuits not written). [#959](https://github.com/Autodesk/revit-ifc/issues/959)
- en: "IfcSystem information related to pipes - IFC4 from Revit" (present in 2x3, missing in IFC4). [bSI forum](https://forums.buildingsmart.org/t/ifcsystem-information-related-to-pipes-ifc4-from-revit/3178)
- nl: «Waarom geen verwijzing naar Systems (IfcDistributionSystem)? NL/SfB-codes sluiten niet geheel aan op de praktijk» (EN: why no reference to IfcDistributionSystem; NL-SfB does not fully match practice). [digiGO imwo #52](https://github.com/nl-digigo/imwo/issues/52)

**Why it happens.** A system is a group; members are linked with `IfcRelAssignsToGroup`. The exporter may drop systems or circuits depending on options and view, and the system *name* often carries the discipline code (forum: put the system code in `IfcSystem` Name, colouring is a viewer feature).

**What a good assistant should do.** List every `IfcSystem`/`IfcDistributionSystem` with member counts, flag empty systems, list distribution elements without any system, and explain that if the file has *no* system entities at all, the likely cause is export settings, not the model. Offer to group by system for lengths/diameters only when membership exists.
**Clarifying questions:** Which systems do you expect (supply air, domestic cold water...)? Was the export limited to a view? Which classification (NL-SfB, Uniclass) should be checked too?

### 11. Tekla and precast: doubling, lost rebar, wrong display

**What users say**
- en: "IFC Import - Link Vs Open: Link IFC imports assemblies plus parts (duplicate geometry)". [#223](https://github.com/Autodesk/revit-ifc/issues/223)
- ru: «Почему не меняется материал и тонирование колонн в Revit 2020, экспортированных из Tekla? арматура и узлы не переносятся» (EN: why can't I change material/shading of columns exported from Tekla; rebar and connections are not carried). [dwg.ru](https://forum.dwg.ru/showthread.php?t=155997)
- ru: «арматура неправильно отображается в BIMsight после экспорта, как передать свойства» (EN: rebar displays wrongly in BIMsight after export, how to pass properties). [dwg.ru](https://forum.dwg.ru/showthread.php?t=150272&page=2)
- ru: «что выбрать конструктору КЖ: Revit, Tekla или Allplan» (EN: which to choose for reinforced-concrete design). [dwg.ru](https://dwg.ru/b/utrfm/263)
- en: "Export a Tekla Structures model to an IFC file: brace exports as IfcMember; how do I choose export type and shrink huge files?" [BIM Corner](https://bimcorner.com/export-a-tekla-structures-model-to-an-ifc-file/)

**Why it happens.** A cast unit is an `IfcElementAssembly` with parts; Revit's Link IFC imports both. Revit cannot natively import Tekla rebar. Tekla's export view (Coordination View 2.0, Surface Geometry, Steel Fabrication View), base point and ZIP packaging change the result; in the ru thread the reinforcement option yielded CV2.0 and an `IfcPropertySetConfigurations_CV2` config exported the properties.

**What a good assistant should do.** List `IfcElementAssembly` with their children (via `IfcRelAggregates`) and warn about duplication when linked in Revit; suggest mapping the assembly class to a deletable category; do not promise native rebar in Revit.
**Clarifying questions:** Link IFC or Open IFC? Do you need the parts, or only the assemblies? Which Tekla export view was used?

### 12. Units of MEP flow

**What users say**
- en: "Flow Units export to Ifc not correct: flow parameter should be L/s but IFC has ft3/s". [#444](https://github.com/Autodesk/revit-ifc/issues/444)
- en: "IFC VolumetricFlowRate is m3/s; user wants duct flow in m3/h and pipe flow in l/s though both use the same parameter name". [bSI forum](https://forums.buildingsmart.org/t/supported-data-type-volumetricflowrate-m-h/4189)
- en: "Airflow properties not scaled from revit internal units" (workaround: change display unit). [#237](https://github.com/Autodesk/revit-ifc/issues/237)

**What a good assistant should do.** Read the project `IfcUnitAssignment` and the property's own unit; show raw value, unit and converted value; say "this looks like ft3/s, I'm converting" rather than silently correcting. Synthetic fr prompt "j'ai l'impression que c'est en ft3/s au lieu de L/s" tests exactly this.
**Clarifying questions:** Do you want values converted for display, or the file corrected? What unit does the receiving calculation expect?

### 13. Penetrations: MEP through walls, slabs and beams

**What users say**
- zh: «機電管線穿過牆、樓板或樑時要逐筆確認穿透位置與開孔大小；希望AI能指定MEP/結構在主模型或連結模型、預留量、樓層與品類，回傳候選清單» (EN: MEP crossing walls/floors/beams must be checked one by one; want an AI tool returning candidate list with reserve amount, level, category). [REVIT_MCP_study #99](https://github.com/shuotao/REVIT_MCP_study/issues/99)
- en: "Parametric Openings for MEP Penetrations (Walls, Slabs, Roofs)... associative update when MEP moves, clearance offsets, batch from clash scan". [IfcOpenShell #8037](https://github.com/IfcOpenShell/IfcOpenShell/issues/8037)
- en: "Headless Parametric Opening Creation for Walls and Slabs" (reusable API). [#10012](https://github.com/IfcOpenShell/IfcOpenShell/issues/10012)

**Why it happens.** There is no standard "penetration" object; an opening is a separate `IfcOpeningElement` related with `IfcRelVoidsElement`; clearance, sleeve rules and fire-rating are project decisions. The real MCP implementation in the zh thread is read-only, returns `candidate` / `review_required` states and uses **no default clearance**.

**What a good assistant should do.** Intersect MEP segments with hosts, subtract crossings that already sit inside an opening, return a table, and let a human confirm. Treat oblique crossings and beam penetrations as needing review. If asked for sleeve size, ask for the clearance rule; do not assume 30 mm.
**Clarifying questions:** Clearance per side? Which hosts (walls only, slabs, beams)? Which fire rating counts? Should existing openings/sleeves be excluded? Main model or linked model?

### 14. Converting IFC pipes into native Revit MEP

**What users say**
- ja: «IFCをRevitのMEP要素(配管・ダクト)に変換するアドインを作ろうとして失敗» (EN: I tried to build an add-in converting IFC to Revit MEP pipes/ducts and failed). [Qiita](https://qiita.com/KengoTanaka-BIM/items/6cec74e04bf581b21cf5)
- ja: «元請から意匠IFCを受けて設備ルートを3D確認したい。ソフトを買う根拠がない» (EN: small MEP office wants to check routes in 3D against the architect's IFC without buying software). [note.com](https://note.com/limber_stork5044/n/n68df8d5a268b)

**Why it happens.** Link IFC gives DirectShapes, which are not editable and carry no pipe parameters the API can set. The Qiita author concluded full automatic conversion is not feasible and suggested narrower tools (quantity summaries).

**What a good assistant should do.** Be upfront that there is no one-click conversion, offer the realistic alternatives (link and model over; extract quantities; view only).

---

## Real questions

All rows are paraphrases from the linked source. "Persona" is the role inferred by the research pass.

| lang | Question (original-language paraphrase) | EN gloss | Persona | Source |
|---|---|---|---|---|
| en | Pipes carry the system material name rather than the real material; some systems mix PVC and HDPE; how do I export the actual material? | — | mep_engineer | [revit-ifc #577](https://github.com/Autodesk/revit-ifc/issues/577) |
| en | Several MEP IFCs received, some coloured, some grey; I suspect the MVD. What is the root cause? | — | bim_coordinator | [revit-ifc #579](https://github.com/Autodesk/revit-ifc/issues/579) |
| en | Hot water red, cold blue, sewage green in Revit become beige/blue/blue in ArchiCAD; I tried IfcPresentationLayer. | — | mep_engineer | [bSI forum](https://forums.buildingsmart.org/t/how-can-i-control-the-ifc-pipes-colors-revit-to-archicad/2729) |
| en | Duct fitting material disappears in the IFC. | — | mep_engineer | [Autodesk forum](https://forums.autodesk.com/t5/revit-mep-forum/losing-duct-fitting-material-when-exported-to-ifc-files/td-p/8736337) |
| en | One duct type used for Supply and Return, coloured by system, but fittings export wrong. | — | mep_engineer | [revit-ifc #373](https://github.com/Autodesk/revit-ifc/issues/373) |
| en | Security devices export as proxies while electrical equipment exports correctly. | — | mep_engineer | [Autodesk forum](https://forums.autodesk.com/t5/revit-mep-forum/ifc-export-issue/m-p/12250648) |
| en | Ducts and pipes show as generic types after export. | — | mep_engineer | [Autodesk forum](https://forums.autodesk.com/t5/revit-mep-forum/ifc-export-ducts-and-pipes/td-p/12370919) |
| en | PVC reducing coupling joins different pipe sizes; CONNECTOR for couplings, but two different ports suggest TRANSITION. | — | mep_engineer | [bSI forum](https://forums.buildingsmart.org/t/best-ifc-classification-for-a-reducing-coupling/5963) |
| en | There is no obvious IFC class for a grounding rod. | — | mep_engineer | [bSI forum](https://forums.buildingsmart.org/t/ifc-class-for-earthing-rod/5632) |
| en | IfcExportAs=IfcFlowMeterType and IfcExportType=WATERMETER exports the class but PredefinedType is NOTDEFINED. | — | mep_engineer | [revit-ifc #525](https://github.com/Autodesk/revit-ifc/issues/525) |
| en | New to IFC: I made a shared parameter named like the duct Pset Material attribute but it does not appear in the IFC. | — | bim_coordinator | [bSI forum](https://forums.buildingsmart.org/t/ifc-mapping-in-revit-mep/4591) |
| en | How do I map width/height for rectangular and diameter for round to the same pset property, depending on which exists? | — | mep_engineer | [revit-ifc #303](https://github.com/Autodesk/revit-ifc/issues/303) |
| en | Consultants send IfcFlowSegment instead of specific classes; our HVAC mapping tables must be re-selected every time. | — | bim_manager | [revit-ifc #798](https://github.com/Autodesk/revit-ifc/issues/798) |
| en | I tried to put user-defined psets on an IfcSystem but none appear in the IFC. | — | mep_engineer | [revit-ifc #523](https://github.com/Autodesk/revit-ifc/issues/523) |
| en | Can I override the IfcDistributionSystem membership of elements, like I override IfcName via shared parameters? | — | bim_coordinator | [revit-ifc #900](https://github.com/Autodesk/revit-ifc/issues/900) |
| en | Circuits are not written when export is limited to visible elements. | — | bim_coordinator | [revit-ifc #959](https://github.com/Autodesk/revit-ifc/issues/959) |
| en | IfcSystem info for pipes exists in the IFC2x3 export but not in IFC4. | — | bim_coordinator | [bSI forum](https://forums.buildingsmart.org/t/ifcsystem-information-related-to-pipes-ifc4-from-revit/3178) |
| en | As MEP coordinator I colour by system abbreviation; where does the system code go in IFC? | — | mep_engineer | [bSI forum](https://forums.buildingsmart.org/t/mep-system-classification/2464) |
| en | Ports can't be disabled in the export options and my models are large. | — | bim_manager | [revit-ifc #630](https://github.com/Autodesk/revit-ifc/issues/630) |
| en | Ports are lost when I import MEP types from a project library. | — | mep_engineer | [OSArch](https://community.osarch.org/discussion/2885/ifcpipefittingtype-does-not-import-ports-from-a-library) |
| en | Our coordination app needs connected-network selection; connectivity is lost in native IFC to Fragments conversion. | — | developer_programmer | [ThatOpen #27](https://github.com/ThatOpen/platform_services/issues/27) |
| en | Flow in L/s is exported in ft3/s. | — | mep_engineer | [revit-ifc #444](https://github.com/Autodesk/revit-ifc/issues/444) |
| en | Pipe and duct plus their insulation come out as one IfcPipeSegment/IfcDuctSegment in IFC4. | — | mep_engineer | [revit-ifc #416](https://github.com/Autodesk/revit-ifc/issues/416) |
| en | Industrial plant export takes 6h16 and 720 MB with insulation vs 2h43 without. | — | bim_manager | [revit-ifc #892](https://github.com/Autodesk/revit-ifc/issues/892) |
| en | Fabrication ductwork produces hundreds of duplicate IfcElementTypes; each type has one occurrence. | — | bim_coordinator | [revit-ifc #510](https://github.com/Autodesk/revit-ifc/issues/510) |
| en | 400 MB+ Revit IFC4 MEP files abort with "memory access out of bounds" in GetFlatMesh/GetLine. | — | developer_programmer | [web-ifc #1999](https://github.com/ThatOpen/engine_web-ifc/issues/1999) |
| en | Linking an MEP IFC drops many elements in 2023; the log is full of pGeomArr validation errors. | — | mep_engineer | [revit-ifc #658](https://github.com/Autodesk/revit-ifc/issues/658) |
| en | Dedicated penetration tool wanted: host-aware placement, updates when MEP moves, clearance offsets, batch from clash scan. | — | mep_engineer | [IfcOpenShell #8037](https://github.com/IfcOpenShell/IfcOpenShell/issues/8037) |
| en | I want total data ports per floor to size telecom racks; the family stores a port count parameter but every attempt returns null; ChatGPT and Gemini didn't help. | — | mep_engineer | [Dynamo forum](https://forum.dynamobim.com/t/extracting-telecom-data-port-quantities-from-bim-model-using-dynamo/114169) |
| en | Keep getting "Method XXX not found" errors although the MCP server and Revit plugin work: "list all pipes in the revit model". | — | mep_engineer | [revit-mcp #28](https://github.com/mcp-servers-for-revit/revit-mcp/issues/28) |
| en | A basic MEP IFC (header says generated by OpenAI) cannot be opened. | — | other | [IfcOpenShell #7945](https://github.com/IfcOpenShell/IfcOpenShell/issues/7945) |
| es | Ejecuta la corrida 5 HVAC sobre mi selección actual en modo detalle. | Run the HVAC takeoff on my current selection in detail mode (ducts and fittings with size, length, area, gauge, kilos). | estimator_qs | [RevitMCPBOQ](https://github.com/JefaturaBIM94/RevitMCPBOQ) |
| zh | 機電管線穿過牆、樓板或樑時要逐筆確認穿透位置與開孔大小；希望AI能回傳候選清單 | Turn the manual MEP-penetration opening-locating workflow into AI-callable tools. | mep_engineer | [REVIT_MCP_study #99](https://github.com/shuotao/REVIT_MCP_study/issues/99) |
| ja | Jw_cadで2D図面。元請から意匠IFCを受けて設備ルートを3D確認したい。ソフトを買う根拠がない | Small MEP office on Jw_cad wants to check routes in 3D from the architect's IFC without a purchase case. | mep_engineer | [note.com](https://note.com/limber_stork5044/n/n68df8d5a268b) |
| ja | IFCをRevitのMEP要素(配管・ダクト)に変換するアドインを作ろうとして失敗 | I tried an add-in converting IFC to Revit MEP elements and failed. | developer_programmer | [Qiita](https://qiita.com/KengoTanaka-BIM/items/6cec74e04bf581b21cf5) |
| nl | Waarom geen verwijzing naar Systems (IfcDistributionSystem)? NL-SfB-codes sluiten niet geheel aan op de praktijk. | Why no reference to IfcDistributionSystem; NL-SfB does not match practice for installations. | mep_engineer | [digiGO imwo #52](https://github.com/nl-digigo/imwo/issues/52) |
| no | Hvordan skal kummer, rør og rørdeler modelleres i IFC 4.3 for VA? | How should manholes, pipes and pipe parts be modelled in IFC 4.3 for water and wastewater? | civil_infra_engineer | [buildingSMART Norge](https://www.buildingsmart.no/standarder/publikasjoner-og-veiledninger.html) |
| es | Exportar resultados de cálculo eléctrico a DXF/IFC con propiedades eléctricas para Revit y AutoCAD. | Export electrical calculation results with electrical psets. | mep_engineer | [calculadora-RIC #10](https://github.com/jmarinderko/calculadora-RIC/issues/10) |
| zh | Revit机电专业IFC导入BIM5D操作过程 | Steps to export a Revit MEP model to IFC and import it into Glodon BIM5D. | mep_engineer | [zhulong](https://www.zhulong.com/zt_bim_3002296/detail40283815/) |
| en | ETABS model exported with Structural Analysis View shows nothing in Solibri or BIMsight; can geometry be put into this view? | — | structural_engineer | [bSI forum](https://forums.buildingsmart.org/t/ifc-structural-analysis-view/1267) |
| en | I want to export STAAD analysis results, not just the model, so clients can view them in a general BIM viewer. | — | structural_engineer | [bSI forum](https://forums.buildingsmart.org/t/ifcstructuralanalysisdomain/832) |
| en | Mapped nodes to IfcStructuralPointConnection and axes to IfcStructuralCurveMember; is there a dedicated object for rigid links? | — | structural_engineer | [bSI forum](https://forums.buildingsmart.org/t/rigid-link-representation-in-structural-analysis-model/1364) |
| en | AxisVM structural analysis IFC fails to load with a StopIteration error. | — | structural_engineer | [IfcOpenShell #6459](https://github.com/IfcOpenShell/IfcOpenShell/issues/6459) |
| en | IfcStructuralCurveMembers no longer display after the Bonsai update; the example file displayed before. | — | structural_engineer | [IfcOpenShell #5788](https://github.com/IfcOpenShell/IfcOpenShell/issues/5788) |
| en | Applying, editing and seeing loads in Bonsai is hard and nothing analyses the model; I want easier load authoring and a solver. | — | structural_engineer | [IfcOpenShell #9866](https://github.com/IfcOpenShell/IfcOpenShell/issues/9866) |
| en | I tested an RFEM round trip: missing declares, member axis, units, load direction flipped by Z-down axes. | — | structural_engineer | [OSArch](https://community.osarch.org/discussion/comment/30616#Comment_30616) |
| en | Tolerance rounds 10-decimal coordinates so elements disconnect after import into ETABS. | — | structural_engineer | [BHoM #548](https://github.com/BHoM/ETABS_Toolkit/issues/548) |
| en | How do I get start and end coordinates of each member from a Tekla IFC to build an OpenSeesPy model? | — | researcher_academic | [IfcOpenShell #5931](https://github.com/IfcOpenShell/IfcOpenShell/issues/5931) |
| ru | не происходит экспорт модели из ревита в старк ес | Revit to STARK ES link: model export does not happen. | structural_engineer | [dwg.ru](https://forum.dwg.ru/showthread.php?t=133669) |
| ru | не все элементы передаются из Ревита 2016 в Старк ЕС, IFC пробовала — результат плохой | Elements are lost to STARK ES; IFC tried, result unsatisfactory. | structural_engineer | [dwg.ru](https://forum.dwg.ru/showthread.php?t=133669) |
| ru | как лучше передать конструктив из Ревита в СКАД, есть ли прямая связь, можно ли DWG/DXF | Best way to move structure from Revit into SCAD: direct link, DWG/DXF or IFC? | structural_engineer | [dwg.ru](https://forum.dwg.ru/showthread.php?t=142967) |
| ru | как перенести модель из архитектурной программы в расчётную, какой формат лучше, через IFC можно? | Which format moves an Archicad model into analysis software; IFC import to SCAD gives odd wall junctions. | structural_engineer | [dwg.ru](https://forum.dwg.ru/showthread.php?t=33352) |
| ru | экспорт в расчётные программы через IFC | Revit Structure lesson: export to calculation programs via IFC. | structural_engineer | [YouTube](https://www.youtube.com/watch?v=z1BcpIq3Tss) |
| es | Problema al importar modelo de Revit en plantilla de estructuras; ETABS muestra mensaje de error | ETABS shows an error importing the Revit IFC. | structural_engineer | [bSI forum](https://forums.buildingsmart.org/t/como-poder-exportar-un-modelo-3d-estructural-realizado-en-revit-a-etabs-por-medio-del-formato-ifc/2985) |
| zh | BIM模型於結構分析軟體之資料傳遞研究：Revit傳到Robot/ETABS/SAP2000，IFC方式資料遺失或更動 | NTU thesis: IFC transfer lost or changed data; native and API better. | structural_engineer | [NTU](https://tdr.lib.ntu.edu.tw/handle/123456789/90111) |
| ja | IfcIShapeProfileDefのFlangeSlopeは正の値でどっち向き？基準位置はフランジのどこ？ | Sign and reference position of FlangeSlope are unspecified; which way is positive? | researcher_academic | [Zenn](https://zenn.dev/kiyuka/scraps/2894037aa4f997) |
| en | Steel and steel-connected framing are missing from the export after 2025.4.3. | — | structural_engineer | [revit-ifc #890](https://github.com/Autodesk/revit-ifc/issues/890) |
| en | Beams and columns vanish from IFC in Revit 2026, blamed on the predefined type. | — | structural_engineer | [revit-ifc #952](https://github.com/Autodesk/revit-ifc/issues/952) |
| en | Hollow square columns with base plate connections are displaced in IFC2x3 and the IFC4 file will not open. | — | structural_engineer | [revit-ifc #1010](https://github.com/Autodesk/revit-ifc/issues/1010) |
| en | Revit weld exports to 0.0 (welds at origin). | — | structural_engineer | [revit-ifc #901](https://github.com/Autodesk/revit-ifc/issues/901) |
| en | Structural connections lack shared parameters in the IFC. | — | structural_engineer | [Autodesk forum](https://forums.autodesk.com/t5/revit-structure-forum/structural-connections-ifc-parameters/td-p/13252740) |
| en | Beam NetWeight is not exported as IfcQuantityWeight. | — | estimator_qs | [revit-ifc #764](https://github.com/Autodesk/revit-ifc/issues/764) |
| en | Reinforcement rounding is not reflected in the IFC (3422 instead of 3420). | — | structural_engineer | [revit-ifc #14](https://github.com/Autodesk/revit-ifc/issues/14) |
| en | Rebar sets are split into many entities; I want a set as a single instance (file went 200 MB to 70 MB after a merge). | — | bim_coordinator | [revit-ifc #76](https://github.com/Autodesk/revit-ifc/issues/76) |
| en | API-created rebar container does not export to IFC. | — | developer_programmer | [revit-ifc #335](https://github.com/Autodesk/revit-ifc/issues/335) |
| en | I want rebar coloured by diameter in the IFC as it appears in the view. | — | structural_engineer | [revit-ifc #731](https://github.com/Autodesk/revit-ifc/issues/731) |
| en | Rebar geometry from IfcSweptDiskSolid fails to convert though BimVision, DDScad and Solibri open the same file. | — | developer_programmer | [IfcOpenShell #4945](https://github.com/IfcOpenShell/IfcOpenShell/issues/4945) |
| en | Precast + rebar Tekla IFC does not render in a web viewer. | — | bim_coordinator | [web-ifc #445](https://github.com/ThatOpen/engine_web-ifc/issues/445) |
| en | How do I model precast girder stirrups that are bent in the field, conveying both fabricator and final geometry? | — | structural_engineer | [bSI forum](https://forums.buildingsmart.org/t/field-bent-rebar/5870) |
| en | Detailing software groups bars but IFC lacks a group entity; proposal: IfcReinforcingBarGroup. | — | structural_engineer | [bSI forum](https://forums.buildingsmart.org/t/there-is-a-need-for-a-reinforcing-bar-group/5688) |
| en | I want rebar weight per concrete volume as a custom Qto for a cost schedule; rebar is not modelled. | — | estimator_qs | [OSArch](https://community.osarch.org/discussion/2578/how-to-create-a-custom-qto-calculation) |
| en | Calculate Gross/NetWeight from MassPerLength times length so hollow steel sections need not be modelled in detail. | — | estimator_qs | [IfcOpenShell #6344](https://github.com/IfcOpenShell/IfcOpenShell/issues/6344) |
| en | Open IFC creates in-place families without IFC data; Link IFC duplicates assembly and parts (Tekla). | — | bim_manager | [revit-ifc #223](https://github.com/Autodesk/revit-ifc/issues/223) |
| ru | Почему не меняется материал и тонирование колонн в Revit 2020, экспортированных из Tekla? | Why can't I change material/shading of Tekla columns in Revit; rebar and connections not carried. | structural_engineer | [dwg.ru](https://forum.dwg.ru/showthread.php?t=155997) |
| ru | арматура неправильно отображается в BIMsight после экспорта, как передать свойства | Rebar shows wrongly in BIMsight after Tekla IFC export; how to export properties? | structural_engineer | [dwg.ru](https://forum.dwg.ru/showthread.php?t=150272&page=2) |
| ru | Как из Advance Steel вывести модель в Archicad | How to move a model from Advance Steel into Archicad, in what order? | structural_engineer | [dwg.ru](https://forum.dwg.ru/showthread.php?t=163697) |
| ru | что выбрать конструктору КЖ: Revit, Tekla или Allplan | Compare Revit, Tekla, Allplan for reinforced concrete; which handles IFC links better? | structural_engineer | [dwg.ru](https://dwg.ru/b/utrfm/263) |
| no | Hvordan går vi fra armeringsmodell til bestilling og produksjon med åpne standarder? | From a rebar model to ordering and production with open standards. | structural_engineer | [buildingSMART Norge](https://www.buildingsmart.no/standarder/publikasjoner-og-veiledninger.html) |
| en | TQS plugin writes kg per diameter; special elements need automation of host element parameters. | — | structural_engineer | [Dynamo forum](https://forum.dynamobim.com/t/exporting-reinforcement-data-from-revit-to-ifc-automating-host-element-parameters/101288) |

---

## Ready test prompts

All prompts below are **synthetic** (written for testing, never real quotes). "Base" names the synthetic record in `research_raw/wave1` it was derived from; "new" means written for this page. Several were reworded to sound less like a textbook. "Expected behavior" is what a good assistant or MCP server should do; the tester judges against it. Difficulty: easy = one read-only lookup; medium = grouping, comparison, or one ambiguity; hard = multi-step, absent data, risk of invention, or a write.

| # | lang | Prompt | Type | Difficulty | Expected behavior |
|---|---|---|---|---|---|
| M01 | en | list all pipes in the model with system type and diameter | query_model_data | easy | Query pipes, group by system type, return diameters. If the Revit tool replies "Method not found", report a likely server/plugin version mismatch instead of looping. (base en-aimcp-s006) |
| M02 | en | pipes show material = system name (HOT WATER) not copper. can you list pipes and what material they actually have | query_model_data | medium | Read material associations for pipe segments, list distinct names, flag those equal to system names; say whether a real material exists elsewhere (pset/type); do not invent copper. (base en-eng-s003) |
| M03 | en | which pipes and fittings arent in any IfcSystem? need before coord meeting | validate_check | medium | Find flow segments/fittings without `IfcRelAssignsToGroup` to a system; list with names, levels and GlobalIds; if the file has no systems at all say that first. (base en-eng-s002) |
| M04 | ru | покажи воздуховоды и трубы которые не входят ни в одну систему, ифс из ревита, нужно до сдачи | validate_check | medium | Same check; mention that systems may be missing because of export options (visible-only), ask for the Revit exporter version if everything is orphaned. (base ru-mep-s005) |
| M05 | ru | при экспорте в ifc системы вентиляции пропали, в навигаторе пусто, галку Export only visible вроде стояла. че не так | troubleshoot_export | medium | Explain that systems are groups and can be dropped when export is limited to visible elements (reported in revit-ifc #959 for circuits); ask version; if a file is available check for systems; do not claim to change Revit settings without a Revit tool. (base ru-mep-s006) |
| M06 | en | which ducts/fittings have ports with no IfcRelConnectsPorts? need the open ends for the coord meeting | validate_check | hard | Collect ports via nesting, check ConnectedTo/ConnectedFrom, list parent element, system, level and flow direction for open ones; state IFC version assumptions. (base en-mep-s002) |
| M07 | it | controlla se le porte dei raccordi hanno FlowDirection SOURCE/SINK coerente con il flusso, export DDS-CAD | validate_check | hard | Read port FlowDirection and connections, flag SOURCE-SOURCE or SINK-SINK pairs; explain that tees have more than two ports and direction is a usage convention. (base it-mep-s014) |
| M08 | en | how do i get the element on the other side of a duct port in ifcopenshell? ports are nested but i keep getting None | troubleshoot_code | medium | Explain nesting (`IsNestedBy`/`Nests`) vs `ConnectedTo`/`ConnectedFrom`, and that IFC2x3 uses a different relation; give a short code sketch. (base en-mep-s015) |
| M09 | fr | verifie les unites des debits sur les gaines, j'ai l'impression que c'est en ft3/s au lieu de L/s | validate_check | hard | Inspect unit assignment and the property's unit, show raw vs converted values, say it looks like the known Revit L/s bug if so; do not silently rewrite the file. (base fr-mep-s011) |
| M10 | de | gib mir alle Rohre mit DN und Volumenstrom aus dem Pset, MagiCAD Export, als Liste pro Gewerk | query_model_data | medium | Read segment psets (nominal diameter, flow), group by system/discipline, mark missing values rather than filling them. (base de-mep-s007) |
| M11 | en | set predefined type TRANSITION on all reducer pipe fittings | modify_model_data | hard | Identify reducers by differing port sizes, show list and count first, ask confirmation, change on a copy, verify after reload. (base en-eng-s008) |
| M12 | pt | as conexoes estao vindo como proxy, muda tudo pra IfcPipeFitting e poe o tipo TRANSITION nas reducoes | modify_model_data | hard | Warn that name-based reclass is a guess, list candidates, ask confirmation, preserve GlobalIds, report counts. (base pt-mep-s010) |
| M13 | ja | Revitの吊りボルトとサポートをIFCに出したいけど、クラスはどれが正解？ | how_to | medium | Recommend a discrete accessory class via Export-to-IFC-As, avoid proxy, state that evidence in the KB is thin and the choice depends on the receiving party. (base ja-mep-s012) |
| M14 | en | file is 700MB, drop the insulation and ports, keep everything else, and tell me size after | modify_model_data | hard | Warn that removing ports kills connectivity; work on a copy; report what was removed and size before/after. (base en-mep-s016) |
| M15 | en | total insulation per system - is it separate element or merged into the pipe? give length/area by system | extract_quantities | hard | Detect whether insulation is a separate covering or inside segment geometry; sum by system or explain it cannot be separated. (base en-mep-s004) |
| M16 | de | kannst du mir Kollisionen zwischen Lüftungskanälen und Unterzügen im Koordinationsmodell raussuchen und nach Geschoss gruppieren? für die BCF Liste | coordinate_clash | medium | Run duct vs beam clash across federated files, group by storey, prepare BCF-style list; ask tolerance and whether touching counts. (base de-coord-s011) |
| M17 | ru | прогони коллизии вентиляция vs балки, допуск 20мм, сгруппируй по этажам, без касаний | coordinate_clash | medium | Ask whether 20 mm is overlap tolerance or clearance; exclude touching; group by storey; report counts. (base ru-clash-s007) |
| M18 | en | need list of ducts and pipes that go thru fire rated walls but have no opening, pls export as bcf | coordinate_clash | hard | Intersect MEP with walls having a fire rating, exclude those inside an existing opening, export BCF only after listing; say if FireRating property is missing. (base en-openings-s003) |
| M19 | zh | 幫我掃一下水管穿樑的位置,列出每個穿透點需要的套管口徑,預留每邊30mm | coordinate_clash | hard | Pipe-vs-beam intersections, sleeve = diameter + 2x30 mm, flag oblique or beam penetrations for review, read-only. (base zh-revit-auto-s011) |
| M20 | ko | 배관이 벽 관통하는데 슬리브 안 들어간 곳 뽑아줘 | coordinate_clash | medium | Find pipe-wall crossings without sleeve/opening; list; ask what counts as a sleeve in this model. (base ko-openings-s018) |
| M21 | es | dame los ductos por nivel con longitud, area y kilos, solo los de la selección | extract_quantities | hard | Needs a live Revit selection; ask material/gauge for "kilos" or state assumptions; report method (direct vs estimate). (base es-aimcp-s015) |
| M22 | zh | revit导出ifc后管道颜色都是灰的，系统颜色没带出来，用的哪个设置？ | troubleshoot_export | medium | Colour comes from materials/by-category not view filters; guide material colour and IfcStyledItem check. (base zh-mep-s008) |
| M23 | nl | welke installatieobjecten zitten niet in een IfcSystem? en hebben ze NL-SfB 5x codes? | validate_check | medium | List unassigned MEP elements and classification presence in one table. (base nl-dutch-s013) |
| M24 | no | list opp alle ventilasjonssystemer og antall kanaler i hvert system | query_model_data | easy | Systems with duct counts; flag empty systems. (base no-norway-s007) |
| M25 | ru | посчитай длину воздуховодов по системам, в ифс они в IfcSystem вроде | extract_quantities | medium | Group ducts by system, sum Length from quantities or geometry; report which source; note missing system links. (base ru-eng-s009) |
| M26 | ja | 設備モデルのIFC、前回と今回の差分を出してもらえますか。ダクトとか配管だけで | compare_versions | medium | Diff by GlobalId for duct/pipe classes; warn that Revit can regenerate GlobalIds unless "Store IFC GUID" was on; fall back to geometry/name matching only if asked. (base ja-eng-s016) |
| M27 | en | do ducts have NominalDiameterOrWidth and NominalHeight in Pset_DuctSegmentTypeCommon? show those missing | validate_check | medium | Check type and occurrence psets; list segments lacking the properties; note round vs rectangular. (base en-psets-s011) |
| S01 | en | is there an actual analysis model in this ifc? count structural curve members, point connections and load cases | query_model_data | easy | Count analysis model, curve members, connections, load groups; if absent, say "this file has only the physical model" and explain. (base en-eng-s004) |
| S02 | en | show every IfcStructuralCurveMember with profile, material, start/end point connection. whats missing before i can send this to the solver (density, units, supports)? | query_model_data | hard | Enumerate members; report missing density, yield strength, unit mismatches, supports. (base en-struct-s004) |
| S03 | ru | как из ревита в ifc выгрузить расчётную схему чтобы открыть в Robot или Лире? стержни и узлы а не тела | how_to | hard | Explain analytical vs physical model, that the default Revit exporter does not write the analytical branch (per forum reports), offer alternatives; do not claim a setting that does it. (base ru-struct-s007) |
| S04 | es | exporté de revit a etabs por ifc y me sale error al importar, que config del exportador debo usar? | troubleshoot_import | medium | Ask exporter/IFC version and the ETABS message; explain what ETABS needs; inspect the file if given. (base es-err-s007) |
| S05 | it | controlla se nel modello analitico ci sono vincoli e carichi assegnati, altrimenti SCIA non lo calcola | validate_check | medium | Check boundary conditions and load groups; list missing. (base it-struct-s017) |
| S06 | en | opened structural ifc and nothing shows, only axes? why | troubleshoot_viewing | easy | Analytical members have no solid; hidden by default in some viewers; check filters. (base en-eng-s017) |
| S07 | en | we lost beams and columns in the IFC after the exporter update. list IfcBeam/IfcColumn counts per level so i can compare with revit schedule | validate_check | medium | Per-storey counts including IfcMember; hint at "Include steel elements" and exporter build. (base en-struct-s002) |
| S08 | zh | revit导出ifc钢结构节点螺栓全没了，勾了包含钢构件也不行，咋回事 | troubleshoot_export | hard | Count fasteners/plates; explain the option and known regressions; suggest build check; cannot promise a fix. (base zh-struct-s009) |
| S09 | en | how many IfcReinforcingBar in this model and are the sets exported per bar or as one instance? need to know why the file is so big | query_model_data | medium | Count, group by set/pset, estimate size impact. (base en-struct-s001) |
| S10 | ru | глянь арматура в ифс пришла как IfcReinforcingBar или опять прокси? выдай диаметры и общую длину по классам | query_model_data | medium | Count `IfcReinforcingBar` vs proxies named like rebar; diameters and total lengths per class. (base ru-struct-s006) |
| S11 | de | mach mir ne Stahlliste aus dem IFC, Bewehrung nach Durchmesser, Gewicht in kg | extract_quantities | medium | Group by NominalDiameter, compute mass with a stated density (7850 kg/m3), flag bars with no length. (base de-struct-s012) |
| S12 | en | pull rebar from the ifc - bar mark, size, length, count and total weight per pier. need it for the bid | extract_quantities | hard | Per-host aggregation only if host relations exist; state assumptions; flag missing quantities; a bid number needs a caveat. (base en-us-canada-infra-s007) |
| S13 | ja | 鉄骨の梁をプロファイル別に本数と重量集計して。H-400x200とか | extract_quantities | medium | Group by profile name, weight from quantity or MassPerLength x length, flag missing. (base ja-japan-s012) |
| S14 | en | linked tekla ifc in revit and everything is doubled, assembly + parts. how to avoid? | troubleshoot_import | medium | Explain assembly plus sub-part import; map assembly class to a deletable category. (base en-tekla-s012) |
| S15 | en | tekla precast ifc w/ rebar kills my web viewer. can u make a lighter copy without IfcReinforcingBar? | convert_format | medium | Filtered copy removing rebar/fasteners, report size reduction and exactly what was removed. (base en-struct-s005) |
| S16 | es | ponle acero S275 a todas las vigas y pilares del modelo y mételo en un pset propio | modify_model_data | hard | Show counts, ask pset/property names, write, reload to verify; do not overwrite existing grades silently. (base es-struct-s010) |
| S17 | zh | 梁柱的材质是不是都写了混凝土强度等级？C30 C35 这种，没写的挑出来 | validate_check | medium | Read material names/psets on beams and columns, regex for grade, list those without. (base zh-revit-export-s013) |
| S18 | pt | como levar o modelo da estrutura metálica do Tekla pro Robot via IFC sem perder os perfis? | how_to | medium | Profiles live in material profile sets; IFC transfer to analysis is lossy; mention alternatives; inspect profiles if a file is given. (base pt-struct-s011) |
| S19 | ja | 梁の開口位置がZ方向にずれている気がします。IFC4で出したものを確認してもらえますか | validate_check | hard | Compare opening placement with the host beam's bounding box; known IFC4 issue fixed in Revit 2026. (base ja-geom-s013) |
| S20 | en | can you just fix the rebar weights, the model says 0 for half of the bars | modify_model_data | hard | Do not write numbers without basis: find why weights are 0 (missing length/quantity), propose a recompute with stated density, ask before writing. (new) |

---

## Edge cases and traps for MCP testing in this area

1. **"No result" is not "no problem".** If a file has no `IfcSystem`, no ports, no `IfcMechanicalFastener` or no `IfcReinforcingBar`, the assistant must say that explicitly and offer likely export causes; it must not return an empty table as if everything were fine.
2. **IFC2x3 vs IFC4 vocabulary.** `IfcDuctSegment`/`IfcPipeSegment` do not exist in IFC2x3 (generic `IfcFlowSegment`); ports are related differently (`IfcRelConnectsPortToElement` vs nesting). A query written for one version silently returns nothing on the other.
3. **System name as material.** Pipes whose material is literally "Domestic Hot Water" are a known exporter behaviour. Test that the assistant flags it instead of reporting "material: Domestic Hot Water" as a fact.
4. **Name-based reclassification is a guess.** Prompts like "change everything called reducer to TRANSITION" should trigger a preview and confirmation, preservation of GlobalIds, and verification after reload.
5. **Weights from nowhere.** For "kilos" and "total weight" the answer needs a source (Qto, pset, MassPerLength x length, density x volume). A number with no stated source or density is a failure; so is silently using 7850 kg/m3 for a concrete bar's host.
6. **Rebar can be gigantic.** A single Tekla precast model can mean hundreds of thousands of entities. Whole-file operations should warn, filter by class first, and avoid dumping thousands of GlobalIds in a reply.
7. **Hosted rebar is not guaranteed.** The bar-to-host relation may be assembly, aggregation, nesting or nothing. "Rebar per column" must say when the host relation is absent.
8. **Analytical vs physical.** A request for "the analysis model" on a file with only solids is a trap. The correct answer explains the difference; the wrong answer fabricates nodes from beam axes without saying so.
9. **Flow units and Z-down axes.** Check that the assistant reports units before comparing values, and does not flip load directions or axis conventions without being asked.
10. **Clash "tolerance".** In Russian and English prompts "20 mm tolerance" can mean overlap threshold or clearance distance. Strong assistants ask; weak ones pick one silently. Also test "without touching" (exclude coplanar contacts).
11. **Penetration clearance.** "Reserve 30 mm per side" is a user instruction; with no number given the assistant must ask, not default.
12. **GlobalId churn.** Diffing two Revit exports by GlobalId works only if GUIDs were stored or stable; otherwise everything looks changed. Good assistants warn and offer name/geometry matching.
13. **Revit selection vs IFC file.** "Only my selection" requires a live Revit session; against a static IFC it is meaningless. Likewise "set the Revit export option" requires a Revit tool, not an IFC reader.
14. **Version mismatch noise.** "Method not found" from a Revit MCP plugin is often a server/plugin version mismatch. Test that the assistant stops after one or two attempts and reports it.
15. **AI-generated IFC.** A hand-made IFC claimed to be "generated by OpenAI" failed to open; the useful response is to run a schema validation (e.g. the buildingSMART validation service) and fix errors, not to guess.
16. **Multilingual identifiers.** Mixed-language prompts ("ифс", "ифс из ревита", "ОВ и ВК", "КЖ") use discipline abbreviations. ОВ/ОВиК = HVAC, ВК = water/sewer, ЭОМ = electrical, КЖ = reinforced-concrete structures. The assistant should map them without asking for translation.
17. **Do not claim standards status from memory.** Statements like "Revit exports the analytical model" or "IFC 4.4 includes X" are version-dependent; answers should say "per the file I inspected" rather than quote support claims.

---

## Related docs

- [IFC domain overview: MEP, structural, infrastructure, 4D/5D, FM](../../01_ifc_basics/08_domains_mep_structural_infra_4d5d_fm.md)
- [Spatial structure and relationships (systems, groups, containment)](../../01_ifc_basics/04_spatial_structure_and_relationships.md)
- [Properties, quantities, psets](../../01_ifc_basics/05_properties_quantities_psets.md)
- [Geometry, placement, units](../../01_ifc_basics/06_geometry_placement_coordinates_units.md)
- [Materials, classification, types, styles](../../01_ifc_basics/07_materials_classification_types_styles.md)
- [Revit IFC export reference](../../03_software/revit/ifc_export_reference.md) and [import/link reference](../../03_software/revit/ifc_import_link_reference.md)
- [Authoring tools (Tekla, Archicad, Allplan, Civil 3D, Bonsai)](../../03_software/authoring_tools_ifc.md)
- [Viewers, checkers, CDE, converters](../../03_software/viewers_checkers_cde_converters.md)
- [MCP servers and AI tools for IFC/Revit](../../04_open_source/mcp_servers_and_ai_tools.md)
- [Libraries and toolkits (IfcOpenShell, web-ifc, xBIM)](../../04_open_source/libraries_and_toolkits.md)
- [Glossary (multilingual)](../../08_glossary/glossary_multilingual.md) and [abbreviations](../../08_glossary/abbreviations.md)
- Companion page: [Infrastructure, site, GIS, energy](infrastructure_site_gis_energy.md)
