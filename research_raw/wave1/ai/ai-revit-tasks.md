# What tasks people want to automate in Revit (wishes that map to Revit MCP tests)
Cell: ai-revit-tasks · Languages: English (dominant), Chinese (Traditional, Taiwan), Russian (1 weak record); Spanish/Portuguese/German only as synthetic · Collected: 2026-11-06 · Records: 38 real / 17 synthetic · Communities covered: forum.dynamobim.com, discourse.pyrevitlabs.io, GitHub issues of Revit MCP projects, one dwg.ru thread

## Top themes (ranked by frequency)
- Create or arrange views and sheets in bulk: viewports, crop regions per apartment or room, elevations on sheets, view titles.
- Read or write parameters at scale: copy type to instance, fill shared parameters, Excel round-trip, find blanks, type vs instance mixups.
- Room and area work: area plans and boundaries, room styles, abbreviations, areas pushed into schedules or view titles.
- Model QA/QC reports: duplicate or missing rooms, untagged doors, duplicate instances, empty parameters, exported to Excel.
- Cleanup: unused or "zombie" parameters, filters, fonts, links, worksets, pre-publish routines.
- Quantities and schedules: counts per floor (data ports, devices), area totals, family sizes from tables.
- MEP: fill cable trays, route around obstacles, sleeves and openings at penetrations, clash scans.
- Auto-tagging and dimensioning with layout logic.
- Numbering elements along a path (parking, rooms).
- Code-style checks: egress distance, slopes steeper than a ratio.
- Model comparison between versions or between independently built models.
- AI/MCP usage itself: connecting agents (Claude, Gemini, local Ollama) to Revit, arbitrary code execution tool failures, cost and trust concerns.
- CAD to Revit conversion (DWG layers to walls, beams, columns) and IFC to Revit wall recovery.

## What people want (the goals behind the questions)
- Replace repetitive clicking: 40+ views duplicated, renamed and given templates in one prompt is the typical success story.
- Get a trustworthy report before acting: read-only scans first, then confirmed edits (the Taiwan MCP project insists on read-only scan, review flags, and no invented default values).
- Hand a vague office rule to a tool ("area tags into view titles", "fonts to Roboto") without learning node graphs.
- Verify what AI built: compare by location instead of ElementId, section-box issue views.
- Cheap or local AI: several users ask how to run Mistral, Llama or Ollama against Revit tools.
- Many askers have already tried ChatGPT or Gemini and got empty lists, null values or broken graphs, so expect follow-ups on fixing AI output.

## How people write here
- English forum posts: first-person goal description, node names as jargon (Element.SetParameterByName, lacing, code block), often no Revit version, screenshots or attachments instead of context. Example fragments: "works for a few instances only"; "I am new to Dynamo"; "returns null"; "Need help with...".
- Titles often carry the whole request, sometimes with misspellings ("appartment", "boudnary", "packges").
- Typical length: 3-8 sentences; polite closers rare; thanks appear after solution.
- Users cite failed AI attempts ("ChatGPT and Gemini didn't help").
- Taiwan Chinese GitHub issues: structured (問題說明 / 建議修改 / 驗證結果), mm units, terms like 翻模 (convert CAD to Revit model), 開孔 (opening), 套管 (sleeve), 穿樑 (through beam), 圖塊 (CAD block).
- The Russian record is a short family-parameter question on dwg.ru; text was recovered only as a gist, so Russian slang is not captured. Synthetic Russian prompts use short imperative style ("глянь", "до экспорта надо").
- Missing context is the norm: no category, no level name, no version, no desired naming pattern.

## Local ecosystem
- Autodesk-staffed Dynamo forum moderators actively steer people to schedules, tags and packages: https://forum.dynamobim.com
- Dynamo packages named in threads: Clockwork, Pickles, VASA, Data-Shapes, Monocle, Dynamo Multiplayer.
- pyRevit (open source, now with a built-in MCP, pyRevit 7): https://discourse.pyrevitlabs.io ; tools like pychilizer, Ideate Apps.
- Revit MCP projects: https://github.com/mcp-servers-for-revit/revit-mcp ; https://github.com/mcp-servers-for-revit/mcp-servers-for-revit ; https://github.com/shuotao/REVIT_MCP_study (Taiwan, Chinese issues, 200+ tools) ; https://github.com/oakplank/RevitMCP ; https://github.com/bimwright/rvt-mcp ; https://github.com/HorizunGroup/horizun-revit-mcp ; https://github.com/LuDattilo/revit-mcp-server ; https://github.com/Demolinator/revit-mcp-server
- Autodesk Assistant with built-in MCP for Dynamo and Revit (discussed in Dynamo forum AI category).
- Russian: forum.dwg.ru Revit subforum https://forum.dwg.ru/forumdisplay.php?f=58

