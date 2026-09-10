#!/usr/bin/env python3
"""Exact validator for TIR Platonic L-constant closure v0.1.

This validator proves only the finite/combinatorial statements encoded here.
It does not establish a physical interpretation of the L-constants.
"""

from __future__ import annotations

import json
from fractions import Fraction
from itertools import permutations


def parity(perm: tuple[int, ...]) -> int:
    inversions = sum(
        perm[i] > perm[j]
        for i in range(len(perm))
        for j in range(i + 1, len(perm))
    )
    return inversions % 2


def compose(a: tuple[int, ...], b: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(a[b[i]] for i in range(len(a)))


def left_cosets(
    group: set[tuple[int, ...]],
    subgroup: set[tuple[int, ...]],
) -> list[set[tuple[int, ...]]]:
    unseen = set(group)
    cosets: list[set[tuple[int, ...]]] = []
    while unseen:
        g = next(iter(unseen))
        coset = {compose(g, h) for h in subgroup}
        cosets.append(coset)
        unseen -= coset
    return cosets


def collatz_depth_to_one(n: int) -> int:
    depth = 0
    while n != 1:
        n = 3 * n + 1 if n % 2 else n // 2
        depth += 1
        if depth > 1000:
            raise RuntimeError("unexpected Collatz depth overflow")
    return depth


def rotational_triangle_group_order(q: int) -> int:
    # Orientation-preserving spherical triangle group (2,3,q):
    # |G_q| = 2 / (1/2 + 1/3 + 1/q - 1).
    excess = Fraction(1, 2) + Fraction(1, 3) + Fraction(1, q) - 1
    order = Fraction(2, 1) / excess
    if order.denominator != 1:
        raise AssertionError(f"non-integral order for q={q}: {order}")
    return order.numerator


def main() -> int:
    platonic_pairs = [
        (p, q)
        for p in range(3, 101)
        for q in range(3, 101)
        if Fraction(1, p) + Fraction(1, q) > Fraction(1, 2)
    ]
    expected_pairs = [(3, 3), (3, 4), (3, 5), (4, 3), (5, 3)]
    assert platonic_pairs == expected_pairs

    triangular_q = [q for p, q in platonic_pairs if p == 3]
    assert triangular_q == [3, 4, 5]

    s4 = set(permutations(range(4)))
    a4 = {p for p in s4 if parity(p) == 0}
    a5 = {p for p in permutations(range(5)) if parity(p) == 0}
    a4_in_a5 = {p + (4,) for p in a4}

    assert len(a4) == 12
    assert len(s4) == 24
    assert len(a5) == 60
    assert a4_in_a5 <= a5

    s4_cosets = left_cosets(s4, a4)
    a5_cosets = left_cosets(a5, a4_in_a5)

    l4 = len(s4_cosets)
    l5 = len(a5_cosets)

    # TIR root-extension closure rule:
    # the tetrahedral root carrier is the disjoint union of the two
    # non-self-dual Platonic extension coset spaces.
    l3 = l4 + l5

    assert (l3, l4, l5) == (7, 2, 5)

    triangle_orders = {q: rotational_triangle_group_order(q) for q in triangular_q}
    assert triangle_orders == {3: 12, 4: 24, 5: 60}
    assert triangle_orders[4] // triangle_orders[3] == l4
    assert triangle_orders[5] // triangle_orders[3] == l5

    # Independent arithmetic/provenance crosschecks already present in TIR.
    assert collatz_depth_to_one(3) == l3
    assert 5 - 3 == l4
    assert 5 == l5

    # 3-4-5 / symmetry-order crosschecks. These are checks, not derivation steps.
    assert 3**2 + 4**2 == 5**2
    assert 3 + 4 + 5 == len(a4)
    assert 2 * (3 + 4 + 5) == len(s4)
    assert 3 * 4 * 5 == len(a5)

    result = {
        "schema": "TIR_PLATONIC_L_CONSTANTS_VALIDATION_V0_1",
        "status": "PASS",
        "claim_scope": "EXACT_INTERNAL_STRUCTURAL_DERIVATION_CONDITIONAL_ON_TIR_ROOT_EXTENSION_CLOSURE_RULE",
        "platonic_schlafli_pairs": [list(x) for x in platonic_pairs],
        "triangular_branch_q": triangular_q,
        "group_orders": {"A4": len(a4), "S4": len(s4), "A5": len(a5)},
        "subgroup_indices": {
            "[S4:A4]": l4,
            "[A5:A4]": l5,
        },
        "L": {"L3": l3, "L4": l4, "L5": l5},
        "independent_crosschecks": {
            "collatz_depth_3": collatz_depth_to_one(3),
            "twin_prime_gap_3_5": 5 - 3,
            "upper_twin_prime": 5,
            "pythagorean_3_4_5": True,
        },
        "physical_claim": False,
    }
    print(json.dumps(result, sort_keys=True, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
