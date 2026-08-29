# The Space of Geometry: From First Distinction to Pythagoras

Paper outline v0.3

Status: `LOCAL_DERIVATION_CLOSED_AT_TIR_AXIOM_MODEL_LEVEL_CANDIDATE`

## Abstract target

Present a short auditable construction of local Euclidean relation geometry from the binary quantum-point carrier. The normalized two-level state hull is a three-real-dimensional affine torsor whose unique endpoint-carrying displacement lies in `Herm_0(2)`. Minimal full-dimensional affine support therefore gives a 3-simplex. The intrinsic automorphism group of the unlabeled simplex acts transitively on its edges; applying the A5 geometric edge measure and A7 law invariance makes all six edge lengths equal, selecting the regular tetrahedron. The invariant inner product then gives distance, angle, orthogonality and Pythagorean closure.

A tetrahedral qubit SIC supplies an independent information-theoretic convergence on the same Gram frame. Global refinement, curvature and spacetime closure are downstream.

## 1. Research question

\[
\boxed{
\text{How little primitive relational structure is required for local Euclidean geometry to appear?}
}
\]

Endpoint:

\[
\boxed{a^2+b^2=c^2.}
\]

## 2. Imported TIR root

Import only the upstream primitive chain required to supply the binary quantum carrier:

\[
0
\to P
\to \text{FIRST DISTINCTION}
\to \{N,S\}
\to \frac12
\to \ln2
\to \mathbb C^2.
\]

The paper begins its new geometry derivation at the normalized binary quantum-point state.

## 3. Quantum-point affine geometry

Write

\[
\rho_x=\frac12(I+\mathbf r_x\cdot\boldsymbol\sigma).
\]

The trace-one Hermitian affine hull is

\[
\boxed{
\mathcal A_2=\frac12I+\operatorname{Herm}_0(2).
}
\]

Therefore

\[
\boxed{
\dim_{\mathbb R}\mathcal A_2=3,
\qquad
T\mathcal A_2=\operatorname{Herm}_0(2)\cong\mathbb R^3.
}
\]

## 4. Canonical relational displacement

Use the universal affine-torsor property: for every ordered pair there is a unique vector `delta_xy` satisfying

\[
\rho_x+\delta_{xy}=\rho_y.
\]

Hence

\[
\boxed{
\delta_{xy}=\rho_y-\rho_x.
}
\]

In Pauli generator normalization,

\[
\boxed{
\mathcal E_{xy}=2(\rho_y-\rho_x)
=(\mathbf r_y-\mathbf r_x)\cdot\boldsymbol\sigma.
}
\]

Derive immediately:

\[
\mathcal E_{yx}=-\mathcal E_{xy},
\]

\[
\boxed{
\mathcal E_{xz}=\mathcal E_{xy}+\mathcal E_{yz},
}
\]

and triangular closure.

The previous minimal-faithful-`SO(3)` promotion theorem remains an independent representation-theoretic crosscheck rather than the primary construction.

## 5. Invariant local metric

The `SU(2)` conjugation action on `Herm_0(2)` factors through

\[
PSU(2)\cong SO(3).
\]

The positive invariant inner product is unique up to scale. Use the canonical Pauli normalization

\[
\boxed{
\langle A,B\rangle=\frac12\operatorname{Tr}(AB).
}
\]

Then

\[
\boxed{
\|\mathcal E_{xy}\|^2
=|\mathbf r_y-\mathbf r_x|^2.
}
\]

A5 supplies the arithmetic/geometric measurement crosswalk.

## 6. Minimal three-dimensional cell

For `m` affine points,

\[
\dim\operatorname{Aff}\{x_1,\ldots,x_m\}\le m-1.
\]

Since the local carrier has dimension three,

\[
\boxed{m\ge4.}
\]

The minimum full-dimensional cell is therefore

\[
\boxed{\Delta^3.}
\]

This is the primary tetrahedrality theorem.

## 7. Regularity from A5+A7 edge-orbit invariance

The abstract unlabeled simplex has

\[
\boxed{\operatorname{Aut}(\Delta^3)\cong S_4.}
\]

Its six edges form one orbit under `S_4`.

Define

\[
q_{ij}=\frac12\operatorname{Tr}(\mathcal E_{ij}^2),
\qquad
\ell_{ij}=\sqrt{q_{ij}}.
\]

A7 invariance of the geometric edge-measure law under the intrinsic simplex automorphisms gives

\[
q_{\pi(i)\pi(j)}=q_{ij}.
\]

Transitivity of the edge orbit therefore gives

\[
\boxed{q_{ij}=q_*}
\]

and

\[
\boxed{\ell_{ij}=\ell_*}
\]

for all six edges. Hence the tetrahedron is regular.

This is the preferred regularity route. Maximal-symmetry and moment-isotropy derivations remain crosschecks.

## 8. Tetrahedral Gram geometry

Center and normalize the regular tetrahedron. Derive

\[
\boxed{\sum_{a=1}^{4}n_a=0}
\]

and

\[
\boxed{n_a\cdot n_b=-\frac13\quad(a\ne b).}
\]

Therefore

\[
\boxed{G=\frac43I_4-\frac13\mathbf1\mathbf1^T}
\]

and

\[
\boxed{\sum_an_an_a^T=\frac43I_3.}
\]

The oriented rotational subgroup is `A_4 subset SO(3)` with binary tetrahedral lift `2T subset SU(2)`.

## 9. Independent informational convergence

For a qubit, normalized outcome probabilities carry at most `m-1` independent real parameters, so informational completeness requires

\[
m\ge4.
\]

The minimal symmetric rank-one solution is the tetrahedral SIC with the same Gram relation

\[
\boxed{n_a\cdot n_b=-\frac13.}
\]

Keep this as an independent convergence/crosscheck rather than a premise in the spatial derivation.

## 10. Distance, angle and orthogonality

For relation vectors `A,B`, define

\[
\|A\|^2=\langle A,A\rangle,
\]

\[
\cos\theta=\frac{\langle A,B\rangle}{\|A\|\|B\|},
\]

and

\[
\boxed{A\perp B\iff\langle A,B\rangle=0.}
\]

Endpoint composition supplies

\[
C=A+B.
\]

## 11. Pythagorean closure

Expand

\[
\|A+B\|^2
=\|A\|^2+\|B\|^2+2\langle A,B\rangle.
\]

For orthogonal `A,B`, obtain

\[
\boxed{a^2+b^2=c^2.}
\]

Terminate the fundamental local derivation here.

## 12. Global geometry boundary

For a regular tetrahedron

\[
\theta_T=\arccos(1/3)
\]

and

\[
5\theta_T<2\pi<6\theta_T.
\]

Use the tetrahedron as the minimal local frame. Treat global triangulation, curvature, holonomy, torsion and continuum refinement as downstream geometry.

## 13. Proof-status surface

The manuscript should distinguish:

- imported TIR primitive input;
- canonical affine construction;
- exact linear algebra / group theory;
- A5/A7 axiom crosswalk;
- independent information-theoretic convergence;
- downstream global geometry.

## 14. Conclusion target

\[
\boxed{
\text{binary quantum point}
\to
\text{affine state hull}
\to
\text{canonical displacement}
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
