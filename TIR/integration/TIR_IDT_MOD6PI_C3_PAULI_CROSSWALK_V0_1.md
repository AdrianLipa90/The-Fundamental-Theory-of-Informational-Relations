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


---

## Appendix T — NEW 2026-09-19 — Scalar \(q_C\) separable-phase CP no-go

### T.1 Exact current IDT phase vertices

The current IDT/TIR Collatz-Fubini-Study interface supplies the scalar projective phase coordinate

\[
\zeta_C(n)=e^{2\pi i q_C(n)},
\qquad
q_C(Cn)=2q_C(n)\pmod1.
\]

On the active Stage-22 center projection,

\[
m_1=4,\qquad m_2=6,\qquad m_3=12,
\]

the exact phase vertices are

\[
\boxed{
q_1=\frac17,\qquad
q_2=\frac{141}{448},\qquad
q_3=\frac{141}{896}.
}
\]

These are exact scalar vertex data.

### T.2 Natural vertex-difference phase is separable

The most immediate pair phase generated solely from those vertex scalars is

\[
\boxed{
\phi_{ij}=2\pi(q_i-q_j).
}
\]

In turns, the exact antisymmetric matrix is

\[
\frac{\phi_{ij}}{2\pi}
=
\begin{pmatrix}
0 & -11/64 & -13/896\\
11/64 & 0 & 141/896\\
13/896 & -141/896 & 0
\end{pmatrix}.
\]

More generally, any phase law of the form

\[
\phi_{ij}=\alpha_i-\beta_j
\]

is row/column separable.

### T.3 Every rephasing-invariant plaquette vanishes

For any row pair \(i,j\) and column pair \(k,l\), the plaquette phase is

\[
\Phi_{ij;kl}
=
\phi_{ik}
+
\phi_{jl}
-
\phi_{il}
-
\phi_{jk}.
\]

Substituting a separable phase,

\[
\Phi_{ij;kl}
=
(\alpha_i-\beta_k)
+
(\alpha_j-\beta_l)
-
(\alpha_i-\beta_l)
-
(\alpha_j-\beta_k)
=
0.
\]

Therefore

\[
\boxed{
\Phi_{ij;kl}=0
}
\]

for every plaquette, exactly.

Equivalently, if

\[
W_{ij}=a_{ij}e^{i(\alpha_i-\beta_j)},
\]

all of these phases can be removed by independent row and column rephasings.

Status:

\`SCALAR_VERTEX_QC_PHASE_DIFFERENCE_CP_NO_GO\`.

### T.4 Consequence for Stage 36

Stage 36 requires a phase matrix with a nonzero rephasing-invariant plaquette phase and obtains

\[
J_F\neq0
\]

at mechanism level.

Therefore the Stage-36 complex phase cannot be generated solely by assigning one scalar \(q_C\) value to each family label and taking pair differences.

The required phase source must contain genuinely pair-dependent information:

\[
\boxed{
\phi_{ij}
\neq
\alpha_i-\beta_j
}
\]

for at least one nontrivial plaquette.

Status:

\`NONSEPARABLE_PAIR_DEPENDENT_HOLONOMY_REQUIRED_FOR_NONZERO_PLAQUETTE_PHASE\`.

### T.5 Boundary

This is not a no-go for the IDT phase coordinate itself.

The scalar \(q_C\) remains an exact projective phase coordinate and may still contribute to a larger relational operator, path-local cochain, curvature integral, or state-dependent holonomy.

The no-go is narrower:

\`\`\`text
scalar q_C vertex data
    = EXACT

q_i-q_j pair phase
    = EXACT / SEPARABLE

all plaquette phases from q_i-q_j
    = ZERO EXACT

scalar q_C alone as Stage-36 CP source
    = REFUTED

genuinely pair-dependent nonseparable holonomy
    = REQUIRED FOR NONZERO PLAQUETTE CP
\`\`\`

Thus the current clean-source gate becomes

\`OPEN_CLEAN_NONSEPARABLE_COLLATZ_POINCARE_TO_COMPLEX_FAMILY_HOLONOMY_MAP\`.

Current aggregate frontier:

\`CUBIC_SELECTOR_CLOSED__SPLIT_REAL_BRANCH_OPERATOR_CLOSED__GEOMETRIC_RHYTHM_ALPHABET_CLOSED__COMPACT_ENDPOINT_FIXED__POLAR_AND_CONTINUOUS_LIE_LIFTS_REFUTED__SCALAR_QC_CP_REFUTED__COMPLEX_HOLONOMY_EXISTS__RHO_BINDING_AND_NONSEPARABLE_DISCRETE_HOLONOMIC_BRANCH_MAP_OPEN\`.


---

## Appendix U — NEW 2026-09-19 — Equatorial \(q_C\) Bargmann-phase no-go

### U.1 Scalar \(q_C\) on the existing equatorial \(CP^1\) carrier

The Collatz-Fubini-Study interface admits the equal-weight qubit ray

\[
\boxed{
|\psi(q)\rangle
=
\frac{|0\rangle+e^{2\pi iq}|1\rangle}{\sqrt2}.
}
\]

All such rays lie on one equator

\[
S^1\subset\mathbb CP^1.
\]

For two such rays,

\[
\langle\psi(q_i)|\psi(q_j)\rangle
=
\frac{1+e^{2\pi i(q_j-q_i)}}{2}
=
e^{i\pi(q_j-q_i)}
\cos\!\big(\pi(q_j-q_i)\big).
\]

### U.2 Three-point Bargmann phase telescopes on one equator

For three active rays, define the Bargmann invariant

\[
B_{123}
=
\langle\psi_1|\psi_2\rangle
\langle\psi_2|\psi_3\rangle
\langle\psi_3|\psi_1\rangle.
\]

Its explicit phase factor is

\[
\exp\left\{
i\pi\left[
(q_2-q_1)
+
(q_3-q_2)
+
(q_1-q_3)
\right]
\right\}.
\]

The exponent vanishes exactly:

\[
\boxed{
(q_2-q_1)+(q_3-q_2)+(q_1-q_3)=0.
}
\]

Hence the Bargmann product is real.

For the active exact values

\[
q_1=\frac17,
\qquad
q_2=\frac{141}{448},
\qquad
q_3=\frac{141}{896},
\]

all three pair separations satisfy

\[
|q_i-q_j|<\frac12.
\]

Therefore every cosine factor is positive and

\[
\boxed{
B_{123}>0,
\qquad
\arg B_{123}=0.
}
\]

Status:

\`ACTIVE_SCALAR_QC_EQUATORIAL_BARGMANN_PHASE_ZERO\`.

### U.3 This is stronger than the separable plaquette no-go

Appendix T showed that pair phases generated as

\[
\phi_{ij}=2\pi(q_i-q_j)
\]

have zero rephasing-invariant plaquette phase.

The present result additionally shows that promoting the same scalar \(q_C\) values to equatorial projective rays and taking the standard three-ray Bargmann/Pancharatnam phase still does not generate a nonzero geometric phase for the active triplet.

Thus neither of the two direct constructions

\[
q_i-q_j
\]

nor

\[
\arg\!
\left(
\langle\psi_1|\psi_2\rangle
\langle\psi_2|\psi_3\rangle
\langle\psi_3|\psi_1\rangle
\right)
\]

supplies the Stage-36 CP phase.

### U.4 Nonzero Bargmann phase exists elsewhere in current TIR

The current hexahedral Bloch dual-frame theorem contains exact non-coplanar multi-ray triangles. For the ordered Bloch rays

\[
(+x,+y,+z)
\]

it gives

\[
\boxed{
\gamma_B=+\frac{\pi}{4}
}
\]

in the stated orientation convention.

This proves that the TIR geometric framework can carry a nonzero Bargmann/Pancharatnam phase once the rays span genuine two-dimensional spherical area.

It does **not** identify that spatial/hexahedral triangle with the family sector.

### U.5 Correct remaining CP source requirement

The active scalar \(q_C\) equator is therefore insufficient by itself.

A viable clean family CP source must add at least one structure not contained in the single scalar equatorial coordinate, for example:

\`\`\`text
genuinely pair-dependent relational connection
non-equatorial CP1 motion
multi-ray Berry geometry with nonzero enclosed area
path-local holonomy not reducible to vertex phases
state-dependent complex operator data
\`\`\`

Status:

\`ADDITIONAL_NONSEPARABLE_CONNECTION_OR_NON_EQUATORIAL_MULTI_RAY_GEOMETRY_REQUIRED\`.

The sector firewall remains active: a nonzero Berry triangle from another TIR carrier is not reassigned to the family sector without an explicit intertwiner.

Current aggregate frontier:

\`CUBIC_SELECTOR_CLOSED__SPLIT_REAL_BRANCH_OPERATOR_CLOSED__GEOMETRIC_RHYTHM_ALPHABET_CLOSED__COMPACT_ENDPOINT_FIXED__POLAR_AND_CONTINUOUS_LIE_LIFTS_REFUTED__SCALAR_QC_SEPARABLE_AND_EQUATORIAL_BARGMANN_CP_REFUTED__COMPLEX_HOLONOMY_EXISTS__RHO_BINDING_AND_NONSEPARABLE_DISCRETE_HOLONOMIC_BRANCH_MAP_OPEN\`.

---

## Appendix V — NEW 2026-09-19 — Family plaquette phase as a Bargmann quadrilateral

### V.1 Conditional overlap realization

Assume a family matrix admits a projective-overlap realization

\[
\boxed{W_{ij}=\langle u_i|d_j\rangle}
\]

for two ordered sets of nonzero complex rays \(\{|u_i\rangle\}\) and \(\{|d_j\rangle\}\).

No orthonormality assumption is required for the phase identity below.

### V.2 Rephasing-invariant plaquette

Take two row labels \(i,k\) and two column labels \(j,\ell\). The standard rephasing-invariant plaquette is

\[
\Pi_{ik;j\ell}=W_{ij}W_{kj}^*W_{k\ell}W_{i\ell}^*.
\]

Substituting the overlap realization gives

\[
\Pi_{ik;j\ell}
=
\langle u_i|d_j\rangle
\langle d_j|u_k\rangle
\langle u_k|d_\ell\rangle
\langle d_\ell|u_i\rangle.
\]

Therefore

\[
\boxed{
\Pi_{ik;j\ell}
=
\mathcal B_4(u_i,d_j,u_k,d_\ell)
}
\]

and

\[
\boxed{\arg\Pi_{ik;j\ell}=\arg\mathcal B_4(u_i,d_j,u_k,d_\ell).}
\]

Status:

`PLAQUETTE_PHASE_EQUALS_BARGMANN_QUADRILATERAL_UNDER_OVERLAP_REALIZATION`.

### V.3 Gauge invariance

Under independent ray rephasings

\[
|u_i\rangle\to e^{i\alpha_i}|u_i\rangle,
\qquad
|d_j\rangle\to e^{i\beta_j}|d_j\rangle,
\]

the four phase factors cancel exactly around the quadrilateral.

Hence the plaquette/Bargmann phase is ray-gauge invariant.

### V.4 Relation to the scalar-qC no-go

Appendices T/U show that a separable vertex-phase assignment of the form

\[
W_{ij}\propto e^{2\pi i(\alpha_i-\beta_j)}
\]

has trivial plaquette phase.

The Bargmann-quadrilateral identity shows what extra structure is missing: a nonseparable projective relation among four rays, not merely one scalar phase attached independently to each family label.

Thus the source problem is narrowed to

\[
\boxed{
\text{derive two projective family frames, or an equivalent pairwise holonomy, from source dynamics}.
}
\]

### V.5 Geometric support and authority firewall

The current hexahedral Bloch theorem independently demonstrates nonzero Berry/Bargmann phases in a multi-ray projective geometry. That establishes that the TIR projective machinery can support nontrivial gauge-invariant geometric phases.

It does not identify the hexahedral spatial rays with family rays.

GREMLIN candidate XFI.02 records the same plaquette-to-Bargmann relation as `EXACT_CONDITIONAL`, but the GREMLIN overlay is explicitly `CANDIDATE_ONLY / CHYBA / NON_CANONICAL_OVERLAY`.

This Appendix does not promote that candidate by authority; it independently verifies the algebraic identity.

Current state:

```text
scalar q_C vertex phase -> family CP
    = REFUTED

