# Scale-Compatible Local Carrier Gluing v0.1

Status: `EXACT_LOCAL_METRIC_COMPATIBLE_GLUING_THEOREM_CANDIDATE`

Scope: glue the calibrated local relation carriers of `The Space of Geometry` using the existing TIR `SU(2)` spatial transport and determine exactly how the physical length calibration behaves across adjacent local frames.

## 1. Local calibrated carriers

At each local site `x`, let

\[
V_x\cong\operatorname{Herm}_0(2)
\]

with dimensionless reference metric

\[
g_0(A,B)=\frac12\operatorname{Tr}(AB)
\]

and calibrated physical metric

\[
\boxed{
g_x=L_x^2g_0,
\qquad L_x>0.
}
\]

The constant-scale branch is the special case

\[
L_x=L_*
\]

on every site of a connected spatial component.

## 2. Existing TIR spatial transport

Let the spatial transport on an oriented edge be

\[
W_{xy}^{X}\in SU(2).
\]

Its adjoint action on the traceless Hermitian carrier is

\[
\boxed{
R_{xy}=\operatorname{Ad}(W_{xy}^{X})\in SO(3).
}
\]

Therefore

\[
g_0(R_{xy}A,R_{xy}B)=g_0(A,B).
\]

## 3. Pure rotational metric compatibility

Suppose the edge transport is purely rotational,

\[
T_{xy}=R_{xy}.
\]

Then

\[
\begin{aligned}
g_y(T_{xy}A,T_{xy}B)
&=L_y^2g_0(R_{xy}A,R_{xy}B)\\
&=L_y^2g_0(A,B).
\end{aligned}
\]

Exact physical metric compatibility requires

\[
g_y(T_{xy}A,T_{xy}B)=g_x(A,B)=L_x^2g_0(A,B)
\]

for all `A,B`. Hence

\[
\boxed{L_y=L_x.}
\]

Thus pure `SU(2) -> SO(3)` spatial transport propagates one common physical length calibration across every connected component on which metric compatibility is imposed.

For the constant branch,

\[
\boxed{
L_x=L_*
\quad\Longrightarrow\quad
T_{xy}=R_{xy}\in SO(3)
\text{ is physically length preserving.}
}
\]

## 4. Conformal transport for locally varying calibration

If neighboring sites carry positive local calibrations `L_x` and `L_y`, define

\[
\boxed{
C_{xy}:=\frac{L_x}{L_y}R_{xy}.
}
\]

Then

\[
\begin{aligned}
g_y(C_{xy}A,C_{xy}B)
&=L_y^2\left(\frac{L_x}{L_y}\right)^2
  g_0(R_{xy}A,R_{xy}B)\\
&=L_x^2g_0(A,B)\\
&=g_x(A,B).
\end{aligned}
\]

Therefore

\[
\boxed{
C_{xy}=\frac{L_x}{L_y}R_{xy}
}
\]

is the unique positive scalar multiple of the established rotational transport that preserves the calibrated physical metric between two differently normalized local carriers.

The scalar edge factor is

\[
\boxed{s_{xy}=\frac{L_x}{L_y}.}
\]

## 5. Scale-loop closure

For a closed loop

\[
\gamma:x_0\to x_1\to\cdots\to x_n=x_0,
\]

the product of node-induced scale factors is

\[
\prod_{k=0}^{n-1}s_{x_kx_{k+1}}
=
\prod_{k=0}^{n-1}\frac{L_{x_k}}{L_{x_{k+1}}}
=1.
\]

Hence a single-valued local calibration field produces

\[
\boxed{S_\gamma=1.}
\]

The conformal scale part closes exactly around every loop, while the rotational part may retain nontrivial holonomy

\[
\boxed{
R_\gamma
=R_{x_0x_1}R_{x_1x_2}\cdots R_{x_{n-1}x_0}
\in SO(3).
}
\]

Thus rotational holonomy and calibration closure are cleanly separated.

## 6. Relation composition across local frames

Let `E_xy^(x)` denote the relation from `x` to `y` expressed in the carrier frame at `x`. For a second edge `y -> z`, transport its relation into the `x` frame before composing.

On the common-scale branch,

\[
\boxed{
\mathcal E_{xz}^{(x)}
=
\mathcal E_{xy}^{(x)}
+R_{xy}\mathcal E_{yz}^{(y)}.
}
\]

Equivalently, in the parent TIR matrix carrier,

\[
\boxed{
\mathcal E_{xz}^{(x)}
=
\mathcal E_{xy}^{(x)}
+W_{xy}^{X}\mathcal E_{yz}^{(y)}(W_{xy}^{X})^\dagger.
}
\]

With locally varying calibration and metric-compatible conformal transport, replace `R_xy` by `C_xy`.

This is the local-carrier gluing form of endpoint composition.

## 7. Closure defect and downstream geometry

Define the transported endpoint-closure defect

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

The exact zero-defect branch is

\[
\boxed{\mathcal C_{xyz}=0.}
\]

Nontrivial loop rotation `R_gamma`, endpoint-closure defect, and their refinement limits are the existing TIR entry points to holonomy, curvature and torsion analysis. This theorem supplies the missing calibrated-carrier compatibility layer before that downstream step.

## 8. Dependency result

The geometry chain is now

\[
\boxed{
\begin{aligned}
V_x&\cong\operatorname{Herm}_0(2),\\
g_x&=L_x^2g_0,\\
W_{xy}^{X}&\in SU(2),\\
R_{xy}&=\operatorname{Ad}(W_{xy}^{X})\in SO(3),\\
L_x=L_y&\Longleftrightarrow\text{ pure rotational physical metric compatibility},\\
C_{xy}&=(L_x/L_y)R_{xy}\quad\text{for varying local calibration}.
\end{aligned}
}
\]

The next gluing frontier is to bind the allowed loop holonomy and endpoint-closure sectors to the parent TIR `W_ij` laws and then pass to controlled tetrahedral refinement.

## 9. Claim classes

| Statement | Class |
|---|---|
| `Ad(W_xy^X) in SO(3)` | ESTABLISHED TIR SPATIAL TRANSPORT |
| pure rotational transport preserves `g_0` | EXACT |
| physical metric compatibility under pure rotation implies `L_x=L_y` | EXACT |
| `C_xy=(L_x/L_y)R_xy` preserves `g_x -> g_y` | EXACT |
| node-induced scale factors telescope to one around a loop | EXACT |
| rotational holonomy may remain in `SO(3)` | EXACT GROUP-THEORETIC STRUCTURE |
| transported endpoint composition | EXACT LOCAL FRAME COMPOSITION RULE |
| closure defect is the gluing diagnostic entering curvature/torsion refinement | TIR DOWNSTREAM INTERFACE |
