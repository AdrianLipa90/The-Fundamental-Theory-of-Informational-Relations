# TIR CKM 600-cell A2 Selector Bridge Candidate v0.2

Status: `EXACT_LOCAL_A2_GEOMETRY / EXACT_B_C_OPERATOR_READOUTS / MIXING_WEIGHT_OPERATOR_REALIZATION / UNIQUE_FLAVOUR_SELECTOR_OPEN`

Date: 2026-09-14

Supersedes only the mathematical working surface of
`TIR_CKM_600CELL_FLAG_INCIDENCE_CANDIDATE_V0_1.md`; the v0.1 receipt remains
valid provenance.

## 1. Input already closed by v0.1

The executable 600-cell coordinate carrier gives exactly

\[
|V|=120,\qquad |E|=720,\qquad |F|=1200,\qquad |C|=600,
\]

with uniform tetrahedral incidences

\[
\nu_F=|\operatorname{Star}(f)|=2,
\qquad
\nu_E=|\operatorname{Star}(e)|=5.
\]

For every edge define the normalized cell-star state

\[
|e_*\rangle=\frac1{\sqrt5}\sum_{T\supset e}|T\rangle
\in\ell^2(C).
\]

If two distinct edges belong to one triangular face, then

\[
\langle e_*|e'_*\rangle=\frac25.
\]

The v0.1 validator checks this for all 3600 such edge pairs.

## 2. One face generates an exact A2 carrier

Let a triangular face have edges \(e_1,e_2,e_3\) and define

\[
|x_i\rangle:=|e_i{}_ *\rangle.
\]

Their Gram matrix is

\[
\boxed{
G_F=
\begin{pmatrix}
1&2/5&2/5\\
2/5&1&2/5\\
2/5&2/5&1
\end{pmatrix}.
}
\]

Let

\[
|\mu\rangle=\frac13(|x_1\rangle+|x_2\rangle+|x_3\rangle),
\qquad
|y_i\rangle=|x_i\rangle-|\mu\rangle.
\]

Then exactly

\[
\langle\mu|\mu\rangle=\frac35,
\]

\[
\langle y_i|y_i\rangle=\frac25,
\qquad
\langle y_i|y_j\rangle=-\frac15\quad(i\ne j),
\]

and

\[
\sum_i|y_i\rangle=0.
\]

Therefore the normalized vectors

\[
|\widehat y_i\rangle=\sqrt{\frac52}|y_i\rangle
\]

satisfy

\[
\boxed{
\langle\widehat y_i|\widehat y_j\rangle=-\frac12
\quad(i\ne j).
}
\]

Thus every triangular face canonically supplies the regular three-weight
configuration of the \(A_2\) plane.  Permuting the three edges acts by the Weyl
group \(S_3\).  This is an exact local geometric carrier for three labelled
channels up to Weyl permutation; no CKM data are used.

The orthogonal decomposition is

\[
\operatorname{span}\{x_1,x_2,x_3\}
=\mathbf 1\oplus A_2,
\]

where the centroid is the one-dimensional symmetric mode and the centered
subspace is two-dimensional.

## 3. The five-face ring around an edge

Every 600-cell edge belongs to five triangular faces.  Those five faces form a
cyclic local link.  For each face \(f\), let \(W_f\subset\ell^2(C)\) be its
centered \(A_2\) plane from Section 2.

For two different faces \(f,g\) containing the same edge there are exactly two
combinatorial relation classes.

### 3.1 Adjacent ring faces

If \(f\) and \(g\) are faces of a common tetrahedral cell, the two principal
cosines between \(W_f\) and \(W_g\) are

\[
\boxed{
\left\{\frac59,\frac13\right\}.
}
\]

### 3.2 Non-adjacent ring faces

If \(f\) and \(g\) contain the same edge but do not bound one tetrahedral cell,
the principal cosines are

\[
\boxed{
\left\{\frac29,0\right\}.
}
\]

The validator exhaustively checks all 720 edge links.  Across the full
600-cell it finds

\[
3600
\]

adjacent-ring face pairs and

\[
3600
\]

non-adjacent-ring face pairs, with no third principal-angle class.

Hence the CKM base quantity

\[
\boxed{b=\frac29}
\]

has a direct operator-geometric realization: it is the unique nonzero
principal cosine for non-adjacent local \(A_2\) planes around one 600-cell
edge.

This is stronger than merely recovering \(2/9\) as a cardinality ratio.

## 4. Exact derivation of the principal cosines

Choose, on each face, the orthonormal basis

\[
q_1=\frac{x_1-x_2}{\sqrt{6/5}},
\qquad
q_2=\frac{x_1+x_2-2x_3}{\sqrt{18/5}}.
\]

For adjacent ring faces the centered-frame cross Gram has nonzero singular
values

\[
\frac56,\quad\frac12.
\]

Each centered equilateral triple is a tight frame with frame factor \(3/2\),
so the corresponding principal cosines are

\[
\frac23\frac56=\frac59,
\qquad
\frac23\frac12=\frac13.
\]

For non-adjacent ring faces the centered-frame cross Gram has the sole nonzero
singular value

\[
\frac13,
\]

hence the sole nonzero principal cosine is

\[
\boxed{\frac23\frac13=\frac29.}
\]

The exhaustive numerical calculation is therefore only a global incidence
check of an exact rational local result.

## 5. Operator trace realization of a, b and s23

The typed incidence packets of v0.1 can be promoted from cardinality notation
to normalized finite-dimensional trace readouts.

Let

