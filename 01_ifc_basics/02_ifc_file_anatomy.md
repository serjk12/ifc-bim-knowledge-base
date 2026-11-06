# Inside an .ifc file: STEP/SPF, header, entity instances, encodings, ifcXML/ifcZIP/ifcJSON

## In plain words

An `.ifc` file is just a plain-text file. Every line in its DATA section is one "object" or "fact" about the building, numbered with a local number like `#12`, written in a very old but simple format called STEP Part 21 (ISO 10303-21). The top of the file (the header) says which IFC version the file uses and, often, which "exchange scenario" (MVD) it was made for. Strings with non-Latin letters (Cyrillic, Chinese, German umlauts) are not stored as raw letters but as escape codes such as `\X2\0421...\X0\`, which is why a text editor shows "garbage" even though the file is fine. The same data can also be stored as XML (ifcXML), zipped (ifcZIP), JSON (ifcJSON, not yet an official release) or RDF (ifcOWL). For an MCP tester: the `#12` number is only valid inside one file and changes on every export; the 22-character GlobalId is the identity that is meant to be stable.

Last researched: 2026-11-06 (fact-checked 2026-11-06, see `_meta/qa/qa-basics-1.md`)

> Research note. Most buildingSMART pages (technical.buildingsmart.org, standards.buildingsmart.org) returned HTTP 403 to the fetch tool, so facts from them were taken from search-result excerpts and are marked "(via search excerpt)". The web-search budget ran out before the "tools" and "real questions" topics were fully covered; see "Gaps".

---

## 1. The big picture: layers of the IFC "stack"

| Layer | What it is | Example |
|---|---|---|
| Data model (schema) | EXPRESS language definition of all entities | `IFC2X3`, `IFC4`, `IFC4X3_ADD2` |
| Exchange structure / encoding | How instances are written to a file | STEP Part 21 `.ifc`, XML `.ifcXML`, JSON, RDF |
| Packaging | Compression wrapper | `.ifcZIP` |
| Exchange scenario (MVD) | Which subset of the schema a file is meant to contain | Coordination View 2.0, Reference View |

Version/ISO mapping (Wikipedia [13], buildingSMART specification database via search excerpt [24]): IFC2x3 (Feb 2006); IFC4 (March 2013); IFC4 ADD2 TC1 (2017, ISO 16739-1:2018); IFC 4.3 ADD2, i.e. version 4.3.2.0 (2024, ISO 16739-1:2024). IFC4.1 and IFC4.2 are listed as withdrawn [13]. The official 4.3.x development repository is on GitHub [15].

---

## 2. ISO 10303-21 (STEP Part 21): the file skeleton

The STEP physical file ("SPF", the classic `.ifc`) is defined by ISO 10303-21, "Clear text encoding of the exchange structure" [1]. Editions: 1st 1994, 2nd 2002, 3rd 2016 (adds ZIP-based packaging, anchors/references/signatures and UTF-8) [1]. IFC files in practice still follow the older, ASCII-only conventions (see section 6).

```
ISO-10303-21;                      <- magic first line
HEADER;
FILE_DESCRIPTION(...);             <- description list + implementation level
FILE_NAME(...);                    <- file name, time, author, org, tools
FILE_SCHEMA(('IFC4'));             <- which EXPRESS schema the DATA obeys
ENDSEC;
DATA;
#1=IFCPROJECT(...);                <- instances
#2=IFCSITE(...);
...
ENDSEC;
END-ISO-10303-21;                  <- closing line
```

Facts from [1]:
- The HEADER has a fixed order. The first edition defines FILE_DESCRIPTION, FILE_NAME, FILE_SCHEMA; the second adds optional FILE_POPULATION, SECTION_LANGUAGE, SECTION_CONTEXT (IFC files use the first three).
- `FILE_DESCRIPTION(description_list, implementation_level)`: implementation level is typically `'2;1'`; per Wikipedia (QA-checked) the first number is the version ("2" refers to the 1995 technical corrigendum) and the second is the conformance option ("1" = internal mapping of complex entity instances, the more compact form). FILE_POPULATION, SECTION_LANGUAGE and SECTION_CONTEXT are valid only in second-edition files.
- `FILE_NAME(name, time_stamp, author_list, organization_list, preprocessor_version, originating_system, authorization)`; time stamp is ISO 8601.
- `FILE_SCHEMA` names the governing EXPRESS schema(s).

Real header from an IfcOpenShell documentation sample (the KIT "AC20-FZK-Haus" house, IFC4) [2]:

```
ISO-10303-21;
HEADER;FILE_DESCRIPTION(('ViewDefinition [, QuantityTakeOffAddOnView, SpaceBoundary2ndLevelAddOnView]'),'2;1');
FILE_NAME('AC20-FZK-Haus.ifc','2016-12-21T17:54:06',('Architect'),(''),'','','');
FILE_SCHEMA(('IFC4'));
ENDSEC;

DATA;
```

Practical points (general STEP knowledge unless cited):
- Whitespace and line breaks are not significant: one instance may span many lines, or a whole file may be on one line. Grepping for `FILE_SCHEMA` works only if the writer used line breaks (the buildingSMART forum thread says so about `grep -m 1`) [18].
- Comments `/* ... */` are legal in Part 21 (unverified for every parser; strip them in test files to be safe).
- Every statement ends with `;`. Keywords are upper case in IFC files; the schema is case-insensitive in principle but tools write upper case.

---

## 3. Instance lines: `#12=IFCWALL(...);`

Syntax [1][2]:

```
#66= IFCPROJECT('0lY6P5Ur90TAQnnnI6wtnb',#12,'Projekt-FZK-Haus',$,$,$,$,(#2,#3),#4);
 ^id   ^entity     ^attribute 1 (GlobalId) ^attr 2 = reference to #12 (OwnerHistory) ...
```

