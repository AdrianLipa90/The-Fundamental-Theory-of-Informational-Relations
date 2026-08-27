#!/usr/bin/env python3
"""TIR polygonal Stage 67: strict N=6 boundary + gauge-matter source carrier audit."""
from __future__ import annotations

import cmath
import json
import math
from pathlib import Path
from typing import Any

HERE = Path(__file__).resolve().parent
VALIDATION_ROOT = HERE.parent
RESULTS = VALIDATION_ROOT / "results"
REPO_ROOT = Path(__file__).resolve().parents[4]
MASS_AUDIT = (
    REPO_ROOT
    / "TIR"
    / "validation"
    / "results"
    / "collatz_sector_holonomy_mass_audit_v10_2r1.json"
)
STAGE27 = RESULTS / "TIR_POLYGONAL_STAGE27_QUARK_LINK_COUPLING_RECEIPT_V0_1.json"
STAGE28 = RESULTS / "TIR_POLYGONAL_STAGE28_DISCRETE_GAUGE_MATTER_RECEIPT_V0_1.json"
OUT = RESULTS / "TIR_POLYGONAL_STAGE67_MATERIALITY_THRESHOLD_RECEIPT_V0_1.json"
TOL = 1e-12


def load_json(path: Path) -> dict[str, Any]:
    if not path.exists():
        raise FileNotFoundError(path)
    return json.loads(path.read_text(encoding="utf-8"))


def strict_equal_edge_state(n: int) -> dict[str, Any]:
    if n < 3:
        raise ValueError("N must be >= 3")
    angle = 2.0 * math.pi / n
    cosine = math.cos(angle)
    c_n = cosine / (1.0 - cosine)
    r2 = 1.0 - c_n * c_n
    if abs(r2) <= TOL:
        r2 = 0.0
    radius = math.sqrt(r2) if r2 >= 0.0 else None
    return {
        "N": n,
        "c_N": c_n,
        "r_N_squared": r2,
        "r_N": radius,
        "nondegenerate_on_unit_sphere": bool(
            (-1.0 + TOL) < c_n < (1.0 - TOL) and r2 > TOL
        ),
        "degenerate_boundary": bool(abs(c_n - 1.0) <= TOL and abs(r2) <= TOL),
        "strict_equal_edge_forbidden": bool(c_n > 1.0 + TOL or r2 < -TOL),
    }


def gauge_source_witness() -> dict[str, Any]:
    """One nonzero witness for q_i^dagger W_ij q_j and local U(1) subset SU(3) covariance."""
    alpha = 0.37
    beta = -0.23

    # q_i=q_j=e1 and W=I in the first color channel, so B=1.
    b_before = 1.0 + 0.0j

    # G_i=diag(e^{i alpha},e^{-i alpha},1),
    # G_j=diag(e^{i beta}, e^{-i beta},1).
    # The (1,1) component of W' = G_i W G_j^dagger is e^{i(alpha-beta)}.
    qi_prime = cmath.exp(1j * alpha)
    qj_prime = cmath.exp(1j * beta)
    w11_prime = cmath.exp(1j * (alpha - beta))
    b_after = qi_prime.conjugate() * w11_prime * qj_prime

    return {
        "B_before_real": b_before.real,
        "B_after_real": b_after.real,
        "B_after_imag": b_after.imag,
        "gauge_residual": abs(b_after - b_before),
        "nonzero_source_witness": abs(b_before) > TOL,
        "gauge_invariant_witness": abs(b_after - b_before) <= TOL,
    }


