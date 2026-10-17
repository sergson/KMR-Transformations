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

# 20. Relational KMR Basis: From Abel's Equation to Cascade Invariants and the Hypothesis of Ergodic Symmetry
**Author**: Sergei Terikhov  
**Date**: 18.10.2026

## Abstract

This work establishes the mathematical foundation of the relational KMR algebra (K-modulated Relational algebra) — a framework in which the basis elements of space are not point coordinates but operators of continuous scale transformation. We rigorously derive: the 1D KMR flow, its real hyperbolic 2D extension, the complex circular continuation (genesis of trigonometry), the 3D cascade coupling invariant, and the attractor of an infinite continued fraction. A hypothesis is formulated about the structural symmetry between a spatial ensemble (dimensionality) and a time series (iterations). All philosophical-ontological consequences are placed outside the scope of strict statements.

---

## 20.1. Abel's Functional Equation and the 1D KMR Basis

### 20.1.1. Abel's Equation

The classical Abel functional equation:

$$
\alpha(f(x)) = \alpha(x) + 1
$$

linearizes an iterative process by mapping a nonlinear step $f$ into an additive shift $+1$ in the coordinate $\alpha$. For a continuous parameter $t \in \mathbb{R}$:

$$
f^{t}(x) = \alpha^{-1}(\alpha(x) + t).
$$

Here $f^t$ denotes the continuous Abel iterate, not the pointwise power of $f$.

### 20.1.2. Atomic Kernel

We postulate a complementary pair of fractional-linear Möbius operators:

$$
f(x) = \frac{x}{1+x}, \qquad g(x) = \frac{x}{1-x}.
$$

For the direct kernel:

$$
\frac{1}{f(x)} = \frac{1+x}{x} = \frac{1}{x} + 1.
$$

Therefore, the Abel function has a unique exact expression:

$$
\alpha(x) = \frac{1}{x}, \qquad \alpha^{-1}(z) = \frac{1}{z}.
$$

### 20.1.3. Continuous 1D KMR Flow

Substitution into the canonical formula yields a closed expression:

$$
f^{t}(x) = \frac{x}{1+tx}.
$$

This is a rigorous result without approximations or Taylor series. The corresponding operator:

$$
A \odot K = \frac{A}{1+KA}, \qquad (A \odot K) \odot C = A \odot (K+C).
$$

**Interpretation.** The Abel–Möbius basis is projectively linear: in the coordinate $u = 1/x$, 
the nonlinear step becomes a pure linear shift $u \mapsto u+K$. The origin is not the point $x=0$
but the entire inverse scale: $x \to 0 \iff u \to \infty$.

**Why the basis is an iterator: a plain-language interlude**

In ordinary geometry the basis is a set of fixed directions, and motion is $x(t)=x_0+t\cdot e$: a static vector stretched by a number. The KMR basis does something different. It declares the **step itself** to be the basis element. Motion is no longer addition of a fixed increment; it is **iteration of a scale-sensitive rule**:

For integer $t\ge 0$ let $f^{\circ t}$ denote the $t$-fold iterate:

$$
f^{\circ 0}(x_0)=x_0,\qquad
f^{\circ(t+1)}(x_0)=f\bigl(f^{\circ t}(x_0)\bigr),\qquad
f(x)=\frac{x}{1+x}.
$$

Then

$$
x_t=f^{\circ t}(x_0)
$$

is the trajectory: $x_0=x_0,\ x_1=f(x_0),\ x_2=f(f(x_0)),\dots$.
The map $f$ itself does not depend on $t$ or $x_0$; it is the generator of the step.

For continuous $t$, the iterate is defined through Abel's equation
$\alpha(f(x))=\alpha(x)+1$ with $\alpha(x)=1/x$. Hence

$$
f^{\circ t}(x_0)
=\alpha^{-1}\bigl(\alpha(x_0)+t\bigr)
=\frac{x_0}{1+t\,x_0},
$$

where defined. The point $x_0=0$ is the fixed point and is treated separately.

The coordinate $t$ is no longer a distance along a pre-existing line — it is the **iteration index** (the power of the operator). This is why changing the basis changes the geometry: the group operation is no longer translation in $\mathbb{R}$, but composition of Möbius steps. Abel’s equation $\alpha(f(x))=\alpha(x)+1$ with $\alpha(x)=1/x$ is the isomorphism that linearizes this new group: in the inverse coordinate $u=1/x$, the shrinking Möbius step becomes the ordinary shift $u\mapsto u+1$. The “basis” is therefore not a collection of points but the **generator of the group that produces the space**.

---

## 20.2. Real KMR-2D: Hyperbolic Dynamics

