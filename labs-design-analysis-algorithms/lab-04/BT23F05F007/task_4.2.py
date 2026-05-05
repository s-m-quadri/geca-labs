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
# Recursive version
def fib_recursive(n):
    if n < 0:
        raise ValueError("Fibonacci not defined for negative numbers.")
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fib_recursive(n - 1) + fib_recursive(n - 2)


# Iterative version
def fib_iterative(n):
    if n < 0:
        raise ValueError("Fibonacci not defined for negative numbers.")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


# Bonus: Print the whole Fibonacci sequence up to n
def fib_sequence(n):
    if n < 0:
        raise ValueError("Fibonacci not defined for negative numbers.")
    seq = []
    a, b = 0, 1
    for _ in range(n + 1):
        seq.append(a)
        a, b = b, a + b
    return seq


# Example test
print(fib_recursive(6))   # Output: 8
print(fib_iterative(6))   # Output: 8
print(fib_sequence(6))    # Output: [0, 1, 1, 2, 3, 5, 8]
