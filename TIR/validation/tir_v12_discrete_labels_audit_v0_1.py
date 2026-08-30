from __future__ import annotations

import itertools
import json

SCHEMA = "TIR_V12_DISCRETE_LABELS_AUDIT_V0_1"


def collatz_step(n: int) -> int:
    if not isinstance(n, int) or isinstance(n, bool) or n <= 0:
        raise ValueError("n must be a positive integer")
    return 3 * n + 1 if n % 2 else n // 2


def finite_orbit_to_one(seed: int, max_steps: int = 1000) -> tuple[int, ...]:
    n = seed
    orbit = [n]
    for _ in range(max_steps):
        if n == 1:
            return tuple(orbit)
        n = collatz_step(n)
        orbit.append(n)
    raise RuntimeError("declared finite verification budget exhausted")


def assignment_survivors() -> tuple[list[dict[str, int]], list[dict[str, int]]]:
    slots = ("u", "d", "s", "c", "b", "t")
    primes = (3, 5, 7, 11, 13, 17)
    arithmetic_survivors: list[dict[str, int]] = []
    ordered_survivors: list[dict[str, int]] = []
    for perm in itertools.permutations(primes):
        q = dict(zip(slots, perm))
        arithmetic_ok = (
            q["d"] - q["u"] == 2
            and q["s"] == 7
            and abs(q["s"] - q["c"]) == 4
            and abs(q["b"] - q["t"]) == 4
        )
        if arithmetic_ok:
            arithmetic_survivors.append(q)
        typed_order_ok = tuple(q[name] for name in slots) == primes
        if arithmetic_ok and typed_order_ok:
            ordered_survivors.append(q)
    return arithmetic_survivors, ordered_survivors


def main() -> int:
    expected_orbit = (3, 10, 5, 16, 8, 4, 2, 1)
    orbit = finite_orbit_to_one(3)
    arithmetic, ordered = assignment_survivors()
    canonical = {"u": 3, "d": 5, "s": 7, "c": 11, "b": 13, "t": 17}
    swapped_heavy = {"u": 3, "d": 5, "s": 7, "c": 11, "b": 17, "t": 13}
    checks = {
        "finite_orbit_3_exact": orbit == expected_orbit,
        "L3_depth_is_7": len(orbit) - 1 == 7,
        "candidate_space_is_6_factorial": len(tuple(itertools.permutations((3, 5, 7, 11, 13, 17)))) == 720,
        "arithmetic_constraints_leave_two": len(arithmetic) == 2,
        "heavy_pair_swap_is_only_residual": arithmetic == [canonical, swapped_heavy],
        "typed_order_rule_is_unique": ordered == [canonical],
    }
    receipt = {
        "schema": SCHEMA,
        "checks": checks,
        "collatz_orbit_3": list(orbit),
        "L3": len(orbit) - 1,
        "prime_candidate_set": [3, 5, 7, 11, 13, 17],
        "permutations_checked": 720,
        "arithmetic_survivor_count": len(arithmetic),
        "arithmetic_survivors": arithmetic,
        "typed_order_survivor_count": len(ordered),
        "typed_order_survivors": ordered,
        "global_collatz_conjecture_used": False,
        "quark_prime_uniqueness_status": "UNIQUE_ONLY_AFTER_EXPLICIT_TYPED_ORDER_RULE",
        "status": "PASS" if all(checks.values()) else "FAIL",
    }
    print(json.dumps(receipt, indent=2, sort_keys=True))
    return 0 if receipt["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
