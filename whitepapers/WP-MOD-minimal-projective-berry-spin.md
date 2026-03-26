# WP-MOD — Minimal Projective / Berry / Spin Foundations

## Status
`defined`

## Scope
This whitepaper collects the minimal first-principles module already frozen in the repository:
- projective ray states,
- minimal \(\mathbb{CP}^1\) / Bloch manifold,
- Fubini–Study metric,
- Berry connection and phase,
- spinorial sign under \(2\pi\),
- closure functional.

## 1. Theory chapter
### 1.1 Projective states
Physical states are rays in Hilbert space. The minimal two-level sector reduces to \(\mathbb{CP}^1\).

### 1.2 Kähler / Fubini–Study structure
The projective manifold carries the compatible geometric data needed for transport and geometric phase.

### 1.3 Berry transport
A Berry connection and Berry phase are defined over transported cycles.

### 1.4 Spinor sign
The minimal spinorial sector changes sign under a full \(2\pi\) cycle.

### 1.5 Closure functional
A compact closure-defect functional is defined for transported phase families.

## 2. Source files
- `axioms/AX-0001-projective-state-space.md`
- `axioms/AX-0002-kahler-fubini-study-structure.md`
- `axioms/AX-0003-spinor-sign-under-2pi.md`
- `definitions/DEF-0001-projective-ray-and-cp1.md`
- `definitions/DEF-0002-berry-connection-and-phase.md`
- `definitions/DEF-0003-closure-functional.md`
- `derivations/D-0001-hilbert-to-projective-cp1.md`
- `derivations/D-0002-berry-phase-and-spinor-sign.md`

## 3. Code bindings
- `src/ciel_foundations/geometry/projective_state.py`
- `src/ciel_foundations/holonomy/berry.py`
- `src/ciel_foundations/closure/euler.py`

## 4. Tests
- `tests/test_projective_state.py`
- `tests/test_berry_and_closure.py`

## 5. Numerical appendix
See:
- `LaTeX/appendices/APP-0001-minimal-cp1-berry-spin-numerical-derivations.tex`
- `Simulations/code/sim_cp1_berry_spin.py`
- `Simulations/results/ART-0001-cp1-berry-spin-demo.csv`

## 6. Epistemic note
This module is minimal. It is not yet the full closure law, not yet the white-thread layer, and not yet the tau-from-coupling layer.
