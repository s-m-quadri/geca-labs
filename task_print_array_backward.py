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


def print_reverse_recursive(arr, i=None):
	if i is None:
		i = len(arr) - 1
	if i < 0:
		print()
		return
	print(arr[i], end=' ' if i > 0 else '')
	print_reverse_recursive(arr, i - 1)


def print_reverse_iterative(arr):
	for idx in range(len(arr) - 1, -1, -1):
		end = ' ' if idx > 0 else ''
		print(arr[idx], end=end)
	print()


if __name__ == '__main__':
	example = [1, 2, 3, 4]
	print("Recursive reverse:")
	print_reverse_recursive(example)

	print("Iterative reverse:")
	print_reverse_iterative(example)

