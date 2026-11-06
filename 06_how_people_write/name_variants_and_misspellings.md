# Name variants and misspellings: how people spell IFC, Revit and the tools around them

**Audience:** a tester (or an LLM acting for one) with no BIM background who must write requests that look like a real colleague typed them, and must judge whether an IFC / Revit MCP server recognised the thing the user meant.
**Companions:** [jargon_slang_dictionary.md](jargon_slang_dictionary.md) (what the slang words mean), [style_guide.md](style_guide.md) (register, length, tone; its section 8 is the short version of this file), [anti_patterns_llm_questions.md](anti_patterns_llm_questions.md) (what invented questions look like), [../08_glossary/glossary_multilingual.md](../08_glossary/glossary_multilingual.md) (standard terms), [../08_glossary/abbreviations.md](../08_glossary/abbreviations.md).
**Data basis:** the records in `research_raw/wave1/` (3,592 records at the time of writing: 2,304 real, 1,288 synthetic, per `kb.py stats`) and the "How people write" sections of the cell reports. A scripted scan of the JSONL text fields supplied the counts below. No `wave2` data existed when this file was written.

---

## In plain words

Nobody types "Industry Foundation Classes" or "Autodesk Revit". People type **IFC**, **ifc**, **Ifc**, **ифс**, **ifc文件**, and they type **Revit**, **revit**, **REVIT**, **Ревит**, **레빗**. They glue a version number on without a space (`IFC4x3`, `REVIT2023`), copy a class name from a program (`IfcBuildingElementProxy`) or from a raw file line (`IFCBUILDINGELEMENTPROXY`), and sometimes drop a letter (`IfcBuildingElementProxi`, `Qto_SpaceBaesQuantities`).

Why this matters for testing: an MCP server (a plug-in that lets an AI assistant read and change a model) has to work out what the person meant even when the spelling is sloppy. A good test therefore uses some of these variants, but **only in places where a human would really be sloppy**. A request that is full of random typos looks fake, and a request with a typo inside the one token the test depends on measures typo tolerance, not the feature under test.

If you only read one thing: **product names and casing vary freely; class names, property names, numbers and IDs are the part you keep exact.**

## How to read the tables

Every row has an evidence tag. Do not treat all rows as equally real.

