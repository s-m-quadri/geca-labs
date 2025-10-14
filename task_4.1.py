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
# factorial_task.py
# Task 4.1: Factorial (Recursive vs Iterative)

def factorial_recursive(n):
    """Compute factorial of n using recursion"""
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)


def factorial_iterative(n):
    """Compute factorial of n using iteration"""
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


# Example usage
n = 5
print(f"Factorial of {n} (recursive): {factorial_recursive(n)}")  # Output: 120
print(f"Factorial of {n} (iterative): {factorial_iterative(n)}")  # Output: 120
