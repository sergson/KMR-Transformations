# example_quick_start.py
"""
Quick start example for functional KMR chains
"""

from kmr_chains import get_default_space, add_element
from kmr_chains_operations_init import initialize_all_operations
from kmr_chains_operations_func import evaluate_function_chain

# Initialize all operations (ID and functional)
space = get_default_space()
initialize_all_operations(space)

print("=== Quick Start: Creating and evaluating KMR function chains ===")

# 1. Create simple KMR function: f(x) = x ⊙ 2
print("\n1. Creating f(x) = x ⊙ 2:")
start = add_element('identity', lambda x: x)
f_id = add_element('⊙f', 2, parent_id=start)

for x in [1, 2, 3, 5, 10]:
    result = evaluate_function_chain(f_id, space, x)
    print(f"  f({x}) = {result:.4f}")

# 2. Create chain of KMR transformations: g(x) = x ⊙ 2 ⊙ 3
print("\n2. Creating g(x) = x ⊙ 2 ⊙ 3:")
start2 = add_element('identity', lambda x: x)
g1_id = add_element('⊙f', 2, parent_id=start2)
g2_id = add_element('⊙f', 3, parent_id=g1_id)

for x in [1, 2, 3]:
    result = evaluate_function_chain(g2_id, space, x)
    print(f"  g({x}) = {result:.4f}")

# 3. Create function with mathematical expression
print("\n3. Creating h(x) = x^2 + 2x + 1:")
expr_id = add_element('identity', 'x**2 + 2*x + 1')

for x in [0, 1, 2, 3]:
    result = evaluate_function_chain(expr_id, space, x)
    print(f"  h({x}) = {result:.4f}")

# 4. Apply KMR to quadratic function
print("\n4. Creating k(x) = (x^2) ⊙ 2:")
square_id = add_element('identity', 'square')
k_id = add_element('⊙f', 2, parent_id=square_id)

for x in [1, 2, 3]:
    result = evaluate_function_chain(k_id, space, x)
    print(f"  k({x}) = {result:.4f}")

print("\n=== Quick start completed! ===")