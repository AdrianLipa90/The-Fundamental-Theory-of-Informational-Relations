#!/usr/bin/env python3
"""Deterministic structural audit for the TIR zero-axiom relational foundation.

This validator checks the finite identities attached to the current canonical
foundation. It does not claim that executable checks prove the metalogical
or physical universality of the foundation.
"""
from __future__ import annotations

import json
import math
from fractions import Fraction


def relational_minimum() -> dict[str, object]:
    poles = ("N", "S")
    exchange = {"N": "S", "S": "N"}
    orbit = []
    x = "N"
    for _ in range(4):
        if x not in orbit:
            orbit.append(x)
        x = exchange[x]
    return {
        "primitive_object": "RELATION",
        "pole_roles": list(poles),
        "exchange_squared_identity": all(exchange[exchange[k]] == k for k in exchange),
        "exchange_orbit": orbit,
        "pass": set(orbit) == set(poles) and len(orbit) == 2,
    }


def relational_zero() -> dict[str, object]:
    values = (-3, -1, 0, 1, 3)
    residuals = [x - x for x in values]
    return {
        "typing": "0 is a null value of a relation/measure, not ontic nothing",
        "sample_self_differences": residuals,
        "pass": all(v == 0 for v in residuals),
    }


def half_and_ln2() -> dict[str, object]:
    w_n = Fraction(1, 2)
    w_s = Fraction(1, 2)
    h = -sum(float(w) * math.log(float(w)) for w in (w_n, w_s))
    return {
        "weights": [[w_n.numerator, w_n.denominator], [w_s.numerator, w_s.denominator]],
        "exchange_invariant": w_n == w_s,
        "normalized": w_n + w_s == 1,
        "entropy": h,
        "ln2": math.log(2.0),
        "pass": w_n == w_s and w_n + w_s == 1 and math.isclose(h, math.log(2.0), rel_tol=0.0, abs_tol=1e-15),
    }


def bloch_sphere_samples() -> dict[str, object]:
    rows = []
    passed = True
    for u, phi in ((0.0, 0.0), (0.5, 0.0), (0.5, math.pi / 2), (1.0, 0.0), (0.25, math.pi / 3)):
        r = (
            2.0 * math.sqrt(u * (1.0 - u)) * math.cos(phi),
            2.0 * math.sqrt(u * (1.0 - u)) * math.sin(phi),
            1.0 - 2.0 * u,
        )
        norm2 = sum(x * x for x in r)
        row_pass = math.isclose(norm2, 1.0, rel_tol=0.0, abs_tol=1e-14)
        passed &= row_pass
        rows.append({"u": u, "phi": phi, "r": list(r), "norm2": norm2, "pass": row_pass})
    return {"identity": "CP1 ~= S2 via the standard pure-qubit Bloch map", "rows": rows, "pass": passed}


def build_receipt() -> dict[str, object]:
    blocks = {
        "relational_minimum_finite_certificate": relational_minimum(),
        "relational_zero_typing_certificate": relational_zero(),
        "half_ln2_certificate": half_and_ln2(),
        "bloch_sphere_certificate": bloch_sphere_samples(),
    }
    passed = all(block["pass"] for block in blocks.values())
    return {
        "schema": "TIR_ZERO_AXIOM_RELATIONAL_FOUNDATION_V0_1",
        "canonical_nonlogical_axiom_count": 0,
        "primitive_content": "RELATION",
        "ontic_zero_object": False,
        "zero_typing": "RELATIONAL_NULLITY_ONLY",
        "dependency_spine": ["RELATION", "POLE_PAIR", "HALF_SEAM", "LN2", "C2", "CP1_S2", "TIR"],
        "claim_boundary": {
            "zero_axiom_status": "canonical TIR foundation declaration",
            "metalogical_universality": "requires independent formal audit; not established by this executable certificate",
            "physical_identification": "requires downstream empirical/physical binding",
            "finite_identities": "checked here",
        },
        "blocks": blocks,
        "technical_status": "PASS" if passed else "FAIL",
    }


def main() -> None:
    receipt = build_receipt()
    print(json.dumps(receipt, indent=2, sort_keys=True))
    if receipt["technical_status"] != "PASS":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
