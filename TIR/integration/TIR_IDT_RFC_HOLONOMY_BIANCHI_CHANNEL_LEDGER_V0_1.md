# TIR × IDT × RFC Holonomy Bianchi Channel Ledger v0.1

Status: EXACT_PARTITION_BOOKKEEPING_INVARIANCE / D_TO_DYNAMIC_LAMBDA_ROUNDTRIP_PASS / OMITTED_COMPLEMENT_DEFECT_EXACT / HOLONOMY_PHYSICS_REQUIRES_NONZERO_TOTAL_SOURCE_RESIDUAL / INDEPENDENT_TEMPORAL_U1_STRESS_OR_TOPOLOGICAL_BINDING_OPEN

Date: 2026-09-24

## 1. Purpose

The preceding cosmological-acceleration gate established two facts:

1. the canonical information scalar can source accelerated expansion without an additional bare cosmological constant;
2. the current temporal holonomy coordinate is a spectator in the RF-L3 scalar potential.

This gate asks whether the exact IDT holonomy partition

\[
C_h=\cos^2\frac{\tau_R}{2},
\qquad
D_h=\sin^2\frac{\tau_R}{2},
\qquad
C_h+D_h=1
\]

can nevertheless create a new gravitational effect merely by assigning the \(D_h\) share to a dynamic-Lambda channel.

The answer is no if the complementary source is retained consistently.

## 2. Parent canonical scalar

On the homogeneous canonical information-scalar branch, let

