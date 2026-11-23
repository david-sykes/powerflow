# powerflow

A small steady-state AC power flow solver in Python. It works for transmission and distribution networks. Inspired by [microgrid](https://github.com/david-sykes/microgrid).

## Scope

### Analyses

Planned, in build order:

1. **AC power flow**: Newton-Raphson in polar form first. Gauss-Seidel and fast decoupled later, for comparison.
2. **DC power flow** and **sensitivity factors** (PTDF, LODF).
3. **Contingency analysis**: N-1 outages, screened with DC sensitivities, then checked with AC power flow.
4. **Fault analysis**: balanced 3-phase faults first, then unbalanced faults with symmetrical components.
5. **State estimation**: weighted least squares, with bad-data detection.
6. **Optimal power flow**: economic dispatch, then DC OPF, then AC OPF.
7. **Continuation power flow**: PV curves and the voltage collapse point.
8. **Time-series power flow**: one power flow for each timestep of a load profile.
9. **Unbalanced 3-phase power flow**: a per-phase network model (3x3 branch matrices, wye and delta loads, transformer vector groups) that uses the same Newton-Raphson solver as item 1.

`pandapower` can check items 1 to 6 and item 9. Item 7 needs a different check.

### Out of scope

- Dynamic analyses: transient stability, small-signal stability, and harmonic analysis.

### Constraints

- Each timestep is solved alone.
- Runtime dependency: `numpy` only. `pandapower` is used only to check results.

## Setup

```bash
uv sync
```
