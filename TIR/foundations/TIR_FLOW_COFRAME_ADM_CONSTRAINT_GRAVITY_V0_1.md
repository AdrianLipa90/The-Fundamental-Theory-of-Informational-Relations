# TIR Flow-Coframe ADM Constraint Gravity Derivation v0.1

Status: CONDITIONAL_DYNAMICAL_DERIVATION / VACUUM_SPHERICAL_RIVER_PROFILE_DERIVED / FLAT_FLRW_HAMILTONIAN_CROSSWALK / SOURCE_TO_COFRAME_BINDING_OPEN

Date: 2026-09-24

Parent:
- TIR_FRACTAL_ORBITAL_INFORMATIONAL_HOLONOMIC_GRAVITY_V0_1
- existing TIR ADM/Einstein-form downstream gate, on its declared assumptions

## 1. Purpose

The parent fractal-orbital gravity gate established the flow coframe

\[
e^0=c\,dt,\qquad e^i=dX^i-V^i\,dt
\]

and used Schwarzschild--Painleve--Gullstrand and flat-FLRW metrics as exact controls.

This gate strengthens one part of that result. Conditional on the already-admitted ADM/Einstein constraint sector and on a stationary, spherically symmetric, unit-lapse, intrinsically flat spatial slicing, the vacuum Hamiltonian constraint derives

\[
\boxed{V^2(r)=\frac{C}{r}}.
\]

The integration constant is then fixed by the asymptotic Newtonian/ADM mass normalization,

\[
\boxed{C=2GM},
\]

so

\[
\boxed{V^2(r)=\frac{2GM}{r}}.
\]

This is a conditional spacetime dynamics derivation. It still does not derive the physical map from the microscopic TIR/orbital source to the coframe.

## 2. ADM flow metric

Use

\[
\boxed{ds^2=-c^2dt^2+\bigl(dr-V(r,t)dt\bigr)^2+r^2d\Omega^2}
\]

for the radial sector.

The spatial slices are Euclidean, \(^{(3)}R=0\), the lapse is unity, and the radial shift is the flow field.

For a stationary radial flow \(V=V(r)\), the mixed extrinsic-curvature eigenvalues are, up to one overall sign convention,

