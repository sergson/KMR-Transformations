# kmr_tunneling.py
"""
KMR Tunneling and Element Extraction Operations
Version: 3.0.0
License: GPL 3.0 (see LICENSE)
Author: Sergei Terikhov
Date: 08.12.2025
"""

import math
from typing import List, Optional, Union
from kmr_operations import kmr_dircly, kmr_invly


# ========== TUNNELING FUNCTIONS ==========

def kmr_tunnel_transform(Y: float, X: float) -> float:
    """
    Apply tunneling transformation: Y ⊙ X ⊘ Y⁻¹ = X⁻¹

    Args:
        Y: Tunneling parameter (Y ≠ 0)
        X: Input value

    Returns:
        X⁻¹ (inverse of X)

    Raises:
        ValueError: If transformation is undefined
    """
    if Y == 0:
        raise ValueError("Tunneling parameter Y cannot be zero")

    # Y ⊙ X
    Y_odot_X = kmr_dircly(Y, X)
    if math.isnan(Y_odot_X):
        raise ValueError(f"Direct operation Y ⊙ X is undefined for Y={Y}, X={X}")

    # Y⁻¹
    Y_inv = 1.0 / Y

    # (Y ⊙ X) ⊘ Y⁻¹
    result = kmr_invly(Y_odot_X, Y_inv)
    if math.isnan(result):
        raise ValueError(f"Inverse operation (Y ⊙ X) ⊘ Y⁻¹ is undefined")

    return result


def create_tunneling_chain(chain_space, Y: float, X: float) -> str:
    """
    Create a chain that represents Y ⊙ X ⊘ Y⁻¹

    Args:
        chain_space: KMRChainSpace instance
        Y: Tunneling parameter
        X: Input value

    Returns:
        Element ID of the final result
    """
    if Y == 0:
        raise ValueError("Tunneling parameter Y cannot be zero")

    # Step 1: Create starting element with value Y
    start_id = chain_space.add_element(
        operation='+',  # Identity operation
        value=0.0,
        parent_id=None,
        chain_value_before=Y
    )

    # Step 2: Apply ⊙ X operation
    y_odot_x_id = chain_space.add_element(
        operation='⊙',
        value=X,
        parent_id=start_id
    )

    # Step 3: Apply ⊘ Y⁻¹ operation
    Y_inv = 1.0 / Y
    final_id = chain_space.add_element(
        operation='⊘',
        value=Y_inv,
        parent_id=y_odot_x_id
    )

    return final_id


# ========== ELEMENT EXTRACTION FUNCTIONS ==========

def extract_intermediate_element(X: float, left_chain: List[float], right_chain: List[float]) -> float:
    """
    Extract an intermediate element A_k from a KMR chain.
    
    CORRECTED FORMULA (Section 11.3.4):
    A_k = 1/(X ⊘ A_n ⊘ A_{n-1} ⊘ ... ⊘ A_{k+1}) - 1/L
    where L = A1 ⊙ ... ⊙ A_{k-1} (computed from left_chain)
    
    Args:
        X: Full chain result (A1 ⊙ A2 ⊙ ... ⊙ An)
        left_chain: List of elements [A1, ..., A_{k-1}] in original order
        right_chain: List of elements [A_{k+1}, ..., A_n] in original order
        
    Returns:
        The element A_k
        
    Raises:
        ValueError: If extraction is impossible
    """
    # Step 1: Compute L = A1 ⊙ ... ⊙ A_{k-1}
    if left_chain:
        L = left_chain[0]
        for element in left_chain[1:]:
            L = kmr_dircly(L, element)
            if math.isnan(L):
                raise ValueError(f"Cannot compute left part L at element {element}")
    else:
        L = 0.0  # Empty left chain means L = 0 (special case for k=1)
    
    # Step 2: Compute D = X ⊘ A_n ⊘ ... ⊘ A_{k+1}
    D = X
    for element in reversed(right_chain):  # Apply inverse operators in reverse order
        D = kmr_invly(D, element)
        if math.isnan(D):
            raise ValueError(f"Cannot compute X ⊘ ... ⊘ {element}")
    
    # Step 3: Compute A_k = 1/D - 1/L
    if abs(D) < 1e-15:
        raise ValueError(f"Cannot compute 1/D: D={D} (too close to zero)")
    
    if abs(L) < 1e-15:
        raise ValueError(f"Cannot compute 1/L: L={L} (too close to zero)")
    
    result = 1.0 / D - 1.0 / L
    
    # Special handling for near-zero results
    if abs(result) < 1e-15:
        result = 0.0
    
    return result


