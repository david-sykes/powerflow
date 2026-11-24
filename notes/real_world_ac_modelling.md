# Real-world AC modelling

How real network equipment and conventions map onto the power flow equations in [power_flow_equations.md](power_flow_equations.md).

## 1. Balanced three-phase modelling

To cover:

- Three phases, 120° apart
- What "balanced" means, and why one phase is enough
- Line-to-line and line-to-neutral voltages (the √3 factor)
- Three-phase power and one-phase power

## 2. Shunts

To cover:

- A shunt is a branch from a bus to ground, and ground is at V = 0
- So it adds y_shunt V_i to the KCL equation, and y_shunt to the Ybus diagonal Y_ii
- Examples: capacitor banks, reactors, line capacitance

## 3. Lines: the pi model

To cover:

- Series impedance R + jX between the two buses
- Half the shunt admittance, jB/2, from each end to ground
- Parameters per km (ohm/km, nF/km) times the length
- Short lines: B can be ignored. Cables: B matters even when short

## 4. Transformers

To cover:

- Ideal transformer: voltage ratio and current ratio
- Series impedance from the nameplate data
- Off-nominal tap ratio and phase shift
- The transformer as a pi model, and its Ybus entries
- With per-unit at nominal ratio, it becomes 1:1

## 5. Conventions in the field

To cover:

- Quoted voltages are RMS and line-to-line (11 kV, 400 V, 230 V)
- Quoted power is three-phase (MW, Mvar)
- Insulation ratings are in kV peak
- Loads are entered with the load sign (p_mw = +1 means 1 MW drawn), but the equations use injections, so the sign flips
