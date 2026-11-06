# Revit IFC export: complete reference (settings, mapping, parameters, versions)

## In plain words

Revit is Autodesk's BIM authoring program; its native `.rvt` file is proprietary. To hand a model to other programs (viewers, checkers, other CAD) it can export to IFC (Industry Foundation Classes, open standard by buildingSMART, ISO 16739). The export is done by an add-in called "IFC for Revit" (the exporter). Its source code is public on GitHub as Autodesk/revit-ifc [1]. Each export is controlled by a "setup" (a named configuration): IFC schema/view (for example IFC2x3 Coordination View 2.0, IFC4 Reference View), which property sets to write, how to place the model in space, how detailed the geometry is, and a mapping table that decides which Revit category becomes which IFC class (IfcWall, IfcSlab, ...). Most "wrong IFC" complaints come from a wrong setup, a wrong mapping, or a known exporter bug, not from the IFC format itself.

Last researched: 2026-11-06

> Research limits for this document: the web-search quota was exhausted after the first calls, so most facts come from fetching the official GitHub repository pages and source files directly (read as text only, nothing downloaded). Autodesk help pages and buildingSMART pages could not be read (JavaScript-only pages or HTTP 403). Anything from memory or general practice is marked "(unverified)". See "Gaps".

---

## 1. Where IFC export lives in Revit

- Menu: File > Export > IFC. This opens the "Export IFC" dialog with the current setup name, a "Modify setup..." button, and the file type [18][14].
- Ribbon route (varies by version): the same command can be reached from the IFC export entry in the export menu (unverified for exact ribbon placement in 2027).
- "Modify setup..." opens the large setup dialog with the tabs described in section 4. Tab names read from the exporter's resource file: General, Additional Content, Property Sets, Level of Detail, Advanced, Geographic Reference, Classification Settings, Project Address, Category Mapping, Parameter Mapping, Property Mapping [14]. There is also a COBie company/project info pair of tabs in the source (COBieCompanyInfoTab / COBieProjectInfoTab) [19].
- Export is limited to the active view only if you tick "Export only elements visible in view"; otherwise the whole model (minus filtered categories) is exported [14].
- The exporter overrides the IFC support that ships inside Revit; installing a newer "IFC for Revit" add-on release replaces the built-in one for that Revit year [1]. Add-ons from 2023 onward should also be available via the Autodesk Desktop App [1].

## 2. The open-source exporter (Autodesk/revit-ifc)

Facts from the repository README and release pages [1][2][18]:

| Item | Value |
|---|---|
| What it is | .NET code used by Revit and Revit LT (2019 and later) for IFC export, Link IFC, and the export UI; improves Navisworks import [1] |
| Support policy | "The most current annual version and two previous versions are supported with fixes/changes" [1] |
| Default branch | `master`; for building use the branch that matches your Revit year, e.g. `Release_27.x.x` for Revit 2027 [1][18] |
| License | LGPL v2.0; uses ANTLR 4 (BSD); includes a proprietary Autodesk DLL (Autodesk.SteelConnections.ASIFC.DLL) [1] |
| Import code | IFC import logic is largely inside Revit and not open source [18] |
| Docs | Autodesk help "IFC in Revit" (2022-2024 pages linked), Revit IFC Manual V2.0 (multilingual, on Autodesk blog), and a small GitHub wiki with two pages: "Mapping geo reference in IFC4" and "Revit IfcExporter parameter expression" [1][6] |
| Old forums | archived SourceForge forums (ifcexporter) [18] |
| Source layout | `Source/Revit.IFC.Export`, `Revit.IFC.Common`, `Revit.IFC.Import`, `Revit.IFC.Import.Core`, `IFCExporterUIOverride`, `RevitIFCTools` [19] |

### Release numbering and recent releases

Tag format: `IFC_v<RevitYear-2000>.<minor>.<patch>[.<build>]`, e.g. `IFC_v27.4.0.30` = Revit 2027. The releases page shows dates without the year [2]; the issue tracker context (2026 issue dates) implies the 27.x releases are 2026 (unverified).

