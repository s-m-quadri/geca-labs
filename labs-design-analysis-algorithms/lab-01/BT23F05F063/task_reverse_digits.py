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

def reverse_digits_recursive(n, acc=0):
    if n == 0:
        return acc
    return reverse_digits_recursive(n // 10, acc * 10 + n % 10)

def reverse_digits_iterative(n):
    reversed_num = 0
    while n > 0:
        digit = n % 10
        reversed_num = reversed_num * 10 + digit
        n = n // 10
    return reversed_num

# Test the functions
num = 1234
print("Original number:", num)
print("Recursive reverse:", reverse_digits_recursive(num))
print("Iterative reverse:", reverse_digits_iterative(num))
