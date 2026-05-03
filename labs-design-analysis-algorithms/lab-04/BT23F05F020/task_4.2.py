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
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_recursive(n - 1) + fib_recursive(n - 2)

# Iterative version
def fib_iterative(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

# Bonus: Print entire sequence up to n
def fib_sequence(n):
    seq = []
    a, b = 0, 1
    for i in range(n + 1):
        if i == 0:
            seq.append(0)
        elif i == 1:
            seq.append(1)
        else:
            a, b = b, a + b
            seq.append(b)
    return seq

# Example usage
n = 6
print("Recursive result:", fib_recursive(n))
print("Iterative result:", fib_iterative(n))
print("Fibonacci sequence up to n:", fib_sequence(n))
