# TIR Golden-Mean Dynamical Prime-Orbit Asymptotic v0.1

Status: `EXACT_PRIMITIVE_ORBIT_ASYMPTOTIC / EXPLICIT_ERROR_BOUND / ENTROPY_GROWTH_IDENTITY / ARITHMETIC_PNT_FIREWALL`

Scope: pure symbolic/topological dynamics of the already-established golden-mean system. The term **prime orbit** is used only in the standard dynamical sense of a primitive periodic orbit. It is not an arithmetic prime number.

## 1. Upstream exact inputs

The canonical golden-mean transfer matrix is

```math
A=\begin{pmatrix}1&1\\1&0\end{pmatrix}
```

with eigenvalues

```math
\varphi,
\qquad
\psi=-\varphi^{-1},
\qquad
\varphi=\frac{1+\sqrt5}{2}.
```

The exact fixed-point count is

```math
\boxed{
F_n=\#\operatorname{Fix}(D^n|_{K_C})
=\operatorname{tr}(A^n)
=L_n
=\varphi^n+\psi^n.
}
```

The primitive-orbit Euler-product theorem gives the number `O_n` of primitive period-`n` dynamical orbits:

```math
\boxed{
O_n
=\frac1n\sum_{d\mid n}
\mu\!\left(\frac nd\right)F_d.
}
```

Equivalently,

```math
F_n=\sum_{d\mid n}dO_d.
```

## 2. Isolate the Perron contribution

Separate the divisor `d=n` from the Möbius sum:

```math
O_n
=\frac{F_n}{n}
+\frac1n
\sum_{\substack{d\mid n\\d<n}}
\mu\!\left(\frac nd\right)F_d.
```

Using

```math
F_n=\varphi^n+\psi^n,
```

define the remainder `R_n` by

```math
\boxed{
O_n=\frac{\varphi^n}{n}+R_n.
}
```

Then exactly

```math
R_n
=\frac{\psi^n}{n}
+\frac1n
\sum_{\substack{d\mid n\\d<n}}
\mu\!\left(\frac nd\right)
\left(\varphi^d+\psi^d\right).
```

No asymptotic theorem has yet been invoked; this is an algebraic rearrangement of the exact Möbius formula.

## 3. Explicit error bound

For every `n>=2`, every proper positive divisor `d<n` satisfies

```math
\boxed{d\le n/2.}
```

Moreover

```math
|\psi|=\varphi^{-1}<1
```

and therefore, for a proper divisor `d`,

```math
|F_d|
\le\varphi^d+\varphi^{-d}
\le\varphi^{n/2}+1
\le2\varphi^{n/2}.
```

Let `tau(n)` denote the number of positive divisors of `n`. The exact remainder therefore obeys

```math
\boxed{
|R_n|
\le
\frac{\varphi^{-n}}{n}
+
\frac{2(\tau(n)-1)}{n}\varphi^{n/2}.
}
```

Using only the trivial bound `tau(n)-1<=n`, we obtain the simpler uniform estimate

```math
\boxed{
|R_n|
\le
2\varphi^{n/2}+\frac1n,
\qquad n\ge2.
}
```

Thus

```math
\boxed{
\left|
\frac{nO_n}{\varphi^n}-1
\right|
\le
2n\varphi^{-n/2}+\varphi^{-2n}.
}
```

The right-hand side tends to zero exponentially.

## 4. Exact dynamical prime-orbit asymptotic

It follows immediately that

```math
\boxed{
O_n\sim\frac{\varphi^n}{n}.
}
```

Equivalently,

```math
\boxed{
\lim_{n\to\infty}
\frac{nO_n}{\varphi^n}
=1.
}
```

Since the upstream topological entropy is

```math
h_{\rm top}=\ln\varphi,
```

the same statement is

```math
\boxed{
O_n\sim\frac{e^{nh_{\rm top}}}{n}.
}
```

This is the discrete-time prime-orbit growth law for this specific mixing shift of finite type, here obtained directly from the already-proved exact Lucas/Möbius formulas.

## 5. Relation to the fractal dimension and canonical kappa normalization