## Notable sources
- https://forum.dynamobim.com/t/would-you-use-an-mcp-based-ai-assistant-for-dynamo/114952 (AI opinions)
- https://forum.dynamobim.com/t/extract-areas-from-area-plans/115283
- https://forum.dynamobim.com/t/automate-the-creation-of-view-plans-of-each-appartment-with-the-cropzone-aligning-exactly-on-the-outer-boundary-of-the-boudnary-walls-of-each-appartment/115202
- https://forum.dynamobim.com/t/automatic-tagging/114838
- https://forum.dynamobim.com/t/deleting-duplicate-instances-in-revit/115296
- https://forum.dynamobim.com/t/updating-structural-foundation-size-parameters-via-excel-input/115236
- https://forum.dynamobim.com/t/issue-with-element-numbering-script-in-dynamo-revit/105235
- https://forum.dynamobim.com/t/help-with-automated-quality-check-script-getting-empty-list-and-blank-excel/112252
- https://forum.dynamobim.com/t/extracting-telecom-data-port-quantities-from-bim-model-using-dynamo/114169
- https://forum.dynamobim.com/t/set-room-style-based-on-room-name-input/115142
- https://forum.dynamobim.com/t/automatically-fill-cable-tray-with-cables/115192
- https://forum.dynamobim.com/t/delete-parameters-with-blank-value/115164
- https://forum.dynamobim.com/t/automating-wall-extraction-from-ifc/115089
- https://forum.dynamobim.com/t/exit-access-travel-distance/115179
- https://forum.dynamobim.com/t/fonts-update-all-project-fonts-to-a-different-font-attempt-at-aggregating-old-posts/113268
- https://forum.dynamobim.com/t/deleting-zombie-parameters/112603
- https://forum.dynamobim.com/t/unload-revit-linked-with-its-worksets-closed/115193
- https://forum.dynamobim.com/t/automating-filter-creation/108901
- https://discourse.pyrevitlabs.io/t/connecting-agent-to-pyrevit-mcp-newbie/10627
- https://discourse.pyrevitlabs.io/t/placing-elevations-on-sheet-one-elevation-behaves-differently/1467
- https://discourse.pyrevitlabs.io/t/revit-model-compare-check-what-the-ai-actually-built/10681
- https://github.com/shuotao/REVIT_MCP_study/issues/99
- https://github.com/shuotao/REVIT_MCP_study/issues/150
- https://github.com/shuotao/REVIT_MCP_study/issues/144
- https://github.com/mcp-servers-for-revit/revit-mcp/issues/30
- https://github.com/mcp-servers-for-revit/revit-mcp/issues/26
- https://github.com/mcp-servers-for-revit/mcp-servers-for-revit/issues/30

## Gaps
- The WebSearch budget was exhausted before any search ran (all four attempted searches were refused), so discovery relied on forum category/JSON listings, direct fetches and GitHub CLI. No search with domain filters was possible.
- Russian, Spanish, Portuguese and German communities are essentially uncovered: dwg.ru pages come back garbled (cp1251) and one thread only yielded a gist; a direct curl attempt to read it with re-encoding was blocked by the permission layer and not retried. Habr search is JS-rendered. Telegram t.me/s/revitapi returned no posts.
- Chinese: only Taiwan GitHub issues found; cnblogs, 51cto searches returned 404/empty; Bilibili, Zhihu, CSDN not reached.
- Autodesk forums (Revit API, Revit Ideas) returned 403; Reddit not reachable without search.
- Five real records are title-only (evidence "snippet"); the dwg.ru record has an unreliable paraphrase.
- Spanish/Portuguese/German/Russian/Chinese synthetic prompts are not backed by real posts from those languages.
- No suspicious or pirated sites were encountered.
