#!/usr/bin/env python3
"""Stage 17: exact E7/E8 branching multiplicity comparison around the common E6 core.

Pure dimension and tensor-product arithmetic. Physical family selection remains open.
"""
import json


def run():
    # Standard branch dimensions.
    e7 = {
        "adjoint_dimension": 133,
        "E6_core": 78,
        "U1_singlet": 1,
        "E6_27": 27,
        "E6_27bar": 27,
    }
    e8 = {
        "adjoint_dimension": 248,
        "E6_core": 78,
        "SU3_commutant_adjoint": 8,
        "E6_27_x_SU3_3": 27 * 3,
        "E6_27bar_x_SU3_3bar": 27 * 3,
    }

    # E6 fundamental branch 27 -> 16 + 10 + 1.
    e6_27 = {"SO10_16": 16, "SO10_10": 10, "SO10_1": 1}

    # Tensor multiplicities from the external factor dimensions.
    e7_positive_27 = {
        "SO10_16_carrier_dimension": 16,
        "multiplicity_factor": 1,
        "total_16_sector_dimension": 16,
    }
    e8_positive_27_triplet = {
        "SO10_16_carrier_dimension": 16,
        "multiplicity_factor": 3,
        "total_16_sector_dimension": 16 * 3,
        "SO10_10_total_dimension": 10 * 3,
        "SO10_1_total_dimension": 1 * 3,
    }

    checks = {
        "E7_branch_dimension": 78 + 1 + 27 + 27 == 133,
        "E8_branch_dimension": 78 + 8 + 27*3 + 27*3 == 248,
        "E6_27_branch_dimension": 16 + 10 + 1 == 27,
        "E7_single_27_multiplicity": e7_positive_27["multiplicity_factor"] == 1,
        "E8_27_triplet_multiplicity": e8_positive_27_triplet["multiplicity_factor"] == 3,
        "E8_16_triplet_dimension": e8_positive_27_triplet["total_16_sector_dimension"] == 48,
    }

    return {
        "schema": "TIR-E7-E8-MULTIPLICITY/0.1",
        "stage": 17,
        "E7_under_E6_x_U1": e7,
        "E8_under_E6_x_SU3": e8,
        "E6_27_under_SO10": e6_27,
        "E7_positive_27_carrier": e7_positive_27,
        "E8_positive_27_SU3_triplet_carrier": e8_positive_27_triplet,
        "checks": checks,
        "verdict": "PASS" if all(checks.values()) else "FAIL",
        "physical_family_identification": "OPEN"
    }


if __name__ == "__main__":
    print(json.dumps(run(), indent=2))
