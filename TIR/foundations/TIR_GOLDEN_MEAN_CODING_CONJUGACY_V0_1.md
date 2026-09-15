# TIR Golden-Mean Coding Conjugacy and Artin-Mazur Zeta v0.1

Status: `EXACT_ONE_SIDED_SYMBOLIC_CONJUGACY / EXACT_PERIODIC_POINT_COUNTS / EXACT_ARTIN_MAZUR_ZETA / RIEMANN_ZETA_FIREWALL`

Scope: pure symbolic/topological dynamics of the already-established golden-mean envelope `K_C` under the dyadic circle map. No physical time, entropy, energy, cosmological, particle, Riemann-zeta, or RH interpretation is asserted.

## 1. Upstream objects

The canonical golden-mean symbolic space is

```math
\Sigma_{\rm GM}^{+}
=
\left\{
b=(b_0,b_1,\ldots)\in\{0,1\}^{\mathbb N_0}:
 b_kb_{k+1}=0\ \forall k
\right\}.
```

Its one-sided left shift is

```math
\sigma(b_0,b_1,b_2,\ldots)=(b_1,b_2,b_3,\ldots).
```

The upstream dyadic/Collatz-admissible fractal theorem defines

```math
K_C=
\left\{
\sum_{k\ge0}\frac{b_k}{2^{k+1}}:
 b\in\Sigma_{\rm GM}^{+}
\right\}
\subset[0,2/3].
```

Define the coding map

```math
\boxed{
\pi:\Sigma_{\rm GM}^{+}\to K_C,
\qquad
\pi(b)=\sum_{k\ge0}\frac{b_k}{2^{k+1}}.
}
```

The phase dynamics is the degree-two circle map

```math
D(x)=2x\pmod1.
```

## 2. The coding map is continuous

Equip `Sigma_GM^+` with the usual product topology, for example through the metric

```math
d_2(b,c)=2^{-N(b,c)},
```

where `N(b,c)` is the first index at which the two sequences differ, with distance `0` for identical sequences.

If two sequences agree through index `N-1`, then

```math
|\pi(b)-\pi(c)|
\le
\sum_{k\ge N}2^{-(k+1)}
=2^{-N}.
```

Hence `pi` is continuous.

## 3. The golden-mean constraint removes binary ambiguity

The only possible non-uniqueness of a binary expansion in `[0,1]` is the terminating/eventually-one ambiguity.

Here it can be excluded directly. Suppose

```math
\pi(b)=\pi(c),
\qquad b\ne c,
```

and let `j` be the first index at which they differ. Without loss of generality let

```math
b_j=0,
\qquad c_j=1.
```

After multiplying the equality by `2^{j+1}` and cancelling the common prefix,

```math
\sum_{r\ge1}(b_{j+r}-c_{j+r})2^{-r}=1.
```

But the left-hand side is bounded above by

```math
\sum_{r\ge1}2^{-r}=1,
```

and equality can occur only if

```text
b_{j+1}b_{j+2}b_{j+3}... = 1111...
c_{j+1}c_{j+2}c_{j+3}... = 0000...
```

The first tail is forbidden by the golden-mean rule `11`.

Therefore

```math
\boxed{\pi\ \text{is injective}.}
```

Surjectivity onto `K_C` is true by the definition of `K_C`. Since `Sigma_GM^+` is compact and `K_C\subset\mathbb R` is Hausdorff, a continuous bijection is a homeomorphism. Thus

```math
\boxed{
\pi:\Sigma_{\rm GM}^{+}\overset{\cong}{\longrightarrow}K_C
}
```

is a topological coding homeomorphism.

## 4. Exact topological conjugacy

For any `b in Sigma_GM^+`,

```math
2\pi(b)
=
b_0+\sum_{k\ge1}\frac{b_k}{2^k}.
```

Taking modulo one removes the integer `b_0`, so

```math
D(\pi(b))
=
\sum_{k\ge1}\frac{b_k}{2^k}
=
\pi(\sigma b).
```

Hence the diagram commutes exactly:

```math
\boxed{
D\circ\pi=\pi\circ\sigma.
}
```

Because `pi` is a homeomorphism,

```math
\boxed{
(\Sigma_{\rm GM}^{+},\sigma)
\cong
(K_C,D|_{K_C})
}
```

as topological dynamical systems.

This is the correct nonlinear/topological intertwiner. It does **not** contradict the upstream linear no-go theorem for the geometric `E7,E8` axial representation: a coding homeomorphism between sequence space and `K_C` is a differently typed object from a nonzero linear map `T` satisfying `AT=TJ_6`.

## 5. Periodic points are Lucas counts

The golden-mean shift has adjacency matrix

```math
A=
\begin{pmatrix}
1&1\\
1&0
\end{pmatrix}.
```

A point fixed by `sigma^n` is an admissible period-`n` sequence, equivalently a closed walk of length `n` in the adjacency graph. Therefore

```math
\boxed{
\#\operatorname{Fix}(\sigma^n)=\operatorname{tr}(A^n).
}
```

By conjugacy, the same count holds on `K_C`:

```math
\boxed{
\#\operatorname{Fix}(D^n|_{K_C})=\operatorname{tr}(A^n).
}
```

Since

```math
\operatorname{spec}(A)=\left\{\varphi,-\varphi^{-1}\right\},
```

