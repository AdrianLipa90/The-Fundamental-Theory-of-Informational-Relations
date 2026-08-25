# TIR Polygonal Excitation — Stage 37 Common Family-Axis No-Go v0.1

Status: `STAGE_37_COMMON_FAMILY_AXIS_NOGO_PASS`

## Scope

This is a pure mathematical gate. It determines whether non-trivial quark-family mixing can arise if both sector operators are constructed only from scalar functions of one common frozen family operator.

No observed CKM entries or particle masses are used.

## Common normal family operator

Let `K` be any normal operator on the ordered three-dimensional family space. Assume

```math
H_u=f(K),
\qquad
H_d=g(K),
```

for scalar spectral functions `f` and `g`.

Because both operators belong to the same commutative functional calculus of `K`,

```math
\boxed{
[H_u,H_d]=0.
}
```

Therefore they admit a common eigenbasis. Their relative diagonalizer is identity up to diagonal phases and permutations, and any Jarlskog-type invariant vanishes.

Thus

```math
\boxed{
J_F=0.
}
```

for any construction using only one common normal family axis.

## Frozen family-axis instances

The executable sanity check instantiates three already derived label systems from the polygonal/McKay chain:

```text
polygonal level:       (3,4,5)
affine ADE node count: (7,8,9)
local c_N coordinate:  (-1/3,0,1/sqrt(5))
```

Representative independent scalar functions of each diagonal operator give exact numerical commutators

```text
N axis:        0.0
ADE node axis: 0.0
c_N axis:      0.0
```

and the common-basis representative gives

```text
J_F = 0.0.
```

These numerical examples are consistency checks of the general algebraic theorem.

## Consequence for the family-mixing program

A non-trivial family transformation requires at least one additional operator that is not a scalar function of the same family axis.

The structural requirement is therefore

```math
\boxed{
[H_u,H_d]\neq0
}
```

with a second geometric, orientation, or holonomy structure that supplies the relative basis misalignment.

For CP violation, the relative structure must additionally contain a non-removable complex phase so that a rephasing-invariant plaquette phase and `J_F` can be non-zero.

## Relation to Stage 36

Stage 36 supplies an explicit mechanism example: the pre-existing v3.5 open-holonomy amplitudes and phase-displacement records create a complex matrix whose two Hermitian products do not commute and whose relative unitary has `J_F != 0`.

Stage 37 establishes why a single scalar `N=3,4,5` / `E6,E7,E8` family coordinate cannot replace that missing relative holonomy by itself.

## Reproducibility

Executable:

`TIR/frozen_predictions/validation/scripts/family_axis_commuting_nogo_stage37_v01.py`

Receipt:

`TIR/frozen_predictions/validation/results/TIR_POLYGONAL_STAGE37_FAMILY_AXIS_COMMUTING_NOGO_RECEIPT_V0_1.json`

## Next gate

Search the already frozen polygonal/McKay/CP1 structure for a second non-commuting operator fixed independently of CKM data. Candidate classes are restricted to operators already implied by the geometry: cyclic transport, spinorial/Berry holonomy, affine-McKay adjacency, or an orientation operator with a pre-existing provenance record. Any candidate must be frozen before quantitative comparison and must reproduce a non-zero rephasing-invariant phase without an observable-specific coefficient.
