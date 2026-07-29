#!/usr/bin/env python3
"""Normalize LaTeX references and line breaking before monograph compilation.

The transformations are deterministic and idempotent. They do not alter any
scientific formula or numerical result; they only repair cross-references and
prevent non-breaking paths/tables from overflowing the page.
"""
from __future__ import annotations

from pathlib import Path


def replace(path: str, old: str, new: str, count: int = -1) -> bool:
    p = Path(path)
    text = p.read_text(encoding="utf-8")
    if old not in text:
        print(f"SKIP already normalized: {path}")
        return False
    p.write_text(text.replace(old, new, count), encoding="utf-8")
    print(f"UPDATED: {path}")
    return True


def main() -> None:
    root = "TIR/monograph/metatime_monograph.tex"
    replace(
        root,
        "\\usepackage{graphicx}\n\\usepackage{hyperref}",
        "\\usepackage{graphicx}\n\\usepackage{xurl}\n\\usepackage{microtype}\n\\usepackage{hyperref}",
        1,
    )
    replace(
        root,
        "]{geometry}\n",
        "]{geometry}\n\\setlength{\\emergencystretch}{3em}\n",
        1,
    )

    app_m = "TIR/monograph/appendices/appM_prospective_observable_identifiability.tex"
    replace(
        app_m,
        "\\label{app:observable_identifiability}\n",
        "\\label{app:observable_identifiability}\n"
        "\\label{app:prospective_observable_identifiability}\n",
        1,
    )
    replace(app_m, "\\texttt{heavy\\_quark\\_resonance}", "\\path{heavy_quark_resonance}")
    replace(app_m, "\\texttt{charged\\_lepton\\_small\\_seed}", "\\path{charged_lepton_small_seed}")
    replace(
        app_m,
        "\\texttt{TIR/validation/up\\_sector\\_observable\\_identifiability\\_v10\\_6.py}",
        "\\path{TIR/validation/up_sector_observable_identifiability_v10_6.py}",
    )

    app_n = "TIR/monograph/appendices/appN_separable_candidate_family.tex"
    replace(
        app_n,
        "Appendix~\\ref{app:prospective_observable_identifiability}",
        "Appendix~\\ref{app:observable_identifiability}",
    )
    replace(
        app_n,
        """\\[
\\boxed{
\\text{candidate family frozen}
\\;\\land\\;
\\text{no mass benchmark}
\\;\\land\\;
\\text{no candidate selected}
\\;\\land\\;
\\text{canonical promotion denied}
}
\\]""",
        """\\[
\\boxed{
\\begin{gathered}
\\text{candidate family frozen}
\\;\\land\\;
\\text{no mass benchmark}\\\\
\\text{no candidate selected}
\\;\\land\\;
\\text{canonical promotion denied}
\\end{gathered}
}
\\]""",
    )
    replace(
        app_n,
        "\\texttt{TIR/validation/separable\\_universal\\_candidate\\_family\\_v10\\_7.py}",
        "\\path{TIR/validation/separable_universal_candidate_family_v10_7.py}",
    )
    replace(
        app_n,
        "\\texttt{2bbf9985b6a4fc9d19d039e117b15eb446a51a3e8828a2894c8d797bb35f23f4}",
        "\\path{2bbf9985b6a4fc9d19d039e117b15eb446a51a3e8828a2894c8d797bb35f23f4}",
    )

    app_k = "TIR/monograph/appendices/appK_sector_holonomy_release.tex"
    replace(
        app_k,
        "\\chapter{Sector-Holonomy Release of the Collatz Quarter-Power Trace}",
        "\\chapter[Sector-Holonomy Release]{Sector-Holonomy Release of the Collatz Quarter-Power Trace}",
        1,
    )
    replace(
        app_k,
        "\\texttt{TIR/validation/collatz\\_sector\\_holonomy\\_mass\\_audit\\_v10\\_2.py}",
        "\\path{TIR/validation/collatz_sector_holonomy_mass_audit_v10_2.py}",
    )
    replace(
        app_k,
        "\\texttt{TIR/validation/collatz\\_sector\\_holonomy\\_mass\\_audit\\_v10\\_2r1.py}",
        "\\path{TIR/validation/collatz_sector_holonomy_mass_audit_v10_2r1.py}",
    )

    app_j = "TIR/monograph/appendices/appJ_collatz_quarter_power_scaling.tex"
    replace(
        app_j,
        "\\texttt{TIR/validation/collatz\\_quarter\\_power\\_mass\\_audit\\_v10\\_1.py}",
        "\\path{TIR/validation/collatz_quarter_power_mass_audit_v10_1.py}",
    )

    app_l = "TIR/monograph/appendices/appL_up_sector_common_baseline_no_go.tex"
    replace(app_l, "\\texttt{light\\_quark\\_seed}", "\\path{light_quark_seed}")
    replace(app_l, "\\texttt{heavy\\_quark\\_resonance}", "\\path{heavy_quark_resonance}")
    replace(
        app_l,
        "\\texttt{TIR/validation/up\\_sector\\_common\\_baseline\\_no\\_go\\_v10\\_4.py}",
        "\\path{TIR/validation/up_sector_common_baseline_no_go_v10_4.py}",
    )

    ch31 = "TIR/monograph/chapters/ch31_open_problems.tex"
    replace(
        ch31,
        "\\subsection{Sector-Holonomy Release (Retrospective Signal; Absolute Offset Open)}",
        "\\subsection{Sector-Holonomy Release (Retrospective; Offset Open)}",
        1,
    )

    app_f = "TIR/monograph/appendices/appF_baryon_calculations.tex"
    replace(
        app_f,
        """\\[
\\begin{array}{ccccccc}
\\text{Particle} & Y & I(I{+}1) & \\beta Y & \\gamma(I(I{+}1){-}Y^2/4) & \\text{Mass (MeV)} & \\text{PDG (MeV)} \\\\
\\hline
p,n & 1 & 0.75 & -185.90 & 38.73(0.75{-}0.25) = 19.37 & 925.95{+}189.77{-}185.90{+}19.37 = 949.19 & 938.92 \\\\
\\Lambda & 0 & 0 & 0 & 0 & 925.95{+}189.77 = 1115.72 & 1115.68 \\\\
\\Sigma & 0 & 2 & 0 & 38.73(2{-}0) = 77.46 & 925.95{+}189.77{+}77.46 = 1193.18 & 1193.15 \\\\
\\Xi & -1 & 0.75 & +185.90 & 38.73(0.75{-}0.25) = 19.37 & 925.95{+}189.77{+}185.90{+}19.37 = 1320.99 & 1318.29 \\\\
\\end{array}
\\]""",
        """\\begin{center}
\\resizebox{\\textwidth}{!}{$
\\begin{array}{ccccccc}
\\text{Particle} & Y & I(I{+}1) & \\beta Y & \\gamma(I(I{+}1){-}Y^2/4) & \\text{Mass (MeV)} & \\text{PDG (MeV)} \\\\
\\hline
p,n & 1 & 0.75 & -185.90 & 38.73(0.75{-}0.25) = 19.37 & 925.95{+}189.77{-}185.90{+}19.37 = 949.19 & 938.92 \\\\
\\Lambda & 0 & 0 & 0 & 0 & 925.95{+}189.77 = 1115.72 & 1115.68 \\\\
\\Sigma & 0 & 2 & 0 & 38.73(2{-}0) = 77.46 & 925.95{+}189.77{+}77.46 = 1193.18 & 1193.15 \\\\
\\Xi & -1 & 0.75 & +185.90 & 38.73(0.75{-}0.25) = 19.37 & 925.95{+}189.77{+}185.90{+}19.37 = 1320.99 & 1318.29 \\\\
\\end{array}
$}
\\end{center}""",
    )


if __name__ == "__main__":
    main()
