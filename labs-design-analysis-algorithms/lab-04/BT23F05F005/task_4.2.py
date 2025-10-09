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

#solution
def fib_recursive(n):
    """Return the nth Fibonacci number using recursion."""
    if n < 0:
        raise ValueError("n must be >= 0")
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib_recursive(n - 1) + fib_recursive(n - 2)

def fib_iterative(n):
    """Return the nth Fibonacci number using iteration."""
    if n < 0:
        raise ValueError("n must be >= 0")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


#examples 
print("Recursive Fibonacci:")
print("5th Fibonacci number:", fib_recursive(5))   
print("13th Fibonacci number:", fib_recursive(13))   
print("1st Fibonacci number:", fib_recursive(1))   

print("\nIterative Fibonacci:")
print("6th Fibonacci number:", fib_iterative(8))   
print("7th Fibonacci number:", fib_iterative(7))  
print("1st Fibonacci number:", fib_iterative(1))   

