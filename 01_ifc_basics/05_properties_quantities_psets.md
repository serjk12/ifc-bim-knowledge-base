# Properties, quantities and property sets (Pset_, Qto_)

## In plain words

An IFC model is not only geometry. Almost everything a person wants to filter, schedule or check (fire rating, "is this wall external?", wall area, manufacturer) lives in **property sets** (`IfcPropertySet`, names like `Pset_WallCommon`) and **quantity sets** (`IfcElementQuantity`, names like `Qto_WallBaseQuantities`). A property set is a named container of name/value pairs attached to an element (an "occurrence", for example one wall) or to its type (for example "Wall type 200 mm concrete"). Standard sets use the reserved `Pset_` / `Qto_` prefixes and fixed property names defined by buildingSMART; your own sets must use a different name. For an MCP tester: most "read/edit property" requests boil down to "find the right set name + property name + value type, on the right object (type or occurrence)", and most failures are a wrong set name, a wrong value type, or editing the type when the occurrence overrides it.

Last researched: 2026-11-06

> Research caveat: the buildingSMART documentation site (`standards.buildingsmart.org`, `ifc43-docs.standards.buildingsmart.org`) returned HTTP 403 to direct page fetches during the first research pass (note: `ifc43-docs...` now answers with a 301 redirect to `standards.buildingsmart.org/IFC/DEV/IFC4_3/HTML/...`, which is the 4.3.2.0 "under development" build and also returns 403 to scripts). Property lists below were first taken from search-engine summaries and the GitHub documentation sources. **QA pass 2026-11-06:** every Pset/Qto row in sections 3 and 4 was re-checked against the property-set and quantity-set pages of the buildingSMART documentation mirror hosted at `bsi-infraroom.github.io/IFC-Documentation-Tunnel/4_4_0_0/...` [40] (this is the IFC 4.4.0.0 working draft, so lists may differ slightly from the frozen 4.3.2.0 release; differences are flagged "(4.4 draft mirror)"). Anything still not confirmed is marked "(unverified)". Always verify an exact property name in the official docs before putting it in an automated test.

---

## 1. The property model

### 1.1 Containers

| Concept | IFC entity | Notes |
|---|---|---|
| Property set | `IfcPropertySet` | Container of `IfcProperty` subtypes in attribute `HasProperties`. `Name` is mandatory; property names inside one set must be unique (formal rules ExistsName, UniquePropertyNames) [4] |
| Quantity set | `IfcElementQuantity` | Container of `IfcPhysicalQuantity` (length, area, volume, weight, count, time). Optional `MethodOfMeasurement`; quantity names unique within the set [13] |
| Assignment to an occurrence | `IfcRelDefinesByProperties` | N-to-N: one relationship can attach several sets to several objects [5] |
| Assignment to a type | `IfcTypeObject.HasPropertySets` (direct attribute, no relationship) | Every set name on a type must be unique [7] |
| Occurrence-to-type link | `IfcRelDefinesByType` | Occurrence inherits the type's sets [6] |
| Template of a standard set | `IfcPropertySetTemplate` via `IfcRelDefinesByTemplate` | Machine-readable definition of "what Pset_WallCommon should contain" [4] (template details unverified beyond the relationship name) |

Standard (predefined) sets: since IFC4 they are no longer separate entity subtypes of `IfcPropertySet`; they are ordinary `IfcPropertySet` instances whose `Name` equals the standard name [4]. A predefined property that is not set is interpreted as "no value" [4].

### 1.2 Property kinds

All are subtypes of `IfcSimpleProperty` (plus `IfcComplexProperty` for nested groups) in the property resource schema [14] (the GitHub folder lists IfcComplexProperty, IfcPropertyBoundedValue, IfcPropertyEnumeratedValue, IfcPropertyListValue, IfcPropertyReferenceValue, IfcPropertySingleValue, IfcPropertyTableValue).

| Kind | Entity | What it holds | Typical example |
|---|---|---|---|
| Single value | `IfcPropertySingleValue` | One `NominalValue` typed by a measure type, optional `Unit` | `FireRating = IFCLABEL('REI60')`, `IsExternal = IFCBOOLEAN(.T.)` |
| Enumerated | `IfcPropertyEnumeratedValue` | One or more values chosen from an `IfcPropertyEnumeration` (referenced via `EnumerationReference`); the enumeration also fixes the unit. `EnumerationValues` optional since IFC4; each value must be a member of the referenced enumeration (rule WR21) [10] | `Status = PEnum_ElementStatus: NEW` (enum name pattern `PEnum_...` seen in standard docs) |
| Bounded | `IfcPropertyBoundedValue` | `UpperBoundValue`, `LowerBoundValue` (both inclusive, either may be missing = open interval), optional `Unit`, `SetPointValue` (added IFC4). Both bounds must share a measure type; upper must exceed lower for numeric types [8] | Door `OverallHeight` 1930 to 2300 (example from the spec page) |
| List | `IfcPropertyListValue` | Ordered `ListValues`, all of the same type; optional since IFC4 [11] | Several standard widths: 1200, 1600, 2400 |
| Table | `IfcPropertyTableValue` | Two columns: `DefiningValues` (unique) and `DefinedValues`, optional units, `Expression` (informational only), `CurveInterpolation` (IFC4, linear assumed if absent). For 3+ columns the spec points to `IfcPropertyReferenceValue` + `IfcTable` [9] | Curve such as pressure vs flow |
| Reference | `IfcPropertyReferenceValue` | `UsageName` + `PropertyReference` pointing to another entity from the `IfcObjectReferenceSelect` select (allowed targets not listed on the page I read) [12] | A property that points to a material or a table |
| Complex | `IfcComplexProperty` | Named group of properties inside a set | Nested sub-properties (rare in practice) |

