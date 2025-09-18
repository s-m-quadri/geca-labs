# -------------------------------------------
# TASK: Print Elements of Array in Reverse
# -------------------------------------------
# Write two functions:
#   1. print_reverse_recursive(arr): prints last to first using recursion
#   2. print_reverse_iterative(arr): prints using a loop
#
# Example:
#   Input: [1, 2, 3, 4]
#   Output: 4 3 2 1
#
# -------------------------------------------
# HINTS:
# - For recursion, start from last index: len(arr) - 1
# - Reduce index by 1 each call
# - For iteration, use a loop from end to start

def print_reverse_recursive(arr, i=None):
	if i is None:
		i = len(arr) - 1
	if i < 0:
		return
	print(arr[i])
	print_reverse_recursive(arr, i - 1)

def print_reverse_iterative(arr):
	for idx in range(len(arr) - 1, -1, -1):
		print(arr[idx])

# Example run
arr = [1, 2, 3, 4]
print_reverse_recursive(arr)
print_reverse_iterative(arr)
