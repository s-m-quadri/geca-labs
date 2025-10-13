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
        left, inv_left = merge_sort_and_count(arr[:mid])
        right, inv_right = merge_sort_and_count(arr[mid:])
        merged, inv_merge = merge_and_count(left, right)

        total_inversions = inv_left + inv_right + inv_merge
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
                inversions += len(left) - i
                j += 1

        merged.extend(left[i:])
        merged.extend(right[j:])
        return merged, inversions

    _, count = merge_sort_and_count(arr)
    return count

# Example usage
arr = [2, 4, 1, 3, 5]
print("Inversion count:", count_inversions(arr))  # Output: 3
