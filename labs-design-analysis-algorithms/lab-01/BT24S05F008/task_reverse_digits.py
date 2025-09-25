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

def reverse_digits_iterative(num):
    rev = 0
    while(num>0):
        ld = num%10
        rev = (rev*10)+ld
        num = num//10
    return rev

def reverse_digits_recursive(num,rev):
    if num == 0:
        return rev
    ld = num %10
    rev = (rev*10)+ld
    return reverse_digits_recursive(num//10,rev)


print("Iterativey Reversed Number : ",reverse_digits_iterative(1234))
print("Recursively Reversed Number : ",reverse_digits_recursive(1234,0))