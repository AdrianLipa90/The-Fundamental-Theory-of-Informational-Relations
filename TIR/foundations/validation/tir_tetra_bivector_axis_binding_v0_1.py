from itertools import permutations

PAIR_BASIS=((0,1),(0,2),(0,3),(2,3),(3,1),(1,2))

def parity(p):
    inv=sum(1 for i in range(4) for j in range(i+1,4) if p[i]>p[j])
    return -1 if inv%2 else 1

def pair_index_sign(i,j):
    for k,(a,b) in enumerate(PAIR_BASIS):
        if (i,j)==(a,b): return k,1
        if (i,j)==(b,a): return k,-1
    raise ValueError((i,j))

def induced_pair_matrix(p):
    M=[[0]*6 for _ in range(6)]
    for col,(i,j) in enumerate(PAIR_BASIS):
        row,sign=pair_index_sign(p[i],p[j])
        M[row][col]=sign
    return M

def transpose(A): return list(map(list,zip(*A)))
def matmul(A,B): return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
def scale(A,s): return [[s*x for x in row] for row in A]

def wedge_pairing():
    J=[[0]*6 for _ in range(6)]
    for i in range(3):
        J[i][i+3]=1
        J[i+3][i]=1
    return J

def validate():
    J=wedge_pairing()
    checks={
        "edge_count_6": len(PAIR_BASIS)==6,
        "edge_pair_channel_count_36": len(PAIR_BASIS)**2==36,
        "opposite_pairs_are_J": all(J[i][i+3]==1 and J[i+3][i]==1 for i in range(3)),
    }
    total=even=odd=0
    for p in permutations(range(4)):
        C=induced_pair_matrix(p)
        ok=matmul(matmul(transpose(C),J),C)==scale(J,parity(p))
        total+=int(ok)
        if parity(p)==1: even+=int(ok)
        else: odd+=int(ok)
    checks["s4_all_24_conformal_wedge"]=total==24
    checks["a4_all_12_preserve_J"]=even==12
    checks["odd_all_12_reverse_J"]=odd==12
    return {
        "schema":"TIR_TETRA_BIVECTOR_AXIS_BINDING_V0_1",
        "status":"PASS" if all(checks.values()) else "FAIL",
        "checks":checks,
        "s4_pass_count":total,
        "a4_pass_count":even,
        "odd_pass_count":odd,
        "legacy_phase36_edgepair_binding":"NOT_DERIVED",
        "candidate_only":True,
    }

if __name__=="__main__":
    import json
    print(json.dumps(validate(),indent=2,sort_keys=True))
