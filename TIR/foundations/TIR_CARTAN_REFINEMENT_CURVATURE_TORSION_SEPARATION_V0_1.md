# TIR Cartan Refinement and Curvature–Torsion Separation v0.1

Status: `EXACT_GENERAL_SE3_LOOP_DECOMPOSITION / CONTROLLED_SMALL_LOOP_CARTAN_REFINEMENT / CURVATURE_TORSION_ORDER_SEPARATION_PASS / ZERO_TORSION_SELECTION_DOWNSTREAM`

Date: 2026-08-30

## 1. Purpose

Gate A bound the TIR discrete solder object to the translational part of an `SE(3)` loop on the rotationally closed triangle sector. Gate A2 removes that rotational-closure restriction and establishes the continuum small-loop firewall required before the spatial GR branch can select the zero-torsion sector.

The parent objects are

\[
G_{xy}^{\nabla}=(R_{xy},\mathbf e_{xy})\in SE(3),
\qquad
R_{xy}=\operatorname{Ad}(W_{xy}^{X}),
\]

with intrinsic affine endpoint displacement

\[
\mathbf e_{xy}=\operatorname{vec}(\mathcal E_{xy}),
\qquad
\mathcal E_{xy}=2(\rho_y-\rho_x).
\]

The continuum targets are the Cartan torsion and curvature two-forms

\[
\boxed{T^a=de^a+\omega^a{}_b\wedge e^b},
\]

\[
\boxed{\Omega^a{}_b=d\omega^a{}_b+\omega^a{}_c\wedge\omega^c{}_b}.
\]

The essential requirement is to separate translational torsion from rotational curvature without forcing either one to vanish merely because the other is selected.

## 2. General triangular `SE(3)` loop

For an oriented triangle `x -> y -> z -> x`, use

\[
G_{xy}=(R_{xy},\mathbf e_{xy}),
\qquad
G_{yz}=(R_{yz},\mathbf e_{yz}),
\qquad
G_{xz}=(R_{xz},\mathbf e_{xz}).
\]

The inverse direct edge is

\[
G_{zx}=G_{xz}^{-1}
=\left(R_{xz}^{-1},-R_{xz}^{-1}\mathbf e_{xz}\right).
\]

The loop is

\[
G_C=G_{xy}G_{yz}G_{zx}=(R_C,\mathbf t_C),
\]

with exact rotational part

\[
\boxed{R_C=R_{xy}R_{yz}R_{xz}^{-1}}.
\]

Using the semidirect-product law gives

\[
\boxed{
\mathbf t_C
=\mathbf e_{xy}
+R_{xy}\mathbf e_{yz}
-R_C\mathbf e_{xz}.
}
\]

## 3. Discrete solder vector without rotational closure

The TIR reverse-edge rule gives

\[
\mathbf e_{zx}
=-R_{xz}^{-1}\mathbf e_{xz}.
\]

Therefore the vector form of the existing discrete solder object is

\[
\begin{aligned}
\boldsymbol\tau_{xyz}
&:=\operatorname{vec}(\mathcal T_{xyz})\\
&=\mathbf e_{xy}
+R_{xy}\mathbf e_{yz}
+R_{xz}\mathbf e_{zx}\\
&=\boxed{
\mathbf e_{xy}+R_{xy}\mathbf e_{yz}-\mathbf e_{xz}
}.
\end{aligned}
\]

Subtracting this from the general loop translation yields the exact identity

\[
\boxed{
\mathbf t_C
=\boldsymbol\tau_{xyz}
+(I-R_C)\mathbf e_{xz}.
}
\]

Equivalently,

\[
\boxed{
\mathbf t_C-\operatorname{vec}(\mathcal T_{xyz})
=(I-R_C)\mathbf e_{xz}.
}
\]

This identity holds without assuming `R_C=I`.

On the Gate-A rotationally consistent sector,

\[
R_C=I,
\]

and the previous exact result is recovered:

