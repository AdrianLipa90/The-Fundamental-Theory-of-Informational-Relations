# DEF-0002 — Berry connection and phase

## Status
`defined`

## Depends on
- `AX-0002`
- `AX-0003`
- `DEF-0001`

## Objects defined here
1. `OBJ-BERRY-CONNECTION-0001`
2. `OBJ-BERRY-PHASE-0001`
3. `OBJ-SPIN-BUNDLE-0001`

## Berry connection
For a normalized local representative \(|\psi\rangle\), define the Berry one-form:
\[
A_B = i\langle \psi | d\psi \rangle.
\]

## Berry phase
For a closed cycle \(\gamma\):
\[
\gamma_B[\gamma] = \oint_\gamma A_B.
\]

The Berry phase is geometric: it depends on the transported ray and the cycle, not on an arbitrary global phase choice of the representative.

## Spin-bundle role
The minimal spinorial sector is encoded through a double-valued lift of orbital phase. In the minimal model, compatibility requires the sign relation:
\[
\psi(\phi + 2\pi) = -\psi(\phi).
\]

## Canonical role
This object binds geometry to transport. It is the immediate upstream formal object for closure, holonomy, and later white-thread derivations.

## Falsification target
A downstream code path that produces a Berry phase dependent on a pure global-phase gauge transformation violates this definition.
