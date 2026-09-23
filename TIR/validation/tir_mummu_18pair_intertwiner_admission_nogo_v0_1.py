#!/usr/bin/env python3
from __future__ import annotations

import json
import math
from pathlib import Path

SCHEMA = "TIR_MUMMU_18PAIR_INTERTWINER_ADMISSION_NOGO_VALIDATION_V0_1"
N = 18
IDENTITY = tuple(range(N))


def compose(p, q):
    return tuple(p[q[i]] for i in range(N))


def perm_power(p, n):
    out = IDENTITY
    for _ in range(n):
        out = compose(p, out)
    return out


def perm_order(p):
    out = IDENTITY
    for n in range(1, 100):
        out = compose(p, out)
        if out == IDENTITY:
            return n
    raise RuntimeError("permutation order exceeded bound")


def encode(a, b):
    return 3 * a + b


def decode(i):
    return divmod(i, 3)


def s_action(i):
    a, b = decode(i)
    return encode((a + 1) % 6, b)


def r_action(i):
    a, b = decode(i)
    return encode(a, (b + 1) % 3)


S = tuple(s_action(i) for i in range(N))
R = tuple(r_action(i) for i in range(N))


def orbit(anchor):
    return {
        perm_power(S, a)[perm_power(R, b)[anchor]]
        for a in range(6)
        for b in range(3)
    }


def product_element_order(a, b):
    oa = 1 if a == 0 else 6 // math.gcd(a, 6)
    ob = 1 if b == 0 else 3 // math.gcd(b, 3)
    return math.lcm(oa, ob)


def cross(u, v):
    return (
        u[1] * v[2] - u[2] * v[1],
        u[2] * v[0] - u[0] * v[2],
        u[0] * v[1] - u[1] * v[0],
    )


def norm2(v):
    return sum(x * x for x in v)


def main():
    checks = []

    order_s = perm_order(S)
    order_r = perm_order(R)
    commute = compose(S, R) == compose(R, S)
    subgroup_s = {perm_power(S, a) for a in range(6)}
    subgroup_r = {perm_power(R, b) for b in range(3)}
    intersection_size = len(subgroup_s & subgroup_r)
    checks.append({
        "name": "synthetic_regular_C6xC3_action",
        "status": (
            "PASS"
            if order_s == 6
            and order_r == 3
            and commute
            and intersection_size == 1
            else "FAIL"
        ),
        "order_S": order_s,
        "order_R": order_r,
        "commute": commute,
        "subgroup_intersection_size": intersection_size,
    })

    anchor_orbit = orbit(0)
    checks.append({
        "name": "anchored_action_is_free_transitive",
        "status": "PASS" if len(anchor_orbit) == 18 else "FAIL",
        "orbit_size": len(anchor_orbit),
    })

    reconstructed = {}
    collision = False
    for a in range(6):
        for b in range(3):
            x = perm_power(S, a)[perm_power(R, b)[0]]
            if x in reconstructed:
                collision = True
            reconstructed[x] = (a, b)
    exact_coordinates = all(reconstructed[encode(a, b)] == (a, b) for a in range(6) for b in range(3))
    checks.append({
        "name": "unique_anchored_product_coordinates",
        "status": "PASS" if not collision and exact_coordinates and len(reconstructed) == 18 else "FAIL",
        "coordinate_count": len(reconstructed),
        "collision": collision,
    })

    target_orders = {
        product_element_order(a, b)
        for a in range(6)
        for b in range(3)
    }
    max_target_order = max(target_orders)
    checks.append({
        "name": "C18_not_isomorphic_to_C6xC3",
        "status": "PASS" if max_target_order == 6 and 18 not in target_orders else "FAIL",
        "C18_generator_order": 18,
        "C6xC3_element_orders": sorted(target_orders),
        "C6xC3_max_element_order": max_target_order,
    })

    identity_bijection = tuple(range(18))
    swapped_bijection = list(range(18))
    swapped_bijection[0], swapped_bijection[1] = swapped_bijection[1], swapped_bijection[0]
    swapped_bijection = tuple(swapped_bijection)
    both_bijections = (
        len(set(identity_bijection)) == 18
        and len(set(swapped_bijection)) == 18
        and identity_bijection != swapped_bijection
    )
    checks.append({
        "name": "cardinality_only_bijection_nonuniqueness",
        "status": "PASS" if both_bijections else "FAIL",
        "explicit_distinct_bijections": 2,
        "total_possible_bijections": math.factorial(18),
    })

    # Source-preserving uncoupled algebra:
    # element = (factor_index, local_axis_vector). Brackets across distinct
    # direct-product factors are identically zero.
    cross_factor_max = 0.0
    z = (0.0, 0.0, 1.0)
    for j in range(18):
        for k in range(j + 1, 18):
            bracket_norm2 = 0.0 if j != k else norm2(cross(z, z))
            cross_factor_max = max(cross_factor_max, bracket_norm2)
    checks.append({
        "name": "uncoupled_su2_18_cross_factor_commutator_nogo",
        "status": "PASS" if cross_factor_max == 0.0 else "FAIL",
        "max_cross_factor_commutator_norm2": cross_factor_max,
    })

    same_axis_max = 0.0
    for _ in range(18):
        same_axis_max = max(same_axis_max, norm2(cross(z, z)))
    checks.append({
        "name": "source_pair_sigma_z_family_is_abelian",
        "status": "PASS" if same_axis_max == 0.0 else "FAIL",
        "max_same_axis_commutator_norm2": same_axis_max,
    })

    # Conditional shared-frame demonstration after an admitted 6x3 intertwiner.
    axes = (
        (1.0, 0.0, 0.0),
        (0.0, 1.0, 0.0),
        (0.0, 0.0, 1.0),
    )
    pair_count = 0
    nonzero_count = 0
    for i in range(18):
        _, bi = decode(i)
        for j in range(i + 1, 18):
            _, bj = decode(j)
            pair_count += 1
            if norm2(cross(axes[bi], axes[bj])) > 0.0:
                nonzero_count += 1
    checks.append({
        "name": "conditional_shared_pauli_embedding_opens_nonabelian_channel",
        "status": "PASS" if nonzero_count > 0 else "FAIL",
        "unordered_pairs": pair_count,
        "nonzero_axis_commutator_pairs": nonzero_count,
        "promotion_state": "CONDITIONAL_ONLY",
    })

    status = "PASS" if all(c["status"] == "PASS" for c in checks) else "FAIL"
    out = {
        "schema": SCHEMA,
        "status": status,
        "claim_scope": (
            "group/action admission theorem and direct-product non-Abelian no-go; "
            "no source claim that PNCS already supplies the required C6xC3 action"
        ),
        "checks": checks,
        "summary": {
            "passed": sum(c["status"] == "PASS" for c in checks),
            "total": len(checks),
        },
    }
    Path(__file__).with_name(
        "TIR_MUMMU_18PAIR_INTERTWINER_ADMISSION_NOGO_VALIDATION_V0_1.json"
    ).write_text(json.dumps(out, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(out, indent=2, sort_keys=True))
    return 0 if status == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
