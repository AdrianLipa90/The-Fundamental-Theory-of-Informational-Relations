# Claim Ledger — v0.1 frozen baseline + v0.2 extension

## Frozen v0.1 baseline

| ID | Claim | Status | Falsification / open debt |
|---|---|---|---|
| C-001 | Binary entropy has a unique maximum at `sigma=1/2` with value `ln(2)`. | THEOREM | Standard differentiation. |
| C-002 | `J(s)=1-conj(s)` has fixed set `Re(s)=1/2`. | THEOREM | Elementary algebra. |
| C-003 | Two complementary amplitudes cancel at phase `pi` iff `sigma=1/2`. | THEOREM | Exact algebra. |
| C-004 | The balanced Bloch latitude has Berry holonomy `-1`. | THEOREM | Gauge-invariant holonomy. |
| C-005 | `eta(s)=(1-2^(1-s))*zeta(s)` and `eta(1)=ln(2)`. | THEOREM | Classical analytic identity. |
| C-006 | `sigma=Re(s)` is the correct probability coordinate. | MODEL POSTULATE | Requires canonical operator or integral representation. |
| C-007 | Every nontrivial zero is a genuine two-branch cancellation state. | OPEN GAP | Must avoid zero factors, fitted normalization, and circular use of RH. |
| C-008 | All nontrivial zeros lie on the critical line. | OPEN | Would follow from C-007 plus C-003, but C-007 is unproved. |

The v0.1 entries above are historical and are not rewritten. The v0.2 records below refine their logical content append-only.

## v0.2 inverse-holonomy extension

| ID | Claim | Status | Falsification / open debt |
|---|---|---|---|
| C-009 | With `u=s-1/2`, the zeta involution becomes `J_tilde(u)=-conj(u)` and has fixed set `Re(u)=0`. | THEOREM | Elementary coordinate conjugation. |
| C-010 | The reciprocal map `I(u)=1/u` is an involution on `C\{0}` and commutes with `J_tilde`. | THEOREM | Exact complex algebra. |
| C-011 | The centred critical axis is invariant as a set under reciprocal inversion: `i*tau -> -i/tau`. | THEOREM | Exact for `tau != 0`; does not imply zero-to-zero mapping. |
| C-012 | `C(u)=u/(1+abs(u))` maps the centred point to disk centre and the asymptotic region to the unit-boundary limit. | THEOREM | Exact radial compactification; deliberately non-holomorphic. |
| C-013 | Under affine endpoint-preserving strip-to-simplex identification, the unique probability coordinate is `p=Re(s)`. | CONDITIONAL THEOREM | Depends explicitly on affine + endpoint assumptions. |
| C-014 | The physical zero-state representation is compelled to use that affine coordinate as its branch population. | MODEL POSTULATE / OPEN | Requires a canonical zeta-derived state/operator representation. |
| C-015 | Berry phase and Aharonov–Bohm phase are both `U(1)` connection holonomies; phase `pi mod 2*pi` gives holonomy `-1`. | STRUCTURAL THEOREM | Does not identify their physical potentials. |
| C-016 | `L_H=c/H_0` and `r_H=H_0 L/c` provide a dimensionless radial normalization with `r_H(L_H)=1`. | DEFINITION / IDENTITY | Treating this as the compactified zeta boundary is not standard cosmology. |
| C-017 | The AB/Berry local holonomy sector and Hubble radial normalization are two coordinates of one TIR potential-tension architecture. | MODEL POSTULATE | Requires an explicit dimensionless bridge and independent physical derivation. |
| C-018 | Canonical zerohood enforces a gauge-invariant `pi` loop closure. | OPEN POSTULATE | Must be derived from zeta data, not inserted as a boundary condition. |
| C-019 | The naive lifted map `T(s)=1/2 + 1/(s-1/2)` is a symmetry of the nontrivial zeta zero set. | NEGATIVE CONTROL / FAIL | The first 10 tabulated zeros map to points with `abs(zeta(T(rho))) > 0.1`; the first image is about `1.447`. Reciprocal symmetry is therefore currently only an ambient/axis symmetry, not a zero-set symmetry. |

## Promotion verdict

- **C-006 is partially promoted, not fully closed.** Its coordinate-theoretic core becomes C-013, a conditional theorem. Its physically substantive remainder is isolated as C-014.
- **C-004 gains a stronger structural interpretation** through C-015: Berry and Aharonov–Bohm phases belong to the same `U(1)` holonomy class.
- **C-010/C-011 do not promote C-007 by themselves.** C-019 explicitly blocks the naive zero-to-zero interpretation of reciprocal inversion.
- **C-007 remains OPEN GAP.** Reciprocal symmetry does not yet construct a genuine zero-state cancellation representation.
- **C-008 remains OPEN.** No unconditional proof of the Riemann hypothesis is claimed.
- `W_[ij]` is referenced only as a broader TIR holonomic relation/information connector; its definition and dynamics are out of scope for this module.
