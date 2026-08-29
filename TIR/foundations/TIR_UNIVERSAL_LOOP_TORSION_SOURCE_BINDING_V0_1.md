# TIR Universal-Loop Translational-Holonomy Source Binding v0.1

Status: `EXACT_CONNECTION_AFFINE_LIFT_SOURCE_BINDING / EXACT_ENDPOINT_DEFECT_TO_LOOP_TRANSLATION_IDENTITY / DISCRETE_TRANSLATIONAL_HOLONOMY_SOURCE_PASS_CANDIDATE / CONTINUUM_COFRAME_CORRESPONDENCE_DOWNSTREAM`

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
4. the SE(3) gluing theorem supplies affine semidirect-product composition;
5. the anchor-source theorem supplies the pure-atlas cocycle baseline.

RF/GREMLIN candidate search is therefore replaced at this source coordinate by an explicit deterministic identity.

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

the direct and composed affine maps have the same rotation. Their translation difference is therefore

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

The previously typed endpoint defect is exactly the translational direct/composed affine-gluing defect.

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
t_C
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

This is the Universal-Loop translational-holonomy source identity on the rotationally closed triangular sector.

## 6. Local-frame covariance

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

Hence

\[
\boxed{
\|\mathbf c'_{xyz}\|=\|\mathbf c_{xyz}\|
}
\]

and, by the loop identity,

\[
\boxed{
\|\mathbf t'_C\|=\|\mathbf t_C\|.
}
\]

The scalar witness `tau_C` is therefore independent of the chosen orthonormal local vector frames.

## 7. Pure-atlas baseline

The SE(3) anchor-source theorem gives ordinary overlapping affine charts the exact cocycle

\[
G_{cb}^{atlas}G_{ba}^{atlas}=G_{ca}^{atlas}.
\]

On that sector, the corresponding endpoint composition is exact and the triangular source defect satisfies

\[
\boxed{
\mathbf c_{xyz}=0,
\qquad
\mathbf t_C=0.
}
\]

The connection-lifted witness therefore measures departure from the exact affine-coboundary closure baseline while retaining the same intrinsic endpoint source carrier.

## 8. Discrete torsion-source promotion

TIR SE(3) gluing already identifies the pure-translation loop norm in the rotationally closed sector as the discrete torsion candidate carrier. RF-S12-style source ambiguity is absent here because both components have explicit parents:

```text
rotation source      W_xy^X -> R_xy = Ad(W_xy^X)
translation source   E_xy   -> e_xy = vec(E_xy)
affine edge           (R_xy,e_xy) in SE(3)
loop translation      t_C
endpoint defect       c_xyz
exact identity        t_C = -c_xyz
scalar witness        tau_C = ||t_C|| = ||c_xyz||
```

Accordingly, the TIR global-gluing source coordinate is promoted to

\[
\boxed{
\text{DISCRETE TRANSLATIONAL-HOLONOMY SOURCE BINDING}
}
\]

with `tau_C` as the frame-invariant source witness.

The continuum coframe/Cartan realization is the next typed correspondence:

\[
\boxed{
\text{discrete translational holonomy}
\longrightarrow
\text{continuum coframe / torsion two-form correspondence}.
}
\]

## 9. Universal-Loop source provenance

The source chain used by this theorem is entirely contained in the current TIR geometry/holonomy stack:

```text
QUANTUM_RELATION_AFFINE_TORSOR_V0_1
  -> intrinsic E_xy displacement

TIR_WIJ_HOLONOMY_CROSSWALK_V0_1
  -> R_xy = Ad(W_xy^X)
  -> endpoint defect C_xyz

TIR_SE3_GLOBAL_GLUE_HOLONOMY_V0_1
  -> SE(3) composition
  -> pure-translation loop norm

TIR_SE3_ANCHOR_SOURCE_BINDING_V0_1
  -> exact atlas-source baseline
  -> trivial pure-atlas loop
```

The earlier Universal Loop energy-equation artifact is maintained in its energy-framework lineage; the present torsion-source theorem is sourced by the TIR affine/holonomy lineage above.

## 10. Promotion ledger

```text
E_xy intrinsic affine displacement source                 PASS EXACT PARENT
R_xy = Ad(W_xy^X)                                         PASS EXACT PARENT
G_xy^nabla=(R_xy,e_xy) affine connection lift             PASS TYPED SOURCE BINDING
SE(3) semidirect composition                              PASS EXACT
endpoint defect = direct/composed translation defect      PASS EXACT
rotationally closed triangle R_C=I                        PASS EXACT GIVEN R_xz=R_xy R_yz
loop translation t_C=-c_xyz                               PASS EXACT
frame covariance c' = Q_x c                               PASS EXACT
frame-invariant tau_C=||t_C||=||c_xyz||                   PASS EXACT
pure-atlas zero-witness baseline                          PASS EXACT PARENT
Universal-Loop discrete translational-holonomy source     PASS CANDIDATE PENDING VALIDATOR
continuum coframe / torsion-two-form correspondence       DOWNSTREAM GATE
```

## 11. Deterministic validation target

The validator must verify:

1. exact source lift `G_xy=(R_xy,e_xy)` under semidirect composition;
2. direct/composed endpoint-defect identity;
3. `R_C=I` and `t_C=-c_xyz` for a rotationally consistent triangle;
4. zero-defect loop closure;
5. nonzero translational witness with `||t_C||=||c_xyz||`;
6. independent local-frame covariance and norm invariance;
7. deterministic randomized triangle family;
8. pure-affine/coboundary baseline closure.

Verdict target:

`PASS_TIR_UNIVERSAL_LOOP_TORSION_SOURCE_BINDING`.
