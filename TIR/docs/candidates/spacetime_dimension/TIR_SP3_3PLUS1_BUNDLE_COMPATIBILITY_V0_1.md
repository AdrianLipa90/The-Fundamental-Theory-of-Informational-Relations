# TIR SP3 3+1 Bundle Compatibility v0.1

Status: `CANDIDATE_ONLY / EXACT_SAME_PARENT_BUNDLE_COMPATIBILITY / STRUCTURAL_GATES_PASS / PRODUCTION_EVIDENCE_BLOCKED / CANON_ALLOWED_FALSE`

Date: 2026-09-19

## 1. Purpose

This candidate tests whether one external two-epoch SP3 parent source can generate both sides of the already-canonical

`TIR_PHYSICAL_REALIZATION_SOURCE_BUNDLE_V0_2`

without fabricating production evidence.

The parent source is the archived record set `RT218283.SP3@8013` used by the RFC ToE candidate.

Each source record is a literal (3+1) tuple

[
y_s^{(a)}=(x_s^{(a)},y_s^{(a)},z_s^{(a)},c_s^{(a)}).
]

For two epochs, define

[
ar y_s=rac{y_s^{(1)}+y_s^{(2)}}{2},
qquad
dot y_s=rac{y_s^{(2)}-y_s^{(1)}}{Delta t}.
]

The transform is exactly invertible for (\Delta t\neq0).

## 2. Candidate source typing

The source is deliberately admitted as

`source_class = CANDIDATE_SOURCE`

and the matching packet as

`production = false`.

This is mandatory for the present audit. The external archive is real observational data, but the tetrahedral spatial complex and inter-leaf matching field are derived model surfaces rather than independent full physical (3+1) production measurements.

No field in this candidate may relabel the archive-derived geometry as a production capture.

## 3. Common realization identity

Let

[
H_S=operatorname{SHA256}(	ext{canonical frozen SP3 source records}).
]

The candidate uses

[
R_S=	exttt{physical:igs-sp3:sha256:}H_S
]

as the shared source-derived realization identifier and

[
H_S
]

as the common realization receipt.

Both the spatial v0.2 capture and the matching v0.2 input therefore carry exactly the same

```text
physical_realization_id
physical_realization_receipt_sha256
```

derived from one source parent.

## 4. Spatial projection

The five observed nodes `G01..G05` generate the deterministic boundary-of-a-4-simplex tetrahedral complex already used by the RFC observational candidate.

The TIR v0.2 spatial capture is submitted as `CANDIDATE_SOURCE`.

Expected result:

```text
input integrity       PASS
A5 manifold           PASS
same source receipt   PASS
production admitted   FALSE
promotion eligible    FALSE
```

## 5. Matching projection

For each node,

[
eta_s=
rac{mathbf x_s^{(2)}-mathbf x_s^{(1)}}{Delta t}.
]

For directed overlaps from the reference node (r=mathrm{G01}),

[
A_{rs}=I_3,
qquad
v_{rs}=eta_r-eta_s,
]

so

[
eta_s=A_{rs}eta_r-v_{rs}
]

holds up to ordinary float conversion residual.

The TIR matching input is submitted with `production=false`.

Expected result:

```text
payload integrity     PASS
GSC3A handoff         PASS
same source receipt   PASS
production input      FALSE
promotion eligible    FALSE
```

## 6. Bundle expectation

The exact expected bundle certificate is

```text
same_physical_realization = true
same_realization_receipt  = true
spatial_ready             = false
matching_ready            = false
promotion_review_eligible = false

blockers =
  TIR_GSC1_PRODUCTION_SPATIAL_CAPTURE
  TIR_INTERLEAF_PRODUCTION_MATCHING_CAPTURE
```

No `SAME_PHYSICAL_REALIZATION_ID` or `SAME_PHYSICAL_REALIZATION_RECEIPT` blocker is expected.

Therefore a PASS means:

[
oxed{
	ext{constructor solved}
;land;
	ext{same-parent association solved}
;land;
	ext{production evidence still open}.
}
]

## 7. Relation to 3+1 and half normalization

This candidate is compatible with the independently exact TIR local carrier

[
operatorname{Herm}(2)
=
mathbb RIoplusoperatorname{Herm}_0(2),
qquad
1+3=4,
]

and

[
ho=rac12(I+mathbf rcdotoldsymbolsigma).
]

It does not identify the SP3 coordinate tuple with that Hermitian carrier. The common (3+1) and (1/2) pattern remains a cross-repository structural correspondence until an explicit physical intertwiner is proved.

## 8. Collatz firewall

TIR Stage 48 separately has

[
O:nmapsto3n+1,
qquad
E:nmapsto n/2.
]

No equality between the two-epoch midpoint/tangent transform and Collatz dynamics is asserted here.

## 9. Falsification

This candidate FAILS if any of the following occurs:

- the two packet surfaces do not share the exact source-derived realization ID;
- the realization receipts differ;
- the spatial A5 manifold certificate fails;
- the matching handoff law fails;
- the candidate is accidentally admitted as production;
- either candidate surface becomes promotion eligible;
- the bundle reports any blocker other than the two production-evidence blockers.

A PASS cannot promote a physical-production claim.
