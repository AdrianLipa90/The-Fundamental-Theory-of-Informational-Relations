# TIR Relational Phase Lagrangian Core v0.1

Status: `SOURCE_PROMOTED_EXACT_STRUCTURAL_PHASE_CORE__PHYSICAL_TIME_BINDING_SEPARATE`

Scope: promote the already-existing relational phase Lagrangian into the active TIR foundation without importing the archived Hilbert/CP1 assumptions as parents. The phase core supplies the compact relative-phase carrier (U(1)cong S^1); the Lagrangian--Bloch theorem uses it downstream.

## 1. Relative phase as a compact coordinate

A phase is represented by an angle

[
chiinmathbb R/2pimathbb Z.
]

Equivalently,

[
oxed{
e^{ichi}in U(1)
cong
S^1.
}
]

The identification

[
chisimchi+2pi k,
qquad
kinmathbb Z,
]

is the standard Euler phase closure and does not require a Bloch sphere, a Pauli algebra, or an (SO(3)) action.

## 2. Relational gauge transport

Let (q^a) denote relational configuration coordinates and let (mathcal A=mathcal A_a(q)dq^a) be a phase connection. Define

[
oxed{
D_	auchi
=
dotchi+mathcal A_a(q)dot q^a.
}
]

Under a local phase change

[
chimapstochi-lambda(q),
qquad
mathcal Amapstomathcal A+dlambda,
]

one has

[
oxed{
D_	auchimapsto D_	auchi.
}
]

Thus the covariant phase velocity is gauge invariant.

## 3. Minimal relational phase Lagrangian

The archived TIR/Metatime formal note contains the phase-first Lagrangian

[
oxed{
L
=
rac12 g_{ab}(q)dot q^adot q^b
+
rac{I_phi}{2}(D_	auchi)^2
+
J_0D_	auchi
-
V(q).
}
]

For the foundation layer only the structural roles are retained:

- (g_{ab}): configuration-space metric to be selected by downstream geometry;
- (chiin U(1)): compact relative phase;
- (mathcal A): relational phase connection;
- (I_phi>0): positive phase inertia/normalization;
- (V): scalar potential.

No physical elapsed-time, mass, neutrino, electromagnetic, or gravitational identification is made here.

## 4. Phase momentum

The momentum conjugate to the phase is

[
oxed{
J
=
rac{partial L}{partialdotchi}
=
I_phi D_	auchi+J_0.
}
]

Hence

[
D_	auchi
=
rac{J-J_0}{I_phi}.
]

The compact phase degree of freedom is therefore a genuine Lagrangian coordinate with a conjugate conserved quantity whenever (L) is independent of (chi).

## 5. Foundation output

The phase core exports

[
oxed{
chiin U(1)
cong S^1
}
]

independently of the later Bloch realization.

Combined with the binary relational population coordinate

[
uin[0,1]
]

and the two pole endpoints (N,S), the downstream Lagrangian--Bloch theorem constructs

[
oxed{
([0,1]	imes S^1)/partial
cong
S^2
cong
mathbb{CP}^1.
}
]

Therefore the canonical dependency is

[
oxed{
	ext{RELATIONAL PHASE LAGRANGIAN}
	o
U(1)cong S^1
	o
	ext{LAGRANGIAN--BLOCH SELECTION}.
}
]

## 6. Provenance

Promoted source:

`archive/v7.9/full/01_foundational_formal_notes/hilbert_kahler_phase_hamiltonian/main.tex`.

Only the phase-coordinate, covariant-velocity and Lagrangian identities are promoted here. The archived document's CP1/Bloch assumptions are not used as upstream premises of this phase-core module.

## 7. Claim classes

| Statement | Status |
|---|---|
| (mathbb R/2pimathbb Zcong U(1)cong S^1) | STANDARD EXACT |
| phase closure (chisimchi+2pi k) | STANDARD EXACT |
| (D_	auchi) is gauge invariant under the declared transformation | EXACT |
| conjugate phase momentum formula | EXACT |
| cyclic (chi) gives conserved (J) | STANDARD EULER--LAGRANGE/NOETHER RESULT |
| physical interpretation of (	au) | SEPARATE / OPEN BINDING |
| physical identity of (mathcal A) | SEPARATE / OPEN BINDING |

Validator:

`TIR/validation/tir_relational_phase_lagrangian_core_v0_1.py`.