equatorial scalar-q_C Bargmann phase
    = ZERO

generic overlap plaquette -> Bargmann quadrilateral
    = CLOSED CONDITIONAL

nonzero projective Bargmann geometry exists in TIR
    = CLOSED IN OTHER CARRIERS

source-derived family overlap frames
    = OPEN
```

Remaining source gate:

`OVERLAP_REALIZATION_CONDITIONAL__SOURCE_STATES_NOT_YET_DERIVED`.

---

## Appendix W — NEW 2026-09-19 — (C_3) label/character projective frames and the (F_3) Bargmann plaquette

### W.1 Two exact projective frames are already present

Let the ordered Stage-22 family-seed basis be

\[
\{|s_1\rangle,|s_2\rangle,|s_3\rangle\}.
\]

The regular family cycle (P_3) has the exact character eigenbasis

\[
\{|\chi_0\rangle,|\chi_1\rangle,|\chi_2\rangle\}
\]

with overlap matrix

\[
\boxed{
\langle s_i|\chi_j\rangle=(F_3)_{ij}.
}
\]

Thus the two projective frames required by Appendix V already exist at the representation level.

Status:

`C3_LABEL_AND_CHARACTER_PROJECTIVE_FRAMES_CURRENT_EXACT`.

### W.2 A nonzero Bargmann quadrilateral is built into (F_3)

Take the plaquette formed by rows (1,2) and columns (1,2):

\[
\Pi
=
(F_3)_{11}(F_3)_{21}^*(F_3)_{22}(F_3)_{12}^*.
\]

With

\[
\omega=e^{2\pi i/3},
\]

one obtains

\[
\boxed{\Pi=\frac{\omega}{9}.}
\]

Therefore

\[
\boxed{\arg\Pi=\frac{2\pi}{3}}
\]

and

\[
\boxed{
\operatorname{Im}\Pi
=
\frac{1}{6\sqrt3}
=
J(F_3).
}
\]

By Appendix V this plaquette is exactly the Bargmann quadrilateral

\[
\langle s_1|\chi_0\rangle
\langle \chi_0|s_2\rangle
\langle s_2|\chi_1\rangle
\langle \chi_1|s_1\rangle.
\]

Status:

`F3_NONZERO_BARGMANN_PLAQUETTE_AND_JARLSKOG_CURRENT_EXACT`.

### W.3 What has been closed

The earlier Appendix-V source statement

`OVERLAP_REALIZATION_CONDITIONAL__SOURCE_STATES_NOT_YET_DERIVED`

is now narrowed.

At the (C_3) representation level:

```text
ordered label frame
    = DERIVED / CURRENT

C3 character frame
    = DERIVED / CURRENT

overlap matrix
    = F3 EXACT

Bargmann plaquette
    = NONZERO EXACT

J(F3)
    = 1/(6 sqrt(3)) EXACT
```

### W.4 Remaining physical sector gate

The unresolved step is not the existence of projective frames or a nonzero geometric plaquette phase.

It is the physical identification of the two exact (C_3) frames with the dynamical sector eigenframes that would enter a physical CKM- or PMNS-type relative transformation.

Thus

\[
\boxed{
\text{C3 label/character frames}
\stackrel{?}{\longrightarrow}
\text{physical sector frames}
}
\]

remains OPEN.

Status:

`REPRESENTATION_LEVEL_C3_FRAMES_DERIVED__PHYSICAL_SECTOR_FRAME_BINDING_OPEN`.

This does not promote (F_3) itself to the observed CKM or PMNS matrix.

---

## Appendix X — NEW 2026-09-19 — Stage-39 structural sector eigenframes and retained Stage-40 CKM-shape failure

### X.1 Frozen two-operator sector construction

Stage 39 freezes

\[
D=\operatorname{diag}\left(-\frac13,0,\frac1{\sqrt5}\right),
\qquad
C=F_3DF_3^\dagger,
\]

and the family of Hermitian operators

\[
\boxed{H(\alpha)=D+\alpha C.}
\]

The endpoint weights are imported from the earlier Stage-33 invariant receipt:

\[
a=\frac27,
\qquad
b=\frac29.
\]

The Stage-33 receipt states that these ratios are not reconstructed from CKM or mass data.

Stage 39 retains both assignments

```text
A: alpha_u = a, alpha_d = b
B: alpha_u = b, alpha_d = a
```

without selecting one by target fit.

### X.2 Two structural sector eigenframes exist

For either assignment,

\[
H_u=H(\alpha_u),
\qquad
H_d=H(\alpha_d)
\]

are noncommuting Hermitian operators.

Their ordered eigenframes define a relative transformation

\[
V=U_u^\dagger U_d,
\]

which is normalized to

\[
V\in SU(3).
\]

The present crosswalk independently reproduces the Stage-39 result:

\[
|J_A|=|J_B|
\approx
2.01742207300684\times10^{-5},
\]

with

\[
J_B=-J_A.
\]

Thus exchanging the two frozen endpoint assignments reverses the CP orientation while preserving the mixing scale.

Status:

`TWO_HERMITIAN_SECTOR_EIGENFRAMES_FROZEN_STRUCTURAL_CANDIDATE`

`NONZERO_CP_UNITARY_RELATIVE_TRANSFORMATION_REPRODUCED_NO_TARGET_FIT`.

### X.3 What remains open

The existence of two structural sector eigenframes is therefore not the remaining issue.

The unresolved questions are:

```text
which frozen assignment is physically up/down
    = OPEN

whether the Stage-39 structural relative transformation is the physical CKM map
    = NOT PROMOTED

full CKM shape reproduction
    = FAIL (Stage 40 retained)
