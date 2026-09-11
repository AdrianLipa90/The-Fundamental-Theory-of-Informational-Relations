# TIR Platonic L-Constant Closure v0.1

Status: `TIR_INTERNAL_STRUCTURAL_DERIVATION`  
Date: 2026-09-10  
Scope: exact finite-group/combinatorial closure inside TIR.  
Physical claim: none. This document does **not** identify the construction with a physical law by itself and does **not** claim a derivation from \(CP^3\) Kähler geometry.

## 1. Problem

TIR uses the discrete structural constants

\[
(L_3,L_4,L_5)=(7,2,5).
\]

Historically these values had separate arithmetic provenance:

\[
L_3=\operatorname{depth}_{\rm Collatz}(3)=7,\qquad
L_4=5-3=2,\qquad
L_5=5.
\]

The open structural question was whether the same triple can be obtained from an independent geometric/group-theoretic construction rather than being retained only as three disconnected assignments.

## 2. Platonic classification fixes the index alphabet \(3,4,5\)

For a convex regular polyhedron with Schläfli symbol \(\{p,q\}\),

\[
\frac1p+\frac1q>\frac12,\qquad p,q\ge3.
\]

The integer solutions are exactly

\[
\boxed{
\{3,3\},\{3,4\},\{3,5\},\{4,3\},\{5,3\}.
}
\]

Therefore the complete index alphabet of the Platonic classification is

\[
\boxed{\{3,4,5\}}.
\]

The triangular-face branch is

\[
\boxed{
\{3,3\},\{3,4\},\{3,5\}.
}
\]

Its orientation-preserving rotational groups are

\[
G_3\simeq A_4,\qquad
G_4\simeq S_4,\qquad
G_5\simeq A_5,
\]

with

\[
|A_4|=12,\qquad |S_4|=24,\qquad |A_5|=60.
\]

Equivalently, for the spherical triangle groups \((2,3,q)\),

\[
|G_q|
=
\frac{2}{
\frac12+\frac13+\frac1q-1
}
=
\frac{12q}{6-q},
\qquad q\in\{3,4,5\},
\]

which yields \(12,24,60\).

## 3. Common tetrahedral root and exact subgroup indices

The tetrahedral rotational group \(A_4\) is a subgroup of both extension groups:

\[
A_4\triangleleft S_4,
\]

and an \(A_4\) subgroup of \(A_5\) is obtained as the stabilizer of one point in the natural five-point action of \(A_5\).

Hence the two exact subgroup indices are

\[
\boxed{
[S_4:A_4]=\frac{24}{12}=2
}
\]

and

\[
\boxed{
[A_5:A_4]=\frac{60}{12}=5.
}
\]

These are not fitted numbers.

Define the two Platonic extension coset spaces over the tetrahedral root

\[
X_4:=S_4/A_4,
\qquad
X_5:=A_5/A_4.
\]

Then

\[
|X_4|=2,\qquad |X_5|=5.
\]

TIR therefore identifies

\[
\boxed{
L_4:=|X_4|=2,
\qquad
L_5:=|X_5|=5.
}
\]

## 4. Root-extension closure gives \(L_3=7\)

The TIR root-extension closure rule is:

> For the tetrahedral root, the complete non-self-dual Platonic extension carrier is the disjoint union of all admissible extension coset spaces.

Thus

\[
X_3^{\rm closure}:=X_4\sqcup X_5.
\]

Because the union is disjoint,

\[
|X_3^{\rm closure}|
=
|X_4|+|X_5|
=
2+5
=
7.
\]

Therefore

\[
\boxed{
L_3:=|X_3^{\rm closure}|=7.
}
\]

The full TIR structural triple is consequently

\[
\boxed{
(L_3,L_4,L_5)
=
\left(
|S_4/A_4|+|A_5/A_4|,
|S_4/A_4|,
|A_5/A_4|
\right)
=
(7,2,5).
}
\]

This is an exact consequence of standard finite-group facts plus the explicit TIR root-extension closure rule. The closure rule is a TIR structural definition; the values following from it are not fitted.

## 5. Independent arithmetic crosscheck

The group-theoretic derivation reproduces the pre-existing arithmetic values without using them as inputs:

\[
\operatorname{depth}_{\rm Collatz}(3)=7=L_3,
\]

\[
5-3=2=L_4,
\]

\[
5=L_5.
\]

Thus the two provenance paths are

\[
\boxed{
\text{Platonic/group path}
\longrightarrow
(7,2,5)
}
\]

and

\[
\boxed{
\text{Collatz/twin-prime path}
\longrightarrow
(7,2,5).
}
\]

Their numerical agreement is an independent structural crosscheck inside TIR.

## 6. 3-4-5 symmetry-order identities

The Platonic index triple also satisfies

\[
3^2+4^2=5^2,
\]

and the same three integers recover the symmetry orders:

\[
\boxed{3+4+5=12=|A_4|},
\]

\[
\boxed{2(3+4+5)=24=|S_4|},
\]

\[
\boxed{3\cdot4\cdot5=60=|A_5|}.
\]

These are exact crosschecks. They are **not** used as derivation steps for \((L_3,L_4,L_5)\).

## 7. Claim classification

The epistemic split is:

- Platonic classification, group orders, subgroup embeddings and subgroup indices: standard mathematics (`A` in the TIR claim hierarchy).
- Tetrahedral-root extension closure \(X_3^{\rm closure}=X_4\sqcup X_5\): explicit TIR structural rule (`B` / `D_TIR` parent).
- \((L_3,L_4,L_5)=(7,2,5)\) from that rule: exact TIR-internal derived structural quantity (`D_TIR`).
- Collatz/twin-prime recovery of the same values: independent TIR arithmetic provenance/crosscheck.
- Any identification of these integers with measured particle-physics observables remains sector-specific and keeps its existing evidence classification.
- A derivation specifically from \(CP^3\) Kähler geometry remains open unless a separate map from this finite Platonic/coset construction into that geometry is proved.

## 8. Validator

Exact validator:

`TIR/validation/tir_platonic_l_constants_closure_v0_1.py`

The validator independently enumerates:

1. the five Schläfli pairs,
2. \(S_4\), \(A_4\), and \(A_5\) as permutation groups,
3. the embedded \(A_4\subset A_5\),
4. the left-coset partitions,
5. the subgroup indices \(2\) and \(5\),
6. the closure cardinality \(7\),
7. the Collatz/twin-prime and 3-4-5 crosschecks.

Expected result:

```text
status = PASS
L3 = 7
L4 = 2
L5 = 5
[S4:A4] = 2
[A5:A4] = 5
```

## 9. Canonical compact form

\[
\boxed{
\{3,3\},\{3,4\},\{3,5\}
\;\longrightarrow\;
A_4,S_4,A_5
\;\longrightarrow\;
[S_4:A_4]=2,\ [A_5:A_4]=5
}
\]

\[
\boxed{
X_3^{\rm closure}
=
S_4/A_4\sqcup A_5/A_4
}
\]

\[
\boxed{
(L_3,L_4,L_5)=(7,2,5).
}
\]
