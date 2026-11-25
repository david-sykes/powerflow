# DC power flow

## Starting point

From [02_power_flow_equations.md](02_power_flow_equations.md), each bus $i$ has two equations:

$$\boxed{P_i = |V_i| \sum_k |V_k| \left( G_{ik}\cos\theta_{ik} + B_{ik}\sin\theta_{ik} \right)}$$

$$\boxed{Q_i = |V_i| \sum_k |V_k| \left( G_{ik}\sin\theta_{ik} - B_{ik}\cos\theta_{ik} \right)}$$

This note simplifies them into a linear model. The name "DC" is historical: the model is still AC, but its maths looks like a DC circuit. The equipment models and per-unit are in [03_network_modelling.md](03_network_modelling.md).

## What this solver takes from the network model

To cover:

| Equipment | AC uses | DC uses |
| --- | --- | --- |
| Line | R, X, and the shunt capacitance | X only |
| Transformer | impedance, tap ratio, phase shift | X, and the phase shift |
| Shunt | all of it | nothing |
| Load, generator | P and Q | P only |

- For each dropped item, which DC assumption (section 2) removes it?
- Per-unit: why the DC model can't work without it

## 1. High X and high R: decoupling

To cover:

- Take one line between two buses, with R = 0. What is left of the P and Q equations?
- Which variable mainly drives P? Which variable mainly drives Q?
- Transmission lines have high X/R. Distribution feeders have X/R near 1 or below. What changes?
- Why rooftop solar raises the voltage on LV feeders
- Why distribution networks need the full AC solver

## 2. The DC assumptions

To cover:

- Four assumptions: resistance is ignored, voltage magnitudes are all 1 pu, angle differences are small, and reactive power is ignored
- For each one: why it is reasonable on a transmission network
- Which assumption needs per-unit?

## 3. The linear model

To cover:

- Apply the four assumptions to the P equation. What is left?
- Write it in matrix form. How does the matrix relate to Ybus?
- The Q equation: what happens to it?

## 4. Solving

To cover:

- The slack bus again: why the matrix can't be solved as it is, and what to remove
- One linear solve, with no iteration
- Compare the cost with Newton-Raphson

## 5. Line flows

To cover:

- Flow on each line from the two bus angles
- Why the model has no losses, and what that means for the slack bus

## 6. Accuracy

To cover:

- Run the DC and AC models on the same network and compare the line flows
- Where it works: transmission, light loading
- Where it fails: distribution, heavy loading, large angle differences, voltages far from 1 pu

## 7. Sensitivity factors

To cover:

- PTDF: if a bus injects 1 MW more, how much does the flow on each line change?
- LODF: if a line trips, how much of its flow moves onto each other line?
- Why the linear model makes these quick to calculate
- How contingency analysis uses them (README analysis 3)
