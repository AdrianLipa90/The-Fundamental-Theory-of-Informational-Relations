# The Space of Geometry: From First Distinction to Pythagoras

Manuscript draft v0.2

Status: `LOCAL_DEPENDENCY_FORK_CLOSED_AT_TIR_AXIOM_MODEL_LEVEL_CANDIDATE`

## Abstract

We construct a local relation geometry from the binary quantum-point carrier of the Theory of Informational Relations (TIR). The normalized two-level state space has affine hull

\[
\mathcal A_2=\frac12I+\operatorname{Herm}_0(2),
\]

whose translation space has real dimension three. Every ordered pair of normalized point states determines the unique endpoint-carrying affine displacement

\[
\delta(\rho_x,\rho_y)=\rho_y-\rho_x.
\]

With Pauli normalization this becomes

\[
\mathcal E_{xy}=2(\rho_y-\rho_x)
\in\operatorname{Herm}_0(2)\cong\mathbb R^3.
\]

The `SU(2)` conjugation action induces the standard `SO(3)` action and preserves the positive quadratic form `Tr(AB)/2`. At this point the derivation forks. The first branch is directly Euclidean: additive endpoint composition plus the invariant inner product supplies distance, angle, orthogonality and the Pythagorean norm identity. The second branch asks for the minimal finite full-dimensional cell of the same three-dimensional carrier. Four affinely independent vertices are necessary and sufficient, giving a 3-simplex. Its unlabeled automorphism group is `S_4`, transitive on the six edges. Applying the TIR arithmetic-geometric measure axiom A5 and law-symmetry axiom A7 to the edge-measure law makes all six edge lengths equal, selecting the regular tetrahedron. Its centered unit directions obey

\[
n_a\cdot n_b=-\frac13\qquad(a\ne b).
\]

The same Gram frame appears independently as the tetrahedral qubit SIC. Thus Pythagorean closure and the tetrahedral finite-cell theorem are parallel consequences of the common local carrier rather than steps in one another's proofs. Global triangulation, curvature, holonomy and the TIR–Time spacetime join are downstream.

## 1. Question and scope

The question is deliberately narrow:

\[
\boxed{
\text{How little primitive relational structure is required for local Euclidean geometry to appear?}
}
\]

The principal endpoint is the local Pythagorean identity

\[
\boxed{a^2+b^2=c^2.}
\]

A second result characterizes the minimal finite full-dimensional local cell and its symmetry. These are kept as separate theorem branches after their common carrier is constructed.

The dependency graph is

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
V=\operatorname{Herm}_0(2)\cong\mathbb R^3
}
\]

followed by

\[
\boxed{
V
\to
\begin{cases}
\text{invariant inner product}
\to
\text{distance / angle / orthogonality}
\to
\text{Pythagoras},\\[2mm]
\text{minimal finite support}
\to
\Delta^3
\xrightarrow{A5+A7}
\text{regular tetrahedron}
\to
\text{tetrahedral Gram/SIC convergence}.
\end{cases}
}
\]

This fork is important: the tetrahedron is a theorem about minimal finite support of the derived three-dimensional carrier. The Pythagorean identity follows directly from the inner-product branch.

## 2. Imported TIR root

The parent TIR programme supplies the primitive chain

\[
0
\to P
\to \text{FIRST DISTINCTION}
\to \{N,S\}
\to \frac12
\to \ln2
\to \mathbb C^2.
\]

The present paper begins its new construction at the binary quantum carrier. A normalized point state is represented by

\[
\rho_x=\rho_x^\dagger,
\qquad
\operatorname{Tr}\rho_x=1.
\]

Every two-level state has Bloch form

\[
\boxed{
\rho_x
=\frac12\left(I+\mathbf r_x\cdot\boldsymbol\sigma\right),
\qquad
|\mathbf r_x|\le1,
}
\]

where

\[
\boldsymbol\sigma=(\sigma_x,\sigma_y,\sigma_z).
\]

## 3. The normalized state hull is a three-real-dimensional affine space

The real vector space of Hermitian `2 x 2` matrices is

\[
\operatorname{Herm}(2)
=\{a_0I+a_i\sigma_i:a_\mu\in\mathbb R\}
\]

and therefore

\[
\dim_{\mathbb R}\operatorname{Herm}(2)=4.
\]

Trace normalization imposes one real affine constraint. Hence

\[
\boxed{
\mathcal A_2
=\left\{\rho=\rho^\dagger:\operatorname{Tr}\rho=1\right\}
=\frac12I+\operatorname{Herm}_0(2).
}
\]

Its translation space is

