# TIR Polygonal Excitation — Stage 48 Collatz Branch-Word Operator Interface v0.1

Status: `STAGE_48_BRANCH_WORD_INTERFACE_PASS_OPERATOR_ASSIGNMENT_OPEN`

## Purpose

Stage 47 established a unique common forward-reachable seed `n2=35`. Stage 48 encodes each deterministic path to that common seed as an exact word in the two Collatz branches

```text
O : n -> 3n+1   for odd n
E : n -> n/2    for even n.
```

This separates the already-fixed discrete dynamics from the still-open operator representation used by the phase propagator.

## Existing ordered-propagator requirement

The foundational phase-intention Hamiltonian already uses an ordered propagator of the form

```math
U_\Phi(K,0)=\mathcal T\exp\left[-i\sum_{k=0}^{K-1}\rho_s(k)\hat{\mathcal I}_s(k)\right].
```

Therefore step order is structurally relevant. The same source states that the explicit rhythm `rho_s(k)` used in reference simulations is a placeholder rather than a canonical final rule.

The repository freeze also retains the exact `W_s` operator and exact Collatz/twin-prime rhythm as open derivation debts.

## Exact branch words to the common seed

Using the Stage 47 common target `35` gives

```math
w_1=\texttt{OEOE},
```

with length `4`, odd-step count `2`, even-step count `2`, and

```math
C^{w_1}(15)=35.
```

For the middle seed,

```math
w_2=\varepsilon
```

is the empty word because the initial state is already `35`.

For the third seed,

```text
w3 = OEOEOEOEEEEOEOEEOEOEOEEOEOEOEOEEOEEEOEOEOEEOEOEEOEOEOEOEOEOEEEOEOEOEOEEEEOEEOEEOEEEEOEEEOE
```

with length `90`, odd-step count `34`, even-step count `56`, and

```math
C^{w_3}(143)=35.
```

The words are exact consequences of the Collatz map and contain no amplitude, mixing or mass input.

## Algebraic interface

Let

```math
\mathcal W=\{E,O\}^*
```

be the free monoid of Collatz branch words.

To turn the discrete orbit into a family-space propagator, the missing object is an operator representation / step map such as

```math
\Pi:\mathcal W\to U(3)_F
```

or, at generator level,

```math
E\mapsto U_E,\qquad O\mapsto U_O,
```

supplemented by the exact rhythm/weight rule required by the existing time-ordered phase propagator.

Once `U_E`, `U_O` and the canonical weights are fixed, the words above determine their ordered products with no further path ambiguity.

## Result

The family-seed Collatz dynamics has now been reduced to a completely explicit discrete input:

```text
seed values + branch words + common merge target
```

while the unresolved layer is precisely

```text
branch symbol -> family-space operator
and
exact per-step rhythm/weight.
```

## Boundary

No assignment `E -> U_E`, `O -> U_O` is selected in this stage. In particular, Stage 48 does not identify the two Collatz branches with any chosen pair of SU(3)_F generators and does not set the open rhythm to unity.

## Reproducibility

`TIR/frozen_predictions/validation/scripts/collatz_branch_word_stage48_v01.py`

Receipt:

`TIR/frozen_predictions/validation/results/TIR_POLYGONAL_STAGE48_COLLATZ_BRANCH_WORD_RECEIPT_V0_1.json`
