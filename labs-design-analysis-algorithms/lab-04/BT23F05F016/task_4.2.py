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
# -------------------------
# Task 4.2: Fibonacci Numbers
# -------------------------

# 1️⃣ Recursive approach
def fib_recursive(n):
    """Return the nth Fibonacci number using recursion."""
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_recursive(n - 1) + fib_recursive(n - 2)


# 2️⃣ Iterative approach
def fib_iterative(n):
    """Return the nth Fibonacci number using a loop."""
    if n <= 0:
        return 0
    elif n == 1:
        return 1

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


# Example usage:
num = 10
print(f"{num}th Fibonacci number (Recursive):", fib_recursive(num))
print(f"{num}th Fibonacci number (Iterative):", fib_iterative(num))
