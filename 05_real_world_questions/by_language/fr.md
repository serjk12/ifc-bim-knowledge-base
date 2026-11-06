# French: how people ask about IFC, BIM and Revit

**Last researched: 2026-11-06** · France (main), French-speaking Belgium, Switzerland (Romandie), Quebec, francophone Africa. Language code `fr`.

## In plain words

IFC is the open file format that moves a BIM model between programs. In France it is called a *maquette numérique* (digital mock-up), and the surrounding rules usually come from a *convention BIM* or a *cahier des charges BIM* written by the client (*maître d'ouvrage*, MOA), not from a national law that fixes the IFC version. French-speaking users of an AI assistant connected to an IFC file will ask short work requests in lowercase: check a property against the convention, count proxies, get *métrés* for a *chiffrage*, compare *indice B* and *indice C*, prepare *DOE / GMAO* data.

## How much data is behind this page (read first)

| Fact | Value |
|---|---|
| French records in the KB | 45 (2 real, 43 synthetic) |
| Real French-language posts | **0**. Both real records are GitHub issues **written in English** by French-speaking reporters; their `lang` is `fr` because of the reporters' background. |
| Research cell | fr-francophone: the web-search budget was exhausted before the first search ran. No forum thread was found. Only KROQI and BIM&CO pages were read. See [fr-francophone report](../../research_raw/wave1/fr/fr-francophone.md). |
| Synthetic prompts | 43, written from general knowledge of French BIM vocabulary |

The requested 30-60 real examples **cannot be provided** from this corpus. This page therefore lists the 2 real records, plus 3 more English-language real posts by French-speaking authors found in other cells, and keeps the rest honest: everything about phrasing is a **hypothesis from synthetic prompts**, marked **(syn)**, or from general knowledge, marked **(GK)**. A second research pass is needed (Autodesk and Graphisoft French communities, cadxp, BIM-francophone groups, LinkedIn, YouTube, Reddit r/bim and French subreddits, Discord).

## Where people ask

| Place | Evidence | Notes |
|---|---|---|
| GitHub issues in international repos (Autodesk/revit-ifc, IfcOpenShell, ThatOpen/web-ifc) | **Seen**, in English | French-speaking reporters write English and keep French units and names ("15Mo", "Chaussée" with accent). |
| OSArch community (English) | **Seen**, one thread by a French-speaking facility manager | Clear two-part question about equipment identification for operation and maintenance. |
| Autodesk and Graphisoft community forums | **Not reached** (HTTP 403) | |
| cadxp.com | **Not reached**: the domain now redirects to a domain-for-sale page | A historic French CAD forum **(GK)**. |
| buildingSMART France / MediaConstruct | **Not reached**: mediaconstruct.fr returned 403, buildingsmart.fr is a parked page | National chapter per Wikipedia (see national doc). |
| KROQI knowledge base (CSTB) | Read, no IFC article found | Platform with IFC and BCF; user questions not available. |
| BIM&CO FAQ | Read, no IFC content | Object platform and Revit plugin. |
| Reddit, Discord, LinkedIn, YouTube | **Not reached** | Do not assume anything. |

## Top themes (ranked)

No measured ranking exists for real users. The order is the research agent's expectation from domain knowledge (flagged unverified in the report), checked against topic counts over the 45 French records: `quantities_qto` 6, `validation_checking` 5, `cobie_fm_handover` 4, `encoding_text` 3, `export_revit` 3, `spaces_rooms_areas` 3, `viewers_opening` 3, `conversion_formats` 3.

| # | Theme | Typical need | Related KB doc |
|---|---|---|---|
| 1 | Conformity to the *convention BIM* / *cahier des charges BIM* (required properties per class, level naming "RDC, R+1") | Controls with a list of gaps | [validation_ids_model_checking](../by_topic/validation_ids_model_checking.md) |
| 2 | Quantities / *métrés* for *chiffrage* and *DPGF* (net wall areas, concrete volumes per level, windows and doors counts by type) | Tables per level or per *lot* | [quantities_cost_schedule](../by_topic/quantities_cost_schedule.md) |
| 3 | Export problems from Revit/Archicad: shared parameters missing in Psets, proxies, class mapping table (*table de correspondance*) | Understand and fix | [revit_export_and_class_mapping](../by_topic/revit_export_and_class_mapping.md) |
| 4 | *DOE* / *GMAO* handover: equipment lists with manufacturer, reference, warranty; rooms with areas | Data for facility management | [materials_spaces_zones](../by_topic/materials_spaces_zones.md) |
| 5 | Georeferencing: RGF93 / Lambert-93 (EPSG:2154), model shifted by kilometres | Fix or check the CRS | [coordinates_georef_units_levels](../by_topic/coordinates_georef_units_levels.md) |
| 6 | *Synthèse* and clash detection, BCF; Navisworks no longer loading IFC2x3 | Coordination | [coordination_clash_bcf_cde](../by_topic/coordination_clash_bcf_cde.md) |
| 7 | Accents and special characters in IFC text (Revit writes "é" in two valid ways; IfcConvert fails on raw accents in the header) | Encoding fixes | [versions_mvd_encoding_guid](../by_topic/versions_mvd_encoding_guid.md) |
| 8 | Opening or viewing an IFC (empty viewer, 1.2 GB file out of memory, colours lost after IFC to OBJ) | Open and lighten | [file_size_viewing_conversion](../by_topic/file_size_viewing_conversion.md) |
| 9 | Version comparison between *indices* and GlobalId stability | What changed | [versions_mvd_encoding_guid](../by_topic/versions_mvd_encoding_guid.md) |
| 10 | Accessibility (PMR) and other regulatory checks | Measure doors and corridors | [regulations_permits_contracts](../by_topic/regulations_permits_contracts.md) |

## Local ecosystem

Full detail, with unverified flags: [france_francophone.md](../../02_standards_regulations/national/france_francophone.md).

**France**
- Policy: PTNB (2015) replaced by Plan BIM 2022 (2018, operated by AND Construction). Public buyers *may* require BIM tools under EU Directive 2014/24/EU. **No verified French law fixes an IFC version**; the requirement lives in each tender's *cahier des charges BIM* and the *convention BIM* signed by the project team.
- Standards: NF EN ISO 19650-1 and -2 (AFNOR), XP P07-150 (older vocabulary), ISO 16739-1 (IFC).
- Organisations: Mediaconstruct (buildingSMART France), CSTB with **KROQI** (collaborative BIM platform that uses IFC and BCF, data hosted in France), AFNOR.
- Terms: *maquette numérique*; official term *bâti immobilier modélisé* (Journal officiel, 29 Jan 2019); professional titles *BIM modeleur du bâtiment* and *Coordinateur BIM du bâtiment* (2019).
- Coordinates: Lambert-93 (EPSG:2154) and CC zones (EPSG:3942-3950) **(GK, flagged in the national doc)**.
- Software: Revit, Archicad, Allplan, Solibri, IfcOpenShell; BIMData, BIM&CO, Visiativ/Arkance resellers **(GK)**.

**Belgium (French-speaking part)**: buildingSMART Belgium; Brussels Airport Company open-BIM policy published 8 May 2026 (IFC is the contractual final deliverable; IFC version not stated). Regional rules unverified.

**Switzerland**: Bauen digital Schweiz / buildingSMART Switzerland (French pages exist); LOIN guides based on SN EN 17412-1; **eBKP-H** cost classification (verified in the national doc). SIA 2051 and KBOB: not verified.

**Quebec**: SQI documents in French (*Cahier des exigences BIM de projet*, *PEB* template, *Niveaux d'information requis*); government roadmap 2021-2026; the SQI calls BIM *modélisation des données des infrastructures (MDI)*. The SQI pages read do not name IFC.

**Africa (Morocco, Algeria, Senegal, Côte d'Ivoire)**: nothing verified.

## How people write

**There are no real French-language samples**, so this section describes synthetic prompts **(syn)** and general knowledge **(GK)**. The two real records give only one observable trait: French speakers writing English keep their own conventions ("15Mo", accented names).

### Register, length, structure

- **Very short, lowercase, no greeting (syn)**: "dis moi quels murs n'ont pas de résistance au feu renseignée dans la maquette, la convention BIM l'exige".
- **Imperative / informal verbs (syn)**: "sors moi", "donne moi", "liste", "vérifie", "compare", "renomme", "ajoute", "contrôle". Hyphens in "dis-moi / sors-moi / donne-moi" are often dropped.
- **Dropped negation "ne" (syn, and GK for spoken French)**: "j'arrive pas à ouvrir", "ça m'affiche rien", "mes paramètres partagés sortent pas".
- **Purpose clause (syn)**: "pour le chiffrage", "pour le DOE / GMAO", "avant la synthèse", "avant l'export de vendredi", "pour mon rendu de projet".
- **Decimal comma and French units (syn)**: "1,2 go", "couloirs < 1,40 m", "tolérance 2 cm", "débits ... en L/s".
- **Politeness exists (syn)**: "peux-tu vérifier...", "Quels réglages d'export IFC dans Archicad pour que Revit récupère correctement murs et dalles ?" with a capital letter and question mark. The more formal the persona (reviewer, architect asking a how-to), the more complete the sentence.
- **Tone**: mostly neutral; frustration when something broke after an update ("depuis la maj de l'export IFC revit, navisworks ne charge plus mon ifc2x3").

### Jargon and slang

| Term | Meaning | Standard / IFC term | Evidence |
|---|---|---|---|
| maquette (numérique) | the BIM model, native or IFC | model | syn, national doc |
| synthèse | multi-discipline coordination | coordination / clash review | syn |
| indice B / indice C | document revision letter | revision | syn |
| MOA, MOE | client, design team | appointing party | syn, GK |
| convention BIM, charte BIM, cahier des charges BIM | project BIM rules from the client (EIR/BEP equivalent) | EIR / BEP | syn, national doc |
| MediaConstruct | French buildingSMART chapter; "recos MediaConstruct" | national chapter | syn |
| DOE | as-built handover file | as-built / handover | syn, glossary |
| GMAO | maintenance management system | CMMS / FM | syn |
| SDP, surface utile | floor area (*surface de plancher*), usable area | area quantities | syn |
| lot, DPGF, chiffrage, métré | trade package, price schedule, costing, takeoff | Qto | syn |
| RDC, R+1, SS1 | ground floor, first floor, basement 1 | IfcBuildingStorey names | syn |
| niveau, étage | storey | IfcBuildingStorey | syn, glossary |
| pièce, local (locaux) | room | IfcSpace | syn |
| poteau, poutre, dalle, voile, cloison | column, beam, slab, structural wall, partition | IfcColumn, IfcBeam, IfcSlab, IfcWall | syn |
| mur-rideau, meneaux | curtain wall, mullions | IfcCurtainWall | syn |
| gaine, soufflage, reprise | duct, supply, return | IfcDuctSegment, systems | syn |
| trémie, réservation | opening in structure, sleeve/provision | IfcOpeningElement | syn |
| PMR | reduced-mobility accessibility | accessibility check | syn |
| table de correspondance | Revit IFC class mapping table | mapping table | syn, glossary |
| paramètres partagés, pset perso | Revit shared parameters, custom property set | shared parameter, Pset | syn |
| proxy | element exported as placeholder | IfcBuildingElementProxy | syn |
| visualiseur | viewer | viewer | syn |
| maj | mise à jour (update) | update | syn |
| go, Mo | gigabyte, megabyte (French spelling of units) | GB, MB | syn ("1,2 go"); real ("15Mo") |
| pb | problème | problem | syn |
| nomenclature | Revit schedule | schedule | glossary |

### Misspellings, name variants, code-switching

- Program names mixed case: "ArchiCAD" in prompts, "Revit 2022", "Navisworks", "Robot", "MagiCAD".
- Class names in English exactly: "IfcSpace", "IfcBuildingElementProxy", "IfcCurtainWall", "IfcTunnel".
- English terms inside French sentences: "clash", "pset", "export", "proxy", "viewer", "BCF", "GlobalId", "tolérance".
- Accents get dropped in fast typing (syn): "verifie", "metres" (for "métrés"), "memoire insuffisante", "fenetres".
- Unit spellings: "Mo", "go" (French) vs "MB", "GB".

### Encoding is a real French topic

Both real records concern accents. Revit's native exporter wrote `Chaussée` as `Chauss\X2\00E9\X0\` while add-in 22.4.1 wrote `\X\E9`; the reporter asked if the encoding changed (answer: the toolkit changed; both are valid). A French-speaking team found IfcConvert failing with `wstring_convert: to_bytes error` when the header `FILE_NAME` contained raw accented characters, while other viewers opened the file (answer: strict STEP strings must be ASCII; encode as `\X2\`). A French test set should include such cases.

### What context is given or omitted (syn)

Given: the program, sometimes the year ("Revit 2022"), the reason ("convention BIM", "DOE", "sous-traitant n'ouvre pas l'ifc4"). Omitted: exact convention text, IFC view definition, file name.

## Real questions

| ID | Original (title as posted) | English gloss | Persona | Evidence | Source |
|---|---|---|---|---|---|
| en-gh-encoding-r018 (also stored as en-err-r024) | "[IfcConvert] Convert string error" (written in English by a French-speaking team; cites buildingSMART string-encoding guidance) | IFC with special characters in the header `FILE_NAME` gives a conversion error when converting to XML; DAE works; BIMcollab and BIMvision open it. Answer: raw non-ASCII violates the STEP string rules; encode with `\X2\`; the tool may become lenient and warn. | bim_coordinator, 2020 | A (English), page | [IfcOpenShell #1016](https://github.com/IfcOpenShell/IfcOpenShell/issues/1016) |
| en-gh-encoding-r024 | "New codification for special character and accent?" (polite, French-influenced English) | Revit native wrote `Chauss\X2\00E9\X0\`, add-in 22.4.1 writes `\X\E9` for "é": has the encoding changed? Answer: toolkit changed (the ODA library uses a compact form); both valid. | bim_manager, 2022 | A (English), page | [revit-ifc #441](https://github.com/Autodesk/revit-ifc/issues/441) |
| en-gh-thatopen-r003 | "15Mo IFC file takes more than 5 minutes to load" (very short, French "Mo" for MB, file shared privately) | Parsing a 15 MB IFC takes more than 5 minutes; data is confidential so the file was sent privately. Later commits opened a 10 MB file quickly. | developer_programmer, 2023 | D, page | [web-ifc #527](https://github.com/ThatOpen/engine_web-ifc/issues/527) |
| en-osarch-gis-r014 | "Operation and maintenance on campus/site with ifc" (French-speaking poster, clear two-part question) | Does anyone know a similar project? Which IFC entity gives a unique code to each piece of equipment so plumbing, ventilation and electrical items can be identified in operation and maintenance? Answer: Dutch Rijksvastgoedbedrijf IFC standardisation; maybe a classification reference. | facility_manager, 2022 | D, page | [OSArch #1118](https://community.osarch.org/discussion/1118/operation-and-maintenance-on-campus-site-with-ifc) |
| en-ghrevitifc-r014 | "Mapping pset value from a parameter or another ? Mapping using built in parameter name ?" (markdown sections, French parameter names, e.g. "Largeur") | Wants to map two different Revit parameters to one Pset property depending on which exists (duct width and height for rectangular, diameter for round). No answer found. | mep_engineer, 2021 | D, page | [revit-ifc #303](https://github.com/Autodesk/revit-ifc/issues/303) |

Evidence level: **A (English)** = a person's own post, written in English by a French-speaking author; **D** = English post whose author is described by the research agent as French-speaking.

## Ready test prompts

All **synthetic**. Items 1-41 are rewritten or lightly edited from the research agents' prompts (Src = record id); 42-43 are **adapted** by the author of this page for Switzerland and Quebec from the national document, and the usage is **not observed** in the corpus. Variants: **FR** = France wording (default), **CH**, **QC**.

| # | Prompt (synthetic) | Var. | Intent, difficulty, persona | Src | Expected behavior |
|---|---|---|---|---|---|
| 1 | dis moi quels murs n'ont pas de résistance au feu renseignée dans la maquette, la convention BIM l'exige | FR | validate_check, medium, bim_coordinator, file | fr-francophone-s001 | Scan walls for the fire-rating property (standard or custom Pset); list GlobalId, name, level of the missing or empty ones. |
| 2 | j'ai plein de proxy dans mon IFC, c'est quoi comme catégories revit ? faut que je corrige la table de correspondance | FR | query_model_data, medium, bim_manager, file | fr-francophone-s002 | Count proxies, group by Revit category or ObjectType, suggest mapping fixes. |
| 3 | donne moi la surface par niveau des pièces (IfcSpace), SDP et surface utile si dispo | FR | query_model_data, easy, architect, file | fr-francophone-s003 | Sum net and gross floor area per storey; report spaces lacking values; do not equate IFC area with the legal *SDP* without saying so. |
| 4 | vérifie que les niveaux sont nommés comme dans la convention BIM (RDC, R+1...) et que les altitudes sont cohérentes | FR | validate_check, medium, bim_manager, file | fr-francophone-s004 | List storey names and elevations, compare with the naming pattern, flag mismatches and duplicates. |
| 5 | compare l'indice B et l'indice C de la maquette, je veux les éléments ajoutés/supprimés/modifiés avant la synthèse | FR | compare_versions, hard, bim_coordinator, file | fr-francophone-s005 | Diff by GlobalId; report added, removed, changed with property deltas, grouped by discipline. |
| 6 | ajoute le lot et le code Uniformat sur tous les poteaux, propriété dans un pset perso | FR | modify_model_data, medium, structural_engineer, file | fr-francophone-s006 | Create a custom Pset on all columns with the values; confirm counts first. |
| 7 | liste les gaines par système (soufflage, reprise...) avec longueur totale, si les systèmes sont bien exportés | FR | query_model_data, medium, mep_engineer, file | fr-francophone-s007 | Group duct segments by system, sum lengths from quantities; warn if systems are missing. |
| 8 | contrôle la maquette par rapport au cahier des charges BIM : propriétés obligatoires par classe, résume les écarts | FR | validate_check, hard, reviewer_authority, file | fr-francophone-s008 | Needs the requirements list; if absent, ask for it. Output pass/fail counts and non-conforming elements. |
| 9 | sors moi les volumes de béton par niveau pour le chiffrage, murs + dalles + poteaux | FR | extract_quantities, medium, contractor_site, file | fr-francophone-s009 | Sum net volume of walls, slabs, columns with concrete material per storey; flag elements without volume. |
| 10 | mon IFC est décalé de plusieurs km dans le viewer, regarde le géoréférencement RGF93 / Lambert 93 de la maquette | FR | query_model_data, hard, bim_coordinator, file | fr-francophone-s010 | Read map conversion and projected CRS, site placement; report CRS, offsets, suggest fixes. |
| 11 | fais moi la liste des équipements avec fabricant et référence pour le DOE / GMAO | FR | extract_quantities, medium, facility_manager, file | fr-francophone-s011 | Export equipment with manufacturer-type properties to a table; flag blanks. |
| 12 | renomme les matériaux selon la nomenclature de la convention, ex MAT_BETON_C25 | FR | modify_model_data, medium, architect, file | fr-francophone-s012 | Map existing names to the standard names, apply renames after confirmation, report unmapped. |
| 13 | pourquoi mes paramètres partagés sortent pas dans l'IFC ? j'ai coché pset personnalisé | FR | troubleshoot_export, medium, architect | fr-francophone-s013 | Explain the export setup (user-defined property sets file, "export Revit property sets", parameter groups); offer to inspect the model. |
| 14 | j'arrive pas a ouvrir le fichier ifc, ça m'affiche rien dans le visualiseur, c'est quoi le pb | FR | troubleshoot_viewing, easy, student_beginner | fr-francophone-s014 | Check that the file loads, entities and geometry exist, version; suggest other viewers. |
| 15 | comment je configure l'export IFC pour respecter les recos MediaConstruct / la charte BIM du MOA ? | FR | how_to, medium, bim_manager | fr-francophone-s015 | Describe mapping, property sets, view setup; do not claim specific MediaConstruct content that is not verified; offer to check an existing model. |
| 16 | un script ifcopenshell pour remplir une propriété sur tous les IfcDoor selon le nom du type ? | FR | how_to, medium, developer_programmer | fr-francophone-s016 | Show a loop over doors by type name that creates and edits a Pset; or run it on the loaded model. |
| 17 | fais un clash gaines vs structure, tolérance 2 cm, et sors les points en BCF | FR | coordinate_clash, hard, bim_coordinator, file | fr-francophone-s017 | Run duct vs structure with tolerance, group results, output BCF. |
| 18 | peux-tu verifier si toutes les portes ont bien la propriété FireRating et le bon niveau, avant l'export de vendredi | FR | validate_check, easy, bim_coordinator, file | fr-coord-s012 | Check doors for the property and storey assignment, list missing. |
| 19 | je dois sortir les métrés pour le DPGF : surfaces de murs nettes des ouvertures par niveau, et le nb de portes par type | FR | extract_quantities, medium, estimator_qs, file | fr-s012 | Net wall areas per storey, door counts by type, flag missing quantities. |
| 20 | combien de portes et fenetres par type? c'est pour le contrat de maintenance | FR | extract_quantities, easy, owner_client, file | en-fmor-s017 | Count doors and windows by type and storey; table. |
| 21 | vérifie que mon IFC a bien la hiérarchie site / bâtiment / niveaux, c'est pour mon rendu de projet | FR | validate_check, medium, student_beginner, file | p-student-s016 | Validate project, site, building, storey chain; list orphans and missing containers; explain simply. |
| 22 | depuis la maj de l'export IFC revit, navisworks ne charge plus mon ifc2x3, les clash tests sont vides | FR | troubleshoot_viewing, medium, bim_coordinator | fr-clash-s013 | Check exporter version, Navisworks IFC reader mode, IFC2x3 vs IFC4 settings. |
| 23 | comment je rattache mes éléments à un dictionnaire bSDD dans l'ifc ? | FR | how_to, easy, architect | fr-classbsdd-s014 | Explain classification references with a bSDD URI, tools to do it, how to check. |
| 24 | peux-tu ajouter le géoréférencement Lambert 93 (EPSG:2154) à la maquette, X 652000 Y 6862000 | FR | modify_model_data, medium, bim_coordinator, file | mul-coord-s014 | Create the projected CRS and map conversion with the given values; confirm before writing. |
| 25 | donne moi les surfaces de murs par pièce, dans un tableau, avec les murs sans pièce à part | FR | extract_quantities, hard, estimator_qs, file | fr-data-s013 | Associate walls with spaces (boundaries or containment), sum per space, list orphan walls separately; say how association was done. |
| 26 | IfcConvert plante avec 'to_bytes error', y'a des accents dans le header, tu peux corriger le fichier ? | FR | convert_format, medium, developer_programmer, file | fr-err-s010 | Read the header, escape non-ASCII as `\X2\`, rewrite, verify conversion. Based on real IfcOpenShell issue #1016. |
| 27 | mon ifc de 1,2 go plante dans le navigateur, memoire insuffisante, comment on fait pour l'afficher quand meme ? | FR | troubleshoot_viewing, easy, bim_manager | fr-fs-s012 | Explain streaming viewers, converting to fragments or glTF, splitting by discipline or level, desktop viewers. |
| 28 | le mur-rideau est bizarre dans l'IFC, les meneaux manquent. tu peux verifier les IfcCurtainWall et leurs composants ? | FR | troubleshoot_export, medium, architect, file | fr-geom-s012 | Inspect curtain-wall decomposition, count members and plates, report missing parts. |
| 29 | verifie que tous les GlobalId sont valides (22 caracteres base64) et qu'il n'y a pas de doublons dans la maquette | FR | validate_check, easy, bim_manager, file | fr-guid-s011 | Validate length and alphabet of each id (first character 0-3), report invalid and duplicates. |
| 30 | dans ce modele de tunnel IFC 4.3, liste les IfcTunnel et leurs parties avec la longueur | FR | query_model_data, medium, civil_infra_engineer, file | fr-infra-s013 | List tunnel and tunnel-part entities, lengths if present; say what is missing. |
| 31 | compare les couleurs entre mon export IFC2x3 et l'IFC4, y a des elements gris en IFC4 | FR | compare_versions, hard, architect, file | mx-mcl-s007 | Resolve the effective colour per element in both files, match by GlobalId, list elements grey only in IFC4. |
| 32 | verifie les unites des debits sur les gaines, j'ai l'impression que c'est en ft3/s au lieu de L/s | FR | validate_check, medium, mep_engineer, file | fr-mep-s011 | Inspect unit assignment and flow property units, report mismatches, convert values. |
| 33 | vérifie les réservations MEP par rapport aux trémies dans les voiles, lesquelles ne correspondent pas ? | FR | validate_check, hard, bim_coordinator, file | fr-openings-s016 | Match reservation elements with openings in walls; list mismatches. |
| 34 | vérifie l'accessibilité PMR : portes < 90 cm et couloirs < 1,40 m dans la maquette, liste avec niveau | FR | comply_regulation, hard, reviewer_authority, file | fr-permit-s014 | Measure doors and corridor spaces, list those under the thresholds with storey; do not state legal compliance. |
| 35 | vérifie qu'aucun IfcBuildingElementProxy n'a un nom qui contient 'Mur' ou 'Cloison', sinon liste-les | FR | validate_check, easy, bim_coordinator, file | fr-proxy-s007 | Filter proxies by name patterns, list GlobalId and name, flag likely misclassification. |
| 36 | j'ai besoin d'un métré par lot : maçonnerie en m3, cloisons en m2, menuiseries en nombre | FR | extract_quantities, medium, estimator_qs, file | fr-qto-s016 | Map classes to trade packages, compute volumes, areas and counts with units and sources. |
| 37 | Quels réglages d'export IFC dans Archicad pour que Revit récupère correctement murs et dalles ? | FR | how_to, medium, architect | fr-roundtrip-s013 | Explain translator, view definition, element classification and geometry options. |
| 38 | y a-t-il des IfcSpace pas rattachés à un niveau ? liste-les | FR | query_model_data, easy, architect, file | fr-spaces-s015 | List spaces without a storey container. |
| 39 | liste moi les poteaux et poutres avec section et matériau, je veux les mettre dans Robot | FR | query_model_data, easy, structural_engineer, file | fr-struct-s014 | Enumerate columns and beams with profile and material in a table. |
| 40 | peux tu me sortir une version ifc2x3 de ce modele, le sous-traitant n'ouvre pas l'ifc4 | FR | convert_format, medium, bim_coordinator, file | fr-vm-s011 | Export or convert to IFC2x3, warn about lost features, verify the schema of the result. |
| 41 | mon obj exporté depuis l'ifc n'a plus aucune couleur, pourquoi ? | FR | troubleshoot_viewing, medium, architect, file | fr-viewconv-s010 | Explain styles vs OBJ material files, check that colours exist in the IFC, advise re-export. |
| 42 | regarde si tous les éléments ont un code eBKP-H dans l'ifc, et donne-moi ceux qui n'en ont pas | CH | validate_check, medium, bim_manager, file | adapted; eBKP-H from national doc | List elements without a classification reference, name the system actually found; do not assume eBKP-H is present. Usage not observed. |
| 43 | contrôle la maquette avec notre grille de niveaux d'information requis, voici le tableau, et dis-moi les écarts par discipline | QC | validate_check, hard, reviewer_authority, file | adapted; SQI documents from national doc | Needs the table; report gaps per discipline. Usage not observed; "niveaux d'information requis" is a title in the SQI toolkit. |

## Tips for generating authentic French prompts

**Do**
- Use the project vocabulary: *maquette, synthèse, indice B, convention BIM, MOA, DOE, GMAO, DPGF, lot, RDC / R+1, trémie, réservation, voile, PMR*.
- Keep it short, lowercase, no greeting; drop the hyphen in "dis moi / sors moi / donne moi"; occasionally drop "ne" ("j'arrive pas").
- Add the purpose or deadline: "avant la synthèse", "pour le chiffrage", "avant l'export de vendredi".
- Keep class names, "clash", "pset", "proxy", "viewer", "BCF" in English inside French sentences.
- Use French number and unit formats: "1,2 go", "1,40 m", "L/s", "Mo".
- Include accent and encoding situations: they are the only well-documented real French issue in the corpus.
- Vary the register: a reviewer or architect writing a how-to uses a full, polite sentence; a coordinator hitting an export bug writes a clipped complaint.

**Don't**
- Don't use English-looking terms where French users say something else (say *maquette* more than "modèle BIM", *métré* more than "quantity takeoff").
- Don't claim a French national rule for IFC version, Psets or classification: none is verified; the convention of the project decides. Expected behavior should say "check the convention".
- Don't invent MediaConstruct, KROQI or Plan BIM details. The doc marks them unverified.
- Don't present these prompts as quotes: the corpus has no real French-language post.
- Don't write like a translated textbook ("Pourriez-vous m'indiquer...").
- Don't assume Belgian, Swiss or Quebec phrasing is identical; the corpus has no data for it. If you add Quebec wording, remember the SQI term *MDI*, and for Switzerland remember *eBKP-H*, but mark such prompts as hypotheses.

## Gaps and next steps

- A research pass with working search is needed for real French posts (Autodesk and Graphisoft French communities, cadxp archive, LinkedIn, YouTube comments, Reddit, Discord, MediaConstruct and BIM-francophone resources).
- The French national doc flags MediaConstruct, Plan BIM 2022 successors, and Lambert-93 rules as not verified.

## Related KB documents

- [France and francophone countries: BIM/IFC requirements](../../02_standards_regulations/national/france_francophone.md)
- [Revit IFC export reference](../../03_software/revit/ifc_export_reference.md), [Multilingual glossary](../../08_glossary/glossary_multilingual.md) (French column with Revit French menu names)
- [IFC basics: coordinates and units](../../01_ifc_basics/06_geometry_placement_coordinates_units.md)
- Other languages: [es](es.md), [pt](pt.md), [it](it.md)
