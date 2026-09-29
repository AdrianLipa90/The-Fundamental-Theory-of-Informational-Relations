# TIR × PhaseNav Moire/Bivector36 ADM–Curvature Crosswalk v0.1

**Date:** 2026-09-26  
**Status:** CROSS_REPO_STRENGTHENING / EXACT_KINEMATIC_AND_LINEAR_BRIDGES / NONLINEAR_FIREWALL / PHYSICAL_SOURCE_BINDING_OPEN

## 1. Purpose

This file imports only the mathematically validated consequences of the
2026-09-26 PhaseNav/NOEMA continuum-to-curvature stack.

It does not replace the existing TIR gravity chain and does not promote any
previously open physical source gate.

Pinned upstream evidence:

- AdrianLipa90/noema-phasenav-core
- branch: formalism/nonlinear-coframe-incompatibility-firewall-v0.1-20260926
- head: 7eb6f0e37a27c1d3e2f0b5c2bdda666ad36b91d2

The upstream branch contains, in linear ancestry:
- typed Moire/Bivector36 orbital calibration;
- GL(3) deformation carrier;
- continuum hyperelastic and defect dynamics;
- finite-strain multiplicative plasticity;
- GL(4) exterior-square coframe representation;
- Lorentz holonomy and shrinking-loop field strength;
- Cartan-to-Riemann analytic reference;
- Einstein geometric reference and source firewall;
- typed ADM coframe adapter;
- independent string-dust source reference;
- Saint-Venant / linearized Einstein identity;
- nonlinear raw-Curl curvature firewall.

## 2. Exact flow-coframe agreement with existing TIR convention

Existing TIR flow coframe:

\[
e^0=c\,d\tau,\qquad
e^i=dX^i-V^i d\tau.
\]

The typed ADM coframe is

\[
e^0=N\,d\tau,\qquad
e^a=E^a{}_i(dX^i+\beta^i d\tau).
\]

Set

\[
\boxed{N=c,\qquad E=I,\qquad \beta=-V}.
\]

Then

\[
ds^2
=
-c^2d\tau^2
+
\delta_{ij}(dX^i-V^i d\tau)(dX^j-V^j d\tau),
\]

exactly the existing TIR flow metric.

Equivalently, using \(x^0=c\tau\),

\[
\boxed{N=1,\qquad b=-V/c},
\]

which agrees with the existing TIR inter-leaf shift convention.

Status:

TIR_FLOW_COFRAME_TO_TYPED_ADM = PASS_EXACT_KINEMATIC.

This does not determine \(V\) from the microscopic orbital source.

## 3. Spatial GL(3) carrier as a typed triad sector

The PhaseNav spatial deformation carrier is

\[
F\in GL^+(3),
\]

with exterior-square representation

\[
\Lambda^2\operatorname{diag}(1,F)
=
\operatorname{diag}(F,\operatorname{cof}F).
\]

The typed ADM bridge permits

\[
E=F
\]

only when the array is explicitly admitted in the role SPATIAL_TRIAD.

Then

\[
h=E^T E=F^T F.
\]

For

\[
N=1,\qquad \beta=0,
\]

the 4D Bivector36 carrier reduces exactly to the earlier spatial GL(3) carrier.

Status:

TIR_GL3_TO_TIME_GAUGE_COFRAME = PASS_EXACT_TYPED_KINEMATICS.

No generic PhaseNav T36 vector is promoted to a spacetime triad.

## 4. Compatible-deformation flatness firewall

If

\[
E=\nabla y
\]

is literally a smooth compatible Euclidean deformation gradient, then

\[
h=E^T E=y^*\delta.
\]

Therefore the induced intrinsic spatial geometry is flat.

Hence a curved spatial metric cannot be obtained merely by renaming a
compatible Euclidean deformation gradient as a spacetime triad.

Status:

TIR_COMPATIBLE_DEFORMATION_TO_INTRINSIC_CURVATURE = NO_GO.

A curved triad requires incompatible/nonintegrable structure, an independent
connection/background geometry, or a different physical role for the array.

## 5. Exact Saint-Venant / linearized Einstein bridge

With row-wise Curl

\[
(\operatorname{Curl}A)_{ij}
=
\epsilon_{jkl}\partial_kA_{il},
\]

define

\[
\operatorname{inc}\varepsilon
=
\operatorname{Curl}
\bigl[(\operatorname{Curl}\varepsilon)^T\bigr].
\]

For the linearized spatial metric

\[
h_{ij}
=
\delta_{ij}+2\varepsilon_{ij},
\]

the exact first-order identity is

\[
\boxed{
G_{ij}^{(1)}
=
\operatorname{inc}\varepsilon_{ij}
}.
\]

For compatible total distortion

\[
\beta=\nabla u=\beta_e+\beta_p,
\]

with

\[
\varepsilon_e=\operatorname{sym}\beta_e,
\qquad
\alpha=\operatorname{Curl}\beta_p,
\]

the same convention gives

\[
\boxed{
G^{(1)}[\varepsilon_e]
=
-\operatorname{sym}\operatorname{Curl}(\alpha^T)
}.
\]

Status:

TIR_SAINT_VENANT_LINEARIZED_EINSTEIN = PASS_EXACT.

This is a geometry/continuum identity, not a physical statement that defects
are gravity.

## 6. Nonlinear raw-Curl curvature firewall

The exact linear bridge cannot be extrapolated by replacing nonlinear
curvature with raw \(\operatorname{Curl}E\).