\[
\boxed{\mathbf t_C=\operatorname{vec}(\mathcal T_{xyz})}.
\]

## 4. Controlled shrinking-loop scaling

Let `C_epsilon` be a regular refining family of oriented relational triangles of characteristic edge scale `epsilon`.

Assume the coframe and connection limits are smooth enough that

\[
\mathbf e_{ij}=O(\epsilon),
\]

and the rotational loop has the standard curvature scaling

\[
\boxed{
R_C
=I+A_C\,\Omega(u,v)+o(A_C),
}
\]

where

\[
A_C=\Theta(\epsilon^2).
\]

Then

\[
I-R_C=O(\epsilon^2),
\]

so the exact correction term obeys

\[
\boxed{
(I-R_C)\mathbf e_{xz}=O(\epsilon^3).
}
\]

If the discrete solder family has a finite area-normalized limit

\[
\boxed{
\frac{\boldsymbol\tau_{xyz}}{A_C}
\longrightarrow T(u,v),
}
\]

then

\[
\frac{\mathbf t_C}{A_C}
=\frac{\boldsymbol\tau_{xyz}}{A_C}
+O(\epsilon),
\]

and therefore

\[
\boxed{
\lim_{\epsilon\to0}
\frac{\mathbf t_C}{A_C}
=
\lim_{\epsilon\to0}
\frac{\boldsymbol\tau_{xyz}}{A_C}
=T(u,v).
}
\]

Thus rotational curvature cannot contaminate the leading `O(area)` torsion coefficient.

## 5. Local Cartan expansion

Let the refining relation carrier admit the smooth coframe limit

\[
\mathcal E_{xy}
=e^a{}_i(x)\Delta x^i\sigma_a
+O(|\Delta x|^2),
\]

and let the spatial transport admit the smooth connection expansion

\[
R_{x,x+\epsilon u}
=I+\epsilon\,\omega(u)+O(\epsilon^2)
\]

in one local vector frame.

Compare the two infinitesimal two-step developments from the same initial point:

```text
path uv: x -> x+epsilon u -> x+epsilon u+epsilon v
path vu: x -> x+epsilon v -> x+epsilon v+epsilon u
```

Taylor expansion of the coframe and first-order connection transport gives

\[
\boxed{
\Delta_{uv}-\Delta_{vu}
=\epsilon^2
\left[
(de+\omega\wedge e)(u,v)
\right]
+O(\epsilon^3).
}
\]

Hence

\[
\boxed{
\Delta_{uv}-\Delta_{vu}
=\epsilon^2 T(u,v)+O(\epsilon^3).
}
\]

The corresponding rotational commutator has the independent expansion

\[
\boxed{
R_{uv}R_{vu}^{-1}
=I+\epsilon^2\Omega(u,v)+O(\epsilon^3).
}
\]

This is the required discrete-to-Cartan separation:

```text
translation commutator / area -> torsion T^a
rotation commutator / area    -> curvature Omega^a_b
```

## 6. Zero torsion does not remove curvature

The spatial GR sector targets

\[
T^a=0.
\]

Gate A2 makes the logical consequence precise. If

\[
\boldsymbol\tau_{xyz}=o(A_C),
\]

then

\[
\frac{\mathbf t_C}{A_C}\to0,
\]

while it remains possible that

\[
\boxed{
\frac{R_C-I}{A_C}
\longrightarrow\Omega(u,v)\ne0.
}
\]

Therefore

\[
\boxed{
T^a=0
\not\Rightarrow
\Omega^a{}_b=0.
}
\]

This firewall is essential: the Levi-Civita/GR branch may be torsion-free and still geometrically curved.

At finite loop size, even on an exact discrete `boldsymbol tau=0` sample, the general identity allows an `O(epsilon^3)` translational loop term generated by nonzero rotational curvature:

\[
\mathbf t_C=(I-R_C)\mathbf e_{xz}.
\]

Its area-normalized contribution vanishes in the continuum limit.

