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
    if n == 0:
        return 0
    elif n == 1:
        return 1
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

def fib_sequence(n):
    sequence = []
    for i in range(n + 1):
        sequence.append(fib_iterative(i))
    return sequence

n = int(input())
print(fib_recursive(n))
print(fib_iterative(n))
print(fib_sequence(n))
