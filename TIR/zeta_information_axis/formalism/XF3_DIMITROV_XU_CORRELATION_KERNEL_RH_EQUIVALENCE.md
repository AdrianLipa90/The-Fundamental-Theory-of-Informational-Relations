# XF-3 — Dimitrov–Xu correlation-kernel RH-equivalence audit

Status: `STANDARD_EXTERNAL_THEOREM / NUMERICAL_DIAGNOSTICS_IMPLEMENTED / GLOBAL_DENSITY_OPEN / RIEMANN_HYPOTHESIS_OPEN`

## 1. Scope

XF-3 adds an independent analytic route from the canonical Riemann Xi Fourier kernel to a published RH-equivalent density criterion. It is intentionally separated from the XF-2 Hermite–Biehler candidate family.

The theorem-level source is:

Dimitar K. Dimitrov and Yuan Xu, *Wronskians of Fourier and Laplace Transforms*, arXiv:1606.05011 (2016), especially Theorem 1.1, Theorem 1.3 / Theorem 2.5, and Corollary 3.5.

Repository convention:

\[
\Xi(z)=\xi\!\left(\frac12+i z\right)
      =\int_{\mathbb R}\Phi(t)e^{i z t}\,dt,
\]

with the even Riemann kernel \(\Phi\) used by XF-1.

## 2. Correlation kernel

For the \(n=2\) Dimitrov–Xu correlation function,

\[
\boxed{
\nu_2(t)
=\int_{-\infty}^{\infty}
(t-2s)^2\,\Phi(t-s)\Phi(s)\,ds
}
\]

and for

\[
0<|y|<\frac12,
\]

define

\[
\boxed{
\Phi_{2,y}(t)=\cosh(ty)\,\nu_2(t).
}
\]

The runtime implementation in `src/critical_axis/correlation_kernel.py` evaluates these expressions with explicit finite series and integration cutoffs. Those cutoffs belong to the numerical-validation layer only.

## 3. External STANDARD equivalence

Dimitrov–Xu Theorem 1.1 gives the following necessary-and-sufficient criterion:

\[
\boxed{
\mathrm{RH}
\iff
\forall y\in\left(-\frac12,\frac12\right)\setminus\{0\},
\quad
\operatorname{span}\mathcal T(\Phi_{2,y})
\text{ is dense in }L^1(\mathbb R).
}
\]

Here \(\mathcal T(f)\) denotes the set of translates of \(f\).

The same theorem states a stronger real-and-simple-zero criterion when density is required for every fixed \(y\in(-1/2,1/2)\), including \(y=0\). XF-3 keeps that statement separate from the RH criterion.

Corollary 3.5 supplies the equivalent annihilator formulation:

\[
\boxed{
\mathrm{RH}
\iff
\Phi_{2,y}*g=0
\text{ for bounded }g
\Longrightarrow g=0
}
\]

for each \(0<|y|<1/2\).

These equivalences are imported as `STANDARD` external mathematics. The repository obligation is the independent establishment of the density/annihilator premise, not the re-labelling of the theorem itself.

## 4. Wronskian bridge

For \(n=2\), Dimitrov–Xu Theorem 1.3 gives

\[
W_2(\Xi;x)
=-\mathcal F[\nu_2](x),
\]

where

\[
W_2(\Xi;x)=\Xi(x)\Xi''(x)-\Xi'(x)^2.
\]

On the real axis \(\Xi(x)\in\mathbb R\), hence the first Laguerre quantity is

\[
\boxed{
L_1[\Xi](x)
=\Xi'(x)^2-\Xi(x)\Xi''(x)
=-W_2(\Xi;x)
=\mathcal F[\nu_2](x).
}
\]

The identity `xi_laguerre_quantity(x) + xi_wronskian2_real(x) = 0` is therefore an exact implementation-level consistency check on the repository convention.

## 5. Epistemic firewall

### STANDARD / admitted

- the Dimitrov–Xu definition of \(\nu_2\) and \(\Phi_{2,y}\);
- the Wronskian–Fourier correlation identity;
- the `RH iff L1-translation-density` theorem;
- the equivalent bounded-convolution-annihilator theorem.

### NUMERICAL_DIAGNOSTIC

- finite `max_terms` evaluation of the Riemann kernel;
- finite symmetric integration cutoff for \(\nu_2\);
- sampled values of \(\Phi_{2,y}\), the Wronskian, and Laguerre quantity;
- finite-grid positivity or sign observations.

### OPEN

\[
\boxed{
\forall\,0<|y|<\frac12:
\operatorname{span}\mathcal T(\Phi_{2,y})
\text{ dense in }L^1(\mathbb R)
}
\]

and equivalently the absence of a nonzero bounded convolution annihilator for every admissible \(y\).

`RIEMANN_HYPOTHESIS` therefore retains status `OPEN` in the solver unless one of these global premises is independently admitted.

## 6. Relation to XF-1 and XF-2

XF-1 supplies the canonical Xi kernel and the exact two-branch cancellation identity at every Xi zero.

XF-2 / XF-2A record a negative result for the raw de Branges branch candidate and its constant real mixing family.

XF-3 uses the same canonical Xi kernel through a different theorem-level object:

\[
\Phi
\longrightarrow
\nu_2
\longrightarrow
\Phi_{2,y}
\longrightarrow
L^1\text{-translation density / convolution annihilator}.
\]

No Hermite–Biehler assumption is required for this route.

## 7. Falsification and validation gates

1. `nu_2(t)` must be numerically even under the symmetric implementation.
2. `Phi_{2,y}` must satisfy the exact runtime symmetry `Phi_{2,y}=Phi_{2,-y}` because the multiplier is `cosh(ty)`.
3. `0 < |y| < 1/2` is fail-closed at the criterion interface.
4. The real-axis Laguerre/Wronskian identity must close to numerical precision.
5. Finite sampled positivity remains tagged `NUMERICAL_DIAGNOSTIC`.
6. No finite grid, finite cutoff, or finite family of translates can promote the global density premise.

## 8. Next mathematical frontier

The next admissible target is a rigorous attack on the global density/annihilator condition. Candidate work must preserve the theorem's quantifiers over every admissible \(y\) and the full space \(L^1(\mathbb R)\).

A finite-dimensional surrogate may be used only as a falsification or convergence diagnostic. Promotion requires an analytic argument controlling the infinite-domain and all-translation limits.
