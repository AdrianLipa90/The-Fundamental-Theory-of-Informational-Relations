# TIR Golden-Mean Transfer / κ Identity v0.1

Status: `EXACT_GOLDEN_MEAN_TRANSFER / EXACT_FIBONACCI_POWER_LAW / STANDARD_PERRON_FROBENIUS_ENTROPY / EXACT_KAPPA_ENTROPY_DIMENSION_IDENTITY / EXACT_LINEAR_INTERTWINER_NOGO / PHYSICAL_BINDING_OPEN`

Scope: pure symbolic dynamics, linear algebra, and normalization bookkeeping on the already-derived Collatz-admissible golden-mean phase language. No thermodynamic entropy, physical time rate, energy scale, mass scale, cosmological observable, or new fundamental constant is inferred.

## 1. Upstream exact inputs

The CP1/Collatz gate established the binary language

```math
\mathcal L_C=\{w\in\{0,1\}^*:11\not\subset w\}
```

and its compact phase envelope

```math
K_C\subset S^1\subset\mathbb{CP}^1
```

with

```math
\boxed{\dim_HK_C=\frac{\ln\varphi}{\ln2}=\log_2\varphi},
\qquad
\varphi=\frac{1+\sqrt5}{2}.
```

The homogeneous-fibration gate established the geometric vertical plane

```math
\mathfrak m=\operatorname{span}_{\mathbb R}\{E_7,E_8\}
```

and the axial isotropy generator `E6`.

The canonical TIR normalization surface independently gives

```math
\boxed{\kappa=\frac{\ln2}{24\pi}}.
```

The present note combines these already-established mathematical inputs without altering their claim classes.

## 2. Golden-mean transfer matrix

Use symbolic states labelled by the **current parity symbol** `0` and `1`. The forbidden word `11` gives the transition rules

```text
0 -> 0 or 1
1 -> 0 only.
```

Hence the adjacency/transfer matrix is

```math
\boxed{
A=\begin{pmatrix}
1&1\\
1&0
\end{pmatrix}.
}
```

Its characteristic polynomial is

```math
\chi_A(\lambda)=\lambda^2-\lambda-1,
```

so

```math
\boxed{
\operatorname{spec}(A)
=\left\{\varphi,-\varphi^{-1}\right\}.
}
```

The Perron-Frobenius spectral radius is therefore

```math
\boxed{\rho(A)=\varphi.}
```

A positive right Perron vector is

```math
\boxed{r=(\varphi,1)^T.}
```

Since `A` is symmetric, the same vector may be used on the left.

## 3. Exact Fibonacci power law

For `n>=1`,

```math
\boxed{
A^n=
\begin{pmatrix}
F_{n+1}&F_n\\
F_n&F_{n-1}
\end{pmatrix},
}
```

where `F_0=0`, `F_1=1`.

Consequently, for words of length `k>=1`,

```math
\boxed{
|\mathcal L_C(k)|
=\mathbf 1^T A^{k-1}\mathbf 1
=F_{k+2}.
}
```

Thus the Fibonacci count previously obtained combinatorially is exactly the path-count law of the transfer matrix.

## 4. Topological entropy

For the golden-mean shift of finite type, the standard entropy theorem gives

```math
h_{\rm top}=\ln\rho(A).
```

Therefore

```math
\boxed{h_{\rm top}=\ln\varphi.}
```

This is topological entropy of the symbolic dynamical system. It is not identified here with thermodynamic entropy or with an elapsed physical-time production rate.

The already-derived fractal dimension can therefore be written

```math
\boxed{
\dim_HK_C
=\frac{h_{\rm top}}{\ln2}.
}
```

## 5. Exact κ normalization identity

The canonical TIR normalization obeys

```math
24\pi\kappa=\ln2.
```

Substituting this into the entropy-dimension relation yields

```math
\dim_HK_C
=\frac{h_{\rm top}}{24\pi\kappa},
```

or equivalently

```math
\boxed{
h_{\rm top}
=24\pi\,\kappa\,\dim_HK_C.
}
```

For the golden-mean system,

```math
\boxed{
24\pi\,\kappa\,\log_2\varphi
=\ln\varphi.
}
```

This is an exact normalization identity. It does **not** derive `κ` from the golden-mean fractal; `κ` and `K_C` have independent upstream derivations, and the identity follows because both contain the same binary logarithmic unit `ln 2`.

One may define the derived quantity

```math
\boxed{
\kappa_\varphi
:=\kappa\,\dim_HK_C
=\frac{\ln\varphi}{24\pi}.
}
```

`κ_phi` is only a derived shorthand. It is not promoted to a new fundamental or fitted parameter.

## 6. Maximum-entropy Markov realization

The Perron vector gives the standard Parry transition matrix

```math
P_{ij}=\frac{A_{ij}r_j}{\varphi r_i}.
```

Explicitly,

```math
\boxed{
P=
\begin{pmatrix}
\varphi^{-1}&\varphi^{-2}\\
1&0
\end{pmatrix}.
}
```

Its stationary distribution is

```math
\boxed{
\pi_0=\frac{\varphi^2}{\varphi^2+1},
\qquad
\pi_1=\frac{1}{\varphi^2+1}.
}
```

The Shannon entropy rate of this Markov presentation is exactly

