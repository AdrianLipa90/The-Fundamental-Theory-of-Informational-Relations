# DEF-0001 — Projective ray and minimal \(\mathbb{CP}^1\) state space

## Status
`defined`

## Depends on
- `AX-0001`
- `AX-0002`

## Objects defined here
1. `OBJ-STATE-RAY-0001`
2. `OBJ-CP1-0001`
3. `OBJ-FS-METRIC-0001`

## Definition
A physical state is a ray:
\[
[\psi] = \{ \lambda \psi : \lambda \in \mathbb C^\times \}
\subset \mathcal H.
\]

For a minimal two-level sector, projective state space is:
\[
\mathbb P(\mathcal H_2) \simeq \mathbb{CP}^1.
\]

This is the minimal Bloch / spinor state manifold used in the first foundations layer.

## Fubini–Study metric
For normalized representatives \(|\psi\rangle, |\phi\rangle\), the projective distance is:
\[
d_{FS}([\psi],[\phi]) = \arccos\big(|\langle \psi | \phi \rangle|\big).
\]

In coordinates induced on \(\mathbb{CP}^1\), this defines the minimal Kähler metric used downstream.

## Canonical role
This object is the minimal state-space target for:
- Berry transport,
- spinorial sign,
- closure functional,
- later holonomy and tau derivation.

## Interface requirement
Code must operate on rays or normalized representatives with explicit projective invariance.

## Falsification target
A code path that changes observable results under multiplication of a state by a global phase violates this definition.
