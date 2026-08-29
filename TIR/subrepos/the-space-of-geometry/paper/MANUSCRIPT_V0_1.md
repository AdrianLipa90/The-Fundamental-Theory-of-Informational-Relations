# The Space of Geometry: From First Distinction to Pythagoras

Manuscript draft v0.1

## Abstract

We construct a local Euclidean relation geometry from the binary quantum-point carrier of the Theory of Informational Relations (TIR). A normalized two-level quantum state belongs to the affine space

\[
\mathcal A_2=\frac12I+\operatorname{Herm}_0(2),
\]

whose translation space has real dimension three. Every ordered pair of states therefore determines a unique endpoint-carrying affine displacement

\[
\delta(\rho_x,\rho_y)=\rho_y-\rho_x.
\]

With the Pauli normalization, the relation generator is

\[
\mathcal E_{xy}=2(\rho_y-\rho_x)
\in\operatorname{Herm}_0(2)\cong\mathbb R^3.
\]

The `SU(2)` conjugation action induces the standard `SO(3)` action and preserves the positive quadratic form `Tr(AB)/2`. Minimal full-dimensional affine support in three real dimensions requires four vertices and therefore a 3-simplex. The unlabeled simplex has automorphism group `S_4`, acting transitively on its six edges. Applying the TIR arithmetic-geometric measure axiom (A5) and universal symmetry axiom (A7) to the edge-measure law makes all six edge lengths equal, selecting the regular tetrahedron. Its centered unit directions satisfy

\[
n_a\cdot n_b=-\frac13\qquad(a\ne b).
\]

The same Gram geometry appears independently in the tetrahedral qubit SIC frame. Finally, affine endpoint composition and the invariant inner product give distance, angle and orthogonality; for orthogonal relation vectors the norm identity reduces to

\[
a^2+b^2=c^2.
\]

The construction terminates at local Pythagorean closure. Global triangulation, curvature, holonomy and the TIR–Time spacetime join are downstream developments.

## 1. Introduction

The purpose of this paper is deliberately narrow. We ask:

\[
\boxed{
\text{How little primitive relational structure is required for local Euclidean geometry to appear?}
}
\]

The target is equally narrow. We stop when the derived local relation geometry supports the Pythagorean identity

\[
\boxed{a^2+b^2=c^2.}
\]

The parent TIR programme supplies the primitive point, first distinction, binary balance and binary quantum carrier. The present work begins its new derivation at the normalized two-state quantum point and follows the shortest dependency chain to a three-dimensional affine relation carrier, a minimal regular tetrahedral frame, and Euclidean inner-product closure.

The resulting route is

\[
\boxed{
\mathbb C^2
\to
\rho_x
\to
\mathcal A_2
\to
\delta(\rho_x,\rho_y)
\to
\operatorname{Herm}_0(2)\cong\mathbb R^3
\to
\Delta^3
\xrightarrow{A5+A7}
\text{regular tetrahedron}
\to
\text{Pythagoras}.
}
\]

Two independent checks accompany the main route. First, the minimal faithful real orthogonal representation of `SO(3)` is three-dimensional, agreeing with the affine carrier dimension. Second, minimal symmetric informational completeness for a qubit produces the same regular tetrahedral Gram frame.

## 2. Imported primitive TIR input

We import the TIR primitive chain

\[
0
\to P
\to \text{FIRST DISTINCTION}
\to \{N,S\}
\to \frac12
\to \ln2
\to \mathbb C^2.
\]

Only the binary quantum carrier is required as the direct mathematical parent of the new geometry construction.

Let the normalized point state be represented by a density operator

\[
\rho_x=\rho_x^\dagger,
\qquad
\operatorname{Tr}\rho_x=1.
\]

For a two-state carrier every normalized state has Bloch form

\[
\boxed{
\rho_x
=\frac12\left(I+\mathbf r_x\cdot\boldsymbol\sigma\right),
\qquad
|\mathbf r_x|\le1.
}
\]

Here

\[
\boldsymbol\sigma=(\sigma_x,\sigma_y,\sigma_z)
\]

is the Pauli basis.

## 3. The affine state hull is three-real-dimensional

The real vector space of Hermitian `2 x 2` matrices is

\[
\operatorname{Herm}(2)
=\{a_0I+a_i\sigma_i:a_\mu\in\mathbb R\}
\]

and has real dimension four.

Trace normalization imposes one real affine constraint. Therefore the trace-one affine hull is

\[
\boxed{
\mathcal A_2
=\left\{\rho=\rho^\dagger:\operatorname{Tr}\rho=1\right\}
=\frac12I+\operatorname{Herm}_0(2),
}
\]

where

\[
\operatorname{Herm}_0(2)
=\operatorname{span}_{\mathbb R}\{\sigma_x,\sigma_y,\sigma_z\}.
\]

