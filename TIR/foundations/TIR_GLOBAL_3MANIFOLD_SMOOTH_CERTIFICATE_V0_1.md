# TIR Global 3-Manifold and Smooth-Realization Certificate v0.1

Status: `EXACT_COMBINATORIAL_MANIFOLD_CERTIFICATE / STANDARD_MOISE_SMOOTHING_BRIDGE / GLOBAL_METRIC_LEVI_CIVITA_GLUE_PASS_ON_CERTIFICATE / ACTUAL_RELATIONAL_COMPLEX_CERTIFICATE_OPEN`

Date: 2026-08-30

## 1. Purpose

Gates A2--A4 close the local spatial-GR continuum chain:

\[
\text{discrete relation complex}
\to(T^a,\Omega^a{}_b)
\to T^a=0
\to D=D^{LC}
\to \text{leading metric jet order }\le2.
\]

Gate A5 turns the remaining phrase `global smooth refinement` into an executable topological certificate.

The central question is now:

\[
\boxed{\text{Does the global relational cell complex realize a combinatorial 3-manifold?}}
\]

If that certificate passes, standard three-dimensional topology supplies the smooth realization; smoothness need not be introduced as a separate primitive assumption.

## 2. Simplicial carrier

Let the admitted finite or locally finite spatial relational cell complex be triangulated consistently to a pure three-dimensional simplicial complex

\[
K=(V,E,F,\mathcal T),
\]

where every maximal simplex is a tetrahedron.

A hexahedral or other polyhedral realization may enter Gate A5 through a compatible simplicial subdivision. The subdivision is a representation of the same PL carrier and must preserve face identifications.

This gate first implements the closed, boundary-free certificate. Boundary sectors can be added with the standard sphere/ball link distinction in a later extension.

## 3. Closed combinatorial 3-manifold certificate

For a finite pure tetrahedral complex, Gate A5 requires:

1. every tetrahedron has four distinct vertices;
2. no tetrahedron is duplicated;
3. the tetrahedron adjacency graph is connected;
4. every triangular face is incident to exactly two tetrahedra;
5. for every vertex `v`, the simplicial link
   \[
   \operatorname{Lk}_K(v)
   \]
   is a connected closed triangulated two-manifold;
6. every vertex link has Euler characteristic
   \[
   \boxed{\chi(\operatorname{Lk}_K(v))=2.}
   \]

The validator certifies the two-manifold condition in each vertex link by checking:

- every link edge belongs to exactly two link triangles;
- the link triangle adjacency graph is connected;
- the link of every link-vertex is one connected cycle.

For a connected closed triangulated surface, the surface-classification theorem then gives

\[
\chi=2
\Longrightarrow
\operatorname{Lk}_K(v)\cong S^2.
\]

Hence every vertex has a neighborhood PL-homeomorphic to a 3-ball, and `K` is a closed combinatorial 3-manifold.

## 4. Moise bridge

The standard three-dimensional Moise theorem supplies the next category bridge. A topological 3-manifold admits a compatible PL structure unique up to the appropriate PL equivalence, and a PL 3-manifold is smoothable with a compatible smooth structure unique up to the corresponding smooth equivalence.

Therefore, once Gate A5 certifies that the relational carrier is a combinatorial 3-manifold,

\[
\boxed{
|K|\text{ combinatorial 3-manifold}
\Longrightarrow
|K|\text{ smooth 3-manifold}
}
\]

by standard three-dimensional topology.

External theorem anchor:

E. E. Moise, *Geometric Topology in Dimensions 2 and 3*, Springer, 1977, together with the classical Moise triangulation/uniqueness results for 3-manifolds.

## 5. Relational cocycle to atlas

The existing TIR relational cocycle theorem supplies, on a contractible local relation set,

\[
\boxed{\mathcal E_{xy}=r(y)-r(x)}
\]

and exact additive endpoint composition. The anchored `SE(3)` source theorem supplies exact overlap cocycles for ordinary affine chart changes.

Thus on the certified combinatorial-manifold carrier, local TIR relation neighborhoods provide the affine coordinate data while the topological certificate guarantees that those neighborhoods assemble into a global 3-manifold atlas.

The pure-atlas cocycle remains distinct from physical connection holonomy, preserving the existing curvature firewall.

## 6. Global metric gluing

Let `U_A,U_B` be overlapping local TIR spatial patches with coframes related by

