# -------------------------------------------
# TASK: Sum of Even Numbers up to n
# -------------------------------------------
# Write two functions:
#   1. sum_even_recursive(n): uses recursion
#   2. sum_even_iterative(n): uses a loop
#
# Example:
#   Input: n = 10
#   Output: 2 + 4 + 6 + 8 + 10 = 30
#
# -------------------------------------------
# HINTS:
# - Base case for recursion: if n <= 1, return 0
# - Recursive step: if n is even, add n and recurse on n-2
# - Use `range()` with a step of 2 for the iterative version

# ---------------- Sum of Even Numbers ----------------

# Recursive function to sum even numbers up to n
def sum_even_recursive(n):
    if n <= 1:
        return 0
    if n % 2 != 0:
        n -= 1  # Make n even
    return n + sum_even_recursive(n - 2)

# Iterative function to sum even numbers up to n
def sum_even_iterative(n):
    total = 0
    for i in range(2, n + 1, 2):
        total += i
    return total

# -------------------- Main Program --------------------
if __name__ == "__main__":
    n = int(input("Enter a positive integer n: "))
    if n < 1:
        print("Please enter a positive integer.")
    else:
        sum_rec = sum_even_recursive(n)
        sum_iter = sum_even_iterative(n)

        print(f"Sum of even numbers up to {n} (recursive): {sum_rec}")
        print(f"Sum of even numbers up to {n} (iterative): {sum_iter}")
