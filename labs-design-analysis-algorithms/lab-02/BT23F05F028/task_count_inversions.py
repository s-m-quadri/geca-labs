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

# Write your solution here
def count_inversions(arr):
    def merge_sort_and_count(arr):
        if len(arr) <= 1:
            return arr, 0

        mid = len(arr) // 2
        left, left_inv = merge_sort_and_count(arr[:mid])
        right, right_inv = merge_sort_and_count(arr[mid:])
        merged, split_inv = merge_and_count(left, right)

        return merged, left_inv + right_inv + split_inv

    def merge_and_count(left, right):
        merged = []
        i = j = inv_count = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
                inv_count += len(left) - i  # Count all remaining elements in left

        # Append remaining elements
        merged += left[i:]
        merged += right[j:]

        return merged, inv_count

    _, total_inversions = merge_sort_and_count(arr)
    return total_inversions

arr = [2, 4, 1, 3, 5]
print(count_inversions(arr))  # Output: 3