# TIR Polygonal Excitation — Stage 46 Low-Complexity Distance Identity Audit v0.1

Status: `STAGE_46_LOW_COMPLEXITY_IDENTITY_AUDIT_PASS_WITH_NONUNIQUENESS_BOUNDARY`

## Purpose

Stage 44 established the exact Collatz meeting-distance matrix for the three frozen scalar family seeds

```math
n_1=3\cdot5=15,\qquad n_2=5\cdot7=35,\qquad n_3=11\cdot13=143,
```

with

```math
D_C=\begin{pmatrix}
0&4&88\\
4&0&90\\
88&90&0
\end{pmatrix}.
```

Stage 46 tests whether the three nonzero distances admit unusually low-complexity exact expressions in the already frozen structural integers

```math
L_3=7,\qquad L_4=2,\qquad L_5=5.
```

This is an arithmetic multiplicity audit only. It does not promote any distance-to-amplitude law.

## Frozen search class

Before inspecting target multiplicities, enumerate all fully parenthesized expressions built from leaves

```text
L3, L4, L5
```

with repetition allowed, binary operations

```text
+, -, *, /
```

and at most three binary operations.

Exact rational arithmetic is used. Division by zero is excluded. For the commutative operations `+` and `*`, operand order is canonicalized lexically to suppress trivial left-right duplicates. Parenthesization remains explicit, so the audit still records distinct expression-tree forms.

## Exact results

### Distance d12 = 4

The value `4` is highly non-unique in this search class. Examples include

```math
L_4L_4=4,
```

```math
L_4+L_4=4,
```

```math
(L_3-L_5)L_4=4,
```

and many further identities.

Therefore Stage 46 does not select a unique structural expression for `d12`.

### Distance d13 = 88

Exactly one canonical expression-tree hit occurs within the frozen search class:

```math
\boxed{d_{13}=(L_3^2-L_5)L_4=88.}
```

No second expression using at most three operations survives the stated enumeration rule.

### Distance d23 = 90

Five canonical expression-tree hits occur:

```math
(L_3+L_4)(L_4L_5),
```

```math
(L_5^2-L_3)L_5,
```

```math
((L_3+L_4)L_5)L_4,
```

```math
((L_3+L_4)L_4)L_5,
```

```math
(L_3+L_4)(L_5+L_5).
```

The first, third and fourth are the same symbolic monomial after associativity/commutativity of multiplication:

```math
\boxed{L_4L_5(L_3+L_4)=90.}
```

The fifth coincides numerically because `L4=2`, while the second is a separate low-complexity identity:

```math
L_5(L_5^2-L_3)=90.
```

Thus `d23` has several low-complexity descriptions and is not unique in the same sense as `d13`.

## Result

The audit establishes:

```text
d12 = 4  -> strongly non-unique low-complexity arithmetic value
d13 = 88 -> unique hit in the frozen <=3-operation search class
d23 = 90 -> multiple low-complexity hits
```

The strongest arithmetic selectivity is therefore attached to `d13=88` under this explicitly frozen grammar.

## Boundary

The search grammar is finite and intentionally narrow. Uniqueness inside this grammar is not a theorem of unrestricted arithmetic expression complexity.

No formula in this stage is promoted as a physical coupling, amplitude, probability or mass rule. Stage 45 remains controlling: the repository currently has no canonical Collatz-distance-to-amplitude map.

## Reproducibility

`TIR/frozen_predictions/validation/scripts/low_complexity_distance_identity_stage46_v01.py`

Receipt:

`TIR/frozen_predictions/validation/results/TIR_POLYGONAL_STAGE46_LOW_COMPLEXITY_DISTANCE_IDENTITY_RECEIPT_V0_1.json`
