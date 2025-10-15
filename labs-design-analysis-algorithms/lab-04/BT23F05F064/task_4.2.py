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



# 1. Recursive approach
def fib_recursive(n):
    if n < 0:
        return "Invalid input! Fibonacci is not defined for negative numbers."
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_recursive(n - 1) + fib_recursive(n - 2)

# 2. Iterative approach
def fib_iterative(n):
    if n < 0:
        return "Invalid input! Fibonacci is not defined for negative numbers."
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

# Bonus: Print the whole Fibonacci sequence up to n
def fibonacci_sequence(n):
    if n < 0:
        return "Invalid input!"
    sequence = []
    a, b = 0, 1
    for _ in range(n + 1):
        sequence.append(a)
        a, b = b, a + b
    return sequence

# Example usage
if __name__ == "__main__":
    n = int(input("Enter a non-negative integer: "))
    print(f"{n}th Fibonacci number (recursive): {fib_recursive(n)}")
    print(f"{n}th Fibonacci number (iterative): {fib_iterative(n)}")
    print(f"Fibonacci sequence up to {n}: {fibonacci_sequence(n)}")
