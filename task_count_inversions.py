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
    inversions = 0

    # Merge while counting inversions
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
            inversions += (len(L) - i)  # all remaining elements in L are greater
        k += 1

    # Copy leftovers
    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1
    while j < len(R):
        arr[k] = R[j]
        j += 1
        k += 1

    return inversions


def merge_sort_and_count(arr, left, right):
    inversions = 0
    if left < right:
        mid = (left + right) // 2
        inversions += merge_sort_and_count(arr, left, mid)
        inversions += merge_sort_and_count(arr, mid+1, right)
        inversions += merge_and_count(arr, left, mid, right)
    return inversions


def count_inversions(arr):
    return merge_sort_and_count(arr, 0, len(arr)-1)



arr = [2, 4, 1, 3, 5]
print("Number of inversions:", count_inversions(arr))
