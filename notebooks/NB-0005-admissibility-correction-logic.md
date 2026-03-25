# NB-0005 Admissibility / Correction Logic

## Purpose
Executable scaffold for D-0005.

## Steps
1. compute closure tuple from Γ
2. compare C_H to ε_C
3. keep Γ if admissible
4. otherwise either reject or correct
5. test corrected closure defect

## Expected outputs
- admissible/reject/correct decision
- corrected channels if applicable
- closure tuple before and after correction

## TODO
- connect to state-to-phase-channels operator
- add anti-phase degeneracy examples
