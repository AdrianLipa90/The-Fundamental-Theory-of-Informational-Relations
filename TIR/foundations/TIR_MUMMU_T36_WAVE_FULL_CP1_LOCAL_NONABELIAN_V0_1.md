# TIR MUMMU T36 Wave-Amplitude Full-CP1 Lift and Local Non-Abelian Closure v0.1

Status: `EXACT_SOURCE_WEIGHTED_CP1_LIFT / EXACT_PHASE_ONLY_EQUATOR_LIMIT / EXACT_HORIZONTAL_PROJECTIVE_CONNECTION_NONCOMMUTATIVITY / SOURCE_OPERATOR_GATE_SEPARATE / CROSS_FACTOR_COUPLING_STILL_OPEN / PHYSICAL_BINDING_OPEN`

Date: 2026-09-23

## 1. Correction scope

This theorem corrects an over-strong statement in

`TIR_MUMMU_18PAIR_INTERTWINER_ADMISSION_NOGO_V0_1.md`.

The exact no-go that survives is:

\[
\boxed{
[\mathfrak{su}(2)_j,\mathfrak{su}(2)_k]=0
\qquad(j\neq k)
}
\]

for an uncoupled direct product.

However, the stronger phrase

\[
\text{“uncoupled T36 cannot generate any non-Abelian local transport”}
\]

is false once the already-existing PNCS wave-amplitude carrier is included.

PNCS contains both:

1. a 36-phase temporal projection; and
2. a normalized 36-amplitude temporal wave state.

Together they produce a full local \(CP^1\) state in each complementary pair,
not only the equal-amplitude equator.

## 2. Source pin

PNCS source:

`AdrianLipa90/PhaseNav-Natural-Coding-System@8855abed440e9949f576ffbe2153325f69e78963`.

Relevant source:

`src/phasenav_natural_code/temporal_geometry_v02.py`.

The source defines:

- exactly 36 ordered temporal phase coordinates;
- an 18-pair dual projection;
- a normalized 36-component complex wave-amplitude state;
- probabilities \(p_k=|a_k|^2\);
- fail-closed finite/nonzero normalization.

The source remains experimental and non-promoting. Only its exact mathematical
carrier is imported here.

## 3. Pairwise weighted spinor

For pair \(j\), let

\[
\theta_{jL}=\theta_{2j-1},
\qquad
\theta_{jR}=\theta_{2j},
\]

and source probabilities

\[
p_{jL}=|a_{2j-1}|^2,
\qquad
p_{jR}=|a_{2j}|^2.
\]

Define pair support

\[
q_j=p_{jL}+p_{jR}.
\]

The local projective state is admitted only when

\[
\boxed{q_j>0.}
\]

Then define

\[
\boxed{
|\psi_j\rangle
=
\frac1{\sqrt{q_j}}
\begin{pmatrix}
\sqrt{p_{jL}}e^{i\theta_{jL}}\\
\sqrt{p_{jR}}e^{i\theta_{jR}}
\end{pmatrix}.
}
\]

No fitted coefficient is introduced.

## 4. Full Bloch map

Let

\[
\delta_j
=
\theta_{jR}-\theta_{jL},
\]

and

\[
\boxed{
u_j
=
\frac{p_{jL}-p_{jR}}{p_{jL}+p_{jR}}
\in[-1,1].
}
\]

Then

\[
\boxed{
\mathbf n_j
=
\left(
\sqrt{1-u_j^2}\cos\delta_j,,
\sqrt{1-u_j^2}\sin\delta_j,,
u_j
\right).
}
\]

Therefore

\[
\boxed{
P_j
=
|\psi_j\rangle\langle\psi_j|
=
\frac12(I+\mathbf n_j\cdot\boldsymbol\sigma).
}
\]

This is a full \(CP^1\cong S^2\) carrier.

## 5. Phase-only equator as a special case

If

\[
p_{jL}=p_{jR}>0,
\]

then

\[
u_j=0
\]

and

\[
\boxed{
\mathbf n_j
=
(\cos\delta_j,\sin\delta_j,0).
}
\]

Thus the earlier phase-only theorem is recovered exactly as the equal-amplitude
equatorial submanifold.

Its \(\sigma_z\)-only horizontal connection is therefore a special case, not
the full source geometry.

## 6. Source-derived local spin connection

For an admitted smooth pair trajectory

