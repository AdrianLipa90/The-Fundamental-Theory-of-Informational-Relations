"""Critical-axis solver and typed implication engine.

The solver has two jobs:
1. solve the recurrent sigma=1/2 constraints through independent mathematical
   routes (complement, entropy, Berry holonomy, and cancellation), and
2. compute semantic closure without silently promoting model/open bridges.

XF-1 adds the standard Xi Fourier-kernel decomposition as a canonical
zeta-derived two-branch representation. Exact branch cancellation is then a
theorem at every Xi zero. The remaining XF-1 RH-level debt is split into
explicit global branch nondegeneracy and kernel-population/strip-coordinate
binding.

XF-3 adds the Dimitrov--Xu n=2 correlation kernel as a second analytic route.
The published RH-equivalent translation-density and convolution-annihilator
criteria are STANDARD implications, while satisfaction of either global
criterion remains OPEN unless independently supplied as a premise.

XF-4 resolves the XF-3 density condition to the pointwise Wiener--Laguerre
scalar Q_Xi(x,y). The identity Q_Xi=Fourier(Phi_{2,y}) and the equivalence
between L1 translation density and global strict positivity are STANDARD.
Actual strict positivity for every real x and every 0<|y|<1/2 remains OPEN.
"""
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Iterable, Mapping

import mpmath as mp

from .core import binary_entropy, berry_holonomy, two_channel_amplitude


class ClaimStatus(str, Enum):
    EXACT = "exact"
    STANDARD = "standard"
    MODEL = "model"
    OPEN = "open"


@dataclass(frozen=True)
class Rule:
    premises: tuple[str, ...]
    conclusion: str
    status: ClaimStatus
    provenance: str


@dataclass(frozen=True)
class ProofStep:
    conclusion: str
    rule: Rule


@dataclass(frozen=True)
class ClosureResult:
    facts: frozenset[str]
    proof: Mapping[str, ProofStep]
    blocked: tuple[Rule, ...]

    def derives(self, claim: str) -> bool:
        return claim in self.facts


class ClaimSolver:
    """Forward-chaining solver over typed hyperedges."""

    def __init__(self, rules: Iterable[Rule]) -> None:
        self.rules = tuple(rules)

    def closure(self, facts: Iterable[str], *, allow_model: bool = False) -> ClosureResult:
        allowed = {ClaimStatus.EXACT, ClaimStatus.STANDARD}
        if allow_model:
            allowed.add(ClaimStatus.MODEL)
        known = set(map(str, facts))
        proof: dict[str, ProofStep] = {}
        changed = True
        while changed:
            changed = False
            for rule in self.rules:
                if rule.status not in allowed:
                    continue
                if rule.conclusion in known:
                    continue
                if all(premise in known for premise in rule.premises):
                    known.add(rule.conclusion)
                    proof[rule.conclusion] = ProofStep(rule.conclusion, rule)
                    changed = True
        blocked = tuple(
            rule
            for rule in self.rules
            if rule.conclusion not in known
            and (rule.status not in allowed or not all(p in known for p in rule.premises))
        )
        return ClosureResult(frozenset(known), proof, blocked)

    def missing_premises(
        self,
        goal: str,
        facts: Iterable[str],
        *,
        allow_model: bool = False,
    ) -> tuple[tuple[Rule, tuple[str, ...]], ...]:
        closure = self.closure(facts, allow_model=allow_model)
        if goal in closure.facts:
            return ()
        candidates = []
        for rule in self.rules:
            if rule.conclusion != goal:
                continue
            missing = tuple(p for p in rule.premises if p not in closure.facts)
            candidates.append((rule, missing))
        return tuple(candidates)


