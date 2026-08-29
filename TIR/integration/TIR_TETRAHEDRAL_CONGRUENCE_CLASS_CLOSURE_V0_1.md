# TIR — Tetrahedral Congruence-Class Closure v0.1

Status: `EXACT_COMMON_GRAM_CLASS / ORTHOGONAL_CONGRUENCE_PASS / SHAPE_CROSSWALK_SOURCE_BINDING_PASS / SEMANTIC_ROLE_BINDING_SEPARATE`

## 1. Purpose

Two independent TIR routes produce a regular tetrahedral frame inside the same real Pauli/Bloch coefficient carrier

\[
\operatorname{Herm}_0(2)\simeq\mathbb R^3.
\]

The spatial route `TIR_MINIMAL_ISOTROPIC_TETRAHEDRAL_CELL_V0_1` derives a minimal equal-weight unit local relation frame from zero first moment and isotropic second moment. The quantum-information route `TIR_QUBIT_TETRAHEDRAL_INFORMATIONAL_COMPLETENESS_V0_1` uses the minimal symmetric informationally complete qubit frame.

Both routes yield

\[
\boxed{
\mathbf n_a\cdot\mathbf n_b=
\begin{cases}
1,&a=b,\\
-1/3,&a\ne b,
\end{cases}}
\]

with

\[
\sum_{a=1}^4\mathbf n_a=0,
\qquad
\sum_{a=1}^4\mathbf n_a\mathbf n_a^T=\frac43I_3.
\]

RF-S1/TIR PR #104 needs common dimensionless shape data. RF-S1 does not require the stronger semantic statement that an informational outcome label and a spatial adjacency label are literally the same physical role. TIR therefore isolates the exact geometric content required by the shape crosswalk.

## 2. Common Gram matrix

Let

\[
N=(\mathbf n_1\;\mathbf n_2\;\mathbf n_3\;\mathbf n_4)
\]

be an ordered spatial tetrahedral frame and

\[
M=(\mathbf m_1\;\mathbf m_2\;\mathbf m_3\;\mathbf m_4)
\]

an ordered SIC tetrahedral frame.

Both have the same Gram matrix

\[
\boxed{
G=N^TN=M^TM
=\frac43I_4-\frac13\mathbf1\mathbf1^T.
}
\]

Both also satisfy

\[
\boxed{NN^T=MM^T=\frac43I_3.}
\]

Hence both frames have rank three.

## 3. Explicit orthogonal congruence map

Define

\[
\boxed{
Q:=\frac34MN^T.
}
\]

Then

\[
QN
=\frac34MN^TN
=\frac34MG.
\]

Using

\[
MG=M(M^TM)=(MM^T)M=\frac43M,
\]

we obtain

\[
\boxed{QN=M.}
\]

Now

\[
QQ^T
=\frac9{16}MN^TNM^T
=\frac9{16}MGM^T.
\]

Since

\[
MGM^T=M(M^TM)M^T=(MM^T)^2=\frac{16}{9}I_3,
\]

it follows that

\[
\boxed{QQ^T=I_3.}
\]

Thus

\[
\boxed{Q\in O(3)}
\]

and the two tetrahedral frames are exactly congruent.

For fixed ordered spanning frames the linear map satisfying `QN=M` is unique. Therefore the common Gram data determine one orthogonal congruence between the two ordered realizations.

## 4. Orientation refinement

The orthogonal map has

\[
\det Q=\pm1.
\]

The tetrahedral vertex labels may be reordered by a permutation matrix `P`. An odd permutation reverses the oriented tetrahedral volume while preserving all pairwise inner products and all unoriented shape invariants.

Therefore, after choosing compatible orientation of the ordered frames, one may take

\[
\boxed{Q\in SO(3).}
\]

The TIR isotropy group already acts through the rotational carrier on `Herm_0(2)`. Hence the two tetrahedral constructions occupy the same rotational congruence class.

## 5. Exact common shape invariants

Every quantity used by the tetrahedral FS/spatial dual-shape crosswalk is invariant under orthogonal congruence:

\[
\|Q(\mathbf n_a-\mathbf n_b)\|
=\|\mathbf n_a-\mathbf n_b\|,
\]

\[
(Q\mathbf n_a)\cdot(Q\mathbf n_b)
=\mathbf n_a\cdot\mathbf n_b,
\]

and the absolute Euclidean tetrahedral volume is unchanged.

The Bloch central angle is determined only by the dot product,

\[
\cos\chi=-\frac13,
\]

so the qubit Fubini--Study geodesic edge lengths, spherical face angles and FS face areas are likewise fixed by the same Gram class.

Consequently the following dimensionless shape data belong to the common congruence class:

\[
\boxed{\hat a=\sqrt{\frac83}},
\]

\[
\boxed{\hat V_{\Delta^3}=\frac{8}{9\sqrt3}},
\]

\[
\boxed{a_{FS}^{face}=\frac\pi4},
\qquad
\boxed{a_{FS}^{tet}=\pi},
\]

and therefore

\[
\boxed{
C_{\Delta/FS}
=\frac{8}{9\sqrt3\pi}.
}
\]

The TIR PR #104 shape coefficient therefore depends only on the exact common Gram/congruence class and does not require literal identification of the two role label sets.

## 6. Canonical integer frame

Both routes admit the same representative of the congruence class,

\[
\frac1{\sqrt3}(1,1,1),
\quad
\frac1{\sqrt3}(1,-1,-1),
\]

\[
\frac1{\sqrt3}(-1,1,-1),
\quad
\frac1{\sqrt3}(-1,-1,1).
\]

Using this common representative is a gauge/coordinate choice inside the proven congruence class. Shape invariants computed from it are independent of that choice.

## 7. Crosswalk promotion

The geometric source chain is now

```text
TIR spatial minimal isotropy
 -> spatial tetra Gram G

TIR qubit minimal symmetric IC
 -> SIC tetra Gram G

same rank-3 Gram in Herm_0(2)
 -> explicit Q=(3/4) M N^T in O(3)
 -> common tetrahedral congruence class
 -> common orthogonal shape invariants
 -> TIR PR #104 C_Delta/FS
 -> RF-S1 scale-composition input
```

This closes the shape-class source requirement of the dual-shape coefficient.

## 8. Semantic and physical role ledger

The two constructions retain their typed roles:

```text
spatial relation frame     : local isotropic adjacency/direction carrier
SIC frame                  : minimal symmetric qubit information probe
common proven object       : tetrahedral Gram/congruence class in Herm_0(2)
common proven observables  : orthogonal shape invariants
```

A downstream physical model may bind the informational outcome roles to particular spatial adjacency roles. The shape crosswalk and RF-S1 coefficient already have the weaker exact congruence-class source they require.

## 9. Promotion status

```text
COMMON_GRAM_MATRIX                         PASS EXACT
RANK3_SPANNING                             PASS EXACT
EXPLICIT_ORTHOGONAL_CONGRUENCE             PASS EXACT
SO3_AFTER_ORIENTATION_CHOICE               PASS EXACT
COMMON_EDGE_VOLUME_FS_SHAPE_INVARIANTS     PASS EXACT
PR104_SHAPE_COEFFICIENT_SOURCE_CLASS       PASS EXACT
LITERAL_ROLE_LABEL_IDENTIFICATION          SEPARATE DOWNSTREAM BINDING
PHYSICAL_LENGTH_SCALE ell_s                OPEN CALIBRATION
PHASE_CLOCK_SCALE ell_phi                  IDT CALIBRATION LINE
```

Reference validator: `TIR/validation/tir_tetrahedral_congruence_class_closure_v0_1.py`.
