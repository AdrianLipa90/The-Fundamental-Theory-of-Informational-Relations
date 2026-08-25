#!/usr/bin/env python3
"""Stage 21: exact threefold one-generation hypercharge carrier inside (16,3)."""
from fractions import Fraction
from collections import Counter
import json


def fs(x):
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


def run():
    one_family = Counter({
        Fraction(1,6): 6,
        Fraction(-2,3): 3,
        Fraction(1,1): 1,
        Fraction(1,3): 3,
        Fraction(-1,2): 2,
        Fraction(0,1): 1,
    })
    threefold = Counter({y: 3*m for y,m in one_family.items()})

    YQ=Fraction(1,6); Yu=Fraction(-2,3); Yd=Fraction(1,3); YL=Fraction(-1,2); Ye=Fraction(1,1)
    per_family = {
        "SU3^2_U1": 2*YQ + Yu + Yd,
        "SU2^2_U1": 3*YQ + YL,
        "gravity^2_U1": 6*YQ + 3*Yu + 3*Yd + 2*YL + Ye,
        "U1^3": 6*YQ**3 + 3*Yu**3 + 3*Yd**3 + 2*YL**3 + Ye**3,
    }
    total = {k: 3*v for k,v in per_family.items()}

    state_count = sum(threefold.values())
    traceY = sum(y*m for y,m in threefold.items())

    checks = {
        "E8_16_triplet_dimension_48": state_count == 48,
        "three_exact_copies": all(threefold[y] == 3*one_family[y] for y in one_family),
        "threefold_trace_Y_zero": traceY == 0,
        "per_copy_anomalies_zero": all(v == 0 for v in per_family.values()),
        "threefold_anomalies_zero": all(v == 0 for v in total.values()),
    }

    return {
        "schema": "TIR-E8-THREEFOLD-SM-CARRIER/0.1",
        "stage": 21,
        "carrier": "(16,3) subset of (27,3) under E8 -> E6 x SU3",
        "one_copy_hypercharge_multiplicities": {fs(k):v for k,v in sorted(one_family.items())},
        "threefold_hypercharge_multiplicities": {fs(k):v for k,v in sorted(threefold.items())},
        "total_state_count": state_count,
        "trace_Y": fs(traceY),
        "per_copy_anomaly_residuals": {k:fs(v) for k,v in per_family.items()},
        "threefold_anomaly_residuals": {k:fs(v) for k,v in total.items()},
        "checks": checks,
        "verdict": "PASS" if all(checks.values()) else "FAIL",
        "TIR_seed_to_SU3_weight_map": "OPEN_BIJECTION_GATE"
    }


if __name__ == "__main__":
    print(json.dumps(run(), indent=2, sort_keys=True))
