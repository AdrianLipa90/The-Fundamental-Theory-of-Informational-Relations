#!/usr/bin/env python3
"""Metatime reproducibility runner for a selected legacy audit subset.

Usage:
    python3 TIR/run_audit.py
    python3 TIR/run_audit.py --json

The runner verifies that nine declared legacy quantities remain reproducible
within their frozen engineering tolerances.  A technical PASS here is not a
physical validation of the full TIR programme, does not replace the v11
publication-readiness ledger, and must not be interpreted as a global accuracy
score across heterogeneous observables.
"""
from __future__ import annotations

import importlib.util
import json
import os
import sys

script_dir = os.path.dirname(os.path.abspath(__file__))
audit_path = os.path.join(script_dir, "metatime_audit.py")
spec = importlib.util.spec_from_file_location("metatime_audit", audit_path)
if spec is None or spec.loader is None:
    raise RuntimeError(f"cannot load audit module from {audit_path}")
audit = importlib.util.module_from_spec(spec)
sys.modules["metatime_audit"] = audit
spec.loader.exec_module(audit)

PDG = audit.PDG
checks = [
    ("m_e", audit.me, PDG["e"], 0.02, "MeV"),
    ("m_mu", audit.mμ, PDG["μ"], 2.0, "MeV"),
    ("m_tau", audit.mτ, PDG["τ"], 20, "MeV"),
    ("1/α", audit.α_inv_metatime, 137.035999084, 1, ""),
    ("sin2θ12", audit.sin2θ12, PDG["sin2θ12"], 0.05, ""),
    ("sin2θ23", audit.sin2θ23, PDG["sin2θ23"], 0.05, ""),
    ("δ_CP", audit.δ_CP, PDG["δCP"], 30, "°"),
    ("λ_CKM", audit.λ_ckm, PDG["λ"], 0.005, ""),
    ("M_H", audit.MH, PDG["MH"], 5, "GeV"),
]

passed = 0
failed = 0
results_list = []
for name, val, ref, tol, unit in checks:
    err = abs(val - ref)
    ok = err <= tol
    results_list.append((name, val, ref, tol, unit, ok, err))
    if ok:
        passed += 1
    else:
        failed += 1

technical_status = "PASS" if failed == 0 else "FAIL"
claim_boundary = (
    "Selected legacy reproducibility subset only; technical PASS is not a "
    "physical PASS, a full-parameter derivation, or a global accuracy score."
)

if "--json" in sys.argv:
    print(
        json.dumps(
            {
                "schema": "TIR_SELECTED_LEGACY_REPRODUCIBILITY_V11_1",
                "technical_status": technical_status,
                "selected_check_count": len(checks),
                "passed": passed,
                "failed": failed,
                "structural_choices": audit.total_structural_my,
                "external_scales": audit.total_ext_scale,
                "external_inputs": audit.total_ext_input,
                "claim_boundary": claim_boundary,
                "checks": [
                    {
                        "name": name,
                        "value": value,
                        "ref": ref,
                        "tolerance": tol,
                        "unit": unit,
                        "status": "PASS" if ok else "FAIL",
                        "absolute_error": err,
                    }
                    for name, value, ref, tol, unit, ok, err in results_list
                ],
            },
            indent=2,
            ensure_ascii=False,
        )
    )
else:
    print("=" * 72)
    print("  METATIME SELECTED LEGACY REPRODUCIBILITY CHECK")
    print("=" * 72)
    for name, val, ref, tol, unit, ok, err in results_list:
        sym = "✓" if ok else "✗"
        u = f" {unit}" if unit else ""
        print(
            f"  {sym} {name:15s} = {val:>12.6g}{u}  "
            f"(ref {ref:>12.6g}, tol {tol:g})  err {err:.4g}"
        )
    print()
    print(f"  Technical passed: {passed}, failed: {failed}")
    print(f"  Structural choices reported by legacy audit: {audit.total_structural_my}")
    print(f"  External: {audit.total_ext_scale} scales + {audit.total_ext_input} inputs")
    print(f"  Technical status: {technical_status}")
    print(f"  Boundary: {claim_boundary}")
    print("=" * 72)
