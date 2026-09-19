# TIR–IDT Mod-6pi C3 / Pauli Representation Crosswalk v0.1

Status: `REPRESENTATION_CROSSWALK_CLOSED / PHYSICAL_SECTOR_BINDING_OPEN`

Date: 2026-09-19

## Scope

This integration note reconciles three already-existing mathematical surfaces:

1. IDT half-frame temporal gluing and its (6pi) three-frame sector;
2. the TIR local generator carrier (operatorname{Herm}_0(2)congmathbb R^3) with Pauli basis;
3. the TIR (C_3) character basis (F_3) used in the family-space branch.

The new result is a representation crosswalk. It does not identify temporal, spatial, and flavour sectors as the same physical degree of freedom.

## 1. IDT periodic three-frame quotient

IDT 02J/02JB gives the open-cut (N=3) support path

[
|1|12|23|3|
]

with path complex (P_4).

Under the explicit periodic phase condition

[
ThetasimTheta+6pi,
]

the endpoints are identified,

[
v_0sim v_3,
]

and therefore

[
oxed{P_4/(v_0sim v_3)cong C_3.}
]

The ordered frame carrier has the cyclic shift

[
P_3=
egin{pmatrix}
0&0&1\
1&0&0\
0&1&0
end{pmatrix},
qquad
P_3^3=I.
]

## 2. Exact character crosswalk

The TIR Stage-38 character matrix is

[
F_3=rac1{sqrt3}
egin{pmatrix}
1&1&1\
1&omega&omega^2\
1&omega^2&omega
end{pmatrix},
qquad
omega=e^{2pi i/3}.
]

For the IDT cyclic shift,

[
oxed{
F_3^dagger P_3F_3
=
operatorname{diag}(1,omega^2,omega).
}
]

Thus the IDT periodic triad and the TIR Stage-38 family calculation use the same abstract (C_3) character decomposition.

This closes the representation-theoretic bridge only. It does not prove that the temporal carrier is the physical flavour carrier.

## 3. Exact Pauli crosswalk

TIR already establishes

[
operatorname{Herm}_0(2)
=
operatorname{span}_{mathbb R}{sigma_x,sigma_y,sigma_z}
congmathbb R^3
]

with Hilbert-Schmidt metric

[
langle A,Bangle=rac12operatorname{Tr}(AB).
]

Let the IDT ordered frame basis be (e_1,e_2,e_3). Define

[
iota(e_1)=sigma_x,qquad
iota(e_2)=sigma_y,qquad
iota(e_3)=sigma_z.
]

Because the Pauli basis is Hilbert-Schmidt orthonormal, (iota) is an isometric real vector-space isomorphism.

Now define

[
U_3=
exp!left[
-rac{ipi}{3}
rac{sigma_x+sigma_y+sigma_z}{sqrt3}
ight]in SU(2).
]

Direct calculation gives

[
U_3sigma_xU_3^dagger=sigma_y,qquad
U_3sigma_yU_3^dagger=sigma_z,qquad
U_3sigma_zU_3^dagger=sigma_x.
]

Hence

[
oxed{
iotacirc P_3
=
operatorname{Ad}_{U_3}circiota.
}
]

The IDT (C_3) frame action and the TIR cyclic Pauli action are therefore exactly equivariantly isomorphic.

The lift also satisfies

[
U_3^3=-I,qquad U_3^6=I,
]

whereas the adjoint action has order three. This is the standard (SU(2)	o SO(3)) double-cover structure and must not be conflated with the separate numerical value of the IDT (6pi) phase budget.

## 4. Consequence for the completion frontier

The earlier seam

[
{1,2,3}_{6pi}
stackrel{?}{longrightarrow}
{sigma_x,sigma_y,sigma_z}
]

should no longer be classified as wholly open.

Its corrected status is

[
oxed{
	ext{PERIODIC TRIAD}
	o
C_3
	o
	ext{PAULI EQUIVARIANT REPRESENTATION}
quad	ext{CLOSED}.
}
]

The remaining stronger claim

[
	ext{IDT temporal triad}
equiv
	ext{physical TIR spatial tangent carrier}
]

remains open and requires an explicit physical sector-binding theorem.

Likewise,

[
C_3	o F_3
]

is exact, but

[
	ext{IDT temporal }C_3
equiv
	ext{physical flavour }C_3
]

remains open.

## 5. Relation to existing TIR CP work

The crosswalk explains why the same (C_3/F_3) algebra can appear both in the temporal modular carrier and in the TIR family-space CP calculations.

It does **not** by itself promote the Stage-38 mathematical CP result to a temporal origin theorem for CKM CP violation. Such a promotion still requires a source-owned sector map that binds the temporal carrier to the quark-family operators without importing fitted or observed mixing data.

## 6. Validation

Deterministic validator:

`TIR/validation/tir_idt_mod6pi_c3_pauli_crosswalk_v0_1.py`

Parents:

