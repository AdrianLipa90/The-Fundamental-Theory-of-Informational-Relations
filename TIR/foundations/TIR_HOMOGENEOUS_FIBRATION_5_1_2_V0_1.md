# TIR Homogeneous Fibration 5|1|2 v0.1

Status: `EXACT_NESTED_HOMOGENEOUS_FIBRATION / EXACT_7_EQUALS_5_PLUS_2_TANGENT_SPLIT / EXACT_SO2_ISOTROPY_ROLE / EXACT_LOCAL_CP1_GOLDEN_MEAN_FRACTAL / EXACT_TRIVIAL_AXIAL_ROTATION_STABILIZER / GLOBAL_FRACTAL_SUBBUNDLE_NOT_DERIVED / PHYSICAL_HORIZON_NOT_CLAIMED`

Scope: pure compact Lie-group, homogeneous-space, and symbolic/projective dynamics. The words `base`, `fiber`, `vertical`, `horizontal`, and `isotropy` are used in their mathematical bundle sense. No spacetime horizon, causal boundary, cosmological surface, or physical dimensional reduction is asserted.

## 1. Upstream exact basis

Use the already validated adapted Hermitian basis

```math
(E_1,E_2,E_3,E_4,E_5,E_6,E_7,E_8)
```

of `su(3)` with

```math
\mathfrak p=\operatorname{span}_{\mathbb R}\{E_1,\ldots,E_5\},
```

and the principal `so(3)` image

```math
\mathfrak k
=\operatorname{span}_{\mathbb R}\{E_6,E_7,E_8\}.
```

The principal generators satisfy

```math
[E_6,E_7]=iE_8,
\qquad
[E_6,E_8]=-iE_7,
\qquad
[E_7,E_8]=iE_6.
```

Select the axis stabilizer

```math
\mathfrak h=\mathbb R E_6\cong\mathfrak{so}(2)
```

and its orthogonal complement inside `k`,

```math
\mathfrak m=\operatorname{span}_{\mathbb R}\{E_7,E_8\}.
```

Therefore

```math
\boxed{
\mathfrak{su}(3)
=\mathfrak p\oplus\mathfrak h\oplus\mathfrak m
}
```

with dimensions

```math
\boxed{8=5+1+2.}
```

Under

```math
\langle A,B\rangle=\frac12\operatorname{Tr}(AB),
```

the three summands are mutually orthogonal.

## 2. Nested closed subgroups

At group level the principal spin-1 image is

```math
K\cong SO(3)\subset G=SU(3).
```

The selected axis has stabilizer

```math
H\cong SO(2)\subset K.
```

Thus

```math
\boxed{H\subset K\subset G.}
```

For any nested closed subgroups `H subset K subset G`, the canonical projection

```math
\pi:G/H\longrightarrow G/K,
\qquad
\pi(gH)=gK
```

is a homogeneous fiber bundle with fiber `K/H`.

Therefore here

```math
\boxed{
SO(3)/SO(2)
\hookrightarrow
SU(3)/SO(2)
\xrightarrow{\;\pi\;}
SU(3)/SO(3).
}
```

Using the standard identification

```math
SO(3)/SO(2)\cong S^2\cong\mathbb{CP}^1,
```

the fiber is exactly the previously identified two-real-dimensional `CP1` carrier.

## 3. Exact dimension bookkeeping

The homogeneous-space dimensions are

```math
\dim G/H=8-1=7,
```

```math
\dim G/K=8-3=5,
```

```math
\dim K/H=3-1=2.
```

Hence

```math
\boxed{7=5+2.}
```

This is the tangent-space dimension of the total homogeneous space. The original algebraic mnemonic

```text
12345 | 6 | 78
```

must therefore be typed carefully:

- `12345` = five-dimensional horizontal/base directions;
- `6` = one-dimensional isotropy/stabilizer algebra removed by the quotient `G/H`;
- `78` = two-dimensional vertical/fiber directions.

In particular,

```math
\boxed{E_6\notin T_{eH}(G/H).}
```

It is not a tangent sheet separating the five- and two-dimensional tangent sectors.

## 4. Tangent exact sequence and the 5+2 split

At the identity coset,

```math
T_{eH}(G/H)\cong\mathfrak g/\mathfrak h
\cong\mathfrak p\oplus\mathfrak m.
```

Likewise,

```math
T_{eK}(G/K)\cong\mathfrak g/\mathfrak k
\cong\mathfrak p,
```

and

```math
T_{eH}(K/H)\cong\mathfrak k/\mathfrak h
\cong\mathfrak m.
```

The differential of the bundle projection fits into the exact sequence

