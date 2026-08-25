# TIR Polygonal Excitation — Stage 53 Spin-1 Subgroup CP No-Go and 3+5 Decomposition v0.1

Status: `STAGE_53_SPIN1_CP_NOGO_AND_SU3_3PLUS5_DECOMPOSITION_PASS`

## Purpose

Stage 52 embeds the compact spin-one image `Sym^2(SU(2))` into the three-dimensional family-unitary carrier. Stage 53 tests whether that compact subgroup alone can support a nonzero three-family Jarlskog invariant.

## General spin-one matrix

In the standard weight basis `m=+1,0,-1`, a general spin-one rotation has Wigner form

```math
D^1(\alpha,\beta,\gamma)
=
P_L(\alpha)\,d^1(\beta)\,P_R(\gamma),
```

where

```math
P_L(\alpha)=\operatorname{diag}(e^{-i\alpha},1,e^{i\alpha}),
```

```math
P_R(\gamma)=\operatorname{diag}(e^{-i\gamma},1,e^{i\gamma}),
```

and the reduced Wigner matrix can be chosen entirely real:

```math
d^1(\beta)=
\begin{pmatrix}
(1+c)/2&-s/\sqrt2&(1-c)/2\\
s/\sqrt2&c&-s/\sqrt2\\
(1-c)/2&s/\sqrt2&(1+c)/2
\end{pmatrix},
```

with `c=cos(beta)` and `s=sin(beta)`.

Therefore every complex phase in a spin-one subgroup element is removable by independent row and column rephasings.

## Jarlskog consequence

For any rephasing-invariant quartet

```math
J_{ij;kl}=\operatorname{Im}(D_{ik}D_{jl}D_{il}^*D_{jk}^*),
```

the diagonal phase factors cancel, leaving the corresponding product of real entries of `d^1(beta)`.

Hence

```math
\boxed{J=0}
```

for every element of the compact spin-one `SU(2)` subgroup when used as a three-family mixing matrix.

Thus compactification of the Stage 50 polynomial carrier is sufficient for unitarity but insufficient for CP violation.

## Exact SU(3) decomposition under the spin-one subgroup

The family carrier is the spin-one representation `V_1` of dimension three. Its endomorphism space decomposes under `SU(2)` as

```math
V_1\otimes V_1^*
\cong
V_0\oplus V_1\oplus V_2,
```

with dimensions

```math
9=1+3+5.
```

Removing the scalar identity sector gives the traceless algebra

```math
\boxed{
\mathfrak{su}(3)
\cong
\mathbf 3\oplus\mathbf 5
}
```

as a real representation of the embedded spin-one `SU(2)`:

- the `3` is the compact `su(2)` subalgebra generated in Stage 52;
- the remaining `5` is the complementary spin-two sector required to reach the full eight-dimensional family algebra.

## Relation to earlier gates

Stage 42 already established that the frozen polygonal/character operators generate the full eight-dimensional `su(3)_F` algebra. Stage 53 now identifies a precise representation-theoretic boundary inside that algebra:

```text
compactified Collatz Sym^2 carrier -> 3 generators
full family su(3)                  -> 3 + 5 generators
```

Any family CP mechanism that is absent in the spin-one subgroup must therefore involve directions outside the compact `su(2)` subalgebra, i.e. the five-dimensional complement.

This is consistent with Stage 36, where non-removable complex holonomy was required for `J != 0`.

## Boundary

Stage 53 does not assign the five-dimensional complement to a particle multiplet or to polygon level `N=5`. It records only the exact representation decomposition and the CP no-go of the spin-one subgroup.

No CKM or mass input is used.

## Reproducibility

`TIR/frozen_predictions/validation/scripts/spin1_cp_nogo_stage53_v01.py`

Receipt:

`TIR/frozen_predictions/validation/results/TIR_POLYGONAL_STAGE53_SPIN1_CP_NOGO_3PLUS5_RECEIPT_V0_1.json`
