# TIR CKM 600-cell Clean Noncommuting Family Pair Candidate v0.4

Status: `EXACT_REAL_NONCOMMUTING_PAIR / STAGE37_MECHANISM_REPAIR / COMPLEX_CP_OPERATOR_OPEN`

Date: 2026-09-14

## Purpose

Stage 37 proves that a pair of family operators obtained only as scalar
functions of one common normal family axis must commute and therefore cannot
produce nontrivial family misalignment or CP violation.

This surface constructs a second, genuinely noncommuting operator directly from
the clean 600-cell incidence geometry developed in v0.1-v0.3.  It uses no
observed CKM entry, no particle mass, and none of the quarantined heavy-family
orientation rows used by the historical Stage 35/36 mechanism test.

The result closes only the **real noncommuting-pair mechanism**.  A clean complex
orientation/holonomy lift remains open.

## 1. Canonical local three-label basis

Fix one 600-cell edge

\[
e=(u,v),
\]

with an ordering \(u<v\).  Any triangular face containing this edge has the
form

\[
f=(u,v,w).
\]

Order its three edge-star labels canonically as

\[
\mathcal B_f=(uv,uw,vw).
\]

For another face

\[
g=(u,v,z)
\]

around the same edge use

\[
\mathcal B_g=(uv,uz,vz).
\]

For any two edge labels \(p,q\), use the exact normalized 600-cell cell-star
overlap

\[
\Omega(p,q)
=\langle p_*|q_*\rangle
=\frac{|\operatorname{Star}(p)\cap\operatorname{Star}(q)|}{5}.
\]

The local cross-relation operator is the \(3\times3\) matrix

\[
M(f,g)_{ij}=\Omega((\mathcal B_f)_i,(\mathcal B_g)_j).
\]

## 2. Exactly two global relation matrices

The exhaustive 600-cell incidence enumeration gives exactly two classes for
pairs of different faces around one edge.

If \(f,g\) bound a common tetrahedral cell,

\[
\boxed{
M_A=
\begin{pmatrix}
1&2/5&2/5\\
2/5&2/5&1/5\\
2/5&1/5&2/5
\end{pmatrix}.
}
\]

If they are non-adjacent in the five-face edge link,

\[
\boxed{
M_N=
\begin{pmatrix}
1&2/5&2/5\\
2/5&0&0\\
2/5&0&0
\end{pmatrix}.
}
\]

The validator checks every local pair in the full coordinate 600-cell and
finds

\[
3600\quad M_A\text{ pairs},
\qquad
3600\quad M_N\text{ pairs},
\]

with no additional matrix pattern in the canonical endpoint-aligned basis.

Thus \(M_A\) and \(M_N\) are relation-class operators, not hand-picked example
matrices.

## 3. Exact noncommutation

Both matrices are real symmetric.  Their commutator is exactly

\[
\boxed{
[M_A,M_N]
=
\begin{pmatrix}
0&-6/25&-6/25\\
6/25&0&0\\
6/25&0&0
\end{pmatrix}
\neq0.
}
\]

Hence the adjacent and non-adjacent 600-cell transport classes cannot be scalar
functions of one common normal operator.

This directly supplies the kind of second geometric structure required by the
Stage 37 no-go theorem.

## 4. Positive-semidefinite Hermitian pair

If a PSD pair is desired, define

\[
H_A=M_A^2,
\qquad
H_N=M_N^2.
\]

Since \(M_A,M_N\) are real symmetric, both \(H_A,H_N\) are real symmetric
positive-semidefinite.  Nevertheless,

\[
\boxed{
[H_A,H_N]
=
\begin{pmatrix}
0&-48/125&-48/125\\
48/125&0&0\\
48/125&0&0
\end{pmatrix}
\neq0.
}
\]

Thus positivity does not remove the clean geometric misalignment.

The maximum absolute commutator entry is

\[
\boxed{\frac{48}{125}=0.384.}
\]

## 5. Relation to the A2 selector

Each face already carries the exact centered \(A_2\) weight plane from v0.2.
The two matrices above encode two inequivalent ways of relating such local
three-label carriers around the same five-face edge link.

In particular, the non-adjacent class contains the exact \(2/9\) principal
cosine used by the base \(12\) selector, while the full relation operator does
not commute with the adjacent class.

Therefore the base CKM selector no longer relies on one scalar family axis:
its incidence realization naturally contains distinct relative-geometry
operators.

## 6. What this repairs from Stage 35-37

Historical Stage 35 showed that a real noncommuting Hermitian pair can produce
family eigenframe misalignment, but its heavy-family source rows remained
quarantined.

Historical Stage 36 showed that a complex holonomy lift can produce nonzero
rephasing-invariant CP, but inherited the same source-provenance quarantine.

Stage 37 proved that replacing those rows by scalar functions of only one clean
family axis cannot work because the operators would commute.

The present 600-cell construction supplies, from clean incidence alone,

\[
\boxed{[H_A,H_N]\neq0.}
\]

Thus the Stage 37 structural obstruction is removed at the real mechanism
level without reviving the quarantined heavy-family ansatz.

## 7. Remaining CP gate

The pair \(H_A,H_N\) is real.  Consequently this surface does not claim a
nonzero Jarlskog invariant from the pair alone.

The next admissible gate is to add a **pre-existing, coefficient-free oriented
holonomy** from the Stella/spinorial/Berry layer to the clean incidence pair and
test all of the following fail-closed:

1. Hermiticity/positivity where required;
2. noncommutation survives;
3. the complex phase is not removable by row/column rephasing;
4. the resulting relative family unitary lies in \(SU(3)_F\);
5. its Jarlskog invariant is nonzero;
6. no CKM observable or fitted continuous coefficient enters the construction.

No such complex lift is promoted in this v0.4 surface.

## 8. Proof firewall

This result does not claim:

- a unique physical identification of \(H_A,H_N\) as up/down quark mass
  operators;
- a unique relative diagonalizer, since degeneracies remain in the real local
  relation operators;
- CP violation from the real pair;
- closure of the additive \(a\kappa\) refinement;
- physical realization of the 600-cell carrier.

It proves the narrower exact statement that clean 600-cell incidence supplies a
canonical pair of distinct real family-relation operators whose Hermitian PSD
squares do not commute.

Validator:

`TIR/validation/tir_ckm_600cell_clean_noncommuting_family_pair_candidate_v0_4.py`
