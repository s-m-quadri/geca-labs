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


def merge(arr, temp, left, mid, right):
    i = left        # Left subarray pointer
    j = mid + 1     # Right subarray pointer
    k = left        # Temp array pointer
    inv_count = 0

    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp[k] = arr[i]
            i += 1
        else:
            temp[k] = arr[j]
            inv_count += (mid - i + 1)  # All remaining elements in left form an inversion
            j += 1
        k += 1

   
    while i <= mid:
        temp[k] = arr[i]
        i += 1
        k += 1

    # Copy remaining elements from right (if any)
    while j <= right:
        temp[k] = arr[j]
        j += 1
        k += 1

    # Copy merged elements back into original array
    for p in range(left, right + 1):
        arr[p] = temp[p]

    return inv_count


def merge_sort(arr, temp, left, right):
    inv_count = 0
    if left < right:
        mid = (left + right) // 2

        # Count inversions in left half
        inv_count += merge_sort(arr, temp, left, mid)

        # Count inversions in right half
        inv_count += merge_sort(arr, temp, mid + 1, right)

        # Count split inversions while merging
        inv_count += merge(arr, temp, left, mid, right)

    return inv_count


def count_inversions(arr):
    temp = arr.copy()  # Temporary array for merging
    return merge_sort(arr, temp, 0, len(arr) - 1)
    list1 = [1, 3, 5]
    
list2 = [2, 4, 6]
print(merge_sorted_lists(list1, list2))

