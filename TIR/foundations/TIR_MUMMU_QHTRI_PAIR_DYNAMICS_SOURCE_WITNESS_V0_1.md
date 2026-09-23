# TIR MUMMU QHTRI Pair-Dynamics Source Witness v0.1

Status: `SOURCE_DERIVED_PAIR_DYNAMICS / EXACT_HORIZONTAL_PROJECTIVE_CONNECTION_WITNESS / FIXED_SOURCE_H_COMMUTES / ADAPTIVE_SOURCE_OPERATOR_GATE_SEPARATE / PHYSICAL_BINDING_OPEN`

Date: 2026-09-23

## 1. Purpose

This theorem continues the source-weighted full-`CP1` correction and removes the
remaining free pair-imbalance trajectory from the local MUMMU witness.

The parent result is

[
P_j(	au)
=
rac12
left(
I+mathbf n_j(	au)cdotoldsymbolsigma
ight),
]

with the local orbital generator

[
mathcal A_j
=
-rac{i}{2}
left(
mathbf n_j	imesdot{mathbf n}_j
ight)cdotoldsymbolsigma.
]

The open question was whether (dot u_j) had to be supplied by an external
ansatz.

It does not.  The existing PNCS temporal-fibre / QHTRI path already supplies a
36-dimensional Hermitian Hamiltonian and unitary evolution.

## 2. Source pins

PNCS source:

`AdrianLipa90/PhaseNav-Natural-Coding-System@8855abed440e9949f576ffbe2153325f69e78963`.

Imported contracts:

- `src/phasenav_natural_code/temporal_fibre_v1.py`;
- `src/phasenav_natural_code/semantic_htri_drive_v32.py`;
- `tests/test_semantic_htri_drive_v32.py`;
- `src/phasenav_natural_code/temporal_geometry_v02.py`.

The deterministic source fixture declares

[
phi_k
=
operatorname{linspace}(0.07,5.91,36)_k,
]

[
omega_k
=
39.6+operatorname{linspace}(-0.12,0.12,36)_k,
]

and

[
g_{mn}
=
0.18cosrac{(m-n)pi}{18},
qquad
g_{mm}=0.
]

The source QHTRI Hamiltonian law is

[
oxed{
H
=
0.25,operatorname{diag}(widehatomega)
+
0.7,widehat g,
}
]

where (widehatomega) is the centered/std-normalized frequency vector and
(widehat g) is the symmetric coupling matrix normalized by its spectral
radius.

For this deterministic cosine fixture,

[
ho(g)=3.06,
]

so off diagonal

[
widehat g_{mn}
=
rac1{17}
cosrac{(m-n)pi}{18}.
]

## 3. Exact 36D wave dynamics

The initial PNCS phase state is

[
oxed{
psi_k(0)
=
rac{e^{iphi_k}}{sqrt{36}}.
}
]

The fixed-H temporal fibre obeys

[
oxed{
ihbardotpsi
=
Hpsi,
}
]

with the source default convention (hbar=1) in the executable reference.

Therefore

[
dotpsi=-iHpsi,
qquad
ddotpsi=-H^2psi.
]

No pair-level population law is introduced separately.

## 4. Pair support and imbalance dynamics

For pair (j), write

[
v_j
=
egin{pmatrix}
psi_{2j}\
psi_{2j+1}
end{pmatrix},
qquad
q_j=v_j^dagger v_j.
]

The normalized local projector is

[
oxed{
P_j
=
rac{v_jv_j^dagger}{q_j},
qquad
q_j>0.
}
]

Let

[
p_L=|psi_{2j}|^2,
qquad
p_R=|psi_{2j+1}|^2.
]

From the source Schrödinger dynamics,

[
oxed{
dot p_k
=
2,operatorname{Im}
left[
psi_k^*(Hpsi)_k
ight].
}
]

Thus the pair imbalance

