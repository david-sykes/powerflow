"""Draw three-phase phasors, a star connection and a delta connection.

Used in notes/03_network_modelling.md section 1.
Run: uv run python notes/diagrams/three_phase.py
"""

import math
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Arc, Circle, Rectangle
from matplotlib.transforms import Affine2D

out = Path(__file__).with_suffix(".svg")

COL = {"a": "#dc2626", "b": "#ca8a04", "c": "#2563eb"}
INK, MUTED = "#1d1d1b", "#6b6a64"


def arrow(ax, x0, y0, x1, y1, col, lw=2.5):
    ax.annotate("", xy=(x1, y1), xytext=(x0, y0),
                arrowprops=dict(arrowstyle="-|>", color=col, lw=lw, mutation_scale=16))


def box(ax, x0, y0, x1, y1, label=None):
    """A wire from (x0, y0) to (x1, y1) with an impedance box in the middle."""
    mx, my = (x0 + x1) / 2, (y0 + y1) / 2
    ang = math.degrees(math.atan2(y1 - y0, x1 - x0))
    L = math.hypot(x1 - x0, y1 - y0)
    w, h = min(0.9, L * 0.45), 0.32
    ax.plot([x0, x1], [y0, y1], color=INK, lw=1.8, zorder=1)
    r = Rectangle((mx - w / 2, my - h / 2), w, h, facecolor="white", edgecolor=INK, lw=1.8, zorder=2)
    r.set_transform(Affine2D().rotate_deg_around(mx, my, ang) + ax.transData)
    ax.add_patch(r)
    if label:
        ax.text(mx, my, label, ha="center", va="center", fontsize=10, zorder=3)


def terminal(ax, x, y, name, dx=0.0, dy=0.25):
    ax.add_patch(Circle((x, y), 0.08, color=COL[name], zorder=3))
    ax.text(x + dx, y + dy, name, color=COL[name], ha="center", va="center", fontsize=13, weight="bold")


fig, axes = plt.subplots(1, 3, figsize=(11, 3.9))

# 1. Phasors
ax = axes[0]
ax.axhline(0, color="#dddddd", lw=1)
ax.axvline(0, color="#dddddd", lw=1)
for name, deg in [("a", 0), ("b", -120), ("c", 120)]:
    t = math.radians(deg)
    arrow(ax, 0, 0, 1.6 * math.cos(t), 1.6 * math.sin(t), COL[name])
    ax.text(1.95 * math.cos(t), 1.95 * math.sin(t), f"$V_{name}$", color=COL[name],
            ha="center", va="center", fontsize=14)
ax.add_patch(Arc((0, 0), 1.0, 1.0, theta1=0, theta2=120, color=MUTED, lw=1))
ax.text(0.45, 0.55, "120°", fontsize=10, color=MUTED)
ax.set_title("Three phases, 120° apart", fontsize=12)
ax.set_xlim(-2.3, 2.4)
ax.set_ylim(-2.2, 2.2)

# 2. Star (wye)
ax = axes[1]
N = (0, 0)
ends = {"a": (0, 1.9), "b": (-1.65, -0.95), "c": (1.65, -0.95)}
for name, (x, y) in ends.items():
    box(ax, N[0], N[1], x, y, "Z")
    terminal(ax, x, y, name, dx=0.0 if name == "a" else (-0.3 if name == "b" else 0.3), dy=0.3 if name == "a" else -0.2)
ax.add_patch(Circle(N, 0.1, color=INK, zorder=3))
ax.text(0.28, 0.05, "N", fontsize=13, weight="bold", va="center")
# Earth symbol below the neutral
ax.plot([0, 0], [-0.1, -1.55], color=INK, lw=1.5, ls=":")
for i, w in enumerate([0.36, 0.24, 0.12]):
    ax.plot([-w, w], [-1.55 - i * 0.1] * 2, color=INK, lw=1.5)
ax.text(0.12, -1.0, "earth", fontsize=9, color=MUTED)
ax.set_title("Star (wye): each Z sees line-to-neutral", fontsize=12)
ax.set_xlim(-2.3, 2.3)
ax.set_ylim(-2.1, 2.4)

# 3. Delta
ax = axes[2]
pts = {"a": (0, 1.9), "b": (-1.65, -0.95), "c": (1.65, -0.95)}
for p, q in [("a", "b"), ("b", "c"), ("c", "a")]:
    box(ax, *pts[p], *pts[q], "Z")
for name, (x, y) in pts.items():
    terminal(ax, x, y, name, dx=0.0 if name == "a" else (-0.3 if name == "b" else 0.3), dy=0.3 if name == "a" else -0.2)
ax.text(0, -1.6, "no neutral", fontsize=9, color=MUTED, ha="center")
ax.set_title("Delta: each Z sees line-to-line", fontsize=12)
ax.set_xlim(-2.3, 2.3)
ax.set_ylim(-2.1, 2.4)

for ax in axes:
    ax.set_aspect("equal")
    ax.axis("off")
fig.tight_layout()
fig.savefig(out, facecolor="white", bbox_inches="tight")
