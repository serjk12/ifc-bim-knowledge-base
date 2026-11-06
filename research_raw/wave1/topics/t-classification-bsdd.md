# Classification (Uniclass, OmniClass, КСИ, CoClass, NL-SfB, GB/T 51269) and bSDD in IFC

Cell: t-classification-bsdd · Languages: English (real sources); synthetic prompts in en, ru, zh, es, pt, de, fr, ja, ko, it · Collected: 2026-11-06 · Records: 38 real / 18 synthetic · Communities covered: Autodesk revit-ifc GitHub issues, IfcOpenShell/Bonsai GitHub issues, OSArch community, buildingSMART forums

IMPORTANT LIMITATION: the WebSearch budget was exhausted before any search ran, so no native-language community (dwg.ru, csdn, cnblogs, qiita, etc.) was searched. All real records are English-language and come from GitHub (via gh), OSArch and buildingSMART forum pages fetched directly.

## Top themes (ranked by frequency)
- Revit IFC exporter classification settings regress or silently do nothing between exporter versions (22.5.1, 23.1.1, 22.6).
- Unwanted Uniformat IfcClassification always written when Assembly Code is used for another national system.
- Getting number + description of a code (Uniclass, DIN 276) into IfcClassificationReference Identification and Name.
- ClassificationCode[Type] landing on occurrences instead of types.
- Multiple classifications per element and filling all IfcClassification attributes (edition, source, location).
- How IFC classes, predefined types and external classification systems relate (layered approach).
- Mapping tables between Uniclass / OmniClass / Uniformat / national systems and IFC; lack of official ones.
- bSDD usage: adding dictionaries (e.g. Brazilian SICLIC), classification vs property mapping, GUID identity, rate limiting and errors in Bonsai.
- Lack of standardisation of IfcClassification values; calls for a registry with URIs.
- Rule-based automatic classification from properties (IDS vs bSDD).
- Exporting classification data to CSV / cost schedules.
- Request for native bSDD integration in Revit.
- Choosing the right IFC class/enum (reducing coupling, assemblies) which people also call classification.
- IFC4.3 domain placement versus classification.

## What people want (the goals behind the questions)
- Export a national classification (Uniclass, DIN 276, eBKP, CCI, NL-SfB, SICLIC) from Revit into IFC reliably, without Uniformat noise.
- Verify that every element has a code and that the code survives to downstream tools (Solibri, BIMvision, CSV, cost schedules).
- Assign classifications in bulk and by rule (property to code), and convert between systems.
- Use bSDD dictionaries (including their own national ones) to attach properties and classes without clunky plugins.
- Understand conceptually how IFC classes and external classification coexist.

## How people write here
- Register: GitHub issues are terse and technical, often with screenshots, version numbers and tracebacks and no greeting. Forum posts are polite and longer, with numbered questions.
- Jargon: "Assembly Code", "Classification Manager", "ClassificationCode(2)", "Uniclass Ss code", "bSDD", "Demo mode", "pset".
- Typical fragments: "we don't use Uniformat" ; "works in 22.5.0.0, broken in 22.5.1.0" ; "No bSDD Props Found" ; "propperly" (misspelling) ; "are there more people with these issues?".
- Context given: Revit version, exporter version, IFC schema, viewer used to check; context omitted: sample files, exact parameter names.
- Tone: mostly frustrated or confused for bug reports, curious/neutral for conceptual forum threads; occasional sarcasm about vendor mappings.
- Code-switching: non-native speakers (German, Portuguese, Polish contexts) write English with local standard names (DIN 276, ABNT NBR 15965, ÖNORM B 1801).

## Local ecosystem
- Standards/systems: Uniclass 2015 (NBS) https://www.thenbs.com/our-tools/uniclass ; OmniClass/Uniformat (CSI) https://www.csiresources.org ; NL-SfB, CCS (Cuneco), CoClass (ISO 81346 based), eBKP (Switzerland), DIN 276 (Germany), ÖNORM B 1801 (Austria), SICLIC / ABNT NBR 15965 (Brazil). КСИ and GB/T 51269 not researched (see Gaps).
- bSDD: https://search.bsdd.buildingsmart.org ; dictionary management https://manage.bsdd.buildingsmart.org
- Tools: Autodesk Revit IFC exporter https://github.com/Autodesk/revit-ifc ; Autodesk Classification Manager; Bonsai/IfcOpenShell https://github.com/IfcOpenShell/IfcOpenShell ; usBIM.viewer+ ; Solibri ; BIMvision ; MagiCAD ; Graphisoft XML classification lists.
- Communities: OSArch https://community.osarch.org ; buildingSMART forums https://forums.buildingsmart.org ; OSArch wiki Revit classification setup (page URL returned 404 on direct fetch).

