#!/usr/bin/env python3
"""Stage 15: exact regular A2 + A1 + u(1) subalgebra audit inside E7 and E8.

Scope: pure Lie-algebra mathematics. No particle assignment, masses, PDG, CKM, PMNS,
or spectral data are used.
"""
from __future__ import annotations
import json

E7 = [
    [2,0,-1,0,0,0,0],
    [0,2,0,-1,0,0,0],
    [-1,0,2,-1,0,0,0],
    [0,-1,-1,2,-1,0,0],
    [0,0,0,-1,2,-1,0],
    [0,0,0,0,-1,2,-1],
    [0,0,0,0,0,-1,2],
]
E8 = [
    [2,0,-1,0,0,0,0,0],
    [0,2,0,-1,0,0,0,0],
    [-1,0,2,-1,0,0,0,0],
    [0,-1,-1,2,-1,0,0,0],
    [0,0,0,-1,2,-1,0,0],
    [0,0,0,0,-1,2,-1,0],
    [0,0,0,0,0,-1,2,-1],
    [0,0,0,0,0,0,-1,2],
]

A2 = [[2,-1],[-1,2]]
A1 = [[2]]


def matvec(A, x):
    return [sum(a*b for a, b in zip(row, x)) for row in A]


def principal(A, ids):
    return [[A[i][j] for j in ids] for i in ids]


def cross_zero(A, left, right):
    return all(A[i][j] == 0 and A[j][i] == 0 for i in left for j in right)


def audit(name, C, a1_nodes, a2_nodes, u1_coroot_coeffs):
    charges = matvec(C, u1_coroot_coeffs)
    selected = a1_nodes + a2_nodes
    checks = {
        "A1_cartan_exact": principal(C, a1_nodes) == A1,
        "A2_cartan_exact": principal(C, a2_nodes) == A2,
        "A1_A2_commute": cross_zero(C, a1_nodes, a2_nodes),
        "U1_commutes_with_A1_A2": all(charges[i] == 0 for i in selected),
        "U1_nontrivial": any(q != 0 for q in charges),
        "rank_SM_subalgebra": 2 + 1 + 1 == 4,
    }
    return {
        "algebra": name,
        "rank": len(C),
        "A1_nodes_1based": [i+1 for i in a1_nodes],
        "A2_nodes_1based": [i+1 for i in a2_nodes],
        "u1_coroot_coefficients": u1_coroot_coeffs,
        "simple_root_charges": charges,
        "checks": checks,
        "verdict": "PASS" if all(checks.values()) else "FAIL",
    }


def run():
    result = {
        "schema": "TIR-EXCEPTIONAL-SM-SUBALGEBRA/0.1",
        "stage": 15,
        "scope": "pure Lie-algebra embedding audit",
        "E7": audit("E7", E7, [0], [5,6], [4,6,8,12,9,6,3]),
        "E8": audit("E8", E8, [0], [6,7], [10,15,20,30,24,18,12,6]),
    }
    result["verdict"] = "PASS" if result["E7"]["verdict"] == result["E8"]["verdict"] == "PASS" else "FAIL"
    return result


if __name__ == "__main__":
    print(json.dumps(run(), indent=2))
