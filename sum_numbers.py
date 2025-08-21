# -------------------------------------------
# Problem: Sum of first n natural numbers
# Example: sum(5) = 1 + 2 + 3 + 4 + 5 = 15
# -------------------------------------------

def sum_numbers_recursive(n):
    if n <= 0:
        return 0
    return n + sum_numbers_recursive(n - 1)

def sum_numbers_iterative(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

if __name__ == "__main__":
    n = int(input("Enter n: "))
    print("Recursive sum:", sum_numbers_recursive(n))
    print("Iterative sum:", sum_numbers_iterative(n))
