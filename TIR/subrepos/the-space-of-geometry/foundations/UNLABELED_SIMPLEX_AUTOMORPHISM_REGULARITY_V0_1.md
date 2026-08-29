# Unlabeled 3-Simplex Automorphism Regularity v0.1

Status: `EXACT_CONDITIONAL_UNLABELED_SIMPLEX_REGULARITY_THEOREM_CANDIDATE`

Scope: replace the stronger maximal-symmetry wording by a sharper combinatorial-to-metric theorem. The primitive minimal 3-simplex has a canonical abstract automorphism group. If the orientation-preserving part of that intrinsic symmetry is faithfully realized by local isometries, regular tetrahedral geometry follows.

## 1. Abstract minimal 3-simplex

Once the local relation carrier has affine dimension three, minimal full-dimensional support requires four affinely independent vertices:

\[
\Delta^3=\{1,2,3,4\}
\]

with every nonempty vertex subset defining a face of the abstract simplex.

No vertex label belongs to the abstract simplex structure itself. Therefore every permutation of its four vertices is a combinatorial automorphism:

\[
\boxed{\operatorname{Aut}(\Delta^3)\cong S_4.}
\]

If an orientation is fixed, the orientation-preserving combinatorial automorphisms are the even permutations:

\[
\boxed{\operatorname{Aut}^+(\Delta^3)\cong A_4.}
\]

## 2. Faithful geometric realization condition

Let

\[
x_1,x_2,x_3,x_4\in E^3
\]

be a nondegenerate Euclidean realization of the abstract simplex.

Define **automorphism-faithful isometric realization** by the condition that for every

\[
\pi\in A_4
\]

there exists an orientation-preserving Euclidean isometry `g_pi` satisfying

\[
\boxed{g_\pi(x_i)=x_{\pi(i)}.}
\]

This is a precise bridge condition between intrinsic combinatorial symmetry and metric symmetry.

## 3. A4 is transitive on edges

The six simplex edges are the unordered pairs

\[
\{i,j\},\qquad i\ne j.
\]

The natural action of `A_4` on these six unordered pairs is transitive. Therefore, for any two edges

\[
\{i,j\},\qquad\{k,l\},
\]

there exists

\[
\pi\in A_4
\]

with

\[
\pi\{i,j\}=\{k,l\}.
\]

Under automorphism-faithful isometric realization,

\[
|x_i-x_j|
=
|g_\pi x_i-g_\pi x_j|
=
|x_k-x_l|.
\]

Hence all six edge lengths coincide:

\[
\boxed{|x_i-x_j|=\ell\quad(i\ne j).}
\]

Therefore the realization is a regular tetrahedron.

## 4. Exact theorem

### Theorem — unlabeled simplex symmetry forces regularity

A nondegenerate Euclidean realization of an abstract oriented 3-simplex is regular if its intrinsic orientation-preserving automorphism group

\[
A_4=\operatorname{Aut}^+(\Delta^3)
\]

is faithfully realized by orientation-preserving Euclidean isometries.

Thus

\[
\boxed{
\Delta^3
+
\text{faithful isometric realization of }\operatorname{Aut}^+(\Delta^3)
\Longrightarrow
\text{regular tetrahedron}.
}
\]

Conversely, the regular tetrahedron realizes exactly this rotational symmetry group.

## 5. Gram and moment consequences

With barycenter at the origin and normalized vertex directions `n_a`, regularity gives

\[
\sum_{a=1}^4n_a=0
\]

and equal off-diagonal inner product `q`. Therefore

\[
0
=\left|\sum_a n_a\right|^2
=4+12q,
\]

so

\[
\boxed{n_a\cdot n_b=-\frac13\quad(a\ne b).}
\]

The Gram matrix is

\[
\boxed{G=\frac43I_4-\frac13\mathbf1\mathbf1^T}
\]

and

\[
\boxed{\sum_a n_an_a^T=\frac43I_3.}
\]

The finite first/second moment isotropy identities therefore follow from the intrinsic simplex-automorphism realization.

## 6. TIR crosswalk

This route uses two already isolated TIR principles more directly than a separate maximal-symmetry assumption:

- A3: primitive relational distinctions are preserved rather than collapsed by the realization;
- A7: the primitive relational law is symmetry-governed.

For the source-minimal unlabeled simplex, the intrinsic symmetry available before metric decoration is `S_4`, with orientation-preserving part `A_4`.

The remaining TIR inheritance condition can therefore be stated narrowly as

\[
\boxed{
\texttt{A3+A7\_FAITHFULLY\_REALIZE\_INTRINSIC\_ORIENTED\_SIMPLEX\_AUTOMORPHISMS\_ISOMETRICALLY}.
}
\]

Under that condition, regularity is exact and no independent equal-edge or moment-isotropy postulate is required.

## 7. Quantum symmetry compatibility

The regular tetrahedral rotation group sits naturally inside the parent carrier symmetry:

\[
A_4\subset SO(3)\cong PSU(2).
\]

Its inverse image under the double cover is

\[
\boxed{2T\subset SU(2),}
\]

the binary tetrahedral group.

Thus the finite primitive frame is compatible with the continuous parent rotational carrier while retaining its own intrinsic discrete stabilizer.

## 8. Claim classes

| Statement | Class |
|---|---|
| `Aut(Delta^3) ~= S4` | EXACT COMBINATORICS |
| oriented automorphism subgroup is `A4` | EXACT |
| `A4` acts transitively on the six simplex edges | EXACT GROUP THEORY |
| faithful isometric realization of `A4` makes all six edge lengths equal | EXACT |
| equal six edge lengths imply regular tetrahedron | EXACT |
| regularity gives pairwise normalized dot product `-1/3` | EXACT |
| regularity gives second moment `(4/3) I3` | EXACT |
| A3+A7 select faithful isometric realization of intrinsic simplex automorphisms | TIR FOUNDATIONAL INHERITANCE GATE |
