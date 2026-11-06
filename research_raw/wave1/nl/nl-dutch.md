# Nederland/Vlaanderen: BIM basis ILS, NL-SfB, IFC export problemen

Cell: nl-dutch · Languages: Dutch (a few English posts from Dutch contributors) · Collected: 2026-11-06 · Records: 23 real / 14 synthetic · Communities covered: digiGO (BIM basis ILS, NL-SfB), GitHub issue trackers of Dutch standards bodies and open-source BIM tools.

IMPORTANT LIMITATION: the WebSearch budget was exhausted before the first query ran (every call was refused). All real records come from direct WebFetch of digigo.nu pages and GitHub issue pages, plus gh CLI, which was rate-limited after the first batch. No open forum threads (Autodesk NL, Graphisoft NL, bimconnected, LinkedIn, Reddit) were reached. Real records are therefore skewed to standards-body discussions and normative text rather than typical practitioner "my export is broken" threads.

## Top themes (ranked by frequency)
- NL-SfB 4-digit codes per element (BIM basis ILS 3.6), and whether the code fits the IFC class
- Correct IFC entity plus TypeEnumeration, and avoiding IfcBuildingElementProxy through export settings
- Georeferencing and shared origin (nulpunt, RD / EPSG 28992, IfcMapConversion) across aspect models
- Validation of models: IDS, Solibri rules, BIMcollab checks and Smart Views against BIM basis ILS
- Storey structure and naming (IfcBuildingStorey, "00 begane grond")
- Spaces and zones: IfcSpace, ObjectType as Bouwbesluit function, IfcZone, GO/BVO (NEN 2580)
- Material naming, NAA.K.T., IfcMaterial on every object
- Property sets: Pset_WallCommon LoadBearing, IsExternal, FireRating; IFC2x3 vs IFC4 gaps
- Quantity take-off per classification for cost estimating (Solibri ITO, BIMcollab Lists)
- Linking NLCS (2D infra layers) and NL-SfB to 3D/IFC 4.3, bSDD
- MEP systems (IfcSystem / IfcDistributionSystem) and NL-SfB installation codes
- Software manuals per tool (Revit, Archicad, Tekla, Vectorworks, BricsCAD, SketchUp)

## What people want
- A checkable, unambiguous contract: which IFC classes, psets and codes exactly, verified automatically (IDS, Solibri, BIMcollab).
- Models from several disciplines that lie on the same origin and clash-check meaningfully.
- Revit/other native exports that land in the right IFC class with correct properties without manual cleanup.
- Quantities and fire/load-bearing data per NL-SfB code for estimating and permits.
- Alignment between Dutch classifications (NL-SfB, NLCS, IMBOR, NAA.K.T.) and international ones (IFC 4.3, bSDD).

## How people write here
- Register: terse, professional, informal "je/jij"; maintainers use structured headings (Waarom / Nu / Gevraagd).
- Heavy code-switching: English tool and IFC terms inside Dutch ("aspectmodel", "export settings", "Smart Views", "clashdetectie").
- Jargon: nulpunt (origin), bouwlaag (storey), aspectmodel (discipline model), ruimte (space), BVO/GO/VG (area types), peil, stramien (grid), kozijn (window frame), ILS (information delivery spec), RVB (requirements doc).
- Typical fragments: "windveer is dakafwerking, code 27 is niet juist"; "hebben alle 212 deuren een FireRating?"; "staat er op jullie roadmap een Revit template oid?"; "gaat vaak mis doordat modellen niet op hetzelfde nulpunt liggen".
- Context given: standard name (BIM basis ILS), code numbers, EPSG codes, class names; context omitted: Revit version, IFC schema, file.
- Tone: neutral to mildly frustrated; polite hedging ("voor zover ik weet").

## Local ecosystem
- digiGO (successor of BIM Loket content, bimloket.nl redirects here): https://www.digigo.nu/ ; BIM basis ILS https://www.digigo.nu/ilsen-en-richtlijnen/bim-basis-ils/ (v2, NL-SfB 4 digits, IFC2x3 TC1 most used then IFC4)
- NL-SfB: owned by Ketenstandaard Bouw en Techniek since 1 April 2026: https://www.digigo.nu/standaarden/nlsfb/ and https://ketenstandaard.nl/nlbe-sfb-facts/
- NLCS, IMBOR (CROW), GWSW, IMWO, RVB, NEN 2580, NEN 2660, ICDD-NL, Geonovum GeoBIM georeferencing guideline
- Software manuals for BIM basis ILS: Revit, Archicad, Tekla, Vectorworks, BricsCAD, SketchUp, Allplan, DDS-CAD, HiCAD; checking with Solibri and BIMcollab
- Tools: Solibri, BIMcollab, Dalux, Navisworks, IfcOpenShell, bSDD Revit plugin, OpenAEC BIM validator (open source)
- Dataset: Schependomlaan IFC2x3 sample (buildingSMART community)

