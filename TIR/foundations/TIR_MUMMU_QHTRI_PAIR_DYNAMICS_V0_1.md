# TIR MUMMU QHTRI-Driven Pair Dynamics and Local Holonomy Closure v0.1

Status: `EXACT_PAIR_PROJECTOR_DYNAMICS / SOURCE_PINNED_QHTRI_FIXTURE_NONABELIAN_PASS / MODEL_LEVEL_RUNTIME_CLOSURE / PHYSICAL_BINDING_OPEN`

Date: 2026-09-23

## 1. Purpose

This theorem closes the local-dynamics gate left by

`TIR_MUMMU_T36_WAVE_FULL_CP1_LOCAL_NONABELIAN_V0_1.md`.

The previous theorem established that the pair coordinates
\((\delta_j,u_j)\) support a full \(CP^1\) carrier and a locally
noncommuting \(\mathfrak{su}(2)\) connection.

Here the population-imbalance dynamics are derived directly from the existing
PNCS 36D unitary runtime rather than supplied as an ansatz.

## 2. Source pin

PNCS source:

`AdrianLipa90/PhaseNav-Natural-Coding-System@8855abed440e9949f576ffbe2153325f69e78963`.

Imported exact computational contracts:

- `src/phasenav_natural_code/temporal_fibre_v1.py`;
- `src/phasenav_natural_code/semantic_htri_drive_v32.py`;
- deterministic fixture from
  `tests/test_semantic_htri_drive_v32.py`.

No claim is made that this model-level Hamiltonian is a physical microscopic
Hamiltonian of Nature.

## 3. 36D unitary dynamics

The temporal fibre uses

\[
\boxed{
i\hbar\dot\psi=H\psi,
\qquad
H=H^\dagger.
}
\]

For the source QHTRI graph law,

\[
\boxed{
H
=
d\,\mathrm{diag}(\widehat\omega)
+
c\,\widehat g,
}
\]

with source defaults

\[
c=0.7,
\qquad
d=0.25,
\]

where \(\widehat g\) is the symmetric coupling matrix normalized by its
spectral norm and \(\widehat\omega\) is the centered/standardized frequency
vector.

These constants are source runtime policy values, not fitted in this theorem.

## 4. Exact probability flow

For coordinate \(k\),

\[
p_k=|\psi_k|^2.
\]

Using the Schrödinger equation,

\[
\boxed{
\dot p_k
=
\frac{2}{\hbar}
\operatorname{Im}
\left[
\psi_k^*(H\psi)_k
\right].
}
\]

For pair \(j\), write

\[
p_L=p_{2j-1},
\qquad
p_R=p_{2j},
\qquad
q=p_L+p_R.
\]

When \(q>0\), define

\[
u_j=\frac{p_L-p_R}{q}.
\]

Then differentiation gives the exact source-driven law

\[
\boxed{
\dot u_j
=
\frac{
2(p_R\dot p_L-p_L\dot p_R)
}{
(p_L+p_R)^2
}.
}
\]

Therefore \(u_j(\tau)\) is computable directly from \((H,\psi)\).

## 5. Exact pair projector dynamics

Let

\[
v_j=
\begin{pmatrix}
\psi_{2j-1}\\
\psi_{2j}
\end{pmatrix},
\qquad
q_j=v_j^\dagger v_j>0.
\]

The normalized local projector is

\[
\boxed{
P_j=\frac{v_jv_j^\dagger}{q_j}.
}
\]

Let \(\dot v_j\) be the corresponding two selected components of
\(-iH\psi/\hbar\). Then

\[
\boxed{
\dot P_j
=
\frac{
\dot v_jv_j^\dagger
+
v_j\dot v_j^\dagger
}{q_j}
-
\frac{\dot q_j}{q_j}P_j,
}
\]

where

\[
\dot q_j
=
2\operatorname{Re}
(v_j^\dagger\dot v_j).
\]

No phase unwrapping is required.

The Bloch variables are

\[
n_{j,a}=\operatorname{Tr}(P_j\sigma_a),
\]

so

\[
\boxed{
\dot n_{j,a}
=
\operatorname{Tr}(\dot P_j\sigma_a).
}
\]

## 6. Source-derived orbital connection

Define

\[
\boxed{
\Omega_j
=
\mathbf n_j\times\dot{\mathbf n}_j.
}
\]

The horizontal orbital spin connection is

\[
\boxed{
\mathcal A_j
=
-\frac{i}{2}
\Omega_j\cdot\boldsymbol\sigma.
}
\]

Thus the complete computational chain is

\[
\boxed{
(\phi,\omega,g)
\to
H
\to
\psi(\tau)
\to
P_j(\tau)
\to
\mathbf n_j(\tau)
\to
\mathcal A_j(\tau).
}
\]

Every step is deterministic once an admitted PNCS snapshot is supplied.

