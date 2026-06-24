<!-- 
License: CC BY-SA 4.0 (see LICENSE-CC.md)
-->

# 17. KMR Chains of Power Functions

Building on the arithmetic framework of Section 14, this section develops a purely relational construction of integer powers $K^n$ and their extension to real exponents. The approach uses the iterative multiplication method, showing that polynomial powers emerge from repeated application of a single KMR operator, without introducing any external arithmetic operations.

---

## 17.1 The KMR Extraction Operator

To recover the classical value of a parameter embedded in a KMR state, we use the cleaner configuration introduced in Section 10.2.2:

$$
\mathcal{E}_{A}(X) = \left( X \oslash A^{-1} \right)^{-1}.
$$

For the direct operator, this extraction yields the parameter itself:

$$
\mathcal{E}_{A}(A \odot K) = K.
$$

When applied to a composite expression, $\mathcal{E}_{A}$ strips away the KMR wrapping and reveals the effective parameter accumulated through the sequence of transformations. This will be the fundamental tool for interpreting KMR chains as power functions.

---

## 17.2 The Integer Square: Iterative Chain

As established in Section 14.8.5, the pure square $K^2$ for an integer $K \ge 0$ is obtained by chaining the operator $\odot K$ exactly $K$ times:

$$
\boxed{ K^2 = \Bigl( \bigl( A \odot \underbrace{K \odot K \odot \cdots \odot K}_{K \text{ times}} \bigr) \oslash A^{-1} \Bigr)^{-1} }.
$$

**Proof.** By the group property (Theorem 1), the $K$-fold left‑associative application of $\odot K$ to the base $A$ is equivalent to a single direct operator with the sum of the parameters:

$$
A \odot \underbrace{K \odot K \odot \cdots \odot K}_{K \text{ times}} = A \odot (K \cdot K) = A \odot (K^2) = \frac{A}{1 + K^2 A}.
$$

Applying the inverse tunneling $\oslash A^{-1}$ and then inverting gives exactly $K^2$. The construction uses only the operators $\odot$ and $\oslash$ with the fixed base $A$; the number of repetitions is the integer $K$ itself. ∎

**Example** ($A=1$, $K=3$):

$$
\begin{aligned}
1 \odot 3 &= \frac{1}{4},\\
\frac{1}{4} \odot 3 &= \frac{1/4}{1+3/4} = \frac{1}{7},\\
\frac{1}{7} \odot 3 &= \frac{1/7}{1+3/7} = \frac{1}{10},\\
\frac{1}{10} \oslash 1 &= \frac{1/10}{1-1/10} = \frac{1}{9},\\
\Bigl(\frac{1}{9}\Bigr)^{-1} &= 9 = 3^2.
\end{aligned}
$$

---

## 17.3 Higher Integer Powers: The Linear Cascade

The iterative mechanism extends directly to any integer power. For a positive integer $n$ and an integer $K \ge 0$, the $n$-th power $K^n$ can be obtained by applying $\odot K$ a total of $K^{n-1}$ times:

$$
\boxed{ K^n = \Bigl( \bigl( A \odot \underbrace{K \odot K \odot \cdots \odot K}_{K^{n-1} \text{ times}} \bigr) \oslash A^{-1} \Bigr)^{-1} }.
$$

**Proof.** By induction on $n$. The base case $n=1$ is trivially

$$K = \mathcal{E}_{A}(A \odot K)$$

with 1 application of $\odot K$. Assume the formula holds for $n-1$:

$$K^{n-1} = \mathcal{E}_{A}(A \odot (K^{n-1}))$$

is obtained by $K^{n-2}$ applications of $\odot K$. Then $K^n = K \cdot K^{n-1}$. Using the iterative multiplication formula (Section 14.3.1.2) with $C = K^{n-1}$ (which is an integer), we need a chain of length $C = K^{n-1}$ of the operator $\odot K$. The extraction then yields $K^n$. ∎
The length of the chain grows exponentially with the exponent $n$, but for any concrete integer $K$ and $n$ it remains a finite, purely KMR expression. No classical arithmetic is performed inside the chain—the repetition count is exactly the integer $K^{n-1}$.

**Example: cube of 2 ($K=2$, $n=3$).**  
Here $K^{n-1} = 2^{2} = 4$. The chain consists of 4 applications of $\odot 2$ starting from $A=1$:

$$
\begin{aligned}
1 \odot 2 &= \frac{1}{3}, \\
\frac{1}{3} \odot 2 &= \frac{1/3}{1+2/3} = \frac{1}{5}, \\
\frac{1}{5} \odot 2 &= \frac{1/5}{1+2/5} = \frac{1}{7}, \\
\frac{1}{7} \odot 2 &= \frac{1/7}{1+2/7} = \frac{1}{9}, \\
\frac{1}{9} \oslash 1 &= \frac{1/9}{1-1/9} = \frac{1}{8}, \\
\Bigl(\frac{1}{8}\Bigr)^{-1} &= 8 = 2^3.
\end{aligned}
$$

The result is exactly $8$, confirming the pure cubic power.

---

## 17.4 Extension to Real Exponents

The iterative chain construction of Section 17.3 provides a purely relational definition of $K^n$ for any integer exponent $n \ge 0$. For a real exponent $r \ge 0$, the KMR framework offers a natural extension via the canonical extension theorem (Section 9.2), without requiring recursive parameter re‑injection or external arithmetic operations.

Recall that the canonical extension defines the direct operator for any real argument $X$ as

$$
A \odot X = \frac{A}{1 + XA},
$$

and this definition is the unique continuous extension from integer to real parameters that preserves the group property. In particular, the expression $A \odot (K^r)$ is well defined for any real $K^r$, provided the product $K^r A$ does not hit the singularity.

Consequently, the real power $K^r$ can be represented in KMR form directly as

$$
\boxed{ K^r = \mathcal{E}_{A}\bigl( A \odot (K^r) \bigr) }.
$$

**Interpretation.** This formula states that once the real number $K^r$ is known (from classical arithmetic, or from any other context), it can be injected into the KMR framework through a single application of the direct operator and then extracted back with the cleaner $\mathcal{E}_{A}$. The expression is tautological from a computational standpoint—it does not attempt to generate $K^r$ from scratch—but it demonstrates that the KMR algebra is closed under real powers: any real power can be encoded and decoded without loss of the algebraic structure.

**Avoidance of recursive decomposition.** The earlier approach (Section 14.3.4) that decomposes a real multiplier into integer and fractional parts and then computes the fractional part via the very multiplication it intends to define, while valid as a theoretical fixed‑point characterization, is not required for the purpose of representing powers in KMR. Here we rely on the fact that the object $K^r$ already exists as a real number, and the canonical extension allows us to wrap it directly. Thus, no iterative or recursive application of KMR operators is needed to define the state $A \odot (K^r)$.

**Connection with integer powers.** For integer $r = n$, the two representations coincide: the iterative chain of length $K^{n-1}$ yields $A \odot (K^n)$, and the direct application of the canonical extension with argument $K^n$ gives exactly the same state. Hence the real‑exponent formula is a consistent generalisation.

**Spectral Isomorphic Relation.** For any real exponent $r = n + \delta$ (where $n = \lfloor r \rfloor$ is the integer power quantum and $\delta = \lbrace r \rbrace$ is the continuous flow residual), the state $A \odot K^r$ can be non‑recursively decomposed by extracting the integer isomorphic core. By the General Decomposition Theorem (14.3.2.1), the full real power state is obtained in exactly two steps without parameter re‑injection:

$$
A \odot K^{r} = \bigl( A \odot K^{n} \bigr) \odot \Delta_{\text{flow}}, \quad \text{where } \Delta_{\text{flow}} = K^{r} - K^{n}.
$$

This establishes that the continuum of real exponents is a linear modular flow shifting the system between discrete quantum states generated by the finite KMR chains.

**Practical significance.** In applications where real powers appear as parameters (e.g., scaling laws, physical models), the KMR algebra can accommodate them seamlessly. The extraction operator $\mathcal{E}_{A}$ provides a bridge between the relational KMR world and ordinary real arithmetic, allowing one to freely convert between the two representations.

Thus, the KMR framework supports real exponents without introducing any new operational rules beyond those already established in Sections 9 and 10.

---

## 17.5 Conclusion

The KMR chain construction demonstrates that integer powers are obtained by purely relational chains whose length is the integer power of $K$. Real exponents are accessible via the decomposition property and the canonical extension. No external algebraic operations enter the definition of the chains themselves—the repetition counts are the only numerical constants that appear, and they are precisely the integers $K^{n-1}$. This establishes that polynomial powers naturally emerge from the repeated action of a single KMR operator.
