# TIR Spatial Geometry Core v0.1

Status: `TIR_SPATIAL_GEOMETRY_CORE_CANDIDATE`

Scope: TIR-owned continuation of the primitive dependency bridge into spatial geometry. The temporal scalar/tensor sector remains a sibling crosslink owned by `Informational-Dynamics-of-Time`. The Standard Model branch remains a second downstream physical branch from the same primitive core.

## 1. Architectural role

The primitive TIR spine is

\[
0\prec P\prec \{N,S\}\prec \frac12\prec \ln2
\prec \mathbb C^2\prec \mathbb{CP}^1\cong S^2.
\]

TIR now takes ownership of the spatial-geometric continuation of this common core:

\[
\boxed{
\mathcal C_0
\prec
\mathcal G_X^{\rm TIR}
}
\]

where `C_0` denotes the admitted primitive informational/quantum/geometric core and `G_X^TIR` denotes the spatial geometry sector.

The Time programme receives the same primitive core through a sibling interface

\[
\boxed{
\mathcal C_0\prec \mathcal B_T
}
\]

and owns temporal scalar/tensor dynamics.

## 2. Geometry firewall: state sphere and spatial sphere

Two spherical structures occur in the programme and remain typed separately.

### 2.1 Quantum state sphere

For the two-state carrier,

\[
\mathbb{CP}^1\cong S^2_{\rm Bloch}.
\]

This is projective state-space geometry.

### 2.2 Spatial efficiency sphere

A4 selects a sphere under the declared three-dimensional isoperimetric functional

\[
A^3\ge 36\pi V^2,
\]

with equality for

\[
S^2_X=\partial B^3.
\]

This is spatial enclosure geometry.

The two objects are therefore stored as different typed nodes:

```text
S2_BLOCH   = projective quantum-state geometry
S2_SPACE   = boundary of an isotropic spatial enclosure
```

A future identification map

\[
\Xi:S^2_{\rm Bloch}\to S^2_X
\]

becomes an admitted bridge only after explicit construction and audit. Until that gate, the two sphere types remain separately typed by construction.

## 3. Primitive relational geometry

Let the admitted spatial relation carrier be a connected weighted graph

\[
G=(V,E,\ell),
\qquad
\ell:E\to\mathbb R_{>0}.
\]

Vertices are distinguishable relational loci and positive edge weights are primitive geometric relation measures.

For a path

\[
\gamma=(v_0,v_1,\ldots,v_k),
\]

define path length

\[
L(\gamma)=\sum_{r=0}^{k-1}\ell(v_r,v_{r+1}).
\]

The induced shortest-path distance is

\[
\boxed{
d_G(a,b)=\inf_{\gamma:a\to b} L(\gamma).
}
\]

For a connected undirected graph with strictly positive symmetric edge weights this is a metric:

\[
d_G(a,b)\ge0,
\]

\[
d_G(a,b)=0\iff a=b,
\]

\[
d_G(a,b)=d_G(b,a),
\]

\[
d_G(a,c)\le d_G(a,b)+d_G(b,c).
\]

This gives TIR a pre-continuum spatial metric layer directly from relations.

## 4. Symmetry acts as spatial isometry

Let `Aut(G,ell)` denote graph automorphisms preserving edge weights. For

\[
g\in\operatorname{Aut}(G,\ell),
\]

path lengths are preserved, hence

\[
\boxed{
d_G(ga,gb)=d_G(a,b).
}
\]

Thus A7 acts geometrically as an isometry principle once a relational metric is admitted.

The dependency is

\[
\boxed{
\text{relational distinction}
+\text{positive relation measure}
+\text{symmetry}
\rightarrow
\text{metric geometry + isometries}.
}
\]

## 5. Arithmetic measures the geometry

A5 acts on the spatial carrier through geometric invariants such as

\[
\text{path length},\quad
\text{degree},\quad
\text{intersection count},\quad
\text{winding},\quad
\text{covering degree},\quad
\text{curvature integrals}.
\]

