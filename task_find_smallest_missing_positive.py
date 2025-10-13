# Puzzle / Learning focus:
# - Given a sorted array of positive numbers, find the smallest missing positive integer.
# - Use binary search thinking to locate the “gap” without checking every element.
# - Challenge: handle edge cases at the start and end of the array.
#
# Example test cases:
# Input: [1, 2, 3, 5, 6]
# Output: 4
#
# Input: [2, 3, 4, 5]
# Output: 1

def find_smallest_missing_positive(arr):
	n = len(arr)
	left, right = 0, n - 1
	# If the first element is not 1, then 1 is missing
	if n == 0 or arr[0] != 1:
		return 1
	# Binary search for the gap
	while left <= right:
		mid = (left + right) // 2
		# If arr[mid] == mid + 1, missing is to the right
		if arr[mid] == mid + 1:
			left = mid + 1
		else:
			right = mid - 1
	# The smallest missing is left + 1
	return left + 1

# Example usage:
if __name__ == "__main__":
	arr1 = [1, 2, 3, 5, 6]
	print(find_smallest_missing_positive(arr1))  # Output: 4

	arr2 = [2, 3, 4, 5]
	print(find_smallest_missing_positive(arr2))  # Output: 1
