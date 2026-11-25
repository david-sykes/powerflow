"""Draw the series RLC circuit for notes/02_power_flow_equations.md section 1.

Run: uv run python notes/diagrams/series_rlc.py
"""

from pathlib import Path

import schemdraw
import schemdraw.elements as elm

out = Path(__file__).with_suffix(".svg")

with schemdraw.Drawing(file=str(out), show=False) as d:
    d.config(unit=2.5, fontsize=13)
    elm.SourceSin().up().label(["−", "$v(t)$", "+"])
    elm.Resistor().right().label("$R$").label("$v_R$", loc="bottom", ofst=0.5)
    elm.Inductor2().right().label("$L$").label("$v_L$", loc="bottom", ofst=0.5)
    elm.Capacitor().down().label("$C$", ofst=0.3).label("$v_C$", loc="bottom", ofst=0.5)
    elm.Line().left().tox(0)
    elm.CurrentLabelInline(direction="in").at(d.elements[1]).label("$i(t)$")
