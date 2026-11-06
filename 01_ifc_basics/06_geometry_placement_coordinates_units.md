# Geometry, placement, coordinates, georeferencing and units

**In plain words.** An IFC file stores two kinds of information about every wall, slab or pipe: what it *is* (class, properties) and *where and what shape* it has (geometry). The shape is a "representation" (extrusion, mesh, boundary surface...) written in the element's own local coordinates; a chain of "local placements" then moves it into the building, the site and finally the project's coordinate system. The project coordinate system can optionally be tied to a real-world map system (EPSG code, Eastings/Northings) with a few extra entities. Everything is measured in the units declared once for the project (often millimetres, sometimes metres or feet). Most "model is in the wrong place / rotated / 1000 times too big" bugs come from one of three things: a wrong or missing unit, a huge offset hidden in the placement chain, or georeferencing data that is missing, duplicated or inconsistent.

**Last researched: 2026-11-06**

Source markers like [3] refer to the Sources section. "(unverified)" marks claims that I could not confirm from a page I actually read. Note: in this research session the buildingSMART HTML spec pages and Autodesk support articles returned HTTP 403 to my fetch tool, so spec facts were read from the buildingSMART GitHub documentation sources (same text as the IFC 4.3 spec) and Autodesk articles are cited only from search snippets (marked). **QA pass 2026-11-06:** spec facts on `IfcMapConversion`, `IfcProjectedCRS`, `IfcMapConversionScaled`, `IfcRigidOperation`, `IfcPolygonalFaceSet`, `IfcUnitAssignment`, `IfcGeometricRepresentationContext` and the Revit "Coordinate Base" option names were re-read against the GitHub docs sources and the Autodesk IFC Exporter help 25.2; corrections are marked "QA".

---

## 1. Geometry in IFC: the big picture

### 1.1 Product -> representation -> items
- An element (IfcWall, IfcBeam...) has `ObjectPlacement` (where its local origin is) and `Representation` (an `IfcProductDefinitionShape`) containing one or several `IfcShapeRepresentation`s.
- Each `IfcShapeRepresentation` has a **context** (`IfcGeometricRepresentationContext`, or a sub-context), a **RepresentationIdentifier** (the "purpose" slot, e.g. Body), a **RepresentationType** (the "kind of geometry" hint, e.g. SweptSolid) and a list of geometric **Items** [5].
- The spec says an identifier and a type *should* be provided, and the items must fit the declared type (rule `CorrectItemsForType`) [5]. A test that claims "SweptSolid" but contains a mesh is a legitimate finding.

### 1.2 Contexts
- One 3D context with `ContextType = 'Model'` is mandatory, a 2D `'Plan'` context is optional; at most one of each [6]. (QA: the spec lists the recognised `ContextType` values as `'Model'`, `'Plan'` and `'NotDefined'`; `Precision` is described as typically in the 1E-5 to 1E-8 range; `TrueNorth` defaults to (0,1) when absent [6].)
- `CoordinateSpaceDimension` (2 or 3), `Precision` (a tolerance, typically 1E-5 to 1E-8, below which two points are the same), `WorldCoordinateSystem` and `TrueNorth` live here [6].
- `IfcGeometricRepresentationSubContext` carries view or scale dependent variations (its parent is the Model or Plan context). Typical sub-context identifiers seen in practice are Body, Axis, FootPrint, Box (these are common ArchiCAD/Revit/IfcOpenShell conventions; the exact list of ContextIdentifier values is not in the page I read, so treat as (unverified)) [6].

### 1.3 RepresentationIdentifier values (from the spec)
| Identifier | Meaning [5] |
|---|---|
| **Body** | Main 3D representation (wireframe, surface or solid). This is what viewers show. |
| **Axis** | 2D or 3D axis / single-line representation (wall centreline, beam axis) |
| **FootPrint** | 2D footprint or double-line view projected on the ground (plan symbol) |
| **Box** | Simplified 3D box bounding the element |
| Body-FallBack | Extra 3D body (tessellation or Brep) delivered alongside a solid model |
| CoG | Centre-of-gravity point used for validation |
| Profile | Planar 3D line representation of a profile (door/window outlines) |
| Surface | 3D analytical surface of the element's plane |
| Reference | 3D geometry outside the Body, e.g. opening geometry that is *not* subtracted |
| Annotation | 2D/3D annotations |
| Clearance | Clearance volume that must not intersect other elements' Body |
| Lighting | Light source |

### 1.4 RepresentationType values (the ones testers meet most)
| Type | Meaning [5] | Typical producer |
|---|---|---|
| **SweptSolid** | Swept area solids from extrusion and revolution (no tapered sweeps) | ArchiCAD, Revit (walls, slabs, columns), Tekla |
| **Clipping** | Boolean *differences* between swept solids, half-spaces and Boolean results (e.g. a wall with a slanted top) | Revit/ArchiCAD walls with attach-top |
| **CSG** | Boolean results of operations between solids, half spaces and other Boolean results | rare in exports |
| **Brep** | Faceted Breps (planar faces), with or without voids | older exporters, fallback |
| **AdvancedBrep** | Breps with advanced faces / B-spline geometry | NURBS-heavy CAD (Rhino, mechanical equipment) |
| **Tessellation** | Tessellated surfaces only (triangles/polygons) | Revit IFC4 "Reference View" style exports, Blender, viewers |
| **MappedRepresentation** | Representation made of mapped items referring to a representation map (like a block/instance); the mapped item's type defines the item types | Revit/ArchiCAD for repeated families, furniture, windows |
| SurfaceModel / SolidModel / SurfaceOrSolidModel | Face/shell/tessellated surfaces, or solids incl. swept, Boolean, Brep | generic |
| AdvancedSweptSolid | Swept along a directrix incl. tapered sweeps | pipes/sweeps |
| BoundingBox | Simplified box | `Box` identifier |
| Curve2D / Curve3D, GeometricCurveSet, GeometricSet | 2D/3D curves and sets | Axis, FootPrint, annotations |

