#!/usr/bin/env python3
"""Stage 41 — seed-incidence family asymmetry gate.

Pure mathematics on the already frozen ordered seed pairs:
  s1=(3,5), s2=(5,7), s3=(11,13).
No CKM, masses, or fitted coefficients are used.
"""
from __future__ import annotations

import json
import math
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "results"
OUT.mkdir(parents=True, exist_ok=True)

SEEDS = [(3, 5), (5, 7), (11, 13)]
PRIMES = sorted({p for pair in SEEDS for p in pair})


def main() -> None:
    B = np.zeros((3, len(PRIMES)), dtype=float)
    for i, pair in enumerate(SEEDS):
        for p in pair:
            B[i, PRIMES.index(p)] = 1.0

    # Unit-normalized pair-incidence vectors.
    X = B / math.sqrt(2.0)
    G = X @ X.T
    A = G - np.eye(3)

    expected_G = np.array(
        [[1.0, 0.5, 0.0], [0.5, 1.0, 0.0], [0.0, 0.0, 1.0]],
        dtype=float,
    )
    residual = float(np.max(np.abs(G - expected_G)))
    evals, U = np.linalg.eigh(A)

    # The isolated 1-2 block has eigenvectors (s1 +/- s2)/sqrt(2).
    overlap_12 = float(G[0, 1])
    overlap_23 = float(G[1, 2])
    overlap_13 = float(G[0, 2])
    unique_12 = overlap_12 > 0 and overlap_23 == 0.0 and overlap_13 == 0.0

    passed = residual == 0.0 and unique_12
    receipt = {
        "schema": "TIR_POLYGONAL_STAGE41_SEED_INCIDENCE_FAMILY_ASYMMETRY_V0_1",
        "status": "STAGE_41_SEED_INCIDENCE_ASYMMETRY_PASS" if passed else "STAGE_41_FAIL",
        "ordered_seeds": [list(x) for x in SEEDS],
        "prime_basis": PRIMES,
        "incidence_matrix": B.tolist(),
        "normalized_gram": G.tolist(),
        "family_adjacency": A.tolist(),
        "overlap_12": overlap_12,
        "overlap_23": overlap_23,
        "overlap_13": overlap_13,
        "unique_shared_seed_channel": "1<->2" if unique_12 else None,
        "adjacency_eigenvalues": [float(x) for x in evals],
        "expected_12_block_eigenvectors": "(s1+s2)/sqrt(2), (s1-s2)/sqrt(2)",
        "uses_observed_CKM": False,
        "uses_observed_masses": False,
        "uses_fitted_coefficients": False,
        "pass": passed,
    }
    path = OUT / "TIR_POLYGONAL_STAGE41_SEED_INCIDENCE_FAMILY_ASYMMETRY_RECEIPT_V0_1.json"
    path.write_text(json.dumps(receipt, indent=2), encoding="utf-8")
    print(json.dumps(receipt, indent=2))
    if not passed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
