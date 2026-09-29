# TIR × IDT × RFC Euler–Palatini Adapter and Torsion-Source Bifurcation v0.1

Status: PALATINI_EULER_METRIC_RESPONSE_ZERO_BRANCH_EXACT / EULER_PROJECTOR_CONNECTION_CURRENT_EXACT_CONDITIONAL / TORSION_FREE_MINIMAL_GR_BRANCH_INCOMPATIBLE_WITH_NONZERO_EULER_SPIN_CURRENT / EINSTEIN_CARTAN_EXTENSION_REQUIRED / LORENTZ_TO_U1_REDUCTION_OPEN

Date: 2026-09-24

## 1. Purpose

RFC RF-F20 leaves the Euler contribution to the phase-connection metric response open:

\[
R^{(E)}_{\mu\nu}
=
g^{\alpha\beta}q_\alpha
\frac{\partial\mathcal A^E_\beta}{\partial g^{\mu\nu}}.
\]

RFC RF-E21 independently supplies a first-order Cartan–Palatini gravitational action with Lorentz connection

\[
\omega^{AB}
\]

independent of the coframe

\[
E^A
\]

during variation.

This gate tests the most direct candidate identification of the legacy Euler/spin phase connection with an Abelian projection of the RFC Lorentz spin connection.

The result is a variational bifurcation:

\[
\boxed{
\text{Euler as Palatini connection}
\Rightarrow
\text{no direct RF-F20 metric response at fixed }\omega
}
\]

but generically

\[
\boxed{
\text{Euler projector}
\Rightarrow
\text{nonzero connection/spin current}
\Rightarrow
\text{torsion source}.
}
\]

## 2. Candidate Abelian Euler projection

Let

\[
n_{AB}=-n_{BA}
\]

be a dimensionless adjoint bivector selecting an Abelian spin-axis direction.

Use the candidate projection

\[
\boxed{
\mathcal A_E
=
\frac{s_E}{2}
n_{AB}\omega^{AB},
}
\]

with the spin-half normalization

\[
\boxed{
s_E=\frac12.
}
\]

The factor \(1/2\) prevents double counting of antisymmetric Lorentz-index pairs.

This is a candidate physical adapter.

It is not yet a theorem that the RFC Lorentz bundle admits the required global/local \(U(1)\) reduction.

## 3. Gauge-reduction firewall

The Lorentz connection transforms inhomogeneously under local Lorentz transformations.

Therefore the projected one-form

\[
n_{AB}\omega^{AB}
\]

is not automatically a \(U(1)\) gauge connection.

Promotion requires a reduction in which

\[
n_{AB}
\]

is an admitted adjoint field or section selecting a residual Abelian subgroup and transforms consistently with the Lorentz frame.

Schematically,

\[
\boxed{
SO^+(1,3)
\longrightarrow
H_n
\supseteq
U(1)
}
\]

must be supplied on the selected phase/spin branch.

Without this reduction, the formula for \(\mathcal A_E\) is a local projection candidate only.

## 4. Palatini metric-response theorem

RF-E21 uses the first-order variables

\[
(E^A,\omega^{AB})
\]

as independent variational coordinates.

On a coframe/metric variation at fixed Lorentz connection and fixed \(n_{AB}\),

\[
\boxed{
\delta_E\omega^{AB}=0,
\qquad
\delta_E n_{AB}=0.
}
\]

Hence

\[
\boxed{
\delta_E\mathcal A_E=0.
}
\]

Therefore the direct RF-F20 Euler response satisfies

\[
\boxed{
R^{(E)}_{\mu\nu}=0
}
\]

on this first-order Palatini branch.

Thus identifying the Euler phase connection with the independent Palatini connection does not generate the required negative RF-F20 metric response.

## 5. Phase projector with Euler connection

Let the gauge-covariant phase one-form be

\[
q_\mu
=
\partial_\mu\vartheta
+
\mathcal A^{rest}_\mu
+
\mathcal A^E_\mu,
\]

and define