```

Stage 40 reports that the frozen construction underproduces the Cabibbo-like entry, overproduces other entries, and does not reproduce the full hierarchy. No retuning is introduced here.

Status:

`OPEN_STAGE39_A_B_ASSIGNMENT_NOT_SELECTED`

`STAGE40_FULL_CKM_SHAPE_FAIL_RETAINED`.

### X.4 Narrowed projective-frame frontier

Appendix W derived the label and character projective frames at the (C_3) representation level.

Stage 39 now supplies two further structural sector eigenframes from the same (D/F_3DF_3^\dagger) operator pair.

Therefore the projective-frame frontier is narrowed to

`C3_PROJECTIVE_FRAMES_AND_STAGE39_STRUCTURAL_SECTOR_FRAMES_DERIVED__PHYSICAL_ASSIGNMENT_AND_CKM_PROMOTION_OPEN`.

This remains a structural/postdictive candidate line; it is not a successful quantitative CKM derivation.

---

## Appendix Y — NEW 2026-09-19 — Coefficient-orientation firewall for Stage-39 sector assignment

### Y.1 The current coefficient theorem does not define \(\alpha_u,\alpha_d\)

The current coefficient-role theorem types

\[
R_h\leftrightarrow h,
\qquad
R_a\leftrightarrow a,
\qquad
R_b\leftrightarrow b,
\qquad
R_c\leftrightarrow c,
\]

and supplies an exact source-consensus sign rule when the declared gradient, directed-orbit and chiral orientation sources agree.

It does not define a map

\[
(h,a,b,c)
\longrightarrow
(\alpha_u,\alpha_d)
\]

for the Stage-39 sector operators.

Status:

`COEFFICIENT_ORIENTATION_DOES_NOT_YET_SELECT_STAGE39_SECTOR_ASSIGNMENT`.

### Y.2 The qC sign correlation is not an up/down assignment rule

The coefficient-cocycle theorem establishes the exact structural correlation

\[
\operatorname{sgn}(\Delta q_{ij})
=
\operatorname{sgn}(b_{ij})
=
\operatorname{sgn}(c_{ij})
\]

on the closed Stage-24 cycle.

That same theorem explicitly keeps

`q_phase_to_b_c_orientation_binding = OPEN`

and proves that a fixed scalar-linear qC-to-Z4 coefficient map is impossible.

Therefore the qC sign correlation cannot be silently promoted to

\[
\alpha_u=2/7,\quad\alpha_d=2/9
\]

or to its swapped assignment.

### Y.3 Target-leakage firewall

Stage 39 freezes both assignments

```text
A: alpha_u = 2/7, alpha_d = 2/9
B: alpha_u = 2/9, alpha_d = 2/7
```

before target comparison.

Swapping A and B reverses the sign of the structural Jarlskog invariant while preserving its magnitude.

Therefore selecting A or B because its sign matches an observed CKM sign convention would use the target to choose the theory branch.

That is not an admissible derivation.

Status:

`OBSERVED_CP_SIGN_SELECTION_FORBIDDEN_AS_TARGET_LEAKAGE`.

### Y.4 Current closure target

The Standard-Model reconciliation ledger states the next CKM closure operation directly:

```text
bind the full CKM matrix to the same coefficient-free
holonomic/orientation forcing theorem used by the mass/flavour sector
```

Hence the exact remaining theorem is

\[
\boxed{
\text{coefficient-free holonomic/orientation source state}
\longrightarrow
\text{Stage-39 sector assignment / family operator}
}
\]

without observed CKM entries, masses, or the sign of the measured Jarlskog invariant on the parent side.

Status:

`OPEN_COEFFICIENT_FREE_HOLONOMIC_SECTOR_ASSIGNMENT_THEOREM`.

Current frontier:

`CUBIC_SELECTOR_CLOSED__SPLIT_REAL_BRANCH_OPERATOR_CLOSED__GEOMETRIC_RHYTHM_ALPHABET_CLOSED__COMPACT_ENDPOINT_FIXED__POLAR_AND_CONTINUOUS_LIE_LIFTS_REFUTED__SCALAR_QC_CP_REFUTED__C3_F3_BARGMANN_FRAMES_CLOSED__STAGE39_STRUCTURAL_SECTOR_FRAMES_CLOSED_STAGE40_CKM_SHAPE_FAIL__COEFFICIENT_ORIENTATION_NOT_YET_SECTOR_ASSIGNMENT__RHO_BINDING_AND_COEFFICIENT_FREE_HOLONOMIC_ASSIGNMENT_OPEN`.

---

## Appendix Z — NEW 2026-09-19 — Path-local (W_{ij}) location of the remaining family selector

### Z.1 Generic path-holonomy grammar is already current

The current (W_{ij}) crosswalk defines the common transport object

\[
\boxed{
W_{ij}^{(G,R)}
=
\mathcal P\exp\!\left(\int_{\gamma_{ij}}A_R\right).
}
\]

It obeys path reversal

\[
W_{ji}=W_{ij}^{-1}=W_{ij}^\dagger
\]

in unitary representations and local-frame covariance

\[
W_{ij}\mapsto G_iW_{ij}G_j^{-1}.
\]

Status:

`GENERIC_WIJ_PATH_HOLONOMY_GRAMMAR_TYPED_CURRENT`.

### Z.2 Existing explicit sector instances

The source-bound crosswalk currently gives explicit path transports for

```text
White-Thread phase    : W_ij^WT in U(1)
spatial spin frame    : W_ij^X  in SU(2)
colour/gluon sector   : W_ij^c  in SU(3)
```

The word “family” in the title of the generic (W_{ij}) crosswalk denotes a typed family of transport objects. It does not itself provide a flavour-family connection

\[
W_{ij}^{F}\in SU(3)_F.
\]

No explicit current source-bound (W_{ij}^{F}) path transport is present in that crosswalk.

Status:

`OPEN_FAMILY_SPECIFIC_WIJ_PATH_LOCAL_SOURCE_BINDING`.

### Z.3 Why the selector must live upstream of endpoint reduction

The coefficient-cocycle theorem proves that a composition-preserving endpoint map

\[
\Phi:SU(3)\to\mathbb Z^4
\]

must be trivial because (SU(3)) is perfect.

Therefore the nonzero coefficient selector cannot be recovered solely by abelianizing the endpoint holonomy.

A viable family/sector selector must retain additional path-local information before endpoint reduction, such as

```text
path-local cochain
seed/path position
projective pair phase
curvature/path integral
state-dependent transition datum
```

or an equivalent source-derived object.

Status:

`SELECTOR_MUST_RETAIN_PATH_LOCAL_DATA_UPSTREAM_OF_ENDPOINT_SU3_REDUCTION`.

### Z.4 Exact remaining source object

Combining Appendices V–Y with the generic holonomy grammar narrows the missing object to

\[
\boxed{
\text{Collatz/Poincare/IDT source path data}
\longrightarrow
W_{ij}^{F}\text{ or equivalent pair-dependent projective holonomy}
\longrightarrow
\text{Stage-39 sector assignment}
}
\]

with path composition and gauge covariance preserved and without CKM/mass targets on the parent side.

This is precisely upstream of the already-known compact endpoint (SU(3)_F).

Current frontier:

`CUBIC_SELECTOR_CLOSED__SPLIT_REAL_BRANCH_OPERATOR_CLOSED__GEOMETRIC_RHYTHM_ALPHABET_CLOSED__COMPACT_ENDPOINT_FIXED__POLAR_AND_CONTINUOUS_LIE_LIFTS_REFUTED__SCALAR_QC_CP_REFUTED__C3_F3_BARGMANN_FRAMES_CLOSED__STAGE39_STRUCTURAL_SECTOR_FRAMES_CLOSED_STAGE40_CKM_SHAPE_FAIL__COEFFICIENT_ORIENTATION_NOT_YET_SECTOR_ASSIGNMENT__GENERIC_WIJ_GRAMMAR_CLOSED__FAMILY_WIJ_PATH_SOURCE_AND_RHO_BINDING_OPEN`.

---

## Appendix AA — NEW 2026-09-19 — Stage-24 orientation plus Stage-66 stationary selector

### AA.1 Independent parents

Stage 24 fixes the oriented representation-level cycle

\[
s_1\to s_2\to s_3\to s_1.
\]

Stage 66 independently derives the unique negative constrained-Hessian mode of the frozen stationary cubic selector and finds

\[
\boxed{
v_-\parallel P_3A_{seed}P_3^T.
}
\]

The (C_3) orbit of the symmetric seed-incidence direction is

```text
A0 = A_seed                 -> 12 channel
A1 = P3 A_seed P3^T        -> 23 channel
A2 = P3^2 A_seed (P3^T)^2  -> 13 channel
```

so the unique selected stationary tangent is the (23) channel.

### AA.2 Directed representation-level tangent

The Stage-66 tangent itself is symmetric and therefore does not carry an arrow.

Combining it with the independently frozen Stage-24 cycle orientation selects the representation-level directed edge

\[
\boxed{s_2\to s_3.}
\]

Status:

`STAGE24_ORIENTATION_PLUS_STAGE66_SELECTS_DIRECTED_2_TO_3_TANGENT_AT_REPRESENTATION_LEVEL`.

### AA.3 What this closes

This removes another arbitrary choice inside the family carrier:

```text
three C3-related symmetric tangent channels
    -> unique Stage66 negative channel 23

orientation of C3 cycle
    -> Stage24 direction 2 -> 3
