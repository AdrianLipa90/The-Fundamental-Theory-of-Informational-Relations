# TIR × IDT × RFC Euler–Cartan Projector-Profile Identifiability Gate v0.1

Status: FIRST_DERIVATIVE_SPIN_CURRENT_INSUFFICIENT_FOR_TORSION_ELIMINATION / F_SECOND_DERIVATIVE_DEPENDENCE_EXACT / AFFINE_PROFILE_CONTROL_SOLVABLE / STRONG_COUPLING_DENOMINATOR_EXACT_CONDITIONAL / EFFECTIVE_EOS_NOT_YET_IDENTIFIED

Date: 2026-09-24

## 1. Purpose

RF-F17 fixes the projector normalization

\[
f(1)=1,
\]

and the dust-normalized candidate uses

\[
f'(1)=\frac12.
\]

The Euler–Palatini gate shows that \(f'(1)\) determines the local connection/spin current.

This gate asks whether those data are sufficient to eliminate the Cartan connection and derive an effective cosmological stress.

They are not.

The off-shell connection susceptibility also depends on

\[
\boxed{f''(1)}
\]

and, away from the projector surface, on the full profile \(f(C)\).

## 2. One-axis local control variable

Use the local reduced Euler connection amplitude \(h\) defined by the Cartan torsion solution

\[
T^0{}_{ij}
=
-h\,n_{ij}.
\]

On the local one-axis control branch the corresponding projected Euler connection changes the normal phase covector as

\[
\boxed{
q_0(h)
=
Q+\frac{s_E}{2}h,
}
\]

where \(Q\) contains all pieces independent of the varied Euler connection.

Define

\[
\boxed{
C(h)
=
\frac{q_0(h)^2}{\mu_\vartheta^2}.
}
\]

At the physical projector point

\[
C=1,
\]

write

\[
q_0
=
\varsigma_q\mu_\vartheta,
\qquad
\varsigma_q=\pm1.
\]

## 3. First derivative

Let

\[
a_E:=\frac{s_E}{2}.
\]

Then

\[
C'(h)
=
\frac{2a_Eq_0(h)}{\mu_\vartheta^2}.
\]

At \(C=1\),

\[
\boxed{
C'_*
=
\varsigma_q\frac{s_E}{\mu_\vartheta}.
}
\]

For

\[
\mathcal L_{int}
=
\eta\widehat U_Lf(C),
\]

the first derivative is

\[
\boxed{
\mathcal L'_{int,*}
=
\eta\widehat U_L
f'(1)
\varsigma_q
\frac{s_E}{\mu_\vartheta}.
}
\]

This is equivalent to the previously derived Euler spin-current amplitude.

## 4. Second derivative

The projector curvature is

\[
\boxed{
C''(h)
=
\frac{2a_E^2}{\mu_\vartheta^2}
=
\frac{s_E^2}{2\mu_\vartheta^2}.
}
\]

Therefore

\[
\mathcal L''_{int}
=
\eta\widehat U_L
\left[
f''(C)(C')^2
+
f'(C)C''
\right].
\]

At \(C=1\),

\[
\boxed{
\mathcal L''_{int,*}
=
\eta\widehat U_L
\frac{s_E^2}{\mu_\vartheta^2}
\left[
f''(1)
+
\frac12f'(1)
\right].
}
\]

For the normalized slope

\[
f'(1)=\frac12,
\]

this becomes

\[
\boxed{
\mathcal L''_{int,*}
=
\eta\widehat U_L
\frac{s_E^2}{\mu_\vartheta^2}
\left[
f''(1)+\frac14
\right].
}
\]

Thus the same physical projector value and the same first-order spin current do not determine the local connection susceptibility.

## 5. Explicit non-identifiability pair

Consider

\[
\boxed{
f_A(C)
=
\frac{1+C}{2}.
}
\]

Then

\[
f_A(1)=1,
\qquad
f_A'(1)=\frac12,
\qquad
f_A''(1)=0.
\]

Now define, for any real \(\lambda\),

\[
\boxed{
f_B(C)
=
\frac{1+C}{2}
+
\lambda(C-1)^2.
}
\]

Then

\[
f_B(1)=1,
\qquad
f_B'(1)=\frac12,
\]

but

\[
\boxed{
f_B''(1)=2\lambda.
}
\]

Hence both profiles give the same projector value and the same Euler spin current on \(C=1\), while their connection Hessians differ by

\[
\boxed{
\Delta\mathcal L''_{int,*}
=
2\lambda
\eta\widehat U_L
\frac{s_E^2}{\mu_\vartheta^2}.
}
\]

Therefore the torsion-eliminated action and its effective stress cannot be uniquely reconstructed from \(f(1)\) and \(f'(1)\) alone.

## 6. Constant-source gravitational control

For the local constant-source Cartan solution

\[
h=\kappa_E\sigma_E
\]

of the preceding gate, a flat Levi-Civita normal-frame control gives the Riemann–Cartan scalar correction

\[
\boxed{
\Delta R
=
-\frac12h^2
}
\]

for the declared connection/torsion convention.

Thus the local gravitational density contains

\[
\boxed{
\Delta\mathcal L_g
=
-\frac{h^2}{4\kappa_E}.
}
\]

This is a local constant-source control term. Derivatives of the contorsion and global boundary terms are separate on nonuniform branches.

## 7. Minimal affine-profile control

Take the minimal affine representative

\[
\boxed{
f_A(C)=\frac{1+C}{2}.
}
\]

Then

\[
\mathcal L_{int}
=
\frac{\eta\widehat U_L}{2}
\left[
1+
\frac{
\left(Q+\frac{s_E}{2}h\right)^2
}{\mu_\vartheta^2}
\right].
\]

Combining with

\[
\Delta\mathcal L_g=-\frac{h^2}{4\kappa_E},
\]

the stationary connection equation is

\[
-\frac{h}{2\kappa_E}
+
\eta\widehat U_L
\frac{s_E}{2\mu_\vartheta^2}
\left(
Q+\frac{s_E}{2}h
\right)
=
0.
\]

Define

\[
\boxed{
\gamma_E
:=
\frac{
\kappa_E\eta\widehat U_Ls_E^2
}{
2\mu_\vartheta^2
}.
}
\]

Then, for

\[
\gamma_E\neq1,
\]

the exact local solution is

\[
\boxed{
h
=
\frac{
\kappa_E\eta\widehat U_Ls_EQ
}{
\mu_\vartheta^2(1-\gamma_E)
}.
}
\]

The denominator

\[
\boxed{
1-\gamma_E
}
\]

is the exact affine-branch algebraic susceptibility factor.

## 8. Affine control on-shell action correction

Relative to the same local control at \(h=0\), completing the square gives

\[
\boxed{
\Delta\mathcal L_{\rm eff}^{aff}
=
\frac{
\kappa_E\eta^2\widehat U_L^2s_E^2Q^2
}{
4\mu_\vartheta^4(1-\gamma_E)
}.
}
\]

This is exact for the declared local affine-profile reduction.

It is not yet an equation of state.

The quantities \(Q,\mu_\vartheta,\widehat U_L\) can themselves depend on the matter/clock state and on the spacetime geometry outside the eliminated connection coordinate.

## 9. Strong-coupling / degeneracy surface

At

\[
\boxed{
\gamma_E=1,
}
\]

the quadratic connection coefficient vanishes in the local affine control.

The algebraic elimination becomes singular unless the linear source simultaneously vanishes.

This is a genuine degeneracy surface of the affine candidate, not a prediction that the physical system reaches it.

A viable physical projector profile must therefore be checked for:

- algebraic invertibility of the Cartan equation;
- sign/stability of the eliminated connection sector;
- absence of unacceptable strong-coupling regions.

## 10. EOS firewall

Even when

\[
\Delta\mathcal L_{\rm eff}
\]

is known, the cosmological pressure is not obtained merely by changing its sign.

The effective stress requires

\[
\boxed{
T_{\mu\nu}^{eff}
=
-\frac{2}{\sqrt{-g}}
\frac{\delta S_{\rm eff}}{\delta g^{\mu\nu}}.
}
\]

That variation must include the metric dependence of all surviving state variables and the coarse-grained spin statistics.

Therefore

\[
\boxed{
\text{positive/negative }\Delta\mathcal L_{\rm eff}
\not\Rightarrow
w=-1
}
\]

without the full metric variation.

## 11. Current verdict

The current stack determines the first-order Euler spin current but not the torsion-eliminated cosmological stress.

The missing information is now sharply identified:

\[
\boxed{
f''(1)\text{ / full }f(C)
}
\]

plus the physical state dependence of

\[
Q,\quad
\mu_\vartheta,\quad
\widehat U_L.
\]

The affine profile

\[
f_A=(1+C)/2
\]

is an exactly solvable control branch, not a promoted physical choice.

Reference validator:

TIR/validation/tir_idt_rfc_euler_cartan_projector_profile_identifiability_v0_1.py
