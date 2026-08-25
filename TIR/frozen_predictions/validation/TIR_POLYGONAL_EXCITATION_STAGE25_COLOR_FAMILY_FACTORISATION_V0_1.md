# TIR Polygonal Excitation — Stage 25 Color / Family Factorisation v0.1

Status: `STAGE_25_COLOR_FAMILY_FACTORISATION_PASS`

## Existing TIR color connection

TIR v3.9 provides the complex triplet / CP2 / SU(3)-candidate color carrier. Modules v4.0 and v4.1 equip that carrier with SU(3)-valued holonomic links `W_ij` and their local connection/curvature continuation.

## Family carrier from Stage 21

Stage 21 supplies the independent exceptional factor

```math
E_8\supset(E_6\times SU(3)_F)/Z_3
```

with the matter carrier `(16,3_F)`.

The Standard Model color factor is contained inside the E6 branch, while `SU(3)_F` is the external triplet factor. Therefore the two triplet actions occupy different tensor factors.

## Exact carrier factorisation

For the left quark doublet across all three family labels,

```math
V_Q=\mathbb C^3_C\otimes\mathbb C^2_L\otimes\mathbb C^3_F.
```

Hence

```math
\dim V_Q=3\cdot2\cdot3=18,
```

matching the Stage 21 multiplicity at `Y=+1/6`.

The remaining one-family Standard Model multiplicities tensor with the family triplet as

```text
Q      : 3_C x 2_L x 3_F = 18
u^c    : 3bar_C x 1   x 3_F = 9
d^c    : 3bar_C x 1   x 3_F = 9
L      : 1   x 2_L x 3_F = 6
e^c    : 1   x 1   x 3_F = 3
nu^c   : 1   x 1   x 3_F = 3
```

for a total of 48 states.

## Independent actions

A color holonomy acts as

```math
W_C\otimes I_2\otimes I_3,
\qquad W_C\in SU(3)_C,
```

while a family transformation acts as

```math
I_3\otimes I_2\otimes U_F,
\qquad U_F\in SU(3)_F.
```

Therefore

```math
\boxed{
[W_C\otimes I_2\otimes I_3,
 I_3\otimes I_2\otimes U_F]=0
}
```

identically for every `W_C` and `U_F`.

The computational audit uses exact integer 3-cycle representatives on both factors and obtains commutator residual zero on the 18-state quark-doublet carrier.

## Result

The color triplet used by the TIR `W_ij` holonomy and the Stage 21 threefold family carrier are two independent commuting SU(3) factors. This removes the label ambiguity between "three colors" and "three family copies" at representation level.

Gauge interpretation of the external family factor is tracked separately; the present gate establishes carrier factorisation and commutation.

## Reproducibility

`TIR/frozen_predictions/validation/scripts/color_family_factorisation_stage25_v01.py`
