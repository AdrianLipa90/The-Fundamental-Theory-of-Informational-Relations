# TIR Inter-Leaf Shift to Orbital Rapidity and Invariant Mass Bridge v0.1

Status: EXACT_KINEMATIC_BINDING / PARAMETER_FREE_SHIFT_TO_RAPIDITY / SPHERICAL_MISNER_SHARP_INVARIANT_CROSSWALK / PRODUCTION_MATCHING_INPUT_OPEN

Date: 2026-09-24

Parents:
- TIR_INTERLEAF_MATCHING_FIELD_INPUT_CONTRACT_V0_1
- TIR_SPATIAL_TEMPORAL_CLOSURE_INTERFACE_V0_1
- TIR_FRACTAL_ORBITAL_INFORMATIONAL_HOLONOMIC_GRAVITY_V0_1
- TIR_FLOW_COFRAME_ADM_CONSTRAINT_GRAVITY_V0_1

## 1. Purpose

The gravity branch previously left a source-to-rapidity gate open. The native TIR spacetime interface already supplies a more direct kinematic object: the inter-leaf matching field.

For coordinate time \(t\), TIR exports

\[
\boxed{b^i_{(0)}=\frac{\beta^i_{(t)}}{c}},
\qquad x^0=ct.
\]

The flow-coframe convention used by the fractal-orbital gravity branch is

\[
\vartheta^a=e^a{}_i\left(dx^i-\frac{V^i}{c}dx^0\right).
\]

Comparison with the TIR/RF-E8 coframe

\[
\vartheta^a=e^a{}_i(dx^i+b^i_{(0)}dx^0)
\]

gives the exact sign-convention bridge

\[
\boxed{V^i=-c\,b^i_{(0)}=-\beta^i_{(t)}.}
\]

No new scale or fitted coefficient is introduced.

## 2. Shift norm and rapidity

Let the spatial metric be \(h_{ij}\) and define

\[
b^2=h_{ij}b^i b^j.
\]

On the subluminal chart sector

\[
0\le b^2<1,
\]

the flow speed satisfies

\[
\boxed{\frac{|V|}{c}=|b|.}
\]

Therefore define the orbital rapidity

\[
\boxed{\chi=\operatorname{artanh}|b|.}
\]

The associated Poincare-disk radius is

\[
\boxed{q=\tanh\frac{\chi}{2}}
\]

and equivalently

\[
\boxed{
q=\frac{|b|}{1+\sqrt{1-b^2}}
=
\frac{1-\sqrt{1-b^2}}{|b|}
}
\]

for \(|b|>0\), with \(q=0\) at \(b=0\).

Thus the chain

\[
\boxed{
\beta_{\rm match}
\longrightarrow
b
\longrightarrow
V
\longrightarrow
\chi
\longrightarrow
q
}
\]

is exact after the temporal coordinate and sign convention are fixed.

This is a kinematic representation bridge, not a claim that the shift itself is a gauge-invariant gravitational source.

## 3. Metric equivalence

In \(x^0=ct\) units with unit lapse, the ADM block is

\[
ds^2=-(dx^0)^2+
h_{ij}(dx^i+b^i dx^0)(dx^j+b^j dx^0).
\]

Substituting \(b^i=-V^i/c\) gives

\[
\boxed{
ds^2=-(dx^0)^2+
h_{ij}\left(dx^i-\frac{V^i}{c}dx^0\right)
\left(dx^j-\frac{V^j}{c}dx^0\right),
}
\]

which is exactly the flow-coframe metric.

Therefore the parent flow representation is already present in the TIR inter-leaf ADM interface up to sign convention.

## 4. Gauge firewall

The ADM shift is coordinate/slicing dependent. Therefore the following inference is forbidden:

\[
\text{nonzero }b^i
\Longrightarrow
\text{new physical gravitational field}.
\]

Physical content must be read from the full spacetime geometry or a gauge-invariant/covariant observable built from it.

In particular, local Lorentz or coordinate re-expression may change the shift while leaving the spacetime invariant.

The role of \(b\), \(V\), \(\chi\), and \(q\) in this bridge is therefore representational.

