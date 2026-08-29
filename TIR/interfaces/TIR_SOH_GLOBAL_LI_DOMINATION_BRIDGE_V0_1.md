# TIR ↔ Secret-of-a-Half Global Li Domination Bridge v0.1

Status: `EXACT_CONDITIONAL_GLOBAL_DOMINATION_THEOREM_CANDIDATE`

Date: 2026-08-29

## 1. Starting point

Use the already-established negative-inverse coordinate

\[
\Omega(s)=\frac{s}{1-s},
\qquad
z_L(s)=1-\frac1s=-\frac1{\Omega(s)}.
\]

For every non-trivial zero `rho`, define

\[
z_\rho:=z_L(\rho),
\qquad
r_\rho:=\max\{|z_\rho|,|z_\rho|^{-1}\}\ge1.
\]

The half-axis condition is

\[
\boxed{
\Re\rho=\frac12
\iff
|z_\rho|=1
\iff
r_\rho=1.
}
\]

For one reciprocal-conjugate quartet with

\[
z_\rho=Re^{i\phi},
\]

the local Li contribution is

\[
\boxed{
L_n(Q_\rho)
=4-2(R^n+R^{-n})\cos(n\phi).
}
\]

## 2. Lemma A — radial compactification at large height

Write

\[
\rho=\beta+i\gamma,
\qquad 0<\beta<1.
\]

Then

\[
|z_\rho|^2
=
\left|\frac{\rho-1}{\rho}\right|^2
=
\frac{(1-\beta)^2+\gamma^2}{\beta^2+\gamma^2}
=
1+\frac{1-2\beta}{\beta^2+\gamma^2}.
\]

Hence uniformly in `0<beta<1`,

\[
\bigl||z_\rho|^2-1\bigr|
\le \frac1{\gamma^2},
\]

and therefore

\[
\boxed{r_\rho\to1\quad\text{as }|\gamma|\to\infty.}
\]

This is the precise compactified-boundary statement needed by the domination argument: radial departure from the unit boundary is forced to vanish at high imaginary height.

## 3. Lemma B — existence of a finite extremal off-circle shell

Assume at least one non-trivial zero has `r_rho>1`. Define

\[
r_*=\sup_{\rho}r_\rho.
\]

By Lemma A, for every `epsilon>0` all sufficiently high zeros satisfy

\[
r_\rho<1+\epsilon.
\]

Choose an existing off-circle zero with radius `r_0>1` and take

\[
0<\epsilon<r_0-1.
\]

Every zero with `r_\rho\ge r_0` then lies below a finite height. Since zeta zeros are discrete, only finitely many occur there. Therefore the supremum is attained:

\[
\boxed{r_*=\max_\rho r_\rho>1.}
\]

The extremal set

\[
\mathcal S_*:=\{\rho:r_\rho=r_*\}
\]

is finite modulo the standard conjugate/functional-equation symmetries.

After removing this finite shell there is a strict spectral gap

\[
\boxed{
1\le r_2<r_*.
}
\]

## 4. Lemma C — simultaneous phase recurrence on the extremal shell

Let the distinct extremal quartet phases be

\[
\phi_1,\dots,\phi_m.
\]

Dirichlet simultaneous approximation gives an infinite sequence of positive integers `n_k` such that

\[
\frac{n_k\phi_j}{2\pi}
\to \mathbb Z
\qquad(j=1,\dots,m).
\]

Equivalently,

\[
\boxed{
\cos(n_k\phi_j)\to1
\quad\text{simultaneously for every extremal phase.}
}
\]

Thus for sufficiently large `k`,

\[
\sum_{j=1}^{m}\cos(n_k\phi_j)\ge\frac m2.
\]

## 5. Extremal-shell contribution

Along the recurrent subsequence, the total extremal-shell contribution obeys

\[
S_{n_k}^{(*)}
=4m
-2(r_*^{n_k}+r_*^{-n_k})
\sum_{j=1}^{m}\cos(n_k\phi_j).
\]

Therefore for all sufficiently large `k`,

\[
S_{n_k}^{(*)}
\le
4m-mr_*^{n_k}.
\]

Hence

\[
\boxed{
S_{n_k}^{(*)}
=-\Theta(r_*^{n_k}).
}
\]

## 6. Lemma D — subextremal remainder estimate

