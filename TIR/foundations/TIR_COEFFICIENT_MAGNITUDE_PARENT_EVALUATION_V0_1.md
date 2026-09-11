# TIR Coefficient Magnitude Parent Evaluation v0.1

Status: `EXACT_PARENT_PACKET_EVALUATION / TRANSITION_PARENT_SELECTOR_OPEN`

Date: 2026-09-10

Scope: exact TIR-internal evaluation of already-declared coefficient-magnitude parent expressions. Physical claim: none.

## 1. Problem split

The TIR action/release generator is

\[
G(h,a,b,c)
=\frac h2+a\kappa+b\frac{\kappa}{L_3}+c\frac{\kappa^2}{2},
\qquad
(h,a,b,c)\in\mathbb Z^4.
\]

The role/orientation theorem already types the four slots as

\[
h\leftrightarrow\text{projective-half-spin},\quad
a\leftrightarrow\text{generation-release},\quad
b\leftrightarrow\text{return-axis},\quad
c\leftrightarrow\text{curvature-holonomy}.
\]

Historically, the integration lineage also records explicit magnitude-parent expressions for the three charged-lepton action/release gates. The remaining question was previously tracked as one coarse gate, `COEFFICIENT_MAGNITUDE_EXTRACTION`.

That coarse gate contains two logically distinct tasks:

1. evaluate a declared parent expression once the parent packet is supplied;
2. prove which parent packet is selected by a coefficient-free physical transition.

This surface closes (1). It does not claim to close (2).

## 2. Upstream certified integers

The three-flavour carrier gives

\[
\boxed{N_F=3}.
\]

The independent Platonic/group closure gives

\[
\boxed{L_3=7,\qquad L_4=2,\qquad L_5=5}.
\]

The unit-count parent is

\[
\boxed{I=1}.
\]

For the half-base slot, `I=1` means one insertion of the generator basis element `1/2`; it does not replace the basis element by the number one.

## 3. Typed parent-count valuation

Define the finite source-count valuation `nu` on the parent expressions used by the historical lineage:

\[
\nu(0)=0,
\qquad
\nu(I)=1,
\qquad
\nu(F)=N_F=3,
\]

\[
\nu(X_4)=L_4=2,
\qquad
\nu(X_5)=L_5=5,
\qquad
\nu(X_3)=L_3=7,
\]

and on the declared additive parent expression

\[
\nu(X_3+I)=\nu(X_3)+\nu(I)=L_3+1=8.
\]

Here `F`, `X_3`, `X_4`, `X_5`, `I`, and `X_3+I` are typed count labels. This theorem does not assert that an arbitrary physical transition must choose any particular one of them.

## 4. Historical parent packets, evaluated without mass targets

The parent lineage already declares the following magnitude packets.

### 4.1 Electron action packet

\[
P_e=(I,F,I,I).
\]

Therefore

\[
\boxed{
(|h|,|a|,|b|,|c|)_e
=(1,3,1,1).
}
\]

### 4.2 Electron-to-muon release packet

The release operator has no independent half-base insertion and its declared magnitude packet is

\[
P_{e\mu}=(0,X_5,X_4,X_3+I).
\]

Therefore

\[
\boxed{
(|h|,|a|,|b|,|c|)_{e\mu}
=(0,5,2,8).
}
\]

### 4.3 Muon-to-tau release packet

The declared magnitude packet is

\[
P_{\mu\tau}=(0,F,I,X_3).
\]

Therefore

\[
\boxed{
(|h|,|a|,|b|,|c|)_{\mu\tau}
=(0,3,1,7).
}
\]

These evaluations use only the declared parent expressions and the upstream integers `N_F`, `L_3`, `L_4`, `L_5`, and `I`. No observed lepton mass, Yukawa coupling, fitted action, residual-to-target value, or recovered coefficient tuple is used as an input to the evaluation.

## 5. Downstream historical reconstruction check

The legacy signed coefficient states are

