# DEF-0012 — Dynamic path weights from semantic action

## Status
`hypothesis`

## Depends on
- `DEF-0011`

## Objects defined here
1. `OBJ-PATH-ACTION-0001`
2. `OBJ-DYNAMIC-PATH-WEIGHTS-0001`

## Path action
For each auxiliary path \(\gamma^{(a)}_{ij}\) in a loose-thread bundle, define a semantic action
\[
\mathcal S(\gamma^{(a)}) = \alpha L(\gamma^{(a)}) + \beta\,\Delta\phi(\gamma^{(a)}) + \kappa D_{\mathrm{rel}}(\gamma^{(a)}) + \mu\,\Pi_{\mathrm{truth}}(\gamma^{(a)}),
\]
with nonnegative coefficients \(\alpha,\beta,\kappa,\mu\ge 0\).

## Dynamic weights
Given a temperature/inverse-noise parameter \(\sigma\ge 0\), define the dynamic weights
\[
\alpha_a = \frac{e^{-\sigma \mathcal S(\gamma^{(a)})}}{\sum_b e^{-\sigma \mathcal S(\gamma^{(b)})}}.
\]

## Canonical role
This object is the first dynamic law for the loose-thread bundle weights. It replaces arbitrary manual weights by a normalized action-based selection rule.

## Immediate properties
1. \(\alpha_a\ge 0\)
2. \(\sum_a \alpha_a = 1\)
3. lower-action paths receive larger weights when \(\sigma>0\)

## Registered numeric trace
For the registered toy actions
\[
\mathcal S = (1.6,\ 2.9,\ 2.0),
\qquad
\sigma = 1.5,
\]
the normalized weights are
\[
\alpha \approx (0.53087315,\ 0.07574431,\ 0.39338254).
\]
For primitive amplitudes
\[
W^{(1)} = 1.0+0.0i,
\quad
W^{(2)} = 0.2+0.6i,
\quad
W^{(3)} = 0.5+0.2i,
\]
this yields
\[
W^{\mathrm{eff}} \approx 0.74224129 + 0.12412309 i.
\]

## Executable bindings
- solver: `src/ciel_foundations/solvers/dynamic_path_weights_solver.py`
- simulation: `Simulations/code/sim_dynamic_path_weights.py`
- appendix: `LaTeX/appendices/APP-0007-dynamic-path-weights-numerical-derivations.tex`

## Artifact bindings
- result: `Simulations/results/ART-0006-dynamic-path-weights-demo.csv`
- provenance: `provenance/ART-0006-provenance.yaml`
- falsification: `falsification/FM-0006-dynamic-path-weights.yaml`

## Scope restriction
This definition does not yet derive the coefficients \(\alpha,\beta,\kappa,\mu\) or the final runtime measurement operators for phase cost, relational defect, and truth penalty. It only registers the first dynamic normalized weighting law.
