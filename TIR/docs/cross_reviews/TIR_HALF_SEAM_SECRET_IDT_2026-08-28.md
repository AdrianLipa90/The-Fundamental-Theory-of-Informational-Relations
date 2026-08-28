# TIR ↔ Secret of a Half ↔ Informational Dynamics of Time crosslink — 2026-08-28

Status: `TIR_ONLY_CROSSLINK_CANDIDATE`

This record registers a TIR-owned structural bridge. The two sibling repositories
are reference consumers in this pass; source changes are confined to TIR.

## TIR source theorem

Canonical candidate source:

`TIR/integration/TIR_RELATIONAL_HALF_SEAM_CROSSLINK_V0_1.md`

For the affine normalized coordinate `u in [0,1]` of the intermediate
relational domain `2`, define

\[
w_{1|2}=1-u,\qquad w_{3|2}=u,\qquad J_2(u)=1-u.
\]

The equal-share meeting set and the fixed-point set coincide:

\[
\boxed{
\{u:w_{1|2}=w_{3|2}\}
=\operatorname{Fix}(J_2)
=\left\{\frac12\right\}.
}
\]

With binary relational entropy,

\[
\boxed{H_{13|2}(1/2)=\ln2},
\]

and with projective odds `q=u/(1-u)`,

\[
\boxed{q(1/2)=1},\qquad q(J_2u)=q(u)^{-1}.
\]

The resulting TIR packet is

```text
u_star              = 1/2
w_1_given_2          = 1/2
w_3_given_2          = 1/2
orientation_reverse = u -> 1-u
relational_entropy   = ln2
projective_odds      = 1
kappa                = ln2/(24*pi)
```

## Secret-of-a-Half crosslink

The packet lands on the already reviewed half-side structures:

\[
\frac12
\longleftrightarrow
\operatorname{Fix}(p\mapsto1-p)
\longleftrightarrow
\operatorname{Fix}(q\mapsto1/q)
\longleftrightarrow
H_2^{\max}=\ln2.
\]

Reference repository:

`AdrianLipa90/secret-of-a-half`

Reference head observed for this pass:

`4cf36453ee2b6d33a1f9177ca324b9ef491270be`

The earlier TIR half review remains relevant provenance:

`TIR/docs/cross_reviews/TIR_SECRET_HALF_2026-08-07.md`

## Informational-Dynamics-of-Time crosslink

The sibling temporal spine currently begins

\[
\mathrm{TIR}
\rightarrow
\mathrm{Temporal\ Primitive}
\rightarrow
\mathrm{Temporal\ Wave}
\rightarrow
\mathrm{NOW}.
\]

The new TIR-owned crosslink inserts a typed outgoing packet at the TIR boundary:

\[
\boxed{
\mathrm{TIR}
\xrightarrow{\mathcal S_{13|2}}
(1/2,\ln2,q=1)
\dashrightarrow
\mathrm{Temporal\ Primitive}
\rightarrow
\mathrm{Temporal\ Wave}
\rightarrow
\mathrm{NOW}.
}
\]

The dashed edge means cross-repository consumption. TIR owns the relational
half-seam theorem and its entropy/projective packet. The temporal repository owns
the subsequent temporal primitive, wave, NOW, bifurcation and transport layers.

Reference repository:

`AdrianLipa90/Informational-Dynamics-of-Time`

Reference head observed for this pass:

`7f46792bc1f18904808f6af9813a35ed81f3ac15`

## Typed bridge summary

```text
TIR
  relational opposition 1 <-> 3 across domain 2
      |
      v
  unique equal-share seam u*=1/2
      |
      +--> H_rel=ln2 --> kappa numerator
      |
      +--> q*=1, reciprocal self-duality --> Secret of a Half
      |
      `--> structural seam packet --> Dynamics of Time / NOW chain
```

## Validation

Executable audit:

`TIR/validation/tir_relational_half_seam_v0_1.py`

Expected receipt schema:

`TIR_RELATIONAL_HALF_SEAM_V0_1`

Current local deterministic audit result for the candidate source: `PASS`.
