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
    else:
        return reverse_digits_recursive(n // 10, acc * 10 + n % 10)


def reverse_digits_iterative(n):
    reversed_num = 0
    while n > 0:
        reversed_num = reversed_num * 10 + n % 10
        n //= 10
    return reversed_num 
# Example usage:
if __name__ == "__main__":
    number = 1234
    print("Recursive:", reverse_digits_recursive(number))
    print("Iterative:", reverse_digits_iterative(number))