\[
\boxed{K^r{}_r=\frac{V'}{c},\qquad K^\theta{}_\theta=K^\phi{}_\phi=\frac{V}{cr}.}
\]

The overall sign drops out of the Hamiltonian constraint.

## 3. Vacuum Hamiltonian constraint

For vanishing matter density and cosmological constant,

\[
{}^{(3)}R+K^2-K_{ij}K^{ij}=0.
\]

With the eigenvalues above,

\[
K=\frac1c\left(V'+\frac{2V}{r}\right),
\]

\[
K_{ij}K^{ij}=\frac1{c^2}\left[(V')^2+2\frac{V^2}{r^2}\right].
\]

Hence

\[
\boxed{K^2-K_{ij}K^{ij}=\frac{2}{c^2}\frac{V}{r}\left(2V'+\frac Vr\right).}
\]

The nontrivial branch \(V\neq0\) therefore obeys

\[
2V'+\frac Vr=0.
\]

Multiplying by \(rV\),

\[
2rVV'+V^2=0,
\]

so

\[
\boxed{\frac{d}{dr}\left(rV^2\right)=0.}
\]

Therefore

\[
\boxed{V^2(r)=\frac Cr.}
\]

No Schwarzschild profile was inserted into this differential equation.

## 4. Mass normalization

The flow metric has

\[
g_{tt}=-(c^2-V^2).
\]

In the weak-field asymptotic regime,

\[
g_{tt}\simeq-c^2\left(1+\frac{2\Phi}{c^2}\right)=-c^2-2\Phi.
\]

Comparison gives \(V^2=-2\Phi\). For

\[
\Phi=-\frac{GM}{r},
\]

one obtains

\[
\boxed{C=2GM,\qquad V(r)=\pm\sqrt{\frac{2GM}{r}}.}
\]

The sign selects ingoing or outgoing Painleve--Gullstrand orientation; the metric coefficient \(V^2\) is unchanged.

Thus

\[
\boxed{\text{flow coframe}+\text{vacuum ADM constraint}+\text{spherical stationary flat slicing}+\text{mass normalization}\Longrightarrow\text{Schwarzschild PG river profile}.}
\]

## 5. Hyperbolic/orbital coordinate

The parent exact map gives

\[
\beta=\frac{|V|}{c}=\tanh\chi.
\]

Therefore on the exterior subluminal domain,

\[
\boxed{\tanh^2\chi(r)=\frac{2GM}{c^2r}.}
\]

This derives the required radial rapidity profile from the ADM vacuum constraint after the coframe-binding premise is admitted. It does not derive the microscopic source formula for \(\chi\).

## 6. Flat-FLRW Hamiltonian control

For \(\mathbf V=H(t)\mathbf R\), the flat spatial slice again has \(^{(3)}R=0\). The three mixed extrinsic-curvature eigenvalues are equal, up to sign,

\[
K^i{}_j=\frac{H}{c}\delta^i{}_j.
\]

Therefore

\[
K^2-K_{ij}K^{ij}=\frac{6H^2}{c^2}.
\]

With energy density \(\varepsilon\) and cosmological constant \(\Lambda\),

\[
{}^{(3)}R+K^2-K_{ij}K^{ij}=\frac{16\pi G}{c^4}\varepsilon+2\Lambda,
\]

so

\[
\boxed{H^2=\frac{8\pi G}{3c^2}\varepsilon+\frac{\Lambda c^2}{3}.}
\]

For \(\varepsilon=\rho_m c^2\),

\[
\boxed{H^2=\frac{8\pi G}{3}\rho_m+\frac{\Lambda c^2}{3}.}
\]

Thus the same flow coframe reproduces the standard flat-FLRW Hamiltonian equation once the existing gravitational field-equation gate is admitted.

## 7. Acceleration equation and mechanism firewall

The kinematic identity is

\[
\frac{D\mathbf V}{Dt}=(\dot H+H^2)\mathbf R=\frac{\ddot a}{a}\mathbf R.
\]

The standard acceleration equation is

\[
\boxed{\frac{\ddot a}{a}=-\frac{4\pi G}{3c^2}(\varepsilon+3p)+\frac{\Lambda c^2}{3}.}
\]

The present gate does not set \(\Lambda\) equal to an informational-holonomic quantity.

A TIR dark-energy-like mechanism would require a derived effective source or geometric correction whose coarse-grained contribution reproduces the observed acceleration while satisfying local gravity constraints. The holonomic/orbital source to effective stress-energy or equivalent geometric term remains OPEN.

## 8. Levi-Civita / teleparallel compatibility

The ADM derivation above belongs to the metric/Levi-Civita representation already selected in the TIR GR sector.

An equivalent teleparallel representation may describe the same metric with a distinct flat spin connection and nonzero torsion. No step in this derivation assigns both zero and nonzero torsion to the same connection.

The torsional/flow description is a representation crosswalk, not a new physical degree of freedom by itself.

## 9. Promotion ledger

- radial ADM extrinsic-curvature eigenvalues: PASS EXACT
- vacuum constraint reduction: PASS EXACT
- 2V'+V/r=0: PASS EXACT
- V^2=C/r: PASS EXACT
- C=2GM from mass normalization: PASS CONDITIONAL PHYSICAL NORMALIZATION
- Schwarzschild PG profile: PASS CONDITIONAL DERIVATION
- flat-FLRW Hamiltonian crosswalk: PASS STANDARD/CONDITIONAL
- source B omega N /(AR Lambda) to chi(x): OPEN
- orbital recursion to unique physical coframe: OPEN
- holonomic source of late acceleration: OPEN

The phrase gravity derived from TIR foundations is permitted only with an explicit qualifier: TIR has a closed internal spatial/Cartan/ADM chain and now a conditional flow-coframe derivation of the spherical vacuum river law. The microscopic physical source-to-coframe binding remains open.

## 10. Falsification surface

This gate fails if:
1. the ADM constraint algebra does not reduce to the stated ODE;
2. \(V^2=C/r\) fails the exact vacuum constraint;
3. a non-\(1/r\) power law passes the same nontrivial vacuum constraint without an added source;
4. the weak-field mass normalization does not recover \(C=2GM\);
5. the FLRW flow fails the standard Hamiltonian constraint;
6. the result is represented as closing the still-open microscopic source binding.

Reference validator:

TIR/foundations/validation/tir_flow_coframe_adm_constraint_gravity_v0_1.py
