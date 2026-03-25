# NB-0003 State / Phase Vectorization

## Purpose
Executable scaffold for D-0003.

## Steps
1. Normalize ψ
2. Build projector ρ = |ψ><ψ|
3. Compute Bloch components via Pauli expectations
4. Verify unit norm
5. Extract angular chart (theta, phi)

## Expected outputs
- Bloch vector n = (n_x, n_y, n_z)
- (theta, phi)
- gauge-invariance check summary

## TODO
- connect downstream phase-channel extraction operator
- add pole-handling metadata for chart singularities
