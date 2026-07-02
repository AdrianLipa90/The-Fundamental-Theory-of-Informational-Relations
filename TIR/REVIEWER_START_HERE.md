# Reviewer Orientation — Metatime

## What this repository is
A **low-parameter phenomenological ansatz** (not a complete derivation) expressing Standard Model parameters through geometric phase information theory using:
- κ = ln2/(24π) — information constant
- L₃=7, L₄=2, L₅=5 — integer L-constants
- q = {u:3, d:5, s:7, c:11, b:13, t:17} — quark primes
- 2 external scales (E_P, E_proton) + 3 external inputs (N_c, Y_L, Crewther)

## Quick start
```bash
python3 TIR/metatime_audit.py      # Full formula ledger + free param audit
python3 TIR/run_reproducibility.py  # One-command reproducibility (if created)
```

## Repository structure
```
TIR/
├── metatime_audit.py         # Core solver: all formulas → predictions → PDG comparison
├── metatime_paper.tex        # Paper source
├── metatime_paper.pdf        # Compiled paper
├── monograph/                # Extended monograph
├── system_map_complete.md    # Architecture map
├── STRUCTURAL_CHOICES.md     # Full structural-choice audit
├── CLAIM_HIERARCHY.md        # Theorem/prediction/coincidence classification
├── FALSIFIABILITY.md         # Falsification criteria + nEDM table
│
archive/                      # Version timeline
├── TIMELINE.md               # v7.0 → v7.8 → v7.9 → v7.9r1 → v10_final
├── v7.8/{full,slim}/         # M₀ derived, GMO standardized
├── v7.9/{full,slim}/         # CKM, gauge bosons, strong CP, DE
├── v7.9r1/slim/              # CKM refinement
├── v10_final/slim/           # α derived, final version
├── originals/                # SHA-verified original zips
```

## What to review
1. `metatime_audit.py` line by line — every formula has an auditable code path
2. `STRUCTURAL_CHOICES.md` — is every structural choice accounted for?
3. `FALSIFIABILITY.md` — especially nEDM (factor 10 above bound)
4. Gauge boson sector (M_W/M_Z ~4% systematic error)
5. `archive/TIMELINE.md` — derivation history with version diffs

## What this is NOT
- NOT a complete derivation from first principles (see STRUCTURAL_CHOICES.md)
- NOT a zero-free-parameter theory (see CLAIM_HIERARCHY.md)
- NOT peer-reviewed beyond first + second stage reviews (Gregg Milligan)
