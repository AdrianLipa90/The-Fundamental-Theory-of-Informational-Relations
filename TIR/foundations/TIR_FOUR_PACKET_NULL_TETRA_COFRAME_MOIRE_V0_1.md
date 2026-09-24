# TIR Four-Packet Null-Tetra Coframe Moire Bridge v0.1

Status: CANDIDATE_FOUNDATIONAL_BRIDGE / EXACT_LOCAL_COFRAME_PARAMETERIZATION / PHYSICAL_CLOCK_AND_DYNAMICS_OPEN
Date: 2026-09-24

## 1. Purpose

This bridge removes the remaining need to interpret an anonymous legacy PhaseNav 36-vector as a gravitational source.

The existing TIR x IDT lift already maps one positive elapsed binary-state packet

\[
(\ell,\rho)
\]

to a four-real-coordinate Hermitian carrier

\[
X=\ell\rho
=
x^0I+x^1\sigma_x+x^2\sigma_y+x^3\sigma_z,
\]

with

\[
x^0=\frac{\ell}{2},
\qquad
x^i=\frac{\ell}{2}r_i.
\]

This file takes **four** independently admissible packets and uses them directly as the four columns of a local coframe candidate.

## 2. Four-packet frame

For packets

\[
(\ell_a,\mathbf r_a),
\qquad
a=0,1,2,3,
\]

define

\[
x_a
=
\frac{\ell_a}{2}
\begin{pmatrix}
1\\
\mathbf r_a
\end{pmatrix},
\]

and

\[
\boxed{
E=[x_0\;x_1\;x_2\;x_3].
}
\]

Whenever

\[
\det E\neq0,
\]

the four packets form a local frame/coframe matrix.

No choice of four coordinates from a 36-vector is involved.

## 3. Exact local rank 16

For one packet, the already-proved map

\[
F:(\ell,r_x,r_y,r_z)\mapsto(x^0,x^1,x^2,x^3)
\]

has Jacobian determinant

\[
\det J_F=\frac{\ell^3}{16}.
\]

For four independently parameterized packets the total parameter-to-matrix map is block diagonal in the packet coordinates. Therefore

\[
\boxed{
\det J_{F^{\times4}}
=
\prod_{a=0}^{3}\frac{\ell_a^3}{16}
=
\frac{(\ell_0\ell_1\ell_2\ell_3)^3}{16^4}.
}
\]

For every \(\ell_a>0\),

\[
\boxed{
\operatorname{rank}J_{F^{\times4}}=16.
}
\]

Thus the four-packet construction supplies all 16 local real matrix coordinates on its admitted open domain. The additional coframe condition \(\det E\neq0\) selects an open subset.

This is a local parameterization theorem. It does not by itself identify the packets with physical spacetime events.

## 4. Canonical tetrahedral null seed

Use the regular tetrahedral Bloch directions

\[
\mathbf n_0=\frac1{\sqrt3}(1,1,1),
\quad
\mathbf n_1=\frac1{\sqrt3}(1,-1,-1),
\]

\[
\mathbf n_2=\frac1{\sqrt3}(-1,1,-1),
\quad
\mathbf n_3=\frac1{\sqrt3}(-1,-1,1).
\]

For equal elapsed scale \(\ell>0\), each pure packet

\[
x_a=\frac{\ell}{2}(1,\mathbf n_a)
\]

is null with respect to the standard Minkowski quadratic form,

\[
(x_a^0)^2-|\mathbf x_a|^2=0.
\]

The frame determinant is

\[
\boxed{
\det E_{tet}
=
-\frac{\sqrt3}{9}\ell^4
\neq0.
}
\]

Therefore four future-null tetrahedral packets span the full four-dimensional carrier.

Their Minkowski Gram matrix is

\[
\boxed{
(E_{tet})^T\eta E_{tet}
=
\frac{\ell^2}{3}
\begin{pmatrix}
0&1&1&1\\
1&0&1&1\\
1&1&0&1\\
1&1&1&0
\end{pmatrix}.
}
\]

So the regular tetrahedral SIC boundary is not rank-deficient as a four-vector frame.

## 5. Exact rational Hadamard form

Rescale the spatial coordinates by \(\sqrt3\) and ignore the common positive scalar. The tetrahedral null frame becomes

