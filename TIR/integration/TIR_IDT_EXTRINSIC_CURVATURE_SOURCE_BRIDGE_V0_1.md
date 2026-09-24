# TIR × IDT Extrinsic-Curvature Source Bridge v0.1

Status: CONDITIONAL_EXTRINSIC_CURVATURE_SOURCE_THEOREM / REPARAMETRIZATION_INVARIANT_NORMAL_STRAIN / DISCRETE_GRAM_REFERENCE_PASS / CP1_TO_TIR_PURE_STATE_REPRESENTATION_SEAM_EXACT / PHYSICAL_SAME_STATE_BINDING_OPEN

Date: 2026-09-24

## 1. Purpose

The current TIR gravity spine no longer treats the ADM shift as a fundamental physical source. The remaining dynamical question is whether the temporal branch can generate the deformation tensor

\[
K_{ij}
\]

or equivalently the normal evolution of the spatial metric.

This bridge combines the existing TIR spatial coframe/metric construction with the existing IDT activity-derived temporal flow. The result is exact conditional mathematics once one additional cross-repository binding is admitted:

\[
\boxed{
\Xi:\mathcal M_{\rm IDT}\longrightarrow
\mathcal G_{\rm TIR},
}
\]

where \(\Xi\) assigns the same evolving relational state used by IDT to a smooth family of TIR coframes or metrics.

The existence of a representation overlap does not by itself establish this physical same-state binding.

## 2. Parent TIR geometry

TIR supplies a spatial coframe

\[
e^a=e^a{}_i\,dx^i
\]

and

\[
\boxed{
h_{ij}=\delta_{ab}e^a{}_i e^b{}_j.
}
\]

The primitive discrete spatial relation is

\[
\boxed{
\mathcal E_{xy}=2(\rho_y-\rho_x)
}
\]

with the Hilbert--Schmidt inner product on the local \(\operatorname{Herm}_0(2)\) carrier.

The Cartan refinement gate supplies a smooth coframe family under its declared refining assumptions.

## 3. Parent IDT temporal flow

IDT 01A supplies

\[
\boxed{
d\Theta_x=\mathfrak a_x\,d\lambda,
\qquad
\mathfrak a_x>0,
}
\]

and the local relational-state flow

\[
\boxed{
\frac{dx^A}{d\lambda}
=
-G^{AB}\partial_B\mathcal I
+
J^A{}_C G^{CB}\partial_B\mathcal H.
}
\]

Define

\[
V_\lambda^A
:=
-G^{AB}\partial_B\mathcal I
+
J^A{}_C G^{CB}\partial_B\mathcal H.
\]

Then the intrinsic-time state velocity is

\[
\boxed{
U^A
:=
\frac{dx^A}{d\Theta_x}
=
\frac{V_\lambda^A}{\mathfrak a_x}.
}
\]

