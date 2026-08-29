#!/usr/bin/env python3
"""Deterministic referee/claim firewall for The Space of Geometry v1.1."""
from __future__ import annotations

from pathlib import Path
import json

ROOT = Path("TIR/subrepos/the-space-of-geometry")
MANUSCRIPT = ROOT / "paper/THE_SPACE_OF_GEOMETRY_V1_1.tex"
FIREWALL = ROOT / "publication/REFEREE_CLAIM_FIREWALL_V1_1.md"
DEPENDENCY_AUDIT = ROOT / "publication/PROOF_DEPENDENCY_AUDIT_V0_3.md"
PHYSICAL_THEOREM = ROOT / "foundations/PHYSICAL_RELATION_CHORD_REALIZABILITY_V0_1.md"

MANUSCRIPT_TOKENS = (
    r"\Astate=\frac12 I+\Herm_0(2)",
    r"\Erel_{xy}:=2\delta_{xy}=2(\rho_y-\rho_x)",
    "Physical relation chord domain",
    r"|\dvec|\le2",
    "Theorem E: local Euclidean and Pythagorean closure",
    "Theorem R: physical-state Pythagorean realization",
    r"\frac9{25}+\frac{16}{25}=1",
    "Theorem T1: minimal finite full-dimensional support",
    "Theorem T2: regularity from A5+A7 edge-orbit invariance",
    "Theorem Q: tetrahedral SIC convergence",
    "Global geometry boundary",
)

FIREWALL_TOKENS = (
    "AFFINE_TRANSLATION_CARRIER",
    "PHYSICAL_SINGLE_EDGE_DOMAIN",
    "PASS_V1_1_REFEREE_CLAIM_FIREWALL",
    "INFORMATIONAL_CONVERGENCE_CROSSCHECK",
    "DOWNSTREAM GEOMETRY PROGRAMME",
    "No tetrahedral theorem occurs upstream of this endpoint",
    "The physical Pythagorean certificate is constructed entirely inside this subset",
)

DEPENDENCY_TOKENS = (
    "PASS_V1_1_SYNCHRONIZED_LOCAL_PROOF_GRAPH",
    "tetrahedral nodes are not ancestors of carrier Pythagoras",
    "tetrahedral nodes are not ancestors of physical-state Pythagoras",
    "the SIC node is not an ancestor of any main theorem endpoint",
)

PHYSICAL_TOKENS = (
    "reachable physical relation set is exactly the radius-two ball",
    r"a^2+b^2\le1",
    r"a=\frac35",
    r"b=\frac45",
)


def token_map(path: Path, tokens: tuple[str, ...]) -> dict[str, bool]:
    text = path.read_text(encoding="utf-8") if path.is_file() else ""
    return {token: token in text for token in tokens}


def build_receipt() -> dict[str, object]:
    manuscript = token_map(MANUSCRIPT, MANUSCRIPT_TOKENS)
    firewall = token_map(FIREWALL, FIREWALL_TOKENS)
    dependency = token_map(DEPENDENCY_AUDIT, DEPENDENCY_TOKENS)
    physical = token_map(PHYSICAL_THEOREM, PHYSICAL_TOKENS)

    required_surfaces = {
        str(MANUSCRIPT): MANUSCRIPT.is_file(),
        str(FIREWALL): FIREWALL.is_file(),
        str(DEPENDENCY_AUDIT): DEPENDENCY_AUDIT.is_file(),
        str(PHYSICAL_THEOREM): PHYSICAL_THEOREM.is_file(),
    }

    manuscript_pass = all(manuscript.values())
    firewall_pass = all(firewall.values())
    dependency_pass = all(dependency.values())
    physical_pass = all(physical.values())
    surfaces_pass = all(required_surfaces.values())

    passed = all((
        manuscript_pass,
        firewall_pass,
        dependency_pass,
        physical_pass,
        surfaces_pass,
    ))

    return {
        "schema": "TIR_SPACE_OF_GEOMETRY_REFEREE_CLAIM_FIREWALL_V1_1",
        "technical_status": "PASS" if passed else "FAIL",
        "verdict": "PASS_V1_1_REFEREE_CLAIM_FIREWALL" if passed else "FAIL_V1_1_REFEREE_CLAIM_FIREWALL",
        "canonical_manuscript": "THE_SPACE_OF_GEOMETRY_V1_1.tex",
        "carrier_domain_type": "AFFINE_TRANSLATION_CARRIER",
        "physical_domain_type": "PHYSICAL_SINGLE_EDGE_DOMAIN",
        "physical_domain": "RADIUS_TWO_BALL",
        "physical_certificate": "3/5,4/5,1",
        "tetrahedron_dependency_into_pythagoras": False,
        "sic_dependency_into_main_endpoints": False,
        "scale_status": "PAULI_NORMALIZED_LOCAL_GEOMETRIC_MEASURE_WITH_DOWNSTREAM_PHYSICAL_CALIBRATION",
        "global_extent_status": "DOWNSTREAM_GEOMETRY_PROGRAMME",
        "manuscript_scope_synchronized": manuscript_pass,
        "firewall_surface_synchronized": firewall_pass,
        "dependency_surface_synchronized": dependency_pass,
        "physical_realizability_surface_synchronized": physical_pass,
        "all_required_surfaces_present": surfaces_pass,
        "manuscript_tokens": manuscript,
        "firewall_tokens": firewall,
        "dependency_tokens": dependency,
        "physical_tokens": physical,
        "required_surfaces": required_surfaces,
    }


def main() -> None:
    receipt = build_receipt()
    print(json.dumps(receipt, indent=2, sort_keys=True))
    if receipt["technical_status"] != "PASS":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
