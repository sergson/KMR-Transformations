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


# 25. On Two Algebras of the Triadic Level: External Negation, Cantor's Meta-Levels, and the Primacy of Division $x/(1-x)$
**Author**: Sergei Terikhov  
**Date**: 24.10.2026

**Abstract.** A complete block is constructed: the rigorous core of the theory of external and residual negation is used to derive two algebras of the triadic level—the observer algebra and the datum algebra. It is proved that external negation $\nu$ is typed above the datum algebra, that without generating an extension the datum algebra collapses at the next meta-level, that division $A_{\mathrm{div}}(x)=x/\partial(x)$ is available in the datum algebra at level $C_3$ in the signature $\Sigma_3^+$, while successor $\sigma$ is not. The statement “$\nu$ generated shift” is formalized as the generation of an extension, not as a logical derivation of $\sigma$ from $A_{\mathrm{div}}$. The core includes: $\nu(S)\notin S$; the chain $C_{n+1}=C_n\cup\{\nu(C_n)\}$; the impossibility of residual negation for $\lvert S\rvert>2$; the non-definability of $\Phi$ in $\Sigma_0$; the definability and value of $\Phi(e)$ in $\Sigma_3^+$; the uniqueness of $\Phi$ in the Möbius class.

**Keywords:** external negation, residual negation, meta-level, Cantor's theorem, observer algebra, datum algebra, atomicity, primacy of division.

---

## 25.1. Introduction and Status

### 25.1.1. Goal

The paper combines the rigorous core of the theory of external and residual negation with the triadic scheme of levels. The core includes:

1. External negation $\nu(S)\notin S$.
2. The chain $C_0=\varnothing$, $C_{n+1}=C_n\cup\{\nu(C_n)\}$ with strict increase.
3. The impossibility of residual negation for $\lvert S\rvert>2$.
4. The non-definability of $\Phi(x)=x/(1-x)$ in the minimal signature $\Sigma_0$.
5. The definability of $\Phi$ in $\Sigma_3^+$ and the value $\Phi(e)=\varepsilon/(1_R-\varepsilon)$.
6. The uniqueness of $\Phi$ in the Möbius class with $f(0)=0$, a pole at $1$, and $f(\varepsilon)=\varepsilon/(1-\varepsilon)$.

From the core we derive:

- the necessity of a meta-level (the lemma on the impossibility of a total $\nu$ and Cantor's theorem);
- two algebras of the level—the observer algebra and the datum algebra;
- the collapse of the datum algebra without generating an extension;
- the primacy of division in the order of signatures;
- the formal meaning of the phrase “ $\nu$ generated shift. ”

### 25.1.2. Status

All theorems in §2–§5 are proved in ZFC or in the standard model $\mathcal M_R$. Points requiring additional definitions are marked explicitly. Absolute primeness of $\Phi$ is not proved; what is proved is relative atomicity and primacy in the order of signatures.

---

## 25.2. Core: External and Residual Negation

### 25.2.1. Sorts and External Negation

We consider a many-sorted language with sorts $E$ (elements) and $S$ (sets of elements). In the interpretation, $E$ has a carrier $U$, and $S$ has the domain $\mathcal P(U)$.

**Definition 2.1.** External negation is a partial operation $\nu:S\rightharpoonup E$ such that if $\nu(S)$ is defined, then $\nu(S)\notin S$.

**Definition 2.2.** Cumulative step:

$$
C_0=\varnothing,\qquad a_n=\nu(C_n),\qquad C_{n+1}=C_n\cup\{a_n\}.
$$

First steps: $0^\ast:=a_0=\nu(\varnothing)$; $e:=a_1=\nu(\{0^\ast\})$; $1:=a_2=\nu(\{0^\ast,e\})$. Hence

$$
C_1=\{0^\ast\},\qquad C_2=\{0^\ast,e\},\qquad C_3=\{0^\ast,e,1\}.
$$

**Theorem 2.3.** If $\nu(S)$ is defined, then $\nu(S)\notin S$. In particular, $\delta_\nu(S)=S\cup\{\nu(S)\}\nsubseteq S$.

**Proof.** Directly from Definition 2.1: $\nu(S)\notin S$, hence $\nu(S)\in\delta_\nu(S)\setminus S$. $\square$

**Theorem 2.4.** For all $n\ge0$:

$$
\text{(i) }a_n\notin C_n;\qquad
\text{(ii) }C_n\subsetneq C_{n+1};\qquad
\text{(iii) }C_n=\{a_0,\dots,a_{n-1}\}.
$$

**Proof.** Induction on $n$. Base $C_0=\varnothing$ is obvious. Suppose $C_n=\{a_0,\dots,a_{n-1}\}$. By Definition 2.1, $a_n=\nu(C_n)\notin C_n$, which gives (i). Then $C_n\subsetneq C_n\cup\{a_n\}=C_{n+1}$, which gives (ii). Equality (iii) follows from the construction. $\square$

### 25.2.2. Residual Negation

**Definition 2.5.** For a finite set $S$, residual negation is a map $r_S:S\to S$ satisfying

$$
S\setminus\{x\}=\{r_S(x)\}\qquad\forall x\in S.
$$

**Lemma 2.6.** For a finite $S$, residual negation $r_S$ exists if and only if $\lvert S\rvert=0$ or $\lvert S\rvert=2$. If only nonempty $S$ are considered, then $r_S$ exists if and only if $\lvert S\rvert=2$.

**Proof.** For $S=\varnothing$ the condition holds vacuously, and $r_\varnothing:\varnothing\to\varnothing$ exists. For $\lvert S\rvert=2$, the set $S\setminus\{x\}$ is a singleton, and $r_S(x)$ is determined uniquely. For $\lvert S\rvert=1$, we have $S\setminus\{x\}=\varnothing$, but $\{r_S(x)\}$ is a singleton; contradiction. For $\lvert S\rvert>2$, the set $S\setminus\{x\}$ contains more than one element, so equality with a singleton is impossible. $\square$

**Corollary 2.7.** On $C_3=\{0^\ast,e,1\}$, residual negation is not defined: $\lvert C_3\rvert=3>2$. Internal complementation at the lower layer is impossible; an external act $\nu$ is necessary.

### 25.2.3. Meta-Level: Impossibility of a Total $\nu$ and Cantor's Theorem

**Theorem 2.8 (on the meta-level for $\nu$).** Let $U$ be a set, and let $\nu:\mathcal P(U)\rightharpoonup U$ be a partial operation with $\nu(S)\notin S$ for all $S$ in its domain. Then $U$ does not belong to the domain of $\nu$.

**Proof.** If $U$ were in the domain, then $\nu(U)\in U$ and simultaneously $\nu(U)\notin U$. Contradiction. $\square$

**Corollary 2.9.** A total operation $\nu:\mathcal P(U)\to U$ with $\nu(S)\notin S$ for all $S\subseteq U$ is impossible. External negation can only be partial or typed: its domain does not contain the universe.

**Theorem 2.10 (Cantor).** For any set $S$, $\lvert S\rvert<\lvert\mathcal P(S)\rvert$. In particular, there is no universal set of all sets.

**Corollary 2.11.** The hierarchy of encompassing levels has no greatest element: for any $S$ there exists a strictly larger level. External negation always requires a meta-level.

**Remark 2.12.** Cantor's theorem gives a strictly larger power set, not a concrete element $\nu(S)$. External negation $\nu$ chooses one new element but requires an encompassing level $U\supsetneq S$. Together with Lemma 2.8 this yields: external negation cannot be closed inside $S$, and the hierarchy of meta-levels does not terminate.

---

## 25.3. Signatures and Model

### 25.3.1. Signatures

**Definition 3.1.** The minimal signature

$$
\Sigma_0=\{0^\ast,e,1,\nu\}
$$

contains constants $0^\ast,e,1$ of sort $E$ and a partial operation $\nu:S\rightharpoonup E$.

**Definition 3.2.** The field signature

$$
\Sigma_3^+=\{0^\ast,e,1,\partial,/\}
$$

contains constants $0^\ast,e,1$ of sort $E$, a unary operation $\partial:E\to E$, and a partial binary operation $/$ on $E$. Division $a/b$ is defined only for $b\neq0_R$.

The symbol $\sigma$ (successor) is not in $\Sigma_3^+$; adding it gives $\Sigma_3^\sigma=\Sigma_3^+\cup\{\sigma\}$.

### 25.3.2. The Model $\mathcal M_R$

**Definition 3.3.** Let $R$ be a field or an integral domain with fractions. The model

$$
\mathcal M_R=(R;0_R,1_R,\varepsilon,\partial^{\mathcal M},\sigma^{\mathcal M},/^{\mathcal M})
$$

is defined as follows:

$$
0^{\ast\mathcal M}=0_R,\qquad e^{\mathcal M}=\varepsilon,\qquad 1^{\mathcal M}=1_R,
$$

where $\varepsilon\neq0_R,1_R$;

$$
\partial^{\mathcal M}(x)=1_R-x;
$$

$ /^{\mathcal M}$ is ordinary division for nonzero denominator. The injection $\iota:C_3\to R$ is:

$$
\iota(0^\ast)=0_R,\qquad \iota(e)=\varepsilon,\qquad \iota(1)=1_R.
$$

### 25.3.3. Terms and Atomicity

**Definition 3.4.** A term $t(x)$ of sort $E$ **essentially depends** on $x$ if there exist $a,b\in R$ such that $t^{\mathcal M}[x\mapsto a]$ and $t^{\mathcal M}[x\mapsto b]$ are defined and unequal.

**Definition 3.5.** A unary operation $F$ on the $E$-part of the model is **$\Sigma$-definable** if there exists a term $t(x)$ of sort $E$ in signature $\Sigma$ such that $F(a)=t^{\mathcal M}[x\mapsto a]$ for all $a$ where both sides are defined, and $t$ essentially depends on $x$. The operation $F$ is **$\Sigma$-atomic** if it is not definable by any such nontrivial term in signature $\Sigma$. Atomicity is relative: it may disappear under an extension of the signature.

---

## 25.4. Atomicity of $\Phi(x)=x/(1-x)$

### 25.4.1. Non-Definability in $\Sigma_0$

**Theorem 4.1.** In $\Sigma_0=\{0^\ast,e,1,\nu\}$, where $\nu:S\rightharpoonup E$ and $0^\ast,e,1$ are constants of sort $E$, every term of sort $E$ with one free variable $x$ of sort $E$ is either $x$ or one of the constants $0^\ast,e,1$. In particular, among terms of sort $E$ in $x$ there are no terms essentially depending on $x$ except the projection $x\mapsto x$.

**Proof.** The only operation $\nu$ has arity $1$, but its argument is of sort $S$, not $E$. The constants have arity $0$. Therefore, among terms of sort $E$ in $x:E$, one cannot construct expressions of the form $\nu(x)$: the argument of $\nu$ must be of sort $S$. Hence every term of sort $E$ in $x$ is either $x$ or one of the constants. $\square$

**Corollary 4.2.** $\Phi(x)=x/(1-x)$ is not definable in $\Sigma_0$ as a nontrivial unary operation on elements in the sense of a term essentially depending on $x$. This is **relative atomicity**: it is not preserved under extension of the signature.

### 25.4.2. Definability in $\Sigma_3^+$

**Theorem 4.3.** In $\Sigma_3^+=\{0^\ast,e,1,\partial,/\}$, the expression

$$
t(x)=\frac{x}{\partial(x)}
$$

is a term of sort $E$. Under the substitution $x=e$, i.e. $x^{\mathcal M}=\iota(e)=\varepsilon$, the value of the term is defined and equals

$$
t^{\mathcal M}[x\mapsto\iota(e)]=\frac{\varepsilon}{1_R-\varepsilon}.
$$

Moreover,

$$
\partial^{\mathcal M}(\iota(e))=1_R-\varepsilon\neq0_R,
$$

since $\varepsilon\neq1_R$.

**Proof.** The term $t(x)$ uses the constants $e,1\in\Sigma_3$, the operation $\partial$, and division; hence it belongs to $\Sigma_3^+$. For $x=\varepsilon$: $\partial^{\mathcal M}(\varepsilon)=1_R-\varepsilon\neq0_R$, since $\varepsilon\neq1_R$. Therefore division is defined and gives the stated value. $\square$

### 25.4.3. Uniqueness in the Möbius Class

**Theorem 4.4.** Let $R$ be a field or an integral domain with fractions, and let

$$
f(x)=\frac{ax+b}{cx+d}
$$

with integer coefficients, where $f(0)=0$, the pole of $f$ is at $x=1$, and for $\varepsilon\neq0,1$

$$
f(\varepsilon)=\frac{\varepsilon}{1-\varepsilon}.
$$

Then

$$
f(x)=\frac{x}{1-x}.
$$

**Proof.** From $f(0)=0$ it follows that $b=0$, $d\neq0$. The pole at $1$ gives $c+d=0$, $d=-c$, $c\neq0$. Then

$$
f(x)=\frac{ax}{c(x-1)}.
$$

The condition $f(\varepsilon)=\varepsilon/(1-\varepsilon)$ gives

$$
\frac{a\varepsilon}{c(\varepsilon-1)}=\frac{\varepsilon}{1-\varepsilon}.
$$

Cancelling by $\varepsilon\neq0$:

$$
\frac{a}{c(\varepsilon-1)}=-\frac{1}{\varepsilon-1},
$$

whence $a/c=-1$. Therefore $f(x)=x/(1-x)$. $\square$

---

## 25.5. Two Algebras of the Triadic Level

### 25.5.1. Definitions

**Definition 5.1 (datum algebra).** The datum algebra of level $n$ is the structure

$$
\mathcal A_n^{G}=(C_n;\Sigma\upharpoonright C_n),
$$

where $C_n$ is the carrier of the level and $\Sigma$ is the signature of operations on elements. At $C_3$ in the signature $\Sigma_3^+$, the datum algebra contains $\partial$ and division; $\sigma$ is not in it.

**Definition 5.2 (observer algebra).** The observer algebra of level $n$ is the structure

$$
\mathcal A_n^{\mathcal O}=(\mathcal O_n;\nu_n),
$$

where $\mathcal O_n$ is the meta-level over $C_n$, and $\nu_n$ is the act of external negation sending $C_n$ to $C_{n+1}=C_n\cup\{\nu_n(C_n)\}$.

**Proposition 5.3 (typing).** $\nu_n$ is not an operation of the datum algebra $\mathcal A_n^{G}$. The argument of $\nu_n$ is of sort $S$ (set), the value is of sort $E$; the symbol $\nu_n$ is absent from $\mathcal A_n^{G}$. $\nu_n$ belongs to the observer algebra and is typed above: its domain of action is the transition $C_n\to C_{n+1}$, not operations inside $C_n$.

**Proof.** By Theorem 4.1, in $\Sigma_0$ there are no terms of sort $E$ in $x:E$ except $x$ and constants; there $\nu$ is an operation $S\rightharpoonup E$. In $\Sigma_3^+$ the symbol $\nu$ is absent altogether. Therefore $\nu_n$ is not in the signature of the datum algebra; it acts on levels. This is “typing above”: not an evaluative superiority, but a different sort. $\square$

### 25.5.2. Collapse of the Datum Algebra without Extension

**Theorem 5.4 (collapse).** Let $\mathcal A_n^{G}=(C_n;\Sigma\upharpoonright C_n)$ be the datum algebra, and suppose that at level $n$ no new element is generated: $C_{n+1}=C_n$. Then the datum algebra is not an algebra with external negation: either $\nu_n$ is not defined on $C_n$, or $\nu_n(C_n)\in C_n$, which contradicts $\nu(S)\notin S$.

**Proof.** If $C_{n+1}=C_n$, then $C_n\cup\{\nu_n(C_n)\}=C_n$, whence $\nu_n(C_n)\in C_n$. This directly contradicts Definition 2.1: $\nu_n(C_n)\notin C_n$. If $\nu_n$ is taken to be undefined on $C_n$, then the datum algebra is not closed under negation: at level $C_n$ there is no operation with the condition $\nu(S)\notin S$. In both cases the datum algebra is not an algebra with external negation. $\square$

**Corollary 5.5 (extension is forced).** The transition $C_n\to C_{n+1}=C_n\cup\{\nu(C_n)\}$ is not an additional construction; it is necessary for the existence of $\nu$ as an operation with the condition $\nu(S)\notin S$. Without generating an extension, the datum algebra collapses at level $n$.

### 25.5.3. Formal Meaning of “$\nu$ Generated Shift”

**Definition 5.6 (generation of extension).** The act $\nu_n$ **generates an extension** $\mathcal A_n^{G}\to\mathcal A_{n+1}^{G}$ if $C_{n+1}=C_n\cup\{\nu_n(C_n)\}$ and $\nu_n(C_n)\notin C_n$. Without this, $\mathcal A_n^{G}$ collapses by Theorem 5.4.

**Definition 5.7 (identification).** At level $C_{n+1}$, the element $\nu_n(C_n)$ is **identified** with a name if $\iota(\nu_n(C_n))\in R$ is fixed. For $n=1,2$: $\iota(\nu(C_1))=\iota(e)=\varepsilon$, $\iota(\nu(C_2))=\iota(1)=1_R$.

**Definition 5.8 (generation of shift).** We say that $\nu$ **generated shift** $\sigma$ if:
1. $\nu$ generates the extension $C_n\to C_{n+1}$;
2. at $C_{n+1}$ the identification $\nu(C_n)\mapsto n$ is fixed;
3. $\sigma$ is added to the signature $\Sigma_3^\sigma$ and $\sigma(n)$ becomes a term.

This is a **definition**, not a theorem. It fixes the meaning of the phrase “generation of shift” as the generation of an extension, not as a logical derivation of $\sigma$ from $A_{\mathrm{div}}$.

**Remark 5.9.** In the drafts, the phrase “distinct $\mathrm{NOT}$ generated shift at the meta-level” was understood precisely in this way: the act $\nu$ created a new level, at the level an identification became possible, and after the identification and addition of $\sigma$ to the signature, $\sigma(n)$ became available. Not as a derivation of $\sigma$ from $A_{\mathrm{div}}$.

### 25.5.4. Availability of a Term at a Level

**Definition 5.10 (availability).** A term $t(x)$ in signature $\Sigma$ is **available at level $C_n$** if:
1. all constants of $t$ lie in $C_n$;
2. all operations of $t$ belong to $\Sigma$;
3. there exists a substitution $x\in C_n$ for which $t^{\mathcal M}[x]$ is defined.

**Theorem 5.11 (primacy of division in the order of signatures).** In $\mathcal A_3^{G}$ with signature $\Sigma_3^+$:

1. The term $A_{\mathrm{div}}(x)=x/\partial(x)$ is available at $C_3$: for $x=e$ its value $\varepsilon/(1_R-\varepsilon)$ is defined (Theorem 4.3).
2. The term $\sigma(1)$ is not a term of $\Sigma_3^+$: $\sigma\notin\Sigma_3^+$.
3. The triadic step $C_{n+1}=C_n\cup\{\nu(C_n)\}$ does not use $\sigma$.
4. Therefore, in the order of signatures, division precedes shift inside the datum algebra of level $C_3$.

**Proof.** Point 1 is Theorem 4.3. Point 2 holds by definition of $\Sigma_3^+$; $\sigma$ is not in it. Point 3 holds by Definition 2.2: the step uses only $\nu$. Point 4 follows from 1–3. $\square$

**Theorem 5.12 (availability of shift at the next level).** In $\mathcal A_4^{G}$, after the identification $\nu(C_3)\mapsto4$ (or another fixed identification) and the addition of $\sigma$ to $\Sigma_3^\sigma$, the expression $\sigma(n)$ becomes a term. Its value $\sigma^{\mathcal M}(n)$ generally does not lie in $C_4$.

**Proof.** By Definition 5.10: after adding $\sigma$ to $\Sigma_3^\sigma$, under the substitution $x=1$ (which lies in $C_3\subsetneq C_4$), the expression $\sigma(1)$ has all constants in $C_3$, all operations in $\Sigma_3^\sigma$, and a substitution from $C_3\subseteq C_4$. The value $\sigma^{\mathcal M}(1_R)$—by definition of $\sigma^{\mathcal M}$—generally does not lie in $\iota(C_4)$. $\square$

**Remark 5.13.** In Theorem 5.12, the value $\sigma^{\mathcal M}(1_R)$ may not lie in $C_4$ in $\mathcal M_R$: $C_4$ is finite, while $\sigma^{\mathcal M}$ may go beyond $\iota(C_4)$. This does not prevent the term from being available: availability by Definition 5.10 does not require the value to lie in the carrier.

---

## 25.6. Summary Theorem

**Theorem 6.1 (complete block).** In the model $\mathcal M_R$ with $C_3=\{0^\ast,e,1\}$, $\partial(x)=1_R-x$, and $A_{\mathrm{div}}(x)=x/\partial(x)=x/(1_R-x)$:

1. **External negation.** $\nu(S)\notin S$; $C_{n+1}=C_n\cup\{\nu(C_n)\}$ with strict increase $C_n\subsetneq C_{n+1}$.
2. **Impossibility of residual negation.** $r_S$ exists only for $\lvert S\rvert=0$ or $\lvert S\rvert=2$. On $C_3$ ($\lvert C_3\rvert=3$), $r_{C_3}$ is not defined.
3. **Meta-level.** A total $\nu$ on a universal carrier is impossible (Theorem 2.8). The hierarchy of meta-levels does not terminate (Cantor, Theorem 2.10).
4. **Atomicity of division.** $A_{\mathrm{div}}$ is not definable in $\Sigma_0$ (Theorem 4.1); it is definable in $\Sigma_3^+$ (Theorem 4.3); it is unique in the Möbius class with $f(0)=0$, a pole at $1$, and $f(\varepsilon)=\varepsilon/(1-\varepsilon)$ (Theorem 4.4).
5. **Two algebras.** The datum algebra $\mathcal A_n^{G}=(C_n;\Sigma\upharpoonright C_n)$; the observer algebra $\mathcal A_n^{\mathcal O}=(\mathcal O_n;\nu_n)$. $\nu_n$ is not an operation of $\mathcal A_n^{G}$ (Proposition 5.3).
6. **Collapse without extension.** Without $C_{n+1}\supsetneq C_n$, the datum algebra is not an algebra with external negation (Theorem 5.4).
7. **Primacy of division.** $A_{\mathrm{div}}$ is available in $\mathcal A_3^{G}$ with $\Sigma_3^+$; $\sigma$ is not (Theorem 5.11).
8. **Generation of shift.** “ $\nu$ generated shift ” means (5.6)→(5.7)→(5.12): generation of extension, identification, addition of $\sigma$ to the signature. Not a logical derivation.

Points 1–7 are proved. Point 8 is a definition.

---

## 25.7. Status by Section

| Section | Statement | Status |
|---|---|---|
| External negation | $\nu(S)\notin S$; $C_{n+1}=C_n\cup\{\nu(C_n)\}$ | Proved (§2) |
| Residual negation | $r_S$ for $\lvert S\rvert=0,2$ | Proved (§2) |
| Meta-level | $\nu$ not total on $U$ | Proved (§2) |
| Hierarchy | does not terminate | Proved (Cantor, §2) |
| Non-definability of $\Phi$ | in $\Sigma_0$ | Proved (§4) |
| Definability of $\Phi$ | in $\Sigma_3^+$ | Proved (§4) |
| Uniqueness of $\Phi$ | in the Möbius class | Proved (§4) |
| Two algebras | $\nu$ typed above | Proved (§5) |
| Collapse | without extension | Proved (§5) |
| Primacy of division | in the order of signatures | Proved (§5) |
| “ $\nu$ generated shift ” | as generation of extension | Definition (§5) |
| Absolute primeness of $\Phi$ | — | Not proved |
| “ $e/e$ is not primitive” | — | Not proved; requires linear terms |

---

## 25.8. Conclusion

The rigorous core of the theory of external and residual negation yields:

- $\nu(S)\notin S$; the chain $C_n$; the impossibility of $r_S$ for $\lvert S\rvert>2$;
- the meta-level lemma and Cantor's theorem as a guarantee of a non-terminating hierarchy;
- $\Sigma_0$-atomicity of $\Phi$, $\Sigma_3^+$-definability, uniqueness in the Möbius class.

From the core we derive:

- **two algebras of the triadic level**—the observer algebra $\mathcal A_n^{\mathcal O}$ and the datum algebra $\mathcal A_n^{G}$;
- **typing of the observer above:** $\nu$ acts on levels, not on elements;
- **collapse without extension:** without $C_{n+1}\supsetneq C_n$, the datum algebra is not an algebra with external negation;
- **primacy of division in the order of signatures:** $A_{\mathrm{div}}$ is available in $\mathcal A_3^{G}$ with $\Sigma_3^+$, $\sigma$ is not;
- **formal meaning of “generation of shift”:** generation of extension $\to$ identification $\to$ addition of $\sigma$ to the signature. Not a logical derivation.

The main limitation: this proves the primacy of division in the order of availability, not the absolute primeness of $\Phi$ and not the logical derivation of $\sigma$ from $A_{\mathrm{div}}$. Absolute primeness requires a separate order of term complexity; the question of $e/e$ requires linear or resource-sensitive terms. Both questions lie beyond the scope of this paper and remain open.

$$
\boxed{
\begin{aligned}
&\text{Core: }\nu(S)\notin S;\ C_{n+1}=C_n\cup\{\nu(C_n)\};\ r_S\text{ for }\lvert S\rvert=0,2;\ \Phi\ \Sigma_0\text{-atomic.}\\
&\text{Meta-level: total }\nu\text{ impossible; hierarchy does not terminate (Cantor).}\\
&\text{Two algebras: }\mathcal A_n^{\mathcal O}=(\mathcal O_n;\nu_n),\ \mathcal A_n^{G}=(C_n;\Sigma\upharpoonright C_n);\ \nu_n\text{ typed above.}\\
&\text{Collapse: without }C_{n+1}\supsetneq C_n\text{ the datum algebra has no external negation.}\\
&\text{Primacy: }A_{\mathrm{div}}\text{ available in }\mathcal A_3^{G}\text{ with }\Sigma_3^+;\ \sigma\text{ is not.}\\
&\text{Generation of shift: extension }\to\text{ identification }\to\ \sigma\text{ in the signature.}
\end{aligned}}
$$