[
u_j
=
rac{p_L-p_R}{p_L+p_R}
]

has the exact derivative

[
oxed{
dot u_j
=
rac{
2(p_Rdot p_L-p_Ldot p_R)
}{
(p_L+p_R)^2
}.
}
]

Hence the previously open (u_j(	au)) channel is generated directly by the
existing 36D Hamiltonian.

## 5. Projector derivatives without phase unwrapping

Define

[
N_j=v_jv_j^dagger.
]

Then

[
dot q_j
=
2operatorname{Re}(v_j^daggerdot v_j),
]

[
ddot q_j
=
2operatorname{Re}
left(
dot v_j^daggerdot v_j
+
v_j^daggerddot v_j
ight).
]

The exact normalized projector derivatives are

[
oxed{
dot P_j
=
rac{dot N_j}{q_j}
-
rac{N_jdot q_j}{q_j^2},
}
]

and

[
oxed{
ddot P_j
=
rac{ddot N_j}{q_j}
-
rac{2dot N_jdot q_j}{q_j^2}
-
rac{N_jddot q_j}{q_j^2}
+
rac{2N_jdot q_j^2}{q_j^3}.
}
]

This avoids wrapped-phase differentiation entirely.

Using

[
P_j=rac12(I+mathbf n_jcdotoldsymbolsigma),
]

the Bloch derivatives are read directly from
(dot P_j,ddot P_j).

## 6. Local horizontal projective-connection acceleration

Define

[
oxed{
oldsymbolOmega_j
=
mathbf n_j	imesdot{mathbf n}_j.
}
]

Then

[
mathcal A_j
=
-rac{i}{2}
oldsymbolOmega_jcdotoldsymbolsigma.
]

Its derivative is

[
oxed{
dot{oldsymbolOmega}_j
=
mathbf n_j	imesddot{mathbf n}_j,
}
]

because
(dot{mathbf n}_j	imesdot{mathbf n}_j=0).

For infinitesimally separated proper-time sections,

[
oldsymbolOmega_j(	au+arepsilon)
=
oldsymbolOmega_j(	au)
+
arepsilondot{oldsymbolOmega}_j(	au)
+
O(arepsilon^2).
]

Therefore

[
oxed{
[
mathcal A_j(	au),
mathcal A_j(	au+arepsilon)
]
=
-rac{iarepsilon}{2}
left(
oldsymbolOmega_j
	imes
dot{oldsymbolOmega}_j
ight)cdotoldsymbolsigma
+
O(arepsilon^2).
}
]

A nonzero

[
oxed{
mathcal W_j
:=
left|
oldsymbolOmega_j
	imes
dot{oldsymbolOmega}_j
ight|
}
]

is therefore an exact local witness that the declared horizontal/projective CP1 connection changes generator axis. It does not, by itself, establish noncommutativity of the underlying source Hamiltonian history.

## 7. Deterministic PNCS witness

For the exact deterministic fixture above, pair (j=0) at (	au=0) gives

[
oldsymbolOmega_0
approx
(-0.00176948,,
  0.01050618,,
 -0.02741997),
]

[
dot{oldsymbolOmega}_0
approx
(-0.00598490,,
  0.03553493,,
 -0.00800126).
]

Their cross product is

[
oldsymbolOmega_0
	imes
dot{oldsymbolOmega}_0
approx
(8.90304	imes10^{-4},,
 1.49948	imes10^{-4},,
 0),
]

with

[
oxed{
mathcal W_0
approx
9.02843	imes10^{-4}
>0.
}
]

Therefore the existing source Hamiltonian and source phase state already produce a changing, noncommuting horizontal/projective CP1 connection. The pinned Hamiltonian used in this fixture is nevertheless time-independent, so its direct source-operator history commutes.

This is a computational/model-level witness from the pinned PNCS reference
fixture. It is not evidence that the same dynamics is physically realized by
neutrinos, gravity, or spacetime.

