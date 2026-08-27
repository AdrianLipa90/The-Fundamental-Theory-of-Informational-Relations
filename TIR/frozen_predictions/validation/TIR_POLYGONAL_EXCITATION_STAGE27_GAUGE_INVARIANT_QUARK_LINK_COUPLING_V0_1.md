# TIR Polygonal Excitation — Stage 27 Gauge-Invariant Quark-Link Coupling v0.1

Status: `STAGE_27_QUARK_LINK_COUPLING_PASS`

## Input rule from TIR v4.0

The holonomic color link satisfies

```math
W_{ij}\in SU(3)_C,
\qquad
W_{ij}\mapsto G_iW_{ij}G_j^\dagger,
```

while a quark color triplet at node `i` transforms as

```math
q_i\mapsto G_i q_i.
```

## Parameter-free link bilinear

Define

```math
B_{ij}=q_i^\dagger W_{ij}q_j.
```

Under the local transformation,

```math
B_{ij}'
=q_i^\dagger G_i^\dagger
(G_iW_{ij}G_j^\dagger)
G_jq_j
=q_i^\dagger W_{ij}q_j
=B_{ij}.
```

Therefore

```math
\boxed{B_{ij}'=B_{ij}}
```

exactly.

The reverse-link rule `W_ji=W_ij^dagger` gives

```math
B_{ji}=B_{ij}^*.
```

Hence the real edge contribution

```math
S_{ij}^{(qW)}=-\operatorname{Re}B_{ij}
```

is an exact local gauge scalar.

## Family extension

Using Stage 25,

```math
W_{ij}^{(3F)}=W_{ij}\otimes I_{3,F}.
```

The same bilinear is therefore replicated over the three family labels while the color link remains family-blind.

## Computational audit

A deterministic SU(3) test constructs `W_ij`, `G_i`, and `G_j` by exponentiating traceless Hermitian Gell-Mann combinations. The measured residuals are

```text
gauge-invariant bilinear residual: 2.2887833992611187e-16
reverse-link conjugacy residual:    1.1443916996305594e-16
W unitarity residual:               2.288105085202532e-16
|det(W)-1|:                         1.7115916575508467e-18
```

## Result

The TIR `W_ij` transformation rule already supplies an exact gauge-invariant quark-link coupling form. This closes the graph-level matter/source coupling interface required by the v4.1 continuation.

Continuum normalization and running-coupling calibration remain explicit later gates; the present result is the parameter-free gauge-covariant structural coupling.

## Reproducibility

`TIR/frozen_predictions/validation/scripts/quark_link_coupling_stage27_v01.py`
