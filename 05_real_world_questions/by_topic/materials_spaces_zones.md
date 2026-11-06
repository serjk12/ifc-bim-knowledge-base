# Materials, colours, layers; spaces, rooms, areas, zones, systems

Topics covered (KB vocabulary): `materials_colors_styles`, `layers_presentation`, `spaces_rooms_areas`, `zones_groups_systems`.
Data basis (wave 1): `materials_colors_styles` 159 records (104 real, 55 synthetic), `layers_presentation` 46 (32 real, 14 synthetic), `spaces_rooms_areas` 165 (91 real, 74 synthetic), `zones_groups_systems` 46 (24 real, 22 synthetic). Records can carry several topics, so the sets overlap. The "question" text below is the knowledge base's paraphrase of the asker's post (kept in the original language where the record has one), not a verbatim quote. Synthetic prompts are labelled as such and are never real quotes.

Note on the label `layers_presentation`: it mixes two different things. About a third of its records are about IFC presentation layers (CAD-style layers) and layer export; the rest are about drawings, views, sheets and crop regions (mostly Revit automation via Dynamo/pyRevit and Bonsai 2D drawings). They are treated separately below.

## In plain words

**Materials and colours.** In IFC an `IfcMaterial` is only a name (for example "Concrete C30/37") plus optional properties; it does not carry a colour. The colour you see in a viewer comes from a separate "style" object (`IfcSurfaceStyle`) that must be attached either to the shape of the element or to the material. If the exporter writes no style, or the viewer looks in a different place than the exporter wrote it, everything shows grey or white, even though the file is "fine". Layered walls (gypsum, insulation, brick) are stored as a material layer set, but some IFC variants store them differently, and some viewers only understand one form. See [materials, styles, types](../../01_ifc_basics/07_materials_classification_types_styles.md) and [Revit IFC export reference](../../03_software/revit/ifc_export_reference.md).

**Layers.** "Layer" means three different things people confuse: a wall's material layers, CAD-style presentation layers (`IfcPresentationLayerAssignment`, used for DWG/DXF layer names), and Revit's own view/sheet organisation. The last one is not stored in IFC at all.

**Spaces, rooms, areas, zones, systems.** A room in Revit becomes an `IfcSpace` in IFC. Walls do not "sit inside" a room; they bound it, and that link exists only if the exporter writes "space boundaries" (default: off). Areas (net, gross) are stored in separate quantity sets that Revit sometimes leaves out or fills with the same number twice. A zone (`IfcZone`) is a grouping of spaces with no geometry; a system (`IfcSystem`, `IfcDistributionSystem`) groups pipes, ducts and equipment. See [spatial structure and relationships](../../01_ifc_basics/04_spatial_structure_and_relationships.md) and [properties and quantities](../../01_ifc_basics/05_properties_quantities_psets.md).

For an MCP tester: before judging a colour, area or room answer, the assistant must say where in the file the information was (or was not) found.

## Problem map

Ranked by records and breadth. Counts are my reading plus rough text-match counts (`kb.py stats --text`): signals, not exact measurements.