\[
\boxed{
\mathcal C_\vartheta
=
-\frac{g^{\mu\nu}q_\mu q_\nu}{\mu_\vartheta^2}.
}
\]

Take the state-dependent interaction

\[
\boxed{
\mathcal L_{int}
=
\eta\widehat U_L
f(\mathcal C_\vartheta).
}
\]

During connection variation hold

\[
E^A,
\quad
\mu_\vartheta,
\quad
n_{AB}
\]

fixed.

Then

\[
\delta_\omega q_\mu
=
\frac{s_E}{2}
n_{AB}
\delta\omega_\mu{}^{AB}.
\]

Therefore

\[
\boxed{
\delta_\omega\mathcal C_\vartheta
=
-\frac{s_E}{\mu_\vartheta^2}
q^\mu n_{AB}
\delta\omega_\mu{}^{AB}.
}
\]

Consequently

\[
\boxed{
\frac{\partial\mathcal L_{int}}
{\partial\omega_\mu{}^{AB}}
=
-
\eta\widehat U_L
f'(\mathcal C_\vartheta)
\frac{s_E}{\mu_\vartheta^2}
q^\mu n_{AB}.
}
\]

This is an exact conditional connection-current formula for the candidate adapter.

## 6. Nonzero Euler spin-current condition

Define the Euler connection current by

\[
\boxed{
\mathfrak s^\mu{}_{AB}
:=
-2
\frac{\partial\mathcal L_{int}}
{\partial\omega_\mu{}^{AB}}.
}
\]

Then

\[
\boxed{
\mathfrak s^\mu{}_{AB}
=
\frac{
2\eta\widehat U_L s_E
f'(\mathcal C_\vartheta)
}{\mu_\vartheta^2}
q^\mu n_{AB}.
}
\]

On the projector surface

\[
\mathcal C_\vartheta=1,
\]

this becomes

\[
\boxed{
\mathfrak s^\mu{}_{AB}
=
\frac{
2\eta\widehat U_L s_E
f'(1)
}{\mu_\vartheta^2}
q^\mu n_{AB}.
}
\]

Thus the connection current is nonzero whenever the admitted branch has simultaneously

\[
\eta\ne0,
\quad
\widehat U_L\ne0,
\quad
s_E\ne0,
\quad
f'(1)\ne0,
\quad
q^\mu\ne0,
\quad
n_{AB}\ne0.
\]

## 7. Cartan equation with Euler source

RF-E21 gives the source-free connection equation

\[
\epsilon_{ABCD}E^C\wedge T^D=0.
\]

Define the Euler spin-current three-form

\[
\tau^{(E)}_{AB}
\]

with normalization chosen so that the sourced Cartan equation is

\[
\boxed{
\epsilon_{ABCD}
E^C\wedge T^D
=
\kappa_E
\tau^{(E)}_{AB}.
}
\]

The component current

\[
\mathfrak s^\mu{}_{AB}
\]

above is the local density representative of this source, up to the displayed convention defining the three-form.

Therefore

\[
\boxed{
\tau^{(E)}_{AB}\ne0
\Rightarrow
T^A\ne0
}
\]

for an invertible coframe.

## 8. Torsion-free no-go

The minimal RF-E21 GR branch imposes

\[
\boxed{
T^A=0.
}
\]

But the candidate Euler projector generically gives

\[
\boxed{
\tau^{(E)}_{AB}\ne0.
}
\]

Hence the simultaneous assumptions

\[
\mathcal A_E
=
\frac{s_E}{2}n_{AB}\omega^{AB},
\]

\[
\eta\widehat U_Lf'(1)\ne0,
\]

\[
q^\mu n_{AB}\ne0,
\]

and

\[
T^A=0
\]

are incompatible.

The torsion-free branch survives only on a zero-current surface such as

\[
\eta=0,
\]

or

\[
\widehat U_L=0,
\]

or

\[
f'(1)=0,
\]

or

\[
q^\mu n_{AB}=0.
\]

For the nontrivial positive projector branch these are not the intended generic conditions.

