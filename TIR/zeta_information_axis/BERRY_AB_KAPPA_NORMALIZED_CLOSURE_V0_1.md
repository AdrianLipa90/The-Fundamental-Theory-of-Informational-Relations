# Berry–Aharonov–Bohm Normalized Closure and κ Structural Promotion v0.1

Status: `EXACT_NORMALIZED_U1_CLOSURE / TIR_INTERNAL_KAPPA_STRUCTURE_CLOSED / PHYSICAL_UNIVERSALITY_SEPARATE / ZERO_STATE_BRIDGE_OPEN`

Date: 2026-09-11

Parents:
- `PI_PHASE_CLOSURE_OBSTRUCTION_V0_1.md`
- `NORMALIZED_PHASE_CLOSURE_TEST_V0_1.md`
- `TIR/foundations/TIR_KAPPA_FLAVOUR_MIXING_NORMALIZATION_V0_1.md`

## 1. Question

After removing radians as the primary phase coordinate, do the Berry and Aharonov–Bohm sectors still require `pi` intrinsically, and does the normalized form close the outstanding `ln(2)/12` structural step in the current κ chain?

The calculation must keep four layers distinct:

1. exact `U(1)` quotient geometry;
2. the standard radian chart;
3. TIR-internal structural premises;
4. external physical universality.

## 2. Berry phase in normalized turns

For the latitude convention already implemented in the information-spinor module,

```text
gamma_B = -2*pi*(1-sigma).
```

Define the normalized turn class

```text
q_B = gamma_B/(2*pi) mod 1.
```

Then exactly

```text
q_B = -(1-sigma) mod 1.
```

No numerical evaluation of `pi` is needed for this quotient relation.

At the balanced point,

```text
sigma = 1/2,
q_B = -1/2 mod 1 = 1/2,
```

and therefore

```text
U_B = exp(2*pi*i*q_B) = -1.
```

The exact invariant statement is therefore the half-turn class

```text
q_B = 1/2 in R/Z,
```

while the familiar radian representative is

```text
gamma_B = pi mod 2*pi.
```

Thus `pi` is not an intrinsic Berry-closure obstruction. It is the radian measure of the exact half-turn class.

## 3. Aharonov–Bohm phase in normalized turns

For charge `Q`, flux `Phi`, and flux quantum

```text
Phi_0 = h/Q,
```

the standard Aharonov–Bohm phase can be written

```text
gamma_AB = Q*Phi/hbar
         = 2*pi*(Phi/Phi_0).
```

Define

```text
q_AB = gamma_AB/(2*pi) mod 1.
```

Then

```text
q_AB = Phi/Phi_0 mod 1.
```

Again, the exact quotient coordinate does not require a numerical value of `pi`.

For half a flux quantum,

```text
Phi/Phi_0 = 1/2,
q_AB = 1/2,
U_AB = -1.
```

For an integer flux quantum,

```text
Phi/Phi_0 in Z,
q_AB = 0 mod 1,
U_AB = +1.
```

## 4. Common normalized holonomy class

The balanced Berry loop and the half-flux Aharonov–Bohm loop therefore occupy the same exact `U(1)` quotient class:

```text
q_B = q_AB = 1/2 mod 1
```

and both yield

```text
U = -1.
```

This promotes the common half-turn holonomy class, not an identification of their physical connections or potentials.

The physical mechanisms remain distinct:

```text
Berry: geometry of state-space transport
AB: electromagnetic gauge connection / enclosed flux
```

The common object is the `U(1)` holonomy class.

## 5. Normalized κ structure

The parent TIR κ derivation already fixes the three-flavour carrier and mixing algebra:

```text
N_F = 3,
dim su(3) = 3^2 - 1 = 8.
```

Hence the canonical TIR mixing-channel count is

```text
N_mix = N_F * dim su(3)
      = 3*8
      = 24.
```

In normalized turns, the primitive half-turn is exactly

```text
Delta q_(1/2) = 1/2.
```

One half-turn for each of the 24 canonical mixing channels gives the total normalized mixing measure

```text
Q_mix = N_mix * Delta q_(1/2)
      = 24*(1/2)
      = 12.
```

