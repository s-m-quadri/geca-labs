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
# TASK: Count Inversions using Merge Sort
# -------------------------------------------

def count_inversions(arr):
    # Helper function: merge two halves and count cross inversions
    def merge_and_count(left, right):
        i = j = 0
        merged = []
        inversions = 0

        # Merge with inversion counting
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
                # All remaining elements in left[i:] form inversions
                inversions += len(left) - i
        
        # Add remaining elements
        merged.extend(left[i:])
        merged.extend(right[j:])
        return merged, inversions

    # Recursive divide and conquer
    def sort_and_count(sub_arr):
        if len(sub_arr) <= 1:
            return sub_arr, 0
        
        mid = len(sub_arr) // 2
        left, left_inv = sort_and_count(sub_arr[:mid])
        right, right_inv = sort_and_count(sub_arr[mid:])
        merged, cross_inv = merge_and_count(left, right)
        
        # Total inversions = left + right + cross
        return merged, left_inv + right_inv + cross_inv

    # Call recursive function and return inversion count
    _, total_inversions = sort_and_count(arr)
    return total_inversions


# -------------------------------------------
# Example Usage
# -------------------------------------------
arr = [2, 4, 1, 3, 5]
print("Input:", arr)
print("Number of inversions:", count_inversions(arr))
