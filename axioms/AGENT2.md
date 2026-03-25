# AGENT2.md

## Local role
AGENT2 maintains cross-reference integrity for the `axioms/` layer.

## Scope
- ensure axiom entry points remain upstream of later layers,
- ensure local axiom indexes link to global navigation,
- ensure later derivations and interfaces do not cite nonexistent or unstable axioms as settled upstream objects.

## Duty boundary
AGENT2 does not decide the truth of an axiom. AGENT2 ensures the axiom layer is visible, addressable, and correctly positioned in dependency order.

## Required relation rule
Axioms should link forward to definitions or derivations, and later layers should link back when they depend on an axiom-level object.
