# example_functional_operations_fixed.py
"""
Example of using functional operations in KMR chains
"""

from kmr_chains import get_default_space
from kmr_chains_operations_init import initialize_functional_operations
from kmr_chains_operations_func import evaluate_function_chain, create_kmr_function

# Initialize functional operations in the space
space = get_default_space()
initialize_functional_operations(space)

print("=== Example 1: Creating simple functional chains ===")

from kmr_chains import add_element

# Example 1: Create function f(A) = A ⊙ 2
start_id = add_element('identity', lambda x: x)
f1_id = add_element('⊙f', 2, parent_id=start_id)
print(f"Created chain for f(A) = A ⊙ 2")
print(f"Element ID: {f1_id[:16]}...")

print(f"f(1) = {evaluate_function_chain(f1_id, space, 1):.3f}")
print(f"f(2) = {evaluate_function_chain(f1_id, space, 2):.3f}")
print(f"f(5) = {evaluate_function_chain(f1_id, space, 5):.3f}")

print("\n=== Example 2: Using predefined functions ===")

square_id = add_element('identity', 'square')
print(f"Created square function")

g_id = add_element('⊙f', 3, parent_id=square_id)
print(f"Created chain for g(A) = A^2 ⊙ 3")

print(f"g(1) = {evaluate_function_chain(g_id, space, 1):.3f}")
print(f"g(2) = {evaluate_function_chain(g_id, space, 2):.3f}")
print(f"g(3) = {evaluate_function_chain(g_id, space, 3):.3f}")

print("\n=== Example 3: Chain of KMR transformations ===")

h1_id = add_element('identity', lambda x: x)
h2_id = add_element('⊙f', 2, parent_id=h1_id)
h3_id = add_element('⊙f', 3, parent_id=h2_id)
h4_id = add_element('⊙f', 4, parent_id=h3_id)
print(f"Created chain for h(A) = A ⊙ 2 ⊙ 3 ⊙ 4")

print(f"h(1) = {evaluate_function_chain(h4_id, space, 1):.3f}")
print(f"h(2) = {evaluate_function_chain(h4_id, space, 2):.3f}")

print("\n=== Example 4: Using string expressions ===")

expr_id = add_element('identity', 'x**2 + 2*x + 1')
print(f"Created chain for p(A) = A^2 + 2A + 1")

print(f"p(0) = {evaluate_function_chain(expr_id, space, 0):.3f}")
print(f"p(1) = {evaluate_function_chain(expr_id, space, 1):.3f}")
print(f"p(2) = {evaluate_function_chain(expr_id, space, 2):.3f}")

print("\n=== Example 5: Function composition ===")

square_id2 = add_element('identity', 'square')
sin_id = add_element('identity', 'sin')
comp_id = add_element('∘', sin_id, parent_id=square_id2)
print(f"Created chain for r(A) = sin(A^2)")

print(f"r(0) = {evaluate_function_chain(comp_id, space, 0):.3f}")
print(f"r(π/2) = {evaluate_function_chain(comp_id, space, 3.14159/2):.3f}")

print("\n=== Example 6: Arithmetic with functions ===")

f_square = add_element('identity', 'square')
g_linear = add_element('identity', lambda x: x)

sum_id = add_element('+f', g_linear, parent_id=f_square)
print(f"Created sum function: f(x) = x^2 + x")
print(f"sum(2) = {evaluate_function_chain(sum_id, space, 2):.3f}")

mul_id = add_element('*f', g_linear, parent_id=f_square)
print(f"Created product function: f(x) = x^2 * x = x^3")
print(f"product(2) = {evaluate_function_chain(mul_id, space, 2):.3f}")

print("\n=== Example 7: Extracting and using functions ===")

f_func = space.get_chain_value(f1_id)
print(f"Type of f_func: {type(f_func)}")
print(f"Is callable: {callable(f_func)}")

if callable(f_func):
    print(f"Direct call f_func(3): {f_func(3):.3f}")
    print(f"Direct call f_func(10): {f_func(10):.3f}")

