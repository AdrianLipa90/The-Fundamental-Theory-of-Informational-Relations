#!/usr/bin/env python3
"""Stage 19: representation-conjugation Z2 on the E7/E8 branch labels."""
import json


def conj_e7(label):
    table = {
        "27_+2": "27bar_-2",
        "27bar_-2": "27_+2",
        "78_0": "78_0",
        "1_0": "1_0",
    }
    return table[label]


def conj_e8(label):
    table = {
        "(27,3)": "(27bar,3bar)",
        "(27bar,3bar)": "(27,3)",
        "(78,1)": "(78,1)",
        "(1,8)": "(1,8)",
    }
    return table[label]


def run():
    e7_labels = ["78_0", "1_0", "27_+2", "27bar_-2"]
    e8_labels = ["(78,1)", "(1,8)", "(27,3)", "(27bar,3bar)"]
    checks = {
        "E7_conjugation_order_2": all(conj_e7(conj_e7(x)) == x for x in e7_labels),
        "E8_conjugation_order_2": all(conj_e8(conj_e8(x)) == x for x in e8_labels),
        "E7_27_pair_exchanged": conj_e7("27_+2") == "27bar_-2",
        "E8_triplet_pair_exchanged": conj_e8("(27,3)") == "(27bar,3bar)",
        "E6_core_adjoint_fixed": conj_e7("78_0") == "78_0" and conj_e8("(78,1)") == "(78,1)",
    }
    return {
        "schema": "TIR-EXCEPTIONAL-CONJUGATION-Z2/0.1",
        "stage": 19,
        "checks": checks,
        "verdict": "PASS" if all(checks.values()) else "FAIL",
        "TIR_chiral_intertwiner_status": "OPEN_OPERATOR_GATE"
    }


if __name__ == "__main__":
    print(json.dumps(run(), indent=2))
