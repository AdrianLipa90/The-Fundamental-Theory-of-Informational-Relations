# NB-0006 Minimal Dynamics / Update Step

## Purpose
Executable scaffold for D-0006.

## Steps
1. define current channel state Γ_n
2. define increment vector V_n and step size dt
3. compute proposed step Γ_prop
4. evaluate closure before and after step
5. apply update mode:
   - accept_if_nonworsening
   - rollback
   - correct
6. record accepted output Γ_{n+1}

## Expected outputs
- proposed channels
- accepted channels
- closure tuple before and after
- acceptance mode/result flags

## TODO
- connect channel dynamics to state-level update proposals
- compare rollback vs correction trajectories over multiple steps
