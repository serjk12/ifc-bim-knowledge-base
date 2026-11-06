# Dynamo and pyRevit forums: IFC automation questions
Cell: en-dynamo-pyrevit · Languages: English (some posters are non-native, German and Portuguese/Brazilian context) · Collected: 2026-11-06 · Records: 56 real / 17 synthetic · Communities covered: forum.dynamobim.com (tag "ifc" and IFC export search), discourse.pyrevitlabs.io (search "IFC")

## Top themes (ranked by frequency, 8-15 bullets, one line each)
- Batch / unattended IFC export from Revit with Dynamo or pyRevit (multi-file, per view, per level, overnight, CLI).
- Export node pitfalls: "Export IFC in Document" vs active-document nodes giving empty or duplicated IFCs.
- Custom export setups and options via Python `AddOption` (IFCFileType, ActivePhase, classification, tessellation, Psets).
- Class mapping and `IfcExportAs` / `IFC_EXPORT_ELEMENT_TYPE_AS` set by script; mapping tables ignored by API export.
- Property sets: empty, missing or user-defined Psets after export; base quantities.
- IFC GUID handling: reading, storing, stability, GUID vs UniqueId/ElementId, Civil 3D.
- Revit-version breakage of exporter API (namespace moves, Revit 2027, add-in DLL versions, IronPython 3 vs PythonNet).
- Importing / linking IFC: coordinates and base point, reading data from linked IFC, hiding IFC elements via filters.
- Geometry that does not export: Dynamo-made objects, Direct Shapes, ceiling grids, rooms/IfcSpace, IfcRelSpaceBoundary.
- Colours/materials not carried into IFC; curtain walls on wrong levels.
- Civil 3D / infrastructure IFC (corridors, surfaces, IFC 4.3 command).
- IfcOpenShell and LLM/AI tooling beside Revit (IFCNodes, LangChain in pyRevit).
- Tool choice: Dynamo vs dedicated exporters (RTV Xporter, ProSheets).

## What people want (the goals behind the questions)
- Press one button (or a scheduler) and get correct IFC files for many models, views or levels without manual clicking.
- Make the scripted export identical to the manual dialog (same mapping, Psets, classification).
- Keep stable identifiers and write custom IDs/properties into elements for downstream tools.
- Get data out of IFC links (quantities, names) and place IFC links correctly.
- Understand why a viewer shows empty data and whether the model or the viewer is at fault.
- Survive Revit upgrades without rewriting export scripts.

## How people write here (register, typical length, jargon/slang with translations, misspellings of terms, code-switching, openers/closers, what context they give or omit, emotional tone)
- Short, polite forum posts; often 3-8 sentences plus screenshot or code. Greeting and thanks are common ("Hi all", "Thanks in advance").
- Revit and IFC versions are frequently omitted; a reply asks for them later.
- Many non-native writers; German names (Leerrohr) and German UI strings leak in.
- Jargon: "node", "lacing", "custom node", "Genius Loci", "AddOption", "mapping table", "Pset", "LOI", "export setup", "proxy".
- Misspellings seen: "Costum Export Setup", "Handeling Revitparameters", "Ifc".
- Tone mostly neutral to apologetic; frustration appears after hours of failed tests.
- Fragments: "script produced empty IFC files"; "does not respect the mapping"; "weird error, cheers"; "not sure if this is possible".

## Local ecosystem (official/government bodies, regulations and standards, local software, enthusiasts/educators, open-source projects encountered, with URLs)
- buildingSMART IFC and Autodesk Revit IFC exporter (open source, GitHub Autodesk/revit-ifc).
- Dynamo packages: Genius Loci (Export IFC), Orchid, Clockwork, Archilab, Bird Tools Multi Player, dyn2ifc (GeometryGym based), IFCNodes: https://forum.dynamobim.com/t/ifcnodes-ai-powered-ifc-toolkit-for-dynamo/113569
- pyRevit: https://discourse.pyrevitlabs.io/ ; CLI automation.
- IfcOpenShell / Bonsai: https://ifcopenshell.org/
- Commercial batch exporters mentioned: RTV Xporter Pro, ProSheets.
- Viewers/checkers: Solibri, Navisworks, Blender BIM.
- The Building Coder blog (Revit API IFC GUID and export samples).