\[
\tau\mapsto
(\delta_j(\tau),u_j(\tau)),
\]

use the already-derived orbital spin connection with zero extra fiber phase:

\[
\boxed{
\mathcal A_j
=
-\frac{i}{2}
(\mathbf n_j\times d\mathbf n_j)
\cdot\boldsymbol\sigma.
}
\]

For a general full-sphere trajectory the generator direction is not fixed.

Let

\[
\Omega_j
=
\mathbf n_j\times\dot{\mathbf n}_j.
\]

Then

\[
\boxed{
\mathcal A_j
=
-\frac{i}{2}
\Omega_j\cdot\boldsymbol\sigma.
}
\]

## 7. Exact horizontal projective-connection noncommutativity criterion

For two admitted tangent segments at parameters \(\tau_1,\tau_2\),

\[
\boxed{
[
\mathcal A_j(\tau_1),
\mathcal A_j(\tau_2)
]
=
-\frac{i}{2}
\left(
\Omega_j(\tau_1)
\times
\Omega_j(\tau_2)
\right)
\cdot\boldsymbol\sigma.
}
\]

Therefore

\[
\boxed{
[
\mathcal A_j(\tau_1),
\mathcal A_j(\tau_2)
]\ne0
\iff
\Omega_j(\tau_1)
\not\parallel
\Omega_j(\tau_2).
}
\]

A single source pair can therefore carry a noncommuting horizontal/projective connection history. This statement does not by itself establish noncommutativity of the underlying source Hamiltonian.

No inter-pair coupling is mathematically required for this **local**
non-Abelianity.

## 8. Minimal exact witness

At

\[
u=0,
\qquad
\delta=0,
\qquad
\mathbf n=(1,0,0),
\]

take the two independent source-coordinate tangent directions.

### Phase tangent

\[
\partial_\delta\mathbf n
=
(0,1,0),
\]

so

\[
\boxed{
\Omega_\delta
=
\mathbf n\times\partial_\delta\mathbf n
=
(0,0,1).
}
\]

Hence

\[
A_\delta
=
-\frac{i}{2}\sigma_z.
\]

### Population-imbalance tangent

\[
\partial_u\mathbf n
=
(0,0,1),
\]

so

\[
\boxed{
\Omega_u
=
\mathbf n\times\partial_u\mathbf n
=
(0,-1,0).
}
\]

Hence

\[
A_u
=
+\frac{i}{2}\sigma_y.
\]

Their commutator is

\[
\boxed{
[A_\delta,A_u]
=
-\frac{i}{2}\sigma_x
\ne0.
}
\]

Thus the source coordinates \((\delta,u)\) already span a genuinely noncommuting local \(\mathfrak{su}(2)\) channel for the declared horizontal/projective connection.

## 9. Corrected interpretation of the 18-factor product

The full uncoupled carrier is

\[
\boxed{
\prod_{j=1}^{18}CP^1_j
}
\]

with local algebra

\[
\boxed{
\mathfrak g_{36}
=
\bigoplus_{j=1}^{18}\mathfrak{su}(2)_j.
}
\]

Two distinct statements must not be mixed:

### Local statement

Within one factor,

\[
[A_j(\tau_1),A_j(\tau_2)]
\]

may be nonzero through full-CP1 dynamics.

### Cross-factor statement

For \(j\ne k\),

\[
\boxed{
[X_j,Y_k]=0
}
\]

until a source-derived inter-factor coupling/shared connection is supplied.

Therefore the 18-pair intertwiner gate remains relevant only for
**cross-factor organization/coupling**, not for the existence of local
non-Abelian path transport itself.

## 10. Consequence for the quartic seam

The quartic shared-\(SU(2)\) history theorem no longer requires an
inter-factor coupling to have a source-derived local realization.

A single pair trajectory with changing \((\delta,u)\) can provide two
noncommuting local generators.

What remains open is whether the exact quartic coefficient/probe used in the
existing seam theorem is selected by the PNCS pair dynamics rather than by a
separately declared two-history probe.

Thus:

\[
\boxed{
\text{local horizontal/projective non-Abelian carrier = CLOSED}
}
\]

while

\[
\boxed{
\text{specific quartic MUMMU source selection = OPEN}.
}
\]

## 11. Pauli C3 compatibility

The full Bloch sphere is invariant under the exact Pauli cyclic adjoint action

