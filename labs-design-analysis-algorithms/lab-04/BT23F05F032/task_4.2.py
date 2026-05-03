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
# -----------------------------
# Recursive Fibonacci
# -----------------------------
def fib_recursive(n):
    """
    Returns the nth Fibonacci number using recursion.
    Note: Exponential time for large n.
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib_recursive(n - 1) + fib_recursive(n - 2)


# -----------------------------
# Iterative Fibonacci
# -----------------------------
def fib_iterative(n):
    """
    Returns the nth Fibonacci number using iteration.
    Time complexity: O(n)
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    if n == 0:
        return 0
    a, b = 0, 1
    for _ in range(1, n):
        a, b = b, a + b
    return b


# -----------------------------
# Bonus: Full sequence up to n
# -----------------------------
def fib_sequence(n):
    """
    Returns the full Fibonacci sequence up to the nth number (0-based).
    """
    if n < 0:
        raise ValueError("n must be non-negative")
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


# -----------------------------
# Example Usage
# -----------------------------
n = 6
print("Recursive Fibonacci of", n, "is:", fib_recursive(n))  # Output: 8
print("Iterative Fibonacci of", n, "is:", fib_iterative(n))  # Output: 8
print("Full Fibonacci sequence up to", n, ":", fib_sequence(n))  # Output: [0,1,1,2,3,5,8]
