# Minimal 3-Simplex and Maximal Symmetry v0.1

Status: `EXACT_CONDITIONAL_REGULAR_TETRAHEDRON_SYMMETRY_THEOREM_CANDIDATE`

Scope: sharpen the step from the minimal full-dimensional 3-simplex to the regular tetrahedral local frame without using moment-isotropy as the primary selector.

## 1. Minimal full-dimensional simplex

Let `V` be a real affine space of dimension three. For `m` points,

\[
\dim\operatorname{Aff}\{x_1,\ldots,x_m\}\le m-1.
\]

Full affine dimension therefore requires

\[
3\le m-1,
\]

hence

\[
\boxed{m\ge4.}
\]

At the minimum `m=4`, affine independence gives exactly a 3-simplex:

\[
\boxed{\Delta^3=\operatorname{conv}\{x_1,x_2,x_3,x_4\}.}
\]

Thus tetrahedrality follows from three-dimensionality plus minimal full-dimensional affine support.

## 2. Orientation-preserving symmetry bound

Any Euclidean symmetry of a nondegenerate tetrahedron permutes its four vertices faithfully. Therefore its full symmetry group embeds in `S_4`.

Fix an orientation of the affine 3-simplex. A vertex permutation preserves this orientation exactly when it is even. Hence the orientation-preserving Euclidean symmetry group `G^+` embeds in

\[
\boxed{A_4\subset S_4}
\]

and consequently

\[
\boxed{|G^+|\le12.}
\]

## 3. Maximal orientation-preserving symmetry forces regularity

Suppose the tetrahedral cell realizes the maximal possible orientation-preserving vertex symmetry:

\[
\boxed{|G^+|=12.}
\]

Then the faithful embedding gives

\[
G^+\cong A_4.
\]

The natural action of `A_4` on the six unordered vertex pairs is transitive. Each unordered pair is an edge of the tetrahedron. Because Euclidean symmetries preserve distance, all six edge lengths are therefore equal:

\[
\boxed{|x_i-x_j|=\ell\qquad(i\ne j).}
\]

A nondegenerate tetrahedron with all six edges equal is regular. Hence

\[
\boxed{
\text{minimal 3D simplex}
+
\text{maximal orientation-preserving vertex symmetry}
\Longrightarrow
\text{regular tetrahedron}.
}
\]

Conversely, the regular tetrahedron realizes the full rotational tetrahedral group

\[
\boxed{G^+\cong A_4,\qquad |G^+|=12,}
\]

so the bound is sharp.

## 4. Centered Gram geometry

Place the barycenter at the origin and normalize the four vertex directions:

\[
|n_a|=1,
\qquad
\sum_{a=1}^{4}n_a=0.
\]

Regularity makes every off-diagonal inner product equal to one constant `q`:

\[
n_a\cdot n_b=q\qquad(a\ne b).
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

Therefore

\[
\boxed{
n_a\cdot n_b=-\frac13\quad(a\ne b)
}
\]

and the Gram matrix is

\[
\boxed{
G=\frac43I_4-\frac13\mathbf1\mathbf1^T.
}
\]

The first and second moment identities follow:

\[
\boxed{\sum_a n_a=0,}
\]

\[
\boxed{\sum_a n_an_a^T=\frac43I_3.}
\]

Thus the earlier finite isotropy conditions are recovered as consequences of the maximally symmetric regular simplex rather than being required as the primary tetrahedron selector in this route.

## 5. A7 crosswalk

A7 states that the fundamental law is symmetry-governed. The exact theorem above isolates a narrow candidate inheritance rule for the primitive cell stage:

\[
\boxed{
\texttt{A7\_PRIMITIVE\_MINIMAL\_CELL\_SELECTS\_MAXIMAL\_AVAILABLE\_ORIENTATION\_PRESERVING\_SYMMETRY}.
}
\]

If that inheritance is admitted, then once the local carrier has dimension three and minimality selects `Delta^3`, A7 selects the regular tetrahedron by the maximal-symmetry theorem.

This is a sharper gate than separately assuming equal weights plus moment isotropy.

## 6. Group-theoretic bridge to the quantum carrier

The rotational symmetry group of the regular tetrahedron is

\[
A_4\subset SO(3).
\]

Under the double cover

\[
SU(2)\to SO(3),
\]

its inverse image is the binary tetrahedral group

\[
\boxed{2T\subset SU(2).}
\]

Thus the finite regular tetrahedral frame is compatible with the parent continuous `SU(2)/{\pm I}\cong SO(3)` carrier symmetry: the law-level carrier keeps full rotational symmetry, while a selected finite local frame has stabilizer `A_4` and lift `2T`.

## 7. Claim classes

| Statement | Class |
|---|---|
| a full-dimensional affine simplex in dimension 3 requires at least 4 vertices | EXACT AFFINE GEOMETRY |
| minimum 4 vertices gives `Delta^3` | EXACT |
| orientation-preserving tetrahedral symmetries embed in `A_4` | EXACT |
| therefore `|G^+| <= 12` | EXACT |
| saturation `|G^+|=12` makes the edge action transitive | EXACT GROUP THEORY |
| edge transitivity forces all six edge lengths equal | EXACT |
| all six equal edges give a regular tetrahedron | EXACT |
| centered normalized regular tetrahedron has pairwise dot product `-1/3` | EXACT |
| first/second moment isotropy follows from the regular tetrahedral Gram geometry | EXACT |
| A7 selects maximal available primitive-cell symmetry | TIR FOUNDATIONAL INHERITANCE GATE |
