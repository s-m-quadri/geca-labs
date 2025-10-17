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
from typing import List, Tuple

def _merge_count(left: List[int], right: List[int]) -> Tuple[List[int], int]:
    """Merge two sorted lists and count cross inversions (left element > right element)."""
    merged = []
    i = j = 0
    inv_count = 0
    n_left, n_right = len(left), len(right)

    while i < n_left and j < n_right:
        # if left[i] <= right[j], no inversion with left[i]
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            # left[i] > right[j] => al
