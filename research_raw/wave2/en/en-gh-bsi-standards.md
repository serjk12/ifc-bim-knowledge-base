# buildingSMART GitHub: IFC4.3 docs, IDS, bSDD, BCF issues (implementer questions)
Cell: en-gh-bsi-standards · Languages: English · Collected: 2026-11-06 · Records: 50 real / 16 synthetic · Communities covered: buildingSMART GitHub issue trackers (IDS, bSDD, BCF-XML, BCF-API, IFC4.x-development which hosts IFC4.3 docs)

## Top themes (ranked by frequency)
- IDS semantics: cardinality, empty strings, null vs missing, applicability vs requirement symmetry
- IDS facet limits: no cross-entity relationships, partOf/aggregation, grouped objects not inheriting properties
- IDS data types and units: IfcLabel vs IfcText vs IfcIdentifier, measures, float tolerance
- IDS test cases and XSD defects found by tool implementers (IfcOpenShell, xbim, Bonsai, usBIM)
- bSDD API ergonomics: too many calls, no entity filter, no bulk dictionary download
- bSDD modelling of IFC: predefined and USERDEFINED types, psets vs qtos, property inheritance, units/datatypes
- BCF-XML spec ambiguity: mandatory snapshot, camera units, multiple IFC files, GUID rules, 2.1 branch known broken
- BCF-API doc vs SwaggerHub mismatches, documents API, project extensions, batch endpoints
- IFC4.3 documentation bugs: typos, empty pages, inconsistent EXPRESS vs text, broken search
- Property set and Qto proposals (door hold-open, covering length, slab Width vs thickness)
- Georeferencing and linear placement clarifications (IfcMapConversion, WorldCoordinateSystem, PlacementRelTo)
- Decomposition semantics: aggregates, openings, materials/layers, reinforcement

## What people want
- Deterministic, spec-backed answers on whether a given IFC file passes an IDS rule and why.
- IDS able to express relationships, grouped requirements, and user-defined predefined types.
- Fast, filterable, offline-capable bSDD access to find applicable properties per IFC class.
- Interoperable BCF files that third-party tools accept; unambiguous spec text.
- Standard psets/qtos for real-world gaps (fire door hardware, covering lengths) and consistent naming.
- Clarity about IFC4.3 docs vs schema vs examples; sample files.

## How people write here
Register: technical, polite, issue-template driven (Summary / Motivation / Use cases). Typical length is 3-15 lines, often with pasted IDS XML, STEP lines, JSON or screenshots. Implementers write precisely and quote spec sections; end users and vendor-support staff write more loosely and give less context.
- Jargon: applicability, requirement, facet, cardinality, PredefinedType, pset/qto, "early bound", viewpoint, topic.
- Openers: "Hi all," "Hello everyone," "I'm wondering if...". Closers: "All tips are appreciated", "Thanks in advance".
- Fragments: "Not good." / "Is it a software failure?" / "Question: Difference between ...".
- Frustration appears around API latency ("up to 5 seconds") and vendors blaming the spec.
- Typos in titles occur ("shapshot", "defintion"). Missing context: IFC version often omitted; file rarely attached.

## Local ecosystem
- buildingSMART International: https://github.com/buildingSMART (IDS, bSDD, BCF-XML, BCF-API, IFC4.3.x-development now IFC4.x-development)
- IFC 4.3 docs: https://ifc43-docs.standards.buildingsmart.org/ ; DEV docs https://standards.buildingsmart.org/IFC/DEV/IFC4_3/HTML/
- bSDD: https://search.bsdd.buildingsmart.org/ , API on SwaggerHub
- Open source: IfcOpenShell / IfcTester / Bonsai (https://github.com/IfcOpenShell/IfcOpenShell), xbim, BCFier, python-mvdxml
- Sample models: https://github.com/buildingSMART/IFC4.3.x-sample-models
- Forum: https://forums.buildingsmart.org/ (referenced, not fetched)
- Tools named: usBIM, Sortdesk, Trimble (BCF/IDS checkers)
- Note: several repos received "Archival Notice" issues dated 2026-10-23, so the trackers may be archived soon.

## Notable sources
- https://github.com/buildingSMART/IDS/issues/400 same-entity differing requirements
- https://github.com/buildingSMART/IDS/issues/403 empty string cardinality
- https://github.com/buildingSMART/IDS/issues/416 grouped objects
- https://github.com/buildingSMART/IDS/issues/418 tolerance
- https://github.com/buildingSMART/IDS/issues/430 symmetry
- https://github.com/buildingSMART/IDS/issues/447 predefined type mix
- https://github.com/buildingSMART/IDS/issues/463 graph facet
- https://github.com/buildingSMART/IDS/issues/391 material property fail
- https://github.com/buildingSMART/IDS/issues/337 datatype mismatch
- https://github.com/buildingSMART/IDS/issues/392 relationships
- https://github.com/buildingSMART/bSDD/issues/138 IfcDataType
- https://github.com/buildingSMART/bSDD/issues/131 filter properties
- https://github.com/buildingSMART/bSDD/issues/132 dictionary download
- https://github.com/buildingSMART/bSDD/issues/129 predefined types
- https://github.com/buildingSMART/bSDD/issues/77 psets vs qtos
- https://github.com/buildingSMART/BCF-XML/issues/399 snapshot mandatory
- https://github.com/buildingSMART/BCF-XML/issues/396 2.1 extension.xsd
- https://github.com/buildingSMART/BCF-XML/issues/365 type GUID in BCF
- https://github.com/buildingSMART/BCF-XML/issues/352 BCF 3.0 tools
- https://github.com/buildingSMART/BCF-API/issues/387 documents API
- https://github.com/buildingSMART/BCF-API/issues/376 project extensions
- https://github.com/buildingSMART/IFC4.x-development/issues/1089 Slab Width
- https://github.com/buildingSMART/IFC4.x-development/issues/1212 openings and coverings
- https://github.com/buildingSMART/IFC4.x-development/issues/743 WorldCoordinateSystem
- https://github.com/buildingSMART/IFC4.x-development/issues/974 PlacementRelTo
- https://github.com/buildingSMART/IFC4.x-development/issues/1002 examples as files

## Gaps
- WebSearch was unavailable (session search budget exhausted), so no forum.buildingsmart.org or non-GitHub sources were read; only gh CLI issue data was used.
- Only ~45 issue bodies were read; several records are snippet-level (title only).
- Posters are implementers and vendors; Revit end-user questions are rare here, so Revit-specific phrasing is thin.
- No suspicious sites encountered.
