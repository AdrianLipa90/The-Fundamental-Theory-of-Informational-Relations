# TIR Neutrino Absolute-Action Source Repair v0.1

Status: `SOURCE_CONFLICT_RESOLVED / SINGLE_OFFSET_RULE_RESTORED / PHYSICAL_ABSOLUTE_MASS_VALIDATION_SEPARATE`

Date: 2026-09-10

## Scope

This repair addresses an internal formula-definition conflict in the neutrino action surface. It does not use observed neutrino masses to select a new model and does not promote the absolute neutrino spectrum to an empirical PASS.

The shared definitions are

\[
S_{\rm bare}=\frac{1+L_4/L_3}{2}=\frac9{14},
\qquad
A_{\rm face}=\frac{(L_4/L_3)^2}{2}=\frac2{49},
\]

and

\[
dS:=\kappa A_{\rm face}(1-\kappa).
\]

## 1. Conflicting source surfaces

The repository systematization surface states directly

\[
S_1=\frac9{14}+\kappa\frac{(L_4/L_3)^2}{2}(1-\kappa)
=S_{\rm bare}+dS.
\]

The legacy neutrino chapter separately defines exactly the same `dS`, but then prints

\[
S_1=S_{\rm bare}+\kappa dS.
\]

Substituting the chapter's own definition of `dS` into that line gives

\[
S_1=S_{\rm bare}+\kappa^2 A_{\rm face}(1-\kappa),
\]

which is not the direct systematization equation. The extra factor is therefore an internal transcription/composition inconsistency.

Both source files entered the repository in commit `015fd9f37472f6ee2bb7d0a357e375ab15e10e77`; chronology is not used to choose between them.

## 2. Canonical repair rule

The source-consistent rule is

\[
\boxed{S_1=S_{\rm bare}+dS}
\]

with

\[
\boxed{dS=\kappa A_{\rm face}(1-\kappa)}.
\]

This is not a new coefficient. It is the direct substitution of the already declared action-offset definition into the direct systematization equation.

The legacy line

\[
S_1=S_{\rm bare}+\kappa dS
\]

is retained only as a quarantined transcription defect and must not be used as the canonical action equation.

## 3. Ratio layer remains separate

For the declared structural ratios

\[
r_i\in(1,L_4,L_3+L_4+1)=(1,2,10),
\]

and

\[
S_i=S_1-\kappa\ln r_i,
\]

the exponential action map implies exactly

\[
\frac{m_i}{m_1}=r_i.
\]

This ratio identity is independent of the repaired absolute offset. It does not by itself validate the physical absolute mass scale.

## 4. Epistemic boundary

The repair closes the repository-internal formula inconsistency. It does **not** establish that the underlying neutrino action ansatz is uniquely forced by established physics, nor that the absolute masses are experimentally measured at the displayed values.

```text
NEUTRINO_ACTION_SOURCE_CONFLICT = CLOSED
CANONICAL_S1_RULE = S_bare + dS
EXTRA_KAPPA_AFTER_dS = QUARANTINED_TRANSCRIPTION_DEFECT
STRUCTURAL_RATIO_IDENTITY = CLOSED_INTERNAL
ABSOLUTE_NEUTRINO_MASS_EMPIRICAL_STATUS = OPEN
```
