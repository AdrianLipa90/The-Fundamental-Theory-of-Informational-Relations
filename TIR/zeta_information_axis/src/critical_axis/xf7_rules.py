"""Typed XF-7 solver extension for the Laguerre-hierarchy programme.

The extension is isolated from DEFAULT_SOLVER.  The peer-reviewed positivity
and strict radial decrease of the classical Xi kernel are STANDARD external
input.  The 2026 Planat--Sole second-level concavity result remains an OPEN
preprint gate unless explicitly supplied as a fact.  Everything downstream
that is ordinary calculus is typed EXACT.
"""

from __future__ import annotations

from .solver import ClaimSolver, ClaimStatus, HALF_AXIS_RULES, Rule
from .xf6_rules import XF6_RULES


XF7_RULES = (
    Rule(
        ("xi_fourier_kernel",),
        "xi_kernel_positive_strict_decrease",
        ClaimStatus.STANDARD,
        "Planat, Symmetry 18 (2026) 1283: Phi>0 and Phi'(r)<0 for r>0",
    ),
    Rule(
        ("xi_fourier_kernel",),
        "planat_sole_second_level_concavity",
        ClaimStatus.OPEN,
        "Planat--Sole arXiv:2608.19160 external preprint claim: log F strictly concave for F=s'^2-s s'', s(t)=Phi(sqrt(t))",
    ),
    Rule(
        ("planat_sole_second_level_concavity",),
        "xf7_first_laguerre_positive_s_sqrt",
        ClaimStatus.STANDARD,
        "source theorem is formulated for log F on (0,infinity), hence F>0 on its stated domain",
    ),
    Rule(
        ("planat_sole_second_level_concavity",),
        "xf7_double_turan_hierarchy",
        ClaimStatus.STANDARD,
        "Planat--Sole: second-level concavity implies the associated double Turan inequalities via Csordas--Dimitrov",
    ),
    Rule(
        ("xf7_first_laguerre_positive_s_sqrt", "xi_kernel_positive_strict_decrease"),
        "xf7_b0_positive",
        ClaimStatus.EXACT,
        "F(r^2)=Phi(r)^2 B0(r)/(4 r^3), with Phi>0 and r>0",
    ),
    Rule(
        ("xf7_b0_positive", "xi_kernel_positive_strict_decrease"),
        "xf7_radial_log_slope_ratio_increasing",
        ClaimStatus.EXACT,
        "d[A0(r)/r]/dr=B0(r)/r^2>0 and A0=-Phi'/Phi>0",
    ),
    Rule(
        ("xf7_b0_positive", "xi_kernel_positive_strict_decrease"),
        "xi_kernel_strict_log_concavity_tp2",
        ClaimStatus.EXACT,
        "B0=r A0'-A0>0 with A0>0 gives A0'>A0/r>0 and (log Phi)''=-A0'<0",
    ),
    Rule(
        ("xf7_radial_log_slope_ratio_increasing",),
        "xf7_adaptive_transverse_mass_envelope",
        ClaimStatus.EXACT,
        "q=A0/r positive increasing gives M(a,b)<=M(a,0) exp[-b^2 q(a-|b|)]",
    ),
    Rule(
        (
            "xf7_adaptive_transverse_mass_envelope",
            "xf6_transverse_mass_strict_abs_b_decay",
        ),
        "xf7_signed_cosine_tail_ibp_bound",
        ClaimStatus.EXACT,
        "one integration by parts for monotone M preserves cosine cancellation and gives |tail|<=M(a,r)/|x|",
    ),
    Rule(
        (
            "xf6_exact_positive_curvature_corridor",
            "xf7_signed_cosine_tail_ibp_bound",
        ),
        "xf7_global_signed_core_tail_domination",
        ClaimStatus.OPEN,
        "uniform correlated control must include the remaining a-oscillatory sector and close the full XF-5 integral for every real x and 0<|y|<1/2",
    ),
    Rule(
        ("xf7_global_signed_core_tail_domination",),
        "xi_wiener_laguerre_strict_positivity",
        ClaimStatus.STANDARD,
        "XF-7 signed core-tail gate is a sufficient global sign bound for the XF-5 integral representation",
    ),
)


XF7_SOLVER = ClaimSolver((*HALF_AXIS_RULES, *XF6_RULES, *XF7_RULES))