| Tag | Date shown | Revit | Notes [2][3][4][5] |
|---|---|---|---|
| IFC_v27.4.0.30 | 30 Oct | 2027 | Extended properties go to their own property set named after the containing element (not "Other"); fixes: mapped parameters missing from user-defined sets, wall shift with "Show Parts", wall geometry for IFC2x3 and IFC4x3, IFC parameters dialog when editing family type parameters [3] |
| IFC_v27.3.0.12 | 13 Aug | 2027 | Bug fixes only: export to network location, room geometry, assemblies, ramps exported as IfcSlab, MEP duplicates, footing/slab/stair base quantities, ObjectType for IfcProject (IFC4/IFC4x3), predefined type when changing "Export to IFC As", user-defined property sets on project (#971) [4] |
| IFC_v27.0.1.1 | 22 Apr | 2027 | Shared parameters can be added to user-defined property sets; room geometry shift fix (#924) [2] |
| IFC_v27.0.1 | 9 Apr | 2027 | First IFC extension for Revit 2027 [5] |
| IFC.v26.4.1 | 18 Dec | 2026 | Adds IFC4.3 Reference View exchange requirements [2] |
| IFC_v26.4.0 | 30 Oct | 2026 | Assembly placement, rebar material, space elevation (#907) fixes [2] |
| IFC_v25.4.40 | 14 Jan | 2025 | Adds IFC4.3 Reference View exchange requirements [2] |
| IFC_v24.3.40 | 14 Jan | 2024 | Adds IFC4.3 Reference View exchange requirements; fixes in Regulatory Requirement View and Link IFC placement [2] |

Practical reading: IFC4.3 export in Revit exists as "IFC4.3 Reference View" and "IFC4.3 Design Transfer View [Unofficial]" [14]; the 2024/2025/2026 updates are what added it to older Revit years [2]. The file header produced for it names schema `IFC4X3_ADD2` [24].

## 3. IFC versions / MVDs available in the setup

Labels as they appear in the exporter resource file [14] and the internal enum names [10][15]:

| UI label | Internal id | Schema | Typical use |
|---|---|---|---|
| IFC 2x3 Coordination View 2.0 | IFC2x3CV2 | IFC2x3 TC1 | Default setup in code [9]; the most widely accepted exchange view for coordination (unverified claim about popularity, but it is the code default) |
| IFC 2x3 Coordination View | IFC2x3 | IFC2x3 | Older CV 1.0-style setup, split walls on [10] |
| IFC 2x2 Coordination View | IFC2x2 | IFC2x2 | Legacy [14] |
| IFC 4 Coordination View 2.0 (label in enum) | IFC4 | IFC4 | Present in the enum; may be hidden in the UI (unverified) [15] |
| IFC4 Reference View | IFC4RV | IFC4 | Read-only reference; three built-in setups by Exchange Requirement: Architecture, Structural, BuildingService [10] |
| IFC4 Design Transfer View [Unofficial] | IFC4DTV | IFC4 | Editable handover; label says "[Unofficial]" [14] |
| IFC4.3 Reference View | IFC4x3RV | IFC4.3 (header `IFC4X3_ADD2`) | Same three Exchange Requirements [10][24] |
| IFC4.3 Design Transfer View [Unofficial] | IFC4x3DTV | IFC4.3 | [14] |
| IFC2x3 COBie 2.4 Design Deliverable View | IFC2x3FM | IFC2x3 | COBie handover; uses property set file "IFC2x3 COBie 2.4 Design Deliverable.txt" and COBie company/project info tabs [9][14] |
| IFC 2x3 GSA Concept Design BIM 2010 | IFCCOBIE | IFC2x3 | Legacy US GSA view (label from the resource key `IFCMVDGSA`); bounding box on by default [10][11][15] |
| IFC 2x3 Basic FM Handover View | IFC2x3BFM | IFC2x3 | Legacy FM handover [14] |
| IFC+SG | IFCSG | IFC2x3 | Singapore e-submission: preset CRS SVY21 (EPSG:3414), uses "IFC+SG Property Sets.txt", site placement = Project Base Point, uses view geometry [9] |

Built-in setups created in code (15 entries, by internal id): IFC2x3CV2, IFC2x3, IFCCOBIE, IFC2x3BFM, IFC2x2, IFC2x3FM, IFC4RV x3 (Architecture/Structural/BuildingService), IFC4DTV, IFC4x3RV x3, IFC4x3DTV, IFCSG [10]. Setup names are generated as `<version label> [<exchange requirement>]`, e.g. "IFC4 Reference View [Architecture]" (exact short label text unverified) [9]. All Reference View and DTV setups enable base quantities; the default IFC2x3CV2 setup has everything off except common property sets [9][10].

"IFC4 Reference View" is a buildingSMART MVD (Model View Definition) that limits what is exported, while the "Design Transfer View" is not a certified view, hence "[Unofficial]" [14]. Whether a given Revit build is buildingSMART-certified for a view must be checked on buildingSMART's certification pages (not readable in this research) (unverified).

Related schema facts (unverified here, buildingSMART pages returned 403): IFC2x3 TC1 and IFC4 (ADD2 TC1) are ISO 16739:2013 and ISO 16739-1:2018; IFC4.3 ADD2 is the latest, published as a newer edition of ISO 16739-1. Check exact numbers at buildingsmart.org before quoting.

### File types

The exporter supports four formats [16]: IFC (`.ifc`, STEP text, default), IFCXML (`.ifcxml`), IFCZIP (`.ifczip`, zipped STEP) and IFCXML-ZIP (`.ifczip`) [14]. There is no IFCJSON option in the exporter [16]. File type is inferred from the extension if absent in API use [11].

## 4. Setup dialog tab by tab

Defaults below are the code defaults in `IFCExportConfiguration` [9] (the UI shows built-in setups with different combos [10]).

### General tab
| Option | Meaning / default |
|---|---|
| IFC Version | see section 3; default IFC2x3CV2 [9] |
| Exchange Requirement (IFC4/IFC4.3 RV) | Architecture, BuildingService, Structural, NotDefined [13] |
| Facility Type / Facility Predefined Type | IFC4.3 only: Building (default), Bridge, Railway, Road, MarineFacility [13]; UI strings "Marine Facility (IfcMarineFacility)" [14] |
| File type | IFC / IFCXML / IFCZIP / IFCXMLZIP [16] |
| Phase to export | "Phase to export"; default is the last phase of the document; a filter view's phase overrides the value [11][14] |
| Space boundaries | None / 1st Level / 2nd Level; default None [14][9]. COBie setup uses 2nd level; IFC2x3 and IFC2x2 presets use 1st level [10] |
| Coordinate Base | Project Base Point, Internal Origin, Survey Point, Shared Coordinates [14]; internal enum SiteTransformBasis: Shared (default), Site (survey point), Project, Internal, ProjectInTN, InternalInTN [12]. The two "in True North" variants are "Project Base Point oriented in True North" and "Internal Origin oriented in True North" [14] |
| Split walls and columns by level | default off; on in several legacy setups (IFC2x3, COBie, BFM, SG) [10] |
| Include steel elements | default true; only effective for IFC2x3 export per cache code [9][11] |
| Include IFCSite elevation in the site local placement origin | default off [14] |
| Selected site | name of site when the model has several (config field SelectedSite) [9] |

### Additional Content tab
| Option | Default |
|---|---|
| Export only elements visible in view | off [9] |
| Export rooms, areas and spaces in 3D views | off [9][14] |
| Export 2D plan view elements | off in code defaults; on for FM presets [9][10] |
| Export linked files as separate IFCs | LinkedFileExportAs.DontExport; export-as-separate creates one IFC per link plus a host IFC [9][14] |
| Export parts as building elements | off [9] |
| Export ceiling grids | off [9] |
| Export bounding box | off (on for IFCCOBIE/FM presets) [9][11] |
| Include space boundaries | via Space boundaries combo [14] |

Linked instance errors reported by the exporter: not exported if non-conformal, mirrored (mirror the geometry and relink) or scaled [14].

### Property Sets tab
| Option | Default | Notes |
|---|---|---|
| Export Revit property sets | off | "Pset_Revit_..." sets with Revit parameters (the so-called Revit psets), e.g. Pset_Revit_Type_Identity Data (name pattern unverified) [14][9] |
| Export IFC common property sets | on | Pset_WallCommon, Pset_DoorCommon... (IsExternal, FireRating, LoadBearing) [9] |
| Export base quantities | off (on for RV/DTV setups) | Qto_* quantity sets (Qto_WallBaseQuantities etc.) [9][10] |
| Export material property sets | off | Pset_MaterialCommon and similar [9] |
| Export schedules as property sets | off | schedule columns become a pset named after the schedule [9] |
| Export only schedules containing IFC, Pset, or Common in the title | optional restriction (config `ExportSpecificSchedules`) [9][14] |
| Export user defined property sets | off | needs a text file path (`ExportUserDefinedPsetsFileName`); see section 7 [9] |
| Export user defined parameter mapping table | off | legacy "custom parameter mapping table" with its own file [9][14] |
| Allow use of type properties in instance property sets | off | `UseTypePropertiesInInstacePSets` (spelling as in code) [9]; issue #989 happened with this ticked [21] |
| Classification settings | tab | classification system name, edition, source, file for IfcClassification [9] |

### Level of Detail tab
"Level of detail for some element geometry": Extra Low / Low / Medium / High (labels for Low-High unverified; "Extra Low" confirmed) [14]. In code the default is Low; `TessellationLevelOfDetail` 0.5 in config default; the API cache clamps values and maps legacy `UseCoarseTessellation` true to Extra Low [9][11]. Related checkboxes: "Use coarse tessellation for some BReps", "Keep tessellated geometry as triangulation" (UseOnlyTriangulation) [14].

### Advanced tab
| Option (UI label) | Config name | Default |
|---|---|---|
| Store the IFC GUID in an element parameter after export | StoreIFCGUID | off; writes IfcGUID parameter back to the Revit element so GUIDs stay stable across re-exports [14][11] |
| Export bounding box | ExportBoundingBox | off [9] |
| Use family and type name for references | UseFamilyAndTypeNameForReference | off [9] |
| Use 2D room boundaries for room volume | Use2DRoomBoundaryForVolume | off [9] |
| Use active view when creating geometry | UseActiveViewGeometry | off [9] |
| Always export faceted floors and roofs as a single IFC entity | ExportHostAsSingleEntity | off [9][14] |
| Export bars in uniform rebar sets as separate IFC entities | ExportBarsInUniformSetsAsSeparateIFCEntities | off [9] |
| Set "Last Modified" user to the Author in Project Information | OwnerHistoryLastModified | off [9] |
| Use visible Revit name as the IFCEntity name | UseVisibleRevitNameAsEntityName | off [9] |
| Use Type name only for IFCType name | UseTypeNameOnlyForIfcType | off [9] |
| Export solid model representation | ExportSolidModelRep | off [9] |
| Exclude filter | ExcludeFilter | text filter of excluded elements (syntax unverified) [9] |

### Geographic Reference, Classification, Project Address, COBie
- Geographic reference fields: CRS name, description, EPSG code, geodetic datum, map unit (GeoRefCRSName / GeoRefCRSDesc / GeoRefEPSGCode / GeoRefGeodeticDatum / GeoRefMapUnit) [9]. For IFC4, these feed IfcProjectedCRS and IfcMapConversion; the GitHub wiki "Mapping geo reference in IFC4" is a set of diagrams only (text not readable) [8].
- Project Address: assign address to building and/or site [14][9].
- COBie company and project info: used only by COBie setups [9][19].

### Saved configurations
- Setups ("configurations") are stored inside the Revit project via extensible storage in `DataStorage` elements; the current schema stores each configuration as one JSON string (schema name "IFCExportConfigurationMap") [10]. Older schemas are deleted when saved in the new one [10]. Therefore setups travel with the .rvt file, but not with the user profile. Built-in setups are saved only if modified [10].
- The special "<In-Session Setup>" holds unsaved edits (exact label unverified); in-session configurations are cached, not saved [10].
- Setups can be exported/imported as files in some versions (unverified).

## 5. Class mapping: category to IFC class and predefined type

In the setup dialog, "Category Mapping" (older name: "Export Class mapping table" or "Export IFC Class Mapping") lists every Revit category (and subcategory) with columns: Category, IFC Class Name, IFC Predefined Type (and a User Defined Type), Type IFC Class, etc. Templates can be created, copied, renamed, deleted, exported/imported as `.txt` files ("IFC Category Mapping Files") [14][19]. The setup stores the selected template name in `CategoryMapping` [9].

How the class is decided for one element (order in `GetExportTypeImpl`, from source comments) [17]:
1. The category export table (mapping) is checked first; a "not exported" entry stops export immediately.
2. Group / furniture checks.
3. The element's own override parameters: instance "Export to IFC As" first, then the type parameter "Export Type to IFC As" (built-in parameters `IFC_EXPORT_ELEMENT_AS`, `IFC_EXPORT_ELEMENT_TYPE_AS`); predefined type from `IFC_EXPORT_PREDEFINEDTYPE` (instance) then `IFC_EXPORT_PREDEFINEDTYPE_TYPE` (type) [17].

Typical default results (general knowledge of the shipped default table; exact table not verified here (unverified)):

| Revit category | IFC class | Typical predefined type |
|---|---|---|
| Walls | IfcWall (IfcWallStandardCase only in IFC2x3) | STANDARD / PARTITIONING / SHEAR (set by type) |
| Floors | IfcSlab | FLOOR |
| Roofs | IfcRoof (+ IfcSlab for layers in IFC2x3) | FLAT_ROOF, SHED_ROOF, etc. |
| Ceilings | IfcCovering | CEILING |
| Doors / Windows | IfcDoor / IfcWindow | DOOR / WINDOW |
| Columns / Structural Columns | IfcColumn | COLUMN |
| Structural Framing | IfcBeam (IfcMember for bracing) | BEAM |
| Structural Foundations | IfcFooting (IfcPile for piles) | FOOTING_BEAM, PAD_FOOTING |
| Stairs / Ramps / Railings | IfcStair / IfcRamp / IfcRailing | per type |
| Rooms / Spaces | IfcSpace | INTERNAL |
| Furniture | IfcFurniture (IfcFurnishingElement in IFC2x3) | NOTDEFINED |
| Generic Models | IfcBuildingElementProxy (IFC4.3: IfcBuildingElementProxy; IfcGeographicElement/IfcCivilElement for civil use) | NOTDEFINED |
| Mechanical/Plumbing equipment | IfcFlowTerminal / IfcDistributionElement family | per type |

Rules of thumb: predefined type values must belong to the chosen class' enum in the selected schema; a mismatch is written as USERDEFINED/NOTDEFINED or ignored (unverified). Some classes only exist in IFC4+ (e.g. IfcFurniture vs. IfcFurnishingElement; see issue #1007 on the wrong furniture type) [20].

## 6. Per-element override parameters

| Parameter (as seen in Revit) | Purpose | Notes |
|---|---|---|
| Export to IFC As (instance) / Export Type to IFC As (type) | IFC class, e.g. `IfcWall`, `IfcBuildingElementProxy`, or `IfcWall.SHEAR`-style "class.predefined" (syntax unverified) | Built-in parameters in current versions; the shared-parameter names `IfcExportAs` / `IfcExportType` were used in older workflows (unverified) [17] |
| IFC Predefined Type / Type IFC Predefined Type | enum value, e.g. `STANDARD`, `USERDEFINED` | instance first, then type [17] |
| IfcName / IfcDescription / IfcObjectType / IfcTag / IfcLongName | overrides of those IFC attributes | Names per the "IFC Parameters" group (unverified list); `IfcObjectType` handling bugs: #1009 [20] |
| IfcGUID | per-element GlobalId; written back when "Store the IFC GUID" is on | `AllowGUIDParameterOverride` option exists in API [11] |
| IfcSiteGUID, IfcBuildingGUID, IfcBuildingStoreyGUID | for site/building/storey (unverified) | |
| Pset_xxx.PropertyName (parameter naming) | a project/shared parameter named "Pset_WallCommon.FireRating" is written to that pset; a short name like "FireRating" works for most types but IfcLogical needs the full name (issue #1020) | [22] |

### Parameter expressions (verified, official wiki)
Introduced in exporter 18.3.2 [7]. Put a text expression in an IFC parameter such as IfcName and the exporter evaluates it:
- `{expr}` evaluate; `U{expr}` make unique by appending " (n)".
- `{$this("Name")}` instance parameter; `{$type("Name")}` type parameter; `{$this("Level").("Name")}` follow an ElementId parameter one step; `{$ElementId}`.
- `#` running number per parameter in a category; `##` per instance.
- Operators `+ - * /`, power `^`; `+` concatenates strings.
- Example: `{$type("Mark") + "-" + $this("Mark") + " " + #}`.
- The parameter must be a text parameter; the result is converted to the destination property type when known, else string. Store long expressions in a global parameter (e.g. IfcNameExpr) [7].
- The wiki page itself contains some typos in its examples [7].

## 7. Property sets, mapping tables and the user-defined pset file

Four ways to control properties:
1. IFC common psets (automatic; tick "Export IFC common property sets") using built-in code tables such as the 88+ "calculator" classes (Area, GrossVolume, FireRating, IsExternal, LoadBearing, Span, ...) [19].
2. Revit property sets ("Export Revit property sets"): every Revit parameter as a property in groups like "Pset_Revit_Identity" (naming pattern unverified).
3. User-defined property set file (legacy text file) selected under "Export user defined property sets".
4. Newer "Property Mapping" and "Parameter Mapping" tabs in the setup (UI in `IFCPropertyMapping` with property filter and Revit property selector), with templates saved as `.txt` ("IFC Property Mapping Files / Setups") [14][19]. Config field `PropertyMapping` stores the template name; a flag `isNewParameterMappingEnabled` switches the new mode on and the legacy flags (Revit psets, common psets, base quantities, material psets, schedules, user-defined psets) are ignored in that mode [9]. Hence the new UI is a replacement for the old checkboxes, not an addition.

Legacy user-defined property set file syntax (from the Revit IFC Manual and the shipped sample "DefaultUserDefinedParameterSets.txt"; content from memory, (unverified), verify against a real file):
```
# comment line
PropertySet:   <PsetName>   I|T   <IfcEntity>[, <IfcEntity> ...]
   <PropertyName>   <DataType>   [<RevitParameterName>]
```
- `I` = instance-level pset, `T` = type-level pset.
- Tabs separate fields; if the Revit parameter name is omitted, it equals the property name.
- Data types include Text, Label, Identifier, Boolean, Logical, Integer, Real, Length, Area, Volume, PlaneAngle (list unverified).
- File default name: `<setup name>.txt` in the add-in directory (e.g. "IFC+SG Property Sets.txt", "IFC2x3 COBie 2.4 Design Deliverable.txt") [9].
- 27.0.1.1 added support for shared parameters in user-defined sets; 27.3.0.12 and 27.4.0.30 fixed several mapping bugs [2][3][4].
- Duplicate property names within one set: the later wins; empty string does not overwrite [code reading of PropertySetDescription.cs].

Mapped-parameter precedence: if a Revit built-in parameter and a shared parameter have the same name, the exporter may pick the built-in value, ignoring case (issue #989, Czech names OBJEM/PLOCHA) [21].

## 8. Newest versions (2025-2027) and the new property-mapping UI

- Revit 2025 line: add-on 25.4.40 (Jan) added IFC4.3 RV; users still report 25.4.40 in 2026 bug reports [2][21].
- Revit 2026 line: 26.4.0 / 26.4.1; known open problems: IFC4x3 RV header says `CoordinationView` (#1013, Autodesk reproduced in 2026.4, not in 2027, logged internally, workaround: manual header edit which does not guarantee conformance) [24]; joined-geometry walls with masses regression (#1014) [25].
- Revit 2027 line: 27.0.1 (first), 27.0.1.1, 27.3.0.12, 27.4.0.30 [2]. Newest verified release at research date: 27.4.0.30 (30 Oct) [3]. README uses Revit 2027 as the build example [18].
- Property/category/parameter mapping is now UI-driven with templates (Category Mapping / Parameter Mapping / Property Mapping tabs) [14].
- A write-access pre-check was added in the 26.1/27 add-ons and blocks export to some network shares (#981) [23].
- Revit 2027 release timing and non-IFC changes: not researched (unverified).

## 9. Batch export: API, Dynamo, pyRevit, Design Automation

All of the following were not readable on Autodesk's site in this research; the code-side facts come from the exporter source [11].

### Revit API (C#, Python)
`Document.Export(string folder, string name, IFCExportOptions options)` runs an export. `IFCExportOptions` has `FileVersion` (IFCVersion enum) and `SpaceBoundaryLevel`, `WallAndColumnSplitting`, and `AddOption(key, value)` named options. Keys recognised by the open-source exporter [9][11]:
- Booleans: ExportBaseQuantities, ExportInternalRevitPropertySets, ExportIFCCommonPropertySets, ExportMaterialPsets, ExportSchedulesAsPsets, ExportUserDefinedPsets, Export2DElements, ExportCeilingGrids, ExportPartsAsBuildingElements, ExportBoundingBox, ExportRoomsInView, IncludeSiteElevation, UseCoarseTessellation, UseOnlyTriangulation, ExportSolidModelRep, UseActiveViewGeometry, StoreIFCGUID, UseFamilyAndTypeNameForReference, Use2DRoomBoundaryForVolume, IncludeSteelElements, UseVisibleRevitNameAsEntityName, UseTypeNameOnlyForIfcType, ExportHostAsSingleEntity, OwnerHistoryLastModified, ExportBarsInUniformSetsAsSeparateIFCEntities.
- Strings: ExchangeRequirement, FacilityType, FacilityPredefinedType, SitePlacement (Shared/Site/Project/Internal...), IFCFileType, ConfigName, CategoryMapping, PropertyMapping, ExportUserDefinedPsetsFileName, ExportUserDefinedParameterMappingFileName, ExcludeFilter, GeoRef* fields, SelectedSite, ExportingLinks.
- Numbers/IDs: ActivePhaseId, ActiveViewId/HostViewId, TessellationLevelOfDetail (double).
Defaults when an option is absent: Shared coordinates, Low detail, no steel for non-2x3, `ExportingLinks` = don't export [11]. Tip: to reproduce a saved UI setup, read its JSON from the DataStorage schema or call `IFCExportConfiguration.UpdateOptions` [9][10].

### Dynamo
A Dynamo Python or C# node can call the same API; community packages wrap it (no package named here to avoid unverified claims) (unverified).

### pyRevit
pyRevit is a GPL-3.0 rapid-development environment for Revit with Python (IronPython/CPython), C# and VB.NET scripting [27]; scripts call `doc.Export(...)` with `DB.IFCExportOptions()` for batch folder export (usage unverified).

### Design Automation for Revit (Autodesk Platform Services)
Cloud Revit engine runs add-in bundles headless; exporting IFC there means the app bundle must call the API and, to use the open-source exporter behaviour, the matching IFC add-on must be present in the engine; which engine versions and whether the IFC add-on is bundled could not be verified (unverified). Pages: aps.autodesk.com docs were JavaScript-only [28].

## 10. Known problems and fixes

| Symptom | Likely cause | Fix / workaround | Source |
|---|---|---|---|
| Everything is IfcBuildingElementProxy | Category not mapped, or Generic Model, or mapping template lost | Set Category Mapping or "Export to IFC As" on type/instance | [17] |
| Properties missing from pset | Wrong setup (mapping disabled by new parameter mapping mode), user pset file not selected, parameter not text/typed | Check Property Mapping tab; use full name `Pset_X.Prop` | [9][22] |
| IfcLogical property exports UNKNOWN | Yes/No parameter with short name not matched | Name the parameter `Pset_BuildingStoreyCommon.AboveGround` (full name) (issue open) | [22] |
| Built-in value overrides shared parameter with same name | Case-insensitive name collision in mapping | Rename shared parameter; (issue open, tracked internally) | [21] |
| Cannot export to network folder ("no write access") | ACL pre-check in 26.1+/27 add-ons | Export locally then copy; 27.3.0.12 lists a network-location fix, but #981 remains open | [4][23] |
| IFC4.3 RV header says CoordinationView | Bug in 2026 add-on | Fixed in 2027; manual header edit possible but not conformance-proof | [24] |
| Walls with joined masses/door frames wrong in Revit 2026 | Join geometry regression | Try Revit 2027 add-on; provide sample to Autodesk | [25] |
| Model far from origin / wrong location | Coordinate base wrong or shared coordinates not set | Pick Shared/Project Base Point; check survey point; use IfcMapConversion (IFC4) | [9][8] |
| Duplicated MEP fabrication parts, ramps as IfcSlab | Exporter bugs | Fixed in 27.3.0.12 | [4] |
| Rooms shifted | geometry bug | Fixed in 27.0.1.1 / 27.3.0.12 | [2][4] |
| Windows/doors outside walls on import; 2D symbols affect placement | open issues #1019, #1018 | check 2D symbols/annotation inside families | [20] |
| Huge file / slow | high LOD, linked files, 2D elements | Lower Level of Detail, untick "Export 2D plan view elements", export visible view only | [14] |
| Export aborts with "unrecoverable error" | open issue #1021; curtain wall access violation #992 | Try latest add-on; split by view | [20] |

## 11. Typical questions people ask about this

Real (from the repo issue tracker, 2026):
1. "IFC export ignores the mapping table for parameters with the same name as built-in ones" – issue #989 [21].
2. "Yes/No parameter AboveGround not exported to Pset_BuildingStoreyCommon, shows UNKNOWN" – #1020 [22].
3. "Export to network folder fails with a write-permission message though I can write there" – #981 [23].
4. "IFC4x3 Reference View writes CoordinationView in FILE_DESCRIPTION" – #1013 [24].
5. "Revit 2026 export of walls joined with masses is wrong, but fine in 2027" – #1014 [25].
6. "Doors and windows sit outside the wall face after export/import" – #1019 [20].
7. "IfcObjectType is ignored for IfcCivilElement" – #1009 [20].
8. "Furnishing exported as IfcFurnishingElement with IfcFurnitureType" – #1007 [20].
9. "Unrecoverable error during export, export aborted" – #1021 [20].

Illustrative (invented to cover usual QA cases):
10. Which IFC version should I choose for coordination with an architect (illustrative)?
11. What is the difference between IFC2x3 CV2.0 and IFC4 Reference View (illustrative)?
12. How do I make all my Generic Models export as IfcFurniture (illustrative)?
13. How do I export only the selected view/phase (illustrative)?
14. Why are my custom parameters missing in the IFC (illustrative)?
15. How do I keep the same GlobalId on every re-export (illustrative)?
16. How do I export with the survey point coordinates (illustrative)?
17. How do I export each linked model as a separate IFC (illustrative)?
18. How do I set a pset such as Pset_WallCommon.FireRating from a shared parameter (illustrative)?
19. Can I automate IFC export for 50 projects overnight (illustrative)?
20. Why is IfcSpace missing or has no geometry (illustrative)?
21. What do "Export Revit property sets" and "Export IFC common property sets" produce, and which should I leave on (illustrative)?
22. How do I export COBie (illustrative)?

QA tip for MCP servers: a good test prompt asks the tool to set one specific option (e.g. coordinate base = Project Base Point, base quantities on, IFC4 RV Architecture), perform an export, then verify in the output file (header `FILE_SCHEMA`, `FILE_DESCRIPTION` ViewDefinition, presence of `Qto_*` sets, `IFCMAPCONVERSION` for IFC4).

## 12. Common pitfalls and misconceptions

- "IFC is a Revit file format." No; IFC is an open standard. The Revit exporter produces IFC using its own mapping rules, which differ between setups.
- "More psets is better." Enabling Revit property sets, common sets and base quantities together makes files large and duplicates values; the new Property Mapping mode ignores the legacy checkboxes [9].
- Setups live inside the .rvt, not the user profile [10]. A colleague's machine may show different setups.
- Reference View is read-oriented and not for round-trip editing; Design Transfer View is marked unofficial [14].
- Coordinate base defaults to Shared Coordinates [9]; with default Revit templates (project base point at internal origin) people often get models at the wrong place in a GIS/federated view.
- Predefined type, class and type-level override interplay: instance beats type [17].
- Revit 2026 and 2027 add-ons differ; verify the add-on version, not only the Revit year [2].
- `IncludeSteelElements` only affects IFC2x3 in the cache logic; the code comment says default true but the code defaults to false when the option is omitted [11].
- Header text editing does not make a file conformant [24].
- The IFC4.3 schema in Revit is written as `IFC4X3_ADD2` [24].

## Gaps

- Web-search quota was exhausted; no new searches were possible, so no community blogs/forums (Revit forums, Building Coder, BIM blogs) were consulted.
- Not readable: Autodesk help pages (JavaScript only, including the "IFC in Revit" page linked from the README), blogs.autodesk.com IFC Manual post (403/redirect), buildingSMART technical pages (403), APS Design Automation docs (JS only), pyRevit docs (JS only). The default category mapping table and the sample user-defined pset files were not located in the repository tree; the syntax and class table in this file come from memory and are marked (unverified).
- No suspicious or pirated sites were encountered.
- Release dates on GitHub were shown without years.

## Sources

[1] https://github.com/Autodesk/revit-ifc – README summary, support policy, license
[2] https://github.com/Autodesk/revit-ifc/releases – list of releases
[3] https://github.com/Autodesk/revit-ifc/releases/tag/IFC_v27.4.0.30
[4] https://github.com/Autodesk/revit-ifc/releases/tag/IFC_v27.3.0.12
[5] https://github.com/Autodesk/revit-ifc/releases/tag/IFC_v27.0.1
[6] https://github.com/Autodesk/revit-ifc/wiki
[7] https://github.com/Autodesk/revit-ifc/wiki/Revit-IfcExporter-parameter-expression
[8] https://github.com/Autodesk/revit-ifc/wiki/Mapping-geo-reference-in-IFC4 (images only)
[9] https://raw.githubusercontent.com/Autodesk/revit-ifc/master/Source/Revit.IFC.Export/Utility/IFCExportConfiguration.cs
[10] https://raw.githubusercontent.com/Autodesk/revit-ifc/master/Source/Revit.IFC.Export/Utility/IFCExportConfigurationsMap.cs
[11] https://raw.githubusercontent.com/Autodesk/revit-ifc/master/Source/Revit.IFC.Export/Utility/ExportOptionsCache.cs
[12] https://raw.githubusercontent.com/Autodesk/revit-ifc/master/Source/Revit.IFC.Common/Enums/CommonEnum.cs
[13] https://raw.githubusercontent.com/Autodesk/revit-ifc/master/Source/Revit.IFC.Common/Enums/IFCKnownMVDAndER.cs
[14] https://raw.githubusercontent.com/Autodesk/revit-ifc/master/Source/IFCExporterUIOverride/Properties/Resources.resx
[15] https://raw.githubusercontent.com/Autodesk/revit-ifc/master/Source/IFCExporterUIOverride/IFCVersionExtensions.cs
[16] https://raw.githubusercontent.com/Autodesk/revit-ifc/master/Source/IFCExporterUIOverride/IFCFileFormatAttributes.cs
[17] https://raw.githubusercontent.com/Autodesk/revit-ifc/master/Source/Revit.IFC.Export/Utility/ExporterUtil.cs
[18] https://raw.githubusercontent.com/Autodesk/revit-ifc/master/README.md – build, branches, doc links (also links https://blogs.autodesk.com/revit/2022/02/09/now-available-revit-ifc-manual-version-2-0/ and https://help.autodesk.com/view/RVT/2024/ENU/?guid=GUID-6EB68CEC-6C17-4B16-A509-30537F666C1F, not readable here)
[19] Repository directory listings: https://github.com/Autodesk/revit-ifc/tree/master/Source , .../Source/Revit.IFC.Export/Exporter , .../Exporter/PropertySet , .../PropertySet/Calculators , .../Source/IFCExporterUIOverride , .../IFCPropertyMapping , .../IFCCategoryMapping
[20] https://github.com/Autodesk/revit-ifc/issues – open issues list
[21] https://github.com/Autodesk/revit-ifc/issues/989
[22] https://github.com/Autodesk/revit-ifc/issues/1020
[23] https://github.com/Autodesk/revit-ifc/issues/981
[24] https://github.com/Autodesk/revit-ifc/issues/1013
[25] https://github.com/Autodesk/revit-ifc/issues/1014
[27] https://github.com/pyrevitlabs/pyRevit
[28] https://aps.autodesk.com/en/docs/design-automation/v3/developers_guide/overview/ (content not readable)
