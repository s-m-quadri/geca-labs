def reverse_digits_recursive(n, rev=0):
    if n == 0:
        return rev
    return reverse_digits_recursive(n // 10, rev * 10 + n % 10)

def reverse_digits_iterative(n):
    rev = 0
    while n > 0:
        rev = rev * 10 + n % 10
        n //= 10
    return rev

n = 1234
print(reverse_digits_recursive(n))
print(reverse_digits_iterative(n))
