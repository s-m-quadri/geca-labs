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
def reverse_digits_recursive(n, result=0):
    if n == 0:
        return result
    last_digit = n % 10
    result = result * 10 + last_digit
    return reverse_digits_recursive(n // 10, result)

def reverse_digits_iterative(n):
    result = 0
    while n > 0:
        last_digit = n % 10
        result = result * 10 + last_digit
        n //= 10
    return result

n = 1234

print("Recursive Reverse Digits:")
print(reverse_digits_recursive(n))

print("Iterative Reverse Digits:")
print(reverse_digits_iterative(n))