```

Neither observed CKM data nor masses enter either parent.

### AA.4 Remaining dynamical gate

This result does not yet identify a Collatz branch symbol with the selected family tangent and does not derive the exact Hamiltonian rhythm \\(\rho_s(k)\\).

Thus the remaining map is

\[
\boxed{
\{E,O\}\text{ branch data}
\longrightarrow
\text{directed family generator / step operator}
\longrightarrow
\rho_s(k)\text{-weighted ordered propagator}.
}
\]

Status:

`OPEN_COLLATZ_BRANCH_TO_DIRECTED_FAMILY_GENERATOR_AND_EXACT_RHO_BINDING`.

The directed (2\to3) tangent is also not an up/down-sector assignment and therefore does not select Stage-39 A versus B.

Current frontier:

`CUBIC_SELECTOR_CLOSED__SPLIT_REAL_BRANCH_OPERATOR_CLOSED__GEOMETRIC_RHYTHM_ALPHABET_CLOSED__COMPACT_ENDPOINT_FIXED__POLAR_AND_CONTINUOUS_LIE_LIFTS_REFUTED__SCALAR_QC_CP_REFUTED__C3_F3_BARGMANN_FRAMES_CLOSED__STAGE39_STRUCTURAL_SECTOR_FRAMES_CLOSED_STAGE40_CKM_SHAPE_FAIL__COEFFICIENT_ORIENTATION_NOT_YET_SECTOR_ASSIGNMENT__GENERIC_WIJ_GRAMMAR_CLOSED__STAGE24_PLUS_STAGE66_DIRECTED_23_TANGENT_CLOSED__COLLATZ_BRANCH_OPERATOR_AND_RHO_BINDING_OPEN`.

---

## Appendix AC — NEW 2026-09-19 — Single-axis branch-map order-loss no-go

Stage 66 selects the symmetric (23) tangent

\[
T_{23}\propto P_3A_{seed}P_3^T.
\]

Suppose both Collatz branch operators were generated only by this one tangent:

\[
U_E=\exp(-iaT_{23}),
\qquad
U_O=\exp(-ibT_{23}).
\]

Because both generators are scalar multiples of the same matrix,

\[
[aT_{23},bT_{23}]=0
\]

and therefore

\[
\boxed{U_EU_O=U_OU_E}.
\]

Any word built from these two operators would depend only on branch counts, not branch order.

By contrast, the exact Stage-49 Collatz Möbius generators satisfy

\[
\boxed{M_EM_O\ne M_OM_E}.
\]

The exact affine translation term retains branch ordering, and the Stage-50 symmetric-square lift likewise remains noncommutative.

Hence a single fixed Stage-66 tangent cannot be the complete branch-symbol-to-family-operator source map.

Status:

`NO_GO_SINGLE_STAGE66_TANGENT_CANNOT_PRESERVE_COLLATZ_BRANCH_ORDER`.

A surviving family branch map therefore requires at least

```text
two noncommuting family generators
or
state/path-dependent conjugation that preserves branch-order information.
```

Status:

`AT_LEAST_TWO_NONCOMMUTING_GENERATORS_OR_STATE_DEPENDENT_CONJUGATION_REQUIRED`.

This no-go does not invalidate the Stage-66 selected tangent; it only prevents using that one axis for both branch generators.

Current frontier:

`CUBIC_SELECTOR_CLOSED__SPLIT_REAL_BRANCH_OPERATOR_CLOSED__GEOMETRIC_RHYTHM_ALPHABET_CLOSED__COMPACT_ENDPOINT_FIXED__POLAR_AND_CONTINUOUS_LIE_LIFTS_REFUTED__SCALAR_QC_CP_REFUTED__C3_F3_BARGMANN_FRAMES_CLOSED__STAGE39_STRUCTURAL_SECTOR_FRAMES_CLOSED_STAGE40_CKM_SHAPE_FAIL__COEFFICIENT_ORIENTATION_NOT_YET_SECTOR_ASSIGNMENT__GENERIC_WIJ_GRAMMAR_CLOSED__STAGE24_PLUS_STAGE66_DIRECTED_23_TANGENT_CLOSED__SINGLE_AXIS_BRANCH_MAP_REFUTED__NONCOMMUTING_BRANCH_OPERATOR_AND_RHO_BINDING_OPEN`.

---

## Appendix AD — NEW 2026-09-19 — Minimal D/C branch map reduces to a Z2 assignment

Stage 42 supplies the source-derived noncommuting Hermitian family pair

\[
D,
\qquad
C=F_3DF_3^\dagger,
\qquad
[D,C]\ne0.
\]

Using the exact branch-length scalars \(\ell_E=\ln2\), \(\ell_O=\ln3\), there are two minimal branch assignments using only this pair:

```text
A: E -> D, O -> C
B: E -> C, O -> D
```

At Lie-generator level,

\[
[\ell_ED,\ell_OC]
=
\ell_E\ell_O[D,C],
\]

while the swapped assignment gives

\[
[\ell_EC,\ell_OD]
=
-\ell_E\ell_O[D,C].
\]

Therefore both assignments retain noncommutativity, but branch swap reverses the commutator orientation.

Status:

`TWO_NONCOMMUTING_DC_ASSIGNMENTS_EXIST_WITH_BRANCH_SWAP_SIGN_REVERSAL`.

The current source graph contains no theorem selecting which Collatz branch owns \(D\) and which owns \(C\). Hence the continuous operator ambiguity has been reduced, at this minimal level, to a discrete branch-swap ambiguity:

\[
\boxed{\mathbb Z_2:\ (E\leftrightarrow O)\text{ against }(D\leftrightarrow C).}
\]

Status:

`OPEN_Z2_EO_TO_DC_ASSIGNMENT_NOT_SOURCE_SELECTED`.

Selecting one assignment from an observed CKM matrix or CP-sign convention would be target leakage and is excluded.

Current frontier:

`CUBIC_SELECTOR_CLOSED__SPLIT_REAL_BRANCH_OPERATOR_CLOSED__GEOMETRIC_RHYTHM_ALPHABET_CLOSED__COMPACT_ENDPOINT_FIXED__POLAR_AND_CONTINUOUS_LIE_LIFTS_REFUTED__SCALAR_QC_CP_REFUTED__C3_F3_BARGMANN_FRAMES_CLOSED__STAGE39_STRUCTURAL_SECTOR_FRAMES_CLOSED_STAGE40_CKM_SHAPE_FAIL__COEFFICIENT_ORIENTATION_NOT_YET_SECTOR_ASSIGNMENT__GENERIC_WIJ_GRAMMAR_CLOSED__STAGE24_PLUS_STAGE66_DIRECTED_23_TANGENT_CLOSED__SINGLE_AXIS_BRANCH_MAP_REFUTED__MINIMAL_DC_NONCOMMUTING_PAIR_CLOSED__EO_TO_DC_Z2_ASSIGNMENT_AND_RHO_PHYSICAL_BINDING_OPEN`.

---

## Appendix AE — NEW 2026-09-19 — Spectral invariants cannot break the E/O to D/C Z2

The two minimal family generators satisfy

\[
C=F_3DF_3^\dagger.
\]

Therefore (D) and (C) are unitarily conjugate and have exactly the same characteristic polynomial and spectrum.

In particular,

\[
\operatorname{tr}(D^n)=\operatorname{tr}(C^n)
\qquad(n=1,2,3),
\]

and

\[
\|D\|_F=\|C\|_F.
\]

Thus no single-generator spectral invariant can distinguish the two branch assignments

```text
A: E -> D, O -> C
B: E -> C, O -> D.
```

Status:

`NO_GO_SINGLE_GENERATOR_SPECTRAL_INVARIANTS_CANNOT_SELECT_EO_TO_DC_Z2`.

The superficial distinction that (D) is diagonal while (C) is character-mixed is not invariant under basis change. Stage 52 explicitly establishes only the availability of a split-real to compact real-form bridge and retains its dynamical selection as OPEN.

Accordingly, diagonal-versus-mixed appearance cannot be used as a source theorem for choosing A over B.

Status:

`DIAGONAL_VS_MIXED_APPEARANCE_NOT_INVARIANT_WITHOUT_DERIVED_REAL_FORM_INTERTWINER`.

The remaining Z2 must therefore be broken, if at all, by a relational invariant involving at least two generators, an oriented commutator/path datum, or a separately derived real-form intertwiner.

Current frontier:

`CUBIC_SELECTOR_CLOSED__SPLIT_REAL_BRANCH_OPERATOR_CLOSED__GEOMETRIC_RHYTHM_ALPHABET_CLOSED__COMPACT_ENDPOINT_FIXED__POLAR_AND_CONTINUOUS_LIE_LIFTS_REFUTED__SCALAR_QC_CP_REFUTED__C3_F3_BARGMANN_FRAMES_CLOSED__STAGE39_STRUCTURAL_SECTOR_FRAMES_CLOSED_STAGE40_CKM_SHAPE_FAIL__COEFFICIENT_ORIENTATION_NOT_YET_SECTOR_ASSIGNMENT__GENERIC_WIJ_GRAMMAR_CLOSED__STAGE24_PLUS_STAGE66_DIRECTED_23_TANGENT_CLOSED__SINGLE_AXIS_BRANCH_MAP_REFUTED__MINIMAL_DC_NONCOMMUTING_PAIR_CLOSED__SPECTRAL_Z2_SELECTION_REFUTED__RELATIONAL_EO_TO_DC_ASSIGNMENT_AND_RHO_PHYSICAL_BINDING_OPEN`.

---

## Appendix AF — NEW 2026-09-19 — Stage-52 spin-one bridge alone cannot generate the D/C family pair

Stage 52 supplies the compact real-form route

\[
\mathfrak{sl}(2,\mathbb R)
\to
\mathfrak{sl}(2,\mathbb C)
\leftarrow
\mathfrak{su}(2)
\xrightarrow{\operatorname{Sym}^2}
\mathfrak k\subset\mathfrak{su}(3)_F,
\]

with \(\mathfrak k\cong\mathfrak{so}(3)\).

Stage 55 gives the compact symmetric-pair decomposition

\[
\mathfrak{su}(3)_F=\mathfrak k\oplus\mathfrak p,
\qquad
\dim\mathfrak k=3,
\quad
\dim\mathfrak p=5.
\]

Using the exact Stage-55 Casimir projectors on the traceless Stage-42 operators \(D_0\) and \(C_0\), the current validator reproduces

\[
\|P_{\mathfrak p}D_0\|_F^2
=
\frac7{135}-\frac{\sqrt5}{45}>0,
\]

and

\[
\|P_{\mathfrak p}C_0\|_F^2
=
\frac{28}{405}+\frac{2\sqrt5}{135}>0.
\]

Thus neither member of the minimal D/C pair lies wholly inside the Stage-52 compact spin-one subgroup.

Status:

`NO_GO_COMPACT_SPIN1_SUBGROUP_ALONE_CANNOT_GENERATE_DC_PAIR`.

The missing branch-to-family map must therefore inject nonzero content into the symmetric-space complement \(\mathfrak p\cong T(SU(3)/SO(3))\), or provide an equivalent mixed \(\mathfrak k\oplus\mathfrak p\) dynamics.

Status:

`OPEN_BRANCH_TO_SU3_OVER_SO3_COMPLEMENT_INJECTION_OR_EQUIVALENT_MIXED_KP_DYNAMICS`.

This is consistent with Stage 53: the compact spin-one subgroup alone has rephasing-invariant \(J=0\), while leaving it is necessary for a nontrivial family CP structure.

The result does not select the remaining E/O to D/C Z2 assignment and does not promote the geometric rhythm candidate to the physical Hamiltonian rhythm.

Current frontier:

`CUBIC_SELECTOR_CLOSED__SPLIT_REAL_BRANCH_OPERATOR_CLOSED__GEOMETRIC_RHYTHM_ALPHABET_CLOSED__COMPACT_ENDPOINT_FIXED__POLAR_AND_CONTINUOUS_LIE_LIFTS_REFUTED__SCALAR_QC_CP_REFUTED__C3_F3_BARGMANN_FRAMES_CLOSED__STAGE39_STRUCTURAL_SECTOR_FRAMES_CLOSED_STAGE40_CKM_SHAPE_FAIL__COEFFICIENT_ORIENTATION_NOT_YET_SECTOR_ASSIGNMENT__GENERIC_WIJ_GRAMMAR_CLOSED__STAGE24_PLUS_STAGE66_DIRECTED_23_TANGENT_CLOSED__SINGLE_AXIS_BRANCH_MAP_REFUTED__MINIMAL_DC_NONCOMMUTING_PAIR_CLOSED__SPECTRAL_Z2_SELECTION_REFUTED__SPIN1_ONLY_DC_GENERATION_REFUTED__BRANCH_TO_COMPLEMENT_INJECTION_EO_Z2_AND_RHO_PHYSICAL_BINDING_OPEN`.

---

## Appendix AG — NEW 2026-09-19 — Stage-66 C3 orbit as a full source-derived SU(3)_F generator set

Stage 66 supplies the frozen orbit

\[
A_0=A_{seed},
\qquad
A_1=P_3A_0P_3^T,
\qquad
A_2=P_3^2A_0(P_3^T)^2.
\]

In the ordered family basis these are the symmetric channels

\[
A_0\sim12,
\qquad
A_1\sim23,
\qquad
A_2\sim13.
\]

### AG.1 Pairwise closure is only three-dimensional

For each pair

\[
(A_0,A_1),\quad(A_1,A_2),\quad(A_2,A_0),
\]

the real Lie closure of the traceless skew-Hermitian generators has dimension

\[
\boxed{3}.
\]

Thus no fixed pair from the orbit alone gives the full family algebra.

### AG.2 The full C3 orbit generates all of su(3)_F

Using all three orbit members gives

\[
\boxed{
\dim_{\mathbb R}\operatorname{Lie}\langle iA_0,iA_1,iA_2\rangle=8
}
\]

and therefore

\[
\boxed{
\operatorname{Lie}\langle iA_0,iA_1,iA_2\rangle
=
\mathfrak{su}(3)_F.
}
\]

Status:

`STAGE66_C3_ORBIT_GENERATES_FULL_SU3F_LIE_ALGEBRA`.

### AG.3 Exact k/p content

Under the Stage-55 symmetric-pair decomposition

\[
\mathfrak{su}(3)_F=\mathfrak k\oplus\mathfrak p,
\]

the three orbit members have exact squared norms

```text
A0: ||Pk A0||^2 = 1/4,  ||Pp A0||^2 = 1/4
A1: ||Pk A1||^2 = 1/4,  ||Pp A1||^2 = 1/4
A2: ||Pk A2||^2 = 0,    ||Pp A2||^2 = 1/2
```

so the orbit already contains explicit nonzero SU(3)/SO(3) complement content, and the forward successor A2 is purely in the complement.

Status:

`CLOSED_AT_STAGE66_C3_ORBIT_GENERATOR_SET_LEVEL__BRANCH_BINDING_OPEN`.

### AG.4 Oriented noncommuting forward pair

Stage 66 selects A1 as the unique negative Hessian mode. Stage 24 supplies the forward C3 orientation, so its successor is A2.

The pair

\[
\boxed{A_1\to A_2}
\]

is noncommuting, with

\[
\|[A_1,A_2]\|_F^2=\frac18.
\]

Since A2 is pure complement while A1 is mixed k/p, this gives a source-derived oriented pair with explicit complement injection.

Status:

`ORIENTED_A1_TO_A2_NONCOMMUTING_PAIR_WITH_EXPLICIT_COMPLEMENT_INJECTION`.

### AG.5 Remaining boundary

This closes the problem of finding a source-derived full family generator set. It does not yet decide which Collatz branch symbol is assigned to which member of the oriented pair.

Remaining:

`OPEN_EO_TO_ORIENTED_STAGE66_GENERATOR_PAIR_ASSIGNMENT`.

The independently frozen Poincare rhythm candidate remains mathematically valid but is not yet promoted to the unique physical Hamiltonian rhythm.

Current frontier:

`CUBIC_SELECTOR_CLOSED__SPLIT_REAL_BRANCH_OPERATOR_CLOSED__GEOMETRIC_RHYTHM_ALPHABET_CLOSED__COMPACT_ENDPOINT_FIXED__POLAR_AND_CONTINUOUS_LIE_LIFTS_REFUTED__SCALAR_QC_CP_REFUTED__C3_F3_BARGMANN_FRAMES_CLOSED__STAGE39_STRUCTURAL_SECTOR_FRAMES_CLOSED_STAGE40_CKM_SHAPE_FAIL__COEFFICIENT_ORIENTATION_NOT_YET_SECTOR_ASSIGNMENT__GENERIC_WIJ_GRAMMAR_CLOSED__STAGE24_PLUS_STAGE66_DIRECTED_23_TANGENT_CLOSED__SINGLE_AXIS_BRANCH_MAP_REFUTED__STAGE66_C3_ORBIT_FULL_SU3F_GENERATOR_SET_CLOSED__ORIENTED_A1_A2_COMPLEMENT_PAIR_CLOSED__EO_TO_ORBIT_PAIR_ASSIGNMENT_AND_RHO_PHYSICAL_BINDING_OPEN`.

---

## Appendix AH — NEW 2026-09-19 — Static two-axis Stage-66 branch map no-go

Appendix AG establishes

\[
\dim\operatorname{Lie}\langle iA_i,iA_j\rangle=3
\]

for every distinct pair of Stage-66 orbit generators, while

\[
\dim\operatorname{Lie}\langle iA_0,iA_1,iA_2\rangle=8.
\]

Therefore any static assignment of the two Collatz branch symbols to only two fixed orbit axes, for example

```text
E -> A1, O -> A2
```

or the swapped assignment, remains confined to a three-dimensional subalgebra.

It cannot reproduce the full source-derived family algebra

\[
\mathfrak{su}(3)_F.
\]

Status:

`STATIC_EO_TO_TWO_STAGE66_ORBIT_GENERATORS_REFUTED`.

### AH.1 Consequence

If the Stage-66 orbit is used as the family-generator source, full family access requires either

```text
state/path-dependent traversal that visits all three A0,A1,A2
or
an independently derived additional generator outside the chosen pair.
```

Status:

`FULL_SU3F_FROM_STAGE66_REQUIRES_ALL_THREE_ORBIT_GENERATORS_OR_EQUIVALENT_EXTRA_DIRECTION`.

### AH.2 Current missing binding

The current repository contains the temporal C3 cycle and the Stage-66 C3 generator orbit, but no current theorem identifies the Collatz step/state index with a specific temporal-C3/orbit index at each step.

Accordingly no rule such as

\[
r_k=k\bmod3
\]

is introduced here.

Remaining gate:

`OPEN_COLLATZ_STATE_OR_PATH_TO_STAGE66_C3_ORBIT_INDEX_BINDING`.

The separately frozen Poincare rhythm remains a validated mathematical candidate, not yet the unique physical Hamiltonian rhythm.

Current frontier:

`CUBIC_SELECTOR_CLOSED__SPLIT_REAL_BRANCH_OPERATOR_CLOSED__GEOMETRIC_RHYTHM_ALPHABET_CLOSED__COMPACT_ENDPOINT_FIXED__POLAR_AND_CONTINUOUS_LIE_LIFTS_REFUTED__SCALAR_QC_CP_REFUTED__C3_F3_BARGMANN_FRAMES_CLOSED__STAGE39_STRUCTURAL_SECTOR_FRAMES_CLOSED_STAGE40_CKM_SHAPE_FAIL__COEFFICIENT_ORIENTATION_NOT_YET_SECTOR_ASSIGNMENT__GENERIC_WIJ_GRAMMAR_CLOSED__STAGE24_PLUS_STAGE66_DIRECTED_23_TANGENT_CLOSED__SINGLE_AXIS_BRANCH_MAP_REFUTED__STAGE66_C3_ORBIT_FULL_SU3F_GENERATOR_SET_CLOSED__STATIC_TWO_AXIS_EO_MAP_REFUTED__STATE_DEPENDENT_ORBIT_INDEX_AND_RHO_PHYSICAL_BINDING_OPEN`.

---

## Appendix AI — NEW 2026-09-19 — Collatz stopping-depth modulo three as an exact temporal-C3 state index

Let

\[
L(n)
\]

be the first-hit stopping depth from the positive integer state \(n\) to \(1\), on the admitted finite-stopping basin.

Define

\[
\boxed{
r_C(n)=(-L(n))\bmod3.
}
\]

### AI.1 Exact one-step equivariance

For every nonterminal state before the first hit of 1,

\[
L(Tn)=L(n)-1.
\]

Hence

\[
r_C(Tn)
=
-(L(n)-1)
=
r_C(n)+1
\pmod3.
\]

For the terminal step \(1\to4\),

\[
L(1)=0,
\qquad
L(4)=2\equiv-1\pmod3,
\]

so the same modular relation holds.

Therefore

\[
\boxed{
r_C(Tn)=r_C(n)+1\pmod3
}
\]

throughout the admitted basin.

Status:

`STOPPING_DEPTH_MOD3_COLLATZ_TO_TEMPORAL_C3_EQUIVARIANT_BINDING_CLOSED`.

### AI.2 Terminal-cycle anchor and qC agreement

The terminal Collatz cycle is

\[
1\to4\to2\to1.
\]

Its stopping depths are

\[
(L(1),L(4),L(2))=(0,2,1),
\]

so

\[
(r_C(1),r_C(4),r_C(2))=(0,1,2).
\]

The exact IDT Collatz-FS phases are

\[
q_C(1)=\frac47,
\qquad
q_C(4)=\frac17,
\qquad
q_C(2)=\frac27.
\]

Under one Collatz step

\[
q_C(Tn)=2q_C(n)\pmod1,
\]

and on the terminal cycle this gives

\[
\frac47\to\frac17\to\frac27\to\frac47.
\]

Thus the stopping-depth C3 index and the IDT terminal phase cycle have the same orientation.

### AI.3 State-dependent Stage-66 generator index

Using the Stage-66 orbit

\[
(A_0,A_1,A_2)
=
(12,23,13)
\]

define the representation-level state-selected generator

\[
\boxed{
G_C(n)=A_{r_C(n)}.
}
\]

Because

\[
A_{r+1}=P_3A_rP_3^T,
\]

one obtains

\[
\boxed{
G_C(Tn)=P_3G_C(n)P_3^T.
}
\]

The current validator checks the stopping-depth relation for every \(1\le n\le10000\), with zero failures, and independently checks the matrix equivariance.

Status:

`CLOSED_REPRESENTATION_LEVEL_VIA_NEGATIVE_STOPPING_DEPTH_MOD3`

`G_N_EQUALS_A_MINUS_L_MOD3_C3_EQUIVARIANT`.

### AI.4 Boundary

This closes the previously open state/path-to-C3-orbit-index problem on the finite-stopping basin.

It does not prove that the temporal C3 carrier is physically identical to the quark-family carrier, and it does not promote the frozen geometric rhythm candidate to the unique physical Hamiltonian rhythm.

Current frontier:

`CUBIC_SELECTOR_CLOSED__SPLIT_REAL_BRANCH_OPERATOR_CLOSED__GEOMETRIC_RHYTHM_ALPHABET_CLOSED__COMPACT_ENDPOINT_FIXED__POLAR_AND_CONTINUOUS_LIE_LIFTS_REFUTED__SCALAR_QC_CP_REFUTED__C3_F3_BARGMANN_FRAMES_CLOSED__STAGE39_STRUCTURAL_SECTOR_FRAMES_CLOSED_STAGE40_CKM_SHAPE_FAIL__COEFFICIENT_ORIENTATION_NOT_YET_SECTOR_ASSIGNMENT__GENERIC_WIJ_GRAMMAR_CLOSED__STAGE24_PLUS_STAGE66_DIRECTED_23_TANGENT_CLOSED__SINGLE_AXIS_BRANCH_MAP_REFUTED__STAGE66_C3_ORBIT_FULL_SU3F_GENERATOR_SET_CLOSED__STATIC_TWO_AXIS_EO_MAP_REFUTED__COLLATZ_STOPPING_DEPTH_MOD3_TO_C3_ORBIT_INDEX_CLOSED__RHO_PHYSICAL_AND_TEMPORAL_FAMILY_PROMOTION_OPEN`.

---

## Appendix AJ — NEW 2026-09-19 — Freeze of the state-dependent signed-geometric SU(3) step candidate

Status: `STATE_DEPENDENT_SIGNED_GEOMETRIC_SU3_STEP_CANDIDATE_FROZEN_PREVALIDATION`.

Freeze date: `2026-09-19`.

### AJ.1 Frozen parent objects

The candidate uses only already-admitted source objects:

```text
Collatz branch symbol b(n) in {E,O}
stopping-depth C3 index r_C(n)=(-L(n)) mod 3
Stage-66 orbit generators A0,A1,A2
exact Poincare branch lengths rho_E=ln2, rho_O=ln3
exact signed log-Jacobian orientation chi_E=-1, chi_O=+1
```

No observed CKM, PMNS, mass, PDG, or fitted coefficient enters the definition.

### AJ.2 Frozen signed generator

For a state n on the admitted finite-stopping basin, define

\[
\boxed{
K_{geo}(n)
=
\chi_{b(n)}\rho_{geo}(b(n))A_{r_C(n)}
=
\sigma_{b(n)}A_{r_C(n)}.
}
\]

Explicitly,

\[
\sigma_E=-\ln2,
\qquad
\sigma_O=+\ln3.
\]

The branch symbol therefore controls the exact signed geometric scalar, while the Collatz state controls the C3-orbit generator index.

No static map

\[
E\to A_i,\qquad O\to A_j
\]

is introduced.

### AJ.3 Frozen unitary step candidate

Define

\[
\boxed{
U_{geo}(n)=\exp[-iK_{geo}(n)].
}
\]

Because each A_r is Hermitian and traceless and each sigma_b is real, the candidate is typed to lie in SU(3).

### AJ.4 Prospective validation gates

After this freeze, and before any target comparison, validate:

1. Hermiticity and tracelessness of every K_geo branch/frame combination.
2. Unitarity and determinant one of every U_geo branch/frame combination.
3. C3 covariance of the state-selected axis.
4. Order sensitivity for distinct branch words with equal branch counts.
5. Full eight-dimensional Lie accessibility over every three consecutive C3 axes.
6. No dependence on observed CKM, PMNS, masses, or fitted coefficients.

### AJ.5 Promotion boundary

This freeze does not claim

```text
physical Hamiltonian = K_geo
physical rho_s = rho_geo
physical CKM/PMNS = product of U_geo
temporal C3 = physical flavour C3
```

Those remain separate physical-binding gates.

The candidate is frozen solely as the minimal parameter-free state-dependent operator scaffold compatible with the current exact mathematical parents.

---

## Appendix AK — NEW 2026-09-19 — Hosted validation of the signed-geometric state-dependent SU(3) step

### AK.1 Validation provenance

The Appendix-AJ candidate was frozen before validation. It has now been tested on the exact GitHub Actions checkout

`46e1ed199a5467d114877e41202cdd94f983a3eb`

with workflow

`TIR IDT mod6pi C3 Pauli crosswalk`

run `#193`, run id `35443884068`, job id `105899384839`.

