def sum_even_recursive(n):
    if n <= 1:
        return 0
    if n % 2 == 0:
        return n + sum_even_recursive(n-2)
    else:
        return sum_even_recursive(n-1)

def sum_even_iterative(n):
    s = 0
    for i in range(2, n+1, 2):
        s += i
    return s

n = 10
print("Recursive:", sum_even_recursive(n))
print("Iterative:", sum_even_iterative(n))
