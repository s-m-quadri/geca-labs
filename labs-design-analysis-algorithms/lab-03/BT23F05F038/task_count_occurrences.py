# Puzzle / Learning focus:
# - You have a sorted array with repeated elements.
# - Count how many times a target number appears using binary search logic.
# - Consider how to find the first and last occurrence efficiently.
#
# Example test cases:
# Input: arr = [1, 2, 2, 2, 3, 4], target = 2
# Output: 3
#
# Input: arr = [5, 5, 5, 5, 5], target = 5
# Output: 5

def find_first(arr, target):
	left, right = 0, len(arr) - 1
	result = -1
	while left <= right:
		mid = (left + right) // 2
		if arr[mid] == target:
			result = mid
			right = mid - 1
		elif arr[mid] < target:
			left = mid + 1
		else:
			right = mid - 1
	return result

def find_last(arr, target):
	left, right = 0, len(arr) - 1
	result = -1
	while left <= right:
		mid = (left + right) // 2
		if arr[mid] == target:
			result = mid
			left = mid + 1
		elif arr[mid] < target:
			left = mid + 1
		else:
			right = mid - 1
	return result

def count_occurrences(arr, target):
	first = find_first(arr, target)
	if first == -1:
		return 0
	last = find_last(arr, target)
	return last - first + 1

# Example usage:
if __name__ == "__main__":
	arr1 = [1, 2, 2, 2, 3, 4]
	target1 = 2
	print(count_occurrences(arr1, target1))  # Output: 3

	arr2 = [5, 5, 5, 5, 5]
	target2 = 5
	print(count_occurrences(arr2, target2))  # Output: 5