## Notable sources
- https://github.com/Autodesk/revit-ifc/issues/509 regression: one IfcClassification per Assembly Code
- https://github.com/Autodesk/revit-ifc/issues/556 classification settings not exported (2023)
- https://github.com/Autodesk/revit-ifc/issues/456 Classification Manager values to IFC
- https://github.com/Autodesk/revit-ifc/issues/486 cannot disable Uniformat
- https://github.com/Autodesk/revit-ifc/issues/856 disable Uniformat enhancement, localised parameter names
- https://github.com/Autodesk/revit-ifc/issues/807 classification system from parameter name
- https://github.com/Autodesk/revit-ifc/issues/903 bSDD integration request
- https://github.com/Autodesk/revit-ifc/issues/691 ClassificationCode[Type] lands on occurrences
- https://github.com/Autodesk/revit-ifc/issues/182 multiple classifications metadata
- https://github.com/Autodesk/revit-ifc/issues/277 classification options from API
- https://github.com/IfcOpenShell/IfcOpenShell/issues/4126 bSDD IFC2X3 Location crash
- https://github.com/IfcOpenShell/IfcOpenShell/issues/4112 bSDD classify error
- https://github.com/IfcOpenShell/IfcOpenShell/issues/9034 NL-SfB KeyError
- https://github.com/IfcOpenShell/IfcOpenShell/issues/7985 bSDD rate limit
- https://github.com/IfcOpenShell/IfcOpenShell/issues/7506 manual classification entry error
- https://github.com/IfcOpenShell/IfcOpenShell/issues/4612 classification UI suggestions
- https://github.com/IfcOpenShell/IfcOpenShell/issues/7150 duplicate IfcClassification on library import
- https://community.osarch.org/discussion/3680/bsdd-dictionaries SICLIC dictionary
- https://community.osarch.org/discussion/comment/29871#Comment_29871 automatic rule based classification
- https://community.osarch.org/discussion/comment/18591#Comment_18591 export classification to CSV
- https://community.osarch.org/discussion/2480/rfc-classification-s classification RFC
- https://forums.buildingsmart.org/t/uniclass-2015-and-ifc/4423 Uniclass and IFC
- https://forums.buildingsmart.org/t/bsdd-classification-mapping-and-specific-pset-values/4538 bSDD NL-SfB mapping
- https://forums.buildingsmart.org/t/how-does-ifc-work-with-existing-classification-systems-such-as-omniclass-uniformat-etc/804 classic concept thread
- https://forums.buildingsmart.org/t/lack-of-standardisation-of-ifcclassification/2581 registry proposal
- https://forums.buildingsmart.org/t/bsdd-access-for-products-and-classification-standard-bsdd-guid-vs-ifc-guid/1726 bSDD GUIDs
- https://forums.buildingsmart.org/t/bsdd-buildingsmart-data-dictionary-and-classification-of-ifc-4x3-domain-mapping/4854 IFC4.3 domains

## Gaps
- WebSearch quota was exhausted at the start; zero web searches ran. No dwg.ru, csdn, cnblogs, zhihu, qiita, cad.de, Spanish/Portuguese/French/Italian/Korean community content was found; direct fetch of dwg.ru and cnblogs search URLs returned 404.
- No real records for КСИ, CoClass, GB/T 51269, Japanese, Korean or other languages; synthetic prompts for these are plausible but not evidence-based.
- Autodesk forums, Graphisoft community, Stack Overflow and Reddit not reached.
- The OSArch wiki classification page fetch gave 404; forums.autodesk.com returned 403.
- 38 real records (below the 25-50 target only if counting depth; some are title-only snippets: revit-ifc 101, 186, 487, 660, 327 and three OSArch threads).
- No suspicious sites encountered.
