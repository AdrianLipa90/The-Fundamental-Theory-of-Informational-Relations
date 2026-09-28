#!/usr/bin/env python3
"""Zero-axiom audit for relational state-difference uniqueness v0.2."""
from __future__ import annotations
from fractions import Fraction
import json

RZ90=((0,-1,0),(1,0,0),(0,0,1))
RX90=((1,0,0),(0,0,-1),(0,1,0))

def idx(i,j): return 3*i+j

def constraint_rows(r):
    rows=[]
    for i in range(3):
        for j in range(3):
            row=[Fraction(0) for _ in range(9)]
            for k in range(3):
                row[idx(i,k)]+=Fraction(r[k][j])
                row[idx(k,j)]-=Fraction(r[i][k])
            rows.append(row)
    return rows

def matrix_rank(rows):
    a=[row[:] for row in rows]
    m=len(a); n=len(a[0]); rank=0; col=0
    while rank<m and col<n:
        pivot=next((i for i in range(rank,m) if a[i][col]!=0),None)
        if pivot is None:
            col+=1
            continue
        a[rank],a[pivot]=a[pivot],a[rank]
        p=a[rank][col]
        a[rank]=[x/p for x in a[rank]]
        for i in range(m):
            if i==rank: continue
            f=a[i][col]
            if f!=0:
                a[i]=[x-f*y for x,y in zip(a[i],a[rank])]
        rank+=1; col+=1
    return rank

def main():
    rank=matrix_rank(constraint_rows(RZ90)+constraint_rows(RX90))
    nullity=9-rank
    passed=(rank==8 and nullity==1)
    receipt={
      "schema":"TIR_RELATIONAL_STATE_DIFFERENCE_UNIQUENESS_V0_2",
      "canonical_nonlogical_axiom_count":0,
      "exact_result":"D(rho_x,rho_y)=lambda*(rho_y-rho_x)",
      "uniqueness":"UP_TO_NONZERO_GLOBAL_SCALE_AND_ORIENTATION",
      "remaining_zero_axiom_derivation_gates":[
        "RELATIONAL_AFFINE_ARITHMETIC_COMPATIBILITY",
        "ZERO_KERNEL_ENDPOINT_COMPOSITION_CLOSURE"
      ],
      "commutant_dimension":nullity,
      "technical_status":"PASS" if passed else "FAIL",
    }
    print(json.dumps(receipt,indent=2,sort_keys=True))
    if not passed: raise SystemExit(1)

if __name__=="__main__": main()