The balanced binary information unit is

```text
I_* = ln(2).
```

Therefore the TIR information normalization per normalized mixing turn is

```text
kappa_q = I_*/Q_mix
        = ln(2)/12.
```

This is not an additional fitted integer and it is not obtained by numerically approximating `pi`. It is the normalized-turn form of the already canonical parent TIR flavour-mixing construction.

## 6. Radian κ as a coordinate image

With

```text
phi = 2*pi*q,
dq/dphi = 1/(2*pi),
```

the radian information-phase coefficient is

```text
kappa_phi = kappa_q * dq/dphi
          = (ln(2)/12)/(2*pi)
          = ln(2)/(24*pi).
```

Thus the exact dependency chain becomes

```text
binary balance
    -> I_* = ln(2)
three-flavour SU(3)_F structure
    -> N_mix = 3*(3^2-1) = 24
normalized half-turn
    -> Delta q = 1/2
    -> Q_mix = 12
    -> kappa_q = ln(2)/12
radian chart phi = 2*pi*q
    -> kappa_phi = ln(2)/(24*pi)
```

Under the existing TIR structural premises, the coefficient is therefore structurally determined.

## 7. Candidate-status consequence

The repository's live `TIR/CLAIM_HIERARCHY.md` already classifies

```text
kappa = ln(2)/(24*pi)
```

as a Class-B `TIR-internal derived structural normalization`, not as a prospective Class-E candidate.

The normalized-turn calculation explains why that classification is the consistent one: the formerly isolated `ln(2)/12` step is recovered from the canonical 24-channel structure and the exact half-turn.

Therefore, for the κ normalization itself:

```text
candidate status -> NOT NEEDED inside the TIR internal dependency graph
structural Class B -> RETAIN
```

This does not convert the TIR information-phase law into an externally established law of nature. Empirical universality and physical realization remain separate validation questions.

It also does not alter unrelated prospective Class-E predictions in the repository.

## 8. What remains open

This closure does not solve the separate zeta zero-state bridge.

In particular, it does not prove that

```text
canonical nontrivial zeta zerohood
    -> balanced U(1) half-turn holonomy
```

without an independent zeta-derived state/operator construction.

Therefore the historical C-018/C-007/C-008 debts remain open unless and until that bridge is derived without assuming the critical line.

Likewise, no causal explanation of Bell nonlocality follows merely from rewriting its phase variables in normalized turns.

## 9. Verdict

```text
V1: Berry half-turn class can be written exactly without numeric pi      PASS
V2: AB flux phase can be written exactly as Phi/Phi_0 mod 1             PASS
V3: balanced Berry and half-flux AB share q=1/2 and U=-1                PASS
V4: common U(1) class identifies the physical potentials                FAIL / NOT CLAIMED
V5: canonical TIR N_mix=24 and half-turn 1/2 give Q_mix=12              PASS
V6: normalized TIR coefficient is kappa_q=ln(2)/12                      PASS within TIR premises
V7: radian coefficient is kappa_phi=ln(2)/(24*pi) by Jacobian           PASS
V8: kappa itself needs prospective candidate status inside TIR          FAIL
V9: kappa is externally established universal physics                   OPEN / NOT CLAIMED
V10: zeta zerohood is thereby derived                                   FAIL / OPEN
```

Final classification:

```text
pi = radian chart scale
half-turn = intrinsic normalized class 1/2
Berry/AB common closure = U(1) class 1/2, not common physical potential
kappa_q = ln(2)/12 = TIR-internal structural normalization
kappa_phi = ln(2)/(24*pi) = radian-coordinate image
kappa candidate status inside TIR = superseded by structural Class B
external physical universality = separate evidence question
zeta zero-state bridge = OPEN
```

## 10. Executable witness

Implementation:

```text
src/critical_axis/phase_closure.py
```

Tests:

```text
tests/test_phase_closure.py
```

The discrete closure and channel-count factors use exact integer/Fraction arithmetic. Floating-point `pi` appears only in numerical cross-checks of the radian representation, not in the exact normalized structural closure.
