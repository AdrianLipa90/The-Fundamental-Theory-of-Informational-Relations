# TIR Polygonal Excitation — Stage 44 Collatz Product-Seed Intersection Geometry v0.1

Status: `STAGE_44_COLLATZ_PRODUCT_SEED_INTERSECTION_PASS`

## Scope

This gate uses the pre-existing foundational scalar-seed rule

```math
n_0=p(p+2)
```

for the already ordered twin-prime family labels

```math
(3,5),\qquad(5,7),\qquad(11,13).
```

No bounded rhythm ansatz, `eta`, CKM element, mass, or fitted coefficient is used.

## Scalar seeds

The exact scalar seeds are

```math
n_1=15,\qquad n_2=35,\qquad n_3=143.
```

Their ordinary Collatz stopping lengths are

```text
15  -> 17 steps
35  -> 13 steps
143 -> 103 steps
```

## Pairwise orbit meeting metric

For two scalar seeds `a,b`, compute their complete Collatz orbits to `1`. Among all common nodes choose the node minimizing

```math
d(a,b)=k_a+k_b,
```

where `k_a,k_b` are the directed step indices at which the two orbits reach that common node. Maximum individual step and node value are used only as exact-tie breakers.

This is a discrete orbit-intersection metric with no continuous parameter.

## Exact meetings

### Family 1 and 2

The orbits first meet optimally at

```math
35
```

with step counts

```text
15 -> 35 : 4 steps
35 -> 35 : 0 steps
```

so

```math
\boxed{d_{12}=4.}
```

### Family 1 and 3

The optimal common node is

```math
46
```

with

```text
15  -> 46 : 1 step
143 -> 46 : 87 steps
```

hence

```math
\boxed{d_{13}=88.}
```

### Family 2 and 3

The optimal common node is

```math
35
```

with

```text
35  -> 35 : 0 steps
143 -> 35 : 90 steps
```

hence

```math
\boxed{d_{23}=90.}
```

The exact meeting-distance matrix is therefore

```math
\boxed{
D_C=
\begin{pmatrix}
0&4&88\\
4&0&90\\
88&90&0
\end{pmatrix}.
}
```

## Structural hierarchy

The ratios are

```math
\frac{d_{13}}{d_{12}}=22,
\qquad
\frac{d_{23}}{d_{12}}=22.5.
```

Thus the exact product-seed Collatz geometry contains the discrete hierarchy

```math
\boxed{d_{12}\ll d_{13}\simeq d_{23}.}
```

This independently reinforces the Stage 41 result that the `1<->2` family channel is structurally distinguished.

## Orbit-overlap control

The orbit-set Jaccard overlaps are

```text
Jaccard(1,2) = 0.7777777778
Jaccard(1,3) = 0.1619047619
Jaccard(2,3) = 0.1346153846
```

so the same channel hierarchy is visible in orbit-set overlap as well as meeting distance.

## Evidential status

```text
product scalar-seed rule: PRE-EXISTING
Collatz transitions: EXACT INTEGER DYNAMICS
continuous rhythm parameter: NONE
CKM input: NONE
mass input: NONE
family 1<->2 orbital proximity: STRONGLY DISTINGUISHED
mapping from distance to physical mixing amplitude: OPEN
```

The distance matrix is retained as a structural object. This stage does not identify `1/d_ij`, the Jaccard overlap, or any other function of the orbit data with a CKM element.

## Reproducibility

Executable:

`TIR/frozen_predictions/validation/scripts/collatz_product_seed_intersection_stage44_v01.py`

Receipt:

`TIR/frozen_predictions/validation/results/TIR_POLYGONAL_STAGE44_COLLATZ_PRODUCT_SEED_INTERSECTION_RECEIPT_V0_1.json`

## Next gate

Determine whether TIR already contains a general graph/holonomy rule that converts a discrete transition distance or path cost into an operator amplitude. If such a rule exists independently, apply it to `D_C` without modifying its functional form. If no such rule exists, freeze candidate kernels as separate hypotheses before any CKM comparison rather than selecting a kernel by fit.
