# Nordic and Baltic countries: BIM/IFC requirements

## In plain words

The Nordic countries (Norway, Denmark, Sweden, Finland, Iceland) are among the earliest adopters of open BIM. Large state clients (property agencies, road and rail authorities) have required IFC deliverables since the mid-2000s. The Baltic countries (Estonia, Latvia, Lithuania) came later and are still moving from industry-led guidance to legal rules. The Nordics have no single "BIM law". Requirements usually come from the client (state property agency, road/rail authority, municipality), from national BIM guidelines published by the local buildingSMART chapter or a BIM association, and from national classification standards. Denmark is the main exception, because it had a state-level executive order on ICT in construction. For a tester, the practical point is this: "the requirement" in these countries usually means a client document, a Property Set list, a naming convention and an IFC export setting (for example IFC2x3 Coordination View 2.0 or an IFC4 view), not a statute.

**Last researched: 2026-11-06** (QA pass 2026-11-06: Wikipedia pages for Statsbygg and Norwegian BIM re-fetched; the web search budget was exhausted, so the many `(unverified)` Denmark, Sweden, Finland, Estonia, Latvia and Iceland items could not be upgraded and stay marked; see `_meta/qa/qa-standards-2.md`.)

**Research limitations (read first).** This document was produced under a hard limit: the web-search budget was exhausted before any search ran, so only direct page fetches were possible, and many official sites (statsbygg.no, DiBK, Trafikverket, Väylävirasto, buildingsmart.org, wiki.buildingsmart.fi, Estonian and Latvian government portals) returned errors, empty JavaScript shells or title-only pages. Facts that were actually confirmed on a fetched page carry a [n] marker. Everything else is general domain knowledge written from memory and marked **(unverified)**. Do not quote unverified items as authoritative. Check them against the primary sources listed under "Gaps".

## Overview table

| Country | Main public "drivers" | Mandate type | Key IFC point | Confidence |
|---|---|---|---|---|
| Norway | Statsbygg (state property), Statens vegvesen, Nye Veier, Bane NOR, DiBK (digital permits) | Client requirements, no national mandate [2] | Large public clients require open-format BIM (IFC) for most or all projects [2] | Medium |
| Denmark | State clients; "IKT-bekendtgørelsen" (executive order on ICT in construction); bips/Molio | Legal for state-funded projects (unverified details) | IFC as delivery format (unverified) | Low-medium |
| Sweden | Trafikverket, BIM Alliance (hosts buildingSMART Sweden) [3][4] | Client requirements and industry guidance | IFC, bSDD, BCF, IDS are the standards promoted in the national Praxi portal [4] | Medium |
| Finland | Senate Properties (Senaatti-kiinteistöt), Finnish Transport Infrastructure Agency, buildingSMART Finland [6][11] | Client requirements built on national "common BIM requirements" series (YTV/YIV/YKV) [6] | IFC-based; Inframodel for infrastructure [6] | Medium |
| Iceland | buildingSMART Iceland (chapter exists [8]) | Voluntary, early stage (unverified) | Not verified | Low |
| Estonia | Digital Construction Cluster; state e-construction platform; RKAS (state real estate) | Cluster and platform driven, moving to rules (unverified) | Not verified | Low |
| Latvia | Ministry and industry roadmap (unverified) | Roadmap, not verified | Not verified | Very low |
| Lithuania | "Skaitmeninė statyba" (Digital Construction) association body [12] | Proposals and legal amendments around 2020-2021 [12] | IFC and a national classifier mentioned [12] | Low-medium |

## IFC basics relevant to all countries

- IFC is registered as ISO 16739-1:2024 (this is the IFC4.3 line); releases run from IFC 1.0 (1996) to IFC4.3 Add2 (2024). IFC4.1 and IFC4.2 are withdrawn [7].
- A valid IFC file contains exactly one `IfcProject` [7]. The common storage format is IFC-SPF (`.ifc`); IFC-XML, IFC-ZIP and ifcJSON also exist [7].
- Most Nordic national requirements in practice still reference **IFC2x3 Coordination View 2.0** or **IFC4 Reference View / Design Transfer View** (unverified for each country). Newer documents increasingly add **bSDD**, **IDS** (Information Delivery Specification) for machine-checkable requirements, and **BCF** for issues [4].
- buildingSMART's public repositories include IDS, IFC4.x-development, IFC5-development, bSDD, BCF-XML, BCF-API and the IFC validation service [9].

