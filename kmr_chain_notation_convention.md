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

# 12. Chain Notation and Left-Associativity Convention
**Author**: Sergei Terikhov  
**Date**: 16.07.2025  

## 12.1 Chain Notation for KMR Operators

### 12.1.1 Definition of KMR Chains

A **KMR chain** is a sequence of KMR operators applied successively to an initial value. For the direct operator (⊙), we define:

$A ⊙ K ⊙ C ⊙ D \coloneqq ((A ⊙ K) ⊙ C) ⊙ D$

Similarly, for the inverse operator (⊘):

$A ⊘ K ⊘ C ⊘ D \coloneqq ((A ⊘ K) ⊘ C) ⊘ D$

### 12.1.2 Left-Associativity Convention

By convention, chains of KMR operators are **left-associative**. This means:

1. **Direct operator chains**:
$A ⊙ K ⊙ C = (A ⊙ K) ⊙ C$
$A ⊙ K ⊙ C ⊙ D = ((A ⊙ K) ⊙ C) ⊙ D$

2. **Inverse operator chains**:
$A ⊘ K ⊘ C = (A ⊘ K) ⊘ C$
 $A ⊘ K ⊘ C ⊘ D = ((A ⊘ K) ⊘ C) ⊘ D$

### 12.1.3 Justification

This convention is natural because:
- It matches the recursive definition: $A_{n+1} = f(A_n)$ where $f(x) = x/(1 + x)$
- It corresponds to sequential application in time: first apply parameter $K$, then $C$, then $D$
- It maintains consistency with the group property: $(A ⊙ K) ⊙ C = A ⊙ (K + C)$

## 12.2 Mathematical Properties of Chains

### 12.2.1 Direct Operator Chains

For a chain of length $n$ with parameters $K_1, K_2, \dots, K_n$:

$A ⊙ K_1 ⊙ K_2 ⊙ \dots ⊙ K_n = \frac{A}{1 + A(K_1 + K_2 + \dots + K_n)}$

*Proof*: By repeated application of the group property:
$((\dots((A ⊙ K_1) ⊙ K_2) \dots ) ⊙ K_n) = A ⊙ (K_1 + K_2 + \dots + K_n) = \frac{A}{1 + A\sum_{i=1}^n K_i}$

### 12.2.2 Inverse Operator Chains

For the inverse operator:

$A ⊘ K_1 ⊘ K_2 ⊘ \dots ⊘ K_n = \frac{A}{1 - A(K_1 + K_2 + \dots + K_n)}$

### 12.2.3 Mixed Chains

For chains containing both ⊙ and ⊘ operators, parentheses are **required** because:

1. **Non-associativity**: $(A ⊙ K) ⊘ C \neq A ⊙ (K ⊘ C)$
2. **Non-commutativity**: The order of operations matters significantly

**Example**:
- $(A ⊙ K) ⊘ C = \frac{A/(1+AK)}{1 - C \cdot A/(1+AK)} = \frac{A}{1 + AK - AC}$
- $A ⊙ (K ⊘ C) = \frac{A}{1 + A \cdot \frac{K}{1-KC}} = \frac{A(1-KC)}{1 + AK - AKC}$

These are generally different, confirming that parentheses cannot be omitted in mixed chains.

## 12.3 Computational Interpretation

### 12.3.1 Chain Evaluation

The chain notation provides a concise way to represent sequential transformations:

```python
# Evaluating A ⊙ K ⊙ C ⊙ D (left-associative)
def evaluate_chain(A: float, *params: float) -> float:
    """Evaluate A ⊙ param1 ⊙ param2 ⊙ ... ⊙ param_n"""
    result = A
    for param in params:
        result = result / (1 + result * param)
    return result

# Example: A ⊙ K ⊙ C ⊙ D = ((A ⊙ K) ⊙ C) ⊙ D
result = evaluate_chain(A, K, C, D)
```



### 12.3.2 Chain Decomposition

Any chain can be decomposed into its cumulative parameter:

$A ⊙ K ⊙ C ⊙ D = A ⊙ (K + C + D)$

This decomposition is computationally useful as it reduces $n$ operations to a single operation.

## 12.4 Chain Algebra

### 12.4.1 Chain Concatenation

Two chains can be concatenated if their intermediate values match:
$(A ⊙ K_1 ⊙ \dots ⊙ K_m) ⊙ (C_1 ⊙ \dots ⊙ C_n) = A ⊙ K_1 ⊙ \dots ⊙ K_m ⊙ C_1 ⊙ \dots ⊙ C_n$

### 12.4.2 Chain Inversion

The inverse of a chain is obtained by reversing the order and inverting each operator:
$(A ⊙ K ⊙ C)^{-1} = (A ⊙ K ⊙ C) ⊘ (K + C) = A$
More generally:
$(A ⊙ K_1 ⊙ \dots ⊙ K_n) ⊘ (K_1 + \dots + K_n) = A$

### 12.4.3 Chain Equivalence

Two chains are equivalent if they produce the same result for all valid inputs $A$:
$A ⊙ K ⊙ C ≡ A ⊙ (K + C)$
$A ⊘ K ⊘ C ≡ A ⊘ (K + C)$

