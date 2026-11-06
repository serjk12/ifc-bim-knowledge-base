# Text encoding and non-Latin characters in IFC (Cyrillic, Chinese, Japanese, Arabic garbled), special characters, decimal separators

Cell: t-encoding · Languages: en (dominant), plus ru, zh, ja, ko, ar, el, tr, de, fr, pt, cs, da content/synthetic · Collected: 2026-11-06 · Records: 31 real / 16 synthetic · Communities covered: GitHub issues only (IfcOpenShell/Bonsai, ThatOpen web-ifc, xBIM Essentials, Autodesk revit-ifc, FreeCAD)

Important limitation: the web search budget was exhausted before any search ran, so no forum, Q&A or native-language community was reached. All real records come from GitHub issues read via the gh CLI. See Gaps.

## Top themes (ranked by frequency)
- Parser strictness: one malformed or raw non-ASCII string makes a reader drop an entity, a later string or the whole file (xBIM, web-ifc, IfcOpenShell).
- Raw (unescaped) non-ASCII bytes written by exporters instead of \X\ / \X2\ escapes (SolidWorks Cyrillic, ArchiStation Latin-1, FreeCAD STEP).
- Wrong or mixed escape flavours: \X\ (ISO 8859-1) vs \X2\ (UTF-16), MacRoman bytes, lowercase hex, nested \X\ inside \X2\.
- Invalid backslashes (Windows paths in FILE_NAME header, doubled backslash before \X2\).
- Control characters (form feed, newline, \X\1F) in names/properties breaking XML output or geometry loading.
- Writers (web-ifc export) corrupting escapes, dropping the following character.
- Conversion tools failing on non-ASCII in header or file names (IfcConvert to XML/OBJ/DAE).
- Locale effects in Revit: German UI import class mapping file ANSI vs UTF-8.
- Exporter change visibility: users surprised that accents are now \X\E9 instead of \X2\00E9\X0\.
- Non-Latin text breaking UI dropdowns (Blender enum limitation affecting Japanese material names, umlauts).
- Decimal separator: requests to accept comma as decimal input (numpad), numbers stored as text.
- Users asking what the correct encoding is for generating IFC with Chinese text.

## What people want (the goals behind the questions)
- Names, property sets and addresses in their own language to survive export and re-import unchanged.
- Files to open in any viewer; tolerant readers that skip one bad string instead of failing.
- To know which tool is at fault (exporter, file, or viewer) and whether the file is valid.
- A simple rule: how to write Unicode correctly when generating IFC programmatically.
- Locale-friendly input (comma decimals) in authoring tools.

## How people write here
Register: terse, technical, issue-template style; non-native English is common (Chinese, Czech, Danish, Portuguese reporters). Typical length 2-8 lines plus a pasted raw IFC line.
- Quote the failing STEP line verbatim, e.g. `\X2\7d20586b571f\X0\` and `\X\E6`.
- Tool-name jargon: "messy code", "garbled", "eats the next character".
- Chinese/Japanese in other languages: 乱码 (luanma), 文字化け (mojibake), Russian кракозябры (seed terms, not yet observed in real posts).
- Short opener-less posts: "which Chinese encoding do you use?" Closers: "Thank you!".
- Context usually given: tool version, OS, a zipped sample; often omitted: IFC schema, the exporting settings.
- Tone mostly neutral to frustrated; politeness markers in non-native posts.

## Local ecosystem
- buildingSMART string encoding guidance (cited in issues, page not fetchable): https://technical.buildingsmart.org/resources/ifcimplementationguidance/string-encoding/
- ISO 10303-21 Part 21 spec text cited by users: https://www.steptools.com/stds/step/IS_final_p21e3.html#clause-6-4-3
- Open source: IfcOpenShell/Bonsai https://github.com/IfcOpenShell/IfcOpenShell ; web-ifc https://github.com/ThatOpen/engine_web-ifc ; xBIM https://github.com/xBimTeam/XbimEssentials ; Revit IFC exporter https://github.com/Autodesk/revit-ifc ; FreeCAD https://github.com/FreeCAD/FreeCAD
- Viewers named: Solibri, BimVision, BIMcollab, eveBIM, XbimXplorer. Authoring tools named: Revit, ArchiCAD, SolidWorks (SwIFC), ArchiStation, SimpleBIM.
- Not reached: national bodies, local software, native-language communities.

## Notable sources
- https://github.com/IfcOpenShell/IfcOpenShell/issues/571 - Chinese encoding in IFC generation
- https://github.com/IfcOpenShell/IfcOpenShell/issues/3182 - SolidWorks raw Cyrillic read error
- https://github.com/IfcOpenShell/IfcOpenShell/issues/7305 - raw Latin-1 bytes from ArchiStation, Bonsai
- https://github.com/IfcOpenShell/IfcOpenShell/issues/1016 - accents in header, IfcConvert
- https://github.com/IfcOpenShell/IfcOpenShell/issues/1501 - nested \X\ in \X2\
- https://github.com/IfcOpenShell/IfcOpenShell/issues/2043 - XML not well-formed from control char
- https://github.com/IfcOpenShell/IfcOpenShell/issues/3499 - Cyrillic/Chinese truncation in ifcXML
- https://github.com/IfcOpenShell/IfcOpenShell/issues/8262 - decimal comma input
- https://github.com/IfcOpenShell/IfcOpenShell/issues/6496 - Japanese material names in Bonsai
- https://github.com/IfcOpenShell/IfcOpenShell/issues/101 - Turkish letters in style name
- https://github.com/ThatOpen/engine_web-ifc/issues/949 - lowercase hex in \X2\ (Chinese)
- https://github.com/ThatOpen/engine_web-ifc/issues/468 - MacRoman in ArchiCAD files
- https://github.com/ThatOpen/engine_web-ifc/issues/1559 - malformed escape breaks whole file
- https://github.com/ThatOpen/engine_web-ifc/issues/440 - Czech export corrupted
- https://github.com/ThatOpen/engine_web-ifc/issues/358 - Danish \X\E6
- https://github.com/xBimTeam/XbimEssentials/issues/605 - Japanese text, doubled backslash
- https://github.com/xBimTeam/XbimEssentials/issues/512 - \S\ in wall name kills geometry
- https://github.com/xBimTeam/XbimEssentials/issues/561 - backslash in header FILE_NAME
- https://github.com/Autodesk/revit-ifc/issues/7 - German import class mapping encoding
- https://github.com/Autodesk/revit-ifc/issues/441 - exporter now writes \X\E9
- https://github.com/Autodesk/revit-ifc/issues/686 - Chinese address and lat/long in Revit export
- https://github.com/FreeCAD/FreeCAD/issues/33914 - STEP exports raw CJK characters

## Gaps
- WebSearch returned "budget used up" for every query, so none of the seed searches (кракозябры, 乱码, 文字化け, etc.) or the target communities (dwg.ru, csdn, qiita, forums.autodesk.com, OSArch, buildingSMART forum, Stack Overflow, Reddit, cad.de, Korean/Arabic/Greek/Turkish sites) were queried. Real non-English phrasing is therefore missing; the non-English synthetic prompts are based on my own knowledge of typical phrasing, not observed posts.
- technical.buildingsmart.org returned 403 to WebFetch.
- Revit-side user complaints (Autodesk forum "IFC export garbled", Russian/Chinese forum threads) and decimal separator/locale posts in Revit were not covered.
- Several records have lang set to the poster's likely native language inferred from content; the posts themselves are in English except one Portuguese issue.
- No suspicious sites encountered.
