# TIR Coefficient-Magnitude Identifiability Audit v0.1

Status: `PARTIAL_EXACT_PARENT_ARITHMETIC / SOURCE_SELECTION_OPEN / NO_FALSE_CLOSURE`

Date: 2026-09-10

## Scope

For the TIR generator

\[
G(h,a,b,c)=\frac h2+a\kappa+b\frac{\kappa}{L_3}+c\frac{\kappa^2}{2},
\]

the role router and orientation theorem already determine slot identity and, when the active signs agree, coefficient sign. This audit asks the strictly narrower question: are the integer magnitudes forced by coefficient-free parents?

Observed masses, Yukawa values, target actions/releases, recovered coefficient tuples, coefficient-enriched PhaseNav envelopes and residual-to-target information are excluded.

## Theorem 1 — role/sign data do not identify magnitude

Let a slot role and a nonzero orientation sign be fixed. If the framework supplies no integer-valued extraction map from the admitted source invariant to the slot magnitude, then the coefficient is not identifiable: for any distinct positive integers m and n, the two coefficients chi*m and chi*n preserve the same role and sign data.

Therefore typed role routing plus sign forcing cannot by itself close `|h|,|a|,|b|,|c|`.

## Theorem 2 — parent arithmetic is exact after parent selection

The current Platonic closure supplies exactly

\[
(L_3,L_4,L_5)=(7,2,5).
\]

Consequently, after a parent expression has independently been selected, the following magnitudes are exact arithmetic consequences:

\[
L_5=5,\qquad L_4=2,\qquad L_3+1=8,\qquad L_3=7.
\]

This closes arithmetic evaluation, not the semantic rule selecting one of those expressions for a particular transition/slot.

## Current row classification

| state | slot | current magnitude expression | arithmetic status | source-selection status |
|---|---|---:|---|---|
| ELECTRON_ACTION | h | 1 | exact identity | projective/spin role admitted |
| ELECTRON_ACTION | a | 3 | exact if generation-count-3 admitted | generation count is observation/project primitive |
| ELECTRON_ACTION | b | 1 | exact identity integer | transition binding remains project assignment |
| ELECTRON_ACTION | c | 1 | exact identity integer | leading-curvature binding remains project assignment |
| E_TO_MU_RELEASE | a | L5=5 | exact from Platonic L closure | selection of L5 for this transition remains project assignment |
| E_TO_MU_RELEASE | b | L4=2 | exact from Platonic L closure | selection of L4 for this transition remains project assignment |
| E_TO_MU_RELEASE | c | L3+1=8 | exact arithmetic from Platonic L closure | selection of L3+1 remains underdetermined/retrospective |
| MU_TO_TAU_RELEASE | a | 3 | exact if generation-count-3 admitted | generation count is observation/project primitive |
| MU_TO_TAU_RELEASE | b | 1 | exact identity integer | transition binding remains project assignment |
| MU_TO_TAU_RELEASE | c | L3=7 | exact from Platonic L closure | selection of L3 remains project assignment |

## Legacy arithmetic defect

The historical generation-release source contains the statement `5 = L4 + L3`. With the current and historical values `L4=2` and `L3=7`, the right-hand side is 9. The same paragraph subsequently switches to `L5=5`. The equality is therefore a legacy arithmetic defect and MUST NOT be used as provenance for the coefficient 5. The admissible arithmetic parent, if the transition assignment is separately justified, is `L5=5`.

## Retrospective curvature pattern firewall

The current atomic canonization layer records `abs(c)=ell_destination-1`, giving 8 and 7 for the two known charged-lepton transitions, but explicitly marks that relation retrospective and underdetermined. It is not a prospective theorem and cannot be promoted as the missing extraction map.

## Exact conclusion

The previous gate name `TYPED_INTEGER_MAGNITUDE_EXTRACTION` is too broad. Current status is:

```text
ROLE_ROUTING = CLOSED
SIGN_ORIENTATION = CLOSED_WHEN_SOURCES_AGREE
MAGNITUDE_PARENT_ARITHMETIC = PARTIALLY_CLOSED
PLATONIC_L_EVALUATION = CLOSED_INTERNAL
GENERATION_COUNT_3 = EXTERNAL_OR_PROJECT_PRIMITIVE
TRANSITION_TO_PARENT_SELECTION = OPEN
RETROSPECTIVE_COLLATZ_CURVATURE_RULE = NOT_CANON
FULL_COEFFICIENT_MAGNITUDE_FORCING = OPEN
```

The next theorem must be a coefficient-free transition-to-parent selection map. It must be frozen before reading target masses, target actions or recovered coefficient tuples.
