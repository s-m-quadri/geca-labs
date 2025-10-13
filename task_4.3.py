# -----------------------------
# Full Fibonacci sequence up to n
# -----------------------------
def fib_sequence(n):
    """
    Returns the full Fibonacci sequence up to the nth number (0-based).
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    seq = []
    a, b = 0, 1
    for i in range(n + 1):
        if i == 0:
            seq.append(0)
        elif i == 1:
            seq.append(1)
        else:
            a, b = b, a + b
            seq.append(b)
    return seq


# -----------------------------
# Example Usage
# -----------------------------
n = 6
print("Recursive Fibonacci of", n, "is:", fib_recursive(n))  # Output: 8
print("Iterative Fibonacci of", n, "is:", fib_iterative(n))  # Output: 8
print("Full Fibonacci sequence up to", n, ":", fib_sequence(n))  # Output: [0,1,1,2,3,5,8]