def main() -> None:
    stage27 = load_json(STAGE27)
    stage28 = load_json(STAGE28)
    mass = load_json(MASS_AUDIT)

    n3_to_n7 = [strict_equal_edge_state(n) for n in range(3, 8)]
    n6 = n3_to_n7[3]
    n7 = n3_to_n7[4]
    source = gauge_source_witness()

    checks = {
        "strict_equal_edge_N6_is_degenerate_boundary": n6["degenerate_boundary"],
        "strict_equal_edge_N7_is_forbidden_on_unit_sphere": n7[
            "strict_equal_edge_forbidden"
        ],
        "stage27_quark_link_gauge_invariance_pass": (
            stage27.get("status") == "PASS"
            and bool(stage27.get("checks", {}).get("gauge_invariant_bilinear"))
        ),
        "stage28_gauge_matter_action_pass": (
            stage28.get("status") == "PASS"
            and bool(stage28.get("checks", {}).get("full_action_invariant"))
            and bool(stage28.get("checks", {}).get("matter_term_invariant"))
        ),
        "nonzero_gauge_invariant_source_witness_exists": (
            source["nonzero_source_witness"] and source["gauge_invariant_witness"]
        ),
        "mass_audit_keeps_physical_mass_open": (
            mass.get("physical_mass_spectrum_status") == "FAIL_OPEN"
            and mass.get("debt9_status") == "OPEN_NOT_CLOSED"
        ),
        "mass_audit_denies_canonical_mass_derivation": (
            mass.get("canon_allowed") is False
            and mass.get("mass_derivation_claimed") is False
            and mass.get("current_promotion") == "DENY_CURRENT"
        ),
    }

    structural_keys = [
        "strict_equal_edge_N6_is_degenerate_boundary",
        "strict_equal_edge_N7_is_forbidden_on_unit_sphere",
        "stage27_quark_link_gauge_invariance_pass",
        "stage28_gauge_matter_action_pass",
        "nonzero_gauge_invariant_source_witness_exists",
    ]
    firewall_keys = [
        "mass_audit_keeps_physical_mass_open",
        "mass_audit_denies_canonical_mass_derivation",
    ]
    structural_pass = all(checks[key] for key in structural_keys)
    firewall_pass = all(checks[key] for key in firewall_keys)

    if not structural_pass:
        raise RuntimeError("Stage 67 structural material-carrier gate failed")
    if not firewall_pass:
        raise RuntimeError("Stage 67 mass/physical-materiality firewall failed")

    payload = {
        "schema": "tir.polygonal.stage67.materiality-threshold/v0.1",
        "status": "PASS",
        "status_detail": (
            "STRUCTURAL_MATERIAL_CARRIER_PASS__MASS_NORMALIZATION_AND_PHYSICAL_MATERIALITY_OPEN"
        ),
        "checks": checks,
        "strict_equal_edge_geometry": {
            "formula": "c_N=cos(2*pi/N)/(1-cos(2*pi/N)); r_N^2=1-c_N^2",
            "N3_to_N7": n3_to_n7,
            "interpretation": (
                "N=6 is the terminal degenerate boundary of the strict equal-edge continuation; "
                "N=7 is outside the unit-sphere branch under the same rule."
            ),
        },
        "source_carrier": {
            "definition": "B_ij=q_i^dagger W_ij q_j",
            "witness": source,
            "six_plus_one_typing": (
                "terminal geometric-six boundary plus one independent gauge-matter source degree"
            ),
            "septahedral_alias_semantics": "GEOMETRIC_SIX_BOUNDARY_PLUS_SOURCE_ONE",
        },
        "mass_firewall": {
            "source_schema": mass.get("schema"),
            "physical_mass_spectrum_status": mass.get("physical_mass_spectrum_status"),
            "debt9_status": mass.get("debt9_status"),
            "canon_allowed": mass.get("canon_allowed"),
            "mass_derivation_claimed": mass.get("mass_derivation_claimed"),
            "consequence": (
                "Stage 67 admits a structural sourced matter carrier. "
                "Absolute mass normalization, bound-state energy, continuum stress-energy, "
                "and physical materiality remain later gates."
            ),
        },
        "claim_gates": {
            "structural_matter_carrier": "PASS",
            "mass_normalization": "OPEN",
            "bound_state_energy": "OPEN",
            "continuum_stress_energy": "OPEN",
            "physical_materiality": "OPEN",
        },
        "dependencies": {
            "stage27": str(STAGE27.relative_to(REPO_ROOT)),
            "stage28": str(STAGE28.relative_to(REPO_ROOT)),
            "mass_audit": str(MASS_AUDIT.relative_to(REPO_ROOT)),
        },
        "gremlin_role": "candidate-generation/audit; promotion is controlled by executable gates",
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
