#!/usr/bin/env python3
import cmath
import json
import math

TOL = 2e-10

X = [[0j, 1+0j], [1+0j, 0j]]
Y = [[0j, -1j], [1j, 0j]]
Z = [[1+0j, 0j], [0j, -1+0j]]
I2 = [[1+0j, 0j], [0j, 1+0j]]


def zeros(n, m=None):
    m = n if m is None else m
    return [[0j for _ in range(m)] for _ in range(n)]


def eye(n):
    A = zeros(n)
    for i in range(n):
        A[i][i] = 1+0j
    return A


def add(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def sub(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def scale(c, A):
    return [[c * A[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def mm(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]


def dagger(A):
    return [[A[j][i].conjugate() for j in range(len(A))] for i in range(len(A[0]))]


def kron(A, B):
    out = zeros(len(A) * len(B), len(A[0]) * len(B[0]))
    for i in range(len(A)):
        for j in range(len(A[0])):
            for k in range(len(B)):
                for l in range(len(B[0])):
                    out[i*len(B)+k][j*len(B[0])+l] = A[i][j] * B[k][l]
    return out


def kron_all(ms):
    out = [[1+0j]]
    for M in ms:
        out = kron(out, M)
    return out


def maxnorm(A):
    return max((abs(x) for row in A for x in row), default=0.0)


def comm(A, B):
    return sub(mm(A, B), mm(B, A))


def gammas(d):
    m = d // 2
    gs = []
    for j in range(m):
        gs.append(kron_all([Z] * j + [X] + [I2] * (m-j-1)))
        gs.append(kron_all([Z] * j + [Y] + [I2] * (m-j-1)))
    if d % 2:
        gs.append(kron_all([Z] * m))
    return gs[:d]


def lincomb(coeffs, mats):
    out = zeros(len(mats[0]))
    for c, M in zip(coeffs, mats):
        out = add(out, scale(c, M))
    return out


def simplex_data(n):
    D = n + 1
    gs = gammas(D)
    dspin = len(gs[0])
    mean = scale(1.0 / D, lincomb([1.0] * D, gs))
    fac = math.sqrt(D / n)
    sigmas = [scale(fac, sub(g, mean)) for g in gs]
    vertices = []
    for i in range(D):
        v = [-1.0 / D] * D
        v[i] += 1.0
        vertices.append([fac * x for x in v])
    return gs, sigmas, vertices, dspin


def dot(a, b):
    return sum(x*y for x, y in zip(a, b))


def transport(A, B, c):
    I = eye(len(A))
    return scale(1.0 / math.sqrt(2.0 * (1.0 + c)), add(I, mm(A, B)))


def add_block(M, br, bc, B, coeff=1.0):
    d = len(B)
    for i in range(d):
        for j in range(d):
            M[br*d+i][bc*d+j] += coeff * B[i][j]


def global_sigma(sigmas):
    N = len(sigmas)
    d = len(sigmas[0])
    S = zeros(N*d)
    for i, s in enumerate(sigmas):
        add_block(S, i, i, s)
    return S


def bloch_hamiltonian(n, sigmas, U, k, break_edge=False):
    N = n + 1
    d = len(sigmas[0])
    I = eye(d)
    H = zeros(N*d)
    for i, s in enumerate(sigmas):
        eps = (i + 1) / (10.0 * N)
        mu = (i + 1) / (20.0 * N)
        add_block(H, i, i, add(scale(eps, I), scale(mu, s)))
    for i in range(N):
        for j in range(i + 1, N):
            t = 1.0 / (N + i + j + 1.0)
            add_block(H, i, j, U[i, j], -t)
            add_block(H, j, i, U[j, i], -t)
    tau = 0.173
    for i in range(N):
        a = (i + 1) % N
        edge = I if (break_edge and i == 0) else U[a, i]
        add_block(H, a, i, edge, -tau * cmath.exp(1j*k))
        add_block(H, i, a, dagger(edge), -tau * cmath.exp(-1j*k))
    return H


def face_holonomy_check(n, gs, sigmas, vertices, U):
    i, j, k = 0, 1, 2
    c = -1.0 / n
    W = mm(mm(U[i, j], U[j, k]), U[k, i])
    vi, vj, vk = vertices[i], vertices[j], vertices[k]
    den = math.sqrt(1.0 - c*c)
    p = [(vj[a] - c*vi[a]) / den for a in range(n+1)]
    tk = [(vk[a] - c*vi[a]) / den for a in range(n+1)]
    cosA = c / (1.0 + c)
    sinA = math.sqrt(1.0 - cosA*cosA)
    q = [(tk[a] - cosA*p[a]) / sinA for a in range(n+1)]
    Gp = lincomb(p, gs)
    Gq = lincomb(q, gs)
    J = mm(Gp, Gq)
    I = eye(len(J))
    A = math.acos(-1.0 / (n - 1.0))
    omega = 3.0*A - math.pi
    pred = add(scale(math.cos(omega/2.0), I), scale(math.sin(omega/2.0), J))
    return {
        'omega': omega,
        'turn_fraction': omega / (2.0 * math.pi),
        'J_square_error': maxnorm(add(mm(J, J), I)),
        'J_antihermitian_error': maxnorm(add(dagger(J), J)),
        'face_formula_error': maxnorm(sub(W, pred)),
        'face_commutator_error': maxnorm(comm(W, sigmas[i])),
    }


def run_n(n):
    gs, sigmas, vertices, dspin = simplex_data(n)
    I = eye(dspin)
    c = -1.0 / n
    checks = {}
    checks['simplex_dot_error'] = max(abs(dot(vertices[i], vertices[j]) - (1.0 if i == j else c)) for i in range(n+1) for j in range(n+1))
    checks['involution_error'] = max(maxnorm(sub(mm(s, s), I)) for s in sigmas)
    checks['clifford_pair_error'] = max(maxnorm(sub(add(mm(sigmas[i], sigmas[j]), mm(sigmas[j], sigmas[i])), scale(2.0*c, I))) for i in range(n+1) for j in range(i+1, n+1))
    U = {}
    unit_err = 0.0
    int_err = 0.0
    dag_err = 0.0
    for i in range(n+1):
        U[i, i] = I
        for j in range(n+1):
            if i == j:
                continue
            u = transport(sigmas[i], sigmas[j], c)
            U[i, j] = u
            unit_err = max(unit_err, maxnorm(sub(mm(u, dagger(u)), I)))
            int_err = max(int_err, maxnorm(sub(mm(sigmas[i], u), mm(u, sigmas[j]))))
    for i in range(n+1):
        for j in range(n+1):
            dag_err = max(dag_err, maxnorm(sub(U[j, i], dagger(U[i, j]))))
    checks['transport_unitarity_error'] = unit_err
    checks['transport_intertwiner_error'] = int_err
    checks['reverse_transport_dagger_error'] = dag_err
    SG = global_sigma(sigmas)
    IG = eye(len(SG))
    checks['global_involution_error'] = maxnorm(sub(mm(SG, SG), IG))
    bloch_err = 0.0
    herm_err = 0.0
    sector_cross_err = 0.0
    for k in (0.0, 0.37, 1.1, math.pi):
        H = bloch_hamiltonian(n, sigmas, U, k)
        bloch_err = max(bloch_err, maxnorm(comm(H, SG)))
        herm_err = max(herm_err, maxnorm(sub(H, dagger(H))))
        Pp = scale(0.5, add(IG, SG))
        Pm = scale(0.5, sub(IG, SG))
        sector_cross_err = max(sector_cross_err, maxnorm(mm(mm(Pp, H), Pm)), maxnorm(mm(mm(Pm, H), Pp)))
    checks['bloch_commutator_error'] = bloch_err
    checks['bloch_hermiticity_error'] = herm_err
    checks['sector_cross_error'] = sector_cross_err
    Hbad = bloch_hamiltonian(n, sigmas, U, 0.37, break_edge=True)
    negative = maxnorm(comm(Hbad, SG))
    checks['negative_control_commutator'] = negative
    face = face_holonomy_check(n, gs, sigmas, vertices, U) if n >= 3 else None
    pass_small = all(v < TOL for k, v in checks.items() if k != 'negative_control_commutator')
    pass_neg = negative > 1e-4
    pass_face = True if face is None else all(face[k] < TOL for k in ('J_square_error','J_antihermitian_error','face_formula_error','face_commutator_error'))
    return {
        'n': n,
        'ambient_dimension': n+1,
        'spinor_dimension': dspin,
        'checks': checks,
        'face': face,
        'pass': pass_small and pass_neg and pass_face,
    }


results = [run_n(n) for n in range(2, 8)]
q3 = results[1]['face']['turn_fraction']
uniqueness_numeric = abs(q3 - 0.5) < TOL and all(abs(r['face']['turn_fraction'] - 0.5) > 1e-6 for r in results[2:])
passed = all(r['pass'] for r in results) and uniqueness_numeric
payload = {
    'schema': 'DYNAMIC_IDENTITY_INVARIANT_PERIODIC_SIMPLEX_BLOCH_FLOQUET_V0_2',
    'technical_status': 'PASS' if passed else 'FAIL',
    'claim_scope': {
        'explicit_periodic_n_simplex_construction': 'EXACT_BY_CONSTRUCTION_FOR_N>=2',
        'triangular_face_holonomy_formula': 'EXACT_FOR_N>=3',
        'tetrahedral_half_turn_uniqueness': 'EXACT_FOR_REGULAR_N_SIMPLEX_FAMILY_N>=3',
        'validator': 'NUMERICAL_WITNESS_N_2_THROUGH_7',
        'physical_identity_binding': False,
        'personal_identity_binding': False,
        'physical_hamiltonian_binding': False,
    },
    'tetrahedral_turn_fraction_q3': q3,
    'numeric_half_turn_unique_in_sample': uniqueness_numeric,
    'results': results,
}
print(json.dumps(payload, indent=2, sort_keys=True))
raise SystemExit(0 if passed else 1)
