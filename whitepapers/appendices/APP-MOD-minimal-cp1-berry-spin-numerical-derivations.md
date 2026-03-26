# Appendix — Numerical Derivations for the Minimal CP1 / Berry / Spin Module

## Status
`derived`

## Scope
This appendix records the minimal step-by-step numerical derivations backing the first executable foundations layer.

## 1. State normalization
For a raw state \((a,b)\in\mathbb C^2\setminus\{0\}\):
\[
|\psi\rangle = \frac{1}{\sqrt{|a|^2+|b|^2}}\begin{pmatrix}a\\b\end{pmatrix}.
\]

## 2. Bloch parametrization
A normalized representative may be written as
\[
|\psi(\theta,\phi)\rangle = \cos\frac{\theta}{2}|0\rangle + e^{i\phi}\sin\frac{\theta}{2}|1\rangle.
\]
For the equatorial cycle used in the toy solver:
\[
\theta = \frac{\pi}{2}.
\]

## 3. Berry connection and phase
With the toy connection component
\[
A_\phi = q(1-\cos\theta),\qquad q=\frac12,
\]
we obtain on the equator
\[
A_\phi = \frac12.
\]
Therefore the phase accumulated over the full cycle is
\[
\gamma_B = \int_0^{2\pi} A_\phi\,d\phi = \pi.
\]
This gives the spinorial sign
\[
e^{i\gamma_B} = -1.
\]

## 4. Closure-functional check
For the simple phase pair \((0,\pi)\):
\[
\Delta_H = e^{i\cdot 0} + e^{i\pi} = 1-1=0,
\qquad
R_H = |\Delta_H|^2 = 0.
\]
This is the minimal exact closure check used by the test suite.

## 5. Executable bindings
- `src/ciel_foundations/geometry/projective_state.py`
- `src/ciel_foundations/holonomy/berry.py`
- `src/ciel_foundations/closure/euler.py`
- `src/ciel_foundations/solvers/minimal_cp1_berry_spin_solver.py`
- `tests/test_projective_state.py`
- `tests/test_berry_and_closure.py`
- `tests/test_minimal_cp1_berry_spin_solver.py`
- `Simulations/code/sim_cp1_berry_spin.py`
- `Simulations/results/ART-0001-cp1-berry-spin-demo.csv`
