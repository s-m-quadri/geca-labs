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

def reverse_digits_recursive(n, rev=0):
    if n == 0:
        return rev
    return reverse_digits_recursive(n // 10, rev * 10 + n % 10)


def reverse_digits_iterative(n):
    rev = 0
    while n > 0:
        rev = rev * 10 + n % 10
        n //= 10
    return rev


num = 1234
print("Recursive:", reverse_digits_recursive(num))
print("Iterative:", reverse_digits_iterative(num))