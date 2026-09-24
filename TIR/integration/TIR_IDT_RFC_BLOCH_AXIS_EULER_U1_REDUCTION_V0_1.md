# TIR × IDT × RFC Bloch-Axis Euler \(U(1)\) Reduction v0.1

Status: LOCAL_SO3_TO_SO2_STABILIZER_EXACT / EULER_PROJECTED_CONNECTION_GAUGE_LAW_EXACT / SPIN_HALF_2PI_4PI_RECOVERY_EXACT / ABSOLUTE_AXIS_ORIENTATION_NOT_REQUIRED / INTERNAL_TO_SPACETIME_SOLDER_BINDING_OPEN

Date: 2026-09-24

## 1. Purpose

The Euler–Palatini torsion gate uses the candidate local projection

\[
\mathcal A_E
=
\frac{s_E}{2}n_{ab}\omega^{ab},
\qquad
s_E=\frac12,
\]

where \(\omega^{ab}\) is the spatial rotational part of the RFC Lorentz connection and \(n_{ab}\) must select one local spin-axis generator.

This gate proves that, once a unit axis is supplied on the local spatial frame, the stabilizer reduction is exactly

\[
SO(3)\longrightarrow SO(2)\simeq U(1),
\]

and that the projected RFC connection transforms with the same sign convention as the existing phase connection.

It does not by itself identify the internal TIR \(A_1/CP^1\) axis with the RFC spacetime coframe.

## 2. Unit spin-axis carrier

Let

\[
s^a s_a=1,
\qquad
a=1,2,3,
\]

be a local oriented unit axis in the RFC spatial orthonormal frame.

Define

\[
\boxed{
n_{ab}
:=
\epsilon_{abc}s^c.
}
\]

Then

\[
n_{ab}=-n_{ba},
\]

and

\[
\boxed{
\frac12n_{ab}n^{ab}=1.
}
\]

As an endomorphism,

\[
N^a{}_b:=n^a{}_b
\]

generates rotations about \(s^a\).

Indeed,

\[
\boxed{
N^a{}_b s^b=0.
}
\]

## 3. Stabilizer theorem

The subgroup of \(SO(3)\) preserving \(s\),

\[
H_s
:=
\{R\in SO(3):Rs=s\},
\]

acts as ordinary rotations on the oriented two-plane

\[
s^\perp.
\]

Therefore

\[
\boxed{
H_s\simeq SO(2)\simeq U(1).
}
\]

A one-parameter representative is

\[
\boxed{
R_s(\alpha)=\exp(\alpha N).
}
\]

Because \(N\) generates its own stabilizer,

\[
R_s(\alpha)NR_s(\alpha)^{-1}=N.
\]

## 4. RFC connection convention

RF-02I uses the local frame-change law

\[
\boxed{
\omega'
=
R\omega R^{-1}
-
dR\,R^{-1}.
}
\]

For the residual rotation

\[
R=R_s(\alpha),
\]

with the axis section fixed in the selected local reduction,

\[
dR\,R^{-1}=N\,d\alpha.
\]

Define the Euler projection

\[
\boxed{
\mathcal A_E
=
\frac{s_E}{2}
n_{ab}\omega^{ab}.
}
\]

The homogeneous term is invariant under the stabilizer. The inhomogeneous term gives

\[
\mathcal A_E'
=
\mathcal A_E
-
\frac{s_E}{2}
n_{ab}n^{ab}\,d\alpha.
\]

Using

\[
\frac12 n_{ab}n^{ab}=1,
\]

one obtains exactly

\[
\boxed{
\mathcal A_E'
=
\mathcal A_E-s_E\,d\alpha.
}
\]

## 5. Exact \(U(1)\) gauge coordinate

Define

\[
\boxed{
\lambda_E:=s_E\alpha.
}
\]

Then

\[
\boxed{
\mathcal A_E'
=
\mathcal A_E-d\lambda_E.
}
\]

This is exactly the RFC/IDT phase-connection sign convention

\[
\mathcal A'\!=\mathcal A-d\lambda,
\qquad
\vartheta'\!=\vartheta+\lambda.
\]

Therefore the phase-clock one-form

\[
q=d\vartheta+\mathcal A
\]

remains invariant under the reduced Euler rotation.

