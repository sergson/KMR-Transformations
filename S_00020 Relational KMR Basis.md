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

# 20. Relational KMR Basis: From Abel's Equation to Chain Algebras and the Hypothesis of Ergodic Symmetry
**Author**: Sergei Terikhov  
**Date**: 18.10.2026

## Abstract

This work establishes the mathematical foundation of the relational KMR algebra (K-modulated Relational algebra) — a framework in which the basis elements of space are not point coordinates but **chains of scale operators**. We introduce two primitive chain operations ($\odot$ and $\oslash$), state the chain algebra (homogeneous chains collapse to a sum of parameters; mixed chains are non-commutative), and rigorously derive: the 1D KMR flow, its real hyperbolic 2D extension as cross-modulated chains, the complex circular continuation (genesis of trigonometry) as an imaginary-parameter chain, the 3D cascade coupling invariant as a linear chain in inverse coordinates, and the attractor of an infinite continued fraction as an iterated chain. A hypothesis is formulated about the structural symmetry between a spatial ensemble (dimensionality) and a time series (iterations). All philosophical-ontological consequences are placed outside the scope of strict statements.

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

### 20.1.2. Atomic Kernel: Two Primitive Chain Operations

We postulate a complementary pair of fractional-linear Möbius operators:

$$
f(x) = \frac{x}{1+x}, \qquad g(x) = \frac{x}{1-x}.
$$

These are the two **primitive chain operations** of the KMR basis:

$$
A \odot K = \frac{A}{1+KA} \quad\text{(direct chain step)},
\qquad
A \oslash K = \frac{A}{1-KA} \quad\text{(inverse chain step)}.
$$

For the direct kernel:

$$
\frac{1}{f(x)} = \frac{1+x}{x} = \frac{1}{x} + 1.
$$

Therefore, the Abel function has a unique exact expression:

$$
\alpha(x) = \frac{1}{x}, \qquad \alpha^{-1}(z) = \frac{1}{z}.
$$

A **KMR chain** is a finite sequence of these operations applied left to right. The notation follows the convention of S_00012: a chain is written as

$$
A \odot K_1 \odot K_2 \oslash K_3 \cdots
$$

where the leftmost symbol acts first, and parentheses are mandatory when direct and inverse steps alternate (see §20.1.4).

### 20.1.3. Continuous 1D KMR Flow as a Chain

Substitution into the canonical formula yields a closed expression:

$$
f^{t}(x) = \frac{x}{1+tx}
= x \odot \underbrace{(1 \odot 1 \odot \cdots \odot 1)}_{t\text{ steps}}
= x \odot t .
$$

In chain language, the continuous flow is a **homogeneous chain of length $t$ with unit parameters**, which collapses by the homogeneous chain law:

$$
(A \odot K_1) \odot K_2 = A \odot (K_1 + K_2).
$$

This is the algebraic content of the Abel isomorphism: a chain of $t$ unit steps equals one step with parameter $t$. The corresponding operator law:

$$
A \odot K = \frac{A}{1+KA}, \qquad (A \odot K) \odot C = A \odot (K+C).
$$

**Interpretation.** The Abel–Möbius basis is projectively linear: in the coordinate $u = 1/x$, the nonlinear chain step becomes a pure linear shift $u \mapsto u+K$. The origin is not the point $x=0$ but the entire inverse scale: $x \to 0 \iff u \to \infty$.

### 20.1.4. Chain Algebra: Homogeneous and Mixed Chains

Two structural facts govern all chains in this framework.

**Homogeneous chains collapse.** If all steps share the same sign ($\odot$ or all $\oslash$), the chain reduces to a single step whose parameter is the sum (or alternating sum) of the individual parameters:

$$
A \odot K_1 \odot K_2 \odot \cdots \odot K_n = A \odot (K_1 + K_2 + \cdots + K_n),
$$

$$
A \oslash K_1 \oslash K_2 \oslash \cdots \oslash K_n = A \oslash (K_1 + K_2 + \cdots + K_n).
$$

This is why the 1D flow, the 2D cross-chains and the 3D cascade all admit closed-form solutions: they are **homogeneous at the level of the inverse coordinate $u = 1/x$**.

**Mixed chains do not commute.** When direct and inverse steps alternate, the order of operations matters:

$$
(A \odot K) \oslash C = \frac{A}{1 + (K - C)A},
\qquad
A \odot (K \oslash C) = \frac{A\,(1 - KC)}{1 - KC + AK}.
$$

These are different rational functions for generic $K, C$. Consequently:

$$
(A \odot K) \oslash C \;\neq\; A \odot (K \oslash C).
$$

**Parentheses are not decorative.** In a mixed chain, they fix the evaluation order. The convention adopted here (and in S_00012) is **left-to-right evaluation with explicit parentheses**:

$$
A \odot K \oslash C \;\equiv\; (A \odot K) \oslash C,
$$

and any deviation from this must be written out explicitly. This non-commutativity is the algebraic fingerprint of the KMR basis: it is what distinguishes the relational geometry from ordinary commutative addition, and it is the reason why changing the basis changes the group operation itself.

### 20.1.5. Why the Basis is an Iterator: A Plain-Language Interlude

In ordinary geometry the basis is a set of fixed directions, and motion is $x(t)=x_0+t\cdot e$: a static vector stretched by a number. The KMR basis does something different. It declares the **step itself** to be the basis element. Motion is no longer addition of a fixed increment; it is **iteration of a scale-sensitive chain**:

For integer $t\ge 0$ let $f^{\circ t}$ denote the $t$-fold iterate:

$$
f^{\circ 0}(x_0)=x_0,\qquad
f^{\circ(t+1)}(x_0)=f\bigl(f^{\circ t}(x_0)\bigr),\qquad
f(x)=\frac{x}{1+x}.
$$

Then

$$
x_t=f^{\circ t}(x_0)
= x_0 \odot \underbrace{(1 \odot 1 \odot \cdots \odot 1)}_{t\text{ steps}}
= x_0 \odot t
$$

is the trajectory: $x_0=x_0,\ x_1=f(x_0),\ x_2=f(f(x_0)),\dots$.
The map $f$ itself does not depend on $t$ or $x_0$; it is the generator of the chain step.

For continuous $t$, the iterate is defined through Abel's equation $\alpha(f(x))=\alpha(x)+1$ with $\alpha(x)=1/x$. Hence

$$
f^{\circ t}(x_0)
=\alpha^{-1}\bigl(\alpha(x_0)+t\bigr)
=\frac{x_0}{1+t\,x_0},
$$

where defined. The point $x_0=0$ is the fixed point and is treated separately.

The coordinate $t$ is no longer a distance along a pre-existing line — it is the **chain length** (the accumulated parameter of the operator). This is why changing the basis changes the geometry: the group operation is no longer translation in $\mathbb{R}$, but composition of Möbius steps. Abel’s equation $\alpha(f(x))=\alpha(x)+1$ with $\alpha(x)=1/x$ is the isomorphism that linearizes this new group: in the inverse coordinate $u=1/x$, the shrinking Möbius step becomes the ordinary shift $u\mapsto u+1$. The “basis” is therefore not a collection of points but the **generator of the chain that produces the space**.

---

## 20.2. Real KMR-2D: Hyperbolic Dynamics as Cross-Modulated Chains

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

### 20.2.2. Chain Representation: Cross-Modulated Chains

The 2D system is naturally read as a **pair of chains of length 1**, in which the parameter of each chain is the current value of the other coordinate:

$$
x_1(n+1) = x_1(n) \odot x_2(n),
\qquad
x_2(n+1) = x_2(n) \oslash x_1(n).
$$

This is the **minimal mixed chain**: one direct step and one inverse step, interleaved across coordinates. In the notation of §20.1.4:

$$
\bigl(x_1(n) \odot x_2(n),\;
x_2(n) \oslash x_1(n)\bigr).
$$

The pair is **ordered**, because $\odot$ and $\oslash$ do not commute. Swapping the order of the two coordinates changes the trajectory — this is the first place in the paper where the non-commutativity of §20.1.4 has dynamical consequences.

**Vector form.** Let $X = (x_1, x_2)$ and define the componentwise chain map

$$
\Phi(X) = \bigl(x_1 \odot x_2,\; x_2 \oslash x_1\bigr).
$$

The discrete dynamics is the iterate

$$
X(n) = \Phi^{\circ n}(X(0)),
$$

where $\Phi^{\circ n}$ is the $n$-fold composition (in the sense of §20.1.5, not a pointwise power). This confirms the central thesis: **the basis is the iterator**, and the iterator here is a cross-chain.

