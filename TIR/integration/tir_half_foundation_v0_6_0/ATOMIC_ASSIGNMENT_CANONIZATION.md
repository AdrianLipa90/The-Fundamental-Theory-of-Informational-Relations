# Atomic Assignment Canonization v0.6

Status: `PASS_WITH_OPEN_TIR_BINDING`.

This layer continues the merged TIR × Secret-of-a-Half v0.5 foundation. It does not fit masses and does not consume a known coefficient tuple as an input.

## 1. Four-slot role routing

For

`G(h,a,b,c) = h/2 + a*kappa + b*kappa/L3 + c*kappa^2/2`,

the source roles are now structurally routed as:

- `h <- projective CP1 / spin-half identity`;
- `a <- twin-prime generation seed + Ramanujan admissibility/release`;
- `b <- Collatz terminal / return / orbit layer`;
- `c <- tetrahedral -> Poincare -> Berry curvature/holonomy layer`.

Status: `STRUCTURAL_ROLE_ROUTING_PASS`.

This closes which source layer owns each slot. It does not yet prove the numerical tuple for every sector.

## 2. Pre-coefficient orientation operator

The current CIEL orbital runtime implements

`spin = tanh(-alpha_s * dV_dphi)`

with `dV_dphi` obtained as a central finite difference of the total relational potential. For every `alpha_s > 0`, `tanh` is odd and strictly increasing, therefore

`orientation_gradient = sign(-dV_dphi)`.

The sign is independent of the magnitude of positive `alpha_s`.

The orbital source model independently defines each first-class relation as `attractor -> satellite`; its system mean phase uses outgoing phase shifts positively and incoming/satellite phase shifts negatively. This supplies a second pre-coefficient orientation convention.

These rules are implemented project operators. Their binding to a particular TIR coefficient slot remains `CANDIDATE_TIR_BINDING` until prospective validation.

## 3. Circularity firewall

The atomic assignment input MUST NOT contain:

- observed masses or PDG masses;
- fitted Yukawa values;
- target action or target release;
- an already known `(h,a,b,c)` tuple;
- a PhaseNav envelope generated from that tuple;
- residual-to-target information.

A 36D PhaseNav envelope is an output/routing representation of the atomic state, not evidence from which the same state may be derived.

## 4. Retrospective Collatz pattern — NOT CANON

The no-mass-input generation assignment supplies the structural centers and ordinary stopping lengths:

- generation 1: `(3,5)`, center `4`, `ell=2`;
- generation 2: `(11,13)`, center `12`, `ell=9`;
- generation 3: `(5,7)`, center `6`, `ell=8`.

For the two recovered charged-lepton transitions one observes retrospectively:

`sign(b,c) = sign(ell_destination - ell_source)`

and

`abs(c) = ell_destination - 1`.

Thus e->mu gives positive orientation and `|c|=8`, while mu->tau gives negative orientation and `|c|=7`.

This has only two examples and was noticed after the recovered coefficient states were known. Its status is therefore `RETROSPECTIVE_CANDIDATE_NEEDS_PROSPECTIVE_TEST`, not canon.

## 5. Next gate

The next valid test is prospective:

`pre-coefficient atomic/orbital geometry -> relational gradient + directed orbit + holonomy -> orientation/sign -> coefficient assignment`.

The transition input must be frozen before reading its recovered coefficient tuple or any mass target.

Secret-of-a-Half proof debts `SOH-C004` and `SOH-C005` remain OPEN.