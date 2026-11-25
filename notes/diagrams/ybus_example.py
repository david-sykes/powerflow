"""Draw the 4-bus example network for the Ybus section.

Used in notes/02_power_flow_equations.md section 9.
Run: uv run python notes/diagrams/ybus_example.py
"""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle

out = Path(__file__).with_suffix(".svg")

BUS, BRANCH = "#1d1d1b", "#2563eb"

pos = {1: (0, 0), 2: (0, 2), 3: (3, 0), 4: (6, 0)}
branches = [(1, 2), (1, 3), (3, 4)]

fig, ax = plt.subplots(figsize=(6.5, 2.8))

for i, k in branches:
    (x0, y0), (x1, y1) = pos[i], pos[k]
    ax.plot([x0, x1], [y0, y1], color=BRANCH, lw=2, zorder=1)
    mx, my = (x0 + x1) / 2, (y0 + y1) / 2
    dx, dy = (0.45, 0) if x0 == x1 else (0, 0.35)
    ax.text(mx + dx, my + dy, f"$y_{{{i}{k}}}$", color=BRANCH, ha="center", va="center", fontsize=14)

for b, (x, y) in pos.items():
    ax.add_patch(Circle((x, y), 0.32, facecolor="white", edgecolor=BUS, lw=2, zorder=2))
    ax.text(x, y, str(b), ha="center", va="center", fontsize=13, zorder=3)

ax.set_xlim(-0.8, 6.8)
ax.set_ylim(-0.6, 2.6)
ax.set_aspect("equal")
ax.axis("off")
fig.savefig(out, facecolor="white", bbox_inches="tight")
