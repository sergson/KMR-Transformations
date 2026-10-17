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

# 21. KMR Modulations: Cross-Chain Dynamics in 2D and 3D
**Author**: Sergei Terikhov  
**Date**: 18.10.2026

## Abstract

We explore two **cross-modulated** extensions of the KMR chain algebra of S_00020: a real 2D cross-chain and a real 3D mediated cascade. The design principle of each is stated explicitly: signs are chosen so that a **linear relation in inverse coordinates** closes the chain. In 2D the relation is multiplicative ($u_1u_2=C$), in 3D additive ($u_1+u_3=C$). We record the failed attempt at a spherical invariant in 3D and explain why it failed. **No practical application is claimed.** The paper is an algebraic exploration of what cross-modulation can and cannot do; the hypothesis on ensemble–time-series symmetry is stated and left open.

---

## 21.1. Design Principle

Two questions governed the construction of the systems below.

**Why 2D, and why these signs?** The 2D system is the **minimal symmetric cross-chain**: two variables, each serving as the parameter for the other. The signs are chosen so that the product $u_1u_2$ is conserved — the first equation uses $\odot$, the second uses $\oslash$, precisely so that $u_2\dot u_1+u_1\dot u_2=0$. This choice is **not motivated by trigonometry**: as §21.2.3 proves, real 2D modulation cannot produce circular rotation; the associated quadratic form has signature $(+,-)$, not $(+,+)$.

**Why 3D, and why these signs?** The 3D system is the **minimal mediated chain**: two end variables $u_1,u_3$ coupled through a mediator $u_2$, with no direct coupling between the ends. The original motivation was a Kolmogorov–Arnold-style hope of reducing $n$-D flows to a single 1D KMR function, which suggested a spherical invariant $u_1^2+u_2^2+u_3^2=C$. That hope failed (§21.3.3). The correct design principle, discovered after the failure, is: choose signs so that the end variables cancel — $u_1\odot\kappa$ and $u_3\oslash\kappa$ with the same $\kappa=1/u_2$ — yielding the linear invariant $u_1+u_3=C$.

**General statement.** In both cases the design principle is the same: **choose signs so that a linear relation in inverse coordinates closes the chain.** In 2D the relation is multiplicative; in 3D it is additive. Neither is spherical, and neither yields rotation without complexification (see S_00022).

---

## 21.2. Real 2D Cross-Chain

### 21.2.1. Discrete System

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

### 21.2.2. Chain Representation

The 2D system is naturally read as a **pair of chains of length 1**, in which the parameter of each chain is the current value of the other coordinate:

$$
x_1(n+1) = x_1(n) \odot x_2(n),
\qquad
x_2(n+1) = x_2(n) \oslash x_1(n).
$$

This is the **minimal mixed chain**: one direct step and one inverse step, interleaved across coordinates. The pair is **ordered**, because $\odot$ and $\oslash$ do not commute (S_00020, §4). Swapping the order of the two coordinates changes the trajectory.

**Vector form.** Let $X = (x_1, x_2)$ and define the componentwise chain map $\Phi(X) = (x_1\odot x_2,\; x_2\oslash x_1)$. The discrete dynamics is the iterate $X(n) = \Phi^{\circ n}(X(0))$, confirming the central thesis of S_00020: the basis is the iterator, and the iterator here is a cross-chain.

**Linearization.** Passing to $u_i = 1/x_i$ makes the cross-chain additive:

$$
u_1(n+1) = u_1(n) + u_2^{-1}(n), \qquad
u_2(n+1) = u_2(n) - u_1^{-1}(n).
$$

The chain is no longer written with $\odot$ and $\oslash$; it has been **linearized** by the Abel isomorphism. This is the sense in which $u$-coordinates are the natural chain coordinates.

### 21.2.3. Continuous Limit and True Invariant

In the infinitesimal limit:

$$
\frac{du_1}{dt} = \frac{1}{u_2}, \qquad
\frac{du_2}{dt} = -\frac{1}{u_1}.
$$

**Derivation of the invariant.** Multiplying the first by $u_2$, the second by $u_1$, and adding:

$$
u_2 \dot u_1 + u_1 \dot u_2 = 1 - 1 = 0
\implies \frac{d}{dt}(u_1 u_2) = 0.
$$

**Exact invariant:**

