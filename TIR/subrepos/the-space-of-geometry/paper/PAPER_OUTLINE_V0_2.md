# The Space of Geometry: From First Distinction to Pythagoras

Paper outline v0.2

## Abstract target

Present the shortest auditable local derivation from the primitive TIR distinction structure to Euclidean Pythagorean closure. The core theorem line is: binary quantum carrier -> traceless Hermitian real generator space -> minimal faithful real orthogonal realization of the primitive rotational symmetry -> three-dimensional local spatial carrier -> minimal tetrahedral simplex -> inner-product distance, angle and orthogonality -> Pythagoras.

A tetrahedral qubit SIC supplies an independent information-theoretic convergence check. Global manifold/refinement construction is separated from the local endpoint.

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

## 2. Primitive relational input

Import the TIR first-distinction chain and binary quantum lift:

\[
0\to P\to\{N,S\}\to\frac12\to\ln2\to\mathbb C^2.
\]

## 3. Exact real generator geometry

Construct

\[
\mathfrak g_{\rm rel}=\operatorname{Herm}_0(2)
=\operatorname{span}_{\mathbb R}\{\sigma_x,\sigma_y,\sigma_z\}
\]

with

\[
\langle A,B\rangle=\frac12\operatorname{Tr}(AB).
\]

Establish:

\[
\dim_{\mathbb R}\mathfrak g_{\rm rel}=3,
\]

\[
SU(2)/\{\pm I\}\cong SO(3),
\]

and invariance of the Hilbert--Schmidt metric under conjugation.

## 4. Spatial promotion as a uniqueness theorem

Define the spatial-realization criterion: the local physical displacement carrier is finite-dimensional, real, continuous, orthogonal, faithful under the full primitive `SO(3)` action, and minimal among such carriers.

Prove:

- real dimension 1 gives only a trivial connected orthogonal image;
- real dimension 2 gives connected image in abelian `SO(2)`, excluding faithful `SO(3)` action;
- the defining real dimension-3 `SO(3)` representation is faithful.

Therefore

\[
\boxed{
V_x\cong\mathbb R^3\cong\operatorname{Herm}_0(2)
}
\]

up to orthogonal equivalence, with invariant positive metric unique up to scale.

The explicit TIR gate is to derive the realization criterion from the primitive axioms.

## 5. Minimal geometry: the tetrahedron

A full-dimensional simplex in three dimensions needs four affinely independent vertices:

\[
\Delta^3.
\]

Under equal norm and full isotropy derive

\[
\sum_a n_a=0,
\qquad
\sum_a n_an_a^T=\frac43I_3,
\]

and

\[
\boxed{n_a\cdot n_b=-\frac13\quad(a\ne b).}
\]

Thus the minimal isotropic local cell is the regular tetrahedron.

## 6. Independent informational convergence

Show that a qubit requires at least four normalized outcome probabilities for informational completeness and that the minimal symmetric solution is the tetrahedral SIC.

Keep this as an independent convergence/cross-check rather than an additional premise in the spatial derivation.

## 7. Local displacement, distance and angle

For

\[
A=A^a\sigma_a,
\]

use

\[
\|A\|^2=\frac12\operatorname{Tr}(A^2).
\]

For consecutive local displacements in one frame, use

\[
C=A+B.
\]

Define

\[
\cos\theta=\frac{\langle A,B\rangle}{\|A\|\|B\|}
\]

and

\[
A\perp B\iff\langle A,B\rangle=0.
\]

## 8. Pythagorean closure

Expand

\[
\|A+B\|^2
=\|A\|^2+\|B\|^2+2\langle A,B\rangle.
\]

For orthogonal `A,B`, obtain

\[
\boxed{a^2+b^2=c^2.}
\]

Terminate the fundamental derivation here.

## 9. Global-gluing firewall

Record the regular tetrahedron dihedral angle

\[
\theta_T=\arccos(1/3)
\]

and the exact inequality

\[
5\theta_T<2\pi<6\theta_T.
\]

This shows why a global flat Euclidean continuum should not be built by assuming an exact face-to-face tessellation of congruent regular tetrahedra. Global refinement and curvature are a separate downstream programme.

## 10. Proof-status table

The manuscript should classify every statement as one of:

- exact linear algebra / group theory;
- exact conditional geometry;
- TIR realization criterion gate;
- independent information-theoretic convergence;
- downstream global refinement.

## 11. Conclusion target

\[
\boxed{
\text{distinction}
\to
\mathbb C^2
\to
\operatorname{Herm}_0(2)
\to
\text{minimal faithful }SO(3)\text{ carrier}
\to
\mathbb R^3
\to
\Delta^3
\to
\text{Euclidean inner product}
\to
\text{Pythagoras}.
}
\]
