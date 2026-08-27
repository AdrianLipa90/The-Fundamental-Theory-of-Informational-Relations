# TIR Polygonal Excitation — Stage 16 Exceptional Hypercharge Match v0.1

Status: `STAGE_16_EXACT_HYPERCHARGE_REPRESENTATION_PASS`

## Scope

Pure representation arithmetic linking the Stage 14 exceptional chain to the already-frozen TIR v3.8 one-generation hypercharge skeleton. Active inputs contain no masses, PDG tables, CKM, PMNS or atomic observables.

## Branching route used

The standard exceptional/unitary chain used by the audit is

```text
E7 -> E6 x U(1)
E8 -> E6 x SU(3)
E6 27 -> SO(10): 16 + 10 + 1
SO(10) 16 -> SU(5): 10 + bar(5) + 1
SU(5) -> SU(3) x SU(2) x U(1)_Y
```

Dimension closures checked by the script include

```text
133 = 78 + 27 + 27 + 1
248 = 78 + 8 + 3*27 + 3*27
27 = 16 + 10 + 1
16 = 10 + 5 + 1
```

## Exact SU(5) hypercharge generator

Use the traceless fundamental generator

```math
Y_5=\operatorname{diag}\left(-\frac13,-\frac13,-\frac13,\frac12,\frac12\right).
```

Its trace is exactly zero.

### The 10 = wedge^2 5

Weights of the antisymmetric tensor are pairwise sums of the fundamental weights. Exact enumeration gives

```text
Y = +1/6   multiplicity 6
Y = -2/3   multiplicity 3
Y = +1     multiplicity 1
```

matching the TIR v3.8 left-handed Weyl pattern

```text
Q   : 6 states, Y = +1/6
u^c/u_c sector used here: u_c : 3 states, Y = -2/3
e_c : 1 state, Y = +1
```

### The bar(5)

Opposite fundamental weights give

```text
Y = +1/3   multiplicity 3
Y = -1/2   multiplicity 2
```

matching

```text
d_c : 3 states, Y = +1/3
L   : 2 states, Y = -1/2
```

The SU(5) singlet has

```text
Y = 0
```

and supplies an anomaly-neutral singlet channel.

## Independent anomaly replay

Using exactly the v3.8 hypercharges,

```math
Y_Q=\frac16,\quad
Y_u=-\frac23,\quad
Y_d=\frac13,\quad
Y_L=-\frac12,\quad
Y_e=1,
```

the script re-evaluates

```math
2Y_Q+Y_u+Y_d=0,
```

```math
3Y_Q+Y_L=0,
```

```math
6Y_Q+3Y_u+3Y_d+2Y_L+Y_e=0,
```

```math
6Y_Q^3+3Y_u^3+3Y_d^3+2Y_L^3+Y_e^3=0.
```

All residuals are exactly zero as rational numbers.

## Result

The exceptional chain reached from the N=4/N=5 McKay stages contains a representation path whose SU(5) hypercharge weights reproduce the previously derived TIR v3.8 one-generation hypercharge pattern exactly, including multiplicities and anomaly cancellation.

Next gate: compare the N=4/E7 and N=5/E8 branch multiplicities around the common E6 core before assigning any physical family meaning.

## Reproducibility

Script:

`TIR/frozen_predictions/validation/scripts/exceptional_hypercharge_stage16_v01.py`

Expected verdict: `PASS`.

## Standard mathematical references

- J. McKay, *Graphs, singularities, and finite groups*.
- R. Slansky, *Group Theory for Unified Model Building*, Physics Reports 79 (1981).
