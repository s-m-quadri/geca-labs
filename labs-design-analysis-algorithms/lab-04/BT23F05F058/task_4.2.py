# Recursive version
def fib_recursive(n):
    if n <= 1:
        return n
    return fib_recursive(n - 1) + fib_recursive(n - 2)


# Iterative version
def fib_iterative(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


# Bonus: Print the full Fibonacci sequence up to n
def fib_sequence(n):
    seq = []
    a, b = 0, 1
    for _ in range(n + 1):
        seq.append(a)
        a, b = b, a + b
    return seq


# Example usage
n = 6
print("Recursive:", fib_recursive(n))  # Output: 8
print("Iterative:", fib_iterative(n))  # Output: 8
print("Sequence up to n:", fib_sequence(n))  # Output: [0, 1, 1, 2, 3, 5, 8]
