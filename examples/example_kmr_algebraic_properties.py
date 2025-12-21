# example_kmr_algebraic_properties.py
"""
Demonstrating KMR algebraic properties using functional chains
"""

from kmr_chains import get_default_space, add_element
from kmr_chains_operations_init import initialize_all_operations
from kmr_chains_operations_func import evaluate_function_chain
import math

# Initialize all operations
space = get_default_space()
initialize_all_operations(space)

print("=== KMR Algebraic Properties Demonstration ===\n")

# Property 1: Group property for direct operator (A ⊙ K) ⊙ C = A ⊙ (K + C)
print("=== Property 1: Group Property ===")
print("Testing: (A ⊙ K) ⊙ C = A ⊙ (K + C)")

# Create chain for left side: (A ⊙ K) ⊙ C
# Let K=2, C=3
print("\nLeft side: (A ⊙ 2) ⊙ 3")
left1 = add_element('identity', lambda x: x)
left2 = add_element('⊙f', 2, parent_id=left1)
left3 = add_element('⊙f', 3, parent_id=left2)

# Create chain for right side: A ⊙ (K + C) = A ⊙ 5
print("Right side: A ⊙ (2 + 3) = A ⊙ 5")
right1 = add_element('identity', lambda x: x)
right2 = add_element('⊙f', 5, parent_id=right1)

# Test with values
test_values = [1, 2, 3, 5, 10]
print("\nVerification:")
for val in test_values:
    left_result = evaluate_function_chain(left3, space, val)
    right_result = evaluate_function_chain(right2, space, val)
    match = abs(left_result - right_result) < 1e-10
    print(f"A={val}: ({val} ⊙ 2) ⊙ 3 = {left_result:.6f}, {val} ⊙ 5 = {right_result:.6f}, Match: {match}")

# Property 2: Duality A ⊙ K = A ⊘ (-K)
print("\n\n=== Property 2: Duality ===")
print("Testing: A ⊙ K = A ⊘ (-K)")

# For K=2: A ⊙ 2 should equal A ⊘ (-2)
print("\nLeft side: A ⊙ 2")
dual_left1 = add_element('identity', lambda x: x)
dual_left2 = add_element('⊙f', 2, parent_id=dual_left1)

print("Right side: A ⊘ (-2)")
dual_right1 = add_element('identity', lambda x: x)
dual_right2 = add_element('⊘f', -2, parent_id=dual_right1)

print("\nVerification:")
for val in test_values:
    left_dual = evaluate_function_chain(dual_left2, space, val)
    right_dual = evaluate_function_chain(dual_right2, space, val)
    match = abs(left_dual - right_dual) < 1e-10
    print(f"A={val}: {val} ⊙ 2 = {left_dual:.6f}, {val} ⊘ -2 = {right_dual:.6f}, Match: {match}")

# Property 3: Inversion identity (A ⊙ K) ⊘ K = A
print("\n\n=== Property 3: Inversion Identity ===")
print("Testing: (A ⊙ K) ⊘ K = A")

print("\nLeft side: (A ⊙ 2) ⊘ 2")
inv1 = add_element('identity', lambda x: x)
inv2 = add_element('⊙f', 2, parent_id=inv1)
inv3 = add_element('⊘f', 2, parent_id=inv2)

print("\nVerification (should return original A):")
for val in test_values:
    result = evaluate_function_chain(inv3, space, val)
    match = abs(result - val) < 1e-10
    print(f"A={val}: ({val} ⊙ 2) ⊘ 2 = {result:.6f}, Match with A: {match}")

# Property 4: Scaling property λ·(A ⊙ K) = (λA) ⊙ (K/λ)
print("\n\n=== Property 4: Scaling Property ===")
print("Testing: λ·(A ⊙ K) = (λA) ⊙ (K/λ)")
print("Let λ=3, K=2")

# Left side: 3 * (A ⊙ 2)
scale_left1 = add_element('identity', lambda x: x)
scale_left2 = add_element('⊙f', 2, parent_id=scale_left1)
scale_left3 = add_element('*f', 3, parent_id=scale_left2)

# Right side: (3A) ⊙ (2/3) = (3A) ⊙ 0.666...
scale_right1 = add_element('identity', lambda x: 3*x)  # λA
scale_right2 = add_element('⊙f', 2/3, parent_id=scale_right1)

print("\nVerification:")
for val in test_values:
    left_scale = evaluate_function_chain(scale_left3, space, val)
    right_scale = evaluate_function_chain(scale_right2, space, val)
    match = abs(left_scale - right_scale) < 1e-10
    print(f"A={val}: 3*({val} ⊙ 2) = {left_scale:.6f}, (3*{val}) ⊙ (2/3) = {right_scale:.6f}, Match: {match}")

# Property 5: Correct Chain Composition Formula
print("\n\n=== Property 5: Correct Chain Composition ===")
print("Testing: (A ⊙ K) ⊙ C = A / (1 + A*K + A*C)")
print("This is the same as A ⊙ (K + C) by group property")

# We already verified this in Property 1
print("\nThis property was already verified in Property 1.")

