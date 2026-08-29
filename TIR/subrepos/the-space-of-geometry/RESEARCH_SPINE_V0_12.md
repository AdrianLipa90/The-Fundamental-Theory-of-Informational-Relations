# The Space of Geometry — Research Spine v0.12

Status: `TIR_SPACE_OF_GEOMETRY_CALIBRATED_LOCAL_GLUE_V0_12_CANDIDATE`

## 1. Imported local geometry

The v0.11 calibrated local carrier is

\[
V_x\cong\operatorname{Herm}_0(2),
\qquad
g_x=L_x^2g_0,
\qquad
g_0(A,B)=\frac12\operatorname{Tr}(AB).
\]

For the constant physical-unit branch,

\[
L_x=L_*.
\]

## 2. Spatial transport

The parent TIR spatial transport is

\[
W_{xy}^{X}\in SU(2),
\]

with adjoint action

\[
\boxed{
R_{xy}=\operatorname{Ad}(W_{xy}^{X})\in SO(3).
}
\]

Since `R_xy` preserves `g_0`, pure rotational transport is compatible with calibrated physical metrics exactly when adjacent local scale parameters agree:

\[
\boxed{
T_{xy}=R_{xy},
\quad
g_y(T_{xy}A,T_{xy}B)=g_x(A,B)
\iff
L_y=L_x.
}
\]

Thus a metric-compatible connected pure-rotation spatial component carries one common physical length calibration.

## 3. Varying local calibration

For positive local calibrations `L_x,L_y`, the metric-compatible transport in the same rotational direction is

\[
\boxed{
C_{xy}=\frac{L_x}{L_y}R_{xy}.
}
\]

Indeed,

\[
g_y(C_{xy}A,C_{xy}B)=g_x(A,B).
\]

The scalar transport factor is

\[
\boxed{s_{xy}=L_x/L_y.}
\]

## 4. Scale-loop closure

For a closed loop

\[
\gamma:x_0\to x_1\to\cdots\to x_n=x_0,
\]

node-induced scale factors telescope:

\[
\boxed{
S_\gamma
=\prod_{k=0}^{n-1}\frac{L_{x_k}}{L_{x_{k+1}}}
=1.
}
\]

The rotational loop factor remains

\[
\boxed{
R_\gamma
=\prod_{k=0}^{n-1}R_{x_kx_{k+1}}
\in SO(3).
}
\]

Hence scale closure and rotational holonomy are separately typed.

## 5. Transported endpoint composition

Relations from distinct local frames are composed only after transport into one comparison frame. On the common-scale branch,

\[
\boxed{
\mathcal E_{xz}^{(x)}
=
\mathcal E_{xy}^{(x)}
+R_{xy}\mathcal E_{yz}^{(y)}.
}
\]

In the matrix carrier,

\[
\boxed{
\mathcal E_{xz}^{(x)}
=
\mathcal E_{xy}^{(x)}
+W_{xy}^{X}\mathcal E_{yz}^{(y)}(W_{xy}^{X})^\dagger.
}
\]

For varying calibration, replace `R_xy` by the metric-compatible conformal transport `C_xy`.

## 6. Closure defect

Define

\[
\boxed{
\mathcal C_{xyz}
=
\mathcal E_{xz}^{(x)}
-\left(
\mathcal E_{xy}^{(x)}
+R_{xy}\mathcal E_{yz}^{(y)}
\right).
}
\]

The zero-defect branch is

\[
\boxed{\mathcal C_{xyz}=0.}
\]

This is the calibrated local-carrier version of the existing endpoint-closure interface.

## 7. Updated geometry chain

\[
\boxed{
\begin{aligned}
\operatorname{Herm}_0(2)
&\xrightarrow{g_0}
\text{local Euclidean geometry}\\
&\xrightarrow{L_*}
\text{calibrated local length geometry}\\
&\xrightarrow{W_{xy}^{X},\,\operatorname{Ad}}
\text{metric-compatible local-carrier gluing}\\
&\xrightarrow{R_\gamma,\,\mathcal C}
\text{holonomy / closure sectors}\\
&\longrightarrow
\text{tetrahedral refinement / curvature / torsion}.
\end{aligned}
}
\]

## 8. Current frontier

The next theorem programme is now sharply defined:

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
\text{refinement curvature/torsion}.
}
\]

The active task is to bind the allowed `W_ij` loop-holonomy and closure sectors to a tetrahedral refinement law while preserving the metric-compatibility result above.
