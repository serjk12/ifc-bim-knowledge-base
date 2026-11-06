# QA log: fact-check of 01_ifc_basics/00 to 04

Date: 2026-11-06. Scope: `01_ifc_basics/00_ifc_in_real_projects.md`, `01_what_is_ifc_and_versions.md`, `02_ifc_file_anatomy.md`, `03_entities_cheat_sheet.md`, `04_spatial_structure_and_relationships.md`.

Method: direct page fetches (WebFetch) of primary sources: URA circulars, EVS catalogue, Autodesk help and revit-ifc GitHub, Graphisoft help, Tekla help, Bricsys, NIBS, the buildingSMART IFC4.3.x-development GitHub markdown (raw), buildingSMART forum, Wikipedia (for dates only). Nothing was downloaded or executed; web text was treated as data. The shared web-search quota ran out partway through, so the last checks relied on direct fetches only.

## 1. Corrections made (errors fixed in place)

| # | File | Was | Now | Evidence |
|---|---|---|---|---|
| 1 | 00 (4.4, 1) | CORENET X mandatory for **all** new projects from 1 Oct 2026 (circular dc25-01) | From 1 Oct 2026 mandatory for new projects with GFA **>= 5,000 m2**; below that voluntary; ongoing projects may stay in CORENET 2. Plan revised by circular **dc26-08, 23 July 2026**; dc25-01 marked superseded | URA dc26-08 page (read) |
| 2 | 00 (3) | ISO 29481-1 "(framework)" | ISO 29481-1 = methodology and format; CEN/TR 17741:2021 guides EN ISO 29481-1 IDMs | CEN/TR 17741 catalogue entry (genorma) |
| 3 | 00 (4.5) | COBie v3 "announced in 2022" | NIBS lists COBie V3.0 as part of NBIMS-US V4 in 2023 | nibs.org/cobie |
| 4 | 00 (9), 02, sources | revit-ifc #521 described as "room GUIDs change" with title unknown | Title and outcome added: opened Oct 2022, closed as completed 5 Sep 2023, 22.6.x exporter confirmed stable | GitHub issue #521 |
| 5 | 00/01 | Nordic BIM IFC 4.3 page "undated" and "no software certified when written" | Page dated 11 May 2026: no software currently certified; Nordic BIM IDS article dated 8 July 2026 | Nordic BIM pages |
| 6 | 01 (2) | IAI renamed "1996 or 1997", chapters "roughly 30" | Sept 1995 opened as Industry Alliance for Interoperability; May 1996 International Alliance for Interoperability; 2005 buildingSMART; about 38 distinct chapters listed | Wikipedia buildingSMART |
| 7 | 01 (6) | Revit release notes "25.3.40 / 25.4.40 / 26.4.1" | **24.3.40** / 25.4.40 / 26.4.1 ("Added IFC4.3 Reference View exchange requirements"); added built-in setups seen in the 26.4.1 help and 27.x release context | revit-ifc releases page, exporter help 26.4.1 |
| 8 | 01 (6) | Tekla export "carries buildingSMART certification for IFC2x3 and IFC4 model views" | Tekla 2026 help calls only IFC2x3 Coordination view 2.0 "certified"; views per version listed (Precast = IFC4 only, Bridge = IFC4.3 only) | Tekla 2026 help |
| 9 | 01 (3.1, 3.2) | IFC5: JSON "IFCX" repository warns derivatives and production use prohibited | README does not use "IFCX"; says schema to be published on ifcx.dev; examples preliminary, educational/testing only, asks not to create derivatives | IFC5-development README |
| 10 | 01 (3.2) | EN ISO 16739-1:2020 "seen only as a catalogue title" | EVS: published 2 Mar 2020, **withdrawn 15 Apr 2024**, replaced by EN ISO 16739-1:2024 | evs.ee |
| 11 | 01 (4) | "Alignment-based View (AbV)" stated as confirmed official MVD | Forum says "two official ones for 4.3" without naming; names kept but flagged as not re-read | buildingSMART forum, 6 Nov 2024 |
| 12 | 02 (2) | Part 21 implementation level "first digit version, second conformance class" | First number refers to the 1995 technical corrigendum; second = conformance option (1 = internal mapping of complex entities); header entities FILE_POPULATION / SECTION_LANGUAGE / SECTION_CONTEXT are 2nd-edition only | Wikipedia ISO 10303-21 |
| 13 | 02 (6, 7) | IfcText length limit and OwnerHistory optionality "via search excerpt" | Verified on IFC4.3.x-development: 32767 octets; "attribute has been changed to be OPTIONAL" | GitHub IfcText.md, IfcRoot.md |
| 14 | 03 (3.1) | IfcWallStandardCase "Deprecated from IFC4 ADD2 TC1 on" | Reworded: deprecation timing unverified; the dev markdown has no deprecation note; ElementedCase is "Deprecated" in IFC4 ADD2 TC1 docs; wall enum STANDARD/POLYGONAL deprecated in IFC4 | GitHub IfcWallStandardCase.md, IfcWallTypeEnum.md, forum thread |
| 15 | 03 (3.1) | Several PredefinedType lists marked "(unverified)" or truncated | Full 4.3 lists written and verified for Window, Door, Plate, Beam (adds GIRDER_SEGMENT, DIAPHRAGM, PIERCAP, HATSTONE, CORNICE, EDGEBEAM), Column (adds PIERSTEM, PIERSTEM_SEGMENT, STANDCOLUMN), Stair (adds LADDER and the full turn list), Ramp, Railing (adds FENCE), Pile, ShadingDevice, BuildingElementPart, ReinforcingBar (adds SPACEBAR) | GitHub enumeration markdown |
| 16 | 03 (3.3, 3.6, 5) | `IfcFacilityPart` "4.3; replaces IfcBridgePart" | Introduced in IFC4.2 per release notes; 4.3 notes: IfcBridgePart now covered by IfcFacilityPart via SELECT | IFC-Release-Notes.md |
| 17 | 03 (3.6) | `IfcLinearPlacement`, `IfcSectionedSolidHorizontal`, `IfcAlignment` implied 4.3 | Release notes place linear placement, sectioned solid horizontal and alignment in IFC4.1; 4.3 adds `IfcLinearPlacementWithInclination`, `IfcSectionedSurface` | IFC-Release-Notes.md |
| 18 | 03 (1) | Release-note counts presented as final 4.3 | Counts are labelled "IFC4.3 RC1" in the notes; per-domain split added | IFC-Release-Notes.md |
| 19 | 04 (1.1) | In IFC4.3 `IfcBuildingStorey` "a subtype of IfcFacilityPart"; referencing targets "IfcFacilityPart subtypes (IfcBuildingStorey, IfcSpace)" | Softened: 4.3 docs say "IfcFacilityPart, or more specifically IfcBuildingStorey or IfcSpace"; EXPRESS supertype in 4.3 unconfirmed (earlier schemas: IfcSpatialStructureElement) | GitHub IfcRelReferencedInSpatialStructure.md, IfcSpace.md |
| 20 | 04 (2.4) | "Split Walls, Columns, Ducts by Level" / "Export rooms in 3D views" described loosely | Exact labels and tabs recorded; exporter 26.4.1 help words the first one "Split walls and columns by Level"; Building Story quote added | Revit 2024 help, exporter help 26.4.1 |

