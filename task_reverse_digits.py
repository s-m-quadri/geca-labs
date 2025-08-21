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

def reverse_digits_recursive(num,sum=0):
    if num<=0:
        return sum

    rem = num%10
    sum= sum*10+rem
    return reverse_digits_recursive(num//10,sum)

num = 1234
print(reverse_digits_recursive(num))
