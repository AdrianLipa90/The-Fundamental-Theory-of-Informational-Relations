#!/usr/bin/env python3
from __future__ import annotations

import itertools
import json
from pathlib import Path

import numpy as np

SCHEMA = "TIR_MUMMU_PNCS_HARMONIC_MASK_STELLA_BINDING_NOGO_VALIDATION_V0_1"

CHANNEL_HARMONICS = np.asarray(
    [
        [1,1,0,0], [1,1,0,0], [1,1,0,0],
        [1,0,1,0], [1,0,1,0], [1,0,1,0],
        [1,0,0,1], [1,0,0,1], [1,0,0,1],
        [0,1,1,0], [0,1,1,0], [0,1,1,0],
        [0,1,0,1], [0,1,0,1], [0,1,0,1],
        [0,0,1,1], [0,0,1,1], [0,0,1,1],
        [1,1,1,0], [1,1,1,0], [1,1,1,0],
        [1,1,1,1], [1,1,1,1], [1,1,1,1],
        [1,1,1,1], [1,1,1,1], [1,1,1,1],
        [1,1,1,0], [1,1,1,0], [1,1,1,0],
        [1,1,0,1], [1,1,0,1], [1,1,0,1],
        [1,0,1,1], [1,0,1,1], [1,0,1,1],
    ],
    dtype=np.uint8,
)


def hamming(a, b):
    return int(np.count_nonzero(a != b))


def main():
    checks = []

    unique, counts = np.unique(CHANNEL_HARMONICS, axis=0, return_counts=True)
    multiplicities = sorted(int(x) for x in counts)
    regular = unique[counts == 3]
    exceptional = unique[counts == 6]

    checks.append({
        "name": "source_mask_multiplicity_partition",
        "status": (
            "PASS"
            if unique.shape[0] == 10
            and regular.shape[0] == 8
            and exceptional.shape[0] == 2
            and multiplicities == [3] * 8 + [6] * 2
            else "FAIL"
        ),
        "unique_mask_count": int(unique.shape[0]),
        "regular_count": int(regular.shape[0]),
        "exceptional_count": int(exceptional.shape[0]),
        "multiplicities": multiplicities,
        "regular_masks": ["".join(map(str, row.tolist())) for row in regular],
        "exceptional_masks": ["".join(map(str, row.tolist())) for row in exceptional],
    })

    dist = np.zeros((8, 8), dtype=np.int64)
    for i in range(8):
        for j in range(8):
            dist[i, j] = hamming(regular[i], regular[j])
    degrees = np.sum(dist == 1, axis=1)
    checks.append({
        "name": "regular_mask_hamming_graph_is_not_cube_Q3",
        "status": "PASS" if sorted(degrees.tolist()) != [3] * 8 else "FAIL",
        "degree_sequence_source_order": degrees.tolist(),
        "degree_sequence_sorted": sorted(degrees.tolist()),
        "Q3_degree_sequence": [3] * 8,
    })

    deletion_counts = []
    for drop in range(4):
        projected = {
            tuple(np.delete(row, drop).tolist())
            for row in regular
        }
        deletion_counts.append(len(projected))
    checks.append({
        "name": "no_single_coordinate_deletion_bijects_to_three_bits",
        "status": "PASS" if max(deletion_counts) < 8 else "FAIL",
        "distinct_projected_counts": deletion_counts,
    })

    xor_differences = set()
    for i in range(8):
        for j in range(i + 1, 8):
            xor_differences.add(tuple(np.bitwise_xor(regular[i], regular[j]).tolist()))

    all_nonzero = {
        tuple(int(x) for x in f"{n:04b}")
        for n in range(1, 16)
    }
    missing = sorted(all_nonzero - xor_differences)
    checks.append({
        "name": "regular_pair_differences_exhaust_all_nonzero_F2_4_vectors",
        "status": "PASS" if xor_differences == all_nonzero else "FAIL",
        "difference_count": len(xor_differences),
        "expected_nonzero_vector_count": 15,
        "missing_vectors": ["".join(map(str, x)) for x in missing],
    })

    # Any rank-3 linear quotient F2^4 -> F2^3 has a nonzero one-vector kernel.
    # Since every possible nonzero kernel vector occurs as a regular-pair
    # difference, each quotient must identify at least one regular pair.
    collisions_by_kernel = {}
    for v in sorted(all_nonzero):
        vv = np.asarray(v, dtype=np.uint8)
        pairs = []
        for i in range(8):
            for j in range(i + 1, 8):
                if np.array_equal(np.bitwise_xor(regular[i], regular[j]), vv):
                    pairs.append([i, j])
        collisions_by_kernel["".join(map(str, v))] = pairs

    checks.append({
        "name": "rank3_linear_quotient_injection_is_impossible",
        "status": "PASS" if all(len(v) > 0 for v in collisions_by_kernel.values()) else "FAIL",
        "kernel_collision_witnesses": collisions_by_kernel,
    })

    # Hamming-weight profile also shows the eight classes are not one uniform
    # orbit under the full coordinate-permutation action.
    weights = sorted(int(np.sum(row)) for row in regular)
    checks.append({
        "name": "regular_classes_have_mixed_hamming_weights",
        "status": "PASS" if len(set(weights)) > 1 else "FAIL",
        "hamming_weights_sorted": weights,
    })

    status = "PASS" if all(c["status"] == "PASS" for c in checks) else "FAIL"
    out = {
        "schema": SCHEMA,
        "status": status,
        "claim_scope": (
            "the current PNCS 36-channel harmonic-mask table has an exact "
            "8x3+2x6 multiplicity split, but the eight multiplicity-three classes "
            "do not carry canonical cube/Stella combinatorics under Hamming adjacency, "
            "coordinate deletion, or rank-three linear GF(2) quotient"
        ),
        "checks": checks,
        "summary": {
            "passed": sum(c["status"] == "PASS" for c in checks),
            "total": len(checks),
        },
    }

    Path(__file__).with_name(
        "TIR_MUMMU_PNCS_HARMONIC_MASK_STELLA_BINDING_NOGO_VALIDATION_V0_1.json"
    ).write_text(json.dumps(out, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(out, indent=2, sort_keys=True))
    return 0 if status == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
