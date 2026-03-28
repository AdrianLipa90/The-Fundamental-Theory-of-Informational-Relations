# Glossary

## Tau / kernel / White-Thread / action stack

### White-Thread primitive
Minimal transported pairwise quantity
\[
W_{ij}[\gamma] = \langle \Psi_i|U[\gamma_{ij}]|\Psi_j\rangle.
\]
See `DEF-0010`.

### Loose-thread bundle
Finite family of admissible auxiliary paths for a fixed ordered pair. See `DEF-0011`.

### Effective White-Thread
Convexly aggregated transported pairwise amplitude
\[
W_{ij}^{eff} = \sum_a \alpha_a W_{ij}^{(a)}.
\]
See `DEF-0011`.

### Semantic path action
Scalar cost assigned to a candidate path. See `DEF-0012`.

### Dynamic path weights
Softmax-like normalized path weights
\[
\alpha_a = \frac{e^{-\sigma \mathcal S(\gamma^{(a)})}}{\sum_b e^{-\sigma \mathcal S(\gamma^{(b)})}}.
\]
See `DEF-0012`.

### Hermitian coupling projection
Real symmetric coupling extracted from effective White-Thread transport. See `DEF-0014`.

### Spectral tau modes
Eigenvalue-defined relational timescales
\[
\tau_i = \lambda_i(A).
\]
See `DEF-0014`.

### Flavor / color sector
Reserved downstream classification layer for fermion-sector interpretation. Not yet canonically identified in the current toy spectral bridge.