HALF_AXIS_RULES = (
    Rule(("sigma_half",), "complement_fixed", ClaimStatus.EXACT, "sigma=1-sigma"),
    Rule(("sigma_half",), "centered_zero", ClaimStatus.EXACT, "u=sigma-1/2"),
    Rule(("sigma_half",), "entropy_max_ln2", ClaimStatus.EXACT, "binary Shannon theorem"),
    Rule(("sigma_half", "qubit_representation"), "bloch_equator", ClaimStatus.STANDARD, "n_z=2 sigma-1"),
    Rule(("sigma_half", "qubit_representation"), "berry_minus_one", ClaimStatus.EXACT, "equatorial Berry holonomy"),
    Rule(("sigma_half", "symmetric_readout", "half_turn_phase"), "exact_cancellation", ClaimStatus.EXACT, "complementary cancellation theorem"),
    Rule(("centered_zeta_chart",), "zeta_fixed_axis_half", ClaimStatus.STANDARD, "J(s)=1-conj(s)"),
    Rule(("centered_zeta_chart", "reciprocal_chart"), "reciprocal_axis_invariant", ClaimStatus.EXACT, "I o J~=J~ o I"),
    Rule(("affine_endpoint_map",), "sigma_equals_real_part_coordinate", ClaimStatus.EXACT, "unique affine strip-simplex map"),
    Rule(("projective_cycle", "spin_half"), "spinor_double_cover", ClaimStatus.STANDARD, "SU(2)->SO(3)"),
    Rule(("binary_information", "twelve_projective_cycles"), "information_per_turn_ln2_over_12", ClaimStatus.MODEL, "Metatime information-cycle assignment"),
    Rule(("information_per_turn_ln2_over_12", "radian_closure_tau"), "kappa_ln2_over_24pi", ClaimStatus.MODEL, "(ln2/12)/tau"),
    Rule(("eight_mix_sectors", "three_flavours"), "twenty_four_sector_count", ClaimStatus.MODEL, "8*3=24"),
    Rule(("twenty_four_sector_count", "half_turn_phase"), "twenty_four_pi_normalization", ClaimStatus.MODEL, "24 half-turn phase units"),
    Rule(("xi_fourier_kernel",), "canonical_xi_two_branch_representation", ClaimStatus.STANDARD, "XF-1 exponential resolution of the Riemann Xi cosine kernel"),
    Rule(("canonical_xi_two_branch_representation",), "all_xi_zeros_exact_kernel_branch_cancellation", ClaimStatus.EXACT, "Xi=A_+ + A_- implies A_+=-A_- at every Xi zero"),
    Rule(("canonical_xi_two_branch_representation",), "global_kernel_branch_nondegeneracy", ClaimStatus.OPEN, "XF-1 global nonzero-branch obligation"),
    Rule(("canonical_xi_two_branch_representation",), "kernel_population_equals_strip_coordinate", ClaimStatus.OPEN, "XF-1 RH-equivalent population/affine-coordinate bridge"),
    Rule(("all_xi_zeros_exact_kernel_branch_cancellation", "global_kernel_branch_nondegeneracy"), "all_xi_zero_kernel_population_half", ClaimStatus.EXACT, "nondegenerate equal-and-opposite branches have equal squared-norm population"),
    Rule(("all_xi_zero_kernel_population_half", "kernel_population_equals_strip_coordinate", "sigma_equals_real_part_coordinate"), "all_zeros_on_half_axis", ClaimStatus.EXACT, "XF-1 normalized-population route"),
    Rule(("all_xi_zeros_exact_kernel_branch_cancellation", "global_kernel_branch_nondegeneracy", "kernel_population_equals_strip_coordinate", "sigma_equals_real_part_coordinate"), "all_zeros_on_half_axis", ClaimStatus.EXACT, "XF-1 direct RH firewall"),
    Rule(("all_zeros_on_half_axis",), "riemann_hypothesis", ClaimStatus.STANDARD, "definition of RH"),
    Rule(("xi_fourier_kernel",), "dimitrov_xu_nu2_correlation_kernel", ClaimStatus.STANDARD, "XF-3 / Dimitrov-Xu correlation kernel n=2"),
    Rule(("dimitrov_xu_nu2_correlation_kernel",), "xi_wronskian_nu2_fourier_identity", ClaimStatus.STANDARD, "Dimitrov-Xu Theorem 1.3 / Theorem 2.5 for n=2"),
    Rule(("dimitrov_xu_nu2_correlation_kernel",), "phi2y_translation_density_condition", ClaimStatus.OPEN, "Dimitrov-Xu Theorem 1.1 global L1-density obligation for every 0<|y|<1/2"),
    Rule(("phi2y_translation_density_condition",), "riemann_hypothesis", ClaimStatus.STANDARD, "Dimitrov-Xu Theorem 1.1 forward implication"),
    Rule(("riemann_hypothesis", "dimitrov_xu_nu2_correlation_kernel"), "phi2y_translation_density_condition", ClaimStatus.STANDARD, "Dimitrov-Xu Theorem 1.1 reverse implication"),
    Rule(("dimitrov_xu_nu2_correlation_kernel",), "phi2y_bounded_convolution_annihilator_condition", ClaimStatus.OPEN, "Dimitrov-Xu Corollary 3.5 global annihilator obligation"),
    Rule(("phi2y_bounded_convolution_annihilator_condition",), "riemann_hypothesis", ClaimStatus.STANDARD, "Dimitrov-Xu Corollary 3.5 forward implication"),
    Rule(("riemann_hypothesis", "dimitrov_xu_nu2_correlation_kernel"), "phi2y_bounded_convolution_annihilator_condition", ClaimStatus.STANDARD, "Dimitrov-Xu Corollary 3.5 reverse implication"),
    Rule(("xi_wronskian_nu2_fourier_identity",), "phi2y_fourier_equals_xi_wiener_laguerre_scalar", ClaimStatus.STANDARD, "XF-4 / Dimitrov-Xu Eq. (3.10) plus Jensen derivative identity"),
    Rule(("phi2y_fourier_equals_xi_wiener_laguerre_scalar",), "xi_wiener_laguerre_strict_positivity", ClaimStatus.OPEN, "XF-4 global condition Q_Xi(x,y)>0 for all real x and every 0<|y|<1/2"),
    Rule(("phi2y_translation_density_condition", "phi2y_fourier_equals_xi_wiener_laguerre_scalar"), "xi_wiener_laguerre_strict_positivity", ClaimStatus.STANDARD, "Wiener L1 theorem plus Q_Xi(0,y)>0 fixes the nonvanishing transform sign"),
    Rule(("xi_wiener_laguerre_strict_positivity", "phi2y_fourier_equals_xi_wiener_laguerre_scalar"), "phi2y_translation_density_condition", ClaimStatus.STANDARD, "Q_Xi=Fourier(Phi_{2,y}) is everywhere nonzero; Wiener L1 translation theorem"),
)