Hence

\[
\boxed{
\dim_{\mathbb R}\mathcal A_2=3,
\qquad
T\mathcal A_2\cong\operatorname{Herm}_0(2)\cong\mathbb R^3.
}
\]

The notation `T A_2` here denotes the translation space of the affine carrier.

## 4. Canonical endpoint-carrying relation

An affine space is a torsor for its translation space. Consequently, for every ordered pair

\[
\rho_x,\rho_y\in\mathcal A_2
\]

there exists a unique vector

\[
\delta_{xy}\in\operatorname{Herm}_0(2)
\]

such that

\[
\rho_x+\delta_{xy}=\rho_y.
\]

Therefore

\[
\boxed{
\delta_{xy}=\rho_y-\rho_x.
}
\]

We take this canonical endpoint-carrying torsor displacement as the primitive vector relation exported by the spatial branch.

Using the standard Bloch/Pauli normalization, define

\[
\boxed{
\mathcal E_{xy}:=2(\rho_y-\rho_x).
}
\]

Then

\[
\boxed{
\mathcal E_{xy}
=(\mathbf r_y-\mathbf r_x)\cdot\boldsymbol\sigma
\in\operatorname{Herm}_0(2).
}
\]

The affine definition immediately gives

\[
\boxed{\mathcal E_{yx}=-\mathcal E_{xy}}
\]

and

\[
\boxed{
\mathcal E_{xz}
=\mathcal E_{xy}+\mathcal E_{yz}.
}
\]

Equivalently,

\[
\boxed{
\mathcal E_{xy}+\mathcal E_{yz}+\mathcal E_{zx}=0.
}
\]

Thus local endpoint composition is already encoded in the torsor structure.

## 5. Rotational symmetry and the invariant metric

For

\[
U\in SU(2),
\]

a common quantum frame transformation acts as

\[
\rho\mapsto U\rho U^\dagger.
\]

Therefore

\[
\boxed{
\mathcal E_{xy}
\mapsto
U\mathcal E_{xy}U^\dagger.
}
\]

The effective action on the three real Pauli coefficients factors through

\[
\boxed{
SU(2)/\{\pm I\}
\cong
SO(3).
}
\]

The defining real representation of `SO(3)` is irreducible, so its positive invariant quadratic form is unique up to global scale. In the canonical Pauli normalization we use

\[
\boxed{
\langle A,B\rangle
=\frac12\operatorname{Tr}(AB).
}
\]

Since

\[
\frac12\operatorname{Tr}(\sigma_i\sigma_j)=\delta_{ij},
\]

we obtain

\[
\boxed{
\|\mathcal E_{xy}\|^2
=\frac12\operatorname{Tr}(\mathcal E_{xy}^2)
=|\mathbf r_y-\mathbf r_x|^2.
}
\]

This quantity is the local squared relation length. A5 supplies its arithmetic-geometric typing.

## 6. Minimal full-dimensional support is tetrahedral

Let

\[
x_1,\ldots,x_m
\]

be points of a real affine space. Their affine span satisfies

\[
\dim\operatorname{Aff}\{x_1,\ldots,x_m\}
\le m-1.
\]

For full support of a three-dimensional affine carrier,

\[
3\le m-1.
\]

Hence

\[
\boxed{m\ge4.}
\]

At the minimum `m=4`, affine independence gives exactly the 3-simplex

\[
\boxed{
\Delta^3
=\operatorname{conv}\{x_1,x_2,x_3,x_4\}.
}
\]

The tetrahedron is therefore the minimal full-dimensional affine cell of the derived local relation carrier.

## 7. Regularity from intrinsic edge-orbit symmetry

The abstract unlabeled 3-simplex has automorphism group

\[
\boxed{
\operatorname{Aut}(\Delta^3)\cong S_4.
}
\]

Its six edges are the unordered vertex pairs

\[
\{i,j\},\qquad1\le i<j\le4.
\]

The natural `S_4` action on this edge set is transitive. Therefore all six primitive edges belong to one intrinsic combinatorial symmetry orbit.

For every realized edge define the arithmetic geometric measure

\[
\boxed{
q_{ij}
:=\frac12\operatorname{Tr}(\mathcal E_{ij}^2)
}
\]

and

\[
\ell_{ij}=\sqrt{q_{ij}}.
\]

A5 identifies the arithmetic invariant with geometric measure. A7 requires the primitive law to be invariant under the intrinsic symmetry action, so

\[
\boxed{
q_{\pi(i)\pi(j)}=q_{ij}
\qquad
\forall\pi\in S_4.
}
\]

Since the six edges form one orbit,

\[
\boxed{q_{ij}=q_*}
\]

for every edge, and therefore

\[
\boxed{\ell_{ij}=\ell_*}.
\]

