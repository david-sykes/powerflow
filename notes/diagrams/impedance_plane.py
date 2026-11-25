"""Draw Z and I in the complex plane for inductive and capacitive cases.

Used in notes/02_power_flow_equations.md section 3.
Run: uv run python notes/diagrams/impedance_plane.py
"""

import math
from pathlib import Path

import matplotlib.pyplot as plt

out = Path(__file__).with_suffix(".svg")

V_COL, Z_COL, I_COL, AXIS = "#2563eb", "#9333ea", "#dc2626", "#999999"


def arrow(ax, x, y, col, width=2.5):
    ax.annotate("", xy=(x, y), xytext=(0, 0),
                arrowprops=dict(arrowstyle="-|>", color=col, lw=width, mutation_scale=16))


def panel(ax, sign, title):
    """sign=+1 inductive (X > 0), sign=-1 capacitive (X < 0)."""
    r, x = 3.0, 2.0 * sign
    ang = math.atan2(x, r)

    ax.axhline(0, color=AXIS, lw=1)
    ax.axvline(0, color=AXIS, lw=1)
    ax.text(4.6, 0.12, "Re", color=AXIS)
    ax.text(0.12, 2.7, "Im", color=AXIS)

    # V is the reference, on the real axis
    arrow(ax, 4.0, 0, V_COL)
    ax.text(4.05, -0.4, "V", color=V_COL, fontsize=13)

    # Z = R + jX, with the R and X parts dashed
    arrow(ax, r, x, Z_COL)
    ax.plot([r, r], [0, x], "--", color=Z_COL, lw=1)
    ax.text(r + 0.15, x / 2, "X > 0" if sign > 0 else "X < 0", color=Z_COL, va="center")
    ax.text(r / 2 - 0.5, x / 2 + 0.3 * sign, "Z", color=Z_COL, fontsize=13, va="center")

    # I = V / Z: the angle of I is minus the angle of Z (mirror in the real axis)
    il = 2.6
    ix, iy = il * math.cos(-ang), il * math.sin(-ang)
    arrow(ax, ix, iy, I_COL)
    ax.text(ix - 0.6, iy - 0.15 * sign, "I", color=I_COL, fontsize=13, va="center")

    ax.set_title(title, fontsize=12)
    ax.set_xlim(-0.6, 5.0)
    ax.set_ylim(-2.9, 2.9)
    ax.set_aspect("equal")
    ax.axis("off")


fig, axes = plt.subplots(1, 2, figsize=(9, 4.2))
panel(axes[0], +1, "Inductive: X > 0, I lags V")
panel(axes[1], -1, "Capacitive: X < 0, I leads V")
fig.tight_layout()
fig.savefig(out, facecolor="white", bbox_inches="tight")
