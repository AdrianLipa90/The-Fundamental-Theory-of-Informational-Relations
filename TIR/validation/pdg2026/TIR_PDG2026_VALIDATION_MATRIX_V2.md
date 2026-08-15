# TIR ↔ PDG 2026 Validation Matrix V2

Freeze date: **2026-08-15**  
Repository base: current `main` at branch creation (`df8a6e1321ecf2e2c8819f4e9d5ec7d4f997d170`)

This matrix separates numerical compatibility from provenance and precision-level validation. Approximate sigma pulls are diagnostics, not substitutes for full correlated likelihoods.

| Sector | Observable | TIR | PDG 2026 / reference | Status | Pull | Provenance |
|---|---|---:|---:|---|---:|---|
| CKM | Vud | 0.97439 | 0.97431 | **PASS_COMPATIBILITY** | +0.50 | POSTDICTION |
| CKM | Vus | 0.22485 | 0.22517 | **PASS_COMPATIBILITY** | -0.47 | POSTDICTION |
| CKM | Vub | 0.003628 | 0.003763 | **PASS_COMPATIBILITY** | -1.63 | POSTDICTION |
| CKM | Vcd | 0.22470 | 0.22503 | **PASS_COMPATIBILITY** | -0.49 | POSTDICTION |
| CKM | Vcs | 0.97357 | 0.97345 | **PASS_COMPATIBILITY** | +0.75 | POSTDICTION |
| CKM | Vcb | 0.04082 | 0.04189 | **PASS_COMPATIBILITY** | -1.55 | POSTDICTION |
| CKM | Vtd | 0.00886 | 0.00863 | **PASS_COMPATIBILITY** | +1.21 | POSTDICTION |
| CKM | Vts | 0.04001 | 0.04117 | **PASS_COMPATIBILITY** | -1.71 | POSTDICTION |
| CKM | Vtb | 0.99916 | 0.999115 | **PASS_COMPATIBILITY** | +1.55 | POSTDICTION |
| CKM | delta_CKM | 66.42 deg | 1.154 +/- 0.025 rad | **PASS_STRONG_COMPATIBILITY** | +0.21 | POSTDICTION |
| CKM | J_CP structural | 3.11e-5 | 3.16(+0.13/-0.11)e-5 | **PASS_STRONG_COMPATIBILITY** | -0.45 | POSTDICTION |
| Neutrino | sin² theta12 | 0.30385 | global fits ~0.303-0.308 | **PASS_COMPATIBILITY** | -0.38..+0.06 | POSTDICTION |
| Neutrino | Delta m²21 | 7.500e-5 eV² | global fits ~7.37-7.55e-5 eV² | **PASS_COMPATIBILITY** | -0.25..+0.87 | POSTDICTION |
| Neutrino | sin² theta23 | 0.54082 | octant-dependent ~0.47 or ~0.56 | **AMBIGUOUS_COMPATIBILITY** | -1.35..+4.17 | POSTDICTION |
| Neutrino | sin² theta13 | 0.02041 | global fits ~0.02195-0.02230 | **TENSION** | -3.98..-2.66 | POSTDICTION |
| Neutrino | delta_CP | 246.1 deg | NO best fits ~177-216 deg; broad regions | **INCONCLUSIVE** | +0.97..+3.64 | POSTDICTION |
| Neutrino | absolute masses | 0.00501, 0.01002, 0.0501 eV | not fixed by oscillations | **NOT_INDEPENDENTLY_TESTED** | NA | MODEL_OUTPUT |
| Charged leptons | electron | 0.511641997 MeV | 0.510998951 MeV | **FAIL_PRECISION** | +4.02e6 | RETROSPECTIVELY_REFINED |
| Charged leptons | muon | 104.831758 MeV | 105.658376 MeV | **FAIL_PRECISION** | -3.59e5 | RETROSPECTIVELY_REFINED |
| Charged leptons | tau | 1767.50388 MeV | 1776.93 MeV | **FAIL_PRECISION** | -105 | RETROSPECTIVELY_REFINED |
| Baryon octet | mass pattern | mean rel. error ~0.33% revised | PDG masses used as targets | **PROVENANCE_CONTAMINATED** | NA | RETROSPECTIVE_REFINEMENT |
| Baryon decuplet | Delta/Sigma*/Xi*/Omega | residuals ~0.18-0.45% | PDG 2026 masses | **CANDIDATE_COMPATIBILITY** | NA | POSTDICTION_WITH_PROTON_ANCHOR |
| Mesons | pion printed formula | E_P exp(-6/pi) | printed target 139.57 MeV | **FORMULA_BROKEN** | NA | INTERNAL_ARITHMETIC_FAIL |
| Mesons | kaon printed formula | E_P exp(-(zeta(2)-1)) | printed target 493.68 MeV | **FORMULA_BROKEN** | NA | INTERNAL_ARITHMETIC_FAIL |
| Mesons | eta/eta' | 547.86 / 957.78 MeV | identical displayed PDG values | **PROVENANCE_INCOMPLETE** | NA | INSUFFICIENT_DERIVATION |
| Mesons | heavy/vector table | near-exact PDG equality | PDG values | **REPRODUCTION_NOT_VALIDATION** | NA | INSUFFICIENT_DERIVATION |
| Electroweak | VEV v | 244.89 GeV | GF-derived ~246.2197 GeV | **CLOSE_RELATIVE_MATCH_NOT_INDEPENDENT** | NA | DERIVED_REFERENCE |
| Electroweak | sin² theta_W | 0.23141537 | scheme-dependent | **SCHEME_UNDEFINED_TENSION** | +3.26 vs MSbar | SCHEME_NOT_DECLARED |
| Electroweak | alpha^-1(0) | 137.036772600 | 137.035999177(21) | **FAIL_PRECISION** | +36830 | POSTDICTION |
| Electroweak | M_W | 83.96 GeV | 80.3625 +/- 0.0077 GeV | **FAIL_PRECISION** | +467 | POSTDICTION |
| Electroweak | M_Z | 95.77 GeV | 91.1879 +/- 0.0020 GeV | **FAIL_PRECISION** | +2291 | POSTDICTION |
| Higgs | M_H | 126.07 GeV | ATLAS Run1+2 125.11 +/- 0.108 GeV | **FAIL_PRECISION_TENSION** | +8.88 | RETROSPECTIVELY_REVISED |
| Quark masses | u,d,s,c,b,t | prime labels + mass table | scheme/scale-dependent | **NOT_TESTABLE_CURRENTLY** | NA | MASS_MAP_NOT_DERIVED |
| Strong CP | theta_QCD / neutron EDM | existing monograph values | current references | **NOT_AUDITED_IN_THIS_ADDENDUM** | NA | UNKNOWN_UNTIL_PROBED |
| Gauge anomalies | A1-A5 | existing monograph values | current references | **NOT_AUDITED_IN_THIS_ADDENDUM** | NA | UNKNOWN_UNTIL_PROBED |
| Cosmology | Omega_Lambda / rho_Lambda | existing monograph values | current references | **NOT_AUDITED_IN_THIS_ADDENDUM** | NA | UNKNOWN_UNTIL_PROBED |

## Interpretation

`PASS` means compatibility, not proof of TIR. `FAIL_PRECISION` means the printed formula is incompatible with current uncertainty if interpreted as a precision prediction. `PROVENANCE_*` means agreement cannot be counted as independent evidence. `FORMULA_BROKEN` means the printed expression does not reproduce its own numerical result. Failed and tension results are retained and may not be silently overwritten.