In practice, more than 95% of properties in real BIM exports are single values (this ratio is the author's observation, unverified); table/list/bounded values are rare and many authoring tools cannot create them (Archicad IFC property mapping supports "single value" properties only [28]).

### 1.3 Measure (value) types

The `NominalValue` of a single value is a typed wrapper. The ones a tester meets most:

| Type | Meaning | Example in the standard |
|---|---|---|
| `IfcLabel` | Short text | `FireRating` (national classification string, e.g. "REI60", "EI30", "F90" - format depends on country) [1] |
| `IfcIdentifier` | Short code/id | `ArticleNumber`, `Reference` [20] |
| `IfcText` | Long text | Descriptions (unverified for a specific property) |
| `IfcBoolean` | TRUE/FALSE | `IsExternal`, `LoadBearing`, `SmokeStop` [1][15] |
| `IfcLogical` | TRUE/FALSE/UNKNOWN | `AboveGround` on a storey: TRUE fully above ground, FALSE below, UNKNOWN partly both [18] |
| `IfcInteger`, `IfcReal` | Numbers without a physical unit | counts, ratios |
| `IfcLengthMeasure` / `IfcPositiveLengthMeasure` | Length | `Span` of a beam (clear span) [19] |
| `IfcAreaMeasure` | Area | `GrossPlannedArea`, `NetPlannedArea` on spaces and storeys [17][18] |
| `IfcPlaneAngleMeasure` | Angle | `PitchAngle` of a roof slab, `Slope` of a column [16][19] |
| `IfcThermalTransmittanceMeasure` | U-value | `ThermalTransmittance` of slab, door, window [16][15][21] |
| `IfcPositiveRatioMeasure` | Fraction (a ratio greater than 0) | `GlazingAreaFraction` of door/window [15][21][40] (QA fix: was written `IfcRatioMeasure`) |
| `IfcVolumetricFlowRateMeasure` | Flow rate | `Infiltration` of window and door (air leakage; "at 50 Pa" wording from the first-pass summary) [21][40] (QA fix: type name was written `IfcVolumeFlowRateMeasure`, which is not the IFC name) |

Units: if a property has no explicit `Unit`, the unit comes from the measure type and the project's global unit assignment (`IfcProject.UnitsInContext`); an explicit `Unit` overrides it [8][9][11]. Typical trap: a model in millimetres where a tool writes metres (or the reverse) because it ignored `UnitsInContext`. Tekla's property-set export needs manual conversion factors for area/volume (1E-06 and 1E-09 for mm-based values) or numbers come out wrong [31].

---

## 2. Type vs occurrence properties and override rules

* A **type** (`IfcWallType`, `IfcDoorType`...) carries sets via `HasPropertySets`. They are common to every occurrence [7].
* An **occurrence** (`IfcWall`) gets its own sets through `IfcRelDefinesByProperties` and inherits the type's sets through `IfcRelDefinesByType` [5][6].
* **Effective value = union of type and occurrence properties; same-named property on the occurrence wins.** The spec states that if the same property name appears in a property set on both the type and the occurrence, "the occurrence property overrides the type property" [7]. The override is **per property**, not per whole set: other type properties still apply [6]. The spec's example: type-level `ExtendToStructure = TRUE` overridden by an occurrence-level `FALSE` gives FALSE for that wall, while the type's `ThermalTransmittance` of 0.375 still applies to the wall because the wall does not override it [6] (QA fix: the first pass described `ThermalTransmittance` as an occurrence-level property that is "added"; in the spec example it is the *type's* value that remains in force).
* Three design scenarios from the spec [6]: (1) all occurrences identical -> pset only on the type; (2) all values differ -> pset on each occurrence; (3) mixed -> common properties on the type, varying ones on occurrences.
* Quantities are normally **per occurrence** (geometry differs per wall), so `Qto_*` sets are attached to occurrences. (Author's statement; the quantity-set page I read does not discuss type vs occurrence [13].)
* Practical consequence for tests:
  * "Set FireRating on this wall" - correct tools write to the occurrence; if a tool edits the type, all walls of that type change.
  * A reader that only looks at the occurrence's own psets will miss type-level values. Good MCP tools expose both and say which level a value came from (expected behaviour, not a standard requirement).
  * In IFC2x3 the same mechanism exists; the `HasPropertySets` list became a set in 2x3 [7].
* Revit-specific: since Revit IFC exporter 24.1.0 type properties are not exported unless declared in the user-defined property-set file [25]; from 25.2.0.5 `IsExternal` support "at type level" was removed [22].

---

## 3. Standard property sets - key properties

Documentation chapter numbers are from page titles of the IFC 4.3.2 documentation as shown by search results (e.g. "6.1.4.23 Pset_WallCommon"). The full list of building-element sets in the IFC4.3.x development repo includes: Pset_BeamCommon, Pset_BearingCommon, Pset_BuildingElementProxyCommon, Pset_BuildingSystemCommon, Pset_ChimneyCommon, Pset_ColumnCommon, Pset_CoveringCommon, Pset_CoveringFlooring, Pset_CurtainWallCommon, Pset_DoorCommon, Pset_DoorWindowGlazingType, Pset_MemberCommon, Pset_PlateCommon, Pset_RailingCommon, Pset_RampCommon, Pset_RampFlightCommon, Pset_RoofCommon, Pset_ShadingDeviceCommon, Pset_SlabCommon, Pset_StairCommon, Pset_StairFlightCommon, Pset_Tiling, Pset_WallCommon, Pset_WindowCommon [14].

| Pset | Applies to | Key properties (type) | Notes |
|---|---|---|---|
| `Pset_WallCommon` (6.1.4.23) [1] | `IfcWall`, `IfcWallStandardCase`, `IfcWallType` | **11 properties confirmed (4.4 draft mirror [40]):** `Reference` (IfcIdentifier, deprecated since 4.3.0.0), `Status` (enum PEnum_ElementStatus), `AcousticRating` (IfcLabel), `FireRating` (IfcLabel), `Combustible` (IfcBoolean), `SurfaceSpreadOfFlame` (IfcLabel), `ThermalTransmittance` (IfcThermalTransmittanceMeasure), `IsExternal` (IfcBoolean), `LoadBearing` (IfcBoolean), `ExtendToStructure` (IfcBoolean), `Compartmentation` (IfcBoolean). Only `Reference` carries a deprecation note | `IsExternal=TRUE` means the element faces the outside of the building |
| `Pset_DoorCommon` (6.1.4.10) [15] | `IfcDoor`, `IfcDoorType` | **19 properties confirmed [40]:** `Reference` (deprecated), `Status` (enum); ratings, all IfcLabel: `FireRating`, `AcousticRating`, `SecurityRating`, `DurabilityRating`, `HygrothermalRating`, `WaterTightnessRating`, `MechanicalLoadRating`, `WindLoadRating` (the last three added in IFC4 Add1); `Infiltration` (IfcVolumetricFlowRateMeasure); `ThermalTransmittance` (U-value); `GlazingAreaFraction` (IfcPositiveRatioMeasure); IfcBoolean flags: `IsExternal`, `HandicapAccessible`, `FireExit`, `HasDrive`, `SelfClosing`, `SmokeStop` | The IFC2x3 version had a smaller subset (FireRating, AcousticRating, SecurityRating, FireExit, SelfClosing, SmokeStop) |
| `Pset_WindowCommon` (6.1.4.24) [21] | `IfcWindow`, `IfcWindowType` | **17 properties confirmed [40]:** `Reference` (deprecated), `Status`, `AcousticRating`, `FireRating`, `SecurityRating`, `WaterTightnessRating`, `MechanicalLoadRating`, `WindLoadRating` (IfcLabel); `IsExternal`, `HasSillExternal`, `HasSillInternal`, `HasDrive`, `SmokeStop`, `FireExit` (IfcBoolean); `Infiltration` (IfcVolumetricFlowRateMeasure), `ThermalTransmittance`, `GlazingAreaFraction` | Note: there is **no** `LoadBearing` or `SelfClosing` on windows |
| `Pset_SlabCommon` (6.1.4.19) [16] | `IfcSlab`, `IfcSlabType` | **11 properties confirmed [40]:** `Reference` (deprecated), `Status`; `AcousticRating`, `FireRating`, `SurfaceSpreadOfFlame` (IfcLabel); `PitchAngle` (IfcPlaneAngleMeasure, roof slabs, geometry wins on conflict, "write-only" for CAD); `Combustible`, `Compartmentation`, `IsExternal`, `LoadBearing` (IfcBoolean); `ThermalTransmittance` (U-value across all layers) | |
| `Pset_SpaceCommon` (5.4.4.21) [17] | `IfcSpace` | **6 properties confirmed [40]:** `Reference` (deprecated), `IsExternal`, `PubliclyAccessible`, `HandicapAccessible` (IfcBoolean); `GrossPlannedArea`, `NetPlannedArea` (IfcAreaMeasure, programming/briefing areas) | `IfcSpace.IsExternal` attribute is deprecated in favour of the Pset property. IFC2x3 had a `Category` property; confirmed that the 4.3/4.4 set has no category property. Real area comes from `Qto_SpaceBaseQuantities`, not from the planned areas |
| `Pset_BuildingStoreyCommon` (5.4.4.8) [18] | `IfcBuildingStorey` | `EntranceLevel` (Boolean), `AboveGround` (Logical), `SprinklerProtection` (Boolean), `SprinklerProtectionAutomatic` (only meaningful when SprinklerProtection is TRUE), `GrossPlannedArea`, `NetPlannedArea` (IfcAreaMeasure). The 4.4 draft mirror [40] additionally lists `Reference` (deprecated), `LoadBearingCapacity` (IfcPlanarForceMeasure), `ElevationOfSSLRelative` and `ElevationOfFFLRelative` (IfcLengthMeasure, structural / finished floor level relative to the storey) - whether these three are already in the frozen 4.3.2.0 is (unverified) | IFC2x3 names were `GrossAreaPlanned` / `NetAreaPlanned`. Storey elevation is the attribute `IfcBuildingStorey.Elevation`, not a pset |
| `Pset_ColumnCommon` (6.1.4.6) [19] | `IfcColumn`, `IfcColumnType` | **8 properties confirmed [40]:** `Reference` (deprecated), `Status` (enum PEnum_ElementStatus: New, Existing, Demolish, Temporary), `Slope` and `Roll` (IfcPlaneAngleMeasure; slope is relative to horizontal), `IsExternal`, `LoadBearing` (IfcBoolean), `ThermalTransmittance`, `FireRating` (IfcLabel) | QA fix: first pass omitted `Roll` and `ThermalTransmittance` |
| `Pset_BeamCommon` (6.1.4.1) [19] | `IfcBeam`, `IfcBeamType` | **9 properties confirmed [40]:** `Reference` (deprecated), `Status`, `Span` (IfcPositiveLengthMeasure, clear span), `Slope`, `Roll` (IfcPlaneAngleMeasure; Roll is measured relative to global Z, new in IFC4), `IsExternal`, `ThermalTransmittance`, `LoadBearing`, `FireRating` | A search-engine summary of the official 4.3.2 page listed only 8 properties (no `Status`); the draft mirror lists `Status` - treat `Status` as present but check the frozen 4.3.2 page if exactness matters |
| `Pset_CoveringCommon` [Annex B list, search] | `IfcCovering` (ceilings, floor finishes, cladding) | **11 properties confirmed [40]:** `Reference` (deprecated), `Status`, `AcousticRating`, `FlammabilityRating`, `FragilityRating`, `FireRating` (IfcLabel), `Combustible` (IfcBoolean), `SurfaceSpreadOfFlame` (IfcLabel), `Finish` (IfcText), `IsExternal` (IfcBoolean), `ThermalTransmittance` | QA fix: `TotalThickness` (listed "from memory" in the first pass) is **not** in this set; `FragilityRating` was missing. Thickness of a covering is a layer/geometry matter or `Qto_CoveringBaseQuantities.Width` |
| `Pset_RoofCommon` (6.1.4.17) [19] | `IfcRoof`, `IfcRoofType` | **7 properties confirmed [40]:** `Reference` (deprecated), `Status`, `AcousticRating`, `IsExternal`, `ThermalTransmittance`, `LoadBearing`, `FireRating` | QA fix: `ProjectedArea` and `TotalArea` appear only in the change-history note (added in IFC2x3) and are **not** properties of the IFC4.3/4.4 set; projected/gross/net roof area live in `Qto_RoofBaseQuantities` (`GrossArea`, `NetArea`, `ProjectedArea`) |
| `Pset_ManufacturerTypeInformation` (6.4.4.15) [20] | Types (e.g. `IfcFlowController`, `IfcRoof`, `IfcPipeFitting` types and many more) | **10 properties confirmed [40]:** `GlobalTradeItemNumber` (IfcIdentifier), `ArticleNumber` (IfcIdentifier, "often the purchasing number"), `ModelReference` (IfcLabel, manufacturer model number), `ModelLabel` (IfcLabel), `Manufacturer` (IfcLabel), `ProductionYear` (IfcLabel - text, not a number), `AssemblyPlace` (enum PEnum_AssemblyPlace: factory / off-site / site; added in IFC4, "IFC 2x4" in the page history), `OperationalDocument` (reference value, IfcExternalReference), `SafetyDocument`, `PerformanceCertificate` (reference values, IfcDocumentReference) | Replaced the old `IfcManufacturerInformation` entity. Reads like a datasheet block - very common in product libraries. The page does not say in which release `GlobalTradeItemNumber` and the three document references were added (first pass said "IFC4.3 adds", (unverified)) |

Related general-purpose sets worth knowing (unverified list from memory, presence confirmed only where cited): `Pset_BuildingCommon` [18], `Pset_SiteCommon`, `Pset_BuildingUse`, `Pset_ElementShading`, `Pset_ProductRequirements`, `Pset_Condition`, `Pset_EnvironmentalImpactIndicators`.

---

## 4. Base quantities (Qto_)

* `IfcElementQuantity` with `MethodOfMeasurement = 'BaseQuantities'` is the "base quantity" set. Base quantities are independent of any national measurement method, are published with fixed names, are defined as gross and net values and derived from the element's shape representation; the set `Name` equals the quantity-set template name (e.g. `Qto_WallBaseQuantities`) [13]. In IFC2x3 the set was typically just called `BaseQuantities`; since IFC4 each element class has its own `Qto_` name (naming history from memory plus the Tekla IFC2x3/IFC4 lists, partly unverified).
* A custom or national method uses another `MethodOfMeasurement`, e.g. German DIN 277-2 net floor area or Wohnfläche (2. BV) (`2.BV` is the old German living-area ordinance) [13]. One element can carry several quantity sets for different methods [13].
* **Gross vs net**: gross ignores openings/recesses/projections; net subtracts them (openings, recesses, connections) [2].

| Qto set | Applies to | Quantities (type) |
|---|---|---|
| `Qto_WallBaseQuantities` (6.1.5.15) [2][3] | `IfcWall`, `IfcWallStandardCase`, `IfcWallType` | `Length` (along the centre line even if the wall path differs), `Width` (perpendicular to the wall path, only when constant), `Height` (nominal total height, only if constant), `GrossFootPrintArea`, `NetFootPrintArea` (spelled with a capital P in the standard; QA fix, first pass wrote "Footprint"), `GrossSideArea` (elevation area of the middle plane, ignoring openings), `NetSideArea` (accounting for openings), `GrossVolume` (no openings/recesses/enclosed objects/projections), `NetVolume` (after openings and connection geometry), `GrossWeight`, `NetWeight` (Q_WEIGHT; confirmed in the 4.4 draft mirror [40], not checked on the frozen 4.3.2 page) |
| `Qto_WindowBaseQuantities` (6.1.5.16) [21] | `IfcWindow` | `Width`, `Height`, `Perimeter` (IfcQuantityLength), `Area` (IfcQuantityArea) (confirmed [40]) |
| `Qto_DoorBaseQuantities` | `IfcDoor` | Confirmed [40]: `Width`, `Height`, `Perimeter` (lengths), `Area` (area) |
| `Qto_BuildingStoreyBaseQuantities` (5.4.5.2) [18] | `IfcBuildingStorey` | `GrossHeight`, `NetHeight` (only when constant), `GrossPerimeter`, `GrossFloorArea` (includes construction elements), `NetFloorArea` (excludes them), `GrossVolume`, `NetVolume` (exactly these 7 confirmed [40]) |
| `Qto_BuildingBaseQuantities` (5.4.5.1) [search result] | `IfcBuilding` | Gross/net floor area, volume, footprint (details unverified) |
| `Qto_SlabBaseQuantities` | `IfcSlab` | Confirmed [40], 10 quantities: `Width`, `Length`, `Depth`, `Perimeter` (lengths), `GrossArea`, `NetArea`, `GrossVolume`, `NetVolume`, `GrossWeight`, `NetWeight` |
| `Qto_SpaceBaseQuantities` | `IfcSpace` | Confirmed [40], 13 quantities: lengths `Height`, `FinishCeilingHeight`, `FinishFloorHeight`, `GrossPerimeter`, `NetPerimeter`; areas `GrossFloorArea`, `NetFloorArea`, `GrossWallArea`, `NetWallArea`, `GrossCeilingArea`, `NetCeilingArea`; volumes `GrossVolume`, `NetVolume` |
| `Qto_BeamBaseQuantities`, `Qto_ColumnBaseQuantities` | `IfcBeam`, `IfcColumn` | Confirmed [40], identical 9 quantities each: `Length`, `CrossSectionArea`, `OuterSurfaceArea`, `GrossSurfaceArea`, `NetSurfaceArea`, `GrossVolume`, `NetVolume`, `GrossWeight`, `NetWeight` |
| `Qto_CoveringBaseQuantities` | `IfcCovering` | Confirmed [40], 3 quantities: `Width` (length), `GrossArea`, `NetArea` |
| `Qto_RoofBaseQuantities` | `IfcRoof` | Confirmed [40], 3 areas: `GrossArea`, `NetArea`, `ProjectedArea` (roof projected onto the ground plan) |

The Tekla IFC4 list also confirms that these `Qto_` names are exported by that tool [31].

Quantity value entities: `IfcQuantityLength`, `IfcQuantityArea`, `IfcQuantityVolume`, `IfcQuantityWeight`, `IfcQuantityCount`, `IfcQuantityTime` (subtypes of `IfcPhysicalSimpleQuantity`) [13].

**Quantities are exported numbers, not live formulas.** Editing geometry after export or in an MCP tool does not recompute a `Qto_` set unless the tool does it. Autodesk states Revit base quantities "are generated from model geometry to reflect actual physical quantity values" independent of measurement rules, so they can differ from Revit schedules that follow other rules [22].

---

## 5. Custom property sets - naming conventions

| Rule | Source |
|---|---|
| `Pset_` is reserved for property sets defined in the IFC specification; a user-defined set must not carry the `Pset_` prefix | IfcPropertySet definition [4]; IfcOpenShell API docs [36]; Graphisoft guidance [29]; Tekla [31] |
| Standard quantity sets use `Qto_`; custom ones should not | pattern from standard names; explicit rule not found on the pages I could read (unverified) |
| Enumerations conventionally use `PEnum_` | seen in `PEnum_ElementStatus`, `PEnum_AssemblyPlace` |
| Property names inside a set must be unique | UniquePropertyNames [4] |
| A blank property set is invalid in IFC | IfcOpenShell docs [36] |
| Do not store a standard property under a custom set name (e.g. fire rating in `MyCompany_Wall`) if a standard property exists; use the standard one | recommended practice (author, unverified) |

Common real-world custom names: `COBie_Specification` (type-level, from the Revit exporter template [25]), `AC_Pset_RenovationAndPhasing` (Archicad predefined [28]), company/project prefixes such as `ACME_Wall`, national sets (e.g. national classification or cost-code sets), Revit-generated sets from groups like "Dimensions", "Identity Data", "Constraints" (when "Export Revit property sets" is on [22]). Avoid spaces and special characters in names used by automated tools (practical tip, unverified).

---

## 6. How authoring tools map parameters to psets

### 6.1 Revit (Autodesk IFC exporter, open source `Autodesk/revit-ifc`)

* Export options, Property Sets tab (names as in Autodesk's IFC help) [22]:
  * **Export Revit property sets** - exports Revit parameters grouped by Revit parameter group; off by default and noisy [22].
  * **Export IFC Common property sets** - writes the standard `Pset_*Common` sets (on by default) [22]. (Exact label capitalisation per the 25.2 help page; the Revit 25.2 help page lists exactly these six property-set options, checked 2026-11-06.)
  * **Export base quantities** - writes `Qto_`/BaseQuantities from model geometry [22].
  * **Export schedules as property sets** - the schedule name becomes the pset name, column names become property names; the companion option "Export only schedules containing IFC, Pset, or Common in the title" limits it [22].
  * **Export user defined property sets** - uses a TXT mapping file [22][23].
  * **Export user defined parameter mapping table** (label per the exporter resource file; not on the 25.2 help page) - maps your own Revit parameters onto standard IFC property names, only when the data types match [search summary of Autodesk knowledge article, 27]. The Revit 2027 help describes the newer "Manage IFC Export User Defined Property Sets" dialog, where sets can be duplicated, edited, saved and exchanged as `.txt` files [24].
* **User-defined property set file** (TXT, tab-separated, UTF-8) [23][25]:
  ```
  #PropertySet:	ColumnPSet	I	IfcColumn, IfcColumnType
  #	CommentsProp		Text	Comments
  ```
  Header: `#PropertySet:` + set name + `I` (instance) or `T` (type) + comma-separated IFC classes; property rows: IFC property name, data type (Text, Boolean, Integer, Real, Label, Length, Area, Volume, Count, Time...; the shipped template lists the full set of supported types, starting "Acceleration, AngularVelocity, Area, AreaDensity, Boolean..."), optional Revit parameter name if different [25]. Verified QA 2026-11-06: the Autodesk Revit 2025 help page says the header and property lines are tab-separated, and that "starting in 2024.1" the I/T flag is not required (you can use `I`) [23]; the template header in the repository confirms that since version 24.1.0 type properties are not exported unless the type entity (e.g. `IfcElementType`) is named in the file [25].
  Known snags (from community search results, titles only; see section 9): IFC class names are case-sensitive (`IfcProject`, not `ifcProject`) and fields must be separated by real TAB characters (neither is stated in the template header; community-reported, (unverified)); Boolean mapping was reported unreliable by some users, who used Text instead (unverified).
* **Defaults** the exporter produces for common parameters (from vendor/manual knowledge, unverified for each version): Revit "Fire Rating" -> `FireRating`; wall Function = Exterior -> `IsExternal` (Autodesk notes `IsExternal` handling improved in 25.2.0.5 and was removed at type level [22]); structural flag -> `LoadBearing`; type name -> `Reference` (option "Use family and type name for references" [22]).
* Special Revit parameters controlling export (from memory, unverified): `IfcExportAs`, `IfcExportType`, `IfcName`, `IfcDescription`, `IfcGUID`.
* Revit file menu path (from memory, unverified on an Autodesk page: the help pages fetched on 2026-11-06 only say "Export a Model to IFC" without a path): File > Export > IFC; "Modify setup..." opens the dialog with the Property Sets tab; "Manage IFC Export User Defined Property Sets" dialog exists in Revit 2027 help (confirmed) [24].
* IFC versions in Revit export (QA 2026-11-06, from the open-source exporter's release notes and resource file, see `../03_software/revit/ifc_export_reference.md`): IFC2x3 Coordination View 2.0, IFC4 Reference View, IFC4 Design Transfer View [Unofficial], and since add-on 26.4.1 (18 Dec 2025; backported to 25.4.40 and 24.3.40 on 14 Jan 2026) also IFC4.3 Reference View.

### 6.2 Archicad (Graphisoft)

* Properties come from **Property Mapping** in the IFC translators ("Map IFC Properties for Export") [28][29]. Available standard property sets depend on the element's **Classification** (a Wall classified as Wall becomes `IfcWall` and offers `Pset_WallCommon`; a Column offers `Pset_ColumnCommon`) [29].
* **Predefined mappings** (do not appear in the mapping dialog; shown with a grey chain icon in IFC Project Manager / Element Settings): Structural Function -> `Pset_...Common.LoadBearing`; Position (exterior/interior) -> `...IsExternal`; Renovation Status -> `AC_Pset_RenovationAndPhasing`; column/beam reference -> `Pset_ColumnCommon.Reference` / `Pset_BeamCommon.Reference` generated by an automatic naming rule; Site Gross Area -> `BaseQuantity>GrossLandArea`; door/window width/height -> `OverallWidth`/`OverallHeight` attributes [28].
* Custom property sets: avoid the `Pset` prefix [29]. Mapping works for **single-value** properties only; table-type properties are not supported [29].
* On IFC import the default is to import all IFC properties as IFC properties (skipping the mapping table), which means they are not usable for graphic overrides, expressions or collision detection until mapped to Archicad Properties [29].

### 6.3 Tekla Structures (Trimble)

* IFC2x3 export is **configuration-driven** (XML property-set configuration files); IFC4 export has **hard-coded** default psets and quantities (`Pset_BeamCommon`, `Pset_ColumnCommon`, `Pset_SlabCommon`, `Pset_WallCommon`, `Pset_PlateCommon`, `Pset_MemberCommon`, `Pset_FootingCommon`, `Pset_PileCommon`, `Pset_ReinforcingBarCommon`, `Pset_ReinforcingMeshCommon`...; `Qto_BeamBaseQuantities`, `Qto_ColumnBaseQuantities`, `Qto_SlabBaseQuantities`, `Qto_WallBaseQuantities`, ...) [31]; additional sets (including rules) can be added for both schemas as of Tekla 2022 [32 / release notes in search results].
* Additional sets: File > Export > IFC / IFC4 > "Additional property sets" > `<new>` > Edit; choose entity category, IFC entity type, then attributes; attributes can be **template attributes** (from `contentattributes_global.lst`) or **UDAs** (from the environment database); UDA names longer than 19 characters must use Template attribute; to export a UDA as a string use prefix `USERDEFINED.`, property type Template attribute, type String [31].
* Gotchas [31]: wrong Type makes the pset export fail; missing value means the whole pset is not written unless `optional=true`; one definition per `ReferenceId`; psets created before Tekla 2022 apply only to the Structural category; the source page itself spells `Pset_BuildingElementProxymCommon` (typo in the source, the standard name is `Pset_BuildingElementProxyCommon`).
* Tekla 2026 adds **attribute overrides** for IFC attributes such as Name, Description, Tag (stored as `.attributeoverride` under `IfcAttributeOverrides` in the model folder; GlobalId is hard-coded) [33].

### 6.4 Others (brief)

* IfcOpenShell/Bonsai: `ifcopenshell.api.pset.add_pset(file, product, name)` creates an empty named set (a TypeError is raised if the class cannot have psets), then `edit_pset` adds properties; `add_qto`/`edit_qto` exist for quantity sets; example from the docs: a wall type receives `Pset_WallCommon` with `FireRating = "2HR"` [36].
* FreeCAD, BlenderBIM/Bonsai, Allplan, Vectorworks, Bentley: not researched here (gap).

---

## 7. bSDD linkage

* The buildingSMART Data Dictionary (bSDD) provides classes and properties with URIs; IFC and IDS can reference them [34].
* In IFC, a bSDD **class** is attached through `IfcClassification` + `IfcClassificationReference` + `IfcRelAssociatesClassification` (assigns a classification item to object occurrences or types) [34][39]. bSDD dictionary name -> `IfcClassification.Name`; dictionary URI -> `IfcClassification.Specification` (IFC4.3) or `.Location` (IFC4); IFC2x3 has no direct equivalent [34].
* bSDD **properties** map to IFC properties grouped into `IfcPropertySet` [34]:
  * bSDD `PropertyCode` -> `IfcPropertySingleValue.Name` (in IFC4x3, IFC4, IFC2x3). The human-readable name is not written, so datasets stay language independent [34].
  * bSDD property URI -> `IfcPropertySingleValue.Specification` (IFC4x3) or `.Description` (IFC4 / IFC2x3) [34].
  * predefined value -> `NominalValue`; unit -> `Unit`; allowed values -> `IfcPropertyEnumeratedValue.EnumerationValues`; property set name -> `IfcPropertySet.Name` [34].
  * Example from the bSDD doc: `#1=IFCPROPERTYSINGLEVALUE("EF021146", "https://identifier.buildingsmart.org/uri/etim/etim/9.0/prop/EF021146", $, $);` [34].
* URI pattern: `http://identifier.buildingsmart.org/uri/<OrganizationCode>/<DictionaryCode>/<DictionaryVersion>/prop/<PropertyCode>` [34].
* Properties exist independently of classes; class-level allowed values override property-level ones; the bSDD `PropertySet` field of a class property says in which set it should be serialised to IFC [34][35].
* IDS 1.0 uses `ids:property` with `uri`, `propertySet` (e.g. `Pset_ManufacturerTypeInformation`), `baseName` (e.g. `Manufacturer`) [34]. Useful for "does this model satisfy requirement X" tests.

---

## 8. Common pitfalls and misconceptions

1. **Custom set named `Pset_...`.** The prefix is reserved; tools (IfcOpenShell docs, Graphisoft, Tekla) warn against it [4][36][29][31]. Validators may flag it as non-standard.
2. **Type vs occurrence confusion.** Editing the type changes all occurrences; an occurrence value silently overrides the type value for the same property name [6][7]. Revit 24.1+ also stopped exporting type properties unless declared [25].
3. **Empty or partially filled sets.** Blank psets are invalid [36]; a predefined property that is not set means "no value", not FALSE [4]. Tekla does not write a pset at all if one property lacks a value [31]. For booleans, "missing" is not the same as FALSE; `IfcLogical` also has UNKNOWN [18].
4. **Wrong value type.** `FireRating` is a text label (national classification, e.g. "REI60" or "2HR"), not a number of minutes [1]; `ProductionYear` is `IfcLabel` text [20]; `AboveGround` is Logical [18]. Mapping tables in Revit require matching data types [27].
5. **Units.** Property units come from `IfcProject.UnitsInContext` unless overridden [8]; mm/m confusion and Tekla area/volume conversion factors cause 1000x or 1,000,000x errors [31]. Angles: `IfcPlaneAngleMeasure` uses the project's angle unit (often degrees in building IFC; verify, unverified).
6. **Gross vs net quantities.** `GrossSideArea` vs `NetSideArea` and `GrossVolume` vs `NetVolume` differ by openings; `NetVolume` also depends on connection geometry [2]. Height and Width are provided only if constant along the wall; `Length` is the centre line length [3].
7. **Quantities are not guaranteed to match schedules** from the authoring tool (geometry-based vs rule-based) [22].
8. **`Reference` property deprecated** in IFC4.3 (use the `Name` of the relating type) - appears in Wall, Slab, Space, Column, Window etc. [1][16][17][19][21].
9. **`IfcSpace.IsExternal` attribute** is deprecated in favour of `Pset_SpaceCommon.IsExternal` [17].
10. **Planned vs actual area.** `GrossPlannedArea`/`NetPlannedArea` are programme values, not measured areas; measured area is in `Qto_SpaceBaseQuantities` / `Qto_BuildingStoreyBaseQuantities` [17][18].
11. **`IsExternal` meaning.** TRUE means facing outside the building [1]; some tools derive it from wall Function (Revit) or Position (Archicad) [28]; wrong source parameter gives all-FALSE results.
12. **Revit "Export Revit property sets" exports a flood of parameters** and is off by default; many users turn it on just to find a missing parameter [22].
13. **IFC class capitalisation and tabs** in the Revit user-defined pset file [search results on community threads; 25].
14. **Archicad mapping limited to single values;** table/list/bounded values are not mappable [29].
15. **After an IDS import in Archicad, `Pset_WallCommon` can appear on every object** (community report; verify) [37].
16. **Classification is not a property.** A bSDD/Uniclass/OmniClass code lives in `IfcClassificationReference` (via `IfcRelAssociatesClassification`), not in a `Pset_` [34][39]. People often put it in a custom property as well.
17. **Case and spelling.** Pset and property names are case-sensitive strings (`Pset_WallCommon`, `FireRating`); a pset named `Pset_Wallcommon` is simply a custom set.
18. **Applicability.** `Pset_WallCommon` applies to walls, `Pset_DoorCommon` to doors; a tool that writes `Pset_DoorCommon` onto a wall creates an invalid/odd file [15] (applicability rule from `Applicable entities` of each template; general statement, unverified for validators' exact message).

---

## 9. Typical questions people ask about this

Real discussions (titles from search results; I could not open the Autodesk community pages - HTTP 403 - so content is summarised from search snippets):

1. "IFC Custom PropertySets not working" (Revit user-defined pset file produces no output) - https://forums.autodesk.com/t5/revit-architecture-forum/ifc-custom-propertysets-not-working/td-p/9665491 [37]. Snippet-level cause: wrong capitalisation of IFC class names or missing TABs.
2. "IFC export issue - Revit 2022" - https://forums.autodesk.com/t5/revit-architecture-forum/ifc-export-issue-revit-2022/td-p/11070698 [37].
3. "PSet parameters" (how to get pset parameters out of Revit) - https://forums.autodesk.com/t5/revit-architecture-forum/pset-parameters/td-p/9926144 [37].
4. "Revit IFC Export with User Parameters: Issue with Plate and Bolts" (user parameters missing for some categories) - https://forums.autodesk.com/t5/revit-structure-forum/revit-ifc-export-with-user-parameters-issue-with-plate-and-bolts/td-p/13150852 [37].
5. "IDS import creates IFC Properties as Archicad properties" - https://community.graphisoft.com/t5/Collaboration-with-other/IDS-import-creates-IFC-Properties-as-Archicad-properties/td-p/641956 [37].
6. Autodesk support article "How to export custom Parameters into an IFC file from Revit" - https://www.autodesk.com/support/technical/article/caas/sfdcarticles/sfdcarticles/Custom-Parameter-into-IFC-Export-file-from-Revit.html [27].
7. Autodesk support article "How to export model from Revit to IFC file format with quantities" - https://www.autodesk.com/support/technical/article/caas/sfdcarticles/sfdcarticles/How-to-export-model-from-Revit-to-IFC-export-with-quantities.html [27].
8. Autodesk support article "How to use the IFC parameter mapping table in Revit" - https://www.autodesk.com/support/technical/article/caas/sfdcarticles/sfdcarticles/REVIT-How-to-use-the-IFC-parameter-mapping-table.html [27].

Illustrative questions (invented, realistic for MCP tests):

9. (illustrative) "List all property sets on wall X and show the value of FireRating." Expect: set names incl. `Pset_WallCommon`, value text, and level (type/occurrence).
10. (illustrative) "Which walls are external?" Expect: `Pset_WallCommon.IsExternal = TRUE`; note walls without the property are "unknown", not internal.
11. (illustrative) "Set FireRating to EI60 on all fire doors." Expect: `Pset_DoorCommon.FireRating` as IfcLabel, occurrence level (or type if user says so).
12. (illustrative) "What is the total net volume of concrete walls?" Expect: sum of `Qto_WallBaseQuantities.NetVolume` filtered by material; mention gross vs net.
13. (illustrative) "Why does my wall have no NetSideArea?" Expect: model exported without base quantities (Revit option "Export base quantities" [22]) or tool omitted it.
14. (illustrative) "Add a custom property 'Zone' to all spaces." Expect: custom set name not starting with `Pset_`, e.g. `Company_SpaceData`.
15. (illustrative) "Is `Pset_Fire` a valid set name?" Expect: it is a custom set; `Pset_` is reserved so it is not a standard name.
16. (illustrative) "Edit the type's LoadBearing, but one wall should differ." Expect: occurrence-level override.
17. (illustrative) "Which property tells the manufacturer of this door type?" Expect: `Pset_ManufacturerTypeInformation.Manufacturer` [20].
18. (illustrative) "What unit is the area in?" Expect: from `IfcProject.UnitsInContext` unless the property has its own `Unit` [8].
19. (illustrative) "How do I make Revit export my shared parameter 'FireRating_Custom'?" Expect: mapping table or user-defined pset TXT; data types must match [22][23][27].
20. (illustrative) "Which properties does a storey have and what's the difference between GrossFloorArea and NetFloorArea?" Expect: `Pset_BuildingStoreyCommon`, `Qto_BuildingStoreyBaseQuantities` [18].
21. (illustrative) "Link this wall type to a bSDD class and property." Expect: `IfcClassificationReference` + property with bSDD URI in `Specification` (IFC4.3) / `Description` (IFC4) [34].
22. (illustrative) "Find all elements missing Pset_*Common.FireRating" (validation / IDS style).
23. (illustrative) "Delete property set Qto_WallBaseQuantities from the model." Expect: warning that quantities will be lost and are not auto-recalculated.
24. (illustrative) "Why does Archicad not export my table property?" Expect: mapping supports single-value properties only [29].
25. (illustrative) "Tekla: my UDA is missing from the IFC." Expect: property set definition, long UDA name, template attribute, `optional=true`, or empty value [31].

---

## 10. Hints for QA testers and answer judges

* Check three things in any "property" answer: **set name**, **property name**, **value type** (Boolean vs text vs number). Wrong casing is a failure.
* For edits, ask: "which level (type or occurrence)?" and check the result on both.
* Distinguish **IFC attribute** (e.g. `Name`, `Description`, `Elevation`, `OverallWidth`) from **property** (in a pset). Door/window width/height are attributes `OverallWidth`/`OverallHeight`, with `Qto_` copies [28][21].
* Reasonable independent verification: open the exported IFC in a viewer such as Bonsai/BlenderBIM, or inspect the STEP text lines `IFCPROPERTYSET`, `IFCPROPERTYSINGLEVALUE`, `IFCRELDEFINESBYPROPERTIES`, `IFCRELDEFINESBYTYPE`, `IFCELEMENTQUANTITY`, `IFCQUANTITYAREA`.
* Expected values in sample files: the buildingSMART sample "wall with opening and window" sets `IsExternal = TRUE`, `ExtendToStructure` and `LoadBearing = FALSE` on the wall (IFC4 annex E sample, as described in search results) [1].

---

## Gaps and limits of this research

* Direct fetches of `standards.buildingsmart.org`, `ifc43-docs.standards.buildingsmart.org`, `technical.buildingsmart.org`, `autodesk.com/support` and `forums.autodesk.com` returned HTTP 403; content was taken from search-engine summaries and the buildingSMART GitHub documentation sources. **QA pass 2026-11-06:** the Pset/Qto tables were re-verified line by line against the 4.4.0.0 draft mirror [40]; the frozen IFC 4.3.2.0 pages themselves remained unreachable (HTTP 403), so differences between 4.3.2 and the 4.4 draft are possible and not excluded. Chapter numbers in page titles (6.1.4.x, 5.4.4.x, 6.1.5.x) were not re-checked.
* The web-search quota was exhausted before searching community sources (OSArch, FreeCAD forum, Archicad/Tekla communities) for real practitioner questions; only five thread titles were obtained.
* One PDF (Autodesk "Revit IFC Manual 2.0" class handout, `static.au-uw2-prd.autodesk.com/Class_Handout_BES500080_Revit_IFC_Manual_v2.pdf`) could not be read as text; not used for facts.
* Not researched: Bentley, Allplan, Vectorworks, ArchiCAD Tekla-specific community tips, IFC-SPF vs ifcXML differences for properties, IFC4.3 infrastructure `Pset`s (road/rail/bridge), IDS authoring details, ISO 16739-1 edition numbers (not verified here; the docs I saw are labelled "IFC 4.3.2.0").
* No suspicious/pirated sites were encountered.

## Sources

[1] Pset_WallCommon, IFC 4.3.2 - https://ifc43-docs.standards.buildingsmart.org/IFC/RELEASE/IFC4x3/HTML/lexical/Pset_WallCommon.htm (also https://standards.buildingsmart.org/IFC/RELEASE/IFC4/ADD2/HTML/schema/ifcsharedbldgelements/pset/pset_wallcommon.htm; sample file https://standards.buildingsmart.org/IFC/RELEASE/IFC4/ADD2/HTML/annex/annex-e/wall-with-opening-and-window.ifc.htm)
[2] Qto_WallBaseQuantities, IFC 4.3.2 - https://ifc43-docs.standards.buildingsmart.org/IFC/RELEASE/IFC4x3/HTML/lexical/Qto_WallBaseQuantities.htm ; NetSideArea - https://standards.buildingsmart.org/IFC/DEV/IFC4_3/HTML/property/NetSideArea.html
[3] Qto_WallBaseQuantities (GitHub source) - https://github.com/buildingSMART/IFC4.3.x-development/blob/master/docs/schemas/shared/IfcSharedBldgElements/QuantitySets/Qto_WallBaseQuantities.md
[4] IfcPropertySet (GitHub source) - https://github.com/buildingSMART/IFC4.3.x-development/blob/master/docs/schemas/core/IfcKernel/Entities/IfcPropertySet.md
[5] IfcRelDefinesByProperties - https://github.com/buildingSMART/IFC4.3.x-development/blob/master/docs/schemas/core/IfcKernel/Entities/IfcRelDefinesByProperties.md
[6] IfcRelDefinesByType - https://github.com/buildingSMART/IFC4.3.x-development/blob/master/docs/schemas/core/IfcKernel/Entities/IfcRelDefinesByType.md
[7] IfcTypeObject - https://github.com/buildingSMART/IFC4.3.x-development/blob/master/docs/schemas/core/IfcKernel/Entities/IfcTypeObject.md
[8] IfcPropertyBoundedValue - https://github.com/buildingSMART/IFC4.3.x-development/blob/master/docs/schemas/resource/IfcPropertyResource/Entities/IfcPropertyBoundedValue.md
[9] IfcPropertyTableValue - https://github.com/buildingSMART/IFC4.3.x-development/blob/master/docs/schemas/resource/IfcPropertyResource/Entities/IfcPropertyTableValue.md
[10] IfcPropertyEnumeratedValue - https://github.com/buildingSMART/IFC4.3.x-development/blob/master/docs/schemas/resource/IfcPropertyResource/Entities/IfcPropertyEnumeratedValue.md
[11] IfcPropertyListValue - https://github.com/buildingSMART/IFC4.3.x-development/blob/master/docs/schemas/resource/IfcPropertyResource/Entities/IfcPropertyListValue.md
[12] IfcPropertyReferenceValue - https://github.com/buildingSMART/IFC4.3.x-development/blob/master/docs/schemas/resource/IfcPropertyResource/Entities/IfcPropertyReferenceValue.md
[13] IfcElementQuantity - https://github.com/buildingSMART/IFC4.3.x-development/blob/master/docs/schemas/core/IfcProductExtension/Entities/IfcElementQuantity.md
[14] Property resource entity list - https://github.com/buildingSMART/IFC4.3.x-development/tree/master/docs/schemas/resource/IfcPropertyResource/Entities ; shared building element property sets list - https://github.com/buildingSMART/IFC4.3.x-development/tree/master/docs/schemas/shared/IfcSharedBldgElements/PropertySets
[15] Pset_DoorCommon, IFC 4.3.2 - https://ifc43-docs.standards.buildingsmart.org/IFC/RELEASE/IFC4x3/HTML/lexical/Pset_DoorCommon.htm
[16] Pset_SlabCommon, IFC 4.3.2 - https://standards.buildingsmart.org/IFC/RELEASE/IFC4_3/HTML/lexical/Pset_SlabCommon.htm ; PitchAngle - https://standards.buildingsmart.org/IFC/RELEASE/IFC4_3/HTML/property/PitchAngle.htm
[17] Pset_SpaceCommon, IFC 4.3.2 - https://ifc43-docs.standards.buildingsmart.org/IFC/RELEASE/IFC4x3/HTML/lexical/Pset_SpaceCommon.htm
[18] Pset_BuildingStoreyCommon - https://ifc43-docs.standards.buildingsmart.org/IFC/RELEASE/IFC4x3/HTML/lexical/Pset_BuildingStoreyCommon.htm ; Qto_BuildingStoreyBaseQuantities - https://ifc43-docs.standards.buildingsmart.org/IFC/RELEASE/IFC4x3/HTML/lexical/Qto_BuildingStoreyBaseQuantities.htm ; Pset_BuildingCommon - https://ifc43-docs.standards.buildingsmart.org/IFC/RELEASE/IFC4x3/HTML/lexical/Pset_BuildingCommon.htm ; Qto_BuildingBaseQuantities - https://ifc43-docs.standards.buildingsmart.org/IFC/RELEASE/IFC4x3/HTML/lexical/Qto_BuildingBaseQuantities.htm
[19] Pset_ColumnCommon - https://ifc43-docs.standards.buildingsmart.org/IFC/RELEASE/IFC4x3/HTML/lexical/Pset_ColumnCommon.htm ; Pset_BeamCommon - https://ifc43-docs.standards.buildingsmart.org/IFC/RELEASE/IFC4x3/HTML/lexical/Pset_BeamCommon.htm ; Pset_RoofCommon - https://ifc43-docs.standards.buildingsmart.org/IFC/RELEASE/IFC4x3/HTML/lexical/Pset_RoofCommon.htm ; Annex B property set listing - https://standards.buildingsmart.org/IFC/DEV/IFC4_3/HTML/annex-b3.html
[20] Pset_ManufacturerTypeInformation, IFC 4.3.2 - https://ifc43-docs.standards.buildingsmart.org/IFC/RELEASE/IFC4x3/HTML/lexical/Pset_ManufacturerTypeInformation.htm ; IFC2x3 definition - https://standards.buildingsmart.org/IFC/RELEASE/IFC2x3/TC1/HTML/psd/IfcSharedFacilitiesElements/Pset_ManufacturerTypeInformation.xml
[21] Pset_WindowCommon - https://ifc43-docs.standards.buildingsmart.org/IFC/RELEASE/IFC4x3/HTML/lexical/Pset_WindowCommon.htm ; Qto_WindowBaseQuantities - https://ifc43-docs.standards.buildingsmart.org/IFC/RELEASE/IFC4x3/HTML/lexical/Qto_WindowBaseQuantities.htm
[22] Autodesk Revit IFC Exporter help 25.2 - https://up1.autodesk.com/2025/RVT/ADSKIFCExporterHelp_25_2.htm
[23] Autodesk Revit 2025 help, user-defined property set TXT - https://help.autodesk.com/view/RVT/2025/ENU/?guid=GUID-0968B3FF-832B-4155-8B36-E848ACC97B95
[24] Autodesk Revit 2027 help, Manage IFC Export User Defined Property Sets - https://help.autodesk.com/cloudhelp/2027/ENU/Revit-DocumentPresent/files/GUID-E6B1753C-7396-4176-995B-8306C4F50EF4.htm ; Revit 2026 IFC export index - https://help.autodesk.com/cloudhelp/2026/ENU/Revit-DocumentPresent/files/GUID-6EB68CEC-6C17-4B16-A509-30537F666C1F.htm
[25] revit-ifc DefaultUserDefinedParameterSets.txt - https://github.com/Autodesk/revit-ifc/blob/master/Install/Program%20Files%20to%20Install/DefaultUserDefinedParameterSets.txt
[26] revit-ifc QuantityEntryMap.cs - https://github.com/Autodesk/revit-ifc/blob/master/Source/Revit.IFC.Export/Exporter/PropertySet/QuantityEntryMap.cs
[27] Autodesk support articles (search-summary level only; direct fetch 403) - see items 6-8 URLs in section 9
[28] Graphisoft, Predefined Property Mapping (Archicad 27) - https://help.graphisoft.com/AC/27/INT/_AC27_Help/121_IFC/121_IFC-50.htm
[29] Graphisoft help (search-summary level): Property Mapping for IFC Import - https://help.graphisoft.com/AC/27/INT/_AC27_Help/121_IFC/121_IFC-27.htm ; IFC Translators overview - https://help.graphisoft.com/AC/24/INT/_AC24_Help/115_IFC/115_IFC-23.htm ; Predefined Property Mapping (AC21) - https://help.graphisoft.com/AC/21/INT/AC21Help/07_Interoperability/07_Interoperability-89.htm
[30] Graphisoft, IFC Data Types - https://help.graphisoft.com/AC/25/INT/_AC25_Help/121_IFC/121_IFC-47.htm
[31] Tekla Structures 2023, Create new property sets for IFC export - https://support.tekla.com/doc/tekla-structures/2023/int_admin_creating_property_sets_for_ifc
[32] Tekla Structures 2023, Exported IFC properties and quantities - https://support.tekla.com/doc/tekla-structures/2023/int_property_sets_in_ifc_export ; IFC improvements 2022 - https://support.tekla.com/doc/tekla-structures/2022/rel_int_ifc_improvements
[33] Tekla Structures 2026, attribute overrides for IFC export - https://support.tekla.com/doc/tekla-structures/2026/int_create_attribute_overrides_for_ifc_export
[34] buildingSMART bSDD-IFC documentation - https://github.com/buildingSMART/bSDD/blob/master/Documentation/bSDD-IFC%20documentation.md
[35] buildingSMART Technical, Referencing bSDD in IDS and IFC - https://technical.buildingsmart.org/services/bsdd/referencing-bsdd-in-ids-and-ifc/ (search-summary level; direct fetch 403) ; Data structure of bSDD - https://technical.buildingsmart.org/services/bsdd/data-structure/
[36] IfcOpenShell API, pset.add_pset - https://docs.ifcopenshell.org/autoapi/ifcopenshell/api/pset/add_pset/index.html
[37] Community threads: see section 9, items 1-5 (URLs there)
[38] IFC4.3 IfcSharedBldgElements overview - https://standards.buildingsmart.org/IFC/RELEASE/IFC4_3/HTML/ifcsharedbldgelements/content.html
[39] IfcRelAssociatesClassification, IFC 4.3.2 - https://ifc43-docs.standards.buildingsmart.org/IFC/RELEASE/IFC4x3/HTML/lexical/IfcRelAssociatesClassification.htm
[40] buildingSMART documentation mirror, IFC 4.4.0.0 working draft (readable without 403; used by QA 2026-11-06 to verify Pset/Qto lists). Examples: https://bsi-infraroom.github.io/IFC-Documentation-Tunnel/4_4_0_0/general/HTML/schema/ifcsharedbldgelements/pset/pset_wallcommon.htm ; .../pset/pset_doorcommon.htm ; .../pset/pset_windowcommon.htm ; .../pset/pset_coveringcommon.htm ; .../pset/pset_roofcommon.htm ; .../ifcproductextension/pset/pset_buildingstoreycommon.htm ; .../ifcsharedfacilitieselements/pset/pset_manufacturertypeinformation.htm ; .../ifcsharedbldgelements/qset/qto_wallbasequantities.htm (same pattern for the other psets and qsets)
[41] Autodesk, Revit IFC Exporter help 25.2 (QA-read 2026-11-06; same as [22]) and Revit 2025 help on the user-defined property set text file - https://help.autodesk.com/view/RVT/2025/ENU/?guid=GUID-0968B3FF-832B-4155-8B36-E848ACC97B95
