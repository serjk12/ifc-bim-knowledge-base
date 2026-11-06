# buildingSMART forums and standards discussions (implementers and users)
Cell: en-buildingsmart-forums · Languages: English · Collected: 2026-11-06 · Records: 59 real / 17 synthetic · Communities covered: forums.buildingsmart.org (Discourse, read through its own JSON endpoints), GitHub buildingSMART/IDS, IFC4.x-development (the IFC4.3.x-development repo name now redirects there), BCF-XML, IFC5-development, IDS-Audit-tool

## Top themes (ranked by frequency, 8-15 bullets, one line each)
- IDS authoring and semantics: facets, applicability, PredefinedType, cardinality, data types, federated models, validating IDS files.
- Georeferencing: IfcMapConversion, IfcProjectedCRS, WorldCoordinateSystem, IfcSite lat/long, true north, wrongly written map conversions.
- Psets and properties: custom psets, uniqueness of pset names, table/bounded values, Qto expectations, applicability of a property to a predefined type.
- IfcBuildingElementProxy: what it means, how to detect the real class, schema rules (Name, ObjectPlacement).
- Validation errors: IfcCheckingTool, ifcopenshell.validate, Validation Service rule codes, WHERE rules, cardinality of inverse attributes.
- Spatial structure and relationships: Aggregates vs Nests vs ContainedInSpatialStructure, IfcSpatialZone vs IfcSpace, voids in spatial elements.
- Class choice for odd objects (culvert, clearance volume, composite electrical devices, curtain wall vs wall, rebar).
- Infrastructure/IFC 4.3: alignment, linear placement, road/bridge parts, WBS, US bridge exchange standards.
- MVD/Reference View limits and certification (material layers excluded, speed not a criterion, IFC2x3 IAs).
- Interop and parsing: Revit/ODA export quirks, STEP serialisation of selects, viewer crashes, downgrade 4.3 to 4/2x3.
- Developer tooling: IfcOpenShell, xBIM, BIMserver, Speckle, "which library to start with".
- Data extraction to DB, estimation, IoT; geometry weight and file size.
- BCF 2.1/3.0 ambiguities (snapshots, camera origin with several IFC files).
- IFC5/ifcx early feedback (modularisation, predefined types, composition bugs).

## What people want (the goals behind the questions)
- Unambiguous, machine-checkable requirements (IDS) that give the same result in every tool.
- A single obviously correct IFC class/relationship for a real-world object, and a rule for when the schema allows something.
- Georeferencing that reads and writes consistently across CAD, GIS and viewers.
- To read model data into their own system or database without writing a converter per CAD vendor.
- Clear explanations of validator messages, and confirmation that a received file is really invalid.
- Contractual clarity: what MVD/view to demand, what data a vendor must fill (EIR/IDS).
- Tools: which library/viewer/validator to use first.

## How people write here (register, typical length, jargon/slang with translations, misspellings of terms, code-switching, openers/closers, what context they give or omit, emotional tone) with short illustrative fragments (max 12 words each)
- Register: technical, polite, often non-native English (Europe, India, Asia); openers like "Hello everyone" or "Dear IFC developers"; thanks as closer.
- Length: forum posts are long with numbered sub-questions; GitHub issues are structured (Summary / Motivation); IDS questions are short.
- Jargon: "proxy" (IfcBuildingElementProxy), "Pset", "Qto", "RV/CV" (Reference View / Coordination View), "MVD", "IA" (implementation agreement), "facet", "applicability", "TIA", "IMHO", "WR1" (where rule).
- They paste raw STEP lines and validator output instead of describing. Fragment: "#1000= IFCBUILDINGELEMENTPROXY(...) validator always complains".
- Confession of level: "I am new in the IFC world", "I don't have any technical knowledge".
- Opinion framing: "IMHO", "we (the BIM industry) have a problem".
- Entity names are often typed in lowercase/uppercase STEP style (IFCWALL, IFCRELAGGREGATES) and sometimes misspelled/plural ("IfcBuildingElementProxies").
- Context often omitted: file, authoring tool version and IFC schema version; people ask "is this valid?" without attaching the model.
- Emotion: mostly neutral/curious; frustration with vendors ignoring map conversion or crashing viewers; skepticism towards MVD and certification.

