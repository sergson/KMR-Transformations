<!-- 
License: CC BY-SA 4.0 (see LICENSE-CC.md)
-->

### For Theoretical Content
- All mathematical formulations and documentation must be licensed under **CC BY-SA 4.0**
- When adding new theoretical content, include the header:
```markdown
<!-- 
License: CC BY-SA 4.0 (see LICENSE-CC.md)
-->
```

# 22. Complex KMR Continuation: The Genesis of Trigonometry
**Author**: Sergei Terikhov  
**Date**: 18.10.2026

## Abstract

We show that complexifying the KMR chain parameter — replacing the real $K$ by $K=it$ — produces a perfect circle in the complex plane, and that classical sine and cosine appear as rational projections of the complex flow. Trigonometry is not imported from outside: it is born from the division operation of the complex projective Abel basis. The construction is self-contained and requires only the chain algebra of S_00020.

---

## 22.1. Imaginary Chain Parameter

Let the modulation parameter of the KMR chain become purely imaginary: $K = it$. Then

$$
f^{t}(x) = \frac{x}{1 + i t x}
= x \odot (i t),
$$

a homogeneous chain of length $t$ with purely imaginary parameter. Denote $u = 1/x$ (real), $z = f^t(x)$ (complex):

$$
\frac{1}{z} = u + i t
\implies
z(t) = \frac{1}{u + it} = \frac{u - it}{u^2 + t^2}.
$$

Separating real and imaginary parts:

$$
\mathop{\mathrm{Re}} z = \frac{u}{u^2 + t^2},
\qquad
\mathop{\mathrm{Im}} z = -\frac{t}{u^2 + t^2}.
$$

**Chain reading.** An imaginary parameter rotates the chain in the complex plane. The step $K = it$ is still a Möbius map, but its trajectory is a circle rather than a hyperbola. This is the precise sense in which trigonometry is a chain phenomenon: the chain $\odot(it)$ is the generator of rotation.

---

## 22.2. The Circle Invariant

Squaring and adding:

$$
(\mathop{\mathrm{Re}} z)^2 + (\mathop{\mathrm{Im}} z)^2 = \frac{1}{u^2 + t^2}.
$$

Reduction to canonical form gives:

$$
\left( \mathop{\mathrm{Re}} z - \frac{1}{2u} \right)^2 + (\mathop{\mathrm{Im}} z)^2 = \left( \frac{1}{2u} \right)^2.
$$

The point $z(t)$ therefore describes a perfect circle in the complex plane with radius $R = 1/(2u)$, centered at $(1/(2u), 0)$.

**Contrast with real 2D.** The real 2D cross-chain of S_00021 preserves a quadratic form of signature $(+,-)$, giving hyperbolas. The complex chain here preserves a form of signature $(+,+)$, giving circles. The transition is exactly the replacement of a real parameter by a purely imaginary one.

---

## 22.3. Sine and Cosine as Rational Projections

Classical $\sin t$ and $\cos t$ are rational projections of the complex KMR flow:

$$
\cos t = \frac{u}{\sqrt{u^2 + t^2}},
\qquad
\sin t = \frac{t}{\sqrt{u^2 + t^2}}.
$$

These expressions are exactly the normalizations of $\mathop{\mathrm{Re}} z$ and $-\mathop{\mathrm{Im}} z$ by the radius $R = 1/\sqrt{u^2+t^2}$. In other words, trigonometry is not introduced from outside — circular rotation is born from the division operation of the complex projective Abel basis, i.e. from an **imaginary-parameter chain**.

---

## 22.4. Relation to Euler's Formula

The complex flow can be written

$$
z(t) = \frac{1}{u + it}
= \frac{1}{\sqrt{u^2+t^2}} \left( \cos t - i \sin t \right).
$$

Equivalently,

$$
\frac{z(t)}{|z(t)|} = e^{-i\theta(t)},
\qquad
\theta(t) = \arctan(t/u),
$$

so the complex chain of parameter $it$ **is** a rotation by angle $\theta(t) = \arctan(t/u)$. Euler's formula is thus the polar form of the KMR complex chain; the Möbius step $x \odot (it)$ and the rotation $e^{-i\theta}$ are two views of the same object.

**De Moivre.** Iterating the chain $n$ times corresponds to adding the parameter $n\cdot it$, i.e. to rotating by $n\theta$. This is the chain-algebraic content of de Moivre's formula: homogeneous collapse in the complex chain is angle addition.

---

## 22.5. Conclusion

Complexifying the KMR chain parameter produces:

- a perfect circle in the complex plane (§22.2);
- classical $\sin,\cos$ as rational projections of the flow (§22.3);
- Euler's formula as the polar form of the chain (§22.4);
- de Moivre's formula as homogeneous collapse of an imaginary-parameter chain (§22.4).

Trigonometry is not an external import. It is what the KMR chain looks like when the parameter is imaginary.

---

## 22.6. Appendix: Summary

| Object | Formula |
| :--- | :--- |
| Complex flow | $z(t) = \dfrac{1}{u+it}$ |
| Components | $\mathop{\mathrm{Re}} z = \dfrac{u}{u^2+t^2},\; \mathop{\mathrm{Im}} z = -\dfrac{t}{u^2+t^2}$ |
| Circle radius | $R = \dfrac{1}{2u}$ |
| Projections | $\cos t = \dfrac{u}{\sqrt{u^2+t^2}},\; \sin t = \dfrac{t}{\sqrt{u^2+t^2}}$ |
| Euler form | $z/\lvert z \rvert = e^{-i\arctan(t/u)}$ |

## 22.7. Python Reference

```python
"""
KMR Complex Continuation: Reference Implementation
License: GPL 3.0 (see LICENSE)
"""

from __future__ import annotations
import math
from typing import Tuple


def complex_flow(u: float, t: float) -> complex:
    """z(t) = 1 / (u + i t)."""
    return 1.0 / complex(u, t)


def complex_components(u: float, t: float) -> Tuple[float, float]:
    """Return (Re z, Im z) for z = 1 / (u + i t)."""
    denom = u * u + t * t
    if denom == 0.0:
        return (float("nan"), float("nan"))
    return (u / denom, -t / denom)


def complex_invariant(u: float, t: float) -> float:
    """|z|^2 = 1 / (u^2 + t^2)."""
    denom = u * u + t * t
    if denom == 0.0:
        return float("nan")
    return 1.0 / denom


def trig_projection(u: float, t: float) -> Tuple[float, float]:
    """(cos t, sin t) as projections of the complex flow."""
    norm = math.sqrt(u * u + t * t)
    if norm == 0.0:
        return (float("nan"), float("nan"))
    return (u / norm, t / norm)
