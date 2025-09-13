def guess_the_peak(arr):
	low, high = 0, len(arr) - 1
	while low < high:
		mid = (low + high) // 2
		if arr[mid] < arr[mid + 1]:
			low = mid + 1
		else:
			high = mid
	return arr[low]

# Example usage
arr = [1, 3, 7, 12, 9, 5, 2]
print(guess_the_peak(arr))
arr2 = [0, 2, 4, 6, 3, 1]
print(guess_the_peak(arr2))
