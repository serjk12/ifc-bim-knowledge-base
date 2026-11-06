# COBie, FM handover and asset data from IFC (CAFM import)

Cell: t-cobie-fm · Languages: English (real records), one Dutch; synthetic prompts in en, ru, zh, de, es, pt, fr, ja, ko, it · Collected: 2026-11-06 · Records: 29 real / 16 synthetic · Communities covered: community.osarch.org, GitHub issues (IfcOpenShell, Autodesk/revit-ifc, opensourceBIM/COBie-plugins, buildingSMART, xBim, openbimrs, OpenAEC)

Important limitation: the WebSearch budget was exhausted before any search ran, so the work was done only via direct page fetches and the GitHub CLI. Nothing was found in forums.autodesk.com, forums.buildingsmart.org, Graphisoft, Stack Overflow, Reddit or non-English communities. The synthetic non-English prompts are not backed by real native-language posts.

## Top themes (ranked by frequency)
- COBie spreadsheet export from open-source tools (Bonsai/IfcOpenShell ifcfm, BIMserver plugin) failing or incomplete.
- Empty or missing COBie sheets (Systems, Components, Coordinate, PickLists) caused by missing types, containment or mappings.
- Which tool converts IFC to COBie (standalone, Python, XBIM, BIMserver).
- COBie vs the FM Handover MVD and the doubt about whether COBie spreadsheets are still the right target.
- Validating COBie / handover requirements (COBie QC, IDS, IfcTester, Xbim IDS facets).
- Missing or duplicated property sets from Revit export breaking checks (Pset_ManufacturerTypeInformation).
- Custom and empty Revit parameters not appearing in IFC (COBie fields, empty values).
- IFC2x3 vs IFC4 differences affecting COBie mapping (Pset_Warranty, IfcDate, occurrence type mapping).
- Enterprise-scale asset management from project-based IFC (GIS/database, CDE, Maximo).
- FM apps on top of as-built IFC (GlobalId stability, ERP/CMMS links, IDS at handover).
- Unit inconsistencies and sheet fidelity in COBie output.

## What people want (the goals behind the questions)
- A reliable, one-click COBie 2.4 (UK or US template) from the model, with a list of what is missing.
- To know exactly which elements fail COBie required fields before handover.
- To feed a CAFM/CMMS/ERP with spaces, equipment, systems, warranties and serials.
- To keep FM data alive across model versions (stable GlobalIds).
- To query assets across many buildings or projects, not file by file.
- Open-source alternatives with parity to commercial tools.

## How people write here
- Register: short, technical, often only a traceback or a title; maintainers answer tersely. Typical length 1-4 sentences plus attachments.
- Jargon: "COBie sheet/tab", "Type.Name", "Components", "ifcfm", "IfcFM", "MVD", "CAFM", "handover", "closeout", "foreign key".
- Misspellings: "Cobiee", "cobiee sheet", "COBIe", "PisckLists".
- Code-switching: Dutch spec with English terms (GlobalId, IDS, ERP); synthetic non-English prompts mix English terms (cobie, CAFM, ifc).
- Openers/closers: almost none; no greeting; "Any idea what's happening here?"
- Context given: tool and version, sheet names; context omitted: the IFC itself ("IFC is private").
- Tone: neutral to confused; urgency in older posts ("Urgent, Can we use...").
- Fragments: "missing Instruction, Impact, Coordinate, Issue, PickLists tabs"; "systems tab empty"; "Blank Rows inserted"; "Where can we download the compiled COBie jar".

