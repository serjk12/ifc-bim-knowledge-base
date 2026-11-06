# MEP engineer: who they are and what they do with IFC

> Persona tag in the data: `mep_engineer`. Evidence base: `kb.py stats --persona mep_engineer` gives 143 records (84 real, 59 synthetic) from `research_raw/wave1`. Last compiled 2026-11-06.
> Sibling pages: [structural engineer](structural_engineer.md), [civil / infrastructure engineer](civil_infra_engineer.md), [contractor / site](contractor_site.md), [developer](developer_programmer.md). Topic overview: [MEP, structural, rebar](../by_topic/mep_structural_rebar.md); related: [coordination, clash, BCF](../by_topic/coordination_clash_bcf_cde.md).

## In plain words

MEP stands for **M**echanical, **E**lectrical, **P**lumbing: ventilation and air conditioning (HVAC, "ОВиК", "TGA/HLS", "暖通"), water supply and drainage ("ВК", "Sanitär"), fire protection, power and low-current cabling, cable trays. An MEP engineer designs the *network* inside the building: ducts, pipes, fittings, valves, pumps, air terminals, panels, luminaires, cable trays, and the **systems** that group them ("Supply Air 1", "Hot Water", "Sewer").

For them IFC is mostly a **delivery and coordination format**: they export their model so the BIM coordinator can look for clashes with the architecture and structure, so the architect can see where the shafts must be, and so the contractor and facility manager receive equipment lists. Their typical sentence is not "write me an IfcDuctSegment query" but "which pipes are not in any system" or "where do my ducts go through fire walls and is there already a hole".

What makes MEP special in IFC (plain version):
- A pipe run is not one object; it is many straight **segments** joined by **fittings**, and the join is made through **ports** (connection points). If the ports are not exported, the network is just a pile of tubes.
- The **system** (the named circuit) is a separate grouping object. If the exporter does not write it, "which ducts belong to Supply Air 1" cannot be answered.
- Flow, pressure and pipe size are properties with **units**, and the units are where most silent damage happens (litres per second turning into cubic feet per second, see below).

Real data is overwhelmingly English (GitHub trackers, the buildingSMART forum, the Autodesk MEP forum, OSArch). Native-language MEP questions in the data are sparse: a few Chinese, Japanese, Dutch, Spanish items; German, Russian, French, Italian, Portuguese and Korean appear mostly as synthetic prompts. This is a research gap, not proof that those users do not ask.

## Daily IFC tasks

| Task | What it looks like in practice | Typical programs | Example ids |
|---|---|---|---|
| Export the MEP model for coordination | Press Export so the coordinator can check clashes; hope colours, systems and sizes come through. | Revit MEP, MagiCAD, DDS-CAD, Allplan | `en-mcl-r001`, `en-mep-r001`, `ru-mep-s017`, `de-mep-s007` |
| Check that everything is in a system | List ducts / pipes / equipment not assigned to any system before the meeting. | IFC viewer + script, Solibri | `en-eng-s002`, `ru-mep-s005`, `es-spain-s010`, `ko-korea-s010` |
| Quantities by system | Total duct length per system, pipes by diameter and system, equipment counts. | Revit schedules, scripts | `en-reddit-s006`, `ja-japan-s007`, `fr-francophone-s007`, `pt-brazil-s008` |
| Penetrations / openings coordination | Find where services cross walls, slabs and beams; plan sleeves and holes; compare with architect and structure openings. | Revit, Navisworks, Solibri | `zh-revit-auto-r026`, `en-openings-r002`, `de-dach-s001`, `ja-openings-s017` |
| Receive and link the architect's IFC | See rooms/spaces to hang diffusers and equipment on; keep the link light. | Revit (Link IFC / Open IFC) | `en-autodesk-revit-import-r018`, `en-roundtrip-r004`, `ja-japan-r025` |
| Classify unusual parts | Decide which IFC class and type for a coupling, earthing rod, hanger, power supply. | forums, Revit mapping | `en-eng-r007`, `en-mep-r032`, `en-bsforum-r014`, `ja-mep-s012` |
| Feed energy / calculation tools | Space boundaries, HVAC design data on spaces. | BEM tools, EnergyPlus | `en-spaces-r006`, `en-eng-r013`, `pt-spaces-s014` |
| Compare revisions | "What moved or got resized since last week's model?" | scripts, Revit add-ins | `en-revit-auto-r025`, `en-revit-auto-s007`, `ru-mep-s017`, `ja-eng-s016` |

## Goals

- **Correct values after export**: right unit for flow, right material (the real pipe material, not the system name), right size on every segment (`en-eng-r003`, `en-eng-r015`, `en-ghrevitifc-r017`).
- **A connected, system-grouped network** that a coordinator can select by system and trace through ports (`en-eng-r016`, `en-mep-r023`, `en-eng-r017`, `en-mep-r020`).
- **Colours that mean something**: hot water red, cold blue, sewer green in the viewer; no mysterious grey (`en-mcl-r001`, `en-mcl-r024`, `en-mep-r014`, `zh-mep-s008`).
- **Control file size and export time**: insulation, flex duct, ports and fittings make files huge (`en-mep-r001`, `en-autodesk-revit-export-s012`).
- **Penetration list without manual hunting**: every duct or pipe that crosses a wall/beam, size of the hole, with or without an existing opening (`zh-revit-auto-r026`, `de-dach-s015`, `ko-openings-s018`).
- **Pass the client's rule set**: e.g. a Dutch NL-SfB code on every installation object (`nl-dutch-r014`, `nl-dutch-s013`).

## Pains (ranked)

Editorial ranking by how many independent real threads show the pain; several records often point at the same ticket, so the thread count is smaller than the record count.