The operational correspondence is

\[
\boxed{
\text{spatial relation}
\xrightarrow{\text{geometric invariant}}
\text{arithmetic value}.
}
\]

A6 then acts where complex phase closure is present and promotes discrete closure indices as the natural-number branch of the same geometric-arithmetic correspondence.

## 6. Continuum spatial carrier

The continuum target object of the TIR spatial branch is typed as

\[
\boxed{
\mathfrak S_X
=
(\Sigma,h_{ij},D_i,{}^{(3)}R^{i}{}_{jkl},dV_h).
}
\]

Here:

- `Sigma` is a spatial relational carrier;
- `h_ij` is a positive-definite spatial metric;
- `D_i` is its Levi-Civita connection;
- `3R^i_jkl` is the intrinsic spatial curvature tensor;
- `dV_h=sqrt(det h) d^n x` is the induced volume element.

For an admitted spatial dimension `n`,

\[
h_{ij}=h_{ji},
\qquad
v^i h_{ij}v^j>0
\quad(v\ne0),
\]

and

\[
D_k h_{ij}=0.
\]

The branch keeps dimension selection as its own explicit derivation gate. The `n=3` specialization is the interface used by the later ADM/spacetime closure.

## 7. Discrete-to-continuum bridge target

The geometric convergence problem is now explicit:

\[
\boxed{
(G,\ell,d_G)
\longrightarrow
(\Sigma,h_{ij},D_i,{}^{(n)}R)
}
\]

under a declared coarse-graining / continuum limit.

The objects to preserve across this bridge are:

```text
DISTINGUISHABILITY
CONNECTIVITY
POSITIVE DISTANCE
SYMMETRY / ISOMETRY
ARITHMETIC GEOMETRIC INVARIANTS
ORIENTATION / HOLONOMY WHEN PRESENT
```

This is the active TIR spatial derivation programme.

## 8. TIR spatial export packet

The future closure interface exports the admitted spatial structure:

```text
spatial_carrier      = Sigma
spatial_metric       = h_ij
spatial_connection   = D_i
spatial_curvature    = 3R^i_jkl
spatial_volume       = dV_h
spatial_symmetry     = Isom(Sigma,h)
geometry_owner       = TIR
```

These spatial objects are defined prior to temporal-rate normalization.

## 9. Crosslink ownership

The architecture becomes

```text
PRIMITIVE TIR CORE
      |
      +--> TIR SPATIAL GEOMETRY
      |
      +--> TIR STANDARD MODEL BRANCH
      |
      `--> INFORMATIONAL DYNAMICS OF TIME
             temporal scalar/tensor branch
```

The first major cross-repository closure is then

\[
\boxed{
\mathfrak S_X^{\rm TIR}
\otimes
\mathfrak T^{\rm IDT}
\longrightarrow
\mathfrak M_{X\!T}
}
\]

where `M_XT` is the later spacetime closure surface.

## 10. Claim classes

| Statement | TIR class |
|---|---|
| positive weighted connected undirected graph induces shortest-path metric | EXACT METRIC-GEOMETRIC |
| weight-preserving graph automorphism preserves shortest-path distance | EXACT |
| `CP1 ~= S2_Bloch` | STANDARD PROJECTIVE GEOMETRY |
| A4 isoperimetric sphere selection | STANDARD GEOMETRIC EXTREMAL INPUT + TIR SELECTION POSTULATE |
| `S2_Bloch` and `S2_space` are separately typed | EXACT ARCHITECTURAL FIREWALL |
| continuum spatial packet `(Sigma,h,D,3R,dV)` | TIR CONTINUUM GEOMETRY TARGET |
| spatial dimension selection | OPEN TIR DERIVATION GATE |
| spacetime closure with temporal scalar/tensor sector | DOWNSTREAM CROSS-BRANCH INTERFACE |
