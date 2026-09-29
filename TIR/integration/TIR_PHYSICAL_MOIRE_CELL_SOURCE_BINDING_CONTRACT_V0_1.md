# TIR Physical Moire Cell Source-Binding Contract v0.1

Date: 2026-09-26
Status: EXECUTABLE_FAIL_CLOSED_CONTRACT / PHYSICAL_INPUT_OPEN / ANTI_CIRCULARITY_ACTIVE

## 1. Purpose

This contract turns the remaining Moire/MUMMU-to-TIR scale gap into one
machine-checkable physical input surface.

It does not infer a physical cell from a mathematical resemblance.

The contract has two logically separate channels:

1. calibration channel: establish the physical MUMMU/Moire cell period \(a_M\);
2. validation channel: test at least one independent observable predicted from
   that cell.

The same source digest may not occupy both channels.

## 2. Calibration channel

A calibration packet declares one physical realization and one immutable source
digest.

The cell period may be supplied directly,

\[
a_M>0,
\]

or reconstructed from independently supplied Moire wavelength and twist,

\[
\boxed{
a_M
=
2L_M\sin(|\delta\theta|/2).
}
\]

Inputs are SI:

- \(a_M\) in metres;
- \(L_M\) in metres;
- \(\delta\theta\) in radians.

If both direct and reconstructed values are present, the contract reports their
consistency defect rather than silently choosing one.

The calibration role is explicitly

MUMMU_PHASE_CLOCK_CELL_CANDIDATE.

This role declaration is a physical hypothesis carried by the receipt.

## 3. Conditional prediction constants

The exact combined RF-S4/RF-S8/TIR ratio is

\[
C_{\Delta/FS}
=
\frac8{9\sqrt3\pi},
\]

\[
Q_{\Delta/FS}
=
C_{\Delta/FS}^{-1/3}
=
1.82931154035502,
\]

\[
\hat a_\Delta
=
\sqrt{\frac83},
\]

and

\[
\boxed{
\gamma_{\Delta M}
=
\hat a_\Delta Q_{\Delta/FS}
=
2.98725323630302.
}
\]

Given \(a_M\), the conditional candidate surface predicts:

### TIR tetrahedral edge

\[
\boxed{
L_\Delta^{pred}
=
\gamma_{\Delta M}a_M.
}
\]

### physical phase-clock / KG angular frequency

\[
\boxed{
\omega_\varphi^{pred}
=
\frac{c}{a_M}.
}
\]

### inverse-length mass coordinate

\[
\boxed{
m_I^{pred}
=
\frac1{a_M}.
}
\]

### SI rest mass

\[
\boxed{
M_I^{pred}
=
\frac{\hbar}{ca_M}.
}
\]

### SI rest energy

\[
\boxed{
E_I^{pred}
=
\frac{\hbar c}{a_M}.
}
\]

These predictions are conditional on the common-mode physical bindings. They
are not current empirical claims.

## 4. Independent validation channels

At least one validation channel must be supplied from an immutable source
digest different from the calibration source digest.

Supported channels:

### TIR_TETRA_EDGE

Observed \(L_\Delta\) in metres.

Dimensionless test coordinate:

\[
\boxed{
R_\Delta
=
\frac{L_\Delta}{a_M}.
}
\]

Conditional target:

\[
R_\Delta=\gamma_{\Delta M}.
\]

### PHASE_FREQUENCY

Observed angular frequency \(\omega_\varphi\) in rad/s.

Dimensionless test coordinate:

\[
\boxed{
R_\omega
=
\frac{\omega_\varphi a_M}{c}.
}
\]

Conditional target:

\[
R_\omega=1.
\]

### REST_MASS

Observed rest mass \(M\) in kilograms.

Dimensionless test coordinate:

\[
\boxed{
R_M
=
\frac{Mca_M}{\hbar}.
}
\]

Conditional target:

\[
R_M=1.
\]

The validator reports residuals and, where uncertainties are supplied,
first-order propagated z-scores.

The contract does not retune any theorem constant to improve agreement.

## 5. Anti-circularity firewall

For every validation observable,

\[
\boxed{
SHA_{validation}
\neq
SHA_{calibration}.
}
\]

A validation source may not be the same immutable source record used to define
\(a_M\).

This prevents one measured quantity or one transformed copy of it from serving
as both the calibration and the validation.

For production packets, the realization ID and immutable source digests are
mandatory.

## 6. Direct versus Moire-derived calibration

If \(a_M\), \(L_M\), and \(\delta\theta\) are all supplied, define

\[
a_M^{moire}
=
2L_M\sin(|\delta\theta|/2).
\]

The validator reports

\[
\boxed{
\Delta_a
=
\frac{|a_M-a_M^{moire}|}
{\max(a_M,a_M^{moire})}.
}
\]

If uncertainties are available it also reports the propagated z-score.

This is a calibration-consistency diagnostic, not an averaging rule.

## 7. Production firewall

The following are rejected as production substitutes:

- a synthetic fixture;
- a generic NOEMA or PhaseNav state vector;
- a repository constant without a physical source receipt;
- a MUMMU model parameter with no laboratory/observational provenance;
- a fitted adapter selected using the validation target;
- the same immutable source digest in calibration and validation.

Reference and candidate fixtures may be validated structurally but are labeled
non-production.

## 8. Required packet fields

Top-level:

- schema;
- physical_realization_id;
- source_class;
- calibration;
- validations.

Calibration:

- source_ref;
- source_sha256;
- role;
- one of:
  - a_m_m;
  - l_m_m plus twist_rad;
- optional uncertainties.

Each validation:

- kind;
- source_ref;
- source_sha256;
- same_physical_mode = true;
- value;
- optional uncertainty.

## 9. Contract output

The executable validator emits:

- structure_status;
- production_status;
- calibrated \(a_M\);
- calibration consistency diagnostics;
- exact prediction constants;
- predicted \(L_\Delta,\omega_\varphi,M_I,E_I\);
- one residual record per independent validation;
- anti-circularity status;
- open physical-binding flags.

A structurally valid packet is not automatically empirical confirmation.

## 10. Open gates after this contract

MUMMU_PHYSICAL_CELL_REALIZATION  
SAME_PHYSICAL_MODE_BINDING  
RADIAL_INFORMATION_SOURCE_BINDING  
PHYSICAL_JOINT_INFORMATION_STATE_BINDING  
COMMON_RELATIONAL_AREA_SOURCE_BINDING  
TIR_RFC_CELL_CHART_SOURCE_BINDING  
TRANSLATIONAL_OBSERVABLE  
GENERAL_MATTER_MULTIPLET

The contract only makes the missing evidence executable and fail-closed.

canon_allowed = false.
