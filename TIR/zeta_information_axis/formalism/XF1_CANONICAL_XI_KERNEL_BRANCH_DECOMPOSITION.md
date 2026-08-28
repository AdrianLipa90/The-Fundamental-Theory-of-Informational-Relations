# XF-1 — Canonical Xi-Kernel Branch Decomposition

Status: `STANDARD_REPRESENTATION / EXACT_BRANCH_IDENTITY / GLOBAL_NONDEGENERACY_OPEN / RH_OPEN`

## 1. Coordinate

Use the entire Xi coordinate

\[
\Xi(z):=\xi\!\left(\frac12+i z\right).
\]

For

\[
s=\beta+i\gamma,
\]

the corresponding Xi coordinate is

\[
\boxed{z=\gamma+i\left(\frac12-\beta\right)}.
\]

Hence the critical line \(\beta=1/2\) is exactly the real \(z\)-axis.

## 2. Standard Riemann kernel

Use the standard rapidly decaying real kernel

\[
\Phi(u)
=
\sum_{n=1}^{\infty}
\left(
4\pi^2n^4e^{9u/2}
-
6\pi n^2e^{5u/2}
\right)
\exp\!\left(-\pi n^2e^{2u}\right),
\qquad u\ge0,
\]

with the classical cosine representation

\[
\boxed{
\Xi(z)=2\int_0^\infty \Phi(u)\cos(zu)\,du.
}
\]

The repository already uses this Xi/Fourier route in the critical-axis monograph. XF-1 resolves its cosine into the two exponential branches carried by the same kernel.

## 3. Canonical branches

Define

\[
A_+(z)
:=
\int_0^\infty \Phi(u)e^{+izu}\,du,
\]

\[
A_-(z)
:=
\int_0^\infty \Phi(u)e^{-izu}\,du.
\]

Since

\[
2\cos(zu)=e^{izu}+e^{-izu},
\]

one obtains the exact decomposition

\[
\boxed{
\Xi(z)=A_+(z)+A_-(z).
}
\]

This branch pair is fixed by the standard Xi kernel and the exponential resolution of the cosine transform.

## 4. Exact zero cancellation

For every zero \(z_0\) of \(\Xi\),

\[
\Xi(z_0)=0
\]

implies

\[
\boxed{
A_+(z_0)=-A_-(z_0).
}
\]

Therefore the two Xi-kernel branches form an exact cancellation pair at every Xi zero.

This promotes the representation part of the previous zero-state debt to an exact kernel identity. The stronger global statement that both branch amplitudes remain nonzero at every nontrivial zero is tracked separately as `GLOBAL_NONDEGENERACY_OPEN`.

## 5. Real-axis conjugacy

For real \(t\), the kernel \(\Phi(u)\) is real, so

\[
\boxed{
A_-(t)=\overline{A_+(t)}.
}
\]

Thus a real Xi zero satisfies

\[
A_+(t_0)+\overline{A_+(t_0)}=0,
\]

and its branch amplitude is purely imaginary in this representation.

## 6. Nondegenerate branch population

Whenever

\[
|A_+(z)|^2+|A_-(z)|^2>0,
\]

define

\[
P_+(z)
=
\frac{|A_+(z)|^2}
{|A_+(z)|^2+|A_-(z)|^2}.
\]

At every nondegenerate Xi zero, exact cancellation gives

\[
|A_+(z_0)|=|A_-(z_0)|,
\]

hence

\[
\boxed{P_+(z_0)=\frac12.}
\]

The runtime validation checks this explicitly on known critical-line zeros without using that numerical evidence as a statement about unobserved zeros.

## 7. Sharpened RH firewall

The affine strip result already establishes that, under endpoint-preserving affine identification, the binary coordinate is

\[
\sigma=\Re s=\beta.
\]

XF-1 independently gives, at every nondegenerate Xi zero,

\[
P_+=\frac12.
\]

The remaining identification is therefore the explicit bridge

\[
\boxed{
P_+(z_0)\stackrel{?}{=}\sigma(z_0)=\Re s_0.
}
\]

Call this `KERNEL_POPULATION_TO_STRIP_COORDINATE`.

On the nondegenerate zero sector, admitting that bridge for every nontrivial zero gives

\[
\Re s_0=P_+(z_0)=\frac12.
\]

Conversely, if every nontrivial zero has \(\Re s_0=1/2\), then the exact kernel cancellation and nondegeneracy give \(P_+(z_0)=\Re s_0\).

Thus, after XF-1 and global branch nondegeneracy, the universal `KERNEL_POPULATION_TO_STRIP_COORDINATE` statement is RH-equivalent. Its status is therefore kept `OPEN / RH_EQUIVALENT_BRIDGE`; it cannot be promoted from the affine-coordinate theorem alone.

## 8. Numerical realization

`src/critical_axis/xi_kernel.py` implements a finite-series, finite-cutoff evaluator with explicit controls:

- default kernel truncation: 12 terms;
- default integration cutoff: \(u=4\);
- branch reconstruction is compared directly with `completed_xi(1/2 + i z)`;
- invalid cutoffs and truncations fail closed.

The analytic identity uses the infinite series and integral. Runtime truncation is validation evidence for the implementation.

## 9. Promotion ledger

- `XI_FOURIER_KERNEL_REPRESENTATION`: `STANDARD`
- `CANONICAL_XI_TWO_BRANCH_REPRESENTATION`: `EXACT_FROM_STANDARD_REPRESENTATION`
- `XI_ZERO -> EXACT_KERNEL_BRANCH_CANCELLATION`: `EXACT`
- `REAL_Z -> A_MINUS = CONJ(A_PLUS)`: `EXACT`
- `NONDEGENERATE_ZERO -> P_PLUS = 1/2`: `EXACT`
- `GLOBAL_KERNEL_BRANCH_NONDEGENERACY`: `OPEN`
- `KERNEL_POPULATION_TO_STRIP_COORDINATE`: `OPEN / RH_EQUIVALENT_BRIDGE`
- `RIEMANN_HYPOTHESIS`: `OPEN`

## 10. Next falsifiable target

The next useful mathematical target is an independently sourced structural property of the half-kernel transform

\[
A_+(z)=\int_0^\infty\Phi(u)e^{izu}\,du
\]

that constrains its modulus or zero geometry away from the real \(z\)-axis. Candidate audits include Hermite--Biehler inequalities, total positivity / variation-diminishing conditions, and half-plane zero exclusion. Any such promotion requires a proof independent of tabulated zeta zeros.
