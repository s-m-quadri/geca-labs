# Task 4.3: Reverse a String
# ------------------------
# Write two functions to reverse a string:
# 1. reverse_recursive(s): Reverse the string using recursion.
# 2. reverse_iterative(s): Reverse the string using a loop.
#
# Input: string s
# Output: reversed string
#
# Example:
# Input: "hello"
# Output: "olleh"
#
# Bonus: Try solving without using Python slicing [::-1].
# task_4.3.py
# Example: Calculate the sum of elements in a list

def sum_elements(arr):
	total = 0
	for num in arr:
		total += num
	return total

if __name__ == "__main__":
	arr = [3, 1, 4, 1, 5, 9, 2, 6, 5]
	print("Sum of elements:", sum_elements(arr))
