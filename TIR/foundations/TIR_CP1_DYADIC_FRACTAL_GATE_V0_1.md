# TIR CP1 Dyadic Fractal Gate v0.1

Status: `EXACT_DYADIC_COVERING / EXACT_BINARY_PREIMAGE_TREE / EXACT_IFS_DIMENSION_ONE / NONTRIVIAL_FRACTAL_GEOMETRY_NOT_DERIVED`

Scope: pure dynamics on the already-established `78` transverse `CP1` carrier. No physical horizon, cosmological fractal, measured fractal dimension, or particle interpretation is asserted.

## 1. Upstream carrier

The principal-SU(2) theorem gives the exact axis-adapted split

```math
8=5+1+2
```

with the transverse two-real-dimensional sector

```math
SO(3)/SO(2)\cong S^2\cong \mathbb{CP}^1.
```

The Collatz-Fubini-Study phase interface independently supplies

```math
\zeta_C(Cn)=\zeta_C(n)^2,
\qquad |\zeta_C|=1.
```

Therefore the canonical phase dynamics on the equatorial `CP1` section is

```math
\boxed{F(\zeta)=\zeta^2}.
```

## 2. Exact two-sheeted covering

Writing

```math
\zeta=e^{2\pi i q},\qquad q\in\mathbb R/\mathbb Z,
```

gives the angle-doubling map

```math
\boxed{D(q)=2q\pmod1}.
```

Each phase has exactly two inverse phase branches,

```math
g_0(q)=\frac q2,
\qquad
g_1(q)=\frac{q+1}{2}
\pmod1.
```

Thus `F:S1->S1` is a degree-two covering. After `k` inverse levels, a phase `q_*` has exactly

```math
\boxed{2^k}
```

preimages

```math
q_{k,m}=\frac{q_*+m}{2^k},
\qquad m=0,\ldots,2^k-1
\pmod1.
```

This is an exact dyadic self-similar **branching hierarchy**.

The two inverse branches are branch labels of the covering map. They are not identified with the coordinate basis vectors `E7,E8`; such an identification would require an additional intertwiner and is not claimed.

## 3. The natural inverse IFS is not a nontrivial fractal

On the lifted phase interval `[0,1]`, the two contractions are

```math
g_0([0,1])=[0,1/2],
\qquad
g_1([0,1])=[1/2,1].
```

Hence

```math
\boxed{g_0([0,1])\cup g_1([0,1])=[0,1]}.
```

The IFS attractor is the full interval, not a Cantor-type proper subset.

Its similarity-dimension equation is

```math
2\left(\frac12\right)^d=1,
```

so

```math
\boxed{d=1}.
```

Therefore the canonical dyadic inverse system has integer Hausdorff/similarity dimension one.

## 4. Complex dynamics of z^2

For the polynomial

```math
F(z)=z^2,
```

iteration gives

```math
F^{\circ k}(z)=z^{2^k}.
```

Therefore

- if `|z|<1`, then `F^k(z)->0`;
- if `|z|>1`, then `|F^k(z)|->infinity`;
- if `|z|=1`, then every iterate remains on the unit circle.

The boundary between the two basins is exactly

```math
\boxed{J(F)=S^1},
```

the standard Julia set of `z^2`. Its Hausdorff dimension is exactly one.

Thus the currently imported nonlinear map is degree two and dynamically nontrivial, but it still does **not** generate a non-integer-dimensional fractal set.

## 5. What survives from the "78 fractal" intuition

The following typed statement is exact:

```math
\boxed{
78\text{ transverse }CP1\text{ carrier}
\;\longrightarrow\;
\zeta\mapsto\zeta^2
\;\longrightarrow\;
2^k\text{ inverse-branch hierarchy}.
}
```

This establishes dyadic recursive branching on the higher two-dimensional carrier.

It does not establish a nontrivial geometric fractal.

## 6. Finite rotations do not change the verdict

The existing polygonal action

```math
R_N:z\mapsto e^{2\pi i/N}z
```

has finite order `N`, and the existing `C3 x Z2` lift has finite order six. Composing these finite/compact rotational actions with the carrier does not by itself introduce a contractive Cantor IFS or a new rational-map critical orbit.

Likewise, the DII transports are unitary `SU(2)` actions. On `CP1` they are Möbius automorphisms of degree one. Composition of them remains degree one.

Therefore a nontrivial fractal cannot be attributed to the existing compact transport sector alone.

## 7. Historical claim firewall

An archived pre-canonical MetaTheory text contains an historical statement assigning a numerical Hausdorff dimension to a Collatz IFS. That archival number is not imported here. The present canonical interface is tested from its explicit operator `zeta -> zeta^2`, for which the exact invariant set above has dimension one.

Any future non-integer dimension must be re-derived from a separately specified canonical operator and ambient metric.

## 8. What would be sufficient for a nontrivial fractal

A future gate may promote `FRACTAL_DYNAMICS` only if TIR independently derives at least one of:

1. a proper restricted branch language/subshift whose invariant set is a strict self-similar subset;
2. a coefficient-free contractive IFS with a nontrivial attractor;
3. a rational map `R:CP1->CP1` of degree at least two whose critical orbit is not conjugate to the trivial `z^d` circle case;
4. a hyperbolic/noncompact transport semigroup with a derived fractal limit set.

No fitted parameter may be inserted solely to obtain a desired dimension.

## 9. Claim classes

| Statement | Status |
|---|---|
| `78` sector is a real two-dimensional `CP1` transverse carrier | `EXACT_UPSTREAM` |
| imported phase dynamics `zeta -> zeta^2` | `EXACT_UPSTREAM` |
| angle doubling / two inverse branches | `EXACT` |
| depth-k preimage count `2^k` | `EXACT` |
| dyadic recursive branching hierarchy | `EXACT` |
| natural inverse IFS attractor is `[0,1]` | `EXACT` |
| natural IFS similarity dimension is `1` | `EXACT` |
| Julia set of `z^2` is `S1`, dimension `1` | `STANDARD_EXACT_COMPLEX_DYNAMICS` |
| current `78` geometry has a non-integer fractal dimension | `FAIL_NOT_DERIVED` |
| archived numerical fractal dimension imported into canon | `NO` |
| future nontrivial fractal dynamics | `OPEN` |