- `#n` is a positive integer unique only inside that file. It is an exporter-assigned line label, not an identity. Re-export, re-save in another tool or even a different export option can renumber everything. Never store `#n` as a persistent key (use GlobalId).
- Attributes are positional, in the order the EXPRESS schema declares them, supertype attributes first. That is why you cannot read an `IFCWALL(...)` line without the schema (IfcWall has 9 attributes in IFC4: GlobalId, OwnerHistory, Name, Description, ObjectType, ObjectPlacement, Representation, Tag, PredefinedType).
- References to other instances are `#id`; forward references (to a later line) are allowed.
- Lists/aggregates are parenthesised: `(#2,#3)`; nested: `((0.,0.,0.))` [2].
- Numbers: reals must contain a decimal point (`0.`, `1.5`, `1.E-05`); an integer-looking `0` where a real is expected is invalid in strict parsers [2 shows `IFCDIRECTION((1.,0.,0.))`].

### 3.1 `$`, `*`, enumerations, typed values

| Token | Meaning | Example |
|---|---|---|
| `$` | Attribute not set (null / "no value"). Different from an empty string `''`. | `IFCWALL('...',$,'Wall-001',$,...)` |
| `*` | Attribute is "derived" in this subtype: its value is computed by the schema, so the file writes an asterisk placeholder in that position [1]. | `IFCSIUNIT(*,.LENGTHUNIT.,.MILLI.,.METRE.)` [2] |
| `.NAME.` | Enumeration value, upper case between dots | `.ELEMENT.`, `.STANDARD.`, `.FLOOR.`, `.ADDED.` [2] |
| `.T.` / `.F.` | BOOLEAN true/false (IFC files conventionally use the short form; [1] shows `.TRUE.` as the long form, unverified which strict parsers accept) | `IFCBOOLEAN(.T.)` |
| `.U.` | LOGICAL "unknown" (unverified in this research; general STEP knowledge) | |
| `.NOTDEFINED.` | The conventional "no specific type" enumeration literal present in almost every IFC predefined-type enumeration | `IFCWALL(...,.NOTDEFINED.)` |
| `.USERDEFINED.` | "Custom type": by IFC rule the free-text `ObjectType` (or `ElementType`) attribute should then describe it (general IFC knowledge) | |
| `'text'` | String, single quotes; a literal apostrophe is doubled `''` | `'Wall-001'` |
| `IFCLABEL('x')` | Typed value: a SELECT type (e.g. IfcValue) needs the defined-type name wrapped around the value | `IFCLABEL('REI60')` |
| `"0A3F"` | Binary (rare in IFC) [1] | |

`$` vs `*` vs `''` vs `.NOTDEFINED.` are four different kinds of "nothing" and good sources of test cases: an MCP tool that prints `None` for all of them loses information.

---

## 4. EXPRESS basics (just enough to read the spec)

IFC is defined in EXPRESS (ISO 10303-11), a textual data-modelling language. What a tester must recognise:

- ENTITY: a class, e.g. `IfcWall`. Entities form an inheritance tree (`IfcWall` is an `IfcBuildingElement`, an `IfcElement`, an `IfcProduct`, an `IfcObject`, an `IfcRoot`). Subtypes inherit all attributes of their supertypes, which is why GlobalId (from `IfcRoot`) is the first attribute of a wall.
- Explicit attributes: the ones written in the file, in order. They may be OPTIONAL (can be `$`).
- INVERSE attributes: back-pointers computed by the reader, never written to the file. Example: `IfcWall.IsDefinedBy` (property sets), `IfcWall.ContainedInStructure` (storey), `IfcWall.HasOpenings`. In the file you only find the forward link inside a relationship entity such as `IFCRELDEFINESBYPROPERTIES` or `IFCRELCONTAINEDINSPATIALSTRUCTURE` (see example, section 8). To answer "which properties does this wall have?" a tool must find the relationship lines that mention the wall; that is exactly what IfcOpenShell's `ifcopenshell.util.element.get_psets` style helpers do.
- DERIVED attributes: calculated (the reason for `*` in subtypes).
- TYPE (defined type): a named wrapper around a basic type, e.g. `IfcLabel = STRING`, `IfcLengthMeasure = REAL`, `IfcGloballyUniqueId = STRING(22) FIXED` (the 22-character rule is in the schema, see section 5). Defined types are why values sometimes appear as `IFCLABEL('x')`.
- SELECT type: a union, e.g. `IfcValue` can be any measure type; in the file the chosen member's name is written (`IFCLABEL(...)`, `IFCLENGTHMEASURE(...)`, `IFCBOOLEAN(...)`).
- ENUMERATION type: fixed list of literals, e.g. `IfcWallTypeEnum` (`MOVABLE, PARAPET, PARTITIONING, PLUMBINGWALL, SHEAR, SOLIDWALL, STANDARD, POLYGONAL, ELEMENTEDWALL, RETAININGWALL, WAVEWALL, NOTDEFINED, USERDEFINED`; list from IFC4.x, unverified for each version).
- Rules: `WHERE` clauses and global rules, checked by validators, not by parsers.

The schema is distributed as EXPRESS (`.exp`), XSD (for ifcXML), and for IFC4 also OWL/Turtle (ifcOWL) [24].

---

## 5. GlobalId: the 22-character compressed GUID

