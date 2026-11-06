# Dutch: how people ask about IFC, BIM and Revit

Language code `nl` (Netherlands, with a note on Flanders/Belgium and Luxembourg). Built from research wave 1 (collected 2026-11-06).

**Read this first: what the Dutch data really is.**
The knowledge base holds 35 records tagged `nl` (21 real, 14 synthetic). The web-search budget was exhausted before the first query, so no open practitioner forum was reached (Autodesk NL, Graphisoft NL, bimconnected, LinkedIn, Reddit, bimnieuws.nl: blocked, expired certificate or not resolving). The real Dutch records therefore come from two kinds of places:

| Kind | Count | What it is |
|---|---|---|
| GitHub issues of Dutch standards bodies and open-source projects (digiGO `nl-digigo`, Aedes, CROW IMBOR, OpenAEC Foundation) | 14 | Written in Dutch, mostly by working-group members and project maintainers: backlog items, review remarks, consultation comments, a few user questions. This is a **specification voice**, not the "my export is broken" voice of a forum |
| Official digiGO pages (BIM basis ILS chapters, NAA.K.T.) | 7 | Normative text. The dataset's "question" is a paraphrase of what the page answers |
| Dutch-context records tagged `en` | 11 | English or Dutch-titled issues from Dutch users (Revit parameter mapping with Dutch parameter names, OpenAEC validator issues, bSDD plugin). Listed separately |
| Synthetic Dutch prompts | 14 in the data, plus 16 new here | Written from jargon in the sources, not copied from real posts |

Expect the data to over-represent classification (NL-SfB), the national information delivery specification (BIM basis ILS) and model checking, and to under-represent plain "how do I export" questions.

Related docs: [Netherlands, Belgium, Luxembourg: BIM/IFC requirements](../../02_standards_regulations/national/netherlands_belgium_luxembourg.md); [classification, COBie and FM](../by_topic/classification_cobie_fm.md); [validation, IDS and model checking](../by_topic/validation_ids_model_checking.md); [coordinates and georeferencing](../by_topic/coordinates_georef_units_levels.md); [materials, spaces, zones](../by_topic/materials_spaces_zones.md); [multilingual glossary](../../08_glossary/glossary_multilingual.md); [spatial structure basics](../../01_ifc_basics/04_spatial_structure_and_relationships.md).

## Where people ask

