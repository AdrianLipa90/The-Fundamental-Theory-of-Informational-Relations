from __future__ import annotations

from dataclasses import dataclass, asdict
import math

FORBIDDEN_INPUT_KEYS = frozenset({
    "mass", "masses", "observed_mass", "pdg_mass", "yukawa",
    "target_action", "target_release", "coefficients", "coefficient_tuple",
    "action_envelope", "mass_fit", "residual_target",
})

ROLE_ROUTER = {
    "h": {
        "source_role": "projective_half_spin_identity",
        "status": "STRUCTURAL_ROLE_ROUTING_PASS",
        "parents": ("SOURCE_DERIVED_CHIRAL_CP1_AXIS", "HALF", "SPIN_HALF_EULER_BERRY_GATE"),
    },
    "a": {
        "source_role": "generation_seed_release",
        "status": "STRUCTURAL_ROLE_ROUTING_PASS",
        "parents": ("TWIN_PRIME_SEED_INDEX", "RAMANUJAN_SCALING", "GENERATION_ASSIGNMENT"),
    },
    "b": {
        "source_role": "collatz_return_axis",
        "status": "STRUCTURAL_ROLE_ROUTING_PASS",
        "parents": ("COLLATZ_TERMINAL_AXIS", "ORBIT_RETURN_DIRECTION"),
    },
    "c": {
        "source_role": "poincare_berry_curvature_holonomy",
        "status": "STRUCTURAL_ROLE_ROUTING_PASS",
        "parents": ("TETRAHEDRAL_DEPTH", "POINCARE_DISK", "BERRY_CONNECTION"),
    },
}


def validate_precoefficient_payload(payload: dict) -> None:
    lower = {str(k).lower() for k in payload}
    bad = sorted(lower & FORBIDDEN_INPUT_KEYS)
    if bad:
        raise ValueError(f"circular/forbidden atomic input keys: {bad}")


def sign3(x: float, eps: float = 1e-15) -> int:
    return 1 if x > eps else -1 if x < -eps else 0


def relational_gradient_orientation(dV_dphi: float) -> int:
    """Project-runtime orientation inherited from spin=tanh(-alpha_s*dV_dphi).

    For every positive alpha_s the sign is sign(-dV_dphi), so no tuned alpha
    magnitude is needed to obtain the orientation class.
    """
    if not math.isfinite(dV_dphi):
        raise ValueError("dV_dphi must be finite")
    return sign3(-float(dV_dphi))


def relational_spin(dV_dphi: float, alpha_s: float = 1.0) -> float:
    if not math.isfinite(alpha_s) or alpha_s <= 0:
        raise ValueError("alpha_s must be finite and positive")
    return math.tanh(-alpha_s * float(dV_dphi))


def orbital_direction_orientation(direction: str) -> int:
    d = direction.strip().lower().replace(" ", "")
    if d in {"attractor->satellite", "attractor→satellite", "outgoing"}:
        return 1
    if d in {"satellite->attractor", "satellite→attractor", "incoming"}:
        return -1
    if d in {"neutral", "none"}:
        return 0
    raise ValueError(f"unknown orbital direction: {direction}")


def chiral_path_orientation(path: str) -> int:
    """Kept separate: surviving documentation is inside a retrospective layer."""
    p = path.strip().upper()
    if p == "H+":
        return 1
    if p in {"H-", "H−"}:
        return -1
    if p == "NEUTRAL":
        return 0
    raise ValueError(path)


@dataclass(frozen=True)
class AtomicGeometryState:
    state_id: str
    source_role: str
    dV_dphi: float
    orbital_direction: str
    chiral_path: str = "neutral"
    seed_from: tuple[int, int] | None = None
    seed_to: tuple[int, int] | None = None
    collatz_stop_from: int | None = None
    collatz_stop_to: int | None = None

    def payload(self) -> dict:
        out = asdict(self)
        validate_precoefficient_payload(out)
        return out


def evaluate_orientation(state: AtomicGeometryState) -> dict[str, object]:
    state.payload()
    g = relational_gradient_orientation(state.dV_dphi)
    o = orbital_direction_orientation(state.orbital_direction)
    c = chiral_path_orientation(state.chiral_path)
    nonzero = [x for x in (g, o, c) if x]
    agreement = "UNANIMOUS" if nonzero and len(set(nonzero)) == 1 else "CONFLICT" if len(set(nonzero)) > 1 else "INSUFFICIENT"
    return {
        "state_id": state.state_id,
        "gradient_orientation": g,
        "orbital_orientation": o,
        "chiral_orientation": c,
        "agreement": agreement,
        "status": "IMPLEMENTED_SOURCE_OPERATOR_CANDIDATE_TIR_BINDING",
    }


def retrospective_collatz_candidate() -> dict[str, object]:
    """Observation only; MUST NOT be consumed as canon without a prospective test."""
    def s(a: int, b: int) -> int:
        return sign3(b-a)
    return {
        "e_to_mu": {"ell_source": 2, "ell_destination": 9, "sign": s(2, 9), "candidate_abs_c": 8},
        "mu_to_tau": {"ell_source": 9, "ell_destination": 8, "sign": s(9, 8), "candidate_abs_c": 7},
        "candidate_rules": [
            "sign_transition = sign(ell_destination-ell_source)",
            "abs(c) = ell_destination-1",
        ],
        "status": "RETROSPECTIVE_PATTERN_ONLY_NOT_CANON",
    }
