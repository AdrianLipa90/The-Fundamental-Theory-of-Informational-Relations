# TIR Universal-Loop Translational-Holonomy Source Binding v0.1

Status: `EXACT_CONNECTION_AFFINE_LIFT_SOURCE_BINDING / EXACT_DISCRETE_SOLDER_TORSION_CROSSWALK / EXACT_ENDPOINT_DEFECT_TO_LOOP_TRANSLATION_IDENTITY / DISCRETE_TORSION_SOURCE_BINDING_CANDIDATE / CONTINUUM_REFINEMENT_GATE_NEXT`

Date: 2026-08-29

## 1. Purpose and parent chain

The current TIR global-completion frontier asks for the source binding

\[
\mathcal E_{ij}
\to W_{ij}^{X}
\to G_{ij}\in SE(3)
\to G_C=(R_C,t_C)
\to \text{translational loop closure}.
\]

The required parents are already present in TIR:

1. the affine quantum-state torsor supplies the intrinsic endpoint displacement
   \[
   \mathcal E_{xy}=2(\rho_y-\rho_x)\in\operatorname{Herm}_0(2);
   \]
2. the spatial holonomy family supplies
   \[
   W_{xy}^{X}\in SU(2),
   \qquad
   R_{xy}:=\operatorname{Ad}_{W_{xy}^{X}}\in SO(3);
   \]
3. the covariant endpoint seam supplies
   \[
   \mathcal C_{xyz}
   =\mathcal E_{xz}
   -\left(
   \mathcal E_{xy}
   +W_{xy}^{X}\mathcal E_{yz}(W_{xy}^{X})^\dagger
   \right);
   \]
4. the discrete relational solder form supplies the triangle object
   \[
   \mathcal T_{xyz}
   =\mathcal E_{xy}
   +U_{xy}\mathcal E_{yz}U_{xy}^{\dagger}
   +U_{xz}\mathcal E_{zx}U_{xz}^{\dagger};
   \]
5. the SE(3) gluing theorem supplies affine semidirect-product composition;
6. the anchor-source theorem supplies the exact pure-atlas cocycle baseline.

These parents reduce the Universal-Loop source coordinate to an explicit identity among already typed TIR objects.

## 2. Pauli-vector source convention

Write

\[
\mathcal E_{xy}
=\mathbf e_{xy}\cdot\boldsymbol\sigma,
\qquad
\boxed{
\mathbf e_{xy}:=\operatorname{vec}(\mathcal E_{xy})
=\mathbf r_y-\mathbf r_x
}.
\]

The affine-torsor theorem gives this vector as the unique intrinsic displacement between the normalized quantum-point endpoints in the adopted Pauli normalization.

The spatial transporter acts on the same real coefficient carrier through

\[
\boxed{
\operatorname{vec}\!\left(
W_{xy}^{X}\mathcal E_{yz}(W_{xy}^{X})^\dagger
\right)
=R_{xy}\mathbf e_{yz}.
}
\]

Hence the endpoint defect has vector form

\[
\boxed{
\mathbf c_{xyz}
:=\operatorname{vec}(\mathcal C_{xyz})
=\mathbf e_{xz}
-\left(\mathbf e_{xy}+R_{xy}\mathbf e_{yz}\right).
}
\]

## 3. Connection-lifted affine edge

Define the connection-lifted affine transport from the `y` local carrier into the `x` local carrier by

\[
\boxed{
G_{xy}^{\nabla}
:=\left(R_{xy},\mathbf e_{xy}\right)
\in SE(3).
}
\]

Its affine action is

\[
\boxed{
\mathbf v_x
=\mathbf e_{xy}+R_{xy}\mathbf v_y.
}
\]

The rotational component is source-owned by `W_xy^X`; the translational component is source-owned by the intrinsic affine endpoint relation `E_xy`.

For two consecutive edges,

\[
G_{xy}^{\nabla}G_{yz}^{\nabla}
=
\boxed{
\left(
R_{xy}R_{yz},
\mathbf e_{xy}+R_{xy}\mathbf e_{yz}
\right)
}.
\]

This is exactly the covariant endpoint-composition expression appearing in the TIR closure seam.

## 4. Direct/composed translational defect theorem

Let the direct edge be

\[
G_{xz}^{\nabla}
=\left(R_{xz},\mathbf e_{xz}\right).
\]

On the rotationally consistent triangle sector,

\[
\boxed{
R_{xz}=R_{xy}R_{yz},
}
\]

the direct and composed affine maps have the same rotation. Their translation difference is

\[
\begin{aligned}
\Delta\mathbf t_{xyz}
&:=
\mathbf e_{xz}
-\left(\mathbf e_{xy}+R_{xy}\mathbf e_{yz}\right)\\
&=\mathbf c_{xyz}.
\end{aligned}
\]

