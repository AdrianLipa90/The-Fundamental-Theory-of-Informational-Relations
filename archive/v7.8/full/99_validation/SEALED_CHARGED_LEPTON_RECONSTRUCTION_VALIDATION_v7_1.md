# v7.1 validation — sealed charged-lepton reconstruction benchmark

## Step-by-step derivation

(9 steps, no measured masses used as derivation inputs.)

### Step 1-2: Fundamental constants
```
OI = ln(2)/(24·π)  = 0.009193150006360484   [OP-OI, v5.3]
L3 = 7              (Collatz base channel)   [OP-COLLATZ, v4.5]
```

### Step 3: Absolute electron action S_e
```
S_e = 1/2 − 3·OI + OI/L3 − OI²/2
    = 0.5 − 0.027579450019081 + 0.001313307143766 − 0.000042257003520
    = 0.47369160012116457                      [v6.7]
```

### Step 4-5: Release operators
```
R_em = 5·OI + 2·OI/L3 + ((L3+1)/2)·OI²      [v7.0]
     = 0.045965750031802 + 0.002626614287532 + 0.000338056028158
     = 0.048930420347491774

R_mt = 3·OI − OI/L3 − (L3/2)·OI²             [v6.8]
     = 0.027579450019081 − 0.001313307143766 − 0.000295799024638
     = 0.025970343850677605
```

### Step 6: Planck normalizer
```
E_P = sqrt(ħ·c⁵/G)
    = 1.2208901285838957e22 MeV              [v6.1]
```

### Step 7-8: Derived actions
```
S_μ = S_e − R_em  = 0.4247611797736728
S_τ = S_μ − R_mt  = 0.3987908359229952
```

### Step 9: Energy prediction
```
E_i = E_P · exp(-S_i / OI)
```

### Results
```
electron: 0.511642 MeV  (ref 0.510999 MeV)   error +0.1259%
muon:    104.831769 MeV (ref 105.65838 MeV)   error −0.7823%
tau:    1767.504070 MeV (ref 1776.86 MeV)     error −0.5265%

Mean abs error: 0.4782%
Max abs error:  0.7823%
```

## Technical rows
```
module71 validator: PASS
nested_archives_count: 0
full-root syntax compile: PASS
```

## Gate decision
- Charged-lepton sector: FULLY_GATED_SUB_PERCENT_ALL_CHANNELS
- canon: DENIED (DEBT-009 hadron/meson split still open)
- Next gate: v7.2 DEBT-009 baryon triplet freeze gate
