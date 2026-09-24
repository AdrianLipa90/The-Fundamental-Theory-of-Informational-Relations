# TIR MUMMU T36 Complementary-Pair CP1 Projection v0.1

Status: `EXACT_CONDITIONAL_ON_PNCS_T36_PAIRING / EIGHTEEN_CP1_PRODUCT_CARRIER / SINGLE_CP1_SELECTOR_OPEN / PHYSICAL_BINDING_OPEN`

Date: 2026-09-23

## 1. Purpose

The previous orbital-spin theorem left one map open:

\[
\Pi:T^{36}\to CP^1.
\]

The source-pinned PNCS T36 realization shows that a single \(CP^1\) is not the
native source object. The exact temporal T36 contract is built from eighteen
complementary phase pairs. Therefore the source-derived local projective carrier
is

\[
\boxed{
\Pi_{18}:T^{36}\longrightarrow(CP^1)^{18}.
}
\]

No individual T36 coordinate and no single pair is privileged by this theorem.

Source:

`AdrianLipa90/PhaseNav-Natural-Coding-System@8855abed440e9949f576ffbe2153325f69e78963`

using:

- `spec/experimental/PNCS_PRIME_TEMPORAL_HYDRO_V0_1.md`;
- `native/experimental/PNCS_PRIME_TEMPORAL_HYDRO_V0_1.pnv`;
- `src/phasenav_natural_code/prime_temporal_hydro_v01.py`.

The PNCS source remains explicitly experimental/read-only/non-promoting. This
TIR theorem imports only its exact 18-pair geometry.

## 2. Exact T36 pair structure

For eighteen registered frequencies the source contract defines

\[
\theta_{2j-1}
=
(\theta_c-\omega_j t)\bmod2\pi,
\]

\[
\theta_{2j}
=
(\theta_c+\omega_j t)\bmod2\pi,
\qquad
j=1,\ldots,18.
\]

Hence

\[
\boxed{
\delta_j
:=
\theta_{2j}-\theta_{2j-1}
\equiv
2\omega_jt
\pmod{2\pi}.
}
\]

## 3. Canonical pair spinor

For each complementary pair define

\[
\boxed{
|\psi_j\rangle
=
\frac1{\sqrt2}
\begin{pmatrix}
e^{i\theta_{2j-1}}\\
e^{i\theta_{2j}}
\end{pmatrix}.
}
\]

Its rank-one projector is

\[
\boxed{
P_j
=
|\psi_j\rangle\langle\psi_j|
=
\frac12
\begin{pmatrix}
1 & e^{-i\delta_j}\\
e^{i\delta_j} & 1
\end{pmatrix}.
}
\]

Therefore

\[
P_j^2=P_j,
\qquad
P_j^\dagger=P_j,
\qquad
\operatorname{Tr}P_j=1.
\]

The corresponding Bloch vector is

\[
\boxed{
\mathbf n_j
=
(\cos\delta_j,\sin\delta_j,0).
}
\]

Thus every source pair is an equatorial \(CP^1\) state.

## 4. Center-phase cancellation

Apply a common pair phase

\[
\theta_{2j-1}\mapsto\theta_{2j-1}+\alpha,
\qquad
\theta_{2j}\mapsto\theta_{2j}+\alpha.
\]

Then

\[
|\psi_j\rangle\mapsto e^{i\alpha}|\psi_j\rangle
\]

but

\[
\boxed{
P_j\mapsto P_j.
}
\]

In particular, the explicit PNCS center phase \(\theta_c\) cancels from the
projective state. The projective carrier depends only on the complementary
relative phase \(\delta_j\).

## 5. Product projective carrier

Define

\[
\boxed{
\Pi_{18}(\theta_1,\ldots,\theta_{36})
=
(P_1,\ldots,P_{18}).
}
\]

This map:

- consumes all 36 phase coordinates exactly once;
- preserves the source 18-pair partition;
- introduces no coordinate weights;
- introduces no pair selector;
- is covariant under permutation of the registered pair labels.

A registry permutation

\[
j\mapsto\pi(j)
\]

only permutes the \(CP^1\) factors:

\[
\boxed{
\Pi_{18}\mapsto
(P_{\pi(1)},\ldots,P_{\pi(18)}).
}
\]

