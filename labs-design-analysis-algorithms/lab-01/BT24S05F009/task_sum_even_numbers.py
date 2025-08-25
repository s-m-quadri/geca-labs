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
# Recursive version
def sum_even_recursive(n):
    if n <= 1:
        return 0
    if n % 2 != 0:  # if n is odd, reduce by 1 to make it even
        n -= 1
    return n + sum_even_recursive(n - 2)


# Iterative version
def sum_even_iterative(n):
    if n < 2:
        return 0
    if n % 2 != 0:  # if n is odd, reduce by 1
        n -= 1
    total = 0
    for i in range(2, n + 1, 2):  # loop through even numbers
        total += i
    return total


# -------------------------------
# Example usage
n = 10

print("Recursive Sum of Even Numbers:", sum_even_recursive(n))  # Output: 30
print("Iterative Sum of Even Numbers:", sum_even_iterative(n))  # Output: 30
