#!/usr/bin/env python3
from __future__ import annotations
import json
import numpy as np

TOL=1e-10

def audit(name, group, order, weights, edges):
    d=np.asarray(weights,dtype=int)
    A=np.zeros((len(d),len(d)),dtype=int)
    for i,j in edges:
        A[i,j]=A[j,i]=1
    C=2*np.eye(len(d),dtype=float)-A
    null_res=A@d-2*d
    eig=np.linalg.eigvalsh(C)
    return {
      'affine_dynkin':name,
      'binary_group':group,
      'binary_group_order':order,
      'dimension_vector':d.tolist(),
      'sum_dimension_squares':int(np.sum(d*d)),
      'mckay_dimension_equation_residual':null_res.tolist(),
      'max_dimension_equation_residual':int(np.max(np.abs(null_res))),
      'affine_cartan_smallest_eigenvalue':float(eig[0]),
      'node_count':len(d),
      'edge_count':len(edges),
    }

def main():
    e6=audit('E6_tilde','2T',24,
      [3,2,2,2,1,1,1],
      [(0,1),(0,2),(0,3),(1,4),(2,5),(3,6)])
    e7=audit('E7_tilde','2O',48,
      [4,3,2,1,3,2,1,2],
      [(0,1),(1,2),(2,3),(0,4),(4,5),(5,6),(0,7)])
    e8=audit('E8_tilde','2I',120,
      [6,5,4,3,2,1,4,2,3],
      [(0,1),(1,2),(2,3),(3,4),(4,5),(0,6),(6,7),(0,8)])
    rows={'3':e6,'4':e7,'5':e8}
    checks={
      'orders_24_48_120':[rows[str(n)]['binary_group_order'] for n in (3,4,5)]==[24,48,120],
      'sum_squares_match_group_orders':all(r['sum_dimension_squares']==r['binary_group_order'] for r in rows.values()),
      'dimension_vectors_satisfy_2d_equals_Ad':all(r['max_dimension_equation_residual']==0 for r in rows.values()),
      'affine_cartan_has_numerical_zero_mode':all(abs(r['affine_cartan_smallest_eigenvalue'])<TOL for r in rows.values()),
    }
    out={
      'schema':'TIR-MCKAY-ADE-CLOSURE/0.1',
      'mapping':{'3':'2T <-> affine E6','4':'2O <-> affine E7','5':'2I <-> affine E8'},
      'rows':rows,
      'checks':checks,
      'verdict':'PASS' if all(checks.values()) else 'FAIL'
    }
    print(json.dumps(out,indent=2))
    return 0 if out['verdict']=='PASS' else 1

if __name__=='__main__':
    raise SystemExit(main())
