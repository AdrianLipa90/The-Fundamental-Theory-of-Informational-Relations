# TIR Polygonal Excitation — Stage 10: Platonic Closure of the N=4 and N=5 Equal-Edge Stars

Status: `STAGE_10_PURE_MATHEMATICS_PASS`

Parent frozen prediction: `TIR_POLYGONAL_EXCITATION_POINCARE_ORBITAL_HYPOTHESIS_V0_1.md`

Scope: pure geometric and combinatorial validation. Particle, atomic, and spectroscopic assignments remain outside this stage.

## 1. Equal-edge pole-to-N-gon family

Let the apex be

\[
P=(0,0,1),
\]

and let the regular base vertices on the unit sphere be

\[
b_k=\left(\sqrt{1-c_N^2}\cos\frac{2\pi k}{N},\sqrt{1-c_N^2}\sin\frac{2\pi k}{N},c_N\right).
\]

Requiring each apex-base edge to equal each adjacent base edge gives

\[
1=(1+c_N)\left(1-\cos\frac{2\pi}{N}\right),
\]

hence

\[
\boxed{c_N=\frac{\cos(2\pi/N)}{1-\cos(2\pi/N)}}.
\]

The lateral faces are therefore equilateral triangles.

For the cases of interest,

\[
c_3=-\frac13,
\qquad
c_4=0,
\qquad
c_5=\frac1{\sqrt5},
\qquad
c_6=1.
\]

## 2. Discrete curvature at the apex

Each equilateral triangular face contributes an apex angle \(\pi/3\). The angular defect of an N-fold triangular vertex star is therefore

\[
\boxed{\delta_N=2\pi-\frac{N\pi}{3}=\frac{(6-N)\pi}{3}}.
\]

Thus

\[
\delta_3=\pi,
\qquad
\delta_4=\frac{2\pi}{3},
\qquad
\delta_5=\frac{\pi}{3},
\qquad
\delta_6=0.
\]

The sequence N=3,4,5 has positive discrete curvature; N=6 is the zero-defect boundary.

## 3. Global regular triangular closure

Assume a closed regular triangular tessellation in which exactly N triangular faces meet at every vertex. Let \(V,E,F\) denote the numbers of vertices, edges, and triangular faces.

Incidence counting gives

\[
NV=2E,
\qquad
3F=2E.
\]

Together with Euler's relation

\[
V-E+F=2,
\]

this yields

\[
\boxed{V_N=\frac{12}{6-N}},
\qquad
\boxed{E_N=\frac{6N}{6-N}},
\qquad
\boxed{F_N=\frac{4N}{6-N}}.
\]

For the finite positive-curvature cases:

| N | \(V_N\) | \(E_N\) | \(F_N\) | Regular closure |
|---:|---:|---:|---:|---|
| 3 | 4 | 6 | 4 | tetrahedron \(\{3,3\}\) |
| 4 | 6 | 12 | 8 | octahedron \(\{3,4\}\) |
| 5 | 12 | 30 | 20 | icosahedron \(\{3,5\}\) |

At N=6 the finite spherical closure formula has a zero denominator while \(\delta_6=0\). The corresponding regular triangular geometry is the Euclidean \(\{3,6\}\) tiling.

## 4. Gauss-Bonnet consistency

For N=3,4,5,

\[
V_N\delta_N
=
\frac{12}{6-N}\frac{(6-N)\pi}{3}
=
\boxed{4\pi}.
\]

Therefore the total discrete curvature of every finite member is exactly the total Gaussian curvature of the unit sphere.

The numerical audit reproduces this identity to floating-point precision.

## 5. Exact N=4 identification

For N=4,

\[
c_4=0,
\]

so the four base vertices lie on the equator. With the north-pole apex they form the upper vertex star of the regular octahedron. Adding the antipodal south pole gives the complete six-vertex octahedral closure.

The numerical audit verifies four apex neighbours and the equal-edge dot-product condition with residual below \(10^{-12}\).

## 6. Exact N=5 identification

For N=5,

\[
\boxed{c_5=\frac1{\sqrt5}}.
\]

For a normalized regular icosahedron, adjacent vertices have exactly the same dot product \(1/\sqrt5\). Every icosahedral vertex has five such neighbours, and those five neighbours form a pentagonal cycle under the same edge criterion.

Therefore the N=5 equal-edge pole-to-pentagon construction is exactly the local vertex star of the regular icosahedron.

The numerical audit verifies a five-neighbour ring with degree sequence

\[
(2,2,2,2,2)
\]

inside that neighbour set.

## 7. Stage verdict

The equal-edge sequence now has an exact finite spherical classification:

\[
\boxed{
N=3\to\{3,3\},
\quad
N=4\to\{3,4\},
\quad
N=5\to\{3,5\},
\quad
N=6\to\{3,6\}\text{ boundary}
}
\]

The Stage 10 result is therefore:

`STAGE_10_PURE_MATHEMATICS_PASS`

The frozen v0.1 prediction remains unchanged. The next gate is the spinor double-cover structure of the N=4 and N=5 rotational stabilizers.