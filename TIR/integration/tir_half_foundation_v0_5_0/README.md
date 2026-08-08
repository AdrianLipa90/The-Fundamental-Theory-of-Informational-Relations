# TIR × Secret-of-a-Half Foundation / PhaseNav v0.5.0

Status: `PASS` integration snapshot.

This directory records the recovered dependency boundary between TIR and
Secret-of-a-Half without promoting open claims to canon.

## Recovered information/phase chain

- `Delta I_cycle = ln(2)/12`
- `dI/dt = (ln(2)/12) f`
- `dphi/dt = C f`
- `kappa_C = (ln(2)/12)/C`
- for radians `C=2*pi`:
  `kappa = ln(2)/(24*pi)`

`kappa` is therefore tracked as project-derived exact algebra, not an
unparented arbitrary literal. The earlier RAW receipt for the twelve-cycle
normalization is still a provenance item to recover.

## Discrete charged-lepton generator

The three previously frozen pre-benchmark gates factor into

`G(h,a,b,c) = h/2 + a*kappa + b*kappa/L3 + c*kappa^2/2`.

Recovered states:

- electron action: `(1,-3,+1,-1)`
- e->mu release: `(0,L5,L4,L3+1)`
- mu->tau release: `(0,3,-1,-L3)`

with project arithmetic definitions:

- `L3 = CollatzDepth(3) = 7`
- `L4 = 5-3 = 2`
- `L5 = 5`

Measured electron/muon/tau masses are scoring-only and are not parents of these
derivation gates.

## Current debt boundary

Coefficient magnitude audit:

- unparented magnitudes: `0`
- project-level role/orientation assignments still open: `10`

The remaining generator problem is therefore:

`geometry / holonomy -> sign + orientation + semantic role -> (h,a,b,c)`

rather than fitting another continuous F/D family.

Secret-of-a-Half proof firewall remains unchanged:
`xi-zero -> canonical/native closure` is still OPEN.

## PhaseNav receipt

- graph nodes: `83`
- graph edges: `89`
- graph paths: `7`
- graph sha256: `b2fec0c566aac74c7b62af6911cbbabc7c2785db231ef05487c55ea52d900328`
- action-lattice Berry holonomy: `3.4093526061025701e-05`

The intrinsic coefficient lattice is 4D. The PhaseNav routing/holonomy envelope
is 36D. These spaces are not identified.

No canon promotion is implied by this integration snapshot.
