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

# Factorial using recursion
def factorial_recursive(n: int) -> int:
    if n == 0 or n == 1:  # base case
        return 1
    return n * factorial_recursive(n - 1)  # recursive step


# Factorial using iteration (loop)
def factorial_iterative(n: int) -> int:
    result = 1
    for i in range(2, n + 1):  # multiply numbers from 2 to n
        result *= i
    return result


# Example usage
if __name__ == "__main__":
    n = 5
    print("Recursive:", factorial_recursive(n))   # Output: 120
    print("Iterative:", factorial_iterative(n))   # Output: 120

