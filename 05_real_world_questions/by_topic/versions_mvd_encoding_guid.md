# IFC versions and MVDs, text encoding, GUIDs and change tracking

Topics covered (KB vocabulary): `versions_mvd`, `encoding_text`, `guid_change_tracking`.
Data basis (wave 1): `versions_mvd` 210 records (164 real, 46 synthetic), `encoding_text` 99 (69 real, 30 synthetic), `guid_change_tracking` 154 (71 real, 83 synthetic). Records can carry more than one topic, so the three sets overlap slightly. The "question" text in the tables below is the knowledge base's paraphrase of the asker's post (kept in the original language), not a verbatim quote. Synthetic prompts are labelled as such and are never real quotes.

## In plain words

An IFC file is a plain-text file that always declares, in its first lines, which "edition" of IFC it follows (`IFC2X3`, `IFC4`, `IFC4X3_ADD2`) and, as a claim by the exporting program, which "view" (MVD, Model View Definition) it was meant for, for example Coordination View 2.0 or Reference View. Most day-to-day IFC trouble starts here: the sender exported edition X, the receiving program only really understands edition Y, and geometry, materials or colours quietly disappear. See [what IFC is and its versions](../../01_ifc_basics/01_what_is_ifc_and_versions.md) and [file anatomy: header, schema and view](../../01_ifc_basics/02_ifc_file_anatomy.md).

Second, IFC is old-style text that only allows plain ASCII letters. Every accented, Cyrillic, Chinese or Japanese character must be written as an escape such as `\X2\0421...\X0\`. That looks like garbage in Notepad but is correct; the real failures are programs that write raw bytes, write broken escapes, or read them badly. See [section 6 of the file anatomy doc](../../01_ifc_basics/02_ifc_file_anatomy.md).

Third, every object has a 22-character `GlobalId` that is supposed to stay the same for "the same" wall in every revision. When it does not (Revit regenerates some of them, copied files repeat them), comparing two versions shows "everything deleted and re-added", BCF issues lose their target and cost/4D links break. Revit-specific export behaviour is in the [Revit IFC export reference](../../03_software/revit/ifc_export_reference.md) and [import and link reference](../../03_software/revit/ifc_import_link_reference.md).

For an MCP tester: the first thing any good assistant must do with an IFC is read `FILE_SCHEMA` and `FILE_DESCRIPTION` and say what it found, never assume.

## Problem map

Ranked by how many records and how many languages show the problem. Counts are my reading of the records plus rough text-match counts (`kb.py stats --text`), so treat them as signals, not exact measurements.

| # | Problem | How users describe it | Frequency signal | Root cause | Typical fix |
|---|---|---|---|---|---|
| 1 | Which IFC version and which view should I deliver or ask for? | "2x3 or ifc4? what is coordination view?"; "какой ифс выгружать, 2х3 или 4, и какой вид"; "per la gara cosa esporto, 2x3 CV2.0 o IFC4 RV?" | Largest cluster: roughly 15-20 real records plus about 17 synthetic prompts in 7 languages (en, ru, zh, de, it, pt-BR, ko); 57 real records mention 2x3 | No single right answer: depends on receiving software, EIR/BEP and national rules; IFC2x3 CV2.0 is the safe default for unknown recipients, IFC4 RV for confirmed modern toolchains | Ask for the recipient, tool and contract; recommend, then test with a viewer or checker; write the choice into the BEP |
| 2 | "What version/MVD is this file?" and the header disagrees with the content | "how can I tell whether a file is IFC2x3 or IFC4? File properties show nothing"; "header says CoordinationView but I exported Reference View" | About 8 real records (en, ja, de, es) plus about 6 synthetic | Version is only in the text header (`FILE_SCHEMA`, `ViewDefinition`); header is the exporter's claim, bugs exist (Revit 2026.4 IFC4x3 RV wrote CoordinationView) | Read the header, then spot-check entities against the declared schema; do not trust or hand-edit the label |
| 3 | IFC4 file does not open, or geometry vanishes, in the receiver | "Revit does not open IFC4 file, only link"; "BIMServer does not render IFC4 from ARCHICAD"; "навис не показывает ифс4 из ревита, 2x3 открывается" | About 15 real records: Revit Open vs Link, BIMserver, Solibri/Trimble, Navisworks, Assimp/3D Tiles | IFC4 brought new geometry types (`IfcTriangulatedFaceSet`, `IfcPolygonalFaceSet`, `IfcAdvancedBrep`) that older importers do not read; Revit "Open" has only partial IFC4 support | Use Link IFC, re-export as IFC2x3 CV2.0, or avoid advanced geometry; update the receiving tool |
| 4 | Materials or layers "missing" in IFC4 Reference View | "Solibri shows no Material pset"; "Why are material layer sets excluded from IFC4 Reference View?" | 5-6 real records (en only, but heavy threads); 3 synthetic | RV prefers `IfcMaterialConstituentSet` over `IfcMaterialLayerSet`; viewers that look only for layer sets show nothing | Read constituents too; use DTV or IFC4.3 if layers are contractually needed; check thickness in quantities |
| 5 | IFC4.3: "Unsupported schema", unknown schema name, link errors | "SchemaError: Unsupported schema: IFC4X3"; "No schema named IFC4x3"; "Unable to open IFC 4x3 add2" | About 12 real records (en, ja) across IfcOpenShell, web-ifc, xBIM, Revit | The real identifier is `IFC4X3_ADD2` (case-sensitive); many tools or builds only know older drafts | Use the right identifier, a current build, or downgrade; check which tool version supports it |
| 6 | Converting between versions and what is lost | "How to convert an IFC2x3 file to IFC4?"; "这个IFC4的模型能不能转成IFC2x3？会丢哪些东西" | About 14 real records + 4 synthetic; no official downgrade guide | Classes, properties and geometry types differ; no official mapping table; entities cannot just be copied across schemas | Schema-aware migration (IfcOpenShell upgrade, Geometry Gym, Revit export in the target schema); report losses; keep original |
| 7 | Design Transfer View: what is it, is it official? | "IFC4 Design Transfer View experiences?"; "Why are CSG representations mandated for DTV?" | About 15 real records (almost all en) | DTV was never finalised as an official MVD; Revit labels it "Unofficial"; advanced B-reps and CSG fail across tools | Prefer Reference View for coordination; use DTV only after testing with the exact receiver |
| 8 | Text looks like `\X2\0421...\X0\` or like mojibake | "в ифс кракозябры вместо русских названий"; "ifcopenshell读出来的中文是\X2\开头的"; "Chinese encode in IFC: tried utf-8 but still messy" | About 25 real records, about 30 synthetic prompts in 11 languages (ru, zh, ja, ko, tr, ar, el, de, fr, no, en) | `\X2\` UTF-16 hex escapes are the correct STEP way of writing non-ASCII; real mojibake appears only when an exporter writes raw bytes or a program double-decodes | Decode escapes in the reader; for raw bytes, re-encode and re-export with escaping |
| 9 | Parser fails on invalid strings (the file will not load) | "IFC file fails to load due to invalid string"; "Malformed encoding causes global decoding failure"; "Unexpected 'A' ... Parsing terminated" | About 20 real records on xBIM, web-ifc, IfcOpenShell; en with ru, ja, fr, pt, cs, da, tr, ko affected texts | Raw non-ASCII, single backslash in header path, doubled backslash before `\X2\`, newline or control chars inside strings, BOM, lowercase hex handled wrongly | Locate the exact line and entity, fix or re-export; newer parsers degrade gracefully to a null value |
| 10 | Encoding and locale problems in the tool chain | "Текла просит файл без спецсимволов, имя латиница"; "REVIT2023 export fails when change language"; "tessellation written with a comma" | About 10 real records (ru, en, de, pt, zh) | Cyrillic or non-ASCII in file path or header, Windows code page when reading config files, decimal comma versus point | ASCII-only paths, latin header, explicit UTF-8, set locale or update exporter |
| 11 | GUIDs change between exports, so the diff shows "all deleted and re-added" | "guids got regenerated again"; "GUID все поменялись"; "两次导出的IFC，GUID全不一样" | About 15 real text-match records; most of the 83 synthetic prompts in this topic are "compare two versions", in 12 languages | Revit regenerates some GUIDs (collisions, steel, design options, links, groups, phases); other tools re-issue ids | Match by GlobalId first, fall back to type + name/Tag + position/geometry hash; store GUID in a parameter |
| 12 | Duplicate or invalid GlobalIds | "Why are GlobalIds not unique across files?"; "GUID valid/invalid"; "дубли" | About 8 real records + 10 synthetic | Copied or split Revit files keep UniqueIds; some writers produce 22 characters that overflow 128 bits (first char above `3`) | Regenerate for one copy only; validate format and uniqueness |
| 13 | Revit UniqueId vs IFC GUID, "Store IFC GUID" and its edge cases | "Revit のUniqueIdとIFC のGUIDとの変換"; "IfcGuids are deleted when primary design option is made secondary" | About 12 real records (en, ja) | IFC GUID is derived (XOR of ids) or stored; special cases change it | Use the stored `IfcGUID` parameter and current exporter; own IDs as properties |
| 14 | Comparing, merging and version-controlling IFC; diff tool correctness | "Is there any command line tool to diff two ifc models?"; "IfcDiff results not as expected"; "ifcmerge" | About 27 real text-match records; about 60 synthetic compare prompts in 12 languages | STEP ids (`#123`) are not stable identities; diff tools compare step ids or miss geometry | Use GlobalId, content hashes and tolerances; treat uncertain matches as "for review" |

## Problems in depth

### 1. Which version and which view should I deliver?

