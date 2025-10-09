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

#solution:
def find_smallest_missing_positive(arr):
	n = len(arr)
	left, right = 0, n - 1

	if n == 0 or arr[0] != 1:
		return 1
	# this is supposed to be the binary search part where it scans for the gap T_T
	while left <= right:
		mid = (left + right) // 2

		if arr[mid] == mid + 1:
			left = mid + 1
		else:
			right = mid - 1
	return left + 1

# Example (much needed):
if __name__ == "__main__":
	arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 10]
	print(find_smallest_missing_positive(arr1))  #i'd expect 9 as output

	arr2 = [1, 2, 3, 4, 6, 7]
	print(find_smallest_missing_positive(arr2))  #and here 5 as output
