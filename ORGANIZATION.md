# Organization and Methodology

## Methodology
1. Register the object.
2. State assumptions.
3. Write the formal definition.
4. Write the derivation.
5. Implement code.
6. Add tests.
7. Register artifacts/results.
8. Add interpretation only after the formal layer is stable.

## Review gates
A module cannot move to `derived` status unless:
- assumptions are explicit
- interface is explicit
- tests exist
- falsification target exists
- artifact lineage can be traced

## Epistemic statuses
- `axiom`
- `defined`
- `derived`
- `fitted`
- `empirical_input`
- `hypothesis`
- `deprecated`

## Artifact discipline
Every generated artifact must have:
- ID
- hash
- creation date
- code source
- parameters/environment
- linked derivation and whitepaper

## Interpretation discipline
Interpretation is explanatory only. It cannot introduce new equations, new constants, or new dependencies.