Let

\[
\lambda_n
=
\sum_\rho^{\mathrm{sym}}
\left[1-z_\rho^n\right]
\]

be the standard symmetrically regularized Li coefficient, and write

\[
\lambda_n=S_n^{(*)}+R_n.
\]

We claim

\[
\boxed{R_n=o(r_*^n).}
\]

A direct route is as follows.

Choose `q` with

\[
r_2<q<r_*.
\]

By Lemma A there is a fixed height `T_0` such that every non-extremal zero above `T_0` has radial factor at most `q`.

Split the remainder into

\[
R_n=R_n^{\le Cn}+R_n^{>Cn},
\]

with fixed sufficiently large `C`.

### Moderate-height part

The classical zero-counting estimate

\[
N(T)=O(T\log T)
\]

gives only `O(n log n)` quartets up to height `Cn`. Every non-extremal quartet in this range has radial factor at most `q`, hence

\[
\boxed{
R_n^{\le Cn}=O(n\log n\,q^n).
}
\]

Since `q<r_*`,

\[
R_n^{\le Cn}=o(r_*^n).
\]

### High-height tail

Write

\[
z_\rho=e^{u_\rho}.
\]

From

\[
z_\rho=1-\frac1\rho
\]

one has uniformly for large `|gamma|`,

\[
|u_\rho|=O(|\gamma|^{-1}).
\]

A reciprocal-conjugate quartet contributes

\[
4-\left(e^{nu}+e^{-nu}+e^{n\bar u}+e^{-n\bar u}\right)
=4-4\Re\cosh(nu).
\]

For `|gamma|>Cn`, choose `C` so that `|nu|` stays in a fixed small disk. Taylor control of `cosh` then gives

\[
|L_n(Q_\rho)|
\le
K\frac{n^2}{\gamma^2}
\]

with a constant `K` independent of `n` and the high zero.

Using `N(T)=O(T\log T)` and partial summation,

\[
\sum_{|\gamma|>Cn}\frac1{\gamma^2}
=O\!\left(\frac{\log n}{n}\right).
\]

Therefore

\[
\boxed{
R_n^{>Cn}=O(n\log n)=o(r_*^n).
}
\]

Combining both pieces yields Lemma D.

## 7. Global domination theorem

### Theorem

Assume the standard symmetric Li representation and the classical zeta zero-counting estimate. If a non-trivial zero exists away from the critical line, then the full Li sequence contains a negative subsequence.

### Proof

An off-axis zero gives `r_*>1` by Lemmas A and B. Lemma C supplies an infinite sequence `n_k` on which all extremal-shell phases recur simultaneously near phase zero. The extremal shell then contributes

\[
S_{n_k}^{(*)}=-\Theta(r_*^{n_k}).
\]

Lemma D gives

\[
R_{n_k}=o(r_*^{n_k}).
\]

Hence for all sufficiently large `k`,

\[
\boxed{\lambda_{n_k}<0.}
\]

Therefore

\[
\boxed{
\exists\rho:\Re\rho\ne\frac12
\Longrightarrow
\exists\text{ infinitely many }n:\lambda_n<0.
}
\]

Equivalently,

\[
\boxed{
\lambda_n\ge0\ \forall n
\Longrightarrow
\Re\rho=\frac12\ \forall\rho.
}
\]

## 8. What this closes in the project graph

This theorem upgrades the earlier local statement

\[
r_\rho>1
\Longrightarrow
L_n(Q_\rho)\text{ has an unbounded negative subsequence}
\]

to a full-sequence domination statement:

\[
\boxed{
\text{off-circle zero}
\Longrightarrow
\text{negative full Li coefficient along a subsequence}.
}
\]

Thus the local-to-global aggregation gate is reduced to the standard analytic ingredients made explicit above.

The remaining promotion target in the Secret-of-a-Half programme is the independent positivity/native-closure direction for the complete arithmetic form / Li sequence.

## 9. Next proof target

The next theorem should bind the framework closure functional to global Li/Weil positivity:

\[
\boxed{
\text{native closure / complete arithmetic positivity}
\Longrightarrow
\lambda_n\ge0\quad\forall n.
}
\]

Together with the domination theorem above, this is the shortest current path from the negative-inverse boundary geometry to full critical-axis closure.
