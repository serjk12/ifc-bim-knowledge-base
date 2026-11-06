# dwg.ru: IFC с ArchiCAD, Renga, nanoCAD, Tekla, Allplan, Navisworks
Cell: ru-dwg-other · Languages: Russian · Collected: 2026-11-06 · Records: 30 real / 14 synthetic · Communities covered: forum.dwg.ru (Revit, Tekla, ArchiCAD, Allplan, Renga threads), dwg.ru blogs/news, Renga official manual and articles

## Top themes (ranked by frequency)
- Tekla -> Revit via IFC: only grids visible, elements lost, rebar/connections not transferred (phases, "surface geometry" option)
- IFC into AutoCAD (no native import): workarounds via BricsCAD BIM, IfcConvert, KIT tool, AutoCAD Architecture
- ArchiCAD IFC -> Revit/SCAD/Lira: missing partitions, odd glass, wall junction offsets, class mapping file
- Transfer to structural analysis (SCAD, Lira, STARK ES): IFC loses analytical info
- Choosing IFC export settings (surface geometry, Coordination View, translators, schema 2x3 vs IFC4)
- Checking/validating IFC: free viewers (xBIM, KIT, BIMvision), text editor, online validators
- Customer/expertise requirements: IFC vs native formats, classifier-filled properties, national BIM rules (SP draft, 2019 deadline)
- Cyrillic in file names/paths and header breaking import (Tekla, Navisworks)
- Editing imported IFC in Revit (DirectShape, rebuild families)
- Exporting from products without IFC (Plant 3D, Navisworks) via Codemill / custom Xbim code
- Renga: property mapping JSON, Qto/Pset, IFC maturity doubts, Tessellation for Navisworks
- Software choice comparisons (Revit vs Tekla vs Allplan vs Renga)

## What people want
- Make a model from one tool arrive in another with geometry, types and properties intact, with minimal manual rework.
- Understand why a received IFC shows nothing/only axes, and diagnose whether export or import is at fault.
- Satisfy a customer or expert review demanding IFC with filled properties/classifier.
- Round-trip: edit imported IFC, convert to DWG/DXF, or feed analysis programs.
- Free tools to view/check IFC without licenses.

## How people write here
- Short, practical, often lower-case; thread title states the software pair ("Экспорт из Tekla в Revit").
- Transliterated and slang names: "Текла", "Ревит", "Архикад", "Сапфир", "нанокад", "ифс/ифц", "нависворкс/навис", "проксики".
- Little context: often no version, no IFC schema, no export settings; files attached instead.
- Quote error text verbatim ("System Error encountered during import").
- Fragments: "стандартный экспорт даёт одни оси"; "получается фигня"; "всё пучком"; "заказчик требует IFC".
- Forum conventions: replies terse, sometimes ironic ("IFC и аналитическая модель как молоток и кирпич"); thank-you closers like "помогло".
- Emotional tone: frustrated/confused, pressure from customer or expertise deadlines.
- Mixed: English product names plus Russian grammar ("экспортнуть", "импортнуть").

## Local ecosystem
- Renga Software / Renga BIM (Russian BIM, IFC mapping files): https://manual.rengabim.com/ehksport_atributov_obektov.html , https://rengabim.com/stati/bol-she-10-formatov-eksporta-importa-v-renga-kakoj-iz-nih-vybrat/
- nanoCAD / nanoCAD VK, Model Studio (Nanosoft/CSoft): IFC import of rooms and floors, news at https://dwg.ru/cat/news/4048
- SCAD, Lira, STARK ES, Forum-Scad, SAPFIR-3D, Bocad, Advance Steel, Allplan, Tekla BIMsight: structural/analysis tools mentioned.
- Regulations: draft SP on information modeling and Russian BIM requirements from 01.07.2019 (discussed on the forum); state expertise of information models (Renga article).
- Open-source/free: IfcOpenShell (IfcConvert), xBIM, KIT IFC viewer, BricsCAD BIM (commercial), Codemill IFC exporter (commercial).

## Notable sources
- https://forum.dwg.ru/showthread.php?t=146029 Tekla to Revit via IFC
- https://forum.dwg.ru/showthread.php?t=160240 SAPFIR IFC export / AutoCAD import
- https://forum.dwg.ru/showthread.php?t=173570 Plant 3D 2025 to IFC
- https://forum.dwg.ru/showthread.php?t=126080 Bocad IFC
- https://forum.dwg.ru/showthread.php?t=149046 Renga alternative opinions
- https://forum.dwg.ru/showthread.php?t=76210 ArchiCAD IFC to r2s
- https://forum.dwg.ru/showthread.php?t=154396 How to open IFC correctly
- https://forum.dwg.ru/showthread.php?t=166052 IFC import Revit 2022
- https://forum.dwg.ru/showthread.php?t=159943 IFC import error Tekla (Cyrillic)
- https://forum.dwg.ru/showthread.php?t=158006 IFC into AutoCAD
- https://forum.dwg.ru/showthread.php?t=163697 Advance Steel to Archicad
- https://forum.dwg.ru/showthread.php?t=155997 Tekla columns in Revit
- https://forum.dwg.ru/showthread.php?t=146367 Tekla Field 3D IFC
- https://forum.dwg.ru/showthread.php?t=133669 Revit to STARK ES
- https://forum.dwg.ru/showthread.php?t=96356 IFC to DWG
- https://forum.dwg.ru/showthread.php?t=153428 Revit expertise / BIM 2019
- https://forum.dwg.ru/showthread.php?page=2&t=150272 Tekla BIMsight IFC
- https://forum.dwg.ru/showthread.php?t=142967 Revit to SCAD
- https://forum.dwg.ru/showthread.php?t=33352 ArchiCAD to analysis
- https://forum.dwg.ru/showthread.php?t=75883 ArchiCAD to DWG solid
- https://forum.dwg.ru/showthread.php?t=159973 SolidWorks to Revit
- https://forum.dwg.ru/showthread.php?t=130296&page=2 Edit IFC family
- https://forum.dwg.ru/showthread.php?t=75685 Resave ArchiCAD files
- https://dwg.ru/b/utrfm/263 Revit vs Tekla vs Allplan
- https://manual.rengabim.com/ehksport_atributov_obektov.html Renga attribute export

## Gaps
- No genuine nanoCAD- or Navisworks-specific IFC question threads found; only mentions (nanoCAD VK news, Navisworks inside Plant 3D thread). Allplan IFC threads only appear as long threads (pages not read in depth).
- Many forum pages returned garbled encoding; summaries are approximate. Snippet-evidence records (r002, r024, r025, r028-r030) not fully read; years of those are estimated from thread ids.
- The ArchiCAD-specific ArchiCAD forums (archicad-talk, Telegram) not covered; Renga support forum not accessed. No suspicious sites were encountered or linked.
- Posts are mostly 2011-2021; few 2023-2026 posts.
