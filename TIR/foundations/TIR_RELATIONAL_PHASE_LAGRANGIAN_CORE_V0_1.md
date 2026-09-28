# TIR Relational Phase Lagrangian Core v0.1

Status: \`SOURCE_PROMOTED_EXACT_STRUCTURAL_PHASE_CORE__PHYSICAL_TIME_BINDING_SEPARATE\`

Scope: promote the already-existing relational phase Lagrangian into the active TIR foundation without importing the archived Hilbert/\(\mathbb{CP}^1\) assumptions as parents. The phase core supplies the compact relative-phase carrier \(U(1)\cong S^1\); the Lagrangian--Bloch theorem uses it downstream.

## 1. Relative phase as a compact coordinate

A phase is represented by an angle

\[
\chi\in\mathbb R/2\pi\mathbb Z.
\]

Equivalently,

\[
\boxed{
e^{i\chi}\in U(1)
\cong
S^1.
}
\]

The identification

\[
\chi\sim\chi+2\pi k,
\qquad
k\in\mathbb Z,
\]

is the standard Euler phase closure and does not require a Bloch sphere, a Pauli algebra, or an \(SO(3)\) action.

## 2. Relational gauge transport

Let \(q^a\) denote relational configuration coordinates and let \(\mathcal A=\mathcal A_a(q)dq^a\) be a phase connection. Define

\[
\boxed{
D_\tau\chi
=
\dot\chi+\mathcal A_a(q)\dot q^a.
}
\]

Under a local phase change

\[
\chi\mapsto\chi-\lambda(q),
\qquad
\mathcal A\mapsto\mathcal A+d\lambda,
\]

one has

\[
\boxed{
D_\tau\chi\mapsto D_\tau\chi.
}
\]

Thus the covariant phase velocity is gauge invariant.

## 3. Minimal relational phase Lagrangian

The archived TIR/Metatime formal note contains the phase-first Lagrangian

\[
\boxed{
L
=
\frac12 g_{ab}(q)\dot q^a\dot q^b
+
\frac{I_\phi}{2}(D_\tau\chi)^2
+
J_0D_\tau\chi
-
V(q).
}
\]

For the foundation layer only the structural roles are retained:

- \(g_{ab}\): configuration-space metric to be selected by downstream geometry;
- \(\chi\in U(1)\): compact relative phase;
- \(\mathcal A\): relational phase connection;
- \(I_\phi>0\): positive phase inertia/normalization;
- \(V\): scalar potential.

No physical elapsed-time, mass, neutrino, electromagnetic, or gravitational identification is made here.

## 4. Phase momentum

The momentum conjugate to the phase is

\[
\boxed{
J
=
\frac{\partial L}{\partial\dot\chi}
=
I_\phi D_\tau\chi+J_0.
}
\]

Hence

\[
D_\tau\chi
=
\frac{J-J_0}{I_\phi}.
\]

The compact phase degree of freedom is therefore a genuine Lagrangian coordinate with a conjugate conserved quantity whenever \(L\) is independent of \(\chi\).

## 5. Foundation output

The phase core exports

\[
\boxed{
\chi\in U(1)
\cong S^1
}
\]

independently of the later Bloch realization.

Combined with the binary relational population coordinate

\[
u\in[0,1]
\]

and the two pole endpoints \(N,S\), the downstream Lagrangian--Bloch theorem constructs

\[
\boxed{
([0,1]\times S^1)/\partial
\cong
S^2
\cong
\mathbb{CP}^1.
}
\]

Therefore the canonical dependency is

\[
\boxed{
\text{RELATIONAL PHASE LAGRANGIAN}
\to
U(1)\cong S^1
\to
\text{LAGRANGIAN--BLOCH SELECTION}.
}
\]

## 6. Provenance

Promoted source:

\`archive/v7.9/full/01_foundational_formal_notes/hilbert_kahler_phase_hamiltonian/main.tex\`.

Only the phase-coordinate, covariant-velocity and Lagrangian identities are promoted here. The archived document's \(\mathbb{CP}^1\)/Bloch assumptions are not used as upstream premises of this phase-core module.

## 7. Claim classes

| Statement | Status |
|---|---|
| \(\mathbb R/2\pi\mathbb Z\cong U(1)\cong S^1\) | STANDARD EXACT |
| phase closure \(\chi\sim\chi+2\pi k\) | STANDARD EXACT |
| \(D_\tau\chi\) is gauge invariant under the declared transformation | EXACT |
| conjugate phase momentum formula | EXACT |
| cyclic \(\chi\) gives conserved \(J\) | STANDARD EULER--LAGRANGE/NOETHER RESULT |
| physical interpretation of \(\tau\) | SEPARATE / OPEN BINDING |
| physical identity of \(\mathcal A\) | SEPARATE / OPEN BINDING |

Validator:

\`TIR/validation/tir_relational_phase_lagrangian_core_v0_1.py\`.
