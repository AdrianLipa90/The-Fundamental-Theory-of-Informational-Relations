# WP-MOD — Dynamic path weights from semantic action

## Status
`defined`

## Scope
This whitepaper records the first dynamic law for loose-thread bundle weights using a semantic action over candidate paths.

## 1. Theory chapter
### 1.1 Path action
Each candidate path carries a scalar action built from length, phase cost, relational defect, and truth penalty.

### 1.2 Dynamic weights
The bundle weights are chosen by the normalized rule
\[
\alpha_a = \frac{e^{-\sigma \mathcal S_a}}{\sum_b e^{-\sigma \mathcal S_b}}.
\]

### 1.3 Effective White-Thread
The resulting action-driven effective amplitude is
\[
W_{ij}^{\mathrm{eff}} = \sum_a \alpha_a W_{ij}^{(a)}.
\]

## 2. Source files
- `definitions/DEF-0012-dynamic-path-weights-from-semantic-action.md`
- `derivations/D-0011-dynamic-softmax-weights-from-semantic-action.md`
- `interfaces/IF-0010-dynamic-path-weights.yaml`

## 3. Code bindings
- `src/ciel_foundations/solvers/dynamic_path_weights_solver.py`
- `tests/test_dynamic_path_weights.py`
- `Simulations/code/sim_dynamic_path_weights.py`

## 4. Epistemic note
This module is the first dynamic weighting law for loose-thread bundles. It does not yet derive the final runtime measurement operators or the values of the action coefficients.