| Tag | Meaning | How much to trust it |
|---|---|---|
| **R** | The spelling appears in a **real** record. Titles of up to 20 words are verbatim; question text is a paraphrase made by the research agent, so a typo or casing in the body may have been tidied (or, for Cyrillic names, may have been written by the agent in the asker's register). The record id links to its `source_url`. | High for titles, medium for body text. |
| **N** | Named in the "How people write" note of a cell report as seen in real sources, but no single record is traceable. The report is linked. | Medium. |
| **S** | Appears **only in synthetic prompts** (written by a research agent to imitate chat style). The synthetic id is linked to its file. | Low to medium: plausible, not proven. Good for generating tests; do not describe it as "how users really write". |
| **K** | Standard spelling from the reference docs or general domain knowledge, not observed as a variant in the data. | High as a canonical form. |
| **P** | **Plausible but not observed anywhere** in the data. Suggested by the author of this file from keyboard, phonetic or font logic. | Low. Use rarely, and label such test cases "plausible phrasing, not observed". |

Example fragments are at most 12 words. Synthetic fragments are never presented as quotes of a person.

---

## 1. What the data says about how often (rates)

These numbers come from a scripted count over the record text (title, paraphrase, synthetic prompt). They are **lower bounds for roughness** in real data, because paraphrases normalise spelling and the research notes were not coded systematically (the same caveat as in [style_guide.md](style_guide.md)).

| Observation | Numbers | Tag | Reading |
|---|---|---|---|
| Real records whose notes flag a typo or misspelling | 39 of 2,304 (about 1.7%); a wider net (typo, caps, lowercase, transliteration) catches 65 (about 3%), of which 59 are English | R | Typos are visible but rare; they sit mostly in titles by non-native English writers. |
| Standalone "IFC" token in real English text | `IFC` in about 864 records, `ifc` in about 138, `Ifc` in about 47 | R | Roughly 1 in 8 real English records use lowercase `ifc`. |
| Same token in real Chinese records | `IFC` about 93, `ifc` about 22 | R | About 1 in 5 Chinese records use lowercase. |
| Same token in real Russian records | `IFC` about 82, `ifc` about 5, Cyrillic `ифс`/`ифц` **0** | R | Real Russian text keeps Latin `IFC`. The Cyrillic spoken forms were reported by researchers but never appear in record text. |
| Same token in synthetic English prompts | `ifc` about 163, `IFC` about 38 | S | The synthetic set is far more lowercase than the real set. Do not copy this ratio into new tests. |
| Same token in synthetic Chinese prompts | `ifc` about 58, `IFC` about 21 | S | Same exaggeration. |
| Cyrillic `ифс` / `ифц` | 59 synthetic Russian prompts, 0 real records | S, N | Plausible spoken/chat form. See [section 4](#4-the-word-ifc-itself). |
| "Revit" casing, real English | `Revit` about 326, `revit` about 29, `REVIT` about 5 | R | Lowercase is about 8%. |
| "Revit" casing, real Chinese | `Revit` about 57, `revit` about 17, `REVIT` about 6 | R | Lowercase about 21%. |
| "Revit" casing, synthetic English | `revit` about 73, `Revit` about 9 | S | Again exaggerated lowercase. |
| Mixed-script homoglyph (Cyrillic letter inside "IFC") | 1 real title in 2,304 | R | "Lecture 8.4. Export to IFС" with a Cyrillic С. A curiosity, not a pattern. |
| ASCII-fied umlauts and dropped accents | German "fuer", "geaendert"; Spanish "por que", "como exporto"; Portuguese "nao" | S | Only in synthetic prompts here; real Spanish notes mention missing accents ([es-latam report](../research_raw/wave1/es/es-latam.md)). |

Take-away for generation: in **real** data the spelling of the key tokens is mostly canonical (`IFC`, `Revit`, `Archicad`), with a minority of lowercase and a thin tail of typos. The **synthetic** records already over-use lowercase; adding more noise on top makes them look worse, not better.

---

## 2. Quick lookup: canonical form to the variants worth using

Use this as a menu. Pick one variant per prompt at most. "Weight" is a suggestion for casual chat prompts, not a measured rate.

| Canonical | Common variants (use freely) | Rare variants (use sparingly) | Do not use unless testing robustness |
|---|---|---|---|
| IFC | `ifc`, `Ifc`, `IFCs`, `ifcs`, `IFC-file`, `.ifc` | `ифс`, `ифц` (RU), `ifc文件` (ZH), `IFC's` (ES, EN) | `AIFC`, `IFS`, `IFK`, `ИФК`, `IFС` with a Cyrillic С |
| IFC4 | `IFC4`, `IFC 4`, `ifc4`, `IFC4 RV`, `IFC4 Reference View` | `ифс4` (RU) | `IFC 4.0`, `IFC four` |
| IFC2x3 | `IFC2x3`, `IFC 2x3`, `IFC2X3`, `ifc2x3`, `2x3`, `2x3 CV2`, `IFC2x3 CV2.0` | | `IFC2*3` (real but a slip), `ifc3X2` (real but a slip) |
| IFC4.3 | `IFC4.3`, `IFC 4.3`, `IFC4x3`, `IFC4X3`, `ifc4x3`, `IFC4x3 add2`, `IFC4X3_ADD2` | `4.3 ADD2` | `IFC 5`, `IFC5` when the person means 4.3 |
| Revit | `Revit`, `revit`, `Revit 2024`, `REVIT 2024`, `rvt` (file) | `Ревит` / `ревит` (RU), `레빗` (KO) | `Revitt`, `Revet`, `Rvit`, `レビット` |
| Archicad | `Archicad`, `ArchiCAD`, `ARCHICAD`, `archicad` | `ArchiCad`, `Архикад` (RU), `아키캐드` (KO) | `Archi-cad`, `ArchiKAD` |
| Navisworks | `Navisworks`, `navisworks`, `Navis` | `Навис` (RU), `нависворкс` (RU, N) | `Naviswork`, `NavisWorks Manage` for a generic viewer |
| Solibri | `Solibri` | `solibri`, `Солибри` | `Soliberi`, `Solibry` |
| Tekla | `Tekla`, `tekla` | `Текла` (RU), `TEKLA` (ZH-TW blog) | `Teckla` |
| BlenderBIM / Bonsai | `Bonsai`, `BlenderBIM`, `blenderbim`, `BBIM` | `Blender BIM`, `BlenderBim` | `BlenderBin` |
| IfcOpenShell | `IfcOpenShell`, `ifcopenshell` | `IFCOpenShell`, `IFCopenshell`, `IfcOpenshell` | `IfcOpenShel` |
| BCF | `BCF`, `bcf`, `BCFs` | `бцф` (RU, S) | `BCF-XML` for a plain issue list |

---

## 3. A few real examples to anchor the idea

Short verbatim-or-near-verbatim fragments. Links go to the real source. The point is the *spelling*, not the question.

| Spelling feature | Fragment (original language) | Gloss | Tag, source |
|---|---|---|---|
| Letter swap inside a property-set name | "Qto_SpaceBaesQuantities" | Typo in the standard name "Qto_SpaceBaseQuantities". | R [en-spaces-r013](https://github.com/Autodesk/revit-ifc/issues/529) |
| Dropped last letter in a class name | "Separating IfcBuildingElementProxi in parts" | "Proxi" for "Proxy". | R [en-gh-proxy-r033](https://github.com/IfcOpenShell/IfcOpenShell/issues/6299) |
| Plural of a class name | "How to find out what a IfcBuildingElementProxies is" | Invented plural of a class name. | R [en-bsforum-r016](https://forums.buildingsmart.org/t/5130) |
| STEP-style UPPERCASE class in a title | "IFCELEMENTASSEMLBY and openings" | Raw-file casing plus a letter swap (ASSEMBLY). | R [en-openings-r032](https://forums.buildingsmart.org/t/ifcelementassemlby-and-openings/4143) |
| Version label with a typed `*` | "Merging IFC2*3 Elntities in a IFC4 file" | `2*3` for `2x3`, "Elntities" for "Entities". | R [en-bsmart-r015](https://forums.buildingsmart.org/t/merging-ifc2-3-elntities-in-a-ifc4-file/2846) |
| Version label reversed | "Error when import file of ifc3X2 into blenderbim" | `3X2` for `2X3`; lowercase product name. | R [en-err-r034](https://forums.buildingsmart.org/t/error-when-import-file-of-ifc3x2-into-blenderbim-do-the-shape-or-filesize-have-some-limits/3836) |
| Lowercase version label in a title | "Question regarding ifc4x3 support" | The body shows the exact schema name was required: `IFC4x3` was not found. | R [en-civil-infra-r008](https://github.com/IfcOpenShell/IfcOpenShell/issues/2382) |
| Misspelled product | "Urgent, Can we use Cobiee plugin with bimserver1.2" | `Cobiee` for `COBie`. | R [en-cobie-r026](https://github.com/opensourceBIM/COBie-plugins/issues/2) |
| Misspelled product (different tool) | "How to generate an OpenCeepy finite element model" | `OpenCeepy` for OpenSees. | R [en-struct-r019](https://github.com/IfcOpenShell/IfcOpenShell/issues/5931) |
| Misspelled topic word | "Georefrancing added Meters as a unit" | Georeferencing. | R [t-coordinates-rx016](https://github.com/IfcOpenShell/IfcOpenShell/issues/6182) |
| Misspelled topic word | "Georeferening IFC2x3, where are my ePset values?" | Georeferencing; `ePset` is community slang. | R [en-coord-r040](https://community.osarch.org/discussion/comment/29556/) |
| English plural apostrophe in Spanish | "Problemas con IFC's" | Problems with IFCs. | R [es-spain-r001](https://forums.autodesk.com/t5/revit-architecture-forum/problemas-con-ifc-s/td-p/10189111) |
| All caps and a typo (Spanish) | "SOPOTARÁ ARCHIVOS IFC?" | Typo for "soportará": will it support IFC files? | R [es-latam-r001](https://github.com/ingelibre/ingetrazo/issues/1033) |
| Caps product name in a title | "REVIT2023 - Fail export when change language." | No space between product and year. | R [en-err-r008](https://github.com/Autodesk/revit-ifc/issues/718) |
| Caps product name and class | "REVIT 2019 LT: IFC Export - IFCSpaces are missing" | `IFCSpaces`: raw-file prefix plus English plural. | R [en-autodesk-revit-export-r015](https://forums.autodesk.com/t5/revit-architecture-forum/revit-2019-lt-ifc-export-ifcspaces-are-missing/td-p/8424409) |
| Title-case "Ifc" | "Ifc export in 2027 - mapping parameters severely lacking" | The frustrated-verdict title keeps a mixed-case `Ifc`. | R [en-autodesk-revit-export-r008](https://forums.autodesk.com/t5/revit-architecture-forum/ifc-export-in-2027-mapping-parameters-severely-lacking/td-p/14229702) |
| Lowercase title, no punctuation | "whats the root cause of grey MEP-components in IFC" | Missing apostrophe, lowercase start. | R [en-gh-revit-ifc-r040](https://github.com/Autodesk/revit-ifc/issues/579) |
| Chinese: no spaces, lowercase | "ifc导入revit后三维不可见" | After importing IFC into Revit, nothing is visible in 3D. | R [zh-revit-export-r001](https://zhidao.baidu.com/question/341569640619976845.html) |
| Taiwan: caps product names | "[IFC]REVIT匯入IFC時需注意的事項" | Things to watch when importing IFC into Revit; Taiwanese verb 匯入. | R [zh-tw-hk-r001](https://housegear.pixnet.net/blog/posts/3042268210) |
| Russian: Latin names inside Cyrillic title | "Экспорт из Tekla в Revit" | Real forum title keeps Latin product names. | R [ru-dwg-other-r001](https://forum.dwg.ru/showthread.php?t=146029) |
| Russian: Latin stem plus Cyrillic ending | "IFC-модели", "IFC-выгрузка" | IFC models, IFC export. | R [ru-autodesk-telegram-r009](https://habr.com/ru/companies/pik_digital/articles/1057314/) (and r027) |
| Cyrillic С inside "IFC" | "Экспорт в IFС связь" (third letter is Cyrillic) | Export to IFC, link. | R [ru-autodesk-telegram-r032](https://www.youtube.com/watch?v=VPlQf3fv908) |

---

## 4. The word "IFC" itself

| Variant | Where it shows up | Tag, source | Notes for tests |
|---|---|---|---|
| `IFC` | The default everywhere, including all languages in Latin script. | R (hundreds); K | Use as the base. |
| `ifc` | English issue titles, Chinese blogs, chat style in every language. | R [zh-revit-export-r001](https://zhidao.baidu.com/question/341569640619976845.html), [en-gh-revit-ifc-r040](https://github.com/Autodesk/revit-ifc/issues/579) | The most natural variant for a casual prompt. |
| `Ifc` | Titles of the form "Ifc export ...", also class-name style (`IfcWall` means the class, not the format). | R [en-autodesk-revit-export-r024](https://forums.autodesk.com/t5/revit-mep-forum/ifc-export-ducts-and-pipes/td-p/12370919), [en-autodesk-revit-export-r008](https://forums.autodesk.com/t5/revit-architecture-forum/ifc-export-in-2027-mapping-parameters-severely-lacking/td-p/14229702) | Ambiguous with the entity prefix: "list all Ifc" is not a valid class. |
| `IFCs`, `ifcs`, `IFC's` | Plural for "several IFC files". The apostrophe form is a Spanish-forum habit. | R [en-autodesk-revit-import-r005](https://github.com/Autodesk/revit-ifc/issues/566) shows plural `IFCs` as a group; R [es-spain-r001](https://forums.autodesk.com/t5/revit-architecture-forum/problemas-con-ifc-s/td-p/10189111); S [en-navis-acc-s012](../research_raw/wave1/en/en-navis-acc.jsonl) "two ifcs, are there walls in both" | Good way to test "several files" handling. |
| `IFC file`, `IFC model`, `ifc-file`, `IfcFile` | `IfcFile` is a code object in IfcOpenShell and xBIM, not a plain word. | R [en-dev-r006](https://github.com/IfcOpenShell/IfcOpenShell/issues/4009) (developer voice) | Developers write `IfcFile`; coordinators write "the IFC". |
| `IFC-Export`, `IFC exportieren` | German blogs mix a hyphenated compound with the English noun. | R [de-arch-r012](https://community.graphisoft.com/t5/Modellierung/IFC-Export-aus-ArchiCAD-f%C3%BCr-Revit-MEP/m-p/544905) (German compound), [en-blogs-linkedin-r009](https://bim-me-up.com/revit-typenparameter-nach-ifc-exportieren/) | Compound forms "IFC-Datei", "IFC-Modell" are expected in German but were not seen as exact strings in the data (K). |
| `file IFC`, `modello IFC`, `archivos IFC`, `maquette IFC` | Romance languages put the noun first and keep `IFC` as a Latin acronym. | R [it-italy-r001](https://biblus.acca.it/problemi-editing-file-ifc/), [es-latam-r001](https://github.com/ingelibre/ingetrazo/issues/1033), [fr-arch-r032](https://www.ge.ch/utiliser-bim-building-information-modeling/je-prepare-maquette-bim-autorisation-construire) | `IFC` is never translated. |
| `ifc-filen`, `IFC-bestand` | Nordic and Dutch compounds. | S [no-norway-s016](../research_raw/wave1/no/no-norway.jsonl); K for the Dutch form | One compound per prompt is enough. |
| `ифс`, `ифц`, `ифс4` | Spoken Russian: "if-ess" (ИФС), a variant ending in Ц, and a version glued on. | S (59 synthetic prompts, e.g. [ru-arch-s010](../research_raw/wave1/roles/p-architect.jsonl), [ru-dwg-other-s003](../research_raw/wave1/ru/ru-dwg-other.jsonl), [ru-vm-s004](../research_raw/wave1/topics/t-versions-mvd.jsonl)); N [ru-dwg-other report](../research_raw/wave1/ru/ru-dwg-other.md) "ифс/ифц", [ru-habr-dev report](../research_raw/wave1/ru/ru-habr-dev.md) "ифс (spoken IFC)" | Very natural in Russian chat. Not seen in any real record text, so label it "plausible". |
| `IFC-модели` | Latin stem with a Cyrillic suffix after a hyphen. Cases are attached to the Latin word with a hyphen. | R [ru-autodesk-telegram-r009](https://habr.com/ru/companies/pik_digital/articles/1057314/) | This is how formal Russian writes it; informal Russian drops the hyphen and uses `ифс`. |
| `IFС` (Cyrillic С) | A copy-paste or keyboard-layout accident in a course title. | R [ru-autodesk-telegram-r032](https://www.youtube.com/watch?v=VPlQf3fv908) | One in 2,304 real records. A string-match on `IFC` fails on it. Only for deliberate robustness tests. |
| `ifc文件`, `IFC文件`, `IFC格式`, `IFC模型`, `IFC标准` | Chinese: no space between Latin and Chinese; 文件 (file), 格式 (format), 模型 (model). | R [zh-csdn-dev-r022](https://blog.csdn.net/pumbkin/article/details/141029954), [zh-zhihu-r034](https://ask.csdn.net/questions/8391346) | Natural. |
| `IFC檔` | Taiwan: 檔 for "file". | R [zh-tw-hk-r007](https://dbadgp.gov.taipei/DownFiles/Login/使照竣工模型上繳操作手冊.pdf), S [zh-tw-hk-s003](../research_raw/wave1/zh/zh-tw-hk.jsonl) | Use with Traditional characters. |
| `工业基础类` | The Chinese long name of IFC (Industry Foundation Classes). | N [zh-csdn-dev report](../research_raw/wave1/zh/zh-csdn-dev.md) | Textbook, rarely used in questions. |
| `IFC出力`, `IFCに出したら` | Japanese: 出力 and 書き出し both mean "export"; IFC stays Latin. | R [ja-arch-r035](https://note.com/iu_bimstudio_n/n/nf41bb9e91025); N [ja-japan report](../research_raw/wave1/ja/ja-japan.md) | `IFC` is not written in katakana (アイエフシー) anywhere in the data. |
| `ifc에`, `IFC 파일` | Korean: the Latin acronym takes the particle directly (`ifc에`, `ifc를`). | S [ko-korea-s001](../research_raw/wave1/ko/ko-korea.jsonl), [ko-korea-s014](../research_raw/wave1/ko/ko-korea.jsonl) | Real Korean posts in the data are institutional; casual forms are assumptions. |
| `AIFC` | A guess: "A" prefixed, or the Apple audio format AIFC. | P (not in the data) | Note: AIFC is a real audio file extension, so a tool may reasonably reject it. |
| `IFS`, `IFK`, `ИФК`, `айфс` | Slip or phonetic respelling. `IFS` is also a company name (K). | P (not in the data) | Only for a "typo tolerance" test with a clear surrounding context ("the ifs file from Archicad"). |

Two reminders:

- **Never test with a bare variant and no context.** "send me the ifs" is not a BIM request. Put the variant next to a verb and an object a modeller would use (open, export, count proxies, link).
- IFC is **not translated** in any language. People translate the words around it ("file", "model", "export"), not the acronym.

---

## 5. Version labels (the most common source of confusion)

People abbreviate the edition (IFC2x3, IFC4, IFC4.3), the *view* (Coordination View 2.0, Reference View, Design Transfer View) and the *addendum* (TC1, ADD2) in a dozen ways. The file itself stores a fixed identifier (`FILE_SCHEMA`): `IFC2X3`, `IFC4`, `IFC4X3_ADD2` (see [../01_ifc_basics/01_what_is_ifc_and_versions.md](../01_ifc_basics/01_what_is_ifc_and_versions.md)). A server should accept all spoken forms and report the stored identifier.

| What the person means | Spellings seen | Tag, source | Stored identifier (K) |
|---|---|---|---|
| IFC2x3 | `IFC2x3`, `IFC 2x3`, `IFC2X3`, `ifc2x3`, `Ifc2x3`, `2x3`, `IFC2x3 TC1`, `IFC2x3 CV2`, `IFC2x3 Coordination` | R [de-dach-r006](https://github.com/Autodesk/revit-ifc/issues/530); R [en-gh-thatopen-r011](https://github.com/ThatOpen/engine_web-ifc/issues/451) "IFC 2x3"; R [en-dev-r026](https://github.com/ThatOpen/engine_web-ifc/issues/2302) "IFC2X3"; S [fr-clash-s013](../research_raw/wave1/topics/t-clash-bcf.jsonl) "ifc2x3" | `IFC2X3` |
| IFC2x3, mistyped | `IFC2*3`, `ifc3X2` | R [en-bsmart-r015](https://forums.buildingsmart.org/t/merging-ifc2-3-elntities-in-a-ifc4-file/2846), R [en-err-r034](https://forums.buildingsmart.org/t/error-when-import-file-of-ifc3x2-into-blenderbim-do-the-shape-or-filesize-have-some-limits/3836) | `IFC2X3` |
| IFC4 | `IFC4`, `IFC 4`, `ifc4`, `IFC4 Reference View`, `IFC4 RV`, `IFC4RV`, `IFC4 DTV`, `IFC4 export` | R [en-autodesk-revit-export-r033](https://forums.autodesk.com/t5/revit-architecture-forum/revit-ifc4x3-export-incorrect-space-boundaries/m-p/14048745); R [en-revit-r038](https://github.com/Autodesk/revit-ifc/issues/96) "IFC4RV"; S [it-italy-s011](../research_raw/wave1/it/it-italy.jsonl) "IFC4 RV" | `IFC4` |
| IFC4 in Russian chat | `ифс4`, `IFC4`, "2х3 или 4" | S [ru-vm-s004](../research_raw/wave1/topics/t-versions-mvd.jsonl) `ифс4`; S [ru-autodesk-telegram-s015](../research_raw/wave1/ru/ru-autodesk-telegram.jsonl) "2х3 или 4, CV2 или RV" | `IFC4` |
| IFC 4.3 | `IFC4.3`, `IFC 4.3`, `IFC4x3`, `IFC4X3`, `Ifc4x3`, `ifc4x3`, `IFC 4x3`, `IFC 4x3 add2`, `IFC4X3_ADD2`, `IFC4.3 ADD2` | R [en-civil-infra-r002](https://github.com/IfcOpenShell/IfcOpenShell/issues/4921); R [en-civil-infra-r008](https://github.com/IfcOpenShell/IfcOpenShell/issues/2382) lowercase; R [en-gh-thatopen-r020](https://github.com/ThatOpen/engine_web-ifc/issues/1171) "IFC 4x3 add2"; R [en-bsforum-r017](https://forums.buildingsmart.org/t/5133) "Ifc4x3 (add2)" | `IFC4X3_ADD2` (Add2 is the officially published 4.3.2.0 edition) |
| "IFC4.3" and "IFC4x3" spoken as different things | The version-spelling mess is itself a topic: "IFC 4.3 vs IFC4X3". | N [t-versions-mvd report](../research_raw/wave1/topics/t-versions-mvd.md) "Spelling traps seen" | Three meanings: RC4, 4.3.0.0, 4.3.2.0 (K) |
| IFC 5 | `IFC 5`, `IFC5`, `Ifc5D` (that last one is **5D cost**, not version 5) | R [en-gh-ifcos-r013](https://github.com/IfcOpenShell/IfcOpenShell/issues/6616) `Ifc5D`; R [it-italy-r011](https://biblus.acca.it/conversione-modello-bim-in-ifc5/) `IFC5`; `ifc5d` is a module name in IfcOpenShell (R [en-qto-r012](https://github.com/IfcOpenShell/IfcOpenShell/issues/6570)) | IFC5 exists only as an alpha (JSON-based "IFCX"), not a production edition (see [../01_ifc_basics/01_what_is_ifc_and_versions.md](../01_ifc_basics/01_what_is_ifc_and_versions.md)); a test that says "IFC5" should expect a clarification. |
| Views (MVD) | `CV2`, `CV2.0`, `RV`, `Reference View`, `DTV`, `Design Transfer`, `RVArch` | R [en-geom-r010](https://github.com/Autodesk/revit-ifc/issues/763), R [ru-autodesk-telegram-r031](https://iek-digital.ru/upload/iblock/685/4jzi0mt4ob86xb78imiswfg6dngrrots/Instruktsiya-po-eksportu-IFC-dlya-REVIT.pdf) (Russian PDF using CV2.0) | These are views, not editions. |
| Addenda | `ADD2`, `add2`, `TC1`, `tc1` | R [en-civil-infra-r010](https://github.com/IfcOpenShell/IfcOpenShell/issues/4565), R [en-bsforum-r017](https://forums.buildingsmart.org/t/5133) | `_ADD2` suffix only for 4.3 identifiers. |
| Country flavours | `IFC+SG`, `IFC-SG`, `ifc-sg`, `IFCSG`, `ifc+sg`; `SZ-IFC`; `IFC0000101` (portal error code) | R [en-sg-corenetx-r003](https://github.com/noddlesskcho/IFC-Repair-Studio), R [en-sg-corenetx-r005](https://github.com/noddlesskcho/IFCSG-Parameter-Consolidator), R [en-sg-corenetx-r014](https://github.com/samsonleegh/revit-coach), R [zh-lightweight-review-r001](https://zhuanlan.zhihu.com/p/673078056) (SZ-IFC, Shenzhen); N [en-sg-corenetx report](../research_raw/wave1/en/en-sg-corenetx.md) says "IFC+SG" and "IFC-SG" are both used | Singapore and Shenzhen submission profiles. Not separate schema editions. |

A real tool log shows why exact spelling can matter: a person asked about `schema_by_name IFC4x3` and the library answered "No schema named IFC4x3" ([en-civil-infra-r008](https://github.com/IfcOpenShell/IfcOpenShell/issues/2382)). An assistant that forwards the user's loose spelling straight to a library will fail the same way. The assistant should **normalise** before calling.

---

## 6. File extensions and packaging

| Thing | Spellings seen | Tag, source | Notes |
|---|---|---|---|
| IFC file | `.ifc`, `.IFC`, "an ifc" | R [en-autodesk-revit-import-r021](https://github.com/Autodesk/revit-ifc/issues/710); R [en-dynamo-pyrevit-r036](https://discourse.pyrevitlabs.io/t/ifc-setup-loading-fails/9920) `.IFC` | Extension casing varies on Windows. |
| Compressed IFC | `.ifczip`, `ifcZIP`, `ifczip`, `IFCZIP`, "zipped ifc" | R [en-bsforum-r046](https://forums.buildingsmart.org/t/1957), [es-spain-r029](https://forums.autodesk.com/autodesk/attachments/autodesk/revit-acc-navisworks-forum-es/19931/1/Exportar%20IFC.pdf) `ifcZIP`, [en-dynamo-pyrevit-r004](https://forum.dynamobim.com/t/ifc-export-settings-ifcfiletype/91626); S [pt-fs-s010](../research_raw/wave1/topics/t-file-size.jsonl) "ifc, ifczip e ifcxml" | `.ifczip` in the file system, `ifcZIP` in the standard text. |
| XML flavour | `ifcXML`, `IfcXml`, `IfcXML`, `IFCXML`, `ifcxml` | R [de-dach-r027](https://www.bimdeutschland.de/bim-deutschland/faq), [en-gh-xbim-others-r003](https://github.com/xBimTeam/XbimEssentials/issues/670), [t-versions-mvd-rx003](https://community.osarch.org/discussion/3150/free-standalone-revit-to-ifc-ifc2x3-ifc4-ifc4-3-ifcxml-conversion-without-revit-and-autodesk) | Casing of the second half varies. |
| JSON flavour | `IFC JSON`, `ifcJSON`, `IFC+JSON` | R [en-bsi-gis-r009](https://forums.buildingsmart.org/t/the-future-of-ifc-for-urban-design-planning-development/3916), [en-dynamo-pyrevit-r038](https://discourse.pyrevitlabs.io/t/pyrevit-cli-problem-with-creating-new-family-instance-in-opened-ifc-file/2935) | Rare in practice. |
| Revit project | `.rvt`, `RVT`, `rvt`, "the native file" (ES: `nativo`) | R [en-aimcp-r043](https://github.com/bimwright/rvt-mcp); N [es-latam report](../research_raw/wave1/es/es-latam.md) "nativo" | `rvt` stands for the project file, `rfa` for a family, `rte` for a template (K). |
| Navisworks | `.nwc`, `.nwd`, `NWC`, `NWD` | R [ru-autodesk-telegram-r028](https://t.me/s/bimacad?before=557), [en-dynamo-pyrevit-r015](https://forum.dynamobim.com/t/objects-created-using-dynamo-is-not-exported-to-ifc/16102) | `nwc` is the cache export, `nwd` the published file. |
| Archicad project | `pln` | R [zh-revit-export-r005](https://zhidao.baidu.com/question/593298625.html) "archicad的pln文件" | |
| BCF | `BCF`, `bcf`, `BCFs`, `BCF zip`, `.bcfzip` | R [en-clash-r018](https://github.com/LTplus-AG/ifc-lite/issues/4099); S [ja-japan-s008](../research_raw/wave1/ja/ja-japan.jsonl) "BCFにして出して" | People use "BCF" for any issue list. |
| That Open fragments | `.frag` | R [en-gh-thatopen-r004](https://github.com/ThatOpen/engine_web-ifc/issues/1774) | Developer-only. |

---

## 7. Class names, property sets, IDs and export keys

### 7.1 Three ways the same class name appears

| Form | Where it comes from | Examples | Tag |
|---|---|---|---|
| CamelCase `IfcWall` | Copied from a viewer, the schema documentation, code. | `IfcBuildingElementProxy`, `IfcSpace`, `IfcOpeningElement` | R (dozens) |
| UPPERCASE `IFCWALL` | Copied from a raw line of an `.ifc` file ("#12=IFCWALL(...)"). | `IFCBUILDINGELEMENTPROXY` ([en-bsforum-r020](https://forums.buildingsmart.org/t/5260)), `IFCROOF` ([en-gh-thatopen-r058](https://github.com/ThatOpen/engine_fragment/issues/206)), `IFCBEAMTYPE` ([en-gh-thatopen-r060](https://github.com/ThatOpen/engine_fragment/issues/143)), `IFCWALLSTANDARDCASE` ([en-qto-r024](https://github.com/Autodesk/revit-ifc/issues/141)) | R |
| lowercase or mixed `ifcwall`, `IFCSpaces`, `ifcSite`, `IFCsite` | Typed from memory, no special care. | "list ifcspaces w/ name number and area" ([en-autodesk-revit-import-s006](../research_raw/wave1/en/en-autodesk-revit-import.jsonl), S); "Elevation in IFCsite" ([t-coordinates-rx013](https://github.com/Autodesk/revit-ifc/issues/581), R); `ifcSite` ([en-autodesk-revit-export-r013](https://forums.autodesk.com/t5/revit-mep-forum/ifc-exports-at-wrong-elevation-even-when-ifcsite-is-ticked/td-p/11214407), R) | R, S |

Both CamelCase and UPPERCASE are the *same class*; the file format is case-insensitive for keywords in principle, and tools write uppercase (see [../01_ifc_basics/02_ifc_file_anatomy.md](../01_ifc_basics/02_ifc_file_anatomy.md)). A server must accept all three.

### 7.2 Observed misspellings and plural slips of entity and property names

| Written | Meant | Type of slip | Tag, source |
|---|---|---|---|
| `IfcBuildingElementProxi` | `IfcBuildingElementProxy` | Last letter changed | R [en-gh-proxy-r033](https://github.com/IfcOpenShell/IfcOpenShell/issues/6299) |
| `IfcBuildingElementProxies` | the plural of the class | English plural on a class name | R [en-bsforum-r016](https://forums.buildingsmart.org/t/5130) |
| `IFCELEMENTASSEMLBY` | `IFCELEMENTASSEMBLY` | Two letters swapped | R [en-openings-r032](https://forums.buildingsmart.org/t/ifcelementassemlby-and-openings/4143) |
| `IfcCoveting.CEILING` | `IfcCovering.CEILING` | One letter changed | R [en-gh-proxy-r037](https://github.com/Autodesk/revit-ifc/issues/157) |
| `IfcOpenning` | `IfcOpeningElement` / opening | Doubled letter | N [p-developer report](../research_raw/wave1/roles/p-developer.md) |
| `IFCRoad` | `IfcRoad` | Mixed case | N [t-infra-ifc43 report](../research_raw/wave1/topics/t-infra-ifc43.md) |
| `IfcSpaces`, `IFCSPACEs`, `IFCSTOREYs` | several spaces / storeys | English `s` glued on | R [en-gh-thatopen-r036](https://github.com/ThatOpen/engine_components/issues/414), [de-dach-r003](https://github.com/Autodesk/revit-ifc/issues/924) |
| `IfcOpeningElements` | several opening elements | Plural on a class name | R [en-autodesk-revit-import-r047](https://github.com/Autodesk/revit-ifc/issues/804) |
| `Qto_SpaceBaesQuantities` | `Qto_SpaceBaseQuantities` | Letter swap inside a property-set name | R [en-spaces-r013](https://github.com/Autodesk/revit-ifc/issues/529) |
| `CoveringBaseQuantitie`, `Widht` | `CoveringBaseQuantities`, `Width` | Missing and swapped letter | R [de-dach-r013](https://github.com/Autodesk/revit-ifc/issues/872) |
| `Pset_Pset_ManufacturerTypeInformation` | one `Pset_` prefix | Doubled prefix | R [en-gh-ifcopenshell-r038](https://github.com/IfcOpenShell/IfcOpenShell/issues/7095) |
| `EnvironmenalClass`, `ContructionType` | `EnvironmentalClass`, `ConstructionType` | Dropped letter in a property name | N [t-versions-mvd report](../research_raw/wave1/topics/t-versions-mvd.md) |
| `IfcGuid`, `IFCGuid`, `IfcGUID`, `GlobalId`, `GlobalID`, `Global ID`, `Globel Id` | the 22-character element id | Five spellings for one thing | R [en-gh-revit-ifc-r044](https://github.com/Autodesk/revit-ifc/issues/696) `IfcGuid`, [en-autodesk-revit-export-r038](https://forums.autodesk.com/t5/revit-api-forum/ifc-guid-is-different-in-the-ifcguid-parameter-written-by-revit/td-p/12650094) `IFCGuid`, [en-osarch-guid-r010](https://community.osarch.org/discussion/3678/no-global-id-for-filled-surfaces-in-drawings) `Global ID`; N [p-developer report](../research_raw/wave1/roles/p-developer.md) `Globel Id` |
| `IfcExportAs`, `IFCExportAs`, `ifcExportAs`, `IfcExportType`, `IFCExportType` | Revit parameter that decides the IFC class | Case varies | R [de-dach-r019](https://github.com/Autodesk/revit-ifc/issues/676), [es-spain-r003](https://forums.autodesk.com/t5/revit-architecture-forum/mapping-of-revit-parameters-to-ifc-parameters-for-export/td-p/7638232), [en-gh-proxy-r020](https://github.com/Autodesk/revit-ifc/issues/497) |
| `pset`, `Pset`, `PSet`, `psets`, `Psets`, `ePset`, `property set`, `PropertySet` | property set | Spoken short form vs standard | R [en-autodesk-revit-export-r008](https://forums.autodesk.com/t5/revit-architecture-forum/ifc-export-in-2027-mapping-parameters-severely-lacking/td-p/14229702), [en-coord-r040](https://community.osarch.org/discussion/comment/29556/) `ePset`, [es-spain-r011](https://forums.autodesk.com/t5/revit-architecture-forum/pset-parameters/td-p/9926144) `PSet` |
| `Qto`, `QTO`, `qto`, `Qto_WallBaseQuantities`, `quantity set` | quantity set vs the human activity "quantity take-off" | Inconsistent case; two meanings | N [t-qto-cost report](../research_raw/wave1/topics/t-qto-cost.md) "Qto vs QTO inconsistently"; R [de-dach-r025](https://www.bimdeutschland.de/bim-wissen/standards-normen-richtlinien/model-view-definitions) |
| `qantities`, `take offs` | quantities, take-offs | Dropped letter, noun plural | R [en-qto-r036](https://github.com/xBimTeam/XbimEssentials/issues/389) |
| `COBie`, `COBIe`, `Cobiee`, `cobiee` | COBie | Mixed case, doubled letter | R [en-uk-anz-india-r003](https://github.com/IfcOpenShell/IfcOpenShell/issues/5702) `COBIe`; R [en-cobie-r026](https://github.com/opensourceBIM/COBie-plugins/issues/2), [en-cobie-r027](https://github.com/opensourceBIM/COBie-plugins/issues/3) |
| `bSDD`, `BSDD`, `bsdd` | buildingSMART Data Dictionary | Case | R [t-classification-bsdd report](../research_raw/wave1/topics/t-classification-bsdd.md) (lowercase b in the real name); K |
| `IDS` | Information Delivery Specification | Easy to confuse with the Russian "ИДС" or a database id | K |

Rule of thumb from the real data: **a misspelled class or property name nearly always comes from someone who is typing it by hand without a viewer open** (beginners, non-native English writers). Experienced coordinators paste the name.

### 7.3 Free words around the technical tokens

| Slip | Examples | Tag, source |
|---|---|---|
| Letter swaps and drops in everyday words | "properites", "Strucutral", "Documantation", "qantities", "Querry", "convertig", "Elntities" | R [en-gh-thatopen-r017](https://github.com/ThatOpen/engine_web-ifc/issues/402), [en-struct-r003](https://github.com/IfcOpenShell/IfcOpenShell/issues/6459), [p-student-r017](https://forums.buildingsmart.org/t/ifc-documantation/1454), [en-qto-r036](https://github.com/xBimTeam/XbimEssentials/issues/389), [en-val-r011](https://forums.buildingsmart.org/t/querry-the-whole-list-of-ifc-classes-to-bsdd-for-ids-writing/5395), [en-infra-r034](https://github.com/IfcOpenShell/IfcOpenShell/issues/5502), [en-bsmart-r015](https://forums.buildingsmart.org/t/merging-ifc2-3-elntities-in-a-ifc4-file/2846) |
| Same word spelled two ways (alignment) | "alignment" / "allignment" / "alignement" | R [en-civil-infra-r024](https://github.com/IfcOpenShell/IfcOpenShell/issues/5471), [en-civil-infra-r013](https://github.com/ThatOpen/engine_web-ifc/issues/926) |
| More everyday-word slips | "expoted", "shapshot", "propperly", "appartment", "boudnary", "Professioonals", "MIME tipe", "Costum Export Setup", "Handeling" | R [en-us-canada-infra-r032](https://forums.autodesk.com/t5/revit-architecture-forum/expoted-ifc-is-missing-elements-while-using-ifc4-schema/m-p/11455810), [en-clash-r027](https://github.com/buildingSMART/BCF-XML/issues/385), [en-gh-r002](https://github.com/Autodesk/revit-ifc/issues/556), [en-revit-auto-r007](https://forum.dynamobim.com/t/automate-the-creation-of-view-plans-of-each-appartment-with-the-cropzone-aligning-exactly-on-the-outer-boundary-of-the-boudnary-walls-of-each-appartment/115202), [en-mea-r002](https://forums.buildingsmart.org/t/bottlenecks-faced-by-bim-professioonals/6633), [en-val-r015](https://forums.buildingsmart.org/t/what-mime-tipe-could-be-ids/5338), [en-dynamo-pyrevit-r033](https://forum.dynamobim.com/t/ifc-export-with-costum-export-setup/104007), [en-dynamo-pyrevit-r018](https://forum.dynamobim.com/t/handeling-revitparameters-to-ifcparameters-ifcspatialcontainer-ifcspace/83281) |
| Unit slip, French writers | "Mo" for "MB" | N [en-gh-thatopen report](../research_raw/wave1/en/en-gh-thatopen.md) |
| German-influenced English | "vom" for "from" | R [en-us-canada-infra-r023](https://forums.autodesk.com/t5/civil-3d-forum/exporting-a-bridge-vom-civil-3d-infraworks-to-revit/td-p/8841283) |
| Mixed British/American spelling | "colour/ color" | N [t-materials-colors-layers report](../research_raw/wave1/topics/t-materials-colors-layers.md) |
| Missing apostrophe, lowercase start | "whats the root cause ...", "doesnt" | R [en-gh-revit-ifc-r040](https://github.com/Autodesk/revit-ifc/issues/579); N [t-infra-ifc43 report](../research_raw/wave1/topics/t-infra-ifc43.md) |

---

## 8. Product and tool names

Counts are rough occurrence counts in the record text (real and synthetic together unless a kind is given). Non-Latin forms are in the language sections below.

| Canonical | Variants seen | Tag, source | Notes |
|---|---|---|---|
| **Revit** | `Revit` (dominant), `revit`, `REVIT`, `Revit 2024`, `REVIT 2026`, `REVIT2023`, `Revit 25`, `Revit 21`, `RevitIFC`, `RevitIFCUnitBug` (a code identifier in an issue title), `Revitparameters` (run together with another word) | R [en-us-canada-infra-r022](https://forums.autodesk.com/t5/revit-architecture-forum/revit-2026-won-t-export-to-ifc/td-p/13807489) `REVIT 2026`; R [en-err-r008](https://github.com/Autodesk/revit-ifc/issues/718) `REVIT2023`; R [en-gh-ifcopenshell-r007](https://github.com/IfcOpenShell/IfcOpenShell/issues/6120) `Revit 25`; R [en-ghrevitifc-r030](https://github.com/Autodesk/revit-ifc/issues/576) `RevitIFCUnitBug`; R [en-dynamo-pyrevit-r018](https://forum.dynamobim.com/t/handeling-revitparameters-to-ifcparameters-ifcspatialcontainer-ifcspace/83281) | Short year forms (`Revit 21`, `Revit 25`) appear. |
| **Archicad** | `Archicad` (most), `ArchiCAD`, `ARCHICAD`, `archicad`, `ArchiCad`, `AC` (not seen) | R [en-arch-r022](https://forums.autodesk.com/t5/revit-architecture-forum/ifc-exchange-revit-archicad/td-p/10357376) `ARCHICAD`; R [en-autodesk-revit-import-r010](https://github.com/Autodesk/revit-ifc/issues/358) `ArchiCAD`; R [es-aimcp-r031](https://github.com/joacos/archicad-mcp) `archicad`; R [ru-dwg-other-r021](https://forum.dwg.ru/showthread.php?t=75883) "ArchiCad" (small d) | The vendor writes **Archicad**; users write `ArchiCAD` almost as often. Both are fine. |
| **Navisworks** | `Navisworks`, `navisworks`, `Navis`, `navis`, `NWC`, `NWD` | R [en-mea-r003](https://forums.buildingsmart.org/t/bottlenecks-of-current-version-of-navisworks/6628) lowercase title; S [en-navis-acc-s001](../research_raw/wave1/en/en-navis-acc.jsonl) "navis shows empty tabs"; S [en-navis-acc-s007](../research_raw/wave1/en/en-navis-acc.jsonl); N [en-navis-acc report](../research_raw/wave1/en/en-navis-acc.md) "Not verified from sources" | "Navis" is plausible and common in speech but only synthetic in the data. |
| **Solibri** | `Solibri`, `solibri` | R [en-autodesk-revit-import-r006](https://github.com/Autodesk/revit-ifc/issues/658); S [en-autodesk-revit-export-s015](../research_raw/wave1/en/en-autodesk-revit-export.jsonl) | Stable spelling. |
| **Tekla** | `Tekla`, `tekla`, `TEKLA`, `Tekla BIMsight` | R [zh-zhihu-r009](https://www.zhihu.com/question/60173683) lowercase; R [zh-tw-hk-r001](https://housegear.pixnet.net/blog/posts/3042268210) caps | |
| **Tekla BIMsight** | `BIMsight`, `BimSight`, `bimsight` | R [ru-dwg-other-r018](https://forum.dwg.ru/showthread.php?t=150272&page=2), [ru-arch-r042](https://forum.dwg.ru/showthread.php?t=160240) | Old viewer; still named in Russian threads. |
| **BIMcollab** | `BIMcollab`, `BimCollab`, `bimcollab`, `BIMcollab ZOOM` | R [en-clash-r006](https://github.com/IfcOpenShell/IfcOpenShell/issues/7152) `BimCollab`; S [en-gh-ifcopenshell-s013](../research_raw/wave1/en/en-gh-ifcopenshell.jsonl) lowercase | |
| **BIMvision** | `BIMvision`, `BIM Vision`, `BIMVision`, `BimVision`, `BIM vision` | R [de-dach-r016](https://github.com/Autodesk/revit-ifc/issues/566) `BIM Vision`; R [en-osarch-r031](https://community.osarch.org/discussion/462/blenderbim-add-on-ifc-export-not-visible-in-revit) `BIMVision` | The free Polish viewer, often named as the cross-check. |
| **SimpleBIM** | `SimpleBIM`, `simplebim` | R [en-gh-encoding-r023](https://github.com/ThatOpen/engine_web-ifc/issues/506); S [en-model-checking-s013](../research_raw/wave1/en/en-model-checking.jsonl) | |
| **BlenderBIM / Bonsai** | `BlenderBIM`, `Blenderbim`, `blenderbim`, `BlenderBim`, `Blender BIM`, `BBIM`, `Bonsai`, `BONSAI`, `bonsai`, `ifc-bonsai` | R [en-err-r034](https://forums.buildingsmart.org/t/error-when-import-file-of-ifc3x2-into-blenderbim-do-the-shape-or-filesize-have-some-limits/3836) `blenderbim`; R [p-student-r009](https://community.osarch.org/discussion/635/ifcspace-and-blenderbim) `BlenderBim`; R [ja-japan-r023](https://note.com/akram/n/n8a6e9c5602ca) "Bonsai(Blender BIM)"; R [en-osarch-r019](https://community.osarch.org/discussion/1753/bbim-two-door-types-with-connected-properties) `BBIM`; R [en-qto-r008](https://github.com/IfcOpenShell/IfcOpenShell/issues/5706) `BONSAI`; S [en-aimcp-s003](../research_raw/wave1/ai/ai-mcp-usage.jsonl) "won't open in bonsai" | **Old name versus new name.** BlenderBIM was renamed Bonsai; people still write the old name. A server should know both. |
| **IfcOpenShell** | `IfcOpenShell`, `ifcopenshell`, `IFCOpenShell`, `IFCopenshell`, `IfcOpenshell`, `IFCOpenshell` | R [en-gh-ifcopenshell-r022](https://github.com/IfcOpenShell/IfcOpenShell/discussions/7538) `IFCOpenShell`; R [ru-habr-dev-r027](https://github.com/Autodesk/revit-ifc/issues/777) `IFCopenshell`; R [p-student-r023](https://github.com/IfcOpenShell/IfcOpenShell/issues/2848) `IfcOpenshell`; R [en-gh-encoding-r028](https://github.com/IfcOpenShell/IfcOpenShell/issues/388) `IFCOpenshell` | Package name on PyPI is lowercase `ifcopenshell`. |
| **web-ifc / That Open / IFC.js** | `web-ifc`, `WEB-IFC` (log prefix), `WebIFC`, `webifc`, `IFC.js`, `ifc.js`, `web-ifc-three`, `ifc-three`, `ThatOpen`, `That Open` | R [en-err-r013](https://github.com/ThatOpen/engine_web-ifc/issues/1402) `[WEB-IFC]`; R [en-gh-thatopen-r006](https://github.com/ThatOpen/engine_web-ifc/issues/1816) `WebIFC`; R [en-gh-thatopen-r014](https://github.com/ThatOpen/engine_web-ifc/issues/2203) `webifc`; R [zh-smoke-r007](https://blog.csdn.net/jiangxinyu50/article/details/135743196) `ifc.js`; R [ru-habr-dev-r016](https://habr.com/ru/articles/759230/) `IFC.js`; R [zh-csdn-dev-r022](https://blog.csdn.net/pumbkin/article/details/141029954) `web-ifc-three`; N [en-gh-thatopen report](../research_raw/wave1/en/en-gh-thatopen.md) lists "ifc.js" and "ifcs" among the variants seen | IFC.js is the earlier name of the project now called That Open (see [../04_open_source/libraries_and_toolkits.md](../04_open_source/libraries_and_toolkits.md); the rename is general knowledge there, not stated by the sources). |
| **xBIM** | `xBIM`, `Xbim`, `xbim`, `XBim`, `XBIM`, `xBim`, `.xbim` (file) | R [en-bsforum-r028](https://forums.buildingsmart.org/t/5760), [en-beginner-qa-r009](https://github.com/IfcOpenShell/IfcOpenShell/issues/2499) `XBim`, [zh-csdn-dev-r020](https://blog.csdn.net/qq_40244176/article/details/96828787) `xBim` | The same library appears in five casings. |
| **Dynamo / pyRevit** | `Dynamo`, `dynamo`, `pyRevit`, `pyrevit`, `Pyrevit`, `PyRevit` | R [en-revit-auto-r022](https://discourse.pyrevitlabs.io/t/connecting-agent-to-pyrevit-mcp-newbie/10627) `Pyrevit`; R [en-dynamo-pyrevit-r038](https://discourse.pyrevitlabs.io/t/pyrevit-cli-problem-with-creating-new-family-instance-in-opened-ifc-file/2935) `PyRevit`; R [zh-aimcp-r012](https://github.com/shuotao/REVIT_MCP_study/issues/110) `pyRevit` | |
| **Autodesk cloud** | `BIM 360`, `BIM360`, `bim360`, `ACC` (Autodesk Construction Cloud) | R [en-dynamo-pyrevit-r001](https://forum.dynamobim.com/t/ifc-export-node-return-an-empty-ifc/82822) `BIM 360`; R [en-autodesk-revit-import-r027](https://github.com/Autodesk/revit-ifc/issues/568) `BIM360`; S [en-navis-acc-s003](../research_raw/wave1/en/en-navis-acc.jsonl) `ACC` | `ACC` is also a common letter combination; keep context. |
| **Civil 3D** | `Civil 3D`, `Civil3D`, `civil3d` | R [en-us-canada-infra-r026](https://forums.autodesk.com/t5/civil-3d-forum/link-ifc4-from-civil3d-to-revit/td-p/12269817) `Civil3D`; S [en-us-canada-infra-s003](../research_raw/wave1/en/en-us-canada-infra.jsonl) `civil3d` | |
| **usBIM / ACCA** | `usBIM`, `Edificius` | R [it-italy-r027](https://biblus.acca.it/usbim-checker-verifica-informativa-del-modello/) | Italian vendor products. |
| **AI side** | `Claude`, `claude`, `ChatGPT`, `chatgpt`, `MCP`, `mcp`, `LLM`, `Cursor`, `клод` | R [en-aimcp-r003](https://github.com/mcp-servers-for-revit/mcp-servers-for-revit/issues/1) `Claude`; R [en-aimcp-r015](https://github.com/IfcOpenShell/IfcOpenShell/issues/6256) `chatgpt`; R [zh-aimcp-r024](https://github.com/ZedMoster/revit-mcp/issues/1) `Cursor`; S [ru-aimcp-s012](../research_raw/wave1/ai/ai-mcp-usage.jsonl) `клод пишет не могу подключиться к ревиту` | The chat partner itself is named in lowercase or transliterated in casual speech. |
| **Repo-style names** | `revit-mcp`, `revit_mcp_server`, `revit_create_level`, `ifc-bonsai-mcp`, `ifcopenshell-mcp`, `REVIT_MCP_study` | R [en-aimcp-r005](https://github.com/bimwright/rvt-mcp/issues/21), [en-aimcp-r009](https://github.com/oakplank/RevitMCP/issues/1), [en-aimcp-r044](https://github.com/Show2Instruct/ifc-bonsai-mcp), [en-aimcp-r028](https://github.com/Daviidro/ifcopenshell-mcp) | Hyphen, underscore and camel forms all appear; match by meaning, not by string. |

---

## 9. Language by language

For each language: how the **key tokens** (IFC, Revit, other products) are written, and what slips are plausible. Most casual-form rows are S or N, because the data holds few real chat messages (see the evidence table in [jargon_slang_dictionary.md](jargon_slang_dictionary.md#coverage-how-much-evidence-each-language-has)).

### 9.1 Russian (Cyrillic)

**Finding that matters:** real forum **titles** keep Latin product names ("Экспорт из Tekla в Revit"), while the **question text** of the same threads uses Cyrillic spoken forms ("из Теклы в Ревит"). The research report says it plainly: «Текла/Ревит» транслитом ([ru-dwg-other-r001](https://forum.dwg.ru/showthread.php?t=146029)). So a Russian prompt can legitimately show **either**; mixing both in one sentence is also normal.

| Canonical | Cyrillic forms seen | Tag, source | Notes |
|---|---|---|---|
| IFC | `ифс`, `ифц`, `ифс4`; formal `IFC`, `IFC-модели` | S (59 prompts); N [ru-dwg-other report](../research_raw/wave1/ru/ru-dwg-other.md); R (Latin) [ru-autodesk-telegram-r009](https://habr.com/ru/companies/pik_digital/articles/1057314/) | `ифс` takes normal case endings in speech (в ифс, из ифса). |
| Revit | `Ревит`, `ревит`, `Ревите` (in Revit), `Ревита` (of Revit), `ревиту` (to Revit) | R (paraphrase) [ru-dwg-other-r001](https://forum.dwg.ru/showthread.php?t=146029), [ru-dwg-other-r006](https://forum.dwg.ru/showthread.php?t=149046), [ru-autodesk-telegram-r019](https://sapr.ru/article/25825); S [ru-aimcp-s012](../research_raw/wave1/ai/ai-mcp-usage.jsonl) | Declined like a normal noun. |
| Archicad | `Архикад`, `Архикаде`, `Архикада`, `ArchiCad` | R [ru-dwg-other-r007](https://forum.dwg.ru/showthread.php?t=76210), [ru-dwg-other-r024](https://forum.dwg.ru/showthread.php?t=75685), [ru-dwg-other-r021](https://forum.dwg.ru/showthread.php?t=75883) | |
| Tekla | `Текла`, `Теклы`, `Теклой` | R [ru-dwg-other-r001](https://forum.dwg.ru/showthread.php?t=146029), [ru-dwg-other-r010](https://forum.dwg.ru/showthread.php?t=159943) | |
| Navisworks | `Навис`, `нависа`, `нависе` (genitive and locative), `нависворкс` | R (paraphrase) [ru-habr-dev-r003](https://habr.com/ru/articles/1089018/); S [ru-dwg-other-s005](../research_raw/wave1/ru/ru-dwg-other.jsonl), [ru-dwg-other-s014](../research_raw/wave1/ru/ru-dwg-other.jsonl); N [ru-dwg-other report](../research_raw/wave1/ru/ru-dwg-other.md) "нависворкс/навис" | |
| Solibri | `солибри` | S [ru-vm-s004](../research_raw/wave1/topics/t-versions-mvd.jsonl) | |
| Renga | `Renga`, `ренга`, `ренги`, `ренге` | R [ru-autodesk-telegram-r017](https://blog.rengabim.com/2021/08/ifc.html); S [ru-renga-nanocad-s001](../research_raw/wave1/ru/ru-renga-nanocad.jsonl) | Russian CAD/BIM product. |
| Sapfir (SAPFIR) | `САПФИР`, `Сапфира` | R [ru-dwg-other-r003](https://forum.dwg.ru/showthread.php?t=160240) | Russian architecture software; written in caps in titles. |
| SCAD, Lira, Monomakh, Stark ES | `СКАД`, `Скад`, `Лира`, `Мономах`, `Старк ЕС` | R [ru-dwg-other-r019](https://forum.dwg.ru/showthread.php?t=142967), [ru-dwg-other-r020](https://forum.dwg.ru/showthread.php?t=33352), [ru-autodesk-telegram-r006](https://forum.dwg.ru/showthread.php?t=133669) | Structural analysis programs; Cyrillic names. |
| nanoCAD | `нанокад`, `nanoCAD` | N [ru-dwg-other report](../research_raw/wave1/ru/ru-dwg-other.md) | |
| BCF | `бцф` | S/N [ru-renga-nanocad report](../research_raw/wave1/ru/ru-renga-nanocad.md) (assumption) | |
| proxy | `проксик`, `проксики`, `прокси`, `проксей` (genitive plural) | S [ru-arch-s010](../research_raw/wave1/roles/p-architect.jsonl), [ru-coord-s007](../research_raw/wave1/roles/p-bim-coordinator.jsonl); N [ru-dwg-other report](../research_raw/wave1/ru/ru-dwg-other.md) | See the [dictionary](jargon_slang_dictionary.md). |
| pset | `псеты`, `психеты` (jocular) | S [ru-autodesk-telegram-s010](../research_raw/wave1/ru/ru-autodesk-telegram.jsonl) "покажи психеты у одной стены" | "Psychets" is a pun on "pset"; rare, jocular. |
| export / import verbs | `экспортнуть`, `импортнуть`, `выгрузить`, `выгрузил` | N [ru-dwg-other report](../research_raw/wave1/ru/ru-dwg-other.md) (the first two); R [ru-dwg-other-r021](https://forum.dwg.ru/showthread.php?t=75883) title uses `экспортнуть` | |

Plausible Russian slips (all P): wrong keyboard layout (`ifc` typed on a Russian layout gives `шас`; `Revit` gives `Кумше`; `IfcWall` gives `ШасЦфдд`), `ё` written as `е` everywhere, missing `ь`. Only the layout slip is a realistic *accident*; the data shows no instance of it.

### 9.2 Chinese (Mainland, Taiwan, Hong Kong)

| Feature | Seen | Tag, source |
|---|---|---|
| No space between Latin and Chinese | `revit导出ifc`, `ifc转成`, `tekla导出的钢结构IFC太大` | R [zh-arch-r036](https://blog.csdn.net/d001014/article/details/140438872), [zh-arch-r038](https://blog.csdn.net/weixin_32199769/article/details/112582298) |
| Spaces only between Latin tokens | `revit 2020 ifc guid不生成是为什么?` | R [zh-zhihu report](../research_raw/wave1/zh/zh-zhihu.md) (quoted example) |
| Lowercase product names | `revit`, `tekla`, `rvt`, `Su` (SketchUp), `MAX` (3ds Max), `pln` | N [zh-revit-export report](../research_raw/wave1/zh/zh-revit-export.md), [zh-zhihu report](../research_raw/wave1/zh/zh-zhihu.md) |
| Caps in Taiwan blogs | `REVIT`, `ARCHICAD`, `TEKLA` | R [zh-tw-hk-r001](https://housegear.pixnet.net/blog/posts/3042268210), N [zh-tw-hk report](../research_raw/wave1/zh/zh-tw-hk.md) |
| Mainland versus Taiwan verbs | 导出/导入 vs 匯出/匯入; vendor help 導入/導出 | N [zh-tw-hk report](../research_raw/wave1/zh/zh-tw-hk.md) |
| Simplified vs Traditional tokens in one phrase | `IFC文件` (simplified) vs `IFC檔` (Taiwan) | R [zh-csdn-dev-r022](https://blog.csdn.net/pumbkin/article/details/141029954), [zh-tw-hk-r009](https://etheses.lib.ntust.edu.tw/thesis/detail/2e82ca6d84bfe5f839f58b35029a1d54) |
| Bracket tags | `【BIM】`, `[IFC]`, `[Revit]` | R [zh-zhihu-r003](https://zhuanlan.zhihu.com/p/651323857), [zh-tw-hk-r001](https://housegear.pixnet.net/blog/posts/3042268210) |
| Half-width comma inside a Chinese title | `关于tekla导出ifc到revit,3D视图不显示的问题？` | R [zh-zhihu-r009](https://www.zhihu.com/question/60173683) |
| Domestic software names | `广联达`, `构力`, `PKPM`, `BIMBase` | R [zh-zhihu-r027](https://www.zhihu.com/question/642487361), [zh-revit-export-r011](https://bbs.zhulong.com/106010_group_3002227/detail33178172/) |
| Regional IFC profiles | `SZ-IFC`, `宁建模` | R [zh-lightweight-review-r001](https://zhuanlan.zhihu.com/p/673078056); N [zh-lightweight-review report](../research_raw/wave1/zh/zh-lightweight-review.md) |
| Chinese names for products | None seen for Revit or Archicad; Latin always | R (negative result across about 170 real Chinese records) |

Full-width Latin (`ＩＦＣ`) was searched for and **not found**; if used, it is a P-level robustness test (and will break naive string match).

### 9.3 Japanese

| Feature | Seen | Tag, source |
|---|---|---|
| Latin acronym, Latin product names | `IFC出力`, `ArchicadのIFC`, `RevitのUniqueIdとIFCのGUID`, `IfcOpenShellで階情報を取得する` | R [ja-arch-r035](https://note.com/iu_bimstudio_n/n/nf41bb9e91025), S [ja-roundtrip-s014](../research_raw/wave1/topics/t-roundtrip-interop.jsonl), R [p-student-r034](https://qiita.com/Takashi_Kasuya/items/97899d15e7ec0186eecf), R [ja-japan-r002](https://zenn.dev/cote2/articles/6459c1c44091da) |
| Katakana for ordinary borrowed words | `ビューア` (viewer), `パラメータ`, `レイヤー` / `レイヤ`, `プロパティ`, `エクスポート` | R [ja-japan-r013](https://zenn.dev/kazuyamaeda/articles/97933cdafce6d8), [ja-japan-r021](https://note.com/onestruction/n/ne8322e3be44d), [ja-japan-r015](https://note.com/toshio_nakamura/n/nc8db42ce3191); S [ja-guid-s012](../research_raw/wave1/topics/t-guid-versioning.jsonl) |
| Two katakana spellings of one word (long-vowel mark kept or dropped) | `レイヤー` / `レイヤ` | R [ja-arch-r035](https://note.com/iu_bimstudio_n/n/nf41bb9e91025) vs [ja-japan-r015](https://note.com/toshio_nakamura/n/nc8db42ce3191) |
| Product names in katakana | **Not found.** `レビット` for Revit and `アーキキャド` for Archicad are plausible but unobserved | P |
| Export/import verbs | 書き出し (write out), 出力 (output), 読み込み (read in), 取り込み | N [ja-japan report](../research_raw/wave1/ja/ja-japan.md) |
| Dropped `ー` in long vowels (`ビューア` vs `ビューアー`) | Plausible slip | P |
| Casual ending | `〜してほしいんだけど...合ってる`, `〜して` | S [ja-japan-s014](../research_raw/wave1/ja/ja-japan.jsonl), [ja-japan-s008](../research_raw/wave1/ja/ja-japan.jsonl) |

### 9.4 Korean

| Feature | Seen | Tag, source |
|---|---|---|
| Revit as `레빗` | `레빗에서`, `레빗으로`, `레빗 없이` | S [ko-korea-s001](../research_raw/wave1/ko/ko-korea.jsonl), [ko-korea-s014](../research_raw/wave1/ko/ko-korea.jsonl), [p-student-s018](../research_raw/wave1/roles/p-student.jsonl); N [ko-korea report](../research_raw/wave1/ko/ko-korea.md) |
| Archicad as `아키캐드` | Real association event title | R [ko-korea-r006](https://www.buildingsmart.or.kr/Home/NewsDetail?board=1&id=3451) |
| IFC with a particle | `ifc에`, `IFC를`, `ifc 레빗으로 링크하니까` | S [ko-korea-s001](../research_raw/wave1/ko/ko-korea.jsonl), [ko-korea-s014](../research_raw/wave1/ko/ko-korea.jsonl) |
| Latin class names inside Korean | `IfcColumn으로`, `ifcopenshell로` | S [ko-korea-s007](../research_raw/wave1/ko/ko-korea.jsonl), [ko-korea-s011](../research_raw/wave1/ko/ko-korea.jsonl) |
| Wrong-layout accident (2-set Korean layout) | `ifc` becomes `ㅑㄹㅊ`; `revit` becomes `ㄱㄷㅍㅑㅅ` | P |

Informal endings (`뽑아줘`, `찾아줘`, `확인해줘`) are in 9 to 10 synthetic prompts; they affect tone, not spelling of the key tokens.

### 9.5 Spanish

| Feature | Seen | Tag, source |
|---|---|---|
| Missing accents in titles and chat | "Exportacion", "Descripcion", "cuantos", "por que" | N [es-latam report](../research_raw/wave1/es/es-latam.md); N [es-spain report](../research_raw/wave1/es/es-spain.md); S [es-spain-s005](../research_raw/wave1/es/es-spain.jsonl) "por que?" |
| English plural apostrophe | `IFC's` | R [es-spain-r001](https://forums.autodesk.com/t5/revit-architecture-forum/problemas-con-ifc-s/td-p/10189111) |
| All caps and a typo | `SOPOTARÁ ARCHIVOS IFC?` | R [es-latam-r001](https://github.com/ingelibre/ingetrazo/issues/1033) |
| Lowercase acronym | `ifc`, `pset`, `proxys` (English plural `s`), `proxy` | S [es-spain-s005](../research_raw/wave1/es/es-spain.jsonl), [es-latam-s004](../research_raw/wave1/es/es-latam.jsonl); N [es-spain report](../research_raw/wave1/es/es-spain.md) |
| Product names | `Revit`, `revit`, `Archicad`, `archicad` (Latin) | R [es-aimcp-r031](https://github.com/joacos/archicad-mcp) `archicad`; S [es-latam-s004](../research_raw/wave1/es/es-latam.jsonl) |
| Regional tag | Rioplatense `Creá`; Mexican `qué onda`; Peruvian `metrados` | R [es-aimcp-r031](https://github.com/joacos/archicad-mcp); N [es-latam report](../research_raw/wave1/es/es-latam.md) |
| Spelling of "IFC" as a word | Never `ifece`; always `IFC` / `ifc` | R (negative) |

### 9.6 Portuguese, French, Italian, German, Dutch, Norwegian

| Language | Seen | Tag, source |
|---|---|---|
| Portuguese | Dropped tilde ("nao"), `ifc`/`ifczip`/`ifcxml` lowercase, `compatibilização`, `pavimento` | S [pt-vm-s009](../research_raw/wave1/topics/t-versions-mvd.jsonl), [pt-fs-s010](../research_raw/wave1/topics/t-file-size.jsonl); N [pt-brazil report](../research_raw/wave1/pt/pt-brazil.md) (illustrative, from synthetic) |
| French | Apostrophe dropped ("l export"), lowercase, `maquette IFC`, `ifc2x3` | S [fr-clash-s013](../research_raw/wave1/topics/t-clash-bcf.jsonl); R [fr-arch-r032](https://www.ge.ch/utiliser-bim-building-information-modeling/je-prepare-maquette-bim-autorisation-construire) |
| Italian | `file IFC`, `modello IFC`, `IFC VS RVT` (VS in caps), lowercase terse | R [it-italy-r001](https://biblus.acca.it/problemi-editing-file-ifc/); N [it-italy report](../research_raw/wave1/it/it-italy.md); S [it-italy-s011](../research_raw/wave1/it/it-italy.jsonl) "2x3 CV2.0 o IFC4 RV" |
| German | ASCII-fied umlauts ("fuer", "geaendert"), `Stand 12`, `TGA`, `LV`, capitalised nouns kept | S [de-dach-s008](../research_raw/wave1/de/de-dach.jsonl), [de-guid-s008](../research_raw/wave1/topics/t-guid-versioning.jsonl); N [de-dach report](../research_raw/wave1/de/de-dach.md) |
| Dutch | English terms kept ("export settings", "clashdetectie") and Dutch compounds | N [nl-dutch report](../research_raw/wave1/nl/nl-dutch.md) |
| Norwegian | Lowercase start, `æøå` kept or lost in file names, `ifc-filen` | S [no-norway-s016](../research_raw/wave1/no/no-norway.jsonl); N [no-norway report](../research_raw/wave1/no/no-norway.md) |

### 9.7 Arabic, Turkish, Greek, Czech, Danish, Vietnamese, Slovak, Polish

Almost all of the evidence is about **characters inside the model** (room names, property values), not about how users spell product names.

| Language | What the data shows | Tag, source |
|---|---|---|
| Arabic | Room names in Arabic appear as question marks after export; the sentence mixes Arabic with Latin `IFC` | S [enc-s005](../research_raw/wave1/topics/t-encoding.jsonl) |
| Turkish | `ş ğ ı İ` letters in names; the dotted/dotless I problem (a real XML-reading bug under the Turkish culture) | S [enc-s004](../research_raw/wave1/topics/t-encoding.jsonl), [enc-s015](../research_raw/wave1/topics/t-encoding.jsonl); R [en-gh-xbim-others-r003](https://github.com/xBimTeam/XbimEssentials/issues/670), [en-gh-encoding-r020](https://github.com/IfcOpenShell/IfcOpenShell/issues/101) |
| Greek | Greek space names show weird characters | S [enc-s006](../research_raw/wave1/topics/t-encoding.jsonl) |
| Danish | Request for UTF-8 because `æ ø å` appear as `\X\E6` | R [en-gh-encoding-r022](https://github.com/ThatOpen/engine_web-ifc/issues/358) |
| Czech | Czech diacritics broken after export; reporter writes in English | R [en-gh-encoding-r021](https://github.com/ThatOpen/engine_web-ifc/issues/440) |
| Vietnamese | Toolkit README with Vietnamese example commands | R [vi-aimcp-r042](https://github.com/andyluu98/vn-revit-mcp) |
| Slovak | Feature request with relative camera commands | R [sk-aimcp-r016](https://github.com/Menezeris/AIMviewer/issues/65) |
| Polish | **No data.** BIMvision is a Polish product but no Polish text was sampled. | gap |

---

## 10. Non-ASCII text inside the model: what the file stores

Names with accents, umlauts or non-Latin scripts are written inside `.ifc` files as escape codes, and questions about them are a reliable source of "does the server show the real name?" tests. People describe the symptom, they rarely spell the escape.

| Where | What it looks like | Tag, source |
|---|---|---|
| Header or name field | `\X2\00C70130\X0\ZG` for "ÇİZG" | R [en-gh-encoding-r020](https://github.com/IfcOpenShell/IfcOpenShell/issues/101) |
| ISO 8859-1 escape | `V\X\E6gelement` for "Vægelement" (Danish) | R [en-gh-encoding-r022](https://github.com/ThatOpen/engine_web-ifc/issues/358) |
| Lowercase hex in a `\X2\` block (Chinese) | One tool fails on lowercase hex digits | R [en-gh-encoding-r006](https://github.com/ThatOpen/engine_web-ifc/issues/949) (web-ifc issue 949) |
| User wording | "кракозябры вместо русских названий" (garbage instead of Russian names); "한글이 깨지고" (Korean letters broken); "乱码" (mojibake) | S [ru-renga-nanocad-s010](../research_raw/wave1/ru/ru-renga-nanocad.jsonl), S [ko-korea-s014](../research_raw/wave1/ko/ko-korea.jsonl), N [zh-csdn-dev report](../research_raw/wave1/zh/zh-csdn-dev.md) |
| ASCII-only restrictions | "path without special characters, Latin only" | R [ru-dwg-other-r010](https://forum.dwg.ru/showthread.php?t=159943) |

In synthetic prompts, a name with an umlaut or Cyrillic text should be shown as the user would **see** it (`Wände`, `Дверь_01`), not as the escape code.

---

## 11. Accidents that are not typos: layout, homoglyph, case-folding

| Accident | What happens | Tag | Use in tests? |
|---|---|---|---|
| Cyrillic letter in a Latin word | `IFС` with Cyrillic С looks identical but fails a text match | R (1 case) | Only as a robustness test: "does the server normalise confusable letters?" |
| Wrong keyboard layout | `ifc` becomes `шас` (Russian layout), `ㅑㄹㅊ` (Korean 2-set), `revit` becomes `кумше` | P | Rare, usually corrected by the writer in the next message. Do not generate by default. |
| Auto-capitalisation | Phone keyboards write `Ifc`, `Revit`, `Bim` | P | Fine in chat prompts. |
| Auto-correct | `IFC` becomes `IF`, `ifc` becomes `if`, `Revit` becomes `Revolt` | P | Not observed; do not generate. |
| Case-folding by tools | Python dictionaries and URLs are case-sensitive, Windows paths are not | K | Exact names matter when a prompt gives a file path. |
| Turkish dotted-I | Culture-sensitive upper-casing turns `i` into dotted `İ` under the Turkish locale, so a type-name lookup fails | R [en-gh-xbim-others-r003](https://github.com/xBimTeam/XbimEssentials/issues/670) | A good real example of why case-folding is not trivial. |
| Locale decimal comma | `3,5` vs `3.5` (IT: "decimali con il punto diventano testo") | N [it-italy report](../research_raw/wave1/it/it-italy.md); see the [dictionary](jargon_slang_dictionary.md) | Numbers, not names, but a frequent source of mismatched results. |

---

## 12. Typo patterns (what real slips look like)

From the 39 real records flagged for typos and the title list above:

| Pattern | Examples | Frequency (author's impression from the examples) |
|---|---|---|
| Two letters swapped | Strucutral, Documantation, Elntities, shapshot, boudnary, Baes | Most common |
| One letter dropped | CoveringBaseQuantitie, qantities, convertig | Common |
| One letter doubled or inserted | Professioonals, propperly, Cobiee, appartment, Querry | Common |
| One letter replaced | IfcCoveting, Proxi, tipe, Georefrancing | Occasional |
| Wrong sequence in a code | ifc3X2, IFC2*3 | Occasional |
| Missing apostrophe | whats, doesnt | Occasional |
| Wrong word in the right language | "vom" for "from" | Rare |
| Fused words | RevitIFCUnitBug (in code), Revitparameters, Handeling Revitparameters | Rare |

Typos concentrate in **titles typed by non-native English writers and beginners** ([en-mea-r002](https://forums.buildingsmart.org/t/bottlenecks-faced-by-bim-professioonals/6633), [p-student-r017](https://forums.buildingsmart.org/t/ifc-documantation/1454)) and are almost absent in structured developer reports (template headings, pasted logs). No real record contains more than one or two slips in a title.

---

## 13. Tips for using variants in synthetic prompts without overdoing it

These rules extend [style_guide.md](style_guide.md#8-typos-casing-punctuation) (section 8.3: at most one slip per prompt, about 1 in 4 casual prompts).

1. **Choose a persona and a register first, then the spelling.** A BIM coordinator in chat writes `ifc` and `revit` in lowercase; a vendor support agent writes `IFC` and `Revit`; an official email writes `IFC4` and `Autodesk Revit`.
2. **At most one slip per prompt.** The slip may be a casing change, a dropped accent, a transliterated product name or one typo. Not two. Not in every prompt.
3. **Spell the *non-critical* token loosely and the *critical* token exactly.** If the test checks that the server finds `Pset_WallCommon.FireRating`, type those names exactly and loosen something else (`revit`, `ifc`, the missing accent).
4. **Product names may vary freely; class, property and numeric tokens may not**, unless you are deliberately running a robustness test (rule 9).
5. **Casing recipes.** Casual EN/ZH/RU/ES/PT/KO prompts: product names in lowercase, class names exact. Semi-formal: `IFC`, `Revit`, `Archicad`. A STEP-style `IFCWALL` only when the person is pasting from a raw line or a log.
6. **Respect each script.** Russian may transliterate (`ревит`, `текла`); Chinese does not (Latin product names, no spaces); Japanese uses katakana for ordinary borrowed words but Latin for IFC and product names (observed); Korean transliterates Revit and Archicad (`레빗`, `아키캐드`) but this is mostly synthetic evidence.
7. **Mixed-script homoglyphs and keyboard-layout accidents** (section 11) are P-level. If used at all, keep them to a separate small robustness set, not the main test bank.
8. **Labels.** If a test case uses a P or S variant, write "plausible phrasing, not observed" in the case notes. Do not claim it is "how Russian users write".
9. **Robustness pairs.** To test normalisation, send the same task twice, once with canonical spelling and once with one variant, and compare answers. This is cleaner than putting a typo in a one-off prompt.
10. **Leave context out on purpose** (no schema version, no export setting), but do not delete the *task noun*. "count the proxis" is more useful than "count the p".
11. **Match the number to the data.** Real roughness is mostly casing, not typos: about 1 in 8 English and 1 in 5 Chinese real records use lowercase `ifc`, and about 1 in 60 real records carry a flagged typo. Casual chat prompts can be rougher than forum titles, but not 100% rough.
12. **Keep names that real tools actually use.** `BlenderBIM` (old) and `Bonsai` (new) are both correct today. `IFC.js` (old) and `That Open` / `web-ifc` (current) too. Do not "update" a user's old name; test that the server handles it.

### Do-not list

- A bare variant with no verb or object (`ifs`).
- Any variant of the token that the pass/fail check depends on (`IfcBuildingElementProxi` when the test counts proxies by exact class), unless the case is explicitly about typo tolerance.
- Typos in *every* word of a long prompt (looks like an LLM imitating a drunk user).
- Random letter noise in non-Latin scripts (a wrong Cyrillic letter produces a different word, not a typo).
- Translating `IFC`, `Pset`, `GlobalId` or a class name into the local language.
- Using `AIFC`, `IFS`, `ИФК`, `Revitt` as if they were observed. They are P.

---

## 14. Mini bank: synthetic prompts that carry one variant

Written for this file to show the recipe. **All synthetic** (S in the sense of the tag table); none is a real quote. Each carries exactly one spelling feature; class names and property names are exact.

| # | Language | Prompt | Spelling feature | Gloss (EN) |
|---|---|---|---|---|
| 1 | en | `how many ifc walls are on level 2` | lowercase ifc | How many IFC walls are on level 2. |
| 2 | en | `Ifc export from Revit dropped my shared params, which psets do they land in?` | `Ifc` title case, `psets` | Where do my shared parameters end up. |
| 3 | en | `two ifcs from different teams, do the slabs overlap anywhere` | plural `ifcs` | Compare two IFC files. |
| 4 | en | `still on blenderbim, can it open this file or do I need bonsai` | old product name | Old and new name of the same add-on. |
| 5 | en | `list IFCSPACE names and areas from the ifc` | STEP-style uppercase class | List rooms with their areas. |
| 6 | en | `is this ifc4x3 or 2x3, I can't tell from the file name` | lowercase `ifc4x3`, `2x3` | Which schema is this file. |
| 7 | ru | `сколько в ифс IfcBuildingElementProxy и из каких категорий ревита` | `ифс`, `ревита` | How many proxies, from which Revit categories. |
| 8 | ru | `Текла выгрузила IFC4, в Navisworks одни оси, это фаза или что` | `Текла`, Latin `Navisworks` | Grids only after the import; phase issue? |
| 9 | ru | `в ифс4 файле есть зоны? сколько` | `ифс4` | Are there zones in an IFC4 file. |
| 10 | zh | `revit导出的ifc里门窗都变proxy了，帮我数一下` | lowercase, no spaces | Doors and windows became proxies; count them. |
| 11 | zh (Taiwan) | `這份IFC檔的GUID跟上一版有沒有變` | `IFC檔`, Traditional | Did the GUIDs change since the last version. |
| 12 | zh | `ifc文件里楼层名乱码了，查一下哪些构件受影响` | mojibake wording | Floor names garbled; which elements. |
| 13 | ja | `IFCのスペースを一覧にして、面積も出して` | Latin IFC, katakana word | List the spaces with areas. |
| 14 | ja | `ArchicadのIFC、クラス別の数をだして` | Latin product name | Count by class from an Archicad IFC. |
| 15 | ko | `이 ifc에 프록시 몇 개 있어? 레빗 카테고리별로` | `레빗`, particle on `ifc` | Count proxies by Revit category. |
| 16 | es | `cuantos proxys hay en el ifc de archicad?` | missing accent, `proxys` | How many proxies in the Archicad IFC. |
| 17 | pt | `lista as paredes do ifc que nao tem pset` | dropped tilde | List walls without a property set. |
| 18 | de | `welche Wande im IFC haben keine FireRating, bitte als Liste` | `Wande` for `Wände` | Which walls lack FireRating. |
| 19 | fr | `combien de portes dans l ifc et lesquelles n ont pas de pset` | apostrophes dropped | How many doors, which lack a pset. |
| 20 | it | `quanti proxy ci sono nel file IFC? raggruppali per categoria` | none (control) | Count proxies by category. |

Prompt 20 is a deliberate **no-slip control**: roughly 3 of 4 casual prompts in a batch should look like it (clean, in the person's own style).

---

## 15. For judges: what an MCP server should do with these variants

A server (or the assistant driving it) should treat these as the same thing and say what it assumed.

| Input | Expected behaviour | Pass signal | Fail signal |
|---|---|---|---|
| `ifc`, `IFC`, `Ifc`, `.ifc` | Treat as the IFC format. | Works. | Asks "what is ifc?" |
| `IFC4x3`, `ifc4x3`, `IFC 4.3`, `IFC4X3_ADD2` | Map to the stored `IFC4X3_ADD2` and state it. | Names the real schema found in the file. | Passes the user's string to a library and returns "No schema named IFC4x3". |
| `2x3`, `IFC2x3 CV2`, `ifc3X2` | Accept `2x3` and `CV2`; for `3X2` ask or infer `2X3` and say so. | Reports `IFC2X3` and the view. | Rejects without help. |
| `IFC5`, `Ifc5D` | Clarify: IFC5 is only an alpha, not a production schema; `5D` is cost. | Asks one short question. | Pretends an IFC5 production schema exists. |
| `IFCWALL`, `IfcWall`, `ifcwall` | Same class. | Same count. | Different counts per case. |
| `IfcBuildingElementProxi`, `IFCELEMENTASSEMLBY` | Say "closest class is X" and proceed or ask. | One short correction. | Silent wrong class or silent empty result. |
| `Qto_SpaceBaesQuantities` | Suggest `Qto_SpaceBaseQuantities`. | Corrects. | "0 results" with no hint. |
| `GUID`, `GlobalId`, `IfcGuid`, `Global ID` | One concept: the element's global id. | Returns the 22-character id. | Confuses it with Revit `UniqueId` without saying (see the [dictionary](jargon_slang_dictionary.md)). |
| `revit`, `REVIT`, `Ревит`, `레빗` | Understand the product. | Proceeds. | Asks which software. |
| `Navis`, `Навис`, `нависа` | Understand Navisworks. | Proceeds. | Treats as a word. |
| `BlenderBIM` | Understand as Bonsai's earlier name. | Proceeds; may mention the rename. | Says "no such tool". |
| `IFС` with a Cyrillic С | Normalise confusable letters or at least warn. | Works or warns. | Silent "not an IFC file". |
| `ифс` | Understand as IFC in Russian chat. | Proceeds. | Answers about a different acronym. |

Judging rule of thumb: the server should *either* correct silently and say what it did, *or* ask **one** short question. It should never return an empty result with no explanation because of a spelling difference.

---

## Gaps

- No real casual chat to an AI assistant exists in the corpus. Every "typed to the AI" spelling is synthetic or assumed. The real data is forum titles, issue titles, blog posts and vendor pages.
- Cyrillic spoken forms (`ифс`, `ифц`, `проксики`, `нависворкс`) are reported by researchers but appear in **no** real record text; the real Russian titles use Latin names.
- `AIFC`, `IFS`, `ИФК`, `Revitt`, katakana product names, full-width Latin and keyboard-layout slips were searched for and are **absent**; they are P in this file.
- Portuguese, French, Korean, Arabic, Turkish, Greek and Polish have no real casual spelling evidence; Polish has none at all.
- Counts in section 1 and section 8 are from record text, which is partly paraphrase; real raw spelling may be rougher than shown.
- `wave2` research was not available; rerun the counts when it is.
