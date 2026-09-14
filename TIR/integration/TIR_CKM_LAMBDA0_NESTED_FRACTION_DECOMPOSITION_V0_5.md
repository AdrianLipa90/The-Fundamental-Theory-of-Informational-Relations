# TIR CKM lambda0 Nested-Fraction Decomposition v0.5

Status: `EXACT_RATIONAL_IDENTITY / INDEPENDENT_PROVENANCE_CROSSCHECK / DYNAMICAL_BINDING_OPEN`

Date: 2026-09-14

## Scope

This surface preserves the unsimplified structure of the CKM base weight

\[
\lambda_0=\frac29
\]

instead of treating the reduced fraction as the only meaningful representation.
The exact identity is

\[
\boxed{
\lambda_0
=\frac{1}{4+\frac12}
=\frac{1}{9/2}
=\frac29.
}
\]

The purpose is not to promote a new physical interpretation from algebra alone.
The purpose is to test whether the denominator decomposition has independent
provenance in the already validated 600-cell, flavour, McKay and half-seam
layers.

## Route A: 600-cell incidence packet

The coordinate 600-cell reconstruction gives, exhaustively,

\[
\nu_F=2
\]

tetrahedral cells incident on each triangular face and

\[
\nu_E=5
\]

tetrahedral cells incident on each edge.

For the typed source-edge-target packet

\[
F_{\rm src}\sqcup E\sqcup F_{\rm dst},
\]

the exact packet dimension is

\[
2\nu_F+\nu_E=2+5+2=9.
\]

Hence

\[
\boxed{
\lambda_0
=\frac{\nu_F}{2\nu_F+\nu_E}
=\frac29.
}
\]

No CKM observable is used in this reconstruction.

## Route B: flavour algebra plus McKay doublet

The existing three-flavour carrier gives

\[
\dim\mathfrak{su}(3)=3^2-1=8.
\]

Adjoining the identity channel gives the full three-state matrix-channel count

\[
8+1=9.
\]

Independently, the binary-icosahedral McKay layer identifies the fundamental
representation as a doublet,

\[
d_Q=2.
\]

Therefore

\[
\boxed{
\lambda_0
=\frac{d_Q}{\dim\mathfrak{su}(3)+1}
=\frac2{8+1}
=\frac29.
}
\]

Invert before reducing:

\[
\lambda_0^{-1}
=\frac{8+1}{2}
=\frac82+\frac12
=4+\frac12.
\]

Thus

\[
\boxed{
\lambda_0
=\frac{1}{4+\frac12}.
}
\]

The decomposition is exact and retains the provenance that is erased by the
fully reduced notation `2/9`.

## Route C: independent half-seam crosscheck

The half-seam phase-fibre gate independently establishes the primitive balanced
coordinate

\[
h=\frac12.
\]

Using the already reconstructed nine-channel packet gives

\[
9h=\frac92=4+\frac12,
\]

so

\[
\boxed{
\lambda_0
=\frac1{9h}
=\frac1{4+\frac12}
=\frac29.
}
\]

This is retained as a crosscheck, not as an identification of the half-seam
mechanism with the McKay doublet. Their provenance remains distinct even though

\[
h=\frac1{d_Q}=\frac12.
\]

## Exact computational gate

The validator recomputes the 600-cell tetrahedral complex from coordinates,
checks all face and edge incidence counts, calls the existing flavour
normalization audit, calls the existing McKay representation validator, and
calls the existing half-seam audit.

It then requires exact rational equality among

\[
\frac{\nu_F}{2\nu_F+\nu_E},
\qquad
\frac{d_Q}{\dim\mathfrak{su}(3)+1},
\qquad
\frac1{(\dim\mathfrak{su}(3)+1)/d_Q},
\qquad
\frac1{9h}.
\]

All arithmetic is performed with exact `Fraction` objects rather than
floating-point comparison.

Validator:

`TIR/validation/tir_ckm_lambda0_nested_fraction_decomposition_v0_5.py`

Expected terminal identity:

```text
lambda0.reduced = 2/9
lambda0.nested = 1/(4+1/2)
lambda0.inverse = 9/2
```

## Epistemic boundary

Closed by this surface:

- the exact rational identity `2/9 = 1/(4+1/2)`;
- the 600-cell incidence derivation of `2/9`;
- the independent `SU(3)_F + identity + McKay doublet` derivation of `2/9`;
- the independent half-seam numerical crosscheck of the `9/2` denominator;
- exact agreement of the three provenance routes.

Still open:

- whether `9/2` must be interpreted physically as an effective channel count;
- the dynamical operator producing the historical additive refinement
  \(a\kappa\);
- promotion of
  \(\lambda=b+a\kappa\)
  from postdictive refinement to a prospective first-principles result.

The operational rule is therefore:

\[
\boxed{
\text{do not simplify away provenance before the structure has been audited.}
}
\]
