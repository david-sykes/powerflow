# Power flow equations

## 1. Voltage and current in an RLC circuit

![Series RLC circuit](diagrams/series_rlc.svg)

The source voltage is a cosine with peak $V_m$ and angular frequency $\omega = 2\pi f$:

$$v(t) = V_m\cos(\omega t)$$

The elements are in series, so the same current $i(t)$ flows through all three.

**Kirchhoff's voltage law** around the loop:

$$v(t) = v_R + v_L + v_C$$

The voltage across each element:

$$v_R = R i(t)$$

$$v_L = L\frac{di}{dt}$$

$$\frac{dv_C}{dt} = \frac{i(t)}{C} \quad\Rightarrow\quad v_C = \frac{1}{C}\int i(t) dt$$

So putting that all together gives:

$$V_m\cos(\omega t) = R i(t) + L\frac{di}{dt} + \frac{1}{C}\int i(t) dt$$

This is one equation with one unknown function, $i(t)$. It is a differential equation, and its solution has two parts:

- **Transient part:** dies away after the circuit switches on. Power flow ignores it.
- **Steady-state part:** a cosine at the same frequency $\omega$, with a different peak $I_m$ and a phase shift $\varphi$:

$$i(t) = I_m\cos(\omega t + \varphi)$$

To find $I_m$ and $\varphi$, substitute this $i(t)$ into the equation, expand all the sin and cos terms, and match coefficients. This is messy and requires a lot of trigonometry, hence the complex representation.

Unlike a resistor alone, there is no fixed ratio between $v(t)$ and $i(t)$. The inductor and capacitor make the voltage depend on how fast the current changes, so $v(t)/i(t)$ varies through the cycle. In the complex representation, this ratio becomes a constant, $Z$.

## 2. Complex representation and phasors

We use a complex representation of $v(t)$ and $i(t)$ to make the maths a lot simpler. Euler's formula links a cosine to a complex exponential:

$$e^{j\theta} = \cos\theta + j\sin\theta$$

So each cosine is the real part of a complex number that rotates at $\omega$:

$$v(t) = \text{Re}\lbrace V_m\cos(\omega t) + jV_m\sin(\omega t) \rbrace = \text{Re}\lbrace V_m e^{j\omega t} \rbrace$$

$$i(t) = \text{Re}\lbrace I_m\cos(\omega t+\varphi) + jI_m\sin(\omega t+\varphi) \rbrace = \text{Re}\lbrace I_m e^{j(\omega t+\varphi)} \rbrace$$

**Why we can do this.** The circuit equation is linear and $R$, $L$, $C$ are real. Taking the real part gives the same result before or after a derivative, an integral or a multiplication by a real constant. So if the complex versions satisfy the equation, their real parts do too.

**Calculus becomes algebra.** The exponential is easy to differentiate and integrate:

$$\frac{d}{dt}e^{j(\omega t+\varphi)} = j\omega  e^{j(\omega t+\varphi)} \qquad \int e^{j(\omega t+\varphi)} dt = \frac{1}{j\omega}  e^{j(\omega t+\varphi)}$$

(The constant of integration would be a DC offset. Steady state has none, so we drop it.)

So going back to KVL, $v = v_R + v_L + v_C$:

$$V_m e^{j\omega t} = R I_m e^{j(\omega t+\varphi)} + j\omega L I_m e^{j(\omega t+\varphi)} + \frac{1}{j\omega C} I_m e^{j(\omega t+\varphi)}$$

Rearranging:

$$V_m e^{j\omega t} = I_m e^{j\varphi} e^{j\omega t}\left(R + j\omega L + \frac{1}{j\omega C}\right)$$

**Phasors.** The factor $e^{j\omega t}$ is on both sides, so it cancels. This is where the steady-state assumption pays off: every voltage and current is a sinusoid at the same $\omega$, so $e^{j\omega t}$ cancels from every equation. What remains is one complex number per quantity, which holds its magnitude and its phase angle. This is the **phasor**. With the source as the angle reference:

$$V = V_m \qquad I = I_m e^{j\varphi}$$

$$\boxed{V = Z I} \qquad Z = R + j\omega L + \frac{1}{j\omega C}$$

This is Ohm's law with complex numbers. The time has gone, and the differential equation is now one line of algebra.

To get back to the time domain, multiply by $e^{j\omega t}$ and take the real part: $i(t) = \text{Re}\lbrace I e^{j\omega t} \rbrace$.

