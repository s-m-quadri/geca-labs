
def find_smallest_missing_positive(arr):
	low, high = 0, len(arr) - 1
	while low <= high:
		mid = (low + high) // 2
		if arr[mid] == mid + 1:
			low = mid + 1
		else:
			high = mid - 1
	return low + 1

# Example test cases
if __name__ == "__main__":
	arr1 = [1, 2, 3, 5, 6]
	print(find_smallest_missing_positive(arr1))  # Output: 4

	arr2 = [2, 3, 4, 5]
	print(find_smallest_missing_positive(arr2))  # Output: 1