## 2. Claims verified without change (key items)

- IFC version dates: IFC 1.0 June 1996, 1.5 Nov 1997, 1.5.1 Sept 1998, 2.0 March 1999, IFC2x3 Feb 2006, IFC4 March 2013, Add1 2015, Add2 2016, Add2 TC1 2017, IFC4.2 April 2019 (Wikipedia). 
- IFC 4.3: approval announced 4 Jan 2024 (New Year message says 3 Jan), publication announced 2 Apr 2024, database row 4.3.2.0 / IFC 4.3 ADD2 / ISO 16739-1:2024 / 2024-04 / Official (search results).
- IDS 1.0: approved 1 June 2024, press release 4 June 2024, XSD, >200 people from 34 countries (search result summaries of buildingSMART pages).
- Revit export labels and tabs: "Export base quantities" (Property Sets), GUID-in-parameter option, "Export only elements visible in view" (Additional Content), space boundaries None / 1st / 2nd level, coordinate base options; IFC4 Reference View "certified (IFC4 RV 1.2)", DTV unofficial/experimental (exporter help 26.4.1, issue #629 maintainer statements); `ExportBaseQuantities` API wording; revit-ifc LGPLv2, fixes for current plus two previous Revit versions, Navisworks reader work.
- revit-ifc issue #629 (opened 21 Apr 2023, closed 18 Apr 2025) and #1013 (opened 14 Oct 2026, open, not reproduced in Revit 2027).
- Autodesk Docs naming standard: seven fields, Status/Revision/Classification metadata, hyphen/underscore/point delimiters; status code table S0-S7, A1/An, B1/Bn, CR (Archive not on that page).
- Archicad help: "supports the import and export of IFC2x3, IFC4, and IFC4.3"; Reference View mainly one-directional; DTV "not meant for round-trip"; Coordination View 2.0 certified import and export; IFC4 "not supported by all applications"; type mapping behaviour (Element Type vs Classification, USERDEFINED, greyed-out PT). ifcXML 300-400% larger than .ifc; ifcZIP 60-80% / 90-95% smaller (AC30 help).
- BricsCAD "IFC4 Architectural Reference Exchange Export Certification" 28 Jan 2025; Inventor 2026 IFC 4x3 in two workflows; Archicad 28+ IDS import (Nordic BIM article).
- Habr article (17 Feb 2025) uses SPb GAU CGE published IDS with ifcopenshell/ifctester.
- IfcBuiltElement renamed from IfcBuildingElement and made non-abstract in 4.3.0.0; IfcBuildingElementProxy: "change", not formal deprecation, advice to use IfcBuiltElement / IfcVirtualElement; IfcWallTypeEnum, IfcSpaceTypeEnum (incl. BERTH), IfcDuctFittingTypeEnum values.
- IfcRelContainedInSpatialStructure (single container, lift-shaft example), IfcRelDefinesByProperties (type psets via HasPropertySets), IfcRelServicesBuildings deprecated in 4.3.0.0, IfcBuilding.ElevationOfRefHeight and IfcBuildingStorey.Elevation deprecated, Pset_BuildingStoreyCommon properties, IfcSpatialElement inverse attributes.
- IFC4 attribute counts in the hand-written example (IfcProject 9, IfcSite 14, IfcBuilding 12, IfcBuildingStorey 10, IfcWall 9), GlobalId format (22 chars, IFC alphabet, first char 0-3) for all 12 example ids, and `\X2\` code points (computed locally).
- OSArch wiki statements on `IfcSpatialContainer`, one site/one building, ZoneName-based IfcZone, space Name/LongName defaults.

## 3. Residual uncertainty (marked "(unverified)" or flagged in the files)

- Moscow ЦИМ АГР IFC requirement from 2 April 2026: RBC page HTTP 401; no official source reachable.
- Spain BIM Plan (June 2023) and Finland 2007 IFC requirement: EU PDF text not extractable; Medium blog is secondary.
- ГОСТ Р 10.0.02-2019 entry-into-force date: catalogue page timed out twice.
- IFC 4.3 certification status after May 2026; buildingSMART certified list and BCF/IFC specification database pages returned HTTP 403.
- IfcWallStandardCase deprecation version; EXPRESS supertype of IfcBuildingStorey in 4.3.
- Revit menu path "File > Export > IFC" not stated on the fetched help pages; Archicad "File > Interoperability > IFC" likewise.
- IfcOpenShell geometry-support statement (PyPI page failed), Bentley statements, IFC4.1 date, IFC4.4 status, IFC2x3 TC1 date (2007-07), ISO/TC 59/SC 13 (ISO pages 403).
- BCF versions "2.1 and 3.0": BCF-XML README mentions only a `release_3_0` branch; creators (Tekla, Solibri) not confirmed on a primary page.
- Enumeration lists for pipe segment/fitting, furniture, bearing, transport element and MEP equipment remain "(unverified)".

## 4. Gaps and skipped sources

- Pages returning HTTP 403 (not read): iso.org, technical.buildingsmart.org, standards.buildingsmart.org (IFC4.3 HTML), buildingsmart.org (BCF, IDS, certified software), www1.bca.gov.sg FAQ returned 404.
- No suspicious, pirated or "free download" sites were encountered or linked. One tool call returned a PDF (EU executive summary) that the fetch tool saved locally; it was not opened or executed. Mirror/aggregator pages (wiki mirrors, Stack Overflow mirrors cited in the original doc 02) were left as originally labelled "mirror, via search excerpt" and not extended.
- No personal data of forum posters was recorded; forum summaries refer to roles only.

## 5. New sources added to the docs

- URA/BCA circular dc26-08: https://www.ura.gov.sg/guidelines/circulars/dc26-08/
- revit-ifc releases: https://github.com/Autodesk/revit-ifc/releases
- Revit 2024 help, IFC Export Setup Options: https://help.autodesk.com/cloudhelp/2024/ENU/Revit-DocumentPresent/files/GUID-E029E3AD-1639-4446-A935-C9796BC34C95.htm
- Wikipedia ISO 10303-21 and buildingSMART forum "IFC Schema Identifier" (doc 02 sources 42, 43)
- IFC4.3.x-development enumeration markdown (doc 03 source 30)
