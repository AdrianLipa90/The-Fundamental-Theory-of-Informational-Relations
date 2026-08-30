#!/usr/bin/env python3
from __future__ import annotations

import json

CLASSES = frozenset("ABCDEF")
TIMING = frozenset({"RETROSPECTIVE", "PROSPECTIVE", "EXTERNAL", "--"})
VERDICTS = frozenset({"PASS", "COMPATIBLE", "TENSION", "FAIL", "OPEN", "QUARANTINED"})

LEGACY_MAP = {
    "PASS_COMPATIBILITY": "COMPATIBLE",
    "PASS_STRONG_COMPATIBILITY": "COMPATIBLE",
    "CANDIDATE_COMPATIBILITY": "COMPATIBLE",
    "TENSION": "TENSION",
    "SCHEME_UNDEFINED_TENSION": "TENSION",
    "FAIL_PRECISION": "FAIL",
    "FAIL_PRECISION_TENSION": "FAIL",
    "FORMULA_BROKEN": "FAIL",
    "AMBIGUOUS_COMPATIBILITY": "OPEN",
    "INCONCLUSIVE": "OPEN",
    "NOT_INDEPENDENTLY_TESTED": "OPEN",
    "NOT_TESTABLE_CURRENTLY": "OPEN",
    "PROVENANCE_CONTAMINATED": "QUARANTINED",
    "PROVENANCE_INCOMPLETE": "QUARANTINED",
    "REPRODUCTION_NOT_VALIDATION": "QUARANTINED",
}

ROWS = {
    "ckm_magnitudes": ("C", "RETROSPECTIVE", "COMPATIBLE"),
    "ckm_delta": ("C", "RETROSPECTIVE", "COMPATIBLE"),
    "ckm_jcp": ("C", "RETROSPECTIVE", "COMPATIBLE"),
    "pmns_theta12": ("C", "RETROSPECTIVE", "COMPATIBLE"),
    "pmns_dm21": ("C", "RETROSPECTIVE", "COMPATIBLE"),
    "pmns_theta23": ("C", "RETROSPECTIVE", "OPEN"),
    "pmns_theta13": ("C", "RETROSPECTIVE", "TENSION"),
    "pmns_delta": ("C", "RETROSPECTIVE", "OPEN"),
    "neutrino_absolute_masses": ("C", "RETROSPECTIVE", "OPEN"),
    "neutrino_absolute_action_legacy_equation": ("D", "RETROSPECTIVE", "QUARANTINED"),
    "charged_lepton_e": ("C", "RETROSPECTIVE", "FAIL"),
    "charged_lepton_mu": ("C", "RETROSPECTIVE", "FAIL"),
    "charged_lepton_tau": ("C", "RETROSPECTIVE", "FAIL"),
    "baryon_octet": ("C", "RETROSPECTIVE", "QUARANTINED"),
    "baryon_decuplet": ("C", "RETROSPECTIVE", "COMPATIBLE"),
    "meson_pion_legacy_formula": ("D", "RETROSPECTIVE", "FAIL"),
    "meson_kaon_legacy_formula": ("D", "RETROSPECTIVE", "FAIL"),
    "meson_eta_mapping": ("C", "RETROSPECTIVE", "QUARANTINED"),
    "meson_heavy_vector_table": ("C", "RETROSPECTIVE", "QUARANTINED"),
    "ew_vev": ("B", "RETROSPECTIVE", "OPEN"),
    "ew_sin2theta": ("B", "RETROSPECTIVE", "TENSION"),
    "ew_alpha_inverse": ("C", "RETROSPECTIVE", "FAIL"),
    "ew_mw": ("C", "RETROSPECTIVE", "FAIL"),
    "ew_mz": ("C", "RETROSPECTIVE", "FAIL"),
    "higgs_mass": ("C", "RETROSPECTIVE", "FAIL"),
    "quark_mass_map": ("B", "--", "OPEN"),
    "strong_cp_theta": ("C", "RETROSPECTIVE", "OPEN"),
    "strong_cp_neutron_edm_gate": ("D", "RETROSPECTIVE", "FAIL"),
    "gauge_anomaly_algebra": ("B", "--", "OPEN"),
    "cosmological_density_legacy_formula": ("D", "RETROSPECTIVE", "QUARANTINED"),
}


def main() -> None:
    checks: dict[str, bool] = {}
    checks["row_ids_unique"] = len(ROWS) == len(set(ROWS))
    checks["all_classes_valid"] = all(row[0] in CLASSES for row in ROWS.values())
    checks["all_timing_valid"] = all(row[1] in TIMING for row in ROWS.values())
    checks["all_verdicts_valid"] = all(row[2] in VERDICTS for row in ROWS.values())
    checks["theta13_tension_retained"] = ROWS["pmns_theta13"][2] == "TENSION"
    checks["charged_lepton_precision_fail_retained"] = all(
        ROWS[key][2] == "FAIL" for key in ("charged_lepton_e", "charged_lepton_mu", "charged_lepton_tau")
    )
    checks["neutron_edm_fail_retained"] = ROWS["strong_cp_neutron_edm_gate"][2] == "FAIL"
    checks["neutrino_formula_diagnostic_quarantined"] = ROWS["neutrino_absolute_action_legacy_equation"][2] == "QUARANTINED"
    checks["cosmology_formula_diagnostic_quarantined"] = ROWS["cosmological_density_legacy_formula"][2] == "QUARANTINED"
    checks["legacy_map_targets_valid"] = set(LEGACY_MAP.values()) <= VERDICTS

    status = "PASS" if all(checks.values()) else "FAIL"
    receipt = {
        "schema": "TIR_V12_EVIDENCE_MATRIX_CONSISTENCY_V0_1",
        "status": status,
        "current_evidence_owner": "TIR/monograph/v12/chapters/ch19_unified_evidence_matrix.tex",
        "row_count": len(ROWS),
        "allowed_claim_classes": sorted(CLASSES),
        "allowed_timing": sorted(TIMING),
        "allowed_verdicts": sorted(VERDICTS),
        "legacy_status_normalization": LEGACY_MAP,
        "checks": checks,
        "rows": {key: {"class": value[0], "timing": value[1], "verdict": value[2]} for key, value in ROWS.items()},
    }
    print(json.dumps(receipt, indent=2, sort_keys=True))
    raise SystemExit(0 if status == "PASS" else 1)


if __name__ == "__main__":
    main()