### 20.2.1. Conjugate Pair

Consider the discrete system with cross-modulation:

$$
x_1(n+1) = \frac{x_1(n)}{1 + x_1(n) x_2(n)}, \qquad
x_2(n+1) = \frac{x_2(n)}{1 - x_1(n) x_2(n)}.
$$

In inverse coordinates $u_i = 1/x_i$:

$$
u_1(n+1) = u_1(n) + \frac{1}{u_2(n)}, \qquad
u_2(n+1) = u_2(n) - \frac{1}{u_1(n)}.
$$

### 20.2.2. Continuous Limit and True Invariant

In the infinitesimal limit:

$$
\frac{du_1}{dt} = \frac{1}{u_2}, \qquad
\frac{du_2}{dt} = -\frac{1}{u_1}.
$$

Multiplying the first by $u_2$, the second by $u_1$, and adding:

$$
u_2 \dot u_1 + u_1 \dot u_2 = 0 \implies \frac{d}{dt}(u_1 u_2) = 0.
$$

**Exact invariant:**

$$
u_1 u_2 = C = \text{const}.
$$

**Conclusion.** Real cross-modulation generates not a circle but a hyperbola. 
The trajectory obeys a pseudo-Euclidean Minkowski metric: exponential contraction/expansion, 
but not oscillations. Deriving circular trigonometry from purely real 2D modulation 
is **mathematically inconsistent**.

---

## 20.3. Complex Continuation of KMR-1D and Genesis of Trigonometry

### 20.3.1. Imaginary Step Time

Let the modulation parameter become purely imaginary: $K = i t$. Then

$$
f^{t}(x) = \frac{x}{1 + i t x}.
$$

Denote $u = 1/x$ (real), $z = f^{t}(x)$ (complex):

$$
\frac{1}{z} = u + i t \implies z(t) = \frac{1}{u + i t} = \frac{u - i t}{u^2 + t^2}.
$$

Separating real and imaginary parts:

$$
\mathop{\mathrm{Re}} z = \frac{u}{u^2 + t^2}, \qquad
\mathop{\mathrm{Im}} z = -\frac{t}{u^2 + t^2}.
$$

### 20.3.2. Invariant of the Complex Flow

Squaring and adding:

$$
(\mathop{\mathrm{Re}} z)^2 + (\mathop{\mathrm{Im}} z)^2 = \frac{1}{u^2 + t^2}.
$$

Reduction to canonical form gives:

$$
\left( \mathop{\mathrm{Re}} z - \frac{1}{2u} \right)^2 + (\mathop{\mathrm{Im}} z)^2 = \left( \frac{1}{2u} \right)^2.
$$

**Conclusion.** The point $z(t)$ describes a perfect circle in the complex plane with radius $R = 1/(2u)$. 
Classical $\sin t$ and $\cos t$ are rational projections of the complex KMR flow:

$$
\cos t = \frac{u}{\sqrt{u^2 + t^2}}, \qquad \sin t = \frac{t}{\sqrt{u^2 + t^2}}.
$$

Trigonometry is not introduced from outside — circular rotation is born from the division operation of the complex projective Abel basis.

---

## 20.4. KMR-3D and Cascade Coupling Invariants

### 20.4.1. ODE System

Consider the 3D cascade in original coordinates:

$$
\dot x_1 = -x_1^2 x_2, \qquad
\dot x_2 = -x_2^2 x_3 + x_2^2 x_1, \qquad
\dot x_3 = x_3^2 x_2.
$$

In inverse coordinates $u_i = 1/x_i$:

$$
\dot u_1 = \frac{1}{u_2}, \qquad
\dot u_2 = \frac{1}{u_3} - \frac{1}{u_1}, \qquad
\dot u_3 = -\frac{1}{u_2}.
$$

### 20.4.2. Check of the Spherical Invariant

$$
\frac{d}{dt}(u_1^2 + u_2^2 + u_3^2) = 2 \left( \frac{u_1}{u_2} + \frac{u_2}{u_3} - \frac{u_2}{u_1} - \frac{u_3}{u_2} \right) \neq 0.
$$

The claim of a spherical invariant $u_1^2 + u_2^2 + u_3^2 = \text{const}$ is **false**.

### 20.4.3. True Coupling Invariant

Adding the first and third equations:

$$
\dot u_1 + \dot u_3 = \frac{1}{u_2} - \frac{1}{u_2} = 0 \implies u_1 + u_3 = C = \text{const}.
$$

**Conclusion.** The real 3D cascade obeys a linear conservation law. The sum of inverses of the first and third dimensions remains unchanged, coupled through the intermediate second dimension. Dimensionality in KMR acts as a hierarchical containerization of couplings, not as a Cartesian volume.

