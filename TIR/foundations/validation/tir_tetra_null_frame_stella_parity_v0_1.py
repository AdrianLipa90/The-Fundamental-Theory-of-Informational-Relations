from fractions import Fraction
from itertools import permutations

def det(a):
    n=len(a)
    out=Fraction(0)
    for p in permutations(range(n)):
        inv=sum(1 for i in range(n) for j in range(i+1,n) if p[i]>p[j])
        term=Fraction(-1 if inv%2 else 1)
        for i in range(n):
            term*=a[i][p[i]]
        out+=term
    return out

def transpose(a):
    return tuple(tuple(a[j][i] for j in range(len(a))) for i in range(len(a[0])))

def matmul(a,b):
    return tuple(tuple(sum(a[i][k]*b[k][j] for k in range(len(b))) for j in range(len(b[0]))) for i in range(len(a)))

def scale(a,s):
    return tuple(tuple(s*x for x in row) for row in a)

def exterior_square(e):
    pairs=((0,1),(0,2),(0,3),(2,3),(3,1),(1,2))
    out=[]
    for i,j in pairs:
        row=[]
        for mu,nu in pairs:
            row.append(e[i][mu]*e[j][nu]-e[i][nu]*e[j][mu])
        out.append(tuple(row))
    return tuple(out)

def validate():
    # ell=2 normalization gives x_a=(1,n_a), so off-diagonal Minkowski Gram = 4/3.
    gram=tuple(tuple(Fraction(0) if i==j else Fraction(4,3) for j in range(4)) for i in range(4))
    eta=tuple(tuple(Fraction(1 if i==j==0 else -1 if i==j else 0) for j in range(4)) for i in range(4))
    parity=eta

    q=Fraction(3,2)
    e=scale(parity,q)
    c2=exterior_square(e)

    j=[[Fraction(0) for _ in range(6)] for _ in range(6)]
    for i in range(3):
        j[i][i+3]=Fraction(1)
        j[i+3][i]=Fraction(1)
    j=tuple(tuple(row) for row in j)

    expected_c2=tuple(
        tuple(
            (q*q)*(
                -1 if i==k and i<3
                else 1 if i==k and i>=3
                else 0
            )
            for k in range(6)
        )
        for i in range(6)
    )

    checks={
        "tetra_null_gram_det": det(gram)==Fraction(-256,27),
        "tetra_frame_rank4": det(gram)!=0,
        "parity_lorentz_isometry": matmul(matmul(transpose(parity),eta),parity)==eta,
        "parity_det_minus_one": det(parity)==-1,
        "scaled_parity_det": det(e)==-(q**4),
        "bivector_exact_3plus3": c2==expected_c2,
        "bivector_det": det(c2)==-(q**12),
        "wedge_pairing_orientation": matmul(matmul(transpose(c2),j),c2)==scale(j,-(q**4)),
    }
    return {
        "schema":"TIR_TETRA_NULL_FRAME_STELLA_PARITY_V0_1",
        "status":"PASS" if all(checks.values()) else "FAIL",
        "checks":checks,
        "candidate_only":True,
        "generic_gravity_closed":False,
        "next_gate":"DYNAMICAL_DEFORMATION_OF_TETRA_NULL_FRAMES",
    }

if __name__=="__main__":
    import json
    print(json.dumps(validate(),indent=2,sort_keys=True))
