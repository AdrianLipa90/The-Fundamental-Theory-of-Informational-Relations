# TIR Polygonal Excitation — Stage 18 Shared Z3 Seam v0.1

Status: `STAGE_18_SHARED_CENTER_QUOTIENT_PASS`

## Structural data

The relevant compact exceptional subgroup structures are

```math
E_7\supset (E_6\times U(1))/Z_3,
```

and

```math
E_8\supset (E_6\times SU(3))/Z_3.
```

The common E6 core and common Z3 quotient are retained across the N=4/E7 and N=5/E8 stages.

## Explicit U(1) -> SU(3) embedding

Define

```math
\iota(e^{i\theta})=
\operatorname{diag}(e^{i\theta},e^{i\theta},e^{-2i\theta}).
```

Its determinant is identically one, so its image lies in SU(3).

At the one-third turn

```math
\theta=\frac{2\pi}{3},
```

all three diagonal entries coincide:

```math
\iota(e^{2\pi i/3})=\omega I_3,
\qquad
\omega=e^{2\pi i/3},
\qquad
\omega^3=1.
```

Thus the Z3 element in the U(1) stage maps directly onto the center Z3 of SU(3).

## CP2 projective check

For a nonzero vector z in C^3 define the projective rank-one representative

```math
P(z)=\frac{zz^\dagger}{z^\dagger z}.
```

For the center action,

```math
P(\omega z)=P(z).
```

The audit evaluates this numerically on a generic complex vector and obtains a machine-scale residual.

Therefore the center quotient carried by the E8 SU(3) factor is compatible with the projectivization already used by the TIR `C^3 -> CP2` triplet carrier.

## N=4 -> N=5 algebraic transition

The tested group-level inclusion is

```math
(E_6\times U(1))/Z_3
\hookrightarrow
(E_6\times SU(3))/Z_3,
```

with the displayed U(1) embedding preserving the same order-three central seam.

This gives a parameter-free algebraic relation between the N=4/E7 and N=5/E8 branches while preserving the E6 core.

## Reproducibility

`TIR/frozen_predictions/validation/scripts/e7_e8_z3_seam_stage18_v01.py`

Expected verdict: `PASS`.
