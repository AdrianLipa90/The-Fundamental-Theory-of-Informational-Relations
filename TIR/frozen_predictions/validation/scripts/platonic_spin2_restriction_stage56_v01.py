#!/usr/bin/env python3
"""Stage 56: character restriction of the l=2 SO(3) carrier to A4, S4, A5."""
from __future__ import annotations

from fractions import Fraction
import json

# Exact l=2 character values at the required rotation classes.
CHI = {
    "0": 5,
    "pi": 1,
    "2pi/3": -1,
    "pi/2": -1,
    "2pi/5": 0,
    "4pi/5": 0,
}

GROUPS = {
    "A4": [(1, "0"), (3, "pi"), (8, "2pi/3")],
    "S4_rot": [(1, "0"), (3, "pi"), (6, "pi"), (8, "2pi/3"), (6, "pi/2")],
    "A5": [(1, "0"), (15, "pi"), (20, "2pi/3"), (12, "2pi/5"), (12, "4pi/5")],
}


def char_norm(rows):
    order = sum(size for size, _ in rows)
    return Fraction(sum(size * CHI[angle] ** 2 for size, angle in rows), order)


def trivial_multiplicity(rows):
    order = sum(size for size, _ in rows)
    return Fraction(sum(size * CHI[angle] for size, angle in rows), order)


def main() -> None:
    norms = {name: char_norm(rows) for name, rows in GROUPS.items()}
    trivial = {name: trivial_multiplicity(rows) for name, rows in GROUPS.items()}

    checks = {
        "A4_norm_3": norms["A4"] == 3,
        "S4_norm_2": norms["S4_rot"] == 2,
        "A5_norm_1": norms["A5"] == 1,
        "A5_irreducible": norms["A5"] == 1,
        "A4_no_trivial": trivial["A4"] == 0,
        "S4_no_trivial": trivial["S4_rot"] == 0,
        "A5_no_trivial": trivial["A5"] == 0,
    }

    result = {
        "schema": "TIR_POLYGONAL_STAGE56_PLATONIC_SPIN2_RESTRICTION_V0_1",
        "spin2_character_values": CHI,
        "character_norms": {k: str(v) for k, v in norms.items()},
        "trivial_multiplicities": {k: str(v) for k, v in trivial.items()},
        "decompositions": {
            "A4_complex": "1' + 1'' + 3",
            "A4_real": "2 + 3",
            "S4_rot": "2 + 3",
            "A5": "5 irreducible"
        },
        "checks": checks,
        "pass": all(checks.values()),
        "physical_particle_assignment_claimed": False,
        "CKM_input_used": False,
        "mass_input_used": False
    }
    print(json.dumps(result, indent=2))
    if not result["pass"]:
        raise SystemExit("Stage 56 audit failed")


if __name__ == "__main__":
    main()
