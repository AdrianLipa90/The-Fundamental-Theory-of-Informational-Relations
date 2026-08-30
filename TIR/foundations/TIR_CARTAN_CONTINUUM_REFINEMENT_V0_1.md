# TIR Cartan Continuum Refinement from the Discrete Solder Form v0.1

Status: `CONDITIONAL_SMOOTH_REFINEMENT_THEOREM / DISCRETE_SOLDER_TO_CARTAN_TORSION / ROTATIONAL_HOLONOMY_TO_CURVATURE / AFFINE_LOOP_TRANSLATION_ASYMPTOTIC_TORSION / PHYSICAL_REFINING_FAMILY_BINDING_NEXT`

Date: 2026-08-29

## 1. Purpose

The exact discrete TIR source chain now contains

\[
\mathcal E_{ij}
\to W_{ij}^{X}
\to \mathcal T_{\triangle}
\leftrightarrow t_C.
\]

The next global-geometry question is the controlled small-cell limit. This theorem gives the local refinement statement under an admitted smooth refining family.

The continuum target variables are a spatial coframe

\[
\boxed{e^a=e^a{}_{\mu}\,dx^{\mu}}
\]

and an `so(3)` connection

\[
\boxed{\omega^a{}_b=\omega^a{}_{b\mu}\,dx^{\mu}}.
\]

Their Cartan field strengths are

\[
\boxed{
T^a
=de^a+\omega^a{}_b\wedge e^b
}
\]

and

\[
\boxed{
\Omega^a{}_b
=d\omega^a{}_b
+\omega^a{}_c\wedge\omega^c{}_b.
}
\]

## 2. Smooth refinement assumptions

Let `P` be a contractible spatial patch with local coordinates `x^mu`. Assume:

1. `e^a_mu` is `C^2` on `P`;
2. `omega_mu` is a `C^1` `so(3)`-valued connection on `P`;
3. a shape-regular family of oriented TIR triangles refines the patch with maximal edge size `ell -> 0`;
4. TIR edge generators are the connection-covariant line integrals of the coframe to the edge source frame;
5. TIR `W_ij^X` transport converges to the parallel transport of `omega`.

These assumptions define the refinement surface to be tested against a physical or constructed graph family.

## 3. Covariant edge integral

For an oriented edge `p -> q`, let

\[
R_{p\leftarrow s}
\]

transport an internal vector at a point `s` on the edge into the frame at `p`. Use the convention

\[
\frac{d}{d\lambda}R_{p\leftarrow\gamma(\lambda)}
=
R_{p\leftarrow\gamma(\lambda)}
\,\omega_{\mu}(\gamma(\lambda))\dot\gamma^{\mu}(\lambda),
\]

with identity initial value at `p`.

Define the continuum representative of the TIR edge displacement by

\[
\boxed{
E^a_{pq}
:=
\int_{\gamma_{pq}}
(R_{p\leftarrow s})^a{}_b
\,e^b{}_{\mu}(s)\,dx^{\mu}.
}
\]

For a short edge `Delta x^mu`, Taylor expansion gives

\[
\boxed{
E^a_{pq}
=e^a{}_{\mu}(p)\Delta x^{\mu}
+O(\ell^2),
}
\]

which is the continuum realization of the existing TIR discrete-solder ansatz.

The endpoint transporter is

\[
\boxed{
R_{pq}:=R_{p\leftarrow q}
=\operatorname{Ad}(W_{pq}^{X}).
}
\]

## 4. Oriented triangle and area bivector

Let a triangle be

\[
x\to y\to z\to x
\]

with edge vectors at `x`

\[
u^{\mu}=y^{\mu}-x^{\mu},
\qquad
v^{\mu}=z^{\mu}-x^{\mu}.
\]

Define its oriented coordinate-area bivector

\[
\boxed{
\Sigma^{\mu\nu}_{\triangle}
:=
\int_{\triangle}dx^{\mu}\wedge dx^{\nu}
=\frac12
\left(u^{\mu}v^{\nu}-u^{\nu}v^{\mu}\right).
}
\]

