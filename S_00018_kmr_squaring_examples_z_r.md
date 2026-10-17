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

# 18. Practical Examples of KMR Applications for Natural and Real Numbers
**Author**: Sergei Terikhov  
**Date**: 05.09.2026

## Abstract

This note is a companion to S_00017 (§17.1–§17.3), where the KMR squaring operator is derived and proved. Here we restate the general formula in a form that works uniformly for natural and real $K$, and verify it on two worked examples ($3^2=9$ and $3.7^2=13.69$). No new theory is introduced; the note serves as a set of exercises ("warm-ups") for readers who want to check the chain arithmetic by hand. The operator $E_A$ and the chain operations $\odot,\oslash$ are exactly those of S_00017 and S_00020.

---

## 18.1. Setup (recall from S_00017)

We use the two chain operations of the KMR basis:

$$
A \odot K = \frac{A}{1+KA},
\qquad
A \oslash K = \frac{A}{1-KA},
$$

and the extraction operator with anchor $A$:

$$
E_A(X) = \bigl(X \oslash A^{-1}\bigr)^{-1}
= \frac{1}{X} - \frac{1}{A}
= \frac{A - X}{A\,X}.
$$

In the Abel coordinate $\alpha(X) = 1/X$ this reads $E_A(X) = \alpha(X) - \alpha(A)$: the extraction returns the Abel distance from $X$ back to the anchor $A$. The case $A=1$ used throughout S_00017 and below is the special case

$$
E_1(X) = \frac{1}{X} - 1 = \frac{1-X}{X}.
$$

The identity to be exercised is the **squaring formula** of S_00017, §17.2, written here in a form that covers both integer and non-integer $K$.

**Squaring formula.** For any $K>0$ and any integer $M\ge 1$ such that $KM\in\mathbb{N}$, let

$$
dt = \frac{K}{M},
\qquad
n = K M,
$$

and iterate the direct chain $n$ times starting from $x_0 = 1$:

$$
x_n = \underbrace{1 \odot dt \odot dt \odot \cdots \odot dt}_{n\ \text{times}}.
$$

Then

$$
x_n = \frac{1}{1 + K^2},
\qquad
E_1(x_n) = K^2.
$$

**Verification of the closed form.** By the homogeneous collapse law of S_00020 (§20.4), $n$ direct steps with parameter $dt$ equal one step with parameter $n\,dt$:

$$
x_n = 1 \odot (n\,dt) = \frac{1}{1 + n\,dt}.
$$

Since $n\,dt = (KM)\cdot(K/M) = K^2$, we get $x_n = 1/(1+K^2)$. Applying $E_1$:

$$
E_1\left(\frac{1}{1+K^2}\right)
= \frac{1 - 1/(1+K^2)}{1/(1+K^2)}
= K^2.
$$

The integer case of S_00017, §17.2 corresponds to $M=1$, i.e. $dt = K$ and $n = K$ steps. The condition $KM\in\mathbb{N}$ is automatic when $K$ is rational and $M$ is a multiple of its denominator; this is why the real example below uses $K=3.7=37/10$ with $M=10$.

---

## 18.2. Example 1: $K = 3$ (integer, $M = 1$)

Take $dt = 3$ and $n = 3$ steps. The chain is

$$
x_0 = 1,
\qquad
x_1 = 1 \odot 3 = \frac{1}{4},
\qquad
x_2 = \frac{1}{4} \odot 3 = \frac{1}{7},
\qquad
x_3 = \frac{1}{7} \odot 3 = \frac{1}{10}.
$$

Extraction:

$$
E_1\left(\frac{1}{10}\right)
= \frac{1 - 1/10}{1/10}
= 9.
$$

So $3^2 = 9$, as expected.

---

## 18.3. Example 2: $K = 3.7$ (real, $M = 10$)

Take $dt = 3.7/10 = 0.37$ and $n = 37$ steps. Rather than listing all 37 iterates, we use the closed form directly and then confirm on a short prefix.

**Closed form.** $n\,dt = 37 \cdot 0.37 = 13.69$, so

