# TIR MUMMU Source Magnus-Order Theorem v0.1

Status: `EXACT_CUBIC_PROJECTIVE_CONNECTION_MAGNUS_DEFECT / NOT_SOURCE_HAMILTONIAN_MAGNUS_CLAIM / QUARTIC_SCALAR_PROJECTIVE_BINDING_FAIL / NUMERIC_SEXTIC_CHARACTER_SCALING / DISCRETE_QUARTIC_THEOREM_RETAINED`

Date: 2026-09-23

## 1. Purpose

The source-derived QHTRI pair trajectory induces a smooth horizontal/projective local connection

[
mathcal A(	au)
=
-rac{i}{2}
oldsymbolOmega(	au)cdotoldsymbolsigma.
]

The earlier MUMMU quartic-seam theorem used a different comparison: two finite
noncommuting pulse histories with the same integrated generator vector.

This theorem determines whether the smooth source-derived QHTRI connection has
the same leading order.

It does not.

## 2. Local expansion

At one admitted proper-time section,

[
mathcal A(	au)
=
A_0+	au A_1+O(	au^2).
]

The exact time-ordered transporter is

[
U(T)
=
mathcal P
exp
left(
int_0^Tmathcal A(	au),d	au
ight).
]

Let the first-Magnus/commutative surrogate be

[
U_1(T)
=
exp
left(
int_0^Tmathcal A(	au),d	au
ight).
]

The second Magnus term is

[
Omega_2(T)
=
rac12
int_0^Tdt_1
int_0^{t_1}dt_2
[
mathcal A(t_1),mathcal A(t_2)
].
]

Using

[
[
A_0+t_1A_1,,
A_0+t_2A_1
]
=
(t_2-t_1)[A_0,A_1],
]

one obtains

[
oxed{
Omega_2(T)
=
-rac{T^3}{12}
[A_0,A_1]
+
O(T^4).
}
]

Therefore the first history defect of this horizontal/projective connection is cubic at operator level.

## 3. SU(2) vector form

Write

[
A_0
=
-rac{i}{2}
oldsymbolOmega_0cdotoldsymbolsigma,
qquad
A_1
=
-rac{i}{2}
dot{oldsymbolOmega}_0cdotoldsymbolsigma.
]

Then

[
oxed{
[A_0,A_1]
=
-rac{i}{2}
left(
oldsymbolOmega_0
	imes
dot{oldsymbolOmega}_0
ight)cdotoldsymbolsigma.
}
]

Define

[
mathcal W_0
=
left|
oldsymbolOmega_0
	imes
dot{oldsymbolOmega}_0
ight|.
]

The Frobenius norm of the leading Magnus correction is therefore

[
oxed{
|Omega_2(T)|_F
=
rac{mathcal W_0}{12sqrt2}
T^3
+
O(T^4).
}
]

For the pinned PNCS witness,

[
mathcal W_0
approx
9.0284300874	imes10^{-4},
]

so

[
oxed{
rac{mathcal W_0}{12sqrt2}
approx
5.32005345	imes10^{-5}.
}
]

## 4. Why the scalar quartic term vanishes

The normalized (SU(2)) character depends on the rotation-vector magnitude.

The leading history correction vector is proportional to

[
oldsymbolOmega_0
	imes
dot{oldsymbolOmega}_0,
]

which is orthogonal to both
(oldsymbolOmega_0) and
(dot{oldsymbolOmega}_0).

Consequently the leading (T^3) Magnus correction does not produce a
(T^4) scalar-character correction through an inner product with the
leading (T) rotation vector.

Thus the smooth source-derived QHTRI trajectory does **not** inherit the
quartic scalar coefficient of the discrete two-pulse theorem.

The correct statement is

[
oxed{
	ext{quartic scalar source binding: FAIL}.
}
]

This does not invalidate the discrete quartic theorem.  It separates two
different history regimes.

## 5. Deterministic source scaling

For the pinned PNCS pair-0 trajectory, numerical path ordering gives

[
rac{|U(T)-U_1(T)|_F}{T^3}
]

approximately

[
egin{array}{c|c}
T & |U-U_1|_F/T^3\
hline
0.1 & 5.3873	imes10^{-5}\
0.2 & 5.4691	imes10^{-5}\
0.3 & 5.5665	imes10^{-5}
end{array}
]

approaching the local prediction

[
5.3201	imes10^{-5}
]

as (T	o0).

The scalar trace difference is much more suppressed.  Over the stable numerical
window,

[
oxed{
operatorname{Tr}U(T)
-
operatorname{Tr}U_1(T)
=
O(T^6)
}
]

