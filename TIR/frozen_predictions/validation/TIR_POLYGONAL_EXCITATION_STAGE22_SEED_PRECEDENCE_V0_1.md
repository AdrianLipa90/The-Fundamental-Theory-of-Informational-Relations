# TIR Polygonal Excitation — Stage 22 Seed Precedence v0.1

Status: `STAGE_22_SEED_PRECEDENCE_PASS`

## Purpose

Resolve the ordering of the three previously selected TIR structural generation seeds before identifying them with the three labels of the Stage 21 SU(3) family carrier.

## Preserved historical records

The early generation-embedding / single-kernel line ordered the selected seeds as

```text
(3,5), (11,13), (5,7)
```

with v0.5 assigning generations 1, 2, 3 in that order.

The later full-action arbitration v1.0 combines three independent structural kernels:

```text
Collatz-Poincare v0.4
tetrahedral-Poincare v0.8
spin-Fibonacci-Kepler-Collatz v0.9
```

Each kernel is normalized over the three frozen seeds and the normalized values are averaged. The resulting integrated damping values are

```text
(3,5)   0.8471633855025916
(5,7)   0.6088811663290957
(11,13) 0.23926393244694075
```

The arbitration sorts this quantity in descending order and assigns

```math
s_1=(3,5),\qquad s_2=(5,7),\qquad s_3=(11,13).
```

Euler-Berry coherence gate v1.3 carries the same `assigned_generation_v10` labels.

## Precedence rule for the present validation branch

The Stage 21 family-carrier test uses the later multi-kernel full-action arbitration as the active seed ordering:

```math
\boxed{(3,5)\to1,\quad(5,7)\to2,\quad(11,13)\to3.}
```

Earlier orderings remain preserved as historical stages. The present ordering is selected by explicit version/method precedence and the frozen full-action scalar, with zero use of particle masses in this gate.

## Claim scope

`PASS` establishes an ordered three-element TIR seed basis for subsequent representation tests. A dynamical cyclic transition between the seeds is a separate gate.

## Reproducibility

`TIR/frozen_predictions/validation/scripts/seed_precedence_stage22_v01.py`