## 6. Spin-half double-cover recovery

On the spin-half branch,

\[
\boxed{
s_E=\frac12.
}
\]

A \(2\pi\) spatial rotation gives

\[
\alpha\mapsto\alpha+2\pi,
\]

hence

\[
\Delta\lambda_E
=
s_E\,2\pi
=
\pi.
\]

Thus the associated phase factor changes by

\[
\boxed{
e^{i\Delta\lambda_E}=e^{i\pi}=-1.
}
\]

A \(4\pi\) rotation gives

\[
\Delta\lambda_E
=
s_E\,4\pi
=
2\pi,
\]

so

\[
\boxed{
e^{i\Delta\lambda_E}=1.
}
\]

Hence the projected Cartan connection reproduces exactly the current TIR spin-lift rule

\[
\boxed{
2\pi\to-1,
\qquad
4\pi\to+1.
}
\]

This is not inserted as a separate periodicity condition; it follows from the normalized \(SO(2)\) projection with \(s_E=1/2\).

## 7. Relation to current TIR axis results

Current TIR already proves that normalized \(A_1\simeq\mathfrak{su}(2)\) Cartan-axis representatives lie in one \(SU(2)\) conjugacy class.

Therefore an absolute pre-breaking axis orientation is not required for the representation theorem.

This is compatible with the present local reduction: any local unit representative \(s^a\) gives an isomorphic

\[
SO(2)\simeq U(1)
\]

stabilizer and the same projected gauge law.

The unresolved issue is not which coordinate axis is called north.

The unresolved physical seam is

\[
\boxed{
\text{TIR internal }A_1/CP^1\text{ axis}
\stackrel{?}{\longrightarrow}
\text{RFC spatial Lorentz-frame axis }s^a.
}
\]

## 8. Current White-Thread spin-lift cross-check

Current TIR separately has

\[
\text{projective }U(1)\text{ closure mod }2\pi
\]

and its exact two-sheet lift

\[
\text{spin closure mod }4\pi.
\]

The present theorem reproduces the same structure from the RFC connection projection:

\[
\boxed{
SO(3)\supset SO(2)
\overset{s_E=1/2}{\longrightarrow}
U(1)\text{ phase}
\longrightarrow
4\pi\text{ spin lift}.
}
\]

Thus the two current mathematical surfaces are representation-compatible.

Their physical identity still consumes the internal-to-spacetime solder receipt.

## 9. Lorentz embedding

Embed the spatial generator into the Lorentz algebra by

\[
\boxed{
n_{0a}=0,
\qquad
n_{ab}=\epsilon_{abc}s^c.
}
\]

This selects the compact rotational stabilizer inside

\[
SO^+(1,3).
\]

No boost generator is included in the Euler \(U(1)\) reduction.

This is essential: the phase fibre is compact, while boost directions are noncompact.

## 10. Consequence for the torsion gate

The candidate adapter

\[
\mathcal A_E
=
\frac{s_E}{2}n_{AB}\omega^{AB}
\]

is now algebraically gauge-consistent on the local reduced bundle.

Therefore the Euler–Palatini connection current

\[
\mathfrak s^\mu{}_{AB}
=
\frac{
2\eta\widehat U_Ls_Ef'(1)
}{\mu_\vartheta^2}
q^\mu n_{AB}
\]

has a well-defined local \(U(1)\)-reduced rotational generator once the physical solder of \(s^a\) is admitted.

The remaining obstruction is physical binding, not the local gauge algebra.

## 11. Verdict

Exact conditional on a local unit spatial axis:

\[
\boxed{
SO(3)\to SO(2)\simeq U(1)
}
\]

\[
\boxed{
\mathcal A_E'
=
\mathcal A_E-d(s_E\alpha)
}
\]

and for \(s_E=1/2\),

\[
\boxed{
2\pi\to-1,\qquad4\pi\to+1.
}
\]

Open:

- TIR internal \(A_1/CP^1\) axis \(\leftrightarrow\) RFC spatial tetrad-axis solder;
- global existence/patching of the reduced axis section;
- defects/zeros where an axis section cannot be continued;
- physical Einstein–Cartan solution sourced by the reduced Euler current.

Reference validator:

TIR/validation/tir_idt_rfc_bloch_axis_euler_u1_reduction_v0_1.py
