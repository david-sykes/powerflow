# Definitions

## Network definitions

A network is made of two things:

- **Bus:** a point in the network with a single voltage (magnitude and angle, measured relative to ground). This could be a connection point, like a substation, or a point where multiple lines meet. Loads and generators connect to buses.
- **Branch:** an element that connects two buses, such as a line or a transformer. It can have its own resistance, inductance and capacitance, but it always joins exactly two buses.

## Physics definitions

The whole system relies on just six physics equations.

### Component equations

| Component | Equation | Intuition |
| --- | --- | --- |
| Resistor (Ohm's law) | $V = IR$ | |
| Inductor | $V = L \dfrac{dI}{dt}$ | Inertia. The larger $L$, the more voltage is needed to change its current. |
| Capacitor | $I = C \dfrac{dV}{dt}$ | A bath tub. The larger $C$, the more current is needed to raise the level ($V$) at the same rate. |

### Kirchhoff's laws

- **Kirchhoff's current law (KCL):** at any bus, the current flowing in equals the current flowing out:
  $$\sum_k I_k = 0$$
- **Kirchhoff's voltage law (KVL):** around any closed loop, the voltage rises and drops sum to zero:
  $$\sum_k V_k = 0$$

### Power

- **Instantaneous power:** the power into any element at time $t$ is the voltage across it times the current through it:
  $$p(t) = v(t) i(t)$$
