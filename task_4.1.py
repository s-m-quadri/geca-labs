# Recursive version
def factorial_recursive(n):
    if n == 0 or n == 1:   # base case
        return 1
    return n * factorial_recursive(n - 1)


# Iterative version
def factorial_iterative(n):
    result = 1
    for i in range(2, n + 1):  # start from 2 since multiplying by 1 does nothing
        result *= i
    return result


# Test both
n = 5
print("Recursive factorial of", n, ":", factorial_recursive(n))
print("Iterative factorial of", n, ":", factorial_iterative(n))
