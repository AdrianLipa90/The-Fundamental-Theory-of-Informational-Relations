# TIR Polygonal Excitation — Stage 5 Poincare / Z2 Double-Cover Test v0.1

**Status:** `STAGE_5_DOUBLE_COVER_PASS`  
**Data use:** none  
**PDG use:** none  
**Atomic-spectrum use:** none

## 1. Question

Stage 4 established the exact integer equality

\[
N_{\rm deg}=6=\operatorname{ord}(U_3)
\]

under the frozen geometric assumptions. Stage 5 asks whether the existing TIR Bloch/Klein/Poincare transport preserves the same closure information, or whether the spinorial sign is lost under projection.

## 2. Existing TIR disk map is rotation-equivariant

The TIR tetrahedral-depth layer uses the radial Bloch/Klein-to-Poincare map

\[
F(X)=\frac{X}{1+\sqrt{1-|X|^2}}.
\]

For every spatial rotation \(R\in SO(3)\),

\[
|RX|=|X|
\]

and therefore

\[
F(RX)=RF(X).
\]

Projection to the two-dimensional plane orthogonal to the polar axis likewise commutes with rotations about that axis. Hence the canonical tetrahedral rotation

\[
R_3=R_z(2\pi/3)
\]

induces on the disk

\[
z\mapsto e^{2\pi i/3}z.
\]

Thus the projected orbit closes after three steps:

\[
z_3=z_0.
\]

## 3. Spinor lift closes after six steps

The spin-1/2 lift is

\[
U_3=\exp\!\left(-\frac{i\pi}{3}\sigma_z\right).
\]

Hence

\[
U_3^3=-I,
\qquad
U_3^6=I.
\]

For a lifted state \(\psi_k=U_3^k\psi_0\),

\[
\psi_3=-\psi_0,
\qquad
\psi_6=\psi_0.
\]

The Bloch/projective map identifies \(\psi\) and \(-\psi\). Therefore

\[
\pi(\psi_3)=\pi(\psi_0)
\]

on the Bloch sphere and on the derived Poincare disk, even though the lifted spinor has not yet returned to identity.

## 4. Exact six-state lifted orbit

For a generic non-axis state, the six successive lifted states project pairwise onto three disk positions:

\[
\begin{aligned}
\psi_0 &\mapsto z_0, & \psi_3=-\psi_0 &\mapsto z_0,\\
\psi_1 &\mapsto z_1, & \psi_4=-\psi_1 &\mapsto z_1,\\
\psi_2 &\mapsto z_2, & \psi_5=-\psi_2 &\mapsto z_2.
\end{aligned}
\]

Thus the disk orbit has cardinality three while its spinorial lift has cardinality six.

The lifted orbit is represented by a two-sheeted state space over the disk orbit:

\[
\widetilde{\mathcal O}=\mathcal O_{C_3}\times Z_2.
\]

Equivalently, at the cyclic-group level there is the exact sequence

\[
1\longrightarrow Z_2\longrightarrow C_6\longrightarrow C_3\longrightarrow1.
\]

Because \(\gcd(2,3)=1\),

\[
\boxed{C_6\cong C_3\times C_2}.
\]

This is the precise algebraic form of the Stage 2 observation that six decomposes into the already present cyclic triplet and binary sheet structure.

## 5. Relation to existing TIR structure

The older TIR Step 8 already separates:

- the tetrahedral terminal action of order three, \(C_3\);
- a binary parity/sign sheet, \(Z_2\);
- the Euler-consistent spinor identity closure at \(4\pi\).

Stage 5 shows that these ingredients are not merely numerically adjacent. Under the standard spinor lift of the canonical tetrahedral rotation, the three-state disk orbit acquires exactly two spinorial sheets, producing a six-state lifted orbit.

## 6. Result

The Poincare projection alone closes after three steps and therefore loses the spinorial sign. The augmented lifted state retains it and closes after six:

\[
\boxed{\mathcal O_{\rm disk}:3\quad\longleftarrow\quad\widetilde{\mathcal O}_{\rm spinor}:6}.
\]

Hence the relevant closure object is not the bare disk coordinate alone, but the disk coordinate together with the spinorial sheet label.

This provides a non-arbitrary structural bridge between the canonical tetrahedral \(C_3\), the existing TIR \(Z_2\) sheet, and the six-step spinor identity closure.

## 7. Boundary relative to the polygonal-excitation hypothesis

Stage 1 independently found that the strict equal-edge pole-to-polygon family reaches its first degeneracy at

\[
N=6.
\]

Stage 5 now finds that the canonical tetrahedral disk orbit has a natural lifted cardinality

\[
|\widetilde{\mathcal O}|=6.
\]

The equality

\[
N_{\rm deg}=|\widetilde{\mathcal O}|=6
\]

is therefore established as an exact structural coincidence under the frozen assumptions.

A physical causal identification between polygonal degeneracy and lifted-orbit closure is not promoted at this stage.

## 8. Next gate

The next mathematical gate is to determine whether the polygonal excitation operator can be defined on the lifted state space so that progression in base cardinality \(N=3,4,5\) accumulates a geometric/Berry/holonomic invariant whose closure occurs at the same six-state boundary, without inserting \(N=6\) by hand.
