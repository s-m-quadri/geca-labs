# Task 4.1: Factorial (Recursive vs Iterative)
# -----------------------------------------
# Write two functions:
# 1. factorial_recursive(n): Uses recursion to compute factorial of n.
# 2. factorial_iterative(n): Uses loops to compute factorial of n.
#
# Input: an integer n (n >= 0)
# Output: factorial of n (n!)
#
# Example:
# Input: 5
# Output: 120
#
# Hint: Start with the mathematical definition:
# factorial(n) = 1 if n == 0 else n * factorial(n-1)
# task_4.1.py
# Example: Find the maximum element in a list

def find_max(arr):
	if not arr:
		return None
	max_val = arr[0]
	for num in arr:
		if num > max_val:
			max_val = num
	return max_val

if __name__ == "__main__":
	arr = [3, 1, 4, 1, 5, 9, 2, 6, 5]
	print("Maximum element:", find_max(arr))
