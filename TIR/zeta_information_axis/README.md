# The Information-Spinor Critical Axis

**Author:** Adrian Lipa — Independent Researcher, Doncaster, United Kingdom  
**Version:** v0.1 — 29 July 2026  
**Parent programme:** The Fundamental Theory of Informational Relations (TIR)

## Research question

Why is the line `Re(s) = 1/2` simultaneously:

- the fixed axis of the completed Riemann-zeta functional symmetry;
- the maximum-entropy point of a binary Shannon distribution;
- the equator of a two-level Bloch geometry;
- the unique equal-weight point supporting exact destructive interference at relative phase `pi`;
- the latitude whose full azimuthal cycle has Berry holonomy `-1`?

This repository derives those bridges rigorously and states the remaining implication as an explicit open representation problem.

## Central exact theorem

For

```text
A(sigma, phi) = sqrt(sigma) + exp(i phi) sqrt(1-sigma),
```

exact cancellation occurs if and only if

```text
sigma = 1/2,
phi = pi mod 2*pi.
```

At the same point:

```text
H_binary(1/2) = ln(2),
J(s) = 1-conj(s) fixes s exactly when Re(s)=1/2,
Berry holonomy = exp(-i*pi) = -1.
```

## Scientific status

| Layer | Status |
|---|---|
| Binary Shannon derivation | **THEOREM / PASS** |
| Complement fixed-point derivation | **THEOREM / PASS** |
| Two-channel cancellation theorem | **THEOREM / PASS** |
| Bloch/Berry/spinor derivation | **THEOREM / PASS** |
| Dirichlet eta bridge | **THEOREM / PASS** |
| Numerical reproduction | **TECHNICAL PASS** |
| Identification `sigma = Re(s)` | **MODEL POSTULATE** |
| Canonical zero-state representation | **OPEN GAP** |
| Riemann hypothesis | **OPEN — NOT CLAIMED** |

The repository does **not** claim that symmetry alone proves the Riemann hypothesis. Functional symmetry permits hypothetical off-axis quartets. The missing theorem must force pointwise self-duality rather than merely pairwise symmetry.

## Repository structure

```text
.
├── monograph/
│   ├── main.tex
│   ├── chapters/
│   └── references.tex
├── src/critical_axis/
│   └── core.py
├── scripts/
│   ├── make_figures.py
│   └── run_audit.py
├── tests/
│   └── test_core.py
├── reports/
│   ├── claim_ledger.md
│   ├── numerical_audit.json
│   └── numerical_audit.md
├── figures/
├── logs/
│   └── changes.jsonl
└── .github/workflows/
    └── compile.yml
```

## Reproduce

```bash
python3 -m pip install -e .[test]
python3 scripts/make_figures.py
python3 scripts/run_audit.py
pytest -q
make monograph
```

The PDF is written to:

```text
monograph/information_spinor_critical_axis.pdf
```

## Proof obligations for the next version

1. Construct an exact, noncircular complementary-branch representation of `xi(s)`.
2. Derive equal branch normalization from unitarity, symmetry, or a positive metric.
3. Prove that zerohood is genuine cancellation of two nonzero branch amplitudes.
4. Convert global zeta symmetry into pointwise self-duality.
5. Alternatively, construct a self-adjoint operator or a kernel-positivity theorem that enforces real spectral ordinates.

## Integrity policy

- Technical PASS is distinct from physical or mathematical closure.
- Negative results and failed operator candidates remain in the history.
- Change logs are append-only.
- No individual zero ordinates may be fitted into a claimed Hilbert–Pólya operator.
- A construction that assumes `Re(s)=1/2` before deriving zerohood is circular and must be rejected.

## Licensing

See [`LICENSES.md`](LICENSES.md). Code is AGPL-3.0-or-later; the monograph and research documentation are CC BY 4.0; public test vectors are CC0 1.0.

## Citation

Use [`CITATION.cff`](CITATION.cff) and cite the exact Git commit or release used.