\[
(1,-3,+1,-1),
\qquad
(0,+5,+2,+8),
\qquad
(0,+3,-1,-7).
\]

Taking absolute values gives exactly the three independently evaluated parent-count vectors above.

This equality is a downstream reproduction check. The signed tuples are not used to generate the parent-count vectors.

## 6. Exact theorem

### Theorem — uniqueness conditional on a declared parent packet

Let `P=(P_h,P_a,P_b,P_c)` be any packet whose entries belong to the finite parent-expression set

\[
\mathcal P=\{0,I,F,X_3,X_4,X_5,X_3+I\}.
\]

Once the upstream values

\[
N_F=3,
\qquad
(L_3,L_4,L_5)=(7,2,5),
\qquad
I=1
\]

are fixed, the componentwise valuation

\[
M(P)=\bigl(\nu(P_h),\nu(P_a),\nu(P_b),\nu(P_c)\bigr)
\]

is single-valued. Hence every declared parent packet has one and only one coefficient-magnitude vector.

For the three packets already recorded in the TIR integration lineage,

\[
\boxed{
M(P_e)=(1,3,1,1),
}
\]

\[
\boxed{
M(P_{e\mu})=(0,5,2,8),
}
\]

\[
\boxed{
M(P_{\mu\tau})=(0,3,1,7).
}
\]

### Proof

Each primitive parent label has one fixed integer valuation from the upstream certified TIR state. The only composite parent used here, `X_3+I`, is evaluated by ordinary integer addition. Componentwise application of a single-valued valuation is therefore single-valued. Substitution of the certified integers yields the three displayed vectors directly.

## 7. What is now closed

The following statements are closed internally:

```text
coefficient_parent_expression_evaluation = EXACT
historical_parent_packets_have_unique_magnitudes = TRUE
ELECTRON_ACTION magnitude vector = (1,3,1,1)
E_TO_MU_RELEASE magnitude vector = (0,5,2,8)
MU_TO_TAU_RELEASE magnitude vector = (0,3,1,7)
target_mass_or_yukawa_input_required = FALSE
```

This removes numerical evaluation of the already-declared magnitude parents from the active frontier.

## 8. What remains open

The remaining non-circular coefficient theorem is narrower:

`COEFFICIENT_TRANSITION_PARENT_SELECTOR`.

Required statement:

\[
\boxed{
\text{coefficient-free transition state}
\longrightarrow
(P_h,P_a,P_b,P_c)
}
\]

with no access to measured masses, Yukawa couplings, the recovered coefficient tuple, a tuple-generated PhaseNav envelope, or residual-to-target information.

The current lineage labels the transition-level semantic assignments as `PROJECT_MODEL_ASSIGNMENT`. Therefore this surface does **not** claim that the three historical parent packets are uniquely forced by projective/Collatz/holonomy geometry.

In particular, the retrospective stopping-length observation in `ATOMIC_ASSIGNMENT_CANONIZATION.md` is not promoted by this theorem.

## 9. Dependency boundary

```text
THREE_FLAVOUR_CARRIER                 CLOSED -> N_F=3
PLATONIC_L_CONSTANT_CLOSURE           CLOSED -> L3=7,L4=2,L5=5
COEFFICIENT_ROLE_SIGN_FORCING         CLOSED on its declared assumptions
HISTORICAL_MAGNITUDE_PARENT_PACKETS   PRESENT
COEFFICIENT_MAGNITUDE_PARENT_EVAL     CLOSED_EXACT
COEFFICIENT_TRANSITION_PARENT_SELECTOR OPEN
PHYSICAL_MASS/YUKAWA_BINDING          OPEN downstream
```

## 10. Validator

Deterministic validator:

`TIR/validation/tir_coefficient_magnitude_parent_evaluation_v0_1.py`

It reconstructs `N_F`, `L_3`, `L_4`, and `L_5` from upstream integer relations, evaluates the three parent packets without using the historical coefficient tuples as inputs, and only then compares the resulting magnitudes against the legacy generator source as a downstream consistency check.
