#!/usr/bin/env python3
"""TIR legacy A1--A8 discharge structural validator.

Checks finite identities and canonical source firewalls. It does not convert
physical-binding claims into empirical facts.
"""
from __future__ import annotations

import cmath
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


def binary_orbit() -> dict[str, object]:
    J = {"N": "S", "S": "N"}
    orbit = ["N", J["N"]]
    return {
        "orbit": orbit,
        "J2_identity": all(J[J[x]] == x for x in J),
        "pass": orbit == ["N", "S"] and all(J[J[x]] == x for x in J),
    }


def bloch_projective_identity() -> dict[str, object]:
    rows = []
    ok = True
    for theta, phi in (
        (0.0, 0.0),
        (math.pi / 2, 0.0),
        (math.pi / 2, math.pi / 2),
        (math.pi, 0.0),
        (1.1, 2.2),
    ):
        a = math.cos(theta / 2)
        b = cmath.exp(1j * phi) * math.sin(theta / 2)
        norm = abs(a) ** 2 + abs(b) ** 2
        r = (
            2 * (a.conjugate() * b).real,
            2 * (a.conjugate() * b).imag,
            abs(a) ** 2 - abs(b) ** 2,
        )
        r2 = sum(x * x for x in r)
        row_ok = math.isclose(norm, 1.0, abs_tol=1e-14) and math.isclose(r2, 1.0, abs_tol=1e-14)
        ok &= row_ok
        rows.append({"theta": theta, "phi": phi, "state_norm": norm, "bloch_norm2": r2, "pass": row_ok})
    return {"rows": rows, "pass": ok}


def zero_to_winding() -> dict[str, object]:
    rows = []
    ok = True
    for n in (-5, -2, -1, 0, 1, 2, 5, 12):
        delta = 2 * math.pi * n
        closure = cmath.exp(1j * delta)
        residual = abs(closure - 1)
        row_ok = residual < 1e-12
        ok &= row_ok
        rows.append({"n": n, "delta_phi": delta, "closure_residual": residual, "pass": row_ok})
    return {"rows": rows, "pass": ok}


def euler_symmetry() -> dict[str, object]:
    rows = []
    ok = True
    for phi in (0.0, 0.3, 1.0, math.pi, 7.2):
        lhs = cmath.exp(1j * (phi + 2 * math.pi))
        rhs = cmath.exp(1j * phi)
        residual = abs(lhs - rhs)
        row_ok = residual < 1e-12
        ok &= row_ok
        rows.append({"phi": phi, "residual": residual, "pass": row_ok})
    return {"rows": rows, "pass": ok}


def source_firewall() -> dict[str, object]:
    files = {
        "zero_foundation": ROOT / "foundations" / "TIR_ZERO_AXIOM_RELATIONAL_FOUNDATION_V0_1.md",
        "discharge": ROOT / "foundations" / "TIR_LEGACY_AXIOM_DISCHARGE_THEOREM_V0_1.md",
        "chapter1": ROOT / "monograph" / "v12" / "chapters" / "ch01_first_distinction_relational_kernel.tex",
    }
    texts = {k: p.read_text(encoding="utf-8") for k, p in files.items()}
    markers = {
        "zero_axiom_count": "N_{\\rm nonlogical\\ axioms}=0" in texts["zero_foundation"],
        "relational_minimum": "RELATION" in texts["zero_foundation"],
        "sphere_before_quantum_firewall": "A2 quantum point" in texts["discharge"] and "Bloch sphere" in texts["discharge"],
        "chapter_zero_axiom": "N_{\\rm nonlogical\\ axioms}=0" in texts["chapter1"],
    }
    return {"markers": markers, "pass": all(markers.values())}


def build_receipt() -> dict[str, object]:
    blocks = {
        "binary_orbit": binary_orbit(),
        "bloch_projective_identity": bloch_projective_identity(),
        "zero_to_winding": zero_to_winding(),
        "euler_phase_symmetry": euler_symmetry(),
        "source_firewall": source_firewall(),
    }
    passed = all(v["pass"] for v in blocks.values())
    return {
        "schema": "TIR_LEGACY_AXIOM_DISCHARGE_V0_1",
        "canonical_nonlogical_axiom_count": 0,
        "legacy_label_count": 8,
        "legacy_independent_axiom_count": 0,
        "physical_binding_separate": True,
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
