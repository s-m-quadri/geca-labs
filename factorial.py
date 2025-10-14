# Recursive factorial
def factorial_recursive(n):
    if n == 0:
        return 1
    return n * factorial_recursive(n - 1)
 
# Iterative factorial
def factorial_iterative(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
 
# Driver
n = 5
print("Recursive:", factorial_recursive(n))
print("Iterative:", factorial_iterative(n))
# Completed the program