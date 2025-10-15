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

# ---------------- Factorial Functions ----------------

# Recursive factorial function
def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)

# Iterative factorial function
def factorial_iterative(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# -------------------- Main Program --------------------
if __name__ == "__main__":
    # Take input from the user
    n = int(input("Enter a non-negative integer: "))
    if n < 0:
        print("Factorial is not defined for negative numbers.")
    else:
        fact_rec = factorial_recursive(n)
        fact_iter = factorial_iterative(n)

        print(f"Recursive factorial of {n} is: {fact_rec}")
        print(f"Iterative factorial of {n} is: {fact_iter}")