All six edge lengths coincide. A nondegenerate Euclidean tetrahedron with six equal edges is regular. We therefore obtain

\[
\boxed{
\mathbb R^3
\to
\Delta^3
\xrightarrow{A5+A7}
\text{regular tetrahedron}.
}
\]

This is the primary regularity theorem used in the present paper.

## 8. Tetrahedral Gram geometry

Place the barycenter of the regular tetrahedron at the origin and normalize its four center-to-vertex directions:

\[
|n_a|=1.
\]

The barycenter condition gives

\[
\boxed{
\sum_{a=1}^{4}n_a=0.
}
\]

Regularity implies that every off-diagonal inner product has one common value `q`:

\[
n_a\cdot n_b=q
\qquad(a\ne b).
\]

Taking the squared norm of the zero sum,

\[
0
=\left|\sum_a n_a\right|^2
=4+12q,
\]

so

\[
\boxed{q=-\frac13.}
\]

Hence

\[
\boxed{
n_a\cdot n_b=-\frac13
\qquad(a\ne b).
}
\]

The Gram matrix is

\[
\boxed{
G
=\frac43I_4-\frac13\mathbf1\mathbf1^T.
}
\]

Equivalently, the tetrahedral directions form a tight frame:

\[
\boxed{
\sum_{a=1}^{4}n_an_a^T
=\frac43I_3.
}
\]

For oriented rotations the finite stabilizer is

\[
A_4\subset SO(3),
\]

whose inverse image under the `SU(2)` double cover is the binary tetrahedral group

\[
2T\subset SU(2).
\]

## 9. Independent qubit informational convergence

A general qubit density operator has three independent real Bloch coordinates. A normalized `m`-outcome probability vector carries at most `m-1` independent real values. Informational completeness therefore requires

\[
m-1\ge3,
\]

hence

\[
\boxed{m\ge4.}
\]

For four symmetric rank-one outcomes the regular tetrahedral Bloch frame gives

\[
\boxed{n_a\cdot n_b=-\frac13\qquad(a\ne b).}
\]

With

\[
E_a=\frac14(I+n_a\cdot\boldsymbol\sigma),
\]

the measurement probabilities are

\[
p_a=\operatorname{Tr}(\rho E_a)
=\frac14(1+\mathbf r\cdot n_a),
\]

and the tight-frame identity gives exact reconstruction

\[
\boxed{
\mathbf r=3\sum_{a=1}^{4}p_an_a.
}
\]

Thus minimal symmetric qubit informational completeness independently selects the same regular tetrahedral Gram geometry as the spatial simplex route.

## 10. Distance, angle and orthogonality

For nonzero relation vectors `A,B`, define

\[
\|A\|=\sqrt{\langle A,A\rangle}
\]

and

\[
\boxed{
\cos\theta
=\frac{\langle A,B\rangle}{\|A\|\|B\|}.
}
\]

Orthogonality is

\[
\boxed{
A\perp B
\iff
\langle A,B\rangle=0.
}
\]

For consecutive local relations, affine endpoint composition gives

\[
C=A+B.
\]

## 11. Pythagorean closure

The quadratic norm satisfies

\[
\begin{aligned}
\|A+B\|^2
&=\langle A+B,A+B\rangle\\
&=\|A\|^2+\|B\|^2+2\langle A,B\rangle.
\end{aligned}
\]

For orthogonal `A,B`,

\[
\langle A,B\rangle=0,
\]

and therefore

\[
\boxed{
\|A+B\|^2
=\|A\|^2+\|B\|^2.
}
\]

Writing

\[
a=\|A\|,
\qquad
b=\|B\|,
\qquad
c=\|A+B\|,
\]

we obtain

\[
\boxed{a^2+b^2=c^2.}
\]

This is the terminal theorem of the local fundamental construction.

## 12. Boundary of the present construction

The regular tetrahedron has dihedral angle

\[
\theta_T=\arccos(1/3)
\]

with

\[
5\theta_T<2\pi<6\theta_T.
\]

Accordingly, the regular tetrahedron serves here as the minimal local frame. Global simplicial refinement, curvature from angular defects, nontrivial holonomy, torsion sectors, physical scale calibration and the TIR–Time spacetime join form the downstream geometry programme.

## 13. Conclusion

The construction may be summarized as

\[
\boxed{
\text{binary quantum point}
\to
\text{affine state hull}
\to
\text{canonical endpoint displacement}
\to
\mathbb R^3
\to
\Delta^3
\xrightarrow{A5+A7}
\text{regular tetrahedron}
\to
\text{Euclidean inner product}
\to
\text{Pythagoras}.
}
\]

The same tetrahedral Gram structure is reached independently through minimal symmetric informational completeness of a qubit. The result is a compact local bridge from primitive informational relation structure to the elementary closure law of Euclidean geometry.
