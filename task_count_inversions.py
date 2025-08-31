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
    def merge_sort(arr, temp, left, right):
        inv_count = 0
        if left < right:
            mid = (left + right) // 2

            # Count inversions in left half
            inv_count += merge_sort(arr, temp, left, mid)

            # Count inversions in right half
            inv_count += merge_sort(arr, temp, mid + 1, right)

            # Count inversions during merge
            inv_count += merge(arr, temp, left, mid, right)
        return inv_count

    def merge(arr, temp, left, mid, right):
        i = left       # Left subarray index
        j = mid + 1    # Right subarray index
        k = left       # Temp array index
        inv_count = 0

        while i <= mid and j <= right:
            if arr[i] <= arr[j]:
                temp[k] = arr[i]
                i += 1
            else:
                temp[k] = arr[j]
                j += 1
                # All remaining elements in left subarray are greater → inversions
                inv_count += (mid - i + 1)
            k += 1

        # Copy remaining elements
        while i <= mid:
            temp[k] = arr[i]
            i += 1
            k += 1
        while j <= right:
            temp[k] = arr[j]
            j += 1
            k += 1

        # Copy back to original array
        for idx in range(left, right + 1):
            arr[idx] = temp[idx]

        return inv_count

    n = len(arr)
    temp = [0] * n
    return merge_sort(arr, temp, 0, n - 1)


# Example usage:
arr = [2, 4, 1, 3, 5]
print("Number of inversions:", count_inversions(arr))  
# Output: 3