| Rank | Pain | What the user says (paraphrase) | Evidence ids |
|---|---|---|---|
| 1 | **Material and colour wrong or grey.** Pipe material is exported as the *system* name, fittings lose colour, system colours do not reach the other program. | "pipes carry the system name, not PVC or copper" / "some pipes are grey, others coloured" / "hot water red in Revit, beige in ArchiCAD" | `en-eng-r015`, `en-mep-r003`, `en-mcl-r001`, `en-mcl-r003`, `en-mcl-r008`, `en-mcl-r024`, `en-mep-r013`, `en-mep-r014`, `zh-mep-s008` |
| 2 | **Units and scale of flow values.** | "flow in L/s is exported in ft3/s" / "air flow value is the wrong scale" / "can duct flow be m3/h and pipe flow l/s from one parameter?" | `en-eng-r003`, `en-eng-r018`, `en-eng-r019`, `en-gh-revit-ifc-r042`, `en-mep-r010`, `fr-mep-s011` |
| 3 | **Systems missing, empty or impossible to edit.** No system object, no properties on it, cannot override membership. | "tried user-defined psets, none appear on the system" / "override the distribution system of elements" / "why no reference to Systems (IfcDistributionSystem)?" | `en-eng-r016`, `en-ghrevitifc-r036`, `en-mep-r023`, `nl-dutch-r014`, `en-eng-s002`, `ru-mep-s005` |
| 4 | **Wrong class or type for MEP parts.** | "security devices export as proxies, electrical equipment fine" / "ducts and pipes show as generic types" / "best class for a reducing coupling" | `en-autodesk-revit-export-r003`, `en-autodesk-revit-export-r024`, `en-gh-proxy-r019`, `en-eng-r007`, `en-mep-r031`, `en-mep-r032`, `en-bsforum-r014` |
| 5 | **Ports lost or not connected.** | "ports are lost on library import" / "port property sets not available" / "expose open ports of a linked model" | `en-eng-r017`, `en-mep-r017`, `en-mep-r020`, `en-mep-r021`, `en-mep-r030`, `it-mep-s014`, `en-mep-s002` |
| 6 | **IfcSpace behaves badly when linked or exported.** Imported as generic models that obstruct views; shifted in position; boundaries displaced; many overlapping HVAC psets. | "we need IfcSpace to become a Room or MEP Space on Link IFC" / "spaces shifted and wrong height" | `en-autodesk-revit-import-r018`, `en-roundtrip-r004`, `en-spaces-r002`, `en-gh-revit-ifc-r025`, `en-spaces-r006`, `en-spaces-r030` |
| 7 | **Linked MEP IFC drops elements / becomes DirectShape generic models.** | "linking an MEP IFC drops many elements in 2023, log full of geometry validation errors" | `en-autodesk-revit-import-r006`, `en-roundtrip-r013`, `en-roundtrip-r008` |
| 8 | **Insulation merged into the pipe; no centre line; heavy files.** | "pipe and insulation come out as one IfcPipeSegment" / "need duct centre line to measure" / "600 MB because of flex duct" | `en-mep-r001`, `en-mep-r009`, `en-autodesk-revit-export-s012` |
| 9 | **Parameter mapping into psets is fiddly.** | "map width or height depending on which one exists" / "matched parameter name with the duct pset attribute" | `en-ghrevitifc-r014`, `en-ghrevitifc-r017`, `en-mep-r033` |
| 10 | **Penetration planning is manual.** | "AI should return candidate list by host, model, level, category" / "dedicated penetration tool, associative update when MEP moves" | `zh-revit-auto-r026`, `en-openings-r002`, `de-dach-s015` |

Cross-language finding: pains 1 to 5 are English-only in the real data; the same symptoms appear in synthetic Chinese, Portuguese, French and Italian prompts only because the research pass translated them, so treat non-English MEP phrasing as plausible, not observed.

## Vocabulary they use (and what they do not know)

| They say | Meaning for them | What they usually do not know / confuse |
|---|---|---|
| ОВиК / ВК / системы ОВ и ВК (ru); 暖通, 机电, 管线 (zh); TGA, Lüftungskanäle, Leitungen, Nennweite DN (de); 設備, ダクト, 配管 (ja); HVAC, plumbing, ductwork (en) | The trades and their runs | IFC class names (`IfcDuctSegment`, `IfcPipeFitting`, `IfcFlowTerminal`, `IfcDistributionSystem`). |
| "system", "system type", "Supply Air 1" | A named circuit | That in IFC the system is a *separate object* that elements are assigned to, and the exporter may not write it. |
| "fitting", "reducer", "coupling", "elbow", "tee" | Parts joining segments | That each needs a class and often a type (TRANSITION when sizes change, JUNCTION, BEND...). They pick by trade habit. |
| "flow", "Volumenstrom", "расход", "L/s", "m3/h" | Design flow of air or water | That IFC stores one fixed internal unit for volumetric flow and the displayed unit is a conversion (`en-eng-r003`). |
| "clash", "collision", "коллизия", "干渉", "碰撞" | A pipe hitting a beam | That many "clashes" are really *missing sleeves* (openings), a coordination item, not a model error. |
| "sleeve / гильза / 套管 / Hülse / スリーブ" | Pipe through a wall | How sleeves/openings are represented (void + filling) or that they may be absent. |
| "Space" vs "Room" | Revit uses *Spaces* (MEP) and *Rooms* (architecture) | That IFC has only `IfcSpace`, and the importing program decides what it becomes (`en-autodesk-revit-import-r018`). |
| "magicad", "DDS-CAD", "Revit MEP export" | Source tools | That each writes a different structure of ports, systems and psets (`ru-mep-s017`, `it-mep-s014`, `de-mep-s007`). |