Under any increasing relabeling \(\lambda\mapsto\lambda'\),

\[
V_{\lambda'}^A
=
V_\lambda^A\frac{d\lambda}{d\lambda'},
\qquad
\mathfrak a_x'
=
\mathfrak a_x\frac{d\lambda}{d\lambda'},
\]

so

\[
\boxed{
\frac{V_{\lambda'}^A}{\mathfrak a_x'}
=
\frac{V_\lambda^A}{\mathfrak a_x}.
}
\]

The intrinsic state velocity is therefore reparameterization invariant.

## 4. Conditional metric-strain theorem

Assume the cross-repository binding \(\Xi\) is smooth enough that

\[
h_{ij}=h_{ij}(x^A,\mathbf y)
\]

on a common relational/spatial patch.

Holding the spatial chart coordinate \(\mathbf y\) fixed along the normal evolution,

\[
\boxed{
\frac{\partial h_{ij}}{\partial\Theta_x}
=
U^A\partial_A h_{ij}
=
\frac{V_\lambda^A}{\mathfrak a_x}\partial_A h_{ij}.
}
\]

In the zero-shift normal gauge with the sign convention already used by the TIR spatial-temporal closure interface,

\[
K_{ij}
=
-\frac12
\frac{\partial h_{ij}}{\partial\Theta_x}.
\]

Hence

\[
\boxed{
K_{ij}^{\rm IDT\to TIR}
=
-\frac{1}{2\mathfrak a_x}
V_\lambda^A\partial_A h_{ij}.
}
\]

Substituting the IDT response law,

\[
\boxed{
K_{ij}^{\rm IDT\to TIR}
=
\frac{1}{2\mathfrak a_x}
\left(
G^{AB}\partial_B\mathcal I
-
J^A{}_C G^{CB}\partial_B\mathcal H
\right)
\partial_A h_{ij}.
}
\]

No new fitted coefficient is introduced by this bridge.

## 5. Relational lapse cancellation

IDT 01AD supplies a reference clock with

\[
N_R(x|r)=\frac{\mathfrak a_x}{\mathfrak a_r}.
\]

Using the reference temporal coordinate \(\Theta_r\),

\[
\frac{\partial h_{ij}}{\partial\Theta_r}
=
\frac{V_\lambda^A}{\mathfrak a_r}\partial_A h_{ij}.
\]

The ADM normal-gauge relation is

\[
K_{ij}
=
-\frac{1}{2N_R}
\frac{\partial h_{ij}}{\partial\Theta_r}.
\]

Therefore

\[
\boxed{
K_{ij}
=
-\frac{1}{2\mathfrak a_x}
V_\lambda^A\partial_A h_{ij}.
}
\]

The reference activity \(\mathfrak a_r\) cancels exactly.

This is the key convention check: the IDT activity ratio does not create an additional independent gravity coefficient.

## 6. General shift representation

For a nonzero matching shift,

\[
\boxed{
K_{ij}
=
\frac{1}{2N_R}
\left(
D_i\beta_j+D_j\beta_i
-
\frac{V_\lambda^A}{\mathfrak a_r}\partial_A h_{ij}
\right).
}
\]

The \(\beta\) term is representation/gauge data for the chosen foliation and coordinate matching. It is not promoted to a standalone physical source.

The normal-gauge theorem above isolates the physical deformation content from this shift freedom.

## 7. Discrete TIR relation derivative

Let one anchor state and three independent neighboring states define local relation vectors

\[
\mathcal E_I
=
2(\rho_I-\rho_0),
\qquad I=1,2,3.
\]

If the admitted temporal state binding supplies \(\dot\rho=d\rho/d\Theta\), then exactly

\[
\boxed{
\dot{\mathcal E}_I
=
2(\dot\rho_I-\dot\rho_0).
}
\]

Define the local relation Gram matrix

\[
\boxed{
\mathsf G_{IJ}
=
\frac12
\operatorname{Tr}(\mathcal E_I\mathcal E_J).
}
\]

Its temporal derivative is

\[
\boxed{
\dot{\mathsf G}_{IJ}
=
\frac12\operatorname{Tr}
\left(
\dot{\mathcal E}_I\mathcal E_J
+
\mathcal E_I\dot{\mathcal E}_J
\right).
}
\]

This formula is invariant under a common time-dependent internal orthogonal frame rotation when the corresponding covariant temporal derivative is used. For the metric Gram itself, a common \(SO(3)\) re-expression leaves the value unchanged.

Under the existing smooth-refinement assumptions, the normalized relation Gram converges to the coordinate spatial metric, so the discrete strain is the finite relation-level precursor of \(\partial_\Theta h_{ij}\).

## 8. CP1 representation seam

IDT already contains a \(\mathbb{CP}^1\) qubit-state carrier. For a normalized pure state

\[
|\psi\rangle,
\]

the standard density map is

\[
\boxed{
\rho_\psi=|\psi\rangle\langle\psi|
=
\frac12(I+\mathbf n\cdot\boldsymbol\sigma).
}
\]

This lies on the pure-state boundary of the same trace-one Hermitian two-level affine carrier used by the TIR spatial branch.

Therefore the representation-level map

\[
\boxed{
\mathbb{CP}^1
\longrightarrow
\{\rho:\rho^2=\rho,\ \operatorname{Tr}\rho=1\}
\subset
\mathcal A_2
}
\]

is exact.

This closes a representation seam only.

It does not prove

\[
\boxed{
\text{physical IDT temporal state}
=
\text{physical TIR spatial endpoint state}.
}
\]

That same-state physical binding remains OPEN.

## 9. Gauge and physical firewall

The following statements are prohibited without the remaining binding:

1. IDT phase flow is automatically spatial metric flow;
2. every IDT CP1 memory state is a physical TIR spatial locus;
3. the ADM shift is a physical observable;
4. a synthetic NOEMA/PhaseNav state is a production spacetime realization;
5. the conditional formula for \(K_{ij}\) closes full physical gravity by itself.

The allowed present statement is:

> If the evolving IDT relational state is physically identified with the state family that generates the TIR coframe/metric, then the IDT activity-normalized response flow determines the normal spatial strain and therefore \(K_{ij}\) without a new fitted coefficient.

## 10. Promotion ledger

- IDT \(d\Theta=\mathfrak a\,d\lambda\): CLOSED PARENT
- IDT tensor-scalar response flow: CLOSED/CANDIDATE PARENT ON DECLARED SECTOR
- \(V_\lambda/\mathfrak a\) reparameterization invariance: PASS EXACT
- TIR \(h_{ij}=\delta_{ab}e^a_i e^b_j\): CLOSED CONDITIONAL GEOMETRY PARENT
- chain-rule metric strain: PASS EXACT CONDITIONAL
- relational lapse cancellation: PASS EXACT
- normal-gauge \(K_{ij}\) formula: PASS EXACT CONDITIONAL
- discrete edge derivative: PASS EXACT
- discrete Gram derivative: PASS EXACT
- common \(SO(3)\) frame invariance of Gram strain: PASS EXACT
- CP1 pure-state density-map seam: PASS EXACT REPRESENTATION
- physical IDT-state to TIR-state identity: OPEN
- production refining relational family carrying that identity: OPEN INPUT
- full Einstein constraints/evolution after source binding: DOWNSTREAM TEST

## 11. Smallest remaining physical gate

The next gate is no longer

\[
\text{fundamentals}\to\beta_{\rm match}.
\]

It is

\[
\boxed{
\text{physical same-state binding } \Xi
:
x_{\rm IDT}(\Theta)
\longleftrightarrow
\rho_{\rm TIR}(\Theta)
}
\]

together with one admitted production refining family.

Once \(\Xi\) is established, this theorem provides the direct source map

\[
\boxed{
\text{IDT activity/response}
\to
\partial_\Theta h_{ij}
\to
K_{ij}
\to
\text{ADM/Einstein closure}.
}
\]

Reference validator:

TIR/validation/tir_idt_extrinsic_curvature_source_bridge_v0_1.py
