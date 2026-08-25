# TIR Polygonal Excitation — Stage 58 Icosahedral Quadrupole SU(3) Generation v0.1

Status: `STAGE_58_ICOSAHEDRAL_QUADRUPOLE_SU3_GENERATION_PASS`

## Purpose

Stage 57 establishes the representation identity

```math
\operatorname{End}_0(\mathbf 3_{A_5})=\mathbf 3\oplus\mathbf 5.
```

Stage 58 tests whether the actual `N=5` icosahedral geometry supplies an explicit spanning set for the five-dimensional symmetric-traceless factor and whether its commutators recover the three-dimensional rotational factor.

No CKM entries, masses, fitted coefficients, or amplitude kernels are used.

## Icosahedral axes

Let the 12 vertices of a regular icosahedron be represented by the standard coordinate set

```math
(0,\pm1,\pm\varphi),\qquad
(\pm1,\pm\varphi,0),\qquad
(\pm\varphi,0,\pm1),
```

where

```math
\varphi=\frac{1+\sqrt5}{2}.
```

Identifying antipodal vertices leaves six unoriented unit axes `u_a`, `a=1,...,6`.

For every axis define the traceless symmetric quadrupole

```math
Q_a=u_a u_a^T-\frac13 I_3.
```

Each `Q_a` belongs to

```math
\operatorname{Sym}^2_0(\mathbb R^3),
```

a real vector space of dimension five.

## Exact Gram structure

The six icosahedral axes obey

```math
(u_a\cdot u_b)^2=\frac15\qquad(a\ne b).
```

Therefore

```math
\operatorname{tr}(Q_a^2)=\frac23,
```

and, for `a != b`,

```math
\operatorname{tr}(Q_aQ_b)
=(u_a\cdot u_b)^2-\frac13
=-\frac{2}{15}.
```

Hence the quadrupole Gram matrix is

```math
G_Q=\frac45 I_6-\frac{2}{15}J_6.
```

Its spectrum is

```math
0\quad(\text{multiplicity }1),
\qquad
\frac45\quad(\text{multiplicity }5).
```

Thus

```math
\boxed{\operatorname{rank}\{Q_a\}=5.}
```

Moreover,

```math
\boxed{\sum_{a=1}^{6}Q_a=0.}
```

The six quadrupoles therefore form a centered regular 5-simplex inside the five-dimensional symmetric-traceless carrier.

## Commutator sector

For rank-one projectors,

```math
[Q_a,Q_b]
=(u_a\cdot u_b)
\left(u_a u_b^T-u_bu_a^T\right).
```

Every such commutator is real antisymmetric and therefore belongs to

```math
\mathfrak{so}(3).
```

The executable verifies that the set of all pairwise commutators has real span dimension

```math
\boxed{3}.
```

Hence the quadrupole geometry recovers the complete rotational factor.

## SU(3) closure

Every traceless skew-Hermitian `3x3` matrix can be written uniquely as

```math
X=A+iS,
```

with

```math
A\in\mathfrak{so}(3),
\qquad
S\in\operatorname{Sym}^2_0(\mathbb R^3).
```

Therefore, as real vector spaces,

```math
\mathfrak{su}(3)
=\mathfrak{so}(3)
\oplus
i\operatorname{Sym}^2_0(\mathbb R^3),
```

with dimensions `3 + 5 = 8`.

Because the six `Q_a` span the complete five-dimensional symmetric-traceless sector and their commutators span the complete three-dimensional antisymmetric sector,

```math
\boxed{
\operatorname{Lie}\langle iQ_1,\ldots,iQ_6\rangle
=\mathfrak{su}(3).
}
```

The executable independently obtains Lie-closure dimension `8`.

## Result

The `N=5` icosahedral geometry supplies an explicit finite generating set for the complete family Lie algebra carrier:

```math
\boxed{
\{\text{six icosahedral axes}\}
\longrightarrow
\{Q_a\}_{a=1}^{6}
\longrightarrow
\mathbf5
\stackrel{[\ ,\ ]}{\longrightarrow}
\mathbf3
\longrightarrow
\mathfrak{su}(3)_F.
}
```

This strengthens Stage 57 from a representation-character match to an explicit geometric spanning and Lie-generation result.

## Evidential status

```text
icosahedral axes: 6 antipodal pairs
quadrupole span dimension: 5
commutator span dimension: 3
Lie closure dimension: 8
CKM input: NONE
mass input: NONE
fitted coefficients: NONE
physical family dynamics selector: OPEN
```

## Reproducibility

Executable:

`TIR/frozen_predictions/validation/scripts/icosahedral_quadrupole_su3_stage58_v01.py`

Receipt:

`TIR/frozen_predictions/validation/results/TIR_POLYGONAL_STAGE58_ICOSAHEDRAL_QUADRUPOLE_SU3_RECEIPT_V0_1.json`
