#!/usr/bin/env python3
"""Source-first validator for the TIR canonical derivation spine.

This validator checks:
- required proof surfaces exist;
- the canonical root does not use SO(3) to create S2;
- exact finite identities for half-seam/Bloch/spin closure;
- source-status markers for the archived Euler--Berry theorem.

It does not compile the monograph and does not validate physical universality.
"""
from __future__ import annotations

import cmath
import json
import math
from pathlib import Path

TIR = Path(__file__).resolve().parents[1]
REPO = TIR.parent

SOURCES = {
    "spine": TIR / "foundations" / "TIR_CANONICAL_DERIVATION_SPINE_V0_1.md",
    "registry": TIR / "provenance" / "TIR_FOUNDATION_PROOF_SOURCE_REGISTRY_V0_1.md",
    "first_distinction": TIR / "foundations" / "TIR_FIRST_DISTINCTION_THEOREM_V0_2.md",
    "phase_core": TIR / "foundations" / "TIR_RELATIONAL_PHASE_LAGRANGIAN_CORE_V0_1.md",
    "half_seam": TIR / "foundations" / "TIR_HALF_SEAM_PHASE_FIBER_V0_1.md",
    "lagrangian_bloch": TIR / "foundations" / "TIR_LAGRANGIAN_BLOCH_SELECTION_V0_1.md",
    "spin_lift": TIR / "foundations" / "TIR_WHITE_THREAD_SPIN_LIFT_LYAPUNOV_V0_1.md",
    "euler_berry_spin": REPO / "archive" / "v7.9" / "full" / "22_euler_identity_berry_phase_spin_constraint_v2_4" / "METATIME_SM_EULER_IDENTITY_BERRY_PHASE_SPIN_CONSTRAINT_v2_4.md",
    "hilbert_kahler": REPO / "archive" / "v7.9" / "full" / "01_foundational_formal_notes" / "hilbert_kahler_phase_hamiltonian" / "main.tex",
}

def half_seam_check() -> dict[str, object]:
    u = 0.5
    h = -(1-u)*math.log(1-u) - u*math.log(u)
    return {
        "u": u,
        "entropy": h,
        "ln2": math.log(2.0),
        "pass": math.isclose(h, math.log(2.0), rel_tol=0.0, abs_tol=1e-15),
    }

def bloch_check() -> dict[str, object]:
    rows = []
    ok = True
    for u, phi in ((0.0,0.0),(0.5,0.0),(0.5,math.pi/2),(1.0,0.0),(0.2,1.3)):
        r = (
            2*math.sqrt(u*(1-u))*math.cos(phi),
            2*math.sqrt(u*(1-u))*math.sin(phi),
            1-2*u,
        )
        norm2 = sum(x*x for x in r)
        good = math.isclose(norm2,1.0,rel_tol=0.0,abs_tol=1e-14)
        ok &= good
        rows.append({"u":u,"phi":phi,"norm2":norm2,"pass":good})
    return {"rows":rows,"pass":ok}

def euler_berry_spin_check() -> dict[str, object]:
    candidates = [0.5,1.0,1.5,2.0,2.5]
    rows = []
    valid = []
    for s in candidates:
        phase = cmath.exp(-1j * s * 2*math.pi)
        sign_residual = abs(phase + 1)
        double_phase = cmath.exp(-1j * s * 4*math.pi)
        double_residual = abs(double_phase - 1)
        good = sign_residual < 1e-12 and double_residual < 1e-12
        if good:
            valid.append(s)
        rows.append({
            "s":s,
            "half_sphere_sign_residual":sign_residual,
            "doubled_loop_identity_residual":double_residual,
            "pass":good,
        })
    return {
        "rows":rows,
        "valid":valid,
        "minimal_positive":min(valid) if valid else None,
        "pass":bool(valid) and min(valid)==0.5,
    }

def spin_lift_check() -> dict[str, object]:
    two_pi = cmath.exp(-0.5j * 2*math.pi)
    four_pi = cmath.exp(-0.5j * 4*math.pi)
    return {
        "2pi": [two_pi.real,two_pi.imag],
        "4pi": [four_pi.real,four_pi.imag],
        "pass": abs(two_pi+1)<1e-12 and abs(four_pi-1)<1e-12,
    }

def source_firewall() -> dict[str, object]:
    missing = [name for name,path in SOURCES.items() if not path.is_file()]
    if missing:
        return {"missing":missing,"pass":False}
    texts = {name:path.read_text(encoding="utf-8",errors="replace") for name,path in SOURCES.items()}
    markers = {
        "zero_nonlogical_axioms": "N_{\\rm nonlogical\\ axioms}=0" in texts["spine"],
        "minimum_object_point": "minimum object" in texts["spine"] and "point" in texts["spine"],
        "minimum_structure_relation": "minimum nontrivial structure" in texts["spine"],
        "phase_core_u1": "SOURCE_PROMOTED_EXACT_STRUCTURAL_PHASE_CORE" in texts["phase_core"] and "U(1)" in texts["phase_core"],
        "half_fibre_source": "phase fiber" in texts["half_seam"] or "phase fibre" in texts["half_seam"],
        "lagrangian_bloch_owner": "EXACT_MINIMAL_COHERENT_PROJECTIVE_GEOMETRY" in texts["lagrangian_bloch"],
        "euler_spin_source_status": "FORMAL_SYMBOLIC_PASS" in texts["euler_berry_spin"],
        "spin_lift_4pi": "4\\pi" in texts["spin_lift"] or "4π" in texts["spin_lift"],
        "lagrangian_u1": "\\chi\\in U(1)" in texts["hilbert_kahler"],
        "no_so3_before_s2": (
            "no pre-existing \\(SO(3)\\) action is required" in texts["lagrangian_bloch"]
            or "No prior \\(SO(3)\\)" in texts["spine"]
        ),
    }
    return {"missing":[],"markers":markers,"pass":all(markers.values())}

def main() -> None:
    blocks = {
        "half_seam": half_seam_check(),
        "bloch_unit_sphere": bloch_check(),
        "euler_berry_spin": euler_berry_spin_check(),
        "spin_lift": spin_lift_check(),
        "source_firewall": source_firewall(),
    }
    passed = all(block["pass"] for block in blocks.values())
    receipt = {
        "schema":"TIR_CANONICAL_DERIVATION_SPINE_V0_1",
        "canonical_nonlogical_axiom_count":0,
        "minimum_object":"POINT",
        "minimum_nontrivial_structure":"RELATION",
        "canonical_phase_fibre":"U(1) ~= S1",
        "sphere_route":"S1 + RELATIONAL_POLAR_PAIR -> SUSPENSION(S1) ~= S2 -> CP1 -> BERRY/EULER -> SPIN1/2",
        "so3_used_to_create_s2":False,
        "compile_performed":False,
        "blocks":blocks,
        "technical_status":"PASS" if passed else "FAIL",
    }
    print(json.dumps(receipt,indent=2,sort_keys=True))
    if not passed:
        raise SystemExit(1)

if __name__=="__main__":
    main()
