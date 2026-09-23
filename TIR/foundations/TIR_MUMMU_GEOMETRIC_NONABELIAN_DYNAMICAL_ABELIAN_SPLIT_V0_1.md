# TIR MUMMU Geometric-Non-Abelian / Dynamical-Abelian Split v0.1

Status: `EXACT_FIXED_AMPLITUDE_PHASE_HAMILTONIAN / EXACT_DYNAMICAL_COMMUTATOR_ZERO / EXACT_GEOMETRIC_CONNECTION_NONCOMMUTATIVITY / INTERPRETATION_FIREWALL`

Date: 2026-09-23

## 1. Purpose

The coefficient-free observed-hydro lane produces a nonzero commutator for the
local horizontal (CP^1) connection.

That result must not be conflated with a noncommuting physical/dynamical
Hamiltonian.

For the frozen-amplitude policy the underlying phase evolution has an exact
diagonal Hermitian generator.  This theorem separates the two structures.

## 2. Fixed-amplitude pair state

For one admitted pair let

\[
|psi\rangle
=
\frac1{sqrt q}
\begin{pmatrix}
sqrt{p_L},e^{i\theta_L}\
sqrt{p_R},e^{i\theta_R}
end{pmatrix},
\]

with (p_L,p_R) constant along the bound hydro trace.

Let

\[
v_L=dot\theta_L,
qquad
v_R=dot\theta_R,
qquad
dotdelta=v_R-v_L.
\]

Then

\[
dotpsi
=
i
\begin{pmatrix}
v_L&0\
0&v_R
end{pmatrix}
psi.
\]

Therefore

\[
\boxed{
idotpsi
=
H_{\rm phase}psi
}
\]

with

\[
\boxed{
H_{\rm phase}
=
-
\begin{pmatrix}
v_L&0\
0&v_R
end{pmatrix}.
}
\]

## 3. Pauli decomposition

Write

\[
c
=
-\frac{v_L+v_R}{2}.
\]

Then

\[
\boxed{
H_{\rm phase}
=
cI
+
\frac{dotdelta}{2}sigma_z.
}
\]

Hence every section belongs to the same Abelian algebra

\[
operatorname{span}{I,sigma_z}.
\]

For any two proper-time sections,

\[
\boxed{
\[
H_{\rm phase}(\tau_1),
H_{\rm phase}(\tau_2)
\]
=
0.
}
\]

Thus the frozen-amplitude hydrodynamic wave lane is dynamically Abelian in this
fixed computational basis.

## 4. Bloch dynamics

Let

\[
mathbf n
=
(rcosdelta,rsindelta,u),
qquad
r=sqrt{1-u^2}.
\]

The traceless dynamical field is

\[
mathbf h
=
(0,0,dotdelta).
\]

The Bloch equation is

\[
\boxed{
dot{mathbf n}
=
mathbf h\timesmathbf n.
}
\]

The horizontal/geometric generator is

\[
\boldsymbol\Omega
=
mathbf n\timesdot{mathbf n}.
\]

Using the vector triple-product identity,

\[
\boxed{
\boldsymbol\Omega
=
mathbf h
-
(mathbf ncdotmathbf h)mathbf n.
}
\]

Thus (\boldsymbolOmega) is the component of the dynamical rotation vector
orthogonal to the instantaneous projective state.

For the fixed-imbalance latitude,

\[
\boxed{
\boldsymbol\Omega
=
dotdelta
(-urcosdelta,,-ursindelta,,r^2).
}
\]

## 5. Why the geometric generators can fail to commute

Although (mathbf h) always points along the fixed (z) axis, the projection

\[
mathbf h
mapsto
mathbf h-(mathbf ncdotmathbf h)mathbf n
\]

depends on the moving state (mathbf n(\tau)).

Therefore the horizontal generator direction can rotate in
(mathfrak{su}(2)).

Define

