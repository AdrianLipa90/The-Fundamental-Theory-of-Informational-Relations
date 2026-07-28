# Collatz quarter-power mass audit v10.1

## Status

- **Technical status:** PASS
- **Comparative status:** PASS — the fixed `3/4` operator beats the fixed `2/3`, `1`, and `4/3` comparators on mean, median, and maximum absolute log error.
- **Physical mass-spectrum status:** FAIL / OPEN
- **Canonical promotion:** DENIED
- **Claimed mass derivation:** no

This module tests whether the Collatz contraction factor can enter the existing mass-scaling pipeline as a structural exponent. It does not replace the current mass operator and does not close Debt 9.

## 1. Collatz derivation of the numerical factor

For the accelerated odd Collatz map

\[
T(n)=\frac{3n+1}{2^{a(n)}},
\qquad a(n)=\nu_2(3n+1),
\]

uniform odd residue classes give

\[
\Pr[a=k]=2^{-k},\qquad k\geq 1,
\]

and therefore

\[
\mathbb E[a]=2.
\]

Ignoring the vanishing finite-size correction from `+1` at large `n`, the geometric mean multiplier is

\[
\rho_C
=\exp\!\left(\mathbb E\left[\ln\frac{3}{2^a}\right]\right)
=\exp(\ln3-2\ln2)
=\frac34.
\]

The executable checks this directly over all odd residues below `2^18`:

- mean valuation: `1.9999923706054688`
- empirical geometric multiplier: `0.7500039662304689`
- asymptotic value: `0.75`

This establishes `3/4` as the asymptotic log-geometric contraction of the accelerated map. It does **not**, by itself, prove that `3/4` must be a particle-mass exponent.

## 2. Bridge hypothesis

The current EB action coordinate decreases as the fermion mass hierarchy increases. Applying a direct power to `A_i/A_e` compresses the hierarchy in the wrong direction. The candidate therefore acts on the inverse structural coordinate

\[
X_i=\frac{A_e}{A_i}.
\]

For a fixed exponent `alpha`, the frozen mass-ratio trace is

\[
\ln\frac{m_i}{m_e}
=
\frac{X_i^{\alpha}-1}{L_3\kappa}
+
\frac{R_i-R_e}{\kappa},
\]

where

\[
\kappa=\frac{\ln2}{24\pi},
\qquad L_3=7,
\]

and `R_i` is the mandatory, non-fitted Ramanujan release coordinate already present in the archived pipeline.

The tested Collatz hypothesis is

\[
\boxed{\alpha=\rho_C=\frac34}.
\]

The identification of the Collatz multiplier with the scaling exponent is explicitly classified as a **bridge hypothesis**, not a theorem.

## 3. Provenance and no-hidden-fit policy

The structural operator is frozen and fingerprinted before validation masses are loaded.

Operator inputs:

- `archive/v7.9/full/14_debt3_debt6_zeta_polar_eb_action_v1_6/results/charged_fermion_eb_action_debt6_v1_6.csv`
- `archive/v7.9/full/19_debt5_ramanujan_seed_suppression_v2_1/results/ramanujan_seed_suppression_table_v2_1.csv`

Observed input:

- electron mass only, used as the dimensional anchor.

Validation-only table:

- `archive/v7.9/full/10_standard_model_derivation_stages/02_metatime_sm_mass_vectorization_v0_1/mass_action_validation_targets.csv`

No non-electron mass enters the frozen operator trace. A later exponent scan is labelled post-hoc and cannot promote or alter the predeclared operator.

## 4. Fixed-comparator result

Metrics exclude the electron anchor.

| Variant | Mean absolute log error | Median absolute log error | Maximum absolute log error | Geometric mean factor error |
|---|---:|---:|---:|---:|
| `2/3` | 2.5455 | 2.4786 | 4.6769 | 12.75x |
| **`3/4`** | **2.2993** | **2.2966** | **4.4781** | **9.97x** |
| `1` | 2.8506 | 3.1581 | 5.0162 | 17.30x |
| `4/3` | 5.3866 | 5.3597 | 7.7179 | 218.46x |

The `3/4` variant preserves the generation ordering in all three charged-fermion classes:

- `e < mu < tau`
- `d < s < b`
- `u < c < t`

A diagnostic scan over `alpha in [0.2, 1.5]` with step `0.005` places the minimum mean absolute log error at `alpha = 0.75`. Because this scan uses validation masses, it is recorded only as retrospective evidence; it is not a fitting licence.

## 5. Predicted values under the candidate

| Fermion | Prediction (GeV) | Validation target (GeV) |
|---|---:|---:|
| e | 0.000510999 | 0.000510999 |
| mu | 0.00152075 | 0.105658 |
| tau | 0.0201752 | 1.77686 |
| d | 0.0275743 | 0.00467 |
| s | 0.121639 | 0.0934 |
| b | 4.17760 | 4.18 |
| u | 0.0522391 | 0.00216 |
| c | 0.248465 | 1.27 |
| t | 10.3185 | 172.69 |

The near agreement for the bottom quark is not treated as closure because the charged-lepton and top-quark scales remain wrong by orders of magnitude.

## 6. Interpretation

The audit supports a narrow statement:

> Within the frozen inverse-EB-action plus Ramanujan coordinate tested here, the Collatz-derived exponent `3/4` is the best of the predeclared fixed comparators and is also the retrospective minimum of the scanned mean log error.

It does **not** support the stronger statement that elementary-particle masses have been derived from Collatz dynamics.

The remaining failure is structural rather than a small coefficient error. The common exponent improves global compression, but the present coordinate lacks enough sector-specific geometry to reproduce simultaneously:

- the charged-lepton release scale,
- the light-quark ordering magnitude,
- the top-quark hierarchy.

The next admissible step is to derive a sector term from already declared Euler–Berry, chirality, colour, and twin-prime geometry before looking at residuals. Particle-by-particle correction factors are forbidden.

## 7. Execution

```bash
python TIR/validation/collatz_quarter_power_mass_audit_v10_1.py
```

Outputs:

- `TIR/validation/results/collatz_quarter_power_mass_audit_v10_1.json`
- `TIR/validation/results/collatz_quarter_power_predictions_v10_1.csv`