\[
\boxed{
H_4=
\begin{pmatrix}
1&1&1&1\\
1&1&-1&-1\\
1&-1&1&-1\\
1&-1&-1&1
\end{pmatrix}.
}
\]

It obeys

\[
\boxed{
H_4^2=4I,
\qquad
H_4^{-1}=\frac14H_4,
\qquad
\det H_4=-16.
}
\]

With the equivalent rescaled Lorentz metric

\[
\eta'=
\operatorname{diag}(3,-1,-1,-1),
\]

\[
\boxed{
H_4^T\eta'H_4
=
4(\mathbf 1\mathbf 1^T-I_4).
}
\]

This gives an exact rational validator for the tetrahedral null frame.

## 6. Relative layer / moire coframe

Let two admissible packet frames be

\[
E_A(x),\qquad E_B(x).
\]

Where \(E_A\) is invertible, define the relative layer operator

\[
\boxed{
e_{BA}(x)=E_B(x)E_A(x)^{-1}.
}
\]

This is the local moire/coframe variable.

A constant \(e_{BA}\) is only a global relative frame change. Gravity is not inferred from a constant layer offset.

The downstream gravitational gate remains

\[
e(x)
\to
g(x)=e(x)^T\eta e(x)
\to
\omega_{LC}[e]
\to
R[\omega_{LC}].
\]

If the field is globally removable/integrable so that the resulting metric is flat, the gravity claim fails.

## 7. Exterior-square 36D is downstream, not assumed upstream

Every 4x4 relative frame produces canonically

\[
\boxed{
B_{BA}=C_2(e_{BA})=\Lambda^2 e_{BA},
}
\]

a 6x6 operator with 36 coefficients.

Therefore the non-arbitrary chain is

\[
\boxed{
4\text{ elapsed-state packets}
\to
E\in GL(4)
\to
e_{BA}
\to
C_2(e_{BA})\in\operatorname{Mat}_6.
}
\]

The existing exact identities follow automatically:

\[
C_2(e)^TJC_2(e)=\det(e)J,
\]

\[
\det C_2(e)=\det(e)^3.
\]

This reverses the unsafe inference direction. A generic legacy T36 vector is not promoted to geometry merely because it can be reshaped 6x6. Instead, admitted four-packet geometry generates its own 36D bivector representation.

## 8. Antipodal / Stella involution

The Bloch antipode

\[
\mathbf r\mapsto-\mathbf r
\]

acts on the lifted four-vector by spatial parity

\[
\boxed{
P=\operatorname{diag}(1,-1,-1,-1).
}
\]

For the regular tetrahedral frame,

\[
E_{-T}=PE_T,
\]

so the relative antipodal operator is exactly \(P\).

On bivectors,

\[
\boxed{
C_2(P)
=
\operatorname{diag}(-1,-1,-1,+1,+1,+1)
}
\]

in the ordered basis

\[
(01,02,03,23,31,12).
\]

Thus the antipodal layer produces an exact 3+3 sign split:

- time-space bivectors are odd;
- purely spatial bivectors are even.

Moreover

\[
\boxed{
C_2(P)^TJC_2(P)=-J
}
\]

because \(\det P=-1\).

This is a precise phase/antiphase-style involution at the bivector representation level. It is not by itself a physical matter/antimatter or gravity identification.

## 9. Relative elapsed-scale moire sector

Keep the tetrahedral directions fixed but allow each corresponding packet pair to have an independent positive relative elapsed-scale ratio

\[
r_a=\frac{\ell_a^{(B)}}{\ell_a^{(A)}}.
\]

In the rational Hadamard frame,

\[
\boxed{
A(r)=H_4\operatorname{diag}(r_0,r_1,r_2,r_3)H_4^{-1}
=
\frac14H_4\operatorname{diag}(r_a)H_4.
}
\]

This gives

\[
\boxed{
\det A(r)=r_0r_1r_2r_3.
}
\]

If all ratios are equal,

\[
r_0=r_1=r_2=r_3=r,
\]

then

\[
A(r)=rI.
\]

Only unequal relative packet scales produce off-diagonal contrast modes.

The four Hadamard modes are one average mode plus three signed contrast modes. This is an exact \(1+3\) linear decomposition of the four vertex-scale ratios; no physical interpretation of those modes is assumed here.

For the antipodal companion layer,

\[
e_{anti}(r)=P A(r),
\]

with

\[
\det e_{anti}(r)=-r_0r_1r_2r_3.
\]

