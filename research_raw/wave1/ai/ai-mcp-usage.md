# What people ask AI assistants and MCP servers about IFC/BIM (real prompts, demos, issues)
Cell: ai-mcp-usage · Languages: English, Chinese (zh-CN/zh-TW), Japanese, Spanish, Vietnamese, Slovak (Russian only synthetic) · Collected: 2026-11-06 · Records: 45 real / 17 synthetic · Communities covered: GitHub issues and READMEs of Revit, Archicad, Bonsai/IfcOpenShell and IFC MCP servers; OSArch and buildingSMART forum snippets

Note: the WebSearch budget was exhausted before the first search ran. All research was done through the GitHub CLI (repo and issue search, issue bodies, READMEs) and direct WebFetch of repo pages and two forums. Blogs, LinkedIn, YouTube, Zhihu, Habr and Reddit were not reached.

## Top themes (ranked by frequency)
- Connection and setup failures: Claude or Cursor "cannot connect to Revit", ports 8080/8964, plugin not loading, "Method not found" (many issues)
- Version support: Revit 2019-2022 vs 2025-2027, .NET Framework 4.8 vs .NET 8, "is Revit 2027 supported?"
- Write tools that report success but do the wrong thing: wall on the wrong level, door unhosted at the origin, duplicate elements on retry
- Hard categories with no native tool: stairs, families, MEP system joins, curtain walls, falling back on send_code_to_revit
- Read and query tasks on IFC: counts of walls/doors/windows, spatial structure, properties, spaces and room areas
- Quantity takeoffs: wall areas, concrete volume, duct length/area/weight, CSV/Excel/BC3 export
- Validation and QA: missing names/marks/classifications, door width rules, model warnings, pre-issue checks, BCF export
- Trust: models that claim "done" without persisted state, fabricated IFC that fails validation, the demand for UNKNOWN instead of guesses
- Context and cost: tool catalogs of 200+ tools bloat the context; split toolsets
- Human-in-the-loop: preview, approve, apply, read back, undo (undo is limited)
- Vision and viewer: screenshot of the current view for multimodal models, camera control, opening a viewer
- CAD to BIM: turning DWG layers into walls, beams, columns
- Non-Claude clients: Cursor, LM Studio, Mistral/Llama, DeepSeek, ChatGPT desktop, OpenWebUI
- Local-language use: Chinese issue titles, Spanish voseo prompts, Japanese law-aware tooling

## What people want (the goals behind the questions)
- Ask in plain language instead of opening a viewer or writing IfcOpenShell code (counts, "largest window", "total wall area")
- Generate and edit geometry from text ("10 m wall", "rectangle 5x4 with 3 m walls", "storeys at 0 and 3.5 m")
- Automate repetitive QA: marks, room numbers, warnings, door widths, missing classification
- Get reproducible numbers, not estimates; explicit PASS/FAIL/UNKNOWN
- Produce deliverables: CSV, Excel, BCF, BC3 budget, floor-plan PNG, GLB
- Run it safely: local data, read-only mode, approval before writes, rollback
- Connect any LLM (local models, cheaper clients) to Revit/IFC
- Make the model "see" the drawing and place elements by visual position

## How people write here
- GitHub issues in English are bug-template style: environment, repro steps, expected vs actual, pasted traceback. Beginners write one-liners ("How Can i connect mistral or Llama with the revit MCP") or very polite requests ("Could you please provide a simple tutorial?").
- Users often quote the assistant's reply back: "I'll help you find all the pipes... Method not found".
- Chinese issues use short titles and local slang: "二开" for secondary development (plugin work), "翻模" for rebuilding a model from drawings, "在启动时产生报错". Traditional-Chinese (Taiwan) maintainers write long structured proposals with tables and tool names in code font.
- Spanish prompts use voseo and imperative: "Creá cuatro muros de 3 m", "Ejecuta la corrida 5 HVAC", "dame los ductos".
- Japanese README style is formal and law-aware (建築基準法, 社内標準).
- Slovak example: short imperatives "Oddiaľ pôdorys o 15 percent."
- Code-switching is heavy: tool names (`create_wall`, `send_code_to_revit`), class names (IfcBuildingElementProxy), units in mm, English error strings inside Chinese text.
- Context given: Revit year, Windows, client name; omitted: IFC schema version, file size, which MVD.
- Tone: frustrated when setup fails ("tried apparently everything"), curious in demos, skeptical in engineering proposals ("answered a confident done on 8 of 15").
- Fragments: "list all pipes in the revit model"; "dimension every wall on this view"; "put the sofa here, by the window"; "Creá cuatro muros de 3 m".

