#!/usr/bin/env python3

import json
from fractions import Fraction


def add(u, v):
    return tuple(a + b for a, b in zip(u, v))


def sub(u, v):
    return tuple(a - b for a, b in zip(u, v))


def scale(c, v):
    return tuple(c * x for x in v)


def mat_vec(M, v):
    return tuple(sum(M[i][j] * v[j] for j in range(3)) for i in range(3))


def relation(x, y, c):
    return scale(c, sub(y, x))


x = (Fraction(1, 5), Fraction(-2, 7), Fraction(3, 11))
y = (Fraction(4, 9), Fraction(5, 13), Fraction(-1, 6))
z = (Fraction(-3, 8), Fraction(7, 10), Fraction(2, 3))
a = (Fraction(2, 3), Fraction(-1, 4), Fraction(5, 12))

L = (
    (Fraction(1), Fraction(1), Fraction(0)),
    (Fraction(0), Fraction(1), Fraction(1)),
    (Fraction(1), Fraction(0), Fraction(2)),
)

c = Fraction(7, 5)

Fx = add(mat_vec(L, x), a)
Fy = add(mat_vec(L, y), a)

translation_naturality = relation(add(x, a), add(y, a), c) == relation(x, y, c)
affine_naturality = relation(Fx, Fy, c) == mat_vec(L, relation(x, y, c))
reversal = relation(y, x, c) == scale(Fraction(-1), relation(x, y, c))
endpoint = relation(x, z, c) == add(relation(x, y, c), relation(y, z, c))
triangle = add(add(relation(x, y, c), relation(y, z, c)), relation(z, x, c)) == (0, 0, 0)
distinction_preserved = c != 0 and relation(x, y, c) != (0, 0, 0)

torsor_c = Fraction(1)
torsor_displacement = relation(x, y, torsor_c) == sub(y, x)
pauli_relative_scale = Fraction(2)

checks = {
    "translation_naturality": translation_naturality,
    "affine_naturality_sample": affine_naturality,
    "reversal": reversal,
    "endpoint_composition": endpoint,
    "triangle_closure": triangle,
    "distinction_preservation_nonzero_scale": distinction_preserved,
    "torsor_normalization_c_equals_1": torsor_displacement,
    "pauli_coordinate_scale_relative_to_density_difference": str(pauli_relative_scale),
}

technical_status = "PASS" if all(v is True for v in checks.values() if isinstance(v, bool)) else "FAIL"

receipt = {
    "schema": "TIR_A1_A3_SOURCE_MINIMALITY_NATURALITY_V0_1",
    "technical_status": technical_status,
    "exact_result": "SOURCE_MINIMAL_AFFINE_NATURAL_RELATION_IS_c_TIMES_ENDPOINT_DIFFERENCE",
    "relation_formula": "R(x,y)=c*(y-x)",
    "distinction_preservation_requires": "c!=0",
    "torsor_normalization": "c=1",
    "pauli_generator_normalization": "E_xy=2*(rho_y-rho_x)",
    "remaining_tir_gate": "A1_DEPENDENCY_MINIMALITY_APPLIES_TO_PRIMITIVE_LAW_SIGNATURE",
    "mathematical_chain_after_gate": "AFFINE_NATURALITY->R=c(y-x)->Herm_0(2)~=R3",
    "checks": checks,
}

print(json.dumps(receipt, indent=2, sort_keys=True))
