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

n = 10
print("Recursive sum:", sum_even_recursive(n))
print("Iterative sum:", sum_even_iterative(n))
