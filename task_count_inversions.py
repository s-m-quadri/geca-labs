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

# -------------------------------------------
# TASK: Count Inversions in an Array (O(n log n))
# -------------------------------------------

def count_inversions(arr):
    # Helper function: merge sort with inversion counting
    def merge_sort(nums):
        if len(nums) <= 1:
            return nums, 0  # (sorted array, inversion count)
        
        mid = len(nums) // 2
        left, left_inv = merge_sort(nums[:mid])
        right, right_inv = merge_sort(nums[mid:])
        
        merged, cross_inv = merge(left, right)
        return merged, left_inv + right_inv + cross_inv

    # Merge two halves and count cross-inversions
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
                inv_count += len(left) - i  # All remaining left elements form inversions
        
        merged.extend(left[i:])
        merged.extend(right[j:])
        
        return merged, inv_count

    # Run merge sort and return total inversions
    _, total_inversions = merge_sort(arr)
    return total_inversions


# Example test
arr = [2, 4, 1, 3, 5]
print("Array:", arr)
print("Inversion Count:", count_inversions(arr))