$$
u_1(t)\, u_2(t) = u_1(0)\, u_2(0) = C = \text{const}.
$$

**Explicit solution.** Substituting $u_2 = C/u_1$ into the first equation:

$$
u_1(t) = u_1(0)\, e^{t/C},
\qquad
u_2(t) = u_2(0)\, e^{-t/C}.
$$

In original coordinates $x_i = 1/u_i$: $x_1(t) = x_1(0)e^{-t/C}$, $x_2(t) = x_2(0)e^{t/C}$. One coordinate decays exponentially while the other grows; there is no oscillation, because both solutions are real exponentials.

**Geometric meaning.** In the $(u_1,u_2)$-plane the trajectory lies on the level set $u_1u_2=C$, a hyperbola. Rotating the axes by $45^\circ$ ($v_\pm = (u_1\pm u_2)/\sqrt 2$) gives $u_1u_2 = (v_+^2-v_-^2)/2$, so the invariant becomes

$$
v_+^2 - v_-^2 = 2C.
$$

The preserved quadratic form $Q(v_+,v_-)=v_+^2-v_-^2$ has signature $(+,-)$ — this is the precise sense of a **pseudo-Euclidean (Minkowski-like) metric**. The asymptotes $v_+=\pm v_-$ (i.e. $u_1u_2=0$) play the role of a light cone.

**Why not a circle.** A circle would require a preserved form of signature $(+,+)$, i.e. an invariant $u_1^2+u_2^2=\text{const}$. No real linear change of coordinates maps a $(+,-)$ form to a $(+,+)$ form. This is the algebraic content of the statement that **circular trigonometry cannot arise from purely real 2D modulation**. Circles require the complex continuation of S_00022.

---

## 21.3. Real 3D Mediated Cascade

### 21.3.1. ODE System

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

Note the signs: $\dot u_1$ is positive (direct step with $\kappa = 1/u_2$), $\dot u_3$ is negative (inverse step with the same $\kappa$). The 3D system is therefore also a **mixed chain**, though the mixing only becomes visible in $u$-coordinates.

### 21.3.2. Chain Representation

In $u$-coordinates the 3D cascade is a **homogeneous linear chain** with signed parameters. The first and third equations are chains of length 1:

$$
u_1(t) = u_1(0) \odot \kappa(t),
\qquad
u_3(t) = u_3(0) \oslash \kappa(t),
\qquad
\kappa(t) = \int_0^t \frac{ds}{u_2(s)},
$$

while the second is a chain of length 2 with alternating signs:

$$
u_2(t) = u_2(0) \odot \Bigl(\int_0^t \frac{ds}{u_3(s)}\Bigr) \oslash \Bigl(\int_0^t \frac{ds}{u_1(s)}\Bigr).
$$

### 21.3.3. Failed Spherical Invariant

$$
\frac{d}{dt}(u_1^2 + u_2^2 + u_3^2) = 2 \left( \frac{u_1}{u_2} + \frac{u_2}{u_3} - \frac{u_2}{u_1} - \frac{u_3}{u_2} \right) \neq 0.
$$

The claim of a spherical invariant $u_1^2+u_2^2+u_3^2=\text{const}$ is **false**. This failure is what motivated the reformulation of the design principle in §21.1.

### 21.3.4. True Linear Invariant

Adding the first and third equations:

$$
\dot u_1 + \dot u_3 = \frac{1}{u_2} - \frac{1}{u_2} = 0 \implies u_1 + u_3 = C = \text{const}.
$$

**Chain reading.** The 3D invariant is the **closure of a mixed chain with opposite parameters**: $u_1\odot\kappa$ and $u_3\oslash\kappa$ with the same $\kappa$. Adding them, the integrals cancel. The invariant is linear precisely because the chain is evaluated in $u$-coordinates.

---

## 21.4. What the Modulation Does and Does Not Buy

| Gain | Where it appears | Concrete form |
| :--- | :--- | :--- |
| Exact closed forms | 2D on invariant, 3D components | $u_1u_2=C$, $u_1+u_3=C$ |
| Conservation law | 3D cascade | $u_1+u_3=C$ reduces effective dimension from 3 to 2 |
| Structural role assignment | 3D cascade | $u_2$ is the mediator; $u_1,u_3$ are symmetric ends |
| Path dependence | Mixed chains | $(A\odot K)\oslash C \neq A\odot(K\oslash C)$ |

