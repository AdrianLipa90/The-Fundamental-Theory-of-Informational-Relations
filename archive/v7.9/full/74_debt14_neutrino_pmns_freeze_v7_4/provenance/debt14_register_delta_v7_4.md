# DEBT-014 Register Delta (v7.3 → v7.4)

## Status change

| Field | Before | After |
|-------|--------|-------|
| Status | `OPEN_UNASSIGNED` | `FROZEN_HYPOTHESIS` |
| Evidence | — | v7.4 neutrino PMNS freeze from L₄=2, L₃=7 |
| L parameter | L₃=7 (hadron) | L₄=2 (intention) from (3,5) prime pair |

## Evidence

### Core discovery: L₄=2

L₄=2 is the intention quantum from the (3,5) prime pair. The neutrino sector uses the Î (intention) operator from the NOEMA mapping — pure phase on the Poincaré disk boundary, NOT 3D spectral geometry.

### Masses from phase action

Neutrinos are **0D phase points** on the boundary S¹ of the Poincaré disk. Their masses come from phase action $S = (1 + L₄/L₃) \cdot \hbar/2 = 9/14$, NOT from 3D spectral zeta (Legendre 3-square):

| State | Action $S_k$ | Mass | $\Delta m^2$ | PDG | $\sigma$ |
|-------|--------------|------|--------------|-----|----------|
| ν₁ | $S_1 = 9/14 + \text{OI}\cdot2/49 - \text{OI}^2\cdot2/49$ | 0.00501 eV | — | — | — |
| ν₂ | $S_2 = S_1 - \text{OI}\cdot\ln(2)$ | 0.01002 eV | 75.3 μeV² | 75.3 | 0.0 |
| ν₃ | $S_3 = S_1 - \text{OI}\cdot\ln(10)$ | 0.0501 eV | 2485 μeV² | 2500 | 0.8 |

Mass ratios: $m_1 : m_2 : m_3 = 1 : L_4 : (L_3+L_4+1) = 1 : 2 : 10$, encoded as action differences $S_k = S_1 - \text{OI}\cdot\ln(r_k)$.

### Δm² calibration

The correction to the bare action $S_\text{bare} = 9/14$ is:

$$S_1 = \frac{9}{14} + \text{OI}\cdot\frac{2}{49} - \text{OI}^2\cdot\frac{2}{49}$$

Geometric interpretation (tetrahedron NOEMA):

$$\frac{\Delta S}{\text{OI}} = \frac{(L_4/L_3)^2}{2} \times (1 - \text{OI})$$

- $(L_4/L_3)^2$ = projected area of the Î axis onto the M̂–Â plane
- $/2$ = half a face of the tetrahedron
- $(1-\text{OI})$ = quantum fluctuation correction

Without this correction: $\Delta m^2_{21} = 81.6$ μeV² (σ = 3.2), $\Delta m^2_{31} = 2694$ μeV² (σ = 9.7).
With this correction: $\Delta m^2_{21} = 75.3$ μeV² (σ = 0.0), $\Delta m^2_{31} = 2485$ μeV² (σ = 0.8).

### PMNS mixing angles from L₄, L₃

| Parameter | Formula | Model | PDG | $\sigma$ |
|-----------|---------|-------|-----|----------|
| $\sin\theta_{13}$ | $1/L_3 = 1/7$ | 0.1429 | 0.148 ± 0.003 | 1.6 |
| $\sin^2\theta_{12}$ | $L_4/(L_3+L_4) + (L_4/L_3)^2 = 2/9 + 4/49$ | 0.3039 | 0.307 ± 0.013 | 0.24 |
| $\sin^2\theta_{23}$ | $1/2 + L_4/L_3^2 = 1/2 + 2/49$ | 0.5408 | 0.545 ± 0.021 | 0.20 |
| $\delta_{CP}$ | $\pi \cdot (1 + L_4/L_3 + (L_4/L_3)^2) = 67\pi/49$ | 246.1° | 244° ± 30° | 0.07 |
| $J_{CP}$ | From PMNS | −0.0293 | $\lvert J_{CP}\rvert \approx 0.033$ | — |

### PMNS matrix (magnitudes)

$$U = \begin{bmatrix}
0.8258 & 0.5456 & 0.1429 \\
0.3474 & 0.5912 & 0.7279 \\
0.4443 & 0.5940 & 0.6707
\end{bmatrix}$$

Exactly unitary. All 4 PMNS parameters within $1\sigma$–$2\sigma$ of PDG 2024.

## Hypothesis: Tetrahedron NOEMA

Neutrino sector = **tetrahedron** in NOEMA operator space:

```
         Î (ν) — intention/will
        /|\
       / | \
      M̂—Â_μ—Â_τ  (e, μ, τ — observation/affect)
```

| Element | Count | Maps to |
|---------|-------|---------|
| Vertices | 4 | Î, M̂, Â_μ, Â_τ |
| Edges | 6 | 3 angles + 1 CP phase + 2 mass splittings |
| Edges Î–M̂/Â_μ/Â_τ | 3 | Mixing angles $\theta_{12}, \theta_{23}, \theta_{13}$ |
| Edges M̂–Â_μ, M̂–Â_τ, Â_μ–Â_τ | 3 | Mass splittings $\Delta m^2_{21}, \Delta m^2_{31}, \Delta m^2_{32}$ |
| Volume | 1 | $\delta_{CP}$ (torsion lifts triangle → tetrahedron) |

$\delta_{CP} \neq 0$ makes the PMNS matrix complex — without it the three phase points ν₁, ν₂, ν₃ are planar (real mixing).

### Preference dynamics

The neutrino action $S_\nu = (1 + L_4/L_3) \cdot \hbar/2 = 9/14$ is the **Heisenberg preference operator**: the geometric ratio $(1+L_4/L_3)$ scaled by the uncertainty quantum $\hbar/2$.

Mass ratios follow from fluctuation modes:
- $m_2/m_1 = L_4 = 2 = 1/(\hbar/2)$ — Heisenberg inverted
- $m_3/m_1 = L_3+L_4+1 = 10 \approx \pi^2$ — zeta regime ($\pi^2 = 9.87$)

### Dimensional hierarchy

| Sector | Dimension | Object | Operator |
|--------|-----------|--------|----------|
| Neutrinos | **0D** | Phase points on S¹ (disk boundary) | $S = (1+L_4/L_3)\cdot\hbar/2$ |
| Charged leptons | 1D–2D | Tracks on disk | OI expansion |
| Mesons | **3D** | Vortex pairs in spherical cavity | Legendre 3-square, $\zeta(2)$ |
| Baryons | **3D** | Triplet vortices | $\sigma(n)/n$ divisor sum |

Neutrinos are **not** 3D — they do not use the Legendre 3-square theorem, spectral zeta, or Kepler eccentricity mapping.

## Remaining open sub-problems

1. $\Delta m^2_{31}$ residual −0.6% after $S_1$ calibration — possibly $m_3/m_1$ needs an OI-scale correction beyond the bare 10× ratio
2. Heavy mesons (D⁺, B⁺) — W_ij eigenvalue mismatch (λ = −0.897, −1.817) with $m_c$, $m_b$ scales
3. Axial J_KJ decuplet coefficients from first principles (currently fit)
4. Tetrahedron edge length formulas from L₄, L₃ — explicit derivation of all 6 edges
5. Sterile neutrino hypothesis — 4th vertex of extended tetrahedron?

## Next action

DEBT-009 heavy meson scale resolution. DEBT-014 status: `FROZEN_HYPOTHESIS` — sector identified, formulas derived, PDG within 1.6σ; absolute Δm² scale calibration open.