**Symptoms in users' words**
- en: "client says deliver in IFC. ifc2x3 or ifc4? what is coordination view? im using revit 2023" (synthetic, `en-mea-s011`, inspired by many threads; gloss: a typical beginner phrasing).
- it: "come si esporta un IFC? meglio 2x3 o IFC4?" (real, "how do I export an IFC, is 2x3 or IFC4 better?") [it-italy-r007](https://biblus.acca.it/come-creare-un-file-ifc/)
- de (source in German, KB paraphrase in English): MVD defines which data an IFC must contain for an exchange use case; MVDs must be named in the AIA and the BAP (real, Germany, explainer page) [de-dach-r025](https://www.bimdeutschland.de/bim-wissen/standards-normen-richtlinien/model-view-definitions)
- en: "IFC4 exports lose geometry, change property sets and show glitches; should we switch from IFC2x3?" (real) [en-blogs-linkedin-r022](https://bimcorner.com/is-the-industry-ready-for-ifc4/)
- ru: "версия IFC и MVD критичны; связи выгружаются отдельным IFC" (real guide for Revit export: choose IFC2x3 CV2.0 or IFC4 RV; linked files are exported separately) [ru-autodesk-telegram-r031](https://iek-digital.ru/upload/iblock/685/4jzi0mt4ob86xb78imiswfg6dngrrots/Instruktsiya-po-eksportu-IFC-dlya-REVIT.pdf)

**Why it happens.** IFC2x3 Coordination View 2.0 is the most widely accepted exchange; IFC4 Reference View (RV 1.2) is the certified IFC4 view, read-only, with simplified geometry; IFC4.3 is needed for roads, rail and bridges ([versions doc, section 5](../../01_ifc_basics/01_what_is_ifc_and_versions.md)). Forum answers say IFC2x3 certification was lax while IFC4 certification is pass/fail with no public problem documents [en-bsmart-r005](https://forums.buildingsmart.org/t/bsi-software-certification-and-ifc4/3192), and German guidance says the MVD must be named in the AIA and BAP [de-dach-r025](https://www.bimdeutschland.de/bim-wissen/standards-normen-richtlinien/model-view-definitions).

**What fixes it.** A decision based on the recipient: unknown or mixed recipients -> 2x3 CV2.0; confirmed modern toolchain -> IFC4 RV; infrastructure -> 4.3; and a test export opened in the receiver's viewer.

**What a good assistant should do.** Not announce one universal answer. Explain the three options in plain words, name the exact Revit setup labels ("IFC 2x3 Coordination View 2.0", "IFC 4 Reference View"), recommend a default with reasons, and say it must be confirmed against the EIR/BEP. If a file is loaded, read its header first.
**Clarifying questions:** Who receives the file and in what software? Does the EIR/BEP or tender document name a version and MVD? Is this for viewing/clash checking (RV is fine) or for the recipient to edit (neither IFC option round-trips well)? Which authoring tool and version? Any national or authority rule (Singapore CORENET X needs IFC4 [en-sg-corenetx-r003](https://github.com/noddlesskcho/IFC-Repair-Studio); Shenzhen filing needs the current SZ-IFC checker [zh-lightweight-review-r003](https://zhuanlan.zhihu.com/p/672903162))?

### 2. "What is the version/MVD of this file?" and the header that lies

**Symptoms**
- en: "how can I tell whether a file is IFC2x3 or IFC4? File properties show nothing; only found out by opening in a viewer" (real, student) [en-bsforum-r013](https://forums.buildingsmart.org/t/4802)
- en: "Exporting IFC4x3 Reference View yields header ViewDefinition [CoordinationView] instead of ReferenceView" (real; reproduced in Revit 2026.4, fixed in 2027) [en-gh-revit-ifc-r019](https://github.com/Autodesk/revit-ifc/issues/1013)
- ja: "IFC ファイルの中身を解読する" (real tutorial title; gloss: decoding an IFC file; FILE_SCHEMA is the IFC version, so pick the matching spec) [ja-qiita-r036](https://qiita.com/kiyuka/items/00434f1b8e0b38c621fb)
- en: "IfcLoader::GetSchema() returns IFC2X3 for every file: FILE_SCHEMA quoted identifier is a STRING token" (real developer bug in web-ifc) [en-dev-r026](https://github.com/ThatOpen/engine_web-ifc/issues/2302)

**Why.** `FILE_SCHEMA(('IFC4'))` covers IFC4 and all its addenda, so ADD1, ADD2 and ADD2 TC1 look identical; IFC4.3 appears as `IFC4X3_ADD2` (exact-match checks for `IFC4X3` miss it). The `ViewDefinition` text in `FILE_DESCRIPTION` is only what the exporter says, and the header can contradict the entities (a file labelled IFC2X3 may contain IFC4-only entities).

**Fix.** Report both facts (schema and claimed view), then check the entities; if they conflict say so. A hand-edited header does not make a file conformant.

**Good assistant behaviour.** Quote the raw header lines, state the schema, state the view as "claimed", list entity types that do not belong to the declared schema, and name the authoring application from the header. **Clarifying questions:** Was this file exported with a specific Revit/Archicad setup? Do you need a conformance verdict (then ask which checker/MVD) or only the label?

### 3. IFC4 file will not open or geometry disappears in the receiver

**Symptoms**
- en: "Open IFC lacks full IFC4 support; try IFC2x3 or Link IFC" (real answer to why a file does not open in Revit 2020) [en-autodesk-revit-import-r012](https://github.com/Autodesk/revit-ifc/issues/414)
- en: "BIMServer does not render IFC4 files from ARCHICAD 23" (real; root cause `IfcPolygonalFaceSet` unsupported) [en-bimserver-r031](https://github.com/opensourceBIM/BIMserver/issues/1103)
- en: "Revit emits IfcAdvancedBrep where extrusions would do and Solibri and Trimble can't read it" (real) [en-gh-revit-ifc-r033](https://github.com/Autodesk/revit-ifc/issues/480)
- ru: "навис не показывает ифс4 из ревита, 2x3 нормально открывается. че делать" (synthetic, `ru-vm-s017`)
- it: "ho esportato in ifc4 da archicad ma revit non lo apre, solo collegato" (synthetic, `it-vm-s014`, gloss: exported IFC4 from Archicad, Revit only links it)

**Why.** IFC4 introduced tessellated (`IfcTriangulatedFaceSet`, `IfcPolygonalFaceSet`) and advanced B-rep geometry. Revit's File > Open IFC and Link IFC are different code paths; Open has only partial IFC4 support, and cannot import `IfcTriangulatedFaceSet` [en-revit-r023](https://github.com/Autodesk/revit-ifc/issues/587); see [import/link reference](../../03_software/revit/ifc_import_link_reference.md).

**Fix.** Link instead of open; export the sender's file as IFC2x3 CV2.0 or IFC4 RV without advanced B-rep; try "Force Faceted Breps"-style workarounds (reported in [en-osarch-r032](https://community.osarch.org/discussion/898/ifc-file-doesnt-import-open-into-revit)); update the receiving tool.

**Good assistant behaviour.** Identify which geometry types the file really contains (counts of `IfcTriangulatedFaceSet`, `IfcPolygonalFaceSet`, `IfcAdvancedBrep`, CSG), tie them to the named receiver, and recommend the least lossy fix. **Clarifying:** Which program fails and which version? Open or Link? Is the sender also able to re-export?

### 4. Materials/layers "missing" in IFC4 Reference View

**Symptoms**
- en: "Solibri shows no Material pset, SimpleBIM one row with combined name for layered walls on IFC4 Reference View" (real) [en-mcl-r005](https://github.com/Autodesk/revit-ifc/issues/610)
- en: "layer information is fundamental but RV prefers constituent sets, so vendors do not deliver layers" (real) [en-mcl-r027](https://forums.buildingsmart.org/t/why-are-material-layer-sets-excluded-from-ifc4-reference-view-mvd/3638)
- en: "Materials in IFC difference between IFCVersions ... asks whether it's a bSI requirement; complains about hidden options" (real) [en-revit-r018](https://github.com/Autodesk/revit-ifc/issues/396)
- en (synthetic): "have two exports of same wall, one RV one DTV. why does one have no layers? compare materials" (`en-vm-s003`)

**Why.** Reference View uses `IfcMaterialConstituentSet` (plus shape aspects/quantities) instead of `IfcMaterialLayerSet`; a viewer that only looks for layer sets reports "no material". The wall is not missing its layers; the information is stored differently. Details in [materials doc](../../01_ifc_basics/07_materials_classification_types_styles.md).

**Fix.** Read constituent sets and base quantities; if layered build-ups are contractually required, ask for DTV/4.3 or a custom setup, and test it.

**Good assistant behaviour.** Compare the two structures per wall type, explain "different storage, not data loss" only if the thickness is in quantities, and say when it IS lost. **Clarifying:** RV or DTV? Which viewer shows nothing? Do you need layer thicknesses for quantities?

### 5. IFC4.3: "Unsupported schema", wrong identifier, tool support

**Symptoms**
- en: "i am trying to open a IFC4x3 file with ifcopenshell python but i get the error that IFC4x3 is not supported" (real) [en-civil-infra-r004](https://github.com/IfcOpenShell/IfcOpenShell/issues/6886)
- en: "schema_by_name IFC4x3 throws No schema named IFC4x3" (real beginner) [en-civil-infra-r008](https://github.com/IfcOpenShell/IfcOpenShell/issues/2382)
- ja: "web-ifc 13 バージョンを同じ IFC で比べた検証ログ ... 0.0.50はIFC4X3_ADD2でUnsupported Schema" (real, gloss: comparing 13 web-ifc versions; old ones reject IFC4X3_ADD2) [ja-japan-r012](https://zenn.dev/grok_prtex/articles/webifc-version-compare)
- en: "Is 'IFC 4.3' officially a change in the naming schema?" (real; EXPRESS identifier `IFC4X3_ADD2` is authoritative) [en-bsmart-r003](https://forums.buildingsmart.org/t/is-ifc-4-3-officially-a-change-in-the-naming-schema/5446)
- en: "IFC4X3_ADD2 header causes a Link error in Revit 2024; changing the header to IFC4X3 works" (recorded in the [Revit import reference](../../03_software/revit/ifc_import_link_reference.md), issue #928 there)

**Why.** The final 4.3 edition is `IFC4X3_ADD2`; older RC files used other names; IfcOpenShell conda/docker builds compile only some schemas; the identifier is case-sensitive.

**Fix.** Use `IFC4X3_ADD2`, a build that includes it, and a viewer version that supports it; as a temporary workaround people edit the header, which only helps if the content is valid.

**Good assistant behaviour.** Read the header, say which edition it really is, say which part of the tool chain is rejecting it (parser, schema build, viewer), and warn that header edits are a workaround. **Clarifying:** Which library/viewer version? Where did the file come from (RC export or final)?

### 6. Converting between versions and what is lost

**Symptoms**
- en: "Guidelines for IFC4x3 exports to IFC2x3 and IFC4? how to downgrade IfcConveyorSegment to IfcFlowSegment? IfcBridge parts to IfcSite?" (real) [en-bsforum-r017](https://forums.buildingsmart.org/t/5133)
- en: "Convert/upgrade ifc2x3 to ifc4? Has IFC2x3 from Revit, no Revit access" (real) [en-roundtrip-r020](https://forums.buildingsmart.org/t/convert-upgrade-ifc2x3-to-ifc4/5210)
- en: "Merging IFC2x3 entities in a IFC4 file ... add() does not work across schemas" (real) [en-bsmart-r015](https://forums.buildingsmart.org/t/merging-ifc2-3-elntities-in-a-ifc4-file/2846)
- zh: "这个IFC4的模型能不能转成IFC2x3？帮我看看会丢哪些东西" (synthetic, `zh-vm-s006`)
- en: "IFC4 property name changes ... asks for rename document to update automation mapping" (real) [en-bsmart-r016](https://forums.buildingsmart.org/t/ifc4-property-name-changes/2539)

**Why.** There is no official downgrade mapping; the change log (Annex F) omits renames; classes (`IfcAlignment`, `IfcPavement`, `IfcBuiltElement`), property names and geometry types differ between schemas.

**Fix.** Re-export from the authoring tool in the target schema if possible; otherwise use a schema-aware migration (IfcOpenShell upgrade, Geometry Gym, BIMserver) and a loss report; never edit only the schema string.

**Good assistant behaviour.** Work on a copy, state the target schema, list classes with no equivalent (and what they became: proxy, supertype), verify the output header and that the original is untouched. **Clarifying:** Why is the downgrade needed (which receiver)? Is re-export from the authoring tool possible? Which losses are acceptable?

### 7. Design Transfer View: official or not?

**Symptoms**
- en: "IFC4 Design Transfer View experiences?" (short open question) [en-bsmart-r010](https://forums.buildingsmart.org/t/ifc4-design-transfer-view-experiences/4362) - answer: DTV never finalised; Revit DTV is CV2.0 plus advanced B-reps, now unofficial.
- en: "IFC4 design transfer view spec: RV easy to find but DTV index page empty" (real) [en-bsmart-r017](https://forums.buildingsmart.org/t/ifc4-design-transfer-view-spec/1737)
- en: "Why are CSG representations mandated for DTV?" (real) [en-bsmart-r012](https://forums.buildingsmart.org/t/why-are-csg-representations-mandated-for-dtv/2311)
- ko (synthetic): "레빗에서 IFC4 내보낼때 Reference View랑 Design Transfer View 중에 뭐 써야돼요?" (`ko-vm-s013`, gloss: which of RV or DTV in Revit IFC4 export)

**Why.** DTV was meant for editable handover, but the buildingSMART database lists it as draft; Revit labels it "[Unofficial]". Advanced B-rep/CSG fail across tools.

**Fix / behaviour.** Recommend RV for coordination; DTV only after a test with the exact receiver. **Clarify:** Does the receiver need to edit geometry? Which tool?

### 8. Text shows as `\X2\...\X0\` or mojibake

**Symptoms**
- ru: "в ифс кракозябры вместо русских названий, найди где поломано" (synthetic, `ru-renga-nanocad-s010`)
- zh: "导出的IFC里中文变成\X2\...\X0\，是UTF-16十六进制，怎么解回来" (real: Revit's Chinese escaping explained) [zh-csdn-dev-r021](https://blog.csdn.net/qq_35042852/article/details/137257689)
- en/zh: "which chinese encoding pattern do you use in IFC generation? tried utf-8 but still messy code" (real, answer: STEP uses `\X2\` hex escapes; IfcOpenShell supports it) [en-gh-encoding-r001](https://github.com/IfcOpenShell/IfcOpenShell/issues/571)
- fr: "Revit native wrote Chauss\X2\00E9\X0\, add-in 22.4.1 writes \X\E9; has there been a change?" (real; both are valid) [en-gh-encoding-r024](https://github.com/Autodesk/revit-ifc/issues/441)
- da: "I use UTF-8 because of AE O AA; values read like V\X\E6gelement" (real) [en-gh-encoding-r022](https://github.com/ThatOpen/engine_web-ifc/issues/358)
- ru (synthetic, double decoding): "в модели имена вида РЎС‚РѕР№ка - вылечи, перекодируй обратно" (`enc-s016`)

**Why.** The STEP file format is ASCII-only: `\X2\hhhh\X0\` (UTF-16 hex), `\X\hh` (Latin-1) and `\S\c` are the standard escapes; both `\X\E9` and `\X2\00E9\X0\` are valid. Real mojibake (e.g. `РЎС‚...`) means a program wrote UTF-8/cp1251 bytes and another read them with the wrong code page. See [file anatomy, section 6](../../01_ifc_basics/02_ifc_file_anatomy.md).

**Fix.** Use a STEP-aware reader that decodes escapes (IfcOpenShell does; a raw text view will not). If raw bytes were written, re-export from the source or run a repair that re-encodes.

**Good assistant behaviour.** Distinguish the three cases (valid escapes shown raw; double-decoded text; raw bytes written illegally), decode to readable text, list affected entities with class and GlobalId, and never "fix" a valid escape. **Clarifying:** Where do you see the garbage (Notepad, a viewer, Python, Excel)? Which exporter and version wrote the file? Is the text wrong in the file or only in one program?

### 9. The parser fails on an invalid string: the whole file refuses to load

**Symptoms**
- en: "one malformed escape in IFCPROPERTYSINGLEVALUE drops many entities; wants the parser to skip and log instead" (real, xBIM) [en-gh-xbim-others-r019](https://github.com/xBimTeam/XbimEssentials/issues/605)
- en/ja: "File with Japanese \X2\ text and a doubled backslash loads only 10 of 78 products" (real) [en-gh-encoding-r015](https://github.com/xBimTeam/XbimEssentials/issues/605)
- en: "FILE_NAME('C:\Users\1PIPEIFC.IFC') not properly encoded; latest Xplorer cannot open" (real) [en-gh-encoding-r016](https://github.com/xBimTeam/XbimEssentials/issues/561)
- en: "IfcOpenShell failed to load UTF-8 BOM file: Unable to parse IFC SPF header; resaving without BOM works" (real) [en-err-r023](https://github.com/IfcOpenShell/IfcOpenShell/issues/4256)
- ru: "IFCBUILDINGELEMENTPROXY name mixes \X2\ escapes with raw Cyrillic; Python exception on read" (real, SolidWorks) [en-gh-encoding-r017](https://github.com/IfcOpenShell/IfcOpenShell/issues/3182)
- pt: "IFC from Archstation does not open in Bonsai on Ubuntu; file has raw 0xE7/0xE3 bytes" (real) [en-gh-encoding-r019](https://github.com/IfcOpenShell/IfcOpenShell/issues/7305)
- en: "Encoding of special characters eats the following character" (real, writer bug) [en-gh-encoding-r008](https://github.com/ThatOpen/engine_web-ifc/issues/406); lowercase hex in `\X2\...\X0\` decodes wrongly in `GetLine()` [zh-csdn-dev-r014](https://github.com/ThatOpen/engine_web-ifc/issues/949)

**Why.** Strict readers follow ISO 10303-21: raw non-ASCII, single backslashes, a BOM, newlines inside an `\X2\` run, form feed or `\X\1F` control characters (illegal in XML) or an unterminated escape make the string invalid. Older tools tolerated this; newer ones stop, or make the value null.

**Fix.** Find the exact entity and line and repair that string, or re-export from a conforming source; ask parser authors for lenient mode where available. Writers must escape every non-ASCII character.

**Good assistant behaviour.** Scan the raw STEP text (not only the parsed model, which may already have dropped the string), report line numbers, entity ids and attribute, and offer a repaired copy while keeping GlobalIds. **Clarifying:** Which tool fails and with what exact message? Can I write a repaired copy next to the original? Should I only report, not change?

### 10. Encoding and locale problems around the file, not inside it

**Symptoms**
- ru: "Текла просит переименовать файл без спецсимволов, имя только латиница, не помогает" (real; Cyrillic in the header path suspected) [ru-dwg-other-r010](https://forum.dwg.ru/showthread.php?t=159943)
- en: "REVIT2023 - Fail export when change language. Export produces nothing" (real) [en-err-r008](https://github.com/Autodesk/revit-ifc/issues/718); "IFC export: empty file ... cause was a change of interface language" [es-latam-r008](https://forums.autodesk.com/t5/revit-architecture-forum/ifc-export-empty-file/m-p/8336603)
- en: "Floors not exporting ... changing Windows language fixed it" (root cause: `exportlayers-ifc-IAI.txt` read as UTF-16 without encoding on non-English code pages; fixed in Revit 2025) [en-geom-r009](https://github.com/Autodesk/revit-ifc/issues/759)
- en: "Unrecoverable Error during IFC Export using Dynamo" (tessellation level written as '0,5' with a comma, locale issue) [en-dynamo-pyrevit-r007](https://forum.dynamobim.com/t/unrecoverable-error-during-ifc-export-using-dynamo/113291)
- en: "Character encoding issues with import class mappings in German locale" [en-gh-encoding-r010](https://github.com/Autodesk/revit-ifc/issues/7)
- zh: "路径里有中文好像会失败，所以进工具目录里执行" (real, gloss: Chinese in the path seems to break IfcConvert, so run from the tool folder) [zh-csdn-dev-r003](https://www.cnblogs.com/LeeSki/p/14293418.html)

**Why.** Config files, paths and command lines go through the operating system's code page and locale, not through IFC escaping. Decimal comma versus point breaks numbers sent to exporters.

**Fix.** ASCII-only paths for tools, explicit UTF-8, up-to-date exporter, point as decimal in scripts.

**Good assistant behaviour.** Ask about environment before blaming the file: Windows/Revit UI language, exporter version, path characters, locale of the script. **Clarifying:** What is the full path and Revit UI language? Does the same model export on another PC? Which exporter version?

### 11. GUIDs change between exports: "everything deleted and added"

**Symptoms**
- en: "Revit regenerates GlobalIds for some categories so a GlobalId-only diff makes everything look deleted and re-added; planned fallback is matching orphans by IfcType, geometry hash and centroid proximity" (real) [en-osarch-guid-r001](https://community.osarch.org/discussion/3616/browser-based-ifc-clash-version-diff-how-would-you-group-clashes-and-handle-guid-churn)
- en: "the authoring tool regenerates the GlobalIds every week, only geometric extents matter" (real) [en-osarch-guid-r002](https://community.osarch.org/discussion/comment/12255#Comment_12255)
- en: "GUIDs of some walls change on every export; traced to CreateAlternateGUID collisions" (real) [de-dach-r007](https://github.com/Autodesk/revit-ifc/issues/109)
- en: "Since Revit 2023 IfcGuid follows UniqueId so moving a door with Disjoin changes its GUID" (real) [en-gh-revit-ifc-r044](https://github.com/Autodesk/revit-ifc/issues/696)
- en: "New phases change GUIDs and break external databases keyed on them" (real, FM) [en-gh-revit-ifc-r048](https://github.com/Autodesk/revit-ifc/issues/65)
- zh: "两次导出的IFC，GUID全不一样，帮我按类型和坐标匹配一下，看看到底哪些构件真的改了" (synthetic, `zh-guid-s007`)

**Why.** In Revit the IFC GUID is derived from the element's UniqueId (or stored in the `IfcGUID` parameter); special cases create new ones: collisions, steel, groups, design options, linked models (hash of link instance GUID and element GUID, deliberate), type elements, new phases. Other authoring tools may re-issue ids on each export.

**Fix.** Current exporter; "Store the IFC GUID in an element parameter after export"; keep elements instead of recreating them; fall back to type + name/Tag + placement + geometry hash.

**Good assistant behaviour.** Before running the diff, measure how many GlobalIds are shared between the two files; if the overlap is suspiciously low (e.g. thousands "deleted" and the same number "added"), say so and offer fallback matching with a confidence label, rather than reporting a huge false change list. **Clarifying:** Which tool and exporter version made each file? Was the Revit file copied, split or exported with linked models merged? How close in position (tolerance) counts as the same element?

### 12. Duplicate or invalid GlobalIds

**Symptoms**
- en: "found 2,578 duplicate GlobalIds among ~1.9M elements across six architectural IFC files; users copy or split Revit files" (real) [en-revitifc-guid-r015](https://github.com/Autodesk/revit-ifc/issues/378)
- en: "asks if GUID like k0el31... is allowed" (real; not valid, exceeds 128 bits; fixed in IFC4.3) [en-val-r013](https://forums.buildingsmart.org/t/guid-valid-invalid/3776)
- en: "GUIDs produced have a letter as the first character" (real, IfcPlusPlus regression) [en-gh-xbim-others-r037](https://github.com/ifcquery/ifcplusplus/issues/305)
- fr (synthetic): "vérifie que tous les GlobalId sont valides (22 caractères base64) et qu'il n'y a pas de doublons" (`fr-guid-s011`)
- it (synthetic): "abbiamo copiato il file e ora ci sono GlobalId doppi tra i due modelli, puoi rigenerarli solo per il secondo?" (`it-guid-s014`)

**Why.** GlobalId must be unique inside a project, but duplicating a Revit file keeps its UniqueIds, so copies repeat them. A valid GlobalId is 22 characters of IFC's own base-64 alphabet and the first character is `0`-`3` ([anatomy doc, section 5](../../01_ifc_basics/02_ifc_file_anatomy.md)).

**Fix.** Regenerate IDs for one copy only; check format and uniqueness; keep a mapping old -> new.

**Good assistant behaviour.** Distinguish duplicates inside one file (a defect) from the same GUID in two files (expected after copying), list class/name/storey for each pair, never regenerate without being asked, and warn about broken external references (BCF, cost, 4D). **Clarifying:** Within one file or across files? Should the original keep its IDs? Do external systems reference the old GUIDs?

### 13. Revit UniqueId vs IFC GUID and "Store IFC GUID"

**Symptoms**
- ja: "RevitのUniqueIdとIFCのGUIDが全然違って見えるので、どう対応するのか知りたい" (real; gloss: UniqueId and IFC GUID look completely different, how do they correspond?) [p-student-r034](https://qiita.com/Takashi_Kasuya/items/97899d15e7ec0186eecf); answer (also [ja-qiita-guid-r026](https://qiita.com/Takashi_Kasuya/items/97899d15e7ec0186eecf)): four rules (imported IFC GUID kept; 1:1 elements use episode-id GUID XOR element id; entities without counterpart use Detach GUID XOR element id; others random).
- en: "IFC Guid is different in the IFCGuid parameter (written by revit) and the exported IFC" (real) [en-autodesk-revit-export-r038](https://forums.autodesk.com/t5/revit-api-forum/ifc-guid-is-different-in-the-ifcguid-parameter-written-by-revit/td-p/12650094)
- en: "If you delete an IfcGuid (e.g. of a room or a level), always the same IfcGuid will be created again" (real; deterministic by design, persistent GUID is a certification requirement) [en-revitifc-guid-r014](https://github.com/Autodesk/revit-ifc/issues/617)
- en: "IfcGuids are deleted when primary design option is made secondary" [en-revitifc-guid-r017](https://github.com/Autodesk/revit-ifc/issues/314); "Type IfcGUID of IFC Element Type changes" [en-revitifc-guid-r016](https://github.com/Autodesk/revit-ifc/issues/512)
- en: "Federated Export with wrong IfcGuids" (by design, each link instance needs its own GUID) [en-revitifc-guid-r013](https://github.com/Autodesk/revit-ifc/issues/825)
- zh: "revit 2020 ifc guid不生成是为什么?" (real; gloss: why are no IFC GUIDs generated in a Revit 2020 export; generic answer: export settings, version, plugin) [zh-zhihu-r007](https://www.zhihu.com/question/625548241)

**Fix / behaviour.** Do not claim an exact conversion from UniqueId to the exported GUID without qualification: the actual exported value may differ for derived entities, linked elements and design options. Offer the stored `IfcGUID` parameter as the reliable key. **Clarify:** Is the "Store IFC GUID" option on? Revit and exporter version? Elements in groups, design options or links?

### 14. Comparing, merging and version-controlling IFC

**Symptoms**
- en: "Is there any command line tool to diff two ifc models?" (real) [en-roundtrip-r028](https://forums.buildingsmart.org/t/is-there-any-command-line-tool-to-diff-two-ifc-models/1252)
- it: "ho due revisioni dello stesso IFC, come vedo cosa e cambiato (aggiunti, rimossi, modificati)?" (real) [it-italy-r009](https://biblus.acca.it/rilevare-modifiche-nei-modelli-ifc/)
- en: "all 1,025 matched elements flagged as property changes because pset STEP ids are compared; geometry not checked without MODEL_VIEW; wall thickened 1.5x gave empty change register" (real, IfcDiff) [en-ifcos-diff-r023](https://github.com/IfcOpenShell/IfcOpenShell/issues/9610)
- en: "IfcDiff not catching predefined type removal as change" [en-gh-ifcopenshell-r035](https://github.com/IfcOpenShell/IfcOpenShell/issues/8214)
- en: "How can a Revit model be re-exported to IFC and updated in BlenderBIM without losing cost and schedule data?" (real, estimator) [en-osarch-r011](https://community.osarch.org/discussion/626/versioning-of-revit-ifc-exports)
- en: "two people branch the same IFC and both create entity #12346, git cannot merge" (real) [en-osarch-guid-r003](https://community.osarch.org/discussion/comment/11630#Comment_11630)
- ru: "как найти дубли в IFC которых не видно и переслать правки коллеге" (real, edit journal keyed by GlobalId) [ru-habr-dev-r008](https://habr.com/ru/articles/1100956/)

**Why.** STEP ids (`#123`) are renumbered at every save and are not identities; diff tools that compare step ids over-report; geometry comparison needs a mode and tolerances.

**Good assistant behaviour.** Report added, removed, modified separately; say how matching was done (GlobalId or fallback), what was not compared (geometry? psets? relationships?) and tolerance used; mention groups of changes by class/storey; flag cost/4D/BCF links tied to removed elements. **Clarifying:** Which two files (and which is older)? Compare attributes, properties, geometry, or all? Tolerance in mm? Restrict to a discipline or classes?

## Real questions

KB paraphrases, original language kept; "EN gloss" given where the original is not English. Source link text is the KB record id. Personas are the KB's inference of the asker's role.

| # | lang | question (original-language paraphrase) | EN gloss | persona | source |
|---|---|---|---|---|---|
| 1 | en | how can I tell whether a file is IFC2x3 or IFC4? File properties show nothing; only found out by opening in a viewer | – | student_beginner | [en-bsforum-r013](https://forums.buildingsmart.org/t/4802) |
| 2 | en | Short polite post asking for a changelog of renamed/deprecated entities and subtypes between schema versions, with one example | – | bim_coordinator | [en-bsmart-r002](https://forums.buildingsmart.org/t/list-of-changes-between-ifc-versions/4604) |
| 3 | en | Is "IFC 4.3" officially a change in the naming schema? (spacing changes forum search results) | – | researcher_academic | [en-bsmart-r003](https://forums.buildingsmart.org/t/is-ifc-4-3-officially-a-change-in-the-naming-schema/5446) |
| 4 | en | What is the actual status of IFC4ADD2TC1? Friend pointed to doc site marked official, no news on buildingSMART site | – | bim_manager | [en-bsmart-r004](https://forums.buildingsmart.org/t/what-is-the-actual-status-of-ifc4add2tc1/663) |
| 5 | en | Question about MVD, IDM, COBie, etc.: confused by "these many formats" | – | student_beginner | [en-bsmart-r009](https://forums.buildingsmart.org/t/question-about-mvd-idm-cobie-etc/2762) |
| 6 | en | IFC4 Design Transfer View experiences? | – | bim_manager | [en-bsmart-r010](https://forums.buildingsmart.org/t/ifc4-design-transfer-view-experiences/4362) |
| 7 | en | Official Model View Definitions for IFC 4.3: no direct doc link, no 4.3 folder in the MVD release repo | – | developer_programmer | [en-bsmart-r011](https://forums.buildingsmart.org/t/official-model-view-definitions-for-ifc-4-3/5737) |
| 8 | en | Why are material layer sets excluded from IFC4 Reference View MVD? RV is the only final IFC4 MVD so it is what vendors export, but without IfcMaterialLayerSet it is unusable for contract specification | – | developer_programmer | [en-bsmart-r001](https://forums.buildingsmart.org/t/why-are-material-layer-sets-excluded-from-ifc4-reference-view-mvd/3638) |
| 9 | en | Is the industry ready for IFC4? IFC4 exports lose geometry, change property sets and show glitches; should we switch from IFC2x3? | – | bim_manager | [en-blogs-linkedin-r022](https://bimcorner.com/is-the-industry-ready-for-ifc4/) |
| 10 | en | Option to prevent export of IfcAdvancedBrep: Revit emits it where extrusions would do and Solibri and Trimble can't read it | – | developer_programmer | [en-gh-revit-ifc-r033](https://github.com/Autodesk/revit-ifc/issues/480) |
| 11 | en | Can't import IfcTriangulatedFaceSet (gives Revit version/add-in, sample from the buildingSMART site) | – | bim_coordinator | [en-revit-r023](https://github.com/Autodesk/revit-ifc/issues/587) |
| 12 | en | IFC file doesn't import/open into Revit (thread about Open failing for IFC4) | – | bim_coordinator | [en-osarch-r032](https://community.osarch.org/discussion/898/ifc-file-doesnt-import-open-into-revit) |
| 13 | en | IFC4 loses element colors compared to IFC2x3: two files from the same Revit model, 2x3 renders all colors in my viewer, IFC4 only some | – | bim_coordinator | [en-gh-thatopen-r015](https://github.com/ThatOpen/engine_web-ifc/issues/1793) |
| 14 | en | IFC4x3 Reference View export writes CoordinationView in FILE_DESCRIPTION instead of ReferenceView | – | bim_coordinator | [en-gh-revit-ifc-r019](https://github.com/Autodesk/revit-ifc/issues/1013) |
| 15 | en | IFC-Repair-Studio: got IFC0000101 "update file to supported IFC version", I exported ifc2x3, how to export ifc4 with IFC+SG settings | – | architect | [en-sg-corenetx-r003](https://github.com/noddlesskcho/IFC-Repair-Studio) |
| 16 | en | i am trying to open a IFC4x3 file with ifcopenshell python but i get the error that IFC4x3 is not supported | – | developer_programmer | [en-civil-infra-r004](https://github.com/IfcOpenShell/IfcOpenShell/issues/6886) |
| 17 | en | Merging IFC2*3 entities in a IFC4 file (IfcTransportElement, IfcDiscreteAccessory) | – | developer_programmer | [en-bsmart-r015](https://forums.buildingsmart.org/t/merging-ifc2-3-elntities-in-a-ifc4-file/2846) |
| 18 | en | Convert/upgrade ifc2x3 to ifc4? Has IFC2x3 from Revit, no Revit access, believes Archicad needs IFC4 | – | student_beginner | [en-roundtrip-r020](https://forums.buildingsmart.org/t/convert-upgrade-ifc2x3-to-ifc4/5210) |
| 19 | en | Guidelines for Ifc4x3 (add2) exports to Ifc2x3 (tc1) and Ifc4 (add2 tc1)? how to downgrade IfcConveyorSegment to IfcFlowSegment? | – | developer_programmer | [en-bsforum-r017](https://forums.buildingsmart.org/t/5133) |
| 20 | en | BIMServer does not render IFC4 files from ARCHICAD 23 (bug report, exception log) | – | bim_coordinator | [en-bimserver-r031](https://github.com/opensourceBIM/BIMserver/issues/1103) |
| 21 | es | Como poder exportar un modelo 3D estructural realizado en Revit a ETABS por medio del formato IFC? | Exporting a structural Revit model to ETABS via IFC: ETABS says "Could not find ENDSEC at end of file", grids show as not exported (polite formal Spanish, thesis researcher) | structural_engineer | [es-bsmart-r007](https://forums.buildingsmart.org/t/como-poder-exportar-un-modelo-3d-estructural-realizado-en-revit-a-etabs-por-medio-del-formato-ifc/2985) |
| 22 | es | Trabajar con IFC (Ayuda Archicad 28): IFC formato abierto, Archicad soporta IFC2x3 e IFC4, IFC Manager, traductores | Archicad help: supports IFC2x3 and IFC4, translators, model filters | student_beginner | [es-latam-r018](https://help.graphisoft.com/AC/28/SPA/_AC28_Help/121_IFC/121_IFC-1.htm) |
| 23 | es | IFC e interoperabilidad en BIM | e-zigurat article: history and limits of IFC; Revit to Archicad exchange can lose information, test each case | student_beginner | [es-spain-r020](https://www.e-zigurat.com/es/blog/ifc-e-interoperabilidad-en-bim/) |
| 24 | it | Come creare un file IFC: come si esporta un IFC? meglio 2x3 o IFC4? | How do I create an IFC and which version (2x3 or 4)? | student_beginner | [it-italy-r007](https://biblus.acca.it/come-creare-un-file-ifc/) |
| 25 | it | IFC Coordination View: cos'e la Coordination View 2.0 e quando usarla? | What is Coordination View 2.0 and when to use it? | architect | [it-italy-r017](https://biblus.acca.it/ifc-2x3-coordination-view-2-0/) |
| 26 | it | IFC 4.3: cosa cambia per strade e ferrovie? i software lo supportano? | What does IFC 4.3 change for roads and rail, is it supported? | civil_infra_engineer | [it-italy-r016](https://biblus.acca.it/ifc-4-3-approvato-come-standard-finale/) |
| 27 | de* | Model View Definitions: MVD defines which data an IFC must contain for an exchange use case (Coordination View, Design Transfer View, Reference View, QTO View) | MVDs must be named in AIA and BAP | reviewer_authority | [de-dach-r025](https://www.bimdeutschland.de/bim-wissen/standards-normen-richtlinien/model-view-definitions) |
| 28 | de* | Die Wunderwaffe IFC: partner imports my IFC and windows/walls come as plain dumb objects; is IFC supposed to be lossless? | IFC is no miracle weapon: parametric objects arrive as dumb objects | bim_manager | [en-blogs-linkedin-r004](https://bim-me-up.com/die-wunderwaffe-ifc/) |
| 29 | de* | Aktuelle Revit IFC Exporter: which exporter version do I have and where to get the newest? | Many export issues come from an outdated Revit IFC exporter add-in | bim_coordinator | [en-blogs-linkedin-r008](https://bim-me-up.com/aktuelle-revit-ifc-exporter/) |
| 30 | ru | САПФИР-3D 2020 R2. Как правильно экспортировать модель в IFC? импортирую IFC из сапфира, выдаёт System Error encountered during import | IFC from SAPFIR gives a system error in Autodesk tools; how to export correctly? | structural_engineer | [ru-autodesk-telegram-r003](https://forum.dwg.ru/showthread.php?t=160240) |
| 31 | ru | Экспорт из Tekla в Revit: IFC не работает; позже свойства и геометрия теряются при импорте | Tekla IFC export did not work for Revit; later properties and geometry lost, which IFC version? | structural_engineer | [ru-autodesk-telegram-r005](https://forum.dwg.ru/showthread.php?t=146029) |
| 32 | ru | Инструкция по выгрузке IFC из Revit: версия IFC и MVD критичны; связи выгружаются отдельным IFC | Guide: IFC version and MVD are critical, linked files exported separately | bim_coordinator | [ru-autodesk-telegram-r031](https://iek-digital.ru/upload/iblock/685/4jzi0mt4ob86xb78imiswfg6dngrrots/Instruktsiya-po-eksportu-IFC-dlya-REVIT.pdf) |
| 33 | ru | Пересохранение файлов ArchiCAD: как сохранить файл Архикада в IFC для открытия в младшей версии | How to resave ArchiCAD files to an older version via IFC? | architect | [ru-dwg-other-r024](https://forum.dwg.ru/showthread.php?t=75685) |
| 34 | ru | Эпоха перемен: IFC уходит в прошлое. Autodesk бросит IFC ради USD? | Autodesk may abandon IFC for USD; opinion thread | developer_programmer | [ru-habr-dev-r019](https://habr.com/ru/articles/860936/) |
| 35 | zh | revit低版本的模型能在高版本打开吗：高版本revit的模型低版本打不开，导出ifc行不行 | Can a lower Revit open a higher-version model? Export IFC2x3? | bim_coordinator | [zh-revit-export-r010](https://www.zhulong.com/zt_bim_3002296/detail42826395/) |
| 36 | zh | Revit打开IFC文件后元素丢失或者变形怎么办 | Revit shows missing or distorted elements when opening IFC | bim_coordinator | [zh-revit-export-r002](https://ask.csdn.net/questions/8391346) |
| 37 | zh | Revit2020导出IFC选项是灰的 | Revit 2020 IFC export option greyed out | bim_coordinator | [zh-revit-export-r016](https://zhuanlan.zhihu.com/p/611709017) |
| 38 | zh | 1.1.0版本自检通过的模型2024年起传不上去政府报建系统，要更新到1.3.0吗 | Models passed with the 1.1.0 self-check can no longer be uploaded to the Shenzhen filing system from 2024 | bim_manager | [zh-lightweight-review-r003](https://zhuanlan.zhihu.com/p/672903162) |
| 39 | zh | IFC2x3和IFC4主要区别 | Main differences between IFC2x3 and IFC4 | developer_programmer | [zh-zhihu-r038](https://www.cnblogs.com/herd/p/17350345.html) |
| 40 | ja | web-ifcを上げる前に何が変わるか。0.0.50はIFC4X3_ADD2でUnsupported Schema | What changes before upgrading web-ifc: 0.0.50 rejects IFC4X3_ADD2 | developer_programmer | [ja-japan-r012](https://zenn.dev/grok_prtex/articles/webifc-version-compare) |
| 41 | ja | IFCにすれば別ソフトで編集を続けられると思われがち。実際はパラメトリック関係や独自パラメータが落ちる | People think IFC lets you keep editing elsewhere; parametrics and custom parameters get lost | bim_manager | [ja-japan-r021](https://note.com/onestruction/n/ne8322e3be44d) |
| 42 | ja* | IFC ファイルの中身を解読する (tutorial title) | Decoding an IFC file: FILE_SCHEMA is the IFC version; links IFC4x3 docs because IFC2x3 docs lack type links | developer_programmer | [ja-qiita-r036](https://qiita.com/kiyuka/items/00434f1b8e0b38c621fb) |
| 43 | ko | IFC 최신 버전, IDS, IFC 검증 서비스, 인증 스코어카드, 국내 BIM 지침 목록 | buildingSMART Korea R&D page: latest IFC, IDS, validation, certification, Korean guidelines | researcher_academic | [ko-korea-r002](https://www.buildingsmart.or.kr/Home/RnDCenter) |
| 44 | no | hvilke IFC-versjoner brukes i prosjekter nå, og hva er nytt i IFC4.3? | Which IFC versions are used in Norwegian projects now and what is new in 4.3? | student_beginner | [no-norway-r001](https://www.buildingsmart.no/standarder/kort-forklart.html) |
| 45 | nl | Pset_WallCommon: FireRating, LoadBearing, IsExternal; eigen PropertySet-namen mogen niet met Pset beginnen | Dutch ILS guide: custom property set names must not start with Pset; Pset_PileCommon has no LoadBearing in IFC2x3 TC1, use a custom set | structural_engineer | [nl-dutch-r020](https://www.digigo.nu/ilsen-en-richtlijnen/bim-basis-ils/3-7-gebruik-propertysets) |
| 46 | en | Material pset Wall/Floors with several material layers not exported IFC4: Solibri shows no Material pset | – | bim_coordinator | [en-mcl-r005](https://github.com/Autodesk/revit-ifc/issues/610) |
| 47 | en | Dynamo: tried several Revit/Dynamo versions, reset Dynamo, reinstalled Revit (cause: tessellation level written with a comma) | – | developer_programmer | [en-dynamo-pyrevit-r007](https://forum.dynamobim.com/t/unrecoverable-error-during-ifc-export-using-dynamo/113291) |
| 48 | en | Chinese encode in IFC: which chinese encoding pattern do you use in IFC generation? tried utf-8 but still messy code | – | developer_programmer | [en-gh-encoding-r001](https://github.com/IfcOpenShell/IfcOpenShell/issues/571) |
| 49 | zh | IFCPROPERTYSINGLEVALUE里的\X2\...\X0\小写十六进制，GetLine读出来是错的，改成大写就对 | GetLine() returns wrong Chinese text for lowercase hex; uppercase decodes correctly | developer_programmer | [zh-csdn-dev-r014](https://github.com/ThatOpen/engine_web-ifc/issues/949) |
| 50 | zh | 导出的IFC里中文变成\X2\...\X0\，是UTF-16十六进制，怎么解回来 | Chinese turns into \X2\ UTF-16 hex escapes in the exported IFC, how to decode | developer_programmer | [zh-csdn-dev-r021](https://blog.csdn.net/qq_35042852/article/details/137257689) |
| 51 | zh | ifcxml里Name含中文或西里尔字符，读出来被截断，非拉丁字符成了字符串起点 | Strings with Chinese/Cyrillic get truncated reading ifcXML in IfcOpenShell | student_beginner | [zh-csdn-dev-r015](https://github.com/IfcOpenShell/IfcOpenShell/issues/3499) |
| 52 | ru | Текла просит переименовать файл без спецсимволов, имя только латиница, не помогает | Tekla asks to rename the file without special characters though the name is Latin; Cyrillic in the header path suspected | structural_engineer | [ru-dwg-other-r010](https://forum.dwg.ru/showthread.php?t=159943) |
| 53 | ru* | Swood Design (SolidWorks) - IFC read error: IFCBUILDINGELEMENTPROXY name mixes \X2\ escapes with raw Cyrillic; Python exception on read | SolidWorks IFC has Cyrillic written raw next to \X2\ pieces, Python read fails | structural_engineer | [en-gh-encoding-r017](https://github.com/IfcOpenShell/IfcOpenShell/issues/3182) |
| 54 | fr* | [IfcConvert] Convert string error: IFC with special characters in header FILE_NAME gives wstring_convert: to_bytes error; DAE works | IfcConvert to XML fails with accented characters in the header FILE_NAME | bim_coordinator | [en-gh-encoding-r018](https://github.com/IfcOpenShell/IfcOpenShell/issues/1016) |
| 55 | fr* | New codification for special character and accent? Revit native wrote Chauss\X2\00E9\X0\, add-in 22.4.1 writes \X\E9; has there been a change? | Accents written differently after exporter update; was the encoding changed? (answer: both valid) | bim_manager | [en-gh-encoding-r024](https://github.com/Autodesk/revit-ifc/issues/441) |
| 56 | pt* | Falha de importação de arquivo IFC com Bonsai (title); IFC from Archstation does not open in Bonsai on Ubuntu 24.04 even after downgrading Blender | Brazilian user; analysis found raw 0xE7/0xE3 Latin-1 bytes instead of \X\ escapes | student_beginner | [en-gh-encoding-r019](https://github.com/IfcOpenShell/IfcOpenShell/issues/7305) |
| 57 | tr* | Unicode characters in IFC file made OBJ conversion fail: IFCSURFACESTYLE('\X2\00C70130\X0\ZG...') fails OBJ conversion; used to work | OBJ conversion fails on a surface style name with Turkish dotted I and C-cedilla | developer_programmer | [en-gh-encoding-r020](https://github.com/IfcOpenShell/IfcOpenShell/issues/101) |
| 58 | da* | UTF-8 encoding: I use UTF-8 because of AE O AA; values read like V\X\E6gelement; probably other languages too | Danish letters show as \X\E6; request UTF-8 style handling | architect | [en-gh-encoding-r022](https://github.com/ThatOpen/engine_web-ifc/issues/358) |
| 59 | ko* | STEP AP214 export writes raw Korean/Japanese/Chinese characters instead of \X2\ escapes, commercial CAD cannot open it (FreeCAD) | – | developer_programmer | [en-gh-encoding-r030](https://github.com/FreeCAD/FreeCAD/issues/33914) |
| 60 | ko* | IFC metadata is searchable in English but not in Korean (Cesium) | – | developer_programmer | [ko-cesium-r027](https://community.cesium.com/t/ifc-metadata-not-shown-when-it-is-korean/44612) |
| 61 | ja* | Browse External Style fails when the external material name is Japanese (Blender enum limitation) | – | architect | [en-gh-encoding-r029](https://github.com/IfcOpenShell/IfcOpenShell/issues/6496) |
| 62 | en | The latest XbimXplorer fails to load geometry if the property string contains a newline character (Russian address encoded with \X2\) | – | developer_programmer | [en-gh-xbim-others-r008](https://github.com/xBimTeam/XbimEssentials/issues/660) |
| 63 | en | IfcOpenShell failed to load UTF-8 BOM file: Unable to parse IFC SPF header; resaving without BOM works | – | developer_programmer | [en-err-r023](https://github.com/IfcOpenShell/IfcOpenShell/issues/4256) |
| 64 | en | A number of interesting Revit IFC parsing errors: timestamp in header, nested parentheses in list attributes, a string ending in an escaped quote like 8'' (the file is valid, the parser was wrong) | – | developer_programmer | [en-coord-r008](https://forums.buildingsmart.org/t/a-number-of-interesting-revit-ifc-parsing-errors/4605) |
| 65 | en | Decimal , and . for parametric elements: my keyboard uses , as decimal separator; want numpad use | – | architect | [en-gh-encoding-r003](https://github.com/IfcOpenShell/IfcOpenShell/issues/8262) |
| 66 | en | Random IFC GUID for walls at each export: GUIDs of some walls change on every export | – | bim_manager | [de-dach-r007](https://github.com/Autodesk/revit-ifc/issues/109) |
| 67 | en | Room IfcGUID changes on each export (store GUID in parameter): exported the same file twice with identical settings and Room GUIDs differ | – | bim_coordinator | [en-revitifc-guid-r012](https://github.com/Autodesk/revit-ifc/issues/521) |
| 68 | en | Why are GlobalIds not unique across files? 2,578 duplicates among ~1.9M elements across six IFC files | – | developer_programmer | [en-revitifc-guid-r015](https://github.com/Autodesk/revit-ifc/issues/378) |
| 69 | en | Dealing with multiple imports (link) of an updated IFC file: each time Revit generates new shared parameters with different GUIDs for the same Pset names; filters and schedules break | – | bim_coordinator | [en-revitifc-guid-r018](https://github.com/Autodesk/revit-ifc/issues/408) |
| 70 | en | Issue with model groups and IfcGUID: Store IFC GUID parameter doesn't update for grouped objects | – | bim_coordinator | [en-revitifc-guid-r019](https://github.com/Autodesk/revit-ifc/issues/164) |
| 71 | en | Track real changes in IfcDiff: when a tool re-issues GlobalIds the same element shows as one deletion and one addition; want to treat element as unchanged if placement within 5 cm | – | bim_coordinator | [en-ifcos-diff-r022](https://github.com/IfcOpenShell/IfcOpenShell/issues/8412) |
| 72 | en | merge IFCs: could elements with matching GUIDs be overwritten so incremental exports from Revit merge into the main file? | – | bim_coordinator | [en-osarch-guid-r004](https://community.osarch.org/discussion/comment/8352#Comment_8352) |
| 73 | en | GUID valid/invalid: asks if GUID like k0el31... is allowed | – | developer_programmer | [en-val-r013](https://forums.buildingsmart.org/t/guid-valid-invalid/3776) |
| 74 | ja | RevitのUniqueIdとIFCのGUIDが全然違って見えるので、どう対応するのか知りたい。 | UniqueId and IFC GUID look completely different, how do they correspond? | developer_programmer | [p-student-r034](https://qiita.com/Takashi_Kasuya/items/97899d15e7ec0186eecf) |
| 75 | it | ho un IFC ricevuto dal collega, devo modificare le proprieta ma il viewer e solo lettura e i muri sono finiti come proxy, come faccio senza rompere i GUID? | Editing a received IFC: read-only viewer, walls became proxies, how to avoid breaking GUIDs | bim_coordinator | [it-italy-r001](https://biblus.acca.it/problemi-editing-file-ifc/) |
| 76 | ru | Постобработка IFC без Revit: как найти дубли в IFC которых не видно и переслать правки коллеге | Find invisible duplicates and share edits without resending big files (edit journal keyed by GlobalId) | bim_coordinator | [ru-habr-dev-r008](https://habr.com/ru/articles/1100956/) |
| 77 | zh | revit 2020 ifc guid不生成是为什么? | Why are IFC GUIDs not generated in a Revit 2020 export? | bim_coordinator | [zh-zhihu-r007](https://www.zhihu.com/question/625548241) |
| 78 | nl* | FM-toepassing: gebouwbeheer op het model (title); GlobalIds must survive versions | FM app on the as-built model: link assets via GlobalId, maintenance plans, fault reports to ERP work orders | facility_manager | [nl-cobie-r016](https://github.com/OpenAEC-Foundation/open-bim-platform/issues/10) |

`*` = the source or the asker is in that language but the knowledge base stored the paraphrase in English; the text shown is the KB paraphrase (title kept in the original language where the record has one).

Language spread in this table (78 rows): en 35, zh 9, ru 8, it 4, ja 5, es 3, de 3, ko 3, fr 2, nl 2, no 1, pt 1, tr 1, da 1 (the "lang" column shows the record language, which for GitHub issues can differ from the asker's country).

## Ready test prompts

Synthetic. They are curated from the KB's synthetic records (record id in the "type" column); weak or repetitive ones were rewritten to sound like a real person with a deadline or an annoyance. Unless noted, "needs file" means an IFC (or two IFCs) must be loaded.

| # | lang | prompt | type | difficulty | expected behavior |
|---|---|---|---|---|---|
| 1 | en | client says deliver in IFC, doesnt say which. 2x3 or ifc4? what even is coordination view? we're on revit 2023 | understand_concept (en-mea-s011) | easy | Explain 2x3 CV2.0 vs IFC4 RV in plain words; say to confirm EIR/BEP and receiver; give exact Revit setup names; no file needed |
| 2 | ru | подрядчик просит ифс, но не говорит какой. 2х3 или 4? и какой вьюшкой выгружать из ревита | understand_concept (ru-vm-s005) | easy | Compare 2x3 CV2.0, IFC4 RV, 4.3; ask who receives; default 2x3 CV2.0 for broad compatibility, RV where supported |
| 3 | de | AG fordert laut AIA IFC4 Reference View. prüf mal ob die Datei wirklich RV ist und nicht 2x3 oder IFC4x3 | validate_check (de-vm-s010) | medium | Read FILE_SCHEMA and ViewDefinition; confirm IFC4 and ReferenceView; check constituent material sets; note header is a claim |
| 4 | zh | 甲方要求交付IFC2x3，帮我检查一下这个文件的版本和视图定义对不对 | validate_check (zh-vm-s007) | easy | Read header; confirm IFC2X3 and CoordinationView 2.0; list deviations |
| 5 | en | what schema is this file, 2x3 or 4? and does the header say CV2.0 / RV / DTV | query_model_data (en-vm-s001) | easy | Report FILE_SCHEMA, ViewDefinition and authoring app; flag if the view label contradicts content |
| 6 | ja | このIFCのFILE_SCHEMAとエクスポートしたRevitのバージョン教えて | query_model_data (ja-vm-s012) | easy | Return schema, header application and exporter version |
| 7 | en | exported IFC4x3 reference view from revit 2026 but the header says CoordinationView. is the file wrong or just the label? | validate_check (en-gh-revit-ifc-s011) | medium | Read header and schema; explain known exporter header bug (fixed in 2027); do not claim conformance after label edit |
| 8 | en | client wants IFC4 RV. check this export, is it actually RV or is it DTV with advanced breps? need to know before I send it back | validate_check (en-vm-s002) | hard | Detect IfcAdvancedBrep/CSG/parametric profiles, layer sets vs constituent sets, header view; conclude with listed violations and uncertainty |
| 9 | ru | сколько в ифс4 файле элементов с AdvancedBrep? солибри их не видит, нужен список по классам и guid | query_model_data (ru-vm-s004) | medium | Count IfcAdvancedBrep users, group by class, list GlobalIds, suggest re-export or 2x3 |
| 10 | it | ho esportato in ifc4 da archicad ma revit non lo apre, solo collegato. perche? | troubleshoot_import (it-vm-s014) | medium | Check schema and face-set types; explain Open vs Link limits; suggest IFC2x3 or faceted brep |
| 11 | zh | 这个IFC4的模型能不能转成IFC2x3？先告诉我会丢哪些东西，别动原文件 | convert_format (zh-vm-s006) | hard | Check schema, list IFC4-only entities (PolygonalFaceSet, constituent sets), work on a copy, report losses |
| 12 | en | need this 4x3 file in ifc4 for a legacy tool. migrate and tell me whats lost (alignments etc), dont overwrite mine | modify_model_data (en-vm-s015) | hard | Schema-aware migration to a new file; list entities with no IFC4 equivalent (IfcAlignment, IfcPavement); verify output header |
| 13 | es | el ifc que saqué de revit no abre en etabs, dice que falta ENDSEC. qué versión es y está truncado? | troubleshoot_import (es-vm-s008) | medium | Check schema, EOF and ENDSEC, file size sanity, encoding; recommend re-export |
| 14 | en | my ifc wont open, SchemaError unsupported IFC4X3. whats the FILE_SCHEMA in this file and is it ok | validate_check (en-infra-s003) | medium | Read FILE_SCHEMA, compare with IFC4X3_ADD2, say which library build is the issue |
| 15 | en | is this file ifc4 or 2x3? corenet x only takes ifc4 right | validate_check (en-sg-corenetx-s002) | easy | Read header, state version, note IFC+SG expects IFC4, advise re-export if not |
| 16 | en | two exports of the same wall, one RV one DTV. why does one have no layers? compare the materials | compare_versions (en-vm-s003) | hard | Compare IfcMaterialLayerSet vs IfcMaterialConstituentSet and quantities across files; explain storage difference |
| 17 | fr | peux tu me sortir une version ifc2x3 de ce modèle, le sous-traitant n'ouvre pas l'ifc4 | convert_format (fr-vm-s011) | medium | Convert/export to IFC2X3 CV2.0 as a new file, warn about lost features, verify result schema |
| 18 | en | FILE_SCHEMA says IFC4 but I think there are IFC4X3 entities in there. confirm the real schema and list the ones that dont belong | validate_check (en-dev-s009) | hard | Read FILE_SCHEMA, check every entity type against the declared schema, list violations |
| 19 | ko | 레빗에서 IFC4 내보낼때 Reference View랑 Design Transfer View 중에 뭐 써야돼요? | how_to (ko-vm-s013) | easy | Explain RV is the certified common one, DTV unofficial with advanced BReps; recommend RV for coordination |
| 20 | zh | 香港屋宇署BIM要用IFC2x3還是IFC4？Revit要選哪個MVD | how_to (zh-tw-hk-s014) | hard | Must not invent the authority rule; explain typical CV/RV, say to check the authority's current circular and confirm |
| 21 | ru | в ифс названия типов как кракозябры, найди все где имя битое и скажи из какой категории | query_model_data (enc-s001) | medium | Scan Name/ObjectType/property strings for mojibake patterns, list class and Revit category, suggest cause |
| 22 | zh | ifcopenshell读出来的中文是\X2\开头的，怎么转成正常汉字 | troubleshoot_code (enc-s012) | easy | Explain that IfcOpenShell decodes automatically; inspect whether raw escapes appear and show a snippet |
| 23 | ja | IFCを別のビューアで開くとプロパティの日本語が文字化けしてる。ファイル側の問題か確認して | validate_check (enc-s003) | medium | Read raw STEP text, verify \X2\ UTF-16 escapes decode to Japanese, decide whether file or viewer is at fault |
| 24 | tr | ifc dosyasında ğ ü ş harfleri neden \X2\ diye kodlanıyor? bozuk mu? | understand_concept (enc-s015) | easy | Explain STEP Part 21 ASCII-only rule and \X2\ escapes; not corruption |
| 25 | ru | в модели имена вида РЎС‚РѕР№ка - вылечи, перекодируй обратно | modify_model_data (enc-s016) | hard | Detect cp1251/UTF-8 double decoding, convert back, write to a new file, report before/after |
| 26 | en | IfcConvert dies on 'Unexpected A ... Parsing terminated'. scan the file for broken \X2\ \X0\ sequences and non-ascii chars, line numbers pls | troubleshoot_code (en-err-s003) | medium | Scan raw text, report line, entity id and attribute, propose fixes |
| 27 | fr | IfcConvert plante avec 'to_bytes error', y'a des accents dans le header, tu peux corriger le fichier ? | convert_format (fr-err-s010) | medium | Read header, escape non-ASCII as \X2\, rewrite as a copy, verify the conversion |
| 28 | en | some lengths come as text like '2,5' not numbers. list them and tell me if the exporter is set to a european locale | query_model_data (enc-s014) | medium | Find text properties with numeric-looking comma values, count them, suggest IfcReal |
| 29 | ko | 한글 속성값이 깨진 요소 찾아줘. 웹뷰어에서 검색이 안돼 | validate_check (ko-gis-s017) | medium | Detect encoding problems in Korean property strings, list elements, suggest fixes |
| 30 | ru | Текла не открывает ифц, глянь заголовок - там кириллица в пути? какая версия экспортёра и схема | validate_check (ru-dwg-other-s003) | medium | Read FILE_NAME/FILE_SCHEMA, report path, schema, exporter, non-ASCII characters |
| 31 | en | fix the file so all non-latin names get proper \X2\ escaping, save as new file, keep guids | modify_model_data (enc-s009) | hard | Re-serialise with correct escaping, preserve GlobalIds, report count of changed strings |
| 32 | ar | أسماء الغرف بالعربي تظهر علامات استفهام بعد تصدير IFC، شو المشكلة؟ | troubleshoot_viewing (enc-s005) | hard | Check how strings are stored, explain \X2\ escapes, viewer font and right-to-left display |
| 33 | no | æøå blir rare tegn i navnene når jeg leser IFC med ifcopenshell, hvorfor | troubleshoot_code (no-norway-s012) | medium | Explain \X2\ escaping, check source encoding, show how to decode |
| 34 | en | diff says 4000 walls deleted and 4000 added between the two exports but nothing really changed. GUIDs regenerated or what? match them by type + position instead | compare_versions (en-guid-s002) | hard | Check GlobalId overlap, report the regenerated share, match leftovers by class, name/Tag and placement within tolerance, list true changes only |
| 35 | ru | сравни вчерашний и сегодняшний ифс: что добавили, удалили, что поменялось по GUID. guid опять могли поплыть, проверь по имени тоже | compare_versions (ru-guid-s006) | hard | Match by GlobalId, fall back to class + Name/Tag, list deleted with class, level and name, flag GUID churn |
| 36 | de | vergleich mal Stand KW12 und KW14 vom Archicad-IFC, welche Wandtypen wurden geändert? GUIDs sind nicht stabil, glaub ich | compare_versions (de-guid-s008) | hard | Compare IfcWallType definitions and layers, matching types by name when GUIDs differ, list affected instances |
| 37 | zh | 两次导出的IFC，GUID全不一样，帮我按类型和坐标匹配一下，看看到底哪些构件真的改了 | compare_versions (zh-guid-s007) | hard | Detect GUID mismatch, pair by class, name, placement; list truly modified, added, removed |
| 38 | en | any duplicate GlobalIds in this file? the checker complained | validate_check (en-sg-corenetx-s011) | easy | List duplicate GlobalIds across all rooted entities with class and name |
| 39 | fr | vérifie que tous les GlobalId sont valides (22 caractères base64) et qu'il n'y a pas de doublons dans la maquette | validate_check (fr-guid-s011) | medium | Validate length, alphabet and first char 0-3; report invalid and duplicate ids |
| 40 | it | abbiamo copiato il file e ora ci sono GlobalId doppi tra i due modelli, puoi rigenerarli solo per il secondo? | modify_model_data (it-guid-s014) | hard | Find shared GlobalIds, generate new ones for the second file only, report mapping, warn about external references |
| 41 | en | here's a list of GUIDs from open BCF issues. which of them are gone in the new IFC and which changed geometry? | query_model_data (en-guid-s004) | hard | Look up each GUID in the new model, report missing ones, compare placement/geometry for found ones if the old revision is supplied |
| 42 | ja | RevitのUniqueIdからIFCのGUIDを出したい。エクスポートしなくてもできる？ | convert_format (ja-guid-s012) | hard | Explain conversion rules and limits; say the exported GUID may differ for derived entities, links, options |
| 43 | en | how do i make the IFC GUIDs stay the same between exports from revit? contractor keeps complaining their links break every revision | how_to (en-guid-s005) | medium | Explain deterministic GUIDs, current exporter, Store IFC GUID parameter, avoiding recreated elements |
| 44 | pt | o que mudou da revisão anterior pra essa? preciso saber quais elementos já estão no cronograma 4D e foram alterados | compare_versions (pt-guid-s010) | hard | Diff by GlobalId, intersect changed elements with those assigned to schedule tasks |
| 45 | es | revisa si los GlobalId de estos 50 elementos siguen iguales entre la v3 y la v4 del modelo | query_model_data (es-guid-s009) | medium | Look up each id in both files, report present, missing and changed |
| 46 | en | compare rev B and rev C of the architectural model. what was added, deleted or moved? just the list by level, meeting in 20 | compare_versions (en-mea-s004, en-guid-s001) | medium | Match by GlobalId, group per storey; if match rate is low, warn about GUID regeneration and offer fallback |
| 47 | ja | この壁のIFCのGUIDとRevitのIDを一覧にして。卒論で対応表が必要 | convert_format (p-student-s017) | medium | Export GlobalId and Tag/ElementId mapping; note UniqueId vs GUID difference |
| 48 | en | find property values with bad \X2\ encoding or line breaks inside, the file wont load in some tools | validate_check (en-gh-xbim-others-s009) | hard | Scan raw STEP strings for malformed escapes and newlines, report line numbers and entity ids, offer a fix |

## Edge cases and traps for MCP testing in this area

**Versions and MVDs**
- Do not answer "which version should I use?" with one confident answer. A good response gives options plus the question about the receiver or EIR. A bad one says "always IFC4".
- Header is a claim, not proof. Test files where `ViewDefinition` is `CoordinationView` but the schema is `IFC4X3_ADD2`; a file labelled `IFC2X3` containing IFC4-only entities; `FILE_SCHEMA` with quotes or extra schemas (web-ifc once reported IFC2X3 for every file because of string-token handling).
- `IFC4` in `FILE_SCHEMA` covers ADD1, ADD2 and ADD2 TC1. An assistant that says "IFC4 ADD2 TC1" from the header alone is guessing.
- `IFC4X3` vs `IFC4X3_ADD2`: case-sensitive, exact-match logic fails; older RC files differ.
- Never convert by only rewriting the schema string; a tool that claims "converted to IFC2x3" must show what was changed or dropped, and must verify the output header. The original file must stay untouched.
- Local rules (CORENET X, SZ-IFC, Hong Kong BD, SP 333, Moscow AGR) must be flagged as "check the current official document"; do not invent clause numbers. The KB itself holds some of these only as synthetic expectations.
- Revit capability traps: "export IFC4.3 from Revit" may be limited; Open vs Link IFC; DTV is labelled unofficial; Revit 2026 vs 2027 exporter behave differently.
- Receiver-specific claims (what Solibri, Navisworks, BIM 360 or ETABS can read) are time-dependent; the assistant should say "check current docs" rather than assert.

**Encoding and text**
- The same text appears in three forms: decoded Unicode, raw `\X2\...\X0\`, and real mojibake. A test should include all three and check that the assistant tells them apart.
- Both `\X\E9` and `\X2\00E9\X0\` are valid and mean the same; an assistant should not call the first "corrupt".
- Lowercase hex digits inside `\X2\` (a-f), doubled backslashes, a single backslash in a Windows path in `FILE_NAME`, a UTF-8 BOM, newline inside an escaped run, form feed or `\X\1F` control characters, apostrophe doubling (`O''Brien`), strings ending in `\X0\` missing: each broke at least one real parser.
- Characters outside the BMP (`\X4\`) and Turkish dotted/dotless I (culture-sensitive uppercasing broke ifcXML reading).
- Output side: an MCP server that returns names to the user can itself garble them (console code page, JSON ASCII escaping) or can write raw UTF-8 into STEP; test the round trip: write a Cyrillic name, save, reopen in another reader.
- Numbers as text: `'2,5'` stored as IfcText with a decimal comma; Python scripts under a comma locale writing `0,5`.
- Environment is not the file: non-ASCII file paths, Windows UI language, ANSI vs UTF-8 mapping files.
- A repair tool must keep GlobalIds, write a copy, and report the count of changed strings.

**GUIDs and change tracking**
- Before claiming "N elements were deleted", check the share of shared GlobalIds. If it is very low, the real finding is "ids were regenerated", and the right action is fallback matching with confidence labels.
- Fallback matching is heuristic: type + name/Tag + placement/bounding box + geometry hash. Identical repeated elements (rows of identical columns, duplicates stacked on each other) create ambiguous matches; the assistant must mark them as uncertain, not silently pair them.
- Do not compare by STEP id (`#123`). The same number refers to different entities in the next export.
- Same GlobalId in two different project files is expected after copying a Revit file; the same GlobalId twice inside one file is a defect.
- A user asking to "regenerate duplicates" must be warned about external references; regenerating all IDs when only the copy needed it is a destructive error. A user who says "keep guids" must get them kept.
- Valid GlobalId rules: 22 characters, IFC base-64 alphabet, first char 0-3, case-sensitive. Standard base64 decoding gives wrong bytes. Some tools (IfcOpenShell `by_guid`) fail on charset-legal but invalid ids.
- A comparison request with only one file loaded: the assistant should ask for the second file, not invent a baseline. A "compare to last week's" request may refer to a file the assistant cannot see.
- Revit-specific ids: UniqueId, ElementId, IfcGUID parameter and the exported GlobalId are four different things; linked-model export, groups, design options and phases deliberately create new GUIDs.
- Diff completeness: say what was compared (attributes, psets, geometry, relationships). A diff that silently skips geometry will report "no changes" for a thickened wall.
- Large models: comparing two 200 MB files can take many minutes; the assistant should warn or offer a class/storey filter.

## Related docs

- [What IFC is: history, versions, MVDs, certification](../../01_ifc_basics/01_what_is_ifc_and_versions.md)
- [Inside an .ifc file: header, schema id, GlobalId, string escapes](../../01_ifc_basics/02_ifc_file_anatomy.md)
- [Materials, styles, types (layer sets vs constituent sets)](../../01_ifc_basics/07_materials_classification_types_styles.md)
- [Revit IFC export reference (setups, Store IFC GUID, known problems)](../../03_software/revit/ifc_export_reference.md)
- [Revit IFC import and link reference (Open vs Link, IFC4.3 header issue)](../../03_software/revit/ifc_import_link_reference.md)
- [Viewers, checkers, CDE and converters](../../03_software/viewers_checkers_cde_converters.md)
- [Authoring tools and their IFC settings](../../03_software/authoring_tools_ifc.md)
- [Open-source libraries and toolkits (IfcOpenShell, web-ifc, xBIM)](../../04_open_source/libraries_and_toolkits.md)
- [Glossary (multilingual)](../../08_glossary/glossary_multilingual.md) and [abbreviations](../../08_glossary/abbreviations.md)
- Sibling topic file: [Materials, colours, layers; spaces, rooms, areas, zones, systems](./materials_spaces_zones.md)
- Other topic files: [Revit export and class mapping](./revit_export_and_class_mapping.md), [Import and interoperability](./import_and_interoperability.md), [Validation, IDS and model checking](./validation_ids_model_checking.md), [Coordination, clash, BCF, CDE](./coordination_clash_bcf_cde.md)
