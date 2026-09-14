# TIR Principal SU(2) 5|1|2 Decomposition v0.1

Status: `EXACT_PRINCIPAL_SU2_EMBEDDING / EXACT_5_1_2_AXIS_DECOMPOSITION / EXACT_CP1_TRANSVERSE_CARRIER / ABSOLUTE_BARRIER_HYPOTHESIS_FAIL / FRACTAL_DYNAMICS_OPEN`

Scope: pure Lie-algebra and homogeneous-space mathematics. This note does not identify any sector with a physical horizon, spacetime boundary, particle, biological identity, or fractal dynamics.

## 1. Normalized SU(3) basis

Let `lambda_a`, `a=1,...,8`, be the standard Hermitian Gell-Mann matrices with

```math
\frac12\operatorname{Tr}(\lambda_a\lambda_b)=\delta_{ab}.
```

Define the three Hermitian generators

```math
J_1=\frac{\lambda_1+\lambda_6}{\sqrt2},\qquad
J_2=\frac{\lambda_2+\lambda_7}{\sqrt2},\qquad
J_3=\frac{\lambda_3+\sqrt3\,\lambda_8}{2}.
```

Direct matrix multiplication gives

```math
[J_a,J_b]=i\varepsilon_{abc}J_c,
```

and

```math
J_1^2+J_2^2+J_3^2=2I_3.
```

Hence these matrices realize the spin-1 / principal Lie-algebra embedding

```math
\iota:\mathfrak{su}(2)\hookrightarrow\mathfrak{su}(3),
\qquad
\iota(\sigma_a/2)=J_a.
```

At group level the spin-1 representation has kernel `{+I,-I}`, so its image is isomorphic to `SO(3)`.

## 2. Orthogonal five-dimensional complement

Define

```math
Q_1=\frac{\lambda_1-\lambda_6}{\sqrt2},\qquad
Q_2=\frac{\lambda_2-\lambda_7}{\sqrt2},
```

```math
Q_3=\lambda_4,\qquad
Q_4=\lambda_5,\qquad
Q_5=\frac{\sqrt3\,\lambda_3-\lambda_8}{2}.
```

Under the inner product

```math
\langle A,B\rangle=\frac12\operatorname{Tr}(AB),
```

the ordered basis

```math
(Q_1,Q_2,Q_3,Q_4,Q_5,J_1,J_2,J_3)
```

is exactly orthonormal.

Let

```math
\mathfrak h=\operatorname{span}_{\mathbb R}\{J_1,J_2,J_3\},
\qquad
\mathfrak p=\operatorname{span}_{\mathbb R}\{Q_1,\ldots,Q_5\}.
```

The commutator supports satisfy

```math
[\mathfrak h,\mathfrak h]\subset\mathfrak h,
\qquad
[\mathfrak h,\mathfrak p]\subset\mathfrak p,
\qquad
[\mathfrak p,\mathfrak p]\subset\mathfrak h.
```

Therefore

```math
\boxed{\mathfrak{su}(3)=\mathfrak h\oplus\mathfrak p}
```

is the compact symmetric-pair decomposition associated with the principal `SO(3)` subgroup, with

```math
\dim\mathfrak p=5,
\qquad
\dim\mathfrak h=3.
```

Equivalently,

```math
\boxed{8=5+3}.
```

The corresponding homogeneous-space dimension is

```math
\boxed{\dim SU(3)/SO(3)=5}.
```

## 3. DII axis selection and the exact 5|1|2 split

The upstream Dynamic Identity Invariant uses Pauli-axis operators

```math
\Sigma_{\mathbf n}=\mathbf n\cdot\boldsymbol\sigma.
```

The principal embedding maps the Lie-algebra generator

```math
S_{\mathbf n}=\Sigma_{\mathbf n}/2
```

to

```math
\boxed{J_{\mathbf n}=n_1J_1+n_2J_2+n_3J_3}.
```

Because `iota` is a Lie-algebra homomorphism, conjugation/transport of the Pauli axis is carried to conjugation/transport of the spin-1 axis.

Choose coordinates so that the selected axis is `J_3`. Then

```math
\mathfrak h
=
\underbrace{\mathbb R J_3}_{1}
\oplus
\underbrace{\operatorname{span}_{\mathbb R}\{J_1,J_2\}}_{2}.
```

Thus

```math
\boxed{
\mathfrak{su}(3)
=
\underbrace{\mathfrak p}_{5}
\oplus
\underbrace{\mathbb RJ_3}_{1}
\oplus
\underbrace{\operatorname{span}\{J_1,J_2\}}_{2}
}
```

and therefore

```math
\boxed{8=5+1+2}.
```

This split is not the standard numerical ordering of the Gell-Mann matrices. It is a basis adapted to the principal `SU(2)` and to the selected DII axis.

## 4. Homogeneous-space interpretation

The three dimensions of the principal subgroup split under the stabilizer of the selected axis:

```math
SO(3)\supset SO(2).
```

Dimensionally,

```math
\boxed{
8
=
\dim SU(3)/SO(3)
+
\dim SO(2)
+
\dim SO(3)/SO(2)
=
5+1+2.
}
```

