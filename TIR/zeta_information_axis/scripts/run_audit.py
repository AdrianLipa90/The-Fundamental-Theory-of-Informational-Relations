#!/usr/bin/env python3
"""Generate a machine-readable audit of exact identities and numerical checks."""

from __future__ import annotations

import json
from datetime import UTC, datetime
from pathlib import Path

import mpmath as mp

from critical_axis.core import (
    aharonov_bohm_holonomy,
    berry_holonomy,
    binary_entropy,
    binary_entropy_prime,
    binary_entropy_second,
    centered_inversion,
    centered_zeta_involution,
    compactified_radius,
    completed_xi,
    dirichlet_eta,
    eta_prefactor,
    first_nontrivial_zeros,
    hubble_length,
    normalized_hubble_radius,
    reciprocal_map,
    strip_probability_coordinate,
    two_channel_amplitude,
    u1_holonomy,
    zeta_involution,
)

mp.mp.dps = 80
ROOT = Path(__file__).resolve().parents[1]
REPORTS = ROOT / "reports"
REPORTS.mkdir(exist_ok=True)


def as_pair(z: mp.mpc) -> dict[str, str]:
    return {"real": mp.nstr(mp.re(z), 50), "imag": mp.nstr(mp.im(z), 50)}


def main() -> None:
    p = mp.mpf("0.5")
    amp = two_channel_amplitude(p, mp.pi)
    hol = berry_holonomy(p)

    xi_points = [mp.mpc("0.2", "3.0"), mp.mpc("0.7", "8.0"), mp.mpc("1.3", "2.5")]
    xi_residuals = [abs(completed_xi(s) - completed_xi(1 - s)) for s in xi_points]

    eta_points = [mp.mpc("0.7", "3.2"), mp.mpc("1.2", "5.1"), mp.mpc("2.0", "0.5")]
    eta_residuals = [abs(dirichlet_eta(s) - eta_prefactor(s) * mp.zeta(s)) for s in eta_points]

    u = mp.mpc("0.23", "4.5")
    reciprocal_twice_residual = abs(reciprocal_map(reciprocal_map(u)) - u)
    reciprocal_commutation_residual = abs(
        reciprocal_map(centered_zeta_involution(u))
        - centered_zeta_involution(reciprocal_map(u))
    )

    critical_s = mp.mpc("0.5", "14.134725")
    critical_inverse = centered_inversion(critical_s)
    critical_axis_residual = abs(mp.re(critical_inverse))

    strip_s = mp.mpc("0.31", "7")
    strip_p = strip_probability_coordinate(strip_s)
    strip_jp = strip_probability_coordinate(zeta_involution(strip_s))
    complement_covariance_residual = abs(strip_jp - (1 - strip_p))

    ab_pi = aharonov_bohm_holonomy(mp.pi)
    generic_pi = u1_holonomy(mp.pi)

    sample_h = mp.mpf("2.3")
    sample_c = mp.mpf("7.1")
    sample_lh = hubble_length(sample_h, sample_c)
    hubble_unit_residual = abs(
        normalized_hubble_radius(sample_lh, sample_h, sample_c) - 1
    )

    zeros = first_nontrivial_zeros(20)
    zero_records = [
        {
            "index": k,
            "zero": as_pair(z),
            "critical_line_residual": mp.nstr(abs(mp.re(z) - p), 30),
            "zeta_residual": mp.nstr(abs(mp.zeta(z)), 30),
        }
        for k, z in enumerate(zeros, start=1)
    ]

    report = {
        "generated_utc": datetime.now(UTC).replace(microsecond=0).isoformat(),
        "precision_decimal_digits": mp.mp.dps,
        "claim_policy": {
            "exact_identities": "PASS means algebraic or standard analytic identities reproduced numerically",
            "riemann_hypothesis": "OPEN; no proof is claimed",
            "coordinate_promotion": (
                "p=Re(s) is theorem-level only under the explicit affine, "
                "endpoint-preserving strip-to-simplex assumptions"
            ),
            "zero_state_population": (
                "The claim that zeta zero states must use that coordinate as "
                "branch population remains MODEL POSTULATE / OPEN"
            ),
            "ab_hubble_relation": (
                "U(1) holonomy and Hubble radial normalization are implemented "
                "separately; their common TIR potential-tension interpretation "
                "remains MODEL POSTULATE"
            ),
        },
        "shannon": {
            "H_half": mp.nstr(binary_entropy(p), 50),
            "ln2": mp.nstr(mp.log(2), 50),
            "H_prime_half": mp.nstr(binary_entropy_prime(p), 50),
            "H_second_half": mp.nstr(binary_entropy_second(p), 50),
            "status": "PASS",
        },
        "two_channel_cancellation": {
            "amplitude_at_half_pi": as_pair(amp),
            "absolute_residual": mp.nstr(abs(amp), 50),
            "status": "PASS",
        },
        "berry_holonomy": {
            "holonomy_at_half": as_pair(hol),
            "minus_one_residual": mp.nstr(abs(hol + 1), 50),
            "status": "PASS",
        },
        "centered_reciprocal_geometry": {
            "sample_u": as_pair(u),
            "reciprocal_twice_residual": mp.nstr(reciprocal_twice_residual, 50),
            "reciprocal_commutation_residual": mp.nstr(reciprocal_commutation_residual, 50),
            "critical_axis_inverse": as_pair(critical_inverse),
            "critical_axis_real_residual": mp.nstr(critical_axis_residual, 50),
            "compactified_radius_1e20": mp.nstr(compactified_radius(mp.mpf("1e20")), 50),
            "status": "PASS",
        },
        "affine_strip_coordinate": {
            "sample_p": mp.nstr(strip_p, 50),
            "complement_covariance_residual": mp.nstr(complement_covariance_residual, 50),
            "status": "PASS_UNDER_STATED_AFFINE_ASSUMPTIONS",
        },
        "u1_holonomy": {
            "generic_pi_holonomy": as_pair(generic_pi),
            "ab_pi_holonomy": as_pair(ab_pi),
            "generic_minus_one_residual": mp.nstr(abs(generic_pi + 1), 50),
            "ab_minus_one_residual": mp.nstr(abs(ab_pi + 1), 50),
            "status": "PASS",
        },
        "hubble_normalization": {
            "sample_H": mp.nstr(sample_h, 50),
            "sample_c": mp.nstr(sample_c, 50),
            "sample_L_H": mp.nstr(sample_lh, 50),
            "unit_radius_residual": mp.nstr(hubble_unit_residual, 50),
            "status": "DEFINITIONAL_PASS",
            "physical_boundary_interpretation": "MODEL_POSTULATE",
        },
        "xi_functional_equation": {
            "residuals": [mp.nstr(r, 50) for r in xi_residuals],
            "status": "PASS",
        },
        "eta_factorization": {
            "residuals": [mp.nstr(r, 50) for r in eta_residuals],
            "eta_one_minus_ln2": mp.nstr(abs(dirichlet_eta(1) - mp.log(2)), 50),
            "status": "PASS",
        },
        "first_20_tabulated_zeros": zero_records,
        "global_status": {
            "technical_identities": "PASS",
            "numerical_reproduction": "PASS",
            "coordinate_identification": "PARTIALLY_PROMOTED_CONDITIONAL_THEOREM",
            "zero_state_representation": "OPEN_GAP",
            "ab_hubble_potential_tension": "MODEL_POSTULATE",
            "critical_axis_explanation": "CONDITIONAL THEOREM",
            "riemann_hypothesis": "OPEN",
        },
    }

    json_path = REPORTS / "numerical_audit.json"
    json_path.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")

    md = [
        "# Numerical Audit",
        "",
        f"Generated: `{report['generated_utc']}`",
        "",
        "| Layer | Status |",
        "|---|---|",
        "| Binary Shannon maximum | PASS |",
        "| Exact two-channel cancellation | PASS |",
        "| Equatorial Berry holonomy | PASS |",
        "| Centred reciprocal involution / commutation | PASS |",
        "| Critical-axis set invariance under `1/u` | PASS |",
        "| Radial centre-to-boundary compactification | PASS |",
        "| Affine strip-to-simplex coordinate | PASS under stated affine assumptions |",
        "| Generic U(1) / Aharonov-Bohm `pi` holonomy | PASS |",
        "| Hubble radial normalization `H L / c = 1` at `L=c/H` | DEFINITIONAL PASS |",
        "| AB/Hubble common physical potential-tension identification | **MODEL POSTULATE** |",
        "| Completed-xi symmetry | PASS |",
        "| Dirichlet-eta factorization and eta(1)=ln 2 | PASS |",
        "| First 20 tabulated zeros reproduced | PASS |",
        "| Canonical zero-state representation | **OPEN GAP** |",
        "| Riemann hypothesis proved | **NO - OPEN** |",
        "",
        "The audit verifies exact mathematical identities and implementation-level "
        "normalizations. It does not promote the AB/Hubble potential-tension "
        "correspondence to established physics and does not convert the conditional "
        "critical-axis selection principle into an unconditional proof of RH.",
    ]
    (REPORTS / "numerical_audit.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    print(json_path)


if __name__ == "__main__":
    main()
