"""Task 4.1: Factorial (Recursive vs Iterative)

Provides two implementations:
- factorial_recursive(n)
- factorial_iterative(n)
"""
from __future__ import annotations

def factorial_recursive(n: int) -> int:
    """Return n! computed recursively. Raises ValueError for negative n."""
    if n < 0:
        raise ValueError("n must be >= 0")
    if n == 0:
        return 1
    return n * factorial_recursive(n - 1)

def factorial_iterative(n: int) -> int:
    """Return n! computed iteratively. Raises ValueError for negative n."""
    if n < 0:
        raise ValueError("n must be >= 0")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

if __name__ == "__main__":
    import sys
    try:
        if len(sys.argv) > 1:
            n = int(sys.argv[1])
        else:
            n = int(input("Enter non-negative integer n: ").strip())
    except Exception as e:
        print("Invalid input:", e)
        sys.exit(1)

    print(f"{n}! (recursive) = {factorial_recursive(n)}")
    print(f"{n}! (iterative) = {factorial_iterative(n)}")
