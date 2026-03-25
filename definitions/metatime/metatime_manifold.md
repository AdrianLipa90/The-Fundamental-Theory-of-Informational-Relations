# Metatime Manifold

ID: `DEF-MTT-0001`
Layer: `definitions`
Domain: `MTT`
Status: `transcribed`
Epistemic status: `imported`
Provenance kind: `imported`

## Canonical role
`M_time` is the configuration-space manifold assigned to the metatime sector. In the source formulation it parameterizes the configuration space of an effective tensor-scalar time field and serves as the geometric carrier for later cycle, holonomy, and spectrum constructions.

## Canonical transcribed statement
In the imported Metatime sector, `M_time` is defined as a compact Kahler manifold. The source text gives concrete toy/model options such as `S^2` and `CY_3`. Its intended role is not ordinary spacetime itself, but the configuration geometry on which the metatime field and fermion cycles are organized.

Minimal imported statement:

```text
M_time := compact Kahler configuration manifold for the metatime field sector.
```

Imported model examples:

```text
M_time ∈ { S^2, CY_3, ... }
```

## Formal imported content
The source sector assigns to `M_time`:
1. a Kahler metric `g_K`,
2. a Kahler form `ω = i ∂ ∂̄ K`,
3. compatibility with a dynamical metatime field,
4. support for closed cycles `C_i` representing fermion-sector structure.

At the current stage in Foundations, these items are preserved as imported sector content, not yet as fully re-derived canonical objects.

## Upstream compatibility in Foundations
This imported object is currently compatible with the already frozen primitive chain:

```text
Chaos -> Potential -> Relation -> Boundary -> Locality -> CP^1 -> ordered phase motion
```

Compatibility claim at this stage is weak and honest:
- `M_time` is allowed as a downstream geometric sector object,
- it is not yet licensed as an upstream primitive,
- its promotion from imported object to derived canonical object requires an explicit derivation path from the Foundations layer.

## Dependencies
Upstream Foundations dependencies currently required for honest use:
- `AX-FND-0001`
- `AX-FND-0002`
- `DEF-FND-0003` boundary
- `DEF-FND-0004` locality

Downstream Metatime objects depending on this definition:
- `DEF-MTT-0002` metatime field
- `DEF-MTT-0003` fermion cycles
- `DER-MTT-0001` topological eigenvalues
- `OP-MTT-0001` white-thread holonomy

## Scope guard
This definition does **not** yet canonize:
- the exact metric form of `g_K`,
- the exact choice `S^2` versus `CY_3`,
- any derived eigenvalue spectrum,
- any white-thread correction factors,
- any cosmological or neutrino-sector claims.

Those remain downstream and require separate derivation-bearing files.

## Source anchors
Imported from:
- `AdrianLipa90/Metatime`
- source anchor: `README.md`

## Migration note
This file is intentionally a canonical transcribed definition, not a proof. It preserves source semantics while making the epistemic status explicit.