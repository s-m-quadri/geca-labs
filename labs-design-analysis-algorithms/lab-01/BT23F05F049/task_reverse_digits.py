# -------------------------------------------
# TASK: Reverse the Digits of a Number
# -------------------------------------------
# Write two functions:
#   1. reverse_digits_recursive(n): recursive
#   2. reverse_digits_iterative(n): loop-based
#
# Example:
#   Input: 1234
#   Output: 4321
#
# -------------------------------------------
# HINTS:
# - Recursive version can peel off last digit using n % 10
# - You may pass an extra parameter (e.g., accumulator) if needed
# - Iterative version: use while-loop and integer math

# Recursive version
def reverse_digits_recursive(n, ref=0):
    if n == 0:  
        return ref
    last_digit = n % 10
    return reverse_digits_recursive(n // 10, ref * 10 + last_digit)


# Function to reverse digits using iteration
def reverse_digits_iterative(n):
    ref = 0
    while n > 0:
        last_digit = n % 10
        ref = ref * 10 + last_digit
        n //= 10
    return ref

num = 1234
print("Recursive Output:", reverse_digits_recursive(num))
print("Iterative Output:", reverse_digits_iterative(num))