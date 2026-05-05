# -------------------------------------------
# TASK: Reverse the Digits of a Number
# -------------------------------------------

#solution
def reverse_digits_recursive(n):
    """Returns the digits of n reversed using recursion."""
    def helper(n, result):
        if n == 0:
            return result
        return helper(n // 10, result * 10 + n % 10)
    return helper(n, 0)

def reverse_digits_iterative(n):
    """Returns the digits of n reversed using a loop."""
    result = 0
    while n > 0:
        result = result * 10 + n % 10
        n //= 10
    return result

# Example usage:
if __name__ == "__main__":
    num = 56789
    print("Recursive:", reverse_digits_recursive(num))
    print("Iterative:", reverse_digits_iterative(num))