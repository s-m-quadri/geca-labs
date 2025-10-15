def fib_recursive(n):
    if n == 0:   
        return 0
    elif n == 1:
        return 1
    else:
        return fib_recursive(n - 1) + fib_recursive(n - 2)

def fib_iterative(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

def fib_sequence(n):
    sequence = []
    a, b = 0, 1
    for _ in range(n + 1):
        sequence.append(a)
        a, b = b, a + b
    return sequence

n = 6
print("Recursive Fibonacci of", n, ":", fib_recursive(n))
print("Iterative Fibonacci of", n, ":", fib_iterative(n))
print("Fibonacci sequence up to", n, ":", fib_sequence(n))
