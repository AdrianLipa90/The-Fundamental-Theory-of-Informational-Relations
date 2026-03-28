# DEF-0011 — Loose-thread bundle and effective White-Thread

## Status
`hypothesis`

## Depends on
- `DEF-0010`

## Objects defined here
1. `OBJ-LOOSE-THREAD-BUNDLE-0001`
2. `OBJ-EFFECTIVE-WHITE-THREAD-0001`

## Loose-thread bundle
For a fixed ordered pair \((i,j)\), define a finite family of admissible auxiliary transport paths
\[
\mathcal L_{ij} = \{\gamma_{ij}^{(a)}\}_{a=1}^{M}
\]
with associated primitive White-Thread amplitudes
\[
W_{ij}^{(a)} = W_{ij}[\gamma_{ij}^{(a)}].
\]
These are called the loose-thread bundle for the pair \((i,j)\).

## Effective White-Thread
Given nonnegative weights \(\alpha_a\ge 0\) satisfying
\[
\sum_{a=1}^{M} \alpha_a = 1,
\]
define the effective White-Thread amplitude by
\[
W_{ij}^{\mathrm{eff}} = \sum_{a=1}^{M} \alpha_a W_{ij}^{(a)}.
\]

## Canonical role
This object is the first dressed extension beyond the single-path primitive. It models a controlled aggregation of auxiliary transport channels without yet introducing a full non-abelian or dynamically reweighted bundle law.

## Immediate bound
If each primitive amplitude satisfies \(|W_{ij}^{(a)}|\le 1\), then
\[
|W_{ij}^{\mathrm{eff}}|\le 1
\]
by convexity and the triangle inequality.

## Registered numeric trace
For the registered one-channel reduction,
\[
W_{ij}^{\mathrm{eff}} = W_{ij}^{(1)}
\]
when \(\alpha_1=1\).
For the registered two-channel toy example,
\[
W_{ij}^{\mathrm{eff}} = 0.5(0.6+0.0i)+0.5(0.0+0.8i)=0.3+0.4i,
\qquad
|W_{ij}^{\mathrm{eff}}|=0.5.
\]
Hence the convex bound remains satisfied.

## Executable bindings
- solver: `src/ciel_foundations/solvers/effective_white_thread_solver.py`
- tests: `tests/test_effective_white_thread.py`
- section: `LaTeX/sections/SEC-0008-effective-white-thread.tex`

## Artifact bindings
- upstream primitive artifact: `Simulations/results/ART-0005-white-thread-primitive-demo.csv`
- downstream dynamic-weight artifact: `Simulations/results/ART-0006-dynamic-path-weights-demo.csv`

## Scope restriction
This definition does not yet specify how the weights \(\alpha_a\) are generated dynamically. It only registers the first normalized aggregation law for loose-thread bundles.
