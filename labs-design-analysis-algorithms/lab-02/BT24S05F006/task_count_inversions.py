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
    def merge_sort(arr):
        if len(arr) <= 1:
            return arr, 0

        mid = len(arr) // 2
        left, left_inv = merge_sort(arr[:mid])
        right, right_inv = merge_sort(arr[mid:])
        merged, split_inv = merge(left, right)

        return merged, left_inv + right_inv + split_inv

    def merge(left, right):
        merged = []
        i = j = 0
        inversions = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
                # All remaining elements in left are greater than right[j]
                inversions += len(left) - i  

        merged.extend(left[i:])
        merged.extend(right[j:])
        return merged, inversions

    _, total_inversions = merge_sort(arr)
    return total_inversions


# Example usage:
arr = [2, 4, 1, 3, 5]
print("Number of inversions:", count_inversions(arr))  # Output: 3
