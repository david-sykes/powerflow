# AC power flow

## Starting point

From [02_power_flow_equations.md](02_power_flow_equations.md), each bus $i$ has two equations:

$$\boxed{P_i = |V_i| \sum_k |V_k| \left( G_{ik}\cos\theta_{ik} + B_{ik}\sin\theta_{ik} \right)}$$

$$\boxed{Q_i = |V_i| \sum_k |V_k| \left( G_{ik}\sin\theta_{ik} - B_{ik}\cos\theta_{ik} \right)}$$

This note solves them in full, with no approximations. The equipment models and per-unit are in [03_network_modelling.md](03_network_modelling.md).

## What this solver takes from the network model

To cover:

- Everything in [03_network_modelling.md](03_network_modelling.md): R, X and shunt capacitance of lines, transformer impedance, tap and phase shift, shunts
- P and Q for loads and generators, and |V| setpoints for generators
- All values in per-unit

## 1. Knowns and unknowns

To cover:

- Each bus has four quantities. Which are they?
- Each bus has two equations. So how many quantities must we know at each bus?
- What does the network operator actually know at a load, at a generator, and at the grid connection?

## 2. Bus types

To cover:

- PQ, PV and slack buses: what each one fixes, and which real device each one represents
- Why the network needs exactly one slack bus. Two reasons: the Ybus property from the equations note, and the losses
- Count the equations and the unknowns for a network with a given number of PQ and PV buses. Do they match?

## 3. Mismatch equations

To cover:

- Write each equation as "specified value minus calculated value = 0"
- Which equations go into the solver, and which are left out? Why?
- Which variables does the solver change?

## 4. Newton-Raphson

To cover:

- The idea in one variable: follow the tangent line to the zero
- Extend it to many variables. What replaces the derivative?
- The Jacobian: what each entry means, and its block structure
- Build the Jacobian by finite differences first. Then derive it by hand, and check the two against each other
- Starting values ("flat start"), the stop tolerance, the maximum number of iterations, and what to do when it fails to converge
- Warm start: use the last timestep's answer as the start for the next timestep

## 5. Fill in the remaining values

To cover:

- With all voltages known, find the values the solver did not calculate. Which values at which bus types?
- Power flow in each branch, at both ends
- Losses in each branch, and in the whole network
- Why this step needs no iteration

## 6. Generator Q limits

To cover:

- What a real generator can and cannot do to hold its voltage
- What happens when a PV bus needs more Q than the generator can give
- Switch the bus type and solve again

## 7. Other solvers (later)

To cover:

- Gauss-Seidel: simpler, slower. Compare the iteration count with Newton-Raphson
- Fast decoupled: uses the X/R decoupling from [05_dc_power_flow.md](05_dc_power_flow.md). Where does it work, and where does it fail?
