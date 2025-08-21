# -------------------------------------------
# Problem: Sum even numbers from 1 to n
# Example: n=6 → 2+4+6=12
# -------------------------------------------

def sum_even_numbers_recursive(n):
    if n <= 0:
        return 0
    if n % 2 == 0:
        return n + sum_even_numbers_recursive(n - 2)
    else:
        return sum_even_numbers_recursive(n - 1)

def sum_even_numbers_iterative(n):
    total = 0
    for i in range(2, n + 1, 2):
        total += i
    return total

if __name__ == "__main__":
    n = int(input("Enter n: "))
    print("Recursive sum of even numbers:", sum_even_numbers_recursive(n))
    print("Iterative sum of even numbers:", sum_even_numbers_iterative(n))
