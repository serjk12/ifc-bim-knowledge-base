# Custom parameters and property sets mapping (Revit/Archicad/Tekla -> IFC)
Cell: t-psets-params · Languages: English only in practice (native-language searches could not be run) · Collected: 2026-11-06 · Records: 36 real / 17 synthetic · Communities covered: GitHub Autodesk/revit-ifc issue tracker only

IMPORTANT: the WebSearch budget was exhausted before the first query ran (every search returned "budget used up"). All real records therefore come from the GitHub CLI (issues of Autodesk/revit-ifc), 36 records, about 11 read in full (evidence "page") and the rest from title/snippet. No forum, Archicad, Tekla or non-English community was reached. See Gaps.

## Top themes (ranked by frequency)
- User-defined pset txt file ("PropertySet: name I/T IfcEntity") silently not exporting certain parameters or categories (Parts, Roofs, Stairs, Railings, Rooms)
- Parameter mapping table does not override built-in values for Pset_*Common (FireRating, LoadBearing, Nominal sizes)
- Instance vs type confusion: the I/T flag, type parameter ignored for entity-level properties
- Entity name in the txt (IfcElement vs IfcRoot, predefined type filters) changing whether psets appear
- Non-English parameter names (Dutch, Czech, French, German) mapped to standard English pset properties
- Shared / hidden / project parameters not reaching the IFC; hidden params ignored
- Data type and unit problems (IfcLogical, Yes/No, length vs ratio, 304.8 scale, wrong measure type)
- Revit 2027 new Manage Default Property Sets dialog: missing parameters, missing IfcProject, undocumented property types
- Classification codes (NL-SfB, Assembly Code vs Classification Code) landing in the wrong place or duplicated psets in Solibri
- Built-in parameters (material, category, Area of rooms) not mappable to custom psets
- Request for a better exporter design (map parameters instead of iterating psets; attributes mapping)
- Checking results in Solibri / KIT viewer after export

## What people want (the goals behind the questions)
- Deliver client-required property sets (national/office standards: DIN 276, NL-SfB, project psets) without duplicating parameters
- Re-use existing Revit parameters (Mark, Comments, localized names) for standard Pset_*Common properties
- Predictable rules: which entity name, which I/T flag, which data type works
- A way to verify what actually landed in the IFC (fill rates, missing psets) and to fix it after export
- Vendor-confirmed workarounds or bug status (people quote Jira ids)

## How people write here
- Register: terse engineering English, GitHub template headings (Problem Description, Revit Version), often non-native English
- Length: 2-8 sentences, frequently with pasted txt mapping lines and screenshots
- Jargon: "UDPset", "mapping table", "Common Pset", "OOTB parameters", "Solibri check"; fragments like "Label # works", "Is it only me?", "by design?"
- Code-switching: parameter names stay in local language (Dutch brandwerendheid, Czech OBJEM/PLOCHA, German _BA_Fenster_E, French Largeur)
- Openers/closers: sometimes "Hi there", "Thanks already!"; one lowercase unpunctuated complaint ("hidden shared parameters are not exported")
- Context given: Revit version, add-in version, schema (IFC2x3 CV2 / IFC4), test file; omitted: the exact txt contents, or the viewer used
- Tone: frustrated by silent failures; confused by undocumented behavior; polite on inquiries

## Local ecosystem
- Autodesk revit-ifc exporter (open source): https://github.com/Autodesk/revit-ifc
- Autodesk Jira ids quoted by maintainers (e.g. REVIT-248491) show internal tracking
- buildingSMART IFC property set definitions (Pset_WallCommon, Pset_BuildingStoreyCommon etc.)
- Viewers used to check results: Solibri, KIT Model Viewer
- Regional hints: Dutch (NL-SfB), German (DIN 276, DIN EN 13501), Czech, French users in the same tracker
- Dynamo mentioned as workaround; IfcOpenShell relevant for post-export fixes (not searched)

## Notable sources
- https://github.com/Autodesk/revit-ifc/issues/960 category not exportable in UDPset
- https://github.com/Autodesk/revit-ifc/issues/971 Revit 2027 IfcProject missing for UDPset
- https://github.com/Autodesk/revit-ifc/issues/984 Revit 2027 Manage Property dialog
- https://github.com/Autodesk/revit-ifc/issues/989 shared params replaced by built-in same-name
- https://github.com/Autodesk/revit-ifc/issues/879 IFCElement vs IFCRoot
- https://github.com/Autodesk/revit-ifc/issues/752 predefined type filtering
- https://github.com/Autodesk/revit-ifc/issues/662 Parts not exporting UDPsets
- https://github.com/Autodesk/revit-ifc/issues/159 custom properties IfcWindow
- https://github.com/Autodesk/revit-ifc/issues/855 room area to custom pset
- https://github.com/Autodesk/revit-ifc/issues/252 double psets in Solibri
- https://github.com/Autodesk/revit-ifc/issues/205 mapping for all entity attributes
- https://github.com/Autodesk/revit-ifc/issues/206 meaning of I and T flag
- https://github.com/Autodesk/revit-ifc/issues/303 mapping one of two parameters
- https://github.com/Autodesk/revit-ifc/issues/735 localized parameters to Common psets
- https://github.com/Autodesk/revit-ifc/issues/833 LoadBearing overwrite
- https://github.com/Autodesk/revit-ifc/issues/889 duct/pipe nominal sizes
- https://github.com/Autodesk/revit-ifc/issues/858 mapping table in IFC2X3
- https://github.com/Autodesk/revit-ifc/issues/38 hidden shared parameters
- https://github.com/Autodesk/revit-ifc/issues/199 PanelWidth type
- https://github.com/Autodesk/revit-ifc/issues/791 exporter design critique
- https://github.com/Autodesk/revit-ifc/issues/1020 Yes/No AboveGround IfcLogical
- https://github.com/Autodesk/revit-ifc/issues/766 material parameters

## Gaps
- WebSearch unavailable (budget exhausted), so no forums.autodesk.com, community.osarch.org, forums.buildingsmart.org, community.graphisoft.com, StackOverflow, Reddit, dwg.ru, csdn, cnblogs, zhihu, cad.de, qiita or Spanish/Portuguese/French/Italian/Korean communities were reached.
- No Archicad or Tekla content; only Revit exporter issues.
- Several real records are title-only (evidence "snippet").
- Non-English synthetic prompts (ru, de, zh, es) are original and not grounded in native-language sources.
- No suspicious sites encountered. A follow-up run with search access is needed for all non-English and non-Revit coverage.
