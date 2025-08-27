# -------------------------------------------
# TASK: Sum of Even Numbers up to n
# -------------------------------------------
# Write two functions:
#   1. sum_even_recursive(n): uses recursion
#   2. sum_even_iterative(n): uses a loop
#
# Example:
#   Input: n = 10
#   Output: 2 + 4 + 6 + 8 + 10 = 30
#
# -------------------------------------------
# HINTS:
# - Base case for recursion: if n <= 1, return 0
# - Recursive step: if n is even, add n and recurse on n-2
# - Use `range()` with a step of 2 for the iterative version

def sum_even_recursive(n):
	if n <= 1:
		return 0
	if n % 2 == 0:
		return n + sum_even_recursive(n - 2)
	else:
		return sum_even_recursive(n - 1)

def sum_even_iterative(n):
	return sum(i for i in range(2, n + 1, 2))

if __name__ == "__main__":
	n = 10
	print("Recursive:", sum_even_recursive(n))
	print("Iterative:", sum_even_iterative(n))