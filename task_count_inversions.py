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

def merge_and_count_inversions(left, right):
    result = []
    inversions = 0
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            # Count inversions: all remaining elements in left array form inversions
            inversions += len(left) - i
            j += 1
    
    # Add remaining elements
    result.extend(left[i:])
    result.extend(right[j:])
    return result, inversions

def count_inversions(arr):
    if len(arr) <= 1:
        return arr, 0
        
    # Divide array into two halves
    mid = len(arr) // 2
    left, left_inv = count_inversions(arr[:mid])
    right, right_inv = count_inversions(arr[mid:])
    
    # Merge and count split inversions
    merged, split_inv = merge_and_count_inversions(left, right)
    
    # Total inversions = left inversions + right inversions + split inversions
    return merged, left_inv + right_inv + split_inv

def count_inversions_wrapper(arr):
    _, inversions = count_inversions(arr)
    return inversions
