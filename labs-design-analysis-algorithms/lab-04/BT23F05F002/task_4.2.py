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
    return fib_recursive(n - 1) + fib_recursive(n - 2)

def fib_iterative(n):
    if n <= 1:
        return n
    
    a, b = 0, 1
    for i in range(2, n + 1):
        a, b = b, a + b
    return b

def print_fib_sequence(n):
    print(f"Fibonacci sequence up to {n}:")
    for i in range(n + 1):
        print(fib_iterative(i), end=" ")
    print()

n = 6
print(f"Fibonacci number at position {n}:")
print(f"Recursive: {fib_recursive(n)}")
print(f"Iterative: {fib_iterative(n)}")

n = 10
print(f"\nFibonacci number at position {n}:")
print(f"Recursive: {fib_recursive(n)}")
print(f"Iterative: {fib_iterative(n)}")

print_fib_sequence(10)