```math
\boxed{
h_\mu=\ln\varphi=h_{\rm top}.}
```

This is the standard measure of maximal entropy for the golden-mean shift. It is a symbolic-statistical statement only.

## 7. Normalized transfer spectrum

Normalize the transfer matrix by its Perron root:

```math
\widehat A=\frac{A}{\varphi}.
```

Then

```math
\boxed{
\operatorname{spec}(\widehat A)
=\left\{1,-\varphi^{-2}\right\}.
}
```

Thus the non-Perron linear mode alternates sign and contracts by the exact factor `phi^{-2}` per normalized transfer step.

No physical damping, oscillator decay, or relaxation time is inferred from this linear-algebraic fact.

## 8. Exact no-go: symbolic transfer is not the axial `6` generator

On the geometric vertical plane

```math
\mathfrak m=\operatorname{span}_{\mathbb R}\{E_7,E_8\},
```

the Hermitian-coordinate isotropy action is

```math
J_6:=-i\,\operatorname{ad}_{E_6}|_{\mathfrak m}.
```

Because

```math
-i[E_6,E_7]=E_8,
\qquad
-i[E_6,E_8]=-E_7,
```

its matrix in the ordered basis `(E7,E8)` is

```math
\boxed{
J_6=
\begin{pmatrix}
0&-1\\
1&0
\end{pmatrix},
}
```

with

```math
\boxed{\operatorname{spec}(J_6)=\{i,-i\}.}
```

By contrast,

```math
\operatorname{spec}(A)=\{\varphi,-\varphi^{-1}\}.
```

The spectra are disjoint. Therefore `A` and `J6` are not similar over `C` or `R`.

More strongly, the Sylvester intertwining equation

```math
\boxed{AT-TJ_6=0}
```

has only the zero solution

```math
\boxed{T=0}
```

because the spectra of `A` and `J6` are disjoint.

Hence there is no nonzero linear intertwiner that identifies the two symbolic states of the golden-mean transfer operator with the geometric `(E7,E8)` rotation representation while conjugating their dynamics.

This sharpens the existing firewall:

```math
\boxed{
\text{two symbolic states}\neq\text{the two geometric basis directions }E_7,E_8
}
```

unless an additional, differently typed nonlinear or enlarged-state construction is independently derived.

## 9. Operator typing

The two operators have different mathematical roles:

```math
A:
\text{symbolic transition/path-count operator},
```

```math
J_6:
\text{continuous infinitesimal axial rotation on the CP1 tangent plane}.
```

`A` has real hyperbolic/Perron spectrum; `J6` has purely imaginary rotational spectrum. Their shared dimension `2x2` is therefore only a dimension match, not an operator identity.

The fractal is preserved by the discrete symbolic/doubling dynamics, whereas the full continuous axial rotation group does not preserve `K_C` and in fact has trivial setwise stabilizer on it.

## 10. Claim classes

| Statement | Status |
|---|---|
| golden-mean adjacency matrix `A=[[1,1],[1,0]]` | `EXACT` |
| `spec(A)={phi,-1/phi}` and `rho(A)=phi` | `EXACT` |
| Fibonacci matrix-power identity | `EXACT` |
| `|L_C(k)|=F_{k+2}` from path counting | `EXACT` |
| `h_top=ln(phi)` | `STANDARD_THEOREM_APPLIED_EXACTLY` |
| `dim_H K_C=h_top/ln2` | `EXACT_DOWNSTREAM_CROSSWALK` |
| canonical `kappa=ln2/(24*pi)` | `EXACT_UPSTREAM_TIR_NORMALIZATION` |
| `h_top=24*pi*kappa*dim_H(K_C)` | `EXACT_NORMALIZATION_IDENTITY` |
| `kappa_phi=ln(phi)/(24*pi)` | `EXACT_DERIVED_SHORTHAND` |
| Parry transition matrix and stationary distribution | `STANDARD_THEOREM_APPLIED_EXACTLY` |
| symbolic entropy rate `h_mu=ln(phi)` | `STANDARD_THEOREM_APPLIED_EXACTLY` |
| normalized transfer spectrum `{1,-phi^-2}` | `EXACT` |
| geometric axial generator spectrum `{+i,-i}` | `EXACT_UPSTREAM_REPRESENTATION` |
| nonzero linear intertwiner `A T = T J6` | `FAIL` |
| literal identification of symbolic states with `E7,E8` | `NOT_DERIVED` |
| physical entropy/time/energy interpretation | `OPEN_NOT_CLAIMED` |

## 11. Validation requirements

A deterministic validator must:

1. verify the characteristic polynomial and exact eigenvalues of `A`;
2. verify the Fibonacci formula for `A^n` and the word-count identity;
3. verify the Perron vector and Parry transition matrix;
4. verify stationarity and the exact symbolic entropy-rate identity;
5. verify `dim_H K_C=ln(phi)/ln2` from the upstream receipt;
6. verify the pinned upstream `kappa=ln2/(24*pi)` receipt;
7. verify `h_top=24*pi*kappa*dim_H K_C` symbolically;
8. reconstruct `J6` from the parent adapted Gell-Mann basis;
9. verify `spec(J6)={+i,-i}` and disjointness from `spec(A)`;
10. solve the Sylvester equation and verify its nullspace is trivial;
11. re-run the golden-mean fractal and homogeneous-fibration validators.