---

## 20.5. Infinite KMR Chains: Attractors and Scale Filter

### 20.5.1. Canonical Continued Fraction

For the recursion

$$
x_{n+1} = \frac{x}{1 + x x_n}
$$

the stationary point $x_\infty$ satisfies:

$$
x_\infty = \frac{x}{1 + x x_\infty} \implies x x_\infty^2 + x_\infty - x = 0.
$$

The unique positive root:

$$
x_\infty = \frac{\sqrt{1 + 4x^2} - 1}{2x}.
$$

### 20.5.2. Attractor Behavior Across Scales

| Initial $x$ | $x_\infty$ | Note |
| :--- | :--- | :--- |
| $1$ | $(\sqrt{5}-1)/2 \approx 0.618034$ | Golden ratio |
| $\pi$ | $\approx 0.853431$ | Transcendental scale |
| $x \to \infty$ | $1 - \frac{1}{2x} \to 1.0$ | Macroscopic limit |

**Conclusion.** The infinite continued fraction acts as a scale filter: microscopic initial values contract to zero, macroscopic ones asymptotically approach unity. Intermediate scales yield individual attractors computed by the quadratic formula.

### 20.5.3. Distinction from KMR-M Cascades

The simplest continued fraction **does not coincide** with multidimensional KMR-M cascades. Numerical dimensional passports at $x_i = 1$ (for $M \ge 2$ only the first step is shown):

| Model | Step 1 | Step 2 | Step 3 |
| :--- | :--- | :--- | :--- |
| 1D KMR atom | 0.5 | 0.333 | 0.25 |
| Simple continued fraction | 0.5 | 0.6 | 0.625 |
| True KMR-2D | 0.666 | — | — |
| True KMR-3D | 0.6 | — | — |

These classes must be described separately.

---

## 20.6. Hypothesis on Symmetry of Ensemble and Time Series

### 20.6.1. Formulation

In the KMR-L ontology, two limiting constructions are considered:

1. **Spatial ensemble (dimensionality):** cascade $M \to \infty$ of conjugate inverse axes $u_1, \dots, u_M$.
2. **Time series (iterations):** infinite iteration of a single operator $t \to \infty$.

### 20.6.2. Observed Symmetry

Both constructions:
- are described by the same class of rational operators;
- possess invariants of the form $\sum_i u_i = \text{const}$ (linear couplings in 3D) or $u_1 u_2 = \text{const}$ (hyperbolic in 2D);
- in the macroscopic limit yield stable attractors (e.g., approach to $1$ for large initial scales).

### 20.6.3. Status of the Statement

**This is a hypothesis, not a theorem.** To elevate it to a rigorous result, one must:

1. Define an invariant measure on the phase space of KMR-M.
2. Prove metric transitivity of the flow on the invariant manifold.
3. Numerically confirm the coincidence of temporal and spatial averages in simulations.

Until these steps are completed, the statement remains a scientifically motivated heuristic that encourages further research.

---

## 20.7. Conclusion

The KMR-Transformations framework contains:

- **a rigorous core:** 1D KMR flow $f^t(x) = x/(1+tx)$, real 2D invariant $u_1 u_2 = C$, complex circular flow and trigonometry as its projection, 3D invariant $u_1 + u_3 = C$, continued fraction attractor $x_\infty = \frac{\sqrt{1+4x^2}-1}{2x}$;
- **a hypothetical layer:** ergodic symmetry of ensemble and time series, emergence of macroscopic metric, bridges to quantum mechanics and general relativity.

This separation preserves mathematical honesty while leaving room for a constructive ontological program.

---

## 20.8. Appendix: Summary of Key Formulas

| Object | Formula |
| :--- | :--- |
| 1D KMR flow | $f^t(x) = \dfrac{x}{1+tx}$ |
| Abel function | $\alpha(x) = \dfrac{1}{x}$ |
| Group property | $(A \odot K) \odot C = A \odot (K+C)$ |
| Real 2D invariant | $u_1 u_2 = C$ |
| Complex flow components | $\mathop{\mathrm{Re}} z = \dfrac{u}{u^2+t^2}, \quad \mathop{\mathrm{Im}} z = -\dfrac{t}{u^2+t^2}$ |
| Complex radius | $R = \dfrac{1}{2u}$ |
| Trigonometric projection | $\cos t = \dfrac{u}{\sqrt{u^2+t^2}}, \ \sin t = \dfrac{t}{\sqrt{u^2+t^2}}$ |
| 3D coupling invariant | $u_1 + u_3 = C$ |
| Continued fraction attractor | $x_\infty = \dfrac{\sqrt{1+4x^2}-1}{2x}$ |
| Macroscopic limit | $\lim\limits_{x \to \infty} x_\infty = 1$ |

