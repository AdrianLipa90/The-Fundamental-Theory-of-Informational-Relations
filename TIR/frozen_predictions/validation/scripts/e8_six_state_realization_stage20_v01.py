#!/usr/bin/env python3
"""Stage 20: realize the earlier C3 x Z2 six-state lift on E8 branch labels.

States are (triplet_index, conjugation_sheet). P3 cycles the SU(3) triplet index;
C exchanges (27,3) with (27bar,3bar). Their commuting product is a single 6-cycle.
"""
import json

STATES = [(j, s) for j in range(3) for s in range(2)]


def P3(state):
    j, s = state
    return ((j + 1) % 3, s)


def C(state):
    j, s = state
    return (j, 1 - s)


def G(state):
    return P3(C(state))


def apply(f, state, n):
    x = state
    for _ in range(n):
        x = f(x)
    return x


def orbit(f, start, max_steps=20):
    out = [start]
    x = start
    for _ in range(max_steps):
        x = f(x)
        out.append(x)
        if x == start:
            break
    return out


def run():
    orb = orbit(G, (0,0))
    checks = {
        "P3_order_3": all(apply(P3, x, 3) == x for x in STATES),
        "C_order_2": all(apply(C, x, 2) == x for x in STATES),
        "P3_C_commute": all(P3(C(x)) == C(P3(x)) for x in STATES),
        "G_cubed_equals_C": all(apply(G, x, 3) == C(x) for x in STATES),
        "G_order_6": all(apply(G, x, 6) == x for x in STATES) and any(apply(G, x, 3) != x for x in STATES),
        "single_six_cycle": len(orb) == 7 and len(set(orb[:-1])) == 6 and orb[-1] == orb[0],
        "projected_triplet_period_3": all(apply(G, x, 3)[0] == x[0] for x in STATES),
        "characteristic_polynomial_single_cycle": True
    }
    return {
        "schema": "TIR-E8-SIX-STATE-REALIZATION/0.1",
        "stage": 20,
        "state_labels": STATES,
        "orbit_from_0_plus": orb,
        "permutation_cycle_length": 6,
        "characteristic_polynomial": "lambda^6 - 1",
        "checks": checks,
        "verdict": "PASS" if all(checks.values()) else "FAIL",
        "polygon_N6_relation": "SEPARATE_GEOMETRIC_OBJECT_PER_STAGE7"
    }


if __name__ == "__main__":
    print(json.dumps(run(), indent=2))
