# NB-0004 State to Phase Channels

## Purpose
Executable scaffold for D-0004.

## Steps
1. Vectorize ψ to Bloch coordinates
2. Extract (theta, phi)
3. Handle poles deterministically
4. Feed channels into closure operator

## Expected outputs
- Γ(ψ) = (theta, phi)
- pole metadata
- closure tuple (Δ_H, R_H, C_H)

## TODO
- add composite state-to-closure examples
- compare gauge-equivalent inputs
