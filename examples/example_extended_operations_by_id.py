# extended_example_with_graph.py
"""
Extended example of using ID operations with space state visualization
"""

from kmr_chains import get_default_space, add_element
from kmr_chains_operations_by_id import create_id_handlers, ID_OPERATION_ALIASES


def print_enhanced_chain_graph(space):
    """Print enhanced chain structure with better formatting"""
    print("\n🎯 ENHANCED CHAIN GRAPH WITH VALUES:")
    print("=" * 80)

    # Build parent-child relationships
    children = {}
    for elem_id, private_elem in space.private_heap.items():
        parent_id = private_elem.parent_id
        if parent_id not in children:
            children[parent_id] = []
        children[parent_id].append(elem_id)

    # Find roots
    roots = []
    for elem_id, private_elem in space.private_heap.items():
        parent_id = private_elem.parent_id
        if parent_id is None or parent_id not in space.private_heap:
            roots.append(elem_id)

    def build_enhanced_graph(node_id, depth=0, prefix="", is_last=True):
        # Get element data
        if node_id in space.public_heap:
            public_elem = space.public_heap[node_id]
            private_elem = space.private_heap[node_id]

            # Format value
            value_display = public_elem.value
            if isinstance(value_display, str) and len(value_display) == 32:
                value_display = f"ref:{value_display[:8]}..."
            elif isinstance(value_display, float):
                value_display = f"{value_display:.6f}"

            # Format operation and values
            before = f"{private_elem.chain_value_before:.6f}"
            after = f"{private_elem.chain_value_after:.6f}"

            # Display with connector
            connector = "└── " if is_last else "├── "
            print(f"{prefix}{connector}{node_id[:8]}... [{public_elem.operation} {value_display}]")
            print(f"{prefix}    {' ' * 4}Before: {before} → After: {after}")
        else:
            print(f"{prefix}[ROOT:{node_id[:8] if isinstance(node_id, str) else 'None'}]")

        # Process children
        if node_id in children:
            child_list = children[node_id]
            for i, child_id in enumerate(child_list):
                is_last_child = (i == len(child_list) - 1)
                child_prefix = prefix + ("    " if is_last else "│   ")
                build_enhanced_graph(child_id, depth + 1, child_prefix, is_last_child)

    if roots:
        for i, root in enumerate(roots):
            if i > 0:
                print()
            build_enhanced_graph(root)
    else:
        print("No graph structure found")

