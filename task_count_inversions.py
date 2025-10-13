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
    def merge_sort_and_count(nums):
        if len(nums) <= 1:
            return nums, 0

        mid = len(nums) // 2
        left, inv_left = merge_sort_and_count(nums[:mid])
        right, inv_right = merge_sort_and_count(nums[mid:])
        merged, inv_split = merge_and_count(left, right)

        total_inversions = inv_left + inv_right + inv_split
        return merged, total_inversions

    def merge_and_count(left, right):
        merged = []
        i = j = inversions = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                inversions += len(left) - i  # All remaining elements in left are > right[j]
                j += 1

        # Add remaining elements
        merged.extend(left[i:])
        merged.extend(right[j:])
        return merged, inversions

    _, total = merge_sort_and_count(arr)
    return total
