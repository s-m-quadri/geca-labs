# Task 4.2: Fibonacci Numbers
# -------------------------
# Write two versions of Fibonacci sequence generator:
# 1. fib_recursive(n): Uses recursion to return the nth Fibonacci number.
# 2. fib_iterative(n): Uses a loop to return the nth Fibonacci number.
#
# Input: an integer n (n >= 0)
# Output: nth Fibonacci number
#
# Example:
# Input: 6
# Output: 8
#
# Bonus: Try printing the whole Fibonacci sequence up to n instead of just nth number.
# ---------------- Fibonacci Functions ----------------

# Recursive Fibonacci function
def fib_recursive(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_recursive(n - 1) + fib_recursive(n - 2)

# Iterative Fibonacci function
def fib_iterative(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

# Generate full Fibonacci sequence up to n
def fibonacci_sequence(n, method="iterative"):
    sequence = []
    if method == "iterative":
        a, b = 0, 1
        for i in range(n + 1):
            sequence.append(a)
            a, b = b, a + b
    elif method == "recursive":
        for i in range(n + 1):
            sequence.append(fib_recursive(i))
    return sequence


# -------------------- Main Program --------------------
if __name__ == "__main__":
    n = int(input("Enter a non-negative integer: "))
    if n < 0:
        print("Input must be a non-negative integer.")
    else:
       
        nth_fib_rec = fib_recursive(n)
        nth_fib_iter = fib_iterative(n)

        print(f"\n{n}th Fibonacci number (recursive): {nth_fib_rec}")
        print(f"{n}th Fibonacci number (iterative): {nth_fib_iter}")

  
        print("\nFull Fibonacci sequence up to n (iterative):")
        print(fibonacci_sequence(n, method="iterative"))

        print("\nFull Fibonacci sequence up to n (recursive):")
        print(fibonacci_sequence(n, method="recursive"))