Thus

\[
\boxed{
\Delta\mathbf t_{xyz}=\mathbf c_{xyz}.
}
\]

The TIR endpoint defect is exactly the translational direct/composed affine-gluing defect.

## 5. Closed triangular loop theorem

Use the reversal/inverse edge

\[
\boxed{
G_{zx}^{\nabla}
=\left(G_{xz}^{\nabla}\right)^{-1}
=\left(
R_{xz}^{-1},
-R_{xz}^{-1}\mathbf e_{xz}
\right).
}
\]

Define the oriented triangular loop

\[
\boxed{
G_C
:=G_{xy}^{\nabla}G_{yz}^{\nabla}G_{zx}^{\nabla}.
}
\]

Using `R_xz=R_xy R_yz`, its rotational part is

\[
\boxed{
R_C
=R_{xy}R_{yz}R_{xz}^{-1}
=I.
}
\]

Its translational part is

\[
\begin{aligned}
\mathbf t_C
&=\mathbf e_{xy}
+R_{xy}\mathbf e_{yz}
+R_{xz}\left(-R_{xz}^{-1}\mathbf e_{xz}\right)\\
&=\mathbf e_{xy}+R_{xy}\mathbf e_{yz}-\mathbf e_{xz}\\
&=-\mathbf c_{xyz}.
\end{aligned}
\]

Therefore

\[
\boxed{
\mathbf t_C=-\mathbf c_{xyz}
}
\]

and

\[
\boxed{
\tau_C:=\|\mathbf t_C\|
=\|\mathbf c_{xyz}\|.
}
\]

## 6. Exact discrete-solder torsion crosswalk

The existing TIR discrete solder form uses the same oriented triangle and defines

\[
\boxed{
\mathcal T_{xyz}
:=
\mathcal E_{xy}
+U_{xy}\mathcal E_{yz}U_{xy}^{\dagger}
+U_{xz}\mathcal E_{zx}U_{xz}^{\dagger}.
}
\]

Use the spatial connection identification

\[
U_{xy}=W_{xy}^{X},
\qquad
U_{xz}=W_{xz}^{X},
\]

and the admitted reverse-edge rule

\[
\mathcal E_{zx}
=-U_{zx}\mathcal E_{xz}U_{zx}^{\dagger},
\qquad
U_{zx}=U_{xz}^{-1}.
\]

Then

\[
U_{xz}\mathcal E_{zx}U_{xz}^{\dagger}
=-\mathcal E_{xz}.
\]

Therefore

\[
\begin{aligned}
\mathcal T_{xyz}
&=\mathcal E_{xy}
+W_{xy}^{X}\mathcal E_{yz}(W_{xy}^{X})^{\dagger}
-\mathcal E_{xz}\\
&=-\mathcal C_{xyz}.
\end{aligned}
\]

Hence

\[
\boxed{
\mathcal T_{xyz}=-\mathcal C_{xyz}.
}
\]

Taking Pauli coefficient vectors gives

\[
\boxed{
\operatorname{vec}(\mathcal T_{xyz})
=-\mathbf c_{xyz}
=\mathbf t_C.
}
\]

Thus the SE(3) translational loop holonomy and the previously defined TIR discrete torsion object are the same source-owned vector on this rotationally closed triangle sector:

\[
\boxed{
\mathbf t_C
=\operatorname{vec}(\mathcal T_{xyz}).
}
\]

Using the Hilbert--Schmidt normalization of the relation carrier,

\[
\boxed{
\tau_C
=\|\mathbf t_C\|
=\sqrt{\frac12\operatorname{Tr}(\mathcal T_{xyz}^{2})}
=\|\mathbf c_{xyz}\|.
}
\]

This is the exact discrete torsion-source binding targeted by Gate A.

## 7. Local-frame covariance

Let independent local vector frames change by

\[
Q_x,Q_y,Q_z\in SO(3).
\]

The source objects transform as

\[
\boxed{
\mathbf e'_{xy}=Q_x\mathbf e_{xy},
\qquad
R'_{xy}=Q_xR_{xy}Q_y^{-1},
}
\]

and analogously on the other edges.

Then

\[
\begin{aligned}
\mathbf c'_{xyz}
&=Q_x\mathbf e_{xz}
-\left(
Q_x\mathbf e_{xy}
+Q_xR_{xy}Q_y^{-1}Q_y\mathbf e_{yz}
\right)\\
&=Q_x\mathbf c_{xyz}.
\end{aligned}
\]

Consequently