## 3. Impedance and the phase shift

What this means physically: $\lvert Z \rvert$ sets the size of the current, and the reactive parts $j\omega L$ and $\frac{1}{j\omega C}$ set the phase shift $\varphi$. This section shows the maths.

Tidy $Z$ first. Since $j \cdot (-j) = 1$, we have $\frac{1}{j} = -j$. So:

$$Z = R + j\left(\omega L - \frac{1}{\omega C}\right) = R + jX$$

| Symbol | Name | Value |
| --- | --- | --- |
| $R$ | resistance | real part of $Z$ |
| $X_L$ | inductive reactance | $\omega L$ |
| $X_C$ | capacitive reactance | $\frac{1}{\omega C}$ |
| $X$ | reactance | $X_L - X_C$, the imaginary part of $Z$ |

**Polar form.** Write $Z$ as a magnitude and an angle (see the appendix):

$$Z = |Z| e^{j\theta_Z} \qquad |Z| = \sqrt{R^2 + X^2} \qquad \theta_Z = \text{atan2}(X, R)$$

**The phase shift.** To divide complex numbers in polar form, divide the magnitudes and subtract the angles:

$$I = \frac{V}{Z} = \frac{V_m e^{j0}}{|Z| e^{j\theta_Z}} = \frac{V_m}{|Z|} e^{-j\theta_Z}$$

Compare this with $I = I_m e^{j\varphi}$:

$$\boxed{I_m = \frac{V_m}{|Z|} \qquad \varphi = -\theta_Z}$$

| Case | $X$ | $\theta_Z$ | Current |
| --- | --- | --- | --- |
| Inductive | $X > 0$ | $0^\circ$ to $90^\circ$ | lags the voltage |
| Capacitive | $X < 0$ | $-90^\circ$ to $0^\circ$ | leads the voltage |
| Resonance | $X = 0$ | $0^\circ$ | in phase, and at its maximum $V_m/R$ |

Resonance occurs when $X_L = X_C$, at $\omega_0 = 1/\sqrt{LC}$.

**Example.** Take $R = 10$ Ω and $X = 10$ Ω. Then:

$$|Z| = \sqrt{10^2 + 10^2} = 14.1 \ \Omega \qquad \theta_Z = \text{atan2}(10, 10) = 45^\circ$$

So $I_m = V_m / 14.1$ and the current lags the voltage by 45°. At 50 Hz one cycle takes 20 ms, so the time shift is:

$$\frac{45}{360} \times 20 \text{ ms} = 2.5 \text{ ms}$$

Try it: [demos/rlc_series.html](../demos/rlc_series.html).

## 4. Admittance (Y, G, B)

## 5. Instantaneous power to complex power (S = VI*)

## 6. Kirchhoff's current law at each bus

## 7. Building the Ybus matrix

## 8. Complex power at each bus in terms of Y and V

## 9. Separate equations for P and Q

## 10. Bus types and the count of equations and unknowns

## 11. Newton-Raphson on the unknown subset

## 12. Fill in the remaining values

## 13. Per-unit system

## Appendix: complex number toolkit

| Fact | Formula |
| --- | --- |
| Definition | $j^2 = -1$, so $\frac{1}{j} = -j$ |
| Rectangular form | $z = a + jb$ |
| Polar form | $z = r e^{j\theta} = r(\cos\theta + j\sin\theta)$ |
| Rectangular to polar | $r = \sqrt{a^2 + b^2}$, $\theta = \text{atan2}(b, a)$ |
| Polar to rectangular | $a = r\cos\theta$, $b = r\sin\theta$ |
| Multiply | multiply the magnitudes, add the angles |
| Divide | divide the magnitudes, subtract the angles |
| Multiply by $j$ | $j = e^{j\pi/2}$, so it turns a phasor $90^\circ$ forward |
| Conjugate | $z^{\ast} = a - jb = r e^{-j\theta}$, and $z z^{\ast} = r^2$ |

Use `atan2(b, a)`, not `atan(b/a)`. `atan` loses the quadrant when $a < 0$. In numpy: `np.abs(z)`, `np.angle(z)`, `np.conj(z)`.

Multiply by $j$ explains the inductor: $V_L = j\omega L I$, so the inductor voltage is $90^\circ$ ahead of the current. The capacitor has $-j$, so its voltage is $90^\circ$ behind.
