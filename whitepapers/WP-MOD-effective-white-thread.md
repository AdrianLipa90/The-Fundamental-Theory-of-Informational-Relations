# WP-MOD — Effective White-Thread from a loose-thread bundle

## Status
`defined`

## Scope
This whitepaper records the first dressed extension of the White-Thread primitive via a normalized bundle of auxiliary transport channels.

## 1. Theory chapter
### 1.1 Loose-thread bundle
For a fixed pair \((i,j)\), introduce a finite family of primitive transport channels \(\gamma_{ij}^{(a)}\).

### 1.2 Effective White-Thread
Define the convexly weighted aggregate
\[
W_{ij}^{\mathrm{eff}} = \sum_a \alpha_a W_{ij}^{(a)},
\qquad \alpha_a\ge 0,
\qquad \sum_a\alpha_a=1.
\]

### 1.3 Properties
The aggregate reduces to the primitive object in the one-channel limit and remains bounded by one when the primitive amplitudes are bounded by one.

## 2. Source files
- `definitions/DEF-0011-loose-thread-bundle-and-effective-white-thread.md`
- `derivations/D-0010-effective-white-thread-from-loose-thread-bundle.md`
- `interfaces/IF-0009-effective-white-thread.yaml`

## 3. Code bindings
- `src/ciel_foundations/solvers/effective_white_thread_solver.py`
- `tests/test_effective_white_thread.py`

## 4. Epistemic note
This module is the first normalized dressing of White-Thread transport. It does not yet derive dynamic bundle weights or non-abelian path selection.
