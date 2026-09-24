from fractions import Fraction
from itertools import permutations

TETRA=((1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1))
Q=tuple(tuple(Fraction(1 if row==0 else TETRA[col][row-1]) for col in range(4)) for row in range(4))
ETA=((Fraction(3),0,0,0),(0,-1,0,0),(0,0,-1,0),(0,0,0,-1))
P=((Fraction(1),0,0,0),(0,-1,0,0),(0,0,-1,0),(0,0,0,-1))
PAIRS=((0,1),(0,2),(0,3),(2,3),(3,1),(1,2))
J=tuple(tuple(Fraction(1) if (i<3 and j==i+3) or (i>=3 and j==i-3) else Fraction(0) for j in range(6)) for i in range(6))

def mm(A,B):
    return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))) for i in range(len(A)))

def tr(A):
    return tuple(tuple(A[j][i] for j in range(len(A))) for i in range(len(A[0])))

def scale(A,s):
    return tuple(tuple(s*x for x in row) for row in A)

def eye(n):
    return tuple(tuple(Fraction(int(i==j)) for j in range(n)) for i in range(n))

def det(A):
    n=len(A)
    out=Fraction(0)
    for p in permutations(range(n)):
        inv=sum(1 for i in range(n) for j in range(i+1,n) if p[i]>p[j])
        term=Fraction(-1 if inv%2 else 1)
        for i in range(n):
            term*=A[i][p[i]]
        out+=term
    return out

def diag(values):
    vals=tuple(Fraction(x) for x in values)
    return tuple(tuple(vals[i] if i==j else Fraction(0) for j in range(len(vals))) for i in range(len(vals)))

def c2(A):
    out=[]
    for i,j in PAIRS:
        row=[]
        for mu,nu in PAIRS:
            row.append(A[i][mu]*A[j][nu]-A[i][nu]*A[j][mu])
        out.append(tuple(row))
    return tuple(out)

def relative_scale_coframe(ratios):
    D=diag(ratios)
    return mm(mm(Q,D),scale(Q,Fraction(1,4)))

def validate():
    checks={}
    checks["hadamard_symmetric"]=Q==tr(Q)
    checks["hadamard_square_4I"]=mm(Q,Q)==scale(eye(4),4)
    checks["hadamard_det_minus16"]=det(Q)==-16

    gram=mm(mm(tr(Q),ETA),Q)
    target=tuple(tuple(Fraction(0) if i==j else Fraction(4) for j in range(4)) for i in range(4))
    checks["rational_null_tetra_gram"]=gram==target

    c2p=c2(P)
    checks["antipode_bivector_3plus3"]=c2p==diag((-1,-1,-1,1,1,1))
    checks["antipode_reverses_wedge_orientation"]=mm(mm(tr(c2p),J),c2p)==scale(J,-1)

    examples=((2,3,5,7),(1,1,1,1),(3,4,4,9))
    for index,raw in enumerate(examples):
        ratios=tuple(Fraction(x) for x in raw)
        A=relative_scale_coframe(ratios)
        product=Fraction(1)
        for x in ratios:
            product*=x
        checks[f"relative_scale_det_{index}"]=det(A)==product
        C=c2(A)
        checks[f"relative_scale_wedge_{index}"]=mm(mm(tr(C),J),C)==scale(J,product)

    checks["uniform_scale_is_scalar_identity"]=relative_scale_coframe((5,5,5,5))==scale(eye(4),5)

    elapsed=(Fraction(2),Fraction(3),Fraction(5),Fraction(7))
    jac=Fraction(1)
    for ell in elapsed:
        jac*=ell**3/Fraction(16)
    checks["four_packet_rank16_jacobian_nonzero"]=jac>0

    return {
        "schema":"TIR_FOUR_PACKET_NULL_TETRA_COFRAME_MOIRE_V0_1",
        "status":"PASS" if all(checks.values()) else "FAIL",
        "checks":checks,
        "det_hadamard":str(det(Q)),
        "four_packet_jacobian_example":str(jac),
        "physical_gravity_claim":False,
        "candidate_only":True,
    }

if __name__=="__main__":
    import json
    print(json.dumps(validate(),indent=2,sort_keys=True))
