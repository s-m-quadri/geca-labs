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
# -----------------------------------------
# Task 4.1: Factorial (Recursive vs Iterative)
# -----------------------------------------

# 1️⃣ Recursive approach
def factorial_recursive(n):
    """Compute factorial of n using recursion."""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)


# 2️⃣ Iterative approach
def factorial_iterative(n):
    """Compute factorial of n using a loop."""
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


# Example usage:
num = 5
print(f"Factorial of {num} (Recursive):", factorial_recursive(num))
print(f"Factorial of {num} (Iterative):", factorial_iterative(num))
