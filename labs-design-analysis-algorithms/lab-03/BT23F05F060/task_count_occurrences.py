def find_first(arr, target):
	low, high = 0, len(arr) - 1
	result = -1
	while low <= high:
		mid = (low + high) // 2
		if arr[mid] == target:
			result = mid
			high = mid - 1
		elif arr[mid] < target:
			low = mid + 1
		else:
			high = mid - 1
	return result

def find_last(arr, target):
	low, high = 0, len(arr) - 1
	result = -1
	while low <= high:
		mid = (low + high) // 2
		if arr[mid] == target:
			result = mid
			low = mid + 1
		elif arr[mid] < target:
			low = mid + 1
		else:
			high = mid - 1
	return result

def count_occurrences(arr, target):
	first = find_first(arr, target)
	if first == -1:
		return 0
	last = find_last(arr, target)
	return last - first + 1


if __name__ == "__main__":
	arr1 = [1, 2, 2, 2, 3, 4]
	target1 = 2
	print(count_occurrences(arr1, target1))  # Output: 3

	arr2 = [5, 5, 5, 5, 5]
	target2 = 5
	print(count_occurrences(arr2, target2))  # Output: 5
