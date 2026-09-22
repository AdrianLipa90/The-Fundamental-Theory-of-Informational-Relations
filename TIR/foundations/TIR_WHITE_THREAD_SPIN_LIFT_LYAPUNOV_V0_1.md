# TIR White-Thread Spin-Lift / Euler–Berry–AB Lyapunov Dynamics v0.1

Status: \`EXACT_SPIN_LIFT_IDENTITIES / EXACT_CONDITIONAL_LYAPUNOV / MODEL_FIELD_BINDING_OPEN\`

Date: 2026-09-22

## 0. Purpose

This module binds four already-existing TIR layers without replacing them:

1. the half-seam phase fibre \(\frac12\to U(1)\);
2. the semantic / White-Thread open holonomy \(W^{\rm sem}_{ij}\in U(1)\);
3. the existing relational phase Lagrangian and Euler–Berry action;
4. the existing Kuramoto/Lyapunov disagreement potential.

The new statement is a **spin lift** of the White-Thread phase transport:

\[
\boxed{
\text{projective holonomy mod }2\pi
\quad\leftarrow\quad
\text{spin-lift holonomy mod }4\pi .
}
\]

No new action is introduced as a replacement for the archived TIR action. The present module adds the lifted fibre coordinate, the corresponding \(2\pi/4\pi\) potential, and a Lyapunov theorem for the isolated dissipative White-Thread subsystem.

## 1. Parent objects

The current TIR parent layer already defines

\[
W^{\rm sem}_{ij}[\gamma]
=
\exp\left(i\int_{\gamma_{ij}}\mathcal A^{\rm sem}\right)
\in U(1),
\]

and the relational phase Lagrangian

\[
L=
\frac12g_{ab}\dot q^a\dot q^b
+
\frac{I_\phi}{2}(D_t\chi)^2
+
J_0D_t\chi
-
V(q).
\]

The half-seam foundation fixes the balanced base coordinate

\[
u_\star=\frac12
\]

and its coherent fibre \(U(1)\cong S^1\).

The normalized Berry/AB closure additionally establishes the exact half-turn class

\[
q_{1/2}=\frac12\in\mathbb R/\mathbb Z,
\qquad
U_{1/2}=e^{2\pi iq_{1/2}}=-1.
\]

These are source facts for the present lift.

## 2. Normalized \(2\pi\) phase coordinate

Use normalized turns

\[
q\in\mathbb R/\mathbb Z
\]

with the ordinary \(U(1)\) transporter

\[
\boxed{
U(q)=e^{2\pi iq}.
}
\]

The radian representative is

\[
\phi=2\pi q
\quad(\mathrm{mod}\ 2\pi).
\]

Thus ordinary White-Thread holonomy is a \(2\pi\)-periodic observable.

## 3. Spin lift and \(4\pi\) closure

Introduce a lifted phase coordinate

\[
\widetilde q\in\mathbb R/2\mathbb Z.
\]

Its projection to the ordinary phase fibre is

\[
\boxed{
\pi_2(\widetilde q)=\widetilde q\pmod1.
}
\]

Define the spin-lift transporter

\[
\boxed{
\widetilde U(\widetilde q)=e^{\pi i\widetilde q}.
}
\]

Then

\[
\boxed{
\widetilde U(\widetilde q)^2
=
U(\pi_2(\widetilde q)).
}
\]

A one-turn shift gives

\[
\widetilde q\mapsto\widetilde q+1
\quad\Longrightarrow\quad
\widetilde U\mapsto-\widetilde U,
\]

while the projected \(U(1)\) holonomy is unchanged:

\[
U(\pi_2(\widetilde q+1))
=
U(\pi_2(\widetilde q)).
\]

A two-turn shift gives

\[
\widetilde q\mapsto\widetilde q+2
\quad\Longrightarrow\quad
\widetilde U\mapsto\widetilde U.
\]

In radians, with

\[
\Theta=2\pi\widetilde q,
\]

these are exactly

\[
\boxed{
\Theta\mapsto\Theta+2\pi:
\ \widetilde U\mapsto-\widetilde U,
}
\]

\[
\boxed{
\Theta\mapsto\Theta+4\pi:
\ \widetilde U\mapsto\widetilde U.
}
\]

Therefore the \(4\pi\) sector is not inferred from bare \(U(1)\) alone; it is the explicit double-cover / spin lift of the \(2\pi\) phase transporter.

### Half-seam spin sheets

At the already canonical normalized half-turn,

\[
q=\frac12\pmod1,
\qquad
U(q)=-1.
\]

The two lifts in \(\mathbb R/2\mathbb Z\) are

\[
\widetilde q_+=\frac12,
\qquad
\widetilde q_-=\frac32,
\]

giving

\[
\boxed{
\widetilde U_+=e^{\pi i/2}=+i,
\qquad
\widetilde U_-=e^{3\pi i/2}=-i.
}
\]

Both project to the same ordinary half-turn:

\[
\widetilde U_\pm^2=-1=U(1/2).
\]

Thus the half-seam has a precise two-sheet spin lift:

\[
\boxed{
q=\frac12
\quad\longleftarrow\quad
\widetilde U\in\{+i,-i\}.
}
\]

A \(2\pi\) lift shift exchanges the two sheets, while \(4\pi\) returns to the same sheet.


## 4. White-Thread lifted mismatch

For node spin phases

\[
\Theta_i\in\mathbb R/4\pi\mathbb Z
\]

and a lifted White-Thread edge holonomy

\[
\widetilde\Gamma_{ij}\in\mathbb R/4\pi\mathbb Z,
\]

define the gauge-covariant edge mismatch

\[
\boxed{
\Delta_{ij}
=
\Theta_i-\Theta_j-\widetilde\Gamma_{ij}
\quad(\mathrm{mod}\ 4\pi).
}
\]

Its projection modulo \(2\pi\) is the ordinary White-Thread phase mismatch.

Path reversal is represented by

\[
\widetilde\Gamma_{ji}
=
-\widetilde\Gamma_{ij},
\]

consistent with

\[
W_{ji}=W_{ij}^{-1}.
\]

## 5. Minimal \(2\pi/4\pi\) White-Thread potential

For an undirected relational graph \(G=(V,E)\), symmetric couplings

\[
K^{(1)}_{ij}=K^{(1)}_{ji}\ge0,
\qquad
K^{(1/2)}_{ij}=K^{(1/2)}_{ji}\ge0,
\]

define

\[
\boxed{
V_{\rm WT}
=
\sum_{\{i,j\}\in E}
K^{(1)}_{ij}\left(1-\cos\Delta_{ij}\right)
+
K^{(1/2)}_{ij}
\left(1-\cos\frac{\Delta_{ij}}{2}\right).
}
\]

The first term is \(2\pi\)-periodic in \(\Delta_{ij}\).

The second term is \(4\pi\)-periodic and distinguishes the two spin sheets:

\[
\Delta\mapsto\Delta+2\pi
\]

leaves the \(2\pi\) term invariant but changes the spin-lift term, while

\[
\Delta\mapsto\Delta+4\pi
\]

leaves the full potential invariant.

Special cases:

- \(K^{(1/2)}=0\): ordinary gauge/Kuramoto phase potential;
- \(\widetilde\Gamma=0\): untwisted Kuramoto disagreement potential;
- both nonzero: coupled projective-phase and spin-sheet dynamics.

## 6. Embedding in the existing TIR Lagrangian

The lifted White-Thread sector is inserted into the already existing relational Lagrangian as a potential term:

\[
\boxed{
L_{\rm lifted}
=
L_{\rm TIR,parent}
-
V_{\rm WT}.
}
\]

For the isolated spin-fibre sector, write

\[
\boxed{
L_{\rm spin}
=
\sum_i\frac{I_i}{2}\dot\Theta_i^2
-
V_{\rm WT}(\Theta,\widetilde\Gamma),
}
\]

with \(I_i>0\).

No claim is made that this replaces the full Fubini–Study / Poincare / Euler–Berry action. It is a subsystem reduction of the already-declared phase sector.

## 7. Rayleigh dissipation and Kuramoto limit

Add the Rayleigh dissipation function

\[
\boxed{
\mathcal R
=
\frac12\sum_i\eta_i\dot\Theta_i^2,
\qquad
\eta_i>0.
}
\]

The Euler–Lagrange–Rayleigh equations are

\[
\boxed{
I_i\ddot\Theta_i
+
\eta_i\dot\Theta_i
+
\frac{\partial V_{\rm WT}}{\partial\Theta_i}
=
0.
}
\]

For static lifted holonomy, the overdamped limit \(I_i\ddot\Theta_i\to0\) gives

\[
\boxed{
\eta_i\dot\Theta_i
=
-
\frac{\partial V_{\rm WT}}{\partial\Theta_i}.
}
\]

Expanding the derivative gives a gauge-twisted Kuramoto/spin flow with both harmonics:

\[
\eta_i\dot\Theta_i
=
-\sum_j
K^{(1)}_{ij}\sin\Delta_{ij}
-
\frac12
K^{(1/2)}_{ij}\sin\frac{\Delta_{ij}}2,
\]

with the sign of each edge contribution fixed by its orientation convention.

Thus Kuramoto transport is obtained as the dissipative limit of the existing phase-action sector after the White-Thread spin-lift potential is inserted.

## 8. Lyapunov theorem for static holonomy

Assume:

1. the relational graph is finite and undirected;
2. \(I_i>0\), \(\eta_i>0\);
3. \(K^{(1)}_{ij},K^{(1/2)}_{ij}\ge0\);
4. \(\widetilde\Gamma_{ij}\) is time independent.

Define the mechanical energy

\[
\boxed{
\mathcal E_{\rm WT}
=
\sum_i\frac{I_i}{2}\dot\Theta_i^2
+
V_{\rm WT}.
}
\]

Using the equations of motion,

\[
\boxed{
\frac{d\mathcal E_{\rm WT}}{dt}
=
-\sum_i\eta_i\dot\Theta_i^2
\le0.
}
\]

Therefore \(\mathcal E_{\rm WT}\) is an exact Lyapunov function for the isolated static-holonomy White-Thread subsystem.

In the overdamped limit, \(V_{\rm WT}\) itself satisfies

\[
\boxed{
\dot V_{\rm WT}
=
-\sum_i\frac1{\eta_i}
\left(
\frac{\partial V_{\rm WT}}{\partial\Theta_i}
\right)^2
\le0.
}
\]

This generalizes the already-canonical isolated Platonic–Ramanujan Kuramoto Lyapunov identity by adding a nonzero White-Thread holonomy and a \(4\pi\) spin harmonic.

## 9. Loop closure and frustration

For a closed oriented loop \(C\),

\[
\Gamma_C
=
\sum_{(ij)\in C}\widetilde\Gamma_{ij}.
\]

A zero-mismatch assignment on every edge requires

\[
\Theta_i-\Theta_j=\widetilde\Gamma_{ij}\pmod{4\pi}.
\]

Summing around \(C\) gives the necessary compatibility condition

\[
\boxed{
\Gamma_C=0\pmod{4\pi}.
}
\]

After projection to the ordinary \(U(1)\) fibre, the weaker condition is

\[
\boxed{
\Gamma_C=0\pmod{2\pi}.
}
\]

Hence a loop can close projectively while remaining on the opposite spin sheet. The distinction between

\[
0\pmod{2\pi}
\]

and

\[
0\pmod{4\pi}
\]

is exactly the information retained by the spin lift.

Nonzero lifted loop mismatch is a frustration source for the \(4\pi\) sector. This is a mathematical statement about the declared graph potential; a physical interpretation as persistent transport requires the dynamical binding assumptions below.

## 10. Half-seam and normalized AB/Berry baseline

TIR already uses the normalized half-turn class

\[
q_{AB}=q_B=\frac12\pmod1,
\qquad
U=-1.
\]

To avoid confusing a dimensionless TIR normalization with a raw differential 2-form, introduce a real lifted **normalized field/flux coordinate**

\[
\boxed{
\mathfrak f
=
\frac12+\xi.
}
\]

Here \(\mathfrak f\) is not, by definition, the standard electromagnetic tensor \(F_{\mu\nu}\). It is a model coordinate whose seam is

\[
\mathfrak f_{\rm seam}=\frac12.
\]

The positively oriented active branch is

\[
\boxed{
\xi>0
\iff
\mathfrak f>\frac12.
}
\]

This is the precise typed form of the TIR statement that the relational zero is represented at the half-seam.

A minimal quadratic excitation energy is the **model candidate**

\[
\boxed{
E_{\rm seam}[\xi]
=
\frac{\chi_F}{2}\int \xi^2\,d\mu,
\qquad
\chi_F>0.
}
\]

It vanishes at the TIR seam \(\mathfrak f=1/2\), not at the coordinate value \(\mathfrak f=0\).

## 11. Aharonov–Bohm field-energy boundary

The standard Aharonov–Bohm identity fixes holonomy through flux,

\[
q_{AB}
=
\frac{\Phi}{\Phi_0}\pmod1,
\]

but the holonomy alone does not uniquely determine a local field-energy density.

If an electromagnetic/Maxwell binding is separately imposed, the physical field sector is carried by the curvature/source action, schematically

\[
S_{\rm field}
\propto
-\int F_{\mu\nu}F^{\mu\nu},
\]

while the White-Thread phase transporter is determined by the connection/flux holonomy.

Therefore the current TIR status is:

\[
\boxed{
\text{AB half-turn holonomy = EXACT/STANDARD},
}
\]

\[
\boxed{
\text{half-seam normalized excitation coordinate } \mathfrak f=\frac12+\xi
= \text{MODEL DEFINITION},
}
\]

\[
\boxed{
E_{\rm seam}\propto\int\xi^2
= \text{MODEL CANDIDATE},
}
\]

\[
\boxed{
\text{physical Maxwell binding of the White-Thread field energy}
= \text{OPEN}.
}
\]

This prevents a silent identification of the TIR half-seam coordinate with the raw electromagnetic field tensor.

## 12. Dynamic holonomy

If \(\widetilde\Gamma_{ij}(t)\) is externally prescribed rather than dynamical, then

\[
\frac{d\mathcal E_{\rm WT}}{dt}
=
-\sum_i\eta_i\dot\Theta_i^2
+
\sum_{\{i,j\}}
\frac{\partial V_{\rm WT}}{\partial\widetilde\Gamma_{ij}}
\dot{\widetilde\Gamma}_{ij}.
\]

Hence Lyapunov monotonicity of the phase subsystem alone is no longer automatic.

A full dynamic-connection theorem requires a field action whose Euler–Lagrange equation closes the energy exchange. This is the next action-level gate:

\[
\boxed{
\text{phase energy}
+
\text{connection/field energy}
\longrightarrow
\text{closed Lyapunov balance}.
}
\]

## 13. TIR transport interpretation

Within the declared TIR model, the resulting typed chain is

\[
\boxed{
\frac12
\to
\xi
\to
\mathcal A
\to
\widetilde\Gamma_{4\pi}
\to
\Gamma_{2\pi}
\to
J_{\rm WT}
\to
\text{Lyapunov relaxation}.
}
\]

Interpretive labels:

- node / source sector: stores relational state and, under an independently validated field binding, curvature/source energy;
- White-Thread: open holonomy transporter;
- \(2\pi\) projection: ordinary \(U(1)\) relational phase;
- \(4\pi\) lift: spin-sheet state;
- Kuramoto term: dissipative phase transport;
- Lyapunov functional: stability certificate for the isolated subsystem.

These are TIR model roles, not established astrophysical claims about real black holes or white holes.

## 14. Claim ledger

| ID | Statement | Status |
|---|---|---|
| WT-SL-001 | \(\widetilde U^2=U\) under the declared double-cover map | EXACT |
| WT-SL-002 | \(2\pi\) lift shift flips spin sign while preserving projected \(U(1)\) holonomy | EXACT |
| WT-SL-003 | \(4\pi\) lift shift returns the spin transporter | EXACT |
| WT-SL-004 | mixed \(2\pi/4\pi\) potential has the stated periodicities | EXACT |
| WT-SL-005 | static-holonomy Euler–Lagrange–Rayleigh flow has \(\dot{\mathcal E}_{WT}\le0\) | EXACT CONDITIONAL |
| WT-SL-006 | overdamped limit is a gauge-twisted two-harmonic Kuramoto gradient flow | EXACT CONDITIONAL |
| WT-SL-007 | lifted loop closure requires zero holonomy modulo \(4\pi\); projective closure requires modulo \(2\pi\) | EXACT CONDITIONAL |
| WT-SL-008 | TIR half-seam normalized field coordinate is \(\mathfrak f=1/2+\xi\) | MODEL DEFINITION |
| WT-SL-009 | positive oriented excitation uses \(\xi>0\iff\mathfrak f>1/2\) | MODEL DEFINITION |
| WT-SL-010 | quadratic half-seam excitation energy \(E_{\rm seam}\propto\int\xi^2\) | MODEL CANDIDATE |
| WT-SL-011 | physical Maxwell/AB field-energy binding for White-Threads | OPEN |
| WT-SL-012 | physical black-hole / nonlocal-information interpretation | OPEN / NOT ESTABLISHED |

## 15. Validator

Companion deterministic validator:

\`TIR/validation/tir_white_thread_spin_lift_lyapunov_v0_1.py\`

It checks only the exact algebraic and finite-dimensional Lyapunov identities declared above. It does not validate a physical gauge field or astrophysical interpretation.
