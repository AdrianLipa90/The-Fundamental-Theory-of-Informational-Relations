# TIR Conditional Absolute Mass/Alpha Closure from Spatial Scale v0.1

Date: 2026-09-26
Status: EXACT_CONDITIONAL_CLOSURE / SOURCE_GATES_OPEN / NO_FIT

## 1. Parent surfaces

The following parent results are individually typed and must not be silently
collapsed.

### RF-S4 radial single-carrier surface

On the physically admitted zero-defect radial source-binding surface,

\[
\Delta_{A\Xi}=0,
\]

single-carrier action equivalence forces

\[
m_\Psi=m_I.
\]

For the same selected matter target, RF-S4 gives

\[
\boxed{
\rho_\omega=1,
\qquad
r_m=1.
}
\]

The physical radial-information source binding remains a separate gate.

### RF-S8 joint-action coefficient surface

On one physically admitted joint clock/radial information state with common
relational area and equivalent joint/decomposed action representations,

\[
\boxed{
\alpha_{clk}=\alpha_I,
\qquad
r_\alpha=1.
}
\]

The physical joint-state and common-area bindings remain separate gates.

### RF-S6 common cell-chart surface

If the normalized TIR tetrahedral cell and the RF-L5A premetric cell are
source-bound as the same physical cell,

\[
\boxed{
\Gamma_x=\ell_s,
\qquad
\sigma_x=1.
}
\]

The TIR/RFC cell-chart source binding remains a separate physical gate.

## 2. Exact conditional closure

RF-S2/RF-S4 give

\[
r_\alpha\rho_\omega^2\zeta_s^3
=
\frac{r_m}{C_{\Delta/FS}},
\]

where

\[
\zeta_s=m_I\ell_s
\]

and

\[
C_{\Delta/FS}
=
\frac8{9\sqrt3\pi}.
\]

On the simultaneous RF-S4 and RF-S8 surfaces,

\[
r_\alpha=\rho_\omega=r_m=1.
\]

Therefore

\[
\boxed{
(m_I\ell_s)^3
=
\frac1{C_{\Delta/FS}}
=
\frac{9\sqrt3\pi}{8}.
}
\]

Define

\[
Q_{\Delta/FS}
:=
C_{\Delta/FS}^{-1/3}
=
\left(\frac{9\sqrt3\pi}{8}\right)^{1/3}.
\]

Numerically,

\[
\boxed{
Q_{\Delta/FS}
=
1.82931154035502.
}
\]

Hence an independently calibrated spatial scale gives

\[
\boxed{
m_I
=
\frac{Q_{\Delta/FS}}{\ell_s}.
}
\]

RF-L4A then gives

\[
\boxed{
\alpha_I
=
\kappa_E m_I^2
=
\kappa_E
\frac{Q_{\Delta/FS}^2}{\ell_s^2}.
}
\]

Numerically,

\[
Q_{\Delta/FS}^2
=
3.34638071167607.
\]

Thus

\[
\boxed{
\alpha_I
=
3.34638071167607\,
\frac{\kappa_E}{\ell_s^2}
}
\]

on the fully admitted conditional surface.

No numerical parameter is fitted in these equations.

## 3. Physical KG frequency consequence

RF-L5A gives

\[
\omega_t^{KG}=c\,m_I.
\]

Therefore the same conditional surface predicts

\[
\boxed{
\omega_t^{KG}
=
\frac{cQ_{\Delta/FS}}{\ell_s}.
}
\]

Because RF-S4 also implies \(\rho_\omega=1\), the independently measured or
derived phase-clock line must satisfy

\[
\boxed{
|\omega_t^\varphi|
=
\frac{cQ_{\Delta/FS}}{\ell_s}.
}
\]

This is a direct falsification target once \(\ell_s\) and the physical phase
frequency are independently supplied.

Failure of the frequency equality falsifies the combined RF-S4/RF-S8 closure
surface rather than being repaired by retuning \(Q_{\Delta/FS}\).

