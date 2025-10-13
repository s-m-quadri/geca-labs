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
    if n <= 1:
        return n
    return fib_recursive(n-1) + fib_recursive(n-2)

def fib_iterative(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

# Print nth Fibonacci number
print(fib_recursive(6))
print(fib_iterative(6))

# Bonus: Print the whole sequence up to n
def fib_sequence(n):
    seq = []
    a, b = 0, 1
    for _ in range(n+1):
        seq.append(a)
        a, b = b, a + b
    return seq

print(fib_sequence(6))