The hosted job conclusion is `success`.

Status:

`PASS_MATH_PROVENANCE__PHYSICAL_PROMOTION_OPEN`.

### AK.2 Algebraic type checks

For every branch/frame combination

\[
K_{geo}(n)=\sigma_{b(n)}A_{(-L(n))\bmod3}
\]

the hosted validator obtains

```text
Hermiticity residual = 0
trace residual       = 0
```

and for

\[
U_{geo}(n)=e^{-iK_{geo}(n)}
\]

it obtains

```text
max unitarity residual   = 3.3306690738754696e-16
max determinant residual = 3.3388414414438688e-16
```

so every frozen step is an (SU(3))-typed matrix to floating-point tolerance.

Status:

`SOURCE_DERIVED_PARAMETER_FREE_SU3_STEP_SCAFFOLD_VALIDATED`.

### AK.3 Ordered branch sensitivity

The state-dependent rotating (C_3) axis prevents the equal-count words `EO` and `OE` from collapsing to the same step product.

For all three starting (C_3) indices the hosted separation is

\[
\boxed{
\|U_{EO}-U_{OE}\|_{\max}
=
0.8617726992906661.
}
\]

Thus exact branch order survives even though `EO` and `OE` contain the same number of odd and even steps.

Status:

`EQUAL_COUNT_EO_OE_ORDER_DISTINGUISHED_ON_ROTATING_C3_AXES`.

