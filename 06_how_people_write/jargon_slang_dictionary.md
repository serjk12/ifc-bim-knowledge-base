# Jargon and slang dictionary (by language)

**Audience:** a tester (or an LLM acting for one) with no BIM background who must write requests that sound like a real colleague typed them, and must judge whether an IFC / Revit MCP server understood them.
**Companions:** [name_variants_and_misspellings.md](name_variants_and_misspellings.md) (how product and entity names are spelled and misspelled), [style_guide.md](style_guide.md) (register, length, tone), [../08_glossary/glossary_multilingual.md](../08_glossary/glossary_multilingual.md) (standard terms in 10 languages), [../08_glossary/abbreviations.md](../08_glossary/abbreviations.md).
**Data basis:** the 3,525 records in `research_raw/wave1/` (2,256 real, 1,269 synthetic) and the "How people write" sections of the 77 cell reports. No `wave2` data existed when this file was written.

---

## In plain words

People who work with IFC (an open file format for building models) and Revit (Autodesk's design program) do not use textbook words. They shorten, borrow English words into their own language, write product names in their own alphabet, and use one word for several things. This file lists those words, what they literally say, what the person means, what the standard term is, a short example, and where it was seen.

If you only read one thing: **the same few ideas are named differently everywhere.** "Proxy", "pset", "family", "level", "link", "export" appear in almost every language, but each hides a trap (see [Section 12](#12-false-friends-and-ambiguity-traps)).

## How to read the tables

Every row carries an **evidence tag** in the last column. Do not treat all rows as equally real.

| Tag | Meaning | How much to trust it |
|---|---|---|
| **R** | The word appears in a **real** record (a forum post, issue, blog, vendor page). The record id is linked to its `source_url`. | High: someone really wrote it. The record text is a paraphrase (titles up to 20 words are verbatim), so a typo may have been cleaned. |
| **N** | The word is named in the "How people write" note of a cell report as seen in real sources, but no single record carries it. The report file is linked. | Medium: observed by the researcher, not individually traceable. |
| **S** | The word appears **only in synthetic prompts** (written by a research agent to imitate chat style). The synthetic id is given. | Low to medium: plausible, not proven as real chat usage. Good for generating tests, not for claiming "people say this". |
| **K** | Standard or reference terminology from the glossary / reference docs, or general domain knowledge, not observed in the data. | Medium for official words, low for slang. Verify before hard-coding in a test expectation. |

**Example fragments** are at most 12 words. For R rows they are shortened from the record's paraphrase or verbatim title; for S rows they are cut from the synthetic prompt. They are never presented as quotes of a named person. IFC class names (IfcWall) are never translated: they stay in Latin script in every language.

## Coverage: how much evidence each language has

| Language | Real records | Synthetic | Reliability of slang in this file |
|---|---|---|---|
| English (en) | 1,796 | 618 | Strong. Includes tracker, forum and blog voices. Very little real "chat to an AI" voice. |
| Chinese (zh) | 166 | 132 | Strong for developer blogs, Zhihu, permit-system vocabulary. Traditional-Chinese (Taiwan, Hong Kong) is thinner. |
| Russian (ru) | 104 | 149 | Good for forum.dwg.ru and Habr vocabulary. Spoken slang ("ифс", "проксики") is mostly **N or S**: the real titles are mostly Latin or formal. |
| Japanese (ja) | 57 | 47 | Good (Zenn, Qiita, note). Mostly blog voice, not chat. |
| Spanish (es) | 33 | 67 | Medium. Real posts are few; LatAm vs Spain differences come mostly from synthetic prompts and institutional pages. |
| Italian (it) | 28 | 42 | Medium, but real records are vendor articles (biblus.acca.it), not forum posts. |
| German (de) | 22 | 53 | Thin for native slang: most real "German" posts are written in English. Native slang is **S or N**. |
| Dutch (nl) | 21 | 14 | Medium for official / GitHub spec vocabulary, no casual chat. |
| Norwegian (no) | 13 | 17 | Thin, institutional; low confidence. |
| Korean (ko) | 8 | 40 | Thin. Almost everything casual is **S**. |
| French (fr) | 2 | 43 | Almost purely synthetic. |
| Portuguese (pt, pt-BR) | 1 | 43 | Purely synthetic. The one real record is English-style GitHub text by a Portuguese speaker. |
| Turkish, Arabic, Greek | 1 / 0 / 0 | 2 / 1 / 1 | Only synthetic encoding prompts. |
| Slovak, Vietnamese, Czech, Danish | 1 each | 0 | One README or issue each. |
| Polish | 0 | 0 | **No data at all.** Section 10 gives clearly marked background terms only. |

---

## 1. The shared "IFC-world" shorthand (works in almost every language)

These terms are kept in Latin script inside local-language sentences. A test request in any language can use them unchanged.

| Shorthand | Literal | Meaning in plain words | Standard term | Example fragment | Evidence and source |
|---|---|---|---|---|---|
| proxy / proxies | "a stand-in" | An element that came out of the export as a generic "unknown thing" instead of a wall, door, column. Usually a sign the export was mapped badly. | `IfcBuildingElementProxy` | "Slab edges still export as proxy" | N [en-autodesk-revit-export.md](../research_raw/wave1/en/en-autodesk-revit-export.md); R [de-dach-r019 area](../research_raw/wave1/de/de-dach.md) |
| pset / psets | "p-set" | A named bundle of properties on an element (FireRating, IsExternal). | Property set, `IfcPropertySet` | "where are my ePset values?" | R [en-coord-r040](https://community.osarch.org/discussion/comment/29556/) |
| ePset | "extra pset" (OSArch speech) | A custom property set added by the user. | Custom pset | same | R [en-coord-r040](https://community.osarch.org/discussion/comment/29556/) |
| UDPS / UDPset | "user-defined pset" | Revit's text file that tells the exporter which parameters become properties. | User-defined property set file | "UDPS" in a Habr post | R [ru-autodesk-telegram-r011](https://habr.com/ru/articles/1098340/) |
| Qto / QTO | "quantity set" | Measured values (length, area, volume) stored in the file. Not the same as a quantity take-off done by a person. | `IfcElementQuantity`, `Qto_*BaseQuantities` | "net wall area per storey, csv pls" | S [en-aimcp-s004](../research_raw/wave1/ai/ai-mcp-usage.jsonl) |
| GUID / GlobalId / IfcGUID | "global id" | The 22-character id of an element that should stay the same between exports. | `IfcRoot.GlobalId` | "Revit regenerates GlobalIds for some categories" | N [t-guid-versioning.md](../research_raw/wave1/topics/t-guid-versioning.md) |
| GUID churn | "id turnover" | The ids change on every re-export, so version comparison breaks. | unstable GlobalId | "GUID churn" | N [p-bim-coordinator.md](../research_raw/wave1/roles/p-bim-coordinator.md) |
| MVD | "model view" | The agreed subset of IFC for one exchange purpose. | Model View Definition | "MVD" | N [en-buildingsmart-forums.md](../research_raw/wave1/en/en-buildingsmart-forums.md) |
| RV / CV2 / CV2.0 / DTV / RVArch | letters | RV = Reference View, CV2.0 = Coordination View 2.0 (IFC2x3), DTV = Design Transfer View. People also write "IFC4 RV". | Named MVDs | "22.4.2 ok, 23.2.3 not ok" next to "CV2" | N [en-gh-revit-ifc.md](../research_raw/wave1/en/en-gh-revit-ifc.md), [t-proxy-mapping.md](../research_raw/wave1/topics/t-proxy-mapping.md) |
| 2x3 / 4x3 / ADD2 / TC1 | schema nicknames | IFC2x3, IFC4.3, "Addendum 2", "Technical Corrigendum 1". | IFC schema editions | "IFC 4x3 add2" | R [en-gh-thatopen-r020](https://github.com/ThatOpen/engine_web-ifc/issues/1171) |
| BCF | "b-c-f" | A small file for passing issues (clashes, comments) between programs. | BIM Collaboration Format | "Draw Revision cloud in shapshot" (BCF repo) | R [en-clash-r027](https://github.com/buildingSMART/BCF-XML/issues/385) |
| IDS | "ids" | A machine-readable rulebook ("every wall needs FireRating") to check a model against. | Information Delivery Specification | "bug or misunderstanding of IDS?" | N [en-osarch.md](../research_raw/wave1/en/en-osarch.md) |
| bSDD | "bee-ess-dee-dee" | buildingSMART's online dictionary of classifications and properties. | buildingSMART Data Dictionary | "No bSDD Props Found" | N [t-classification-bsdd.md](../research_raw/wave1/topics/t-classification-bsdd.md) |
| COBie | "cobie" | Spreadsheet-style handover data for facility management. | Construction Operations Building information exchange | "systems tab empty" | R [en-gh-ifcopenshell-r028](https://github.com/IfcOpenShell/IfcOpenShell/issues/6068) |
| EIR / BEP / AIA / BAP / LOIN / LOD | process words | EIR = client's information requirements, BEP = project's BIM execution plan (German: AIA, BAP). LOD/LOIN = how much detail/information. | ISO 19650 documents | "EIR says all doors need FireRating" | S [en-uk-anz-india-s002](../research_raw/wave1/en/en-uk-anz-india.jsonl); K [abbreviations](../08_glossary/abbreviations.md) |
| clash | "collision" | Two elements occupying the same space; also used as a verb ("clash the models"). | Clash detection | "0 clashes found even with a deliberate clash" | N [t-clash-bcf.md](../research_raw/wave1/topics/t-clash-bcf.md) |
| federate / federated model | "make a federation" | Combine the discipline models into one coordination view. | Model federation | "federate" | N [p-bim-coordinator.md](../research_raw/wave1/roles/p-bim-coordinator.md) |
| viewer names as verdicts | "BIMvision shows it fine" | People prove a bug by naming a program that opens the file correctly. | cross-viewer check | "same file fine in BIMvision" | N [t-geometry.md](../research_raw/wave1/topics/t-geometry.md) |

---

## 2. English (EN)

English real data is mostly GitHub issues, forums and blogs; "typed to an AI" English is mostly **S**.

| Slang / jargon | Literal | Meaning | Standard term | Example fragment | Evidence and source |
|---|---|---|---|---|---|
| proxies | plural of proxy | Many elements exported as generic. Also "going proxy", "came out as proxy". | `IfcBuildingElementProxy` | "half my walls came out as proxy??" | S [en-allplan-vw-bentley-s001](../research_raw/wave1/en/en-allplan-vw-bentley.jsonl); N [en-civil-infra.md](../research_raw/wave1/en/en-civil-infra.md) ("painful BuildingElementProxy") |
| dumb solids / dumb objects | "unintelligent shapes" | Geometry with no wall/door behaviour or parameters after import. | DirectShape (Revit), or an element with only a shape | "windows/walls come as plain dumb objects" | R [en-blogs-linkedin-r004](https://bim-me-up.com/die-wunderwaffe-ifc/); S [en-allplan-vw-bentley-s004](../research_raw/wave1/en/en-allplan-vw-bentley.jsonl) |
| ghost mullions | invisible frame bars | Curtain-wall mullions that appear in the file but not as expected. | `IfcMember` in `IfcCurtainWall` | "Ghost mullions in IFC export" | R [en-autodesk-revit-export-r023](https://forums.autodesk.com/t5/revit-architecture-forum/quot-ghost-quot-mullions-in-ifc-export/td-p/13056918) |
| zombie parameters | dead params | Leftover unused Revit parameters. | unused project/shared parameters | "Deleting zombie Parameters" | R [en-revit-auto-r019](https://forum.dynamobim.com/t/deleting-zombie-parameters/112603) |
| mapping table / export setup | table / saved settings | The Revit text file or setup that decides which category becomes which IFC class. | IFC mapping table, export setup | "does not respect the mapping" | N [en-dynamo-pyrevit.md](../research_raw/wave1/en/en-dynamo-pyrevit.md) |
| IfcExportAs | "export as" | The Revit parameter that overrides the IFC class of one family or element. | `IfcExportAs` / "Export to IFC As" | "IfcExportAs Parameter doesn't work" | R [en-autodesk-revit-export (title)](../research_raw/wave1/en/en-autodesk-revit-export.md) |
| Link IFC vs Open IFC | two import buttons | Link keeps the IFC as a reference; Open converts it toward native Revit elements. | link vs open | "IFC Import - Link Vs Open" | R [en-autodesk-revit-import-r003](https://github.com/Autodesk/revit-ifc/issues/223) |
| ifc.rvt | cache file | The converted file Revit creates beside a linked IFC. | `.ifc.RVT` | "ifc.rvt" | N [en-autodesk-revit-import.md](../research_raw/wave1/en/en-autodesk-revit-import.md) |
| PR: / ENH: / INQ: | title prefixes | Problem report, enhancement, inquiry labels used on Autodesk's revit-ifc tracker. | issue labels | "PR: Link IFC fail" | R [en-autodesk-revit-import-r002](https://github.com/Autodesk/revit-ifc/issues/951) |
| base point / PBP / survey point / shared coordinates | places on the map | Revit's reference points; the usual cause of "model is miles away". | Project Base Point, Survey Point, `IfcMapConversion` | "6 objects close to the zero point" | N [en-autodesk-revit-import.md](../research_raw/wave1/en/en-autodesk-revit-import.md) |
| false origin | fake zero | The shifted local origin used so numbers stay small in a far-away site. | `IfcMapConversion` offset | "false origin" | N [en-osarch.md](../research_raw/wave1/en/en-osarch.md) |
| Bonsai / BlenderBIM / BBIM | tree / old name / nickname | The open-source IFC add-on for Blender. BlenderBIM was renamed Bonsai; "BBIM" is the short form. | Bonsai | "BBIM - Ifc 4x3 class and predefined type" | R [en-us-canada-infra-r005](https://community.osarch.org/discussion/2266/bbim-ifc-4x3-class-and-predefined-type-quick-guide-for-beginners) |
| dailies | nightly builds | Daily test versions of Bonsai. | nightly builds | "dailies" | N [en-osarch.md](../research_raw/wave1/en/en-osarch.md) |
| frag / fragments | "frag" | That Open Company's compact model format. | fragments file | "frag" | N [en-gh-thatopen.md](../research_raw/wave1/en/en-gh-thatopen.md) |
| express ID | "express id" | The integer line number (#123) inside one IFC file; changes between files, unlike GlobalId. | STEP instance id | "express ID" | N [en-gh-thatopen.md](../research_raw/wave1/en/en-gh-thatopen.md); R [zh-csdn-dev-r002](https://juejin.cn/post/7691297274821705728) (丢 expressID) |
| navis | nickname | Navisworks. Also "append" (add a file to the open one). | Navisworks | "arch ifc and struct ifc dont line up when appended" | S [en-navis-acc-s002](../research_raw/wave1/en/en-navis-acc.jsonl) |
| ACC / BIM360 | product names | Autodesk Construction Cloud / its older name BIM 360. | cloud CDE | "before I push to ACC" | S [en-navis-acc-s004](../research_raw/wave1/en/en-navis-acc.jsonl); R [en-autodesk-revit-import-r027 (BIM360)](../research_raw/wave1/en/en-autodesk-revit-import.md) |
| CX / IFC+SG / IFC-SG | Singapore submission | CORENET X, the Singapore e-submission system, and its IFC profile (spelled with + or -). | IFC+SG | "cx submission tomorrow" | S [en-sg-corenetx-s001](../research_raw/wave1/en/en-sg-corenetx.jsonl); N [en-sg-corenetx.md](../research_raw/wave1/en/en-sg-corenetx.md) |
| issue (UK) | "an issue" | A formal information release ("before the issue tonight"), not a bug. | information delivery | "before the issue tonight" | S [en-uk-anz-india-s002](../research_raw/wave1/en/en-uk-anz-india.jsonl) |
| Uniclass Ss / Pr | codes | UK classification: Ss = systems, Pr = products. | Uniclass 2015 | "Uniclass Ss for systems and Pr for products" | S [en-uk-anz-india-s001](../research_raw/wave1/en/en-uk-anz-india.jsonl) |
| MGA zone / state plane / SVY21 / SIRGAS | coordinate systems | National coordinate reference systems (Australia, US, Singapore, Brazil). | CRS / EPSG code | "georeferenced to MGA zone 56?" | S [en-uk-anz-india-s009](../research_raw/wave1/en/en-uk-anz-india.jsonl); N [t-coordinates.md](../research_raw/wave1/topics/t-coordinates.md) (MGA) |
| BoQ / takeoff / take offs / SoR / 5D | cost words | Bill of quantities, quantity take-off ("take offs" used as plural noun), schedule of rates, cost-linked model. | BoQ, QTO | "Problems with Quantity take offs." | R [en-qto (title)](../research_raw/wave1/topics/t-qto-cost.md); N same file |
| alignment / chainage / station / cant / superelevation | civil words | Road or rail centre line and its measurements. "Allignment" is a frequent misspelling. | `IfcAlignment` | "station 15+00 landed 1500 ft" | N [en-civil-infra.md](../research_raw/wave1/en/en-civil-infra.md), [t-infra-ifc43.md](../research_raw/wave1/topics/t-infra-ifc43.md) |
| kerbs / curbs; colour / color | UK vs US | Both spellings appear, sometimes in one title. | spelling variants | "colour/ color wrongly exported" | R [en-mcl-r002](https://github.com/Autodesk/revit-ifc/issues/92) |
| G'day all / Hi all / Hello IFC gurus | openers | Greeting style marks the community (Australian OSArch, general forums). | none | "Hello Ifc gurus" | R [en-mep-r004](https://github.com/Autodesk/revit-ifc/issues/579) |
| pls / u / w/ / n / asap | text speak | Used when typing to an AI or colleagues. | none | "can u list what ifc class each wall got" | S [en-allplan-vw-bentley-s001](../research_raw/wave1/en/en-allplan-vw-bentley.jsonl) |
| bug or intended? / by design? | hedged complaint | The user is not sure the behaviour is wrong. | none | "bug or misunderstanding of IDS?" | N [en-osarch.md](../research_raw/wave1/en/en-osarch.md), [t-psets-params.md](../research_raw/wave1/topics/t-psets-params.md) |
| "export" for any conversion | "export" | People say "export dwg to ifc4" for converting, importing or saving as. | convert | "how can i export dwg to ifc4 by ifcopenshell" | R [en-viewconv-r004](https://github.com/IfcOpenShell/IfcOpenShell/issues/3124) |
| native (file) | "original" | The authoring file (.rvt, .pln), as opposed to IFC. | native format | "can i actually edit this ifc in revit or is it just a reference?" | S [en-beginner-qa-s008](../research_raw/wave1/en/en-beginner-qa.jsonl) |
| levels / storeys / floors | three words | "Levels" is Revit speech, "storeys" is IFC speech, "floors" is beginner speech. | `IfcBuildingStorey` | "how many levels does this have and at what heights" | S [en-beginner-qa-s002](../research_raw/wave1/en/en-beginner-qa.jsonl) |
| 1000x too big / floating / miles away | complaints | Unit error or far-from-origin geometry. | units / coordinates | "navis shows my ifc 1000x too big" | S [en-navis-acc-s008](../research_raw/wave1/en/en-navis-acc.jsonl) |

### Developer voice (EN)

| Slang / jargon | Meaning | Example fragment | Evidence and source |
|---|---|---|---|
| repro / regression | steps to reproduce / "worked in version N, broken in N+1" | "22.4.2 ok, 23.2.3 not ok" | N [en-gh-revit-ifc.md](../research_raw/wave1/en/en-gh-revit-ifc.md) |
| StreamMeshes / GetFlatMesh / get_inverse / by_type | API calls named as nouns | "never completes" next to API name | N [en-gh-thatopen.md](../research_raw/wave1/en/en-gh-thatopen.md), [p-developer.md](../research_raw/wave1/roles/p-developer.md) |
| OOM / WASM / fps / memory leak | out of memory, WebAssembly | "memory climbs and climbs" | N [t-file-size.md](../research_raw/wave1/topics/t-file-size.md) |
| wexbim / IfcStore / Esent | xBIM library words | "IfcStore" | N [en-gh-xbim-others.md](../research_raw/wave1/en/en-gh-xbim-others.md) |
| node / lacing / custom node | Dynamo script words | "returns null" | N [en-dynamo-pyrevit.md](../research_raw/wave1/en/en-dynamo-pyrevit.md), [ai-revit-tasks.md](../research_raw/wave1/ai/ai-revit-tasks.md) |
| Method not found | error text quoted back to the AI | "every call says Method not found" | S [en-revit-auto-s006](../research_raw/wave1/ai/ai-revit-tasks.jsonl); N [ai-mcp-usage.md](../research_raw/wave1/ai/ai-mcp-usage.md) |

### Other authoring tools' own words (EN, language-independent)

| Tool | Word people use | What it is | IFC counterpart | Evidence |
|---|---|---|---|---|
| Archicad | zone, story, Element ID, IFC Manager / translator | room, storey, element id, export settings | `IfcSpace`, `IfcBuildingStorey`, Tag/Name, export preset | K; R [es-latam-r018](https://help.graphisoft.com/AC/28/SPA/_AC28_Help/121_IFC/121_IFC-1.htm) (Gestor IFC, traductores) |
| Tekla Structures | assembly, cast unit, pour object, reference model, UDA, Organizer | structural fabrication terms | `IfcElementAssembly`, user-defined attribute | N [en-tekla.md](../research_raw/wave1/en/en-tekla.md) |
| Vectorworks | custom record fields | user data fields | psets | S [en-allplan-vw-bentley-s002](../research_raw/wave1/en/en-allplan-vw-bentley.jsonl) |
| Civil 3D / Infraworks | corridor, alignment, profile | road design objects | `IfcAlignment`, `IfcRoad` | S [en-us-canada-infra-s003](../research_raw/wave1/en/en-us-canada-infra.jsonl) |

---

## 3. Russian (RU)

Russian speakers write product names in Cyrillic with case endings (в Ревите, из Теклы), and shorten IFC to **ифс** or **ифц**. Real forum titles are often Latin ("Экспорт из Tekla в Revit") while the body uses Cyrillic names. The spoken forms come mostly from the cell reports and synthetic prompts.

| Slang / jargon | Literal | Meaning | Standard term | Example fragment | Evidence and source |
|---|---|---|---|---|---|
| ифс | IFS (Cyrillic letters) | IFC as people say and type it | IFC | "открыл ифс в ревите, пусто, одни оси видны" | N [ru-dwg-other.md](../research_raw/wave1/ru/ru-dwg-other.md), [ru-autodesk-telegram.md](../research_raw/wave1/ru/ru-autodesk-telegram.md); S [ru-autodesk-telegram-s013](../research_raw/wave1/ru/ru-autodesk-telegram.jsonl) (56 synthetic uses) |
| ифц | IFTs (ц = "ts") | Variant of ифс | IFC | "Текла не открывает ифц" | N same; S [ru-dwg-other-s003](../research_raw/wave1/ru/ru-dwg-other.jsonl) |
| проксик, проксики, прокси, проксей | little proxy | Elements exported as the generic class | `IfcBuildingElementProxy` | "все проксики с именем Wall* переделай в IfcWall" | N [ru-dwg-other.md](../research_raw/wave1/ru/ru-dwg-other.md); S [ru-dwg-other-s007](../research_raw/wave1/ru/ru-dwg-other.jsonl); R [ru-habr-dev-r020](https://habr.com/ru/articles/590819/comments/) ("Proxy" in a heated comment) |
| ревит, в Ревите, из Ревита | Revit in Cyrillic | Revit | Revit | "при открытии в Ревите элементы теряются" | R [ru-dwg-other-r001](https://forum.dwg.ru/showthread.php?t=146029) |
| Текла | Tekla | Tekla Structures | Tekla | "конструкции из Теклы в Ревит не передаются нормально" | R [ru-dwg-other-r001](https://forum.dwg.ru/showthread.php?t=146029) |
| Архикад | Archicad | Archicad | Archicad | "работаю в Архикаде" | R [ru-dwg-other-r016](https://forum.dwg.ru/showthread.php?t=96356) |
| Сапфир | Sapphire | Russian BIM program SAPFIR-3D | SAPFIR-3D | "IFC из Сапфира в автокад не импортируется" | R [ru-dwg-other-r003](https://forum.dwg.ru/showthread.php?t=160240) |
| Навис, нависворкс | Navis | Navisworks | Navisworks | "Навис показывает 1500 коллизий, сервис 200" | R [ru-habr-dev-r003](https://habr.com/ru/articles/1089018/); S [ru-dwg-other-s014](../research_raw/wave1/ru/ru-dwg-other.jsonl) ("в нависе") |
| солибри | Solibri in Cyrillic | Solibri model checker | Solibri | "солибри их не видит" | S [ru-vm-s004](../research_raw/wave1/topics/t-versions-mvd.jsonl) |
| ренга, нанокад | Renga, nanoCAD | Russian BIM / CAD programs | Renga, nanoCAD | "ифс из ренги в ревит заходит" | N [ru-dwg-other.md](../research_raw/wave1/ru/ru-dwg-other.md), [ru-renga-nanocad.md](../research_raw/wave1/ru/ru-renga-nanocad.md); S [ru-renga-nanocad-s007](../research_raw/wave1/ru/ru-renga-nanocad.jsonl) |
| бцф | BCF in Cyrillic | Clash / issue exchange file | BCF | "найди пересечения труб с балками и скинь в бцф" | S [ru-renga-nanocad-s014](../research_raw/wave1/ru/ru-renga-nanocad.jsonl) |
| экспортнуть, импортнуть | to "export-ify" | Colloquial verbs made from English | export, import | "Как из ArchiCad экспортнуть в DWG Solid?" | R [ru-dwg-other-r021](https://forum.dwg.ru/showthread.php?t=75883) |
| выгрузка, выгрузить | unloading | Export from Revit. Strongly preferred over "экспорт" in practice. | export | "Два часа выгрузки ради пустого параметра" | R [ru-habr-dev-r001](https://habr.com/ru/articles/1089018/) |
| грузить в Ревит | load into Revit | Import or link into Revit | import | "заказчик требует выдавать IFC и грузить в Ревит" | R [ru-dwg-other-r002](https://forum.dwg.ru/showthread.php?t=146029) |
| тела / родные объекты | solids / native objects | After import, shapes instead of real Revit walls and doors | DirectShape vs native elements | "элементы приходят как тела, а не как родные объекты" | R [ru-dwg-other-r009](https://forum.dwg.ru/showthread.php?t=166052) |
| обобщённые модели | generic models | The Revit category Generic Models, source of proxies | Generic Models category | "колонны пришли обобщенными" | S [ru-eng-s010](../research_raw/wave1/roles/p-engineers.jsonl); K [../03_software/revit/ifc_export_reference.md](../03_software/revit/ifc_export_reference.md) |
| семейство | family | Revit family | Revit family; IFC type | "можно ли редактировать семейство из IFC в Ревите" | R [ru-dwg-other-r023](https://forum.dwg.ru/showthread.php?t=130296&page=2) |
| типоразмер | size-type | Revit family type; not exactly IFC "type" | family type, `IfcXxxType` | (UI term) | K [glossary](../08_glossary/glossary_multilingual.md) [V:17] |
| общие параметры, ФОП | shared parameters; shared-parameter file | Parameters defined once in a file and reused; the usual way to push custom data into IFC | shared parameter | "мои общие параметры куда-то пропали" | S [ru-dwg-revit-s002](../research_raw/wave1/ru/ru-dwg-revit.jsonl); N [ru-autodesk-telegram.md](../research_raw/wave1/ru/ru-autodesk-telegram.md) (ФОП listed) |
| RUS_* параметры | RUS_ prefix | Company parameters named RUS_Area, RUS_Height | custom parameters | "RUS_Height" | R [ru-autodesk-telegram-r009](https://habr.com/ru/companies/pik_digital/articles/1057314/) |
| пар-р | abbreviation of параметр | Parameter | parameter | "не заполнен пар-р Система и Маркировка" | S [ru-coord-s006](../research_raw/wave1/topics/t-coordinates.jsonl) |
| псеты, психеты | psets; "psychets" (joke) | Property sets | Pset | "покажи психеты у одной стены" | S [ru-autodesk-telegram-s010](../research_raw/wave1/ru/ru-autodesk-telegram.jsonl) |
| гуид | guid in Cyrillic | GlobalId | GUID | "guid опять поменялись" | S [ru-guid-s006](../research_raw/wave1/topics/t-guid-versioning.jsonl) |
| маппинг | mapping | Class or parameter mapping | mapping | "Codemill платный и с ручным маппингом" | R [ru-dwg-other-r004](https://forum.dwg.ru/showthread.php?t=173570) |
| постобработка | post-processing | Editing the IFC after export, outside Revit | post-processing | "Постобработка IFC без Revit" | R [ru-habr-dev-r006](https://habr.com/ru/articles/1100956/) |
| дубли | doubles | Duplicate elements that are invisible in the viewer | duplicates | "как найти дубли в IFC которых не видно" | R [ru-habr-dev-r008](https://habr.com/ru/articles/1100956/) |
| склейка | gluing | Merging models into one file | merge / federation | (jargon list) | N [ru-habr-dev.md](../research_raw/wave1/ru/ru-habr-dev.md) |
| зона, зоны | zone | Spatial unit with a boundary (apartment, area). Habr: zones with curved borders were counted in Revit but did not export as solids. | likely `IfcSpace` / `IfcZone` (check) | "зоны с кривыми границами не выгружаются как тело" | R [ru-habr-dev-r002](https://habr.com/ru/articles/1089018/) |
| помещение | room | Revit room | `IfcSpace` | "зоны пропадают" | N [ru-autodesk-telegram.md](../research_raw/wave1/ru/ru-autodesk-telegram.md) |
| косоуры | stair stringers | Stair parts that still export although export is off | `IfcStairFlight` parts / members | "косоуры выгружаются при Нет" | R [ru-habr-dev-r009](https://habr.com/ru/articles/1098340/) |
| связь, линк | link | Revit Link (a linked model) vs opening the IFC | link | "ифс открывается в ревите минут 40 ... связью лучше?" | S [ru-dwg-revit-s009](../research_raw/wave1/ru/ru-dwg-revit.jsonl) |
| точка съёмки, базовая точка | survey point, base point | Revit reference points for coordinates | Survey Point, Project Base Point | "вроде одна точка съёмки везде" | S [ru-autodesk-telegram-s006](../research_raw/wave1/ru/ru-autodesk-telegram.jsonl) |
| улетел, уехал | flew away | Model sits far from zero or shifted | wrong coordinates | "в нависе ифц улетел куда-то в сторону" | S [ru-dwg-other-s014](../research_raw/wave1/ru/ru-dwg-other.jsonl); N [t-coordinates.md](../research_raw/wave1/topics/t-coordinates.md) |
| кракозябры | scribbles | Garbled characters | mojibake | "в ифс названия типов как кракозябры" | S [enc-s001](../research_raw/wave1/topics/t-encoding.jsonl); N [t-encoding.md](../research_raw/wave1/topics/t-encoding.md) (seed term) |
| ЦИМ, ТИМ | acronyms | Digital information model; information-modelling technologies (Russian BIM) | BIM model / BIM | "нужно ли с 01.07.2019 переходить на ТИМ" | R [ru-dwg-other-r017](https://forum.dwg.ru/showthread.php?t=153428); R [ru-autodesk-telegram-r021](https://t.me/s/revithelper_kmv/146) (ЦИМ) |
| АГР | acronym | Architectural-urban concept approval; an XML data form | AGR submission | "площадь по зонам не сходится с XML АГР" | R [ru-habr-dev-r007](https://habr.com/ru/articles/1100956/) |
| ТЭП | acronym | Technical and economic indicators (areas, volumes) | project indicators | "площади ТЭП" | R [ru-habr-dev-r007](https://habr.com/ru/articles/1100956/) |
| МССК | acronym | Classifier of construction resources | classifier | (in Habr jargon list) | N [ru-habr-dev.md](../research_raw/wave1/ru/ru-habr-dev.md) |
| КЖ, АР, КР, ОВ, ВК | design-set codes | Reinforced-concrete drawings, architecture, structures, HVAC, water supply and drainage | discipline codes | "АР и ОВ в ифс не совмещаются по координатам" | R [ru-dwg-other-r027](https://dwg.ru/b/utrfm/263) (КЖ); S [ru-autodesk-telegram-s006](../research_raw/wave1/ru/ru-autodesk-telegram.jsonl); K |
| ВОР | acronym | Bill of work volumes (Russian BoQ) | BoQ | "объём бетона по этажам ... ВОР в эксель" | S [ru-aimcp-s011](../research_raw/wave1/ai/ai-mcp-usage.jsonl) |
| экспертиза, госэкспертиза | expertise | State design review where IFC/ЦИМ is submitted | state review | "эксперты не принимают прокси" | S [ru-tim-expertiza-s003](../research_raw/wave1/ru/ru-tim-expertiza.jsonl); R [ru-dwg-other-r017](https://forum.dwg.ru/showthread.php?t=153428) |
| заказчик требует IFC | the client demands IFC | Typical pressure phrase | none | "заказчик требует выдавать IFC" | R [ru-dwg-other-r002](https://forum.dwg.ru/showthread.php?t=146029) |
| работа в стол | work into the drawer | Requirements or deliverables nobody will use | none | "работа в стол" | N [ru-autodesk-telegram.md](../research_raw/wave1/ru/ru-autodesk-telegram.md) |
| получается фигня, всё пучком | comes out rubbish; all fine | Frustrated and satisfied verdicts | none | "получается фигня" | N [ru-dwg-other.md](../research_raw/wave1/ru/ru-dwg-other.md); R [ru-dwg-other-r029](https://forum.dwg.ru/showthread.php?t=154396) (notes) |
| глянь, скинь, сроки горят | look, drop me, deadlines burn | Casual imperatives to the AI | none | "глянь сколько в модели проксей" | S [ru-coord-s007](../research_raw/wave1/topics/t-coordinates.jsonl) (21 synthetic "глянь/посмотри") |
| эксель, ексель | Excel | Spreadsheet export target | Excel | "в эксель" | S [ru-aimcp-s011](../research_raw/wave1/ai/ai-mcp-usage.jsonl) |

---

## 4. Chinese (ZH)

Chinese text keeps product and class names in Latin letters, often lowercase and glued to Chinese characters (`revit导出ifc`, `ifc模型`). Mainland and Taiwan/Hong Kong differ: 导出/导入 vs 匯出/匯入. Developer blogs add English technical nouns (draw call, LOD, GLB).

| Slang / jargon | Literal | Meaning | Standard term | Example fragment | Evidence and source |
|---|---|---|---|---|---|
| 二开 / 二次开发 | second development | Writing plug-ins or add-ins on top of Revit (API work) | secondary development | "马上二开要失业了" | R [zh-aimcp-r023](https://github.com/mcp-servers-for-revit/revit-mcp-plugin/issues/11); R [zh-lightweight-review-r001](https://zhuanlan.zhihu.com/p/673078056) (Revit二次开发) |
| 翻模 | flip the model | Rebuild a Revit model from CAD / PDF drawings | CAD-to-BIM remodelling | "把dwg里A-WALL那层的双线墙翻成revit墙" | R [zh-revit-auto-r027](https://github.com/shuotao/REVIT_MCP_study/issues/150); S [zh-aimcp-s008](../research_raw/wave1/ai/ai-mcp-usage.jsonl) |
| 开孔 / 開孔, 洞口, 预留洞 | open a hole | Openings and reserved holes in walls / slabs / beams | `IfcOpeningElement` | "管线穿梁穿墙的位置，哪些还没开洞" | R [zh-revit-auto-r026](https://github.com/shuotao/REVIT_MCP_study/issues/99); S [zh-openings-s012](../research_raw/wave1/topics/t-openings-penetrations.jsonl) |
| 套管 | casing / sleeve | A sleeve through a wall or beam for a pipe | pipe sleeve (no fixed IFC class) | "每个穿透点需要的套管口径" | R [zh-revit-auto-r026](https://github.com/shuotao/REVIT_MCP_study/issues/99); S [zh-revit-auto-s011](../research_raw/wave1/zh/zh-revit-auto.jsonl) |
| 穿樑 / 穿梁 | pass through beam | A pipe crossing a beam | beam penetration | "水管穿樑的位置" | R [zh-revit-auto-r026](https://github.com/shuotao/REVIT_MCP_study/issues/99) |
| 图块 / 圖塊 | picture block | CAD block | CAD block | (jargon list) | N [ai-revit-tasks.md](../research_raw/wave1/ai/ai-revit-tasks.md) |
| 构件 / 構件 / 要素 | component / element | Any building element in the model | building element, `IfcElement` | "导进revit构件丢了不少" | R [zh-csdn-dev-r002](https://juejin.cn/post/7691297274821705728) ("合并构件"); S [zh-roundtrip-s009](../research_raw/wave1/topics/t-roundtrip-interop.jsonl) |
| 属性集 / 属性表 | attribute set / table | Property set | Pset | "读入IFC文件... 加属性集" | R [zh-csdn-dev-r006](https://www.cnblogs.com/herd/p/12183392.html) |
| 属性 | attribute / property | Used for both IFC attribute and IFC property; context decides | attribute, property | "属性集里值为空的构件" | K [glossary note](../08_glossary/glossary_multilingual.md); S [zh-lightweight-review-s004](../research_raw/wave1/zh/zh-lightweight-review.jsonl) |
| 轻量化 | make light | Convert or compress a heavy model so it displays smoothly (web, mobile) | lightweighting / simplified viewing format | "BIM轻量化之路（一）" | R [zh-csdn-dev-r004](https://www.cnblogs.com/nihaozhe/articles/13651935.html); R [zh-zhihu-r019](https://www.zhihu.com/question/385964946) |
| 减肥 | slim down | Reduce file size | decimation | "IFC转Revit模型后体积暴涨怎么减肥" | R [zh-zhihu-r035](https://blog.csdn.net/zzutt/article/details/121492254) |
| 合模 | merge models | Combine discipline models | federation | "高效合模神器" (viewer promo) | R [zh-zhihu-r032](https://zhuanlan.zhihu.com/p/634784856) |
| 报建 / 报批 / 报审 | file for construction / for approval / review | Submitting the BIM model to a city permit system | permit submission | "BIM报批报建之Revit端自检工具" | R [zh-lightweight-review-r002](https://zhuanlan.zhihu.com/p/633827596) |
| 审图 | review drawings | Authority review of construction drawings, now with BIM | drawing review | "广州开始BIM审图试点" | R [zh-lightweight-review-r021](https://zhuanlan.zhihu.com/p/504617257) |
| 自检 | self-check | Pre-submission check by the city's tool (e.g. SZ-IFC self-check) | self-check tool | "1.1.0版本自检通过的模型传不上去" | R [zh-lightweight-review-r003](https://zhuanlan.zhihu.com/p/672903162) |
| SZ-IFC | Shenzhen IFC | Shenzhen's IFC storage standard for permit submissions | SZ-IFC (SJG114-2022) | "SZ-IFC自检工具" | R [zh-lightweight-review-r027](https://zjj.sz.gov.cn/attachment/0/678/678888/7768421.pdf) |
| 图模一致 / 图模对位 | drawing-model match | The model must agree with the 2D drawings | drawing-model consistency | "图模对位不合格传不上去" | R [zh-lightweight-review-r023](https://zfcj.gz.gov.cn/attachment/7/7943/7943479/10589336.pdf) |
| 项目基点 / 测量点 / 基点 | project base point / survey point | Revit reference points | Project Base Point, Survey Point | "测量点基点怎么设才能定位拼起来，求教" | R [zh-revit-export-r023](https://zhidao.baidu.com/question/1755259387786621668.html) |
| 2000坐标 | "2000 coordinates" | China Geodetic Coordinate System 2000 | CGCS2000 | "项目基点坐标是不是2000的" | R [zh-revit-export-r003](https://ask.csdn.net/questions/8816624); S [zh-lightweight-review-s001](../research_raw/wave1/zh/zh-lightweight-review.jsonl) |
| 乱码 | messy code | Garbled text from an encoding problem | mojibake | "which Chinese encoding ... still messy code" | R [zh-csdn-dev-r013](https://github.com/IfcOpenShell/IfcOpenShell/issues/571); S [zh-err-s006](../research_raw/wave1/topics/t-error-messages.jsonl) |
| 卡 / 卡顿 | stuck / jerky | Slow, laggy viewing | performance problem | "为什么这么卡" | R [zh-csdn-dev-r001](https://juejin.cn/post/7698926562423357450) |
| 踩坑 | step in a pit | A hard-won lesson, blog-title genre | pitfall | (genre word) | N [zh-csdn-dev.md](../research_raw/wave1/zh/zh-csdn-dev.md) |
| 导进 / 链进来 | lead in / link in | Import / link an IFC into Revit | import, link | "MAX模型导进Revit材质全没了" | R [zh-revit-export-r004](https://ask.csdn.net/questions/8796533) |
| 丢了 / 丢失 | lost | Elements or properties missing after export or import | missing data | "Revit导出IFC会丢哪些信息" | R [zh-csdn-dev-r032](https://blog.csdn.net/weixin_39590472/article/details/112503752) |
| 映射表 | map table | Revit-to-IFC mapping table | IFC mapping table | "revit导出ifc对应类型" | R [zh-csdn-dev-r007](https://www.cnblogs.com/liaocheng/p/15905467.html) |
| 族 / 族类型 / 类别 / 共享参数 / 标高 | family / type / category / shared parameter / level | Revit UI words | family, type, category, shared parameter, level | "我自己加的共享参数属性集没了" | S [zh-psets-s016](../research_raw/wave1/topics/t-psets-params.jsonl); K [glossary](../08_glossary/glossary_multilingual.md) [V:26] |
| 楼层 | floor | Storey, whether called 标高 (Revit) or 楼层 (everyday) | `IfcBuildingStorey` | "每层有多少面墙" | S [zh-aimcp-s007](../research_raw/wave1/ai/ai-mcp-usage.jsonl) |
| 幕墙 / 竖梃 | curtain wall / mullion | Curtain wall parts | `IfcCurtainWall`, `IfcMember` | "幕墙导出IFC后竖梃都没了" | S [zh-geom-s008](../research_raw/wave1/topics/t-geometry.jsonl) |
| 算量 / 工程量 | calculate quantity | Quantity take-off | QTO | "按楼层统计一下混凝土墙、板、柱的体积" | S [zh-qto-s011](../research_raw/wave1/topics/t-qto-cost.jsonl) |
| 甲方 | Party A | The client | owner / client | "甲方要求交付IFC2x3" | S [zh-vm-s007](../research_raw/wave1/topics/t-versions-mvd.jsonl) |
| 碰撞 / 碰撞检查 | collision check | Clash detection | clash detection | "机电和结构ifc做个碰撞检查" | S [zh-clash-s009](../research_raw/wave1/topics/t-clash-bcf.jsonl) |
| 三角面 / 拾取 / draw call | triangles / picking | Web 3D rendering vocabulary | triangles, picking | "WebGL三角面多了内存爆" | R [zh-csdn-dev-r004](https://www.cnblogs.com/nihaozhe/articles/13651935.html) |
| Su / MAX / pln | SketchUp / 3ds Max / ArchiCAD file | Short names of other programs and files | SketchUp, 3ds Max, `.pln` | "Su导进Revit材质总是丢" | R [zh-revit-export-r020](https://zhuanlan.zhihu.com/p/372183287); R [zh-revit-export-r005](https://zhidao.baidu.com/question/593298625.html) |
| 神器 / 干货 / 保姆级教程 | killer tool / substance / nanny-level tutorial | Hype words in titles | none | "干货满满，设计师聊广州市BIM审查" | R [zh-lightweight-review-r021](https://zhuanlan.zhihu.com/p/504617257); N [zh-zhihu.md](../research_raw/wave1/zh/zh-zhihu.md) |
| 信创 / 国产 / 自主可控 | IT-innovation / domestic / self-controllable | Domestic software push in government projects | domestic stack | "国产BIM软件" | R [zh-zhihu-r027](https://www.zhihu.com/question/642487361); N [zh-lightweight-review.md](../research_raw/wave1/zh/zh-lightweight-review.md) |
| 宁建模 / 存证 | Nanjing model / certificate storage | Local permit file format and record keeping | local standards | (list) | N [zh-lightweight-review.md](../research_raw/wave1/zh/zh-lightweight-review.md); R [zh-lightweight-review-r024](http://ghj.nanjing.gov.cn/njsgtzyj/202103/t20210301_2834720.html) |
| 求教 / 请教 | beg advice | Humble closer of a question | none | "...求教" | R [zh-revit-export-r023](https://zhidao.baidu.com/question/1755259387786621668.html) |
| 匯出 / 匯入, 檔, 圖則, 牆, 樑 (Traditional) | export / import, file, plans, wall, beam | Taiwan / Hong Kong spelling and vocabulary; 圖則 and 認可人士 (AP) are Hong Kong terms | export, import | "IFC檔太大傳不上系統" | N [zh-tw-hk.md](../research_raw/wave1/zh/zh-tw-hk.md); S [zh-revit-auto-s011](../research_raw/wave1/zh/zh-revit-auto.jsonl) |
| 工业基础类 | industrial foundation class | The Chinese expansion of IFC | Industry Foundation Classes | (formal text) | N [zh-csdn-dev.md](../research_raw/wave1/zh/zh-csdn-dev.md) |

---

## 5. Spanish (ES)

Voseo (Creá, contame) shows up in Rioplatense prompts. Spain and Latin America use different words for the same Revit and cost concepts. Most casual forms are **S**.

| Slang / jargon | Literal | Meaning | Standard term | Example fragment | Evidence and source |
|---|---|---|---|---|---|
| ifc (lowercase), proxys | plural with s | IFC; proxy elements. Real posts also write IFC's with an English apostrophe. | `IfcBuildingElementProxy` | "problemas con los ifc" | R [es-spain-r001](https://forums.autodesk.com/t5/revit-architecture-forum/problemas-con-ifc-s/td-p/10189111); S [es-latam-s001](../research_raw/wave1/es/es-latam.jsonl) |
| sale como proxy | comes out as proxy | Element lost its class | proxy | "sale como proxy" | N [es-spain.md](../research_raw/wave1/es/es-spain.md) |
| corrida | run | A batch run of a takeoff tool ("corrida 5 HVAC") | tool run | "Ejecuta la corrida 5 HVAC sobre mi selección" | R [es-aimcp-r032](https://github.com/JefaturaBIM94/RevitMCPBOQ) |
| creá / contame / dame | voseo imperative | Direct commands to the AI | none | "Creá cuatro muros de 3 m" | R [es-aimcp-r031](https://github.com/joacos/archicad-mcp); S [es-aimcp-s016](../research_raw/wave1/ai/ai-mcp-usage.jsonl) |
| metrados | measured amounts | Quantities (Peru, parts of LatAm) | quantity take-off | "necesito los metrados de muros, losas y columnas por nivel" | S [es-latam-s003](../research_raw/wave1/es/es-latam.jsonl); N [es-latam.md](../research_raw/wave1/es/es-latam.md) |
| cómputo | computation | Quantity take-off (Argentina, others) | takeoff | (jargon list) | N [es-latam.md](../research_raw/wave1/es/es-latam.md) |
| mediciones | measurements | Quantities for a budget (Spain) | takeoff | "necesito mediciones de muros por planta" | S [es-spain-s007](../research_raw/wave1/es/es-spain.jsonl) |
| ambientes | environments | Rooms (Argentina, Chile, Peru) | `IfcSpace` | "pásame los ambientes con nombre y área" | S [es-latam-s014](../research_raw/wave1/es/es-latam.jsonl); N |
| estancia | stay | Room (Spain) | `IfcSpace` | "superficie total por tipo de estancia" | S [es-spain-s016](../research_raw/wave1/es/es-spain.jsonl) |
| nivel / planta | level / floor | LatAm "nivel", Spain "planta" for storey | `IfcBuildingStorey` | "lista los niveles con su cota" | S [es-latam-s005](../research_raw/wave1/es/es-latam.jsonl), [es-spain-s006](../research_raw/wave1/es/es-spain.jsonl) |
| hormigón / concreto | concrete | Spain "hormigón", LatAm often "concreto" (the data used hormigón) | concrete | "volumen de hormigón por planta" | S [es-eng-s014](../research_raw/wave1/roles/p-engineers.jsonl); K |
| pilar / columna; losa / forjado | column; slab | Spain "pilar", LatAm "columna" | `IfcColumn`, `IfcSlab` | "pasalos a IfcColumn los que tengan 'pilar'" | S [es-spain-s004](../research_raw/wave1/es/es-spain.jsonl) |
| conductos / ductos | ducts | Spain "conductos", LatAm "ductos" | `IfcDuctSegment` | "dame los ductos por nivel" | S [es-aimcp-s015](../research_raw/wave1/ai/ai-mcp-usage.jsonl); S [es-spain-s010](../research_raw/wave1/es/es-spain.jsonl) |
| hueco | hole | Spain: opening in a wall | opening | "las ventanas no hacen hueco en el muro" | S [es-spain-s012](../research_raw/wave1/es/es-spain.jsonl) |
| cuantía | quantity (rebar/concrete rate) | Missing quantities | quantity | "avisame si falta algun cuantia" | S [es-s009](../research_raw/wave1/es/es-latam.jsonl) |
| nativo | native | The Revit file; clients ask "IFC y nativo" | native file | "piden ifc y nativo" | S [es-latam-s016](../research_raw/wave1/es/es-latam.jsonl) |
| qué onda | what's up | Mexican colloquial opener | none | "en el 2024 andaba bien, qué onda" | S [es-latam-s004](../research_raw/wave1/es/es-latam.jsonl) |
| lejisimos | farthest | Intentional misspelling of "lejísimos": model is very far from origin | far from origin | "sale lejisimos del origen" | S [es-spain-s005](../research_raw/wave1/es/es-spain.jsonl); N [es-spain.md](../research_raw/wave1/es/es-spain.md) |
| pesa 800mb | weighs 800 MB | File size complaint | file size | "el ifc pesa 800mb y no abre" | S [es-latam-s010](../research_raw/wave1/es/es-latam.jsonl); N |
| MIDE, MEI, fichas IFC | Chile's PlanBIM documents | Information matrix and checking files for public projects | MIDE | "revisa si el modelo cumple la MIDE de planbim" | R [es-latam-r012](https://planbim.cl/documentos/mide/); S [es-latam-s002](../research_raw/wave1/es/es-latam.jsonl) |
| Gestor IFC, traductores | IFC manager, translators | Archicad's export settings in Spanish | IFC Manager, translator | (help text) | R [es-latam-r018](https://help.graphisoft.com/AC/28/SPA/_AC28_Help/121_IFC/121_IFC-1.htm) |
| Plan BIM, licitación | tender | Spanish public procurement context | public tender | "licitación con Plan BIM" | S [es-spain-s003](../research_raw/wave1/es/es-spain.jsonl); R [es-spain-r022](https://www.construible.es/2023/05/02/mitma-aprueba-propuesta-plan-implantacion-bim-contra) |
| familia, tipo, ejemplar, parámetro compartido, subproyecto | Revit UI words (subproyecto = workset) | Spanish Revit terms; "ejemplar" = instance | family, type, instance, shared parameter, workset | (UI terms) | K [glossary](../08_glossary/glossary_multilingual.md) [V:21], [V:29][49] |
| sin accentos, mayúsculas | accentless / caps | "Exportacion", "Descripcion"; all-caps titles | none | "SOPOTARÁ ARCHIVOS IFC?" | R [es-latam-r001](https://github.com/ingelibre/ingetrazo/issues/1033); R [es-latam-r003](https://github.com/jmarinderko/calculadora-RIC/issues/10) |

---

## 6. Portuguese (PT, mostly Brazilian)

All Portuguese slang below is **S** unless marked: the corpus has no real Portuguese chat record. Treat as plausible, not proven.

| Slang / jargon | Literal | Meaning | Standard term | Example fragment | Evidence and source |
|---|---|---|---|---|---|
| compatibilização | making compatible | Coordination of discipline models, the standard Brazilian word | coordination | "preciso mandar a compatibilização hoje" | S [pt-brazil-s001](../research_raw/wave1/pt/pt-brazil.jsonl) |
| incompatibilidades / apontamentos | incompatibilities / notes | Clashes / BCF issues sent to the designer | clash issues | "gera os apontamentos em BCF pro projetista" | S [pt-clash-s011](../research_raw/wave1/topics/t-clash-bcf.jsonl), [pt-brazil-s007](../research_raw/wave1/pt/pt-brazil.jsonl) |
| quantitativo | quantitative | Quantity take-off | QTO | "quantitativo das portas e janelas por tipo" | S [pt-qto-s014](../research_raw/wave1/topics/t-qto-cost.jsonl) |
| pavimento | pavement (floor) | Storey | `IfcBuildingStorey` | "por pavimento" | S [pt-brazil-s003](../research_raw/wave1/pt/pt-brazil.jsonl) |
| ambiente | environment | Room | `IfcSpace` | "área de todos os ambientes por pavimento" | S [pt-revit-auto-s015](../research_raw/wave1/ai/ai-revit-tasks.jsonl) |
| furo | hole | Penetration in a slab / wall | opening | "lista os furos nas lajes" | S [pt-openings-s015](../research_raw/wave1/topics/t-openings-penetrations.jsonl) |
| laje, pilar, viga | slab, column, beam | Structural elements | `IfcSlab`, `IfcColumn`, `IfcBeam` | "pilares, vigas e lajes por pavimento" | S [pt-brazil-s003](../research_raw/wave1/pt/pt-brazil.jsonl) |
| prumadas, shafts | risers, shafts | Vertical service runs | shaft | "passagem de shafts e prumadas" | S [pt-openings-s015](../research_raw/wave1/topics/t-openings-penetrations.jsonl) |
| cronograma | schedule | Project programme (4D) | schedule | "ainda nao tem atividade no cronograma" | S [pt-s010](../research_raw/wave1/pt/pt-brazil.jsonl) |
| alvará | permit | Building permit | permit | "preciso pro alvará" | S [pt-permit-s015](../research_raw/wave1/topics/t-permits-codecheck.jsonl) |
| cara, mano, né | dude | Casual address to the AI | none | "cara olha o ifc e me fala quantos elementos viraram proxy" | S [pt-brazil-s001](../research_raw/wave1/pt/pt-brazil.jsonl) |
| viraram proxy | turned into proxy | Elements lost their class | proxy | same | S |
| tá, tao, pra, n (contractions) | informal spelling | Everyday contractions typed to chat | none | "tao sem os campos obrigatorios do cobie" | S [pt-cobie-s012](../research_raw/wave1/topics/t-cobie-fm.jsonl) |
| SIRGAS 2000 | geodetic system | Brazilian CRS | CRS | "georreferenciado em SIRGAS 2000" | S [mul-coord-s012](../research_raw/wave1/topics/t-coordinates.jsonl) |
| fck, Eberick | concrete strength; Brazilian structural program | Property and tool names | none | "seção, fck e em qual pavimento tá" | S [pt-brazil-s010](../research_raw/wave1/pt/pt-brazil.jsonl), [pt-brazil-s003](../research_raw/wave1/pt/pt-brazil.jsonl) |
| BEP, EIR | kept in English | Plan / requirements documents | BEP, EIR | "padrão do BEP" | S [pt-brazil-s004](../research_raw/wave1/pt/pt-brazil.jsonl) |
| ABNT NBR 15965 | classification standard | Brazilian classification | classification | (standard name) | N [t-classification-bsdd.md](../research_raw/wave1/topics/t-classification-bsdd.md) |
| Archstation | CAD program | Name in a real Bonsai failure report | none | "IFC from Archstation does not open in Bonsai" | R [en-gh-encoding-r019](https://github.com/IfcOpenShell/IfcOpenShell/issues/7305) |
| família, tipo, instância, parâmetro compartilhado, prancha | Revit terms (prancha = sheet) | Brazilian Revit UI | family, type, instance, shared parameter, sheet | (UI terms) | K [glossary](../08_glossary/glossary_multilingual.md) [V:22]. In Portugal "ficheiro" replaces "arquivo" (K, unverified). |

---

## 7. German (DE)

Real German-language evidence is thin (German experts post in English, and bim-me-up.com blog titles are real German). The jargon below is mostly **S or N**.

| Slang / jargon | Literal | Meaning | Standard term | Example fragment | Evidence and source |
|---|---|---|---|---|---|
| TGA | technical building services | MEP (heating, ventilation, plumbing, electrical) | MEP | "TGA gegen Tragwerk" | N [de-dach.md](../research_raw/wave1/de/de-dach.md); S [de-clash-s012](../research_raw/wave1/topics/t-clash-bcf.jsonl) |
| Durchbruch, Aussparung, Schlitz | breakthrough, recess, slot | Opening types in walls / slabs | `IfcOpeningElement` | "Öffnung, Durchbruch, Schlitz" | R [de-dach-r028](https://www.bimpedia.de/artikel/16092-oeffnung-durchbruch-schlitz/); S [de-geom-s011](../research_raw/wave1/topics/t-geometry.jsonl) |
| Wanddurchbrüche / Deckendurchbrüche | wall / slab breakthroughs | Penetrations | openings | "zeig mir alle Wanddurchbrüche im Arch-Modell" | S [de-dach-s001](../research_raw/wave1/de/de-dach.jsonl) |
| LV | Leistungsverzeichnis | Bill of quantities | BoQ | "Liste fürs LV, nur Außenwände" | S [de-dach-s007](../research_raw/wave1/de/de-dach.jsonl); N |
| AIA / BAP | client requirements / execution plan | German names for EIR / BEP | EIR / BEP | "sonst fliegen wir beim AIA-Check raus" | S [de-dach-s004](../research_raw/wave1/de/de-dach.jsonl); R [de-dach-r026](../research_raw/wave1/de/de-dach.md) |
| OKFF / OKRD | upper edge finished floor / raw ceiling | Two level references per storey | level definitions | "Elemente auf OKRD-Ebenen ... dem OKFF-Geschoss zuordnen" | S [de-dach-s006](../research_raw/wave1/de/de-dach.jsonl) |
| Fachmodell | discipline model | One discipline's model | discipline model | "Fachmodelle passen nicht übereinander" | S [de-dach-s003](../research_raw/wave1/de/de-dach.jsonl); N |
| Rohbau, Statik | shell, structural analysis | Structural shell model; structural engineering | structural model | "Stand 12 und Stand 14 vom Rohbau-IFC" | S [de-dach-s008](../research_raw/wave1/de/de-dach.jsonl) |
| Stand 12 / KW12 | status 12 / calendar week 12 | German way to name a revision | revision | "vergleich mal Stand KW12 und KW14" | S [de-guid-s008](../research_raw/wave1/topics/t-guid-versioning.jsonl) |
| Geschoss, Bauteil, Stütze, Unterzug | storey, building part, column, downstand beam | Core element words | `IfcBuildingStorey`, `IfcColumn`, `IfcBeam` | "Stützen sind alle als Proxy drin" | S [de-dach-s012](../research_raw/wave1/de/de-dach.jsonl) |
| Projektbasispunkt, Vermessungspunkt, Projektnullpunkt | project base point, survey point | Revit and site reference points | PBP, survey point | "wo sitzt der Projektbasispunkt in der IFC" | S [de-dach-s003](../research_raw/wave1/de/de-dach.jsonl), [de-coord-s018](../research_raw/wave1/de/de-dach.jsonl) |
| Kostengruppe (KG) DIN 276 | cost group | German classification of building costs | DIN 276 | "hat jedes Bauteil eine Kostengruppe DIN 276" | S [de-classbsdd-s013](../research_raw/wave1/topics/t-classification-bsdd.jsonl) |
| NGF, Raumliste | net floor area, room list | Area measure, space schedule | `NetFloorArea` | "ob jeder Raum eine Raumnummer und NGF hat" | S [de-cobie-s009](../research_raw/wave1/topics/t-cobie-fm.jsonl) |
| Kollision / Kollisionsprüfung | collision | Clash check | clash detection | "mach mal Kollisionsprüfung TGA gegen Tragwerk" | S [de-clash-s012](../research_raw/wave1/topics/t-clash-bcf.jsonl) |
| Stahlliste, Bewehrung | steel list, reinforcement | Rebar schedule | rebar | "mach mir ne Stahlliste aus dem IFC" | S [de-struct-s012](../research_raw/wave1/topics/t-structural.jsonl) |
| F90 | fire class | 90-minute fire resistance | fire rating | "durchdringen F90 Wände" | N [de-dach.md](../research_raw/wave1/de/de-dach.md); S [de-dach-s009](../research_raw/wave1/de/de-dach.jsonl) |
| mach mal, prüf mal, zeig mir | do it, check it | Casual imperative with "mal" | none | "prüf mal ob alle Räume ne Nutzung haben" | S [en-fmor-s014](../research_raw/wave1/roles/p-fm-owner-reviewer.jsonl) (15 synthetic uses) |
| ne, nen | eine, einen | Spoken contraction | none | "ne Stahlliste" | S [de-struct-s012](../research_raw/wave1/topics/t-structural.jsonl) |
| Typenparameter, Exemplarparameter | type / instance parameter | Revit parameter kinds in German | type parameter | "Revit Typenparameter nach IFC exportieren" | R [en-blogs-linkedin-r009](https://bim-me-up.com/revit-typenparameter-nach-ifc-exportieren/) |
| Gesamtmodell | total model | Federated model; appears in file names | federated model | (file name) | N [en-gh-ifcopenshell.md](../research_raw/wave1/en/en-gh-ifcopenshell.md) |
| Leerrohr | empty conduit | Electrical conduit, leaks into English posts | conduit | (German UI string in English post) | N [en-dynamo-pyrevit.md](../research_raw/wave1/en/en-dynamo-pyrevit.md) |
| Bearbeitungsbereich, Merkmal vs Eigenschaft | workset; characteristic vs property | Revit workset; two words for property | workset, property | (UI terms) | K [glossary](../08_glossary/glossary_multilingual.md) [V:27] |
| Umlaute, Dezimalkommas | umlauts, decimal commas | Encoding and CSV problems | encoding | "stimmen Umlaute und Dezimalkommas in den Psets" | S [enc-s010](../research_raw/wave1/topics/t-encoding.jsonl) |

---

## 8. French (FR)

Only 2 real French records exist; everything casual below is **S**. The report itself warns the terms are plausible, not verified.

| Slang / jargon | Literal | Meaning | Standard term | Example fragment | Evidence and source |
|---|---|---|---|---|---|
| maquette | model | The BIM model | BIM model | "murs sans résistance au feu dans la maquette" | N [fr-francophone.md](../research_raw/wave1/fr/fr-francophone.md); S [fr-francophone-s001](../research_raw/wave1/fr/fr-francophone.jsonl) |
| synthèse | synthesis | Coordination between trades | coordination | "avant la synthèse" | N [fr-francophone.md](../research_raw/wave1/fr/fr-francophone.md); S [fr-francophone-s005](../research_raw/wave1/fr/fr-francophone.jsonl) |
| indice B / indice C | index B | Revision letter | revision | "compare l'indice B et l'indice C" | S [fr-francophone-s005](../research_raw/wave1/fr/fr-francophone.jsonl) |
| DOE, GMAO | as-built file; maintenance software | Handover documents and CMMS | handover, CMMS | "liste des équipements ... pour le DOE / GMAO" | S [fr-francophone-s011](../research_raw/wave1/fr/fr-francophone.jsonl) |
| SDP | surface de plancher | Floor area for permits | gross floor area | "SDP et surface utile" | S [fr-francophone-s003](../research_raw/wave1/fr/fr-francophone.jsonl) |
| MOA, MOE, lot | project owner, designer, trade package | Roles and packages | owner, designer | "charte BIM du MOA" | S [fr-francophone-s015](../research_raw/wave1/fr/fr-francophone.jsonl) |
| convention BIM, charte BIM, cahier des charges BIM | BIM agreement / charter | Project BIM rules | BEP / EIR | "la convention BIM l'exige" | S [fr-francophone-s001](../research_raw/wave1/fr/fr-francophone.jsonl) |
| CCTP, DPGF | technical spec; priced breakdown | Tender documents | spec / BoQ | "métrés pour le DPGF" | N [fr-francophone.md](../research_raw/wave1/fr/fr-francophone.md); S [fr-s012](../research_raw/wave1/fr/fr-francophone.jsonl) |
| métré | metering | Quantity take-off | QTO | "j'ai besoin d'un métré par lot" | S [fr-qto-s016](../research_raw/wave1/topics/t-qto-cost.jsonl) |
| gaines, locaux, niveau, RDC, R+1 | ducts, rooms, level, ground floor, floor 1 | Everyday building words | duct, `IfcSpace`, storey | "RDC, R+1..." | S [fr-francophone-s004](../research_raw/wave1/fr/fr-francophone.jsonl), [fr-francophone-s007](../research_raw/wave1/fr/fr-francophone.jsonl) |
| voile, dalle, poteau | concrete wall, slab, column | Structural words | `IfcWall`, `IfcSlab`, `IfcColumn` | "murs + dalles + poteaux" | S [fr-francophone-s009](../research_raw/wave1/fr/fr-francophone.jsonl) |
| trémie, réservation | shaft hole, reservation | Openings left for services | opening | "réservations MEP par rapport aux trémies" | S [fr-openings-s016](../research_raw/wave1/topics/t-openings-penetrations.jsonl) |
| PMR | reduced-mobility persons | Accessibility check | accessibility | "accessibilité PMR : portes < 90 cm" | S [fr-permit-s014](../research_raw/wave1/topics/t-permits-codecheck.jsonl) |
| MediaConstruct, RGF93 / Lambert 93 | French BIM association; French CRS | Local standards | CRS | "géoréférencement RGF93 / Lambert 93" | S [fr-francophone-s010](../research_raw/wave1/fr/fr-francophone.jsonl), [mul-coord-s014](../research_raw/wave1/topics/t-coordinates.jsonl) |
| Mo | mégaoctet | French "MB"; leaks into English posts | MB | "15Mo IFC file takes more than 5 minutes" | R [en-gh-thatopen-r003](https://github.com/ThatOpen/engine_web-ifc/issues/527) |
| pb, maj, ça m'affiche rien | problem, update | Chat shorthand | none | "c'est quoi le pb" | S [fr-francophone-s014](../research_raw/wave1/fr/fr-francophone.jsonl), [fr-clash-s013](../research_raw/wave1/topics/t-clash-bcf.jsonl) |
| famille, paramètre partagé, occurrence, sous-projet | Revit UI (occurrence = instance, sous-projet = workset) | French Revit terms | family, shared parameter, instance, workset | (UI terms) | K [glossary](../08_glossary/glossary_multilingual.md) [V:20][48] |

---

## 9. Italian, Japanese, Korean

### Italian (IT)

Real records are vendor articles (biblus.acca.it, ingenio-web.it) whose headings turn into questions; there is no forum chat. Casual forms are **S**.

| Slang / jargon | Literal | Meaning | Standard term | Example fragment | Evidence and source |
|---|---|---|---|---|---|
| fuori di km | out by kilometres | Model located kilometres from origin | wrong coordinates | "uno è fuori di km" | R [it-italy-r005](https://biblus.acca.it/ifc-coordinate-system/) |
| sballato / sballate | out of whack | Units or coordinates wrong | wrong values | "misure sballate" | R [it-italy-r013 (paraphrase)](https://www.ingenio-web.it/articoli/ifc-in-pratica-unita-di-misura-dove-tr); S [it-italy-s003](../research_raw/wave1/it/it-italy.jsonl) |
| proxy | proxy | Same loan | `IfcBuildingElementProxy` | "i muri sono finiti come proxy" | R [it-italy-r001](https://biblus.acca.it/problemi-editing-file-ifc/) |
| mappatura classi / class mapping | class mapping | Revit mapping file | mapping table | "come carico il file di mappatura classi IFC" | R [it-italy-r003](https://biblus.acca.it/ifc-class-mapping-file/) |
| capitolato informativo, oGI, pGI | information specification; offer / plan for information management | Italian EIR and BEP-like documents | EIR, BEP | "se non presento l'oGI vengo escluso?" | R [it-italy-r018](https://biblus.acca.it/notizie/appalti-bim-lofferta-di-gestione-informativa-e-obbligatoria/), [it-italy-r004](https://biblus.acca.it/nuovo-codice-appalti-il-bim-e-obbligatorio/) |
| ACDat | data sharing environment | Italian name for CDE | CDE | (tender term) | R [it-italy-r004](https://biblus.acca.it/nuovo-codice-appalti-il-bim-e-obbligatorio/) |
| stazione appaltante, RUP, RTI, DL, CSE | contracting authority, project manager, consortium, site manager | Tender and site roles | public client | "Requisiti BIM negli RTI" | R [it-italy-r020](https://biblus.acca.it/notizie/requisiti-bim-negli-rti-conta-il-professionista-o-il-gruppo-di-lavoro/); R [it-italy-r019](https://biblus.acca.it/notizie/bim-maggiorazione-del-10-anche-per-direzione-lavori-e-cse/) |
| computo (metrico) | metric computation | Quantity take-off | QTO | "mi servono per il computo oggi" | S [it-italy-s017](../research_raw/wave1/it/it-italy.jsonl) |
| locali, stanze, ambienti | rooms | Rooms | `IfcSpace` | "lista locali con superficie e nome" | S [it-italy-s014](../research_raw/wave1/it/it-italy.jsonl) |
| solai, pilastro, muri, piano | slabs, column, walls, floor | Building words | `IfcSlab`, `IfcColumn` | "i proxy con nome 'Pilastro' mettili come IfcColumn" | S [it-italy-s009](../research_raw/wave1/it/it-italy.jsonl) |
| forature | perforations | Openings for services | openings | "quali forature sono cambiate" | S [it-openings-s019](../research_raw/wave1/topics/t-openings-penetrations.jsonl) |
| verbale di consegna | handover record | Delivery document | handover | "per il verbale di consegna" | S [it-italy-s013](../research_raw/wave1/it/it-italy.jsonl) |
| usBIM, Edificius, EdiLus | ACCA products | Italian vendor tools | none | "usBIM.checker" | R [it-italy-r027](https://biblus.acca.it/usbim-checker-verifica-informativa-del-modello/); N [it-italy.md](../research_raw/wave1/it/it-italy.md) |
| decreto BIM 560/2017 | law | Italian mandate | regulation | "il decreto BIM 560/2017 impone IFC?" | R [it-italy-r028](https://biblus.acca.it/obbligo-di-adozione-del-bim-capitolati-informativi-e-formati-di-interscambio-le-prime-osservazioni-ad-decreto-bim/) |

### Japanese (JA)

Japanese keeps IFC class names in Latin, writes Revit terms in katakana (ファミリ, レベル), and uses casual verb-stem requests to an AI (出して, 調べて). Real records are blog voice; casual chat is **S**.

| Slang / jargon | Literal | Meaning | Standard term | Example fragment | Evidence and source |
|---|---|---|---|---|---|
| 確認申請 | confirmation application | Building-permit filing | building confirmation | "確認申請用に出したIFC" | R [ja-japan-r016](https://note.com/kensesu_ai/n/nee08ddde31f1); S [ja-japan-s002](../research_raw/wave1/ja/ja-japan.jsonl) |
| BIM図面審査 / BIMデータ審査 | BIM drawing review / BIM data review | 2026 and 2029 permit review stages | permit review | "2029年春のBIMデータ審査" | R [ja-japan-r016](https://note.com/kensesu_ai/n/nee08ddde31f1), [ja-japan-r019](https://note.com/t_note_memo/n/n8903305b00fb) |
| 入出力基準 | in-out criteria | Official data input/output rules | exchange criteria | (list) | N [ja-japan.md](../research_raw/wave1/ja/ja-japan.md) |
| 壁芯 | wall core | Wall centre line (vs face) | centreline | "壁が芯でなく面基準" | R [ja-japan-r023](https://note.com/akram/n/n8a6e9c5602ca) |
| 1間 | one ken (about 1.82 m) | Traditional Japanese module in door and wall sizes | Japanese module | "1間引き違い戸が作れない" | R [ja-japan-r023](https://note.com/akram/n/n8a6e9c5602ca) |
| 野良データ | stray data | Uncontrolled, non-standard data deliveries | non-conforming data | "納品IFCのチェックが人力" | R [ja-japan-r003](https://zenn.dev/miyamiyaumya/articles/6714ef2c6e2c6c) |
| 軽量化 | make lighter | Reduce model weight | lightweighting | "ファイルを軽量化する方法" | N [ja-japan.md](../research_raw/wave1/ja/ja-japan.md); R [ja-japan-r030 (title)](../research_raw/wave1/ja/ja-japan.jsonl) |
| 干渉チェック | interference check | Clash detection | clash detection | "設備と構造のIFCで干渉チェックして" | S [ja-clash-s014](../research_raw/wave1/topics/t-clash-bcf.jsonl); R [ja-japan-r029](https://note.com/hip_sedum1639/n/n14c9af7dd03e) |
| 書き出し / 出す | write out / put out | Export. "IFCに出す" is the everyday form. | export | "IFCに出したら、半分なかった" | R [ja-japan-r015](https://note.com/toshio_nakamura/n/nc8db42ce3191); R [ja-japan-r001](https://zenn.dev/miyamiyaumya/articles/19a4247133dde6) |
| 読み込み / 取り込み / リンク | read in / take in / link | Import or link | import, link | "リンクとか開くとか何が違う" | S [ja-japan-s013](../research_raw/wave1/ja/ja-japan.jsonl); N |
| 属性 | attribute | Property in general | property | "Attributeしか書き出せないので" | R [ja-japan-r001](https://zenn.dev/miyamiyaumya/articles/19a4247133dde6) |
| 部材 | member | Element | element | "追加・削除・変更された部材" | S [ja-japan-s006](../research_raw/wave1/ja/ja-japan.jsonl) |
| 階 / 部屋 | floor / room | Storey; room | `IfcBuildingStorey`, `IfcSpace` | "階ごとの柱と梁の数を出して" | S [ja-aimcp-s013](../research_raw/wave1/ai/ai-mcp-usage.jsonl) |
| 意匠 / 構造 / 設備 | design / structure / equipment | Architecture, structure, MEP | disciplines | "意匠設計者のためのRevit-MCP解説" | R [ja-japan-r004](https://zenn.dev/yuichi_ai/articles/879de49ee8e1bb) |
| 積算 / 数量拾い | estimating / picking quantities | Quantity take-off | QTO | "積算用に、階ごとのRC壁・柱・梁のコンクリ体積を合計して" | S [ja-japan-s004](../research_raw/wave1/ja/ja-japan.jsonl); R [ja-japan-r024](https://note.com/bold_cobra9180/n/n4f52d62f230f) |
| 施工前検討会 | pre-construction review | Meeting where past defects are reviewed | review meeting | "施工前検討会で過去の不具合事例を参照する" | R [ja-data-r035](https://qiita.com/dnp-hiraoka/items/aa1d12e5784485542583) |
| 平面直角座標系 | plane rectangular coordinate system | Japanese national CRS with zones ("第9系") | CRS | "第9系でIFC出力したら原点からめちゃ遠い" | S [mul-coord-s015](../research_raw/wave1/topics/t-coordinates.jsonl) |
| 防火区画, 吊りボルト, 梁貫通スリーブ | fire compartment, hanger bolt, beam sleeve | Site-specific parts | none | "梁貫通スリーブが必要な箇所を一覧に" | S [ja-japan-s015](../research_raw/wave1/ja/ja-japan.jsonl), [ja-mep-s012](../research_raw/wave1/topics/t-mep.jsonl), [ja-openings-s017](../research_raw/wave1/topics/t-openings-penetrations.jsonl) |
| 線形 | line shape | Road alignment | `IfcAlignment` | "道路の線形をIFC4.3に変換して" | S [ja-infra-s014](../research_raw/wave1/topics/t-infra-ifc43.jsonl) |
| 文字化け | character change | Mojibake | mojibake | "プロパティの日本語が文字化けしてる" | S [enc-s003](../research_raw/wave1/topics/t-encoding.jsonl); N [t-encoding.md](../research_raw/wave1/topics/t-encoding.md) |
| ファミリ / タイプ / パラメータ / レベル | Revit katakana UI | Revit terms | family, type, parameter, level | (UI terms) | K [glossary](../08_glossary/glossary_multilingual.md) [V:23] |
| ファセット / バリデーション | facet / validation | IDS loanwords | facet, validation | (blog terms) | N [t-validation-ids.md](../research_raw/wave1/topics/t-validation-ids.md) |
| IFC検定 | IFC certification test | buildingSMART Japan's software certification | IFC certification | "IFC検定とは？" | R [ja-japan-r031](https://www.building-smart.or.jp/ifc/whatsifcverifi/) |
| 〜してみた / できなかった話 | I tried it / the story I could not do | Blog-title idioms with a failure framing | none | "作ろうとしてできなかった話" | R [ja-coord-r015](https://qiita.com/KengoTanaka-BIM/items/6cec74e04bf581b21cf5) |
| 〜と思います / かもしれません | I think / maybe | Hedges, even in technical text | none | (hedges) | N [t-geometry.md](../research_raw/wave1/topics/t-geometry.md) |
| 出して / 調べて / 教えて | give / check / tell me | Casual imperatives to an AI | none | "このIFC、...数えて、元のRevitカテゴリ別に集計して" | S [ja-japan-s001](../research_raw/wave1/ja/ja-japan.jsonl) |

### Korean (KO)

Casual Korean in this corpus is entirely **S** (8 real records, all institutional). Treat the register as an assumption stated in the cell report ("banmal-like requests", "ㅠㅠ").

| Slang / jargon | Literal | Meaning | Standard term | Example fragment | Evidence and source |
|---|---|---|---|---|---|
| 레빗 | "rebit" | Revit in Hangul | Revit | "레빗 카테고리별로 나눠줘" | S [ko-korea-s001](../research_raw/wave1/ko/ko-korea.jsonl); N [ko-korea.md](../research_raw/wave1/ko/ko-korea.md) |
| 아키캐드 | "akikaedeu" | Archicad in Hangul | Archicad | "아키캐드 30, 공식 발표회 초대" | R [ko-korea-r006](https://www.buildingsmart.or.kr/Home/NewsDetail?board=1&id=3451) |
| 프록시 / proxy | proxy | Same generic class | `IfcBuildingElementProxy` | "proxy로 나온 것 중 이름에 '기둥' 들어간거" | S [ko-korea-s007](../research_raw/wave1/ko/ko-korea.jsonl) |
| 부재 / 객체 | member / object | Element | element | "어제 올린 ifc랑 오늘 거 비교해서 추가/삭제/변경된 부재" | S [ko-korea-s009](../research_raw/wave1/ko/ko-korea.jsonl) |
| 물량 | quantity | Quantities for estimating | QTO | "층별 콘크리트 물량 m3로 정리해줘" | S [ko-korea-s006](../research_raw/wave1/ko/ko-korea.jsonl) |
| 간섭검토 / 오탐 | interference review / false positive | Clash review; false hit | clash detection | "ifc 간섭검토 할때 오탐이 너무 많은데" | S [ko-clash-s015](../research_raw/wave1/topics/t-clash-bcf.jsonl) |
| 공유 매개변수 | shared parameter | Revit shared parameter | shared parameter | "공유 매개변수가 속성에 하나도 안 보여" | S [ko-korea-s002](../research_raw/wave1/ko/ko-korea.jsonl); K [glossary](../08_glossary/glossary_multilingual.md) [V:24] |
| 층 / 레벨 / 실 | floor / level / room | Storey and room words | `IfcBuildingStorey`, `IfcSpace` | "층 목록이랑 레벨 높이 뽑아줘" | S [ko-korea-s004](../research_raw/wave1/ko/ko-korea.jsonl) |
| 발주처 / 조달청 | ordering agency / Public Procurement Service | Client and the public procurement body whose BIM guideline is cited | client | "조달청 시설사업 BIM 적용 지침서 V2.0" | R [ko-korea-r004](https://www.buildingsmart.or.kr/Data/Main/시설사업%20BIM%20적용%20기본지침서%20v2.0-S.pdf); S [ko-korea-s003](../research_raw/wave1/ko/ko-korea.jsonl) |
| 공정표 / 4D 시뮬 | process table / 4D sim | Schedule linked to the model | 4D scheduling | "공정표랑 연결 안 된 부재" | S [ko-s014](../research_raw/wave1/ko/ko-korea.jsonl) |
| 뽑아줘 / 봐줘 / 줘 | pull out / look / give | Casual banmal requests | none | "덕트 중에 시스템 지정 안된거 있나 봐줘" | S [ko-korea-s010](../research_raw/wave1/ko/ko-korea.jsonl); N |
| 한글이 깨지고 | Hangul breaks | Mojibake | encoding problem | "한글이 깨지고 너무 느려요 ㅠㅠ" | S [ko-korea-s014](../research_raw/wave1/ko/ko-korea.jsonl) |
| 용량 | capacity | File size | file size | "용량은 200MB" | S [ko-korea-s005](../research_raw/wave1/ko/ko-korea.jsonl) |

---

## 10. Dutch, Norwegian, and the small languages

### Dutch (NL)

Dutch uses English tool words as verbs ("mappen", "toetsen") and many official abbreviations. Real material is GitHub issues of national standards and the digigo.nu guidance.

| Slang / jargon | Literal | Meaning | Standard term | Example fragment | Evidence and source |
|---|---|---|---|---|---|
| nulpunt | zero point | Model origin | origin | "modellen niet op hetzelfde nulpunt liggen" | R [nl-dutch-r008](https://github.com/OpenAEC-Foundation/OpenAEC-BIM-validator/issues/21) |
| bouwlaag | building layer | Storey | `IfcBuildingStorey` | "Naamgeving bouwlagen gelijk in alle aspectmodellen" | R [nl-dutch-r018](https://www.digigo.nu/ilsen-en-richtlijnen/bim-basis-ils/3-3-bouwlaagindeling-en-naamgeving) |
| aspectmodel | aspect model | Discipline model | discipline model | (same) | R [nl-dutch-r018](https://www.digigo.nu/ilsen-en-richtlijnen/bim-basis-ils/3-3-bouwlaagindeling-en-naamgeving) |
| ruimte / ruimten | space | Room (Revit "ruimte") | `IfcSpace` | "4.1 Ruimten" | R [nl-dutch-r021](https://www.digigo.nu/ilsen-en-richtlijnen/bim-basis-ils/4-1-ruimten) |
| kozijn | window/door frame | Window or door unit | `IfcWindow` | "mijn kozijn familie komt als proxy in het ifc" | S [nl-dutch-s011](../research_raw/wave1/nl/nl-dutch.jsonl) |
| peil, stramien | datum level, grid | Height datum, structural grid | level, grid | (jargon list) | N [nl-dutch.md](../research_raw/wave1/nl/nl-dutch.md) |
| NL-SfB, NLCS, NAA.K.T., GWSW, IMBOR | Dutch classifications | Building, civil, material and sewer-network naming systems | classification | "NL-SfB code 27 is daarom niet juist" | R [nl-dutch-r001](https://github.com/Aedes-datastandaarden/ILS-woco/issues/2), [nl-dutch-r023](https://www.digigo.nu/ilsen-en-richtlijnen/bim-basis-ils/praktijk/1-naa-k-t-eenduidige-materiaalbenaming) |
| ILS, RVB, BIM Basis ILS | delivery specification, requirements document | Dutch EIR-like documents | EIR | "kloppen de bouwlagen met de ILS?" | S [nl-dutch-s004](../research_raw/wave1/nl/nl-dutch.jsonl); R [nl-dutch-r017](https://www.digigo.nu/ilsen-en-richtlijnen/bim-basis-ils/3-4-correct-gebruik-entiteiten) |
| BVO, GO, VG | area types | Gross floor area, usable area, floor area | area types | (list) | N [nl-dutch.md](../research_raw/wave1/nl/nl-dutch.md) |
| federatie, toetsen, mappen | federation, test, map | Anglicised verbs | check, map | "wil ze goed mappen voor de export" | S [nl-dutch-s001](../research_raw/wave1/nl/nl-dutch.jsonl) |
| oid | "etc." | Casual "or the like" | none | "Revit template oid?" | R [nl-dutch-r013](https://github.com/nl-digigo/NLCS/issues/238) |
| Smart Views | BIMcollab feature | Colour-by-property views | colour filter | "kleuren op eigenschap" | R [nl-dutch-r012](https://github.com/OpenAEC-Foundation/OpenAEC-BIM-validator/issues/17) |

### Norwegian (NO)

Low confidence: institutional text and synthetic prompts only.

| Slang / jargon | Literal | Meaning | Standard term | Example fragment | Evidence and source |
|---|---|---|---|---|---|
| RIB / RIV / ARK | discipline codes | Structural, HVAC, architecture | disciplines | "kollisjonskontroll RIV mot RIB" | S [no-norway-s010](../research_raw/wave1/no/no-norway.jsonl) |
| MMI | model maturity index | Everyday maturity code (MMI 300, 400 ...) | maturity level | "mangler MMI i modellen" | R [no-norway-r007](https://www.mmi-veilederen.no/); S [no-norway-s001](../research_raw/wave1/no/no-norway.jsonl) |
| bestiller / leverandør | orderer / supplier | Client and delivering party | client, supplier | (list) | R [no-norway-r002](https://www.buildingsmart.no/pofin.html) |
| POFIN | national framework | Norwegian BIM framework | BIM framework | "hva er POFIN" | R [no-norway-r002](https://www.buildingsmart.no/pofin.html) |
| FDV, BTA / NTA, TEK17, NS 3451, NS 8360 | handover info, areas, building code, standards | Handover data, gross/net areas, regulations | handover, areas, code | "har alle tekniske komponenter FDV-info og NS 3451-kode" | S [no-norway-s006](../research_raw/wave1/no/no-norway.jsonl); R [no-norway-r012](https://www.buildingsmart.no/standarder/kort-forklart.html) |
| kum, armering, romliste, etasje | manhole, rebar, room list, floor | Local building words | manhole etc. | "romliste med romnr, navn og BTA/NTA" | R [no-norway-r004](https://www.buildingsmart.no/standarder/publikasjoner-og-veiledninger.html); S [no-norway-s013](../research_raw/wave1/no/no-norway.jsonl) |
| origo, EUREF89 NTM | origin; coordinate system | Coordinates | CRS | "EUREF89 NTM sone?" | S [no-norway-s005](../research_raw/wave1/no/no-norway.jsonl) |
| æøå blir rare tegn | letters turn odd | Encoding failure | mojibake | "æøå blir rare tegn i navnene" | S [no-norway-s012](../research_raw/wave1/no/no-norway.jsonl) |

### Arabic (AR), Turkish (TR), Greek (EL)

One synthetic prompt each. Use only for encoding tests, not as vocabulary evidence.

| Language | Expression | Meaning | Evidence |
|---|---|---|---|
| AR | أسماء الغرف بالعربي تظهر علامات استفهام بعد تصدير IFC | "room names in Arabic show question marks after exporting IFC": تصدير = export, الغرف = rooms, بالعربي = colloquial "in Arabic" | S [enc-s005](../research_raw/wave1/topics/t-encoding.jsonl) |
| TR | modeldeki isimlerde ş ğ ı İ gibi türkçe karakter geçen elemanları listele | "list elements whose names contain Turkish characters" | S [enc-s004](../research_raw/wave1/topics/t-encoding.jsonl), [enc-s015](../research_raw/wave1/topics/t-encoding.jsonl) |
| EL | δείξε μου τα ονόματα των χώρων στα ελληνικά | "show me the space names in Greek" | S [enc-s006](../research_raw/wave1/topics/t-encoding.jsonl) |

Arabic glossary terms (فئات أسس الصناعة for IFC, كائن النوع for type object) are in [glossary_multilingual.md](../08_glossary/glossary_multilingual.md); that file marks Arabic as the weakest, unverified column.

### Slovak, Vietnamese, Czech, Danish

| Language | Expression | Meaning | Evidence |
|---|---|---|---|
| SK | "Oddiaľ pôdorys o 15 percent." | "Zoom out the floor plan by 15 percent": short imperative to an AI viewer tool | R [sk-aimcp-r016](https://github.com/Menezeris/AIMviewer/issues/65) |
| VI | "Thống kê cửa, phòng; khối lượng tường, sàn" | "Statistics of doors, rooms; quantities of walls, floors" (README example) | R [vi-aimcp-r042](https://github.com/andyluu98/vn-revit-mcp) |
| CS | parameter names OBJEM / PLOCHA (volume / area) inside English posts | Czech property names leak into Revit exports | N [t-psets-params.md](../research_raw/wave1/topics/t-psets-params.md); R [en-gh-encoding-r021](https://github.com/ThatOpen/engine_web-ifc/issues/440) |
| DA | "I use UTF-8 because of AE O AA" (Danish letters) | Danish æøå encoding report | R [en-gh-encoding-r022](https://github.com/ThatOpen/engine_web-ifc/issues/358) |

### Polish (PL): no data

No Polish record exists in the corpus, so nothing below is evidence. These are general background terms (**K, unverified**) for a tester who must generate Polish prompts; have a Polish speaker check them first.

| Term | Literal | Meaning |
|---|---|---|
| kolizje | collisions | clashes |
| kondygnacja | storey | `IfcBuildingStorey` |
| przedmiar / obmiar | take-off / measurement | quantities |
| rodzina, parametr udostępniony, poziom | family, shared parameter, level | Revit UI words (as commonly localised) |
| pomieszczenie | room | `IfcSpace` |
| współrzędne, punkt bazowy projektu | coordinates, project base point | location problems |

---

## 11. Revit-isms and how they map to IFC (language-independent)

People who work in Revit describe problems in Revit words, while the IFC file contains IFC concepts. A request that says "my family is missing" cannot be answered by looking for a "family" in the file. Details: [ifc_export_reference.md](../03_software/revit/ifc_export_reference.md), [ifc_import_link_reference.md](../03_software/revit/ifc_import_link_reference.md), [03_entities_cheat_sheet.md](../01_ifc_basics/03_entities_cheat_sheet.md), [04_spatial_structure_and_relationships.md](../01_ifc_basics/04_spatial_structure_and_relationships.md).

| Revit word (what the person says) | Plain meaning | IFC concept | What goes wrong in practice | Evidence |
|---|---|---|---|---|
| family | A reusable content definition (a "door family" holds many sizes); also its class (system / loadable / in-place) | Not stored as a family. The shared part is the type object (`IfcDoorType` etc.). The Revit family name often ends up inside `Name` as "Family:Type:ElementId". | "Export my families to IFC" has no meaning; the user wants types and properties. | R [zh-csdn-dev-r011](https://www.cnblogs.com/herd/p/14908387.html) (name like 楼板:JG-b-200-0现浇:394165); K [03_entities_cheat_sheet](../01_ifc_basics/03_entities_cheat_sheet.md) |
| type / family type / Typ / типоразмер | A named variant with fixed values (900 x 2100) | `IfcXxxType` linked by `IfcRelDefinesByType` | Type parameters live on the type; a query that reads only the occurrence misses them. | K [04_spatial_structure](../01_ifc_basics/04_spatial_structure_and_relationships.md) |
| instance / occurrence | One placed element | The `IfcWall` occurrence | "Instance" is also an IFC word (a line in the file); keep the context clear. | K |
| category | Revit's top group (Walls, Doors, Generic Models) | Drives the **default** IFC class through the mapping table; not identical to a class | Habr: the category-to-class table "lies"; the class comes from export settings. | R [ru-habr-dev-r001](https://habr.com/ru/articles/1089018/) |
| Generic Model | Catch-all category | Exported as `IfcBuildingElementProxy` unless overridden | The classic source of "everything is proxy". | K [ifc_export_reference](../03_software/revit/ifc_export_reference.md); S [ru-eng-s010](../research_raw/wave1/roles/p-engineers.jsonl) |
| parameter | A named value on an element | An `IfcProperty` in a Pset, or an IFC attribute | "My parameter does not show in IFC": it needs a mapping, a shared parameter or an export option. | R [en-ghrevitifc-r020](https://github.com/Autodesk/revit-ifc/issues/38) |
| shared parameter | A parameter defined in a shared file with a GUID | Becomes a property only if the export is told to write it (user-defined Pset file or parameter mapping) | Typical complaint in all languages; "hidden shared parameters are not exported". | R [en-ghrevitifc-r020](https://github.com/Autodesk/revit-ifc/issues/38); S [fr-francophone-s013](../research_raw/wave1/fr/fr-francophone.jsonl), [de-dach-s005](../research_raw/wave1/de/de-dach.jsonl) |
| project parameter | Parameter bound to categories in one project | Same as above | Not available inside the family editor. | K [glossary](../08_glossary/glossary_multilingual.md) |
| Export to IFC As / IfcExportAs | Per-element or per-type override of the class | The `IfcClass.PredefinedType` of the occurrence | Two places can disagree (category mapping vs override); which wins confuses users. | S [zh-proxy-s014](../research_raw/wave1/topics/t-proxy-mapping.jsonl); K |
| level | A horizontal datum plane | Usually `IfcBuildingStorey` | Not every level becomes a storey in every setup; elements may land on the wrong storey. | R [en-blogs-linkedin-r016](https://bim-me-up.com/ifcbuildingstorey/); K [glossary Q1](../08_glossary/glossary_multilingual.md) |
| room / space / area | Revit Room (architectural), Space (MEP), Area (area plan) | `IfcSpace` | Areas can export as `IfcSpace` with offsets; on import Link IFC gives Generic Models, not Rooms. | R [en-autodesk-revit-import-r018](https://github.com/Autodesk/revit-ifc/issues/15); N [t-spaces-areas.md](../research_raw/wave1/topics/t-spaces-areas.md) |
| Revit Link / link | A linked model (RVT or IFC) in the project | No link concept in IFC | "Link vs Open" decides whether you get DirectShape or native elements. | R [en-autodesk-revit-import-r003](https://github.com/Autodesk/revit-ifc/issues/223) |
| DirectShape | Revit's "dumb geometry" element | Not an IFC term; what a linked IFC becomes | "Dumb solids", "тела", "ダムソリッド"-style complaints. | K [ifc_import_link_reference](../03_software/revit/ifc_import_link_reference.md); R [ru-dwg-other-r009](https://forum.dwg.ru/showthread.php?t=166052) |
| in-place family / model in place | One-off geometry built inside the project | Often exported as a proxy or the mapped class | Cannot be edited back from IFC either. | R [en-autodesk-revit-import-r003](https://github.com/Autodesk/revit-ifc/issues/223) |
| workset | An ownership slice of a shared model | **No IFC counterpart**; do not equate with `IfcPresentationLayerAssignment` | Users ask "export without these worksets"; that is an export filter, not an IFC feature. | K [07_materials](../01_ifc_basics/07_materials_classification_types_styles.md); S [ru-habr-dev-s016](../research_raw/wave1/ru/ru-habr-dev.jsonl) |
| project base point / survey point / internal origin / shared coordinates / true north | Revit's reference points | Site placement, `IfcMapConversion`, `IfcProjectedCRS` | "Model is kilometres away": mismatch of which point the export used. | K [ifc_export_reference](../03_software/revit/ifc_export_reference.md); S [zh-lightweight-review-s001](../research_raw/wave1/zh/zh-lightweight-review.jsonl) |
| ElementId / UniqueId / IfcGUID | Integer id; 36-character id; 22-character IFC id | `IfcRoot.GlobalId` (22 characters) | Students ask for a table "Revit ID to IFC GUID". | R [ja-coord-r014](https://qiita.com/Takashi_Kasuya/items/97899d15e7ec0186eecf); S [p-student-s017](../research_raw/wave1/roles/p-student.jsonl) |
| Mark / Type Mark / Tag | User-typed id text | Lands in properties depending on mapping | "Which doors have no mark" is common; the answer depends on the export mapping. | S [ru-aimcp-s010](../research_raw/wave1/ai/ai-mcp-usage.jsonl) |
| phase | Construction stage (existing / new / demolished) | No native attribute; written as properties if configured | "Revit Phasen nach IFC exportieren". | R [en-blogs-linkedin-r012](https://bim-me-up.com/revit-phasen-nach-ifc-exportieren/) |
| host | The element that holds another (a wall hosts a door) | `IfcRelFillsElement` / `IfcRelVoidsElement` | "Doors not hosted in a wall". | S [en-uk-anz-india-s015](../research_raw/wave1/en/en-uk-anz-india.jsonl) |
| curtain wall / panel / mullion | Glazed facade system | `IfcCurtainWall`, `IfcPlate`, `IfcMember` | Missing mullions are a recurrent complaint. | R [en-autodesk-revit-export-r023](https://forums.autodesk.com/t5/revit-architecture-forum/quot-ghost-quot-mullions-in-ifc-export/td-p/13056918) |
| room bounding / 2nd level boundaries | How rooms see walls | `IfcRelSpaceBoundary` (1st / 2nd level) | Energy-model users care. | N [t-spaces-areas.md](../research_raw/wave1/topics/t-spaces-areas.md) |
| view / sheet / schedule | Drawings and tables | Not IFC content (a view may filter what is exported) | "Make a sheet per level" is a Revit task, not an IFC task. | S [en-revit-auto-s002](../research_raw/wave1/ai/ai-revit-tasks.jsonl) |

Revit UI words in ten languages (family, type, shared parameter, level, workset) come from vendor help pages and are tabulated in the [glossary](../08_glossary/glossary_multilingual.md). Check the glossary caveat there: "workset" has five translations, so a test that matches one UI string fails on another locale.

---

## 12. False friends and ambiguity traps

A good MCP answer resolves these; a good test prompt can deliberately include them.

| Trap | Where it appears | Why it matters |
|---|---|---|
| "export" used for any conversion | EN: "export dwg to ifc4" (R); RU: "выгрузить" | The tool must decide whether the user means save-as, convert or export from Revit. |
| "IFC4" meaning Reference View or Design Transfer View, or even 4.3 | EN, DE ("AG fordert IFC4 Reference View") | N [t-versions-mvd.md](../research_raw/wave1/topics/t-versions-mvd.md): users say "IFC4" for RV or DTV interchangeably. |
| "level" vs storey vs "floor" | all languages | Revit level may not be a storey; "floor" is also the slab (Revit Floors = `IfcSlab`). |
| "type" vs "типоразмер" vs "tipo" | RU/ES | Russian Revit "типоразмер" is a size variant; the IFC type is a different layer. |
| "Eigenschaft" vs "Merkmal"; 属性 for both | DE, ZH | Attribute vs property confusion. |
| "zone" | RU (зона), Archicad (zone), IFC (`IfcZone`) | Can mean room, area or a real IFC zone. |
| "layer" | CAD layers (`IfcPresentationLayerAssignment`), material layers, Revit "layers" export | Three different things. |
| "model" | FR maquette, EN model | One IFC file, a federation, or the authoring file. |
| "space" | Revit Space (MEP) vs `IfcSpace` vs "space" for room | Rooms become `IfcSpace`; Revit Spaces too. |
| "link" | Revit Link, IFC link, URL link | Link IFC vs Open IFC. |
| "proxy" | many | Sometimes the class, sometimes a placeholder family, sometimes a network proxy. |
| "units" | all | File length unit (mm vs m) vs Revit display units; decimal comma vs point (IT: "decimali con il punto diventano testo"). |
| "BCF" vs "BCF-API" vs "clash report" | all | People say BCF for any issue list. |

---

## 13. Using this dictionary in synthetic prompts

1. **Pick the language and the persona first, then the register.** A Russian estimator says "ВОР", a Norwegian coordinator says "RIV mot RIB", a Japanese architect says "確認申請". Do not mix registers (a student does not say "Zugriffsrechte der Fachmodelle").
2. **Use at most two or three slang items in one prompt.** Real messages usually contain one ("проксики", "navis", "gaines"). A prompt stuffed with every nickname reads as invented.
3. **Keep IFC class names exact and Latin** (IfcWall, IfcBuildingElementProxy, IfcMapConversion) even in Chinese, Korean or Arabic sentences. People write them unchanged.
4. **Match region to synonym.** Spain "planta/hormigón/pilar/conductos"; Rioplatense "creá/contame/ambientes"; Peru "metrados"; Brazil "pavimento/compatibilização/quantitativo"; Mainland ZH "导出/导入", Taiwan "匯出/匯入".
5. **Leave context out on purpose.** Real posts omit the IFC schema, the exporter version and the file (see the "partial context" rule in the [style guide](style_guide.md)). A test where the server must ask or infer is realistic.
6. **Label confidence in the test case.** If a row is **S** or **K**, the test case should say "plausible phrasing, not observed". Do not describe it as "how Russian users speak".
7. **Spell-variant noise** belongs in [name_variants_and_misspellings.md](name_variants_and_misspellings.md): follow its rates and rules.

## Gaps

- No real casual chat to an AI assistant in any language: the corpus is forums, issue trackers, blogs and vendor pages. All "typed to the AI" phrasing is synthetic.
- Russian spoken forms (ифс, проксики, нависворкс) are named in the cell reports but appear in no real record text.
- French, Portuguese, Korean, Norwegian, Arabic, Turkish, Greek and Polish casual vocabulary is unverified or absent.
- `wave2` research was not available; rerun the checks when it is.
