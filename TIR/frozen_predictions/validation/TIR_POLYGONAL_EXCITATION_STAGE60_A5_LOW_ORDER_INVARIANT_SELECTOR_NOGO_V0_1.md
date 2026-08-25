# TIR Polygonal Excitation — Stage 60 A5 Low-Order Invariant Selector No-Go v0.1

Status: `STAGE_60_A5_LOW_ORDER_SELECTOR_NONUNIQUENESS_PASS`

## Purpose

Stages 58--59 identify the five-dimensional `A5` carrier explicitly as the reduced six-axis permutation representation and as the symmetric-traceless quadrupole space.

Stage 60 tests whether `A5` symmetry alone selects a unique low-order scalar functional on that five-dimensional carrier that could serve as a family-dynamics selector.

No CKM entries, masses, fitted coefficients, or amplitude kernels are used.

## Molien audit

For the five-dimensional irreducible representation of `A5`, use the rotation realization inherited from spin two.

The eigenvalue sets by element order are:

```text
identity:  (1,1,1,1,1)
order 2:   (1,1,1,-1,-1)
order 3:   (1,omega,omega,omega^2,omega^2)
order 5:   (1,zeta,zeta^2,zeta^3,zeta^4)
```

with class multiplicities

```text
1, 15, 20, 24.
```

The Molien series is therefore

```math
M(t)=\frac1{60}\left[
\frac1{(1-t)^5}
+\frac{15}{(1-t)^3(1+t)^2}
+\frac{20}{(1-t)(1+t+t^2)^2}
+\frac{24}{1-t^5}
\right].
```

Its low-degree expansion is

```math
M(t)=
1+t^2+2t^3+2t^4+4t^5+7t^6+7t^7+12t^8+\cdots.
```

Hence the invariant multiplicities are

```text
degree 0: 1
degree 1: 0
degree 2: 1
degree 3: 2
degree 4: 2
degree 5: 4
degree 6: 7
```

## Consequence at degrees one and two

There is no nonzero invariant vector in the irreducible five-dimensional carrier:

```math
\dim \operatorname{Inv}(\mathbf5)=0.
```

At quadratic order there is exactly one invariant, proportional to the norm

```math
I_2(S)=\operatorname{tr}(S^2).
```

A norm fixes a radius but does not select a direction in the five-dimensional carrier.

## Cubic sector

At degree three the invariant space already has dimension two.

Two explicit invariant cubic forms are:

```math
I_{3,\mathrm{iso}}(S)=\operatorname{tr}(S^3),
```

which is invariant under the full rotational subgroup, and

```math
I_{3,A_5}(S)
=\sum_{a=1}^{6}
\left[\operatorname{tr}(SQ_a)\right]^3,
```

where the `Q_a` are the six Stage 58 quadrupoles.

The second form is invariant because `A5` permutes the six quadrupoles.

The executable represents both cubic forms as symmetric rank-three tensors on an orthonormal basis of `Sym^2_0(R^3)` and obtains tensor-space rank

```math
\boxed{2}.
```

Therefore the two cubic invariants are linearly independent.

## No-go result

`A5` symmetry alone does not select a unique anisotropic cubic functional on the five-dimensional family complement.

Thus a unique family evolution cannot be promoted from the finite `A5` symmetry by choosing an arbitrary linear combination

```math
\alpha I_{3,\mathrm{iso}}+\beta I_{3,A_5}.
```

Any such coefficient pair requires an independent derivation or a previously frozen TIR invariant.

The retained result is

```math
\boxed{
A_5\text{ symmetry alone}
\;\not\Rightarrow\;
\text{unique low-order family selector}.
}
```

## Evidential status

```text
Molien invariant multiplicities: PASS
no invariant linear direction: PASS
unique quadratic norm: PASS
two-dimensional cubic invariant space: PASS
unique A5-only selector: NO-GO
CKM input: NONE
mass input: NONE
fitted coefficients: NONE
```

## Reproducibility

Executable:

`TIR/frozen_predictions/validation/scripts/a5_low_order_invariant_selector_stage60_v01.py`

Receipt:

`TIR/frozen_predictions/validation/results/TIR_POLYGONAL_STAGE60_A5_LOW_ORDER_INVARIANT_SELECTOR_RECEIPT_V0_1.json`
