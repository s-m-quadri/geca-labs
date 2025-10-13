def count_occurrences(arr, target):
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

	first = find_first(arr, target)
	last = find_last(arr, target)
	if first == -1 or last == -1:
		return 0
	return last - first + 1

# Example usage
arr = [1, 2, 2, 2, 3, 4]
target = 2
print(count_occurrences(arr, target))
arr2 = [5, 5, 5, 5, 5]
target2 = 5
print(count_occurrences(arr2, target2))
