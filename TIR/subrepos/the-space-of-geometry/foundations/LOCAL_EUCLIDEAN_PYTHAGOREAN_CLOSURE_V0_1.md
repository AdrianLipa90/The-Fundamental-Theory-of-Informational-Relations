# Local Euclidean and Pythagorean Closure v0.1

Status: `EXACT_LOCAL_EUCLIDEAN_CLOSURE_CANDIDATE`

Scope: local endpoint of *The Space of Geometry*. This note isolates the minimal structure required to reach Euclidean angle, orthogonality and Pythagoras once the local three-dimensional spatial carrier has been promoted.

## 1. Local displacement carrier

Let

\[
V_x\cong\operatorname{Herm}_0(2)
\]

with inner product

\[
\boxed{
\langle A,B\rangle
=\frac12\operatorname{Tr}(AB).
}
\]

For a local relational displacement `A`, define

\[
\boxed{
\|A\|^2=\langle A,A\rangle.
}
\]

The positive-definite Hilbert--Schmidt form gives the local Euclidean norm.

## 2. Endpoint composition in one local frame

For two consecutive local displacements represented in the same local frame,

\[
A:x\to y,
\qquad
B:y\to z,
\]

define the composed displacement by vector addition,

\[
\boxed{
C=A+B.
}
\]

With varying frames this becomes the already-registered transported endpoint law

\[
\mathcal E_{xz}
=
\mathcal E_{xy}
+
\operatorname{Ad}(U_{xy})\mathcal E_{yz}.
\]

The one-frame limit `U_xy=I` gives ordinary vector addition.

## 3. Law of cosines

For arbitrary `A,B`, bilinearity gives

\[
\begin{aligned}
\|A+B\|^2
&=\langle A+B,A+B\rangle\\
&=\|A\|^2+\|B\|^2+2\langle A,B\rangle.
\end{aligned}
\]

For nonzero vectors define

\[
\cos\theta
=
\frac{\langle A,B\rangle}{\|A\|\|B\|}.
\]

Hence

\[
\boxed{
\|A+B\|^2
=
\|A\|^2+\|B\|^2
+2\|A\|\|B\|\cos\theta.
}
\]

This is the local Euclidean law of cosines.

## 4. Orthogonality and Pythagoras

Define

\[
A\perp B
\iff
\langle A,B\rangle=0.
\]

Then

\[
\boxed{
\|A+B\|^2
=
\|A\|^2+\|B\|^2.
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

gives

\[
\boxed{a^2+b^2=c^2.}
\]

This is the declared endpoint of the subrepo.

## 5. Role of the tetrahedron

The regular tetrahedron is the minimal full-dimensional isotropic local cell in the three-dimensional carrier. Its four center-to-vertex unit directions satisfy

\[
\sum_{a=1}^{4}n_a=0,
\qquad
n_a\cdot n_b=-\frac13
\quad(a\ne b).
\]

It supplies a minimal isotropic local relational scaffold. The Euclidean inner product and Pythagorean identity are properties of the carrier itself, so the endpoint theorem requires only the local promoted carrier and its additive displacement law.

## 6. Regular-tetrahedron flat-gluing firewall

A regular tetrahedron has internal dihedral angle

\[
\boxed{
\theta_T=\arccos\left(\frac13\right).
}
\]

Because

\[
\cos\frac{\pi}{3}=\frac12>\frac13,
\]

and cosine decreases on `[0,pi]`,

\[
\theta_T>\frac{\pi}{3}.
\]

Also

\[
\cos\frac{2\pi}{5}
=\frac{\sqrt5-1}{4}
<\frac13,
\]

so

\[
\theta_T<\frac{2\pi}{5}.
\]

Therefore

\[
\boxed{
5\theta_T<2\pi<6\theta_T.
}
\]

No integer number of congruent regular tetrahedra can exactly fill a flat Euclidean neighborhood around a common edge.

This result is useful structurally: the primitive regular tetrahedron is a local minimal cell, while a global flat continuum may use refinement, variable simplices, mixed cells or a continuum limit rather than a face-to-face tessellation by identical regular tetrahedra.

## 7. Scope reduction

The core paper can terminate at the local theorem

\[
\boxed{
\text{promoted inner-product carrier}
\to
\text{distance}
\to
\text{angle}
\to
\text{orthogonality}
\to
\text{Pythagoras}.
}
\]

Global manifold construction, tetrahedral refinement and curvature belong to a downstream geometry programme. They are not prerequisites for the local Pythagorean endpoint.

## 8. Claim classes

| Statement | Class |
|---|---|
| Hilbert--Schmidt form on `Herm_0(2)` is positive Euclidean | EXACT |
| local vector composition yields the law of cosines | EXACT INNER-PRODUCT ALGEBRA |
| orthogonality yields `a^2+b^2=c^2` | EXACT |
| regular tetrahedral dihedral angle is `acos(1/3)` | STANDARD EXACT GEOMETRY |
| `5 theta_T < 2pi < 6 theta_T` | EXACT |
| identical regular tetrahedra do not form a flat face-to-face edge tessellation | EXACT CONSEQUENCE |
| a regular tetrahedron is the minimal isotropic local cell under the declared conditions | EXACT CONDITIONAL, UPSTREAM |
| global continuum/refinement | DOWNSTREAM RESEARCH PROGRAMME |