- IDT: `formalism/02JN_modular_cyclic_c3_pauli_bridge.md`;
- TIR: `TIR/validation/tir_relational_generator_space_v0_1.py`;
- TIR Stage-38: `TIR/frozen_predictions/validation/scripts/c3_character_basis_cp_stage38_v01.py`.

Promotion boundary:

`REPRESENTATION_CROSSWALK_CLOSED / TEMPORAL_SPATIAL_PHYSICAL_BINDING_OPEN / TEMPORAL_FLAVOUR_PHYSICAL_BINDING_OPEN`.


---

## Appendix A — NEW 2026-09-19 — Anchored temporal-C3 to family-C3 intertwiner

### A.1 Existing parents

No new three-family cycle is introduced here.

IDT 02JN supplies the periodic ordered temporal carrier

\[
E_T=\operatorname{span}\{e_1,e_2,e_3\}
\]

with regular cyclic action

\[
P_Te_1=e_2,\qquad
P_Te_2=e_3,\qquad
P_Te_3=e_1.
\]

TIR Stage 22 already freezes the ordered family labels

\[
s_1=(3,5),\qquad
s_2=(5,7),\qquad
s_3=(11,13),
\]

and Stage 24 already defines

\[
P_Fs_1=s_2,\qquad
P_Fs_2=s_3,\qquad
P_Fs_3=s_1.
\]

Thus both carriers realize the regular three-cycle representation of \(C_3\).

### A.2 Anchored equivariant map

Declare only the ordering anchor

\[
\boxed{M_{TF}e_1=s_1}
\]

and require equivariance

\[
\boxed{M_{TF}P_T=P_FM_{TF}.}
\]

Because the temporal orbit is transitive,

\[
e_2=P_Te_1,\qquad
e_3=P_T^2e_1.
\]

Therefore equivariance forces

\[
M_{TF}e_2
=
M_{TF}P_Te_1
=
P_FM_{TF}e_1
=
P_Fs_1
=
s_2,
\]

and similarly

\[
M_{TF}e_3=s_3.
\]

Hence the single anchor plus \(C_3\)-equivariance uniquely fixes the indexed basis map

\[
\boxed{
M_{TF}:
(e_1,e_2,e_3)
\longmapsto
(s_1,s_2,s_3).
}
\]

In the declared ordered orthonormal bases,

\[
\boxed{M_{TF}=I_3.}
\]

This is not a claim that an abstract \(C_3\) intertwiner is unique without an anchor. The three cyclic relabellings all intertwine the regular representation. The declared \(e_1\mapsto s_1\) anchor removes that residual cyclic ambiguity.

Status:

\`ANCHORED_EQUIVARIANT_LABEL_INTERTWINER_CLOSED\`.

### A.3 Conditional cardinality theorem

The orbit of \(e_1\) under \(P_T\) has exactly three elements:

\[
\mathcal O_T(e_1)=\{e_1,e_2,e_3\}.
\]

Any bijective equivariant physical binding of this transitive temporal orbit to a transitive family orbit preserves orbit cardinality. Therefore

\[
\boxed{
\text{physical temporal-family binding}
\Longrightarrow
N_F=3.
}
\]

The implication is exact. The premise is not yet promoted:

\`N_F_EQUALS_3_CONDITIONAL_ON_PHYSICAL_TEMPORAL_FAMILY_BINDING\`.

Thus the current result is stronger than a numerical coincidence but weaker than a physical derivation of the observed three generations.

### A.4 Character basis and CP-capable invariant

Because

\[
M_{TF}P_T=P_FM_{TF}
\]

and the anchored ordered bases give \(M_{TF}=I_3\), the same canonical character matrix

\[
F_3=\frac1{\sqrt3}
\begin{pmatrix}
1&1&1\\
1&\omega&\omega^2\\
1&\omega^2&\omega
\end{pmatrix},
\qquad
\omega=e^{2\pi i/3},
\]

diagonalizes both cycles:

\[
F_3^\dagger P_TF_3
=
F_3^\dagger P_FF_3
=
\operatorname{diag}(1,\omega^2,\omega).
\]

Stage 38 already establishes for this exact transform

\[
\boxed{
J(F_3)=\frac1{6\sqrt3}\neq0.
}
\]

Therefore the parameter-free CP-capable character invariant transfers exactly across the representation map.

Status:

\`F3_JARLSKOG_MATH_TRANSFER_CLOSED / PHYSICAL_CP_BINDING_OPEN\`.

This does not identify \(F_3\) with the physical CKM or PMNS matrix.

### A.5 Stage-42 SU(3)_F closure under pullback

Stage 42 defines a nondegenerate ordered family axis

\[
D_F=
\operatorname{diag}
\left(
-\frac13,\,
0,\,
\frac1{\sqrt5}
\right)
\]

and its character-oriented partner

\[
C_F=F_3D_FF_3^\dagger.
\]

It has already been validated that

\[
\operatorname{Lie}
\left\langle
i(D_F)_0,\,
i(C_F)_0
\right\rangle
=
\mathfrak{su}(3)_F,
\]

with real dimension \(8\).

Pull these operators back through the unitary intertwiner:

\[
D_T=M_{TF}^\dagger D_FM_{TF},
\qquad
C_T=M_{TF}^\dagger C_FM_{TF}.
\]

Unitary conjugation preserves commutators, linear independence, tracelessness and skew-Hermiticity. Consequently

\[
\boxed{
\dim_{\mathbb R}
\operatorname{Lie}
\langle i(D_T)_0,i(C_T)_0\rangle
=
8.
}
\]

Thus the full Stage-42 \(\mathfrak{su}(3)\) closure is preserved under the ordered representation crosswalk.

Status:

\`SU3F_LIE_DIMENSION_8_PRESERVED_UNDER_ORDERED_INTERTWINER\`.

Again, this is an algebraic transport theorem, not yet a physical identification of temporal and flavour degrees of freedom.

### A.6 Updated frontier

The earlier coarse statement

\`TEMPORAL_FLAVOUR_PHYSICAL_BINDING_OPEN\`

is now split into two typed levels:

\`\`\`text
temporal C3 <-> ordered family C3 label representation
    = CLOSED_EXACT_WITH_DECLARED_ANCHOR

temporal C3 <-> physical flavour degree of freedom
    = OPEN
\`\`\`

Consequently the remaining physical seam is narrower:

\[
\boxed{
\text{ordered representation binding}
\quad\longrightarrow\quad
\text{physical sector-binding theorem}.
}
\]

If that final sector-binding theorem passes, the three-family cardinality is no longer an independent model input; it follows from the transitive \(C_3\) orbit.


---

## Appendix B — NEW 2026-09-19 — Exact \(C_3\times Z_2\) six-state lift

### B.1 Independent binary carrier

Stage 23 already supplies the structural two-state CP1/chirality carrier

\[
\{|N\rangle,|S\rangle\}
\]

with involution

\[
J_\chi=
\begin{pmatrix}
0&1\\
1&0
\end{pmatrix},
\qquad
J_\chi^2=I_2.
\]

This \(Z_2\) channel is independent of the ordered three-family label index.

### B.2 Product carrier

Combine the periodic temporal \(C_3\) carrier with the existing chirality \(Z_2\):

\[
\mathcal H_{6,T}
=
E_T\otimes\mathbb C^2.
\]

Define

\[
G_T=P_T\otimes J_\chi.
\]

Because the two factors act on independent tensor components,

\[
(P_T\otimes I_2)(I_3\otimes J_\chi)
=
(I_3\otimes J_\chi)(P_T\otimes I_2).
\]

Since

\[
P_T^3=I_3,
\qquad
J_\chi^2=I_2,
\qquad
\gcd(3,2)=1,
\]

the product generator has order six:

\[
\boxed{G_T^6=I_6}
\]

while

\[
\boxed{G_T^3=I_3\otimes J_\chi\neq I_6.}
\]

Therefore the generated finite action is a \(C_6\) realization of

\[
\boxed{C_3\times Z_2\cong C_6.}
\]

The orbit of one basis state contains all six product labels exactly once before returning.

### B.3 Existing Stage-24 family realization

Stage 24 already defines

\[
G_F=P_F\otimes J_\chi
\]

on the ordered family×chirality basis and records the six-cycle

\[
(s_1,N)
\to
(s_2,S)
\to
(s_3,N)
\to
(s_1,S)
\to
(s_2,N)
\to
(s_3,S)
\to
(s_1,N).
\]

The temporal-to-family intertwiner from Appendix A lifts canonically to

\[
M_6=M_{TF}\otimes I_2.
\]

Then

\[
\boxed{
M_6G_T=G_FM_6.
}
\]

Thus

\[
\boxed{
(C_3^{\rm temporal}\times Z_2^\chi)
\cong
(C_3^{\rm family}\times Z_2^\chi)
}
\]

as anchored six-state label representations.

Status:

\`C3_X_CHIRALITY_Z2_SIX_STATE_INTERTWINER_CLOSED\`.

### B.4 What six means here

The exact result is

\[
\boxed{3\times2=6}
\]

for **family×chirality labels**.

It is not yet a derivation of the six quark flavours

\[
u,d,c,s,t,b.
\]

That stronger statement requires an additional theorem identifying the binary factor with the physical weak-isospin doublet:

\[
\boxed{
Z_2^{\chi}
\stackrel{?}{\longrightarrow}
Z_2^{\rm weak}.
}
\]

The current repository supports a CP1/Bloch weak-axis structure, but the exact identity of the Stage-23 chirality involution with the physical \(u/d\)-type weak-doublet index is not established by this crosswalk.

Therefore:

\`SIX_STATE_FAMILY_X_CHIRALITY = CLOSED\`

but

\`SIX_QUARK_FLAVOURS_FROM_3_X_2 = OPEN_PENDING_CHIRALITY_TO_WEAK_DOUBLET_BINDING\`.

This is the next minimal physical gate.


---

## Appendix C — NEW 2026-09-19 — Weak-family cardinality versus six-cycle operator identity

### C.1 Current weak-doublet parent

Stage 15 contains an exact

\[
\mathfrak{su}(3)\oplus\mathfrak{su}(2)\oplus\mathfrak u(1)
\]

subalgebra witness, while Stage 16 reproduces the one-generation weak-doublet hypercharge multiplicities. In particular the weak carrier has dimension

\[
\boxed{\dim V_W=2.}
\]

The ordered family carrier has

\[
\boxed{\dim V_F=3}
\]

under the Appendix-A temporal-family binding theorem.

Therefore

\[
\boxed{
\dim(V_F\otimes V_W)
=
3\times2
=
6.
}
\]

This is an exact dimension statement once the physical temporal-to-family binding premise is admitted.

Status:

\`DIMENSION_3_X_2_EQUALS_6_CONDITIONAL_ON_PHYSICAL_TEMPORAL_FAMILY_BINDING\`.

### C.2 What is already forced and what is not

The current chain therefore distinguishes two separate results.

First, cardinality:

\[
\boxed{
N_F=3,\quad
\dim V_W=2
\quad\Longrightarrow\quad
\dim(V_F\otimes V_W)=6.
}
\]

Thus a three-family weak-doublet carrier has six family×weak component labels.

Second, operator identity:

Appendix B produces an exact six-cycle on

\[
V_F\otimes V_\chi
\]

using the Stage-23 chirality involution. The physical weak carrier is

\[
V_F\otimes V_W.
\]

The equality of these two binary factors is not yet established:

\[
\boxed{
V_\chi
\stackrel{?}{\cong}
V_W.
}
\]

Therefore the six-label cardinality does not by itself prove that the exact Appendix-B six-cycle is the physical quark-flavour operator.

### C.3 Physical interpretation firewall

At the current frontier:

\`\`\`text
three-family cardinality from temporal C3
    = CONDITIONAL ON PHYSICAL TEMPORAL-FAMILY BINDING

weak-doublet dimension 2
    = CURRENT STRUCTURAL PARENT

3 x 2 = 6 weak-family component labels
    = CONDITIONAL EXACT CARDINALITY

C3 x Z2_chirality exact six-cycle
    = CLOSED

Z2_chirality <-> Z2_weak operator identity
    = OPEN

six physical quark flavours as the exact Stage-24 six-cycle
    = OPEN
\`\`\`

The minimal remaining operator gate is

\[
\boxed{
\texttt{CHIRALITY\_Z2\_TO\_WEAK\_ISOSPIN\_DOUBLET\_BINDING}.
}
\]

A legacy implementation exists in the archived chiral-projection line, where north/south CP1 poles were associated with \(T_3=\pm\tfrac12\) upper/lower weak-doublet components, but that archived mapping is not promoted here as a current theorem.


---

## Appendix D — NEW 2026-09-19 — Legacy weak-pole orientation audit and conditional current crosswalk

### D.1 Provenance recovery

The archived chiral-projection source

\`archive/v7.9/full/28_debt11_chiral_representation_projection_v3_0/scripts/debt11_chiral_representation_projection_v3_0.py\`

is pinned by Git blob SHA

\`01b9be380f095b613a731ba258865bc617d8e854\`.

It contains the explicit one-generation weak-doublet pole assignments

\[
|N\rangle
\leftrightarrow
T_3=+\frac12
\leftrightarrow
\text{upper weak-doublet component},
\]

\[
|S\rangle
\leftrightarrow
T_3=-\frac12
\leftrightarrow
\text{lower weak-doublet component}.
\]

In particular the source code contains

\[
u_L:
\quad
\text{north/+},\quad T_3=+\frac12,
\]

and

\[
d_L:
\quad
\text{south/-},\quad T_3=-\frac12.
\]

No observed masses are used by that archived source.

### D.2 Generated-artifact consistency audit

The archived generated CSV

\`archive/v7.9/full/28_debt11_chiral_representation_projection_v3_0/results/projection_channel_table_v3_0.csv\`

is pinned by blob SHA

\`3ec7331cbb859d8d955c9d7d5d1bd67ef75e8fb1\`.

The archived source generator contains the corrected row

\`\`\`text
u_L,up_quark,"T3=1/2, pole=north/+"
\`\`\`

whereas the preserved generated CSV contains the historical stale identifier

\`\`\`text
nu_L,up_quark,"T3=1/2, pole=north/+"
\`\`\`

for the same up-quark weak-doublet row.

Therefore the archived source generator is the provenance authority for the particle identifier. The generated CSV is retained as a historical artifact, and its stale identifier is diagnostic only; it does not gate the representation theorem.

Status:

\`ARCHIVAL_GENERATED_CSV_STALE_UP_QUARK_ID_DETECTED / SOURCE_SCRIPT_AUTHORITATIVE\`.

### D.3 Historical axis status

The archived v1.8 axis document states that the weak doublet uses one universal weak-isospin axis and that the zeta-polar map labels the north/south pair of that same Killing field. However it explicitly classifies the physical axis selection as a canonical working ansatz.

The later v2.3 source-grammar document strengthens the result. It first derives the abstract

\`SOURCE_DERIVED_CHIRAL_CP1_AXIS\`

from source-geometric criteria and only afterward identifies weak isospin as the Standard-Model realization of that abstract axis.

Its status remains

\`CONDITIONALLY_CLOSED_STRUCTURAL_ENUMERATION\`,

not an unconditional first-principles proof of the complete weak sector.

### D.4 Current representation crosswalk using the recovered orientation anchor

Current Stage 23 supplies

\[
J_\chi=
\begin{pmatrix}
0&1\\
1&0
\end{pmatrix}
\]

on the ordered pole basis

\[
(|N\rangle,|S\rangle).
\]

Let the ordered weak-doublet basis be

\[
(|+\rangle_W,|-\rangle_W),
\qquad
T_3|+\rangle_W=+\frac12|+\rangle_W,
\qquad
T_3|-\rangle_W=-\frac12|-\rangle_W.
\]

Using the recovered historical orientation anchor

\[
|N\rangle\mapsto|+\rangle_W,
\qquad
|S\rangle\mapsto|-\rangle_W,
\]

define

\[
F_{\chi W}=I_2.
\]

The weak-component exchange operator is

\[
J_W=
\begin{pmatrix}
0&1\\
1&0
\end{pmatrix}.
\]

Then

\[
\boxed{
F_{\chi W}J_\chi
=
J_WF_{\chi W}.
}
\]

Thus the binary label representations are exactly intertwined once the recovered north/south-to-\(T_3\) orientation anchor is admitted.

Status:

\`CHIRALITY_TO_WEAK_LABEL_INTERTWINER_CLOSED_CONDITIONAL_ON_RECOVERED_ORIENTATION_ANCHOR\`.

### D.5 Six-state weak-family lift

Combine the Appendix-A family map and the recovered binary map:

\[
M_{6W}
=
M_{TF}\otimes F_{\chi W}.
\]

On the temporal side use

\[
G_T=P_T\otimes J_\chi,
\]

and on the weak-family label side use

\[
G_W=P_F\otimes J_W.
\]

Then

\[
\boxed{
M_{6W}G_T
=
G_WM_{6W}.
}
\]

Therefore the exact six-cycle has a weak-family label realization conditional on the recovered orientation anchor.

The resulting label set is

\[
\boxed{
\{(1,+),(1,-),(2,+),(2,-),(3,+),(3,-)\},
}
\]

which has cardinality six.

For the quark-doublet interpretation this has the label pattern

\[
(u,d),\qquad(c,s),\qquad(t,b),
\]

but this Appendix does not derive the masses, charges, CKM matrix, or full physical particle spectrum from the six-cycle alone.

Status:

\`SIX_WEAK_FAMILY_LABEL_OPERATOR_CLOSED_CONDITIONAL_ON_RECOVERED_WEAK_ORIENTATION_ANCHOR\`.

### D.6 Remaining physical gate

The old gate

\`CHIRALITY_Z2_TO_WEAK_ISOSPIN_DOUBLET_BINDING = OPEN\`

is narrowed but not erased.

Its corrected decomposition is:

\`\`\`text
legacy N/S <-> T3 +/-1/2 orientation
    = SOURCE RECOVERED

current Z2 representation intertwiner under that orientation
    = CLOSED EXACT

current six-state weak-family label intertwiner
    = CLOSED EXACT CONDITIONAL ON RECOVERED ORIENTATION

first-principles physical selection of weak isospin from the source geometry
    = OPEN / historically conditional

full six-quark physical spectrum derivation
    = OPEN
\`\`\`

The remaining target is therefore no longer the existence of a \(2\)-state weak map. It is the promotion of the weak-axis orientation from recovered/conditional source status to a current first-principles physical selection theorem.


---

## Appendix E — NEW 2026-09-19 — Current \(A_1\) Weyl \(Z_2\) and the six-state family×weak carrier

### E.1 Binary weak carrier from the current \(A_1\) parent

Stage 15 provides the current exact weak-algebra factor

\[
A_1\cong\mathfrak{su}(2),
\]

and Stage 16 supplies the current one-generation weak-doublet representation.

In the standard weight basis of the fundamental doublet,

\[
T_3=
\begin{pmatrix}
\frac12&0\\
0&-\frac12
\end{pmatrix}.
\]

The nontrivial Weyl element of \(A_1\) is represented by

\[
J_W=
\begin{pmatrix}
0&1\\
1&0
\end{pmatrix}.
\]

It satisfies

\[
\boxed{J_W^2=I_2}
\]

and

\[
\boxed{
J_WT_3J_W^{-1}=-T_3.
}
\]

Thus the weak doublet contains an exact current \(Z_2\) weight-reflection action independently of the Stage-23 chirality/conjugation channel.

Status:

\`CURRENT_A1_WEYL_Z2_EXACT\`.

### E.2 Product with the ordered family three-cycle

Let \(P_F\) be the ordered family \(C_3\) action established in Appendix A. On

\[
V_F\otimes V_W
\]

define

\[
\boxed{
G_{FW}=P_F\otimes J_W.
}
\]

The two factors act on independent tensor components and commute. Since

\[
P_F^3=I_3,
\qquad
J_W^2=I_2,
\qquad
\gcd(3,2)=1,
\]

one obtains

\[
\boxed{
G_{FW}^6=I_6,
\qquad
G_{FW}^3=I_3\otimes J_W\neq I_6.
}
\]

The orbit of one family×weak basis state is transitive on all six labels, and

\[
\boxed{
\chi_{G_{FW}}(\lambda)=\lambda^6-1.
}
\]

Therefore

\[
\boxed{
C_3^{\rm family}\times W(A_1)^{\rm weak}
\cong
C_3\times Z_2
\cong
C_6
}
\]

as a six-state label action.

Status:

\`CURRENT_C3_X_A1_WEYL_Z2_C6_EXACT\`.

### E.3 Separation from the chirality six-cycle

Appendix B constructs

\[
V_F\otimes V_\chi
\]

with generator \(P_F\otimes J_\chi\).

Appendix E constructs instead

\[
V_F\otimes V_W
\]

with generator \(P_F\otimes J_W\).

Both are six-dimensional and both admit a \(C_6\) permutation realization, but they are differently typed carriers. Their equality is not assumed.

The legacy orientation audit in Appendix D provides a historical label crosswalk between the CP1 north/south basis and \(T_3=\pm\frac12\), but this crosswalk is not needed to derive the current family×weak six-state carrier itself.

### E.4 Consequence for flavour counting

Under the remaining physical family-binding premise

\[
C_3^{\rm temporal}
\longrightarrow
C_3^{\rm physical\ family},
\]

the current weak-doublet parent yields

\[
\boxed{
\dim(V_F\otimes V_W)=3\times2=6.
}
\]

For the quark sector, the conventional family×weak-component naming is

\[
(u,d),\qquad
(c,s),\qquad
(t,b).
\]

Hence the number six is no longer an independent count once the three-family binding is admitted:

\[
\boxed{
N_F=3
\quad\land\quad
\dim V_W=2
\quad\Longrightarrow\quad
N_{\rm quark\ family\text{-}weak\ labels}=6.
}
\]

Status:

\`SIX_WEAK_COMPONENT_LABELS_CONDITIONAL_ON_PHYSICAL_TEMPORAL_FAMILY_BINDING\`.

This does not derive quark masses, Yukawa couplings, CKM entries, confinement, or the complete physical spectrum.

### E.5 Narrowed remaining gate

The binary factor no longer requires the legacy chirality-to-weak identification in order to obtain the six-state weak-family carrier.

The principal unresolved seam is now

\[
\boxed{
C_3^{\rm temporal}
\stackrel{?}{\longrightarrow}
C_3^{\rm physical\ family}.
}
\]

After that, the remaining particle-physics work concerns dynamics and assignments rather than the bare \(3\times2\) cardinality:

\`\`\`text
temporal C3 -> ordered family C3 representation
    CLOSED

physical temporal C3 -> physical family index
    OPEN

weak A1 Weyl Z2
    CLOSED EXACT

family C3 x weak Weyl Z2 -> six-state C6 carrier
    CLOSED EXACT

six-state cardinality after physical family binding
    FORCED: 3 x 2 = 6

masses / Yukawa / CKM / full physical spectrum
    OPEN
\`\`\`


---

## Appendix F — NEW 2026-09-19 — \(A_1\) Cartan-axis conjugacy and gauge-orientation firewall

### F.1 Current weak parent

Stage 15 supplies the current exact \(A_1\cong\mathfrak{su}(2)\) weak factor and Stage 16 supplies the current two-state weak-doublet representation.

Choose the conventional Cartan representative

\[
T_3=\frac12\sigma_z.
\]

For any unit vector

\[
\hat n=(\sin\theta\cos\phi,\sin\theta\sin\phi,\cos\theta),
\]

define

\[
U(\hat n)
=
e^{-i\phi\sigma_z/2}
e^{-i\theta\sigma_y/2}
\in SU(2).
\]

Then

\[
\boxed{
U(\hat n)\,T_3\,U(\hat n)^\dagger
=
\frac12\,\hat n\cdot\boldsymbol{\sigma}.
}
\]

Thus all normalized \(A_1\) Cartan-axis representatives lie in one \(SU(2)\) conjugacy class.

Status:

\`A1_CARTAN_ORIENTATION_SU2_CONJUGACY_CLASS_CLOSED\`.

### F.2 Weyl \(Z_2\) is conjugacy-covariant

In the reference basis use

\[
J_W=\sigma_x,
\qquad
J_W^2=I_2,
\qquad
J_WT_3J_W^\dagger=-T_3.
\]

Transport the reflection together with the axis:

\[
J_{\hat n}
=
U(\hat n)J_WU(\hat n)^\dagger.
\]

Then

\[
J_{\hat n}^2=I_2
\]

and

\[
\boxed{
J_{\hat n}
\left(\frac12\hat n\cdot\boldsymbol{\sigma}\right)
J_{\hat n}^\dagger
=
-\frac12\hat n\cdot\boldsymbol{\sigma}.
}
\]

Therefore the binary weak carrier and its Weyl exchange do not depend on an absolute external orientation of the \(A_1\) axis.

The validator checks this explicitly on the non-axis-aligned deterministic direction

\[
\hat n=\frac{(1,2,3)}{\sqrt{14}}.
\]

### F.3 Consequence for the historical weak-axis debt

The old question

\[
\text{“which absolute Bloch/weak axis is the physical one?”}
\]

is too strong as a pre-breaking representation gate. Within the current \(SU(2)\) carrier, a change of normalized Cartan orientation is implemented by conjugation.

Accordingly, the legacy north/south anchor remains useful to fix an orientation convention,

\[
N/S\leftrightarrow \operatorname{sign}(T_3),
\]

but it is not required for the existence of the two-state weak representation or its Weyl \(Z_2\).

The current exact status is therefore:

\`\`\`text
A1 weak carrier
    = CLOSED

normalized Cartan-axis conjugacy class
    = CLOSED

Weyl Z2 on any conjugate axis
    = CLOSED

absolute pre-breaking axis orientation as an independent observable
    = NOT REQUIRED BY THE REPRESENTATION THEOREM
\`\`\`

### F.4 What remains physically open

Axis conjugacy does not by itself determine electroweak vacuum alignment.

The stronger physical problem is to bind the internal \(SU(2)\) carrier, the hypercharge carrier and the symmetry-breaking/vacuum structure so that the unbroken electromagnetic direction and physical component assignments follow from the source dynamics.

Current status:

\`OPEN_HIGGS_HYPERCHARGE_ALIGNMENT_NOT_CLOSED_BY_AXIS_CONJUGACY\`.

This is distinct from the already closed representation results

\[
C_3^{\rm family}\times W(A_1)^{\rm weak}
\cong C_6
\]

and

\[
\dim(V_F\otimes V_W)=3\times2=6.
\]

The principal family-side physical gate remains

\[
C_3^{\rm temporal}
\stackrel{?}{\longrightarrow}
C_3^{\rm physical\ family},
\]

while the electroweak-side gate is vacuum/hypercharge alignment rather than an absolute \(T_3\)-axis selection.


---

## Appendix G — NEW 2026-09-19 — Active Stage-22 precedence versus historical generation numbering

### G.1 Two different orderings are preserved in the repository

The historical atomic-assignment layer records

\[
\text{generation 1}\to(3,5),\qquad
\text{generation 2}\to(11,13),\qquad
\text{generation 3}\to(5,7).
\]

Stage 22 later fixes the active ordered seed basis for the family-carrier validation line as

\[
\boxed{
s_1=(3,5),\qquad
s_2=(5,7),\qquad
s_3=(11,13).
}
\]

The precedence-falsification layer explicitly states that the active Stage-22 ordering supersedes the early v0.5 generation ordering for the present validation branch.

Therefore these are not interchangeable metadata surfaces.

### G.2 Correct temporal-family representation binding

The Appendix-A intertwiner

\[
M_{TF}:
(e_1,e_2,e_3)\mapsto(s_1,s_2,s_3)
\]

is bound to the **active Stage-22 ordered family-seed basis**.

Status:

\`TEMPORAL_C3_TO_ACTIVE_STAGE22_FAMILY_SEED_ORDER_CLOSED\`.

It is not a direct identification

\[
e_i\equiv\text{historical physical generation }i.
\]

The historical generation labels remain preserved for provenance but are not used as the \(C_3\) anchor.

Status:

\`HISTORICAL_GENERATION_NUMBERING_PRESERVED_BUT_NOT_USED_AS_ACTIVE_C3_ANCHOR\`.

### G.3 Physical-family gate remains separate

Stage 22 itself establishes an ordered three-element structural seed basis for subsequent family representation tests. Its PASS does not by itself prove that the active ordering is the physical mass-generation ordering.

Therefore the remaining family-side physical seam is typed as

\[
\boxed{
C_3^{\rm temporal}
\longrightarrow
C_3^{\rm active\ family\ seed\ carrier}
\quad\text{CLOSED},
}
\]

followed by

\[
\boxed{
C_3^{\rm active\ family\ seed\ carrier}
\stackrel{?}{\longrightarrow}
C_3^{\rm physical\ generation/family}
\quad\text{OPEN}.
}
\]

This firewall prevents the old v0.5 ordering from being silently reintroduced into the new mod-\(6\pi\) crosswalk.

---

## Appendix H — NEW 2026-09-19 — Source-order anchor and raw-qC negative control

### H.1 Independent order check on the active Stage-22 carrier

The active family-seed order is

\[
s_1=(3,5),\qquad s_2=(5,7),\qquad s_3=(11,13).
\]

On the current integer-center projection this gives

\[
m_1=4,\qquad m_2=6,\qquad m_3=12.
\]

Ordinary Collatz stopping depth to \(1\) is

\[
\boxed{L(4)=2,\qquad L(6)=8,\qquad L(12)=9.}
\]

Thus the independent stopping-depth ranking is strictly consistent with the active Stage-22 order.

### H.2 Unique order-preserving representation map

The IDT parent retains the ordered open-cut frame provenance

\[
e_1<e_2<e_3
\]

before periodic endpoint identification. The active TIR family carrier is also an ordered three-element basis.

There is exactly one order-preserving bijection between these ordered triples:

\[
\boxed{M_{\rm ord}(e_j)=s_j,\qquad j=1,2,3.}
\]

Therefore the earlier explicit anchor \(e_1\mapsto s_1\) is no longer a free cyclic relabelling at the ordered-label representation level.

Status:

`UNIQUE_ORDER_PRESERVING_LABEL_CROSSWALK_CLOSED`

`DECLARED_ANCHOR_DEPENDENCY_REMOVED_AT_ORDERED_LABEL_REPRESENTATION_LEVEL`.

This does not identify temporal frame rank with physical generation rank. Appendix G's precedence firewall remains in force.

### H.3 Raw \(q_C\) is not the uniform three-frame clock

The current IDT Collatz phases on the active centers are

\[
q_C(4)=\frac17,\qquad
q_C(6)=\frac{141}{448},\qquad
q_C(12)=\frac{141}{896}.
\]

They are not monotone in active Stage-22 order and are not an arithmetic progression:

\[
q_C(6)-q_C(4)=\frac{11}{64}
\neq
-\frac{141}{896}=q_C(12)-q_C(6).
\]

Hence the raw \(q_C\) values cannot be directly identified with uniformly spaced positions of the periodic \(6\pi\) three-frame carrier.

Status:

`DIRECT_UNIFORM_C3_CLOCK_IDENTIFICATION_REFUTED`.

The exact IDT phase coboundary and its existing sign correlations remain valid; they simply do not close the physical temporal-to-family seam by themselves.

### H.4 Frontier after the negative control

```text
temporal C3 -> active Stage-22 ordered family C3      CLOSED representation/order
free cyclic anchor                                   REMOVED
raw qC -> uniform mod-6pi three-frame clock          REFUTED
active Stage-22 family seed carrier -> physical family/generation index
                                                     OPEN