\[
\sigma_x\to\sigma_y\to\sigma_z\to\sigma_x.
\]

The phase-only equator is not invariant under that action.

Therefore the wave-amplitude lift removes the geometric obstruction to using the
existing Pauli \(C_3\) representation locally.

It does **not** identify the eighteen pair labels with six ports times three
axes.

## 12. Claim ledger

| Statement | Status |
|---|---|
| weighted pair spinor from source phase + probability data | `EXACT` |
| weighted pair projector is rank-one CP1 | `EXACT` |
| Bloch vector formula in \((\delta,u)\) | `EXACT` |
| equal pair weights recover equatorial phase-only carrier | `EXACT` |
| local connection direction varies on full CP1 | `EXACT` |
| horizontal/projective connection commutator criterion \(\Omega_1\times\Omega_2\) | `EXACT` |
| phase and imbalance tangents generate nonzero Pauli commutator in the declared projective connection | `EXACT` |\n| this commutator alone proves source-Hamiltonian noncommutativity | `REFUTED` |
| distinct uncoupled factors commute | `EXACT` |
| inter-factor 6×3 intertwiner is required for any non-Abelianity | `REFUTED / CORRECTED` |
| inter-factor 6×3 intertwiner is required for cross-factor port/axis organization | `OPEN ADMISSION GATE` |
| specific physical MUMMU interpretation | `OPEN / NOT CLAIMED` |

## 13. Validation

Deterministic validator:

`TIR/validation/tir_mummu_t36_wave_full_cp1_local_nonabelian_v0_1.py`

Static receipt:

`TIR/validation/TIR_MUMMU_T36_WAVE_FULL_CP1_LOCAL_NONABELIAN_VALIDATION_V0_1.json`

## 14. Next gate

The new narrow gate is to derive the **dynamics of the pair imbalance**

\[
\boxed{
u_j(\tau)
=
\frac{p_{jL}(\tau)-p_{jR}(\tau)}
{p_{jL}(\tau)+p_{jR}(\tau)}
}
\]

from the existing PhaseNav temporal/wave evolution, and test whether its
resulting local holonomy reproduces the MUMMU quartic seam without selecting two
histories by hand.


## 15. QHTRI pair-dynamics source closure

The previously open pair-imbalance trajectory is now source-bound at model
level by

`TIR/foundations/TIR_MUMMU_QHTRI_PAIR_DYNAMICS_SOURCE_WITNESS_V0_1.md`.

The existing PNCS fixed-H/QHTRI dynamics gives

[
idotpsi=Hpsi,
]

so

[
dot p_k
=
2,operatorname{Im}
left[
psi_k^*(Hpsi)_k
ight]
]

and therefore

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

For the pinned deterministic PNCS fixture, pair 0 has the local witness

[
oxed{
left|
oldsymbolOmega_0
	imes
dot{oldsymbolOmega}_0
ight|
approx
9.02843	imes10^{-4}>0.
}
]

Thus the source 36D Hamiltonian generates a changing local (SU(2)) generator
without an inserted pair-level dynamics ansatz.

The remaining gate is no longer the existence of local noncommutativity of the horizontal/projective connection. It is
whether the source-derived time-ordered connection reproduces the previously
declared quartic MUMMU seam coefficient/order.


## 20. Projective-connection versus source-operator firewall

The local (CP^1) algebra above is exact for the declared horizontal connection,

[
mathcal A_{m hor}
=
-rac{i}{2}
(mathbf n	imes dmathbf n)cdotoldsymbolsigma.
]

A nonzero commutator of two such connection values does not imply that every
Hamiltonian capable of generating the same state path must be noncommuting.

The exact counterexample and the direct source-operator test are recorded in

`TIR/foundations/TIR_MUMMU_SOURCE_OPERATOR_NONABELIANITY_FIREWALL_V0_1.md`.

In particular, fixed-modulus phase flow admits the commuting diagonal lift

[
H_D(	au)
=
-operatorname{diag}dot	heta(	au),
]

while the actual adaptive PNCS v0.32 semantic path has directly verified

[
oxed{
[H_k,H_{k+1}]
eq0
}
]

for all six adjacent steps of the frozen seven-role trajectory.

Accordingly, this document establishes the local projective connection algebra.
Direct source-Hamiltonian noncommutativity is claimed only when the Hamiltonian
commutator itself has been evaluated.
