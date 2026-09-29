# TIR Stella Alternating-Rotation Inference v0.1

Status: EXACT_RELABELING_INVARIANT_RELATIONAL_SIGNATURE / ALTERNATING_TRANSFORM_LIFT / PRESPACETIME_ONLY

Date: 2026-09-28

## 1. Purpose

This note refines the pre-spacetime Stella half-step construction. The carrier is the abstract/internal Stella Octangula relation

\[
\mathcal S_\star=T_4^+\cup T_4^-,
\]

but neither the containing sphere nor the tetrahedral coordinates are identified here with already-existing physical space. They are a representation of a relational Gram/symmetry structure.

Likewise, repeated transformations are not motion in an already-existing time. They are composable operations from which serial order may later be extracted.

The new statement is that the inference-bearing object can be the relative transformation orbit of the two tetrahedral sectors rather than a static assignment of named vertices.

## 2. Reference tetrahedral carrier

Use the standard centered tetrahedral vectors

\[
n_1=\frac{(1,1,1)}{\sqrt3},\quad
n_2=\frac{(1,-1,-1)}{\sqrt3},
\]

\[
n_3=\frac{(-1,1,-1)}{\sqrt3},\quad
n_4=\frac{(-1,-1,1)}{\sqrt3}.
\]

Then

\[
n_i\cdot n_j=
\begin{cases}
1,&i=j,\\
-1/3,&i\ne j.
\end{cases}
\]

The antipodal sector is \(-T_4\).

The orientation-preserving rotational symmetry group of one regular tetrahedron is

\[
\boxed{A_4\subset SO(3),\qquad |A_4|=12.}
\]

Arbitrary names attached to the four vertices are bookkeeping. Relabeling does not define a new relational state.

## 3. Two orientation lifts and label gauge

Let

\[
A,B\in SO(3)
\]

be orientation lifts for the plus and minus tetrahedral sectors. Their vertices are

\[
p_i=A n_i,\qquad m_j=-B n_j.
\]

Define the cross-sector overlap matrix

\[
\boxed{
C_{ij}(A,B)=p_i\cdot m_j
=-n_i^{T}A^{T}B n_j.
}
\]

Changing the tetrahedral reference labels by

\[
a,b\in A_4
\]

sends

\[
A\mapsto Aa,\qquad B\mapsto Bb.
\]

This only permutes the rows and columns of \(C\). Therefore the unordered multiset

\[
\boxed{
\mathcal I(A,B)
=
\{\!\{C_{ij}(A,B):1\le i,j\le4\}\!\}
}
\]

is exactly invariant under independent tetrahedral relabelings:

\[
\boxed{
\mathcal I(Aa,Bb)=\mathcal I(A,B)
\qquad
\forall a,b\in A_4.
}
\]

This is the label-free relational inference signature.

The stronger full relative configuration may be represented as the corresponding double-coset class. The overlap multiset is a concrete invariant readout; completeness of this invariant for every possible relative orientation is not claimed.

## 4. Alternating transformation rather than static vertex identity

Extend the pretemporal carrier to

\[
\widetilde{\mathcal X}
=
\mathbb N_0\times\mathbb Z_2\times SO(3)\times SO(3).
\]

Write a lifted state as

\[
X=(n,\sigma,A,B).
\]

Choose two admitted orientation transformations

\[
R_+,R_-\in SO(3).
\]

They are transformation operators, not functions of a pre-existing time variable.

Define the alternating half-step

\[
\boxed{
\widetilde H(n,0,A,B)
=
(n,1,R_+A,B),
}
\]

\[
\boxed{
\widetilde H(n,1,A,B)
=
(n+1,0,A,R_-B).
}
\]

Thus one application transforms only one tetrahedral sector; the next application transforms the complementary sector.

Define the decorated full successor

\[
\boxed{
\widetilde S(n,\sigma,A,B)
=
(n+1,\sigma,R_+A,R_-B).
}
\]

Because the two half-operations act on different orientation slots,

\[
\boxed{
\widetilde H^2=\widetilde S.
}
\]

Projection to \((n,\sigma)\) recovers the earlier exact IDT/TIR relation

\[
H^2=S.
\]

## 5. Inference orbit

After each half-step evaluate

\[
\mathcal I_k=\mathcal I(A_k,B_k).
\]

The pretemporal inference record is therefore

\[
\boxed{
\mathcal I_0
\to
\mathcal I_1
\to
\mathcal I_2
\to\cdots
}
\]

together with the alternating sector parity.

Information is not tied to the statement "vertex 1 is this pole". The invariant content is carried by how the relational overlap class changes under the alternating transformation sequence.

Hence the intended structural reading is

\[
\boxed{
\text{static labelled vertices}
\;\longrightarrow\;
\text{gauge-equivalent labels},
}
\]

\[
\boxed{
\text{inference}
=
\text{relational transformation orbit}.
}
\]

## 6. Connection to the half-step/Hilbert chain

The projection of the decorated orbit onto the successor skeleton gives

\[
\frac12,1,\frac32,2,\ldots
\]

only as the normalized pretemporal grade of successive applications of \(H\).

The coarse relational chain remains

\[
\boxed{
1\,|\,12\,|\,23\,|\,34\,|\,45\,|\cdots
}
\]

with

\[
E_n=\{n,n+1\},
\qquad
E_n\cap E_{n+1}=\{n+1\}.
\]

The Hilbert unilateral shift

\[
S_{\mathbb N}:n\mapsto n+1
\]

moves the entire chain while preserving this incidence rule. The alternating Stella operator is therefore a two-sector decorated square root of the successor structure.

## 7. Pre-spacetime split

This construction deliberately precedes physical spacetime.

Temporal route:

\[
\boxed{
\text{relation}
\to
\text{alternating transformation}
\to
\text{successor/order}
\to
\text{IDT duration and clock calibration}.
}
\]

Spatial route:

\[
\boxed{
\text{relation}
\to
\text{incidence / Gram structure}
\to
\text{geometric realization}
\to
\text{physical space binding}.
}
\]

The abstract sphere/tetrahedron is therefore a state/symmetry representation at this layer, not an already physical three-space.

## 8. Exact claims and firewall

| Statement | Status |
|---|---|
| tetrahedral orientation-preserving symmetry is \(A_4\) of order 12 | EXACT |
| \(C_{ij}=-n_i^TA^TBn_j\) | EXACT DEFINITION |
| \(\mathcal I(Aa,Bb)=\mathcal I(A,B)\) for \(a,b\in A_4\) | EXACT |
| one half-step transforms exactly one tetrahedral sector | EXACT DEFINITION |
| \(\widetilde H^2=\widetilde S\) | EXACT |
| projection recovers \(H^2=S\) | EXACT |
| inference can be represented by the label-free signature orbit | EXACT CONSTRUCTION |
| overlap multiset is a complete invariant for all relative orientations | NOT CLAIMED |
| physical time is assumed | FALSE |
| physical space is assumed | FALSE |
| particle-physics supersymmetry is proved or required | NOT CLAIMED |

Reference validator:

TIR/validation/tir_stella_alternating_rotation_inference_v0_1.py
