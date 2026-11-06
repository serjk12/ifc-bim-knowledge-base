# Deutschland/Österreich/Schweiz: Foren: IFC Export Probleme, Durchbruchsplanung, BIM Deutschland

Cell: de-dach · Languages: German (real user posts found were mostly English, from DACH-based users) · Collected: 2026-11-06 · Records: 28 real / 16 synthetic · Communities covered: GitHub Autodesk/revit-ifc issues, BIM Deutschland (official), BIMpedia (title only)

IMPORTANT LIMITATION: the WebSearch budget was exhausted before the first search ran (all 4 attempts refused). Only direct WebFetch and the GitHub CLI worked. The German forums (cad.de, Autodesk DE forum, Graphisoft DE, Allplan) were not reachable or not findable without search. This cell is therefore thin on genuine German forum voice. The German phrasing in the synthetic records is based on general knowledge of German BIM jargon, not on quoted posts.

## Top themes (ranked by frequency)
- Revit IFC exporter regressions between exporter builds (spaces shifted, openings lost)
- Openings and Durchbrüche missing or wrong (shafts, floor openings, joined beams)
- Class mapping: elements ending up as IfcBuildingElementProxy, IfcExportAs not working
- Custom (shared) parameters vs built-in parameters in property sets and the mapping txt file
- Coordinates: shared coordinates, survey point / base point, True North rotation, room elevation offsets
- Several Revit levels per storey (German practice: OKFF / OKRD) vs one IfcBuildingStorey
- GUID instability between exports
- Base quantities missing or wrong (Qto)
- Classification systems other than Uniformat
- IDS checking and AIA/BAP/MVD requirements from clients
- Importing IFC into Revit (placement, windows offset)

## What people want (the goals behind the questions)
- Reliable openings so MEP and structural can do Durchbruchsplanung from the architect model
- Control over IFC class, spatial structure and property sets without scripting
- Stable GUIDs for change tracking and databases
- Pass client checks (AIA/BAP, IDS) before delivery
- Correct georeferencing so discipline models overlay
- Correct quantities for tendering (LV)

## How people write here
- Real posts found: English, structured, with Revit/exporter build numbers (e.g. "Revit 2026 (Build 26.4.0.32, DEU)"); German context shows as "In Germany we typically use...".
- Terse variants: a title plus two screenshots ("Openings in floors").
- Typos in titles ("Widht", "CoveringBaseQuantitie"); parameter names in German or Czech ("ARC_Tragwerk", loadbearing in german).
- Politeness openers ("Hello,", "thank you for possibility to ask") and ending with "is my syntax wrong?".
- Typical German synthetic style (assumption): "zeig mir alle Wanddurchbrüche", "Stand 12", "TGA", "LV", "F90"; mixes English terms (Proxy, Pset, GUID, Mapping).
- German jargon glossary: Durchbruch/Aussparung/Schlitz = opening/penetration/slot; TGA = building services; LV = bill of quantities; AIA = client information requirements; BAP = BIM execution plan; OKFF/OKRD = top of finished floor / top of raw slab; Fachmodell = discipline model; Rohbau = shell construction.

## Local ecosystem
- BIM Deutschland (federal initiative): https://www.bimdeutschland.de/ ; BIM-Portal with machine-readable AIA and REST API; Muster-AIA/BAP downloads: https://www.bimdeutschland.de/bim-wissen/downloads
- BIM4INFRA2020 Handreichung Teil 9 (IFC data exchange): https://www.bimdeutschland.de/fileadmin/media/Downloads/Download-Liste/BIM4INFRA/3_9_BIM4INFRA2020_AP4_Teil9.pdf
- Standards named: DIN EN ISO 19650, DIN SPEC 91391, VDI 2552 Blatt 5; MVD page https://www.bimdeutschland.de/bim-wissen/standards-normen-richtlinien/model-view-definitions
- Regional guides: Bayern BIM-Leitfaden, Baden-Württemberg Straßenwesen, NRW Qualifizierungsleitfaden (linked from downloads page)
- buildingSMART Deutschland (buildingsmart.de): fetch returned empty, not verified
- Software: Revit with the open-source Autodesk revit-ifc exporter, Archicad, Allplan, Dynamo
- BIMpedia: https://www.bimpedia.de/

## Notable sources
- https://github.com/Autodesk/revit-ifc/issues/609 shaft openings in floors
- https://github.com/Autodesk/revit-ifc/issues/985 missing opening cut at flush beam
- https://github.com/Autodesk/revit-ifc/issues/924 shifted IfcSpaces
- https://github.com/Autodesk/revit-ifc/issues/907 room elevation with shared coordinates
- https://github.com/Autodesk/revit-ifc/issues/301 double True North rotation
- https://github.com/Autodesk/revit-ifc/issues/794 German multi-level storeys
- https://github.com/Autodesk/revit-ifc/issues/833 LoadBearing mapping
- https://github.com/Autodesk/revit-ifc/issues/676 proxy types from curtain walls
- https://github.com/Autodesk/revit-ifc/issues/481 proxy class override
- https://github.com/Autodesk/revit-ifc/issues/109 random GUIDs
- https://github.com/Autodesk/revit-ifc/issues/566 shared coordinates import
- https://github.com/Autodesk/revit-ifc/issues/902 IDS auditing in Revit
- https://github.com/Autodesk/revit-ifc/issues/856 national classification
- https://www.bimdeutschland.de/bim-wissen/standards-normen-richtlinien/common-data-environment
- https://www.bimdeutschland.de/bim-wissen/downloads
- https://www.bimdeutschland.de/bim-deutschland/faq
- https://www.bimpedia.de/artikel/16092-oeffnung-durchbruch-schlitz/ (not read)

## Gaps
- WebSearch unavailable (budget exhausted): no discovery of German forum threads at all.
- Fetch failures: forum.cad.de (DNS), cad.de/foren (404), forums.autodesk.com DE board (403), community.graphisoft.com (403), forum.allplan.com (DNS), bimpedia.de and bimpedia.eu article (connection refused), buildingsmart.de (empty).
- No Austrian or Swiss sources (e.g. Swiss SIA/ KBOB, Austrian Austrian Standards, openBIM Austria) were reached.
- No Durchbruchsplanung-specific user threads read; coverage of that theme is via GitHub opening bugs only.
- Re-run this cell with search enabled for real German forum voice. No suspicious sites encountered.
