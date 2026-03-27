# D-0002 — Berry phase and spinor sign in the minimal CP1 sector

## Status
`derived`

## Depends on
- `AX-0002`
- `AX-0003`
- `DEF-0002`
- `DEF-0003`

## Goal
Show how the minimal geometric phase language is compatible with the spinorial minus sign and yields a first closure functional.

## Step 1 — Berry connection on projective state space
For a normalized representative \(|\psi\rangle\), define:
\[
A_B = i\langle \psi | d\psi \rangle.
\]
For a closed cycle \(\gamma\), define the Berry phase:
\[
\gamma_B[\gamma] = \oint_\gamma A_B.
\]

## Step 2 — Minimal spinorial compatibility
The spinorial sector requires:
\[
\psi(\phi + 2\pi) = -\psi(\phi).
\]
This is equivalent to the phase condition
\[
e^{i\Phi_{2\pi}} = -1
\]
for the effective transported phase accumulated over a full spinorial cycle.

## Step 3 — Minimal geometric realization
In the simplest equatorial CP1/Bloch cycle, the geometric phase has magnitude \(\pi\) for a spin-1/2 cycle, so
\[
e^{i\gamma_B} = -1.
\]
This reproduces the spinorial sign relation geometrically.

## Step 4 — Closure functional
For a finite transported phase family \(\{\phi_k\}\), define:
\[
\Delta_H = \sum_k e^{i\phi_k},
\qquad
R_H = |\Delta_H|^2.
\]
This yields a compact measurable defect for phase closure without yet freezing the exact admissibility threshold.

## Result
The minimal CP1 sector already supports:
1. geometric phase accumulation,
2. spinorial sign under 2π transport,
3. a closure-defect functional suitable for later acceptance / rollback logic.

## Downstream use
This derivation supports:
- `src/ciel_foundations/holonomy/berry.py`
- `src/ciel_foundations/closure/euler.py`
- `tests/test_berry_and_closure.py`
- `Simulations/code/sim_cp1_berry_spin.py`