## 5. Spherical invariant mass crosswalk

For the radial unit-lapse flat-slice metric

\[
ds^2=-c^2dt^2+(dr-Vdt)^2+r^2d\Omega^2,
\]

the \(t,r\) block is

\[
g_{ab}=
\begin{pmatrix}
-(c^2-V^2) & -V\\
-V & 1
\end{pmatrix}.
\]

Its inverse obeys

\[
\boxed{g^{rr}=1-\frac{V^2}{c^2}.}
\]

For spherical symmetry with areal radius \(r\), define the Misner--Sharp mass by

\[
\boxed{
1-\frac{2Gm_{\rm MS}}{c^2r}
=
g^{ab}\nabla_a r\nabla_b r.
}
\]

Since \(\nabla_a r\) selects the radial coordinate,

\[
g^{ab}\nabla_a r\nabla_b r=g^{rr},
\]

and therefore

\[
\boxed{
m_{\rm MS}(r,t)=\frac{rV^2(r,t)}{2G}
=
\frac{c^2r}{2G}b^2(r,t).
}
\]

This quantity is invariantly defined by the spherical geometry and areal radius, unlike the shift by itself.

The orientation sign \(V\mapsto -V\) leaves \(m_{\rm MS}\) unchanged.

## 6. Vacuum result

The downstream ADM gate derives

\[
V^2=\frac Cr
\]

in stationary spherical vacuum.

Therefore

\[
\boxed{
m_{\rm MS}=\frac{C}{2G}=\text{constant}.
}
\]

With asymptotic mass normalization \(C=2GM\),

\[
\boxed{m_{\rm MS}=M.}
\]

Thus the condition

\[
\frac{d}{dr}(rV^2)=0
\]

is equivalently

\[
\boxed{\frac{dm_{\rm MS}}{dr}=0}
\]

for the stationary vacuum branch.

This recasts the river-flow result in terms of an invariant mass observable.

## 7. Consequence for the historical B omega N / AR source

The gravity construction no longer needs to identify the historical amplitude-like source expression with rapidity.

The historical source may remain a separate candidate dynamical or wave-sector input, but the TIR-native spacetime chain is now

\[
\boxed{
\text{TIR spatial coframe}
+
\text{inter-leaf matching field}
\to
\text{ADM spacetime coframe}
\to
\text{flow representation}
\to
\text{rapidity/Poincare coordinate}.
}
\]

The open physical gate moves upstream:

\[
\boxed{
\text{fundamental/source dynamics}
\to
\beta_{\rm match}(x)
}
\]

for a genuine production realization.

The repository already records that production \(\beta_{\rm match}\) is OPEN INPUT.

## 8. Promotion ledger

- beta(t) to dimensionless x0 shift: PASS EXACT EXISTING TIR CONTRACT
- shift to flow velocity: PASS EXACT SIGN-CONVENTION BRIDGE
- shift norm to rapidity: PASS EXACT ON SUBLUMINAL SECTOR
- rapidity to Poincare radius: PASS EXACT
- flow metric equals ADM shift metric: PASS EXACT
- spherical flow to Misner-Sharp mass: PASS EXACT
- stationary vacuum implies constant Misner-Sharp mass: PASS CONDITIONAL
- production beta_match dataset: OPEN INPUT
- microscopic/fundamental dynamics generating beta_match: OPEN
- shift itself as physical source: FORBIDDEN PROMOTION

## 9. Falsification surface

This bridge fails if:
1. the TIR x0 shift conversion differs from \(b=\beta_t/c\);
2. the coframe sign map fails to reproduce the same metric;
3. rapidity is used outside the subluminal real chart without a separate continuation;
4. the inverse radial metric does not give \(g^{rr}=1-V^2/c^2\);
5. the Misner-Sharp definition does not reduce to \(rV^2/(2G)\);
6. a gauge-dependent shift is reported as a standalone physical source;
7. an absent production matching dataset is silently replaced by a synthetic/runtime vector.

Reference validator:

TIR/foundations/validation/tir_interleaf_shift_orbital_rapidity_mass_bridge_v0_1.py
