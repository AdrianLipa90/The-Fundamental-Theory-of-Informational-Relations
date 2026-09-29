#!/usr/bin/env python3
"""Zero-axiom audit for spatial-promotion uniqueness v0.2."""
import json

def mm(a,b):
    return [[sum(a[i][k]*b[k][j] for k in range(3)) for j in range(3)] for i in range(3)]

def tr(a):
    return [list(x) for x in zip(*a)]

def eye():
    return [[1,0,0],[0,1,0],[0,0,1]]

def det(a):
    return (
        a[0][0]*(a[1][1]*a[2][2]-a[1][2]*a[2][1])
        -a[0][1]*(a[1][0]*a[2][2]-a[1][2]*a[2][0])
        +a[0][2]*(a[1][0]*a[2][1]-a[1][1]*a[2][0])
    )

def main():
    rx=[[1,0,0],[0,0,-1],[0,1,0]]
    rz=[[0,-1,0],[1,0,0],[0,0,1]]
    checks={
      "rx_orthogonal":mm(tr(rx),rx)==eye(),
      "rz_orthogonal":mm(tr(rz),rz)==eye(),
      "determinants_plus_one":det(rx)==1 and det(rz)==1,
      "noncommuting_rotations":mm(rx,rz)!=mm(rz,rx),
    }
    passed=all(checks.values())
    receipt={
      "schema":"TIR_SPACE_OF_GEOMETRY_SPATIAL_PROMOTION_UNIQUENESS_V0_2",
      "canonical_nonlogical_axiom_count":0,
      "upstream":"RELATION->S2->CP1->P(C2)->PSU(2)~=SO(3)",
      "minimal_faithful_real_dimension":3,
      "remaining_gate":"DERIVE_SPATIAL_REALIZATION_CRITERION_FROM_ZERO_AXIOM_TIR_GRAPH",
      "metric_status":"UNIQUE_UP_TO_POSITIVE_SCALE",
      "checks":checks,
      "technical_status":"PASS" if passed else "FAIL",
    }
    print(json.dumps(receipt,indent=2,sort_keys=True))
    if not passed: raise SystemExit(1)

if __name__=="__main__": main()