What the modulation does **not** buy:

- no universal Kolmogorov–Arnold reduction of $n$-D flows to 1D; that claim failed in 3D (§21.3.3);
- no elimination of nonlinearity — it is **relocated** from the coupling in $x$-coordinates to individual chain steps in $u$-coordinates;
- no spherical invariant in 3D;
- no classification of which $n$-D systems admit exact chain representations — that remains open.

**Honest status of applications.** No practical application is claimed in this paper. The candidates one might explore — modeling of cross-modulated systems, control respecting the linear invariant, feature decomposition by dynamic role — remain **open questions**, not results. This honesty is deliberate: the framework is algebraic, and applications require domain-specific validation not attempted here.

---

## 21.5. Hypothesis on Symmetry of Ensemble and Time Series

### 21.5.1. Formulation

Two limiting constructions are considered:

1. **Spatial ensemble (dimensionality):** cascade $M \to \infty$ of conjugate inverse axes $u_1,\dots,u_M$ — a chain in dimension index.
2. **Time series (iterations):** infinite iteration of a single operator $t \to \infty$ — a chain in time index.

### 21.5.2. Observed Symmetry

Both constructions are described by the same class of rational chain operators; both possess invariants of the form $\sum_i u_i = \text{const}$ (3D) or $u_1u_2=\text{const}$ (2D); both yield stable attractors in the macroscopic limit.

### 21.5.3. Status

**This is a hypothesis, not a theorem.** To elevate it to a rigorous result, one must (i) define an invariant measure on the phase space of KMR-M, (ii) prove metric transitivity of the flow on the invariant manifold, (iii) numerically confirm coincidence of temporal and spatial averages. Until then it remains a scientifically motivated heuristic.

---

## 21.6. Conclusion

The paper explores two cross-modulated KMR chains. What is rigorous:

- the 2D invariant $u_1u_2=C$ and the explicit exponential solution;
- the 3D linear invariant $u_1+u_3=C$;
- the algebraic explanation of why real 2D cannot produce a circle.

What is **not** claimed:

- universal reduction of $n$-D flows to 1D;
- practical applications;
- the ensemble–time-series symmetry (hypothesis only).

The design principle is explicit: **choose signs so that a linear relation in inverse coordinates closes the chain.** Multiplicative in 2D, additive in 3D. Neither is spherical. Rotation requires complexification, treated in S_00022.

---

## 21.7. Appendix: Summary

| Object | Formula |
| :--- | :--- |
| 2D cross-chain | $x_1\odot x_2,\; x_2\oslash x_1$ |
| 2D invariant | $u_1 u_2 = C$ |
| 2D explicit solution | $u_1(t)=u_1(0)e^{t/C},\; u_2(t)=u_2(0)e^{-t/C}$ |
| 3D mediated chain | $u_1\odot\kappa,\; u_3\oslash\kappa,\; \kappa=1/u_2$ |
| 3D linear invariant | $u_1 + u_3 = C$ |
| Failed spherical invariant | $u_1^2+u_2^2+u_3^2 \neq \text{const}$ |

## 21.8. Python Reference

```python
"""
KMR Modulations: Reference Implementation
License: GPL 3.0 (see LICENSE)
"""

from __future__ import annotations
from typing import Tuple


def cross_step_2d(x1: float, x2: float) -> Tuple[float, float]:
    """One 2D cross-chain step."""
    d1 = 1.0 + x1 * x2
    d2 = 1.0 - x1 * x2
    if abs(d1) < 1e-15 or abs(d2) < 1e-15:
        return (float("nan"), float("nan"))
    return (x1 / d1, x2 / d2)


def invariant_2d(u1: float, u2: float) -> float:
    """Real 2D invariant u1 * u2 = const."""
    return u1 * u2


def cascade_step_3d(x1: float, x2: float, x3: float, dt: float) -> Tuple[float, float, float]:
    """One explicit Euler step of the 3D cascade (dt small)."""
    dx1 = -x1 * x1 * x2
    dx2 = -x2 * x2 * x3 + x2 * x2 * x1
    dx3 = x3 * x3 * x2
    return (x1 + dt * dx1, x2 + dt * dx2, x3 + dt * dx3)


def invariant_3d(u1: float, u3: float) -> float:
    """Real 3D coupling invariant u1 + u3 = const."""
    return u1 + u3