## Local ecosystem
- buildingSMART International (IFC, IDS, MVD/FM handover): https://github.com/buildingSMART/IFC4.x-development
- IfcOpenShell / Bonsai with ifcfm (COBie 2.4 export): https://github.com/IfcOpenShell/IfcOpenShell
- Autodesk Revit IFC exporter: https://github.com/Autodesk/revit-ifc
- BIMserver COBie plugins (legacy, includes QC report): https://github.com/opensourceBIM/COBie-plugins
- XBIM toolkit (COBie export, IDS validator): https://github.com/xBimTeam/Xbim.IDS.Validator
- openbimrs (Rust IFC): https://github.com/openbimrs/ifc
- OpenAEC open-bim-platform (Dutch, NEN 2767 context): https://github.com/OpenAEC-Foundation/open-bim-platform
- OSArch community: https://community.osarch.org
- Referenced standards/programs: COBie 2.4, NBS Digital BIM Toolkit, ISO 19650, TPF-5(480) pooled fund, NEN 2767, Uniclass 2015, OmniClass.

## Notable sources
- https://community.osarch.org/discussion/726/how-to-convert-an-ifc-file-to-cobie-using-ifcopenshell-or-other-python-based-solution - IFC to COBie via Python, COBie vs MVD.
- https://community.osarch.org/discussion/449/ifc-and-input-data-for-facility-management - FM data without geometry.
- https://community.osarch.org/discussion/comment/25545 - asset management across many IFC projects.
- https://community.osarch.org/discussion/comment/30246 - COBie metres vs millimetres.
- https://community.osarch.org/discussion/3568/massing-ifc-native-platform-from-feasibility-through-turnover-built-on-ifcopenshell-that-open - COBie closeout platform.
- https://community.osarch.org/discussion/3212/aec-open-source-framework - CI export of validated IFC and COBie.
- https://github.com/IfcOpenShell/IfcOpenShell/issues/5926 - missing COBie tabs.
- https://github.com/IfcOpenShell/IfcOpenShell/issues/6068 - empty Systems tab explained.
- https://github.com/IfcOpenShell/IfcOpenShell/issues/5702 - COBie export traceback.
- https://github.com/IfcOpenShell/IfcOpenShell/issues/3901 - multi-file IfcFM export.
- https://github.com/IfcOpenShell/IfcOpenShell/issues/3978 - Revit exporter versions and property extraction.
- https://github.com/IfcOpenShell/IfcOpenShell/issues/7095 - duplicate psets break IDS.
- https://github.com/IfcOpenShell/IfcOpenShell/issues/7212 - IDS on IFC2x3 mapping.
- https://github.com/buildingSMART/IFC4.x-development/issues/698 - Pset_Warranty vs COBie.
- https://github.com/xBimTeam/Xbim.IDS.Validator/issues/11 - COBie facets for IDS.
- https://github.com/IndustryFoundationClasses/Questions/issues/15 - tools for IFC to COBie.
- https://github.com/opensourceBIM/COBie-plugins/issues/10 - curtain wall COBie export.
- https://github.com/opensourceBIM/COBie-plugins/issues/13 - blank rows in COBie.xls.
- https://github.com/Autodesk/revit-ifc/issues/963 - empty parameter values not exported.
- https://github.com/openbimrs/ifc/issues/477 - COBie export feature spec.
- https://github.com/OpenAEC-Foundation/open-bim-platform/issues/10 - FM app on as-built model (Dutch).

## Gaps
- WebSearch quota was exhausted at the start; zero search-engine queries ran. Targets not reached: forums.autodesk.com (403 on direct fetch), forums.buildingsmart.org (404/empty on tag and search), community.graphisoft.com (403), Stack Overflow (fetch blocked), Reddit, dwg.ru, csdn/cnblogs/zhihu (404 on search), qiita (irrelevant results), cad.de, Spanish/Portuguese/French/Korean/Italian communities.
- Real records are therefore almost all English and dominated by open-source GitHub/OSArch; the Revit-to-COBie, CAFM vendor (Planon, Archibus, FAMIS etc.) and national-requirement angles (UK BS 1192-4, German AIA/CAFM-Connect, Chinese 运维 standards) are under-represented.
- GitHub API rate limit hit mid-run; some repos (COBie-plugins further queries) were not fully searched.
- Records 021-029 are search-snippet or title level only (evidence "snippet").
- No suspicious sites were encountered.
- Recommend a follow-up run with search access for the native-language communities.
