# TIR Lagrangian--Bloch Selection Theorem v0.1

Status: `EXACT_MINIMAL_COHERENT_PROJECTIVE_GEOMETRY__TIR_SOURCE_RECONCILIATION`

Scope: close the foundation seam between the primitive point/relational distinction, the half-seam phase circle, the projective two-state carrier, the Bloch sphere, and the Fubini--Study Lagrangian geometry. This theorem introduces no physical empirical binding.

## 1. Primitive point and first nontrivial coherent relation

The minimum non-empty object carrier is a point (P). A nontrivial relation distinguishes two orientation roles

[
{N,S}.
]

Normalized relational shares are

[
(1-u,u),qquad 0le ule1.
]

The smallest coherent extension retaining the already-admitted relative phase (arphiin U(1)cong S^1) is

[
oxed{
|psi(u,arphi)angle
=
sqrt{1-u},|Nangle
+
e^{iarphi}sqrt{u},|Sangle.
}
]

The endpoints are phase-independent:

[
u=0Rightarrow [psi]=[N],
qquad
u=1Rightarrow [psi]=[S].
]

Hence the relative-phase circle collapses at the two endpoints.

## 2. Quotient geometry

The parameter space before endpoint identification is

[
S^1	imes[0,1].
]

Collapsing the lower boundary circle to (N) and the upper boundary circle to (S) gives

[
oxed{
left(S^1	imes[0,1]ight)/
left(S^1	imes{0}sim N,;
S^1	imes{1}sim S
ight)
cong
Sigma S^1
cong
S^2.
}
]

Thus the sphere follows from the phase fibre plus the two pole endpoints; no pre-existing (SO(3)) action is required.

Equivalently, the same coherent state is a normalized vector in (mathbb C^2). Removing global phase gives

[
oxed{
S^3/U(1)
=
mathbb{CP}^1
cong
S^2.
}
]

The suspension and projective quotients are two descriptions of the same minimal two-state coherent geometry.

## 3. Explicit Bloch map

Define

[
mathbf r(u,arphi)
=
left(
2sqrt{u(1-u)}cosarphi,;
2sqrt{u(1-u)}sinarphi,;
1-2u
ight).
]

Then

[
|mathbf r|^2
=
4u(1-u)+(1-2u)^2
=
1.
]

Therefore

[
oxed{mathbf r:[psi]mapsto S^2}
]

is the standard Bloch realization. At (u=1/2),

[
oxed{
mathbf r(1/2,arphi)
=
(cosarphi,sinarphi,0),
}
]

so the TIR half-seam fibre is exactly the Bloch equator.

## 4. Euler closure of the topology

Suspension obeys

[
chi(Sigma X)=2-chi(X).
]

Because

[
chi(S^1)=0,
]

we obtain

[
oxed{
chi(S^2)=chi(Sigma S^1)=2.
}
]

This is the topological Euler closure of the phase circle into the sphere.

It must not be confused with Euler's complex identity (e^{ipi}=-1), which enters the Berry/spin closure after the projective geometry has been established.

## 5. Fubini--Study metric is the canonical projective metric

On normalized rays,

[
ds_{m FS}^2
=
langle dpsi|dpsiangle
-
|langlepsi|dpsiangle|^2.
]

Using

[
u=sin^2rac{	heta}{2},
]

the metric becomes

[
oxed{
ds_{m FS}^2
=
rac14
left(
d	heta^2+sin^2	heta,darphi^2
ight).
}
]

For (mathbb{CP}^1), the (PU(2))-invariant Kähler metric is unique up to one positive overall scale. TIR fixes the standard Fubini--Study normalization above.

Thus the minimal coherent projective carrier does not admit an arbitrary angular metric once projective-unitary invariance and the standard normalization are imposed.

## 6. Lagrangian geometry

The existing TIR relational phase Lagrangian has the geometric kinetic term

[
L_{m geom}
=
rac12 g_{ab}(q)dot q^adot q^b.
]

On the minimal coherent projective carrier, the canonical choice is

[
oxed{
g_{ab}=g^{m FS}_{ab}
}
]

up to the overall scale already fixed by the Fubini--Study normalization.

Hence the minimal projective Lagrangian geometry is

[
oxed{
(mathbb{CP}^1,g_{m FS})
cong
(S^2,g_{m round}/4).
}
]

This is the precise TIR content of “the point/minimal carrier maps to Bloch geometry through the Lagrangian”: a primitive point carrying the first nontrivial coherent relation has the minimal normalized projective configuration space (mathbb{CP}^1), and its invariant Kähler kinetic metric is Fubini--Study.

## 7. Berry curvature and next theorem

The Kähler/Berry curvature is

[
oxed{
F_B
=
rac12sin	heta,d	hetawedge darphi,
}
]

with

[
oxed{
rac1{2pi}int_{S^2}F_B=1.
}
]

The next canonical theorem is the already-existing Euler--Berry spin gate:

[
(mathbb{CP}^1,g_{m FS},F_B)
+
e^{igamma_B}=-1
Longrightarrow
oxed{s_{min}=rac12}.
]

That spin theorem remains separately sourced and preserves its original status `FORMAL_SYMBOLIC_PASS`.

## 8. Dependency result

The foundation seam is therefore

[
oxed{
P
	o
R
	o
{N,S}
	o
left([0,1]	imes S^1ight)/partial
cong
Sigma S^1
cong
S^2
cong
mathbb{CP}^1
	o
g_{m FS}
	o
F_B
	o
s=rac12.
}
]

The scalar information branch

[
{N,S}	orac12	oln2
]

is a commuting branch of the same binary carrier.

## 9. Claim classes

| Statement | Class |
|---|---|
| (S^1) with two collapsed boundary circles gives (Sigma S^1cong S^2) | STANDARD EXACT TOPOLOGY |
| normalized two-complex-state rays give (mathbb{CP}^1cong S^2) | STANDARD EXACT PROJECTIVE GEOMETRY |
| Bloch map has unit norm | EXACT |
| half-seam fibre is the equator | EXACT |
| (chi(Sigma S^1)=2) | STANDARD EXACT TOPOLOGY |
| Fubini--Study formula on (mathbb{CP}^1) | STANDARD EXACT |
| invariant Kähler metric is unique up to scale on this homogeneous carrier | STANDARD REPRESENTATION/GEOMETRY RESULT |
| standard FS normalization fixes the scale used by TIR | CONVENTION / NORMALIZATION |
| TIR relational Lagrangian uses this minimal projective metric | SOURCE-RECONCILED TIR IDENTIFICATION |
| Euler--Berry sign selects minimal spin (1/2) | DOWNSTREAM FORMAL_SYMBOLIC_PASS |
| empirical universality of the carrier | NOT CLAIMED HERE |

Validator:

`TIR/validation/tir_lagrangian_bloch_selection_v0_1.py`.