```math
0
\longrightarrow\mathfrak m
\longrightarrow\mathfrak p\oplus\mathfrak m
\xrightarrow{\;d\pi\;}
\mathfrak p
\longrightarrow0.
```

Thus

```math
\boxed{
\ker(d\pi)=\mathfrak m
=\operatorname{span}\{E_7,E_8\}
}
```

is the vertical fiber tangent, while

```math
\boxed{
\mathfrak p
=\operatorname{span}\{E_1,\ldots,E_5\}
}
```

is an orthogonal horizontal complement for the normal homogeneous metric induced by the invariant trace/Killing form.

This is the precise bundle-level form of the `5 | 1 | 2` organization.

## 5. The role of the `6` direction

The commutators

```math
[E_6,E_7]=iE_8,
\qquad
[E_6,E_8]=-iE_7
```

show that `E6` is the infinitesimal `SO(2)` isotropy generator rotating the transverse plane `m`.

Exponentiation gives the axis-rotation subgroup `H=SO(2)`. On the fiber

```math
K/H\cong S^2,
```

this is the standard rotation about the selected axis. Its generic orbit is a latitude circle; on the selected equatorial phase section it acts transitively as

```math
q\mapsto q+\alpha\pmod1.
```

Therefore the mathematically exact interpretation is

```math
\boxed{6=\text{isotropy / axial phase-rotation generator}.}
```

Calling it a physical `horizon` requires additional metric/causal physics and is not inferred here.

## 6. Placement of the Collatz-admissible fractal

The downstream CP1 theorem derives the exact compact set

```math
K_C
=\left\{
\sum_{k\ge0}\frac{b_k}{2^{k+1}}:
 b_kb_{k+1}=0
\right\}
\subset S^1\subset\mathbb{CP}^1
```

with self-similarity

```math
K_C=\frac12K_C
\cup
\left(\frac12+\frac14K_C\right)
```

and

```math
\boxed{
\dim_H K_C=\log_2\varphi
\approx0.6942419136.
}
```

Thus one selected `CP1` fiber carries the exact hierarchy

```math
\boxed{
K_C\subset S^1\subset\mathbb{CP}^1\cong SO(3)/SO(2).
}
```

The doubling map

```math
D(q)=2q\pmod1
```

preserves the golden-mean symbolic envelope:

```math
\boxed{D(K_C)=K_C.}
```

Indeed, `D` deletes the first binary symbol, so it preserves the forbidden-word condition `11`; surjectivity on `K_C` follows because prefixing any admissible itinerary by `0` gives an admissible preimage.

## 7. Exact symmetry firewall: `K_C` is not SO(2)-invariant

The continuous isotropy action on the equator is the full rotation action

```math
R_\alpha(q)=q+\alpha\pmod1.
```

A nonempty subset of the equator invariant under **all** such rotations must equal the full circle, because the `SO(2)` orbit of any equatorial point is all of `S^1`.

But

```math
\dim_H K_C=\log_2\varphi<1
```

while

```math
\dim_H S^1=1.
```

Therefore

```math
\boxed{K_C\text{ is not invariant under the full }SO(2)\text{ isotropy action}.}
```

An explicit witness is

```math
0\in K_C,
\qquad
R_{3/8}(0)=3/8=0.011_2\notin K_C,
```

because the binary word `11` occurs.

This distinguishes two symmetries:

```math
\boxed{
D(K_C)=K_C
\quad\text{but}\quad
SO(2)\cdot K_C\neq K_C.
}
```

The discrete Collatz/doubling dynamics preserves the fractal; the full continuous axial rotation symmetry does not.

### 7.1 Exact axial setwise stabilizer

The rotational symmetry can be sharpened completely. Since

```math
K_C\subset[0,2/3]
```

on the chosen circle coordinate, the complement contains the open arc

```math
G_\star=(2/3,1)
```

of length `1/3`.

Inside the convex hull `[0,2/3]`, the first self-similar gap is

```math
(1/3,1/2)
```

of length `1/6`. Every remaining internal gap is an image of this gap under a finite composition of the contractions `x/2` and `1/2+x/4`; hence every descendant gap has length at most `1/6`, and in fact strictly less after at least one contraction.

Therefore `G_*` is the **unique largest connected component** of `S1 \ K_C`.

Any rotation preserving `K_C` setwise also preserves its complement and therefore must map the unique largest gap `G_*` to itself. An orientation-preserving circle rotation that maps the proper arc `(2/3,1)` to itself must fix its endpoints, hence has rotation angle `0 mod 1`.

Thus

