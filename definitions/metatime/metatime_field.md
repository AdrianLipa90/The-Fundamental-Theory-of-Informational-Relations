# Metatime Field

ID: `DEF-MTT-0002`
Layer: `definitions`
Domain: `MTT`
Status: `transcribed`
Epistemic status: `imported`
Provenance kind: `imported`

## Canonical role
The metatime field is the sector object that replaces ordinary passive time-parameter usage with a dynamical field object. In the imported source it appears as a tensor-scalar object with scalar and rank-2 components.

## Canonical transcribed statement
In the imported Metatime sector, the metatime field is written schematically as:

```text
T(x) = { tau(x), T^{mu nu}(x) }
```

where:
- `tau(x)` is the scalar metatime component,
- `T^{mu nu}(x)` is the tensor component.

Its intended role is to encode a dynamical time structure rather than a fixed background parameter.

## Imported functional meaning
The source sector attributes to the metatime field the following role set:
1. time becomes dynamical rather than merely parametric,
2. fermion-sector objects are organized relative to this field on `M_time`,
3. later spectral and oscillation sectors inherit their structure from this field geometry.

This file preserves that intended role without yet promoting it to a fully derived Foundations theorem.

## Minimal imported expression
```text
T(x) := tensor-scalar metatime field on M_time.
```

## Upstream compatibility in Foundations
At current maturity, the metatime field is admissible as a downstream imported field object if read conservatively:
- it must not outrun the primitive Foundations chain,
- it must remain downstream of locality and ordered phase motion,
- it must not be used as a canonical export until derivation paths are supplied.

Current upstream compatibility requirements:
- `DEF-MTT-0001` metatime manifold
- `AX-FND-0001`
- `AX-FND-0002`
- `AX-FND-0003`
- `DEF-FND-0004` locality
- `DEF-FND-0005` attractor

## Downstream targets
This definition is upstream to:
- `DER-MTT-0002` metatime field equations
- `DER-MTT-0003` metatime parameter tau role
- neutrino-sector later imports
- cosmology-sector later imports

## Scope guard
This file does **not** yet canonize:
- exact Lagrangian structure,
- exact equations of motion,
- numerical calibration,
- any claim that the tensor-scalar split is already re-derived from the Foundations primitive chain.

Those require later derivation-bearing documents.

## Source anchors
Imported from:
- `AdrianLipa90/Metatime`
- source anchor: `README.md`

## Migration note
This file is a canonical transcribed definition only. It records the source-side field object honestly and keeps the distinction between imported content and derived canonical content explicit.