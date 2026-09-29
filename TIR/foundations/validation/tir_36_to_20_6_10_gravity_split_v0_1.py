from fractions import Fraction

G=((Fraction(1),0,0,0),(0,Fraction(-1,3),0,0),(0,0,Fraction(-1,3),0),(0,0,0,Fraction(-1,3)))
GINV=((Fraction(1),0,0,0),(0,Fraction(-3),0,0),(0,0,Fraction(-3),0),(0,0,0,Fraction(-3)))

def mm(A,B): return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))) for i in range(len(A)))
def tr(A): return tuple(tuple(A[j][i] for j in range(len(A))) for i in range(len(A[0])))
def add(A,B): return tuple(tuple(x+y for x,y in zip(a,b)) for a,b in zip(A,B))
def sub(A,B): return tuple(tuple(x-y for x,y in zip(a,b)) for a,b in zip(A,B))
def scale(A,s): return tuple(tuple(s*x for x in row) for row in A)
def zero(n): return tuple(tuple(Fraction(0) for _ in range(n)) for _ in range(n))
def gadjoint(H): return mm(mm(GINV,tr(H)),G)
def split(H):
    A=gadjoint(H)
    return scale(sub(H,A),Fraction(1,2)),scale(add(H,A),Fraction(1,2))
def delta_metric(H): return scale(add(mm(tr(H),G),mm(G,H)),Fraction(-1))

def validate():
    b=Fraction(2,7)
    boost=((0,b,0,0),(3*b,0,0,0),(0,0,0,0),(0,0,0,0))
    strain=((Fraction(1,5),0,0,0),(0,Fraction(2,5),0,0),(0,0,Fraction(-1,7),0),(0,0,0,Fraction(3,11)))
    generic=((Fraction(1,5),Fraction(1,9),0,0),(Fraction(2,7),Fraction(2,5),Fraction(1,8),0),(0,Fraction(-1,6),Fraction(-1,7),Fraction(1,10)),(Fraction(1,12),0,Fraction(1,13),Fraction(3,11)))
    gb,mb=split(boost); gs,ms=split(strain); gg,mg=split(generic)
    checks={
      "boost_is_lorentz_gauge":mb==zero(4) and gb==boost,
      "boost_delta_metric_zero":delta_metric(boost)==zero(4),
      "strain_is_metric_sector":gs==zero(4) and ms==strain,
      "strain_changes_metric":delta_metric(strain)!=zero(4),
      "generic_reconstructs":add(gg,mg)==generic,
      "lorentz_sector_g_antisymmetric":add(mm(tr(gg),G),mm(G,gg))==zero(4),
      "metric_sector_g_symmetric":sub(gadjoint(mg),mg)==zero(4),
      "metric_variation_only_from_metric_sector":delta_metric(generic)==delta_metric(mg),
    }
    return {"schema":"TIR_36_TO_20_6_10_GRAVITY_SPLIT_V0_1","status":"PASS" if all(checks.values()) else "FAIL","checks":checks,"dimension_ledger":{"raw_bivector":36,"simplicity_defect":20,"geometric_gl4":16,"lorentz_gauge":6,"metric_deformation":10},"next_gate":"SOURCE_DYNAMICS_FOR_10D_METRIC_SECTOR"}

if __name__=="__main__":
 import json
 print(json.dumps(validate(),indent=2,sort_keys=True))
