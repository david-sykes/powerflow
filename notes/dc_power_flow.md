# DC power flow

Placeholder. Write this when building the DC power flow (README analysis 2).

To cover:

- Start from the P equation in power_flow_equations.md section 11
- Assumptions: R = 0 (high X/R), |V| = 1 pu, small angle differences (sin θ ≈ θ, cos θ ≈ 1), ignore Q
- Result: P = B θ, a linear equation that solves in one step
- Where it works (transmission) and where it fails (distribution, heavy loading)
- Sensitivity factors (PTDF, LODF) come from the same linear model