- Every `IfcRoot` subtype (walls, spaces, property sets, relationships, the project...) has a `GlobalId` of type `IfcGloballyUniqueId`: a string of exactly 22 characters [6] (via search excerpt).
- It is a 128-bit GUID compressed into base-64 with IFC's own alphabet: `0-9`, `A-Z`, `a-z`, `_`, `$` (in this order) [7][8]. This is not RFC 4648 base64 (no `+` and `/`, different order); decoding it with a standard base64 decoder silently gives wrong bytes [7].
- 22 x 6 = 132 bits, so the first character carries only the 2 high bits and must be `0`-`3` [7][6]. A GlobalId starting with `4`...`z` is invalid. Example endpoints: all-zero GUID = `0000000000000000000000`; all-ones = `3$$$$$$$$$$$$$$$$$$$$$` [7].
- History: IFC R1.5.1 used a 20-character base-85 scheme; IFC 2x switched to base-64 to avoid clashing with special characters in STEP and XML [5] (via search excerpt). buildingSMART says compression would be considered unnecessary today, but it is retained for backward compatibility [5].
- Conversion (IfcOpenShell `ifcopenshell.guid`): `compress(hex_uuid)`, `expand(ifc_guid)`, `new()` = random UUID4 compressed [8].
- Persistence is the whole point: GlobalId should stay the same for "the same" element across versions. In Revit this depends on the exporter: by default IFC GUIDs derive from Revit element identifiers (per the Revit IFC code owner, via search excerpt [21]) and the option "Store the IFC GUID in an element parameter after export" writes the GUID into an `IfcGUID` parameter that later exports reuse [16][20]. Reports exist of GUIDs changing between exports of the same file [21][28][29].
- Case matters: `aBc` and `ABC` are different IDs (alphabet has both cases).
- Duplicates: GlobalIds must be unique within a project; copy-paste in some tools or merging two files can create duplicates (general knowledge; validators report it).

---

## 6. String encoding, `\X2\...\X0\`, and why Notepad "garbles" Cyrillic and Chinese

Rule: the classic STEP physical file only allows printable characters 32-126 from the ISO 8859-1 code table; every other character must be escaped [4] (via search excerpt). Current IFC documentation says allowed characters come from ISO 10646 (Unicode), and that `IfcText` is "not formally restricted in length" but a string in an ISO 10303-21 file must not exceed 32767 octets after encoding and escaping (QA-verified on the IFC4.3.x-development `IfcText` page) [30b].

Control directives (ISO 10303-21 / -11; described in the IFC2x Model Implementation Guide [26], plus the buildingSMART string-encoding page [4]):

| Escape | Meaning | Example |
|---|---|---|
| `\X2\` hhhh hhhh `\X0\` | One or more 16-bit Unicode code points (4 hex digits each, big-endian UTF-16, BMP) until `\X0\` switches back to plain ASCII | `\X2\00C4\X0\` = Ä [4] |
| `\X4\` hhhhhhhh `\X0\` | 32-bit code points (outside the BMP: emoji, rare CJK) [26] | |
| `\X\hh` | One ISO 8859-1 character by 2 hex digits | `\X\E4` = ä |
| `\S\c` | ISO 8859-1 character: code of `c` plus 128 (older style) | `\S\d` = ä |
| `''` | Apostrophe inside a string | |

(`\X\` and `\S\` examples computed from the ISO 8859-1 table; the existence of all three decoders `\X`, `\X2\` and `\S\` is confirmed by a Python-decoder answer title found in search [23].)

Worked examples (checked by computation):

| Text | In the file |
|---|---|
| Стена (Russian "wall") | `'\X2\042104420435043D0430\X0\'` (С=0421, т=0442, е=0435, н=043D, а=0430) |
| 墙 (Chinese "wall") | `'\X2\5899\X0\'` |
| Ä | `'\X2\00C4\X0\'` |
| Rus. "Рабочий проект" | each letter becomes a 4-hex group; spaces can be written plain between `\X0\` and the next `\X2\` |

Why "garbled in Notepad":
1. Normal case, not a bug. Notepad (and any editor) does not decode STEP escapes; it shows the raw `\X2\0420043504310440043E\X0\` text. The file is correct; a STEP-aware reader (IfcOpenShell, any viewer) decodes it. Decode by hand: split into 4-hex groups, treat as big-endian UTF-16 [23][22]. Autodesk forum answer: every 4 characters between `\X2\` and `\X0\` are one Unicode code point [22].
2. Real mojibake, a bug in the writer. Some exporters/converters write raw bytes (UTF-8 or Windows-1251 / GBK) straight into strings instead of escaping. An editor guessing the wrong code page then shows things like `РЎС‚РµРЅР°`. It may be unreadable in other tools too, and strict parsers may fail. A text editor encoding switch (e.g. Notepad++ Encoding menu) can reveal this; converting already garbled text does not repair it [Notepad++ community report via search, not linked].
3. Edition 3 of Part 21 allows UTF-8 [1]; buildingSMART says IFC will move to UTF-8 in future and older files are not UTF-8 [4] (via search excerpt). Do not assume UTF-8 today.

Testing implication: an MCP tool that returns `\X2\...\X0\` to the user has failed to decode; one that writes a Cyrillic name must escape it (or write valid UTF-8 only where the target schema/tool allows). Test names with Cyrillic, Chinese, apostrophes (`O'Brien`), backslashes and very long strings.

---

## 7. OwnerHistory

`IfcOwnerHistory` records who created/modified an object and with which application. IFC attribute list (8 attributes): OwningUser (IfcPersonAndOrganization), OwningApplication (IfcApplication), State, ChangeAction, LastModifiedDate, LastModifyingUser, LastModifyingApplication, CreationDate (an integer: seconds since 1970-01-01).

Real example [2]:

```
#12= IFCOWNERHISTORY(#7,#11,$,.ADDED.,$,$,$,1482339244);
```

