# TIR × IDT Event-Spatial State Binding Contract v0.1

Status: EXECUTABLE_SOURCE_BINDING_CONTRACT / EVENT_INDEXED_METRIC_STRAIN_TO_EXISTING_RF_E9 / SAME_REALIZATION_AND_CLOCK_FIREWALL / PRODUCTION_INPUT_OPEN

Date: 2026-09-24

## 1. Purpose

The gravity derivation no longer requires an abstract physical identification between a generic IDT state coordinate and a TIR density operator.

Instead, this contract binds independently sourced objects at the event level:

\[
\boxed{
\text{IDT realized event}
\longleftrightarrow
\text{TIR spatial snapshot}
}
\]

under one declared physical realization, one immutable realization receipt and one calibrated clock identity.

The contract outputs a discrete approximation to the temporal metric rate

\[
\boxed{
\frac{\Delta h_{ij}}{\Delta x^0}
}
\]

and hands that quantity to the already-existing RFC RF-E9 extrinsic-curvature operator.

It does not define a second \(K_{ij}\).

## 2. Parent surfaces

IDT GSC-2 provides a realized event complex with:

- unique event identifiers;
- directed elapsed edges;
- positive \(d\Theta\);
- source provenance;
- clock identity;
- exactness/integrity gates.

TIR provides a spatial metric or a source-backed coframe/Gram representation on an admitted spatial patch.

RFC RF-E9 owns the operator

\[
\boxed{
K_{ij}
=
\frac{1}{2N}
\left(
-\partial_0 h_{ij}
+
D_i b_j
+
D_j b_i
\right),
\qquad
x^0=ct.
}
\]

RFC GSC3B and GSC3D own the matching-field/shift crosslink.

Therefore this contract supplies only the missing source term \(\partial_0h_{ij}\).

## 3. Binding envelope

A source packet contains one envelope with:

- non-empty physical_realization_id;
- 64-hex physical_realization_receipt_sha256;
- non-empty clock_id;
- source_class in PRODUCTION_SOURCE, REFERENCE_CONTROL or CANDIDATE_SOURCE;
- positive finite temporal scale
  \[
  \boxed{\alpha=\frac{dx^0}{d\Theta}>0};
  \]
- a non-empty event list;
- a non-empty directed elapsed-edge list.

For a production packet, runtime/synthetic realization identifiers are forbidden.

## 4. Event-spatial snapshots

Every event record contains:

- event_id;
- scalar \(\Theta_v\);
- positive lapse \(N_v\) or a source reference for the admitted lapse;
- patch_id;
- a symmetric positive-definite \(3\times3\) spatial metric \(h_{ij}(v)\);
- immutable spatial_source_ref.

The metric may be emitted directly or generated upstream from a source-backed coframe/Gram object. This contract validates the metric carrier and its lineage; it does not fabricate the spatial state.

All event snapshots belong to the common realization envelope.

## 5. Temporal edges

For each directed IDT edge \(u\to v\),

\[
\boxed{
d\Theta_{uv}
=
\Theta_v-\Theta_u
>0.
}
\]

The calibrated RFC temporal separation is

\[
\boxed{
\Delta x^0_{uv}
=
\alpha\,d\Theta_{uv}.
}
\]

The edge metric-rate estimator is

\[
\boxed{
\mathcal D^{(uv)}_{ij}
:=
\frac{h_{ij}(v)-h_{ij}(u)}
{\Delta x^0_{uv}}.
}
\]

This object has dimension \(L^{-1}\) when \(h_{ij}\) is dimensionless.

## 6. Handoff to RF-E9

The contract exports

\[
\boxed{
\partial_0h_{ij}
\longleftarrow
\mathcal D^{(uv)}_{ij}
}
\]

as a refinement estimator.

RFC RF-E9 remains the unique extrinsic-curvature authority:

\[
\boxed{
K_{ij}^{\rm RF-E9}
=
\frac1{2N}
\left(
-\partial_0h_{ij}
+D_i b_j+D_j b_i
\right).
}
\]

On a zero-shift reference control with constant lapse,

\[
\boxed{
K_{ij}^{(uv,0)}
=
-\frac{1}{2N}
\mathcal D^{(uv)}_{ij}
}
\]

is only an executable consistency control for RF-E9, not a competing definition.

