# Other languages (Arabic, Persian, Turkish, Polish, Czech, Estonian and the rest): how people ask about IFC, BIM and Revit

**Read this first: the data for these languages is very thin.** After wave 1 the whole knowledge base holds **9 records** in the "other" language codes (5 real, 4 synthetic), against 2,414 in English and 253 in Russian. Most of the 5 real records are *English-language GitHub posts* written by people whose first language is probably Turkish, Czech or Danish (the `lang` code was inferred from the content, not from the post language). Only two real records contain actual native-language text (Slovak, Vietnamese), and neither is a forum question from a human; see the table below. So this file is short on purpose. It tells a test writer what is known, what is only a hint, and what is missing. Do not treat any of it as a statistical picture of these communities.

Data basis: wave 1 only (`research_raw/wave1/`); no `wave2` files existed when this was written. Re-run this document after wave 2 if more languages arrive.

## Data inventory

| Language (code) | Real | Synthetic | Language of the real text | Where it comes from | Raw cell |
|---|---|---|---|---|---|
| Turkish (`tr`) | 1 | 2 | English (poster is likely Turkish; one-line issue with a pasted IFC line) | IfcOpenShell issue #101; prompts written by the research agent | `t-encoding` |
| Czech (`cs`) | 1 | 0 | English (Czech diacritics are the subject) | web-ifc issue #440 | `t-encoding` |
| Danish (`da`) | 1 | 0 | English (poster states the country, shows `V\X\E6gelement`) | web-ifc issue #358 | `t-encoding` |
| Slovak (`sk`) | 1 | 0 | **Slovak**, but the quoted prompts sit inside an issue written by the AI assistant itself | AIMviewer issue #65 (MCP viewer) | `ai-mcp-usage` |
| Vietnamese (`vi`) | 1 | 0 | **Vietnamese**, a README command, not a question | vn-revit-mcp README | `ai-mcp-usage` |
| Arabic (`ar`) | 0 | 1 | n/a (synthetic only) | prompt written by the research agent | `t-encoding` |
| Greek (`el`) | 0 | 1 | n/a (synthetic only) | prompt written by the research agent | `t-encoding` |
| Polish, Estonian, Persian, others | 0 | 0 | none | Polish appears only in one English-language record (see below); Estonian only in a national-policy doc; Persian nowhere | n/a |

Raw reports: [`t-encoding.md`](../../research_raw/wave1/topics/t-encoding.md), [`ai-mcp-usage.md`](../../research_raw/wave1/ai/ai-mcp-usage.md). Both reports say the web-search budget was exhausted before any native-language community (forums, Q&A sites, social networks) was reached. That is why the real records come almost only from GitHub.

A bias to keep in mind: the `t-encoding` cell was *designed* to look for non-ASCII letters, so "encoding" dominates the table above. It does not mean Turkish, Czech or Danish users only ask about encoding.

