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

#solution
def factorial_recursive(n):
    """Compute factorial of n recursively."""
    if n < 0:
        raise ValueError("n must be >= 0")
    if n == 0:
        return 1
    return n * factorial_recursive(n - 1)

def factorial_iterative(n):
    """Compute factorial of n using iteration."""
    if n < 0:
        raise ValueError("n must be >= 0")
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Example (very important)
print("Recursive Factorial Examples:")
print("5! =", factorial_recursive(5))   #i'd expect 120 as output
print("0! =", factorial_recursive(0))   #here output should be 1
print("7! =", factorial_recursive(7))   #and here 5040 (yusss)

print("\nIterative Factorial Examples:")
print("6! =", factorial_iterative(6))   #i'd expect 720 as output
print("2! =", factorial_iterative(2))   #umm 2 should be output here
print("8! =", factorial_iterative(8))   #40320 for sure
