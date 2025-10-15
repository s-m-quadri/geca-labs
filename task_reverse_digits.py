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
# -------------------------------------------
# TASK: Reverse the Digits of a Number
# -------------------------------------------

def reverse_digits_recursive(n, rev=0):
    # Base case: if n becomes 0, return the reversed number
    if n == 0:
        return rev
    
    # Extract last digit
    last_digit = n % 10
    # Add it to reversed number
    rev = rev * 10 + last_digit
    # Recurse with remaining digits
    return reverse_digits_recursive(n // 10, rev)


def reverse_digits_iterative(n):
    rev = 0
    while n > 0:
        last_digit = n % 10
        rev = rev * 10 + last_digit
        n = n // 10
    return rev


# Example usage
num = 1234

print("Recursive Reverse of", num, ":", reverse_digits_recursive(num))
print("Iterative Reverse of", num, ":", reverse_digits_iterative(num))
