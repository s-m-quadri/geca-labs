# -------------------------------------------
# Problem: Sum of first n natural numbers
# Example: sum(5) = 1 + 2 + 3 + 4 + 5 = 15
# -------------------------------------------

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

# Closed-form version
def sum_closed_form(n):
    return n * (n + 1) // 2

# Simple test function
def test_sum_functions():
    test_cases = [0, 1, 5, 10, 100]
    for n in test_cases:
        r = sum_recursive(n)
        i = sum_iterative(n)
        c = sum_closed_form(n)
        assert r == i == c, f"Mismatch for n={n}: {r}, {i}, {c}"
    print("All tests passed.")

# Try all three
n = 10
print("Recursive sum:", sum_recursive(n))
print("Iterative sum:", sum_iterative(n))
print("Closed-form sum:", sum_closed_form(n))

# Run tests
test_sum_functions()
# completed the program