## Local ecosystem
- IfcOpenShell / Bonsai: https://github.com/IfcOpenShell/IfcOpenShell (maintainers advise validating LLM-written IFC with https://validate.buildingsmart.org/)
- buildingSMART forum and bSDD: https://forums.buildingsmart.org/
- OSArch community (open-source AEC): https://community.osarch.org/
- Revit MCP family: https://github.com/mcp-servers-for-revit/mcp-servers-for-revit, https://github.com/bimwright/rvt-mcp, https://github.com/LuDattilo/revit-mcp-server, https://github.com/HorizunGroup/horizun-revit-mcp, https://github.com/Demolinator/revit-mcp-server, https://github.com/shuotao/REVIT_MCP_study (Taiwan), https://github.com/okuno-dsi/revit-mcp-toolkit (Japan), https://github.com/andyluu98/vn-revit-mcp (Vietnam)
- Autodesk APS sample bundle: https://github.com/autodesk-platform-services/aps-sample-revit-mcp-tools-bundle
- IFC / Bonsai MCP: https://github.com/smartaec/ifcMCP (Tsinghua), https://github.com/JotaDeRodriguez/Bonsai_mcp, https://github.com/Show2Instruct/ifc-bonsai-mcp, https://github.com/flinker-app/ifc-mcp, https://github.com/Daviidro/ifcopenshell-mcp, https://github.com/zeussilver/bim-ifc-mcp, https://github.com/louistrue/ifcx-mcp, https://github.com/ekkodale/IFC-MCP
- Archicad: https://github.com/SzamosiMate/tapir-archicad-MCP, https://github.com/joacos/archicad-mcp
- Tekla: https://github.com/teknovizier/tekla_mcp_server
- Regulation and standards seen: Japan's Building Standards Act (in okuno-dsi README); IFC4.3 and IFC5/IFCX; IDS; BCF 2.1; Uniclass; bSDD

## Notable sources
- https://github.com/mcp-servers-for-revit/mcp-servers-for-revit/issues/1 connection failure with a 10 m wall prompt
- https://github.com/mcp-servers-for-revit/mcp-servers-for-revit/issues/30 knowledge-graph proposal with false-"done" benchmark
- https://github.com/mcp-servers-for-revit/mcp-servers-for-revit/issues/48 command instance failure
- https://github.com/mcp-servers-for-revit/mcp-servers-for-revit/issues/63 port and autostart config
- https://github.com/mcp-servers-for-revit/revit-mcp/issues/28 "list all pipes" Method not found
- https://github.com/mcp-servers-for-revit/revit-mcp/issues/26 using Mistral or Llama
- https://github.com/mcp-servers-for-revit/revit-mcp-plugin/issues/5 tutorial request
- https://github.com/mcp-servers-for-revit/revit-mcp-plugin/issues/11 Chinese post on developer job fears
- https://github.com/bimwright/rvt-mcp/issues/13 door placement ignores coordinates
- https://github.com/bimwright/rvt-mcp/issues/14 stairs and send_code crash
- https://github.com/bimwright/rvt-mcp/issues/21 mutating tools fail
- https://github.com/bimwright/rvt-mcp/issues/23 context compaction
- https://github.com/shuotao/REVIT_MCP_study/issues/144 create_wall level selection (zh-TW)
- https://github.com/shuotao/REVIT_MCP_study/issues/150 DWG beams to walls
- https://github.com/shuotao/REVIT_MCP_study/issues/110 pyRevit button limits
- https://github.com/IfcOpenShell/IfcOpenShell/issues/7945 LLM-fabricated IFC rejected by viewers
- https://github.com/IfcOpenShell/IfcOpenShell/issues/8951 empty tool descriptions
- https://github.com/Menezeris/AIMviewer/issues/65 camera control prompts (Slovak)
- https://github.com/LuDattilo/revit-mcp-server/issues/16 view screenshot for vision models
- https://github.com/SzamosiMate/tapir-archicad-MCP/issues/23 duplicate elements on retry
- https://github.com/JotaDeRodriguez/Bonsai_mcp prompt list for Bonsai
- https://github.com/flinker-app/ifc-mcp prompt list and ChatGPT desktop setup
- https://github.com/Daviidro/ifcopenshell-mcp "You ask / It does" table
- https://github.com/zeussilver/bim-ifc-mcp deterministic checks philosophy
- https://github.com/ekkodale/IFC-MCP persona-driven business case
- https://github.com/joacos/archicad-mcp Spanish prompts
- https://github.com/JefaturaBIM94/RevitMCPBOQ Spanish takeoff prompts
- https://github.com/matsuokakoki/ifc-bim-llm-finetuning Japanese fine-tuning experiment and error types
- https://community.osarch.org/discussion/comment/30650 AI-connected IFC 4.3 scheduler

## Gaps
- WebSearch was unavailable (budget exhausted), so no blog, LinkedIn, YouTube, Habr, Zhihu, CSDN, Qiita, Zenn or Reddit content was found. Qiita, Zenn, Habr and cnblogs site-search pages did not return usable results via fetch.
- No real Russian-language record: the Russian synthetic prompts are based on English/Chinese patterns, not on observed posts.
- buildingSMART forum search returned only one snippet; most ChatGPT/LLM threads there were not seen.
- Several "real" records are README example prompts (official_doc), not genuine user posts; user-voice records come mostly from GitHub issues.
- Japanese and Chinese user prompts typed to an AI (as opposed to issue text) were not found.
- No suspicious or pirated sites were encountered.
