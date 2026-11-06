# 繁體中文 (台灣/香港): IFC 匯出, BIM 送審, Revit

Cell: zh-tw-hk · Languages: Chinese (Traditional), some English · Collected: 2026-11-06 · Records: 18 real / 17 synthetic · Communities covered: HK government and CIC pages, Taiwan city-government manuals (snippets), Taiwan university theses, one Taiwanese blog, vendor help, GitHub issues. NOT covered: PTT, Mobile01, HK forums (see Gaps).

Important caveat: the WebSearch budget ran out after about 8 searches, and PTT returned 403 to fetch. Real records are therefore fewer and less "forum-voiced" than intended. Records r012-r018 are English-language issues; they relate to the zh cell only through CJK encoding, export errors and common Revit IFC pain points.

## Top themes (ranked by frequency)
- Government and authority submission rules: HK Buildings Department (BD) BIM tools and roadmap, Taipei and New Taipei permit and as-built IFC uploads.
- BIM model is supplementary to drawings in HK; drawings prevail if they conflict.
- Revit export class mapping and IfcExportAs (proxy problem).
- IFC interoperability loss between Revit, ArchiCAD, Tekla and structural analysis software (ETABS, SAP2000, Robot); this is the main theme in Taiwan theses.
- Chinese/CJK characters and special-character encoding in IFC (mojibake, STEP escapes).
- File too large / export fails (permissions, network drive, complex geometry).
- Importing IFC back into Revit: phase and view visibility issues.
- Regulation-driven parameters: Taiwan Building Technical Regulations (建築技術規則) parameters for automated code checking.
- Open BIM workshops: Archicad-Revit IFC round trips (CIC).
- As-built (竣工) models for FM handover.

## What people want (the goals behind the questions)
- To pass permit review: know which IFC version, MVD and parameters the authority expects, and self-check before upload.
- Get IFC out of Revit without everything becoming IfcBuildingElementProxy, and without data loss.
- Keep Chinese names and properties readable.
- Shrink huge IFC files so they upload to a government portal.
- Check areas (GFA), fire ratings, storey data against area tables.
- Hand over as-built models and room lists to FM.

## How people write here
- Taiwan blogs are first-person and casual, with English software names kept in capitals: "REVIT、ARCHICAD與TEKLA".
- Government and academic writing is formal; ROC years are used (「108年版」 = 2019).
- Taiwan uses 匯出/匯入 (export/import) and 模型; Mainland-flavored vendor help uses 導入/導出. HK uses 建築信息模擬 (BIM), 認可人士 (AP, Authorized Person) and 圖則 (plans).
- Code-switching is heavy: IFC, proxy, MVD, GUID, Pset stay in English.
- Short, context-light prompts are expected. Fragments: "IFC檔太大傳不上系統"; "門都變proxy"; "2D看得到3D找不到".
- Mojibake and "messy code" complaints are written in basic English by Chinese-speaking developers.

## Local ecosystem
- HK Buildings Department BIM page (Revit and ArchiCAD plug-ins, openBIM tools, BST): https://www.bd.gov.hk/tc/resources/online-tools/building-information-modelling/index.html
- HK DEVB roadmap for BIM-based plan submission: https://www.devb.gov.hk/filemanager/tc/content_2373/BIM-Book-content-cn.pdf
- HK Construction Industry Council (CIC) BIM portal and standards: https://www.bim.cic.hk/zh-hant/resources/publications
- Taipei Building Administration Office as-built IFC upload manual: https://dbadgp.gov.taipei/DownFiles/Login/使照竣工模型上繳操作手冊.pdf
- New Taipei Public Works BIM reference manual (Revit permit template and review system): https://www.bim.ntpc.gov.tw/Filedownload/新北市政府工務局BIM工作參考手冊108年版.pdf
- Software: Revit, Archicad (Graphisoft HK and TW), Tekla, ETABS, SAP2000, Navisworks.
- Open source: IfcOpenShell, Autodesk revit-ifc exporter.

## Notable sources
- https://housegear.pixnet.net/blog/posts/3042268210 - Taiwanese blog on importing IFC into Revit (2013).
- https://www.bd.gov.hk/tc/resources/online-tools/building-information-modelling/index.html - BD BIM tools and policy.
- https://www.devb.gov.hk/filemanager/tc/content_2373/BIM-Book-content-cn.pdf - roadmap booklet (cover only readable).
- https://www.careyourbuilding.bd.gov.hk/ors/tc/event/307.html - roadmap consultation event.
- https://www.bim.cic.hk/zh-hant/events/detail/304 - CIC Archicad/Revit IFC workshop.
- https://www.bim.cic.hk/zh-hant/resources/publications_detail/117 - CIC publications list (openBIM beginner's guide 2025).
- https://help.graphisoft.com/AC/29/TAI/_AC29_Help/121_IFC/121_IFC-1.htm - Archicad IFC help in Traditional Chinese.
- https://dbadgp.gov.taipei/DownFiles/Login/使照竣工模型上繳操作手冊.pdf - Taipei as-built upload.
- https://www.bim.ntpc.gov.tw/Filedownload/新北市政府工務局BIM工作參考手冊108年版.pdf - New Taipei manual.
- https://etheses.lib.ntust.edu.tw/thesis/detail/2e82ca6d84bfe5f839f58b35029a1d54 - NTUST thesis on permit rule checking.
- https://tdr.lib.ntu.edu.tw/handle/123456789/90111 - NTU thesis on IFC loss to analysis software.
- https://github.com/Autodesk/revit-ifc/issues/458 - file too large export.
- https://github.com/Autodesk/revit-ifc/issues/441 - special character encoding.
- https://github.com/IfcOpenShell/IfcOpenShell/issues/571 - Chinese encoding in IFC.
- https://github.com/IfcOpenShell/IfcOpenShell/issues/3499 - Chinese strings truncated.
- https://github.com/IfcOpenShell/IfcOpenShell/issues/797 - Chinese in file names with IfcConvert.
- https://forums.autodesk.com/t5/revit-structure-forum/ifcexportas-parameter-doesn-t-work/td-p/8219179 - IfcExportAs not working.

## Gaps
- The WebSearch budget (shared limit) was exhausted after about 8 searches. Planned searches of ptt.cc, mobile01, HK forums, Facebook groups and Taiwan teaching blogs never ran.
- ptt.cc search pages returned 403 on fetch. Several Taiwan and HK PDFs failed (ECONNRESET, certificate error, or text not extractable), including the NTPC manual, the Taipei manual and the DEVB booklet; these were used as snippets only.
- Little genuine forum voice was collected; the real records are mostly official and academic. A follow-up pass is needed on PTT (Architecture, Civil), Mobile01, Facebook BIM groups, Vocus and Medium Taiwan authors.
- Not found: buildingSMART Taiwan or Taipei BIM Association material, TW-BIM standard text, Taiwan Construction and Planning Agency IFC guidelines.
- No suspicious or pirated sites were encountered.
