def factorial_recursive(n): 
    if n == 0:
        return 1
    return n * factorial_recursive(n - 1)

n=5
print("Recursion:",(factorial_recursive(n)))