Moreover,

```math
SO(3)/SO(2)\cong S^2\cong \mathbb{CP}^1.
```

Hence the two-dimensional transverse sector is an exact real tangent carrier for the `CP1`/Bloch-sphere geometry already used elsewhere in TIR.

This statement does not by itself produce an iterative or fractal dynamics.

## 5. Explicit 1...8 adapted basis

For the mnemonic ordering `12345|6|78`, define

```math
E_1=Q_5,
\quad E_2=Q_1,
\quad E_3=Q_2,
\quad E_4=Q_3,
\quad E_5=Q_4,
```

```math
E_6=J_3,
\qquad E_7=J_1,
\qquad E_8=J_2.
```

Then `E_6,E_7,E_8` close exactly:

```math
[E_6,E_7]=iE_8,
\qquad
[E_6,E_8]=-iE_7,
\qquad
[E_7,E_8]=iE_6.
```

Two intra-sector area commutators of the five-dimensional block land on the distinguished axis:

```math
\boxed{[E_2,E_3]=iE_6},
```

```math
\boxed{[E_4,E_5]=2iE_6}.
```

Cross-couplings between those two internal planes instead generate the transverse pair:

```math
[E_2,E_4]=iE_8,
\qquad
[E_2,E_5]=-iE_7,
```

```math
[E_3,E_4]=iE_7,
\qquad
[E_3,E_5]=iE_8.
```

These identities are exact matrix statements.

## 6. Axis-weight decomposition

On the complexified adjoint space define the ordinary adjoint action

```math
\boxed{A_6=\operatorname{ad}_{E_6},\qquad A_6(X)=[E_6,X].}
```

Although `A_6` sends a Hermitian real basis element to an anti-Hermitian one, the complexified adjoint space is invariant and diagonalizes into the standard weight sectors. Its spectrum is

```math
\boxed{\operatorname{spec}(A_6)=\{-2,-1,-1,0,0,1,1,2\}}.
```

Equivalently,

```math
\boxed{\chi_{A_6}(x)=x^2(x^2-1)^2(x^2-4)}.
```

If instead one represents `-i ad(E_6)` on the real Hermitian basis, the corresponding real rotation blocks have complex eigenvalues `+-i` and `+-2i`; those are a differently typed representation of the same weight decomposition and are not to be confused with the weights above.

Under the selected `SO(2)` axis, the five-dimensional sector decomposes as

```math
\boxed{5=1+2+2},
```

with adjoint weights `0`, `+-1`, and `+-2`, while the principal three-dimensional sector decomposes as

```math
\boxed{3=1+2},
```

with weights `0`, `+-1`.

Thus the full adjoint has the nested form

```math
\boxed{8=(1+2+2)+(1+2)}.
```

This is a representation-theoretic recursion pattern; it is not, by itself, a proof of fractality.

## 7. Exact negative gate: the axis is not an absolute barrier

A literal barrier hypothesis would require the five-dimensional sector to couple to the transverse two-dimensional sector only through `E_6`.

That hypothesis is false. For example,

```math
[E_2,E_4]=iE_8,
\qquad
[E_2,E_5]=-iE_7.
```

Therefore the distinguished one-dimensional sector is not an algebraically impermeable membrane.

The mathematically justified description is narrower:

```math
\boxed{E_6\text{ is the selected }SO(2)\text{ stabilizer / axial generator}.}
```

Calling this a `horizon` is an interpretation and is not promoted to an exact physical claim here.

## 8. Claim classes

| Statement | Status |
|---|---|
| principal `su(2)` generators `J_a` satisfy the Lie algebra | `EXACT` |
| spin-1 Casimir `sum J_a^2 = 2I` | `EXACT` |
| orthonormal `5+3` basis | `EXACT` |
| symmetric-pair closure `h/h`, `h/p`, `p/p` | `EXACT` |
| DII-axis map `sigma_n/2 -> J_n` | `EXACT_LIE_ALGEBRA_INTERTWINER` |
| `8=5+1+2` after axis choice | `EXACT` |
| `SO(3)/SO(2) ~= S2 ~= CP1` transverse carrier | `STANDARD_GEOMETRIC_IDENTIFICATION` |
| complexified spectrum of `ad(E6)` | `EXACT` |
| `E6` as absolute barrier | `FAIL` |
| `E6` as axial stabilizer | `EXACT` |
| physical horizon identification | `NOT_CLAIMED` |
| fractal dynamics on the `78` carrier | `OPEN` |

## 9. Falsification / validation requirements

A deterministic validator must:

1. construct all eight Gell-Mann matrices;
2. verify the principal `su(2)` commutators and Casimir;
3. verify the full adapted-basis Gram matrix is `I8`;
4. verify the three symmetric-pair support rules;
5. verify the explicit `12345|6|78` commutators above;
6. verify the exact characteristic polynomial of complexified `ad(E6)`;
7. verify separately that the real-basis `-i ad(E6)` blocks have the corresponding `+-i` and `+-2i` spectrum;
8. include the direct `5 -> 78` commutators as a negative control against the absolute-barrier interpretation.
