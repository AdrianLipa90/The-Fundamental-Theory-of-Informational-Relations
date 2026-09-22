# TIR Herm(2) Lorentz Covariance v0.1

Status: CANDIDATE_ONLY / EXACT_SPINOR_LORENTZ_COVARIANCE / FUTURE_CONE_PRESERVED / KERNEL_PLUS_MINUS_I / PHYSICAL_EVENT_BINDING_CONDITIONAL / CANON_ALLOWED_FALSE

Date: 2026-09-19

## 1. Purpose

TIR Causal 3+1 Pair Closure v0.1 established that

\[
X=tI+\mathbf x\cdot\boldsymbol\sigma
\in\operatorname{Herm}(2)
\]

has determinant

\[
\det X=t^2-|\mathbf x|^2
\]

and that the positive-semidefinite cone is exactly the future cone

\[
\mathcal C_+
=
\{(t,\mathbf x):t\ge|\mathbf x|\}.
\]

This note proves that the natural determinant-preserving action on the same carrier generates the Lorentz symmetry of that cone.

## 2. Spinor action

Let

\[
A\in SL(2,\mathbb C)
\]

and define

\[
\boxed{
\Phi_A(X)=AXA^\dagger.
}
\]

If \(X=X^\dagger\), then

\[
(AXA^\dagger)^\dagger
=
AXA^\dagger.
\]

Therefore

\[
\Phi_A:
\operatorname{Herm}(2)
\to
\operatorname{Herm}(2).
\]

The map is real-linear in \(X\).

## 3. Determinant preservation

Using multiplicativity of the determinant,

\[
\det(AXA^\dagger)
=
\det A\,
\det X\,
\det A^\dagger.
\]

Since

\[
\det A=1
\]

and

\[
\det A^\dagger
=
\overline{\det A}
=
1,
\]

one obtains

\[
\boxed{
\det\Phi_A(X)=\det X.
}
\]

Hence

\[
\boxed{
t^2-|\mathbf x|^2
}
\]

is invariant under the induced real \(4\times4\) transformation.

Therefore the image of \(SL(2,\mathbb C)\) lies in the Lorentz group of the determinant form.

## 4. Future-cone preservation

If

\[
X\succeq0,
\]

then for every \(v\in\mathbb C^2\),

\[
v^\dagger AXA^\dagger v
=
(A^\dagger v)^\dagger X(A^\dagger v)
\ge0.
\]

Therefore

\[
\boxed{
X\succeq0
\Longrightarrow
AXA^\dagger\succeq0.
}
\]

Since \(A\) is invertible, applying the same argument to \(A^{-1}\) gives equivalence:

\[
\boxed{
X\succeq0
\Longleftrightarrow
AXA^\dagger\succeq0.
}
\]

Thus the future PSD cone is preserved exactly, including its timelike interior and null boundary.

The action therefore preserves both:

\[
\det X
\]

and the selected future component of the cone.

## 5. Explicit spatial rotations

Choose

\[
U_z(\theta)
=
\begin{pmatrix}
e^{-i\theta/2}&0\\
0&e^{i\theta/2}
\end{pmatrix}
\in SU(2).
\]

For

\[
X=
\begin{pmatrix}
t+z & x-iy\\
x+iy & t-z
\end{pmatrix},
\]

the conjugated matrix is

\[
U_z XU_z^\dagger
=
\begin{pmatrix}
t+z &
e^{-i\theta}(x-iy)\\
e^{i\theta}(x+iy)&
t-z
\end{pmatrix}.
\]

Therefore

\[
\boxed{
t'=t,
\qquad
z'=z,
}
\]

\[
\boxed{
x'=x\cos\theta-y\sin\theta,
}
\]

\[
\boxed{
y'=x\sin\theta+y\cos\theta.
}
\]

So the \(SU(2)\) subgroup reproduces the ordinary spatial \(SO(3)\) rotation action already present in TIR.

## 6. Explicit Lorentz boost

Choose the positive determinant-one matrix

\[
B_z(\chi)
=
\begin{pmatrix}
e^{\chi/2}&0\\
0&e^{-\chi/2}
\end{pmatrix}
\in SL(2,\mathbb C).
\]

Then

\[
B_zXB_z^\dagger
=
\begin{pmatrix}
e^\chi(t+z)&x-iy\\
x+iy&e^{-\chi}(t-z)
\end{pmatrix}.
\]

Recovering the Pauli coefficients gives

\[
\boxed{
t'
=
t\cosh\chi
+
z\sinh\chi,
}
\]

\[
\boxed{
z'
=
z\cosh\chi
+
t\sinh\chi,
}
\]

and

\[
\boxed{
x'=x,
\qquad
y'=y.
}
\]

This is exactly the standard Lorentz boost of rapidity \(\chi\) along the \(z\)-axis for the \(+---\) convention.

Directly,

\[
(t')^2-(z')^2
=
t^2-z^2.
\]

## 7. Arbitrary boost directions

For a unit spatial direction \(\mathbf n\), define

\[
\boxed{
B_{\mathbf n}(\chi)
=
\exp\left(
\frac{\chi}{2}
\mathbf n\cdot\boldsymbol\sigma
\right).
}
\]

