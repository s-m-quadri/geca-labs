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
def reverse_digits_recursive(n, reversed_num=0):
    if n == 0:
        return reversed_num

    last_digit = n % 10
    reversed_num = reversed_num * 10 + last_digit
    return reverse_digits_recursive(n // 10, reversed_num)

# Iterative version
def reverse_digits_iterative(n):
    reversed_num = 0
    while n > 0:
        last_digit = n % 10
        reversed_num = reversed_num * 10 + last_digit
        n = n // 10
    return reversed_num

# Test both functions
test_number = 1234
print(f"Original number: {test_number}")
print(f"Recursive reverse: {reverse_digits_recursive(test_number)}")
print(f"Iterative reverse: {reverse_digits_iterative(test_number)}")

# Test with another number
test_number2 = 56789
print(f"\nOriginal number: {test_number2}")
print(f"Recursive reverse: {reverse_digits_recursive(test_number2)}")
print(f"Iterative reverse: {reverse_digits_iterative(test_number2)}")