# -------------------------------------------
# Problem: Reverse digits of a number
# Example: 123 → 321
# -------------------------------------------

def reverse_digits_recursive(n):
    def helper(n, res):
        if n == 0:
            return res
        return helper(n // 10, res * 10 + n % 10)
    return helper(n, 0)

def reverse_digits_iterative(n):
    res = 0
    while n > 0:
        res = res * 10 + n % 10
        n //= 10
    return res

if __name__ == "__main__":
    n = int(input("Enter a number: "))
    print("Recursive reverse:", reverse_digits_recursive(n))
    print("Iterative reverse:", reverse_digits_iterative(n))