\[
\boxed{e_{(B)}=R_{BA}e_{(A)},\qquad R_{BA}:U_A\cap U_B\to SO(3).}
\]

Each local metric is

\[
h_{(A)}=\delta_{ab}e_{(A)}^a\otimes e_{(A)}^b.
\]

Since

\[
R_{BA}^{\mathsf T}R_{BA}=I,
\]

one obtains identically on the overlap

\[
\boxed{h_{(B)}=h_{(A)}.}
\]

Therefore compatible local TIR metrics define one global positive spatial metric

\[
\boxed{h\in\Gamma(S^2T^*\Sigma)}
\]

on the certified smooth 3-manifold `Sigma=|K|`.

## 7. Global Levi-Civita gluing

Gate A3 gives on every local GR patch

\[
T^a=0,
\qquad
Dh=0,
\qquad
D=D^{LC}.
\]

Once the local metrics agree on overlaps, the fundamental theorem of Riemannian geometry gives a unique Levi-Civita connection for the global metric `h`. Its restriction to every patch is the already selected local Levi-Civita connection.

Hence

\[
\boxed{
\text{A5 manifold certificate}
+\text{SO(3) metric cocycle}
+\text{A3 local Levi-Civita}
\Longrightarrow
(h,D^{LC})\text{ globally on }\Sigma.
}
\]

Curvature remains globally represented by the curvature of this connection and may be nonzero.

## 8. What remains data-dependent

Gate A5 separates a standard theorem from a concrete repository datum.

The theorem/certifier is complete for a supplied closed tetrahedral complex. Promotion of the actual TIR global relational carrier requires a frozen machine-readable tetrahedralization or equivalent cell-complex incidence table and a PASS receipt from the certifier.

Current status:

```text
combinatorial 3-manifold certifier                   IMPLEMENTED
positive control: boundary of 4-simplex = S^3        PASS TARGET
open-face negative control                            FAIL TARGET
disconnected negative control                        FAIL TARGET
duplicate-cell negative control                      FAIL TARGET
actual global TIR relational-complex incidence data  OPEN INPUT
```

Thus the remaining global issue is now an evidence/input gate rather than an unspecified smoothness assumption.

## 9. Spacetime interface

Gate A5 owns the global spatial slice. The four-dimensional RFC/IDT join additionally requires the admitted temporal carrier/foliation to extend over the certified spatial manifold. RF-G0/RF-E8 already close that join locally.

The global spacetime promotion line is therefore

```text
A5 certified global spatial 3-manifold + global h, D^LC
+ IDT global temporal orientation/foliation certificate
-> global Lorentzian spacetime carrier
-> RF-E24 local Einstein equation on every chart
-> globally compatible Einstein system
```

This keeps spatial topology and temporal foliation as separately testable inputs.

## 10. Claim ledger

| Claim | Status |
|---|---|
| face-incidence and vertex-link certificate implemented | `PASS EXECUTABLE CONTRACT` |
| connected closed 2-manifold link with `chi=2` is `S^2` | `STANDARD SURFACE CLASSIFICATION` |
| all vertex links `S^2` imply closed combinatorial 3-manifold | `STANDARD PL TOPOLOGY` |
| combinatorial/PL 3-manifold admits compatible smooth realization | `STANDARD MOISE BRIDGE` |
| `SO(3)`-related coframes give identical overlap metrics | `EXACT` |
| compatible local metrics glue globally | `STANDARD SHEAF/ATLAS GLUING` |
| local A3 Levi-Civita restrictions glue to global `D^LC` | `EXACT BY UNIQUENESS` |
| actual TIR global complex passes certificate | `OPEN INPUT/VALIDATION` |
| global IDT temporal foliation over certified space | `CROSS-REPOSITORY GATE` |

## 11. Validation authority

Deterministic certifier:

`TIR/foundations/validation/tir_global_3manifold_smooth_certificate_v0_1.py`

Static receipt:

`TIR/foundations/validation/TIR_GLOBAL_3MANIFOLD_SMOOTH_CERTIFICATE_V0_1.json`

Hosted workflow:

`.github/workflows/tir-global-3manifold-smooth-certificate.yml`

Verdict target for the certifier implementation:

`PASS_TIR_GLOBAL_3MANIFOLD_SMOOTH_CERTIFIER`

The distinct promotion verdict for an actual frozen TIR global complex is reserved as

`PASS_TIR_GLOBAL_RELATIONAL_COMPLEX_3MANIFOLD_CERTIFICATE`.
