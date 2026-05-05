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

def fib_recursive(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_recursive(n - 1) + fib_recursive(n - 2)

def fib_iterative(n):
    a, b = 0, 1
    sequence = []
    for _ in range(n + 1):
        sequence.append(a)
        a, b = b, a + b
    return sequence

n = 6
print("Recursive nth Fibonacci:", fib_recursive(n))
print("Iterative full sequence up to n:", fib_iterative(n))
