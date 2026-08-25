# TIR Polygonal Excitation — Stage 28 Discrete Gauge–Matter Action v0.1

Status: `STAGE_28_DISCRETE_GAUGE_MATTER_ACTION_PASS`

## Inputs

TIR v4.1 supplies the plaquette / loop term

```math
S_W\propto 3-\operatorname{Re}\operatorname{Tr}U_p,
```

with

```math
U_p=W_{01}W_{12}W_{20}.
```

Stage 27 supplies the gauge-scalar quark-link bilinear

```math
B_{ij,f}=q_{i,f}^\dagger W_{ij}q_{j,f}.
```

## Combined discrete action form

For arbitrary real normalization symbols `beta` and `eta`, define

```math
S_{graph}[W,q]
=
\beta\sum_p\left(3-\operatorname{Re}\operatorname{Tr}U_p\right)
-
\eta\sum_{\langle ij\rangle,f}
\operatorname{Re}\left(q_{i,f}^\dagger W_{ij}q_{j,f}\right).
```

Here `f=1,2,3` is the Stage 25 family label, while `W_ij` acts on color.

## Local gauge transformation

```math
q_{i,f}\mapsto G_iq_{i,f},
\qquad
W_{ij}\mapsto G_iW_{ij}G_j^\dagger.
```

The loop transforms by conjugation at its base node,

```math
U_p\mapsto G_0U_pG_0^\dagger,
```

so its trace is invariant. Each matter-link bilinear is independently invariant by Stage 27. Therefore

```math
\boxed{S_{graph}[W',q']=S_{graph}[W,q]}
```

for every real `beta, eta`.

## Computational audit

A deterministic three-node triangle with three family copies was tested using SU(3) links and independent local SU(3) transformations at every node. The numerical residuals were

```text
full action residual:  3.3306690738754696e-15
Wilson term residual:  2.4424906541753444e-15
matter term residual:  1.3322676295501878e-15
```

The test values of `beta` and `eta` serve only as an invariance witness; the proof is coefficient-independent.

## Result

The existing TIR holonomic color sector and the Stage 27 quark-link source term compose into one locally gauge-invariant discrete gauge–matter action form across the three-family carrier.

Normalization, continuum scale matching, and running remain subsequent quantitative gates. The structural gauge–matter interface is closed at the graph/action level.

## Reproducibility

`TIR/frozen_predictions/validation/scripts/discrete_gauge_matter_stage28_v01.py`
