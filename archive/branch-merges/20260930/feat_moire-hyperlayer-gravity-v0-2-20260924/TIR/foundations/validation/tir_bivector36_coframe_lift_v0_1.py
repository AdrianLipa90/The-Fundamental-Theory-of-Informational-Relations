from __future__ import annotations
from fractions import Fraction
from itertools import permutations
from typing import Sequence

PAIRS = ((0,1),(0,2),(0,3),(2,3),(3,1),(1,2))

def _det_exact(matrix: Sequence[Sequence[Fraction]]) -> Fraction:
    n=len(matrix)
    if any(len(row)!=n for row in matrix): raise ValueError("matrix must be square")
    total=Fraction(0)
    for p in permutations(range(n)):
        inv=sum(1 for i in range(n) for j in range(i+1,n) if p[i]>p[j])
        term=Fraction(-1 if inv%2 else 1)
        for i in range(n): term*=matrix[i][p[i]]
        total+=term
    return total

def wedge_pairing_j():
    J=[[Fraction(0) for _ in range(6)] for _ in range(6)]
    for i in range(3):
        J[i][i+3]=Fraction(1); J[i+3][i]=Fraction(1)
    return tuple(tuple(r) for r in J)

def exterior_square(e4):
    if len(e4)!=4 or any(len(row)!=4 for row in e4): raise ValueError("expected 4x4 matrix")
    E=[[Fraction(x) for x in row] for row in e4]
    out=[]
    for i,j in PAIRS:
        row=[]
        for mu,nu in PAIRS:
            row.append(E[i][mu]*E[j][nu]-E[i][nu]*E[j][mu])
        out.append(row)
    return tuple(tuple(r) for r in out)

def _transpose(A): return tuple(tuple(A[j][i] for j in range(len(A))) for i in range(len(A[0])))
def _matmul(A,B): return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))) for i in range(len(A)))
def _scale(A,s): return tuple(tuple(s*x for x in row) for row in A)
def _equal(A,B): return all(a==b for ra,rb in zip(A,B) for a,b in zip(ra,rb))

def coframe_lift_certificate(e4):
    E=tuple(tuple(Fraction(x) for x in row) for row in e4)
    d4=_det_exact(E)
    if d4==0: raise ValueError("coframe must be invertible")
    B=exterior_square(E); J=wedge_pairing_j()
    lhs=_matmul(_matmul(_transpose(B),J),B)
    wedge_ok=_equal(lhs,_scale(J,d4))
    d6=_det_exact(B)
    determinant_ok=d6==d4**3
    return {"det_e":d4,"det_b":d6,"wedge_pairing_identity":wedge_ok,"determinant_identity":determinant_ok,"status":"PASS" if wedge_ok and determinant_ok else "FAIL"}

def wedge_lift_residual_exact(B6):
    if len(B6)!=6 or any(len(row)!=6 for row in B6): raise ValueError("expected 6x6 matrix")
    B=tuple(tuple(Fraction(x) for x in row) for row in B6)
    J=wedge_pairing_j()
    K=_matmul(_matmul(_transpose(B),J),B)
    lam=K[0][3]
    target=_scale(J,lam)
    mismatch=sum(1 for r1,r2 in zip(K,target) for x,y in zip(r1,r2) if x!=y)
    wedge_ok=mismatch==0
    det_b=_det_exact(B); det_ok=det_b==lam**3
    return {"lambda":lam,"wedge_pairing_identity":wedge_ok,"mismatched_entries":mismatch,"det_b":det_b,"determinant_identity":det_ok,"status":"PASS_NECESSARY_GATE" if wedge_ok and det_ok and lam!=0 else "FAIL_GATE"}

def euclidean_hodge_star():
    return wedge_pairing_j()

def half_projectors():
    I=tuple(tuple(Fraction(int(i==j)) for j in range(6)) for i in range(6))
    H=euclidean_hodge_star()
    Pp=tuple(tuple((I[i][j]+H[i][j])/2 for j in range(6)) for i in range(6))
    Pm=tuple(tuple((I[i][j]-H[i][j])/2 for j in range(6)) for i in range(6))
    return Pp,Pm

def validate():
    checks={}
    I6=tuple(tuple(Fraction(int(i==j)) for j in range(6)) for i in range(6))
    J=wedge_pairing_j()
    checks["j_square_identity"]=_equal(_matmul(J,J),I6)
    examples=[
        [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]],
        [[2,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]],
        [[1,2,0,1],[0,1,1,0],[1,0,2,1],[0,1,0,1]],
    ]
    for idx,E in enumerate(examples):
        cert=coframe_lift_certificate(E)
        checks[f"coframe_{idx}_wedge"]=cert["wedge_pairing_identity"]
        checks[f"coframe_{idx}_det"]=cert["determinant_identity"]
        checks[f"coframe_{idx}_raw_gate"]=wedge_lift_residual_exact(exterior_square(E))["status"]=="PASS_NECESSARY_GATE"
    Bbad=[list(r) for r in exterior_square(examples[2])]; Bbad[0][0]+=1
    checks["perturbed_36d_rejected"]=wedge_lift_residual_exact(Bbad)["status"]=="FAIL_GATE"
    Pp,Pm=half_projectors()
    zero=tuple(tuple(Fraction(0) for _ in range(6)) for _ in range(6))
    checks["pplus_idempotent"]=_equal(_matmul(Pp,Pp),Pp)
    checks["pminus_idempotent"]=_equal(_matmul(Pm,Pm),Pm)
    checks["projectors_orthogonal"]=_equal(_matmul(Pp,Pm),zero)
    checks["projectors_sum_identity"]=_equal(tuple(tuple(Pp[i][j]+Pm[i][j] for j in range(6)) for i in range(6)),I6)
    checks["rank_trace_three_each"]=sum(Pp[i][i] for i in range(6))==3 and sum(Pm[i][i] for i in range(6))==3
    return {"schema":"TIR_BIVECTOR36_COFRAME_GATE_V0_1","status":"PASS" if all(checks.values()) else "FAIL","checks":checks}

if __name__=="__main__":
    import json
    print(json.dumps(validate(),indent=2,sort_keys=True,default=str))
