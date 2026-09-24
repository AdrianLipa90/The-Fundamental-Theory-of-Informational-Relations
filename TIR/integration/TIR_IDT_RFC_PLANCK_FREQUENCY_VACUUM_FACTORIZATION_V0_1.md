# TIR × IDT × RFC Planck-Frequency Factorization of the RF-F15 Vacuum Integration Constant v0.1

Status: PLANCK_FREQUENCY_REFERENCE_SCALE_EXACT / RF_F15_DIMENSIONLESS_CHI_LAMBDA_FACTORIZATION_EXACT_CONDITIONAL / FULL_TETRA_NORMALIZATION_EXACT / LEGACY_224_TRANSLATION_EXACT_NOT_DERIVATION / INTERNAL_OMEGA_STAR_PREDICTION_OPEN

Date: 2026-09-24

## 1. Purpose

The RF-F15 fixed-\(x\) transport family contains the conserved integration coordinate

\[
C_\Lambda
=
|\omega|^4
\left[
v-\frac{1-x}{2}
\right],
\qquad
[C_\Lambda]=T^{-4},
\]

and the constant vacuum component

\[
\boxed{
\rho_\Lambda=K_0 C_\Lambda,
}
\]

with

\[
\boxed{
K_0
=
\frac{q_0\mathcal N}{2a_{FS}c^3}.
}
\]

The previous dimensional gate proves that dimensionless topology cannot fix a nonzero \(C_\Lambda\) without an independent frequency scale.

This gate introduces a universal reference scale without using \(H_0\), \(\Lambda\), \(\rho_\Lambda\), or \(\Omega_\Lambda\).

It is a calibration/factorization theorem, not an internal derivation of the scale.

## 2. Planck-frequency reference

Using the independently known dimensional constants \(c,\hbar,G\), define

\[
\boxed{
\Omega_P
:=
\sqrt{\frac{c^5}{\hbar G}}.
}
\]

Then

\[
\boxed{
[\Omega_P]=T^{-1}.
}
\]

Equivalently,

\[
\Omega_P=t_P^{-1}
\]

for the standard Planck time

\[
t_P=\sqrt{\frac{\hbar G}{c^5}}.
\]

Define the dimensionless RF-F15 vacuum coordinate

\[
\boxed{
\chi_\Lambda
:=
\frac{C_\Lambda}{\Omega_P^4}.
}
\]

Hence

\[
\boxed{
C_\Lambda
=
\Omega_P^4\chi_\Lambda.
}
\]

No cosmological observable enters this definition.

## 3. Planck energy-density reference

Define the standard Planck energy-density scale

\[
\boxed{
\varepsilon_P
:=
\frac{c^7}{\hbar G^2}.
}
\]

Using

\[
\Omega_P^4
=
\frac{c^{10}}{\hbar^2G^2},
\]

the RF-F15 vacuum density becomes

\[
\rho_\Lambda
=
\frac{q_0\mathcal N}{2a_{FS}c^3}
\frac{c^{10}}{\hbar^2G^2}
\chi_\Lambda.
\]

Define the dimensionless carrier-action ratio

\[
\boxed{
\zeta_q:=\frac{q_0}{\hbar}.
}
\]

Then exactly

\[
\boxed{
\rho_\Lambda
=
\frac{\mathcal N\zeta_q}{2a_{FS}}
\varepsilon_P
\chi_\Lambda.
}
\]

Therefore

\[
\boxed{
\frac{\rho_\Lambda}{\varepsilon_P}
=
\frac{\mathcal N\zeta_q}{2a_{FS}}
\chi_\Lambda.
}
\]

This is the RF-F15 ↔ Planck-scale normalization bridge.

## 4. Full tetrahedral \(CP^1\) specialization

RFC RF-S10 derives the exact full tetrahedral projective area

\[
\boxed{
a_{FS}^{tet}=\pi.
}
\]

Therefore on the FULL_TETRA_CP1 branch,

\[
\boxed{
\frac{\rho_\Lambda}{\varepsilon_P}
=
\frac{\mathcal N\zeta_q}{2\pi}
\chi_\Lambda.
}
\]

If one additionally imposes the separately open elementary-carrier normalization

\[
q_0=\hbar
\quad\Longleftrightarrow\quad
\zeta_q=1,
\]

and the unit-occupation specialization

\[
\mathcal N=1,
\]

then

\[
\boxed{
\frac{\rho_\Lambda}{\varepsilon_P}
=
\frac{\chi_\Lambda}{2\pi}.
}
\]

Equivalently,

\[
\boxed{
\chi_\Lambda
=
2\pi
\frac{\rho_\Lambda}{\varepsilon_P}.
}
\]

The \(q_0=\hbar\) and \(\mathcal N=1\) conditions are explicit normalization assumptions, not currently promoted RF-F15 inputs.

## 5. Relation to the v12 cosmology suppression coordinate

