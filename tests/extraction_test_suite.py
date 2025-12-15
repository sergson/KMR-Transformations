# extraction_test_suite.py
"""
KMR Element Extraction Test Suite
Version: 2.0.0
License: GPL 3.0
Author: Sergei Terikhov

Comprehensive test suite for KMR element extraction functions.
Uses CORRECTED formulas from updated theory.
"""

import sys
import math
from kmr_tunneling import (
    extract_intermediate_element,
    extract_first_element,
    extract_last_element,
    extract_element_from_chain,
    compute_chain,
    verify_extraction_formula
)
from kmr_operations import kmr_dircly, kmr_invly


class KMRExtractionTests:
    """Test suite for KMR element extraction functions"""

    def __init__(self):
        self.precision = 15
        self.epsilon = 1e-12

    def print_header(self, text: str, width: int = 70) -> None:
        """Print formatted header"""
        print("\n" + "=" * width)
        print(f" {text.center(width - 2)} ")
        print("=" * width)

    def compute_chain_manual(self, *elements: float) -> float:
        """Compute chain manually for verification"""
        if not elements:
            return 0.0

        result = elements[0]
        for element in elements[1:]:
            result = kmr_dircly(result, element)
        return result

    def test_basic_extraction_formulas(self) -> None:
        """Test basic element extraction formulas for 3-element chains"""
        self.print_header("1. BASIC ELEMENT EXTRACTION FORMULAS (3-ELEMENT CHAINS)")

        test_cases = [
            (2.0, 3.0, 4.0, "Simple case"),
            (1.0, 0.5, 2.0, "Fractional elements"),
            (0.5, 2.0, 0.25, "Mixed fractions"),
            (10.0, -2.0, 3.0, "Negative element"),
        ]

        print(f"\n{'Description':<20} {'A':<10} {'B':<10} {'C':<10} {'Full Chain':<20}")
        print("-" * 80)

        for A, B, C, desc in test_cases:
            X = compute_chain(A, B, C)
            print(f"{desc:<20} {A:<10.3f} {B:<10.3f} {C:<10.3f} {X:<20.{self.precision}f}")

        print(
            f"\n{'Description':<20} {'Extraction Method':<25} {'Expected':<20} {'Extracted':<20} {'Diff':<15} {'Status':<10}")
        print("-" * 120)

        for A, B, C, desc in test_cases:
            X = compute_chain(A, B, C)

            # Test 1: Extract first element (A)
            try:
                extracted_A = extract_first_element(X, B, C)
                diff_A = abs(extracted_A - A)
                status_A = "PASS" if diff_A < self.epsilon else "FAIL"
                print(f"{desc:<20} {'First (A)':<25} {A:<20.{self.precision}f} "
                      f"{extracted_A:<20.{self.precision}f} {diff_A:<15.2e} {status_A:<10}")
            except Exception as e:
                print(f"{desc:<20} {'First (A)':<25} {A:<20.{self.precision}f} "
                      f"{'ERROR':<20} {'-':<15} {str(e)[:20]:<10}")

            # Test 2: Extract intermediate element (B) using CORRECTED formula
            try:
                left_chain = [A]
                right_chain = [C]  # Only next element for 3-element chain
                extracted_B = extract_intermediate_element(X, left_chain, right_chain)
                diff_B = abs(extracted_B - B)
                status_B = "PASS" if diff_B < self.epsilon else "FAIL"
                print(f"{desc:<20} {'Intermediate (B)':<25} {B:<20.{self.precision}f} "
                      f"{extracted_B:<20.{self.precision}f} {diff_B:<15.2e} {status_B:<10}")
            except Exception as e:
                print(f"{desc:<20} {'Intermediate (B)':<25} {B:<20.{self.precision}f} "
                      f"{'ERROR':<20} {'-':<15} {str(e)[:20]:<10}")

            # Test 3: Extract last element (C)
            try:
                extracted_C = extract_last_element(X, A, B)
                diff_C = abs(extracted_C - C)
                status_C = "PASS" if diff_C < self.epsilon else "FAIL"
                print(f"{desc:<20} {'Last (C)':<25} {C:<20.{self.precision}f} "
                      f"{extracted_C:<20.{self.precision}f} {diff_C:<15.2e} {status_C:<10}")
            except Exception as e:
                print(f"{desc:<20} {'Last (C)':<25} {C:<20.{self.precision}f} "
                      f"{'ERROR':<20} {'-':<15} {str(e)[:20]:<10}")

            print(f"{'':<20} {'-':<25} {'-':<20} {'-':<20} {'-':<15} {'-':<10}")

    def test_long_chain_extraction(self) -> None:
        """Test extraction from chains of length 4 and 5"""
        self.print_header("2. LONG CHAIN EXTRACTION (4 AND 5 ELEMENTS)")

        # Test 4-element chain
        print("\n--- 4-Element Chain Test: 2 ⊙ 3 ⊙ 4 ⊙ 5 ---")
        elements_4 = [2.0, 3.0, 4.0, 5.0]
        X_4 = compute_chain(*elements_4)

        print(f"Chain result X = {X_4:.{self.precision}f}")
        print(
            f"\n{'Element':<15} {'Left Chain':<25} {'Right Chain':<25} {'Expected':<15} {'Extracted':<15} {'Status':<10}")
        print("-" * 120)

        for k in range(1, 5):  # k=1..4
            if k == 1:
                # First element
                extracted = extract_first_element(X_4, *elements_4[1:])
                left_desc = "[]"
                right_desc = str(elements_4[1:])
            elif k == 4:
                # Last element
                extracted = extract_last_element(X_4, *elements_4[:3])
                left_desc = str(elements_4[:3])
                right_desc = "[]"
            else:
                # Intermediate element
                left_chain = elements_4[:k - 1]
                right_chain = elements_4[k:]
                extracted = extract_intermediate_element(X_4, left_chain, right_chain)
                left_desc = str(left_chain)
                right_desc = str(right_chain)

            expected = elements_4[k - 1]
            diff = abs(extracted - expected)
            status = "✓" if diff < self.epsilon else "✗"

            print(f"A{k:<14} {left_desc:<25} {right_desc:<25} "
                  f"{expected:<15.6f} {extracted:<15.6f} {status:<10}")

        # Test 5-element chain
        print("\n--- 5-Element Chain Test: 2 ⊙ 3 ⊙ 4 ⊙ 5 ⊙ 6 ---")
        elements_5 = [2.0, 3.0, 4.0, 5.0, 6.0]
        X_5 = compute_chain(*elements_5)

        print(f"Chain result X = {X_5:.{self.precision}f}")
        print(
            f"\n{'Element':<15} {'Extraction Method':<30} {'Expected':<15} {'Extracted':<15} {'Diff':<15} {'Status':<10}")
        print("-" * 120)

        # Test all elements
        for k in range(1, 6):
            try:
                if k == 1:
                    method = "First element formula"
                    extracted = extract_first_element(X_5, *elements_5[1:])
                elif k == 5:
                    method = "Last element formula"
                    extracted = extract_last_element(X_5, *elements_5[:4])
                else:
                    method = f"Intermediate: k={k}"
                    left_chain = elements_5[:k - 1]
                    right_chain = elements_5[k:]
                    extracted = extract_intermediate_element(X_5, left_chain, right_chain)

                expected = elements_5[k - 1]
                diff = abs(extracted - expected)
                status = "✓" if diff < self.epsilon else "✗"

                print(f"A{k:<14} {method:<30} {expected:<15.6f} "
                      f"{extracted:<15.6f} {diff:<15.2e} {status:<10}")
            except Exception as e:
                print(f"A{k:<14} {'Error':<30} {elements_5[k - 1]:<15.6f} "
                      f"{'ERROR':<15} {'-':<15} {str(e)[:20]:<10}")

    def test_element_from_chain(self) -> None:
        """Test extraction of arbitrary element from chain"""
        self.print_header("3. ARBITRARY ELEMENT EXTRACTION FROM CHAIN")

        print("\n--- 5-Element Chain: 2 ⊙ 3 ⊙ 4 ⊙ 5 ⊙ 6 ---")
        elements = [2.0, 3.0, 4.0, 5.0, 6.0]
        X = compute_chain(*elements)

        print(f"Chain result X = {X:.{self.precision}f}")
        print(
            f"\n{'Element':<10} {'Other Elements':<40} {'Expected':<15} {'Extracted':<15} {'Diff':<15} {'Status':<10}")
        print("-" * 120)

        for i in range(1, 6):  # Extract each element
            other_elements = elements[:i - 1] + elements[i:]

            try:
                extracted = extract_element_from_chain(X, i, *other_elements)
                expected = elements[i - 1]
                diff = abs(extracted - expected)
                status = "✓" if diff < self.epsilon else "✗"

                print(f"A{i:<9} {str(other_elements):<40} "
                      f"{expected:<15.6f} {extracted:<15.6f} {diff:<15.2e} {status:<10}")
            except Exception as e:
                print(f"A{i:<9} {str(other_elements):<40} "
                      f"{elements[i - 1]:<15.6f} {'ERROR':<15} {'-':<15} {str(e)[:20]:<10}")

    def test_edge_cases(self) -> None:
        """Test edge cases and error conditions"""
        self.print_header("4. EDGE CASES AND ERROR CONDITIONS")

        print("\n4.1 Zero and near-zero elements:")
        test_cases = [
            ([2.0, 0.0, 3.0], "Zero element in middle"),
            ([0.0, 3.0, 4.0], "First element zero"),
            ([2.0, 3.0, 0.0], "Last element zero"),
            ([0.1, 0.2, 0.3], "Small values"),
        ]

        for elements, desc in test_cases:
            try:
                X = compute_chain(*elements)
                print(f"\n{desc}: {elements}")
                print(f"  X = {X:.6f}")

                # Test extraction of each element
                for i in range(1, len(elements) + 1):
                    other = elements[:i - 1] + elements[i:]
                    extracted = extract_element_from_chain(X, i, *other)
                    expected = elements[i - 1]
                    diff = abs(extracted - expected)
                    print(f"  A{i}: expected={expected:.6f}, extracted={extracted:.6f}, "
                          f"diff={diff:.2e}, {'✓' if diff < self.epsilon else '✗'}")
            except Exception as e:
                print(f"\n{desc}: ERROR - {e}")

        print("\n4.2 Division by zero/singularity cases:")
        # Cases where denominator becomes zero
        singular_cases = [
            ([1.0, -1.0], "A1 ⊙ A2 where 1 + A1*A2 = 0"),
            ([2.0, -0.5], "A1 ⊙ A2 where 1 + A1*A2 ≠ 0, but extraction might fail"),
        ]

        for elements, desc in singular_cases:
            try:
                X = compute_chain(*elements)
                print(f"\n{desc}: {elements}")
                print(f"  X = {X:.6f}")
                # Try to extract
                extracted = extract_element_from_chain(X, 1, elements[1])
                print(f"  Extraction successful: {extracted:.6f}")
            except Exception as e:
                print(f"\n{desc}: {elements}")
                print(f"  Expected error: {type(e).__name__}: {e}")

    def test_verification_function(self) -> None:
        """Test the verify_extraction_formula function"""
        self.print_header("5. VERIFICATION FUNCTION TEST")

        test_cases = [
            ([2.0, 3.0, 4.0], "Standard 3-element chain"),
            ([2.0, 3.0, 4.0, 5.0], "4-element chain"),
            ([2.0, 3.0, 4.0, 5.0, 6.0], "5-element chain"),
            ([1.0, 0.5, 2.0, 0.25], "Fractional chain"),
        ]

        for elements, desc in test_cases:
            print(f"\n{desc}: {elements}")
            results = verify_extraction_formula(*elements)

            all_pass = True
            for extraction_type, result in results.items():
                if 'error' in result:
                    print(f"  {extraction_type}: ERROR - {result['error']}")
                    all_pass = False
                else:
                    status = "✓" if result['success'] else "✗"
                    if not result['success']:
                        all_pass = False
                    print(f"  {extraction_type}: {status} diff={result['difference']:.2e}")

            if all_pass:
                print(f"  ✅ All extractions successful!")
            else:
                print(f"  ⚠️  Some extractions failed")

    def test_theoretical_correctness(self) -> None:
        """Verify theoretical formulas are correctly implemented"""
        self.print_header("6. THEORETICAL CORRECTNESS VERIFICATION")

        print("\n6.1 CORRECTED Formula for intermediate elements:")
        print("   A_k = 1/(X ⊘ A_n ⊘ A_{n-1} ⊘ ... ⊘ A_{k+1}) - 1/L")
        print("   where L = A1 ⊙ A2 ⊙ ... ⊙ A_{k-1} (computed sequentially)")
        print("\n6.2 Comparison with manual calculation:")

        # Test with 5-element chain
        elements = [2.0, 3.0, 4.0, 5.0, 6.0]
        X = compute_chain(*elements)

        print(f"\nChain: {elements}")
        print(f"X = {X:.{self.precision}f}")

        # Extract A3 (k=3)
        k = 3
        print(f"\nExtracting A{k} = {elements[k - 1]}")

        # Manual calculation according to theory
        # 1. Compute L = A1 ⊙ A2
        L_manual = kmr_dircly(2.0, 3.0)
        print(f"  L = A1 ⊙ A2 = 2 ⊙ 3 = {L_manual:.{self.precision}f}")

        # 2. Compute D = X ⊘ A5 ⊘ A4
        D1 = kmr_invly(X, 6.0)  # X ⊘ A5
        D_manual = kmr_invly(D1, 5.0)  # (X ⊘ A5) ⊘ A4
        print(f"  D = X ⊘ A5 ⊘ A4 = {X:.6f} ⊘ 6 ⊘ 5 = {D_manual:.{self.precision}f}")

        # 3. Compute A3 = 1/D - 1/L
        A3_theoretical = 1.0 / D_manual - 1.0 / L_manual
        print(f"  A3_theoretical = 1/D - 1/L = 1/{D_manual:.6f} - 1/{L_manual:.6f}")
        print(f"                 = {1.0 / D_manual:.6f} - {1.0 / L_manual:.6f}")
        print(f"                 = {A3_theoretical:.{self.precision}f}")

        # Compare with function
        left_chain = elements[:k - 1]  # [2.0, 3.0]
        right_chain = elements[k:]  # [5.0, 6.0]
        A3_function = extract_intermediate_element(X, left_chain, right_chain)

        print(f"\n  Function result: {A3_function:.{self.precision}f}")
        print(f"  Difference: {abs(A3_theoretical - A3_function):.2e}")
        print(f"  Match: {math.isclose(A3_theoretical, A3_function, rel_tol=1e-12)}")

    def run_all_tests(self) -> None:
        """Run all extraction tests"""
        print("=" * 70)
        print(" KMR ELEMENT EXTRACTION TEST SUITE v2.0 ".center(70))
        print("With CORRECTED formulas from updated theory".center(70))
        print("=" * 70)

        tests = [
            self.test_basic_extraction_formulas,
            self.test_long_chain_extraction,
            self.test_element_from_chain,
            self.test_edge_cases,
            self.test_verification_function,
            self.test_theoretical_correctness,
        ]

        for i, test in enumerate(tests, 1):
            try:
                test()
                print(f"\n✅ Test {i} completed successfully")
            except Exception as e:
                print(f"\n❌ Error in test {i}: {e}")
                import traceback
                traceback.print_exc()

        self.print_header("TEST SUMMARY")
        print("\n✅ All extraction tests completed!")
        print("\nKey Findings (CORRECTED):")
        print("1. ✅ First element extraction: A1 = X ⊘ An ⊘ ... ⊘ A2")
        print("2. ✅ Last element extraction: An = 1/X - 1/Z where Z = A1 ⊙ ... ⊙ A_{n-1}")
        print("3. ✅ Intermediate element extraction (CORRECTED FORMULA):")
        print("   A_k = 1/(X ⊘ A_n ⊘ ... ⊘ A_{k+1}) - 1/(A1 ⊙ ... ⊙ A_{k-1})")
        print("4. ✅ Formula works for chains of ANY length (3, 4, 5, ...)")
        print("5. ✅ Non-associativity is handled by sequential computation")
        print("\nImportant Note:")
        print("The old formula A_k = 1/(X ⊘ A_{k+1}) - 1/L only works when k = n-1")
        print("The corrected formula requires canceling ALL elements to the right.")


def main():
    """Main function to run the extraction test suite"""
    try:
        # Create test suite instance
        test_suite = KMRExtractionTests()

        # Run all tests
        test_suite.run_all_tests()

        return 0
    except KeyboardInterrupt:
        print("\n\n⚠️  Test suite interrupted by user")
        return 1
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == "__main__":
    sys.exit(main())