## 4. Conditional conversion from an observed physical edge

The normalized tetrahedral spatial edge is

\[
\hat a_\Delta=\sqrt{8/3}.
\]

If an independent source adapter establishes

\[
L_\Delta^{phys}
=
\gamma_s a_{obs}
\]

for an observed physical edge \(a_{obs}\), then

\[
\ell_s
=
\frac{\gamma_s a_{obs}}{\hat a_\Delta}
=
\gamma_s a_{obs}\sqrt{3/8}.
\]

Substitution yields

\[
\boxed{
m_I
=
\frac{Q_{\Delta/FS}\hat a_\Delta}
{\gamma_s a_{obs}}.
}
\]

The dimensionless coefficient is

\[
Q_{\Delta/FS}\hat a_\Delta
=
2.98725323630302.
\]

Thus

\[
\boxed{
m_I
=
\frac{2.98725323630302}
{\gamma_s a_{obs}}
}
\]

in inverse-length units.

Physical rest-energy and rest-mass conversions are then

\[
E_I=\hbar c\,m_I,
\qquad
M_I=\frac{\hbar}{c}m_I.
\]

The coefficient \(\gamma_s\) is not supplied by the Moire residual and must be
source-owned.

## 5. Why a 2D Moire cell is not automatically the TIR tetrahedral cell

A planar Moire primitive cell and the TIR regular tetrahedral relation cell
have different typed geometry:

- Moire cell: two-dimensional lattice/reciprocal-lattice object;
- TIR tetrahedral cell: three-dimensional regular tetrahedral spatial
  relation carrier;
- FS tetrahedral object: projective CP1 area carrier.

The fact that all may feed a common Bivector36 or relational framework does not
supply an isometry between their physical cell edges.

Therefore

\[
L_M=L_\Delta
\]

or

\[
a_{lattice}=L_\Delta
\]

is not a theorem.

It is an additional physical adapter hypothesis.

Status:

MOIRE_2D_CELL_TO_TIR_TETRA_CELL = OPEN_SOURCE_BINDING.

## 6. Moire-compatible falsification route

The Moire calibration remains useful because it supplies exact operational
relations

\[
d_M=(a/L_M)^2
\]

and

\[
L_M=\frac{a}{2\sin(|\theta|/2)}.
\]

A future experiment/source receipt may therefore provide a physical
\(a_{obs}\), \(L_M\), and a declared mapping coefficient \(\gamma_s\).

The conditional closure then predicts a KG/phase frequency

\[
|\omega_t^\varphi|
=
\frac{cQ_{\Delta/FS}\hat a_\Delta}
{\gamma_s a_{obs}}.
\]

This prediction can be compared against an independently measured phase-clock
line.

The same data must not be used both to define \(\gamma_s\) and to validate the
frequency prediction.

## 7. Promotion status

Exact algebraic consequence:

CONDITIONAL_ABSOLUTE_MASS_CLOSURE = PASS_EXACT_GIVEN_PARENT_SURFACES.

Still open physically:

RADIAL_INFORMATION_SOURCE_BINDING  
PHYSICAL_JOINT_INFORMATION_STATE_BINDING  
COMMON_RELATIONAL_AREA_SOURCE_BINDING  
TIR_RFC_CELL_CHART_SOURCE_BINDING  
MOIRE_2D_CELL_TO_TIR_TETRA_CELL  
PHYSICAL_PHASE_CLOCK_FREQUENCY  
TRANSLATIONAL_OBSERVABLE  
GENERAL_MATTER_MULTIPLET

Validation-status caution:

- RF-S4 receipt: hosted CI pass with post-CI bookkeeping delta noted;
- RF-S8 receipt: hosted reference pass, final-head rerun pending;
- RF-S6 receipt: reference candidate, hosted CI pending.

Therefore this theorem is conditional algebra, not a canon promotion.

canon_allowed = false.
