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

# Recursive version
def fib_recursive(n):
    if n <= 1:
        return n
    return fib_recursive(n - 1) + fib_recursive(n - 2)


# Iterative version
def fib_iterative(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


# Bonus: Generate the full Fibonacci sequence up to n
def fib_sequence(n):
    seq = []
    a, b = 0, 1
    for _ in range(n + 1):
        seq.append(a)
        a, b = b, a + b
    return seq


# Example usage
n = 6
print("Recursive nth Fibonacci:", fib_recursive(n))
print("Iterative nth Fibonacci:", fib_iterative(n))
print("Fibonacci sequence up to n:", fib_sequence(n))