## 9. Correct route: Einstein–Cartan extension

A nontrivial Euler–Palatini phase adapter therefore belongs to the Einstein–Cartan/torsional extension branch already separated by RF-E21.

The structural chain is

\[
\boxed{
\mathcal A_E[\omega]
\to
\mathcal C_\vartheta
\to
\mathfrak s^\mu{}_{AB}
\to
\tau^{(E)}_{AB}
\to
T^A
}
\]

rather than

\[
\boxed{
\mathcal A_E[g]
\to
R^{(E)}_{\mu\nu}
}
\]

on the first-order branch.

This is the mathematically proper location for a genuine torsional/vortical gravitational mechanism.

## 10. Why RF-F22's metric-response threshold cannot be reused directly

The RF-F22 threshold

\[
\frac{R_0+3R_s}{\mu_\vartheta^2}
+
(S_0+3S_s)
<
-\frac12
\]

belongs to the metric/projector response ledger.

On the Palatini Euler branch,

\[
R^{(E)}_{\mu\nu}=0
\]

at fixed independent connection.

The new physical effect enters instead through the connection equation and torsion.

Therefore the RF-F22 acceleration threshold is not the acceleration test for this branch.

One must first solve or integrate out the Cartan torsion and then derive the resulting effective homogeneous/isotropic Einstein source.

## 11. Second-order Levi-Civita substitution firewall

One may alternatively solve the source-free/minimal Cartan equation first and substitute

\[
\omega=\omega[E].
\]

Then

\[
\mathcal A_E
=
\mathcal A_E[E,\partial E]
\]

contains derivatives of the coframe.

In that second-order representation the matter interaction depends on metric/coframe derivatives.

Therefore the algebraic formula

\[
T_{\mu\nu}
=
-2\frac{\partial\mathcal L}{\partial g^{\mu\nu}}
+
g_{\mu\nu}\mathcal L
\]

is insufficient.

The correct object is the full functional derivative

\[
\boxed{
T_{\mu\nu}
=
-\frac{2}{\sqrt{-g}}
\frac{\delta S}{\delta g^{\mu\nu}}.
}
\]

Hence a nonzero second-order Euler metric response requires a new variational gate including derivative terms and boundary handling.

It cannot be inserted into RF-F20 by replacing the open \(R^{(E)}_{\mu\nu}\) with an ad hoc number.

## 12. No-double-counting rule

The Levi-Civita connection already appears in the RF-E21 Einstein–Hilbert gravitational action.

A new Euler phase coupling is legitimate only as an explicit additional matter/phase coupling

\[
S_{int}[q(\omega),E,\ldots].
\]

Its variation must then be included in the Cartan/coframe equations exactly once.

The existence of gravitational spin connection in the Einstein–Hilbert action alone does not create an extra Euler projector source.

## 13. Current verdict

The candidate identification

\[
\boxed{
\mathcal A_E
=
\frac{s_E}{2}n_{AB}\omega^{AB}
}
\]

does produce a rigorous new result:

\[
\boxed{
\text{Palatini metric variation}
\Rightarrow
R^{(E)}_{\mu\nu}=0
}
\]

while

\[
\boxed{
\text{connection variation}
\Rightarrow
\mathfrak s^\mu{}_{AB}
=
\frac{
2\eta\widehat U_Ls_Ef'(1)
}{\mu_\vartheta^2}
q^\mu n_{AB}
}
\]

on the projector surface.

Therefore a nontrivial Euler/spin adapter generically sources Cartan torsion and leaves the minimal torsion-free GR branch.

Open gates:

- Lorentz-to-\(U(1)\) reduction selected by \(n_{AB}\);
- physical choice/dynamics of \(n_{AB}\);
- Einstein–Cartan solution for the induced torsion;
- effective stress after eliminating torsion;
- FLRW/isotropy reduction;
- sign of the resulting acceleration term;
- observational constraints.

Reference validator:

TIR/validation/tir_idt_rfc_euler_palatini_torsion_source_v0_1.py
