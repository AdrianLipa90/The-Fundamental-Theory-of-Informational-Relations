# TIR Coefficient Transition-Selector Precedence Falsification v0.2

Status: `EXACT_ACTIVE_PRECEDENCE_FALSIFICATION / TRANSITION_SELECTOR_REMAINS_OPEN`

Date: 2026-09-14

Scope: test the retrospective Collatz stopping-length selector candidate against the repository's later active seed-precedence rule. Physical claim: none.

## 1. Active seed precedence

The later Stage-22 precedence gate explicitly supersedes the early v0.5 generation ordering for the present validation line and fixes

\[
\boxed{s_1=(3,5),\qquad s_2=(5,7),\qquad s_3=(11,13).}
\]

The corresponding integer seed centers are

\[
\boxed{m_1=4,\qquad m_2=6,\qquad m_3=12.}
\]

Using the ordinary Collatz stopping length to 1,

\[
4\to2\to1,
\]

\[
6\to3\to10\to5\to16\to8\to4\to2\to1,
\]

\[
12\to6\to3\to10\to5\to16\to8\to4\to2\to1,
\]

so

\[
\boxed{\ell_1=2,\qquad \ell_2=8,\qquad \ell_3=9.}
\]

No particle mass, Yukawa coupling, recovered coefficient tuple, or residual-to-target quantity enters this computation.

## 2. Retrospective candidate under test

The older atomic canonization note recorded, under the earlier seed ordering, the retrospective candidate

\[
\operatorname{sgn}(b,c)=\operatorname{sgn}(\ell_{\rm dst}-\ell_{\rm src}),
\]

and

\[
|c|=\ell_{\rm dst}-1.
\]

The same note explicitly marked the pattern non-canonical and prospective-test-only.

The independently recorded historical release packets are

\[
P_{e\mu}=(0,X_5,X_4,X_3+I),
\qquad
P_{\mu\tau}=(0,F,I,X_3),
\]

with curvature-slot magnitudes

\[
\boxed{|c|_{e\mu}=8,\qquad |c|_{\mu\tau}=7}
\]

and historical curvature signs

\[
\boxed{\operatorname{sgn}(c_{e\mu})=+1,\qquad
\operatorname{sgn}(c_{\mu\tau})=-1.}
\]

## 3. Exact falsification under active precedence

For the active generation ordering, the two successive release transitions are

\[
1\to2:\quad \ell_1=2\to\ell_2=8,
\]

\[
2\to3:\quad \ell_2=8\to\ell_3=9.
\]

Therefore the retrospective magnitude rule predicts

\[
|c|_{1\to2}^{\rm stop}=8-1=7,
\]

\[
|c|_{2\to3}^{\rm stop}=9-1=8.
\]

But the independently recorded historical packet magnitudes are respectively 8 and 7. Hence

\[
\boxed{|c|=\ell_{\rm dst}-1\quad\text{fails on both successive transitions under active precedence}.}
\]

Likewise,

\[
\ell_2-\ell_1=+6,
\qquad
\ell_3-\ell_2=+1,
\]

so the retrospective sign rule predicts positive orientation for both transitions. The historical second release has negative curvature sign. Hence

\[
\boxed{\operatorname{sgn}(c)=\operatorname{sgn}(\ell_{\rm dst}-\ell_{\rm src})
\quad\text{fails for }2\to3.}
\]

This is a source-precedence falsification, not a fit to measured observables.

## 4. DII holonomy does not repair identifiability by itself

The periodic regular-simplex DII theorem establishes, for the tetrahedral carrier,

\[
q_3=\frac12.
\]

That value is a carrier-level triangular-holonomy invariant. If two transition states use the same canonical tetrahedral carrier, the scalar value `q_3` is the same for both and therefore cannot by itself distinguish `e->mu` from `mu->tau`.

Thus neither the active stopping-length scalar alone nor the carrier-level tetrahedral face-turn scalar alone supplies the missing injective transition selector.

## 5. Minimal surviving selector requirement

A future source-derived selector

\[
\Sigma:\mathcal S_{\rm precoef}\to
\mathcal P_h\times\mathcal P_a\times\mathcal P_b\times\mathcal P_c
\]

must contain a transition-sensitive invariant that survives current source precedence and is not reducible to either

\[
\ell_{\rm dst}-1,
\qquad
\operatorname{sgn}(\ell_{\rm dst}-\ell_{\rm src}),
\qquad
q_3
\]

alone.

The candidate may still use richer seed-path, directed-orbit, projective, Wilson-loop, or holonomy data, but such a map must be specified before reading recovered coefficient packets and must fail closed when non-unique.

## 6. Theorem

### Theorem — active-precedence stopping-length selector is incompatible with the recorded release packets

Assume the active Stage-22 seed ordering `(3,5)->1`, `(5,7)->2`, `(11,13)->3`, ordinary Collatz stopping length to 1 on the corresponding centers, and the independently recorded historical release packets. Then the rule `|c|=ell_destination-1` disagrees with both successive release packets, and the rule `sign(c)=sign(ell_destination-ell_source)` disagrees with the second release packet.

### Proof

The active centers are `(4,6,12)` with stopping lengths `(2,8,9)`. Direct substitution gives predicted curvature magnitudes `(7,8)` for the two successive transitions, while the recorded packet magnitudes are `(8,7)`. The active stopping-length differences are both positive, while the second recorded curvature sign is negative. Therefore both candidate rules fail as stated.

## 7. Claim ledger

```text
active_seed_precedence = EXACT_REPOSITORY_PRECEDENCE
active_center_stopping_lengths = EXACT_INTEGER_COMPUTATION
legacy_abs_c_equals_destination_ell_minus_1 = FALSIFIED_UNDER_ACTIVE_PRECEDENCE
legacy_sign_equals_stopping_length_difference_sign = FALSIFIED_FOR_SECOND_ACTIVE_TRANSITION
tetrahedral_q3_alone_transition_injective = FALSE
COEFFICIENT_TRANSITION_PARENT_SELECTOR = OPEN
physical_mass_or_yukawa_binding = OPEN_DOWNSTREAM
```

## 8. Validator

Deterministic validator:

`TIR/validation/tir_coefficient_transition_selector_precedence_falsification_v0_2.py`

The validator independently computes the Collatz stopping lengths, checks the active precedence and historical packet source tokens, verifies the two magnitude mismatches and the sign mismatch, and fails if the falsified retrospective rule becomes accidentally re-promoted.