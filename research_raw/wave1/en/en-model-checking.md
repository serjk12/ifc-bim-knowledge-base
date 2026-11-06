# Model checking tools: Solibri, BIMcollab, Simplebim, dRofus (IFC QA questions)
Cell: en-model-checking · Languages: English (plus Dutch/Norwegian titles found on GitHub) · Collected: 2026-11-06 · Records: 21 real / 16 synthetic · Communities covered: BIMcollab Help Center (vendor KB), GitHub issues (IfcOpenShell, OpenAEC BIM validator, pragmaticBIM, small dRofus/Revit tool repos)

NOTE: this cell is THIN. The WebSearch budget was exhausted before the first search ran (0 searches done), so only direct fetches and GitHub CLI searches were possible. Real records are below the 30-60 target; 12 of 21 are title-only snippets.

## Top themes (ranked by frequency)
- BCF issue sync between Solibri and BIMcollab (status mapping, numbering, overwritten data, missing properties)
- BCF viewpoints losing or mis-typing components (selected vs colored, missing after import)
- Connector/export failures (https URL, proxy, duplicate titles, admin rights)
- Clash detection and duplicate/overlapping elements as a standard checking need
- Property-based coloring/filtering (Smart Views, Solibri checking views)
- Classification validity (NL-SfB code lists), not just presence
- Rulesets beyond IDS (clearance zones, envelope, accessibility, Bbl)
- Georeference consistency across federated models
- Viewer differences in how IFC styles/transparency render (Solibri vs Bonsai)
- dRofus integration with Revit parameters (Norwegian users)
- Quantities/model intake checks without needing Solibri

## What people want
- Trustworthy round-trip of issues between checkers and issue trackers without data loss.
- Counts and lists of failing elements per storey/class, not hundreds of repeated clash lines.
- Checks for presence AND validity of properties and classification codes.
- Cheaper or open alternatives to Solibri-style rule checking (IDS, scripts).

## How people write here
- Vendor KB titles are short "Why is/are/don't I..." questions with product names, no model context ("Why are viewpoint components missing after an import?").
- Developer issues are structured and technical: numbered findings, GUIDs, counts ("427 of 580 lose every style").
- Dutch/Norwegian GitHub titles mix local words with English tool names (Smart Views, Solibri, dRofus).
- Jargon: issue, presentation, viewpoint, BCF, smart view, ruleset, clash set, IDS.
- Context usually omitted: IFC version, tool version, file size.

## Local ecosystem
- Solibri: https://www.solibri.com ; BIMcollab (KP/BIMcollab): https://helpcenter.bimcollab.com ; Simplebim: https://simplebim.com ; dRofus: https://support.drofus.com
- IfcOpenShell / Bonsai: https://github.com/IfcOpenShell/IfcOpenShell
- OpenAEC BIM validator (NL, IDS-based): https://github.com/OpenAEC-Foundation/OpenAEC-BIM-validator
- pragmaticBIM reference rulesets: https://github.com/pragmaticBIM/pragmaticBIM-reference
- buildingSMART IDS/BCF standards (referenced, not fetched).

## Notable sources
- https://helpcenter.bimcollab.com/en/articles/341453-solibri-bcf-live-connector-tips-and-troubleshooting
- https://helpcenter.bimcollab.com/en/articles/340730-why-is-issue-status-in-solibri-changed-after-synchronization-to-bimcollab
- https://helpcenter.bimcollab.com/en/articles/341451-why-are-viewpoint-components-missing-after-an-import
- https://helpcenter.bimcollab.com/en/articles/341452-why-don-t-i-see-selected-colored-components-in-other-bim-tools
- https://helpcenter.bimcollab.com/en/collections/714834-integrations-and-desktop-apps
- https://github.com/IfcOpenShell/IfcOpenShell/issues/10020
- https://github.com/OpenAEC-Foundation/OpenAEC-BIM-validator/issues/12
- https://github.com/OpenAEC-Foundation/OpenAEC-BIM-validator/issues/17
- https://github.com/pragmaticBIM/pragmaticBIM-reference/issues/55

## Gaps
- WebSearch unavailable (budget exhausted), so no forum/Reddit/LinkedIn/community threads were found; no genuine end-user questions on Solibri/Simplebim/dRofus beyond vendor KB titles.
- community.solibri.com did not resolve; solibri.com/community and simplebim.com/support returned 404; support.drofus.com showed no IFC articles on its landing page.
- BIMcollab KB entries 5-9 are title-only (snippet evidence); year unknown (null).
- Suspicious sites: none encountered.
- Recommend re-running this cell once search quota is available.
