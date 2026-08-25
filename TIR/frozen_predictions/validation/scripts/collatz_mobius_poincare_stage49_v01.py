#!/usr/bin/env python3
"""Stage 49: exact Collatz branch words as Möbius / Poincare transformations."""
from __future__ import annotations

from fractions import Fraction
import cmath
import json
import math

WORDS = {
    15: "OEOE",
    35: "",
    143: "OEOEOEOEEEEOEOEEOEOEOEEOEOEOEOEEOEEEOEOEOEEOEOEEOEOEOEOEOEOEEEOEOEOEOEEEEOEEOEEOEEEEOEEEOE",
}
TARGET = 35

E = (Fraction(1, 2), Fraction(0, 1))
O = (Fraction(3, 1), Fraction(1, 1))


def compose(f, g):
    """Return affine composition f o g for tuples (a,b): x -> a*x+b."""
    a, b = f
    c, d = g
    return a * c, a * d + b


def word_affine(word: str):
    total = (Fraction(1, 1), Fraction(0, 1))
    for branch in word:
        total = compose(O if branch == "O" else E, total)
    return total


def cayley(z: complex) -> complex:
    return (z - 1j) / (z + 1j)


def cayley_inv(w: complex) -> complex:
    return 1j * (1 + w) / (1 - w)


def apply_affine_complex(branch: str, z: complex) -> complex:
    return 3 * z + 1 if branch == "O" else z / 2


def disk_branch(branch: str, w: complex) -> complex:
    z = cayley_inv(w)
    return cayley(apply_affine_complex(branch, z))


def main() -> None:
    composites = {}
    for seed, word in WORDS.items():
        a, b = word_affine(word)
        value = a * seed + b
        composites[str(seed)] = {
            "word_length": len(word),
            "odd_count": word.count("O"),
            "even_count": word.count("E"),
            "slope": f"{a.numerator}/{a.denominator}",
            "translation": f"{b.numerator}/{b.denominator}",
            "maps_seed_to": int(value),
        }

    tr_E = 3 / math.sqrt(2)
    tr_O = 4 / math.sqrt(3)

    sample_disk_points = [0j, 0.2 + 0.1j, -0.3 + 0.25j, 0.4 - 0.2j]
    disk_checks = {}
    for branch in ("E", "O"):
        images = [disk_branch(branch, w) for w in sample_disk_points]
        disk_checks[branch] = {
            "max_image_modulus": max(abs(x) for x in images),
            "all_inside_open_disk": all(abs(x) < 1 for x in images),
        }

    checks = {
        "E_trace_hyperbolic": tr_E > 2,
        "O_trace_hyperbolic": tr_O > 2,
        "15_exact_composite": composites["15"]["slope"] == "9/4"
        and composites["15"]["translation"] == "5/4"
        and composites["15"]["maps_seed_to"] == TARGET,
        "35_identity": composites["35"]["slope"] == "1/1"
        and composites["35"]["translation"] == "0/1",
        "143_exact_slope": composites["143"]["slope"] == "16677181699666569/72057594037927936",
        "143_maps_to_35": composites["143"]["maps_seed_to"] == TARGET,
        "disk_preserved_E": disk_checks["E"]["all_inside_open_disk"],
        "disk_preserved_O": disk_checks["O"]["all_inside_open_disk"],
    }

    result = {
        "schema": "TIR_POLYGONAL_STAGE49_COLLATZ_MOBIUS_POINCARE_V0_1",
        "normalized_generator_traces": {"E": tr_E, "O": tr_O},
        "both_generators_hyperbolic": tr_E > 2 and tr_O > 2,
        "word_composites": composites,
        "disk_sample_checks": disk_checks,
        "checks": checks,
        "pass": all(checks.values()),
        "CKM_input_used": False,
        "mass_input_used": False,
        "distance_to_amplitude_rule_used": False,
        "SU3_family_identification_claimed": False,
    }
    print(json.dumps(result, indent=2))
    if not result["pass"]:
        raise SystemExit("Stage 49 audit failed")


if __name__ == "__main__":
    main()