| Place | Kind | What we saw | Access note |
|---|---|---|---|
| [digiGO](https://www.digigo.nu/) (successor of BIM Loket; bimloket.nl redirects here) | Official portal for BIM basis ILS, NL-SfB, NLCS, IMWO | 7 chapters of the BIM basis ILS read; per-software manuals and Solibri/BIMcollab check guides exist | Open. The Revit manual PDF could not be parsed as text |
| GitHub [nl-digigo](https://github.com/nl-digigo) (NLCS, imwo, GeoBIM_Georefereren) | Standards issue trackers | User questions and consultation remarks on NLCS vs NL-SfB, Revit templates, installations, georeferencing | Open. API rate limit hit after the first batch, so only part of the repos was mined |
| GitHub [OpenAEC-Foundation](https://github.com/OpenAEC-Foundation/OpenAEC-BIM-validator) (BIM validator, open-bim-platform) | Open-source Dutch project backlog | Structured Dutch specs (Waarom / Nu / Gevraagd) for NL-SfB checks, georeference checks, takeoff, Smart Views, FM | Open |
| GitHub Aedes-datastandaarden, Stichting-CROW/imbor, buildingsmart-community/bSDD-Revit-plugin | Sector standards trackers | NL-SfB code corrections for housing corporations, NAA.K.T. in IMBOR, bSDD plugin bug | Open |
| Autodesk NL, Graphisoft NL, bimconnected.com, bimnieuws.nl, LinkedIn, Reddit, BIMcollab/Solibri knowledge bases, Flemish sources (Vlaamse overheid, Digitaal Vlaanderen, NBN, Agoria) | Where practitioners most likely ask | **Not reached** (403, expired certificate, not resolving, or never tried). Activity unknown | Gap |

Belgium and Luxembourg: no Flemish or Walloon posts were found. The national doc covers buildingSMART Belgium, a Brussels Airport "IFC-first" policy and CRTI-B / BIMids in Luxembourg, but no questions.

## Top themes (ranked)

| Rank | Theme | What people want | Evidence |
|---|---|---|---|
| 1 | NL-SfB 4-digit codes per element, and whether the code fits the IFC class | Every object carries a valid code; an IFC wall must not have a door code; where the code lives (`IfcClassificationReference`) | OpenAEC #22, Aedes ILS-woco #2, NLCS #38, bSDD plugin #77 |
| 2 | Correct IFC entity and `TypeEnumeration` instead of `IfcBuildingElementProxy` | Export settings that land elements in the right class | ILS chapter 3.4 |
| 3 | Georeferencing and shared origin ("nulpunt") | Aspect models lie on the same origin so clash detection means something; RD / EPSG:28992 via `IfcMapConversion` | OpenAEC #21, GeoBIM_Georefereren #5, ILS 3.2 |
| 4 | Checking: IDS, Solibri rules, BIMcollab checks, Smart Views | Machine-checkable delivery agreements; colour or filter by missing property | OpenAEC #17, #22 |
| 5 | Storey structure and naming | Only `IfcBuildingStorey`, names like "00 begane grond", intermediate floors "00a" | ILS 3.3 |
| 6 | Spaces and zones | `IfcSpace` min 1.5 m net height, `Name` plus `ObjectType` (Bouwbesluit function), `IfcZone` for dwelling type or fire compartment, area types GO/BVO | ILS 4.1 |
| 7 | Material naming (NAA.K.T.) and `IfcMaterial` on every object | One naming pattern "NAam_Kenmerk_Toepassing"; no performance requirements in names | ILS 4.7, NAA.K.T. page, IMBOR #1254 |
| 8 | Property sets | `Pset_WallCommon` FireRating, LoadBearing, IsExternal; custom set names not starting with "Pset"; IFC2x3 vs IFC4 gaps | ILS 3.7, revit-ifc #858 and #125 (Dutch parameter names) |
| 9 | Quantities per classification for cost estimating | "m2 binnenwand per NL-SfB-code", "hebben alle 212 deuren een FireRating?" | OpenAEC #19, NLCS #687 |
| 10 | Linking NLCS (2D/infra layers) and NL-SfB to 3D, IFC 4.3, bSDD | One classification story from model to cost | NLCS #38, #147 |
| 11 | MEP systems and installation codes | `IfcDistributionSystem` vs NL-SfB installation codes | imwo #52 |
| 12 | Software manuals per tool, FM handover | Revit, Archicad, Tekla, Vectorworks, BricsCAD, SketchUp; asset linking by GlobalId and NEN 2767 condition | digiGO manuals; open-bim-platform #10 |

## Local ecosystem

Details and confidence marks: [national doc](../../02_standards_regulations/national/netherlands_belgium_luxembourg.md).

- **digiGO** maintains the open standards: **BIM basis ILS** (information delivery specification; v1.0 Nov 2023, v2.0 Sept 2024; German version called "ILH", English "BIM base IDS" which is **not** the buildingSMART IDS), ILS Ontwerp & Engineering, NLCS, ILS Configurator (can export an IDS file), NAA.K.T. material naming with an IDS file.
- **NL-SfB**: the classification for building parts; ownership moved to Ketenstandaard Bouw en Techniek on 1 April 2026, with a revised version announced for May 2026 (details of the new code format unverified).
- **IFC is "pas toe of leg uit"** (comply or explain) for Dutch public bodies buying ICT for 3D model exchange; the registered version is IFC 2x3 TC1, while practice moves to IFC4 and 4.3. Public clients: Rijksvastgoedbedrijf (RVB BIM Norm, older than the ILS, applies only if the contract says so), Rijkswaterstaat and ProRail (requirements not read).
- **Georeferencing:** national grid RD (EPSG:28992) with NAP heights; the practice guideline (Geonovum, now digiGO) and the BIM basis ILS rule "local origin near zero, outside the building".
- **Other Dutch standards named in the records:** IMBOR (CROW), GWSW (sewer), IMWO, NEN 2580 (areas), NEN 2660, NEN 2767 (condition), ICDD-NL, Bouwbesluit / Bbl.
- **Software:** Revit, Archicad, Tekla, Allplan, Vectorworks, BricsCAD, SketchUp, DDS-CAD, HiCAD (digiGO manuals); checking with Solibri and BIMcollab; Dalux, Navisworks; open source: IfcOpenShell, OpenAEC BIM validator, open-bim-platform, bSDD Revit plugin. Community sample data: Schependomlaan IFC2x3 model.
- **Belgium/Luxembourg** (national doc, no questions): buildingSMART Belgium, Brussels Airport IFC-first policy, CRTI-B and BIMids in Luxembourg; a Belgian test model may use French ("rez-de-chaussée") or Dutch ("gelijkvloers") storey names.

## How people write

### Evidence status

| Statement type | Source |
|---|---|
| Observed | The 21 Dutch records (GitHub titles and bodies, official pages) |
| Inferred | Chat-style request phrasing, from 14 synthetic prompts plus the 16 new ones written here |

### Register and structure (observed)

- **Informal-professional "je/jij"**, no formal "u". Maintainers write structured issues with fixed headings: "Waarom / Nu / Gevraagd / Klaar". Working-group notes are outlines ("Wat / Hoe ongeveer"; "te beschrijven wat het probleem is en wat we willen bereiken").
- **Very short corrections** exist too: one issue just says that "windveer" is roof finishing, so NL-SfB code 27 is wrong and should be 47 (47.12), no greeting.
- **Hedged and polite:** "voor zover ik weet", "staat er op jullie roadmap een Revit template oid?" ("oid" = "of iets dergelijks", or the like).
- **Quoted concrete examples:** "hebben alle 212 deuren een FireRating?", "m2 binnenwand per NL-SfB-code", "rood voor 'LoadBearing ontbreekt'".
- **Review remarks as rhetorical questions:** "Waarom geen verwijzing naar Systems (IfcDistributionSystem)?"
- **Synthetic prompts** (n=14): 10 to 21 words, median 14.5; all start in lower case; 13 contain a question mark (often mid-sentence); polite particles are rare ("graag" in 1, "kun je" in 1); informal abbreviations: "bijv", "ipv", "excel kan?".

### Jargon and slang table

| Term | Meaning | Standard term |
|---|---|---|
| nulpunt | model origin / zero point | project/shared origin, `IfcMapConversion` |
| bouwlaag | building storey | `IfcBuildingStorey`; "00 begane grond", "-1 kelder", "00a" for intermediate floors |
| hulpbouwlaag | auxiliary storey, only allowed in source files | extra level not exported |
| peil / peil = 0 | level / datum agreement | reference elevation (NAP) |
| stramien | structural grid | `IfcGrid` |
| aspectmodel / deelmodel | discipline model | discipline model |
| federatie | combined model of several aspect models | federated model |
| ruimte | space | `IfcSpace` |
| GO / BVO / VG | usable area (gebruiksoppervlak) / gross floor area (bruto vloeroppervlak) / habitable area (verblijfsgebied, a Bouwbesluit term); the data only lists the abbreviations, the expansions are general knowledge | area quantities (NEN 2580) |
| kozijn | window or door frame | `IfcWindow` / `IfcDoor` |
| sparing / sparingscoördinatie | opening / penetration; coordination of openings | `IfcOpeningElement` |
| ILS | information delivery specification | EIR-like specification in ISO 19650 sense; **not** buildingSMART IDS |
| RVB | requirements document ("Rijksvastgoedbedrijf" is also abbreviated RVB or Rgd) | EIR or the government real-estate agency, depending on context |
| BUP | BIM execution plan | BEP |
| NL-SfB | 4-digit building-part classification | `IfcClassificationReference` |
| NAA.K.T. | material naming pattern "Naam_Kenmerk_Toepassing" | `IfcMaterial.Name` |
| brandwerendheid | fire resistance | `Pset_WallCommon.FireRating` |
| draagt / dragend | load-bearing | `LoadBearing` |
| hoeveelheden / takeoff | quantities | `Qto_*BaseQuantities` |
| clashdetectie | clash detection | clash check |
| opdrachtgever / opdrachtnemer | client / contractor | appointing / appointed party |
| woningcorporatie | housing association | Aedes members, ILS-woco |
| windveer | wind feather (barge board at roof edge) | roof finishing, NL-SfB 47.12 per the issue |

### Misspellings, name variants, code-switching (observed)

- **Heavy code-switching:** English tool and IFC terms inside Dutch sentences: "aspectmodel", "export settings", "Smart Views", "clashdetectie", "takeoff", "federatie", "Pset", "proxy", "GUID". Class names are written as in the schema (`IfcBuildingElementProxy`, `IfcSpace`).
- **Typos in English-language Dutch posts:** "swiching", "avialable" (bSDD plugin issue).
- **Name variants:** "NL-SfB", "NL/SfB", "NL-sfb" (all seen); "BIM basis ILS", "BIM Basis ILS", "Basis ILS"; "IFC2x3" vs "IFC 2x3 TC1"; "BIM Loket" (old name) vs digiGO; "Rgd" vs "RVB".
- **Dutch parameter names in tools:** a Dutch FireRating parameter ("brandwerendheid") that fails to reach `Pset_WallCommon.FireRating` (revit-ifc #858, #125).

### Tone, context given and omitted

- **Tone:** neutral to mildly frustrated; the most frustrated source is an issue about federated models that do not share an origin ("gaat vaak mis doordat modellen niet op hetzelfde nulpunt liggen").
- **Context given:** the standard name (BIM basis ILS), code numbers (21, 27, 47.12), EPSG codes (28992), IFC class names, the check tool (Solibri, BIMcollab).
- **Context omitted:** Revit version, IFC schema version, file name; in chat prompts also the model reference ("dit model", "het constructie ifc v3 en v4").

## Real questions

"Paraphrase in original language" is the dataset's Dutch paraphrase (not a verbatim copy). Official-page rows paraphrase the page's rule, so they are statements, not questions.

### A. GitHub issues in Dutch (14)

| # | Original title (verbatim) | Paraphrase in original language | Gist in English | Persona · type · year | Source |
|---|---|---|---|---|---|
| 1 | NL-SfB code Windveer | windveer is dakafwerking, NL-SfB code 27 is daarom niet juist, moet 47 zijn (47.12) | Windveer is roof finishing so NL-SfB code 27 is wrong, should be 47.12 | other · feature_request · 2026 | [GH Aedes-datastandaarden/ILS-woco#2](https://github.com/Aedes-datastandaarden/ILS-woco/issues/2) (github_issue) |
| 2 | NL-SfB-classificatie inhoudelijk toetsen aan de codelijst | IDS controleert alleen het patroon van de NL-SfB code, niet of de code bij het element past; IfcWall met 32.xx is formeel goed en inhoudelijk fout. Wil codelijst, koppeling IfcWall->21/22, IfcDoor->31/32 en controle waar de code staat (IfcClassificationReference) | An IDS can check the pattern of an NL-SfB code but not whether the code fits the element; an IfcWall with 32.xx (doors) passes formally | bim_coordinator · feature_request · 2026 | [GH OpenAEC-Foundation/OpenAEC-BIM-validator#22](https://github.com/OpenAEC-Foundation/OpenAEC-BIM-validator/issues/22) (github_issue) |
| 3 | integratie tussen de NLCS en de NL/SfB codering? | In Revit wordt informatie vooral toegekend op basis van NL/SfB via Assembly Code en Assembly Description, bouwkundig ingestoken. Kan NLCS gekoppeld worden aan elementen in Revit? | In Revit info is assigned via NL/SfB Assembly Code and Description; can NLCS codes be linked to Revit elements or integrated with NL-SfB? | bim_coordinator · how_to · 2023 | [GH nl-digigo/NLCS#38](https://github.com/nl-digigo/NLCS/issues/38) (github_issue) |
| 4 | Onderzoeken aansluiting op IFC 4.3 | voor uitwisseling van 3D BIM-modellen is een classificatie nodig zoals NL-sfb; onderzoek hoe NLCS aligned kan worden met IFC 4.3, evt via bSDD | Exchanging 3D BIM models needs a classification like NL-SfB; research aligning NLCS with IFC 4.3 and bSDD | developer_programmer · feature_request · 2023 | [GH nl-digigo/NLCS#147](https://github.com/nl-digigo/NLCS/issues/147) (github_issue) |
| 5 | Verduidelijking samenhang GEO Coordinatiepunt en BIM nulpunt (Bijlage 1) | GEO Coordinatiepunt en BIM nulpunt los gedefinieerd, maar samen beschrijven ze dezelfde transformatie als IfcMapConversion: translatie op het GEO punt, rotatie tussen beide punten | GEO coordination point and BIM origin are defined separately but together equal IfcMapConversion; clarify their relationship | bim_manager · opinion · 2026 | [GH nl-digigo/GeoBIM_Georefereren#5](https://github.com/nl-digigo/GeoBIM_Georefereren/issues/5) (github_issue) |
| 6 | Aansluiten op materiaalbenaningen van de NAA.K.T | GWSW Werkgroep Basis wil aansluiten op de materiaalbenamingen van de NAA.K.T., namen (skos:prefLabel) aanpassen op de norm | GWSW working group asks to align IMBOR names with NAA.K.T. material names | developer_programmer · feature_request · 2024 | [GH Stichting-CROW/imbor#1254](https://github.com/Stichting-CROW/imbor/issues/1254) (github_issue) |
| 7 | Georeferentie en ligging van modellen controleren bij federatie | In een federatie van bouwkunde, constructie en installaties gaat het vaak mis doordat modellen niet op hetzelfde nulpunt liggen. Rapporteer per model schema, lengte-eenheid, IfcSite ref, MapConversion (EPSG 28992), afstand tot oorsprong | Federated models often don't share the same origin so clash detection is pointless; report CRS, units, distance to origin per model | bim_coordinator · feature_request · 2026 | [GH OpenAEC-Foundation/OpenAEC-BIM-validator#21](https://github.com/OpenAEC-Foundation/OpenAEC-BIM-validator/issues/21) (github_issue) |
| 8 | BIM Basis Infra / BIM Basis ILS -> BIM Basis Stedelijk Spoor | Werkpakket B BIM Basis Infra Stedelijk Spoor: te beschrijven wat het probleem is en wat we willen bereiken | Describe problem and goal for BIM Basis Infra / urban rail based on BIM basis ILS | bim_manager · how_to · 2023 | [GH nl-digigo/NLCS#189](https://github.com/nl-digigo/NLCS/issues/189) (github_issue) |
| 9 | Hoeveelheden en informatietabellen uit het model (takeoff naar Excel) | Opdrachtgever en calculator gebruiken tabellen om te controleren wat geleverd is: 'hebben alle 212 deuren een FireRating?' of 'm2 binnenwand per NL-SfB-code' | Quantity tables from the model to Excel: e.g. do all 212 doors have FireRating, m2 interior wall per NL-SfB code | estimator_qs · feature_request · 2026 | [GH OpenAEC-Foundation/OpenAEC-BIM-validator#19](https://github.com/OpenAEC-Foundation/OpenAEC-BIM-validator/issues/19) (github_issue) |
| 10 | Kleuren en filteren op eigenschap (Smart Views) | BIMcollab Smart Views, Dalux-filters en Solibri checking views kleuren op eigenschap: per brandwerendheid, NL-SfB-code, of rood voor 'LoadBearing ontbreekt' | Colour/filter elements by property (fire rating, NL-SfB code, red for 'LoadBearing missing') to see model gaps at a glance | bim_coordinator · feature_request · 2026 | [GH OpenAEC-Foundation/OpenAEC-BIM-validator#17](https://github.com/OpenAEC-Foundation/OpenAEC-BIM-validator/issues/17) (github_issue) |
| 11 | gebruikersvraag: Revit template | staat er op jullie roadmap de ontwikkeling van een Revit template oid? | Does the NLCS roadmap include a Revit template? | bim_manager · feature_request · 2023 | [GH nl-digigo/NLCS#238](https://github.com/nl-digigo/NLCS/issues/238) (github_issue) |
| 12 | Ref #4: [installaties] - keuze nader toelichten | Waarom geen verwijzing naar Systems (IfcDistributionSystem)? NL/SfB-codes sluiten niet geheel aan op de praktijk; is classificeren op NL-SfB echt de bedoeling? | Why no reference to IfcDistributionSystem; NL-SfB codes do not fully match practice for installations - is NL-SfB really the intent? | mep_engineer · opinion · 2026 | [GH nl-digigo/imwo#52](https://github.com/nl-digigo/imwo/issues/52) (github_issue) |
| 13 | Experiment Hoeveelheden berekenen met NLCS Classificatie VH door VolkerWessels | Analyse Revit-workflow, beschrijving gewenste informatiestructuur, realiseren gewenste output in IFC voor eerste testbatch, testen in IBIS | Experiment: quantity take-off with NLCS classification; analyse Revit workflow, deliver desired IFC output for test batch and test it in IBIS | estimator_qs · knowledge · 2025 | [GH nl-digigo/NLCS#687](https://github.com/nl-digigo/NLCS/issues/687) (github_issue) |
| 14 | FM-toepassing: gebouwbeheer op het model |  | Facility management app on the as-built model: link assets via GlobalId, maintenance plans, fault reports to ERP work orders, NEN 2767 condition. | facility_manager · feature_request · 2026 | [GH OpenAEC-Foundation/open-bim-platform#10](https://github.com/OpenAEC-Foundation/open-bim-platform/issues/10) (github_issue) |

### B. Official digiGO pages (7)

| # | Original title (verbatim) | Paraphrase in original language | Gist in English | Persona · type · year | Source |
|---|---|---|---|---|---|
| 1 | 3.4 Correct gebruik entiteiten | Zonder de correcte exportinstelling wordt een element vaak een BuildingElementProxy; gebruik TypeEnumeration, NOTDEFINED als je niet kiest | Without correct export settings an element often becomes IfcBuildingElementProxy; use TypeEnumeration, USERDEFINED only when strictly needed | bim_coordinator · knowledge · 2024 | [digigo.nu](https://www.digigo.nu/ilsen-en-richtlijnen/bim-basis-ils/3-4-correct-gebruik-entiteiten) (official_doc) |
| 2 | 3.3 Bouwlaagindeling en naamgeving | Naamgeving bouwlagen gelijk in alle aspectmodellen; hulpbouwlagen alleen in bronbestanden; tussenverdieping met letter (00a) | One IfcBuildingStorey per floor, numeric-sortable names like '-1 kelder', '00 begane grond'; foundations not a separate storey | architect · knowledge · 2024 | [digigo.nu](https://www.digigo.nu/ilsen-en-richtlijnen/bim-basis-ils/3-3-bouwlaagindeling-en-naamgeving) (official_doc) |
| 3 | 3.2 Lokale positie | positie van aspectmodellen ten opzichte van het nulpunt coordineren; nulpunt buiten het gebouw; referentieobject 100% overlappend | Coordinate aspect models relative to an origin placed outside the building; optional reference object; geo-reference as model property | bim_manager · knowledge · 2024 | [digigo.nu](https://www.digigo.nu/ilsen-en-richtlijnen/bim-basis-ils/3-2-lokale-positie) (official_doc) |
| 4 | 3.7 Gebruik propertysets | Pset_WallCommon: FireRating, LoadBearing, IsExternal; eigen PropertySet-namen mogen niet met Pset beginnen | Pset_PileCommon has no LoadBearing in IFC2x3 TC1, use a custom property set; included from IFC4.0.2 | structural_engineer · knowledge · 2024 | [digigo.nu](https://www.digigo.nu/ilsen-en-richtlijnen/bim-basis-ils/3-7-gebruik-propertysets) (official_doc) |
| 5 | 4.1 Ruimten | Ruimte: toegankelijk, minimaal 1,5 m netto hoogte; Name (toilet) en ObjectType (toiletruimte); zones voor woning, brandcompartiment | IfcSpace needs min 1.5 m net height; Name plus ObjectType (Bouwbesluit function); IfcZone for dwelling type etc. | architect · knowledge · 2024 | [digigo.nu](https://www.digigo.nu/ilsen-en-richtlijnen/bim-basis-ils/4-1-ruimten) (official_doc) |
| 6 | 4.7 Materiaal | Kwaliteits- en prestatie-eisen horen niet in de materiaalnaam; NAAm_Kenmerk_Toepassing | Every object gets an IfcMaterial; no performance requirements or NL-SfB codes in material names; use NAA.K.T. structure | bim_coordinator · knowledge · 2024 | [digigo.nu](https://www.digigo.nu/ilsen-en-richtlijnen/bim-basis-ils/4-7-materiaal) (official_doc) |
| 7 | NAA.K.T. Eenduidige materiaalbenaming | Materiaalnamen verschillen: prefabbeton, gewapend beton, grindbeton, ihw, ihwg, tpg; computers kunnen dit niet betrouwbaar interpreteren | Material names vary (prefab concrete, grindbeton, ihw); computers cannot interpret; NAA.K.T. fixes order | bim_manager · knowledge · 2024 | [digigo.nu](https://www.digigo.nu/ilsen-en-richtlijnen/bim-basis-ils/praktijk/1-naa-k-t-eenduidige-materiaalbenaming) (official_doc) |

### C. Dutch-context records tagged `en` (11)

Titles are verbatim. Dutch-titled ones keep their Dutch wording.

| # | Original title (verbatim) | Paraphrase in original language | Gist in English | Persona · type · year | Source |
|---|---|---|---|---|---|
| 1 | NL-SfB 2005 dictionary stays green after swiching building element |  | After switching the building element, the NL-SfB 2005 dictionary validation stays green even though it is unavailable for the new element | bim_coordinator · troubleshooting · 2024 | [GH buildingsmart-community/bSDD-Revit-plugin#77](https://github.com/buildingsmart-community/bSDD-Revit-plugin/issues/77) (github_issue) |
| 2 | Clashdetectie en dubbele elementen |  | Tool lacks geometric clash detection and duplicate/overlapping element checks that Solibri and BIMcollab Zoom have | developer_programmer · feature_request · 2026 | [GH OpenAEC-Foundation/OpenAEC-BIM-validator#12](https://github.com/OpenAEC-Foundation/OpenAEC-BIM-validator/issues/12) (github_issue) |
| 3 | Kleuren en filteren op eigenschap (Smart Views) |  | Color and filter elements by any property like Smart Views (fire rating, NL-SfB code, missing LoadBearing) | developer_programmer · feature_request · 2026 | [GH OpenAEC-Foundation/OpenAEC-BIM-validator#17](https://github.com/OpenAEC-Foundation/OpenAEC-BIM-validator/issues/17) (github_issue) |
| 4 | NL-SfB-classificatie inhoudelijk toetsen aan de codelijst |  | Check NL-SfB classification content against the code list | developer_programmer · feature_request · 2026 | [GH OpenAEC-Foundation/OpenAEC-BIM-validator#22](https://github.com/OpenAEC-Foundation/OpenAEC-BIM-validator/issues/22) (github_issue) |
| 5 | Regels buiten IDS: vrije ruimte, toegankelijkheid en ruimtes (Bbl) |  | Rules beyond IDS: clearance, accessibility and spaces under Dutch Bbl | developer_programmer · feature_request · 2026 | [GH OpenAEC-Foundation/OpenAEC-BIM-validator#20](https://github.com/OpenAEC-Foundation/OpenAEC-BIM-validator/issues/20) (github_issue) |
| 6 | Georeferentie en ligging van modellen controleren bij federatie |  | Check georeference and position of models when federating | bim_coordinator · feature_request · 2026 | [GH OpenAEC-Foundation/OpenAEC-BIM-validator#21](https://github.com/OpenAEC-Foundation/OpenAEC-BIM-validator/issues/21) (github_issue) |
| 7 | Ifc Custom Property set: Double Psets / Property not written to Ifc |  | Custom pset appears twice in Solibri and a Classification Code parameter (NL-SfB) is not written, because building elements use the type Assembly Code and distribution elements use instance Classification Code. | bim_coordinator · troubleshooting · 2020 | [GH Autodesk/revit-ifc#252](https://github.com/Autodesk/revit-ifc/issues/252) (github_issue) |
| 8 | PR: Export IFC - Export parameter mapping table not working for IFC2X3 schema |  | Parameter mapping table txt is not applied for IFC2X3 export: Dutch fire-rating parameter does not reach Pset_WallCommon.FireRating. | bim_coordinator · troubleshooting · 2025 | [GH Autodesk/revit-ifc#858](https://github.com/Autodesk/revit-ifc/issues/858) (github_issue) |
| 9 | Parameter mapping |  | Own ParameterMappingTable with Dutch FireRating parameter adds an extra value to Pset_WallCommon rather than overriding Revit's Fire Rating. | bim_coordinator · troubleshooting · 2019 | [GH Autodesk/revit-ifc#125](https://github.com/Autodesk/revit-ifc/issues/125) (github_issue) |
| 10 | bSDD classification mapping and specific pset values |  | bSDD NL-SfB 22.21 maps to IfcWall LoadBearing=True/IsExternal=False but the class page leaves values empty. | developer_programmer · how_to · 2022 | [forums.buildingsmart.org](https://forums.buildingsmart.org/t/bsdd-classification-mapping-and-specific-pset-values/4538) (forum) |
| 11 | bSDD KeyError: 'referenceCode when adding classification |  | KeyError referenceCode adding NL-SfB classification from bSDD | architect · troubleshooting · 2026 | [GH IfcOpenShell/IfcOpenShell#9034](https://github.com/IfcOpenShell/IfcOpenShell/issues/9034) (github_issue) |

Counting: 21 Dutch-language records plus 11 Dutch-context records = 32.

## Ready test prompts

All prompts are **synthetic**. 14 are verbatim from the dataset (source id shown); 16 are new, written for this document from rules and wording in the sources above (marked `new`). Difficulty tags for dataset prompts come from the dataset; new prompts are tagged by the editor. Expected behaviors are in English. Where a prompt relies on a rule of the BIM basis ILS, a good assistant should name the rule as "per BIM basis ILS (digiGO)" and say the ILS version it assumed, because the rules differ by version and are not a law.

### 1. Classification and entities

| ID | Prompt (synthetic) | EN gloss | Persona · intent · difficulty | Expected behavior (what a good assistant does) |
|---|---|---|---|---|
| NA1<br><sub>nl-dutch-s002</sub> | welke elementen hebben geen NL-SfB code of niet 4 cijfers? lijst per IFC class graag | Which elements lack a 4-digit NL-SfB code | bim_coordinator · validate_check · medium · needs file | Scan classification references/Pset for NL-SfB; list elements missing or malformed per class with counts. |
| NA2<br><sub>nl-dutch-s003</sub> | check of de NL-SfB codes wel kloppen bij het element, die IfcWall met 32.xx bijv | Does code match element type | bim_coordinator · validate_check · hard · needs file | Check main group vs IFC class (walls 21/22, doors 31/32), report mismatches, state mapping is interpretive. |
| NA3<br><sub>nl-dutch-s001</sub> | hoeveel IfcBuildingElementProxy zitten er in dit model en uit welke Revit categorieen komen die? wil ze goed mappen voor de export | How many proxies and from which Revit categories | bim_coordinator · validate_check · medium · needs file | Count IfcBuildingElementProxy, group by Revit category/ObjectType, suggest IfcExportAs per group. |
| NA4<br><sub>nl-dutch-s011</sub> | mijn kozijn familie komt als proxy in het ifc ipv IfcWindow, wat moet ik instellen in Revit? | Revit generic model family exports as proxy | bim_coordinator · troubleshoot_export · easy | Explain IfcExportAs, category mapping, check export setup. |
| NA5<br><sub>nl-dutch-s008</sub> | materiaalnamen volgens NAA.K.T.? geef afwijkingen, en welke objecten hebben geen IfcMaterial | Materials not conforming to NAA.K.T. | bim_coordinator · validate_check · medium · needs file | List materials, flag names with NL-SfB codes or performance, elements without material. |
| NA6<br><sub>new</sub> | staat de NL-SfB code als IfcClassificationReference in het bestand, of in een eigen pset? geef een telling per IFC class | Is the NL-SfB code stored as an IfcClassificationReference or in a custom pset? Give a count per IFC class. | bim_coordinator · query_model_data · medium · needs file | Count elements per IFC class that carry an IfcClassificationReference with source NL-SfB, and elements where a code-like value sits only in a custom property; report both and the elements with neither; state that which location a project expects is defined by its ILS or IDS. |

### 2. Storeys, origin and georeference

| ID | Prompt (synthetic) | EN gloss | Persona · intent · difficulty | Expected behavior (what a good assistant does) |
|---|---|---|---|---|
| NB1<br><sub>nl-dutch-s004</sub> | kloppen de bouwlagen met de ILS? alleen IfcBuildingStorey, namen als '00 begane grond', en elk element aan de juiste laag | Check storey naming per BIM basis ILS | bim_coordinator · validate_check · medium · needs file | List storeys, check naming pattern, elements without storey, auxiliary storeys. |
| NB2<br><sub>nl-dutch-s007</sub> | architectuur en constructie liggen niet op elkaar, check nulpunt en IfcMapConversion, RD of lokaal? | Two models do not line up; check coordinates | bim_manager · validate_check · hard · needs file | Read IfcSite, IfcMapConversion/IfcProjectedCRS, units, bbox offset; diagnose. |
| NB3<br><sub>new</sub> | tussenverdieping heet bij ons 00a. klopt de naamgeving van de bouwlagen in alle drie de aspectmodellen? | Our mezzanine is called 00a. Are storey names consistent across the three discipline models? | bim_coordinator · validate_check · medium · needs file | Load the three files; list IfcBuildingStorey names and elevations per file; compare names across models; flag names that do not sort numerically or differ between files; mention that intermediate floors take a letter suffix and auxiliary levels should not be exported. |
| NB4<br><sub>new</sub> | ligt het nulpunt van dit aspectmodel buiten het gebouw, bij het eerste stramienkruispunt? hoe ver zit het ernaast? | Is the model origin outside the building near the first grid intersection, and how far off is it? | bim_manager · validate_check · hard · needs file | Read IfcSite/IfcBuilding placements, bounding box and, if present, IfcGrid; compute the distance of the origin to the building footprint and to the first grid intersection; report clearly that this is a recommendation in the BIM basis ILS, not a hard rule; say if no grid is modelled. |
| NB5<br><sub>new</sub> | zit er een IfcMapConversion in met EPSG 28992 en NAP, of is het alleen lokaal? en is het IFC2x3? | Does the file carry an IfcMapConversion with EPSG 28992 and NAP heights, or is it local only? Is it IFC2x3? | architect · query_model_data · medium · needs file | Read FILE_SCHEMA first; if IFC2x3 explain there is no IfcMapConversion and look for a property-set workaround; if IFC4+ read IfcMapConversion and IfcProjectedCRS (name, EPSG code, eastings/northings, rotation, height datum); report what is missing. |

### 3. Spaces, openings, systems

| ID | Prompt (synthetic) | EN gloss | Persona · intent · difficulty | Expected behavior (what a good assistant does) |
|---|---|---|---|---|
| NC1<br><sub>nl-dutch-s006</sub> | ruimten check: hebben alle IfcSpace een Name en ObjectType (bouwbesluit functie) en zitten ze in een zone per woningtype? | Check spaces: Name, ObjectType, height >=1.5 m, zones | architect · validate_check · medium · needs file | Check IfcSpace attributes, IfcZone membership, report gaps. |
| NC2<br><sub>nl-dutch-s013</sub> | welke installatieobjecten zitten niet in een IfcSystem? en hebben ze NL-SfB 5x codes? | MEP objects without IfcSystem | mep_engineer · validate_check · medium · needs file | List MEP elements w/o system assignment and classification. |
| NC3<br><sub>new</sub> | zijn er IfcSpaces met een netto hoogte onder 1,5 m? die horen er volgens de ILS niet in | Any IfcSpace with a net height below 1.5 m? According to the ILS they should not be spaces. | bim_coordinator · validate_check · easy · needs file | Read space height from Qto_SpaceBaseQuantities or geometry; list spaces below 1.5 m with GUID, name and storey; note the source of the 1.5 m rule (BIM basis ILS, chapter on spaces) and that the height may be missing in some files. |
| NC4<br><sub>new</sub> | welke sparingen zitten er in de constructievloeren en welke leidingen uit het installatiemodel hebben nog geen sparing? | Which openings exist in the structural floors, and which MEP pipes still have no opening? | mep_engineer · coordinate_clash · hard · needs file | List IfcOpeningElement in slabs from the structural model; intersect MEP segments with the slabs; subtract matches within a tolerance; return a table of missing openings with size, storey and element GUIDs; say which tolerance was used. |
| NC5<br><sub>new</sub> | check de vrije ruimte bij de deuren en de verblijfsruimten volgens het Bbl, voor zover dat uit het model kan | Check clearance at doors and habitable rooms against the Bbl, as far as the model allows. | reviewer_authority · comply_regulation · hard · needs file | Be explicit that the Bbl (Dutch building regulations) rules cannot be fully checked from IFC and that IDS cannot express them; ask for or state the thresholds assumed; measure what is measurable (door clear width, space height, area) and list the rest as not checkable. |

### 4. Properties, quantities, comparison

| ID | Prompt (synthetic) | EN gloss | Persona · intent · difficulty | Expected behavior (what a good assistant does) |
|---|---|---|---|---|
| ND1<br><sub>nl-dutch-s005</sub> | welke wanden en vloeren missen LoadBearing of IsExternal in Pset_WallCommon? | Which walls/slabs lack LoadBearing and IsExternal | structural_engineer · validate_check · easy · needs file | Query Pset_WallCommon/Pset_SlabCommon; list missing; no edits. |
| ND2<br><sub>nl-dutch-s009</sub> | m2 binnenwand per NL-SfB code en aantal deuren met FireRating, naar excel kan? | m2 interior walls per NL-SfB code | estimator_qs · extract_quantities · medium · needs file | Aggregate NetSideArea by classification; door count; export table. |
| ND3<br><sub>new</sub> | hebben alle 212 deuren een FireRating? lijst van de deuren zonder, per bouwlaag | Do all 212 doors have a FireRating? List those without, per storey. | estimator_qs · validate_check · easy · needs file | Count IfcDoor (confirm the 212), check Pset_DoorCommon.FireRating on instance and type, list doors without a value grouped by storey with GUIDs; mention if the number found differs from 212. |
| ND4<br><sub>new</sub> | in mijn IFC2x3 export komt mijn eigen parameter brandwerendheid niet in Pset_WallCommon terecht. wat kan het zijn? | In my IFC2x3 export my own fire-resistance parameter does not reach Pset_WallCommon. What could be wrong? | architect · troubleshoot_export · medium | Explain the user-defined parameter mapping file (exact IFC names, tab-separated, type vs instance), name clashes with Revit's built-in Fire Rating, the known exporter issue where the mapping is not applied for IFC2x3; suggest checking the exported file text; do not claim a single cause. |
| ND5<br><sub>new</sub> | geef alle kozijnen zonder IsExternal, per bouwlaag, en zeg erbij hoeveel het er zijn | List all windows/frames without IsExternal, per storey, with the count. | bim_coordinator · validate_check · easy · needs file | Query IfcWindow (and IfcDoor if the user means frames in a wider sense; ask or state the choice) for Pset_WindowCommon.IsExternal; group missing values by storey; give totals and GUID lists. |
| ND6<br><sub>nl-dutch-s010</sub> | wat is er veranderd tussen v3 en v4 van het constructie ifc? nieuwe, verwijderde en gewijzigde elementen op GUID | Compare IFC v3 and v4 | bim_coordinator · compare_versions · medium · needs file | Diff by GlobalId, report added/removed/changed. |
| ND7<br><sub>nl-dutch-s014</sub> | zijn er dubbele objecten in dit aspectmodel? en wanden die elkaar doorsnijden | Duplicates/intersections | bim_coordinator · validate_check · hard · needs file | Detect duplicates by geometry/GUID, intersections; report. |

### 5. Requirements, tooling, FM

| ID | Prompt (synthetic) | EN gloss | Persona · intent · difficulty | Expected behavior (what a good assistant does) |
|---|---|---|---|---|
| NE1<br><sub>nl-dutch-s012</sub> | kun je een IDS maken van BIM basis ILS en daarmee dit model toetsen? | IDS from BIM basis ILS | bim_manager · how_to · hard | Draft IDS facets, run against model, report. |
| NE2<br><sub>new</sub> | pas toe of leg uit: welke IFC versie is dit bestand en moet dat 2x3 TC1 zijn voor de overheid? | Comply or explain: which IFC version is this file, and does government require 2x3 TC1? | owner_client · understand_concept · easy · needs file | Read FILE_SCHEMA (and view definition if present); explain that 'pas toe of leg uit' applies to public bodies buying ICT for 3D exchange, that the registered version is IFC 2x3 TC1, and that the client's ILS or contract decides the real requirement; do not say IFC4 is forbidden. |
| NE3<br><sub>new</sub> | wat is het verschil tussen een ILS en een IDS? en kan ik het ene in het andere omzetten? | What is the difference between an ILS and an IDS, and can I convert one into the other? | student_beginner · understand_concept · easy | Explain that ILS is a delivery agreement document (ISO 19650 sense) and IDS is a machine-readable buildingSMART file for automated checks; mention the English label 'BIM base IDS' for the Dutch ILS as a source of confusion and that the ILS Configurator can export an IDS file; do not claim full automatic conversion of every ILS rule. |
| NE4<br><sub>new</sub> | hoe stel ik Revit in zodat de IFC voldoet aan de BIM basis ILS? is er een handleiding voor mijn versie? | How do I configure Revit so the IFC meets the BIM basis ILS, and is there a manual for my version? | architect · how_to · medium | Point to the digiGO Revit manual and say its published version may lag current Revit; summarise the rules it must meet (entity plus TypeEnumeration, NL-SfB code per object, standard psets, IfcBuildingStorey only, origin near zero); ask for the Revit version; do not invent menu paths. |
| NE5<br><sub>new</sub> | geef per bouwlaag het BVO en GO uit de ruimten volgens NEN 2580, welke velden gebruik je? | Give gross floor area and usable area per storey from the spaces per NEN 2580; which fields do you use? | estimator_qs · extract_quantities · hard · needs file | Read IfcSpace area quantities and any area-type property; state which fields were used; warn that the NEN 2580 measurement rules are not applied automatically and that BVO normally needs the building outline, not only spaces; present per-storey sums with caveats. |
| NE6<br><sub>new</sub> | kleur alle wanden rood waar LoadBearing ontbreekt en groepeer de rest op brandwerendheid | Colour all walls red where LoadBearing is missing and group the rest by fire resistance. | bim_coordinator · validate_check · medium · needs file | Find walls without Pset_WallCommon.LoadBearing and group the others by FireRating with counts; if the server can set colours or create a selection set or view, do so; otherwise return the groups and offer the list of GUIDs; never claim a colour was applied if no tool can do it. |
| NE7<br><sub>new</sub> | welke objecten hebben tussen v3 en v4 een andere GlobalId gekregen? ik koppel mijn beheersysteem op GlobalId | Which objects got a different GlobalId between v3 and v4? My asset system links on GlobalId. | facility_manager · compare_versions · hard · needs file | Compare the two files by GlobalId; for objects missing in v4 try to match by name, type and position to find probable GUID changes; report added, removed and probably re-GUIDed objects separately; state the matching rule and its confidence. |

## Tips for generating authentic prompts in this language

**Do**
- Write lower-case, informal "je" lines without greeting: "welke wanden ...", "check of ...", "kun je ...".
- Use NL jargon: aspectmodel, nulpunt, bouwlaag, kozijn, sparing, NL-SfB, ILS, NAA.K.T., GO/BVO; keep IFC class names and tool names in English.
- Mention the rule source in one word ("volgens de ILS", "BIM basis ILS", "RD of lokaal?").
- Use concrete numbers like the real examples: "alle 212 deuren", "code 32.xx", "EPSG 28992", "1,5 m".
- Add a version label ("v3 en v4") instead of a file name; leave out the Revit version and IFC schema in most prompts.
- Let an occasional developer persona write a structured spec in Dutch (Waarom / Nu / Gevraagd) for validator-style requests.
- Include mild frustration where the data shows it: models that do not lie on the same origin, a tool that stays green when it should not.

**Don't**
- Do not use formal "u" or long polite introductions; the records show terse register.
- Do not confuse the Dutch **ILS** with buildingSMART **IDS**; a prompt that asks "maak een IDS van de ILS" is legitimate, one that treats them as the same thing is a trap.
- Do not state that a Dutch IFC "must" be IFC4 or 4.3; the registered version is 2x3 TC1 and the client's ILS decides.
- Do not assume Belgian users use the same codes (NL/BE-SfB equivalents are unverified) or the same storey names.
- Do not present these prompts as real quotes: no practitioner forum was reached.
