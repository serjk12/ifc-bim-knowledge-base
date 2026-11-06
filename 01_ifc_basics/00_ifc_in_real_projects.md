# How IFC is used in real projects: workflows, roles, deliverables

**In plain words**

IFC (Industry Foundation Classes) is a neutral, vendor-independent file format for describing buildings and civil structures: what each object is (a wall, a duct, a bridge girder), where it is, what it is made of and which properties it carries. It exists so that an architect on Revit, a structural engineer on Tekla, an MEP designer on another tool and a client with a free viewer can all look at the same model without owning the same software. In real projects IFC is mostly a **one-way snapshot**: each discipline exports its model, a coordinator combines the snapshots, checks them, reports problems, and the authors fix the problems in their *native* tools and export again. It is a delivery and checking format, not a replacement for the native design file. The work happens around it: agreed export settings, naming rules, a shared folder system (CDE), issue tracking (BCF), and requirement checks (IDS).

**Last researched: 2026-11-06**

Reading guide: `[n]` markers point to the Sources section. "(unverified)" marks statements from general domain knowledge or single weak sources that I could not confirm on a primary page. "(illustrative)" marks invented examples.

---

## 1. Why IFC exists: openBIM and vendor neutrality

- **The problem.** Every BIM authoring tool (Revit, Archicad, Tekla, Allplan, Renga, and others) has its own proprietary file. A project team almost never uses a single product, so a neutral exchange format is needed. buildingSMART argues that heavy reliance on one vendor's databases creates lock-in, and promotes vendor-neutral data structures [1][2].
- **What IFC is formally.** An open standard maintained by buildingSMART International and published by ISO as **ISO 16739-1**. The version commonly called IFC4 was published as ISO 16739-1:2018; **IFC 4.3** (which adds roads, railways, bridges, tunnels, ports and waterways) was approved as a final buildingSMART standard and published by ISO as **ISO 16739-1:2024** [1][22][23]. The older **IFC2x3** is still very common in practice (unverified for current market share; it is widely reported as the most-requested version in many briefs).
- **openBIM.** buildingSMART's umbrella term for working with open standards instead of one vendor's stack. The usual set: **IFC** (data model), **IDM / MVD** (what to exchange and in which subset), **IDS** (machine-readable requirements), **BCF** (issue communication), **bSDD** (shared dictionary of classifications and properties) [1][6][32].
- **Public policy.** Several governments and public clients require or prefer IFC for deliveries. Examples seen in sources: Singapore requires IFC-SG for regulatory submission via CORENET X [16][17]; Spain approved a BIM Plan for public procurement in June 2023 (whether it names IFC specifically was not confirmed) [37]; Finland's state property agency is reported (blog source, secondary) to have required IFC since 2007 [37]; Moscow now asks for IFC models in architectural-urban-planning (АГР) approval (see 4.4) [19]. buildingSMART publishes a "Global openBIM Mandates" document, but its PDF could not be fetched in this research (HTTP 403), so the country list here is partial [1].

**Why a tester should care:** an MCP server that opens IFC is working with the *neutral deliverable*. It is typically given a model that somebody else exported with some settings. Many "bugs" a user sees (missing property, wrong quantity, weird class) come from the export, not from the MCP tool.

---

## 2. Reference model vs design transfer: why IFC is not for round-trip editing

### 2.1 The two ideas

| Idea | Meaning | Typical IFC4 MVD |
|---|---|---|
| **Reference model** | You export a model so others can view, measure, check, coordinate against it. They do not change it; if they need a change they ask the author. Flow is mainly one-directional. | **IFC4 Reference View** (also **IFC2x3 Coordination View 2.0** for IFC2x3) |
| **Design transfer** | Receiver may insert, delete, move and modify elements in a limited parametric way, e.g. an architect handing the building to an engineer who needs to adjust geometry. | **IFC4 Design Transfer View** |

Graphisoft's help describes the Reference View as intended for reference-model workflows with one-directional exchange (requested shape changes go back to the author as change requests), and the Design Transfer View as supporting editing but "not meant for round-trip exchange" [3]. The Coordination View 2.0 is described as the IFC2x3 view for sharing between architects, structural engineers and building-services designers [3].

### 2.2 What goes wrong with "round-trip"