- In IFC2x3 `IfcRoot.OwnerHistory` is mandatory; since IFC4 it is OPTIONAL: the IFC4.3 `IfcRoot` page says "The attribute has been changed to be OPTIONAL" (QA-verified) [27]. Hence minimal IFC4 files can write `$` there; IFC2x3 files must carry one, and tools that write IFC2x3 and leave it null produce invalid files.
- Many IFC4 files still contain OwnerHistory (the FZK-Haus IFC4 sample does [2]) because exporters kept the pattern.
- Revit writes a single shared OwnerHistory for most objects (general knowledge): it does not give a reliable per-element audit trail. Do not use it for "who edited this wall" questions.

---

## 8. Tiny annotated IFC4 example (project > site > building > storey > wall + property set)

Hand-written for this knowledge base, using the IFC4 attribute order from the schema. GlobalIds were generated with the compression algorithm in section 5 (illustrative values, not from a real model). It has not been run through the buildingSMART validation service in this research (unverified). QA 2026-11-06: attribute counts of every instance were checked by hand against the IFC4 definitions (IfcProject 9, IfcSite 14, IfcBuilding 12, IfcBuildingStorey 10, IfcWall 9, IfcRelAggregates 6, IfcPropertySet 5), all 12 GlobalIds were checked locally to be 22 characters from the IFC alphabet with a first character in `0`-`3`, and the `\X2\` code points (С=0421 ... а=0430, 墙=5899, Ä=00C4) were recomputed. Remove the `/* */` comments if a strict parser complains. It deliberately omits OwnerHistory (`$`, allowed in IFC4, see section 7).

```
ISO-10303-21;
HEADER;
FILE_DESCRIPTION(('ViewDefinition [ReferenceView]'),'2;1');
FILE_NAME('tiny_wall.ifc','2026-11-06T10:00:00',('Tester'),('QA'),'hand-written','hand-written','');
FILE_SCHEMA(('IFC4'));
ENDSEC;
DATA;
/* --- units and geometric context --- */
#10=IFCSIUNIT(*,.LENGTHUNIT.,.MILLI.,.METRE.);
#11=IFCUNITASSIGNMENT((#10));
#22=IFCCARTESIANPOINT((0.,0.,0.));
#21=IFCAXIS2PLACEMENT3D(#22,$,$);
#20=IFCGEOMETRICREPRESENTATIONCONTEXT($,'Model',3,1.E-05,#21,$);

/* --- spatial structure: Project > Site > Building > Storey --- */
#1=IFCPROJECT('1b4oSE9fuDD$AdJUHIvhGu',$,'Demo Project',$,$,$,$,(#20),#11);
#2=IFCSITE('3IFmWa4eilCmnSVz2cewHG',$,'Demo Site',$,$,#30,$,$,.ELEMENT.,$,$,$,$,$);
#3=IFCBUILDING('2LCPXTNPt9_1WOw169Bv0h',$,'Demo Building',$,$,#31,$,$,.ELEMENT.,$,$,$);
#4=IFCBUILDINGSTOREY('0szdNCWUTEzUZYNPGEsGHr',$,'Level 1',$,$,#32,$,$,.ELEMENT.,0.);
#30=IFCLOCALPLACEMENT($,#21);
#31=IFCLOCALPLACEMENT(#30,#21);
#32=IFCLOCALPLACEMENT(#31,#21);

/* --- the wall: GlobalId, OwnerHistory=$, Name, Description (Cyrillic "Стена"), ObjectType=$,
       ObjectPlacement, Representation, Tag=$, PredefinedType --- */
#5=IFCWALL('1h3LIRRmDdMXO0ere9cL3O',$,'Wall-001','\X2\042104420435043D0430\X0\',$,#33,#40,$,.STANDARD.);
#33=IFCLOCALPLACEMENT(#32,#21);

/* --- wall geometry: 5000 x 200 footprint extruded 3000 up (mm) --- */
#40=IFCPRODUCTDEFINITIONSHAPE($,$,(#41));
#41=IFCSHAPEREPRESENTATION(#20,'Body','SweptSolid',(#42));
#42=IFCEXTRUDEDAREASOLID(#43,#45,#46,3000.);
#43=IFCRECTANGLEPROFILEDEF(.AREA.,'Wall 5000x200',#44,5000.,200.);
#44=IFCAXIS2PLACEMENT2D(#47,$);
#47=IFCCARTESIANPOINT((2500.,100.));
#45=IFCAXIS2PLACEMENT3D(#22,$,$);
#46=IFCDIRECTION((0.,0.,1.));

/* --- relationships: these are separate instances, not attributes of the wall --- */
#50=IFCRELAGGREGATES('2D4MxE5pZtsJsS5oGHuWkF',$,$,$,#1,(#2));
#51=IFCRELAGGREGATES('2GmPBFqwoKhmyXtRPihKec',$,$,$,#2,(#3));
#52=IFCRELAGGREGATES('2XSBCuEIOmMVAC45qViNmZ',$,$,$,#3,(#4));
#53=IFCRELCONTAINEDINSPATIALSTRUCTURE('0FrZ3nyfqDgPK$IF6WdtQr',$,$,$,(#5),#4);

