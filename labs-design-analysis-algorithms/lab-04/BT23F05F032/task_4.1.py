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
# Recursive approach
def factorial_recursive(n):
    """
    Computes factorial of n using recursion.
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    if n == 0:
        return 1
    return n * factorial_recursive(n - 1)


# Iterative approach
def factorial_iterative(n):
    """
    Computes factorial of n using iteration (loop).
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


# --------------------------
# Example Usage
# --------------------------
n = 5
print("Recursive factorial of", n, "is:", factorial_recursive(n))  # Output: 120
print("Iterative factorial of", n, "is:", factorial_iterative(n))  # Output: 120