Plain-language bridge: tell the non-BIM tester to picture a pipe network drawn on paper. IFC can store (a) each pipe piece, (b) which circuit it belongs to, (c) which neighbours it touches. The MEP persona mostly cares about (b) and (c) and about numbers on (a), and notices only when one of the three is missing. Background: [domains overview](../../01_ifc_basics/08_domains_mep_structural_infra_4d5d_fm.md), [spatial structure and relationships](../../01_ifc_basics/04_spatial_structure_and_relationships.md), [properties and quantities](../../01_ifc_basics/05_properties_quantities_psets.md), [Revit export reference](../../03_software/revit/ifc_export_reference.md), [Revit import/link reference](../../03_software/revit/ifc_import_link_reference.md), [glossary](../../08_glossary/glossary_multilingual.md).

## Real questions

55 real questions, grouped loosely by theme (material/colour, units, systems, class choice, ports, spaces, linking, insulation and size, mapping, openings, plus a few automation and non-English items). Language mix: en 50, zh 2, nl 1, ja 1, es 1. The "Question" column is the research pass's **paraphrase** of the source post (not a verbatim quote); the English gloss appears only for non-English rows. Where the source was title-only, the paraphrase is short and the outcome says so.

| # | ID | Lang | Question (paraphrase, original language) | English gloss | Outcome in source | Source |
|---|---|---|---|---|---|---|
| 1 | `en-eng-r015` | en | Pipe material exported as system name; unreliable since one system has mixed materials. | — | Designed per user demand; tracked internally REVIT-236144, open. | [GitHub #577](https://github.com/Autodesk/revit-ifc/issues/577) |
| 2 | `en-mep-r003` | en | pipes carry system material name rather than real material; some systems mix PVC and HDPE; how to export actual material | — | Behaviour was demanded for colours; suggested use system material as style and real material as material. | [GitHub #577](https://github.com/Autodesk/revit-ifc/issues/577) |
| 3 | `en-mcl-r001` | en | some pipes/ducts are grey in the exported IFC, others coloured; is the MVD (2x2 Coordination View) unable to carry system colours? | — | Colours from view filters/graphic overrides are view-specific and not exported; set colour on the Material itself, update exporter, use 2x3 CV2.0 or IFC4 RV. | [GitHub #579](https://github.com/Autodesk/revit-ifc/issues/579) |
| 4 | `en-mcl-r024` | en | hot water red/cold blue/sewage green in Revit become beige/blue/blue in ArchiCAD; tried IfcPresentationLayer | — | No direct answer; Revit colour/material export is a known weakness; asks for the file. | [forums.buildingsmart.org](https://forums.buildingsmart.org/t/how-can-i-control-the-ifc-pipes-colors-revit-to-archicad/2729) |
| 5 | `en-mcl-r025` | en | pipe-diameter colours exported from Allplan disappear in other apps but show in a viewer | — | Material is only a name; colour needs IfcSurfaceStyle via styled representation; Allplan attached style to the shape; 428 duplicate materials. | [forums.buildingsmart.org](https://forums.buildingsmart.org/t/where-and-how-will-my-colors-be-saved-in-ifc/1806) |
| 6 | `en-mep-r013` | en | fittings lose system colour in IFC | — | Reproduced again in 2021 with attached model. | [GitHub #112](https://github.com/Autodesk/revit-ifc/issues/112) |
| 7 | `en-mep-r014` | en | one duct type used for Supply and Return, colours by system, but fittings export wrong | — | Asked for versions. | [GitHub #373](https://github.com/Autodesk/revit-ifc/issues/373) |
| 8 | `en-autodesk-revit-export-r025` | en | Duct fitting material disappears in IFC. | — | Workaround: IfcSingleMaterialOverride parameter in IFC group naming a material. | [forums.autodesk.com](https://forums.autodesk.com/t5/revit-mep-forum/losing-duct-fitting-material-when-exported-to-ifc-files/td-p/8736337) |
| 9 | `en-eng-r003` | en | IFC VolumetricFlowRate is m3/s; user wants duct flow in m3/h and pipe flow in l/s though both use the same parameter name. | — | Units are a display matter; Revit stores internal units; exporter offers only one flow data type. | [forums.buildingsmart.org](https://forums.buildingsmart.org/t/supported-data-type-volumetricflowrate-m-h/4189) |
| 10 | `en-eng-r018` | en | Tested base quantities, custom pset, volumetricFlowRate; all wrong units. | — | Maintainers analysed file; unit scaling issue. | [GitHub #444](https://github.com/Autodesk/revit-ifc/issues/444) |
| 11 | `en-eng-r019` | en | Air Flow value in IFC wrong scale; project upgrading and relies on fix. | — | L/s bug; workaround change display unit. | [GitHub #237](https://github.com/Autodesk/revit-ifc/issues/237) |
| 12 | `en-gh-revit-ifc-r042` | en | Flow in L/s is exported in ft3/s. | — | Value written as volumetric flow in IFC unit definition. | [GitHub #444](https://github.com/Autodesk/revit-ifc/issues/444) |
| 13 | `en-eng-r016` | en | Tried user-defined psets but none appear on IfcSystem. | — | Maintainers first called it by-design limitation, later revised. | [GitHub #523](https://github.com/Autodesk/revit-ifc/issues/523) |
| 14 | `en-ghrevitifc-r036` | en | Override IfcDistributionSystem of elements | — | Snippet only. | [GitHub #900](https://github.com/Autodesk/revit-ifc/issues/900) |
| 15 | `en-mep-r023` | en | project with many MEP systems and subsystems, cannot nest in UI | — | Open feature request. | [GitHub #7062](https://github.com/IfcOpenShell/IfcOpenShell/issues/7062) |
| 16 | `nl-dutch-r014` | nl | Waarom geen verwijzing naar Systems (IfcDistributionSystem)? NL/SfB-codes sluiten niet geheel aan op de praktijk; is classificeren op NL-SfB echt de bedoeling? | Why no reference to IfcDistributionSystem; NL-SfB codes do not fully match practice for installations - is NL-SfB really the intent? | digiGO: NL-SfB chosen on Techniek NL advice, starting point; mapping to IfcDistributionSystem should be possible. | [GitHub #52](https://github.com/nl-digigo/imwo/issues/52) |
| 17 | `en-autodesk-revit-export-r003` | en | Security devices export as proxies while electrical equipment exports correctly. | — | Replies: check per-category IFC class in export options, and use the interoperability tools to set IFC class. | [forums.autodesk.com](https://forums.autodesk.com/t5/revit-mep-forum/ifc-export-issue/m-p/12250648) |
| 18 | `en-autodesk-revit-export-r024` | en | Ducts and pipes show as generic types after export. | — | In 2x3 only IfcFlowSegment; IfcDuctSegment/IfcPipeSegment exist from IFC4; use IfcExportAs to force class. | [forums.autodesk.com](https://forums.autodesk.com/t5/revit-mep-forum/ifc-export-ducts-and-pipes/td-p/12370919) |
| 19 | `en-gh-proxy-r019` | en | IfcExportAs=IfcFlowMeterType and IfcExportType=WATERMETER exports class correctly but PredefinedType NOTDEFINED; same for IfcValveType PRESSUREREDUCING. | — | Maintainer asked for a minimal sample; WaterMeter exists in code. | [GitHub #525](https://github.com/Autodesk/revit-ifc/issues/525) |
| 20 | `en-eng-r007` | en | PVC reducing coupling joins different pipe sizes; CONNECTOR for couplings, but two different ports suggest TRANSITION. | — | TRANSITION when nominal diameter changes; MagiCAD does the same for ventilation and piping. | [forums.buildingsmart.org](https://forums.buildingsmart.org/t/best-ifc-classification-for-a-reducing-coupling/5963) |
| 21 | `en-mep-r032` | en | no obvious class for grounding rod | — | IfcCableSegment or ProtectiveDevice; IfcEarthingElement planned in 4.4; or USERDEFINED GROUNDINGROD. | [forums.buildingsmart.org](https://forums.buildingsmart.org/t/ifc-class-for-earthing-rod/5632) |
| 22 | `en-bsforum-r014` | en | wants to model an AC-DC power supply with rectifier, battery and controller as sub-parts; no single IFC class so considers IfcTransformer, IfcElectricFlowStorageDevice, IfcController with ports and IfcRelNests | — | Compose the device from several classes with nesting/aggregation and ports; there is no dedicated composite class. | [forums.buildingsmart.org](https://forums.buildingsmart.org/t/5016) |
| 23 | `en-bsforum-r042` | en | how to model a reserved clearance volume for equipment movement or servicing; is IfcSpatialZone RESERVATION right? | — | IfcVirtualElement CLEARANCE linked via IfcRelAssignsToProduct. | [forums.buildingsmart.org](https://forums.buildingsmart.org/t/6528) |
| 24 | `en-gh-revit-ifc-r056` | en | One alarm type with 10 instances exports as 3 IFC types. | — | REVIT-237057. | [GitHub #809](https://github.com/Autodesk/revit-ifc/issues/809) |
| 25 | `en-eng-r017` | en | Heater-to-port relation changed in IFC4; asks how Revit does dynamic port connection. | — | Clarified IfcRelNests vs IfcRelConnectsPortToElement. | [GitHub #162](https://github.com/Autodesk/revit-ifc/issues/162) |
| 26 | `en-mep-r017` | en | port property sets from the IFC spec not available | — | Logged REVIT-249225, open. | [GitHub #188](https://github.com/Autodesk/revit-ifc/issues/188) |
| 27 | `en-mep-r020` | en | expose open ports of a linked model to connect different MEP systems | — | Discussion with related port import request. | [GitHub #7496](https://github.com/IfcOpenShell/IfcOpenShell/issues/7496) |
| 28 | `en-mep-r021` | en | ports are lost when importing MEP types from a project library | — | PR 7543 implements it. | [GitHub #6687](https://github.com/IfcOpenShell/IfcOpenShell/issues/6687) |
| 29 | `en-eng-r020` | en | Asks when Revit export will be IFC4 MEP certified. | — | Progress shared; certification (IFC4 RV1.2) finished 2022-04-27. | [GitHub #357](https://github.com/Autodesk/revit-ifc/issues/357) |
| 30 | `en-autodesk-revit-import-r018` | en | Wants IfcSpace converted to Rooms (architectural link) or Spaces (MEP link). | — | Open enhancement. | [GitHub #15](https://github.com/Autodesk/revit-ifc/issues/15) |
| 31 | `en-roundtrip-r004` | en | IfcSpace imported as generic models obstructs views; MEP engineers must use Open IFC just to get Rooms. | — | Maintainer asked how to decide Room vs Space; open since 2018. | [GitHub #15](https://github.com/Autodesk/revit-ifc/issues/15) |
| 32 | `en-gh-revit-ifc-r025` | en | Spaces are shifted in position and wrong in height across three MEP models, compared with 25.4.20.11. | — | 29 comments; sample provided in reduced form. | [GitHub #924](https://github.com/Autodesk/revit-ifc/issues/924) |
| 33 | `en-spaces-r006` | en | with SpaceBoundaries=2 the IfcRelSpaceBoundary2ndLevel geometry is shifted several metres in XY from the IfcSpace, breaking BEM workflows | — | Open as REVIT-248675. | [GitHub #961](https://github.com/Autodesk/revit-ifc/issues/961) |
| 34 | `en-eng-r013` | en | HVAC-relevant space data (thermal design) and intermediate calculated results in IfcSpace psets. | — | Not in snippet. | [forums.buildingsmart.org](https://forums.buildingsmart.org/t/propertysets-of-ifcspace/3997) |
| 35 | `en-spaces-r036` | en | contain cables and equipment in IfcSpace via IfcRelContainedInSpatialStructure | — | Participants agreed it is possible. | [community.osarch.org #3316](https://community.osarch.org/discussion/3316/ifcspace-good-for-spatial-containment-of-ifcdistributionelements) |
| 36 | `en-autodesk-revit-import-r006` | en | Linking an MEP IFC drops many elements in 2023; log full of pGeomArr validation errors; model only about 70 m from the origin. | — | Suspected far-from-origin geometry validation issue; maintainer asked about distance. | [GitHub #658](https://github.com/Autodesk/revit-ifc/issues/658) |
| 37 | `en-roundtrip-r008` | en | Link IFC maps several MEP types to Generic Model despite a custom mapping table; asks why hardcoded since all become DirectShapes. | — | Autodesk: a regression in the mapping table for Link IFC, believed fixed. | [GitHub #803](https://github.com/Autodesk/revit-ifc/issues/803) |
| 38 | `ja-japan-r025` | ja | Jw_cadで2D図面。元請から意匠IFCを受けて設備ルートを3D確認したい。ソフトを買う根拠がない | Small MEP office on Jw_cad: how to prepare for BIM cheaply, view architect IFC for free | Learn, view IFC free, trial on small area, buy later; verify round-trip conversion before delivery. | [note.com](https://note.com/limber_stork5044/n/n68df8d5a268b) |
| 39 | `en-mep-r001` | en | pipe and duct plus their insulation come out as a single IfcPipeSegment/IfcDuctSegment in IFC4 | — | Maintainers asked for Revit and exporter versions; no fix in thread. | [GitHub #416](https://github.com/Autodesk/revit-ifc/issues/416) |
| 40 | `en-mep-r009` | en | need duct/pipe centre line in export to measure length between centre lines and axes/walls | — | Maintainer answer unclear to later commenters; no solution. | [GitHub #33](https://github.com/Autodesk/revit-ifc/issues/33) |
| 41 | `en-ghrevitifc-r014` | en | I did not find how to map 2 different parameters depending of which one is available in the object to the same pset property. Duct width and height for rectangular, diameter for round. | — | No answer in thread at time of reading. | [GitHub #303](https://github.com/Autodesk/revit-ifc/issues/303) |
| 42 | `en-ghrevitifc-r017` | en | I'm trying to use the following export mapping to have the nominal dimensions of pipe and duct segments in the appropriate psets, as per the Autodesk IFC Handbook. Unfortunately this doesn't work. | — | Unanswered. | [GitHub #889](https://github.com/Autodesk/revit-ifc/issues/889) |
| 43 | `en-mep-r033` | en | new to IFC, matched parameter name with duct pset attribute | — | No confirmed fix; pointed to Autodesk support. | [forums.buildingsmart.org](https://forums.buildingsmart.org/t/ifc-mapping-in-revit-mep/4591) |
| 44 | `en-eng-r031` | en | Angled pipes invisible in viewer. | — | Likely fixed in latest. | [GitHub #1974](https://github.com/ThatOpen/engine_web-ifc/issues/1974) |
| 45 | `zh-revit-auto-r026` | zh | 機電管線穿過牆、樓板或樑時要逐筆確認穿透位置與開孔大小;希望AI能指定MEP/結構在主模型或連結模型、預留量、樓層與品類,回傳候選清單 | Turn the manual MEP-penetration opening-locating workflow into AI-callable tools that scan pipes crossing walls/floors/beams and propose opening sizes | Implemented as read-only scan_opening_candidates with candidate/review_required states and 7 warning codes; no default clearance. | [GitHub #99](https://github.com/shuotao/REVIT_MCP_study/issues/99) |
| 46 | `en-openings-r002` | en | Dedicated penetration tool: host-aware placement, associative update when MEP moves, clearance offsets, batch from clash scan, metadata like fire rating and sealing. | — | Closed; related work on openings API tracked separately. | [GitHub #8037](https://github.com/IfcOpenShell/IfcOpenShell/issues/8037) |
| 47 | `en-revit-auto-r025` | en | standard compare tools match by ElementId so independent models look entirely different; tool matches ducts/pipes by endpoints and creates a section-boxed 3D view per issue | — | Classifies match/offset/moved/wrong size/missing/extra; no replies. | [discourse.pyrevitlabs.io](https://discourse.pyrevitlabs.io/t/revit-model-compare-check-what-the-ai-actually-built/10681) |
| 48 | `en-revit-auto-r011` | en | want total data ports per floor to size telecom racks; the family stores port count in a parameter but every attempt returns null; ChatGPT and Gemini didn't help | — | Check type vs instance parameter, storage type, drop quotes in String node; a schedule may be simpler. | [forum.dynamobim.com](https://forum.dynamobim.com/t/extracting-telecom-data-port-quantities-from-bim-model-using-dynamo/114169) |
| 49 | `en-revit-auto-r013` | en | can Dynamo fill a cable tray with multiple cables from inside width/height and cable diameter, compute rows, create cable paths | — | Use tray curves, conduits without fittings then NewElbowFitting; Python sample for one layer. | [forum.dynamobim.com](https://forum.dynamobim.com/t/automatically-fill-cable-tray-with-cables/115192) |
| 50 | `en-revit-auto-r016` | en | new Dynamo user; large warehouses with conveyors and platforms; can Dynamo calculate egress distance from any point on a platform to nearest ground-floor exit; any generic script | — | Use VASA package voxel pathfinding; clarify point-to-exit vs find-areas-too-far. | [forum.dynamobim.com](https://forum.dynamobim.com/t/exit-access-travel-distance/115179) |
| 51 | `en-aimcp-r020` | en | list all pipes in the revit model -> Get element information failed: Method not found | — | Registry mismatch between server and plugin versions; reply suggested aligning them. | [GitHub #28](https://github.com/mcp-servers-for-revit/revit-mcp/issues/28) |
| 52 | `es-latam-r003` | es | integración con herramientas BIM: mapeo de conductores calculados a entidades, generar IFC con propiedades eléctricas, endpoint export/ifc | Export electrical calculation results as DXF/IFC with electrical properties for Revit and AutoCAD | Planned work items only: investigate ezdxf, map conductors to entities, generate IFC with electrical Psets, REST endpoints. | [GitHub #10](https://github.com/jmarinderko/calculadora-RIC/issues/10) |
| 53 | `zh-revit-export-r012` | zh | 机电模型从Revit出IFC再导进BIM5D的步骤 | Process of exporting Revit MEP model as IFC and importing into BIM5D. | Export > IFC from Revit, then import IFC into Glodon BIM5D. | [zhulong.com](https://www.zhulong.com/zt_bim_3002296/detail40283815/) |
| 54 | `en-us-canada-infra-r028` | en | COBie data export problem in Revit MEP. | — | Not read. | [forums.autodesk.com](https://forums.autodesk.com/t5/revit-mep-forum/revit-mep-cobie-data-export-issue/td-p/11566679) |
| 55 | `en-val-r010` | en | Pset_SoundGeneration SoundCurve is IfcPropertyTableValue with two measure types | — | Write two requirements (one per column type); Audit tool wrongly reports no allowed data types, raised as GitHub issue. | [forums.buildingsmart.org](https://forums.buildingsmart.org/t/specifying-data-type-for-table-value-with-multiple-data-types/5740) |

## Ready test prompts

45 prompts for an MCP server or assistant connected to an IFC (or a Revit session). **All are synthetic**: written for testing, modelled on the real records in the data files, never real quotes. Russian and English get the most rows. The "What a good answer does" column is the research pass's expected behavior for the judge. Row language is in the "Lang" column; the id prefix is only the research-cell label.

| # | ID | Lang | Prompt (synthetic, as the user would type it) | File needed | Difficulty | What a good answer does |
|---|---|---|---|---|---|---|
| 1 | `en-aimcp-s006` | en | list all pipes in the model with system type and diameter | yes | medium | Query pipes, group by system type, return diameters; do not loop on failed methods. |
| 2 | `en-eng-s001` | en | list all IfcDuctSegments with airflow prop, units look off, is it m3/s or ft3/s | yes | medium | Query IfcDuctSegment, read flow properties, inspect project unit assignments, report values and likely scale issue. |
| 3 | `en-eng-s002` | en | which pipes and fittings arent in any IfcSystem? need before coord meeting | yes | medium | Find IfcFlowSegment/IfcFlowFitting without group assignment to an IfcSystem; list with names and levels. |
| 4 | `en-eng-s003` | en | pipes show material = system name (HOT WATER) not copper. can you list pipes and what material they actually have | yes | medium | Read material associations for IfcPipeSegment, list names, point out system-name materials, suggest where real material may be in psets. |
| 5 | `en-eng-s008` | en | set predefined type TRANSITION on all reducer pipe fittings | yes | medium | Find IfcPipeFitting with different port diameters, set PredefinedType TRANSITION, report changes. |
| 6 | `en-mep-s002` | en | which ducts and fittings have ports with no IfcRelConnectsPorts? need the open ends for the coord meeting | yes | hard | Collect IfcDistributionPort via IsNestedBy, check ConnectedTo/ConnectedFrom, list parent element, system, level and port flow direction for open ones. |
| 7 | `en-revit-auto-s007` | en | compare the ducts in this model with the linked old coordination model, what moved or got resized | yes | hard | Match ducts by endpoints, classify moved/resized/missing/new, give counts and an element list per class. |
| 8 | `en-allplan-vw-bentley-s012` | en | are all ducts in a system? list orphans | no | medium | Check IfcRelAssignsToGroup/IfcSystem membership for IfcDuctSegment, list orphans. |
| 9 | `en-autodesk-revit-export-s008` | en | what IFC classes are my ducts and pipes, flowsegment or proxy? also fittings | yes | easy | Group MEP elements by class and predefined type; flag proxies. |
| 10 | `en-autodesk-revit-export-s012` | en | ifc export of mep model is 600mb because of flex duct, how to reduce | no | easy | Suggest LOD, view-based export, exclude flex duct, zip. |
| 11 | `en-autodesk-revit-import-s005` | en | find all IfcFlowSegment that are not duct or pipe segments, hvac model from consultant | yes | medium | Filter IfcFlowSegment, group by predefined type and system, suggest Revit category mapping. |
| 12 | `en-bsforum-s013` | en | add a clearance volume IfcVirtualElement CLEARANCE around pump P-101 and assign it to the pump | yes | hard | Create the virtual element and an IfcRelAssignsToProduct link; keep containment consistent |
| 13 | `en-gh-revit-ifc-s006` | en | pipes and ducts - whats their material, real material or the system name? | yes | medium | Inspect IfcMaterial assignments on IfcPipeSegment/IfcDuctSegment, report if material equals system name vs real material. |
| 14 | `en-reddit-s006` | en | total duct length per system name in the mech model | yes | medium | Group IfcDuctSegment by IfcSystem membership, sum lengths from quantities or geometry. |
| 15 | `en-psets-s011` | en | do ducts have NominalDiameterOrWidth and NominalHeight in Pset_DuctSegmentTypeCommon? show those missing | yes | medium | Inspect IfcDuctSegment type psets, list segments lacking the properties. |
| 16 | `en-spaces-s003` | en | do we have IfcRelSpaceBoundary2ndLevel in this file? how many per space, any space with zero | yes | medium | Count boundaries per IfcSpace, flag spaces with none, report level (1st/2nd). |
| 17 | `en-openings-s003` | en | need list of ducts and pipes that go thru fire rated walls but have no opening, pls export as bcf | yes | hard | Clash MEP segments vs walls with FireRating, exclude those already inside an IfcOpeningElement, export issues as BCF with GlobalIds and viewpoints. |
| 18 | `mx-mcl-s011` | en | do the pipes have the real material (PVC/copper) or just the system material name like SEWER? list by system | yes | medium | Read IfcRelAssociatesMaterial for IfcPipeSegment/fittings, compare with system names, report mismatches. |
| 19 | `en-dynamo-pyrevit-s014` | en | give me all IfcSystem and their members count | yes | medium | Query IfcSystem and IfcRelAssignsToGroup. |
| 20 | `ru-eng-s009` | ru | посчитай длину воздуховодов по системам, в ифс они в IfcSystem вроде *(EN: Group ducts by system and total length)* | yes | medium | Group IfcDuctSegment by IfcSystem and sum lengths, report table, note missing system links. |
| 21 | `ru-autodesk-telegram-s018` | ru | покажи системы ОВ и ВК из ифс, какие сегменты не привязаны ни к одной системе *(EN: List duct and pipe systems and unconnected segments)* | yes | medium | List IfcSystem/IfcDistributionSystem with members, find IfcDistributionElement without system assignment, group by class. |
| 22 | `ru-dwg-revit-s010` | ru | у труб в модели есть имя системы и диаметр? выдай список без них *(EN: Check pipes have system names and diameters)* | yes | medium | Iterate IfcPipeSegment, check system assignment and NominalDiameter, list elements lacking them. |
| 23 | `ru-renga-nanocad-s009` | ru | выдай трубы и воздуховоды по системам, с диаметрами *(EN: List pipe and duct segments grouped by system name)* | yes | medium | Find IfcPipeSegment/IfcDuctSegment, group by system via IfcRelAssignsToGroup/IfcSystem, report diameters from psets. |
| 24 | `ru-tim-expertiza-s013` | ru | какие инженерные элементы не входят ни в одну систему, список с уровнями *(EN: List MEP elements not assigned to any system)* | yes | medium | Find flow segments/fittings/terminals with no IfcRelAssignsToGroup/IfcSystem, list by storey. |
| 25 | `ru-mep-s005` | ru | покажи воздуховоды и трубы которые не входят ни в одну систему, ифс из ревита, нужно до сдачи *(EN: Which elements are not in any system)* | yes | medium | Find IfcDuctSegment/IfcPipeSegment/fittings without IfcRelAssignsToGroup to IfcDistributionSystem; list with level and Revit Id. |
| 26 | `ru-mep-s017` | ru | сравни две выгрузки из магикад, что поменялось в системах и трассах *(EN: Compare two MEP exports)* | yes | hard | Diff by GlobalId and system membership, report added/removed/changed elements. |
| 27 | `zh-revit-auto-s011` | zh | 幫我掃一下水管穿樑的位置,列出每個穿透點需要的套管口徑,預留每邊30mm *(EN: Scan pipes crossing beams and list needed sleeve sizes)* | yes | hard | Find pipe-vs-StructuralFraming intersections, compute diameter + 2*30 mm, flag oblique or beam penetrations for review, read-only. |
| 28 | `zh-eng-s012` | zh | 机电管线和结构梁碰撞结果导出成bcf，按楼层分组 *(EN: Export clashes between pipes and structure as BCF)* | yes | hard | Run clash, group by storey, export BCF. |
| 29 | `zh-mep-s008` | zh | revit导出ifc后管道颜色都是灰的，系统颜色没带出来，用的哪个设置？ *(EN: MEP colours lost in IFC)* | no | medium | Explain colour derives from materials/by-category, not view filters; guide setting system material and checking IfcStyledItem. |
| 30 | `zh-openings-s012` | zh | 帮我查一下管线穿梁穿墙的位置，哪些还没开洞，导出预留洞清单 *(EN: Find pipes through beams/walls needing reserved holes)* | yes | hard | Find MEP-structure intersections without openings, export reserved-hole list with size and location. |
| 31 | `de-dach-s001` | de | zeig mir alle Wanddurchbrüche im Arch-Modell, wo keine TGA-Leitung durchgeht. brauch ich für die Durchbruchsplanung morgen *(EN: List all openings in walls from the architect model that have no matching MEP penetration.)* | yes | hard | Find IfcOpeningElement in walls, intersect with MEP element geometry from the linked model, list openings without crossing element with ids, storey, size. |
| 32 | `de-dach-s009` | de | welche Lüftungskanäle > 300 mm durchdringen F90 Wände? mit Geschoss und Position *(EN: List all ducts larger than 300 mm passing through fire walls.)* | yes | hard | Find ducts, intersect with walls whose FireRating is F90, list size, storey, location. |
| 33 | `de-dach-s015` | de | mach mir aus den Kollisionen Rohr/Wand ein BCF mit Position und Bauteil-GUID, Durchbruch fehlt *(EN: Create BCF for missing wall penetrations.)* | yes | hard | Compute pipe-wall intersections lacking openings, produce BCF issues with viewpoint and GUIDs. |
| 34 | `de-mep-s007` | de | gib mir alle Rohre mit DN und Volumenstrom aus dem Pset, MagiCAD Export, als Liste pro Gewerk *(EN: Nominal diameter and flow for all pipes)* | yes | medium | Read IfcPipeSegment psets (Pset_PipeSegmentTypeCommon, vendor psets), return NominalDiameter and flow, grouped by system; note missing values. |
| 35 | `de-openings-s007` | de | zeig mir alle Leitungen TGA die durch Wände/Decken gehen und noch keinen Durchbruch haben, DN und Wandstärke dazu *(EN: Find all TGA pipes through walls that have no Aussparung/Durchbruch yet)* | yes | hard | Intersect MEP segments with walls/slabs, subtract existing openings, output diameter/size and host thickness table. |
| 36 | `es-latam-s012` | es | qué sistemas de tuberías hay en el modelo y cuáles tubos no están conectados a ningún sistema? *(EN: List piping systems and check segments with no system)* | yes | medium | List IfcSystem/IfcDistributionSystem membership, find IfcPipeSegment without system, report counts. |
| 37 | `fr-mep-s011` | fr | verifie les unites des debits sur les gaines, j'ai l'impression que c'est en ft3/s au lieu de L/s *(EN: Check units of flow)* | yes | medium | Inspect IfcUnitAssignment and flow property units, report discrepancies, convert values. |
| 38 | `ja-mep-s012` | ja | Revitの吊りボルトとサポートをIFCに出したいけど、クラスはどれが正解？ *(EN: Export hangers and supports)* | no | medium | Recommend IfcDiscreteAccessory (or IfcPipeSegment-adjacent support classes) via export class mapping, avoiding IfcBuildingElementProxy; explain how to set IfcExportAs on the family. |
| 39 | `ja-japan-s007` | ja | 設備IFCの空調ダクトをシステム名別・階別に本数と合計長さでまとめて *(EN: List ducts per system and their storey)* | yes | medium | Collect IfcDuctSegment, group by IfcSystem membership and containing storey, sum Length quantity, report ungrouped. |
| 40 | `ko-openings-s018` | ko | 배관이 벽 관통하는데 슬리브 안 들어간 곳 뽑아줘 *(EN: List walls penetrated by pipes needing sleeves)* | yes | medium | Find pipe-wall crossings with no sleeve/opening, list. |
| 41 | `it-mep-s014` | it | controlla se le porte dei raccordi hanno FlowDirection SOURCE/SINK coerente con il flusso, export DDS-CAD *(EN: Check port flow directions)* | yes | hard | Read IfcDistributionPort FlowDirection and connections, flag SOURCE-SOURCE or SINK-SINK connected pairs. |
| 42 | `pt-mep-s010` | pt | as conexoes estao vindo como proxy, muda tudo pra IfcPipeFitting e poe o tipo TRANSITION nas reducoes *(EN: Fix pipe fittings classes)* | yes | hard | Identify proxies named as fittings, change class, set PredefinedType by port-size change, report changes. |
| 43 | `pt-openings-s015` | pt | lista os furos nas lajes pra passagem de shafts e prumadas, tem algum sem abertura? *(EN: List slab holes for shafts and risers)* | yes | medium | Find vertical MEP risers crossing slabs without IfcOpeningElement. |
| 44 | `nl-dutch-s013` | nl | welke installatieobjecten zitten niet in een IfcSystem? en hebben ze NL-SfB 5x codes? *(EN: MEP objects without IfcSystem)* | yes | medium | List MEP elements w/o system assignment and classification. |
| 45 | `no-norway-s007` | no | list opp alle ventilasjonssystemer og antall kanaler i hvert system *(EN: List ventilation systems and the number of ducts per system)* | yes | easy | Query IfcSystem/IfcDistributionSystem and assigned duct segments, count per system. |

## How to role-play this persona in tests

**Voice.** Practical and time-boxed. Writes like a person preparing for a coordination meeting ("before the meeting", "до сдачи", "morgen"). Uses trade words, not IFC classes: "воздуховоды", "Rohre", "管道", "ductos", "pipes and fittings". Lists and counts first, explanations second. Fragments are normal: *"which pipes and fittings arent in any IfcSystem? need before coord meeting"* (`en-eng-s002`), *"ifc из ревита, нужно до сдачи"* (`ru-mep-s005`), *"revit导出ifc后管道颜色都是灰的"* (`zh-mep-s008`). Typos and missing capitals are fine; polite closers appear in forum style ("Thanks.").

**Typical context.**
- A Revit MEP or MagiCAD / DDS-CAD export (named in the prompt about a third of the time), IFC2x3 or IFC4 not stated unless the persona already got burnt.
- A deadline (coordination meeting tomorrow, handover), and a specific consumer of the answer: coordinator, architect, structural engineer, contractor.
- Usually `needs_file = true`; a few "how do I" questions need no file (`ja-mep-s012` hanger class, `en-eng-r007` coupling class).

**Knowledge level.**
- Strong: system design, sizing, flow and pressure, trade standards, their authoring tool (Revit MEP, MagiCAD, DDS-CAD).
- Medium: knows "systems" and "ports" in their own tool and expects them in the IFC too.
- Weak: IFC schema, class and PredefinedType names, the idea that units are stored in the file separately from the values, difference between instance and type properties, MVD/view names.
- Habit: judges the answer by whether it *matches what the authoring program shows*. If the assistant reports 0 systems while Revit shows 12, the persona says "it's wrong".

**What to test with this persona.**
- Honest absence: the file really has no systems or no ports. A good assistant says so and does not invent groups from names.
- Units: ask for flow and then challenge "is it m3/s or ft3/s" (`en-eng-s001`, `fr-mep-s011`). A good assistant reads the unit assignment in the file and shows the raw and converted value.
- Real material vs system name (`en-eng-s003`, `mx-mcl-s011`).
- Counts per system / per level with orphans listed separately.
- Safe edits only on request: "set predefined type TRANSITION on reducers" (`en-eng-s008`) needs a confirmation of scope and saving to a new file.
- Language switching: the same request in ru / de / zh / pt / ja should give the same factual answer.

**Typical follow-ups.**
1. "Только вентиляция, первый этаж" / "only supply air, level 1".
2. "Дай как bcf / export this as a BCF" (clash issues to the coordinator; see `de-dach-s015`, `zh-eng-s012`).
3. "Is that my Revit export setting or is the model wrong?"
4. "Which IFC class should a reducer be?" (expects a plain answer, with the caveat that the receiving tool decides).
5. "Сравни с прошлой выгрузкой" / "compare with last export, only ducts and pipes" (`ja-eng-s016`).
6. "Put the result in a table / Excel."
7. Mild frustration after a wrong answer: "no, Revit shows 12 systems" (expects a re-check, not repetition).

**Quick judge checklist.**
- Did the answer distinguish *segments*, *fittings*, *terminals*, *equipment*, and *systems*, and report each count?
- Are units and their source stated for every flow or size value?
- Are orphans (not in a system, not connected, no level) listed, not just counted?
- Is anything claimed about the Revit export (version, checkbox) that the assistant could not have seen? That is a fail.