\[
\boxed{
\operatorname{vec}(\mathcal T'_{xyz})
=Q_x\operatorname{vec}(\mathcal T_{xyz}),
}
\]

and

\[
\boxed{
\|\mathbf t'_C\|
=\|\mathbf t_C\|
=\sqrt{\frac12\operatorname{Tr}(\mathcal T_{xyz}^{2})}.
}
\]

The scalar witness `tau_C` is frame invariant.

## 8. Pure-atlas baseline

The SE(3) anchor-source theorem gives ordinary overlapping affine charts the exact cocycle

\[
G_{cb}^{atlas}G_{ba}^{atlas}=G_{ca}^{atlas}.
\]

On that exact affine-coboundary sector,

\[
\boxed{
\mathcal C_{xyz}=0,
\qquad
\mathcal T_{xyz}=0,
\qquad
\mathbf t_C=0.
}
\]

The connection-lifted source witness therefore has an exact zero baseline supplied by the already validated atlas theorem.

## 9. Continuum refinement target

The discrete solder theorem already supplies the continuum ansatz

\[
\mathcal E_{xy}
=e^a{}_i(x)\,\Delta x^i\,\sigma_a
+O(|\Delta x|^2),
\]

with

\[
e^a=e^a{}_i dx^i
\]

and the Cartan target

\[
\boxed{
T^a
=de^a+\omega^a{}_b\wedge e^b.
}
\]

Gate A now supplies the exact discrete source object entering that refinement:

\[
\boxed{
\operatorname{vec}(\mathcal T_{xyz})
=\mathbf t_C.
}
\]

The next global-geometry gate is therefore a convergence theorem for a refining family of TIR triangles, establishing the controlled small-loop limit from `mathcal T_xyz` to the continuum torsion two-form and the corresponding curvature limit from rotational holonomy.

The spatial GR branch contains the distinguished zero-torsion sector

\[
\boxed{T^a=0,}
\]

while the broader Cartan branch retains the full sourced `T^a` coordinate.

## 10. Universal-Loop source provenance

The source chain used by this theorem is contained in the current TIR geometry/holonomy stack:

```text
QUANTUM_RELATION_AFFINE_TORSOR_V0_1
  -> intrinsic E_xy displacement

TIR_WIJ_HOLONOMY_CROSSWALK_V0_1
  -> R_xy = Ad(W_xy^X)
  -> endpoint defect C_xyz

TIR_DISCRETE_SOLDER_FORM_V0_1
  -> discrete torsion object T_xyz
  -> continuum coframe target

TIR_SE3_GLOBAL_GLUE_HOLONOMY_V0_1
  -> SE(3) composition
  -> pure-translation loop norm

TIR_SE3_ANCHOR_SOURCE_BINDING_V0_1
  -> exact atlas-source baseline
  -> trivial pure-atlas loop
```

The Universal Loop energy-equation artifact remains in its energy-framework lineage. The present torsion-source theorem is sourced by the TIR affine, solder and holonomy lineage above.

## 11. Promotion ledger

```text
E_xy intrinsic affine displacement source                 PASS EXACT PARENT
R_xy = Ad(W_xy^X)                                         PASS EXACT PARENT
TIR discrete solder torsion T_xyz                         PASS EXACT PARENT OBJECT
G_xy^nabla=(R_xy,e_xy) affine connection lift             PASS TYPED SOURCE BINDING
SE(3) semidirect composition                              PASS EXACT
endpoint defect = direct/composed translation defect      PASS EXACT
rotationally closed triangle R_C=I                        PASS EXACT GIVEN R_xz=R_xy R_yz
loop translation t_C=-c_xyz                               PASS EXACT
T_xyz=-C_xyz                                               PASS EXACT
vec(T_xyz)=t_C                                             PASS EXACT
frame-invariant tau_C                                     PASS EXACT
pure-atlas zero-source baseline                           PASS EXACT PARENT
Universal-Loop discrete torsion source binding            PASS CANDIDATE UNDER HOSTED VALIDATION
continuum refining-family torsion correspondence          NEXT GLOBAL GEOMETRY GATE
```

## 12. Deterministic validation target

The validator verifies:

1. exact source lift `G_xy=(R_xy,e_xy)` under semidirect composition;
2. direct/composed endpoint-defect identity;
3. `R_C=I` and `t_C=-c_xyz` for a rotationally consistent triangle;
4. discrete-solder identity `T_xyz=-C_xyz`;
5. exact vector crosswalk `vec(T_xyz)=t_C`;
6. zero-defect / zero-torsion loop closure;
7. nonzero source witness with all norm identities;
8. independent local-frame covariance;
9. deterministic randomized triangle family;
10. pure-affine/coboundary baseline closure.

Verdict target:

`PASS_TIR_UNIVERSAL_LOOP_TORSION_SOURCE_BINDING`.