### AK.4 Three-step Lie accessibility

For every starting (C_3) frame (r=0,1,2) and every three-step branch word

```text
EEE EEO EOE EOO OEE OEO OOE OOO
```

the three selected Stage-66 orbit generators have

\[
\boxed{\dim_{\mathbb R}\operatorname{Lie}=8}
\]

with reported Lie-closure residual `0.0` in all (3\times8=24) cases.

Hence every three consecutive state-selected axes has access to the full family algebra

\[
\boxed{\mathfrak{su}(3)_F.}
\]

Status:

`EVERY_THREE_CONSECUTIVE_C3_AXES_LIE_GENERATE_SU3F`.

### AK.5 Provenance result

The validated scaffold uses only

```text
Collatz parity branch E/O
exact stopping-depth mod-3 state index
Stage-66 C3 orbit generators
ln(2), ln(3) from exact Poincare branch lengths
signed log-Jacobian branch orientation
```

and the hosted receipt reports

```text
uses observed CKM          = false
uses observed PMNS         = false
uses observed masses       = false
uses fitted coefficients   = false
```

### AK.6 Promotion boundary

The validation closes the mathematical scaffold. It does not establish

```text
physical Hamiltonian = K_geo
physical rho_s(k) = signed geometric branch scale
temporal C3 = physical flavour-generation dynamics
physical CKM/PMNS = ordered product of U_geo
```

Those remain separate physical-binding gates.

Status:

`NOT_PROMOTED_PHYSICAL_HAMILTONIAN_BINDING_OPEN`.

Current frontier:

`SIGNED_GEOMETRIC_SU3_STEP_CANDIDATE_VALIDATED__PHYSICAL_RHO_TEMPORAL_FAMILY_AND_CKM_PROMOTION_OPEN`.

---

## Appendix AL — NEW 2026-09-19 — Hosted validation of the Collatz–Poincare branch-rhythm candidate

### AL.1 Frozen candidate

The separately frozen branch-local positive rhythm candidate is

\[
\boxed{
\rho_{geo}(b)
=
\begin{cases}
\ln2,&b=E,\\
\ln3,&b=O.
\end{cases}
}
\]

with signed companion

\[
\sigma_E=-\ln2,
\qquad
\sigma_O=+\ln3.
\]

The freeze predates validation and excludes CKM, PMNS, fermion masses, fitted White-Thread values, the historical `eta=0.35`, and retrospective target tuning.

### AL.2 Hosted validation

The candidate passed the hosted workflow

`TIR Collatz Poincare branch rhythm v0.1`

on the same validated branch state used by the AJ hosted audit.

Hosted result:

`PASS_CANDIDATE_MATHEMATICAL_AND_PROVENANCE_VALIDATION__PHYSICAL_RHYTHM_NOT_PROMOTED`.

The exact recomputation gives

\[
\rho_E=0.6931471805599453=\ln2,
\]

\[
\rho_O=1.0986122886681098=\ln3.
\]

The Stage-48 frozen words accumulate additively:

\[
R_{geo}(\texttt{OEOE})
=2\ln2+2\ln3
=\ln36,
\]

and for the 90-step third-seed word

\[
R_{geo}(w_3)=56\ln2+34\ln3.
\]

Status:

`COLLATZ_POINCARE_BRANCH_RHYTHM_CANDIDATE_MATH_PROVENANCE_PASS`.

### AL.3 Exact boundary

The hosted receipt explicitly keeps

```text
physical_rhythm_promoted      = false
branch_to_family_operator     = OPEN
```

Therefore the old broad phrase `exact rho_s(k) open` must now be split into two statements:

```text
source-derived positive branch-local rhythm candidate
    = VALIDATED

uniqueness as the physical Hamiltonian rhythm
    = OPEN

physical Hamiltonian identification rho_s = rho_geo
    = OPEN
```

Status:

`BRANCH_LOCAL_GEOMETRIC_RHYTHM_VALIDATED__PHYSICAL_UNIQUENESS_AND_HAMILTONIAN_BINDING_OPEN`.

---

## Appendix AM — NEW 2026-09-19 — Freeze of the common-target family path-holonomy candidate

Status: `COMMON_TARGET_FAMILY_PATH_HOLONOMY_CANDIDATE_FROZEN_PREVALIDATION`.

Freeze date: `2026-09-19`.

### AM.1 Frozen parent objects

The candidate uses only already-frozen objects:

```text
Stage-47 scalar seeds: n1=15, n2=35, n3=143
Stage-47 unique common forward-reachable seed: n*=35
Stage-48 exact branch words w1=OEOE, w2=epsilon, w3=(90-step frozen word)
Appendix-AI state index r_C(n)=(-L(n)) mod 3
Appendix-AJ validated step U_geo(n)=exp[-i sigma_b A_r]
```

No CKM, PMNS, fermion mass, fitted coefficient, or target matrix enters this freeze.

### AM.2 Ordered path propagators

For seed (n_i), let

\[
n_i=n_{i,0}\to n_{i,1}\to\cdots\to n_{i,m_i}=35
\]

be its exact Stage-48 Collatz path, with branch symbols (b_{i,k}\).

Define the ordered propagator from the seed to the common target by

\[
\boxed{
G_i
=
U_{geo}(n_{i,m_i-1})\cdots U_{geo}(n_{i,1})U_{geo}(n_{i,0}).
}
\]

The later Collatz step multiplies on the left, matching the existing ordered-propagator convention.

For the middle seed, the path is empty and

\[
\boxed{G_2=I_3.}
\]

### AM.3 Pairwise family transport candidate

Use the generic (W_{ij}) convention in which (W_{ij}) maps the (j)-frame into the (i)-frame. Define

\[
\boxed{
W^F_{ij}=G_i^\dagger G_j.
}
\]

This is a source-derived candidate family transport built from path-local Collatz state data rather than endpoint fitting.