**Linearization.** Passing to $u_i = 1/x_i$ makes the cross-chain additive:

$$
u_1(n+1) = u_1(n) + u_2^{-1}(n), \qquad
u_2(n+1) = u_2(n) - u_1^{-1}(n).
$$

The chain is no longer written with $\odot$ and $\oslash$; it has been **linearized** by the Abel isomorphism. This is the sense in which $u$-coordinates are the natural chain coordinates.

### 20.2.3. Continuous Limit and True Invariant

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

**Conclusion.** Real cross-modulation generates not a circle but a hyperbola. The trajectory obeys a pseudo-Euclidean Minkowski metric: exponential contraction/expansion, but not oscillations. Deriving circular trigonometry from purely real 2D modulation is **mathematically inconsistent**.

### 20.2.4. Infinitesimal Chains

The continuous limit admits a direct chain interpretation. Each infinitesimal time step $dt$ is a chain of length $dt$ with parameter $K_i(t)\,dt$:

$$
x_i(t+dt) = x_i(t) \odot \bigl(K_i(t)\,dt\bigr) + o(dt),
\qquad
K_1 = u_2^{-1},\quad K_2 = -u_1^{-1}.
$$

The differential equation is the **limit of the chain** as $dt \to 0$:

$$
\frac{du_i}{dt}
= \lim_{dt\to 0}\frac{u_i(t+dt)-u_i(t)}{dt}
= K_i(t).
$$

The invariant $u_1 u_2 = C$ is therefore a **chain invariant**: it is preserved along every infinitesimal step, hence along the whole chain. In this language, the statement $u_1 u_2 = C$ is exactly the statement that the chain in $u$-coordinates is **closed with respect to the product**.

---

## 20.3. Complex Continuation of KMR-1D and Genesis of Trigonometry

### 20.3.1. Imaginary Step Time as an Imaginary Chain

Let the modulation parameter become purely imaginary: $K = i t$. Then

$$
f^{t}(x) = \frac{x}{1 + i t x}
= x \odot (i t),
$$

a homogeneous chain of length $t$ with purely imaginary parameter. Denote $u = 1/x$ (real), $z = f^{t}(x)$ (complex):

$$
\frac{1}{z} = u + i t \implies z(t) = \frac{1}{u + i t} = \frac{u - i t}{u^2 + t^2}.
$$

Separating real and imaginary parts:

$$
\mathop{\mathrm{Re}} z = \frac{u}{u^2 + t^2}, \qquad
\mathop{\mathrm{Im}} z = -\frac{t}{u^2 + t^2}.
$$

**Chain reading.** An imaginary parameter rotates the chain in the complex plane: the step $K = it$ is still a Möbius map, but its trajectory is a circle rather than a hyperbola. This is the precise sense in which “trigonometry is a chain phenomenon”: the chain $\odot (it)$ is the generator of rotation.

### 20.3.2. Invariant of the Complex Flow

Squaring and adding:

$$
(\mathop{\mathrm{Re}} z)^2 + (\mathop{\mathrm{Im}} z)^2 = \frac{1}{u^2 + t^2}.
$$

Reduction to canonical form gives:

$$
\left( \mathop{\mathrm{Re}} z - \frac{1}{2u} \right)^2 + (\mathop{\mathrm{Im}} z)^2 = \left( \frac{1}{2u} \right)^2.
$$

**Conclusion.** The point $z(t)$ describes a perfect circle in the complex plane with radius $R = 1/(2u)$. Classical $\sin t$ and $\cos t$ are rational projections of the complex KMR flow:

$$
\cos t = \frac{u}{\sqrt{u^2 + t^2}}, \qquad \sin t = \frac{t}{\sqrt{u^2 + t^2}}.
$$

Trigonometry is not introduced from outside — circular rotation is born from the division operation of the complex projective Abel basis, i.e. from an **imaginary-parameter chain**.

---

## 20.4. KMR-3D and Cascade Coupling Invariants as Linear Chains

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

### 20.4.2. Chain Representation in Inverse Coordinates

In $u$-coordinates the 3D cascade is a **homogeneous linear chain** with signed parameters. The first and third equations are chains of length 1:

$$
u_1(t) = u_1(0) \odot \Bigl(\int_0^t \frac{ds}{u_2(s)}\Bigr),
\qquad
u_3(t) = u_3(0) \oslash \Bigl(\int_0^t \frac{ds}{u_2(s)}\Bigr),
$$

while the second is a chain of length 2 with alternating signs:

$$
u_2(t) = u_2(0) \odot \Bigl(\int_0^t \frac{ds}{u_3(s)}\Bigr) \oslash \Bigl(\int_0^t \frac{ds}{u_1(s)}\Bigr).
$$

**Why the invariant is linear.** Adding the first and third chain equations, the integrals cancel because the parameters are equal in magnitude and opposite in sign:

$$
u_1(t) + u_3(t) = u_1(0) + u_3(0).
$$

Thus the 3D invariant is not a circle or a sphere: it is the **closure of a mixed chain with opposite parameters**, and it is linear precisely because the chain is evaluated in $u$-coordinates.

### 20.4.3. Check of the Spherical Invariant

$$
\frac{d}{dt}(u_1^2 + u_2^2 + u_3^2) = 2 \left( \frac{u_1}{u_2} + \frac{u_2}{u_3} - \frac{u_2}{u_1} - \frac{u_3}{u_2} \right) \neq 0.
$$

The claim of a spherical invariant $u_1^2 + u_2^2 + u_3^2 = \text{const}$ is **false**.

### 20.4.4. True Coupling Invariant

Adding the first and third equations:

$$
\dot u_1 + \dot u_3 = \frac{1}{u_2} - \frac{1}{u_2} = 0 \implies u_1 + u_3 = C = \text{const}.
$$

**Conclusion.** The real 3D cascade obeys a linear conservation law. The sum of inverses of the first and third dimensions remains unchanged, coupled through the intermediate second dimension. Dimensionality in KMR acts as a hierarchical containerization of couplings, not as a Cartesian volume.

---

## 20.5. Infinite KMR Chains: Attractors and Scale Filter

### 20.5.1. Canonical Continued Fraction as an Iterated Chain

For the recursion

$$
x_{n+1} = \frac{x}{1 + x x_n}
$$

we recognize a chain of length 1 with a **fixed parameter** $x$ acting on the variable $x_n$:

$$
x_{n+1} = x \odot x_n.
$$

The stationary point $x_\infty$ satisfies the chain fixed-point equation $x \odot x_\infty = x_\infty$:

$$
x_\infty = \frac{x}{1 + x x_\infty} \implies x x_\infty^2 + x_\infty - x = 0.
$$

The unique positive root:

$$
x_\infty = \frac{\sqrt{1 + 4x^2} - 1}{2x}.
$$

**Chain reading.** The continued fraction is the **simplest non-trivial infinite chain**: a single parameter $x$ applied repeatedly to its own output. Unlike the 1D flow of §20.1.3, the chain is not homogeneous in the usual sense — the parameter is fixed while the argument varies, so the chain does not collapse to a sum. This is exactly why the attractor is non-trivial.

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

These classes must be described separately: the continued fraction is a **self-referential chain**, while KMR-M cascades are **cross-referential chains** across dimensions.

---

## 20.6. Hypothesis on Symmetry of Ensemble and Time Series

### 20.6.1. Formulation

In the KMR-L ontology, two limiting constructions are considered:

1. **Spatial ensemble (dimensionality):** cascade $M \to \infty$ of conjugate inverse axes $u_1, \dots, u_M$, i.e. a chain in dimension index.
2. **Time series (iterations):** infinite iteration of a single operator $t \to \infty$, i.e. a chain in time index.

### 20.6.2. Observed Symmetry

Both constructions:
- are described by the same class of rational chain operators;
- possess invariants of the form $\sum_i u_i = \text{const}$ (linear chains in 3D) or $u_1 u_2 = \text{const}$ (hyperbolic chains in 2D);
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

- **a rigorous core:** 1D KMR flow $f^t(x) = x/(1+tx)$ as a homogeneous chain $x \odot t$; real 2D invariant $u_1 u_2 = C$ as the closure of a cross-modulated chain; complex circular flow and trigonometry as the projection of an imaginary-parameter chain; 3D invariant $u_1 + u_3 = C$ as a linear chain with opposite parameters; continued fraction attractor $x_\infty = \frac{\sqrt{1+4x^2}-1}{2x}$ as a self-referential chain;
- **a chain-algebraic layer:** the homogeneous collapse law, the non-commutativity of mixed chains, and the Abel isomorphism as the linearization that makes chains tractable;
- **a hypothetical layer:** ergodic symmetry of ensemble and time series, emergence of macroscopic metric, bridges to quantum mechanics and general relativity.

