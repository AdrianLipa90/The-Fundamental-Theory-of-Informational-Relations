# TIR Polygonal Excitation — Stage 23 Chirality Intertwiner v0.1

Status: `STAGE_23_Z2_INTERTWINER_PASS_WITH_ORIENTATION_CONVENTION`

## Inputs already present in TIR

The weak-axis line uses a CP1/Bloch two-pole selector and carries chirality as a structural channel. The one-generation representation line uses the left-handed Weyl convention.

Stage 19 supplies the exceptional conjugate pair

```math
27\leftrightarrow\overline{27}
```

and, at the E8 level,

```math
(27,3)\leftrightarrow(\overline{27},\overline3).
```

## Two-state label representations

Use the ordered TIR pole basis

```math
\{|N\rangle,|S\rangle\}
```

with pole-exchange involution

```math
J_\chi=
\begin{pmatrix}
0&1\\
1&0
\end{pmatrix},
\qquad J_\chi^2=I_2.
```

Use the ordered exceptional branch basis

```math
\{|27\rangle,|\overline{27}\rangle\}
```

with conjugation-label involution

```math
C_E=
\begin{pmatrix}
0&1\\
1&0
\end{pmatrix},
\qquad C_E^2=I_2.
```

Define the convention-fixed label map

```math
F|N\rangle=|27\rangle,
\qquad
F|S\rangle=|\overline{27}\rangle.
```

In these ordered bases, `F=I2`, and therefore

```math
\boxed{FJ_\chi=C_EF}
```

exactly.

## Orientation degeneracy

The swapped map `F'=X2` also intertwines the same two abstract Z2 representations. The existing left-handed Weyl convention fixes which exceptional branch is used as the active matter-carrier label in this stage. This is a convention-level orientation choice.

## Result

The TIR CP1 two-pole label involution and the exceptional `27/bar(27)` conjugation label involution are equivalent Z2 representations. The intertwining residual is exactly zero in integer arithmetic.

Dynamical chirality selection / matter-antimatter asymmetry remains an independent physical gate; this stage establishes the representation interface used by the next six-state composition test.

## Reproducibility

`TIR/frozen_predictions/validation/scripts/chirality_intertwiner_stage23_v01.py`