### AM.4 Prospective validation gates

After this freeze, validate without changing the construction:

1. Every (G_i\in SU(3)).
2. Every (W^F_{ij}\in SU(3)).
3. Reversal: (W^F_{ji}=(W^F_{ij})^\dagger).
4. Composition: (W^F_{ij}W^F_{jk}=W^F_{ik}).
5. The triangular Wilson product (W^F_{12}W^F_{23}W^F_{31}).
6. Whether the common-target construction is flat/pure-gauge or carries nontrivial loop holonomy.
7. No target data or fitted coefficient enters the result.

### AM.5 Promotion boundary

If the triangular Wilson product is identity, the result will be retained as a flat groupoid/path-frame scaffold and will **not** be promoted as a CP source.

If it is nontrivial, its gauge-invariant content will be recorded before any CKM/PMNS comparison.

This freeze does not claim

```text
W^F_ij = physical flavour connection
common target 35 = physical preferred generation
path propagators = physical CKM/PMNS
flatness or non-flatness in advance
```

Status remains:

`COMMON_TARGET_FAMILY_PATH_HOLONOMY_CANDIDATE_FROZEN_PREVALIDATION`.

---

## Appendix AN — NEW 2026-09-19 — Hosted validation of the common-target family (W^F_{ij}) scaffold

### AN.1 Hosted provenance

The Appendix-AM candidate has passed the exact-head hosted crosswalk gate.

```text
validated head : f930361fe52cd899c8bba12ece67ea160e017413
workflow       : TIR IDT mod6pi C3 Pauli crosswalk
run            : #205 / 35446617955
job            : 105906536985
conclusion     : success
```

Status:

`PASS_SU3_GROUPOID_FLAT_PURE_GAUGE`.

### AN.2 Exact source paths

The hosted replay uses

```text
15  -> 35 : OEOE, 4 steps
35  -> 35 : empty word, 0 steps
143 -> 35 : frozen 90-step Stage-48 word
```

with starting (C_3) frame indices

```text
15  : 1
35  : 2
143 : 2
```

and common target frame `2`.

### AN.3 Path propagators and pairwise transports

For

\[
G_i=\overleftarrow{\prod}U_{geo}(n_{i,k}),
\qquad
W^F_{ij}=G_i^\dagger G_j,
\]

the hosted residuals are

```text
path unitarity residual     = 2.0206066545682744e-14
path determinant residual   = 3.033368243768708e-14
W_ij unitarity residual     = 4.04121180963557e-14
W_ij determinant residual   = 6.028513077328184e-14
W_ij reversal residual      = 5.551115123125783e-17
W_ij composition residual   = 2.0206123459202648e-14
```

Thus the candidate closes an (SU(3))-typed pairwise transport groupoid to floating-point tolerance.

Status:

`SOURCE_DERIVED_COMMON_TARGET_FAMILY_WIJ_SCAFFOLD_CLOSED`.

### AN.4 Non-Abelian edges but flat loop

The transport is not trivial:

\[
\max\|W^F_{ij}-I\|
=
1.521891036749805,
\]

and representative edge transports do not commute:

\[
\max\|[W^F_{12},W^F_{23}]\|
=
0.8527092175626987.
\]

Nevertheless the triangular Wilson loop closes to identity:

\[
\boxed{
W^F_{12}W^F_{23}W^F_{31}=I
}
\]

with residual

\[
2.1094300329942488\times10^{-14},
\]

and the reverse orientation gives

\[
2.1094257466330393\times10^{-14}.
\]

Therefore the common-target construction is a non-Abelian but flat frame coboundary:

`FLAT_PURE_GAUGE_COMMON_TARGET_GROUPOID`.

### AN.5 Consequence

The source-derived family (W^F_{ij}) scaffold is no longer absent. What remains open is a **non-flat** physical family connection.

A common-target coboundary alone cannot source a nonzero gauge-invariant loop phase or CP curvature.

Status:

`TRIANGULAR_WILSON_LOOP_IDENTITY`

`NO_GO_COMMON_TARGET_COBoundARY_TRANSPORT_ALONE_CANNOT_SOURCE_NONZERO_LOOP_HOLONOMY`

`OPEN_NONFLAT_PATH_DEPENDENT_EXTENSION_OR_ADDITIONAL_CONNECTION`.

Current family-source status:

`COMMON_TARGET_FAMILY_WIJ_SCAFFOLD_SOURCE_DERIVED_FLAT__NONFLAT_PHYSICAL_CONNECTION_OPEN`.

---

## Appendix AO — NEW 2026-09-19 — Retrospective structural candidate: terminal Collatz-cycle SU(3) holonomy

Status: `RETROSPECTIVE_STRUCTURAL_CANDIDATE_NOT_PROSPECTIVE_TEST`.

### AO.1 Provenance disclosure

The nontriviality of the loop below was observed in an exploratory dry-run before this Appendix was formalized.

Accordingly this is **not** classified as a blind/prospective validation freeze.

No CKM, PMNS, fermion mass, PDG value, fitted coefficient, or target matrix was used in the exploratory calculation or in the definition below.

### AO.2 Exact closed Collatz cycle

The standard terminal Collatz cycle is

\[
\boxed{1\to4\to2\to1}.
\]

Under the already validated stopping-depth state index

\[
r_C(n)=(-L(n))\bmod3,
\]

the three states carry

\[
r_C(1)=0,
\qquad
r_C(4)=1,
\qquad
r_C(2)=2.
\]

The branch sequence is

\[
\boxed{O,E,E}.
\]

### AO.3 AJ loop candidate

Using the validated Appendix-AJ step

\[
U_{geo}(n)=\exp[-i\,\sigma_{b(n)}A_{r_C(n)}],
\]

with

\[
\sigma_O=+\ln3,
\qquad
\sigma_E=-\ln2,
\]

define the ordered terminal-cycle loop

\[
\boxed{
U_\circ
=
U_E(A_2)\,U_E(A_1)\,U_O(A_0).
}
\]

Later Collatz steps multiply on the left, consistently with Appendix AJ/AM.

### AO.4 Exact analytic nontriviality witness

Let

\[
a=\ln3,
\qquad
b=\ln2.
\]

Because each (A_r) is the symmetric half-strength generator of one coordinate two-plane, the loop trace reduces exactly to

\[
\boxed{
\operatorname{tr}U_\circ
=
2\cos\frac a2\cos\frac b2
+\cos^2\frac b2
+i\sin\frac a2\sin^2\frac b2.
}
\]

The imaginary part is

\[
\boxed{
\operatorname{Im}\operatorname{tr}U_\circ
=
\sin\frac{\ln3}{2}
\sin^2\frac{\ln2}{2}
>0.
}
\]

Therefore

\[
\boxed{U_\circ\neq I_3}
\]

without reference to any physical target.

### AO.5 Retrospective numerical checkpoint

The exploratory dry-run gave

```text
max |U_circle - I|  = 0.5008161081115994
tr(U_circle)        = 2.4889716929998738 + 0.06023967414631505 i
det(U_circle)       ≈ 1
eigenphases         ≈ (-0.82849754, 0.55400195, 0.27449558)
```

These values are recorded only as a retrospective checkpoint to be independently reproduced by the repository validator.

### AO.6 Validation gates

The current validator should now independently verify:

1. the exact cycle states, frames and branch word `OEE`;
2. (U_\circ\in SU(3));
3. (U_\circ\neq I);
4. the analytic trace formula above;
5. the strictly nonzero imaginary trace witness;
6. gauge-conjugacy invariance of trace/eigenvalues;
7. no physical-target input;
8. no promotion to CKM/PMNS or physical CP merely from nontrivial loop holonomy.

### AO.7 Scope boundary

A nontrivial (SU(3)) Wilson loop is a non-flat source-derived holonomy candidate.

It is **not** by itself a derivation of a Jarlskog invariant, CKM matrix, PMNS matrix, or physical CP violation.

Physical sector binding remains OPEN.

Status:

`TERMINAL_COLLATZ_CYCLE_NONTRIVIAL_SU3_HOLONOMY_RETROSPECTIVE_CANDIDATE`.

---

## Appendix AP — NEW 2026-09-19 — Hosted validation of the terminal Collatz-cycle SU(3) holonomy

### AP.1 Hosted provenance

The retrospective Appendix-AO structural candidate has passed the exact-head hosted crosswalk gate.

```text
validated head : 65ce0d93fb0358eb709fbdc7904c51e5f7665509
workflow       : TIR IDT mod6pi C3 Pauli crosswalk
run            : #213 / 35446942861
job            : 105907392990
conclusion     : success
```

The evidential class remains

`RETROSPECTIVE_STRUCTURAL_CANDIDATE_NOT_PROSPECTIVE_TEST`.

### AP.2 Exact loop data

The hosted validator independently reproduces

```text
states      = [1, 4, 2]
next states = [4, 2, 1]
branches    = [O, E, E]
frames      = [0, 1, 2]
```

and

\[
U_\circ=U_E(A_2)U_E(A_1)U_O(A_0).
\]

### AP.3 SU(3) and nontriviality

The hosted residuals are

```text
unitarity residual   = 6.661338147750939e-16
determinant residual = 9.994535692500799e-16
max |U_circle-I|     = 0.5008161081115994
```

so the loop is a nonidentity (SU(3))-typed holonomy.

Status:

`TERMINAL_COLLATZ_CYCLE_NONTRIVIAL_SU3_HOLONOMY_RETROSPECTIVE_STRUCTURAL_PASS`.

### AP.4 Analytic trace witness

The validator reproduces

\[
\boxed{
\operatorname{tr}U_\circ
=
2\cos\frac{\ln3}{2}\cos\frac{\ln2}{2}
+\cos^2\frac{\ln2}{2}
+i\sin\frac{\ln3}{2}\sin^2\frac{\ln2}{2}
}
\]

with

```text
trace real             = 2.4889716929998738
trace imaginary        = 0.06023967414631505
trace formula residual = 8.884223316973178e-16
imaginary residual     = 2.0816681711721685e-17
```

and therefore a strictly nonzero imaginary conjugacy-class witness.

### AP.5 Eigenphases and gauge-conjugacy audit

The hosted eigenphases are

\[
(-0.8284975357488279,
\ 0.2744955841537181,
\ 0.5540019515951093).
\]

After conjugation by the exact (F_3) basis transform, the invariant residuals are

