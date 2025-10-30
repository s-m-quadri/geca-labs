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

def factorial_recursive(n: int) -> int:
    """Return n! using recursion. Raises ValueError for negative inputs."""
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    if n < 0:
        raise ValueError("n must be >= 0")
    if n == 0:
        return 1
    return n * factorial_recursive(n - 1)


def factorial_iterative(n: int) -> int:
    """Return n! using an iterative loop. Raises ValueError for negative inputs."""
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    if n < 0:
        raise ValueError("n must be >= 0")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


if __name__ == "__main__":
    # simple demo
    for x in [0, 1, 5, 10]:
        print(f"{x}! (rec) = {factorial_recursive(x)}; (iter) = {factorial_iterative(x)}")
