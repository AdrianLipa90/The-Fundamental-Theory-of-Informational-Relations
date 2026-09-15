# TIR Golden-Mean Primitive-Orbit Euler Product v0.1

Status: `EXACT_PRIMITIVE_ORBIT_COUNTS / EXACT_DYNAMICAL_EULER_PRODUCT / EXACT_WEIGHTED_ORBIT_PRODUCT / ARITHMETIC_PRIME_FIREWALL`

Scope: pure symbolic/topological dynamics of the already-established golden-mean system `(K_C,D|_{K_C})`. The word `Euler product` refers only to factorization over primitive periodic **dynamical orbits**. No identification with arithmetic primes, the Riemann zeta function, the Euler product over prime numbers, or the Riemann hypothesis is asserted.

## 1. Exact upstream inputs

The upstream coding-conjugacy theorem establishes

```math
(\Sigma_{\rm GM}^{+},\sigma)\cong(K_C,D|_{K_C})
```

and the adjacency matrix

```math
A=\begin{pmatrix}1&1\\1&0\end{pmatrix}.
```

For every `n>=1`,

```math
\boxed{F_n:=\#\operatorname{Fix}(D^n|_{K_C})=\operatorname{tr}(A^n)=L_n,}
```

where `L_n` is the Lucas sequence.

The number of points of exact period `n` is

```math
\boxed{E_n=\sum_{d\mid n}\mu\!\left(\frac nd\right)F_d,}
```

and the number of primitive period-`n` orbits is

```math
\boxed{O_n=\frac{E_n}{n}.}
```

Every exact-period-`n` orbit contains exactly `n` points, so `O_n` is a nonnegative integer.

For `n=1,...,12`, the exact values are

```text
n   F_n   E_n   O_n
1     1     1     1
2     3     2     1
3     4     3     1
4     7     4     1
5    11    10     2
6    18    12     2
7    29    28     4
8    47    40     5
9    76    72     8
10  123   110    11
11  199   198    18
12  322   300    25
```

## 2. Fixed points decompose into primitive cycles

A point fixed by `D^n` belongs to a primitive orbit whose least period `m` divides `n`. A primitive orbit of length `m` contributes all of its `m` points to `Fix(D^n)` whenever `m|n`. Therefore

```math
\boxed{F_n=\sum_{m\mid n}mO_m.}
```

Möbius inversion of this divisor identity gives precisely

```math
nO_n=\sum_{d\mid n}\mu\!\left(\frac nd\right)F_d.
```

Thus the primitive-orbit multiplicities are not additional fitted data; they are exactly forced by the upstream periodic-point counts.

## 3. Primitive-orbit Euler product

Let `\mathcal P` denote the set of primitive periodic orbits of `D|_{K_C}` and let `|p|` be the least period of `p`.

Define the orbit product formally by

```math
\boxed{
\mathcal Z_{\rm orb}(z)
:=\prod_{p\in\mathcal P}\frac1{1-z^{|p|}}.
}
```

Grouping primitive orbits by their lengths yields

```math
\boxed{
\mathcal Z_{\rm orb}(z)
=\prod_{m\ge1}(1-z^m)^{-O_m}.
}
```

Take the formal logarithm. Since

```math
-\log(1-z^m)=\sum_{k\ge1}\frac{z^{mk}}k,
```

we obtain

```math
\log\mathcal Z_{\rm orb}(z)
=\sum_{m\ge1}O_m\sum_{k\ge1}\frac{z^{mk}}k.
```

The coefficient of `z^n` is

```math
\sum_{m\mid n}\frac{O_m}{n/m}
=\frac1n\sum_{m\mid n}mO_m
=\frac{F_n}{n}.
```

Hence

```math
\boxed{
\log\mathcal Z_{\rm orb}(z)
=\sum_{n\ge1}\frac{F_n}{n}z^n.
}
```

But the right-hand side is exactly the defining logarithm of the Artin-Mazur zeta function. Therefore

```math
\boxed{
\zeta_{\rm AM}(z)
=\prod_{p\in\mathcal P}(1-z^{|p|})^{-1}
=\prod_{m\ge1}(1-z^m)^{-O_m}.
}
```

Using the upstream determinant theorem,

```math
\boxed{
\prod_{m\ge1}(1-z^m)^{-O_m}
=\frac1{\det(I-zA)}
=\frac1{1-z-z^2}.
}
```

This equality is exact as an identity of formal power series around `z=0`, and analytically throughout the common disk of convergence `|z|<1/\varphi`.

## 4. Finite truncations are exact to finite order

For any `N>=1`, define

```math
Z_N(z):=\prod_{m=1}^{N}(1-z^m)^{-O_m}.
```

Every omitted factor with `m>N` starts at degree `m>N`. Consequently

```math
\boxed{
Z_N(z)
=\frac1{1-z-z^2}+O(z^{N+1}).
}
```

Equivalently,

```math
\boxed{
z\frac{d}{dz}\log Z_N(z)
=\sum_{n=1}^{N}F_nz^n+O(z^{N+1}).
}
```