## Local ecosystem (official/government bodies, regulations and standards, local software, enthusiasts/educators, open-source projects encountered, with URLs)
- buildingSMART International technical site: https://technical.buildingsmart.org ; forum https://forums.buildingsmart.org
- Standards docs: IFC 4.3.2 https://ifc43-docs.standards.buildingsmart.org ; IDS https://github.com/buildingSMART/IDS ; BCF https://github.com/buildingSMART/BCF-XML ; IFC5 https://github.com/buildingSMART/IFC5-development
- Validation Service: https://validate.buildingsmart.org ; IDS Audit tool https://github.com/buildingSMART/IDS-Audit-tool
- bSDD (dictionary): https://search.bsdd.buildingsmart.org
- Open source: IfcOpenShell/Bonsai (formerly BlenderBIM) https://ifcopenshell.org ; xBIM https://github.com/xBimTeam ; BIMserver https://github.com/opensourceBIM/BIMserver ; Speckle ; IFC++
- Commercial tools named: Solibri, usBIM, BIMcollab, Sortdesk, BIMQ, Allplan, Archicad, Revit, Civil 3D, Navisworks
- Standards bodies: ISO 16739, ISO 19650, ISO 7817 (CEN/TC 442), AASHTO/ACI/AISC (US bridge standards), buildingSMART USA, Spain, Austria chapters
- People/educators visible: IfcOpenShell maintainers and core buildingSMART technical staff answer most threads (names not recorded).

## Notable sources (15-30 best URLs, one line each)
- https://forums.buildingsmart.org/t/5695 IfcMapConversion written wrongly by software
- https://forums.buildingsmart.org/t/6331 empty/NIL IfcMapConversion in 4.3
- https://forums.buildingsmart.org/t/4976 how real-world placement is stored
- https://forums.buildingsmart.org/t/5130 what is a proxy
- https://forums.buildingsmart.org/t/5951 proxy Name rule WR1
- https://forums.buildingsmart.org/t/5260 proxy placement and validator
- https://forums.buildingsmart.org/t/4272 decomposition vs nesting
- https://forums.buildingsmart.org/t/4372 IfcCheckingTool PlacesObject
- https://forums.buildingsmart.org/t/5049 duplicate pset names
- https://forums.buildingsmart.org/t/5521 IfcRelDefinesByProperties with sets
- https://forums.buildingsmart.org/t/5993 validating IDS files
- https://forums.buildingsmart.org/t/6234 IDS applicability for all elements
- https://forums.buildingsmart.org/t/5760 IDS PredefinedType requirement
- https://forums.buildingsmart.org/t/5740 IDS table value data types
- https://forums.buildingsmart.org/t/4199 IDS vs IDM/MVD
- https://forums.buildingsmart.org/t/3638 material layers missing in Reference View
- https://forums.buildingsmart.org/t/4605 Revit IFC parsing errors
- https://forums.buildingsmart.org/t/6528 spatial reservation modeling
- https://forums.buildingsmart.org/t/5239 environmental impact values
- https://forums.buildingsmart.org/t/6429 Name/Reference usage
- https://github.com/buildingSMART/IDS/issues/189 property without pset in EIRs
- https://github.com/buildingSMART/IDS/issues/337 datatype mismatch bypasses checks
- https://github.com/buildingSMART/IDS/issues/379 conditional PartOf
- https://github.com/buildingSMART/IFC4.x-development/issues/1212 openings and decomposition
- https://github.com/buildingSMART/BCF-XML/issues/399 BCF 2.1 snapshots

## Gaps (what you could not access or find; suspicious sites skipped)
- WebSearch was unavailable (the per-turn search budget was already used up), so no general web search was done and no forum search of other sites. Research relied on the forum's own JSON search endpoints (fetched by curl; read-only) and the gh CLI. Total about 30 calls, but fewer true web searches than requested.
- Only first posts and first two replies were read per topic; many answer_summary fields are condensed.
- technical.buildingsmart.org pages and GitHub discussions were not fetched; Validation-service repo was not found by gh.
- Some GitHub issue records have thin answer_summary (issue not resolved). Poster names were not recorded.
- No suspicious sites encountered.