For a shape-regular refinement,

\[
|\Sigma_{\triangle}|=O(\ell^2).
\]

## 5. Discrete solder torsion convergence theorem

The TIR discrete solder object in the `x` frame is

\[
\boxed{
\mathbf T_{\triangle}^{disc}
:=
\mathbf E_{xy}
+R_{xy}\mathbf E_{yz}
+R_{xz}\mathbf E_{zx}.
}
\]

Expanding the three covariant edge integrals and collecting the antisymmetric second-order terms gives

\[
\boxed{
(T_{\triangle}^{disc})^a
=
\frac12
T^a{}_{\mu\nu}(x)
\Sigma^{\mu\nu}_{\triangle}
+O(\ell^3).
}
\]

Equivalently, in the matrix carrier,

\[
\boxed{
\mathcal T_{\triangle}
=
\frac12
T^a{}_{\mu\nu}(x)
\Sigma^{\mu\nu}_{\triangle}\,\sigma_a
+O(\ell^3).
}
\]

Thus the discrete TIR solder-closure object is the second-order flux coordinate of Cartan torsion.

For the coordinate triangle

\[
u=h\,\partial_{\mu},
\qquad
v=h\,\partial_{\nu},
\qquad
A_{\triangle}=\frac{h^2}{2},
\]

one obtains

\[
\boxed{
\frac{\mathbf T_{\triangle}^{disc}}{A_{\triangle}}
\longrightarrow
\mathbf T_{\mu\nu}(x)
}
\]

as `h -> 0`.

## 6. Rotational holonomy convergence theorem

The rotational loop is

\[
\boxed{
R_{\triangle}
:=R_{xy}R_{yz}R_{zx}.
}
\]

The standard small-loop expansion in the adopted back-transport convention is

\[
\boxed{
R_{\triangle}
=I
+\frac12
\Omega_{\mu\nu}(x)
\Sigma^{\mu\nu}_{\triangle}
+O(\ell^3).
}
\]

Because `Omega_mu_nu` is antisymmetric in the internal orthonormal representation,

\[
\boxed{
\frac{R_{\triangle}-R_{\triangle}^{T}}{2A_{\triangle}}
\longrightarrow
\Omega_{\mu\nu}(x)
}
\]

for the coordinate triangle above.

The TIR loop therefore carries both Cartan channels in the refining limit:

```text
translation / solder closure -> T^a
rotation / frame holonomy     -> Omega^a_b
```

## 7. Full SE(3) loop translation at nonzero curvature

Gate A established the exact identity between the SE(3) loop translation and the discrete solder torsion on the rotationally closed triangle sector.

For a general smooth refining triangle, define the full affine loop translation

\[
\boxed{
\mathbf t_C
=\mathbf E_{xy}
+R_{xy}\mathbf E_{yz}
+R_{xy}R_{yz}\mathbf E_{zx}.
}
\]

The discrete solder torsion uses the direct transporter `R_xz` on the closing edge:

\[
\mathbf T_{\triangle}^{disc}
=\mathbf E_{xy}
+R_{xy}\mathbf E_{yz}
+R_{xz}\mathbf E_{zx}.
\]

Hence exactly

\[
\boxed{
\mathbf t_C-\mathbf T_{\triangle}^{disc}
=
(R_{xy}R_{yz}-R_{xz})\mathbf E_{zx}.
}
\]

Smooth connection holonomy gives

\[
R_{xy}R_{yz}-R_{xz}=O(\ell^2),
\]

while

\[
\mathbf E_{zx}=O(\ell).
\]

Therefore

\[
\boxed{
\mathbf t_C
=\mathbf T_{\triangle}^{disc}
+O(\ell^3).
}
\]

and consequently

\[
\boxed{
\frac{\mathbf t_C}{A_{\triangle}}
\longrightarrow
\mathbf T_{\mu\nu}(x).
}
\]

