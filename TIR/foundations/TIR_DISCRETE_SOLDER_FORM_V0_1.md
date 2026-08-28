# TIR Discrete Relational Solder Form v0.1

Status: `TIR_DISCRETE_SOLDER_CONSTRUCTION_CANDIDATE`

Scope: TIR-only construction of the missing bridge between internal three-dimensional relation generators and displacement between relational loci. The construction is discrete first. Its continuum limit is the candidate origin of the spatial coframe/solder form.

## 1. Relational edge as geometric displacement

Let the pre-continuum TIR spatial carrier be a connected oriented graph

\[
G=(V,E).
\]

For every oriented edge

\[
e=(x\to y)
\]

assign a traceless Hermitian displacement generator

\[
\boxed{
\mathcal E_{xy}
=E^a_{xy}\sigma_a
\in\operatorname{Herm}_0(2).
}
\]

Its TIR spatial length is defined by the generator metric

\[
\boxed{
\ell_{xy}^2
:=\frac12\operatorname{Tr}(\mathcal E_{xy}^2)
=\delta_{ab}E^a_{xy}E^b_{xy}.
}
\]

Thus edge length and internal generator displacement are one typed object rather than separately introduced quantities.

## 2. Local frame covariance

At a vertex `x`, a local binary quantum frame may change by

\[
U_x\in SU(2).
\]

The edge generator transforms by conjugation,

\[
\boxed{
\mathcal E_{xy}
\mapsto
U_x\mathcal E_{xy}U_x^\dagger.
}
\]

Because the Hilbert--Schmidt metric is invariant under conjugation,

\[
\ell_{xy}^2
\mapsto
\ell_{xy}^2.
\]

Therefore the scalar distance is frame-independent while the directional components rotate by the associated `SO(3)` adjoint action.

This is the exact discrete analogue of a coframe carrying an internal orthonormal index.

## 3. Parallel transport between vertices

Let

\[
U_{xy}\in SU(2)
\]

be the relational frame transporter from `x` to `y`.

An internal generator `A_y` at `y` is compared in the frame at `x` by

\[
\boxed{
A_y^{(x)}
=U_{xy}A_yU_{xy}^\dagger.
}
\]

For the reversed edge, consistency is represented by

\[
\boxed{
U_{yx}=U_{xy}^{-1}
}
\]

and the reversed displacement satisfies

\[
\boxed{
\mathcal E_{yx}
=-U_{yx}\mathcal E_{xy}U_{yx}^\dagger.
}
\]

This is the discrete oriented-displacement rule.

## 4. Discrete torsion / closure defect

Consider an oriented triangle

\[
x\to y\to z\to x.
\]

Bring each edge displacement into the frame at `x` and define the closure defect

\[
\boxed{
\mathcal T_{xyz}
:=
\mathcal E_{xy}
+U_{xy}\mathcal E_{yz}U_{xy}^\dagger
+U_{xz}\mathcal E_{zx}U_{xz}^\dagger.
}
\]

The discrete torsion-free closure condition is

\[
\boxed{\mathcal T_{xyz}=0}.
\]

With trivial transport in a flat patch this reduces to ordinary vector closure

\[
\mathbf E_{xy}+\mathbf E_{yz}+\mathbf E_{zx}=0.
\]

This supplies a pre-continuum form of Cartan's first structural equation.

## 5. Discrete curvature from holonomy

For the same loop define the `SU(2)` holonomy

\[
\boxed{
\mathcal H_{xyz}
:=U_{xy}U_{yz}U_{zx}.
}
\]

Flat frame transport around that loop satisfies

\[
\boxed{\mathcal H_{xyz}=I}.
\]

A nontrivial loop holonomy records curvature of the relational frame connection.

For a refining family of loops with oriented area bivector `Sigma^{ij}`, the continuum target relation is

\[
\mathcal H_\gamma
=I+\mathcal F_{ij}\Sigma^{ij}+O(|\Sigma|^{3/2}),
\]

where `F` is the `su(2)` curvature two-form.

## 6. Continuum solder limit

Suppose a sequence of relational graphs admits a smooth continuum limit with local coordinates `x^i`. For a small edge displacement `Delta x^i`, require

\[
\boxed{
\mathcal E_{xy}
= e^a{}_i(x)\,\Delta x^i\,\sigma_a
+O(|\Delta x|^2).
}
\]

Then the coefficient fields define the coframe

\[
\boxed{
e^a=e^a{}_i\,dx^i.}
\]

The spatial metric follows directly:

\[
\boxed{
h_{ij}
=\delta_{ab}e^a{}_i e^b{}_j.}
\]

Thus the solder form is the continuum limit of relational edge-generator displacements.

## 7. Rank and dimension

At a local vertex, collect outgoing displacement coefficient vectors

\[
\mathbf E_{xy}\in\mathbb R^3.
\]

Their span rank satisfies

\[
\operatorname{rank}\{\mathbf E_{xy}\}\le3
\]

because every edge generator lies in `Herm_0(2)`.

A nondegenerate spatial patch requires three linearly independent local displacement generators:

\[
\boxed{
\operatorname{rank}\{\mathbf E_{xy}\}=3.
}
\]

Under the spatial promotion gate this gives a full-rank coframe and a positive-definite local metric.

This links the earlier Gram-rank dimension audit directly to the generator algebra.

## 8. Cartan continuum target

Under the continuum limit, the discrete closure and holonomy objects target

\[
\boxed{
T^a
=de^a+\omega^a{}_b\wedge e^b
}
\]

and

\[
\boxed{
\Omega^a{}_b
=d\omega^a{}_b
+\omega^a{}_c\wedge\omega^c{}_b.
}
\]

The torsion-free spatial closure gate is

\[
T^a=0,
\]

and curvature is encoded by

\[
\Omega^a{}_b
=\frac12 R^a{}_{bcd}e^c\wedge e^d.
\]

Therefore the primitive TIR chain can now be written

\[
\boxed{
\text{RELATIONAL EDGE}
\to
\mathcal E_{xy}\in\operatorname{Herm}_0(2)
\to
\ell_{xy}
\to
\text{DISCRETE COFRAME}
\to
(e^a,\omega)
\to
(h,D,R).
}
\]

## 9. What is exact and what remains open

Exact at the discrete algebraic level:

```text
edge generator in Herm_0(2)
Hilbert-Schmidt edge norm
SU(2) frame covariance
SO(3) rotation of directional components
oriented reverse-edge rule
loop closure defect definition
loop holonomy definition
rank <= 3 of local generator displacements
```

Open continuum gates:

```text
existence of a refining relational graph family
regularity of the continuum limit
full-rank local coframe almost everywhere
convergence of discrete transport to a smooth connection
selection/derivation of zero torsion
```

## 10. Next TIR gate

The next question is now measurable:

\[
\boxed{
\text{Which primitive relation law makes generic local edge-generator rank equal to 3 and stabilizes the torsion-free continuum limit?}
}
\]

That is the next spatial-geometric frontier before coupling the result to the Time scalar/tensor sector.