## 8. Relation to the finite-time witness

Direct source evolution also gives, for the same pair,

[
u_0(0)approx0,
qquad
u_0(0.5)approx-0.0101752.
]

The generator direction changes from

[
oldsymbolOmega_0(0)
approx
(-0.00176948,0.01050618,-0.02741997)
]

to

[
oldsymbolOmega_0(0.5)
approx
(-0.00502308,0.03059681,-0.03291479),
]

and

[
oxed{
left|
oldsymbolOmega_0(0)
	imes
oldsymbolOmega_0(0.5)
ight|
approx
4.99522	imes10^{-4}.
}
]

The small-(	au) ratio

[
rac{
|Omega(0)	imesOmega(	au)|
}{	au}
]

converges to the local derivative witness
(mathcal W_0).

## 9. What is now closed

The following chain is source-derived at model level:

[
oxed{
(phi,omega,g)
	o
H
	o
psi(	au)
	o
P_j(	au)
	o
mathbf n_j(	au)
	o
mathcal A_j(	au).
}
]

Thus neither the pair imbalance trajectory nor the local (SU(2)) generator
needs to be inserted by hand.

## 10. What remains open

Three boundaries remain:

1. the default QHTRI coefficients (0.25) and (0.7) are source-contract
   parameters, not derived fundamental constants;
2. cross-factor coupling between distinct (CP^1_j) fibres remains separate;
3. the specific quartic MUMMU seam coefficient is not yet derived from this
   source trajectory.

The next gate is therefore to compare the BCH/Magnus expansion of the
source-derived (mathcal A_j(	au)) with the existing quartic seam and test
whether the quartic coefficient emerges or fails.

## 11. Claim ledger

| Statement | Status |
|---|---|
| QHTRI fixture Hamiltonian is Hermitian | `EXACT SOURCE CONTRACT` |
| pair probabilities evolve from the same 36D Hamiltonian | `EXACT` |
| (dot u_j) formula follows from Schrödinger evolution | `EXACT` |
| projector first/second derivative formulas | `EXACT` |
| local witness (Omega	imesdotOmega) controls first noncommuting time separation | `EXACT` |
| deterministic pair-0 witness is nonzero | `NUMERIC PASS / PINNED FIXTURE` |
| no pair-dynamics ansatz is required | `PASS AT MODEL LEVEL` |
| QHTRI coefficients are fundamental physical constants | `NOT CLAIMED` |
| physical MUMMU/neutrino/gravity realization | `OPEN / NOT CLAIMED` |

## 12. Validation

Deterministic validator:

`TIR/validation/tir_mummu_qhtri_pair_dynamics_source_witness_v0_1.py`

Static receipt:

`TIR/validation/TIR_MUMMU_QHTRI_PAIR_DYNAMICS_SOURCE_WITNESS_VALIDATION_V0_1.json`


## 13. Source-operator correction firewall

A later direct operator audit separates the horizontal projective connection from
the Hamiltonian that generates the 36D source trajectory:

`TIR/foundations/TIR_MUMMU_SOURCE_OPERATOR_NONABELIANITY_FIREWALL_V0_1.md`.

For this pinned fixture,

[
H(	au)=H_0
]

is time independent, hence

[
oxed{
[H(	au_1),H(	au_2)]=0.
}
]

Therefore the nonzero quantity

[
mathcal W_j
=
|Omega_j	imesdotOmega_j|
]

must be read as a witness for the declared horizontal/projective connection,
not as a direct source-Hamiltonian commutator witness.

Genuine source-operator noncommutativity is established separately on the
adaptive PNCS semantic path, where (g_k) and therefore (H_k) vary between
steps and direct evaluation gives

[
oxed{
[H_k,H_{k+1}]
eq0.
}
]

This correction preserves all pair-dynamics and projector-derivative results
above while narrowing the operator-level claim to the quantity actually tested.
