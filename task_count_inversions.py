# Given an array of integers, count the number of inversions in the array.
# An inversion is a pair (i, j) such that i < j and arr[i] > arr[j].

# Example:
# Input: [2, 4, 1, 3, 5]
# Output: 3
# Explanation: The inversions are (2,1), (4,1), (4,3)

# INSTRUCTIONS:
# - Implement a function using Merge Sort modification to count inversions efficiently.
# - Target time complexity: O(n log n)
# - Do not use brute force O(n^2) method.

def count_inversions(arr):
	def merge_count(left, right):
		merged = []
		i = j = inv_count = 0
		while i < len(left) and j < len(right):
			if left[i] <= right[j]:
				merged.append(left[i])
				i += 1
			else:
				merged.append(right[j])
				inv_count += len(left) - i
				j += 1
		merged.extend(left[i:])
		merged.extend(right[j:])
		return merged, inv_count

	def sort_count(arr):
		if len(arr) <= 1:
			return arr, 0
		mid = len(arr) // 2
		left, inv_left = sort_count(arr[:mid])
		right, inv_right = sort_count(arr[mid:])
		merged, inv_split = merge_count(left, right)
		return merged, inv_left + inv_right + inv_split

	_, total_inversions = sort_count(arr)
	return total_inversions

# Example usage:
if __name__ == "__main__":
	arr = [2, 4, 1, 3, 5]
	print(count_inversions(arr))  # Output: 3

