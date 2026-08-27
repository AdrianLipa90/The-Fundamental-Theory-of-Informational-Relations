# TIR Polygonal Excitation — Stage 67 Source-Carrying Materiality Threshold v0.1

Status: `STAGE_67_STRUCTURAL_MATERIAL_CARRIER_PASS__MASS_NORMALIZATION_AND_PHYSICAL_MATERIALITY_OPEN`

## Purpose

This stage tests the GREMLIN-generated relational isomorphism

```math
\text{terminal geometric boundary}
\;\longrightarrow\;
\text{independent gauge-matter source degree}
\;\longrightarrow\;
\text{sourced matter carrier}
```

using only already admitted TIR geometry and gauge-matter artifacts.

Promotion is controlled by the executable gate and source receipts. GREMLIN supplies the candidate relation and audit target.

## 1. Strict equal-edge geometric boundary

Stage 1 derived the strong equal-edge continuation

```math
c_N=\frac{\cos(2\pi/N)}{1-\cos(2\pi/N)},
\qquad
r_N^2=1-c_N^2.
```

The deterministic replay gives

```text
N=3  c_N=-1/3                  nondegenerate
N=4  c_N=0                     nondegenerate
N=5  c_N=1/sqrt(5)             nondegenerate
N=6  c_N=1, r_N=0              degenerate terminal boundary
N=7  c_N=1.655970555...        outside the unit-sphere branch
```

Hence the strict equal-edge continuation encounters a sharp type boundary at `N=6`:

```math
\boxed{
N=6:\;r_6=0,
\qquad
N>6:\;c_N>1.
}
```

The canonical Stage-67 meaning of the later `6+1` notation therefore uses `6` as the terminal strict-geometric boundary. A literal seven-vertex continuation is a separate geometric construction; under the frozen strict equal-edge rule the `N=7` member lies outside the unit sphere.

## 2. Existing gauge-matter source degree

Stage 27 has already established the local gauge scalar

```math
\boxed{
B_{ij}=q_i^\dagger W_{ij}q_j
}
```

with

```math
B'_{ij}=B_{ij}.
```

Stage 28 combines the color loop and quark-link terms into

```math
S_{\rm graph}[W,q]
=
\beta\sum_p\left(3-\operatorname{Re}\operatorname{Tr}U_p\right)
-
\eta\sum_{\langle ij\rangle,f}
\operatorname{Re}\left(q_{i,f}^\dagger W_{ij}q_{j,f}\right),
```

and verifies exact local gauge invariance independently of the real coefficients `beta` and `eta`.

The Stage-27 and Stage-28 receipts both report `PASS`.

## 3. The `6+1` sourced extension

Define the typed sourced carrier

```math
\boxed{
\mathcal C_{6+1}
=
\left(\mathcal C_{6}^{\rm geom},\;\mathcal S_{qW}\right),
\qquad
\mathcal S_{qW}
:=\operatorname{Re}\left(q_i^\dagger W_{ij}q_j\right).
}
```

The two entries have different roles:

```text
C_6^geom : terminal strict-geometric boundary state
S_qW     : independent gauge-matter source degree
```

The label `septahedral` is therefore typed in this stage as

```text
SEPTAHEDRAL_6_PLUS_1 := GEOMETRIC_SIX_BOUNDARY + SOURCE_ONE.
```

This is a source-extension label. The geometric `N=7` strict equal-edge branch remains governed by the Stage-1 result above.

## 4. Nonzero source witness

The reference implementation constructs a deterministic witness with

```math
q_i=q_j=e_1,
\qquad
W_{ij}=I_3,
```

so

```math
B_{ij}=1.
```

Apply independent endpoint transformations in the diagonal `U(1)\subset SU(3)` subgroup,

```math
G_i=\operatorname{diag}(e^{i\alpha},e^{-i\alpha},1),
\qquad
G_j=\operatorname{diag}(e^{i\beta},e^{-i\beta},1),
```

with

```math
W'_{ij}=G_iW_{ij}G_j^\dagger.
```

The replay returns

```text
B_before = 1
B_after  = 1 + O(10^-17)i
gauge residual = 2.237726045655905e-16
```

so the source degree has an explicit nonzero gauge-invariant representative in addition to the general Stage-27 proof.

## 5. Structural material-carrier predicate

The current gate admits the structural predicate

```math
\boxed{
\mathfrak M_{\rm struct}(\mathcal C)=1
\iff
\begin{cases}
\mathcal C\text{ reaches the strict }N=6\text{ geometric boundary},\\
\mathcal S_{qW}\text{ exists as a gauge scalar},\\
\mathcal S_{qW}\neq0\text{ for an admitted state},\\
S_{\rm graph}[W,q]\text{ is locally gauge invariant}.
\end{cases}
}
```

All four structural checks pass.

This is the exact point at which the candidate relation changes type from a purely geometric carrier to a sourced gauge-matter carrier.

## 6. Mass and physical-materiality gate

The active TIR mass provenance remains decisive here. The superseding v10.2r1 audit reports

```text
physical_mass_spectrum_status = FAIL_OPEN
debt9_status                   = OPEN_NOT_CLOSED
canon_allowed                  = false
mass_derivation_claimed        = false
current_promotion              = DENY_CURRENT
```

Therefore Stage 67 records the downstream chain as

```math
\boxed{
\mathcal C_{6+1}
\longrightarrow
E_{\rm bound}
\longrightarrow
M_{\rm bound}
\longrightarrow
T_{\mu\nu}
}
```

with the final three arrows retained as explicit open gates.

A later physical-materiality promotion requires an executable route for at least:

```text
1. bound-state / localized positive energy,
2. absolute mass normalization with admissible provenance,
3. conserved continuum source or stress-energy,
4. a volume/scale map sufficient to form rho_m,
5. independent validation after the operator is frozen.
```

The current Stage-67 result is therefore stronger than a numerical coincidence and narrower than a complete mass derivation.

## 7. RFC export interface

The clean downstream interface is

```math
\boxed{
\mathcal C_{6+1}
\xrightarrow{\;\text{future energy/mass gate}\;}
M_C
\xrightarrow{\;V_C\;}
\rho_m
\xrightarrow{\;\text{RFC}\;}
\text{continuum source equations}.
}
```

TIR owns the discrete geometric boundary and gauge-matter carrier. RFC can consume the later normalized `rho_m` only after the TIR mass/source gate closes.

## Verdict

```text
strict N=6 boundary replay:                    PASS
strict N=7 continuation under same rule:       OUTSIDE_UNIT_SPHERE
Stage-27 gauge-invariant quark-link source:     PASS
Stage-28 discrete gauge-matter action:          PASS
nonzero gauge-invariant source witness:         PASS
structural sourced matter carrier:              PASS
absolute mass normalization:                    OPEN
bound-state energy:                             OPEN
continuum stress-energy:                        OPEN
physical materiality:                           OPEN
```

Final Stage-67 status:

`STAGE_67_STRUCTURAL_MATERIAL_CARRIER_PASS__MASS_NORMALIZATION_AND_PHYSICAL_MATERIALITY_OPEN`

## Reproducibility

Executable:

`TIR/frozen_predictions/validation/scripts/materiality_threshold_stage67_v01.py`

Receipt:

`TIR/frozen_predictions/validation/results/TIR_POLYGONAL_STAGE67_MATERIALITY_THRESHOLD_RECEIPT_V0_1.json`
