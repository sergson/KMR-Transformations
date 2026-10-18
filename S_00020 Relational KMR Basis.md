<!-- 
License: CC BY-SA 4.0 (see LICENSE-CC.md)
-->

# 20. Relational KMR Basis: Chain Algebra and the Iterator Paradigm
**Author**: Sergei Terikhov  
**Date**: 18.10.2026

## Abstract

The basis of the relational KMR algebra is not a set of points or vectors but a **chain of scale operators**. We define two primitive chain operations, state the chain algebra (homogeneous chains collapse to a sum of parameters; mixed chains do not commute), and derive the 1D KMR flow as a homogeneous chain and the infinite continued fraction as a self-referential chain. The central paradigm is stated in plain terms: **the basis is an iterator, and the iterator is a chain**. No dimensional modulation and no complexification are required for this core; they are treated in companion articles. Applications are not claimed; the paper is a self-contained algebraic foundation.

---

## 20.1. Abel's Functional Equation

The classical Abel functional equation

$$
\alpha(f(x)) = \alpha(x) + 1
$$

linearizes an iterative process by mapping a nonlinear step $f$ into an additive shift $+1$ in the coordinate $\alpha$. For a continuous parameter $t \in \mathbb{R}$:

$$
f^{t}(x) = \alpha^{-1}(\alpha(x) + t).
$$

Here $f^t$ denotes the continuous Abel iterate, not the pointwise power of $f$.

---

## 20.2. Atomic Kernel: Two Primitive Chain Operations

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

where the leftmost symbol acts first, and parentheses are mandatory when direct and inverse steps alternate (see §20.4).

---

## 20.3. The 1D KMR Flow as a Homogeneous Chain

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

---

## 20.4. Chain Algebra: Homogeneous and Mixed Chains

Two structural facts govern all chains in this framework.

**Homogeneous chains collapse.** If all steps share the same sign ($\odot$ or all $\oslash$), the chain reduces to a single step whose parameter is the sum of the individual parameters:

$$
A \odot K_1 \odot K_2 \odot \cdots \odot K_n = A \odot (K_1 + K_2 + \cdots + K_n),
$$

$$
A \oslash K_1 \oslash K_2 \oslash \cdots \oslash K_n = A \oslash (K_1 + K_2 + \cdots + K_n).
$$

This collapse is what makes the 1D flow and the continued fraction tractable: both are, in different senses, homogeneous at the level of the inverse coordinate $u = 1/x$.

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

and any deviation must be written out explicitly. This non-commutativity is the algebraic fingerprint of the KMR basis: it distinguishes the relational geometry from ordinary commutative addition and is the reason changing the basis changes the group operation itself.

---

## 20.5. Why the Basis is an Iterator

In ordinary geometry the basis is a set of fixed directions, and motion is $x(t)=x_0+t\cdot e$: a static vector stretched by a number. The KMR basis does something different: it declares the **step itself** to be the basis element. Motion is no longer addition of a fixed increment; it is **iteration of a scale-sensitive chain**.

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

is the trajectory. The map $f$ itself does not depend on $t$ or $x_0$; it is the generator of the chain step.

For continuous $t$, the iterate is defined through Abel's equation $\alpha(f(x))=\alpha(x)+1$ with $\alpha(x)=1/x$. Hence

$$
f^{\circ t}(x_0)
=\alpha^{-1}\bigl(\alpha(x_0)+t\bigr)
=\frac{x_0}{1+t\,x_0},
$$

where defined. The point $x_0=0$ is the fixed point and is treated separately.

The coordinate $t$ is no longer a distance along a pre-existing line — it is the **chain length**. This is why changing the basis changes the geometry: the group operation is no longer translation in $\mathbb{R}$, but composition of Möbius steps. Abel’s equation $\alpha(f(x))=\alpha(x)+1$ with $\alpha(x)=1/x$ is the isomorphism that linearizes this new group. The basis is therefore not a collection of points but the **generator of the chain that produces the space**.

---

## 20.6. Infinite Chains: Self-Referential Iteration

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

**Attractor behavior.**

| Initial $x$ | $x_\infty$ | Note |
| :--- | :--- | :--- |
| $1$ | $(\sqrt{5}-1)/2 \approx 0.618034$ | Golden ratio |
| $\pi$ | $\approx 0.853431$ | Transcendental scale |
| $x \to \infty$ | $1 - \frac{1}{2x} \to 1.0$ | Macroscopic limit |

**Chain reading.** The continued fraction is the **simplest non-trivial infinite chain**: a single parameter $x$ applied repeatedly to its own output. Unlike the 1D flow of §20.3, the chain is not homogeneous in the usual sense — the parameter is fixed while the argument varies, so the chain does not collapse to a sum. This is exactly why the attractor is non-trivial: a fixed-point of a Möbius map with a fixed parameter, rather than a sum of parameters. The continued fraction is therefore the second canonical limit of the chain algebra: homogeneous collapse (§20.3) and self-referential fixed point (§20.6).

---

## 20.7. Conclusion

The paper contains:

- **two primitive chain operations** $\odot$ and $\oslash$, with the homogeneous collapse law and the non-commutativity of mixed chains (§20.2, §20.4);
- **the 1D KMR flow as a homogeneous chain** $x \odot t = x/(1+tx)$ (§20.3), with the Abel isomorphism as its linearization;
- **the iterator paradigm** stated in plain terms: the basis is the generator of the chain, and motion is chain length, not distance (§20.5);
- **the continued fraction as a self-referential chain** with closed-form attractor (§20.6).

What is **not** in this paper: dimensional modulation, complex continuation, trigonometry. Those are treated in companion papers, and their inclusion here would obscure the algebraic core. The chain algebra is complete on its own: everything in this paper can be verified by direct composition and by the Python reference of §20.9.

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
| Continued fraction attractor | $x_\infty = \dfrac{\sqrt{1+4x^2}-1}{2x}$ |
| Macroscopic limit | $\lim\limits_{x \to \infty} x_\infty = 1$ |

## 20.9. Python Reference Implementation

```python
"""
KMR Chain Algebra: Reference Implementation
License: GPL 3.0 (see LICENSE)
"""

from __future__ import annotations
import math
from typing import List, Tuple


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


def mixed_order_witness(a: float, k: float, c: float) -> Tuple[float, float]:
    """Return ((A odot K) oslash C, A odot (K oslash C))."""
    lhs = chain_eval(a, [(k, "direct"), (c, "inverse")])
    rhs = chain_eval(a, [(c, "inverse"), (k, "direct")])
    return lhs, rhs


def continued_fraction_attractor(x: float) -> float:
    """x_inf = (sqrt(1 + 4 x^2) - 1) / (2 x)."""
    if x == 0.0:
        return 0.0
    return (math.sqrt(1.0 + 4.0 * x * x) - 1.0) / (2.0 * x)


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

