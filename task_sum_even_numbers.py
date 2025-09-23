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
# Sum of Even Numbers up to n (Recursive + Iterative)
# -------------------------------------------

# Recursive Function
def sum_even_recursive(n):
    # Base case
    if n <= 1:
        return 0
    
    # If n is even, include it
    if n % 2 == 0:
        return n + sum_even_recursive(n - 2)
    else:
        # If n is odd, skip to nearest even below it
        return sum_even_recursive(n - 1)


# Iterative Function
def sum_even_iterative(n):
    total = 0
    for i in range(2, n + 1, 2):  # loop over evens
        total += i
    return total


# ----------------------------
# Example usage
n = 10
print(f"Sum of even numbers up to {n}:")

print("Recursive:", sum_even_recursive(n))
print("Iterative:", sum_even_iterative(n))
