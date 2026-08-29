# The Space of Geometry

Status: `TIR_SUBREPO_V1_1_CALIBRATED_LOCAL_GLUE_CANDIDATE`

Working title:

> **The Space of Geometry: From First Distinction to Pythagoras**

Current manuscript source:

`paper/THE_SPACE_OF_GEOMETRY_V1_1.tex`

Current research spine and publication controls:

- `RESEARCH_SPINE_V0_12.md`
- `publication/PROOF_DEPENDENCY_AUDIT_V0_3.md`
- `publication/REFEREE_CLAIM_FIREWALL_V1_1.md`

The common local carrier is

\[
\mathbb C^2
\to
\rho_x
\to
\mathcal A_2
\to
\delta(\rho_x,\rho_y)
\to
\operatorname{Herm}_0(2)\cong\mathbb R^3.
\]

The canonical relation and dimensionless local metric are

\[
\mathcal E_{xy}=2(\rho_y-\rho_x),
\qquad
g_0(A,B)=\frac12\operatorname{Tr}(AB).
\]

For physical binary density states,

\[
\boxed{
\mathcal R_{\rm phys}
=\{\mathbf d\cdot\boldsymbol\sigma:\ |\mathbf d|\le2\}.
}
\]

The physical-state Pythagorean family contains the exact normalized certificate

\[
\boxed{
\frac9{25}+\frac{16}{25}=1
}
\]

with \(a=3/5\), \(b=4/5\), \(c=1\).

The parallel finite-cell branch gives

\[
\operatorname{Herm}_0(2)
\to
\Delta^3
\xrightarrow{A5+A7}
\text{regular tetrahedron},
\]

with normalized Gram invariant

\[
\boxed{n_a\cdot n_b=-\frac13\qquad(a\ne b),}
\]

while the qubit-SIC branch remains an independent convergence crosscheck on the same finite frame.

## Physical length calibration

Introduce the positive physical length calibration

\[
L_*>0,
\qquad [L_*]=L.
\]

The calibrated local metric and relation length are

\[
\boxed{
g_{\rm phys}=L_*^2g_0,
}
\]

\[
\boxed{
\ell_{\rm phys}(\mathcal E)
=L_*\sqrt{\frac12\operatorname{Tr}(\mathcal E^2)}.
}
\]

One nonzero typed physical reference length fixes `L_*` uniquely. The exact physical single-edge coefficient radius `2` becomes

\[
\boxed{D_{\rm edge}=2L_*.}
\]

Angles, orthogonality, relative lengths, Pythagorean closure and the normalized tetrahedral Gram frame are common-scale invariant.

## Calibrated local-carrier gluing

At each local site `x`, write

\[
\boxed{g_x=L_x^2g_0.}
\]

The existing TIR spatial transport

\[
W_{xy}^{X}\in SU(2)
\]

induces

\[
\boxed{
R_{xy}=\operatorname{Ad}(W_{xy}^{X})\in SO(3).
}
\]

Pure rotational transport preserves the calibrated physical metric exactly when adjacent scales agree:

\[
\boxed{
T_{xy}=R_{xy}
\quad\Longrightarrow\quad
\text{metric compatibility}\iff L_x=L_y.
}
\]

Thus a connected metric-compatible pure-rotation branch propagates one common physical length calibration.

For varying positive local calibration, the unique positive scalar multiple of the same rotational transport that preserves the calibrated metrics is

\[
\boxed{
C_{xy}=\frac{L_x}{L_y}R_{xy}.
}
\]

Node-induced scale factors telescope around every closed loop:

\[
\boxed{
S_\gamma
=\prod_{(xy)\in\gamma}\frac{L_x}{L_y}
=1,
}
\]

while the rotational loop factor may retain nontrivial holonomy

\[
\boxed{R_\gamma\in SO(3).}
\]

Relations in different local frames compose only after transport into one comparison frame. On the common-scale branch,

\[
\boxed{
\mathcal E_{xz}^{(x)}
=
\mathcal E_{xy}^{(x)}
+R_{xy}\mathcal E_{yz}^{(y)}.
}
\]

The transported closure defect is

\[
\boxed{
\mathcal C_{xyz}
=
\mathcal E_{xz}^{(x)}
-\left(\mathcal E_{xy}^{(x)}+R_{xy}\mathcal E_{yz}^{(y)}\right).
}
\]

This supplies the calibrated gluing layer needed before the existing TIR holonomy/curvature/torsion refinement programme.

The current geometry frontier is now

\[
\boxed{
\Delta^3
\to
\mathcal E_{ij}
\to
W_{ij}
\to
W_{\rm loop}
\to
\mathcal C
\to
\text{tetrahedral refinement / curvature / torsion}.
}
\]

Current release and frontier surfaces include:

- `paper/THE_SPACE_OF_GEOMETRY_V1_1.tex`
- `RESEARCH_SPINE_V0_12.md`
- `foundations/PHYSICAL_LENGTH_SCALE_CALIBRATION_V0_1.md`
- `foundations/SCALE_COMPATIBLE_LOCAL_CARRIER_GLUING_V0_1.md`
- `validation/physical_length_scale_calibration_v0_1.py`
- `validation/scale_compatible_local_carrier_gluing_v0_1.py`
- `publication/PROOF_DEPENDENCY_AUDIT_V0_3.md`
- `publication/REFEREE_CLAIM_FIREWALL_V1_1.md`

The v1.1 publication remains frozen at local Pythagorean closure and the parallel tetrahedral finite-cell theorem. Scale calibration and calibrated local-carrier gluing are downstream geometry results.

TIR remains the parent Source of Truth for the primitive axioms, first-distinction chain and `W_ij` transport family.
