# -------------------------------------------
# TASK: Sum of Even Numbers up to n
# -------------------------------------------
# Write two functions:
#   1. sum_even_recursive(n): uses recursion
#   2. sum_even_iterative(n): uses a loop
#
# Example:
#   Input: n = 10
#   Output: 2 + 4 + 6 + 8 + 10 = 30
#
# -------------------------------------------
# HINTS:
# - Base case for recursion: if n <= 1, return 0
# - Recursive step: if n is even, add n and recurse on n-2
# - Use `range()` with a step of 2 for the iterative version
def sum_even_recursive(n):
    """Calculate the sum of even numbers up to n using recursion."""
    if n <= 1:
        return 0  # Base case: no even numbers to add
    elif n % 2 == 0:
        return n + sum_even_recursive(n - 2)  # If n is even, add it and recurse
    else:
        return sum_even_recursive(n - 1)  # If n is odd, skip it and recurse
def sum_even_iterative(n):
    """Calculate the sum of even numbers up to n using iteration."""
    total = 0
    for i in range(2, n + 1, 2):  # Loop through even numbers only
        total += i  # Add current even number to total
    return total
# Example usage
if __name__ == "__main__":  
    example_n = 10
    print("Recursive sum of even numbers:", sum_even_recursive(example_n))
    print("Iterative sum of even numbers:", sum_even_iterative(example_n))