Revit practice (general knowledge, unverified in this research): Revit's built-in IFC export offers "IFC 2x3 Coordination View 2.0", "IFC4 Reference View" and "IFC4 Design Transfer View", configured via File > Export > IFC > Modify setup. The property set mapping can be extended with a user-defined parameter-mapping file. Nordic BIM guidelines normally dictate: IFC version/MVD, which Psets/properties must exist, model origin and georeferencing, element naming and classification codes.

## Norway

**Who:** Statsbygg (the Norwegian Directorate of Public Construction and Property) reports to the Ministry of Local Government and Regional Development, manages about 2.7 million m2 in 2,350 buildings (115 of them abroad) [10] (re-confirmed in QA; the Wikipedia Statsbygg page says nothing about BIM or IFC, so BIM claims for Statsbygg rest on [2] and on unverified material). Other big public clients: Statens vegvesen (roads), Nye Veier (roads, company owned by the state [1 does not describe it]), Bane NOR (rail, links to "Tekniske spesifikasjoner" at tekniskregelverk.banenor.no per its homepage), municipalities, hospital trusts. DiBK (Direktoratet for byggkvalitet) runs digital permit services (unverified).

**Policy:** Wikipedia summarises that Statsbygg bases its processes on open-format BIM and several large public clients require IFC for most or all projects; buildingSMART Norway leads national development [2]. There is no general national BIM mandate [2].

**Statsbygg claims to check (unverified):** IFC-based BIM requirements since about 2007; the "Statsbygg BIM Manual" (SBM) with numbered versions (for example 1.2, 2.0); "SIMBA" as the name of the project/approach for model-based delivery. The Statsbygg pages fetched returned only titles, so no version number, date or clause could be confirmed.

**National framework:** buildingSMART Norge publishes **POFIN**, described as the national framework for openBIM that helps projects set requirements, agree on information deliveries and follow them up, in both project and asset management [1]. The site also has a "Kort forklart" (explained briefly) section, consultations (Høring) and domain networks for product, technical, infrastructure, sustainability, legal and owner topics [1]. It offers an "openBIM maturity" self-assessment [1].

**Classification and standards (unverified):** NS 3451 (table of building elements, the dominant "bygningsdelstabell" used in IFC models), NS 3420 (specification texts), the Norwegian adoption of ISO 19650 (NS-EN ISO 19650). QA note: the Norwegian Wikipedia BIM page re-read mentions none of these standard numbers, so they remain from background knowledge. Norway uses "tverrfaglig" (multidisciplinary) coordination models checked in Solibri.

**Ecosystem:** ArchiCAD and Revit are widely used; Tekla and the Norwegian DDS are also used; Solibri for clash and rule checking; StreamBIM for bringing models to site [14]. BIM-tekniker is a one-year vocational course (fagskole, 60 credits) running since 2008 [14] (re-confirmed in QA on the Norwegian Wikipedia page). The Randselva bridge was reported as the world's best modelling project at the 2020 Tekla awards [14] (QA: this claim was not found on the Norwegian Wikipedia page re-read, so treat it as (unverified)). Novapoint (Trimble) is used for infrastructure design (unverified).

## Denmark