def extract_first_element(X: float, *chain_elements: float) -> float:
    """
    Extract the first element from a KMR chain.

    Formula: A1 = X ⊘ An ⊘ ... ⊘ A2

    Args:
        X: Full chain result (A1 ⊙ A2 ⊙ ... ⊙ An)
        *chain_elements: Known elements A2, A3, ..., An

    Returns:
        The first element A1

    Raises:
        ValueError: If extraction fails
    """
    if not chain_elements:
        return X  # If no chain elements, X itself is A1

    # Apply inverse operations from right to left
    result = X
    for element in reversed(chain_elements):
        result = kmr_invly(result, element)
        if math.isnan(result):
            raise ValueError(f"Cannot compute inverse at element {element}")

    return result


def extract_last_element(X: float, *chain_elements: float) -> float:
    """
    Extract the last element from a KMR chain.

    Formula: An = X^(-1) - Z^(-1)
    where Z = A1 ⊙ ... ⊙ A_{n-1}

    Args:
        X: Full chain result (A1 ⊙ ... ⊙ An)
        *chain_elements: Known elements A1, A2, ..., A_{n-1}

    Returns:
        The last element An

    Raises:
        ValueError: If extraction fails
    """
    if not chain_elements:
        # If no chain elements, X itself is the only element
        return X

    # Compute Z = A1 ⊙ ... ⊙ A_{n-1}
    Z = chain_elements[0]
    for element in chain_elements[1:]:
        Z = kmr_dircly(Z, element)
        if math.isnan(Z):
            raise ValueError(f"Cannot compute direct operation at element {element}")

    # Check for division by zero
    if X == 0:
        raise ValueError(f"Cannot compute 1/X: X={X}")
    if Z == 0:
        raise ValueError(f"Cannot compute 1/Z: Z={Z}")

    # Compute An = 1/X - 1/Z
    result = 1.0 / X - 1.0 / Z

    return result


def extract_element_from_chain(X: float, element_index: int, *all_elements_except: float) -> float:
    """
    Extract an element from a KMR chain when all other elements are known.

    For a chain A1 ⊙ A2 ⊙ ... ⊙ An = X, extract A_k.

    Args:
        X: Full chain result
        element_index: Index of element to extract (1-based)
        *all_elements_except: All elements except the one to extract

    Returns:
        The extracted element

    Raises:
        ValueError: If extraction fails
    """
    if element_index < 1:
        raise ValueError("Element index must be >= 1")

    n = len(all_elements_except) + 1  # Total number of elements in chain

    # Special cases for first and last elements
    if element_index == 1:
        # Extract first element: A1 = X ⊘ An ⊘ ... ⊘ A2
        return extract_first_element(X, *all_elements_except)

    elif element_index == n:
        # Extract last element: An = 1/X - 1/Z where Z = A1 ⊙ ... ⊙ A_{n-1}
        return extract_last_element(X, *all_elements_except)

    else:
        # Extract intermediate element using corrected formula
        # A_k = 1/(X ⊘ A_n ⊘ ... ⊘ A_{k+1}) - 1/(A1 ⊙ ... ⊙ A_{k-1})
        
        # Split into left and right parts
        left_elements = all_elements_except[:element_index - 1]  # A1..A_{k-1}
        right_elements = all_elements_except[element_index - 1:]  # A_{k+1}..A_n
        
        # Use the corrected extract_intermediate_element function
        return extract_intermediate_element(X, list(left_elements), list(right_elements))


