# TIR 600-cell S3 angular carrier candidate v0.1

Status: `CANDIDATE / ACTIVE_WORKING_VERSION / STRUCTURAL_ONLY / PHYSICAL_BINDING_OPEN`

Date: 2026-09-11

## Status semantics

Within this workstream, `CANDIDATE` means an active working implementation. It may be executed, benchmarked, composed with other candidate components, and used to produce validation evidence. It is not a synonym for unused, disabled, speculative-only, or documentation-only.

The status boundary is:

```text
CANONICAL   = admitted contract; promotion gates passed
CANDIDATE   = active working contract; provenance flag mandatory
QUARANTINED = excluded from working routes except diagnosis
FAILED      = failed evidence/gate; excluded except diagnosis
```

Candidate results MUST carry candidate provenance and MUST NOT be silently reported as canonical.

## 600-cell carrier

Let `V_600` be the 120 vertices of the regular 600-cell normalized to the unit 3-sphere `S^3`. Nearest-neighbour incidence gives a 12-regular graph with 720 undirected edges.

Its adjacency spectrum contains the following six sectors:

| ell | multiplicity | adjacency eigenvalue | S3 angular eigenvalue ell(ell+2) |
|---:|---:|---:|---:|
| 0 | 1 | 12 | 0 |
| 1 | 4 | 6 phi | 3 |
| 2 | 9 | 4 phi | 8 |
| 3 | 16 | 3 | 15 |
| 4 | 25 | 0 | 24 |
| 5 | 36 | -2 | 35 |

where `phi=(1+sqrt(5))/2`.

The multiplicities reproduce

\[
\dim H_\ell(S^3)=(\ell+1)^2
\]

for `ell=0..5`.

Define the candidate angular operator

\[
\mathcal L_{600}^{(c)}=\sum_{\ell=0}^{5}\ell(\ell+2)\Pi_\ell,
\]

where `Pi_ell` is the graph-spectral projector onto the listed eigenspace.

The supported carrier dimension is

\[
1+4+9+16+25+36=91.
\]

This is a finite structural model of the first six S3 angular sectors. It is not, by itself, a physical identification of an electron orbital, Kaluza-Klein compactification, soliton, or measured atomic observable.

## Quadrature boundary

The 120 vertices form a spherical 11-design on `S^3`. The independent repository validator checks every coordinate monomial of total degree <= 11, 1365 monomials in total, against analytic `S^3` moments.

The explicit degree-12 witness is

\[
\langle x_1^{12}\rangle_{600}-\langle x_1^{12}\rangle_{S^3}=\frac{1}{4096}.
\]

Thus the present candidate does not extrapolate the exact quadrature claim beyond degree 11. The working angular operator fails closed when asked to act on graph sectors outside the supported `ell=0..5` carrier.

## Relation to existing Platonic-Ramanujan work

The canonical 36D Platonic-Ramanujan carrier remains unchanged. The 600-cell construction is a new higher-dimensional candidate surface, not a retroactive reinterpretation of the accepted 36D result and not a reversal of the preserved rejection of additive `C_PR v0.1` runtime activation.

## Required promotion evidence

Before structural promotion:

1. candidate implementation tests PASS;
2. independent TIR validator PASS;
3. exact-byte/provenance receipt is recorded;
4. independent hyperspherical-harmonic comparison PASS;
5. existing PhaseNav invariants show no regression.

Physical promotion is a separate gate and remains `OPEN`.

Validator:

`TIR/validation/TIR_600CELL_S3_CANDIDATE_VALIDATION_V0_1.py`
