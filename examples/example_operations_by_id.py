# example_operations_by_id.py
"""
Example of using ID operations without modifying the core code
"""

from kmr_chains import get_default_space, add_element
from kmr_chains_operations_by_id import create_id_handlers, ID_OPERATION_ALIASES

# Get the default space
space = get_default_space()

# Create handlers for ID operations
id_handlers = create_id_handlers(lambda: space)

# Register ID operations in the space
for op_symbol, handler in id_handlers.items():
    space.register_operation(op_symbol, handler, op_map=ID_OPERATION_ALIASES)

# Now we can use ID operations!

# Example 1: Create two chains
# Chain A: A1 ⊙ 2 ⊙ 3 ⊙ 4
a1_id = add_element('⊙', 2)
a2_id = add_element('⊙', 3, parent_id=a1_id)
a3_id = add_element('⊙', 4, parent_id=a2_id)

# Chain B: B1 ⊙ 1.5 ⊙ 2 ⊙ 3
b1_id = add_element('⊙', 1.5)
b2_id = add_element('⊙', 2, parent_id=b1_id)
b3_id = add_element('⊙', 3, parent_id=b2_id)

# Example 2: Sum the results of the two chains
# Using +id, where the second parameter is the ID of element b3
sum_id = add_element('+id', b3_id, parent_id=a3_id)

# Example 3: Multiply the result of chain A by the result of chain B
mul_id = add_element('*id', b3_id, parent_id=a3_id)

# Example 4: Direct KMR operation with the result of another chain
kmr_id = add_element('⊙id', b3_id, parent_id=a3_id)

print("Results:")
print(f"Chain A: {space.get_chain_value(a3_id)}")
print(f"Chain B: {space.get_chain_value(b3_id)}")
print(f"Sum (A+B): {space.get_chain_value(sum_id)}")
print(f"Product (A*B): {space.get_chain_value(mul_id)}")
print(f"KMR(A, B): {space.get_chain_value(kmr_id)}")