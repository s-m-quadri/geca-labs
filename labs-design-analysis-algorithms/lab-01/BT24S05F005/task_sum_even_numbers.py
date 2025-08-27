# -------------------------------------------
# reursion: if n <= 1, return 0
# - Recursive step: if n is even, add n and recurse on n-2
# - Use `range()` with a step of 2 for the iterative version
def sum_even_recursive(n):
    if n <= 1:
        return 0
    if n % 2 == 0:
        return n + sum_even_recursive(n - 2)
    else:
        return sum_even_recursive(n - 1)

def sum_even_iterative(n):
    total = 0
    for i in range(2, n + 1, 2):
        total += i
    return total
