# TIR Collatz–Poincare Branch Rhythm Candidate Freeze v0.1

Status: `COLLATZ_POINCARE_BRANCH_RHYTHM_CANDIDATE_FROZEN_PREVALIDATION`

Freeze date: `2026-09-19`

## Purpose

Stage 43 establishes an ordered Collatz-step Hamiltonian scaffold but retains the exact rhythm \(\rho_s(k)\) as an open derivation debt.

Stage 49 and the current crosswalk independently establish the exact hyperbolic translation lengths of the two normalized Collatz branch generators in the standard curvature-\(-1\) Poincare normalization:

\[
\ell_E=\ln 2,
\qquad
\ell_O=\ln 3.
\]

The archival reference Hamiltonian states only the formal type requirement

\[
\rho_s(k)>0
\]

and explicitly classifies its historical bounded rhythm as a model choice.

This file freezes the minimal parameter-free branch-local candidate before any CKM, PMNS, mass, or other physical-target comparison.

## Frozen candidate

For a Collatz step with branch symbol \(b_k\in\{E,O\}\), define

\[
\boxed{
\rho_{\rm geo}(k)
=
\begin{cases}
\ln 2,& b_k=E,\\
\ln 3,& b_k=O.
\end{cases}
}
\]

Equivalently,

\[
\boxed{\rho_{\rm geo}(k)=\ell_{b_k}.}
\]

Both values are strictly positive and dimensionless.

No continuous coefficient is introduced.

## Exact orientation companion

The branch signed log-Jacobian cocycle is

\[
\sigma_E=-\ln2,
\qquad
\sigma_O=+\ln3.
\]

Hence the exact factorization is

\[
\boxed{
\sigma_b=\chi_b\,\rho_{\rm geo}(b),
\qquad
\chi_E=-1,\quad
\chi_O=+1.
}
\]

The candidate therefore keeps positive Hamiltonian rhythm magnitude and branch orientation as separate typed objects.

## Word accumulation

For a branch word

\[
w=b_0b_1\cdots b_{K-1},
\]

define the accumulated geometric rhythm

\[
R_{\rm geo}(w)
=
\sum_{k=0}^{K-1}\rho_{\rm geo}(b_k).
\]

If the word contains \(N_E\) even branches and \(N_O\) odd branches,

\[
\boxed{
R_{\rm geo}(w)
=
N_E\ln2+N_O\ln3
=
\ln(2^{N_E}3^{N_O}).
}
\]

Therefore the candidate is additive under word concatenation.

For the Stage-48 words,

\[
w_1=\texttt{OEOE},
\]

so

\[
R_{\rm geo}(w_1)=2\ln2+2\ln3=\ln36.
\]

For the 90-step third-family word with \(N_O=34\), \(N_E=56\),

\[
R_{\rm geo}(w_3)
=
56\ln2+34\ln3
=
\ln(2^{56}3^{34}).
\]

## Pre-validation firewall

The following are excluded from defining or selecting this candidate:

```text
CKM entries or phase
PMNS entries
fermion masses
PDG comparison values
Stage39 A/B target selection
reference eta=0.35
fitted White-Thread values
retrospective observable tuning
```

The candidate uses only:

```text
exact Collatz branch identity
exact PSL(2,R) branch lift
exact Poincare translation length
formal Hamiltonian positivity type rho_s(k) > 0
```

## Scope boundary

This freeze does **not** prove

\[
\rho_s(k)=\rho_{\rm geo}(k)
\]

as the unique physical rhythm.

It freezes \(\rho_{\rm geo}\) as the minimal source-derived, positive, parameter-free candidate admissible under the current Hamiltonian typing.

It also does not assign \(E\) or \(O\) to a physical family generator. The branch-symbol-to-family-operator map remains open.

## Validation gates

1. Recompute \(\ell_E=\ln2\) and \(\ell_O=\ln3\) from the normalized Stage-49 branch matrices.
2. Verify \(\rho_E,\rho_O>0\).
3. Verify the exact signed factorization \(\sigma_b=\chi_b\rho_b\).
4. Verify word additivity for the frozen Stage-48 words.
5. Verify the historical reference rhythm remains explicitly a model choice.
6. Verify no CKM, PMNS, mass, or fitted coefficient enters the candidate.
7. Preserve candidate status; do not promote to physical rhythm merely because the mathematical validation passes.

## Evidential status

```text
candidate freeze: PREVALIDATION
source geometry: EXACT
rho positivity typing: SATISFIED
continuous fitted parameter: NONE
physical rhythm uniqueness: NOT CLAIMED
branch -> family operator: OPEN
physical CKM assignment: OPEN
```