`PointCloud` is deprecated in IFC4.3.2.0 in favour of `Point` [5].

### 1.5 Parametric vs tessellated: trade-offs
| Aspect | Parametric (profile + extrusion, SweptSolid) | Tessellated (IfcTriangulatedFaceSet / IfcPolygonalFaceSet) | Brep / AdvancedBrep |
|---|---|---|---|
| Size in file | Tiny: a profile, a direction, a depth | Large for curved things; every curve is chopped into triangles | Medium to large |
| Editability downstream | High: dimensions can be read back (width, depth, height are explicit) | Low: only vertices, no design intent | Low |
| Quantities | Can be derived from profile * depth | Must be computed from mesh | Computed |
| Viewer speed | Viewer must tessellate | Fast (already triangles) | Viewer must tessellate |
| Robustness | Needs correct profile orientation / extrusion direction | Very robust; "what you see" | Topology errors possible |
| Fidelity of curves | Exact | Approximate (depends on tolerance) | Exact for advanced |

Facts from the spec: `IfcTriangulatedFaceSet` is a tessellated face set where every face is a triangle; `Closed = TRUE` makes it a Brep-like solid, `FALSE` a face-based surface; indices are one-based [10]. `IfcPolygonalFaceSet` allows polygonal faces with holes (`IfcIndexedPolygonalFaceWithVoids`) and was new in **IFC4 Addendum 2** (verified in the entity's own version note [11]; so an "IFC4" file written before ADD2, or a reader built for IFC4 ADD1, may not know it). Both reference an `IfcCartesianPointList3D`, so shared vertices keep the file smaller than classic `IfcFacetedBrep` which repeats points per face [10][11] (the file-size comparison itself is common knowledge, not a quoted statement, (unverified) as a number).

QA hint: a "small" IFC that suddenly grows by 5-10x after a round trip usually means parametric solids were converted to meshes (typical for exports aimed at viewing). Common practice, no source (unverified).

### 1.6 Profiles, extrusions
- `IfcExtrudedAreaSolid` = a 2D profile (`SweptArea`, e.g. `IfcRectangleProfileDef`, `IfcIShapeProfileDef`, `IfcArbitraryClosedProfileDef`) swept along `ExtrudedDirection` for `Depth`. The profile lies in the XY plane of the solid's position; inner boundaries (holes) in the profile become holes in the solid [12].
- Rule `ValidExtrusionDirection`: the direction must not be perpendicular to the local z-axis [12]. Typical test failure: extrusion depth 0 or negative, or direction (1,0,0) in a 3D position without the right axis.
- Profile positions: a rectangle profile is centred at its own origin unless a profile `Position` is given [12]. That is why a wall's "origin" is often mid-thickness, mid-length.

### 1.7 Clipping and booleans
- `IfcBooleanClippingResult` is a restricted Boolean: first operand must be an `IfcSweptAreaSolid` (or an earlier clipping result), second must be an `IfcHalfSpaceSolid`, operator is always `DIFFERENCE`. Repeated cuts are allowed [13].
- `IfcBooleanResult` is the general case; `RepresentationType = 'CSG'` is for Boolean results of solids/half-spaces/Booleans [5].

### 1.8 Openings (voids)
- Openings are separate objects, `IfcOpeningElement`, linked to the host by `IfcRelVoidsElement`; doors and windows that fill them are linked by `IfcRelFillsElement`. The opening must **not** be spatially contained itself [14].
- The opening's `Body` is *implicitly subtracted* from the host's `Body`. A `Reference` representation is not subtracted [14].
- The opening's local placement should be relative to the host element's placement (`PlacementRelTo` = host's placement) [14].
- `PredefinedType` OPENING (at least as thick as host) or RECESS (thinner) [14].
- So the wall body geometry itself shows no hole; the hole appears only after the viewer evaluates the void. A viewer or script that ignores `IfcRelVoidsElement` shows solid walls, a very common "my doors float in solid walls" symptom.

### 1.9 Mapped (instanced) geometry
`MappedRepresentation` uses `IfcMappedItem` + `IfcRepresentationMap`, "like an inserted block reference" [5]. The geometry is stored once per type, each instance only has a transform. It keeps files small but means a naive script that reads `Representation.Representations[0].Items[0]` sees a mapped item, not a solid; one must go into the map (and apply the mapping target transform).

---

## 2. Placement: IfcLocalPlacement chains

- `IfcLocalPlacement` has `PlacementRelTo` (optional parent placement) and `RelativePlacement` (an `IfcAxis2Placement3D` = location point + Z axis + X ref direction) [4].
- If `PlacementRelTo` is empty, the placement is absolute in the **world coordinate system** of the project's context [4].
- The absolute transform of an element = product of all the relative transforms up the chain: element -> storey -> building -> site -> (world). The rule: 3D placements may only refer to 3D parents; cycles must be prevented by applications [4].
- Spec default conventions: `IfcSite` absolute in the project's WCS; facility relative to site; openings and fillings relative to their host element; ordinary elements relative to their spatial container [4].

### Example chain (illustrative)
```
#10= IFCCARTESIANPOINT((0.,0.,0.));
#20= IFCAXIS2PLACEMENT3D(#10,$,$);
#30= IFCLOCALPLACEMENT($,#20);                    /* Site: absolute */
#40= IFCLOCALPLACEMENT(#30,#21);                  /* Building: relative to site */
#50= IFCLOCALPLACEMENT(#40,#22);                  /* Storey: Z = level elevation */
#60= IFCLOCALPLACEMENT(#50,#23);                  /* Wall: relative to storey */
```
If *any* link in the chain carries a large translation or a rotation, everything below it inherits it. This is how Revit-exported files end up "far from origin" without any single wall having big coordinates (see 4.4) [21].

### How to check in a file
- Walk `ObjectPlacement` up to the root for a few elements and sum the translations. Large sums (say > 10 km, or > 1e5 in project units) are suspicious.
- Compare the absolute position of `IfcSite`, `IfcBuilding`, first storey and a wall: they should differ by plausible amounts (storey Z = level elevation).
- IfcOpenShell: `ifcopenshell.util.placement.get_local_placement(element.ObjectPlacement)` returns the 4x4 absolute matrix (QA 2026-11-06: confirmed in `ifcopenshell/util/placement.py` v0.8.0, signature `get_local_placement(placement=None)`; it returns the identity matrix for `None` and recursively multiplies the parent chain via `PlacementRelTo`; the same module also has `get_storey_elevation`).

---

## 3. Coordinate systems: who is "zero"?

### 3.1 The IFC side
| Concept | Where | Notes |
|---|---|---|
| **World Coordinate System (WCS)** | `IfcGeometricRepresentationContext.WorldCoordinateSystem` | The shared engineering (project) coordinate system of all contexts. Usually origin with standard axes; can be shifted for numerical stability when the building is far from the origin. With a map conversion it defines the offset between local zero and the geographic reference point [6]. |
| **True North** | `IfcGeometricRepresentationContext.TrueNorth` (2D direction in the XY plane) | Default (0,1), i.e. +Y is north. If a coordinate operation exists, TrueNorth is informational only and IfcMapConversion wins; it must not be applied again on top of a transformation already done by the operation [6]. |
| **Site / building / storey placements** | `IfcLocalPlacement` | Chain, see section 2. |
| **Map conversion** | `IfcMapConversion` + `IfcProjectedCRS` (IFC4+) | Section 5. |

The same spec text suggests the *project base point and survey point should ideally coincide* in practice [6].

### 3.2 Revit vs IFC
Revit has three reference points:
| Revit element | Role | Can move? |
|---|---|---|
| **Internal Origin** | Hidden fixed origin of the Revit database; all geometry is stored relative to it. Keep content within about 16 km (10 miles) of it [22][23] (the figure comes from two community blogs; the Autodesk page that states the exact limit was not readable, so treat the number as (unverified); other Autodesk/community texts quote other distances, e.g. recommending much smaller distances for performance) | No (fixed) |
| **Project Base Point (PBP)** | Origin of the *project* coordinate system (the "0,0" the designers see). Has `E/W`, `N/S`, `Elev` and **Angle to True North** [21] | Yes (but it is easiest to leave it on the Internal Origin [22]) |
| **Survey Point** | Surveyor's common point (e.g. property corner). With **Shared Coordinates** it defines the relation to the survey/GIS system | Yes (clipped by default; moving it changes the shared coordinate system [22]) |

"**Shared coordinates**" is an Autodesk concept; IFC has no such thing, it only has the WCS and map conversion [24] (statement made in the Autodesk/revit-ifc issue thread; also stated in an Autodesk Community answer seen in search results).

### 3.3 Revit IFC export: "Coordinate Base" (a.k.a. Project Origin) options
In the IFC Export setup (General tab), the **Coordinate Base** option offers four choices (verified QA 2026-11-06 on Autodesk's IFC Exporter help 25.2): **Shared Coordinates (default)**, **Survey Point**, **Project Base Point**, **Internal Origin**. The open-source exporter's resource file additionally has the two "oriented in True North" variants ("Project Base Point oriented in True North", "Internal Origin oriented in True North"), i.e. six entries in the UI list [20][22]; see `../03_software/revit/ifc_export_reference.md` section 4. Autodesk's own article titles/snippets say: if coordinates come out wrong, check the base; make sure at least one set (Shared Coordinates, Survey Point, Project Base Point, Internal Origin) matches the other disciplines' coordinate system [Autodesk articles, snippet-only, 28].

What each means in practice:
- **Project Base Point**: the PBP lands at the IFC (0,0,0) and the building is near the origin. Recommended by the OSArch workflow, together with entering an EPSG code, in Revit IFC 19.4.0.0 / 20.2.0.0 / 21.1.0.0 and later (IFC4 only) [20].
- **Survey Point**: the model is offset by the PBP-to-survey-point distance [22]. Reported to populate Eastings/Northings correctly where Shared Coordinates did not [Autodesk Community thread, snippet-only, 33].
- **Shared Coordinates**: per Autodesk, the model is exported in real-world coordinates so global X/Y/Z equal shared coordinates [snippet, 28]. Consequence: huge coordinates and the Revit warning "The elements in this model are very far from the origin in this exported file" [snippet, 28]. Autodesk's own suggestion for scattered geometry is to export with PBP or Survey Point as reference [snippet, 28]. Users also report Eastings/Northings = 0 with this option [snippet, 33].
- **Internal Origin**: fixed, cannot be moved; stable for coordination when all disciplines use it [22][23].

IFC links in Revit were historically "Origin to Origin" (IFC origin to Revit internal origin) [22][23]; Revit 2026 adds a choice at link time, so pick the option that matches how the IFC was exported, and check the `*.ifc.log.html` report [23]. Revit-ifc issue #566 shows people still struggle linking IFCs with shared coordinates; the answer given there is that "shared coordinates" is an Autodesk-specific concept and to validate the IFC georeferencing before importing [24].

### 3.4 What Revit actually writes (documented by an enthusiast, Revit IFC 2021-2022 era; re-test on your version) [21]
- One `IfcGeometricRepresentationContext`; `Precision` 0.01 mm in a metric project; `WorldCoordinateSystem` always (0,0,0).
- `TrueNorth` comes from the PBP's "Angle to True North".
- `IfcSite.RefLatitude/RefLongitude` come from the project **Location** dialog (not from survey point); `RefElevation` from PBP `Elev`.
- `IfcSite` placement is derived from PBP position; `IfcBuilding` is at (0,0,0) relative to the site; storey Z = level elevation + PBP Elev.
- Large local eastings/northings typed into PBP/Survey Point put the `IfcSite` very far from the origin, and everything inherits it.
- Newer exporters (19.4+/20.2+/21.1+) can write `IfcMapConversion` and `IfcProjectedCRS` natively in IFC4 [20].

---

## 4. Georeferencing

### 4.1 Levels of Georeferencing (LoGeoRef)
The LoGeoRef model (Clemen and Görne, 2019, according to a search-result summary; the paper PDFs from FIG 2018 / ISPRS 2024 were not readable in my tool, so this is secondary) defines five levels. The open-source IFCGeoRefChecker (City2BIM project) implements them as follows [15]:

| Level | Content | IFC location checked [15] |
|---|---|---|
| **LoGeoRef 10** | Postal address of the project/site | `IfcPostalAddress` referenced by `IfcSite` or `IfcBuilding` (no plausibility check) |
| **LoGeoRef 20** | One point as latitude/longitude (+ optional elevation) | `IfcSite.RefLatitude`, `RefLongitude` (required), `RefElevation` (optional), read as compound angle integers, WGS84 |
| **LoGeoRef 30** | Location of a spatial element via its placement | `IfcLocalPlacement` of `IfcSite`/`IfcBuilding`/`IfcBuildingStorey`/`IfcSpace` with `PlacementRelTo` empty and a non-zero location |
| **LoGeoRef 40** | Georeferencing in the project's model context | `IfcGeometricRepresentationContext` ("Model") `WorldCoordinateSystem` location (non-zero) and axes, plus `TrueNorth` |
| **LoGeoRef 50** | Full map conversion | `IfcMapConversion` (Eastings, Northings, OrthogonalHeight, XAxisAbscissa, XAxisOrdinate, Scale) with `SourceCRS` = the geometric context and `TargetCRS` = `IfcProjectedCRS` (ideally EPSG) |

- 50 is IFC4+ only; files older than IFC4 cannot reach it [15].
- The levels are independent; a file can satisfy several [15, search summary].
- The 2025 buildingSMART Deutschland BIM Fit Check on georeferencing (IFC 4.3, ETRS89 / UTM 32N + DHHN2016) found that all six tested products passed, but that the spec does not clearly say when to use `IfcMapConversion` vs `IfcRigidOperation`, that `IfcProjectedCRS` only holds a free-text vertical datum, and that the "LoGeoRef 30" style (base point without CRS) stays valid in IFC 4.3; it proposes requiring LoGeoRef50 in a "modern" MVD [16].

### 4.2 IFC2x3
IFC2x3 has no map conversion entities. Two mechanisms:
1. **IfcSite attributes**: `RefLatitude`, `RefLongitude` (compound angles: degrees, minutes, seconds, optional millionths of seconds; WGS84; N/E positive) and `RefElevation` (elevation relative to the site's height datum, unit not stated on the page) [9]. Per the IFC4.x text, these values refer to the point where the IfcSite's local placement origin (0,0,0) is [9]. This gives only an approximate location.
2. **Property sets by convention** (not part of the IFC2x3 schema): `EPset_ProjectedCRS` (Name, Description, GeodeticDatum, VerticalDatum, MapProjection, MapZone, MapUnit) and `EPset_MapConversion` (Eastings, Northings, OrthogonalHeight, XAxisAbscissa, XAxisOrdinate, Scale) [19][20]. Capitalisation varies in the wild: `ePSet_MapConversion`, `EPset_MapConversion`, `ePset_MapConversion`; a buildingSMART forum reviewer flagged the inconsistency in the official user guide [19]. Placement also varies: the forum proposal says IfcSite [19], while IfcOpenShell's `get_helmert_transformation_parameters` reads `ePSet_MapConversion` from `IfcProject` for IFC2X3 [27]. So a checker should look at both IfcProject and IfcSite and accept all name variants.
3. In Revit for IFC2x3, the documented route is a Toposurface exported as IfcSite plus property sets from a mapping text file [20]; the OSArch page also says the export duplicates the coordinates (once in the map conversion data, once in the IfcSite `Location`) and must be patched [20].

### 4.3 IFC4 and IFC4.3
- `IfcMapConversion` (new in IFC4) defines how the local engineering coordinate system (WCS) maps to the CRS of a map. Operation order: **scale** (one uniform `Scale` for x, y, z) -> **rotate** anticlockwise about z by `atan2(XAxisOrdinate, XAxisAbscissa)` -> **translate** by `Eastings`, `Northings`, `OrthogonalHeight`. The local z axis stays parallel to the map z axis [1].
- In formula form (derived from the same order): with scale s and angle θ, `E = Eastings + s*(x cosθ - y sinθ)`, `N = Northings + s*(x sinθ + y cosθ)`, `H = OrthogonalHeight + s*z`.
- Attributes [1]: `Eastings`, `Northings`, `OrthogonalHeight` (height relative to the vertical datum), `XAxisAbscissa`, `XAxisOrdinate` (the easting/northing components of the local x axis; if no rotation, 1 and 0), `Scale` (default 1.0; **must** be given when source and map units differ, e.g. feet to metres, or millimetres to metres = 0.001).
- IfcOpenShell notes: both abscissa and ordinate being 0 is treated as (1, 0), and files may hold non-unit vectors, so tools normalise them [27]. The user-guide formula `atan2(abscissa, ordinate)` was challenged on the buildingSMART forum; the spec text uses ordinate over abscissa [19][1].
- `IfcMapConversionScaled` is a subtype of `IfcMapConversion` that adds `FactorX`, `FactorY`, `FactorZ`; they multiply the respective axis after the uniform `Scale` and before the rotation, and scale coordinates, not units. It is a **new entity in IFC4X3_ADD1** (IFC 4.3.1.0) [1] (QA verified from the entity source). `IfcRigidOperation` (also **new in IFC4X3_ADD1**) "specifies an offset in the coordinate reference system" and "does not specify any conversion or distortion": attributes `FirstCoordinate`, `SecondCoordinate`, `Height` (translation above/below the coordinate surface). It is mentioned in the 2025 Fit Check [16] and read by IfcOpenShell [27]. Because both are post-4.3.0 additions, an older 4.3 reader may not know them.
- `IfcMapConversion` is a subtype of `IfcCoordinateOperation` whose `SourceCRS` is the geometric representation context and `TargetCRS` is an `IfcProjectedCRS`; the context links to it via the inverse `HasCoordinateOperation`. With several contexts they must all reference the same operation instance [6]. It does not handle projection from a geodetic CRS [1].
- `IfcProjectedCRS` [2][3]:
  - `Name`: the unambiguous identifier, "should come from the EPSG list and carry the EPSG namespace", e.g. `EPSG:5555`; **only one EPSG code** in Name. If no code fits, `Name = 'WKT'` and an `IfcWellKnownText` is provided [3].
  - 3D context: the CRS must be a **compound** CRS so the geodetic and vertical datums are identifiable; 2D context: projected or compound [2].
  - Spec examples: EPSG:5555 (ETRS89 / UTM zone 32N + DHHN92 height), EPSG:9286 (ETRS89 + NAP height), EPSG:9306 (HS2 Survey Grid + HS2-VRF height) [2].
  - When Name is specific, `GeodeticDatum`, `VerticalDatum`, `MapProjection`, `MapZone` can be omitted. `MapUnit` is the length unit of the map axes; if omitted the project units apply [2].
- **Precedence**: if `IfcMapConversion` exists, `TrueNorth` is informational, and `IfcSite.RefLatitude/Longitude/Elevation` should not be used for georeferencing; they are kept for upward compatibility, require a single IfcSite and WGS84 [6][9][17][18].
- IFC4.3 renamed/moved things around infrastructure (alignments are placed relative to the project WCS [4]); not needed for buildings.

### 4.4 Large coordinates and precision
- Good practice: keep local coordinates small and put the real-world position in `IfcMapConversion` [18]. Putting the offset into placements (Revit workaround) loses scale and rotation and is "incorrect" in the community view [18].
- Float precision: 32-bit floats have about 7 significant digits. A point at northing 5,500,000 m has spacing of 0.5 m in float32 (general numeric fact, not from a source), so viewers using float32 show jitter, jagged edges or disappearing surfaces far from origin. Revit-specific: content should stay within ~16 km of the internal origin [22][23].
- IFC `Precision` of the context (e.g. 1E-5) is a tolerance in context units, not a coordinate limit [6].
- STEP files store coordinates as text, so double precision is kept; the problem is in consuming software (viewers, GPU pipelines, boolean kernels).

### 4.5 Georeferencing in Archicad (for cross-tool tests)
Graphisoft's community page "Survey Point is now supported at IFC import/export" exists (title seen in search results) but the page returned 403, so details are (unverified).

---

## 5. Units

### 5.1 Structure
- `IfcProject.UnitsInContext` -> `IfcUnitAssignment` -> set of units. Each unit type may appear only once (rule WR01); at most one monetary unit [8]. The assignment sets project-wide units "unless otherwise defined"; objects may have local assignments for other units [8].
- `IfcSIUnit` has `UnitType` (LENGTHUNIT, AREAUNIT, VOLUMEUNIT, PLANEANGLEUNIT...), optional `Prefix`, and `Name`. A millimetre is written as `IFCSIUNIT(*,.LENGTHUNIT.,.MILLI.,.METRE.)` [search result of IFC 2x2 examples, 35]. A metre has no prefix.
- SI prefixes in the schema and their factors (from IfcOpenShell's table [26]): EXA 1e18, PETA 1e15, TERA 1e12, GIGA 1e9, MEGA 1e6, KILO 1e3, HECTO 1e2, DECA 1e1, DECI 1e-1, CENTI 1e-2, MILLI 1e-3, MICRO 1e-6, NANO 1e-9, PICO 1e-12, FEMTO 1e-15, ATTO 1e-18.
- `IfcConversionBasedUnit` = non-SI unit defined via a conversion factor (an `IfcMeasureWithUnit`) to an SI unit: inch = 25.4 mm, foot = 304.8 mm (also expressible via inch); the US survey foot is 304.80060960122 mm, not 304.8 [7]. Example: `IFCCONVERSIONBASEDUNIT(#9,.LENGTHUNIT.,'FOOT',#8)` (shape of the example from the IFC 2x2 examples; the name 'FOOT' is from the standard names table, which is case-insensitive [7]).
- Angles: `PLANEANGLEUNIT` is usually radians, or degrees via a conversion based unit; angles in `IfcSite.RefLatitude` are separate (compound DMS integers) [9].
- Derived/area/volume units follow the length unit prefix. IfcOpenShell raises the prefix to the power for pure length-power dimensions (so cubic millimetres scale by 1e-9) [26].

### 5.2 Which values are in project units?
Coordinates, extrusion depths, profile dimensions, and `IfcLengthMeasure` property values are in the **project length unit**. `IfcMapConversion` `Eastings/Northings/OrthogonalHeight` are in the **target CRS map unit** (`IfcProjectedCRS.MapUnit`), and `Scale` converts between the two [1][2]. So a typical Revit file: project in millimetres, map in metres, Scale = 0.001.

### 5.3 Conversion helpers
- IfcOpenShell: `ifcopenshell.util.unit.calculate_unit_scale(ifc_file, "LENGTHUNIT")` returns the factor: `value_in_project_units * scale = SI value` [26]; `convert_file_length_units(ifc_file, "METER")` can produce a file in metres [26].

---

## 6. Typical failures and how to check them

| Symptom | Likely cause | How to check in the file |
|---|---|---|
| Model very far from origin in the viewer; "zoom to fit" shows empty space, jitter | Georeferenced coordinates baked into placements (Revit Shared Coordinates / PBP with real E/N) [21][28] | Print absolute location of IfcSite, first storey, a wall. Look at `IfcSite.ObjectPlacement` and `WorldCoordinateSystem`. Magnitude > 1e5 (in metres) is a red flag |
| Two federated models do not line up | Different coordinate base (Internal Origin vs PBP vs Survey Point vs shared); one has map conversion, other has none [22][28] | Compare `IfcMapConversion` of both files, WCS, site placement; find a shared object (grid, column) and compute delta |
| Model rotated | True North applied twice or north confusion: `TrueNorth` + `XAxisAbscissa/Ordinate` both applied; project north vs true north [6][22] | Check TrueNorth vector and map conversion angle `atan2(ordinate, abscissa)`; they must not be added |
| Model 1000x too big/small | Units: mm declared as m (or reverse); `Scale` missing/wrong; map unit mismatch [1][25] | Read `IfcUnitAssignment`. Check typical dimensions: a door ~900 (mm) or ~0.9 (m). Check `IfcMapConversion.Scale` vs `IfcProjectedCRS.MapUnit` |
| Eastings/Northings are 0 | Export base was Shared Coordinates or no PBP coordinates entered [snippet, 28][33] | Look for `IFCMAPCONVERSION` line; values 0. |
| Wrong EPSG | Name missing, multiple codes in Name, or a code that is horizontal-only in a 3D context [2][3] | Read `IfcProjectedCRS.Name` and `MapUnit`; confirm on epsg.org (not fetched) |
| Latitude/longitude wrong or off by km | `RefLatitude/RefLongitude` not WGS84 or from the address geocoder in Revit; `RefElevation` often wrong [20] | Convert DMS to decimal and compare to the CRS point |
| Doors not cutting walls | `IfcRelVoidsElement` missing, or opening placement wrong [14] | Query `IfcOpeningElement` and relations |
| Units bug in Revit 2020 exports | Metre as conversion-based unit with feet factor and unscaled map conversion; fixed in Revit 2021+ (issue #290) [25] | Read unit entities; check if Eastings are 1000x off |
| Storey elevations double-counted | OrthogonalHeight applied both in storey Z and map conversion [20] | Compare storey placement Z with `Elevation` attribute and OrthogonalHeight |

### Check recipe (human or MCP)
1. Read the schema (`FILE_SCHEMA`): IFC2X3 vs IFC4 vs IFC4X3.
2. Read the length unit (`IfcUnitAssignment`).
3. Read the 3D context: `WorldCoordinateSystem`, `TrueNorth`, `Precision`, `HasCoordinateOperation`.
4. Read `IfcMapConversion` + `IfcProjectedCRS` (or IFC2x3 psets on IfcProject/IfcSite).
5. Read `IfcSite` placement, RefLatitude/RefLongitude/RefElevation.
6. Compute absolute positions of site, building, storeys, a few elements; compute bounding box.
7. Compare with the other models / expected survey coordinates; grade the LoGeoRef level (10-50) [15].

---

## Typical questions people ask about this

Real (observed) threads, paraphrased:
1. How should coordinates in `IfcLocalPlacement/IfcCartesianPoint` be handled when georeferencing pushes them into millions? (buildingSMART forum) [18]
2. Which point do `RefLatitude/RefLongitude` refer to, and is the IfcSite origin the WCS or the placement origin? (buildingSMART forum) [17]
3. How to propose standard geolocation property sets for IFC2x3 alongside IfcMapConversion in IFC4? (buildingSMART forum) [19]
4. Why won't IFC files with shared coordinates link correctly in Revit when other viewers show them correctly? (revit-ifc issue) [24]
5. Why are Revit IFC `IfcProjectedCRS` units "feet-based" and the map conversion 1000x off? (revit-ifc issue) [25]
6. Why do I get "The elements in this model are very far from the origin in this exported file" when exporting IFC from Revit? (Autodesk support article, title seen in search results) [28]
7. How do I export the same Revit model to IFC with different real-world locations? (Autodesk support article title) [28]
8. Why is my IFC from Revit far away from the IFC exported from different software? (Autodesk support article title) [28]
9. How do I export a georeferenced model with shared coordinates including correct IFCMAPCONVERSION data from Revit? (Autodesk support article title) [28]
10. Why do Eastings and Northings stay 0 in the export when Coordinate Base = Shared Coordinates? (Autodesk Community thread, snippet) [33]
11. What is the correct way to link IFC files in Revit 2026 so the position matches? [23]

Illustrative (invented, for test design):
12. (illustrative) "Open this IFC and tell me what length unit it uses and what the bounding box of the building is in metres."
13. (illustrative) "Which EPSG code is set in this model and what are its Eastings, Northings and rotation?"
14. (illustrative) "The architect model and the structural model do not overlap. Find out why."
15. (illustrative) "Move the model so the project base point is at E 500123.4, N 5400567.8 in EPSG:25832 and write IfcMapConversion."
16. (illustrative) "This IFC is in feet but my script assumes millimetres. Convert all coordinates and fix the unit assignment."
17. (illustrative) "List all walls whose Body is tessellated rather than SweptSolid."
18. (illustrative) "How far is the site placement from the origin? Is that normal?"
19. (illustrative) "True north in Revit says 23 degrees, what does the IFC contain?"
20. (illustrative) "Why is the door not cutting the wall in the viewer?"
21. (illustrative) "What is the LoGeoRef level of this file?"
22. (illustrative) "Export to IFC4 from Revit: should Coordinate Base be Project Base Point or Survey Point?"
23. (illustrative) "The model is 1000 times larger in the new viewer. What went wrong?"
24. (illustrative) "Does the file size go up if I export as IFC4 Reference View?" (see unverified remark in 1.5)

---

## Common pitfalls and misconceptions

- "Revit has shared coordinates, so IFC has them too." No: IFC has WCS + map conversion; "shared coordinates" is Autodesk-specific [24].
- "Setting latitude/longitude in IfcSite is georeferencing." It is only LoGeoRef 20, approximate, WGS84 only; IfcMapConversion overrides it [9][17][18].
- "TrueNorth and IfcMapConversion rotation both apply." They don't; TrueNorth is informational when a coordinate operation exists [6].
- "Large coordinates are fine because IFC stores doubles." The file is fine, the viewers/kernels are not [18][22].
- "A wall with no hole has no door." Openings are separate entities [14].
- "Representation[0] is the Body." Not guaranteed; select by RepresentationIdentifier = 'Body' (and consider Axis, FootPrint, Box) [5].
- "Units: IFC is always millimetres." No. Read `IfcUnitAssignment`; metres and feet are common [8][7].
- "MapUnit is irrelevant." If omitted it defaults to the project units, which can silently be wrong if the CRS is in metres but the project is in mm [2].
- "Revit Project Base Point can be placed anywhere without side effects." Moving it alone does not move elements; the model must be positioned relative to survey point first (community answer, snippet) [28].
- In Revit IFC exports, duplicate georeference info (map conversion + IfcSite location + storey Z offset) is common and needs post-processing (IfcPatch recipes `ResetSpatialElementLocations`, `OffsetStoreyElevations`, `SetRefElevation` as described by an OSArch wiki author) [20].
- Single CRS only: no established way to carry several CRSs in one Revit export [20].

---

## Gaps

- buildingSMART HTML spec pages and Autodesk support articles were not fetchable (HTTP 403); facts were taken from the buildingSMART GitHub docs and search snippets. Revit "Coordinate Base" option wording should be re-checked in the Revit version being tested (QA: the four base names were confirmed on the 25.2 exporter help; the two True-North variants come from the exporter resource file).
- QA 2026-11-06 re-verified against GitHub sources: `IfcProjectedCRS` EPSG examples (EPSG:5555 = ETRS89 / UTM zone 32N + DHHN92 height; EPSG:9286 = ETRS89 + NAP height; EPSG:9306 = HS2 Survey Grid + HS2-VRF height), `IfcUnitAssignment` rule WR01 and single monetary unit, `IfcGeometricRepresentationContext` (TrueNorth informational when a coordinate operation exists). Not re-verified: LoGeoRef literature (secondary), Autodesk articles (403), Revit 16 km figure, `PointCloud` deprecation in 4.3.2.0, sub-context identifier list.
- LoGeoRef original papers (FIG 2018, ISPRS 2024) and the buildingSMART User Guide for Geo-referencing PDF could not be read as text; definitions come from the City2BIM IFCGeoRefChecker wiki.
- Not verified: ContextIdentifier values, exact behaviour of IFC4 Reference View vs Design Transfer View regarding tessellation, IfcRigidOperation details, Archicad Survey Point behaviour, Bonsai/web-ifc docs (pages were 404/unreachable).
- Search budget was exhausted before native-language searches (German, Russian, Chinese, Japanese) could be performed; national georeferencing practice (e.g. German ETRS89/UTM, Dutch RD/NAP, British grids) is covered only by the examples in the spec [2][16].
- Suspicious/skipped sites: none encountered.

---

## Sources

1. IfcMapConversion (IFC4.3.x docs source) https://github.com/buildingSMART/IFC4.3.x-development/blob/master/docs/schemas/resource/IfcRepresentationResource/Entities/IfcMapConversion.md ; official page (seen in search, not fetchable): https://standards.buildingsmart.org/IFC/RELEASE/IFC4_3/HTML/lexical/IfcMapConversion.htm
2. IfcProjectedCRS https://github.com/buildingSMART/IFC4.3.x-development/blob/master/docs/schemas/resource/IfcRepresentationResource/Entities/IfcProjectedCRS.md ; official: https://ifc43-docs.standards.buildingsmart.org/IFC/RELEASE/IFC4x3/HTML/lexical/IfcProjectedCRS.htm
3. IfcCoordinateReferenceSystem https://github.com/buildingSMART/IFC4.3.x-development/blob/master/docs/schemas/resource/IfcRepresentationResource/Entities/IfcCoordinateReferenceSystem.md
4. IfcLocalPlacement https://github.com/buildingSMART/IFC4.3.x-development/blob/master/docs/schemas/resource/IfcGeometricConstraintResource/Entities/IfcLocalPlacement.md
5. IfcShapeRepresentation https://github.com/buildingSMART/IFC4.3.x-development/blob/master/docs/schemas/resource/IfcRepresentationResource/Entities/IfcShapeRepresentation.md
6. IfcGeometricRepresentationContext https://github.com/buildingSMART/IFC4.3.x-development/blob/master/docs/schemas/resource/IfcRepresentationResource/Entities/IfcGeometricRepresentationContext.md
7. IfcConversionBasedUnit https://github.com/buildingSMART/IFC4.3.x-development/blob/master/docs/schemas/resource/IfcMeasureResource/Entities/IfcConversionBasedUnit.md
8. IfcUnitAssignment https://github.com/buildingSMART/IFC4.3.x-development/blob/master/docs/schemas/resource/IfcMeasureResource/Entities/IfcUnitAssignment.md ; official: https://standards.buildingsmart.org/IFC/RELEASE/IFC4_3/HTML/lexical/IfcUnitAssignment.htm ; Project Units concept (search result): https://ifc43-docs.standards.buildingsmart.org/IFC/RELEASE/IFC4x3/HTML/concepts/Project_Context/Project_Units/content.html
9. IfcSite https://github.com/buildingSMART/IFC4.3.x-development/blob/master/docs/schemas/core/IfcProductExtension/Entities/IfcSite.md
10. IfcTriangulatedFaceSet https://github.com/buildingSMART/IFC4.3.x-development/blob/master/docs/schemas/resource/IfcGeometricModelResource/Entities/IfcTriangulatedFaceSet.md
11. IfcPolygonalFaceSet https://github.com/buildingSMART/IFC4.3.x-development/blob/master/docs/schemas/resource/IfcGeometricModelResource/Entities/IfcPolygonalFaceSet.md
12. IfcExtrudedAreaSolid https://github.com/buildingSMART/IFC4.3.x-development/blob/master/docs/schemas/resource/IfcGeometricModelResource/Entities/IfcExtrudedAreaSolid.md
13. IfcBooleanClippingResult https://github.com/buildingSMART/IFC4.3.x-development/blob/master/docs/schemas/resource/IfcGeometricModelResource/Entities/IfcBooleanClippingResult.md
14. IfcOpeningElement https://github.com/buildingSMART/IFC4.3.x-development/blob/master/docs/schemas/core/IfcProductExtension/Entities/IfcOpeningElement.md
15. IFCGeoRefChecker (City2BIM wiki, community/academic tool) https://github.com/dd-bim/City2BIM/wiki/IFCGeoRefChecker
16. buildingSMART BIM Fit Check, georeferencing results (Intergeo agenda page) https://programm.dvw.de/intergeo-agenda-en/ergebnisse-des-buildingsmart-bim-fit-check-zur-georeferenzierung-und-trassierung
17. Forum: WorldCoordinateSystem, IfcMapConversion and IfcSite (community) https://forums.buildingsmart.org/t/worldcoordinatesystem-ifcmapconversion-and-ifcsite/1924
18. Forum: Coordinates of the IfcLocalPlacement/IfcCartesianPoint (community) https://forums.buildingsmart.org/t/coordinates-of-the-ifclocalplacement-ifccartesianpoint/1809
19. Forum: Geolocation standards in IFC2X3 and IFC4 (community) https://forums.buildingsmart.org/t/geolocation-standards-in-ifc2x3-and-ifc4/2329
20. OSArch wiki, Revit IFC geolocation (enthusiast/community) https://wiki.osarch.org/revit-setup-for-openbim-revit-ifc-geolocation/
21. IFC Coordinate Reference Systems and Revit (blog, enthusiast) https://thinkmoult.com/ifc-coordinate-reference-systems-and-revit.html
22. Revit, IFC and coordinate systems (blog) https://bim-me-up.com/en/revit-ifc-and-coordinate-systems/
23. Linking IFC to Revit 2026 (blog) https://bimcorner.com/linking-ifc-to-revit-2026/
24. Autodesk/revit-ifc issue 566 "IFC to Revit (shared coordinates)" https://github.com/Autodesk/revit-ifc/issues/566
25. Autodesk/revit-ifc issue 290 "ProjectedCRS units" https://github.com/Autodesk/revit-ifc/issues/290
26. IfcOpenShell util/unit.py (v0.8.0) https://raw.githubusercontent.com/IfcOpenShell/IfcOpenShell/v0.8.0/src/ifcopenshell-python/ifcopenshell/util/unit.py
27. IfcOpenShell util/geolocation.py (v0.8.0) https://raw.githubusercontent.com/IfcOpenShell/IfcOpenShell/v0.8.0/src/ifcopenshell-python/ifcopenshell/util/geolocation.py
28. Autodesk support articles (seen only as search results/snippets, pages returned 403):
    - https://www.autodesk.com/support/technical/article/caas/sfdcarticles/sfdcarticles/The-elements-in-this-model-are-very-far-from-the-origin-in-this-exported-file-exporting-IFC-from-Revit.html
    - https://www.autodesk.com/support/technical/article/caas/sfdcarticles/sfdcarticles/How-to-export-the-same-Revit-model-to-IFC-using-different-real-world-locations.html
    - https://www.autodesk.com/support/technical/article/caas/sfdcarticles/sfdcarticles/IFC-File-exporting-with-wrong-Coordinates-in-Revit.html
    - https://www.autodesk.com/support/technical/article/caas/sfdcarticles/sfdcarticles/IFC-model-exported-from-Revit-far-away-from-IFC-model-exported-from-different-software.html
    - https://www.autodesk.com/support/technical/article/caas/sfdcarticles/sfdcarticles/How-to-export-georeferenced-model-with-shared-coordinates-to-IFC-including-correct-IFCMAPCONVERSION-data-from-Revit.html
29. buildingSMART User Guide for Geo-referencing in IFC v2.0 (seen in search, not readable) https://www.buildingsmart.org/wp-content/uploads/2020/02/User-Guide-for-Geo-referencing-in-IFC-v2.0.pdf
30. FIG 2018 LoGeoRef presentation (seen, PDF unreadable) https://www.fig.net/resources/proceedings/2018/05_bim/FIG2018_BIM_and_Surveying_03_02_IFC_Clemen.pdf
31. ISPRS Archives 2024 georeferencing paper (seen, PDF unreadable) https://isprs-archives.copernicus.org/articles/XLVIII-4-W11-2024/41/2024/isprs-archives-XLVIII-4-W11-2024-41-2024.pdf
33. Autodesk Community, Coordinate Base setting during IFC export (search snippet; 403) https://forums.autodesk.com/t5/revit-api-forum/coordinate-base-setting-during-ifc-export/td-p/14004716
34. Graphisoft Community, Survey Point supported at IFC import/export (title only; 403) https://community.graphisoft.com/t5/Collaboration-with-other/Survey-Point-is-now-supported-at-IFC-import-export/ta-p/304009
35. IFC 2x2 MeasureUnit Examples (search result) https://iaiweb.lbl.gov/Resources/IFC_Releases/R2x3_final/ifcmeasureresource/lexical/text/IFC_2x2_MeasureUnit_Examples.pdf
36. Autodesk/revit-ifc wiki index (page "Mapping geo reference in IFC4" has only images) https://github.com/Autodesk/revit-ifc/wiki/Mapping-geo-reference-in-IFC4