/* --- property set Pset_WallCommon attached to the wall --- */
#60=IFCPROPERTYSINGLEVALUE('FireRating',$,IFCLABEL('REI60'),$);
#61=IFCPROPERTYSINGLEVALUE('IsExternal',$,IFCBOOLEAN(.T.),$);
#62=IFCPROPERTYSET('0CiUASPOpQ59Nc2lMJlGJF',$,'Pset_WallCommon',$,(#60,#61));
#63=IFCRELDEFINESBYPROPERTIES('2EWPS_2_pNi3YOqP3vwzhC',$,$,$,(#5),#62);
ENDSEC;
END-ISO-10303-21;
```

Reading guide:
- `#1`..`#4`: the spatial tree. The hierarchy is not nested in the file; it is built by the three `IFCRELAGGREGATES` lines (`#50-#52`).
- `#53` puts the wall in the storey (`IfcRelContainedInSpatialStructure`). The inverse attribute `IfcWall.ContainedInStructure` is computed from this line.
- `#63` connects wall and property set; the inverse `IfcWall.IsDefinedBy` is computed from it. The property values live in `#60`/`#61`, wrapped in typed values `IFCLABEL`/`IFCBOOLEAN` (SELECT `IfcValue`).
- `*` in `#10`, `$` for all unset attributes, `.STANDARD.`/`.ELEMENT.`/`.AREA.` as enumerations, `.T.` as boolean.
- `\X2\042104420435043D0430\X0\` decodes to "Стена".
- Line numbers need not be consecutive or in dependency order.

---

## 9. How to tell version and MVD from the header

Schema (`FILE_SCHEMA`) = the data model version. Typical values:

| FILE_SCHEMA value | Meaning |
|---|---|
| `IFC2X3` | IFC2x3 (TC1 is still `IFC2X3`) |
| `IFC4` | IFC4 and its addenda (ADD1, ADD2, ADD2 TC1 all identify as `IFC4`; general knowledge, unverified here) |
| `IFC4X3` / `IFC4X3_ADD2` | IFC 4.3 / IFC 4.3.2.0 (Revit 2026.4 writes `IFC4X3_ADD2` for IFC4x3 exports [9]; exact-match checks miss variants [18]) |
| `IFC2X_FINAL`, `IFC2X2_...` | Old; Tekla states `IFC2X_FINAL` is unsupported and tells users to re-export as IFC2X3 or IFC4 [19] |

`FILE_DESCRIPTION` first argument carries the MVD ("Model View Definition", the exchange scenario the exporter claims to follow):

| Header text seen in the wild | Meaning |
|---|---|
| `ViewDefinition [CoordinationView]` | IFC2x3/IFC4 ADD2 sample style (buildingSMART IFC4 ADD2 annex sample, via search excerpt) |
| `ViewDefinition [CoordinationView_V2.0]` | IFC2x3 Coordination View 2.0 (community files, via search excerpt) |
| `ViewDefinition [ReferenceView_V1.0]` | IFC4 Reference View (community files, via search excerpt; exact suffix varies by exporter, unverified) |
| `ViewDefinition [DesignTransferView...]` | IFC4 Design Transfer View (suffix unverified) |
| `ViewDefinition [, QuantityTakeOffAddOnView, SpaceBoundary2ndLevelAddOnView]` | empty base view plus add-ons [2] |

MVD facts from Graphisoft [11]: IFC4 splits the Coordination View into the Reference View (mostly one-way, reference models) and the Design Transfer View (supports editing of connected elements, not meant for round trips); "the IFC4 Schema is not supported by all applications". Revit's export dialog offers: IFC 2x3 Coordination View 2.0, IFC 2x3 Coordination View, IFC 2x2 Coordination View, IFC 2x3 GSA Concept Design BIM 2010, IFC 4 Reference View, IFC 4 Design Transfer View [16]. Revit file types: IFC, IFC XML, Zipped IFC, Zipped IFC XML [16]; Revit opens `.ifc`, `.ifcXML`, `.ifcZIP` [17]. Menu path: Revit 2025 and later: File > Export > IFC > Modify Setup (via search excerpt of an Autodesk support article [17]; QA could not confirm the path on the Revit 2024/2026 help pages, which only describe the setup options - unverified; earlier versions use "Export > Options > IFC Options": unverified). Option labels confirmed in QA (Revit 2024 help): "Export base quantities" (Property Sets tab), "Store the IFC GUID in an element parameter after export", "Split Walls, Columns, Ducts by Level" (General tab), "Export only elements visible in view" and "Export rooms in 3D views" (Additional Content tab), Space boundaries None / 1st level / 2nd level (General tab), coordinate base options Shared Coordinates / Survey Point / Project Base Point / Internal Origin / Project Base Point oriented in True North / Internal Origin oriented in True North [41].

Caveat: the header is a claim by the exporter, not proof. In Revit 2026.4 with the IFC4x3 Reference View option, the header wrongly said `CoordinationView` (schema `IFC4X3_ADD2`); Autodesk reproduced it in 2026.4, not in 2027, and warned that hand-editing the line does not make the file conform [9]. (revit-ifc issue #1013 was opened on 14 Oct 2026 and answered on 16 Oct 2026; still open when checked on 2026-11-06, no decision yet on a 2026.x fix.) Likewise, a file labelled `IFC2X3` can contain an IFC4-only entity [18-related fixture, via search excerpt].

---

## 10. Other file formats

| Format | Extension | Based on | Status / notes |
|---|---|---|---|
| IFC-SPF | `.ifc` | ISO 10303-21 | Most widely used; buildingSMART recommends it for file-based exchange (widest compatibility, smallest size) [3][13] |
| ifcXML | `.ifcXML` | ISO 10303-28, XSD from the EXPRESS schema | Official but rare because of file size [13][3]. Graphisoft: normally 300-400% larger than `.ifc` [12]. Used when the partner's tools need XML [12] |
| ifcZIP | `.ifcZIP` (often `.ifczip`) | ZIP container holding one SPF or XML model | Graphisoft: shrinks `.ifc` by about 60-80%, `.ifcXML` by 90-95% (vendor figures) [12]. Any ZIP tool can unpack it [12]. Text-editor version checks need unzipping first [18] |
| ifcJSON | `.json`/`.ifcJSON` | JSON mapping of EXPRESS | buildingSMART community repo "ifcJSON-4", described as in sync with the EXPRESS schema, still under development, no formal release listed at capture time [14]; the README (QA-read) says the initial standard is being developed against IFC4, specifically IFC4.3. Listed in the "provisional/candidate" tier on buildingSMART's formats page (via search excerpt) [3]. ODA's IFC SDK offers only experimental read support [30]. Wikipedia mentions ifcJSON v4 and v5 work in 2020 [13] |
| HDF5 | `.ifcHDF` | HDF5, relating to ISO 10303-26 | Hierarchical binary storage for fast access; listed as official on the formats page (via search excerpt) [3]; ODA IFC SDK reads and writes HDF5 [30]. Rare in practice (general knowledge) |
| ifcOWL / RDF / Turtle | `.ttl`, `.rdf` | OWL ontology generated from EXPRESS | buildingSMART Linked Data WG documented ifcOWL as a standard in 2017 [25]; RDF/TTL files are listed for IFC 2x3 and IFC4 ADD2 TC1 in the specification database (via search excerpt) [24]. Whether official ifcOWL exists for IFC 4.3.2 was not confirmed (unverified). Research-oriented, rarely used in production (secondary source, low confidence) |
| IFC5 / "IFCX" | `.ifcx` (extension from community material, unverified) | JSON-based | Next-generation work, separate from 4.x; the buildingSMART IFC5-development README (QA-read) calls its files "alpha examples" and says the JSON schema will be published on ifcx.dev; it does not use the word "IFCX" or the `.ifcx` extension itself. Do not rely on this row beyond "experimental" |

Important for MCP testing: schema-level semantics are the same across SPF/XML/JSON; but file size, parser speed and tool support are very different. An MCP server that "supports IFC" almost always means SPF (+ often ifcZIP); asking it to open `.ifcXML` or `.ifcJSON` is a legitimate edge-case test.

---

## 11. Tools to inspect and open files

Verified in this research:
- Any text editor (VS Code, Notepad++, Notepad) for the header and for reading lines; large files need a pager or `grep` [18].
- IfcOpenShell (Python): `ifcopenshell.open(path)`, `model.schema`, `model.by_type("IfcSlab")` [2]; `ifcopenshell.guid` module for GlobalId conversion [8].
- Revit: imports and exports the formats above [16][17]. Archicad: supports `.ifc`, `.ifcXML`, `.ifcZIP` [12].

General knowledge, not re-verified in this session (treat as unverified): Bonsai (formerly BlenderBIM) and FreeCAD for editing; xBIM Xplorer, BIMvision, usBIM.viewer, Solibri, BIMcollab ZOOM, Autodesk Viewer, FZK Viewer for viewing and checking; That Open Engine / web-ifc for browsers; buildingSMART's online validation service and IDS (Information Delivery Specification) checkers for validation; `grep -m 1 FILE_SCHEMA file.ifc` for a header peek [18].

Quick Python header check (the `model.schema` part is from [2]; accessing header objects via `model.wrapped_data.header` is from memory, unverified):

```python
import ifcopenshell
m = ifcopenshell.open("model.ifc")
print(m.schema)                       # 'IFC4', 'IFC2X3', ...
print(m.wrapped_data.header)          # unverified API; shows description/name/schema
print(len(m.by_type("IfcWall")))
```

---

## 12. What this means for MCP-server testing

- Identity: ask tools to refer to elements by GlobalId; a test "get element #123" is only meaningful within the same open file/session and numbers change after save/re-export.
- Round trip: open > modify > save; check that step ids may be renumbered, GlobalIds stay, header `FILE_NAME` timestamp/application changes, strings with Cyrillic are re-escaped, and MVD label is not falsely upgraded.
- Version detection: tool should read `FILE_SCHEMA` and report IFC2X3 vs IFC4 vs IFC4X3_ADD2 correctly; behaviours differ (OwnerHistory required in 2x3; Pset/entity names differ).
- Inverse relationships: "properties of wall X", "which storey is wall X on" require walking relationship entities.
- Packaging: `.ifcZIP`, huge files, one-line files, comment blocks, CRLF vs LF.
- Revit side: the IFC an MCP exports from Revit depends on Setup (version, MVD, file type, "Store IFC GUID", base quantities) [16].

---

## Typical questions people ask about this

Real questions found (linked in Sources):
1. "What is the meaning of the string \X2\****\X0\ in IFC export file?" (Autodesk forum) [22]
2. "How do I convert hexadecimal \X2\ IFC strings (a Russian example) to Unicode?" (Stack Overflow, via mirror) [23]
3. "How can I find out the version of an IFC file (IFC2X3 vs IFC4)?" (buildingSMART forum) [18]
4. "Why do IFC GUIDs change on every export of the same Revit file?" (revit-ifc issue 521 - title: room IfcGUID changes every time if the store-GUID option is checked; opened Oct 2022, closed as completed 5 Sep 2023 with exporter 22.6.x reported stable; plus Autodesk forum threads) [21][28][29]
5. "Revit IFC4x3 Reference View export writes CoordinationView in FILE_DESCRIPTION: is the file wrong?" (revit-ifc issue 1013) [9]
6. "Why does Element.UniqueId change and what does that do to the IFC GUID?" (Revit API forum) [31]

Illustrative (invented) questions, typical of testers and users:
7. (illustrative) "Why is my .ifc full of `\X2\0422...\X0\` instead of Russian text?"
8. (illustrative) "Which IFC version is this file? I only have Notepad."
9. (illustrative) "What does `$` mean in `#5=IFCWALL('...',$,'Wall-001',...)`?"
10. (illustrative) "What is `#12` and will it be the same after I re-export?"
11. (illustrative) "Is the 22-character GlobalId the same as the GUID/UniqueId in Revit?"
12. (illustrative) "Can I rename a wall by editing the text file? Do I need to change anything else?"
13. (illustrative) "Open this .ifcZIP and tell me the schema and number of walls."
14. (illustrative) "Convert this GlobalId `3IFmWa4eilCmnSVz2cewHG` to a normal hex GUID."
15. (illustrative) "Why is the ifcXML 4x bigger than the .ifc? Which should I send to the contractor?"
16. (illustrative) "Is ifcJSON an official IFC format? Can Revit import it?"
17. (illustrative) "My file says IFC4 but the viewer says IFC4X3. Which is right?"
18. (illustrative) "What is Coordination View vs Reference View? Which should I choose in Revit?"
19. (illustrative) "Do I need an IfcOwnerHistory when I create walls with IfcOpenShell for IFC4? And for IFC2X3?"
20. (illustrative) "What is the difference between `$`, an empty string and `.NOTDEFINED.`?"
21. (illustrative) "Where are the wall's properties in the file if the IFCWALL line has no property values?"
22. (illustrative) "Why does my file validate in one tool and fail in another with 'invalid GlobalId'?"
23. (illustrative) "Can the MCP server open a 2 GB IFC without loading all of it into memory?"

