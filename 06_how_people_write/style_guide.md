# Style guide: how real people write about IFC, Revit and openBIM

**Audience:** a tester (or an LLM acting for one) who has no BIM background and must write requests that sound like a real person typed them to an AI assistant connected to an IFC model or to Revit.
**Companion file:** [anti_patterns_llm_questions.md](anti_patterns_llm_questions.md) (what invented questions look like, 40+ before/after pairs, rewriting rules).
**Data basis:** the JSONL records under `research_raw/wave1/` (3,525 records at the time of writing: 2,256 real, 1,269 synthetic) and the "How people write" sections of the 77 cell reports. Reference docs: [IFC in real projects](../01_ifc_basics/00_ifc_in_real_projects.md), [multilingual glossary](../08_glossary/glossary_multilingual.md), [abbreviations](../08_glossary/abbreviations.md), [real questions by language](../05_real_world_questions/by_language/ru.md).

---

## 0. The ten rules in one screen

1. **People start from the symptom or the task, not from a greeting.** On GitHub and dwg.ru there is usually no greeting at all. A title often is the whole question: "Link IFC fail", "Export IFC - wrong position !".
2. **Short.** Median real title: 7 words in English and Russian, 24 characters in Chinese/Japanese. A typed request to an AI is usually one line (10 to 25 words).
3. **Context is partial and lopsided.** About half the real records never say which IFC schema is involved; a software version number appears in under a third of them. People give what they happen to know: the Revit year, the file size, "opens fine in another viewer".
4. **Evidence beats explanation.** People paste an error line, a screenshot, a STEP line (`#1929=IFCCURVEBOUNDEDPLANE(...)`) or a number ("12MB: 222s vs 2s") instead of describing the problem.
5. **Jargon is used loosely.** "Proxy", "pset", "mapping", "export", "IFC4" mean different things to different people. Revit words (family, category, link) are applied to IFC.
6. **Local slang and transliteration are normal:** ифс, ревит, текла, навис, проксики; `revit导出ifc`; 레빗; "ifc" in lowercase.
7. **Emotion is understated.** Frustration shows through numbers, "again", "still", a customer or an expert panel who is waiting. Shouting ("!!!") exists but is rare (about 1% of titles).
8. **Politeness depends on the place and the language,** not on the topic: polite and long on buildingSMART forums, none on GitHub and in Russian forums, blunt imperatives when talking to an AI.
9. **Mess is small and local:** one typo, one missing accent, one mixed-up term, one pasted log. Never a whole message of noise.
10. **The "why" is often there:** "заказчик требует IFC", "need it for handover friday", "the expert panel does not accept proxies". That motive is what makes a request feel real.

---

## 1. What the data can and cannot tell us

### 1.1 Three registers (do not mix them up)

| Register | Where it was observed | Typical shape | Use it for |
|---|---|---|---|
| **A. Post to humans** (forum thread, GitHub issue, Q&A) | 2,256 real records: GitHub issues 1,204; forums 628; blogs 244; Q&A, vendor KB, video, social, papers, regulation texts the rest | Title that states the symptom, short body, version/screenshot/log, sometimes numbered sub-questions, thanks at the end on forums | Content of problems; context habits; terminology errors; emotion |
| **B. Prompt typed to an AI that already "sees" the model** | A few dozen real examples: README prompt lists of MCP servers ("list all pipes in the revit model"), prompts quoted inside GitHub issues, plus 1,269 synthetic records written for this KB | One line, imperative, no greeting, deictic ("this model", "эту модель", "这个ifc"), output format at the end ("csv ok", "list names + guids") | **The actual test requests.** Take the content from A, the form from B. |
| **C. Search-style fragment** | Zhihu/Baidu titles, forum titles, YouTube titles | Noun phrase + "怎么办", "как открыть IFC", "IFC viewer free" | Beginner and tool-finding requests |

Evidence for register B is thin in the real data. Only a handful of genuine user prompts were captured (README examples, quotes inside issues such as `en-aimcp-r003` and `en-aimcp-r020`). The rest of register B is **synthetic and labelled so** in the data (`kind: synthetic`).

### 1.2 Real records per language (what the language sections below rest on)

| Language | Real | Synthetic | Quality of evidence for "how people type" |
|---|---|---|---|
| English | 1,796 | 618 | Strong for GitHub/forum English (heavily non-native speakers). Reddit, Stack Overflow, Quora, YouTube comments were **not** collected. |
| Chinese (zh) | 166 | 132 | Good for titles (Zhihu, Baidu, CSDN, cnblogs, GitHub). Many CSDN items are polished or auto-generated summaries; treat as low trust for "voice". |
| Russian (ru) | 104 | 149 | Medium: about 40 genuine forum questions (dwg.ru), the rest are Habr articles, Telegram posts, video titles. Three of six Russian cells found no real posts. |
| Japanese (ja) | 57 | 47 | Blog-style (Zenn, Qiita, note). Real "questions to a forum" are rare. |
| Spanish (es) | 33 | 67 | Thin; a few genuine short posts, many institutional pages. |
| Italian / Dutch / Norwegian | 28 / 21 / 13 | 42 / 14 / 17 | Italian is article-derived; Dutch is mostly GitHub issues from standard-setting groups; Norwegian is institutional (low confidence). |
| German (de) | 22 | 53 | German is mostly blog titles; DACH forum users write in English with German parameter names. |
| Korean (ko) | 8 | 40 | **No real user question.** Real records are institutional pages. Everything about casual Korean is a hypothesis. |
| French (fr) / Portuguese (pt) | 2 / 1 | 43 / 43 (28 pt + 15 pt-BR) | **Essentially no real posts**; the real records are English or Portuguese issues on GitHub. Casual style is a hypothesis. |
| Arabic (ar) | 0 | 1 | **No data.** One synthetic prompt about garbled Arabic room names. |
| tr, sk, vi, cs, da, el | 1 each (tr, sk, vi, cs, da) | tr 2, el 1 | Anecdotal. |

**Honest limits.**
- In the real records the field `question_paraphrase` is a *paraphrase* (often a neutral summary), so its length and wording are **not** the original length and wording. Titles of 20 words or fewer are verbatim. All length statistics below therefore use **titles** (verbatim) and the cell reports' notes on body length.
- Percentages taken from `phrasing_notes` (typos, screenshots, greetings) are **lower bounds**: the notes were not coded systematically.
- 41 record ids occur in two files (for example `en-osarch-r012`), so the **source URL is the canonical reference** for every example below.
- Several records share one thread, so independent voices are fewer than rows.

---

## 2. Length

### 2.1 Observed (real titles, verbatim when 20 words or fewer)

| Group | n | min | p10 | p25 | median | p75 | p90 | max |
|---|---|---|---|---|---|---|---|---|
| English titles (words) | 1,773 | 1 | 3 | 5 | **7** | 10 | 12 | 25 |
| Russian titles (words) | 104 | 1 | 3 | 5 | **7** | 8 | 10 | 13 |
| All other languages (words) | 133 | 1 | 3 | 4 | **6** | 8 | 10 | 17 |
| Chinese + Japanese titles (characters) | 223 | 7 | 14 | 18 | **24** | 33 | 42 | 99 |

For comparison, the synthetic prompts already in this KB (typed-to-AI register) are: English median **15 words** (p10 10, p90 22), Russian 14, other European 15, zh/ja 36 characters. None of the 1,269 contains a line break.

### 2.2 Body length bands (from the cell reports)

| Band | Share / evidence | Who and where |
|---|---|---|
| **Title only, empty body** | at least 7% of real records are flagged "title only" in the notes; many bare titles on GitHub ("Can't open an IFC file", "PR: Link IFC fail") | Beginners, frustrated users, anyone filing from a phone or in a hurry |
| **One to three sentences** | "concise, often one to three sentences" (US/Canada infra cell); one-line tool questions (Spanish, Chinese) | Coordinators, estimators, MEP engineers |
| **Two to eight sentences + screenshot or log** | the commonest forum shape (Dynamo, Autodesk forums, OSArch) | Architects, coordinators |
| **GitHub bug template (3 to 10 lines)** | revit-ifc: Problem Description / Revit Version / Add-in Version / Windows Version; That Open: 1 to 5 lines + stack trace | Developers, power users |
| **Long and structured** | buildingSMART forum posts with numbered sub-questions (a to f); Taiwan Chinese proposals with 問題說明 / 建議修改 / 驗證結果; MCP proposals with tables; Habr retrospectives | Developers, BIM managers, academics |