This provides a deterministic finite-order validator of the infinite orbit factorization without numerically approximating an infinite product.

## 5. Weighted primitive-orbit product

The upstream pressure family is

```math
M(s)=2^{-s}A.
```

Write

```math
q:=2^{-s}>0.
```

A primitive orbit of length `m` accumulates the constant one-step weight `q` exactly `m` times, hence its orbit weight is `q^m`. The corresponding weighted primitive-orbit product is

```math
\boxed{
\zeta_{\rm orb}(z;s)
=\prod_{p\in\mathcal P}\frac1{1-(qz)^{|p|}}
=\prod_{m\ge1}(1-(qz)^m)^{-O_m}.
}
```

The same logarithmic divisor calculation gives

```math
\boxed{
\zeta_{\rm orb}(z;s)
=\frac1{\det(I-zqA)}
=\frac1{1-qz-q^2z^2}.
}
```

Substituting `q=2^{-s}`,

```math
\boxed{
\zeta_{\rm orb}(z;s)
=\frac1{1-2^{-s}z-2^{-2s}z^2}.
}
```

Its nearest positive pole remains

```math
\boxed{z_c(s)=\frac1{q\varphi}=\frac{2^s}{\varphi},}
```

so the upstream pressure relation is recovered exactly:

```math
\boxed{P(s)=-\ln z_c(s)=\ln\varphi-s\ln2.}
```

With the canonical TIR normalization `\kappa=\ln2/(24\pi)`, this is equivalently

```math
\boxed{P(s)=h_{\rm top}-24\pi\kappa s.}
```

No new parameter is introduced by the orbit product.

## 6. Dynamical-prime versus arithmetic-prime firewall

A primitive periodic orbit is sometimes called a **prime orbit** in dynamical-systems literature because it cannot be written as an iterate of a shorter periodic orbit. That terminology is structural, not arithmetic.

Here:

```text
primitive / prime dynamical orbit != prime integer
```

and therefore

```text
prod_{primitive dynamical orbits} (1-z^period)^(-1)
!=
prod_{p arithmetic prime} (1-p^(-s))^(-1)
```

as a claimed identification.

The left-hand side is an Artin-Mazur/dynamical Euler product generated by periodic orbit lengths. The familiar arithmetic Euler product is a representation of the Riemann zeta function over prime integers. They are differently typed constructions.

Accordingly, this theorem establishes no map

```math
\mathcal P\longrightarrow\{2,3,5,7,\ldots\}
```

with number-theoretic significance, no equality with `\zeta_R(s)`, no correspondence of zeros or poles with Riemann zeros, no critical-line result, and no implication for RH.

## 7. Claim classes

| Statement | Status |
|---|---|
| `F_n=tr(A^n)=L_n` | `EXACT_UPSTREAM` |
| `F_n=sum_{m|n} m O_m` | `EXACT` |
| `O_n=(1/n) sum_{d|n} mu(n/d)F_d` | `STANDARD_MOBIUS_INVERSION_APPLIED_EXACTLY` |
| `O_n` counts primitive period-n dynamical orbits | `EXACT` |
| primitive-orbit Euler product for `zeta_AM` | `STANDARD_DYNAMICAL_ZETA_THEOREM_DERIVED_EXACTLY` |
| `prod_m(1-z^m)^(-O_m)=1/(1-z-z^2)` | `EXACT` |
| finite product through `m=N` matches through degree `N` | `EXACT` |
| weighted product `prod_m(1-(2^-s z)^m)^(-O_m)` | `EXACT` |
| nearest weighted pole recovers pressure | `EXACT_UPSTREAM_CROSSCHECK` |
| primitive dynamical orbit equals arithmetic prime | `FALSE / TYPE_ERROR` |
| dynamical Euler product equals Riemann Euler product | `NOT_DERIVED / NOT_CLAIMED` |
| Riemann-zeta identification | `NOT_DERIVED / NOT_CLAIMED` |
| implication for RH | `NONE` |
| physical particle/cosmological interpretation of primitive orbits | `OPEN_NOT_CLAIMED` |

## 8. Validation requirements

A deterministic validator must:

1. read the upstream coding-conjugacy theorem and verify the `F_n=tr(A^n)=L_n` and Artin-Mazur receipts;
2. compute `F_n`, `E_n`, and `O_n` exactly for a finite audit range and check nonnegative integrality;
3. verify `F_n=sum_{m|n}mO_m` and Möbius inversion exactly;
4. expand the finite primitive-orbit product to degree `N` and compare it with `1/(1-z-z^2)` through degree `N`;
5. compare `z d/dz log Z_N` with the exact fixed-point generating coefficients through degree `N`;
6. verify the weighted finite product against `1/det(I-zqA)` through degree `N` with symbolic `q`;
7. verify the nearest positive weighted pole and pressure identity;
8. re-run the coding-conjugacy, pressure, transfer, CP1-fractal, homogeneous-fibration, and canonical-kappa validators;
9. verify the arithmetic-prime, Riemann-zeta, RH, and physical-interpretation firewalls.
