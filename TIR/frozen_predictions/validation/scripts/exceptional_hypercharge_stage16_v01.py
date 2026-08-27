#!/usr/bin/env python3
"""Stage 16: exact SU(5) hypercharge weight audit along the E7/E8 -> E6 -> SO(10) -> SU(5) chain.

Pure representation arithmetic. No masses or experimental inputs.
"""
from fractions import Fraction
from collections import Counter
import json


def fstr(x: Fraction) -> str:
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


def run():
    # Traceless SU(5) hypercharge direction on the fundamental 5.
    y5 = [Fraction(-1,3)] * 3 + [Fraction(1,2)] * 2

    # 10 = wedge^2 5: weights are pairwise sums.
    y10 = []
    for i in range(5):
        for j in range(i+1, 5):
            y10.append(y5[i] + y5[j])

    # bar5 carries opposite fundamental weights.
    ybar5 = [-y for y in y5]

    c10 = Counter(y10)
    cb5 = Counter(ybar5)

    expected10 = Counter({Fraction(1,6): 6, Fraction(-2,3): 3, Fraction(1,1): 1})
    expectedb5 = Counter({Fraction(1,3): 3, Fraction(-1,2): 2})

    YQ = Fraction(1,6)
    Yu = Fraction(-2,3)
    Yd = Fraction(1,3)
    YL = Fraction(-1,2)
    Ye = Fraction(1,1)

    anomaly = {
        "SU3^2_U1": 2*YQ + Yu + Yd,
        "SU2^2_U1": 3*YQ + YL,
        "gravity^2_U1": 6*YQ + 3*Yu + 3*Yd + 2*YL + Ye,
        "U1^3": 6*YQ**3 + 3*Yu**3 + 3*Yd**3 + 2*YL**3 + Ye**3,
    }

    branch_dimension_checks = {
        "E7_adjoint_to_E6_U1": 78 + 27 + 27 + 1 == 133,
        "E8_adjoint_to_E6_SU3": 78 + 8 + 3*27 + 3*27 == 248,
        "E6_27_to_SO10": 16 + 10 + 1 == 27,
        "SO10_16_to_SU5": 10 + 5 + 1 == 16,
        "SU5_family_state_count": 10 + 5 + 1 == 16,
    }

    checks = {
        "Y5_traceless": sum(y5) == 0,
        "10_weights_match_TIR_v3_8": c10 == expected10,
        "bar5_weights_match_TIR_v3_8": cb5 == expectedb5,
        "anomalies_zero": all(v == 0 for v in anomaly.values()),
        "branch_dimensions_close": all(branch_dimension_checks.values()),
    }

    return {
        "schema": "TIR-EXCEPTIONAL-HYPERCHARGE/0.1",
        "stage": 16,
        "Y5_fundamental": [fstr(x) for x in y5],
        "SU5_10_hypercharge_multiplicities": {fstr(k): v for k,v in sorted(c10.items())},
        "SU5_bar5_hypercharge_multiplicities": {fstr(k): v for k,v in sorted(cb5.items())},
        "singlet_hypercharge": "0",
        "TIR_v3_8_identification_pattern": {
            "Q": {"Y": "1/6", "multiplicity": 6},
            "u_c": {"Y": "-2/3", "multiplicity": 3},
            "e_c": {"Y": "1", "multiplicity": 1},
            "d_c": {"Y": "1/3", "multiplicity": 3},
            "L": {"Y": "-1/2", "multiplicity": 2},
            "nu_c": {"Y": "0", "multiplicity": 1}
        },
        "anomaly_residuals": {k: fstr(v) for k,v in anomaly.items()},
        "branch_dimension_checks": branch_dimension_checks,
        "checks": checks,
        "verdict": "PASS" if all(checks.values()) else "FAIL",
    }


if __name__ == "__main__":
    print(json.dumps(run(), indent=2, sort_keys=True))
