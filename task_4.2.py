"""Task 4.2: Fibonacci Numbers

Provides two implementations:
- fib_recursive(n)
- fib_iterative(n)

Both raise ValueError for negative n. Includes optional sequence printer in CLI.
"""
from __future__ import annotations

from typing import List

def fib_recursive(n: int) -> int:
    """Return the nth Fibonacci number using recursion. Raises ValueError for negative n."""
    if n < 0:
        raise ValueError("n must be >= 0")
    if n < 2:
        return n
    return fib_recursive(n - 1) + fib_recursive(n - 2)

def fib_iterative(n: int) -> int:
    """Return the nth Fibonacci number using an iterative loop. Raises ValueError for negative n."""
    if n < 0:
        raise ValueError("n must be >= 0")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def fib_sequence(n: int) -> List[int]:
    """Return the Fibonacci sequence up to and including the nth element (0..n)."""
    if n < 0:
        raise ValueError("n must be >= 0")
    seq: List[int] = []
    a, b = 0, 1
    for i in range(n + 1):
        seq.append(a)
        a, b = b, a + b
    return seq

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

    # Print nth value (both implementations) and full sequence as a bonus
    try:
        print(f"{n}th Fibonacci (recursive) = {fib_recursive(n)}")
    except RecursionError:
        print("Recursive computation failed due to recursion depth for n =", n)

    print(f"{n}th Fibonacci (iterative) = {fib_iterative(n)}")
    print(f"Fibonacci sequence up to {n}:", fib_sequence(n))
