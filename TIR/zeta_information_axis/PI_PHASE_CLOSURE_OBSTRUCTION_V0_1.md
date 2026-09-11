# Pi as a Phase-Closure Constant and Representation Obstruction v0.1

Status: `EXACT_TOPOLOGICAL_CORE / RESTRICTED_REPRESENTATION_OBSTRUCTION / NONLOCALITY_BRIDGE_OPEN`

Date: 2026-09-11

Parent module: `TIR/zeta_information_axis`

## 1. Scope

This note isolates the mathematical role of `pi` in recurrent phase geometry without promoting the stronger statement that `pi` causes Goedel incompleteness or quantum nonlocality.

The exact core is:

1. recurrence can be defined before radians as `q in R/Z`;
2. the radian representation is `phi = 2*pi*q`;
3. winding and `U(1)` holonomy close modulo `2*pi`;
4. spin-1/2 lifts the projective recurrence to a `4*pi` spinor-sheet recurrence;
5. `pi` is irrational and transcendental in every positional radix, so no finite rational positional expansion represents it exactly;
6. this is a representation obstruction only for systems restricted to finite rational numerics. It is not an obstruction to exact symbolic mathematics, which can carry `pi` as a defined constant.

## 2. Radix invariance

Changing the positional base does not change whether a real number is rational, irrational, algebraic, or transcendental.

Therefore `pi` remains irrational and transcendental in base 10, base 12, base 60, and every integer radix `b > 1`.

For any such base,

```text
x in Q  <=>  the radix-b expansion of x is eventually periodic.
```

Hence the radix expansion of `pi` is infinite and non-eventually-periodic in every integer base.

This blocks only a finite rational positional encoding of `pi`; it does not block exact symbolic representation.

## 3. Winding closure

Let the recurrent coordinate be

```text
q in R/Z.
```

Its standard radian representative is

```text
phi = 2*pi*q.
```

For a closed loop `gamma`, the winding number is

```text
w(gamma) = (1/(2*pi)) * integral_gamma dphi  in Z.
```

Thus `2*pi` is the radian closure period, while the topological invariant itself is the integer winding. The recurrence exists independently of the choice of radians; `pi` enters when the normalized cycle is represented on the real angular line.

This refines the existing TIR distinction between intrinsic recurrence and angular representation.

## 4. U(1) holonomy

For a `U(1)` connection `A`, the loop holonomy is

```text
U_gamma = exp(i * integral_gamma A)
        = exp(i * theta_gamma),
```

with

```text
theta_gamma ~ theta_gamma + 2*pi*n.
```

Therefore `2*pi` is the phase-identification period of the angular representative.

At half-turn phase,

```text
theta_gamma = pi mod 2*pi
```

gives

```text
U_gamma = -1.
```

This covers the already-recorded Berry/Aharonov-Bohm common `U(1)` holonomy class without identifying their physical gauge potentials.

## 5. Spinor double cover

For spin-1/2,

```text
2*pi rotation  ->  spinor sign flip,
4*pi rotation  ->  spinor-sheet restoration.
```

The projective ray is already recurrent after the `2*pi` rotation, whereas the lifted spinor state requires `4*pi` for literal state-vector closure.

This is the standard `SU(2) -> SO(3)` double-cover distinction. It must not be conflated with a generic Berry phase unless the relevant loop and connection are explicitly identified.

## 6. What the obstruction actually is

A system restricted to finite rational positional numerics cannot store `pi` exactly. Any such implementation uses a rational approximation

```text
pi_N in Q,
```

with nonzero residual

```text
Delta_pi = pi - pi_N != 0.
```

Consequently, if exact angular closure is implemented only by finite rational numerics, the represented closure constant carries a nonzero numerical residual.

This is a genuine **representation obstruction under the stated restriction**.

It is not a theorem that all discrete formal systems fail to close because of `pi`. Exact symbolic systems can represent `pi` by a symbol together with defining identities, convergent constructions, or analytic specifications. The distinction is therefore:

```text
finite rational numerical representation  -> exact pi unavailable,
exact symbolic formal representation      -> exact pi available as a defined object.
```

## 7. Goedel boundary

`pi` is not a Goedel number in the standard technical sense. A Goedel number is a natural-number encoding of syntax, formulas, or proofs under a chosen arithmetization.

Likewise, Goedel incompleteness is not caused by `pi`. It arises from the expressive strength and self-referential arithmetization of sufficiently strong consistent effectively axiomatized formal systems.

The valid TIR statement is narrower:

```text
pi is a closure constant for standard continuous phase geometry,
and a finite-rational numerical implementation cannot represent that constant exactly.
```

Any analogy between this residual and formal incompleteness is interpretive and is not promoted here.

## 8. Nonlocality boundary

Quantum nonlocality is not established to be caused by `pi`.

Angular quantum correlations can contain phase geometry, for example correlations of the form

```text
E(a,b) = -cos(theta),
```

and Bell/CHSH-optimal settings can involve angles such as `pi/4`. In a TIR model where nonlocal relational structure is encoded through a phase connection or holonomy, `pi` necessarily enters the radian representation of that phase geometry.

That gives the conditional bridge

```text
nonlocal relational phase model
    -> phase/holonomy geometry
    -> 2*pi periodic angular representation.
```

It does **not** establish the converse statement that `pi` generates or explains quantum nonlocality.

Status: `MODEL BRIDGE / OPEN PHYSICAL INTERPRETATION`.

## 9. Closure statement

The exact statement supported by the current formalism is

```text
normalized recurrence q in R/Z
    -> radian representative phi = 2*pi*q
    -> winding normalization by 2*pi
    -> U(1) phase identification modulo 2*pi
    -> spin-1/2 lifted closure at 4*pi.
```

Hence `pi` should be treated in TIR as a **phase-closure constant of the radian representation**.

The stronger phrase "pi prevents system closure" is valid only after specifying a restricted representation class, e.g. finite rational positional numerics. It is not a general theorem about mathematics, formal systems, or physics.

## 10. Relation to existing TIR claims

This note refines, but does not rewrite, the existing claim chain:

```text
C-020  normalized recurrence before radians
C-021  spin-1/2 double cover
C-024  conditional kappa reconstruction with C = 2*pi
C-015  Berry/AB common U(1) holonomy class
C-018  canonical pi holonomic zero-closure remains OPEN
```

No Riemann-hypothesis, nonlocality, Standard-Model, GR, cosmology, QPU, or physical-laboratory claim is promoted by this note.
