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
# task_4.2.py
# Example: Find the minimum element in a list

def find_min(arr):
	if not arr:
		return None
	min_val = arr[0]
	for num in arr:
		if num < min_val:
			min_val = num
	return min_val

if __name__ == "__main__":
	arr = [3, 1, 4, 1, 5, 9, 2, 6, 5]
	print("Minimum element:", find_min(arr))
