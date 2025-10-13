
# Recursive approach
def factorial_recursive(n):
    if n == 0:
        return 1
    else:
        return n * factorial_recursive(n - 1)

# Iterative approach
def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Test the functions
n = int(input("Enter a non-negative integer: "))

print(f"Recursive factorial of {n} is: {factorial_recursive(n)}")
print(f"Iterative factorial of {n} is: {factorial_iterative(n)}")
