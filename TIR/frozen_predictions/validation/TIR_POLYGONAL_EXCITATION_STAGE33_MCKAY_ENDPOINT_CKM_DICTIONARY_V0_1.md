# TIR Polygonal Excitation — Stage 33 McKay Endpoint CKM Dictionary v0.1

Status: `STAGE_33_ENDPOINT_RATIO_RECONSTRUCTION_PASS__FUNCTIONAL_SELECTION_RETROSPECTIVE`

## Frozen geometric input

Stages 10 and 14 establish the complete nondegenerate spherical equal-edge sequence

```math
N\in\{3,4,5\}
```

with the flat/degenerate threshold at `N=6`, and the McKay correspondence

```math
N=3\to\widetilde E_6,
\qquad
N=4\to\widetilde E_7,
\qquad
N=5\to\widetilde E_8.
```

The endpoint levels are therefore uniquely

```math
N_-=3,
\qquad
N_+=5.
```

The affine McKay graphs at those endpoints have respectively

```math
n_-=7,
\qquad
n_+=9
```

vertices/irreducible-representation labels. The defining SU(2) representation used by McKay has dimension

```math
s=2.
```

## Endpoint ratios

Define only from these frozen invariants

```math
a=\frac{s}{n_-}=\frac27,
\qquad
b=\frac{s}{n_+}=\frac29,
\qquad
c=\frac{s}{N_+}=\frac25.
```

These reproduce exactly the three rational ratios appearing in the archived TIR CKM candidate:

```math
\boxed{a=\frac{L_4}{L_3}},
```

```math
\boxed{b=\frac{L_4}{L_3+L_4}},
```

```math
\boxed{c=\frac{L_4}{L_5}}.
```

This is an independent ratio reconstruction: the McKay calculation does not use CKM data, particle masses, or the original Collatz/twin-prime derivation of `L3,L4,L5`.

## Existing CKM formulas in endpoint variables

The v7.9/r1 structural formulas become identically

```math
\lambda=b+a\kappa,
```

```math
|V_{cb}|=\frac{a^2}{s},
```

```math
|V_{ub}|=\frac{a^2b}{N_+}
=\frac{a^2bc}{s},
```

```math
J=\kappa^2c\left(1-\frac{c^2}{s}\right),
```

and the current direct phase candidate is

```math
\delta=\arccos c.
```

Every equality above is exact except for the transcendental evaluation of `kappa` and `arccos`.

## Uniqueness boundary

The selection of `(N_-,N_+)=(3,5)`, `(n_-,n_+)=(7,9)`, and `s=2` is fixed once the following rule is stated:

```text
use the lower and upper endpoints of the complete nondegenerate spherical polygonal/McKay ladder and the defining McKay SU(2) representation dimension.
```

No CKM observable enters that rule.

## Epistemic boundary

This stage reconstructs the rational ingredients of the already-known CKM functional form from the newly derived geometry. The functional form itself predates this reconstruction and was developed with CKM reference values already available, so its predictive status remains postdictive until a new independent observable is preregistered.

## Reproducibility

`TIR/frozen_predictions/validation/scripts/mckay_endpoint_ckm_dictionary_stage33_v01.py`
