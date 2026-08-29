# The Space of Geometry — Research Spine v0.4

Status: `TIR_SPACE_OF_GEOMETRY_SPINE_V0_4_CANDIDATE`

## 1. Shortest local derivation route

The current shortest route is

\[
\boxed{
\text{QUANTUM POINT}
\to
\text{normalized state }\rho_x
\to
\mathcal A_2=\frac12I+\operatorname{Herm}_0(2)
\to
\text{intrinsic affine displacement}
\to
\operatorname{Herm}_0(2)\cong\mathbb R^3
\to
\Delta^3
\to
\text{metric / angle / orthogonality}
\to
\text{PYTHAGORAS}.
}
\]

The first-distinction and half-seam line remains the upstream TIR route that supplies the minimal binary quantum carrier.

## 2. Exact affine theorem

Every affine space `A` modeled on a vector space `V` is a torsor for `V`. For every ordered pair `x,y in A`, there is a unique vector

\[
\delta(x,y)\in V
\]

such that

\[
x+\delta(x,y)=y.
\]

Hence

\[
\boxed{\delta(x,y)=y-x}
\]

and exactly

\[
\delta(y,x)=-\delta(x,y),
\]

\[
\delta(x,z)=\delta(x,y)+\delta(y,z),
\]

\[
\delta(x+a,y+a)=\delta(x,y).
\]

## 3. Quantum-point specialization

For the binary point carrier

\[
\rho_x=\frac12(I+\mathbf r_x\cdot\boldsymbol\sigma),
\]

its trace-one Hermitian affine hull is

\[
\boxed{
\mathcal A_2=\frac12I+\operatorname{Herm}_0(2)
}
\]

with

\[
\boxed{
\dim_{\mathbb R}\operatorname{Herm}_0(2)=3.
}
\]

The intrinsic ordered relation displacement is

\[
\delta(\rho_x,\rho_y)=\rho_y-\rho_x.
\]

With Pauli normalization,

\[
\boxed{
\mathcal E_{xy}=2(\rho_y-\rho_x)
=(\mathbf r_y-\mathbf r_x)\cdot\boldsymbol\sigma.
}
\]

Thus the same relation object supplies real dimension three, orientation, endpoint composition and an origin-independent local displacement.

## 4. Intrinsic affine naturality

If a primitive vector relation law is required to use only the affine structure already present in the point-state carrier, then it must be natural under affine frame changes

\[
F(x)=Lx+a,
\qquad L\in GL(V),
\]

through

\[
R(Fx,Fy)=L R(x,y).
\]

Translation naturality gives

\[
R(x,y)=f(y-x),
\]

and `GL(V)` equivariance gives

\[
f(Lv)=L f(v).
\]

The stabilizer of a nonzero `v` fixes only `span(v)`, and `GL(V)` is transitive on nonzero vectors. Therefore every continuous intrinsic affine vector relation law has the form

\[
\boxed{R(x,y)=c(y-x).}
\]

Distinction preservation requires `c != 0`; scale and orientation remain conventional. The torsor normalization is `c=1`, while the Pauli-coordinate convention is `c=2` relative to density-operator difference.

This reduces the remaining TIR bridge to whether A1 minimality plus A3 relational primacy select intrinsic affine naturality, i.e. a relation law with no auxiliary origin, axis or background object.

## 5. Metric

The canonical invariant quadratic form is

\[
\boxed{
\langle A,B\rangle
=\frac12\operatorname{Tr}(AB).
}
\]

For the Pauli-normalized displacement,

\[
\boxed{
\|\mathcal E_{xy}\|^2
=|\mathbf r_y-\mathbf r_x|^2.
}
\]

## 6. Minimal local cell

The affine carrier has real dimension three. The minimal full-dimensional simplex therefore has four vertices:

\[
\boxed{\Delta^3.}
\]

Under equal weighting and full local isotropy,

\[
\sum_{a=1}^{4}\mathbf n_a=0,
\qquad
\mathbf n_a\cdot\mathbf n_b=-\frac13\quad(a\ne b),
\]

so the minimal isotropic cell is the regular tetrahedron.

The same four pure-state directions form a minimal affine frame of the qubit-state hull and the tetrahedral qubit SIC, providing an independent informational convergence check.

## 7. Pythagorean closure

Affine endpoint composition gives

\[
\mathcal E_{xz}=\mathcal E_{xy}+\mathcal E_{yz}.
\]

Therefore

\[
\|\mathcal E_{xz}\|^2
=\|\mathcal E_{xy}\|^2
+\|\mathcal E_{yz}\|^2
+2\langle\mathcal E_{xy},\mathcal E_{yz}\rangle.
\]

For orthogonal consecutive relations,

\[
\langle\mathcal E_{xy},\mathcal E_{yz}\rangle=0,
\]

and hence

\[
\boxed{a^2+b^2=c^2.}
\]

## 8. Remaining foundational typing gate

The exact affine mathematics has reduced the promotion problem to one TIR inheritance question:

\[
\boxed{
A1+A3:\ \text{primitive relation uses the minimal intrinsic affine-natural law on the A2 point-state carrier.}
}
\]

Under that typing, the local route from quantum point to three-dimensional Euclidean relation geometry is closed by standard affine and representation mathematics.

A5 then measures the geometry through arithmetic invariants of the relation carrier. A8 acts as the consistency/context-lift layer: local affine displacement has exact endpoint closure, while nontrivial loop/context defects are retained for downstream curvature and holonomy.

## 9. Proof-status surface

| Edge | Status |
|---|---|
| binary quantum carrier -> trace-one affine hull | EXACT / STANDARD QUANTUM MATHEMATICS |
| affine hull translation space -> `Herm_0(2)` | EXACT |
| `Herm_0(2)` real dimension -> 3 | EXACT |
| ordered affine pair -> unique displacement | EXACT AFFINE GEOMETRY |
| intrinsic affine-natural relation -> `c(y-x)` | EXACT CONDITIONAL NATURALITY THEOREM |
| distinction preservation -> `c != 0` | EXACT CONDITIONAL |
| displacement -> endpoint composition | EXACT |
| displacement -> Hilbert--Schmidt Euclidean metric | EXACT |
| 3D -> minimal full-dimensional simplex `Delta^3` | EXACT AFFINE GEOMETRY |
| equal isotropy -> regular tetrahedron | EXACT CONDITIONAL |
| orthogonality -> Pythagoras | EXACT |
| A1+A3 select intrinsic affine naturality | TIR FOUNDATIONAL INHERITANCE GATE |

## 10. Paper endpoint

The paper remains deliberately local and terminates at Pythagorean closure. Global tetrahedral refinement, curvature, holonomy, torsion sectors and the TIR x Time spacetime join remain downstream programmes.