DEFAULT_SOLVER = ClaimSolver(HALF_AXIS_RULES)


def solve_sigma_from_complement() -> mp.mpf:
    """Solve sigma=1-sigma."""
    return mp.mpf("0.5")


def solve_sigma_from_entropy() -> mp.mpf:
    """Solve H'(sigma)=0 in the open probability interval."""
    return mp.findroot(lambda p: mp.log((1 - p) / p), mp.mpf("0.5"))


def solve_sigma_from_berry_minus_one() -> mp.mpf:
    """Solve exp[-2*pi*i*(1-sigma)]=-1 for the interior branch sigma in (0,1)."""
    root = mp.findroot(lambda p: mp.im(berry_holonomy(p)), (mp.mpf("0.4"), mp.mpf("0.6")))
    # Imaginary-part roots also occur at endpoints; retain the root whose real holonomy is -1.
    if not (0 < root < 1) or abs(berry_holonomy(root) + 1) > mp.mpf("1e-30"):
        raise RuntimeError("failed to isolate the interior -1 Berry-holonomy solution")
    return root


def solve_sigma_from_cancellation() -> mp.mpf:
    """Solve the phase-pi complementary cancellation condition."""
    return mp.findroot(
        lambda p: mp.re(two_channel_amplitude(p, mp.pi)),
        (mp.mpf("0.4"), mp.mpf("0.6")),
    )


def solve_half_axis_routes() -> dict[str, mp.mpf]:
    """Return four independent routes selecting sigma=1/2 within their domains."""
    return {
        "complement": solve_sigma_from_complement(),
        "entropy": solve_sigma_from_entropy(),
        "berry_minus_one": solve_sigma_from_berry_minus_one(),
        "cancellation": solve_sigma_from_cancellation(),
    }


def kappa_from_projective_cycle(
    information_quantum: mp.mpf | float | None = None,
    projective_cycles: int = 12,
    closure_period: mp.mpf | float | None = None,
) -> mp.mpf:
    """Conditional Metatime normalization kappa=I/(N*C).

    Arithmetic is evaluated at the caller's active mpmath precision. The
    assignment N=12 as one information cycle is a TIR/Metatime model
    assumption. Delaying default ``ln(2)`` and ``2*pi`` evaluation avoids
    freezing them at import-time precision.
    """
    n = int(projective_cycles)
    if n <= 0:
        raise ValueError("projective_cycles must be positive")
    info = mp.log(2) if information_quantum is None else mp.mpf(information_quantum)
    c = 2 * mp.pi if closure_period is None else mp.mpf(closure_period)
    if c <= 0:
        raise ValueError("closure_period must be positive")
    return info / (n * c)


def validate_half_axis_routes(tol: mp.mpf | float = mp.mpf("1e-30")) -> bool:
    half = mp.mpf("0.5")
    eps = mp.mpf(tol)
    routes = solve_half_axis_routes()
    return all(abs(value - half) <= eps for value in routes.values())
