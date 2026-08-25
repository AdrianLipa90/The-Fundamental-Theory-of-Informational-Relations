# TIR Polygonal Excitation — Stage 24 TIR Seed × Chirality / E8 Intertwiner v0.1

Status: `STAGE_24_SIX_STATE_LABEL_INTERTWINER_PASS`

## Ordered TIR seed basis

Stage 22 fixes the active ordered seed labels

```math
s_1=(3,5),\qquad s_2=(5,7),\qquad s_3=(11,13).
```

Define the cyclic label operator

```math
P_s|s_1\rangle=|s_2\rangle,
\quad
P_s|s_2\rangle=|s_3\rangle,
\quad
P_s|s_3\rangle=|s_1\rangle.
```

This operator acts on the ordered seed-label space. Dynamical Collatz transition status is tracked separately.

## Exceptional triplet basis

Use the Stage 20 ordered SU(3) triplet-label basis

```math
\{|t_1\rangle,|t_2\rangle,|t_3\rangle\}
```

with the same three-cycle matrix `P3`.

Define

```math
M_s|s_j\rangle=|t_j\rangle.
```

In the ordered bases `M_s=I3`, so

```math
M_sP_s=P_3M_s.
```

## Add the chirality / conjugation label

Stage 23 supplies

```math
FJ_\chi=C_EF,
```

with convention-fixed `F=I2`.

On the six-dimensional label space define

```math
G_{TIR}=P_s\otimes J_\chi,
```

and on the exceptional six-label sector define

```math
G_{E8}=P_3\otimes C_E.
```

The product map

```math
\mathcal T=M_s\otimes F
```

satisfies the exact intertwining identity

```math
\boxed{\mathcal T G_{TIR}=G_{E8}\mathcal T}.
```

## Exact finite closure

Both representations satisfy

```math
G^3=I_3\otimes X_2,
\qquad
G^6=I_6,
```

with no smaller positive identity power. Their characteristic polynomial is

```math
\boxed{\chi_G(\lambda)=\lambda^6-1}.
```

The orbit is

```text
(s1,N) -> (s2,S) -> (s3,N) -> (s1,S) -> (s2,N) -> (s3,S) -> (s1,N)
```

and maps one-to-one to the Stage 20 exceptional orbit.

## Result

The Stage 6 abstract `C3 x Z2` six-state label lift, the Stage 20 exceptional E8 six-label realization, and the present TIR ordered-seed × CP1-chirality label space are exactly equivalent as finite label representations.

The seed three-cycle used here is the canonical cyclic action on the ordered three-element basis. A dynamical derivation of that cycle from Collatz/Poincare seed evolution remains a separate validation gate.

## Reproducibility

`TIR/frozen_predictions/validation/scripts/tir_seed_chirality_e8_stage24_v01.py`
