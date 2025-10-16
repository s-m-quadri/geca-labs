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
def merge_and_count(arr, left, mid, right):
    # Temp arrays
    L = arr[left:mid+1]
    R = arr[mid+1:right+1]

    i = j = 0
    k = left
    inv_count = 0

    # Merge with inversion count
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
            inv_count += (len(L) - i)  # All remaining L[i:] form inversions
        k += 1

    # Copy remaining elements
    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1
    while j < len(R):
        arr[k] = R[j]
        j += 1
        k += 1

    return inv_count


def merge_sort_and_count(arr, left, right):
    inv_count = 0
    if left < right:
        mid = (left + right) // 2

        # Count inversions in left half
        inv_count += merge_sort_and_count(arr, left, mid)

        # Count inversions in right half
        inv_count += merge_sort_and_count(arr, mid + 1, right)

        # Count cross inversions during merge
        inv_count += merge_and_count(arr, left, mid, right)

    return inv_count


def count_inversions(arr):
    return merge_sort_and_count(arr, 0, len(arr) - 1)


# Example usage
arr = [2, 4, 1, 3, 5]
print("Number of inversions:", count_inversions(arr))
