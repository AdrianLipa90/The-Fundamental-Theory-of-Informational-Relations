#!/usr/bin/env python3
"""Generate publication figures without encoding any fitted physical claim."""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import mpmath as mp
import numpy as np

# Embed scalable TrueType outlines in PDF figures rather than Type 3 glyphs.
plt.rcParams["pdf.fonttype"] = 42
plt.rcParams["ps.fonttype"] = 42
plt.rcParams["mathtext.fontset"] = "dejavusans"

ROOT = Path(__file__).resolve().parents[1]
FIG = ROOT / "figures"
FIG.mkdir(exist_ok=True)


def binary_entropy_figure() -> None:
    p = np.linspace(1e-5, 1 - 1e-5, 1200)
    h = -p * np.log(p) - (1 - p) * np.log(1 - p)
    fig, ax = plt.subplots(figsize=(6.4, 4.2))
    ax.plot(p, h, linewidth=2)
    ax.axvline(0.5, linewidth=1, linestyle="--")
    ax.scatter([0.5], [np.log(2)], zorder=3)
    ax.set_xlabel(r"$\sigma$")
    ax.set_ylabel(r"$H(\sigma)$ [nats]")
    ax.set_title("Binary entropy and the balanced point")
    ax.grid(alpha=0.25)
    fig.tight_layout()
    fig.savefig(FIG / "binary_entropy.pdf")
    plt.close(fig)


def cancellation_figure() -> None:
    p = np.linspace(0, 1, 1200)
    intensity = (np.sqrt(p) - np.sqrt(1 - p)) ** 2
    fig, ax = plt.subplots(figsize=(6.4, 4.2))
    ax.plot(p, intensity, linewidth=2)
    ax.axvline(0.5, linewidth=1, linestyle="--")
    ax.scatter([0.5], [0], zorder=3)
    ax.set_xlabel(r"$\sigma$")
    ax.set_ylabel(r"$|\sqrt{\sigma}-\sqrt{1-\sigma}|^2$")
    ax.set_title(r"Exact destructive interference at relative phase $\pi$")
    ax.grid(alpha=0.25)
    fig.tight_layout()
    fig.savefig(FIG / "destructive_interference.pdf")
    plt.close(fig)


def bloch_equator_figure() -> None:
    theta = np.linspace(0, 2 * np.pi, 600)
    fig, ax = plt.subplots(figsize=(5.4, 5.4))
    ax.plot(np.cos(theta), np.sin(theta), linewidth=1.6)
    ax.axhline(0, linewidth=0.8)
    ax.axvline(0, linewidth=0.8)
    ax.plot(np.cos(theta), 0.35 * np.sin(theta), linewidth=2)
    ax.annotate(r"equator: $\sigma=1/2$", xy=(0.70, 0.25), xytext=(0.1, 0.62), arrowprops={"arrowstyle": "->"})
    ax.annotate(r"$|0\rangle$", xy=(0, 1), xytext=(0.04, 1.05))
    ax.annotate(r"$|1\rangle$", xy=(0, -1), xytext=(0.04, -1.14))
    ax.set_aspect("equal")
    ax.set_xlim(-1.2, 1.2)
    ax.set_ylim(-1.2, 1.2)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_title("Bloch-sphere schematic: complement exchange and the fixed equator")
    fig.tight_layout()
    fig.savefig(FIG / "bloch_equator.pdf")
    plt.close(fig)


def xi_zero_figure() -> None:
    mp.mp.dps = 35
    t = np.linspace(0, 55, 1800)
    zvals = np.array([float(mp.re(mp.siegelz(float(x)))) for x in t])
    roots = [float(mp.im(mp.zetazero(k))) for k in range(1, 11)]
    fig, ax = plt.subplots(figsize=(7.2, 4.2))
    ax.plot(t, zvals, linewidth=1)
    ax.axhline(0, linewidth=0.8)
    ax.scatter(roots, np.zeros(len(roots)), marker="x", zorder=3)
    ax.set_xlabel(r"$t$ in $s=1/2+it$")
    ax.set_ylabel(r"Hardy $Z(t)$")
    ax.set_title("First sign changes and tabulated critical-line zeros")
    ax.grid(alpha=0.2)
    fig.tight_layout()
    fig.savefig(FIG / "hardy_z_zeros.pdf")
    plt.close(fig)


def main() -> None:
    binary_entropy_figure()
    cancellation_figure()
    bloch_equator_figure()
    xi_zero_figure()
    print(FIG)


if __name__ == "__main__":
    main()
