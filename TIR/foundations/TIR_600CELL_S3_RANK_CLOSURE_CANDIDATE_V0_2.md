# TIR 600-cell / S^3 Rank Closure Candidate v0.2

Status: `CANDIDATE / ACTIVE_WORKING_RESULT / PHYSICAL_BINDING_OPEN`

Date: 2026-09-11

This surface extends the executable 600-cell/S^3 candidate with the missing representation-rank test for `ell=6` and `ell=7`.

`CANDIDATE` here means active working mathematics: it may execute, feed dependent candidate work, and be benchmarked. It is not a canonical physical identification.

## Construction

For each `ell`, take the homogeneous harmonic polynomial space `H_ell(R^4)` and evaluate a numerical basis on the 120 unit vertices of the regular 600-cell in `S^3`.

The continuum dimension is

`dim H_ell(S^3) = (ell+1)^2`.

The validator constructs the harmonic basis as the nullspace of the Euclidean Laplacian acting from homogeneous degree-`ell` monomials to degree-`ell-2` monomials. No orbital labels are fitted into the rank calculation.

## Verified sampled ranks

```text
ell  continuum dim  rank(H_ell restricted to V_600)
0    1              1
1    4              4
2    9              9
3    16             16
4    25             25
5    36             36
6    49             25
7    64             40
```

Thus the first failure of one-to-one angular sampling occurs at

```text
ell = 6
49 continuum directions -> 25 sampled directions.
```

This independently agrees with the degree-12 failure of the spherical-design quadrature test: products of `ell=6` harmonics can reach degree 12, while the 600-cell is exact only through degree 11 in the tested monomial quadrature.

## Cumulative closure

The cumulative ranks of the sampled spaces `H_0 + ... + H_ell` are

```text
ell  cumulative sampled rank
0    1
1    5
2    14
3    30
4    55
5    91
6    116
7    120
```

Therefore:

```text
L6_SPECTRAL_QUADRATURE_HORIZON = CANDIDATE_VALIDATED_BOUNDARY
L7_FINITE_CLOSURE = CANDIDATE_VALIDATED_FINITE_SAMPLING_CLOSURE
```

The precise statement is finite-dimensional and mathematical:

- through `ell=5`, every hyperspherical-harmonic sector is sampled at full dimension;
- at `ell=6`, rank first collapses;
- adding the sampled `ell=7` sector contributes exactly four new directions beyond `H_0...H_6`;
- those four directions complete the full 120-dimensional function space on the 120 vertices.

This does **not** by itself prove that `6` is a physical event horizon, that `7` is a higher fractal level, or that atomic orbitals are literally 600-cell modes. Those remain candidate interpretations requiring an independent physical map.

## Validator

`TIR/validation/tir_600cell_s3_rank_closure_candidate_v0_2.py`

Expected terminal result:

```text
status = PASS
implementation_status = CANDIDATE
l0_l5_exact_sampling = true
l6_first_rank_collapse = true
l7_new_directions_beyond_l0_l6 = 4
finite_sample_space_closed_by_l7 = true
finite_sample_dimension = 120
```

## Downstream use

This result may be consumed immediately by candidate-labelled PhaseNav/PNCS orbital operators and by candidate spectral/soliton experiments. Receipts must retain `CANDIDATE` provenance until promotion gates are passed.
