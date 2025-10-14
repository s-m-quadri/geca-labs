# Function 1: Recursive approach
def factorial_recursive(n):
    if n == 0 or n == 1:   # Base case
        return 1
    else:                  # Recursive case
        return n * factorial_recursive(n - 1)

# Function 2: Iterative approach
def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Example usage
n = int(input("Enter a number: "))

print("Factorial (Recursive):", factorial_recursive(n))
print("Factorial (Iterative):", factorial_iterative(n))