Counterexample A:

\[
E(x,y)=R_z(\theta(x,y)).
\]

Then

\[
E^TE=I
\]

and the metric is exactly flat, while generally

\[
\|\operatorname{Curl}E\|^2
=
\theta_x^2+\theta_y^2
\neq0.
\]

The corresponding torsion-free spin connection is

\[
\omega=-J_z\,d\theta
\]

with

\[
\Omega=d\omega+\omega\wedge\omega=0.
\]

Counterexample B:

\[
E=\operatorname{diag}(e^\sigma,e^\sigma,1),
\qquad
\sigma=a(x^2+y^2).
\]

At the origin,

\[
\operatorname{Curl}E=0,
\]

but for \(a\neq0\),

\[
R=-8a
\]

there.

Therefore raw coframe Curl is neither sufficient nor pointwise necessary for
intrinsic curvature.

Status:

TIR_RAW_COFRAME_CURL_EQUALS_CURVATURE = NO_GO.

The existing TIR Levi-Civita/teleparallel firewall remains unchanged.

## 7. GL(4) / Bivector36 representation strengthening

For

\[
A\in GL(4),
\]

the upstream representation is

\[
\rho_{36}(A)=\Lambda^2 A.
\]

Exact identities:

\[
\Lambda^2(AB)
=
\Lambda^2(A)\Lambda^2(B),
\]

\[
\det(\Lambda^2A)=\det(A)^3.
\]

The exact inverse ambiguity is

\[
\boxed{
\Lambda^2(-A)=\Lambda^2(A)
}.
\]

Thus a Bivector36-to-coframe inverse carries an unavoidable
\(\mathbb Z_2\) ambiguity unless an independent orientation/time-orientation
witness is supplied.

Status:

TIR_BIVECTOR36_GL4_Z2_KERNEL = PASS_EXACT.

## 8. Lorentz holonomy and curvature reference strengthening

The upstream stack separately validates:

\[
H_{\rm pure\ gauge}=I
\]

for vertex-frame coboundary links,

and for a Lorentz connection

\[
F_{\mu\nu}
=
\partial_\mu A_\nu
-
\partial_\nu A_\mu
+
[A_\mu,A_\nu],
\]

the declared shrinking plaquette satisfies

\[
\frac{H(h)-I}{h^2}
\to
F_{\mu\nu}.
\]

A torsion-free analytic coframe reference then verifies

\[
e
\to
\omega
\to
\Omega
\to
R^\rho{}_{\sigma\mu\nu}
\]

against an independent metric/Christoffel calculation.

Status:

TIR_LORENTZ_SMALL_LOOP_CURVATURE_REFERENCE = PASS.

TIR_CARTAN_TO_RIEMANN_REFERENCE = PASS.

These reference results strengthen representation and validation surfaces; they
do not establish a production spacetime realization.

## 9. Independent source reference

An independently typed source family is available as a control:

static straight string dust aligned with \(z\),

\[
T_{\mu\nu}
=
\operatorname{diag}(\rho,0,0,-\rho).
\]

For the validated quadratic-conformal reference,

\[
G_{\mu\nu}
=
\operatorname{diag}(-q,0,0,q),
\qquad
q=4ae^{-2\sigma},
\]

and with \(\Lambda=0\),

\[
G_{\mu\nu}
=
\kappa_E T_{\mu\nu}
\]

requires

\[
\boxed{
\rho
=
-\frac{4a}{\kappa_E}e^{-2\sigma}
}.
\]

For positive \(\kappa_E\), positive source density therefore requires \(a<0\).

The matched source is covariantly conserved on the static reference but is not
globally localized on an infinite transverse plane.

Status:

TIR_STRING_DUST_SOURCE_REFERENCE = PASS_CONDITIONAL_LOCAL_REFERENCE.

This does not identify the TIR informational source with string dust.

## 10. Reconciliation with existing TIR open gates

The new results do not close:

SOURCE_TO_DIMENSIONLESS_RAPIDITY_BINDING  
ORBITAL_RECURSION_TO_UNIQUE_PHYSICAL_COFRAME  
DYNAMICAL_FIELD_EQUATION_FOR_V_FO  
PRODUCTION_BETA_MATCH  
PRODUCTION_EVENT_SPATIAL_REALIZATION  
COSMOLOGICAL_DIMENSIONFUL_SCALE/RHO_CRIT_BINDING  
TEMPORAL_U1_TO_LOCAL_ABE_RESPONSE_BINDING

They sharpen those gates by ruling out several invalid shortcuts.

In particular:

- a 36-coordinate shape match is not a coframe binding;
- a generic PhaseNav runtime vector is not production spacetime input;
- raw coframe Curl is not nonlinear curvature;
- shifting source terms between matter and Lambda channels is not new physics;
- defining \(T=(G+\Lambda g)/\kappa_E\) is not source evidence;
- a physical source-to-coframe claim still requires source-owned realization
  data and calibration.

## 11. Updated narrow frontier

The gravity frontier can now be stated more narrowly:

\[
\boxed{
\text{source-owned orbital/IDT event data}
\to
\text{typed }(N,\beta,E)
\to
\text{production coframe}
\to
\text{curvature/ADM observables}
\to
\text{independent }T_{\mu\nu}
\to
\text{empirical gravity tests}
}
\]

The mathematical adapters and negative controls are increasingly closed.

The physical realization inputs remain open.

canon_allowed = false.
