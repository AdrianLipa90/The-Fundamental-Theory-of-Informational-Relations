# The Information-Spinor Critical Axis

**Author:** Adrian Lipa — Independent Researcher, Doncaster, United Kingdom  
**Version:** v0.2 — 7 August 2026  
**Parent programme:** The Fundamental Theory of Informational Relations (TIR)

## Research question

Why is the line `Re(s) = 1/2` simultaneously:

- the fixed axis of the completed Riemann-zeta functional symmetry;
- the maximum-entropy point of a binary Shannon distribution;
- the equator of a two-level Bloch geometry;
- the unique equal-weight point supporting exact destructive interference at relative phase `pi`;
- the latitude whose full azimuthal cycle has Berry holonomy `-1`;
- the fixed transverse centre after the shift `u = s - 1/2`;
- invariant as a set under the reciprocal chart `u -> 1/u`?

Version v0.2 additionally studies a finite radial compactification, the common `U(1)` holonomy structure of Berry and Aharonov–Bohm phases, and a dimensionless Hubble radial normalization. These additions are deliberately separated into exact mathematics and explicit model postulates.

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

## v0.2 exact reciprocal-geometry results

With

```text
u = s - 1/2,
J_tilde(u) = -conj(u),
I(u) = 1/u,
```

we now have exact results:

```text
I(I(u)) = u,
I(J_tilde(u)) = J_tilde(I(u)),
I(i*tau) = -i/tau  for tau != 0.
```

Thus the centred critical axis is invariant as a set under reciprocal inversion. This does **not** imply that a zeta zero is mapped to another zeta zero.

The finite centre-to-boundary representation is kept mathematically distinct:

```text
C(u) = u / (1 + abs(u)).
```

`C` is intentionally non-holomorphic, with `C(0)=0` and `abs(C(u)) -> 1` as `abs(u) -> infinity`. In contrast, `1/u` is conformal on the punctured plane.

## Partial promotion of the probability-coordinate assumption

The v0.1 claim `sigma = Re(s) is the correct probability coordinate` is split in v0.2.

If `p(x)=a*x+b` is required to be an affine map from the strip coordinate `x=Re(s) in [0,1]` to the binary simplex with

```text
p(0)=0,
p(1)=1,
```

then uniquely

```text
p(x)=x.
```

This is now a **CONDITIONAL THEOREM** under the stated affine/endpoint assumptions. The stronger claim that a canonical zeta zero-state representation must physically use this coordinate as branch population remains **MODEL POSTULATE / OPEN**.

## Aharonov–Bohm, Berry, and Hubble scope

Berry and Aharonov–Bohm phases are treated as members of the same mathematical `U(1)` connection-holonomy class:

```text
U_gamma = exp(i*theta_gamma).
```

At `theta_gamma = pi mod 2*pi`, the holonomy is `-1`.

The Hubble scale is used only as a dimensionless radial normalization:

```text
L_H = c / H_0,
r_H(L) = H_0 * L / c,
r_H(L_H) = 1.
```

The statement that the AB/Berry local holonomy sector and the Hubble radial sector are two coordinates of one TIR **potential-tension** architecture is an explicit **MODEL POSTULATE**, not an established identity of gauge theory or cosmology.

`W_[ij]` is mentioned only as the broader TIR holonomic relation/information connector. Its formal definition and dynamics are out of scope for this critical-axis module and remain in TIR.

## Scientific status

| Layer | Status |
|---|---|
| Binary Shannon derivation | **THEOREM / PASS** |
| Complement fixed-point derivation | **THEOREM / PASS** |
| Two-channel cancellation theorem | **THEOREM / PASS** |
| Bloch/Berry/spinor derivation | **THEOREM / PASS** |
| Dirichlet eta bridge | **THEOREM / PASS** |
| Centred reciprocal involution and commutation | **THEOREM / PASS** |
| Critical-axis set invariance under `1/u` | **THEOREM / PASS** |
| Radial centre-to-boundary compactification | **THEOREM / PASS** |
| Affine strip-to-simplex `p=Re(s)` | **CONDITIONAL THEOREM** |
| Berry / Aharonov–Bohm common `U(1)` holonomy class | **STRUCTURAL THEOREM** |
| Hubble radial normalization | **DEFINITION / PASS** |
| AB/Hubble common TIR potential-tension architecture | **MODEL POSTULATE** |
| Canonical zero-state representation | **OPEN GAP** |
| Riemann hypothesis | **OPEN — NOT CLAIMED** |

The repository does **not** claim that symmetry, reciprocal geometry, or holonomy alone proves the Riemann hypothesis. Functional symmetry still permits hypothetical off-axis quartets. The missing theorem must force pointwise self-duality or construct a canonical zero-state/spectral representation that excludes pairwise balance without local balance.

## Repository structure

```text
.
├── monograph/
│   ├── main.tex
│   ├── chapters/
│   │   └── 08b_inverse_holonomy_hubble.tex
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
2. Derive equal branch normalization from unitarity, symmetry, a positive metric, or a canonical gauge connection.
3. Prove that zerohood is genuine cancellation of two nonzero branch amplitudes.
4. Determine whether the centred reciprocal symmetry acts on a canonical zeta-derived object, rather than only on the ambient coordinate plane.
5. Derive the `pi` holonomic zero-closure condition from zeta data rather than impose it.
6. Produce an explicit dimensionless bridge if the AB/Berry and Hubble sectors are to be promoted beyond the TIR potential-tension postulate.
7. Convert global zeta symmetry into pointwise self-duality, or construct a self-adjoint / positive spectral mechanism that enforces the critical axis.

## Integrity policy

- Technical PASS is distinct from physical or mathematical closure.
- Negative results and failed operator candidates remain in the history.
- Change logs are append-only.
- No individual zero ordinates may be fitted into a claimed Hilbert–Pólya operator.
- A construction that assumes `Re(s)=1/2` before deriving zerohood is circular and must be rejected.
- `1/u` must not be described as non-conformal; the separate radial compactification carries that role.
- The Hubble normalization must not be presented as a cosmological horizon theorem.
- The AB/Hubble potential-tension identification remains a model postulate until an independent bridge is derived.

## Licensing

See [`LICENSES.md`](LICENSES.md). Code is AGPL-3.0-or-later; the monograph and research documentation are CC BY 4.0; public test vectors are CC0 1.0.

## Citation

Use [`CITATION.cff`](CITATION.cff) and cite the exact Git commit or release used.
