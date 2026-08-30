#!/usr/bin/env python3
"""Fail-closed integration audit for substantive TIR monograph v12 appendices."""
from __future__ import annotations

import hashlib
import json
import math
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
APP = ROOT / "TIR/monograph/v12/appendices"
RECEIPT = ROOT / "TIR/validation/TIR_V12_APPENDIX_INTEGRATION_AUDIT_V0_1.json"

FILES = {
    "A": APP / "appA_formal_proofs_long_algebra.tex",
    "B": APP / "appB_numerical_tables_reproducibility.tex",
    "C": APP / "appC_publication_protocol_prospective_gates.tex",
    "D": APP / "appD_cross_framework_interfaces.tex",
}

EXPECTED_SHA256 = {
    "A": "6c988340da4ea2ed087f70967896b2175ff3938cecf15b39422802a8aca8749e",
    "B": "0c1f19cb52ef8439d7440783cf3a0ebaec9b0d5a0f3a8308252a52e10290a182",
    "C": "0be84432c1b7353f103e508410041f2e59e52580c6550bb3e4875834d7608884",
    "D": "5dfd16a354aca4fd1aa55032c0fb4d55e89cf265d1168b5cd1b5d5f908e98834",
}

def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")

def sha256(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()

def main() -> None:
    checks: dict[str, bool] = {}
    detail: dict[str, object] = {}

    texts = {}
    for key, path in FILES.items():
        checks[f"appendix_{key}_exists"] = path.is_file()
        texts[key] = read(path) if path.is_file() else ""
        checks[f"appendix_{key}_substantive"] = len(texts[key]) >= 5000
        checks[f"appendix_{key}_wrapper_marker_absent"] = (
            r"\section*{v12 source integration map}" not in texts[key]
        )
        checks[f"appendix_{key}_sha256_frozen"] = sha256(texts[key]) == EXPECTED_SHA256[key]

    A, B, C, D = (texts[k] for k in "ABCD")

    checks["su3_27_irrep_repair_present"] = (
        r"\dim(2,2)=27" in A and r"3\otimes\bar3=8\oplus1" in A
    )
    checks["poincare_factor_two_repair_present"] = (
        r"=2\,\operatorname{artanh}" in A
        and "normalization repair" in A
    )
    checks["tetrahedral_gram_rank3_present"] = (
        r"\operatorname{rank}G=3" in A
        and r"\operatorname{Aut}(\Delta^3)\cong S_4" in A
        and r"|S_4|=24" in A
    )
    checks["legacy_dihedral_surface_quarantined"] = (
        "Legacy operator-tetrahedron firewall" in A
        and r"\vTwelveStatus{D}{RETROSPECTIVE}{QUARANTINED}" in A
    )
    checks["quarter_power_arithmetic_present"] = (
        r"\rho_C" in A and r"=\frac34" in A
    )
    checks["common_baseline_no_go_present"] = (
        r"\varepsilon_{\min}" in A and "4.7207104" in A
        and r"\vTwelveStatus{D}{RETROSPECTIVE}{PASS}" in A
    )

    dim_22 = (2 + 1) * (2 + 1) * (2 + 2 + 2) // 2
    checks["su3_dim_22_exact"] = dim_22 == 27

    a = Fraction(-1, 3)
    principal_minor = (1 - a) ** 2 * (1 + 2 * a)
    checks["tetrahedron_principal_minor_rank3"] = principal_minor == Fraction(16, 27)

    residuals = [3.1857238256, 0.0818052322, 0.2293790515]
    spread = max(residuals) - min(residuals)
    eps = spread / 2.0
    factor = math.exp(eps)
    checks["common_baseline_minimax_numeric"] = (
        abs(spread - 3.1039185934) < 1e-10
        and abs(eps - 1.5519592967) < 1e-10
        and abs(factor - 4.7207104) < 1e-6
    )

    rho_c = math.exp(math.log(3.0) - 2.0 * math.log(2.0))
    checks["quarter_power_rho_exact_numeric"] = abs(rho_c - 0.75) < 1e-15

    required_B = (
        "TIR_PDG2026_VALIDATION_MATRIX_V2.md",
        "tir_v12_hadron_formula_audit_v0_2.py",
        "tir_v12_evidence_matrix_consistency_v0_2.py",
        "tir_v12_appendix_integration_audit_v0_1.py",
        "formula FAIL",
        "zero Type-3 fonts",
        "exact PR-head SHA",
    )
    checks["appendix_B_reproducibility_contract_present"] = all(x in B for x in required_B)
    checks["appendix_B_neutrino_reconciliation_present"] = (
        r"S_1^{\rm literal}" in B and r"S_1^{\rm rec}" in B
    )
    checks["appendix_B_ckm_pmns_snapshot_present"] = (
        "246.122449" in B and "66.4218215" in B and "3.110115459" in B
    )
    checks["appendix_B_legacy_zero_error_tables_not_promoted"] = (
        "target-matched tables as fresh evidence" in B
        and "QUARANTINED" in B
    )

    checks["appendix_C_freeze_date_present"] = "29 July 2026" in C
    checks["appendix_C_exactly_three_named_candidates"] = (
        C.count(r"\paragraph{C1:") == 1
        and C.count(r"\paragraph{C2:") == 1
        and C.count(r"\paragraph{C3:") == 1
        and r"N_{\rm candidate}=3" in C
    )
    checks["appendix_C_orthogonal_pair_present"] = (
        r"\frac{y_c}{y_\mu}" in C and r"\frac{y_c}{y_t}" in C
        and "isolates the sector contribution" in C
        and "isolates the generation/release contribution" in C
    )
    frozen_values = (
        "4.850346751338371",
        "0.16766796647328305",
        "2.3521800134268784",
        "0.17147213462587316",
        "6.858021228826228",
        "2.8101955040512466",
    )
    checks["appendix_C_six_frozen_values_present"] = all(x in C for x in frozen_values)
    checks["appendix_C_no_refit_versioning_present"] = (
        "No-refit and versioning rule" in C
        and "new version identity" in C
        and "retrospective mass tables remain outside the prospective score" in C
    )
    checks["appendix_C_old_tau_mapping_historical_only"] = (
        r"y_c/y_\tau" in C and "historical" in C and "provenance" in C
    )

    checks["appendix_D_half_entropy_exact"] = (
        r"H_2(1/2)=\ln2" in D and r"\operatorname*{arg\,max}" in D
    )
    checks["appendix_D_kappa_internal_owner"] = (
        r"\kappa" in D and r"\frac{\ln2}{24\pi}" in D
        and "canonical TIR-internal normalization theorem" in D
    )
    checks["appendix_D_negative_inverse_identity_present"] = (
        r"z_L(s)=1-\frac1s=-\frac1{\Omega(s)}" in D
        and r"\Re s=\frac12" in D and r"|z_L(s)|=1" in D
    )
    checks["appendix_D_li_frontier_present"] = (
        "negative Li" in D and r"\lambda_n\ge0\quad\forall n" in D
        and "native arithmetic closure" in D
    )
    checks["appendix_D_idt_phase_clock_present"] = (
        r"\ell_\varphi" in D and r"\frac{c}{|\omega_t|}" in D
        and r"ds_{\rm rel}^2" in D
    )
    checks["appendix_D_gremlin_bounded"] = (
        "bounded candidate-generation and adversarial-audit layer" in D
        and "deterministic proof/validator gate" in D
    )
    checks["appendix_D_stale_kappa_postulate_phrase_absent"] = (
        "model postulate" not in D and "TIR structural definition" not in D
    )
    checks["appendix_D_negative_definition_section_absent"] = (
        "What this is NOT" not in D and "Claim boundary" not in D
    )

    receipt_ok = False
    receipt = {}
    if RECEIPT.is_file():
        try:
            receipt = json.loads(read(RECEIPT))
            receipt_ok = (
                receipt.get("schema") == "TIR_V12_APPENDIX_INTEGRATION_AUDIT_V0_1"
                and receipt.get("technical_status") == "PASS"
                and receipt.get("appendix_sha256") == EXPECTED_SHA256
            )
        except json.JSONDecodeError:
            receipt_ok = False
    checks["static_receipt_bound_to_appendix_hashes"] = receipt_ok

    detail["appendix_sizes"] = {k: len(texts[k]) for k in "ABCD"}
    detail["appendix_sha256"] = {k: sha256(texts[k]) for k in "ABCD"}
    detail["su3_dim_22"] = dim_22
    detail["tetrahedron_principal_minor"] = str(principal_minor)
    detail["common_baseline_spread"] = spread
    detail["common_baseline_epsilon_min"] = eps
    detail["common_baseline_factor_min"] = factor
    detail["quarter_power_rho"] = rho_c

    status = "PASS" if all(checks.values()) else "FAIL"
    out = {
        "schema": "TIR_V12_APPENDIX_INTEGRATION_AUDIT_V0_1",
        "technical_status": status,
        "appendix_count": 4,
        "checks": checks,
        "detail": detail,
    }
    print(json.dumps(out, indent=2, sort_keys=True))
    raise SystemExit(0 if status == "PASS" else 1)

if __name__ == "__main__":
    main()