## 7. Exact local non-Abelian diagnostic

At two proper times,

\[
\boxed{
[
\mathcal A_j(\tau_1),
\mathcal A_j(\tau_2)
]
=
-\frac{i}{2}
\left[
\Omega_j(\tau_1)
\times
\Omega_j(\tau_2)
\right]
\cdot\boldsymbol\sigma.
}
\]

Define

\[
\boxed{
\chi_j(\tau_1,\tau_2)
=
\left\|
\Omega_j(\tau_1)
\times
\Omega_j(\tau_2)
\right\|.
}
\]

Then

\[
\chi_j>0
\]

is an exact witness of noncommuting local history for pair \(j\).

## 8. Deterministic v0.32 fixture result

Use the exact deterministic fixture already present in PNCS:

\[
\phi_k
=
\operatorname{linspace}(0.07,5.91,36),
\]

\[
\omega_k
=
39.6+
\operatorname{linspace}(-0.12,0.12,36),
\]

\[
g_{mn}
=
0.18
\cos\left(
\frac{(m-n)\pi}{18}
\right),
\qquad
g_{mm}=0.
\]

The initial state is the existing phase state

\[
\boxed{
\psi_k(0)
=
\frac{e^{i\phi_k}}{\sqrt{36}}.
}
\]

Thus every initial pair has equal support and

\[
u_j(0)=0
\]

up to floating-point roundoff.

Using the source QHTRI Hamiltonian and exact unitary evolution to

\[
\Delta\tau=0.01,
\]

the validator finds

\[
\boxed{
\max_j|u_j(0.01)|
=
1.1191617466482784\times10^{-4}.
}
\]

Hence the runtime dynamically leaves the equal-amplitude equator.

For pair index \(j=9\) in zero-based validator indexing,

\[
\boxed{
\chi_9(0,0.01)
=
9.440215696404591\times10^{-6}
>0.
}
\]

The corresponding commutator has Frobenius norm

\[
\boxed{
\|
[
\mathcal A_9(0),
\mathcal A_9(0.01)
]
\|_F
=
6.675240534791372\times10^{-6}.
}
\]

Therefore the source-pinned deterministic PNCS/QHTRI fixture produces a
noncommuting local pair history without any inter-pair coupling ansatz.

## 9. Numerical integrity

For the declared \(0.01\) evolution:

\[
\|U^\dagger U-I\|_{\max}
=
3.774758283725532\times10^{-15}.
\]

Initial pair supports are all

\[
q_j=\frac1{18}
\]

up to floating-point roundoff.

After evolution all pair supports remain strictly positive in the probe.

The largest initial imbalance velocity is

\[
\boxed{
\max_j|\dot u_j(0)|
=
1.1014611729223812\times10^{-2}.
}
\]

## 10. What is closed and what is not

Closed at model/runtime level:

\[
\boxed{
\text{admitted 36D snapshot}
\to
H
\to
\psi(\tau)
\to
u_j(\tau)
\to
P_j(\tau)
\to
\mathcal A_j(\tau)
}
\]

with no free local MUMMU transport coefficient.

Still open:

1. physical identification of the QHTRI Hamiltonian with a microscopic field;
2. derivation of the QHTRI policy constants \(0.7\) and \(0.25\) from a deeper
   physical action rather than runtime policy;
3. cross-factor coupling between different \(CP^1_j\) sectors;
4. derivation of the previously declared quartic MUMMU coefficient from this
   runtime trajectory rather than from a separate two-history probe;
5. any neutrino/gravity identification.

## 11. Consequence for the 6×3 intertwiner gate

The \(C_6\times C_3\) factorization is no longer required to obtain local
non-Abelian MUMMU dynamics.

It remains a separate question only if the theory requires an intrinsic
six-port × three-axis organization of the **eighteen distinct pair labels**.

Therefore:

\[
\boxed{
\text{local non-Abelian closure}
\not\Rightarrow
\text{18-pair }C_6\times C_3\text{ factorization}.
}
\]

and conversely

\[
\boxed{
\text{18-pair factorization is not a prerequisite for local closure}.
}
\]

## 12. Validation

Deterministic validator:

`TIR/validation/tir_mummu_qhtri_pair_dynamics_v0_1.py`

Static receipt:

`TIR/validation/TIR_MUMMU_QHTRI_PAIR_DYNAMICS_VALIDATION_V0_1.json`

## 13. Next gate

The next mathematically useful test is no longer “can MUMMU become
non-Abelian?” It can, in the pinned computational model.

The next gate is:

\[
\boxed{
\text{Does the source-derived local holonomy produce the existing quartic seam}
}
\]

with no hand-selected pair of history generators.

That requires extracting the small-loop expansion of the QHTRI-driven
\(P_j(\tau)\) path and comparing its leading invariant with the current
quartic-seam theorem.
