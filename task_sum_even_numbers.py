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

# Recursive version
def sum_even_recursive(n):
    if n <= 1:
        return 0
    
    if n % 2 == 0:
        return n + sum_even_recursive(n - 2)
    else:
        return sum_even_recursive(n - 1)

# Iterative version
def sum_even_iterative(n):
    total = 0
    for i in range(2, n + 1, 2):
        total += i
    return total

# Test both functions
test_n = 10
print(f"Sum of even numbers up to {test_n}:")
print("Recursive result:", sum_even_recursive(test_n))
print("Iterative result:", sum_even_iterative(test_n))

# Test with another number
test_n2 = 15
print(f"\nSum of even numbers up to {test_n2}:")
print("Recursive result:", sum_even_recursive(test_n2))
print("Iterative result:", sum_even_iterative(test_n2))

# Test edge case
test_n3 = 1
print(f"\nSum of even numbers up to {test_n3}:")
print("Recursive result:", sum_even_recursive(test_n3))
print("Iterative result:", sum_even_iterative(test_n3))