## 12.5 Examples

### Example 1: Basic Chain
Let $A = 2$, $K = 3$, $C = 4$, $D = 5$.

$2 ⊙ 3 ⊙ 4 ⊙ 5 = ((2 ⊙ 3) ⊙ 4) ⊙ 5$
Step-by-step:
$2 ⊙ 3 = \frac{2}{1 + 6} = \frac{2}{7}$
$\frac{2}{7} ⊙ 4 = \frac{2/7}{1 + (8/7)} = \frac{2}{15}$
$\frac{2}{15} ⊙ 5 = \frac{2/15}{1 + (10/15)} = \frac{2}{25}$

Using the cumulative property:
$2 ⊙ (3 + 4 + 5) = 2 ⊙ 12 = \frac{2}{1 + 24} = \frac{2}{25}$

### Example 2: Chain with Negative Parameters
$3 ⊙ (-2) ⊙ 4 = (3 ⊙ (-2)) ⊙ 4$
$3 ⊙ (-2) = \frac{3}{1 + 3 \cdot (-2)} = \frac{3}{1 - 6} = -\frac{3}{5}$
$-\frac{3}{5} ⊙ 4 = \frac{-3/5}{1 + (-3/5) \cdot 4} = \frac{-3/5}{1 - 12/5} = \frac{-3/5}{-7/5} = \frac{3}{7}$

Using cumulative property:
$3 ⊙ (-2 + 4) = 3 ⊙ 2 = \frac{3}{1 + 6} = \frac{3}{7}$

### Example 3: Mixed Chain (Requires Parentheses)
$(2 ⊙ 3) ⊘ 4 = \frac{2/7}{1 - 4 \cdot (2/7)} = \frac{2/7}{1 - 8/7} = \frac{2/7}{-1/7} = -2$
$2 ⊙ (3 ⊘ 4) = 2 ⊙ \frac{3}{1 - 12} = 2 ⊙ \frac{3}{-11} = \frac{2}{1 + 2 \cdot (-3/11)} = \frac{2}{1 - 6/11} = \frac{2}{5/11} = \frac{22}{5}$

The results are different, confirming that parentheses cannot be omitted.

## 12.6 Implementation in Code

```python
class KMRChain:
    """Represents and manipulates KMR chains."""
    
 def __init__(self, initial_value: float):
        self.value = initial_value
        self.operations = []  # List of (operator, parameter) tuples
        
    def add_operation(self, operator: str, parameter: float):
        """Add an operation to the chain."""
        if operator not in ('⊙', '⊘'):
            raise ValueError("Operator must be '⊙' or '⊘'")
        self.operations.append((operator, parameter))
        
        # Apply the operation immediately
        if operator == '⊙':
            self.value = self.value / (1 + self.value * parameter)
        else:  # '⊘'
            self.value = self.value / (1 - self.value * parameter)
    
 def evaluate(self) -> float:
        """Return the current value of the chain."""
        return self.value
    
 def cumulative_parameter(self) -> float:
        """Return the cumulative parameter for a homogeneous chain."""
        result = 0
        for op, param in self.operations:
            if op == '⊙':
                result += param
            else:  # '⊘'
                result -= param
        return result
    
 def __str__(self):
        chain_str = "A"
        for op, param in self.operations:
            chain_str += f" {op} {param}"
        return f"{chain_str} = {self.value}"
    
 @staticmethod
    def from_chain(initial: float, *operations):
        """Create a chain from a sequence of (operator, parameter) pairs."""
        chain = KMRChain(initial)
        for op, param in operations:
            chain.add_operation(op, param)
        return chain

# Example usage
chain = KMRChain.from_chain(2, ('⊙', 3), ('⊙', 4), ('⊙', 5))
print(chain)  # Output: A ⊙ 3 ⊙ 4 ⊙ 5 = 0.08
print(f"Cumulative parameter: {chain.cumulative_parameter()}")  # 12.0
```

## 12.7 Important Notes

1.  **Homogeneous chains** (all ⊙ or all ⊘) can be simplified using cumulative parameters
    
2.  **Mixed chains** require explicit parentheses and cannot be simplified in the same way
    
3.  **Chain notation** is primarily syntactic sugar for readability
    
4.  **Left-associativity** is the default and most natural interpretation for sequential processes
    

## 12.8 Applications

1.  **Concise notation**: Complex sequences of transformations can be written compactly
    
2.  **Algebraic manipulation**: Chains can be rearranged and simplified using algebraic properties
    
3.  **Code optimization**: Homogeneous chains can be computed with a single operation using cumulative parameters
    
4.  **Theoretical analysis**: Chain notation facilitates proofs and derivations involving multiple KMR operations
    

## 12.9 Conclusion

The chain notation $A ⊙ K ⊙ C ⊙ D$ with left-associativity convention provides a natural and consistent way to represent sequential KMR transformations. While it simplifies homogeneous chains through cumulative parameters, it maintains the necessity of parentheses for mixed chains due to the non-associative nature of KMR operators. This notation enhances both mathematical clarity and computational efficiency in KMR algebra.

----------

_This convention applies throughout all KMR documentation unless explicitly stated otherwise._
