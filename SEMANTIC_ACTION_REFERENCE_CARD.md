# Semantic Action Reference Card

## Online action
\[
\mathcal S_{online}[\gamma] = \alpha\widehat L[\gamma] + \beta\widehat{\Delta\phi}[\gamma] + \kappa\widehat D_{rel}[\gamma] + \mu\widehat\Pi_{truth}^{struct}[\gamma]
\]

## Full action
\[
\mathcal S_{full} = \mathcal S_{online} + \nu\widehat\Pi_{truth}^{audit}
\]

## Components
- `L_sem` — semantic length cost
- `Delta_phi` — phase transport cost
- `D_rel_holonomic` — closure-defect cost
- `D_rel_resonance` — resonance/intention defect cost
- `Pi_truth_struct` — structural truth deviation
- `Pi_truth_audit` — post-hoc audited truth deviation

## Distortion channels
- `false`
- `unmarked`
- `omit`
- `hall`
- `smooth`

## Minimal output contract
```json
{
  "S_online": 0.0,
  "S_full": 0.0,
  "L_sem": 0.0,
  "Delta_phi": 0.0,
  "D_rel_holonomic": 0.0,
  "D_rel_resonance": 0.0,
  "Pi_truth_struct": 0.0,
  "Pi_truth_audit": 0.0,
  "distortion_channels": {
    "false": 0.0,
    "unmarked": 0.0,
    "omit": 0.0,
    "hall": 0.0,
    "smooth": 0.0
  },
  "verdict": "accept"
}
```

## Minimal test procedure
1. constant phase must yield zero phase cost
2. Euler-closed phase triple must yield vanishing holonomic defect
3. perfect resonance must yield zero structural truth cost
4. full action must equal online action plus audit contribution
