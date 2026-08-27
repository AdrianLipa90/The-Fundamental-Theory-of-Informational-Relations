# TIR Polygonal Excitation — Stage 56 Platonic Spin-2 Restriction v0.1

Status: `STAGE_56_N5_ICOSAHEDRAL_SPIN2_IRREDUCIBILITY_PASS`

## Purpose

Stage 55 identifies the five-dimensional family complement as the spin-two (`l=2`) representation of the embedded rotational `SO(3)`. Stage 56 tests whether the number five has a representation-theoretic relation to the frozen polygon levels `N=3,4,5`.

The test restricts the same `l=2` representation to the rotational symmetry groups of the three finite spherical closures:

```math
N=3:\ A_4,
\qquad
N=4:\ S_4,
\qquad
N=5:\ A_5.
```

No particle, CKM, or mass information is used.

## Spin-two character

For an `SO(3)` rotation through angle `theta`, the spin-two character is

```math
\chi_2(\theta)
=\frac{\sin(5\theta/2)}{\sin(\theta/2)}
=1+2\cos\theta+2\cos2\theta.
```

The values needed for the Platonic rotation classes are

```text
theta = 0       -> chi_2 =  5
theta = pi      -> chi_2 =  1
theta = 2pi/3   -> chi_2 = -1
theta = pi/2    -> chi_2 = -1
theta = 2pi/5   -> chi_2 =  0
theta = 4pi/5   -> chi_2 =  0
```

## N=3 tetrahedral restriction

The rotational tetrahedral group `A4` has class-angle multiplicities

```text
1 x 0,
3 x pi,
8 x 2pi/3.
```

Hence

```math
\langle\chi,\chi\rangle_{A_4}
=\frac{25+3+8}{12}=3.
```

The restriction is reducible. Over the complex irreducible representations it is

```math
\boxed{\mathbf5\downarrow A_4=\mathbf1'\oplus\mathbf1''\oplus\mathbf3.}
```

The conjugate one-dimensional pair combines to a real two-dimensional sector, giving real form `2 + 3`.

## N=4 octahedral restriction

The rotational octahedral group is isomorphic to `S4`. Its relevant rotation classes have multiplicities

```text
1 x 0,
3 x pi,
6 x pi,
8 x 2pi/3,
6 x pi/2.
```

Therefore

```math
\langle\chi,\chi\rangle_{S_4}
=\frac{25+3+6+8+6}{24}=2.
```

The character has zero trivial multiplicity, and the exact decomposition is

```math
\boxed{\mathbf5\downarrow S_4=\mathbf2\oplus\mathbf3.}
```

Thus the five-dimensional spin-two carrier splits under the octahedral symmetry.

## N=5 icosahedral restriction

The rotational icosahedral group is `A5`. Its conjugacy-class angle multiplicities are

```text
1 x 0,
15 x pi,
20 x 2pi/3,
12 x 2pi/5,
12 x 4pi/5.
```

The restricted character is therefore

```text
(5, 1, -1, 0, 0).
```

Its character norm is

```math
\boxed{
\langle\chi,\chi\rangle_{A_5}
=\frac{25+15+20}{60}=1.
}
```

A finite-group character has norm one exactly when the representation is irreducible. Hence

```math
\boxed{
\mathbf5\downarrow A_5=\mathbf5_{\rm irr}.
}
```

The full Stage 55 five-dimensional spin-two complement remains irreducible under the `N=5` icosahedral rotation group.

## Binary-group consistency

Stages 11 and 14 use the binary Platonic groups `2T`, `2O`, `2I`. Because the present carrier has integer spin `l=2`, the central element `-I` of the binary cover acts trivially. Therefore the restriction factors through

```math
2T/\mathbb Z_2=A_4,
\qquad
2O/\mathbb Z_2=S_4,
\qquad
2I/\mathbb Z_2=A_5.
```

This is compatible with the earlier binary-group/McKay chain.

## Result

Among the three finite spherical levels, `N=5` is distinguished by an exact representation property:

```math
\boxed{
\text{the five-dimensional }SU(3)/SO(3)\text{ tangent carrier remains irreducible under }A_5.
}
```

At `N=3` and `N=4` the same carrier splits into smaller invariant sectors.

This establishes a genuine representation-theoretic bridge between the frozen `N=5` icosahedral geometry and the five-dimensional complement found independently in Stages 53--55.

## Boundary

The result identifies matching representation structure. It does not assign the `A5` five-dimensional irrep to a physical particle multiplet and does not by itself derive a CKM matrix or CP phase.

## Reproducibility

`TIR/frozen_predictions/validation/scripts/platonic_spin2_restriction_stage56_v01.py`

Receipt:

`TIR/frozen_predictions/validation/results/TIR_POLYGONAL_STAGE56_PLATONIC_SPIN2_RESTRICTION_RECEIPT_V0_1.json`