**Who and what (unverified except where marked):**
- **IKT-bekendtgørelsen** (executive order on the use of ICT in construction, first issued in the mid-2000s) made digital deliveries, including IFC and digital tender material, mandatory for state-funded construction above a value threshold. The exact order number, year of each revision and the threshold in DKK were **not verified**.
- **bips** was the industry body that produced Danish BIM guidance and the "C-krav" (IT requirements) documents. bips.dk today is hosted by **Molio** (the TLS certificate of bips.dk is issued to *.molio.dk) [15 observation].
- **Molio** is the Danish information organisation for the construction sector; **buildingSMART Danmark** is "a part of Molio" (link on Molio's site) [15].
- **CCS (Cuneco Classification System)**: Danish classification based on ISO 12006-2 and ISO 81346 (unverified); the maintenance sits with Molio (unverified).
- Molio offers a "CAD og bygningsmodel" tool section and "Beskrivelsesværktøjet 2.0" for specifications, replacing B1.000 [15].

**For testers:** Danish models are expected to carry CCS-based type/component classification and project-specific property data; use the project's own "informationskrav" as the source of truth.

## Sweden

- **BIM Alliance Sweden** is a sector-driven non-profit member organisation for digital construction and BIM [3]. **buildingSMART Sweden** is hosted by BIM Alliance and promotes IFC, bSDD, BCF and IDS; Nordic cooperation runs through **Nordic BIM Hub**, a network of Nordic buildingSMART chapters and associations [4].
- **Praxi** is BIM Alliance's web portal of guidance, templates and value lists. Version 1.0.0 (infopack dated 2025-08-29) contains ISO 19650, openBIM, **CoClass** (structuring principles) and other guidance sections; "Värdelistor" (value lists) 2.0.1 is a separate infopack [5]. IFC guidance page: `praxi.bimalliance.se/.../swe-nrb-openbim-1-0-0/1_introduktion_openbim/ifc-partial-html/` [4].
- Other BIM Alliance products: **Standardkartan** (which standards apply to a role), **BIP - Building Information Properties** (properties/designation system), **fi2xml** (Swedish property information standard, members) [3].
- **CoClass**: Swedish classification system aligned with ISO 12006-2 / ISO 81346 (unverified details); replaced BSAB 96 as the main national system (unverified).
- **Trafikverket** (Swedish Transport Administration): BIM requirements for infrastructure projects; page fetches failed, so IFC version, TDOK document numbers and start dates are **not verified**.

## Finland

- **buildingSMART Finland** describes itself as an open BIM collaboration network. Its **RYTV** programme standardises BIM for the built environment: national BIM requirements and definitions of the information to be exchanged [6].
- Publication series listed on its site [6]: **YTV** (Yleiset tietomallivaatimukset, buildings), **YIV** (infrastructure), **Inframodel** (infrastructure exchange format), **YKV** (cities), general standards, RYTV publications. These pages exist on wiki.buildingsmart.fi (title confirmed only; content unavailable).
- **COBIM 2012** ("Common BIM Requirements 2012", 13 parts, English translation of the Finnish YTV 2012) and **Senate Properties' BIM requirements (2007)** are widely cited; neither could be confirmed in this research (unverified). Senate Properties (Senaatti-kiinteistöt) is a state-owned enterprise managing state real estate, founded 1999, Helsinki [11].
- Finnish software: **Solibri** (model checking, Finnish origin; unverified) and **Tekla** (Trimble). The joint Finland and Baltic Tekla BIM Awards 2019 were won by Tripla in Pasila (source: fi.wikipedia.org/wiki/Tietomallinnus, see [14]).
- **InfraBIM** is the Finnish infrastructure BIM programme (unverified); **Inframodel** is the national LandXML-based exchange format [6].

## Iceland

buildingSMART Iceland is listed among the Nordic chapters [8]. Beyond that nothing about Icelandic BIM mandates, standards or agencies could be verified (HMS as housing/construction authority, ÍST standards via Staðlaráð Íslands: unverified).

## Estonia

- The **Digital Construction Cluster (Digitaalehituse Klaster)** was formed in 2015, co-funded by EU structural funds via Enterprise Estonia, with about EUR 600,000 for 2016-2018 [2]. Its website promotes digital construction and links to an "e-ehitus" theme site and a BIM section labelled "ÜBN" [13].
- The state building register (Ehitisregister, EHR) is online at ehr.ee (redirects to livekluster.ehr.ee) (redirect observed only). That BIM-based permit checks and a state e-construction platform exist is stated in the task brief but **not verified**. RKAS (Riigi Kinnisvara AS, state real-estate company) BIM requirements: **unverified**.

## Latvia

Nothing could be fetched or verified (bim.lv does not resolve). The task brief mentions a "BIM roadmap"; its issuer, year and content are **unverified**. Building permits go through the national construction information system BIS (Būvniecības informācijas sistēma) (unverified).

## Lithuania

- **Skaitmeninė statyba** (Digital Construction) is a non-profit coordinating digitalisation of construction (BIM adoption, training, best practice). The annual conference "Skaitmeninė statyba Lietuvoje" has run since 2012; the body is managed by 13 associations [2][12].
- The site lists: training, BIM object libraries, an annual "Lietuvos BIM projektai" competition, a 2020 webinar on free IFC viewers, a 2020 draft **National Construction Information Classifier**, a 2020 proposal for mandatory BIM in public construction, 2020-2021 amendments to laws regarding BIM, a 2019 note on tenders with BIM criteria, and a 2025 article asking whether e-construction permits will become reality [12]. These are headlines only; the legal status today is **unverified**.

## Local terminology

| Native term | Transliteration / language | English |
|---|---|---|
| bygningsinformasjonsmodellering (BIM) | Norwegian | building information modelling |
| byggherre | Norwegian/Danish/Swedish | client/owner |
| bygningsdelstabell (NS 3451) | Norwegian | table of building elements (unverified) |
| IKT-bekendtgørelsen | Danish | ICT executive order |
| tietomalli, tietomallinnus | Finnish | information model, BIM |
| Yleiset tietomallivaatimukset (YTV) | Finnish | common BIM requirements |
| Senaatti-kiinteistöt | Finnish | Senate Properties |
| digitalt samhällsbyggande | Swedish | digital built environment [3] |
| Skaitmeninė statyba | Lithuanian | digital construction [12] |
| Statinio informacinis modeliavimas (SIM) | Lithuanian | BIM (unverified) |
| Digitaalehituse klaster | Estonian | digital construction cluster [13] |
| ehitisregister | Estonian | building register |
| Būvniecības informācijas sistēma (BIS) | Latvian | construction information system (unverified) |

## Typical questions people ask about this

None of these was found as a real forum thread in this run, so all are (illustrative).

1. Which IFC version do I export for a Statsbygg project: IFC2x3 or IFC4? (illustrative)
2. Does Norway have a national BIM mandate? (illustrative; see [2])
3. What does POFIN contain and is it a standard or a framework? (illustrative; see [1])
4. Is the Danish IKT-bekendtgørelsen still in force, and what does it say about IFC? (illustrative)
5. Where do I find the current CCS codes and how do they map to IFC classification references? (illustrative)
6. What is the difference between CoClass and BSAB 96? (illustrative)
7. Which Revit parameters must map to which IFC property sets for a Swedish Trafikverket delivery? (illustrative)
8. What do YTV 2012, COBIM and the newer YTV edition differ in? (illustrative)
9. How do I georeference an IFC for a Finnish infrastructure project (Inframodel vs IFC4.3)? (illustrative)
10. Is BIM mandatory for public buildings in Lithuania? (illustrative; see [12])
11. Does Estonia accept IFC models for building permits? (illustrative)
12. Does buildingSMART Iceland publish national guidance? (illustrative)
13. How can I check an IFC against a client's IDS file? (illustrative; see [9])
14. Which MVD does a Nordic "coordination model" normally use? (illustrative)

## Common pitfalls and misconceptions

- **"The Nordics have a BIM law."** Mostly not. Requirements are client-based [2]; Denmark is the closest exception (verify).
- **COBIM vs YTV.** COBIM 2012 is the English version of Finland's earlier common requirements; newer Finnish material is branded YTV/YIV/YKV under RYTV [6]. Do not assume an English COBIM is the current rule.
- **bips vs Molio.** bips content is now hosted by Molio [15]; old bips.dk URLs may redirect or break.
- **IFC version confusion.** IFC4.3 is ISO 16739-1:2024 [7], but many Nordic client documents still require IFC2x3 or IFC4.
- **Classification varies by country** (NS 3451, CCS, CoClass, Finnish classification, Lithuanian classifier). A model valid in Norway will not carry Danish codes automatically.
- **Native names.** Sweden "BIM Alliance" hosts buildingSMART Sweden; there is no separate legal chapter body [4].

## Gaps

- WebSearch could not be run (budget exhausted); no real practitioner questions were collected.
- Failed or content-less fetches: statsbygg.no pages (title only), DiBK, Trafikverket, vayla.fi, buildingsmart.org chapters/IFC pages (403), buildingSMART Denmark (connection refused), wiki.buildingsmart.fi (title only), mkm.ee, ibim.is, bim.lv, nordicbimhub.org, coclass domain.
- Not verified at all: Statsbygg/SIMBA/SBM details, Nye Veier and Bane NOR requirements, IKT-bekendtgørelsen details, Trafikverket, COBIM 2012, Senate 2007, Estonian BIM permit checks and RKAS, Latvia roadmap, Iceland.
- No suspicious or pirated sites were encountered.

## Sources

1. https://www.buildingsmart.no/
2. https://en.wikipedia.org/wiki/Building_information_modeling
3. https://www.bimalliance.se/
4. https://www.bimalliance.se/tjanster-produkter/buildingsmart-sweden/
5. https://praxi.bimalliance.se/
6. https://www.buildingsmart.fi/ (links to https://wiki.buildingsmart.fi/fi/04_Julkaisut_ja_Standardit/YTV and .../YIV)
7. https://en.wikipedia.org/wiki/Industry_Foundation_Classes
8. https://en.wikipedia.org/wiki/BuildingSMART
9. https://github.com/buildingSMART
10. https://en.wikipedia.org/wiki/Statsbygg
11. https://en.wikipedia.org/wiki/Senate_Properties
12. https://www.skaitmeninestatyba.lt/
13. https://www.digitaalehitus.ee/
14. https://no.wikipedia.org/wiki/Bygningsinformasjonsmodellering (also https://fi.wikipedia.org/wiki/Tietomallinnus for the Tekla awards)
15. https://www.molio.dk/
