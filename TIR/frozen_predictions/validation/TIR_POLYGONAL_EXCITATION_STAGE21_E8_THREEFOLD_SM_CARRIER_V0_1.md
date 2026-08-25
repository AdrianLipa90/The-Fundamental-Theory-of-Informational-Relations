# TIR Polygonal Excitation — Stage 21 E8 Threefold SM Carrier v0.1

Status: `STAGE_21_THREEFOLD_HYPERCHARGE_CARRIER_PASS`

## Exceptional branch

From

```math
E_8\supset (E_6\times SU(3))/Z_3
```

and

```math
(27,3)\to(16,3)\oplus(10,3)\oplus(1,3),
```

the SO(10) spinor carrier occurs in the tensor product `(16,3)`.

Its dimension is

```math
16\cdot3=48.
```

## Hypercharge spectrum

Stage 16 established one exact SU(5) family carrier with multiplicities

```text
Y = +1/6   x6
Y = -2/3   x3
Y = +1     x1
Y = +1/3   x3
Y = -1/2   x2
Y = 0      x1
```

Tensoring with the SU(3) triplet gives

```text
Y = +1/6   x18
Y = -2/3   x9
Y = +1     x3
Y = +1/3   x9
Y = -1/2   x6
Y = 0      x3
```

for a total of 48 states.

## Exact consistency checks

The total hypercharge trace over the 48-state carrier is

```math
\operatorname{Tr}Y=0.
```

Each one-copy anomaly residual from Stage 16 is zero, hence the tripled carrier also gives exact zero for

```text
SU(3)^2 U(1)
SU(2)^2 U(1)
gravity^2 U(1)
U(1)^3
```

using rational arithmetic.

## Current gate

The exceptional representation fixes a multiplicity factor of three. The next TIR-specific gate is a bijection between the three SU(3) triplet weights and the three previously frozen TIR structural generation channels/seeds, derived from an existing invariant rather than label assignment.

## Reproducibility

`TIR/frozen_predictions/validation/scripts/e8_threefold_sm_carrier_stage21_v01.py`

Expected verdict: `PASS`.