\[
\boxed{
V=\operatorname{Herm}_0(2)
=\operatorname{span}_{\mathbb R}\{\sigma_x,\sigma_y,\sigma_z\}
\cong\mathbb R^3.
}
\]

Therefore

\[
\boxed{
\dim_{\mathbb R}V=3.
}
\]

This is the common carrier theorem for both downstream branches.

## 4. Canonical endpoint-carrying relation

An affine space is a torsor for its translation space. For every ordered pair

\[
\rho_x,\rho_y\in\mathcal A_2
\]

there exists exactly one vector

\[
\delta_{xy}\in V
\]

such that

\[
\boxed{
\rho_x+\delta_{xy}=\rho_y.
}
\]

By uniqueness of the torsor translation,

\[
\boxed{
\delta_{xy}=\rho_y-\rho_x.
}
\]

The TIR spatial branch exports this canonical endpoint-carrying affine displacement as its primitive vector relation. In Pauli generator normalization,

\[
\boxed{
\mathcal E_{xy}:=2(\rho_y-\rho_x)
=(\mathbf r_y-\mathbf r_x)\cdot\boldsymbol\sigma.
}
\]

No coordinate origin is needed. The relation is intrinsic to the ordered endpoints in their affine carrier.

The torsor identities immediately yield

\[
\boxed{\mathcal E_{yx}=-\mathcal E_{xy},}
\]

\[
\boxed{
\mathcal E_{xz}=\mathcal E_{xy}+\mathcal E_{yz},
}
\]

and

\[
\boxed{
\mathcal E_{xy}+\mathcal E_{yz}+\mathcal E_{zx}=0.
}
\]

The earlier source-minimality/naturality theorem and minimal faithful real `SO(3)` representation theorem remain independent uniqueness checks on this construction.

## 5. Rotational covariance and invariant metric

For

\[
U\in SU(2),
\]

a common quantum-frame transformation acts by conjugation:

\[
\rho\mapsto U\rho U^\dagger.
\]

Therefore

\[
\boxed{
\mathcal E_{xy}\mapsto U\mathcal E_{xy}U^\dagger.
}
\]

The effective action on the three real Pauli coefficients factors through

\[
\boxed{
SU(2)/\{\pm I\}\cong SO(3).
}
\]

The defining three-dimensional real `SO(3)` representation is irreducible. Its positive invariant inner product is unique up to an overall positive scale. With the canonical Pauli normalization,

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

we have

\[
\boxed{
\|\mathcal E_{xy}\|^2
=\frac12\operatorname{Tr}(\mathcal E_{xy}^2)
=|\mathbf r_y-\mathbf r_x|^2.
}
\]

A5 supplies the TIR arithmetic/geometric crosswalk for this invariant.

# Part I — The Euclidean branch

## 6. Theorem E: local Euclidean closure

Let

\[
A=\mathcal E_{xy},
\qquad
B=\mathcal E_{yz}.
\]

Torsor endpoint composition gives

\[
\boxed{
\mathcal E_{xz}=A+B.
}
\]

Define the local relation length by

\[
\|A\|=\sqrt{\langle A,A\rangle}.
\]

For nonzero `A,B`, define the angle by

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

The quadratic norm obeys

\[
\begin{aligned}
\|A+B\|^2
&=\langle A+B,A+B\rangle\\
&=\|A\|^2+\|B\|^2+2\langle A,B\rangle.
\end{aligned}
\]

For orthogonal `A,B`,

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

This is the principal endpoint of the paper.

### Theorem E

The canonical affine relation carrier of normalized binary quantum points is a three-real-dimensional inner-product space with additive endpoint composition. Consequently, orthogonal consecutive local relations satisfy the Pythagorean norm identity.

# Part II — The finite-cell branch

## 7. Theorem T1: minimal finite full-dimensional support

Let

\[
x_1,\ldots,x_m
\]

be points in a three-dimensional affine carrier. Their affine span satisfies

\[
\dim\operatorname{Aff}\{x_1,\ldots,x_m\}
\le m-1.
\]

Full three-dimensional support requires

\[
3\le m-1,
\]

so

\[
\boxed{m\ge4.}
\]

At the minimum, four affinely independent vertices define exactly the 3-simplex

\[
\boxed{
\Delta^3=\operatorname{conv}\{x_1,x_2,x_3,x_4\}.
}
\]

Thus the tetrahedron is the minimal finite full-dimensional affine cell of the same derived local carrier.

## 8. Theorem T2: regularity from A5+A7 edge-orbit invariance

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

The natural `S_4` action on these six edges is transitive. Thus all primitive simplex edges lie in one intrinsic combinatorial symmetry orbit.

For each realized edge define

