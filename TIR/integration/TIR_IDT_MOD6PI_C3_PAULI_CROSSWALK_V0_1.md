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

`archive/v7.9/full/28_debt11_chiral_representation_projection_v3_0/results/projection_channel_table_v3_0.csv`

is pinned by blob SHA

`3ec7331cbb859d8d955c9d7d5d1bd67ef75e8fb1`.

The archived source generator contains the corrected up-quark identifiers, including

```text
u_L,up_quark,"T3=1/2, pole=north/+"
```

and the right-handed up-quark identifier `u_R`.

An earlier connector-facing retrieval rendered the generated CSV with historical `nu_L/nu_R` identifiers. That observation is superseded for repository provenance by an exact GitHub Actions audit of the immutable PR-head Git object.

The validator now obtains the CSV object through

```text
git ls-tree HEAD
git cat-file blob <sha>
```

and independently verifies that the checked-out bytes equal the HEAD object. On that authoritative hosted Git object it obtains

```text
HEAD tree blob            = 3ec7331cbb859d8d955c9d7d5d1bd67ef75e8fb1
working tree == HEAD blob = true
up_quark particle_ids     = ["u_L", "u_R"]
CSV state                 = CORRECTED_UP_QUARK_PARTICLE_ID
```

Therefore the source generator and the hosted immutable generated-CSV object agree on the up-quark particle identifiers. The contradictory connector-facing rendering is quarantined as a retrieval-layer discrepancy and is not used as provenance authority.

Status:

`ARCHIVAL_SOURCE_AND_HEAD_OBJECT_CSV_CONSISTENT / CONNECTOR_VIEW_DISCREPANCY_QUARANTINED`.

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


---

## Appendix J — NEW 2026-09-19 — Raw seed-dynamics no-go and temporal orientation selection

### J.1 Ordinary center Collatz remains a no-go for the Stage-24 cycle

The active center projection

\[
(4,6,12)
\]

has the exact directed reachability chain

\[
12\to6\to4,
\]

while \(4\nrightarrow6\) and \(6\nrightarrow12\) under the ordinary forward Collatz map.

Therefore

\[
\boxed{
P_s\neq C
}
\]

on the active center projection.

Status:

\`ORDINARY_CENTER_COLLATZ_STAGE24_C3_CYCLE_REFUTED\`.

### J.2 Product-seed Collatz also does not generate a three-cycle

Stage 44 uses the pre-existing scalar-seed rule

\[
n_0=p(p+2)
\]

for the active family labels, giving

\[
n_1=15,\qquad n_2=35,\qquad n_3=143.
\]

Direct first-hit reachability among these three scalar seeds is

\[
15\to35\quad\text{in }4\text{ steps},
\]

\[
143\to35\quad\text{in }90\text{ steps},
\]

with no other directed hit between distinct members of the set.

Writing absent directed hits as \(-1\), the exact first-hit matrix is

\[
\boxed{
R_C=
\begin{pmatrix}
0&4&-1\\
-1&0&-1\\
-1&90&0
\end{pmatrix}.
}
\]

This directed graph contains no three-cycle.

Status:

\`ORDINARY_PRODUCT_SEED_COLLATZ_C3_CYCLE_REFUTED\`.

The Stage-44 symmetric meeting geometry

\[
D_C=
\begin{pmatrix}
0&4&88\\
4&0&90\\
88&90&0
\end{pmatrix}
\]

remains an exact structural object, but it is not itself a directed cycle.

### J.3 No canonical path-cost-to-amplitude law is available

Stage 45 explicitly finds

\[
\boxed{
\text{canonical distance/path-cost}\to\text{amplitude rule: NOT FOUND}.
}
\]

Therefore \(D_C\), \(1/D_C\), \(e^{-D_C}\), or \(e^{-\kappa D_C}\) cannot be inserted as though they were already-derived TIR dynamics.

Status:

\`CANONICAL_PATH_COST_TO_AMPLITUDE_RULE_NOT_FOUND\`.

This blocks retrospective conversion of Stage-44 proximity into a physical transition operator.

### J.4 Icosahedral geometry supplies a rigid \(C_3\)-compatible carrier

Stage 61 establishes that the frozen family generator

\[
P_3=
\begin{pmatrix}
0&0&1\\
1&0&0\\
0&1&0
\end{pmatrix}
\]

is an orientation-preserving order-three icosahedral symmetry and embeds the frozen family operators into the five-dimensional quadrupole carrier.

Stage 62 then removes the continuous orientation freedom. With the frozen ordered axis and seed-incidence operator imposed, the labelled embedding is rigid.

Status:

\`STAGE61_62_C3_COMPATIBLE_RIGID_EMBEDDING_CURRENT_PASS\`.

These stages establish compatibility and rigidity. They do not derive \(P_3\) from raw Collatz seed evolution.

### J.5 Temporal orientation selects \(P_3\) against its inverse

The periodic IDT carrier is oriented:

\[
e_1\to e_2\to e_3\to e_1.
\]

There are two nontrivial orientation-preserving order-three permutation generators on the same ordered triplet:

\[
P_3
\qquad\text{and}\qquad
P_3^{-1}=P_3^2.
\]

They differ already on the first basis vector:

\[
P_3e_1=e_2,
\qquad
P_3^{-1}e_1=e_3.
\]

Under the exact ordered temporal-family intertwiner \(M_{TF}\),

\[
M_{TF}P_T=P_3M_{TF}.
\]

Hence the forward temporal orientation selects \(P_3\), while reversing the temporal orientation selects \(P_3^{-1}\).

Status:

\`TEMPORAL_ORIENTATION_SELECTS_P3_VS_INVERSE_AT_REPRESENTATION_LEVEL\`.

This is an orientation theorem for the representation. It is not a claim that ordinary Collatz trajectories dynamically cycle the three physical families.

### J.6 Correct remaining dynamical gate

The old broad gate

\[
\text{“derive }P_s\text{ from Collatz/Poincare”}
\]

now decomposes as

\`\`\`text
raw center Collatz C3 cycle
    = REFUTED

raw product-seed Collatz C3 cycle
    = REFUTED

Stage-44 distance -> amplitude law
    = NOT FOUND

C3-compatible rigid family geometry
    = CLOSED

orientation P3 vs P3^-1 from temporal direction
    = CLOSED AT REPRESENTATION LEVEL

physical seed/family transition dynamics
    = OPEN
\`\`\`

The remaining positive route therefore requires a richer Poincare/holonomy/action operator, specified independently before any CKM or mass comparison.

Status:

\`OPEN_RICHER_POINCARE_HOLONOMY_OPERATOR_REQUIRED\`.


---

## Appendix K — NEW 2026-09-19 — Canonical Collatz/Poincare \(2\to3\) carrier and compact-real-form boundary

Stage 48 freezes exact Collatz branch words in the free monoid
\[
\mathcal W=\{E,O\}^*,
\]
while keeping
\[
E\mapsto U_E,\qquad O\mapsto U_O
\]
and the exact per-step rhythm/weight explicitly OPEN.

Stage 49 gives the canonical Möbius/Poincare lift
\[
\boxed{
\{E,O\}^*
\longrightarrow
PSL(2,\mathbb R)
\longrightarrow
\operatorname{Isom}^+(\mathbb D_{\rm Poincare})
}.
\]

For the normalized branch generators,
\[
\widehat M_E=
\begin{pmatrix}
1/\sqrt2&0\\
0&\sqrt2
\end{pmatrix},
\qquad
\widehat M_O=
\frac1{\sqrt3}
\begin{pmatrix}
3&1\\
0&1
\end{pmatrix}.
\]

Stage 50 applies the standard symmetric-square representation
\[
\rho_2:
SL(2,\mathbb R)\to SL(3,\mathbb R).
\]
Since
\[
\dim\operatorname{Sym}^2(\mathbb R^2)=3,
\]
the two-component projective carrier has the canonical three-component lift
\[
\boxed{
SL(2,\mathbb R)
\xrightarrow{\operatorname{Sym}^2}
SL(3,\mathbb R)
}.
\]

The exact branch matrices are
\[
R_E=
\begin{pmatrix}
1/2&0&0\\
0&1&0\\
0&0&2
\end{pmatrix},
\qquad
R_O=
\begin{pmatrix}
3&2&1/3\\
0&1&1/3\\
0&0&1/3
\end{pmatrix},
\]
and preserve
\[
Q(x,y,z)=xz-y^2.
\]

Status:

\`BRANCH_WORD_TO_PSL2R_TO_SYM2_THREE_CARRIER_CURRENT_EXACT\`

\`SYM2_TWO_TO_THREE_CARRIER_CLOSED\`.

This is a representation theorem; it is not by itself a physical \(x,y,z\) identification.

Stage 51 supplies the exact obstruction to direct fixed-similarity unitarization. In particular
\[
\operatorname{spec}(R_E)=\{1/2,1,2\}
\]
is incompatible with preservation of a positive-definite Hermitian form. Therefore
\[
\boxed{
\operatorname{Sym}^2(PSL(2,\mathbb R))
\not\sim SU(3)_F
}
\]
by direct similarity.

Stage 52 nevertheless gives the valid real-form bridge
\[
\boxed{
\mathfrak{sl}(2,\mathbb R)
\to
\mathfrak{sl}(2,\mathbb C)
\leftarrow
\mathfrak{su}(2)
\xrightarrow{\operatorname{Sym}^2}
\mathfrak{su}(3)
}.
\]

The bridge exists, but the repository still lacks a derived rule selecting the compact real form from the split-real Collatz/Poincare dynamics.

Status:

\`DIRECT_UNITARIZATION_REFUTED_COMPACT_REAL_FORM_BRIDGE_AVAILABLE_SELECTION_OPEN\`.

Stage 53 further proves that the compact spin-one subgroup alone has
\[
\boxed{J=0},
\]
while
\[
\mathfrak{su}(3)\cong\mathbf3\oplus\mathbf5
\]
under that embedded spin-one \(SU(2)\). Nonzero family CP therefore requires directions outside the compact spin-one subalgebra.

Status:

\`COMPACT_SPIN1_SUBGROUP_JARLSKOG_ZERO_FULL_SU3_COMPLEMENT_REQUIRED\`.

Stage 64 keeps the remaining selector debt explicit. The updated dynamical frontier is

\`\`\`text
Collatz branch words                              = EXACT
branch words -> PSL(2,R) / Poincare              = CLOSED
PSL(2,R) -> Sym^2 three-carrier                  = CLOSED
direct split-real -> SU(3)_F similarity          = REFUTED
compact real-form bridge into SU(3)              = AVAILABLE
dynamical compact-real-form selection            = OPEN
branch symbol -> physical family-space operator  = OPEN
exact per-step rhythm/weight                     = OPEN
compact spin-1 subgroup alone -> CP              = REFUTED (J=0)
full SU(3) complement / complex holonomy         = REQUIRED
\`\`\`

Therefore the remaining positive target is not “find a three-state carrier”; that carrier is already derived. The missing object is the canonical selection and weighting mechanism that maps the exact Collatz/Poincare branch dynamics into the full compact family operator.

Status:

\`OPEN_BRANCH_OPERATOR_RHYTHM_REALFORM_AND_COMPLEMENT_SELECTION\`.


---

## Appendix L — NEW 2026-09-19 — \(N=5\) icosahedral realization of the five-dimensional \(SU(3)/SO(3)\) complement

### L.1 Symmetric-pair decomposition

Stages 53--55 establish the exact compact symmetric-pair decomposition

\[
\mathfrak{su}(3)_F
=
\mathfrak k\oplus\mathfrak p,
\qquad
\mathfrak k\cong\mathfrak{so}(3),
\]

with

\[
\dim\mathfrak k=3,
\qquad
\dim\mathfrak p=5.
\]

The bracket relations are

\[
[\mathfrak k,\mathfrak k]\subset\mathfrak k,
\qquad
[\mathfrak k,\mathfrak p]\subset\mathfrak p,
\qquad
[\mathfrak p,\mathfrak p]\subset\mathfrak k.
\]

Therefore

\[
\boxed{
\mathfrak p
\simeq
T_{[e]}(SU(3)/SO(3))
}
\]

is the five-dimensional spin-two tangent carrier.

Status:

\`FIVE_DIMENSIONAL_SU3_OVER_SO3_SPIN2_COMPLEMENT_CURRENT_EXACT\`.

This five-dimensional object is a Lie/tangent representation sector. It is not a claim of five physical spatial dimensions.

### L.2 \(N=5\) is the unique irreducible Platonic restriction in the frozen \(N=3,4,5\) set

Stage 56 restricts the same spin-two carrier to the rotational symmetry groups

\[
N=3:\ A_4,
\qquad
N=4:\ S_4,
\qquad
N=5:\ A_5.
\]

For \(N=3\),

\[
\mathbf5\downarrow A_4
=
\mathbf1'\oplus\mathbf1''\oplus\mathbf3.
\]

For \(N=4\),

\[
\mathbf5\downarrow S_4
=
\mathbf2\oplus\mathbf3.
\]

For \(N=5\),

\[
\boxed{
\mathbf5\downarrow A_5
=
\mathbf5_{\rm irr}.
}
\]

Hence the complete five-dimensional complement remains irreducible specifically under the icosahedral rotational group.

Status:

\`N5_A5_IRREDUCIBLE_FIVE_CARRIER_CURRENT_EXACT\`.

### L.3 Tensor-square origin of the \(3+5\) decomposition

For the rotational triplet \(V\cong\mathbf3\),

\[
V\otimes V
=
\Lambda^2V
\oplus
\operatorname{Sym}^2V.
\]

Under \(SO(3)\),

\[
\Lambda^2V\cong\mathbf3,
\]

and

\[
\operatorname{Sym}^2V
\cong
\mathbf1\oplus\mathbf5.
\]

Therefore

\[
\boxed{
\mathbf3\otimes\mathbf3
=
\mathbf1\oplus\mathbf3\oplus\mathbf5
}
\]

and after removing the scalar identity,

\[
\boxed{
\operatorname{End}_0(\mathbf3)
=
\mathbf3\oplus\mathbf5.
}
\]

Stage 57 shows that the same decomposition holds exactly for the icosahedral rotational triplet.

### L.4 Explicit icosahedral quadrupole generation

Let \(u_a\), \(a=1,\ldots,6\), be the six unoriented axes obtained from the 12 vertices of the regular icosahedron.

Define

\[
Q_a
=
u_au_a^T-\frac13I_3.
\]

Each \(Q_a\) lies in

\[
\operatorname{Sym}^2_0(\mathbb R^3).
\]

Stage 58 obtains

\[
\boxed{
\operatorname{rank}\{Q_a\}=5,
}
\]

with

\[
\sum_{a=1}^{6}Q_a=0.
\]

Their pairwise commutators lie in \(\mathfrak{so}(3)\) and span a three-dimensional space:

\[
\boxed{
\dim\operatorname{span}\{[Q_a,Q_b]\}=3.
}
\]

Thus

\[
\mathfrak{su}(3)
=
\mathfrak{so}(3)
\oplus
i\operatorname{Sym}^2_0(\mathbb R^3)
\]

is generated by the icosahedral quadrupole set:

\[
\boxed{
\operatorname{Lie}\langle iQ_1,\ldots,iQ_6\rangle
=
\mathfrak{su}(3).
}
\]

Status:

\`SIX_ICOSAHEDRAL_QUADRUPOLES_GENERATE_FULL_SU3_CURRENT_EXACT\`.

### L.5 Updated interpretation of the missing CP-capable directions

Appendix K showed that compact spin-one \(SU(2)\subset SU(3)\) alone has

\[
J=0.
\]

The present appendix localizes the additional directions exactly:

\[
\boxed{
\text{CP-trivial compact subgroup directions}
=
\mathbf3,
}
\]

\[
\boxed{
\text{complement directions}
=
\mathbf5
=
T(SU(3)/SO(3)),
}
\]

with the \(N=5\) icosahedral geometry supplying an explicit finite generating set for that \(\mathbf5\).

This does not yet prove that the physical family dynamics selects a particular point, path, or holonomy in the complement. It shows that the required non-spin-one directions already have a concrete geometric carrier.

### L.6 Remaining dynamical gate

The current chain is therefore

\`\`\`text
compact spin-1 subgroup                         = CLOSED
five-dimensional SU(3)/SO(3) tangent complement = CLOSED
N=5/A5 irreducible realization                  = CLOSED
six icosahedral quadrupoles -> full su(3)        = CLOSED
physical family selector / path / holonomy       = OPEN
\`\`\`

The remaining problem is selector dynamics, not carrier existence.

Status:

\`PHYSICAL_FAMILY_SELECTOR_ON_RIGID_3_PLUS_5_CARRIER_OPEN\`.


---

## Appendix M — NEW 2026-09-19 — Stage-65/66 stationary cubic selector closure

### M.1 Historical Stage-64 OPEN is superseded by a frozen prospective selector

Stage 64 correctly records that the rigid five-dimensional carrier still leaves a two-dimensional cubic invariant space,

\[
\operatorname{span}
\{I_{\rm iso},I_{A5}\},
\]

and that no canonical relative coefficient had yet been promoted at that stage.

Stage 65 then freezes, before validation and before CKM/mass comparison, the projectively normalized functional

\[
\boxed{
\mathcal F_\eta(S)
=
I_{\rm iso}(S)
+
\eta I_{A5}(S)
}
\]

together with the constrained-stationarity condition at the already frozen ordered axis \(D_0\),

\[
\boxed{
\nabla\mathcal F_\eta(D_0)
=
\lambda D_0.
}
\]

The selector freeze explicitly excludes CKM entries, CKM phase/Jarlskog targets, fermion masses, PMNS data, \(A_{\rm seed}\) alignment and retrospective coefficient tuning.

Status:

\`STAGE_65_STATIONARY_ORDERED_AXIS_SELECTOR_FROZEN_PREVALIDATION\`.

### M.2 Unique selector coefficient

Stage 66 solves the frozen condition and obtains the unique real projective coefficient

\[
\boxed{
\eta_*
=
-\frac{75(59+21\sqrt5)}{638}
}
\]

with

\[
\boxed{
\lambda_*
=
-\frac{8765+4758\sqrt5}{4785}.
}
\]

Numerically,

\[
\eta_*
\approx
-12.4558104460222.
\]

The present crosswalk validator independently reconstructs the six icosahedral quadrupoles, the two cubic gradients and the constrained stationarity equations and reproduces both exact formulas to numerical tolerance.

Status:

\`STAGE66_UNIQUE_STATIONARY_CUBIC_SELECTOR_CLOSED_SADDLE\`.

### M.3 Constrained Hessian

At the frozen stationary point, the constrained Hessian has signature

\[
\boxed{
(-,+,+,+).
}
\]

Thus the selected point is a saddle, not a minimum.

This classification is retained exactly as obtained and is not repaired by changing \(\eta\).

### M.4 Independent \(C_3\)-orbit check

The Stage-65 selector equation deliberately excludes \(A_{\rm seed}\) from solving \(\eta\).

Only after the selector is fixed, compare the pre-existing orbit

\[
A_0=A_{\rm seed},
\qquad
A_1=P_3A_{\rm seed}P_3^T,
\qquad
A_2=P_3^2A_{\rm seed}(P_3^T)^2.
\]

The unique negative Hessian mode aligns exactly with

\[
\boxed{
A_1=P_3A_{\rm seed}P_3^T.
}
\]

Hence the \(C_3\)-orbit alignment is an external structural check rather than an input used to fit the selector.

### M.5 Updated selector frontier

The Stage-64 broad OPEN is therefore narrowed.

Current status:

\`\`\`text
five-dimensional SU(3)/SO(3) complement carrier
    = CLOSED

two independent cubic invariants
    = CLOSED

unique projective cubic selector coefficient eta
    = CLOSED

selector stationarity
    = CLOSED

Hessian classification
    = CLOSED / SADDLE

negative mode alignment with independent C3 A_seed orbit
    = CLOSED

branch symbol -> physical family operator
    = OPEN

exact Collatz/twin-prime rhythm rho_s(k)
    = OPEN

split-real -> compact-real-form dynamical selection
    = OPEN

physical mass/mixing spectrum
    = OPEN
\`\`\`

Therefore the corrected remaining gate is

\`CUBIC_SELECTOR_CLOSED__BRANCH_OPERATOR_RHYTHM_AND_REALFORM_SELECTION_OPEN\`.

The selector closure is mathematical. It does not by itself identify the saddle mode with a physical fermion generation or derive CKM/PMNS/masses.


---

## Appendix N — NEW 2026-09-19 — Exact split-real branch operators and rhythm provenance firewall

### N.1 Stage-43 ordering principle versus weight map

Stage 43 already distinguishes two statements:

\`\`\`text
ordered Collatz-step accumulation
    = PRESENT

exact rho_s(k)
    = OPEN DERIVATION DEBT
\`\`\`

The archived reference simulation

\`archive/v7.9/full/01_foundational_formal_notes/phase_hamiltonian_english_derivations/scripts/collatz_phase_sim.py\`

at Git blob SHA

\`7a06e83f70a7061678752773f4fc3e5868fe6d08\`

states explicitly:

\`\`\`text
The exact rhythm map is a model choice.
\`\`\`

Its default

\[
\eta_{\rm legacy}=0.35
\]

is therefore not a current derivation and is not promoted here.

Status:

\`LEGACY_BOUNDED_RHYTHM_MODEL_CHOICE_NOT_PROMOTED\`.

### N.2 Branch symbols already have exact split-real operators

Stage 49 supplies the determinant-one two-component branch operators

\[
E\mapsto \widehat M_E,
\qquad
O\mapsto \widehat M_O,
\]

and Stage 50 supplies the symmetric-square representation

\[
\rho_2:
SL(2,\mathbb R)\to SL(3,\mathbb R).
\]

Hence the branch symbols have exact three-component operators

\[
\boxed{
E\mapsto R_E=\rho_2(\widehat M_E),
\qquad
O\mapsto R_O=\rho_2(\widehat M_O).
}
\]

The representation law is exact:

\[
\boxed{
\rho_2(M_1M_2)
=
\rho_2(M_1)\rho_2(M_2).
}
\]

The current validator checks this independently for both ordered products \(EO\) and \(OE\).

Moreover,

\[
R_ER_O\neq R_OR_E,
\]

so branch-word ordering survives faithfully in the three-component carrier.

Status:

\`BRANCH_SYMBOL_TO_SPLIT_REAL_THREE_OPERATOR_CLOSED\`.

### N.3 What remains open

The exact operators \(R_E,R_O\) live in the split-real carrier

\[
SL(3,\mathbb R),
\]

not directly in the compact physical-family carrier \(SU(3)_F\).

Stage 51 forbids a fixed direct unitarization, while Stage 52 supplies only the existence of a compact-real-form bridge.

Therefore

\[
\boxed{
E/O\to R_E/R_O
}
\]

is closed, but

\[
\boxed{
E/O\stackrel{?}{\longrightarrow}U_E/U_O\in SU(3)_F
}
\]

remains open.

Separately, the Hamiltonian weighting

\[
\rho_s(k)
\]

remains an exact derivation debt. Word length/order and Hamiltonian time/rhythm are not identified.

Current status:

\`\`\`text
branch symbol -> split-real 3x3 operator
    = CLOSED

branch-word noncommutativity/order
    = CLOSED

legacy bounded rhythm eta=0.35
    = MODEL CHOICE / NOT PROMOTED

exact rho_s(k)
    = OPEN

split-real branch operator -> compact SU(3)_F operator
    = OPEN
\`\`\`

The corrected aggregate frontier is

\`CUBIC_SELECTOR_CLOSED__SPLIT_REAL_BRANCH_OPERATOR_CLOSED__RHYTHM_AND_COMPACT_FAMILY_MAP_OPEN\`.


---

## Appendix O — NEW 2026-09-19 — Exact Poincare branch-length alphabet

### O.1 Canonical hyperbolic translation lengths

Stage 49 places the normalized Collatz branch generators in

\[
PSL(2,\mathbb R)
\]

with

\[
\widehat M_E=
\begin{pmatrix}
1/\sqrt2&0\\
0&\sqrt2
\end{pmatrix},
\qquad
\widehat M_O=
\frac1{\sqrt3}
\begin{pmatrix}
3&1\\
0&1
\end{pmatrix}.
\]

For a hyperbolic element \(g\in PSL(2,\mathbb R)\), in the standard curvature-\(-1\) Poincare normalization, the canonical translation length is

\[
\ell(g)
=
2\,\operatorname{arcosh}
\left(
\frac{|\operatorname{tr}g|}{2}
\right).
\]

Therefore

\[
\boxed{
\ell_E=\ln2
}
\]

and

\[
\boxed{
\ell_O=\ln3.
}
\]

Status:

\`POINCARE_BRANCH_TRANSLATION_LENGTH_ALPHABET_CLOSED\`.

### O.2 Signed local scale cocycle

On the real boundary the two affine branch derivatives are

\[
E'(x)=\frac12,
\qquad
O'(x)=3.
\]

Hence the signed logarithmic scale cocycle is

\[
\boxed{
\chi(E)=-\ln2,
\qquad
\chi(O)=+\ln3.
}
\]

For an ordered branch word \(w=b_1\cdots b_m\),

\[
\chi(w)
=
\sum_j\chi(b_j)
\]

reproduces the logarithm of the exact affine slope of the composite.

For the frozen word

\[
w_1=OEOE,
\]

\[
\chi(w_1)
=
2\ln3-2\ln2
=
\ln\frac94.
\]

For the long third-family word with 34 odd and 56 even steps,

\[
\chi(w_3)
=
34\ln3-56\ln2
=
\ln\frac{3^{34}}{2^{56}}.
\]

Status:

\`SIGNED_LOG_JACOBIAN_COCYCLE_CLOSED\`.

### O.3 Exact relation to the canonical information scale

The project fixes

\[
\kappa=\frac{\ln2}{24\pi}.
\]

Because

\[
\ell_E=\ln2,
\]

one has the exact identity

\[
\boxed{
\kappa
=
\frac{\ell_E}{24\pi}.
}
\]

No fit or external physical target enters this equality.

The dimensionless odd/even geometric length ratio is

\[
\boxed{
\frac{\ell_O}{\ell_E}
=
\frac{\ln3}{\ln2}
=
\log_2 3.
}
\]

### O.4 Geometric rhythm alphabet versus Hamiltonian rhythm

The exact Poincare geometry therefore supplies the positive branch-length alphabet

\[
\boxed{
E\mapsto\ln2,
\qquad
O\mapsto\ln3.
}
\]

This is a canonical geometric scalar attached to each exact Collatz branch.

Status:

\`CANONICAL_GEOMETRIC_RHYTHM_ALPHABET_AVAILABLE\`.

However, the Hamiltonian scaffold uses a symbol

\[
\rho_s(k)
\]

as a dynamical weighting factor. The equality

\[
\boxed{
\rho_s(k)
\stackrel{?}{=}
\ell(\widehat M_{b_k})
}
\]

is not promoted by this Appendix.

The distinction is:

\`\`\`text
exact Poincare branch translation lengths
    = CLOSED

exact signed log-Jacobian cocycle
    = CLOSED

geometric positive branch-length alphabet
    = CLOSED

identification with Hamiltonian rho_s(k)
    = OPEN
\`\`\`

Thus the prior broad rhythm debt is narrowed to a binding problem, not a lack of an exact branch-local geometric scale.

Current aggregate frontier:

\`CUBIC_SELECTOR_CLOSED__SPLIT_REAL_BRANCH_OPERATOR_CLOSED__GEOMETRIC_RHYTHM_ALPHABET_CLOSED__RHO_BINDING_AND_COMPACT_FAMILY_MAP_OPEN\`.


---

## Appendix P — NEW 2026-09-19 — Compact \(SU(3)_F\) endpoint class versus branch-wise real-form lift

### P.1 Current family endpoint is already compact and unitary

The current TIR family carrier is

\[
\boxed{
V_F\cong\mathbb C^3
}
\]

with full determinant-one family transformations

\[
\boxed{
U_F\in SU(3)_F.
}
\]

This is not introduced by the present crosswalk. It is already a current structural parent of the flavour branch.

Stage 25 independently uses

\[
I_3\otimes I_2\otimes U_F,
\qquad
U_F\in SU(3)_F,
\]

on the factorized matter carrier.

Therefore the physical family endpoint class is a positive-definite compact unitary three-carrier.

Status:

\`CURRENT_FAMILY_ENDPOINT_COMPACT_SU3F_REQUIRED\`.

### P.2 Stage-51 no-go remains intact

The Stage-50 split-real generators

\[
R_E,R_O\in SL(3,\mathbb R)
\]

preserve an indefinite form. Stage 51 proves that no fixed similarity transformation can convert the same split-real representation into the current compact unitary family representation.

Hence

\[
\boxed{
\operatorname{Sym}^2(PSL(2,\mathbb R))
\not\sim SU(3)_F
}
\]

by fixed similarity.

The endpoint requirement does not weaken or bypass this no-go.

### P.3 Stage-52 bridge fixes availability, not branch-wise dynamics

Stage 52 supplies the mathematically valid change-of-real-form route

\[
\mathfrak{sl}(2,\mathbb R)
\to
\mathfrak{sl}(2,\mathbb C)
\leftarrow
\mathfrak{su}(2)
\xrightarrow{\operatorname{Sym}^2}
\mathfrak{su}(3).
\]

Combined with the already-current family carrier, this means the **target real-form class** is no longer ambiguous:

\[
\boxed{
\text{physical family endpoint}
=
SU(3)_F.
}
\]

What remains unresolved is the dynamical map that takes the exact ordered split-real branch operators to definite compact family operators,

\[
\boxed{
R_E,R_O
\stackrel{?}{\longrightarrow}
U_E,U_O\in SU(3)_F.
}
\]

Status:

\`COMPACT_ENDPOINT_CLASS_FIXED__DYNAMICAL_BRANCHWISE_LIFT_OPEN\`.

### P.4 Corrected real-form frontier

The broad phrase

\`compact-real-form selection OPEN\`

is therefore decomposed into two levels:

\`\`\`text
physical family endpoint class SU(3)_F
    = CLOSED / CURRENT PARENT

direct split-real similarity to SU(3)_F
    = REFUTED

complexification/change-of-real-form bridge
    = AVAILABLE

branch-wise lift R_E,R_O -> U_E,U_O in SU(3)_F
    = OPEN
\`\`\`

This distinction is important. Unitarity fixes what class the physical family transformation must belong to; it does not derive the map from Collatz/Poincare branch dynamics into that class.

Current split-real/unitary status:

\`DIRECT_UNITARIZATION_REFUTED__COMPACT_SU3F_ENDPOINT_REQUIRED__BRANCHWISE_REALFORM_LIFT_OPEN\`.

Current aggregate family-dynamics frontier:

\`CUBIC_SELECTOR_CLOSED__SPLIT_REAL_BRANCH_OPERATOR_CLOSED__GEOMETRIC_RHYTHM_ALPHABET_CLOSED__COMPACT_ENDPOINT_CLASS_FIXED__RHO_BINDING_AND_BRANCHWISE_COMPACT_LIFT_OPEN\`.


---

## Appendix Q — NEW 2026-09-19 — Canonical polar compactification no-go

### Q.1 Why test the polar factor

Stage 30 already uses the unique orthogonal polar factor as a canonical mathematical diagnostic for a nonsingular structural overlap matrix, while explicitly refusing to promote that diagnostic to a physical family-mixing operator without an independent rule.

Apply the same canonical diagnostic to the exact Stage-49 branch generators before introducing any new compactification ansatz.

For a real \(2\times2\) matrix with positive determinant,

\[
M=QP,
\qquad
Q\in SO(2),
\qquad
P=P^T>0,
\]

is the unique polar decomposition.

### Q.2 Exact compact factors of the two branch generators

For the even branch,

\[
\widehat M_E=
\begin{pmatrix}
1/\sqrt2&0\\
0&\sqrt2
\end{pmatrix}
\]

is already positive symmetric. Hence

\[
\boxed{
Q_E=I_2.
}
\]

For the odd branch,

\[
\widehat M_O=
\frac1{\sqrt3}
\begin{pmatrix}
3&1\\
0&1
\end{pmatrix},
\]

the exact orthogonal polar factor is

\[
\boxed{
Q_O=
\frac1{\sqrt{17}}
\begin{pmatrix}
4&1\\
-1&4
\end{pmatrix}
\in SO(2).
}
\]

### Q.3 Generator-wise polar assignment loses branch order

If one defines a compact generator assignment by

\[
E\mapsto Q_E,
\qquad
O\mapsto Q_O,
\]

then \(Q_E=I\). Consequently

\[
Q_EQ_O=Q_OQ_E=Q_O.
\]

Thus the two distinct ordered words

\[
EO
\qquad\text{and}\qquad
OE
\]

become identical after generator-wise polar compactification.

Therefore this map destroys exactly the ordering information that the Collatz branch monoid carries.

Status:

\`GENERATORWISE_POLAR_COMPACTIFICATION_ORDER_BLIND\`.

### Q.4 Word-wise polar factor is not a representation

One may instead take the polar factor only after composing the split-real word.

For the two words,

\[
Q(\widehat M_E\widehat M_O)
\neq
Q(\widehat M_O\widehat M_E),
\]

so word order is then retained.

However,

\[
\boxed{
Q(M_1M_2)
\neq
Q(M_1)Q(M_2)
}
\]

already for the branch generators. Therefore the word-wise polar-factor operation is not a monoid representation of the Collatz branch alphabet.

It cannot replace the required branch-symbol operator map.

### Q.5 Consequence

The most immediate canonical compactification route is therefore excluded in both natural forms:

\`\`\`text
generator-wise polar compact factors
    = representation-like product rule
    = loses E positions/order

word-wise polar compact factor
    = preserves some order information
    = not a branch-monoid homomorphism
\`\`\`

Status:

\`CANONICAL_POLAR_COMPACTIFICATION_REFUTED_AS_SUFFICIENT_BRANCH_LIFT\`.

This does not refute every possible split-real-to-compact dynamical map. It refutes only the canonical polar-factor shortcut.

The remaining compact-family gate is therefore narrower:

\[
\boxed{
R_E,R_O
\stackrel{?}{\longrightarrow}
U_E,U_O\in SU(3)_F
}
\]

through a non-polar mechanism that preserves ordered branch composition and can access the full \(\mathbf3\oplus\mathbf5\) family algebra.

Current frontier:

\`CUBIC_SELECTOR_CLOSED__SPLIT_REAL_BRANCH_OPERATOR_CLOSED__GEOMETRIC_RHYTHM_ALPHABET_CLOSED__COMPACT_ENDPOINT_CLASS_FIXED__CANONICAL_POLAR_LIFT_REFUTED__RHO_BINDING_AND_NONPOLAR_COMPACT_LIFT_OPEN\`.


---

## Appendix R — NEW 2026-09-19 — Complex-holonomy mechanism versus clean branch-source map

### R.1 Real family misalignment is CP-trivial

Stage 35 constructs the Hermitian pair

\[
H_u=OO^T,
\qquad
H_d=O^TO
\]

from the pre-CKM real cross-sector map.

The operators do not commute and therefore produce nontrivial family-frame misalignment, but the relative transformation remains real:

\[
V_{\rm rel}\in SO(3)\subset SU(3)_F.
\]

Hence

\[
\boxed{J(V_{\rm rel})=0.}
\]

Status:

\`STAGE35_REAL_FAMILY_MISALIGNMENT_CP_TRIVIAL\`.

### R.2 A non-polar complex mechanism already exists

Stage 36 uses the pre-existing complex open-holonomy data

\[
a_{ij},
\qquad
\phi_{ij},
\]

through the coefficient-free lift

\[
\boxed{
W^\mathbb C_{ij}
=
a_{ij}e^{i\phi_{ij}}.
}
\]

The resulting Hermitian pair

\[
H_u=WW^\dagger,
\qquad
H_d=W^\dagger W
\]

is noncommuting, and its relative family transformation lies in \(SU(3)_F\) after removal of the global determinant phase.

Stage 36 obtains a non-removable rephasing-invariant plaquette phase and

\[
\boxed{
J_F\neq0.
}
\]

Therefore a non-polar complex-holonomy route into CP-capable family dynamics already exists at mechanism level.

Status:

\`NONPOLAR_COMPLEX_HOLONOMY_CP_MECHANISM_EXISTS_SOURCE_QUARANTINED\`.

### R.3 Provenance quarantine remains active

The Stage-36 heavy-family source rows retain their historical quarantine classification.

Accordingly, the Stage-36 result establishes

\[
\text{mechanism feasibility}
\]

but does not supply a clean source-derived family operator for physical promotion.

No CKM phase or observed mass is inserted by the Stage-36 construction, but the quarantined heavy-family bridge rows prevent promotion.

### R.4 Later stages do not remove this source debt

Stage 37 proves that two sector operators that are merely scalar functions of one common normal family axis commute and cannot produce nontrivial family mixing.

Stage 38 gives an exact CP-capable \(C_3/F_3\) character mechanism.

Stage 39 freezes a minimal two-operator family candidate.

Stage 40 retains the mechanism but records

\`STAGE_40_FULL_CKM_SHAPE_FAIL__MECHANISM_RETAINED\`

without retuning.

Thus none of these stages creates the missing source map

\[
\boxed{
\text{Collatz/Poincare branch dynamics}
\stackrel{?}{\longrightarrow}
W^\mathbb C_{\rm family}.
}
\]

### R.5 Correct remaining non-polar gate

The current situation is therefore:

\`\`\`text
real family misalignment
    = CLOSED / J=0

complex open-holonomy CP mechanism
    = CLOSED AT MECHANISM LEVEL / J!=0

Stage-36 source provenance
    = QUARANTINED

canonical polar compactification
    = REFUTED AS SUFFICIENT

clean Collatz/Poincare -> complex family holonomy source map
    = OPEN
\`\`\`

Status:

\`OPEN_CLEAN_COLLATZ_POINCARE_TO_COMPLEX_FAMILY_HOLONOMY_SOURCE_MAP\`.

The current aggregate frontier is

\`CUBIC_SELECTOR_CLOSED__SPLIT_REAL_BRANCH_OPERATOR_CLOSED__GEOMETRIC_RHYTHM_ALPHABET_CLOSED__COMPACT_ENDPOINT_CLASS_FIXED__POLAR_LIFT_REFUTED__COMPLEX_HOLONOMY_MECHANISM_EXISTS__RHO_BINDING_AND_CLEAN_BRANCH_TO_COMPLEX_HOLONOMY_MAP_OPEN\`.


---

## Appendix S — NEW 2026-09-19 — Continuous \(PSL(2,\mathbb R)\to SU(3)_F\) real-Lie lift no-go

### S.1 Source algebra is simple and noncompact

Use the standard basis of

\[
\mathfrak{sl}(2,\mathbb R)
\]

given by

\[
H=
\begin{pmatrix}
1&0\\0&-1
\end{pmatrix},
\qquad
E=
\begin{pmatrix}
0&1\\0&0
\end{pmatrix},
\qquad
F=
\begin{pmatrix}
0&0\\1&0
\end{pmatrix}.
\]

The Killing-form matrix in the ordered basis \((H,E,F)\) is

\[
\boxed{
B_{\mathfrak{sl}_2}
=
\begin{pmatrix}
8&0&0\\
0&0&4\\
0&4&0
\end{pmatrix}
}
\]

with eigenvalues

\[
\boxed{
8,\ 4,\ -4.
}
\]

Hence its real signature is

\[
\boxed{(2,1)}.
\]

This is the noncompact real form.

### S.2 No nonzero real-Lie embedding into compact \(\mathfrak{su}(3)\)

The real Lie algebra

\[
\mathfrak{sl}(2,\mathbb R)
\]

is simple. Therefore the kernel of any real Lie-algebra homomorphism

\[
\varphi:
\mathfrak{sl}(2,\mathbb R)
\to
\mathfrak{su}(3)
\]

is either the full algebra or zero.

If \(\varphi\neq0\), it must therefore be injective.

But every real Lie subalgebra of the compact algebra \(\mathfrak{su}(3)\) is of compact type; it inherits a positive-definite invariant inner product from the compact target. The noncompact simple algebra \(\mathfrak{sl}(2,\mathbb R)\), with indefinite Killing form, cannot be isomorphic to such a compact subalgebra.

Therefore

\[
\boxed{
\operatorname{Hom}_{\rm Lie,\mathbb R}
\big(
\mathfrak{sl}(2,\mathbb R),
\mathfrak{su}(3)
\big)
=
\{0\}.
}
\]

Equivalently, there is no nontrivial continuous Lie-group representation

\[
PSL(2,\mathbb R)
\longrightarrow
SU(3)
\]

whose differential realizes the Stage-49 split-real algebra as a compact family subalgebra.

Status:

\`NONTRIVIAL_CONTINUOUS_PSL2R_TO_SU3F_LIE_HOMOMORPHIC_LIFT_REFUTED\`.

### S.3 Relation to Stage 52

This does not contradict Stage 52.

Stage 52 uses the shared complexification

\[
\mathfrak{sl}(2,\mathbb R)\otimes\mathbb C
\cong
\mathfrak{sl}(2,\mathbb C)
\cong
\mathfrak{su}(2)\otimes\mathbb C
\]

and then changes real form before applying the compact symmetric square.

Thus

\[
\mathfrak{sl}(2,\mathbb R)
\to
\mathfrak{sl}(2,\mathbb C)
\leftarrow
\mathfrak{su}(2)
\]

is not a direct homomorphism from the split real form into the compact real form. The arrows meet only after complexification.

### S.4 Consequence for the remaining family map

Together with Appendix Q, two simple compactification routes are now excluded:

\`\`\`text
canonical polar factor
    = REFUTED AS SUFFICIENT

continuous real-Lie homomorphism PSL(2,R) -> SU(3)_F
    = REFUTED
\`\`\`

Therefore a nontrivial branch-to-family map must use additional structure.

Admissible remaining classes include:

\`\`\`text
discrete branch-monoid representation
complex holonomy
state-dependent operator map
complexification + independently derived dynamical selector
\`\`\`

The current Stage-36 complex-holonomy mechanism is structurally of the required non-polar/non-real-homomorphic type, but its Collatz/Poincare source map remains open.

The remaining operator gate is therefore

\`OPEN_DISCRETE_OR_HOLONOMIC_NONPOLAR_BRANCHWISE_SU3F_LIFT\`.

Current aggregate frontier:

\`CUBIC_SELECTOR_CLOSED__SPLIT_REAL_BRANCH_OPERATOR_CLOSED__GEOMETRIC_RHYTHM_ALPHABET_CLOSED__COMPACT_ENDPOINT_FIXED__POLAR_AND_CONTINUOUS_LIE_LIFTS_REFUTED__COMPLEX_HOLONOMY_EXISTS__RHO_BINDING_AND_DISCRETE_HOLONOMIC_BRANCH_MAP_OPEN\`.
