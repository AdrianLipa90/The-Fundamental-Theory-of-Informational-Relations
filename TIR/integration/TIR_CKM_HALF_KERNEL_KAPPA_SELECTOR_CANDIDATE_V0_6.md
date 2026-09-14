# TIR CKM Half-Kernel Kappa Selector Candidate v0.6

Status: `EXACT_HALF_KERNEL / EXACT_9_TO_7_BOUNDARY_COMPRESSION / EXACT_PRODUCT_GENERATOR_TRACE / PHYSICAL_BINDING_CONDITIONAL_POSTDICTIVE`

Date: 2026-09-14

## Scope

This layer tests whether the projective half endpoint can supply the missing mechanism behind the historical refinement

\[
s_{12}=b+a\kappa.
\]

It does not change the provenance classification of the CKM formula: the historical refined form remains postdictive. The purpose is to replace a free operator realization by a structurally selected boundary sector.

## 1. Positive half kernel

On the ordered terminal basis

\[
(|4\rangle,|2\rangle,|1\rangle,|1/2\rangle)
\]

use the deterministic transfer

\[
4\to2,\qquad2\to1,\qquad1\to1/2,\qquad1/2\to1/2.
\]

With \(G_C=I-P_C\),

\[
A_C=G_C^\dagger G_C=
\begin{pmatrix}
2&-1&0&0\\
-1&2&-1&0\\
0&-1&2&0\\
0&0&0&0
\end{pmatrix}.
\]

This is positive semidefinite and has

\[
\ker A_C=\operatorname{span}\{|1/2\rangle\}.
\]

The exact spectral projector is

\[
\Pi_{1/2}=I-\frac52A_C+\frac32A_C^2-\frac14A_C^3=|1/2\rangle\langle1/2|.
\]

No CKM observable enters this construction.

## 2. Half-boundary packet compression

The already validated source-edge-target incidence packet is

\[
F_{\rm src}\oplus E\oplus F_{\rm dst},\qquad2+5+2=9.
\]

At an absorbing terminal half-boundary, one terminal face side is removed. The surviving one-sided packet is

\[
F\oplus E,\qquad2+5=7.
\]

Thus the normalized rank-two face projector changes from

\[
\tau_9(P_F)=\frac29=b
\]

to

\[
\boxed{\tau_7(P_F)=\frac27=a.}
\]

The result is independent of which of the two equivalent face ends is called source or target.

## 3. Product-flow generator

For independent bulk and half-boundary factors, the generator of the tensor product flow is the Kronecker sum

\[
\boxed{\mathcal O_{12}=P_F^{(9)}\otimes I_7+\kappa I_9\otimes P_F^{(7)}.}
\]

Its normalized trace is exact:

\[
\begin{aligned}
\tau_{63}(\mathcal O_{12})&=\frac{2\cdot7}{63}+\kappa\frac{9\cdot2}{63}\\
&=\boxed{\frac29+\kappa\frac27}\\
&=\boxed{b+a\kappa}.
\end{aligned}
\]

Therefore the additive \(a\kappa\) term has an exact product-generator realization in which the coefficient \(a\) is selected by the half-boundary compression \(9\to7\), rather than inserted as a free scalar.

What remains conditional is the physical statement that this product flow is the unique CKM \(1\leftrightarrow2\) generator.

## 4. Exact inverse-scale ladder

The three incidence weights obey

\[
c=\frac25,\qquad a=\frac27,\qquad b=\frac29,
\]

hence

\[
\boxed{c^{-1}=\frac52,\qquad a^{-1}=\frac72,\qquad b^{-1}=\frac92.}
\]

The middle scale is exactly

\[
\boxed{a^{-1}=\frac12\left(c^{-1}+b^{-1}\right)=\frac72.}
\]

Equivalently \(a\) is the harmonic mean of \(b\) and \(c\).

## 5. Xi-kernel crosscheck

The canonical TIR Xi implementation

`TIR/zeta_information_axis/src/critical_axis/xi_kernel.py`

contains the standard Riemann-kernel powers

\[
e^{9u/2}\quad\text{and}\quad e^{5u/2}.
\]

These are exactly

\[
b^{-1}=\frac92,\qquad c^{-1}=\frac52.
\]

A mixed/cross exponent has midpoint

\[
\frac12\left(\frac92+\frac52\right)=\frac72=a^{-1}.
\]

This is an exact structural crosscheck between the CKM incidence ladder and the standard Xi kernel. It is not promoted here to a physical CKM–Xi coupling law.

## 6. Epistemic boundary

Closed exactly in this candidate layer:

- positive self-adjoint half operator \(A_C\);
- unique half kernel and exact half projector;
- boundary packet compression \(9\to7\);
- \(b=2/9\), \(a=2/7\), \(c=2/5\);
- Kronecker-sum trace \(b+a\kappa\);
- inverse ladder \(5/2,7/2,9/2\);
- exact Xi endpoint-exponent/midpoint crosscheck.

Still open:

- derivation that the product flow is the unique physical CKM generator;
- prospective validation independent of historical CKM development;
- promotion of the refined formula to a first-principles prediction.

The correct status is therefore **conditional mechanism closure**, not prospective prediction.

Validator:

`TIR/validation/tir_ckm_half_kernel_kappa_selector_candidate_v0_6.py`
