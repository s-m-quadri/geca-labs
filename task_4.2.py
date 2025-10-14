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
    """Compute nth Fibonacci number using recursion."""
    if n < 0:
        raise ValueError("n must be >= 0")
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib_recursive(n - 1) + fib_recursive(n - 2)

def fib_iterative(n):
    """Compute nth Fibonacci number using iteration."""
    if n < 0:
        raise ValueError("n must be >= 0")
    if n == 0:
        return 0
    if n == 1:
        return 1

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

def fib_sequence(n):
    """Generate Fibonacci sequence up to nth number."""
    if n < 0:
        raise ValueError("n must be >= 0")

    sequence = []
    a, b = 0, 1
    for i in range(n + 1):
        if i == 0:
            sequence.append(0)
        elif i == 1:
            sequence.append(1)
        else:
            sequence.append(a + b)
            a, b = b, a + b
    return sequence

if __name__ == "__main__":
    # Test both functions
    test_values = [0, 1, 6, 10]

    print("Testing Fibonacci Functions:")
    print("-" * 40)

    for n in test_values:
        if n <= 10:  # Only use recursive for small values due to performance
            rec_result = fib_recursive(n)
        else:
            rec_result = "Skipped (too slow)"

        iter_result = fib_iterative(n)
        sequence = fib_sequence(n)

        print(f"n = {n}")
        print(f"  Recursive: {rec_result}")
        print(f"  Iterative: {iter_result}")
        print(f"  Sequence: {sequence}")
        print()