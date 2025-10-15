# Task 4.1: Factorial (Recursive vs Iterative)
# -----------------------------------------
# Write two functions:
# 1. factorial_recursive(n): Uses recursion to compute factorial of n.
# 2. factorial_iterative(n): Uses loops to compute factorial of n.
#
# Input: an integer n (n >= 0)
# Output: factorial of n (n!)
#
# Example:
# Input: 5
# Output: 120
#
# Hint: Start with the mathematical definition:
# factorial(n) = 1 if n == 0 else n * factorial(n-1)
def factorial_recursive(n):
    """Compute factorial using recursion."""
    if n < 0:
        raise ValueError("n must be >= 0")
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)

def factorial_iterative(n):
    """Compute factorial using iteration."""
    if n < 0:
        raise ValueError("n must be >= 0")
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

if __name__ == "__main__":
    # Test both functions
    test_values = [0, 1, 5, 7]

    print("Testing Factorial Functions:")
    print("-" * 40)

    for n in test_values:
        rec_result = factorial_recursive(n)
        iter_result = factorial_iterative(n)
        print(f"n = {n}")
        print(f"  Recursive: {rec_result}")
        print(f"  Iterative: {iter_result}")
        print(f"  Match: {rec_result == iter_result}")
        print()