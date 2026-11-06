# Speckle, SketchUp, Rhino/Grasshopper, FreeCAD communities: IFC questions
Cell: en-speckle-sketchup-rhino-freecad · Languages: English · Collected: 2026-11-06 · Records: 40 real / 15 synthetic · Communities covered: forums.sketchup.com, discourse.mcneel.com, GitHub (FreeCAD/FreeCAD, specklesystems/speckle-server, speckle-sharp)

Note: the web search budget ran out, so threads were found through Discourse search.json (SketchUp, McNeel) and the gh CLI. 17 real records have evidence "page"; the rest are "snippet" (title and blurb from search results).

## Top themes (ranked by frequency)
- Everything exports as IfcBuildingElementProxy; how to assign proper IFC classes (SketchUp classification, VisualARQ/GeometryGym layers).
- Custom properties and Psets (UserText, Dynamic Component attributes, Ruby metadata) are not written to IFC.
- Georeferencing: IfcSite lat/long, IfcProjectedCRS, IfcMapConversion, EPSG codes, models appearing far from origin.
- Wrong scale or units on import into Revit (metre vs foot, mm vs m).
- Spatial structure and hierarchy: IfcProject/Site/Building/Storey from Outliner or layers; multiple buildings break.
- Viewer disagreement: which viewer to trust, how to validate (BIMvision, Solibri, BIMcollab Zoom, Trimble Connect).
- Geometry type: faceted B-rep or tessellation versus editable extrusions in ArchiCAD/Revit.
- Missing quantities (IfcBaseQuantities, IfcElementQuantity), also in Speckle's IFC importer.
- Materials and colours lost, edge colours, layer colours.
- Rhino has no native IFC; need paid plugins (VisualARQ, Geometry Gym, BEAM) and a Mac/Rhino 8 gap.
- Round-tripping and information loss; importing IFC into Grasshopper efficiently (block instances).
- Large or corrupt files, hidden or empty objects included in export.
- FreeCAD native IFC bugs: openings, spatial structure, import failing on material layers.
- Speckle IFC file import service: upload failures, missing relations, self-hosting.

## What people want (the goals behind the questions)
- Hand off a model made in a non-BIM tool (SketchUp, Rhino) to Revit/ArchiCAD/Solibri without it being unusable.
- Make the IFC pass rule-based checking, council or compliance review, quantity takeoff and structural analysis.
- Control exactly which IFC class, Pset, quantity, material and location each object gets, ideally automated (Ruby, Grasshopper, templates).
- Keep georeference and units right so models line up in federated coordination.
- Know which free or cheap tool does the job, and whether an AI's claim about a tool is true.
- Round-trip and edit IFC without losing data; get geometry and data into Speckle for analytics.

## How people write here
Register: informal-technical forum posts, usually 2-6 sentences, often a numbered list of questions at the end; GitHub issues follow templates with repro steps and pasted tracebacks. Context given: software and version (SketchUp 2023 Pro, Revit 2022, Rhino 8, FreeCAD 1.1), IFC version, the viewer used. Context often omitted: the file itself, units, export options. Tone: mildly frustrated or confused; some strongly critical ("not BIM-ready"); thanks at the end.
- Jargon: "proxy" (IfcBuildingElementProxy), "Pset", "UserText", "Outliner", "ggIfc/GG", "Dynamic Components", "Qto".
- Spellings: "Sketchup", "Ifc", "IFC2x3 / IFC 2x3 / IFC4", "geo-referenced", "Visual Arq".
- Code-switching: French/Dutch users writing English, citing EPSG 2154, NL-SfB, Lambert 93.
- Fragments: "Geometry not exported for IfcSite"; "only one building element proxy"; "comes in at about one third size"; "Can I automate an IFC export with Ruby?"; "unreadable IFC".
- Some now cite AI chatbots as the origin of the misunderstanding (Rhino 8 "has an IFC manager").

## Local ecosystem
- SketchUp: native IFC export (2x3, IFC4; Tessellation or Body options), IFC Manager extension (Dutch NL-SfB focus), Trimble Connect, TrimBIM. https://forums.sketchup.com
- Rhino: no native IFC; VisualARQ (Asuni), Geometry Gym (ggRevitIFC, IfcTemplatePath), BEAM (MKS), Tessera converter, IfcHopperShell, Rhino.Inside.Revit. https://discourse.mcneel.com
- FreeCAD BIM workbench with IfcOpenShell, native IFC mode, strict IFC mode. https://github.com/FreeCAD/FreeCAD
- Speckle: connectors, fileimport-service, archived speckleifc importer, web-ifc. https://github.com/specklesystems/speckle-server
- Viewers/checkers: BIMvision, BIMcollab Zoom, Solibri, Open IFC Viewer, Blender BIM, TU Delft CRS tool, georeference-ifc, IfcOpenShell.
- Standards: buildingSMART IFC2x3/IFC4/IFC4x3, IfcProjectedCRS/IfcMapConversion.

## Notable sources
- https://forums.sketchup.com/t/sketchup-ifc-export-is-not-bim-ready/350104 (2026 critique and Trimble reply)
- https://forums.sketchup.com/t/ifc4-export-from-sketchup2023-pro/228565 (single proxy; viewers)
- https://forums.sketchup.com/t/how-to-export-ifc-files-from-sketchup-2024-including-ifcprojectedcrs/295229
- https://forums.sketchup.com/t/ifc-export-wrong-scale/212339
- https://forums.sketchup.com/t/ifc-structural-model-export-from-sketchup-to-archicad-and-use-it-for-bim-process/344695
- https://forums.sketchup.com/t/export-to-ifc-with-ifcbasequantities/235164
- https://forums.sketchup.com/t/corrupt-ifc-export/254366
- https://forums.sketchup.com/t/ifc-export-geometry-not-exported-for-ifcsite-and-ifcbuilding/3478
- https://forums.sketchup.com/t/export-and-import-ifc-colors/54101
- https://discourse.mcneel.com/t/ifc-for-rhino8/219225
- https://discourse.mcneel.com/t/grasshopper-ifc-import-optimizations/204628
- https://discourse.mcneel.com/t/export-georeferenced-ifc-file/142727
- https://discourse.mcneel.com/t/ifc-round-tripping/210129
- https://discourse.mcneel.com/t/export-ifc-from-rhino-with-custom-properties/154156
- https://discourse.mcneel.com/t/problem-exporting-from-rhino-8-to-ifc/212641
- https://discourse.mcneel.com/t/importing-ifc-to-revit-2022-from-rhino-shows-no-objects-inside/140503
- https://discourse.mcneel.com/t/geometry-gym-revit-elements-change-position-after-ifc-import/187724
- https://github.com/FreeCAD/FreeCAD/issues/21399
- https://github.com/FreeCAD/FreeCAD/issues/30614
- https://github.com/FreeCAD/FreeCAD/issues/25529
- https://github.com/FreeCAD/FreeCAD/issues/32744
- https://github.com/specklesystems/speckle-server/issues/5773
- https://github.com/specklesystems/speckle-server/issues/4943
- https://github.com/specklesystems/speckle-sharp/issues/1261

## Gaps
- Web search quota exhausted after the first calls; no WebSearch-based discovery was possible.
- speckle.community returned HTTP 403 for all fetches, so no Speckle forum threads were read; Speckle coverage comes only from GitHub issues.
- forum.freecad.org blocked by Anubis bot protection; FreeCAD coverage comes only from GitHub issues (not forum phrasing).
- 22 real records are snippet-level (title and blurb only). Reddit, YouTube and Stack Overflow not covered. No suspicious sites encountered.
