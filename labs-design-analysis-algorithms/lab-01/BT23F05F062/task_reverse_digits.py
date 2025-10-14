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
# Reverse Digits of a Number (Recursive + Iterative)
# -------------------------------------------

# Recursive Function
def reverse_digits_recursive(n, rev=0):
    # Handle negative numbers
    if n < 0:
        return -reverse_digits_recursive(-n, rev)

    # Base case
    if n == 0:
        return rev
    
    # Extract last digit and build reverse
    last_digit = n % 10
    rev = rev * 10 + last_digit
    
    # Recursive call
    return reverse_digits_recursive(n // 10, rev)


# Iterative Function
def reverse_digits_iterative(n):
    sign = -1 if n < 0 else 1  # track negative numbers
    n = abs(n)
    rev = 0
    while n > 0:
        last_digit = n % 10
        rev = rev * 10 + last_digit
        n //= 10
    return sign * rev


# ----------------------------
# Example usage
num = 1234
neg_num = -567

print("Recursive (positive):", reverse_digits_recursive(num))
print("Iterative (positive):", reverse_digits_iterative(num))

print("Recursive (negative):", reverse_digits_recursive(neg_num))
print("Iterative (negative):", reverse_digits_iterative(neg_num))
