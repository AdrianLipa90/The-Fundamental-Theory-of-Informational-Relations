# TIR × IDT × RFC \(C_\Lambda\) Topological Dimensional No-Go v0.1

Status: C_LAMBDA_DIMENSION_EXACT / DIMENSIONLESS_HOLONOMY_ALONE_CANNOT_FIX_MAGNITUDE / INDEPENDENT_FREQUENCY_SCALE_REQUIRED / TOPOLOGICAL_RATIO_BINDING_REMAINS_POSSIBLE

Date: 2026-09-24

## 1. Parent transport constant

RF-F15 gives, on the fixed-\(x\) transport family,

\[
v(\omega)
=
\frac{1-x}{2}
+
\frac{C_\Lambda}{\omega^4},
\]

where \(v\) and \(x\) are dimensionless.

Therefore

\[
\boxed{
[C_\Lambda]=[\omega]^4=T^{-4}.
}
\]

The associated constant vacuum density is

\[
\boxed{
\rho_\Lambda=K_0C_\Lambda.
}
\]

## 2. Dimensionless topological data

The current project holonomy/topology carriers include quantities of the following types:

\[
\tau_R\in\mathbb R/2\pi\mathbb Z,
\]

\[
e^{i\tau_R}\in U(1),
\]

\[
n_{\rm wind}\in\mathbb Z,
\]

\[
c_1=\frac{1}{2\pi}\int F_B\in\mathbb Z,
\]

and

\[
\kappa=\frac{\ln2}{24\pi}.
\]

All of these are dimensionless.

Let

\[
Q_{\rm top}
\]

denote any collection built only from such dimensionless holonomy, winding, Chern, Euler or information numbers.

Then every ordinary function

\[
F(Q_{\rm top})
\]

is dimensionless.

Hence

\[
\boxed{
C_\Lambda=F(Q_{\rm top})
}
\]

is dimensionally impossible unless \(C_\Lambda=0\) is selected trivially or an additional dimensionful scale is supplied.

## 3. Minimal dimensionally admissible topological binding

A nonzero topological/holonomic binding must have the form

\[
\boxed{
C_\Lambda
=
\Omega_*^4
F(Q_{\rm top}),
}
\]

where

\[
\boxed{
[\Omega_*]=T^{-1}.
}
\]

Equivalently,

\[
\boxed{
\frac{C_\Lambda}{\Omega_*^4}
=
F(Q_{\rm top})
}
\]

is the dimensionless quantity that topology may determine.

The topology may therefore quantize, constrain or select a dimensionless ratio, but it cannot by itself create the missing physical frequency scale.

## 4. Consequence for vacuum density

The RF-F15 vacuum density becomes

\[
\boxed{
\rho_\Lambda
=
K_0\Omega_*^4F(Q_{\rm top}).
}
\]

Thus a parameter-free vacuum-density prediction requires independent derivations of:

1. \(K_0\) on the physical carrier/current realization;
2. the frequency scale \(\Omega_*\);
3. the dimensionless topological factor \(F(Q_{\rm top})\).

A topological integer alone closes only item 3.

## 5. Why the phase rate \(\omega\) does not automatically solve the scale problem

The dynamical phase rate satisfies

\[
|\omega|\propto a^{-1}
\]

on the RF-F12 FLRW branch.

The integration constant \(C_\Lambda\), however, is conserved:

\[
\frac{dC_\Lambda}{d\ln|\omega|}=0.
\]

Therefore a formula

\[
C_\Lambda=\omega(t)^4F(Q_{\rm top})
\]

with fixed nonzero \(F\) would generally vary as the universe evolves and contradict the fixed-\(x\) conserved integration coordinate.

A phase-rate scale can be used only if an independently selected reference/boundary value

\[
\Omega_*:=|\omega|_{\rm boundary}
\]

or another invariant physical frequency is derived.

Such a boundary scale is additional physical information; it is not supplied by the dimensionless holonomy alone.

## 6. Relation to \(\kappa\)

The canonical information constant

\[
\kappa=\frac{\ln2}{24\pi}
\]

is dimensionless.

Therefore expressions such as

\[
C_\Lambda\propto\kappa,
\qquad
C_\Lambda\propto n_{\rm wind}\kappa,
\qquad
C_\Lambda\propto f(\tau_R,\kappa)
\]

do not close the dimension of \(C_\Lambda\).

A dimensionally admissible version is, for example,

\[
C_\Lambda
=
\Omega_*^4 f(\tau_R,\kappa,n_{\rm wind},c_1,\ldots).
\]

The scale \(\Omega_*\) still requires independent provenance.

## 7. Legacy Hubble/Poincaré normalization firewall

Archived TIR/MetaTime notes contain constructions in which a dimensionless cosmological closure coordinate is formed using a Hubble/Poincaré area.

Those constructions import a dimensionful cosmological scale such as \(H_0\) into the normalization.

They therefore do not constitute a parameter-free derivation of the dimensionful vacuum scale from topology alone.

They may be used as historical candidate interfaces, not as current evidence closing \(C_\Lambda\).

## 8. Current frontier

The strongest non-circular target is now

\[
\boxed{
\text{derive }\Omega_*\text{ independently}
}
\]

and separately test whether

\[
\boxed{
C_\Lambda/\Omega_*^4
}
\]

is fixed by an Euler/Berry/Chern/winding invariant.

Possible scale sources must come from already source-owned physics rather than the target cosmological vacuum magnitude itself.

## 9. Verdict

\[
\boxed{
\text{dimensionless holonomy/topology alone cannot determine nonzero }C_\Lambda.
}
\]

But

\[
\boxed{
\text{topology may determine }C_\Lambda/\Omega_*^4
}
\]

once an independent frequency scale is available.

This is a dimensional no-go on the absolute magnitude, not a no-go on topological quantization of a dimensionless ratio.

Reference validator:

TIR/validation/tir_idt_rfc_c_lambda_topological_dimensional_no_go_v0_1.py