\[
\mathcal H_-:=\mathbb C^2_F\oplus\mathbb C^5_E,
\qquad \dim\mathcal H_-=7,
\]

and let \(P_F\) be the rank-two projector onto the face-side block.  With the
normalized trace state \(\tau_7(X)=\operatorname{Tr}X/7\),

\[
\boxed{
a=\tau_7(P_F)=\frac27.}
\]

Likewise let

\[
\mathcal H_0:=\mathbb C^2_{F_{\rm src}}
\oplus\mathbb C^5_E
\oplus\mathbb C^2_{F_{\rm dst}},
\qquad \dim\mathcal H_0=9,
\]

with rank-two source-face projector \(P_{F_{\rm src}}\).  Then

\[
\boxed{
\tau_9(P_{F_{\rm src}})=\frac29=b.
}
\]

This normalized-trace result is independently crosschecked by the principal
cosine theorem of Section 3.

Finally use the binary side space \(\mathbb C^2_{\pm}\) and a rank-one side
projector \(P_+\).  On

\[
\mathcal H_{23}
=\mathbb C^2_{\pm}\otimes\mathcal H_-\otimes\mathcal H_-
\]

the product projector

\[
P_{23}=P_+\otimes P_F\otimes P_F
\]

has normalized trace

\[
\boxed{
\tau_{98}(P_{23})
=\frac12\left(\frac27\right)^2
=\frac2{49}.
}
\]

Thus the current value

\[
s_{23}=\frac2{49}
\]

has an exact finite-operator realization.  The remaining open statement is why
this product packet, rather than another admissible packet, is uniquely selected
by the physical/flavour \(23\) transition.

## 6. Composite-root realization of s13

In the standard \(A_2\cong\mathfrak{su}(3)\) root algebra,

\[
[E_{12},E_{23}]=E_{13}.
\]

Therefore the \(13\) channel is algebraically non-simple: once the two simple
root channels are fixed, its leading non-Abelian carrier is their commutator.

The current CKM structural value factorizes exactly as

\[
\boxed{
s_{13}=s_{23}\,b\,c.}
\]

The three factors now have independent operator meanings inside this candidate:

- \(s_{23}=2/49\): normalized product-projector trace;
- \(b=2/9\): normalized packet trace and non-adjacent \(A_2\)-plane principal
  cosine;
- \(c=2/5\): normalized edge-star overlap.

Consequently an incidence-dressed commutator whose \(13\) projection contracts
through the two geometric overlaps has coefficient

\[
\boxed{
\frac2{49}\frac29\frac25
=\frac8{2205},
}
\]

which is exactly the current \(s_{13}\).

This establishes an exact **operator realization** of the formula.  It does not
yet establish uniqueness of the dressing/projection functor, so the
first-principles selector remains open.

## 7. s12 and the remaining kappa problem

The geometric base part is now operator-derived twice:

\[
\boxed{s_{12}^{(0)}=b=\frac29.}
\]

The current full value is

\[
\boxed{s_{12}=b+a\kappa.}
\]

Both factors in the correction are individually derived in TIR:

\[
a=\frac27,
\qquad
\kappa=\frac{\ln2}{24\pi}.
\]

At the purely operator-algebra level one may realize the sum on
\(\mathcal H_0\otimes\mathcal H_-\) by the Hermitian observable

\[
\mathcal O_{12}
=P_{F_{\rm src}}\otimes I_7
+\kappa I_9\otimes P_F,
\]

because the maximally mixed normalized trace gives

\[
\boxed{
\tau_{63}(\mathcal O_{12})
=\frac29+\kappa\frac27.
}
\]

This proves existence of an exact operator realization, but **not** the dynamic
selection of this additive observable.  Deriving that additive linear-response
term from a connection/holonomy or information-flow operator is the principal
remaining mathematical gate.

## 8. What has actually been reduced

Before this bridge the CKM upstream gate was

\[
\text{why }\frac27,\ \frac29,\ \frac25,
\quad\text{and why combine them this way?}
\]

After v0.2 the open part is narrower:

1. one face canonically generates the local \(A_2\) three-channel geometry;
2. \(b=2/9\) is an exact principal overlap of a specific local transport class;
3. \(c=2/5\) is an exact edge-star overlap;
4. \(a=2/7\) is an exact normalized typed-packet projector trace;
5. \(s_{23}=2/49\) has an exact product-projector realization;
6. \(s_{13}\) matches the \(A_2\) composite-root structure and exact geometric
   dressing product;
7. only the **unique channel-selector / dynamical dressing theorem**, especially
   the additive \(a\kappa\) term, remains open.

The current atomic transition-selector elsewhere in TIR does not close this
problem: its transition-sensitive fields are present in the schema but are not
consumed by the orientation evaluator.  This candidate does not silently use
that underdetermined route.

## 9. Proof firewall

This document does not claim that:

- the 600-cell is a physically literal lattice;
- every normalized projector trace is automatically a particle mixing angle;
- the Weyl permutation of the three local channels is physically fixed;
- the \(23\) product packet is uniquely selected by current first principles;
- the \(13\) incidence dressing is the unique possible equivariant dressing;
- the additive \(a\kappa\) term has a dynamical derivation.

The safe result is:

\[
\boxed{
\text{600-cell incidence}
\Rightarrow
A_2\text{ local carrier}
+\left\{\frac27,\frac29,\frac25,\frac2{49}\right\}
\text{ exact operator readouts}
}
\]

with full current CKM arithmetic reconstructed downstream and selector
uniqueness still explicitly open.

Validator:

`TIR/validation/tir_ckm_600cell_a2_selector_bridge_candidate_v0_2.py`
