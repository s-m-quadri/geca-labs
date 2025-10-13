# Task 4.1: Factorial (Recursive vs Iterative)
# -----------------------------------------
# Write two functions:
# 1. factorial_recursive(n): Uses recursion to compute factorial of n.
# 2. factorial_iterative(n): Uses loops to compute factorial of n.
#
# Input: an integer n (n >= 0)
# Output: factorial of n (n!)
#
# Example:
# Input: 5
# Output: 120
#
# Hint: Start with the mathematical definition:
# factorial(n) = 1 if n == 0 else n * factorial(n-1)

def f_rec(n):
    if n == 0:
        return 1
    return n * f_rec(n - 1)

def f_itr(n):
    r = 1
    for i in range(1, n + 1):
        r *= i
    return r

n = int(input())
print(f_rec(n))
print(f_itr(n))
