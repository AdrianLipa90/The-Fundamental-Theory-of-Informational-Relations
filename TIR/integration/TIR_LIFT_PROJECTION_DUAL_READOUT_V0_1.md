# TIR Lift–Projection Dual Readout Bridge v0.1

Status: `EXACT_MATHEMATICAL_BRIDGE`

Scope: formalize the relation between a normalized two-state lift, its projective quotient, phase/holonomy data retained by a lift, and the common relational readout shared by both descriptions.

## 1. Lift and quotient

Let

\[
|\psi\rangle\in\mathbb C^2,
\qquad
\langle\psi|\psi\rangle=1.
\]

Normalized spinors form \(S^3\). Quotienting the global phase gives

\[
\boxed{S^3/U(1)\cong\mathbb{CP}^1\cong S^2.}
\]

The rank-one projector

\[
\boxed{P_\psi=|\psi\rangle\langle\psi|}
\]

is invariant under

\[
|\psi\rangle\mapsto e^{i\alpha}|\psi\rangle.
\]

Thus the projective layer intentionally forgets global \(U(1)\) phase.

## 2. Shared relational readout

For two normalized states,

\[
\boxed{
R(S,I)=|\langle S|I\rangle|^2=\operatorname{Tr}(P_SP_I).
}
\]

For pure-qubit Bloch vectors \(\mathbf n_S,\mathbf n_I\),

\[
\boxed{R(S,I)=\frac{1+\mathbf n_S\cdot\mathbf n_I}{2}.}
\]

Therefore

\[
\boxed{
\text{spinor overlap}
=
\text{projector trace}
=
\text{Bloch dot-product readout}.
}
\]

These are coordinate descriptions of the same invariant.

## 3. Information retained by a lift

A lift equipped with a connection can retain path-dependent phase and holonomy that is absent from a single ray/projector label.

The standard \(SU(2)\to SO(3)\) double cover gives the finite example: \(U\) and \(-U\) induce the same \(SO(3)\) rotation. A spinorial \(2\pi\) cycle can retain the central residue \(-I\), while the corresponding projective state has returned.

For Pauli lifts,

\[
\widetilde R=i\sigma_x,
\qquad
\widetilde E=i\sigma_z,
\qquad
\widetilde N=i\sigma_y,
\]

the generated finite subgroup is

\[
Q_8=\{\pm I,\pm i\sigma_x,\pm i\sigma_y,\pm i\sigma_z\},
\]

with

\[
\boxed{Q_8/\{\pm I\}\cong V_4.}
\]

This provides an exact example in which the quotient retains the projective operation while discarding a central lift label.

## 4. One invariant, different relation classes

The same readout

\[
R=\frac{1+\mathbf n\cdot\mathbf m}{2}
\]

gives

\[
\mathbf n\cdot\mathbf m=0
\Rightarrow
R=\frac12,
\]

whereas tetrahedral geometry gives

\[
\mathbf n_i\cdot\mathbf n_j=-\frac13
\Rightarrow
R=\frac13.
\]

Thus \(1/2\) and \(1/3\) are different values of one relation operator on different geometric relation classes; they are not competing probability rules.

## 5. Dependency

\[
\boxed{
\text{first distinction}
\to
\mathbb C^2
\to
S^3
\to
\mathbb{CP}^1
\to
P_\psi,\ R(S,I)
}
\]

with the lift-sensitive branch

\[
\boxed{
S^3+\text{connection}
\to
SU(2)\text{ transport}
\to
\text{phase / holonomy / central residue}.
}
\]

The stella distinction–holonomy foundation supplies a finite carrier on which the projective and lift-sensitive readouts coexist.

## 6. Interpretation firewall

This file proves only the mathematical lift/quotient/readout relation. Mapping this split onto named interpretations of quantum mechanics is a separate interpretive crosswalk and is not promoted to theorem status here.

## 7. Claim classes

| Statement | Status |
|---|---|
| \(S^3/U(1)\cong\mathbb{CP}^1\cong S^2\) | `STANDARD_GEOMETRIC_THEOREM` |
| \(P_\psi\) is invariant under global phase | `EXACT` |
| \(R=|\langle S|I\rangle|^2=\operatorname{Tr}(P_SP_I)\) | `EXACT` |
| \(R=(1+n_S\cdot n_I)/2\) for pure qubits | `EXACT` |
| \(SU(2)\to SO(3)\) is a double cover | `STANDARD_GROUP_THEOREM` |
| \(Q_8/\{\pm I\}\cong V_4\) in the Pauli example | `EXACT` |
| lift and quotient can share the same \(R\) while retaining different phase information | `EXACT` |
| any named interpretation is identical to one mathematical layer | `NOT CLAIMED` |
