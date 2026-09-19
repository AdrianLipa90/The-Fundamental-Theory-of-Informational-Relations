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
