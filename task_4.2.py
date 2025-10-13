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

def fib_recursive(n):
	"""Return the nth Fibonacci number using recursion."""
	if n < 0:
		raise ValueError("n must be >= 0")
	if n == 0:
		return 0
	if n == 1:
		return 1
	return fib_recursive(n-1) + fib_recursive(n-2)

def fib_iterative(n):
	"""Return the nth Fibonacci number using iteration."""
	if n < 0:
		raise ValueError("n must be >= 0")
	a, b = 0, 1
	for _ in range(n):
		a, b = b, a + b
	return a

def fib_sequence(n):
	"""Return the Fibonacci sequence up to n (inclusive)."""
	seq = []
	a, b = 0, 1
	for _ in range(n+1):
		seq.append(a)
		a, b = b, a + b
	return seq

if __name__ == "__main__":
	n = 6
	print(f"Recursive: Fib({n}) =", fib_recursive(n))
	print(f"Iterative: Fib({n}) =", fib_iterative(n))
	print(f"Fibonacci sequence up to {n}:", fib_sequence(n))
