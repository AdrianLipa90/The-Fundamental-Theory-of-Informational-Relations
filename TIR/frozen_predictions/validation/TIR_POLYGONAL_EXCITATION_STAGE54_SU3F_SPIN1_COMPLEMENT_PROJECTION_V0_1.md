# TIR Polygonal Excitation — Stage 54 SU(3)_F Spin-1 Complement Projection v0.1

Status: `STAGE_54_FROZEN_SU3F_GENERATORS_HAVE_SPIN2_COMPLEMENT_PASS`

## Purpose

Stage 53 decomposed the family Lie algebra under the explicit compact spin-one `SU(2)` embedding of Stage 52 as

```math
\mathfrak{su}(3)_F\cong\mathbf 3\oplus\mathbf 5.
```

Stage 54 projects the already-frozen Stage 42 generators onto this decomposition and tests whether the polygonal/character construction genuinely accesses the five-dimensional complement.

No CKM entries, masses, or fitted coefficients are used.

## Frozen family generators

Stage 42 uses

```math
D=\operatorname{diag}\left(-\frac13,0,\frac1{\sqrt5}\right),
```

and

```math
C=F_3DF_3^\dagger,
```

with traceless Hermitian parts

```math
D_0=D-\frac{\operatorname{tr}D}{3}I,
\qquad
C_0=C-\frac{\operatorname{tr}C}{3}I.
```

Stage 52 fixes the explicit spin-one Hermitian generators `J_x,J_y,J_z` in the same three-component matrix carrier.

Use the Hilbert--Schmidt inner product

```math
\langle A,B\rangle=\operatorname{Tr}(A^\dagger B).
```

Since

```math
\operatorname{Tr}(J_aJ_b)=2\delta_{ab},
```

the projection onto the spin-one subalgebra is

```math
P_3(X)=\sum_{a=x,y,z}\frac{\operatorname{Tr}(J_aX)}{2}J_a,
```

and the complementary component is

```math
P_5(X)=X-P_3(X).
```

## Ordered polygonal axis D_0

The spin-one component of `D_0` lies along `J_z`. The five-dimensional component is exactly proportional to the quadrupole matrix

```math
Q_0=\operatorname{diag}(1,-2,1).
```

Explicitly,

```math
P_5(D_0)=
\frac{3\sqrt5-5}{90}
\operatorname{diag}(1,-2,1).
```

This is nonzero.

The Hilbert--Schmidt norm fractions are

```math
\boxed{
\frac{\|P_5(D_0)\|^2}{\|D_0\|^2}
=
\frac{143-63\sqrt5}{302}
\approx0.0070454219123,
}
```

and

```math
\frac{\|P_3(D_0)\|^2}{\|D_0\|^2}
\approx0.992954578088.
```

Thus the ordered polygonal axis is predominantly in the compact spin-one sector but already contains a strictly nonzero spin-two component.

## C3-character axis C_0

For the character-rotated axis,

```math
\boxed{
\frac{\|P_5(C_0)\|^2}{\|C_0\|^2}=\frac13,
}
```

and

```math
\boxed{
\frac{\|P_3(C_0)\|^2}{\|C_0\|^2}=\frac23.
}
```

The five-dimensional component is therefore substantial rather than perturbatively small.

In the Stage 52 spin-one weight basis it occupies the `m=+1 <-> m=-1` quadrupole channel, as expected for a spin-two component.

## Adjoint-Casimir verification

Define the embedded `SU(2)` adjoint Casimir acting on traceless Hermitian `3x3` matrices by

```math
\mathcal C_{\rm ad}(X)
=\sum_{a=x,y,z}[J_a,[J_a,X]].
```

Using a full Gell-Mann basis for the eight-dimensional Hermitian traceless matrix space gives eigenvalues

```text
2, 2, 2, 6, 6, 6, 6, 6.
```

These are exactly

```math
j(j+1)=2\quad(j=1)
```

with multiplicity three and

```math
j(j+1)=6\quad(j=2)
```

with multiplicity five.

Moreover,

```math
\mathcal C_{\rm ad}(P_3X)=2P_3X,
\qquad
\mathcal C_{\rm ad}(P_5X)=6P_5X
```

for both `X=D_0` and `X=C_0` to floating-point residual below `2e-16`.

## Result

The frozen Stage 42 generators do not remain inside the compact spin-one subgroup. They already contain directions in the five-dimensional complement required to generate the full family algebra:

```math
\boxed{
P_5(D_0)\neq0,
\qquad
P_5(C_0)\neq0.
}
```

This gives a precise representation-theoretic refinement of Stage 42:

```text
compact Sym^2 / spin-one sector -> 3-dimensional subalgebra
polygonal + C3-character axes   -> include spin-two complement
Lie closure                     -> full 3 + 5 = 8 dimensional su(3)_F
```

## Selection boundary

The Stage 52 compact embedding is an explicitly recorded mathematical embedding, while its dynamical selection from the split-real Collatz/Poincare representation remains open. Stage 54 therefore establishes the component structure relative to that fixed embedding; it does not yet derive a physical compactification mechanism.

No physical particle assignment is made to the five-dimensional complement.

## Reproducibility

`TIR/frozen_predictions/validation/scripts/su3f_spin1_complement_stage54_v01.py`

Receipt:

`TIR/frozen_predictions/validation/results/TIR_POLYGONAL_STAGE54_SU3F_SPIN1_COMPLEMENT_RECEIPT_V0_1.json`
