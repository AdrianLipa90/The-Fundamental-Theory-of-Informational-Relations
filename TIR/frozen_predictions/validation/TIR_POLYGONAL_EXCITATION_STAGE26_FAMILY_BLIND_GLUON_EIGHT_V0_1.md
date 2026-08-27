# TIR Polygonal Excitation — Stage 26 Family-Blind Eight-Gluon Sector v0.1

Status: `STAGE_26_EIGHT_COLOR_GENERATORS_FAMILY_BLIND_PASS`

## Color algebra already present in TIR

TIR v3.9 validates the eight Gell-Mann directions on the complex color triplet. Modules v4.0/v4.1 use this `su(3)_C` algebra for the holonomic `W_ij` / local-connection gluon sector.

Stage 25 introduces an independent family factor `C^3_F`.

## Generator extension over three family labels

On

```math
V_C\otimes V_F=\mathbb C^3_C\otimes\mathbb C^3_F,
```

extend each color generator by

```math
\Lambda_a^{(C)}=\lambda_a\otimes I_{3,F},
\qquad a=1,\ldots,8.
```

The eight matrices remain linearly independent. Their Hilbert-Schmidt Gram matrix is

```math
\operatorname{Tr}\left[(\Lambda_a^{(C)})^\dagger\Lambda_b^{(C)}\right]
=3\operatorname{Tr}(\lambda_a\lambda_b)
=6\delta_{ab}.
```

Thus family multiplicity rescales the trace norm by three while preserving the color-algebra dimension exactly at eight.

## Family commutation

For every family transformation `U_F`,

```math
[\lambda_a\otimes I_3,\ I_3\otimes U_F]=0.
```

The computational audit uses the exact three-cycle representative for `U_F`; every commutator is exactly zero in the tensor-product construction.

## State-count consequence

The three family copies therefore share the same eight color-generator directions:

```text
color algebra dimension = 8
family carrier dimension = 3
color generators after family extension = 8
```

The gluon sector is family-blind at this representation layer, while quark matter carries the extra family multiplicity.

## Claim scope

This gate establishes generator counting and tensor-factor commutation. The external `SU(3)_F` gauge-status gate remains open; no extra family gauge bosons are introduced by the TIR color connection in this stage.

## Reproducibility

`TIR/frozen_predictions/validation/scripts/family_blind_gluon_stage26_v01.py`
