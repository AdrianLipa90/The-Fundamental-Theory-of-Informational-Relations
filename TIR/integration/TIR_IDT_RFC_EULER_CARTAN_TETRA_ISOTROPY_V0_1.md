# TIR × IDT × RFC Euler–Cartan Local Torsion and Tetrahedral Isotropy Gate v0.1

Status: LOCAL_CARTAN_TORSION_SOLUTION_EXACT_CONDITIONAL / SINGLE_AXIS_FLRW_ISOTROPY_NO_GO / TETRAHEDRAL_FIRST_MOMENT_ZERO_EXACT / TETRAHEDRAL_SECOND_MOMENT_ISOTROPIC_EXACT / MACROSCOPIC_SPIN_SQUARED_STRESS_OPEN

Date: 2026-09-24

## 1. Purpose

The Euler–Palatini gate produces the local connection current

\[
\mathfrak s^\mu{}_{ab}
=
\frac{2\eta\widehat U_Ls_Ef'(1)}
{\mu_\vartheta^2}
q^\mu n_{ab}
\]

on the phase-projector surface.

The Bloch-axis reduction supplies

\[
n_{ab}
=
\epsilon_{abc}s^c,
\qquad
s^as_a=1.
\]

This gate solves the sourced Cartan equation locally for a normal-flow current and determines the isotropy status of the resulting torsion.

## 2. Normal-flow spin-current amplitude

Use an oriented local orthonormal coframe

\[
(E^0,E^1,E^2,E^3)
\]

with signature

\[
(-,+,+,+)
\]

and volume orientation

\[
\operatorname{vol}_4
=
E^0\wedge E^1\wedge E^2\wedge E^3.
\]

Let

\[
u=e_{\hat0}
\]

be the normal material/phase flow and write

\[
q^\mu
=
\varsigma_q\mu_\vartheta u^\mu,
\qquad
\varsigma_q\in\{+1,-1\}.
\]

Define the signed Euler spin-current amplitude

\[
\boxed{
\sigma_E
:=
\varsigma_q
\frac{
2\eta\widehat U_Ls_Ef'(1)
}{\mu_\vartheta}.
}
\]

Then

\[
\boxed{
\mathfrak s^\mu{}_{ab}
=
\sigma_Eu^\mu n_{ab}.
}
\]

## 3. Spin-current three-form convention

Define the spatial volume form

\[
V_3
:=
E^1\wedge E^2\wedge E^3.
\]

Use the local source convention

\[
\boxed{
\tau^{(E)}_{ab}
=
\sigma_E n_{ab}V_3,
\qquad
\tau^{(E)}_{0a}=0.
}
\]

The Cartan equation is normalized as in the preceding gate:

\[
\boxed{
\epsilon_{ABCD}
E^C\wedge T^D
=
\kappa_E\tau^{(E)}_{AB}.
}
\]

All results below are conditional on this explicitly declared source normalization.

## 4. Exact local torsion solution

Consider

\[
\boxed{
T^0
=
-\frac{\kappa_E\sigma_E}{2}
n_{ij}E^i\wedge E^j,
}
\]

\[
\boxed{
T^i=0.
}
\]

For a spatial pair \(a,b\), let \(c\) be its complementary oriented spatial index.

Since only \(T^0\) is nonzero,

\[
\epsilon_{abCD}E^C\wedge T^D
=
\epsilon_{abc0}E^c\wedge T^0.
\]

Substitution gives exactly

\[
\boxed{
\epsilon_{abCD}E^C\wedge T^D
=
\kappa_E\sigma_E n_{ab}V_3
=
\kappa_E\tau^{(E)}_{ab}.
}
\]

For \(AB=0a\), both sides vanish.

Therefore the displayed torsion is an exact solution of the local Cartan system.

## 5. Component form

With

\[
T^A
=
\frac12
T^A{}_{BC}
E^B\wedge E^C,
\]

the only nonzero components are

\[
\boxed{
T^0{}_{ij}
=
-\kappa_E\sigma_E n_{ij}
=
-\kappa_E\sigma_E\epsilon_{ijk}s^k.
}
\]

The torsion trace vanishes:

\[
\boxed{
T^B{}_{AB}=0.
}
\]

The quadratic contraction in the declared signature is

\[
\boxed{
T^A{}_{BC}T_A{}^{BC}
=
-2\kappa_E^2\sigma_E^2.
}
\]

This invariant is independent of the orientation of the unit axis.

## 6. Spatial dual torsion vector

Define the local spatial dual

\[
\boxed{
b^k
:=
\frac12
\epsilon^{kij}T^0{}_{ij}.
}
\]

Then

\[
\boxed{
b^k
=
-\kappa_E\sigma_Es^k.
}
\]

Thus the linear Euler torsion contains one distinguished spatial axis.

## 7. Single-axis FLRW isotropy no-go

An exactly homogeneous and isotropic FLRW background has no nonzero invariant spatial vector under the full local spatial rotation group.

But a nonzero single-axis Euler source gives

\[
\mathbf b
=
-\kappa_E\sigma_E\mathbf s
\neq0.
\]

Therefore

\[
\boxed{
\sigma_E\neq0
\ \land\
\text{one coherent spatial axis}
\quad\Longrightarrow\quad
\text{not exactly FLRW-isotropic}.
}
\]

This does not forbid anisotropic cosmology or local vortical/torsional structure.

It forbids treating one coherent Euler spin axis as an exactly isotropic dark-energy background.

## 8. Tetrahedral axis ensemble

Let the four regular tetrahedral unit directions be

\[
\mathbf s_A,
\qquad
A=1,2,3,4,
\]

with

\[
\mathbf s_A\cdot\mathbf s_B
=
-\frac13
\qquad
(A\neq B).
\]

They satisfy exactly

\[
\boxed{
\sum_{A=1}^4
\mathbf s_A
=
0,
}
\]

and

\[
\boxed{
\frac14
\sum_{A=1}^4
s_A^is_A^j
=
\frac13\delta^{ij}.
}
\]

For equal-magnitude microscopic Euler torsion vectors

\[
\mathbf b_A
=
-\kappa_E\sigma_E\mathbf s_A,
\]

the first moment is

\[
\boxed{
\langle b^i\rangle
=
0,
}
\]

while the second moment is

\[
\boxed{
\langle b^ib^j\rangle
=
\frac{\kappa_E^2\sigma_E^2}{3}
\delta^{ij}.
}
\]

Thus the regular tetrahedral set is an exact finite isotropic second-moment design for the Euler torsion axis.

## 9. Averaging firewall

The identities

\[
\langle b^i\rangle=0
\]

and

\[
\langle b^ib^j\rangle
\propto\delta^{ij}
\]

do not imply a nonzero macroscopic torsion field.

If the four sources cancel pointwise before solving the algebraic Cartan equation, the net torsion source is zero.

A nonzero isotropic macroscopic correction requires a microscopic/statistical coarse-graining in which nonlinear spin/torsion products survive:

\[
\boxed{
\langle b\rangle=0,
\qquad
\langle b\otimes b\rangle\neq0.
}
\]

This is the standard type of second-moment closure problem, but its physical realization must be derived for the present TIR/RFC carrier rather than assumed.

## 10. Consequence for the gravity mechanism

The current chain is now

\[
\boxed{
\text{Euler }U(1)\text{ reduced connection}
\to
\text{spin current}
\to
\text{Cartan torsion}
\to
\mathbf b\parallel\mathbf s.
}
\]

A single coherent axis naturally belongs to local/anisotropic vortex-like geometry.

The tetrahedral carrier supplies the exact finite geometry needed to remove the first-moment preferred direction while retaining an isotropic second moment.

The next dynamical gate is therefore

\[
\boxed{
\text{integrate out / coarse-grain Cartan torsion}
\to
T_{\mu\nu}^{\rm eff}[\langle b_ib_j\rangle]
}
\]

and determine its pressure and acceleration sign.

## 11. Verdict

Exact conditional:

\[
\boxed{
T^0
=
-\frac{\kappa_E\sigma_E}{2}
n_{ij}E^i\wedge E^j,
\qquad
T^i=0.
}
\]

Single-axis background:

\[
\boxed{
\text{FLRW isotropy FAIL unless }\sigma_E=0
}
\]

for a coherent axis.

Equal tetrahedral ensemble:

\[
\boxed{
\langle\mathbf b\rangle=0,
\qquad
\langle b^ib^j\rangle
=
\frac{\kappa_E^2\sigma_E^2}{3}\delta^{ij}.
}
\]

Open:

- microscopic coexistence/ensemble semantics of tetrahedral torsion carriers;
- action-level elimination of torsion;
- effective energy density and pressure;
- scaling with \(a(t)\);
- acceleration sign;
- observational anisotropy/perturbation constraints.

Reference validator:

TIR/validation/tir_idt_rfc_euler_cartan_tetra_isotropy_v0_1.py
