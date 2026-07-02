#!/usr/bin/env python3
"""
Metatime Reproducibility Runner — one-command audit verification.

Usage:
    python3 TIR/run_audit.py            # Run audit + verify outputs
    python3 TIR/run_audit.py --json     # JSON output for automated verification
"""
import json, sys, importlib.util, os

script_dir = os.path.dirname(os.path.abspath(__file__))
audit_path = os.path.join(script_dir, "metatime_audit.py")
spec = importlib.util.spec_from_file_location("metatime_audit", audit_path)
audit = importlib.util.module_from_spec(spec)
sys.modules['metatime_audit'] = audit
spec.loader.exec_module(audit)

PDG = audit.PDG
checks = [
    ('m_e',       audit.me,        PDG['e'],      0.02,    'MeV'),
    ('m_mu',      audit.mμ,        PDG['μ'],      2.0,     'MeV'),
    ('m_tau',     audit.mτ,        PDG['τ'],      20,      'MeV'),
    ('1/α',       audit.α_inv_metatime, 137.035999084, 1,   ''),
    ('sin2θ12',   audit.sin2θ12,   PDG['sin2θ12'], 0.05,   ''),
    ('sin2θ23',   audit.sin2θ23,   PDG['sin2θ23'], 0.05,   ''),
    ('δ_CP',      audit.δ_CP,      PDG['δCP'],     30,     '°'),
    ('λ_CKM',     audit.λ_ckm,     PDG['λ'],       0.005,  ''),
    ('M_H',       audit.MH,        PDG['MH'],      5,      'GeV'),
]

passed, failed = 0, 0
results_list = []
for name, val, ref, tol, unit in checks:
    err = abs(val - ref)
    ok = err <= tol
    results_list.append((name, val, ref, unit, ok, err))
    if ok: passed += 1
    else:  failed += 1

if '--json' in sys.argv:
    print(json.dumps({
        "status": "PASS" if failed == 0 else "FAIL",
        "passed": passed, "failed": failed,
        "structural_choices": audit.total_structural_my,
        "external_scales": audit.total_ext_scale,
        "external_inputs": audit.total_ext_input,
        "checks": [{"name":n,"value":v,"ref":r,"status":"PASS" if ok else "FAIL","error":e}
                    for n,v,r,_,ok,e in results_list]
    }, indent=2))
else:
    print("=" * 65)
    print("  METATIME REPRODUCIBILITY CHECK")
    print("=" * 65)
    for name, val, ref, unit, ok, err in results_list:
        sym = "✓" if ok else "✗"
        u = f" {unit}" if unit else ""
        print(f"  {sym} {name:15s} = {val:>12.6g}{u}  (ref {ref:>12.6g})  err {err:.4g}")
    print()
    print(f"  Passed: {passed}, Failed: {failed}")
    print(f"  Structural choices: {audit.total_structural_my}")
    print(f"  External: {audit.total_ext_scale} scales + {audit.total_ext_input} inputs")
    print(f"  Overall: {'✓ PASS' if failed==0 else '✗ FAIL'}")
    print("=" * 65)
