# TIR CP1 Dyadic / Collatz-Admissible Fractal Gate v0.1

Status: `EXACT_DYADIC_COVERING / EXACT_UNREDUCED_COLLATZ_LANGUAGE / EXACT_GOLDEN_MEAN_SYMBOLIC_FRACTAL / EXACT_DIMENSION_LOG2_PHI / TERMINAL_PHASE_SET_COUNTABLE / PHYSICAL_FRACTAL_BINDING_OPEN`

Scope: pure symbolic and projective dynamics on the already-established `78` transverse `CP1` carrier. No physical horizon, cosmological fractal, measured spatial fractal dimension, or particle interpretation is asserted.

## 1. Upstream carrier and phase map

The principal-SU(2) theorem gives the exact axis-adapted split

```math
8=5+1+2
```

with the transverse two-real-dimensional sector

```math
SO(3)/SO(2)\cong S^2\cong \mathbb{CP}^1.
```

The Collatz-Fubini-Study phase interface imports the **unreduced** Collatz map

```math
C(n)=
\begin{cases}
n/2,&n\equiv0\pmod2,\\
3n+1,&n\equiv1\pmod2,
\end{cases}
```

and its parity itinerary

```math
b_k(n)=C^k(n)\bmod2.
```

For the canonical terminal-reaching phase coordinate,

```math
\zeta_C(n)=e^{2\pi i q_C(n)},
\qquad
\boxed{\zeta_C(Cn)=\zeta_C(n)^2}.
```

Thus the equatorial `CP1` carrier carries the degree-two phase map

```math
\boxed{F(\zeta)=\zeta^2}.
```

## 2. Full dyadic covering before Collatz admissibility

Writing

```math
\zeta=e^{2\pi i q},\qquad q\in\mathbb R/\mathbb Z,
```

gives

```math
\boxed{D(q)=2q\pmod1}.
```

The unrestricted inverse branches are

```math
g_0(q)=\frac q2,
\qquad
g_1(q)=\frac{q+1}{2}\pmod1.
```

At depth `k`, the unrestricted degree-two covering has `2^k` inverse phases.

This full inverse tree is a property of the circle map. It must not be conflated with the **Collatz-admissible** parity language.

The two inverse branch labels are also not identified with the coordinate basis vectors `E7,E8`; such an identification would require an additional intertwiner.

## 3. Exact local grammar of the unreduced Collatz map

If `n` is odd, then

```math
C(n)=3n+1
```

is even. Therefore every parity itinerary obeys

```math
\boxed{b_k=1\Longrightarrow b_{k+1}=0}.
```

Equivalently, the binary word

```text
11
```

is forbidden.

This is an exact local statement and does not depend on the Collatz conjecture.

Conversely, **every finite binary word containing no `11` occurs as the initial parity word of some positive integer**.

### Proof by the accelerated parity-vector map

Define the one-halving map

```math
T(n)=
\begin{cases}
n/2,&n\text{ even},\\
(3n+1)/2,&n\text{ odd}.
\end{cases}
```

For every `m>=1`, the length-`m` parity-vector map of `T` is a bijection

```math
\mathbb Z/2^m\mathbb Z\longleftrightarrow\{0,1\}^m.
```

Inductively:

- for an initial `0`, write `n=2r`; the tail is the parity vector of `r`;
- for an initial `1`, write `n=2r+1`; then `T(n)=3r+2`, and multiplication by `3` is invertible modulo `2^{m-1}`, so every desired tail has a unique `r mod 2^{m-1}`.

For the unreduced map `C`, a `T`-bit `0` corresponds to the one-step block

```text
0
```

while a `T`-bit `1` corresponds to the two-step block

```text
10
```

because

```math
n\text{ odd}\Longrightarrow
n\xrightarrow{C}3n+1\xrightarrow{C}(3n+1)/2=T(n).
```

Every finite binary word with no `11` can be uniquely parsed into the blocks `0` and `10` after appending one final `0` if the word ends in `1`. Hence the `T` parity-vector bijection realizes every such finite `C` word as a prefix.

Therefore the exact finite Collatz language is

```math
\boxed{\mathcal L_C=\{w\in\{0,1\}^*: 11\not\subset w\}}.
```

The number of allowed words of length `k` is

```math
\boxed{|\mathcal L_C(k)|=F_{k+2}},
```

where `F_k` is the Fibonacci sequence.

## 4. Golden-mean symbolic fractal envelope

Define the compact symbolic phase envelope

```math
\boxed{
K_C=
\left\{
\sum_{k\ge0}\frac{b_k}{2^{k+1}}:
 b_k\in\{0,1\},\ b_kb_{k+1}=0
\right\}.
}
```

This is the binary-image realization of the golden-mean subshift.

Every sequence in `K_C` either begins with `0`, or begins with the forced block `10`. Therefore

```math
\boxed{
K_C=f_0(K_C)\cup f_{10}(K_C)
}
```

with

```math
f_0(x)=\frac{x}{2},
\qquad
f_{10}(x)=\frac12+\frac{x}{4}.
```

The maximum admissible binary sequence is

```text
10101010...
```

so

```math
\max K_C=\frac23.
```

Consequently,

```math
f_0(K_C)\subset[0,1/3],
\qquad
f_{10}(K_C)\subset[1/2,2/3].
```