The Gate-A translational holonomy therefore retains the same continuum torsion limit in the presence of smooth rotational curvature.

## 8. Frame covariance of the continuum limit

Under a smooth local orthonormal frame transformation `Q(x) in SO(3)`,

\[
e\mapsto Qe,
\]

\[
\omega\mapsto Q\omega Q^{-1}-dQ\,Q^{-1},
\]

so

\[
\boxed{
T\mapsto QT,
\qquad
\Omega\mapsto Q\Omega Q^{-1}.
}
\]

The discrete edge and transporter transformations reproduce the same base-frame covariance. Hence the normalized refinement limits inherit the correct Cartan transformation laws.

## 9. Metric and rank channel

The coframe gives

\[
\boxed{
h_{\mu\nu}
=\delta_{ab}e^a{}_{\mu}e^b{}_{\nu}.}
\]

On a full-rank local TIR displacement patch,

\[
\operatorname{rank}(e^a{}_{\mu})=3,
\]

so `h` is positive definite. The existing local spatial dimension theorem and discrete solder rank gate therefore supply the correct rank condition for the spatial continuum chart.

## 10. Zero-torsion refinement criterion

For a shape-regular refining family whose triangle bivectors span the local tangent two-planes,

\[
\boxed{
T^a=0
\quad\Longleftrightarrow\quad
\frac{\mathcal T_{\triangle}}{A_{\triangle}}
\longrightarrow0
\text{ on every local oriented refinement family}.
}
\]

The same criterion may be read from the affine loop translation because

\[
\frac{\mathbf t_C-\mathbf T_{\triangle}^{disc}}{A_{\triangle}}
=O(\ell)\to0.
\]

This provides an operational spatial torsion-free criterion for the later GR action/connection gate.

## 11. Evidence and validation surface

The theorem is conditional on the smooth refinement assumptions of Section 2. The deterministic reference validator supplies an independent analytic-family check with:

1. a full-rank affine coframe field;
2. a constant noncommuting `so(3)` connection;
3. decreasing triangular cell sizes;
4. covariant edge integration by midpoint refinement;
5. direct evaluation of the continuum `T_12` and `Omega_12` targets;
6. convergence of discrete solder torsion per area;
7. convergence of affine loop translation per area;
8. convergence of rotational holonomy per area;
9. constant-frame covariance;
10. Euclidean zero-torsion/zero-curvature baseline.

This validator is a synthetic convergence reference for the theorem. A physical TIR refining-family receipt is the next evidence surface.

## 12. Promotion ledger

```text
Gate A discrete torsion source binding                    PASS EXACT PARENT
C2 coframe + C1 so(3) connection refinement surface       TYPED ASSUMPTION
covariant edge integral                                   EXACT DEFINITION
E_pq=e_mu Delta x^mu+O(ell^2)                             PASS TAYLOR
T_disc=1/2 T_mn Sigma^mn+O(ell^3)                         PASS CONDITIONAL THEOREM
R_loop=I+1/2 Omega_mn Sigma^mn+O(ell^3)                   PASS CONDITIONAL THEOREM
t_C-T_disc=O(ell^3)                                       PASS CONDITIONAL THEOREM
normalized torsion convergence                            PASS CONSEQUENCE
normalized curvature convergence                          PASS CONSEQUENCE
full-rank coframe -> positive spatial metric              PASS STANDARD
zero-torsion refinement criterion                         PASS CONDITIONAL
physical refining relational graph family                 NEXT SOURCE RECEIPT
TIR x IDT ADM join                                        DOWNSTREAM GR GATE
```

## 13. Validation authority

Reference validator:

`TIR/foundations/validation/tir_cartan_continuum_refinement_v0_1.py`.

Dedicated workflow:

`.github/workflows/tir-cartan-continuum-refinement.yml`.

Stack parent:

`TIR_UNIVERSAL_LOOP_TORSION_SOURCE_BINDING_V0_1` exact-green head `91333253adc2a09f37704bfad5bc15d3df5e3c33`.
