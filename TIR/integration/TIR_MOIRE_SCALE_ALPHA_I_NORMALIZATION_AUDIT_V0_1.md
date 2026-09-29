# TIR x Moire Physical-Length / Alpha-I Normalization Audit v0.1

Date: 2026-09-26
Status: EXACT_SCALE_FIREWALL / MOIRE_ONLY_ALPHA_I_NO_GO / SPATIAL_ANCHOR_CONDITIONAL

## 1. Exact scale invariance

The calibrated homobilayer relation is

\[
d_M=4\sin^2(\theta/2)=(a/L_M)^2.
\]

For every \(s>0\),

\[
a\mapsto sa,\qquad L_M\mapsto sL_M
\]

leaves

\[
d_M\mapsto (sa/sL_M)^2=d_M.
\]

Therefore the Moire/Bivector36 residual and twist determine a ratio, not an
absolute length.

MOIRE_RESIDUAL_TO_ABSOLUTE_LENGTH = NO_GO_WITHOUT_DIMENSIONFUL_INPUT.

A measured lattice constant or Moire wavelength is an external physical input.

## 2. Conditional TIR spatial scale

The normalized TIR tetrahedral edge is

\[
\hat a_\Delta=\sqrt{8/3}.
\]

With physical TIR spatial scale \(\ell_s\),

\[
a_\Delta^{phys}=\ell_s\sqrt{8/3}.
\]

If and only if a source-owned adapter independently establishes

\[
a_\Delta^{phys}=\gamma_s a_{obs},
\]

then

\[
\boxed{\ell_s=\gamma_s a_{obs}\sqrt{3/8}}.
\]

The dimensionless \(\gamma_s\), or an equivalent cell identity, cannot be chosen
from the desired mass/clock result.

MOIRE_TO_TIR_SPATIAL_LENGTH = CONDITIONAL_SOURCE_BINDING.

## 3. RF-L5A spatial calibration

RF-L5A uses

\[
\Gamma_x=L_h/h.
\]

A source-owned physical Moire cell can supply \(L_h\) only after that physical
cell is identified with the selected premetric cell.

Even then the light-cone relation is

\[
M_{eff}\Gamma_x^2/\Gamma_t^2=c^2,
\]

and the mass slot is

\[
\mu_\lambda^2=\Gamma_t^2c^2m_I^2.
\]

Thus a known spatial length does not determine \(m_I\) unless the same mode has
independently fixed \(M_{eff}\), \(\Gamma_t\) and \(\mu_\lambda\).

## 4. Independent spectral route

RF-L5/RF-L5A give

\[
(\omega_t^{KG})^2=c^2m_I^2=c^2\alpha_I/\kappa_E.
\]

If an independently calibrated physical phase-clock line is shown to be the
same mode on the same physical time coordinate,

\[
\omega_t^{KG}=|\omega_{phase}|,
\]

then

\[
\boxed{
m_I=|\omega_{phase}|/c,\qquad
\alpha_I=\kappa_E(\omega_{phase}/c)^2.
}
\]

That would close the absolute normalization, but the current repository state
keeps INDEPENDENT_PHASE_KG_SPECTRAL_MATCH open.

## 5. RF-S1 coupling ratio

RF-L4A gives

\[
\boxed{\alpha_I=\kappa_E m_I^2}.
\]

RF-S1 separately defines

\[
\boxed{r_\alpha=\alpha_{clk}/\alpha_I}.
\]

Hence

\[
\boxed{\alpha_{clk}/\kappa_E=r_\alpha m_I^2}.
\]

Therefore \(\alpha_{clk}=\alpha_I\) is the separate specialization
\(r_\alpha=1\), not an automatic identity.

## 6. RF-S1 remains underdetermined

RF-S1 gives

\[
\boxed{
r_\alpha q_s^3=
\frac{r_m\mu_\varphi}{C_{\Delta/FS}}
}
\]

with

\[
q_s=\ell_s/\ell_\varphi,\qquad
\mu_\varphi=E_\varphi/m_I,\qquad
r_m=m_{target}/m_I,
\]

and

\[
C_{\Delta/FS}=\frac{8}{9\sqrt3\pi}.
\]

For every positive \(q_s,\mu_\varphi,r_m\),

\[
\boxed{
r_\alpha=
\frac{r_m\mu_\varphi}
{C_{\Delta/FS}q_s^3}
}
\]

satisfies the closure.

The equation therefore defines a constraint surface rather than a unique
absolute normalization.

MOIRE_SPATIAL_ANCHOR_TO_ALPHA_I_UNIQUENESS = NO_GO.

## 7. Typed kappas

The canonical information coefficient

\[
\kappa=\ln2/(24\pi)
\]

and the Einstein/source coupling \(\kappa_E\) are different typed quantities.
No Moire equation identifies them.

## 8. Exact advancement and remaining gates

The new Moire calibration can feed a physical spatial-scale slot after a
source-owned lattice/cell identity.

It does not by itself close:
- TIR tetrahedral physical-cell identity;
- phase-clock scale \(\ell_\varphi\);
- common-scale relation;
- \(r_\alpha\);
- \(\mu_\lambda\);
- independent phase/KG spectral match;
- \(m_I\);
- \(\alpha_I\);
- translational-observable selection;
- target mass binding.

Shortest non-circular routes are:

\[
\text{physical clock}\to\omega_{phase}
\to\omega_t^{KG}\to m_I\to\alpha_I,
\]

or

\[
\text{physical cell length}\to\Gamma_x
+\ M_{eff}\to\Gamma_t
+\ \mu_\lambda\to m_I\to\alpha_I.
\]

Current verdict:

MOIRE_SCALE_INVARIANCE = PASS_EXACT  
MOIRE_TO_SPATIAL_SCALE = CONDITIONAL_SOURCE_BINDING  
RF_S1_ALPHA_RATIO_EXPLICIT = PASS_EXACT  
MOIRE_ONLY_ALPHA_I_NORMALIZATION = NO_GO  
ABSOLUTE_ALPHA_I_NORMALIZATION = OPEN  
INDEPENDENT_PHASE_KG_SPECTRAL_MATCH = OPEN  
PHYSICAL_PROJECTIVE_CELL_SELECTION = OPEN

canon_allowed = false.
