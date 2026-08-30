# TIR Completion Frontier v0.5

Status: `CARTAN_REFINEMENT_CURVATURE_TORSION_SEPARATED / ZERO_TORSION_SELECTION_NEXT / EINSTEIN_SELECTION_CROSSLINK_AVAILABLE`

Date: 2026-08-30

Parent frontier: `TIR_COMPLETION_FRONTIER_V0_4.md`.

## 1. Gate A2 advancement

The discrete Universal-Loop torsion source of v0.4 has now been extended to the general non-rotationally-closed `SE(3)` loop.

For

\[
G_C=G_{xy}G_{yz}G_{zx}=(R_C,\mathbf t_C),
\]

the exact identity is

\[
\boxed{
\mathbf t_C
=\operatorname{vec}(\mathcal T_{xyz})
+(I-R_C)\mathbf e_{xz}.
}
\]

For a regular shrinking family,

\[
\mathbf e_{xz}=O(\epsilon),
\qquad
R_C-I=O(\epsilon^2),
\qquad
A_C=\Theta(\epsilon^2),
\]

so

\[
(I-R_C)\mathbf e_{xz}=O(\epsilon^3).
\]

Therefore

\[
\boxed{
\lim_{\epsilon\to0}
\frac{\mathbf t_C}{A_C}
=
\lim_{\epsilon\to0}
\frac{\operatorname{vec}(\mathcal T_{xyz})}{A_C}
=T(u,v)
}
\]

whenever the declared smooth coframe/connection refinement hypotheses hold.

The rotational limit remains independently

\[
\boxed{
\frac{R_C-I}{A_C}
\to\Omega(u,v).
}
\]

Thus the continuum Cartan coordinates are separated:

```text
translation / area -> T^a
rotation / area    -> Omega^a_b
```

Canonical theorem:

`TIR/foundations/TIR_CARTAN_REFINEMENT_CURVATURE_TORSION_SEPARATION_V0_1.md`.

## 2. Curvature firewall

The spatial GR sector may satisfy

\[
T^a=0
\]

while retaining

\[
\Omega^a{}_b\ne0.
\]

The deterministic Gate A2 family explicitly verifies this separation: zero discrete torsion coexists with a nonzero `O(epsilon^2)` rotational defect, while the induced finite-loop translational correction is only `O(epsilon^3)`.

Status:

`PASS_CURVATURE_TORSION_ORDER_SEPARATION`.

## 3. Next Gate A3 — zero-torsion / Levi-Civita selection

The remaining spatial-GR selection is now one sharply typed question:

\[
\boxed{
\text{Why does the physical TIR connection select }T^a=0?
}
\]

Already available parents:

1. intrinsic affine relation is the unique torsor displacement;
2. same-carrier endpoint composition is exact;
3. local spatial metric is positive and rank three;
4. discrete solder and translational holonomy share the same area-normalized Cartan limit;
5. curvature remains an independent rotational channel.

The next theorem must bind the physical connection to the metric/coframe carrier without importing an independent torsional degree of freedom by assumption.

Candidate theorem routes remain theorem-gated:

```text
A. intrinsic endpoint uniqueness + connection compatibility
B. metric compatibility + TIR minimality -> Levi-Civita uniqueness
C. two-path refinement equality through O(area)
```

GREMLIN may rank A/B/C but cannot promote one.

## 4. Relativistic cross-repository line

RFC now has an independent RF-E21 selection gate on draft PR #91. On the standard four-dimensional Lovelock premises it selects

\[
G_{\mu\nu}+\Lambda g_{\mu\nu}
\]

as the metric-side tensor form, while keeping project-owned prerequisites explicit.

The source-owned TIR dependency is therefore

```text
Gate A   discrete torsion source
 -> Gate A2 Cartan refinement and curvature/torsion separation
 -> Gate A3 zero-torsion / Levi-Civita selection
 -> TIR x IDT four-dimensional covariant carrier
 -> RFC RF-E21 Einstein tensor-form selection
 -> RFC RF-E3 coupling normalization
 -> RFC RF-E12/RF-E13 ADM constraints/evolution
```

No merge/promotion into TIR `main` is implied by this frontier document; hosted validation remains attached to the exact feature-branch commit.

## 5. Validation receipt

Local deterministic Gate A2 receipt before hosted validation:

```text
general SE(3) translation decomposition        PASS
Gate-A rotational closure roundtrip            PASS
discrete torsion area coefficient              PASS
curvature correction exact identity            PASS
curvature contamination slope                  2.9549696910 ~ O(epsilon^3)
rotational holonomy slope                      1.9999902811 ~ O(epsilon^2)
area-normalized translation convergence         PASS
zero torsion with nonzero curvature             PASS
pure-atlas exact-zero baseline                  PASS
```

Hosted authority:

`.github/workflows/tir-cartan-refinement-curvature-torsion.yml`.
