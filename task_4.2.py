# #Task 4.2: Fibonacci Numbers
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
# Fibonacci Numbers
# -------------------------

# Recursive (exponential time, elegant for small n)
# -------------------------
# Fibonacci Numbers
# -------------------------

# Recursive (exponential time, elegant for small n)
def fib_recursive(n):
    if n < 0:
        raise ValueError("Fibonacci not defined for negative numbers")
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib_recursive(n - 1) + fib_recursive(n - 2)


# Iterative (O(n), efficient)
def fib_iterative(n):
    if n < 0:
        raise ValueError("Fibonacci not defined for negative numbers")
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


# Bonus: Full sequence up to n
def fib_sequence(n):
    if n < 0:
        raise ValueError("Fibonacci not defined for negative numbers")
    if n == 0:
        return [0]
    seq = [0, 1]
    for i in range(2, n + 1):
        seq.append(seq[-1] + seq[-2])
    return seq


# -------------------------
# Example usage
# -------------------------
n = 6
print("Recursive (n=6):", fib_recursive(n))   # Output: 8
print("Iterative (n=6):", fib_iterative(n))   # Output: 8
print("Sequence up to n=6:", fib_sequence(n)) # Output: [0, 1, 1, 2, 3, 5, 8]
