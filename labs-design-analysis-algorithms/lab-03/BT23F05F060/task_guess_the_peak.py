
def find_peak(arr):
	low, high = 0, len(arr) - 1
	while low < high:
		mid = (low + high) // 2
		if arr[mid] < arr[mid + 1]:
			low = mid + 1
		else:
			high = mid
	return arr[low]

# Example test cases
if __name__ == "__main__":
	arr1 = [1, 3, 7, 12, 9, 5, 2]
	print(find_peak(arr1))  # Output: 12

	arr2 = [0, 2, 4, 6, 3, 1]
	print(find_peak(arr2))  # Output: 6
