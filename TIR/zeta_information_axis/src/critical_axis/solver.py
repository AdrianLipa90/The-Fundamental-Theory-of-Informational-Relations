"""Critical-axis solver and typed implication engine.

The solver has two jobs:
1. solve the recurrent sigma=1/2 constraints through independent mathematical
   routes (complement, entropy, Berry holonomy, and cancellation), and
2. compute semantic closure without silently promoting model/open bridges.

No rule in the default graph derives RH.  The zero-state bridge remains open.
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
    Rule(("zero_state_representation", "exact_cancellation", "sigma_equals_real_part_coordinate"), "all_zeros_on_half_axis", ClaimStatus.OPEN, "open zeta zero-state bridge"),
    Rule(("all_zeros_on_half_axis",), "riemann_hypothesis", ClaimStatus.OPEN, "definition of RH"),
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
