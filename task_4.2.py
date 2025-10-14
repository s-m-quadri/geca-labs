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
# fibonacci_task.py
# Task 4.2: Fibonacci Numbers

def fib_recursive(n):
    """Return the nth Fibonacci number using recursion"""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fib_recursive(n - 1) + fib_recursive(n - 2)


def fib_iterative(n):
    """Return the nth Fibonacci number using iteration"""
    if n == 0:
        return 0
    elif n == 1:
        return 1

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


def fib_sequence(n):
    """Return the full Fibonacci sequence up to nth number"""
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
print(f"{n}th Fibonacci number (recursive): {fib_recursive(n)}")  # Output: 8
print(f"{n}th Fibonacci number (iterative): {fib_iterative(n)}")  # Outp_
