# TIR Collatz–Poincare Branch Rhythm Candidate Freeze v0.1

Status: `COLLATZ_POINCARE_BRANCH_RHYTHM_CANDIDATE_FROZEN_PREVALIDATION`

Freeze date: `2026-09-19`

## Purpose

Stage 43 establishes an ordered Collatz-step Hamiltonian scaffold but retains the exact rhythm (ho_s(k)) as an open derivation debt.

Stage 49 and the current crosswalk independently establish the exact hyperbolic translation lengths of the two normalized Collatz branch generators in the standard curvature-(-1) Poincare normalization:

[
ell_E=ln 2,
qquad
ell_O=ln 3.
]

The archival reference Hamiltonian states only the formal type requirement

[
ho_s(k)>0
]

and explicitly classifies its historical bounded rhythm as a model choice.

This file freezes the minimal parameter-free branch-local candidate before any CKM, PMNS, mass, or other physical-target comparison.

## Frozen candidate

For a Collatz step with branch symbol (b_kin{E,O}), define

[
oxed{
ho_{m geo}(k)
=
egin{cases}
ln 2,& b_k=E,\\
ln 3,& b_k=O.
end{cases}
}
]

Equivalently,

[
oxed{ho_{m geo}(k)=ell_{b_k}.}
]

Both values are strictly positive and dimensionless.

No continuous coefficient is introduced.

## Exact orientation companion

The branch signed log-Jacobian cocycle is

[
sigma_E=-ln2,
qquad
sigma_O=+ln3.
]

Hence the exact factorization is

[
oxed{
sigma_b=chi_b,ho_{m geo}(b),
qquad
chi_E=-1,quad
chi_O=+1.
}
]

The candidate therefore keeps positive Hamiltonian rhythm magnitude and branch orientation as separate typed objects.

## Word accumulation

For a branch word

[
w=b_0b_1cdots b_{K-1},
]

define the accumulated geometric rhythm

[
R_{m geo}(w)
=
sum_{k=0}^{K-1}ho_{m geo}(b_k).
]

If the word contains (N_E) even branches and (N_O) odd branches,

[
oxed{
R_{m geo}(w)
=
N_Eln2+N_Oln3
=
ln(2^{N_E}3^{N_O}).
}
]

Therefore the candidate is additive under word concatenation.

For the Stage-48 words,

[
w_1=	exttt{OEOE},
]

so

[
R_{m geo}(w_1)=2ln2+2ln3=ln36.
]

For the 90-step third-family word with (N_O=34), (N_E=56),

[
R_{m geo}(w_3)
=
56ln2+34ln3
=
ln(2^{56}3^{34}).
]

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

[
ho_s(k)=ho_{m geo}(k)
]

as the unique physical rhythm.

It freezes (ho_{m geo}) as the minimal source-derived, positive, parameter-free candidate admissible under the current Hamiltonian typing.

It also does not assign (E) or (O) to a physical family generator. The branch-symbol-to-family-operator map remains open.

## Validation gates

1. Recompute (ell_E=ln2) and (ell_O=ln3) from the normalized Stage-49 branch matrices.
2. Verify (ho_E,ho_O>0).
3. Verify the exact signed factorization (sigma_b=chi_bho_b).
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
