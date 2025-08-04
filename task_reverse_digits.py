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
    """Reverse the digits of n using recursion."""
    if n == 0:
        return acc  # Base case: when n is 0, return accumulated result
    else:
        return reverse_digits_recursive(n // 10, acc * 10 + n % 10)  # Recursive call
def reverse_digits_iterative(n):

    """Reverse the digits of n using iteration."""
    reversed_num = 0
    while n > 0:
        reversed_num = reversed_num * 10 + n % 10  # Append last digit to reversed number
        n //= 10  # Remove last digit from n
    return reversed_num

# Example usage
if __name__ == "__main__":
    example_number = 1234
    print("Recursive reverse:", reverse_digits_recursive(example_number))
    print("Iterative reverse:", reverse_digits_iterative(example_number))
