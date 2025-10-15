# Recursive implementation
def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)


# Iterative implementation
def factorial_iterative(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


# Example usage
n = 5
print("Recursive:", factorial_recursive(n))  # Output: 120
print("Iterative:", factorial_iterative(n))  # Output: 120