## 6. Pairwise orbital spin connection

For one pair,

\[
\mathbf n_j
=
(\cos\delta_j,\sin\delta_j,0),
\]

so

\[
\boxed{
\mathbf n_j\times d\mathbf n_j
=
(0,0,d\delta_j).
}
\]

With zero additional lifted fiber phase, the unique orbital-spin connection from
the parent theorem reduces exactly to

\[
\boxed{
\mathcal A_j
=
-\frac{i}{2}\sigma_z\,d\delta_j.
}
\]

Therefore

\[
\boxed{
\rho_j
=
\exp\left[
-\frac{i}{2}
\Delta\delta_j\sigma_z
\right].
}
\]

For the explicit temporal source,

\[
\delta_j=2\omega_jt,
\]

hence

\[
\boxed{
\rho_j(t_1,t_0)
=
\exp\left[
-i\omega_j(t_1-t_0)\sigma_z
\right].
}
\]

Thus the source T36 pair geometry reproduces the same registered frequency in
the spin-lift transport without a fitted scale factor.

## 7. Full T36 transporter

Before any additional coupling between pair sectors is derived, the natural
transport group is the direct product

\[
\boxed{
G_{36}
=
SU(2)^{18}.
}
\]

The source-derived transporter is

\[
\boxed{
\rho_{18}(\Lambda)
=
(\rho_1(\Lambda),\ldots,\rho_{18}(\Lambda)).
}
\]

This is not identified with a Standard-Model gauge group.

## 8. Single-CP1 selector firewall

The exact 18-pair source does not contain a rule selecting one pair or one
weighted combination of pairs as the unique \(CP^1\) carrier.

Therefore a collapse

\[
(CP^1)^{18}\to CP^1
\]

requires an additional source-typed selector/intertwiner.

Until such an operator is derived:

\[
\boxed{
\text{single-}CP^1\text{ MUMMU projection is not canonical.}
}
\]

The correct source-preserving carrier is \((CP^1)^{18}\).

## 9. Consequence for orbital algebra

For an orbital word \(w\), the state is refined to

\[
\boxed{
x_w=
\left(
w,
\Pi_{18}[\theta_w],
\varphi_w,
r_w,
\tau_w
\right).
}
\]

The orbital path representation becomes

\[
\boxed{
\rho_{18}:
\mathsf{Path}(\mathcal O)
\to
SU(2)^{18}.
}
\]

The previously defined MUMMU obstruction may therefore be evaluated pairwise,
retaining the ordered 18-component vector rather than collapsing it with
arbitrary weights.

## 10. Claim ledger

| Statement | Status |
|---|---|
| PNCS T36 uses 18 complementary pairs | `EXACT IMPORTED EXPERIMENTAL CONTRACT` |
| pair spinor/projector formula | `EXACT` |
| pair Bloch vector is equatorial | `EXACT` |
| common center phase cancels projectively | `EXACT` |
| \(\Pi_{18}:T^{36}\to(CP^1)^{18}\) uses all coordinates once | `EXACT GIVEN SOURCE PAIRING` |
| pair connection reduces to \(-i\sigma_z d\delta/2\) | `EXACT` |
| source \(\delta_j=2\omega_jt\) gives \(\rho_j=e^{-i\omega_j\Delta t\sigma_z}\) | `EXACT` |
| natural uncoupled transport group is \(SU(2)^{18}\) | `EXACT PRODUCT CONSTRUCTION` |
| unique collapse to one CP1 | `OPEN / NO SOURCE SELECTOR` |
| physical interpretation of the 18 factors | `OPEN / NOT CLAIMED` |

## 11. Validation

Deterministic validator:

`TIR/validation/tir_mummu_t36_cp1_pair_projection_v0_1.py`

Static receipt:

`TIR/validation/TIR_MUMMU_T36_CP1_PAIR_PROJECTION_VALIDATION_V0_1.json`

## 12. Remaining gate

The projection ambiguity has been reduced from arbitrary T36 coordinate
selection to one explicit question:

\[
\boxed{
\text{Is there a source-derived coupling/selector }
\mathcal J:(CP^1)^{18}\to\mathcal Y
\text{ required by MUMMU?}
}
\]

No such \(\mathcal J\) is introduced here.