```


---

## Appendix I — NEW 2026-09-19 — Independent \(E_8\) family multiplicity-three parent

### I.1 Exceptional family parent

Stage 21 supplies the current exact exceptional carrier

\[
E_8\supset(E_6\times SU(3)_F)/Z_3
\]

with matter content containing

\[
(16,3_F).
\]

Therefore the one-family spinor content is replicated by an independent triplet factor:

\[
16\times3=48.
\]

Stage 21 explicitly states that the exceptional representation fixes a multiplicity factor of three.

Status:

\`STAGE21_E8_THREEFOLD_MULTIPLICITY_3_CURRENT_PASS\`.

### I.2 Seed-to-exceptional triplet binding

Stage 22 fixes the active ordered seed basis

\[
s_1=(3,5),\qquad
s_2=(5,7),\qquad
s_3=(11,13),
\]

and Stage 24 maps it to the ordered exceptional triplet basis by

\[
M_s|s_j\rangle=|t_j\rangle,
\]

with

\[
\boxed{
M_sP_s=P_3M_s.
}
\]

Status:

\`STAGE24_ORDERED_SEED_TO_E8_TRIPLET_INTERTWINER_CURRENT_PASS\`.

### I.3 Independence from color

Stage 25 factors the quark-doublet carrier as

\[
V_Q
=
\mathbb C^3_C
\otimes
\mathbb C^2_L
\otimes
\mathbb C^3_F
\]

and verifies that color and family transformations commute on separate tensor factors.

Hence the family triplet is not the color triplet:

\[
SU(3)_C\neq SU(3)_F
\]

as typed carrier actions.

### I.4 Role of the new temporal \(C_3\)

The new periodic IDT carrier supplies an independent

\[
C_3^{\rm temporal}.
\]

The crosswalk now gives

\[
C_3^{\rm temporal}
\longleftrightarrow
C_3^{\rm active\ seed}
\longleftrightarrow
C_3^{E_8\rm\ triplet}
\]

at ordered representation level.

The correct status is therefore

\`INDEPENDENT_C3_CROSSWALK_TO_EXISTING_MULTIPLICITY3_FAMILY_CARRIER\`.

The temporal \(C_3\) is not claimed as the sole source of family multiplicity three. Instead, two independently constructed triplet structures meet in one equivariant representation diagram.

### I.5 Consequence for six weak-family labels

The current representation chain has independently typed dimensions

\[
\dim V_F=3,
\qquad
\dim V_W=2.
\]

Therefore

\[
\boxed{
\dim(V_F\otimes V_W)=6.
}
\]

This six-state carrier is a representation-level consequence of the already-current family and weak parents. Masses, Yukawa couplings, physical CKM/PMNS values and full spectrum dynamics remain separate open gates.
