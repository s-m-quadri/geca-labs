# # Recursive approach
def fib_recursive(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_recursive(n - 1) + fib_recursive(n - 2)

# Iterative approach
def fib_iterative(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

# Bonus: Print full Fibonacci sequence up to n
def fib_sequence_iterative(n):
    seq = []
    a, b = 0, 1
    if n >= 0:
        seq.append(0)
    if n >= 1:
        seq.append(1)
    for _ in range(2, n + 1):
        a, b = b, a + b
        seq.append(b)
    return seq

# Test the functions
n = int(input("Enter a non-negative integer: "))

print(f"Recursive Fibonacci of {n} is: {fib_recursive(n)}")
print(f"Iterative Fibonacci of {n} is: {fib_iterative(n)}")
print(f"Full Fibonacci sequence up to {n}: {fib_sequence_iterative(n)}")

