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

# Task 4.1: Factorial (Recursive vs Iterative)
# --------------------------------------------


# 1. Recursive approach
def factorial_recursive(n):
    if n < 0:
        return "Invalid input! Factorial is not defined for negative numbers."
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)

# 2. Iterative approach
def factorial_iterative(n):
    if n < 0:
        return "Invalid input! Factorial is not defined for negative numbers."
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


if __name__ == "__main__":
    n = int(input("Enter a non-negative integer: "))
    print(f"Factorial of {n} (recursive): {factorial_recursive(n)}")
    print(f"Factorial of {n} (iterative): {factorial_iterative(n)}")
