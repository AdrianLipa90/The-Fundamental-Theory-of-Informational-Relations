from __future__ import annotations
from fractions import Fraction
from itertools import permutations

PAIR_BASIS=((0,1),(0,2),(0,3),(2,3),(3,1),(1,2))
E_PLUS=((1,1,1,1),(1,1,-1,-1),(1,-1,1,-1),(1,-1,-1,1))
PARITY=((1,0,0,0),(0,-1,0,0),(0,0,-1,0),(0,0,0,-1))
G_TETRA=((Fraction(1),0,0,0),(0,Fraction(-1,3),0,0),(0,0,Fraction(-1,3),0),(0,0,0,Fraction(-1,3)))

def matmul(A,B):
    return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))) for i in range(len(A)))
def transpose(A): return tuple(tuple(A[j][i] for j in range(len(A))) for i in range(len(A[0])))
def scale(A,s): return tuple(tuple(s*x for x in row) for row in A)
def add(A,B): return tuple(tuple(x+y for x,y in zip(a,b)) for a,b in zip(A,B))
def sub(A,B): return tuple(tuple(x-y for x,y in zip(a,b)) for a,b in zip(A,B))
def identity(n): return tuple(tuple(Fraction(1 if i==j else 0) for j in range(n)) for i in range(n))
def det(A):
    n=len(A); total=Fraction(0)
    for p in permutations(range(n)):
        inv=sum(1 for i in range(n) for j in range(i+1,n) if p[i]>p[j])
        term=Fraction(-1 if inv%2 else 1)
        for i in range(n): term*=Fraction(A[i][p[i]])
        total+=term
    return total
def exterior_square(A):
    return tuple(tuple(Fraction(A[i][mu])*Fraction(A[j][nu])-Fraction(A[i][nu])*Fraction(A[j][mu]) for mu,nu in PAIR_BASIS) for i,j in PAIR_BASIS)

def validate():
    E=tuple(tuple(Fraction(x) for x in row) for row in E_PLUS)
    P=tuple(tuple(Fraction(x) for x in row) for row in PARITY)
    Em=matmul(P,E)
    Einv=scale(transpose(E),Fraction(1,4))
    gram=matmul(matmul(transpose(E),G_TETRA),E)
    target=tuple(tuple(Fraction(0) if i==j else Fraction(4,3) for j in range(4)) for i in range(4))
    Bp=exterior_square(E); Bm=exterior_square(Em); Pi=exterior_square(P); I=identity(6)
    Qp=scale(add(I,Pi),Fraction(1,2)); Qm=scale(sub(I,Pi),Fraction(1,2))
    zero=scale(I,Fraction(0))
    checks={
        "hadamard_orthogonality":matmul(E,transpose(E))==scale(identity(4),Fraction(4)),
        "det_E_plus_minus16":det(E)==-16,
        "det_E_minus_plus16":det(Em)==16,
        "tetra_null_gram":gram==target,
        "relative_frame_is_parity":matmul(Em,Einv)==P,
        "bivector_frame_invertible":det(Bp)!=0,
        "det_C2_identity":det(Bp)==det(E)**3==-4096,
        "bminus_functorial":Bm==matmul(Pi,Bp),
        "Pi_involution":matmul(Pi,Pi)==I,
        "Pi_3plus3":tuple(Pi[i][i] for i in range(6))==(-1,-1,-1,1,1,1),
        "Qplus_idempotent":matmul(Qp,Qp)==Qp,
        "Qminus_idempotent":matmul(Qm,Qm)==Qm,
        "Qplus_Qminus_zero":matmul(Qp,Qm)==zero,
        "half_sum_projection":scale(add(Bp,Bm),Fraction(1,2))==matmul(Qp,Bp),
        "half_difference_projection":scale(sub(Bp,Bm),Fraction(1,2))==matmul(Qm,Bp),
    }
    return {
        "schema":"TIR_TETRA_NULL_FRAME_BIVECTOR_MOIRE_V0_1",
        "status":"PASS" if all(checks.values()) else "FAIL",
        "checks":checks,
        "det_E_plus":"-16",
        "det_E_minus":"16",
        "det_B_plus":"-4096",
        "bivector_parity_diag":["-1","-1","-1","1","1","1"],
        "legacy_phase36_required":False,
        "constant_antipodal_pair_gravity":"FAIL_FLAT_BACKGROUND",
        "next_gate":"SPACETIME_DEPENDENT_FRAME_DYNAMICS_AND_SOURCE_BINDING"
    }

if __name__=="__main__":
    import json
    print(json.dumps(validate(),indent=2,sort_keys=True))
