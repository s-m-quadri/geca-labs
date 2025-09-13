# Task 4.2: Fibonacci Numbers
# -------------------------
# Write two versions of Fibonacci sequence generator:
# 1. fib_recursive(n): Uses recursion to return the nth Fibonacci number.
# 2. fib_iterative(n): Uses a loop to return the nth Fibonacci number.
#
# Input: an integer n (n >= 0)
# Output: nth Fibonacci number
#
# Example:
# Input: 6
# Output: 8
#
# Bonus: Try printing the whole Fibonacci sequence up to n instead of just nth number.
# Recursive version: returns the nth Fibonacci number
def fib_recursive(n):
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fib_recursive(n - 1) + fib_recursive(n - 2)

def fib_iterative(n):
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    if n == 0:
        return 0
    elif n == 1:
        return 1

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

def fib_sequence(n):
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    sequence = []
    a, b = 0, 1
    for _ in range(n + 1):
        sequence.append(a)
        a, b = b, a + b
    return sequence


# Example usage:
print("Recursive:", fib_recursive(6))      # Output: 8
print("Iterative:", fib_iterative(6))      # Output: 8
print("Sequence up to 6:", fib_sequence(6))  # Output: [0, 1, 1, 2, 3, 5, 8]
