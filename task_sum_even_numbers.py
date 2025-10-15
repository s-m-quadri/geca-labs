def sum_even_recursive(n):
    if n <= 1:
        return 0
    if n % 2 != 0:
        n -= 1
    return n + sum_even_recursive(n - 2)

def sum_even_iterative(n):
    s = 0
    for i in range(2, n + 1, 2):
        s += i
    return s

n = 10
print(sum_even_recursive(n))
print(sum_even_iterative(n))
