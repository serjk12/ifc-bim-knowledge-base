# Netherlands, Belgium, Luxembourg: BIM/IFC requirements

## In plain words

The three Benelux countries do not have one single legal "BIM mandate" like the UK Level 2 programme. Instead, each has a mix of public-client policies, national "information delivery specifications" and open-standards rules. The Netherlands is the most formalised: IFC is on the government "pas toe of leg uit" (comply or explain) list, and the sector-wide **BIM basis ILS** (a minimum set of IFC modelling and delivery agreements) is maintained by the **digiGO** organisation, which absorbed the old **BIM Loket** in 2023 [1][2][5]. Belgium is regionally fragmented and driven by large clients and communities (for example Brussels Airport's 2026 "IFC-first" policy) plus buildingSMART Belgium and Buildwise [11][12]. Luxembourg is small and coordinated by the resource centre **CRTI-B**, which runs the national BIM working groups and promotes IDS-based exchange requirements ("BIMids") [13][14]. For a QA tester: expect IFC files with Dutch NL-SfB codes, `IfcBuildingStorey` naming rules, Dutch coordinates (RD/NAP) and IDS files as the new way to state requirements.

Last researched: 2026-11-06. QA pass 2026-11-06: the Forum Standaardisatie IFC entry, the digiGO BIM basis ILS downloads page and the digiGO NL-SfB page were re-fetched and confirm the IFC 2x3 TC1 listing (registered 26-05-2011, decided 15-11-2011), the 1 April 2026 NL-SfB ownership transfer and the ILS v1.0/v2.0 files; one date caveat added. See `_meta/qa/qa-standards-2.md`.

**Research note.** The web search tool hit its call budget during this run, so only direct page fetches of primary sources were possible. Items I could not confirm from a fetched page are marked "(unverified)". No real forum threads were found; all questions below are "(illustrative)".

---

## 1. Netherlands

### 1.1 Who is who

| Body | Role | Notes |
|---|---|---|
| **digiGO** ("Digitaal samenwerken in de Gebouwde Omgeving") | Maintains open standards and ILS documents: BIM basis ILS, ILS Ontwerp & Engineering, NL-SfB (until 2026), VISI, NLCS, ILS Configurator | Director named on site; partners include Ministry of BZK, Rijkswaterstaat, Rijksvastgoedbedrijf, ProRail, municipalities Amsterdam and Rotterdam, Bouwend Nederland, BNA, NLingenieurs, Aedes, Techniek Nederland [1] |
| **BIM Loket** | Founded 2015, officially merged into digiGO in 2023; old overview of ICT standards still at bimloket.nl/ictstandaarden [2][3] | bimloket.nl root redirects to digigo.nu |
| **Forum Standaardisatie** | Government advisory body keeping the "open standards" lists, including "pas toe of leg uit" [4] | |
| **buildingSMART Benelux / Stichting buildingSMART Nederland** | National chapter; domains (Airport, Construction, Railway, Regulatory, Building, Infrastructure, Product, Technical), programmes and projects [6][7] | works with Buildwise (BE) and CRTI-B (LU) |
| **Ketenstandaard Bouw en Techniek** | Took over ownership of NL-SfB on 1 April 2026 [5][8] | |
| **Geonovum** | Government geo-standards body; produced the georeferencing practice guideline, now maintained by digiGO [9][10] | |
| **Rijksvastgoedbedrijf (RVB / Rgd)** | Government real-estate client; has its own "RVB BIM Norm" [15] | |
| **Rijkswaterstaat, ProRail** | Infrastructure clients (own requirements; details unverified, see Gaps) | |

### 1.2 Open-standards policy: IFC on "pas toe of leg uit"

* IFC is on the Forum Standaardisatie list **"Verplicht (pas toe of leg uit)"**. Listed version: **IFC 2x3 TC1**; management organisation: buildingSMART; registration date 26-05-2011, decision date 15-11-2011 [4].
* Functional scope: IFC as file format for communicating and coordinating building information models. Organisational scope: Dutch government bodies (state, provinces, municipalities, water boards) and (semi-)public institutions, **when investing in ICT systems that exchange 3D building models** [4].
* The listing's "Uitstekend beheer" field is "Nee", meaning a newer IFC version must first be reviewed by Forum Standaardisatie before it can replace 2x3 TC1 on the list (re-read in QA) [4]. The expert review noted IFC is aimed primarily at buildings; civil works (viaducts, dredging) are outside its primary domain. A 2021 evaluation advised aligning IFC with NLCS, BGT and IMBOR, speeding vendor uptake of the new version, and using the IFC "coordination view" where possible [4].
* "Comply or explain" means a public body must use the standard or document why not. It is not a criminal or tender-law ban on other formats.
* BCF was not shown on the "pas toe of leg uit" list in the fetched page [4]. The BIM Loket overview lists IFC (as ISO 16739 under NEN), BCF and IDS as buildingSMART International standards [3]. Whether BCF/IDS are on the broader "lijst met open standaarden" is unverified.
* The registered version (2x3 TC1) lags the practice: modern ILS work and the buildingSMART Dutch project "Dutch translation of IFC 4.3.0.0" show the sector moving to IFC4/IFC4.3 [7]. Which IFC version a given government project requires is set by the individual client or ILS (unverified).

### 1.3 BIM basis ILS (the central document)

* **What**: "BIM basis informatieleveringsspecificatie" (ILS = information delivery specification, in the ISO 19650 sense), a minimal set of agreements for exchanging IFC models in building projects [1][16].
* **Versions**: PDFs for v1.0 (Nov 2023) and v2.0 (Sept 2024, in many languages including English "BIM base IDS"; German version is called "ILH") [17]. QA caveat: the downloads page gives no explicit release dates; "Nov 2023" and "Sept 2024" are the upload-folder months in the file links (2023/11 for all v1.0 files; 2024/09 for the first v2.0 files, with later languages added up to 2026/03), so treat them as approximate publication months. Note the translation "IDS" in English file names means *ILS*, not buildingSMART IDS. Do not confuse them.
* **Governance**: volunteer-run Beheerorganisatie with Beheercommissie, Expertcommissie, Toepassingscommissie and Klankbordgroep; related to digiGO and buildingSMART Benelux; questions to basis-ils@digigo.nu [18]. Organisations can sign up as "partners" [16].
* **Rules confirmed from the web page** [16]:
  * Objects carry a **four-digit NL-SfB code** (latest published version).
  * Use the **PropertySets prescribed by buildingSMART** in the international standard where possible (i.e. standard `Pset_*Common`, not custom ones).
  * Building storeys are modelled **only as `IfcBuildingStorey`**, with consistent storey names.
  * Consistent file names for aspect models ("deelmodellen"), consistent `Name` and `Type` of objects.
  * Place each aspect model's local origin **close to the origin** (no huge coordinates).
  * Agree up front who delivers which information and when.
* **Not confirmed** (page does not say): exact IFC schema version, MVD, BIM-checker, georeferencing rules. Treat any claim like "BIM basis ILS requires IFC4 Reference View" as (unverified).
* **Software manuals** ("handleidingen") list how to meet the ILS from native tools: Revit (v2.01, Oct 2020; older v1.01 Feb 2020), Archicad (v2.01, Oct 2020), Tekla Structures (v3.1, May 2023), Allplan (v1.0, Jan 2017), Adomi, BricsCAD, DDS-CAD, HiCAD, SketchUp, Vectorworks (v2.1, June 2023) [19].
* **Related ILS and tools** on digiGO: ILS Ontwerp & Engineering (described together with NL-SfB and IFC), BIM basis Infra, Basis ILS Puntenwolk, ILS Bestaande Bouw, ILS-woco, MiniBIM, MiniGIM, Model Informatieprotocol, Model BUP, BCF-kaart, NAA.K.T., Basis USO, Workflow sparingscoordinatie, 3D GeoBIM, Praktijkrichtlijn geopositionering, ILS Configurator [20]. The BIM Loket overview additionally names ILS Constructieve betonvloeren/-wanden, ILS Provincies, ILS Staalconstructie, ILS houten kozijnen, ILS kalkzandsteenwanden [3].
* **ILS Configurator** (ilsconfigurator.nl): online tool to create, assess and approve a project-specific ILS, drawing on NL-SfB, IFC, ILS O&E, Aedes ILS, ILS VMRG, ILS NBvT. It can now **export an IDS file** [21]. This is the main Dutch bridge from "ILS" to buildingSMART IDS.
* **NAA.K.T.** (NAAm_Kenmerk_Toepassing): material-naming convention (name, characteristic, application) with an IDS file (IDS_NAAKT-v2.5) and a bSDD entry (version 2.5) [22].

### 1.4 NL-SfB classification

* "The most used classification for building parts" in NL; used to code layers and objects in BIM/CAD [8].
* Ownership moved to **Ketenstandaard Bouw en Techniek on 1 April 2026**; Ketenstandaard announced a **revised NL-SfB version on 04/05/2026** [8][23]. The page calls it multilingual and cross-border; the precise relation to the Belgian "NL/BE-SfB" scheme and the code format of the new version are unverified.
* In BIM basis ILS the **four-digit table-1 code** goes on each object (typical examples from practice, unverified for the new version: 21 = exterior walls, 23 = floors, 28 = roofs, 31 = windows/doors in the exterior; check the current table).
* In IFC the code is normally stored as `IfcClassificationReference` (Identification = code, ReferencedSource = `IfcClassification` named "NL-SfB") or, in many Revit setups, as a text parameter mapped into a property set. Which of the two a project expects is defined by its ILS/IDS (unverified for BIM basis ILS).

### 1.5 Georeferencing

* **Praktijkrichtlijn Geopositionering** (Geonovum working group; online version **0.8**; pamphlet file dated 09-12-2025). The Geonovum repository is archived; maintenance moved to digiGO (github.com/nl-digigo/GeoBIM_Georefereren) [9][10].
* Content per file listing: CRS and projection chapter, georeferencing methods, data exchange, domains, software manuals, practical test, appendices with **IFC, WKT, PROJ, GML, CityJSON, API, Python examples** [10].
* buildingSMART NL project "Georefereren IFC": practical guideline so BIM and geo data align in common software [7].
* Dutch background (general knowledge, unverified in this run): national CRS is **Rijksdriehoekstelsel (RD), EPSG:28992**, heights relative to **NAP (EPSG:5709)**, compound often **EPSG:7415**. In IFC4 this is expressed with `IfcMapConversion` + `IfcProjectedCRS`; IFC2x3 has no such entities, so tools use a property-set workaround.

### 1.6 Public clients

* **Rgd/RVB BIM Norm**: the page I could read names **RVB BIM Norm (RBN) 1.1**, **RVB BIM Specification (RBS) 1.1-c** (content equal to RBN 1.1 without CAD specs) and **RCS 1.0** (CAD specification for 2D drawings). RBS applies to 3D models, RCS to 2D; contractors must deliver in RBS **only when the contract explicitly prescribes it**; any BIM-based drawing must come with its source model. IFC is **not mentioned** on that page. An English translation of "RVB BIM Standard v1.0.1" (2014) exists [15]. So "Rgd BIM Norm" is a real name (as "RVB BIM Norm"), but it is older than BIM basis ILS and not IFC-centric.
* **Rijkswaterstaat** and **ProRail**: partners of digiGO [1]; their specific BIM requirement documents could not be fetched (404 on guessed URLs). Do not quote versions, years or thresholds for them (unverified). Infrastructure IFC work is tracked in buildingSMART NL's "IFC Infra" project on IFC 4.3 [7].
* **Thresholds / mandate date**: I found no national legal threshold (budget, floor area) or start year for a general Dutch BIM mandate (unverified; likely none exists). The mandatory element is the "pas toe of leg uit" IFC listing (2011) [4] plus client-specific contract clauses.

### 1.7 Other NL facts
* **Information protocol / Model BUP / Model Informatieprotocol** are contractual templates on digiGO [20].
* **ISO 19650 templates**: buildingSMART project combining NL and BE knowledge to produce one uniform set [7].
* **IFC 4.3 Dutch translation** (phase 2, to be available through bSDD) [7].
* **Certification**: buildingSMART Professional Certification for Benelux practitioners, plus a "Practitioner Course" project [6][7].
* **Events**: DigiBouw 2026 on 25-26 November 2026 [6]; digiGO Standaardendag 2026 and DigiDare Award 2026 [1].

---

## 2. Belgium

Belgium has no national BIM mandate I could verify; construction policy is regional (Flanders, Wallonia, Brussels) plus the federal Regie der Gebouwen. Statements below about regional programmes are limited to what I fetched.

* **buildingSMART Belgium** (buildingsmart.be): community of "openBIM enthusiasts"; site since 2012; team members from Qonic, Arcade Groep, Brussels Airport Company, Buildwise and Bimplan|Bimproof; events include IDS Escape Game, Bonsai for Blender sessions, an OpenBIM Gebruikersdag in Amsterdam, Digital Construction Day [11][12][24].
* **Brussels Airport Company (BAC) "BAC BIM Open Standards Policy"** (published 8 May 2026 by buildingSMART Belgium): IFC is the contractual final deliverable on all projects; all quality checks are done **exclusively on IFC**; suppliers may use their own native tools; IFC is the required archive format; native as-built files must still be delivered alongside IFC for model maintenance; BAC's internal team maintains Revit and Civil 3D models. IFC schema version not stated [11]. A PDF of the policy is listed on the downloads page [24].
* **Buildwise** (Belgian construction research centre, formerly WTCB/CSTC): partner of buildingSMART Benelux and CRTI-B [6][13]. Its BIM pages could not be fetched (404). The "BIM Charter" and "BIM protocol" often cited in Belgian practice are (unverified) products of Buildwise/regional partners; check buildwise.be directly.
* **Classification**: NL-SfB is described as cross-border [23]. Belgian equivalents (NL/BE-SfB, "Cel-codes", Flemish "CCTB" in specifications) are (unverified).
* **Flanders** (Digitaal Vlaanderen page fetched: no BIM content) and **Federal Regie der Gebouwen** (URL 404): no verified requirements. (unverified) Do not assert specific Flemish or federal BIM decree names or dates.
* Language note: Belgian documents appear in Dutch (NL), French (FR) and English. A Belgian test model may have French storey names ("rez-de-chaussée") and Dutch ("gelijkvloers").

---

## 3. Luxembourg

* **CRTI-B** (Centre de Ressources des Technologies et de l'Innovation pour le Bâtiment, Luxembourg-Kirchberg): coordinates the national BIM working groups since the first national BIM-strategy steps in **2015**; cross-sector working group with sub-groups (owners, architects, consultants, contractors, craftspeople, researchers, project managers) [13][14].
* Members listed: Ministère de la mobilité et des travaux publics, Chambre des métiers, OAI, Fédération des artisans, Groupement des entrepreneurs. Associated partners: **buildingSMART, Buildwise, bimids.eu** [14].
* Resources listed under "Digitalisation": Guide d'application, BIMIDS.EU, Guide de formation, SMARTBuilding, Formations BIM, Actualités BIM [14]. The individual page URLs could not be confirmed (guessed URL gave 404).
* **BIMids** ("Exchange requirements in a BIM process", bimids.eu/lu-fr): the page text I could read held only the title. It is evidently a service for stating exchange requirements (IDS). Details such as publisher, versions and IFC version are (unverified) [25].
* Public procurement page of CRTI-B: crtib.lu/fr/mpu [26]; whether it states a BIM clause is (unverified).
* The "CRTI-B" name appears in buildingSMART Benelux materials as the Luxembourg sister organisation [6].
* Languages: FR, DE, LU; documents mostly FR.

---

## 4. IFC-specific expectations (what QA should assume)

| Topic | NL | BE | LU |
|---|---|---|---|
| Registered IFC version | IFC 2x3 TC1 on pas toe of leg uit [4] | Not stated (BAC: IFC-first) [11] | Not verified |
| Newer schema work | IFC4 / 4.3 projects, Dutch IFC 4.3 translation [7] | n/a | n/a |
| MVD | "Coordination view" advised [4]; exact MVD of ILS (unverified) | n/a | n/a |
| Property sets | buildingSMART standard `Pset_*` preferred [16] | n/a | n/a |
| Classification | 4-digit NL-SfB [16] | NL/BE-SfB (unverified) | Not verified |
| Storeys | only `IfcBuildingStorey` [16] | | |
| Origin | local origin near 0; georeferencing via Geonovum/digiGO guideline [9][16] | | |
| Naming | consistent file, storey, Name, Type; NAA.K.T. for materials [16][22] | | |
| Requirement language | ILS / IDS export [21] | IFC-first policy at BAC [11] | BIMids [14][25] |
| Checking | Solibri-type rule checks and IDS checks (unverified for official portals) | all checks on IFC at BAC [11] | |

Submission portals: no national IFC upload portal for permits was verified in this research. (Dutch building permits go through Omgevingsloket under the Omgevingswet; whether it accepts IFC/BIM is unverified.)

---

## 5. Local software and community (labelled as community knowledge, mostly unverified)

* Native tools covered by the BIM basis ILS manuals: Revit, Archicad, Tekla, Allplan, Vectorworks, SketchUp, BricsCAD, DDS-CAD, HiCAD, Adomi [19].
* **ILS Configurator** (ilsconfigurator.nl) [21].
* **Bonsai (ex-BlenderBIM)** open-source IFC authoring in Blender is actively demonstrated by buildingSMART Belgium sessions [11].
* Belgian software/consultancy names appearing on buildingSMART Belgium's team page: Qonic, Bimplan|Bimproof, Arcade Groep [24].
* Well-known from general knowledge (not verified here): BIMcollab (Dutch, KUBUS) for BCF issues; BIMserver open-source IFC server originating in the Netherlands; Solibri used widely for rule checking; IfcOpenShell developed with strong Dutch contributors.

---

## 6. Local terminology

| Native term | Transliteration / language | English |
|---|---|---|
| pas toe of leg uit | NL | comply or explain |
| verplicht | NL | mandatory |
| informatieleveringsspecificatie (ILS) | NL | information delivery specification |
| BIM-uitvoeringsplan (BUP) | NL | BIM execution plan |
| informatieprotocol | NL | information protocol (contract annex) |
| deelmodel / aspectmodel | NL | aspect (discipline) model |
| bouwlaag | NL | building storey |
| sparing | NL | opening / penetration |
| sparingscoördinatie | NL | opening coordination |
| materiaalbenaming | NL | material naming |
| Rijksdriehoekstelsel (RD) | NL | Dutch national grid (EPSG:28992) |
| Normaal Amsterdams Peil (NAP) | NL | Dutch height datum |
| opdrachtgever / opdrachtnemer | NL | client / contractor |
| Omgevingsloket | NL | environment permit portal |
| gelijkvloers | BE-NL | ground floor |
| rez-de-chaussée | FR | ground floor |
| maquette numérique / modélisation des données du bâtiment | FR | BIM model |
| cahier des charges BIM | FR | BIM brief/specification |
| Guide d'application | FR | application guide (CRTI-B) |
| marchés publics | FR | public procurement |
| centre de ressources | FR | resource centre |
| Beheerorganisatie | NL | management organisation |
| handleiding | NL | manual |

---

## Typical questions people ask about this

None of these were found as real threads in this run; all are illustrative.

1. Is IFC mandatory for Dutch government projects, and in which version? (illustrative) See [4]: "pas toe of leg uit", listed as 2x3 TC1.
2. What is the difference between BIM Loket and digiGO? (illustrative) See [2].
3. Which IFC version does BIM basis ILS 2.0 require? (illustrative; answer unverified) Check [17].
4. How do I export a Revit model that meets the BIM basis ILS? (illustrative) See the Revit manual v2.01 [19].
5. Where do I put the NL-SfB code in the IFC file? (illustrative) See section 1.4.
6. Why is my model so far from the origin after IFC export? (illustrative) Rule: keep local origin near zero [16]; use the georeferencing guideline [9][10].
7. What coordinate reference system should a Dutch IFC use? (illustrative) See section 1.5 (RD/NAP, unverified in this run).
8. Is `IfcMapConversion` supported when exporting IFC2x3? (illustrative) No, IFC4 only (general knowledge).
9. How do I convert my ILS into an IDS file? (illustrative) Use the ILS Configurator export [21].
10. Is the RVB BIM Norm still valid, and is it IFC-based? (illustrative) See [15].
11. Does Rijkswaterstaat have its own IFC requirement? (illustrative, unverified; see Gaps)
12. What does "IFC-first" mean for a Belgian airport contract? (illustrative) See [11].
13. Does Belgium have a national BIM mandate? (illustrative) None verified; see section 2.
14. What is BIMids in Luxembourg? (illustrative) See [25]; details unverified.
15. How is NL-SfB changing in 2026 and who owns it? (illustrative) See [8][23].
16. Which tools can run an IDS check on a Dutch model? (illustrative) Not verified here; check buildingSMART tool listings.
17. Can an MCP tool that edits IFC keep `IfcBuildingStorey` names consistent with the ILS? (illustrative) QA test idea based on [16].
18. What is NAA.K.T. and where is the IDS file? (illustrative) See [22].
19. How do I get buildingSMART certification in Benelux? (illustrative) See [6][7].
20. Which IFC entity should carry French storey names in Luxembourg? (illustrative) `IfcBuildingStorey.Name`; language convention unverified.

## Common pitfalls and misconceptions

* **"BIM Loket" no longer exists as an organisation.** It merged into digiGO in 2023; bimloket.nl redirects there [2].
* **"ILS" vs buildingSMART "IDS".** English translations of BIM basis ILS use the label "BIM base IDS", which is a different thing from the buildingSMART IDS file standard [17][21].
* **IFC "mandatory" is conditional.** It applies to public bodies when buying ICT for 3D model exchange, under comply-or-explain [4].
* **Listed version is IFC 2x3 TC1**, even though modern projects use IFC4/4.3 [4][7].
* **Rgd BIM Norm is not the same as BIM basis ILS.** It dates from the RVB BIM Standard (2014 English translation), applies only if the contract prescribes it, and the page does not mention IFC [15].
* **Version-file naming glitches.** On digiGO the Dutch "versie 2 tegels" zips are named `v1_0`, and the Estonian v1.0 file is named `_POL`; German is "ILH" [17].
* **NL-SfB ownership changed** on 1 April 2026 [8].
* **Georeferencing guideline is still v0.8** (draft-level) [9].
* **Assuming a Belgian or Luxembourg mandate** exists because the Netherlands has comply-or-explain.

## Gaps (what could not be verified)

* Search tool budget was exhausted; only direct fetches succeeded.
* Rijkswaterstaat and ProRail BIM requirement documents, thresholds and start dates: not retrieved (guessed URLs 404).
* Rgd BIM Norm current status (newer than RBN 1.1?): unknown.
* BIM basis ILS IFC schema/MVD, BIM-checker, georeferencing clauses: not stated on the web pages; the PDFs could not be machine-read (compressed streams). I did not download or run anything; one PDF was cached by the fetch tool automatically.
* Belgian regional and federal mandates (Flanders, Wallonia, Brussels, Regie der Gebouwen), Buildwise BIM Charter/protocol, Belgian classification: not retrieved.
* Luxembourg Guide d'application, public-sector requirements, BIMids content: page URLs unconfirmed.
* IDS official standard status and buildingSMART technical pages: 403 Forbidden.
* No real practitioner forum questions found; no suspicious or pirated sites were encountered.

## Sources

[1] https://www.digigo.nu/ (digiGO home, programmes, partners)
[2] https://www.digigo.nu/welkom-in-ons-clubhuis/ (BIM Loket founded 2015, merged into digiGO 2023)
[3] https://www.bimloket.nl/ictstandaarden/ (overview of ICT standards)
[4] https://www.forumstandaardisatie.nl/open-standaarden/lijst/verplicht and https://www.forumstandaardisatie.nl/open-standaarden/ifc
[5] https://www.digigo.nu/ilsen-en-richtlijnen/
[6] https://www.buildingsmart.nl/
[7] https://www.buildingsmart.nl/projecten
[8] https://www.digigo.nu/standaarden/nlsfb/
[9] https://www.digigo.nu/ilsen-en-richtlijnen/tools-voor-informatiemanagement/praktijkrichtlijn-geopositionering/
[10] https://github.com/Geonovum/GeoBIM_Georefereren (archived; successor github.com/nl-digigo/GeoBIM_Georefereren)
[11] https://buildingsmart.be/brussels-airport-sets-new-standard-with-ifc-first-bim-policy/
[12] https://www.buildingsmart.be/
[13] https://www.crtib.lu/
[14] https://www.crtib.lu/fr/bim-au-luxembourg
[15] https://www.rijksvastgoedbedrijf.nl/onderwerpen/b/bouw-informatie-model
[16] https://www.digigo.nu/ilsen-en-richtlijnen/bim-basis-ils/
[17] https://www.digigo.nu/ilsen-en-richtlijnen/bim-basis-ils/downloads/
[18] https://www.digigo.nu/ilsen-en-richtlijnen/bim-basis-ils/beheer/
[19] https://www.digigo.nu/ilsen-en-richtlijnen/bim-basis-ils/handleidingen/
[20] https://www.digigo.nu/ilsen-en-richtlijnen/ils-ontwerp-en-engineering/ and [5]
[21] https://www.digigo.nu/ilsen-en-richtlijnen/ils-configurator/
[22] https://www.digigo.nu/ilsen-en-richtlijnen/bim-basis-ils/praktijk/1-naa-k-t-eenduidige-materiaalbenaming
[23] https://ketenstandaard.nl/nlbe-sfb-facts/
[24] https://www.buildingsmart.be/about/ and https://www.buildingsmart.be/downloads-resources/ and https://www.buildingsmart.be/news/
[25] https://www.bimids.eu/lu-fr
[26] https://www.crtib.lu/fr (procurement link /fr/mpu)
