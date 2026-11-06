# German: how people ask about IFC, BIM and Revit

Language code `de` (Germany, Austria, Switzerland: "DACH"). Built from research wave 1 (collected 2026-11-06).

**Read this first: how much real German voice is in the data.**
The knowledge base holds 75 records tagged `de`: 22 real and 53 synthetic (`kb.py stats --lang de`). The web-search budget ran out before the first query, so no German forum could be reached (cad.de, the Autodesk DE forum, the Graphisoft DE community and the Allplan forum all failed or were blocked, see "Where people ask"). What exists is:

| Kind | Count | What it really is |
|---|---|---|
| Real, German text | 22 | 5 official pages (BIM Deutschland, BIMpedia); 15 German blog articles from the educator blog bim-me-up.com (titles are verbatim German; each article answers a typical user problem, so the "question" is the problem the article addresses, not a forum post); 2 GitHub issues with German content |
| Real, English text by DACH users | 23 | Autodesk revit-ifc GitHub issues by users whose posts show a German context (German Revit build "DEU", German parameter names, "In Germany we typically use..."). Listed separately because the records are tagged `en` |
| Synthetic, German | 53 | Prompts written from general knowledge of German BIM jargon, **not** copied from real posts. Their phrasing is an informed guess at style, not observed behaviour |

So the themes and technical content are well grounded, but the exact wording of German chat-style requests is not. The "How people write" section marks each statement as observed or inferred from synthetic records. A re-run with search enabled should add real forum posts.

Related docs: national background in [Germany, Austria, Switzerland: BIM/IFC requirements](../../02_standards_regulations/national/germany_austria_switzerland.md); topic digests in [Revit export and class mapping](../by_topic/revit_export_and_class_mapping.md), [geometry and openings](../by_topic/geometry_openings_curtainwalls_stairs.md), [coordinates](../by_topic/coordinates_georef_units_levels.md), [quantities](../by_topic/quantities_cost_schedule.md); [multilingual glossary](../../08_glossary/glossary_multilingual.md); [Revit IFC export reference](../../03_software/revit/ifc_export_reference.md).

## Where people ask