for this pinned source trajectory.

Representative scaled values are

[
egin{array}{c|c}
T & [operatorname{Tr}U-operatorname{Tr}U_1]/T^6\
hline
0.2 & 9.12	imes10^{-10}\
0.3 & 9.34	imes10^{-10}\
0.4 & 9.69	imes10^{-10}\
0.5 & 1.01	imes10^{-9}
end{array}
]

within the declared numerical discretization.

## 6. Relation to the quartic-seam theorem

The existing result

[
K_{m seq}-K_{m const}
=
rac{alpha^2eta^2}{96}
+
O(6)
]

remains exact for its declared finite sequential-vs-constant-axis pulse
comparison.

The source-induced smooth horizontal/projective CP1 connection belongs to a different asymptotic class:

[
oxed{
	ext{smooth source history}
Rightarrow
	ext{cubic operator ordering defect}
}
]

while the scalar character does not acquire that discrete quartic term.

Therefore the previous combined seam

[
-rac1{108}C_4
+
rac{alpha^2eta^2}{96}
]

must not be presented as the leading source-bound smooth QHTRI seam.

## 7. Revised MUMMU seam ledger

Keep the two channels separate:

[
oxed{
mathfrak S_{m MUMMU}^{m source}
=
left(
C_4,,
mathcal W,,
mathcal D_{mathcal L}
ight).
}
]

Here:

- (C_4) is the quartic Stella geometric anisotropy;
- (mathcal W=|Omega	imesdotOmega|) is the local source-derived
  non-Abelian history witness;
- (mathcal D_{mathcal L}) is the loop/holonomy centrality defect.

No scalar weighting between them is introduced.

## 8. Claim ledger

| Statement | Status |
|---|---|
| second Magnus term is (-T^3[A_0,A_1]/12+O(T^4)) | `EXACT` |
| local SU(2) commutator vector is (Omega_0	imesdotOmega_0) | `EXACT` |
| operator defect is cubic | `EXACT` |
| predicted Frobenius cubic coefficient for pinned fixture | `EXACT FROM SOURCE WITNESS` |
| discrete two-pulse quartic theorem remains valid in its own scope | `EXACT` |
| same quartic scalar term is leading smooth-QHTRI source seam | `FAIL` |
| pinned source character difference is numerically consistent with (T^6) | `NUMERIC PASS` |
| physical neutrino/gravity realization | `OPEN / NOT CLAIMED` |

## 9. Validation

Deterministic validator:

`TIR/validation/tir_mummu_source_magnus_order_v0_1.py`

Static receipt:

`TIR/validation/TIR_MUMMU_SOURCE_MAGNUS_ORDER_VALIDATION_V0_1.json`


## 10. Operator-scope correction

This theorem concerns the Magnus expansion of the induced horizontal/projective
connection

\[
\mathcal A_{\rm hor}(\tau)
=
-\frac{i}{2}
\boldsymbol\Omega(\tau)\cdot\boldsymbol\sigma.
\]

It must not be identified with the Magnus expansion of the fixed 36D QHTRI
Hamiltonian used to generate the pinned trajectory.

For that fixture,

\[
H_{\rm source}(\tau)=H_0,
\]

hence

\[
\boxed{
[H_{\rm source}(\tau_1),H_{\rm source}(\tau_2)]=0
}
\]

and all higher Magnus commutator terms of the source Hamiltonian vanish.

Genuine source-Hamiltonian ordering is established separately on the adaptive
v0.32 semantic path in

TIR/foundations/TIR_MUMMU_SOURCE_OPERATOR_NONABELIANITY_FIREWALL_V0_1.md,

where the directly evaluated adjacent commutators satisfy

\[
[H_k,H_{k+1}]\neq0.
\]

Thus the cubic result in this theorem remains valid, but its operator is
\(\mathcal A_{\rm hor}\), not the fixed source \(H_0\).


## 10. Operator-level scope correction

The (A(	au)) analyzed here is the reduced horizontal/projective connection
derived from the (CP^1) trajectory. Therefore the cubic Magnus defect proven
here is a statement about that connection.

It is not the Magnus expansion of the fixed parent QHTRI Hamiltonian used to
generate the reference trajectory; that fixed parent Hamiltonian commutes with
itself.

For genuine parent-source-operator history, use the distinct multi-step
controlled PNCS sequence and test the actual (H_k) matrices directly. That
test is recorded in

`TIR_MUMMU_QHTRI_DIRECT_SOURCE_OPERATOR_NONCOMMUTATIVITY_V0_1.md`.