The images are strictly separated by the open gap `(1/3,1/2)`. Thus the strong separation condition holds.

## 5. Exact Hausdorff/similarity dimension of the admissible envelope

The contraction ratios are

```math
r_0=\frac12,
\qquad
r_{10}=\frac14.
```

By the standard self-similar-set dimension theorem under strong separation, the Hausdorff dimension `d_C` is the unique solution of

```math
\left(\frac12\right)^{d_C}
+
\left(\frac14\right)^{d_C}
=1.
```

Let

```math
x=2^{-d_C}.
```

Then

```math
x+x^2=1,
```

so

```math
x=\frac{\sqrt5-1}{2}=\frac1\varphi,
\qquad
\varphi=\frac{1+\sqrt5}{2}.
```

Therefore

```math
\boxed{
\dim_H K_C
=\frac{\ln\varphi}{\ln2}
=\log_2\varphi
\approx0.6942419136.
}
```

This is a non-integer symbolic/projective fractal dimension derived from the unreduced Collatz parity constraint, with no fitted parameter.

Equivalently, the word-count growth

```math
F_{k+2}\sim\frac{\varphi^{k+2}}{\sqrt5}
```

has topological entropy

```math
h_{top}=\ln\varphi,
```

and

```math
\dim_H K_C=\frac{h_{top}}{\ln2}.
```

## 6. What is — and is not — the fractal here

There are three differently typed sets:

### A. Full circle dynamics

The map

```math
F(z)=z^2
```

has the standard Julia set

```math
\boxed{J(F)=S^1}
```

with Hausdorff dimension `1`.

### B. Collatz-admissible symbolic envelope

The forbidden word `11` restricts the binary phase language to `K_C`, with

```math
\boxed{\dim_H K_C=\log_2\varphi<1}.
```

This is the nontrivial fractal established here.

### C. Canonical terminal-reaching IDT phase set

IDT currently promotes `q_C(n)` canonically for trajectories reaching the terminal cycle. Since the positive integers are countable, the set of those individual canonical phase points is countable and therefore has Hausdorff dimension `0`.

The present theorem does **not** claim that the closure of terminal-reaching phase points equals all of `K_C`. Establishing that density would require a separate theorem and must not be inferred from the Collatz conjecture or from finite numerical checks.

Thus the fractal statement applies to the exact **local-admissibility closure / symbolic envelope**, not to the raw countable set of terminal phase points.

## 7. Finite-prefix density for unrestricted positive-integer parity itineraries

Section 3 proves that every finite admissible cylinder `w` with no `11` is realized by a positive integer orbit prefix.

Therefore, if the binary itinerary sum is considered purely mathematically for all positive integers (without requiring terminal arrival), the set of positive-integer parity codes intersects every cylinder of the golden-mean shift. Its symbolic closure is exactly `K_C`.

This is a mathematical extension of the parity code. It does not alter the canonical IDT claim boundary, which currently binds the named phase interface to terminal-reaching trajectories.

## 8. Relation to the `78` carrier

The typed chain now supported is

```math
\boxed{
78\text{ transverse }CP1\text{ carrier}
\longrightarrow
S^1\text{ phase section}
\longrightarrow
\text{unreduced Collatz parity grammar}
\longrightarrow
K_C
}
```

with

```math
\boxed{
\dim_H K_C=\log_2\varphi.
}
```

This is substantially stronger than the unrestricted `2^k` inverse tree: the Collatz grammar removes the `11` cylinders and leaves a genuine Cantor-like self-similar subset.

It still does not identify the two coordinate directions `E7,E8` with the two symbolic branch labels; that requires an independent intertwiner.

## 9. Historical claim firewall

An archived pre-canonical MetaTheory text contains a historical numerical statement assigning a different Hausdorff dimension to a Collatz IFS. That archival number is **not imported**.

The canonical value derived here follows solely from:

1. the explicit unreduced Collatz rule;
2. the exact local prohibition `11`;
3. the resulting self-similar maps `x/2` and `1/2+x/4`.

No observational target or fitted parameter enters the derivation.

## 10. Claim classes

| Statement | Status |
|---|---|
| `78` sector is a real two-dimensional `CP1` transverse carrier | `EXACT_UPSTREAM` |
| imported phase dynamics `zeta -> zeta^2` | `EXACT_UPSTREAM` |
| unrestricted circle map is degree two | `EXACT` |
| unreduced Collatz parity forbids `11` | `EXACT` |
| every finite `11`-free word is realizable as a positive-integer orbit prefix | `EXACT` |
| number of allowed length-k words is `F_{k+2}` | `EXACT` |
| admissible symbolic envelope obeys `K=f0(K) union f10(K)` | `EXACT` |
| strong separation of the two self-similar pieces | `EXACT` |
| `dim_H K_C = log_2(phi)` | `STANDARD_THEOREM_APPLIED_EXACTLY` |
| Julia set of `z^2` is `S1`, dimension `1` | `STANDARD_EXACT_COMPLEX_DYNAMICS` |
| canonical terminal-reaching phase-point set is countable, dimension `0` | `EXACT` |
| closure of terminal-reaching phase points equals `K_C` | `OPEN` |
| inverse symbolic branches are literally `E7,E8` | `NOT_CLAIMED` |
| archived numerical fractal dimension imported into canon | `NO` |
| physical/cosmological fractal binding | `OPEN` |
