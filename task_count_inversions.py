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
        left, left_inv = merge_sort(nums[:mid])
        right, right_inv = merge_sort(nums[mid:])

        merged, merge_inv = merge(left, right)
        total_inv = left_inv + right_inv + merge_inv

        return merged, total_inv

    def merge(left, right):
        result = []
        i = j = count = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
                count += len(left) - i  

        result.extend(left[i:])
        result.extend(right[j:])

        return result, count

    _, total_inversions = merge_sort(arr)
    return total_inversions


arr = [2, 4, 1, 3, 5]
print("Number of inversions:", count_inversions(arr))
