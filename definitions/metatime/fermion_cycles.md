# Fermion Cycles

ID: `DEF-MTT-0003`
Layer: `definitions`
Domain: `MTT`
Status: `transcribed`
Epistemic status: `imported`
Provenance kind: `imported`

## Canonical role
Fermion cycles are the imported Metatime sector objects that represent fermion-species structure as closed cycles on the metatime manifold `M_time`.

## Canonical transcribed statement
In the imported source formulation, fermionic objects are not treated as primitive point particles moving only through passive spacetime. Instead, each fermion sector is associated with a closed cycle `C_i` on `M_time`.

Minimal imported statement:

```text
fermion species i <-> closed cycle C_i on M_time
```

The intended consequence in the source sector is that mass and inter-sector structure depend on topological/geometric properties of these cycles.

## Imported functional meaning
The imported source attributes to `C_i` the following role set:
1. support of species distinction,
2. carrier of topological depth,
3. upstream object for later holonomy and correction structure,
4. geometric substrate for later eigenvalue and oscillation claims.

At this stage in Foundations, those roles are preserved only as imported sector semantics.

## Upstream compatibility in Foundations
A conservative compatibility reading inside Foundations is:
- a cycle object must remain downstream of locality and primitive ordered phase motion,
- it must be read as a sector-specific closed organization pattern,
- it is not yet a primitive axiom.

Current upstream dependencies:
- `DEF-MTT-0001` metatime manifold
- `DEF-MTT-0002` metatime field
- `AX-FND-0002` boundary/locality
- `AX-FND-0003` ordered phase motion
- `DEF-FND-0005` attractor

## Downstream targets
This definition is upstream to:
- `DER-MTT-0001` topological eigenvalues lambda_i
- `OP-MTT-0001` white-thread holonomy
- sector-specific later files for neutrino/lepton/quark mapping

## Scope guard
This file does **not** yet canonize:
- a complete topological classification of all `C_i`,
- a derived mass map,
- white-thread couplings,
- any numerical spectrum,
- any exact oscillation or CP formulas.

Those require later explicit derivation-bearing files.

## Source anchors
Imported from:
- `AdrianLipa90/Metatime`
- source anchor: `README.md`

## Migration note
This file is a canonical transcribed definition only. It preserves the source sector object honestly while keeping the imported status explicit until a non-arbitrary derivation path is completed.