```text
trace residual          = 4.518280359883027e-16
trace(U^2) residual     = 8.326672684688674e-16
determinant residual    = 5.592276282644142e-16
characteristic residual = 3.722145839155691e-15
```

confirming that the nontriviality is a conjugacy-class property, not a basis artifact.

### AP.6 Structural consequence

The common-target construction of Appendix AN is flat because it is a frame coboundary.

The actual directed terminal Collatz cycle is different: it is a genuine closed source loop and the validated AJ connection assigns it a nonidentity (SU(3)) holonomy.

Thus a source-derived non-flat loop candidate now exists.

Status:

`TERMINAL_CYCLE_SUPPLIES_NONFLAT_SOURCE_DERIVED_LOOP_CANDIDATE`.

### AP.7 Physical firewall

A nontrivial Wilson loop is not automatically physical CP violation.

No physical sector identification, CKM/PMNS matrix, Jarlskog invariant, or mass relation is promoted by this result.

Status:

`NONTRIVIAL_WILSON_LOOP_NOT_YET_PHYSICAL_CP_OR_SECTOR_BINDING`.

The remaining gate is the physical interpretation/binding of this source-derived non-flat holonomy.

---

## Appendix AQ — NEW 2026-09-19 — Terminal Collatz holonomy lies outside every conjugate spin-one \(SU(2)\) subgroup

### AQ.1 Spin-one character constraint

For the irreducible spin-one representation of \(SU(2)\), every group element has eigenvalues

\[
\{e^{i\theta},1,e^{-i\theta}\}.
\]

Hence its character is

\[
\boxed{\chi_1(\theta)=1+2\cos\theta\in\mathbb R.}
\]

In particular every element of any conjugate spin-one subgroup

\[
g\,SU(2)_{j=1}\,g^{-1}\subset SU(3)
\]

has real trace and an eigenvalue equal to \(1\). Both properties are invariant under conjugation.

### AQ.2 Terminal-loop witnesses

Appendix AP gives the exact terminal Collatz-cycle holonomy

\[
U_\circ=U_E(A_2)U_E(A_1)U_O(A_0)\in SU(3)
\]

for

\[
1\to4\to2\to1.
\]

The hosted validator obtains

\[
\operatorname{Im}\operatorname{tr}U_\circ
=
0.06023967414631505
\neq0.
\]

It also verifies

\[
\boxed{\det(U_\circ-I_3)\neq0,}
\]

so \(1\) is not an eigenvalue of the terminal-loop holonomy.

Either invariant is already sufficient to exclude membership in the spin-one subgroup; together they provide independent conjugacy witnesses.

### AQ.3 Exact subgroup exclusion

Therefore

\[
\boxed{
U_\circ
\notin
g\,SU(2)_{j=1}\,g^{-1}
\quad
\text{for every }g\in SU(3).
}
\]

Status:

`TERMINAL_LOOP_OUTSIDE_EVERY_CONJUGATE_SPIN1_SU2_SUBGROUP`.

Equivalently, the terminal Collatz loop requires group directions beyond the compact spin-one subgroup singled out in Stage 53.

Status:

`TERMINAL_LOOP_REQUIRES_DIRECTIONS_BEYOND_COMPACT_SPIN1_SUBGROUP`.

### AQ.4 Relation to the \(3\oplus5\) decomposition

Stage 53 gives

\[
\mathfrak{su}(3)
\cong
\mathbf3\oplus\mathbf5
\]

under the embedded spin-one \(SU(2)\).

The terminal-loop subgroup exclusion shows that the validated state-dependent Collatz construction is not confined to the compact \(\mathbf3\) subgroup at group level.

This is consistent with the independent Stage-66 result that the full orbit generates all eight real directions of \(\mathfrak{su}(3)_F\).

### AQ.5 Physical firewall

A non-real trace is a conjugacy/subgroup witness here. It is not itself identified with a physical CP-odd observable.

The result does not establish

```text
terminal loop = CKM holonomy
terminal loop = PMNS holonomy
Im tr(U_circle) = physical CP phase
temporal C3 = physical flavour dynamics
```

Those bindings remain OPEN.

Current frontier:

`TERMINAL_COLLATZ_CYCLE_NONFLAT_SU3_LOOP_OUTSIDE_SPIN1_RETROSPECTIVE_PASS__PHYSICAL_RHO_TEMPORAL_FAMILY_CP_AND_CKM_PROMOTION_OPEN`.

---

## Appendix AR — NEW 2026-09-19 — Basepoint covariance and orientation-odd terminal-loop class invariant

### AR.1 Three basepoints on the same terminal cycle

For the exact Collatz cycle

\[
1\xrightarrow{O}4\xrightarrow{E}2\xrightarrow{E}1,
\]

write the validated step matrices as

\[
U_{1\to4},\qquad U_{4\to2},\qquad U_{2\to1}.
\]

The loop based at 1 is

\[
U_1=U_{2\to1}U_{4\to2}U_{1\to4}.
\]

The same oriented loop based at 4 and 2 is

\[
U_4=U_{1\to4}U_{2\to1}U_{4\to2},
\]

\[
U_2=U_{4\to2}U_{1\to4}U_{2\to1}.
\]

These obey

\[
\boxed{U_4=U_{1\to4}U_1U_{1\to4}^{-1}}
\]

and

\[
\boxed{U_2=U_{1\to2}U_1U_{1\to2}^{-1}},
\qquad
U_{1\to2}=U_{4\to2}U_{1\to4}.
\]

Therefore trace, characteristic polynomial, eigenvalues and every conjugacy-class observable are independent of the chosen basepoint on the terminal cycle.

Status:

`TERMINAL_LOOP_CONJUGACY_CLASS_BASEPOINT_COVARIANT`.

### AR.2 Orientation reversal

Traversing the same loop in reverse gives

\[
\boxed{U_{\circ^{-1}}=U_\circ^{-1}=U_\circ^\dagger.}
\]

Hence

\[
\operatorname{tr}(U_{\circ^{-1}})
=
\operatorname{tr}(U_\circ)^*.
\]

Therefore

\[
\operatorname{Re}\operatorname{tr}(U_{\circ^{-1}})
=
\operatorname{Re}\operatorname{tr}(U_\circ),
\]

while

\[
\boxed{
\operatorname{Im}\operatorname{tr}(U_{\circ^{-1}})
=
-\operatorname{Im}\operatorname{tr}(U_\circ).
}
\]

For the validated terminal loop, the forward value is nonzero, so the imaginary trace is a strictly orientation-odd conjugacy-class witness.

Status:

`TERMINAL_LOOP_IMAGINARY_TRACE_ORIENTATION_ODD_CLASS_WITNESS`.

### AR.3 Combined structural meaning

Appendix AQ established that the terminal loop lies outside every conjugate compact spin-one \(SU(2)\) subgroup.

Appendix AR adds that this nontrivial conjugacy class is basepoint-covariant and carries an orientation-odd imaginary-trace invariant.

Thus the source-derived terminal Collatz loop has a genuine non-Abelian, orientation-sensitive \(SU(3)\) conjugacy class.

### AR.4 Physical firewall

The orientation-odd quantity

\[
\operatorname{Im}\operatorname{tr}U_\circ
\]

is used here only as a Wilson-loop conjugacy invariant.

It is not identified with the CKM Jarlskog invariant, a CP phase, or any measured flavour observable.

Status remains:

`NONTRIVIAL_WILSON_LOOP_NOT_YET_PHYSICAL_CP_OR_SECTOR_BINDING`.

---

## Appendix AS — NEW 2026-09-19 — Terminal Collatz holonomy is non-coboundary and path-nonseparable

### AS.1 Flat endpoint-frame factorization theorem

If pairwise transports on a connected three-vertex system have the endpoint-only form

\[
\boxed{W_{ij}=G_i^\dagger G_j,}
\]

then the triangular Wilson product telescopes:

\[
W_{12}W_{23}W_{31}
=
G_1^\dagger G_2G_2^\dagger G_3G_3^\dagger G_1
=
I.
\]

Therefore every globally factorized endpoint-frame/coboundary transport is flat on the triangle.

Appendix AN verifies exactly this situation for the common-target scaffold.

### AS.2 Terminal Collatz loop violates the coboundary identity

For the terminal Collatz cycle

\[
1\to4\to2\to1,
\]

Appendices AP–AR give the source-derived loop

\[
U_\circ=U_E(A_2)U_E(A_1)U_O(A_0),
\]

with

\[
\boxed{U_\circ\neq I.}
\]

Thus no globally defined endpoint frames \(G_1,G_4,G_2\) can satisfy all three terminal edge transports simultaneously as

\[
W_{ij}=G_i^\dagger G_j.
\]

Status:

`NONTRIVIAL_TERMINAL_WILSON_LOOP_REFUTES_GLOBAL_GI_DAGGER_GJ_FACTORIZATION`.

### AS.3 Nonseparable path source

The terminal edge data therefore contains path information that cannot be reduced to a difference of endpoint frames.

Equivalently, it is a genuinely non-coboundary/path-nonseparable holonomy candidate.

Status:

`SOURCE_DERIVED_NONSEPARABLE_PATH_HOLONOMY_CANDIDATE_EXISTS`.

This is exactly the structural class required by the earlier scalar-phase no-go: a nonzero loop phase/holonomy cannot arise from separable vertex phases or endpoint-only coboundaries.

### AS.4 Flat versus nonflat source structures

The current branch now contains both:

```text
common-target W_ij scaffold
    = exact SU(3) groupoid
    = flat / pure gauge

terminal Collatz-cycle transport
    = exact SU(3) loop candidate
    = nonflat / non-coboundary
    = outside compact spin-one subgroup
    = orientation-sensitive
```

This distinction is source-derived and does not require CKM, PMNS, masses, or fitted coefficients.

### AS.5 Promotion boundary

The existence of a nonseparable source holonomy candidate closes the old structural question

\[
\text{“can the Collatz/Poincare-side construction produce path-local non-coboundary }SU(3)\text{ data?”}
\]

at candidate level.

It does not establish that this terminal-cycle loop is the physical family connection.

Current status:

`SOURCE_DERIVED_STATE_DEPENDENT_NONSEPARABLE_SU3_HOLONOMY_MAP_CANDIDATE_EXISTS__PHYSICAL_FAMILY_CP_BINDING_OPEN`.
