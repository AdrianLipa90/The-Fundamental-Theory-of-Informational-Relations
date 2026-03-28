# Export Repository State

## Status
`defined`

## Purpose
This note records the exact command for generating real `objects_state.csv` and `couplings.csv` from a checked-out repository tree.

## Command
Run from the repository root:

```bash
python scripts/export_repository_state.py \
  --repo-root . \
  --objects-out exports/objects_state.csv \
  --couplings-out exports/couplings.csv
```

## Result
This command produces:
- `exports/objects_state.csv`
- `exports/couplings.csv`

using the canonical extractor
- `src/ciel_foundations/solvers/repo_object_state_extractor.py`

and the schemas
- `schemas/objects_state.schema.yaml`
- `schemas/couplings.schema.yaml`

## Notes
- This is the real-export path for a current checkout, not the deterministic fixture demo.
- The export reflects the working tree that is present locally when the command is run.
- Generated export files are runtime products and should be registered as artifacts only after intentional capture and review.
