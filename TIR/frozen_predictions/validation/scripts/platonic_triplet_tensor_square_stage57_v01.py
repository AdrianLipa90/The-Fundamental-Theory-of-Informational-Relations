#!/usr/bin/env python3
"""Stage 57 — Platonic triplet tensor-square audit.

Computational character-table verification of the tensor-square,
symmetric-square and exterior-square decompositions for the rotational
triplets of A4, S4 and A5. No CKM, mass or fitted inputs are used.
"""
from __future__ import annotations

import cmath
import json
import math
from pathlib import Path

TOL = 1e-12


def inner_product(class_sizes, chi_a, chi_b):
    order = sum(class_sizes)
    return sum(
        n * complex(a).conjugate() * complex(b)
        for n, a, b in zip(class_sizes, chi_a, chi_b)
    ) / order


def decompose(class_sizes, target, irreps):
    out = {}
    residual = 0.0
    for name, chi in irreps.items():
        val = inner_product(class_sizes, chi, target)
        nearest = round(val.real)
        residual = max(residual, abs(val.imag), abs(val.real - nearest))
        if nearest:
            out[name] = int(nearest)
    return out, residual


def sym_wedge(chi, square_class_index):
    sym = []
    wedge = []
    for i, x in enumerate(chi):
        x2 = chi[square_class_index[i]]
        sym.append((x * x + x2) / 2)
        wedge.append((x * x - x2) / 2)
    return sym, wedge


def audit_group(name, class_sizes, triplet, square_class_index, irreps,
                expected_tensor, expected_sym, expected_wedge):
    tensor = [x * x for x in triplet]
    sym, wedge = sym_wedge(triplet, square_class_index)
    tensor_dec, r_t = decompose(class_sizes, tensor, irreps)
    sym_dec, r_s = decompose(class_sizes, sym, irreps)
    wedge_dec, r_w = decompose(class_sizes, wedge, irreps)
    passed = (
        tensor_dec == expected_tensor
        and sym_dec == expected_sym
        and wedge_dec == expected_wedge
        and max(r_t, r_s, r_w) < TOL
    )
    return {
        "group": name,
        "order": sum(class_sizes),
        "tensor_square": tensor_dec,
        "symmetric_square": sym_dec,
        "exterior_square": wedge_dec,
        "max_character_inner_product_integer_residual": max(r_t, r_s, r_w),
        "pass": passed,
    }


def build_receipt():
    omega = cmath.exp(2j * math.pi / 3)

    a4 = audit_group(
        "A4_tetrahedral_rotations",
        [1, 3, 4, 4],
        [3, -1, 0, 0],
        [0, 0, 3, 2],
        {
            "1": [1, 1, 1, 1],
            "1'": [1, 1, omega, omega**2],
            "1''": [1, 1, omega**2, omega],
            "3": [3, -1, 0, 0],
        },
        {"1": 1, "1'": 1, "1''": 1, "3": 2},
        {"1": 1, "1'": 1, "1''": 1, "3": 1},
        {"3": 1},
    )

    s4 = audit_group(
        "S4_octahedral_rotations",
        [1, 6, 3, 8, 6],
        [3, -1, -1, 0, 1],
        [0, 0, 0, 3, 2],
        {
            "1": [1, 1, 1, 1, 1],
            "sgn": [1, -1, 1, 1, -1],
            "2": [2, 0, 2, -1, 0],
            "3": [3, 1, -1, 0, -1],
            "3_rot": [3, -1, -1, 0, 1],
        },
        {"1": 1, "2": 1, "3": 1, "3_rot": 1},
        {"1": 1, "2": 1, "3": 1},
        {"3_rot": 1},
    )

    phi = (1 + math.sqrt(5)) / 2
    phibar = (1 - math.sqrt(5)) / 2
    a5 = audit_group(
        "A5_icosahedral_rotations",
        [1, 15, 20, 12, 12],
        [3, -1, 0, phi, phibar],
        [0, 0, 2, 4, 3],
        {
            "1": [1, 1, 1, 1, 1],
            "3": [3, -1, 0, phi, phibar],
            "3'": [3, -1, 0, phibar, phi],
            "4": [4, 0, 1, -1, -1],
            "5": [5, 1, -1, 0, 0],
        },
        {"1": 1, "3": 1, "5": 1},
        {"1": 1, "5": 1},
        {"3": 1},
    )

    chi3 = [3, -1, 0, phi, phibar]
    chi1 = [1, 1, 1, 1, 1]
    chi5 = [5, 1, -1, 0, 0]
    identity_residual = max(
        abs(chi3[i] * chi3[i] - (chi1[i] + chi3[i] + chi5[i]))
        for i in range(5)
    )

    groups = [a4, s4, a5]
    passed = all(g["pass"] for g in groups) and identity_residual < TOL

    return {
        "schema": "TIR_POLYGONAL_STAGE57_PLATONIC_TRIPLET_TENSOR_SQUARE_RECEIPT_V0_1",
        "status": (
            "STAGE_57_ICOSAHEDRAL_TRIPLET_TENSOR_SQUARE_MATCH_PASS"
            if passed else "STAGE_57_FAIL"
        ),
        "group_audits": groups,
        "a5_direct_character_identity": "chi_3^2 = chi_1 + chi_3 + chi_5",
        "a5_direct_character_identity_max_residual": identity_residual,
        "a5_end0_decomposition": "3 + 5",
        "a5_symmetric_traceless_sector": "5_irreducible",
        "uses_observed_CKM": False,
        "uses_observed_masses": False,
        "uses_fitted_coefficients": False,
        "pass": passed,
    }


def main():
    receipt = build_receipt()
    root = Path(__file__).resolve().parents[1]
    out = root / "results"
    out.mkdir(parents=True, exist_ok=True)
    path = out / "TIR_POLYGONAL_STAGE57_PLATONIC_TRIPLET_TENSOR_SQUARE_RECEIPT_V0_1.json"
    path.write_text(json.dumps(receipt, indent=2), encoding="utf-8")
    print(json.dumps(receipt, indent=2))
    if not receipt["pass"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
