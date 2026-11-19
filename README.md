# powerflow

A small steady-state AC power flow solver in Python. It works for transmission and distribution networks. Inspired by [microgrid](https://github.com/david-sykes/microgrid).

## Scope

- Balanced, positive-sequence networks only. Unbalanced 3-phase networks are out of scope.
- Newton-Raphson solver in polar form.
- Each timestep is solved alone.
- Runtime dependency: `numpy` only. `pandapower` is used only to check results.

## Setup

```bash
uv sync
```
