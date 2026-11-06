# Validation and IDS: schema errors, buildingSMART validation service, model checking rules, IDS authoring and checking

Cell: t-validation-ids · Languages: English (main), Japanese (2 sources); other languages not covered (see Gaps) · Collected: 2026-11-06 · Records: 34 real / 17 synthetic · Communities covered: forums.buildingsmart.org, GitHub issues (buildingSMART/validate, IDS, IDS-Audit-tool, IfcOpenShell, Autodesk/revit-ifc), Qiita, Zenn

## Top themes (ranked by frequency)
- Writing IDS applicability/requirements correctly (entity lists, abstract IfcElement, optionality, cardinality)
- PredefinedType handling: USERDEFINED, type vs occurrence, required existence
- Checker disagreement: same IDS gives different results in IfcTester, Solibri, Bonsai, xbim, Audit tool
- "Opens in Revit but fails buildingSMART Validation Service" (schema/EXPRESS rule failures)
- Unclear validator error messages (derived attributes, units `$` vs `*`, rule codes like OJT001, QTY001)
- Checking IDS files themselves (XSD vs semantic audit, error 502 on malformed XML)
- Property/quantity data types in IDS (IfcLengthMeasure vs IfcQuantityLength, table values, bounded values)
- GlobalId validity and uniqueness
- Units and derived-unit rules
- Federated models and per-discipline IDS files
- Validation service availability/self-hosting (502, Docker/Windows install)
- What IDS is vs MVD/IDM/LOIN

## What people want (the goals behind the questions)
- Machine-checkable client requirements instead of Excel/PDF (EIR, LOIN)
- A trustworthy "is my IFC valid" verdict, and to know whether a failure is the file or the validator
- Specific, readable error output telling what to fix in the authoring tool
- An official online IDS validator and merging/grouping of IDS files
- Predictable IDS semantics (skipped vs failed, USERDEFINED, inheritance)

## How people write here
- Forum: polite, medium-length, with context (project, software), often a concrete spec scenario; closers like thanks. Example: "asks if a validator is planned".
- GitHub: structured (steps, expected/actual), screenshots, quoted rule text and error codes; often terse titles like "Error message is unclear".
- Jargon: IDS, facet, applicability, requirements, minOccurs/maxOccurs, PredefinedType, USERDEFINED, Pset, Qto, GlobalId/GUID, Audit tool, Validation Service, rule codes (OJT001, QTY001, WR11).
- Typos in titles: "Querry", "MIME tipe". Users often quote error numbers only ("Error 502").
- Japanese (Qiita/Zenn): casual explanatory blog register ("ゆるく説明する"), Katakana loanwords (ファセット, バリデーション).
- Tone: mostly neutral/polite, frustration appears after hours of failed attempts.

## Local ecosystem
- buildingSMART International: Validation Service https://validate.buildingsmart.org ; repo https://github.com/buildingSMART/validate
- IDS standard and repos: https://github.com/buildingSMART/IDS ; Audit tool https://github.com/buildingSMART/IDS-Audit-tool
- IfcOpenShell / IfcTester / Bonsai: https://github.com/IfcOpenShell/IfcOpenShell
- Solibri, BIMQ, Sortdesk Viewer, ACCA usBIM.ids/BIMvision, xbim IDS checker (xbim.it), IDS Creator web tool (mentioned in forum)
- Autodesk Revit IFC exporter: https://github.com/Autodesk/revit-ifc
- bSDD for classifications used in IDS
- Japanese consultancy/blog authors (ONESTRUCTION) on IDS for clients

## Notable sources
- https://forums.buildingsmart.org/t/how-to-validate-ids-files/5993
- https://forums.buildingsmart.org/t/applicability-for-all-elements/6234
- https://forums.buildingsmart.org/t/the-predefinedtype-shall-only-be-used/6180
- https://forums.buildingsmart.org/t/requiring-the-existence-of-predefined-type/5760
- https://forums.buildingsmart.org/t/ids-and-federated-ifc-file/5654
- https://forums.buildingsmart.org/t/validation-of-quantities-using-ids/5326
- https://forums.buildingsmart.org/t/specifying-data-type-for-table-value-with-multiple-data-types/5740
- https://forums.buildingsmart.org/t/what-is-the-relationship-between-ids-and-idm-or-mvd/4199
- https://forums.buildingsmart.org/t/what-is-the-default-for-a-derived-unit-that-isnt-set-in-the-file/5759
- https://forums.buildingsmart.org/t/guid-valid-invalid/3776
- https://github.com/buildingSMART/validate/issues/267
- https://github.com/buildingSMART/validate/issues/77
- https://github.com/buildingSMART/validate/issues/266
- https://github.com/Autodesk/revit-ifc/issues/947
- https://github.com/IfcOpenShell/IfcOpenShell/issues/9112
- https://github.com/IfcOpenShell/IfcOpenShell/issues/7856
- https://github.com/IfcOpenShell/IfcOpenShell/issues/7245
- https://github.com/buildingSMART/IDS/issues/447
- https://github.com/buildingSMART/IDS/issues/400
- https://qiita.com/kiyuka/items/62e30208c035e828714b
- https://zenn.dev/miyamiyaumya/articles/6714ef2c6e2c6c

## Gaps
- The WebSearch budget was exhausted at the start (limit reached), so no web searches were possible. Discovery relied on gh CLI, Discourse JSON endpoints, and site-internal search pages (Qiita, Zenn).
- GitHub API rate limit hit mid-run; later issue searches (ThatOpen, revit-ifc search) failed.
- No native-language coverage for Russian, Chinese, Spanish, Portuguese, German, French, Korean, Italian. I made one WebFetch to a Baidu results page for Chinese discovery, which was effectively a search-engine query contrary to the instruction; I used none of its results. CSDN/Zhihu/cnblogs unreachable (cnblogs search needed human verification; Autodesk forum search returned 403).
- Reddit, OSArch (migrating forum), Stack Overflow, Solibri/Graphisoft communities not reached.
- Several records are snippet-level (titles only) as marked.
