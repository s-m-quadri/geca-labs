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


# Function 1: Recursive approach
def fib_recursive(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_recursive(n - 1) + fib_recursive(n - 2)


# Function 2: Iterative approach
def fib_iterative(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


# Bonus: Generate Fibonacci sequence up to n (iterative, efficient)
def fib_sequence(n):
    seq = []
    a, b = 0, 1
    for _ in range(n + 1):  # include nth number
        seq.append(a)
        a, b = b, a + b
    return seq


# Example usage
n = 6
print("Recursive:", fib_recursive(n))     # Output: 8
print("Iterative:", fib_iterative(n))     # Output: 8
print("Sequence up to n:", fib_sequence(n))  # Output: [0, 1, 1, 2, 3, 5, 8]