## 7. Refinement theorem

Let a smooth metric family \(h_{ij}(x^0)\) be sampled at source-bound events with maximal temporal mesh

\[
\delta=\max_{uv}|\Delta x^0_{uv}|.
\]

For a regular refining sequence and \(h\in C^1\),

\[
\boxed{
\mathcal D^{(uv)}_{ij}
\to
\partial_0 h_{ij}
}
\]

at the corresponding point in the standard finite-difference sense as \(\delta\to0\).

For \(h\in C^2\), the one-sided edge estimator has first-order truncation error,

\[
\boxed{
\mathcal D_{ij}^{(uv)}
=
\partial_0h_{ij}
+
O(\Delta x^0_{uv}).
}
\]

A central event stencil may provide \(O(\delta^2)\) accuracy when the source event complex supplies the required symmetric neighboring events.

The theorem concerns convergence of a source-backed derivative estimator only.

## 8. Spatial covariance

Under one time-independent spatial basis change

\[
h\mapsto QhQ^T
\]

with constant invertible \(Q\), the metric-rate estimator transforms covariantly:

\[
\boxed{
\mathcal D
\mapsto
Q\mathcal DQ^T.
}
\]

For an orthogonal frame re-expression this preserves the corresponding scalar matrix norms and eigenvalue structure.

For time-dependent spatial relabelings, the metric-rate term alone is not covariant; the shift/Lie-derivative terms in RF-E9 are required. This is precisely why the present contract does not promote \(\Delta h/\Delta x^0\) to a standalone gravitational observable.

## 9. Relation to the earlier abstract state-flow bridge

The conditional theorem

TIR_IDT_EXTRINSIC_CURVATURE_SOURCE_BRIDGE_V0_1

showed that, if one common smooth state family \(x^A\) parameterizes the TIR metric,

\[
\partial_\Theta h_{ij}
=
\frac{dx^A}{d\Theta}\partial_A h_{ij}.
\]

The present event-spatial contract removes the need to promote that abstract same-state identity as a production premise.

Instead, physical lineage is checked directly:

\[
\boxed{
\text{same event ID}
+
\text{same realization}
+
\text{same receipt}
+
\text{same clock}
+
\text{source-backed spatial snapshot}.
}
\]

The abstract chain-rule theorem remains mathematically valid, but this event-indexed route is the preferred production architecture.

## 10. Production firewall

A packet is not a production physical realization merely because the schema and reference controls pass.

Production requires source-owned event and spatial captures with matching:

\[
\boxed{
\text{physical realization ID}
}
\]

and

\[
\boxed{
\text{physical realization receipt}.
}
\]

The following are rejected as production substitutes:

- NOEMA runtime vectors;
- PhaseNav/Terminal36D phase states;
- synthetic event graphs;
- reference fixtures;
- inferred event IDs without source receipts.

## 11. Claim ledger

- event-spatial binding schema: EXACT EXECUTABLE CONTRACT
- same-realization receipt gate: EXACT FAIL-CLOSED CONTRACT
- same-clock gate: EXACT FAIL-CLOSED CONTRACT
- positive elapsed-edge gate: EXACT
- SPD spatial metric gate: EXACT NUMERICAL/ALGEBRAIC
- \(dx^0=\alpha d\Theta\): EXACT CONDITIONAL CLOCK-SCALE BINDING
- edge metric-rate estimator: EXACT DEFINITION
- first-order refinement convergence: STANDARD CONDITIONAL NUMERICAL THEOREM
- spatial constant-basis covariance: EXACT
- zero-shift RF-E9 control: EXACT CONDITIONAL CONTROL
- RF-E9 operator ownership: REUSED EXISTING RFC GATE
- production event-spatial realization: OPEN INPUT
- global production refinement/coverage: OPEN INPUT
- physical late-time acceleration source: OPEN DOWNSTREAM

## 12. Smallest remaining source gate

After this contract, the missing physical evidence is no longer an abstract equality between IDT and TIR state variables.

It is the concrete source packet

\[
\boxed{
\{
v,\Theta_v,h_{ij}(v),N_v
\}_{v\in\mathcal E}
}
\]

with one admitted physical-realization lineage and enough event density/coverage for the intended continuum claim.

Reference validator:

TIR/validation/tir_idt_event_spatial_state_binding_v0_1.py
