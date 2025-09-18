# Task 4.3: Reverse a String
# ------------------------
# Write two functions to reverse a string:
# 1. reverse_recursive(s): Reverse the string using recursion.
# 2. reverse_iterative(s): Reverse the string using a loop.
#
# Input: string s
# Output: reversed string
#
# Example:
# Input: "hello"
# Output: "olleh"
#
# Bonus: Try solving without using Python slicing [::-1].

from functools import lru_cache

# 1. Fibonacci using Recursion
def fib_recursive(n):
    if n < 0:
        raise ValueError("Fibonacci is not defined for negative numbers")
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_recursive(n - 1) + fib_recursive(n - 2)


# 2. Fibonacci using Iteration (Loop)
def fib_iterative(n):
    if n < 0:
        raise ValueError("Fibonacci is not defined for negative numbers")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


# 3. Optimized Recursive Fibonacci (Memoization)
@lru_cache(maxsize=None)
def fib_recursive_optimized(n):
    if n < 0:
        raise ValueError("Fibonacci is not defined for negative numbers")
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_recursive_optimized(n - 1) + fib_recursive_optimized(n - 2)


# 4. Bonus: Generate full Fibonacci sequence up to n
def fib_sequence(n):
    if n < 0:
        raise ValueError("Fibonacci is not defined for negative numbers")
    seq = []
    a, b = 0, 1
    for _ in range(n + 1):
        seq.append(a)
        a, b = b, a + b
    return seq



def fib_generator(n):
    if n < 0:
        raise ValueError("Fibonacci is not defined for negative numbers")
    a, b = 0, 1
    for _ in range(n + 1):
        yield a
        a, b = b, a + b



if __name__ == "__main__":
    n = 6

    print("Recursive Fibonacci of", n, ":", fib_recursive(n))
    print("Iterative Fibonacci of", n, ":", fib_iterative(n))
    print("Optimized Recursive Fibonacci of", n, ":", fib_recursive_optimized(n))
    print("Fibonacci sequence up to", n, ":", fib_sequence(n))
    print("Fibonacci generator up to", n, ":", list(fib_generator(n)))