---

## Common pitfalls and misconceptions

- "The Cyrillic is corrupted" when it is `\X2\` escapes: by design, not a bug (section 6). Conversely, "IFC is always escaped correctly" is false; some writers emit raw bytes.
- Treating `#12` as an ID that survives re-export. Only GlobalId (and even that depends on exporter settings [20][21]) is intended to persist.
- Using a standard base64 decoder on a GlobalId (wrong alphabet [7]); or forgetting that the first character is limited to `0`-`3`.
- Believing the header proves the MVD or the version. It is the exporter's claim; bugs exist [9] and mismatches between the header and content exist [18-related].
- Assuming `FILE_SCHEMA` is exactly `IFC4X3`; real files use `IFC4X3_ADD2` etc. [9][18].
- Expecting OwnerHistory in every file, or expecting it to be a true audit log (section 7).
- Expecting properties, storeys or types to appear as attributes inside the `IFCWALL(...)` line; they are in separate relationship instances (inverse attributes are not stored).
- Writing `0` instead of `0.` for reals; writing booleans as `true`; forgetting the closing `ENDSEC;` or `END-ISO-10303-21;`.
- Thinking `.ifcZIP` is a different data model; it is just a container [12][3].
- Treating ifcJSON as a ratified IFC release (it is in "provisional/candidate" status per [3]/[14]); treating ifcXML as the normal format (it is official but rare [13]).
- Equating "IFC4" files from different MVDs: Reference View exports may omit relations and surfaces (Graphisoft notes chained wall/beam connections and material surfaces are dropped in their IFC4 export [11]).

