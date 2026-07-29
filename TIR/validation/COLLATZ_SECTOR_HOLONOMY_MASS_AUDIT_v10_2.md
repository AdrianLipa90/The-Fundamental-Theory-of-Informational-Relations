# Collatz sector-holonomy mass audit v10.2 / method correction v10.2r1

## Corrected status

- **Technical status:** PASS
- **Methodological status:** RETROSPECTIVE STRUCTURAL CANDIDATE — not a prospective sealed test
- **Comparative status:** retrospective signal — the candidate reduces the global non-anchor mean absolute log error from `2.2993` to `0.5137`
- **Sector-relative status:** retrospective signal with one explicit open baseline — excluding `u`, the geometric-mean multiplicative error is `1.141x`
- **Physical mass-spectrum status:** FAIL / OPEN
- **Canonical promotion:** DENIED
- **Claimed mass derivation:** no

### Why the correction is necessary

The executable operator uses no non-electron mass as an input, fits no continuous coefficient, and inserts no particle-specific residual correction. However, the **form of the v10.2 sector operator was selected after inspection of the v10.1 residual pattern**. Therefore fingerprinting the code before its internal benchmark does not make the overall scientific test prospective.

The v10.2 numerical trace is retained as a useful hypothesis generator. The v10.2r1 ledger supersedes its original epistemic classification without changing the formula, predictions or operator fingerprint.

## 1. Candidate operator

The v10.1 base coordinate is

\[
Q_i=
\frac{(A_e/A_i)^{3/4}-1}{L_3\kappa}
+
\frac{R_i-R_e}{\kappa},
\qquad
\kappa=\frac{\ln2}{24\pi}.
\]

The retrospective v10.2 candidate is

\[
\ln\frac{m_i}{m_e}=Q_i+G_i+H_i+W_i.
\]

### Collatz generation release

\[
G_i=(L_5-c_i)\frac{\ell_i-\ell_e}{L_3},
\]

where `c_i` is the declared colour depth and `ell_i` is the ordinary Collatz stopping length of the twin-prime centre `p+1` attached to the existing Euler–Berry row.

For the canonical centres,

\[
4\mapsto \ell=2,
\qquad
6\mapsto \ell=8,
\qquad
12\mapsto \ell=9.
\]

The release depth is `L5=5` for colourless charged leptons and `L5-3=2` for colour-depth-three quarks.

### Signed orientation release

\[
H_i=
\frac{s_i}{\max(1,c_i)}
\ln\left[
\frac{1+|v_{7,i}|/\kappa}
     {1+|v_{7,a(i)}|/\kappa}
\right],
\]

with `s_i=+1` on an `H_plus` path and `s_i=-1` on an `H_minus` path. The reference `a(i)` is the first structural generation of the same family, not an observed mass anchor.

### White-Thread release

For down quarks only,

\[
W_i=L_4\ln w_i,
\qquad
w_i=\max_{u\in\{u,c,t\}}
|\mathcal O_{\rm open}(u,d_i)|.
\]

The selected structural channels are `u -> d`, `u -> s`, and `c -> b`. No observed CKM value enters the executable selection. The choice of this form nevertheless belongs to the retrospective model-selection history and is not promotion-eligible.

## 2. Provenance

Structural artifacts used by the executable:

- Euler–Berry action table v1.6;
- mandatory Ramanujan seed-suppression table v2.1;
- projection-orientation sector basis v3.4;
- White-Thread open-holonomy matrix v3.5.

Observed executable input:

- electron mass only, as dimensional anchor.

Validation-only data inside the executable:

- the remaining eight charged-fermion masses.

Heavy-quark orientation rows retain their existing `old_doc_bridge_ansatz_quarantined` status.

## 3. Numerical result

| Fermion | Quarter-power prediction (GeV) | Sector candidate (GeV) | Validation target (GeV) | Sector log error |
|---|---:|---:|---:|---:|
| e | 0.000510999 | 0.000510999 | 0.000510999 | 0.0000 |
| mu | 0.00152075 | 0.108819 | 0.105658 | +0.0295 |
| tau | 0.0201752 | 1.64836 | 1.77686 | -0.0751 |
| d | 0.0275743 | 0.00461801 | 0.00467 | -0.0112 |
| s | 0.121639 | 0.120407 | 0.0934 | +0.2540 |
| b | 4.17760 | 5.33173 | 4.18 | +0.2434 |
| u | 0.0522391 | 0.0522391 | 0.00216 | +3.1857 |
| c | 0.248465 | 1.37826 | 1.27 | +0.0818 |
| t | 10.3185 | 217.213 | 172.69 | +0.2294 |

Global metrics, excluding the electron anchor:

| Metric | Quarter power v10.1 | Retrospective sector candidate |
|---|---:|---:|
| Mean absolute log error | 2.2993 | 0.5137 |
| Median absolute log error | 2.2966 | 0.1556 |
| Maximum absolute log error | 4.4781 | 3.1857 |
| Geometric-mean multiplicative error | 9.967x | 1.672x |

Excluding only the unresolved `u` baseline:

- mean absolute log error: `0.1320`;
- median absolute log error: `0.0818`;
- maximum absolute log error: `0.2540`;
- geometric-mean multiplicative error: `1.141x`.

All three generation orders remain correct:

\[
e<\mu<\tau,
\qquad
d<s<b,
\qquad u<c<t.
\]

## 4. Permitted interpretation

The result supports only the following statement:

> The combination of existing Collatz-generation, orientation and White-Thread coordinates is a promising retrospective structural candidate for the relative charged-fermion hierarchy.

It does **not** establish a mass derivation or a prospective confirmation. The first-generation up-quark absolute position remains too high by a factor of approximately `24.18`.

A `u`-specific subtraction is forbidden. Before inspecting any new validation result, the next operator or independent observable must be frozen in a separate preregistration artifact.

## 5. Execution and supersession

Original numerical audit:

```bash
python TIR/validation/collatz_sector_holonomy_mass_audit_v10_2.py
```

Corrected method-status ledger:

```bash
python TIR/validation/collatz_sector_holonomy_mass_audit_v10_2r1.py
```

Authoritative status output:

- `TIR/validation/results/collatz_sector_holonomy_mass_audit_v10_2r1.json`

The v10.2 prediction CSV remains numerically valid; only its original methodological classification is superseded.