def print_chain_connections(space):
    """Print parent-child connections as a graph with branching visualization"""
    print("\n🔗 CHAIN CONNECTIONS (with branching):")
    print("-" * 50)

    # Build parent-child relationships
    parent_to_children = {}
    for elem_id, private_elem in space.private_heap.items():
        parent_id = private_elem.parent_id
        if parent_id not in parent_to_children:
            parent_to_children[parent_id] = []
        parent_to_children[parent_id].append(elem_id)

    # Build child-to-parent mapping
    child_to_parent = {}
    for elem_id, private_elem in space.private_heap.items():
        child_to_parent[elem_id] = private_elem.parent_id

    # Find all chains (paths from roots to leaves)
    def get_chain_paths(start_id, current_path=None):
        if current_path is None:
            current_path = []

        current_path = current_path + [start_id]

        # If no children, this is a leaf
        if start_id not in parent_to_children or not parent_to_children[start_id]:
            return [current_path]

        paths = []
        children = parent_to_children[start_id]

        for i, child_id in enumerate(children):
            # Add branching marker for multiple children
            if len(children) > 1:
                branch_marker = f"[BRANCH {i + 1}/{len(children)}]"
                paths.extend(get_chain_paths(child_id, current_path + [branch_marker]))
            else:
                paths.extend(get_chain_paths(child_id, current_path))

        return paths

    # Find root elements (elements whose parents don't exist in space)
    roots = []
    for elem_id in space.private_heap:
        parent_id = child_to_parent[elem_id]
        if parent_id is None or parent_id not in space.private_heap:
            roots.append(elem_id)

    # Print all chains
    chain_counter = 1
    for root in roots:
        paths = get_chain_paths(root)

        for path in paths:
            print(f"Chain {chain_counter}: ", end="")
            chain_counter += 1

            for i, item in enumerate(path):
                if item.startswith("[BRANCH"):
                    print(f" \n       {item} → ", end="")
                elif isinstance(item, str) and len(item) == 32:
                    if i == 0:
                        print(f"[ROOT:{item[:8]}...]", end="")
                    else:
                        print(f"[{item[:8]}...]", end="")

                    if i < len(path) - 1 and not path[i + 1].startswith("[BRANCH"):
                        print(" → ", end="")
                else:
                    print(f"{item}", end="")
                    if i < len(path) - 1:
                        print(" → ", end="")
            print()

    print("\n📊 BRANCHING ANALYSIS:")
    print("-" * 50)

    # Analyze branching points
    branching_points = {}
    for parent_id, children in parent_to_children.items():
        if len(children) > 1:
            # Try to get the ID of the parent element (might be None for roots)
            parent_display = parent_id[:8] + "..." if parent_id and len(parent_id) == 32 else str(parent_id)
            branching_points[parent_display] = {
                'branch_count': len(children),
                'children': [child_id[:8] + "..." for child_id in children],
                'operations': [space.public_heap[child_id].operation if child_id in space.public_heap else "?"
                               for child_id in children]
            }

    if branching_points:
        for parent, data in branching_points.items():
            print(f"  Branching at {parent}:")
            print(f"    Number of branches: {data['branch_count']}")
            for i, (child, op) in enumerate(zip(data['children'], data['operations']), 1):
                print(f"    Branch {i}: → {child} (operation: {op})")
    else:
        print("  No branching points found")

    # Calculate convergence points (where multiple chains merge)
    print("\n🔄 CONVERGENCE POINTS (if any):")
    print("-" * 50)

    element_ref_count = {}
    for children_list in parent_to_children.values():
        for child in children_list:
            element_ref_count[child] = element_ref_count.get(child, 0) + 1

    convergence_points = {elem: count for elem, count in element_ref_count.items() if count > 1}

    if convergence_points:
        for elem_id, count in convergence_points.items():
            elem_display = elem_id[:8] + "..." if len(elem_id) == 32 else elem_id
            print(f"  Element {elem_display} is referenced by {count} different parents")
    else:
        print("  No convergence points (tree structure)")


# Main example
print("🚀 INITIALIZING KMR CHAIN SPACE WITH ID OPERATIONS")
print("-" * 60)

# Get the default space
space = get_default_space()
print(f"✓ Default space created: {space}")

# Create handlers for ID operations
id_handlers = create_id_handlers(lambda: space)

# Register ID operations in the space
for op_symbol, handler in id_handlers.items():
    space.register_operation(op_symbol, handler, op_map=ID_OPERATION_ALIASES)

print("✓ ID operations registered")
print(f"  - Handlers: {list(id_handlers.keys())}")
print(f"  - Aliases: {len(ID_OPERATION_ALIASES)} entries")

print("\n🔗 CREATING CHAIN A: A1 ⊙ 2 ⊙ 3 ⊙ 4")
print("-" * 40)

a1_id = add_element('⊙', 2)
print(f"  Created A1: ID={a1_id[:8]}..., value=2, operation=⊙")

a2_id = add_element('⊙', 3, parent_id=a1_id)
print(f"  Created A2: ID={a2_id[:8]}..., value=3, operation=⊙, parent={a1_id[:8]}...")

a3_id = add_element('⊙', 4, parent_id=a2_id)
print(f"  Created A3: ID={a3_id[:8]}..., value=4, operation=⊙, parent={a2_id[:8]}...")

print(f"  Chain A complete: {a1_id[:8]}... → {a2_id[:8]}... → {a3_id[:8]}...")

print("\n🔗 CREATING CHAIN B: B1 ⊙ 1.5 ⊙ 2 ⊙ 3")
print("-" * 40)

b1_id = add_element('⊙', 1.5)
print(f"  Created B1: ID={b1_id[:8]}..., value=1.5, operation=⊙")

b2_id = add_element('⊙', 2, parent_id=b1_id)
print(f"  Created B2: ID={b2_id[:8]}..., value=2, operation=⊙, parent={b1_id[:8]}...")

b3_id = add_element('⊙', 3, parent_id=b2_id)
print(f"  Created B3: ID={b3_id[:8]}..., value=3, operation=⊙, parent={b2_id[:8]}...")

print(f"  Chain B complete: {b1_id[:8]}... → {b2_id[:8]}... → {b3_id[:8]}...")