## 7. Pure-atlas baseline remains stronger

The TIR anchor-source theorem already proves that ordinary re-expression of one common affine carrier obeys an exact `SE(3)` cocycle and therefore

\[
G_C^{atlas}=e_{SE(3)}.
\]

Thus the pure-atlas baseline has both

\[
R_C=I,
\qquad
\mathbf t_C=0
\]

exactly.

The physical connection branch is different: it may retain nontrivial rotational holonomy while its leading translational area coefficient is zero.

This preserves the existing firewall

```text
coordinate transition defect != physical curvature
zero torsion              != zero curvature
```

## 8. What Gate A2 promotes

Gate A2 promotes the following statements:

```text
general SE(3) loop rotation R_C                         PASS EXACT
general loop translation t_C                            PASS EXACT
discrete solder vector tau=e_xy+R_xy e_yz-e_xz         PASS EXACT
t_C = tau + (I-R_C)e_xz                                 PASS EXACT
Gate-A R_C=I roundtrip                                  PASS EXACT
curvature correction to t_C is O(epsilon^3)             PASS UNDER SMOOTH SMALL-LOOP SCALING
rotational holonomy is O(epsilon^2)                     PASS UNDER SMOOTH CONNECTION SCALING
torsion is O(epsilon^2)                                 PASS UNDER SMOOTH COFRAME/CONNECTION SCALING
area-normalized t_C and discrete tau have same limit     PASS CONDITIONAL CONVERGENCE THEOREM
T=0 remains compatible with Omega!=0                    PASS EXACT/ASYMPTOTIC FIREWALL
pure-atlas closed loop                                  PASS EXACT PARENT
```

## 9. Remaining zero-torsion selection gate

Gate A2 identifies the continuum torsion coordinate and separates it from curvature. The next spatial-GR theorem must determine why the physical TIR connection lies in the distinguished sector

\[
\boxed{T^a=0}.
\]

The affine torsor parent supplies exact endpoint uniqueness and same-chart composition,

\[
\mathcal E_{xz}=\mathcal E_{xy}+\mathcal E_{yz},
\]

but an independently admitted connection can in general carry a torsional translational defect. Therefore zero torsion is promoted only after an independent TIR compatibility/minimality theorem binds the physical connection to the intrinsic metric/coframe carrier.

Candidate parent routes for that next theorem are:

1. metric compatibility plus a no-independent-geometric-connection principle derived from the TIR foundational carrier;
2. a direct refinement theorem showing two-path intrinsic endpoint developments agree through `O(area)`;
3. an independently derived Levi-Civita uniqueness binding from the TIR metric and solder carrier.

GREMLIN may rank these candidates, but promotion remains theorem/validator controlled.

## 10. Updated GR dependency line

```text
TIR affine torsor E_xy
 -> W_ij^X / R_ij connection transport
 -> SE(3) affine lift
 -> discrete solder tau_triangle
 -> Gate A exact torsion-source binding
 -> Gate A2 general loop decomposition
 -> tau_triangle / area -> Cartan T^a
 -> rotational holonomy / area -> Cartan Omega^a_b
 -> ZERO-TORSION SELECTION GATE
 -> Levi-Civita spatial GR sector
 -> TIR x IDT ADM join
 -> RFC RF-E21 Einstein-form selection
 -> RF-E3 coupling normalization
 -> RF-E12/RF-E13 constraints and evolution
```

## 11. Validation authority

Deterministic validator:

`TIR/foundations/validation/tir_cartan_refinement_curvature_torsion_separation_v0_1.py`

Static receipt:

`TIR/foundations/validation/TIR_CARTAN_REFINEMENT_CURVATURE_TORSION_SEPARATION_V0_1.json`

Hosted workflow:

`.github/workflows/tir-cartan-refinement-curvature-torsion.yml`

Verdict target:

`PASS_TIR_CARTAN_REFINEMENT_CURVATURE_TORSION_SEPARATION`.