TIR v12 retains the declared dimensionless legacy suppression

\[
\boxed{
r_\Lambda^{(224)}
=
\left(\frac27\right)^{224}
=
1.345110818116154\times10^{-122}.
}
\]

Current TIR explicitly classifies the dark-energy use of this expression as an ansatz because the exponent lacks an independent geometric derivation.

The v12 audit also quarantines the dimensionful reconstruction until a reference scale is specified.

If, only as a translation surface, one interprets

\[
r_\Lambda
=
\frac{\rho_\Lambda}{\varepsilon_P},
\]

then the RF-F15 coordinate must satisfy

\[
\boxed{
\chi_\Lambda
=
\frac{2a_{FS}}{\mathcal N\zeta_q}
r_\Lambda.
}
\]

For the full-tetra, unit-action-quantum, unit-occupation specialization,

\[
\boxed{
\chi_\Lambda
=
2\pi r_\Lambda.
}
\]

Thus the legacy arithmetic would correspond to

\[
\boxed{
\chi_\Lambda^{(224)}
=
2\pi\left(\frac27\right)^{224}
=
8.451580528915731\times10^{-122}.
}
\]

This is an exact translation of conventions.

It is not an independent derivation of \(224\), \(r_\Lambda\), \(q_0=\hbar\), or \(\mathcal N=1\).

## 6. Why this is not target leakage

The reference frequency

\[
\Omega_P
=
\sqrt{\frac{c^5}{\hbar G}}
\]

uses no late-time cosmological quantity.

In particular it does not use

\[
H_0,
\qquad
\Lambda,
\qquad
\rho_\Lambda,
\qquad
\Omega_\Lambda.
\]

Therefore defining

\[
\chi_\Lambda=C_\Lambda/\Omega_P^4
\]

is a non-circular dimensional factorization.

However, it is not a derivation of \(G\) from TIR/IDT/RFC.

RFC RF-N1B explicitly keeps the source normalization and universal \(G\) derivation open.

Thus the status is:

\[
\boxed{
\text{external universal scale calibration}
\neq
\text{internal scale prediction}.
}
\]

## 7. Relation to the RF-N1B \(G\)-consistency condition

RF-N1B gives the candidate consistency relation

\[
G
=
\mathcal C_G
\frac{c^5}{\hbar\omega^2},
\]

where

\[
\mathcal C_G
:=
\frac{\beta_I\mathcal J_\pi}
{24\pi\sqrt6\,n_Ea_{FS}}
\]

is not yet independently fixed.

Rearranging gives

\[
\boxed{
\omega^2
=
\mathcal C_G
\Omega_P^2.
}
\]

Thus

\[
\boxed{
\frac{\omega}{\Omega_P}
=
\sqrt{\mathcal C_G}
}
\]

on that candidate joint source bridge.

This does not internally derive \(\Omega_P\); instead it shows that RF-N1B already isolates the remaining problem into a dimensionless invariant \(\mathcal C_G\).

The same structural pattern now appears in the vacuum sector:

\[
\boxed{
C_\Lambda
=
\Omega_P^4\chi_\Lambda.
}
\]

Therefore the absolute-scale problem has been reduced to dimensionless closure coordinates once \(c,\hbar,G\) are admitted as calibrated constants.

## 8. What topology may now determine

The dimensional no-go is resolved at the level of factorization:

\[
\boxed{
\chi_\Lambda
=
F(Q_{\rm top})
}
\]

is dimensionally admissible.

Here \(Q_{\rm top}\) may include dimensionless winding, Chern, Euler, Berry or information coordinates.

A genuine first-principles cosmological prediction would therefore require a theorem fixing

\[
\boxed{
F(Q_{\rm top})
}
\]

without fitting to the observed vacuum density.

The legacy expression

\[
(2/7)^{224}
\]

is one historical candidate for such a dimensionless suppression, but its exponent remains un-derived and therefore cannot be promoted.

## 9. Current verdict

Exact:

\[
\boxed{
\Omega_P=\sqrt{c^5/(\hbar G)}
}
\]

\[
\boxed{
\chi_\Lambda=C_\Lambda/\Omega_P^4
}
\]

\[
\boxed{
\rho_\Lambda/\varepsilon_P
=
(\mathcal N\zeta_q/2a_{FS})\chi_\Lambda
}
\]

and, on full tetrahedral \(CP^1\),

\[
\boxed{
\rho_\Lambda/\varepsilon_P
=
(\mathcal N\zeta_q/2\pi)\chi_\Lambda.
}
\]

Open:

- internal derivation of \(G\);
- physical \(q_0/\hbar\);
- physical occupation \(\mathcal N\);
- independent derivation of \(\chi_\Lambda\);
- independent derivation of the legacy exponent \(224\).

Reference validator:

TIR/validation/tir_idt_rfc_planck_frequency_vacuum_factorization_v0_1.py