### 2.3 Recommendation for generated requests (derived, not measured)

| Register | Words | Share of a test batch (suggested) |
|---|---|---|
| Typed to AI, one line | 6 to 25 (zh/ja: 15 to 50 characters) | about 60% |
| Typed to AI, line + one pasted detail (error line, path, STEP line, list of 3 to 6 names) | 20 to 60 | about 25% |
| Forum-style paragraph (context first, 3 to 6 sentences) | 40 to 120 | about 10% |
| Title-only fragment ("revit导出ifc没有东西") | 2 to 8 | about 5% |

---

## 3. Structure: context-first or question-first?

| Pattern | What it looks like | Seen mostly in | Example (source) |
|---|---|---|---|
| **Symptom-first title, no body** | The title states what broke; nothing else | GitHub (revit-ifc, IfcOpenShell), Chinese Q&A | "Link IFC fail" ([link](https://github.com/Autodesk/revit-ifc/issues/951)) |
| **Question-first** | The ask comes first, one clause of context after | Russian forums, Zhihu, typed-to-AI prompts | "Как пересести из ifc в dwg ?" ([link](https://forum.dwg.ru/showthread.php?t=96356)) |
| **Context-first narrative** | Who I am / what the project is, then the problem, then the question near the end | buildingSMART forum, OSArch, Habr | "Roadmap for Revit migrator to Bonsai BIM - absolute beginner" ([link](https://community.osarch.org/discussion/3765/roadmap-for-revit-migrator-to-bonsai-bim-absolute-beginner)) |
| **Compare-two-paths** | "Works in A, fails in B", often with version numbers | GitHub regressions, Autodesk forums | "22.4.2 ok, 23.2.3 not ok"; "fine in Revit 2023/2024, broken in 2025-2027" (revit-ifc cell reports) |
| **Template-driven** | Fixed headings filled in tersely | revit-ifc, That Open, Chinese zh-TW proposals | "PR: Problem with Z coordinate when using Link IFC" ([link](https://github.com/Autodesk/revit-ifc/issues/990)) |
| **Question list** | Numbered or lettered sub-questions (2 to 6) | buildingSMART forum, newcomers in MCP repos | "3 numbered questions, non-native English" ([link](https://github.com/LuDattilo/revit-mcp-server/issues/17)) |
| **Story-first (failure or discovery)** | A title that tells the outcome | Japanese blogs, Habr | "IFCに出したら、半分なかった" ([link](https://note.com/toshio_nakamura/n/nc8db42ce3191)) |

**Rule of thumb for typed-to-AI prompts:** question-first, with the *reason* either attached at the end ("need it before the coord meeting") or placed first as a short clause ("архитектор прислал ифс на 480 МБ, ..."). Do not open with "I am a BIM manager and I need you to ...".

---

## 4. How context is given

### 4.1 What real posts contain (counts over 2,256 real records)

| Context element | Observed | Comment |
|---|---|---|
| IFC schema identified (IFC2x3, IFC4, IFC4.3, ...) | about **50%**; the other ~50% are `unknown`, `unspecified`, empty or n/a | Writers say "IFC" and mean whatever the exporter defaulted to. Maintainers then ask "which version?" |
| Software name with a version number | **29%** | The Revit year ("Revit 2022") is the commonest; exporter build ("22.5.1.0", "25.4.40") appears mostly in GitHub bug templates |
| Any version-like number in the context list | about 11% (4-digit year pattern) | Under-counts because many context lists name tools without numbers |
| No context at all | **12%** (empty context list) | Title-only posts, short Q&A |
| Screenshot mentioned | at least 6% (notes) | Screenshots and attachments often carry the real information and are invisible to the dataset |
| Pasted code, error text, STEP line, traceback, log | at least 5% (notes mention code or logs), far more in developer cells | "System Error encountered during import" quoted verbatim inside a Russian sentence |
| File attached or offered | at least 3% (notes) | Frequently refused: "cannot be shared (NDA, workshared)", "IFC is private" |

### 4.2 The context ladder (how much each type of asker gives)

| Level | What is included | Typical asker |
|---|---|---|
| 0 | Title only | beginners, mobile posters, frustrated users |
| 1 | Symptom + one tool name ("Tekla to Revit, only grids appear") | architects, structural engineers, students |
| 2 | + software year ("Revit 2019", "Tekla 2017") | BIM coordinators, MEP engineers |
| 3 | + exporter build, IFC view (CV2.0, RV, DTV), second viewer used as a check, screenshot | experienced coordinators, BIM managers |
| 4 | + numbered repro steps, minimal file, expected vs actual, stack trace | developers (IfcOpenShell, xBIM, That Open, revit-ifc) |

### 4.3 Habitual evidence moves (copy these, they are how people prove a point)

| Move | Example (paraphrased or short fragment) | Source |
|---|---|---|
| **Cross-check in another viewer** | "opens fine in BIM Vision / Solibri but not in Revit"; "в BimSight открывается нормально" | revit-ifc issues; [dwg.ru](https://forum.dwg.ru/showthread.php?t=160240) |
| **Bisect by version** | "22.4.2 ok, 23.2.3 not ok"; "worked in 1.5.1" | revit-ifc, web-ifc cell reports |
| **Numbers with units** | "12MB: 222s vs 2s"; "100M的模型导出IFC可能有1GB"; "pesa 800mb"; "1500 коллизий vs 200"; "212 doors" | t-file-size, zh-lightweight-review, es-latam, Habr, nl-dutch |
| **Arithmetic to prove the point** | "$100/U x 5U = $500"; "9.80815 m2 vs 20.08 m2" | t-qto-cost report |
| **List of what was tried** | "tried ExportAs to IfcSpace", "raised Void Limit from 30 to 5000 without effect" | [OSArch](https://community.osarch.org/discussion/3754/opening-cuts-skipped-in-bonsai-studio-0-9) |
| **Quote the exact label or parameter** | "IfcExportAs", "Link IFC", "Apply Openings", "exportlayers-ifc-IAI" | Autodesk forums, Zhihu |
| **Quote the assistant back** | "Claude replies: unable to connect to Revit... will create a 10-meter wall once connected" | [mcp-servers-for-revit #1](https://github.com/mcp-servers-for-revit/mcp-servers-for-revit/issues/1) |
| **Say who is waiting** | "заказчик требует IFC", "эксперты не принимают прокси", "when a client asks why the IFC classes are wrong" | dwg.ru, t-proxy-mapping |

### 4.4 What is usually missing (leave it missing in generated requests)

IFC schema or MVD; exporter version; units; the exact property name; which viewer was used; the file itself; what the model contains ("a house" or "a bridge"); the expected result. Roughly: **give one or two context items, not six.**

---

## 5. Openers and closers per language

| Language | Openers observed | Closers observed | Notes |
|---|---|---|---|
| **English** | None (GitHub, most forum titles). "Hi all", "Hello everyone", "Hi Team", "Dear XBim Team", "Dear IFC developers", "G'day all" (OSArch, Australian), "Hello IFC gurus". "I know this is not a new topic" | "Thanks in advance", "Thanks already!", "Cheers", "Many thanks for your help", "Any idea what's happening here?", "Thoughts?", "Any updates on this?" | Politeness markers cluster among non-native writers and on buildingSMART/OSArch forums |
| **Russian** | None on dwg.ru; first-person narrative on Habr | "помогло", "спасибо" after a solution; irony in replies | Titles carry the software pair: "Экспорт из Tekla в Revit" |
| **Chinese** | None; Zhihu titles start with the topic | Humble closer 求教 / 请教; titles end with 怎么办 / 如何解决 / 是为什么？ / 求推荐 | Vendor notices address readers as 小伙伴; "亲测" ("tested personally") in workarounds |
| **Spanish** | "Hola", "Buenas tardes" (thesis context), "¡Hola! Les comparto..." (student blog) | "Que tengan un buen día" (in an international repo) | Formal wrapper appears when writing to an international (English) project |
| **Portuguese** | not observed | not observed | Synthetic style: "cara olha o ifc", "lista ai" (unverified) |
| **German** | "Hallo all" (German-influenced English), "Hi Team" | "bitte" in prompts (synthetic) | Real German is blog titles ("Die Wunderwaffe IFC") |
| **French** | "Hi team" in English posts | n/a | No real French posts |
| **Japanese** | None; blogs say 〜してみた, 〜という話, 調べてみた | hedges such as 〜と思います, 〜かもしれません; some notes invite corrections | Zenn: terse da/dearu; note: polite desu/masu with ■ headings |
| **Korean** | not observed | not observed | Synthetic casual style: 뽑아줘, 봐줘, ㅠㅠ (unverified) |
| **Dutch** | none; maintainers use Waarom / Nu / Gevraagd headings | "voor zover ik weet" (hedge), "oid" | "staat er op jullie roadmap ... oid?" |
| **Italian / Norwegian** | not observed in posts | n/a | Titles in question form ("e obbligatoria?"); Norwegian terse imperatives (inferred) |

---

## 6. Politeness

| Setting | Level | Evidence |
|---|---|---|
| GitHub issue (English) | Neutral, blunt; "polite" tag only about 4% of records | Titles: "Link IFC fail", "Floors not exporting" |
| buildingSMART forum, OSArch | Polite, collegial, long | "Dear IFC developers"; "warm thanks for free tools" in `en-osarch-r001` |
| Russian forums | No greeting, no "please" | dwg.ru titles are bare symptoms |
| Chinese Q&A | Titles blunt; humility in 求教 / 请教 | `zh-revit-export` cell |
| Beginners on GitHub | Over-polite, formal ("Could you please provide a simple tutorial?", "Dear authors") | [revit-mcp-plugin #5](https://github.com/mcp-servers-for-revit/revit-mcp-plugin/issues/5) |
| Typed to an AI (all languages, synthetic and README examples) | **Imperative, no "please" in 93% to 100% of prompts** (English 7% contain please/could you, Russian 1%, Chinese 0%); a "pls" or "плиз" is a light touch | KB statistics over 1,269 synthetic prompts |

Where politeness appears in typed-to-AI prompts it is short: "pls check ...", "по категориям плиз", "bitte", "...graag" (Dutch). Never "I would be very grateful if you could kindly".

---

## 7. Emotion and urgency

Tone tags over 2,256 real records: neutral 33%, frustrated 20%, confused 20%, curious 19%, polite 4%, skeptical 3%, urgent 1.5%.

| How it is expressed | Examples (short fragments from the cell reports or titles) |
|---|---|
| **Pressure from a person or a deadline** | "заказчик требует IFC"; "эксперты не принимают прокси"; "need to submit this tomorrow"; "cx submission tomorrow"; "para mañana"; "before the issue tonight" |
| **Repeated failure** | "i struggle since one year"; "tried apparently everything"; "I googled it, seen many videos"; "ради пустого параметра" (two hours of export for an empty parameter) |
| **Understated sarcasm or fatigue** | "коварная вещь"; "получается фигня"; "mission impossible"; "makes us apologize to the customers every time"; "IFC и аналитическая модель как молоток и кирпич" |
| **Self-deprecation** | "Or am I just too stupid"; "(albeit poorly constructed) model"; "knew I was doing something wrong" |
| **Venting punctuation (rare)** | "Revit crashes every time I export IFC!!!"; "Export IFC - wrong position !"; "真复杂！" |
| **Repeated pings** | "Any updates on this?"; "+1 same problem in 2022"; "any update?" over several years on revit-ifc #76 |
| **Strong verdicts in titles** | "mapping parameters severely lacking"; "unacceptable in a production environment" |

Typed-to-AI prompts carry the same markers in miniature: "again", "опять", "again??", "??", "срочно" are rarer than a plain **because-clause**: "эксперты не принимают прокси", "FM says rooms are empty", "AG fordert IFC4 Reference View".

---

## 8. Typos, casing, punctuation

### 8.1 Observed slips (in real titles and notes)

| Type | Examples | Source |
|---|---|---|
| Letter swaps | "Qto_SpaceBaesQuantities", "Strucutral ifc", "CoveringBaseQuantitie", "Widht", "Documantation", "Informatoin", "Thankx", "qantities", "Querry", "Ceisum JS" | revit-ifc, xBIM, IfcOpenShell titles |
| Entity names misspelled or pluralised | "IfcBuildingElementProxi", "IfcOpenning", "IFCELEMENTASSEMLBY", "IfcBuildingElementProxies", "IFCRoad", "ifc3X2" | Cell reports |
| Product names misspelled | "Cobiee", "COBIe", "OpenCeepy" (OpenSees), "blenderbim" after the rename to Bonsai | t-cobie-fm, t-structural |
| Plural apostrophe | "IFC's" | [Spanish forum](https://forums.autodesk.com/t5/revit-architecture-forum/problemas-con-ifc-s/td-p/10189111) |
| Missing accents / diacritics | "Exportacion", "Descripcion", "cuantos" | es-latam, es-spain |
| All caps | "SOPOTARÁ ARCHIVOS IFC?" (also a typo), "IFC EXPORT APPEARS IN DIFFERENT COLOUR", "REVIT 2019 LT: IFC Export - IFCSpaces are missing" | [IngeTrazo #1033](https://github.com/ingelibre/ingetrazo/issues/1033) |
| Mixed spelling | "colour/ color" in one title | t-materials-colors-layers |
| Unit slip | "Mo" for MB (French writers), decimal commas | That Open, xBIM cells |
| Run-on, no punctuation | "whats the root cause of grey MEP-components in IFC", "hidden shared parameters are not exported" | t-materials-colors-layers, t-psets-params and t-mep cell reports |

### 8.2 Casing patterns that carry meaning

- **Russian, Chinese, Spanish, Portuguese, Norwegian chat style:** lowercase start, software in lowercase or transliterated: `revit`, `ifc`, `ревит`, `ифс`, `текла`, `навис`.
- **Entity names:** CamelCase (`IfcBuildingElementProxy`) when copied from a viewer, UPPERCASE when copied from a STEP line (`IFCWALL`, `IFCRELAGGREGATES`), spoken form when typed from memory ("проксики", "ifcwall"). All three can coexist in one message.
- **Software versions:** "Revit 2022", "revit2019", "REVIT2020", "Revit2020" (no space) all occur in Chinese Q&A titles.
- **Sentence-final marks:** `?` ends 10% of real titles, `!` appears in 1%, `!?` and `??` occur in Russian forum titles ("Как редактировать семейство в модели!?"), a lone full stop at the end of a lowercase English title is common.

### 8.3 How much roughness to generate

At most **one** slip per prompt and not in every prompt: about 1 in 4 to 1 in 3 prompts of the casual kind may carry one (a dropped accent, a lowercase product name, a missing article, a plural slip). Never mangle the technical token that the task depends on (the property name, the class name, the number).

---

## 9. Code-switching and transliteration

| Pattern | Examples |
|---|---|
| **Entity, pset and tool names stay in Latin script inside local-language sentences** | `IfcBuildingElementProxy`, `IfcExportAs`, `GlobalId`, `Pset_WallCommon`, `create_wall`, `send_code_to_revit` |
| **Software transliterated into the local script** | ru: ревит, текла, архикад, сапфир, нанокад, навис, солибри; ko: 레빗, 아키캐드 (the Korean cell hypothesises 레빗/아키캐드; 아키캐드 is seen in a real announcement); ja: katakana ファセット, バリデーション |
| **Local verbs on foreign stems** | ru: "экспортнуть", "импортнуть", "затащить"; zh: 导进, 链进来; ja: 書き出し, 読み込み |
| **Plural/case endings on slang or Latin tokens** | ru: "проксей", "проксики"; "IFC's" in Spanish |
| **Error messages quoted in the UI language, sentence in another** | German "ungültige Daten auf Stammebene" inside an English report; English "System Error encountered during import" inside a Russian sentence |
| **Local parameter names inside English posts** | Czech `OBJEM`/`PLOCHA`, German `ARC_Tragwerk`, `_BA_Fenster_E`, Dutch `brandwerendheid`, French `Largeur` |
| **Local standard names with English glue** | ru: "ЦИМ", "АГР", "ТЭП", "ФОП", "МССК"; nl: NL-SfB, ILS, BVO; no: TEK17, MMI, FDV; de: LV, TGA, OKFF/OKRD; fr: DOE, GMAO, SDP; es: metrados, MIDE; zh: 报建, 轻量化, 翻模 |

Rule: **Don't translate technical tokens.** A Russian prompt with `IfcWall` is right; one that says "ИфкСтена" is wrong.

---

## 10. Vagueness and wrong terminology

People are imprecise in predictable ways. An assistant should be tested on understanding these, so generated requests should contain them (sparingly).

| What they say | What they usually mean | Evidence |
|---|---|---|
| "export" for any conversion ("export dwg to ifc4") | Convert / translate | [`en-viewconv-r004`](https://github.com/IfcOpenShell/IfcOpenShell/issues/3124); "Как пересести из ifc в dwg ?" |
| "edit the **family** from the IFC", "system family" | Revit vocabulary applied to IFC; IFC has types and occurrences, not families | [dwg.ru](https://forum.dwg.ru/showthread.php?t=130296&page=2); [revit-ifc #729](https://github.com/Autodesk/revit-ifc/issues/729) |
| "**category** decides the IFC class" | Believed in Revit; false, the class comes from export settings | Habr: "категории Revit не определяют IFC-класс" |
| "IFC4" | Often means Reference View or Design Transfer View, or just "newer than 2x3" | t-versions-mvd report |
| "IFC4 RV", "ifc3X2", "IFC 4.3" vs "IFC4X3" | Shorthand and slips for specific schema or view | t-versions-mvd, t-infra-ifc43 |
| "**mapping**" | Class mapping, parameter mapping, or property-set mapping, three different things | t-proxy-mapping, t-psets-params |
| "proxy" | `IfcBuildingElementProxy`, the generic leftover class | all cells |
| "**valid**" | Opens in my viewer; or passes the validator; or has all properties | Habr: "файл открывается не значит валиден" |
| "COBie" | The spreadsheet, the MVD subset, or the whole handover requirement | [`en-cobie-r001`](https://community.osarch.org/discussion/726/how-to-convert-an-ifc-file-to-cobie-using-ifcopenshell-or-other-python-based-solution) |
| "link IFC" / "open IFC" | Revit menu commands used as generic verbs | revit-ifc cell |
| "lightweighting" (轻量化) | Converting the model to a light viewable format (glTF, 3D Tiles), not removing data | zh cells |
| "room" and "space"; "zone" | `IfcSpace`; the word "зона" in Russian covers rooms, zones and АГР areas | Habr |
| "levels" / "floors" / "storeys" / "этажи" / "уровни" | `IfcBuildingStorey` (sometimes plus extra levels such as OKRD/OKFF in DACH) | de-dach |
| "the base point" | Project Base Point, Survey Point, internal origin or IfcSite placement, mixed freely | t-coordinates |
| "it doesn't open" | Crashes, hangs, opens empty, opens in the wrong place | t-viewers-conversion |
| "BBIM" / "blenderbim" | Bonsai (renamed) | beginner cells |

**Vagueness that is realistic:** "half my walls came out grey", "the file is heavy", "some elements are missing", "get the info out of the IFC". **Vagueness that is not realistic:** a request with no object at all ("check my model") unless it is a follow-up.

---

## 11. Multi-question posts and follow-ups

| Pattern | What it looks like | Evidence |
|---|---|---|
| **Two to three sub-questions** | "(1) port is hardcoded, (2) plugin must be started manually after each Revit restart" | [mcp-servers-for-revit #63](https://github.com/mcp-servers-for-revit/mcp-servers-for-revit/issues/63) |
| **Lettered list (a to f)** | long questions on buildingSMART forum and clash/BCF threads | t-clash-bcf report |
| **A task plus a safety clause** | "list them, don't delete"; "if there is no Qto, say so" | synthetic `ru-habr-dev-s005`, `ru-aimcp-s011` |
| **Piggy-backed second check** | "which storeys are there and are any elements not assigned to a storey?" | synthetic `ru-dwg-revit-s006`, `es-latam-s005` |
| **Self-answer and "[solved]"** | OSArch threads end with "[solved]" in the title; Autodesk board adds "Solved:" | OSArch, Autodesk forums |
| **Thanks only after the solution** | "помогло", "thanks, that fixed it" | dwg.ru, OSArch |
| **+1 and "any update?" chorus** | Years-long threads, repeated pings; "still a problem in version X" | [revit-ifc #529](https://github.com/Autodesk/revit-ifc/issues/529), [#76](https://github.com/Autodesk/revit-ifc/issues/76) |
| **Thread revival** | Same Tekla-to-Revit thread active in 2018, 2023 and 2024 | ru.md in `05_real_world_questions` |
| **Maintainer asks for the file** | "attach the .ifc", "does the validator say anything", answered later with a zipped file renamed `.txt` | IfcOpenShell, xBIM cells |
| **User cites a failed AI attempt** | "ChatGPT and Gemini didn't help"; shared ChatGPT link in comment | [Dynamo forum](https://forum.dynamobim.com/t/help-with-automated-quality-check-script-getting-empty-list-and-blank-excel/112252) |
| **Follow-up inside the same assistant chat** | "теперь только по 2 этажу", "and just for structure", "same but csv" | typical for register B (inferred, not logged in data) |

For test generation: roughly **one in five** requests may be a two-part request; **one in ten** a follow-up that only makes sense after a first answer (mark it explicitly in the test case).

---

## 12. The assistant-prompt register (typed to an AI with a model loaded)

This is what the test requests should look like. Features, with evidence:

| Feature | Detail | Evidence |
|---|---|---|
| Imperative, no greeting | "list all pipes in the revit model", "dimension every wall on this view" | MCP README prompts (`en-aimcp-r040`, `en-aimcp-r020`) |
| Deictic reference to the loaded model | "this model", "эту модель", "这个ifc", "este ifc", "このIFC" | Synthetic prompts in this KB and README examples almost never give a file path |
| Output format at the end | "csv ok", "list names + guids", "as a table I can paste in excel", "таблицей", "en lista" | Synthetic en, ru, es |
| Numbers with units, specific thresholds | "tolerance 10mm", "bbox in 5 mm", "RUS_Area diff > 0.5 m2", "Level 02" | Synthetic; Habr; `en-aimcp-r007` mm coordinates |
| Honest-answer clause | "if there is no Qto, say so", "не удаляй, просто список" | `ru-aimcp-s011`, `ru-habr-dev-s005`; README of bim-ifc-mcp stresses anti-hallucination |
| Constructive commands on the model | "Creá cuatro muros de 3 m de alto formando un rectángulo de 5 × 4 m"; "put the sofa here, by the window" | [archicad-mcp](https://github.com/joacos/archicad-mcp), [revit-mcp-server #16](https://github.com/LuDattilo/revit-mcp-server/issues/16) |
| Short Slovak-style relative commands | "Oddiaľ pôdorys o 15 percent." (zoom the plan out by 15 percent) | [AIMviewer #65](https://github.com/Menezeris/AIMviewer/issues/65) |
| Natural-language Q&A for non-experts | "How many fire doors are on Level 2?", "how many windows, doors, chimneys, or ramps" | [ifcopenshell-mcp](https://github.com/Daviidro/ifcopenshell-mcp), [IFC-MCP](https://github.com/ekkodale/IFC-MCP) |
| Failure reports quote the assistant | Users paste what the assistant answered | `en-aimcp-r003`, `en-aimcp-r020` |

What differs from a forum post: no persona introduction, no thanks, no explanation of IFC concepts, and the assistant is assumed to already know which file. The content (problems, class names, roles) comes from register A.

### 12.1 Roughness dial by persona (recommendation)

| Persona | Typical form | Roughness |
|---|---|---|
| BIM coordinator | lowercase, slang, deadline clause, class names exact | high |
| Architect | colloquial, Revit words ("семейство", "уровни"), colours/visual symptoms | high |
| Structural / MEP engineer | short, exact class or system names, units | medium |
| Estimator / QS | table-oriented ("BoQ per storey", "ВОР в эксель"), quantities named exactly | medium |
| Facility manager / owner | "for handover", "FM says", asset words (serial number, manufacturer), few IFC terms | medium |
| Developer | precise: class names, Python calls, error line; may paste a snippet | low (but terse) |
| Reviewer from authority | formal, norm names (СП, ГОСТ, IDS, 確認申請) | low |
| Student / beginner | self-label ("новичок", "absolute beginner"), concept or tool-finding questions, over-polite on GitHub | high on vocabulary, low on slang |

---

## 13. Per-language highlights

Each block says how strong the evidence is. "Synthetic" means: written for this KB, not observed.

### 13.1 Russian (ru) - evidence: medium (104 real, 149 synthetic)

- **Form:** no greeting; the title states the software pair or the symptom ("Экспорт из Tekla в Revit", "Не происходит экспорт модели"); one question per thread; replies are terse ("помогло").
- **Slang and transliteration:** ифс/ифц (IFC), ревит, текла, архикад, сапфир, нанокад, навис, солибри, проксики/проксей, склейка (model merge), "зона"; verbs "экспортнуть/импортнуть/затащить/пересести".
- **Vocabulary of the field:** ЦИМ, ТИМ, АГР, ТЭП, ФОП, МССК, КСИ, ВОР, экспертиза, "работа в стол" (work that goes nowhere).
- **Mixed script:** `IfcExportAs`, `RUS_Area`, `UDPS`, `GlobalId` inside Russian sentences; the Revit UI in Russian ("Экспорт в IFC", "общие параметры").
- **Evidence moves:** quote the English error verbatim ("System Error encountered during import"), compare with another viewer (BimSight), blame pressure from `заказчик` or `экспертиза`.
- **Emotion:** fatigue and irony ("коварная вещь", "получается фигня", "ради пустого параметра").
- **Caveats:** dwg.ru pages were fetched with broken encoding, so some Russian paraphrases are reconstructions of the gist. No real posts for estimators, MEP engineers or facility managers; Renga and nanoCAD voices are thin.
- **Synthetic style used in this KB (lowercase, 14 words median):** "глянь файл из Теклы, в Ревите одни оси, геометрия вообще есть?", "в нависе ифц улетел куда-то в сторону, координаты проверь, единицы ок?".

### 13.2 English (en) - evidence: strong (1,796 real, 618 synthetic), but biased to GitHub and forums

- **Registers:** GitHub bug template (Autodesk/revit-ifc: "PR:", "ENH:", "INQ:" title prefixes, about 8% of real titles); forum posts (Autodesk, buildingSMART, OSArch, Dynamo) with greeting and thanks; Q&A fragments.
- **Non-native English is the norm** (Europe, India, Asia, Latin America): "I wants to display an IFC file", "Thankx", "thank you for possibility to ask", run-on sentences, article drops ("Export IFC - wrong position !").
- **Habits:** version strings in the title ("Revit 2024.3 Update - ..."), "Solved:" prefix added by the board, "bug or intended?", "am I doing something wrong?", "is it possible to ...", "any workaround?".
- **Jargon:** proxy, pset, qto, mapping table, CV2.0, RV, DTV, MVD, base point, survey point, federate, GUID churn, dailies (OSArch nightly builds), BBIM.
- **Regional notes:** Australian "G'day all" (OSArch); British "before the issue tonight", "loads of proxies", "pls" (synthetic); US vocabulary (feet, curbs, state DOT) in civil infra; Indian and Middle East posts are short, lowercase, context-light (thin evidence).
- **Not collected:** Reddit, Stack Overflow, Quora, LinkedIn comments. Those would likely be more casual than the GitHub/forum material.

### 13.3 Chinese (zh) - evidence: good for titles (166 real, 132 synthetic)

- **Titles:** a symptom or a bare noun plus a question particle: `ifc导入revit后三维不可见`, `revit导出ifc没有东西`, `IFC是什么意思?`, `revit 2020 ifc guid不生成是为什么?`, `有没有好用、方便的IFC查看工具给推荐一下？`. Endings: 怎么办, 如何解决, 是为什么, 怎么回事, 求推荐, 求教.
- **Casing and spacing:** software in lowercase (`revit`, `tekla`, `rvt`), no space between Chinese and Latin text, half-width commas inside Chinese titles, bracket tags `【BIM】`, `[IFC]`, `[Revit]`.
- **Vocabulary:** 构件 (element), 属性集 (Pset), 映射表 (mapping table), 轻量化 (lightweighting), 项目基点 / 测量点 (project base point / survey point), 原点对原点, 翻模 (rebuild a model from CAD), 二开 (secondary development), 报建 / 报审 / 审图 (permit and review submission), 自检 (self-check), 乱码 (garbled text), 踩坑 (pitfall), 干货 (substance), 保姆级教程 (step-by-step tutorial).
- **Regional split:** mainland 导出 / 导入 vs Taiwan 匯出 / 匯入; Hong Kong 建築信息模擬, 認可人士; Taiwan GitHub proposals are long, structured (問題說明 / 建議修改 / 驗證結果), with mm units and tool names in code font.
- **Caveats:** many CSDN items are auto-generated or keyword-stuffed ("【亲测免费】", "！！！"); do not take that as the voice of a user. Chinese developers writing on GitHub use short, polite English with little context.
- **Typed-to-AI (synthetic):** `revit2019导ifc点了没反应只出个schema文件，咋回事`, `tekla的ifc在viewer里正常，revit里3D视图啥也没有，查下是不是几何有问题`.

### 13.4 Spanish (es) - evidence: thin (33 real, 67 synthetic)

- Short, context-poor: "problemas con los ifc", "no abre", "se pierde parte de la información", "pesa 800mb".
- English-style plural apostrophe ("IFC's"), lowercase "ifc", missing accents ("Exportacion", "Descripcion", "cuantos").
- Voseo and imperative in AI prompts: "Creá cuatro muros de 3 m", vs neutral "Ejecuta la corrida 5 HVAC", "dame los ductos".
- Local words: ambientes (spaces), niveles (storeys), metrados / cómputo (quantities), nativo (native file), plantas, cota (elevation), corrida (takeoff run), MIDE / MEI (Chile).
- Formal wrapper ("Hola", "Que tengan un buen día") when writing to an international English repo.
- ALL CAPS and typos exist in beginner posts (`SOPOTARÁ ARCHIVOS IFC?`).

### 13.5 Portuguese (pt, pt-BR) - evidence: essentially none (1 real, 43 synthetic)

- The only real Portuguese record is a GitHub issue with numbered steps (Bonsai on Ubuntu) and a raw-bytes encoding problem.
- Synthetic style (assumed): informal, lowercase, direct, no greeting; "cara olha o ifc e me fala", "lista ai", "tá tudo cinza, cadê as cores?"
- Vocabulary (assumed, consistent with the glossary): compatibilização (coordination), quantitativo (takeoff), pavimento (storey), pilar, viga, prumada, furos, EIR/BEP/SINAPI.

### 13.6 German (de) - evidence: thin (22 real, 53 synthetic)

- Real German is mostly blog titles ("Revit Typenparameter nach IFC exportieren", "Wand als IfcFooting exportieren"). DACH forum users usually write in English with German parameter names (`ARC_Tragwerk`).
- Vocabulary: Durchbruch / Aussparung / Schlitz (opening, penetration, slot), TGA (building services), LV (bill of quantities), AIA, BAP, Fachmodell, Rohbau, OKFF / OKRD, Geschoss, Stand 12.
- Synthetic casual style: imperative with "mal" or "bitte", umlauts often transliterated (`pruef`, `Waenden`), English terms mixed in (Proxy, Pset, GUID, Mapping): "zeig mir alle Wanddurchbrüche", "die Stützen sind alle als Proxy drin". The umlaut transliteration is an assumption about typing habits.

### 13.7 French (fr) - evidence: none (2 real in English, 43 synthetic)

- Synthetic (assumed): tutoiement toward the AI ("peux-tu", "fais moi la liste"), lowercase, no greeting, English terms (proxy, clash, pset, BCF).
- Vocabulary (assumed, consistent with French BIM practice): maquette (model), synthèse (coordination), DOE / GMAO, SDP, indice B (revision), MOA, CCTP. "Mo" for MB appears in French-speaking writers' English posts.

### 13.8 Japanese (ja) - evidence: medium for blogs (57 real, 47 synthetic)

- **Registers:** Zenn/Qiita: terse, code-first, da/dearu or desu/masu, honest "分からない"; note: first-person, polite, ■ headings, hedged claims.
- **Title genres:** failure stories (`〜できなかった話`), discoveries (`調べてみた`, `作ったよ`), explainer (`ゆるく説明する`), results (`IFCに出したら、半分なかった`).
- **Vocabulary:** 書き出し (export), 読み込み (import), リンク, 属性, 軽量化, 干渉チェック, 確認申請, 図面審査, 入出力基準, 壁芯, 野良データ (stray data).
- **Heavy mixing:** English entity names, katakana jargon (ファセット, バリデーション), acronyms.
- **Typed-to-AI (synthetic):** plain-form imperative or polite-casual: `IFCに出したら半分くらい要素が無い…Revitの元モデルと比べて何が落ちてるか調べて`, `部屋ごとの床面積と壁の面積を拾って、積算用の表にしてほしい`.
- **Caveat:** no real Q&A forum posts; posts with questions are rare, people write notes.

### 13.9 Korean (ko) - evidence: none for casual style (8 real are institutional)

- Institutional text is formal and mixes English (IFC, openBIM, bSI, IDS). 아키캐드 (ArchiCAD) appears in a real announcement title.
- The Korean cell **hypothesises** casual style for AI prompts: banmal-style short requests (`뽑아줘`, `봐줘`, `바꿔줘`), 레빗 for Revit, 프록시 / proxy, 공유 매개변수 (shared parameters), emoticons like `ㅠㅠ`. Use sparingly and mark as unverified.

### 13.10 Arabic (ar) - evidence: none

- One synthetic prompt (Arabic room names show as question marks after export, Levantine "شو المشكلة"). No real post. The multilingual glossary also flags Arabic BIM terminology as the weakest of the ten languages. Keep Arabic prompts short, keep IFC tokens in Latin script, and expect mixed Arabic/English plus encoding complaints (see the encoding topics).

### 13.11 Others

| Language | Evidence | What is known |
|---|---|---|
| **Italian** | 28 real (mostly ACCA Biblus articles and Ingenio) | Question-form titles ("e obbligatoria?"), heavy English mixing (export, class mapping, Pset, viewer, proxy, clash detection), institutional jargon (stazione appaltante, DOCFAP, ACDat, capitolato informativo, oGI/pGI), phrases like "fuori di km" |
| **Dutch** | 21 real (GitHub issues of standards groups) | Terse, informal je/jij; maintainers use Waarom / Nu / Gevraagd; English tool names in Dutch sentences; nulpunt, bouwlaag, aspectmodel, kozijn, peil, stramien; hedge "voor zover ik weet"; "oid" |
| **Norwegian** | 13 real, institutional; synthetic style inferred | Terse bokmål imperatives ("sjekk", "lag"); RIB/RIV/ARK, FDV, BTA/NTA, TEK17, MMI used as everyday words; æøå encoding is a real topic |
| **Turkish, Greek** | 3 synthetic prompts (encoding) | `ğ ü ş` written as `\X2\` codes; Greek space names garbled |
| **Slovak** | 1 real | Short imperatives in an MCP issue: "Oddiaľ pôdorys o 15 percent." |
| **Vietnamese, Czech, Danish** | 1 real each | Anecdotal; Czech parameter names `OBJEM`/`PLOCHA` appear inside English posts |

---

## 14. Checklist: "Does this sound like a real person?"

Tick as many as apply to a generated request. A request that fails more than five is probably an invention.

1. [ ] No greeting, no self-introduction, no "As a BIM coordinator ...".
2. [ ] No "could you please", "I would appreciate", "kindly", "thank you in advance" (unless the persona is a beginner on GitHub).
3. [ ] It is **short** for its register: at most about 25 words if typed to the assistant, unless a log or list is pasted.
4. [ ] It starts with the symptom or the verb, not with background.
5. [ ] It refers to the loaded model as "this model/file/ifc" instead of explaining what is loaded.
6. [ ] There is a **reason or pressure** somewhere ("before the coord meeting", "заказчик требует", "needs to go to the architect today").
7. [ ] At most one or two context items (Revit year, size, viewer comparison); no complete version stack.
8. [ ] Something is missing that a textbook would include (schema version, MVD, exact property set name, units).
9. [ ] One concrete anchor exists: an exact class or pset name, a number with unit, a name pattern ("Колонна_*"), a threshold.
10. [ ] Terminology is slightly loose where a real person's would be (proxy, "export", "family", "mapping", "IFC4").
11. [ ] Local-language sentence keeps technical tokens in Latin script and uses local slang or transliteration where the language has it.
12. [ ] At most one slip (typo, dropped accent, lowercase product name), and not in the key token.
13. [ ] Emotion, if any, is understated (a "??", "again", a deadline), not theatrical ("URGENT!!!", "my career depends on it").
14. [ ] No bullet list, no bold headings, no "Task / Context / Constraints" structure.
15. [ ] No request for a "comprehensive overview", "detailed analysis" or "complete report".
16. [ ] Lists inside the request are uneven (two criteria, not three equal ones; one threshold, not a matrix).
17. [ ] The output format, if stated, is practical and short ("csv ok", "list with guids", "table for excel").
18. [ ] The task is something a person with this role would really do this week (not an exam question, not "explain IFC").
19. [ ] It contains an honest-answer clause or a "don't touch X" clause at least some of the time ("if there is no Qto, say so", "не удаляй").
20. [ ] The phrasing differs from the previous five requests in the batch (different opener, length, mood).
21. [ ] Numbers look measured, not round ("212 doors", "0.5 m2", "480 MB"), unless the person is rounding on purpose ("about 400 megs").
22. [ ] It would still be answerable and verifiable by a tester who can open the model.

---

## 15. Annotated examples (real, paraphrased, linked)

Each entry gives the source (canonical = URL), the original-language text (title verbatim if 20 words or fewer; otherwise the dataset's paraphrase), an English gloss, and what makes it human. Persona and tone are the dataset's labels. The examples are **real records**, not synthetic. A few dwg.ru paraphrases are reconstructions of the gist because the pages were fetched with broken encoding.

### 15.1 English (EN-1 to EN-13)

| # | Source | Text | What makes it human |
|---|---|---|---|
| EN-1 | [Autodesk forum, 2018](https://forums.autodesk.com/t5/revit-structure-forum/ifcexportas-parameter-doesn-t-work/td-p/8219179) (structural engineer, frustrated) | "IfcExportAs Parameter doesn't work" | The title is a UI label plus a verdict. Body is one symptom: slab edges still come out as `IfcBuildingElementProxy`. No version. |
| EN-2 | [Autodesk forum, 2024](https://forums.autodesk.com/t5/revit-architecture-forum/revit-2024-3-update-revit-crashes-every-time-i-export-ifc/td-p/13030432) (BIM manager, urgent) | "Revit 2024.3 Update - Revit crashes every time I export IFC!!!" | Version in the title, "every time", triple exclamation. Urgency without a deadline. |
| EN-3 | [Autodesk forum, 2026](https://forums.autodesk.com/t5/revit-architecture-forum/ifc-export-in-2027-mapping-parameters-severely-lacking/td-p/14229702) (BIM manager, frustrated) | "Ifc export in 2027 - mapping parameters severely lacking" | A verdict in the title; lowercase "Ifc"; names the new GUI and says what is missing. |
| EN-4 | [revit-ifc #223](https://github.com/Autodesk/revit-ifc/issues/223) (coordinator, confused) | "IFC Import - Link Vs Open": why does Open give in-place families without IFC data while Link gives different geometry and duplicates assemblies? Asks for "some official feedback" | Compares two UI commands, uses the Revit menu words as nouns, asks the vendor for a ruling. |
| EN-5 | [buildingSMART forum, 2021](https://forums.buildingsmart.org/t/3953) (estimator, polite) | "Help regarding extracting/ importing data from IFC to Estimation software": a non-programmer asks, in "layman terms", how to read IFC data including Revit keynotes | Self-declared layman, long introduction, then a vague "how do I read it". |
| EN-6 | [buildingSMART forum, 2022](https://forums.buildingsmart.org/t/4199) (coordinator, confused) | "What is the relationship between IDS and IDM or MVD?" | One sentence, three acronyms, "I am confused" tone. |
| EN-7 | [buildingSMART forum, 2023](https://forums.buildingsmart.org/t/4802) (beginner, curious) | "IFC Schema Identifier": file properties show nothing; how do I know if this is IFC2x3 or IFC4? Found out only by opening it in a viewer | A basic question the experts take for granted; the workaround the asker found is part of the post. |
| EN-8 | [OSArch, 2026](https://community.osarch.org/discussion/3754/opening-cuts-skipped-in-bonsai-studio-0-9) (coordinator, confused) | "Opening Cuts Skipped in Bonsai Studio 0.9": Revit-exported IFCs show the message, Apply Openings fixes it, "Bug or intended?" | Reports the fix he found, what he tried (Void Limit 30 to 5000), asks "bug or intended". |
| EN-9 | [OSArch, 2026](https://community.osarch.org/discussion/3765/roadmap-for-revit-migrator-to-bonsai-bim-absolute-beginner) (beginner, polite) | "Roadmap for Revit migrator to Bonsai BIM - absolute beginner" | States background first, warm thanks for free tools, asks for a roadmap while modelling a small timber house. |
| EN-10 | [IfcOpenShell #585](https://github.com/IfcOpenShell/IfcOpenShell/issues/585) (beginner, confused) | "Convert IFC file into svg floor plans": dragged the IFC onto the converter exe and got only an `.obj`; how to get SVG? "thanks in advance" | GUI mindset, no idea about command-line flags, "30 floor model" detail, thanks as closer. |
| EN-11 | [mcp-servers-for-revit #1](https://github.com/mcp-servers-for-revit/mcp-servers-for-revit/issues/1) (architect, frustrated) | "Connection issue": Claude answers it cannot connect to Revit and will create the 10-meter wall once connected; port 8080 opened, no luck | The user quotes the assistant's own reply, lists what was checked, gives no versions. |
| EN-12 | [revit-mcp #28](https://github.com/mcp-servers-for-revit/revit-mcp/issues/28) (MEP engineer, frustrated) | "Keep getting 'Method XXX not found' errors despite MCP server and Revit plugin working": the plain prompt "list all pipes in the revit model" ends in "Method not found" | The real prompt (lowercase, one line) pasted inside a bug report; shows how users actually phrase the first request. |
| EN-13 | [IfcOpenShell #3124](https://github.com/IfcOpenShell/IfcOpenShell/issues/3124) (developer, neutral) | "how can i export dwg to ifc4 by ifcopenshell": "my language is C++, is there an example for CAD to ifc4" | Lowercase, no articles, "export" used for conversion, a language mentioned as context. |

### 15.2 English, more fragments (EN-14 to EN-17)

| # | Source | Text | What makes it human |
|---|---|---|---|
| EN-14 | [Dynamo forum, 2025](https://forum.dynamobim.com/t/help-with-automated-quality-check-script-getting-empty-list-and-blank-excel/112252) (coordinator, frustrated) | "Help with Automated Quality Check Script - Getting Empty List and Blank Excel": ChatGPT and others gave a script that returns an empty list and an Excel with headers only | Mentions failed AI attempts as context; title lists the symptom twice. |
| EN-15 | [revit-ifc #529](https://github.com/Autodesk/revit-ifc/issues/529) (coordinator, frustrated) | "In Revit 2023 IfcSpace Qto_SpaceBaesQuantities NetFloorArea and others are not getting exported" | Typo inside the property-set name ("Baes"); "+1" comments from 2022 users. |
| EN-16 | [COBie-plugins #2](https://github.com/opensourceBIM/COBie-plugins/issues/2) (developer, urgent, 2014) | "Urgent, Can we use Cobiee plugin with bimserver1.2 with JAVA 1.6 ?" | "Urgent" as the first word, misspelled "Cobiee", space before question mark. |
| EN-17 | [Autodesk Civil 3D forum, 2023](https://forums.autodesk.com/t5/civil-3d-forum/export-ifc-wrong-position/td-p/11945739) (civil engineer, frustrated) | "Export IFC - wrong position !" | The whole question is the title; space before "!"; no software version. |

### 15.3 Russian (RU-1 to RU-8)

| # | Source | Text | What makes it human |
|---|---|---|---|
| RU-1 | [dwg.ru, 2018](https://forum.dwg.ru/showthread.php?t=146029) (structural engineer, confused) | «заказчик требует выдавать IFC и грузить в Ревит, стандартный экспорт с настройками по умолчанию даёт в Ревите только оси» | Customer pressure as the first clause; "только оси" is a concrete visual symptom. Gloss: the customer demands IFC; default export shows only grids in Revit. |
| RU-2 | [dwg.ru, 2021](https://forum.dwg.ru/showthread.php?t=160240) (coordinator, confused) | «САПФИР-3D 2020 R2. Как правильно экспортировать модель в IFC?» + IFC из Сапфира в автокад не импортируется, системная ошибка, в BimSight открывается нормально | Software pair in the title, English error text verbatim inside Russian, cross-check in another viewer. |
| RU-3 | [dwg.ru, 2019](https://forum.dwg.ru/showthread.php?t=154396) (coordinator, confused) | «Как корректно открыть IFC»: после экспорта из Ревита часть элементов и параметров потерялась, как проверить, где проблема, в экспорте или в просмотрщике | Declares "новичок в моделировании". Gloss: newcomer, parts lost after Revit export; is the fault in the export or the viewer? |
| RU-4 | [same thread](https://forum.dwg.ru/showthread.php?t=154396) (architect, frustrated) | при экспорте из Архикада в IFC и вставке в Ревит стёкла жёлтые и толщиной в метры, часть перегородок пропала | Emotive description ("получается фигня" is the gist), visual symptoms in plain words. |
| RU-5 | [dwg.ru, 2013](https://forum.dwg.ru/showthread.php?t=96356) (architect, neutral) | «Как пересести из ifc в dwg ?» | A colloquial verb ("пересести" for convert), space before "?", one line. |
| RU-6 | [dwg.ru, 2019](https://forum.dwg.ru/showthread.php?t=153428) (architect, urgent) | «Экспертиза проекта, созданного в Revit»: нужно ли с 01.07.2019 переходить на ТИМ, можно ли работать в 2D и сдавать PDF | Date anxiety, links a government decree, not a tool problem but a rules question. |
| RU-7 | [Habr, 2026](https://habr.com/ru/articles/1089018/) (coordinator, confused) | «Два часа выгрузки ради пустого параметра»: Навис показывает 1500 коллизий, сервис 200, почему разное число | Numbers as the argument; the cause (grouping by Revit category vs IFC class) is only revealed at the end. |
| RU-8 | [dwg.ru, 2016](https://forum.dwg.ru/showthread.php?t=130296&page=2) (architect, neutral) | «Как редактировать семейство в модели!?» | Revit vocabulary ("семейство") applied to an imported IFC; "!?" punctuation. |

### 15.4 Chinese (ZH-1 to ZH-8)

| # | Source | Text | What makes it human |
|---|---|---|---|
| ZH-1 | [Baidu Zhidao, 2025](https://zhidao.baidu.com/question/341569640619976845.html) (architect, frustrated) | 「ifc导入revit后三维不可见」 | No spaces, lowercase software, symptom only. Gloss: after importing IFC into Revit, nothing is visible in 3D. |
| ZH-2 | [Zhihu, 2022](https://www.zhihu.com/question/527323998) (beginner) | 「IFC是什么意思?」 | The "XX是什么" pattern; asks whether it is a file format or a standard. |
| ZH-3 | [Zhihu, 2023](https://www.zhihu.com/question/625548241) (coordinator, confused) | 「revit 2020 ifc guid不生成是为什么?」 | Lowercase "revit", spaces between Latin tokens only, "是为什么" ending. Gloss: why are GUIDs not generated in the IFC from Revit 2020? |
| ZH-4 | [Zhihu, 2023](https://www.zhihu.com/question/583830829) (coordinator, curious) | 「有没有好用、方便的IFC查看工具给推荐一下？」 | Classic "recommend one" request; the question is tool-finding, not troubleshooting. |
| ZH-5 | [CSDN blog, 2024](https://blog.csdn.net/d001014/article/details/140438872) (coordinator, frustrated) | 「revit导出ifc（1）」 body: revit导出ifc没有东西 | Series-number title, body is a bare symptom: "nothing in the exported IFC". |
| ZH-6 | [revit-mcp-plugin #11](https://github.com/mcp-servers-for-revit/revit-mcp-plugin/issues/11) (developer, curious) | 「世界发展真快 马上二开要失业了」 | Slang "二开" (secondary development), two-line exclamatory post, no question. |
| ZH-7 | [REVIT_MCP_study #144](https://github.com/shuotao/REVIT_MCP_study/issues/144) (coordinator, neutral, Traditional Chinese) | 「[提案] 強化 create_wall 的樓層與牆型選擇，避免任意使用第一個樓層」 | Structured proposal, tool names in code font, numbered problem list (no level parameter, no wall type). |
| ZH-8 | [CSDN Ask, 2025](https://ask.csdn.net/questions/8816624) (coordinator, confused) | 「Revit在2000坐标下如何精确移动项目基点至0,0,0？」 | Uses the local coordinate-system jargon ("2000坐标", CGCS2000) without saying what CRS or unit. |

### 15.5 Spanish, Portuguese, German, French, Japanese, others (X-1 to X-9)

| # | Source | Text | What makes it human |
|---|---|---|---|
| ES-1 | [IngeTrazo #1033](https://github.com/ingelibre/ingetrazo/issues/1033) (beginner, curious) | «SOPOTARÁ ARCHIVOS IFC?» + quisiera saber si será posible importar archivos IFC? | All caps, typo "SOPOTARÁ", one-line need, no version. Gloss: will the app support IFC files? |
| ES-2 | [Autodesk forum ES, 2021](https://forums.autodesk.com/t5/revit-architecture-forum/problemas-con-ifc-s/td-p/10189111) (architect, confused) | «Problemas con IFC's»: al abrirlo y guardarlo en otro formato se pierden las coordenadas que traía | English plural apostrophe, vague title, the one concrete detail is lost coordinates. |
| ES-3 | [IfcOpenShell #8131](https://github.com/IfcOpenShell/IfcOpenShell/issues/8131) (other, polite) | «Pérdida de la geometría de los objetos»: al abrir un archivo IFC (2x3) se pierde parte de la información geométrica; adjunto captura en Bonsai y Bonsai Viewer | Formal greeting and farewell, offers the file, Spanish text inside an English-language repo. |
| ES-4 | [archicad-mcp README](https://github.com/joacos/archicad-mcp) (architect) | «Creá cuatro muros de 3 m de alto formando un rectángulo de 5 × 4 m» | Rioplatense voseo (Creá), exact metric numbers, typed to an AI. |
| PT-1 | [IfcOpenShell #7305](https://github.com/IfcOpenShell/IfcOpenShell/issues/7305) (beginner, frustrated) | «Falha de importação de arquivo IFC com Bonsai» | Portuguese title, numbered steps, an IFC from ArchiStation on Ubuntu 24.04, raw-byte encoding problem; the only real Portuguese record. |
| DE-1 | [KIT-IAI #13](https://github.com/KIT-IAI/SDM_KITModelViewer/issues/13) (academic, neutral) | Report in English quoting the German error text «ungültige Daten auf Stammebene. Zeile 9, Position 1» | UI-language error pasted untranslated into an English report. |
| JA-1 | [note, 2026](https://note.com/toshio_nakamura/n/nc8db42ce3191) (architect, frustrated) | 「IFCに出したら、半分なかった。3Dの箱と、壁ツールの壁は別物です」 | Title is the outcome ("half was missing"), then an explanation: plain solids, layers not tied to storeys, hidden elements. Gloss: after exporting to IFC half the model was gone. |
| JA-2 | [Zenn, 2024](https://zenn.dev/miyamiyaumya/articles/19a4247133dde6) (coordinator) | 「IfcOpenShellのIfcCSVだとAttributeしか書き出せないので、PropertySetとMaterialも一緒にExcelへ出したい」 | A tool limitation in one clause, English entity names inline, the goal at the end. Gloss: IfcCSV only exports attributes; I want property sets and materials in Excel too. |
| JA-3 | [Zenn scrap, 2026](https://zenn.dev/kiyuka/scraps/e07bf799384b52) (developer, frustrated) | 「IFC Validation Service をローカルで動かす」: 公式手順どおり make start したら localhost がエラー、backend と worker が再起動を繰り返す | Working-notes tone: "followed the official steps and ..." then the error behaviour. |

### 15.6 Dutch, Slovak, Italian (X-10 to X-12)

| # | Source | Text | What makes it human |
|---|---|---|---|
| NL-1 | [OpenAEC validator #19](https://github.com/OpenAEC-Foundation/OpenAEC-BIM-validator/issues/19) (estimator) | «hebben alle 212 deuren een FireRating?» / «m2 binnenwand per NL-SfB-code» | Concrete example questions in quotes with a real-looking count (212), classification code inline. |
| NL-2 | [NLCS #238](https://github.com/nl-digigo/NLCS/issues/238) (BIM manager, polite) | «staat er op jullie roadmap de ontwikkeling van een Revit template oid?» | Informal "jullie", "oid" ("or the like"), relayed user question. |
| SK-1 | [AIMviewer #65](https://github.com/Menezeris/AIMviewer/issues/65) (BIM manager) | «Oddiaľ pôdorys o 15 percent.» | The shortest relative command to an AI viewer; imperative, a number, no context. |

(That is 17 + 8 + 8 + 12 = **45 annotated real examples**; the IT row from `it-italy-r005`, "i modelli IFC non si sovrappongono, uno e fuori di km", is deliberately left out of the list because it is a vendor article's framing, not a person's question.)

---

## 16. Summary table for a generator (recommended defaults, derived from the data above)

| Knob | Default | Range |
|---|---|---|
| Words per request (typed to AI) | 14 | 6 to 25 (60 with a pasted detail) |
| Greeting / thanks | none | rare; only polite beginners |
| Context items | 1 | 0 to 2 (3 only for developers) |
| Version numbers | none | Revit year in about one in five requests |
| Schema stated | usually no | real posts state it about half of the time; short prompts rarely |
| Because-clause (deadline, person waiting) | present in 1 of 3 | 0 to 1 |
| Slip (typo, accent, case) | in 1 of 4 | max 1 per prompt |
| Loose term (proxy, export, mapping, family) | in 1 of 3 | when the persona is non-expert |
| Output format | in 1 of 3 | csv, table, list with guids |
| Honest-answer clause | in 1 of 8 | "if there's no X, say so" |
| Two-part request | 1 of 5 | |
| Follow-up | 1 of 10 | mark in the test case |

See [anti_patterns_llm_questions.md](anti_patterns_llm_questions.md) for before/after rewrites and the rules that turn a textbook prompt into a human one.
