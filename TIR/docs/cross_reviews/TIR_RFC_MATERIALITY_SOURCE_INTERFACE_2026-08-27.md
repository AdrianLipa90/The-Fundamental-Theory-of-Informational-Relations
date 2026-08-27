# TIR × RFC cross-review — sourced material carrier interface

Date: 2026-08-27

Status: `STRUCTURAL_SOURCE_INTERFACE_PASS / MASS_DENSITY_EXPORT_OPEN`

## Result

The current TIR dependency chain supports a typed source interface

```math
\boxed{
\text{strict polygonal geometry}
\rightarrow
N=6\text{ terminal boundary}
\rightarrow
(q,W)\text{ gauge-matter source degree}
\rightarrow
\mathcal C_{6+1}^{\rm sourced}.
}
```

The geometric part is fixed by the Stage-1 equal-edge continuation,

```math
c_N=\frac{\cos(2\pi/N)}{1-\cos(2\pi/N)},
\qquad
r_N^2=1-c_N^2,
```

which gives

```math
c_6=1,
\qquad
r_6=0,
```

and places the strict `N=7` continuation outside the unit-sphere branch.

The source part is supplied independently by the admitted TIR color/matter sector,

```math
B_{ij}=q_i^\dagger W_{ij}q_j,
```

and by the locally gauge-invariant discrete action

```math
S_{\rm graph}[W,q]
=
\beta\sum_p\left(3-\operatorname{Re}\operatorname{Tr}U_p\right)
-
\eta\sum_{\langle ij\rangle,f}
\operatorname{Re}\left(q_{i,f}^\dagger W_{ij}q_{j,f}\right).
```

Stage 67 therefore types the candidate `6+1` transition as

```math
\boxed{
\mathcal C_{6+1}
=
(\mathcal C_6^{\rm geom},\mathcal S_{qW}),
\qquad
\mathcal S_{qW}=\operatorname{Re}(q_i^\dagger W_{ij}q_j).
}
```

The canonical meaning of the optional `septahedral` label in this interface is `GEOMETRIC_SIX_BOUNDARY + SOURCE_ONE`.

## Dependency ownership

- TIR owns the strict polygonal boundary, the `SU(3)_C` link structure, the quark carrier, the gauge-invariant bilinear, and the discrete gauge-matter action.
- TIR also owns the future admissible energy/mass normalization needed before a matter density can be exported.
- RFC owns the later continuum use of a normalized source density or stress-energy in Newton/Einstein closure tests.
- GREMLIN may propose relational isomorphisms between these layers; executable gates and receipts control promotion.

## Current mass firewall

The active v10.2r1 mass audit classifies the absolute charged-fermion mass closure as

```text
physical_mass_spectrum_status = FAIL_OPEN
debt9_status                   = OPEN_NOT_CLOSED
canon_allowed                  = false
mass_derivation_claimed        = false
```

Accordingly the export chain is frozen as

```math
\boxed{
\mathcal C_{6+1}
\rightarrow
E_C
\rightarrow
M_C
\rightarrow
\rho_m=\frac{M_C}{V_C}
\rightarrow
\text{RFC source equations}
}
```

with `E_C`, `M_C`, `V_C`, and the continuum conservation/stress-energy gate still requiring explicit derivation and validation.

## Evidence

Stage-27 source coupling:

`TIR/frozen_predictions/validation/TIR_POLYGONAL_EXCITATION_STAGE27_GAUGE_INVARIANT_QUARK_LINK_COUPLING_V0_1.md`

Stage-28 gauge-matter action:

`TIR/frozen_predictions/validation/TIR_POLYGONAL_EXCITATION_STAGE28_DISCRETE_GAUGE_MATTER_ACTION_V0_1.md`

Stage-67 threshold audit:

`TIR/frozen_predictions/validation/TIR_POLYGONAL_EXCITATION_STAGE67_MATERIALITY_THRESHOLD_V0_1.md`

Reference executable:

`TIR/frozen_predictions/validation/scripts/materiality_threshold_stage67_v01.py`

Receipt:

`TIR/frozen_predictions/validation/results/TIR_POLYGONAL_STAGE67_MATERIALITY_THRESHOLD_RECEIPT_V0_1.json`

## Next gate

The next admissible question is quantitative:

```math
\boxed{
\text{Can an invariant of the admitted }(q,W)\text{ state determine}
\quad
E_C>0,
\quad
M_C,
\quad
\rho_m
\quad
\text{without target-mass fitting?}
}
```

A successful answer would provide RFC with the missing sourced density input while preserving the present provenance firewall.