\[
mathcal A_{\rm geom}(\tau)
=
-\frac{i}{2}
\boldsymbol\Omega(\tau)cdot\boldsymbolsigma.
\]

Then

\[
\boxed{
\[
mathcal A_{\rm geom}(\tau_1),
mathcal A_{\rm geom}(\tau_2)
\]
=
-\frac{i}{2}
left(
\boldsymbolOmega_1\times\boldsymbolOmega_2
\right)cdot\boldsymbolsigma.
}
\]

Thus it is possible to have simultaneously

\[
\boxed{
[H_{\rm phase}(\tau_1),H_{\rm phase}(\tau_2)]=0
}
\]

and

\[
\boxed{
[mathcal A_{\rm geom}(\tau_1),mathcal A_{\rm geom}(\tau_2)]
e0.
}
\]

There is no contradiction: the objects describe different connections.

## 6. Deterministic observed-hydro witness

For the pinned coefficient-free source-component fixture, pair 9 at replay
sections 50 and 100 gives

\[
|Omega_{50}\timesOmega_{100}|
approx
5.440204449331002\times10^{-6}.
\]

Therefore

\[
\boxed{
left|
\[
mathcal A_{50},mathcal A_{100}
\]
\right|_F
=
\frac{
|Omega_{50}\timesOmega_{100}|
}{sqrt2}
approx
3.846805457163179\times10^{-6}.
}
\]

At the same two sections,

\[
\boxed{
[H_{{\rm phase},50},H_{{\rm phase},100}]
=0
}
\]

exactly.

## 7. Relation to the minimum-Frobenius lift

The previously defined (H_{min}) is the unique minimum-Frobenius Hermitian
operator satisfying

\[
H_{min}psi=idotpsi
\]

at one known state/tangent pair.

The diagonal (H_{\rm phase}) also satisfies that equation for the
frozen-amplitude phase trajectory.

They need not be the same operator because one state/tangent pair does not fix
the operator on the orthogonal complement.

Their difference obeys

\[
\boxed{
(H_{\rm phase}-H_{min})psi=0.
}
\]

Thus:

- (H_{\rm phase}) is selected by the known coordinate-wise phase law;
- (H_{min}) is selected by minimum Frobenius norm among all Hermitian lifts;
- (mathcal A_{\rm geom}) is the horizontal projective connection.

These three operators must not be silently identified.

## 8. Interpretation firewall

The coefficient-free witness establishes:

\[
\boxed{
\text{non-Abelian projective/horizontal geometry}
}
\]

inside the composed model.

It does **not** by itself establish:

\[
\boxed{
\text{a non-Abelian dynamical interaction Hamiltonian}.
}
\]

Any later physical claim requiring non-Abelian dynamical forces must provide a
separate source-derived Hamiltonian with nonzero time-separated commutators.

## 9. Claim ledger

| Statement | Status |
|---|---|
| fixed-amplitude phase evolution has diagonal (H_{\rm phase}) | `EXACT` |
| (H_{\rm phase}) lies in (operatorname{span}{I,sigma_z}) | `EXACT` |
| time-separated (H_{\rm phase}) commute | `EXACT` |
| (dot n=h\times n) | `EXACT` |
| (Omega=h-(ncdot h)n) | `EXACT` |
| geometric connection may be noncommuting | `EXACT` |
| pinned geometric commutator is nonzero | `NUMERIC PASS` |
| geometric noncommutativity proves non-Abelian dynamical forces | `REFUTED` |
| physical neutrino/gravity realization | `OPEN / NOT CLAIMED` |

## 10. Validation

Deterministic validator:

`TIR/validation/tir_mummu_geometric_nonabelian_dynamical_abelian_split_v0_1.py`

Static receipt:

`TIR/validation/TIR_MUMMU_GEOMETRIC_NONABELIAN_DYNAMICAL_ABELIAN_SPLIT_VALIDATION_V0_1.json`
