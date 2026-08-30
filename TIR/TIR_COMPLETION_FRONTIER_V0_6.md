# TIR Completion Frontier v0.6

Status: `CARTAN_REFINEMENT_PASS / ZERO_TORSION_LEVI_CIVITA_SELECTION_PASS_ON_REGULAR_ENDPOINT_COMPATIBLE_REFINEMENT / GLOBAL_CONTINUUM_EXISTENCE_NEXT`

Date: 2026-08-30

Parents:

- `TIR_COMPLETION_FRONTIER_V0_5.md`
- `TIR_CARTAN_REFINEMENT_CURVATURE_TORSION_SEPARATION_V0_1.md`
- `TIR_RELATIONAL_ENDPOINT_CLOSURE_V0_1.md`

## 1. Gate A3 result

The spatial GR branch now has a typed zero-torsion selection theorem.

The intrinsic TIR relation is the unique affine endpoint displacement. Whenever the direct `x -> z` relation and the connection-composed `x -> y -> z` description are admitted as representations of the same primitive endpoint relation in the same comparison frame, uniqueness selects

\[
\boxed{\mathcal C_{xyz}=0}.
\]

The exact parent identity

\[
\mathcal T_{xyz}=-\mathcal C_{xyz}
\]

therefore gives

\[
\boxed{\mathcal T_{xyz}=0}.
\]

Gate A2 transfers this discrete condition to a regular continuum refinement:

\[
\boxed{T^a=de^a+\omega^a{}_b\wedge e^b=0}.
\]

The `SO(3)` relation-frame connection is metric-preserving, so

\[
Dh=0.
\]

The fundamental theorem of Riemannian geometry then selects the unique spatial connection

\[
\boxed{D=D^{\rm LC}}.
\]

Canonical theorem:

`TIR/foundations/TIR_ZERO_TORSION_LEVI_CIVITA_SELECTION_V0_1.md`.

## 2. Branch typing

The result is a spatial-GR sector selection, not a deletion of the broader Cartan channel.

```text
primitive same-endpoint compatible sector
 -> C_xyz=0
 -> T_xyz=0
 -> T^a=0
 -> Levi-Civita

context-lifted endpoint defect
 -> C_xyz retained
 -> torsion source retained
 -> broader Cartan branch
```

A8 therefore remains available as the context-bearing closure mechanism for nonzero endpoint defects.

## 3. Curvature survives

Gate A2 proves the exact general identity

\[
\mathbf t_C
=\operatorname{vec}(\mathcal T_{xyz})
+(I-R_C)\mathbf e_{xz}.
\]

For shrinking loops,

\[
R_C-I=O(\epsilon^2),
\qquad
\mathbf e_{xz}=O(\epsilon),
\]

so the curvature-induced translational correction is only `O(epsilon^3)`.

Consequently the selected spatial GR sector admits

\[
\boxed{T^a=0,\qquad \Omega^a{}_b\ne0}.
\]

The deterministic A3 validator explicitly checks this regime.

## 4. Remaining spatial/global theorem

The local/refining Levi-Civita selection is closed on the declared regular refinement hypotheses. The remaining source-owned geometry question is existence and global stability:

\[
\boxed{
\text{Does the full relational cell complex admit a globally compatible smooth refinement carrying }(e^a,h,D^{LC},\Omega)?
}
\]

This requires control of:

```text
cell refinement compatibility
overlap cocycles
nondegenerate coframe rank
regularity of the metric limit
connection convergence
global topology / spin-lift compatibility where used
```

Status:

`GLOBAL_CONTINUUM_EXISTENCE_NEXT`.

## 5. Relativistic dependency line

The GR line is now

```text
TIR primitive relation
 -> rank-3 spatial carrier
 -> solder/coframe
 -> metric h
 -> spatial connection / holonomy
 -> Gate A torsion source
 -> Gate A2 Cartan refinement
 -> Gate A3 zero-torsion / Levi-Civita selection
 -> GLOBAL CONTINUUM EXISTENCE
 + IDT temporal orientation / lapse
 -> 4D Lorentzian / ADM carrier
 -> 4D covariance / naturality / second-order locality
 -> RFC RF-E21 Lovelock Einstein-form selection
 -> RFC RF-E3 normalization
 -> RFC RF-E12/RF-E13 constraints and evolution
```

The remaining gap to project-level Einstein closure is therefore no longer local spatial torsion selection.

## 6. Local validation receipt

Before hosted CI, Gate A3 returned:

```text
intrinsic affine endpoint composition              PASS
same-endpoint independent local-frame closure      PASS
C=0 iff discrete T=0                               PASS
SO(3) metric compatibility                         PASS
zero-torsion translation/area limit                PASS
zero torsion with nonzero curvature                PASS
torsional extension fail-closed witness            PASS
claim/parent firewalls                              PASS
```

Local verdict:

`PASS_TIR_ZERO_TORSION_LEVI_CIVITA_SELECTION`.

The hosted workflow reruns Gate A2 and Gate A3 on the same exact PR head:

`.github/workflows/tir-spatial-gr-levi-civita.yml`.
