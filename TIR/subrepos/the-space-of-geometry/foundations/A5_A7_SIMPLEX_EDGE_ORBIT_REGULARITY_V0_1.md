# A5+A7 Simplex Edge-Orbit Regularity v0.1

Status: `EXACT_AXIOM_CROSSWALK_REGULAR_TETRAHEDRON_THEOREM_CANDIDATE`

Scope: close the regularity step for the minimal three-dimensional simplex using the intrinsic automorphism group of the abstract simplex, the geometric edge measure, and A7 law invariance.

## 1. Minimal cell

The canonical local relation carrier is

\[
V=\operatorname{Herm}_0(2)\cong\mathbb R^3.
\]

Minimal full-dimensional affine support therefore requires four vertices:

\[
\boxed{\Delta^3.}
\]

Let the abstract vertex set be

\[
\{1,2,3,4\}.
\]

The vertex names are bookkeeping labels; the intrinsic combinatorial object is the unlabeled 3-simplex.

## 2. Intrinsic automorphism group

Every permutation of the four vertices preserves the face structure of the abstract simplex. Therefore

\[
\boxed{
\operatorname{Aut}(\Delta^3)\cong S_4.
}
\]

The six edges are the unordered pairs

\[
E(\Delta^3)=\bigl\{\{i,j\}:1\le i<j\le4\bigr\}.
\]

The natural `S_4` action on this six-element edge set is transitive:

\[
\boxed{
\forall e,f\in E(\Delta^3),\ \exists\pi\in S_4:\ \pi(e)=f.
}
\]

Thus the primitive edge set is one intrinsic symmetry orbit.

## 3. A5 geometric edge measure

For a realized edge relation

\[
\mathcal E_{ij}\in V,
\]

the invariant positive quadratic measure is

\[
\boxed{
q_{ij}:=rac12\operatorname{Tr}(\mathcal E_{ij}^2).
}
\]

A5 types arithmetic invariants of this form as geometric measures. Define the edge length by

\[
\boxed{
\ell_{ij}:=\sqrt{q_{ij}}.
}
\]

## 4. A7 symmetry on the edge-measure law

A7 requires the primitive geometric law to be symmetry-governed. Applied to the intrinsic simplex automorphism action, the scalar edge-measure law satisfies

\[
\boxed{
q_{\pi(i)\pi(j)}=q_{ij}
\qquad
\forall\pi\in\operatorname{Aut}(\Delta^3).
}
\]

Because the six edges form one `S_4` orbit, invariance immediately gives one common value

\[
\boxed{
q_{ij}=q_*>0
\qquad(i\ne j).
}
\]

Therefore

\[
\boxed{
\ell_{ij}=\ell_*
\qquad(i\ne j).
}
\]

All six edge lengths of the realized 3-simplex are equal.

## 5. Regularity theorem

A nondegenerate Euclidean tetrahedron with all six edge lengths equal is regular. Hence

\[
\boxed{
\mathbb R^3
\to
\Delta^3
\xrightarrow{A5+A7\ \text{edge-orbit invariance}}
\text{regular tetrahedron}.
}
\]

The regularity step no longer needs a separate maximal-symmetry condition or a separate moment-isotropy assumption.

## 6. Centered Gram geometry

Place the barycenter at the origin and normalize the four center-to-vertex directions:

\[
|n_a|=1,
\qquad
\sum_{a=1}^{4}n_a=0.
\]

Regularity makes the off-diagonal inner product constant:

\[
n_a\cdot n_b=q\qquad(a\ne b).
\]

Then

\[
0
=\left|\sum_a n_a\right|^2
=4+12q,
\]

so

\[
\boxed{
q=-\frac13.
}
\]

Therefore

\[
\boxed{
n_a\cdot n_b=-\frac13\quad(a\ne b),
}
\]

\[
\boxed{
G=\frac43I_4-\frac13\mathbf1\mathbf1^T,
}
\]

and

\[
\boxed{
\sum_an_an_a^T=\frac43I_3.
}
\]

Thus the finite moment-isotropy identities are consequences of the A5+A7 edge-orbit regularity route.

## 7. Orientation and quantum lift

For scalar edge regularity the full abstract group `S_4` is the relevant automorphism group. Once an orientation is fixed, the orientation-preserving subgroup is

\[
A_4\subset S_4.
\]

Its Euclidean rotational realization is

\[
A_4\subset SO(3),
\]

and its inverse image under the `SU(2)` double cover is the binary tetrahedral group

\[
\boxed{2T\subset SU(2).}
\]

This preserves the distinction between scalar edge-law symmetry and oriented rotational frame symmetry.

## 8. Dependency result

The local tetrahedral regularity chain is now

\[
\boxed{
\operatorname{Herm}_0(2)\cong\mathbb R^3
\to
\Delta^3
\to
\operatorname{Aut}(\Delta^3)=S_4
\xrightarrow{A5+A7}
\ell_{ij}=\ell_*
\to
\text{regular tetrahedron}.
}
\]

This uses the existing A5 arithmetic-measure role and A7 law-invariance role directly on the intrinsic automorphism group of the minimal simplex.

## 9. Claim classes

| Statement | Class |
|---|---|
| `Aut(Delta^3) ~= S4` | EXACT COMBINATORICS |
| `S4` acts transitively on the six edges | EXACT GROUP THEORY |
| `q_ij=Tr(E_ij^2)/2` is a positive invariant edge measure | EXACT GIVEN THE ESTABLISHED CARRIER METRIC |
| A5 types `q_ij` as geometric arithmetic measure | AXIOM CROSSWALK |
| A7 requires the edge-measure law to be invariant on the intrinsic simplex symmetry orbit | AXIOM CROSSWALK |
| orbit invariance makes all six edge measures equal | EXACT |
| all six equal edge lengths imply regular tetrahedron | EXACT |
| regular tetrahedron gives pairwise centered dot product `-1/3` | EXACT |
| second moment `(4/3)I3` follows | EXACT |
