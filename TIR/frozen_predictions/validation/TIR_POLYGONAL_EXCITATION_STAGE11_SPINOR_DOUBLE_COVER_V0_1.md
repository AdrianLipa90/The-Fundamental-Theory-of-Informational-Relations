# TIR Polygonal Excitation — Stage 11: Spinor Double Covers of the N=4 and N=5 Closures

Status: `STAGE_11_SPINOR_DOUBLE_COVER_PASS_WITH_N4_NONTRIVIAL_EXTENSION`

Parent results:

- Stage 3: tetrahedral C3 spinor lift;
- Stage 10: finite spherical closures N=3,4,5 as {3,3}, {3,4}, {3,5}.

Scope: pure mathematics of local SU(2) lifts and global binary polyhedral symmetry.

## 1. Local rotational stabilizer

For a regular N-fold vertex star, the axis-preserving SO(3) generator is rotation by

\[
\theta_N=\frac{2\pi}{N}.
\]

Its spin-1/2 lift is

\[
\boxed{
U_N=\exp\left(-\frac{i\pi}{N}\sigma_z\right)
}
\]

with eigenvalues

\[
e^{-i\pi/N},\qquad e^{+i\pi/N}.
\]

Therefore

\[
U_N^N=\exp(-i\pi\sigma_z)=-I
\]

and

\[
\boxed{U_N^{2N}=I}.
\]

The preimage of the local C_N stabilizer under the SU(2) -> SO(3) double cover is consequently cyclic of order 2N:

\[
\boxed{C_N\longleftarrow C_{2N}}.
\]

For the finite cases,

\[
C_3\leftarrow C_6,
\qquad
C_4\leftarrow C_8,
\qquad
C_5\leftarrow C_{10}.
\]

The numerical audit verifies the orders 6, 8, and 10 directly from the 2x2 complex matrices, with closure residuals below 10^-12.

## 2. Direct-product discriminant

Compare the true local spinor preimage C_{2N} with the abstract direct product C_N x C_2.

For N odd,

\[
\gcd(N,2)=1
\]

and the Chinese remainder theorem gives

\[
C_N\times C_2\cong C_{2N}.
\]

Hence

\[
C_3\times C_2\cong C_6,
\qquad
C_5\times C_2\cong C_{10}.
\]

For N=4,

\[
C_4\times C_2
\]

has eight elements, while every element has order at most four. By contrast, the spinor preimage contains U_4 of order eight. Therefore

\[
\boxed{C_4\times C_2\not\cong C_8}.
\]

This establishes a strict algebraic distinction between the N=4 and N=5 lifts.

## 3. Global rotational symmetry

Stage 10 gives

\[
V_N=\frac{12}{6-N}.
\]

The orientation-preserving rotational group acts transitively on vertices, and the stabilizer of one vertex has order N. By orbit-stabilizer,

\[
|G_N^+|=N V_N=\frac{12N}{6-N}.
\]

Thus

\[
N=3:\quad |G_3^+|=12,\qquad G_3^+\cong A_4,
\]

\[
N=4:\quad |G_4^+|=24,\qquad G_4^+\cong S_4,
\]

\[
N=5:\quad |G_5^+|=60,\qquad G_5^+\cong A_5.
\]

## 4. Binary polyhedral double covers

Taking the SU(2) double cover of the complete orientation-preserving rotational groups gives

\[
A_4\leftarrow 2T,
\qquad
S_4\leftarrow 2O,
\qquad
A_5\leftarrow 2I,
\]

with orders

\[
|2T|=24,
\qquad
|2O|=48,
\qquad
|2I|=120.
\]

The local C_{2N} stabilizer lift is contained in the corresponding binary polyhedral group.

## 5. N=4 / N=5 result

The N=4 and N=5 members therefore have distinct local double-cover algebra:

\[
\boxed{
N=4:\ C_4\leftarrow C_8,
\quad C_4\times C_2\not\cong C_8
}
\]

while

\[
\boxed{
N=5:\ C_5\leftarrow C_{10},
\quad C_5\times C_2\cong C_{10}.
}
\]

At the global level their spinorial symmetry closures are respectively the binary octahedral group 2O and binary icosahedral group 2I.

## 6. Verdict

`STAGE_11_SPINOR_DOUBLE_COVER_PASS_WITH_N4_NONTRIVIAL_EXTENSION`

The frozen prediction remains unchanged. Particle and atomic assignments remain deferred to later gates.