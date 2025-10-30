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

def _merge_and_count(left, right):
    merged = []
    i = j = inv_count = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            inv_count += len(left) - i  # Count inversions
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged, inv_count

def _sort_and_count(arr):
    if len(arr) <= 1:
        return arr, 0
    mid = len(arr) // 2
    left, left_inv = _sort_and_count(arr[:mid])
    right, right_inv = _sort_and_count(arr[mid:])
    merged, merge_inv = _merge_and_count(left, right)
    return merged, left_inv + right_inv + merge_inv

def count_inversions(arr):
    """Return the number of inversions in the array."""
    _, inv_count = _sort_and_count(arr)
    return inv_count

if __name__ == "__main__":
    # Example usage
    examples = [
        [2, 4, 1, 3, 5],
        [5, 4, 3, 2, 1],
        [1, 2, 3, 4, 5],
        [],
        [1]
    ]
    for example in examples:
        print(f"Array: {example} -> Inversions: {count_inversions(example)}")