def compute_chain(*elements: float) -> float:
    """
    Compute the result of a KMR chain: A1 ⊙ A2 ⊙ ... ⊙ An
    
    Args:
        *elements: Elements A1, A2, ..., An
        
    Returns:
        Result of the chain
    """
    if not elements:
        return 0.0
    
    result = elements[0]
    for element in elements[1:]:
        result = kmr_dircly(result, element)
        if math.isnan(result):
            return float('nan')
    
    return result


# ========== HELPER FUNCTIONS ==========

def verify_extraction_formula(*elements: float) -> dict:
    """
    Verify extraction formulas on any KMR chain.
    
    Args:
        *elements: Elements of the chain A1, A2, ..., An
        
    Returns:
        Dictionary with verification results for each element
    """
    if len(elements) < 2:
        raise ValueError("Chain must have at least 2 elements")
    
    # Compute full chain
    X = compute_chain(*elements)
    n = len(elements)
    
    results = {}
    
    # Test extraction of each element
    for k in range(1, n + 1):
        try:
            # Create list of all elements except the k-th
            all_except_k = list(elements[:k-1]) + list(elements[k:])
            
            # Extract element
            extracted = extract_element_from_chain(X, k, *all_except_k)
            
            # Compare with expected
            expected = elements[k-1]
            diff = abs(expected - extracted)
            
            results[f'A{k}_extraction'] = {
                'expected': expected,
                'extracted': extracted,
                'difference': diff,
                'success': math.isclose(expected, extracted, rel_tol=1e-12, abs_tol=1e-15)
            }
            
        except Exception as e:
            results[f'A{k}_extraction'] = {'error': str(e)}
    
    # Additional test: verify intermediate element extraction directly
    if n >= 3:
        for k in range(2, n):  # Only intermediate elements
            try:
                left_chain = list(elements[:k-1])
                right_chain = list(elements[k:])
                
                extracted = extract_intermediate_element(X, left_chain, right_chain)
                expected = elements[k-1]
                
                results[f'A{k}_direct_extraction'] = {
                    'expected': expected,
                    'extracted': extracted,
                    'difference': abs(expected - extracted),
                    'success': math.isclose(expected, extracted, rel_tol=1e-12, abs_tol=1e-15)
                }
            except Exception as e:
                results[f'A{k}_direct_extraction'] = {'error': str(e)}
    
    return results


# ========== EXAMPLE AND TEST FUNCTIONS ==========

def run_example_tests():
    """Run example tests from the documentation"""
    print("=== KMR Extraction Tests ===")
    
    # Test 1: 3-element chain
    print("\n1. Testing 3-element chain: 2 ⊙ 3 ⊙ 4")
    X = compute_chain(2, 3, 4)
    print(f"   Chain result X = {X:.6f}")
    
    results = verify_extraction_formula(2, 3, 4)
    for key, value in results.items():
        if 'success' in value:
            status = "✓" if value['success'] else "✗"
            print(f"   {key}: {status} expected={value['expected']}, extracted={value['extracted']:.6f}, diff={value['difference']:.2e}")
    
    # Test 2: 4-element chain
    print("\n2. Testing 4-element chain: 2 ⊙ 3 ⊙ 4 ⊙ 5")
    X = compute_chain(2, 3, 4, 5)
    print(f"   Chain result X = {X:.6f}")
    
    results = verify_extraction_formula(2, 3, 4, 5)
    for key, value in results.items():
        if 'success' in value:
            status = "✓" if value['success'] else "✗"
            print(f"   {key}: {status} expected={value['expected']}, extracted={value['extracted']:.6f}, diff={value['difference']:.2e}")
    
    # Test 3: 5-element chain
    print("\n3. Testing 5-element chain: 2 ⊙ 3 ⊙ 4 ⊙ 5 ⊙ 6")
    X = compute_chain(2, 3, 4, 5, 6)
    print(f"   Chain result X = {X:.6f}")
    
    results = verify_extraction_formula(2, 3, 4, 5, 6)
    for key, value in results.items():
        if 'success' in value:
            status = "✓" if value['success'] else "✗"
            print(f"   {key}: {status} expected={value['expected']}, extracted={value['extracted']:.6f}, diff={value['difference']:.2e}")
    
    print("\n=== All tests completed ===")


if __name__ == "__main__":
    run_example_tests()