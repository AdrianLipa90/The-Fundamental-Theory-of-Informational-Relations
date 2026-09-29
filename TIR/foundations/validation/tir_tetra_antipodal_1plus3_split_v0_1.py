from fractions import Fraction

E=((1,1,1,1),(1,1,-1,-1),(1,-1,1,-1),(1,-1,-1,1))
P=((1,0,0,0),(0,-1,0,0),(0,0,-1,0),(0,0,0,-1))

def mm(A,B): return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))) for i in range(len(A)))
def add(A,B): return tuple(tuple(x+y for x,y in zip(a,b)) for a,b in zip(A,B))
def sub(A,B): return tuple(tuple(x-y for x,y in zip(a,b)) for a,b in zip(A,B))
def scale(A,s): return tuple(tuple(Fraction(x)*s for x in row) for row in A)

def rank(A):
    a=[list(map(Fraction,row)) for row in A]
    rows=len(a); cols=len(a[0]); r=0
    for c in range(cols):
        piv=next((i for i in range(r,rows) if a[i][c]),None)
        if piv is None: continue
        a[r],a[piv]=a[piv],a[r]
        q=a[r][c]; a[r]=[x/q for x in a[r]]
        for i in range(rows):
            if i!=r and a[i][c]:
                q=a[i][c]; a[i]=[x-q*y for x,y in zip(a[i],a[r])]
        r+=1
        if r==rows: break
    return r

def validate():
    E0=tuple(tuple(Fraction(x) for x in row) for row in E)
    P0=tuple(tuple(Fraction(x) for x in row) for row in P)
    Em=mm(P0,E0)
    common=scale(add(E0,Em),Fraction(1,2))
    diff=scale(sub(E0,Em),Fraction(1,2))
    checks={
      "common_rank_1":rank(common)==1,
      "differential_rank_3":rank(diff)==3,
      "full_rank_4":rank(E0)==4,
      "reconstruct_plus":add(common,diff)==E0,
      "reconstruct_minus":sub(common,diff)==Em,
      "common_only_scalar_row":all(common[i][j]==0 for i in (1,2,3) for j in range(4)),
      "diff_zero_scalar_row":all(diff[0][j]==0 for j in range(4)),
      "differential_column_sum_zero":all(sum(diff[i][j] for j in range(4))==0 for i in range(4)),
    }
    return {"schema":"TIR_TETRA_ANTIPODAL_1PLUS3_SPLIT_V0_1","status":"PASS" if all(checks.values()) else "FAIL","checks":checks,"rank_common":rank(common),"rank_differential":rank(diff),"rank_full":rank(E0),"physical_time_space_binding":"CONDITIONAL","gravity_claim":False}

if __name__=="__main__":
 import json
 print(json.dumps(validate(),indent=2,sort_keys=True))
