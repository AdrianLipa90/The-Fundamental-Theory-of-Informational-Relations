# TIR Tetrahedral Edge <-> Bivector Axis Binding v0.1

Status: EXACT_COMBINATORIAL_BINDING / REPRESENTATION_CROSSWALK / PHYSICAL_EDGE_CARRIER_BINDING_OPEN
Date: 2026-09-24

## 1. Purpose

The preceding moire/bivector bridge used the ordered six-element basis

\[
(01,02,03,23,31,12)
\]

for \(\Lambda^2(\mathbb R^4)\), while TIR independently carries a regular tetrahedral relational cell with four vertices and six edges.

This file proves the exact combinatorial relation between those two six-element index systems without identifying their physical meanings.

## 2. Six tetrahedral edges

For labeled tetrahedron vertices

\[
V=\{0,1,2,3\},
\]

the unordered edge set is

\[
E(T_4)=\bigl\{\{i,j\}:0\le i<j\le3\bigr\},
\]

so

\[
|E(T_4)|=\binom42=6.
\]

Choose the oriented representative basis

\[
\boxed{
\mathcal E=(01,02,03,23,31,12).
}
\]

The orientation on 31 rather than 13 is chosen so that the complementary-edge pairing has the standard positive block form below.

## 3. Opposite edges and the wedge pairing

Each tetrahedral edge has a unique disjoint/opposite edge:

\[
01\leftrightarrow23,
\qquad
02\leftrightarrow31,
\qquad
03\leftrightarrow12.
\]

In the basis \(\mathcal E\), the incidence matrix of this complementary-edge involution is exactly

\[
\boxed{
J=
\begin{pmatrix}
0&I_3\\
I_3&0
\end{pmatrix}.
}
\]

This is the same numeric matrix that represents the oriented wedge pairing on the bivector basis of \(\Lambda^2(\mathbb R^4)\).

The statement is an exact **index/combinatorial crosswalk**:

\[
\text{opposite tetrahedron edge pairing}
\longleftrightarrow
\text{complementary bivector index pairing}.
\]

It is not a claim that a physical tetrahedral edge literally is a spacetime bivector.

## 4. S4 covariance

A permutation \(p\in S_4\) of the tetrahedron vertices induces a signed permutation matrix

\[
C_2(p)
\]

on the six oriented pair indices.

For all 24 elements,

\[
\boxed{
C_2(p)^TJC_2(p)=\operatorname{sgn}(p)J.
}
\]

Therefore:

- the 12 even permutations \(A_4\) preserve the oriented pairing \(J\);
- the 12 odd permutations reverse the orientation and send \(J\mapsto-J\).

The validator exhaustively checks all 24 cases.

## 5. Natural 36-channel carrier

Two six-edge relational sheets, for example the two oppositely oriented tetrahedral families in the Stella-Octangula candidate, have the Cartesian edge-pair set

\[
E(T_4^+)\times E(T_4^-).
\]

Hence

\[
\boxed{
6\times6=36
}
\]

relation channels arise without reshaping an anonymous 36-vector.

A candidate channel is indexed by

\[
(a,b)\in E(T_4^+)\times E(T_4^-).
\]

Its scalar/operator value must be supplied by an explicit relational observable such as a declared phase difference, overlap, holonomy or transport coefficient. The present gate proves the **axis labels**, not the value law.

## 6. PhaseNav legacy firewall

The current canonical PhaseNav runtime exposes coordinates named only

\[
\phi_0,\ldots,\phi_{35}.
\]

Its legacy phase generator is not constructed as six tetrahedral edges times six tetrahedral edges; it uses the existing Metatime/Collatz index law and a seven-periodic term through \(i\bmod L_3\) with \(L_3=7\).

Therefore

\[
\boxed{
\text{legacy Phase36 row-major reshape}
\neq
\text{derived tetra-bivector axis binding}.
}
\]

Any existing 6x6 reshape of legacy Phase36 is a computational view only.

The physically cleaner candidate route is instead

\[
(T_4^+,T_4^-)
\to
E_+\times E_-
\to
X_{ab}
\to
\operatorname{Mat}_6
\to
\mathfrak{co}(3,3)\oplus\mathcal Q
\to
\mathfrak{gl}(4).
\]

## 7. Remaining gate

The remaining unresolved map is now narrower:

\[
\boxed{
(E_a^+,E_b^-)
\longrightarrow
X_{ab}.
}
\]

The relation observable must be fixed before looking at downstream gravity performance. Post-data selection among phase/overlap/holonomy formulas is forbidden for promotion.

## 8. Promotion ledger

- tetrahedron edge count = 6: PASS EXACT
- complementary/opposite edge pairs = 3: PASS EXACT
- complementary-edge matrix equals numeric J: PASS EXACT
- all S4 induced pair actions satisfy C2(p)^T J C2(p)=sgn(p)J: PASS EXACT
- A4 preserves J: PASS EXACT
- odd S4 reverses J orientation: PASS EXACT
- two six-edge sheets give 36 pair channels: PASS EXACT COMBINATORIAL
- legacy Phase36 coordinates are natively tetra-edge x tetra-edge: FAIL / NOT DERIVED
- tetra-edge relation observable X_ab: OPEN
- physical spacetime bivector interpretation: OPEN


## 9. Pre-registered edge-pair relation observable

The relation-value law is fixed before any physical edge-carrier dataset is admitted.

For two PhaseNav 36D edge carriers \(E_a^+\) and \(E_b^-\), use the pre-existing canonical complex overlap

\[
Z_{ab}
=
\frac1{36}
\sum_{k=0}^{35}
e^{i(\phi^-_{b,k}-\phi^+_{a,k})}.
\]

Define

\[
\boxed{
X_{ab}=\arg Z_{ab},
\qquad
R_{ab}=|Z_{ab}|.
}
\]

No fitted coefficient is introduced. A common U(1) shift of both sheets cancels. Exact zero overlap fails closed because its argument is undefined.

This closes the representation-level map

\[
(E_a^+,E_b^-)
\to
(X_{ab},R_{ab})
\]

**provided the edge carriers themselves are already admissible**.

The remaining source gate is therefore

\[
\boxed{
T_4^\pm\ \text{geometry}
\longrightarrow
\{E_a^\pm\}_{a=1}^{6}
\subset T^{36}.
}
\]

Hashing edge labels into legacy PhaseNav IDs is explicitly forbidden as a physical derivation, because that would import arbitrary semantic coordinates rather than derive the carriers from tetrahedral/Bloch geometry.

Updated statuses:

- TETRA_EDGE_PAIR_RELATION_OBSERVABLE = PASS_DEFINITION
- COMMON_SHIFT_INVARIANCE = PASS
- EDGE_OVERLAP_ZERO_FAIL_CLOSED = PASS_DESIGN
- TETRA_GEOMETRY_TO_SIX_PHASE36_EDGE_CARRIERS = OPEN
- LABEL_HASH_AS_PHYSICAL_EDGE_BINDING = FORBIDDEN


## 10. Supersession note: edge labels are now generated by the null-frame lift

The exact pair-index result of this file remains valid, but the previously open requirement to supply six independent Phase36 edge carriers is no longer necessary for the gravity branch.

`TIR_TETRA_NULL_FRAME_BIVECTOR_MOIRE_V0_1` constructs four tetrahedral null rays as a full four-frame \(E\). Their six pairwise wedges are exactly

\[
C_2(E),
\]

so the six edge carriers are generated by the frame itself.

The canonical PhaseNav overlap observable defined here remains available for other typed edge-carrier experiments, but it is not used as the foundational gravity decoder.