## Notable sources (15-30 best URLs, one line each)
- https://forum.dynamobim.com/t/ifc-export-node-return-an-empty-ifc/82822 - empty IFC, Export IFC in Document
- https://forum.dynamobim.com/t/are-anyone-able-to-export-ifc-using-dynamo-in-revit-2027/115000 - Revit 2027 breakage
- https://forum.dynamobim.com/t/ifc-export-settings-ifcfiletype/91626 - IFCFileType option
- https://forum.dynamobim.com/t/completely-automated-ifc-export-on-remote-computer/30482 - nightly export
- https://forum.dynamobim.com/t/unrecoverable-error-during-ifc-export-using-dynamo/113291 - decimal comma bug
- https://forum.dynamobim.com/t/ifc-export-does-not-respect-mapping/112777 - mapping ignored
- https://forum.dynamobim.com/t/ifc-batch-export-through-phases/31076 - ActivePhase option
- https://forum.dynamobim.com/t/ifc-export-by-dynamo-internal-revit-property-set/22301 - Psets option
- https://forum.dynamobim.com/t/store-ifc-guid-in-elements-without-exporting-ifc/24284 - GUID storage
- https://forum.dynamobim.com/t/handle-ifc-guid-in-civil-3d/80717 - Civil 3D GUID
- https://forum.dynamobim.com/t/set-export-type-to-ifc-as-parameter/110128 - IfcExportAs by script
- https://forum.dynamobim.com/t/move-linked-ifc-to-right-coordinate-system/79767 - link placement
- https://forum.dynamobim.com/t/ifc-revitlinkinstance-collect-data-from-ifc-elements/106608 - data from IFC link
- https://forum.dynamobim.com/t/export-ifcrelspaceboundary-room-boundaries/91608 - space boundaries
- https://forum.dynamobim.com/t/hide-ifc-element-in-a-view/79055 - IFC element filters
- https://forum.dynamobim.com/t/ifcnodes-ai-powered-ifc-toolkit-for-dynamo/113569 - LLM + IFC
- https://forum.dynamobim.com/t/duplicate-ifc-export-over-multiple-documents/115062 - multi-document pitfalls
- https://forum.dynamobim.com/t/exporting-ifc-from-civil-3d-with-dynamo/114735 - Civil 3D IFC 4.3
- https://discourse.pyrevitlabs.io/t/share-my-code-for-export-multiple-views-to-ifc/2553 - pyRevit multi-view export
- https://discourse.pyrevitlabs.io/t/ifc-setup-loading-fails/9920 - config loading failure
- https://discourse.pyrevitlabs.io/t/cliifc-export-does-not-output-ifc-file/8441 - CLI export
- https://discourse.pyrevitlabs.io/t/access-to-ifcexporter/330 - reaching the IFC exporter DLLs
- https://discourse.pyrevitlabs.io/t/ifcopenshell-how-to-start/8204 - IfcOpenShell newcomers
- https://discourse.pyrevitlabs.io/t/how-to-use-python-package-like-langchain/2673 - packages in CPython

## Gaps (what you could not access or find; suspicious sites skipped)
- WebSearch quota was exhausted at the start, so no web searches were run; discovery relied on forum search.json and tag pages fetched directly (Dynamo forum search 50 results, tag page 1; pyRevit search 32 results). The 25-search target was not met; about 58 fetches were made.
- Only the first page of Dynamo tag "ifc" and no pages 2+ were read; IFC import to Revit via Dynamo and the "IFC parameters" angle are thinner than export.
- pyRevit forum has no ifc tag (404); the community is small and IFC threads are few.
- Reply text was summarised by the fetch tool, so exact phrasing is paraphrased; "inspired_by" ids in synthetic records are approximate links to the most related real records.
- No suspicious sites were encountered. No GitHub issues were searched.