Because

\[
\operatorname{Tr}
(\mathbf n\cdot\boldsymbol\sigma)=0,
\]

\[
\det B_{\mathbf n}(\chi)=1.
\]

A spatial \(SU(2)\) rotation sends \(\mathbf n\) to the \(z\)-axis, so every such boost is conjugate to the explicit \(z\)-boost above.

Thus the same carrier contains arbitrary spatial rotations and arbitrary boosts.

## 8. Generation of the proper orthochronous Lorentz group

Every

\[
A\in SL(2,\mathbb C)
\]

admits polar decomposition

\[
A=HU,
\]

where

\[
U\in SU(2)
\]

and \(H\) is positive Hermitian with determinant one.

Such an \(H\) can be diagonalized by \(SU(2)\):

\[
H
=
V
\begin{pmatrix}
e^{\chi/2}&0\\
0&e^{-\chi/2}
\end{pmatrix}
V^\dagger.
\]

Therefore every spinor action is built from spatial rotations and a boost.

Conversely spatial rotations together with boosts generate the connected proper orthochronous Lorentz group.

Hence the induced map is the standard double cover

\[
\boxed{
SL(2,\mathbb C)
\longrightarrow
SO^+(1,3).
}
\]

## 9. Kernel

Suppose

\[
AXA^\dagger=X
\]

for every

\[
X\in\operatorname{Herm}(2).
\]

Setting \(X=I\) gives

\[
AA^\dagger=I,
\]

so \(A\) is unitary.

The condition then says \(A\) commutes under conjugation with every Hermitian \(2\times2\) matrix. Since Hermitian matrices span \(M_2(\mathbb C)\), \(A\) is scalar:

\[
A=\lambda I.
\]

Unitarity gives

\[
|\lambda|=1,
\]

while

\[
\det A=\lambda^2=1.
\]

Therefore

\[
\boxed{
\ker\Phi=\{+I,-I\}.
}
\]

Thus

\[
\boxed{
SL(2,\mathbb C)/\{\pm I\}
\cong
SO^+(1,3).
}
\]

## 10. Causal-order covariance

The pair theorem defines

\[
P\preceq Q
\quad\Longleftrightarrow\quad
Q-P\in\mathcal C_+.
\]

Since \(\Phi_A\) is linear,

\[
\Phi_A(Q)-\Phi_A(P)
=
\Phi_A(Q-P).
\]

Since the cone is preserved,

\[
Q-P\in\mathcal C_+
\quad\Longleftrightarrow\quad
\Phi_A(Q-P)\in\mathcal C_+.
\]

Therefore

\[
\boxed{
P\preceq Q
\quad\Longleftrightarrow\quad
\Phi_A(P)\preceq\Phi_A(Q).
}
\]

The Lorentz action therefore preserves the theorem-level causal partial order itself, not only the determinant.

## 11. Compatibility with the half-difference variable

For a centered pair

\[
M=\frac{P+Q}{2},
\qquad
H=\frac{Q-P}{2},
\]

real-linearity gives

\[
\boxed{
\Phi_A(M)
=
\frac{\Phi_A(P)+\Phi_A(Q)}{2}
}
\]

and

\[
\boxed{
\Phi_A(H)
=
\frac{\Phi_A(Q)-\Phi_A(P)}{2}.
}
\]

Thus the unique factor-\(1/2\) pair decomposition is Lorentz covariant.

Moreover,

\[
\det\Phi_A(H)=\det H,
\]

so timelike/null/spacelike classification of the half-difference is invariant.

## 12. Main theorem

### Theorem — Hermitian spinor Lorentz covariance

Assume the TIR primitive event-translation carrier and future cone of Causal 3+1 Pair Closure v0.1.

Then the action

\[
X\mapsto AXA^\dagger,
\qquad
A\in SL(2,\mathbb C),
\]

1. preserves \(\operatorname{Herm}(2)\);
2. preserves the determinant \(t^2-|\mathbf x|^2\);
3. preserves the future PSD cone;
4. contains the spatial \(SO(3)\) rotations;
5. contains Lorentz boosts in every spatial direction;
6. preserves the causal pair order;
7. preserves the midpoint/half-difference decomposition;
8. has kernel exactly \(\{\pm I\}\).

Therefore the natural determinant-and-cone-preserving spinor symmetry of the same \(1+3\) carrier is

\[
\boxed{
SL(2,\mathbb C)/\{\pm I\}
\cong
SO^+(1,3).
}
\]

The Minkowski metric, future causal cone and proper orthochronous Lorentz symmetry therefore arise on one and the same primitive Hermitian carrier.

## 13. Evidence boundary

Exact mathematics:

- determinant preservation;
- PSD-cone preservation;
- explicit rotations;
- explicit boosts;
- arbitrary boost directions by \(SU(2)\) conjugation;
- kernel \(\{\pm I\}\);
- causal-order covariance;
- half-difference covariance;
- standard double-cover identification.

Still conditional physically:

- physical event translations use the TIR \(\operatorname{Herm}(2)\) carrier;
- physical future causality is the PSD-cone order;
- the scalar trace coordinate is physically calibrated to clock time.

No production or canon promotion is claimed.
