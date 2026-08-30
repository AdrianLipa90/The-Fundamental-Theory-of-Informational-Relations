from __future__ import annotations

import json
import math

SCHEMA = "TIR_V12_NEUTRINO_ACTION_CONSISTENCY_V0_1"


def spectrum(*, extra_kappa: bool) -> dict[str, object]:
    kappa = math.log(2.0) / (24.0 * math.pi)
    L3 = 7.0
    L4 = 2.0
    E_P_MEV = 1.22089e22
    S_bare = (1.0 + L4 / L3) / 2.0
    A_face = ((L4 / L3) ** 2) / 2.0
    dS = kappa * A_face * (1.0 - kappa)
    S1 = S_bare + (kappa * dS if extra_kappa else dS)
    ratios = (1.0, L4, L3 + L4 + 1.0)
    actions = tuple(S1 - kappa * math.log(r) for r in ratios)
    masses = tuple(E_P_MEV * 1e6 * math.exp(-S / kappa) for S in actions)
    splittings = (
        masses[1] ** 2 - masses[0] ** 2,
        masses[2] ** 2 - masses[0] ** 2,
    )
    return {
        "kappa": kappa,
        "S_bare": S_bare,
        "A_face": A_face,
        "dS": dS,
        "S1": S1,
        "actions": actions,
        "masses_eV": masses,
        "splittings_eV2": splittings,
    }


def main() -> int:
    published = (0.00501, 0.01002, 0.0501)
    literal = spectrum(extra_kappa=True)
    reconciled = spectrum(extra_kappa=False)

    def max_rel(xs: tuple[float, ...]) -> float:
        return max(abs(x - y) / y for x, y in zip(xs, published))

    literal_error = max_rel(literal["masses_eV"])
    reconciled_error = max_rel(reconciled["masses_eV"])
    checks = {
        "literal_printed_formula_does_not_reproduce_published_masses": literal_error > 0.04,
        "single_offset_rule_reproduces_published_masses": reconciled_error < 2e-6,
        "published_ratio_pattern_is_1_2_10": all(
            abs(reconciled["masses_eV"][i] / reconciled["masses_eV"][0] - r) < 2e-12
            for i, r in enumerate((1.0, 2.0, 10.0))
        ),
    }
    receipt = {
        "schema": SCHEMA,
        "status": "PASS" if all(checks.values()) else "FAIL",
        "checks": checks,
        "published_masses_eV": list(published),
        "literal_printed_rule": "S1 = S_bare + kappa*dS",
        "literal_result": literal,
        "literal_max_relative_mass_error_vs_printed_values": literal_error,
        "reconciled_rule": "S1 = S_bare + dS",
        "reconciled_result": reconciled,
        "reconciled_max_relative_mass_error_vs_printed_values": reconciled_error,
        "diagnostic_class": "FORMULA_VALUE_MISMATCH_WITH_UNIQUE_SINGLE_OFFSET_RECONSTRUCTION",
        "promotion_authority": False,
    }
    print(json.dumps(receipt, indent=2, sort_keys=True))
    return 0 if receipt["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