$$
x_{37} = \frac{1}{1 + 13.69} = \frac{1}{14.69}.
$$

**Prefix check** (first three steps, to confirm the recursion matches the closed form):

$$
x_0 = 1,
\qquad
x_1 = 1 \odot 0.37 = \frac{1}{1.37},
\qquad
x_2 = \frac{1}{1.37} \odot 0.37 = \frac{1}{1.74},
\qquad
x_3 = \frac{1}{1.74} \odot 0.37 = \frac{1}{2.11}.
$$

Indeed $x_k = 1/(1 + 0.37\,k)$ for $k=0,1,2,3$, and at $k=37$ this gives $x_{37} = 1/(1+13.69)$, as claimed.

**Extraction.**

$$
E_1\left(\frac{1}{14.69}\right)
= \frac{1 - 1/14.69}{1/14.69}
= 14.69 - 1
= 13.69.
$$

So $3.7^2 = 13.69$, as expected.

---

## 18.4. Why the two examples differ in step count

| Case | $K$ | $M$ | $dt = K/M$ | $n = KM$ | $n\,dt$ |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Integer | $3$ | $1$ | $3$ | $3$ | $9$ |
| Real | $3.7$ | $10$ | $0.37$ | $37$ | $13.69$ |

The integer case uses one large step per unit of $K$; the real case uses ten small steps per unit. Both are instances of the same squaring formula: what matters is the product $n\,dt = K^2$, not the individual values of $n$ and $dt$. This is the homogeneous collapse law of S_00020 in action: the chain length and the step size are interchangeable, and the invariant is their product.

---

## 18.5. Remarks on the choice of $M$

The parameter $M$ is free. Larger $M$ gives a finer discretization and a longer chain, but the final result $E_1(x_n) = K^2$ is independent of $M$ — provided $n = KM$ and $dt = K/M$ are chosen consistently. Choosing $M$ poorly (for example, $M = 1$ with non-integer $K$) makes $n = KM$ non-integer and breaks the discrete iteration; the formula therefore requires $KM \in \mathbb{N}$, which is automatic when $K$ is rational and $M$ is a multiple of its denominator.

This is why the integer case is treated with $M=1$: for integer $K$, $KM = K$ is already an integer, so the coarsest chain suffices. For $K = 3.7 = 37/10$, the smallest admissible $M$ is $10$, giving $n = 37$.

---

## 18.6. Conclusion

The squaring formula of S_00017, §17.2, extends verbatim to real $K$ by choosing $dt = K/M$ and $n = KM$:

$$
E_1\left(1 \odot \underbrace{\tfrac{K}{M} \odot \cdots \odot \tfrac{K}{M}}_{KM\ \text{times}}\right) = K^2.
$$

The two worked examples ($3^2 = 9$ with $M=1$ and $3.7^2 = 13.69$ with $M=10$) confirm the formula by direct computation. No musical analogy, no numerical approximation of irrationals, no new operators: just the chain arithmetic of S_00017 and S_00020 applied to two concrete cases.

---

## 18.7. Python check

```python
"""
Companion check for S_00018.
Uses the chain operations of S_00017 / S_00020.
License: GPL 3.0 (see LICENSE)
"""

from __future__ import annotations


def chain_direct(a: float, k: float) -> float:
    return a / (1.0 + k * a)


def extract(a: float, x: float) -> float:
    """E_A(X) = (X oslash A^{-1})^{-1} = (1 - X/A) / (X/A)."""
    return (1.0 - x / a) / (x / a)


def square_via_chain(k: float, m: int = 1) -> float:
    """K^2 via n = K*M direct steps with dt = K/M, then extract with A=1."""
    dt = k / m
    n = int(round(k * m))
    x = 1.0
    for _ in range(n):
        x = chain_direct(x, dt)
    return extract(1.0, x)


if __name__ == "__main__":
    assert abs(square_via_chain(3.0, 1) - 9.0) < 1e-12
    assert abs(square_via_chain(3.7, 10) - 13.69) < 1e-10
    print("3^2   =", square_via_chain(3.0, 1))
    print("3.7^2 =", square_via_chain(3.7, 10))
```


