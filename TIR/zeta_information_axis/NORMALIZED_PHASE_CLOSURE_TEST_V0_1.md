# Normalized Phase-Closure Test v0.1

Status: `EXACT_NORMALIZATION_RESULT / PI_TOPOLOGICAL_OBSTRUCTION_FAIL / RADIAN_REPRESENTATION_OBSTRUCTION_RETAINED / NONLOCALITY_CAUSAL_CLAIM_OPEN`

Date: 2026-09-11

Parent: `PI_PHASE_CLOSURE_OBSTRUCTION_V0_1.md`

## Question

Does the proposed `pi` closure obstruction survive after the phase coordinate is normalized from radians to turns,

```text
q = phi / (2*pi) in R/Z ?
```

This test separates three different statements that must not be conflated:

1. topological recurrence/closure;
2. standard radian representation;
3. finite-rational numerical representation.

## Exact normalization

The circle can be represented intrinsically as the quotient group

```text
R/Z.
```

The standard radian chart is the coordinate map

```text
phi = 2*pi*q.
```

A lifted closed path satisfies

```text
Delta q = w in Z,
```

so the winding number is simply

```text
w = integral dq in Z.
```

No occurrence of `pi` is required in this exact normalized closure law.

The radian form

```text
w = (1/(2*pi)) * integral dphi
```

is the same statement after the coordinate conversion `phi=2*pi*q`.

Therefore the hypothesis

```text
pi is intrinsically required for topological winding closure
```

is falsified by normalization.

The correct statement is narrower:

```text
2*pi is the closure period of the standard radian coordinate.
```

## Exact rational turn cycles

For every positive integer `n`, the normalized step

```text
Delta q = 1/n
```

closes exactly after `n` steps:

```text
n*(1/n) = 1 = 0 mod 1.
```

This computation is exact in rational arithmetic and has zero closure residual. The accompanying validator checks orders

```text
2, 3, 4, 5, 7, 12, 24, 60.
```

Thus base-12 and base-60 do not make `pi` rational, but normalized rational phase cycles can still close exactly without representing `pi` at all.

This does not imply that every possible phase coordinate is rational. An arbitrary irrational `q` can still require an infinite numerical representation. That is a generic real-number representation issue, not a special obstruction caused by `pi`.

## U(1) holonomy

The standard angular character is

```text
U(q) = exp(2*pi*i*q).
```

Equivalently, with `phi=2*pi*q`,

```text
U(phi) = exp(i*phi).
```

The group coordinate closes as

```text
q ~ q + n,  n in Z,
```

while the radian coordinate closes as

```text
phi ~ phi + 2*pi*n.
```

The numerical validator checks that both representations produce the same `U(1)` element for representative rational turns. The exact quotient-group closure rule itself is `mod 1` and does not require a numerical value of `pi`.

Hence:

```text
intrinsic U(1) quotient closure obstruction from pi = FAIL
radian-coordinate finite-rational pi representation obstruction = PASS
```

## Spin-1/2 double cover

In normalized projective windings, the spinor sheet sign can be written without radians as

```text
sheet_sign(w) = (-1)^w.
```

Therefore

```text
w=1 -> -1,
w=2 -> +1.
```

The familiar `2*pi` sign change and `4*pi` restoration are the radian-coordinate expression of the same double-cover rule.

Again, `pi` is not an intrinsic obstruction to stating or exactly evaluating the discrete sheet-closure relation.

## Consequence for kappa

The current TIR chain distinguishes the model-level normalized information assignment

```text
dI/dq = ln(2)/12
```

from its radian-coordinate form. Since

```text
phi = 2*pi*q,
dq/dphi = 1/(2*pi),
```

we have the conditional coordinate conversion

```text
dI/dphi = (dI/dq)*(dq/dphi)
        = (ln(2)/12)/(2*pi)
        = ln(2)/(24*pi).
```

Thus, within this existing conditional construction, `pi` enters `kappa` as the Jacobian between normalized turns and radians. This is a stronger and more precise statement than saying that `pi` prevents closure.

It does not independently promote the model premise `dI/dq=ln(2)/12`.

## Nonlocality boundary

A phase-dependent correlation can always be rewritten from a radian angle `theta` to a normalized turn `x=theta/(2*pi)`. For example,

```text
cos(theta) = cos(2*pi*x).
```

This coordinate change does not remove or generate physical nonlocality. Bell-type nonlocality depends on the correlation structure and assumptions of locality, not on whether the phase coordinate is written in radians or normalized turns.

Therefore the claim

```text
pi causes quantum nonlocality
```

remains `OPEN / NOT ESTABLISHED` and is not promoted by this test.

## Verdict

```text
H0: pi intrinsically prevents winding closure                         FAIL
H1: pi intrinsically prevents U(1) quotient closure                   FAIL
H2: spin-1/2 double-cover closure intrinsically requires numeric pi   FAIL
H3: standard radian representation carries a 2*pi closure scale       PASS
H4: finite rational numerics represent radian pi exactly              FAIL
H5: normalized rational turn cycles can close exactly without pi      PASS
H6: current conditional kappa inherits pi through q->phi Jacobian     PASS
H7: pi causes physical quantum nonlocality                             OPEN / NOT ESTABLISHED
```

The resulting classification is:

```text
pi = radian phase-scale / coordinate-conversion constant
pi != intrinsic topological closure obstruction
finite-rational pi residual = representation obstruction only
nonlocality causal bridge = OPEN
```

## Executable witness

Implementation:

```text
src/critical_axis/phase_closure.py
```

Tests:

```text
tests/test_phase_closure.py
```

The exact closure tests use Python `Fraction` arithmetic. Numerical complex exponentials are used only to cross-check equivalence of normalized-turn and radian holonomy representations.
