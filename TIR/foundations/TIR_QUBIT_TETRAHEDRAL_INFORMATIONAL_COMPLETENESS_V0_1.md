# TIR Qubit Tetrahedral Informational Completeness v0.1

Status: `EXACT_QUANTUM_INFORMATION_CONVERGENCE_CANDIDATE`

Scope: TIR-only independent route from the first binary quantum carrier to the same regular tetrahedral structure obtained by the minimal local-isotropy theorem. This route uses informational completeness of a qubit rather than spatial assumptions.

## 1. Binary quantum state

For the primitive two-state carrier

\[
\mathcal H_2\cong\mathbb C^2,
\]

every density operator has Bloch form

\[
\boxed{
\rho=\frac12(I+\mathbf r\cdot\boldsymbol\sigma),
\qquad |\mathbf r|\le1.
}
\]

Because `Tr(rho)=1`, the state contains three independent real Bloch coordinates.

## 2. Lower bound on informationally complete outcomes

A normalized measurement with `m` outcome probabilities

\[
p_1,\ldots,p_m,
\qquad
\sum_a p_a=1
\]

contains at most `m-1` independent real numbers.

To recover all three real Bloch coordinates of a generic qubit state, informational completeness therefore requires

\[
m-1\ge3.
\]

Hence

\[
\boxed{m\ge4.}
\]

So four is the minimum possible number of outcomes of an informationally complete qubit measurement.

## 3. Tetrahedral Bloch directions

Let four unit Bloch vectors satisfy

\[
\sum_{a=1}^{4}\mathbf n_a=0
\]

and

\[
\mathbf n_a\cdot\mathbf n_b=-\frac13
\qquad(a\ne b).
\]

These are the vertices of a regular tetrahedron on `S^2`.

Define rank-one projectors

\[
P_a=\frac12(I+\mathbf n_a\cdot\boldsymbol\sigma)
\]

and POVM elements

\[
\boxed{
E_a=\frac12P_a
=\frac14(I+\mathbf n_a\cdot\boldsymbol\sigma).
}
\]

Because the tetrahedral vectors sum to zero,

\[
\sum_{a=1}^{4}E_a=I.
\]

Thus `{E_a}` is a valid four-outcome qubit POVM.

## 4. Symmetric overlap

For `a != b`,

\[
\operatorname{Tr}(P_aP_b)
=\frac12(1+\mathbf n_a\cdot\mathbf n_b)
\]

and therefore

\[
\boxed{
\operatorname{Tr}(P_aP_b)=\frac13.
}
\]

All distinct pairs have the same overlap. This is the tetrahedral qubit SIC structure.

## 5. Exact reconstruction of the Bloch vector

The measurement probability is

\[
\boxed{
p_a=\operatorname{Tr}(\rho E_a)
=\frac14(1+\mathbf r\cdot\mathbf n_a).
}
\]

The tetrahedral second moment is

\[
\sum_{a=1}^{4}\mathbf n_a\mathbf n_a^T
=\frac43I_3.
\]

Hence

\[
\sum_a p_a\mathbf n_a
=\frac14\sum_a\mathbf n_a
+\frac14\sum_a(\mathbf r\cdot\mathbf n_a)\mathbf n_a
=\frac13\mathbf r.
\]

Therefore

\[
\boxed{
\mathbf r
=3\sum_{a=1}^{4}p_a\mathbf n_a.
}
\]

All three independent real parameters of the qubit state are recovered from the four tetrahedral probabilities.

The measurement is therefore informationally complete and saturates the lower bound `m=4`.

## 6. Independent convergence with the spatial theorem

The spatial-isotropy route produced the same tetrahedron from

```text
zero first moment
+ isotropic second moment
+ equal weights
+ minimal finite valence
```

The quantum-information route produces it from

```text
binary quantum carrier C^2
+ symmetric rank-one outcomes
+ informational completeness
+ minimal outcome count
```

Thus two independently typed requirements converge:

\[
\boxed{
\begin{array}{c}
\text{minimal finite local isotropy}\
\downarrow
\end{array}
\quad
\text{REGULAR TETRAHEDRON}
\quad
\begin{array}{c}
\uparrow\\
\text{minimal symmetric qubit informational completeness}
\end{array}
}
\]

This convergence occurs inside the same Bloch/generator coefficient space `Herm_0(2) ~= R^3`.

## 7. TIR significance

A3 assigns foundational status to informational relations. The present result gives a precise candidate reason that the tetrahedral local cell is more than a convenient spatial discretization: it is also the minimal symmetric finite probe carrying complete information about a local binary quantum state.

The resulting candidate bridge is

\[
\boxed{
\text{FIRST DISTINCTION}
\to
\mathbb C^2
\to
\text{3 real Bloch parameters}
\to
4\text{ minimal IC outcomes}
\to
\text{tetrahedral symmetry}.
}
\]

Its promotion from informational probe geometry to physical spatial adjacency remains separately typed.

## 8. Claim classes

| Statement | TIR class |
|---|---|
| normalized qubit state has three independent real Bloch parameters | STANDARD EXACT |
| an `m`-outcome normalized probability vector has at most `m-1` independent reals | EXACT |
| qubit informational completeness requires `m>=4` | EXACT DIMENSION LOWER BOUND |
| tetrahedral `E_a=(I+n_a.sigma)/4` sum to identity | EXACT |
| pairwise projector overlap is `1/3` | EXACT |
| tetrahedral probabilities reconstruct `r=3 sum p_a n_a` | EXACT |
| four tetrahedral outcomes are minimal symmetric informationally complete qubit data | STANDARD/EXACT QUANTUM-INFORMATION STRUCTURE |
| tetrahedral informational probe equals physical spatial cell | TIR PROMOTION/CROSSLINK GATE |

## 9. Next gate

The new question is whether A3, A4 and A7 jointly select the same tetrahedral object as both

\[
\boxed{
\text{minimal complete information cell}
}
\]

and

\[
\boxed{
\text{minimal isotropic spatial relation cell}.
}
\]

If that identification can be derived rather than declared, the Bloch-to-space promotion gate becomes substantially narrower.