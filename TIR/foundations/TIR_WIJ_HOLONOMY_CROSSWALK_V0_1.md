# TIR W_ij Holonomy Crosswalk v0.1

Status: `SOURCE_BOUND_EXACT_CROSSWALK_CANDIDATE / SPATIAL_SE3_TORSION_SOURCE_CROSSWALK_ADDED`

Date: 2026-08-29

## 1. Purpose

This note unifies the existing `W_ij` objects used in the White-Thread, spatial-transport and Standard-Model branches into one typed holonomy family. The purpose is source binding and type normalization before GREMLIN performs tetrahedral/global gluing search.

## 2. Generic transport object

Let `G` be the structure group of the active sector, `R` a unitary representation and `A_R` the corresponding connection along an oriented path `gamma_ij` from node `j` to node `i`.

The common transport form is

\[
\boxed{
W_{ij}^{(G,R)}
=\mathcal P\exp\!\left(\int_{\gamma_{ij}} A_R\right).
}
\]

For a one-dimensional Abelian phase representation this reduces, after the conventional factor of `i` is included in the connection normalization, to

\[
\boxed{
W_{ij}=\exp\!\left(i\int_{\gamma_{ij}}A\right).
}
\]

For unitary transport,

\[
\boxed{W_{ji}=W_{ij}^{-1}=W_{ij}^{\dagger}.}
\]

Under local frame changes `G_i,G_j`,

\[
\boxed{
W_{ij}\mapsto G_iW_{ij}G_j^{-1}.
}
\]

In unitary representations this is

\[
W_{ij}\mapsto G_iW_{ij}G_j^{\dagger}.
\]

## 3. Sector typing

### White-Thread phase transport

The correlation/phase branch uses an Abelian open-path holonomy,

\[
W_{ij}^{WT}=\exp\!\left(i\int_{\gamma_{ij}}A_{WT}\right)\in U(1).
\]

Its modulus and relative phase feed the bounded White-Thread coupling function.

### Spatial relation transport

The local spatial carrier is

\[
\operatorname{Herm}_0(2)\cong\mathbb R^3.
\]

A spin-frame link is represented by

\[
W_{ij}^{X}\in SU(2),
\]

with induced vector-frame action

\[
\boxed{
R_{ij}=\operatorname{Ad}_{W_{ij}^{X}}\in SO(3).
}
\]

The transported relation vector is

\[
\mathcal E\mapsto
W_{ij}^{X}\mathcal E(W_{ij}^{X})^{\dagger}.
\]

### Colour / gluon transport

The Standard-Model holonomic gluon module uses

\[
\boxed{W_{ij}^{c}\in SU(3),}
\]

with

\[
W_{ji}^{c}=(W_{ij}^{c})^{\dagger},
\qquad
W_{ij}^{c}\mapsto G_iW_{ij}^{c}G_j^{\dagger}.
\]

The elementary triplet loop is

\[
\boxed{
U_{012}=W_{01}^{c}W_{12}^{c}W_{20}^{c}.
}
\]

Its traceless anti-Hermitian/Hermitian projection carries the local `su(3)` curvature content.

## 4. Loop object

For any composable oriented loop

\[
\gamma=(i_0i_1)(i_1i_2)\cdots(i_{m-1}i_0),
\]

define

\[
\boxed{
W_{\gamma}
=W_{i_0i_1}W_{i_1i_2}\cdots W_{i_{m-1}i_0}.
}
\]

The conjugacy class of `W_gamma` is the gauge-covariant loop datum. In the Abelian case this reduces to the accumulated loop phase. In the non-Abelian cases it carries the finite holonomy/curvature defect.

## 5. Spatial endpoint-closure interface

For local relation vectors `E_xy` and spatial transport `W_xy^X`, define the transported endpoint defect

\[
\boxed{
\mathcal C_{xyz}
=
\mathcal E_{xz}
-
\left(
\mathcal E_{xy}
+
W_{xy}^{X}\mathcal E_{yz}(W_{xy}^{X})^{\dagger}
\right).
}
\]

The spatial affine-torsor parent supplies

\[
\boxed{
\mathbf e_{xy}=\operatorname{vec}(\mathcal E_{xy})
}
\]

and the spatial connection supplies

\[
\boxed{
R_{xy}=\operatorname{Ad}(W_{xy}^{X}).
}
\]

The Gate-A source theorem packages them as

\[
\boxed{
G_{xy}^{\nabla}=(R_{xy},\mathbf e_{xy})\in SE(3).
}
\]

On a rotationally consistent triangle,

\[
R_{xz}=R_{xy}R_{yz},
\]

the closed affine loop obeys

\[
\boxed{
R_C=I,
\qquad
\mathbf t_C=-\operatorname{vec}(\mathcal C_{xyz}).
}
\]

The discrete relational solder form gives the exact companion identity

\[
\boxed{
\mathcal T_{xyz}=-\mathcal C_{xyz},
}
\]

so

\[
\boxed{
\mathbf t_C=\operatorname{vec}(\mathcal T_{xyz}).
}
\]

Canonical source-resolution theorem:

`TIR/foundations/TIR_UNIVERSAL_LOOP_TORSION_SOURCE_BINDING_V0_1.md`.

## 6. GREMLIN input contract

GREMLIN receives the following typed graph as a candidate-generation surface:

```text
local tetrahedral cell
  -> oriented relation edges E_ij
  -> W_ij^X spatial connection transport
  -> G_ij^nabla=(Ad(W_ij^X),vec(E_ij))
  -> loop rotational holonomy
  -> loop translation = vec(T_triangle)
  -> continuum curvature/torsion refinement candidates
```

Candidate promotion requires a deterministic theorem or validator receipt.

## 7. Source provenance

Primary source surfaces in the project/library include:

- `White_threads(1).pdf`: open-path holonomy `W_ij = exp(i integral_gamma A)` and White-Thread coupling dependence on holonomy amplitude/phase;
- `METATIME_SM_HOLONOMIC_GLUON_WIJ_v4_0.md`: `SU(3)`-valued `W_ij`, dagger reversal, local gauge covariance, loop holonomy and `su(3)` curvature projection;
- TIR affine relation/endpoint branch: `Herm_0(2)` intrinsic relation displacement;
- `TIR_DISCRETE_SOLDER_FORM_V0_1.md`: discrete solder/torsion object;
- `TIR_SE3_GLOBAL_GLUE_HOLONOMY_V0_1.md`: affine loop holonomy;
- `TIR_UNIVERSAL_LOOP_TORSION_SOURCE_BINDING_V0_1.md`: exact endpoint-defect / discrete-solder / SE(3) loop-translation crosswalk.

## 8. Current result

The `W_ij` symbol is a typed family of connection holonomies:

\[
\boxed{
W_{ij}^{WT}\in U(1),
\qquad
W_{ij}^{X}\in SU(2),
\qquad
W_{ij}^{c}\in SU(3).
}
\]

All three obey the common path-composition, reversal and local-frame covariance pattern in their respective representations.

For the spatial branch, the additional affine lift is now typed by

\[
\boxed{
W_{ij}^{X},\mathcal E_{ij}
\longmapsto
G_{ij}^{\nabla}
=\left(
\operatorname{Ad}(W_{ij}^{X}),
\operatorname{vec}(\mathcal E_{ij})
\right)\in SE(3).
}
\]

The corresponding triangular translational loop source is the existing discrete solder torsion object.
