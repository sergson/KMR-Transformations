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

# 26 Atomic Algebra
**Author**: Sergei Terikhov  
**Date**: 24.10.2026

**Abstract.** The rigorous core (Primacy of Division (Section 25)) of the theory of external negation is extended in two directions. First, a polymorphic atom $A_u(x)=x/(u-x)$ is introduced with a parameter $u$—a "distinguishable norm." It is shown that $x/(1-x)$ is the normalized special case at $u=1_R$, and that the atomicity of $A_u$ in $\Sigma_0$ persists for any $u$. Second, the principle of distinguishability is formalized: each level exists precisely because a threshold $\delta_n$ distinguishes $x$ and $\mathrm{NOT}(x)$; otherwise the level collapses. Shift is realized not by expanding the terms of a level algebra but by expanding the algebras themselves. The top layer is by construction one term larger: this term is the governing unit $\Delta(x)=\mathrm{NOT}(x/\mathrm{NOT}(x))$, which controls the entire hierarchy. A connection to the curvature atom $S_{00024}$ is established through the parametrization $u(k)=1-\cos_k(2\alpha)$.

---

## 26.1. Polymorphic Atom and the Normalized Case

### 26.1.1. Parametrized Signature

**Definition 1.1.** Let $R$ be a field or an integral domain with fractions. For $u\in R\setminus\{0_R\}$, define the signature

$$
\Sigma_3^+(u)=\{0^\ast,e,u,\partial_u,/\},
$$

where $\partial_u(x)=u-x$. The model $\mathcal M_R(u)$ is obtained from $\mathcal M_R$ by replacing $\partial$ with $\partial_u$ and $1_R$ with $u$.

**Definition 1.2.** The polymorphic atom:

$$
A_u(x)=\frac{x}{\partial_u(x)}=\frac{x}{u-x}.
$$

For $u=1_R$, we obtain $A_1(x)=x/(1_R-x)$.

### 26.1.2. Atomicity for Any $u$

**Theorem 1.3.** For any $u\in R\setminus\{0_R\}$, the atom $A_u$ is not definable in $\Sigma_0=\{0^\ast,e,1,\nu\}$.

**Proof.** In $\Sigma_0$ there is neither $\partial_u$ nor division. By Theorem 4.1 of the core (Primacy of Division (Section 25)), in $\Sigma_0$ there are no terms of sort $E$ in $x$ that essentially depend on $x$ except $x$. Therefore $A_u$ is not definable in $\Sigma_0$. $\square$

**Corollary 1.4.** The relative atomicity of $A_1$ in $\Sigma_0$ is a special case of the atomicity of $A_u$. It does not depend on the specific value of the unit.

**Theorem 1.5.** In the class of Möbius transformations $f(x)=(ax+b)/(cx+d)$ with $f(0)=0$, a pole at $u$, and $f(\varepsilon)=\varepsilon/(u-\varepsilon)$, the unique function is $f(x)=x/(u-x)$.

**Proof.** Analogous to Theorem 4.4 of the core (Primacy of Division (Section 25)) with $1$ replaced by $u$: from $f(0)=0$ it follows that $b=0$; the pole at $u$ gives $d=-cu$; the condition $f(\varepsilon)=\varepsilon/(u-\varepsilon)$ gives $a/c=-1$. $\square$

---

## 26.2. Distinguishability Threshold and the Existence of a Level

### 26.2.1. Distinguishability as a Condition for a Level

**Definition 2.1.** The distinguishability threshold of level $n$ is an element $\delta_n\in C_{n+1}\setminus C_n$ that makes $x$ and $\mathrm{NOT}(x)$ distinguishable for all $x\in C_n$.

**Principle of Distinguishability.** A level $C_n$ exists if and only if there exists a threshold $\delta_n$ distinguishing $x$ and $\mathrm{NOT}(x)$ for all $x\in C_n$. In the polymorphic algebra, the threshold is given by the condition $x\neq u/2$: for $x=u/2$, we have $x=\mathrm{NOT}(x)$, and distinction is impossible.

