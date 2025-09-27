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
    def merge_sort(nums):
        if len(nums) <= 1:
            return nums, 0

        mid = len(nums) // 2
        left, inv_left = merge_sort(nums[:mid])
        right, inv_right = merge_sort(nums[mid:])
        merged, inv_split = merge(left, right)

        return merged, inv_left + inv_right + inv_split

    def merge(left, right):
        i = j = inv_count = 0
        merged = []
        
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
                # All remaining elements in left are greater than right[j]
                inv_count += len(left) - i

        merged.extend(left[i:])
        merged.extend(right[j:])
        return merged, inv_count

    _, total_inversions = merge_sort(arr)
    return total_inversions


# Example Usage
arr = [2, 4, 1, 3, 5]
print("Number of inversions:", count_inversions(arr))  # Output: 3

