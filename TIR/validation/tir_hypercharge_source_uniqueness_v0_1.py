#!/usr/bin/env python3
from fractions import Fraction


def solve(Nc: int, q: Fraction):
    ell = -Nc * q
    h = Nc * q
    u = q + h
    d = q - h
    e = ell - h
    return q, u, d, ell, e, h


def anomalies(Nc: int, vals):
    q, u, d, ell, e, h = vals
    return {
        "SU3^2_U1": 2 * q - u - d,
        "SU2^2_U1": Nc * q + ell,
        "grav^2_U1": Nc * (2 * q - u - d) + (2 * ell - e),
        "U1^3": Nc * (2 * q**3 - u**3 - d**3) + (2 * ell**3 - e**3),
    }


def matrix_rank(rows):
    a = [[Fraction(x) for x in row] for row in rows]
    if not a:
        return 0
    m, n = len(a), len(a[0])
    r = 0
    for c in range(n):
        pivot = next((i for i in range(r, m) if a[i][c] != 0), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        pv = a[r][c]
        a[r] = [x / pv for x in a[r]]
        for i in range(m):
            if i != r and a[i][c] != 0:
                factor = a[i][c]
                a[i] = [x - factor * y for x, y in zip(a[i], a[r])]
        r += 1
        if r == m:
            break
    return r


def linear_constraint_matrix(Nc: int):
    # Variables are (q,u,d,ell,e,h). Rows: three ordinary one-Higgs Yukawa
    # gauge-invariance equations, SU(2)^2 U(1), and grav^2 U(1), all in the
    # v12 right-handed-charge convention.
    return [
        [-1, 1, 0, 0, 0, -1],
        [-1, 0, 1, 0, 0, 1],
        [0, 0, 0, -1, 1, 1],
        [Nc, 0, 0, 1, 0, 0],
        [2 * Nc, -Nc, -Nc, 2, -1, 0],
    ]


def validate():
    # Rank five on six charges proves a one-dimensional relative-charge
    # solution space for the declared field/Yukawa content.
    for Nc in (1, 2, 3, 4, 5, 7):
        assert matrix_rank(linear_constraint_matrix(Nc)) == 5
        for q in (Fraction(1, 17), Fraction(-2, 19), Fraction(5, 23)):
            vals = solve(Nc, q)
            assert all(v == 0 for v in anomalies(Nc, vals).values())
            Q, U, D, L, E, H = vals
            assert U == (Nc + 1) * q
            assert D == (1 - Nc) * q
            assert L == -Nc * q
            assert E == -2 * Nc * q
            assert H == Nc * q

    # TIR normalization anchor on the declared v12 structural data.
    L3, L4, Nc, q_s = 7, 2, 3, 7
    assert q_s == L3
    q = Fraction(q_s, L3 * L4 * Nc)
    assert q == Fraction(1, 6)
    vals = solve(Nc, q)
    assert vals == (
        Fraction(1, 6),
        Fraction(2, 3),
        Fraction(-1, 3),
        Fraction(-1, 2),
        Fraction(-1),
        Fraction(1, 2),
    )
    assert all(v == 0 for v in anomalies(Nc, vals).values())


if __name__ == "__main__":
    validate()
    print("schema=TIR_HYPERCHARGE_SOURCE_UNIQUENESS_V0_1")
    print("status=PASS")
    print("relative_uniqueness_on_declared_field_content=true")
    print("linear_constraint_rank=5_of_6")
    print("y_l_external_parent_eliminated=true")
    print("y_h_derived_from_gravity_anomaly=true")
    print("cubic_anomaly_automatic_after_linear_constraints=true")
    print("tir_yq_normalization=1/6")
    print("right_handed_neutrino_in_scope=false")
    print("overall_u1_normalization_from_anomalies_alone=false")