\[
K_I=\frac12(\phi_I')^2
\]

and

\[
\boxed{
\rho_I=K_I+U_I,
\qquad
p_I=K_I-U_I.
}
\]

The flat-FLRW acceleration source is

\[
\boxed{
\mathcal A_I
:=
\frac{a''}{a}
=
-\frac{\kappa_E}{6}
(\rho_I+3p_I)
=
-\frac{2\kappa_E}{3}K_I
+\frac{\kappa_E}{3}U_I.
}
\]

## 3. Exact holonomy partition

Define

\[
\boxed{
U_C:=C_hU_I,
\qquad
U_D:=D_hU_I.
}
\]

Then

\[
\boxed{
U_C+U_D=U_I
}
\]

for every \(\tau_R\).

This identity is algebraic and contains no physical stress attribution by itself.

## 4. Exact D-to-dynamic-Lambda reclassification

Suppose the \(D\) potential contribution is moved to the geometric side as

\[
\boxed{
\Lambda_D:=\kappa_EU_D
=\kappa_EU_ID_h.
}
\]

Keep the complementary canonical source on the matter side:

\[
\boxed{
\rho_C=K_I+U_C,
\qquad
p_C=K_I-U_C.
}
\]

The corresponding acceleration equation is

\[
\mathcal A_{\rm split}
=
-\frac{\kappa_E}{6}
(\rho_C+3p_C)
+
\frac{\Lambda_D}{3}.
\]

Substitution gives

\[
\begin{aligned}
\mathcal A_{\rm split}
&=
-\frac{\kappa_E}{6}
\left(
4K_I-2U_C
\right)
+
\frac{\kappa_EU_D}{3}\\
&=
-\frac{2\kappa_E}{3}K_I
+
\frac{\kappa_E}{3}(U_C+U_D)\\
&=
-\frac{2\kappa_E}{3}K_I
+
\frac{\kappa_E}{3}U_I.
\end{aligned}
\]

Therefore

\[
\boxed{
\mathcal A_{\rm split}
=
\mathcal A_I
}
\]

for every \(\tau_R\).

The same result holds tensorially: moving one metric-proportional subterm from the source side to the geometric side is a bookkeeping transformation of the same Einstein equation.

## 5. Bianchi ledger

Let

\[
V_D:=U_ID_h.
\]

The metric-proportional D-channel tensor is

\[
\boxed{
T^D_{\mu\nu}
=
-V_Dg_{\mu\nu}.
}
\]

Metric compatibility gives exactly

\[
\boxed{
\nabla^\mu T^D_{\mu\nu}
=
-\nabla_\nu V_D.
}
\]

If the complete original information-scalar tensor is conserved on its equations of motion and the D term is displayed separately, the complementary tensor must satisfy

\[
\boxed{
\nabla^\mu T^C_{\mu\nu}
=
+\nabla_\nu V_D.
}
\]

Equivalently, with

\[
\Lambda_D=\kappa_EV_D,
\]

\[
\boxed{
\kappa_E\nabla^\mu T^C_{\mu\nu}
=
\nabla_\nu\Lambda_D.
}
\]

This is the same transfer structure already present in the RF-L2 dynamic-Lambda branch.

No new conservation law is introduced.

## 6. Exact omitted-complement defect

If one keeps only the canonical kinetic source and \(\Lambda_D\), while discarding \(U_C\), the resulting acceleration is

\[
\mathcal A_{\rm omitC}
=
-\frac{2\kappa_E}{3}K_I
+
\frac{\kappa_E}{3}U_ID_h.
\]

The exact discrepancy from the original scalar dynamics is

\[
\boxed{
\mathcal A_I-\mathcal A_{\rm omitC}
=
\frac{\kappa_E}{3}U_IC_h.
}
\]

Thus a \(\tau_R\)-dependent acceleration obtained by moving \(D_hU_I\) to the Lambda side and silently dropping \(C_hU_I\) is precisely an omitted-source artifact.

The defect vanishes only when

\[
C_h=0
\]

or the complementary source is physically removed by an independently derived dynamical mechanism.

## 7. Partition invariance theorem

Let \(T^I_{\mu\nu}\) be a fixed total Euler-Lagrange source tensor. Any exact decomposition

\[
T^I_{\mu\nu}
=
T^C_{\mu\nu}(\tau_R)
+
T^D_{\mu\nu}(\tau_R)
\]

followed by algebraic transfer of a metric-proportional part between the two sides of the same field equation leaves the spacetime solution set unchanged.

Therefore

\[
\boxed{
\text{holonomy-dependent bookkeeping}
\neq
\text{holonomy-dependent gravity}.
}
\]

A physical holonomy effect requires the total variational source to change.

## 8. Minimal physical target

Define the genuinely new holonomy source residual by

\[
\boxed{
\Delta T^{hol}_{\mu\nu}
:=
T^{new}_{\mu\nu}
-
T^I_{\mu\nu}.
}
\]

For a physical modification,

\[
\boxed{
\Delta T^{hol}_{\mu\nu}\neq0
}
\]

must hold on at least one admitted nontrivial holonomy configuration.

If the base source remains separately conserved, consistency requires

\[
\boxed{
\nabla^\mu\Delta T^{hol}_{\mu\nu}=0.
}
\]

If it exchanges energy-momentum with another admitted sector, the complete exchange ledger must instead sum to zero.

The source should also satisfy the trivial-holonomy control

\[
\boxed{
\Delta T^{hol}_{\mu\nu}\to0
\quad
\text{when the independently defined holonomy defect vanishes},
}
\]

unless a nonzero topological sector is explicitly selected by boundary data.

## 9. Connection firewall

The IDT \(\tau_R\) carrier is a temporal/internal \(U(1)\) holonomy.

The TIR/RFC Levi-Civita spacetime holonomy already belongs to the geometric curvature of the metric.

The two may not be identified by notation alone.

A new \(\Delta T^{hol}_{\mu\nu}\) must therefore establish that the temporal/internal \(U(1)\) connection is an independent physical carrier or provide an explicit adapter to the spacetime connection without counting the same curvature twice.

## 10. Current verdict

The exact C/D partition and dynamic-Lambda rearrangement do not produce new cosmology.

The smallest non-circular next gate is

\[
\boxed{
\text{independent temporal }U(1)\text{ physics or topological sector}
\to
\Delta T^{hol}_{\mu\nu}\neq0
\to
\text{Bianchi-compatible total source}
\to
\text{FLRW/perturbation tests}.
}
\]

No value for a new coefficient is introduced at this gate.

Reference validator:

TIR/validation/tir_idt_rfc_holonomy_bianchi_channel_ledger_v0_1.py
