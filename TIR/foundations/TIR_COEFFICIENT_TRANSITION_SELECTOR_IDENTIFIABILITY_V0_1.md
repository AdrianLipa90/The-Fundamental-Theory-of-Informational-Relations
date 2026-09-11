# TIR Coefficient Transition-Selector Identifiability v0.1

Status: `EXACT_CURRENT_INPUT_NONIDENTIFIABILITY / TRANSITION_SELECTOR_CONSTRUCTION_OPEN`

Date: 2026-09-10

Scope: exact statement about what the current TIR coefficient-free routing inputs do and do not determine. Physical claim: none.

## 1. Question

After exact evaluation of the already-declared magnitude-parent packets, the remaining coefficient gate is

\[
\text{coefficient-free transition state}
\longrightarrow
(P_h,P_a,P_b,P_c).
\]

The issue is no longer how to evaluate `L_3`, `L_4`, `L_5`, the flavour count, or the unit parent. It is whether the current source operators uniquely select the transition-specific parent expressions.

## 2. Current implemented transition state

The existing `AtomicGeometryState` contains

```text
state_id
source_role
dV_dphi
orbital_direction
chiral_path
seed_from
seed_to
collatz_stop_from
collatz_stop_to
```

with a fail-closed ban on mass/Yukawa/known-coefficient target inputs.

The implemented `evaluate_orientation` path computes only

\[
\chi_\nabla,
\qquad
\chi_O,
\qquad
\chi_H,
\]

and their agreement class. It does not return a magnitude-parent packet.

In particular, the transition-sensitive seed and stopping-length fields are present in the state schema but are not consumed by the current orientation evaluator to choose the coefficient magnitude parents.

## 3. Exact non-identifiability witness

The two charged-lepton release gates are both release states and therefore have the same four slot roles

\[
(R_h,R_a,R_b,R_c).
\]

Nevertheless, the historical lineage declares different parent packets:

\[
P_{e\mu}=(0,X_5,X_4,X_3+I),
\]

\[
P_{\mu\tau}=(0,F,I,X_3).
\]

Both packets respect the same role ordering:

```text
h = half/base-incidence slot
a = generation/release slot
b = return-axis slot
c = curvature/holonomy slot
```

Therefore role identity alone cannot distinguish the two packets.

Likewise, a common orientation sign cannot determine the magnitudes because the magnitude valuation forgets sign by construction.

Thus

\[
\boxed{
\text{role routing + orientation class}
\not\Rightarrow
\text{unique transition parent packet}.
}
\]

This is a strict identifiability statement: two distinct parent packets are compatible with the same coarse slot-role architecture.

## 4. Existing candidate information is insufficient for promotion

`ATOMIC_ASSIGNMENT_CANONIZATION.md` records the no-mass-input generation seed/stopping data

```text
generation 1: seed (3,5), center 4, ell=2
generation 2: seed (11,13), center 12, ell=9
generation 3: seed (5,7), center 6, ell=8
```

and the retrospective observations

```text
sign_transition = sign(ell_destination - ell_source)
abs(c) = ell_destination - 1
```

for the two known charged-lepton transitions.

That source explicitly labels the pattern retrospective and non-canonical. The repository receipt likewise records `collatz_destination_curvature_magnitude` as `RETROSPECTIVE_CANDIDATE_UNDERDETERMINED`.

Therefore these two examples cannot be converted into a selector theorem merely because they reproduce two already-known values.

## 5. Legacy explanatory inconsistency

The historical generation-release chapter contains the intermediate sentence

```text
5 = L4 + L3
```

although the canonical values are `L4=2`, `L3=7`, so the right-hand side is `9`. The same passage then abandons that line and identifies the coefficient with `L5=5`.

The current v12 monograph does not rely on the false equality. This inconsistency is retained only as source-history evidence that the transition selector requires a fresh typed derivation rather than a reconstruction from legacy prose.

## 6. Minimal missing object

A valid selector requires a transition-sensitive invariant map

\[
\boxed{
\Sigma:
\mathcal S_{\rm precoef}
\to
\mathcal P_h\times\mathcal P_a\times\mathcal P_b\times\mathcal P_c
}
\]

where `S_precoef` contains only coefficient-free structural data and the codomain contains typed parent expressions.

At minimum, `Sigma` must distinguish the two release states before observing their recovered coefficient tuples. Candidate source coordinates already available in the schema include seed-pair data, Collatz stopping data, gradient/orbit/chiral orientation and eventually an independently computed holonomy/curvature class.

No particular formula for `Sigma` is promoted here.

## 7. Exact theorem

### Theorem — current coarse inputs are not injective with respect to parent packets

Let the coarse transition descriptor consist only of

\[
D_{\rm coarse}=(\text{release-state flag},R_h,R_a,R_b,R_c,\chi),
\]

where `chi` is any common orientation label independent of the magnitude valuation.

The historical release states `e->mu` and `mu->tau` share the release flag and slot-role ordering, while their declared parent packets are distinct. Hence there is no function of `D_coarse` alone that reproduces both declared packets.

### Proof

If such a function existed, equal coarse descriptors would have equal outputs. The two release states have the same coarse role descriptor but require different declared packets. This contradicts single-valuedness. Therefore an additional transition-sensitive invariant is necessary.

## 8. What this closes

```text
role_only_selector_is_sufficient = FALSE
orientation_only_selector_is_sufficient = FALSE
current_evaluate_orientation_returns_parent_packet = FALSE
additional_transition_sensitive_invariant_required = TRUE
legacy_L4_plus_L3_equals_5_explanation = FALSE
```

This is a closed non-identifiability result, not a physical coefficient derivation.

## 9. What remains open

`COEFFICIENT_TRANSITION_PARENT_SELECTOR` remains open until a source-derived `Sigma` is specified and validated without target leakage.

The selector must fail closed if its required transition-sensitive inputs are missing or if multiple parent packets remain admissible.

## 10. Validator

Deterministic validator:

`TIR/validation/tir_coefficient_transition_selector_identifiability_v0_1.py`

The validator checks the current atomic operator AST, confirms that magnitude-parent selection is absent from `evaluate_orientation`, verifies the two distinct release parent packets and the legacy arithmetic inconsistency, and keeps the selector status open.
