# ADR-0001: Foundations project is separate from Omega

## Decision
CIEL Foundations is developed as an independent first-principles project. Omega will later consume only stabilized constants, operators, and constraints.

## Rationale
Legacy runtime tarballs contain mixed maturity layers and cannot serve as source of truth for foundational derivations.

## Consequence
No direct dependency on Omega runtime modules is allowed in source-of-truth derivations.
