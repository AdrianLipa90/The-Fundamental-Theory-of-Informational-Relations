# TIR Polygonal Excitation — Stage 47 Directed Collatz Family Merge v0.1

Status: `STAGE_47_DIRECTED_COLLATZ_FAMILY_MERGE_PASS`

## Purpose

Stage 44 used a symmetric first-common-orbit distance. Stage 47 restores the direction of the deterministic Collatz map and asks whether one frozen family seed lies on the future orbit of another.

The scalar seeds are already fixed by the pre-existing product convention

```math
n_1=3\cdot5=15,\qquad
n_2=5\cdot7=35,\qquad
n_3=11\cdot13=143.
```

Define

```math
T_{i\to j}=\min\{k\ge0:C^k(n_i)=n_j\},
```

with `T=∞` if the target seed is never reached on the forward orbit.

## Exact directed reachability

Direct enumeration gives

```math
\boxed{
T=\begin{pmatrix}
0&4&\infty\\
\infty&0&\infty\\
\infty&90&0
\end{pmatrix}.
}
```

Hence

```math
C^4(15)=35,
```

and

```math
C^{90}(143)=35.
```

Neither `35` nor `143` reaches `15`, and neither `15` nor `35` reaches `143`.

Therefore `n2=35` is the unique member of the frozen three-seed set that is reached by both other seeds under forward Collatz evolution.

## Pairwise first merge nodes

For two starting values `a,b`, define the first merge node as the common orbit value minimizing the total forward-step cost.

The exact pairwise results are

```text
(15,35): merge node 35, step indices (4,0), total cost 4
(15,143): merge node 46, step indices (1,87), total cost 88
(35,143): merge node 35, step indices (0,90), total cost 90
```

The non-seed merge node satisfies

```math
C(15)=46,
```

and

```math
C^3(46)=35.
```

Thus the two outer seeds `15` and `143` merge at `46` before the common tail reaches the middle seed `35` three steps later.

## Seed-level directed graph

Discarding self-loops, the induced directed reachability graph on the frozen seed set is

```text
n1 -> n2 <- n3
```

with exact forward lengths `4` and `90` respectively.

This is a parameter-free orientation already present in the raw Collatz dynamics.

## Result

The symmetric Stage 44 distance matrix hides a stronger directed statement:

```math
\boxed{n_2=35\text{ is the unique common forward-reachable seed of the three-seed family set}.}
```

The first/third sectors also have a unique earlier merge at `46`, after which their common trajectory reaches `35`.

## Boundary

This stage establishes only deterministic orbit topology and directed step counts. It does not identify `n2` with a physical preferred generation, does not derive a CKM amplitude, and does not introduce a distance-to-coupling rule.

## Reproducibility

`TIR/frozen_predictions/validation/scripts/directed_collatz_family_merge_stage47_v01.py`

Receipt:

`TIR/frozen_predictions/validation/results/TIR_POLYGONAL_STAGE47_DIRECTED_COLLATZ_FAMILY_MERGE_RECEIPT_V0_1.json`
