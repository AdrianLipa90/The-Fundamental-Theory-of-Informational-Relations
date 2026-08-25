# TIR Polygonal Excitation — Stage 65 Stationary Ordered-Axis Cubic Selector Freeze v0.1

Status: `STAGE_65_STATIONARY_ORDERED_AXIS_SELECTOR_FROZEN_PREVALIDATION`

Freeze date: `2026-08-25`

## Purpose

Stages 60 and 63 establish a two-dimensional cubic invariant space on the rigid five-dimensional family carrier. Stage 64 records that one additional scalar dynamical condition remains an explicit derivation target.

Stage 65 freezes one minimal variational ansatz before mathematical validation and before any comparison with CKM, masses, or other physical targets.

## Frozen ingredients

Use the already defined cubic invariants

```math
I_{iso}(S)=\operatorname{tr}(S^3),
```

and

```math
I_{A5}(S)=\sum_{a=1}^{6}[\operatorname{tr}(SQ_a)]^3.
```

Use the rigid ordered polygonal axis

```math
D_0=\operatorname{diag}\left(-\frac13,0,\frac1{\sqrt5}\right)
-\frac13\operatorname{tr}\!\left[\operatorname{diag}\left(-\frac13,0,\frac1{\sqrt5}\right)\right]I.
```

The unique quadratic `A5` invariant supplies the norm constraint

```math
\operatorname{tr}(S^2)=\operatorname{tr}(D_0^2).
```

## Frozen ansatz

Fix the projective normalization of the cubic coefficient pair by setting the coefficient of `I_iso` to one:

```math
\boxed{
\mathcal F_\eta(S)=I_{iso}(S)+\eta I_{A5}(S).
}
```

The scalar selector condition is constrained stationarity of the already rigid ordered axis:

```math
\boxed{
\nabla\mathcal F_\eta(D_0)=\lambda D_0
}
```

for some Lagrange multiplier `lambda` enforcing the fixed quadratic norm.

Equivalently, the first variation vanishes for every tangent perturbation `X` satisfying

```math
\operatorname{tr}(D_0X)=0.
```

## Pre-validation restrictions

The following data are excluded from solving or selecting `eta`:

```text
CKM entries
CKM phase / Jarlskog target
fermion masses
PMNS data
PDG comparison values
A_seed alignment or Hessian target
retrospective coefficient tuning
```

`A_seed` is deliberately excluded from the selector equation so that any later relation between the independently frozen seed-incidence direction and the variational Hessian can serve as an external structural check rather than an input.

## Validation gates to run after this freeze

1. Determine whether a finite real `eta` exists.
2. Determine whether it is unique under the frozen projective normalization.
3. Verify constrained-stationarity residual.
4. Classify the constrained Hessian at `D0`.
5. Only after gates 1–4, compare Hessian eigendirections with independently frozen family directions such as `A_seed`.
6. Preserve PASS, FAIL, or saddle result without retuning `eta`.

## Evidential status

```text
status: FROZEN_PREVALIDATION
new continuous fitted parameter: NONE
eta: TO_BE_DERIVED_FROM_FROZEN_STATIONARITY_CONDITION
uses observed CKM: NO
uses observed masses: NO
uses A_seed in selector equation: NO
physical interpretation: NONE
```

Any modification of the selector condition requires a new version. This v0.1 freeze is append-only evidence.
