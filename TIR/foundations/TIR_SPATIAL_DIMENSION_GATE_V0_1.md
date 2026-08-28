# TIR Spatial Dimension Gate v0.1

Status: `TIR_CONDITIONAL_SPATIAL_DIMENSION_GATE_CANDIDATE`

Scope: TIR-only analysis of how the spatial branch can select its continuum dimension from already admitted primitive quantum/geometric structure. This file separates exact implications from the still-open bridge that would turn them into an unconditional TIR derivation of spatial dimension.

## 1. Current inputs

The primitive TIR core already admits the two-state quantum carrier

\[
\mathcal H_2\cong\mathbb C^2
\]

and its projective pure-state geometry

\[
\boxed{\mathbb{CP}^1\cong S^2_{\rm Bloch}}.
\]

The spatial branch independently admits an isotropic efficiency selector A4 and a continuum target

\[
\mathfrak S_X=(\Sigma,h_{ij},D_i,{}^{(n)}R,dV_h).
\]

The open variable is the spatial dimension

\[
\boxed{n=\dim\Sigma}.
\]

## 2. Route A — boundary-dimension route

For an `n`-dimensional spatial ball,

\[
B^n\subset\mathbb R^n,
\]

its boundary is

\[
\boxed{\partial B^n\cong S^{n-1}}.
\]

Suppose TIR supplies an admitted topology-preserving identification

\[
\boxed{\Xi:S^2_{\rm Bloch}\longrightarrow \partial B^n}
\]

with `Xi` a homeomorphism onto the spatial isotropic boundary selected by A4.

Topological dimension is invariant under homeomorphism. Therefore

\[
2=n-1,
\]

hence

\[
\boxed{n=3}.
\]

### Conditional theorem A

If the primitive projective state sphere `S2_Bloch` is identified homeomorphically with the boundary of the spatial isotropic enclosure `S^(n-1)_space`, then the spatial bulk dimension is uniquely

\[
\boxed{3}.
\]

The dimension arithmetic is exact. The research gate is the construction of `Xi` from admitted TIR relations.

## 3. Route B — projective symmetry route

The orientation-preserving projective symmetry of the two-state pure-state sphere is

\[
\boxed{\mathrm{PSU}(2)\cong SO(3)}.
\]

Suppose the primitive spatial isotropy at a continuum point `x in Sigma` is supplied by this same admitted symmetry through the defining faithful real representation

\[
\rho_x:SO(3)\longrightarrow GL(T_x\Sigma)
\]

with `rho_x` equivalent to the standard vector representation of `SO(3)`.

That representation acts on

\[
\boxed{\mathbb R^3}.
\]

Hence

\[
\boxed{\dim T_x\Sigma=3},
\]

and therefore, for a connected smooth spatial carrier of constant local dimension,

\[
\boxed{\dim\Sigma=3}.
\]

### Conditional theorem B

If the projective `PSU(2) ~= SO(3)` symmetry of the primitive two-state carrier is promoted to the defining tangent-space isotropy of the spatial continuum, then the spatial dimension is three.

Again the representation-theoretic implication is exact; the open TIR gate is the promotion map from projective-state symmetry to spatial tangent isotropy.

## 4. Convergence of the two routes

The two routes use different preserved structures:

```text
ROUTE A: topology
S2_Bloch --Xi(homeomorphism)--> S^(n-1)_space
                              -> n=3

ROUTE B: symmetry representation
PSU(2) ~= SO(3) --rho_x(defining real rep)--> T_x Sigma
                                            -> dim=3
```

If both bridge maps are derived independently, they converge on the same spatial dimension:

\[
\boxed{n=3}.
\]

That convergence would be stronger than selecting `n=3` by declaration.

## 5. A8 / Banach--Tarski lower-bound crosscheck

A separate downstream crosscheck is available through the paradox branch. Banach--Tarski-type paradoxical decompositions rely on non-amenable rotational group structure available in Euclidean dimensions at least three.

If A8 is strengthened at a later gate to require a geometric paradoxical-decomposition stabilizer in the spatial branch, that requirement supplies only the lower bound

\[
\boxed{n\ge3}.
\]

It does not by itself select `n=3`. It can therefore serve as an independent consistency check after a dimension selector is admitted.

## 6. Local dimension must also be measurable from relations

A selected dimension must agree with the relational metric layer. For a finite Euclidean-embeddable metric sample with squared-distance matrix `Delta`, define the centered Gram matrix

\[
\boxed{B=-\frac12 J\Delta J},
\qquad
J=I-\frac1m\mathbf 1\mathbf 1^T.
\]

When `B` is positive semidefinite, the minimum Euclidean embedding dimension is

\[
\boxed{\operatorname{rank}(B)}.
\]

This gives an A5-compatible operational audit:

\[
\text{relational distances}\longrightarrow\text{Gram rank}\longrightarrow\text{local geometric dimension}.
\]

Thus a future `n=3` derivation must be reflected by rank-three generic local metric data in the continuum limit.

## 7. Dimension-selection firewall

The current status is intentionally split:

```text
EXACT:
  dim(S2_Bloch) = 2
  boundary(B^n) = S^(n-1)
  S2_Bloch ~= boundary(B^n)  => n=3
  PSU(2) ~= SO(3)
  defining real representation of SO(3) has dimension 3

OPEN TIR BRIDGES:
  Xi    : S2_Bloch -> spatial isotropic boundary
  rho_x : projective symmetry -> spatial tangent isotropy
```

Therefore the present file registers exact conditional 3D routes while keeping unconditional spatial dimension selection as an open derivation gate.

## 8. Typed dependency graph

```text
POINT
 -> FIRST DISTINCTION
 -> TWO POLES
 -> C^2
 -> CP1 ~= S2_BLOCH
      |\
      | +--> TOPOLOGICAL BRIDGE Xi --> S^(n-1)_SPACE --> n=3
      |
      `----> PSU2 ~= SO3 --> TANGENT ISOTROPY rho_x --> dim(T_x Sigma)=3

RELATIONAL METRIC
 -> DISTANCE MATRIX
 -> CENTERED GRAM MATRIX
 -> LOCAL RANK AUDIT
```

## 9. Next TIR gate

The next primitive spatial question is now sharply defined:

\[
\boxed{\text{Can }\Xi\text{ or }\rho_x\text{ be derived from the existing TIR relation/symmetry structure?}}
\]

A successful derivation of either bridge selects `n=3` conditionally on the stated standard mathematical identifications. Deriving both gives an independent topology-plus-symmetry convergence test.