# -------------------------------------------
# TASK: Sum of Even Numbers up to n
# -------------------------------------------

# solution
def sum_even_recursive(n):
    """Returns the sum of even numbers up to n using recursion."""
    if n <= 1:
        return 0
    if n % 2 == 0:
        return n + sum_even_recursive(n - 2)
    else:
        return sum_even_recursive(n - 1)

def sum_even_iterative(n):
    """Returns the sum of even numbers up to n using a loop."""
    return sum(i for i in range(2, n + 1, 2))

# Example usage:
if __name__ == "__main__":
    n = 10
    print("Recursive:", sum_even_recursive(n))
    print("Iterative:", sum_even_iterative(n))