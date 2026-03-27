# WP-MOD — Phase-aware kernel composition

## Status
`defined`

## Scope
This whitepaper records the first explicit hypothesis for composing the pairwise kernel \(A_{ij}\) from already-registered piko objects.

## 1. Theory chapter
### 1.1 Abstract kernel
`DEF-0008` introduced an abstract symmetric nonnegative pairwise kernel suitable for the tau-from-coupling generator.

### 1.2 Phase-aware refinement
`DEF-0009` refines the kernel into the product
\[
A_{ij}=|W_{ij}|\,g_{\mathrm{phase}}(\gamma_i-\gamma_j;\lambda)\,g_{\mathrm{closure}}(R_H;\mu).
\]

### 1.3 Rationale
The three factors play different roles:
- \(|W_{ij}|\): coupling amplitude,
- phase alignment: coherence between pairwise phase sectors,
- closure weight: suppression under large closure defect.

## 2. Source files
- `definitions/DEF-0009-phase-aware-kernel-composition.md`
- `derivations/D-0008-kernel-from-holonomy-phase-and-closure.md`
- `interfaces/IF-0007-phase-aware-kernel-composition.yaml`

## 3. Code bindings
- `src/ciel_foundations/solvers/phase_aware_kernel_solver.py`
- `tests/test_phase_aware_kernel.py`

## 4. Epistemic note
This module is a hypothesis-level refinement of the pairwise kernel, not yet a final derived law.
