# WP-MOD — Local attractor hierarchy and nonlocal holonomic vortices

## Status
`defined`

## Scope
This whitepaper records the foundations-layer extension from the minimal projective/Berry/spin module to rotating local attractors and nonlocal holonomic vortices in spacetime.

## 1. Theory chapter
### 1.1 Local attractor hierarchy
Every bounded or stabilized object is modeled as carrying a local attractor \(A_i\) that organizes local relational flow.

### 1.2 Rotating order parameter
In a neighborhood of \(A_i\), define a complex order parameter
\[
\Psi_i = \sqrt{\rho_i}e^{i\theta_i}.
\]
A nonzero local angular velocity defines an axis, poles, and equator.

### 1.3 Coriolis term
The rotating local frame contributes the standard Coriolis-like term
\[
F_{C,i} = -2\Omega_i \times u_i.
\]

### 1.4 Nonlocal holonomic vortex
Using the spacetime phase-flow one-form \(u^{(i)}_\mu\), define the spacetime-loop circulation
\[
\Gamma_i[\mathcal C] = \oint_{\mathcal C} u^{(i)}_\mu dx^\mu.
\]
A nonlocal holonomic vortex is present whenever \(\Gamma_i[\mathcal C] \neq 0\).

## 2. Source files
- `axioms/AX-0005-local-attractor-hierarchy.md`
- `definitions/DEF-0005-local-attractor-and-order-parameter.md`
- `definitions/DEF-0006-nonlocal-holonomic-vortex.md`
- `derivations/D-0004-local-attractor-axis-and-coriolis.md`
- `derivations/D-0005-spacetime-holonomic-circulation.md`

## 3. Code bindings
- `src/ciel_foundations/solvers/nonlocal_holonomic_vortex_solver.py`
- `tests/test_nonlocal_holonomic_vortex.py`
- `Simulations/code/sim_nonlocal_holonomic_vortex.py`

## 4. Epistemic note
This module formalizes a foundations-layer rotating-flow and spacetime-circulation structure. It does not yet constitute the full white-thread layer, the tau-from-coupling layer, or a sector-scale physical fit.
