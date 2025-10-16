# -------------------------------------------
# TASK: Sum of Even Numbers up to n
# -------------------------------------------
# Write two functions:
#   1. sum_even_recursive(n): uses recursion
#   2. sum_even_iterative(n): uses a loop
#
# Example:
#   Input: n = 10
#   Output: 2 + 4 + 6 + 8 + 10 = 30
#
# -------------------------------------------
# HINTS:
# - Base case for recursion: if n <= 1, return 0
# - Recursive step: if n is even, add n and recurse on n-2
# - Use `range()` with a step of 2 for the iterative version
# -------------------------------------------
# TASK: Sum of Even Numbers up to n
# -------------------------------------------

# 1. Recursive approach
def sum_even_recursive(n):
    # Base case: no even numbers below 2
    if n <= 1:
        return 0
    
    # If n is even, include it and recurse by 2
    if n % 2 == 0:
        return n + sum_even_recursive(n - 2)
    else:
        # If n is odd, move to the next smaller even number
        return sum_even_recursive(n - 1)


# 2. Iterative approach
def sum_even_iterative(n):
    total = 0
    # Loop through even numbers only
    for i in range(2, n + 1, 2):
        total += i
    return total


# -------------------------------------------
# Example Usage
# -------------------------------------------
n = 10
print("Recursive Output:", sum_even_recursive(n))
print("Iterative Output:", sum_even_iterative(n))