## Notable sources
- https://www.digigo.nu/ilsen-en-richtlijnen/bim-basis-ils/ - BIM basis ILS overview
- https://www.digigo.nu/ilsen-en-richtlijnen/bim-basis-ils/handleidingen/ - per-software manuals, Solibri/BIMcollab check guides
- https://www.digigo.nu/ilsen-en-richtlijnen/bim-basis-ils/downloads/ - infographics, multilingual
- https://www.digigo.nu/ilsen-en-richtlijnen/bim-basis-ils/3-4-correct-gebruik-entiteiten - proxy and TypeEnumeration
- https://www.digigo.nu/ilsen-en-richtlijnen/bim-basis-ils/3-3-bouwlaagindeling-en-naamgeving
- https://www.digigo.nu/ilsen-en-richtlijnen/bim-basis-ils/3-2-lokale-positie
- https://www.digigo.nu/ilsen-en-richtlijnen/bim-basis-ils/3-7-gebruik-propertysets
- https://www.digigo.nu/ilsen-en-richtlijnen/bim-basis-ils/4-1-ruimten
- https://www.digigo.nu/ilsen-en-richtlijnen/bim-basis-ils/4-7-materiaal
- https://www.digigo.nu/ilsen-en-richtlijnen/bim-basis-ils/praktijk/1-naa-k-t-eenduidige-materiaalbenaming
- https://www.digigo.nu/ilsen-en-richtlijnen/bim-basis-ils/2-hoe-we-informatie-uitwisselen
- https://www.digigo.nu/standaarden/nlsfb/
- https://github.com/nl-digigo/NLCS/issues/38 - NLCS vs NL-SfB in Revit
- https://github.com/nl-digigo/NLCS/issues/238 - Revit template question
- https://github.com/nl-digigo/NLCS/issues/687 - Revit to IFC quantities experiment
- https://github.com/nl-digigo/NLCS/issues/147 - IFC 4.3 alignment
- https://github.com/nl-digigo/imwo/issues/52 - NL-SfB installations vs IfcDistributionSystem
- https://github.com/nl-digigo/GeoBIM_Georefereren/issues/5 - GEO point and BIM origin
- https://github.com/OpenAEC-Foundation/OpenAEC-BIM-validator/issues/22 - NL-SfB content check
- https://github.com/OpenAEC-Foundation/OpenAEC-BIM-validator/issues/21 - federation georeferencing
- https://github.com/OpenAEC-Foundation/OpenAEC-BIM-validator/issues/19 - takeoff to Excel
- https://github.com/OpenAEC-Foundation/OpenAEC-BIM-validator/issues/17 - Smart Views
- https://github.com/Aedes-datastandaarden/ILS-woco/issues/2 - NL-SfB code correction
- https://github.com/Stichting-CROW/imbor/issues/1254 - NAA.K.T. in IMBOR
- https://github.com/buildingsmart-community/bSDD-Revit-plugin/issues/77 - NL-SfB 2005 in bSDD Revit plugin

## Gaps
- WebSearch unavailable (budget exhausted), so no search with allowed_domains for forums, blogs, Autodesk/Graphisoft community, LinkedIn, BIMcollab/Solibri knowledge bases, Vlaanderen sources (Vlaamse overheid, BIM Vlaanderen / Digitaal Vlaanderen, NBN, Agoria) were not reached.
- Autodesk and Graphisoft community pages returned 403; bimconnected.com has an expired certificate (not used); bimnieuws.nl did not resolve.
- bimloket.nl now redirects to digiGO.
- The Revit BIM basis ILS manual PDF could not be parsed as text; its export settings were not read.
- GitHub API rate limit hit after the first batch, so few repos were mined (Revit IFC exporter, IfcOpenShell Dutch issues untouched).
- Only 23 real records (target 25-50) because of the above; "real" official_doc records are normative text, not user questions. No Flemish content. Recommend re-running with search access.
