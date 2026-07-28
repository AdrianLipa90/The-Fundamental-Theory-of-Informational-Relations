# Collatz sector-holonomy mass audit v10.2

## Status

- **Technical status:** PASS
- **Comparative status:** PASS — the sector operator reduces the global non-anchor mean absolute log error from `2.2993` to `0.5137`.
- **Sector-relative status:** PASS with one explicit open baseline — excluding the unresolved `u` channel, the geometric-mean multiplicative error is `1.141x`.
- **Physical mass-spectrum status:** FAIL / OPEN
- **Canonical promotion:** DENIED
- **Claimed mass derivation:** no

This module continues the frozen v10.1 Collatz quarter-power trace. It introduces no fitted coefficient and no particle-specific correction.

## 1. Full operator

The v10.1 base coordinate is

\[
Q_i=
\frac{(A_e/A_i)^{3/4}-1}{L_3\kappa}
+
\frac{R_i-R_e}{\kappa},
\qquad
\kappa=\frac{\ln2}{24\pi}.
\]

The new structural release is

\[
\ln\frac{m_i}{m_e}=Q_i+G_i+H_i+W_i.
\]

### Collatz generation release

\[
G_i=(L_5-c_i)\frac{\ell_i-\ell_e}{L_3},
\]

where `c_i` is the declared colour depth and `ell_i` is the ordinary Collatz stopping length of the twin-prime centre `p+1` attached to the existing Euler–Berry row.

For the canonical centres

\[
4\mapsto \ell=2,\qquad
6\mapsto \ell=8,\qquad
12\mapsto \ell=9.
\]

Hence the release depth is `L5=5` for colourless charged leptons and `L5-3=2` for colour-depth-three quarks.

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

The maximum is selected from the pre-existing mass-free v3.5 open-holonomy matrix. The selected channels are

- `u -> d`,
- `u -> s`,
- `c -> b`.

No observed CKM value enters the selection.

## 2. Provenance and freeze policy

Structural inputs:

- Euler–Berry action table v1.6;
- mandatory Ramanujan seed-suppression table v2.1;
- projection-orientation sector basis v3.4;
- White-Thread open-holonomy matrix v3.5.

Observed input after freezing:

- electron mass only, as dimensional anchor.

Validation-only inputs:

- the remaining eight charged-fermion masses.

The operator is fingerprinted before validation masses are loaded. Heavy-quark orientation rows retain their existing `old_doc_bridge_ansatz_quarantined` status.

## 3. Result

| Fermion | Quarter-power prediction (GeV) | Sector prediction (GeV) | Validation target (GeV) | Sector log error |
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

| Metric | Quarter power v10.1 | Sector operator v10.2 |
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

## 4. Interpretation

The result isolates two logically different problems.

1. **Intra-sector release:** the common Collatz-generation, orientation and White-Thread terms reproduce the relative charged-lepton, down-quark and heavy up-quark hierarchy with a small residual scale.
2. **Inter-sector baseline:** the first-generation up-quark absolute position remains too high by a factor of approximately `24.18`.

The second failure must not be removed by inserting a `u`-specific phase. The next admissible step is to derive an absolute up-sector baseline from already declared colour/Berry/twin-prime geometry and then test it once, sealed, against the existing result.

## 5. Execution

```bash
python TIR/validation/collatz_sector_holonomy_mass_audit_v10_2.py
```

Outputs:

- `TIR/validation/results/collatz_sector_holonomy_mass_audit_v10_2.json`
- `TIR/validation/results/collatz_sector_holonomy_predictions_v10_2.csv`
