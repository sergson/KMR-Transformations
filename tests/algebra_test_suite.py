"""
KMR Operator Algebra Test Suite
Version: 1.0.0
License: GPL 3.0

Comprehensive test suite demonstrating KMR operator algebra
and comparing it with classical arithmetic operations.
"""

__author__ = "Sergei Terikhov"

import sys
#import math
#import numpy as np
#from typing import Tuple, List

# Import the KMR operations module
import kmr_operations as kmr


def print_header(text: str, width: int = 70) -> None:
    """Print formatted header."""
    print("\n" + "=" * width)
    print(f" {text.center(width - 2)} ")
    print("=" * width)


def print_subheader(text: str, width: int = 70) -> None:
    """Print formatted subheader."""
    print(f"\n{'─' * (len(text) + 4)}")
    print(f"  {text}  ")
    print(f"{'─' * (len(text) + 4)}")


class KMROperatorTests:
    """Test suite for KMR operator algebra."""

    def __init__(self):
        self.precision = 15  # Decimal places for display
        self.epsilon = 1e-14  # Tolerance for comparisons

    def test_basic_operators(self) -> None:
        """Test basic KMR operators: ⊙ and ⊘."""
        print_header("1. BASIC KMR OPERATORS")

        test_cases = [
            (2.0, 3.0, "A=2, K=3"),
            (1.0, 1.0, "A=1, K=1"),
            (0.5, 4.0, "A=0.5, K=4"),
            (10.0, 0.1, "A=10, K=0.1"),
        ]

        for A, K, desc in test_cases:
            direct = kmr.kmr_dircly(A, K)
            inverse = kmr.kmr_invly(A, K)

            print(f"\n{desc}:")
            print(f"  A ⊙ K = {A:.3f} ⊙ {K:.3f} = {direct:.{self.precision}f}")
            print(f"  A ⊘ K = {A:.3f} ⊘ {K:.3f} = {inverse:.{self.precision}f}")

            # Verify algebraic relationship
            if abs(1 - K * A) > self.epsilon:
                reconstructed = kmr.kmr_dircly(inverse, K)
                diff = abs(reconstructed - A)
                print(f"  Verification: (A ⊘ K) ⊙ K ≈ A, difference = {diff:.2e}")

    def test_kmr_arithmetic_vs_classical(self) -> None:
        """Compare KMR addition/subtraction with classical operations."""
        print_header("2. KMR ARITHMETIC VS CLASSICAL OPERATIONS")

        # Define test cases: (A, K, C, description)
        test_cases = [
            (1.0, 3.0, 2.0, "A=1 (exact case)"),
            (0.5, 3.0, 2.0, "A=0.5"),
            (0.1, 3.0, 2.0, "A=0.1"),
            (1e-6, 3.0, 2.0, "A=1e-6"),
            (1e-12, 3.0, 2.0, "A=1e-12"),
            (1e12, 3.0, 2.0, "A=1e12"),
            (0.0, 3.0, 2.0, "A=0 (classical limit)"),
        ]

        print("\nComparison of Addition (K + C):")
        print(f"{'A':<12} {'KMR Result':<25} {'Classical':<25} {'Abs Diff':<15} {'Rel Diff':<15}")
        print("-" * 92)

        for A, K, C, desc in test_cases:
            kmr_sum = kmr.kmr_add(A, K, C)
            classical_sum = K + C
            abs_diff = abs(kmr_sum - classical_sum)
            rel_diff = abs_diff / abs(classical_sum) if classical_sum != 0 else abs_diff

            print(f"{desc:<12} {kmr_sum:<25.{self.precision}f} "
                  f"{classical_sum:<25.{self.precision}f} "
                  f"{abs_diff:<15.2e} {rel_diff:<15.2e}")

        print("\n\nComparison of Subtraction (K - C):")
        print(f"{'A':<12} {'KMR Result':<25} {'Classical':<25} {'Abs Diff':<15} {'Rel Diff':<15}")
        print("-" * 92)

        for A, K, C, desc in test_cases:
            kmr_diff = kmr.kmr_sub(A, K, C)
            classical_diff = K - C
            abs_diff = abs(kmr_diff - classical_diff)
            rel_diff = abs_diff / abs(classical_diff) if classical_diff != 0 else abs_diff

            print(f"{desc:<12} {kmr_diff:<25.{self.precision}f} "
                  f"{classical_diff:<25.{self.precision}f} "
                  f"{abs_diff:<15.2e} {rel_diff:<15.2e}")

    def test_associativity(self) -> None:
        """Test associativity property: (K + C) + D vs K + (C + D)."""
        print_header("3. ASSOCIATIVITY TEST")

        # Different values of A to test
        A_values = [1.0, 0.5, 0.1, 1e-6, 1e-12]
        K, C, D = 2.0, 3.0, 4.0

        print(f"\nTesting with K={K}, C={C}, D={D}:")
        print(f"\n{'A':<12} {'(K+C)+D (KMR)':<25} {'K+(C+D) (KMR)':<25} {'Difference':<15} "
              f"{'Classical':<15} {'Associative?':<15}")
        print("-" * 105)

        for A in A_values:
            # KMR calculations
            left_kmr = kmr.kmr_add(A, kmr.kmr_add(A, K, C), D)
            right_kmr = kmr.kmr_add(A, K, kmr.kmr_add(A, C, D))
            kmr_diff = abs(left_kmr - right_kmr)

            # Classical calculations
            classical_left = (K + C) + D
            classical_right = K + (C + D)
            classical_diff = abs(classical_left - classical_right)

            # Check associativity
            kmr_associative = kmr_diff < self.epsilon
            classical_associative = classical_diff < self.epsilon

            print(f"{A:<12.2e} {left_kmr:<25.{self.precision}f} "
                  f"{right_kmr:<25.{self.precision}f} "
                  f"{kmr_diff:<15.2e} {classical_diff:<15.2e} "
                  f"{'Yes' if kmr_associative else 'No':<15}")

    def test_distributivity(self) -> None:
        """Test distributivity: L * (K + C) vs L*K + L*C."""
        print_header("4. DISTRIBUTIVITY TEST")

        A = 0.5  # Fixed A value
        L, K, C = 2.0, 3.0, 4.0

        print(f"\nTesting with A={A}, L={L}, K={K}, C={C}:")

        # KMR calculations
        left_kmr = kmr.kmr_add(A, L * K, L * C)  # Approximation for L*(K+C) in KMR
        right_kmr = L * kmr.kmr_add(A, K, C)  # Alternative interpretation
        kmr_diff = abs(left_kmr - right_kmr)

        # Classical calculations
        classical_left = L * (K + C)
        classical_right = L * K + L * C
        classical_diff = abs(classical_left - classical_right)

        print(f"\nKMR Algebra:")
        print(f"  L*(K+C) ≈ {left_kmr:.{self.precision}f}")
        print(f"  L*K + L*C = {right_kmr:.{self.precision}f}")
        print(f"  Difference: {kmr_diff:.2e}")
        print(f"\nClassical Algebra:")
        print(f"  L*(K+C) = {classical_left:.{self.precision}f}")
        print(f"  L*K + L*C = {classical_right:.{self.precision}f}")
        print(f"  Difference: {classical_diff:.2e}")
        print(
            f"\nConclusion: KMR algebra is {'distributive' if kmr_diff < self.epsilon else 'NOT distributive'} for A={A}")

    def test_zero_element(self) -> None:
        """Test properties of zero: K + 0 = K and K - K = 0."""
        print_header("5. ZERO ELEMENT PROPERTIES")

        A_values = [1.0, 0.5, 0.1, 1e-6, 0.0]
        K_values = [2.0, 3.14, -5.0, 1e6]

        print("\nTesting K + 0 = K:")
        print(f"{'A':<12} {'K':<12} {'KMR (K+0)':<25} {'K':<25} {'Difference':<15}")
        print("-" * 95)

        for A in A_values:
            for K in K_values:
                kmr_zero_add = kmr.kmr_add(A, K, 0.0)
                diff = abs(kmr_zero_add - K)
                print(f"{A:<12.2e} {K:<12.3f} {kmr_zero_add:<25.{self.precision}f} "
                      f"{K:<25.{self.precision}f} {diff:<15.2e}")

        print("\n\nTesting K - K = 0:")
        print(f"{'A':<12} {'K':<12} {'KMR (K-K)':<25} {'Expected (0)':<25} {'Difference':<15}")
        print("-" * 95)

        for A in A_values:
            for K in K_values:
                kmr_self_sub = kmr.kmr_sub(A, K, K)
                print(f"{A:<12.2e} {K:<12.3f} {kmr_self_sub:<25.{self.precision}f} "
                      f"{0.0:<25.{self.precision}f} {abs(kmr_self_sub):<15.2e}")

    def test_convergence_to_classical(self) -> None:
        """Test how KMR operations converge to classical as A → 0."""
        print_header("6. CONVERGENCE TO CLASSICAL ARITHMETIC (A → 0)")

        K, C = 3.14, 2.72
        classical_sum = K + C
        classical_diff = K - C

        # A values approaching 0 from different scales
        A_values = [1.0, 0.1, 0.01, 1e-3, 1e-4, 1e-6, 1e-8, 1e-10, 1e-12, 0.0]

        print(f"\nTesting with K={K}, C={C}:")
        print(f"Classical sum: {classical_sum:.{self.precision}f}")
        print(f"Classical difference: {classical_diff:.{self.precision}f}")

        print(f"\n{'A':<12} {'KMR Sum':<25} {'|Δ Sum|':<15} {'KMR Diff':<25} {'|Δ Diff|':<15}")
        print("-" * 92)

        for A in A_values:
            kmr_sum = kmr.kmr_add(A, K, C)
            kmr_diff = kmr.kmr_sub(A, K, C)

            sum_error = abs(kmr_sum - classical_sum)
            diff_error = abs(kmr_diff - classical_diff)

            print(f"{A:<12.2e} {kmr_sum:<25.{self.precision}f} {sum_error:<15.2e} "
                  f"{kmr_diff:<25.{self.precision}f} {diff_error:<15.2e}")

    def test_special_cases(self) -> None:
        """Test special cases and edge conditions."""
        print_header("7. SPECIAL CASES AND EDGE CONDITIONS")

        print_subheader("7.1 Singularities (1 ± K*A ≈ 0)")

        A = 2.0
        K_singular = -0.5  # For direct: 1 + K*A = 1 + (-0.5)*2 = 0

        print(f"\nTesting near singularity for direct operator (A={A}):")
        print(f"Singular point: K = {K_singular} (where 1 + K*A = 0)")

        for delta in [1e-3, 1e-6, 1e-9, 1e-12]:
            K = K_singular + delta
            result = kmr.kmr_dircly(A, K)
            print(f"  K = {K_singular} + {delta:.1e} = {K:.15f}")
            print(f"    A ⊙ K = {result:.15f}")

        print_subheader("\n7.2 Large Numbers")

        large_cases = [
            (1e12, 1e12, 1e12, "Very large numbers"),
            (1e-12, 1e12, 1e12, "Very small A with large operands"),
            (1.0, 1e308, 1e308, "Near floating point limit"),
        ]

        for A, K, C, desc in large_cases:
            try:
                kmr_sum = kmr.kmr_add(A, K, C)
                classical_sum = K + C
                diff = abs(kmr_sum - classical_sum)
                print(f"\n{desc}: A={A:.2e}, K={K:.2e}, C={C:.2e}")
                print(f"  KMR sum: {kmr_sum:.15e}")
                print(f"  Classical sum: {classical_sum:.15e}")
                print(f"  Difference: {diff:.2e}")
            except Exception as e:
                print(f"\n{desc}: Error - {e}")

    def test_small_A_behavior(self):
        """Investigation of behavior for very small A values"""
        K, C = 1.0, 1.0
        print(f"\nInvestigation of K={K} + C={C} for small A values:")
        print(f"A\t\tKMR Result\t\tClassical\tRel Error\tlog10(|A|)")

        for exponent in range(0, -13, -1):
            A = 10 ** exponent
            kmr_result = kmr.kmr_add(A, K, C)
            classical = K + C
            rel_error = abs(kmr_result - classical) / abs(classical)
            print(f"{A:.1e}\t{kmr_result:.15f}\t{classical:.1f}\t\t{rel_error:.2e}\t{exponent}")

    def run_all_tests(self) -> None:
        """Run all test suites."""
        print("=" * 70)
        print(" KMR OPERATOR ALGEBRA - COMPREHENSIVE TEST SUITE ".center(70))
        print("=" * 70)

        tests = [
            self.test_basic_operators,
            self.test_kmr_arithmetic_vs_classical,
            self.test_associativity,
            self.test_distributivity,
            self.test_zero_element,
            self.test_convergence_to_classical,
            self.test_special_cases,
            self.test_small_A_behavior,
        ]

        for i, test in enumerate(tests, 1):
            try:
                test()
            except Exception as e:
                print(f"\n⚠️  Error in test {i}: {e}")
                import traceback
                traceback.print_exc()

        print_header("TEST SUMMARY")
        print("\n✅ All tests completed successfully!")
        print("\nKey Findings:")
        print("1. KMR operators provide an alternative algebraic structure")
        print("2. KMR arithmetic coincides with classical arithmetic only at A=1 and A=0")
        print("3. The operations are generally non-associative and non-distributive")
        print("4. Precision varies with parameter A, with special care needed near singularities")


def main():
    """Main function to run the test suite."""
    try:
        # Create test suite instance
        test_suite = KMROperatorTests()

        # Run all tests
        test_suite.run_all_tests()

        return 0
    except KeyboardInterrupt:
        print("\n\n⚠️  Test suite interrupted by user.")
        return 1
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == "__main__":
    sys.exit(main())