This separation preserves mathematical honesty while leaving room for a constructive ontological program.

---

## 20.8. Appendix: Summary of Key Formulas

| Object | Formula |
| :--- | :--- |
| Direct chain step | $A \odot K = \dfrac{A}{1+KA}$ |
| Inverse chain step | $A \oslash K = \dfrac{A}{1-KA}$ |
| Homogeneous collapse | $(A \odot K) \odot C = A \odot (K+C)$ |
| Mixed non-commutativity | $(A \odot K) \oslash C \neq A \odot (K \oslash C)$ |
| 1D KMR flow | $f^t(x) = x \odot t = \dfrac{x}{1+tx}$ |
| Abel function | $\alpha(x) = \dfrac{1}{x}$ |
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
from typing import Callable, List, Tuple


# ---------------------------------------------------------------------------
# Primitive chain operations
# ---------------------------------------------------------------------------

def chain_direct(a: float, k: float) -> float:
    """Direct chain step: A odot K = A / (1 + K A)."""
    denom = 1.0 + k * a
    if abs(denom) < 1e-15:
        return float("nan")
    return a / denom


def chain_inverse(a: float, k: float) -> float:
    """Inverse chain step: A oslash K = A / (1 - K A)."""
    denom = 1.0 - k * a
    if abs(denom) < 1e-15:
        return float("nan")
    return a / denom


def chain_eval(a: float, steps: List[Tuple[float, str]]) -> float:
    """
    Evaluate a KMR chain left to right.

    steps: list of (K, op) with op in {'direct', 'inverse'}.
    Parentheses are implicit: the i-th step acts on the result of the
    (i-1)-th step. This is the canonical evaluation order of §20.1.4.
    """
    result = a
    for k, op in steps:
        if op == "direct":
            result = chain_direct(result, k)
        elif op == "inverse":
            result = chain_inverse(result, k)
        else:
            raise ValueError(f"unknown chain operation: {op!r}")
    return result


# ---------------------------------------------------------------------------
# 1D KMR atom and continuous flow
# ---------------------------------------------------------------------------

def kmr_step(x: float, k: float = 1.0) -> float:
    """One KMR step: f_k(x) = x / (1 + k*x)."""
    return chain_direct(x, k)


def kmr_iterate(x0: float, n: int) -> float:
    """Integer iterate f^{\\circ n}(x0), computed by composition."""
    if n < 0:
        raise ValueError("n must be non-negative")
    return chain_eval(x0, [(1.0, "direct")] * n)


def kmr_flow(x0: float, t: float) -> float:
    """Continuous Abel iterate f^t(x0) = x0 / (1 + t*x0)."""
    if x0 == 0.0:
        return 0.0
    denom = 1.0 + t * x0
    if abs(denom) < 1e-15:
        return float("nan")
    return x0 / denom


# ---------------------------------------------------------------------------
# Non-commutativity check for mixed chains
# ---------------------------------------------------------------------------

def mixed_order_witness(a: float, k: float, c: float) -> Tuple[float, float]:
    """
    Return the two mixed-chain evaluations that witness non-commutativity:

        (A odot K) oslash C
        A odot (K oslash C)

    For generic K, C these differ, confirming the warning of §20.1.4.
    """
    lhs = chain_eval(a, [(k, "direct"), (c, "inverse")])
    rhs = chain_eval(a, [(c, "inverse"), (k, "direct")])
    return lhs, rhs


# ---------------------------------------------------------------------------
# Complex continuation: circular trigonometry
# ---------------------------------------------------------------------------

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

def continued_fraction_attractor(x: float) -> float:
    """
    Stationary point of x_{n+1} = x / (1 + x * x_n) = x odot x_n.

    Closed form: x_inf = (sqrt(1 + 4 x^2) - 1) / (2 x).
    """
    if x == 0.0:
        return 0.0
    return (math.sqrt(1.0 + 4.0 * x * x) - 1.0) / (2.0 * x)


# ---------------------------------------------------------------------------
# Convenience: Abel coordinate
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
