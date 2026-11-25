"""Draw KCL at one bus: an injection I_i and branch currents to two neighbours.

Used in notes/02_power_flow_equations.md section 8.
Run: uv run python notes/diagrams/kcl_bus.py
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle

out = Path(__file__).with_suffix(".svg")

BUS, BRANCH, INJ = "#1d1d1b", "#2563eb", "#dc2626"

fig, ax = plt.subplots(figsize=(7, 4.2))

buses = {"i": (0, 0), "k=1": (4, 1.6), "k=2": (4, -1.6)}
labels = {"i": "bus i\n$V_i$", "k=1": "bus 1\n$V_1$", "k=2": "bus 2\n$V_2$"}

# Branches with admittance labels and current arrows (positive away from bus i)
for k, name in [("k=1", "1"), ("k=2", "2")]:
    (x0, y0), (x1, y1) = buses["i"], buses[k]
    ax.plot([x0, x1], [y0, y1], color=BRANCH, lw=2, zorder=1)
    mx, my = (x0 + x1) / 2, (y0 + y1) / 2
    ax.text(mx, my + (0.35 if y1 > 0 else -0.35), f"$y_{{i{name}}}$", color=BRANCH,
            ha="center", va="center", fontsize=13)
    ax.annotate("", xy=(x0 + 0.62 * (x1 - x0), y0 + 0.62 * (y1 - y0)),
                xytext=(x0 + 0.38 * (x1 - x0), y0 + 0.38 * (y1 - y0)),
                arrowprops=dict(arrowstyle="-|>", color=BRANCH, lw=2.5, mutation_scale=18))
    ax.text(mx + 0.35, my + (-0.35 if y1 > 0 else 0.35), f"$I_{{i{name}}}$", color=BRANCH,
            ha="center", va="center", fontsize=13)

# Buses
for b, (x, y) in buses.items():
    ax.add_patch(Circle((x, y), 0.32, facecolor="white", edgecolor=BUS, lw=2, zorder=2))
    ax.text(x + (0.0 if b == "i" else 0.6), y + (-0.75 if b == "i" else 0), labels[b],
            ha="left" if b != "i" else "center", va="center", fontsize=11)

# Injection from devices at bus i
ax.annotate("", xy=(-0.34, 0), xytext=(-2.0, 0),
            arrowprops=dict(arrowstyle="-|>", color=INJ, lw=2.5, mutation_scale=18))
ax.text(-1.2, 0.35, "$I_i$", color=INJ, ha="center", fontsize=13)
ax.text(-2.1, 0, "devices\n(generators,\nloads)", ha="right", va="center", fontsize=10, color=INJ)

ax.set_xlim(-3.6, 5.6)
ax.set_ylim(-2.4, 2.4)
ax.set_aspect("equal")
ax.axis("off")
fig.savefig(out, facecolor="white", bbox_inches="tight")
