# Extracting data from IFC to Excel/SQL/Power BI/graph DBs/RDF; dashboards; analytics

Cell: t-data-extraction · Languages: English (real), Japanese (1 real); synthetic in en, ru, zh, es, pt, de, fr, ja, ko, it · Collected: 2026-11-06 · Records: 36 real / 17 synthetic · Communities covered: IfcOpenShell/Bonsai GitHub issues, OSArch community, buildingSMART forums, Qiita

NOTE: the WebSearch budget was exhausted before the first search ran, so all discovery came from GitHub search (gh), forum-native search endpoints (OSArch, buildingSMART Discourse) and direct fetches. Non-English coverage is therefore thin (see Gaps).

## Top themes (ranked by frequency)
- Spreadsheet export (CSV/XLSX/ODS) of properties and quantities, and its quirks (columns, units, round trips)
- Bill of quantities / cost takeoff from IFC quantities; cross-checking against estimates
- IFC to SQL (SQLite, MySQL, ifcSQL) via Ifc2Sql patch; errors and how to open the result
- Large files and memory: treating IFC as a database, streaming, lazy loading
- COBie / FM spreadsheet export with missing tabs or empty sheets
- Locale problems: decimal separator, delimiter, newline characters in ODS/CSV
- Python (ifcopenshell) scripts that dump psets and break across Revit exporter versions
- Missing or inconsistent quantities/properties found by validation, feeding BI dashboards
- Spreadsheet-driven workflows: BCF from XLSX, GUID linking between rows and elements
- Power BI / flat tables of schema or model data
- Graph/RDF (ifcOWL, Neo4j) mostly in research, rarely in practitioner threads
- IFC to GIS formats (GeoJSON, CityGML) and georeferencing
- AI/RAG on top of IFC properties (early, Japan)
- Choosing tools for non-programmers (Solibri, BIMvision, Bonsai, CYPE)

## What people want (the goals behind the questions)
- A flat table: one row per element, one column per pset.property, with GlobalId and storey.
- Trustworthy quantities for cost and LCA, with a traceable link back to the element.
- Dashboards (Power BI) showing completeness of data per level, class or discipline.
- A queryable store for huge models without loading everything in RAM.
- Round trip: edit in Excel, re-import to IFC, keep GUIDs stable.
- FM handover spreadsheets (COBie) that match the standard.
- Reconciling model quantities with schedules and cost estimates.
- Locale-correct exports (comma decimals, semicolon delimiters).

## How people write here
- Register: technical, neutral, GitHub bug-template style (steps, versions, tracebacks); forum posts longer and more narrative.
- Length: titles often the whole question ("how to open .ifcsqlite files?"); bodies short unless a developer.
- Jargon: pset, qto, BoQ, ITO/QTO, GUID, "preserve existing", "ifc2sql", "spreadsheet import/export", COBie tabs.
- Context given: tool and version in title ("Bonsai 0.8.4", "Revit exporter 22.6"), screenshots, attachments; context omitted: IFC schema version, exact property names.
- Openers/closers: "Hi Everyone!", "thank you", "Couple of wishes".
- Emotion: mostly calm; frustration appears as complaints about missing columns or junk export fields.
- Fragments: "Wishlist item. Few tools can do this."; "I just ctrl+C into a spreadsheet"; "Today I do a workaround in Power Query".
- Code-switching: Japanese post mixes katakana tech terms (RAG, AI Ready-Data) with IFC.

## Local ecosystem
- buildingSMART International and forums: https://forums.buildingsmart.org
- IfcOpenShell / Bonsai (ifccsv, ifcpatch Ifc2Sql, IfcFM COBie, cost schedules): https://github.com/IfcOpenShell/IfcOpenShell
- OSArch community: https://community.osarch.org
- ifcOWL: https://github.com/buildingsmart-community/ifcOWL ; BimSPARQL https://github.com/BenzclyZhang/BimSPARQL
- IFC-to-Neo4j projects: https://github.com/Nobuho/IFC-Neo4j-converter, https://github.com/IFCManager/IFC_Graph_Database
- Converters: https://github.com/datadrivenconstruction/cad2data-Revit-IFC-DWG, https://github.com/chuongmep/Ifc-to-excel
- XBIM (.NET), IFC++; Solibri, BIMvision, CYPE (commercial/free viewers named in threads)
- Japan: DNP-related Qiita demo (IFC + RAG)

## Notable sources
- https://github.com/IfcOpenShell/IfcOpenShell/issues/3978 (Excel dump broken by Revit exporter version)
- https://github.com/IfcOpenShell/IfcOpenShell/issues/4920 (open .ifcsqlite)
- https://github.com/IfcOpenShell/IfcOpenShell/issues/2025 (2 GB IFC)
- https://github.com/IfcOpenShell/IfcOpenShell/issues/6227 (Ifc2Sql failing)
- https://github.com/IfcOpenShell/IfcOpenShell/issues/7762 (BoQ CSV with element linking)
- https://github.com/IfcOpenShell/IfcOpenShell/issues/4290 (decimal separator Poland)
- https://github.com/IfcOpenShell/IfcOpenShell/issues/5736 (BoQ export junk columns)
- https://github.com/IfcOpenShell/IfcOpenShell/issues/5926 (COBie tabs missing)
- https://github.com/IfcOpenShell/IfcOpenShell/issues/7116 (memory-efficient reads)
- https://github.com/IfcOpenShell/IfcOpenShell/issues/6644 (MySQL patcher)
- https://github.com/IfcOpenShell/IfcOpenShell/issues/9008 (ExtractElements differences)
- https://community.osarch.org/discussion/1535/ifc-stored-as-sqlite-and-mysql
- https://community.osarch.org/discussion/3418/free-ifc-concrete-boq-looking-for-test-files-and-honest-feedback
- https://community.osarch.org/discussion/3695/bcf-from-xlsx-file
- https://community.osarch.org/discussion/3519/exporting-ifc-file-schema
- https://community.osarch.org/discussion/comment/27265 (Quantity cross-check)
- https://community.osarch.org/discussion/comment/28482 (coordinates in spreadsheet exports)
- https://forums.buildingsmart.org/t/ifc-flat-data/4044
- https://forums.buildingsmart.org/t/which-software-to-create-lists-of-quantities-of-the-used-building-materials/5181
- https://forums.buildingsmart.org/t/ifc-for-relational-databases-ifcsql/1524
- https://forums.buildingsmart.org/t/store-modify-and-retrieve-ifc-data-with-ifcsql/1558
- https://forums.buildingsmart.org/t/help-regarding-extracting-importing-data-from-ifc-to-estimation-software/3953
- https://forums.buildingsmart.org/t/ifc-to-gis/6115
- https://qiita.com/dnp-hiraoka/items/aa1d12e5784485542583

## Gaps
- WebSearch was unavailable (budget used up), so no general-web discovery, no Reddit, no non-English search with allowed_domains.
- Blocked or unusable: stackoverflow.com and api.stackexchange.com (fetch refused), forums.autodesk.com (403), zhihu/cnblogs (human verification), forum.dwg.ru search (encoding garbled, only a pinned FAQ found), buildingSMART search hit 429 rate limit twice.
- No real Russian, Chinese, Spanish, Portuguese, German, French, Korean or Italian posts; those languages are represented only by synthetic records. Power BI, Neo4j and ifcOWL practitioner questions were found only indirectly (repos and one buildingSMART thread), not in dedicated user threads.
- Many records are developer/enthusiast heavy (Bonsai/OSArch); Revit/Dynamo/Autodesk-forum voices are missing.
- No suspicious or pirated sites were encountered.