**Theorem 2.2 (collapse without distinguishability).** If the threshold $\delta_n$ does not exist, then the level $C_n$ collapses: either $\nu_n$ is not defined on $C_n$, or $\nu_n(C_n)\in C_n$, which contradicts $\nu(S)\notin S$.

**Proof.** If $\delta_n$ does not exist, then $\nu_n(C_n)$ cannot be an external element. If $\nu_n(C_n)\in C_n$, then $\nu(S)\notin S$ is violated. If $\nu_n$ is undefined, then the level is not closed under negation. $\square$

### 26.2.2. Splitting at the Hint of Shift

**Theorem 2.3 (splitting).** If at level $n$ an element $x$ approaches the threshold $\delta_n$ (i.e., $x\to u/2$), then the algebra $\mathcal A_n^G$ is forced to extend to $\mathcal A_{n+1}^G=(C_{n+1};\Sigma\upharpoonright C_{n+1})$, where $C_{n+1}=C_n\cup\{\delta_n\}$.

**Proof.** As $x\to u/2$, the distinction between $x$ and $\mathrm{NOT}(x)$ vanishes. By Theorem 2.2, without extension the level collapses. Hence the extension is forced. $\square$

**Corollary 2.4.** A hint of shift (crossing the distinguishability threshold) immediately generates a power-set algebra: $C_{n+1}$ contains $\delta_n$ as a new element, and $\mathcal P(C_n)$ becomes available as an encompassing level.

---

## 26.3. Shift as Expansion of Algebras, Not Terms

### 3.1. Prohibition of the Shift Term at a Level

**Theorem 3.1.** The term $\sigma(x)=x+1_R$ is not in $\Sigma_3^+(u)$. Any expression with $\sigma$ requires extending the signature to $\Sigma_3^\sigma(u)=\Sigma_3^+(u)\cup\{\sigma\}$.

**Proof.** By definition of $\Sigma_3^+(u)$; $\sigma$ is not in it. $\square$

**Corollary 3.2.** An attempt to introduce $\sigma$ at level $n$ causes collapse: $\sigma$ is not a term of $\Sigma_3^+(u)$, and its introduction requires an extension of the signature, i.e., a transition to a new level.

### 26.3.2. Forced Dynamics

**Theorem 3.3.** The algebra $\mathcal A_n^G$ is forced to:
1. **expand downward (splitting):** $C_n\to C_{n+1}$ upon a hint of shift;
2. **collapse upward (narrowing):** restriction to the threshold $\delta_n$, which becomes a term of the upper level.

**Proof.** Point 1 is Theorem 2.3. Point 2 follows from Corollary 2.2: without narrowing to the threshold, the level loses distinguishability. $\square$

**Corollary 3.4 (principle).** Shift is realized not by expanding the number of terms of a level algebra but by expanding the algebras themselves. The shift term is prohibited at a level; its introduction is possible only through a transition to a new level.

---

## 26.4. Governing Term of the Top Level

### 26.4.1. The Top Layer Is One Term Larger

**Theorem 4.1.** The top layer $C_{\mathrm{top}}$ contains one more term than the layer below: this term is the distinguishability threshold $\delta_{\mathrm{top}}$, which controls the entire hierarchy.

**Proof.** By construction $C_{n+1}=C_n\cup\{\delta_n\}$, where $\delta_n$ is the threshold. At the top level the threshold becomes an explicit term. $\square$

### 26.4.2. The Governing Unit

**Definition 4.2.** The governing term of the top level:

$$
\Delta(x)=\mathrm{NOT}\!\left(\frac{x}{\mathrm{NOT}(x)}\right)=\mathrm{NOT}\!\left(\frac{x}{\partial_u(x)}\right)=\mathrm{NOT}\!\left(\frac{x}{u-x}\right)=u-\frac{x}{u-x}.
$$

This term is the "distinction of distinction"—a threshold that controls all thresholds.