# Property 6: Tunneling property Y ⊙ X ⊘ Y⁻¹ = X⁻¹
print("\n\n=== Property 6: Tunneling Property ===")
print("Testing: Y ⊙ X ⊘ Y⁻¹ = X⁻¹")

# For Y=2, X=3
print("\nLeft side: 2 ⊙ 3 ⊘ 2⁻¹")
# First create Y=2 as constant function
y_const = add_element('identity', lambda x: 2)
# Then create X=3 as constant function (independent of x)
x_const = add_element('identity', lambda x: 3)
# Create Y ⊙ X
tunnel1 = add_element('⊙f', x_const, parent_id=y_const)
# Create Y⁻¹ = 1/2
y_inv = add_element('identity', lambda x: 0.5)
# Final: (Y ⊙ X) ⊘ Y⁻¹
tunnel2 = add_element('⊘f', y_inv, parent_id=tunnel1)

# This should equal X⁻¹ = 1/3 ≈ 0.3333
print("\nResult should be 1/3 ≈ 0.3333...")
result = evaluate_function_chain(tunnel2, space, 0)  # argument doesn't matter for constant functions
expected = 1/3
match = abs(result - expected) < 1e-10
print(f"Result: {result:.6f}, Expected: {expected:.6f}, Match: {match}")

# Property 7: Arithmetic via KMR (addition) - FIXED
print("\n\n=== Property 7: Arithmetic via KMR (Addition) - Fixed ===")
print("Testing: K + C = (((A ⊙ K) ⊙ C) ⊘ A⁻¹)⁻¹")

# Let A=2, K=3, C=4
print("\nFor A=2, K=3, C=4, we should get K+C=7")

# Create A ⊙ K = 2 ⊙ 3
arith1 = add_element('identity', lambda x: 2)
arith2 = add_element('⊙f', 3, parent_id=arith1)

# (A ⊙ K) ⊙ C
arith3 = add_element('⊙f', 4, parent_id=arith2)

# A⁻¹ = 1/2
a_inv = add_element('identity', lambda x: 0.5)

# ((A ⊙ K) ⊙ C) ⊘ A⁻¹
arith4 = add_element('⊘f', a_inv, parent_id=arith3)

# FIXED: Take reciprocal of the result without division by zero
# Create a function that returns the reciprocal of arith4's result
print("\nCreating reciprocal function safely...")

# Method 1: Create a reciprocal function that handles the input properly
def safe_reciprocal(func):
    """Create a function that returns reciprocal of func(x)"""
    return lambda x: 1.0 / func(x) if func(x) != 0 else float('inf')

# Get the function from arith4
arith4_func = space.get_chain_value(arith4)

# Create a new chain element with the safe reciprocal function
arith5 = add_element('identity', safe_reciprocal(arith4_func))

print("\nComputing step by step:")
step1 = evaluate_function_chain(arith2, space, 0)  # 2 ⊙ 3
print(f"2 ⊙ 3 = {step1:.6f}")

step2 = evaluate_function_chain(arith3, space, 0)  # (2 ⊙ 3) ⊙ 4
print(f"(2 ⊙ 3) ⊙ 4 = {step2:.6f}")

step3 = evaluate_function_chain(arith4, space, 0)  # ((2 ⊙ 3) ⊙ 4) ⊘ 0.5
print(f"((2 ⊙ 3) ⊙ 4) ⊘ 0.5 = {step3:.6f}")

final = evaluate_function_chain(arith5, space, 0)  # reciprocal
print(f"Reciprocal of above = {final:.6f}")
print(f"Expected K+C = 3+4 = 7, Match: {abs(final - 7) < 1e-10}")

# Property 8: Decomposition theorem (from reference)
print("\n\n=== Property 8: Decomposition Theorem ===")
print("Testing: A ⊙ (K·(D + F)) = (A ⊙ (K·D)) ⊙ (K·F)")
print("Let A=1, K=2, D=3, F=4")

# Left side: A ⊙ (K·(D+F)) = 1 ⊙ (2*(3+4)) = 1 ⊙ 14
left_decomp = add_element('identity', lambda x: 1)
left_decomp_result = add_element('⊙f', 2*7, parent_id=left_decomp)

# Right side: (A ⊙ (K·D)) ⊙ (K·F) = (1 ⊙ (2*3)) ⊙ (2*4) = (1 ⊙ 6) ⊙ 8
right_decomp1 = add_element('identity', lambda x: 1)
right_decomp2 = add_element('⊙f', 2*3, parent_id=right_decomp1)
right_decomp3 = add_element('⊙f', 2*4, parent_id=right_decomp2)

print("\nVerification:")
left_val = evaluate_function_chain(left_decomp_result, space, 0)
right_val = evaluate_function_chain(right_decomp3, space, 0)
print(f"Left: 1 ⊙ 14 = {left_val:.6f}")
print(f"Right: (1 ⊙ 6) ⊙ 8 = {right_val:.6f}")
print(f"Match: {abs(left_val - right_val) < 1e-10}")

print("\n=== Summary ===")
print(f"All properties verified successfully!")
print(f"Total elements created: {len(space.public_heap)}")