| Place | Language | Kind | What we saw | Access note |
|---|---|---|---|---|
| [Autodesk/revit-ifc GitHub issues](https://github.com/Autodesk/revit-ifc/issues) | English (DACH users) | Bug tracker of the open-source Revit IFC exporter | 23 records with a DACH context, 2019 to 2026; very active; many "still a problem in version X" follow-ups | Open, reachable with the `gh` CLI |
| [bim-me-up.com](https://bim-me-up.com/) | German | Blog (Germany/Austria) with reader comments; short how-to articles about Revit to IFC | 15 articles read (2016 to 2025). Comment threads add "me too" reports and extra problems | Open |
| [BIM Deutschland](https://www.bimdeutschland.de/) (federal initiative) | German | Official site, FAQ, BIM-Portal with machine-readable AIA | 4 pages read: CDE, MVD, downloads (Muster-AIA/BAP), FAQ | Open |
| [BIMpedia](https://www.bimpedia.de/) | German | Glossary/article site | Only the title "Öffnung, Durchbruch, Schlitz" (category Rohbau) was seen; later fetch refused | Content not read |
| KIT-IAI [SDM_KITModelViewer issue 13](https://github.com/KIT-IAI/SDM_KITModelViewer/issues/13) | German/English | Academic GitHub project (IFC to CityGML) | Bug report quoting a German XML error message | Open |
| [IfcOpenShell issue 388](https://github.com/IfcOpenShell/IfcOpenShell/issues/388) | English (German-influenced) | Open-source library tracker | Encoding problem with the euro sign | Open |
| forum.cad.de, Autodesk DE forum, Graphisoft DE community, Allplan forum, buildingSMART Deutschland | German | Where German practitioners most likely ask | **Not reached**: DNS failure, 404, 403 or empty page. Activity not verified. A Graphisoft thread titled "BIM mit der Deutschen Bahn" exists (title only, noted in the [national doc](../../02_standards_regulations/national/germany_austria_switzerland.md)) | Gap |
| OSArch community | English | Open-source BIM forum | A thread on German drawing conventions (DIN 1356-1) exists but was not opened | Gap |

No Austrian or Swiss sources (SIA, KBOB, Austrian Standards, openBIM Austria, Bauen digital Schweiz) were reached in the question research. They appear only in the national doc.

## Top themes (ranked)

Ranking is by how many records (German and DACH-English) touch the theme, using the cell report `de-dach` plus the blog posts.

| Rank | Theme | What people actually want | Evidence (examples below) |
|---|---|---|---|
| 1 | Revit IFC export: class mapping and `IfcBuildingElementProxy` | Walls, columns, curtain-wall parts land in the right IFC class instead of "Proxy"; `IfcExportAs` that works | blog "Wand als IfcFooting exportieren"; revit-ifc #676, #481, #759 |
| 2 | Openings and "Durchbrüche" | Reliable openings from the architect model so MEP and structural can do Durchbruchsplanung; shaft openings in floors | revit-ifc #609, #985, #530; blog "IFC ProvisionForVoid in Revit" |
| 3 | Properties and Revit parameter mapping | Own parameters appear in the IFC property sets; type parameters survive exporter updates; `IsExternal`, `LoadBearing` filled | blog "Revit Typenparameter nach IFC exportieren", "IFC Shared Parameters", "IFC Tipp ... IsExternal"; revit-ifc #833, #989 |
| 4 | Coordinates and georeferencing | Disciplines overlay correctly; project base point vs survey point; True North; rooms with the right elevation | blog "Revit, IFC und Koordinatensysteme"; revit-ifc #301, #907, #566 |
| 5 | Storeys and spatial structure | Several Revit levels per storey (finished floor "OKFF" and slab top "OKRD"); one site/building structure; elements on the right `IfcBuildingStorey` | blog "IfcBuildingStorey", "IFC Struktur"; revit-ifc #794 |
| 6 | Client requirements: AIA, BAP, MVD, IDS, CDE | Pass the client's check before delivery; know which MVD to export | BIM Deutschland pages; revit-ifc #902 (IDS auditing) |
| 7 | GUID stability and version comparison | The same element keeps its GUID between exports so changes can be tracked | revit-ifc #109, #143 |
| 8 | Quantities for tendering (LV) | Net/gross areas and volumes per storey; correct `Qto` | revit-ifc #872 |
| 9 | Importing and linking IFC in Revit | Linked IFC without bloat; windows in the right place; openings that cut | blog "IFC verlinken vs. Data Exchange", revit-ifc #1019 |
| 10 | Viewers and cross-checks | A neutral viewer to verify the export (FZKViewer, BIMcollab ZOOM, BIM Vision) | blog "Die populärsten IFC Viewer", "Materialeigenschaften in IFC" |
| 11 | Phases, expectation management, IFC 5 | "IFC is no miracle weapon"; phase created/demolished lost in IFC | blog "Die Wunderwaffe IFC", "Revit Phasen nach IFC exportieren", "IFC 5: ..." |
| 12 | Niche: encoding, CityGML | Euro sign crash; XML error on GML re-import | IfcOpenShell #388; KIT #13 |

## Local ecosystem

Short version; details and confidence marks are in the [national doc](../../02_standards_regulations/national/germany_austria_switzerland.md).

- **No law says "deliver IFC".** Real requirements sit in the client's AIA (client information requirements, English EIR) and BAP (BIM execution plan). Federal roads use BIM as the standard process from 2026; federal buildings follow a staged masterplan. "BIM-Pflicht" in the press means "the federal client writes BIM into its tenders", not a statute for private builders.
- **Germany:** BIM Deutschland and the BIM-Portal (machine-readable AIA, REST API, IDS-oriented), Muster-AIA/BAP downloads, VDI 2552 series, DIN SPEC 91391 (CDE), DIN EN ISO 19650, DIN 276 cost groups ("Kostengruppe", KG) as the usual classification, GAEB for bills of quantities, OKSTRA for roads, DB InfraGO with its own BIM rules.
- **Austria:** ÖNORM A 6241-2 (BIM), Vienna openBIM building-permit pilot (MA 37; Pset "WienBV"; IFC2x3 or IFC4 Add2 TC1; requirements as PDF, XLSX and IDS), AIA4ALL project with the open-source IDS4All converter, buildingSMART Austria.
- **Switzerland:** no federal BIM law found; eBKP-H / eBKP-T cost plans (CRB), SBB staged BIM roll-out, Bauen digital Schweiz (buildingSMART Switzerland).
- **Software people mention:** Revit with the open-source IFC exporter (most of the real posts), Archicad, Allplan, Dynamo, MagiCAD, Bausoft CAD, Solibri, Navisworks, BIMcollab ZOOM, FZKViewer (KIT), BIM Vision.
- **Enthusiasts and educators:** bim-me-up.com, BIMpedia, BIM Institut Uni Wuppertal and BIM Cluster Bayern (named in the national doc; content not read).

## How people write

### Evidence status

| Statement type | Source |
|---|---|
| Observed in real records | German blog titles (2 to 9 words), the English DACH GitHub issues, official German pages |
| Inferred from the 53 synthetic German prompts | Chat-style request phrasing below. These were written by an AI agent, so treat them as plausible, not proven |

### Register and structure

- **Real German blog titles** are neutral and noun-heavy: "IfcBuildingStorey", "Revit Phasen nach IFC exportieren", "Wand als IfcFooting exportieren". Class names stay as written in the schema, even mid-sentence.
- **Real DACH GitHub posts (English):** numbered reproduction steps, the exact exporter build ("Revit 2026 (Build 26.4.0.32, DEU)"), screenshots; later commenters only add "still a problem in version X". Some are terse: one issue is a title plus two screenshots ("Openings in floors"). Politeness appears as a greeting opener or a closing doubt ("is my syntax wrong?").
- **Synthetic chat prompts** (n=53): 10 to 22 words, median 15; 41 of 53 start in lower case; imperative "du" style addressed to the assistant; only 25 of 53 contain a question mark; 9 contain "bitte". The most common openers are "prüf mal ..." (6, plus 4 spelled "pruef mal"), "zeig mir ..." (5), "kannst du ..." (3), "vergleich mal ...", "mach mir ...", "gib mir ...", "wie krieg ich ...". Typical closers: "bitte", "was tun?", "woran liegts", "check bitte", or a reason with a deadline ("brauch ich für die Durchbruchsplanung morgen", "sonst fliegen wir beim AIA-Check raus").
- **Particles and slang** in the synthetic prompts: "mal" (softener), "ne" for "eine" (5 prompts, e.g. "ne Stahlliste"), "kriegen" for "bekommen" (3), "irgendwie", "wieder". They match informal German office speech but are not confirmed by real posts.

### Jargon and slang table

Terms come from the cell report `de-dach`, the German prompts and the national doc.

| Term (as written) | Meaning | Standard term |
|---|---|---|
| Durchbruch / Aussparung / Schlitz / Öffnung | hole through wall or slab; slot; generic opening (used loosely) | `IfcOpeningElement` (void); before it is cut, often a void-provision proxy |
| Durchbruchsplanung | planning of penetrations for pipes and ducts | opening/penetration coordination |
| Durchbruchsmeldung / -anfrage | request from MEP to structural/architect for an opening | opening request |
| TGA | technical building services | MEP (Technische Gebäudeausrüstung) |
| Fachmodell / Teilmodell / Koordinationsmodell | discipline model / part model / federated model | discipline model, federated model |
| Rohbau | shell construction | structural shell model |
| Tragwerk / Statik / Statikmodell | structure; structural analysis; structural model | structural model |
| LV | bill of quantities / tender specification | Leistungsverzeichnis; exchange via GAEB |
| AIA / BAP | client information requirements / BIM execution plan | EIR / BEP |
| AG / Bauherr | client | employer, appointing party |
| MVD, Reference View (RV), Design Transfer View (DTV), "2x3 CV" | IFC export views | Model View Definitions; "2x3 CV" = IFC2x3 Coordination View |
| Pset | property set | `IfcPropertySet`, Merkmalgruppe |
| Merkmal | single property | `IfcProperty` |
| Kostengruppe / KG / DIN 276 | cost group classification | classification reference |
| NGF, Raumnummer, Nutzung | net floor area, room number, use | `Qto_SpaceBaseQuantities.NetFloorArea`, `IfcSpace.Name/LongName` |
| OKFF / OKRD | top of finished floor / top of raw slab (Rohdecke) | two Revit levels per `IfcBuildingStorey` |
| Geschoss | storey | `IfcBuildingStorey` |
| Projektbasispunkt / Vermessungspunkt / Nordrichtung | Revit project base point / survey point / true north | `IfcMapConversion`, `IfcSite` reference lat/long |
| Rechtswert / Hochwert | easting / northing | `IfcMapConversion.Eastings/Northings` |
| F90 | fire resistance 90 min | `Pset_WallCommon.FireRating` |
| Tragend / Außenwand | load-bearing / external wall | `LoadBearing`, `IsExternal` |
| Stand 12, KW12 | model revision number / calendar week | version label used in place of a file name |
| Bauantrag / Baueinreichung (AT) | building permit application | permit submission |
| CAFM, FM-Übergabe | facility-management software; handover to operations | COBie-like handover |
| Stahlliste, Bewehrung, Fertigteile | rebar schedule, reinforcement, precast parts | `IfcReinforcingBar`, `IfcElementAssembly` |
| Typenparameter / benutzerdefinierte Psets | Revit type parameters / user-defined property sets option | exporter setting |

### Misspellings, name variants, code-switching

- **Transliterated umlauts** ("pruef", "Waenden", "Raeume", "fuer", "Stuetze", "Durchbrueche", "Flaechen", "Oeffnungen") appear in 7 of 53 synthetic prompts, usually together with other casual traits. Plausible as a real habit, but not seen in a real German post in this data. The dataset's German paraphrase of the IfcFooting article is also typed this way ("Fundamentwaende").
- **Typos in real English posts by DACH users:** "Widht", "CoveringBaseQuantitie" (revit-ifc #872). Parameter names in German or other local languages ("ARC_Tragwerk", Czech names in #989).
- **Code-switching:** a German sentence frame with English or Denglish nouns: Proxy, Pset, GUID, Mapping, Export, Viewer, Shared Parameters, Data Exchange, BCF, Solibri, Navisworks; class names exactly as in the schema (`IfcBuildingElementProxy`, `IfcOpeningElement`). The blog uses "Typenparameter", "Data Exchange" and "Shared Parameters" side by side. English posts by DACH users contain German fragments ("In Germany we typically use...", "Gesamtmodell" in file names, German names such as "Leerrohr" in Dynamo posts of the wider data).
- **Name variants for the same thing:** Durchbruch / Aussparung / Öffnung; Projektbasispunkt / Projektnullpunkt (the latter only in synthetic prompts); IFC2x3 written "2x3" or "IFC 2x3 CV"; "IFC4 Reference View" abbreviated "RV".
- **Swiss and Austrian variants:** not observed (no Austrian or Swiss posts). The national doc lists "Baueinreichung" (AT) and "eBKP-H" (CH) as local vocabulary.

### Tone, context given and omitted

- **Tone** in the synthetic set: 36 neutral, 7 urgent, 5 confused, 2 frustrated, 2 curious, 1 skeptical. Urgency is expressed with a deadline ("morgen", "Stand 14"), not with exclamation marks. Real DACH GitHub posts range from neutral to frustrated ("PR: Floors not exporting" lists workarounds the user cannot accept).
- **Context usually given:** the discipline ("TGA", "Arch-Modell", "Statikmodell"), class names, a property or standard (F90, DIN 276, IFC2x3 CV), what the result is for (Durchbruchsplanung, LV, AIA-Check, CAFM-Import).
- **Context usually omitted:** file name or path ("das Modell", "die IFC"), Revit/exporter version (except in bug reports), IFC schema, whether a model is loaded, tolerance values. A good assistant must infer or ask.
- **Real bug reports** give much more: Revit version and exporter build, steps, screenshots, expected vs actual.

## Real questions

"Paraphrase in original language" is filled only where the dataset holds a German paraphrase. For the blog entries the dataset paraphrase is English, so only the verbatim German title and an English gist are shown. Source types: `blog` = how-to article, `official_doc` = authority page, `github_issue` = bug report.

### A. German-language records (22)

| # | Original title (verbatim) | Paraphrase in original language | Gist in English | Persona · type · year | Source |
|---|---|---|---|---|---|
| 1 | Common Data Environment |  | BIM Deutschland explains the CDE per ISO 19650 and says an open CDE must manage IFC, BCF, COBie. | reviewer_authority · knowledge · 2025 | [bimdeutschland.de](https://www.bimdeutschland.de/bim-wissen/standards-normen-richtlinien/common-data-environment) (official_doc) |
| 2 | Model View Definitions |  | Explains MVDs (Coordination View, Design Transfer View, Reference View, QTO View) and that AIA/BAP must name them. | reviewer_authority · knowledge · 2025 | [bimdeutschland.de](https://www.bimdeutschland.de/bim-wissen/standards-normen-richtlinien/model-view-definitions) (official_doc) |
| 3 | BIM Deutschland Downloads |  | Download list of Muster-AIA, Muster-BAP and BIM4INFRA2020 Teil 9 Datenaustausch mit IFC. | reviewer_authority · knowledge · 2025 | [bimdeutschland.de](https://www.bimdeutschland.de/bim-wissen/downloads) (official_doc) |
| 4 | Welche Dateiformate bzw. Standards werden bei den maschinenlesbaren AIA verwendet? |  | FAQ: are BIM-Portal requirements binding nationwide? Which formats do machine-readable AIA use (ifcXML)? | owner_client · knowledge · 2025 | [bimdeutschland.de](https://www.bimdeutschland.de/bim-deutschland/faq) (official_doc) |
| 5 | Öffnung, Durchbruch, Schlitz |  | BIMpedia article 'Öffnung, Durchbruch, Schlitz' in category Rohbau (seen via homepage link only). | architect · knowledge · 2025 | [bimpedia.de](https://www.bimpedia.de/artikel/16092-oeffnung-durchbruch-schlitz/) (blog) |
| 6 | Die Wunderwaffe IFC |  | IFC is no miracle weapon: parametric objects arrive as dumb objects in the partner's software. | bim_manager · opinion · 2016 | [bim-me-up.com](https://bim-me-up.com/die-wunderwaffe-ifc/) (blog) |
| 7 | IFC 5: Eine neue Hoffnung für Interoperabilität |  | IFC 5 as a new hope for interoperability: IFC is slow, heavy, monolithic, no incremental updates. | bim_manager · opinion · 2025 | [bim-me-up.com](https://bim-me-up.com/ifc-5-eine-neue-hoffnung-fuer-interoperabilitaet/) (blog) |
| 8 | Wand als IfcFooting exportieren | meine Fundamentwaende aus dem Wandwerkzeug werden IfcWall statt IfcFooting | Foundations modelled with Revit wall tool export as IfcWall; how to get IfcFooting? | architect · how_to · 2020 | [bim-me-up.com](https://bim-me-up.com/wand-als-ifcfooting-exportieren/) (blog) |
| 9 | Revit, IFC und Koordinatensysteme |  | Revit has several origins; where does my IFC land in other software and does shared coordinates matter for GIS? | bim_coordinator · troubleshooting · 2023 | [bim-me-up.com](https://bim-me-up.com/revit-ifc-und-koordinatensysteme/) (blog) |
| 10 | Aktuelle Revit IFC Exporter |  | Many IFC export issues come from an outdated Revit IFC exporter add-in. | bim_coordinator · how_to · 2021 | [bim-me-up.com](https://bim-me-up.com/aktuelle-revit-ifc-exporter/) (blog) |
| 11 | Revit Typenparameter nach IFC exportieren |  | Type parameters no longer export through user-defined property sets in new exporter versions. | bim_coordinator · troubleshooting · 2023 | [bim-me-up.com](https://bim-me-up.com/revit-typenparameter-nach-ifc-exportieren/) (blog) |
| 12 | IFC verlinken vs. Data Exchange laden in Revit |  | Linked IFC vs Autodesk Data Exchange in Revit: size, performance, use cases. | bim_coordinator · knowledge · 2025 | [bim-me-up.com](https://bim-me-up.com/ifc-verlinken-vs-data-exchange-laden-in-revit/) (blog) |
| 13 | IFC ProvisionForVoid in Revit - Öffnen vs. Referenzieren / Binden |  | ProvisionForVoid openings must cut hosts in Revit and show properties; open vs link vs bind. | bim_coordinator · troubleshooting · 2023 | [bim-me-up.com](https://bim-me-up.com/ifc-provisionforvoid-in-revit-offnen-vs-referenzieren-binden/) (blog) |
| 14 | Revit Phasen nach IFC exportieren |  | Revit exports one phase at a time; demolished elements and phase data are lost in IFC. | bim_coordinator · troubleshooting · 2023 | [bim-me-up.com](https://bim-me-up.com/revit-phasen-nach-ifc-exportieren/) (blog) |
| 15 | IFC Shared Parameters |  | Not all IFC parameters exist in Revit by default; use IFC shared parameter files; material layers differ after export. | bim_coordinator · how_to · 2024 | [bim-me-up.com](https://bim-me-up.com/ifc-shared-parameters/) (blog) |
| 16 | IFC Struktur - IfcProject, IfcSite, IfcFacility |  | Revit exports only one IfcSite and IfcBuilding; how to fill project/site/building and show MEP systems separately? | bim_coordinator · how_to · 2024 | [bim-me-up.com](https://bim-me-up.com/ifc-struktur/) (blog) |
| 17 | Materialeigenschaften in IFC |  | Exported material properties are not visible in every IFC viewer, especially for multilayer walls. | bim_coordinator · troubleshooting · 2024 | [bim-me-up.com](https://bim-me-up.com/materialeigenschaften-in-ifc/) (blog) |
| 18 | IfcBuildingStorey |  | Elements on levels not flagged Building Story land on the wrong IfcBuildingStorey. | bim_coordinator · troubleshooting · 2024 | [bim-me-up.com](https://bim-me-up.com/ifcbuildingstorey/) (blog) |
| 19 | Die populärsten IFC Viewer |  | Which free IFC viewers are most popular, and why keep one vendor-neutral viewer for cross-checks? | bim_coordinator · knowledge · 2020 | [bim-me-up.com](https://bim-me-up.com/die-popularsten-ifc-viewer/) (blog) |
| 20 | IFC Tipp: Revit-Stütze den IsExternal Standardparameter zuweisen |  | Revit columns have no Function so Pset_ColumnCommon.IsExternal is empty; map a custom Yes/No parameter. | architect · how_to · 2019 | [bim-me-up.com](https://bim-me-up.com/ifc-tipp-revit-stutze-den-isexternal-standardparameter-zuweisen/) (blog) |
| 21 | turn off unicode conversion IFCOpenshell Parse |  | The Euro sign decoded from \X2\ crashes wofstream/wcout; can the conversion be disabled? | developer_programmer · troubleshooting · 2018 | [GH IfcOpenShell/IfcOpenShell#388](https://github.com/IfcOpenShell/IfcOpenShell/issues/388) (github_issue) |
| 22 | KITModelViewer IFC Export -> GML reimport not working properly | Export to gml works, reimport throws 'ungültige Daten auf Stammebene. Zeile 9, Position 1' because the generated comment (Level of Detail line) is not valid XML. | IFC export to GML works in KITModelViewer but reimport fails with XML error 'invalid data at root level, line 9' because the header comment is malformed. | researcher_academic · troubleshooting · 2025 | [GH KIT-IAI/SDM_KITModelViewer#13](https://github.com/KIT-IAI/SDM_KITModelViewer/issues/13) (github_issue) |

What the sources answered, for the entries that matter to a tester:

| Entry | Resolution in the source |
|---|---|
| "Wand als IfcFooting exportieren" | Add `IfcExportAs=IfcFooting` to the wall type/instance **and** set the wall Function to Foundation or Retaining, otherwise it still exports `IfcWall` |
| "Revit Typenparameter nach IFC exportieren" | List the type class (`IfcWallType`; `IfcDoorStyle` for 2x3 doors) in the user-defined parameter set file and keep the type/instance flag; a family parameter called `TypeName` can block the built-in Type Name |
| "IFC Tipp: Revit-Stütze den IsExternal Standardparameter zuweisen" | Create a Yes/No parameter and add a tab-separated line to the mapping file with the exact IFC names; instance parameters are needed in newer versions |
| "IfcBuildingStorey" | Use the `IfcSpatialContainer` parameter with the target level name |
| "Revit, IFC und Koordinatensysteme" | Export from a local origin, treat georeferencing separately (IFC4 embeds the map conversion), avoid shared coordinates far from the building |
| "IFC ProvisionForVoid in Revit - Öffnen vs. Referenzieren / Binden" | Link the IFC and bind the link so openings become native instances that can cut; downside: no simple update from the source |
| "Materialeigenschaften in IFC" | Look into the file with a text editor; viewer display matters less than what machines read |
| "Revit Phasen nach IFC exportieren" | Revit exports one phase at a time; add a custom pset with phase created/demolished |

### B. English-language records by DACH users (23, tagged `en`)

Titles are verbatim GitHub issue titles; the "PR:" prefix is the Autodesk issue-template tag. Persona labels are inferred by the research agent.

| # | Original title (verbatim) | Paraphrase in original language | Gist in English | Persona · type · year | Source |
|---|---|---|---|---|---|
| 1 | Problem: Bug Revit 2022 IFC Export Shaft opening in floors |  | Revit 2022 IFC exporter drops shaft openings that share an edge with floors; floor boundary wrong. | bim_coordinator · troubleshooting · 2023 | [GH Autodesk/revit-ifc#609](https://github.com/Autodesk/revit-ifc/issues/609) (github_issue) |
| 2 | PR: IFC export skips opening cut when intersecting element is flush with wall top |  | Beam joined to wall with identical top elevation: no IfcOpeningElement is created, solids overlap (regression vs Revit 2025). | bim_coordinator · troubleshooting · 2026 | [GH Autodesk/revit-ifc#985](https://github.com/Autodesk/revit-ifc/issues/985) (github_issue) |
| 3 | PR: Room geometry shifted in IFC Exporter 25.4.40.17 + 25.4.41.5 + 26.4.0.16 + 26.4.0.32 |  | After updating the IFC exporter, IfcSpaces are shifted out of the building and room heights are wrong in 3 models. | bim_manager · troubleshooting · 2025 | [GH Autodesk/revit-ifc#924](https://github.com/Autodesk/revit-ifc/issues/924) (github_issue) |
| 4 | PR: Rooms exported with wrong elevation with shared coordinates |  | With shared coordinates, rooms are exported high above the geometry by the project elevation. | bim_coordinator · troubleshooting · 2025 | [GH Autodesk/revit-ifc#907](https://github.com/Autodesk/revit-ifc/issues/907) (github_issue) |
| 5 | Building with shared coordinates rotated twice on the site |  | Building exported with shared coordinates and site with survey point leads to double rotation by True North. | bim_coordinator · troubleshooting · 2021 | [GH Autodesk/revit-ifc#301](https://github.com/Autodesk/revit-ifc/issues/301) (github_issue) |
| 6 | Openings in floors |  | Prerelease exporter 2022.5.2 exports floor openings incorrectly in the IFC2x3 Coordination View. | architect · troubleshooting · 2022 | [GH Autodesk/revit-ifc#530](https://github.com/Autodesk/revit-ifc/issues/530) (github_issue) |
| 7 | Random IFC GUID for walls at each export |  | 23 walls get a random IFC GUID on every export which breaks the database linkage. | bim_manager · troubleshooting · 2019 | [GH Autodesk/revit-ifc#109](https://github.com/Autodesk/revit-ifc/issues/109) (github_issue) |
| 8 | IFC GUID changes Revit 2019 |  | GUIDs of steel connections and parametric cuts change on each export. | bim_coordinator · troubleshooting · 2019 | [GH Autodesk/revit-ifc#143](https://github.com/Autodesk/revit-ifc/issues/143) (github_issue) |
| 9 | Revit Slab to IfcSite does not work with modified points |  | Slab mapped to IfcSite works only unmodified; with modified points the class is wrong. | bim_coordinator · troubleshooting · 2022 | [GH Autodesk/revit-ifc#505](https://github.com/Autodesk/revit-ifc/issues/505) (github_issue) |
| 10 | ENH: Export multiple levels as one IfcBuildingStorey |  | In Germany several Revit levels per storey are used (finished floor, slab top); asks to map all of them to one IfcBuildingStorey. | bim_coordinator · feature_request · 2024 | [GH Autodesk/revit-ifc#794](https://github.com/Autodesk/revit-ifc/issues/794) (github_issue) |
| 11 | ENH: Disable Uniformat classification if Assembly Code parameter is used for other classification system |  | Wants to use Assembly Code for national classification without Uniformat being exported. | bim_manager · feature_request · 2025 | [GH Autodesk/revit-ifc#856](https://github.com/Autodesk/revit-ifc/issues/856) (github_issue) |
| 12 | PR: Can't overwrite *_Common.LoadBearing with a user defined parameter |  | Own office-wide LoadBearing parameter (German name Tragwerk) cannot override Pset_WallCommon.LoadBearing via mapping file. | architect · troubleshooting · 2025 | [GH Autodesk/revit-ifc#833](https://github.com/Autodesk/revit-ifc/issues/833) (github_issue) |
| 13 | PR: Widht in CoveringBaseQuantitie from basicwall is missing |  | Width (thickness) base quantity missing for walls exported as IfcCovering. | estimator_qs · troubleshooting · 2025 | [GH Autodesk/revit-ifc#872](https://github.com/Autodesk/revit-ifc/issues/872) (github_issue) |
| 14 | ENH: IDS auditing |  | Run IDS checks inside Revit before the slow IFC export. | bim_manager · feature_request · 2025 | [GH Autodesk/revit-ifc#902](https://github.com/Autodesk/revit-ifc/issues/902) (github_issue) |
| 15 | PR: Beam export IfcRectangleProfileDef, ExtrudedSolid dimensions not as expected |  | Beam length/width/height mixed up in IfcRectangleProfileDef/extrusion depending on IFC version. | structural_engineer · troubleshooting · 2025 | [GH Autodesk/revit-ifc#837](https://github.com/Autodesk/revit-ifc/issues/837) (github_issue) |
| 16 | IFC to Revit (shared coordinates) |  | How to link georeferenced IFC files in Revit 2022 so they sit in the right position; works in Trimble/BIM Vision. | bim_coordinator · how_to · 2022 | [GH Autodesk/revit-ifc#566](https://github.com/Autodesk/revit-ifc/issues/566) (github_issue) |
| 17 | PR: When importing IFC files, windows are positioned outside the wall face in the 3D view |  | IFC import: windows sit outside the wall face in 3D (not in Revit 2024). | architect · troubleshooting · 2026 | [GH Autodesk/revit-ifc#1019](https://github.com/Autodesk/revit-ifc/issues/1019) (github_issue) |
| 18 | PR: Floors not exporting |  | Floors do not export even though mapped to IfcSlab; invalid class elsewhere falls back to proxy. | bim_coordinator · troubleshooting · 2024 | [GH Autodesk/revit-ifc#759](https://github.com/Autodesk/revit-ifc/issues/759) (github_issue) |
| 19 | PR: auto-generated building element proxy type |  | Hundreds of auto-generated IfcBuildingElementProxyTypes from curtain wall profiles cannot be given IfcExportAs. | bim_coordinator · troubleshooting · 2023 | [GH Autodesk/revit-ifc#676](https://github.com/Autodesk/revit-ifc/issues/676) (github_issue) |
| 20 | Fascias and Wall Sweeps not able to override IFC Class from BuildingElementProxy |  | Fascias and wall sweeps stay IfcBuildingElementProxy despite mapping and IfcExportAs. | bim_coordinator · how_to · 2022 | [GH Autodesk/revit-ifc#481](https://github.com/Autodesk/revit-ifc/issues/481) (github_issue) |
| 21 | PR: IFC export ignores mapping table setting for certain built-in parameters |  | User shared parameters with same names as built-ins (Czech names) are replaced by built-in values in property sets. | bim_coordinator · troubleshooting · 2026 | [GH Autodesk/revit-ifc#989](https://github.com/Autodesk/revit-ifc/issues/989) (github_issue) |
| 22 | PR: IFC4 export of curtain walls crashes with AccessViolationException in FootPrintInfo |  | IFC4 export of curtain walls crashes with AccessViolationException. | bim_coordinator · troubleshooting · 2026 | [GH Autodesk/revit-ifc#992](https://github.com/Autodesk/revit-ifc/issues/992) (github_issue) |
| 23 | PR: Revit 2026 export joined geometry walls with mass |  | Joined-geometry walls with mass exported wrongly in Revit 2026. | bim_coordinator · troubleshooting · 2026 | [GH Autodesk/revit-ifc#1014](https://github.com/Autodesk/revit-ifc/issues/1014) (github_issue) |

Counting note: the target of 40 to 80 real records is met only when the 23 English DACH posts are included. Genuinely German-language practitioner questions (forum posts) are missing.

## Ready test prompts

All prompts below are **synthetic** (never real quotes). 51 are taken verbatim from the dataset (source id under the prompt ID); 2 are new, written for this document from facts in the national doc (marked `new`). Difficulty tags are from the dataset (new prompts tagged by the editor). "Needs file" means the request assumes an IFC or Revit model is loaded. Expected behaviors are in English.

### 1. Durchbrüche and MEP coordination

| ID | Prompt (synthetic) | EN gloss | Persona · intent · difficulty | Expected behavior (what a good assistant does) |
|---|---|---|---|---|
| DA1<br><sub>de-dach-s001</sub> | zeig mir alle Wanddurchbrüche im Arch-Modell, wo keine TGA-Leitung durchgeht. brauch ich für die Durchbruchsplanung morgen | List all openings in walls from the architect model that have no matching MEP penetration. | mep_engineer · coordinate_clash · hard · needs file | Find IfcOpeningElement in walls, intersect with MEP element geometry from the linked model, list openings without crossing element with ids, storey, size. |
| DA2<br><sub>de-openings-s007</sub> | zeig mir alle Leitungen TGA die durch Wände/Decken gehen und noch keinen Durchbruch haben, DN und Wandstärke dazu | Find all TGA pipes through walls that have no Aussparung/Durchbruch yet | mep_engineer · coordinate_clash · hard · needs file | Intersect MEP segments with walls/slabs, subtract existing openings, output diameter/size and host thickness table. |
| DA3<br><sub>de-openings-s008</sub> | prüf mal die Durchbruchsmeldungen vom TGA-Modell gegen die Öffnungen im Statikmodell, welche passen nicht? | Check Durchbruchsanfragen from TGA against Statik openings | structural_engineer · validate_check · hard · needs file | Match void-provision proxies to IfcOpeningElements by position/size tolerance; list mismatches and changes. |
| DA4<br><sub>de-dach-s009</sub> | welche Lüftungskanäle > 300 mm durchdringen F90 Wände? mit Geschoss und Position | List all ducts larger than 300 mm passing through fire walls. | mep_engineer · query_model_data · hard · needs file | Find ducts, intersect with walls whose FireRating is F90, list size, storey, location. |
| DA5<br><sub>de-dach-s015</sub> | mach mir aus den Kollisionen Rohr/Wand ein BCF mit Position und Bauteil-GUID, Durchbruch fehlt | Create BCF for missing wall penetrations. | mep_engineer · coordinate_clash · hard · needs file | Compute pipe-wall intersections lacking openings, produce BCF issues with viewpoint and GUIDs. |
| DA6<br><sub>de-geom-s011</sub> | Pruef mal ob alle Wanddurchbrueche als IfcOpeningElement exportiert sind, bei manchen Waenden fehlt die Aussparung fuer die Tuer | Check openings (Durchbrueche) match walls | bim_coordinator · coordinate_clash · medium · needs file | Verify IfcOpeningElement coverage on walls with doors; report walls without; compare against opening sizes. |
| DA7<br><sub>de-openings-s009</sub> | wie kriege ich die Wanddurchbrüche aus Revit als IfcOpeningElement raus? kommen nur als Proxy an | How to export Revit Durchbrueche so the structural engineer sees them as openings | bim_coordinator · how_to · medium | Explain generic-model void families exported as proxy vs wall openings, IFC export settings, Pset mapping. |
| DA8<br><sub>de-dach-s013</sub> | Deckendurchbrüche fehlen in der IFC, in Revit sind sie da (Schacht). Export 2x3 CV. was tun? | Why are floor openings missing after export. | structural_engineer · troubleshoot_export · medium | Explain shaft openings sharing edges may not export, suggest alternative modelling, verify after export. |

### 2. IFC classes and Revit mapping

| ID | Prompt (synthetic) | EN gloss | Persona · intent · difficulty | Expected behavior (what a good assistant does) |
|---|---|---|---|---|
| DB1<br><sub>de-dach-s002</sub> | wieviele IfcBuildingElementProxy sind in dem Export und aus welchen Revit-Kategorien kommen die? Mapping stimmt irgendwie nicht | Count proxies and their Revit categories. | bim_coordinator · query_model_data · medium · needs file | Count IfcBuildingElementProxy, group by category/ObjectType, suggest mapping table fixes. |
| DB2<br><sub>de-dach-s012</sub> | die Stützen sind alle als Proxy drin, kannst du die zu IfcColumn machen? Name fängt mit ST_ an | Reclassify proxies that are really columns. | bim_coordinator · modify_model_data · medium · needs file | Find proxies with matching name, change class to IfcColumn, preserve psets, report changes. |
| DB3<br><sub>de-proxy-s016</sub> | prüf ob die exportierten IFC-Klassen mit dem was in IfcExportAs steht übereinstimmen, wir hatten wieder Abweichungen | Verify exported classes match IfcExportAs values | bim_manager · validate_check · hard · needs file | Compare intended classes with actual classes where parameter present; list mismatches. |
| DB4<br><sub>de-dach-s005</sub> | meine eigenen Parameter kommen in der IFC nicht an obwohl Häkchen bei benutzerdefinierte Psets gesetzt ist, woran liegts | Why do my shared parameters not appear in the IFC. | architect · troubleshoot_export · medium | Explain mapping txt file format, name clashes with built-ins, type vs instance parameters, how to verify. |

### 3. Properties, psets and checks

| ID | Prompt (synthetic) | EN gloss | Persona · intent · difficulty | Expected behavior (what a good assistant does) |
|---|---|---|---|---|
| DC1<br><sub>de-dach-s004</sub> | prüf mal ob bei allen Wänden Tragend, Feuerwiderstand und Außenwand befüllt sind, sonst fliegen wir beim AIA-Check raus | Check that all walls have LoadBearing, FireRating and IsExternal filled in. | bim_manager · validate_check · medium · needs file | List walls missing Pset_WallCommon.LoadBearing, FireRating, IsExternal with GUIDs and counts. |
| DC2<br><sub>de-revit-auto-s016</sub> | prüf mal alle Türen und Wände auf fehlenden Feuerwiderstand, Liste mit IDs bitte | Check doors and walls for missing fire rating | bim_coordinator · validate_check · easy · needs file | Query doors and walls, check fire rating parameter (type and instance), return grouped list with ids. |
| DC3<br><sub>de-psets-s015</sub> | hat jedes Bauteil die Kostengruppe nach DIN 276 im Pset? zeig mir die ohne | Check that Kostengruppe DIN 276 is on all elements | bim_coordinator · validate_check · medium · needs file | Search psets for a Kostengruppe property, list building elements lacking it. |
| DC4<br><sub>de-data-s012</sub> | welche Wände haben keine Feuerwiderstandsklasse? Liste mit GUID und Geschoss raus als csv, Semikolon als Trenner bitte | Which walls lack FireRating and export them with GUID | bim_coordinator · query_model_data · medium · needs file | Find walls without Pset_WallCommon.FireRating, output GUID and storey as semicolon-delimited CSV with German-locale decimals. |
| DC5<br><sub>p-student-s015</sub> | zeig mir bei allen Türen Name, Reference und ObjectType, welches ist jetzt der Instanzname? Allplan Export | Show Name, Reference, ObjectType of all doors, which one is the instance name? | student_beginner · query_model_data · medium · needs file | List attributes for IfcDoor, explain Name vs type name, note Reference deprecated in 4.3. |
| DC6<br><sub>enc-s010</sub> | stimmen Umlaute und Dezimalkommas in den Psets, oder sind da \X\ Reste und Texte statt Zahlen | Do umlauts and comma decimals in the Psets read correctly? | structural_engineer · query_model_data · medium · needs file | Check pset string values for escape remnants and numbers stored as text with comma decimals; list offenders. |
| DC7<br><sub>mx-mcl-s006</sub> | zeig mir alle IfcPresentationLayerAssignment mit Anzahl Objekte, Layer mit gleichem Namen bitte markieren | List presentation layers and elements | bim_coordinator · validate_check · medium · needs file | List all layer assignments with item counts and flag duplicate names. |

### 4. Coordinates and georeferencing

| ID | Prompt (synthetic) | EN gloss | Persona · intent · difficulty | Expected behavior (what a good assistant does) |
|---|---|---|---|---|
| DD1<br><sub>de-dach-s003</sub> | wo sitzt der Projektbasispunkt in der IFC und stimmt die Nordrichtung? Fachmodelle passen nicht übereinander | Check where the project base point and the site are located and whether rotation is correct. | bim_coordinator · validate_check · hard · needs file | Read IfcMapConversion, IfcProjectedCRS, IfcSite reference lat/long, placements; report offsets and true north, compare across files. |
| DD2<br><sub>de-dach-s016</sub> | Modell liegt weit weg vom Ursprung, Einheiten mm oder m? check bitte | Check units and coordinates; model appears kilometres away. | architect · query_model_data · medium · needs file | Report IfcUnitAssignment, bounding box, placement offsets, probable cause and fix. |
| DD3<br><sub>mul-coord-s013</sub> | pruef mal ob die drei IFCs dasselbe Koordinatensystem haben (ETRS89/UTM32), Rechtswert Hochwert Rotation | Check three files share the same CRS (ETRS89/UTM32) | bim_coordinator · coordinate_clash · medium · needs file | Compare CRS and MapConversion of the three files and list deviations in Eastings/Northings/rotation. |
| DD4<br><sub>de-coord-s018</sub> | wie krieg ich beim IFC Export aus Archicad den Projektnullpunkt und die Vermessungskoordinaten sauber rein? | Coordinates in IFC export. | bim_coordinator · how_to · medium | Explain survey point/project origin settings and IfcMapConversion. |

### 5. Storeys, rooms, FM

| ID | Prompt (synthetic) | EN gloss | Persona · intent · difficulty | Expected behavior (what a good assistant does) |
|---|---|---|---|---|
| DE1<br><sub>de-dach-s006</sub> | Elemente auf OKRD-Ebenen bitte dem jeweiligen OKFF-Geschoss zuordnen, wir haben pro Geschoss zwei Ebenen | Move elements from slab-top levels to the finished-floor storeys. | bim_coordinator · modify_model_data · hard · needs file | Reassign IfcRelContainedInSpatialStructure to the intended IfcBuildingStorey; report moved counts; do not duplicate storeys. |
| DE2<br><sub>de-roundtrip-s012</sub> | IFC fuer Allplan pruefen: Geschosse, Bauteilnamen, Typen. Was fehlt beim Import in Allplan 2025? | Check that Allplan can import: storeys, types, names. | bim_coordinator · validate_check · medium · needs file | Report storeys, Name/ObjectType/Reference usage, missing types, IFC2x3 schema. |
| DE3<br><sub>en-fmor-s014</sub> | pruef mal ob alle Raeume ne Nutzung haben und einem Geschoss zugeordnet sind | Check all spaces have a use designation and are assigned to a storey | reviewer_authority · validate_check · medium · needs file | Check IfcSpace for use/occupancy property and containment in IfcBuildingStorey, list violations. |
| DE4<br><sub>de-spaces-s009</sub> | zeig mir alle Räume deren NetFloorArea mehr als 2% von der Revit-Fläche abweicht | List rooms with area deviation | bim_coordinator · query_model_data · hard · needs file | Compare Qto with area parameter per space and list deviations. |
| DE5<br><sub>de-dach-s014</sub> | Raumliste mit Nutzung und Fläche für die FM-Übergabe, Räume ohne Namen markieren | List all rooms with area and usage for FM handover. | facility_manager · extract_quantities · easy · needs file | List IfcSpace with Name, LongName, area from Qto_SpaceBaseQuantities, flag unnamed. |
| DE6<br><sub>de-cobie-s009</sub> | prüf mal ob jeder Raum eine Raumnummer und NGF hat, sonst klappt der CAFM-Import nicht | Check rooms for room numbers and area before CAFM import. | facility_manager · validate_check · easy · needs file | List IfcSpace missing Number/LongName/NetFloorArea; duplicates of room numbers. |

### 6. Quantities and Leistungsverzeichnis

| ID | Prompt (synthetic) | EN gloss | Persona · intent · difficulty | Expected behavior (what a good assistant does) |
|---|---|---|---|---|
| DF1<br><sub>de-dach-s007</sub> | Wandflächen und Volumen je Geschoss als Liste fürs LV, nur Außenwände. werden Öffnungen abgezogen? bitte angeben | Export wall areas and volumes per storey for tendering. | estimator_qs · extract_quantities · medium · needs file | Read Qto_WallBaseQuantities NetSideArea/GrossSideArea, group by storey, filter external, state openings treatment. |
| DF2<br><sub>de-s008</sub> | Mengen fuer die Ausschreibung ziehen: Mauerwerk Wandflaechen netto ohne Oeffnungen, nach Geschoss. Passt das mit Qto? | Take out masses for the tender (LV), grouped by trade. | estimator_qs · extract_quantities · medium · needs file | Read NetSideArea from wall quantities, compare with geometry-derived values, group by storey, flag inconsistencies. |
| DF3<br><sub>de-qto-s013</sub> | kannst du mir die Mauerwerk-Mengen nach Geschoss ziehen, netto ohne Öffnungen, fürs LV (GAEB) | Quantities for bill of works (GAEB) | estimator_qs · extract_quantities · medium · needs file | Compute net wall volume/area per storey excluding openings, present in table suitable for GAEB position mapping. |
| DF4<br><sub>de-struct-s012</sub> | mach mir ne Stahlliste aus dem IFC, Bewehrung nach Durchmesser, Gewicht in kg | Create rebar schedule by diameter with weight in kg | structural_engineer · extract_quantities · medium · needs file | Group IfcReinforcingBar by NominalDiameter, compute length and mass with 7850 kg/m3, output table. |
| DF5<br><sub>de-struct-s013</sub> | prüf mal ob die Fertigteile als IfcElementAssembly drin sind und die Einzelteile korrekt aggregiert | Check precast elements are IfcElementAssembly with parts correctly aggregated | bim_coordinator · validate_check · hard · needs file | List IfcElementAssembly, check IfcRelAggregates parts, PredefinedType, report orphans. |

### 7. Versions and changes

| ID | Prompt (synthetic) | EN gloss | Persona · intent · difficulty | Expected behavior (what a good assistant does) |
|---|---|---|---|---|
| DG1<br><sub>de-dach-s008</sub> | vergleich mal Stand 12 und Stand 14 vom Rohbau-IFC. was ist neu, was weg, was verschoben? GUIDs ändern sich bei uns teilweise | Compare two IFC exports and say what changed, GUIDs may have changed. | bim_coordinator · compare_versions · hard · needs file | Diff by GUID, fall back to geometry/name matching, report added/removed/moved. |
| DG2<br><sub>de-guid-s008</sub> | vergleich mal Stand KW12 und KW14 vom Archicad-IFC, welche Wandtypen wurden geaendert? GUIDs sind nicht stabil, glaub ich | Compare two Archicad IFC exports and list changed wall types | bim_manager · compare_versions · hard · needs file | Compare IfcWallType definitions and layers between versions, matching types by name when GUIDs differ, and list affected wall instances. |

### 8. Requirements: AIA, MVD, IDS, permits

| ID | Prompt (synthetic) | EN gloss | Persona · intent · difficulty | Expected behavior (what a good assistant does) |
|---|---|---|---|---|
| DH1<br><sub>de-dach-s010</sub> | was ist der Unterschied zwischen Reference View und Design Transfer View? welche nimmt man fürs Austauschen mit dem TGA Planer | Difference between Reference View and Design Transfer View, and which for exchange with the MEP planner. | student_beginner · understand_concept · easy | Explain MVDs, recommend according to purpose, note AIA/BAP should state it. |
| DH2<br><sub>de-dach-s011</sub> | prüf die IFC gegen unsere IDS vom Auftraggeber und gib mir die Fehler nach Bauteilen | Check against an IDS file. | reviewer_authority · validate_check · medium · needs file | Run IDS validation, group failures by requirement and entity, provide GUID lists. |
| DH3<br><sub>de-vm-s010</sub> | AG fordert IFC4 Reference View. Prüf mal ob die Datei wirklich RV ist und nicht 2x3 oder IFC4x3 | Check IFC4 RV vs AIA requirement | bim_manager · validate_check · easy · needs file | Read schema and view; confirm IFC4 and ReferenceView, verify constituent material sets, note deviations. |
| DH4<br><sub>de-permit-s012</sub> | Bauantrag IFC: haben alle Räume NetFloorArea und Nutzungsart? Liste die ohne bitte | Check permit data on rooms | reviewer_authority · validate_check · medium · needs file | List IfcSpace missing area or usage and report. |
| DH5<br><sub>de-cobie-s010</sub> | was muss ich in die AIA schreiben damit wir vom Bauherrn ne brauchbare IFC für den Betrieb kriegen? COBie oder was anderes | What should we require in the AIA for FM handover from IFC? | owner_client · understand_concept · medium · needs file | Explain COBie vs FM-handover MVD, list asset attributes, suggest IDS-based requirements. |
| DH6<br><sub>de-err-s009</sub> | Prüf mal das Modell auf Schemafehler, Navisworks meckert beim Öffnen | Check IFC for schema errors | bim_manager · validate_check · medium · needs file | Run validation, summarise errors by type with counts and examples. |
| DH7<br><sub>new</sub> | ist unser IFC für die Baueinreichung in Wien okay? Pset WienBV da, und Schema IFC2x3 oder IFC4 Add2 TC1? | Is our IFC fit for the Vienna building-permit submission: is the WienBV pset present and is the schema one of the allowed ones? | architect · comply_regulation · medium · needs file | Read the IFC schema; accept IFC2x3 or IFC4 Add2 TC1 and flag anything else; look for the Vienna-specific Pset 'WienBV' and the ISO 16739 standard Psets/Qtos; state clearly that the authoritative requirement is the MA 37 IDS and PDF/XLSX files, and that this check is only partial. |
| DH8<br><sub>new</sub> | hat jedes Bauteil einen eBKP-H Code? zeig mir die ohne, nach Bauteilart gruppiert | Does every component carry an eBKP-H code? List those without, grouped by element type. | bim_manager · validate_check · medium · needs file | Look for IfcClassificationReference (or a project property) with an eBKP-H code; list elements without, grouped by IFC class; do not assume DIN 276 in a Swiss project; say which classification system name was found. |

### 9. Files, conversion, clashes, special cases

| ID | Prompt (synthetic) | EN gloss | Persona · intent · difficulty | Expected behavior (what a good assistant does) |
|---|---|---|---|---|
| DI1<br><sub>de-fs-s011</sub> | die ifc ist 700 MB und solibri braucht ewig, kannst du leere psets und nicht benutzte Eigenschaften rausnehmen? | Remove unused property sets before Solibri | bim_coordinator · optimize_performance · medium · needs file | Find empty and unused property sets, strip them in a copy, validate references, report size and element counts before and after. |
| DI2<br><sub>de-viewconv-s009</sub> | brauch fuer den Bauherrn ne abgespeckte Version vom Modell, ohne TGA, als 3D-PDF oder wenigstens leichtes IFC | Make a light PDF/3D export for the client, no MEP | bim_manager · convert_format · medium · needs file | Filter out MEP classes, save reduced IFC, state 3D PDF limits. |
| DI3<br><sub>de-gis-s014</sub> | kannst du aus dem Gebäude ne Außenhülle für CityGML LoD2 ableiten? nur Dach und Wände, Geschosse bitte als Attribut | Create CityGML LoD2 shell from building. | bim_manager · convert_format · hard · needs file | Derive envelope, classify roof/wall/ground, export, record storey count attribute; note limitations. |
| DI4<br><sub>de-infra-s010</sub> | pruef mal ob im Schienenmodell die Gradiente und Trassierung sauber drin sind, inkl. Stationierung. IFC 4.3 | Check whether the rail model has alignment geometry and stationing as required by IFC-Rail. | civil_infra_engineer · validate_check · hard · needs file | Check IfcAlignmentHorizontal/Vertical, segments continuity, referents with stationing, report gaps. |
| DI5<br><sub>de-clash-s012</sub> | mach mal Kollisionsprüfung TGA gegen Tragwerk im Koordinationsmodell, Toleranz 10 mm, pro Geschoss gruppieren und als BCF raus | Clash check MEP vs structure, group by storey, export BCF | bim_coordinator · coordinate_clash · medium · needs file | Run TGA vs Tragwerk clash, group by storey, export BCF 2.1. |
| DI6<br><sub>de-coord-s011</sub> | kannst du mir Kollisionen zwischen Lüftungskanälen und Unterzügen im Koordinationsmodell raussuchen und nach Geschoss gruppieren? für die BCF Liste | Hard clashes between TGA ducts and structural beams. | bim_coordinator · coordinate_clash · hard · needs file | Run clash between IfcDuctSegment and IfcBeam across federated files, group by storey, prepare BCF-style issue list. |
| DI7<br><sub>de-eng-s013</sub> | gib mir alle Rohre mit Nennweite und Material, TGA Modell | List pipe nominal diameters | mep_engineer · query_model_data · easy · needs file | List IfcPipeSegment nominal diameter and material. |
| DI8<br><sub>de-mep-s007</sub> | gib mir alle Rohre mit DN und Volumenstrom aus dem Pset, MagiCAD Export, als Liste pro Gewerk | Nominal diameter and flow for all pipes | mep_engineer · query_model_data · medium · needs file | Read IfcPipeSegment psets (Pset_PipeSegmentTypeCommon, vendor psets), return NominalDiameter and flow, grouped by system; note missing values. |
| DI9<br><sub>mx-mcl-s015</sub> | wie krieg ich die Farben von Archicad IFC in Revit rueber? Oberflaechen sind alle grau | How to keep colours between Archicad and Revit | architect · how_to · medium | Explain Revit import ignores styles, use link vs open, materials mapping; check file for styles first. |

Typing variants to test robustness (same kind of request, different surface form; all in the dataset): DA6 (`Pruef mal ...`, transliterated umlauts), DF2 (`Mengen fuer die Ausschreibung ziehen: ...`), DE3 (`pruef mal ob alle Raeume ne Nutzung haben ...`, with "ne" for "eine"; its dataset id starts `en-fmor` although the text is German).

## Tips for generating authentic prompts in this language

**Do**
- Write short, imperative, lower-case requests with "mal", "mir", "bitte" and no greeting: "prüf mal ...", "zeig mir ...", "vergleich mal ...".
- Name the discipline and the purpose in the same breath ("TGA gegen Tragwerk", "fürs LV", "für die Durchbruchsplanung morgen").
- Use real German-office vocabulary: Durchbruch, Geschoss, Fachmodell, Stand 12 / KW14, AIA, BAP, KG, F90, NGF, OKFF/OKRD.
- Keep IFC class names in English exactly as in the schema (`IfcBuildingElementProxy`, `IfcOpeningElement`, `IfcColumn`) and mix in Denglish nouns (Proxy, Pset, GUID, Mapping, Export).
- Refer to a model revision ("Stand 12 und Stand 14", "KW12") instead of a file path; omit the Revit version and IFC schema in most prompts.
- Vary the register: a polite English bug report with build number and repro steps for developers; a clipped chat line for coordinators.
- Include a deadline or a consequence now and then ("sonst fliegen wir beim AIA-Check raus").
- For a minority of prompts, type without umlauts (ae/oe/ue) and without capitals.

**Don't**
- Do not write textbook German ("Bitte überprüfen Sie, ob ...") for coordinators; keep formal "Sie" for authority or client roles (reviewer_authority, owner_client).
- Do not translate schema names into German ("Gebäudeelement-Proxy"): the data shows English class names inside German sentences.
- Do not assume DIN 276 or GAEB applies in Austria or Switzerland; use ÖNORM / eBKP-H flavoured prompts there (see the two `new` prompts).
- Do not claim these phrasings come from real forum posts; the real German corpus is only blog titles and official pages.
- Do not invent an IFC version requirement per country; "correct" depends on the project's AIA/BAP.