**Theorem 4.3 (properties of the governing term).**
1. $\Delta(x)$ is not definable in $\Sigma_3^+(u)$: external negation $\mathrm{NOT}$ acts on sets, not on elements.
2. $\Delta(x)$ is definable in the extension $\Sigma_3^+(u)\cup\{\nu\}$.
3. $\Delta(x)$ controls the threshold: for $x=u/2$, we have $\Delta(u/2)=u-1$; in the normalized case $u=1_R$, this gives $\Delta(1_R/2)=0_R$.

**Proof.** Point 1 follows from the typing of $\nu$ (sort $S\to E$). Point 2 follows by adding $\nu$ to the signature. Point 3 is by direct substitution. $\square$

**Remark 4.4.** The term $\Delta(x)=\mathrm{NOT}(x/\mathrm{NOT}(x))$ is not a "shift" in the sense of $\sigma(x)=x+1$, but a "control unit"—a distinguishability threshold that makes the existence of all levels possible. The top layer is one term larger precisely because it contains $\Delta$ as an explicit term.

---

## 26.5. Connection to Curvature and the Fuzzy Unit

### 26.5.1. Parametrization of the Unit

**Definition 5.1.** Parametrization of the unit:

$$
u(k)=1-\cos_k(2\alpha),
$$

where $k$ is the curvature parameter (see $S_{00024}$). For $k=1$ (sphere) and $\alpha=\pi/4$, we obtain $u(1)=1_R$.

**Theorem 5.2.** The atom $A_{u(k)}(x)=x/(u(k)-x)$ is a curvature generalization of $A_1$. For $k=1$, $\alpha=\pi/4$, we obtain $A_1(x)=x/(1_R-x)$.

**Proof.** Direct substitution $u(1)=1_R$. $\square$

**Corollary 5.3.** The "fuzzy unit" $u(k)$ is a parameter that descends from the meta-level. The normalized atom $A_1$ is a special case for $k=1$. In the non-normalized algebra, $u$ is not fixed; it is assigned by the observer at the meta-level and passed to the datum algebra as a constant.

### 26.5.2. Non-Normalized Algebra as the Base

**Theorem 5.4.** The algebra $\mathcal A_n^G(u)=(C_n;\Sigma_3^+(u)\upharpoonright C_n)$ is a "shift-free algebra of the non-normalized unit": $\sigma$ is not in it, $u$ is a parameter. The normalized algebra $\mathcal A_n^G(1_R)$ is a special case.

**Proof.** By definition of $\Sigma_3^+(u)$; $\sigma$ is not in it. $u$ is a parameter of the signature. $\square$

**Corollary 5.5.** $x/\mathrm{NOT}(x)$ is a polymorphic scheme with parameter $u$. $x/(1-x)$ is its normalized special case. Development toward the fuzzy unit $u(k)$ yields the curvature atom $S_{00024}$.

---

## 26.6. Conclusion

1. $x/\mathrm{NOT}(x)$ is a polymorphic scheme with parameter $u$ (the distinguishable norm).
2. $x/(1-x)$ is the normalized special case at $u=1_R$.
3. The distinguishability threshold $\delta_n$ is the condition for the existence of a level; without it the level collapses.
4. Shift is realized by expanding algebras, not terms; the shift term is prohibited at a level.
5. The top layer is one term larger: $\Delta(x)=\mathrm{NOT}(x/\mathrm{NOT}(x))$ is the governing term, the control unit of the entire hierarchy.
6. Curvature $k$ parametrizes the unit $u(k)=1-\cos_k(2\alpha)$, linking to $S_{00024}$.

$$
\boxed{
\begin{aligned}
&\text{Base: }A_u(x)=x/(u-x);\quad A_1(x)=x/(1-x)\text{ is the normalized case.}\\
&\text{Threshold: }\delta_n\text{ distinguishes }x\text{ and }\mathrm{NOT}(x);\text{ without it the level collapses.}\\
&\text{Shift: prohibited as a term of a level; realized by expanding algebras.}\\
&\text{Top: }\Delta(x)=\mathrm{NOT}(x/\mathrm{NOT}(x))\text{ is the governing unit; the top layer is one term larger.}\\
&\text{Curvature: }u(k)=1-\cos_k(2\alpha);\quad A_{u(k)}\text{ generalizes }A_1.
\end{aligned}}
$$
```
