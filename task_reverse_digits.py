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

# Function 1: Recursive approach
def reverse_digits_recursive(n, rev=0):
    # Base case: when number becomes 0
    if n == 0:
        return rev
    
    # Extract last digit and build reversed number
    rev = rev * 10 + n % 10
    
    # Recursive call with remaining digits
    return reverse_digits_recursive(n // 10, rev)


# Function 2: Iterative approach
def reverse_digits_iterative(n):
    rev = 0
    while n > 0:
        rev = rev * 10 + n % 10  # Add last digit
        n //= 10                 # Remove last digit
    return rev


# Example usage
num = 1234
print("Recursive Output:", reverse_digits_recursive(num))
print("Iterative Output:", reverse_digits_iterative(num))