The upstream exact identities are

```math
\dim_HK_C=\frac{h_{\rm top}}{\ln2}
```

and

```math
\kappa=\frac{\ln2}{24\pi}.
```

Hence

```math
h_{\rm top}=24\pi\kappa\,\dim_HK_C.
```

Substitution into the orbit-growth law gives the equivalent normalization form

```math
\boxed{
O_n
\sim
\frac{\exp\!\left(24\pi\kappa\,\dim_HK_C\,n\right)}{n}.
}
```

This is only a rewrite of the exact entropy/dimension/kappa identities. It introduces no new parameter and no new physical interpretation of `kappa`.

## 6. What controls the error

There are two distinct subleading mechanisms:

1. the non-Perron eigenvalue contribution

```math
\psi^n=(-\varphi^{-1})^n,
```

which decays exponentially;

2. repetitions of shorter primitive orbits, represented by proper divisors `d|n`, whose largest possible length is `n/2` and whose crude total contribution is therefore at most order `\varphi^{n/2}`.

For the elementary bound proved here, the proper-divisor contribution dominates the asymptotic error scale. No unproved spectral, probabilistic, or number-theoretic assumption is used.

## 7. Arithmetic prime-number-theorem firewall

The formula

```math
O_n\sim\frac{e^{nh_{\rm top}}}{n}
```

is a **dynamical prime-orbit** asymptotic. Its variable `n` is an orbit period. `O_n` counts primitive periodic dynamical cycles.

It does not state or derive the arithmetic prime number theorem

```math
\pi(x)\sim\frac{x}{\ln x},
```

because `O_n` is not the arithmetic prime-counting function and primitive dynamical orbits are not prime integers.

Accordingly this theorem gives:

```text
primitive dynamical orbit = arithmetic prime integer     FALSE / TYPE_ERROR
O_n asymptotic = arithmetic prime-number theorem         NOT_DERIVED
Riemann zeta identification                              NOT_DERIVED
RH implication                                            NONE
```

No map from primitive golden-mean orbits to arithmetic primes with number-theoretic significance is claimed.

## 8. Claim classes

| Statement | Status |
|---|---|
| `F_n=phi^n+(-phi^-1)^n=L_n` | `EXACT_UPSTREAM` |
| Möbius formula for `O_n` | `EXACT_UPSTREAM` |
| every proper divisor `d<n` obeys `d<=n/2` | `EXACT_ELEMENTARY` |
| explicit `tau(n)` remainder bound | `EXACT` |
| `|R_n| <= 2 phi^(n/2)+1/n` | `EXACT_COARSE_BOUND` |
| `lim n O_n / phi^n = 1` | `EXACT_CONSEQUENCE` |
| `O_n ~ phi^n/n = exp(n h_top)/n` | `EXACT_ASYMPTOTIC` |
| `O_n ~ exp(24*pi*kappa*dim_H(K_C)*n)/n` | `EXACT_NORMALIZATION_REWRITE` |
| primitive orbit equals arithmetic prime | `FALSE / TYPE_ERROR` |
| arithmetic prime-number theorem derived | `NOT_DERIVED` |
| Riemann-zeta identification | `NOT_DERIVED` |
| implication for RH | `NONE` |
| physical particle/cosmological interpretation | `OPEN_NOT_CLAIMED` |

## 9. Validation requirements

A deterministic validator must:

1. verify upstream Lucas/Möbius/primitive-orbit receipts;
2. compute exact `O_n` from the Möbius formula over a finite audit range;
3. verify the explicit `tau(n)` bound and the coarser uniform bound for every audited `n>=2`;
4. verify the normalized ratio `n O_n / phi^n` approaches one numerically at increasing audit periods as a witness, while keeping the proof analytic;
5. verify the entropy and kappa normalization rewrites symbolically;
6. re-run the primitive-orbit Euler-product, coding-conjugacy, pressure, transfer, CP1-fractal, homogeneous-fibration, and canonical-kappa validators;
7. verify the arithmetic-prime, PNT, Riemann-zeta, RH, and physical-interpretation firewalls.