```math
\boxed{
\operatorname{Stab}_{SO(2)}(K_C)=\{e\}.
}
```

So within the axial rotation group there is no nontrivial residual continuous or finite rotational symmetry of the golden-mean set.

## 8. Consequence for a global fractal bundle

The homogeneous fibration itself is canonical:

```math
CP^1\hookrightarrow SU(3)/SO(2)\to SU(3)/SO(3).
```

However, the subset `K_C` is not invariant under the full fiber isotropy/phase-rotation action, and its setwise stabilizer inside that axial `SO(2)` is only the identity. Therefore the present data do **not** define a canonical phase-frame-independent global subbundle whose fiber is `K_C`.

In particular, any attempt to patch local `K_C` phase sets using transition functions valued only in the axial `SO(2)` can preserve `K_C` only when those transition functions are identity-valued on overlaps. Equivalently, nontrivial axial holonomy cannot preserve the exact golden-mean set.

To globalize the fractal one must additionally derive at least one of:

1. a distinguished phase trivialization/section compatible across the base;
2. a larger non-axial geometric symmetry whose action preserves the embedded `K_C`;
3. a connection whose holonomy lies in the actual setwise automorphism group of the embedded fractal;
4. an independent intertwiner binding the symbolic branch grammar to the geometric `E7,E8` carrier.

Until then,

```math
\boxed{
\text{local fiber fractal}=\text{EXACT},
\qquad
\text{canonical global fractal subbundle}=\text{OPEN}.
}
```

## 9. What survives from `12345 | 6 | 78`

The strongest exact statement is now

```math
\boxed{
\begin{array}{ccl}
12345 &:& T(SU(3)/SO(3))\ \text{horizontal/base sector},\\[2mm]
6 &:& \mathfrak{so}(2)\ \text{isotropy/axial generator},\\[2mm]
78 &:& T(SO(3)/SO(2))\cong T\mathbb{CP}^1\ \text{vertical/fiber sector}.
\end{array}
}
```

and on a selected phase equator in the `78` fiber,

```math
\boxed{
K_C\subset S^1\subset CP^1,
\qquad
\dim_HK_C=\log_2\varphi.
}
```

This is a bundle-theoretic and projective-dynamical theorem. No physical identification of `6` with a horizon or of the five-dimensional base with a spacetime interior is made.

## 10. Claim classes

| Statement | Status |
|---|---|
| `SO(2) subset SO(3) subset SU(3)` under the selected principal embedding | `EXACT_UPSTREAM` |
| homogeneous fibration `SO(3)/SO(2) -> SU(3)/SO(2) -> SU(3)/SO(3)` | `STANDARD_THEOREM_APPLIED_EXACTLY` |
| total/base/fiber dimensions `7=5+2` | `EXACT` |
| algebra bookkeeping `8=5+1+2` | `EXACT_UPSTREAM` |
| `E6` belongs to isotropy and is absent from `T(G/H)` | `EXACT` |
| horizontal tangent is `span(E1..E5)` | `EXACT` |
| vertical tangent is `span(E7,E8)` | `EXACT` |
| fiber is `S2 ~= CP1` | `STANDARD_GEOMETRIC_IDENTIFICATION` |
| `K_C subset S1 subset CP1` with `dim_H K_C=log_2(phi)` | `EXACT_DOWNSTREAM` |
| doubling map preserves `K_C` | `EXACT` |
| full `SO(2)` rotation action preserves `K_C` | `FAIL` |
| axial setwise stabilizer `Stab_SO2(K_C)` | `EXACT_TRIVIAL` |
| nontrivial axial holonomy preserves `K_C` | `FAIL` |
| canonical phase-independent global `K_C` subbundle | `OPEN` |
| `E7,E8` literally equal symbolic inverse-branch labels | `NOT_CLAIMED` |
| `E6` is a physical horizon | `NOT_CLAIMED` |

## 11. Validation requirements

A deterministic validator must:

1. reconstruct the adapted Gell-Mann basis and verify orthonormality;
2. verify `span(E6,E7,E8)` closes as the principal `so(3)`;
3. verify `E6` rotates `span(E7,E8)`;
4. verify the exact dimension identities `8=5+1+2` and `7=5+2`;
5. verify the quotient tangent classification `p + m` excludes `E6`;
6. verify the upstream golden-mean dimension receipt;
7. verify finite-word forward invariance of the no-`11` language under the binary shift;
8. include the exact counterexample `0 -> 3/8=0.011_2` against full `SO(2)` invariance;
9. verify the unique-largest-gap argument for the trivial axial setwise stabilizer;
10. re-run the parent `5|1|2` and CP1/golden-mean validators.