## 20.9. Python Reference Implementation
```python
"""
KMR Relational Basis: Reference Implementation
License: GPL 3.0 (see LICENSE)
"""

from __future__ import annotations

import math
from typing import Callable, Tuple


# ---------------------------------------------------------------------------
# 1D KMR atom and continuous flow
# ---------------------------------------------------------------------------

def kmr_step(x: float, k: float = 1.0) -> float:
    """
    One KMR step: f_k(x) = x / (1 + k*x).

    For k = 1 this is the atomic map f(x) = x / (1 + x).
    Returns NaN at the pole 1 + k*x = 0.
    """
    if x == 0.0:
        return 0.0
    denom = 1.0 + k * x
    if abs(denom) < 1e-15:
        return float("nan")
    return x / denom


def kmr_iterate(x0: float, n: int) -> float:
    """
    Integer iterate f^{\\circ n}(x0).  n >= 0.

    Equivalent to closed form x0 / (1 + n*x0) but computed
    by actual composition, so it can be used to verify the Abel formula.
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    x = x0
    for _ in range(n):
        x = kmr_step(x, 1.0)
    return x


def kmr_flow(x0: float, t: float) -> float:
    """
    Continuous Abel iterate f^t(x0) = x0 / (1 + t*x0).

    This is the closed-form solution of the Abel equation
    alpha(f(x)) = alpha(x) + 1 with alpha(x) = 1/x.
    The fixed point x0 = 0 is treated separately.
    """
    if x0 == 0.0:
        return 0.0
    denom = 1.0 + t * x0
    if abs(denom) < 1e-15:
        return float("nan")
    return x0 / denom


# ---------------------------------------------------------------------------
# Complex continuation: circular trigonometry
# ---------------------------------------------------------------------------

def complex_flow(u: float, t: float) -> complex:
    """
    z(t) = 1 / (u + i t) for real u = 1/x and real t.

    This is the complexified KMR flow with imaginary modulation K = i t.
    """
    return 1.0 / complex(u, t)


def complex_components(u: float, t: float) -> Tuple[float, float]:
    """
    Return (Re z, Im z) for z = 1 / (u + i t):

        Re z =  u / (u^2 + t^2)
        Im z = -t / (u^2 + t^2)
    """
    denom = u * u + t * t
    if denom == 0.0:
        return (float("nan"), float("nan"))
    return (u / denom, -t / denom)


def complex_invariant(u: float, t: float) -> float:
    """
    Squared radius of the circle traced by z(t):

        |z|^2 = 1 / (u^2 + t^2)
    """
    denom = u * u + t * t
    if denom == 0.0:
        return float("nan")
    return 1.0 / denom


# ---------------------------------------------------------------------------
# Cascade invariants
# ---------------------------------------------------------------------------

def invariant_2d(u1: float, u2: float) -> float:
    """Real 2D invariant u1 * u2 = const."""
    return u1 * u2


def invariant_3d(u1: float, u3: float) -> float:
    """Real 3D coupling invariant u1 + u3 = const."""
    return u1 + u3


# ---------------------------------------------------------------------------
# Infinite continued fraction attractor
# ---------------------------------------------------------------------------

def continued_fraction_attractor(x: float, tol: float = 1e-12,
                                 max_iter: int = 10_000) -> float:
    """
    Stationary point of x_{n+1} = x / (1 + x * x_n).

    Closed form: x_inf = (sqrt(1 + 4 x^2) - 1) / (2 x).
    For x = 0 the limit is 0.
    """
    if x == 0.0:
        return 0.0
    # Closed form is exact; iteration is kept as a numerical cross-check.
    closed = (math.sqrt(1.0 + 4.0 * x * x) - 1.0) / (2.0 * x)
    # Optional iterative refinement (uncomment to verify convergence):
    # xn = x
    # for _ in range(max_iter):
    #     xn_next = x / (1.0 + x * xn)
    #     if abs(xn_next - xn) < tol:
    #         return xn_next
    #     xn = xn_next
    return closed


# ---------------------------------------------------------------------------
# Convenience: check the Abel isomorphism u = 1/x
# ---------------------------------------------------------------------------

def abel_coordinate(x: float) -> float:
    """alpha(x) = 1/x."""
    if x == 0.0:
        return float("inf")
    return 1.0 / x


def abel_inverse(u: float) -> float:
    """alpha^{-1}(u) = 1/u."""
    if u == 0.0:
        return float("inf")
    return 1.0 / u
```