- IFC does not carry the parametric intelligence of the native file (Revit families, constraints, schedules, view setups, sheets). Import re-creates geometry as generic or imported objects, and IDs/GUIDs and geometry representations are not guaranteed to survive a cycle [2].
- A buildingSMART forum discussion (2019) asks whether the Design Transfer View scope changed from excluding "round-trip scenarios" to excluding "data-roundtrip"; replies from the open-source side argue that reliable round-trip is possible only for a restricted, well-defined scope (e.g. only extrusions), and that exact IDs and vertex order will change between cycles even when objects, geometry and properties are preserved [2]. An archive-oriented reply argued that long-term preservation of information requires round-trip fidelity [2].
- A Revit exporter issue (revit-ifc #629, opened 2023, closed 2025) is a good real example: a user wanted Design Transfer View because Reference View dropped the material layers of walls/slabs; DTV geometry differed from RV geometry for some elements. A maintainer noted DTV is not an official, certified-to-be-complete route (newer Revit labels it unofficial or experimental) and that IFC4 lacked a direct replacement for the IFC2x3 Coordination View. In 2025 a user could not reproduce the geometry problem in Revit 2023-2025 and the issue was closed [4].
- Autodesk's own export documentation says the IFC4 Reference View is meant as a reference model that is not modified, while Design Transfer View may create `IfcAdvancedBrep` geometry in some cases [36].

**Practical rule used by coordinators:** *Edit in native, export IFC, never re-import the IFC as the new master.* IFC links (Revit "Link IFC") are fine as background references; "Open IFC" and then continuing to design in the result is the pattern that causes pain [5][36].

---

## 3. Exchange requirements: IDM, MVD, IDS

| Layer | What it answers | Standard / artefact | Status in sources |
|---|---|---|---|
| **IDM** (Information Delivery Manual) | *Who* hands over *what* to *whom* at *which* stage - the process and information needs, written for humans | ISO 29481-1 (framework), ISO 29481-2 (interaction framework); CEN/TR 17741 is a plain-language guide to writing an IDM [9] | IDM methodology; MVD is only introduced, not specified, in the CEN guide [9] |
| **MVD** (Model View Definition) | *Which subset of the IFC schema* an exporter/importer must support for that exchange | Reference View, Design Transfer View, Coordination View 2.0; also COBie (described by NIBS as an MVD of IFC) [26] | Software is certified by buildingSMART against specific MVDs (see 3.2) |
| **IDS** (Information Delivery Specification) | *Which concrete data* (classes, properties, values, classifications, materials) a given model must contain, in a form software can check automatically | XML (XSD) file; **IDS 1.0 approved as a final buildingSMART standard in June 2024** (official page says 1 June 2024; announcement 4 June) [7][8] | Positioned as the machine-readable counterpart to the ISO 19650 information requirements [6][8] |

### 3.1 How they fit in a real project

1. The **client** writes information requirements (EIR in ISO 19650 terms) saying: deliver IFC (version X, view Y), at LOIN/stage Z, with these property sets and this classification.
2. If the client or authority is advanced, part of that is an **IDS file** that the designers load into their authoring tool to see what is expected, and that the coordinator runs against each export [6]. A Russian practitioner article shows an expertise body (St Petersburg state expertise, ГАУ «ЦГЭ») publishing requirements and checking models via IDS with the Python library IfcOpenShell (`ifctester`) [20].
3. The **BIM Execution Plan (BEP)** of the delivery team turns that into concrete export settings (IFC version, MVD, which categories map to which IFC classes, which parameters become Psets).
4. Each export is **validated** (viewer check, rule-based checker such as Solibri, IDS check, sometimes IFC schema validation) before it is published.

Adoption caveat: a Nordic software vendor writing in 2025/2026 (page date unclear) says most software does not yet support IDS or bSDD, so use is still early; Archicad 28+ can import an IDS to create property sets/classifications [6].

### 3.2 Versions: what to ask for

- **IFC2x3 + Coordination View 2.0** - the long-standing "safe" choice; widest tool support [3].
- **IFC4 + Reference View** - what e.g. Singapore's CORENET X supports for submissions [17].
- **IFC4 Design Transfer View** - supported by some exporters but described as unofficial/experimental in newer Revit versions [4].
- **IFC 4.3 (ISO 16739-1:2024)** - needed for infrastructure; at the time of the Nordic BIM page used here, no software was certified for it, tools could open/save but results were not guaranteed, and the advice for building projects was to specify a certified format (IFC4 or IFC2x3) [24]. Check buildingSMART's current certification list before relying on this (page date unclear).

---

## 4. Typical IFC workflows

### 4.1 Design coordination and federation

**Federation** = loading several discipline models (architecture, structure, MEP, façade, site) into one scene without merging them into one file, so each owner keeps control of their part.

Typical loop:

1. Each discipline exports IFC (or native-to-viewer) on the agreed cadence (section 7).
2. The coordinator uploads to the CDE (section 8) and loads all models into a coordination tool (Solibri, Navisworks, BIMcollab Zoom, Trimble Connect, Revizto, ACC Model Coordination - which of these read IFC directly vs through plug-ins varies; Navisworks has an IFC reader that the open-source Revit IFC project also improves [5]).
3. Models are checked for **basics first**: same coordinates and units, correct levels, nothing floating 50 km away, no duplicate or empty models [30].
4. Rule checks and clash tests run; results become **BCF issues** assigned to a discipline.
5. In the weekly meeting the issues are triaged; authors fix in native; next export closes issues.

Guidance seen from practitioners: tag clashes to a discipline *before* the meeting, do not use the meeting itself to find clashes, and re-post the corrected model the same day (project-protocol example) [31].

### 4.2 Clash detection

- **Hard clash** (geometry intersects), **soft/clearance clash** (too close to maintain/insulate), and **workflow clash** (e.g. a duct placed where the structural model has no opening yet) - terminology is common practice (unverified as a formal standard).
- **BCF** (BIM Collaboration Format) carries the issue, viewpoint, comments and status between tools and companies. It began as an XML schema introduced by Tekla and Solibri and exists as file-based exchange and as a web-service API [32]. Versions mentioned in sources: BCF 2.1 and BCF 3.0 [32].
- Static PDF/Excel clash reports go stale as soon as someone fixes the model, which is why BCF-capable platforms are recommended [30][32].
- Pre-filtering matters: broad "everything vs everything" tests create huge, noisy reports; use selection sets per system/area and prioritize structure and architecture first [30].
- IFC-specific caveat: IFC geometry may be tessellated or simplified compared to native; clearance zones/insulation modelled as non-IFC data may be missing (unverified, common practitioner experience).

### 4.3 Quantity takeoff (5D cost / sustainability)

- Quantities in IFC come from **quantity sets** (`Qto_WallBaseQuantities`, `Qto_SlabBaseQuantities`, etc.), which in Revit are written only if **"Export base quantities"** is ticked on the Property Sets tab of the IFC export setup [27][28]. Autodesk's API documentation describes the option as exporting the set of IFC quantities that Revit currently supports, i.e. a subset [28].
- Real forum answers (a sustainability consultant asking how to get material quantities from IFC for life-cycle assessment): IFC is better as an exchange format than as a takeoff database; results depend heavily on export quality; per-material quantities of layered elements are not directly exported, but can be estimated from net area, layer thickness and density; modelling each material as its own element makes it easier; tools suggested were Solibri, IfcOpenShell, BlenderBIM/Bonsai, and commercial quantity tools [27].
- Wall layers are a known pain point: `Qto_WallBaseQuantities` plus layer sets expose thicknesses and names, but building a takeoff from them is awkward [29].
- Exporter version matters: revit-ifc release notes list fixes to base quantities (for example GrossArea for walls exported as `IfcCovering`) [5][29].
- Expect differences between a Revit schedule and IFC quantities (gross vs net area, openings, layer handling) - the explanation is partly my inference rather than a source (unverified).
- Tekla documents its own IFC base-quantities option for steel/concrete [38] (search result title only; content not read).

### 4.4 Permit / expertise submission

| Place | What the sources say |
|---|---|
| **Singapore - CORENET X** | IFC-SG (an extension of IFC4 Reference View with local regulatory parameters from agencies such as BCA, URA, LTA, NEA, NParks, PUB, SCDF) is the submission format; the Code of Practice defines per-gateway requirements; an IFC-SG validator is part of the toolkit [17]. A URA circular (dc25-01) states: CORENET X mandatory for new projects with GFA >= 30,000 m2 from 1 Oct 2025, for all new projects from 1 Oct 2026, and for all ongoing projects from 1 Oct 2027; IFC-SG BIM submission is mandatory for new erections and major A&A with >= 5,000 m2 new GFA, and is not mandatory for ongoing projects being onboarded [16]. Search snippets showed other thresholds in other documents; **check the current BCA/URA circulars** since today's date is after 1 Oct 2026 and changes are possible. |
| **Moscow, Russia (АГР - архитектурно-градостроительное решение)** | Per a business-press item (search snippet; page itself returned HTTP 401): from 2 April 2026 a ЦИМ АГР in IFC is required in addition to FBX models; the project site must export as `IfcSite` [19]. |
| **Mosgosexpertiza / St Petersburg ЦГЭ (госэкспертиза)** | Published requirements include mapping of model elements to IFC classes (separately for КР, ИОС, АР sections - structural, engineering systems, architecture), naming of exported parameters, and file-naming rules [21][20]. Based on the IFC 4.x standard (search snippet). |
| **Russian national standards** | СП 333.1325800 and related ЦИМ rules exist, but I could not retrieve their text in this research; check the official source (unverified). |

Pattern across jurisdictions: authority publishes (a) which IFC version/view, (b) which IFC class each model category must map to, (c) which properties/classifications, (d) a validator or checklist. Failures are usually mapping or property-naming mistakes, not geometry.

### 4.5 Handover and facility management (FM)

- At handover the client wants **asset data** (what equipment, where, manufacturer, serial, warranty, maintenance) more than geometry. **COBie** carries asset data; NIBS describes it as an MVD of IFC that can also be delivered as a spreadsheet; v3 was announced in 2022 [26].
- ISO 19650-3 covers the operational phase and the asset information model (AIM) (general knowledge; I found no primary page in this research - unverified) [26].
- Real-life friction: models from design are not "as-built", spaces and systems are not always modelled in a way FM needs, classification is inconsistent. The usual fix is a pre-agreed IDS/property list and a final validation before handover (illustrative of common practice).

### 4.6 Infrastructure delivery

- IFC 4.3 introduced alignment, road, rail, bridge, tunnel, port and waterway entities (from the IFCRail / IFCInfra work) [1][22][25].
- Tool support is the limit: a Nordic BIM vendor page says no software was certified for IFC 4.3 when written; Archicad 29+ imports/exports it [24]. An Italian trade article says large clients can start rewarding IFC 4.3 use in tenders, and Italian vendors are implementing it [25]. I found **no source documenting a national infrastructure programme that mandates IFC 4.3** in this research.
- Infrastructure models are often georeferenced in a national grid and span kilometres; coordinate handling (section 9) is the first thing to check (unverified generalisation).

---

## 5. Roles and deliverables

| Role | What they do with IFC | Deliverable / output |
|---|---|---|
| **Client / owner (appointing party)** | Sets EIR, chooses IFC version/MVD, sets acceptance criteria, owns the AIM after handover | EIR, IDS (if used), acceptance decision |
| **BIM manager / information manager** | Writes/maintains BEP, export settings, naming rules, CDE structure, validation procedure; arbitrates standards | BEP, MIDP/TIDP-style delivery plans (ISO 19650 terms, general knowledge), export-setting files, mapping tables |
| **BIM coordinator** | Collects exports, federates, checks, runs clash tests, issues BCF, runs the coordination meeting | Federated model, clash/issue reports, BCF, meeting minutes |
| **Discipline modelers (architect, structure, MEP...)** | Model in native tool, export IFC with the agreed settings, fix issues | Discipline IFC + native model, export log |
| **Reviewer / authority / expert** | Checks the submission against rules (code, completeness) often on IFC | Review comments, BCF, pass/fail |
| **Estimator (QS)** | Reads quantities from IFC or native, matches to cost items | Quantity lists, cost plan |
| **Facility manager** | Consumes COBie/IFC asset data | CAFM import, maintenance plan |

---

## 6. Export cadence

Common practice (not a standard; unverified as universal):

- **Weekly** IFC publication before the coordination meeting; **milestone** exports for design stage gates (concept, developed, technical, tender); **ad hoc** export when a major change affects others; **final** export for permit/expertise or handover.
- Each export is a *full replacement* of the previous discipline IFC, not an increment. The coordinator keeps previous versions as archive/superseded.
- Exporting from a **central/detached model synchronized that morning** avoids exporting someone's half-finished local copy (illustrative).

---

## 7. File naming and metadata (ISO 19650)

ISO 19650-2 requires a project naming convention for information containers; the UK National Annex defines a common pattern, and other countries have their own annexes (the UK pattern is general knowledge; the field names vary by annex) [13].

Seven fields appear in most descriptions: **Project - Originator - Volume/System - Level/Location - Type - Role - Number**, with classification optional [11][12][13]. Autodesk's naming-standard template splits them into naming attributes (those seven) and related metadata attributes (Status, Revision, Classification) and allows hyphen, underscore or point as delimiter [11]. Example format shown in an Autodesk reseller article:

`25313-IMGT-ZZ-01-DR-A-0001` (project 25313, originator IMGT, volume ZZ = all, level 01, type DR = drawing, role A = architect, number 0001) [12]

For a model it might be `25313-IMGT-ZZ-XX-M3-A-0001.ifc` (illustrative; `M3` = 3D model, `XX` = not level-specific, per common UK-style code lists - unverified for your annex).

Gotchas: field names differ (volume/level in the ISO text vs functional/spatial breakdown, form and discipline in the older UK annex) [13]; the number length must be consistent within a project; Qatar's Ashghal standard, for example, uses its own 29-character scheme [13]. In Russia, expertise bodies set their own file-naming rules [21].

---

## 8. CDE flow: WIP / Shared / Published (and Archive)

ISO 19650 defines four CDE states: **Work in Progress (WIP)**, **Shared**, **Published**, **Archive** [10][14]. The **status/suitability codes** (S0, S1...) come from a UK-layer table, not from the ISO text itself according to one practitioner blog [14] - treat them as an annex-dependent convention.

Autodesk's Docs naming-standard help maps them like this [10]:

| CDE state | Codes | Meaning |
|---|---|---|
| WIP | S0 | initial status, preliminary |
| Shared (non-contractual) | S1 | suitable for coordination |
| | S2 | suitable for information |
| | S3 | suitable for review and comment |
| | S4 | suitable for stage approval |
| | S5 | withdrawn |
| | S6 / S7 | suitable for PIM / AIM authorization |
| Published (contractual) | A1, An | authorized and accepted |
| | B1, Bn | partial sign-off with comments |
| Published (AIM acceptance) | CR | as-constructed record |
| Archive | - | not listed on that page |

(Other sources define S1/A1 differently; sources conflict, so use your project's own table [14].)

**How an IFC travels:** modeler exports into their own **WIP** folder, internal check, then publishes into **Shared** with status S1 ("for coordination"); the coordinator federates; once approved by the task-team lead / information manager gate it is moved to **Published** (A-codes) for the client; old versions go to **Archive**. The UK BIM Framework's Guidance Part C covers CDE workflow, but I could not extract its text (PDF unreadable via the fetch tool) [15].

---

## 9. What goes wrong in practice

1. **Wrong or inconsistent coordinates.** Very common. Revit has Internal Origin, Project Base Point and Survey Point; IFC export has a "coordinate base" setting. Forum cases: IFC lands at the Project Base Point instead of the Survey Point on link; Z measured from Level 1 instead of the survey datum; rotation/elevation of survey point ignored; models exported with real-world (map) coordinates are placed very far from the origin and Revit has movement limits for the base point [34]. A common fix: set base/survey point coordinates carefully, export with "Shared Coordinates" as coordinate base, and agree a coordinate protocol in the BEP [30][34]. Revit natively did not allow typing geolocated coordinates before certain IFC exporter versions (19.4.0.0 / 20.2.0.0 / 21.1.0.0 per an OSArch wiki snippet) [34].
2. **GUIDs change between exports.** Without the option "store the IFC GUID in an element parameter", GlobalIds can change per export, which breaks BCF issue links and change tracking. Reported advice: use *Link and Export* rather than *Open and Export*, export links as separate IFCs, and enable the GUID-in-parameter option [33]. Even with the option, one issue reported room GUIDs changing on each export in Revit 2022 [33]. Revit's UniqueId cannot be set by hand [33].
3. **Wrong IFC class or missing properties.** Mapping from Revit categories to IFC classes and from Revit parameters to Psets is configured per project; defaults often do not match the client's list [5][36].
4. **Missing materials / layers in Reference View** (see revit-ifc #629) leading people to switch to Design Transfer View, then hitting geometry differences [4].
5. **Missing or misleading quantities** because base quantities were not exported, or wall layers are not separated [27][28][29].
6. **Huge files / slow viewers.** Exporting the whole project with 3D families and details; fix by exporting only visible elements of a prepared 3D view and excluding 2D/annotation (the "Export only elements visible in view" option exists [36]).
7. **Noisy clash reports** because models were not cleaned or filtered [30].
8. **Static reports** instead of BCF [30][32].
9. **Exporting stale or unsynchronised models.** (illustrative common experience)
10. **Round-trip expectations** (section 2).
11. **Version drift of the exporter.** The Revit IFC exporter is open source (Autodesk/revit-ifc on GitHub, LGPLv2); a newer open-source add-on can override the built-in exporter shipped with Revit, so two team members can export differently [5].
12. **Certification confusion.** "Software X exports IFC4.3" is not the same as "buildingSMART certified" [24].

---

## 10. A day in the life of a BIM coordinator working with IFC (composite, illustrative)

Built from practitioner descriptions of the coordinator's weekly cycle [30][31] plus general practice; times are invented.

| Time | Activity |
|---|---|
| 08:30 | Check the CDE: which disciplines published IFC since yesterday? Note who is late. Compare file names to the BEP convention; reject mis-named files back to WIP (section 7). |
| 09:00 | Load architecture, structure, MEP and site IFCs into the coordination tool. First check: do they overlap spatially? Do levels match? Is anything at the wrong location or in the wrong units? (Section 9 item 1). |
| 09:45 | Run rule-based checks / IDS against each IFC: required classes, property sets, classification codes. List failures per author, send as BCF or a short list. |
| 10:30 | Run the agreed clash tests (structure vs MEP, MEP vs architecture ceilings), with filtered selection sets. Remove obvious false positives, group duplicates, assign each clash to one discipline. |
| 12:00 | Prioritise: structure/architecture conflicts and large mains first, small pipes later [30]. Create BCF issues with viewpoints. |
| 13:00 | Prepare the agenda and the issue list (not a clash-hunting session) [31]. |
| 14:00 | Coordination meeting: walk through issues, decisions, owners and deadlines; unresolved items escalated to discipline leads [31]. |
| 15:30 | Answer questions: "why is my duct not in the model?" (class mapping), "why did the GUID change?" (export option), "why is the quantity different from Revit?" (section 4.3). |
| 16:30 | Update the issue tracker; set up tomorrow's re-check once re-exports arrive; update the status of models (S1 to S2/S3 etc.) in the CDE. |
| 17:00 | Note recurring export mistakes and feed them back to the BIM manager to adjust the BEP. |

---

## Typical questions people ask about this

Real questions found (linked); invented ones marked.

**Real (paraphrased)**

1. How can I get lists of material quantities out of IFC files more easily than with Revit schedules, for life-cycle assessment? - [buildingSMART forum thread](https://forums.buildingsmart.org/t/which-software-to-create-lists-of-quantities-of-the-used-building-materials/5181) [27]
2. Is IFC round-trip (export and re-import without loss) something buildingSMART avoids, and does the Design Transfer View cover geometry? - [buildingSMART forum](https://forums.buildingsmart.org/t/ifc-design-transfer-view-and-roundtrip/1384) [2]
3. Why does Revit's IFC4 Design Transfer View give different geometry than Reference View, and why does Reference View drop material layers? - [revit-ifc issue #629](https://github.com/Autodesk/revit-ifc/issues/629) [4]
4. Why do the room GlobalIds change on every export even with the store-GUID option enabled? - [revit-ifc issue #521](https://github.com/Autodesk/revit-ifc/issues/521) [33] (title not fetched; summary from search snippet)
5. Why do my IfcDoor GUIDs differ between two exports of the same model? - [Autodesk forum](https://forums.autodesk.com/t5/revit-architecture-forum/exporting-to-ifc/m-p/10941701) [33] (snippet only)
6. Why are the IfcWallBaseQuantities wrong or missing? - [Autodesk forum](https://forums.autodesk.com/t5/revit-architecture-forum/wrong-ifcwallbasequantities/m-p/9003220) [29] (snippet only)
7. Why does an exported IFC land at the wrong position when linked back into Revit, and should I use Shared Coordinates? - [Autodesk forum](https://forums.autodesk.com/t5/revit-architecture-forum/shared-coordinates-and-ifc-link-positioning/m-p/9598663) [34] (snippet only)
8. How do I check IFC models against requirements automatically (Russian-language practitioner article, using IDS + IfcOpenShell)? - [Habr](https://habr.com/p/883016) [20]

**Illustrative (invented, realistic)**

9. (illustrative) Which IFC version and MVD should I ask the architect for: IFC2x3 Coordination View 2.0, IFC4 Reference View or IFC 4.3?
10. (illustrative) Can I edit the IFC the engineer sent me and send it back so they keep working on it?
11. (illustrative) Our EIR says "IFC, LOD 300" but nothing else. What should I put in the BEP so the export is checkable?
12. (illustrative) What does status S2 vs S3 mean in the CDE, and who may move a file from Shared to Published?
13. (illustrative) How should I name an IFC file under ISO 19650 for the structural model of Block B, level 03?
14. (illustrative) Why does Navisworks show 4,000 clashes between our IFC models and how do I reduce the noise?
15. (illustrative) How do I turn my clash list into BCF issues that the structural engineer can open in their tool?
16. (illustrative) Quantity takeoff from IFC gives a different wall area than the Revit schedule. Which one do I trust?
17. (illustrative) What does the authority check in an IFC submission and where do I find their IDS or checklist?
18. (illustrative) What do I deliver at handover for FM: IFC, COBie spreadsheet, or both?
19. (illustrative) Can I deliver a road and bridge project in IFC4 or must it be IFC 4.3?
20. (illustrative) How often should the disciplines publish IFC, and who checks the export before it goes into Shared?
21. (illustrative, RU) Заказчик требует ЦИМ в IFC для экспертизы: какой версией и какими настройками экспорта из Revit пользоваться? (Customer requires a CIM in IFC for expertise: which version and Revit export settings?)
22. (illustrative, RU) После экспорта в IFC потерялись параметры и классы не те, как настроить маппинг? (After IFC export parameters are lost and classes are wrong; how to set up mapping?)
23. (illustrative, MCP) Open the architectural IFC and tell me which discipline files are missing from the federation compared with the BEP list.
24. (illustrative, MCP) Check that every IfcDoor in the model has a fire-rating property and list the ones that do not.

---

## Common pitfalls and misconceptions

- **"IFC is just a 3D file format."** It is a data model (classes, properties, relationships). Geometry is only a part.
- **"Exporting to IFC and re-importing gives me my model back."** No; see section 2.
- **"Design Transfer View is the better, richer view."** It is not a drop-in upgrade: it is described as unofficial/experimental in newer Revit versions, and users report geometry differences [4].
- **"If my viewer shows it, the data is right."** Viewers can show geometry correctly while properties or classes are wrong or missing.
- **"IFC4.3 is only for roads."** It also contains refinements for buildings, but the headline additions are infrastructure [1][24].
- **"IDS replaces BEP/EIR."** IDS is the machine-checkable part of the requirements; process, responsibilities and naming still live in EIR/BEP [6].
- **"ISO 19650 defines S0, S1, A1..."** Reportedly the codes come from a national-annex/UK table; the ISO text defines the four states [14].
- **"The IFC GUID equals the Revit ElementId."** No; it is a separate identifier, stored/derived by the exporter and not stable unless configured [33].
- **"Everyone must use IFC."** Mandates vary by country and by authority; check local requirements (section 4.4).
- **Tester note:** when an MCP server returns "property not found", first check whether the IFC was exported with property sets/base quantities enabled, and which MVD was used.

---

## Gaps and limits of this research

- Many official pages returned HTTP 403 to the fetch tool: technical.buildingsmart.org, buildingsmart.org (IFC, mandates PDF, IDS announcement), iso.org, Autodesk Support, Graphisoft community FAQ, some Autodesk forum threads. Facts attributed to them come from search-result snippets and are marked accordingly.
- The web-search budget ran out before the planned searches for: ISO 19650 primary text, Navisworks/IFC community threads, and Moscow АГР official sources. Those topics rely on weaker sources or general knowledge (marked unverified).
- UK BIM Framework Guidance Part C could not be text-extracted (PDF streams unreadable); CDE gateway details are therefore general knowledge.
- Suspicious or pirated sites: none encountered/used.
- Facts that need re-checking before use in tests: CORENET X thresholds and dates [16]; Moscow IFC requirement date [19]; IFC 4.3 software certification status [24]; exact BCF versions [32].

---

## Sources

1. buildingSMART - Industry Foundation Classes (IFC) (seen in search results; fetch HTTP 403): https://www.buildingsmart.org/standards/bsi-standards/industry-foundation-classes/
2. buildingSMART forum - IFC Design Transfer View and roundtrip (read): https://forums.buildingsmart.org/t/ifc-design-transfer-view-and-roundtrip/1384
3. Graphisoft Archicad 29 help - Model View Definitions (read): https://help.graphisoft.com/AC/29/INT/_AC29_Help/121_IFC/121_IFC-47.htm
4. Autodesk/revit-ifc issue #629 - Design Transfer View wrong geometry (read): https://github.com/Autodesk/revit-ifc/issues/629
5. Autodesk/revit-ifc repository README (read): https://github.com/Autodesk/revit-ifc
6. Nordic BIM - What is the buildingSMART IDS standard (read; vendor/community article): https://www.nordicbim.com/en/insights/what-is-the-buildingsmart-ids-standard
7. buildingSMART - IDS v1.0 approved as final standard (search snippet; fetch 403): https://www.buildingsmart.org/?p=30065
8. buildingSMART - Information Delivery Specification (search snippet): https://www.buildingsmart.org/standards/bsi-standards/information-delivery-specifications-ids/
9. CEN/TR 17741:2021 (IDM guidance; search snippet): https://genorma.com/en/standards/cen-tr-17741-2021
10. Autodesk Docs - Status Codes (read): https://help.autodesk.com/cloudhelp/ENU/Docs-Files/files/files-naming-standard/Status_Codes.html
11. Autodesk Docs - Create Naming Standards (read): https://help.autodesk.com/cloudhelp/ENG/Docs-Files/files/files-naming-standard/Set_Up_Naming_Standard.html
12. ImagineIT - Forma Data Management naming standard (search snippet; reseller): https://resources.imaginit.com/construction/forma-data-management-naming-standard-mandatory-vs-optional-fields
13. UK National Annex guidance (search snippet): https://www.cdbb.cam.ac.uk/files/national_annex_guidance.pdf ; Ashghal (Qatar) file naming: https://www.ashghal.gov.qa/en/Services/GIS%20and%20CAD%20Manuals/ASHGHAL%20BIM%20STANDARD/D0201_File%20Naming%20Convention%20for%20BIM%20%26%20CAD_V1.pdf
14. bimfix blog on ISO suitability codes (community blog, search snippet): https://bimfix.blogspot.com/
15. UK BIM Framework Guidance Part C (could not extract text): https://www.ukbimframework.org/wp-content/uploads/2021/02/Guidance-Part-C_Facilitating-the-common-data-environment-workflow-and-technical-solutions_Edition-1.pdf
16. URA circular dc25-01 - Updates to CORENET X implementation plan (read): https://www.ura.gov.sg/guidelines/circulars/dc25-01/
17. BCA CORENET X FAQ - getting ready (search snippet): https://www1.bca.gov.sg/regulatory-info/building-control/corenet-x/corenet-x-faq/getting-ready
18. CORENET submission workflows (search result only): https://info.corenet.gov.sg/regulatory-process/about-the-new-submission-process/submission-workflows
19. RBC Companies - reasons for refusal of ЦИМ АГР in IFC (search snippet; fetch 401): https://companies.rbc.ru/news/axjEyNHHOq/iz-za-chego-mogut-otkazat-v-soglasovanii-tsim-agr-v-formate-ifc/
20. Habr - IFC checking against IDS with ifcopenshell (read, Russian): https://habr.com/p/883016
21. Mosgosexpertiza requirements document MKE OD 24-178 (search snippet): https://digest.wizardsoft.ru/wp-content/uploads/media/doc/2025/MKE-OD-24-178Chast3.pdf ; SPb ЦГЭ requirements: https://spbexp.ru/upload/iblock/0b4/trebovaniya_k_tsim_model_razdela_ios.pdf
22. buildingSMART - IFC 4.3 approved as final standard (search snippet): https://www.buildingsmart.org/ifc-4-3-approved-as-a-final-standard/
23. buildingSMART - IFC 4.3 formally published as ISO standard (search snippet): https://www.buildingsmart.org/?p=29521
24. Nordic BIM - IFC 4.3 (read; vendor): https://www.nordicbim.com/knowledge/en/ifc-4.3
25. Ingenio - IFC per le infrastrutture (Italian trade article, search snippet): https://www.ingenio-web.it/articoli/ifc-per-le-infrastrutture-solo-una-questione-di-volonta/
26. NIBS COBie v3 (search snippet): https://www.nibs.org/cobie ; Catenda glossary: https://catenda.com/glossary/construction-operations-and-building-information-exchange-cobie
27. buildingSMART forum - software for lists of quantities (read): https://forums.buildingsmart.org/t/which-software-to-create-lists-of-quantities-of-the-used-building-materials/5181
28. Revit API - IFCExportOptions.ExportBaseQuantities (search snippet): https://help.autodesk.com/cloudhelp/2026/ENU/Revit-API-MainReference/files/html/209a8948-d2c0-0c4e-d3b7-241535ccbad8.htm
29. Autodesk forum - Wrong IfcWallBaseQuantities (search snippet): https://forums.autodesk.com/t5/revit-architecture-forum/wrong-ifcwallbasequantities/m-p/9003220
30. BIMcorner - five common mistakes of new BIM coordinators (read; community blog): https://bimcorner.com/?p=42034
31. Archgyan - how to run BIM coordination meetings (search snippet; blog): https://archgyan.com/how-to-run-bim-coordination-meetings/
32. buildingSMART BCF (search snippet): https://www.buildingsmart.org/standards/bsi-standards/bim-collaboration-format/ ; Teocomi BCF overview (community): https://teocomi.com/bim-collaboration-format/
33. Building Coder - Unique Id and IFC GUID: https://blog.autodesk.io/unique-id-and-ifc-guid/ ; revit-ifc issue #521: https://github.com/Autodesk/revit-ifc/issues/521 ; Autodesk forum (snippet): https://forums.autodesk.com/t5/revit-architecture-forum/exporting-to-ifc/m-p/10941701
34. Coordinates threads (search snippets): https://forums.autodesk.com/t5/revit-architecture-forum/shared-coordinates-and-ifc-link-positioning/m-p/9598663 ; https://wiki.osarch.org/index.php/Revit_setup_for_OpenBIM/Revit_IFC_geolocation ; https://community.pix4d.com/t/export-ifc-from-revit-geolocation/29413
35. Graphisoft community - FAQ about IFC (search result only; fetch 403): https://community.graphisoft.com/t5/Data-Exchange-articles/Frequently-Asked-Questions-About-IFC/ta-p/304113
36. Autodesk Revit help - IFC Export Setup Options (search snippet): https://knowledge.autodesk.com/support/revit-products/learn-explore/caas/CloudHelp/cloudhelp/2020/ENU/Revit-DocumentPresent/files/GUID-E029E3AD-1639-4446-A935-C9796BC34C95-htm.html
37. Spain public procurement BIM plan summary: https://public-buyers-community.ec.europa.eu/system/files/2024-02/Executive%20Summary%20_EN%20A4%20web.pdf ; Finland 2007 claim (blog, secondary): https://medium.com/specter-automation-insights/bim-adoption-across-the-world-a-global-outlook-1b3879f23bc6
38. Tekla Structures - IFC base quantities (title only): https://support.tekla.com/cs/doc/tekla-structures/2021/int_ifc_base_quantities
