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
# Function to reverse digits using recursion
def reverse_digits_recursive(n, rev=0):
    # Base case: when n becomes 0
    if n == 0:
        return rev
    
    # Extract last digit and build reversed number
    rev = rev * 10 + n % 10
    
    # Recursive call with remaining digits
    return reverse_digits_recursive(n // 10, rev)


# Function to reverse digits using iteration (loop)
def reverse_digits_iterative(n):
    rev = 0
    while n > 0:
        rev = rev * 10 + n % 10   # add last digit to reversed number
        n //= 10                  # remove last digit
    return rev


# -------------------------------
# Example usage:
num = 1234

print("Recursive Reverse:", reverse_digits_recursive(num))   # Output: 4321
print("Iterative Reverse:", reverse_digits_iterative(num))   # Output: 4321