we obtain

```math
\operatorname{tr}(A^n)
=\varphi^n+(-\varphi^{-1})^n
=L_n,
```

where `L_n` is the Lucas sequence with

```math
L_0=2,
\qquad L_1=1,
\qquad L_{n+2}=L_{n+1}+L_n.
```

Thus

```math
\boxed{
\#\operatorname{Fix}(D^n|_{K_C})=L_n.
}
```

The number of points of exact period `n` is consequently

```math
\boxed{
E_n=\sum_{d\mid n}\mu\!\left(\frac nd\right)L_d,
}
```

and the number of primitive period-`n` orbits is

```math
\boxed{O_n=E_n/n.}
```

## 6. Exact Artin-Mazur dynamical zeta function

Define the Artin-Mazur dynamical zeta function by

```math
\zeta_{\rm AM}(z)
=
\exp\left(
\sum_{n\ge1}
\frac{\#\operatorname{Fix}(D^n|_{K_C})}{n}z^n
\right).
```

For a finite-state shift of finite type,

```math
\zeta_{\rm AM}(z)=\frac1{\det(I-zA)}.
```

Here

```math
\det(I-zA)=1-z-z^2,
```

therefore

```math
\boxed{
\zeta_{\rm AM}(z)=\frac1{1-z-z^2}.
}
```

As a power-series definition its radius of convergence is

```math
R=\frac1\varphi,
```

because the poles are

```math
z=\frac1\varphi,
\qquad z=-\varphi.
```

Hence the topological entropy is recovered from the nearest pole:

```math
\boxed{
h_{\rm top}=-\ln R=\ln\varphi.
}
```

## 7. Weighted determinant bridge to the pressure theorem

The upstream pressure theorem introduced

```math
M(s)=2^{-s}A
```

with

```math
P(s)=\ln\rho(M(s))=\ln\varphi-s\ln2.
```

Define the weighted dynamical determinant/zeta family

```math
\zeta_{\rm AM}(z;s)
=\frac1{\det(I-zM(s))}.
```

Then

```math
\boxed{
\zeta_{\rm AM}(z;s)
=
\frac1{1-2^{-s}z-2^{-2s}z^2}.
}
```

Its nearest positive pole is

```math
\boxed{
z_c(s)=\frac{2^s}{\varphi}.}
```

Therefore

```math
\boxed{
P(s)=-\ln z_c(s).
}
```

At the Hausdorff dimension

```math
d_H=\log_2\varphi,
```

one has

```math
z_c(d_H)=1,
\qquad
P(d_H)=0.
```

Using the independently established TIR normalization

```math
\kappa=\frac{\ln2}{24\pi},
```

the same exact pressure identity remains

```math
\boxed{
P(s)=h_{\rm top}-24\pi\kappa s.
}
```

No new constant is introduced by the zeta/determinant representation.

## 8. Zeta firewall

The symbol `zeta` is overloaded in mathematics. The function established here is the **Artin-Mazur dynamical zeta function** of a finite-state dynamical system:

```math
\zeta_{\rm AM}(z)=\frac1{1-z-z^2}.
```

It is **not** the Riemann zeta function

```math
\zeta_{\rm R}(s)=\sum_{n\ge1}n^{-s},
```

and no equality, analytic continuation bridge, zero correspondence, critical-line statement, or implication for the Riemann hypothesis is claimed.

Accordingly:

```text
Artin-Mazur zeta = EXACT HERE
Riemann zeta identification = NOT_DERIVED
RH implication = NONE
```

## 9. Claim classes

| Statement | Status |
|---|---|
| `Sigma_GM^+` is the one-sided no-`11` subshift | `EXACT_UPSTREAM` |
| `K_C` is its binary coding image | `EXACT_UPSTREAM` |
| coding map `pi` is continuous | `EXACT` |
| golden-mean constraint removes binary-expansion ambiguity | `EXACT` |
| `pi` is a homeomorphism `Sigma_GM^+ -> K_C` | `STANDARD_TOPOLOGY_APPLIED_EXACTLY` |
| `D o pi = pi o sigma` | `EXACT` |
| `(Sigma_GM^+,sigma)` and `(K_C,D|K_C)` are topologically conjugate | `EXACT` |
| `#Fix(D^n|K_C)=tr(A^n)=L_n` | `EXACT` |
| exact-period counts follow by Moebius inversion | `STANDARD_THEOREM_APPLIED_EXACTLY` |
| `zeta_AM(z)=1/det(I-zA)=1/(1-z-z^2)` | `STANDARD_SFT_THEOREM_APPLIED_EXACTLY` |
| radius `1/phi` recovers `h_top=ln(phi)` | `EXACT` |
| weighted `zeta_AM(z;s)=1/det(I-zM(s))` | `EXACT` |
| `P(s)=-ln z_c(s)` with `z_c(s)=2^s/phi` | `EXACT` |
| coding homeomorphism is a linear `E7,E8` intertwiner | `FALSE / TYPE_ERROR` |
| Artin-Mazur zeta equals Riemann zeta | `NOT_DERIVED / NOT_CLAIMED` |
| implication for RH | `NONE` |
| physical interpretation of dynamical zeta poles | `OPEN_NOT_CLAIMED` |