kmr_func = create_kmr_function(2)
print(f"\nHelper kmr_func(3): {kmr_func(3):.3f}")
print(f"Helper kmr_func(10): {kmr_func(10):.3f}")

print("\n=== Example 8: Complex KMR chain (Fixed - avoiding singularity) ===")

# Fixed: Using different parameters to avoid singularity
# f(A) = (A ⊙ 2) ⊘ 1.5 (instead of 3)
chain1 = add_element('identity', lambda x: x)
chain2 = add_element('⊙f', 2, parent_id=chain1)
chain3 = add_element('⊘f', 1.5, parent_id=chain2)  # Changed from 3 to 1.5
print(f"Created chain for f(A) = (A ⊙ 2) ⊘ 1.5")

# Safe evaluation points
print(f"f(1) = {evaluate_function_chain(chain3, space, 1):.3f}")
print(f"f(2) = {evaluate_function_chain(chain3, space, 2):.3f}")
print(f"f(0.5) = {evaluate_function_chain(chain3, space, 0.5):.3f}")

print("\n=== Example 9: Mixed operations ===")

base = add_element('identity', lambda x: x)
op1 = add_element('⊙f', 2, parent_id=base)
op2 = add_element('+f', 1, parent_id=op1)
op3 = add_element('*f', 3, parent_id=op2)

print(f"Created chain for f(A) = ((A ⊙ 2) + 1) * 3")
print(f"f(1) = {evaluate_function_chain(op3, space, 1):.3f}")
print(f"f(2) = {evaluate_function_chain(op3, space, 2):.3f}")

print("\n=== Example 10: Using reciprocal function ===")

recip_id = add_element('identity', 'reciprocal')
print(f"Created reciprocal function: f(x) = 1/x")

# Avoid x=0 for reciprocal
print(f"recip(1) = {evaluate_function_chain(recip_id, space, 1):.3f}")
print(f"recip(2) = {evaluate_function_chain(recip_id, space, 2):.3f}")
print(f"recip(4) = {evaluate_function_chain(recip_id, space, 4):.3f}")

print("\n=== Example 11: Demonstrating singularities ===")

# Create a function that shows the singularity behavior
print("\nDemonstrating singularity in inverse KMR operator:")
print("For f(x) = x ⊘ K, singularity occurs when x * K = 1")

# Create simple inverse KMR function
inv_kmr = add_element('⊘f', 3, parent_id=add_element('identity', lambda x: x))

# Values approaching singularity
print("\nValues approaching singularity for f(x) = x ⊘ 3:")
print("f(0.2) =", evaluate_function_chain(inv_kmr, space, 0.2))
print("f(0.3) =", evaluate_function_chain(inv_kmr, space, 0.3))
print("f(0.33) =", evaluate_function_chain(inv_kmr, space, 0.33))
print("f(0.333) =", evaluate_function_chain(inv_kmr, space, 0.333))

# After singularity
print("f(0.35) =", evaluate_function_chain(inv_kmr, space, 0.35))
print("f(0.4) =", evaluate_function_chain(inv_kmr, space, 0.4))

print("\n=== Example 12: Safe chain with no singularities ===")

# Create a safe chain: f(x) = ((x ⊙ 0.5) + 2) ⊙ 1.5
safe1 = add_element('identity', lambda x: x)
safe2 = add_element('⊙f', 0.5, parent_id=safe1)
safe3 = add_element('+f', 2, parent_id=safe2)
safe4 = add_element('⊙f', 1.5, parent_id=safe3)

print(f"Created safe chain: f(x) = ((x ⊙ 0.5) + 2) ⊙ 1.5")
for x in [0, 1, 2, 5, 10]:
    result = evaluate_function_chain(safe4, space, x)
    print(f"f({x}) = {result:.3f}")

print("\n=== Summary ===")
print(f"Total elements in space: {len(space.public_heap)}")
print("All operations completed successfully!")