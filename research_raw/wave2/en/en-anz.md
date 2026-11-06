# Australia and New Zealand: IFC practice questions (NATSPEC, TfNSW DE, state requirements)

Cell: en-anz · Languages: English · Collected: 2026-11-06 · Records: 27 real / 16 synthetic · Communities covered: OSArch forum (AU/NZ posters), GitHub (IfcOpenShell, Autodesk/revit-ifc), buildingSMART Australasia (XChange programmes), NATSPEC BIM portal, BIMinNZ, ABAB

NOTE: the web-search budget ran out after the first calls, so this cell was built from direct page fetches and GitHub CLI only. Real records are thinner on genuine user questions than usual; about 10 are conference/official pages (marked official_doc).

## Top themes (ranked by frequency)
- Georeferencing: GDA2020 / MGA zone CRS, IfcMapConversion scale, true vs grid north from Revit.
- IDS authoring and checking as the way clients (TMR, TfNSW) verify IFC deliveries.
- Civil/infra IFC 4.3: alignments from 12d, survey data, rail existing conditions.
- Proxy elements and reclassifying to correct IFC classes.
- Local regulation mapped to IFC: NSW BASIX, NZ Building Code stairs/ramps.
- Type vs instance inheritance of attributes and psets (Tag, Name).
- CSV/spreadsheet round trips of IFC properties and quantities (encoding, BaseQuantities).
- Process guidance vs IFC: NATSPEC Guide and NZ Handbook are ISO 19650 based and do not mandate IFC.
- Owners (Kainga Ora, airports) asking what IFC means for asset portfolios.
- Contractor QA of IFC (OpenBIM Pledge) and MCP/AI validation.
- Local content libraries (AU vs NZ furniture and product sizes).

## What people want (the goals behind the questions)
- Deliver IFC that passes client IDS/validation first time (TMR Queensland, TfNSW).
- Correct coordinates in IFC from Revit and civil tools (MGA/GDA2020).
- Automate compliance inputs (BASIX) and cost/carbon estimating from IFC.
- Fix classification and proxy problems quickly, increasingly with AI help.
- Understand what to write in EIR/AIR so consultants deliver usable openBIM.
- Open formats for long-lived asset data (owners).

## How people write here
- Register: casual, short, practical; forum posts often have no question mark and no greeting.
- Length: 1-3 sentences, or a numbered list of observations in bug reports ("1. Project units are in mm").
- Jargon: proxies ("reclass the proxies"), "press export", "grid north" (map CRS north in AU usage), MGA56, GDA2020, BASIX, TMR, TfNSW, DE (Digital Engineering), EIR/AIR, "openBIM".
- Spelling: Commonwealth English (metres, colour, programme); "Kainga Ora", "Bonsai/BlenderBIM".
- Code-switching: none; but mixes software names (12D, Revit, Solibri, Bonsai).
- Context given: file attached, CRS code, software version; often omitted: schema version and exporter settings.
- Tone: neutral to mildly frustrated; owners are vague and exploratory.
- Fragments: "Not sure what I'm doing wrong here"; "reclassify proxies"; "Here in Australia we call it Grid North".

## Local ecosystem
- NATSPEC BIM Portal and National BIM Guide (2022): https://bim.natspec.org/ ; Guide: https://bim.natspec.org/documents/natspec-national-bim-guide ; Open BIM Object Standard and Properties Generator.
- ABAB (Australasian BIM Advisory Board): https://www.abab.net.au/ (AIR Guide, process consistency report).
- buildingSMART Australasia: https://www.buildingsmart.org.au/ ; XChange conferences ( https://www.buildingsmart.org.au/xchange2026 ).
- Queensland TMR (Transport and Main Roads) openBIM delivery with IFC/IDS/IDM; Transport for NSW digital engineering and IFC-based cost/carbon work; Victorian DE program (all via XChange programmes).
- NZ: BIMinNZ https://www.biminnz.co.nz/ and NZ BIM Handbook; Kainga Ora; Auckland Airport.
- Software: 12d Model, Revit, Vectorworks, Graphisoft, Solibri, Bonsai/IfcOpenShell (open source, active Sydney meetups).
- Regulation: NSW BASIX, NZ Building Code stairs/ramps, AS ISO 19650.

## Notable sources
- https://community.osarch.org/discussion/comment/25227 - IDS and type inheritance, AU steward idea
- https://community.osarch.org/discussion/comment/8942 - Kainga Ora asking what IFC means
- https://community.osarch.org/discussion/comment/30019 - AI-built IFC reclass tool, NZ
- https://community.osarch.org/discussion/comment/29640 - NZ stair class rules vs Bonsai tools
- https://community.osarch.org/discussion/comment/28324 - Sydney open-source meetup
- https://community.osarch.org/discussion/comment/24558 - OpenBIM Pledge
- https://community.osarch.org/discussion/comment/9157 - IFC CSV round trip
- https://community.osarch.org/discussion/comment/13420 - AU vs NZ furniture sizes
- https://github.com/IfcOpenShell/IfcOpenShell/issues/6421 - BASIX validation error
- https://github.com/IfcOpenShell/IfcOpenShell/issues/5072 - 12d alignment IFC
- https://github.com/Autodesk/revit-ifc/issues/465 - grid vs true north
- https://github.com/Autodesk/revit-ifc/issues/784 - MGA56 map conversion scale
- https://www.buildingsmart.org.au/xchange2026 - 2026 programme
- https://www.buildingsmart.org.au/xchange2025 - 2025 programme (TfNSW, BASIX, Auckland)
- https://www.buildingsmart.org.au/what-we-do - IFC/IDS alignment in Queensland transport
- https://bim.natspec.org/documents/natspec-national-bim-guide - National BIM Guide
- https://www.biminnz.co.nz/nz-bim-handbook - NZ BIM Handbook
- https://www.abab.net.au/ - ABAB guides

## Gaps
- Web search was unavailable (budget exhausted) so reddit, LinkedIn, Autodesk and Graphisoft forums, and TfNSW/TMR pages were not reached; transport.nsw.gov.au and tmr.qld.gov.au returned 403 and nsw.gov.au 403.
- TfNSW Digital Engineering Framework IFC clauses and NATSPEC IFC-specific rules were not read directly.
- About 40 percent of real records are official/conference pages, not user questions; genuine user questions from AU/NZ are mostly from OSArch and GitHub.
- No suspicious sites were encountered; nothing was downloaded.
