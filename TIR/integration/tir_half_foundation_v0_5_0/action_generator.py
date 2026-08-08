from __future__ import annotations
from dataclasses import dataclass, asdict
from typing import Iterable
from .foundation import KAPPA
from .l_constants import L3, L4, L5

@dataclass(frozen=True)
class GeneratorCoefficients:
    half_base: int
    linear: int
    return_axis: int
    curvature: int

    def intrinsic_vector4(self) -> tuple[int, int, int, int]:
        return (self.half_base, self.linear, self.return_axis, self.curvature)

@dataclass(frozen=True)
class GeneratorState:
    id: str
    coefficients: GeneratorCoefficients
    status: str
    provenance: tuple[str, ...]
    interpretation: str
    assignment_status: str

def action_release_generator(
    c: GeneratorCoefficients,
    *,
    kappa: float = KAPPA,
    l3: float = float(L3),
) -> float:
    """Discrete basis generator.

    G(h,a,b,c) = h/2 + a*kappa + b*kappa/L3 + c*kappa^2/2.

    The algebra is exact for a supplied coefficient tuple.  The physical
    assignment of a tuple to a particle/transition keeps its own epistemic
    status and is not silently promoted.
    """
    return (
        0.5 * c.half_base
        + c.linear * kappa
        + c.return_axis * (kappa / l3)
        + c.curvature * (kappa * kappa / 2.0)
    )

COEFFICIENT_STATES = {
    "ELECTRON_ACTION": GeneratorState(
        "ELECTRON_ACTION",
        GeneratorCoefficients(1, -3, +1, -1),
        "PROJECT_DERIVED_CANDIDATE_GATE",
        ("TIR v6.7 electron action gate", "Metatime Ch.5"),
        "spin-half base + three-generation deficit + Collatz return + negative Poincare curvature",
        "PROJECT_MODEL_ASSIGNMENT",
    ),
    "E_TO_MU_RELEASE": GeneratorState(
        "E_TO_MU_RELEASE",
        GeneratorCoefficients(0, +L5, +L4, +(L3 + 1)),
        "PROJECT_DERIVED_CANDIDATE_GATE",
        ("TIR v7.0 e->mu release gate", "Metatime Ch.6.1"),
        "L5 preference step + L4/L3 return correction + (L3+1) positive curvature count",
        "PROJECT_MODEL_ASSIGNMENT",
    ),
    "MU_TO_TAU_RELEASE": GeneratorState(
        "MU_TO_TAU_RELEASE",
        GeneratorCoefficients(0, +3, -1, -L3),
        "PROJECT_DERIVED_CANDIDATE_GATE",
        ("TIR v6.8 mu->tau release gate", "Metatime Ch.6.2"),
        "three-generation step + negative return correction + negative L3 curvature count",
        "PROJECT_MODEL_ASSIGNMENT",
    ),
}

def coefficient_state(state_id: str) -> GeneratorState:
    return COEFFICIENT_STATES[state_id]

def electron_action_from_generator() -> float:
    return action_release_generator(COEFFICIENT_STATES["ELECTRON_ACTION"].coefficients)

def e_mu_release_from_generator() -> float:
    return action_release_generator(COEFFICIENT_STATES["E_TO_MU_RELEASE"].coefficients)

def mu_tau_release_from_generator() -> float:
    return action_release_generator(COEFFICIENT_STATES["MU_TO_TAU_RELEASE"].coefficients)

def charged_lepton_actions() -> dict[str, float]:
    se = electron_action_from_generator()
    smu = se - e_mu_release_from_generator()
    stau = smu - mu_tau_release_from_generator()
    return {"S_e": se, "S_mu": smu, "S_tau": stau}

def exact_lattice_identities() -> dict[str, tuple[int, int, int, int]]:
    e = COEFFICIENT_STATES["ELECTRON_ACTION"].coefficients
    em = COEFFICIENT_STATES["E_TO_MU_RELEASE"].coefficients
    mt = COEFFICIENT_STATES["MU_TO_TAU_RELEASE"].coefficients
    total = tuple(a + b for a, b in zip(em.intrinsic_vector4(), mt.intrinsic_vector4()))
    mu = tuple(a - b for a, b in zip(e.intrinsic_vector4(), em.intrinsic_vector4()))
    tau = tuple(a - b - c for a, b, c in zip(
        e.intrinsic_vector4(), em.intrinsic_vector4(), mt.intrinsic_vector4()
    ))
    return {
        "R_e_tau": total,
        "S_mu": mu,
        "S_tau": tau,
    }
