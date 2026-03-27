# D-0001 — From Hilbert space to projective \(\mathbb{CP}^1\)

## Status
`derived`

## Depends on
- `AX-0001`
- `AX-0002`
- `DEF-0001`

## Goal
Derive the minimal Bloch / \(\mathbb{CP}^1\) state manifold from a two-level complex Hilbert space.

## Step 1 — Start with a two-level Hilbert space
Let \(\mathcal H_2 \cong \mathbb C^2\).
A nonzero state is represented by a vector:
\[
|\psi\rangle = \begin{pmatrix} a \\ b \end{pmatrix}, \qquad (a,b) \neq (0,0).
\]

## Step 2 — Quotient by nonzero complex rescaling
Physical states are rays, so:
\[
(a,b) \sim (\lambda a, \lambda b), \qquad \lambda \in \mathbb C^\times.
\]
Therefore the physical state manifold is:
\[
\mathbb P(\mathcal H_2) = \mathbb{CP}^1.
\]

## Step 3 — Normalize and remove global phase
For a normalized representative one may write:
\[
|\psi\rangle = \cos\frac{\theta}{2}|0\rangle + e^{i\phi}\sin\frac{\theta}{2}|1\rangle.
\]
This gives coordinates \((\theta,\phi)\) on the Bloch sphere picture of \(\mathbb{CP}^1\).

## Step 4 — Fubini–Study distance
For normalized rays represented by \(|\psi\rangle\) and \(|\varphi\rangle\):
\[
d_{FS}([\psi],[\varphi]) = \arccos\big(|\langle \psi | \varphi \rangle|\big).
\]
This metric is invariant under global phase and depends only on rays.

## Result
The minimal first-principles state space for the two-level sector is projective and equals \(\mathbb{CP}^1\) with induced Fubini–Study geometry.

## Downstream use
This derivation supports:
- `src/ciel_foundations/geometry/projective_state.py`
- `tests/test_projective_state.py`
- minimal Bloch initial conditions in roadmap M1
