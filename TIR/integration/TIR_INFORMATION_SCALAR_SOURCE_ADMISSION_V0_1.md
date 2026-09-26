# TIR Information-Scalar Source Admission v0.1

**Date:** 2026-09-26  
**Status:** VARIATIONAL_SOURCE_STRUCTURE_PASS / ABSOLUTE_NORMALIZATION_OPEN / PRODUCTION_REALIZATION_OPEN

## 1. Purpose

This gate evaluates the existing TIR canonical information-scalar source
against the new Einstein source-admission firewall.

It does not modify the existing RF-L2/RF-L3/RF-L4A action. It asks whether the
current source is independently defined, variational and Bianchi-compatible,
rather than being obtained by algebraically rearranging the Einstein tensor.

## 2. Existing TIR source

The current TIR information-scalar branch uses

\[
\Xi_I>0,
\qquad
\phi_I=\sqrt{2\Xi_I},
\]

and

\[
U_I
=
\frac{\alpha_I}{\kappa_E}\Xi_I.
\]

Define

\[
m_I^2
:=
\frac{\alpha_I}{\kappa_E}.
\]

Then

\[
\boxed{
U_I
=
\frac12 m_I^2\phi_I^2
}.
\]

This is the standard quadratic potential of a canonical scalar field.

The homogeneous source ledger is

\[
\boxed{
\rho_I
=
\frac12(\phi_I')^2+U_I,
\qquad
p_I
=
\frac12(\phi_I')^2-U_I.
}
\]

This source is defined from the scalar action, not by

\[
T_{\mu\nu}
=
G_{\mu\nu}/\kappa_E.
\]

Therefore it passes the non-circular source-semantics gate.

## 3. Covariant conservation / KG identity

For a homogeneous canonical scalar, the continuity equation is

\[
\rho_I'
+
3H(\rho_I+p_I)
=
0.
\]

Using

\[
\rho_I
=
\frac12(\phi_I')^2+U_I,
\]

one obtains

\[
\rho_I'
=
\phi_I'\phi_I''
+
U_{I,\phi}\phi_I'.
\]

Also

\[
\rho_I+p_I
=
(\phi_I')^2.
\]

Hence

\[
\boxed{
\rho_I'
+
3H(\rho_I+p_I)
=
\phi_I'
\left(
\phi_I''
+
3H\phi_I'
+
U_{I,\phi}
\right).
}
\]

For the quadratic TIR potential,

\[
U_{I,\phi}
=
m_I^2\phi_I,
\]

so on the Euler-Lagrange equation

\[
\boxed{
\phi_I''
+
3H\phi_I'
+
m_I^2\phi_I
=
0
}
\]

the source is conserved exactly.

Thus:

\[
\boxed{
\nabla_\mu T_I^{\mu\nu}=0
}
\]

on-shell, as required by the Bianchi identity.

Status:

TIR_INFORMATION_SCALAR_BIANCHI_SOURCE = PASS_CONDITIONAL_ON_EOM.

## 4. Exact recovery of the existing acceleration formula

The Einstein acceleration equation on the admitted FLRW branch is

\[
\frac{a''}{a}
=
-\frac{\kappa_E}{6}
(\rho_I+3p_I).
\]

For the canonical scalar,

\[
\rho_I+3p_I
=
2(\phi_I')^2-2U_I.
\]

Therefore

\[
\frac{a''}{a}
=
\frac{\kappa_E}{3}
\left(
U_I-(\phi_I')^2
\right).
\]

Using

\[
\phi_I=\sqrt{2\Xi_I}
\]

gives

\[
(\phi_I')^2
=
\frac{(\Xi_I')^2}{2\Xi_I}.
\]

With

\[
U_I
=
\frac{\alpha_I}{\kappa_E}\Xi_I,
\]

we obtain exactly

\[
\boxed{
\frac{a''}{a}\Big|_I
=
\frac{\alpha_I\Xi_I}{3}
-
\frac{\kappa_E}{6\Xi_I}
(\Xi_I')^2.
}
\]

So the existing TIR acceleration theorem is exactly the standard canonical
scalar source result written in the \(\Xi_I\) coordinate.

No additional source term is needed for this equivalence.

## 5. Holonomy spectator result survives the source audit

The current admitted potential is

\[
U_I
=
U_I(\Xi_I)
\]

and

\[
\frac{\partial U_I}{\partial\tau_R}
=
0.
\]

Therefore the current scalar stress tensor has no independent
\(\tau_R\)-dependent variational contribution.

The existing result remains:

\[
\boxed{
\text{current temporal holonomy is a spectator in the admitted scalar source}.
}
\]

The exact \(C_h+D_h=1\) partition cannot change this by bookkeeping alone.

A new holonomy-gravity effect still requires an independently derived
nonzero total-source residual

\[
\Delta T^{hol}_{\mu\nu}
\neq
0
\]

or an independently admitted geometric/topological sector.

## 6. Distinguish the two kappas

The TIR information coefficient

\[
\kappa
=
\frac{\ln2}{24\pi}
\]

and the Einstein/source coupling used in this scalar gravity ledger,

\[
\kappa_E,
\]

are distinct typed quantities.

This gate does not identify them.

Any future equality, scaling relation or dimensional conversion between them
requires its own physical binding and units.

## 7. What passes the source-admission firewall

PASS:

- source tensor comes from an independent canonical scalar action;
- source is symmetric;
- homogeneous \((\rho_I,p_I)\) have standard canonical-scalar form;
- Bianchi conservation is equivalent to the scalar Euler-Lagrange equation;
- existing acceleration formula is recovered exactly;
- dynamic-Lambda repartition is bookkeeping-equivalent when the complementary
  source is retained;
- current \(\tau_R\) holonomy remains spectator.

OPEN:

- absolute physical normalization of \(\alpha_I\);
- absolute physical normalization of \(m_I\);
- production event-spatial realization;
- observational value of \(\Xi_I\) and \(\Xi_I'\);
- independent KG/phase spectral identification;
- holonomy-active \(\Delta T^{hol}_{\mu\nu}\);
- perturbation/growth/late-time cosmology validation.

## 8. Updated classification

\[
\boxed{
\text{information-scalar source structure}
=
\text{ADMITTED VARIATIONAL SOURCE}
}
\]

conditional on the existing scalar-action premises.

But

\[
\boxed{
\text{absolute physical source calibration}
=
\text{OPEN}.
}
\]

This is a real narrowing of the source frontier: the blocker is now physical
normalization/realization, not conservation or source-tensor construction.

canon_allowed = false.
