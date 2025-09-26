# -------------------------------------------
# Problem: Sum of first n natural numbers
# Example: sum(5) = 1 + 2 + 3 + 4 + 5 = 15
# -------------------------------------------

# BT23F05F042
# Recursive version
def sum_recursive(n):
    if n == 0:
        return 0
    return n + sum_recursive(n - 1)

# Iterative version
def sum_iterative(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

# Try both
n = 10
print("Recursive sum:", sum_recursive(n))
print("Iterative sum:", sum_iterative(n))