---

## Gaps and honest limits

- buildingSMART sites (IFC formats page, string-encoding page, GUID page, IFC4.3 lexical pages, specification database) and the Autodesk forum pages returned HTTP 403 to the fetch tool; content was taken from search-result excerpts and is flagged "(via search excerpt)". Statements about the exact "Official/Provisional/Experimental" tiers on the formats page come from one such excerpt.
- Not verified at all: exact MVD view-name strings per exporter version, ifcZIP internal layout rules, IFC5/IFCX format details, ifcOWL for IFC 4.3.2, the exact IfcOpenShell header API, `.U.` logical literal.
- Not researched (search budget exhausted): comprehensive viewer/validator list with official links, Bonsai/xBIM behaviours, Russian/Chinese-language forum posts on encoding (only English results appeared), Revit menu path for versions before 2025.
- Skipped: a Stack Overflow mirror domain was used only because the original excerpt came from it; treat it as a copy of community content. A "compendium" page describing ifcOWL as research-leaning was not linked (secondary, low confidence).

---

## Sources

[1] ISO 10303-21 (Wikipedia): https://en.wikipedia.org/wiki/ISO_10303-21 (fetched)
[2] IfcOpenShell docs, Introduction to IFC: https://docs.ifcopenshell.org/introduction/introduction_to_ifc.html (fetched)
[3] buildingSMART, IFC Formats: https://technical.buildingsmart.org/standards/ifc/ifc-formats/ (403 on fetch; via search excerpts); older URL form https://technical.buildingsmart.org/?p=49
[4] buildingSMART, IFC String Encoding: https://technical.buildingsmart.org/resources/ifcimplementationguidance/string-encoding/ (via search excerpts)
[5] buildingSMART, IFC GUID: https://technical.buildingsmart.org/resources/ifcimplementationguidance/ifc-guid/ (via search excerpts)
[6] IFC 4.3.2.0 IfcGloballyUniqueId: https://standards.buildingsmart.org/IFC/RELEASE/IFC4_3/HTML/lexical/IfcGloballyUniqueId.htm (via search excerpts); also IFC4.1 version https://standards.buildingsmart.org/IFC/RELEASE/IFC4_1/FINAL/HTML/schema/ifcutilityresource/lexical/ifcgloballyuniqueid.htm
[7] ifc-model Rust crate, guid.rs (community): https://docs.rs/ifc-model/latest/src/ifc_model/guid.rs.html (fetched)
[8] IfcOpenShell guid.py (v0.8.0, GitHub): https://raw.githubusercontent.com/IfcOpenShell/IfcOpenShell/v0.8.0/src/ifcopenshell-python/ifcopenshell/guid.py (read as text)
[9] Autodesk/revit-ifc issue 1013: https://github.com/Autodesk/revit-ifc/issues/1013 (fetched)
[10] IfcOpenShell sample file (IFC2X3 header sample): https://github.com/IfcOpenShell/files/blob/master/IfcCShapeProfileDef.ifc (fetched, summarised)
[11] Graphisoft Archicad 29 Help, Model View Definitions: https://help.graphisoft.com/AC/29/INT/_AC29_Help/121_IFC/121_IFC-47.htm (fetched)
[12] Graphisoft Archicad 30 Help, Supported IFC File Types: https://help.graphisoft.com/AC/30/INT/Topics/121_IFC/121_IFC-2.html (fetched)
[13] Industry Foundation Classes (Wikipedia): https://en.wikipedia.org/wiki/Industry_Foundation_Classes (fetched)
[14] buildingSMART/ifcJSON repository: https://github.com/buildingSMART/ifcJSON (fetched)
[15] buildingSMART/IFC4.3.x-development repository: https://github.com/buildingSMART/IFC4.3.x-development (fetched)
[16] Autodesk Revit IFC exporter help 25.2: https://up1.autodesk.com/2025/RVT/ADSKIFCExporterHelp_25_2.htm (fetched)
[17] Autodesk Revit IFC export/import help and manual (via search excerpts): https://help.autodesk.com/view/RVT/2025/ENU/?guid=GUID-E029E3AD-1639-4446-A935-C9796BC34C95 ; https://www.autodesk.com/blogs/aec/wp-content/uploads/sites/36/2022/02/revit-ifc-open-bim-manual-en.pdf ; https://www.autodesk.com/support/technical/article/caas/sfdcarticles/sfdcarticles/Missing-IFC-Options-for-export-from-Revit.html
[18] buildingSMART forum, IFC Schema Identifier: https://forums.buildingsmart.org/t/ifc-schema-identifier/4802 (fetched)
[19] Tekla support, Supported IFC schemas: https://support.tekla.com/article/supported-ifc-schemas (fetched)
[20] Autodesk blog, Unique Id and IFC GUID Parameter: https://blog.autodesk.io/unique-id-and-ifc-guid/ (fetched)
[21] Autodesk/revit-ifc issue 521 (room GUIDs change when "Store the IFC GUID in an element parameter after export" is checked; read in QA): https://github.com/Autodesk/revit-ifc/issues/521
[22] Autodesk forum, meaning of \X2\...\X0\: https://forums.autodesk.com/t5/revit-architecture-forum/what-is-the-meaning-of-the-string-x2-x0-in-ifc-export-file/td-p/9627613 (via search excerpt)
[23] Stack Overflow mirror, convert hexadecimal to Unicode (Russian \X2\ example) and a Python decoder answer for \X, \X2\, \S\: https://kaweah.freedombox.rocks/kiwix/content/stackoverflow.com_en_all_2023-11/questions/65897865/convert-hexadecimal-to-unicode ; https://kiwix.lema.org/stackoverflow.com_en_all_2023-11/questions/43417411/how-to-decoding-ifc-using-ruby (mirrors, via search excerpts)
[24] buildingSMART IFC Specifications Database: https://technical.buildingsmart.org/standards/ifc/ifc-schema-specifications/ (via search excerpts)
[25] buildingSMART LDWG, ifcOWL ontology (2017): https://standards.buildingsmart.org/documents/20170830_LDWG_ifcOWLontology.pdf (via search excerpt)
[26] IFC2x Model Implementation Guide V2.0b: https://standards.buildingsmart.org/documents/Implementation/IFC2x_Model_Implementation_Guide_V2-0b.pdf (via search excerpt)
[27] IFC 4.3.2.0 IfcRoot: https://standards.buildingsmart.org/IFC/RELEASE/IFC4_3/HTML/lexical/IfcRoot.htm (via search excerpt; OwnerHistory optional since IFC4)
[28] Autodesk forum, Exporting to Ifc (door GlobalIds differ): https://forums.autodesk.com/t5/revit-architecture-forum/exporting-to-ifc/td-p/10939088 (via search excerpt)
[29] Autodesk forum, IFC export new ID every time: https://forums.autodesk.com/t5/revit-structure-forum/ifc-export-new-id-everytime-i-export/td-p/11598072 (via search excerpt)
[30] ODA IFC SDK, file formats: https://docs.intellicad.org/files/oda/2023_10/oda_ifc_docs/ifc_overview_file_formats.html (via search excerpt); IFC 4.3 IfcText (string limit): https://standards.buildingsmart.org/IFC/DEV/IFC4_3/HTML/lexical/IfcText.html (via search excerpt, labelled 30b in text)
[31] Autodesk Revit API forum, Anormal modification of Element.UniqueId: https://forums.autodesk.com/t5/revit-api-forum/anormal-modification-of-element-uniqueid/m-p/6372628/highlight/true (via search excerpt)
[41] Autodesk Revit 2024 help, IFC Export Setup Options (read in QA; option labels and tabs): https://help.autodesk.com/cloudhelp/2024/ENU/Revit-DocumentPresent/files/GUID-E029E3AD-1639-4446-A935-C9796BC34C95.htm
[42] Wikipedia, ISO 10303-21 (re-read in QA; editions 1994 / 2002 / 2016, header entities, implementation level): https://en.wikipedia.org/wiki/ISO_10303-21
[43] buildingSMART forum, IFC Schema Identifier (re-read in QA; how to find the version, `grep -m 1 FILE_SCHEMA`; the thread does not settle `IFC4X3` vs `IFC4X3_ADD2`): https://forums.buildingsmart.org/t/ifc-schema-identifier/4802
