# Reproducibility Guide

## One-command audit
```bash
python3 TIR/metatime_audit.py
```
Output: full formula ledger with PDG comparison for every sector.

## Requirements
- Python 3.9+ (stdlib only — no dependencies)
- No pip install required
- Works on Linux, macOS, Windows (WSL)

## Verifying the audit
```bash
# Run audit
python3 TIR/metatime_audit.py > audit_output.txt

# Compare with reference (when available)
sha256sum audit_output.txt  # Compare with published SHA
```

## Docker (optional)
```dockerfile
FROM python:3.11-slim
WORKDIR /metatime
COPY . .
CMD ["python3", "TIR/metatime_audit.py"]
```
```bash
docker build -t metatime-audit . && docker run metatime-audit
```

## Structural-choice audit
Open `TIR/STRUCTURAL_CHOICES.md` — every input/choice classified.

## What to verify as a reviewer
1. Run `metatime_audit.py` — do outputs match CURRENT_STATUS.md?
2. Open `STRUCTURAL_CHOICES.md` — are all 50 choices accounted for?
3. Check `FALSIFIABILITY.md` — nEDM falsification acknowledged?
4. Trace one formula through the code (e.g., charged leptons lines 41–49)