| # | Problem | How users describe it | Frequency signal | Root cause | Typical fix |
|---|---|---|---|---|---|
| 1 | Colours lost, grey or white after export, or different per viewer | "whats the root cause of grey MEP-components in IFC"; "导出来颜色跟rvt不一样"; "why is everything white??" | Largest cluster: about 54 of the 104 real material records mention colour/grey/white/beige; also 18 synthetic; en dominant, zh, es, de, fr, ru, ko in prompts | Colour needs an `IfcSurfaceStyle`; Revit view filters and graphic overrides are not exported; some viewers ignore styles or resolve them differently | Set colour on the material itself, by-category; check whether styles exist in the file; use IFC2x3 CV2.0 or IFC4 RV |
| 2 | Where is the colour stored? Type vs occurrence, shape vs material | "Where and how will my colors be saved in IFC?"; "Material colour assigned to an element type is not applied to its occurrences" | About 12 real records (viewer developers, architects) | Two paths (styled item on geometry, or material definition representation); shape style beats material style; viewers disagree | Trace both paths; report which one carries the colour |
| 3 | Transparency and glass: opaque or beige in viewers | "IFC4 IfcSurfaceStyleShading.Transparency is ignored"; "transparent walls become beige in Solibri" | About 6 real, 2-3 synthetic (ko, en) | Transparency is 0 = opaque, 1 = fully transparent (inverted vs alpha); some viewers ignore it | Check the stored value and the viewer's support |
| 4 | MEP elements carry the system name instead of the real material | "Pipes / ducts / etc export using system material not actual material"; "Losing duct fitting material" | About 8 real records (Revit exporter issues #577, #373, #915, #112) + 4 synthetic | Exporter uses the MEP system material by design (historic demand for system colours) | Work-arounds via `IfcSingleMaterialOverride`; separate style from material (proposal open) |
| 5 | Layered walls: layers collapsed, one layer only, or "no material pset" | "Material pset Wall/Floors with several material layers not exported IFC4"; "only one material is output as material layer" | About 20 real records mention layer sets/constituents; 7 synthetic; en, zh, ja, ru | IFC4 RV uses constituent sets; custom families export one layer; viewers differ | Read constituents too; use IFC2x3 or DTV; check thickness in quantities |
| 6 | Elements "without material" and where to look | "some elements return no material"; "найди элементы без материала" | About 12 synthetic prompts in 7 languages (en, ru, zh, ja, ko, nl, es) ask for this; several real developer threads | A material can sit on the occurrence, the type, a representation item, a layer set, a profile set or constituents | Check all paths, group by class, say which path was used |
| 7 | Material names, duplicates, naming standards, material psets | "428 duplicate materials"; "Kwaliteits- en prestatie-eisen horen niet in de materiaalnaam"; "材质不会通过自定义属性集导出" | About 10 real records (nl, zh, en) + 5 synthetic | Exporters write one material per usage; standards (NAA.K.T., project nomenclature) are not enforced; Revit does not export materials through custom property sets (documented limitation) | Normalise names on request; merge duplicates keeping styles |
| 8 | Colours/materials lost after conversion or import (Revit, glTF/GLB, OBJ, FBX) | "colours missing after IFC to GLB"; "Su 导入 Revit 材质总是丢失"; "mtl lacks material" | About 12 real records (en, zh, ru) | Converters read only some style paths; Revit import ignores styles; textures not embedded | Check the file first; fix at the converter or re-assign materials |
| 9 | Presentation layers and CAD layer mapping | "How does multiple IfcPresentationLayerAssignment with the same name work?"; "[Revit]图层导出设置"; "DXF/DWG export with ifc -> cad layers translation" | 4-6 real, 5 synthetic (de, zh, ru, en) | Layers are display grouping only; Revit layer export uses a mapping text file; no uniqueness rule | List layers and counts; flag duplicates; treat DXF mapping as an export step |
| 10 | Views, sheets, crop regions, 2D drawings | "Automate view plans of each apartment with the cropzone"; "No annotation context Annotation/PLAN_VIEW"; "door swings from ArchiCAD IFCs don't show up" | About 15 real (Revit automation, Bonsai drawings), 5 synthetic | View/sheet state is not in IFC; Revit IFCs lack an annotation context; plan symbols are imported unevenly | Do view/sheet work on the Revit side; add annotation context for Bonsai |
| 11 | IfcSpace missing, without geometry, or shifted/wrong height | "IFC export: IfcSpaces are missing"; "Room geometry shifted in IFC Exporter 25.4.40.17"; "Rooms exported with wrong elevation with shared coordinates" | Largest space cluster: roughly 25 real records (missing, shifted, wrong elevation, no geometry) + about 8 synthetic (en, ru, de, ja) | Export settings (rooms in 3D views, phase, 2D room boundaries), unenclosed/zero-area rooms, exporter regressions, survey-point levels | Check settings and room validity; roll back or update the exporter |
| 12 | Space areas wrong, missing or identical (net = gross), do not match schedules | "Qto values Net Area and Gross Area of IfcSpace exporting same values"; "площадь по зонам не сходится с RUS_Area"; "IFCの面積がRevitの集計表と合わない" | About 15-20 real, 30+ synthetic room-list/area prompts in 12 languages | Quantity export bugs by version, planned vs measured area, units, boundary definition | Compute from geometry and label as computed; compare with the right definition |
| 13 | Link IFC does not turn IfcSpace into Rooms | "Link IFC does not create Room/Space from IfcSpace" | 5 real records of one repeated issue (#15, open since 2018 per the records) | Link IFC creates generic models; only Open IFC converts | Use Open IFC for rooms or accept generic models |
| 14 | Space boundaries and space-to-element relations | "2nd Level Space Boundary ConnectionGeometry displaced"; "Relation between doors to rooms"; "no IfcRelSpaceBoundary in the exported ifc" | About 22 real text matches for "boundar" + 3 synthetic | Boundaries are optional, geometry bugs, doors link rooms only via boundaries or realizing elements | Turn on 1st/2nd level boundaries; use the right relation |
| 15 | Zones: IfcZone vs IfcSpatialZone, membership, unstable IDs | "Space data depending on zone"; "зоны с кривыми границами ... не выгружаются"; "IfcZone ObjectType regression" | About 11 real, 6 synthetic (en, ko) | Zones are groupings; Revit virtual zones lose GlobalIds; bad zone boundaries break export | Fix boundaries; use zone-specific properties |
| 16 | Systems: empty or missing IfcSystem, COBie Systems tab empty, members unassigned | "Cobie export - systems tab empty"; "Revit cannot export properties of an IfcSystem" | About 9 real records (plus 5 copies of one COBie thread) and about 20 synthetic prompts (en, ru, fr, es, nl, no, pt-BR, ko) | COBie needs components with types; systems need `IfcRelAssignsToGroup`; export limits | List systems and orphans; fix assignment or types |

## Problems in depth

### 1. Colours lost: everything grey or white

**Symptoms in users' words**
- en: "Some MEP IFCs show colours and others grey; is it an MVD issue?" (real, BIM coordinator) [en-gh-revit-ifc-r040](https://github.com/Autodesk/revit-ifc/issues/579). Answer: colour comes from the material, not view filters or overrides; set pipes by category.
- en: "Colors from view filters are not exported" (real, Revit Ideas) [en-autodesk-revit-export-r041](https://forums.autodesk.com/t5/revit-ideas/ifc-export-element-color-export-as-per-visibility-graphics/idi-p/12995112)
- zh: "rvt和ifc什么关系，导成ifc颜色为什么变了" (real; gloss: what is the relation of RVT and IFC, why did the colours change after export) [zh-revit-export-r019](https://www.zhihu.com/question/49455994)
- en: "all geometry renders entirely white regardless of materials in the IFC, colours visible in BIMvision are absent in the web viewer" (real) [en-gh-thatopen-r034](https://github.com/ThatOpen/engine_components/issues/745). Analysis: the three IFC2X3 files contain no surface styles, so there were no colours to render.
- zh (synthetic, `zh-zhihu-s011`): "导出来颜色跟rvt不一样，看看ifc里材质和样式是怎么存的"
- es (synthetic, `mx-mcl-s004`): "importé el IFC de Archicad en Revit y se perdieron los colores, revisa si los estilos de superficie están en el archivo"

**Why it happens.** `IfcMaterial` has no colour; `IfcSurfaceStyle` (with `IfcSurfaceStyleShading`) must exist and be linked. Revit writes colours from materials and category, not from the graphic overrides of a view (feature requests to export "current view colours" are open: [en-gh-revit-ifc-r051](https://github.com/Autodesk/revit-ifc/issues/731)). Some viewers colour by element style only, some by material only. See [section 2 of the materials doc](../../01_ifc_basics/07_materials_classification_types_styles.md).

**What fixes it.** Set the colour on the Revit material (Graphics tab) and keep MEP elements by-category; export IFC2x3 CV2.0 or IFC4 RV; verify in the file before blaming the viewer.

**Good assistant behaviour.** Count elements that have a style on the shape, a style via the material, or neither; say which of the three the user's problem is. If the file has no styles, say "the colour was never written" and point to the exporter. If it has styles, the issue is in the viewer/import.
**Clarifying questions:** Which viewer shows it grey? Was the file exported from Revit with a particular setup? Does the same file look coloured in another viewer? Are you looking for the Revit view colours (filters) or the material colours?

### 2. Where is the colour stored? Type, occurrence, shape, material

**Symptoms**
- en: "Where and how will my colors be saved in IFC? pipe-diameter colours exported from Allplan disappear in other apps but show in a viewer" (real) [en-mcl-r025](https://forums.buildingsmart.org/t/where-and-how-will-my-colors-be-saved-in-ifc/1806). Answer: material is only a name; colour needs a surface style via a styled representation; Allplan attached the style to the shape; 428 duplicate materials.
- en: "material via IfcMaterialDefinitionRepresentation on the type only gives white [1,1,1,1], directly on the wall gives red" (real, fixed in web-ifc) [en-gh-thatopen-r024](https://github.com/ThatOpen/engine_web-ifc/issues/2235)
- en: "Why is it so difficult to get colors to show up? IFCSTYLEDITEM on a proxy mass: Solibri shows colour not transparency, ArchiCAD neither" (real) [en-mcl-r023](https://forums.buildingsmart.org/t/why-is-it-so-difficult-to-get-colors-to-show-up/2312). Shape style beats material style per an implementer agreement.
- en: "Occurrences end up on unstyled representation-map copies; Solibri colors from material only while Bonsai resolves via type" (real) [en-model-checking-r010](https://github.com/IfcOpenShell/IfcOpenShell/issues/10020)
- en: "Coloring one part of a multi-layered wall results in whole wall getting colored" (real) [en-gh-thatopen-r023](https://github.com/ThatOpen/engine_web-ifc/issues/1733)
- en (synthetic, `mx-mcl-s016`): "where is the colour of a wall actually stored in IFC? material or shape? show me for the selected one"

**Why.** Colour can come from `IfcStyledItem` on the representation item, from the material's `IfcMaterialDefinitionRepresentation`, or from the type; the occurrence wins over the type; tools differ on which they resolve. A type-level style is often not applied to occurrences. Details: [materials doc section 1.6 and 2](../../01_ifc_basics/07_materials_classification_types_styles.md).

**Fix / behaviour.** The assistant should trace all paths for one selected element and print them in order of precedence (representation item style, material style on the occurrence, type), then say which one a typical viewer would pick. **Clarifying:** Which element or GlobalId? Which viewer is the target?

### 3. Transparency and glass

**Symptoms**
- en: "IFC4 IfcSurfaceStyleShading.Transparency is ignored: alpha stays 1.0 although IfcSurfaceStyleShading has Transparency" (real) [en-mcl-r012](https://github.com/ThatOpen/engine_web-ifc/issues/2229)
- en: "if IfcGeometry colour is not defined it defaults to white; consider alpha (glass, proxies, rooms nearly transparent)" (real) [en-gh-thatopen-r025](https://github.com/ThatOpen/engine_web-ifc/issues/1504)
- ko (synthetic, `mx-mcl-s009`): "IFC 열면 유리가 불투명하게 나오는데 투명도 값이 파일에 들어있는지 확인해줘" (gloss: glass appears opaque, check whether a transparency value is in the file)
- en (synthetic, `en-model-checking-s006`): "why do my cavity walls show opaque beige, they were see through in archicad. style issue?"

**Why.** In IFC `Transparency` 0.0 is opaque and 1.0 is fully transparent, the opposite of alpha; some viewers ignore it, and a style missing on the occurrence returns the default.

**Behaviour.** Read the stored value, state the convention, and separate "value is missing" from "viewer ignores it". **Clarify:** Which viewer? Was the file produced by Archicad or Revit?

### 4. MEP: the material is the system name

**Symptoms**
- en: "Pipes export the pipe system material instead of their actual material such as PVC or copper." (real) [en-gh-revit-ifc-r041](https://github.com/Autodesk/revit-ifc/issues/577). Answer: designed per user demand for system colours; tracked internally, open.
- en: "Duct fitting material disappears in IFC. Workaround: IfcSingleMaterialOverride parameter" (real) [en-autodesk-revit-export-r025](https://forums.autodesk.com/t5/revit-mep-forum/losing-duct-fitting-material-when-exported-to-ifc-files/td-p/8736337)
- en: "one duct type used for Supply and Return, colours by system, but fittings export wrong" (real) [en-mep-r014](https://github.com/Autodesk/revit-ifc/issues/373)
- en (synthetic, `en-eng-s003`): "pipes show material = system name (HOT WATER) not copper. can you list pipes and what material they actually have"
- en (synthetic, `mx-mcl-s011`): "do the pipes have the real material (PVC/copper) or just the system material name like SEWER? list by system"

**Why.** Revit's exporter uses the system material for pipes and ducts so colours match systems; one system can mix PVC and HDPE, so the real material is lost.

**Behaviour.** List material names on `IfcPipeSegment`, `IfcDuctSegment` and fittings, compare them with the list of system names in the model, report counts; say where the real material might live (psets). Do not invent a real material. **Clarify:** Is the system name the problem or the colour? Where else could the real material be recorded (type name, pset)?

### 5. Layered walls: layers collapsed, one layer only

**Symptoms**
- en: "Solibri shows no Material pset, SimpleBIM one row with combined name for layered walls on IFC4 Reference View" (real) [en-mcl-r005](https://github.com/Autodesk/revit-ifc/issues/610)
- en: "only one material is output as material layer for a structural framing family mapped to IfcWall; only one layer, chosen arbitrarily" (real) [en-mcl-r006](https://github.com/Autodesk/revit-ifc/issues/929)
- en: "project.append_asset drops material surface styles when the material is reached via IfcMaterialLayerSetUsage" (real) [en-mcl-r015](https://github.com/IfcOpenShell/IfcOpenShell/issues/8662)
- en: "Composite Wall in Bonsai BIM: can Bonsai make composite walls with layers, materials and thicknesses? Layers do not show in other viewers" (real) [p-student-r008](https://community.osarch.org/discussion/2758/composite-wall-in-bonsai-bim)
- zh (synthetic, `mx-mcl-s003`): "帮我查下这个IFC里墙的材质层有没有丢，是IfcMaterialLayerSetUsage还是只剩一个IfcMaterial"
- ja (synthetic, `mx-mcl-s008`): "壁ごとの材料レイヤーと厚みを一覧にして、レイヤー無い壁はどれか教えて"

**Why.** Layer sets fit standard walls; IFC4 Reference View prefers constituent sets (see the [versions file](./versions_mvd_encoding_guid.md)); a structural-framing family mapped to IfcWall exported only one, arbitrarily chosen layer; some tools lose styles when copying layered materials. Rule of thumb for QA: `sum(LayerThickness)` equals the body thickness; a zero-thickness layer is valid; a layer set usage belongs to occurrences only ([materials doc 1.3-1.4](../../01_ifc_basics/07_materials_classification_types_styles.md)).

**Fix / behaviour.** For each wall report the material association kind (LayerSetUsage, ConstituentSet, single IfcMaterial), list layers with thickness in the project's length unit, compare the total with the geometric thickness, and flag walls reduced to one material. **Clarify:** IFC2x3, IFC4 RV or DTV? Which unit should thickness be shown in? Do you also need volume per layer? (Revit exports only layer thickness; area and volume per layer is an open request [en-qto-r026](https://github.com/Autodesk/revit-ifc/issues/753), so such numbers would be computed, not read.)

### 6. "Which elements have no material?" and where to look

**Symptoms**
- en: "pasted an ExtractMaterialData helper that checks HasAssociations and IfcRelAssociatesMaterial; some elements return no material" (real, xBIM) [en-gh-xbim-others-r011](https://github.com/xBimTeam/XbimEssentials/issues/642). Answer: materials can sit on representation items (door panel, frame), types and layer sets; many assignment paths.
- en: "How can a non-expert list every material in an IFC model given IfcMaterial, LayerSet, ProfileSet, ConstituentSet?" (real) [p-student-r016](https://forums.buildingsmart.org/t/ifc-materials/4861)
- ru (synthetic, `mx-mcl-s002`): "глянь у каких элементов вообще нет материала в ифс, по категориям плиз"
- zh (synthetic, `zh-revit-export-s004`): "帮我找出没有材质的构件，按楼层列出来"
- ja (synthetic, `ja-japan-s017`): "材料が付いてない壁をタイプ別に出して。レイヤ構成も無いやつ"
- ko (synthetic, `ko-korea-s012`): "재료 안 붙은 구조부재 리스트 줘"

**Why.** Material can be associated to the occurrence, to the type, to a profile or constituent set, or only as a style on a representation item. Walls with a layer set in the type but nothing on the occurrence are not "without material".

**Behaviour.** Check occurrence, type, set members (layers, profiles, constituents) and say which levels were checked; group by IFC class and storey; do not claim "no material" for an element that is classed as an opening or virtual element, where materials are not allowed. **Clarify:** Occurrences only, or type-level too? Which classes matter (structural members only)?

### 7. Material names, duplicates and naming standards

**Symptoms**
- nl: "Kwaliteits- en prestatie-eisen horen niet in de materiaalnaam; NAAm_Kenmerk_Toepassing" (real Dutch ILS guide; gloss: quality and performance requirements do not belong in the material name) [nl-dutch-r022](https://www.digigo.nu/ilsen-en-richtlijnen/bim-basis-ils/4-7-materiaal)
- nl: "Materiaalnamen verschillen: prefabbeton, gewapend beton, grindbeton, ihw, ihwg, tpg; computers kunnen dit niet betrouwbaar interpreteren" (real; gloss: names differ, computers cannot interpret them) [nl-dutch-r023](https://www.digigo.nu/ilsen-en-richtlijnen/bim-basis-ils/praktijk/1-naa-k-t-eenduidige-materiaalbenaming)
- zh: "自定义属性集里的材质导不进IFC" (real; gloss: material in a custom property set will not export) [zh-lightweight-review-r008](https://www.autodesk.com.cn/support/technical/article/caas/sfdcarticles/sfdcarticles/CHS/Materials-are-not-exported-to-IFC-with-custom-property-sets-from-Revit.html)
- en: "Where and how will my colors be saved in IFC? ... 428 duplicate materials" [en-mcl-r025](https://forums.buildingsmart.org/t/where-and-how-will-my-colors-be-saved-in-ifc/1806)
- fr (synthetic, `fr-francophone-s012`): "renomme les matériaux selon la nomenclature de la convention, ex MAT_BETON_C25"
- it (synthetic, `mx-mcl-s010`): "ci sono materiali duplicati con lo stesso nome nel modello, uniscili e tieni lo stile colore"

**Behaviour.** Listing and proposing normalised names is safe; renaming or merging is a write action: show the mapping, apply only after confirmation, write a new file, keep surface styles when merging, and list unmapped names. **Clarify:** Which naming standard (project convention, NAA.K.T., other)? Merge only exact duplicates or also near-duplicates (case, spaces)?

### 8. Colours and materials lost after conversion or import

**Symptoms**
- en: "IFCINDEXEDCOLOURMAP not implemented - colours missing after IFC to GLB" (real; answer: not a bug, IFC stores multiple colours per object, GLB is for rendering) [en-viewconv-r006](https://github.com/IfcOpenShell/IfcOpenShell/issues/2824)
- en: "[IfcConvert] Cannot export material to object format: mtl lacks material though ifc has it" (real) [en-gh-ifcopenshell-r042](https://github.com/IfcOpenShell/IfcOpenShell/issues/4846)
- zh: "Su导进Revit材质总是丢" (real) [zh-revit-export-r020](https://zhuanlan.zhihu.com/p/372183287); "MAX模型导进Revit材质全没了" [zh-revit-export-r004](https://ask.csdn.net/questions/8796533)
- ru: "колонны из Теклы в Ревите: материал и тонирование не меняются; арматура и узлы не переносятся" (real) [ru-dwg-other-r013](https://forum.dwg.ru/showthread.php?t=155997)
- zh: "IfcConvert 会合并构件、丢 expressID ... 材质全变灰" (real; gloss: IfcConvert merges parts, drops expressID, materials turn grey) [zh-csdn-dev-r002](https://juejin.cn/post/7691297274821705728)
- fr (synthetic, `fr-viewconv-s010`): "mon obj exporté depuis l'ifc n'a plus aucune couleur, pourquoi ?"
- de (synthetic, `mx-mcl-s015`): "wie krieg ich die Farben von Archicad IFC in Revit rüber? Oberflächen sind alle grau"

**Behaviour.** First check the source file: if it has styles, the loss happened in the import or converter; if not, the exporter. Explain Revit import behaviour (colours depend on import path; Link vs Open). **Clarify:** Source program, target program, format (OBJ, GLB, FBX)? Do you need textures or only colours?

### 9. Layers: presentation layers, CAD layers, drawing views

**Symptoms**
- en: "How does multiple IfcPresentationLayerAssignment with the same name work? one layer or two?" (real) [en-mcl-r028](https://forums.buildingsmart.org/t/how-does-multiple-ifcpresentationlayerassignment-with-the-same-name-work/3126). Answer: no uniqueness rule; treat as separate (debated).
- zh: "Revit图层导出设置怎么调" (real; gloss: how to set Revit layer export settings) [zh-revit-export-r027](https://www.bilibili.com/read/cv20354710/)
- en: "need to deliver IFC plus DXF/DWG; in Revit there is a layer translation table, different IFC classes to different layers, can Bonsai do that" (real) [en-viewconv-r001](https://github.com/IfcOpenShell/IfcOpenShell/issues/8009)
- it: "dall'IFC come estraggo piante e sezioni in DXF?" (real) [it-italy-r023](https://biblus.acca.it/una-guida-completa-per-convertire-file-ifc-in-dxf/)
- en: "error 'No annotation context Annotation/PLAN_VIEW for drawing' when annotating imported Revit file" (real; Revit IFCs lack an annotation context) [en-osarch-r037](https://github.com/IfcOpenShell/IfcOpenShell/issues/3115)
- en: "Doors appear in 3D but are invisible in floor plan; the Model footprint representation is not displayed" (real, Archicad IFC in Revit) [en-autodesk-revit-import-r010](https://github.com/Autodesk/revit-ifc/issues/358)
- en: "Automate the creation of view plans of each apartment with the cropzone aligning exactly..." (real, Dynamo) [en-revit-auto-r007](https://forum.dynamobim.com/t/automate-the-creation-of-view-plans-of-each-appartment-with-the-cropzone-aligning-exactly-on-the-outer-boundary-of-the-boudnary-walls-of-each-appartment/115202)
- de (synthetic, `mx-mcl-s006`): "zeig mir alle IfcPresentationLayerAssignment mit Anzahl Objekte, Layer mit gleichem Namen bitte markieren"
- zh (synthetic, `mx-mcl-s014`): "把IFC里的图层名字列出来，每个图层有多少构件，导出表格"
- ru (synthetic, `ru-viewconv-s011`): "нужен dwg из этого ифс, чтоб слои по классам, а то в автокаде одним куском"

**Why.** Presentation layers are display grouping, not storeys, disciplines or classification ([materials doc section 2](../../01_ifc_basics/07_materials_classification_types_styles.md)). A DXF "layer per IFC class" is an export mapping, not information in the IFC. A Revit worker who says "layers" often means views, filters or sheets; an OSArch reply notes that "view/layer/panel state is not stored in IFC" [en-osarch-r003](https://community.osarch.org/discussion/3782/native-ifc-as-the-source-a-reproducible-project-template-for-bonsai-and-two-questions). Revit's layer export uses a mapping file (a UTF-16 read bug of that file broke floor export on non-English systems: [en-geom-r009](https://github.com/Autodesk/revit-ifc/issues/759)).

**Behaviour.** Ask which "layer" is meant (material layer, IFC presentation layer, CAD layer in DWG, Revit view). For a layer listing, count items per layer and flag same-name duplicates. For view/sheet batch tasks, remember they need a Revit-side tool (rename views with a prefix, create sheets with sequential numbers, handle number collisions), not an IFC reader. **Clarify:** Material layers or presentation layers? What is the target (DWG, drawing set, viewer filter)? Which title block and sheet numbering?

### 10. IfcSpace missing, without geometry, or shifted

**Symptoms**
- en: "IFC Export - IFCSpaces are missing" (real, Revit LT) [en-autodesk-revit-export-r015](https://forums.autodesk.com/t5/revit-architecture-forum/revit-2019-lt-ifc-export-ifcspaces-are-missing/td-p/8424409)
- en: "Spaces moved outside the building and wrong heights after exporter update; only 26.1.0.23 avoids shifting" (real) [de-dach-r003](https://github.com/Autodesk/revit-ifc/issues/924)
- en: "IfcSpaces are offset by project elevation when exporting with shared coordinates; resetting coordinates to zero aligns them" (real; cause: levels using Survey Point as elevation base) [en-autodesk-revit-export-r014](https://github.com/Autodesk/revit-ifc/issues/907)
- en: "list of rooms with no shape in IFC, element id and guid, why no 3D shape exported" (real) [en-sg-corenetx-r004](https://github.com/noddlesskcho/IFC-Repair-Studio). Causes: area but no 3D shape exported, area 0 (unenclosed/redundant), height 0, no area data.
- en: "Rooms placed in wrong storey in IFC. Uncheck 'Use 2D room boundaries for room volume'" (real) [en-autodesk-revit-export-r043](https://forums.autodesk.com/t5/revit-architecture-forum/revit-ifc-export-results-in-wrong-position-of-rooms/td-p/12156364)
- en: "one IfcSpace at roof level is a big solid box above the roof only here" (real; viewers usually hide or make spaces translucent) [en-gh-thatopen-r055](https://github.com/ThatOpen/engine_fragment/issues/301)
- ru (synthetic, `ru-spaces-s010`): "глянь какие помещения из ревита не выгрузились в ифс, в модели вижу только 40 IfcSpace"
- en (synthetic, `en-spaces-s008`): "rooms arent showing up in the ifc at all, what setting am I missing"

**Why.** Revit exports Rooms and Spaces as `IfcSpace`; records show that Areas (area plans) and Masses can also come out as `IfcSpace`, while one KB doc says areas are not exported, so behaviour depends on version and settings. With "export only elements visible in view" you must also enable "export rooms, areas and spaces in 3D views" or none appear ([spatial doc item 7](../../01_ifc_basics/04_spatial_structure_and_relationships.md)); unplaced, unenclosed or redundant rooms have zero area and no volume; certain exporter builds shifted room geometry; shared-coordinate and survey-point settings add an elevation offset.

**Fix.** Check the phase and view-export options, delete or fix invalid rooms, try the 2D-boundary option off, update or roll back the exporter, reset shared coordinates.

**Behaviour.** Count `IfcSpace` per storey, compare with the room list the user supplies (never assume the list), list spaces with no `Representation`, zero area or zero height with GlobalId, test shifts by comparing space bounding boxes with walls on the same storey and report offsets. **Clarify:** Revit version and exporter build? Is "Export only elements visible in view" on? Do you have the Revit room list for comparison?

### 11. Space areas: wrong, missing or identical; do not match the schedule

**Symptoms**
- en: "gross and net floor area in Qto_SpaceBaseQuantities have the same value in the IFC; only volumes differ when space boundary is wall core center" (real; Autodesk reproduced it) [en-spaces-r001](https://github.com/Autodesk/revit-ifc/issues/742)
- en: "In Revit 2023 IfcSpace Qto_SpaceBaseQuantities NetFloorArea and others are not getting exported; still open for years; workaround custom psets" (real) [en-spaces-r013](https://github.com/Autodesk/revit-ifc/issues/529)
- en: "Can't export room area to custom property set (client requirement) while Area objects work fine" (real) [en-gh-revit-ifc-r004](https://github.com/Autodesk/revit-ifc/issues/855)
- en: "standard Qto sets are immutable by design; use custom Psets" (answer in [en-spaces-r011](https://github.com/Autodesk/revit-ifc/issues/865))
- ru: "площади ТЭП в xml расходятся на 20 м2, дубли не найти, как править IFC без ревита" (real) [ru-autodesk-telegram-r010](https://habr.com/ru/articles/1100956/); and "площадь по геометрии зон не сходится с атрибутом и с XML АГР" [ru-habr-dev-r007](https://habr.com/ru/articles/1100956/). Answer: compute from geometry; stale zone areas caused the gap.
- ja: "部屋名・用途・床面積がIFCに出て別ビューアで読めるか。面積が合わない時は境界・計算方法・単位・版を確認" (real; gloss: do room name, use and floor area appear in the IFC and read in another viewer; if the area differs, check boundary, method, unit and edition) [ja-japan-r019](https://note.com/t_note_memo/n/n8903305b00fb)
- en: "ifc5d IfcOpenShell QTO calculator never produces quantities for IfcSpace ... Mapping intentionally empty: space net/gross areas have legal implications" (real) [en-qto-r015](https://github.com/IfcOpenShell/IfcOpenShell/issues/8570)

**Why.** Net vs gross floor area depend on the boundary definition (core centre vs finish face vs inside face), and national methods differ (a forum answer notes Belgian method uses gross volumes: [en-spaces-r027](https://forums.buildingsmart.org/t/level1-boundary-generation-to-the-centre-line-or-inside-face/2724)). `GrossPlannedArea` and `NetPlannedArea` in `Pset_SpaceCommon` are briefing values, not measured; measured area is in `Qto_SpaceBaseQuantities` ([properties doc](../../01_ifc_basics/05_properties_quantities_psets.md)). Units can differ (mm² vs m²).

**Behaviour.** Say which source was used (Qto value, property, or computed from geometry) and label computed values as computed; report the project area unit; list spaces with missing or zero area; compare with the user's schedule per room and show differences above the stated tolerance; never sum areas silently when some spaces lack values. Because area numbers carry legal weight (permit tables, rent, TEP), the assistant should ask which definition applies. **Clarify:** Net or gross, which regulation or method? Compare against which reference (Revit schedule, AGR XML, program)? What tolerance (0.5 m², 2 %, 5 %)?

### 12. Link IFC does not make Rooms

**Symptoms**
- en: "Wants IfcSpace converted to Rooms (architectural link) or Spaces (MEP link)" (real, open since 2018) [en-autodesk-revit-import-r018](https://github.com/Autodesk/revit-ifc/issues/15); "IfcSpace imported as generic models obstructs views; MEP engineers must use Open IFC just to get Rooms" [en-roundtrip-r004](https://github.com/Autodesk/revit-ifc/issues/15)
- en (synthetic, `en-autodesk-revit-import-s006`): "list ifcspaces w/ name number and area, i want rooms in revit not generic models"

**Why.** Link IFC brings `IfcSpace` as generic models (DirectShape); Open IFC can convert them to Rooms ([import/link reference](../../03_software/revit/ifc_import_link_reference.md)).

**Behaviour.** Explain the limit, list the spaces from the IFC (name, number, area, storey) as a table, do not promise creation of native rooms when only a link exists. **Clarify:** Do you need rooms for editing/tagging or only as an underlay?

### 13. Space boundaries and space-to-element relations

**Symptoms**
- en: "with SpaceBoundaries=2 the IfcRelSpaceBoundary2ndLevel geometry is shifted several metres in XY from the IfcSpace, breaking BEM workflows" (real) [en-spaces-r006](https://github.com/Autodesk/revit-ifc/issues/961)
- en: "one space and its curtain wall (room bounding on) gets no RelSpaceBoundary" (real) [en-spaces-r003](https://github.com/Autodesk/revit-ifc/issues/107)
- en: "Revit knows From and To rooms for a door; how can IfcDoor be related to IfcSpace?" (real) [en-gh-revit-ifc-r046](https://github.com/Autodesk/revit-ifc/issues/91). Answer: containment allows one level only; boundary relationships suggested.
- en: "about 1000 models for thermal simulation; boundaries only the four walls" (real) [en-dynamo-pyrevit-r023](https://forum.dynamobim.com/t/export-ifcrelspaceboundary-room-boundaries/91608). Answer: set Energy Settings phase to match walls and spaces.
- pt (synthetic, `pt-spaces-s014`): "preciso rodar simulação energética, verifica se os ambientes estão fechados e têm limite de espaço"
- en (synthetic, `en-blogs-linkedin-s009`): "furniture sits under storeys not spaces, FM says rooms are empty. confirm?"

**Why.** Walls bound rooms and are not contained in them; boundaries exist only if the "space boundaries" option is 1st or 2nd level (default None). Doors relate to rooms through boundaries or realizing elements, not containment ([spatial doc, sections 2 and 6](../../01_ifc_basics/04_spatial_structure_and_relationships.md)).

**Behaviour.** Count boundaries per space, state level (1st or 2nd), list spaces with none, and report which relation was used for each answer. For FM, say whether furniture is contained in the space or only the storey. **Clarify:** Is this for energy analysis (2nd level needed) or just adjacency? Wall centre-line or inside-face boundaries?

### 14. Zones: IfcZone, IfcSpatialZone, membership and stability

**Symptoms**
- en: "Space data depending on zone: five candidate options: psets, classification, proxies, extra zone, IfcAsset" (real) [en-spaces-r028](https://forums.buildingsmart.org/t/space-data-depending-on-zone/4434). Answer: IfcZone supports multi-membership; IfcSpatialZone; custom Psets.
- en: "Advantages of IfcSpatialZone in comparison to IfcSpace" (real) [en-spaces-r032](https://forums.buildingsmart.org/t/advantages-of-ifcspatialzone-in-comparison-to-ifcspace-in-terms-of-cadaster-surveying/4560)
- ru: "зоны с кривыми границами в Revit считаются, а в IFC не выгружаются как тело" (real; gloss: zones with imperfect boundaries compute in Revit but fail IFC export as a solid) [ru-habr-dev-r002](https://habr.com/ru/articles/1089018/); the post also describes zones vanishing and areas being counted twice before an AGR check [ru-autodesk-telegram-r008](https://habr.com/ru/articles/1089018/)
- nl: "Ruimte: toegankelijk, minimaal 1,5 m netto hoogte; Name en ObjectType; zones voor woning, brandcompartiment" (real Dutch guide; gloss: space must be accessible, min 1.5 m net height; zones for dwelling and fire compartment) [nl-dutch-r021](https://www.digigo.nu/ilsen-en-richtlijnen/bim-basis-ils/4-1-ruimten)
- en: "IFC4RV & IFC2x3: IfcZone ObjectType regression" (real, fixed) [en-revit-r038](https://github.com/Autodesk/revit-ifc/issues/96)
- en (synthetic, `en-spaces-s005`): "show all IfcZones and which spaces are in each, flag spaces in more than one zone"
- ko (synthetic, `ko-spaces-s017`): "존에 안 들어간 실(IfcSpace) 찾아줘" (gloss: find spaces that are in no zone)

**Why.** A zone is a pure grouping of spaces (no geometry; a space may be in several zones); a spatial zone has its own shape and is linked through a different relation; Revit "virtual" zones made from a `ZoneName` parameter do not keep GlobalIds between exports. A fire compartment has no dedicated entity ([spatial doc, section 4](../../01_ifc_basics/04_spatial_structure_and_relationships.md)).

**Behaviour.** Say which construct (IfcZone, IfcSpatialZone, IfcGroup) the file uses, list members through the group relation, flag multi-membership and empty zones, and warn that zone IDs may not be stable across exports. **Clarify:** Is "zone" a thermal/HVAC zone, fire compartment, dwelling unit or a Revit/Archicad zone (which may be a room)? Which code or client rule defines it?

### 15. Systems: empty or unassigned, COBie Systems tab empty

**Symptoms**
- en: "systems tab empty when exporting to COBie spreadsheet, but Bonsai's systems tab identifies 214 systems" (real, 5 copies of the same thread) [en-uk-anz-india-r002](https://github.com/IfcOpenShell/IfcOpenShell/issues/6068). Answer: COBie needs foreign keys: systems link to components, and components need a type; the model had no types so the output was correct [en-cobie-r010](https://github.com/IfcOpenShell/IfcOpenShell/issues/6068).
- en: "cannot get psets out from an IfcSystem (Revit's system browser)" (real; first called a limitation, later possible through a custom pset mapping) [en-mep-r005](https://github.com/Autodesk/revit-ifc/issues/523)
- en: "circuits not written when export is limited to visible elements" (real) [en-mep-r008](https://github.com/Autodesk/revit-ifc/issues/959)
- en: "Override IfcDistributionSystem of elements" (real; logged, open) [en-mep-r007](https://github.com/Autodesk/revit-ifc/issues/900)
- nl: "Waarom geen verwijzing naar Systems (IfcDistributionSystem)? NL/SfB-codes sluiten niet geheel aan op de praktijk" (real; gloss: why no reference to IfcDistributionSystem; NL-SfB does not fully match practice) [nl-dutch-r014](https://github.com/nl-digigo/imwo/issues/52)
- ru (synthetic, `ru-mep-s005`): "покажи воздуховоды и трубы которые не входят ни в одну систему, ифс из ревита, нужно до сдачи"
- en (synthetic, `en-mea-s007`): "which ducts/pipes are not in any system? chiller plant room first"
- en (synthetic, `en-fmor-s005`): "whats served by AHU-03? list components and the rooms"

**Why.** System membership is the group relation (`IfcRelAssignsToGroup`); an empty COBie sheet usually means missing types or missing assignments, not a broken exporter. Revit exports groups as `IfcSystem` types, and export filters can drop circuits.

**Behaviour.** List every system with member counts and flag empty ones; find pipes, ducts, fittings and equipment with no system; offer to group by system for lengths and counts; explain the empty COBie sheet from the data. **Clarify:** Which classification of systems (abbreviations like SA, EA, CW)? Is a list enough or should orphans be assigned (a write action)? Limit to a space, level or room such as "chiller plant room"?

## Real questions

KB paraphrases, original language kept; "EN gloss" given where the original is not English. Source link text is the KB record id. Personas are the KB's inference. `*` = the source is in that language but the KB stored its paraphrase in English; the text shown is that paraphrase (title kept in the original language where the record has one).

| # | lang | question (original-language paraphrase) | EN gloss | persona | source |
|---|---|---|---|---|---|
| 1 | en | Losing duct fitting material when exported to IFC files: duct fitting material disappears in IFC | – | mep_engineer | [en-autodesk-revit-export-r025](https://forums.autodesk.com/t5/revit-mep-forum/losing-duct-fitting-material-when-exported-to-ifc-files/td-p/8736337) |
| 2 | en | IFC Export - Element Color Export as per Visibility Graphics (Filters): colours from view filters are not exported | – | contractor_site | [en-autodesk-revit-export-r041](https://forums.autodesk.com/t5/revit-ideas/ifc-export-element-color-export-as-per-visibility-graphics/idi-p/12995112) |
| 3 | en | whats the root cause of grey MEP-components in IFC: some MEP IFCs show colours and others grey; is it an MVD issue? | – | bim_coordinator | [en-gh-revit-ifc-r040](https://github.com/Autodesk/revit-ifc/issues/579) |
| 4 | en | Pipes / ducts / etc export using system material not actual material (PVC or copper) | – | mep_engineer | [en-gh-revit-ifc-r041](https://github.com/Autodesk/revit-ifc/issues/577) |
| 5 | en | Support for Export Current View Colors: export view filter colours e.g. rebar diameter colour coding | – | bim_coordinator | [en-gh-revit-ifc-r051](https://github.com/Autodesk/revit-ifc/issues/731) |
| 6 | en | Possibility to override native IFC model colors by a parameter: all IfcReinforcingBar share one material/colour so rebar groups are indistinguishable | – | structural_engineer | [en-mcl-r007](https://github.com/Autodesk/revit-ifc/issues/75) |
| 7 | en | IFC4 loses element colors compared to IFC2x3: 2x3 renders all colors in my viewer, IFC4 only some (wood beams ok, others not) | – | bim_coordinator | [en-gh-thatopen-r015](https://github.com/ThatOpen/engine_web-ifc/issues/1793) |
| 8 | en | IFC model materials/colors not applied - all geometry renders white; colours visible in BIMvision are absent in the web viewer | – | bim_coordinator | [en-gh-thatopen-r034](https://github.com/ThatOpen/engine_components/issues/745) |
| 9 | en | Material colour assigned to an element type is not applied to its occurrences (white vs red) | – | bim_coordinator | [en-gh-thatopen-r024](https://github.com/ThatOpen/engine_web-ifc/issues/2235) |
| 10 | en | Material colors from IfcMaterialDefinitionRepresentation not resolved in geometry color output; walls appear grey | – | bim_coordinator | [en-gh-thatopen-r021](https://github.com/ThatOpen/engine_web-ifc/issues/1833) |
| 11 | en | Xbim.Essentials IFC 4.3 Color Information Missing/Incorrect: style info present in the IFC2x3 export of the same model is missing in 4.3 | – | developer_programmer | [en-gh-xbim-others-r004](https://github.com/xBimTeam/XbimEssentials/issues/666) |
| 12 | en | Retrieve materials and colors: ExtractMaterialData helper returns no material for some elements | – | developer_programmer | [en-gh-xbim-others-r011](https://github.com/xBimTeam/XbimEssentials/issues/642) |
| 13 | en | ExtractElements drops occurrence IfcStyledItem on MappedRepresentations (transparent walls become beige in Solibri; Bonsai looks fine) | – | developer_programmer | [en-model-checking-r010](https://github.com/IfcOpenShell/IfcOpenShell/issues/10020) |
| 14 | en | IFC4 IfcSurfaceStyleShading.Transparency is ignored | – | developer_programmer | [en-mcl-r012](https://github.com/ThatOpen/engine_web-ifc/issues/2229) |
| 15 | en | Why is it so difficult to get colors to show up? IFCSTYLEDITEM on a proxy mass: Solibri shows colour not transparency, ArchiCAD neither | – | developer_programmer | [en-mcl-r023](https://forums.buildingsmart.org/t/why-is-it-so-difficult-to-get-colors-to-show-up/2312) |
| 16 | en | How can I control the IFC pipes colors (Revit to ArchiCAD)? hot water red/cold blue/sewage green become beige/blue/blue; tried IfcPresentationLayer | – | mep_engineer | [en-mcl-r024](https://forums.buildingsmart.org/t/how-can-i-control-the-ifc-pipes-colors-revit-to-archicad/2729) |
| 17 | en | Where and how will my colors be saved in IFC? pipe-diameter colours exported from Allplan disappear in other apps but show in a viewer | – | mep_engineer | [en-mcl-r025](https://forums.buildingsmart.org/t/where-and-how-will-my-colors-be-saved-in-ifc/1806) |
| 18 | en | Need help with Revit 2x3 ifc export, trying to figure out how the colors are assigned (tentative first post, steps and screenshot) | – | mep_engineer | [en-bsmart-r013](https://forums.buildingsmart.org/t/need-help-with-revit-2x3-ifc-export-trying-to-figure-out-how-the-colors-are-assigned/4461) |
| 19 | en | IFC Textures and Colors: Current Situation (overview of shading, rendering, textures and five assignment techniques) | – | researcher_academic | [en-mcl-r026](https://forums.buildingsmart.org/t/ifc-textures-and-colors-current-situation/2862) |
| 20 | en | Error appending type: '#4005782=IfcSurfaceStyle('ACCENT - DARK',.BOTH.,())' causes error on append | – | architect | [en-err-r031](https://github.com/IfcOpenShell/IfcOpenShell/issues/6972) |
| 21 | en | INQ: Revit family with more than one material layer: only one material is output for a structural framing family mapped to IfcWall | – | architect | [en-mcl-r006](https://github.com/Autodesk/revit-ifc/issues/929) |
| 22 | en | Layered walls in BlenderBIM: multi-layer walls (concrete, insulation, concrete); Revit IFC vs Blender round-trip shows missing wall materials in Solibri | – | architect | [en-osarch-r029](https://community.osarch.org/discussion/261/layered-walls-in-blenderbim) |
| 23 | en | ENH: Quantities of element layers: only layer thickness is exported by Revit; area and volume per layer needed for LCA | – | researcher_academic | [en-qto-r026](https://github.com/Autodesk/revit-ifc/issues/753) |
| 24 | en | How to get weight quantities from Revit? base quantities do not include weight though it is critical for costing and LCA | – | estimator_qs | [en-qto-r029](https://github.com/Autodesk/revit-ifc/issues/545) |
| 25 | en | IFC materials: how can a non-expert list every material in an IFC model given IfcMaterial, LayerSet, ProfileSet, ConstituentSet? | – | student_beginner | [p-student-r016](https://forums.buildingsmart.org/t/ifc-materials/4861) |
| 26 | en | How to check if parameters in an IFC file are compliant and editable: calculation software exports IfcMaterial in a custom property set which the BIM manager rejects | – | structural_engineer | [p-student-r005](https://community.osarch.org/discussion/432/how-to-check-if-parameters-in-an-ifc-file-are-compliant-and-editable) |
| 27 | de* | Materialeigenschaften in IFC: I exported material properties but the viewer does not show them (multilayer walls) | Exported material properties are not visible in every IFC viewer | bim_coordinator | [en-blogs-linkedin-r015](https://bim-me-up.com/materialeigenschaften-in-ifc/) |
| 28 | ru | Почему не меняется материал и тонирование колонн в Revit 2020, экспортированных из Tekla? | Why can't I change material and shading of columns exported from Tekla in Revit 2020; rebar and connections not carried | structural_engineer | [ru-dwg-other-r013](https://forum.dwg.ru/showthread.php?t=155997) |
| 29 | ru | Импорт 3D моделей из SolidWorks в Revit: как лучше перенести 3D из Солида в Ревит, теряются ли параметры и материалы | Which format moves SolidWorks models into Revit; are parameters and materials kept? | architect | [ru-dwg-other-r022](https://forum.dwg.ru/showthread.php?t=159973) |
| 30 | nl | Materiaalnamen verschillen: prefabbeton, gewapend beton, grindbeton, ihw, ihwg, tpg; computers kunnen dit niet betrouwbaar interpreteren | Material names vary; computers cannot interpret them; NAA.K.T. fixes the order | bim_manager | [nl-dutch-r023](https://www.digigo.nu/ilsen-en-richtlijnen/bim-basis-ils/praktijk/1-naa-k-t-eenduidige-materiaalbenaming) |
| 31 | zh | 自定义属性集里的材质导不进IFC | Materials are not exported to IFC through custom property sets from Revit | bim_coordinator | [zh-lightweight-review-r008](https://www.autodesk.com.cn/support/technical/article/caas/sfdcarticles/sfdcarticles/CHS/Materials-are-not-exported-to-IFC-with-custom-property-sets-from-Revit.html) |
| 32 | zh | rvt和ifc什么关系，导成ifc颜色为什么变了 | What is the relation of RVT and IFC; colours differ after RVT to IFC | student_beginner | [zh-revit-export-r019](https://www.zhihu.com/question/49455994) |
| 33 | zh | Su导进Revit材质总是丢 | SketchUp import to Revit always loses materials | architect | [zh-revit-export-r020](https://zhuanlan.zhihu.com/p/372183287) |
| 34 | zh | MAX模型导进Revit材质全没了 | Materials lost when importing a Max model into Revit | architect | [zh-revit-export-r004](https://ask.csdn.net/questions/8796533) |
| 35 | ja | IfcOpenShellのIfcCSVだとAttributeしか書き出せないので、PropertySetとMaterialも一緒にExcelへ出したい | IfcCSV only exports attributes; how do I dump attributes, property sets and materials to Excel? | bim_coordinator | [ja-japan-r001](https://zenn.dev/miyamiyaumya/articles/19a4247133dde6) |
| 36 | ja* | Error when style references to an external material: cannot use external style if the material name consists of Japanese characters | Browse External Style fails when the material name is Japanese | architect | [en-gh-encoding-r029](https://github.com/IfcOpenShell/IfcOpenShell/issues/6496) |
| 37 | en | IFCINDEXEDCOLOURMAP not implemented - colours missing after IFC to GLB | – | developer_programmer | [en-viewconv-r006](https://github.com/IfcOpenShell/IfcOpenShell/issues/2824) |
| 38 | en | IfcConvert excluding transparent geometries: can OBJ export skip transparent glass panes of windows and curtain walls? | – | developer_programmer | [en-osarch-r024](https://community.osarch.org/discussion/2804/ifcconvert-excluding-transparent-geometries) |
| 39 | nl | 4.7 Materiaal: kwaliteits- en prestatie-eisen horen niet in de materiaalnaam; NAAm_Kenmerk_Toepassing | Every object gets an IfcMaterial; no performance requirements or NL-SfB codes in names | bim_coordinator | [nl-dutch-r022](https://www.digigo.nu/ilsen-en-richtlijnen/bim-basis-ils/4-7-materiaal) |
| 40 | zh | Revit图层导出设置怎么调 | How to set Revit layer export (layer mapping) | bim_coordinator | [zh-revit-export-r027](https://www.bilibili.com/read/cv20354710/) |
| 41 | en | How does multiple IfcPresentationLayerAssignment with the same name work? one layer or two? | – | developer_programmer | [en-mcl-r028](https://forums.buildingsmart.org/t/how-does-multiple-ifcpresentationlayerassignment-with-the-same-name-work/3126) |
| 42 | en | DXF/DWG export with ifc -> cad layers translation: need to deliver IFC plus DXF/DWG; Revit has a layer translation table | – | architect | [en-viewconv-r001](https://github.com/IfcOpenShell/IfcOpenShell/issues/8009) |
| 43 | it | dall'IFC come estraggo piante e sezioni in DXF? | How to get 2D plans and sections in DXF from an IFC | architect | [it-italy-r023](https://biblus.acca.it/una-guida-completa-per-convertire-file-ifc-in-dxf/) |
| 44 | en | Error when attempting to annotate Imported IFC file from Revit: 'No annotation context Annotation/PLAN_VIEW for drawing' | – | architect | [en-osarch-r037](https://github.com/IfcOpenShell/IfcOpenShell/issues/3115) |
| 45 | en | Door swings from ArchiCAD IFCs don't show up in Revit: doors appear in 3D but are invisible in the floor plan | – | architect | [en-autodesk-revit-import-r010](https://github.com/Autodesk/revit-ifc/issues/358) |
| 46 | en | Placing elevations on sheet - one elevation behaves differently (plan, RCP, four interior elevations and axon for selected rooms) | – | architect | [en-revit-auto-r021](https://discourse.pyrevitlabs.io/t/placing-elevations-on-sheet-one-elevation-behaves-differently/1467) |
| 47 | en | Automating Filter Creation: script creates View Filters; works with instance parameters but throws object reference error with type parameters | – | bim_coordinator | [en-revit-auto-r018](https://forum.dynamobim.com/t/automating-filter-creation/108901) |
| 48 | en | REVIT 2019 LT: IFC Export - IFCSpaces are missing | – | bim_coordinator | [en-autodesk-revit-export-r015](https://forums.autodesk.com/t5/revit-architecture-forum/revit-2019-lt-ifc-export-ifcspaces-are-missing/td-p/8424409) |
| 49 | en | Is it possible to exclude areas from IFC export? | – | architect | [en-autodesk-revit-export-r016](https://forums.autodesk.com/t5/revit-architecture-forum/is-it-possible-to-exclude-areas-from-ifc-export/td-p/9513180) |
| 50 | en | Revit IFC-Export results in wrong position of Rooms: rooms placed in wrong storey in IFC | – | architect | [en-autodesk-revit-export-r043](https://forums.autodesk.com/t5/revit-architecture-forum/revit-ifc-export-results-in-wrong-position-of-rooms/td-p/12156364) |
| 51 | en | PR: Rooms exported with wrong elevation with shared coordinates | – | bim_coordinator | [en-autodesk-revit-export-r014](https://github.com/Autodesk/revit-ifc/issues/907) |
| 52 | en | PR: Room geometry shifted in IFC Exporter 25.4.40.17 + 25.4.41.5 + 26.4.0.16 + 26.4.0.32: spaces moved outside the building and wrong heights | – | bim_manager | [de-dach-r003](https://github.com/Autodesk/revit-ifc/issues/924) |
| 53 | en | IFC-Repair-Studio: areas without geometry: list of rooms with no shape in IFC, element id and guid | – | bim_coordinator | [en-sg-corenetx-r004](https://github.com/noddlesskcho/IFC-Repair-Studio) |
| 54 | en | Link IFC does not create Room/Space from IfcSpace (wants Rooms in architectural link or Spaces in MEP link) | – | mep_engineer | [en-autodesk-revit-import-r018](https://github.com/Autodesk/revit-ifc/issues/15) |
| 55 | en | IfcSpace with related BuildingStorey, how to find? searching IFC text in Notepad++ for a room by room number | – | architect | [en-bsforum-r018](https://forums.buildingsmart.org/t/5187) |
| 56 | en | PR: Qto values Net Area, and Gross Area of IfcSpace is exporting same values from Revit | – | bim_coordinator | [en-spaces-r001](https://github.com/Autodesk/revit-ifc/issues/742) |
| 57 | en | In Revit 2023 IfcSpace Qto_SpaceBaseQuantities NetFloorArea and others are not getting exported | – | bim_coordinator | [en-spaces-r013](https://github.com/Autodesk/revit-ifc/issues/529) |
| 58 | en | PR: Can't export room area to custom property set (client requirement); area objects work fine | – | bim_coordinator | [en-gh-revit-ifc-r004](https://github.com/Autodesk/revit-ifc/issues/855) |
| 59 | en | IfcSpace Predefined Type not exported: IfcExportAs=IfcSpace.EXTERNAL becomes NOTDEFINED; mandatory in Chilean public deliveries | – | reviewer_authority | [en-spaces-r015](https://github.com/Autodesk/revit-ifc/issues/247) |
| 60 | en | No way to control the generation of IfcSpaceType: not every space needs a type; Revit makes one IfcSpaceType per room | – | developer_programmer | [en-spaces-r009](https://github.com/Autodesk/revit-ifc/issues/494) |
| 61 | en | ifc5d IfcOpenShell QTO calculator never produces quantities for IfcSpace (all 13 formulas null) | – | developer_programmer | [en-qto-r015](https://github.com/IfcOpenShell/IfcOpenShell/issues/8570) |
| 62 | en | 2nd Level Space Boundary ConnectionGeometry displaced from corresponding IfcSpace (breaks BEM workflows) | – | mep_engineer | [en-spaces-r006](https://github.com/Autodesk/revit-ifc/issues/961) |
| 63 | en | Level1 boundary generation to the centre line or inside face? told centreline needed for EnergyPlus/CIBSE but areas then exceed true surface | – | researcher_academic | [en-spaces-r027](https://forums.buildingsmart.org/t/level1-boundary-generation-to-the-centre-line-or-inside-face/2724) |
| 64 | en | How to get IfcDoor relation to IfcSpace: Revit knows From and To rooms for a door | – | developer_programmer | [en-gh-revit-ifc-r046](https://github.com/Autodesk/revit-ifc/issues/91) |
| 65 | en | Broken rendering of IFC files: large block on top of roof, colors missing, glass opaque (the block is an IfcSpace) | – | student_beginner | [en-gh-thatopen-r035](https://github.com/ThatOpen/engine_components/issues/642) |
| 66 | en | IfcSpace and BlenderBim: how do I make an IfcSpace bounded by walls whose volume updates when walls change? | – | architect | [p-student-r009](https://community.osarch.org/discussion/635/ifcspace-and-blenderbim) |
| 67 | en | Problems/errors with Spaces: space made with 3D cursor lacks geometry; take-off gives zero | – | architect | [en-err-r040](https://github.com/IfcOpenShell/IfcOpenShell/issues/9470) |
| 68 | ru | Два часа выгрузки ради пустого параметра: тяжёлая модель выгружается 2 часа, зоны пропадают, площади задваиваются | Heavy model exports IFC in 2 hours; errors only show after upload to the Moscow AGR checker; zones vanish, areas doubled | bim_coordinator | [ru-autodesk-telegram-r008](https://habr.com/ru/articles/1089018/) |
| 69 | ru | площади ТЭП в xml расходятся на 20 м2, дубли не найти, как править IFC без ревита и переслать правки | TEP areas differ ~20 m2 from AGR XML; how to post-process IFC without Revit | bim_coordinator | [ru-autodesk-telegram-r010](https://habr.com/ru/articles/1100956/) |
| 70 | ru | зоны с кривыми границами в Revit считаются, а в IFC не выгружаются как тело | Zones with imperfect boundaries compute area in Revit but fail IFC export | bim_coordinator | [ru-habr-dev-r002](https://habr.com/ru/articles/1089018/) |
| 71 | ja | 部屋名・用途・床面積がIFCに出て別ビューアで読めるか。面積が合わない時は境界・計算方法・単位・版を確認 | Export one room and re-read it in another viewer; if the area differs check boundary, method, unit and edition | architect | [ja-japan-r019](https://note.com/t_note_memo/n/n8903305b00fb) |
| 72 | nl | Ruimte: toegankelijk, minimaal 1,5 m netto hoogte; Name (toilet) en ObjectType (toiletruimte); zones voor woning, brandcompartiment | IfcSpace needs min 1.5 m net height; Name plus ObjectType; IfcZone for dwelling type | architect | [nl-dutch-r021](https://www.digigo.nu/ilsen-en-richtlijnen/bim-basis-ils/4-1-ruimten) |
| 73 | en | Cobie export - systems tab empty: 214 systems in Bonsai but the Systems tab in the spreadsheet is empty | – | facility_manager | [en-gh-ifcopenshell-r028](https://github.com/IfcOpenShell/IfcOpenShell/issues/6068) |
| 74 | nl | Ref #4 [installaties]: Waarom geen verwijzing naar Systems (IfcDistributionSystem)? NL/SfB-codes sluiten niet geheel aan op de praktijk | Why no reference to IfcDistributionSystem; NL-SfB does not fully match practice for installations | mep_engineer | [nl-dutch-r014](https://github.com/nl-digigo/imwo/issues/52) |
| 75 | en | Revit cannot export properties of an IfcSystem (Revit's system browser) | – | bim_manager | [en-mep-r005](https://github.com/Autodesk/revit-ifc/issues/523) |
| 76 | en | INQ: Override IfcDistributionSystem of elements | – | bim_coordinator | [en-mep-r007](https://github.com/Autodesk/revit-ifc/issues/900) |
| 77 | en | MEP System Classification: MEP coordinator colours by system abbreviation | – | bim_coordinator | [en-mep-r034](https://forums.buildingsmart.org/t/mep-system-classification/2464) |
| 78 | en | Space data depending on zone: five candidate options (psets, classification, proxies, extra zone, IfcAsset) | – | facility_manager | [en-spaces-r028](https://forums.buildingsmart.org/t/space-data-depending-on-zone/4434) |
| 79 | en | What are the various use cases of IfcGroup? | – | student_beginner | [p-student-r007](https://community.osarch.org/discussion/1827/what-are-the-various-use-cases-of-ifcgroup) |
| 80 | en | PR: Cannot export model Group as IfcBuiltSystem | – | bim_coordinator | [en-mep-r038](https://github.com/Autodesk/revit-ifc/issues/829) |

Language spread (80 rows): en 61, ru 5, zh 5, nl 4, ja 3, it 1, de 1 (the "lang" column shows the record language). Non-English rows are fewer than in the versions file because the underlying forums for these topics (Revit exporter and web-ifc issues) are English; the synthetic prompts below cover more languages.

## Ready test prompts

Synthetic. Curated from the KB's synthetic records (record id in the "type" column); weak or repetitive ones were rewritten to sound like a real person with a deadline or an annoyance. Unless noted, an IFC (or Revit project) must be loaded.

| # | lang | prompt | type | difficulty | expected behavior |
|---|---|---|---|---|---|
| 1 | en | why is everything white?? find which elements have no IfcSurfaceStyle anywhere (geometry, material, type) | query_model_data (en-gh-thatopen-s003) | medium | Check IfcStyledItem on representations, IfcMaterialDefinitionRepresentation and type-level styles; list elements with no colour; say whether the colour was ever written |
| 2 | en | same revit model exported 2x3 and 4 and the colors differ in my viewer. whats different in the two files | query_model_data (en-gh-thatopen-s013) | hard | Compare style counts and material-style linkage in both files; match by GlobalId; report differences |
| 3 | en | my cavity walls show opaque beige, they were see-through in archicad. style issue? | query_model_data (en-model-checking-s006) | hard | Inspect IfcStyledItem on occurrence and type representation maps and material styles; report which carries transparency; state the 0 = opaque convention |
| 4 | zh | revit导出ifc后管道颜色都是灰的，系统颜色没带出来，用的哪个设置？ | troubleshoot_export (zh-mep-s008) | medium | Explain colour comes from materials/by-category and not view filters; guide to set system material and check IfcStyledItem |
| 5 | es | importé el IFC de Archicad en Revit y se perdieron los colores, revisa si los estilos de superficie están en el archivo | validate_check (mx-mcl-s004) | medium | Check IfcStyledItem/IfcSurfaceStyle on shapes and materials; report whether the data exists so loss is import-side |
| 6 | de | wie krieg ich die Farben von Archicad IFC in Revit rüber? Oberflächen sind alle grau | how_to (mx-mcl-s015) | medium | Explain Revit import ignores styles, link vs open, material mapping; check the file for styles first |
| 7 | pt | pinta todas as lajes de cinza claro no modelo, cria o estilo de superfície e liga no material | modify_model_data (mx-mcl-s005) | hard | Create IfcSurfaceStyle with shading (light grey), assign to material or slabs, save as new file, report what was linked |
| 8 | ko | IFC 열면 유리가 불투명하게 나오는데 투명도 값이 파일에 들어있는지 확인해줘 | troubleshoot_viewing (mx-mcl-s009) | medium | Check IfcSurfaceStyleShading Transparency on glass; explain convention and viewer support |
| 9 | en | where is the colour of a wall actually stored in IFC? material or shape? show me for the selected one | understand_concept (mx-mcl-s016) | easy | Trace styled items and material definition representation; explain precedence (shape style over material style) |
| 10 | fr | mon obj exporté depuis l'ifc n'a plus aucune couleur, pourquoi ? | troubleshoot_viewing (fr-viewconv-s010) | medium | Explain colour maps vs mtl, check styles present in the file, re-export |
| 11 | en | pipes show material = system name (HOT WATER) not copper. can you list pipes and what material they actually have | query_model_data (en-eng-s003) | medium | Read material associations on IfcPipeSegment, list names, point out system-name materials, suggest where real material may be |
| 12 | en | do the pipes have the real material (PVC/copper) or just the system material name like SEWER? list by system | query_model_data (mx-mcl-s011) | medium | Compare material names with system names, report mismatches per system |
| 13 | ru | найди элементы без материала, а у стен покажи слои и толщины | validate_check (ru-dwg-revit-s011) | medium | Find elements without material association; for walls list layer set with thickness; state paths checked |
| 14 | zh | 帮我查下这个IFC里墙的材质层有没有丢，是IfcMaterialLayerSetUsage还是只剩一个IfcMaterial | validate_check (mx-mcl-s003) | medium | Per wall report association kind (LayerSetUsage, ConstituentSet, single IfcMaterial), counts, walls reduced to one material |
| 15 | ru | у типов стен материал есть а у самих стен нет, цвет в просмотрщике белый, проверь | validate_check (mx-mcl-s012) | hard | Compare type vs occurrence association, list occurrences lacking material, explain viewer fallback |
| 16 | it | ci sono materiali duplicati con lo stesso nome nel modello, uniscili e tieni lo stile colore | modify_model_data (mx-mcl-s010) | hard | Find duplicate IfcMaterial names, merge preserving surface styles, save new file, report merged count |
| 17 | nl | materiaalnamen volgens NAA.K.T.? geef afwijkingen, en welke objecten hebben geen IfcMaterial | validate_check (nl-dutch-s008) | hard | List materials, flag names with NL-SfB codes or performance data, list objects without material; ask which rule set applies |
| 18 | en | what concrete grades are on the columns and beams? give counts per grade, need to match the structural spec | query_model_data (en-uk-anz-india-s014) | medium | Read IfcMaterial on columns/beams, parse grade from name or pset, tabulate, flag missing material |
| 19 | en | for every layered wall, replace the layer set with one material equal to the thickest layer, save a new file | automate_batch (mx-mcl-s013) | hard | Destructive edit: confirm, edit via API on a copy, summarise changes; warn about lost layers and quantities |
| 20 | en | append type is failing, find IfcSurfaceStyle with empty Styles | validate_check (en-err-s004) | medium | List IfcSurfaceStyle with empty style list (invalid), offer fix or delete |
| 21 | es | dame el volumen por material de todos los muros, por capa, para el presupuesto | extract_quantities (mx-mcl-s017) | hard | Aggregate layer thickness x area per material per wall; label as computed (Revit exports only thickness); report totals |
| 22 | ru | объём бетона по этажам, только монолит, ВОР в эксель. если в модели нет Qto - скажи прямо | extract_quantities (ru-aimcp-s011) | medium | Aggregate volumes per storey from Qto or compute, export, flag missing quantities |
| 23 | zh | 把IFC里的图层名字列出来，每个图层有多少构件，导出表格 | query_model_data (mx-mcl-s014) | easy | Enumerate IfcPresentationLayerAssignment, count items, output table |
| 24 | de | zeig mir alle IfcPresentationLayerAssignment mit Anzahl Objekte, Layer mit gleichem Namen bitte markieren | validate_check (mx-mcl-s006) | easy | List layer assignments with item counts and flag duplicate names |
| 25 | ru | нужен dwg из этого ифс, чтоб слои по классам, а то в автокаде одним куском | convert_format (ru-viewconv-s011) | hard | Map classes to layers, export DWG/DXF or explain route and limits; ask for layer names |
| 26 | en | why wont annotation work on this revit ifc, no annotation context? add it so I can draw plans | modify_model_data (en-osarch-s010) | medium | Check geometric representation contexts, add Plan/Annotation contexts if absent, save new file |
| 27 | en | rename all floor plan views to 'L{level number}_{old name}' and skip anything already prefixed (Revit) | automate_batch (en-revit-auto-s001) | medium | List plan views, compute names from level, skip prefixed, avoid duplicates, apply in one transaction, report old to new |
| 28 | en | before issue tonight - list rooms not placed / not enclosed / redundant and doors with no tag. excel pls | validate_check (en-revit-auto-s003) | medium | Query rooms with zero area and no location, redundant warnings, untagged doors; grouped lists with element ids; offer Excel/CSV |
| 29 | en | rooms arent showing up in the ifc at all, what setting am I missing | how_to (en-spaces-s008) | easy | Explain room/space export setting, "export rooms in 3D views" with visible-only export, phase, unplaced/unenclosed rooms, IfcExportAs |
| 30 | ru | глянь какие помещения из ревита не выгрузились в ифс, в модели вижу только 40 IfcSpace | validate_check (ru-spaces-s010) | medium | Count IfcSpace, compare with supplied room list, find missing by number/name, note unplaced rooms |
| 31 | en | some rooms look shifted vs the walls after export, can you find spaces whose bbox is not inside the storey/building footprint | validate_check (en-spaces-s004) | hard | Compute space bounding boxes vs walls, flag outliers with offsets, mention exporter and shared-coordinate causes |
| 32 | en | gross and net floor area look identical on all my rooms, is that an export bug? check the model | validate_check (en-spaces-s002) | medium | Compare Gross and Net per space, count equal values, explain exporter limitation |
| 33 | en | which IfcSpaces have no NetFloorArea in Qto_SpaceBaseQuantities? list name + level | query_model_data (en-spaces-s001) | easy | Iterate spaces, list missing quantities with storey; offer to compute from geometry |
| 34 | ru | у меня площадь по зонам не сходится с RUS_Area, посчитай по геометрии IfcSpace и покажи где расхождение больше 0.5 м2 | validate_check (ru-habr-dev-s004) | hard | Compute geometric area, compare with attribute, list deviations above threshold, note zones without solid geometry |
| 35 | ja | IFCの面積がRevitの集計表と合わない。単位か境界の問題？部屋ごとに差を出して | query_model_data (ja-japan-s010) | hard | Report project length and area unit, compare Net vs Gross per space, list rooms with differences |
| 36 | de | prüf mal ob jeder Raum eine Raumnummer und NGF hat, sonst klappt der CAFM-Import nicht | validate_check (de-cobie-s009) | easy | List IfcSpace missing number, long name or NetFloorArea; duplicate room numbers |
| 37 | zh | 幫我檢查這個IFC每層樓的樓地板面積總和，跟送審圖面積表對不對得上 | validate_check (zh-tw-hk-s001) | hard | Sum IfcSpace/IfcSlab area by storey, compare with the given table, list mismatches; ask which definition the table uses |
| 38 | ja | 確認申請用のIFCです。居室の天井高が2.1m未満の部屋と面積を一覧にしてください | validate_check (ja-permit-s010) | hard | List IfcSpace with height and area, filter by 2.1 m; state which height property was used; do not assert code clause |
| 39 | en | all IfcSpace on level 2 with area, and is any fire compartment over 1000 m2? name the spaces | comply_regulation (en-permit-s004) | hard | Read areas from Qto or geometry, group by zone/compartment, compare to threshold; ask how compartments are modelled |
| 40 | en | set Pset_SpaceCommon.NetFloorArea on all spaces from their Qto area, then save as new file | modify_model_data (en-stackoverflow-s005) | medium | Copy Qto NetFloorArea into the pset for each space, write a new file, report counts |
| 41 | en | furniture sits under storeys not spaces, FM says rooms are empty. confirm? | validate_check (en-blogs-linkedin-s009) | medium | List furnishing containers, count under storey vs space, report |
| 42 | en | do we have IfcRelSpaceBoundary2ndLevel in this file? how many per space, any space with zero | query_model_data (en-spaces-s003) | medium | Count boundaries per IfcSpace, flag spaces with none, report level 1st/2nd |
| 43 | en | show all IfcZones and which spaces are in each, flag spaces in more than one zone | query_model_data (en-spaces-s005) | easy | Query group relation for IfcZone, list members, flag multi-membership and empty zones |
| 44 | ko | 존에 안 들어간 실(IfcSpace) 찾아줘 | validate_check (ko-spaces-s017) | easy | List spaces not in any IfcZone |
| 45 | en | which pipes and fittings arent in any IfcSystem? need it before the coord meeting | validate_check (en-eng-s002) | medium | Find flow segments/fittings without group assignment to a system, list names and levels |
| 46 | ru | посчитай длину воздуховодов по системам, в ифс они в IfcSystem вроде | query_model_data (ru-eng-s009) | medium | Group IfcDuctSegment by system, sum lengths (quantities or geometry), table, note missing system links |
| 47 | en | my cobie systems sheet is empty but theres loads of ductwork, whats missing in the model | query_model_data (en-cobie-s002) | hard | Inspect systems, group assignments and component types; explain that systems need components with types; list unassigned MEP elements |
| 48 | en | whats served by AHU-03? list components and the rooms | query_model_data (en-fmor-s005) | hard | Traverse system membership and the served-spaces relation; list components with tags and served spaces; say if the relation is absent |

## Edge cases and traps for MCP testing in this area

**Materials and colours**
- `IfcMaterial` has no colour. An answer such as "the material is red" without naming the `IfcSurfaceStyle` and where it hangs is unsupported.
- Three colour sources conflict: style on the shape, style via material definition representation, style on the type. The occurrence beats the type; the shape style beats the material style (per an implementer agreement). A test model should deliberately carry different colours in two places.
- Transparency is inverted vs alpha: 0.0 opaque, 1.0 fully transparent. A write tool that treats it as alpha makes glass opaque.
- "All white/grey" has two opposite causes: no style was ever written (exporter) or the style exists but the viewer ignores it. Always check the file first.
- Invalid and awkward data: `IfcSurfaceStyle` with empty style list (invalid), two styled items on one material (shading plus fill), a style not linked to the shape (no `Item`), duplicate materials (hundreds), material names in Cyrillic/CJK.
- Revit view filters and graphic overrides are not exported; asking an MCP to "export the colours of the current Revit view" cannot succeed in IFC and should be refused with the alternative (set the material colour).
- MEP: the "material" can be the system name; check against the system list before reporting it as the real material.
- Elements without a material can still have one via type, profile, constituent or layer; openings and virtual elements must not have one at all.
- Layer rules: `sum(LayerThickness)` vs body thickness, zero-thickness layers are legal, a layer set usage on a type is invalid; thickness unit is the project's length unit (mm vs m trap).
- Per-layer area and volume are not in Revit's IFC; any such number must be labelled computed. Weight is not in base quantities.
- Destructive requests (merge duplicates, rename, replace layer set by one material, paint slabs): the assistant should write a new file or ask for confirmation, and report counts; losing layers silently is a failure.

**Layers and drawings**
- "Layer" is ambiguous: material layer, presentation layer, CAD layer, Revit view/filter. A good assistant asks.
- Presentation layers are display grouping; same-name layers are not forbidden by a uniqueness rule, so duplicates should be flagged not merged.
- View, sheet, crop-region and filter tasks need a Revit-connected tool; an IFC-only server cannot do them and should say so. Test for a numbering collision (A101 already exists) and for already-prefixed names.
- IFC from Revit often has no Annotation context; a drawing tool must add it or explain.

**Spaces, rooms, areas**
- Room, Area and Mass can all become `IfcSpace`. Counting "rooms" from IfcSpace may include areas and masses. Areas may appear with an elevation offset.
- The room list the user gives you may not match: unplaced, unenclosed and redundant rooms exist in Revit but have no geometry in IFC.
- Space boundaries default to None in Revit's exporter; "which walls bound this room" has no answer in a file exported with the default.
- Walls bound rooms, they are not contained in them; furniture can be contained in the storey rather than the space.
- Areas: Net vs Gross identical, missing in some Revit versions, planned vs measured (`Pset_SpaceCommon.GrossPlannedArea` is not a measurement), units (m² vs mm²), core-centre vs finish-face boundaries. The assistant must say the source and definition, and must not sum a column with holes.
- Area numbers have legal weight (permit tables, TEP, rent); the IfcOpenShell QTO calculator deliberately leaves space formulas empty. Do not auto-compute an "official" area without saying so.
- Threshold requests (door width under 900, ceiling height under 2.1 m, compartment over 1000 m², corridor width) need the property named, the unit stated and the code clause supplied by the user; the assistant must not invent the regulation.
- Shifted rooms: compare to walls on the same storey; known causes are shared coordinates with survey-point levels and specific exporter builds.
- Open IFC converts spaces to rooms, Link IFC does not; do not promise native rooms from a link.
- Predefined type: IFC2x3 only has USERDEFINED/NOTDEFINED for spaces, so "all spaces must have a predefined type" cannot be satisfied there; one IfcSpaceType per room is Revit's behaviour.
- Writing area into a custom pset: allowed; overriding the standard `Qto_` sets is not (immutable by design in Revit).

**Zones and systems**
- Zone is overloaded: IfcZone, IfcSpatialZone, fire compartment (no own entity), Archicad/Revit "zone" (often a room). Ask which.
- A space can sit in several zones; membership must be read through the group relation. Zone GlobalIds from Revit virtual zones are not stable.
- Empty COBie Systems sheet is usually a data problem (components without types, no assignments), not a tool failure; the assistant should explain from the data.
- "Not in any system" lists depend on what counts as MEP: pipes, ducts, fittings, terminals, equipment; define the class list in the answer.
- "Whats served by X" needs a served-spaces relation that many exports do not write; absence must be reported as absence, not as "serves nothing".
- Export filters (visible elements only) can drop circuits and systems, so an incomplete system list may be an export artefact.
- Assigning orphans to systems is a write action and needs confirmation; classification abbreviations (SA, EA) should be taken from the user, not guessed.

## Related docs

- [Materials, classification, types, colours/styles and layers](../../01_ifc_basics/07_materials_classification_types_styles.md)
- [Spatial structure and relationships (spaces, zones, systems, boundaries)](../../01_ifc_basics/04_spatial_structure_and_relationships.md)
- [Properties, quantities and property sets (Qto_SpaceBaseQuantities, Pset_SpaceCommon)](../../01_ifc_basics/05_properties_quantities_psets.md)
- [Domains: MEP, structural, infrastructure, 4D/5D, FM (COBie, systems)](../../01_ifc_basics/08_domains_mep_structural_infra_4d5d_fm.md)
- [Revit IFC export reference (rooms, material psets, known problems)](../../03_software/revit/ifc_export_reference.md)
- [Revit IFC import and link reference (Open vs Link, IfcSpace as generic model)](../../03_software/revit/ifc_import_link_reference.md)
- [Viewers, checkers, CDE and converters](../../03_software/viewers_checkers_cde_converters.md)
- [Open-source libraries and toolkits](../../04_open_source/libraries_and_toolkits.md)
- [Glossary (multilingual)](../../08_glossary/glossary_multilingual.md) and [abbreviations](../../08_glossary/abbreviations.md)
- Sibling topic file: [IFC versions and MVDs, text encoding, GUIDs and change tracking](./versions_mvd_encoding_guid.md)
- Other topic files: [Revit export and class mapping](./revit_export_and_class_mapping.md), [Properties and parameters](./properties_and_parameters.md), [Quantities, cost, schedule](./quantities_cost_schedule.md), [MEP, structural, rebar](./mep_structural_rebar.md)