| Language | Jump to |
|---|---|
| Turkish | [style](#turkish) / [real](#turkish-1) / [prompts](#turkish-prompts) |
| Czech | [style](#czech) / [real](#czech-1) / [prompts](#czech-prompts) |
| Danish | [style](#danish) / [real](#danish-1) / [prompts](#danish-prompts) |
| Slovak | [style](#slovak) / [real](#slovak-1) / [prompts](#slovak-prompts) |
| Vietnamese | [style](#vietnamese) / [real](#vietnamese-1) / [prompts](#vietnamese-prompts) |
| Arabic | [style](#arabic) / [real](#arabic-and-greek) / [prompts](#arabic-prompts) |
| Greek | [style](#greek) / [real](#arabic-and-greek) / [prompts](#greek-prompts) |
| Polish | [style](#polish) / [real](#polish-english-language-record) / [prompts](#polish-prompts) |
| Estonian, Persian, Finnish, Swedish, others | [no data](#languages-with-no-records) |

## Where people ask (communities and platforms; activity; access notes)

What the data actually shows:

| Platform | Languages seen | What people post there | Access |
|---|---|---|---|
| GitHub issue trackers of open-source IFC tools: IfcOpenShell/Bonsai, ThatOpen `web-ifc`, xBIM, Autodesk `revit-ifc` | Turkish, Czech, Danish, Polish (all as English posts with local content) | Bug reports and feature requests about non-ASCII text, locale, parameter names, CSV decimal separator | Public, no login to read; posting needs a GitHub account |
| GitHub issues and READMEs of MCP servers (AIMviewer, vn-revit-mcp) | Slovak, Vietnamese | Tool requests, usage examples written in the local language | Public |

What is **not** covered (do not assume it does not exist): national forums, Facebook and Telegram groups, YouTube comments, university course sites, vendor support portals in Turkey, the Gulf states, Poland, Czechia, Slovakia, Greece, Vietnam, Estonia, Iran. The research budget ran out before any of them was queried. The Gulf-focused English cell (`en-middle-east-africa`) is explicitly marked incomplete and holds only 3 real records, none Arabic ([report](../../research_raw/wave1/en/en-middle-east-africa.md)).

Practical consequence for testers: for these languages the realistic scene is **a person who works in English-language tools (Revit, Archicad, IfcOpenShell) in a non-English country**, and who meets problems because their language has letters, number formats or parameter names that the tool chain handles badly.

## Top themes (ranked)

Ranked by how many of the 9 + 5 supporting records touch them. Treat the order as weak evidence.

| # | Theme | Evidence in the data | Language(s) |
|---|---|---|---|
| 1 | **Local letters in names and properties break or look wrong** (`\X2\`, `\X\E6`, question marks, parser drops the string) | `en-gh-encoding-r020`, `-r021`, `-r022`, `-r014`, synthetic `enc-s004`, `enc-s005`, `enc-s006`, `enc-s015` | Turkish, Czech, Danish, Arabic, Greek |
| 2 | **Locale side effects** in software: Turkish dotted I makes a type lookup fail; Polish Excel treats `12.5` as text | `en-gh-xbim-others-r003` (xBIM #670), `en-data-r006` (IfcOpenShell #4290) | Turkish, Polish |
| 3 | **Non-English parameter names in Revit export mapping** (Czech `Objem` / `Plocha` overwritten by built-in Volume / Area) | `en-ghrevitifc-r004`, `en-gh-proxy-r026`, `de-dach-r021` (all Autodesk `revit-ifc` #989) | Czech |
| 4 | **Asking an AI/MCP server in the local language**: count doors and rooms, quantities, camera control in a viewer | `sk-aimcp-r016`, `vi-aimcp-r042` | Slovak, Vietnamese |
| 5 | **National compliance checking** with a local-language tool (Turkish permit regulation checker) | MCP server `ifc-ruhsat`, described in [mcp_servers_and_ai_tools.md](../../04_open_source/mcp_servers_and_ai_tools.md) (README claims, unverified) | Turkish |

### Reference: what the local letters look like inside an IFC file

This is the single most useful fact for these languages. An `.ifc` file is ASCII-only text, so any non-ASCII letter is written as an escape (full rules in [02_ifc_file_anatomy.md, section 6](../../01_ifc_basics/02_ifc_file_anatomy.md)). The examples below were **computed for this document** (UTF-16 code points); the first row also matches the string quoted in the real Turkish issue.

| Text | Meaning | How it appears in a correct file |
|---|---|---|
| `Çİ` | start of a Turkish style name | `\X2\00C70130\X0\` (as in IfcOpenShell #101) |
| `İstanbul` | Istanbul, with dotted capital İ | `\X2\0130\X0\stanbul` |
| `Kuchyně` | Czech "kitchen" | `Kuchyn\X2\011B\X0\` |
| `Obývací pokoj` | Czech "living room" | `Ob\X2\00FD\X0\vac\X2\00ED\X0\ pokoj` |
| `Køkken` | Danish "kitchen" | `K\X2\00F8\X0\kken` (older tools may write `K\X\F8kken`) |
| `Vægelement` | Danish "wall element" | `V\X\E6gelement` in the real issue (ISO 8859-1 style escape; valid) |
| `غرفة` | Arabic "room" | `\X2\063A063106410629\X0\` |
| `χώρος` | Greek "space/room" | `\X2\03C703CE03C103BF03C2\X0\` |

Two escape styles (`\X\E6` and `\X2\00E6\X0\`) are both valid; seeing either is **not** corruption ([versions_mvd_encoding_guid.md](../by_topic/versions_mvd_encoding_guid.md) covers this with more real cases). Real breakage looks different: raw non-ASCII bytes written without escapes, malformed or lowercase hex, or `\X2` with the closing `\X0\` missing (Czech issue #440, Czech structural file in xBIM #533).

## Local ecosystem (regulations, national standards, local software, enthusiasts, open source; short, with links)

The knowledge base has **no dedicated national document** for Turkey, Czechia, Poland, Slovakia, Greece, Vietnam or the Arab states. What exists is below. Items marked *(unverified)* are marked so in the source document.

| Country / language | What the KB knows | Where |
|---|---|---|
| Turkey | MCP server `ifc-ruhsat` ("ruhsat" = permit) with Turkish tool names and a Turkish README; claims to check IFC against a Turkish regulation on digital project preparation (IFC 4.3, effective 1 Sept 2027, IFC delivery phased from 2029); flags IFC4 files as not meeting 4.3. All regulation details come only from the README *(unverified)*. | [mcp_servers_and_ai_tools.md, section 2.4](../../04_open_source/mcp_servers_and_ai_tools.md) |
| Czechia / Slovakia | No national BIM documents in the KB. Czech-named shared parameters appear in a Revit export bug; the `Objem`/`Plocha` pair is a known test case. Slovak appears only in an AI-viewer issue. | [ifc_export_reference.md](../../03_software/revit/ifc_export_reference.md) (mapped-parameter precedence, issue #989) |
| Poland | BIMvision, a free IFC viewer from a Polish vendor, with plugins (merge, split, clash, reports, BCF export). buildingSMART Poland listed as a chapter *in development/formation* (Wikipedia-derived list, may be out of date). | [viewers_checkers_cde_converters.md](../../03_software/viewers_checkers_cde_converters.md), [buildingsmart_standards.md, "Chapters and rooms"](../../02_standards_regulations/buildingsmart_standards.md) |
| Denmark | State-level executive order on ICT in construction ("IKT-bekendtgoerelsen") *(details unverified)*; `bips` guidance now hosted by Molio; buildingSMART Danmark is part of Molio; Danish classification CCS (Cuneco Classification System) *(unverified)*. Models are expected to carry CCS codes and project "informationskrav". | [nordics_baltics.md](../../02_standards_regulations/national/nordics_baltics.md) |
| Estonia | Digital Construction Cluster (Digitaalehituse Klaster, formed 2015); state building register ("ehitisregister"); whether IFC is accepted for permits is **not verified**. No Estonian user record exists. | [nordics_baltics.md](../../02_standards_regulations/national/nordics_baltics.md) |
| Greece | buildingSMART Greece listed as in development/formation *(snippet-based)*. | [buildingsmart_standards.md](../../02_standards_regulations/buildingsmart_standards.md) |
| Vietnam | Vietnamese-language MCP toolkits: `vn-revit-mcp` (the README in the real record; Claude builds levels, walls, rooms from a description or an AutoCAD drawing, then counts doors, rooms and quantities and exports Excel, run through pyRevit) and a registry listing `Innoprovn/vn-revit-mcp` v0.8.1; Vietnamese docs also on an AutoCAD + Trimble Connect server. Whether the two `vn-revit-mcp` names are related is not established. | [mcp_servers_and_ai_tools.md](../../04_open_source/mcp_servers_and_ai_tools.md) |
| Arab states | No official Arabic source found for Revit or ISO 19650 terms; the glossary Arabic column is best-effort and untagged. No Gulf authority rules were reached. | [glossary_multilingual.md](../../08_glossary/glossary_multilingual.md) (Gaps section) |
| Slovakia | Open-source viewer with an MCP interface (AIMviewer, GitHub repo `Menezeris/AIMviewer`) accepts Slovak prompts for camera control. | [issue #65](https://github.com/Menezeris/AIMviewer/issues/65) |
| Iran / Persian | Nothing. | n/a |

## How people write (register, typical length and structure, openers/closers, jargon and slang table, misspellings and name variants, code-switching, tone, context given or omitted)

### Patterns that hold across all of these records

- **Very short.** Real posts are one to three lines; the longest context is a pasted raw IFC line. Synthetic prompts in these languages are also one sentence.
- **Raw evidence first.** Reporters paste the failing STEP line (`IFCSURFACESTYLE('\X2\00C70130\X0\ZG...')`, `V\X\E6gelement`, a beam with `\S\` escapes) instead of describing the symptom.
- **Posted in English even when the topic is the mother tongue.** The Czech, Danish and Turkish reporters write English, sometimes "polite and brief", and name the country or alphabet ("I use UTF-8 because of AE O AA"; "probably other languages too").
- **Little context.** Given: tool name and version, sample file. Omitted: IFC schema version (most records say `unknown`), exporter settings, which viewer showed the problem.
- **Tone:** neutral to curious; one frustrated (Czech, "tested about 50 models, only 3 exported OK").
- **Local words stay inside English text:** Czech parameter names `OBJEM` / `PLOCHA` (upper case, as the user typed them), the Czech word `krokev` (rafter) in a beam name.

### Turkish

- Observed (synthetic, so a hypothesis about style): all-lowercase, no final question mark, a comma splitting two asks: "modeldeki isimlerde ş ğ ı İ gibi türkçe karakter geçen elemanları listele, doğru okunuyor mu bak". Even "türkçe" and "ifc" are lower-case.
- Loanwords take Turkish suffixes: `modeldeki` (model + de + ki, "in the model"), `ifc dosyasında` ("in the ifc file").
- Observed in the one real record: English, one line, a raw entity line.

| Term | Meaning | Standard / English term |
|---|---|---|
| bozuk mu? | "is it broken?" | corrupted file vs valid escape |
| kodlanıyor | "is being encoded" | `\X2\` escape |
| ruhsat | permit / licence | building permit |
| yonetmelik_kontrolu | regulation check (tool name in ifc-ruhsat; ASCII-only, no diacritics) | compliance audit |
| ek9_formu, ek5_siniflar, ek6_gerekenler | annex forms / mandatory classes / required attributes (tool names; "EK" = annex) | annex 9 form, annex 5 classes, annex 6 requirements |
| dotted İ / dotless ı | the two Turkish I letters | cause of `ToUpper()` bugs under `tr-TR` |

- Variants/misspellings: the real xBIM bug is a *name variant* problem (`i` uppercases to `İ`, not `I`, in Turkish culture). Tool names such as `yonetmelik_kontrolu` are written without Turkish letters, so do not expect `ö`/`ü` inside identifiers.

### Czech

- Observed: English reports with Czech content. Real parameter names `OBJEM`, `PLOCHA` are the Czech Revit UI words for Volume and Area; the clash with built-in parameters is the whole bug.
- Observed in a structural file: beam name with Czech text and `\S\` escapes mixed with raw characters.
- Hypothesis for synthetic prompts: use Czech with its diacritics intact (the user's own pain is that diacritics get lost), and keep Revit parameter names in Czech capitals when quoting them.

| Term | Meaning | Standard / English term |
|---|---|---|
| Objem | volume | Volume |
| Plocha | area | Area |
| krokev | rafter | roof rafter (IfcMember / IfcBeam in practice) |
| sdílené parametry | shared parameters (general Czech Revit wording; not in the data) | shared parameters |

### Danish

- Observed (real, English): short, states the country, names the letters "AE O AA" in ASCII, gives the wall name line from the file, asks for "UTF-8 style" handling.
- The user writes the letters in transliterated form (AE O AA) because the point is about those letters; a native prompt would write `æ ø å`.

| Term | Meaning | Standard / English term |
|---|---|---|
| Vægelement | wall element | IfcWall (name text) |
| æ ø å | the three Danish letters | `\X\E6`, `\X\F8`, `\X\E5` or `\X2\...\X0\` |
| informationskrav | information requirements | EIR / client requirements |

### Slovak

- Observed (real): short imperatives, no politeness markers, a percentage as a number: "Oddiaľ pôdorys o 15 percent." and "Ukáž vzduchotechniku v perspektíve na celú obrazovku." These are the prompts a human typed to an AI; the issue text around them was written by the assistant itself, in the form of a tool request (`request_tool`).
- Code-switching: English "tool" is used inside Slovak ("Nový tool: Ovládanie kamery", "new tool: camera control").
- Context given: which tool presets were tried (`set_camera` presets with targets). Omitted: IFC version, model name.

| Term | Meaning | Standard / English term |
|---|---|---|
| pôdorys | floor plan | plan view |
| vzduchotechnika | air handling / HVAC | MEP: ventilation |
| perspektíva | perspective view | 3D perspective camera |
| oddialiť | zoom out | relative zoom |
| celú obrazovku | the whole screen | fit to screen |

### Vietnamese

- Observed (real, README, not a question): a terse noun-phrase command, comma and semicolon separated, no verb: "Thống kê cửa, phòng; khối lượng tường, sàn". The README advises trying on a draft model first.
- Domain terms are Vietnamese; the tool stack (pyRevit, Claude, Excel) is named in English.

| Term | Meaning | Standard / English term |
|---|---|---|
| thống kê | count / tabulate | schedule, count |
| khối lượng | quantity (also "volume"/"mass") | quantity takeoff (QTO) |
| cửa | door (also "opening") | IfcDoor |
| phòng | room | IfcSpace / Revit Room |
| tường, sàn | wall, floor | IfcWall, IfcSlab |

Note: "khối lượng" is ambiguous between a measured quantity and a mass or volume; a judge should accept a quantity table, not only volumes.

### Arabic

- **No real Arabic text exists in the data.** The one synthetic prompt (written by the research agent, from its own knowledge) mixes standard vocabulary with a colloquial question: "شو المشكلة؟" ("what's the problem?", the word *شو* is typical of Levantine speech, not Modern Standard Arabic). It writes `IFC` in Latin letters in the middle of right-to-left text, and puts a Latin acronym inside Arabic with no spacing fixes. That mixing is plausible for chat but is a hypothesis.
- The glossary lists Arabic equivalents (best-effort): غرفة room, حيّز space, طابق storey, جدار wall, مجموعة خصائص property set, تصدير كـ IFC export as IFC ([glossary_multilingual.md](../../08_glossary/glossary_multilingual.md)).
- Direction matters for the file too: question marks instead of letters usually mean the *viewer font* or an earlier tool lost the characters, while the IFC file itself should hold `\X2\0627...\X0\` escapes (see reference table above).

### Greek

- **No real Greek text exists in the data.** The synthetic prompt is a full Greek sentence with a two-part ask and a polite informal tone: "δείξε μου τα ονόματα των χώρων στα ελληνικά, βγαίνουν σωστά ή με περίεργους χαρακτήρες;" Note the Greek question mark is `;`.
- No Greek terms appear in the glossary; none are asserted here beyond the words in the prompt (χώρος space/room, όνομα name, ελληνικά Greek).

### Polish

- Observed once, and only in an English post: the reporter says "In Poland Excel regional settings follow the interface language" so numbers with a dot become text; they use Power Query as a workaround, call it a minor problem, and sound polite (IfcOpenShell #4290, record `en-data-r006`). No Polish-language text was collected.

## Real questions (original language + EN gloss + persona + source link)

Only items in the data. "Original" is shown in the language the text was actually written in.

### Turkish

| Original text | EN gloss | Persona | Source |
|---|---|---|---|
| (English) "Unicode characters in IFC file made OBJ conversion fail." plus line `IFCSURFACESTYLE('\X2\00C70130\X0\ZG...')` | OBJ conversion fails on a surface style name with Turkish dotted İ and Ç; it used to work. Answer: write converted names in escaped form. | developer_programmer | [IfcOpenShell #101](https://github.com/IfcOpenShell/IfcOpenShell/issues/101) (2016) |
| (English) "IfcXml reading fails under Turkish culture (culture-sensitive ToUpper() in type lookup)" | On a machine with `tr-TR` locale, `i` becomes `İ` so no type matches; use `ToUpperInvariant`. Polished bug report with a failing test. | developer_programmer | [xBIM #670](https://github.com/xBimTeam/XbimEssentials/issues/670) (2026) |

### Czech

| Original text | EN gloss | Persona | Source |
|---|---|---|---|
| (English) "Encoding breaks when exporting the model" | After export from web-ifc the algorithm changes `\X2` to `\X` and `00E9` to `E9`; other viewers choke; user tested about 50 models, only 3 exported fine. Fixed later. | developer_programmer | [web-ifc #440](https://github.com/ThatOpen/engine_web-ifc/issues/440) (2023) |
| (English) "String decoding": beam `'\S\Z\S\^^l. n\S\ametk. krokev'` parsed empty, attributes null | Czech structural file mixes raw non-ASCII with `\S\` escapes (illegal IFC); user asks the parser to skip bad characters as other readers do. | developer_programmer | [xBIM #533](https://github.com/xBimTeam/XbimEssentials/issues/533) (2023) |
| (English) "I try to export OBJEM (Volume) and PLOCHA (Area) shared parameters but values are replaced with built-in Objem and Plocha. No matter how I configure the TXT file." | Case-insensitive name clash overwrites user parameters with built-in ones. Open bug REVIT-255184. | bim_coordinator | [revit-ifc #989](https://github.com/Autodesk/revit-ifc/issues/989) (2026) |

### Danish

| Original text | EN gloss | Persona | Source |
|---|---|---|---|
| (English) "UTF-8 encoding": "I use UTF-8 because of AE O AA ... values read like V\X\E6gelement; probably other languages too" | Danish letters in property values show as `\X\E6`; asks for UTF-8-style handling. Answer: `\X\E6` is the ISO 8859-1 escape for æ; the library should decode on read. | architect | [web-ifc #358](https://github.com/ThatOpen/engine_web-ifc/issues/358) (2023) |

### Slovak

| Original text | EN gloss | Persona | Source |
|---|---|---|---|
| "Oddiaľ pôdorys o 15 percent." / "Ukáž vzduchotechniku v perspektíve na celú obrazovku." (issue title: "Nový tool: Ovládanie kamery") | "Zoom the floor plan out by 15 percent." / "Show the ventilation in perspective, full screen." The preset-based `set_camera` did not move the camera; a relative zoom/pan/orbit and fit-to-visible tool is needed. | bim_manager | [AIMviewer #65](https://github.com/Menezeris/AIMviewer/issues/65) (2026) |

### Vietnamese

| Original text | EN gloss | Persona | Source |
|---|---|---|---|
| "Thống kê cửa, phòng; khối lượng tường, sàn" (README command) | "Count doors and rooms; wall and floor quantities." Part two of the toolkit counts and exports Excel; command runs fixed scripts via pyRevit. Pre-release 0.2.0. | architect | [vn-revit-mcp](https://github.com/andyluu98/vn-revit-mcp) (2026) |

### Arabic and Greek

No real records. The only items are the synthetic prompts listed below.

### Polish (English-language record)

| Original text | EN gloss | Persona | Source |
|---|---|---|---|
| (English) "Decimal separator in ifcCsv": in Poland Excel regional settings follow the interface language, so dotted numbers become text; Power Query fix today | ifcCsv export should offer a comma decimal separator; maintainers also suggested CSV dialects. | bim_coordinator | [IfcOpenShell #4290](https://github.com/IfcOpenShell/IfcOpenShell/issues/4290) (2024) |

## Ready test prompts (curated/rewritten for realism; tagged intent/difficulty; expected behavior in English)

**All prompts in this section are synthetic.** "From data" means the text is an existing record (real prompt or synthetic record in the JSONL). "New" means written for this document, inspired by the named real record, and is **not** in the JSONL. A native-speaker review of the new prompts is recommended before using them for scoring, since no native-language human sample backed them.

`needs_file` = the prompt assumes an IFC (or Revit) model is loaded. Expected behavior assumes an MCP server that can read IFC properties and spaces; for a Revit server, replace GlobalId with element ID.

### Turkish prompts

| ID | Prompt | EN gloss | Intent / difficulty / needs_file | Expected behavior | Origin |
|---|---|---|---|---|---|
| tr-1 | modeldeki isimlerde ş ğ ı İ gibi türkçe karakter geçen elemanları listele, doğru okunuyor mu bak | List elements whose names contain Turkish letters and check they read correctly | query_model_data / easy / yes | Find names with Turkish characters, show decoded text and the raw escaped form, flag mismatches (especially dotted İ vs I) | From data: `enc-s004` |
| tr-2 | ifc dosyasında ğ ü ş harfleri neden \X2\ diye kodlanıyor? bozuk mu? | Why are ğ ü ş stored as `\X2\` codes? Is the file broken? | understand_concept / easy / no | Explain that IFC text files are ASCII-only and non-ASCII letters are written as `\X2\` UTF-16 hex escapes; it is normal, not corruption; offer to show an example from the loaded file if there is one | From data: `enc-s015` |
| tr-3 | A_blok.ifc ruhsat yönetmeliğine uygun mu? eksikleri listele, EK-9 formunu da çıkar | Does A_blok.ifc comply with the permit regulation? List what is missing and produce the EK-9 form | comply_regulation / hard / yes | If a Turkish compliance tool is connected, call its audit and form tools; flag if the file is IFC4 rather than IFC 4.3. On a generic server: say it cannot verify the regulation, offer to check classes and property sets the user provides. Do not invent article numbers. | New; adapted from the ifc-ruhsat README example in [mcp_servers_and_ai_tools.md](../../04_open_source/mcp_servers_and_ai_tools.md) |
| tr-4 | türkçe windows'ta ifcxml okurken tip bulamıyor, i harfi yüzünden olabilir mi? | On Turkish-locale Windows, reading ifcXML finds no types; could the letter i be the cause? | troubleshoot_code / medium / no | Recognise culture-sensitive upper-casing (`i` to `İ` under `tr-TR`); suggest invariant-culture comparison and a test with another locale; say it is a known class of bug in a .NET reader | New; inspired by `en-gh-xbim-others-r003` |

### Czech prompts

| ID | Prompt | EN gloss | Intent / difficulty / needs_file | Expected behavior | Origin |
|---|---|---|---|---|---|
| cs-1 | Exportuju z Revitu do IFC a sdílené parametry Objem a Plocha se mi v property setu přepisují vestavěnými hodnotami. Mapovací txt mám v pořádku. Co s tím? | Exporting from Revit to IFC, my shared parameters Objem and Plocha are overwritten by built-in values in the property set although the mapping txt is right. What now? | troubleshoot_export / medium / yes | Explain the case-insensitive name clash with built-in Volume and Area, reported as an open Autodesk bug; suggest renaming the shared parameters (e.g. with a prefix) and re-checking the exported pset values; do not claim it is fixed | New; inspired by `en-ghrevitifc-r004` (revit-ifc #989) |
| cs-2 | v ifc mám nosník s českým názvem a načte se jako prázdná instance, všechny atributy jsou null. v čem je chyba? | In the ifc I have a beam with a Czech name that loads as an empty instance with all attributes null. What is wrong? | troubleshoot_import / medium / yes | Show the raw entity line, spot raw non-ASCII bytes mixed with `\S\` / `\X\` escapes, explain that this is invalid IFC and a tolerant reader or a re-export fixes it | New; inspired by `en-gh-encoding-r014` |
| cs-3 | vypiš všechny místnosti s diakritikou v názvu a ukaž, jak jsou uložené v souboru | List all rooms with diacritics in the name and show how they are stored in the file | query_model_data / easy / yes | List IfcSpace Name/LongName with non-ASCII letters; show decoded and raw (`\X2\011B\X0\` style) forms; flag any broken sequences | New; inspired by `en-gh-encoding-r021` |

### Danish prompts

| ID | Prompt | EN gloss | Intent / difficulty / needs_file | Expected behavior | Origin |
|---|---|---|---|---|---|
| da-1 | Egenskabsværdierne med æ, ø og å står som \X\E6 i min IFC-fil. Er filen i stykker, eller skal programmet bare læse den rigtigt? | Property values with æ, ø, å show as `\X\E6` in my IFC file. Is the file broken, or should the program just read it properly? | understand_concept / easy / no | `\X\E6` is a valid ISO 8859-1 escape for æ; the file is fine, the reader must decode it; offer to check the loaded file for real corruption (raw bytes, malformed hex) | New; inspired by `en-gh-encoding-r022` |
| da-2 | Find alle vægge hvor navnet indeholder æ, ø eller å, og vis både den rå streng og den afkodede | Find all walls whose name contains æ, ø or å and show both the raw and the decoded string | query_model_data / easy / yes | List IfcWall names with those letters, with raw escaped and decoded text side by side | New; inspired by `en-gh-encoding-r022` |

### Slovak prompts

| ID | Prompt | EN gloss | Intent / difficulty / needs_file | Expected behavior | Origin |
|---|---|---|---|---|---|
| sk-1 | Oddiaľ pôdorys o 15 percent. | Zoom the floor plan out by 15 percent | how_to (camera control) / medium / yes (viewer open) | Use a relative zoom (not only presets) and confirm the new zoom level; if only fixed presets exist, say the relative zoom is not supported | From data (real prompt in `sk-aimcp-r016`) |
| sk-2 | Ukáž vzduchotechniku v perspektíve na celú obrazovku. | Show the ventilation in perspective, full screen | how_to / medium / yes | Isolate or highlight the MEP ventilation elements, switch to a perspective camera, fit to screen; report if no such camera tool exists | From data (real prompt in `sk-aimcp-r016`) |
| sk-3 | Koľko dverí je na 2. nadzemnom podlaží? Rozdeľ ich podľa typu. | How many doors are on the 2nd above-ground storey? Break them down by type | query_model_data / easy / yes | Filter IfcDoor by IfcBuildingStorey, group by type name, state the storey name matched; ask which storey if naming is unclear | New |

### Vietnamese prompts

| ID | Prompt | EN gloss | Intent / difficulty / needs_file | Expected behavior | Origin |
|---|---|---|---|---|---|
| vi-1 | Thống kê cửa, phòng; khối lượng tường, sàn | Count doors and rooms; wall and floor quantities | extract_quantities / medium / yes | Count IfcDoor and IfcSpace; return wall and slab quantities (area and volume) with units; say when a quantity is missing in the model | From data (README command in `vi-aimcp-r042`) |
| vi-2 | Thống kê số lượng cửa đi và cửa sổ theo từng tầng, xuất ra Excel giúp mình | Count entry doors and windows per storey and export to Excel | extract_quantities / easy / yes | Group doors and windows by storey, produce an .xlsx or CSV file, report the path; state if some elements have no storey | New |
| vi-3 | Kiểm tra giúp mình những phòng nào chưa có tên hoặc diện tích bằng 0 | Check which rooms have no name or an area of zero | validate_check / medium / yes | List spaces with empty Name or zero/missing area, with ids; distinguish "no area stored" from "area is zero" | New |

### Arabic prompts

| ID | Prompt | EN gloss | Intent / difficulty / needs_file | Expected behavior | Origin |
|---|---|---|---|---|---|
| ar-1 | أسماء الغرف بالعربي تظهر علامات استفهام بعد تصدير IFC، شو المشكلة؟ | Room names in Arabic show question marks after exporting to IFC, what is the problem? | troubleshoot_viewing / medium / no | Explain `\X2\` escapes; check how the strings are actually stored in the file; if stored correctly, point to viewer font or right-to-left display; if already `?` in the file, the export lost them | From data: `enc-s005` |
| ar-2 | اعرض لي كل الغرف في ملف الـ IFC مع مساحة كل غرفة بالمتر المربع | Show me all the rooms in the IFC file with each room's area in square metres | query_model_data / easy / yes | List IfcSpace with Name and net or gross floor area (Qto_SpaceBaseQuantities), state which area is used and the model's length unit; say "not found" where the quantity is missing | New |
| ar-3 | كم عدد الأبواب والشبابيك في كل طابق؟ | How many doors and windows are on each floor? | query_model_data / easy / yes | Count IfcDoor and IfcWindow per storey; "شبابيك" is colloquial for "نوافذ" so the system must map both to windows | New |

### Greek prompts

| ID | Prompt | EN gloss | Intent / difficulty / needs_file | Expected behavior | Origin |
|---|---|---|---|---|---|
| el-1 | δείξε μου τα ονόματα των χώρων στα ελληνικά, βγαίνουν σωστά ή με περίεργους χαρακτήρες; | Show me the space names in Greek, do they come out right or with strange characters? | query_model_data / easy / yes | Read IfcSpace Name and LongName, decode, report any broken sequences | From data: `enc-s006` |
| el-2 | πόσα παράθυρα έχει ο κάθε όροφος; βγάλε μου και το εμβαδόν των χώρων ανά όροφο | How many windows does each floor have? Also give the area of the spaces per floor | query_model_data / medium / yes | Count IfcWindow per storey; sum space areas per storey, saying which area quantity is used; mention if some spaces have no storey | New |

### Polish prompts

| ID | Prompt | EN gloss | Intent / difficulty / needs_file | Expected behavior | Origin |
|---|---|---|---|---|---|
| pl-1 | wyeksportuj zestawienie pomieszczeń z powierzchniami do CSV tak, żeby polski Excel nie traktował liczb jako tekstu (u mnie kropka zamiast przecinka) | Export the room schedule with areas to CSV so that Polish Excel does not treat the numbers as text (my numbers use a dot instead of a comma) | convert_format / medium / yes | Export spaces with areas; explain the decimal separator issue; offer comma decimals with semicolon delimiter or XLSX instead; state which choice was made | New; inspired by `en-data-r006` |

## Tips for generating authentic prompts in this language (do / don't)

**Do**
- Make the *problem* local, not the whole sentence: the realistic pain for these users is local letters, number format, local parameter names, or a local-language regulation. Keep tool and class names in English (`IfcSpace`, `set_camera`, `Pset_WallCommon`).
- Keep diacritics and non-Latin letters intact in the prompt when the subject is those letters (ş ğ ı İ, ě š č ř, æ ø å, غ ر ف ة). A prompt that loses its own diacritics defeats the test.
- Paste evidence: include a raw line like `V\X\E6gelement` or `\X2\00C70130\X0\` when the persona is a developer or a BIM coordinator checking the file.
- Keep prompts short: one sentence, at most two asks, lower-case is fine (Turkish example), imperative verbs (Slovak, Vietnamese, Turkish).
- Leave context out: no IFC version, no export settings, no file size. The real posts rarely give them.
- Mix registers where the language does: Arabic chat with a colloquial word and `IFC` in Latin letters; English "tool" inside Slovak.
- For Czech / Polish / Turkish / Danish developers, an *English* message that mentions the local detail is as realistic as a native one (that is what the data shows).

**Don't**
- Don't present these prompts as real quotes. Only the Slovak and Vietnamese lines marked "From data (real)" are observed; all others are synthetic.
- Don't invent national rules (Czech, Polish, Estonian, Arab-state BIM mandates). The KB has none verified; ask the system to say what it cannot verify (see the Turkish compliance case).
- Don't claim a bug is fixed. The Czech `Objem`/`Plocha` issue was open at the last check (REVIT-255184).
- Don't treat `\X\E6` vs `\X2\00E6\X0\` as an error; both are valid. Real errors are raw bytes, bad hex, missing `\X0\`.
- Don't assume question marks in a viewer mean the file is bad; check the raw string first.
- Don't use one language's glossary terms for another: for Arabic, the KB itself says the glossary is best-effort ([glossary_multilingual.md](../../08_glossary/glossary_multilingual.md)).

**Judging notes**
- A good answer in these languages should answer in the user's language (or the language of the prompt), keep IFC class names and `GlobalId` values unchanged, and show the raw escape next to the decoded text when the question is about letters.
- For compliance prompts (Turkish, Danish), a correct answer states its limits ("I cannot verify the regulation text") instead of quoting articles.

## Languages with no records

| Language | Status | What to do |
|---|---|---|
| Persian | No record, no mention in any report. | Do not generate "authentic" Persian prompts from this KB; a future research wave must sample real sources first. |
| Estonian | No user record. Only a policy mention (Digital Construction Cluster, building register; IFC acceptance for permits unverified) in [nordics_baltics.md](../../02_standards_regulations/national/nordics_baltics.md). | Treat Estonian as English-speaking-with-local-names until sampled. |
| Finnish, Swedish, Icelandic, Hungarian, Romanian, Ukrainian, Hebrew, Hindi, Indonesian, others | No record. Finnish and Swedish national context exists in the Nordic doc (RYTV/YTV, BIM Alliance), but there is no user text. | Same as above. |
| Arabic (more depth) | One synthetic prompt only; Gulf regulations not reached. | Re-run the Middle East cell; sample Arabic forums and social media. |
| Polish, Czech, Slovak, Greek, Turkish (more depth) | A handful of records, mostly English-language GitHub posts. | Add national forums (Q&A, Facebook groups, university pages), local vendor support portals, and public regulations. |

See also: [versions_mvd_encoding_guid.md](../by_topic/versions_mvd_encoding_guid.md) (all encoding cases, including Russian, Chinese, Japanese, French), [02_ifc_file_anatomy.md](../../01_ifc_basics/02_ifc_file_anatomy.md) (escape rules), [mcp_servers_and_ai_tools.md](../../04_open_source/mcp_servers_and_ai_tools.md) (tools with local-language READMEs), [glossary_multilingual.md](../../08_glossary/glossary_multilingual.md).