print("\n➕ CREATING ID OPERATIONS (COMBINING CHAINS)")
print("-" * 40)

# Example 2: Sum the results of the two chains
sum_id = add_element('+id', b3_id, parent_id=a3_id)
print(f"  Created SUM: ID={sum_id[:8]}..., value=ref:{b3_id[:8]}..., operation=+id, parent={a3_id[:8]}...")
print(f"    Operation: Chain A result + Chain B result (via reference)")

# Example 3: Multiply the result of chain A by the result of chain B
mul_id = add_element('*id', b3_id, parent_id=a3_id)
print(f"  Created MUL: ID={mul_id[:8]}..., value=ref:{b3_id[:8]}..., operation=*id, parent={a3_id[:8]}...")
print(f"    Operation: Chain A result × Chain B result (via reference)")

# Example 4: Direct KMR operation with the result of another chain
kmr_id = add_element('⊙id', b3_id, parent_id=a3_id)
print(f"  Created KMR: ID={kmr_id[:8]}..., value=ref:{b3_id[:8]}..., operation=⊙id, parent={a3_id[:8]}...")
print(f"    Operation: Chain A result ⊙ Chain B result (via reference)")


print_enhanced_chain_graph(space)

print_chain_connections(space)

print("\n📊 FINAL RESULTS")
print("=" * 60)

# Calculate and display all results
chain_a_result = space.get_chain_value(a3_id)
chain_b_result = space.get_chain_value(b3_id)
sum_result = space.get_chain_value(sum_id)
mul_result = space.get_chain_value(mul_id)
kmr_result = space.get_chain_value(kmr_id)

print(f"🔗 Chain A (A1⊙2⊙3⊙4): {chain_a_result:.6f}")
print(f"   A1 = 2")
print(f"   A2 = 3 (A1⊙2 = {space.get_chain_value(a1_id):.6f} ⊙ 3)")
print(f"   A3 = 4 (A2⊙3 = {space.get_chain_value(a2_id):.6f} ⊙ 4)")
print()

print(f"🔗 Chain B (B1⊙1.5⊙2⊙3): {chain_b_result:.6f}")
print(f"   B1 = 1.5")
print(f"   B2 = 2 (B1⊙1.5 = {space.get_chain_value(b1_id):.6f} ⊙ 2)")
print(f"   B3 = 3 (B2⊙2 = {space.get_chain_value(b2_id):.6f} ⊙ 3)")
print()

print(f"➕ Sum (A+B via +id): {sum_result:.6f}")
print(f"   = {chain_a_result:.6f} + {chain_b_result:.6f}")
print(f"   Verification: {chain_a_result + chain_b_result:.6f}")
print()

print(f"✖️ Product (A×B via *id): {mul_result:.6f}")
print(f"   = {chain_a_result:.6f} × {chain_b_result:.6f}")
print(f"   Verification: {chain_a_result * chain_b_result:.6f}")
print()

print(f"⊙ KMR(A,B via ⊙id): {kmr_result:.6f}")
print(f"   = {chain_a_result:.6f} ⊙ {chain_b_result:.6f}")
print(f"   = {chain_a_result:.6f} / (1 + {chain_b_result:.6f} * {chain_a_result:.6f})")

print("\n✅ OPERATION VERIFICATION")
print("-" * 40)

# Verify all operations are consistent
print(f"Chain A consistency check:")
for elem_id in [a1_id, a2_id, a3_id]:
    consistent = space.check_consistency(elem_id)
    print(f"  [{elem_id[:8]}...]: {'✓ Consistent' if consistent else '✗ Inconsistent'}")

print(f"\nChain B consistency check:")
for elem_id in [b1_id, b2_id, b3_id]:
    consistent = space.check_consistency(elem_id)
    print(f"  [{elem_id[:8]}...]: {'✓ Consistent' if consistent else '✗ Inconsistent'}")

print(f"\nID operations consistency check:")
for elem_id, op_name in [(sum_id, "SUM"), (mul_id, "MUL"), (kmr_id, "KMR")]:
    consistent = space.check_consistency(elem_id)
    print(f"  {op_name} [{elem_id[:8]}...]: {'✓ Consistent' if consistent else '✗ Inconsistent'}")

print("\n" + "=" * 60)
print("🎉 EXAMPLE COMPLETED SUCCESSFULLY!")
print("=" * 60)