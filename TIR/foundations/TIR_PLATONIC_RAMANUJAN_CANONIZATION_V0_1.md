# TIR Platonic–Ramanujan Canonization v0.1

Status: `CANONICAL_STRUCTURAL_LAYER / PHYSICAL_BINDING_OPEN / PHASENAV_RUNTIME_ACTIVATION_REJECTED_V0_1`

Date: 2026-09-11

## Canonical promotion

The exact finite spectral statements in `TIR_PLATONIC_RAMANUJAN_SPECTRAL_CARRIER_V0_1.md` are promoted as a TIR structural layer:

\[
G_{36}=I_{12}\square K_3,
\qquad |V|=36,
\qquad |E|=126,
\qquad \deg G_{36}=7.
\]

Its exact nontrivial spectral radius and normalized Laplacian gap are

\[
\rho_{nt}=2+\sqrt5<2\sqrt6,
\qquad
\gamma_{36}=\frac{5-\sqrt5}{7}.
\]

Thus `G36` is a finite 7-regular Ramanujan graph. The degree identity

\[
7=L_3=L_4+L_5=2+5
\]

is retained as a structural crosscheck of the already-independent Platonic L-constant derivation, not as a replacement derivation.

The five Platonic skeleton graphs remain exact finite Ramanujan-graph statements under the validator.

## Exact dynamical corollary

For the isolated candidate phase operator

\[
C_i^{PR}=-\frac{\beta}{7}\sum_j A_{ij}\sin(\phi_i-\phi_j),
\qquad \beta\ge0,
\]

the disagreement potential

\[
V=\sum_{(i,j)\in E}[1-\cos(\phi_i-\phi_j)]
\]

obeys

\[
\dot V=-\frac{\beta}{7}\|\nabla V\|^2\le0.
\]

This isolated Lyapunov identity is canonical mathematics. It does not imply global synchronization and does not imply stability of the full PhaseNav runtime.

## Runtime evidence boundary

A fresh live-derived comparative benchmark was run against the current 36D PhaseNav state. The exact one-step target residual remained at floating-point roundoff, and the sparse edge-list evaluation of the isolated operator was faster than its dense reference in the measured host microbenchmark. However, paired perturbation recovery in a parent-like read-only v0.32 free-evolution model worsened for every tested positive beta. Therefore:

```text
G36 finite spectral carrier                 CANONICAL
Platonic finite Ramanujan theorem           CANONICAL
isolated Lyapunov theorem                   CANONICAL
sparse support/operator API                 CANONICAL_DISABLED_COMPONENT
additive C_PR activation in parent v0.32    REJECTED_V0_1
support-masking parent adaptive g           OPEN_SEPARATE_GATE
orbital Wigner/Gaunt equivalence            OPEN
physical binding                            OPEN
```

The runtime rejection is evidence preservation, not a rejection of the mathematical carrier.

## Evidence

TIR validator:

`TIR/validation/tir_platonic_ramanujan_spectral_carrier_v0_1.py`

Reference verdict: `PASS`.

PhaseNav comparative receipt:

`provenance/receipts/PNCS_PLATONIC_RAMANUJAN_LIVE_COMPARATIVE_BENCHMARK_20260911.json`

on repository `AdrianLipa90/PhaseNav-Natural-Coding-System`.

No Standard-Model, GR, cosmology, orbital-physics, QPU, H200, or physical-laboratory claim is promoted by this canonization.