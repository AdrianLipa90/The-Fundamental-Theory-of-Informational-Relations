# TIR Polygonal Excitation — Stage 38 C3 Character-Basis CP Gate v0.1

Status: `STAGE_38_C3_CHARACTER_BASIS_CP_MATH_PASS`

## Scope

This is a pure mathematical gate on the already frozen ordered three-family label space. It tests whether the canonical character basis of the Stage 24 cyclic family operator supplies a non-commuting complex basis relation with non-zero rephasing-invariant CP measure.

No CKM angles, observed particle masses, or fitted coefficients are used.

Physical assignment of the two basis choices to the up and down sectors remains open.

## Frozen cyclic family operator

Stage 24 defines the ordered family labels

```math
(s_1,s_2,s_3)=((3,5),(5,7),(11,13))
```

and the cyclic action

```math
P_s|s_1\rangle=|s_2\rangle,
\quad
P_s|s_2\rangle=|s_3\rangle,
\quad
P_s|s_3\rangle=|s_1\rangle.
```

Thus `P_s` is the regular three-cycle representation of `C3`.

## Canonical character basis

Let

```math
\omega=e^{2\pi i/3}.
```

The normalized character matrix of `C3` is

```math
\boxed{
F_3=\frac1{\sqrt3}
\begin{pmatrix}
1&1&1\\
1&\omega&\omega^2\\
1&\omega^2&\omega
\end{pmatrix}.
}
```

It is fixed by the character table of `C3` up to row/column phases and permutations.

The executable verifies

```math
F_3^\dagger P_s F_3
=
\operatorname{diag}(1,\omega^2,\omega)
```

with residual

```text
4.97e-16.
```

## Non-commuting family pair

Use a nondegenerate ordered family-axis representative

```math
K=\operatorname{diag}(3,4,5).
```

Define

```math
H_A=K,
\qquad
H_B=F_3 K F_3^\dagger.
```

Both are Hermitian. The transformed operator has Hermiticity residual of floating-point order `4.92e-17`.

Their commutator is non-zero:

```math
\boxed{
[H_A,H_B]\neq0
}
```

with

```text
max |[H_A,H_B]| = 1.154700538379253.
```

Thus the frozen `C3` character basis supplies a second family orientation independent of scalar functions of the ordered family axis.

## Rephasing-invariant complex structure

The matrix `F3` is unitary:

```text
max |F3^dagger F3-I| = 2.22e-16
```

and has unit determinant modulus to floating-point precision.

For the quartet

```math
Q=F_{11}F_{22}F_{12}^*F_{21}^*,
```

one obtains

```math
\arg Q=\frac{2\pi}{3}.
```

Therefore the complex phase is rephasing-invariant.

The associated Jarlskog-type invariant is exactly

```math
\boxed{
J_{F_3}=\frac1{6\sqrt3}
}
```

with numerical value

```text
0.09622504486493769
```

and exact-form residual `5.55e-17`.

## Result

The Stage 24 family cycle contains, through its canonical character basis, a parameter-free complex orientation that satisfies all mathematical requirements for a non-zero family CP invariant:

```text
C3 character diagonalization: PASS
non-commuting family orientation: PASS
unitarity: PASS
rephasing-invariant phase: PASS
J_F != 0: PASS
physical up/down sector assignment: OPEN
```

The result establishes a clean group-theoretic CP-capable mechanism on the TIR family carrier. It does not assign the character basis to a physical quark sector in this stage.

## Quantitative boundary

The character matrix has equal magnitudes

```math
|F_{3,ij}|=\frac1{\sqrt3}.
```

Accordingly it represents the maximally symmetric `C3` character transform. Any hierarchical family mixing requires an independently derived symmetry-breaking or weighting operator rather than adjustment of the `C3` character matrix itself.

## Reproducibility

Executable:

`TIR/frozen_predictions/validation/scripts/c3_character_basis_cp_stage38_v01.py`

Receipt:

`TIR/frozen_predictions/validation/results/TIR_POLYGONAL_STAGE38_C3_CHARACTER_BASIS_CP_RECEIPT_V0_1.json`

## Next gate

Derive a symmetry-breaking family operator from already frozen polygonal/McKay invariants and test whether it deforms the maximally symmetric `C3` character basis into a hierarchical unitary family transformation while retaining a non-zero rephasing-invariant phase. The deformation rule must be fixed independently of CKM target values.
