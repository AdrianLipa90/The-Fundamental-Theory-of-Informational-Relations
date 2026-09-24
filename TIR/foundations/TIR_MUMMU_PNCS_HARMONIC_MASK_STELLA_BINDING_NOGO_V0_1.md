# TIR MUMMU PNCS Harmonic-Mask to Stella-Shell Binding No-Go v0.1

Status: `EXACT_MASK_MULTIPLICITY_AUDIT / EIGHT_REGULAR_CLASSES_FOUND / HAMMING_CUBE_ISOMORPHISM_FAIL / LINEAR_GF2_QUOTIENT_INJECTION_FAIL / STELLA_SHELL_BINDING_OPEN`

Date: 2026-09-23

## 1. Purpose

The Stella adaptive-coupling quartic crosswalk requires a typed map from source
PNCS coupling/channel structure to eight canonical Stella relation directions.

The PNCS HTRI source contains 36 harmonic-channel masks in

`semantic_htri_drive_v32.py`.

Their multiplicities show a suggestive

[
36=8	imes3+2	imes6
]

split.

This theorem tests whether the eight multiplicity-three mask classes already
carry a canonical cube/Stella combinatorics.

They do not.

## 2. Source mask set

Each PNCS channel carries a four-bit harmonic mask

[
minmathbb F_2^4.
]

The 36 channels contain ten unique masks.

Eight classes occur with multiplicity three:

[
oxed{
mathcal R=
{
0011,,
0101,,
0110,,
1001,,
1010,,
1011,,
1100,,
1101
}.
}
]

Two exceptional classes occur with multiplicity six:

[
oxed{
mathcal X=
{
1110,,
1111
}.
}
]

Thus

[
oxed{
36
=
8cdot3
+
2cdot6.
}
]

The split is exact source combinatorics.

## 3. Why cardinality eight is insufficient

The Stella shell is naturally the cube-vertex set

[
{pm1}^3,
]

whose one-bit adjacency graph is the 3-cube (Q_3).

Every cube vertex has degree three.

Use Hamming-distance-one adjacency on the eight regular source masks
(mathcal R).

Their degree sequence is

[
oxed{
(1,1,0,2,1,3,1,3)
}
]

in the source ordering above, or sorted,

[
oxed{
(0,1,1,1,1,2,3,3).
}
]

This differs from

[
oxed{
(3,3,3,3,3,3,3,3)
}
]

for (Q_3).

Therefore

[
oxed{
G_H(mathcal R)

otcong
Q_3.
}
]

The eight regular classes are not already a Hamming cube.

## 4. Coordinate-deletion no-go

A simple candidate map would delete one of the four harmonic bits and interpret
the remaining three bits as cube coordinates.

For the four possible deleted coordinates, the number of distinct projected
three-bit words is

[
oxed{
6, 7, 7, 6.
}
]

None is eight.

Therefore no coordinate deletion yields a bijection

[
mathcal R	omathbb F_2^3.
]

## 5. Stronger linear-quotient no-go

Any surjective linear map

[
L:mathbb F_2^4	omathbb F_2^3
]

has a one-dimensional kernel

[
ker L={0,v}
]

for some nonzero

[
vinmathbb F_2^4.
]

The restriction of (L) to (mathcal R) is injective iff no two regular masks
differ by (v).

But the exact difference set satisfies

[
oxed{
{r_ioplus r_j:i<j, r_i,r_jinmathcal R}
=
mathbb F_2^4setminus{0}.
}
]

Every nonzero candidate kernel vector occurs as a pair difference.

Hence every rank-three linear quotient identifies at least one pair in
(mathcal R).

Therefore

[
oxed{

exists,
L:mathbb F_2^4	omathbb F_2^3
	ext{ linear with }
L|_{mathcal R}
	ext{ bijective}.
}
]

The same obstruction applies to affine maps because translation does not change
pair differences.

## 6. Exceptional classes do not repair the cube

The multiplicity-six classes

[
1110,qquad1111
]

are source-distinguished by mask and Hamming weight.

It is tempting to interpret

[
8 	ext{regular classes}
+
2 	ext{exceptional classes}
]

as

[
8 	ext{Stella directions}
+
2 	ext{poles}.
]

The source data do not justify that typing.

The failure of the regular eight to carry canonical cube combinatorics remains,
and no source contract labels the two exceptional masks as geometric poles.

Thus the (8+2) count is an exact observation, not a spatial promotion.

## 7. Consequence for the Stella adaptive crosswalk

The conditional theorem

[
-partial_{ar g}mathcal F_H
=
lambda_H S_{m Stella}(q)
]

remains mathematically exact once a Stella-shell binding is admitted.

However the current PNCS harmonic-mask table does not itself supply that
binding.

Therefore:

[
oxed{
	ext{36-channel harmonic masks}

otRightarrow
	ext{canonical Stella shell}.
}
]

A valid source binding requires additional invariant structure.

## 8. Minimal acceptable binding

A future map

[
mathcal B_{m shell}
:
	ext{PNCS local source sectors}
	o
mathcal V_{m Stella}
]

must be justified by at least one source-preserving invariant beyond
cardinality/multiplicity, for example:

- an exact adjacency/incidence isomorphism;
- a source-derived group action with the cube/Stella orbit;
- a canonical relational-vector construction in
  (operatorname{Herm}_0(2));
- an independently frozen physical/source edge receipt.

No arbitrary enumeration of the eight regular masks is admitted.

## 9. Claim ledger

| Statement | Status |
|---|---|
| source has ten unique harmonic-mask classes | `EXACT` |
| multiplicities split as (8	imes3+2	imes6) | `EXACT` |
| eight regular classes form Hamming cube (Q_3) | `FAIL` |
| deleting one source bit produces eight unique 3-bit classes | `FAIL` |
| rank-three GF(2) linear quotient can biject regular classes to cube | `FAIL / EXACT NO-GO` |
| two exceptional classes are physical/geometric poles | `OPEN / NOT CLAIMED` |
| native PNCS harmonic-mask → Stella-shell binding exists | `OPEN` |
| conditional Stella adaptive-coupling crosswalk remains valid | `PASS WITH EXPLICIT BINDING PREMISE` |

## 10. Validation

Deterministic validator:

`TIR/validation/tir_mummu_pncs_harmonic_mask_stella_binding_nogo_v0_1.py`

Static receipt:

`TIR/validation/TIR_MUMMU_PNCS_HARMONIC_MASK_STELLA_BINDING_NOGO_VALIDATION_V0_1.json`
