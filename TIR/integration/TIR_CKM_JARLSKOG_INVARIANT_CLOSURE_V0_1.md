# TIR CKM Jarlskog Invariant Closure v0.1

Status: `EXACT_CKM_INVARIANT_CLOSURE / HISTORICAL_ASSIGNMENT_DEPRECATED / MIXING_WEIGHT_UPSTREAM_OPEN`

Date: 2026-09-14

## Scope

This surface removes the Jarlskog invariant as an independent TIR input once the current CKM parameterization is fixed. It does not promote the current three CKM mixing-magnitude formulas to theorem-level first-principles status; that upstream selector remains open.

## Current TIR CKM parameterization

To avoid collision with the standard Wolfenstein coefficient `A`, define the auxiliary structural ratios

\[
\kappa=\frac{\ln2}{24\pi},\qquad
a=\frac{L_4}{L_3}=\frac27,\qquad
b=\frac{L_4}{L_3+L_4}=\frac29,\qquad
c=\frac{L_4}{L_5}=\frac25.
\]

The retained CKM inputs are

\[
s_{12}=b+a\kappa,
\qquad
s_{23}=\frac{a^2}{2},
\qquad
s_{13}=\frac{a^2bc}{2},
\qquad
\delta=\arccos c.
\]

Let

\[
c_{ij}=\sqrt{1-s_{ij}^2}.
\]

Using the standard CKM factorization

\[
V_{\rm CKM}=R_{23}R_{13}(\delta)R_{12},
\]

with

\[
R_{12}=\begin{pmatrix}
c_{12}&s_{12}&0\\
-s_{12}&c_{12}&0\\
0&0&1
\end{pmatrix},
\]

\[
R_{13}=\begin{pmatrix}
c_{13}&0&s_{13}e^{-i\delta}\\
0&1&0\\
-s_{13}e^{i\delta}&0&c_{13}
\end{pmatrix},
\]

\[
R_{23}=\begin{pmatrix}
1&0&0\\
0&c_{23}&s_{23}\\
0&-s_{23}&c_{23}
\end{pmatrix},
\]

the matrix is unitary and has determinant one identically.

## Exact Jarlskog closure

For any standard three-angle one-phase CKM parameterization,

\[
\boxed{
J=\operatorname{Im}
\left(V_{ud}V_{cs}V_{us}^{\ast}V_{cd}^{\ast}\right)
=s_{12}s_{23}s_{13}c_{12}c_{23}c_{13}^{2}\sin\delta.
}
\]

Substituting the current TIR parameterization gives

\[
\boxed{
J_{\rm TIR}^{\rm CKM}
=
\frac{a^4bc}{4}(b+a\kappa)
\sqrt{1-(b+a\kappa)^2}
\sqrt{1-\frac{a^4}{4}}
\left(1-\frac{a^4b^2c^2}{4}\right)
\sqrt{1-c^2}.
}
\]

For

\[
(a,b,c)=\left(\frac27,\frac29,\frac25\right),
\]

this evaluates to

\[
\boxed{J_{\rm TIR}^{\rm CKM}=2.97106576668\times10^{-5}.}
\]

The validator additionally checks all nontrivial rephasing-invariant quartets and confirms the common magnitude \(|J|\) up to orientation sign.

## Deprecation of the historical structural assignment

The historical independent expression

\[
J_{\rm old}
=\kappa^2 c\left(1-\frac{c^2}{2}\right)
=3.11011545905\times10^{-5}
\]

is not the exact Jarlskog invariant of the current CKM matrix and is therefore deprecated as an independent CP invariant assignment.

Its relative gap from the exact matrix invariant is

\[
\boxed{
\frac{|J_{\rm old}-J_{\rm TIR}^{\rm CKM}|}{J_{\rm old}}
=4.47088522\%.
}
\]

The discrepancy has two structural sources.

First,

\[
\sin\delta=\sqrt{1-c^2},
\]

whereas

\[
1-\frac{c^2}{2}
\]

is only the first nontrivial truncation of the Taylor series of \(\sqrt{1-c^2}\).

Second, the exact invariant carries the full mixing Jacobian

\[
\mathcal M
=
\frac{s_{12}s_{23}s_{13}c_{12}c_{23}c_{13}^2}{\kappa^2c}
=0.95892344664\ldots,
\]

which is absent from the historical assignment.

Thus

\[
\boxed{
J_{\rm TIR}^{\rm CKM}
=\kappa^2c\,\mathcal M\,\sqrt{1-c^2},
}
\]

while \(J_{\rm old}\) replaced the product \(\mathcal M\sqrt{1-c^2}\) by \(1-c^2/2\).

## Historical backsolve correction

The archived Stage-32 backsolve used a denominator proportional to

\[
s_{12}s_{23}s_{13}c_{12}c_{23}c_{13},
\]

but the exact Jarlskog relation contains

\[
\boxed{c_{13}^2}.
\]

Since \(c_{13}\approx1\), the numerical effect is tiny, but the distinction is formal and retained here.

## Epistemic boundary

The following statements are closed:

- once \((s_{12},s_{23},s_{13},\delta)\) are fixed, \(J\) is not an independent parameter;
- the current TIR CKM parameterization gives a unique exact Jarlskog invariant through the quartet identity;
- the historical independent \(J_{\rm old}\) assignment is not equal to that invariant and is deprecated;
- the current CKM matrix is unitary with determinant one;
- all rephasing-invariant quartets carry the same \(|J|\) up to orientation sign.

The following remains open:

\[
\boxed{
\text{first-principles forcing of }
 s_{12}=b+a\kappa,
\quad
 s_{23}=a^2/2,
\quad
 s_{13}=a^2bc/2.
}
\]

Therefore this file closes the Jarlskog invariant downstream of the current CKM inputs, but does not yet close the full CKM mixing-weight upstream.

## Validator

`TIR/validation/tir_ckm_jarlskog_invariant_closure_v0_1.py`