\[
\boxed{
q_{ij}:=\frac12\operatorname{Tr}(\mathcal E_{ij}^2),
\qquad
\ell_{ij}:=\sqrt{q_{ij}}.
}
\]

A5 types `q_ij` as an arithmetic measure of the relation geometry. A7 requires the primitive edge-measure law to be invariant under the intrinsic simplex automorphism action:

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

All six edge lengths coincide. A nondegenerate Euclidean tetrahedron with six equal edges is regular. Hence

\[
\boxed{
\mathbb R^3
\to
\Delta^3
\xrightarrow{A5+A7}
\text{regular tetrahedron}.
}
\]

The maximal-symmetry and moment-isotropy derivations remain independent crosschecks of this result.

## 9. Tetrahedral Gram geometry

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

Regularity makes every off-diagonal inner product equal to one common value `q`. Therefore

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
G=\frac43I_4-\frac13\mathbf1\mathbf1^T.
}
\]

The frame operator is

\[
\boxed{
\sum_{a=1}^{4}n_an_a^T
=\frac43I_3.
}
\]

The orientation-preserving rotational subgroup is

\[
A_4\subset SO(3),
\]

whose inverse image under the `SU(2)` double cover is the binary tetrahedral group

\[
2T\subset SU(2).
\]

# Part III — Independent informational convergence

## 10. Theorem Q: tetrahedral qubit informational completeness

A general qubit density operator contains three independent real Bloch coordinates. A normalized `m`-outcome probability vector has at most `m-1` independent real entries. Hence informational completeness requires

\[
m-1\ge3,
\]

so

\[
\boxed{m\ge4.}
\]

For four symmetric rank-one outcomes, the tetrahedral Bloch frame has

\[
\boxed{n_a\cdot n_b=-\frac13\quad(a\ne b).}
\]

Define

\[
E_a=\frac14(I+n_a\cdot\boldsymbol\sigma).
\]

Then

\[
p_a=\operatorname{Tr}(\rho E_a)
=\frac14(1+\mathbf r\cdot n_a).
\]

Using

\[
\sum_an_an_a^T=\frac43I_3,
\]

one reconstructs

\[
\boxed{
\mathbf r=3\sum_{a=1}^{4}p_an_a.
}
\]

Thus the minimal symmetric qubit informational-completeness construction and the minimal regular finite-cell construction converge on the same tetrahedral Gram geometry.

The spatial edge relation and the informational measurement outcome retain separate physical typing in this paper; the equality of their finite frame geometry is the convergence result.

## 11. Dependency summary

The common carrier theorem is

\[
\boxed{
\mathbb C^2
\to
\mathcal A_2
\to
\delta_{xy}
\to
V\cong\mathbb R^3.
}
\]

From this carrier:

\[
\boxed{
V
\to
\text{Theorem E: Euclidean/Pythagorean closure}
}
\]

and independently

\[
\boxed{
V
\to
\text{Theorem T: minimal regular tetrahedral cell}.
}
\]

The qubit measurement branch then gives

\[
\boxed{
\text{Theorem Q: independent tetrahedral SIC convergence}.
}
\]

This dependency split prevents the finite-cell theorem from being used as an unnecessary premise of the Pythagorean theorem.

## 12. Global geometry boundary

A regular tetrahedron has dihedral angle

\[
\theta_T=\arccos(1/3)
\]

and

\[
5\theta_T<2\pi<6\theta_T.
\]

Thus congruent regular tetrahedra do not exactly fill a flat Euclidean neighborhood around an edge. The tetrahedron is used here as a minimal local finite frame. Global simplicial refinement, curvature encoded by angular defects, nontrivial holonomy, torsion sectors, physical scale calibration and the TIR–Time spacetime join are downstream developments.

## 13. Conclusion

The present local construction begins with the normalized binary quantum-point carrier and produces a canonical affine relation displacement in

\[
\operatorname{Herm}_0(2)\cong\mathbb R^3.
\]

The invariant inner product immediately supplies Euclidean norm geometry and the Pythagorean closure law. Independently, minimal finite support of the same carrier produces a 3-simplex; A5+A7 invariance on its intrinsic edge orbit selects the regular tetrahedron. Minimal symmetric qubit informational completeness reaches the same tetrahedral Gram frame from a separate measurement-theoretic route.

The final structure is therefore

\[
\boxed{
\text{binary quantum point}
\to
\text{canonical three-dimensional relation carrier}
\to
\begin{cases}
\text{Euclidean inner product}\to\text{Pythagoras},\\
\text{minimal finite cell}\to\text{regular tetrahedron}\leftarrow\text{qubit SIC}.
\end{cases}
}
\]
