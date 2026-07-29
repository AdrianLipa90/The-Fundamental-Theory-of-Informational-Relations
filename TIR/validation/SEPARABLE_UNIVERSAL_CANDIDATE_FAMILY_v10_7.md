# Separable universal candidate family v10.7

## Status

- **Artifact class:** prospective candidate-family freeze
- **Candidate count:** exactly three
- **Candidate selected:** no
- **Known charged-fermion masses used:** no
- **Future Higgs likelihood inspected:** no
- **Ramanujan layer:** mandatory
- **Debt 9:** open
- **Canonical promotion:** denied
- **Clean-checkout CI execution:** pending; deterministic arithmetic ledger frozen

This artifact follows the v10.4 architecture no-go and the v10.6 observable-identifiability correction. It freezes a finite family of universal maps before any qualifying future Higgs-coupling likelihood is opened.

## 1. Source layers

The candidate family uses only pre-mass repository artifacts:

1. corrected v1.0 representation actions;
2. the universal v0.6 charged-Dirac chiral cost;
3. the v1.0 tetrahedral-first generation damping units;
4. the v2.1 Ramanujan seed-release layer;
5. the already frozen Collatz exponent
   \[
   \alpha_C=\frac34;
   \]
6. the informational preference quantum
   \[
   \kappa=\frac{\ln2}{24\pi};
   \]
7. the structural constant \(L_3=7\).

The erroneous v0.7 `blocked` status field is not used. Candidate construction reads the corrected v1.0 representation table satisfying

\[
-Y_L+Y_H+Y_R=0.
\]

## 2. Separable architecture

For charged sector \(f\) and generation \(g\), define

\[
\boxed{
\ln y_{f,g}=F(S_f)+D(G_g,R_g)
}
\]

where:

- \(S_f\) is invariant across generations inside a charged sector;
- \(G_g\) is the shared v1.0 generation damping action;
- \(R_g\) is the mandatory Ramanujan release;
- the same algebraic functions \(F\) and \(D\) act on every charged sector.

The sector coordinate is

\[
S_f=A_f^{\rm rep}+C_{\rm chir},
\qquad C_{\rm chir}=2,
\]

which gives

\[
S_\ell=4.5,
\qquad
S_d=3.0876164691516155,
\qquad
S_u=2.920949802484949.
\]

The generation damping coordinates are

\[
G_1=0.8471633855025916,
\qquad
G_2=0.6088811663290957,
\qquad
G_3=0.23926393244694075.
\]

The corresponding Ramanujan release units are

\[
R_1=0.4754443238393299,
\qquad
R_2=1.0262897039931138,
\qquad
R_3=2.442442115365772.
\]

No observed mass is used to obtain these coordinates.

## 3. Frozen candidate C1 — linear separable action

\[
F_1(S)=-S,
\qquad
D_1(G,R)=-G+R.
\]

This is the direct exponential-damping interpretation already stated by the v1.0 action layer: larger structural action gives stronger suppression.

## 4. Frozen candidate C2 — quarter-power separable action

\[
F_2(S)=-S^{3/4},
\qquad
D_2(G,R)=-G^{3/4}+R.
\]

This is the minimal deformation obtained by applying the already frozen Collatz quarter-power to the two independent structural actions while preserving the Ramanujan release additively.

## 5. Frozen candidate C3 — inverse quarter-power information potential

\[
F_3(S)=\frac{S^{-3/4}}{L_3\kappa},
\qquad
D_3(G,R)=\frac{G^{-3/4}}{L_3\kappa}+R.
\]

This is the universal-potential form corresponding to the inverse-action coordinate used in the v10.1 quarter-power bridge. It produces a much larger generation dynamic range than C1 or C2. That numerical extremity is retained rather than removed after inspection.

## 6. Orthogonal prospective observables

### 6.1 Class-A sector baseline

Charm and the muon are both second-generation states. Therefore

\[
\ln\frac{y_c}{y_\mu}
=
F(S_u)-F(S_\ell),
\]

because the complete generation term \(D(G_2,R_2)\) cancels exactly.

Thus the primary class-A observable is refined to:

> the first qualifying joint ATLAS/CMS direct charm-to-muon Higgs-coupling likelihood released after 2026-07-29.

This supersedes the v10.6 use of \(y_c/y_\tau\) as the primary class-A observable. The earlier ratio crossed both sector and generation and therefore did not isolate the sector baseline.

### 6.2 Class-B generation release

Charm and top belong to the same up-type/heavy structural sector in the frozen architecture. Therefore

\[
\ln\frac{y_c}{y_t}
=
D(G_2,R_2)-D(G_3,R_3),
\]

because the sector term cancels.

Thus the class-B observable remains the first qualifying post-2026-07-29 joint ATLAS/CMS direct charm-to-top Higgs-coupling likelihood.

## 7. Frozen prospective predictions

| Candidate | \(y_c/y_\mu\), class A | \(y_c/y_t\), class B |
|---|---:|---:|
| C1 linear separable action | 4.850346751338371 | 0.16766796647328305 |
| C2 quarter-power separable action | 2.3521800134268784 | 0.17147213462587316 |
| C3 inverse quarter information potential | 6.858021228826222 | \(2.8101955040512466\times10^{-11}\) |

All three candidates remain active. No candidate is preferred using known masses or by comparing these values with an already available likelihood.

## 8. Cross-transfer outputs

The same formulas also emit coordinates for down quarks and charged leptons. Examples include:

- \(y_s/y_\mu\), comparing second-generation down and lepton sectors;
- \(y_u/y_e\), comparing first-generation up and lepton sectors;
- \(y_\mu/y_e\), \(y_\tau/y_\mu\), \(y_c/y_u\), and \(y_t/y_c\), testing universal generation transport.

These outputs are recorded before external comparison and may not be used to discard a candidate retrospectively.

## 9. Prospective decision rule

For each candidate and each assigned observable:

1. the prediction is frozen by the v10.7 fingerprint;
2. the first qualifying post-2026-07-29 joint ATLAS/CMS likelihood is used;
3. PASS requires the frozen value to lie inside the published 95% confidence region;
4. FAIL is retained without changing the formula;
5. no observable substitution is allowed after inspection;
6. the three-candidate family requires multiplicity-aware interpretation;
7. if no qualifying likelihood appears, canonical promotion remains unavailable.

## 10. Integrity conclusion

\[
\boxed{
\text{candidate family frozen}
\;\land\;
\text{no mass benchmark}
\;\land\;
\text{no candidate selected}
\;\land\;
\text{physical derivation open}
}
\]

The candidate-family fingerprint is

`2bbf9985b6a4fc9d19d039e117b15eb446a51a3e8828a2894c8d797bb35f23f4`.

Executable:

```bash
python TIR/validation/separable_universal_candidate_family_v10_7.py
```

Outputs:

- `TIR/validation/results/separable_universal_candidate_family_v10_7.json`
- `TIR/validation/results/separable_universal_candidate_predictions_v10_7.csv`