## 10. Relation to canonical tetra edge transports

The previously derived canonical simplex edge transports

\[
U_{ij}
=
\sqrt{\frac{3}{4}}(I+\Sigma_i\Sigma_j)
\]

remain exact, but direct comparison of the aligned tetrahedron and its antipode gives

\[
U^-_{ij}=U^+_{ij}.
\]

Therefore the scalar Hilbert--Schmidt edge-transport overlap does **not** supply the required moire phase. In the aligned case its values are real and include zeros.

This route is explicitly rejected as the primary phase decoder.

The coframe-relative operator \(E_BE_A^{-1}\) is the cleaner layer variable.

## 11. Promotion ledger

- one elapsed-state packet -> four coordinates: PASS UPSTREAM EXACT
- four independent packets -> local 16-parameter matrix family: PASS EXACT
- tetra-SIC pure packets form a nondegenerate null frame: PASS EXACT
- rational Hadamard realization: PASS EXACT
- antipode -> spatial parity P: PASS EXACT
- C2(P) -> exact 3+3 sign split: PASS EXACT
- relative packet frames -> unique local e_BA: PASS EXACT
- e_BA -> C2(e_BA) 36D bivector representation: PASS EXACT
- unequal relative tetra packet scales -> nontrivial Hadamard contrast coframe: PASS EXACT
- canonical aligned T/-T edge-overlap phase as moire source: FAIL
- physical clock scale ell=c dt: OPEN UPSTREAM BINDING
- packet field dynamics: OPEN
- non-flat spacetime curvature from the packet dynamics: OPEN
- Newton constant/source normalization: OPEN
- Einstein equations from pre-geometric dynamics: OPEN
- Clay Millennium closure: NOT CLAIMED


## 12. IDT relative-frame dynamics crosslink

The IDT candidate branch
`feat/four-packet-relative-coframe-dynamics-v01-20260924`
supplies the exact evolution identities for two admitted packet frames.

Let

\[
e=E_BE_A^{-1},
\qquad
L_A=\dot E_AE_A^{-1},
\qquad
L_B=\dot E_BE_B^{-1}.
\]

Then

\[
\boxed{
\dot e=L_Be-eL_A.
}
\]

For the generated bivector operator

\[
B=C_2(e),
\]

the differential exterior-square representation gives

\[
\boxed{
\dot B
=
\rho(L_B)B
-
B\rho(L_A).
}
\]

These identities were validated independently with exact rational arithmetic.

IDT 01A provides the upstream candidate response type

\[
\dot Y=-G\nabla\mathcal I+JG\nabla\mathcal H
\]

on an even-dimensional relational state manifold. Applied to the sixteen packet coordinates, it supplies a typed route to \(\dot E\) once \(G,J,\mathcal I,\mathcal H\) are physically admitted.

This closes the **relative-frame evolution identity**, but not the unique physical packet dynamics. The functionals and response geometry remain an explicit source gate.


## 13. Tetra-SIC Shannon--Onsager packet-flow binding

IDT 09C adds a concrete symmetric packet-velocity sector using the same tetrahedral SIC coordinates already present upstream.

For one packet,

\[
p_a=\frac14(1+\mathbf r\cdot\mathbf n_a),
\qquad
\mathbf r=3\sum_a p_a\mathbf n_a.
\]

The 00C/02B zero-drive mobility law fixes the six tetrahedral edge rates as

\[
M_{ab}
=
\frac{
\sqrt{\rho_R(a)\rho_R(b)}
}{
\tfrac12[\eta_R(a)+\eta_R(b)]
}.
\]

Hence

\[
\dot p=pQ[\rho_R,\eta_R],
\qquad
\dot{\mathbf r}=3\sum_a\dot p_a\mathbf n_a,
\]

and the elapsed-state packet velocity follows by the product rule.

For uniform relational fields,

\[
\rho_R=\rho_0,
\qquad
\eta_R=\eta_0,
\]

the rate is no longer free:

\[
M=\rho_0/\eta_0,
\]

and

\[
\boxed{
\dot{\mathbf r}
=
-4\frac{\rho_0}{\eta_0}\mathbf r.
}
\]

This is an exact symmetric zero-drive control sector. The physical origin/evolution of \(\rho_R\) and \(\eta_R\), nonzero directional drive, and reversible Berry sector remain separate gates.
