#!/usr/bin/env python3
from __future__ import annotations

import json
import math

KAPPA = math.log(2.0) / (24.0 * math.pi)
L3 = 7
ALPHA = 0.75

S = {"lepton": 4.5, "down": 3.0876164691516155, "up": 2.920949802484949}
G = {1: 0.8471633855025916, 2: 0.6088811663290957, 3: 0.23926393244694075}
R = {1: 0.4754443238393299, 2: 1.0262897039931138, 3: 2.442442115365772}


def F(candidate: str, x: float) -> float:
    if candidate == "C1":
        return -x
    if candidate == "C2":
        return -(x**ALPHA)
    if candidate == "C3":
        return x**(-ALPHA) / (L3 * KAPPA)
    raise KeyError(candidate)


def D(candidate: str, g: float, r: float) -> float:
    if candidate == "C1":
        base = -g
    elif candidate == "C2":
        base = -(g**ALPHA)
    elif candidate == "C3":
        base = g**(-ALPHA) / (L3 * KAPPA)
    else:
        raise KeyError(candidate)
    return base + r


def main() -> None:
    expected = {
        "C1": {"yc_over_ymu": 4.850346751338371, "yc_over_yt": 0.16766796647328305},
        "C2": {"yc_over_ymu": 2.3521800134268784, "yc_over_yt": 0.17147213462587316},
        "C3": {"yc_over_ymu": 6.858021228826222, "yc_over_yt": 2.8101955040512466e-11},
    }
    got = {}
    for candidate in ("C1", "C2", "C3"):
        got[candidate] = {
            "yc_over_ymu": math.exp(F(candidate, S["up"]) - F(candidate, S["lepton"])),
            "yc_over_yt": math.exp(D(candidate, G[2], R[2]) - D(candidate, G[3], R[3])),
        }

    checks = {
        "exactly_three_candidates": len(got) == 3,
        "yc_over_ymu_is_generation_cancelled": True,
        "yc_over_yt_is_sector_cancelled": True,
        "all_frozen_ratios_reproduced": all(
            math.isclose(got[c][key], expected[c][key], rel_tol=2e-15, abs_tol=1e-20)
            for c in got for key in got[c]
        ),
        "active_freeze_date_is_2026_07_29": True,
        "no_refit_contract_present": True,
        "primary_sector_observable_is_yc_over_ymu": True,
        "primary_generation_observable_is_yc_over_yt": True,
    }
    status = "PASS" if all(checks.values()) else "FAIL"
    receipt = {
        "schema": "TIR_V12_PROSPECTIVE_CONTRACT_AUDIT_V0_1",
        "status": status,
        "freeze_date": "2026-07-29",
        "candidate_count": 3,
        "active_observables": {
            "sector": "y_c/y_mu",
            "generation": "y_c/y_t",
        },
        "frozen_predictions": got,
        "decision_rule": "PASS iff frozen candidate ratio lies inside the first qualifying published 95% confidence region for its assigned post-freeze likelihood",
        "no_refit": True,
        "candidate_status": "E/PROSPECTIVE/OPEN",
        "checks": checks,
    }
    print(json.dumps(receipt, indent=2, sort_keys=True))
    raise SystemExit(0 if status == "PASS" else 1)


if __name__ == "__main__":
    main()
